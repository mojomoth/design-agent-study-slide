#!/usr/bin/env python3
"""Build the figure-first content manifest from the three local source documents."""
import json
from copy import deepcopy
from style_deck import restyle
from article_content import apply_article
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'slides'
FIGS = {int(p.name.split('-')[1]): str(p.relative_to(ROOT)) for p in (ROOT / 'assets/how-to-turn-your-ai-into-a-world').glob('figure-*')}
MOV = 'assets/guide1-mov/crops/'


def img(src, x=96, y=210, w=1728, h=720, label='', crop=None):
    value = dict(src=FIGS[src] if isinstance(src, int) else src, x=x, y=y, w=w, h=h)
    if label: value['label'] = label
    if crop: value['crop'] = crop
    return value


def text(value, x, y, w, h=60, size=32, color='#70706b', weight=400):
    return dict(text=value, x=x, y=y, w=w, h=h, size=size, color=color, weight=weight)


def slide(title, images, section, *, part=1, kicker='', caption='', notes='', texts=None):
    source = ('SLIDE1.md' if part == 1 else 'NOTE.md') + ' · ' + section
    return dict(title=title, images=images, part=part, kicker=kicker, caption=caption, source=source,
                notes=notes, texts=texts or [])


def add_prompt_layout(s):
    """Keep wide before/after Figures large; place tall demonstrations beside prompts."""
    s = deepcopy(s)
    s['caption'] = ''
    figures = s['images']
    numbers = [int(Path(i['src']).name.split('-')[1]) for i in figures]
    bottom = any(n in [5,6,15,20,22,23,24,25] for n in numbers)
    s['prompt_layout'] = 'bottom' if bottom else 'side'
    if bottom:
        if numbers == [25]:
            figures[0].update(x=1040,y=240,w=690,h=545)
            s['texts'] = [text('4단락 → 2단락',150,383,810,125,82,'#151515',700)]
        elif len(figures) == 2:
            for x, figure in zip([96,992],figures):
                figure.update(x=x,y=255,w=832,h=485)
        else:
            figures[0].update(x=96,y=258,w=1728,h=523)
    elif len(figures) == 1:
        figures[0].update(x=96,y=264,w=1130,h=660)
    else:
        for y,figure in zip([266,622],figures):
            figure.update(x=96,y=y,w=1130,h=302)
    return s


intro = [
    slide('Claude에게 디자인 안목을 주는 방법', [img(MOV+'51-southside-brewing.png', 246, 225, 1428, 710)], '도입',
          kicker='DESIGN EYE', caption='레퍼런스에서 시작해, 비교하며 다듬기',
          notes='발표 순서: SLIDE1 → NOTE1(폴더의 NOTE.md로 해석) → HOW_DESIGN_FROM_CC.\n도입 출처: The AI Automators, Here’s How to Give Claude an Eye for Design (6 easy steps), 2026-09-07.\nhttps://www.youtube.com/watch?v=1Y8OlBgafdE\n표지 Figure: 영상 속 Southside Brewing 결과 화면.'),
    slide('막연한 요청은 평균으로', [
        img(MOV+'02-you-ask-for-prompt.png',96,238,910,245),
        img(MOV+'03-press-crushing.png',96,510,1000,355),
        img(MOV+'04-average-website-mockup.png',1200,365,624,470)], '§1',
        texts=[text('→',1100,527,80,90,60)], notes='“현대적인 웹사이트”처럼 막연하게 요청하면 평균적인 디자인이 나온다는 영상의 프레스 비유. 학습 규모나 모델 이름은 원문의 주장이고 이 발표에서 별도로 검증한 실험 결과가 아니다.'),
    slide('방향은 사람, 구현은 Claude', [
        img(MOV+'09-film-slate.png',96,255,770,605,'DIRECTOR'),
        img(MOV+'10-character-holding-reference.png',1000,255,824,605,'REFERENCE')], '§2',
        notes='영화 감독과 배우의 비유. 사람은 레퍼런스로 방향을 정하고, Claude는 구현한다. ORYZO는 Southside Brewing의 움직임 참고 사이트다.'),
    slide('기준을 넘을 때까지 반복', [img(MOV+'14-loop-diagram-cleared.png',290,210,1340,715)], '§2',
        caption='횟수보다 품질 기준', notes='영상은 v1~v3가 기준선에 미치지 못하고 v4가 통과하는 모습으로 반복을 설명한다. 네 번이면 반드시 통과한다는 의미가 아니다.'),
    slide('말보다 예시', [
        img(MOV+'18-style-adjective-chips.png',130,260,670,440),
        img(MOV+'19-results-gauge-meh.png',345,732,240,190),
        img(MOV+'25-example-cards-stack.png',1020,240,760,455),
        img(MOV+'22-results-gauge-much-better.png',1280,727,270,190)], '§3',
        texts=[text('→',874,440,90,100,72)], notes='MODERN, CLEAN 같은 형용사만 쌓는 것보다 FLOEMA, SON DAVEN, STUDIO 같은 시각 예시가 원하는 모습을 더 직접적으로 전달한다.'),
    slide('취향을 찾는 다섯 가지 재료', [
        img(MOV+'42-category-galleries.png',115,340,145,270),
        img(MOV+'43-category-real-apps.png',270,340,145,270),
        img(MOV+'44-category-components.png',510,340,235,270),
        img(MOV+'45-category-fonts.png',865,340,235,270),
        img(MOV+'46-category-color.png',1220,340,235,270),
        img(MOV+'47-category-systems.png',1575,340,235,270)], '§3',
        texts=[text(label,x,700,330,60,30,'#151515',500) for label,x in [('Reference',125),('Component',510),('Font',865),('Color',1220),('Design System',1530)]],
        notes='영상의 여섯 분류에서 웹사이트 갤러리와 실제 앱 화면을 Reference 하나로 묶어 다섯 분류로 정리한 SLIDE1의 구성을 따른다.'),
]


note = [
    slide('같은 AI, 다른 결과', [img(1,96,250,530,600,'앱'),img(2,685,250,539,600,'게임'),img(3,1285,250,539,600,'랜딩 페이지')], '§2', part=2,
          notes='Anshu Chimala, How to turn your AI into a world-class designer, Lenny’s Newsletter, 2026-09-01.\nhttps://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world\nFigure 1~3: 원문 데모. 이 발표에서 새로 구현하거나 재현한 결과가 아니다.'),
    slide('평균에서 벗어나기', [img(4,192,210,1536,740)], '§3–5', part=2,
          caption='Discover → Define → Deliver', notes='Figure 4는 AI slop과 독창적인 디자인의 대비를 설명하는 개념 그림이다. 실제 통계 분포가 아니다. 발견은 넓게 탐색하기, 정의는 고유한 정체성 심화하기, 전달은 거친 부분 다듬기다.'),
    slide('“무작위로”만으로는 부족하다', [img(5,96,250,832,630,'기본 프롬프트'),img(6,992,250,832,630,'“독특하고 무작위로”')], '§6 · 기법 1', part=2,
          kicker='DISCOVER · 01', notes='Figure 5~6. 기본 생산성 앱 프롬프트는 보라색 UI로, 무작위로 만들라는 지시는 비슷한 오프화이트와 주황 계열로 수렴한 원문 사례. 모든 모델에 대한 일반적 정량 결과는 아니다.'),
    slide('시드로 다양성을 더하기', [img(7,285,200,1350,745)], '§6 · 기법 1', part=2, kicker='DISCOVER · 01',
          notes='Figure 7. 원문은 임의의 외부 시드 문자열을 디자인 방향 해석에 사용해 모델 밖에서 다양성을 공급하도록 제안한다. 시드는 제품명에 그대로 노출시키기 위한 문구가 아니다.'),
    slide('더 대담하게: 픽셀 아트', [img(8,300,205,1320,742)], '§7 · 기법 2', part=2, kicker='DISCOVER · 02',
          notes='Figure 8: QUESTLOG. 생산성 앱을 비디오 게임 장면 같은 픽셀 아트 세계로 구체화한 원문 데모.'),
    slide('더 대담하게: 3D 도시', [img(9,300,205,1320,742)], '§7 · 기법 2', part=2, kicker='DISCOVER · 02',
          notes='Figure 9: SKYLINE. 작업과 프로젝트를 아이소메트릭 3D 도시의 건물과 층으로 표현한다.'),
    slide('더 대담하게: 비대칭', [img(10,300,205,1320,742)], '§7 · 기법 2', part=2, kicker='DISCOVER · 02',
          notes='Figure 10: OFFCUT. 규칙 파괴, 비대칭 레이아웃, 넓은 여백을 방향으로 제시한다.\n기법 2의 실전 대화 흐름은 아이디어 나열 → 반응과 취향을 반영해 다듬기 → 제작용 프롬프트 작성이다. Figure 11~13은 글 위주의 대화 캡처여서 화면에서 생략했다. Figure 14는 Figure 7의 네 시안을 다시 보여주므로 중복 생략했다.'),
    slide('구현자와 비평가를 나누기', [img(15,96,275,1728,620,crop=[0,0,1456,520])], '§9 · 기법 3', part=2, kicker='DEFINE · 03',
          caption='만들기 → 스크린샷 → 비평 → 수정', notes='Figure 15의 Meridian 비교를 확대했다. 제작 대화와 분리된 비평가가 실제 스크린샷을 평가한다. 원문 기법의 9/10 점수 루프는 뒤에 나올 Claude Code의 레퍼런스 비교 방식과 구별한다.'),
    slide('반복으로 개성을 선명하게', [img(15,96,290,1728,590,crop=[0,974,1456,405])], '§9 · 기법 3', part=2, kicker='DEFINE · 03',
          notes='Figure 15의 Quartz 행 확대. 왼쪽은 반복 전, 오른쪽은 반복 후다. 기존 디자인의 핵심 콘셉트를 더 대담한 화면으로 발전시킨 예시다.'),
    slide('이미지가 만드는 차이', [img(16,282,205,1356,348),img(17,282,610,1356,348)], '§10 · 기법 4', part=2, kicker='DEFINE · 04',
          notes='Figure 16~17: Meridian과 zylo. 왼쪽이 생성 이미지 적용 전, 오른쪽이 적용 후다. 이미지를 장식으로 추가하는 것보다 정해진 시각 방향을 강화한다.'),
    slide('방향에 맞는 이미지', [img(18,282,205,1356,348),img(19,282,610,1356,348)], '§10 · 기법 4', part=2, kicker='DEFINE · 04',
          notes='Figure 18~19: Quartz와 Quanta. 원문 생성 이미지 비교이며 HTML에서는 움직임을 보존한다.'),
    slide('이미지를 움직이게', [img(20,96,265,1728,650)], '§11 · 기법 5', part=2, kicker='DEFINE · 05',
          notes='Figure 20. Quartz의 크리스털 이미지를 반복 영상으로 확장한 원문 비교. HTML의 오른쪽 장면은 영상으로 움직이고 PDF/PPTX는 대표 정지 프레임이다.'),
    slide('상태 사이를 연결하기', [img(21,300,205,1320,742)], '§11 · 기법 5', part=2, kicker='DEFINE · 05',
          notes='Figure 21. 여행 가방의 상태 사이를 영상으로 만들고 스크롤에 맞춰 재생 위치를 바꾸는 원문 데모다. 발표의 영상은 이를 보여주는 녹화물이며 슬라이드에서 직접 스크롤에 반응하는 구현은 아니다.'),
    slide('가치를 더하지 않으면 덜어내기', [img(22,96,220,832,695,'BEFORE'),img(23,992,220,832,695,'AFTER')], '§12–13 · 기법 6', part=2, kicker='DELIVER · 06',
          notes='Figure 22~23. 칼로리 앱에서 글로우, 불필요한 라벨, 커스텀 요소를 줄이고 이미지 그리드와 단순한 조작을 남긴 사례.'),
    slide('불필요한 라벨 줄이기', [img(24,96,265,1728,650,crop=[0,182,1456,474])], '§14 · 기법 7', part=2, kicker='DELIVER · 07',
          notes='Figure 24의 첫 번째 비교. 당연한 내용을 되풀이하는 아이브로우 라벨을 덜어낸다. 왼쪽이 흔한 패턴, 오른쪽이 대안이다.'),
    slide('배경에도 의도 담기', [img(24,96,265,1728,650,crop=[0,790,1456,457])], '§14 · 기법 7', part=2, kicker='DELIVER · 07',
          notes='Figure 24의 두 번째 비교. 일반적인 배경 그라데이션 대신 해당 경험에 어울리는 이미지를 쓴 예다. 모든 그라데이션을 금지하라는 의미는 아니다.'),
    slide('컨테이너보다 내용', [img(24,96,265,1728,650,crop=[0,1337,1456,473])], '§14 · 기법 7', part=2, kicker='DELIVER · 07',
          notes='Figure 24의 세 번째 비교. 모든 요소를 카드로 감싸기보다 평평한 그리드로 정리하는 대안을 보여 준다.'),
    slide('글자 스타일은 적게', [img(24,96,265,1728,650,crop=[0,1945,1456,479])], '§14 · 기법 7', part=2, kicker='DELIVER · 07',
          notes='Figure 24의 네 번째 비교. 글꼴 1~2개와 스타일 2~4개로 시작하고, 강조색과 이탤릭을 절제하라는 원문 조언.'),
    slide('카피도 직접 다듬기', [img(25,1080,205,650,755)], '§15–16 · 기법 8', part=2, kicker='DELIVER · 08',
          texts=[text('4단락 → 2단락',160,395,800,135,86,'#151515',700), text('짧고, 구체적으로.',165,565,750,70,40)],
          notes='Figure 25는 Claude의 Lantern 마케팅 카피와 저자의 수정본 비교다. 그림의 글을 전부 읽기보다 분량과 밀도 차이를 보여 준다. AI 초안은 자리표시자로 보고 사람이 한 줄씩 다시 읽고 고친다.\nNOTE의 결론: 발견 → 정의 → 전달을 통해 제품만의 느낌을 만든다.'),
]


def main():
    cc_path = OUT / 'cc-slides.json'
    cc = json.loads(cc_path.read_text()) if cc_path.exists() else []
    for item in cc:
        item['part'] = 3
    # The user explicitly selected NOTE2.md: omit NOTE.md's introductory Figures 1–4.
    techniques = deepcopy(note[2:])
    for item in techniques:
        technique = item['source'].split(' · ')[-1]
        item['source'] = 'NOTE2.md · ' + technique
    techniques[0]['notes'] = '기법 파트 출처: Anshu Chimala, How to turn your AI into a world-class designer, Lenny’s Newsletter, 2026-09-01.\nhttps://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world\n\n' + techniques[0]['notes']
    intro[0]['notes'] = intro[0]['notes'].replace('NOTE1(폴더의 NOTE.md로 해석)', 'NOTE2')
    techniques[-1]['notes'] = techniques[-1]['notes'].replace('NOTE의 결론:', '세 단계 요약:')
    updated = []
    for item in techniques:
        if item['title'] == '더 대담하게: 비대칭':
            item['notes'] = 'Figure 10: OFFCUT. 규칙 파괴, 비대칭 레이아웃, 넓은 여백을 방향으로 제시한다. 뒤의 세 장에서 아이디어 나열, 취향 반영, 제작 프롬프트 작성을 보여 준다. Figure 14는 Figure 7과 같은 시안이라 중복 생략했다.'
        updated.append(add_prompt_layout(item))
        if item['title'] == '더 대담하게: 비대칭':
            for figure_number, title in [(11,'많은 아이디어, 짧은 설명'),(12,'취향으로 방향 좁히기'),(13,'제작용 프롬프트로 정리하기')]:
                new = slide(title,[img(figure_number,label='AI 답변')],'기법 2',part=2,kicker='DISCOVER · 02',
                            notes=f'Figure {figure_number}. 한국어 번역문은 clone/how-to-turn-your-ai-into-a-world/index.html 참조.')
                new['source'] = 'NOTE2.md · 기법 2'
                updated.append(add_prompt_layout(new))
    summaries = [
        '레퍼런스로 방향을 정하고, 반복과 비교로 완성도를 높인다.',
        '추상적인 요청은 익숙한 색과 구조로 수렴하기 쉽다.',
        '사람이 레퍼런스로 방향을 정하고 Claude가 구현한다.',
        '결과를 비교하며 품질 기준을 넘을 때까지 다듬는다.',
        '스타일을 설명하는 형용사보다 실제 화면을 보여 준다.',
        '화면과 부품, 글꼴, 색, 디자인 규칙으로 취향을 구체화한다.',
    ]
    for item, summary in zip(intro,summaries):
        item['summary'] = summary
        item['caption'] = ''
    intro[3]['images'][0].update(y=236,h=689)
    slides = restyle(intro + updated + cc)
    slides = apply_article(slides)
    titles = json.loads((OUT/'titles.json').read_text())
    for item in slides:
        item['title'] = titles.get(item['title'], item['title'])
    slides[0]['display_title'] = 'Claude의\n디자인 안목'
    slides.insert(1, dict(
        title='AI slop', display_title='', part=1, layout='image', theme='white',
        images=[img('slides/img/ai-slop.jpg', 0, 30, 1920, 960)],
        source='사용자 첨부 이미지',
        notes='커버 바로 다음 장에 배치한 AI slop 이미지. 원본 비율과 전체 영역을 유지한다.',
    ))
    slides.append(dict(
        title='AI·SW 마에스트로 디자인 시안 모음', display_title='', part=3,
        layout='image', theme='white',
        images=[img('slides/img/ai-sw-design-collection.png', 0, 20, 1920, 980)],
        source='사용자 첨부 이미지',
        notes='마지막 장에 배치한 AI·SW 마에스트로 디자인 시안 모음. 원본 비율과 전체 영역을 유지한다.',
    ))
    result = dict(title='Claude의 디자인 안목', source_order=['SLIDE1.md','NOTE2.md','HOW_DESIGN_FROM_CC.md'],
                  note2_text_source='clone/how-to-turn-your-ai-into-a-world/index.html',
                  slides=slides)
    (OUT/'content.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(f'content.json: {len(slides)} slides ({sum(s["part"]==1 for s in slides)} + {sum(s["part"]==2 for s in slides)} + {sum(s["part"]==3 for s in slides)})')


if __name__ == '__main__':
    main()
