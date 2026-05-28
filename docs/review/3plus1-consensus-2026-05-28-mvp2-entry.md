# 풀 3+1 합의 보고서 — MVP-2 진입 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증)

> **본 합의** = Reviewer 통합 합의 보고서. Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) 3 병렬 독립 분석 결과 + 외부 LLM 1+ (codex, OpenAI vendor) 응답 통합. CLAUDE.md §3 3+1 멀티 에이전트 합의 프로토콜 답습.
>
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (cross-vendor 의무, 51 entry audit brief §7.2 답습 + 24 entry MVP-1 1.5차 보강 entry brief 동형 패턴)
> **선행 자료**: [[mvp2-entry-brief]] (v1, 480줄) + [[mvp2-entry-eligibility-audit-brief]] (51 entry, 372줄) + [[3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit]] (51 entry, 184줄) + [[2026-05-28-mvp2-entry-codex-response]] (3597줄 full transcript)
> **상위 권위**: [[ADR-011-means-vs-ends-redaction]] §2.1 (a)~(d) + §2.4 + §3 후속 권위 (e) / [[PROJECT_CONSTITUTION]] 제8조 (보안) + 제5조-2 (Provider Liquidity 비협상) / [[implementation-runtime-roadmap-mvp1]] §1.2 + §1.3 / [[governance-preconditions]] §4 / [[provider-agnostic-memory-skill-design]] §4.4 / [[ADR-012-evidence-ledger-protection]] §2.3 + §2.5 + §2.7 + §2.8 + §3.4

---

## §0 판정 + 결과 요약

**Reviewer 통합 판정**: ⚠️ **REVISE AS ENTRY BRIEF INPUT (BLOCKING 7 + 권고 13)** — brief v1.1 보강 후 본 cycle 합의 발효 자격 충실. 24 entry codex 답습 동형 판정 (codex `REVISE AS ENTRY BRIEF INPUT` 직접 답습).

**4 source 판정 합산** (3 Agent + 외부 LLM 1+):

| Source | Vendor | 판정 | BLOCKING | 권고 | NOTE |
|--------|-------|------|---------|------|------|
| Agent A (구현) | Anthropic Claude | APPROVE WITH CONDITIONS | 2 (R-A-1, R-A-2) | 4 (N-A-1~4) | 2 |
| Agent B (안전성) | Anthropic Claude | REVISE | 2 (R-B-1, R-B-2) | 4 (N-B-1~4) | 3 |
| Agent C (대안) | Anthropic Claude | APPROVE WITH CONDITIONS | 2 (R-C-1, R-C-2) | 6 (N-C-1~6) | 3 |
| codex (외부 LLM 1+) | **OpenAI (cross-vendor)** | **REVISE AS ENTRY BRIEF INPUT** | 3 (R-1, R-2, R-3) | 5 (N-1~5) | 3 |
| **Reviewer 통합** | Anthropic Claude (Opus 4.7) | **REVISE AS ENTRY BRIEF INPUT** | **7** (Consensus 2 + Unique 5) | **13** (중복 제거) | 통합 |

**원칙 준수**: 실 코드 0 / CI 0 / hook 0 / branch protection 0 / config 본문 변경 0 / ADR 본문 갱신 0 / 헌법 갱신 0 / roadmap-mvp1 본문 0 / governance-preconditions 본문 0 / G4 본문 0 / ADR-012 본문 0 / MVP-1 PASS 재선언 0 / MVP-2 Implementation Evidence PASS 발효 0 / Operational Readiness PASS 0 / Hermes PMO 격상 0 / sub-수단 결정 0 / threshold 고정 0 / 자동 진입 0 — **17/17 유지**.

⚠️ **본 합의 = entry 합의 자격 한정**. 본 합의 REVISE → brief v1.1 보강 1pass 흡수 → 본 cycle 합의 발효 시 진입 권한 발효. 본 합의 직후 *자동 (β)/(γ)/실 구현 진입 금지* (단계별 합의 cycle 답습).

---

## §1 4 source cross-validation 매트릭스

### §1.1 4 source 분류 (일치 / 부분 일치 / 불일치 / 누락)

| # | 발견 영역 | codex (OpenAI) | Agent A (Claude 구현) | Agent B (Claude 안전) | Agent C (Claude 대안) | 분류 |
|---|---------|--------------|---------------------|---------------------|---------------------|------|
| 1 | **R-S1 잠재 → CONFIRMED 격상** | ✅ R-2 BLOCKING | ✅ N-A-4 권고 + verbatim verify | ✅ R-B-1 BLOCKING | ✅ verbatim verify (NOTE) | **Consensus 4/4 ⭐⭐⭐⭐ + Reviewer verify 5/5** |
| 2 | **ADR-011 §2.1 (a)~(d) + (e) 후속 운영조건 framing** | ✅ R-1 BLOCKING | ✅ NT-A-2 NOTE | ✅ R-B-2 BLOCKING | (미명시, N-C-6 event enum 영역 외) | **Consensus 3/4 ⭐⭐⭐** |
| 3 | §0.1 "(α) 內 흡수" 잔여 문구 제거 | ✅ R-3 BLOCKING | (미명시) | (미명시) | (미명시) | **codex Unique (BLOCKING 격상)** |
| 4 | **`agent/redact.py` 본 repo 内 부재 (filesystem 직접 inspection)** | (미명시) | ✅ R-A-1 BLOCKING (filesystem) | (미명시) | (미명시) | **Agent A Unique ⭐⭐⭐ (BLOCKING 격상, 51 audit brief carry-over 결함)** |
| 5 | **W-A 통합 권고 vs 실 repo 기존 G4 workflow 분리 운영 충돌** | (미명시) | ✅ R-A-2 BLOCKING (filesystem) | (미명시) | (부분 — R-C-1 W-C/D/E 대안 영역) | **Agent A Unique ⭐⭐⭐ (BLOCKING 격상)** |
| 6 | **`tools/jsonl_hash_chain.py` + `canonical_json.py` + `tests/canonical/` + `g4-hash-chain.yml` PoC 시제 이미 운영 중** | (미명시) | ✅ N-A-1 권고 (filesystem) | (미명시) | (미명시) | **Agent A Unique ⭐⭐⭐ (권고 → BLOCKING 격상 자격, brief §2.2.2 "❌ gap" → "⚠️ PoC 시제 충족 / PASS 시제 미충족")** |
| 7 | W-A 외 W-C/W-D/W-E 3 대안 매트릭스 추가 | (미명시) | (미명시) | (미명시) | ✅ R-C-1 BLOCKING | **Agent C Unique (BLOCKING 격상)** |
| 8 | roadmap.md §5.4 "단축 합의 + PoC evidence" vs 본 cycle "풀 3+1 + 외부 LLM 1+" 격상 차이 명시 부재 | (미명시) | (미명시) | (미명시) | ✅ R-C-2 BLOCKING | **Agent C Unique (BLOCKING 격상)** |

### §1.2 Consensus 영역 (3+ source 일치)

- **C-1 (4/4 source + Reviewer = 5/5)**: **R-S1 = CONFIRMED divergence** (ADR-012 §2.3 4-layer numbering vs §2.8/G4 §4.4.1 5-layer numbering)
- **C-2 (3/4 source 명시)**: ADR-011 §2.1 = (a)~(d) 4조건 모법, (e) = 후속 운영조건 (§3 또는 governance §4.5 Exit 표) — brief 다수 위치 표현 정정 의무

### §1.3 Unique 영역 (단일 source 발견, BLOCKING 격상 자격)

5 unique BLOCKING 모두 흡수 의무 (의도된 영역 분리 framing 미명시 또는 filesystem 사실 충돌, 본 brief v1 v1.1 보강 영역):

- **P-1 (codex Unique)**: §0.1 "(α) 內 흡수" 잔여 문구 제거
- **P-2 (Agent A Unique, filesystem evidence ⭐⭐⭐)**: `agent/redact.py` 본 repo 內 부재 (실 위치 = `/tmp/hermes-phase0/hermes-agent/agent/redact.py` Hermes upstream 401 LOC). 51 audit brief carry-over 결함 (51 brief 도 같은 표기 사용)
- **P-3 (Agent A Unique, filesystem evidence ⭐⭐⭐)**: `.github/workflows/g4-hash-chain.yml` (10652B) + `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) 이미 분리 운영 — brief W-A 통합 권고와 충돌
- **P-4 (Agent A Unique, filesystem evidence ⭐⭐⭐)**: `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type) + `tools/canonical_json.py` + `tests/canonical/` 24 fixtures + `g4-hash-chain.yml` PoC 시제 이미 운영 — brief §2.2.2 "❌ gap" 4 row → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상
- **P-5 (Agent C Unique)**: W-A 외 W-C/W-D/W-E 3 대안 매트릭스 추가 (W-C 단계 분리, W-D roadmap.md §5.3 답습 별도 progression, W-E pre-commit hook 활용)
- **P-6 (Agent C Unique)**: roadmap.md §5.4 "단축 합의 + PoC evidence" vs 본 cycle "풀 3+1 + 외부 LLM 1+" 격상 차이 명시 부재 (§1.3 항목 5 추가)

### §1.4 cross-vendor blind 충족 (헌법 5조-2)

- 응답 vendor 분포: **OpenAI (codex) 1 + Anthropic (Agent A/B/C) 3 = cross-vendor 형식 충족**
- 본 cycle 합의 발효 자격 = 헌법 5조-2 Provider Liquidity 비협상 답습 충실

---

## §2 BLOCKING 7건 통합 매트릭스

| # | 식별자 | 영역 | source | brief 영향 영역 | 흡수 방향 |
|---|--------|-----|-------|--------------|---------|
| **B-1** | C-1 (Consensus 4/4 + Reviewer = 5/5) | **R-S1 CONFIRMED 격상** | codex R-2 + Agent A N-A-4 + Agent B R-B-1 + Agent C verify + Reviewer 단독 verify | brief §10 P-4 "잠재 risk" → "CONFIRMED divergence" 격상 + §1.3 G4 §4.4 Layer 4 항목 답습 보강 + §4.3 trigger (4) "부분 발화" → "발화" 격상 + §9.5 cross-reference 정정 cycle 사용자 명시 영역 추가 | v1.1 §10 P-4 본문 정정 + §1.3 + §4.3 + §9.5 |
| **B-2** | C-2 (Consensus 3/4) | **ADR-011 §2.1 framing 정정** | codex R-1 + Agent A NT-A-2 + Agent B R-B-2 | brief 다수 위치 "(a)~(e) 5조건" → "(a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건" 정정. 영향 영역: §0.2 #5, §0.4, §1.1, §3, §4 등 | v1.1 다수 위치 정정 (sed 또는 직접) |
| **B-3** | P-1 (codex Unique) | §0.1 "(α) 內 흡수" 잔여 문구 제거 | codex R-3 | brief §0.1 line ~33 verbatim 정정 | v1.1 §0.1 직접 정정 |
| **B-4** | P-2 (Agent A Unique, filesystem) | **`agent/redact.py` framing 명확화 — 본 repo 內 vs Hermes upstream** | Agent A R-A-1 (filesystem inspection) | brief §2.1.1 영역 정의 + §2.1.2 Entry 표 "✅ 충족" 표기 framing 명확화 의무. 51 audit brief carry-over 결함 명문 | v1.1 §2.1.1 + §2.1.2 framing 정밀화. 51 audit brief 자체는 본 cycle 영역 외 (별도 cross-reference 정정 cycle 사용자 영역) |
| **B-5** | P-3 (Agent A Unique, filesystem) | **W-A 통합 권고 framing 정밀화 — 실 repo 기존 G4 workflow 분리 운영 답습** | Agent A R-A-2 (filesystem inspection) | brief §2.3 W-A 권고 → 3 옵션 명시 의무: (i) 일괄 통합 / (ii) 보존 + 중복 step 추가 / (iii) 분산 추가. 실 repo 기존 `g4-hash-chain.yml` + `history-anchor-verifier.yml` + `rewrite-defense.yml` answer 답습 | v1.1 §2.3 + §1.3 W-A 권고 framing 정밀화 |
| **B-6** | P-4 (Agent A Unique, filesystem) | **brief §2.2.2 "❌ gap" 4 row → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상** | Agent A N-A-1 (filesystem inspection, BLOCKING 격상 자격) | brief §2.2.2 표 4 row 격상 + §3 매트릭스 (b)+(d) gap row 정밀화 + §2.2.4 미발효 영역 답습 보강 | v1.1 §2.2.2 + §3 + §2.2.4 정밀화 |
| **B-7** | P-5 (Agent C Unique) + P-6 (Agent C Unique) | **§1.3 + §2.3 대안 매트릭스 + 격상 차이 명시 추가** | Agent C R-C-1 + R-C-2 | brief §1.3 항목 5 (roadmap.md §5.4 "단축 합의" 격상 차이) 추가 + §2.3 W-A 외 W-C (단계 분리) / W-D (그룹 C+D 별도) / W-E (pre-commit hook) 3 대안 매트릭스 추가 | v1.1 §1.3 항목 5 + §2.3 대안 매트릭스 확장 |

---

## §3 권고 13건 통합 매트릭스 (중복 제거)

| # | 권고 | source | 영역 |
|---|------|-------|------|
| N-1 | Rollback Trigger 본문 "채택" vs "후보" 표현 분리 (entry brief input 단계 vs Implementation Evidence PASS 단계) | codex N-1 + Agent A 영역 | §0.4 + §5 |
| N-2 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 표현 | codex N-2 | §2.2.3 + §8.1 |
| N-3 | RT-5 `canonical_json_fallback 또는 BLOCK` 표현 분리 (위반 검출 = BLOCK, fallback = ledger entry + review) | codex N-3 | §5.1 RT-5 |
| N-4 | E-9 외부 LLM evidence `agent="user"` attribution 명시 | codex N-4 | §5.2 E-9 |
| N-5 | JSONL event enum 후보 "reserved candidate" 표현 격하 (ADR-012 §2.2 amendment 전까지 non-authoritative) | codex N-5 + Agent A N-A-3 | §5.3 |
| N-6 | E-7 evidence carry-over 시 42 entry actual run id `25623028888` 답습 framing 추가 | Agent A N-A-2 | §5.2 E-7 |
| N-7 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) | Agent B N-B-1 | §4.3 |
| N-8 | sub-수단 결정 분리 = 24 entry 답습 형태 변경 자격 명문 | Agent B N-B-2 | §1.3 |
| N-9 | 헌법 8조 본질 보조 영역 본문 답습 보강 | Agent B N-B-3 | §1.1 + §9.1 |
| N-10 | Provider Liquidity sub-수단 자격 평가 본문 명시 | Agent B N-B-4 | §1.1 + §4.1 |
| N-11 | (β) sub-수단 결정 분리 정당화 보강 (25 조합 복잡도 답습) | Agent C N-C-1 | §1.3 |
| N-12 | (γ) 4 대안 매트릭스 ((γ-a) Layer 1+2 우선 → Layer 4 후속 / (γ-b) Layer 4 단독 / (γ-c) Layer 1+2+4 동시 / (γ-d) Layer 4 + Layer 1+2 별도) + L 외부 library trade-off + L-1.5 alternative | Agent C N-C-2 + N-C-3 | §2.2.4 + §8.1 |
| N-13 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 | Agent C N-C-5 + N-C-6 | §9.5 |

---

## §4 R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 결과

### §4.1 Verbatim 직접 read 결과 (Reviewer 단독, 24 entry R-S1 답습 패턴)

**ADR-012 §2.3 line 165~185 (4-layer numbering)** — Reviewer 직접 read verbatim:
- Layer 1 — Hash Chain (MANDATORY 모든 환경)
- Layer 2 — Git append-only branch (MANDATORY)
- Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)
- **Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**

**ADR-012 §2.8 line 264~272 (5-layer numbering)** — Reviewer 직접 read verbatim:
- Layer 1: Hash chain (middle entry tampering 차단)
- Layer 2: Git append-only branch + denyNonFastForwards (history 재작성 차단)
- Layer 3: pre-commit hook
- **Layer 4: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지**
- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host): External anchor**

**G4 §4.4.1 line 629~660 (5-layer numbering, ADR-012 §2.8 동형)** — Reviewer 직접 read verbatim (audit 시):
- Layer 1 — Hash Chain (MANDATORY 모든 환경)
- Layer 2 — Git append-only branch (MANDATORY)
- Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)
- **Layer 4 — CI 회귀 검증 (MANDATORY)**
- **Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**

### §4.2 충돌 분석

⭐⭐⭐⭐ **ADR-012 *자체 내부* §2.3 (4-layer) vs §2.8 (5-layer) divergence**:
- §2.3 = External anchor 를 Layer 4 위치 (4 layer 총)
- §2.8 = External anchor 를 Layer 5 위치 + Layer 4 슬롯에 "CI 회귀 검증" 추가 + Layer 3 슬롯에 "pre-commit hook" 추가 (5 layer 총)
- G4 §4.4.1 = §2.8 동형 (5-layer)

→ 동일 ADR-012 문서 *내부* 에서 "Layer N" semantic 이 §2.3 과 §2.8 사이 충돌. 추가로 G4 §4.4.1 = §2.8 답습 답습 → §2.3 만 isolated 4-layer.

### §4.3 R-S1 판정

**R-S1 = CONFIRMED** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer = 5/5).

**유형**:
- 권위 chain 다중 source divergence (ADR-008 §A.2 R1-2 유형 답습 — 24 entry R-S1 답습 패턴)
- 동일 문서 ADR-012 내부 정의 충돌
- 동일 label "Layer 4" 의 semantic collision

**본 cycle 처리** (24 entry R-S1 답습):
- brief v1.1 보강 = 권위 인용 정정 한정 (G4 §4.4.1 + ADR-012 §2.8 line 264~272 직접 답습, §2.3 = numbering 근거 아닌 *원칙* 근거 한정)
- 다중 source 정정 (ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화) = **본 cycle scope 외 별도 cross-reference 정정 cycle 사용자 명시 영역**

### §4.4 brief v1.1 권위 인용 정정 명시 (B-1 흡수)

v1.1 시점 brief 의 G4 §4.4 Layer 4 인용 = 다음 권위 chain 한정:
- **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의)
- **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형)
- **PRINCIPLE ONLY (not numbering)**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙)
- **MONOTONICITY**: `ADR-012 §3.4`
- **PREV_HASH FAILURE**: `ADR-012 §2.7`
- **CANONICAL**: `ADR-012 §2.5` (RFC 8785 JCS)

---

## §5 v1.1 보강 매트릭스 (BLOCKING 7 + 권고 13 1pass 흡수)

### §5.1 BLOCKING 7 흡수 매트릭스

| # | brief 영역 | 보강 본문 |
|---|---------|---------|
| B-1 | §10 P-4 + §1.3 + §4.3 + §9.5 + 신규 §4.4 (권위 인용 정정 명시) | "잠재 risk" → "CONFIRMED divergence" 격상 + 5 source cross-confirm 답습 + 권위 인용 chain 한정 + 별도 cross-reference 정정 cycle 사용자 명시 영역 명문 |
| B-2 | §0.2 #5, §0.4, §1.1, §3, §4 등 다수 | "ADR-011 §2.1 (a)~(e) 5조건" → "ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건" 정정 |
| B-3 | §0.1 | "(β) sub-수단 결정 cycle — 별도 합의 또는 (α) 內 흡수" → "(β) sub-수단 결정 cycle — 별도 합의 (본 cycle 內 흡수 0). 본 cycle 발효 효과는 (β)/(γ) 진입 자격 발효까지" 정정 |
| B-4 | §2.1.1 + §2.1.2 | Hermes native redaction `agent/redact.py` = **Hermes upstream 영역** (본 repo 內 ≠ 동일 path 부재). 본 cycle 의 GP-2 진입 = Hermes upstream `agent/redact.py` 답습 + 본 repo 의 P1 facade RedactionFilter 본문 (TR-1 (d) carry-over 의존) + R-6 workflow 답습 확장 step 통합 framing 명확화 |
| B-5 | §2.3 + §1.3 | W-A 통합 권고 → 3 옵션 명시: (i) 일괄 통합 / (ii) 보존 + 중복 step 추가 / (iii) 분산 추가. 실 repo 기존 `g4-hash-chain.yml` (10652B) + `history-anchor-verifier.yml` (19094B) + `rewrite-defense.yml` (16454B) 답습 명문 |
| B-6 | §2.2.2 + §3 + §2.2.4 | 4 row gap → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상. 답습 evidence: `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `tests/canonical/` 24 fixtures + `g4-hash-chain.yml` PoC 시제 |
| B-7 | §1.3 항목 5 + §2.3 대안 매트릭스 확장 | roadmap.md §5.4 "단축 합의 + PoC evidence" vs 본 cycle "풀 3+1 + 외부 LLM 1+" 격상 차이 명시 + W-A/B/C/D/E 5 대안 매트릭스 |

### §5.2 권고 13 흡수 매트릭스

| # | brief 영역 | 보강 본문 |
|---|---------|---------|
| N-1 | §0.4 + §5 | Rollback Trigger / Evidence = "후보 채택" vs "구현 발효" 표현 분리 명시 |
| N-2 | §2.2.3 + §8.1 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 |
| N-3 | §5.1 RT-5 | "canonical JSON reference mismatch → BLOCK" vs "fallback canonicalizer used → ledger entry + review" 분리 |
| N-4 | §5.2 E-9 | `external_llm_received` ledger entry + `agent="user"` 강제 + vendor/model identifier + 입력 prompt hash 명시 |
| N-5 | §5.3 | event enum 후보 = "reserved candidate" 표현 + ADR-012 §2.2 amendment 전까지 non-authoritative 명문 |
| N-6 | §5.2 E-7 | E-7 evidence carry-over 시 42 entry actual run id `25623028888` 답습 framing 추가 |
| N-7 | §4.3 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
| N-8 | §1.3 | sub-수단 결정 분리 = 24 entry 답습 형태 변경 자격 명문 |
| N-9 | §1.1 + §9.1 | 헌법 8조 보조 영역 본문 답습 보강 |
| N-10 | §1.1 + §4.1 | Provider Liquidity sub-수단 자격 평가 본문 명시 |
| N-11 | §1.3 | (β) 분리 정당화 보강 (25 조합 R-1~R-5 × L-1~L-5 복잡도) |
| N-12 | §2.2.4 + §8.1 | (γ) 4 대안 매트릭스 + L 외부 library trade-off + L-1.5 alternative |
| N-13 | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |

### §5.3 v1.1 1pass 흡수 정직성

- 본 cycle = 1pass 흡수 (ceremony-inflation 차단 메모리 답습, 24 entry 동형 패턴)
- 별도 v2 cycle 진입 0건
- 본 v1.1 보강 시 추가 신규 자기 발견 잠재 risk 발생 시 = §10 자기진단 추가 항목 명문 한정 (별도 cycle 0)

---

## §6 발효 효과 + 권위 한계

### §6.1 본 합의 발효 효과 (REVISE → v1.1 보강 후 발효 자격 충실)

본 합의 REVISE → brief v1.1 보강 1pass 흡수 commit 후 본 cycle 합의 발효:

1. **MVP-2 영역 진입 권한 발효** (GP-2 + G4 §4.4 Layer 4)
2. **(β) sub-수단 결정 cycle 진입 자격 발효** (R-1~R-5 + L-1~L-5)
3. **(γ) 분리 영역 결정 cycle 진입 자격 발효** (Layer 1+2 의존 vs Layer 4 동시)
4. **Rollback Trigger 본문 *후보 채택*** (구현 발효 ≠ 본 합의, 별도 sub-cycle)
5. **Evidence 형식 본문 *후보 채택*** (구현 발효 ≠ 본 합의)

### §6.2 본 합의 발효 *하지 않는* 영역 (17/17 답습)

§0 답습 (17 원칙 준수 항목) + 본 합의 추가:

- ❌ MVP-2 Implementation Evidence PASS 발효 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도)
- ❌ R-S1 cross-reference 정정 cycle 자동 진입 (별도 사용자 명시 영역, §4.3 답습)
- ❌ 51 audit brief carry-over 결함 정정 자동 진입 (별도 cross-reference 정정 cycle)
- ❌ Hermes upstream `agent/redact.py` 본 repo 내 import 결정 (별도 합의)

---

## §7 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 합의 REVISE → 다음 단계 순서 (단계별 합의 cycle 답습):

1. **brief v1.1 1pass 흡수 보강** (Claude 영역, BLOCKING 7 + 권고 13 흡수 — §5 답습)
2. **SESSION + INDEX commit + push (52 entry)** (사용자 명시 commit 의무)
3. **본 cycle 합의 발효** (v1.1 commit 후 자동 — REVISE → APPROVE WITH CONDITIONS 격상)
4. **(다음 cycle, 별도 영역, 사용자 명시 시점)**:
   - **(β)** sub-수단 결정 cycle (R-1~R-5 + L-1~L-5)
   - **(γ)** 분리 영역 결정 cycle (Layer 1+2 의존 vs Layer 4 동시)
   - **R-S1 cross-reference 정정 cycle** (ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시)
   - 실 구현 sub-cycle (수단별 차등 합의 형태)

본 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §8 메타 편향 자기진단 (Reviewer 통합)

| # | 잠재 편향 | 본 합의 처리 |
|---|--------|----------|
| M-1 | Reviewer + 3 Agent = 모두 Anthropic Claude vendor → cross-vendor blind 의문 | codex (OpenAI) 1+ 응답 통합 + cross-vendor 형식 충족 (헌법 5조-2). 추가 cross-vendor (Gemini 등) 권고는 N-C-4 영역 (사용자 영역 후속 cycle) |
| M-2 | "REVISE" 판정이 풀 3+1 절차 ceremony-inflation 회피 자격 위협 | 24 entry codex 답습 동형 판정 (codex `REVISE AS ENTRY BRIEF INPUT` 직접 답습). v1.1 1pass 흡수 = ceremony-inflation 차단 답습 충실 (별도 v2 cycle 0) |
| M-3 | BLOCKING 7건 = 24 entry 답습 (7건) 동형 → "절차적 답습" 위험 | §1.1 4 source cross-validation 매트릭스 = 발견 영역별 source 분포 명시 (Consensus 2 + Unique 5 = source 다양성 검증). M-2 답습 |
| M-4 | Agent A filesystem 직접 inspection 의존 → 본 repo 상태 즉시 변경 시 evidence 변질 | §1.3 P-2~P-4 = filesystem 직접 inspection evidence 명시 + 본 합의 시점 (2026-05-28) state 답습. 본 cycle scope 內 변경 0 (실 코드 0 답습) |
| M-5 | R-S1 = 24 entry R-S1 답습 동형 패턴 → "절차적 답습" 위험 | §4 verbatim 직접 read evidence (Reviewer 단독 verify + 4 source verbatim cross-confirm = 5 source) + ADR-012 *자체 내부* divergence 명문 (24 entry 답습 외 발견 영역) |
| M-6 | Reviewer 가 자체 brief v1 작성자와 동일 LLM (Opus 4.7) → 편향 위험 | §1.4 cross-vendor blind 충족 + 본 §8 자기진단 + brief v1 §10 자기진단 7 항목 다층 답습 |
| M-7 | 본 합의 REVISE → 자동 v1.1 보강 진입 위험 (단계별 cycle 답습 위반 위험) | §7 명시 = brief v1.1 보강 (Claude 영역, BLOCKING + 권고 흡수) → commit + push (사용자 명시) → 본 cycle 합의 발효. 자동 (β)/(γ)/실 구현 진입 0건 |

---

**본 합의 보고서 v1 끝.**

**다음 단계**: brief v1.1 1pass 흡수 보강 (Claude 영역, §5 답습) → SESSION + INDEX commit + push (52 entry, 사용자 명시 commit 의무) → 본 cycle 합의 발효 (자동 격상).
