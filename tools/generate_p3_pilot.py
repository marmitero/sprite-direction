#!/usr/bin/env python3
"""P3 art pilot: original authored procedural pixel clusters, 8 directions.

Generates actual PNG layers and invokes the tested P2 atlas pipeline. This is a
first *technical/artistic pilot*, not an approved full production class sheet.
All pieces share a 64x72 canvas, origin at (32,71), action, direction and index.
No scaling, vector rendering, filtering or AI-produced frame interpolation.
"""
from __future__ import annotations
import argparse
import json
import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw
from tools.sprite_pipeline import DIRECTIONS, build, validate

W, H = 64, 72
FRAMES = 8
FACING = {
    "N": (0,-1), "NE": (1,-1), "E": (1,0), "SE": (1,1),
    "S": (0,1), "SW": (-1,1), "W": (-1,0), "NW": (-1,-1),
}
INK=(23,22,34,255)
SKIN=(209,151,112,255)
SKIN_SHADOW=(144,89,76,255)
SKIN_HI=(245,189,135,255)
CLOTH=(104,78,65,255)
CLOTH_SHADOW=(64,52,57,255)
METAL=(105,120,138,255)
METAL_DARK=(48,57,75,255)
METAL_HI=(182,198,205,255)
GOLD=(221,166,76,255)
HAIR=(62,51,64,255)
HAIR_HI=(118,91,103,255)
RED=(125,54,63,255)
RED_HI=(190,87,80,255)
BOOTS=(75,53,52,255)
BOOTS_HI=(139,92,63,255)
ALPHA=(0,0,0,0)
LAYERS=("body","hair","chest","hands","feet","main_hand","off_hand")
SLOTS=LAYERS[1:]

def R(draw, box, fill, outline=INK, width=1):
    draw.rectangle(tuple(map(int, box)), fill=fill, outline=outline, width=width)
def E(draw, box, fill, outline=INK):
    draw.ellipse(tuple(map(int, box)), fill=fill, outline=outline)
def P(draw, coords, fill, outline=INK):
    draw.polygon(coords, fill=fill)
    if outline:
        draw.line(coords+[coords[0]], fill=outline, width=1)

def draw_layer(layer, direction, animation, i):
    dx, dy = FACING[direction]
    phase=math.sin(2*math.pi*i/FRAMES) if animation=="walk" else 0.0
    step=int(round(phase*3)) if animation=="walk" else 0
    bob=int(round(abs(phase))) if animation=="walk" else (1 if i in (3,4) else 0)
    hx=32+dx*2
    hy=23+bob
    # Walking feet counter-rotate, always same world pivot.
    la=step
    ra=-step
    im=Image.new("RGBA",(W,H),ALPHA)
    d=ImageDraw.Draw(im)
    front=dy>=0
    side=dx!=0
    if layer=="body":
        # Two distinct bare feet/legs, opaquely clothed undergarment.
        R(d,(26+la,51,30+la,61),SKIN_SHADOW)
        R(d,(34+ra,51,38+ra,61),SKIN)
        E(d,(23+la,59,32+la,65),SKIN)
        E(d,(33+ra,59,42+ra,65),SKIN_SHADOW)
        R(d,(25,36+bob,39,52+bob),CLOTH)
        R(d,(26,42+bob,38,49+bob),CLOTH_SHADOW,outline=None) if False else None
        R(d,(27,43+bob,37,49+bob),CLOTH_SHADOW)
        R(d,(25,50+bob,39,54+bob),CLOTH_SHADOW)
        R(d,(21+dx,38+bob,25+dx,49+bob),SKIN_SHADOW)
        R(d,(39+dx,38+bob,43+dx,49+bob),SKIN)
        E(d,(19+dx,47+bob,25+dx,53+bob),SKIN_SHADOW)
        E(d,(39+dx,47+bob,45+dx,53+bob),SKIN)
        E(d,(22+dx,14+bob,42+dx,36+bob),SKIN_SHADOW)
        E(d,(24+dx,14+bob,41+dx,34+bob),SKIN)
        R(d,(25+dx,17+bob,32+dx,19+bob),SKIN_HI,outline=SKIN_HI)
        if front:
            eyes=[hx-5,hx+4] if not side else ([hx+4] if dx>0 else [hx-4])
            for ex in eyes:
                R(d,(ex,hy+1,ex+1,hy+3),INK,outline=INK)
            R(d,(hx,hy+7,hx+2,hy+7),SKIN_SHADOW,outline=SKIN_SHADOW)
        if dy==0:
            ex=hx+7*dx
            R(d,(ex,hy+1,ex+1,hy+3),INK,outline=INK)
        # highlight shoulders/skin
        R(d,(22+dx,39+bob,23+dx,45+bob),SKIN_HI,outline=SKIN_HI)
        R(d,(40+dx,39+bob,41+dx,44+bob),SKIN_HI,outline=SKIN_HI)
    elif layer=="hair":
        # Hair silhouette shifts to preserve side/rear head coverage.
        E(d,(21+dx,11+bob,43+dx,28+bob),HAIR)
        P(d,[(22+dx,23+bob),(20+dx,30+bob),(27+dx,27+bob),
              (29+dx,23+bob)],HAIR)
        P(d,[(38+dx,23+bob),(44+dx,30+bob),(41+dx,20+bob)],HAIR)
        for sx,sy in [(-7,0),(-3,-3),(2,-2),(7,1)]:
            R(d,(hx+sx,15+bob+sy,hx+sx+3,17+bob+sy),HAIR_HI,outline=HAIR_HI)
        if front:
            # front hairline; leave facial pixels exposed
            P(d,[(23+dx,18+bob),(31+dx,20+bob),(35+dx,17+bob),
                  (42+dx,20+bob),(40+dx,15+bob),(26+dx,14+bob)],HAIR)
        elif dy<0:
            R(d,(23+dx,25+bob,40+dx,31+bob),HAIR)
            R(d,(26+dx,27+bob,37+dx,28+bob),HAIR_HI,outline=HAIR_HI)
    elif layer=="chest":
        # Layered tunic / first light armour. Does not permanently alter body.
        P(d,[(25,35+bob),(32,38+bob),(39,35+bob),(41,51+bob),
              (33,54+bob),(23,51+bob)],METAL_DARK)
        P(d,[(27,37+bob),(32,39+bob),(38,37+bob),
              (38,50+bob),(32,52+bob),(26,50+bob)],METAL)
        R(d,(28,39+bob,35,40+bob),METAL_HI,outline=METAL_HI)
        R(d,(26,48+bob,39,50+bob),RED)
        R(d,(31,46+bob,33,53+bob),GOLD)
        P(d,[(23+dx,36+bob),(28+dx,38+bob),(27+dx,44+bob),
              (20+dx,43+bob)],METAL)
        P(d,[(37+dx,38+bob),(42+dx,36+bob),(45+dx,43+bob),
              (38+dx,44+bob)],METAL_DARK)
        R(d,(23+dx,38+bob,25+dx,39+bob),METAL_HI,outline=METAL_HI)
    elif layer=="hands":
        R(d,(20+dx,45+bob,25+dx,51+bob),METAL_DARK)
        R(d,(39+dx,45+bob,44+dx,51+bob),METAL_DARK)
        R(d,(22+dx,46+bob,24+dx,49+bob),METAL_HI,outline=METAL_HI)
        R(d,(40+dx,46+bob,42+dx,49+bob),METAL_HI,outline=METAL_HI)
    elif layer=="feet":
        for footshift,x in ((la,22),(ra,33)):
            R(d,(x+footshift,56,x+footshift+9,63),BOOTS)
            R(d,(x+footshift,60,x+footshift+10,65),BOOTS)
            R(d,(x+footshift+2,61,x+footshift+7,62),BOOTS_HI,outline=BOOTS_HI)
            R(d,(x+footshift+1,56,x+footshift+8,57),METAL,outline=METAL)
    elif layer=="main_hand":
        # Sword in right hand; diagonal/elevation matches facing, no flips of art.
        x=43+dx+int(round(step*0.2))
        y=48+bob
        sx=dx if dx else 1
        blade_end=(x+sx*12,y-14 if dy<0 else y-8)
        d.line([(x,y),(x+sx*4,y-4),blade_end],fill=INK,width=5)
        d.line([(x,y),(x+sx*4,y-4),blade_end],fill=METAL,width=3)
        d.line([(x+sx*4,y-5),blade_end],fill=METAL_HI,width=1)
        d.line([(x-3,y-4),(x+4,y+2)],fill=GOLD,width=3)
        R(d,(x-1,y-1,x+1,y+3),BOOTS)
    elif layer=="off_hand":
        # Shield anchored to left wrist, remains separate and silhouette-stable.
        x=19+dx
        y=42+bob
        if dy<0:
            x+=2
        P(d,[(x-5,y-3),(x+5,y-3),(x+6,y+6),
              (x,y+13),(x-6,y+6)],METAL_DARK)
        P(d,[(x-3,y-1),(x+3,y-1),(x+4,y+5),
              (x,y+10),(x-4,y+5)],RED)
        R(d,(x-2,y+1,x+2,y+3),GOLD)
        R(d,(x-1,y-2,x+1,y+7),METAL_HI,outline=METAL_HI)
    return im

def generate(root:Path):
    src=root/"_frames"
    out=root/"assets"/"characters"/"classes"/"shared_humanoid"
    out.mkdir(parents=True,exist_ok=True)
    if src.exists():
        shutil.rmtree(src)
    for layer in LAYERS:
        for anim in ("idle","walk"):
            for direction in DIRECTIONS:
                folder=src/layer/anim/direction
                folder.mkdir(parents=True,exist_ok=True)
                for i in range(FRAMES):
                    draw_layer(layer,direction,anim,i).save(folder/f"{i:03d}.png")
    builds={}
    for layer in LAYERS:
        aid="shared_humanoid_"+layer
        target=out/layer
        data=build(src/layer,target,aid,fps=10 if layer=="body" else 10,
                   atlas_size=512,padding=3,make_gif=False)
        check=validate(target,aid)
        builds[layer]={"frames":len(data["frames"]),"atlases":len(data["atlases"]),
                       "status":check["status"],"manifest":str(Path(layer)/f"{aid}.json")}
    # Full-sized preview with four frames per direction, two clothing states.
    tile=Image.new("RGBA",(W,H),ALPHA)
    preview=Image.new("RGBA",(8*W*3,2*H*3),(28,26,39,255))
    for col,direction in enumerate(DIRECTIONS):
        for row in range(2):
            im=Image.new("RGBA",(W,H),ALPHA)
            for layer in (LAYERS if row else ("body","hair")):
                im.alpha_composite(draw_layer(layer,direction,"idle",0))
            view=im.resize((W*3,H*3),Image.Resampling.NEAREST)
            preview.alpha_composite(view,(col*W*3,row*H*3))
    preview.save(out/"p3_pilot_contact_sheet.png")
    # Snapshot animation preview with layer synchronization.
    frames=[]
    for i in range(FRAMES):
        im=Image.new("RGBA",(W,H),ALPHA)
        for layer in LAYERS:
            im.alpha_composite(draw_layer(layer,"SE","walk",i))
        frames.append(im)
    frames[0].save(out/"p3_walk_SE_equipped.gif",save_all=True,
                   append_images=frames[1:],duration=100,loop=0,
                   disposal=2,optimize=False)
    record={
      "schema_version":"1.0","phase":"P3","status":"technical_pilot_pending_visual_approval",
      "asset_id":"shared_humanoid",
      "art_guide":"docs/art-direction/P1_APPROVAL.md",
      "direction_order":list(DIRECTIONS),
      "canvas":{"w":W,"h":H,"pivot":{"x":W//2,"y":H-1}},
      "animations":{"idle":{"frames_per_direction":FRAMES,"fps":10},
                    "walk":{"frames_per_direction":FRAMES,"fps":10}},
      "layers":list(LAYERS),
      "layer_order":list(LAYERS),
      "palette":"docs/art-direction/palette.p1.json",
      "builds":builds,
      "limitations":["Pilot is procedural original pixel art, not final manually polished character art.",
                     "Only idle/walk covered; attack, hurt, died and abilities belong to P3 expansion or P4.",
                     "Character and equipment pivots are shared; layer occlusion changes for rotations are not implemented.",
                     "Aesthetic and movement approval requires human review of contact sheet and GIF."]
    }
    (out/"p3_pilot_manifest.json").write_text(json.dumps(record,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    return record

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output-root",default="build/p3")
    args=parser.parse_args()
    result=generate(Path(args.output_root))
    print(json.dumps({"status":"BUILT","layers":len(result["layers"]),
                      "total_frames":sum(b["frames"] for b in result["builds"].values())}))
