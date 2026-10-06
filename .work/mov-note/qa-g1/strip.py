import sys
sys.path.insert(0,'.')
from fr import frame
from PIL import Image, ImageDraw
# usage: strip.py out l t r b width_each cols t1 t2 ...
out=sys.argv[1]; box=tuple(map(int,sys.argv[2:6])); w=int(sys.argv[6]); cols=int(sys.argv[7]); ts=[float(x) for x in sys.argv[8:]]
tiles=[]
for t in ts:
    p,im=frame(t); c=im.crop(box); h=int(c.height*w/c.width); c=c.resize((w,h))
    d=ImageDraw.Draw(c); d.rectangle([0,0,110,22],fill=(0,0,0)); d.text((4,4),f'{p:.3f}',fill=(255,255,0))
    tiles.append(c)
rows=(len(tiles)+cols-1)//cols; h=tiles[0].height
S=Image.new('RGB',(cols*w+(cols-1)*6, rows*h+(rows-1)*6),(255,0,255))
for i,c in enumerate(tiles): S.paste(c,((i%cols)*(w+6),(i//cols)*(h+6)))
S.save(out)
