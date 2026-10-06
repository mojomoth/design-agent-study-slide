# PART 03 스토리보드: Claude Code로 랜딩 페이지 만들기 (HOW_DESIGN_FROM_CC.md)

Notes for the builder (short):
- Paths are relative to the project root (in HTML from `slides/`: `../assets/...`, `img/...`). Site screenshots in `deck/img/sites/` are all `status: ok` (1600x1000, ratio 1.6), so the 1.6 frames below need no cropping. The tilted video cards (crops 26, 31, 34) are used only on the divider (S1), because the fresh screenshots are sharper.
- Derived crops (PIL crop only, boxes in source px, left/top/right/bottom). All four files now exist in `deck/img/03/` and were checked by eye:
  - `deck/img/03/gofullpage-hero.png` from `deck/img/sites/gofullpage.png` box (240,90,1380,490) → 1140x400: logo, tagline, green CTA and the product shot. The incident notice is cut off.
  - `deck/img/03/gauntlet-title.png` from `deck/img/sites/gauntlet.png` box (440,90,1160,430) → 720x340: title "How to Run a Gauntlet Loop", subtitle, byline "Matt Shumer, Jul 27, 2026".
  - `deck/img/03/frontend-design-repo.png` from `deck/img/sites/frontenddesign.png` box (0,85,1280,400) → 1280x315: "anthropics / skills", the breadcrumb "skills / skills / frontend-design" and the commit "Update frontend-design skill to avoid generic design defaults".
  - `deck/img/03/annajona-wave.png` from `deck/img/sites/annajona.png` box (560,440,1456,1000) → 896x560 (1.6): the pink curve cutting into the bar video, with the bartender and arches. This crop removes the large "Anna Jóna has been closed." notice, which is not in the source and would read as a claim on screen.
- Every image is used once in this part. Cross-part: Part 01 S1 already shows 50, 51 and 52 (51 large, 50 and 52 small), and the case slides here still need them. 49 shows the same three pages and appears once (S17). Part 01 uses the loop frames 13 and 14; S15 uses the unused setup frame 12 (same diagram, empty bar), as a callback.
- Text budget used here: one headline, at most 2 short Korean lines, and at most about 4 tiny labels. Site names on frames go in `.fig figcaption` (one short line each). Tag grids, struck words, code cards, checklists of 2-4 word items and numerals count as visual devices.
- Headline widths were measured with slides/fonts/Anton-Regular.ttf (`.d` line-height .84, so one d-xl line is 252px tall).
- Tone rhythm (6 dark of 19): D L L L D L L D L D L L D L L D L L L.

## S1. OUR TRAM  (dark)
- headline: CLAUDE CODE
- text: 영상 속 사이트와 프롬프트로 랜딩 페이지 만들기
- labels: PART 03, 원문: The AI Automators, "Claude + Design Inspiration: All the Links From the Video", 2026년 9월 7일
- images:
  - assets/guide1-mov/crops/26-site-awwwards.png [cover, object-position left center] — the tilted AWWWARDS card (green "WHY ZERO" page). Left anchoring keeps the whole black name pill; only the right edge of the card is trimmed.
  - assets/guide1-mov/crops/31-site-21st-dev-react-bits.png [cover, .top] — the 21ST.DEV card with the purple REACT BITS card on top. Anchored to the top so the 21ST.DEV pill is not clipped; the trim falls on the empty bottom.
  - assets/guide1-mov/crops/34-site-coolors.png [cover, .top] — the COOLORS card with its colour-swatch stack. Top anchoring keeps the pill and drops the stray half-pill of the next card at the bottom.
- placement: lbl PART 03 at x 56, y 120 (cream). Three frames of 560x400 at y 170, x 56 / 680 / 1304 (cream video cards on black, like the three portraits in OUR TRAM). The Korean line (.lead) at x 56, y 605, and the source line (.cap, one line) at x 56, y 665. CLAUDE CODE at d-xl 300 (1449 wide) in cream, bottom-right (right 56, bottom 30).
- source: 문서 도입부 (원문 제목, 게시자, 날짜, 원문은 영상에 나온 사이트, 도구, 프롬프트를 모은 글)

## S2. BEST CONCEPT  (light)
- headline: 8 STEPS
- text: 페이지마다 프롬프트 하나, 수정은 한두 번
- labels: 1 준비, 2 찾기, 3 모으기, 4 프롬프트, 5 실행, 6 자체 확인, 7 수정, 8 기록
- images: 없음 (visual device: eight huge numerals with one-word labels)
- placement: "8 STEPS" at d-xxl 400 (about 1176 wide) at x 40, y 110. The Korean line (.lead) top-right at x 1300, y 210, 560 wide. Numerals (.num 220) in two rows of four: row 1 at y 520, row 2 at y 800, columns x 56 / 516 / 976 / 1436. Each numeral is a .row with gap 24, and the label sits to its right as one bold .txt word (padding-top 22). No gray hint lines.
- source: ## 1. 전체 흐름

## S3. PORTFOLIO  (light, data-hdr="bottom")
- headline: REFERENCE
- text: 갤러리: 페이지 구성과 분위기 / 실제 앱: 가입 화면과 가격표
- labels (figcaptions): Awwwards, Siteinspire, Lapa Ninja, Mobbin + MCP, Refero
- images:
  - deck/img/sites/awwwards.png [cover] — "Site of the Day" bar and the big "LIDAR DRONE SCANNING" title. Cover at 1.35 trims about 90px per side; the title stays centred.
  - deck/img/sites/siteinspire.png [cover] — category filter row and the HRS Connect / Cactus Digitale thumbnails
  - deck/img/sites/lapaninja.png [cover] — "The Best Landing Page Design Inspiration" title and the card carousel
  - deck/img/sites/mobbin.png [cover] — "Where teams and agents find designs that work" with the app icons (the centre crop keeps the whole headline)
  - deck/img/sites/refero.png [cover] — serif "What are you designing next?" and the research box
- placement: data-hdr="bottom". REFERENCE (d-l 220, 876 wide) at x 56, y 40. The two Korean lines (.txt) top-right at x 1180, y 70, 680 wide. Big image at x 0, y 250, 1000x740. The 2x2 grid uses 400x355 cells at (1040,250), (1470,250), (1040,635), (1470,635) in the order Siteinspire, Lapa Ninja (galleries, top row), Mobbin, Refero (real apps, bottom row). Each frame carries only its site name as a .fig figcaption (cream box, bottom-left).
- source: ## 2. 참고 자료 찾기 (### 2.1 디자인 갤러리, ### 2.2 실제 앱과 웹사이트)

## S4. OUR SERVICES  (light)
- headline: COMPONENT
- text: 버튼, 갤러리, 배경 같은 화면 부품 / Copy prompt로 복사해 Claude Code에 붙여 넣기
- labels: React Bits, 21st.dev
- images:
  - deck/img/sites/21stdev.png [cover] — "The living library of interfaces", "12,000+" and the three hero cards (exact 1.6 frame, no crop)
  - deck/img/sites/reactbits.png [cover] — the middle band: "React components for creative developers" on the purple glow and the code card. Cover at about 1.96 trims the empty top and bottom.
- placement: COMPONENT (d-l 220, 984 wide) at x 48, y 130. The two Korean lines (.txt) at x 56, y 370, 880 wide. On the left, React Bits: .lbl at x 56, y 505, image at x 56, y 560, 880x450. On the right, a .block-dark panel at x 1000, y 360, 920x720 (bleeds right and bottom). Inside it: cream .lbl "21st.dev" at x 1040, y 400, and the 21stdev image at x 1040, y 450, 840x525. No hint captions.
- source: ### 2.3 컴포넌트

## S5. DESIGN IDEA, grouped  (dark)
- headline: FONT + COLOR
- text: 원문 조언: Inter는 피하기 / 팔레트는 trending 목록에서
- labels: Fonts In Use, Google Fonts, Coolors
- images:
  - deck/img/sites/fontsinuse.png [cover] — the FONTS IN USE masthead and the grid of real specimens (OT Scholar, Minion, MD UI ...)
  - deck/img/sites/googlefonts.png [cover] — the family list where Google Sans, Lato, Open Sans and Roboto each render "Everyone has the right ..."
  - deck/img/sites/coolors.png [cover] — "Trending Color Palettes" and the swatch-card grid
- placement: FONT + COLOR (d-l 220, 1084 wide) in cream at x 40, y 120. The Korean lines (.txt) at x 1260, y 165, 600 wide. Grouping is drawn, not written: a 2px cream .rule from x 56 to 1236 at y 455 over the two font frames, and a second one from x 1284 to 1864 over Coolors. Three 580x362 frames at y 480, x 56 / 656 (font pair, 20px gap) and 1284 (colour, 48px gap). Under each: cream .lbl site name at y 868. No hint captions, no FONT/COLOR chips (the headline already says it).
- source: ### 2.4 글꼴, ### 2.5 색

## S6. PHOTOGRAPHY  (light, data-hdr="none")
- headline: BONUS
- text: 주제 뒤에 website를 붙여 검색
- labels: Pinterest, lake side cabin website, toools.design, Book of Shapes
- images:
  - deck/img/sites/pinterest.png [cover] — the search bar reading "lake side cabin website" and the masonry of dark cabin-site pins. The 1.66 frame trims about 11px top and bottom, and the search bar stays.
  - deck/img/sites/toools.png [cover, object-position left] — "Discover the Best Design Resources & Tools" and the category tiles; left anchoring keeps the title.
  - deck/img/sites/bookofshapes.png [cover, object-position left] — the black page with the "Book of Shapes" title and pattern thumbnails.
- placement: data-hdr="none". Pinterest at x 0, y 0, 1060x640. Two small frames of 360x300 at y 0: toools at x 1120 and Book of Shapes at x 1510. Under them at y 330: .lbl site name only. Below at x 1120, y 470: .lbl "Pinterest", the Korean line (.txt) at y 512, and an outlined .tag "lake side cabin website" at y 562. BONUS at d-xxl 400 (959 wide) at x 24, bottom -40, bleeding off the bottom.
- source: ### 2.7 보너스

## S7. STATEMENT SPLIT  (light)
- headline: CAPTURE
- text: 붙여 넣은 이미지는 서브에이전트에게 넘어가지 않는다 / 이미지는 ref 폴더에 두고 경로를 적는다
- labels: GoFullPage, Windows + Shift + S, Command + Shift + 4
- images:
  - deck/img/03/gofullpage-hero.png [cover] — derived crop (see notes): GoFullPage logo, "The most reliable full page screenshot in just a single click", the green CTA and the product mock with its tall page strip
- placement: CAPTURE (d-l 220, 702 wide) at x 48, y 130. Image at x 960, y 140, 904x317 (exact ratio). On the left, the three tools as stacked .tag chips at x 56, y 470 / 545 / 620 (GoFullPage filled, the two shortcuts outlined). No hint captions. On the right under the image: Korean line 1 (.lead) at x 960, y 500, and line 2 (.txt) at y 600. Below them, a .code card at x 960, y 680, 904 wide with two lines: `ref/site1.png   좋은 점, 피할 점` / `ref/site2.png   좋은 점, 피할 점`.
- source: ## 3. 참고 자료를 캡처하고 Claude에게 전달하기, ### 3.1 캡처 도구

## S8. STACKED ROWS  (dark)
- headline: DO NOT COPY (two lines: DO NOT / COPY)
- text: 세 프롬프트 모두 Do not copy 문장을 넣었다
- labels: LIKE  Oryzo의 스크롤 움직임, DISLIKE  Anna Jóna의 애니메이션, DISLIKE  Nimmo Bay의 색과 글꼴
- images:
  - deck/img/sites/oryzo.png [cover] — the ORYZO hero: cork coaster on the green cutting mat, big ORYZO logo (the site whose scroll motion Southside asked Claude to study)
  - deck/img/03/annajona-wave.png [cover] — derived crop (see notes): the pink curve cutting into Anna Jóna's bar video (the site whose animation Harbour Lane rejected), without the closure notice
  - deck/img/sites/nimmobay-2.png [cover] — Nimmo Bay's hand-drawn map, misty forest and thin spaced caps (the site whose colours and fonts Blackwater rejected)
- placement: Three 400x250 frames stacked on the left at x 56, y 140 / 455 / 770 (ends y 1020). Each row has one chip to the right of its frame at x 490, vertically centred (y about 245 / 560 / 875): .tag.fill "LIKE  Oryzo의 스크롤 움직임", outlined .tag "DISLIKE  Anna Jóna의 애니메이션" and "DISLIKE  Nimmo Bay의 색과 글꼴" (cream). The Korean line (.lead, cream) at x 1084, y 380, 780 wide (may wrap to two lines). DO NOT / COPY at d-xl 300 in cream, stacked on two lines, right-aligned at right 56, bottom 30 (block 778 wide, 504 tall, top about y 546). No delivery-method labels here; those sit on S10 to S12.
- source: ### 3.3 좋은 점과 싫은 점을 나눠 적기 (규칙 2와 3), ### 3.2 표의 Southside 행 (가져온 특징)

## S9. TAG GRID  (light)
- headline: 16 BLOCKS
- text: 금지 문장은 사용자가 직접 썼다 / 현재 스킬에는 Inter도 보라색도 없다
- labels: 참고 자료, 만들 것과 목표, 레이아웃, 분위기, 색, 금지 항목, 글꼴, 여백과 정렬, 움직임, 문구, 이미지와 영상, 성능, 주인공 시각 요소, 기술 조건, 스스로 확인, 진행 방식, 원문 프롬프트의 금지 항목 (struck: INTER, ROBOTO, OPEN SANS, 보라색, 그라데이션)
- images: 없음 (visual device: 4x4 block grid + struck-out words)
- placement: 16 BLOCKS (d-l 220, 843 wide) at x 40, y 120. A 4x4 grid of outlined boxes, each 300x96 with a 16px gap, from x 56, y 380 (last row ends near y 812). Block names are in BHS 30px, in table order, read left to right. "금지 항목" and "글꼴" are filled ink boxes with cream text. Right column x 1380: .lbl-s "원문 프롬프트의 금지 항목" at y 380, then d-xs words with .strike stacked at y 420 / 490 / 560 (INTER, ROBOTO, OPEN SANS) and .ko d-xs at y 650 / 720 (보라색, 그라데이션). Korean line 1 (.lead) at x 56, y 880 and line 2 (.txt) at y 935.
- source: ## 4. 프롬프트를 구성하는 블록 (블록 표, 표를 읽을 때 알아 둘 점 중 금지 문장과 스킬 판 차이)

## S10. PHOTOGRAPHY  (dark, data-hdr="none")
- headline: SOUTHSIDE
- text: 캔은 Three.js 기본 도형으로 코드에서 / 목표: 가까운 펍이나 가게 찾기
- labels: URL 하나, Oryzo by Lusion: 스크롤 따라 움직이는 3D (figcaption)
- images:
  - assets/guide1-mov/crops/51-southside-brewing.png [cover] — the result: "BIG HOPS. SHORT WALK." over deep teal-black, the amber SOUTHSIDE IPA can with hops, lime "FIND IT NEAR YOU" button and the SOUTHSIDE BREWING pill. Exact ratio at native size, no crop.
  - deck/img/sites/oryzo-2.png [cover] — Oryzo's dark scroll state: the cork coaster floating in 3D next to "ISN'T JUST A COASTER." This is the effect the prompt asked Claude to study.
- placement: data-hdr="none". Result at x 0, y 0, 1110x661, flush with the top-left corner. Oryzo frame at x 1180, y 0, 680x425, with the figcaption "Oryzo by Lusion: 스크롤 따라 움직이는 3D". Under it: .tag "URL 하나" (cream outline) at x 1180, y 460. The Korean lines (.txt, cream) at x 1180, y 530 and 570, 680 wide. SOUTHSIDE in cream at font-size 360 (about 1408 wide) at x 24, bottom -50, bleeding off the bottom.
- source: ## 5. 세 가지 사례, ### 5.1 Southside Brewing, ### 3.2 표 (URL 하나)

## S11. FLOW, references to result  (light)
- headline: HARBOUR LANE
- text: 목표: 동네 사람이 와서 원두 한 봉지 사기
- labels: 스크린샷 세 장 + 먼저 분석, Café Technica: 영상 히어로, La Colombe: 파랑과 빨강, 카드, Anna Jóna: 스토리텔링 (figcaptions)
- images:
  - assets/guide1-mov/crops/50-harbour-lane.png [cover] — the result: "Roasted by the Atlantic." serif headline on off-white, terracotta button, roaster photo and the HARBOUR LANE pill. Exact ratio (1.13), about 1.18x upscale, so keep it at or below this size.
  - deck/img/sites/cafetechnica.png [cover] — white left panel + espresso video hero (the start of the hero that scrolls sideways into full screen)
  - deck/img/sites/lacolombe-2.png [cover] — product cards with the red and blue La Colombe cans and dark bags
  - deck/img/sites/annajona-2.png [cover] — the pink bar interior in a large rounded frame (big image, storytelling mood)
- placement: HARBOUR LANE (d-l 220, 1190 wide) at x 40, y 100. The three references form a column on the left: 360x225 frames at x 56, y 320 / 560 / 800 (ends y 1025), each with its figcaption. A 2px .vrule at x 436 from y 432 to 912 joins the three rows, and a 2px .rule from x 436 to 520 at y 586 points into the result (refs → result). Result at x 540, y 320, 600x532. To the right of the result, at x 1200: .tag.fill "스크린샷 세 장 + 먼저 분석" at y 340 and the Korean line (.lead) at y 410, 660 wide.
- source: ### 5.2 Harbour Lane Coffee, ### 3.2 표 (스크린샷 세 장, 만들기 전에 분석)

## S12. VISUAL DISPLAY  (light)
- headline: BLACKWATER
- text: 목표: 빈 날짜 확인 후 예약
- labels: 링크 세 개 + 내 로고, Nimmo Bay: 사진 히어로 (색과 글꼴은 빼고), Vipp Guesthouses: 어두운 느낌과 얇은 메뉴 막대, Aman Amangiri: 큰 사진과 세리프 제목의 카드 (figcaptions)
- images:
  - assets/guide1-mov/crops/52-blackwater-cabins.png [cover] — the result: lit cabins on a night lake, the serif "...re Adventure / ...ts Tranquility." (cut by the source crop) and the BLACKWATER CABINS pill. Exact ratio (1.16), native size.
  - deck/img/sites/nimmobay.png [cover] — misty island aerial, edge to edge, with the thin wide-spaced "NIMMO BAY" title set low
  - deck/img/sites/vipp-2.png [cover] — dark, high-contrast page: beige serif statement on charcoal, the thin top nav bar, photo cards below
  - deck/img/sites/amangiri-2.png [cover] — Aman's cream page with large photo cards and wide margins (the card pattern the prompt praised)
- placement: Result at x 56, y 130, 470x404. Three reference frames of 420x263 at y 130, x 566 / 1006 / 1446, each with its figcaption (one line, fits 420). .tag.fill "링크 세 개 + 내 로고" at x 56, y 560 under the result. The Korean line (.lead) at x 566, y 440. BLACKWATER at d-xl 300 (1438 wide) at x 40, bottom -40.
- source: ### 5.3 Blackwater Cabins, ### 3.2 표 (링크 세 개, 내 로고), ### 3.3 규칙 1 (Amangiri 카드)

## S13. PRICING PLAN  (dark)
- headline: SET UP
- text: 이미지와 영상 생성 도구는 따로 연결
- labels: SKILL, OPUS, SCREENSHOT (code-card comments: # 코드 전에 계획, 의뢰가 우선 / # Opus로. 기본 서브에이전트도 따라감 / # 서브에이전트도 사용 가능)
- images:
  - deck/img/03/frontend-design-repo.png [cover] — derived crop (see notes): the anthropics/skills repo at skills / skills / frontend-design, which is the folder the original post linked
- placement: SET UP at d-xl 300 (734 wide) in cream at x 40, y 110. Repo strip at x 960, y 130, 904x223 (exact ratio). Three columns start at y 480, at x 56 / 690 / 1314, each 550 wide, with cream .vrule dividers at x 650 and x 1274 (y 470 to 900). Each column has a cream .lbl title (SKILL / OPUS / SCREENSHOT) at y 500 and a .code card at y 560 (font-size 20px inline, wraps to 2-4 lines) whose last line is a gray `.c` comment. Column 1: `claude plugin install frontend-design@claude-plugins-official` + `# 코드 전에 계획, 의뢰가 우선`. Column 2: `/model` + `# Opus로. 기본 서브에이전트도 따라감`. Column 3: `claude plugin install playwright@claude-plugins-official` + `# 서브에이전트도 사용 가능`. The Korean line (.txt, cream) at x 56, y 970 for the generation-tool note. No separate captions.
- source: ## 6. 실행 전에 준비하기 (### 6.1 frontend-design 스킬 설치와 사용, ### 6.2 서브에이전트를 Opus로 돌리기, ### 6.3 스크린샷을 찍을 수 있게 준비하기, ### 6.4 이미지와 영상을 만드는 도구)

## S14. OUR SERVICES, skeleton + loop  (light)
- headline: TEMPLATE
- text: 원문은 gauntlet loop 이름 한 줄뿐 / 템플릿은 루프 절차까지 적었다
- labels: ## 참고 자료, ## 만들 것과 목표, ## 구성: 위에서 아래로, ## 주인공 시각 요소, ## 분위기, ## 색, ## 글꼴과 여백, ## 움직임, ## 문구, ## 이미지와 영상, ## 기술 조건, ## 확인, ## 진행 방식; loop: 조각 나누기, 제작 서브에이전트, 새 맥락에서 평가, 가장 큰 차이 하나; 멈춤: 우리가 이김, 개선 폭이 작음, 상한 도달, 내가 멈춤
- images:
  - deck/img/03/gauntlet-title.png [cover] — derived crop (see notes): Matt Shumer's "How to Run a Gauntlet Loop" title, subtitle and byline, which the template's procedure follows
- placement: TEMPLATE (d-l 220, 818 wide) at x 48, y 120. Korean line 1 (.lead) at x 960, y 140 and line 2 (.txt) at y 196. On the left, the skeleton: 13 stacked bars from x 56 to 880, starting at y 360, each 44 tall with a 6px gap (ends near y 1004). Each bar is a 2px ink outline with the block name in .lbl-s on the left and a pale gray placeholder strip (x 420 to 860, 16 tall) for the [ ] content. The last bar "## 진행 방식" is filled ink with cream text, and a 2px .rule runs from its right end to the panel. On the right, a .block-dark panel at x 960, y 300, 960x780 (bleeds right and bottom). Inside it: gauntlet-title image at x 1000, y 340, 720x340. Below that, a tiny loop drawn with cream outlined .tag chips and 2px cream arrows. The entry chip "조각 나누기" at (1000, 760) points to "제작 서브에이전트" at (1300, 760), then to "새 맥락에서 평가" at (1600, 760), then to "가장 큰 차이 하나" at (1450, 870), and back to 제작. The stop rule is one .cap line at x 1000, y 980.
- source: ## 7. 바로 쓰는 프롬프트 템플릿 (+ ## 4 note that the original prompts only say "Run this as a gauntlet loop for the best result.")

## S15. DIAGRAM + BLEED TITLE  (light)
- headline: THE BAR
- text: 기준은 그 분야 최고의 실제 사이트 / 닿지 못해도 괜찮다
- labels: MAKE IT AMAZING (struck), Matt Shumer: Claude Code + Opus 5, /loop: 횟수로 멈추지 않기
- images:
  - assets/guide1-mov/crops/12-loop-diagram-setup.png [contain] — "THEN LET IT LOOP", 00 LOOPS, the dashed loop carrying v1 and the empty frame under the orange QUALITY BAR. Its cream background blends into the slide.
- placement: Diagram top-right at x 904, y 120, 960x570 (exact ratio, ends y 690). Left column: "MAKE IT AMAZING" in d-xs (64px, 419 wide) with .strike at x 56, y 150. Korean line 1 (.lead) at x 56, y 250, 800 wide, and line 2 (.txt) at y 310. Two .tag chips stacked at x 56, y 400 and y 460. THE BAR at d-xxl 400 (1193 wide) at x 24, bottom -40, bleeding off the bottom (it starts below y 690, so it does not touch the diagram).
- source: ### 8.2 gauntlet loop로 실행하기

## S16. NUMERALS, staggered  (dark)
- headline: RUN
- text: 없음
- labels: 1 새 폴더에서 claude 실행, 2 ref/에 스크린샷과 로고, 3 템플릿 채워 붙여 넣기, 4 질문에 답하고 workbench.md 보기, 5 브라우저로 열어 직접 확인, 예: ref/site1.png, 예: ref/site2.png
- images:
  - deck/img/sites/cafetechnica-2.png [cover] — full-frame espresso close-up, shown as an example reference screenshot file (Harbour Lane's references were screenshots, so this is consistent with the case)
  - deck/img/sites/lacolombe.png [cover] — La Colombe's green matcha hero, the second example file
- placement: RUN at d-xxl 400 (579 wide) in cream at x 40, y 110. Two thumbnails of 360x225 at y 140, x 1100 and x 1500, each with a mono figcaption ("예: ref/site1.png", "예: ref/site2.png"). Numerals (.num 220, cream) in two staggered rows, like ref set2_04. Row 1 at y 500: 1 at x 56, 2 at x 680, 3 at x 1304. Row 2 at y 780: 4 at x 368, 5 at x 992. Each label is one bold .txt line to the right of its numeral (400 wide, padding-top 22). No gray hint lines.
- source: ## 8. 실행하고 확인하기, ### 8.1 실행 순서

## S17. PANORAMA  (light, data-hdr="none")
- headline: CHECK
- text: 수정 요청은 한 번에 문제 하나
- labels: 1440PX, 390PX (Anton numerals), 맨 위, 각 구간, 맨 아래를 두 너비로; checks: 잘림과 끊김 없음, 어두운 배경 글자 대비, 금지 항목 없음
- images:
  - assets/guide1-mov/crops/49-in-action-sites.png [cover] — the three finished pages side by side (Harbour Lane, Southside Brewing, Blackwater Cabins) on cream: the pages you screenshot and check. Exact ratio, no upscale.
- placement: data-hdr="none". Image full-bleed at x 0, y 0, 1920x615. CHECK at d-xl 300 (702 wide) at x 40, bottom -40. Right block from x 800: "1440PX" and "390PX" in d-s 100 at y 650 (x 800 and x 1120), with one .cap at x 1420, y 690 ("맨 위, 각 구간, 맨 아래를 두 너비로"). Then a one-row .check list in three columns (x 800 / 1160 / 1520, 340 wide each) at y 790. The Korean line (.lead) at x 800, y 930.
- source: ### 8.3 확인 지점과 확인 목록

## S18. PORTFOLIO, one big + two stacked  (light)
- headline: DESIGN SYSTEM
- text: 페이지가 정해지면 규칙을 문서 하나로 / 다음 페이지는 이 문서부터 읽게
- labels (figcaptions): Claude Design: /design과 /design-sync, Refero Styles: DESIGN.md 2,000개 이상, Branding Style Guides: 실제 브랜드 가이드 PDF
- images:
  - deck/img/sites/claudedesign.png [cover] — serif "Design your idea with Claude" and the top of the canvas mock (globe landing page)
  - deck/img/sites/referostyles.png [cover] — "A DESIGN.md your AI can follow", the search box and the style cards
  - deck/img/sites/brandingstyleguides.png [cover] — "THE BRANDING GUIDELINES ARCHIVE" and two guide covers (Zarhak Steels, Colour Memory)
- placement: DESIGN SYSTEM (d-l 220, 1265 wide) at x 40, y 110. The two Korean lines (.txt) top-right at x 1340, y 140 and 180, 520 wide. Big Claude Design frame at x 0, y 340, 1000x625 (exact 1.6, bleeds left). Right column: Refero Styles at x 1060, y 340, 500x313 and Branding Style Guides at x 1060, y 680, 500x313. Each frame carries its figcaption (cream box, bottom-left). The space right of the small frames (x 1580 to 1864) stays empty.
- source: ## 9. 디자인 시스템으로 남기기 (### 9.1 Claude Design이나 Claude Code에 정리 요청하기, ### 9.2 Refero Styles의 design.md 쓰기, ### 9.3 Branding Style Guides로 구성 참고하기), ### 2.6 디자인 시스템과 브랜드 가이드

## S19. CREDITS  (light)
- headline: MORE
- text: 없음 (small text is allowed on this slide)
- labels: Fable 5.1 + Claude Code /design (Beginner's Guide), The AI Automators 2026년 9월 2일 16분 11초, 05:08 참고할 화면 보여 주기, 07:31 이미지와 영상용 도구와 스킬, 10:46 아이콘, 11:45 냉정한 크리에이티브 디렉터, 13:34 디자인 시스템으로 정리하기, 15:05 토큰 관리; 출처: 원문 Claude + Design Inspiration: All the Links From the Video (The AI Automators, 2026년 9월 7일), Matt Shumer How to Run a Gauntlet Loop (2026년 7월 27일), frontend-design SKILL.md와 공식 플러그인 판, Claude Code 문서 (플러그인, 스킬, 서브에이전트, Chrome 연동, 데스크톱 앱, 모델 설정, 명령어), 2절 각 사이트와 가격 페이지, What is DESIGN.md, Claude Design 발표, 확인한 날짜 2026년 10월 6일 (가격은 이후 바뀔 수 있음)
- images: 없음 (closing credits slide)
- placement: MORE at d-xl 300 (636 wide) at x 40, y 120. Follow-up video block from x 760: .lbl title at y 140, .cap channel/date/length at y 185. Six chapter .tag chips in a 3x2 grid from x 760, y 260 (columns about 370 apart, rows 64 apart). A 2px .rule at y 520 from x 56 to 1864. Below it, .lbl-s "SOURCES" at x 56, y 550 and the source list as .cap lines in two columns (x 56 and x 980, 860 wide each) from y 600, ending before y 1040.
- source: ## 10. 더 보기, ## 출처

## Coverage
- 문서 도입부 (원문 소개, 원문이 영상에 딸린 링크 모음이라는 점) → S1 (Korean line + source line). The cross-references to HOW_DESIGN.md, GAUNTLET_LOOP.md and GUIDE_NOTE.md are intentionally omitted (pointers to other docs). The check date (2026년 10월 6일) → S19.
- ## 1. 전체 흐름 → S2 (8 steps as one-word labels, one prompt per page, one or two fixes). The definitions in this section go to S13 (skill) and S14/S15 (gauntlet loop: a builder and a fresh-context evaluator, repeated until the work beats the reference or the user stops).
- ## 2. 참고 자료 찾기 → S3, S4, S5, S6, S18. The doc's six categories (2.1 to 2.6) plus the bonus are all shown; S3 pairs 2.1 and 2.2 under REFERENCE, as Part 01 does. No slide states a category count.
  - ### 2.1 디자인 갤러리 → S3 (Awwwards, Siteinspire, Lapa Ninja; Korean line 1).
  - ### 2.2 실제 앱과 웹사이트 → S3 (Mobbin + MCP, Refero; Korean line 2). Refero Styles → S18. The Mobbin MCP setup command and plan conditions are compressed into the "+ MCP" caption.
  - ### 2.3 컴포넌트 → S4 (definition line, Copy prompt line).
  - ### 2.4 글꼴 → S5 (Fonts In Use, Google Fonts, avoid Inter as the author's advice).
  - ### 2.5 색 → S5 (Coolors, trending list).
  - ### 2.6 디자인 시스템과 브랜드 가이드 → S18.
  - ### 2.7 보너스 → S6 (Pinterest with the exact search, toools.design, Book of Shapes).
  - Per-site prices, plan limits, licence notes and counts ('알아 둘 점', checked on 2026년 10월 6일) are left to the source; the screenshots show some counts themselves (21st.dev 12,000+, React Bits 210+). Only Refero Styles' 2,000 stays as text (S18).
- ## 3. 참고 자료를 캡처하고 Claude에게 전달하기 → S7, S8, S10 to S12.
  - ### 3.1 캡처 도구 → S7 (three tools as chips, pasted images do not reach subagents, save to ref/ and write the path with likes and dislikes as a code card).
  - ### 3.2 원문 사례가 쓴 세 가지 전달 방식 → the delivery-method chip on each case slide: S10 "URL 하나", S11 "스크린샷 세 장 + 먼저 분석", S12 "링크 세 개 + 내 로고"; the borrowed traits are the figcaptions. The note that links need a browser tool is covered by S13's SCREENSHOT column.
  - ### 3.3 좋은 점과 싫은 점을 나눠 적기 → S8 (LIKE/DISLIKE chips and "Do not copy"). Rule 1's Amangiri card example → S12 figcaption.
- ## 4. 프롬프트를 구성하는 블록 → S9 (all 16 block names, the font/colour bans, user-written vs current skill). The note that the gauntlet instruction is a single line → S14 text. The note that only Harbour Lane and Blackwater call /frontend-design is compressed out. The note on image/video instructions conflicting inside one prompt is compressed into S13's generation-tool line. The per-block examples are shown only where they become visuals (bans on S9, case traits on S10 to S12).
- ## 5. 세 가지 사례 → S10, S11, S12. The pointer to the full English prompts ('The Prompt' on the original page) is left to the source link on S19.
  - ### 5.1 Southside Brewing → S10 (Oryzo by Lusion, scroll-driven 3D, Three.js can from primitives, goal). Colour, parallax and reduced-motion details are carried by the result image, not by text.
  - ### 5.2 Harbour Lane Coffee → S11 (three screenshot references with what was borrowed, analyse first, goal). The rejected Anna Jóna animation → S8. The skill-default interpretation is folded into S13's SKILL comment ("의뢰가 우선").
  - ### 5.3 Blackwater Cabins → S12 (three link references with what was borrowed and rejected, own logo, goal). The final dark-background readability check → S17 check item 2.
- ## 6. 실행 전에 준비하기 → S13.
  - ### 6.1 frontend-design 스킬 설치와 사용 → S13 column 1 (install command, plan first, the brief wins) + repo image. The version difference (Inter, Roboto, purple not in the current skill) → S9 text line 2.
  - ### 6.2 서브에이전트를 Opus로 돌리기 → S13 column 2 (/model, default subagents follow the main model). The env vars and /effort ultracode are compressed out.
  - ### 6.3 스크린샷을 찍을 수 있게 준비하기 → S13 column 3 (Playwright plugin, usable by subagents). Claude in Chrome, the Desktop Code tab and /run, /verify are compressed out.
  - ### 6.4 이미지와 영상을 만드는 도구 → S13 Korean line.
- ## 7. 바로 쓰는 프롬프트 템플릿 → S14 (13 template blocks as a skeleton, the gauntlet procedure as a tiny loop with stop rules, Matt Shumer article image). The template text itself is intentionally not pasted. The fill rules show up visually as "## name + [ ] placeholder" bars.
- ## 8. 실행하고 확인하기 → S15, S16, S17.
  - ### 8.1 실행 순서 → S16 (five steps, example ref/ files).
  - ### 8.2 gauntlet loop로 실행하기 → S15 (bar = best real site, "Make it amazing" is not a bar, falling short is fine, Matt Shumer's Claude Code + Opus 5, no fixed loop count and /loop). The ultracode cost remark and the generator page (email signup, 5 prompts a day, no-skill session advice) are compressed out.
  - ### 8.3 확인 지점과 확인 목록 → S17 (top, each section and bottom at 1440px and 390px; the 10 checks compressed to 3; one fix per request). Mobile layout, one CTA per screen, reduced motion, fallback, keyboard focus and page size are dropped in the compression.
- ## 9. 디자인 시스템으로 남기기 → S18.
  - ### 9.1 → S18 (Claude Design image, /design and /design-sync, "다음 페이지는 이 문서부터"). The launch date and plan availability are compressed out.
  - ### 9.2 → S18 (DESIGN.md, 2,000개 이상). The "pair it with a full-page capture" advice is compressed out.
  - ### 9.3 → S18.
- ## 10. 더 보기 → S19 (follow-up video title, date, length, six chapters). The Autoblitz example and the "5 traits, 6 fixes" summary are compressed out.
- ## 출처 → S19 (short source list and check date). The closing line about the fluent-korean writing guide is intentionally omitted (meta note about how the doc was proofread).

## Review log
- Accuracy, S8 image: the old column 2 used `annajona.png`, whose largest text is "Anna Jóna has been closed." That fact is not in HOW_DESIGN_FROM_CC.md and would read as a claim at 560 px. Replaced with the new derived crop `deck/img/03/annajona-wave.png` (curve + bar video, no notice).
- Accuracy, notes: the cross-part note said only 50 and 52 appear in Part 01 S1 and that Part 01 uses crop 08. Part 01 S1 actually shows 51 as its big image (plus 50 and 52), and Part 01 uses 06, not 08. Note corrected. The coverage line "five-category framing" contradicted the source ("여섯 분류"); reworded.
- Accuracy, wording: S11 "La Colombe: 파랑과 빨강의 카드" merged two separate traits into "blue and red cards"; now "파랑과 빨강, 카드". S12 "Nimmo Bay: 사진 히어로와 가는 글자 (색과 글꼴은 빼고)" read as a contradiction (liked thin letters, rejected fonts); now "사진 히어로 (색과 글꼴은 빼고)". "어두운 대비" → "어두운 느낌" (source and 3.2 table wording). S16 step 5 no longer implies `open index.html` is the main method ("브라우저로 열어 직접 확인"; `open` is the Mac shortcut in the source).
- Minimal text: cut every slide to one headline + at most 2 Korean lines + about 4 tiny labels. Removed the gray hint line under all 8 steps (S2) and 5 steps (S16); removed per-site hint captions on S3, S4, S5, S6 and S18 (site names stay as figcaptions or labels); removed the FONT/COLOR chips on S5 (grouping is now drawn with two rules and a wider gap); S7 tool hints removed (chips only); S10 to S12 now use one figcaption per reference instead of label + caption pairs, and one goal line; S13 column captions moved into gray comments inside the code cards; S15 went from 4 chips + date to 2 chips (date sits in the S14 image byline); S17's six sentence-style checks became 3 short checks + "1440PX / 390PX" numerals; S19 lost the Autoblitz sentence.
- S8 refocused: it used to repeat the S10 to S12 mapping (delivery method + case name + chip per column, 9 labels). It now carries only 3.3 (LIKE / DISLIKE / Do not copy) with 3 chips + 1 line, and the delivery methods live once, as chips, on each case slide (S11 "스크린샷 세 장 + 먼저 분석", S12 "링크 세 개 + 내 로고").
- Layout variety: S8 was the same OUR TRAM pattern as S1 (dark, three frames across + title bottom); it is now three stacked image rows on the left with DO NOT / COPY stacked bottom-right. S11 and S12 were the same "result + three refs in a row" layout back to back; S11 is now a refs-column → result flow. S18 was the fourth "title + three frames in a row" slide (after S1, S5, S8); it is now a PORTFOLIO variant (one big frame + two stacked). S15 had the same title-top-left + visual-right split as S14; THE BAR now bleeds along the bottom under a top-right diagram.
- Rhythm: dark slides cut from 7 to 6 (S18 is now light), matching the ref's occasional-black use. No two consecutive slides share a layout.
- Image crops: S1 card 26 now anchors left and cards 31 and 34 anchor top, because the centre cover clipped the AWWWARDS and 21ST.DEV name pills (checked with a PIL simulation). S4 React Bits frame grew to 880x450 after its caption was removed. All other frames were simulated and keep their key content.
- Missing files: the three derived crops named in the notes did not exist; they and the new `annajona-wave.png` were created in `deck/img/03/` with the listed boxes and checked by eye. All other paths exist (ls).
- Korean: lines tightened (S7 "넘어가지 않는다" as in the source, S11 goal as a noun phrase, S14 stop rule as noun phrases "우리가 이김, 개선 폭이 작음, 상한 도달, 내가 멈춤"). No middle dot character in any slide text; the dots visible inside the GoFullPage and Gauntlet screenshots belong to those pages.
