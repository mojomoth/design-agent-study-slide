import subprocess, os
from PIL import Image
V="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
def frame(t):
    p=f"native/n-{t:.2f}.png"
    if not os.path.exists(p):
        subprocess.run(["/opt/homebrew/bin/ffmpeg","-v","error","-y","-ss",f"{t:.2f}","-i",V,"-frames:v","1",p],check=True)
    return p
crops={
 "headline-the-most-important-thing":(10.20,[145,95,1175,405]),
 "film-slate":(10.30,[1195,195,1830,655]),
 "oryzo-reference-card":(10.20,[165,540,790,980]),
 "character-holding-oryzo-reference":(12.45,[66,395,1128,1045]),
 "beer-site-annotation":(12.45,[1065,715,1695,830]),
 "loop-diagram-iterating":(14.50,[140,85,1520,905]),
 "loop-diagram-cleared":(16.40,[140,85,1520,905]),
 "not-a-mind-reader-full":(17.50,[45,290,2150,1110]),
 "not-a-mind-reader-headline":(17.50,[1175,305,2130,920]),
}
import sys
sel=sys.argv[1:] or list(crops)
for k in sel:
    t,b=crops[k]
    im=Image.open(frame(t)).crop(tuple(b))
    out=f"verify/{k}.png"; im.save(out); print(out,im.size)
for t in (10.20,12.45,13.30,14.50,16.40,17.50):
    p=frame(t)
    Image.open(p).save(f"verify/capture-{t:.2f}.png")
