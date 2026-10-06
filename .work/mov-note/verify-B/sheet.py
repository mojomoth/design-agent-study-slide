import sys,glob
from PIL import Image, ImageDraw, ImageFont
files=sorted(glob.glob('frames/f-*.png'))
start=float(sys.argv[1]); end=float(sys.argv[2]); out=sys.argv[3]
scale=float(sys.argv[4]) if len(sys.argv)>4 else 0.2
cols=int(sys.argv[5]) if len(sys.argv)>5 else 4
sel=[]
for i,f in enumerate(files):
    t=6.9+i*0.1
    if start-1e-6<=t<=end+1e-6: sel.append((t,f))
w=int(2190*scale); h=int(1224*scale)
rows=(len(sel)+cols-1)//cols
img=Image.new('RGB',(cols*w,rows*(h+20)),'white')
d=ImageDraw.Draw(img)
try: font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',16)
except: font=None
for k,(t,f) in enumerate(sel):
    im=Image.open(f).resize((w,h))
    x=(k%cols)*w; y=(k//cols)*(h+20)
    img.paste(im,(x,y+20)); d.text((x+4,y+2),f"{t:.2f}",fill='red',font=font)
img.save(out)
