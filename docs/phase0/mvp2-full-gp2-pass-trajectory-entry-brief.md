# full GP-2 PASS trajectory 진입 entry brief (v1.1)

> **작성**: 2026-05-28 (64번째 entry 진입 cycle — 신규 세션 #3)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-full-gp2-trajectory.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 10 1pass 흡수** (별도 v2 cycle 0, ceremony-inflation 차단, 52/55/60 동형). 핵심 정정: **B-1 citation 오귀속** ("(β) §0.2 #23" → **#10**, #23 = 자동 후속) / **B-2** R-2 후보 (R-2-c) secret_scanner 재사용 + (R-2-d) LiteLLM callback hook 추가 / **B-3** "R-1 ∧ R-2 (AND)" 단정 → 대안 해석 병기 (governance §4.1 "GP-2 = 보조" + ADR-011 §2.3 위임). evidence 차단급 over-claim 0 (R-4 = 설계 동등성 일관). §14 흡수 매트릭스 추가.
>
> **scope**: full GP-2 PASS trajectory **진입 자격 audit + R-1/R-2 경로 분석 + 합의 형태 권고**. 실제 sub-수단 *결정* 0 / 실 *구현* 0 / full GP-2 PASS *발효* 0. (사용자 명시 scope = "trajectory entry brief 한정")
>
> **본 cycle = 큰 cycle** (trajectory 진입 합의, 풀 3+1 + 외부 LLM 1+ 의무). 51 audit / 52 (α) entry brief / 55 Layer 통합 PASS entry brief 답습 동형 (entry brief = 진입 자격 + 경로 분석, sub-cycle 진입은 사용자 명시 별도)
>
> **본 cycle 발효 자격** = 진입 자격 audit + 경로 분석 + 합의 형태 권고 + 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = full GP-2 PASS trajectory **진입 자격 발효** + R-1/R-2 sub-cycle 진입 권한 발효 (조건부 승인 조건 우선). 실제 R-1 import *결정* / R-2 facade real *구현* / full GP-2 PASS *발효* = 각각 별도 sub-cycle (본 cycle = trajectory 진입 한정)
>
> **선행 답습**: 60 GP-2 detection-layer PASS 발효 (`92e9078`, B-1 detection/prevention 3축 분리) + 57 (β) R-4 결정 ((β) §0.2 #9 R-1 import 별도 cycle) + 62 MVP-2 Implementation Evidence PASS (prevention deferred scope 명문) + 52 entry R-A-1 (`agent/redact.py` 본 repo 부재 = upstream v0.12.0 401 LOC)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **detection-layer PASS → full GP-2 PASS 격차 정의** (Exit (a) prevention 검증 = R-1 + R-2, 60 §2 3축 답습) (§2)
2. **R-1 경로 분석** (Hermes native redaction, upstream 영역 / import 결정 / 검증 evidence 후보) (§3)
3. **R-2 경로 분석** (facade RedactionFilter, TR-1 발화 / Provider Liquidity 직결 / (d) carry-over 동일 trajectory) (§4)
4. **R-1 ↔ R-2 의존 관계 + sub-cycle 분리 권고** (§5)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ + 승격 트리거** (§6)
6. **trajectory 진입 자격 권고 + 조건** (§7)
7. Rollback Trigger / Evidence 후보 / 금지 / 다음 단계 / cross-ref / 자기진단 (§8~§13)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | full GP-2 PASS *발효* 자체 (본 brief = trajectory 진입 합의 입력) | 0 |
| 2 | **R-1 Hermes upstream `agent/redact.py` 본 repo 內 import 결정** (별도 sub-cycle, 57 (β) §0.2 #9 답습) | 0 |
| 3 | **R-2 facade real 구현** (TR-1 발화 = 별도 sub-cycle, `facade.py` placeholder → real 본문 작성 0) | 0 |
| 4 | Hermes upstream PR 작성 / upstream `agent/redact.py` 본문 변경 (upstream 영역, 본 repo scope 외) | 0 |
| 5 | R-1/R-2 中 *어느 sub-cycle 우선 진입* 결정 (§5 권고 ≠ 결정, 사용자 명시 별도) | 0 |
| 6 | MVP-2 Implementation Evidence PASS 재선언 (62 답습 유지) / detection-layer PASS 재선언 (60 답습) | 0 |
| 7 | R-5 base64/URL/압축 evasion 영역 진입 (영구 분리, G3-4) | 0 |
| 8 | 신규 외부 library 도입 / secret_scanner Tier-2/3 catalog 확장 | 0 |
| 9 | ADR / 헌법 / roadmap / governance / ADR-008/009/011/012 본문 갱신 | 0 |
| 10 | `facade.py` / `secret_scanner.py` / secret-hygiene workflow 본문 변경 | 0 (PoC 시제 + placeholder 보존) |
| 11 | Provider Liquidity 5-way Defense 본문 변경 / LiteLLM 도입 결정 (Q1 합의 보존) | 0 |
| 12 | 자동 후속 sub-cycle 진입 (R-1 / R-2 / full GP-2 PASS) | 0 (사용자 명시 의무) |
| 13 | 본 brief 자체 영구화 / 권위 chain 등재 | 0 |

### §0.3 권위 답습 source

- **governance-preconditions.md §4.5 Exit (a)** (line 451) — "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" (= R-1 + R-2 prevention 검증, full GP-2 PASS Exit 핵심)
- **ADR-011 §2.3 운영 함의 #2** (line 113) — "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0" (R-1 위임 권위) + 권위 위계 (Hermes ≠ root of trust, line 95~108)
- **ADR-011 §2.4 T3** (line 133, verbatim) — "Constitution / ADR / Harness Gates 정의 *자체*의 변경" = 풀 3+1. ⓘ **inference (verbatim 아님, R-1 정정)**: facade real *코드 구현*은 T3 정의 변경 ≠ 해당 → R-2 = TR-1 별도 trigger (풀 3+1 합의 trigger, T3와 구분)
- **ADR-009 §2** (line 49~62) — P1 facade MVP 진입조건 (2026-05-04 이미 충족) + §2.3 Hermes PMO ≠ provider 직접 소유 + LiteLLM 직접 import = `facade.py` 한정
- **`redaction-pattern-equivalence.md` (R-4)** (line 33/39) — 설계 동등성 문서, "Hermes 안전성 선언 금지" (ADR-011 §7.3), prevention *입증* 아님
- **60 GP-2 detection-layer PASS brief v1.1** (`docs/phase0/mvp2-gp2-pass-activation-brief.md`) — §2 3축 분리 (detection ✅ / 설계 동등성 ⚠️ / prevention upstream 위임)
- **57 (β) brief v1.1** (`docs/phase0/mvp2-beta-submeans-decision-brief.md`) — R-4 결정 + R-1 import 별도 cycle + R-2 facade real 별도 trajectory
- **62 MVP-2 PASS brief** (`docs/phase0/mvp2-implementation-evidence-pass-activation-brief.md`) — prevention deferred scope 명문
- **52 entry R-A-1** (`docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`) — `agent/redact.py` 본 repo 부재 = upstream HEAD v0.12.0 `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC
- **본 cycle audit (read-only, 2026-05-28)** — `facade.py` placeholder + governance §4 + ADR-011 §2.3 filesystem direct

---

## §1 진입 컨텍스트

### §1.1 선행 chain

| 합의/구현 | 본 cycle 답습 |
|----------|-----------|
| 62 MVP-2 Implementation Evidence PASS (`82e1ee6`, 4 source APPROVE WITH CONDITIONS) | MVP-2 = G4 ledger 완전 + GP-2 **detection-tier**. **full GP-2 PASS (prevention R-1/R-2) = MVP-2 PASS 잔여 trajectory** (62 §결론 명문) → 본 cycle = 그 trajectory 진입 |
| 60 GP-2 detection-layer PASS (`92e9078`, REVISE → detection reframe) | (b)(c)(d) detection ✅ operative + (a) 설계 동등성 partial. prevention (R-1/R-2) = in-repo 입증 0 (upstream 위임) → 본 cycle = prevention 경로 분석 |
| 57 (β) R-4 결정 (`18e8ad1`) | GP-2 수단 = R-4 (R-3 detection 우선 + R-1/R-2 prevention deferred). **R-1 import = 별도 cycle ((β) §0.2 #9) / R-2 facade real = 별도 trajectory ((β) §0.2 #10)** (B-1 정정 — #23 = 자동 후속 sub-cycle) |

### §1.2 현 GP-2 상태 (60 §2 3축 답습)

- **축 1 detection (operative ✅)**: R-3 (`secret-hygiene-egress-redaction.yml` D-2 + `secret_scanner.py --mode scan-log`) — 송신/로그 secret 잔존 회귀 검출. in-repo operative green (actual run `26517803107`).
- **축 2 설계 동등성 (⚠️ partial)**: R-4 (`redaction-pattern-equivalence.md`) — Tier-1 42 catalog *패턴 동등성 문서*. prevention 입증 아님 (Hermes 안전성 선언 금지).
- **축 3 prevention (in-repo 입증 0)**: R-1 (Hermes native, 본 repo 부재) + R-2 (facade placeholder). **본 cycle 대상 = 축 3 경로 분석**.

→ **detection-layer PASS → full GP-2 PASS 격차 = 축 3 prevention 검증 (= Exit (a))**. 본 cycle = 이 격차를 메우는 trajectory 진입 자격 + 경로 분석 (실제 충족은 sub-cycle).

---

## §2 detection-layer PASS → full GP-2 PASS 격차 (Exit (a) prevention 검증)

### §2.1 Exit 5조건 현 상태 (governance §4.5 + 60 §4)

| # | 조건 | detection-layer (60 발효) | full GP-2 PASS 추가 요구 |
|---|------|------|---------|
| (a) | 동등 이상 보안 결과 | ⚠️ **partial (설계 동등성)** | ✅ 격상 = **R-1 Hermes native Tier-1 42 적용 검증 + R-2 facade redaction filter 검증** (governance §4.5 (a) verbatim) |
| (b) | 격리 PoC 실증 | ✅ secret-hygiene D-2 (detection) | prevention PoC (R-1 실행 evidence + R-2 filter 단위 test) |
| (c) | ADR/SDD 권위 | ✅ ADR-011 §2.3 #2 + governance §4 | (유지) |
| (d) | 자동 회귀 검증 | ✅ secret-hygiene D-2 CI green (detection) | prevention 회귀 (R-1 upstream 변경 시 R-2/R-4.1 자동 재실행, ADR-011 §2.3 #4 R-6) |
| (e) | 합의 APPROVE | ✅ 60 (detection-layer) | full GP-2 PASS 발효 합의 (별도) |

### §2.2 핵심 격차 = (a) prevention 검증 2-pronged

governance §4.5 (a) line 451 = **"Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증"** — 2개 prevention 수단 모두 검증 요구:
1. **R-1**: Hermes native redaction이 Tier-1 42 catalog를 실제 적용함을 *검증* (적용 *구현*은 upstream 영역).
2. **R-2**: facade RedactionFilter가 LLM API request body redaction을 적용함을 *검증* (= facade real 선행).

→ **full GP-2 PASS = R-1 검증 ∧ R-2 검증 (AND, PRIMARY)** — governance §4.5 (a) verbatim "+" 답습. 본 cycle = 두 경로의 진입 자격 + 분석 (§3 + §4).

⚠️ **B-3 대안 해석 병기** (Agent C C2, AND 단정 완화): governance §4.1 line 424 = "GP-2 는 ADR-011 §2.3 운영 함의 #2 의 **보조* 역할*" + ADR-011 §2.3 #2 = R-1 runtime redaction **위임** (본 repo 저장/구현 책임 0). → R-1의 "검증"은 *재구현*이 아니라 **위임 실효 검증** (§3.2). 대안 해석 = "**R-2 in-repo prevention 발효 + R-1 위임 회귀 검증**"으로 (a) 충족 가능 (R-1 직접 구현 강제 아님). **AND = PRIMARY 유지** (Exit (a) verbatim "+"), 단 R-1 충족 형태 = 위임 검증 (R-1-a 권고, §3.3) — full GP-2 PASS가 R-1 *구현*에 hard-block 되지 않음.

---

## §3 R-1 경로 분석 — Hermes native redaction (Tier-1 42 적용 검증)

### §3.1 영역 분리 (52 entry R-A-1 답습 — 핵심)

| 영역 | 내용 | 본 cycle scope |
|------|----|------|
| **(i) Hermes upstream 영역** | `agent/redact.py` (upstream HEAD v0.12.0, `/tmp/hermes-phase0/hermes-agent/agent/redact.py` 401 LOC) — **본 repo 內 ≠ 존재** | ❌ scope 외 (upstream PR 영역) |
| **(ii) 본 repo import 결정 영역** | Hermes runtime redaction을 본 repo runtime 의존성에 *통합/위임 신뢰* 결정 (ADR-011 §2.3 #2 위임 권위 활용) | sub-cycle (본 cycle = 분석만) |
| **(iii) 본 repo 검증 evidence 영역** | Hermes native가 Tier-1 42 catalog 적용함을 격리 환경 실행 검증 (E-1 답습, `agent/redact.py` 실행 evidence) | sub-cycle (본 cycle = 후보 식별) |

> ⓘ **R-10 주석** (Agent A): governance §4.4 Entry line 444 = "Hermes native redaction `agent/redact.py` 존재 확인 (R-1 Day 2 evidence)" 는 **Hermes upstream 영역 기준** 표기 — 본 repo 內 부재 (52 R-A-1, find/rg 직접 확인)와 충돌 아님 (Entry = upstream artifact 존재 확인, 본 repo import ≠ 의미). governance §4.4 본문 변경 0 (T3 영역).

### §3.2 R-1 권위 = ADR-011 §2.3 #2 위임 (이미 발효)

- ADR-011 §2.3 #2 (line 113): "Hermes 자체 redaction은 **로그/LLM 송신 방어로만 신뢰**, 저장 경로(DB/파일) 차단 책임 없음."
- 즉 R-1 runtime redaction은 **이미 ADR 권위로 위임됨** — full GP-2 PASS는 R-1을 *재구현*하는 것이 아니라 **위임이 실효함을 검증** (Tier-1 42 적용 evidence + upstream 변경 자동 회귀, §2.3 #4 R-6).
- ⚠️ **Hermes ≠ root of trust** (권위 위계 line 95~108): Hermes 출력은 Tools로 검증된다 → R-1 검증 = canary/test가 Hermes 위에 위치 (R-5/R-6 근거).

### §3.3 R-1 경로 후보 (sub-cycle 입력, 결정 0)

- **(R-1-a) 위임 검증 한정**: 본 repo는 import 0, ADR-011 §2.3 #2 위임 유지 + Tier-1 42 적용 검증 evidence (격리 실행) + upstream 변경 R-6 자동 재실행. → 본 repo runtime code 변경 최소.
- **(R-1-b) import 통합**: Hermes runtime redaction을 본 repo runtime 의존성으로 통합 (52 R-A-1 import 결정). → Provider Liquidity / Hermes PMO 경계 영향 (ADR-009 §2.3) 평가 필요.
- **(R-1-c) 격리 CI 검증** (Agent C 대안): import 0 + 본 repo CI에서 Hermes artifact 격리 실행 검증만 (upstream PR 0). → (R-1-a)의 CI-자동화 변형.
- ⭐ **권고 방향**: (R-1-a) 위임 검증 우선 — 본 repo = DESIGN/governance repo (60 §1.2), Hermes ≠ root of trust 답습. import (R-1-b)는 Hermes PMO 활성화 시점 별도. **(결정 = sub-cycle, 본 cycle = 권고만)**.

> ⚠️ **R-2 evidence contract 의무** (codex 권고 2 + Agent C R-1-c): (R-1-a)/(R-1-c) "import 0 위임 검증"을 택해도 governance §4.5 (a)는 "Hermes native Tier-1 42 적용 검증"을 요구 (§2.2 AND PRIMARY). 따라서 SC-2 진입 시 **evidence contract 명문 필수**: (i) Hermes artifact/version pin (`hermes-version.yaml` v0.12.0) + (ii) Tier-1 42 catalog 적용 격리 실행 evidence (E-1) + (iii) canary 재검증 (R-5) + (iv) upstream 변경 R-6 자동 재실행 (ADR-011 §2.3 #4). 위임 검증 ≠ "검증 면제" — 실행 가능 evidence 계약으로 (a) 충족.

---

## §4 R-2 경로 분석 — facade RedactionFilter (facade real, TR-1)

### §4.1 현 상태 = placeholder (filesystem direct verify)

- `src/adapters/llm/facade.py` (41 LOC, R-6 정정): `LLMFacade.complete()` = `raise NotImplementedError("Placeholder — TR-1 풀 3+1 합의 후 real 본문 작성")`. `health()` = `return {}`.
- 헤더 명문: "본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로* (§4.1 답습). 현 시점 placeholder — real 본문 작성 시 자동 풀 3+1 합의 trigger **TR-1** 발화."

### §4.2 R-2 = full GP-2 PASS + (d) carry-over 동일 trajectory

- **(d) facade real (TR-1)** = 63 entry carry-over #4 + 본 trajectory R-2 = **동일 작업** (별도 아님). full GP-2 PASS prevention 입증을 위해 facade real이 *선행 필수* (RedactionFilter는 real facade 진입점에만 부착 가능).
- governance §4.3 (line 435): "P1 v2 LLM facade RedactionFilter" = 계산적 강제 메커니즘 (P1 facade layer).

### §4.3 R-2 = Provider Liquidity 5조-2 직결 (비협상)

- ADR-009 §2 (line 49~62): P1 facade MVP 진입조건 4개 **2026-05-04 이미 충족** — 별도 트리거 없음. ADR-008 + P1 v2 합의 APPROVE = MVP 진입 도화선.
- ADR-009 §2.3: **Hermes PMO ≠ provider 직접 소유** — provider SDK 직접 import / 모델명 분기 *금지*, P1 facade 단일 진입점 강제. LiteLLM 직접 import = `facade.py` 한 파일 한정.
- ⚠️ **R-2 facade real = Provider Liquidity 5-way Defense Layer 1 실 구현** (코드 변경 없이 모델/provider 교체 = 헌법 5조-2 비협상, [[feedback_provider_liquidity]]). LiteLLM 도입 자체는 Q1 합의 (2026-05-10) 보존 — 본 cycle 신규 도입 0.

### §4.4 R-2 경로 후보 (sub-cycle 입력, 결정 0)

- **(R-2-a) facade real + RedactionFilter 동시**: facade real 본문 (LiteLLM import + Router 위임) + RedactionFilter (request body Tier-1 42 redaction) 통합 구현. → TR-1 발화 = 풀 3+1 합의.
- **(R-2-b) facade real 먼저 / RedactionFilter 후속**: facade real (Provider Liquidity Layer 1) 우선 발효 → RedactionFilter는 별도 step. → 2 sub-cycle.
- **(R-2-c) `secret_scanner.py` Tier-1 catalog 재사용** (B-2, Agent C C1): 기존 in-repo `tools/secret_scanner.py` Tier-1 catalog (detection 시제)를 RedactionFilter redaction 로직에 재사용 — 신규 catalog 중복 회피, detection ↔ prevention 패턴 단일 source.
- **(R-2-d) LiteLLM callback hook** (B-2, Agent C C1): facade 본문 직접 redaction 대신 LiteLLM callback/logger hook으로 request body redaction 주입 — facade 본문 침습 최소, but LiteLLM hook 시점/순서 검증 필요.
- ⭐ **권고 방향**: (R-2-a) 동시 + (R-2-c) catalog 재사용 — **RedactionFilter = facade *내부 협력자*** (R-5, Agent A): facade 진입점이 LLM API request body 통과 지점이므로 redaction은 facade real에 부착 필수. 분리 시 facade real 후 redaction 미부착 window 발생 (RT-1). TDD 적용 (RED: redaction filter test → GREEN: filter 구현). **(결정 = sub-cycle, 본 cycle = 권고만)**.

---

## §5 R-1 ↔ R-2 의존 관계 + sub-cycle 분리 권고

### §5.1 의존 관계

| 관계 | 내용 |
|------|----|
| R-1 ⊥ R-2 (독립) | R-1 = Hermes runtime (upstream/위임 검증) / R-2 = facade layer (본 repo). 서로 다른 layer = defense-in-depth (R-4 §3.1 답습) |
| full GP-2 PASS = R-1 ∧ R-2 | Exit (a) = "Hermes native 검증 **+** facade filter 검증" — 둘 다 (AND). 한쪽만 = full GP-2 PASS 미충족 |
| R-2 = (d) carry-over 흡수 | R-2 facade real = (d) facade real 동일 작업 → R-2 진행 = (d) 동시 해소 |

### §5.2 sub-cycle 분리 권고 (결정 0 — 사용자 명시 별도)

| sub-cycle | 작업 | 규모 | 의존 |
|-----------|----|----|----|
| **SC-1 (R-2 facade real)** | facade real + RedactionFilter (TR-1) | 풀 3+1 (TR-1 trigger) + 실 코드 | (d) carry-over 흡수, Provider Liquidity Layer 1 |
| **SC-2 (R-1 위임 검증)** | Hermes native Tier-1 42 적용 검증 evidence + R-6 자동 회귀 (import = (R-1-b) 시 추가 평가) | 풀 3+1 + 격리 실행 | ADR-011 §2.3 #2 위임 |
| **SC-3 (full GP-2 PASS 발효)** | SC-1 + SC-2 evidence 완료 후 PASS 발효 합의 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (32/60 답습) | SC-1 ∧ SC-2 |

⭐ **순서 권고**: SC-1 (R-2) → SC-2 (R-1) → SC-3. 사유 = R-2 = 본 repo 영역 + (d) carry-over 흡수 + Provider Liquidity 직결 (즉시 가치). R-1 = upstream 위임 (이미 ADR 권위) → 검증 evidence 중심. **(순서 결정 = 사용자 명시 별도, 본 cycle = 권고)**.

---

## §6 합의 형태 + 풀 3+1 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: trajectory 진입 합의 (52 (α) / 55 entry brief 답습) + 큰 결정 (full GP-2 PASS = MVP-2 잔여 trajectory) + 헌법 5조-2 cross-vendor + R-2 = Provider Liquidity 직결.

### §6.2 7 승격 트리거

| # | trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 큰 결정 (trajectory 진입) | ✅ | full GP-2 PASS trajectory = MVP-2 prevention 잔여 |
| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1 |
| 3 | ADR 본문 변경 | ❌ | 0 |
| 4 | 권위 chain 다중 source 손상 | ❌ | 권위 인용 답습 (governance §4.5 + ADR-011 §2.3) |
| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 (5조-2) |
| 6 | Provider Liquidity 영향 | ✅ ⭐ | R-2 facade real = Provider Liquidity Layer 1 |
| 7 | Hermes PMO 격상 | ❌ | 0 (R-1 import = sub-cycle, 본 cycle 결정 0) |

→ **3/7 발화 → 풀 3+1 + 외부 LLM 1+ 적격**.

### §6.3 외부 LLM = cross-vendor codex (E-α 답습)

55/52/60 entry 답습 — Claude tmux + codex 직접 호출 (`--dangerously-bypass-approvals-and-sandbox`, gpt-5.5 cross-vendor).

---

## §7 trajectory 진입 자격 권고 + 조건

⭐ **권고 = full GP-2 PASS trajectory 진입 APPROVE WITH CONDITIONS**:

1. **trajectory 진입 자격 충족** — detection-layer PASS (60 ✅) + MVP-2 PASS prevention 잔여 trajectory 명문 (62 ✅) + 격차 = (a) prevention 검증 (§2.2).
2. **조건**:
   - (C-1) **R-1 = Hermes upstream 영역 분리 답습** — 본 repo `agent/redact.py` 부재 (52 R-A-1), 직접 구현 = upstream PR (scope 외). 본 repo = 위임 검증 (R-1-a 권고) 또는 import 결정 (R-1-b, Hermes PMO 경계 평가).
   - (C-2) **R-2 facade real = TR-1 발화 = 별도 sub-cycle** — `facade.py` placeholder 보존, real 본문 = SC-1 합의 후. (d) carry-over 동시 해소.
   - (C-3) **full GP-2 PASS = R-1 ∧ R-2 검증 (AND)** — 한쪽 단독 ≠ full GP-2 PASS (Exit (a) 2-pronged).
   - (C-4) **Provider Liquidity 5조-2 비협상** — R-2 facade real = Layer 1 실 구현, LiteLLM 도입은 Q1 합의 보존 (신규 0).
   - (C-5) **detection-layer PASS / MVP-2 PASS 재선언 0** (60/62 답습 유지) + **prevention over-claim 주의** (본 세션 #2 4회 cascade 교훈, [[feedback_pass_scope_overclaim]] — R-4 = 설계 동등성, prevention 입증 아님).
3. **sub-cycle 진입 = 사용자 명시 의무** (SC-1/SC-2/SC-3 순서 §5.2 권고 ≠ 결정).

→ **trajectory 진입 발효 자격 = 진입 자격 audit + R-1/R-2 경로 분석 + 합의 APPROVE + 사용자 명시**. **full GP-2 PASS 발효 = SC-1 + SC-2 evidence 완료 후 SC-3 (별도)**.

---

## §8 Rollback Trigger 후보 (sub-cycle 입력, 결정 0)

| # | trigger | 영역 | 대응 |
|---|---------|----|----|
| RT-1 ⭐ | facade real 후 RedactionFilter 미부착 window (R-7 강화) | SC-1 | **(R-2-a) 동시 구현 안전 제약 명문 — facade real 발효 ∧ RedactionFilter 발효 = 단일 atomic step (분리 발효 금지). facade real PR에 redaction filter test green 필수 gate** |
| RT-2 | Hermes upstream redaction silent 깨짐 (Tier-1 42 미적용 회귀) | SC-2 | R-6 자동 재실행 (ADR-011 §2.3 #4) + R-5 canary 재검증 |
| RT-3 | LiteLLM 도입이 Provider Liquidity 위반 (provider lock-in) | SC-1 | ADR-009 §2.3 facade 단일 진입점 강제 + 5-way Defense |
| RT-4 ⭐ | base64/URL-encoded/압축 evasion 발견 (R-9 자격) | R-5 영역 | **known limitation 명문 (영구 분리, G3-4) — full GP-2 PASS scope = Tier-1 42 평문 한정, base64 evasion 제외 자격 부착 (60 §4.1 답습)** |
| RT-5 | R-1 import (R-1-b)이 Hermes ≠ root of trust 위반 | SC-2 | 위임 검증 (R-1-a) 환원 또는 Hermes PMO 경계 합의 |
| RT-6 ⭐ | **cover 비대칭** (R-8, 60 B-2 답습) — GP-2 prevention ends 의 in-repo 능동 redaction cover = 0 (R-1 upstream 단독 위임), Layer 2 (2b + rewrite-defense CI 이중 cover) 와 비대칭 | SC-2/SC-3 | R-2 facade real 발효 시 in-repo prevention cover 1 확보 (비대칭 해소 부분) + "완전 동형" 표현 회피 명문 |

---

## §9 Evidence 후보 (sub-cycle 입력, 결정 0)

- E-1: Hermes native `agent/redact.py` Tier-1 42 catalog 적용 격리 실행 evidence (governance §4.4 R-1 Day 2 답습)
- E-2: facade RedactionFilter 단위 test (request body Tier-1 42 redaction, TDD RED→GREEN)
- E-3: facade real LiteLLM Router 위임 동작 evidence (Provider Liquidity Layer 1)
- E-4: R-6 workflow upstream 변경 자동 재실행 actual run (ADR-011 §2.3 #4)
- E-5: full GP-2 PASS Exit (a)~(e) evidence 매트릭스 (SC-3 입력)

---

## §10 금지 사항

§0.2 답습 (13). 추가: R-1 import 결정 0 / R-2 facade real 구현 0 / upstream PR 0 / full GP-2 PASS 발효 0 / sub-cycle 우선순위 결정 0 / LiteLLM 신규 도입 0 / 자동 후속 0.

---

## §11 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex E-α) → Reviewer 통합 → v1.1 흡수 → commit + push → **trajectory 진입 자격 발효** (사용자 명시 후)
2. **SC-1 (R-2 facade real + RedactionFilter, TR-1)** — facade real 본문 + filter 구현 (실 코드, TDD). (d) carry-over 동시 해소 (별도 sub-cycle)
3. **SC-2 (R-1 위임 검증)** — Hermes native Tier-1 42 적용 검증 evidence + R-6 자동 회귀 (별도 sub-cycle)
4. **SC-3 (full GP-2 PASS 발효 합의)** — SC-1 ∧ SC-2 evidence 후 (32/60 답습, 별도 cycle)

---

## §12 cross-reference 답습

- governance-preconditions.md §4 (GP-2 정의 + §4.5 Exit (a) line 451)
- ADR-011 §2.3 운영 함의 #2 (R-1 위임) + #4 (R-6 자동 회귀) + 권위 위계 (Hermes ≠ root of trust) + §2.4 T3
- ADR-009 §2 (P1 facade MVP 진입조건) + §2.3 (Hermes PMO ≠ provider, facade 단일 진입점)
- redaction-pattern-equivalence.md (R-4 설계 동등성, Hermes 안전성 선언 금지 §7.3)
- 60 GP-2 detection-layer PASS brief v1.1 + 57 (β) brief v1.1 + 62 MVP-2 PASS brief
- 52 entry R-A-1 (`agent/redact.py` 본 repo 부재 = upstream v0.12.0 401 LOC)
- 실 자료: `src/adapters/llm/facade.py` (placeholder) + `tools/secret_scanner.py` + `secret-hygiene-egress-redaction.yml`

---

## §13 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | full GP-2 PASS *기정사실화* | 발효 = SC-3 (SC-1 ∧ SC-2 evidence 후 합의 + 사용자 명시), 본 cycle = trajectory 진입 한정 (§0.2 #1) |
| P-2 | R-1 = 본 repo 구현 가능 *오인* | §3.1 영역 분리 — `agent/redact.py` 본 repo 부재 (52 R-A-1), 직접 구현 = upstream PR (scope 외) |
| P-3 | R-2 facade real *우회 구현* (TR-1 미발화) | §4.1 + (C-2) — placeholder 보존, real = SC-1 풀 3+1 합의 후 |
| P-4 | prevention over-claim (R-4 = prevention 입증 *오인*) | §1.2 + (C-5) — R-4 = 설계 동등성 (Hermes 안전성 선언 금지), prevention 입증 아님 ([[feedback_pass_scope_overclaim]], 본 세션 #2 4회 cascade 교훈) |
| P-5 | DESIGN repo vs runtime redaction 혼동 | §3.2 — 본 repo = 설계/검증, 실 runtime = Hermes upstream (위임) |
| P-6 | sub-cycle 순서 권고 = *결정* 오인 | §5.2 + (C-1~C-3) — 권고 ≠ 결정, 사용자 명시 별도 |
| P-7 | 작성자 = 60/62 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 (본 세션 #2 over-claim 4회 포착 입증) |
| P-8 | Provider Liquidity 영향 과소 | §4.3 + (C-4) — R-2 = 5조-2 비협상 Layer 1, trigger 6 발화 |

---

## §14 v1.1 흡수 매트릭스 (BLOCKING 3 + 권고 10 1pass)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-full-gp2-trajectory.md` 답습 1pass 흡수 (별도 v2 cycle 0, 52/55/60 동형). **4 source 전원 APPROVE WITH CONDITIONS** (codex BLOCKING 0 + Agent A BLOCKING 0 + Agent B BLOCKING 1 + Agent C BLOCKING 2). evidence 차단급 over-claim 0, citation/framing/후보 누락만.

| # | 흡수 | source | 정정 위치 |
|---|------|--------|------|
| B-1 ⭐ | citation 오귀속 "(β) §0.2 #23" → **#10** (facade real, #23 = 자동 후속) | Agent B (Reviewer verify CONFIRMED) | §1.1 표 |
| B-2 ⭐ | R-2 후보 (R-2-c) secret_scanner Tier-1 재사용 + (R-2-d) LiteLLM callback hook 추가 | Agent C C1 | §4.4 |
| B-3 ⭐ | "R-1 ∧ R-2 (AND)" 단정 → AND PRIMARY 유지 + 대안 해석 NOTE 병기 (governance §4.1 "보조" + ADR-011 §2.3 위임) | Agent C C2 | §2.2 |
| R-1 | ADR-011 §2.4 T3 = verbatim vs inference 분리 | codex 1 | §0.3 |
| R-2 ⭐ | SC-2 evidence contract 의무 명문 (artifact pin + Tier-1 42 검증 + canary + R-6) | codex 2 + Agent C R-1-c | §3.3 |
| R-3 | "carry-off" → "carry-over" 오타 | codex 3 | §5.1 |
| R-4 | §11 마지막 "사용자 명시" 조건 반복 | codex 4 | §11 + 끝 |
| R-5 | RedactionFilter = facade 내부 협력자 근거 강화 | Agent A | §4.4 |
| R-6 | facade.py LOC 42 → 41 | Agent A | §4.1 |
| R-7 | RT-1 window 안전 제약 명문 (atomic step) | Agent B + Agent C | §8 RT-1 |
| R-8 | RT-6 cover 비대칭 (60 B-2 답습) 신설 | Agent B | §8 RT-6 |
| R-9 | RT-4 base64 evasion 자격 부착 | Agent B | §8 RT-4 |
| R-10 | governance §4.4 Entry vs 52 R-A-1 충돌 주석 | Agent A | §3.1 |

**4 source 정합 (evidence 실증)**: facade placeholder (41 LOC, NotImplementedError) / `agent/redact.py` 본 repo 부재 (find/rg) / governance §4.5 (a) AND verbatim / R-4 = 설계 동등성 (Hermes 안전성 선언 금지) / R-3 detection operative / pytest 152 green / prevention over-claim 0 / scope 13개 침입 0. **권위 인용 cross-verify: codex 11/11 일치 + Agent B 13/14 일치 (B-1 1건 모순 CONFIRMED 정정)**.

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → 본 cycle 합의 발효 (APPROVE WITH CONDITIONS → v1.1 흡수) → **full GP-2 PASS trajectory 진입 자격 발효** (사용자 명시 후). 후속: SC-1 (R-2 facade real) / SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) = **사용자 명시 의무 별도 sub-cycle (자동 진입 0)**.
