import subprocess,os
from PIL import Image
V="/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov"
OUT="/Users/jeongyounglee/work/study/webdesign-agent-slide/.work/mov-note/verify-B/r"
def frame(t):
    p=f"chk/n-{t:.2f}.png"
    if not os.path.exists(p):
        subprocess.run(["/opt/homebrew/bin/ffmpeg","-v","error","-y","-ss",f"{t:.3f}","-i",V,"-frames:v","1",p],check=True)
    return Image.open(p)
assets=[
("capture","most-important-thing-slate-oryzo",10.2,(0,0,2190,1224)),
("capture","character-holding-oryzo-reference",12.45,(0,0,2190,1224)),
("capture","then-let-it-loop-setup",13.3,(0,0,2190,1224)),
("capture","then-let-it-loop-iterating",14.5,(0,0,2190,1224)),
("capture","then-let-it-loop-cleared",16.4,(0,0,2190,1224)),
("capture","not-a-mind-reader",17.75,(0,0,2190,1224)),
("crop","headline-the-most-important-thing",10.2,(145,95,1175,405)),
("crop","film-slate",10.3,(1195,195,1830,655)),
("crop","oryzo-reference-card",10.2,(165,540,790,980)),
("crop","character-holding-oryzo-reference",12.45,(66,386,1128,1045)),
("crop","beer-site-annotation",12.45,(1065,715,1695,830)),
("crop","loop-diagram-setup",13.3,(140,85,1520,905)),
("crop","loop-diagram-iterating",14.5,(140,85,1520,905)),
("crop","loop-diagram-cleared",16.4,(140,85,1520,905)),
("crop","not-a-mind-reader-full",17.75,(45,290,2150,1110)),
("crop","not-a-mind-reader-headline",17.75,(1175,305,2130,920)),
]
for kind,slug,t,b in assets:
    im=frame(t).crop(b)
    p=f"{OUT}/{kind}-{slug}-{t:.2f}.png"
    im.save(p); print(p, im.size)
