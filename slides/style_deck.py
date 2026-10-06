"""Adapt the local ref/ slides' paper/ink palette and asymmetric image layouts.

References: set2_slide_05/08/09 and set3_slide_01/03/04.
The user's quieter Pretendard titles take precedence over the references' display type.
"""
from copy import deepcopy

PAPER = '#F6EFE2'
INK = '#141412'
PALETTES = {
    'paper': dict(bg=PAPER, ink='#24231F', muted='#756F65', faint='#817A6E', line='#CDC4B6'),
    'ink': dict(bg=INK, ink=PAPER, muted='#C3BBAE', faint='#ACA497', line='#4E4A43'),
}


def palette(s):
    return PALETTES[s.get('theme','paper')]


def title_box(s):
    if s.get('layout') == 'cover':
        return dict(x=96,y=286,w=516,h=170,size=42,weight=400,line_height=1.35)
    if s.get('layout') == 'case-opener':
        return dict(x=96,y=735,w=720,h=80,size=42,weight=400,line_height=1.25)
    return dict(x=96,y=96,w=1728,h=65,size=42,weight=400,line_height=1.25)


def summary_box(s):
    if s.get('layout') == 'cover':
        return dict(x=96,y=494,w=490,h=175,size=28,line_height=1.5)
    if s.get('layout') == 'case-opener':
        return dict(x=96,y=830,w=680,h=130,size=28,line_height=1.45)
    return dict(x=96,y=165,w=1728,h=52,size=28,line_height=1.4)


def restyle(slides):
    slides = deepcopy(slides)
    panels = {'시드로 다양성을 더하기','이미지가 만드는 차이','상태 사이를 연결하기'}
    for s in slides:
        s['theme'] = 'ink' if s['title'] in {'“무작위로”만으로는 부족하다','참고 화면에서 시작한다'} else 'paper'
        s['prompt_panel'] = 'ink' if s['title'] in panels else 'none'
        p = palette(s)
        for t in s.get('texts',[]):
            t['color'] = p['ink'] if t.get('color','#151515') in {'#151515','#111111','#111','#111110','#242424'} else p['muted']
            if t.get('weight',400) >= 600: t['weight'] = 500
            if t.get('size',0) > 60: t['size'] = 60
        for shape in s.get('shapes',[]):
            if shape.get('fill') in {'#F5F5F3','#FAFAF8'}:
                shape['fill'] = '#EFE6D7'
                shape['stroke'] = 'transparent'

    cover = slides[0]
    cover['layout'] = 'cover'
    cover['display_title'] = 'Claude에게 디자인\n안목을 주는 방법'
    cover['images'][0].update(x=730,y=163,w=1190,h=710)
    case = next(s for s in slides if s['title']=='참고 화면에서 시작한다')
    case['layout'] = 'case-opener'
    case['images'][0].update(x=0,y=0,w=1920,h=616)
    case['texts'] = []
    for index,label in enumerate(['찾기','전달','비교','기록']):
        x = 996 + index*220
        case['texts'].append(dict(text=f'{index+1:02}',x=x,y=736,w=160,h=36,size=20,color=PALETTES['ink']['faint']))
        case['texts'].append(dict(text=label,x=x,y=801,w=160,h=55,size=32,weight=500,color=PAPER))
    return slides
