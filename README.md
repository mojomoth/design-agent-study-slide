# AI를 최고 수준의 디자이너로 만드는 방법

큰 단일 HTML과 원본 영상은 Git LFS로 저장합니다. 저장소를 내려받을 때 Git LFS를 설치한 뒤 `git lfs pull`을 실행하면 원본 파일을 받을 수 있습니다. 슬라이드 HTML, PDF, PPTX와 이미지, 영상, 중간 생성물도 저장소에 포함되어 있습니다. 최종 발표 자료는 [슬라이드 안내](slides/README.md)에서 확인할 수 있습니다.

사용자가 제공한 `guide/How to turn your AI into a world-class designer.html`과 함께 저장된 이미지 파일을 바탕으로 전체 한국어 번역본을 만들었습니다.

## 결과물

| 파일 | 내용 |
| --- | --- |
| [단일 HTML](clone/how-to-turn-your-ai-into-a-world/index.html) | 글 전체의 한국어 번역과 본문 그림 25개 |
| [슬라이드 노트](slide-notes.md) | 기법마다 한 장씩 정리한 노트 8장 |
| [이미지 폴더](assets/how-to-turn-your-ai-into-a-world/) | 제공된 원본 이미지 47개 |
| [이미지 목록](.work/guide-clone/assets-manifest.json) | 원본 파일과 그림 번호의 대응 관계, 파일 크기와 해시 |

## 번역과 보존 범위

글의 제목, 부제, 머리말, 본문, 프롬프트 예시와 맺음말을 번역했습니다. 본문의 문단과 제목 182개를 모두 반영했고, 인용문과 목록, 링크, 그림의 순서를 유지했습니다. 원문에 적힌 모델 이름과 수치도 그대로 옮겼습니다.

본문 그림 25개를 HTML 안에 넣었습니다. 움직이는 이미지 12개도 원본 상태로 보존했습니다. 함께 저장된 프로필 사진과 로고 등을 포함해 이미지 파일 47개를 모두 `assets/` 아래에 복사했고, 원본과 파일 내용이 같은지 확인했습니다.

그림 속 영문은 원본 그대로 유지했습니다. 대화 예시 세 개와 디자인 비교표, 홍보 문구 비교처럼 글을 읽어야 하는 그림 다섯 개에는 아래에 한국어 번역을 붙였습니다. 모든 본문 그림에는 한국어 설명을 추가했습니다.

원본의 스타일을 사용하되, 저장본에 들어 있지 않은 웹 글꼴은 한국어 시스템 글꼴로 대체했습니다. 댓글, 추천 글, 로그인과 구독 조작 화면은 제외했습니다. 본문에 있는 구독 안내 문장은 번역에 포함했습니다. 사이트의 스크립트와 추적 요청은 제거했습니다.

HTML은 이미지와 스타일을 모두 포함한 파일 하나입니다. 다른 파일 없이 열 수 있으며, 원본 GIF를 포함해 파일 크기는 약 174MB입니다. `guide/`의 원본은 수정하지 않았습니다.

## 슬라이드 노트

원문의 여덟 가지 기법을 각각 한 장의 노트로 구성했습니다. 제목은 명사로 끝나며, 각 기법의 번역 본문과 프롬프트 예시를 완성된 클론에서 직접 가져왔습니다. 세 단계의 도입 설명을 포함해 원문 구간 147개를 반영했습니다.

각 파트에는 클론의 해당 위치로 이동하는 링크와 필요한 figure의 파일 경로, 첨부 목적, 원본 이미지를 넣었습니다. 기법에 대응하는 그림 21개를 연결했고, 대화 예시와 비교표, 홍보 문구 이미지에 담긴 한국어 번역도 콘텐츠에 포함했습니다. 별도 표지나 장식은 넣지 않았습니다. [파트와 원문 구간의 대응 목록](.work/guide-clone/slide-notes-source-map.json)에서 연결 관계를 확인할 수 있습니다.

한국어에는 [fluent-korean 작성 지침](https://github.com/snflkd/fluent-korean/blob/main/plugins/fluent-korean/output-styles/fluent-korean.md)을 적용했습니다. 지침 전문을 읽고 번역과 노트의 문장을 검토했습니다. 가운뎃점은 쓰지 않았습니다.

## 출처

Anshu Chimala, [How to turn your AI into a world-class designer](https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world), Lenny’s Newsletter, 2026년 9월 1일.

## 확인 결과

인터넷 연결을 차단한 브라우저에서 화면 너비 1440px과 390px을 확인했습니다. 본문 182개 구간과 HTML에 포함된 이미지 28개가 모두 표시되며, 가로로 잘리는 내용이나 외부 요청은 없었습니다. 본문 그림 25개와 로고 두 개, 작성자 사진 한 개를 합한 수입니다. 원본 제목 앵커 17개와 본문 링크도 보존했습니다.

복사한 이미지 47개와 HTML에 넣은 본문 그림 25개는 원본과 해시가 일치합니다. 자세한 결과는 [확인 기록](.work/guide-clone/qa-report.json)에 있습니다.

## 다시 생성하는 방법

Python의 `lxml`과 `Pillow`가 설치된 환경에서 다음 명령을 실행하면 됩니다. 번역문과 그림 설명은 `.work/guide-clone/`에 있습니다.

```sh
python3 scripts/build_clone.py
python3 scripts/build_slide_notes.py
```
