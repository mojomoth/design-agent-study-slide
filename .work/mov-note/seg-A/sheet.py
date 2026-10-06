import sys, os
from PIL import Image, ImageDraw, ImageFont
# usage: sheet.py start_idx end_idx out cols
s, e, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
cols = int(sys.argv[4]) if len(sys.argv)>4 else 5
W = 438; H = int(1224*W/2190)
idxs = list(range(s, e+1))
rows = (len(idxs)+cols-1)//cols
sheet = Image.new('RGB', (cols*W, rows*(H+20)), 'white')
d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 16)
except: f=None
for k,i in enumerate(idxs):
    p = f'frames/f-{i:04d}.png'
    if not os.path.exists(p): continue
    im = Image.open(p).convert('RGB').resize((W,H))
    x = (k%cols)*W; y=(k//cols)*(H+20)
    sheet.paste(im,(x,y+20))
    d.text((x+4,y+2), f't={(i-1)/10:.1f}', fill='red', font=f)
sheet.save(out)
