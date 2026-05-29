# 3+1 합의 — MVP-2 SC-2 R-1 Hermes 위임 검증 brief — Agent C (대안 탐색가)

> **작성**: 2026-05-28 (66번째 entry cycle — 세션 #3)
> **에이전트**: Agent C (대안 탐색가) — 관점 "더 나은 방법이 있는가?" (대안, 트레이드오프)
> **검토 대상**: `docs/phase0/mvp2-sc2-r1-hermes-delegation-verification-brief.md` (v1, §0~§10)
> **독립성**: Agent A/B·외부 LLM 응답 미참조. 직접 read 한 source = brief v1 + day2-r1 + R-4 (redaction-pattern-equivalence) + ADR-008 + day1 §3 + r2-canary.yml + canary-recheck-design.md + governance §1.2.7/§4.5 + 64 trajectory + 65 SC-1.

---

## 1. 판정

### **APPROVE WITH CONDITIONS**

brief 의 핵심 골격 — R-1 = upstream 위임 검증 (import 0), 4축 종합, 실 격리 canary deferred (day2-r1 선례), over-claim 경계 — 은 **대안 탐색 관점에서 채택할 만한 최선의 trade-off** 다. 채택 정당성:
- "실 격리 canary 즉시 실행" 대안은 artifact 휘발(/tmp) + 환경 의존 + day2-r1 선례 대비 **추가 정보 가치 한계** → deferred 가 비례적.
- "full GP-2 PASS 본 cycle 발효" 대안은 over-claim risk + R-1 ∧ R-2 AND 구조 위반 → SC-3 분리가 정합.

단 **3건의 BLOCKING** (정합성 격차 — 채택 가능하나 *정정 후*) 과 5건 권고를 제시한다. BLOCKING 은 결론(deferred + 위임 검증)을 뒤집지 않고, **evidence contract 의 사실 정확성**과 **R-6 인용 범위**를 바로잡는 것이다. 이 3건은 본 세션 #2 의 4회 over-claim cascade 교훈([[feedback_pass_scope_overclaim]])의 직접 연장선이다.

---

## 2. BLOCKING (정정 필수)

### BLOCKING-1 — R-6 (r2-canary.yml) 은 R-1 의 "자동 회귀 검증"이 *아니다* (축 3 / C-2 인용 범위 격차)

**근거 (직접 read)**: `.github/workflows/r2-canary.yml` 의 `on.push.paths` / `on.pull_request.paths` =
```
docker/r4-1-poc/**, docker/r2-poc/**, docs/architecture/canary-recheck-design.md,
docs/phase0/r4-1-trigger-extension-evidence.md, .github/workflows/r2-canary.yml
```
job 명 = **"R-4.1 Tier-1 42 canary regression"**, 실행 대상 = `docker/r4-1-poc/docker-compose.r4-1-poc.yml`.

즉 R-6 가 자동 회귀로 검증하는 것은 **R-2 trigger UDF (SQLCipher BEFORE INSERT, DB INSERT 차단 = GP-1/Tier-1 catalog 영역)** 다. brief §2.1 가 명확히 분리하듯 R-1 = **Hermes native `agent/redact.py` (로그/송신/도구출력 = GP-2 영역)**. 두 수단은 **다른 코드 · 다른 경로 · 다른 GP**다.

brief §2.3 ("Hermes upstream 변경으로 redaction silent 깨짐 시 자동 검출 경로 ✅") + §3 C-2 ("R-6 자동 재실행 = 답습 유지") 는 R-6 가 **Hermes `agent/redact.py` 의 silent 깨짐을 자동 검출**한다고 인용한다. 그러나:
- r2-canary.yml 의 push paths 에 `agent/redact.py` 또는 Hermes upstream 경로 **없음** (애초에 in-repo 부재 + /tmp 휘발).
- canary-recheck-design.md §3.4 (line 82, 138) 은 `agent/redact.py` diff trigger 를 **"정의"만** 하고 (R-5 = 설계), §11 line 153 "실제 차단 메커니즘은 R-6 작업" — 그런데 R-6 (r2-canary.yml) 에 그 trigger 가 **구현되지 않음** (R-2 poc 경로만).

→ **결론**: R-6 는 R-2 trigger 회귀를 검증하지, **R-1 Hermes native redaction 의 upstream drift 를 자동 검출하지 않는다**. brief 가 R-6 를 R-1 의 축 3 / C-2 로 인용하는 것은 [[feedback_actual_run_trigger_paths_filter]] (paths 필터 미충족 = trigger 0) 위반 패턴이다.

**정정 요구 (택1)**:
- (a) §2.3 / §3 C-2 를 **"R-6 = R-2 trigger 회귀 (DB INSERT/GP-1). R-1 Hermes native redaction 의 upstream drift 자동 검출은 *미구현* — canary-recheck-design.md §3.4 trigger 정의는 있으나 r2-canary.yml paths 에 미반영. R-1 drift 자동 검출 = SC-3 또는 별도 cycle 의 evidence contract 잔여"** 로 정직하게 재기술. (권고)
- (b) 또는 축 3 을 R-1 의 *충족 축*에서 **"잔여 격차"**로 강등 (4축 → 3축 충족 + 1 잔여).

이 정정은 위임 검증 *결론*을 뒤집지 않는다 — R-1 의 위임 신뢰 *지속 보증*이 현재 자동화되어 있지 않다는 사실을 정직하게 명문화할 뿐이다.

### BLOCKING-2 — Hermes upstream URL 은 "ADR-008 확보 선결"이 아니라 day1 §3.1 에 *이미 명시*됨 (C-3 SOP 사실 오류)

**근거 (직접 read)**: brief §3 C-3 step 1 + §4 = "Hermes upstream URL 문서 미명시 → 실 격리 canary 실행 미시행" + "URL = ADR-008 Hermes 도입 출처, 확보 선결".

그러나 `docs/phase0/day1-environment-and-fact-check.md` §3.1 (line 54) =
```
- GitHub: https://github.com/NousResearch/hermes-agent
- v0.12.0 (2026-04-30) "The Curator release"
```
§3.3 (line 100) = `git clone --branch v0.12.0 https://github.com/NousResearch/hermes-agent.git`. R-4 (`redaction-pattern-equivalence.md` line 46/494) = 출처 `/tmp/hermes-phase0/hermes-agent/agent/redact.py v0.12.0 main HEAD 401 LOC`.

→ **URL 은 본 repo 내(day1 §3.1)에 이미 확정 명시**. "ADR-008 확보 선결" 은 사실 오류이며, **deferred 의 진짜 blocker = artifact 휘발(/tmp) 단독**이지 URL 부재가 아니다.

**정정 요구**: §4 + §3 C-3 step 1 을 **"Hermes upstream URL = day1 §3.1 (github.com/NousResearch/hermes-agent, v0.12.0) 확정 명시. deferred 의 단일 blocker = /tmp artifact 휘발 (재clone 시점 SOP 실행 가능)"** 로 정정. URL 이 이미 있으면 deferred 정당화의 "URL 확보 선결" 조건이 사라지므로, deferred 근거가 day2-r1 선례(코드 분석 충분) + 환경 비용 단독으로 좁혀져 **오히려 더 정직**해진다.

### BLOCKING-3 — 격리 canary 재현 자산이 in-repo 에 *부분 존재* (docker/r2-poc/) — "artifact 부재" 단정 과대

**근거 (직접 read)**: `docker/r2-poc/Dockerfile` + `r2_poc.py` (10788 B) + `docker-compose.r2-poc.yml` 이 **in-repo 존재**. `docker/r4-1-poc/` 도 r2-canary.yml 이 참조 (Tier-1 42 canary). 이는 **SQLCipher trigger (R-2) 의 재현 가능 격리 환경**이다.

brief §4 = "agent/redact.py artifact 부재 + Hermes upstream URL 문서 미명시 → 실 격리 canary 실행 미시행" 은 **R-1 (Hermes native) artifact 가 없다**는 점에서는 맞다. 그러나 brief 가 §6.6(질문) "재현 가능 격리 환경 (Docker pin + Hermes 고정 버전 archive)" 을 *미래 과제*로만 두는 것은, **R-2 측 docker 인프라가 이미 재현 패턴을 제공**한다는 사실을 누락한다.

→ R-1 격리 canary 의 *환경 골격*은 `docker/r2-poc/Dockerfile` (python:3.11-slim + pysqlcipher3) 을 **Hermes redaction import 용으로 재사용/포크**하면 즉시 확보 가능 (Hermes `agent/redact.py` 만 추가 + canary 주입). 즉 "재확보 = 처음부터 구축"이 아니라 "기존 docker 골격 + Hermes redact 모듈 + canary".

**정정 요구**: §4 + §6.6 에 **"격리 환경 골격 = `docker/r2-poc/` 재사용 가능 (Dockerfile + canary 주입 패턴). R-1 SOP 실행 = 기존 골격 + Hermes `agent/redact.py` re-clone 만 추가"** 명문. 이는 deferred 를 약화시키지 않고 (실행은 여전히 별도 trigger), **재확보 비용을 정확히 산정** + RT-2 (실 실행 시 day2-r1 불일치 대비) 의 실행 경로를 구체화한다.

---

## 3. 권고 (채택 시 brief 품질 향상)

### REC-1 — C-1 (version pin) 의 절충안 = hermes-version.yaml 즉시 생성을 *deferred* 가 아니라 *SC-3 진입조건*으로 격상 권고

brief §0.2 #6 + §3 C-1 = hermes-version.yaml 파일 생성 = "절충안, 본 cycle 명문만". 이는 비례적(파일 1개 생성도 cycle 분리)이나, **governance §1.2.7 P11 Layer 1 (line 257) 이 이미 "`hermes-version.yaml` v0.12.0 핀" 을 enforcement 로 명문** + P11 차단(line 269) "`hermes-version.yaml` 미명시 = PR auto-reject" 를 규정한다. 즉 **파일 부재 = P11 enforcement 가 가리키는 대상 부재** (governance 명문 vs 실 파일 격차).

→ 권고: 본 cycle 은 contract 명문 유지(채택), 단 **SC-3 (full GP-2 PASS) 진입조건에 "hermes-version.yaml 실 파일 생성" 을 명시적 전제로 등록** (현 brief §5 는 SC-3 자격을 "R-1 ∧ R-2 충족"으로만 기술 — version pin 실파일은 누락). 이유: R-1 위임 신뢰의 *유일한 결정적 anchor* 가 version pin 인데(C-2 R-6 가 BLOCKING-1 로 무력화됨), 이 anchor 가 파일로 존재하지 않으면 위임 검증의 지속성이 명문에만 머문다.

### REC-2 — 누락 검증 축: Hermes 공식 changelog / breaking-change 추적 (5번째 축)

brief 4축(위치/동등성/회귀/권위) 은 **현 시점 스냅샷** 검증이다. 누락 축 = **upstream 변경 추적의 "human-readable" 경로** — Hermes 는 v0.12.0 에서 `redaction.enabled` 를 **default ON → OFF breaking change** (day1 §3 line 20/138 CRITICAL) 한 전례가 있다. redact 동작이 config flag 한 줄로 무력화될 수 있다.

→ 권고: 5번째 축 (또는 RT) = **"Hermes release note / RELEASE_vX.md 의 redaction 관련 breaking change 추적"** 명문. R-6 가 자동(BLOCKING-1 로 미구현) 이면, changelog 추적이 **위임 신뢰의 인간 backstop**. C-3 SOP step 0 = "re-clone 시 RELEASE note 의 redaction default/flag 변경 확인" 추가 권고.

### REC-3 — 대안 검증 방법 NOTE: Hermes test suite 답습 (커뮤니티 audit 보다 우선)

brief 가 검토 질문에 든 "Hermes test suite 답습 / 커뮤니티 audit" 중 — day1 §3.2 line 76 = Hermes 는 `tests/ ~15k 테스트 ~700 파일`. **redact 모듈의 upstream test (`tests/test_redact*.py` 추정)** 가 존재하면, 이를 격리 실행하는 것이 **canary 자작보다 maintainer-authored coverage 답습** 이라는 점에서 더 강한 evidence (자작 canary = 본 repo 가 짐작한 패턴, upstream test = vendor 가 보장하려는 패턴). 단 upstream test 신뢰 = Hermes ≠ root of trust 위반 risk → **canary(self) + upstream test(delegated) 병행이 최선** (둘 다 deferred 가능).
→ 권고: C-3 SOP 에 "step 4.5 = Hermes upstream `tests/` 의 redact 관련 test 격리 실행 (vendor coverage 답습)" 선택지 NOTE. 커뮤니티 audit 은 단일 maintainer(NousResearch) repo 특성상 신뢰 가중 낮음 → 비채택 권고.

### REC-4 — §5 판정 문구에 "축 3 (R-6) 인용 정정 반영" 연동 (BLOCKING-1 cascade)

BLOCKING-1 채택 시 §5 의 "축 1 ✅ + 축 2 ✅ + 축 3 ✅ + 축 4 ✅" → "축 1+2+4 ✅ + 축 3 = R-1 drift 자동검출 잔여(R-6 는 R-2 회귀)" 로 동기화. governance §4.5 (a) "Hermes native redaction Tier-1 42 catalog 적용 검증" 의 충족은 **축 1+2 (위치 + 동등성)** 로 성립하므로, 축 3 강등이 (a) 충족을 깨지 않음을 §5 에 명문.

### REC-5 — SC-2 → SC-3 흡수 대안 NOTE 병기 (scope 대안)

검토 질문 4/5 의 "SC-2 를 SC-3 에 흡수" 대안은 — 본 brief 가 독립 cycle 로 분리한 것이 over-claim 방지(위임 검증 ≠ full PASS 분리)에 유리하므로 **현 분리 채택**. 단 §6 합의 형태(풀 3+1 + 외부 LLM 1+) 가 "문서 종합 + import 0 + 실코드 0" cycle 에 다소 무거울 수 있음 — [[feedback_ceremony_inflation]] 경계. 그러나 본 cycle = full GP-2 PASS R-1 prong (보안 + 큰 결정 + cross-vendor 위임)이므로 §6.2 4/4 trigger 발화는 정당 → **풀 3+1 채택**, 단 §6 에 "본 cycle = 위임 검증 (실코드 0) — ceremony 대비 결정 무게 = R-1 prong milestone 자격으로 정당화" 1줄 명문 권고 (inflation 자가점검 답습).

---

## 4. NOTE (관찰)

- **N-1**: brief §2.1 의 day2-r1 "FAIL = G1a(DB) 맥락, GP-2(송신)는 적용 ✅" 재해석은 day2-r1 원문(§5 "FAIL = LLM 송신/도구 출력 전용") + R-4 (line 48 "DB INSERT 미적용, GP-2 적용") 와 **정합**. 이 맥락 분리는 정확하며 over-claim 아님 (P-2 자가진단 타당).
- **N-2**: brief §2.2 의 "Hermes 47 ⊇ Tier-1 45" 는 R-4 §5.3 (line 272/276) 와 정확히 일치. 단 R-4 line 169 = P-1(sk-) 문자클래스 차이 (Hermes `[A-Za-z0-9_-]` ⊋ P1 `[a-zA-Z0-9]`) — Hermes 가 더 광역이므로 ⊇ 방향 유지, over-claim 아님.
- **N-3**: brief §0.2 #4/§4 의 "실코드 0 + import 0" 는 65 SC-1(R-2 = in-repo operative)과 명확히 구별됨 — R-1 = 위임(검증), R-2 = in-repo(구현). 이 비대칭은 64 trajectory RT-6 (cover 비대칭) 와 정합하며, brief 가 이를 "위임 검증"으로 정직하게 다룸 (over-claim 아님).
- **N-4**: §6 합의 형태 = 작성자=Claude (P-6 자가진단) → cross-vendor codex + 풀 3+1. 본 Agent C 분석은 Claude 계열이나 독립 read 기반 (편향 회피).
- **N-5**: brief §10 P-7 (hermes-version.yaml 파일 부재 = contract 미충족 오인) 자가진단은 타당하나, REC-1 + BLOCKING-1 의 결합 결과 — **version pin 이 R-1 위임의 *유일한 살아있는 anchor*** (R-6 가 R-2 전용이므로) — 라는 점에서 파일 부재의 가중치가 brief 가 평가한 것보다 *높다*. P-7 의 "절충안 별도" 판단은 유지하되 REC-1(SC-3 진입조건 격상)로 보강 권고.

---

## 5. 대안 매트릭스

### 5.1 deferred vs 실 실행 (§4)

| 대안 | 트레이드오프 | 채택 권고 |
|------|------|------|
| **(a) Hermes re-clone 즉시 실행** | evidence 강도 ↑↑ (실 동작 확인) / 환경 비용(/tmp 재clone + Docker) + day2-r1 대비 추가 정보 한계 | **비채택** — 본 cycle. 단 SOP 명문 + RT-2 대비 |
| **(b) deferred (현 brief)** | evidence = 코드/문서 분석 (day2-r1 동형) / 실 동작 미확인 (잔여) | **채택** ⭐ — day2-r1 선례 + 비례성. 단 BLOCKING-2/3 정정 후 (URL 이미 있음 + docker 골격 재사용 명문) |
| **(c) ADR-008 URL 확보 후 docstring 재확인만** | 비용 ↓ / day2-r1 docstring 재확인 = 중복 (가치 0) | **비채택** — day2-r1 §3.2 가 이미 docstring 확정. 게다가 URL 은 ADR-008 아닌 day1 §3.1 (BLOCKING-2) |
| **(d) PyPI hermes 패키지 import 검증** | 표준 의존성 검증 / **day1 §3.3 line 96 = `pip install hermes-agent` → 404 Not Found** (PyPI 부재 확정) | **비채택** (불가능) — PyPI 미배포. git clone 만 가능 |

→ **채택 = (b) deferred**, BLOCKING-2(URL 정정) + BLOCKING-3(docker 골격 재사용) 정정 후. (d) 는 day1 사실로 원천 배제.

### 5.2 evidence contract 형태 (§3)

| 대안 | 트레이드오프 | 채택 권고 |
|------|------|------|
| **version pin 명문 (현 C-1, 파일 부재)** | 비용 0 / 명문만 = 실 anchor 부재 (governance P11 enforcement 대상 부재) | **부분 채택** — 본 cycle 명문 + REC-1 (SC-3 진입조건 격상) |
| **hermes-version.yaml 즉시 생성 (절충안)** | governance §1.2.7 P11 Layer 1 enforcement 충족 / cycle 1개 분리 비용 | **REC-1 권고** — SC-3 진입조건. R-1 위임의 유일 살아있는 anchor |
| **SBOM (cyclonedx 등)** | supply-chain 정합 (P11 (ii)) / 1인 툴 과잉 + governance "별도 합의" 명시 | **비채택** (현 단계) — [[feedback_proportionate_security_personal_tool]] |
| **hash pinning (`--require-hashes`)** | 변조 차단 강(P11 (ii)) / git clone(비-PyPI) 방식과 부정합 (hash = PyPI 전제) | **비채택** — clone 방식엔 commit SHA pin 이 적합 (REC: hermes-version.yaml 에 v0.12.0 + commit SHA 병기) |

→ **채택 = version pin 명문(본 cycle) + hermes-version.yaml 실파일을 SC-3 진입조건 (REC-1)**. commit SHA 병기 권고 (clone 방식 정합).

### 5.3 R-1 위임 검증 방법 (4축 + 누락 축)

| 검증 축 | 강도 | 본 brief | 권고 |
|------|------|------|------|
| 위치 (day2-r1) | 결정적 (코드 분석) | ✅ 축 1 | 채택 |
| 동등성 (R-4 §5) | 강 (패턴 superset) | ✅ 축 2 | 채택 |
| 자동 회귀 (R-6) | **R-2 전용 (R-1 미커버)** | ✅ 축 3 (오인용) | **BLOCKING-1 — 잔여로 강등** |
| 권위 (ADR-011 §2.3 #2) | 위임 근거 | ✅ 축 4 | 채택 |
| **changelog/breaking-change 추적** (누락) | 인간 backstop (default flip 전례) | ❌ | **REC-2 신설** |
| **Hermes upstream test 답습** (누락) | vendor coverage (≠ self canary) | ❌ | **REC-3 NOTE (병행)** |
| 커뮤니티 audit | 약 (단일 maintainer repo) | ❌ | 비채택 |

### 5.4 scope (SC-2 위치)

| 대안 | 트레이드오프 | 채택 권고 |
|------|------|------|
| **SC-2 독립 (문서 종합 위임 검증)** | over-claim 분리 명확 / cycle 다수 | **채택** ⭐ (현 brief) — 위임 검증 ≠ full PASS 분리 |
| SC-2 → SC-3 흡수 | cycle 축소 / R-1 위임 검증과 full PASS 발효 혼재 = over-claim risk | **비채택** — [[feedback_pass_scope_overclaim]] |
| 실 격리 실행을 SC-3 전제조건 | evidence 강도 ↑ / full PASS 가 환경(/tmp)에 hard-block | **부분** — SC-3 진입조건 아닌 *권장* (deferred 유지, REC-1 version pin 우선) |
| R-1 영구 deferred + detection-tier 유지 | 가장 보수 / GP-2 prevention 위임 prong 미충족 (full PASS 영구 불가) | **비채택** — 64 trajectory AND PRIMARY 위반 |

### 5.5 full GP-2 PASS 경로 (R-1 ∧ R-2)

| 대안 | 트레이드오프 | 채택 권고 |
|------|------|------|
| **R-1 위임검증 ∧ R-2 in-repo (AND, 현 brief §5)** | governance §4.5(a) verbatim "+" 정합 / R-1 = 위임(약), R-2 = in-repo(강) 비대칭 | **채택** — 64 trajectory §2.2 AND PRIMARY. 비대칭은 RT-6 명문 |
| R-2 단독 발효 + R-1 milestone 분리 | in-repo prevention 1 확보 / governance "+"(AND) 위반 | **비채택** — Exit (a) 2-pronged verbatim |
| detection-tier 영구 + prevention milestone 분리 | over-claim 0 (가장 안전) / full GP-2 PASS 영구 포기 | **비채택** — trajectory 가 이미 prevention 경로 합의 |

→ **채택 = AND (현 brief)**, 단 BLOCKING-1(R-6 비대칭 정직화) + RT-6(cover 비대칭, 64 trajectory) 명문 연동.

### 5.6 Hermes artifact 재확보 (§6.6 /tmp 휘발)

| 대안 | 트레이드오프 | 채택 권고 |
|------|------|------|
| 처음부터 격리 환경 구축 | 완전성 / 비용 ↑ | **비채택** — docker/r2-poc 골격 존재 (BLOCKING-3) |
| **docker/r2-poc 골격 재사용 + Hermes redact 모듈 추가** | 비용 ↓ (인프라 재사용) / R-2(SQLCipher) vs R-1(redact) 용도 차이 조정 필요 | **채택** ⭐ (REC + BLOCKING-3) — Dockerfile(python:3.11) + canary 주입 패턴 답습 |
| Hermes 고정 버전 archive (commit SHA pin) | 재현성 ↑↑ (휘발 무관) / archive 저장 위치 (1인 툴 비례성) | **권고** — hermes-version.yaml 에 v0.12.0 + commit SHA (REC-1 + 5.2) |

→ **채택 = docker/r2-poc 골격 재사용 + version+SHA pin** (재현 가능 격리 환경 = 기존 자산 + Hermes redact 추가).

---

## 6. 종합

**판정 = APPROVE WITH CONDITIONS**. brief 의 deferred + 위임 검증 + over-claim 경계 골격은 대안 비교상 **최선의 비례적 trade-off** (실 실행 대안 모두 day1 사실 또는 비용으로 열위). 채택 전 **3 BLOCKING** = (1) R-6 는 R-1 아닌 R-2 회귀 검증 — 축 3 / C-2 인용 정정 [[feedback_actual_run_trigger_paths_filter]], (2) Hermes URL 은 ADR-008 아닌 day1 §3.1 이미 명시 — C-3/§4 사실 정정, (3) 격리 골격 docker/r2-poc 부분 존재 — "artifact 부재" 단정 완화. 5 권고 = version pin SC-3 진입조건 격상 / changelog 추적 축 신설 / upstream test 병행 / §5 동기화 / ceremony 자가점검. 모든 BLOCKING 은 결론을 뒤집지 않고 **evidence contract 의 사실 정확성**을 본 세션 #2 over-claim cascade 교훈에 맞춰 정직화하는 것이다.

**대안 탐색 핵심 결론**: 더 나은 방법 = "실 실행 즉시" 가 아니라 **"deferred 유지 + 잔여(R-1 drift 자동검출 미구현)를 정직하게 노출 + version pin 을 R-1 위임의 유일 살아있는 anchor 로 격상"**. R-6 가 R-1 을 자동 보증한다는 *착시*를 제거하는 것이 본 검토의 단일 최대 기여다.

---

**Agent C (대안 탐색가) 분석 끝.**
