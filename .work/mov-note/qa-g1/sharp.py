import sys
sys.path.insert(0,'.')
from fr import frame, PTS
from PIL import ImageFilter, ImageStat, ImageChops
box=tuple(map(int,sys.argv[1:5])); t0=float(sys.argv[5]); t1=float(sys.argv[6])
prev=None
for p in PTS:
    if p< t0-0.004 or p>t1+0.004: continue
    _,im=frame(p); c=im.crop(box).convert('L')
    e=c.filter(ImageFilter.FIND_EDGES); v=ImageStat.Stat(e).var[0]
    d = ImageStat.Stat(ImageChops.difference(c,prev)).mean[0] if prev else 0
    prev=c
    print(f'{p:.3f} sharp={v:8.1f} diffprev={d:6.2f}')
