import sys, glob, os
from PIL import Image, ImageDraw, ImageFont
files = sorted(glob.glob('frames/f-*.png'))
cols, rows = 4, 4
tw, th = 547, 306
font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 28)
os.makedirs('sheets', exist_ok=True)
per = cols*rows
for s in range(0, len(files), per):
    sheet = Image.new('RGB', (cols*tw, rows*th), 'white')
    d = ImageDraw.Draw(sheet)
    for i, f in enumerate(files[s:s+per]):
        idx = int(f.split('-')[-1].split('.')[0]) - 1
        t = idx/10
        im = Image.open(f).resize((tw, th))
        x, y = (i%cols)*tw, (i//cols)*th
        sheet.paste(im, (x, y))
        d.rectangle([x, y, x+90, y+34], fill='red')
        d.text((x+4, y+2), f'{t:.1f}', fill='white', font=font)
    sheet.save(f'sheets/sheet-{s//per:02d}.png')
