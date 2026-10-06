# Claude Code로 랜딩 페이지 만들기: 원문 사례 따라 하기

이 문서는 The AI Automators가 2026년 9월 7일에 올린 [Claude + Design Inspiration: All the Links From the Video](https://www.theaiautomators.com/claude-design-inspiration-all-the-links-from-the-video/)(이하 원문)를 바탕으로 썼습니다. 원문은 The AI Automators가 올린 영상에 딸린 글이며, 그 영상에 나온 사이트와 도구, 프롬프트를 나온 순서대로 모았습니다. 이 문서는 원문이 랜딩 페이지(광고나 링크를 눌러 들어온 방문자가 처음 보게 되는 한 페이지짜리 소개 페이지) 세 개를 만들 때 실제로 쓴 도구와 링크, 프롬프트 구성을 정리합니다. 그리고 Claude Code에서 같은 방법을 따라 하는 절차를 설명합니다.

같은 폴더에 있는 [HOW_DESIGN.md](HOW_DESIGN.md)는 참고 자료 고르기부터 검토와 기록까지 일반 원칙을 다루며, 개별 사이트와 예시 프롬프트는 일부러 뺐습니다. [GAUNTLET_LOOP.md](GAUNTLET_LOOP.md)는 만드는 AI와 평가하는 AI를 나눠 반복하는 방법을, [GUIDE_NOTE.md](GUIDE_NOTE.md)는 막연한 요청이 평균적인 결과로 이어지는 이유를 설명합니다. 이 문서는 반대로 원문에 나온 개별 사이트와 프롬프트 구성, 세 사례를 구체적으로 다룹니다. 일반 원칙은 위 문서에 맡기고 필요한 곳에 링크만 겁니다. 사이트 정보와 가격은 2026년 10월 6일에 확인했으며, 이후 바뀔 수 있습니다.

## 1. 전체 흐름

원문은 세 페이지를 만든 방법을 한 문장으로 밝힙니다. 각 페이지는 프롬프트 하나로 만들었고, [frontend-design 스킬](https://github.com/anthropics/skills/tree/main/skills/frontend-design)과 함께 [gauntlet loop](https://somethingbig.ai/gauntlet-loop)로 실행한 다음 한두 번 고쳤다고 합니다. 이 과정을 단계로 나누면 다음과 같습니다.

1. Claude Code를 준비합니다. frontend-design 스킬을 설치하고, 모델을 Opus로 정하고, 스크린샷을 찍을 브라우저 도구를 연결합니다(6절).
2. 참고할 사이트를 찾습니다(2절).
3. 마음에 드는 부분을 캡처하거나 링크를 모읍니다(3절).
4. 참고 자료와 목표, 디자인 규칙을 프롬프트 하나에 담습니다(4~5절, 7절).
5. Claude Code에서 프롬프트를 frontend-design 스킬과 gauntlet loop로 실행합니다(8절).
6. Claude가 스크린샷을 찍어 스스로 확인하게 합니다(8절).
7. 결과를 보고 한두 번 고칩니다(8절).
8. 페이지 디자인이 정해지면 색, 글꼴, 간격, 부품 규칙을 한곳에 모은 디자인 시스템 문서로 남겨 다음 작업에 다시 씁니다(9절).

스킬은 Claude Code가 필요할 때 불러 쓰는 작업 지침 묶음입니다. frontend-design은 Anthropic이 공개한 화면 디자인용 스킬입니다. gauntlet loop는 Matt Shumer가 소개한 방식입니다. 이 방식은 만드는 AI와 평가하는 AI를 나눕니다. 만드는 AI는 결과물이 기준으로 삼은 실제 사이트보다 낫다고 평가받거나 사용자가 멈출 때까지 결과물을 계속 고칩니다.

## 2. 참고 자료 찾기

원문은 참고 자료를 여섯 분류로 나누고 보너스 세 곳을 더합니다. 표에 있는 '원문 예시'는 원문이 함께 연결한 개별 페이지이며, 대부분 영상에서 실제로 열어 본 페이지입니다. '알아 둘 점'은 2026년 10월 6일에 각 사이트를 확인한 결과입니다. 다만 Lapa Ninja는 접속이 막혀서, 2026년 10월 3일에 저장된 Wayback Machine(웹 페이지의 예전 모습을 보관하는 서비스) 사본으로 확인했습니다. 어떤 결정에 어떤 자료가 맞는지는 [HOW_DESIGN.md](HOW_DESIGN.md) 2절에 정리되어 있습니다.

### 2.1 디자인 갤러리

잘 만든 웹사이트를 모아 보여 주는 곳입니다. 페이지 전체의 구성과 분위기를 정할 때 봅니다.

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Awwwards](https://www.awwwards.com/) | 오늘의 사이트, 후보작, 우수작을 분야나 기능으로 거름. 예: [Architecture](https://www.awwwards.com/websites/architecture/), [360](https://www.awwwards.com/websites/360/) | [Storey Architecture](https://www.storeyarchitecture.co.uk/), [Normal Is Boring](https://normalisboring.es/), [Louisiana Governor's Mansion 투어](https://www.governorsmansion.org/tour/foyer) | 수상작은 무료로 볼 수 있음. 유료 Pro 플랜은 제작사를 목록에 올리는 용도라 보는 데는 필요 없음 |
| [Siteinspire](https://www.siteinspire.com/) | 스타일, 종류, 주제, 플랫폼으로 거름 | [Children](https://www.siteinspire.com/websites/category/children) 분류에 있는 [Lang Mobile](https://langmobile.com/en/) | 스타일, 종류, 주제 필터는 확인함. 플랫폼 필터는 접속이 막혀 확인하지 못함 |
| [Lapa Ninja](https://www.lapa.ninja/) | 랜딩 페이지 모음. 색, 업종, 분류 필터와 Motion 메뉴가 있음 | [Sharplink](https://www.lapa.ninja/post/sharplink/) | 2015년부터 모은 랜딩 페이지 7,300개 이상. Fonts, Sections 메뉴도 있음. 유료 Pro 가격은 확인하지 못함 |

### 2.2 실제 앱과 웹사이트

실제로 출시된 제품 화면을 모은 곳입니다. 가입 화면이나 가격표를 실제 제품이 어떻게 만들었는지 볼 때 씁니다. 플로우는 가입이나 결제처럼 여러 화면으로 이어지는 사용 과정을 말합니다.

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Mobbin](https://mobbin.com/) | 실제 화면 60만 개 이상을 [Apps](https://mobbin.com/discover/apps/web/latest)와 [Sites](https://mobbin.com/discover/sites/latest)로 나눠 보여 줌. [Mobbin MCP](https://mobbin.com/mcp)(Claude가 외부 서비스를 도구로 쓰게 하는 연결 방식, 아래 설명 참고)를 연결하면 Claude가 직접 검색함 | [Cosmos](https://www.cosmos.so/) | 확인한 날 기준 화면 621,500개. 원문은 녹화 당시 가격을 '월 약 $10'으로 적음. 현재 Pro의 월 $10은 연간 결제($120)를 달로 나눈 값이고, 월 단위 결제는 없음. 분기 결제는 월 $15. 무료 플랜은 일부만 보이고 검색과 MCP를 쓸 수 없음 |
| [Refero](https://refero.design/) | 실제 웹과 iOS 앱을 [화면과 플로우](https://refero.design/search)로 보여 줌 | 없음 | 무료 플랜은 검색 결과 수가 제한됨. 플로우와 Refero MCP는 Pro($120/년)부터 |
| [Refero Styles](https://styles.refero.design/) | 스타일마다 design.md(AI가 읽도록 색, 글자, 간격 같은 디자인 규칙을 적은 마크다운 파일)를 제공. 원문은 전체 페이지 캡처와 함께 쓰라고 권함 | [Stripe](https://stripe.com/) | 9.2절 참고 |

MCP는 Claude가 외부 서비스의 기능을 도구로 쓰게 해 주는 연결 방식입니다. 원문은 무료 플랜을 언급한 바로 뒤에 Mobbin MCP를 소개하지만, Mobbin MCP는 Pro, Team, Enterprise 플랜에서만 쓸 수 있습니다. 연결하면 Claude가 화면(`search_screens`), 플로우(`search_flows`), 웹사이트 구간(`search_sections`)을 자연어로 검색합니다. Claude 데스크톱이나 웹의 Customize > Connectors에서 Mobbin을 연결해 두면 Claude Code도 같은 커넥터를 씁니다. 터미널만 쓴다면 `claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp`를 실행한 뒤 `/mcp`에서 Authenticate를 고르고 Mobbin에 로그인합니다.

### 2.3 컴포넌트

컴포넌트는 버튼, 갤러리, 배경처럼 화면을 이루는 부품입니다.

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [21st.dev](https://21st.dev/) | 컴포넌트, 템플릿, 테마. 항목마다 Copy prompt 버튼이 있음 | [WebGL shader hero](https://21st.dev/@designali-in/components/web-gl-shader), [animated scroll gallery](https://21st.dev/@youcefbnm/components/animated-gallery/animated-scroll-gallery) | React와 Tailwind로 만든 항목 12,000개 이상. 복사한 프롬프트를 Claude Code에 붙여 넣으면 에이전트가 내 코드 안에 같은 부품을 만듦. 무료 계정은 복사가 하루 2회로 제한됨. 무제한은 Builder 플랜(연간 결제 시 월 $6) |
| [React Bits](https://reactbits.dev/) | 움직이는 컴포넌트와 배경 | [Topography 배경](https://reactbits.dev/backgrounds/topography) | 무료 오픈소스이며 200개 이상. 라이선스가 MIT + Commons Clause라서 내 사이트 안에서는 상업적으로 써도 되지만 컴포넌트 자체를 팔거나 다시 배포하면 안 됨 |

### 2.4 글꼴

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Fonts In Use](https://fontsinuse.com/) | 실제 물건과 인쇄물, 웹에 쓰인 글꼴 사례. 일부는 유료 글꼴 | [Albra](https://fontsinuse.com/typefaces/101276/albra) | 글꼴을 파는 곳이 아니라 사용 사례를 모은 곳. 서체, 매체, 주제로 찾을 수 있고 무료로 볼 수 있음 |
| [Google Fonts](https://fonts.google.com/) | 무료이고 웹 페이지에 바로 넣을 수 있음. 원문은 Inter를 피하라고 함 | 없음 | 상업적으로 써도 됨. Inter도 Google Fonts에 있으며, 피하라는 말은 원문 글쓴이의 스타일 조언 |

### 2.5 색

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Coolors](https://coolors.co/) | 팔레트(함께 쓰는 색 묶음) 1천만 개 이상과 생성기. 원문은 [trending](https://coolors.co/palettes/trending) 목록을 보고 [most popular](https://coolors.co/palettes/popular) 목록은 건너뜀 | [영상에서 쓴 팔레트](https://coolors.co/palette/335c67-fff3b0-e09f3e-9e2a2b-540b0e) | '1천만 개 이상'은 Pro 플랜 기준. 무료 플랜은 준비된 팔레트 1만 개 이상, 팔레트 하나에 최대 5색 |

### 2.6 디자인 시스템과 브랜드 가이드

디자인 시스템은 색, 글꼴, 간격, 부품 규칙을 한곳에 모은 문서입니다.

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Branding Style Guides](https://brandingstyleguides.com/) | 실제 브랜드 가이드 PDF 모음. 원문은 [most popular](https://brandingstyleguides.com/most-popular-manuals/) 목록부터 보라고 권함 | [Coca-Cola](https://brandingstyleguides.com/guide/coca-cola-2020/), [Mercedes-Benz](https://brandingstyleguides.com/guide/mercedes-benz/) | PDF는 무료로 가입해 로그인한 뒤 받음. Coca-Cola 2020 항목은 브랜드 전체 가이드가 아니라 아이콘 디자인 시스템 문서 |
| [Refero Styles](https://styles.refero.design/) | 스타일마다 미리 만든 design.md | 없음 | 9.2절 참고 |
| [Claude Design](https://claude.com/product/design), [Claude Code](https://claude.com/product/claude-code) | 페이지 디자인이 정해지면 디자인 시스템으로 정리하게 하고 모든 결과물에 다시 씀 | 없음 | 9.1절 참고 |

### 2.7 보너스

| 사이트 | 용도 | 원문 예시 | 알아 둘 점 |
| --- | --- | --- | --- |
| [Pinterest](https://www.pinterest.com/) | 주제 뒤에 "website"를 붙여 검색 | [lakeside cabin website 검색 결과](https://www.pinterest.com/search/pins/?q=lake%20side%20cabin%20website) | 5.3절 Blackwater Cabins와 같은 주제로 검색한 예 |
| [toools.design](https://www.toools.design/) | 디자인 자료 목록. 무료와 유료를 태그로 표시 | 없음 | 자료 2,200개 이상. 태그는 Free, Paid, Freemium, Free Trial 등으로 더 나뉨 |
| [Book of Shapes](https://www.bookofshapes.com/) | 값을 바꿔 쓸 수 있는 SVG(크기를 바꿔도 깨지지 않는 그림 형식) 패턴 | 없음 | 상업용을 포함해 무료이고 출처 표기도 필요 없음. 패턴 자체를 묶어 다시 배포하거나 팔면 안 됨. 기존 작품을 재현한 패턴 3개는 게시나 판매가 금지됨 |

## 3. 참고 자료를 캡처하고 Claude에게 전달하기

### 3.1 캡처 도구

| 도구 | 용도 | 알아 둘 점 |
| --- | --- | --- |
| [GoFullPage](https://gofullpage.com/) | 페이지 전체를 한 장으로 저장할 때 | 무료 Chrome 확장. 아이콘을 누르거나 Alt + Shift + P를 누르면 페이지를 스크롤하며 찍음. 원문은 PNG 한 장이라고 썼지만 JPEG와 PDF로도 내보낼 수 있음 |
| Snipping Tool (Windows + Shift + S) | 부품 하나만 찍거나, 애니메이션이 시작하기 전과 끝난 뒤의 화면을 찍을 때 | Windows 캡처 도구 |
| Command + Shift + 4 | Mac에서 같은 용도 | macOS 기본 캡처 단축키. 원문에는 Snipping Tool 항목에 함께 적혀 있음 |

원문은 찍은 이미지를 [Claude Code](https://claude.com/product/claude-code)나 [Claude Desktop 앱](https://claude.com/download)에 붙여 넣고, 마음에 드는 점과 피할 점을 함께 말하라고 합니다. 다만 대화에 붙여 넣은 이미지는 서브에이전트(메인 Claude가 일을 나눠 맡기는 별도 에이전트, 6.2절)에게 넘어가지 않습니다. 서브에이전트는 메인 대화와 다른 새 맥락에서 일하기 때문입니다. 그래서 gauntlet loop처럼 평가를 서브에이전트에게 맡길 때는 이미지를 작업 폴더 안에 저장하고(예: `ref/site1.png`, `ref/site2.png`), 프롬프트에 이 경로를 적습니다. 그러면 서브에이전트도 Claude Code에 기본으로 들어 있는 Read 도구로 같은 이미지를 열어 볼 수 있습니다. 마음에 드는 점과 피할 점은 경로 옆에 함께 적습니다.

### 3.2 원문 사례가 쓴 세 가지 전달 방식

세 사례는 참고 자료를 각각 다른 방식으로 전달했습니다. 아래 표에서 히어로는 페이지를 열면 처음 보이는 큰 화면을 말합니다.

| 전달 방식 | 사례 | 프롬프트에서 한 일 | 가져온 특징 |
| --- | --- | --- | --- |
| URL 하나 | Southside Brewing | Oryzo 주소를 주고 스크롤할 때 어떻게 움직이는지 공부하라고 함. 물체와 색, 레이아웃은 내 것을 쓰겠다고 밝힘 | 스크롤에 따라 3D 물체가 움직이는 효과 |
| 스크린샷 세 장 | Harbour Lane Coffee | 스크린샷을 붙여 넣고, 만들기 전에 분석해서 내 디자인 취향을 이해하라고 함 | 영상 히어로, 색과 카드, 스토리텔링(이야기를 따라가듯 내용을 풀어 가는 방식) 구간 |
| 링크 세 개 | Blackwater Cabins | 링크마다 좋은 점을 적고 원하지 않는 점도 밝힘. 내 로고를 첨부함 | 사진 히어로, 어두운 느낌과 메뉴 막대, 카드 |

링크만 주는 방식은 Claude가 그 페이지를 직접 열어 볼 수 있어야 제대로 작동합니다. 화면 모습까지 보게 하려면 6.3절의 브라우저 도구를 연결해야 합니다. 정지 화면만으로는 움직임을 다 전달하기 어렵다는 점도 기억해 둡니다. 움직임을 참고할 때 무엇을 기록할지는 [HOW_DESIGN.md](HOW_DESIGN.md) 2절에 있습니다.

### 3.3 좋은 점과 싫은 점을 나눠 적기

세 프롬프트는 참고 자료를 전달할 때 세 가지를 지킵니다.

1. 사이트마다 어느 부분이 좋은지 구체적으로 적습니다. Blackwater Cabins는 Aman Amangiri의 카드가 좋다고 적었습니다. 이 카드는 큰 사진 한 장에 작은 라벨과 세리프(획 끝에 작은 돌기가 있는 글꼴) 제목을 얹고, 둘레에 여백을 넉넉히 둔 형태입니다. 사이트 이름만 대고 끝내지 않습니다.
2. 싫은 점과 가져오지 않을 점도 적습니다. Harbour Lane Coffee는 Anna Jóna의 애니메이션이 싫다고 밝혔습니다. Blackwater Cabins는 Nimmo Bay의 색과 글꼴을 원하지 않는다고 적었습니다.
3. 복사하지 말고 영감만 얻으라고 적습니다. 세 프롬프트 모두 "Do not copy"로 시작하는 문장을 넣었습니다. 관찰한 특징을 내 페이지에 맞는 디자인 결정으로 바꾸는 방법은 [HOW_DESIGN.md](HOW_DESIGN.md) 3절에서 다룹니다.

## 4. 프롬프트를 구성하는 블록

세 프롬프트는 길이와 순서가 조금씩 다르지만, 같은 블록(프롬프트에서 한 가지 주제를 다루는 문단)으로 이루어져 있습니다. 아래 표는 블록마다 무엇을 쓰는지 설명하고, 원문 사례를 짧게 보여 줍니다.

| 블록 | 무엇을 쓰는지 | 원문 사례 |
| --- | --- | --- |
| 참고 자료 | 사이트별 좋은 점과 싫은 점, 복사하지 말라는 문장 | 3절 참고 |
| 만들 것과 목표 | 브랜드와 사업 설명, 방문자가 할 행동 하나 | Harbour Lane: 골웨이에 있는 작은 스페셜티 커피 로스터(품질이 높은 원두를 직접 볶아 파는 가게). 동네 사람이 가게에 와서 원두 한 봉지를 사게 하기 |
| 레이아웃 | 위에서 아래로 놓을 구간과 구간마다 들어갈 내용 | Blackwater: 사진 히어로, 장소 소개, 오두막 카드 세 장, 주말 일정 아이콘 네 개, 손님 후기 하나, 예약 구간, 푸터(페이지 맨 아래 영역) |
| 분위기 | 형용사 두세 개에 구체적인 장면 하나를 덧붙여 표현 | Southside: 대담하고 수제품다운 느낌. 금요일 저녁의 탭룸(양조장에 딸린 술집) 같은 분위기. Blackwater: 어둡고 영화 같으며 조용한 느낌. 해 질 녘 오두막에 불이 켜진 호숫가에 도착하는 장면 |
| 색 | 배경색, 글자색, 강조색 하나와 강조색을 쓸 곳 | Blackwater: 짙은 차콜(검정에 가까운 회색) 배경, 따뜻한 오프화이트(누런 기가 도는 흰색) 글자, 앰버(호박색) 강조색은 버튼, 링크, 가격에만 |
| 금지 항목 | 쓰지 않을 색과 효과 | Southside: 보라색 금지, UI(버튼과 글자 같은 화면 요소)에서 그라데이션 금지. Blackwater: 보라색과 그라데이션 금지. Harbour Lane: 그라데이션 금지 |
| 글꼴 | 제목용 하나, 본문용 하나, 본문 크기 16~18px, 쓰지 않을 글꼴 | 세 사례 모두 Inter, Roboto, Open Sans 금지. 제목용은 Southside가 굵고 폭이 좁은 글꼴, Harbour Lane이 세리프, Blackwater가 자간(글자 사이 간격)이 넓은 세리프 |
| 여백과 정렬 | 간격 단위와 정렬 원칙 | Harbour Lane: 8포인트 간격 체계(간격을 8px 단위로 맞추는 방식), 여백을 가장 우선하는 원칙, 모든 요소를 가운데로 몰지 않기 |
| 움직임 | 무엇이 언제 어떻게 움직이는지와 피할 움직임 | Harbour Lane: 구간이 나타날 때 은은하게 떠오르기, 튀어 오르는 움직임 금지. Blackwater: 움직이는 구간과 조용한 구간을 번갈아 두기 |
| 문구 | 말투, 읽을 사람과 대상이 아닌 사람, 화면마다 방문자에게 요청할 행동 하나 | Blackwater: 조용한 주말을 원하는 커플과 작은 가족이 대상이고 모험 여행객은 대상이 아님. 화면마다 방문자에게 요청하는 행동은 '빈 날짜 확인' 하나 |
| 이미지와 영상 | 생성 도구로 만들지, 사진 자리를 비워 둘지 | Blackwater, Southside: 쓸 수 있는 이미지 모델과 영상 모델로 자료 생성. Southside는 캔 자체는 이미지 파일 없이 코드로 만들라고 함. Harbour Lane: 히어로와 커피 사진 자리는 분명히 비워 두되, 첫 화면 영상은 영상 생성 도구로 만들게 함 |
| 성능 | 페이지 크기, 움직임 줄이기 설정(운영체제에서 화면 움직임을 줄여 달라고 지정하는 설정), 대체 화면 | Southside: 페이지 전체 1MB 미만, 기기 픽셀 비율(고해상도 화면에서 더 촘촘하게 그리는 배율) 최대 2, WebGL(브라우저에서 3D를 그리는 기술)을 쓸 수 없으면 움직이지 않는 히어로 표시 |
| 주인공 시각 요소 | 히어로에 놓을 3D 물체나 대표 이미지의 생김새, 재질, 조명, 만드는 방법 | Southside: 캔을 원통, 고리, 살짝 볼록한 뚜껑 같은 기본 도형으로 코드에서 만듦. 금속 재질에 은은한 반사와 얇은 물방울 막을 입히고, 3점 조명(세 방향에서 비추는 사진 촬영용 조명)과 따뜻한 환경광(주변에서 고르게 비치는 빛)으로 실제 사진처럼 보이게 함 |
| 기술 조건 | 파일 형태와 라이브러리 | Harbour Lane, Blackwater: HTML 파일 하나. Southside: Three.js를 CDN(라이브러리 파일을 내려받는 공개 서버)에서 고정 버전으로 불러오기 |
| 스스로 확인 | 스크린샷을 찍을 위치와 화면 크기, 고칠 문제 | Southside: 맨 위, 각 장면, 맨 아래를 데스크톱과 휴대폰 크기로 찍고, 잘리거나 읽기 어렵거나 끊기는 곳을 고친 뒤 보고 |
| 진행 방식 | 쓸 스킬, 서브에이전트, gauntlet loop, 시작 전 질문 | Harbour Lane, Blackwater: `/frontend-design` 스킬 사용, 시작 전에 질문하기. Southside, Blackwater: Opus 서브에이전트 사용. 세 사례 모두 gauntlet loop |

표를 읽을 때 알아 둘 점이 네 가지 있습니다.

- gauntlet loop 지시는 이름 한 줄뿐입니다. 세 프롬프트는 끝에 "Run this as a gauntlet loop for the best result."라는 문장만 붙였고, 평가자를 따로 두거나 블라인드 비교(어느 쪽이 누구 결과물인지 모르게 하고 비교하는 방식)를 하라는 지시는 없습니다. gauntlet loop는 Matt Shumer가 2026년 7월 27일에 글로 소개한 방식입니다. 모델이 이름만 보고 이 절차를 알아서 따르기는 어렵습니다. 그래서 7절 템플릿에는 절차를 직접 적었습니다.
- `/frontend-design` 스킬을 프롬프트에서 직접 부른 사례는 Harbour Lane과 Blackwater 두 개입니다. Southside 프롬프트에는 스킬 이름이 없습니다.
- 글꼴 금지(Inter, Roboto, Open Sans)와 색 금지(보라색, 그라데이션)는 사용자가 프롬프트에 직접 쓴 문장입니다. 현재 frontend-design 스킬에는 Inter, Roboto, Open Sans, 보라색이라는 단어가 없습니다. 그라데이션은 '히어로의 그라데이션 강조'와 'SaaS(구독형 소프트웨어) 사이트에 흔한 카드 묶음의 장식용 그라데이션'처럼, AI가 자주 쓰는 기본값을 설명하는 예로만 나옵니다(6.1절).
- 이미지와 영상 지시는 한 프롬프트 안에서 서로 부딪치기도 합니다. Harbour Lane은 히어로 사진 자리를 비워 두라고 하면서 첫 화면 영상은 생성하라고 했습니다. Southside는 캔을 만들 때 이미지 파일을 쓰지 말라고 하면서, 끝에서는 이미지와 영상 생성 도구를 쓰라고 했습니다. 내 프롬프트에서 두 방식을 섞는다면 어떤 자료를 생성하고 어떤 자리를 비울지 나눠 적습니다.

## 5. 세 가지 사례

프롬프트 전문은 원문 페이지에서 사례 제목 아래 'The Prompt' 항목에 영어로 실려 있습니다. 원문 사례를 그대로 따라 하려면 그 영어 프롬프트를 복사해 쓰고, 내 프로젝트에 맞추려면 7절 템플릿을 씁니다. 여기서는 사례마다 참고 사이트와 가져온 점, 만든 것과 목표, 눈에 띄는 지시만 요약합니다.

### 5.1 Southside Brewing

- 참고 사이트: 스튜디오 [Lusion](https://lusion.co/)이 만든 [Oryzo](https://oryzo.ai/)입니다. 스크롤에 따라 3D 물체가 움직이는 효과를 참고했습니다.
- 만든 것과 목표: 작은 동네 양조장 Southside Brewing과 대표 맥주 Southside IPA를 알리는 한 페이지짜리 랜딩 페이지입니다. 이 맥주는 동네 펍과 가게에서 캔으로 팝니다. 목표는 방문자가 가까운 펍이나 가게를 찾게 하는 것입니다.
- 눈에 띄는 지시:
  - Three.js(웹에서 3D를 그리는 자바스크립트 라이브러리)를 써서 페이지를 3D 장면으로 만듭니다. 캔은 원통과 고리 같은 기본 도형으로 코드에서 직접 만들고, 라벨은 캔버스(코드로 그림을 그리는 웹 요소)에 그려 입힙니다. 외부 3D 모델 파일이나 이미지 파일은 쓰지 않습니다. 캔에는 금속 재질과 은은한 반사, 얇은 물방울 막을 입히고, 3점 조명과 따뜻한 환경광을 써서 실제 사진처럼 보이게 합니다.
  - 색은 짙은 청록 배경, 탁한 호박색 캔, 따뜻한 오프화이트 글자로 정합니다. 밝은 홉 라임 강조색은 버튼과 링크, ABV(알코올 도수) 표시에만 씁니다.
  - 캔은 혼자 천천히 돌고, 마우스를 따라 조금 기웁니다. 스크롤하면 카메라가 세 장면(첫 화면, 맛 소개, 판매처 찾기)을 지나갑니다.
  - 캔 앞에 홉 꽃송이와 떠다니는 거품 같은 투명한 층을 두고 패럴랙스를 줍니다. 패럴랙스는 앞뒤 층이 서로 다른 속도로 움직여 깊이가 느껴지게 하는 효과입니다.
  - 3D 장면 위에 HTML 글자를 얹습니다. 맛 소개 장면에서는 맛 표현 세 가지가 하나씩 나타날 때마다 그 표현에 맞는 카드가 밝아집니다. 판매처 찾기 장면에는 펍과 가게 목록, 우편번호 검색 칸이 들어갈 자리를 둡니다.
  - 대표 맥주 외에 앰버 에일, 스타우트 같은 다른 맥주도 보여 줍니다. 글과 이미지, 로고는 모두 지어내도 된다고 적었습니다.
  - 움직임 줄이기 설정을 켠 사용자에게는 회전과 패럴랙스를 멈춥니다.

### 5.2 Harbour Lane Coffee

- 참고 사이트: 세 곳을 스크린샷으로 붙여 넣었습니다.
  - [Café Technica](https://www.cafetechnica.com.au/): 자동 재생되는 영상 히어로가 가로로 스크롤되며 전체 화면이 되고, 그다음 페이지가 세로로 이어지는 구성.
  - [La Colombe](https://www.lacolombe.com/): 파랑과 빨강을 쓴 색 구성, 큰 이미지, 카드.
  - [Anna Jóna](https://www.annajona.is/): 화면 전환과 스토리텔링, 큰 글자와 이미지. 다만 이 사이트의 애니메이션은 싫다고 밝혔습니다.
- 만든 것과 목표: 골웨이(Galway)에서 스페셜티 커피 원두를 직접 볶아 파는 작은 가게(로스터)의 랜딩 페이지입니다. 목표는 동네 사람이 가게에 와서 원두 한 봉지를 사게 하는 것입니다.
- 눈에 띄는 지시:
  - 만들기 전에 스크린샷을 분석해 디자인 취향부터 이해하라고 요청합니다.
  - 첫 화면에 영상을 넣습니다. 영상 생성 도구에 시작 프레임과 끝 프레임을 주어 만들게 합니다.
  - 커피 봉지는 가로 스크롤로 보여 주고, 기존 커피 세 가지 외에 제품 두 개를 더 만들고 로고도 새로 만들게 합니다.
  - 실제 사진은 직접 넣을 테니 히어로와 커피 자리를 비워 두라고 합니다.
  - 시작하기 전에 필요한 질문을 먼저 하라고 합니다.
- 참고(이 문서의 해석): 이 사례의 색과 글꼴 지시(종이 같은 오프화이트 배경, 세리프 제목, 테라코타(붉은빛이 도는 갈색) 강조색)는 현재 frontend-design 스킬이 AI가 만든 디자인에서 흔히 보이는 조합으로 꼽는 첫 번째 예와 거의 같습니다. 다만 스킬은 의뢰가 직접 정한 시각 방향은 그대로 따르라고 적습니다. 그래서 이 경우에는 지시대로 만드는 쪽이 스킬 원칙에도 맞습니다.

### 5.3 Blackwater Cabins

- 참고 사이트: 세 곳을 링크로 보냈습니다.
  - [Nimmo Bay](https://www.nimmobay.com/): 화면 가장자리까지 채운 사진 히어로, 사진 구석에 낮게 놓인 제목, 가늘고 자간이 넓은 글자. 이 사이트의 색과 글꼴은 원하지 않는다고 밝혔습니다.
  - [Vipp Guesthouses](https://vipp.com/en/world-of-vipp/our-guesthouses): 어둡고 대비가 강한 느낌, 스크롤해도 화면 위에 따라붙는 얇은 메뉴 막대.
  - [Aman Amangiri](https://www.aman.com/resorts/amangiri): 큰 사진 한 장, 작은 라벨, 세리프 제목, 넉넉한 여백으로 이루어진 카드.
- 만든 것과 목표: 주말에 묵을 수 있는 호숫가 오두막 세 채를 알리는 페이지입니다. 목표는 방문자가 빈 날짜를 확인하고 예약하게 하는 것입니다.
- 눈에 띄는 지시:
  - 첨부한 자기 로고를 쓰게 합니다.
  - 오두막 카드마다 사진 자리, 이름, 묵을 수 있는 인원, 가장 낮은 가격을 넣습니다.
  - 히어로 사진에 은은한 패럴랙스를 주고, 따라붙는 메뉴 막대에는 살짝 흐림 효과를 줍니다. 움직이는 구간 하나와 조용한 구간 하나를 번갈아 둡니다.
  - 완성한 뒤 페이지 위, 가운데, 아래를 스크린샷으로 찍어 어두운 배경 위에 놓인 글자가 잘 읽히는지 확인하게 합니다.

## 6. 실행 전에 준비하기

프롬프트를 실행하기 전에 Claude Code에 세 가지를 준비합니다. frontend-design 스킬을 설치하고(6.1절), 모델을 Opus로 정하고(6.2절), 스크린샷을 찍을 브라우저 도구를 연결합니다(6.3절). 원문 프롬프트처럼 이미지와 영상까지 만들게 하려면 생성 도구도 따로 연결해야 합니다(6.4절).

### 6.1 frontend-design 스킬 설치와 사용

원문은 [skills 저장소의 frontend-design 폴더](https://github.com/anthropics/skills/tree/main/skills/frontend-design)를 연결했습니다. Claude Code에서는 같은 내용을 공식 플러그인으로 설치합니다. 터미널에서는 아래 명령을 실행합니다. 기본 설치 범위는 user이고, 이 프로젝트에만 설치하려면 `--scope project`를 붙입니다.

```bash
claude plugin install frontend-design@claude-plugins-official
```

- Claude Code 세션 안에서는 `/plugin install frontend-design@claude-plugins-official`을 입력합니다. 이 명령은 바로 설치하지 않고 플러그인 상세 화면을 엽니다. 그 화면에서 설치 범위(user, project, local)를 고릅니다.
- `claude-plugins-official` 마켓플레이스(플러그인을 모아 둔 목록)는 대화형 세션을 처음 시작할 때 자동으로 추가됩니다. 목록에 없으면 `/plugin marketplace add anthropics/claude-plugins-official`로 추가합니다. 터미널에서 설치했다면 Claude Code를 다시 실행하거나 `/reload-plugins`를 입력해야 적용됩니다.
- 위 공식 플러그인 대신 skills 저장소 README에 있는 방법을 써도 됩니다. 두 방법 가운데 하나만 씁니다. 둘 다 설치하면 같은 스킬이 두 번 등록됩니다. skills 저장소 README에 있는 방법을 쓰려면 `/plugin marketplace add anthropics/skills`와 `/plugin install example-skills@anthropic-agent-skills`를 차례로 입력합니다. 그러면 frontend-design이 들어 있는 예시 스킬 묶음 전체가 함께 설치됩니다.
- Claude는 스킬 설명을 보고 관련 있는 작업이면 스킬을 자동으로 불러옵니다. 직접 부를 때는 `/frontend-design:frontend-design`(공식 플러그인)이나 `/example-skills:frontend-design`(skills 저장소)을 씁니다. 이름이 겹치는 다른 명령이 없으면 원문처럼 `/frontend-design`만 써도 됩니다. 설치됐는지는 `/`를 입력하면 나오는 목록이나 `/plugin`의 Installed 탭, 터미널의 `claude plugin list`로 확인합니다.

현재 스킬 내용 가운데 원문 방법과 관련된 점은 다음과 같습니다.

- 판에 따른 차이: 현재 스킬(2026년 9월 3일 판)에는 Inter, Roboto, 보라색이라는 단어가 없습니다. 글꼴 이름(Inter, Roboto, Arial)과 '흰 배경 위 보라색 그라데이션'을 직접 짚어 피하라는 문장은 2025년 12월 초기판에만 있었습니다. 현재판은 글꼴 이름 없이, 다른 프로젝트에서도 습관처럼 고르는 기본 글꼴을 피하라고만 적습니다. 영상에서 어느 판을 썼는지는 확인하지 못했습니다.
- 계획 먼저: 스킬은 코드를 쓰기 전에 짧은 디자인 계획부터 세우게 합니다. 계획에는 이름을 붙인 색 4~6개, 글꼴과 역할, 레이아웃 개념(한 문장 설명과 글자로 그린 화면 뼈대)이 들어갑니다. 그다음 계획을 의뢰와 맞대어 보고, 어디서나 나올 법한 기본값을 고친 뒤 코드를 씁니다.
- 흔한 기본값 피하기: 스킬은 AI가 만든 티가 나는 조합 다섯 가지를 예로 듭니다. 첫 번째는 따뜻한 크림색 배경에 대비가 강한 세리프 글꼴과 테라코타 강조색을 쓰는 조합입니다. 구간마다 아래에서 떠오르며 나타나는 효과도 흔한 기본값으로 봅니다. 다만 의뢰가 직접 정한 부분은 그대로 따르고("the brief's own words always win"), 의뢰가 비워 둔 부분에서만 이런 기본값을 피합니다.
- 스스로 검토: 스킬은 만드는 동안 스크린샷을 찍어 자기 작업을 검토하라고 지시합니다. 이 지시를 실행하려면 6.3절의 브라우저 도구가 있어야 합니다.

### 6.2 서브에이전트를 Opus로 돌리기

서브에이전트는 메인 Claude가 일을 나눠 맡기는 별도 에이전트입니다. 각 서브에이전트는 별도의 대화 맥락에서 일하지만, 사용량은 메인 대화와 같은 사용 한도에 함께 계산됩니다. 원문의 "Use sub-agents on Opus"는 자연어 지시입니다. 그래서 Claude가 서브에이전트를 부를 때 이 말을 모델 설정에 반영해 주기를 기대할 수밖에 없습니다.

처음이라면 세션을 시작할 때 `/model` 명령으로 메인 세션의 모델을 Opus로 바꾸는 것으로 충분합니다. 기본 서브에이전트는 따로 정하지 않으면 메인 대화의 모델을 따르기 때문입니다. 아래 두 방법은 서브에이전트를 직접 정의하거나 모델을 강제해야 할 때 씁니다.

- 직접 만든 서브에이전트라면 정의 파일(`.claude/agents/이름.md`)에 `model: opus`를 적습니다.
- 모든 서브에이전트에 한 모델을 강제하려면 환경 변수 `CLAUDE_CODE_SUBAGENT_MODEL`과 `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1`을 함께 씁니다(Claude Code v2.1.257 이상).

모델 설정과 별개로, 큰 작업에는 `/effort ultracode`를 켤 수 있습니다. ultracode는 모델을 고르는 설정이 아닙니다. 이 설정을 켜면 Claude가 큰 작업마다 서브에이전트 여러 개를 나눠 돌리는 워크플로를 스스로 짭니다. 그만큼 토큰을 많이 쓰고 사용 한도에도 빨리 닿습니다.

### 6.3 스크린샷을 찍을 수 있게 준비하기

원문 프롬프트는 완성한 페이지를 스크린샷으로 찍어 스스로 확인하라고 지시합니다. 이 지시는 Claude가 페이지를 브라우저에 띄우고 찍을 수 있어야 실행됩니다. Claude Code의 기본 Read 도구는 PNG나 JPG 파일을 열어 볼 수 있습니다. 하지만 페이지를 화면에 그려서 찍으려면 다음 도구 중 하나를 연결해야 합니다.

| 도구 | 쓰는 법 | 조건과 참고 |
| --- | --- | --- |
| [Claude in Chrome](https://code.claude.com/docs/en/chrome) | `claude --chrome`으로 실행하고 `/chrome`으로 상태를 확인 | Chrome 확장 1.0.36 이상과 Pro, Max, Team, Enterprise 가운데 하나의 플랜이 필요하고, `/login`으로 로그인해야 함. API 키로 인증하면 쓸 수 없음 |
| Playwright 플러그인 | 터미널에서 `claude plugin install playwright@claude-plugins-official` 실행 | 페이지 이동, 클릭, 스크린샷을 지원함. 서브에이전트도 쓸 수 있어서 gauntlet loop에는 이 도구를 먼저 권함(표 아래 설명 참고). 설치와 관리 방법은 [플러그인 문서](https://code.claude.com/docs/en/discover-plugins) 참고 |
| [Claude Desktop 앱 Code 탭](https://code.claude.com/docs/en/desktop) | Browser 미리보기 창에서 Claude가 개발 서버를 띄우고 직접 확인 | `autoVerify` 설정을 켜면 편집할 때마다 자동으로 확인함 |
| `/run`, `/verify` | 앱을 실제로 실행해 변경 사항을 확인하는 내장 스킬 | `/verify`는 사용자가 직접 불러야 실행됨 |

서브에이전트는 메인 대화에 연결된 MCP 도구를 물려받습니다. 그래서 평가를 맡은 서브에이전트가 Playwright 같은 브라우저 MCP로 스크린샷을 찍게 할 수 있습니다. 반면 Claude in Chrome 도구가 서브에이전트에도 넘어가는지는 확인하지 못했습니다. 그래서 평가자가 직접 스크린샷을 찍어야 하는 gauntlet loop에는 Playwright 플러그인을 먼저 권합니다.

### 6.4 이미지와 영상을 만드는 도구

원문 프롬프트에 있는 이미지 생성과 영상 생성 지시에도 6.3절과 비슷한 조건이 붙습니다. Claude Code 기본 도구 목록에서는 이미지나 영상을 만드는 도구를 찾지 못했습니다. 그래서 이 지시를 실행하려면 생성 도구를 따로 연결해야 합니다. 어떤 생성 도구를 연결하면 되는지는 이번에 직접 확인하지 못했습니다. 생성 도구를 연결하지 않았다면 7절 템플릿의 '이미지와 영상' 블록에서 사진 자리를 비워 두라는 줄을 남기고, 사진과 영상은 직접 넣습니다. 이미지와 영상용 도구와 스킬은 10절에 소개한 영상의 07:31 챕터에서 다룹니다.

## 7. 바로 쓰는 프롬프트 템플릿

아래 템플릿은 원문 세 프롬프트의 블록 구성을 따라 한국어로 새로 썼습니다. 원문과 달리 gauntlet loop는 이름만 적지 않고 진행 절차까지 적었습니다. 절차는 Matt Shumer가 쓴 글과 [GAUNTLET_LOOP.md](GAUNTLET_LOOP.md)를 따랐습니다.

템플릿은 다음 규칙에 따라 채웁니다.

- `##`으로 시작하는 줄은 블록 이름입니다. 그대로 둡니다.
- 대괄호 부분은 내 내용으로 바꾸고, 대괄호 기호도 지웁니다.
- `(안내: …)`로 된 줄은 읽고 나서 지웁니다.
- 내 페이지에 필요 없는 블록은 통째로 지웁니다.

```text
## 참고 자료
만들기 전에 아래 참고 자료를 먼저 살펴보고, 제 디자인 취향을 정리해 주십시오.
- [사이트 1 URL 또는 스크린샷 경로. 예: ref/site1.png]: [좋은 점]이 마음에 듭니다. [싫은 점]은 가져오지 않습니다.
- [사이트 2 URL 또는 스크린샷 경로]: [좋은 점]이 마음에 듭니다.
- [사이트 3 URL 또는 스크린샷 경로]: [좋은 점]이 마음에 듭니다.
어느 사이트도 복사하지 않습니다. 영감만 얻습니다.

## 만들 것과 목표
[브랜드 이름]을 알리는 한 페이지짜리 랜딩 페이지를 만들어 주십시오.
[브랜드 이름]은 [사업 설명]입니다. 목표는 방문자가 [행동 하나]를 하게 하는 것입니다.
페이지에 들어갈 글은 [한국어 또는 영어]로 씁니다.
(안내: 다음 두 줄 가운데 하나만 남깁니다. 로고 파일이 없다면 두 번째 줄을 남깁니다.)
로고는 [로고 파일 경로. 예: ref/logo.svg]를 그대로 씁니다.
브랜드에 어울리는 로고를 새로 만들어 주십시오.

## 구성: 위에서 아래로
1. 히어로: [사진 또는 영상], 제목 한 줄, 버튼 하나("[버튼 문구]")
2. [구간 이름]: [들어갈 내용]
3. [구간 이름]: [들어갈 내용]
4. [행동을 요청하는 구간]: 히어로와 같은 버튼
5. 푸터: [주소, 연락처]

## 주인공 시각 요소
(안내: 히어로에 3D 물체나 대표 이미지를 둘 때만 이 블록을 남깁니다.)
히어로에는 [물체나 이미지]를 둡니다. 생김새는 [모양], 재질은 [재질], 조명은 [조명]으로 합니다.
(안내: 3D 물체가 아니면 다음 줄을 지웁니다.)
3D 물체는 외부 모델 파일 없이 기본 도형으로 코드에서 만듭니다.

## 분위기
페이지는 [형용사 두세 개. 예: 차분하고 따뜻한] 느낌을 주도록 만듭니다. [구체적인 장면 하나. 예: 비 오는 오후, 동네 서점 문을 열고 들어선 순간] 같은 분위기를 원합니다.

## 색
배경은 [배경색], 글자는 [글자색]입니다.
강조색은 [강조색] 하나만 쓰고, [버튼, 링크 등 쓸 곳]에만 씁니다.
[쓰지 않을 색과 효과. 예: 보라색, 그라데이션]은 쓰지 않습니다.

## 글꼴과 여백
제목용 [글꼴 성격. 예: 세리프] 글꼴 하나와 본문용 글꼴 하나만 씁니다. 본문 글자 크기는 16~18px로 합니다.
페이지 글이 한국어라면 제목용과 본문용 모두 한글을 지원하는 글꼴로 고릅니다.
[쓰지 않을 글꼴. 예: Inter, Roboto, Open Sans]는 쓰지 않습니다.
[여백과 정렬 규칙. 예: 간격은 8px 단위로 맞추고, 모든 요소를 가운데에 몰지 않습니다.]

## 움직임
[움직일 요소와 방식. 예: 구간이 나타날 때 천천히 떠오릅니다.]
[피할 움직임. 예: 튀어 오르는 움직임은 쓰지 않습니다.]
움직임 줄이기 설정을 켠 사용자에게는 움직임을 멈춥니다.

## 문구
[말투. 예: 차분하고 구체적인 말투]로 짧게 씁니다.
읽는 사람은 [대상]이고, [대상이 아닌 사람]을 위한 글이 아닙니다.
화면마다 방문자에게 요청하는 행동은 "[행동 하나]" 하나만 둡니다. 필요한 세부 내용은 지어내도 됩니다.

## 이미지와 영상
(안내: 다음 두 줄 가운데 하나만 남깁니다. 이미지나 영상 생성 도구를 연결하지 않았다면 두 번째 줄을 남깁니다. 6.4절을 참고합니다.)
쓸 수 있는 이미지 생성 도구와 영상 생성 도구로 필요한 자료를 만들어 주십시오.
실제 사진은 제가 넣겠습니다. 히어로와 [구간 이름]에 사진 자리를 분명히 비워 두십시오.

## 기술 조건
HTML 파일 하나로 만듭니다.
(안내: 외부 라이브러리를 쓰지 않는다면 다음 줄을 지웁니다.)
외부 라이브러리는 CDN에서 고정 버전으로 불러옵니다.
[성능 조건. 예: 페이지 전체를 1MB 미만으로 유지하고, 3D를 쓴다면 기기 픽셀 비율을 최대 2로 제한합니다.]
3D나 영상을 불러오지 못하면 빈 화면 대신 [대체 화면. 예: 정지 이미지와 제목]을 보여 줍니다.

## 확인
끝나면 페이지 맨 위, 각 구간, 맨 아래를 데스크톱 크기와 휴대폰 크기에서 각각 스크린샷으로 찍어 확인해 주십시오.
잘리거나 읽기 어렵거나 끊기는 곳을 고친 뒤에 보고해 주십시오.

## 진행 방식
/frontend-design 스킬을 사용하고, 도움이 되는 곳에는 Opus 서브에이전트를 써 주십시오.
gauntlet loop로 진행해 주십시오. 목표를 여러 조각으로 직접 나눠 주십시오. 각 조각은 따로 개선하고 평가할 수 있는 가장 작은 단위로 정합니다. 조각마다 만드는 서브에이전트와, 새 맥락에서 평가만 하는 서브에이전트를 따로 둡니다.
평가자는 제작자의 설명 대신 실제 스크린샷을 봅니다. 그리고 각 조각을 관련된 참고 사이트(예: 히어로는 사이트 1, 카드는 사이트 3)와 나란히 놓고 더 나은 쪽을 고릅니다. 가능하면 어느 쪽이 우리 것인지 모르게 비교합니다. 참고 사이트와 생김새가 다르다는 이유만으로 우리 결과물이 졌다고 판단하지 않습니다.
참고 사이트가 이기면 가장 큰 차이 하나를 제작자에게 돌려보냅니다. 우리 결과물이 이기거나, 개선 폭이 아주 작아지거나, [상한. 예: 2시간]에 닿거나, 제가 멈출 때까지 반복합니다. 멈출 때는 남은 차이를 정리해 보고해 주십시오.
진행 상황은 workbench.md에 계속 적어 주십시오.
시작하기 전에 필요한 질문을 먼저 해 주십시오.
```

## 8. 실행하고 확인하기

### 8.1 실행 순서

6절 준비를 마쳤다면 아래 순서로 실행합니다.

1. 새 작업 폴더를 만들고, 터미널에서 그 폴더로 이동해 `claude`를 실행합니다.
2. 참고 스크린샷과 로고 파일은 폴더 안 `ref/`에 저장합니다. 프롬프트에는 이 경로(예: `ref/site1.png`)를 적습니다. 터미널 창에 파일을 끌어다 놓아도 경로가 들어갑니다.
3. 7절 템플릿을 채워 붙여 넣습니다.
4. Claude가 먼저 묻는 질문에 답한 뒤 진행을 지켜봅니다. 진행 상황은 workbench.md에서 확인합니다.
5. 작업이 끝나면 만들어진 HTML 파일(예: `index.html`)을 브라우저로 열어 직접 확인합니다. Mac에서는 터미널에서 `open index.html`을 실행해도 됩니다.

### 8.2 gauntlet loop로 실행하기

원문이 연결한 원래 출처는 Matt Shumer가 2026년 7월 27일에 쓴 [How to Run a Gauntlet Loop](https://somethingbig.ai/gauntlet-loop)입니다. [GAUNTLET_LOOP.md](GAUNTLET_LOOP.md)는 이 방법을 쉽게 요약하고, 루프용 프롬프트를 만들어 주는 RoboNuggets의 `/gauntlet-loop` 스킬과 설치 방법을 소개합니다. Matt Shumer의 글에서 원문 사례와 직접 관련된 내용만 추리면 다음과 같습니다.

- 일반 Claude 채팅이 아니라 Claude Code 같은 에이전트 환경에서 실행합니다. 저자는 서브에이전트마다 이전 대화가 섞이지 않은 새 맥락을 쓸 수 있다는 이유로 Claude Code와 Opus 5 조합을 기본으로 씁니다. 큰 작업에는 ultracode를 권하면서, 비용이 훨씬 많이 든다고도 적습니다.
- 저자는 기준(bar)을 가장 중요한 요소로 꼽습니다. "Make it amazing" 같은 말은 기준이 되지 못하고, 웹사이트라면 그 분야에서 가장 잘 만든 실제 사이트가 기준이 됩니다. 기준에 실제로 닿지 못해도 괜찮다고 덧붙입니다.
- 정해진 횟수만 돌고 멈추게 하지 않습니다. 반복 실행에는 Claude Code의 `/loop` 스킬을 쓸 수 있다고 안내합니다.

평가자에게 무엇을 주고 언제 멈출지는 [HOW_DESIGN.md](HOW_DESIGN.md) 10~11절과 [GAUNTLET_LOOP.md](GAUNTLET_LOOP.md)를 따릅니다.

목표(만들 것)를 넣으면 루프용 프롬프트를 써 주는 [생성기 페이지](https://somethingbig.ai/gauntlet-loop/generator)도 있습니다. 기준도 함께 넣을 수 있지만, 비워 두어도 됩니다. 생성기는 이메일을 등록해야 열리고, 프롬프트는 하루 5개까지 만듭니다. 생성기 페이지의 실행 안내는 스킬과 MCP 서버를 하나도 설치하거나 켜지 않은 세션에서 돌리라고 권합니다. 원문 사례처럼 frontend-design 스킬이나 브라우저 MCP와 함께 쓰면 이 권고와 어긋난다는 점을 알고 시작합니다.

### 8.3 확인 지점과 확인 목록

스크린샷은 페이지 맨 위, 각 장면이나 구간, 맨 아래에서 찍습니다. 같은 위치를 데스크톱 크기(예: 너비 1440px)와 휴대폰 크기(예: 너비 390px)로 한 번씩 찍습니다. 원문 세 프롬프트의 확인 지시와 frontend-design 스킬의 기본 품질 항목을 모으면 다음 목록이 됩니다.

- [ ] 잘린 글자나 요소가 없습니다.
- [ ] 모든 글자가 배경 위에서 잘 읽힙니다. 어두운 배경은 따로 한 번 더 봅니다.
- [ ] 스크롤과 움직임이 끊기지 않습니다.
- [ ] 휴대폰 크기에서도 레이아웃이 무너지지 않고 버튼이 작동합니다.
- [ ] 강조색은 정한 곳에만 쓰였고, 금지한 글꼴과 색, 효과는 들어가지 않았습니다.
- [ ] 화면마다 방문자에게 요청하는 행동이 하나뿐입니다.
- [ ] 움직임 줄이기 설정을 켜면 움직임이 멈춥니다.
- [ ] 3D나 영상이 안 될 때 빈 화면 대신 대체 화면이 나옵니다.
- [ ] 키보드로 이동하면 현재 위치가 눈에 보이게 표시됩니다.
- [ ] 페이지 크기가 정한 한도 안에 있습니다.

이 가운데 키보드 항목은 frontend-design 스킬에서 왔고, 나머지는 원문 프롬프트에서 왔습니다. 접근성과 성능의 일반 점검 항목은 [HOW_DESIGN.md](HOW_DESIGN.md) 9절을 따릅니다.

원문은 이렇게 만든 페이지를 한두 번 더 고쳤습니다. 수정 요청에는 위치, 화면 크기, 실제로 나타난 문제, 원하는 결과를 적고, 한 번에 문제 하나만 고쳐 달라고 요청합니다. 예를 들어 "휴대폰 크기(390px)에서 히어로 제목이 세 줄로 넘쳐 버튼을 가립니다. 버튼이 첫 화면 안에 보이도록 제목 크기를 줄여 주십시오."처럼 씁니다. 고칠 문제를 기록하고 순서를 정하는 방법은 [HOW_DESIGN.md](HOW_DESIGN.md) 9절과 11절에 있습니다.

## 9. 디자인 시스템으로 남기기

원문은 마지막 분류에서, 페이지 디자인이 정해지면 Claude에게 디자인 시스템으로 정리하게 하고 이후 모든 결과물에 다시 쓰라고 권합니다. 문서에 남길 항목은 [HOW_DESIGN.md](HOW_DESIGN.md) 12절 표에 정리되어 있습니다.

### 9.1 Claude Design이나 Claude Code에 정리 요청하기

- Claude Code에서는 완성한 페이지를 보여 주고 색, 글꼴, 간격, 부품, 움직임 규칙을 디자인 시스템 문서로 정리하게 합니다. 다음 페이지를 만들 때는 이 문서부터 읽게 합니다.
- [Claude Design](https://claude.com/product/design)은 Anthropic이 2026년 4월 17일에 Anthropic Labs 제품으로 내놓은 디자인 도구입니다. 대화창 옆 캔버스(결과물을 띄워 놓고 바로 고치는 작업 화면)에서 디자인, 프로토타입(실제처럼 눌러 볼 수 있는 시험용 화면), 슬라이드를 만듭니다. GitHub나 디자인 파일, 로컬 코드에서 디자인 시스템을 가져오면 그 부품으로 결과물을 만듭니다. 결과는 PPTX, PDF, HTML로 내보내거나 Claude Code로 넘깁니다. Claude Code 데스크톱과 터미널에서는 `/design`으로 디자인을 만들고 고치며, `/design-sync`로 디자인 시스템을 가져옵니다.
- 이용 조건은 공식 페이지마다 다르게 적혀 있습니다. 제품 페이지는 모든 유료 플랜에 포함된다고 쓰고, [도움말 문서](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)는 Pro, Max, Team, Enterprise에서 베타로 제공한다고 씁니다. Enterprise 플랜에서는 Claude Design이 기본으로 꺼져 있어서 조직 소유자가 직접 켜야 합니다.

### 9.2 Refero Styles의 design.md 쓰기

[Refero Styles](https://styles.refero.design/)는 실제 제품 웹사이트에서 뽑은 디자인 시스템 2,000개 이상을 AI가 읽기 좋은 형태로 모아 둡니다. 스타일마다 DESIGN.md 탭과 다운로드 버튼이 있고, 로그인 없이 볼 수 있습니다. DESIGN.md는 색, 글자, 간격, 컴포넌트, 레이아웃, 아이콘, 사용 규칙을 적은 마크다운 파일이며, Refero는 이 파일을 "a design-system README for agents"라고 설명합니다. 파일 이름은 원문이 소문자 design.md로, 사이트가 대문자 DESIGN.md로 적습니다.

원문은 design.md를 전체 페이지 캡처와 함께 주라고 권하며, 영상에서는 Stripe를 예로 썼습니다. 같은 사이트의 design.md와 캡처를 함께 주면, 규칙은 파일로 전달하고 실제 모습은 캡처로 보여 줄 수 있습니다. 파일은 프로젝트 최상위 폴더(루트)에 두거나, 에이전트가 늘 읽는 지침 파일에 내용을 넣습니다. 그리고 프롬프트에 DESIGN.md를 따르라고 적습니다. 다만 이 파일은 Refero가 만든 문서이며, Refero도 공식 브랜드 가이드가 아니라고 밝힙니다.

### 9.3 Branding Style Guides로 구성 참고하기

[Branding Style Guides](https://brandingstyleguides.com/)는 실제 브랜드 가이드 PDF를 모은 곳입니다. 이름, 언어, 발행 연도, 쪽수, 지역, 태그로 거를 수 있습니다. 내 디자인 시스템 문서를 쓸 때 실제 브랜드가 어떤 항목을 어떤 순서로 정리했는지 보고, 내 문서와 비교해 봅니다. 원문은 most popular 목록부터 보라고 권합니다. PDF는 무료로 가입해 로그인해야 받을 수 있습니다.

## 10. 더 보기

원문은 이어서 볼 영상으로 [Fable 5.1 + Claude Code /design (Beginner's Guide)](https://www.youtube.com/watch?v=MagStZ3yA3A)를 추천합니다. The AI Automators 채널에 2026년 9월 2일에 올라온 16분 11초짜리 영상이며, 데스크톱 앱의 Claude Design 캔버스와 Claude Code 터미널에서 `/design`을 쓰는 방법을 다룹니다.

영상 설명에 따르면, 이 영상은 그냥 요청했을 때 나오는 평균적인 결과에서 보이는 특징 다섯 가지와 이를 고치는 기법 여섯 가지를 소개합니다. 출장 세차 업체 'Autoblitz'를 예로 들어 가격표, 리뷰 카드, 인스타그램 게시물, 360도 AI 영상이 들어간 랜딩 페이지를 만든 뒤 디자인 시스템으로 정리합니다. 챕터는 참고할 화면 보여 주기(05:08), 이미지와 영상용 도구와 스킬(07:31), 아이콘(10:46), 냉정한 크리에이티브 디렉터(11:45), 디자인 시스템으로 정리하기(13:34), 토큰 관리(15:05) 순서로 이어집니다.

## 출처

- 원문: [Claude + Design Inspiration: All the Links From the Video](https://www.theaiautomators.com/claude-design-inspiration-all-the-links-from-the-video/), [The AI Automators](https://www.theaiautomators.com/), 2026년 9월 7일 게시
- Matt Shumer, [How to Run a Gauntlet Loop](https://somethingbig.ai/gauntlet-loop), 2026년 7월 27일. 원본 프롬프트는 [Claude-of-Duty 저장소](https://github.com/mshumer/Claude-of-Duty/blob/main/prompt.md)에 있습니다.
- frontend-design 스킬: [SKILL.md 원문](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), [공식 플러그인 판](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design)
- Claude Code 문서: [플러그인 찾기와 설치](https://code.claude.com/docs/en/discover-plugins), [스킬](https://code.claude.com/docs/en/skills), [서브에이전트](https://code.claude.com/docs/en/sub-agents), [Chrome 연동](https://code.claude.com/docs/en/chrome), [데스크톱 앱](https://code.claude.com/docs/en/desktop), [모델 설정](https://code.claude.com/docs/en/model-config), [명령어](https://code.claude.com/docs/en/commands)
- 사이트 정보: 2절 표의 각 사이트, [Mobbin 가격](https://mobbin.com/pricing), [Mobbin MCP 연결 안내](https://docs.mobbin.com/mcp/clients/claude-code-cli), [Refero 플랜](https://doc.refero.design/help/plans), [21st.dev 가격](https://21st.dev/pricing), [React Bits 저장소](https://github.com/DavidHDev/react-bits), [Coolors 가격](https://coolors.co/pricing), [Book of Shapes 라이선스](https://www.bookofshapes.com/license), [What is DESIGN.md](https://styles.refero.design/design-md/what-is-design-md), [Claude Design 발표](https://www.anthropic.com/news/claude-design-anthropic-labs)
- 확인한 날짜: 2026년 10월 6일. 원문의 가격은 영상 녹화 시점 기준이고, 이 문서의 가격은 확인한 날짜 기준이라 이후 바뀔 수 있습니다.

한국어 문장은 [fluent-korean 작성 지침](https://github.com/snflkd/fluent-korean)에 따라 검토했습니다.
