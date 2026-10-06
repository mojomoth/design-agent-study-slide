import sys, os
from PIL import Image, ImageDraw, ImageFont
d=sys.argv[1]; base=float(sys.argv[2]); step=float(sys.argv[3]); out=sys.argv[4]
s=int(sys.argv[5]) if len(sys.argv)>5 else 0; e=int(sys.argv[6]) if len(sys.argv)>6 else 9999
fs=sorted(os.listdir(d))[s:e]
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',22)
box=(420,1050,1420,1215); w=(box[2]-box[0])//2; h=(box[3]-box[1])//2
cols=3; rows=(len(fs)+cols-1)//cols
img=Image.new('RGB',(cols*w,rows*(h+26)),'white'); dr=ImageDraw.Draw(img)
for i,f in enumerate(fs):
    idx=int(f[2:6])
    im=Image.open(os.path.join(d,f)).crop(box).resize((w,h))
    x=(i%cols)*w; y=(i//cols)*(h+26)
    img.paste(im,(x,y+26)); dr.text((x+4,y+2),f"{base+(idx-1)*step:.1f}s",fill='red',font=font)
img.save(out)
