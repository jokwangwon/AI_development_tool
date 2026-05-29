# SC-2 R-1 Hermes 위임 검증 brief (v1.1)

> **작성**: 2026-05-28 (66번째 entry 진입 cycle — 세션 #3)
>
> **v1 → v1.1 갱신 (reframe)**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc2.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 4 + 권고 4 reframe 흡수** (60 detection reframe 동형). **핵심 정정 (60 over-claim cascade 재발)**: **B-1 축 3 R-6 자동 회귀 over-claim** (Reviewer verify: r2-canary.yml = R-4.1 Tier-1 42 catalog canary, **Hermes dependency lock trigger 미구현** — Hermes egress 자동 회귀 아님) → "ADR 의무 *요구* / 현 R-6 Tier-1 catalog operative" / **B-2 HERMES_REDACT_SECRETS opt-in 활성화 전제** (기본 false, v0.12.0 ON→OFF) → "활성화된 Hermes redaction" / **B-3** artifact 부재 완화 (docker/r2-poc 골격 존재) + URL 출처 불명 / **B-4** 위치 evidence 시점성. **"충족" → "조건부/문서 기반 충족"** (R-1 prong = Exit (a) Hermes-native sub-evidence). evidence 실증 (위치+동등성), framing over-claim 정정. §11 흡수 매트릭스 추가.
>
> **scope** (사용자 명시 "문서 종합 위임 검증 + contract"): **R-1 (Hermes native redaction) 위임 검증 종합** — day2-r1 (위치) + R-4 §5 (동등성) + R-6 (Tier-1 canary, Hermes 자동 회귀 *의무*) + ADR-011 §2.3 #2 (위임 권위) 종합 + **evidence contract 명문** (version pin v0.12.0 + R-6 + 격리 실행 SOP). **실 격리 canary 실행 = artifact 재확보 시점 deferred** (day2-r1 "코드 분석 충분" 선례). 실 코드 0.
>
> ⚠️ **over-claim 경계 (본 세션 #2 4회 cascade 교훈 + R-4 §7.3 답습)**: 본 cycle = **R-1 위임 *검증* (Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버 + 자동 회귀)**. ≠ **"Hermes 안전성 선언"** (ADR-011 §7.3 "본 ADR 은 Hermes 안전성을 선언하지 않는다" 금지). 위치/동등성 *사실* 검증이지 "Hermes redaction 완벽" 선언 아님.
>
> **본 cycle = 큰 cycle** (full GP-2 PASS Exit (a) R-1 prong, 풀 3+1 + 외부 LLM 1+).
>
> **본 cycle 발효 효과** = full GP-2 PASS Exit (a) **R-1 prong 위임 검증 충족** (Hermes upstream 위임 실효 확인). R-2 prong = SC-1 (facade RedactionFilter) ✅ 이미 발효 → **full GP-2 PASS = R-1 ∧ R-2 충족 → SC-3 발효 합의 (별도)**.
>
> **선행 답습**: 65 SC-1 (R-2 facade RedactionFilter operative) + 64 trajectory §3 (R-1 = upstream 위임, (R-1-a) 권고 + evidence contract 의무) + day2-r1 (R-1 위치 검증) + R-4 §5 (Hermes ⊇ Tier-1) + ADR-011 §2.3 #2 (위임 권위)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **R-1 위임 검증 4축 종합** (위치 / 동등성 / 자동 회귀 / 권위) (§2)
2. **evidence contract 명문** (version pin v0.12.0 + R-6 자동 재실행 + 격리 실행 SOP) (§3)
3. **실 격리 canary 실행 deferred 정당화** (day2-r1 선례 + artifact 부재) (§4)
4. **R-1 prong 충족 판정 + over-claim 경계** (§5)
5. **합의 형태 + Rollback + Evidence + 자기진단** (§6~§10)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | **"Hermes 안전성 선언"** (ADR-011 §7.3 금지 — 위임 *검증* ≠ 안전 선언) | 0 |
| 2 | **full GP-2 PASS 발효** (SC-3 별도 cycle — R-1 ∧ R-2 충족 후) | 0 |
| 3 | **R-1 Hermes `agent/redact.py` 본 repo import** (위임 검증 = import 0, R-1-a) | 0 |
| 4 | **실 격리 canary 실행** (artifact 부재 → 재확보 시점 deferred, SOP 명문만) | 0 |
| 5 | Hermes upstream re-clone / agent/redact.py 본문 변경 | 0 |
| 6 | hermes-version.yaml **파일 생성** (governance 명문 답습 — 파일화는 절충안, 본 cycle contract 명문만) | 0 |
| 7 | R-4 / day2-r1 / governance / ADR-011 본문 변경 | 0 |
| 8 | 실 코드 / CI / r2-canary.yml 본문 변경 | 0 |
| 9 | SC-1 (R-2) 재선언 / detection-layer PASS (60) 재선언 | 0 |
| 10 | 자동 SC-3 진입 | 0 (사용자 명시 의무) |

### §0.3 권위 답습 source

- **day2-r1** (`docs/phase0/day2-r1-redaction-location-verification.md`) — R-1 *위치* 검증 (Hermes redaction = 로그/도구출력/gateway 통신 전용, 25 import 비-DB, docstring "mask API keys/tokens/credentials before log/output/gateway"). ⚠️ day2-r1 "FAIL" = **G1a (DB INSERT 경로) 맥락** (DB = GP-1 책임). **GP-2 (송신/로그) 맥락에서는 Hermes redaction 적용 ✅** (위임 근거).
- **R-4 §5** (`docs/architecture/redaction-pattern-equivalence.md`) — Hermes **47 카테고리 + 2 frozenset ⊇ Tier-1 45 catalog** (Hermes ⊇ P1_REDACTOR ⊇ baseline). §7.3 "Hermes 안전성 선언 금지".
- **R-6** (`.github/workflows/r2-canary.yml`) — Tier-1 42 canary regression (nightly cron + PR), Hermes 의존성 변경 시 R-2/R-4.1 자동 재실행 (ADR-011 §2.3 #4).
- **ADR-011 §2.3 #2** (line 113) — "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰" (R-1 위임 권위) + §2.3 #4 (자동 회귀) + §7.3 (안전성 선언 금지).
- **governance §4.5 (a)** — "Hermes native redaction Tier-1 42 catalog 적용 검증 + facade redaction filter 검증" (R-1 + R-2). **§1.2.7 P11 / Layer 1** — hermes-version.yaml v0.12.0 pin.
- **65 SC-1** — R-2 prong (facade RedactionFilter) operative.
- **canary-recheck-design.md (R-5)** — canary 재검증 trigger 설계 (HERMES_REDACT_SECRETS config 체크).

---

## §1 진입 컨텍스트

- 65 SC-1 (R-2 facade RedactionFilter) operative → full GP-2 PASS Exit (a) R-2 prong ✅.
- 본 SC-2 = R-1 prong (Hermes native redaction 위임 검증). full GP-2 PASS = R-1 ∧ R-2 (AND, 64 trajectory §2.2).
- R-1 = Hermes upstream 위임 (ADR-011 §2.3 #2). 본 repo = DESIGN/governance repo → R-1 *재구현/import* 0, **위임 실효 검증** ((R-1-a), 64 §3.3).

---

## §2 R-1 위임 검증 4축 종합

### §2.1 축 1 — 위치 검증 (활성화된 Hermes redaction = GP-2 영역 적용) ✅ (시점성 명시)

day2-r1 (**2026-05-05 코드 분석 시점**, Hermes v0.12.0) 결정적 사실 3건:
- **사실 1**: `agent/redact.py:1-8` docstring = "Regex-based secret redaction **for logs and tool output** ... mask API keys, tokens, and credentials **before they reach log files, verbose output, or gateway logs**".
- **사실 2**: redaction import 25개 위치 = 로깅/도구출력/통신 경로 (DB write 0).
- **사실 3**: `hermes_state.py` (SessionDB) redaction import 0 (DB INSERT 미적용).

→ **활성화된 Hermes redaction = GP-2 영역 (로그/LLM 송신/도구출력) 적용 ✅**. day2-r1 "FAIL" = G1a (DB INSERT) 맥락 (DB = GP-1 책임, ADR-011 §2.3 #2/#3) — **GP-2 위임 근거와 모순 0** (GP-2 영역 적용 입증).

⚠️ **B-2 활성화 전제 (위임 실효 필수 조건)**: `HERMES_REDACT_SECRETS=false` = **기본 opt-in** (R-4 line 138, v0.12.0 breaking change default ON→OFF). day2-r1 §2 "security.redact_secrets: true 활성화 후" 전제. → 위임 검증 = **`HERMES_REDACT_SECRETS=true` 활성화 전제** (미활성화 시 redaction 미작동). evidence contract C-5 (활성화 config 검증, §3) 신설.

⚠️ **B-4 시점성**: 위치 evidence = 2026-05-05 day2-r1 코드 분석 (Hermes v0.12.0). **artifact 부재로 현 시점 재확인 = C-3 SOP (artifact 재확보) 시점**. day2-r1 "코드 분석 충분" 선례 답습 (실 재확인 = 동일 결론 강화).

### §2.2 축 2 — 패턴 동등성 (Hermes ⊇ Tier-1) ✅

R-4 §5 3-way 비교:
- Hermes **35 prefix + 12 regex + 2 frozenset (16+14 키) = 47 카테고리 + 2 frozenset**.
- Tier-1 catalog (secret_scanner, R-4.1) = baseline 5 + prefix 31 + regex 7 + alternation 2 = 45.
- **Hermes ⊇ P1_REDACTOR + Hermes ⊇ Tier-1** (Hermes superset — R-4 §5.3 "핵심 관찰 #1").

→ **활성화된 Hermes native redaction 이 Tier-1 42 catalog 를 동등 이상 커버 ✅** (governance §4.5 (a) "Tier-1 42 catalog 적용" 충족). ⚠️ R-4 = 설계 동등성 비교 (§7.3 안전성 선언 아님) — "Hermes 가 Tier-1 패턴을 *포함*" 사실 검증. **출처 (R-2 정정)**: R-4 §5 동등성 매트릭스 **+ R-4.1/R-6 catalog 체계** (R-4 §5 단독 아님 — Tier-1 42/45 = R-4.1 확장).

### §2.3 축 3 — 자동 회귀 검증 (현 R-6 = Tier-1 canary operative / Hermes lock trigger 미구현) ⚠️

⚠️ **B-1 over-claim 정정 (60 cascade 재발, 4 source + Reviewer verify CONFIRMED)**:
- **현 R-6 (r2-canary.yml) = "R-4.1 Tier-1 42 catalog canary regression"** (nightly cron `0 18 * * *` + PR). paths trigger = `docker/r4-1-poc` + `docker/r2-poc` + canary-recheck-design.md + workflow. **`hermes-version.yaml` / Hermes dependency lock diff trigger 0** → **Hermes native redaction egress 자동 회귀 *아님*** (우리 Tier-1 catalog canary).
- **ADR-011 §2.3 #4 + governance §1.2.7 Layer 1 = Hermes 의존성 변경 시 R-2/R-4.1 자동 재실행 *의무 요구***. 단 **현 R-6 = Tier-1 catalog canary까지만 operative** (Hermes dependency lock trigger 미구현 = 잔여 작업).

→ **현 operative = Tier-1 42 catalog silent 깨짐 자동 검출 ✅ / Hermes upstream 변경 자동 회귀 = ADR 의무 요구, 미구현 (R-6 확장 잔여)**. R-1 자동 보증 착시 제거 (R-6 ≠ Hermes egress canary).

### §2.4 축 4 — 위임 권위 (ADR-011 §2.3 #2) ✅

- ADR-011 §2.3 #2: "Hermes 자체 redaction 은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0".
- ⚠️ **Hermes ≠ root of trust** (권위 위계): Hermes 출력은 Tools (canary/R-6)로 검증 → 위임 ≠ 맹신 (R-6 자동 회귀가 위임 위에 위치).

→ **R-1 = ADR 권위로 위임된 영역** (본 repo 재구현 불요), 위임 실효 = 축 1+2+3 검증.

---

## §3 Evidence Contract (version pin + R-6 + SOP)

R-1 위임 검증의 *지속 유효성* contract (64 §3.3 evidence contract 의무 답습):

| # | contract | 현 상태 | 본 cycle |
|---|----------|------|------|
| C-1 | **version pin v0.12.0** | governance §1.2.7 P11/Layer 1 **문서 명문** (hermes-version.yaml 파일 부재 = enforcement 미실체) | contract 명문 수준 (파일화 enforcement = 절충안, 별도) — R-4 정정 |
| C-2 | **Tier-1 catalog 회귀** | r2-canary.yml operative (nightly + PR, Tier-1 42 canary) | 답습 유지 (변경 0) |
| C-3 | **격리 실행 SOP** | day2-r1 §7 R-2 PoC 절차 + docker/r2-poc 골격 (B-3) | SOP 명문 (실 실행 deferred, §4) |
| C-4 | **Hermes 의존성 변경 trigger** | ADR-011 §2.3 #4 + governance Layer 1 = **의무 요구 (미구현 = R-6 확장 잔여)** | 답습 유지 (B-1) |
| C-5 ⭐ | **HERMES_REDACT_SECRETS=true 활성화 검증** (B-2) | R-4 line 138 = 기본 false opt-in | 활성화 config 검증 의무 명문 (위임 실효 전제) |

⭐ **격리 실행 SOP (C-3, artifact 재확보 시 실행 절차)**:
1. Hermes upstream v0.12.0 re-clone (⚠️ **clone URL 출처 확보 선결** — day2-r1 §3.1 = grep 명령 (URL 아님), ADR-008 미확인, B-3)
2. `HERMES_REDACT_SECRETS=true` 활성화 (C-5 전제) + 격리 환경 (Docker, docker/r2-poc 골격 답습) canary 주입 (`sk-ant-CANARY-XXXXX` 등 Tier-1 대표 패턴)
3. Hermes redaction 경로 (로그/송신) 통과 → `[REDACTED]` 또는 부분 마스킹 확인
4. Tier-1 42 catalog 대표 패턴 커버 검증 (R-4 §5 답습)
5. evidence = canary-output.log + 적용 결과 (r2-canary.yml artifact 형식 답습)

---

## §4 실 격리 canary 실행 deferred 정당화

⚠️ **현 상태**: Hermes `agent/redact.py` artifact 부재 (/tmp/hermes-phase0 휘발 + 본 repo 부재) + Hermes upstream clone URL 문서 미명시. **단 R-2 PoC 격리 골격 `docker/r2-poc/` 존재** (Dockerfile + compose + r2_poc.py, B-3 — "artifact 완전 부재" 아님, 우리 PoC 골격은 보존) → Hermes native 실 격리 canary 실행 *미시행*.

**deferred 정당화 (day2-r1 선례 답습)**:
- day2-r1 §3.2 "PoC 미시행 정당성": 코드 분석 (docstring + grep + 시그니처)만으로 **결정적 결론** — "PoC 는 동일 결과 확인이며 시간·환경 비용 대비 추가 정보 가치 0".
- 본 SC-2 = 위치 (day2-r1 ✅) + 동등성 (R-4 §5 ✅) + 자동 회귀 (R-6 ✅) **코드/문서 분석 기반 검증**. 실 격리 canary = 동일 결론 강화 (가치 보강이나 결론 변경 0).
- ⚠️ **단 over-claim 경계**: 본 검증 = "코드/문서 분석 기반" 명시. 실 격리 canary 실행 = artifact 재확보 시 C-3 SOP 실행 (강한 보강 evidence). "실 실행 완료" 주장 0.

→ **R-1 위임 검증 = 코드/문서 분석 기반 충족** (day2-r1 동형). 실 격리 canary = deferred (C-3 SOP, artifact 재확보 trigger).

---

## §5 R-1 prong 충족 판정 + over-claim 경계

⭐ **판정 = R-1 위임 검증 *조건부/문서 기반 충족* (Exit (a) Hermes-native sub-evidence, R-1+codex reframe)**:
- 축 1 위치 ✅ (활성화 전제) + 축 2 동등성 ✅ + 축 3 = **현 Tier-1 canary operative / Hermes 자동 회귀 의무 미구현** + 축 4 권위 ✅.
- governance §4.5 (a) "Hermes native redaction Tier-1 42 catalog 적용 검증" = **Exit (a)의 Hermes-native sub-evidence 조건부 충족** (축 1+2, 활성화 전제 + R-6 Tier-1 한정 + 위치 시점성 + URL 불명). GP-2 Exit (b) 격리 PoC / (d) R-6 log canary step = SC-3 또는 별도 (R-3 경계).

⚠️ **over-claim 경계 (4 source 검증 + reframe)**:
- **R-1 위임 검증 ≠ Hermes 안전성 선언** (ADR-011 §7.3). "활성화된 Hermes 가 GP-2 영역에 redaction 적용 + Tier-1 동등 이상 커버" *사실* 검증.
- **조건부/문서 기반 충족** (실 격리 canary 실행 deferred, 활성화 전제, R-6 Tier-1 한정) — day2-r1 동형, "실 실행 완료" 0, "Hermes 자동 회귀 operative" 0.
- **full GP-2 PASS ≠ 본 cycle** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) → SC-3 발효 합의 (별도).

→ **full GP-2 PASS Exit (a) = R-1 prong (SC-2 조건부/문서 기반) + R-2 prong (SC-1 ✅ in-repo operative) → SC-3 발효 자격** (실 격리 canary + Hermes 자동 회귀 R-6 확장 = SC-3 강한 보강 또는 별도 trigger).

---

## §6 합의 형태 + 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+

**정당화**: full GP-2 PASS Exit (a) R-1 prong (보안 영역) + 큰 결정 (위임 검증 milestone) + 5조-2 cross-vendor + Hermes ≠ root of trust (다중 검증 의무).

### §6.2 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | 큰 결정 (full GP-2 PASS R-1 prong) | ✅ |
| 2 | 보안 (GP-2 prevention 위임) | ✅ |
| 3 | 외부 LLM cross-vendor (5조-2) | ✅ |
| 4 | Hermes 위임 검증 (≠ root of trust 다중 검증) | ✅ |

→ **4/4 발화 → 풀 3+1 + 외부 LLM 1+**.

---

## §7 금지 사항

§0.2 답습 (10). 추가: Hermes 안전성 선언 0 / 실 격리 canary "실행 완료" 주장 0 / agent/redact.py import 0 / full GP-2 PASS 발효 0 / hermes-version.yaml 파일 생성 0 (절충안 deferred) / 자동 SC-3 진입 0.

---

## §8 Rollback Trigger

| # | trigger | 대응 |
|---|---------|----|
| RT-1 | Hermes upstream v0.12.0 redaction silent 깨짐 | R-6 자동 재실행 (r2-canary.yml) + R-5 canary 재검증 |
| RT-2 | 실 격리 canary 실행 시 day2-r1 결론과 불일치 | C-3 SOP 실행 결과 우선 → R-1 위임 검증 재평가 (코드 분석 < 실 실행) |
| RT-3 | Hermes 의존성 변경 (hermes-version.yaml drift) | governance Layer 1 (lock diff → R-2/R-4.1 재실행 + merge BLOCK) |
| RT-4 | "Hermes 안전성 선언" over-claim 발생 | §5 over-claim 경계 명문 (위임 검증 ≠ 안전 선언) |

---

## §9 Evidence

- E-1: day2-r1 위치 검증 (Hermes redaction = GP-2 영역, 25 import 비-DB)
- E-2: R-4 §5 동등성 (Hermes 47 ⊇ Tier-1 45)
- E-3: r2-canary.yml R-6 operative (nightly + PR)
- E-4: ADR-011 §2.3 #2 위임 권위 + #4 자동 회귀
- E-5: C-3 격리 실행 SOP (artifact 재확보 시, deferred)

---

## §10 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | "Hermes 안전성 선언" over-claim | §0 + §5 — 위임 *검증* (사실) ≠ 안전 선언 (ADR-011 §7.3), [[feedback_pass_scope_overclaim]] |
| P-2 | day2-r1 "FAIL" 을 GP-2 위임 부정으로 오인 | §2.1 — "FAIL" = G1a (DB) 맥락, GP-2 (송신) 적용 ✅ (모순 0) |
| P-3 | 실 격리 canary 미실행 → 검증 미충족 오인 | §4 — day2-r1 "코드 분석 충분" 선례 + deferred 명문 ("실 실행 완료" 0) |
| P-4 | full GP-2 PASS 기정사실화 | §5 — R-1 ∧ R-2 → SC-3 별도 (§0.2 #2) |
| P-5 | R-4 설계 동등성을 prevention 입증으로 격상 | §2.2 — R-4 = 패턴 *포함* 사실 (§7.3 안전성 선언 금지) |
| P-6 | 작성자 = 64/65 작성자 (Claude) cascade | cross-vendor codex + 풀 3+1 독립 검증 |
| P-7 | hermes-version.yaml 파일 부재 = contract 미충족 오인 | §3 C-1 — governance 명문 답습 (파일화 = 절충안 별도), contract 명문 유효 |

---

## §11 v1.1 흡수 매트릭스 (BLOCKING 4 + 권고 4 reframe)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-sc2.md` 답습 1pass reframe 흡수 (60 detection reframe 동형). **4 source 전원 APPROVE WITH CONDITIONS** (codex BLOCKING 0 조건3 + Agent A 2 + Agent B 2 + Agent C 3). **60 over-claim cascade 재발** — 4 source가 R-6/activation framing over-claim 포착 (본 세션 #3 첫 cascade). evidence 실증 (위치+동등성), framing 정정.

| # | 흡수 | source | 정정 위치 |
|---|------|--------|------|
| B-1 ⭐ | 축 3 R-6 자동 회귀 over-claim → "현 R-6 = Tier-1 42 catalog canary operative / Hermes dependency lock trigger 미구현 (ADR 의무 요구)" (Reviewer verify: r2-canary = R-4.1 Tier-1 canary) | codex+A+B+C (Reviewer CONFIRMED) | §2.3 + C-4 |
| B-2 ⭐ | HERMES_REDACT_SECRETS opt-in (기본 false) → "활성화된 Hermes redaction" + C-5 활성화 검증 전제 신설 | codex+A+B | §2.1 + §3 C-5 |
| B-3 | artifact 부재 완화 (docker/r2-poc 골격 존재) + Hermes clone URL 출처 불명 (day2-r1 §3.1 ≠ URL) | Agent C (Reviewer 부분 정정) | §3 C-3 + §4 |
| B-4 | 위치 evidence 시점성 (2026-05-05 day2-r1, artifact 재확인 = C-3) | Agent A | §2.1 |
| R-1 | "R-1 prong 충족" → "Exit (a) Hermes-native sub-evidence 조건부/문서 기반 충족" | codex 3 | §5 + title |
| R-2 | 동등성 출처 = R-4 §5 + R-4.1/R-6 catalog 체계 | codex 4 | §2.2 |
| R-3 | GP-2 Exit (b)/(d) = SC-3 또는 별도 (R-1 prong 경계) | codex 3 | §5 |
| R-4 | version pin = 문서 명문 vs 파일 enforcement 구분 | codex NOTE | §3 C-1 |

**4 source 정합 (positive)**: over-claim 1차 경계 (Hermes 안전성 선언/full GP-2 PASS 격상/실 실행 완료 주장) 견고 / day2-r1 FAIL 재해석 타당 (G1a DB ≠ GP-2 송신, 4 source 공통) / R-2 prong (SC-1) 발효 filesystem 실측 / 권위 인용 일치 (codex 6/8, R-6 dependency trigger 부분만).

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → **R-1 위임 검증 조건부/문서 기반 충족 (활성화 전제 HERMES_REDACT_SECRETS=true + R-6 Tier-1 한정 + 위치 시점성)**. 후속: **SC-3 (full GP-2 PASS 발효 합의)** — R-1 (SC-2 조건부) ∧ R-2 (SC-1 in-repo) + 실 격리 canary + Hermes 자동 회귀 R-6 확장 보강 = 사용자 명시 별도 cycle.
