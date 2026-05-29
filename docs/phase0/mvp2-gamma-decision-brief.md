# (γ-c) 채택 결정 decision brief (v1)

> **작성**: 2026-05-28 (54번째 entry 진입 cycle)
>
> **scope**: (γ) 4 대안 中 **(γ-c) Layer 1+2+4 동시 채택 결정 발효** 한정 (53 entry Reviewer 통합 권고 답습)
>
> **본 cycle = 작은 영역** (1-agent 직접, Reviewer 통합 권고 답습 한정, ceremony-inflation 차단)
>
> **본 cycle 발효 자격** = **1-agent 직접 합의 + 사용자 명시 결정** + 5/5 풀 3+1 승격 trigger 0건 자체 검증
>
> **본 cycle 발효 효과** = (γ-c) Layer 1+2+4 동시 채택 결정 발효 + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 (구현 발효 ≠ 본 합의)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 53 entry, commit `f5cf584`)

53 entry `mvp2-gamma-layer-separation-brief.md` (v1.1) §8.1 다음 단계 항목 1:
- **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)

본 cycle 진입 사용자 명시 (2026-05-28, 53 entry commit `f5cf584` push 후):
- **대안 선택**: **(γ-c) Layer 1+2+4 동시** (Reviewer 통합 권고 1순위 답습, 4 source consensus)
- **합의 형태**: **1-agent 직접** (Reviewer 권고 답습 한정, ceremony-inflation 차단)

본 brief = (γ-c) 채택 결정 영역 한정. (β) sub-수단 결정 + Layer 1+2+4 통합 PASS 격상 + 실 구현 = 후속 별도 cycle.

### §0.2 본 brief 가 *하는* 것

1. (γ-c) 채택 결정 발효 정당성 (53 entry Reviewer 통합 권고 + 4 source consensus 답습 cross-check) (§1)
2. (γ-c) 채택 결정 발효 효과 명문 (Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효) (§2)
3. 5/5 풀 3+1 승격 trigger 0건 발화 자체 검증 (1-agent 직접 적격성) (§3)
4. 후속 cycle 진입 자격 + 금지 사항 (§4 + §5)
5. 답습 참조 (§6)

### §0.3 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 |
| 2 | `tools/` / `tests/canonical/` / `.github/workflows/` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 4 | Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 | 0건 (사용자 명시 의무) |
| 5 | (β) sub-수단 결정 cycle 자동 진입 (R-1~R-5 + L-1~L-5 + W-A~E) | 0건 |
| 6 | 외부 library 도입 결정 | 0건 |
| 7 | threshold 고정 | 0건 |
| 8 | MVP-2 Implementation Evidence PASS 발효 | 0건 |
| 9 | MVP-1 PASS 재선언 | 0건 |
| 10 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 11 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 12 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 (γ-c) = Layer 1+2+4 한정) |
| 13 | (γ-a/b/d) 대안 재평가 | 0건 (Reviewer 통합 권고 답습 한정) |
| 14 | (γ-e/f/g) hybrid 대안 결정 | 0건 (53 entry B-8 답습, 별도 cycle) |
| 15 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습) |
| 16 | `adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory) |
| 17 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 |
| 18 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역) |
| 19 | Tier-2/3 vendor catalog 본문 확장 | 0건 |
| 20 | GP-1/GP-4/GP-6/G3/G4 (Layer 4 외) 영역 진입 결정 | 0건 |
| 21 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **1-agent 직접 합의 + 사용자 명시 결정** + 5/5 풀 3+1 승격 trigger 0건 자체 검증
- ✅ 본 brief 발효 결과 = **(γ-c) Layer 1+2+4 동시 채택 결정 발효** + 후속 Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효 + (γ-c) 특화 의무 명문 ((γ-c) PASS evidence template Layer 1/2/4 subsection 강제 + "부분 답습" framing 영구 유지)
- ❌ 본 brief 자체에서 sub-수단 결정 (L-1~L-5 + R-1~R-5) 0건
- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 0건
- ❌ 본 brief 자체에서 실 구현 0건
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ⚠️ 본 brief 합의 후 *자동 sub-cycle 진입 금지* — 사용자 명시 결정 의무

---

## §1 (γ-c) 채택 결정 발효 정당성

### §1.1 Reviewer 통합 권고 답습 (53 entry §1 답습)

53 entry `3plus1-consensus-2026-05-28-mvp2-gamma.md` §1.4 (4 source 권고 순위 cross-vendor confirm):

| 대안 | codex 권고 | Agent A 권고 | Agent B | Agent C | Reviewer 통합 |
|------|---------|---------|---------|---------|------------|
| **(γ-c) Layer 1+2+4 동시** | **1순위** | **1순위** | (부분 답습 정정 후 권고) | (R-C-3 framing fragile 경고) | **1순위 (3/4 source consensus + Agent B 부분)** |
| (γ-a) 단계적 | 2순위 | 2순위 | (정합) | (정합) | 2순위 (4/4 consensus) |
| (γ-b) 단독 | 3순위 | 3순위 | (evidence 분리 risk) | (정합) | 3순위 |
| (γ-d) 분리 | 비권고 | 비권고 | 비권고 | 비권고 | 비권고 (5 source 모순 CONFIRMED) |

→ **(γ-c) 1순위 = 4 source consensus (3/4 직접 명시 + Agent B 부분 답습 정정 후 권고)**.

### §1.2 (γ-c) 채택 결정 발효 근거

| 근거 | 답습 |
|------|----|
| 4 source consensus 1순위 | codex §6 + Agent A §6 + Agent B (부분 답습 정정 후 권고) + Reviewer 통합 §1.4 |
| ADR-011 §2.1 (a)~(d) + (e) 5조건 충족 정합 | 53 entry §3 매트릭스 — (γ-c) 모든 조건 충족 정합 |
| PoC 시제 답습 충실 | 53 entry §2.5 + Agent A filesystem direct inspection 5 PoC 영역 size verify (tools/jsonl_hash_chain.py 14038B + canonical_json.py 10055B + tests/canonical 8 카테고리 + g4-hash-chain.yml 10652B 7 step + 3 보조 workflow) |
| defense-in-depth 부분 답습 정합 | 53 entry §2.3.2 + B-6 흡수 — Layer 1+2+4 한정 (Layer 3+5 = scope 외) |
| 합의 cycle 효율 | 1 cycle 등가 (Layer 1+2+4 동시 PASS evidence 분리) vs (γ-a) 4 cycle |
| ceremony-inflation 차단 | (γ-a) 4 cycle 대비 (γ-c) 3 cycle 등가 |
| (γ-d) 모순 회피 | 5 source verify CONFIRMED (53 entry §4.4) — (γ-d) 비권고 정합 |
| 사용자 명시 결정 | 2026-05-28, AskUserQuestion (γ-c) Recommended 답습 |

### §1.3 (γ-c) 특화 의무 명문 (53 entry N-1 + B-6 답습 + 영구 유지)

본 (γ-c) 채택 결정 발효 시 다음 의무 영구 유지:

1. **PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제** (53 entry N-1 흡수 답습)
   - Layer 1 (hash chain) evidence + Layer 2 (Git append-only) evidence + Layer 4 (CI 회귀 검증) evidence 각각 분리 명시
   - Layer 4 evidence 內 Layer 1+2 evidence 합산 금지 ((γ-b) risk 회피)
2. **"defense-in-depth 부분 답습" framing 영구 유지** (53 entry B-6 흡수 답습)
   - "부분 답습" 표현 = Layer 1+2+4 한정, Layer 3 (Signed commit) + Layer 5 (External anchor) = 본 cycle scope 외
   - "충실 답습" 또는 "완전 답습" 표현 금지 영구
3. **Layer 1+2+4 통합 PASS evidence 동시 발효** ((γ-a) 단계적 vs (γ-c) 통합 차이)
4. **R-S1 후행 영향 RT-γ-6 답습** (53 entry §5.1 답습) — Layer 1+2+4 통합 PASS 발효 시 R-S1 정정 영향 평가 의무

---

## §2 (γ-c) 채택 결정 발효 효과

### §2.1 본 cycle 발효 효과

본 (γ-c) 채택 결정 발효 시:

1. **(γ-c) Layer 1+2+4 동시 채택 결정 발효** — (γ-a/b/d) 대안 = 비채택 (Reviewer 통합 권고 답습 한정)
2. **Layer 1+2+4 통합 PASS 격상 cycle 진입 자격 발효** — 후속 sub-cycle 진입 권한 (사용자 명시 의무)
3. **(γ-c) 특화 의무 영구 유지 발효** (§1.3 답습)
4. **(γ-d) 비권고 + Layer 4 PASS 선발효 금지 명문 답습 보존** (53 entry §2.4.5 + B-1 답습)

### §2.2 본 cycle 발효 *하지 않는* 영역

§0.3 답습 (21 항목). 핵심:
- ❌ Layer 1+2+4 통합 PASS 격상 sub-cycle 자동 진입 (사용자 명시 의무)
- ❌ (β) sub-수단 결정 cycle 자동 진입
- ❌ 실 구현 / MVP-2 Implementation Evidence PASS 발효
- ❌ (γ-e/f/g) hybrid 대안 결정 (B-8 답습)

---

## §3 5/5 풀 3+1 승격 trigger 0건 발화 자체 검증 (1-agent 직접 적격성)

본 §3 = 본 cycle 1-agent 직접 합의 적격성 자체 검증 (Reviewer 통합 권고 답습 한정 = ceremony-inflation 차단).

| # | trigger | 본 cycle 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (신규 영역 결정 / 수단 결정 / threshold 고정) | ❌ 미발화 | (γ-c) 채택 결정 = Reviewer 통합 권고 답습 한정 (53 entry 4 source consensus 발효 답습). 신규 영역 결정 0 / 수단 결정 0 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일 + SESSION + INDEX, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 = 52/53 entry 발견 + RT-γ-6 답습 (별도 cycle, 본 cycle scope 외) |
| 5 | 외부 LLM 응답 통합 필요성 | ❌ 미발화 | 본 cycle = Reviewer 통합 권고 답습 한정, 외부 LLM 응답 = 53 entry codex 이미 발효 (재호출 불필요) |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #19 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 명시 금지 |

→ **0/7 발화 → 1-agent 직접 합의 적격 (Reviewer 통합 권고 답습 한정, ceremony-inflation 차단 메모리 답습)**.

---

## §4 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 (γ-c) 채택 결정 발효 후 (사용자 명시 의무):

1. **(β) sub-수단 결정 cycle** — R-1~R-5 (GP-2) + L-1~L-5 (G4 §4.4 Layer 4) + W-A~E — 풀 3+1 (수단별 차등)
2. **Layer 1+2+4 통합 PASS 격상 cycle** — Layer 1 hash chain + Layer 2 Git append-only + Layer 4 CI 회귀 검증 동시 PASS evidence (각 layer subsection 분리 강제, §1.3 답습) — 풀 3+1 + 외부 LLM 1+
3. **실 구현 sub-cycle** ((β) + (γ-c) 채택 후) — Hermes upstream `agent/redact.py` 영역 + 본 repo P1 facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1+2+4 PoC → PASS + R-6 workflow 확장 step (Layer 2a `denyNonFastForwards` 활성화 evidence 별도 verify 의무, 53 entry B-3 답습)
4. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 + RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 (32 entry 답습 패턴)
5. **(γ-e/f/g) hybrid 대안 결정 cycle** (53 entry B-8 답습, 선택) — 본 (γ-c) 채택 결정 후 hybrid 영역 검토 가능
6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 강화 (RT-γ-6 답습)
7. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008/012/011

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §5 금지 사항

§0.3 답습 (21 항목). 핵심 강화:

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 Layer 1+2+4 통합 PASS 격상 sub-cycle 진입 | 사용자 명시 의무 |
| 2 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | Layer 4 PASS 선발효 ((γ-d) 모순 답습) | 영구 금지 (53 entry §2.4.5 + B-1 답습) |
| 4 | (γ-a/b/d) 대안 재평가 자동 진입 | 본 (γ-c) 채택 결정 영구 발효 (재평가 = 별도 cycle 사용자 명시) |
| 5 | (γ-e/f/g) hybrid 대안 결정 자동 진입 | 사용자 명시 의무 |
| 6 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 답습) |
| 7 | Layer 3 (Signed commit) + Layer 5 (External anchor) 자동 진입 | 별도 cycle ("부분 답습" framing 영구 유지) |
| 8 | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | 영구 금지 (§1.3 (γ-c) 특화 의무 답습) |
| 9 | Layer 4 evidence 內 Layer 1+2 evidence 합산 | 영구 금지 (PASS evidence template Layer subsection 강제 §1.3 답습) |

---

## §6 답습 참조

### §6.1 상위 권위

- 헌법 제8조 (보안) — `docs/constitution/PROJECT_CONSTITUTION.md`
- 헌법 제5조-2 (Provider Liquidity 비협상) — 동상
- ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`

### §6.2 직접 선행 자료

- 53 entry (γ) brief v1.1 — `docs/phase0/mvp2-gamma-layer-separation-brief.md` (522줄)
- 53 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, APPROVE WITH CONDITIONS, BLOCKING 8 + 권고 16, (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 4 source consensus)
- 53 entry codex 응답 — `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` (3284줄)
- 53 entry Agent A/B/C 응답 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma-agent-{a,b,c}.md`
- 52 entry (α) entry brief v1.1 — `docs/phase0/mvp2-entry-brief.md`
- 52 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- `provider-agnostic-memory-skill-design.md §4.4` (Layer 1~5)
- `ADR-012-evidence-ledger-protection.md §2.3 + §2.8`

### §6.3 메타 영역 (53 entry §9.3 답습)

실 repo PoC 시제:
- `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type)
- `tools/canonical_json.py` (10055B)
- `tests/canonical/` (8 카테고리 verify 충족 / 24 fixture 정량 = 52 entry carry-over)
- `.github/workflows/g4-hash-chain.yml` (10652B, 7 step 분리)
- `.github/workflows/history-anchor-verifier.yml` (19094B)
- `.github/workflows/rewrite-defense.yml` (16454B)
- `.github/workflows/r2-canary.yml` (5476B)

### §6.4 cross-reference 갱신 영역 (별도 commit, 본 cycle scope 외)

- (γ-c) Layer 1+2+4 통합 PASS evidence template 작성 (Layer subsection 강제, §1.3 답습)
- R-S1 cross-reference 정정 (52/53 entry §9.5 + RT-γ-6 답습)

---

## §7 자기진단 (1-agent 직접 메타 편향 회피)

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 brief 가 (γ-c) 채택을 *권유* 방향으로 편향 | §0.3 21 금지 + §0.4 권위 한계 + §3 5/5 trigger 0건 자체 검증 = Reviewer 통합 권고 답습 한정 (4 source consensus 답습) |
| P-2 | 1-agent 직접 합의가 ceremony-inflation 회피 자격 위협 | §3 0/7 trigger 발화 자체 검증 + 53 entry Reviewer 통합 권고 4 source consensus 답습 = ceremony-inflation 차단 정합 (메모리 답습) |
| P-3 | (γ-c) 채택 결정 = (γ-a/b/d) 대안 영구 비채택 → 결정 영역 침입 risk | §5 #4 "재평가 = 별도 cycle 사용자 명시" 영구 보존 + Reviewer 통합 권고 답습 한정 (본 cycle = 권고 답습, 신규 결정 0) |
| P-4 | (γ-c) 특화 의무 (§1.3) 가 후속 sub-cycle 결정 영역 침입 | §1.3 의무 = 53 entry N-1 + B-6 흡수 답습 (Reviewer 통합 권고 답습 한정) + 후속 sub-cycle = 사용자 명시 의무 (§5 #1 답습) |
| P-5 | R-S1 후행 영향 (RT-γ-6) 가 본 cycle 결정 영향 | §1.3 의무 #4 + §5 #6 = 별도 cycle 답습 + Layer 1+2+4 통합 PASS 발효 시 평가 의무 명문 |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 → 1-agent 직접 합의 보고서 작성 → SESSION + INDEX commit + push (54 entry).
