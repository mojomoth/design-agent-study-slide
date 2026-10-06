import sys,subprocess,os
from PIL import Image
V="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
def frame(t):
    p=f"chk/n-{t:.2f}.png"
    if not os.path.exists(p):
        subprocess.run(["/opt/homebrew/bin/ffmpeg","-v","error","-y","-ss",f"{t:.3f}","-i",V,"-frames:v","1",p],check=True)
    return Image.open(p)
name=sys.argv[1]; t=float(sys.argv[2]); bbox=tuple(int(x) for x in sys.argv[3].split(','))
im=frame(t).crop(bbox)
out=f"r/{name}.png"
im.save(out); print(out, im.size)
