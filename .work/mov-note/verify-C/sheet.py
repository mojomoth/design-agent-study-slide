import sys, glob, os
from PIL import Image, ImageDraw, ImageFont
# usage: sheet.py out.png start end step cols scale [crop l t r b]
out=sys.argv[1]; s=float(sys.argv[2]); e=float(sys.argv[3]); step=float(sys.argv[4]); cols=int(sys.argv[5]); scale=float(sys.argv[6])
crop=None
if len(sys.argv)>7: crop=tuple(int(x) for x in sys.argv[7:11])
times=[]
t=s
while t<=e+1e-6:
    times.append(round(t,2)); t+=step
tiles=[]
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',28)
for t in times:
    idx=int(round((t-15.5)/0.05))+1
    p='frames/f-%04d.png'%idx
    if not os.path.exists(p): continue
    im=Image.open(p).convert('RGB')
    if crop: im=im.crop(crop)
    im=im.resize((int(im.width*scale),int(im.height*scale)))
    d=ImageDraw.Draw(im); d.rectangle([im.width-110,0,im.width,34],fill="black"); d.text((im.width-106,2),'%.2f'%t,fill='yellow',font=font)
    tiles.append(im)
w,h=tiles[0].size
rows=(len(tiles)+cols-1)//cols
sheet=Image.new('RGB',(w*cols,h*rows),'white')
for i,tl in enumerate(tiles):
    sheet.paste(tl,((i%cols)*w,(i//cols)*h))
sheet.save(out)
print(sheet.size)
