import subprocess, sys
from pathlib import Path
from PIL import Image
SRC="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
D=Path("/Users/jeongyounglee/work/study/webdesign-agent-slide/.work/mov-note/qa-g2")
TMP=D/"tmp"; TMP.mkdir(exist_ok=True)
pts=[float(x) for x in (D/"pts.txt").read_text().split()]
def pick(req): return next((t for t in pts if t>=req-0.004), pts[-1])
def frame(t):
    p=TMP/f"{t:.6f}.png"
    if not p.exists():
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{max(t-0.001,0):.6f}","-i",SRC,"-frames:v","1",str(p)],check=True)
    return Image.open(p).convert("RGB")
def frames_range(t0,t1):
    """decode all frames in [t0,t1] in one ffmpeg pass"""
    sel=[t for t in pts if t0-1e-6<=t<=t1+1e-6]
    missing=[t for t in sel if not (TMP/f"{t:.6f}.png").exists()]
    if missing:
        out=TMP/"seq_%05d.png"
        subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-ss",f"{max(sel[0]-0.001,0):.6f}","-i",SRC,"-frames:v",str(len(sel)),"-fps_mode","passthrough",str(out)],check=True)
        for i,t in enumerate(sel):
            q=TMP/f"seq_{i+1:05d}.png"
            if q.exists(): q.rename(TMP/f"{t:.6f}.png")
    return sel
