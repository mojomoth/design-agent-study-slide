import fr, json, sys
# specs: list of [slug, time, [l,t,r,b], outdir]
specs=json.load(open(sys.argv[1]))
need={}
for s in specs:
    pt=min(fr.PTS,key=lambda x:abs(x-s[1]))
    need.setdefault(pt,[]).append(s)
t0=min(need)-0.001; t1=max(need)+0.001
for pt,im in fr.frames(t0,t1):
    for k in list(need):
        if abs(k-pt)<0.0005:
            for s in need.pop(k):
                out=f"{s[3]}/{s[0]}.png"
                im.crop(tuple(s[2])).save(out)
                print(s[0], s[1], "pts=%.3f"%pt, s[2], out)
    if not need: break
