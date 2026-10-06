import sys, os
from PIL import Image, ImageDraw, ImageFont
files = sorted(os.listdir('frames'))
start=int(sys.argv[1]); end=int(sys.argv[2]); out=sys.argv[3]; base=24.0
cols=4; tw=540; th=int(1224*tw/2190)
sel=files[start:end]
rows=(len(sel)+cols-1)//cols
img=Image.new('RGB',(cols*tw,rows*(th+24)),'white')
d=ImageDraw.Draw(img)
try: font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',20)
except: font=None
for i,f in enumerate(sel):
    im=Image.open('frames/'+f).resize((tw,th))
    x=(i%cols)*tw; y=(i//cols)*(th+24)
    img.paste(im,(x,y+24))
    idx=int(f[2:6])
    d.text((x+4,y+2),f"{base+(idx-1)*0.1:.1f}s",fill='red',font=font)
img.save(out)
