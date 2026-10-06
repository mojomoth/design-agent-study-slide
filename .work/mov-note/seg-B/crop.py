import sys, subprocess, os
from PIL import Image
# usage: crop.py t l t r b out [scale]
t=float(sys.argv[1]); box=tuple(int(x) for x in sys.argv[2:6]); out=sys.argv[6]; sc=float(sys.argv[7]) if len(sys.argv)>7 else 1.0
src=f"native/n-{t:.2f}.png"
if not os.path.exists(src):
    subprocess.run(["/opt/homebrew/bin/ffmpeg","-v","error","-y","-ss",f"{t:.2f}","-i","/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov","-frames:v","1",src],check=True)
im=Image.open(src).crop(box)
if sc!=1.0: im=im.resize((int(im.width*sc),int(im.height*sc)),Image.LANCZOS)
im.save(out)
print(out, im.size)
