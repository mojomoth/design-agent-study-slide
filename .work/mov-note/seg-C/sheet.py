import sys, glob
from PIL import Image, ImageDraw, ImageFont
files = sorted(glob.glob('frames/f-*.png'))
start=float(sys.argv[1]); end=float(sys.argv[2]); out=sys.argv[3]; cols=int(sys.argv[4]) if len(sys.argv)>4 else 4
sel=[]
for f in files:
    i=int(f.split('-')[-1].split('.')[0]); t=17.5+i*0.1
    if start-1e-6<=t<=end+1e-6: sel.append((t,f))
w,h=548,306
rows=(len(sel)+cols-1)//cols
sheet=Image.new('RGB',(cols*w,rows*(h+20)),'white')
d=ImageDraw.Draw(sheet)
try: font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',16)
except: font=None
for k,(t,f) in enumerate(sel):
    im=Image.open(f).resize((w,h))
    x=(k%cols)*w; y=(k//cols)*(h+20)
    sheet.paste(im,(x,y+20)); d.text((x+4,y+2),f"{t:.2f}",fill='red',font=font)
sheet.save(out)
