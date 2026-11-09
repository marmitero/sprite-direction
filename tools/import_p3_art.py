"""P3 artistic source importer. Reads genuinely illustrated sprite cells, never draws geometry.

Input: original 8-view idle source sheet, 8 columns of 40x52.
Source column order is S, SE, E, NE, N, NW, W, SW.
Output: one authored image per facing (idle frame 000), run through P2.
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

def import_art(source:Path, output:Path):
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
    output.mkdir(parents=True,exist_ok=True)
    with TemporaryDirectory() as tmp:
        tmp=Path(tmp)
        for i,d in enumerate(COL_TO_DIR):
            folder=tmp/"idle"/d
            folder.mkdir(parents=True)
            frame=sheet.crop((i*CELL_W,0,(i+1)*CELL_W,CELL_H))
            frame.save(folder/"000.png")
        result=build(tmp,output,"shared_humanoid_art_v2",fps=10,
                     atlas_size=256,padding=3,make_gif=False)
    check=validate(output,"shared_humanoid_art_v2")
    found={x["direction"] for x in result["frames"]}
    if found!=set(DIRECTIONS) or len(result["frames"])!=8:
        raise ValueError("8 distinct direction frames are required")
    manifest={
      "phase":"P3-ART-REVISION",
      "status":"artistic_idle_direction_pilot_not_finished",
      "character":"shared_humanoid_art_v2",
      "art_source":str(source),
      "original_reference":"P1 approved moodboards",
      "provenance":"8 illustrations separated from a newly generated concept sheet and manually background-keyed",
      "processing":"cell extraction + RGBA + P2 atlas, no geometric redraw or interpolation",
      "source_sheet_dimensions":[320,52],
      "source_view_order":list(COL_TO_DIR),
      "runtime_direction_order":list(DIRECTIONS),
      "frame_count":8,
      "animation":"idle",
      "frames_per_direction":1,
      "completed_components":["artistic eight-view reference images","RGBA atlas and JSON"],
      "uncompleted_components":["frame-by-frame idle animation","walk animation","equipment overlays in eight directions","dynamic occlusion","per-frame anchor verification","manual style QA"],
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
    print(json.dumps({"status":"IMPORTED_ART_SOURCE","frames":r["frame_count"],"directions":len(r["runtime_direction_order"])}))
