# 3+1 합의 — SC-Provider Liquidity (facade Router 위임 real) — Agent C (대안 탐색가)

> **날짜**: 2026-05-28 (69번째 entry cycle — 세션 #4)
> **검토 대상**: `docs/phase0/sc-provider-liquidity-router-delegation-implementation-brief.md` (v1)
> **렌즈**: "더 나은 방법이 있는가?" — 대안 기술 / 트레이드오프 / scope 경계 적절성
> **독립성**: Phase 2 독립 분석. Agent A / Agent B / 외부 codex 결론 미참조. 직접 read 근거(file:line)만.

---

## 판정: **APPROVE WITH CONDITIONS**

brief v1의 핵심 노선(LiteLLM Router 위임 real + Core MVP scope + Router mock 검증 + §17 folding)은 **대안 탐색 관점에서 견고하며, 선택된 대안들이 개인 단일 사용자 자비스 툴의 비례성에 부합**한다. 단 BLOCKING 3건(import-linter 계약 실측 불일치 1건 + manifest 형식 미결정으로 P11 hash 적용 정도 불명 1건 + degraded scope 경계 1건)을 조건부로 해소해야 한다. 나머지는 권고(대안 제시) + NOTE.

---

## BLOCKING (조건부 해소 의무)

### B-1. lazy import 가 import-linter 계약을 통과한다는 주장의 *실측 미검증* — 형식적 근거 불충분
- **위치**: brief §4.1 line 128 ("lazy든 top-level이든 facade 모듈 내 `import litellm`은 AST 그래프에 잡히나 facade 예외 처리 → 계약 PASS") + `.importlinter:24~35`
- **사실**: `.importlinter:31` contract type = `forbidden`, `.importlinter:34~35` `ignore_imports = src.adapters.llm.facade -> *`. 이 ignore 규칙은 **facade 모듈을 *source* 로 하는 import 전부 무시**. lazy import(`import litellm`이 `_build_router()` *함수 본문* 내부)도 grimp AST 그래프상 여전히 `src.adapters.llm.facade -> litellm` 엣지로 잡히므로 ignore 적용 대상이 맞다 — **즉 brief 주장 방향은 옳다**. 그러나 brief는 이를 "잡히나 처리됨"으로 *서술*만 할 뿐, `include_external_packages = True`(`.importlinter:22`)인 미설치 환경에서 lazy import가 실제로 그래프에 *나타나는지*(함수 본문 내 import를 grimp가 정적으로 포착하는지)는 **실증 0**.
- **위험**: grimp는 함수 본문 내 lazy import도 정적으로 포착하지만, brief가 이를 "당연"으로 처리하면 GREEN 단계에서 계약 RED 시 RT-2(hermetic)와 별개의 새 막힘 발생. 또한 만약 grimp가 함수 내부 import를 포착 *못 하면* (버전별 동작 차이) → **litellm import 엣지 자체가 그래프에서 사라져** 오히려 계약이 vacuously PASS → 향후 누군가 facade *외부* 파일에서 lazy import 시 검출 실패 회귀(GP-5 Layer 1 약화).
- **해소 조건**: GREEN 직전 `lint-imports` 를 (a) lazy import 형태 + litellm *미설치* 환경에서 1회 실행 → 계약 PASS 실측 + (b) facade 외부 파일에 의도적 lazy `import litellm` 삽입 → 계약 **FAIL** 실측(negative control). 두 실측을 §8.3 verify E-3 evidence에 첨부. 둘 중 (b)가 FAIL하지 않으면 lazy import 노선은 GP-5 Layer 1을 약화시키므로 **import 전략 재고**(권고 C-2 대안 채택).

### B-2. manifest 형식 미결정 상태에서 P11 hash 적용을 "가능 범위"로 연성화 — supply-chain 기준 우회 가능성
- **위치**: brief §4.2 line 139 ("hash 검증 | `--require-hashes` 또는 hash 매니페스트 (가능 범위)") + line 136 (manifest 형식 = 풀 3+1 권고 미결정) + governance `governance-preconditions.md:268` (P11 감지 기준 (4) "pip install `--require-hashes` 강제 — hash 부재 시 install 차단")
- **사실**: P11 §1.2.7.3 감지 기준 (4)는 `--require-hashes` 를 **강제(차단)** 로 명문화. brief는 "가능 범위"로 연성화 + manifest 형식(`requirements.txt` vs `pyproject.toml [project]`)을 미결정으로 남김. 그런데 **manifest 형식 결정이 hash 적용 가능성을 직접 좌우**한다: `requirements.txt` 는 `--require-hashes` 가 native 지원이나, `pyproject.toml [project] dependencies` 는 (PEP 621) hash 핀을 직접 담지 못해 별도 lock(pip-tools `requirements.lock` / uv.lock / poetry.lock)을 *동반*해야 hash 강제 가능. 즉 형식 미결정 = hash 강제 가능성 미결정.
- **위험**: 비례성을 이유로 hash를 "가능 범위"로 두고 형식까지 미결정이면, 실제 구현 시 hash 0건으로 귀결 → P11 감지 기준 (4) 사실상 미충족 + first runtime dependency(공격면 최대 시점)에 supply-chain gate 공백. [[feedback_proportionate_security_personal_tool]] 의 비례성은 *과잉 ceremony 회피*이지 *gate 생략*이 아님 — P11은 brief 자신이 line 16/53에서 답습 source로 인용한 권위.
- **해소 조건**: (a) manifest 형식을 본 합의에서 *결정* (권고 C-1 참조 — `requirements.txt` runtime 단일 파일 권고), (b) 결정된 형식에서 litellm **및 그 전이 의존성**에 대한 `--require-hashes` 적용을 **Core MVP 의무로 승격**(연성 "가능 범위" → "적용"). 단 litellm은 전이 의존성이 큼(httpx/openai/tiktoken 등 다수) → hash 매니페스트 생성 부담 평가 후, *최소한* litellm 직접 핀의 sha256 + lock diff 회귀 검출(P11 (i)/(v))은 비협상 의무로 고정. transitive hash 전체는 비례성 평가 후 결정 가능하나 *결정 자체*는 본 합의에서 명문화(미결정 금지).

### B-3. degraded 모드 전체 defer = 런타임 강등 무방비 — Min2 fail-fast 의 *시작 시점* 한정이 §6 차단조건 #5 의 핵심을 비움
- **위치**: brief §0.2 #3 line 39 + §5.2 line 171 ("런타임 재검증(R4)은 deferred") + 권위 `llm-providers-design.md:76`(원칙 "Min 2 Always-On (Runtime 재검증) — 시작 + **모든 강등 경로**에서 재검증") + `llm-providers-design.md:737`(차단조건 #5 충족 = "§6.1 시작 시 fail-fast + **§6.2 런타임 재검증 + §6.3 degraded 모드**")
- **사실**: ADR-008 차단조건 #5 + 원본 P1 합의 C-4(`3plus1-consensus-2026-05-04-p1-llm-providers.md:150` "시작 시 1회 검증만으로는 차단조건 #5 충족 불가 — 자동 강등 후 1 active 전락 가능")는 **시작 시점 검증만으로는 #5 미충족**을 만장일치 CRITICAL로 결론지었다. brief는 정확히 그 "시작 시 1회 검증"으로 축소(§5.2 line 171). LiteLLM Router의 기본 fallback/cooldown(brief §6.1 line 179)은 *요청 라우팅*을 우회시키나 **active 카운트 재검증을 수행하지 않음** → 런타임에 provider가 모두 죽어도 facade는 강등 무인지.
- **위험**: 본 cycle은 "Router 위임 real"로 *실제 호출 경로가 처음 살아나는* 시점 → 런타임 강등이 비로소 *발생 가능*해진다. 즉 degraded defer는 "아직 호출이 없어 무해"했던 SC-1과 달리 본 cycle에서 **실효 공백으로 전환**. brief §3 line 118의 "응답 redaction 미부착 = 누출 통로 0(callback deferred)" 논리(통로가 없으니 무해)는 degraded에는 적용 안 됨 — 강등은 *발생*하고 단지 *감지/대응*이 없을 뿐.
- **단, 비례성 반론**: 개인 단일 사용자 + 비핵심 background_jobs 위주(자비스 tmux 워커) 환경에서 degraded "모드"(UI 배너/escalation/30분 timer, §6.3)의 *전체*는 과잉. 핵심은 **모드**가 아니라 **런타임 강등 *감지*+fail-loud** 1점.
- **해소 조건 (택1)**: (a) **최소 degraded 감지만 Core 포함** — `complete()` 의 `AuthenticationError`/`ServiceUnavailableError` 경로에서 active 카운트 재계산 → <2 면 **명시 예외 raise + stderr 경고**(모드 전환/UI/timer 없이 fail-loud만). LOC ~10, 비례성 부합. 또는 (b) **defer 유지하되 brief가 §11/§12에 "런타임 강등 무방비 = 알려진 공백"을 명문화** + §17 재합의에서 차단조건 #5를 "시작 시 fail-fast만 = #5 *부분* 충족(런타임 재검증 deferred)"로 *정직하게 강등 표기*(현 brief §7 line 202는 "R4 재검증(deferred)"로 표기하나, 차단조건 #5 자체를 "충족"으로 오인할 여지 — line 16/52 ADR-008 #5 "Min 2 always-on" 답습 문구와 시작-한정의 간극 명시 의무). **권고: (a) 채택** — 10 LOC로 #5의 본질("always-on")을 시작-한정에서 런타임-감지로 복원.

---

## 권고 (대안 제시 — 비채택 시 근거 명시)

### C-1. manifest 형식 = `requirements.txt`(runtime 단일 파일) 권고 (D4 대안 평가)
- **3 대안 트레이드오프**:
  | 대안 | 장점 | 단점 | 비례성(개인 툴) |
  |------|------|------|----------------|
  | (가) `requirements.txt`(runtime) 신설 | `--require-hashes` native(P11 직결) + `requirements-dev.txt` 와 형식 일관(`requirements-dev.txt:1~9` 이미 핀 컨벤션 확립) + pip 단일 도구 | 두 파일 분리 관리 | ⭐ 최적 — 기존 컨벤션 답습, 신규 도구 0 |
  | (나) `pyproject.toml [project] dependencies` 신설 | 표준 메타데이터 통합 | hash 강제 = 별도 lock 동반 필수(B-2) + `requirements-dev.txt:9` "pyproject 신설 별도 합의(R-RF2)" = *추가 합의 부담* + 신규 빌드 도구 학습 | 과잉(개인 툴에 packaging 메타 불요) |
  | (다) 기존 `requirements-dev.txt` 에 임시 추가 | 파일 0 신설 | **runtime/dev 경계 붕괴** — `requirements-dev.txt:8` "runtime application 의존성 0건" 명시 위반 + dev 설치에 litellm 끌려옴 | ❌ 부적합 |
- **권고**: (가) `requirements.txt`. 근거 = `requirements-dev.txt:9` 가 "pyproject.toml 신설은 *별도 합의*"로 명시적 gate를 둔 반면, `requirements.txt`(runtime) 신설은 그 gate에 걸리지 않고 기존 핀 컨벤션을 그대로 답습. 개인 툴에 PEP 621 packaging 메타는 불요(배포 대상 아님). (나)는 "표준성" 명분이나 hash 강제에 lock 도구를 추가로 끌어들여 [[feedback_proportionate_security_personal_tool]] 의 ceremony 회피와 충돌. **본 권고가 B-2 해소의 전제** (형식 결정 → hash 적용 경로 확정).

### C-2. import 전략 = lazy import 채택에 동의, 단 "주입 우선 + lazy 는 fallback" 명시 (§4.1 대안)
- **3 대안 트레이드오프**:
  | 대안 | hermetic 테스트 | 설계 §4.1 충실성 | 비고 |
  |------|----------------|------------------|------|
  | top-level `import litellm`(설계 §4.1 line 199 예시 그대로) | ❌ 미설치 시 facade import 자체 실패 → 주입 테스트도 실패(brief §4.1 line 126) | ✅ 설계 문구 일치 | RT-2 위험 직결 |
  | lazy import + Router 주입 (brief 권고) | ✅ 주입 시 litellm import 0 | △ "위치만 함수 내부"(brief line 129) — facade-한정 의무는 충족 | B-1 실측 의무 |
  | 순수 DI(router factory 외부 주입, facade는 litellm 무지) | ✅ 완전 hermetic | ❌ facade가 Router 구성 책임 상실 → "facade 한 파일만 litellm import"(ADR-009 §2.2 #1 `ADR-009:70`) 위반 — 외부 factory가 litellm import |
- **권고**: brief의 **lazy import + Router 주입 채택에 동의**. 순수 DI는 ADR-009 §2.2 #1("litellm import = facade 한 파일 한정")을 *외부 factory로 누출*시켜 Provider Liquidity Layer 1 모법(ADR-009 §5 `ADR-009:172`)을 깬다 → 기각. 단 brief가 §4.1 line 127에서 `router=None`이면 facade 내부 `_build_router()`가 litellm import하도록 설계 → **litellm import 책임이 facade 내부에 유지됨을 §10 line 256에 이미 명문화(확인 `brief line 256` "lazy import도 facade 내부")** → 정합. **조건**: 설계 §4.1 top-level 예시(`llm-providers-design.md:199`)와의 deviation을 §17 재합의에서 "facade-한정 import 의무 충족, 위치만 함수 내부"로 정정 명문화(brief line 129 이미 인지 — 이행 확인). + B-1 실측 의무 결합.

### C-3. sync vs async (D1) — async 전환 채택에 동의, 단 자비스 호출 패턴 적합성 근거 보강
- **사실**: brief D1 line 73 = async 전환 권고(실 caller 0 실측 — 본인 독립 확인: `grep ".complete(" src/` → **0건**, `LLMRequest` src 사용 = facade.py 자기 정의만(`facade.py:25/44/53`), test caller 1건(`test_redaction_filter.py:105` `LLMRequest(alias=...)`)). breaking 위험 = test 1건 갱신 trivial → 사실 확인.
- **대안 평가 (자비스 tmux 워커 패턴 적합성)**: [[project_jarvis_local_boss_direction]] = 로컬 LLM 사장 + CLI tmux 워커. 이 패턴에서 facade caller는 **다수 워커의 LLM 호출을 동시 fan-out** 할 개연성 높음(병렬 합의 A/B/C 호출 = `llm-providers-design.md:96~98` consensus_agent_a/b/c). → **async(`acompletion`)가 동시 IO에 적합** (sync `Router.completion` 은 caller가 thread/process로 동시성 자체 구현해야 함). 따라서 async가 자비스 패턴에 *더* 적합 — brief 권고 지지.
- **대안 (sync 유지 + 추후 async 추가)**: caller 0인 *지금*이 async 전환 비용 최소 시점. 추후 sync→async 전환은 caller 누적 후 breaking 폭증 → "지금 sync, 나중 async"는 매몰비용. **기각.** 단 brief가 health()는 이미 async(`facade.py:62`)이나 complete()만 sync인 *혼재*를 async로 통일하는 것이므로 일관성 ↑.
- **권고**: async 채택 + brief §2 D1에 "자비스 워커 fan-out 동시성 적합 + caller 0 시점 전환 비용 최소"를 근거로 1줄 보강.

### C-4. 검증 범위 — Router mock 채택에 동의(사용자 결정 존중), 단 ollama smoke 1건을 *선택적 evidence*로 격상 권고
- **사실**: brief §0 line 7 = Router mock만(CI 안정성), 실 호출 수동/별도. E-7 line 290 = "(선택) 실 litellm 설치 + import smoke (네트워크 가용 시)".
- **트레이드오프**: mock만으로는 (a) `to_router_config` 가 생성한 model_list를 **실 litellm.Router가 수용하는지**(스키마 정합) + (b) `_normalize`의 `raw.choices[0].message.content` 추출이 **실 LiteLLM 응답 객체 형태와 일치하는지**(brief는 dict 가정 line 193 vs litellm는 pydantic 객체 반환 가능성) 미입증. 즉 mock의 "raw" 형태를 *우리가 가정한 대로* 만들면 _normalize는 항상 통과 → **자기충족 위험**(mock이 SUT의 가정을 그대로 반영).
- **Provider Liquidity "실 동작" 입증 관점**: 5조-2 비협상은 "교체가 *코드 경로상* 실동작"(brief line 14)인데, mock만이면 **litellm.Router 인터페이스 정합은 미검증** → "코드 경로 operative"의 입증 강도가 mock 가정에 의존.
- **권고**: mock 검증을 Core로 유지(사용자 결정 + CI 안정성 정당)하되, **로컬 ollama가 가용한 경우 1건 smoke(`to_router_config` → 실 `litellm.Router` 구성 + ollama 호출 1회 → `_normalize` 실 응답 처리)를 E-7의 *권장* evidence로 격상**(현 "(선택)" → "ollama 가용 시 권장"). ollama는 `endpoint: http://localhost:11434`(`llm-providers-design.md:149`) credential 불요 → 네트워크/키 부담 없이 *실 LiteLLM 객체 형태* 1점 입증 가능 → mock 자기충족 위험 완화. 비채택 시(ollama 미설치) brief §13에 "litellm.Router 인터페이스 정합 = 실 호출 시점까지 미입증"을 알려진 공백으로 명문화.

### C-5. _normalize 가 litellm 응답을 dict 로 가정(line 193)하는 형태 위험 (D3 대안)
- **위치**: brief §6.3 line 193 `content = raw.choices[0].message.content` (속성 접근) vs line 85 `raw["choices"][0]["message"]["content"]` (dict 접근) — **brief 내부 표기 불일치**.
- **사실**: litellm `completion`/`acompletion` 은 `ModelResponse`(pydantic, 속성 접근) 반환이 표준이나 dict-like 접근도 지원. brief가 두 표기를 혼용 → mock 작성 시 어느 형태를 모사할지 불명 → C-4 자기충족 위험 가중.
- **권고**: §17 재합의에서 _normalize 입력 계약을 **속성 접근(`raw.choices[0].message.content`)으로 단일화** + mock fake Router가 *동일 속성 인터페이스*를 노출하도록 명문화(dict mock 금지 — 실 litellm 형태 모사). 표기 통일.

### C-6. §17 folding(겸함) 채택에 동의 (별도 선행 재합의 대안 대비 SDD 견고성)
- **트레이드오프**: (가) 별도 선행 재합의(설계 §17 먼저 확정 후 구현 brief) vs (나) 본 합의 겸함(brief 권고).
- **평가**: 설계 §17(`llm-providers-design.md:793~827`)의 검증 항목 다수가 **본 cycle 구현 결정과 동일 대상**(LLMRequest 필드 §17 Agent A line 798 = brief D2 / LLMMetadata 화이트리스트 §17 Agent B line 806 = brief D3 / LiteLLM facade 승격 §17 Agent C line 815 = 본 cycle 전제). → 별도 재합의는 **동일 항목 2회 검토**(중복 ceremony) + deferred 항목(streaming/OAuth)을 *구현 없이* 재합의하면 추상 논의에 그침. 본 cycle 구현 결정과 함께 검토해야 §17 항목이 *구체적 코드 결정으로* 검증됨. → **겸함이 SDD상 더 견고**(문서-코드 동시 정합). 단 brief §7 line 206 지적대로 **설계 §15 로드맵(`llm-providers-design.md:773` "12 보강 모두") ↔ Core MVP 분할 간극**은 Reviewer 판단 대상 — 본 Agent C 견해: 설계 §15 MVP row를 "Core MVP(complete 경로) + 12 보강 단계화"로 *갱신 권고*(현 "12 보강 모두"는 본 cycle이 5종 defer하므로 문구-구현 불일치 잔존).
- **권고**: 겸함 채택 + 설계 §15 MVP row 문구를 단계화로 갱신(§17 통과 시 status flip과 함께).

### C-7. LiteLLM 노선 재확인 — 자체 Adapter v2.0 트리거 미충족 (ADR-009 §3)
- **사실 확인**: ADR-009 §3.1 T1~T4(`ADR-009:120~138`) 트리거 독립 점검:
  - T1(신규 provider 6개월 미지원 + PR 거부): 본 cycle은 anthropic/ollama(litellm 표준 지원) → **미충족**.
  - T2(Apache 2.0 → 비호환 라이센스 전환): brief §4.2 line 138이 라이센스 재확인 의무화 → 전환 사실 없음 → **미충족**.
  - T3(2분기 미해결 보안 CVE/차단 버그/정규화 결함): 해당 없음 → **미충족**.
  - T4(4분기 연속 유지부담 역전): 측정 데이터 0 → **미충족**.
- **결론**: 4 트리거 전원 미충족 → ADR-009 §3.2(`ADR-009:140`) 자동 NO-GO → **LiteLLM 유지가 맞음**. 본 cycle은 ADR-009 §2(MVP 운영) 영역, §3(v2.0) 무관. **NOTE 수준 확인 — BLOCKING 아님.** brief가 자체 Adapter를 일절 언급 안 함 = 정합(v2.0 트리거 미발화 시 LiteLLM 답습이 default 노선, `ADR-009:114`).

---

## NOTE

- **N-1 (over-claim 차단 적정)**: brief §0 line 10 + §14 P-1~P-3은 [[feedback_pass_scope_overclaim]] 의 detection≠prevention / 코드경로≠5-way완결 패턴을 정확히 답습. "full facade real"/"Provider Liquidity 완전 발효" 금지 명문화 적정. **단 B-3 해소 (a) 채택 시에도 "런타임 재검증 *완전*" 표현 금지** — degraded 감지만 추가일 뿐 §6.2/6.3 전체 아님. 명칭 정직성 유지.
- **N-2 (registry 위치 미결정)**: brief §8.2 line 228 = "`llm-providers.yaml`(신규, repo 루트 또는 `config/`)". 독립 확인: `config/` 디렉토리 부재 + 루트 yaml 0건. 개인 툴 비례성 + `requirements.txt`(C-1) 도 루트이므로 **루트 직접 배치 권고**(`config/` 신설 = 디렉토리 1개 추가 ceremony, 단일 yaml에 불요). NOTE 수준.
- **N-3 (LLMRequest.alias rename 영향 실측 일치)**: brief D2 line 80 + RT-3 line 275의 실측("src caller 0, test 1건 `test_redaction_filter.py:105`")을 독립 재확인 — 정확. 추가로 **PoC fixture `tests/fixtures/provider_adapter_enforcement/pass/facade_only.py:21` 도 `alias` 사용**하나 brief line 80이 "import-linter PoC 독립 fixture(실 facade 무관, 영향 0)"로 정확히 격리 — 정합. rename 시 fixture는 *갱신 불요*(독립 모사체) 확인.
- **N-4 (D8 health dry probe 축소 fallback 적정)**: brief D8 line 108 + RT-6 line 278 = litellm Router health API 실형태 불명 시 "active 목록 + 설정검증 반환"으로 축소. 개인 툴 + 실 호출 deferred 맥락에서 dry probe 실배선보다 축소 fallback이 비례적 — 적정. 단 §17 Agent B 항목(dry probe, `llm-providers-design.md:812`)을 "구현 deferred, 설계 명세 존속"으로 표기 의무(현 brief §7 line 202 미언급 — health dry probe는 Agent A line 801 health 모순 해소에 묶임).
- **N-5 (응답 redaction defer 논리 타당)**: brief §3 line 118 "응답이 로그/메트릭에 기록되는 경로 0(callback deferred) → 응답 redaction 미부착 = 누출 통로 0" — DomainMetricsCallback(§8.1 deferred)이 유일 sink이고 그것이 defer되므로 응답이 *persist되는 경로 0* = 논리 타당. 단 응답이 caller에게 반환되어 *caller가* 로그하면 누출 가능 → 그러나 그건 facade scope 밖(caller 책임) → defer 정당. NOTE.

---

## Scope 경계 독립 판단 (Agent C)

| # | DEFER 항목 (brief §0.2) | Agent C 독립 판정 | 근거 |
|---|------------------------|-------------------|------|
| 1 | streaming(`stream`/StreamEvent) | ✅ defer 적정 | caller 0 + 자비스 background_jobs는 비스트리밍 우선. 설계 §16 line 788 "streaming 사용 사례 발생 시" 답습 |
| 2 | OAuth single-flight | ✅ defer 적정 | brief는 api_key 경로만 + ollama(none). OAuth = 비용절감 보조(설계 §7.1 line 446). standby 스키마만 등록 = 정합 |
| 3 | degraded 모드 + R4 런타임 재검증 | ⚠️ **부분 재고 (B-3)** | 모드/UI/timer = defer 적정(과잉). 단 **런타임 강등 감지+fail-loud 최소 1점은 Core 포함 권고** — 차단조건 #5 "always-on" 본질 |
| 4 | DomainMetricsCallback | ✅ defer 적정 | sink defer → 응답 redaction 통로 0(N-5). 비례성 부합 |
| 5 | 폴백 race 5종 완화 | ✅ defer 적정 | LiteLLM Router 기본 fallback만 = 개인 툴 충분. race 완화는 다중 동시 부하 시점(자비스 단일 사용자엔 원거리) |
| 6 | 실 LLM end-to-end | ⚠️ **부분 재고 (C-4)** | mock Core 유지 적정. 단 ollama smoke 1건 = credential 불요 → 권장 evidence 격상(mock 자기충족 완화) |

**종합 scope 판단**: 6 DEFER 중 4건(streaming/OAuth/metrics/race)은 **defer 경계 적정** — 개인 단일 사용자 자비스 툴 비례성에 부합(과잉 defer도, 과소 defer도 아님). 2건(degraded #3 / 실 호출 #6)은 **경계 미세 조정 권고**(전체 defer는 과함 — 각각 10 LOC / ollama 1건의 최소 코어 포함이 차단조건 #5 + 실동작 입증에 필요). **scope 자체는 over-defer 아님** — brief의 "Core MVP = complete 경로 한정" 분할은 첫 runtime dependency 도입 cycle로서 적절한 작은 단위. over-claim 차단(N-1)도 견고.

---

## 합의 입력 요약 (Reviewer 용)

- **판정**: APPROVE WITH CONDITIONS
- **BLOCKING 3**: B-1(lazy import 계약 PASS 실측+negative control 의무 / `.importlinter:34` + brief §4.1 line 128) / B-2(manifest 형식 결정 + P11 `--require-hashes` 최소 직접핀 hash 의무 승격 / brief §4.2 line 139 + `governance:268`) / B-3(런타임 강등 감지 최소 Core 포함 — 차단조건 #5 always-on / brief §5.2 line 171 + `llm-providers-design.md:737`)
- **권고 7**: C-1(manifest=`requirements.txt` runtime) / C-2(lazy import+주입 동의, 순수 DI 기각) / C-3(async 동의, 자비스 fan-out 근거) / C-4(mock 유지+ollama smoke evidence 격상) / C-5(_normalize 속성접근 단일화) / C-6(§17 folding 동의+설계§15 갱신) / C-7(LiteLLM 유지 — v2.0 트리거 4/4 미충족)
- **NOTE 5** + scope 독립 판정(4 defer 적정 / 2 미세조정)
- **주요 대안 제안**: ① manifest = `requirements.txt`(pyproject 기각, 기존 컨벤션+hash native) ② import = lazy+주입(순수 DI 기각, ADR-009 §2.2 #1 누출) ③ degraded 전체 defer 대신 *감지 10 LOC* 코어 포함 ④ mock에 ollama smoke 1건 격상(자기충족 완화)
