# 3+1 합의 — Agent B (품질/안전성 검증가) — Layer 1+2+4 통합 PASS 발효 (e2) (59 entry)

> **관점**: "안전하고 견고한가? PASS 발효가 정당한가?" — 보안, 권위 정합, means-vs-ends
>
> **대상**: `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (v1, §0~§11)
>
> **독립성**: Agent A/C + 외부 LLM 응답 미참조. 권위 문서 + filesystem + gh api + CI run direct verify 기반.
>
> **작성**: 2026-05-28

---

## verdict: **APPROVE WITH CONDITIONS**

PASS 발효의 **핵심 보안 판단 (2a DEFER 가 hole 인가) = hole 아님** (means-vs-ends 정합 확인, 아래 §1). 권위 인용 = 대체로 정확하나 **§3/§10 헤더의 "ADR-011 §2.1 (a)~(e2)" 표기가 (e)/(e2) 를 ADR-011 §2.1 본문에 귀속 (실제 (e) = ADR-012 §4 확장 패턴)** — (β) cycle B-3/B-4 권위 전도 전례 동형의 인용 정밀도 BLOCKING 1건. 나머지 evidence/CI/branch protection 주장은 전수 verify 통과.

- **BLOCKING: 1** (R-B-1 권위 인용 정밀도)
- 권고: 3 (N-B-1~3)
- NOTE: 4 (NT-B-1~4)

---

## §1 means-vs-ends 정합 — 핵심 보안 판단 (2a DEFER) ✅ hole 아님

### §1.1 질문: GitHub branch protection 이 local denyNonFastForwards 와 동등한 append-only 보호를 제공하는가?

**직접 verify (gh api repos/jokwangwon/AI_development_tool/branches/main/protection, 2026-05-28)**:

```
"allow_force_pushes": {"enabled": false}
"allow_deletions":    {"enabled": false}
"enforce_admins":     {"enabled": true}
"required_status_checks.contexts": ["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"] (8)
"required_signatures": {"enabled": false}
"required_linear_history": {"enabled": false}
```

→ brief §2.3 E-PASS-7 "force push/delete false + 8 contexts" = **gh api actual state 와 verbatim 일치**. `enforce_admins: true` (admin 도 우회 불가) 까지 확인 — brief 가 명시 안 했으나 보호 강도 *상향*.

### §1.2 means-vs-ends 판정 (ADR-011 §2.1 (a) "동등 이상 보안 결과")

ADR-012 §2.3 **Layer 2 = 단일 MANDATORY layer** 로, 4 sub-수단 (`denyNonFastForwards` + `branch protection rule` + `pre-commit hook` + `CI 회귀 검증`) 을 *동시* 열거 (line 171~175 verbatim verify). 즉 ADR-012 §2.3 자체가 Layer 2 의 *목적 (append-only history)* 을 **다중 수단** 으로 달성하도록 설계 — 단일 수단 (`denyNonFastForwards`) 종속이 아님.

**append-only 목적 (ends) 의 operative 충족 = 2 독립 layer**:

| 수단 (means) | 상태 | append-only ends 기여 |
|------------|------|---------------------|
| Layer 2a `denyNonFastForwards` (local) | ⚠️ DEFER (컨테이너 미배포) | local push reject — **현재 미작동** |
| Layer 2b GitHub branch protection (`allow_force_pushes:false` + `allow_deletions:false`) | ✅ operative | **remote force-push/delete 차단** |
| Layer 4 CI `rewrite-defense.yml` (`--mode append-only`) | ✅ operative (actual run `26557460227` green) | **`non_fast_forward_detected` + `history_reorder_detected` 검출** (CI step `L2 FAIL` — force-push/reorder fixture rc=1) |

→ **핵심 발견**: `rewrite-defense.yml` 가 *force-push 자체* (`non_fast_forward_detected`) 와 *history reorder* (`history_reorder_detected`) 를 Layer 4 CI 에서 직접 검출 (grep verify, workflow line 128~162). 즉 2a 가 막으려는 *바로 그 시나리오* (non-fast-forward) 가 2b (remote 차단) + Layer 4 (CI 검출) 두 layer 로 **이중 cover**.

**판정**: 2a DEFER 는 보안 hole **아님**. append-only *결과* (ADR-011 §2.1 (a)) 는 2b (remote 강제 차단) + Layer 4 CI (force-push/reorder 검출) 로 operative 충족. 비례 보안 ([[feedback_proportionate_security_personal_tool]]) 관점에서 solo GitHub repo + 컨테이너 미배포 상태에 per-repo local config 강제 = ceremony — DEFER 정당.

### §1.3 단, brief 가 *과소 주장* (NT-B-1 로 분리)

brief §2.2/§4.1 은 2a DEFER 의 근거로 **2b 만** 인용 ("GitHub branch protection (Layer 2b) 이 operative 보호 제공"). 그러나 더 강한 근거 = **Layer 4 `rewrite-defense.yml` 가 non_fast_forward_detected 검출** (2b 가 GitHub 설정 변경/우회 시에도 CI 가 base branch 대비 검출). brief 가 이 2번째 operative layer 를 누락 — 보안 *과대* 가 아니라 *과소* 주장이므로 BLOCKING 아님. NT-B-1 보강 권고.

→ **§1 결론: 2a DEFER = means-vs-ends 정합 (hole 0). PASS 발효 핵심 보안 판단 = APPROVE.** P2 "evidence gap 은폐" 위험 = 해당 없음 (오히려 honest under-claim).

---

## §2 권위 인용 정확성 — (β) B-3/B-4 전례 비판적 검증

(β) cycle (57 entry, `3plus1-consensus-2026-05-28-mvp2-beta.md` B-3/B-4) 에서 "R-1 MANDATORY (ADR-011 §2.3 #2)" 권위 전도 + "ADR-012 §2.1 = 의존성 trigger" misattribution 발견 전례. 본 brief 동일 패턴 비판적 verify.

### §2.1 ⛔ R-B-1 (BLOCKING) — "ADR-011 §2.1 (a)~(e2)" 헤더가 (e)/(e2) 를 ADR-011 §2.1 에 귀속

**verify (ADR-011 §2.1 line 52~61 verbatim)**:

```
| (a) | 동등 이상의 보안 결과 | ...
| (b) | 격리 환경 PoC로 실증   | ...
| (c) | ADR 권위로 명시       | ...
| (d) | 자동 회귀 검증 경로 확보 | ...
```

→ **ADR-011 §2.1 = (a)~(d) 4조건만 존재. "(e)" 는 ADR-011 §2.1 본문에 없음.** "(e) 합의 APPROVE" 는 **ADR-012 §4 "(a)~(d) + (e) 5조건 답습"** (line 436, 478~480) 에서 도입된 *답습 확장 패턴* — ADR-011 §2.1 의 조항이 아니라 ADR-012 가 만든 매핑.

**brief 의 처리 = 혼재**:
- §0.3 (line 50) = ✅ **정확**: "ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건" (4 모법 + (e) 후속 분리)
- §1.2 의무 표 + §2.2 = ✅ "ADR-011 §2.1 (a)~(d) 모법 + (e2) PASS 발효 자격 매핑" (분리)
- §3 헤더 (line 140) = ⚠️ **부정확**: "**ADR-011 §2.1 (a)~(e2)** PASS 발효 자격 매핑" — (e2) 를 ADR-011 §2.1 에 귀속
- §10 cross-ref (line 239) = ⚠️ **부정확**: "ADR-011 §2.1 (a)~(e)" — (e) 를 ADR-011 §2.1 에 귀속

이는 (β) B-4 ("ADR-012 §2.1 misattribution") 동형 — *조항이 그 ADR §에 실재하는 것처럼* 표기하는 인용 전도. PASS *발효* 의 자격 근거를 모법에 귀속시키는 것은 권위 chain 정밀도 BLOCKING (52 entry B-2 + 57 B-3/B-4 답습 — 모법 과장 차단).

**정정 (R-B-1)**:
- §3 헤더 "ADR-011 §2.1 (a)~(e2)" → **"ADR-011 §2.1 (a)~(d) 모법 + ADR-012 §4 (e)/(e2) 답습 패턴"** (또는 §0.3 line 50 framing 으로 통일)
- §10 line 239 "ADR-011 §2.1 (a)~(e)" → **"ADR-011 §2.1 (a)~(d) + ADR-012 §4 (e)"**
- §3 표 (e2) row 출처를 "ADR-012 §4 (e) 답습 + 본 cycle 합의" 로 명문 (모법 = (a)~(d) 한정)

### §2.2 ✅ 나머지 권위 인용 = 정확 (verify 통과)

| brief 인용 | verify 결과 |
|----------|-----------|
| ADR-012 §2.3 Layer 2 (line 171~175) | ✅ Layer 2 = "Git append-only branch (MANDATORY)" 단일 layer, denyNonFastForwards + branch protection + pre-commit + CI 4 수단 열거 정확. brief 의 "2a/2b" 분해 = 분석 framing (53/55 entry 도입) — ADR-012 조항 아님을 brief §2.2/§2.3 이 명시 (귀속 전도 0) |
| ADR-012 §3.4 timestamp monotonicity (line 414~420) | ✅ "본 entry ts ≥ prev_hash entry ts" 정확. brief §2.5/§4.2 인용 정합 |
| ADR-012 §2.8 numbering (5-layer) | ✅ (entry brief 55 §1.1 답습, 본 brief §2.2 §3(c) 인용) |
| (γ-c) 특화 의무 4 (54 entry §1.3) | ✅ §3 verbatim verify (아래 §3) |
| G4 §4.4.1 line 631~660 Layer 1~5 정의 | ✅ (provider-agnostic-memory-skill-design.md 직접 verify) — Layer 1 hash chain / Layer 2 git append-only / Layer 4 CI 회귀, 정의 정합 |

---

## §3 (γ-c) 특화 의무 4 정합 ✅

54 entry decision brief verify (RT-γ-6 = line 54/113/163/183). 4 의무 본 brief 답습:

| # | 의무 | brief 답습 | 판정 |
|---|------|----------|------|
| 1 | Layer 1/2/4 subsection 강제 (evidence 합산 0) | §2.1~§2.5 Layer subsection 분리, §2.6 "Layer subsection 분리 유지" 명시 | ✅ 합산 0 verify |
| 2 | "defense-in-depth 부분 답습" framing (Layer 3+5 scope 외) | §0.2 #5 + §2 "부분 답습" + §7 #4 영구 | ✅ "충실/완전 답습" 표현 0건 (grep-able RT-PASS-3 미위반) |
| 3 | Layer 1+2+4 통합 동시 발효 | §2.6 E-PASS-12 통합 (subsection 분리 유지) | ✅ |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* | §5 평가 수행 → 비차단 결론 | ✅ (§6 참조) |

→ **(γ-c) 특화 의무 4 전원 정합.** Layer evidence 합산 0 = RT-PASS-2 미위반. "부분 답습" framing 유지 = RT-PASS-3 미위반.

---

## §4 PASS 발효 (e2) vs 진입 권한 (e1) 구분 ✅

brief §0 (line 5/11) + §1.1 + §3 (e2) row = (e1) 진입 권한 (55 `311ca3b`) ↔ (e2) PASS 발효 (본 cycle) 명확 구분. §0.2 #1 "Layer 통합 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후)" = 기정사실화 회피 (P-1 처리).

**evidence 충분성 verify (강행 risk 점검)**:

| 조건 | brief 주장 | Agent B verify |
|------|----------|---------------|
| (a) 동등 이상 보안 | Layer 1 (3 violation type) + Layer 2 (2b+CI) + Layer 4 | ✅ §1 means-vs-ends 정합 |
| (b) 격리 PoC 실증 | jsonl_hash_chain + fixtures + 3 G4 actual run | ✅ run 26557460199/227/197 = success (gh run view verify) |
| (c) ADR/SDD 권위 | G4 §4.4.1 + ADR-012 §2.3/§2.8 | ✅ (§2.2 R-B-1 헤더 정밀도 제외) |
| (d) 자동 회귀 경로 | 3 ledger workflow CI | ✅ |
| (e2) 합의 APPROVE | ⏳ 본 cycle | (진행 중) |

→ **evidence 강행 risk = 낮음.** (a)~(d) = filesystem + gh api + CI run 전수 verify 통과. C-1 timestamp fixture = `4c48099` commit + `timestamp_monotonicity.jsonl` (valid chain + ts 역행 10:05→10:00) + actual run `26557936920` green 직접 verify. E-PASS-10 CI 입증 = 사실.

---

## §5 scope 침입 점검 ✅ 0건

| 침입 영역 | verify |
|---------|--------|
| MVP-2 PASS 발효 | §0.2 #2 + §8 명시 차단 — 본 brief 0건 |
| GP-2 PASS 합산 | §0.2 #3 + §8 — 0건 |
| denyNonFastForwards 자동 활성화 | §0.2 #4 + §8 — 실제 git config 미설정 (local/global/system 전수 exit 1 verify) = brief 주장 정확, 활성화 실행 0 |
| R-S1 자동 정정 | §0.2 #6 + §5 — 평가 한정, 정정 0 |
| Layer 3+5 진입 | §0.2 #5 — "부분 답습" 영구, 0건 |
| ADR/헌법/G4/ADR-012 본문 갱신 | §0.2 #9 — 0건 (본 brief = phase0 신규 1) |

→ **scope 침입 0건.** brief = 합의 입력 1 파일 (phase0), 본문 변경 0. C-1 보강 (`4c48099`) 은 brief 작성 *전* 사용자 명시 선행 보강 (§4.2 명문) — 본 brief 의 침입 아님.

---

## §6 R-S1 hard gate (RT-γ-6) 정합 ✅

**brief 주장 (§5)**: "R-S1 = Layer 통합 PASS 발효 비차단 (MVP-2 PASS 가 종속)".

**54 entry verify**:
- line 113 = "**Layer 1+2+4 통합 PASS 발효 시** R-S1 정정 영향 *평가 의무*"
- line 163 = "**MVP-2 PASS 발효** — ... + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가"

→ 54 entry 는 RT-γ-6 *평가* 를 (i) Layer 통합 PASS 발효 시점 **과** (ii) MVP-2 PASS 발효 시점 **양쪽** 에 부착. brief 는 §5 에서 **실제로 평가를 수행** (G4 §4.4.1 numbering = PRIMARY 5-layer 이므로 R-S1 ADR-012 §2.3 vs §2.8 divergence 가 Layer 정의 명확성을 훼손 안 함 → 비차단 결론). 이는 (i) Layer 통합 PASS 시점 평가 의무를 **충족** — 의무는 *평가* 이지 *정정* 이 아님 (57 B-8 "의무" → "*평가* 의무" framing 답습).

**판정**: brief 의 "비차단 (평가 한정)" = RT-γ-6 정합. 단 §5 가 평가를 MVP-2 PASS 종속으로만 framing 하는 인상 — **54 line 113 이 Layer 통합 PASS 발효 시점 평가도 명문화함을 §5 에 cross-ref 보강 권고** (N-B-2). 의무 자체는 §5 평가 수행으로 충족되었으므로 BLOCKING 아님 (P-6 처리 정합).

---

## §7 권고 (non-blocking)

- **N-B-1**: §2.2/§4.1 2a DEFER 근거에 **Layer 4 `rewrite-defense.yml` non_fast_forward_detected 검출** 추가 (현재 2b 단독 근거 → 2b remote 차단 + Layer 4 CI 검출 이중 operative 명문). append-only ends 의 robustness 강화 + honest 과소 주장 보강 (§1.3).
- **N-B-2**: §5 에 54 entry line 113 ("Layer 통합 PASS 발효 시 R-S1 평가 의무") cross-ref 추가 — 본 cycle 이 그 평가 시점임을 명문 (현재 MVP-2 종속 framing 인상 보정).
- **N-B-3**: `enforce_admins: true` (gh api verify) 를 §2.3 E-PASS-7 에 추가 — admin 우회 불가 = append-only 강도 상향 evidence (현재 brief 미언급).

## §8 NOTE

- **NT-B-1**: 2a DEFER 는 보안 *과소* 주장 (2번째 operative layer 누락) — 보안 과대가 아니므로 P2/P3 위험 미해당. honest matrix 정직성 양호.
- **NT-B-2**: E-PASS subsection 제시 순서 (§2.2 E-PASS-5 → §2.3 E-PASS-7 → §2.4 E-PASS-6) = 55 entry §5.2 numbering 보존하되 표시 순서 5/7/6 — 오류 아님 (Layer 그룹핑상 자연). 가독성 NOTE 한정.
- **NT-B-3**: `required_signatures: false` (gh api verify) = Layer 3 (Signed commit) RECOMMENDED-MVP 미발동 상태와 정합 (solo SPOF 면책, ADR-012 §2.3 Layer 3 "1인 동일 호스트 = SHOULD"). "부분 답습" (Layer 3 scope 외) framing 과 actual state 정합 — 모순 0.
- **NT-B-4**: violation_type actual = `prev_hash_mismatch` + `hash_recalculation` + `genesis_mismatch` (3 Layer-1, ViolationType enum) + `schema_*` + `monotonicity_violation` (jsonl_hash_chain.py:75~77 + 224 verify). HISTORY_REWRITE = 58 entry 제거 (commit 052e583) 확인 — brief §2.1 E-PASS-2 "HISTORY_REWRITE Layer 1 제거 → 3 Layer-1 type + schema" 주장 정확. (β) B-2 "dead enum" 우려 = 58 entry 에서 해소됨.

---

## §9 메타 자기진단 (Agent B)

| # | 위험 | 처리 |
|---|------|----|
| MB-1 | Agent B 가 brief 작성자 (Claude) cascade | 권위 = ADR 원문 line verbatim + gh api + CI run + git config direct verify (추론 아닌 계산적 검증 우선, CLAUDE.md §2) |
| MB-2 | R-B-1 (인용 정밀도) over-reach | ADR-011 §2.1 line 52~61 = (a)~(d) only 직접 verify + ADR-012 §4 line 436 "(a)~(d) + (e)" = (e) 가 ADR-012 도입 확인. single-source 아닌 2 ADR cross-verify 후 격상 (57 M-3 답습) |
| MB-3 | 2a DEFER hole 판정 우호 편향 | rewrite-defense.yml line 128~162 force-push 검출 grep + branch protection allow_force_pushes:false gh api 양면 verify — 코드/설정 실측 기반 |
| MB-4 | APPROVE WITH CONDITIONS 회피 편향 | R-B-1 = 인용 정밀도 (52 B-2 + 57 B-3/B-4 답습 동형) BLOCKING 정당. 보안 hole 0 이나 권위 정밀도는 별도 차원 |

---

**Agent B verdict = APPROVE WITH CONDITIONS** (BLOCKING 1 = R-B-1 권위 인용 정밀도 / 권고 3 / NOTE 4).

**핵심**: 2a DEFER = means-vs-ends 정합 (보안 hole 0, append-only ends = 2b + Layer 4 CI 이중 operative). evidence (a)~(d) 전수 verify 통과 (gh api + CI run + git config + ADR line). 단 §3/§10 "ADR-011 §2.1 (a)~(e2)" 헤더 = (e)/(e2) 를 모법 §2.1 에 귀속 ((e) = ADR-012 §4 답습 패턴) — (β) B-3/B-4 전례 동형 인용 전도 정정 의무 (R-B-1).
