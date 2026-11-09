"""P3 artistic source importer. Reads genuinely illustrated sprite cells, never draws geometry.

Input: original 8-view idle source sheet, 8 columns of 40x52.
Source column order is S, SE, E, NE, N, NW, W, SW.
Output: one authored image per facing for idle and a distinct walk pose reference, both through P2.
No fabricated extra frames; walk/gear require individual authoring and validation.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from PIL import Image
from tools.sprite_pipeline import build, validate, DIRECTIONS

COL_TO_DIR=("S","SE","E","NE","N","NW","W","SW")
CELL_W,CELL_H=40,52

def import_equipped_walk_se(source:Path,output:Path):
    """Import eight illustrated, equipped SE walk frames as an isolated reference.

    Do NOT merge these baked-in armored frames with the modular unarmored base.
    """
    with Image.open(source) as raw:
        if raw.format!="PNG": raise ValueError("Equipped walk source must be PNG")
        sheet=raw.convert("RGBA")
    if sheet.size!=(8*40,52):
        raise ValueError(f"Expected 320x52 walk sheet, got {sheet.size}")
    with TemporaryDirectory() as td:
        folder=Path(td)/"walk"/"SE"
        folder.mkdir(parents=True)
        for i in range(8):
            f=sheet.crop((i*40,0,(i+1)*40,52))
            if f.getchannel("A").getbbox() is None:
                raise ValueError(f"Empty equipped walk frame {i}")
            f.save(folder/f"{i:03d}.png")
        result=build(Path(td),output,"humanoid_equipped_walk_se_reference",
                     fps=8,atlas_size=256,padding=3,make_gif=True)
    check=validate(output,"humanoid_equipped_walk_se_reference")
    if len(result["frames"])!=8:raise ValueError("Eight walk frames required")
    return {"status":"reference_only","frames":8,"validation":check}

def import_art(source:Path, output:Path):
    walk_source=source.with_name("walk_8_directions_reference.png")
    if not source.is_file():
        raise FileNotFoundError(f"Art source not found: {source}")
    with Image.open(source) as raw:
        if raw.format!="PNG": raise ValueError("Input must be PNG")
        sheet=raw.convert("RGBA")
    if sheet.size!=(8*CELL_W,CELL_H):
        raise ValueError(f"Expected illustrated 8-view source {8*CELL_W}x{CELL_H}, got {sheet.size}")
    for i in range(8):
        img=sheet.crop((i*CELL_W,0,(i+1)*CELL_W,CELL_H))
        if not img.getchannel("A").getbbox():
            raise ValueError(f"Empty art cell {i}")
        if img.getextrema()[3][0]==255:
            raise ValueError(f"Cell lacks transparency {i}")
    with Image.open(walk_source) as walk_raw:
        if walk_raw.format!="PNG": raise ValueError("Walk reference must be PNG")
        walk_sheet=walk_raw.convert("RGBA")
    if walk_sheet.size!=(8*CELL_W,CELL_H):
        raise ValueError("Walk reference must have 8 cells of 40x52")
    output.mkdir(parents=True,exist_ok=True)
    with TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        for action,art in (("idle",sheet),("walk_pose",walk_sheet)):
            for i,d in enumerate(COL_TO_DIR):
                folder=tmp/action/d
                folder.mkdir(parents=True)
                frame=art.crop((i*CELL_W,0,(i+1)*CELL_W,CELL_H))
                frame.save(folder/"000.png")
        result=build(tmp,output,"shared_humanoid_art_v2",fps=10,
                     atlas_size=256,padding=3,make_gif=False)
    check=validate(output,"shared_humanoid_art_v2")
    found={x["direction"] for x in result["frames"]}
    if found!=set(DIRECTIONS) or len(result["frames"])!=16:
        raise ValueError("8 directions with two distinct pose sets required")
    manifest={
      "phase":"P3-ART-REVISION",
      "status":"artistic_idle_and_walk_pose_references_not_animations",
      "character":"shared_humanoid_art_v2",
      "art_source":str(source),
      "original_reference":"P1 approved moodboards",
      "provenance":"8 illustrations separated from a newly generated concept sheet and manually background-keyed",
      "processing":"cell extraction + RGBA + P2 atlas, no geometric redraw or interpolation",
      "source_sheet_dimensions":[320,52],
      "source_view_order":list(COL_TO_DIR),
      "runtime_direction_order":list(DIRECTIONS),
      "frame_count":16,
      "animations":["idle","walk_pose"],
      "frames_per_direction_per_pose":1,
      "completed_components":["artistic eight-view idle pose","artistic eight-view walk pose reference","RGBA atlas and JSON"],
      "uncompleted_components":["frame-by-frame idle animation","full walk animation","equipment overlays in eight directions","dynamic occlusion","per-frame anchor verification","manual style QA"],
      "p4_authorized":False,
      "test_status":check,
    }
    (output/"art_v2_manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return manifest

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--source",default="assets/characters/classes/shared_humanoid_art_v2/idle_8_directions.png")
    ap.add_argument("--output",default="assets/characters/classes/shared_humanoid_art_v2/runtime")
    args=ap.parse_args()
    r=import_art(Path(args.source),Path(args.output))
    equipped_source=Path(args.source).with_name("walk_SE_8_frame_art_reference.png")
    equipped=import_equipped_walk_se(equipped_source,Path(args.output)/"equipped_walk_se")
    print(json.dumps({"status":"IMPORTED_ART_SOURCE","illustrated_pose_frames":r["frame_count"],"directions":len(r["runtime_direction_order"]),"equipped_walk_se_frames":equipped["frames"]}))
