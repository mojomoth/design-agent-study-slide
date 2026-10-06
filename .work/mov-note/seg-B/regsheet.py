import sys, os
from PIL import Image, ImageDraw, ImageFont
# regsheet.py t0 t1 l t r b out cols scale
start=7.5
t0,t1=float(sys.argv[1]),float(sys.argv[2]); box=tuple(int(v) for v in sys.argv[3:7]); out=sys.argv[7]; cols=int(sys.argv[8]); sc=float(sys.argv[9])
font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",20)
items=[]
t=t0
while t<=t1+1e-6:
    idx=int(round((t-start)*10))+1
    p=f"frames/f-{idx:04d}.png"
    if os.path.exists(p):
        im=Image.open(p).crop(box); im=im.resize((int(im.width*sc),int(im.height*sc)))
        items.append((t,im))
    t+=0.1
w,h=items[0][1].size
rows=(len(items)+cols-1)//cols
s=Image.new('RGB',(cols*w,rows*(h+24)),'white'); d=ImageDraw.Draw(s)
for k,(t,im) in enumerate(items):
    x=(k%cols)*w; y=(k//cols)*(h+24)
    s.paste(im,(x,y+24)); d.text((x+4,y+2),f"{t:.1f}",fill='red',font=font)
s.save(out)
