#!/usr/bin/env python3
"""Sprite Direction P2: deterministic RGBA frame -> trimmed atlas + JSON + GIF.

Input convention: <input>/<animation>/<direction>/<000.png...>.
For stationary NPCs, use 'fixed' as direction. All frame numbers must be consecutive.
Requires Pillow >= 10.0. No artist-generated frames are changed or interpolated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

DIRECTIONS = ("N", "NE", "E", "SE", "S", "SW", "W", "NW")
FRAME_RE = re.compile(r"^\d+\.png$", re.IGNORECASE)


def fail(message):
    raise ValueError(message)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


@dataclass
class SourceFrame:
    animation: str
    direction: str
    index: int
    path: Path
    source_size: tuple[int, int]
    crop_box: tuple[int, int, int, int]
    image: Image.Image
    empty: bool


def _read_frames(root: Path):
    if not root.is_dir():
        fail(f"Input directory not found: {root}")
    items = []
    for animation_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for direction_dir in sorted((p for p in animation_dir.iterdir() if p.is_dir()),
                                    key=lambda p: (DIRECTIONS.index(p.name) if p.name in DIRECTIONS else 8, p.name)):
            direction = direction_dir.name
            if direction not in DIRECTIONS and direction != "fixed":
                fail(f"Invalid direction '{direction}': use {DIRECTIONS} or 'fixed'")
            files = sorted((p for p in direction_dir.iterdir() if p.is_file()), key=lambda p: p.name)
            if not files:
                fail(f"Empty animation direction: {direction_dir}")
            if any(not FRAME_RE.fullmatch(p.name) for p in files):
                fail(f"Only numeric .png frames permitted: {direction_dir}")
            indices = [int(p.stem) for p in files]
            if len(set(indices)) != len(indices) or indices != list(range(len(indices))):
                fail(f"Frame numbers must start at 0 and be consecutive: {direction_dir}")
            dimensions = set()
            for i, p in zip(indices, files):
                with Image.open(p) as raw:
                    if raw.format != "PNG" or raw.mode != "RGBA":
                        fail(f"Frame must be PNG RGBA, not {raw.format}/{raw.mode}: {p}")
                    img = raw.copy()
                if min(img.size) <= 0:
                    fail(f"Invalid image dimensions: {p}")
                dimensions.add(img.size)
                bbox = img.getchannel("A").getbbox()
                empty = bbox is None
                if empty:
                    bbox = (0, 0, 1, 1)
                    cropped = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
                else:
                    cropped = img.crop(bbox)
                items.append(SourceFrame(animation_dir.name, direction, i, p, img.size, bbox, cropped, empty))
            if len(dimensions) != 1:
                fail(f"Frames in one animation/direction must have the same source canvas: {direction_dir}")
    if not items:
        fail(f"No animation/direction PNG files found under {root}")
    return items


def _pack(frames, atlas_size, padding):
    """Deterministic shelf packer. Rects are in content pixels, not padded pixels."""
    pages, placements = [], []
    atlas = Image.new("RGBA", (atlas_size, atlas_size), (0, 0, 0, 0))
    x, y, shelf_h = padding, padding, 0
    for frame in frames:
        w, h = frame.image.size
        if w + 2 * padding > atlas_size or h + 2 * padding > atlas_size:
            fail(f"Frame too large for atlas {atlas_size}: {frame.path} ({w}x{h})")
        if x + w + padding > atlas_size:
            x = padding
            y += shelf_h + padding * 2
            shelf_h = 0
        if y + h + padding > atlas_size:
            pages.append(atlas)
            atlas = Image.new("RGBA", (atlas_size, atlas_size), (0, 0, 0, 0))
            x, y, shelf_h = padding, padding, 0
        atlas.alpha_composite(frame.image, (x, y))
        # Extrude content boundaries into the padded margin: preserves color values
        # and avoids sampling unrelated sprite cells when scaling in a renderer.
        for off in range(1, padding + 1):
            atlas.paste(frame.image.crop((0, 0, 1, h)), (x - off, y))
            atlas.paste(frame.image.crop((w - 1, 0, w, h)), (x + w - 1 + off, y))
            atlas.paste(frame.image.crop((0, 0, w, 1)), (x, y - off))
            atlas.paste(frame.image.crop((0, h - 1, w, h)), (x, y + h - 1 + off))
        for corner, color in (((x - 1, y - 1), frame.image.getpixel((0, 0))),
                              ((x + w, y - 1), frame.image.getpixel((w - 1, 0))),
                              ((x - 1, y + h), frame.image.getpixel((0, h - 1))),
                              ((x + w, y + h), frame.image.getpixel((w - 1, h - 1)))):
            for dx in range(padding):
                for dy in range(padding):
                    cx = corner[0] - dx if corner[0] < x else corner[0] + dx
                    cy = corner[1] - dy if corner[1] < y else corner[1] + dy
                    atlas.putpixel((cx, cy), color)
        placements.append((len(pages), x, y))
        x += w + padding * 2
        shelf_h = max(shelf_h, h)
    pages.append(atlas)
    return pages, placements


def build(input_dir, output_dir, asset_id, fps=12, loop=True, atlas_size=1024, padding=2,
          make_gif=False):
    if not re.fullmatch(r"[a-z0-9][a-z0-9_-]*", asset_id):
        fail("asset-id must use lowercase ASCII letters, digits, _ or -")
    if not (1 <= fps <= 60):
        fail("fps must be 1..60")
    if atlas_size < 32 or atlas_size > 8192 or atlas_size & (atlas_size - 1):
        fail("atlas-size must be power of 2 between 32 and 8192")
    if not (2 <= padding <= 16):
        fail("padding must be 2..16")
    root = Path(input_dir).resolve()
    out = Path(output_dir).resolve()
    if out == root or root in out.parents:
        fail("output directory cannot be the input directory or inside it")
    frames = _read_frames(root)
    pages, placements = _pack(frames, atlas_size, padding)
    out.mkdir(parents=True, exist_ok=True)
    atlas_paths = []
    for i, page in enumerate(pages):
        path = out / f"{asset_id}_atlas_{i:03d}.png"
        page.save(path, optimize=False)
        atlas_paths.append(path)
    entries = []
    duration = round(1000 / fps)
    for f, (page, x, y) in zip(frames, placements):
        left, top, right, bottom = f.crop_box
        sw, sh = f.source_size
        entries.append({
            "id": f"{f.animation}/{f.direction}/{f.index:03d}",
            "animation": f.animation,
            "direction": f.direction,
            "index": f.index,
            "atlas": page,
            "frame": {"x": x, "y": y, "w": right - left, "h": bottom - top},
            "source_size": {"w": sw, "h": sh},
            "sprite_source_size": {"x": left, "y": top, "w": right - left, "h": bottom - top},
            "pivot": {"x": sw // 2, "y": sh - 1},
            "duration_ms": duration,
            "empty": f.empty,
            "sha256_source": digest(f.path),
            "events": [],
        })
    meta = {
        "schema_version": "1.0",
        "asset_id": asset_id,
        "art_style": "sprite-direction-p1-approved",
        "texture_filter": "nearest",
        "pixel_format": "RGBA",
        "direction_order": list(DIRECTIONS),
        "fps": fps,
        "loop": loop,
        "atlas_size": atlas_size,
        "padding": padding,
        "atlases": [{"file": p.name, "width": atlas_size, "height": atlas_size,
                     "sha256": digest(p)} for p in atlas_paths],
        "frames": entries,
    }
    (out / f"{asset_id}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
                                            encoding="utf-8")
    if make_gif:
        for animation, direction in sorted(set((f.animation, f.direction) for f in frames)):
            subset = [f for f in frames if (f.animation, f.direction) == (animation, direction)]
            imgs = []
            for f in subset:
                full = Image.new("RGBA", f.source_size, (0, 0, 0, 0))
                full.alpha_composite(f.image, f.crop_box[:2])
                imgs.append(full)
            # GIF is for human inspection, never a replacement for source RGBA.
            imgs[0].save(out / f"{asset_id}_{animation}_{direction}.gif",
                         save_all=True, append_images=imgs[1:], duration=duration,
                         loop=0 if loop else 1, disposal=2, optimize=False)
    return meta


def validate(output_dir, asset_id):
    out = Path(output_dir)
    meta_path = out / f"{asset_id}.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    if meta.get("schema_version") != "1.0" or meta.get("asset_id") != asset_id:
        fail("Invalid schema or asset id")
    atlases = []
    for a in meta["atlases"]:
        p = out / a["file"]
        if p.name != a["file"] or digest(p) != a["sha256"]:
            fail(f"Missing or modified atlas: {a['file']}")
        with Image.open(p) as img:
            if img.mode != "RGBA" or img.size != (a["width"], a["height"]):
                fail(f"Bad atlas mode/dimensions: {p}")
            atlases.append(img.copy())
    ids, grouped = set(), {}
    occupied = [[] for _ in atlases]
    for f in meta["frames"]:
        if f["id"] in ids:
            fail("Duplicate frame ID: " + f["id"])
        ids.add(f["id"])
        index = f["atlas"]
        if not isinstance(index, int) or not 0 <= index < len(atlases):
            fail("Invalid atlas index")
        x, y, w, h = (f["frame"][k] for k in ("x", "y", "w", "h"))
        aw, ah = atlases[index].size
        pad = meta["padding"]
        if not (w > 0 and h > 0 and x >= pad and y >= pad and x + w + pad <= aw and y + h + pad <= ah):
            fail("Atlas rect out of bounds: " + f["id"])
        for ox, oy, ow, oh in occupied[index]:
            if x < ox + ow + 2 * pad and x + w + 2 * pad > ox and y < oy + oh + 2 * pad and y + h + 2 * pad > oy:
                fail("Atlas rects overlap/padding violation: " + f["id"])
        occupied[index].append((x, y, w, h))
        ss, sp = f["source_size"], f["sprite_source_size"]
        if not (sp["w"] == w and sp["h"] == h and 0 <= sp["x"] <= ss["w"] - w
                and 0 <= sp["y"] <= ss["h"] - h):
            fail("Trim/source-size mismatch: " + f["id"])
        if f["direction"] not in DIRECTIONS and f["direction"] != "fixed":
            fail("Invalid direction")
        if f["duration_ms"] <= 0:
            fail("Non-positive duration")
        grouped.setdefault((f["animation"], f["direction"]), []).append(f["index"])
    for key, indices in grouped.items():
        if sorted(indices) != list(range(len(indices))):
            fail(f"Missing or duplicate frame numbers in {key}")
    return {"asset_id": asset_id, "frames": len(ids), "atlases": len(atlases),
            "animations": len(grouped), "status": "PASS"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("--input", required=True)
    b.add_argument("--output", required=True)
    b.add_argument("--asset", required=True)
    b.add_argument("--fps", type=int, default=12)
    b.add_argument("--atlas-size", type=int, default=1024)
    b.add_argument("--padding", type=int, default=2)
    b.add_argument("--no-loop", action="store_true")
    b.add_argument("--gif", action="store_true")
    v = sub.add_parser("validate")
    v.add_argument("--output", required=True)
    v.add_argument("--asset", required=True)
    args = parser.parse_args()
    if args.command == "build":
        result = build(args.input, args.output, args.asset, args.fps, not args.no_loop,
                       args.atlas_size, args.padding, args.gif)
        print(json.dumps({"status": "BUILT", "asset_id": result["asset_id"],
                          "frames": len(result["frames"]), "atlases": len(result["atlases"])}))
        print(json.dumps(validate(args.output, args.asset)))
    else:
        print(json.dumps(validate(args.output, args.asset)))


if __name__ == "__main__":
    main()
