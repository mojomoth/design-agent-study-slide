import sys, glob
from PIL import Image, ImageDraw, ImageFont
src, prefix, step, cols, rows, scale = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6])
t0 = float(sys.argv[7]) if len(sys.argv)>7 else 0.0
fs = sorted(glob.glob(src+'/*.png'))
im0 = Image.open(fs[0]); w,h = int(im0.width*scale), int(im0.height*scale)
lab=22
try: font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',20)
except: font=None
per=cols*rows
for s in range(0,len(fs),per):
    chunk=fs[s:s+per]
    sheet=Image.new('RGB',(cols*w,rows*(h+lab)),'white')
    for i,f in enumerate(chunk):
        idx=s+i
        im=Image.open(f).resize((w,h))
        x=(i%cols)*w; y=(i//cols)*(h+lab)
        sheet.paste(im,(x,y+lab))
        d=ImageDraw.Draw(sheet); d.text((x+4,y+1),f't={t0+idx*step:.2f}',fill='red',font=font)
    sheet.save(f'{prefix}-{s//per:02d}.png')
    print(f'{prefix}-{s//per:02d}.png', f't={t0+s*step:.2f}..{t0+(s+len(chunk)-1)*step:.2f}')
