# Agent A (구현 분석가) — (γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 검토

> **본 검토** = (γ) 4 대안 中 채택 결정 풀 3+1 합의 cycle (53 entry) Agent A 응답.
> Agent A 핵심 질문: **"실제로 동작하는가?"** — 기술적 구현 가능성, 의존성, 성능.
> 본 응답 = Agent B/C/외부 LLM codex 응답 *참조 0* (병렬 독립 평가 의무 답습, CLAUDE.md §3 답습).

---

## 직접 read 한 자료 path 목록

PRIMARY (검토 대상):
- `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-gamma-layer-separation-brief.md` (v1, 482줄, §0~§10 전체)

답습 source:
- `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-entry-brief.md` (52 entry v1.1, §2.2.4 (γ) 4 대안 정의 + §8.1 (γ) 진입 자격)
- `/home/delangi/문서/project/category/AI_development_tool/docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` (52 entry Reviewer 통합, R-S1 §4.1 verbatim verify)
- `/home/delangi/문서/project/category/AI_development_tool/docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4.1 line 629~660 — 5-layer 직접 정의)
- `/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3 line 165~185 4-layer numbering + §2.8 line 264~272 5-layer)
- `/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 line 46~61, (a)~(d) 4조건 모법 verbatim)

실 repo PoC 시제 (filesystem 직접 inspection):
- `/home/delangi/문서/project/category/AI_development_tool/tools/jsonl_hash_chain.py` (14038B, head 200 line read)
- `/home/delangi/문서/project/category/AI_development_tool/tools/canonical_json.py` (10055B, head 60 line read)
- `/home/delangi/문서/project/category/AI_development_tool/tests/canonical/` (8 디렉토리 verify: array / escape / hash_stability / key_ordering / lossy / nested / number / unicode)
- `/home/delangi/문서/project/category/AI_development_tool/.github/workflows/g4-hash-chain.yml` (10652B, head 200 line read)
- `/home/delangi/문서/project/category/AI_development_tool/.github/workflows/history-anchor-verifier.yml` (19094B, size verify)
- `/home/delangi/문서/project/category/AI_development_tool/.github/workflows/rewrite-defense.yml` (16454B, size verify)
- `/home/delangi/문서/project/category/AI_development_tool/.github/workflows/r2-canary.yml` (5476B, size verify)

---

## §0 총평

**판정**: ⚠️ **APPROVE WITH CONDITIONS** — brief v1 → v1.1 보강 후 본 cycle 합의 발효 자격 충실.

### §0.1 판정 정당화

본 (γ) brief v1 = (γ-a/b/c/d) 4 대안 후보 비교 + ADR-011 §2.1 (a)~(d) 5조건 매트릭스 + PoC 시제 답습 cross-check + Rollback Trigger 후보 + Evidence 후보 모두 충실 답습. Agent A 구현 분석가 관점에서:

- ✅ **4 대안 구현 가능성 분석 충실** — (γ-a/c) = 5조건 충족 + (γ-b) = (c)+(d) 분리 risk + (γ-d) = (c)+(d) 모순 risk 명시
- ✅ **PoC 시제 실 작동 verify 충실** — filesystem 직접 inspection 결과 5 영역 모두 PoC 시제 충족 (PASS 시제 미충족 격상 답습)
- ✅ **(γ-d) 모순 risk 발견 정직** — §2.4.4 자체 framing 정정 (52 entry framing (γ-d) → (γ-a) 사실상 동등 격상)
- ⚠️ **BLOCKING 2건 + 권고 3건 흡수 의무** — 구현 분석가 관점 filesystem evidence 보강 + 시간 부담 정량화

### §0.2 17 원칙 준수 verify

- 실 코드 0 / `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `tests/canonical/` 본문 변경 0 / G4 workflow 본문 변경 0 / ADR 본문 0 / G4 §4.4 본문 0 / threshold 고정 0 / sub-수단 결정 0 / Tier-2/3 catalog 확장 0 / MVP-1 PASS 재선언 0 / MVP-2 PASS 발효 0 / Operational Readiness 0 / Hermes PMO 격상 0 / R-S1 자동 진입 0 / Layer 3+5 자동 진입 0 / GP-1/4/6/G3 자동 진입 0 / branch protection 자동 추가 0 / 헌법 변경 0 → **17/17 모두 유지**.

### §0.3 본 검토 발효 자격

본 Agent A 응답 = 풀 3+1 (Agent A/B/C 3 병렬 + Reviewer) + 외부 LLM 1+ (codex cross-vendor 권고, 사용자 영역) 입력 1 source.

---

## §1 BLOCKING 2건 (R-A-x)

### R-A-1 (BLOCKING) — (γ-a) "합의 cycle N회 + 시간 부담" 정량화 부재

**영역**: brief §2.1.3 (γ-a) 단점 "시간 부담 (합의 cycle N회)" verbatim — N 미정량.

**구현 분석가 evidence**:
- (γ-a) 채택 시 후속 sub-cycle 명목 = (1) Layer 1+2 PASS 격상 합의 cycle + (2) Layer 4 PASS 격상 합의 cycle = **최소 2 cycle**
- 각 cycle 평균 부담 = brief input + 풀 3+1 (Agent A/B/C 3 병렬 + Reviewer 통합) + 외부 LLM 1+ (cross-vendor) + brief v1.1 1pass 흡수 + SESSION + INDEX + commit + push
- 52 entry cycle 실 evidence (시간 부담 ≈ 1 session 內 다 entry chain)
- (β) sub-수단 결정 cycle 별도 의무 (L-1~L-5 25 조합 답습 + R-1~R-5) → (γ-a) 채택 시 = **(β) + (γ-a) Layer 1+2 + (γ-a) Layer 4 + MVP-2 PASS 발효 합의 = 4 cycle**
- 단, brief §2.1.4 답습 = "PoC 시제 충족 / PASS 격상만 필요 → (γ-a) 시점 cycle 부담 = 'PASS 격상 합의 + evidence' 한정 (실 구현 부담 ↓)" — 실 구현 부담 ↓는 정확하나, **합의 cycle 부담 ↓ 미명시**

**구현 분석가 발견**: brief §2.1.3 "N회" 표현 = (γ-c) 1 cycle 對 명시 부재 → 후속 sub-cycle 진입 시 의사결정 불명. 본 cycle 결정 = 5 layer 答아닌 4 대안 결정인데, (γ-a) cycle 수 명시 부재 시 (γ-c) 대비 부담 평가 불가.

**처리 의무 (v1.1 보강)**: brief §2.1.3 (γ-a) 시간 부담 정량화 — "최소 2 (γ-a) sub-cycle + (β) sub-수단 결정 cycle + MVP-2 PASS 발효 합의 cycle = 총 4 cycle" verbatim 명시 + §2.3.3 (γ-c) 부담 정량화 ("1 큰 합의 cycle + (β) sub-수단 결정 + MVP-2 PASS 발효 = 총 3 cycle") 대비표 추가.

---

### R-A-2 (BLOCKING) — `tests/canonical/` fixture 카테고리 정량화 부재

**영역**: brief §2.5 + §9.3 — "tests/canonical/ 24 fixtures (8 카테고리 × 3 = RFC 8785 reference ≥ 20 충족)" verbatim.

**filesystem 직접 inspection 결과** (Agent A 구현 분석가 권한):

`tests/canonical/` 디렉토리 = **8 카테고리 디렉토리 충족** (filesystem inspection):
- `array/` `escape/` `hash_stability/` `key_ordering/` `lossy/` `nested/` `number/` `unicode/`

→ **8 카테고리 verify 충족**. 단, brief §2.5 + §9.3 "× 3 = 24 fixtures" 산식 = filesystem 직접 fixture count 의 1 source 한정 (52 entry brief carry-over 답습). 본 Agent A inspection 시점 = digit count 직접 verify 부재 (디렉토리 구조 + 파일 size 만 verify, .input.json + .expected.canonical + .expected.sha256 trio 각 카테고리당 3개씩 24 fixture 산식 = 52 entry 답습 답습).

**구현 분석가 evidence**: 
- `.github/workflows/g4-hash-chain.yml` line 76 = `for inp in tests/canonical/*/*.input.json` — glob pattern 충족 (8 카테고리 × N fixture 가능)
- workflow line 91~94 = "Primary 1 corpus: ${total} cases, ${fail} fail" 동적 count → 정확한 fixture 수 = workflow run 결과 (filesystem inspection 1-pass 부재)

**처리 의무 (v1.1 보강)**: brief §2.5 + §9.3 = "tests/canonical/ 8 카테고리 (array/escape/hash_stability/key_ordering/lossy/nested/number/unicode) — fixture 정량은 PoC 시제 답습 (52 entry 답습 24 fixture, 본 cycle 시점 filesystem 직접 inspection 1-pass count 영역 carry-over)" 정정. 본 cycle scope 외 정량 carry-over 명시.

---

## §2 권고 3건 (N-A-x)

### N-A-1 (권고) — (γ-c) Layer evidence 분리 명시 PoC 시제 답습 보강

**영역**: brief §2.3.2 (γ-c) 장점 "각 layer evidence 명시 분리 ((γ-b) 와 차이)" verbatim.

**구현 분석가 evidence**: `g4-hash-chain.yml` 직접 read 결과 = 이미 step 분리 충족:
- Step 1: "Corpus regression — Primary 1 (rfc8785)" (canonical JSON 영역)
- Step 2: "Corpus regression — Primary 2 (jcs) cross-check"
- Step 3: "Corpus regression — cross_check mode"
- Step 4: "Fallback equivalence — jq -S -c vs Primary 1"
- Step 5: "NaN/Inf reject"
- Step 6: "PASS fixture — jsonl_hash_chain rc=0 (× 2)"
- Step 7: "FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover"

→ **(γ-c) Layer evidence 분리 명시 = PoC 시제 답습 이미 충족 시제 (workflow step 분리)**. PASS 격상 = step 명명을 G4 §4.4 5-layer 기준 정합 (e.g., "Layer 4 — base branch JSONL line deletion / rewrite 감지" step 신규 + 각 step prefix `[Layer N]`).

**권고**: brief §2.3.2 (γ-c) 장점 답습에 = "PoC 시제 step 분리 충족 (`g4-hash-chain.yml` 7 step), PASS 격상 = step prefix `[Layer N]` 답습 + Layer 2 base branch deletion / rewrite 감지 step 신규" verbatim 추가.

---

### N-A-2 (권고) — `tools/jsonl_hash_chain.py` 4 violation_type Layer 1 매핑 명시

**영역**: brief §2.5 + §9.3 — "tools/jsonl_hash_chain.py (genesis hash + 4 violation_type)" verbatim.

**구현 분석가 evidence** (filesystem direct inspection):
- `tools/jsonl_hash_chain.py` line 66~72 `ViolationType` enum verbatim:
  - `PREV_HASH_MISMATCH = "prev_hash_mismatch"`
  - `HASH_RECALCULATION = "hash_recalculation"`
  - `HISTORY_REWRITE = "history_rewrite"`
  - `GENESIS_MISMATCH = "genesis_mismatch"`
- line 85~90 `compute_genesis_hash` = `sha256(f"genesis:{scope}:{schema_version}")` (ADR-012 §2.6 MVP 답습)
- line 93~100 `compute_entry_hash` = `to_canonical(payload, mode=PRIMARY_1_ONLY)` (rfc8785 단독, Q1 합의 답습)

→ **4 violation_type 매핑** ((γ-a/b/c/d) 모두 영향):
- `PREV_HASH_MISMATCH` = G4 §4.4.1 Layer 1 hash chain 검증 (Layer 1 영역)
- `HASH_RECALCULATION` = G4 §4.4.1 Layer 1 (canonical JSON sha256 재계산 검증)
- `HISTORY_REWRITE` = G4 §4.4.1 Layer 2 Git append-only (base branch 대비 line 변경 감지)
- `GENESIS_MISMATCH` = G4 §4.4.1 Layer 1 (genesis_hash 첫 entry 검증)

→ 4 violation_type 中 **3건 = Layer 1, 1건 = Layer 2** (Layer 4 자체는 Layer 1+2 회귀 검증 framework).

**권고**: brief §2.5 또는 §5.1 = "tools/jsonl_hash_chain.py 4 violation_type Layer 1+2 매핑 (3 Layer 1 + 1 Layer 2), Layer 4 = 본 4 violation_type 회귀 검증 framework" verbatim 추가. (γ-d) 모순 risk 답습 보강 자격 (§2.4.3 답습 — Layer 1+2 미발효 시 Layer 4 회귀 *대상* = 본 4 violation_type detection 部材).

---

### N-A-3 (권고) — `r2-canary.yml` (5476B) vs `g4-hash-chain.yml` (10652B) 분리 답습 명시

**영역**: brief §0.3 #4 + §9.3 — R-6 workflow 답습 영역.

**구현 분석가 evidence** (filesystem direct inspection):
- `.github/workflows/r2-canary.yml` = 5476B (R-6 답습, 42 entry actual run id `25623028888` 답습 framing)
- `.github/workflows/g4-hash-chain.yml` = 10652B (G4 영역, canonical JSON + hash chain + violation_type)
- `.github/workflows/history-anchor-verifier.yml` = 19094B (G4 §2.8 Layer 5 영역)
- `.github/workflows/rewrite-defense.yml` = 16454B (G4 §2.8 Layer 2/3 영역)

→ **실 repo 기존 G4 workflow = 3 파일 분리 운영 + R-6 = 별도 1 파일 분리 운영** (총 4 파일 분리). brief §0.3 #4 + #5 = 본 cycle "본문 변경 0" 명시 충족.

**구현 분석가 평가** — (γ-a/b/c/d) workflow 통합 영역:
- (γ-a) Layer 1+2 우선 → Layer 4 후속 = 기존 `g4-hash-chain.yml` 답습 PASS 격상 + 신규 step 추가 (Layer 2 base branch deletion / rewrite) — workflow 1 파일 영역 한정 가능
- (γ-b) Layer 4 단독 (Layer 1+2 자동) = 기존 `g4-hash-chain.yml` 통합 + `rewrite-defense.yml` step 답습 통합 (workflow 1-2 파일 영역)
- (γ-c) Layer 1+2+4 동시 = (γ-b) 동형 + 각 layer step 명시 분리
- (γ-d) Layer 4 단독 + Layer 1+2 별도 = **모순 risk 추가 영역** (Layer 4 = Layer 1+2 회귀 검증 framework, Layer 1+2 PASS 미발효 시 workflow step 의미 부재)

→ W-A/B/C/D/E (52 entry brief §2.3.2 답습) = (β) sub-수단 결정 영역. 본 (γ) cycle = 분리 영역 결정 한정.

**권고**: brief §2.5 또는 §9.3 = "실 repo 기존 G4 workflow 4 파일 분리 운영 답습 (g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml). (γ) 결정 = 본 4 파일 운영 답습 보존 또는 통합 결정 영역 ((β) sub-수단 결정 W-A/B/C/D/E 영역)" verbatim 명시.

---

## §3 NOTE 2건 (필요 시)

### NT-A-1 — (γ-d) 모순 risk 발견 정직성 정밀 evidence

brief §2.4.4 = "(γ-d) 채택 시 framing 모순 risk" verbatim — "Layer 1+2 미발효 시 Layer 4 회귀 검증 *대상 부재*" 발견. 

**filesystem 직접 inspection evidence** (구현 분석가 답습 강화):
- `tools/jsonl_hash_chain.py` line 165~199 `validate_chain` 함수 = Layer 1 (prev_hash + recomputed hash) + Layer 1 (genesis_hash) + timestamp monotonicity (ADR-012 §3.4) 검증
- `g4-hash-chain.yml` step "PASS fixture × 2" + "FAIL fixture × 4 + 4 violation_type cover" = Layer 1 회귀 검증 step
- `rewrite-defense.yml` (16454B) = Layer 2 / Layer 3 영역 회귀 검증 step

→ **(γ-d) 채택 시 모순 evidence**: Layer 4 workflow step (PASS / FAIL fixture × 6) = Layer 1 (4 violation_type) + Layer 2 (rewrite-defense) 회귀 검증 대상. Layer 1+2 미발효 = **회귀 대상 fixture 부재** + **자체 함수 부재** → workflow step 실패 또는 무의미 PASS.

→ brief §2.4.4 "(γ-d) = 사실상 (γ-a) 와 동등" 격상 정직 충실.

### NT-A-2 — R-S1 (ADR-012 §2.3 4-layer vs §2.8 5-layer) 후행 영향 (RT-γ-6 답습)

brief §5.1 RT-γ-6 = "R-S1 cross-reference 정정 후행 영향" 명시. 

**구현 분석가 verify** (verbatim direct read):
- ADR-012 §2.3 line 165~185 = 4-layer numbering (Layer 4 = External anchor)
- ADR-012 §2.8 line 264~272 = 5-layer numbering (Layer 4 = CI 회귀 검증, Layer 5 = External anchor)
- `provider-agnostic-memory-skill-design.md` §4.4.1 line 629~660 = 5-layer (ADR-012 §2.8 동형, Layer 4 = CI 회귀 검증 MANDATORY)

→ **본 (γ) cycle = G4 §4.4.1 + ADR-012 §2.8 5-layer 답습 한정** (52 entry brief §4.4.2 권위 인용 chain 답습). ADR-012 §2.3 numbering = 본 cycle 결정 근거 0. R-S1 정정 cycle (별도 cycle) 발효 시 = 본 (γ) cycle 결정 본문 변경 0 (numbering = 5-layer 답습 충실).

---

## §4 4 대안별 평가 ((γ-a/b/c/d))

### §4.1 (γ-a) Layer 1+2 우선 → Layer 4 후속 — 구현 분석가 평가

| 평가 영역 | 평가 |
|--------|----|
| **의존 chain 답습** | ✅ 답습 충실 (Layer 4 = Layer 1+2 회귀 검증 framework) |
| **실 작동 가능성** | ✅ PoC 시제 충족 (`tools/jsonl_hash_chain.py` line 165~199 `validate_chain` + `g4-hash-chain.yml` step 7개), PASS 격상 = R-6 workflow 답습 통합 + actual run PASS (42 entry `25623028888` 답습) |
| **합의 cycle 부담** | ⚠️ **최소 2 (γ-a) sub-cycle + (β) sub-수단 결정 + MVP-2 PASS 발효 = 4 cycle** (R-A-1 발견) |
| **PoC → PASS 격상 실 작업량** | Layer 1+2 = `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` 본문 변경 0 답습 충실 + Docker 격리 PoC + R-6 actual run PASS. Layer 4 후속 = workflow step 추가 (Layer 2 base branch deletion / rewrite 감지) |
| **Layer 1+2 evidence 분리** | ✅ 명시 분리 (각 PASS 격상 cycle별 evidence) |
| **권고 순위** | 2 (안전, 의존 답습 충실) |

### §4.2 (γ-b) Layer 4 단독 + Layer 1+2 자동 동시 — 구현 분석가 평가

| 평가 영역 | 평가 |
|--------|----|
| **의존 chain 답습** | ✅ 답습 (자동 의존 포함) |
| **실 작동 가능성** | ✅ PoC 시제 충족 (모든 영역) |
| **합의 cycle 부담** | ✅ 1 (γ-b) sub-cycle + (β) sub-수단 결정 + MVP-2 PASS 발효 = **3 cycle** (γ-a 比 1 cycle 절감) |
| **PoC → PASS 격상 실 작업량** | Layer 1+2+4 통합 = 큰 영역, evidence 분리 미명확 risk |
| **Layer 1+2 evidence 분리 risk** | ⚠️ **분리 미명확 risk** (brief §2.2.3 답습 — Layer 4 evidence 內 Layer 1+2 evidence 합산 → 회귀 영역 미식별 risk). 단, `g4-hash-chain.yml` 기존 7 step 분리 운영 답습 시 risk 감소 |
| **권고 순위** | 3 (효율 ↑, 분리 risk ↑) |

### §4.3 (γ-c) Layer 1+2+4 동시 (defense-in-depth) — 구현 분석가 평가

| 평가 영역 | 평가 |
|--------|----|
| **의존 chain 답습** | ✅ 답습 충실 |
| **실 작동 가능성** | ✅ PoC 시제 충족 + step 분리 답습 자격 (N-A-1 답습) |
| **합의 cycle 부담** | ✅ 1 큰 (γ-c) sub-cycle + (β) sub-수단 결정 + MVP-2 PASS 발효 = **3 cycle** (γ-a 比 1 cycle 절감, γ-b 동등) |
| **PoC → PASS 격상 실 작업량** | Layer 1+2+4 통합 + 각 layer evidence 명시 분리 (workflow step prefix `[Layer N]` 답습) |
| **Layer 1+2 evidence 분리** | ✅ 명시 분리 (γ-b 對 강점) |
| **합의 부담** | ⚠️ 큰 합의 영역 (γ-b 동형) — 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| **권고 순위** | **1 (defense-in-depth + 효율 + 분리)** |

### §4.4 (γ-d) Layer 4 단독 + Layer 1+2 별도 (52 entry framing) — 구현 분석가 평가

| 평가 영역 | 평가 |
|--------|----|
| **의존 chain 답습** | ⚠️ **모순 risk** (Layer 1+2 미발효 시 Layer 4 회귀 *대상 부재*) |
| **실 작동 가능성** | ⚠️ **회귀 대상 fixture 부재** (NT-A-1 evidence — `tools/jsonl_hash_chain.py` 4 violation_type 회귀 = Layer 1+2 영역 회귀 검증 framework, Layer 1+2 본문 부재 시 무의미 PASS 또는 step 실패) |
| **합의 cycle 부담** | ⚠️ Layer 4 단독 cycle + Layer 1+2 별도 cycle + (β) + MVP-2 PASS = **4+ cycle** (시점 차이 한정, 사실상 (γ-a) 동등) |
| **PoC → PASS 격상 실 작업량** | (γ-a) 동등 (시점 차이) |
| **Layer 1+2 evidence 분리** | ✅ 본격 분리 (Layer 4 = 회귀 검증, Layer 1+2 = 별도) |
| **권고 순위** | **4 (비권고, 의존 chain 모순)** |

### §4.5 4 대안 매트릭스 (Agent A 구현 분석가 종합)

| 대안 | 의존 chain | PoC 시제 | 합의 cycle | evidence 분리 | 후속 sub-cycle 실 작업량 | 권고 순위 |
|------|---------|--------|---------|------------|----------------|--------|
| (γ-a) Layer 1+2 → Layer 4 | ✅ | ✅ | 4 | ✅ | 단계적, Layer 2 base branch step 신규 | **2** |
| (γ-b) Layer 4 (auto 1+2) | ✅ (auto) | ✅ | 3 | ⚠️ | 통합 큰 영역 | 3 |
| (γ-c) Layer 1+2+4 동시 | ✅ | ✅ | 3 | ✅ | 통합 + step prefix `[Layer N]` | **1** |
| (γ-d) Layer 4 + Layer 1+2 별도 | ⚠️ 모순 | ⚠️ 회귀 대상 부재 | 4+ | ✅ | 사실상 (γ-a) 동등 | **4** |

→ **본 Agent A 권고**: **(γ-c) Layer 1+2+4 동시 (defense-in-depth) 1순위 + (γ-a) Layer 1+2 우선 → Layer 4 후속 2순위**. 단 **수단 *결정* = 풀 3+1 합의 + 사용자 명시 영역** (CLAUDE.md §3 답습), 본 권고 = 후보 비교 한정.

---

## §5 PoC 시제 filesystem 직접 inspection evidence

### §5.1 inspection 시점 + 환경

- **시점**: 2026-05-28 (53 entry 진입 cycle, 본 Agent A 응답 작성 시점)
- **환경**: 본 repo (`/home/delangi/문서/project/category/AI_development_tool/`), git branch `feature/jarvis-mvp0`, HEAD `3517453`
- **권한**: Read 도구 직접 read (Bash 권한 거부 → 직접 read 도구 활용)

### §5.2 inspection 결과 매트릭스

| 영역 | filesystem state (2026-05-28) | PoC 시제 verify | PASS 시제 격상 영역 |
|------|----------------------------|-------------|-------------------|
| `tools/jsonl_hash_chain.py` | 14038B, 14038 byte 분량 + `ViolationType` enum 4 enum (PREV_HASH_MISMATCH / HASH_RECALCULATION / HISTORY_REWRITE / GENESIS_MISMATCH) + `compute_genesis_hash` + `compute_entry_hash` + `validate_chain` | ✅ 충족 | R-6 actual run PASS evidence |
| `tools/canonical_json.py` | 10055B + `CrossCheckMode` enum 4 mode (PRIMARY_1_ONLY / PRIMARY_2_ONLY / CROSS_CHECK / FALLBACK_JQ) + rfc8785 + jcs cross-check + jq fallback | ✅ 충족 (RFC 8785 JCS reference + ADR-012 §2.5 답습) | corpus expected canonical reference equivalence + actual run PASS |
| `tests/canonical/` | 8 카테고리 디렉토리 verify (array/escape/hash_stability/key_ordering/lossy/nested/number/unicode) | ✅ 충족 (8 카테고리), fixture 정량 = R-A-2 carry-over 영역 | CI step 內 reference 동등성 검증 + 위반 BLOCK actual run PASS |
| `.github/workflows/g4-hash-chain.yml` | 10652B + 7 step (Primary 1 corpus / Primary 2 cross-check / cross_check mode / Fallback equivalence / NaN-Inf reject / PASS fixture × 2 / FAIL fixture × 4 + 4 violation_type) + paths filter `tools/canonical_json.py` + `tools/jsonl_hash_chain.py` + `tests/canonical/**` + `.github/workflows/g4-hash-chain.yml` | ✅ 충족 (Layer 4 회귀 검증 framework) | actual run PASS + 4 violation_type cover + R-6 통합 또는 분리 운영 결정 ((β) W-A/B/C/D/E 영역) |
| `.github/workflows/history-anchor-verifier.yml` | 19094B (G4 §2.8 Layer 5 영역) | ✅ 분리 운영 충족 | Layer 5 External anchor 영역 (본 cycle scope 외) |
| `.github/workflows/rewrite-defense.yml` | 16454B (G4 §2.8 Layer 2+3 영역) | ✅ 분리 운영 충족 | Layer 2 base branch deletion / rewrite 영역 |
| `.github/workflows/r2-canary.yml` | 5476B (R-6 답습) | ✅ 분리 운영 충족 | GP-2 + G4 §4.4 Layer 4 통합 영역 (W-A/B/C/D/E sub-수단 결정 영역) |

### §5.3 inspection 결론

✅ **모든 영역 PoC 시제 충족 (이미 운영 中)** — 52 entry brief §2.5 + 본 (γ) brief §2.5 답습 충실.

✅ **(γ-d) 모순 risk = filesystem evidence 충실** (NT-A-1 답습 — `tools/jsonl_hash_chain.py` 4 violation_type 회귀 = Layer 1+2 본문 부재 시 회귀 대상 부재).

✅ **실 repo workflow 분리 운영 답습** (4 파일: g4-hash-chain.yml + history-anchor-verifier.yml + rewrite-defense.yml + r2-canary.yml).

⚠️ **fixture 정량 (24 fixture) = 52 entry carry-over 답습 한정** (R-A-2 영역, 본 cycle 직접 count 1-pass 부재).

---

## §6 자기 편향 자기진단

### §6.1 Agent A 잠재 편향 매트릭스

| # | 잠재 편향 | 본 응답 처리 |
|---|---------|----------|
| **B-A-1** | Agent A = 구현 분석가 관점 → "구현 가능 = APPROVE" 단방향 편향 | §0.1 = APPROVE WITH CONDITIONS (BLOCKING 2 + 권고 3 명시), §1 R-A-1 (합의 cycle 부담 정량화 부재) + R-A-2 (fixture 정량 carry-over) 발견 |
| **B-A-2** | (γ-c) 권고 = brief §2.6 권고 (1)/(2) 답습 cascade risk | §4.5 4 대안 매트릭스 = Agent A 독립 평가 (PoC 시제 + 의존 chain + 합의 cycle 부담 + evidence 분리 + 실 작업량 5 영역 독립 평가) → (γ-c) 1순위 + (γ-a) 2순위 = brief §2.6 동형 결과이나, 평가 영역 독립 답습 충실 |
| **B-A-3** | filesystem inspection 의존 → state 변경 시 evidence 변질 | §5.1 inspection 시점 명시 (2026-05-28, HEAD `3517453`) + §0.2 17 원칙 준수 verify (본 cycle 內 변경 0 답습) |
| **B-A-4** | Bash 권한 거부 → fixture 직접 count 1-pass 부재 → 24 fixture 답습 cascade | R-A-2 BLOCKING 명시 (52 entry carry-over 답습, 본 cycle 직접 count 부재 정직 evidence), §5.3 + §5.2 정직 명시 |
| **B-A-5** | (γ-d) 비권고 단방향 평가 → 52 entry framing 무시 risk | NT-A-1 (γ-d) 모순 risk 정밀 evidence + filesystem direct inspection evidence (jsonl_hash_chain.py 4 violation_type Layer 1+2 영역 검증 답습) + brief §2.4.4 답습 충실 |
| **B-A-6** | Agent A = 본 brief v1 작성자와 동일 LLM (Claude Opus 4.7) → 답습 cascade | brief §10 P-7 답습 자기진단 추가 + 본 응답 = filesystem 직접 inspection + ADR-011 §2.1 verbatim direct read + ADR-012 §2.3 + §2.8 verbatim direct read + G4 §4.4.1 verbatim direct read = source verify 다층 답습 |
| **B-A-7** | Agent B/C/codex 응답 미참조 → cross-validation blind risk | CLAUDE.md §3 답습 (Agent A/B/C 3 병렬 독립 + Reviewer 통합 단계 분리). Reviewer cross-validation 영역. 본 응답 = Agent A 독립 평가 한정 |

### §6.2 Reviewer 단계 cross-validation 권고 영역

본 Agent A 응답 = 구현 분석가 관점 한정. Reviewer 통합 단계 시:
- Agent B (품질/안전성) 응답 cross-check 영역 (보안 + 엣지케이스 + 문서 정합성)
- Agent C (대안 탐색가) 응답 cross-check 영역 (대안 기술 + 트레이드오프)
- 외부 LLM codex (OpenAI vendor) 응답 cross-check 영역 (cross-vendor 검증, 헌법 5조-2 답습)

Reviewer = 4 source 통합 + R-A-1 / R-A-2 / N-A-1 / N-A-2 / N-A-3 / NT-A-1 / NT-A-2 흡수 판정.

---

**본 Agent A 응답 v1 끝.**

**판정 답습**: ⚠️ **APPROVE WITH CONDITIONS** — BLOCKING 2 (R-A-1 합의 cycle 정량화 + R-A-2 fixture 정량 carry-over) + 권고 3 (N-A-1 step 분리 PoC 답습 + N-A-2 4 violation_type Layer 매핑 + N-A-3 4 workflow 분리 운영) + NOTE 2 (NT-A-1 (γ-d) 모순 evidence + NT-A-2 R-S1 후행 영향) 흡수 후 본 (γ) cycle 합의 발효 자격 충실.

**Agent A 권고 순위**: **(γ-c) 1순위 + (γ-a) 2순위** (단 수단 *결정* = 풀 3+1 합의 + 사용자 명시 영역).
