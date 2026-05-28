# Layer 1+2+4 통합 PASS 발효 합의 entry brief (v1.1)

> **작성**: 2026-05-28 (59번째 entry 진입 cycle — 신규 세션 #2)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md`) **APPROVE WITH CONDITIONS (4 source 전원) → BLOCKING 3 + 권고 4 1pass 흡수**. 정정: B-1 citation (`6ebc634`→`052e583`) / B-2 ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 / B-3 2a denyNonFastForwards = non-bare clone no-op (DEFER 강화) + N-1 2a DEFER 이중 cover (2b + rewrite-defense CI). evidence 4 source 전원 실증 (over-claim 0). §12 흡수 매트릭스 추가.
>
> **scope**: G4 §4.4 Layer 1+2+4 통합 Implementation Evidence PASS **발효 (e2)** — 55 entry 진입 권한 (e1) → 본 cycle 발효 (e2)
>
> **본 cycle = 큰 cycle** (PASS *발효* milestone, 풀 3+1 + 외부 LLM 1+ 의무, 32 entry MVP-1 PASS 발효 답습 동형)
>
> **본 cycle 발효 자격** = (a)~(d) evidence + (e2) 풀 3+1 + 외부 LLM 1+ 합의 APPROVE + 사용자 명시
>
> **본 cycle 발효 효과** = **Layer 1+2+4 통합 PASS 발효** (G4 §4.4 Layer 1+2+4 부분 답습 — Layer 3+5 scope 외). MVP-2 Implementation Evidence PASS = Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도 cycle
>
> **선행 답습**: 55 (Layer 1+2+4 통합 PASS 격상 진입 권한, `311ca3b`) + 57 ((β) R-4/L 보존/W-F 결정, `18e8ad1`) + 58 (실 구현 violation_type 정밀화, `6ebc634`, 3 G4 workflow actual run green)

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **Layer 1/2a/2b/4 evidence 매트릭스 — Layer subsection 강제** ((γ-c) 특화 의무 1, E-PASS-12) (§2)
2. **ADR-011 §2.1 (a)~(d) 모법 + (e2) PASS 발효 자격 매핑** (Layer 별 + 통합) (§3)
3. **gap / DEFER 처리** — Layer 2a denyNonFastForwards DEFER (57/58 비례 보안 결정) + E-PASS-10 timestamp fixture + r2-canary (§4)
4. **R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가** ((γ-c) 특화 의무 4) (§5)
5. **합의 형태 = 풀 3+1 + 외부 LLM 1+ 정당화 + 승격 트리거** (§6)
6. **PASS 발효 권고 + 조건** (§7)
7. 금지 / 다음 단계 / cross-ref / 자기진단 (§8~§11)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | Layer 통합 PASS *발효* 자체 (본 brief = 합의 입력, 발효 = 합의 APPROVE + 사용자 명시 후) | 0건 |
| 2 | **MVP-2 Implementation Evidence PASS 발효** (Layer 통합 PASS + GP-2 PASS + R-S1 후 별도) | 0건 |
| 3 | GP-2 송신 redaction PASS 발효 (별도 영역 — R-3 secret-hygiene actual run + R-1/R-2 trajectory) | 0건 |
| 4 | denyNonFastForwards 활성화 실행 (57/58 DEFER 답습, 비례 보안) | 0건 |
| 5 | Layer 3 (Signed commit) + Layer 5 (External anchor) 영역 진입 ("부분 답습" framing 영구) | 0건 |
| 6 | R-S1 cross-reference 정정 자체 (RT-γ-6 = 평가 한정, 정정 = 별도 cycle) | 0건 |
| 7 | 신규 외부 library 도입 (rfc8785/jcs = Q1 합의 보존, 57 (β) 답습) | 0건 |
| 8 | Hermes import (R-1) / facade real (R-2, TR-1) | 0건 |
| 9 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 |
| 10 | threshold 고정 / Tier-2/3 catalog 확장 | 0건 |
| 11 | MVP-1 PASS 재선언 (32 entry 답습 유지) | 0건 |
| 12 | (γ-a/b/d) + (γ-e/f/g) 재평가 | 0건 |
| 13 | 자동 후속 cycle 진입 (MVP-2 PASS / R-S1 정정) | 0건 (사용자 명시 의무) |
| 14 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |

### §0.3 권위 답습 source

- **ADR-011 §2.1 (a)~(d) 4조건 모법** (line 52~61) — `docs/decisions/ADR-011-means-vs-ends-redaction.md` (B-2: §2.1 = (a)~(d), (e) 아님)
- **ADR-012 §4 (a)~(d) + (e) 5조건 답습 확장** (PASS 발효 (e2) 권위 출처) — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **55 Layer 1+2+4 통합 PASS 격상 brief v1.1 §2.5 (통합) + §3 ((e1)/(e2) 분리) + §5.2 (E-PASS-1~15)** — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- **57 (β) sub-수단 결정 brief v1.1 (R-4/L 보존/W-F) + 합의** — `docs/phase0/mvp2-beta-submeans-decision-brief.md`
- **58 실 구현 (violation_type 정밀화)** — 실 구현 commit `052e583` (`tools/jsonl_hash_chain.py` + `tests/tools/test_jsonl_hash_chain.py`, B-1 정정 — `6ebc634` = docs/session CI 증거 기록 commit) + 3 G4 actual run (`26557460199` + `26557460227` + `26557460197`, headSha `052e583`)
- **32 entry MVP-1 Implementation Evidence PASS 발효 합의** (PASS 발효 패턴 답습) — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5) + **ADR-012 §2.3/§2.5/§2.7/§2.8/§3.4**
- **본 cycle audit (read-only, 2026-05-28)** — evidence 가용 상태 filesystem + gh api + CI run direct

---

## §1 진입 컨텍스트 + (e1) → (e2) 전이

### §1.1 선행 chain (55 → 57 → 58)

| 합의/구현 | 본 cycle 답습 |
|----------|-----------|
| 55 통합 PASS 격상 **진입 권한 (e1)** (`311ca3b`, 4 source APPROVE WITH CONDITIONS, BLOCKING 9 + 권고 18) | (e1) 진입 권한 발효 답습 → 본 cycle = (e2) PASS 발효 |
| 57 (β) **수단 결정** (`18e8ad1`, R-4 / L 보존(rfc8785/jcs) / W-F + W-E 보조) | PASS 발효 시 채택 수단 = R-4/L 보존/W-F 답습 |
| 58 **실 구현** violation_type 정밀화 (`052e583`, HISTORY_REWRITE Layer 1 제거, 3 G4 workflow actual run green; B-1 정정 — `6ebc634` = docs/session CI 증거 commit) | Layer 1 evidence 강화 + Layer 4 actual run 증거 (E-PASS-2/8) |

### §1.2 (γ-c) 특화 의무 4 영구 답습

| # | 의무 | 본 brief 답습 |
|---|------|-----------|
| 1 | PASS evidence template Layer 1/2/4 subsection 강제 | §2 Layer subsection 분리 (E-PASS-12) |
| 2 | "defense-in-depth 부분 답습" framing (Layer 3+5 = scope 외) | §0.2 #5 + §2 "부분 답습" 표현 |
| 3 | Layer 1+2+4 통합 PASS evidence 동시 발효 (evidence 합산 금지) | §2.5 통합 (Layer subsection 분리 유지) |
| 4 | RT-γ-6 R-S1 PASS 시점 선행/동시 정정 *평가* 의무 | §5 평가 (정정 = 별도 cycle) |

---

## §2 Evidence 매트릭스 (Layer subsection 강제 — E-PASS-12, (γ-c) 의무 1)

⚠️ **Layer 별 evidence subsection 분리 강제, Layer 간 evidence 합산 금지** (54 entry §5 #9 / RT-PASS-2 답습).

### §2.1 Layer 1 — Hash Chain (MANDATORY) ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-1: hash chain PASS fixture rc=0 (× 2) | ✅ | `g4-hash-chain.yml:182` PASS fixture step (minimal_chain + roundtrip_t2_strict), 58 actual run `26557460199` green |
| E-PASS-2: violation_type 검출 actual run | ✅ | `g4-hash-chain.yml:197` FAIL fixture (prev_hash_mismatch + hash_recalculation + genesis_mismatch + schema_missing_field), 58 entry violation_type 정밀화 (HISTORY_REWRITE Layer 1 제거 → 3 Layer-1 type + schema) |
| E-PASS-3: canonical JSON sha256 동등성 | ✅ | corpus 회귀 Primary 1 (rfc8785) + Primary 2 (jcs) byte+sha256 + jq fallback equivalence (`tests/canonical/` 72 files / 8 카테고리) + NaN/Inf reject |
| E-PASS-4: genesis hash 첫 entry | ✅ | `compute_genesis_hash` + genesis_mismatch fixture |

→ **Layer 1 = 완전 충족** (PoC 시제 + actual run green + 58 violation_type 정밀화).

### §2.2 Layer 2a — local denyNonFastForwards ⚠️ DEFER

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-5: denyNonFastForwards 활성화 + force-push reject PoC | ⚠️ **DEFER** | 57/58 사용자 비례 보안 결정. ⭐ **B-3 정정**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동 — 본 repo = 비-bare 작업 clone (push 대상 = GitHub) → 본 clone 활성화 = **no-op (효과 0, "영향 최소" 아님)**. operative append-only 보호 = Layer 2b (§2.3) + rewrite-defense.yml CI (§2.4) |

→ **Layer 2a = DEFER** (B-3: 본 clone no-op, 켤 이유 소멸). ⭐ **N-1 — Layer 2 append-only ends 이중 cover** (ADR-012 §2.3 Layer 2 = denyNonFastForwards/branch protection/pre-commit/CI **4 means 동시 열거**, 단일 수단 종속 0): (1) Layer 2b branch protection (allow_force_pushes/deletions false + enforce_admins true) + (2) rewrite-defense.yml Layer 4 CI (`non_fast_forward_detected` / `history_reorder_detected` 검출, actual run green). 2a 가 막으려는 시나리오를 2 layer 가 이미 cover. 2a = 실 bare/server 배포 trigger 시점 (별도, [[feedback_proportionate_security_personal_tool]]).

### §2.3 Layer 2b — remote branch protection ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-7: branch protection rule actual state | ✅ | gh api main protection 8 contexts = `["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]` + allow_force_pushes false + allow_deletions false + **enforce_admins true** (N-4, 43 entry 답습) |

### §2.4 Layer 2 — history (rewrite/deletion 검출) ✅

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-6: base branch JSONL line deletion/rewrite 감지 actual run | ✅ | `rewrite-defense.yml` (58 actual run `26557460227` green) + `history-anchor-verifier.yml` (58 actual run `26557460197` green) + FAIL fixtures 8 (append_only force_push/reorder + line_regression deletion/rewrite + anchor full_rewrite/middle_deletion/substitution/tail_truncation) |

⚠️ **N-3 (Layer 5 framing)**: `history-anchor-verifier.yml` 은 이름이 "Layer 5 External Anchor Verifier" 이나, 본 cycle 은 이를 **Layer 2 history rewrite 검출 보조 evidence 로만 인용** (Layer 5 External anchor *PASS 진입 발효 0*). "부분 답습" framing 유지 (Layer 3+5 scope 외, 55 entry B-2 답습).

→ **Layer 2 = 충족** (2b operative + rewrite-defense CI 이중 cover + history 검출 actual run green, 2a DEFER no-op 문서화).

### §2.5 Layer 4 — CI 회귀 검증 (MANDATORY) ✅ 부분

| Evidence | 상태 | 출처 |
|---------|------|------|
| E-PASS-8: 4 G4 workflow actual run PASS | ✅ 3/4 | 58 entry: g4-hash-chain `26557460199` + rewrite-defense `26557460227` + history-anchor-verifier `26557460197` 전원 green. r2-canary (R-6/R-2 canary) = path 미트리거 (별도 §4.3) |
| E-PASS-9: canonical 위반 BLOCK | ✅ | corpus 회귀 Primary 1/2 byte+sha256 mismatch BLOCK + NaN/Inf reject (RFC 8785 §3.2.2.2) |
| E-PASS-10: timestamp monotonicity 위반 BLOCK | ✅ | 코드 검출 (`jsonl_hash_chain.py:224` monotonicity_violation) + **C-1 보강 (59 entry): `timestamp_monotonicity.jsonl` fixture 추가 (valid chain + ts 역행) → g4-hash-chain.yml 5 violation_type cover, actual run `26557936920` green** |
| E-PASS-11: R-6 workflow 확장 step actual run | ⚠️ W-F | W-F (기존 보존, 신규 step 0) 답습 — 별도 R-6 step 미추가. Layer 4 회귀 = 3 ledger workflow 가 충족 |

→ **Layer 4 = 충족** (3 ledger workflow green + canonical BLOCK ✅ + timestamp monotonicity ✅ C-1 보강, r2-canary 미트리거는 R-6/R-2 영역).

### §2.6 통합 evidence ((γ-c) 의무 3 — 동시 발효, Layer subsection 분리 유지)

| Evidence | 상태 |
|---------|------|
| E-PASS-12: 통합 evidence (Layer subsection 분리 명시) | ✅ 본 §2 (Layer 1/2a/2b/2/4 subsection 분리, 합산 0) |
| E-PASS-13: 합의 보고서 commit | ⏳ 본 cycle 합의 |
| E-PASS-14: 외부 LLM 1+ (cross-vendor) | ⏳ 본 cycle codex |
| E-PASS-15: R-S1 정정 자격 평가 (RT-γ-6) | §5 |

---

## §3 PASS 발효 자격 매핑 — ADR-011 §2.1 (a)~(d) 모법 + (e2) ADR-012 §4 확장 (B-2 정정)

> ⚠️ **B-2**: ADR-011 §2.1 = **(a)~(d) 4조건만** (line 52~61). "(e) 합의 APPROVE" = ADR-012 §4 "(a)~(d) + (e) 5조건 답습" 확장 패턴 (§0.3 framing). 본 §3 = (a)~(d) ADR-011 모법 + (e2) ADR-012 §4 확장 매핑.

| # | 조건 | Layer 1 | Layer 2 (2a+2b) | Layer 4 | 통합 |
|---|------|------|------|------|----|
| (a) | 동등 이상 보안 결과 | ✅ middle tampering 차단 (3 violation type) | ✅ 2b force push/delete 차단 + history 재작성 차단 (2a DEFER, 2b operative) | ✅ CI 회귀 (canonical BLOCK + timestamp monotonicity, C-1 보강) | Layer 1+2+4 통합 (subsection 분리) |
| (b) | 격리 환경 PoC 실증 | ✅ jsonl_hash_chain + fixtures | ✅ 2b actual state + history fixtures 8 | ✅ 3 G4 actual run green | 통합 (합산 0) |
| (c) | ADR/SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.3/§2.8 | ✅ 동상 | ✅ 동상 | ✅ |
| (d) | 자동 회귀 검증 경로 | ✅ g4-hash-chain CI | ✅ rewrite-defense + history-anchor CI | ✅ 3 ledger workflow CI green | ✅ |
| **(e2)** | **PASS 발효 합의 APPROVE** | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ 본 cycle | ⏳ **본 cycle 풀 3+1 + 외부 LLM + 사용자 명시** |

→ **(a)~(d) 충족 = Layer 1 완전 / Layer 2 충족 (2a DEFER 문서화, 2b operative) / Layer 4 충족 (C-1 timestamp 보강 완료, r2-canary = R-6/R-2 영역)**. (e2) = 본 cycle 합의.

---

## §4 gap / DEFER 처리

### §4.1 Layer 2a denyNonFastForwards = DEFER (B-3 + N-1 정정)

- ⭐ **B-3**: `receive.denyNonFastForwards` = push *받는* repo (bare/server) 에서만 작동. 본 repo = 비-bare 작업 clone, push 대상 = GitHub → 본 clone 활성화 = **no-op (효과 0)**. "per-repo = 영향 최소/ceremony" framing (55 §4.4.2) 부정확 → 정정 = **켤 이유 소멸** (no-op), DEFER 강화.
- ⭐ **N-1 — append-only ends 이중 cover** (단일 수단 종속 0, ADR-012 §2.3 Layer 2 = 4 means 동시): (1) Layer 2b branch protection (allow_force_pushes/deletions false + enforce_admins true, gh api verify) + (2) rewrite-defense.yml Layer 4 CI (`non_fast_forward_detected`/`history_reorder_detected` 검출, actual run green). 2a 시나리오를 2 layer 가 cover.
- **PASS 발효 영향**: Layer 2 append-only *결과(ends)* = 2b + rewrite-defense CI 이중 충족. 2a = 실 bare/server 배포 시점 (별도 trigger, no-op 이므로 본 clone 무관). PASS 발효 = ends 충족 + 2a DEFER no-op 명문.

### §4.2 E-PASS-10 timestamp monotonicity fixture (C-1) — ✅ 보강 완료 (합의 전 미리 보강, 사용자 명시)

- 코드 검출 확인 (`validate_chain:224` — `cur_ts < prev_ts` → monotonicity_violation).
- **C-1 보강 완료 (59 entry, commit `4c48099`)**: `tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl` 추가 (valid chain genesis/prev_hash/entry hash + ts 역행 → monotonicity_violation 단독) + g4-hash-chain.yml FAIL fixture step 4→5 violation_type cover (W-F 기존 workflow 內 보강) + TDD test (test_validate_chain_monotonicity_violation). **actual run `26557936920` green** → E-PASS-10 CI 입증.

### §4.3 r2-canary (E-PASS-11) 미트리거

- r2-canary = R-6/R-2 redaction canary (paths = docker/r4-1-poc, docker/r2-poc, canary docs). Layer 1+2+4 *ledger* 검증 핵심 아님 (3 ledger workflow 가 Layer 4 충족).
- **권고**: r2-canary 는 GP-2 영역 (R-3) 또는 workflow_dispatch 로 별도 actual run. 본 Layer 통합 PASS 영향 = 3 ledger workflow 로 충족.

---

## §5 R-S1 hard gate (RT-γ-6) PASS 시점 선행/동시 정정 *자격* 평가

- R-S1 = ADR-012 *자체 내부* §2.3 (4-layer numbering) vs §2.8 / G4 §4.4.1 (5-layer numbering) divergence (52/53 entry 5 source verify CONFIRMED).
- **RT-γ-6 평가** (54 §1.3 의무 4): MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 선행/동시 *자격* 평가 의무. **단 본 cycle = Layer 통합 PASS 발효 (MVP-2 PASS 아님)**. R-S1 정정 = MVP-2 PASS 전 hard gate (3 옵션: ADR-012 §2.3 정정 / §2.8 강화 / 권위 선언) — **별도 cycle**.
- **본 cycle 영향**: Layer 통합 PASS 는 G4 §4.4.1 numbering (PRIMARY, 5-layer) 답습 — R-S1 정정 *전*에도 G4 §4.4.1 권위로 Layer 1+2+4 정의 명확 (52 brief v1.1 답습). **Layer 통합 PASS 발효 = R-S1 정정 미종속** (MVP-2 PASS 가 종속, B-8 답습 "평가 의무" framing).

→ **R-S1 = Layer 통합 PASS 발효 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle). 본 cycle = 평가 한정 (N-4: ADR-011 §2.3 #4 line 113 "의존성 변경 → R-2/R-6 재실행" cross-ref — rfc8785/jcs = Q1 합의 채택이므로 본 cycle trigger 발화 0).

---

## §6 합의 형태 + 풀 3+1 승격 트리거

### §6.1 합의 형태 = 풀 3+1 + 외부 LLM 1+ (의무)

**정당화**: PASS *발효* milestone (32 entry MVP-1 PASS 발효 답습 동형) + 55 §8 #3 "Layer 통합 PASS 발효 합의 = 풀 3+1 + 외부 LLM 1+" + 큰 결정 (ADR-011 §2.4 T3) + 헌법 5조-2 cross-vendor.

### §6.2 7 풀 3+1 승격 트리거

| # | trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 큰 결정 (PASS 발효 milestone) | ✅ | Layer 1+2+4 통합 PASS 발효 = MVP-2 PASS 직전 |
| 2 | 아키텍처/SDD/보안 본문 변경 | ❌ | brief = phase0 신규 1, 본문 0 |
| 3 | ADR 본문 변경 | ❌ | 0 |
| 4 | 권위 chain 다중 source 손상 | ⚠️ 부분 | R-S1 (RT-γ-6 평가 한정) |
| 5 | 외부 LLM 통합 필요 | ✅ | cross-vendor 의무 |
| 6 | Tier-2/3 catalog 확장 | ❌ | 0 |
| 7 | Hermes PMO 격상 | ❌ | 0 |

→ **2/7 발화 + 1 부분 → 풀 3+1 + 외부 LLM 1+ 적격**.

---

## §7 PASS 발효 권고 + 조건

⭐ **권고 = Layer 1+2+4 통합 PASS 발효 APPROVE WITH CONDITIONS**:

1. **Layer 1 + Layer 2 + Layer 4 (3 ledger workflow) = (a)~(d) 충족** — actual run green (58 entry 3 G4 run + 59 C-1 g4-hash-chain `26557936920`) + Layer subsection 분리 evidence.
2. **조건 처리 상태**:
   - (C-1) E-PASS-10 timestamp monotonicity FAIL fixture = ✅ **보강 완료** (`4c48099`, actual run `26557936920` green, 합의 전 미리 보강 사용자 명시)
   - (C-2) Layer 2a denyNonFastForwards DEFER 명문 (2b operative 충족 근거) — 비례 보안 답습 (잔여 문서화 조건)
   - (C-3) r2-canary = R-6/R-2 영역 명시 (Layer 통합 PASS 비차단), workflow_dispatch 별도
3. **R-S1 = Layer 통합 PASS 비차단** (MVP-2 PASS 전 hard gate, 별도 cycle, §5).
4. **"부분 답습" framing 영구** (Layer 3+5 scope 외).

→ **PASS 발효 자격 = (a)~(d) 충족 (C-1 완료) + (e2) 합의 APPROVE + 사용자 명시 + (C-2) 2a DEFER 명문**.

---

## §8 금지 사항

§0.2 답습 (14). 추가: MVP-2 PASS 자동 선언 0 / GP-2 PASS 합산 0 / denyNonFastForwards 자동 활성화 0 / R-S1 자동 정정 0 / Layer 3+5 진입 0 / 자동 후속 cycle 0.

---

## §9 다음 단계 (사용자 명시 의무 — 자동 진입 0)

1. 본 brief 승인 → 풀 3+1 + 외부 LLM 1+ (codex (E-α)) → Reviewer 통합 → brief v1.1 흡수 → commit + push → **Layer 1+2+4 통합 PASS 발효**
2. (C-1) timestamp fixture 보강 (PASS 발효 조건 또는 후속 자율)
3. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS + GP-2 PASS + R-S1 hard gate 후 별도, 32 entry 답습)
4. R-S1 cross-reference 정정 cycle (MVP-2 PASS 전 hard gate 3 옵션)
5. GP-2 PASS 영역 (R-3 secret-hygiene actual run + R-1/R-2 trajectory)

---

## §10 cross-reference 답습

- ADR-011 §2.1 (a)~(e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- ADR-012 §2.3/§2.5/§2.7/§2.8/§3.4 — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- provider-agnostic-memory-skill-design.md §4.4 (Layer 1~5)
- 55 통합 PASS 격상 진입 brief v1.1 — `docs/phase0/mvp2-layer-124-pass-entry-brief.md`
- 57 (β) 결정 brief v1.1 + 합의 — `docs/phase0/mvp2-beta-submeans-decision-brief.md` + `docs/review/3plus1-consensus-2026-05-28-mvp2-beta.md`
- 58 실 구현 — `tools/jsonl_hash_chain.py` + `tests/tools/test_jsonl_hash_chain.py` + 3 G4 actual run
- 32 MVP-1 PASS 발효 합의 — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- 실 evidence: `g4-hash-chain.yml` + `rewrite-defense.yml` + `history-anchor-verifier.yml` + branch protection 8 contexts + `tests/fixtures/{jsonl_ledger,history_anchor_verifier,rewrite_defense}` + `tests/canonical/` 72

---

## §11 자기진단 (메타 편향 회피)

| # | 위험 | 처리 |
|---|------|----|
| P-1 | 본 brief 가 PASS 발효를 *기정사실화* | 발효 = 합의 APPROVE + 사용자 명시 후 (§0.2 #1 + §9) |
| P-2 | evidence gap (timestamp fixture / 2a DEFER) 은폐 | §2.5 + §4 명시 (honest matrix, 57 (β) B-1 cascade 교훈 — 시제 주장 over-claim 방지) |
| P-3 | 2a DEFER 가 Layer 2 충족 *과대* | §2.2 + §4.1 = 2b operative 충족 근거 명시, 2a = 컨테이너 배포 trigger 시점 |
| P-4 | 본 brief 작성자 = 55/57/58 작성자 (Claude) cascade risk | cross-vendor (E-α) codex + 풀 3+1 독립 검증 (57 (β) 동형 — codex/Agent 가 B-1 포착한 process 가치) |
| P-5 | timestamp fixture gap 을 BLOCKING vs 자율 보강 판단 | §7 (C-1) 조건 명시, 풀 3+1 판정 위임 |
| P-6 | R-S1 RT-γ-6 = Layer 통합 PASS 차단 오해 | §5 = MVP-2 PASS 전 hard gate (Layer 통합 PASS 비차단), B-8 "평가 의무" 답습 |

---

---

## §12 v1.1 흡수 매트릭스 (BLOCKING 3 + 권고 4 1pass)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-layer-124-pass-activation.md` 답습 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단, 52/55/57 동형). **4 source 전원 APPROVE WITH CONDITIONS — evidence 실증 (over-claim 0)**.

| # | 흡수 | source | 정정 |
|---|------|--------|------|
| B-1 | citation `6ebc634`→`052e583` (실 구현) | Agent A R-A-1 | §0.3 + §1.1 |
| B-2 | ADR-011 §2.1 = (a)~(d), (e2) = ADR-012 §4 확장 (권위 전도) | Agent B R-B-1 | §3 header + §10 |
| B-3 | 2a denyNonFastForwards = non-bare clone no-op (DEFER 강화) | Agent C R-C-1 | §2.2 + §4.1 |
| N-1 | 2a DEFER append-only ends 이중 cover (2b + rewrite-defense CI) | Agent B + C + codex | §2.2 + §4.1 |
| N-2 | "4 G4" → 3 ledger workflow (r2-canary = R-6/R-2) | codex + Agent A | §2.5 |
| N-3 | history-anchor-verifier "Layer 5" 이름 — "부분 답습" framing | codex + Agent C | §2.4 |
| N-4 | enforce_admins evidence + ADR-011 §2.3 #4 cross-ref | Agent B | §2.3 + §5 |

**4 source 정합 확인**: evidence 전원 실증 (actual run 4개 success direct + fixture + contexts + pytest 152) / (γ-c) 특화 의무 4 정합 / scope 침입 0 / 발효 형태 32 entry 일관 (Agent C 4 대안 기각).

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push → 본 cycle 합의 발효 (APPROVE WITH CONDITIONS 4 source) → **Layer 1+2+4 통합 PASS 발효 (e2)**. 후속: MVP-2 Implementation Evidence PASS 발효 합의 (Layer 통합 PASS + GP-2 PASS + R-S1 hard gate) = 사용자 명시 별도 cycle.
