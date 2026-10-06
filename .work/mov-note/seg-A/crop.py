import sys, subprocess, os
from PIL import Image
# usage: crop.py name t l t r b
name, t = sys.argv[1], sys.argv[2]
l,tp,r,b = map(int, sys.argv[3:7])
src = f'hi/t_{t}.png'
if not os.path.exists(src):
    subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-ss',t,'-i','/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov','-frames:v','1',src],check=True)
im = Image.open(src).convert('RGB')
c = im.crop((l,tp,r,b))
out = f'verify/{name}.png'
c.save(out)
print(out, c.size)
