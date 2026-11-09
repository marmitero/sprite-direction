#!/usr/bin/env python3
"""Import approved magenta-background front Idle as *eight frontal poses only*.

Do not infer 8 directions from the 4x2 art sheet. Do not generate fake frames.
The original PNG sources must be supplied, not downloaded from unverified URLs.
"""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path
from PIL import Image
FRONT_SHA="f528766d28a2ba7a0b22120db413dcc5ec022cb5529b09f452a2ffb2ef709113"
IDLE_SHA="0f29e33d2500dbfe51b14e7662ae0a7064d74dbf1e5cd967e5468b90287613ef"
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def chroma_rgba(frame):
    frame=frame.convert("RGB")
    pix=[]
    for r,g,b in frame.getdata():
        magenta=(r>163 and b>148 and r-g>92 and b-g>84 and abs(r-b)<70)
        pix.append((0,0,0,0) if magenta else (r,g,b,255))
    rgba=Image.new("RGBA",frame.size)
    rgba.putdata(pix)
    return rgba
def process(front,idle,output,verify_hash=True):
    front,idle,output=Path(front),Path(idle),Path(output)
    if verify_hash and (sha(front)!=FRONT_SHA or sha(idle)!=IDLE_SHA):
        raise ValueError("Approved originals do not match frozen SHA256 references")
    with Image.open(front) as f,Image.open(idle) as i:
        if f.size!=(1254,1254) or i.size!=(1448,1086):
            raise ValueError("Input art sizes differ from approved sources")
        sheet=i.copy().convert("RGB")
    output.mkdir(parents=True,exist_ok=True)
    w,h=sheet.size
    frames=[];table=[]
    for idx in range(8):
        col,row=idx%4,idx//4
        frame=chroma_rgba(sheet.crop((col*(w//4),row*(h//2),
                                     (col+1)*(w//4),(row+1)*(h//2))))
        bbox=frame.getchannel("A").getbbox()
        if not bbox:raise ValueError("Empty frame: "+str(idx))
        path=output/f"idle_front_{idx:03d}.png"
        frame.save(path,optimize=True)
        frames.append(frame)
        table.append({"frame":idx,"bbox":bbox,"sha256":sha(path)})
    if len({f["sha256"] for f in table})!=8:
        raise ValueError("Duplicate exact frames; not a genuine eight-pose sheet")
    # Rebuilding from source does not recenter each frame; avoids tremor.
    frames[0].save(output/"idle_front_8frames.gif",save_all=True,
                   append_images=frames[1:],duration=120,loop=0,
                   disposal=2,optimize=False)
    report={"status":"frontal_idle_reference_preview",
       "source_hashes":{"front":sha(front),"idle":sha(idle)},
       "layout":"4 columns x 2 rows","direction":"front_only",
       "frames":table,"runtime_status":"not_an_8_direction_asset",
       "chroma":"hard magenta key, thresholded; fringe inspection still required"}
    (output/"qa.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",
                                   encoding="utf-8")
    return report
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--front",required=True);p.add_argument("--idle",required=True)
    p.add_argument("--output",required=True)
    args=p.parse_args()
    print(json.dumps(process(args.front,args.idle,args.output),
                     ensure_ascii=False,indent=2))
