import sys, json
sys.path.insert(0,'.')
from fr import frame
from PIL import ImageDraw
# usage: ctx.py out t l t r b [scale]
out=sys.argv[1]; t=float(sys.argv[2]); box=list(map(int,sys.argv[3:7])); sc=float(sys.argv[7]) if len(sys.argv)>7 else 0.5
p,im=frame(t)
d=ImageDraw.Draw(im); d.rectangle([box[0],box[1],box[2]-1,box[3]-1],outline=(255,0,0),width=4)
im=im.resize((int(im.width*sc),int(im.height*sc)))
im.save(out); print(p)
