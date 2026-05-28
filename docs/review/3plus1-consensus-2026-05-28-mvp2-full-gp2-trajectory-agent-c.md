# 3+1 합의 — Agent C (대안 탐색가) 독립 분석

> **대상**: `docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md` (v1)
> **관점**: "더 나은 방법이 있는가?" (대안 기술, 트레이드오프)
> **작성**: 2026-05-28 (64번째 entry cycle — full GP-2 PASS trajectory 진입)
> **독립성**: Agent A/B 및 외부 LLM 응답 미참조 (편향 방지). 직접 read 한 source = brief v1 + governance §4.5/§4.1/§4.3 + ADR-011 §2.1/§2.3 + ADR-009 §2.3/§5 + `facade.py` + `llm-providers-design.md` §8.2 + `secret_scanner.py`.
> **scope 인지**: 본 cycle = trajectory **진입 자격 audit + 경로 분석 + 합의 형태 권고** 한정. 실 결정/구현/발효 0건. 본 분석도 sub-cycle 결정을 *대체하지 않음* (대안 식별 + 트레이드오프만).

---

## 1. 판정

**APPROVE WITH CONDITIONS**

brief v1 의 trajectory 진입 자격 audit 와 경로 분석은 권위 답습이 정확하고 scope 절제 (실 결정/구현/발효 0건) 도 일관된다. 대안 탐색가 관점에서 **brief 가 제시한 후보 (R-1-a/b, R-2-a/b, SC 순서) 가 *유일한 후보가 아님*** 을 식별하였다 — 특히 R-2 경로에서 brief 가 누락한 더 가벼운 대안 (기존 `secret_scanner.py` 로직 재사용 + LiteLLM callback hook) 이 실재하며, full GP-2 PASS scope 의 AND 해석 (Exit (a) = R-1 ∧ R-2) 이 governance 본문상 *유일 해석이 아닐 수 있는* 텍스트 근거가 있다. 이들은 **trajectory 진입을 막는 BLOCKING 이 아니라, sub-cycle 입력으로 명시 등재해야 할 누락** 이므로 조건부 승인한다.

---

## 2. BLOCKING (발효 전 정정 필수)

### BLOCKING-C1 — R-2 경로 후보 enumeration 불완전 (대안 2종 누락)

brief §4.4 는 R-2 후보를 **(R-2-a) 동시 / (R-2-b) 분리** 2종으로만 제시한다. 그러나 본 repo 에 *이미 존재하는* 구현 자산을 직접 read 한 결과, 최소 2종의 추가 대안이 실재하며 이들은 (R-2-a/b) 보다 가볍거나 재사용성이 높다:

- **(R-2-c) `secret_scanner.py` Tier-1 45-pattern 로직 재사용**: `tools/secret_scanner.py` 는 이미 R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 를 보유하고, `scan-log` mode + `is_redaction_marker_match()` (FP 회피) 까지 구현되어 있다 (line 45~258). RedactionFilter 를 *신규 작성* 하는 대신 이 패턴 catalog + 매칭 로직을 *공유 모듈* 로 추출하여 facade redaction 과 scan-log detection 이 *동일 source-of-truth* 를 쓰게 하는 대안. → catalog drift (detection 과 prevention 의 패턴 불일치) 를 구조적으로 차단. brief 는 이 자산을 §12 "실 자료" 로 인용만 하고 *재사용 대안* 으로 평가하지 않았다.
- **(R-2-d) LiteLLM callback hook 활용**: `llm-providers-design.md` §8.1 (line 492~496) 은 `litellm.success_callback` / `litellm.failure_callback` 에 `DomainMetricsCallback(redactor=...)` 를 등록하는 경로를 *이미 설계* 했고, §8.2 (line 521) 는 `RedactionFilter` class 를 *이미 명세* 했다. 즉 RedactionFilter 부착 지점이 (i) facade `complete()` 본문 직접 vs (ii) LiteLLM callback 시스템 두 가지로 갈린다. 이는 R-2 의 *부착 위치* 트레이드오프 (Provider Liquidity 영향 차이 — callback 은 LiteLLM-specific, facade 본문은 provider-agnostic) 를 좌우하는 핵심 변수인데 brief 에 미등장.

**근거**: brief §13 P-4 가 "prevention over-claim 주의" 를 자기진단으로 두면서, 정작 *prevention 수단 후보 enumeration 자체의 완전성* 은 audit 하지 않았다. 대안 탐색가의 핵심 책무 = 후보 공간 완전성. (R-2-c)(R-2-d) 누락은 sub-cycle SC-1 에서 "facade 본문에 신규 filter 작성" 으로 *기정사실화* 될 위험. → §4.4 후보 표에 (R-2-c)(R-2-d) 추가 + 각 트레이드오프 1행 등재 의무.

### BLOCKING-C2 — full GP-2 PASS scope 의 AND 해석이 *유일 해석으로 단정* (대안 해석 미평가)

brief §5.1 / §7 (C-3) 은 **full GP-2 PASS = R-1 ∧ R-2 (AND)** 를 *확정* 으로 서술한다 ("한쪽만 = full GP-2 PASS 미충족"). 그러나 governance §4.5 (a) 본문 직접 read 결과, 이 AND 해석이 *유일하지 않을* 텍스트 근거가 존재한다:

- governance §4.1 (line 422) + §4.5 (a) (line 451) 은 "native redaction `agent/redact.py` **+** P1 facade redaction filter" 로 "+" 를 쓴다. 동시에 §4.1 (line 424) 은 **"GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할"** + **"GP-2 단독으로 헌법 8조 본질 충족 시도 금지"** 라고 명시. 즉 GP-2 전체가 *보조 layer* 로 규정되어 있고, 핵심 prevention (DB INSERT) 은 GP-1 책임이다.
- ADR-011 §2.3 #2 (line 113) 는 R-1 (Hermes native) 을 **"로그/LLM 송신 방어로만 신뢰"** 로 *이미 위임* 했다. 즉 R-1 은 본 repo 가 *검증* 할 대상이지 *발효 게이트* 가 아닐 수 있다 — 위임된 신뢰의 "검증" 이 full GP-2 PASS 의 *발효 조건* 인지, 아니면 *지속 회귀 조건* (R-6) 인지가 §4.5 텍스트만으로 모호.

따라서 **(대안 해석 ②) full GP-2 PASS = R-2 (facade filter, 본 repo 영역) 발효 + R-1 위임 신뢰 (이미 ADR 권위, 검증은 R-6 회귀로 지속)** 라는 읽기가 governance 본문과 정합 가능하다. brief 가 AND 해석을 *확정* 으로 쓴 것은 trajectory 의 발효 문턱을 (대안 해석보다) *높게 고정* 하는 결정인데, 이는 §0.2 가 금지한 "scope 결정" 에 근접한다.

**근거**: AND 해석은 본 cycle 에서 *결정될 사안이 아니라 SC-3 발효 합의에서 결정될 사안*. brief §0.2 #1 이 "full GP-2 PASS 발효 0" 을 선언했으므로, *발효 조건의 논리 구조 (AND vs R-2-단독+R-1-위임)* 도 본 cycle 에서 확정해선 안 된다. → §5.1 / (C-3) 을 "AND 해석 = brief 권고안, 대안 해석 ② (R-2 발효 + R-1 위임 회귀) 존재, *발효 조건 논리 구조 확정 = SC-3 영역*" 으로 완화 의무.

---

## 3. 권고 (BLOCKING 아님)

### 권고-C3 — R-1 경로에 (R-1-c) 격리 검증 전용 대안 명시 등재

brief §3.3 은 R-1 후보를 **(R-1-a) 위임 검증 한정 / (R-1-b) import 통합** 2종으로 제시한다. 사용자 질문의 "Hermes redaction 을 본 repo CI 에서 격리 검증만 (import 0)" 은 (R-1-a) 와 *유사하나 구별* 된다:

- (R-1-a) = "import 0 + ADR 위임 유지 + 적용 검증 evidence + R-6 회귀" → 본 repo runtime 0, *검증은 1회 evidence + 지속 회귀*.
- (R-1-c) [추가 제안] = "import 0 + **CI 격리 환경에서 `agent/redact.py` 를 외부 프로세스로 실행하여 Tier-1 42 적용을 black-box 검증**" — 본 repo 는 Hermes 코드를 *의존성으로 끌어오지 않고* `/tmp/hermes-phase0/.../agent/redact.py` 를 격리 subprocess 로 호출, 입력 canary → 출력 redacted 여부만 확인. R-2 PoC (`docker/r2-poc/`) 의 black-box 패턴 답습.

(R-1-c) 는 (R-1-a) 의 "적용 검증 evidence" 를 *어떻게* 만들지의 구체 수단이다. Hermes ≠ root of trust (ADR-011 §2.3) 와 가장 정합 (Hermes 출력을 Tools 로 외부 검증). → 사실상 ⭐ 채택 권고 방향. brief 의 (R-1-a) 권고를 보강하므로 BLOCKING 아님.

### 권고-C4 — sub-cycle 순서에 "병렬" 및 "scope 축소" 대안 명시

brief §5.2 는 SC-1(R-2)→SC-2(R-1)→SC-3 순차를 권고한다. 사용자 질문의 역순/병렬/scope 축소 대안을 §5.2 에 트레이드오프 표로 등재 권고:

- **순차 (brief 권고)**: R-2 = 본 repo 영역 + (d) carry-over 흡수 → 즉시 가치. 단점 = SC-3 까지 직렬, 총 lead time 길다.
- **병렬 (SC-1 ∥ SC-2)**: R-1 ⊥ R-2 독립 (brief §5.1 명시) 이므로 병렬 가능. R-1 = 검증 evidence 중심 (코드 0), R-2 = 실 코드 → 작업 성격이 달라 충돌 적음. 단점 = 합의 ceremony 2회 동시 → 인지 부하. solo 개인 툴 ([[feedback_proportionate_security_personal_tool]]) 맥락에서 병렬은 오히려 context-switching 비용.
- **scope 축소 (detection-tier 영구 유지 + prevention 별도 milestone)**: full GP-2 PASS 를 *추구하지 않고* 60 detection-layer PASS 를 *영구 종착* 으로 두는 대안. R-1 은 ADR-011 §2.3 #2 위임으로 *이미* 처리, R-2 facade real 은 (d) carry-over 로 *어차피* 진행 → "full GP-2 PASS" 명칭 자체가 *불필요한 milestone 인플레이션* 일 가능성 ([[feedback_ceremony_inflation]]). → §5 NOTE-C3 참조.

⭐ 본 대안 탐색가 권고 = **순차 유지** (병렬은 solo 맥락 인지 부하, scope 축소는 §4.5 (a) 권위가 명시 요구하므로 폐기 불가). 단 세 대안 *명시 등재* 의무.

### 권고-C5 — (R-2-a) 동시 권고의 RT-1 근거 강화

brief §4.4 (R-2-a) 동시 권고 + §8 RT-1 ("facade real 후 RedactionFilter 미부착 window") 는 정합한다. 단 (R-2-c)(R-2-d) (BLOCKING-C1) 채택 시 이 window 가 *달라진다*:

- (R-2-d) callback hook 채택 시: facade `complete()` 가 real 이 되어도 callback 미등록 시 redaction 0 → window 동일하거나 *악화* (callback 등록 누락이 silent).
- (R-2-c) 공유 모듈 채택 시: filter 가 catalog 모듈 import 만으로 동작 → window 최소.

→ RT-1 대응을 "(R-2-a) 동시 구현" 에서 "**redaction 부착이 facade real 의 *전제조건* 임을 test 로 강제** (RED: redaction 미부착 시 `complete()` 가 raise)" 로 일반화 권고. 부착 위치 (본문/callback) 와 무관하게 window 0 보장.

---

## 4. NOTE (관찰)

### NOTE-C1 — brief 의 scope 절제는 모범적

brief §0.2 (13 금지) + §13 (8 자기진단) 은 detection≠prevention, in-repo≠upstream, 권고≠결정 분리를 일관 유지. 특히 P-4 (prevention over-claim, 세션 #2 4회 cascade 교훈 [[feedback_pass_scope_overclaim]]) 자기진단은 적절. 본 BLOCKING-C1/C2 는 *scope 위반* 이 아니라 *후보/해석 공간 완전성* 지적 — brief 가 절제한 결과 후보를 좁게 잡은 부작용.

### NOTE-C2 — Provider Liquidity 대안 아키텍처는 brief 와 정합

사용자 질문 6 (ADR-009 §2.3 참조 redaction 대안 아키텍처) 직접 read 결과: ADR-009 §5 Provider Liquidity 5-way Defense 의 **Layer 1 (코드 lock-in 차단)** 이 이미 redaction 을 facade 책임으로 명시 (§2.3 표 line 87 "비용/관측성/Redaction → ✅ Tier-1 42 catalog 강제"). 즉 *redaction 을 facade 단일 진입점에 두는 것 자체가 Provider Liquidity 와 정합* (provider 교체 시 redaction 도 자동 승계). 이는 (R-2-d) callback hook 대안의 *약점* 을 부각 — LiteLLM callback 은 LiteLLM-specific 이므로, v2.0 자체 Adapter 전환 시 (ADR-009 §3 T1~T4) redaction 이 *함께 이동하지 않는* 위험. → 부착 위치 결정 시 facade *본문* 우위 (NOTE 로만, SC-1 결정 영역).

### NOTE-C3 — "full GP-2 PASS" 명칭이 milestone 인플레이션인지 self-check 권고

권고-C4 의 scope 축소 대안을 폐기하는 근거는 "governance §4.5 (a) 가 명시 요구" 이다. 그러나 §4.5 는 *Design/Governance Gate PASS* 시점 (2026-05-09) 의 Exit *정의* 이고, 실제 발효 의무 여부는 MVP 단계화 ([[project_mvp_staged_roadmap]]) 와 비례성 ([[feedback_proportionate_security_personal_tool]]) 재평가 대상. brief 가 "MVP-2 잔여 trajectory" 로 framing 한 것은 62 PASS 답습이나, *MVP-2 가 full GP-2 PASS 를 정말 요구하는지* (detection-tier 로 MVP-2 가 이미 PASS 발효된 점 고려) 는 SC-3 진입 전 1회 self-check 권고. ceremony-inflation 회피 차원 NOTE.

### NOTE-C4 — 합의 형태는 적절, 단 trajectory entry 자체는 단축 후보

사용자 질문 5 (합의 형태 ceremony 관점): brief §6 의 풀 3+1 + 외부 LLM 1+ 정당화 (trigger 3/7 발화 — 큰 결정 + cross-vendor + Provider Liquidity) 는 타당. 단 **trajectory *진입* 합의 (본 cycle) 와 SC-1 의 TR-1 발화 (facade real 코드) 는 별개 trigger** 임을 관찰: TR-1 (facade real) 이 *어차피* SC-1 에서 풀 3+1 을 강제하므로, 본 trajectory entry 는 *논리적으로* 단축 가능 (진입 자격 audit = 권위 답습 + 경로 분석, 신규 권위 결정 0). 그러나 brief 가 풀 3+1 을 택한 것은 51/52/55 entry 답습 동형 + Provider Liquidity 직결이므로 *기각하지 않음* — over-engineering 이 아니라 답습 일관성. 단 향후 동형 trajectory entry 의 *단축 적격성* 을 메모리 패턴으로 검토 가치 (NOTE 로만).

---

## 5. 대안 매트릭스

### 5.1 R-1 경로 대안

| 후보 | 내용 | 트레이드오프 | 채택 권고 |
|------|------|------------|----------|
| (R-1-a) 위임 검증 한정 (brief) | import 0 + ADR 위임 유지 + 적용 evidence + R-6 회귀 | runtime code 최소, Hermes ≠ root of trust 정합. evidence *수단* 미명시 | ⭐ 유지 (권고-C3 으로 보강) |
| (R-1-b) import 통합 (brief) | Hermes runtime redaction 을 본 repo 의존성 통합 | Provider Liquidity / Hermes PMO 경계 영향. 본 repo = DESIGN repo 와 충돌 | 비채택 (Hermes PMO 활성화 시점 별도) |
| **(R-1-c) 격리 black-box 검증** [C 신규] | `agent/redact.py` 를 격리 subprocess 로 실행, canary in → redacted out 검증 (import 0) | (R-1-a) 의 evidence *수단* 구체화. R-2 PoC black-box 패턴 답습. Hermes ≠ root of trust 최정합 | ⭐ (R-1-a) 의 구현 수단으로 권고 (권고-C3) |
| (R-1-d) upstream PR 기여 | Hermes `agent/redact.py` 본문 개선 PR | upstream 영역 (brief §0.2 #4 scope 외). 본 repo 통제 불가 | 비채택 (scope 외, 영구) |
| (R-1-e) runtime wrapper | 본 repo 가 Hermes redaction 을 wrapping 하는 runtime layer | (R-1-b) 변형. wrapper 자체가 신규 root of trust 후보 → ADR-011 §2.3 위반 위험 | 비채택 |

### 5.2 R-2 경로 대안

| 후보 | 내용 | 트레이드오프 | 채택 권고 |
|------|------|------------|----------|
| (R-2-a) facade real + filter 동시 (brief) | facade 본문 + RedactionFilter 통합 | window 0 (RT-1 대응). 단 filter 를 신규 작성 가정 | ⭐ 방향 (단 부착 위치 미결) |
| (R-2-b) facade real 먼저 / filter 후속 (brief) | 2 sub-cycle 분리 | facade real 후 redaction 미부착 window (RT-1) | 비채택 (window 위험) |
| **(R-2-c) `secret_scanner.py` catalog 재사용** [C 신규] | Tier-1 45-pattern + 매칭 로직을 공유 모듈로 추출, detection/prevention 단일 source-of-truth | catalog drift 구조적 차단. detection(scan-log)↔prevention(filter) 동기화. 모듈 추출 refactor 1회 | ⭐ 강력 권고 (SC-1 입력) |
| **(R-2-d) LiteLLM callback hook** [C 신규] | `litellm.success/failure_callback` 에 RedactionFilter 등록 (설계 §8.1 기존) | LiteLLM 기존 메커니즘 재사용. 단 LiteLLM-specific → v2.0 Adapter 전환 시 redaction 미승계 (NOTE-C2), callback 등록 누락 silent | 보조 (provider-agnostic 약점, facade 본문 우위) |
| (R-2-e) facade *외부* 독립 middleware | redaction 을 facade 밖 별도 middleware | facade 단일 진입점 (ADR-009 §2.3) 우회 → Provider Liquidity Layer 1 위반 위험 | 비채택 |

### 5.3 sub-cycle 순서 대안

| 후보 | 내용 | 트레이드오프 | 채택 권고 |
|------|------|------------|----------|
| 순차 SC-1→SC-2→SC-3 (brief) | R-2 먼저, R-1 후, 발효 | 즉시 가치 (R-2 본 repo). 총 lead time 길다 | ⭐ 유지 |
| 역순 SC-2→SC-1 | R-1 검증 먼저 | R-1 = 위임 (이미 ADR 권위) → 먼저 할 가치 낮음 | 비채택 |
| 병렬 SC-1 ∥ SC-2 | R-1 ⊥ R-2 독립 활용 | lead time 단축. 단 solo 맥락 context-switch 인지 부하 | 비채택 (solo 비례성) |
| scope 축소 (detection 영구 + prevention 별도 milestone) | full GP-2 PASS 미추구 | ceremony 회피. 단 §4.5 (a) 권위 명시 요구와 충돌 | 비채택 (단 NOTE-C3 self-check) |

### 5.4 full GP-2 PASS scope (Exit (a)) 해석 대안

| 해석 | 내용 | 텍스트 근거 | 채택 권고 |
|------|------|----------|----------|
| ① AND (brief 확정) | R-1 ∧ R-2 검증 둘 다 | §4.5 (a) "+" + §5.1 | brief 권고안 (단 *확정* 아님) |
| **② R-2 발효 + R-1 위임 회귀** [C 식별] | R-2 (facade, 본 repo) 발효 + R-1 위임 신뢰 (ADR-011 §2.3 #2, R-6 지속 회귀) | §4.1 "GP-2 = 보조 역할" + ADR-011 §2.3 #2 "송신 방어로만 신뢰" (위임) | 대안 해석 (SC-3 영역) |
| ③ OR (한쪽만) | R-1 또는 R-2 | 근거 없음 (§4.5 "+" 와 충돌) | 비채택 |

⭐ **논리 구조 확정 = SC-3 발효 합의 영역** (BLOCKING-C2). 본 cycle 은 ① 을 *유일 해석으로 단정 금지*, ② 병기 의무.

### 5.5 합의 형태 대안

| 후보 | 내용 | 트레이드오프 | 채택 권고 |
|------|------|------------|----------|
| 풀 3+1 + 외부 LLM 1+ (brief) | trajectory entry 풀 합의 | 51/52/55 답습 일관. trigger 3/7 발화 | ⭐ 유지 (답습 일관성) |
| 단축 (Reviewer-only) | trajectory entry = 권위 답습 한정 | TR-1 이 SC-1 에서 어차피 풀 3+1 → entry 는 논리적 단축 가능 | 비채택 (답습 일관성 우선, NOTE-C4) |
| 1-agent 직접 | entry brief = 분석만 | over-simplification (Provider Liquidity 직결 무시) | 비채택 |

---

## 6. 조건 요약 (APPROVE WITH CONDITIONS)

1. **(C-C1, BLOCKING)** §4.4 R-2 후보 표에 **(R-2-c) `secret_scanner.py` catalog 재사용** + **(R-2-d) LiteLLM callback hook** 추가 + 각 트레이드오프 등재. (R-2-c) = catalog drift 구조 차단 강력 권고.
2. **(C-C2, BLOCKING)** §5.1 / §7 (C-3) 의 "full GP-2 PASS = R-1 ∧ R-2 (AND)" 를 *확정* 에서 *brief 권고안* 으로 완화 + **대안 해석 ② (R-2 발효 + R-1 위임 회귀)** 병기 + "발효 조건 논리 구조 확정 = SC-3 영역" 명시.
3. **(C-C3, 권고)** §3.3 R-1 후보에 **(R-1-c) 격리 black-box 검증** 추가 ((R-1-a) evidence 수단 구체화).
4. **(C-C4, 권고)** §5.2 sub-cycle 순서에 병렬 / scope 축소 대안 트레이드오프 표 등재 (순차 유지 권고).
5. **(C-C5, 권고)** §8 RT-1 대응을 "redaction 부착 = facade real 전제조건 test 강제" 로 일반화 (부착 위치 무관 window 0).

조건 1~2 (BLOCKING) 흡수 시 trajectory 진입 자격 **APPROVE**. 조건 3~5 (권고) 는 v1.1 흡수 권장이나 발효 차단 아님.

---

## 7. 자기진단 (대안 탐색가 메타 편향)

| # | 위험 | 처리 |
|---|------|----|
| MC-1 | 대안 *과잉 생성* (alternative inflation) | (R-2-c)(R-2-d)(R-1-c) 는 *실재 자산/설계* 직접 read 기반 (secret_scanner.py / llm-providers-design.md §8 / R-2 PoC), 가상 후보 0 |
| MC-2 | scope 외 침범 (sub-cycle 결정 대체) | 모든 대안 = "sub-cycle 입력 등재" 권고, 결정 0. BLOCKING-C2 는 오히려 brief 의 *과잉 확정* 을 완화 |
| MC-3 | ceremony 가중 (조건 인플레이션) | BLOCKING 2건으로 한정 (후보 완전성 + 해석 단정), 권고 3건은 차단 아님. [[feedback_ceremony_inflation]] 답습 |
| MC-4 | Agent A/B 편향 | 미참조 (독립). 직접 read 6 source 기반 |
| MC-5 | over-claim (prevention 자격 주장) | 본 분석 = *경로 대안 식별* 한정, prevention 입증/발효 주장 0. detection≠prevention 답습 |

---

**Agent C 분석 끝. 판정: APPROVE WITH CONDITIONS (BLOCKING 2 + 권고 3).**
