"""Use the local Korean translation verbatim for NOTE2 prompts and quotations."""
import json
import re
from copy import deepcopy
from pathlib import Path

from lxml import html
from PIL import ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
SOURCE = 'clone/how-to-turn-your-ai-into-a-world/index.html'


def translated_article():
    # The self-contained HTML has very large inline images.
    doc = html.fromstring((ROOT / SOURCE).read_text(), parser=html.HTMLParser(huge_tree=True))
    return doc, {e.get('data-source-block'): e for e in doc.xpath('//*[@data-source-block]')}


def content_text(e):
    return ''.join(e.itertext()).strip()


def wrap_text(value, size, width):
    font = ImageFont.truetype(str(HERE / 'fonts/Pretendard-Regular.ttf'), size)
    lines = []
    for paragraph in value.split('\n'):
        current = ''
        for word in paragraph.split():
            candidate = (current + ' ' + word).strip()
            if current and font.getlength(candidate) > width * .96:
                lines.append(current)
                current = word
            else:
                current = candidate
        lines.append(current)
    return '\n'.join(lines)


def article_reading_elements(s, colors):
    shapes, texts = [], []
    for panel in s.get('article_panels', []):
        p = dict(panel)
        x, y, w = p['x'], p['y'], p['w']
        size, lh, gap = p.get('size', 28), p.get('line_height', 1.4), p.get('gap', 12)
        ink, muted = colors['ink'], colors['faint']
        if p.get('ink'):
            ink, muted = '#F6EFE2', '#ACA497'
            shapes.append(dict(kind='rect', x=x-42, y=245, w=1920-x+42, h=750, fill='#141412'))
        if p.get('rule'):
            shapes.append(dict(kind='line', x=x, y=y-20, w=w, h=0, stroke=colors['line']))
        if p.get('label'):
            texts.append(dict(text=p['label'], x=x, y=y, w=w, h=32, size=20, weight=500, color=muted, role='article-label'))
            y += 50
        for block in p['blocks']:
            value = wrap_text(block.get('prefix', '') + block['text'], size, w)
            height = (value.count('\n')+1) * size * lh + 9
            texts.append(dict(text=value, x=x, y=round(y,2), w=w, h=round(height,2), size=size,
                              line_height=lh, color=ink, role='article-body'))
            y += height + gap
        assert y-gap <= p.get('bottom', 1008), (s['title'], p.get('label'), round(y-gap), p.get('bottom',1008))
    return shapes, texts


def apply_article(slides):
    doc, nodes = translated_article()
    copy = json.loads((HERE / 'article-copy.json').read_text())
    entries = dict(copy['existing'])
    entries.update({e['match_title']:e for e in copy['additional']})
    figures = doc.xpath('//*[contains(@class,"figure-translation")]')

    def blocks(ids):
        result = []
        for source_id in ids:
            e = nodes[source_id]
            prefix = ''
            parents = e.xpath('ancestor::li')
            if parents:
                li = parents[-1]
                prefix = f'{len(li.xpath("preceding-sibling::li"))+1}. ' if li.getparent().tag == 'ol' else '• '
            result.append(dict(source_id=source_id, text=content_text(e), prefix=prefix))
        return result

    def inline(source_id):
        value = content_text(nodes[source_id])
        quote = re.search('“(.+?)”', value)
        assert quote, source_id
        return [dict(source_id=source_id, text=quote[1])]

    def panel(items, x=1230, y=286, w=594, label='프롬프트 전문', **kw):
        return dict(blocks=items,x=x,y=y,w=w,label=label,**kw)

    def side(s, items, *, wide=False, **kw):
        x, w, iw = (1110,714,952) if wide else (1230,594,1080)
        for image in s['images']:
            image.update(x=96,w=iw)
        return panel(items,x=x,w=w,ink=s.get('prompt_panel')=='ink',**kw)

    def bottom(items, **kw):
        return panel(items,x=96,y=830,w=1728,**kw)

    def extra(parent, title, summary, ids, panels):
        s = dict(title=title,summary=summary,part=2,kicker=parent['kicker'],images=[],texts=[],
                 theme='paper',caption='',source=SOURCE,source_blocks=ids,article_panels=panels,
                 notes='한국어 번역문: '+SOURCE+'\n\n'+'\n\n'.join(content_text(nodes[i]) for i in ids))
        return s

    out = []
    for original in slides:
        if original['part'] != 2:
            out.append(original)
            continue
        s = deepcopy(original)
        old_title = s['title']
        c = entries[old_title]
        s.update(title=c['title'],summary=c['summary'],source=SOURCE,source_blocks=c['source_block_ids'],texts=[])
        s['kicker'] = s['kicker'].replace('DISCOVER','탐색').replace('DEFINE','구체화').replace('DELIVER','마무리')
        for key in ('prompt','prompt_label','source_excerpt'):
            s.pop(key,None)
        s['notes'] = 'NOTE2 파트 · 한국어 번역문: '+SOURCE+'\n\n'+'\n\n'.join(content_text(nodes[i]) for i in c['source_block_ids'])
        ids = c['prompt_block_ids']
        s['article_panels'] = []
        following = []
        if old_title == '“무작위로”만으로는 부족하다':
            s['article_panels'] = [panel(blocks(['b028']),x=96,y=815,w=800,label='기본 프롬프트 전문'),
                                   panel(blocks(['b033']),x=992,y=815,w=832,label='무작위 요청 프롬프트 전문')]
        elif old_title in ('시드로 다양성을 더하기','취향으로 방향 좁히기'):
            s['article_panels'] = [side(s,blocks(ids),wide=True,size=28,gap=9)]
        elif old_title == '제작용 프롬프트로 정리하기':
            s['article_panels'] = [side(s,blocks(ids),wide=True)]
            translated = figures[2].xpath('./p|./ul/li')[1:]
            shown = [dict(source_id=f'figure13-{i}',text=content_text(e)) for i,e in enumerate(translated)]
            s['article_panels'].append(panel(shown,x=1110,y=490,w=714,label='AI가 작성한 프롬프트 · 그림에 표시된 범위',size=26,gap=9))
        elif old_title == '구현자와 비평가를 나누기':
            s['images'][0].update(y=264,h=650)
            s['article_panels'] = []
            full_ids = [f'b{i:03}' for i in range(76,88)]
            following.append(extra(s,'디자인 평가자 프롬프트',
                '스크린샷만으로 평가하고, 같은 기준으로 수정과 평가를 반복한다.',full_ids,
                [panel(blocks(full_ids[:6]),x=96,y=275,w=824,label='프롬프트 전문 · 1/2',size=28,gap=10),
                 panel(blocks(full_ids[6:]),x=1000,y=275,w=824,label='프롬프트 전문 · 2/2',size=28,gap=10)]))
        elif old_title == '반복으로 개성을 선명하게':
            s['article_panels'] = [bottom(blocks(['b089']),label='평가 후의 변화')]
            example_ids = ['b093','b094','b095']
            following.append(extra(s,'디자인 평가 기준의 구체화',
                '눈으로 비교할 수 있는 예시와 명확한 품질 기준으로 평가한다.',
                ['b092','b093','b094','b095','b096','b097'],
                [panel(inline(i),x=x,y=300,w=520,label=label,size=30,gap=12)
                 for i,x,label in zip(example_ids,[96,700,1304],['나쁜 예','괜찮은 예','좋은 예'])]
                +[panel(blocks(['b097']),x=96,y=765,w=1728,label='반복 종료 기준',size=28)]))
        elif old_title == '방향에 맞는 이미지':
            s['title'] = '이미지 생성 도구의 연결'
            s['summary'] = '사용 환경에 맞춰 내장 기능, Codex CLI 또는 API를 연결한다.'
            s['source_blocks'] += ['b109','b110','b111','b112','b113','b114','b115','b116']
            s['article_panels'] = [side(s,inline('b113'),wide=True,label='Claude Code + ChatGPT · 요청 전문',size=28)]
            s['article_panels'].append(panel(inline('b116'),x=1110,y=525,w=714,label='API 키 파일 관리 · 요청 전문',size=28))
        elif old_title == '이미지를 움직이게':
            s['images'][0].update(y=250,h=410)
            s['article_panels'] = [panel(blocks(ids[:1]),x=96,y=705,w=824,size=27,label='프롬프트 전문 · 1/2',gap=8),
                                   panel(blocks(ids[1:]),x=1000,y=705,w=824,size=27,label='프롬프트 전문 · 2/2',gap=8)]
        elif old_title == '상태 사이를 연결하기':
            s['images'][0].update(x=96,y=270,w=828,h=650)
            s['article_panels'] = [panel(blocks(ids),x=1010,y=272,w=814,size=27,gap=8)]
        elif old_title == '가치를 더하지 않으면 덜어내기':
            s['article_panels'] = [panel(blocks(ids),x=96,y=800,w=1728,label='원문 요청 전문',size=28,gap=3)]
            for image,label in zip(s['images'],['적용 전','적용 후']): image['label']=label
        elif old_title in ('불필요한 라벨 줄이기','배경에도 의도 담기','컨테이너보다 내용','글자 스타일은 적게'):
            row = ('불필요한 라벨 줄이기','배경에도 의도 담기','컨테이너보다 내용','글자 스타일은 적게').index(old_title)
            cells = figures[3].xpath('.//tbody/tr')[row].xpath('./td')
            s['article_panels'] = [panel([dict(source_id=f'figure24-row{row+1}-before',text=content_text(cells[0]))],
                                         x=96,y=824,w=800,label='너무 자주 쓰는 방식',size=28),
                                   panel([dict(source_id=f'figure24-row{row+1}-after',text=content_text(cells[1]))],
                                         x=992,y=824,w=832,label='더 나은 선택지',size=28)]
        elif old_title == '카피도 직접 다듬기':
            s['images'][0].update(x=1100,y=252,w=650,h=702)
            result_heading=figures[4].xpath('./h4')[1]
            result_nodes=result_heading.xpath('following-sibling::p')
            s['article_panels']=[panel([dict(source_id=f'figure25-revised-{i}',text=content_text(e)) for i,e in enumerate(result_nodes)],
                                      x=96,y=300,w=870,label='작성자가 고친 문구 · 번역 전문',size=30,gap=18)]
        else:
            s['article_panels']=[side(s,blocks(ids))]
        # Recompute notes from the authoritative translation, including new references.
        s['notes'] = 'NOTE2 파트 · 한국어 번역문: '+SOURCE+'\n\n'+'\n\n'.join(content_text(nodes[i]) for i in s['source_blocks'])
        out.append(s)
        out.extend(following)
    return out
