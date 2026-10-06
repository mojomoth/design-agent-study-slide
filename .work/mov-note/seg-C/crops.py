from PIL import Image
crops = {
 'what-style-headline': ('20.60',[80,55,870,130]),
 'make-it-look-chips-all': ('21.55',[150,190,1025,915]),
 'results-gauge-meh': ('21.55',[1265,165,1865,650]),
 'crumpled-paper-ball': ('21.92',[660,680,960,1005]),
 'example-01-floema': ('23.50',[232,340,1110,910]),
 'results-gauge-much-better': ('23.90',[1265,165,1865,650]),
 'example-02-son-daven': ('25.10',[450,215,1200,740]),
 'example-03-studio': ('25.70',[585,455,1280,940]),
 'example-cards-stack': ('25.70',[225,210,1280,950]),
}
import json
for k,(t,b) in crops.items():
    im=Image.open(f'nat/t{t}.png').crop(tuple(b))
    im.save(f'verify/crop-{k}.png'); print(k, im.size)
