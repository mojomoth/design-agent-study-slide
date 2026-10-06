import fr
want=[27.25,27.267,27.3,27.35,28.217,28.233,28.25,28.3,29.3,29.333,29.383,29.417,29.467,29.5,30.383,30.417,30.467]
items=[]
for pt,im in fr.frames(27.2,30.5):
    if any(abs(pt-w)<0.002 for w in want):
        items.append((pt,im.crop((0,0,1460,560)).resize((730,280))))
fr.sheet(items,4,"sheets/dense-head.jpg")
