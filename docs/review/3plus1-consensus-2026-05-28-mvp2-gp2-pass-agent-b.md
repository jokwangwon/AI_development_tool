# 3+1 합의 — Agent B (품질/안전성 검증가) — MVP-2 GP-2 송신 redaction PASS 발효 (60 entry)

> **검토 대상**: `docs/phase0/mvp2-gp2-pass-activation-brief.md` (v1)
> **관점**: "안전하고 견고한가? GP-2 PASS 가 정당한가?" — 보안, 권위 정합성, means-vs-ends
> **작성**: 2026-05-28 / **검토자**: Agent B (품질/안전성)
> **독립성**: Agent A/C 및 외부 LLM 응답 미참조

---

## verdict: **APPROVE WITH CONDITIONS**

핵심 판단: GP-2 PASS = **detection (R-3) operative + 설계 권위 + 패턴 동등성** 으로 GP-2 §4.5 Exit (a)~(d) 를 **정당하게 충족**한다. (d) "자동 회귀 검증 경로" 는 본질이 *detection* 이므로 R-3 단독으로 충족됨이 권위 정합. prevention (R-1/R-2) deferred 는 brief 가 §3.2 + (C-1) 에서 honest 하게 명시 — detection-as-prevention 과장 0. base64 (R-5) known limitation 도 fixture + workflow line 13 으로 명문화. **단 BLOCKING 1건** — Layer 2a DEFER 와의 동형 주장이 **구조적으로 비대칭** (DEFER 된 ends 의 in-repo cover 유무 차이) 이며, 이를 명문화하지 않으면 보안 결과 over-claim 위험. 이를 명시하면 APPROVE.

---

## BLOCKING

### R-B-1 — Layer 2a DEFER 동형 주장의 **구조적 비대칭** 명문 누락 (보안 결과 over-claim 위험)

**위치**: brief §3.2 line 108, §6 (C-1) line 160, §10 P-2

**근거**:
brief 는 R-1/R-2 prevention deferred 를 **"59 Layer 2a DEFER 패턴 동형"** 으로 반복 주장한다 (§0.1 #2, §3.2 line 108 "59 Layer 2a 'operative 보호 = 다른 layer, 본 layer DEFER' 패턴 동형", §10 P-2). 그러나 두 DEFER 는 **보안 결과 측면에서 구조적으로 다르다**:

- **59 Layer 2a DEFER (실제 cross-check)**: `docs/phase0/mvp2-layer-124-pass-activation-brief.md` §2.2 line 105 + §4.1 line 166 (N-1 정정) — Layer 2a (denyNonFastForwards) 를 DEFER 했으나, 그 **ends (history rewrite/force-push 차단) 가 in-repo 다른 2 operative layer 로 이중 cover** 됨: (1) Layer 2b branch protection (operative) + (2) `rewrite-defense.yml` CI (actual run green). 근거 = "ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거**, 단일 수단 종속 0" (line 166). 즉 **DEFER 된 layer 가 막으려는 시나리오를 in-repo 2 layer 가 이미 cover** — 잔여 보안 hole 0.

- **GP-2 R-1/R-2 DEFER (본 brief)**: R-1 (Hermes native redaction) + R-2 (facade real) = GP-2 의 **유일한 prevention (능동 redaction) means**. R-3 는 *detection* (사후 회귀 검증) 이지 prevention 이 아니다. R-1/R-2 deferred 시 **prevention 의 ends (송신 직전 능동 secret redaction) 를 in-repo 에서 cover 하는 다른 operative layer 가 0** — 능동 redaction 의 실행은 전적으로 Hermes upstream runtime (본 repo 외부) 에 의존. 즉 **59 의 "이중 cover" 구조가 GP-2 에는 부재**.

이는 57 (β) 결정 본문과도 충돌 신호이다 — `docs/phase0/mvp2-beta-submeans-decision-brief.md` line 135: "**MVP-2 PASS 시점 GP-2 (a)~(e) 충족 = R-3 actual run PASS (detection) + R-1/R-2 evidence 가용 시점 (prevention) 합산**". 즉 57 (β) 는 prevention 을 *MVP-2 PASS 시점에 합산* 하도록 명시했다. 본 brief 는 이를 "**GP-2 PASS** (MVP-2 PASS 와 별개) = DESIGN repo PASS = detection-only 로 충족" 으로 carve-out 한다. 이 carve-out 자체는 정당할 수 있으나 (DESIGN/governance repo = 능동 redaction runtime 부재가 본질적), **59 와 동형이라는 framing 은 부정확** — 59 는 ends 가 in-repo cover 됐고, GP-2 prevention ends 는 in-repo cover 0 (upstream 의존).

**보안 함의**: GP-2 의 ends = "secret 송신/로그 leak 0". 본 repo PASS 발효 시점에 능동 redaction 이 in-repo 에 0 이면, **본 repo 자체로는 leak 차단의 능동 보증이 없고 detection (사후 회귀) + upstream 신뢰** 에만 의존. ADR-011 §2.3 #2 (verbatim line 113: "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰") 가 이 upstream 신뢰를 *권위로 허용* 하므로 PASS 자체는 정당하나, "Layer 2a 동형 (이중 cover)" framing 은 보안 결과를 실제보다 강하게 표현한다.

**정정**:
1. §3.2 / (C-1) / P-2 에서 "59 Layer 2a DEFER 동형" 주장을 **부분 동형 (DEFER 의사결정 형식만 동형, 보안 cover 구조는 비대칭)** 으로 강등 명문. 구체: "59 Layer 2a = DEFER 된 ends 가 in-repo 2b+CI 이중 cover (잔여 hole 0). GP-2 R-1/R-2 = DEFER 된 prevention ends 의 in-repo cover **0** — 능동 redaction 실행은 Hermes upstream (본 repo 외부) 단독 의존, detection (R-3) 은 사후 회귀이지 prevention cover 아님" 명시.
2. **GP-2 PASS = MVP-2 PASS 아님** 을 보안 결과 측면에서 명문: 본 GP-2 PASS 는 *DESIGN/governance repo 의 detection operative + 설계 권위 + 패턴 동등성* 한정 충족이며, **runtime prevention 의 ends 충족 (R-1/R-2 합산) 은 57 (β) line 135 답습으로 MVP-2 Implementation Evidence PASS / 실 runtime 시점으로 명시 이월**. 즉 "본 repo GP-2 PASS ≠ secret 송신 leak 0 의 능동 보증" 을 정직하게 분리.

이 명문이 추가되면 보안 over-claim 위험 해소 — verdict 는 APPROVE.

---

## 권고 (N-B-N)

### N-B-1 — (e2) 표기 = 프로젝트 내부 label 임을 §4 본문에도 명시 (59 B-2 답습 완결성)

**위치**: brief §0.1 #3, §0.3 line 50, §2 (e2) row, §4 (e2) row, §10 P-7

**근거**: ADR-011 / ADR-012 본문 cross-check 결과 **"(e2)" 문자열은 ADR-011·ADR-012 어디에도 부재** (grep 확인 0건). ADR-011 §2.1 = 명시적으로 **(a)~(d) 4조건** (line 52~61, (e) 미포함). ADR-012 §4 = "(a)~(d) **+ (e)** 5조건 답습" (line 436 header + §4 (e) line 478 "(e) 합의 APPROVE"). 즉 "(e2)" 는 59 brief 가 도입한 **프로젝트 내부 label** ("PASS 발효 합의 APPROVE" = entry-step-2 의미) 이며, ADR-012 의 literal "(e)" 와 *대응* 시킨 것. brief §4 header "(e2) ADR-012 §4 확장" + §0.3 line 50 "(e2) 권위" 는 59 B-2 정정 (59 brief line 147 "B-2: ADR-011 §2.1 = (a)~(d) 4조건만, (e2) = ADR-012 §4 확장") 과 **framing 일치** — 즉 권위 전도 0 (59 B-2 전례 정확히 답습). 단 §4 본문 표가 "(e2) | ADR-012 §4 확장" 으로만 표기되어, 독자가 "(e2)" 를 ADR-012 verbatim 으로 오인할 잔여 위험. (e2) = 본 프로젝트 PASS-발효 label, ADR-012 의 verbatim 은 "(e)" 임을 §4 각주 1줄로 명문 권고.

**판단**: 권위 인용 정확성 (임무 #2) = **PASS** (over-claim 0, 전도 0). 다만 label 출처 1줄 보강 = 완결성 권고 (BLOCKING 아님 — 59 B-2 framing 정확 답습이 이미 §0.3 + §4 header + P-7 3곳에 존재).

### N-B-2 — ADR-011 §2.3 #2 인용 verbatim 정확성 = PASS, 단 §1.2 약식 표현 정밀화

**위치**: brief §1.2 line 73, §2 (c), §4 (c)

**근거**: ADR-011 §2.3 운영 함의 #2 verbatim (line 113) = "**Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음." brief §1.2 line 73 인용 = "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 차단 책임 0" — **verbatim 정확** (의미 보존, "0" = "없음" 표기 차이만). (c) 조건 충족 정합. 단 §1.2 line 73 의 "(DB INSERT = GP-1 책임)" 는 ADR-011 §2.3 #3 (line 114 "DB INSERT 경로는 Hermes 외부에서 별도 보호") + governance §4.1 line 424 ("DB INSERT 차단은 GP-1 의 책임") 답습 — 정확. 인용 정확성 추가 BLOCKING 0.

### N-B-3 — (d) 격상 (51 "gap" → 본 brief "✅") = detection 본질 정합으로 정당, over-claim 0

**위치**: brief §2 (d), §10 P-3

**근거**: 51 audit (`docs/phase0/mvp2-entry-eligibility-audit-brief.md` line 127) = "(d) ❌ gap — R-6 workflow 에 log file canary inject step 추가" 로 표기. 본 brief 는 이를 "(d) ✅ — secret-hygiene D-2 step 이미 운영" 으로 격상. **filesystem cross-check 결과 정당**:
- `.github/workflows/secret-hygiene-egress-redaction.yml` D-2 step (line 165~212) = `secret_scanner.py --mode scan-log` 으로 redaction residual 검출 — 실재.
- `tools/secret_scanner.py` line 275 `--mode scan-log` = redaction marker (`[REDACTED]` 등) 제외 후 잔존 secret 검출 — 실재 (line 184 marker exclusion).
- `redaction_pass/env_redacted.txt` (rc=0 잔존 0) + `redaction_fail/partial_redact.txt` (rc=1, `sk-FAK[REDACTED]` prefix 잔존 leak 검출) — fixture 실재 검증.

GP-2 §4.5 Exit (d) = "자동 회귀 검증 경로" 는 **본질이 detection (사후 회귀)** 이므로, R-3 detection 단독으로 (d) 충족이 권위 정합 — prevention 부재가 (d) 충족을 훼손하지 않음. 51 "gap" 표기는 *PoC 시제 발견 전* 의 audit 시점 기준이었고, 52 entry "PoC 시제 발견 동형" 정정 패턴 답습. **detection-as-prevention 과장 0** — brief 가 (d) 를 detection 으로 정확히 분류 (§3.1 R-3 = detection, §3.2 prevention = R-1/R-2 별도). 임무 #3 = PASS.

### N-B-4 — actual run evidence 의 freshness 한계 = 정직 명문, 단 schedule run 재확인 권고

**위치**: brief §2 (d) line 85, §6 (C-3) line 162

**근거**: brief 는 actual run `26517803107` (headSha `4fec6485`) 을 evidence 로 인용 + workflow_dispatch 미지원 → fresh run 은 schedule (cron `0 3 * * *`) 또는 path 변경 시만 발화 명시. cross-check:
- workflow `on:` (line 23~64) = `push.paths` + `pull_request` + `schedule` cron — **workflow_dispatch 부재 확인** (정직).
- `git log` 확인 = workflow + `secret_scanner.py` + `redaction_pass`/`redaction_fail` fixtures 의 마지막 변경 = `4fec648` (49 entry). **49 entry 이후 변경 0 (불변) 확인** — "코드 불변 → 최근 green run = 현 코드 유효 evidence" 논리 정당.

다만 인용 run (`26517803107`) 이 headSha `4fec6485` 시점 = 본 cycle commit (`feature/jarvis-mvp0` HEAD = `de4e2c8`) 과 시차 존재. 코드 불변이므로 보안 결과 동일하나, GP-2 PASS 발효 commit 직후 schedule (cron) run 1회 green 재확인을 (C-3) 에 *권고* 로 추가 (BLOCKING 아님 — 코드 불변 + actual run 실재로 evidence 유효).

### N-B-5 — base64 (R-5) known limitation = 정당한 영구 분리 (G3-4 답습), 단 ends 잔여 위험 1줄 명문

**위치**: brief §4.1, §10 P-5

**근거 (임무 #4 판단)**: R-5 (base64/URL/압축 evasion) 미검출 = `base64_evasion.txt` fixture (line 5 `encoded_canary=c2st...`) + workflow line 13/205~209/749/807 으로 명문화. 질문: "base64 secret 이 송신되면 GP-2 ends 위반 아닌가?" — **형식적으로는 맞다** (base64 인코딩된 secret 이 송신되면 평문 leak 의 변종). 그러나:
1. R-3 detection 은 **redaction residual 검출** 이지 능동 차단이 아니므로, base64 미검출 = detection 의 catalog 한계 (Tier-1 42 평문 prefix/regex). 능동 prevention (R-1 Hermes) 의 base64 처리는 별도.
2. base64 evasion 의 실 차단 = Hermes upstream R2-6 영역 (governance §4.3 line 436 "base64 evasion test (R2-6)" 답습) — 본 repo 외부.
3. G3-4 MVP-2/3 분리 = base64 = advanced evasion class 로 MVP-3 영역 (57 (β) line 131 "R-5 = 영구 분리, MVP-2/3, G3-4" 답습).

따라서 GP-2 PASS scope = "Tier-1 42 catalog **평문** redaction residual 검출" 한정 명문 (brief §4.1 line 128) = 정당. **단 R-1 R-B-1 정정과 연동** — GP-2 ends ("송신 leak 0") 의 base64 변종 잔여 위험은 (detection catalog 한계 + prevention upstream 의존) 이중으로 in-repo cover 0 임을 §4.1 에 1줄 명문 권고 (정직성 강화). 영구 분리 자체 = 정당.

### N-B-6 — scope 침입 = 0건 확인 (임무 #5 PASS)

**근거**: brief §0.2 (12 비위반 표) + §7 (금지) cross-check 결과 scope 침입 0:
- MVP-2 PASS *발효* 자체 = §0.2 #2 + §8 #2 별도 cycle 명시 (침입 0).
- R-1 Hermes import 결정 = §0.2 #3 + §3.1 (R-1 ❌ 본 repo 부재, import 결정 별도) (침입 0).
- R-2 facade real (TR-1) = §0.2 #4 + §3.1 (R-2 facade placeholder, deferred trajectory) (침입 0).
- R-5 evasion 진입 = §0.2 #5 + §4.1 (known limitation, 영구 분리) (침입 0).
- R-S1 정정 = §0.2 #7 + §5.2 trigger 4 "부분" + §6 #3 (GP-2 PASS 비차단, MVP-2 PASS 전 hard gate 별도 cycle) (침입 0).
- secret_scanner.py / workflow 본문 변경 = §0.2 #10 "0 (PoC 시제 보존)" (침입 0, git log 불변 확인 일치).

---

## NOTE (NT-B-N)

### NT-B-1 — DESIGN repo PASS 의 보안 의미론 = 본질적 정당 (P-4 답습)

본 repo = DESIGN/governance repo (docs + tools + CI) 라는 성격상, 능동 runtime redaction 이 in-repo 에 부재한 것은 *결함이 아니라 본질*. brief §1.2 + §3.2 + P-4 가 이를 명시. ADR-011 §2.3 권위 위계 (line 102~108: Constitution > ADR > SDD > Harness Gates > Hermes > Worker) 상 Hermes 는 *검증 대상* 이지 root of trust 아님 — 따라서 본 repo 의 GP-2 PASS = "Hermes 출력을 검증하는 detection layer (R-3) + 설계 권위 + 패턴 동등성" 충족이 권위 정합. R-B-1 정정은 이 정당성을 부정하는 것이 아니라, *59 동형 framing 의 보안 cover 비대칭* 만 정직화하는 것.

### NT-B-2 — means-vs-ends 정합 종합 판단 (임무 #1)

GP-2 ends = "secret 송신/로그 leak 0". 본 GP-2 PASS 가 충족하는 것:
- **detection ends (사후 회귀)** = R-3 operative ✅ (in-repo, actual run green).
- **prevention ends (능동 redaction)** = R-1 (Hermes upstream runtime, 본 repo 외부) + R-2 (facade real deferred) — **in-repo cover 0, upstream 신뢰 (ADR-011 §2.3 #2 권위 허용)**.

→ GP-2 §4.5 Exit (a)~(d) 는 **detection + 설계 권위 + 패턴 동등성** 으로 충족되며, 이것이 GP-2 가 "ADR-011 §2.3 #2 의 *보조* 역할" (governance §4.1 line 424 "GP-2 단독으로 헌법 8조 본질 충족 시도 금지") 이라는 권위와 정합. **GP-2 PASS 가 prevention 부재로 보안 hole 인가?** → 아니다. (d) 는 detection 본질이고, prevention 의 ends 책임은 ADR-011 §2.3 #2 가 upstream 으로 위임. **단 그 위임 사실 (= in-repo 능동 보증 0) 을 정직하게 명문 (R-B-1)** 해야 over-claim 0.

### NT-B-3 — 메타-편향 회피 (P-6) 적정

brief 작성자 = 57/59 작성자 (Claude) cascade 위험 → cross-vendor codex (E-α) + 풀 3+1 독립 검증 명시 (P-6). 본 Agent B 검토 = 독립 cross-check (Agent A/C/외부 LLM 미참조) 수행. R-B-1 = 본 Agent B 가 독립 발굴한 보안 cover 비대칭 (59 brief 답습 framing 의 정밀화) — cascade over-claim 의 실 사례 식별로 P-6 청산 매커니즘 작동.

---

## 종합

| 임무 | 판단 |
|------|------|
| #1 means-vs-ends 보안 (detection vs prevention) | (d) = detection 본질, R-3 단독 충족 정당. prevention 부재 = 보안 hole 아님 (ADR-011 §2.3 #2 upstream 위임). **단 59 동형 framing 비대칭 명문 의무 (R-B-1)** |
| #2 권위 인용 정확성 | PASS — (e2) = 프로젝트 label (59 B-2 정확 답습, 권위 전도 0), ADR-011 §2.3 #2 verbatim 정확, ADR-011 §2.1 = (a)~(d) 정확. (N-B-1 label 출처 1줄 보강 권고) |
| #3 (d) detection-as-prevention 과장 | PASS — brief 가 detection 으로 정확 분류, 과장 0 (N-B-3) |
| #4 R-5 base64 known limitation | 정당 (G3-4 영구 분리). ends 잔여 위험 1줄 명문 권고 (N-B-5) |
| #5 scope 침입 | 0건 (N-B-6) |

**verdict: APPROVE WITH CONDITIONS**
**BLOCKING: 1건** (R-B-1 — Layer 2a DEFER 동형 주장의 구조적 비대칭 명문)
**권고: 5건** (N-B-1 ~ N-B-5, N-B-6 = scope 확인) · **NOTE: 3건**

R-B-1 (보안 cover 비대칭 정직화) 명문 시 GP-2 송신 redaction PASS 발효 APPROVE. 권위 인용 정확 + detection-as-prevention 과장 0 + scope 침입 0 = 발효 자격의 보안 측면 충족.
