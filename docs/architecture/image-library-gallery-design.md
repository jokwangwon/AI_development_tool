# 이미지 보관함(Gallery/Library) 설계

> 무검열 텍스트→이미지 파이프라인의 **생성 후(post-generation) 보관·정리·다운로드** 계층.
> 상태: **IMPLEMENTED** (2026-06-19, prompt_lab `5aeeeac`, 100 passed/+34). 구현=`~/prompt_lab`(앱) · gen_gate **무변경**(generic 유지).
> 답습: `uncensored-prompt-to-image-pipeline-design.md`(생성 흐름) · `prompt-keyword-dictionary-design.md`(레지스트리 패턴) · 헌법 5조-2 Provider Liquidity.

---

## 1. 동기 / 문제

현재 gen_gate 는 생성 즉시 `outputs/<md5>.png` 로 **익명 저장만** 한다:
- 프롬프트·시드·모델·LoRA·스타일·키워드 등 **메타데이터 기록 0**.
- 브라우징/다운로드/정리 **UI 0**. outputs/ 는 테스트 스텁(0·7B)·3D glb 까지 섞인 누적 더미.

사용자 요구: **마음에 든 이미지를 (1) 저장, (2) 다운로드, (3) 보관함에서 열람, (4) 정리(모델별 그룹 + 선택 이미지 컬렉션), (5) 삭제**.

---

## 2. 계층 결정 — 보관함은 prompt_lab(앱) 소유

| 후보 | 판단 |
|------|------|
| gen_gate 에 gallery 추가 | ❌ gen_gate=**generic 게이트**(만화·VTuber·motion 도 호출, provider-liquidity). "보관함"=UX 관심사 → generic 서비스 오염. |
| **prompt_lab 이 소유** | ✅ webapp 이 생성 시점에 메타데이터를 **모두 손에 쥠**(prompt·model·lora·style·seed·keywords). 앱 계층의 자연스러운 책임. gen_gate 무변경. |

**결정: 보관함 = prompt_lab. gen_gate 코드 0 변경.**

---

## 3. 확정된 사용자 결정 (2026-06-19, AskUserQuestion + 후속)

| # | 결정 | 근거 |
|---|------|------|
| D1 | **명시적 저장 버튼**(전체 자동 기록 ❌) | "원하는 이미지가 생성됐어 이걸 저장" = 큐레이션. outputs 익명 누적과 분리. |
| D2 | **prompt_lab 으로 복사**(참조만 ❌) | 자족적 — gen_gate outputs 정리돼도 보관함 안전, 다운로드 깔끔, 원본 보존. |
| D3 | **그룹 둘 다** — 자동 모델 facet + 사용자 컬렉션(앨범) | 요청 그대로. |
| D4 | **삭제 가능** | 개별/일괄 영구 삭제 + 컬렉션에서 빼기(영구 삭제와 구분). |

---

## 4. 데이터 모델

`~/prompt_lab/library/`(`PROMPT_LAB_LIBRARY` env 로 재배치 가능, 하드코딩 금지):
```
library/
  images/<item_id>.png      # 복사된 이미지 파일(D2)
  manifest.jsonl            # 항목 1줄(append-only 기록, 삭제는 재작성)
  collections.json          # {cid: {name, created_at, item_ids:[...]}}
```

**item 레코드**(manifest.jsonl 한 줄):
```json
{
  "id": "<10자 토큰>", "file": "images/<id>.png", "created_at": "ISO8601",
  "prompt": "...", "model": "animagine-xl-4.0", "lora": "silver-royal",
  "style": "anime-illustration", "seed": 12345,
  "keywords": [{"key":"hetero-pair","weight":1.0}], "commercial": false,
  "source_url": "/outputs/<gen_gate_fid>.png"
}
```
- `id` = 보관함 고유 토큰(gen_gate fid 와 독립 — 복사본이므로).
- 그룹은 **저장하지 않음**: 모델 facet 은 `model` 필드에서 *파생*(D3 자동). 컬렉션만 명시 멤버십(`collections.json`).

---

## 5. 모듈 — `prompt_lab/library.py` (네트워크 무관, 주입식)

순수 함수/클래스. **이미지 바이트 fetch(gen_gate HTTP)는 webapp 이 주입** → library.py 는 파일시스템만, 테스트는 임시 디렉터리로 네트워크 0(webapp fetcher 패턴 답습).

```
class LibraryStore:
    def __init__(self, base_dir): ...
    def save(self, *, image_bytes, meta) -> dict        # 파일 복사 + manifest append, item 반환
    def list(self, *, model=None, collection=None) -> list[dict]   # 필터(자동 facet)
    def get(self, item_id) -> dict | None
    def delete(self, item_id) -> bool                   # 파일+manifest 제거 + 모든 컬렉션에서 제거
    def models(self) -> list[dict]                       # 모델별 개수(자동 그룹 메뉴)
    # 컬렉션
    def collections(self) -> list[dict]                  # {id,name,count}
    def create_collection(self, name) -> dict
    def delete_collection(self, cid) -> bool             # 앨범만 삭제(이미지 보존, D4 구분)
    def add_to_collection(self, cid, item_ids) -> dict
    def remove_from_collection(self, cid, item_id) -> dict
```
- **fail-closed/검증**: 미존재 id/cid → 명시 오류. item_id·cid 는 토큰 패턴만 허용(경로 traversal 차단 — `../` 거부, basename 강제).
- manifest 재작성은 원자적(temp + os.replace).

---

## 6. webapp 엔드포인트 (prompt_lab, Starlette)

| 메서드 | 경로 | 동작 |
|--------|------|------|
| POST | `/api/library/save` | body=메타+`source`(gen_gate url/raw). webapp 이 gen_gate `/outputs/..` 바이트 fetch → store.save. **localhost 강제**(R7 답습, source 경로만 허용·외부 URL 거부). |
| GET | `/api/library` | `?model=&collection=` 필터 목록. |
| GET | `/api/library/models` | 모델별 자동 그룹(개수). |
| DELETE | `/api/library/{id}` | 영구 삭제(파일+레코드). |
| GET | `/api/library/collections` | 컬렉션 목록. |
| POST | `/api/library/collections` | `{name}` 생성. |
| DELETE | `/api/library/collections/{cid}` | 앨범 삭제(이미지 보존). |
| POST | `/api/library/collections/{cid}/items` | `{item_ids}` 담기. |
| DELETE | `/api/library/collections/{cid}/items/{item_id}` | 컬렉션에서 빼기. |
| (mount) | `/library/images/<id>.png` | StaticFiles 서빙(다운로드·썸네일). |

저장은 사용자의 명시 버튼 클릭에만 호출(자동 경로 0 — 파이프라인 안전 경계 답습).

---

## 7. UI (index.html, 프론트 전용 — 백엔드 위 엔드포인트만 사용)

- **결과 카드**: `⬇ 다운로드`(library 또는 gen_gate url `<a download>`) + `🗂 보관함에 저장`(메타 동봉 POST). 저장 후 ✓.
- **🗂 보관함 모달**(기존 modal-overlay 패턴 재사용 — 키워드 사전 모달 동형):
  - 상단: 모델 필터 탭(자동) + 컬렉션 칩(+ 새 컬렉션).
  - 그리드: 썸네일 + 호버 메타(프롬프트·시드·모델·LoRA). 클릭=확대/다운로드.
  - 선택 모드(☑): 다중 선택 → `컬렉션에 담기 ▾` / `⬇ 일괄 다운로드` / `🗑 삭제`.
  - 컬렉션 보기에서 항목 ✕ = 컬렉션에서 빼기(영구 삭제 아님, D4).

---

## 8. 콘텐츠/안전

- 보관함은 **로컬 전용**(사용자 자신의 파일). 무검열 콘텐츠 저장 가능 — 한국 법·콘텐츠 감독=**사용자 직접 책임**(콘텐츠 게이트 DEFER 불변, 기존 합의 답습). 새 게이트 0.
- 절대 금지선(가상 미성년 성적)=영구 불가(파이프라인 상류 책임, 보관함은 사후 계층이라 별도 게이트 추가 안 함).

---

## 9. 검증 (TDD)

- `library.py`: save/list/필터/delete/모델그룹/컬렉션 CRUD/traversal 거부 — 임시 디렉터리, 네트워크 0.
- `webapp`: 주입 store + 주입 fetcher 로 엔드포인트(저장 시 fetch 호출·404·외부 URL 거부) — 실 HTTP 0.
- 라이브(GPU 무관): 2서버 기동 → 기존 이미지 저장→목록→컬렉션 담기→다운로드→삭제 왕복.

---

## 10. 규모/프로세스

- "중간 규모 기능"(CLAUDE.md §3 매트릭스) → full 3+1 생략. 게이트 = **UI mockup 컨펌(완료) + 이 설계 검토**. gen_gate 무변경·기존 안전 경계 불변이라 신뢰경계 신규 0.
- AI_dev = **docs만**(jarvis 코어 무변경). 구현 커밋 = prompt_lab.
