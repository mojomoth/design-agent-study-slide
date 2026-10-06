import sys, subprocess, io, json
from PIL import Image
SRC='/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov'
def frame(t):
    out=subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-ss',f'{t:.3f}','-i',SRC,'-frames:v','1','-f','image2pipe','-vcodec','png','-'],capture_output=True,check=True).stdout
    return Image.open(io.BytesIO(out)).convert('RGB')
# args: slug t l t r b
slug=sys.argv[1]; t=float(sys.argv[2]); box=tuple(int(x) for x in sys.argv[3:7])
im=frame(t)
c=im.crop(box)
p=f'renders/{slug}.png'
c.save(p)
print(p, c.size)
