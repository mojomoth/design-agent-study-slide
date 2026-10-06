import glob
from PIL import Image, ImageDraw, ImageFont
files = sorted(glob.glob('frames/f-*.jpg'))
font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 26)
box=(380,940,1560,1224); sc=0.75
tw=int((box[2]-box[0])*sc); th=int((box[3]-box[1])*sc)
per=24; cols=2
for s in range(0,len(files),per):
    chunk=files[s:s+per]; rows=(len(chunk)+cols-1)//cols
    sheet=Image.new('RGB',(cols*tw,rows*th),'white'); d=ImageDraw.Draw(sheet)
    for i,f in enumerate(chunk):
        t=(int(f.split('-')[-1].split('.')[0])-1)/10
        im=Image.open(f).crop(box).resize((tw,th))
        x,y=(i%cols)*tw,(i//cols)*th
        sheet.paste(im,(x,y)); d.rectangle([x,y,x+70,y+30],fill='red'); d.text((x+3,y+1),f'{t:.1f}',fill='white',font=font)
        d.line([x,y+th-1,x+tw,y+th-1],fill='yellow',width=2)
    sheet.save(f'sheets/sub-{s//per}.jpg',quality=88)
