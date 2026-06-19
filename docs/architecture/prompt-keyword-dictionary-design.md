# 특수 키워드 사전 + 수동 프롬프트 강화 설계 (Keyword Dictionary)

> 상태: **IMPLEMENTED v1 (TDD 완료 + 라이브 검증)** · 날짜: 2026-06-19 · 유형: 아키텍처 설계 (SDD)
> 구현: gen_gate `ffef5d0`(`keywords.py`+`keyword_registry.json`+`gate.generate(keywords=)`+`GET /api/keywords`+`POST /api/compose_prompt`, 164 passed) · prompt_lab(`/api/keywords`·`/api/enhance` 프록시+generate keywords 전달, 53 passed). 라이브: 실 레지스트리 로드·멱등 dedup·미등록 400 실증(GPU 무관, compose 경로). **AI_dev 코드 0(docs만).**
> UX 후속: prompt_lab `0b2cb5d`(키워드 **검색+클릭 추가+적용칩**) · `316b178`(**프롬프트 직접 입력** — dolphin3 저작 선택화, ②의 사람 승인 게이트 불변) · `f23379c`(**📖 사전 도감 모달** — 헤더 항시·검색·전체 상세 읽기전용).
> 시드 확장: gen_gate `93ce13f`(12)→`af5fad7`(13 entries) — 구성 닻(hetero-pair=1girl,1boy,hetero+융합 negative·solo-girl)·체위(missionary/cowgirl/from-behind)·표정(ecstasy-face·ahegao)·상황(after-sex-flaccid=사정 후 이완, negative로 진행중 액션 억제). 동기=인물 수/체위 누락이 2인 장면 해부학 붕괴 1순위.
> 가중치: `(tag:1.2)`(어텐션 가중, lpw 적용) — **그룹 가중 `(a, b, c:1.2)` 지원**(gen_gate `9935a6e`): `_split_tags` paren-aware(괄호 안 콤마 비분리)로 그룹 한 토큰 보존+dedup 멱등.
> **UI 가중치 — 칩별 가중치**(gen_gate `f34895f`·prompt_lab `00ae03e`, 디자인 재설계): 전역칸 폐기→**한 칩=한 괄호 그룹**, 칩의 −/＋ 로 그 키워드만 가중(└ 그룹 미리보기). `activeKeywords=[{key,weight}]`, 클릭=칩 추가(textarea 안 박음), 생성 시 베이스+칩 합성. gen_gate `compose_keyword_items([(spec,weight)])`+`gate.generate` keywords=list[str]|list[{key,weight}]. ⭐ 그룹-인식 dedup(`_covered_keys`)로 생성 단계 평문 재적용 이중적용 방지. 보기=📖 사전 모달. (이전 `caf4a0a`/`04c4db5`=전역 가중치칸, 분산·그룹 불가시 피드백으로 칩별 전환.)
> K1=(b)서버 · K2=안정화 우선+소수 효과 · K3=X(수동만) — 사용자 권고 채택(§7).
> 동기: dolphin3 자유 저작이 상충 태그로 **해부학 붕괴(머리 두 개 등)**를 유발 → 검증된 키워드 스니펫을 *수동* 선택 주입해 안정화 + negative 보강.
> 모법: `docs/architecture/uncensored-prompt-to-image-pipeline-design.md` (OPERATIONAL v3) — 본 설계는 그 위에 얹는 레버.
> 선례(동형): gen_gate `styles.py`/`style_presets.json` (룩 프리셋), `loras.py`/`lora_registry.json` (캐릭터 정체성).
> 적용 대상: `~/gen_gate` (레지스트리+compose 로직) + `~/prompt_lab` (webapp 노출·주입). **AI_dev(`src/jarvis/`) 코드 변경 0** — jarvis 코어 무변경.
> ⚠️ 콘텐츠 게이트는 기존 결정 불변(DEFER, 사용자 직접 감독). 본 설계는 안전 경계를 **약화하지 않는다**(§5).

---

## 0. 한 줄 요약

사용자가 재사용 가능한 **검증된 키워드 묶음**(이름→danbooru 태그 + 선택적 negative 보강)을 사전에 저장하고, 프롬프트 생성 흐름에서 **수동 선택**해 주입한다. 주입은 **사람 승인 *전*** 검토 단계에서 일어나, 사용자가 강화된 최종 프롬프트를 보고 승인한다(안전 경계 불변, 붕괴 즉시 수정 가능).

---

## 1. 사용자 확정 입력 (2026-06-19, brief 승인)

| 항목 | 결정 | 근거 |
|------|------|------|
| 사전 내용 | **자연어→danbooru 용어집 + 재사용 스니펫(이름→태그 묶음)** | 둘 다 선택. 한 스키마가 둘 다 표현(§3.1) |
| 강화 방식 | **수동 — 사용자가 사전 키워드를 골라 주입** | 결정적·예측 가능, 검토 입도 유지 |
| 위치 | **gen_gate 레지스트리 (styles·loras 동형)** | 모든 소비자(만화·VTuber 등) 공유, provider-liquidity 정합 |
| 합의 깊이 | **SDD 문서 → 검토 → TDD** (full 3+1 생략) | 선례 답습 + 안전 게이트 불변 → ceremony 회피(`feedback_ceremony_inflation`) |

---

## 2. 동기 — "흐름에 안 맞으면 머리 두 개" 문제

`uncensored-prompt-to-image-pipeline-design.md` 흐름에서 dolphin3 는 *내용 태그*를 자유 저작한다. 자유 저작은 다음으로 해부학을 깬다:

- **상충 태그**: 시점/포즈/구도가 서로 모순(예: `from above` + `from side` 동시) → 모델이 봉합 실패 → 중복 머리·여분 팔다리.
- **약한 negative**: 전역 style 프리셋의 negative 만으로는 특정 조합의 붕괴를 못 막음.

본 설계의 두 방어:

1. **검증된 스니펫 주입** — 알려진-좋은 태그 조합(사용자가 미리 검증해 저장)을 골라 넣어, dolphin3 의 불안정 어휘를 보강·교정.
2. **항목별 negative 보강** — 사전 항목이 `negative_extra`(예: `extra heads, multiple heads, conjoined`)를 같이 실어, 그 키워드를 쓸 때 붕괴를 *직접* 억제.

style 프리셋(전역 룩 negative)과 **직교**: style=항상 적용되는 룩/품질, keyword=사용자가 건별 선택하는 내용·안정 레버.

---

## 3. 데이터 모델

### 3.1 레지스트리 스키마 (`~/gen_gate/keyword_registry.json`)

용어집과 스니펫은 **구조적으로 동일**(이름→태그 묶음) — 한 스키마가 둘 다 표현한다.

```json
{
  "neon-glow": {
    "label": "네온 글로우",
    "group": "효과",
    "tags": "glowing neon, bioluminescent, rim lighting",
    "negative_extra": "",
    "notes": "재사용 스니펫 — 효과 묶음"
  },
  "twin-tails-stable": {
    "label": "트윈테일(안정)",
    "group": "헤어",
    "tags": "twintails",
    "negative_extra": "extra heads, multiple heads, conjoined",
    "notes": "자연어→danbooru 용어집 + 해부학 안정 negative"
  },
  "dynamic-action-safe": {
    "label": "다이내믹 액션(안정)",
    "group": "포즈",
    "tags": "dynamic pose, action shot, motion blur",
    "negative_extra": "extra limbs, extra arms, deformed, bad anatomy",
    "notes": "큰 포즈의 사지 붕괴 억제"
  }
}
```

| 필드 | 필수 | 의미 |
|------|------|------|
| `label` | ✅ | 사람이 보는 자연어 이름(웹 체크박스 라벨). 용어집의 "자연어" 측. |
| `group` | ✅ | UI 그룹(효과/헤어/포즈/구도 …). 체크박스 분류. |
| `tags` | ✅ | 주입할 정식 danbooru 태그(콤마 구분). 용어집의 "정식 태그" 측 = 스니펫 본문. |
| `negative_extra` | — | 이 키워드 사용 시 negative 에 합칠 안정화 태그(없으면 `""`). |
| `notes` | — | 운영 메모(용도·검증 이력). |

> provider-liquidity: 키워드 추가 = JSON 한 줄, 코드 변경 0(styles/loras 와 동일).

### 3.2 gen_gate 로직 (`~/gen_gate/keywords.py` — styles.py 동형)

순수 함수 + 에러 타입(`styles.py`·`loras.py` 패턴 그대로):

```python
class KeywordError(Exception): ...                 # 미등록 키 → 400

def load_keywords(path=None) -> dict: ...          # registry 로드
def get_keyword(kws, key) -> dict: ...             # 키→spec(없으면 KeywordError)
def keyword_prompt(specs, prompt) -> str: ...      # 선택 tags 를 prompt 에 합성
def keyword_negative(specs, base_negative) -> str: ...  # negative_extra 합성
```

- `keyword_prompt`: 선택된 spec 들의 `tags` 를 프롬프트 **뒤**(내용 보강)로 append, 중복 태그 제거. (트리거를 *앞*에 거는 LoRA 와 반대 — keyword 는 내용 보강이라 후위.)
- `keyword_negative`: 선택된 spec 들의 `negative_extra` 를 base negative 에 합집합으로 합성.
- 합성 순서는 §4 에서 style/lora 와의 결합 순서로 고정.

### 3.3 `gate.generate(keywords=[...])`

`generate` 에 `keywords: list[str] | None` 파라미터 추가(`style=`/`lora=` 동형):

- `keywords` 의 각 키를 `get_keyword` 로 검증(미등록 → `KeywordError`).
- 합성 순서(§4) 에 따라 prompt·negative 에 반영.
- 비-웹 소비자(만화·VTuber 등)도 동일 API 로 키워드 재사용.

### 3.4 HTTP — `GET /api/keywords`

`/api/styles`·`/api/loras` 동형. group 별로 정렬된 `{key, label, group, tags, negative_extra, notes}` 반환(웹 체크박스 구성용). `KeywordError`/`StyleError`/`LoraError` → 400.

---

## 4. 합성 순서 (4축 + 키워드)

기존 4축(내용·베이스·style·LoRA)에 키워드를 끼워넣는 **고정 순서**:

```
prompt  = lora_trigger ⊕ [ style_prefix ⊕ (dolphin3 내용 ⊕ keyword_tags) ⊕ style_suffix ]
negative = base_negative ⊕ style_negative_extra ⊕ keyword_negative_extra
```

- **키워드 tags** 는 dolphin3 내용 *직후*(style prefix/suffix 안쪽) — 내용 보강 의미.
- **LoRA 트리거**는 최선두(정체성 바인딩, 기존 `lora_trigger_prompt` 불변).
- **negative** 는 base → style → keyword 누적 합집합(중복 제거). 안정화 negative 가 항상 살아남음.
- 중복 태그는 합성 시 dedup(같은 태그가 style·keyword 양쪽에 있어도 1회).

---

## 5. ⭐ 주입 지점 — 안전 경계 보존 (BLOCKING 불변식)

키워드 주입은 **사람 승인 *전*** = prompt_lab 웹 검토 단계에서 일어난다.

```
의도(자연어)
  │ author_prompt: dolphin3 저작(텍스트, 자동 승인 — 기존)
  ▼
[웹: 사용자가 키워드 체크 → 강화된 프롬프트 자동 구성 → 편집 textarea 갱신]
  │
  ▼
사용자가 *강화된 최종 프롬프트 전문* 검토·편집
  │ generate_image: plan_approver 가 그 전문을 보고 승인(콘텐츠 게이트 GP-3)
  ▼
gen_gate 이미지 생성
```

근거:

- **콘텐츠 게이트 불변(GP-3)**: 사용자가 승인하는 프롬프트 = 주입 키워드 *포함* 최종본. 키워드가 콘텐츠를 바꿔도 사람이 그 전문을 보고 승인 → 기존 안전 경계(`uncensored-...-design.md` §5) 약화 0.
- **붕괴 즉시 수정**: 강화 후 머리 두 개 등 이상하면 그 자리 textarea 에서 사용자가 고침(§2 동기 충족).
- **default-deny 불변**: `generate_image(plan_approver=None)` → 미실행 유지.

> ⚠️ 안티패턴(채택 안 함): 키워드를 `gate.generate` *내부*(승인 후)에서만 주입하면 사용자가 검토한 프롬프트와 실제 생성 프롬프트가 달라져 안전 경계가 깨진다. → 로직(레지스트리+compose)은 gen_gate 소유하되, **웹 경로의 주입은 승인 전**에서 수행. `gate.generate(keywords=)` 직접 호출은 비-웹/단일-호출 소비자용(그쪽은 호출자가 곧 감독자).

---

## 6. 구현 범위 (TDD)

### 6.1 gen_gate (`~/gen_gate`, master)

| 산출물 | 내용 | 테스트 |
|--------|------|--------|
| `keyword_registry.json` | 초기 시드 키워드(효과/헤어/포즈/구도 + 안정화 negative) | — |
| `keywords.py` | `load/get/keyword_prompt/keyword_negative` + `KeywordError` | RED→GREEN 순수 함수 |
| `gate.generate(keywords=)` | §3.3 통합 + §4 합성 순서 | 키워드 적용·미등록 400·dedup·negative 합성 |
| `GET /api/keywords` | §3.4 | 목록·group·400 |

### 6.2 prompt_lab (`~/prompt_lab`)

| 산출물 | 내용 | 테스트 |
|--------|------|--------|
| webapp `/api/keywords` 프록시 | gen_gate 서버사이드 프록시(CORS 회피, styles/loras 동형) | 프록시·실패 처리 |
| webapp `/api/enhance` 프록시 | gen_gate `POST /api/compose_prompt` 프록시(클릭/강화 합성) | 프록시·실패 처리 |
| `static/index.html` | **검색(클라 필터) + 클릭 추가 + 적용칩** — 사전 browse + 검색(이름·태그·그룹·메모) + 클릭 시 `/api/enhance`(서버 dedup) 로 태그 추가 + `activeKeywords` 칩 추적(생성 시 전달=negative 자동 적용). 🛡️=negative 포함. 칩 ✕=적용 해제(텍스트는 사용자 편집) | (스모크/라이브) |

### 6.3 AI_dev (`src/jarvis/`)

- **코드 0** — jarvis 코어 무변경(라이브러리 재사용). 본 설계 문서 + 이후 CONTEXT/세션 로그/메모리만.

---

## 7. 결정 항목 (확정 — 사용자 권고 채택 2026-06-19)

| # | 항목 | 결정 | 근거 |
|---|------|------|------|
| K1 | 강화 프롬프트 구성 위치 | **(b) 서버** — webapp `/api/enhance` → gen_gate `POST /api/compose_prompt` | gen_gate 단일 진실원. compose 로직이 generate 와 *같은* `keyword_prompt` 사용 → 미리보기=생성 합성 일치 |
| K2 | 초기 시드 키워드 세트 | **안정화 우선 + 소수 효과** | `anatomy-stable`(순수 negative)·`dynamic-action-safe`·`full-body-safe` + `neon-glow`·`soft-lighting`. 동기(붕괴 방지) 직결 |
| K3 | author 단계 system prompt 노출 | **X (수동만)** | 사용자 결정(수동) 답습. 자동 어휘 인지는 별도 trigger 시 재논의 |

---

## 8. 검증 계획

1. **단위/통합(계산적)**: gen_gate keyword 함수 + generate 통합 + /api + prompt_lab 프록시·compose (TDD, 회귀 0).
2. **e2e(실증)**: 의도 → dolphin3 저작 → 키워드 체크(예: `dynamic-action-safe`) → 강화 프롬프트 검토 → 생성. **A/B**(같은 시드, 키워드만 변수)로 안정화 효과 가시화 — 특히 "큰 포즈에서 사지/머리 붕괴" 케이스로 §2 동기 실증.
3. **안전 경계 회귀**: `generate_image(plan_approver=None)` default-deny 유지 + 승인 프롬프트 = 실제 생성 프롬프트 동일성 확인(§5).

---

## 9. 정직 / 한계

- 키워드는 **완화 레버이지 보증 아님** — 검증된 스니펫도 다른 태그와 새로 충돌하면 붕괴 가능(그래서 §5 사람 검토가 핵심).
- negative 보강은 SDXL/애니 모델에서 효과가 태그·모델별로 다름(실측으로 시드 키워드 검증 필요).
- 자연어→태그 용어집의 *번역 품질*은 사용자가 등록한 매핑에 의존(자동 추론 아님 — 수동 결정 답습).
- 콘텐츠 게이트는 여전히 DEFER(사용자 직접 감독) — 본 설계는 그 결정을 바꾸지 않는다.

---

## 10. 태그 탐색(discovery) 레이어 — 큐레이션 사전과 별개 축 (구현됨)

큐레이션 사전(§3, 검증 스니펫+가중치+negative)과 **직교**: 수만 개 *실제 danbooru 태그*를
검색·발견하는 사전적 참조. "이 개념엔 무슨 태그가 있지?"를 푼다.

- **데이터**: `~/gen_gate/data/danbooru_tags.csv`(~14만, `name,category,count,"aliases"`).
  벤더 자산 — gitignore + `data/download_tags.sh`(a1111 tagcomplete), **런타임 네트워크 0**.
- **gen_gate** `5f48dd7`: `tags_db.py`(load/search 빈도순·공백↔underscore·alias·lookup/is_real)
  + `GET /api/tags?q=&limit=&cat=`(부분 검색·카테고리 필터·503 안내) + `POST /api/tags/validate`
  (이름 배치 → real/canonical/count, dolphin3 제안 실재 검증).
- **prompt_lab** `bf73e4a`: `TAG_SUGGEST_SYSTEM` + `suggest_tags`(build_pipeline `system_prompt`
  파라미터화로 재사용) + webapp `/api/tags`(검색 프록시)·`/api/suggest`(dolphin3 개념→태그 →
  gen_gate 실재 검증, 검증 실패 fail-soft). UI '🔎 태그 찾기' 모달: 부분 검색 자동완성 + 개념
  AI 제안(✓ 실제 / ✗ 미등록) → 클릭 시 ② 베이스 프롬프트에 추가(underscore→공백, dedup).
- 두 레이어: **DB = 실재 검증**(환각 차단) · **dolphin3 = 의미 확장**(개념→태그). 라이브 실증
  (`rainy neon alley`→night·city·alley ✓ / neon·rainy ✗).

## 11. 충돌 검출 시스템 (설계 — 구현 예정, 사용자 지정 다음 작업)

키워드/태그의 **의미 충돌**을 결정적 룰로 검출(계산적-우선, CLAUDE.md). "standing+정상위"
수동 수정(§ 직교 원칙)이 이것의 첫 인스턴스.

- **충돌 유형**: ① 같은-축 배타(자세 standing⊥lying, 시점 from above⊥from below) ② 인원
  요구 불충족(행위 2인 필요인데 solo/1girl) ③ 인원 수 모순(1girl+2girls) ④ 정반대 값(smile+angry).
- **설계**: 키워드 스키마에 `axis`(자세·시점·인원·행위·시간대·표정…) + 제약(`min_people`·
  `requires`/`conflicts`). 순수 검사기 = 활성 키워드 + 베이스 인원 태그(1girl/solo/2girls…) →
  경고 목록. 같은 axis = 상호배타.
- **집행(권장)**: 경고(비차단, 콘텐츠는 사용자 영역) + 같은-축 소프트 자동교체. 모호만 dolphin3.
