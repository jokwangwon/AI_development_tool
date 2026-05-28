# 3+1 합의 (Reviewer 통합) — full GP-2 PASS trajectory 진입 entry brief

> **cycle**: 64번째 entry — full GP-2 PASS trajectory 진입 entry brief (세션 #3)
> **대상**: `docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md` (v1)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor codex gpt-5.5)
> **4 source**: codex (OpenAI) + Agent A (구현 분석가) + Agent B (안전 검증가) + Agent C (대안 탐색가) — 모두 Anthropic Claude (Agent) vs OpenAI (codex) cross-vendor 충족 (헌법 5조-2)
> **작성**: 2026-05-28

---

## §0 통합 판정

⭐ **APPROVE WITH CONDITIONS** (4 source 전원 APPROVE WITH CONDITIONS strong consensus) — **BLOCKING 3 + 권고 10 1pass 흡수 후 trajectory 진입 자격 발효**.

| source | 판정 | BLOCKING | 권고 | NOTE |
|--------|------|----------|------|------|
| codex (OpenAI gpt-5.5) | APPROVE WITH CONDITIONS | 0 | 4 | 3 (권위 인용 11건 전원 일치) |
| Agent A (구현 분석가) | APPROVE WITH CONDITIONS | 0 | 4 | filesystem direct 전원 실증 (pytest 152 green) |
| Agent B (안전 검증가) | APPROVE WITH CONDITIONS | 1 | 3 | 권위 인용 14건 中 13 일치 / 1 모순 |
| Agent C (대안 탐색가) | APPROVE WITH CONDITIONS | 2 | 3 | 대안 매트릭스 |

→ BLOCKING 발화 = Agent B 1 + Agent C 2 = 3건 (codex + Agent A = BLOCKING 0). **모두 framing/citation/대안 누락 (evidence 차단급 over-claim 0)**.

---

## §1 4 source cross-validation 매트릭스

### §1.1 Consensus (다수 source 수렴)

| # | 합의 | source |
|---|------|--------|
| CS-1 | **scope 정합 (trajectory 진입 한정 vs 실제 결정/구현/발효 0)** 명확 | codex + Agent A + Agent B (scope 13개 침입 0) |
| CS-2 | **R-1 = upstream 영역 분리 판단 정확** (`agent/redact.py` 본 repo 부재, filesystem/rg 직접 확인) | codex + Agent A + Agent C |
| CS-3 | **R-2 = facade placeholder 정확** (`NotImplementedError` + `health()`={}) | codex + Agent A (41 LOC) |
| CS-4 | **prevention over-claim 통제 우수** (R-4 = 설계 동등성, prevention 입증 아님, 3중 명문) | codex + Agent A + Agent B (본 세션 #2 핵심 risk) |
| CS-5 | **권위 인용 정확** (governance §4.5 (a) + ADR-011 §2.3 #2/#4 + ADR-009 §2.3 + R-4 §7.3) | codex 11/11 일치 + Agent B 13/14 일치 |

### §1.2 BLOCKING (Reviewer 독립 verify 후 흡수 의무)

| # | BLOCKING | source | Reviewer verify | 흡수 |
|---|----------|--------|------|------|
| **B-1** ⭐ | §1.1 line 70 citation 오귀속 — "R-2 facade real = (β) §0.2 **#23**" → 실제 **#10** (#23 = 자동 후속 sub-cycle) | Agent B | ✅ **CONFIRMED** (Reviewer 직접 read: (β) brief line 44 = "#10 facade.py placeholder → real (R-2 구현 경로, TR-1)" / line 57 = "#23 자동 후속 실 구현 sub-cycle") | "#23" → "#10" |
| **B-2** ⭐ | §4.4 R-2 후보 누락 — (R-2-c) `secret_scanner.py` Tier-1 catalog 재사용 + (R-2-d) LiteLLM callback hook 미등재 | Agent C (C1) | ✅ 타당 (trajectory entry = 후보 망라 의무, secret_scanner Tier-1 catalog in-repo 실재) | §4.4에 (R-2-c)/(R-2-d) 추가 |
| **B-3** ⭐ | §5.1 "full GP-2 PASS = R-1 ∧ R-2 (AND)" 단정 → 대안 해석 병기 의무 (governance §4.1 "GP-2 = 보조" + ADR-011 §2.3 위임 = "R-2 in-repo prevention 발효 + R-1 위임 회귀 검증" 대안) | Agent C (C2) | ⚠️ **부분** — governance §4.5 (a) verbatim = "Hermes native 검증 **+** facade filter 검증" (AND가 PRIMARY) but §4.1 "보조" + §2.3 위임 = 대안 해석 valid | AND = PRIMARY 유지 + 대안 해석 NOTE 병기 (over-단정 완화) |

### §1.3 권고 (흡수 — 채택)

| # | 권고 | source | 흡수 |
|---|------|--------|------|
| R-1 | §0.3 ADR-011 §2.4 T3 = "직접 인용 vs inference" 분리 (T3 verbatim = "Constitution/ADR/Harness Gates 정의 변경", "facade real ≠ T3" = inference) | codex 1 | §0.3 inference 표기 |
| R-2 ⭐ | SC-2 "import 0 위임 검증" 택 시에도 **evidence contract 명문** (Hermes artifact/version pin + canary + R-6 재실행) | codex 2 + Agent C R-1-c | §3.3 + §9 보강 |
| R-3 | §5.1 "carry-off" → "carry-over" 오타 | codex 3 | ✅ CONFIRMED 정정 |
| R-4 | §11 마지막 문장 "사용자 명시" 조건 반복 (over-claim risk 감소) | codex 4 | §11 보강 |
| R-5 | §4.4 RedactionFilter = facade **내부 협력자** 근거 강화 (B-3 AND 해석 연결 — facade 진입점 의존) | Agent A | §4.4 |
| R-6 | facade.py LOC "42" → "41" (마지막 공백 줄 제외) | Agent A | §4.1 |
| R-7 | RT-1 window 안전 제약 명문 (facade real 후 RedactionFilter 미부착 window 금지) | Agent B + Agent C | §8 RT-1 |
| R-8 | RT-2 cover 비대칭 (60 B-2 답습 — in-repo 능동 redaction 보증 0) | Agent B | §8 RT-2 |
| R-9 | R-5 base64 evasion 자격 부착 (known limitation 명문) | Agent B | §8 RT-4 |
| R-10 | §3 governance §4.4 Entry "agent/redact.py 존재 확인 (R-1 Day 2)" vs 52 R-A-1 (본 repo 부재) 충돌 주석 | Agent A | §3.1 주석 |

### §1.4 Unique NOTE (단일 source, 채택 0 — 기록)

- (codex) prevention over-claim 방지 우수 — 60/62 brief 도 detection-layer/deferred 일관 (cross-confirm)
- (Agent A) `/tmp/hermes-phase0` 격리 환경 재확보 = SC-2 R-1 검증 선결 risk
- (Agent C) full GP-2 PASS scope 축소 대안 (detection-tier 영구 + prevention 별도 milestone) — B-3 대안 해석과 연결, sub-cycle 시점 평가

---

## §2 Reviewer 독립 verify (5 source 격상 verify)

| 항목 | verify 결과 |
|------|------|
| B-1 citation | ✅ CONFIRMED — (β) brief line 44 (#10 = facade real) / line 57 (#23 = 자동 후속). brief line 70 "#23" 오귀속 |
| facade.py placeholder | ✅ CONFIRMED — `complete()` NotImplementedError + `health()` {} (직접 read) |
| `agent/redact.py` 본 repo 부재 | ✅ CONFIRMED — find/rg 결과 본 repo 內 부재 (codex + Agent A + Reviewer cross) |
| governance §4.5 (a) AND | ✅ CONFIRMED — line 451 "Hermes native redaction Tier-1 42 catalog 적용 검증 **+** P1 facade redaction filter 검증" (AND PRIMARY, B-3 대안은 §4.1 "보조" 근거) |
| R-4 = 설계 동등성 | ✅ CONFIRMED — redaction-pattern-equivalence §7.3 "Hermes 안전성 선언 금지" (prevention 입증 아님) |

---

## §3 합의 결론

✅ **full GP-2 PASS trajectory 진입 자격 발효 APPROVE WITH CONDITIONS** (4 source strong consensus):

1. **trajectory 진입 자격 충족** — detection-layer PASS (60) + MVP-2 PASS prevention 잔여 trajectory 명문 (62) + 격차 = Exit (a) prevention 검증 (R-1 ∧ R-2, AND PRIMARY).
2. **발효 조건 = BLOCKING 3 1pass 흡수**:
   - (B-1) citation "#23" → "#10" 정정
   - (B-2) R-2 후보 (R-2-c)/(R-2-d) 추가
   - (B-3) AND 단정 → 대안 해석 NOTE 병기
3. **권고 10 흡수** (§1.3) — over-claim 완화 + 후보 망라 + evidence contract 명문 (R-2 ⭐).
4. **sub-cycle 진입 = 사용자 명시 의무** (SC-1/SC-2/SC-3 순서 권고 ≠ 결정).
5. **prevention over-claim 0** (4 source 공통 확인) — R-4 = 설계 동등성, full GP-2 PASS *발효* ≠ trajectory *진입* (본 cycle = 진입 한정).

→ **v1.1 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단, 52/55/60 동형) → commit + push → trajectory 진입 자격 발효**.

---

## §4 메타 편향 자기진단 (Reviewer)

| # | 위험 | 처리 |
|---|------|----|
| M-1 | Reviewer = brief 작성자 (Claude) cascade | cross-vendor codex (OpenAI) 독립 + Agent B/C BLOCKING 3 발화 (작성자 미포착 citation/대안 포착) |
| M-2 | B-1 citation 경미 → 무시 risk | Reviewer 직접 read CONFIRMED — citation 정확성 = 권위 chain 무결성 (본 프로젝트 핵심 가치) |
| M-3 | B-3 AND vs 대안 = 작성자 편의 채택 risk | governance §4.5 (a) verbatim AND PRIMARY 유지 + §4.1 "보조" 대안 NOTE 병기 (양쪽 valid 명문) |
| M-4 | 4 source 전원 APPROVE = rubber-stamp risk | BLOCKING 3 + 권고 10 실질 흡수 (citation 정정 + 후보 2 추가 + evidence contract) |
| M-5 | prevention over-claim 재발 (세션 #2 4회) | 4 source 공통 "R-4 = 설계 동등성, prevention 입증 아님" 확인 — 본 brief over-claim 0 (정직 scope) |

---

**본 합의 보고서 끝.**

**다음 단계**: brief v1.1 흡수 (BLOCKING 3 + 권고 10) → SESSION + INDEX commit + push → **full GP-2 PASS trajectory 진입 자격 발효**. 후속: SC-1 (R-2 facade real) / SC-2 (R-1 위임 검증) / SC-3 (full GP-2 PASS 발효) = 사용자 명시 별도 sub-cycle.
