import sys
from PIL import Image, ImageDraw, ImageFont
# usage: sheetidx.py out.png cols scale idx1 idx2 ...  (indices into allf, labeled by pts)
out, cols, scale = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
idxs=[int(x) for x in sys.argv[4:]]
pts=[float(l) for l in open('pts.txt')]
im0=Image.open('allf/a-0000.png'); w,h=int(im0.width*scale),int(im0.height*scale); lab=22
font=ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc',20)
rows=(len(idxs)+cols-1)//cols
sheet=Image.new('RGB',(cols*w,rows*(h+lab)),'white')
for i,ix in enumerate(idxs):
    im=Image.open(f'allf/a-{ix:04d}.png').resize((w,h))
    x=(i%cols)*w; y=(i//cols)*(h+lab)
    sheet.paste(im,(x,y+lab)); ImageDraw.Draw(sheet).text((x+4,y+1),f'#{ix} t={pts[ix]:.3f}',fill='red',font=font)
sheet.save(out)
