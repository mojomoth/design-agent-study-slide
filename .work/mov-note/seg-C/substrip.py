import sys
from PIL import Image, ImageDraw, ImageFont
# args: out prefix start step fileprefix count
out, start, step, pref, n = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], int(sys.argv[5])
off=int(sys.argv[6]) if len(sys.argv)>6 else 0
box=(80,1070,1100,1224)
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',22)
H=box[3]-box[1]; W=box[2]-box[0]
sheet=Image.new('RGB',(W+120,H*n),'white')
d=ImageDraw.Draw(sheet)
for k in range(n):
    i=off+k
    p=f"{pref}-{i:04d}.png"
    im=Image.open(p).crop(box)
    sheet.paste(im,(120,k*H)); d.text((4,k*H+30),f"{start+i*step:.2f}",fill='red',font=font)
sheet.save(out)
