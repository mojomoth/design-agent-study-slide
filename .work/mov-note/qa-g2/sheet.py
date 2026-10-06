import sys; sys.path.insert(0,'/Users/jeongyounglee/work/study/webdesign-agent-slide/.work/mov-note/qa-g2')
from fr import *
from PIL import ImageDraw
def sheet(times, box, out, w=360, cols=4):
    ims=[]
    for t in times:
        im=frame(t).crop(box); r=w/im.width; im=im.resize((w,int(im.height*r)))
        d=ImageDraw.Draw(im); d.rectangle((0,0,70,16),fill=(255,255,0)); d.text((2,2),f'{t:.3f}',fill=(0,0,0))
        ims.append(im)
    h=ims[0].height; rows=(len(ims)+cols-1)//cols
    S=Image.new('RGB',(cols*(w+4),rows*(h+4)),(255,0,255))
    for i,im in enumerate(ims): S.paste(im,((i%cols)*(w+4),(i//cols)*(h+4)))
    S.save(out,quality=85)
if __name__=='__main__':
    import json
    times=[float(x) for x in sys.argv[1].split(',')]; box=tuple(int(x) for x in sys.argv[2].split(',')); out=sys.argv[3]
    w=int(sys.argv[4]) if len(sys.argv)>4 else 360; cols=int(sys.argv[5]) if len(sys.argv)>5 else 4
    sheet(times,box,out,w,cols)
