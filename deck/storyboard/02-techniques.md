# Part 02 storyboard: 8 Techniques (NOTE2.md)

Notes for the builder (short):
- `A/` = `assets/how-to-turn-your-ai-into-a-world/` (in HTML: `../assets/how-to-turn-your-ai-into-a-world/...`). Derived crops go to `deck/img/02/` (PIL crop only; boxes are in original pixels, left/top/right/bottom). Each box is inset past the source's rounded corners, so every frame stays a sharp rectangle. All boxes were test-cropped during review and land on clean tile edges.
- Phase marker system: the first slide of each technique carries one filled chip (`.tag.fill`) reading `DISCOVER 01` … `DELIVER 08`. Define and Deliver also get their own divider slides (S6, S13).
- figure-14 is byte-identical to figure-07 (same md5). S3 shows the full image, and S6 shows only a zoomed crop of one tile (zylo), so the same frame is not repeated. The BEFORE column of figure-15 (S7) and the strips in figures 16-20 (S9, S11) show the same four designs (Meridian, zylo, Quartz, Quanta) on purpose: the article follows them through the whole pipeline, so the audience sees one set of designs improve.
- GIFs animate in the deck. figure-10 opens on a nearly empty cream frame, so keep it in the third slot (S4). In figure-19's first frame the right half is still drawing. Figures 16-20 are before/after pairs: in every strip the left tile is before, the right tile is after.
- Headline widths below were measured with Anton (slides/fonts/Anton-Regular.ttf).
- Cross-part note: Part 01 S1 also uses figure-21 (Waymark suitcase) in a small grid cell. figure-21 belongs to NOTE2 (S12 here), so Part 01 should swap that cell for another image.

## S1. PART DIVIDER: image top-right + phase numerals left + huge title bottom  (dark)
- headline: 8 TECHNIQUES
- text: 없음
- labels: DISCOVER 발견, DEFINE 정의, DELIVER 전달, How to turn your AI into a world-class designer, Anshu Chimala, Lenny's Newsletter, 2026.09.01
- images: A/figure-04-bc7e732b-64b8-4538-8b17-82290d34d032_1774x887.jpg contain — the article's bell curve: blurry purple stock UI cards in the middle marked "AI slop", bold original designs on both tails. It shows what the eight techniques push away from, and it is used nowhere else in the deck.
- placement: Left column x 56-680 holds three phase blocks at y 130 / 330 / 530. Each block has the phase name in .lbl (cream), a 2px cream .rule under it (624 wide), and the technique numbers in Anton at 100px below ("01 02", "03 04 05", "06 07 08"). These numbers are the visual device, so no technique names are needed here. figure-04 sits at x 760, y 130, 1104x552 (exact ratio, a white card on black). The source line is one .cap line at x 760, y 700. "8 TECHNIQUES" is set at 330px (about 1674 wide) at x 40, bottom -30, bleeding slightly off the bottom edge.
- source: 기법 1 ~ 기법 8 headings, 정의, 전달 (overview); phase names from NOTE.md §4; author/date from NOTE.md §1; English title from README.md; figure 4 from NOTE.md §3

## S2. DESIGN IDEA: title + 2 images with labels  (light)
- headline: SAME AGAIN
- text: 모델은 무작위처럼 들리는 토큰을 예측할 뿐
- labels: DISCOVER 01, Claude Opus 5 기본 결과: 거의 매번 보랏빛, "모든 결정을 무작위로" 추가: 그래도 닮은꼴
- images: A/figure-05-7b59bdf3-8a82-46d1-94c2-4a1e60ea7cbf_1456x894.jpg cover — the four near-identical landing pages (left text, right UI card, mostly purple); A/figure-06-f37064a7-2853-4314-b175-aa65b8a13f43_1456x876.jpg cover — the four terracotta "Kiln" pages that still share palette, structure and the pottery metaphor
- placement: "SAME AGAIN" (d-l 220, about 1000 wide) sits top-left at x 48, y 120. The marker chip is at x 1110, y 140, and the Korean line (.lead) is at x 1110, y 200, 750 wide. Two frames of 860x528 sit at y 420: figure-05 at x 56 and figure-06 at x 1004. Each image label (.lbl) goes under its image at y 970.
- source: 기법 1: 시드 문자열로 다양성 불어넣기 (problem: figures 5, 6)

## S3. PHOTOGRAPHY: big image top-left + huge word along bottom  (light, data-hdr="none")
- headline: SEED STRINGS
- text: 없음
- labels: 1 셸 스크립트로 무작위 문자열, 2 패턴에서 색, 레이아웃, 서체, 3 문자열은 숨기고 구현, Sakana AI의 String Seed of Thought
- images: A/figure-07-bcda7156-dbbd-4d18-a7fb-4cfc124563bf_1456x876.jpg cover — the varied seed-string results (Meridian serif, zylo dark mono, Quartz lime, Quanta bold), proof that each run differs
- placement: figure-07 bleeds from the top-left corner (x 0, y 0, 1100x662, exact ratio). A right column at x 1160-1864 holds the three steps at y 90 / 210 / 330. Each step pairs an Anton numeral (100px) with an .lbl text. The Sakana credit is a .cap at y 540. "SEED STRINGS" is set at 330px (about 1655 wide) at x 24, bottom -28, bleeding off the bottom.
- source: 기법 1: 시드 문자열로 다양성 불어넣기 (String Seed of Thought, prompt steps, figure 7)

## S4. OUR TRAM: dark, 3 images top + huge title bottom-right  (dark)
- headline: BE AMBITIOUS
- text: "이게 될 리 없어" 싶다면 제대로 가는 중
- labels: DISCOVER 02, 픽셀 아트 게임 장면, 아이소메트릭 3D 도시, 규칙을 다 깬 레이아웃
- images: A/figure-08-3d880aa5-5e31-45f5-99c4-8055dcb87f4a_640x360.gif cover — QUESTLOG pixel-art landscape (animated); A/figure-09-a7245156-8c71-4ecc-9897-5ce76e561faf_640x360.gif cover — SKYLINE isometric city with "A task is a floor" (animated); A/figure-10-220747d1-f561-405f-a95c-7b05fd64731b_640x360.gif cover — OFFCUT rule-breaking editorial layout (first frame is nearly empty; it fills in as it animates)
- placement: The marker chip sits at x 56, y 116. Three 584x328 frames run at y 170, at x 56 / 668 / 1280 (exact 16:9). Each caption (.txt) sits under its frame at y 520. The Korean line (.lead, cream) is at x 56, y 610, 1000 wide. "BE AMBITIOUS" is set at 320px (about 1636 wide) with right 56, bottom 24, so its top edge sits near y 790, clear of the line.
- source: 기법 2: 프롬프트를 훨씬 더 야심 차게 쓰기 (examples 1-3, figures 8-10; closing tip "이게 될 리 없어")

## S5. STEP ROWS: BEST CONCEPT turned vertical, big numerals 1 2 3 + figure strips  (light)
- headline: STEER IT
- text: 되먹이지 말고 직접 조종한다
- labels: 1 세부 없이 아이디어 잔뜩, 2 반응 적고 다듬기, 3 제작 프롬프트 받기
- images: deck/img/02/t2-step1-ideas.png contain — derived crop of A/figure-11-0e1d6d22-1828-47d5-b2f6-0d88fef90ae2_1456x571.png box (28,40,1428,475): "AI:" plus the five idea names (Brutalist Utility … Comic Book UI); deck/img/02/t2-step2-refine.png contain — derived crop of A/figure-12-0e7340b1-9a93-4d94-abc6-c6b386f3a36c_1456x449.png box (28,40,1428,172): the refined "tactile, engineered interface" answer; deck/img/02/t2-step3-prompt.png contain — derived crop of A/figure-13-4ca0ce7c-c730-443a-bde3-f62996b43c7d_1456x692.png box (28,40,1428,292): the "Precision Industrial" POC build prompt
- placement: "STEER IT" (d-l 220) sits top-left at x 48, y 120, and the Korean line (.lead) is at x 900, y 210. Three rows run under it, each with a .num numeral at 150px at x 56, an .lbl step label at x 230 (420 wide), and the peach crop at x 764, 1100 wide. Row 1 is y 345-687, row 2 is y 717-821, and row 3 is y 851-1049.
- source: 기법 2: 프롬프트를 훨씬 더 야심 차게 쓰기 (#### 1, 2, 3 idea process, figures 11-13, steering tip)

## S6. VISUAL DISPLAY, annotated: image top-left + callouts + huge title bottom-right  (light)
- headline: DEFINE
- text: 시드 문자열 시안도 같은 낡은 패턴
- labels: 1 상단 내비게이션, 2 왼쪽 텍스트와 CTA 버튼, 3 오른쪽 그래픽
- images: deck/img/02/define-zylo.png cover — derived crop of A/figure-14-25c296a8-ce8c-4633-ac96-2dcbad6d9430_1456x876.jpg box (770,26,1414,402) (the zylo tile alone, 644x376): top nav, left headline + START FREE CTA, right task panel, the old pattern in one frame
- placement: The zylo crop is 980x572 at x 56, y 130 (exact ratio). Keep this slide cream: the zylo tile is near-black, so on a dark slide its edge would vanish. Small filled number chips sit over it: "1" at about (640,140) on the nav, "2" at about (480,290) just right of "ship the day.", "3" at about (990,300) on the right panel. A right column at x 1100-1864 holds the Korean line (.lead) at y 160 and the three callout .lbl at y 300 / 380 / 460. "DEFINE" is set at 440px (about 1075 wide) with right 56, bottom -40.
- source: 정의: 디자인 방향 심화하기 (figure 14 framing)

## S7. OUR SERVICES: title left + black panel with tall image right  (light)
- headline: CRITIC LOOP
- text: 스크린샷만 보는 별도 비평가가 10점 만점으로 채점
- labels: DEFINE 03, BUILD  Claude Opus 5, CRITIC  Claude Fable 5
- images: A/figure-15-5e045d71-d5f7-436a-be1f-eb870df24062_1456x1861.jpg contain — the full BEFORE/AFTER column pair: four stock layouts become four distinct identities (Meridian masthead, zylo strike-through, Quartz lime block, Quanta "Spend it well.")
- placement: The marker chip sits at x 56, y 120. "CRITIC" / "LOOP" (d-l 220, two lines) runs from x 48, y 170 to y 540, and the Korean line (.txt) is at x 56, y 880, 640 wide. A .block-dark panel spans x 740-1920, y 400-1080. figure-15 fills a contain frame at x 1160-1920, y 120-1080 (about 751x960), and its top sits on cream above the panel. In the black strip at x 770-1130, BUILD (y 470) and CRITIC (y 720) stack as cream .lbl, each with its model name in .txt below and a thin vrule between them as the loop.
- source: 기법 3: 서브에이전트로 긍정적 피드백 루프 만들기 (critic role, model split, prompt gist, figure 15)

## S8. PRICING PLAN: dark, huge numeral + 3 numeral columns  (dark)
- headline: 9/10
- text: 9점 이상이면 끝, 기준은 비평가에게 비공개
- labels: <10%: Fable 출력 토큰 비중, 직접 맡기면 비용 두 배, 4 + 1: 전문가 디자인 4개와 섞어 순위 매기기, 1~2: 먼저 돌려 보고 수렴하는지 확인
- images: 없음 — visual device: gigantic "9/10" plus three big numerals (<10%, 4 + 1, 1~2) in ruled columns, like the ref price row
- placement: "9/10" is set at 400px (about 690 wide) at x 48, y 130, and the Korean line (.lead) is at x 800, y 360, 1000 wide. Three columns sit at y 640: x 56 / 660 / 1264, 560 wide, split by cream vrules at x 630 and 1234. Each holds an Anton numeral at 150px with its .txt caption under it at y 820 (each caption one or two short lines).
- source: 기법 3: 서브에이전트로 긍정적 피드백 루프 만들기 (9/10 exit rule hidden from the critic, Fable under 10% of output tokens and double cost if Fable redesigned directly, loop tips: 4 expert designs + 1 screenshot ranking, exit criteria with 1-2 trial runs)

## S9. VISUAL DISPLAY, strip grid: 2x2 before/after strips top + huge title bottom  (light)
- headline: IMAGE GEN
- text: 그라데이션 대신 생성 이미지로 개성을
- labels: DEFINE 04, Claude Opus 5 적용 전후 (각 띠의 왼쪽이 전, 오른쪽이 후)
- images: A/figure-16-7e2a6925-7451-4abe-aaa8-bc92823dd69a_1456x399.gif contain — Meridian: flat cream page, then a generated engraved-mountain backdrop; A/figure-17-f4ae7b09-1555-4ade-850c-212cb0d089b2_1456x399.gif contain — zylo: plain dark page, then a generated cable/light-streak image; A/figure-18-7cd81d80-09c1-4244-9651-43bba85771a4_1456x399.gif contain — Quartz: empty lime block, then a generated dark crystal (the crystal S11 turns into video); A/figure-19-c02123f6-00f8-4063-8463-5050d2649647_1456x399.gif contain — Quanta: thin purple strike line, then a painted brush stroke
- placement: Four strips of 880x241 (exact ratio) form a 2x2 grid in the same order as figure-15: figure-16 at (56,130), figure-17 at (984,130), figure-18 at (56,401), figure-19 at (984,401). A right column at x 1300-1864 holds the marker chip (y 700), the Korean line (.lead, 564 wide, may wrap to two lines) at y 756 and the caption (.cap) at y 950. "IMAGE GEN" is set at 300px (about 1193 wide) at x 40, bottom -30, ending left of the text column.
- source: 기법 4: 이미지 생성으로 디자인 풍부하게 만들기 (problem, prompt gist, figures 16-19 shown together as in the source)

## S10. ROUTE MAP: stacked title left + three tag rows right + code card  (light)
- headline: WIRE IT UP
- text: 없음
- labels: → 내장 이미지 생성을 쓰라고 지시, → Codex CLI로, 구독으로 과금, → OpenAI, Gemini 전용 키, 한도 낮게 (tags: Codex, Antigravity, Grok Build / ChatGPT 구독 / Claude만, 기타 도구)
- images: 없음 — visual device: a route map of tool chips with arrows to the matching setup, plus a dark .code card. The before/after strips that were here moved to S9, so S9, S10 and S11 are no longer three strip slides in a row.
- placement: "WIRE" / "IT UP" is set at 300px in two lines (about 550 wide) at x 48, y 140 to about y 650. On the right, 2px rules at y 150 / 390 / 630 / 870 (x 760-1864) split three rows. In each row the .tag chips sit at y +40 and the outcome .lbl with its "→" sits at y +120. Row 1: Codex, Antigravity, Grok Build. Row 2: ChatGPT 구독. Row 3: Claude만, 기타 도구. Bottom-left, a .code card at x 56, y 760, 640 wide, holds two lines: `.env.agents   # gitignore` and `CLAUDE.md     # 개발용, 제품 포함 금지`.
- source: 기법 4: 이미지 생성으로 디자인 풍부하게 만들기 (환경별 연결 방법: built-in tools, Codex CLI on a ChatGPT subscription, low-limit agent key, .env.agents and AGENTS.md/CLAUDE.md note)

## S11. WIDE BAND: dark, title top + full-bleed strip bottom  (dark)
- headline: VIDEO GEN
- text: 단색 배경 루프 영상에서 배경만 지운다
- labels: DEFINE 05, fal.ai 키 하나로 여러 모델 비교, GPT-5.6 Sol 적용 전후
- images: A/figure-20-aa994e2f-caec-40bf-8cc5-8a1ef101dd21_1456x399.gif cover — the Quartz crystal: static image, then a shattering, refracting video loop (caustics, glass refraction, physics). It picks up the crystal that figure-18 (S9) added with image generation.
- placement: "VIDEO GEN" is set at 300px (about 1110 wide) at x 40, y 120. A right column at x 1240-1864 holds the marker chip (y 130), the Korean line (.lead) at y 210 and the fal.ai label (.lbl) at y 330. The strip bleeds across the bottom at x 0, y 554, 1920x526 (exact ratio, a white band on black). The GPT-5.6 Sol caption (.cap, cream) sits at x 56, y 510, just above the band.
- source: 기법 5: 더 정교한 모션에는 영상 생성 활용하기 (fal.ai; #### 눈길을 사로잡는 애니메이션 그래픽 만들기, figure 20)

## S12. HERO SHOT: big image bleeding top-right + text left + huge title bottom  (light, data-hdr="none")
- headline: TRANSITIONS
- text: 두 정지 이미지 사이를 영상으로 잇는다 / 스크롤 따라 프레임 단위로 스크럽
- labels: Codex의 GPT-5.6 Sol, 프롬프트 하나
- images: A/figure-21-2f3bb583-375b-4a12-aa57-64a10bf2d9e7_960x540.gif cover — WAYMARK suitcase demo: the bag floats, lands and opens, then is packed (animated; the strongest photo-like image in the part)
- placement: The GIF is 1240x698 (16:9) at x 680, y 0, bleeding off the top and right edges, so the header is off for this slide. A left column at x 56-640 holds the two Korean lines (.lead, 584 wide) at y 150 and 250 and the caption (.cap) at y 620. "TRANSITIONS" is set at 300px (about 1383 wide) at x 40, bottom -30; its top edge sits near y 858, below the GIF. The title sits at the bottom here because S11 already has its title on top with the image below.
- source: 기법 5: 더 정교한 모션에는 영상 생성 활용하기 (#### 상태 사이의 매끄러운 전환 만들기, figure 21)

## S13. CHECK DIVIDER: dark, 3 check columns top + huge title bottom-right  (dark)
- headline: DELIVER
- text: 디테일을 다듬는 마지막 판단은 사람의 몫
- labels: 말이 되는가, 흐름이 자연스러운가, 실제로 쓸모 있는가
- images: 없음 — visual device: three giant Anton check marks (✓, 150px) as the human-judgment checklist
- placement: Three columns at y 170: x 56 / 660 / 1264, 560 wide. Each has a ✓ glyph with its .lbl below at y 360. The Korean line (.txt, cream) is at x 56, y 500. "DELIVER" is set at 440px (about 1270 wide) with right 56, bottom -30.
- source: 전달: 사용자가 좋아할 디자인으로 다듬기 (framing)

## S14. MEET OUR LEADER: huge title + two image cards with side text  (light)
- headline: SUBTRACT
- text: AI는 더하기만 한다. 빼기는 사람이 시켜야
- labels: DELIVER 06, 글로우, 강조색, 라벨, 커스텀 버튼, 이미지 그리드, 네이티브 iOS (plus the underlined words BEFORE / AFTER)
- images: A/figure-22-dc9186ef-2b04-42a0-a460-8898b0590797_1456x964.jpg cover — Morsel before: pink glow, red progress bar, labels next to food, custom input (both phones must stay fully visible); A/figure-23-fdf80ee5-9f43-44e9-93cf-c477a9e49128_1456x964.jpg cover — after: clean native layout, image-first food grid
- placement: "SUBTRACT" (d-l 220, about 800 wide) sits top-left at x 48, y 120. The marker chip is at x 1000, y 130, and the Korean line (.lead) is at x 1000, y 200. Two 640x580 cover frames sit at y 420: figure-22 at x 56 and figure-23 at x 1000. At that size the image renders 876 wide, so about 118px of white is trimmed from each side and both phones (including side buttons) stay inside the frame. Side text sits at x 720-960 and x 1664-1864: the .cap description at y 430, and an underlined d-xs "BEFORE" / "AFTER" at y 930, like the ref's "Creator / Director".
- source: 기법 6: 가치를 더하지 않는 요소 덜어내기 (figures 22, 23)

## S15. BEFORE/AFTER GRID: stacked title left + 2x2 card pairs right  (light)
- headline: AI TELLS
- text: 모든 디자인에 보이면 AI 슬롭의 신호
- labels: DELIVER 07, 아이브로우 텍스트 → 대부분 삭제, 배경 그라데이션 → 이미지, 패턴, 단색
- images: deck/img/02/t7-eyebrow-before.png cover — derived crop of A/figure-24-65ceb75e-aeb7-411d-99fa-eacaad0dbdae_1456x2424.jpg box (40,216,690,614): card with the red "EXPENSE MANAGEMENT" eyebrow; deck/img/02/t7-eyebrow-after.png cover — derived crop of figure-24 box (768,216,1418,614): same card without the eyebrow; deck/img/02/t7-gradient-before.png cover — derived crop of figure-24 box (40,816,690,1208): Hearthside on a generic blue gradient; deck/img/02/t7-gradient-after.png cover — derived crop of figure-24 box (768,816,1418,1208): Hearthside on a dark forest-cabin photo
- placement: The marker chip sits at x 56, y 120. "AI" / "TELLS" (260px, two lines, about 540 wide) runs from x 48, y 170 to y 610, and the Korean line (.txt) is at x 56, y 650, 560 wide. On the right, 540x331 cards form a grid: before at x 690, after at x 1324, with an Anton "→" (100px) centered between them. Row A is at y 150, with its .lbl-s tag at y 500. Row B is at y 580, with its tag at y 930.
- source: 기법 7: AI 티 없애기 (overused-pattern table rows 1-2, figure 24 top half)

## S16. VISUAL DISPLAY: four cards in a row top + huge title bottom  (light)
- headline: ON PURPOSE
- text: 처음부터 금지하지 말고 다듬을 때 점검
- labels: 카드와 컨테이너 과다 → 그리드, 타일, 폰트와 스타일 과다 → 폰트 1~2개, 스타일 2~4개
- images: deck/img/02/t7-cards-before.png cover — derived crop of figure-24 box (40,1365,690,1763): three boxed feature cards; deck/img/02/t7-cards-after.png cover — derived crop of figure-24 box (768,1365,1418,1763): the same content as flat tiles; deck/img/02/t7-fonts-before.png cover — derived crop of figure-24 box (40,1965,690,2358): "Make space for better ideas." with orange italic accent and mixed styles; deck/img/02/t7-fonts-after.png cover — derived crop of figure-24 box (768,1965,1418,2358): the same page with one quiet type system
- placement: Four 410x251 cards run at y 140, at x 56 / 510 / 1000 / 1454. A small Anton "→" (64px) sits in each 44px gap inside a pair, and a wider gap separates the two pairs. The two tags (.lbl-s) sit under their pairs at y 410 (x 56 and x 1000), and the Korean line (.lead) is at x 56, y 500. "ON PURPOSE" is set at 330px (about 1475 wide) at x 40, bottom -30.
- source: 기법 7: AI 티 없애기 (table rows 3-4, figure 24 bottom half, "don't ban up front" guidance)

## S17. TALL STRIP: stacked title bottom-left + tall image right  (light)
- headline: BY HAND
- text: AI 카피는 Lorem ipsum 같은 자리표시자 / 사람이 쓴 버전이 거의 언제나 더 짧다
- labels: DELIVER 08, Lantern 홍보 문구: Claude 버전과 저자 버전
- images: A/figure-25-3174cc8a-c197-4be5-991d-0834d05cfc42_1456x1949.png contain — the whole comparison, where the long "CLAUDE'S MARKETING COPY" column next to the short "MY REWRITE" column is the visual point
- placement: The marker chip sits at x 56, y 130. The two Korean lines (.lead) are at x 56, y 200 and 260, 960 wide, and the caption (.cap) is at y 350. "BY" / "HAND" is set at 330px, two lines (HAND about 650 wide), from x 40, bottom -30, about y 556 down to the bleed. figure-25 fills a contain frame at x 1100-1864, y 110-1070 (about 717x960).
- source: 기법 8: 카피는 직접 다시 쓰기 (figure 25)

## Coverage
- (Discover phase: NOTE2 has no heading. NOTE.md §4-5 confirms the framing.) Marked on S1 (DISCOVER block) and by the chips `DISCOVER 01` (S2) and `DISCOVER 02` (S4).
- 기법 1: 시드 문자열로 다양성 불어넣기: S2 (figures 5, 6, why asking for randomness fails) and S3 (String Seed of Thought by Sakana AI, the three prompt steps, figure 7 result).
- 기법 2: 프롬프트를 훨씬 더 야심 차게 쓰기: S4 (examples 1-3, figures 8-10, and the closing tip "이게 될 리 없어 싶다면 제대로 가고 있는 것"). The three sub-sections 1. 세부 없이 아이디어를 잔뜩 나열하게 하기 / 2. 마음에 드는 방향을 시각화하고 반응을 적은 뒤 다듬게 하기 / 3. 만족할 때까지 반복한 뒤 제작용 프롬프트를 쓰게 하기 are on S5 (figures 11-13 plus the "steer it yourself" point). Condensed out: the taste sources (games, interior trends, installation art) and saving failed prompts to re-run on new models.
- 정의: 디자인 방향 심화하기: S6 (figure 14, the old pattern of nav, left text + CTA, right graphic). The goal of "a distinct personality per draft" is carried by the S7 result image.
- 기법 3: 서브에이전트로 긍정적 피드백 루프 만들기: S7 (why self-critique fails, critic sees only screenshots, Opus 5 builds / Fable 5 critiques, scoring out of 10, figure 15) and S8 (9/10 exit rule hidden from the critic, Fable under 10% of output tokens and double cost if Fable redesigned, tips: 4 expert designs + 1 of ours to rank, exit criteria with 1-2 trial runs). Condensed out: critic-guideline wording, the reference-image-as-moodboard tip, and the per-role model detail beyond the Opus/Fable split.
- 기법 4: 이미지 생성으로 디자인 풍부하게 만들기: S9 (problem, intent, figures 16-19 together, Claude Opus 5 before/after) and S10 (환경별 연결 방법: built-in tools, Codex CLI on a ChatGPT subscription, low-limit agent key, .env.agents, AGENTS.md/CLAUDE.md note). Condensed out: prompt specifics (shaders/3D, local-only key use, frame-by-frame browser check).
- 기법 5: 더 정교한 모션에는 영상 생성 활용하기: S11 (fal.ai, #### 눈길을 사로잡는 애니메이션 그래픽 만들기: solid-background loop + matting, figure 20 with GPT-5.6 Sol) and S12 (#### 상태 사이의 매끄러운 전환 만들기: keyframe interpolation, scroll scrubbing, figure 21 made with Codex GPT-5.6 Sol in one prompt). Condensed out: the "Will Smith spaghetti" aside, the crystal prompt wording and the Seedance 2.5 model name.
- 전달: 사용자가 좋아할 디자인으로 다듬기: S13 (does it make sense, does it flow, is it useful; the final call is human).
- 기법 6: 가치를 더하지 않는 요소 덜어내기: S14 (AI only adds, figure 22 issues: glow, colors, labels, custom controls; figure 23 result; people must push the removal).
- 기법 7: AI 티 없애기: S15 (each model's overused patterns read as slop, table rows 1-2) and S16 (table rows 3-4; don't ban them in the first prompt, check during polish).
- 기법 8: 카피는 직접 다시 쓰기: S17 (AI copy as Lorem ipsum, rewrite every line, Lantern comparison figure 25, the human version is shorter).
- Intentionally omitted: none of the NOTE2 sections. Inline links (pub.sakana.ai, fal.ai URLs) are reduced to names. The author/date line on S1 comes from NOTE.md §1 and the English title from README.md.
- Image ratio: 14 of 17 slides carry a real asset image (82%). The other three use a strong device: S8 numerals, S10 route map + code card, S13 check marks. Dark slides: S1, S4, S8, S11, S13 (5 of 17), never two in a row.

## Review log
- S1 text budget: the old divider carried 15 labels (11 technique names in three columns, plus a four-part source line). Cut to 3 phase labels + 1 source caption. The technique numbers in Anton are now the visual device, and the unused article figure-04 (the "AI slop" bell curve, NOTE.md §3) became the image. This keeps the part at or above 80% image slides after S10 lost its strips.
- S9/S10/S11 rhythm: three strip slides ran back to back, and S9 and S10 both used the same "two stacked before/after strips" layout. Figures 16-19 now sit together on S9 as a 2x2 grid (the source also groups them as 그림 16~19). S10 became a route map (tool chips → setup, plus a `.env.agents` / `CLAUDE.md` code card) with a stacked title, a layout no other neighbor uses. The S10 label for row 3 now includes "기타 도구" as in the source, and the `CLAUDE.md` note covers the AGENTS.md/CLAUDE.md point that was missing.
- S11/S12 consecutive repeat: both had title top-left with the image below. S12 now has the GIF bleeding off the top-right, text on the left and "TRANSITIONS" at 300px along the bottom (data-hdr="none").
- S9 text budget: 2 Korean lines + 3 labels cut to 1 line + chip + 1 caption.
- S12 text budget: 2 lines + 2 labels cut to 2 lines + 1 caption. The first line was also too wide for its column, so it was reworded to "두 정지 이미지 사이를 영상으로 잇는다".
- S4 coverage: added the Korean line "\"이게 될 리 없어\" 싶다면 제대로 가는 중" (NOTE2, end of 기법 2). The slide had no Korean line, and this tip had been silently dropped.
- S8 accuracy: "전문가 시안 4개" changed to "전문가 디자인 4개" (the source says 전문가 디자인). The <10% caption now also states the source's cost point (직접 맡기면 비용 두 배). The awkward "Fable 몫의 출력 토큰, 매번" was rewritten.
- S2 labels: "(Claude Opus 5)" moved into the label text, and the second label was reworded so it reads as one phrase. Figure-05 is described as "mostly purple" because one of its four pages is teal.
- S6: chip "2" moved from the eyebrow line to sit next to the headline it points at. Added a note to keep the slide cream (a near-black tile on a black slide loses its edge).
- S7: Korean line reads "10점 만점으로 채점" (it was missing the particle).
- S14: frames widened from 620 to 640 so both phones, including side buttons, keep a safe margin. The captions drop the redundant "BEFORE:" and "AFTER:" prefixes because the underlined BEFORE/AFTER words are already there. The Korean line now reads "빼기는 사람이 시켜야" (source: 사람이 밀어 줘야 한다), because "밀어 준다" read as "supports".
- S16: "처음부터 금지 말고, 다듬을 때 점검하고 비교" tightened to "처음부터 금지하지 말고 다듬을 때 점검".
- S3: Sakana credit made into one phrase ("Sakana AI의 String Seed of Thought").
- Notes: confirmed figure-07 and figure-14 have the same md5. Added a note that figure-15 and figures 16-20 show the same four designs on purpose. Flagged that Part 01 S1 also uses figure-21, so Part 01 should swap that cell.
- Verified, no change needed: every image path exists. All 11 derived crop boxes were test-cropped, and each lands inside its tile with clean corners (crop files still need to be written to deck/img/02/). Model names (Claude Opus 5, Claude Fable 5, GPT-5.6 Sol) match NOTE2. No middle-dot character anywhere.
