import sys, os
from PIL import Image, ImageDraw, ImageFont
# frames start at 7.5s, 10fps; f-0001 = 7.5
start=7.5
args=sys.argv
t0=float(args[1]); t1=float(args[2]); out=args[3]; cols=int(args[4]) if len(args)>4 else 5; w=int(args[5]) if len(args)>5 else 438
files=[]
t=t0
while t<=t1+1e-6:
    idx=int(round((t-start)*10))+1
    p=f"frames/f-{idx:04d}.png"
    if os.path.exists(p): files.append((t,p))
    t+=0.1
h=int(w*1224/2190)
rows=(len(files)+cols-1)//cols
sheet=Image.new("RGB",(cols*w,rows*(h+20)),"white")
d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",16)
except: font=None
for i,(t,p) in enumerate(files):
    im=Image.open(p).resize((w,h))
    x=(i%cols)*w; y=(i//cols)*(h+20)
    sheet.paste(im,(x,y+20))
    d.text((x+4,y+2),f"{t:.1f}",fill="red",font=font)
sheet.save(out)
