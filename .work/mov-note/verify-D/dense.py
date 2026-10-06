import fr, sys
from PIL import Image
rngs=[(25.84,26.12,"a"),(30.44,31.0,"b"),(32.45,33.5,"c"),(34.9,35.45,"d")]
for t0,t1,n in rngs:
    items=[(pt,im.resize((547,306))) for pt,im in fr.frames(t0,t1)]
    fr.sheet(items,6,f"sheets/dense-{n}.jpg")
    print(n,len(items))
