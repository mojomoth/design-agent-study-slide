import sys
pts=[float(l) for l in open('pts.txt')]
out=[]
for t in sys.argv[1:]:
    t=float(t); i=min(range(len(pts)),key=lambda k:abs(pts[k]-t)); out.append(str(i))
print(' '.join(out))
