# Layer 1+2+4 통합 PASS 격상 entry brief (v1.1)

> **작성**: 2026-05-28 (55번째 entry 진입 cycle)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass.md`) BLOCKING 9 + 권고 18 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단). §11 v1.1 보강 매트릭스 추가.
>
> **scope**: G4 §4.4 Layer 1+2+4 통합 PASS 격상 진입 합의 ((γ-c) 채택 발효 답습)
>
> **본 cycle = 큰 cycle** (54 entry (γ-c) 채택 발효 후 carry-over 5번, 풀 3+1 + 외부 LLM 1+, 24/52 entry entry brief 답습 동형)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = Layer 1+2+4 통합 PASS 격상 진입 권한 발효 + 후속 실 구현 sub-cycle 진입 자격 발효 (evidence 평가 + (γ-c) 특화 의무 4 답습 + RT-γ-6 평가). 실 구현 + R-6 actual run + PASS 발효 = 별도 sub-cycle (본 cycle = 진입 합의 한정)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 54 entry, commit `895a77b`)

54 entry `mvp2-gamma-decision-brief.md` §4 + SESSION carry-over #5 답습:
- (α) ✅ **54 entry 발효** ((γ-c) Layer 1+2+4 동시 채택 결정 발효)
- (β) sub-수단 결정 cycle — 별도 합의
- **5번: Layer 1+2+4 통합 PASS 격상 cycle ((γ-c) 채택 발효 답습) — 풀 3+1 + 외부 LLM 1+, Layer subsection 강제 + "부분 답습" framing 영구 + RT-γ-6 답습**

본 cycle 진입 사용자 명시 (2026-05-28, 54 entry commit `895a77b` push 후) — "5번 Layer 1+2+4 통합 PASS 격상 진입". 본 brief = (γ-c) 채택 발효 답습 한정. (β) sub-수단 결정 + 실 구현 sub-cycle + MVP-2 PASS 발효 합의 = 별도 cycle.

### §0.2 본 brief 가 *하는* 것

1. **54 entry (γ-c) 채택 발효 답습** ((γ-c) 특화 의무 4 답습 cross-check) (§1)
2. **PoC 시제 충족 자격 평가** (Layer 1+2+4 각 영역별, 53 entry §2.5 + 본 cycle audit 답습) (§2)
3. **Layer 별 PASS 격상 영역 분석** — Layer 1 (hash chain) + Layer 2 (Git append-only, 2a local + 2b remote 분리) + Layer 4 (CI 회귀 검증) (§2)
4. **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 매트릭스 (Layer 별 + 통합)** (§3, 52 entry B-2 framing 답습)
5. **본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화** (53/54 entry 답습) (§4.1)
6. **(γ-c) 특화 의무 4 영구 답습** — Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6 (§4.2)
7. **7 풀 3+1 승격 트리거 발화 검증** (§4.3)
8. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의, 52/53 entry N-1 답습) (§5)
9. **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가** ((γ-c) 특화 의무 4 답습, §5.2 영구 의무) (§5)
10. **외부 LLM 응답 요구 영역** (사용자 영역) (§7)
11. **후속 실 구현 sub-cycle 진입 자격 명문** (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 |
| 2 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | `tests/canonical/` test corpus 본문 변경 | 0건 (72 files / 8 카테고리 답습 보존) |
| 4 | `.github/workflows/*.yml` 본문 변경 | 0건 (4 G4 workflow 답습 보존) |
| 5 | **`git config receive.denyNonFastForwards true` 활성화 실행** ⭐ (53 entry B-3 답습) | 0건 (활성화 = 별도 실 구현 sub-cycle 영역, 본 brief = evidence 평가 + 활성화 계획 권고 한정) |
| 6 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 7 | R-6 workflow actual run 트리거 | 0건 (별도 실 구현 sub-cycle) |
| 8 | **GP-2 sub-수단 결정** (R-1~R-5) | 0건 ((β) 별도 cycle) |
| 9 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1~L-5) | 0건 ((β) 별도 cycle) |
| 10 | **W 통합 결정** (W-A~E) | 0건 ((β) 별도 cycle) |
| 11 | 외부 library (`pyjcs` / `rfc8785`) 도입 결정 | 0건 (L-5 별도) |
| 12 | threshold 고정 | 0건 |
| 13 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 14 | **Layer 1+2+4 통합 PASS 발효** ⭐ | 0건 (본 cycle = 진입 합의, PASS 발효 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도 합의) |
| 15 | **MVP-2 Implementation Evidence PASS 발효** | 0건 (Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도) |
| 16 | **MVP-1 PASS 재선언** | 0건 (32 entry 답습 유지) |
| 17 | Operational Readiness PASS / Hermes PMO 격상 | 0건 |
| 18 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 19 | `adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory) |
| 20 | G4 §4.4 Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 결정 | 0건 ((γ-c) "부분 답습" framing 영구 답습, 54 entry §1.3 의무 2) |
| 21 | (γ-a/b/d) 대안 재평가 | 0건 (54 entry (γ-c) 채택 결정 영구 발효 답습) |
| 22 | (γ-e/f/g) hybrid 대안 결정 | 0건 (53 entry B-8 답습) |
| 23 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle, RT-γ-6 답습 — 단, 본 cycle = PASS 시점 선행/동시 정정 *평가* 의무) |
| 24 | branch protection contexts 자동 추가 | 0건 (사용자 admin scope 영역, 43 entry 답습) |
| 25 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 |
| 26 | 자동 후속 실 구현 sub-cycle 진입 | 0건 (사용자 명시 의무) |
| 27 | Layer 4 PASS 선발효 (Layer 1+2 PASS 부재 시, (γ-d) 모순 답습) | 0건 (영구 금지, 54 entry §5 #3 답습) |
| 28 | Layer 4 evidence 內 Layer 1+2 evidence 합산 (Layer subsection 미준수) | 0건 ((γ-c) 특화 의무 1 영구 답습, 54 entry §5 #9) |
| 29 | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | 0건 ((γ-c) 특화 의무 2 영구 답습, 54 entry §5 #8) |
| 30 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ 응답 입력 (cross-vendor) + 사용자 명시 결정**
- ✅ 본 brief 발효 결과:
  1. Layer 1+2+4 통합 PASS 격상 *진입 권한 발효*
  2. 후속 실 구현 sub-cycle 진입 자격 발효
  3. (γ-c) 특화 의무 4 답습 영구 보존 (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
  4. PASS evidence template *후보 채택* (Layer 1/2/4 subsection 분리 강제)
  5. Rollback Trigger / Evidence 후보 채택
- ❌ 본 brief 자체에서 Layer 1+2+4 통합 PASS *발효* 0건 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE 후 별도)
- ❌ 본 brief 자체에서 sub-수단 결정 0건
- ❌ 본 brief 자체에서 실 구현 0건 (denyNonFastForwards 활성화 0 / R-6 actual run 0)
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ❌ 본 brief 자체에서 R-S1 cross-reference 정정 0건 (RT-γ-6 평가 한정, 정정 = 별도 cycle)
- ❌ 본 brief 자체에서 ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건
- ⚠️ 본 brief 합의 후 *자동 실 구현 sub-cycle 진입 금지* — 사용자 명시 결정 의무

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습 (54 entry + 53 entry + 52 entry + 32 entry)

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| 54 entry decision brief + 1-agent 직접 합의 (`895a77b` 발효) — (γ-c) Layer 1+2+4 동시 채택 결정 발효 | 본 brief 의 **직접 입력 자료** (54 entry §1.3 (γ-c) 특화 의무 4 답습 source) |
| 53 entry (γ) brief v1.1 + Reviewer 통합 합의 — 4 source consensus + R-S1 5 source verify CONFIRMED | 4 source consensus 권고 답습 (Reviewer 통합 (γ-c) 1순위) + R-S1 후행 영향 RT-γ-6 답습 source |
| 52 entry (α) entry brief v1.1 + Reviewer 통합 합의 — MVP-2 진입 권한 발효 | MVP-2 영역 (GP-2 + G4 §4.4 Layer 4) 진입 권한 발효 답습 |
| 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-1 PASS 답습 그대로 유지 (재선언 0). MVP-2 PASS = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도 |
| `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (PRIMARY, 5-layer) | Layer 1~5 정의 |
| `ADR-012 §2.8 line 264~272` (SUPPORTING, 5-layer 동형) | Layer numbering 권위 |
| `ADR-012 §2.3 line 165~185` (PRINCIPLE ONLY) | Hash chain + Append-only 원칙 (numbering 근거 아님, R-S1 답습) |
| `ADR-012 §2.7` (prev_hash 실패 BLOCK + Manual Review) | RT-γ-4 답습 |
| `ADR-012 §3.4` (timestamp monotonicity) | RT-γ-6 답습 |
| `ADR-012 §2.5` (RFC 8785 JCS) | canonical JSON test corpus 답습 |
| `ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건` (52 entry B-2 답습) | 5조건 매트릭스 §3 |
| **본 cycle audit (read-only, 2026-05-28)** | PoC 시제 현 상태 cross-check (§2.5 답습) |

### §1.2 54 entry (γ-c) 특화 의무 4 영구 답습 (본 brief 핵심 framing)

| # | 의무 | 본 cycle 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 | §2 Layer 별 분리 분석 + §3 매트릭스 Layer 별 컬럼 + §5.2 evidence template 후보 (Layer subsection 강제) |
| 2 | "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외) | §0.3 #20 명시 + §2.1 영역 정의 "부분 답습" 표현 사용 + §6 #6 영구 답습 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §2.4 통합 영역 + §3 통합 매트릭스 + §4.2 통합 발효 |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 | §5.2 RT-γ-6 평가 + §8 다음 단계 #5 명문 |

### §1.3 ⭐ PoC 시제 현 상태 cross-check (본 cycle audit 발견)

본 cycle 시점 (2026-05-28) audit 결과:

| 영역 | 현 상태 | 답습 |
|------|--------|----|
| `tools/jsonl_hash_chain.py` | ✅ 14038B (genesis hash + 4 violation_type: PREV_HASH_MISMATCH + HASH_RECALCULATION + HISTORY_REWRITE + GENESIS_MISMATCH) | 53 entry Agent A NT-A-1 + B-6 답습 |
| `tools/canonical_json.py` | ✅ 10055B (rfc8785 + jcs + jq -S -c fallback + cross-check mode) | 53 entry codex NOTE-5 답습 |
| `tests/canonical/` | ✅ **72 files / 8 카테고리** (array, escape, hash_stability, key_ordering, lossy, nested, number, unicode = 8 × 3 case × 3 파일 = 72 = 24 fixtures input) | 53 entry codex NOTE-5 verify (8 × 3 × 3 = 72) + 52 entry Agent A R-A-2 carry-over 해소 |
| `.github/workflows/g4-hash-chain.yml` | ✅ 10652B (7 step 분리) | 53 entry Agent A N-A-1 + N-A-3 답습 |
| `.github/workflows/history-anchor-verifier.yml` | ✅ 19094B | 53 entry Agent A N-A-3 답습 |
| `.github/workflows/rewrite-defense.yml` | ✅ 16454B | 동상 |
| `.github/workflows/r2-canary.yml` | ✅ 5476B | 동상 (N-7 흡수) |
| **`git config receive.denyNonFastForwards`** ⭐ | ⚠️ **미설정** (local + global 모두 출력 0건) — 53 entry B-3 답습 (Layer 2a local workflow evidence 별도 verify 의무) | 53 entry B-3 답습 — 본 cycle = 활성화 evidence 별도 verify 의무 명문 + 실 구현 sub-cycle 활성화 의무 |
| `tests/fixtures/jsonl_ledger/{pass,fail}/` | ✅ 다수 (minimal_chain + roundtrip_t2_strict + genesis_mismatch + hash_recalculation + prev_hash_mismatch + missing_event_field) | 본 cycle audit 신규 발견 |
| `tests/fixtures/history_anchor_verifier/` | ✅ 다수 (original_ledger + extended_ledger + full_rewrite_ledger + middle_deletion_ledger) | 본 cycle audit 신규 발견 |

→ **PoC 시제 전 영역 충족 (Layer 2a denyNonFastForwards 1 영역 미설정 = 실 구현 sub-cycle 활성화 의무)**. tests/canonical 24 fixture 정량 = 본 cycle audit 직접 verify 완료 (72 files / 8 × 3 × 3, 52 entry Agent A R-A-2 carry-over 해소).

---

## §2 Layer 별 PASS 격상 영역 분석

### §2.1 영역 정의 ((γ-c) 특화 의무 2 답습 — "부분 답습" framing)

본 brief = **G4 §4.4 Layer 1+2+4 통합 *부분 답습*** (Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외, 별도 cycle 영역, 54 entry §1.3 의무 2 영구 답습).

### §2.2 Layer 1 — Hash Chain (MANDATORY)

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ `tools/jsonl_hash_chain.py` 14038B (genesis hash 함수 + 4 violation_type: PREV_HASH_MISMATCH + HASH_RECALCULATION + HISTORY_REWRITE + GENESIS_MISMATCH) |
| **권위** | G4 §4.4.1 line 631~636 + ADR-012 §2.3 line 165~169 (PRINCIPLE) + §2.8 line 268 (numbering) |
| **PASS 격상 영역** | (a) hash chain 검증 PoC PASS (middle tampering 차단 PoC, Docker 격리) + (b) canonical JSON sha256 동등성 검증 + (c) genesis hash 첫 entry 작성 evidence + (d) Layer 4 CI step 內 hash chain 검증 actual run PASS |
| **fixtures** | `tests/fixtures/jsonl_ledger/{pass,fail}/` (minimal_chain + roundtrip_t2_strict + genesis_mismatch + hash_recalculation + prev_hash_mismatch + missing_event_field) |
| **violation_type Layer 매핑** (53 entry N-6 답습) | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH = Layer 1 |

### §2.3 Layer 2 — Git Append-only Branch (MANDATORY, 2a + 2b 분리, 53 entry B-3 답습)

#### §2.3.1 Layer 2a — local workflow

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ⚠️ **`git config receive.denyNonFastForwards` 미설정** (local + global 모두 0건 verify, 본 cycle §1.3 답습) — Layer 2a evidence 별도 verify 의무 |
| **권위** | G4 §4.4.1 line 638~642 + ADR-012 §2.3 line 171~175 + §2.8 line 269 |
| **PASS 격상 영역** | (a) `git config --system receive.denyNonFastForwards true` 활성화 + entrypoint 또는 pre-receive hook 강제 + (b) Docker 격리 PoC (force-push 시도 → reject) + (c) Layer 4 CI step base branch 대비 JSONL line deletion / rewrite 감지 actual run PASS |
| **fixtures** | `tests/fixtures/history_anchor_verifier/{pass,fail}/` (original_ledger + extended_ledger + middle_deletion_ledger + full_rewrite_ledger) |
| **실 구현 sub-cycle 의무** | denyNonFastForwards 활성화 = 본 cycle scope 외, 실 구현 sub-cycle 영역 (별도 사용자 명시) |
| **violation_type Layer 매핑** (53 entry N-6 답습) | HISTORY_REWRITE = Layer 2 |

#### §2.3.2 Layer 2b — remote / admin

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ branch protection rule (43 entry 8 contexts 답습) |
| **권위** | G4 §4.4.1 line 640 + ADR-012 §2.3 line 173 |
| **PASS 격상 영역** | (a) main branch protection 8 contexts + force push/delete false + required_approving_review_count + (b) admin scope 신규 contexts 추가 (사용자 영역) |
| **fixtures** | main branch protection rule (43 entry 답습) |

### §2.4 Layer 4 — CI 회귀 검증 (MANDATORY)

| 항목 | 내용 |
|------|------|
| **PoC 시제** | ✅ 4 workflows 분리 운영: `g4-hash-chain.yml` (10652B, 7 step) + `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) + `r2-canary.yml` (5476B) |
| **권위** | G4 §4.4.1 line 649~653 (PRIMARY) + ADR-012 §2.8 line 271 (SUPPORTING) |
| **PASS 격상 영역** | (a) Layer 1 (hash chain) 자동 회귀 검증 + Layer 2 (history) 자동 회귀 검증 + (b) canonical JSON 위반 검출 (RFC 8785 reference 동등성) + (c) timestamp monotonicity 검증 (ADR-012 §3.4) + (d) R-6 workflow 답습 확장 step (사용자 결정 영역, W-A/B/C/D/E 中 결정 = (β) 별도 cycle, 53 entry §2.3.2 답습) |
| **step prefix 권고** (53 entry N-5 답습) | g4-hash-chain.yml 7 step 답습 시 step prefix `[Layer N]` 권고 |
| **canonical test corpus** | ✅ `tests/canonical/` 72 files / 8 카테고리 (RFC 8785 reference ≥ 20 충족, 본 cycle §1.3 audit verify) |

#### §2.4.1 ⭐ workflow ↔ violation_type Layer 분담 매트릭스 (B-1 + B-5 흡수 — codex N-1 + Agent A R-A-1/R-A-2/R-A-3 답습)

⭐⭐⭐ **HISTORY_REWRITE enum fixture 미커버 + workflow internal numbering 명칭 충돌 + history-anchor-verifier.yml Layer 5 성격** (4 source filesystem direct cross-confirm):

| workflow | FAIL fixture cover | violation_type Layer 매핑 | 명칭 / 성격 주의 |
|---------|------------------|------------------------|---------------|
| `g4-hash-chain.yml` (10652B) | prev_hash + hash_recalc + **missing_event_field (schema)** + genesis_mismatch | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH = **Layer 1** + schema 1종 | ⚠️ **HISTORY_REWRITE 미cover** (Layer 1 영역 3종 + schema 한정) |
| `rewrite-defense.yml` (16454B) | append-only / rewrite-command / line-regression | **HISTORY_REWRITE = Layer 2** | ⚠️ **workflow internal numbering "(Layer 2/3/4)" ≠ G4 §4.4.1 Layer 1~5 모델** (B-5 흡수, evidence ownership 혼선 방지 명문 — workflow 自체 numbering 은 별도 의미) |
| `history-anchor-verifier.yml` (19094B) | 5 FAIL 패턴 (middle deletion 등) | history anchor 검증 | ⚠️ **workflow name = "(Layer 5)" — Layer 5 External anchor PoC 시제 *이미 운영 中*** (B-2 흡수). "부분 답습" framing = *결정 영역 진입 0* 의미이지 *PoC 시제 0* 아님. 본 cycle Layer 5 결정 영역 진입 0 (PoC 시제 존재 ≠ Layer 5 PASS 진입) |
| `r2-canary.yml` (5476B) | R-6 canary regression | R-6 workflow 답습 | (W 결정 = (β) 영역) |

→ ⭐ **HISTORY_REWRITE Layer 분담**: g4-hash-chain.yml (Layer 1 3종 + schema) ↔ rewrite-defense.yml + history-anchor-verifier.yml (Layer 2 HISTORY_REWRITE) cross-reference 명문. fixture 추가 권고 (N-1): history_rewrite enum jsonl_ledger/fail fixture 추가 = 실 구현 sub-cycle 영역.

→ ⭐ **history-anchor-verifier.yml Layer 5 성격 명시** (B-2): Layer 5 External anchor PoC 시제 19094B 이미 운영. "4 G4 workflows 시제" 언급 시 Layer 5 PASS 진입 오해 방지 제한 문구 유지 (N-2 답습). 본 cycle = "부분 답습" framing = Layer 1+2+4 *결정 영역* 한정 (Layer 3 Signed commit + Layer 5 External anchor *결정 영역 진입 0*, PoC 시제 존재는 별개).

→ ⭐ **rewrite-defense.yml "(Layer 2/3/4)" internal numbering 명칭 충돌** (B-5): workflow 自체 numbering ≠ G4 §4.4.1 Layer 1~5 모델. evidence ownership 혼선 방지 — PASS evidence template 작성 시 G4 §4.4.1 Layer numbering PRIMARY 기준 (workflow internal numbering 별도 의미 명시).

### §2.5 통합 PASS 격상 ((γ-c) 특화 의무 3 답습 — 통합 동시 발효)

본 (γ-c) 채택 발효 답습 — Layer 1+2+4 **통합** PASS evidence 동시 발효 의무 (54 entry §1.3 의무 3 영구 답습):

| 통합 영역 | evidence template ((γ-c) 특화 의무 1 답습 — Layer subsection 강제) |
|---------|-----------------------------------------------|
| Layer 1 evidence subsection | hash chain 검증 PoC PASS + 4 violation_type 검출 actual run + canonical JSON sha256 동등성 |
| Layer 2a evidence subsection | denyNonFastForwards 활성화 evidence + Docker 격리 PoC (force-push reject) + JSONL line deletion / rewrite 감지 actual run |
| Layer 2b evidence subsection | branch protection rule actual state (43 entry 8 contexts + force push/delete false) |
| Layer 4 evidence subsection | 4 G4 workflow actual run PASS + canonical 위반 BLOCK + timestamp monotonicity 위반 BLOCK + R-6 workflow 통합 step (W 결정 답습) |
| 통합 evidence subsection | Layer 1+2+4 동시 actual run PASS evidence (Layer evidence 합산 금지, 54 entry §1.3 의무 1 영구 답습) |

⚠️ **Layer 4 evidence 內 Layer 1+2 evidence 합산 영구 금지** (54 entry §5 #9 답습).

### §2.6 본 cycle 합의 발효 시 채택 결정 영역

✅ **Layer 1+2+4 통합 PASS 격상 진입 발효 자격** — 본 cycle 합의 APPROVE 시점 발효
✅ **후속 실 구현 sub-cycle 진입 자격 발효** — denyNonFastForwards 활성화 + R-6 workflow 확장 step + actual run PASS evidence 수집 sub-cycle (별도 사용자 명시)
✅ **PASS evidence template *후보 채택*** (Layer subsection 강제, 구현 발효 ≠ 본 합의)
✅ **Rollback Trigger 본문 *후보 채택*** (§5.1 답습, RT-γ-1~6 + RT-PASS-1~3 신규)
✅ **(γ-c) 특화 의무 4 영구 답습 보존** (Layer subsection 강제 + "부분 답습" framing + 통합 동시 + RT-γ-6)
✅ **RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가*** (정정 자체 = 별도 cycle)

### §2.7 미발효 영역 (deferred)

❌ Layer 1+2+4 통합 PASS 발효 자체 = 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도
❌ MVP-2 Implementation Evidence PASS 발효 = Layer 통합 PASS + GP-2 PASS + 통합 합의 후 별도
❌ (β) sub-수단 결정 (R-1~R-5 + L-1~L-5 + W-A~E) = 별도 cycle
❌ Layer 3 + Layer 5 영역 진입 = "부분 답습" framing 영구 답습 (54 entry §1.3 의무 2)
❌ R-S1 cross-reference 정정 자체 = 별도 cycle (RT-γ-6 평가 한정)

---

## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 — 5조건 매트릭스 (Layer 별 + 통합, 52 entry B-2 framing 답습)

| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
|---|------|------|------|------|----|
| (a) | 동등 이상 보안 결과 | hash chain middle tampering 차단 (PoC 시제 충족) | 2a force-push 차단 + 2b branch protection / history 재작성 차단 (2a 미설정 verify 의무) | CI 회귀 검증 (Layer 1+2 통합 회귀, PoC 시제 충족) | Layer 1+2+4 통합 (각 subsection 분리) |
| (b) | 격리 환경 PoC 실증 | ✅ tools/jsonl_hash_chain.py + fixtures (PoC 시제 충족) | 2a ⚠️ denyNonFastForwards 활성화 + Docker 격리 PoC (실 구현 sub-cycle 의무) / 2b ✅ branch protection 답습 | ✅ 4 G4 workflow PoC 시제 충족 + R-6 actual run (실 구현 sub-cycle 의무) | 통합 evidence (Layer subsection 분리 강제) |
| (c) | ADR / SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.3 + §2.8 | ✅ 동상 | ✅ 동상 | ✅ 동상 |
| (d) | 자동 회귀 검증 경로 확보 | Layer 4 CI step 內 hash chain 검증 (R-6 workflow 답습) | Layer 4 CI step 內 base branch JSONL line deletion / rewrite 감지 | R-6 workflow 답습 확장 step (W 결정 = (β) 영역) | 통합 R-6 확장 step |
| (e) | 합의 APPROVE | ❌ gap — 본 cycle (α) 진입 합의 → 발효 ≠ 본 cycle (Layer 통합 PASS 발효 = 별도) | ❌ 동상 | ❌ 동상 | ❌ 동상 |

⭐ **(e) row 분리 (B-6 흡수 — Agent B R-B-1 답습, 자가 모순 정정)**:
- **(e1) 진입 권한** = ✅ **본 cycle 충족** (PASS 격상 *진입* 합의 발효)
- **(e2) PASS 발효** = ❌ **gap** (Layer 통합 PASS *발효* = 실 구현 + (a)~(d) evidence + 합의 APPROVE + 사용자 명시 후 별도 합의)

→ **본 cycle (e1) 진입 권한 충족 / (e2) PASS 발효 ≠ 본 합의 (별도 합의)**. "동일 (e)가 gap이면서 충족" 자가 모순 정정 (Agent B R-B-1 답습).

→ **PoC 시제 충족 영역 = (a)+(b)+(c)+(d) 부분 충족**. PASS 시제 = 실 구현 sub-cycle (denyNonFastForwards 활성화 + R-6 actual run + evidence 수집) 후 (e2) 통합 PASS 발효 합의.

---

## §4 합의 형태 + 풀 3+1 승격 트리거 검증

### §4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (53/54 entry 답습 정당화)

**합의 형태**: **풀 3+1 + 외부 LLM 1+ (cross-vendor 의무)**

**정당화 출처**:
1. 53 entry brief §8.1 항목 3 + 54 entry SESSION carry-over #5 — "Layer 1+2+4 통합 PASS 격상 cycle = 풀 3+1 + 외부 LLM 1+" 직접 답습
2. (γ-c) 채택 발효 답습 (54 entry) — 큰 결정 (PASS 격상 진입 발효 = MVP-2 Implementation Evidence PASS 발효 *직전 단계*)
3. 32 entry MVP-1 PASS 발효 합의 답습 패턴 (풀 3+1 + 외부 LLM 1+)
4. 24/52 entry entry brief 동형 패턴 답습
5. 헌법 5조-2 Provider Liquidity (cross-vendor 의무)
6. ADR-011 §2.1 (e) + §2.4 T3 영역

### §4.2 (γ-c) 특화 의무 4 영구 답습 (54 entry §1.3 답습)

본 cycle = (γ-c) 채택 발효 답습 한정. 특화 의무 4 영구 보존:

| # | 의무 | 본 brief 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/Layer 2/Layer 4 subsection 강제 | §2 Layer 별 분리 + §3 매트릭스 Layer 별 컬럼 + §5.2 evidence template 후보 (Layer subsection 강제) |
| 2 | "defense-in-depth 부분 답습" framing 영구 유지 (Layer 3+5 = scope 외) | §2.1 + §6 영구 답습 + §0.3 #20 명시 금지 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 | §2.5 통합 영역 + §3 통합 매트릭스 |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 평가 의무 | §5.2 평가 + §8 #5 명문 |

### §4.3 7 풀 3+1 승격 트리거 검증

| # | trigger | 본 cycle 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (PASS 격상 진입 발효 / sub-수단 결정 / threshold 고정) | ✅ **발화** | Layer 1+2+4 통합 PASS 격상 *진입* 합의 = MVP-2 PASS 발효 *직전 단계* (큰 영역) |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화** (R-S1 후행 영향 RT-γ-6, 52/53 entry 발견 cascade) | 본 cycle = 후행 영향 평가 한정, 정정 = 별도 cycle |
| 5 | 외부 LLM 응답 통합 필요성 | ✅ **발화** | 큰 결정 + cross-vendor 의무 (53/54 entry 답습) |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #13 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 #17 명시 금지 |

→ **2/7 발화 + 1 부분 발화 → 풀 3+1 + 외부 LLM 1+ 합의 적격 (정당화)**.

### §4.4 ⭐ 합의 형태 + denyNonFastForwards + PASS evidence template 대안 매트릭스 (B-9 흡수 — Agent C R-C-1/2/3 답습)

#### §4.4.1 합의 형태 4 대안 (R-C-1 답습)

| 대안 | trigger 발화 | 적격성 |
|------|---------|------|
| (a) **풀 3+1 + 외부 LLM 1+** | trigger 1 (큰 결정) + trigger 5 (외부 LLM) 발화 | ✅ **정합 (본 cycle 채택)** |
| (b) audit-only 단축 (Reviewer-only) | trigger 1 (큰 결정) 발화 | ❌ 부적격 (trigger 1 발화 → 단축 부적격) |
| (c) 1-agent 직접 | trigger 1 발화 | ❌ 영역 침입 (큰 결정) |
| (d) 단계별 합의 (Layer 1/2/4 분리) | — | ❌ (γ-c) 통합 동시 의무 위반 (54 entry §1.3 의무 3) |

#### §4.4.2 denyNonFastForwards 5 활성화 대안 (R-C-2 + N-10 답습)

| 대안 | 영역 | trade-off |
|------|----|---------|
| (a) `--system` (system-wide) | root 권한 | ⚠️ root 권한 + 다른 repo 영향 risk |
| (b) `--global` (user-global) | user 전역 | ⚠️ 다른 repo 영향 |
| (c) per-repo (`git config receive.denyNonFastForwards true`) | 본 repo | ✅ 영향 최소 |
| (d) entrypoint script + pre-receive hook + Dockerfile | 컨테이너 | ✅ reproducible + 강제 |
| (e) GitHub Actions pre-receive (remote 보조) | remote | 보조 (Layer 2b 답습) |

→ **권고 (실 구현 sub-cycle 영역): (c) per-repo + (d) entrypoint script + Dockerfile 조합** (PoC 시제 + reproducible + 영향 최소, R-C-2 답습). 결정 = 실 구현 sub-cycle (별도 사용자 명시).

#### §4.4.3 PASS evidence template 3 대안 (R-C-3 답습)

| 대안 | 검출 능력 | 적격성 |
|------|--------|------|
| (i) **Layer subsection 강제** | RT-PASS-2 검출 가능 + 통합 동시 발효 정합 | ✅ **권고 ((γ-c) 특화 의무 1 영구 답습)** |
| (ii) 통합 evidence + Layer tag | RT-PASS-2 검출 약화 | ❌ 부적격 |
| (iii) layer evidence file 분리 | 통합 동시 발효 의무 위반 | ❌ 부적격 ((γ-c) 특화 의무 3 위반) |

→ **(i) Layer subsection 강제 유지** ((γ-c) 특화 의무 1 영구 답습).

---

## §5 Rollback Trigger / Evidence *후보 채택* (구현 발효 ≠ 본 합의, 52/53 entry N-1 답습)

### §5.1 Rollback Trigger 본문 후보 (53 entry §5.1 답습 + 본 cycle 신규)

| # | Trigger | 영역 | 발화 조건 | 발화 시점 | 권위 답습 |
|---|---------|----|---------|---------|---------|
| RT-γ-1 | Layer 1+2 PoC 시제 회귀 | 모든 | tools/* 본문 변경 시 PoC 시제 미작동 | 후속 sub-cycle | 53 entry §5.1 답습 |
| RT-γ-4 | Layer 1 violation_type 검출 실패 | Layer 1 | PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH 미작동 | 실 구현 sub-cycle | 53 entry N-6 답습 |
| RT-γ-5 | (γ-d) Layer 4 PASS 선발효 시도 (영구 금지 위반) | (γ-d) 비채택 답습 | Layer 4 PASS 발효 + Layer 1+2 미발효 | 영구 금지 (54 entry §5 #3 답습) | 53 entry §2.4.5 + B-1 답습 |
| RT-γ-6 | R-S1 cross-reference 정정 후행 영향 + **MVP-2 PASS 시점 선행/동시 정정 평가** | 모든 (γ-c 특화 의무 4 답습) | ADR-012 §2.3 본문 정정 + MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 평가 | 본 cycle + Layer 통합 PASS 발효 + MVP-2 PASS 발효 | 52 entry §9.5 + 53 entry §5.1 + 54 entry §1.3 의무 4 답습 |
| **RT-PASS-1** ⭐ (신규) | denyNonFastForwards 활성화 실패 | Layer 2a | 실 구현 sub-cycle 활성화 후 force-push 시도 reject 실패 | 실 구현 sub-cycle | 53 entry B-3 + 본 brief §1.3 audit 답습 |
| **RT-PASS-2** ⭐ (신규) | Layer 4 evidence 內 Layer 1+2 evidence 합산 (subsection 미준수) | (γ-c) 특화 의무 1 위반 | PASS evidence template Layer subsection 분리 미준수 | Layer 통합 PASS 발효 시점 | 54 entry §1.3 의무 1 + §5 #9 답습 |
| **RT-PASS-3** ⭐ (신규) | "defense-in-depth 충실 답습" 또는 "완전 답습" 표현 사용 | (γ-c) 특화 의무 2 위반 | Layer 3+5 scope 외 framing 영구 위반 | 본 cycle 후 모든 시점 | 54 entry §1.3 의무 2 + §5 #8 답습 |

⭐ **RT-PASS-2/3 계산적 sensor 후보 (B-3 흡수 — Agent B R-B-2 + Agent C N-C-2 답습, CLAUDE.md §2 계산적 검증 우선)**: "완전 답습" / "충실 답습" = grep-able 패턴 → **pre-commit grep sensor 후보** (RT-PASS-3) + **Layer subsection lint sensor 후보** (RT-PASS-2, PASS evidence template Layer 1/2/4 subsection 분리 검증). 추론적 검증 only 약화 회피 — 계산적 sensor 우선. 식별만, 실 구현 = 별도 sub-cycle.

### §5.2 Evidence Required (Layer subsection 강제, (γ-c) 특화 의무 1 답습)

| # | Evidence | Layer subsection | 출처 |
|---|---------|-----------------|------|
| E-PASS-1 | hash chain 검증 PoC PASS evidence | Layer 1 | Docker 격리 PoC (middle tampering 차단) |
| E-PASS-2 | 4 violation_type 검출 actual run evidence | Layer 1 | tools/jsonl_hash_chain.py + fixtures |
| E-PASS-3 | canonical JSON sha256 동등성 evidence | Layer 1 | canonical_json.py + tests/canonical/ 72 files |
| E-PASS-4 | genesis hash 첫 entry actual evidence | Layer 1 | jsonl_hash_chain.py + audit log |
| E-PASS-5 | denyNonFastForwards 활성화 evidence | Layer 2a | git config + Docker 격리 PoC (force-push reject) |
| E-PASS-6 | base branch JSONL line deletion / rewrite 감지 evidence | Layer 2 | Layer 4 CI step actual run |
| E-PASS-7 | branch protection rule actual state | Layer 2b | gh api (43 entry 8 contexts 답습) |
| E-PASS-8 | 4 G4 workflow actual run PASS evidence | Layer 4 | GitHub Actions run ID + verdict PASS (42 entry actual run id `25623028888` 답습, 52 entry N-6 답습) |
| E-PASS-9 | canonical 위반 BLOCK PoC | Layer 4 | Docker 격리 + RFC 8785 reference mismatch |
| E-PASS-10 | timestamp monotonicity 위반 BLOCK PoC | Layer 4 | Docker 격리 + ADR-012 §3.4 답습 |
| E-PASS-11 | R-6 workflow 확장 step actual run PASS (W 결정 답습) | Layer 4 | (β) sub-수단 결정 cycle 후 |
| E-PASS-12 | 통합 evidence (Layer subsection 분리 명시) | 통합 | 본 cycle PASS evidence template (Layer subsection 강제, (γ-c) 특화 의무 1) |
| E-PASS-13 | 합의 보고서 commit | 통합 | 본 cycle Reviewer 통합 + 후속 PASS 발효 합의 |
| E-PASS-14 | 외부 LLM 1+ 응답 (cross-vendor) | 통합 | `docs/external-review/2026-05-28-mvp2-layer-124-pass-*.md` |
| E-PASS-15 ⭐ (RT-γ-6 + B-8 흡수) | R-S1 cross-reference 정정 *자격* 평가 evidence | 통합 | ADR-012 §2.3 vs §2.8 정정 cycle 진행 상태 + MVP-2 PASS 시점 선행/동시 정정 *자격* 평가 (B-8 흡수 — "의무" → "*평가* 의무" framing 정정, MVP-2 PASS 합의가 R-S1 정정 결과에 종속 회피, 54 entry verbatim "평가 의무" 답습). R-S1 hard gate 3 옵션: (1) ADR-012 §2.3 본문 정정 / (2) §2.8 동형 답습 강화 / (3) "G4 §4.4.1 numbering PRIMARY / ADR-012 §2.3 principle-only" 권위 선언 (codex §6 + N-18 답습) |

---

## §6 금지 사항

### §6.1 본 brief 자체 금지 사항

§0.3 답습 (30 항목).

### §6.2 본 brief 발효 후 후속 cycle 진입 시점 금지 사항

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 후속 실 구현 sub-cycle 진입 | 사용자 명시 의무 |
| 2 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | Layer 4 PASS 선발효 ((γ-d) 모순, RT-γ-5) | 영구 금지 (54 entry §5 #3 답습) |
| 4 | Layer 4 evidence 內 Layer 1+2 evidence 합산 (Layer subsection 미준수, RT-PASS-2) | 영구 금지 ((γ-c) 특화 의무 1, 54 entry §5 #9 답습) |
| 5 | "defense-in-depth 충실 답습" / "완전 답습" 표현 (RT-PASS-3) | 영구 금지 ((γ-c) 특화 의무 2, 54 entry §5 #8 답습) |
| 6 | Layer 3 (Signed commit) + Layer 5 (External anchor) 자동 진입 | "부분 답습" framing 영구 답습, 별도 cycle |
| 7 | (γ-a/b/d) 대안 재평가 자동 진입 | 54 entry (γ-c) 채택 결정 영구 발효 답습 |
| 8 | MVP-2 Implementation Evidence PASS 자동 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 + R-S1 RT-γ-6 평가 후 별도 |
| 9 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 평가 한정) |
| 10 | branch protection contexts 자동 추가 | 사용자 admin scope 영역 |
| 11 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit |

---

## §7 외부 LLM 응답 요구 영역 (사용자 영역)

### §7.1 외부 LLM 1+ 권고 출처

1. 53 entry brief §8.1 항목 3 + 54 entry SESSION carry-over #5 직접 답습
2. 헌법 5조-2 Provider Liquidity (비협상)
3. ADR-011 §2.1 (a)~(d) + (e) + §2.4 T3 영역
4. 24/32/52/53 entry entry brief 동형 패턴 답습

### §7.2 외부 LLM 자격 옵션 (53 entry N-15 답습 — (E-α/β/γ) 명칭 분리)

| 옵션 | 영역 | 합의 형태 |
|------|----|---------|
| **(E-α)** Claude tmux + codex 직접 호출 (network-isolated 환경, `--dangerously-bypass-approvals-and-sandbox` flag = externally-sandboxed 환경 전용, B-7 흡수 — "bypass sandbox" 보안 wording 약화 정정, 헌법 8조 답습) | 24/52/53 entry 답습 | 풀 3+1 + 외부 LLM 1+ |
| **(E-β)** 사용자 직접 외부 LLM 호출 | 추가 cross-vendor | 풀 3+1 + 외부 LLM 2+ |
| **(E-γ)** 외부 LLM 0 (작은 영역) | 작은 영역 결정 | 풀 3+1만 |

### §7.3 외부 LLM 응답 *입력 자료* (52 entry N-11 + 53 entry §7.3 답습)

| 필수 입력 | 자료 위치 |
|---------|---------|
| 본 brief v1 | `docs/phase0/mvp2-layer-124-pass-entry-brief.md` |
| 54 entry decision brief + 1-agent 직접 합의 | `docs/phase0/mvp2-gamma-decision-brief.md` + `docs/review/1agent-decision-2026-05-28-mvp2-gamma-c-adoption.md` |
| 53 entry (γ) brief v1.1 + Reviewer 통합 합의 + codex 응답 | `docs/phase0/mvp2-gamma-layer-separation-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` + `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` |
| 52 entry (α) entry brief v1.1 + Reviewer 통합 합의 | `docs/phase0/mvp2-entry-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
| `provider-agnostic-memory-skill-design.md §4.4` | 답습 source |
| `ADR-012 §2.3 + §2.5 + §2.7 + §2.8 + §3.4` | 답습 source |
| **`ADR-011 §2.1` + `PROJECT_CONSTITUTION` (헌법 8조 + 5조-2)** (52 entry N-11 답습) | 답습 source |

---

## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 cycle 합의 APPROVE 발효 후 (사용자 명시 의무):

1. **(β) sub-수단 결정 cycle** — R-1~R-5 + L-1~L-5 + W-A~E (수단별 차등) — 풀 3+1
2. **실 구현 sub-cycle** — denyNonFastForwards 활성화 + R-6 workflow 확장 step 통합 + evidence 수집 (E-PASS-1~14) — 수단별 차등
3. **Layer 1+2+4 통합 PASS 발효 합의** — (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (32 entry 답습)
4. **MVP-2 Implementation Evidence PASS 발효 합의** — Layer 통합 PASS + GP-2 PASS + 통합 합의 (32 entry 답습)
5. ⭐ **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 강화 또는 "G4 §4.4.1 numbering PRIMARY / ADR-012 §2.3 principle-only" 권위 선언 (3 옵션, RT-γ-6 답습 + MVP-2 PASS 시점 선행/동시 정정 *자격* 평가 후, B-8 흡수 — MVP-2 PASS 합의 R-S1 종속 회피)
6. (γ-e/f/g) hybrid 대안 결정 cycle (선택)
7. ADR 본문 cross-reference 갱신 별도 commit

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §9 답습 참조

### §9.1 상위 권위

- 헌법 제8조 (보안) — `docs/constitution/PROJECT_CONSTITUTION.md`
- 헌법 제5조-2 (Provider Liquidity 비협상) — 동상
- ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`

### §9.2 직접 선행 자료

- 54 entry decision brief + 1-agent 직접 합의 ((γ-c) 채택 발효 답습 source)
- 53 entry (γ) brief v1.1 + Reviewer 통합 합의 + codex 응답
- 52 entry (α) entry brief v1.1 + Reviewer 통합 합의
- 32 entry MVP-1 PASS 발효 합의
- `provider-agnostic-memory-skill-design.md §4.4`
- `ADR-012-evidence-ledger-protection.md §2.3 + §2.5 + §2.7 + §2.8 + §3.4`

### §9.3 메타 영역 (본 cycle audit 답습)

PoC 시제 (filesystem evidence, 2026-05-28 audit):
- `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type)
- `tools/canonical_json.py` (10055B)
- `tests/canonical/` (72 files / 8 카테고리 / 24 fixtures input verify 완료)
- 4 G4 workflows (g4-hash-chain.yml 10652B + history-anchor-verifier.yml 19094B + rewrite-defense.yml 16454B + r2-canary.yml 5476B)
- `tests/fixtures/jsonl_ledger/{pass,fail}/` (다수 fixture)
- `tests/fixtures/history_anchor_verifier/` (다수 fixture)
- ⚠️ `git config receive.denyNonFastForwards` 미설정 (실 구현 sub-cycle 활성화 의무, B-3 답습)

### §9.4 cross-reference 갱신 영역 (별도 commit, 본 cycle scope 외)

- Layer 1+2+4 통합 PASS evidence template (Layer subsection 강제, (γ-c) 특화 의무 1 답습)
- R-S1 cross-reference 정정 (52/53 entry §9.5 + RT-γ-6 + MVP-2 PASS 시점 선행/동시 평가)
- ADR-008 차단조건 #1 보조 cross-reference 추가
- ADR-012 §2.2 event enum amendment (gp2_redaction_layer1_implementation 등, 52 entry N-A-3 답습)
- ADR-011 §8.5 후속 작업에 Layer 통합 PASS 등록

---

## §10 본 brief v1 작성 자격 자기진단 (메타 편향 회피)

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 brief 가 PASS 격상 진입을 *권유* 방향으로 편향 | §0.3 + §6.2 30+11 금지 + §0.4 권위 한계 = "본 brief 자체에서 PASS 발효 0" 영구 분리 |
| P-2 | (γ-c) 특화 의무 4 영구 답습 강조가 결정 영역 침입 risk | §1.2 + §4.2 = 54 entry §1.3 답습 한정 (Reviewer 통합 권고 답습 + 1-agent 직접 합의 발효 답습) |
| P-3 | PoC 시제 충족 발견 (§1.3 + §2.5) 이 PASS 발효 단순화 risk | §2.7 + §3 (e) gap 명시 + §6.2 #8 "MVP-2 PASS 자동 선언 금지" 영구 답습 |
| P-4 | denyNonFastForwards 미설정 발견 (§1.3) 이 실 구현 자동 진입 risk | §6.2 #1 명시 + §0.3 #5 명시 (활성화 = 실 구현 sub-cycle 영역, 본 cycle scope 외) |
| P-5 | RT-γ-6 R-S1 후행 영향 평가가 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습 + 본 cycle = *평가* 한정 (정정 ≠ 본 cycle) |
| P-6 | 외부 LLM 1+ 권고 사용자 영역 침입 risk | §7.2 자격 옵션 3 (사용자 영역 결정) |
| P-7 | 본 brief 작성자 = 52/53/54 entry brief 작성자 (Claude Opus 4.7) → cascade risk | §1.1 선행 권위 답습 + §1.2 (γ-c) 특화 의무 4 답습 = 54 entry 답습 한정 (Reviewer 통합 권고 + 1-agent 직접 합의 발효 답습 보존). 본 brief = 답습 cascade 정합성 검증 + cross-vendor 후속 합의 시 codex (E-α) 호출 답습 (53 entry 답습, cross-vendor 형식 충족) |
| P-8 ⭐ (신규) | tests/canonical 24 fixture 정량 verify (72 files / 8 × 3 × 3) 가 52 entry Agent A R-A-2 carry-over 해소 자격 | §1.3 audit + §9.3 명시. 본 cycle audit = filesystem direct (find 명령 verify 완료), 52 entry carry-over 해소 evidence |

---

---

## §11 v1.1 보강 매트릭스 (BLOCKING 9 + 권고 18 1pass 흡수)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass.md` §6 답습 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단, 24/52/53 entry 동형 패턴).

### §11.1 BLOCKING 9 흡수 매트릭스

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| B-1 (HISTORY_REWRITE Layer 분담) | §2.4.1 신규 | g4-hash-chain.yml FAIL = Layer 1 3종 + schema 1종, HISTORY_REWRITE = rewrite-defense.yml + history-anchor-verifier.yml Layer 2 분담 cross-reference (codex N-1 + Agent A R-A-1 답습) |
| B-2 (history-anchor Layer 5 명시) | §2.4.1 + §2.1 framing | history-anchor-verifier.yml = Layer 5 External anchor PoC 시제 19094B 이미 운영. "부분 답습" = 결정 영역 진입 0 (PoC 시제 0 아님) (codex N-8 + Agent A R-A-3 답습) |
| B-3 (RT-PASS 계산적 sensor) | §5.1 RT-PASS-2/3 | pre-commit grep + Layer subsection lint sensor 후보 (Agent B R-B-2 + Agent C N-C-2 답습) |
| B-4 (codex 조건부 승인 조건 6) | §4.4 + §5.2 + §8 | denyNonFastForwards 활성화 + R-6 actual run + 4 G4 workflow actual run + R-S1 정정 평가 + violation_type 정밀화 + Layer subsection 분리 |
| B-5 (rewrite-defense 명칭 충돌) | §2.4.1 | workflow internal numbering "(Layer 2/3/4)" ≠ G4 §4.4.1 Layer 1~5, evidence ownership 혼선 방지 (Agent A R-A-2 답습) |
| B-6 (§3 (e) 자가 모순) | §3 (e) row 분리 | (e1) 진입 권한 충족 + (e2) PASS 발효 gap 분리 (Agent B R-B-1 답습) |
| B-7 ("bypass sandbox" wording) | §7.2 (E-α) | "codex 직접 호출 (network-isolated 환경)" framing 정정 (Agent B R-B-3 답습) |
| B-8 ("의무" → "평가 의무") | §5.2 E-PASS-15 + §8 #5 | "R-S1 정정 *자격* 평가" (MVP-2 PASS R-S1 종속 회피, Agent B R-B-4 + 54 entry verbatim 답습) |
| B-9 (3 대안 매트릭스) | §4.4 신규 | 합의 형태 4 대안 + denyNonFastForwards 5 대안 + PASS evidence template 3 대안 (Agent C R-C-1/2/3 답습) |

### §11.2 권고 18 흡수 매트릭스

§4.4 + §5.1 + §5.2 + §8 in-place 흡수 (N-1~N-18). 핵심: N-4 (시점-β) Layer 통합 PASS = MVP-2 PASS 선행 권고 + N-10 denyNonFastForwards (c)+(d) 조합 + N-15 P-8 carry-over 해소 evidence + N-16/17 codex 실 venv 실행 evidence (Layer 1 hash chain PASS + canonical cross_check PASS) + N-18 R-S1 hard gate 3 옵션.

### §11.3 v1.1 1pass 흡수 정직성

- 본 cycle = 1pass 흡수 (ceremony-inflation 차단, 24/52/53 entry 동형)
- 별도 v2 cycle 0건
- 본 v1.1 보강 = 핵심 BLOCKING in-place (§2.4.1 + §3 + §4.4 + §5.1 + §5.2 + §7.2 + §8) + §11 매트릭스 신설

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push (55 entry) → 본 cycle 합의 발효 (APPROVE WITH CONDITIONS 자동 격상) → (β) sub-수단 결정 + 실 구현 sub-cycle (조건부 승인 조건 6 우선) + Layer 통합 PASS 발효 합의 + MVP-2 PASS 발효 합의 = 사용자 명시 별도 cycle.
