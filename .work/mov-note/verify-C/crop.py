import sys, subprocess, os
from PIL import Image
V="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
def frame(t):
    p='n-%.2f.png'%t
    if not os.path.exists(p):
        subprocess.run(['ffmpeg','-v','error','-y','-ss','%.3f'%t,'-i',V,'-frames:v','1',p],check=True)
    return Image.open(p).convert('RGB')
name=sys.argv[1]; t=float(sys.argv[2]); bb=tuple(int(x) for x in sys.argv[3:7])
im=frame(t).crop(bb); im.save(name); print(name, im.size)
