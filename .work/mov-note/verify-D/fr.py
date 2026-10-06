import subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont
SRC="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
W,H=2190,1224
def pts_list():
    out=subprocess.run(["ffprobe","-v","error","-select_streams","v","-show_entries","frame=pts_time","-of","csv=p=0",SRC],capture_output=True,text=True).stdout
    return [float(x.strip().rstrip(',')) for x in out.split() if x.strip().rstrip(',')]
PTS=pts_list()
def frames(t0,t1):
    """yield (pts, PIL image) for frames with t0<=pts<=t1"""
    p=subprocess.Popen(["ffmpeg","-v","error","-i",SRC,"-f","rawvideo","-pix_fmt","rgb24","-fps_mode","passthrough","-"],stdout=subprocess.PIPE)
    n=W*H*3
    for pt in PTS:
        buf=p.stdout.read(n)
        if len(buf)<n: break
        if pt<t0: continue
        if pt>t1: break
        yield pt, Image.frombytes("RGB",(W,H),buf)
    p.kill()
def frame_at(t):
    best=min(PTS,key=lambda x:abs(x-t))
    for pt,im in frames(best-0.001,best+0.001):
        return pt,im
def sheet(items,cols,path,label_h=22):
    w,h=items[0][1].size
    rows=(len(items)+cols-1)//cols
    S=Image.new("RGB",(cols*w,rows*(h+label_h)),"white")
    d=ImageDraw.Draw(S)
    try: f=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",18)
    except: f=None
    for i,(pt,im) in enumerate(items):
        x=(i%cols)*w; y=(i//cols)*(h+label_h)
        S.paste(im,(x,y+label_h)); d.text((x+4,y+2),f"{pt:.3f}",fill="red",font=f)
    S.save(path,quality=80)
