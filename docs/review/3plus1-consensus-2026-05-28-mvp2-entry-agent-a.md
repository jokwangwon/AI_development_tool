# MVP-2 진입 합의 entry brief — Agent A (구현 분석가) 응답

> **검토자**: Agent A — 구현 분석가
>
> **핵심 질문**: "실제로 동작하는가?" (기술적 구현 가능성 / 의존성 / 성능)
>
> **작성일**: 2026-05-28 (52 entry 진입 cycle 풀 3+1 병렬 phase)
>
> **검토 대상**: `docs/phase0/mvp2-entry-brief.md` (v1, 480줄, §0~§10)
>
> **병렬 독립 평가 의무**: 다른 Agent (B / C / 외부 LLM codex) 응답 *참조 금지* — Reviewer 통합 시점 cross-check
>
> **답습 제약**: 본 응답 = entry brief 평가 한정. 본 응답 자체에서 (i) sub-수단 결정 / (ii) threshold 고정 / (iii) MVP-2 진입 발효 / (iv) ADR/헌법 본문 변경 / (v) 실 코드 / CI 변경 — 0건.

---

## 직접 read 한 자료

| # | path | 영역 |
|---|------|-----|
| 1 | `docs/phase0/mvp2-entry-brief.md` | 검토 대상 v1 480줄 전체 |
| 2 | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` | 51 entry audit brief (입력 자료) 전체 |
| 3 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` | 51 entry 합의 보고서 전체 |
| 4 | `docs/architecture/governance-preconditions.md` (line 410~466) | §4 GP-2 정의 + Entry/Exit/산출/의존 ADR |
| 5 | `docs/architecture/provider-agnostic-memory-skill-design.md` (line 615~680) | §4.4 Layer 1~5 본문 |
| 6 | `docs/decisions/ADR-012-evidence-ledger-protection.md` (line 155~185, 230~272, 340~380) | §2.3 (4 Layer) / §2.6 genesis / §2.7 prev_hash 실패 / §2.8 Full Rewrite 5 Layer / §3.1 external LLM entry |
| 7 | `docs/decisions/ADR-011-means-vs-ends-redaction.md` (line 40~75) | §2.1 (a)~(d) 4조건 모법 본문 |
| 8 | `docs/architecture/implementation-runtime-roadmap-mvp1.md` (line 85~108) | §1.2 3-layer + §1.3 GP-2 = MVP-2 분리 사유 |
| 9 | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (line 1~80) | 24 entry 답습 source |
| 10 | `docs/architecture/redaction-pattern-equivalence.md` (line 46, 445, 494) verbatim | R-4 답습 — `agent/redact.py` 실 위치 `/tmp/hermes-phase0/...` 확인 |
| 11 | filesystem inspection | `agent/` directory **부재** / `src/adapters/llm/facade.py` placeholder 확인 / `.github/workflows/` 12 workflow 列 / `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` 존재 / `tests/canonical/` 24 fixtures (8 카테고리 × 3) + `tests/fixtures/jsonl_ledger/{pass,fail}` |

---

## §0 총평

**판정**: ✅ **APPROVE WITH CONDITIONS** (구현 분석가 관점)

**근거 요약**:
- brief 의 framing (영역 진입 ≠ sub-수단 결정 분리 + W-A 통합 권고 + R-S1 자기진단 + 5조건 매트릭스) 은 *구조적으로* 정확하며 §0.3 27 금지 + §6.2 10 금지 다층 답습 충실.
- **그러나 §2 진입 자격 매트릭스에 *실 repo 상태 vs brief 표기 불일치* 결함 2건이 carry-over 됨** — 51 entry brief 의 동일 결함이 본 (α) brief 에 무수정 답습됨. 본 결함은 sub-수단 결정 cycle (β) 시점이 아닌 *본 (α) 진입 자격 발효 시점* 에 의사결정 입력을 왜곡시킬 위험이 있어 *조건* 으로 명시 의무.
- "W-A 통합" (단일 R-6 workflow `r2-canary.yml` 확장) 권고는 실 repo 의 *이미 분리 운영 중인 workflow 구조* (`g4-hash-chain.yml` + `history-anchor-verifier.yml` + `rewrite-defense.yml` + `r2-canary.yml` 등 12 workflow) 와 *기술 사실 충돌* — 구현 분석가 관점에서 sub-수단 결정 cycle (β) 진입 시점 BLOCKING 가능성 prepended 의무.

**BLOCKING**: **2건** (R-A-1, R-A-2)
**권고**: **4건** (N-A-1, N-A-2, N-A-3, N-A-4)
**NOTE**: **2건** (NT-A-1, NT-A-2)

---

## §1 BLOCKING 2건

### R-A-1 (BLOCKING) — `agent/redact.py` 위치 framing 모호 + 본 repo 內 부재 사실 미명시

**brief 영역**: §2.1.2 Entry 조건 표 row 2 + §1.1 GP-2 영역 정의 line 100 + 51 entry audit brief §2.1 Entry 조건 #2 carry-over.

**brief 본문 (line 136)**:
> | Hermes native redaction `agent/redact.py` 존재 확인 | ✅ 충족 | (그대로 유지) |

**실 repo 사실 (filesystem 확인)**:
- `find . -name "redact.py"` 결과 = **본 repo 內 0건**
- `agent/` directory 자체 부재 (`ls /home/delangi/문서/project/category/AI_development_tool/agent/` → `No such file`)
- `redaction-pattern-equivalence.md` line 46 verbatim: `**출처**: /tmp/hermes-phase0/hermes-agent/agent/redact.py (v0.12.0 main HEAD, 401 LOC)` — 즉 *Hermes upstream container HEAD 內 파일* (본 repo 외 `/tmp/hermes-phase0/` clone)

**구현 분석가 관점 문제**:
1. (R-1) Hermes native redaction 의 본 cycle 후속 (β) sub-수단 결정 시 실 구현 경로 = "Hermes container 운영 시점 native redaction 적용" — 본 repo 內 `agent/redact.py` *수정 필요 시* 라는 함의가 brief framing 으로부터 도출될 위험. 실제 = **Hermes upstream 의 R-4.1 답습 catalog 검증 evidence 추가 + Hermes container 환경 內 운영 시점 검증** 영역. brief framing 모호로 인해 (β) cycle 진입 시점 BLOCKING 으로 격상 가능성.
2. (R-2) P1 facade RedactionFilter = `src/adapters/llm/facade.py` 의 1390 byte **placeholder** (TR-1 (d) carry-over 명시). 본 brief §0.3 #24 + §2.1.2 + §8.1 #3 모두 "TR-1 (d) carry-over 의존" 명시 충실 — *그러나* §2.1.2 Entry 표는 R-2 의존 영역을 *진입 자격 평가* 內 명시 *0건* (R-1 만 평가). R-2 진입 자격 = `facade.py` placeholder → real 변환 의존 = **본 cycle 합의 발효 후에도 미충족** 상태 carry-over → (β) cycle 시점 BLOCKING.
3. (R-3) `r2-canary.yml` (5476 byte) 의 R-3 답습 확장 = 본 brief §2.3.1 W-A 통합 권고 의존 영역 — R-A-2 와 연계.

**brief 의 처리 충분성**:
- brief §10 P-4 R-S1 risk 1 = ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 위험만 명시 (G4 §4.4 영역)
- **GP-2 영역 R-A-1 위험 (Hermes upstream 위치 framing) = P-1 ~ P-7 7 자기진단 內 0건**
- 51 entry audit brief 동일 결함 (line 115) → 본 brief 무수정 답습 → P-3 자기진단 "51 brief 결함 잔존 시 cascade" 명시했으나 *실 cascade 검출 0건* (오히려 51 brief = "5/5 trigger 0건 + 14/14 verbatim" cross-confirm 으로 결함 발견 회피).

**처리 권고 (조건 명시 의무)**:
- brief v1.1 1pass 흡수 시 §2.1.2 Entry 표 row 2 "✅ 충족" framing 명확화:
  - 수정안 예: `Hermes native redaction agent/redact.py 존재 확인 (Hermes upstream HEAD /tmp/hermes-phase0/hermes-agent/agent/redact.py 401 LOC, R-4 답습 source) — Hermes upstream 영역 충족 / 본 repo 內 fork / patch 0건 (의도된 영역 분리)` ✅ 충족 (upstream 영역 한정)
- §1.1 GP-2 영역 정의 cross-reference 추가 (Hermes upstream R-4 답습 source line 46 verbatim)
- §10 자기진단 P-8 신규 추가 (51 brief framing 모호 cascade 인식 — R-S2 유형)

---

### R-A-2 (BLOCKING) — "W-A 단일 R-6 workflow 확장 통합" 권고가 실 repo *이미 분리 운영 중* workflow 구조와 기술 사실 충돌

**brief 영역**: §2.3 두 영역 통합 R-6 workflow 확장 + §1.3 선차 변경 매트릭스 row 3 + 51 entry audit brief §4.

**brief 본문 (line 200~215)**:
> ✅ 두 영역 모두 R-6 workflow 답습 확장 동일 영역 = W-A 통합 자격 충족
> ✅ ceremony-inflation 차단 + CI 자원 효율 + evidence 통합 + branch protection contexts 추가 부담 회피 (43 entry 8 contexts 답습) — W-A 정당

**실 repo 사실 (`.github/workflows/` 12 workflow 명시 확인)**:
| workflow | size | 영역 |
|---------|------|----|
| `r2-canary.yml` | 5476 | R-2/R-4.1 canary (현재 GP-2 영역 보조 만) |
| **`g4-hash-chain.yml`** | **10652** | **G4 Hash Chain + JCS — Group C PoC (이미 운영, header verbatim "G4 *부분 충족 시제* 한정 — G4 전체 PASS 권한 0건")** |
| `history-anchor-verifier.yml` | 19094 | G4 history anchor (Layer 2 답습) |
| `rewrite-defense.yml` | 16454 | ADR-012 §2.8 Full Rewrite 5 Layer 답습 |
| `evidence-pass-gate.yml` | 3635 | Layer 2 PASS gate |
| `schema-validation.yml` | 12684 | schema 답습 |
| (외 6 workflow) | | |

**구현 분석가 관점 문제**:
1. G4 §4.4 Layer 4 (CI 회귀 검증) 의 *Layer 1 + Layer 2 자동 회귀 step* = 이미 `g4-hash-chain.yml` + `history-anchor-verifier.yml` + `rewrite-defense.yml` 3 workflow 에서 분산 운영 중. brief 의 "단일 R-6 (`r2-canary.yml`) 확장" 권고는 = (i) 기존 3 workflow → 1 workflow 통합 (대규모 회귀 risk + branch protection contexts 변경 risk) 또는 (ii) 기존 3 workflow 보존 + r2-canary.yml 에 *중복 step* 추가 (CI 자원 비효율, brief 의 W-A 정당화 자체와 충돌) 둘 중 하나로 해석 가능 — **brief framing 어느 쪽도 명시 0건**.
2. brief §2.3.1 line 202 "단일 R-6 workflow (`r2-canary.yml`) 확장 통합" = 51 audit brief §4.1 line 205 line 206 "두 영역 모두 동일 R-6 workflow (`r2-canary.yml`) 확장 대상" 으로부터 carry-over. **그러나** 51 audit brief 작성 시점 (2026-05-28 09 시 추정) → 본 brief 작성 시점 (동일 일자) 사이에 `g4-hash-chain.yml` 등 신규 workflow 발견 0건 (작성자 read 절차 부재).
3. brief §1.3 row 3 권위 정당성 "단점 = step 수 증가 / 실패 영역 식별 복잡도 ↑ 명시 (51 brief §4.2 답습) — step name 분리 완화 답습" → 본 단점 진단 자체가 *기존 workflow 분리 운영의 의도된 이점* 을 무효화 risk.
4. **branch protection 8 contexts (43 entry 답습)** 와의 의존: `g4-hash-chain.yml` + `rewrite-defense.yml` + `history-anchor-verifier.yml` 가 contexts 內 등록 가능성 — 만약 W-A 통합 → 기존 workflow polyfill / removal 시 8 contexts 깨짐 → 사용자 admin scope 변경 의무 (43 entry 답습 carry-over).

**brief 의 처리 충분성**:
- §10 P-6 = "W-A 통합 권고가 사용자 영역 침입 위험" 만 명시 (사용자 결정 영역 보존 framing) — *기술 사실 충돌* 진단 0건
- §2.3.3 row 3 = "branch protection contexts 추가 영역 결정 사용자 영역 carry-over" 만 명시 — *기존 contexts removal risk* 진단 0건
- §3 매트릭스 (d) gap = "R-6 workflow 답습 확장 (§2.3 W-A 통합)" 만 명시 — *기존 g4-hash-chain.yml 등 운영 중 workflow 와의 관계* 0건

**처리 권고 (조건 명시 의무)**:
- brief v1.1 1pass 흡수 시 §2.3 신규 §2.3.4 추가:
  - "기존 운영 중 workflow 매트릭스 (`g4-hash-chain.yml` + `history-anchor-verifier.yml` + `rewrite-defense.yml` 등) cross-reference"
  - "W-A 통합 = (i) 기존 3 workflow 일괄 통합 vs (ii) 보존 + 신규 step 분산 추가 vs (iii) `r2-canary.yml` 한정 GP-2 step 추가 + G4 §4.4 Layer 4 영역은 기존 workflow 확장 — 3 옵션 후보 (β) cycle 결정 영역" 명시
- §1.3 row 3 권위 정당성 추가 cross-reference: "본 (α) 합의 발효 후 (β) sub-수단 결정 cycle 시점에 기존 workflow 운영 사실 cross-check 의무"
- §10 자기진단 P-9 신규 추가: "기존 운영 workflow cross-check 부재 R-S3 risk — Reviewer 단독 verify 자격"

---

## §2 권고 4건

### N-A-1 (권고) — `tools/jsonl_hash_chain.py` 등 G4 Layer 1 사전 구현 *이미 존재* 사실 brief 미반영

**brief 영역**: §2.2.2 Entry 자격 표 row 4~7.

**brief 본문 (line 173~176)**:
> | Layer 1 (hash chain) 실 구현 (의존 영역) | ❌ gap | (β) sub-수단 결정 + 실 구현 sub-cycle 영역 |
> | canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ❌ gap | 실 구현 sub-cycle 영역 |
> | Layer 4 CI step 실 구현 | ❌ gap | 실 구현 sub-cycle 영역 |
> | ledger 첫 entry (genesis hash) | ❌ gap | (γ) 분리 영역 결정 cycle 영역 — Layer 1 의존 |

**실 repo 사실**:
- `tools/jsonl_hash_chain.py` 존재 (genesis hash 함수 `compute_genesis_hash(scope, schema_version)` line 85~90 + 4 violation_type 포함 = `prev_hash_mismatch` / `hash_recalculation` / `history_rewrite` / `genesis_mismatch`)
- `tools/canonical_json.py` 존재 (canonical JSON 구현)
- `tests/canonical/` 24 fixtures (8 카테고리 × 3 = array / escape / hash_stability / key_ordering / lossy / nested / number / unicode) — **RFC 8785 reference corpus ≥ 20 충족 가능성 매우 높음**
- `tests/fixtures/jsonl_ledger/{pass, fail}` 존재 — Layer 1 PoC fixture
- `.github/workflows/g4-hash-chain.yml` header verbatim: `corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성) + NaN/Inf reject 2건 + PASS fixture × 2 + FAIL fixture × 4 + Round-trip PASS fixture` = **PoC 시제 운영 중**
- **그러나** workflow header line 21 verbatim: `본 PoC 는 G4 *부분 충족 시제* 한정 — G4 전체 PASS 권한 0건 (사용자 명시 답습)` — 즉 PoC 시제 (진입 자격 충족) ≠ G4 §4.4 Layer 4 PASS 발효 자격 (의도된 분리)

**구현 분석가 관점**:
- brief §2.2.2 "❌ gap" 표기 = *PASS 발효 자격* 관점으로 해석 시 정확 / *구현 존재* 관점으로 해석 시 *과소 표기* (실제는 PoC 시제 충족 + PASS 발효는 별도 cycle)
- brief 의 framing = "(β) sub-수단 결정 + 실 구현 sub-cycle 영역" → 사용자가 "신규 구현 필요" 로 *오해할 risk* (실제는 *기존 PoC 시제 → PASS 시제 격상* 영역)
- 단, brief §2.2.4 미발효 영역 (deferred) = "Implementation Evidence PASS 발효 = 실 구현 + PoC + R-6 actual run PASS + 합의 후 별도" 명시 = 부분 완화

**처리 권고 (조건 X, 정보 보강)**:
- brief v1.1 1pass 흡수 시 §2.2.2 Entry 자격 표 4 row "❌ gap" → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 으로 격상 + 의존 path (`tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `tests/canonical/` + `.github/workflows/g4-hash-chain.yml`) 명시
- §3 매트릭스 (b) row 2 "❌ gap — Docker 격리 PoC 3종 = 실 구현 sub-cycle 영역" → "⚠️ 부분 — `g4-hash-chain.yml` PoC 운영 중 / PASS 시제 격상 영역 = 실 구현 sub-cycle"

---

### N-A-2 (권고) — §2.3 R-6 workflow `r2-canary.yml` actual run ID evidence 누락

**brief 영역**: §5.2 Evidence Required E-7.

**brief 본문 (line 310)**:
> | E-7 | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (43 entry 답습) |

**51 entry audit brief 본문 (line 266)**:
> | E-7 | R-6 workflow 확장 step actual run PASS | GitHub Actions run ID + verdict PASS (43 entry actual run id 답습 유의 — 42 entry `25623028888` 답습) |

**구현 분석가 관점**:
- 51 audit brief E-7 = actual run ID `25623028888` (42 entry 답습) 명시 → 본 brief E-7 carry-over 시 actual run ID **누락** (본 cycle 진입 시점 신규 actual run 미확보)
- 본 (α) 합의 발효 시점 Evidence E-7 = 사후 evidence (실 구현 sub-cycle 後) 영역으로 분리됨 = 정합 (E-7 = MVP-2 Implementation Evidence PASS 발효 시점 의무)
- 단 brief v1.1 흡수 시 51 audit brief 답습 evidence 명시성 유지 권고

**처리 권고**:
- brief §5.2 E-7 본문에 "(42 entry actual run id `25623028888` 답습)" 추가 또는 명시적 carry-over framing 추가
- E-7 = 본 (α) 합의 발효 시점 ≠ 충족, MVP-2 Implementation Evidence PASS 발효 시점 의무 충족 영역 영구 분리 명시

---

### N-A-3 (권고) — §5.3 JSONL Ledger event enum 후보 신규 등록 = ADR-012 §2.2 본문 변경 trigger 명시 부재

**brief 영역**: §5.3 JSONL Ledger event enum 후보 + §0.3 #19 ADR 본문 갱신 0건 + §9.5 cross-reference 갱신.

**brief 본문 (line 314~324)**:
> 본 cycle 합의 발효 시 신규 등록 자격 (ADR-012 §2.2 답습 + G4 §4.2 11 필드 schema event enum):
> | 1 | `gp2_redaction_layer1_implementation` | GP-2 | ADR-012 §2.2 line 150~152 답습 패턴 (MVP-1 Stage 1/2/3 답습) |
> | 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
> | 3 | `r6_workflow_extension_mvp2` | 통합 | R-6 답습 확장 시점 |
> → 본 enum 후보 = ADR-012 §2.2 후속 합의 영역 (본 (α) 합의 후 ADR-012 §2.2 cross-reference 갱신 별도 commit).

**구현 분석가 관점**:
- ADR-012 §2.2 line 155~158 verbatim 확인 결과 = 23~25 enum 등록 시점 = "Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족". 즉 enum 등록 = *별도 합의 형태 (풀 3+1 + APPROVE)* 필요 영역.
- brief §5.3 "본 (α) 합의 후 ADR-012 §2.2 cross-reference 갱신 별도 commit" = framing 모호 — "cross-reference 갱신" 이라 표현했으나 enum 신규 등록 = **ADR-012 §2.2 본문 *변경*** (line 155~158 표 row 26~28 추가). brief §0.3 #19 "ADR 본문 갱신 0건" 자체 금지와 충돌 가능성.
- 정확한 framing: enum 등록 = ADR-012 §2.2 본문 변경 → 별도 풀 3+1 합의 필요 (MVP-1 PASS §C-2 답습 패턴) → 본 (α) 합의 발효 ≠ enum 등록 자격 발효.

**처리 권고**:
- brief §5.3 본문에 "본 enum 후보 = 후보 식별 한정. *결정* / *등록 발효* = ADR-012 §2.2 본문 변경 (line 155~158 표) = 별도 풀 3+1 합의 영역 (Backlog #5 합의 답습 패턴, MVP-1 PASS §C-2 답습)" 명시 추가
- §9.5 row 2 "ADR-012 §2.2 event enum 신규 등록" 도 동일 framing 보강

---

### N-A-4 (권고) — §1.3 P-4 R-S1 risk 처리 = "Reviewer 단독 verify 자격" 권고 후속 절차 명시 부재

**brief 영역**: §1.3 선차 변경 매트릭스 row 2 + §10 P-4 + §9.5 cross-reference 갱신 영역.

**brief 본문 (line 110)**:
> ⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY". 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역).

**구현 분석가 관점 (verbatim 재확인 결과)**:
- ADR-012 §2.3 line 165~185 직접 read 결과:
  - Layer 1 (line 165): Hash Chain MANDATORY
  - Layer 2 (line 171): Git append-only branch MANDATORY
  - Layer 3 (line 177): Signed commit RECOMMENDED MVP / MANDATORY multi-host
  - **Layer 4 (line 182): External anchor — RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점** ← (Layer 4 = External anchor)
- G4 §4.4.1 (provider-agnostic-memory-skill-design line 629~660) 직접 read 결과:
  - Layer 1 + 2 + 3 동일
  - **Layer 4 (line 649): CI 회귀 검증 MANDATORY** ← (Layer 4 = CI 회귀 검증, 신규 신설)
  - **Layer 5 (line 655): External Anchor** ← (Layer 5 = External anchor, 시프트)
- ADR-012 §2.8 Full Rewrite 방어 (line 264~272) = **5 Layer** 강제 명시 (Layer 4 = CI 회귀 검증, Layer 5 = External anchor) ← G4 §4.4.1 과 일치
- ⭐ **R-S1 진단 결과**: ADR-012 §2.3 (4 Layer, Layer 4 = External anchor) vs ADR-012 §2.8 (5 Layer, Layer 4 = CI 회귀 검증) **본문 內부 자체 불일치 존재** + G4 §4.4.1 (5 Layer) 와 ADR-012 §2.3 (4 Layer) 사이 정의 불일치 = **권위 chain 다중 source 손상** (확정 trigger 4 발화)
- brief §4.3 "trigger (4) 부분 발화 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역)" = 정확 framing
- 단 본 brief 자체에서 "확정 trigger 4 발화" 까지 격상 0 — 본 Agent A verify 결과 = trigger 4 **확정 발화** (부분 발화 아님)

**처리 권고 (조건 X, Reviewer 통합 시점 격상 권고)**:
- Reviewer 통합 시 §1.3 row 2 권위 정당성 표기 변경: "⚠️ 권위 미세 충돌" → "⚠️ 권위 chain 다중 source 손상 *확정* (R-S1 확정)" 격상
- §10 P-4 본문 변경: "R-S1 유형 잠재 risk 1" → "R-S1 확정 risk 1"
- §9.5 row 4 "R-S1 정정 영역" 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle 형태 = **풀 3+1 + 외부 LLM 1+ 의무** 명시 (cross-reference 정정 = ADR-012 §2.3 본문 변경 = T3 영역)
- 본 권고 = Agent A verify 결과 cross-confirm 사실 → Reviewer 통합 시 cross-check 후 최종 격상 판단 (Agent B/C cross-confirm 시점)

---

## §3 NOTE 2건

### NT-A-1 (NOTE) — 24 entry 답습 동형 패턴의 *분리* framing = 정확

**brief 영역**: §1.3 row 4 + §10 P-5.

24 entry brief §0.4 verbatim (line 76~80) 직접 read 결과:
> ✅ 본 brief 발효 결과 = 4 sub-수단 *채택 결정 발효* + 실 구현 sub-cycle 진입 권한 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택

본 brief §0.4 verbatim (line 75~76):
> ✅ 본 brief 발효 결과 = **MVP-2 영역 진입 권한 발효** + (β) sub-수단 결정 cycle 진입 자격 발효 + (γ) 분리 영역 결정 cycle 진입 자격 발효 + Rollback Trigger 본문 채택 + Evidence 형식 본문 채택

→ **차이 framing 정확**: 24 entry = "sub-수단 채택 결정 발효" / 본 (α) = "영역 진입 권한 발효" + "sub-수단 결정 cycle 진입 자격 발효" (2-step 분리). 본 분리 framing = **정확** — 25 조합 (R-1~R-5 × L-1~L-5) 복잡도 답습 + 단계별 cycle 답습 충실.

**NOTE**: 본 framing 분리 정확성 = brief 강점. 단 *사용자 진입 명령 framing* (§0.1 carry-over "4번으로 진행") 이 "(α) MVP-2 진입 합의 entry brief 작성" 한정 = 사용자 의도 정확 답습 — Reviewer 통합 시 사용자 의도 cross-confirm 의무.

---

### NT-A-2 (NOTE) — ADR-011 §2.1 본문 = (a)~(d) 4조건 명시, (e) = 본 brief 의 *합의 APPROVE 운영조건* 추가 framing

**brief 영역**: §3 매트릭스 + §1.1 표 row 5 + §0.3 #15 + §6.2 #4.

ADR-011 §2.1 verbatim (line 54~59) 직접 read 결과:
> | (a) | 동등 이상의 보안 결과 | ... |
> | (b) | 격리 환경 PoC로 실증 | ... |
> | (c) | ADR 권위로 명시 | ... |
> | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

→ ADR-011 §2.1 본문 = **(a)~(d) 4조건** (모법 4조건). brief 의 "(a)~(e) 5조건" framing 中 (e) = "합의 APPROVE 운영조건" = 본 brief / 51 audit brief / 32 entry MVP-1 PASS 합의 패턴 답습 = **본 cycle 의 후속 운영조건** (ADR-011 §2.1 본문 직접 명시 0).

**NOTE**: 본 framing = brief §1.1 row 5 "ADR-011 §2.1 (a)~(e)" 표기에서 (e) 추가 본문 = 24 entry / 32 entry / 51 audit brief 답습 동형 patterns 으로 정합 — 단 ADR-011 §2.1 **본문 자체** 는 4조건이며 (e) 는 *후속 운영조건* 임을 명시적으로 분리 framing 하는 것이 cross-reference 정확성 향상에 기여. (현 framing 으로도 *완전한 결함 아님* — NOTE 등급).

**처리 권고**: brief v1.1 흡수 시 §1.1 row 5 verbatim 보강 "ADR-011 §2.1 (a)~(d) 4조건 + (e) 합의 APPROVE 운영조건 (본 (α) cycle 답습 패턴, 24 entry / 32 entry / 51 audit brief 동형)" 정도 명시 권고.

---

## §4 검토 의무 5 항목별 평가

### 의무 1 — 기술적 구현 가능성 (R-1 / R-2 / R-3 / L-1 / L-3 / L-5)

| 영역 | 평가 | 근거 |
|------|------|------|
| **(R-1) Hermes native redaction `agent/redact.py`** | ⚠️ **R-A-1 BLOCKING** | 본 repo 內 부재. Hermes upstream `/tmp/hermes-phase0/hermes-agent/agent/redact.py` (v0.12.0 main HEAD, 401 LOC) 영역 — brief framing 모호 |
| **(R-2) P1 facade RedactionFilter** | ⚠️ **R-A-1 연계** | `src/adapters/llm/facade.py` 1390 byte placeholder. TR-1 (d) carry-over 의존 — brief §0.3 #24 + §2.1.2 註 + §8.1 #3 답습 정확 / Entry 표 內 미명시 |
| **(R-3) log file canary inject + grep CI step** | ✅ 충족 가능 | `r2-canary.yml` (5476 byte) 기존 + step 추가 영역 / W-A 통합은 R-A-2 BLOCKING |
| **(L-1) Python stdlib hashlib.sha256 + json.dumps canonical** | ✅ **이미 구현 완료** (`tools/jsonl_hash_chain.py` + `tools/canonical_json.py`) | N-A-1 권고 |
| **(L-3) Layer 4 R-6 workflow step (canonical 위반 + prev_hash mismatch + timestamp monotonicity)** | ✅ **이미 PoC 시제 운영** (`.github/workflows/g4-hash-chain.yml`) | N-A-1 권고 / W-A 통합 = R-A-2 BLOCKING |
| **(L-5) 외부 library (pyjcs / rfc8785) 도입 trigger** | ✅ brief framing 정확 | ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 명시 (brief §0.3 #8 + §6.2 #5) |

### 의무 2 — 의존성 분석 (§2.2.4)

| 의존 영역 | brief framing | Agent A 평가 |
|---------|------------|----------|
| Layer 1 (hash chain) — (β) vs (γ) 분리 정확성 | (β) sub-수단 결정 = L-1~L-5 + (γ) 분리 영역 = Layer 1+2 의존 vs Layer 4 동시 | ✅ 분리 framing 정확. 단 N-A-1 권고 = Layer 1 *기존 구현* PoC 시제 인식 보강 |
| canonical JSON test corpus = `tests/canonical/` 신규 생성 시점 | brief §0.3 #6 "신규 생성 0건" + §2.2.2 Entry "❌ gap" | ⚠️ 부정확 — `tests/canonical/` 24 fixtures 이미 존재 (8 카테고리 × 3) = N-A-1 |
| ledger 첫 entry (genesis hash) = §3 매트릭스 영역 외 의존 | (γ) 분리 영역 결정 cycle 영역 — Layer 1 의존 | ✅ framing 정확 (단 `tools/jsonl_hash_chain.py` `compute_genesis_hash` 함수 이미 구현 — 적용 시점 = 분리 영역) |

### 의무 3 — 두 영역 통합 R-6 workflow 확장 (§2.3 W-A) 실 구현 가능성

| 항목 | 평가 |
|------|------|
| 단일 R-6 workflow 확장 = step name 분리 완화 충분성 | ❌ **R-A-2 BLOCKING** — 기존 분리 운영 workflow (`g4-hash-chain.yml` 외 11) 와 충돌 framing 0건 |
| branch protection contexts 8 (43 entry 답습) → 신규 추가 영역 사용자 admin scope carry-over | ⚠️ 부분 — 신규 contexts 추가 framing 만 있고 *기존 contexts removal risk* (W-A 통합 시 기존 workflow 삭제 / 폐기 시) framing 0건 |

### 의무 4 — 24 entry 답습 source 정합성 (§1.3 분리 framing)

| 항목 | 평가 |
|------|------|
| 24 entry = sub-수단 진입 자격 + 채택 결정 통합 / 본 (α) = 영역 진입 한정 | ✅ NT-A-1 — framing **정확** (24 entry §0.4 verbatim 직접 read cross-confirm) |
| 25 조합 (R-1~R-5 × L-1~L-5) 복잡도 답습 (24 entry 4 sub-수단 보다 복잡) | ✅ §1.3 row 4 + §10 P-5 답습 정확 |

### 의무 5 — 선행 권위 답습 정확성

| 항목 | 평가 |
|------|------|
| 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* 답습 (재선언 0) | ✅ §0.3 #14 + §1.1 row 1 답습 정확 |
| roadmap-mvp1 §1.3 "GP-2 = MVP-2 분리 사유 (C-7 답습)" + "시점 분리 ≠ 영구 제외" | ✅ §1.3 row 1 권위 정당성 답습 정확 (verbatim line 107 cross-confirm) |
| ADR-011 §2.1 (a)~(e) 5조건 답습 정확성 | ⚠️ NT-A-2 — 본문은 (a)~(d) 4조건, (e) = 후속 운영조건 framing 분리 권고 (NOTE 등급) |

---

## §5 자기 편향 자기진단

| # | 잠재 편향 | Agent A 처리 |
|---|--------|----------|
| **SA-1** | "구현 분석가" 관점 편향으로 framing 결함 만 강조 = 시각 협착 | brief framing 강점 (24 entry vs 본 (α) 분리 정확성 NT-A-1 / 5 trigger 검증 §4.3 정확) 도 NOTE 명시 |
| **SA-2** | 본 repo `agent/redact.py` 부재 발견 = Hermes upstream 영역 분리 framing 의 *의도된 분리* 무시 risk | R-A-1 처리 = "본 repo 內 fork / patch 0건 (의도된 영역 분리)" 명시 권고 — 단 framing 모호 자체는 BLOCKING 유지 |
| **SA-3** | `tools/jsonl_hash_chain.py` 등 G4 사전 구현 인식 → "MVP-2 진입 자격 *이미 충족*" 으로 과도 격상 risk | N-A-1 권고 등급 유지 (BLOCKING 격상 0) — PASS 시제 격상 영역은 별도 cycle 영역 (brief §2.2.4 framing 정합) |
| **SA-4** | "W-A 통합 권고 충돌" 진단 = Agent C (대안 탐색가) 영역 침입 risk | R-A-2 = 기술 사실 충돌 한정 (대안 탐색 0) — sub-수단 결정 (β) 시점 BLOCKING 가능성만 명시 |
| **SA-5** | R-S1 verify 결과 (trigger 4 확정 발화) = Reviewer 영역 침입 risk | N-A-4 권고 = Reviewer 통합 시 cross-check 후 최종 격상 판단 명시 (Agent A 단독 격상 0) |
| **SA-6** | 본 Agent A 응답 자체가 *Claude Opus 4.7* 작성 = brief 작성자 동일 LLM cascade risk | Agent A 응답 = 직접 read 11 자료 + filesystem inspection evidence 기반 (verbatim 추출 / file size / line number) — 사용자 영역 cross-check 가능 형태로 evidence 명시 |
| **SA-7** | "BLOCKING 2 + 권고 4" 등급 = 24 entry / 32 entry 패턴 답습 = 자동 격상 risk | 각 BLOCKING / 권고 = 기술 사실 / framing 결함 / Carryover risk 각각 명시 (자동 격상 0) — Reviewer 통합 시점 등급 조정 가능 영역 |

---

## §6 (참고) 본 응답이 *하지 않는* 것

- ❌ sub-수단 결정 (R-1~R-5 / L-1~L-5 중 채택)
- ❌ threshold 고정
- ❌ MVP-2 진입 발효 (본 응답 = entry brief 평가 한정)
- ❌ ADR / 헌법 / roadmap-mvp1 / governance-preconditions / provider-agnostic-memory-skill-design / ADR-012 본문 변경
- ❌ R-S1 cross-reference 정정 (확정 verify 결과 = Reviewer 영역 격상 권고만)
- ❌ W-A vs W-B 분리 결정 (R-A-2 = 기술 사실 충돌 진단 한정, 결정 = (β) cycle 영역)
- ❌ Implementation Evidence PASS 발효 / Operational Readiness PASS / Hermes PMO 격상
- ❌ branch protection contexts 변경 / GitHub API 호출
- ❌ Tier-2/3 catalog 확장 결정 / 외부 library (pyjcs / rfc8785) 도입 결정
- ❌ MVP-1 PASS 재선언
- ❌ Agent B / Agent C / 외부 LLM codex 응답 참조 (병렬 독립 평가 의무)

---

**본 Agent A 응답 v1 끝.**

**다음 단계**: Agent B + Agent C 병렬 독립 응답 + 외부 LLM codex 응답 (이미 capture 완료) → Reviewer 통합 보고서 (cross-check + 일치 / 부분 일치 / 불일치 / 누락 4분류 + 최종 판정 + R-A-1 / R-A-2 BLOCKING 격상 처리 + R-S1 확정 verify cross-confirm).
