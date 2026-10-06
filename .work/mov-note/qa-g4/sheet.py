import sys, glob
from PIL import Image, ImageDraw
pts=[float(l) for l in open('pts.txt') if l.strip()]
start=float(sys.argv[1]); out=sys.argv[2]; sel=sys.argv[3] if len(sys.argv)>3 else None
box=tuple(map(int,sys.argv[4].split(','))) if len(sys.argv)>4 and sys.argv[4] else None
scale=float(sys.argv[5]) if len(sys.argv)>5 else 0.2
cols=int(sys.argv[6]) if len(sys.argv)>6 else 4
p0=[p for p in pts if p>=start-0.004]
files=sorted(glob.glob('tmp/f_*.png'))
idx=list(range(len(files)))
if sel:
    a,b,s=sel.split(':'); idx=list(range(int(a),min(int(b),len(files)),int(s)))
ims=[]
for i in idx:
    im=Image.open(files[i])
    if box: im=im.crop(box)
    im=im.resize((int(im.width*scale),int(im.height*scale)))
    d=ImageDraw.Draw(im); d.rectangle((0,0,90,16),fill='black'); d.text((2,2),f"{i}:{p0[i]:.3f}",fill='yellow')
    ims.append(im)
w,h=ims[0].size; rows=(len(ims)+cols-1)//cols
S=Image.new('RGB',(w*cols,h*rows),'white')
for k,im in enumerate(ims): S.paste(im,((k%cols)*w,(k//cols)*h))
S.save(out); print(S.size, len(ims))
