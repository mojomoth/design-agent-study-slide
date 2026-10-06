# Claude에게 디자인 안목을 주는 방법: 도입

## 1. 막연하게 요청하면 평균적인 결과가 나온다

### 콘텐츠

- 출처: The AI Automators 채널의 YouTube 영상 [Here's How to Give Claude an Eye for Design (6 easy steps)](https://www.youtube.com/watch?v=1Y8OlBgafdE)이다. 2026년 9월 7일에 게시됐고 길이는 18분 2초다.
- Claude는 보기 좋은 웹사이트를 만들 수 있지만, 무엇이 뛰어난 디자인인지는 근본적으로 알지 못한다.
- Fable 5.1과 Opus 같은 모델은 수백만 개의 웹사이트로 학습했다.
- 그래서 "현대적인 느낌의 웹사이트"처럼 막연하게 요청하면, 학습한 모든 사이트의 평균에 해당하는 결과가 나온다.
  - 화면은 이 과정을 프레스 기계에 비유한다. 프레스가 수많은 웹사이트 썸네일을 짓눌러 흐릿한 회색 랜딩 페이지 하나로 만든다.
  - 영상 설명은 이 평균 때문에 AI로 만든 결과물이 서로 비슷해 보인다고 덧붙인다.
- 화면 문구
  - TRAINED ON MILLIONS OF WEBSITES: 수백만 개의 웹사이트로 학습
  - YOU ASK FOR > a modern looking website: 여러분이 요청하는 것 > 현대적인 느낌의 웹사이트
  - THE AVERAGE OF EVERYTHING: 모든 것의 평균
- 영상 구간: YouTube 0:00~0:15.1(MOV_NOTE.md 장면 0~3). 화면 녹화 클립은 0:07.6부터 시작한다.

### 관련 이미지

![FABLE 5.1, OPUS 배지와 TRAINED ON MILLIONS OF WEBSITES 카드](assets/guide1-mov/crops/01-millions-of-websites-card.png)
![YOU ASK FOR 카드에 입력된 a modern looking website](assets/guide1-mov/crops/02-you-ask-for-prompt.png)
![프레스가 웹사이트 썸네일을 짓누르는 장면](assets/guide1-mov/crops/03-press-crushing.png)
![일부러 흐리게 처리한 평균적인 웹사이트 목업](assets/guide1-mov/crops/04-average-website-mockup.png)

---

## 2. 레퍼런스로 방향을 정하고, 품질 기준선을 넘을 때까지 반복하게 한다

### 콘텐츠

- 가장 중요한 일은 Claude에게 디자인 영감을 제공해서, 감독이 배우를 이끌듯 Claude를 이끄는 것이다.
  - 화면의 영화 슬레이트에는 작품 칸에 여러분의 웹사이트, 감독 칸에 여러분, 출연 칸에 Claude가 적혀 있다.
  - 방향은 사람이 정하고, 그 방향을 실제로 구현하는 일은 Claude가 맡는다.
- 방향을 정하는 수단은 레퍼런스다.
  - 화면의 레퍼런스 01은 스튜디오 Lusion이 만든 컵받침 제품 사이트 ORYZO다.
  - 카드 옆 손글씨 주석은 ORYZO가 "맥주 사이트의 실제 레퍼런스"라고 밝힌다. 이 맥주 사이트는 발표자가 이 영상을 위해 만든 SOUTHSIDE BREWING이다(HOW_DESIGN_FROM_CC.md 5.1절).
- 레퍼런스를 준 다음에는 Claude가 결과를 반복해서 고치게 한다.
  - 반복을 멈추는 기준은 시도 횟수가 아니라 품질 기준선이다.
  - 화면에서는 v1부터 v3까지는 기준선에 걸려 탈락하고, 네 번째 반복에서 v4가 기준선을 넘는다.
  - 참고: 영상에 딸린 글에 따르면, 발표자는 SOUTHSIDE BREWING을 비롯한 랜딩 페이지 3개를 만들 때 이 반복을 gauntlet loop 방식으로 실행했다(HOW_DESIGN_FROM_CC.md 1절, GAUNTLET_LOOP.md).
- 화면 문구
  - THE MOST IMPORTANT THING: 가장 중요한 것
  - PROD · YOUR WEBSITE / DIRECTOR · YOU / TALENT · CLAUDE: 작품: 여러분의 웹사이트 / 감독: 여러분 / 출연: Claude
  - REFERENCE 01 · ORYZO: 레퍼런스 01: ORYZO
  - THEN LET IT LOOP: 그다음 반복하게 하세요
  - QUALITY BAR / CLEARED ✓: 품질 기준선 / 통과 ✓
- 영상 구간: YouTube 0:15.1~0:24.2(MOV_NOTE.md 장면 4~5). 내레이션은 0:14.5에 시작한다.

### 관련 이미지

![작품, 감독, 출연이 적힌 영화 슬레이트](assets/guide1-mov/crops/09-film-slate.png)
![카메라를 멘 캐릭터가 ORYZO 레퍼런스 카드를 들어 보이는 장면](assets/guide1-mov/crops/10-character-holding-reference.png)
![4회 반복 뒤 v4가 품질 기준선을 통과한 상태](assets/guide1-mov/crops/14-loop-diagram-cleared.png)

---

## 3. 말 대신 예시를 보여 준다: 영감 사이트 6개 카테고리

### 콘텐츠

- Claude는 독심술사가 아니므로, 여러분이 어떤 스타일을 원하는지 알지 못한다.
- 형용사를 아무리 늘어놓아도 원하는 모습은 전달되지 않는다.
  - 화면에서는 MODERN, CLEAN, SLEEK 같은 형용사 칩 14개가 쌓여도 결과 게이지가 MEH(그저 그럼)에서 움직이지 않는다.
- 원하는 모습을 말로 설명하려 하기보다 예시를 보여 주면 훨씬 더 나은 결과를 얻는다.
  - 화면에서는 첫 예시 FLOEMA를 보여 주자마자 게이지가 MUCH BETTER(훨씬 나음)로 넘어가고, 이어서 SON DAVEN과 STUDIO 예시가 쌓인다.
- 이 영상은 디자이너들이 영감을 얻는 사이트를 6개 카테고리로 나눠 소개한다. 이 사이트에서 찾은 예시로 원하는 모습을 Claude에게 정확히 가리켜 보여 줄 수 있다.
  - 01 GALLERIES(갤러리): Awwwards, Siteinspire, Lapa Ninja(챕터 3:05)
  - 02 REAL APPS(실제 앱): Mobbin, Refero(챕터 7:48)
  - 03 COMPONENTS(컴포넌트): 21st.dev, React Bits(챕터 10:38)
  - 04 FONTS(폰트): Fonts In Use, Google Fonts(챕터 12:06)
  - 05 COLOR(색상): Coolors(챕터 13:17)
  - 06 SYSTEMS(시스템): Branding Style Guides(챕터 14:03)
  - 보너스: Pinterest, toools.design(6. Design Systems 챕터 안의 16:14부터 소개)
- 사이트별 카테고리와 용도, 예시 페이지는 HOW_DESIGN_FROM_CC.md 2절에 정리되어 있다.
- 화면 문구
  - NOT A MIND READER: 독심술사가 아닙니다
  - WHAT STYLE DO YOU WANT?: 어떤 스타일을 원하나요?
  - THE SITES WHERE DESIGNERS GET THEIR INSPIRATION: 디자이너들이 영감을 얻는 사이트
  - BROKEN INTO 6 CATEGORIES: 6개 카테고리로 나누어
  - EXACTLY THE LOOK: 정확히 원하는 모습
- 영상 구간: YouTube 0:24.2~0:42.6(MOV_NOTE.md 장면 6~10)

### 관련 이미지

![바늘이 MEH를 가리키는 RESULTS 게이지](assets/guide1-mov/crops/19-results-gauge-meh.png)
![바늘이 MUCH BETTER를 가리키는 RESULTS 게이지](assets/guide1-mov/crops/22-results-gauge-much-better.png)
![FLOEMA, SON DAVEN, STUDIO 카드가 겹쳐 쌓인 모습](assets/guide1-mov/crops/25-example-cards-stack.png)
![6개 카테고리 타일](assets/guide1-mov/crops/41-six-category-tiles.png)
