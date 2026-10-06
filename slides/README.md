# Design Eye 슬라이드

SLIDE1.md → NOTE2.md → HOW_DESIGN_FROM_CC.md 순서로 만든 16:9 발표 자료입니다. 짧은 제목과 원본 Figure를 중심으로 구성했습니다.

`ref/`의 크림색·검정 대비, 비대칭 이미지 배치, 가장자리까지 이어지는 Figure, 작은 세 지점 페이지 표기를 적용했습니다. 편집 가능한 텍스트는 모두 Pretendard이며, 제목은 68px Black, 표지는 88px Black으로 크게 강조했습니다. 원본 Figure 안의 글꼴과 색은 자료의 일부로 유지합니다. 스타일과 대표 배치는 `style_deck.py`에 정의되어 있습니다.

- [브라우저 슬라이드](index.html): 38장, 움직이는 Figure 재생
- [PowerPoint](design-eye.pptx): 제목, 도형, 이미지 배치 편집 가능
- [PDF](deck.pdf): 38장, 정지 이미지
- [전체 미리보기](shots/all/contact.jpg)

1–6장은 SLIDE1의 도입, 7–28장은 NOTE2의 여덟 가지 기법, 29–38장은 Claude Code 실전입니다. 모든 장에 한 문장 요약을 넣고, NOTE2 파트에는 번역된 프롬프트 전문을 Figure 옆이나 아래에 배치했습니다. 긴 디자인 평가자 프롬프트와 평가 기준 예시는 각각 별도 슬라이드로 구성했습니다. Figure 11–13은 아이디어 나열 → 취향 반영 → 제작 프롬프트의 세 장으로 보여 줍니다. 중복 시안 Figure 14는 생략하고, 긴 세로 Figure 15·24는 비교할 부분을 확대했습니다.

NOTE2 파트의 텍스트 기준은 [로컬 한국어 번역문](../clone/how-to-turn-your-ai-into-a-world/index.html)입니다. 제목과 요약은 이 번역문의 표현과 내용을 바탕으로 작성하고, 직접 요청과 평가 예시 19개는 생략 없이 인용했습니다. Figure 13의 AI 작성 프롬프트는 번역문 자체가 ‘이하 생략’으로 끝나므로 표시된 범위임을 명시했습니다. 기법 7은 그림의 비교 항목을 그대로 옮겼으며, 기법 8에는 작성자가 고친 문구의 번역 전문을 넣었습니다. 원문에 없는 요청문은 만들지 않습니다. 발표자 노트와 콘텐츠의 source_blocks에 근거를 기록했습니다.

## 발표

`index.html`을 브라우저에서 엽니다. 방향키·스페이스로 이동하고, Home/End로 처음·마지막 장으로 이동합니다. F는 전체 화면, N은 발표자 노트입니다. 화면 오른쪽 클릭은 다음 장, 왼쪽 클릭은 이전 장이며 휴대폰에서는 좌우로 스와이프할 수 있습니다.

HTML은 이 저장소의 이미지와 글꼴을 상대 경로로 읽습니다. 다른 컴퓨터에 단일 파일로 전달할 때는 PPTX나 PDF를 사용합니다. PPTX와 PDF는 움직이는 Figure의 대표 프레임을 담았습니다. PPTX의 원본 Figure 내부 글자는 이미지의 일부입니다. Pretendard 글꼴 파일은 `fonts/`에 있습니다.

HTML과 PDF 제목은 Pretendard Black입니다. PPTX는 한글 글꼴 호환성을 위해 Pretendard Bold에 동일색 외곽선을 적용합니다. 외곽선을 지원하지 않는 뷰어에서는 Bold로 표시됩니다.

## 다시 생성

Python의 Pillow, lxml, python-pptx, Playwright와 ffmpeg가 필요합니다.

```sh
python3 slides/prepare_media.py
python3 slides/export.py
python3 slides/render.py --pdf
```

`compose.py`가 세 파트를 구성합니다. NOTE2는 `article-copy.json`의 제목·요약·근거 ID를 사용하고, `article_content.py`가 로컬 HTML에서 인용문을 직접 읽어 배치합니다. `article-prompts.json`은 프롬프트 전문과 Figure 번역 대조 자료입니다. 이전의 `note2-copy.json`은 생성에 사용하지 않습니다. `cc-slides.json`은 마지막 파트, `titles.json`은 기존 명사형 제목을 정의합니다. `content.json`은 세 파트를 합친 결과입니다. `export.py`는 HTML 조각과 PPTX를 생성하고 `render.py`는 화면 미리보기와 PDF를 만듭니다. 기존 `parts/00-kit.html`은 견본으로 남아 있으며 실제 발표에는 포함되지 않습니다.

각 장의 발표자 노트에 원문 문서, Figure 경로, 출처 URL을 넣었습니다. 사이트 캡처는 로컬에 저장된 참고 화면으로, 영상 녹화 시점과 동일한 화면이라는 의미는 아닙니다.
