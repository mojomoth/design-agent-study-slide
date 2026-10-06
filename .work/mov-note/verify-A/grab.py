import sys, subprocess, os
from PIL import Image, ImageDraw, ImageFont
# usage: grab.py out.png l,t,r,b scale t1 t2 ...
out = sys.argv[1]; box = tuple(int(x) for x in sys.argv[2].split(',')); scale=float(sys.argv[3]); times=[float(x) for x in sys.argv[4:]]
os.makedirs('tmp', exist_ok=True)
tiles=[]
font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 24)
for t in times:
    p=f'tmp/t{t:.3f}.jpg'
    if not os.path.exists(p):
        subprocess.run(['/opt/homebrew/bin/ffmpeg','-v','error','-y','-ss',f'{t:.3f}','-i','/Users/jeongyounglee/work/study/webdesign-agent-slide/guide/guide1.mov','-frames:v','1','-q:v','2',p],check=True)
    im=Image.open(p).crop(box)
    im=im.resize((int(im.width*scale),int(im.height*scale)))
    d=ImageDraw.Draw(im); d.rectangle([0,0,80,28],fill='red'); d.text((3,1),f'{t:.2f}',fill='white',font=font)
    tiles.append(im)
cols = max(1, min(len(tiles), int(2000//tiles[0].width)))
rows=(len(tiles)+cols-1)//cols
W=tiles[0].width; H=tiles[0].height
sheet=Image.new('RGB',(cols*W,rows*H),'white')
for i,im in enumerate(tiles): sheet.paste(im,((i%cols)*W,(i//cols)*H))
sheet.save(out,quality=90)
print(sheet.size)
