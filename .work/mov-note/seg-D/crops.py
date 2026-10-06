from PIL import Image
import sys
C={
 'in-this-video-headline':('30.0',[140,95,1345,505]),
 'inspiration-sites-fan':('30.0',[63,525,1694,1044]),
 'site-card-awwwards':('26.133',[64,680,640,1044]),
 'site-card-siteinspire':('26.217',[340,690,860,1044]),
 'site-cards-lapa-ninja-mobbin':('26.417',[64,520,930,1044]),
 'site-card-refero':('26.5',[440,640,1070,1044]),
 'site-cards-21st-dev-react-bits':('26.733',[560,470,1180,1010]),
 'site-card-fonts-in-use':('26.833',[700,440,1330,942]),
 'site-cards-google-fonts-coolors':('27.067',[880,430,1600,1044]),
 'site-cards-brandingstyleguides-pinterest':('27.2',[1000,470,1694,1044]),
 'site-card-tooools-design':('27.3',[1050,640,1694,1044]),
 'broken-into-6-categories-headline':('32.3',[85,65,1650,390]),
 'six-category-tiles':('32.3',[15,465,2140,855]),
 'explorer-exactly-the-look':('34.0',[9,465,1415,1135]),
 'in-action-site-trio':('35.0',[38,415,2112,1066]),
 'harbour-lane-site':('35.0',[45,560,546,985]),
 'blackwater-cabins-site':('35.0',[1632,575,2112,985]),
 'southside-brewing-site':('35.0',[535,420,1635,1062]),
}
names=sys.argv[1:] or list(C)
for n in names:
    t,b=C[n]
    Image.open(f'src/t-{t}.png').crop(tuple(b)).save(f'crops/{n}.png')
    print(n,t,b)
