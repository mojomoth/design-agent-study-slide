import subprocess, io, sys
from PIL import Image
SRC='/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov'
PTS=[float(x) for x in open('/Users/jeongyounglee/work/study/webdesign-agent-slide/.work/mov-note/qa-g1/pts.txt') if x.strip()]
def pick(t):
    for p in PTS:
        if p >= t-0.004: return p
    return PTS[-1]
def frame(t):
    p=pick(t)
    out=subprocess.check_output(['ffmpeg','-hide_banner','-loglevel','error','-ss',f'{max(p-0.001,0):.6f}','-i',SRC,'-frames:v','1','-f','image2pipe','-vcodec','png','-'])
    return p, Image.open(io.BytesIO(out)).convert('RGB')
