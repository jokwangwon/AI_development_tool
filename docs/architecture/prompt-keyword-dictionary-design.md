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

## 11. 충돌 검출 시스템 (구현됨 — gen_gate `39626b9`·prompt_lab `8c72406`)

키워드/태그의 **의미 충돌**을 결정적 룰로 검출(계산적-우선, CLAUDE.md). "standing+정상위"
수동 수정(§ 직교 원칙)의 일반화·자동화.

- **데이터**(registry): 키워드에 `axis`(자세·인원·표정·구도·상황 — 상호배타 축) + `min_people`
  (체위=2). axis 없는 키워드(효과·안정화)는 스택 가능. `/api/keywords` 가 axis·min_people 노출.
- **`conflicts.py`**: `detect_people`(solo=1·Ngirl/Nboy 합산·multiple≥3·신호 없으면 None) +
  `check_conflicts(active_keys, base_text, reg)` →
  ① **같은-축 배타**(같은 axis 2+ → 경고) ② **인원 요구**(min_people > 감지 인원 → 경고;
  인원 신호 *전무*면 스킵 = 거짓 경고 회피). `POST /api/check_conflicts`.
- **UI**(prompt_lab): 칩/베이스 변경 시 디바운스(250ms) 검사 → ⚠️ **비차단 경고**(콘텐츠는
  사용자 영역, 사람 판단). 검사 실패는 fail-soft(경고 부재, 작업 안 막음).
- 라이브: standing+정상위→"같은 축(자세) 충돌" · solo+정상위→"2인 필요하나 현재 1인".
- **미구현(후속)**: 정반대 값(smile⊥angry)·시점 축·같은-축 *소프트 자동교체*(현재 경고만).
- 16 tests(conflicts 12 + server 4), gen_gate 198·prompt_lab 65 passed.

## 12. NAI5/artist-mix 그림체 흡수 + 모델별 어휘 의존성 (구현됨 — gen_gate `de739e2`·prompt_lab `aedc032`, 2026-06-19)

사용자 공유 "그림체 프롬프트"(NAI5/ANAI 계열) 분석에서 출발. 발단=그림체 공유. 분석 결과
**그대로 복사 불가** — 단일 프롬프트가 아니라 **서로 다른 학습 어휘 3종의 혼합**이었음.

### 12.1 어휘 출신 분해 (핵심 인사이트)

| 토큰 | 출신 어휘 | 작동 베이스 |
|------|----------|------------|
| `score 9, score 8` | **Pony Diffusion** | Pony 전용 — illustrious/noobai/animagine 에선 **死토큰** |
| `very aesthetic, newest, year 2024/2025` | **NoobAI / Illustrious** | noobai-xl-vpred·illustrious-xl-2.0 ✅ / animagine ❌ |
| `masterpiece, absurdres, best quality, highres` | 범용 danbooru | 대부분 작동 |
| `(@artist:weight)` + `<lora:ANAI5:1>` | **NovelAI V4.5 그림체 로컬 포팅** | danbooru artist 태그 가중 블렌딩 — base 종속 |

→ 정체: **Illustrious/NoobAI 베이스 + ANAI5 LoRA + 다중 artist 가중 믹스**. `score_9`=관성 노이즈.
사용자 선호 확정 animagine 으로는 **전이 불가**(어휘 어휘 다름).

### 12.2 결정 — 모델별 사전 *분리* 안 함 (단일 사전 + base 메타 + UI 필터)

질문("모델별 사전 별도 처리?")에 대한 결정:

- **분리 ❌**. animagine/illustrious/noobai = 전부 **danbooru 학습 SDXL** → 기존 축(인원·자세·구도·
  상황·표정) 태그는 세 모델 공통. 분리 시 ~90% 중복.
- 실제 base 종속은 3종뿐, 각각 담당 메커니즘 존재:
  ① quality/aesthetic 어휘 → **style_presets**(이미 `model` 잠금) ② artist 태그 → **artist-mix 그룹
  + `base_lock`** ③ rating 태그 → rating 축 + `base_lock` 선택.
- 분리가 아니라 **표식(`base_lock`)** 이 정확한 도구. 한 스키마 원칙(styles·loras·keywords 동형) +
  Provider Liquidity(모델 교체 무코드) 보존.
- UI 노이즈는 **필터링**으로 해결(현 베이스 비호환 = 회색/숨김), 데이터 통합 유지. §11 충돌검출이
  base mismatch 경고를 재사용 제공.
- **예외(정직)**: 진짜 경계는 "모델별"이 아니라 **"프롬프트 패러다임별"**(anime-tag vs Qwen 자연어
  vs Pony-score). 레지스트리 `qwen-image`(실사·자연어)는 danbooru 태그 무의미 → 패러다임 다른
  모델 편입 시 *그때* 패러다임 단위 분리 검토. danbooru-anime 패밀리 안에서는 단일 사전.

### 12.3 도입 원칙

- **AI_dev 코드 0**(기존 키워드 세션과 동일, jarvis 코어 무변경). 구현 시 `~/gen_gate`·`~/prompt_lab`.
- 원본의 **반복·중복**(triple solo, negative `artist collaboration`×6 등) **도입 안 함** —
  가중치/그룹-인식 dedup 이 이미 우월(원시 강조의 1급 메커니즘 대체).
- 원본의 **Pony 死토큰**(`score 9/8`) **의도적 제외**.

### 12.4 style_presets.json — 2개 신규 (base-lock, 둘 다 프리셋)

```jsonc
"nai5-aesthetic-illustrious": {
  "label": "NAI5 그림체 (Illustrious·상업)",
  "model": "illustrious-xl-2.0",
  "prompt_prefix": "very aesthetic, newest, masterpiece, absurdres, best quality, highres, year 2024, year 2025",
  "negative_extra": "<§12.7 quality-stable 참조>",
  "levers": { "hires": true, "hires_upscaler": "realesrgan-anime", "hires_strength": 0.4 },
  "notes": "NAI5/ANAI 그림체 로컬 포팅. score_9 등 Pony 死토큰 제외. artist-mix(§12.5)·ANAI LoRA 조합 전제. clip_skip 미설정(illustrious 백지버그)."
},
"nai5-aesthetic-noobai": {
  "label": "NAI5 그림체 (NoobAI·개인전용)",
  "model": "noobai-xl-vpred",
  "prompt_prefix": "(동일)",
  "levers": { "hires": true, "hires_upscaler": "realesrgan-anime", "hires_strength": 0.4, "guidance_rescale": 0.7 },
  "notes": "v-pred 베이스 — guidance_rescale=0.7 필수(native). 다크/콘텐츠 자유도 최상, 상업 불가."
}
```
> 차이=`model` 잠금 + noobai 의 **v-pred native(guidance_rescale 0.7)**. prefix 어휘 공유.

### 12.5 keyword_registry.json — 신규 그룹 `그림체(artist-mix)` + 신규 필드 `base_lock`(승인)

LoRA 보다 가벼운 style 제어 축. 가중 artist 태그 묶음 = 합성 그림체 조각.
```jsonc
"artistmix-nai5-base": {
  "label": "NAI5 합성 그림체", "group": "그림체",
  "tags": "(mx2j:1.5), (yoneyama mai:1.1), (say hana:1.1), (quasarcake:0.8), (hizaka:0.7), (momoko \\(momopoco\\):0.3)",
  "negative_extra": "milkpanda, kurukurumagical, (taroimo \\(00120014\\):0.5), one-hour drawing challenge",
  "base_lock": ["illustrious-xl-2.0", "noobai-xl-vpred"],
  "notes": "danbooru artist 가중 블렌딩. animagine 비호환(태그 어휘 다름). 칩별 가중 조절 가능. artist 네거티브는 이 그림체 선택과 한 묶음(범용 anatomy 아님)."
}
```
> **신규 메타 `base_lock`(승인)**: artist 태그=base 종속. 불일치 베이스 선택 시 §11 충돌검출 패턴
> 재사용 → ⚠️ **비차단 경고**(키워드 레지스트리 첫 도입 필드).

### 12.6 rating 축 신설 (승인 — 시스템에 없던 새 축)

현 축(인원·자세·구도·상황·표정)에 **`등급`** 추가, 상호배타(`axis: 등급`).
```jsonc
"rating-safe":         { "tags": "safe",         "axis": "등급", "group": "등급",
  "notes": "SFW 확률↑(사용자 실측). 단 explicit position 태그 동반 시 NSFW 여전히 출력 — 차단 아님." },
"rating-sensitive":    { "tags": "sensitive",    "axis": "등급", "group": "등급" },
"rating-questionable": { "tags": "questionable", "axis": "등급", "group": "등급" },
"rating-explicit":     { "tags": "explicit",     "axis": "등급", "group": "등급" }
```
> §11 충돌검출 자동 적용 — `safe`+`explicit` 동시 선택 시 ⚠️ 경고. rating 태그 자체는 danbooru
> 공통이나 animagine 처리 차이 시 해당 엔트리에 `base_lock` 선택 부착 가능.

### 12.7 negative 보강 — `anatomy-stable` 확장 (별도 스니펫 아님)

기존에 없는 유효 항목만:
```
+ mob face, wrong head size, distorted body, ambiguous form, black rectangles, one-hour drawing challenge
```
> artist 네거티브(`milkpanda`·`kurukurumagical`·`taroimo`)는 범용 anatomy 아님 → §12.5 그림체
> 스니펫 `negative_extra` 에 귀속.

### 12.8 구현 결과 / 한계 / 후속

- **구현됨**(TDD): conflicts.py `base_lock` 검출(③, base_model 미상 시 스킵) + keyword_registry
  artistmix-nai5-base·rating 4종(axis=등급)·anatomy-stable 보강 + style_presets nai5-aesthetic
  ×2(illustrious 상업 / noobai v-pred 0.7) + server `/api/check_conflicts` base_model·`/api/keywords`
  base_lock 노출. prompt_lab webapp base_model 전달 + index.html 🔒 비호환 회색 표시(비차단)·
  베이스 변경 시 재검사. **gen_gate 198→203·prompt_lab 65→66 passed**.
- **rating 축은 신규 코드 0** — 기존 §11 `same_axis` 룰이 그대로 적용(safe+explicit 자동 경고).
  base_lock 만 신규 type. 모델별 사전 분리 회피(§12.2) = 표식+필터로 충분 실증.
- **검증 한계(정직)**: 검증=**계산적(테스트)**뿐. 실 이미지로 그림체 전이 A/B(illustrious/noobai
  각 베이스 ± artist-mix, 같은 시드)는 **GPU 비점유 시 후속** — 아직 미실증.
- **ANAI5 LoRA**: lora_registry 미등록(실 자산 확보 시). 현재는 artist 태그 가중 믹스만으로 동작.
- **한계**: 사용자 선호 animagine 은 이 그림체 비대상(어휘 비호환) — 명시적 트레이드오프.

## 13. Raw 프롬프트 충돌 분석 — 자유 텍스트 태그 인식 (구현됨 — gen_gate `c3c0c45`·prompt_lab `83eb2ce`, 2026-06-19)

> §11 충돌 검출은 **등록된 키워드(레지스트리 key)** 기준. 사용자가 외부에서 *찾아 붙여넣는* 생(raw) 프롬프트(자유 텍스트 danbooru 태그 + artist 가중 믹스)는 축·rating·base_lock 분석에 안 잡히는 갭. 본 절이 메움. 결정(AskUserQuestion): **계산적 사전 방식**(CLAUDE.md 계산적 우선) + **전 항목 검출**(인원-행위·같은-축 모순·rating 불일치·base_lock·문법 린트).

### 13.1 데이터 — `tag_lexicon.json` (태그 → 제약)
점증 사전(찾을 때마다 등록, rule-of-three 불요 — 발견 즉시 추가):
```jsonc
{
  "rating_order": ["safe","sensitive","questionable","explicit"],
  "tags": {
    "<bare tag>": {
      "axis": "<자세|체위|구도|…>",          // (선택) 같은-축 판정
      "min_people": 2,                          // (선택) 행위 최소 인원
      "implies_rating": "explicit",             // (선택) 내용이 함의하는 수위
      "rating_decl": "sensitive",               // (선택) 이 태그 자체가 레이팅 선언
      "base_lock": ["illustrious-xl-2.0","noobai-xl-vpred"],  // (선택) 어휘 종속(artist 등)
      "contradicts": ["lying","on back"]        // (선택) 명시적 비양립 태그
    }
  }
}
```
- **모르는 태그 = 스킵**(거짓 경고 0 — §11 detect_people 패턴 일관). 커버리지=등록분만.
- artist 태그는 `base_lock`(+의미상 kind=artist)로 표현 → §12 base_lock 재사용.

### 13.2 검출 (`analyze_prompt(text, base_model, lexicon)` — conflicts.py)
1. **토큰화**: §11 paren-aware split 재사용 → 토큰별 가중치/괄호/이스케이프 제거 → bare 태그(lower, `_`→공백).
2. **인원-행위**(min_people): `detect_people(text)` ↔ 인식 태그의 min_people. 인원 신호 없으면 스킵.
3. **같은-축 모순**(contradiction): 인식 태그쌍이 `contradicts` 관계면 hard 경고. (단순 같은-axis 공존은 *보강*일 수 있어 noise → 명시 `contradicts` 쌍만 hard; standing⊥lying 등.)
4. **rating 불일치**: 인식된 `rating_decl` 최대값 < 인식된 `implies_rating` 최대값 → 경고(예: `sensitive` + `rough sex`).
5. **base_lock**: base_model 주어지고 인식 태그가 base_lock 인데 현재 베이스 불포함 → 경고(미상이면 스킵).
6. **문법 린트**(텍스트 직접): 괄호 불균형(이스케이프 `\( \)` 제외 후) · 미분리 그룹 `)( ` · 가중치 [0.1,2.0] 벗어남.
7. 반환 = `[{type, message, ...}]`. type ∈ {min_people, contradiction, rating_mismatch, base_lock, syntax}. 전부 **비차단 경고**(§11 답습).

### 13.3 배선 / UI
- 서버 `/api/check_conflicts` 가 키워드 충돌(§11)에 더해 raw 프롬프트 분석을 **병합** → 프론트 무변경(기존 칩/베이스 디바운스가 그대로 raw 프롬프트 경고도 노출). 베이스 텍스트 붙여넣기 → ⚠️ 자동.
- 사전은 gen_gate 단일 소스(provider-liquidity, styles·keywords 동형).
