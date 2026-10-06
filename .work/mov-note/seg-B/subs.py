from PIL import Image, ImageChops, ImageDraw, ImageFont
import os
start=7.5
crops=[]
prev=None
for i in range(1,126):
    p=f"frames/f-{i:04d}.png"
    if not os.path.exists(p): break
    t=start+(i-1)*0.1
    im=Image.open(p).crop((430,1060,1150,1215))
    g=im.convert('L')
    if prev is not None:
        diff=ImageChops.difference(g,prev)
        # count pixels changed strongly
        n=sum(1 for v in diff.getdata() if v>80)
        if n<300: 
            continue
    prev=g
    crops.append((t,im))
font=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",22)
W=720; H=155
cols=2
rows=(len(crops)+cols-1)//cols
s=Image.new('RGB',(cols*(W+90),rows*(H+6)),'white')
d=ImageDraw.Draw(s)
for k,(t,im) in enumerate(crops):
    x=(k%cols)*(W+90); y=(k//cols)*(H+6)
    d.text((x+2,y+60),f"{t:.1f}",fill='red',font=font)
    s.paste(im,(x+88,y))
s.save('subs_sheet.png')
print(len(crops),[round(t,1) for t,_ in crops])
