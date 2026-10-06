import sys,glob
from PIL import Image, ImageDraw, ImageFilter, ImageStat
# usage: strip.py out.jpg l t r b t0 t1 [cols] [width]
out=sys.argv[1]; l,t,r,b=map(int,sys.argv[2:6]); t0,t1=float(sys.argv[6]),float(sys.argv[7])
cols=int(sys.argv[8]) if len(sys.argv)>8 else 4
W=int(sys.argv[9]) if len(sys.argv)>9 else 480
fs=sorted(glob.glob('full/t_*.png'))
sel=[f for f in fs if t0-1e-4<=float(f[7:-4])<=t1+1e-4]
H=int((b-t)*W/(r-l))
rows=(len(sel)+cols-1)//cols
sheet=Image.new('RGB',(cols*W,rows*(H+20)),'white'); d=ImageDraw.Draw(sheet)
for i,f in enumerate(sel):
    im=Image.open(f).convert('RGB').crop((l,t,r,b))
    g=im.convert('L').filter(ImageFilter.FIND_EDGES)
    s=ImageStat.Stat(g).var[0]
    x=(i%cols)*W; y=(i//cols)*(H+20)
    sheet.paste(im.resize((W,H)),(x,y+20)); d.text((x+4,y+4),f"{f[7:-4]} sharp={s:.0f}",fill='black')
    print(f[7:-4], round(s))
sheet.save(out,quality=85)
