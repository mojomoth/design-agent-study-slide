import sys,glob
from PIL import Image, ImageDraw, ImageFont
files=sorted(glob.glob('frames/f-*.png'))
start=float(sys.argv[1]); end=float(sys.argv[2]); out=sys.argv[3]
box=(300,1050,1700,1224)
sel=[]
for i,f in enumerate(files):
    t=6.9+i*0.1
    if start-1e-6<=t<=end+1e-6: sel.append((t,f))
w=(box[2]-box[0])//2; h=(box[3]-box[1])//2
img=Image.new('RGB',(w+80,len(sel)*h),'white')
d=ImageDraw.Draw(img)
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',18)
for k,(t,f) in enumerate(sel):
    im=Image.open(f).crop(box).resize((w,h))
    img.paste(im,(80,k*h)); d.text((4,k*h+20),f"{t:.2f}",fill='red',font=font)
img.save(out)
