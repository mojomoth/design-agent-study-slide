import fr, numpy as np
from PIL import Image, ImageDraw, ImageFont
f=ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc",20)
states=[]; prev=None
thumbs=[]
targets=[round(25.8+0.1*i,2) for i in range(97)]
for pt,im in fr.frames(19.8,35.5):
    sub=im.crop((250,1000,1950,1224))
    a=np.asarray(sub.convert("L").resize((425,56))).astype(int)
    if prev is None or np.abs(a-prev).mean()>2.0:
        states.append((pt,sub.resize((850,112))))
        prev=a
    if pt>=25.75:
        thumbs.append((pt,im.resize((365,204))))
print(len(states))
# subtitle sheet(s)
per=24
for k in range(0,len(states),per):
    ch=states[k:k+per]
    S=Image.new("RGB",(850*2,(len(ch)+1)//2*(112+24)),"white"); d=ImageDraw.Draw(S)
    for i,(pt,s) in enumerate(ch):
        x=(i%2)*850;y=(i//2)*136
        d.text((x+4,y+2),f"{pt:.3f}",fill="red",font=f); S.paste(s,(x,y+24))
    S.save(f"sheets/sub-{k//per:02d}.jpg",quality=85)
# thumbs: choose nearest to targets
sel=[]
for t in targets:
    c=min(thumbs,key=lambda x:abs(x[0]-t))
    if not sel or sel[-1][0]!=c[0]: sel.append(c)
for k in range(0,len(sel),40):
    fr.sheet(sel[k:k+40],8,f"sheets/thumb-{k//40:02d}.jpg")
