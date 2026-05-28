OpenAI Codex v0.128.0 (research preview)
--------
workdir: /home/delangi/문서/project/category/AI_development_tool
model: gpt-5.5
provider: openai
approval: never
sandbox: danger-full-access
reasoning effort: none
reasoning summaries: none
session id: 019e6c51-b115-7091-9873-6a7e261b8ba5
--------
user
당신은 외부 LLM 검토자 (cross-vendor blind review)입니다. 본 평가의 vendor = OpenAI (codex CLI), 본 cycle 의 풀 3+1 Agent vendor = Anthropic Claude. cross-vendor 충족 (헌법 5조-2 Provider Liquidity 비협상).

## 본 cycle 개요

AI_development_tool 프로젝트 (SDD + TDD 방법론, 한국어 소통). 본 cycle = **(γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 brief** (52 entry MVP-2 (α) 진입 합의 발효 후 carry-over 5번). 본 cycle = **4 대안 (γ-a/b/c/d) 中 채택 결정 cycle** (수단 결정 0, sub-수단 결정 = (β) 별도 cycle).

본 cycle 발효 효과:
- (γ) 4 대안 中 채택 결정 발효 + 후속 sub-cycle (Layer 1+2 PASS 격상 또는 동시 진입) 진입 자격 발효
- Rollback Trigger / Evidence 후보 채택 (구현 발효 ≠ 본 합의)

본 cycle 발효 *하지 않는 것*: 실 코드 0 / G4 §4.4 Layer sub-수단 결정 (L-1~L-5) 0 / GP-2 sub-수단 결정 (R-1~R-5) 0 / W 통합 결정 (W-A~E) 0 / MVP-2 Implementation Evidence PASS 발효 0 (총 27 금지 사항).

## 4 대안 (γ-a/b/c/d) 답습

- **(γ-a)** Layer 1+2 의존 영역 우선 진입 → Layer 4 후속 (단계적, 안전)
- **(γ-b)** Layer 4 단독 진입 (Layer 1+2 = 의존 영역 자동 동시)
- **(γ-c)** Layer 1+2+4 동시 진입 (defense-in-depth)
- **(γ-d)** Layer 4 단독 + Layer 1+2 = 별도 cycle 분리 (52 entry framing) — ⚠️ **모순 risk** (Layer 4 = Layer 1+2 의 회귀 검증 → Layer 1+2 미발효 시 회귀 대상 부재)

본 brief 권고 (수단 결정 0, 후보 비교만): **(γ-c) 1순위 + (γ-a) 2순위**.

## 검토 대상 (working directory 자료, codex 직접 read 의무)

본 검토 대상 (PRIMARY):
- `docs/phase0/mvp2-gamma-layer-separation-brief.md` (v1, 482줄, §0~§10)

본 brief 의 직접 입력 자료 (52 entry):
- `docs/phase0/mvp2-entry-brief.md` (v1.1, 602줄, §2.2.4 + §8.1 항목 2 답습 source)
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` (257줄)
- `docs/external-review/2026-05-28-mvp2-entry-codex-response.md` (3597줄, 52 entry codex 응답)

선행 권위 (답습 source):
- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4.1 line 629~660, G4 Layer 1~5 정의)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (§2.3 + §2.8 — Layer numbering R-S1 답습)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e))

실 repo PoC 시제 (52 entry Agent A 발견, 본 cycle 답습):
- `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type)
- `tools/canonical_json.py`
- `tests/canonical/` 24 fixtures (8 카테고리 × 3)
- `.github/workflows/g4-hash-chain.yml` (10652B)
- `.github/workflows/history-anchor-verifier.yml` (19094B)
- `.github/workflows/rewrite-defense.yml` (16454B)

## 검토 의무 (7 기준)

본 brief 의 (γ) 결정 *입력* 자격을 평가:

1. **cross-vendor 충족 명시** (응답 vendor = OpenAI codex / 본 cycle 풀 3+1 Agent vendor = Anthropic Claude)

2. **본 brief v1 직접 읽기 evidence** (응답 본문 내 brief §X verbatim 인용 또는 영역 식별)

3. **4 대안 (γ-a/b/c/d) 각각 평가 정확성**:
   - (γ-a) 단계적 + 의존 chain 답습
   - (γ-b) Layer 4 단독 + Layer 1+2 자동 (evidence 분리 risk)
   - (γ-c) defense-in-depth + 동시
   - (γ-d) 모순 risk verify (Layer 4 = Layer 1+2 회귀 검증 → Layer 1+2 미발효 시 회귀 대상 부재)

4. **PoC 시제 답습 cross-check** (52 entry Agent A N-A-1 답습): 5 영역 모두 충족 (tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml). 본 brief §2.5 매트릭스 verify

5. **ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 운영조건 매트릭스 각 대안별 평가** (52 entry B-2 framing 답습)

6. **Rollback Trigger / Evidence 후보 채택 (구현 발효 ≠ 본 합의)** 평가 (52 entry N-1 답습)

7. ⚠️ **R-S1 (ADR-012 §2.3 vs §2.8) 후행 영향 (RT-γ-6) 평가** — 52 entry §9.5 답습 (별도 cycle 영역, 본 cycle 후행 영향 답습)

## 판정 형식

- **총평**: APPROVE / APPROVE WITH CONDITIONS / REVISE / REJECT
- **BLOCKING N건** (R-1, R-2, ...)
- **권고 N건** (N-1, N-2, ...)
- **NOTE N건** (필요 시)

## 응답 형식

응답 길이: ~250~400 줄. 한국어 + 영문 기술 용어 혼용 가능. Markdown 형식.

응답 구조:
- 검토자 / Vendor
- 직접 검토한 working directory 자료 (path 목록)
- §0 총평
- §1 BLOCKING N건
- §2 권고 N건
- §3 NOTE N건 (필요 시)
- §4 4 대안별 평가 ((γ-a/b/c/d))
- §5 (γ-d) 모순 risk verify 결과
- §6 권고 매트릭스 (수단 결정 ≠ 본 검토, 후보 비교만)

codex
요청하신 형식에 맞춰 실제 파일을 읽고 검토하겠습니다. 먼저 primary brief와 근거 문서의 관련 구간, PoC 파일 존재와 내용을 병렬로 확인합니다.
exec
/bin/bash -lc "sed -n '220,520p' docs/phase0/mvp2-gamma-layer-separation-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
#### §2.4.4 (γ-d) 채택 시 framing 모순 risk

본 (γ-d) = 52 entry brief framing 자체이지만, 의존 chain 분석 시 **모순 risk**:
- Layer 4 = "Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증" (G4 §4.4.1 line 650 verbatim)
- Layer 1+2 미발효 시 Layer 4 회귀 검증 *대상 부재*
- → (γ-d) 채택 시 Layer 1+2 PASS 격상 = Layer 4 PASS 발효 *선행 의무* 영역

→ **(γ-d) = 사실상 (γ-a) 와 동등** (시점 차이 한정). 본 cycle 평가 영역.

### §2.5 PoC 시제 답습 cross-check (52 entry Agent A N-A-1 + B-6 답습)

본 cycle 시점 PoC 시제 상태 (실 repo `tools/` + `tests/canonical/` + `.github/workflows/`):

| 영역 | PoC 시제 (현 상태) | PASS 시제 (격상 영역) |
|------|--------------|-------------------|
| Layer 1 (hash chain) | ✅ `tools/jsonl_hash_chain.py` (genesis hash 함수 + 4 violation_type) | PASS 격상 = R-6 workflow 답습 통합 + actual run PASS evidence |
| Layer 2 (Git append-only) | ✅ branch protection rule (43 entry 8 contexts 답습) + denyNonFastForwards (PoC 시제 가능) | PASS 격상 = base branch 대비 JSONL line deletion / rewrite 감지 CI step |
| canonical JSON test corpus | ✅ `tests/canonical/` 24 fixtures (8 카테고리 × 3 = RFC 8785 reference ≥ 20 충족) | PASS 격상 = CI step 內 reference 동등성 검증 + 위반 BLOCK |
| genesis hash (첫 entry) | ✅ `tools/jsonl_hash_chain.py` 內 genesis hash 함수 | PASS 격상 = 실 ledger 첫 entry 작성 + audit log |
| Layer 4 (CI 회귀 검증) | ✅ `.github/workflows/g4-hash-chain.yml` (10652B) PoC 시제 운영 | PASS 격상 = R-6 답습 통합 또는 단독 PASS 격상 + actual run PASS |

→ **모든 영역 PoC 시제 충족 (이미 운영 中)**. PASS 격상 = 본 (γ) 결정 후 후속 sub-cycle 영역.

### §2.6 (γ) 4 대안 권고 매트릭스 (수단 결정 0, 후보 비교만)

| 대안 | 의존 chain 답습 | 합의 cycle 수 | ceremony-inflation | PASS 발효 시점 | Layer 1+2 evidence 분리 | 본 brief 권고 |
|------|------------|------------|-----|--------------|----------------|----------|
| (γ-a) Layer 1+2 우선 → Layer 4 후속 | ✅ 답습 충실 | 2+ cycle | ⚠️ 다층 | 단계적 | ✅ 명시 분리 | ✅ **권고 (1)** — 안전 + 의존 답습 |
| (γ-b) Layer 4 단독 (Layer 1+2 자동) | ✅ 답습 (자동) | 1 cycle | ✅ 차단 | 동시 | ⚠️ 통합 risk | 권고 (3) |
| (γ-c) Layer 1+2+4 동시 (defense-in-depth) | ✅ 답습 충실 | 1 cycle (큰 영역) | ✅ 차단 | 동시 | ✅ 명시 분리 | ✅ **권고 (2)** — defense-in-depth + 효율 |
| (γ-d) Layer 4 단독 + Layer 1+2 별도 | ⚠️ 모순 risk (§2.4.3) | 2+ cycle | ⚠️ 다층 | Layer 4 우선 (의존 모순) | ✅ 분리 (사실상 (γ-a) 동등) | ⚠️ 비권고 (모순 risk) |

→ **본 brief 권고 (수단 *결정* 0, 후보 비교만)**: **(γ-c) Layer 1+2+4 동시 (defense-in-depth)** 1순위 + **(γ-a) Layer 1+2 우선 → Layer 4 후속** 2순위. 본 결정 = 풀 3+1 합의 + 사용자 명시 영역.

---

## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 — 5조건 매트릭스 (각 대안별)

본 §3 = 52 entry brief §3 답습 (ADR-011 §2.1 framing 정정 답습).

| # | 조건 | (γ-a) | (γ-b) | (γ-c) | (γ-d) |
|---|------|------|------|------|------|
| (a) | 동등 이상 보안 결과 | Layer 1+2 PASS 발효 + Layer 4 PASS 발효 (단계적 evidence) | Layer 4 PASS 발효 (Layer 1+2 자동 의존 통합 evidence) | Layer 1+2+4 동시 PASS evidence (분리 명시) | Layer 4 PASS 발효 (Layer 1+2 미발효 시 모순) |
| (b) | 격리 환경 PoC 실증 | ✅ PoC 시제 충족 (모든 영역) | ✅ 동일 | ✅ 동일 | ✅ 동일 |
| (c) | ADR / SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.8 (5-layer) | ✅ 동일 | ✅ 동일 | ⚠️ Layer 4 단독 + Layer 1+2 부재 시 ADR-012 §2.3 다층 강제 답습 미충족 |
| (d) | 자동 회귀 검증 경로 확보 | R-6 workflow 답습 확장 (단계적) | R-6 답습 (1 cycle 통합) | R-6 답습 (각 layer step 분리) | R-6 답습 (Layer 4 한정, Layer 1+2 부재 시 회귀 *대상* 부재 모순) |
| (e) | 합의 APPROVE | 단계별 합의 N회 | 1 합의 (풀 3+1 + 외부 LLM 1+) | 1 합의 (큰 영역, 풀 3+1 + 외부 LLM 1+) | 2+ 합의 + 모순 risk |

→ **(γ-c) + (γ-a) = 5조건 모두 충족 자격 정합**. (γ-b) = (c)+(d) Layer 1+2 evidence 분리 risk. (γ-d) = (c)+(d) 모순 risk.

---

## §4 합의 형태 + 풀 3+1 승격 트리거 검증

### §4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ 권고 (52 entry §4.2 답습)

**합의 형태 권고**: **풀 3+1 + 외부 LLM 1+ (cross-vendor 권고, 사용자 영역 결정)**

**정당화 출처**:
1. 52 entry brief §8.1 항목 2 — "(γ) 분리 영역 결정 = 풀 3+1" 권고 직접 답습
2. 52 entry brief §4.2 — "G4 §4.4 Layer 4 발효 시점 합의 형태 권고 = (γ) 분리 영역 결정 = 풀 3+1" 답습
3. 헌법 5조-2 Provider Liquidity (비협상) — cross-vendor 검증 권고 (사용자 영역)
4. ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 운영조건 + §2.4 T3 영역 답습 — 큰 결정 영역
5. roadmap.md §5.4 그룹 C 답습 (G4 §4.4 영역 = 단축 합의 + PoC evidence 권고) vs 본 cycle = 풀 3+1 격상 (52 entry brief §1.3 항목 5 답습, B-7 흡수)

**외부 LLM 1+ 자격 옵션** (사용자 영역 결정):
- **(α) Claude tmux + codex bypass sandbox 직접 호출** (24/52 entry 답습)
- **(β) 사용자 직접 외부 LLM 호출** (codex + Gemini 등 추가 cross-vendor 가능)
- **(γ) 외부 LLM 0** (풀 3+1만, 작은 영역 결정 시점) — 본 cycle 평가 영역

### §4.2 본 (γ) cycle 발효 효과 (4 대안 中 채택 결정 발효)

본 (γ) 합의 APPROVE 시 발효:

1. **(γ-a/b/c/d) 4 대안 中 채택 결정 발효** (사용자 명시 + 풀 3+1 합의)
2. **후속 sub-cycle 진입 자격 발효**:
   - (γ-a) 채택 시 = Layer 1+2 PASS 격상 cycle (1차) + Layer 4 PASS 격상 cycle (2차)
   - (γ-b) 채택 시 = Layer 1+2+4 통합 PASS 격상 cycle (1 cycle, Layer 4 evidence 內 합산)
   - (γ-c) 채택 시 = Layer 1+2+4 통합 PASS 격상 cycle (1 cycle, 각 layer evidence 분리)
   - (γ-d) 채택 시 = Layer 4 단독 cycle + Layer 1+2 별도 cycle (모순 risk 처리)
3. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의, 52 entry N-1 답습)

### §4.3 7 풀 3+1 승격 트리거 검증 (본 (γ) cycle 자체)

| # | trigger | 본 (γ) 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (영역 결정 / 수단 결정 / threshold 고정) | ✅ **발화** | (γ) 4 대안 中 채택 결정 = MVP-2 Implementation Evidence PASS 발효 *시점/방식* 결정 (큰 영역) |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일, 본문 변경 0 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | R-S1 (ADR-012 §2.3 vs §2.8) = 52 entry 발견 + 별도 cross-reference 정정 cycle 답습 (본 cycle scope 외) |
| 5 | 외부 LLM 응답 통합 필요성 | ⚠️ **부분 발화 (사용자 영역 결정)** | (γ) 결정 = 큰 영역, cross-vendor 외부 LLM 권고. 단, 작은 영역 결정 시 외부 LLM 0 가능 |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #12 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 #16 명시 금지 |

→ **1/7 발화 + 1 부분 발화** → **풀 3+1 + 외부 LLM 1+ 권고 (사용자 영역 결정 자격, 외부 LLM 0 시 풀 3+1만 적격)**.

---

## §5 Rollback Trigger / Evidence *후보 채택* (52 entry N-1 답습)

### §5.1 (γ) 채택 결정 후 Rollback Trigger 후보

| # | Trigger | 영역 | 발화 조건 | 권위 답습 |
|---|---------|----|---------|---------|
| RT-γ-1 | (γ) 채택 결정 후 Layer 1+2 PoC 시제 회귀 | 모든 (γ) 대안 | tools/jsonl_hash_chain.py / canonical_json.py / tests/canonical/ 본문 변경 시 PoC 시제 미작동 | 본 brief §2.5 답습 (PoC 시제 답습 보존 의무) |
| RT-γ-2 | (γ-a) 채택 시 Layer 1+2 PASS 발효 지연 | (γ-a) | 합의 cycle N회 지연 → Layer 4 PASS 발효 대기 → MVP-2 Implementation Evidence PASS 발효 시점 지연 | (γ-a) 시간 부담 답습 (§2.1.3) |
| RT-γ-3 | (γ-b) 채택 시 Layer 1+2 evidence 분리 미명확 | (γ-b) | Layer 4 evidence 內 Layer 1+2 evidence 합산 → 회귀 영역 미식별 risk | (γ-b) 단점 답습 (§2.2.3) |
| RT-γ-4 | (γ-c) 채택 시 합의 부담 ↑ → 합의 cycle 지연 | (γ-c) | 큰 합의 영역 (Layer 1+2+4 통합 + 각 layer evidence 분리) | (γ-c) 단점 답습 (§2.3.3) |
| RT-γ-5 | (γ-d) 채택 시 의존 chain 모순 발화 | (γ-d) | Layer 4 PASS 발효 + Layer 1+2 미발효 → 회귀 검증 *대상 부재* | (γ-d) 모순 risk 답습 (§2.4.3) |
| RT-γ-6 | R-S1 cross-reference 정정 후행 영향 | 모든 (γ) | ADR-012 §2.3 본문 정정 시 (γ) 결정 영향 (예: Layer 4 numbering 변경 시 본 cycle 결정 영역 변경) | 52 entry §9.5 답습 (R-S1 정정 cycle 별도, 본 cycle 후행 영향 답습) |

### §5.2 Evidence Required (구현 발효 ≠ 본 합의)

본 (γ) 합의 발효 시 Evidence:

| # | Evidence | 출처 |
|---|---------|------|
| E-γ-1 | (γ) 4 대안 中 채택 결정 합의 보고서 | 본 cycle Reviewer 통합 합의 |
| E-γ-2 | PoC 시제 답습 cross-check evidence | 본 brief §2.5 답습 (실 repo 답습 매트릭스) |
| E-γ-3 | 외부 LLM 1+ 응답 (사용자 영역 결정 시) | `docs/external-review/2026-05-28-mvp2-gamma-*.md` (사용자 영역) |
| E-γ-4 | 후속 sub-cycle 진입 자격 발효 명문 | 본 cycle commit + push 후 자동 (§4.2 답습) |

후속 sub-cycle 시점 Evidence (실 구현 sub-cycle 영역):
- Layer 1+2 PASS 격상 evidence (Docker 격리 PoC + R-6 actual run PASS)
- Layer 4 PASS 격상 evidence (Docker 격리 PoC + R-6 actual run PASS + canonical 위반 + timestamp monotonicity)
- MVP-2 Implementation Evidence PASS 발효 합의 (별도)

---

## §6 금지 사항

### §6.1 본 brief 자체 금지 사항

§0.3 답습 (27 항목 재명시 생략).

### §6.2 본 brief 발효 *후* 후속 cycle 진입 시점 금지 사항

본 (γ) 합의 APPROVE 후:

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 후속 sub-cycle 진입 (Layer 1+2 PASS 격상 / Layer 4 PASS 격상 / 통합) | 사용자 명시 의무 |
| 2 | 자동 (β) sub-수단 결정 cycle 진입 (L-1~L-5 / W-A~E) | 사용자 명시 의무 |
| 3 | 자동 실 구현 sub-cycle 진입 | 사용자 명시 의무 |
| 4 | MVP-2 Implementation Evidence PASS *자동* 선언 | 실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 (별도 합의) |
| 5 | 외부 library (`pyjcs` / `rfc8785`) 자동 도입 | L-5 별도 cycle |
| 6 | G4 §4.4 Layer 3 (Signed commit) / Layer 5 (External anchor) 영역 자동 진입 | 별도 cycle |
| 7 | GP-2 sub-수단 결정 자동 진입 (R-1~R-5) | (β) 별도 cycle |
| 8 | branch protection contexts 자동 추가 | 사용자 admin scope 영역 |
| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 |
| 10 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle 사용자 명시 |

---

## §7 외부 LLM 응답 요구 영역 (사용자 영역)

### §7.1 외부 LLM 1+ 권고 출처

1. 52 entry brief §8.1 + §4.2 — "(γ) 분리 영역 결정 = 풀 3+1" 권고
2. 헌법 5조-2 Provider Liquidity (비협상)
3. ADR-011 §2.1 (a)~(d) + (e) + §2.4 T3 영역 — 큰 결정 영역

### §7.2 외부 LLM 자격 옵션 (사용자 영역 결정)

| 옵션 | 영역 | 합의 형태 |
|------|----|---------|
| **(α) Claude tmux + codex bypass sandbox 직접 호출** | 24/52 entry 답습 | 풀 3+1 + 외부 LLM 1+ (cross-vendor) |
| **(β) 사용자 직접 외부 LLM 호출** (codex + Gemini 등 추가) | 24 entry 외 옵션 | 풀 3+1 + 외부 LLM 2+ (cross-vendor 강화) |
| **(γ) 외부 LLM 0** (풀 3+1만, 작은 영역 결정) | 1-Agent + Reviewer 또는 풀 3+1만 | 작은 영역 결정 시점 |

### §7.3 외부 LLM 응답 *입력 자료* (호출 시점)

| 필수 입력 | 자료 위치 |
|---------|---------|
| 본 (γ) brief v1 | `docs/phase0/mvp2-gamma-layer-separation-brief.md` |
| 52 entry (α) brief v1.1 (입력 자료) | `docs/phase0/mvp2-entry-brief.md` |
| 52 entry Reviewer 통합 합의 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
| 51 entry audit brief | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` |
| `provider-agnostic-memory-skill-design.md §4.4.1` (Layer 1~5) | 답습 source |
| `ADR-012 §2.3 + §2.8` (Layer numbering R-S1) | 답습 source |
| `ADR-011 §2.1 (a)~(d) + §3` | 답습 source |

---

## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

### §8.1 본 brief 발효 *후* (= 본 cycle 합의 APPROVE 시점) 다음 단계

본 (γ) 합의 APPROVE 발효 후 (사용자 명시 의무):

1. **(β) sub-수단 결정 cycle** — R-1~R-5 (GP-2) + L-1~L-5 (G4 §4.4 Layer 4) + W-A/B/C/D/E — 풀 3+1
2. **Layer 1+2 PASS 격상 sub-cycle** ((γ-a) 또는 (γ-d) 채택 시) — 별도 합의
3. **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-b) 또는 (γ-c) 채택 시) — 큰 합의
4. **실 구현 sub-cycle** — Hermes upstream + 본 repo P1 facade + Layer 1+2+4 PoC → PASS + R-6 workflow 확장
5. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 (32 entry 답습)
6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 풀 3+1 + 사용자 명시
7. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008/012/011

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §9 답습 참조

### §9.1 상위 권위

- **헌법 제8조 (보안)** — `docs/constitution/PROJECT_CONSTITUTION.md`
- **헌법 제5조-2 (Provider Liquidity, 비협상)** — 동상
- **ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e)** — `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- **ADR-011 §2.3 (Hermes ≠ root of trust)** — 동상
- **ADR-011 §2.4 (T1/T2/T3)** — 동상

### §9.2 직접 선행 자료

- **52 entry (α) entry brief v1.1** (본 brief 의 직접 입력 자료) — `docs/phase0/mvp2-entry-brief.md`
- **52 entry Reviewer 통합 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- **52 entry codex 응답** — `docs/external-review/2026-05-28-mvp2-entry-codex-response.md`
- **51 entry audit brief** — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- **51 entry 합의 보고서** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md`
- **32 entry MVP-1 PASS 발효 합의** — `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`
- **`implementation-runtime-roadmap-mvp1.md`**
- **`governance-preconditions.md §4`**
- **`provider-agnostic-memory-skill-design.md §4.4`**
- **`ADR-012-evidence-ledger-protection.md §2.3 + §2.5 + §2.7 + §2.8 + §3.4`**

### §9.3 메타 영역

- 실 repo PoC 시제 (52 entry Agent A N-A-1 + B-6 답습):
  - `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type)
  - `tools/canonical_json.py`
  - `tests/canonical/` 24 fixtures (8 카테고리 × 3 = RFC 8785 reference ≥ 20)
  - `.github/workflows/g4-hash-chain.yml` (10652B)
  - `.github/workflows/history-anchor-verifier.yml` (19094B)
  - `.github/workflows/rewrite-defense.yml` (16454B)

### §9.4 본 brief 발효 후 cross-reference 갱신 영역

- (γ-a/c) 채택 시 = Layer 1+2 PASS 격상 + Layer 4 PASS 격상 evidence cross-reference
- (γ-b) 채택 시 = Layer 1+2+4 통합 evidence cross-reference (Layer 4 evidence 內 분리 명시)
- (γ-d) 채택 시 = Layer 4 단독 + Layer 1+2 별도 cycle cross-reference (모순 risk 처리 영역)
- R-S1 cross-reference 정정 영역 (52 entry §9.5 답습, 본 cycle scope 외)

---

## §10 본 brief v1 작성 자격 자기진단

본 brief 작성자 (Claude Opus 4.7) 의 자기 발견 잠재 위험:

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 brief 가 (γ) 특정 대안 (γ-c) 권고 방향으로 편향 | §0.3 + §6.2 27+10 금지 사항 + §2.6 권고 매트릭스 = 후보 비교만, "수단 *결정* = 풀 3+1 합의 + 사용자 명시" 영구 분리 (§0.4) |
| P-2 | (γ-d) 모순 risk 발견이 본 brief 자체에서 결정 무단 침입 | §2.4.4 = "본 cycle 평가 영역" 명시 ((γ-d) 채택 시 후속 sub-cycle 영역 평가, 본 brief = 후보 비교만) |
| P-3 | 52 entry framing ((γ-d) 현 framing) 단방향 답습 — framing 자체 결함 시 본 brief cascade | §2.4 (γ-d) 단점 명시 + §2.6 비권고 명시 (의존 chain 모순 risk) — 본 brief = framing 정정 영역 (52 entry framing 답습 한정) |
| P-4 | R-S1 cross-reference 정정 후행 영향 (RT-γ-6) 가 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습, 본 cycle = 4 대안 결정 한정 |
| P-5 | PoC 시제 답습 발견 (§2.5) 이 본 cycle 결정 단순화 위험 (PASS 격상 = 단순) | §2.5 = "PoC 시제 충족 / PASS 시제 미충족 격상" 답습 명시 + §5.1 RT-γ-1 (PoC 시제 회귀 risk) 답습 |
| P-6 | 외부 LLM 1+ 권고가 사용자 영역 침입 위험 | §7.2 자격 옵션 3 (사용자 영역 결정) + §4.3 trigger (5) "부분 발화" 명시 |
| P-7 | 본 brief 작성자 = 52 entry brief 작성자 (Claude Opus 4.7) → 답습 cascade risk | §1.3 선차 변경 매트릭스 명시 + §2.4 (γ-d) 모순 risk 발견 (52 entry framing 답습 한정) + Reviewer 통합 합의 시 cross-check 영역 (Agent A/B/C 3 병렬 독립 + 외부 LLM 검증) |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 + 외부 LLM 자격 옵션 결정 (§7.2) → 합의 진입 (풀 3+1 ± 외부 LLM 1+) → brief v1.1 1pass 흡수 → SESSION + INDEX commit + push (53 entry).

exec
/bin/bash -lc "sed -n '1,220p' docs/phase0/mvp2-gamma-layer-separation-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# (γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 brief (v1)

> **작성**: 2026-05-28 (53번째 entry 진입 cycle)
>
> **scope**: G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 결정 — 4 대안 (γ-a/b/c/d) 中 채택
>
> **본 cycle = 큰 cycle** (52 entry (α) 발효 후 carry-over 5번, 풀 3+1 ± 외부 LLM 1+)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + (외부 LLM 1+ 사용자 영역) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = (γ) 4 대안 中 채택 결정 발효 + 후속 sub-cycle (Layer 1+2 PASS 격상 또는 동시 진입) 진입 자격 발효

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 52 entry, commit `c739c53`)

52 entry `mvp2-entry-brief.md` (v1.1) §8.1 다음 단계:
- (α) ✅ **52 entry 발효** (REVISE → v1.1 commit 후 본 cycle 합의 발효, `c739c53` push)
- (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 + W-A/B/C/D/E — 별도 합의
- **(γ) 분리 영역 결정 cycle — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (4 대안 (γ-a/b/c/d), §2.2.4 답습) — 풀 3+1 합의**

본 (γ) cycle 진입 사용자 명시 (2026-05-28, 52 entry commit `c739c53` push 후) — "다음 carry-over 5번 (γ) 진입". 본 brief = (γ) 영역 한정. (β) + 실 구현 + MVP-2 Implementation Evidence PASS 발효 = 별도 cycle.

### §0.2 본 brief 가 *하는* 것

1. **(γ) 4 대안 정의 답습** — 52 entry brief §2.2.4 + Reviewer 합의 §6.1.3 + §8.1 답습 직접 인용 (§1)
2. **각 대안 trade-off 분석** — (γ-a) Layer 1+2 우선 / (γ-b) Layer 4 단독 / (γ-c) 동시 / (γ-d) Layer 4 단독 + Layer 1+2 별도 (§2)
3. **현 PoC 시제 답습** — 52 entry brief N-A-1 + B-6 발견 (tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ 24 fixtures + g4-hash-chain.yml PoC 시제 이미 운영) cross-check (§2.5)
4. **ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 운영조건 매트릭스 — 각 대안별** (§3, 52 entry B-2 framing 답습)
5. **본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ *권고*** (52 entry brief §4.2 답습) (§4.1)
6. **(γ) 채택 결정 발효 자격 명문** (§4.2)
7. **7 풀 3+1 승격 트리거 발화 검증** (§4.3)
8. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의, 52 entry brief N-1 답습) (§5)
9. **외부 LLM 응답 요구 영역** (사용자 영역) (§7)
10. **본 cycle 합의 발효 후 후속 sub-cycle 진입 자격 명문** (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 (Layer 1+2+4 PASS 격상 본문 모두 0건) |
| 2 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | `tests/canonical/` test corpus 본문 변경 | 0건 (24 fixtures 답습 보존) |
| 4 | `.github/workflows/g4-hash-chain.yml` / `history-anchor-verifier.yml` / `rewrite-defense.yml` 본문 변경 | 0건 (실 repo 기존 분리 운영 답습 보존) |
| 5 | `.github/workflows/r2-canary.yml` 본문 변경 | 0건 (R-6 workflow 답습 보존) |
| 6 | ledger 첫 entry (genesis hash) 작성 | 0건 (PoC 시제 답습 보존) |
| 7 | **G4 §4.4 Layer sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
| 8 | **GP-2 sub-수단 결정** (R-1 / R-2 / R-3 / R-4 / R-5 中 채택) | 0건 ((β) 별도 cycle) |
| 9 | **W 통합 결정** (W-A / W-B / W-C / W-D / W-E 中 채택) | 0건 ((β) 별도 cycle) |
| 10 | 외부 library (`pyjcs` / `rfc8785`) 도입 결정 | 0건 (L-5 별도 cycle) |
| 11 | threshold *고정* | 0건 |
| 12 | Tier-2 / Tier-3 vendor catalog 본문 확장 | 0건 |
| 13 | **MVP-2 Implementation Evidence PASS *발효*** | 0건 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도) |
| 14 | **MVP-1 PASS *재선언*** | 0건 (32 entry 답습 유지) |
| 15 | **Operational Readiness PASS** | 0건 |
| 16 | **Hermes PMO 격상** | 0건 |
| 17 | ADR 본문 갱신 (ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012) | 0건 (cross-reference 답습 한정) |
| 18 | 헌법 본문 갱신 | 0건 |
| 19 | roadmap-mvp1 본문 변경 | 0건 |
| 20 | governance-preconditions.md §4 본문 변경 | 0건 |
| 21 | provider-agnostic-memory-skill-design.md §4.4 본문 변경 | 0건 |
| 22 | `src/adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 (별도 trajectory) |
| 23 | G4 §4.4 Layer 3 (Signed commit) / Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 cycle = Layer 1+2+4 한정, Layer 3+5 = 별도 cycle 영역) |
| 24 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 | 0건 (MVP-3 ~ MVP-5 영역) |
| 25 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cross-reference 정정 cycle 사용자 명시 영역, 52 entry B-1 답습) |
| 26 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 (52 entry B-4 답습) |
| 27 | 본 brief *자체* 영구화 / 권위 chain 등재 | 0건 |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + (외부 LLM 1+ 사용자 영역 결정) + 사용자 명시 결정**
- ✅ 본 brief 발효 결과 = **(γ) 4 대안 中 채택 결정 발효** + 후속 sub-cycle (Layer 1+2 PASS 격상 또는 동시 진입) 진입 자격 발효 + Rollback Trigger / Evidence 후보 채택
- ❌ 본 brief 자체에서 sub-수단 결정 (L-1~L-5 + R-1~R-5 + W-A~E) 0건
- ❌ 본 brief 자체에서 실 구현 0건
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ❌ 본 brief 자체에서 ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건 (본 cycle = 영역 결정, 충족 evidence = 실 구현 sub-cycle 영역)
- ⚠️ 본 brief 합의 후 *자동 sub-수단 결정 / 실 구현 진입 금지* — 사용자 명시 결정 의무

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습 (52 entry + 51 entry + 32 entry)

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| `mvp2-entry-brief.md` v1.1 (52 entry, `c739c53` 발효) + Reviewer 통합 합의 (BLOCKING 7 + 권고 13 흡수) | 본 (γ) brief 의 **직접 입력 자료**. 본 cycle = 52 entry §2.2.4 + §8.1 항목 2 답습 (γ) 결정 cycle |
| 52 entry brief §2.2.4 — (γ) 4 대안 매트릭스 (N-12 흡수) | (γ-a) Layer 1+2 의존 영역 우선 → Layer 4 후속 / (γ-b) Layer 4 단독 (Layer 1+2 자동 동시) / (γ-c) Layer 1+2+4 동시 (defense-in-depth) / (γ-d) Layer 4 단독 + Layer 1+2 별도 cycle 분리 (현 framing) |
| 52 entry brief Agent A N-A-1 + B-6 — PoC 시제 이미 운영 중 발견 | tools/jsonl_hash_chain.py (genesis hash + 4 violation_type) + tools/canonical_json.py + tests/canonical/ 24 fixtures + g4-hash-chain.yml PoC 시제 충족 / PASS 시제 미충족 |
| `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의 5-layer) — 52 entry §4.4.2 R-S1 답습 PRIMARY 권위 | Layer 1 (Hash Chain MANDATORY) + Layer 2 (Git append-only MANDATORY) + Layer 3 (Signed commit RECOMMENDED MVP) + Layer 4 (CI 회귀 검증 MANDATORY) + Layer 5 (External Anchor RECOMMENDED MVP) |
| `ADR-012 §2.8 line 264~272` (5-layer 동형) — 52 entry §4.4.2 SUPPORTING 권위 | G4 동형 |
| `ADR-012 §2.3 line 165~185` (4-layer numbering) — 52 entry §4.4.2 PRINCIPLE ONLY (numbering 근거 아님) | Append-only + Hash Chain 원칙 영역 답습 한정 |
| 32 entry MVP-1 Implementation Evidence PASS *완전 발효 (α)* | MVP-2 PASS = 본 (γ) + (β) + 실 구현 + 별도 합의 후 발효 (다층 분리) |
| `ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건` (52 entry B-2 답습 정정) | 각 (γ) 대안별 5조건 매트릭스 §3 답습 |

### §1.2 (γ) 4 대안 정의 (52 entry §2.2.4 답습 verbatim)

| 대안 | 정의 | 52 entry brief framing |
|------|----|--------------------|
| **(γ-a)** | **Layer 1+2 의존 영역 우선 진입 후 Layer 4 추가** | "단계적, 안전" |
| **(γ-b)** | **Layer 4 단독 진입** (Layer 1+2 = 의존 영역 자동 동시 진입) | (자동 동시) |
| **(γ-c)** | **Layer 1+2+4 동시 진입** | "defense-in-depth 답습" |
| **(γ-d)** | **Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle 분리** | "현 brief framing" (52 entry framing) |

### §1.3 ⭐ 선차 변경 매트릭스 (52 entry framing vs 본 (γ) cycle 결정)

| 영역 | 52 entry framing | 본 (γ) cycle 결정 | 권위 정당성 |
|------|------------------|------------------|------------|
| Layer 1+2 = 의존 영역 (Layer 4 = 회귀 검증 대상) | "(γ-d) Layer 4 단독 + Layer 1+2 = 별도 cycle 분리 (현 framing)" | **본 cycle = 4 대안 中 채택 결정 (γ-a/b/c/d 中 사용자 명시 + 풀 3+1 합의)** | ✅ 정당 (52 entry brief §8.1 항목 2 답습) |
| PoC 시제 vs PASS 시제 | "PoC 시제 충족 / PASS 시제 미충족" 격상 (B-6 흡수, Agent A N-A-1 답습) | **본 cycle = PoC 시제 답습 보존 + PASS 시제 격상 영역 결정** | ✅ 정당 |
| 합의 형태 | 풀 3+1 (52 entry §8.1 항목 2) + 외부 LLM 1+ 권고 영역 | **풀 3+1 + 외부 LLM 1+ 권고 (사용자 영역 결정)** | ✅ 정당 (52 entry 답습 + cross-vendor 의무 권고) |

---

## §2 4 대안 분석

### §2.1 (γ-a) Layer 1+2 의존 영역 우선 진입 후 Layer 4 후속

#### §2.1.1 영역 정의

| 항목 | 내용 |
|------|------|
| **순서** | (1) Layer 1 (hash chain) PoC → PASS 격상 + (2) Layer 2 (Git append-only) PoC → PASS 격상 + (3) canonical JSON test corpus PoC → PASS + (4) genesis hash 첫 entry → (5) Layer 4 (CI 회귀 검증) PASS 격상 후속 |
| **합의 cycle 수** | 최소 2 cycle (Layer 1+2 합의 + Layer 4 합의) 또는 단계별 multi-cycle |
| **PASS 발효 시점** | Layer 1+2 PASS 발효 후 Layer 4 PASS 발효 (단계적) |

#### §2.1.2 장점

- ✅ 의존 chain 정확 답습 (Layer 4 = Layer 1+2 의 회귀 검증 → Layer 1+2 PASS 부재 시 Layer 4 의미 부재)
- ✅ 단계적 안전 (Layer 1+2 실 구현 risk 분리 + Layer 4 회귀 검증 영역 분리)
- ✅ 합의 부담 분산 (각 layer 별 작은 합의 영역)
- ✅ 별도 검증 분리 (Layer 1+2 evidence + Layer 4 evidence 분리 명확)

#### §2.1.3 단점

- ⚠️ 시간 부담 (합의 cycle N회, 각 cycle 별 brief + 합의 + commit + push)
- ⚠️ ceremony-inflation risk (각 layer 별 cycle = ceremony 다층)
- ⚠️ Layer 4 진입 지연 (Layer 1+2 PASS 발효까지 대기)

#### §2.1.4 PoC 시제 답습

PoC 시제 = 이미 충족 (tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml). PASS 격상만 필요 → (γ-a) 시점 cycle 부담 = "PASS 격상 합의 + evidence" 한정 (실 구현 부담 ↓).

### §2.2 (γ-b) Layer 4 단독 진입 (Layer 1+2 = 자동 의존 영역 동시 진입)

#### §2.2.1 영역 정의

| 항목 | 내용 |
|------|------|
| **순서** | Layer 4 (CI 회귀 검증) 합의 cycle 진입 → Layer 1+2 의존 영역 *자동* 동시 진입 (의존 chain 답습) → 한 cycle 內 모두 진입 |
| **합의 cycle 수** | 1 cycle (Layer 4 단독, 의존 영역 자동 포함) |
| **PASS 발효 시점** | Layer 1+2+4 동시 발효 (단일 합의) |

#### §2.2.2 장점

- ✅ 단순 (1 cycle 진입, 의존 영역 자동)
- ✅ 시간 효율 (Layer 4 합의 cycle 1회로 모든 영역)
- ✅ ceremony-inflation 차단 (다층 cycle 회피)

#### §2.2.3 단점

- ⚠️ Layer 1+2 separate scope 미인식 위험 (Layer 1+2 = "의존 영역" 단순 표기 → 실 구현 + evidence 분리 미명시 risk)
- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 합의 = 큰 영역, 풀 3+1 + 외부 LLM 1+ + 사용자 명시)
- ⚠️ Layer 1+2 evidence 분리 미명확 (Layer 4 evidence 內 합산 risk)

#### §2.2.4 PoC 시제 답습

PoC 시제 답습 자동 (Layer 1+2 PoC 시제 + Layer 4 PoC 시제 = 모두 충족). PASS 격상 영역 = Layer 1+2+4 통합.

### §2.3 (γ-c) Layer 1+2+4 동시 진입 (defense-in-depth)

#### §2.3.1 영역 정의

| 항목 | 내용 |
|------|------|
| **순서** | Layer 1+2+4 동시 합의 cycle 진입 — defense-in-depth 답습 (각 layer 명시 진입 자격) |
| **합의 cycle 수** | 1 cycle (Layer 1+2+4 통합) — (γ-b) 와 형식 유사하지만 각 layer evidence 분리 명시 |
| **PASS 발효 시점** | Layer 1+2+4 동시 발효 |

#### §2.3.2 장점

- ✅ defense-in-depth 답습 (ADR-012 §2.3 다층 강제 + G4 §4.4.1 5-layer 답습 충실)
- ✅ 각 layer evidence 명시 분리 ((γ-b) 와 차이)
- ✅ 통합 합의 효율 + Layer evidence 분리 동시 충족
- ✅ MVP-2 Implementation Evidence PASS 발효 시점 = (a)~(d) 4조건 모두 layer 별 명시 evidence

#### §2.3.3 단점

- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 + 각 layer evidence 분리 = 큰 영역)
- ⚠️ 외부 LLM 1+ + 사용자 명시 부담 (큰 합의)

#### §2.3.4 PoC 시제 답습

(γ-b) 동형 — PoC 시제 충족 자동, PASS 격상 = Layer 1+2+4 통합 동시.

### §2.4 (γ-d) Layer 4 단독 + Layer 1+2 = 별도 cycle 분리 (52 entry framing)

#### §2.4.1 영역 정의

| 항목 | 내용 |
|------|------|
| **순서** | Layer 4 단독 합의 cycle 진입 (Layer 4 evidence 만) + Layer 1+2 = 별도 cycle 분리 (시점 미정) |
| **합의 cycle 수** | 2+ cycle (Layer 4 단독 + Layer 1+2 별도, 각각 사용자 명시) |
| **PASS 발효 시점** | Layer 4 PASS 발효 (Layer 1+2 미발효 또는 후속) |

#### §2.4.2 장점

- ✅ 본격 분리 (Layer 4 = CI 회귀 검증, Layer 1+2 = ledger 무결성 layer — *독립 영역* framing)
- ✅ Layer 4 진입 즉시 가능 (Layer 1+2 PASS 대기 0)
- ✅ Layer 1+2 영역 별도 평가 (Layer 1+2 PASS 격상 = MVP-2 또는 MVP-3 영역 결정 자유)

#### §2.4.3 단점

- ⚠️ 의존 chain 모순 (Layer 4 = Layer 1+2 의 회귀 검증 → Layer 1+2 PASS 부재 시 Layer 4 의미 부재)
- ⚠️ PASS 발효 자체 모순 (Layer 4 PASS 발효 = Layer 1+2 PASS 답습 의무 → 별도 cycle 의무)
- ⚠️ ADR-012 §2.3 + §2.8 다층 강제 답습 미충족 (Layer 1+2 부재 시 Layer 4 단독 의미 부재)

#### §2.4.4 (γ-d) 채택 시 framing 모순 risk

exec
/bin/bash -lc "sed -n '1,220p' docs/decisions/ADR-011-means-vs-ends-redaction.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)

**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
**날짜**: 2026-05-06
**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거

---

## 1. 맥락 (Context)

### 1.1 P2 v2 가정의 붕괴

ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.

Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).

### 1.2 Phase 0 R-1 / R-2 evidence

- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
  - redact 모듈 import 25개 모두 비-DB 경로
  - `hermes_state.py` (SessionDB) redact import 0건

- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.

### 1.3 ADR 권위 해석 요청 사항

위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:

> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**

본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
- G1a/G1b 게이트 분리 공식화
- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
- 자동 학습 vs 자동 정책 변경 분리

---

## 2. 결정 (Decision)

본 ADR은 다음 4가지를 권위로 선언한다.

### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)

**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**

- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:

  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.

### 2.2 G1a / G1b 게이트 분리 공식화

P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   Evidence: agent/redact.py docstring "for logs and tool output",
             redact import 25개 모두 비-DB,
             hermes_state.py redact import 0건
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
             + 6항목 자동 검증 (C1~C6 모두 PASS)
   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
```

#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)

| # | 조건 | 산출 |
|---|------|------|
| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |

R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.

### 2.3 Hermes ≠ Root of Trust

**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**

#### 권위 위계 (Authority Hierarchy)

```
Constitution
  > ADR
  > SDD
  > Harness Gates
  > Hermes
  > Worker Agents
```

#### 운영 함의 (Operational Implications)

1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.

#### prequel과의 관계

본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.

### 2.4 자동 학습과 자동 정책 변경 분리

- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.

#### 3-tier 분류 (T1 / T2 / T3)

| Tier | 정의 | 예시 | 승인 경로 |
|------|------|------|---------|
| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |

본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.

---

## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)

본 ADR은 다음 후속 작업의 권위 근거로 기능한다.

| 작업 | 산출 | 본 ADR §과의 관계 |
|------|------|----------------|
| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |

후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.

---

## 4. 선택지 (Options Considered)

### 옵션 A: ADR-011 단독 (Amendment 없음)

- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.

### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)

- 장점: ADR-008 한 문서로 일관
- 단점:
  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)

### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**

- 장점:
  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
- 단점: 작성 분량 2배 (수용)

---

## 5. 근거 (Rationale)

### 5.1 헌법 제8조 본질 재해석의 정당성

헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.

수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.

### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성

system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.

### 5.3 G1a/G1b 분리의 영구화 필요성

R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.

### 5.4 단축 합의(Reviewer-only)의 정당성

본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.

---

## 6. 합의 결과 (단축 합의 — Reviewer-only)

세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`

| 차원 | 판정 | 핵심 근거 |
|------|------|---------|
| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |

---

## 7. 결과 (Consequences)

### 7.1 긍정적


exec
/bin/bash -lc "sed -n '600,690p' docs/architecture/provider-agnostic-memory-skill-design.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
| `ts` | ISO 8601 | ✅ | entry 생성 timestamp + **monotonicity 의무** (본 entry `ts` ≥ `prev_hash` entry `ts`, ADR-012 §3.4) |
| `agent` | string | ✅ | provider-neutral identifier (`user` / `<worker_name>` / `hermes` 등). **External LLM response 적재 시 `agent="user"` 강제** (ADR-012 §2.1 원칙 7 + §2.12 #4) |
| **`event`** | **enum** | **✅ (ADR-012 §2.2 — 신규 11번째 필드)** | **17 enum 후보 (MVP 12 의무 + 5 후속 확장)** — `memory_write` / `skill_proposed` / `skill_approved` / `skill_promoted` / `skill_revoked` / `gate_pass` / `gate_fail` / `external_llm_received` / `evidence_forgery_detected` / `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` / `migration_failed` / `chain_violation_detected` / `hash_chain_broken` / `policy_change_attempted` / `canonical_json_fallback`. 자세한 분류 + T1/T2/T3 매핑 = ADR-012 §2.2 답습 |
| `content` | object | ✅ | (Memory) 자유 schema, (Skill) §3.1 17 필드 schema 그대로, (Meta) event-specific schema (ADR-012 §3.1 + §2.9 + §2.10 답습) |
| `evidence_refs` | array\<string\> | 권장 | Markdown evidence 파일 경로 |
| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` (§4.4) |
| `hash` | string (sha256) | ✅ | 본 entry 의 canonical JSON sha256 (변조 방지) — sha256 hardcode (schema_version 0.1), `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2) |

**합산 = 11 필드** (ADR-012 §2.2 답습). **모든 필드 provider-neutral 강제** (ADR-012 §2.1 원칙 6).

### 4.3 Hermes 의존 0 보장

**원칙**: Hermes 내부 DB / SDK / plugin 없이도 JSONL entry 를 *읽고 / 검증하고 / import* 할 수 있어야 한다.

| 검증 항목 | 메커니즘 | 권위 |
|---------|--------|-----|
| Hermes 의존 import 0건 | `scripts/hermes-migration/` 변환 스크립트가 `import hermes_agent` 등 의존 0건 | depcruise (G2 GP-5 답습) |
| 표준 도구로 검증 가능 | `jq` 로 parse + sha256 검증 + canonical JSON 검증 가능 (RFC 8785 reference output 동등성, §4.4.2 답습) | POSIX 표준 + RFC 8785 |
| schema_version 호환성 | 본 `0.1` 이외 버전은 **명시 declaration 후만 import 가능** (T2 사용자 승인 + §10.2 합의 절차 충족 + §4.5.3 import 검증 절차 통과 의무) | §4.5 + §10.2 + §4.6.5 답습 |
| 외부 오케스트레이터 import 가능 | claude / openai / gemini / local LLM 등 최소 2+ 로 재해석 가능 | §3.5 + GP-6 답습 |

**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).

### 4.4 Hash Chain 변조 방지 (**ADR-012 §2.3 + §2.5 + §2.6 + §2.7 + §2.8 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강 + 2026-05-11 P-1 흡수 완료**)

> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
>
> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).

#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2 답습)
- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)

**Layer 2 — Git Append-only Branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — ADR-012 §2.8 답습)
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (G3 §5.5 SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (ADR-012 §2.8 답습)
- 1인 SPOF 완화 + 침해 후 발견 가능

**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).

#### 4.4.2 Canonical JSON — RFC 8785 JCS Primary + Fallback

**Primary**: **RFC 8785 JCS** (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증 (ADR-012 §2.5 답습).

**구현 라이브러리 후보**:
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무**:
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시**:
- `event: canonical_json_fallback` ledger entry 작성 의무 (§4.2 + ADR-012 §2.5 답습)
- Reviewer 알림 + 사용자 review 권장

**참고 (이전 정의 — 보강 전)**: lex sort + RFC 8259 escape + IEEE 754 numeric — 본 정의는 fallback 동등 보장의 *최소 기준*. 본 §4.4.2 갱신으로 RFC 8785 JCS 우선 채택.

#### 4.4.3 Genesis Hash

**MVP (schema_version 0.1) — 현 정의 유지** (ADR-012 §2.6):

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

codex
primary brief에서 핵심 구조와 자체 금지 범위, γ-a/b/c/d 분석은 확인했습니다. 이제 52 entry 원문과 consensus, PoC 파일/워크플로우를 대조해서 brief가 과장하거나 빠뜨린 부분이 있는지 확인하겠습니다.
exec
/bin/bash -lc "rg -n \"2\\.2\\.4|γ-a|γ-b|γ-c|γ-d|N-A-1|B-6|§8\\.1|R-S1|9\\.5\" docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
50:| 5 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` / `tests/canonical/` 본문 변경 | 0건 (**실 repo 內 PoC 시제 *이미 운영 중*** — 본 cycle = 진입 권한 한정, 변경 0건, B-6 흡수) |
72:| 27 | **R-S1 cross-reference 정정 cycle 자동 진입** | 0건 (별도 사용자 명시 영역, §4.4 답습) |
109:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. **MANDATORY 등급 5-layer 체계 內 Layer 4** (G4 §4.4.1 + ADR-012 §2.8 동형, B-1 답습 §4.4 권위 인용 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙, **numbering 근거 아님** — §4.4 R-S1 답습) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |
118:| 2 | **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 (5-layer) + ADR-012 §2.3 (4-layer) + §2.8 (5-layer) | **Layer 4 = CI 회귀 검증 (MANDATORY), MVP-2 진입 영역 채택** | **R-S1 CONFIRMED divergence — 권위 인용 chain 정정 답습 (§4.4)** (B-1 흡수) |
123:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 = **CONFIRMED divergence** (§4.4 답습 5 source verify).
175:| **권위 출처** ⭐ (B-1 R-S1 정정 답습) | **PRIMARY**: `provider-agnostic-memory-skill-design.md §4.4.1 line 629~660` (G4 직접 정의 5-layer) + **SUPPORTING**: `ADR-012 §2.8 line 264~272` (5-layer 동형) + **PRINCIPLE ONLY (numbering 근거 아님)**: `ADR-012 §2.3 line 165~185` (Append-only + Hash Chain 원칙) + `ADR-012 §3.4` (timestamp monotonicity) + `ADR-012 §2.7` (prev_hash 실패) + `ADR-012 §2.5` (RFC 8785 JCS) |
177:#### §2.2.2 진입 자격 (51 entry audit brief §3.2 답습 + B-6 PoC 시제 격상 답습)
182:| ADR-012 §2.3 + §2.8 Layer 1~5 권위 정의 발효 (R-S1 정정 답습) | ✅ 충족 | (그대로) |
184:| Layer 1 (hash chain) 실 구현 (의존 영역) | ⚠️ **PoC 시제 충족 / PASS 시제 미충족** ⭐ (B-6 흡수) | (β) sub-수단 결정 + 실 구현 sub-cycle 영역 |
185:| canonical JSON test corpus (≥ 20개 RFC 8785 reference) | ⚠️ **PoC 시제 충족 (`tests/canonical/` 24 fixtures = 8 카테고리 × 3) / PASS 시제 미충족** ⭐ (B-6 흡수) | 실 구현 sub-cycle 영역 |
186:| Layer 4 CI step 실 구현 | ⚠️ **PoC 시제 충족 (`g4-hash-chain.yml`) / PASS 시제 미충족** ⭐ (B-6 흡수) | 실 구현 sub-cycle 영역 |
187:| ledger 첫 entry (genesis hash) | ⚠️ **PoC 시제 충족 (`tools/jsonl_hash_chain.py` genesis hash 함수 + 4 violation_type) / PASS 시제 미충족** ⭐ (B-6 흡수) | (γ) 분리 영역 결정 cycle 영역 |
201:#### §2.2.4 미발효 영역 (deferred) + (γ) 4 대안 매트릭스 (N-12 흡수)
205:- **(γ-a) Layer 1+2 의존 영역 우선 진입 후 Layer 4 추가** (단계적, 안전)
206:- **(γ-b) Layer 4 단독 진입** (Layer 1+2 = 의존 영역 자동 동시 진입)
207:- **(γ-c) Layer 1+2+4 동시 진입** (defense-in-depth 답습)
208:- **(γ-d) Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle 분리** (현 brief framing)
248:| (a) | 동등 이상 보안 결과 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ✅ R-4 답습 (`redaction-pattern-equivalence.md`) — 충족 | ⚠️ PoC 시제 충족 / PASS 시제 = 실 구현 sub-cycle 영역 (B-6 흡수) |
249:| (b) | 격리 환경 PoC 실증 | ADR-011 §2.1 (a)~(d) 4조건 모법 | ⚠️ 부분 (Group D PoC 형식적 검출 layer 한정, 송신 redaction PoC = 실 구현 sub-cycle 영역) | ⚠️ PoC 시제 충족 (`g4-hash-chain.yml`) / PASS 시제 = 실 구현 sub-cycle 영역 (B-6 흡수) |
284:| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (4 대안 (γ-a/b/c/d), §2.2.4 답습) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
295:| 4 | 권위 chain 다중 source 손상 위험 | ✅ **발화 (R-S1 CONFIRMED 격상)** ⭐ (B-1 + N-7 흡수) | §1.3 항목 2 + §2.2.1 + §4.4 = ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) **CONFIRMED divergence** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 답습 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = numbering 근거 아님). 다중 source 정정 = §4.4 + §9.5 별도 cycle 영역 |
302:### §4.4 ⭐ R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 답습 (B-1 흡수)
342:ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 = **별도 cross-reference 정정 cycle 사용자 명시 영역** (§9.5 답습). 본 (α) 합의 = 권위 인용 정정 한정 (본문 변경 0).
409:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 정정 영역 포함) |
412:| 12 ⭐ (B-1 답습) | ADR-012 §2.3 본문 정정 자동 진입 (R-S1 다중 source 정정) | 별도 cross-reference 정정 cycle 사용자 명시 영역 (§9.5 답습) |
457:| 7 | ⭐ **R-S1 CONFIRMED divergence 검증** (B-1 답습) | 본 brief §4.4 권위 인용 chain 정정 답습 + ADR-012 §2.3 vs §2.8 verbatim 직접 read |
463:### §8.1 본 brief 발효 *후* (= 본 cycle 합의 APPROVE 시점) 다음 단계 (사용자 결정 영역)
470:2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 4 분리 영역 4 대안 ((γ-a/b/c/d), §2.2.4 답습) — 풀 3+1 합의
473:5. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시 (§9.5 답습)
514:### §9.4 관련 도구 / workflow (51 entry audit brief §10 답습 + B-5 + B-6 답습)
522:- `tools/jsonl_hash_chain.py` (genesis hash + 4 violation_type) — Layer 1 PoC 시제 (B-6 답습)
523:- `tools/canonical_json.py` — canonical PoC 시제 (B-6 답습)
524:- `tests/canonical/` 24 fixtures (8 카테고리 × 3) — test corpus PoC 시제 (B-6 답습)
527:### §9.5 본 brief 발효 후 cross-reference 갱신 영역 (별도 commit, B-1 + N-13 흡수)
529:- **R-S1 정정 영역 (별도 cross-reference 정정 cycle 사용자 명시 영역)** ⭐ (B-1 흡수):
535:- **Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문** ⭐ (N-13 흡수): MVP-2 Implementation Evidence PASS 합의 시 R-S1 정정 *선행 의무* 또는 *동시 의무* 영역 결정 (별도 합의)
550:| **P-4** ⭐⭐⭐ (CONFIRMED divergence 격상) | **R-S1 CONFIRMED divergence** — ADR-012 §2.3 (4-layer) vs §2.8/G4 §4.4.1 (5-layer) | §4.4 답습 (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer). 본 brief v1.1 = 권위 인용 chain 정정 한정 (§1.2 + §2.2.1 + §4.4.2). 다중 source 정정 = §9.5 별도 cycle 영역 |
554:| **P-8** ⭐ (Agent B 권고 답습) | filesystem 직접 inspection evidence (B-4 + B-5 + B-6) 가 본 cycle 발효 시점 (2026-05-28) state 한정 → 본 cycle 後 변경 시 evidence 변질 | §0.3 #2 + #5 명시 (본 cycle 內 변경 0) + filesystem state 답습 시점 명시. 본 cycle 후 변경 영역 = 별도 cycle |
566:| B-1 (R-S1 CONFIRMED 격상) | §0.4 + §1.2 + §1.3 항목 2 + §2.2.1 + §3 (c) + §4.3 (4) + §4.4 신규 + §6.2 #12 + §9.5 + §10 P-4 | "잠재 risk" → "CONFIRMED divergence" 격상 + 5 source cross-confirm + 권위 인용 chain 정정 (G4 §4.4.1 + ADR-012 §2.8 PRIMARY, §2.3 = principle only) + 별도 cross-reference 정정 cycle 사용자 명시 영역 |
571:| B-6 (PoC 시제 격상) | §0.3 #5 + #6 + §2.2.2 4 row + §3 (a)+(b)+(d) + §2.2.4 + §9.4 + §10 P-8 | "❌ gap" → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상 + 실 PoC evidence 답습 (tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml) |
579:| N-2 (planning vs implementation track) | §2.2.3 + §8.1 항목 3 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 |
582:| N-5 (event enum reserved) | §5.3 + §9.5 | "reserved candidate" 격하 + ADR-012 §2.2 amendment 별도 cycle |
584:| N-7 (trigger 4 격상) | §4.3 (4) | "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
589:| N-12 ((γ) 4 대안 + L-1.5) | §2.2.4 + §8.1 항목 2 | (γ-a/b/c/d) 4 대안 매트릭스 + L-1.5 alternative (stdlib + 자체 RFC 8785 test corpus 충분성) |
590:| N-13 (PASS 발효 사전조건) | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |

exec
/bin/bash -lc "rg -n \"γ|Layer 1\\+2|Layer 4|N-A-1|B-6|R-S1|Rollback|APPROVE|REVISE\" docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
1:# 풀 3+1 합의 보고서 — MVP-2 진입 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증)
13:**Reviewer 통합 판정**: ⚠️ **REVISE AS ENTRY BRIEF INPUT (BLOCKING 7 + 권고 13)** — brief v1.1 보강 후 본 cycle 합의 발효 자격 충실. 24 entry codex 답습 동형 판정 (codex `REVISE AS ENTRY BRIEF INPUT` 직접 답습).
19:| Agent A (구현) | Anthropic Claude | APPROVE WITH CONDITIONS | 2 (R-A-1, R-A-2) | 4 (N-A-1~4) | 2 |
20:| Agent B (안전성) | Anthropic Claude | REVISE | 2 (R-B-1, R-B-2) | 4 (N-B-1~4) | 3 |
21:| Agent C (대안) | Anthropic Claude | APPROVE WITH CONDITIONS | 2 (R-C-1, R-C-2) | 6 (N-C-1~6) | 3 |
22:| codex (외부 LLM 1+) | **OpenAI (cross-vendor)** | **REVISE AS ENTRY BRIEF INPUT** | 3 (R-1, R-2, R-3) | 5 (N-1~5) | 3 |
23:| **Reviewer 통합** | Anthropic Claude (Opus 4.7) | **REVISE AS ENTRY BRIEF INPUT** | **7** (Consensus 2 + Unique 5) | **13** (중복 제거) | 통합 |
27:⚠️ **본 합의 = entry 합의 자격 한정**. 본 합의 REVISE → brief v1.1 보강 1pass 흡수 → 본 cycle 합의 발효 시 진입 권한 발효. 본 합의 직후 *자동 (β)/(γ)/실 구현 진입 금지* (단계별 합의 cycle 답습).
37:| 1 | **R-S1 잠재 → CONFIRMED 격상** | ✅ R-2 BLOCKING | ✅ N-A-4 권고 + verbatim verify | ✅ R-B-1 BLOCKING | ✅ verbatim verify (NOTE) | **Consensus 4/4 ⭐⭐⭐⭐ + Reviewer verify 5/5** |
42:| 6 | **`tools/jsonl_hash_chain.py` + `canonical_json.py` + `tests/canonical/` + `g4-hash-chain.yml` PoC 시제 이미 운영 중** | (미명시) | ✅ N-A-1 권고 (filesystem) | (미명시) | (미명시) | **Agent A Unique ⭐⭐⭐ (권고 → BLOCKING 격상 자격, brief §2.2.2 "❌ gap" → "⚠️ PoC 시제 충족 / PASS 시제 미충족")** |
48:- **C-1 (4/4 source + Reviewer = 5/5)**: **R-S1 = CONFIRMED divergence** (ADR-012 §2.3 4-layer numbering vs §2.8/G4 §4.4.1 5-layer numbering)
73:| **B-1** | C-1 (Consensus 4/4 + Reviewer = 5/5) | **R-S1 CONFIRMED 격상** | codex R-2 + Agent A N-A-4 + Agent B R-B-1 + Agent C verify + Reviewer 단독 verify | brief §10 P-4 "잠재 risk" → "CONFIRMED divergence" 격상 + §1.3 G4 §4.4 Layer 4 항목 답습 보강 + §4.3 trigger (4) "부분 발화" → "발화" 격상 + §9.5 cross-reference 정정 cycle 사용자 명시 영역 추가 | v1.1 §10 P-4 본문 정정 + §1.3 + §4.3 + §9.5 |
74:| **B-2** | C-2 (Consensus 3/4) | **ADR-011 §2.1 framing 정정** | codex R-1 + Agent A NT-A-2 + Agent B R-B-2 | brief 다수 위치 "(a)~(e) 5조건" → "(a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건" 정정. 영향 영역: §0.2 #5, §0.4, §1.1, §3, §4 등 | v1.1 다수 위치 정정 (sed 또는 직접) |
78:| **B-6** | P-4 (Agent A Unique, filesystem) | **brief §2.2.2 "❌ gap" 4 row → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상** | Agent A N-A-1 (filesystem inspection, BLOCKING 격상 자격) | brief §2.2.2 표 4 row 격상 + §3 매트릭스 (b)+(d) gap row 정밀화 + §2.2.4 미발효 영역 답습 보강 | v1.1 §2.2.2 + §3 + §2.2.4 정밀화 |
87:| N-1 | Rollback Trigger 본문 "채택" vs "후보" 표현 분리 (entry brief input 단계 vs Implementation Evidence PASS 단계) | codex N-1 + Agent A 영역 | §0.4 + §5 |
88:| N-2 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 표현 | codex N-2 | §2.2.3 + §8.1 |
93:| N-7 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) | Agent B N-B-1 | §4.3 |
98:| N-12 | (γ) 4 대안 매트릭스 ((γ-a) Layer 1+2 우선 → Layer 4 후속 / (γ-b) Layer 4 단독 / (γ-c) Layer 1+2+4 동시 / (γ-d) Layer 4 + Layer 1+2 별도) + L 외부 library trade-off + L-1.5 alternative | Agent C N-C-2 + N-C-3 | §2.2.4 + §8.1 |
99:| N-13 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 | Agent C N-C-5 + N-C-6 | §9.5 |
103:## §4 R-S1 CONFIRMED divergence — Reviewer 단독 verbatim verify 결과
105:### §4.1 Verbatim 직접 read 결과 (Reviewer 단독, 24 entry R-S1 답습 패턴)
111:- **Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**
117:- **Layer 4: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지**
124:- **Layer 4 — CI 회귀 검증 (MANDATORY)**
130:- §2.3 = External anchor 를 Layer 4 위치 (4 layer 총)
131:- §2.8 = External anchor 를 Layer 5 위치 + Layer 4 슬롯에 "CI 회귀 검증" 추가 + Layer 3 슬롯에 "pre-commit hook" 추가 (5 layer 총)
136:### §4.3 R-S1 판정
138:**R-S1 = CONFIRMED** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer = 5/5).
141:- 권위 chain 다중 source divergence (ADR-008 §A.2 R1-2 유형 답습 — 24 entry R-S1 답습 패턴)
143:- 동일 label "Layer 4" 의 semantic collision
145:**본 cycle 처리** (24 entry R-S1 답습):
151:v1.1 시점 brief 의 G4 §4.4 Layer 4 인용 = 다음 권위 chain 한정:
168:| B-2 | §0.2 #5, §0.4, §1.1, §3, §4 등 다수 | "ADR-011 §2.1 (a)~(e) 5조건" → "ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건" 정정 |
169:| B-3 | §0.1 | "(β) sub-수단 결정 cycle — 별도 합의 또는 (α) 內 흡수" → "(β) sub-수단 결정 cycle — 별도 합의 (본 cycle 內 흡수 0). 본 cycle 발효 효과는 (β)/(γ) 진입 자격 발효까지" 정정 |
172:| B-6 | §2.2.2 + §3 + §2.2.4 | 4 row gap → "⚠️ PoC 시제 충족 / PASS 시제 미충족" 격상. 답습 evidence: `tools/jsonl_hash_chain.py` + `tools/canonical_json.py` + `tests/canonical/` 24 fixtures + `g4-hash-chain.yml` PoC 시제 |
179:| N-1 | §0.4 + §5 | Rollback Trigger / Evidence = "후보 채택" vs "구현 발효" 표현 분리 명시 |
180:| N-2 | §2.2.3 + §8.1 | G4 Layer 4 "planning/decision track" vs "implementation track" 분리 |
185:| N-7 | §4.3 | trigger (4) "부분 발화" → "발화" 격상 (B-1 R-S1 CONFIRMED 답습) |
190:| N-12 | §2.2.4 + §8.1 | (γ) 4 대안 매트릭스 + L 외부 library trade-off + L-1.5 alternative |
191:| N-13 | §9.5 | Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문 |
203:### §6.1 본 합의 발효 효과 (REVISE → v1.1 보강 후 발효 자격 충실)
205:본 합의 REVISE → brief v1.1 보강 1pass 흡수 commit 후 본 cycle 합의 발효:
207:1. **MVP-2 영역 진입 권한 발효** (GP-2 + G4 §4.4 Layer 4)
209:3. **(γ) 분리 영역 결정 cycle 진입 자격 발효** (Layer 1+2 의존 vs Layer 4 동시)
210:4. **Rollback Trigger 본문 *후보 채택*** (구현 발효 ≠ 본 합의, 별도 sub-cycle)
217:- ❌ MVP-2 Implementation Evidence PASS 발효 (실 구현 + (a)~(d) evidence + (e) 합의 APPROVE + 사용자 명시 후 별도)
218:- ❌ R-S1 cross-reference 정정 cycle 자동 진입 (별도 사용자 명시 영역, §4.3 답습)
226:본 합의 REVISE → 다음 단계 순서 (단계별 합의 cycle 답습):
230:3. **본 cycle 합의 발효** (v1.1 commit 후 자동 — REVISE → APPROVE WITH CONDITIONS 격상)
233:   - **(γ)** 분리 영역 결정 cycle (Layer 1+2 의존 vs Layer 4 동시)
234:   - **R-S1 cross-reference 정정 cycle** (ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화 — 별도 풀 3+1 + 사용자 명시)
246:| M-2 | "REVISE" 판정이 풀 3+1 절차 ceremony-inflation 회피 자격 위협 | 24 entry codex 답습 동형 판정 (codex `REVISE AS ENTRY BRIEF INPUT` 직접 답습). v1.1 1pass 흡수 = ceremony-inflation 차단 답습 충실 (별도 v2 cycle 0) |
249:| M-5 | R-S1 = 24 entry R-S1 답습 동형 패턴 → "절차적 답습" 위험 | §4 verbatim 직접 read evidence (Reviewer 단독 verify + 4 source verbatim cross-confirm = 5 source) + ADR-012 *자체 내부* divergence 명문 (24 entry 답습 외 발견 영역) |
251:| M-7 | 본 합의 REVISE → 자동 v1.1 보강 진입 위험 (단계별 cycle 답습 위반 위험) | §7 명시 = brief v1.1 보강 (Claude 영역, BLOCKING + 권고 흡수) → commit + push (사용자 명시) → 본 cycle 합의 발효. 자동 (β)/(γ)/실 구현 진입 0건 |

exec
/bin/bash -lc 'rg -n "N-A-1|B-6|R-S1|Layer 1|Layer 4|jsonl_hash_chain|canonical_json|g4-hash-chain|history-anchor|rewrite-defense" docs/external-review/2026-05-28-mvp2-entry-codex-response.md' in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
20:- MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 진입 권한 발효
22:- (γ) 분리 영역 결정 cycle 진입 자격 발효 (G4 §4.4 Layer 1+2 의존 vs Layer 4 동시)
41:- `docs/architecture/provider-agnostic-memory-skill-design.md` (§4.4 Layer 1~5)
58:4. **두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가** — 각 영역별 평가 본문 + governance-preconditions §4.4 (Entry 3 조건) + §4.5 (Exit 5조건) + G4 §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (다층 강제) verbatim 인용 평가
64:7. ⚠️ **R-S1 잠재 risk 검증** — 본 brief §10 P-4 자기진단 영역 (ADR-012 §2.3 line 182 verbatim = "Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)" 인지 / 또는 G4 §4.4.1 line 649~653 verbatim = "Layer 4 — CI 회귀 검증 (MANDATORY)" 인지). 두 source 의 "Layer 4" 정의 *충돌* 검증 — 권위 chain 다중 source 손상 위험 (24 entry R-S1 답습 패턴, ADR-008 §A.2 R1-2 권위 chain 다중 source 손상 확정 유형). codex 가 ADR-012 §2.3 line 182 verbatim 직접 read + G4 §4.4.1 line 649~653 verbatim 직접 read 후 비교 평가 의무
85:- §5 R-S1 잠재 risk 검증 결과 (verbatim 인용 + 충돌 분석)
96:> **scope**: G2 GP-2 송신 redaction + G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit
110:3. G4 §4.4 Layer 4 (CI 회귀 검증) 진입 자격 audit (Entry 충족 자격 + Exit 5조건 매핑 권고)
126:- ❌ ADR-012 본문 갱신 (Layer 1~5 권위 답습)
138:- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5 다층 강제) — `docs/architecture/provider-agnostic-memory-skill-design.md`
167:50 entry carry-over §4: "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)".
173:**G4 §4.4 Layer 4 — CI 회귀 검증** (provider-agnostic-memory-skill-design §4.4.1):
174:- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
178:- MANDATORY 등급 (Layer 5 中 4번째, Layer 1 + 2 + 4 MANDATORY, Layer 3 + 5 RECOMMENDED MVP)
185:- **G4 §4.4 Layer 4**: R-6 workflow 답습 확장 (Layer 1+2 자동 회귀 + canonical JSON 위반 + timestamp monotonicity)
218:| (d) | 자동 회귀 검증 경로 확보 | ❌ gap | **R-6 workflow 에 log file canary inject step 추가 — §4 통합 권고 (G4 §4.4 Layer 4 와 단일 workflow 확장)** |
237:## §3 G4 §4.4 Layer 4 진입 자격 audit
241:**Layer 4 — CI 회귀 검증 (MANDATORY)**:
242:- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
247:**참고**: 본 audit = Layer 4 영역 한정. Layer 1 / Layer 2 / Layer 3 / Layer 5 = 본 brief 직접 scope 외 (단, Layer 4 검증 대상 = Layer 1 + Layer 2 이므로 *의존 영역* 으로 명시).
254:| 2 | ADR-012 §2.3 Layer 1~5 권위 정의 발효 | ✅ 2026-05-09 PR-2 풀 3+1 + 외부 LLM 2건 APPROVE WITH CONDITIONS | 충족 |
256:| 4 | Layer 1 (hash chain) 실 구현 (`tools/jsonl_chain_verify.py` 또는 동등) | ❌ gap (의존 영역) | 미충족 |
258:| 6 | Layer 4 CI step 실 구현 (R-6 workflow 확장) | ❌ gap | 미충족 |
262:→ **현 시점 Entry 충족 자격 = 3/8 충족 + 1 사용자 영역** (Design Gate + Layer 정의 + JCS 채택만 충족, 4 의존 영역 + Layer 4 자체 구현 gap).
266:| # | 조건 | G4 §4.4 Layer 4 현 상태 | 충족 경로 권고 (수단 결정 0) |
268:| (a) | 동등 이상 보안 결과 | ❌ gap (실 구현 부재) | Layer 1+2+4 결합 보안 결과 vs 기존 (없음) 비교표 — middle entry tampering / canonical 위반 / timestamp 위반 차단 |
272:| (e) | 합의 APPROVE | ❌ gap | **풀 3+1 합의 권고** (G4 §4.4 Layer 1+2+4 통합 + Layer 5 권고 영역 추가 의사결정) |
280:| **L-1** | Layer 1 (hash chain) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) | hash chain 검증 | stdlib | fallback canonical JSON, RFC 8785 동등성 test corpus 의무 |
281:| **L-2** | Layer 1 + RFC 8785 JCS Primary (`pyjcs` / `rfc8785` library) | hash chain + canonical | 외부 library 1+ (의존성 추가 trigger — R-2 / R-4.1 PoC 자동 재실행 의무 ADR-012 §2.1 답습) | Primary 채택, fallback 보조 |
282:| **L-3** | Layer 4 R-6 workflow step (canonical JSON 위반 + prev_hash mismatch + timestamp monotonicity) | CI 회귀 | shell + Python (stdlib) | R-6 답습 확장 |
283:| **L-4** | L-1 + L-3 병행 (MVP 권고) | Layer 1+4 동시 | stdlib 단독 | **본 brief 권고 — MVP 단계 답습 (5/5 입력 권고 답습)** |
284:| **L-5** | L-2 + L-3 병행 (정식 권고) | Layer 1+4 + JCS Primary | 외부 library 1+ | 정식 채택 시점 (Operational Readiness 영역 또는 별도 cycle) |
297:| G4 §4.4 Layer 4 | Layer 1 + Layer 2 자동 회귀 + canonical 위반 + timestamp monotonicity CI step | ✅ R-6 답습 확장 (provider-agnostic-memory-skill-design §4.4.1 line 653 답습) |
305:| **W-A: 단일 R-6 확장 (GP-2 + G4 §4.4 Layer 4 통합)** | ceremony-inflation 차단 / CI 자원 효율 / evidence 통합 / R-6 답습 한 PR | step 수 증가 / 실패 영역 식별 복잡도 ↑ (step name 분리로 완화 가능) | **✅ 본 brief 권고** |
322:  # 신규 G4 §4.4 Layer 4 step (L-3 답습)
340:| RT-4 | hash chain middle entry tampering 검출 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
341:| RT-5 | canonical JSON 위반 검출 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
342:| RT-6 | timestamp monotonicity 위반 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
381:  - GP-2 + G4 §4.4 Layer 4 = 두 영역 통합 합의 (단일 R-6 workflow 확장)
408:- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 자동 의존 영역)
409:- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 (MVP-3 ~ MVP-5 영역 답습)
421:   - **(γ)** 분리 영역 결정 (예: G4 §4.4 Layer 1/2 의존 영역 우선 진입 vs Layer 4 동시 진입)
432:- **provider-agnostic-memory-skill-design.md §4.4** (Layer 1~5 다층 강제 + Canonical JSON RFC 8785 + Genesis Hash + prev_hash 실패)
456:| P-4 | 50 entry carry-over "G4 §4.4 Layer 4" 해석 (Layer 4 = CI 회귀 검증) 가 사용자 의도와 다를 가능성 | §1.3 + §3.1 해석 명시 + 사용자 검토 시 정정 가능 영역 |
457:| P-5 | Layer 4 의 의존 영역 (Layer 1 + Layer 2) 미진입 시 Layer 4 단독 진입 의미 부재 | §3.2 Entry 자격 4/5/7 = Layer 1 / test corpus / genesis hash *의존 영역* 명시, §9 (γ) "분리 영역 결정" 명시 |
472:> **scope**: MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 본격 진입 합의
488:- (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 별도 합의 또는 (α) 內 흡수
489:- (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입
495:1. **MVP-2 영역 정의 답습** — 51 entry audit brief §1.3 (GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 직접 답습 (§1)
496:2. **51 entry audit brief 답습 cross-check** — 진입 자격 매트릭스 (GP-2 Entry 2/3 + Exit 2.5/5 / G4 §4.4 Layer 4 Entry 3/8 + Exit 1/5) 정합성 검증 (§2)
522:| 12 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
523:| 13 | **G4 §4.4 Layer 4 분리 영역 결정** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) | 0건 ((γ) 별도 cycle) |
535:| 25 | G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 자동 결정 | 0건 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 의존 영역 자동) |
536:| 26 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 자동 결정 | 0건 (MVP-3 ~ MVP-5 영역 답습) |
560:| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
568:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |
577:| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
581:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.
622:### §2.2 G4 §4.4 Layer 4 — CI 회귀 검증 — 진입 자격
628:| **목적** | Evidence Ledger 무결성 자동 회귀 검증 — Layer 1 (hash chain) + Layer 2 (history) + canonical JSON 위반 + timestamp monotonicity 위반 자동 검출 |
630:| **메커니즘** | (L-1) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) + (L-2) RFC 8785 JCS Primary (`pyjcs` / `rfc8785`) + (L-3) Layer 4 R-6 workflow step + (L-4) L-1+L-3 병행 (MVP 권고) + (L-5) L-2+L-3 병행 (정식) |
631:| **권위 출처** | provider-agnostic-memory-skill-design.md §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패 처리) + §3.4 (timestamp monotonicity) |
638:| ADR-012 §2.3 Layer 1~5 권위 정의 발효 | ✅ 충족 | (그대로) |
640:| Layer 1 (hash chain) 실 구현 (의존 영역) | ❌ gap | (β) sub-수단 결정 + 실 구현 sub-cycle 영역 |
642:| Layer 4 CI step 실 구현 | ❌ gap | 실 구현 sub-cycle 영역 |
643:| ledger 첫 entry (genesis hash) | ❌ gap | (γ) 분리 영역 결정 cycle 영역 — Layer 1 의존 |
650:✅ **G4 §4.4 Layer 4 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
652:✅ **(γ) 분리 영역 결정 cycle 진입 자격 발효** — Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (별도 합의)
659:❌ Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 = (γ) 분리 영역 결정 cycle (Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 결정)
669:| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
690:| # | 조건 | GP-2 (§2.1) | G4 §4.4 Layer 4 (§2.2) |
702:- (γ) 분리 영역 결정 cycle → Layer 1+2 의존 영역 vs Layer 4 동시 결정
726:| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고, 51 brief §3.4 답습) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
737:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
749:| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |
762:| RT-4 | hash chain middle entry tampering 검출 | G4 §4.4 Layer 4 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
763:| RT-5 | canonical JSON 위반 검출 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
764:| RT-6 | timestamp monotonicity 위반 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
788:| 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
812:| 6 | G4 §4.4 Layer 1/2/3/5 영역 자동 진입 | 별도 cycle 또는 의존 영역 자동 (사용자 명시) |
813:| 7 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 자동 진입 | MVP-3~MVP-5 영역 (별도 합의) |
815:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
842:| provider-agnostic-memory-skill-design.md §4.4 (Layer 1~5) | `docs/architecture/provider-agnostic-memory-skill-design.md` |
859:| 4 | 두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가 | 두 영역별 평가 본문 |
862:| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |
872:1. **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 풀 3+1 합의
873:   - 본 (α) 권고 (51 brief 답습): GP-2 = R-4 (R-1+R-2+R-3 병행) / G4 §4.4 Layer 4 = L-4 (L-1+L-3 병행 MVP)
874:2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 — 풀 3+1 합의
875:3. **실 구현 sub-cycle** ((β) + (γ) 후) — Hermes native redaction evidence + facade RedactionFilter (TR-1 (d) carry-over 의존) + Layer 1 (hash chain) 구현 + canonical JSON test corpus + R-6 workflow 확장 step + 합의 형태 별 (수단별 차등)
877:5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)
903:- **`provider-agnostic-memory-skill-design.md §4.4`** (Layer 1~5) — `docs/architecture/provider-agnostic-memory-skill-design.md`
924:- ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
925:- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle
938:| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
941:| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
947:**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.
983:- ❌ G4 §4.4 Layer 4 sub-수단 결정 (L-1 / L-2 / L-3 / L-4 / L-5)
989:- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정
990:- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정
1004:| 4 | 권위 chain 다중 source 손상 위험 | ❌ 미발화 | brief = cross-reference 답습 한정 (§10 17 source 명시), 24 entry R-S1 유형 손상 0건 |
1014:- carry-over §4 "MVP-2 진입 자격 검토 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4)" = brief §1.3 영역 정의 정확 답습
1015:- "G4 §4.4 Layer 4" 해석 = provider-agnostic-memory-skill-design §4.4.1 line 649 "Layer 4 — CI 회귀 검증 (MANDATORY)" = brief §3.1 답습
1021:- provider-agnostic-memory-skill-design.md §4.4.1 Layer 1~5 → brief §3.1 + §3.4 직접 답습
1029:- G4 §4.4 Layer 4 Exit 5조건 매트릭스 (brief §3.3): (c) 만 충족 / (a)/(b)/(d)/(e) gap → ADR-012 §2.3 답습 일치
1034:- G4 §4.4 Layer 4 L-1~L-5 (brief §3.4) = 후보 비교만, L-4 권고 = "수단 *결정* = 별도 합의 영역" 영구 분리 답습
1051:| §1.3 (lines 80~89) | "G2 GP-2 송신 redaction + G4 §4.4 Layer 4 — CI 회귀 검증" | ✅ 50 entry carry-over §4 직접 답습 |
1052:| §1.4 (lines 91~96) | "두 영역 모두 R-6 workflow 답습 확장 영역" 핵심 발견 | ✅ governance-preconditions §4.6 + G4 §4.4.1 Layer 4 line 653 verbatim 일치 |
1055:| §3.1 (lines 137~141) | "Layer 4 = CI 회귀 검증 (MANDATORY)" | ✅ provider-agnostic-memory-skill-design §4.4.1 line 649~653 verbatim 일치 |
1056:| §3.2 (lines 146~156) | "Entry 충족 = 3/8 + 1 사용자 영역 (의존 영역 4 gap)" | ✅ Layer 1+2+test corpus+genesis 의존 영역 명시 정확 |
1061:| §11 (lines 350~358) | "P-1~P-5 자기진단 (편향 / 통합 복잡도 / 권고 무단 침입 / Layer 4 해석 / 의존 영역)" | ✅ 메타 편향 회피 답습 정확 (특히 P-4 Layer 4 해석 사용자 검토 정정 가능 영역 명시) |
1072:- ❌ **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) 결정 cycle (별도 합의 영역)
1073:- ❌ **(γ) 분리 영역 결정** — G4 §4.4 Layer 1/2 의존 영역 우선 진입 vs Layer 4 동시 진입 (Entry 자격 매트릭스 §3.2 답습)
1075:- ❌ G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 (의존 영역 또는 별도 권위)
1076:- ❌ GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 (MVP-3 ~ MVP-5 영역 답습)
1078:- ❌ Implementation Evidence PASS 발효 (GP-2 / G4 §4.4 Layer 4 각각) — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 + 별도 합의
1112:- (4) **(γ) 분리 영역 결정** — G4 §4.4 Layer 1+2 의존 영역 우선 vs Layer 4 동시 (Entry 자격 매트릭스 답습)
1128:| M-4 | brief §1.3 "G4 §4.4 Layer 4" 해석 정확성 검증 부족 | provider-agnostic-memory-skill-design §4.4.1 line 649~653 verbatim 직접 read + §3 cross-check 일치 + brief §11 P-4 사용자 정정 영역 명시 |
1138:PRIMARY와 51 entry 입력 자료는 확인했습니다. 이제 사용자가 지정한 권위 조항의 실제 문구를 직접 대조해서, 특히 ADR-011의 “(a)~(e)” 표현과 R-S1 Layer 4 충돌 가능성을 판정하겠습니다.
1454:   488	| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
1470:   629	#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)
1472:   631	**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
1490:   649	**Layer 4 — CI 회귀 검증 (MANDATORY)**:
1491:   650	- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
1501:   660	**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).
1535:   149	| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
1536:   150	| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
1537:   151	| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
1538:   152	| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
1551:   165	**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
1568:   182	**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
1577:   191	**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.
1587:   201	**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.
1606:   220	- `event: canonical_json_fallback` ledger entry 작성 의무
1625:   234	genesis_hash = sha256("genesis:" + canonical_json({
1650:   259	- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
1653:   262	- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)
1659:   268	- **Layer 1**: Hash chain (middle entry tampering 차단)
1662:   271	- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
1731:   340	| (d) | JSONL middle tampering | **강** — Layer 1 (hash chain) 정확히 이 케이스 차단 | (그대로) |
1870:    75	- (iii) **GP-2 redaction** (외부 LLM 답습) = MVP-1 vs MVP-2 사이의 *경계* — 본 문서는 GP-2 = MVP-2 로 분리 답습 (C-7 line 379 답습 — "MVP-2 \| G2 GP-2 + G4 §4.4 Layer 4")
1877:    82	│  Layer 1: Design/Governance Gate PASS                          │
1914:   119	| 1 | Layer 1 (Design/Governance Gate) PASS 발효 | ✅ G2/G3/G4 = PASS Bundled (2026-05-09) | `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` |
1916:   121	| 3 | GP-5 PoC 완료 (Layer 1a/1b/1c 시제) | ✅ Group A 1차/2차/3차 PASS (2026-05-09 ~ 2026-05-10) | `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` + `g2-gp5-poc2-import-linter-implementation.md` + `g2-gp5-poc3-url-endpoint-model-name-scanner.md` |
1932:   137	| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
2082:R-S1의 핵심 대조점이 확인됐습니다. ADR-012 §2.3의 Layer 4는 External anchor이고, G4 §4.4.1의 Layer 4는 CI 회귀 검증입니다. 같은 “Layer 4” 라벨이 서로 다른 의미로 쓰여 있어, brief가 이를 “미세 충돌”로만 처리해도 되는지 별도 blocking으로 판단하겠습니다.
2084:/bin/bash -lc 'rg -n "R1-2|권위 chain|다중 source|source 손상|R-S1" docs/decisions docs/review docs/phase0 docs/architecture | head -80' in /home/delangi/문서/project/category/AI_development_tool
2092:docs/architecture/governance-preconditions.md:106:| **P3** | **Credential / OAuth 파일 권한 노출** | API 키 파일 / OAuth credentials 파일이 world-readable / docker socket mount / inotify 미감시 | 8조 #2 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + entrypoint stat 검증 (35번째 entry R-S1 정정 답습) |
2093:docs/architecture/governance-preconditions.md:343:| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | (저장) docker secret + chmod 600 + entrypoint stat + inotify, (코드) gitleaks / detect-secrets pre-commit hook + CI step | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 (35번째 entry R-S1 정정 답습) |
2095:docs/architecture/governance-preconditions.md:488:| 계산적 | docker secret 정의 | `docker-compose.yml` (ADR-008 차단조건 #6 답습, 35번째 entry R-S1 정정 답습) |
2098:docs/architecture/governance-preconditions.md:498:- ✅ ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 (OAuth credentials 처리 강화) 명시 (충족됨, 35번째 entry R-S1 정정 답습)
2099:docs/architecture/governance-preconditions.md:508:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + 헌법 8조 #1 + 본 §5 (35번째 entry R-S1 정정 답습) |
2100:docs/architecture/governance-preconditions.md:523:- ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (35번째 entry R-S1 정정 답습)
2102:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:5:**선행**: (4-way) brief v1.1 (`35e0e8c`, 588줄) + 풀 3+1 합의 (`5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4) + 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`, 2026-05-22, "feat(jarvis): MVP-1 트랙 A — Boss LLM advisory 판단 지점 (TDD)")
2103:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:6:**scope**: 기존 `src/jarvis/boss.py` 99줄 design doc *추출* + Backend 후보 매트릭스 *신규* — **신규 코드 0건, 기존 변경 0건** (R-S1 발효 BLOCKING-1 답습 영구)
2104:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:10:## 1. 본 design doc 의 자격 (R-9 + R-15 + R-S1 답습)
2105:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:398:- ⭐⭐⭐ **본 design doc = 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) design doc *추출* + Backend 후보 매트릭스 *신규* only** (신규 코드 0건, 기존 변경 0건, R-S1 발효 답습 영구)
2106:docs/architecture/jarvis-mvp1-boss-abstraction-design.md:417:| R-S1 발효 (boss.py:24~98 verbatim 인용) | ✓ §2.1~§2.5 verbatim 인용 완료 |
2107:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:3:> **합의 cycle (f-K)**: Provider Liquidity deep-dive 합의 (`a9e1e88`, BLOCKING 13) 의 **R-26 (C-R2) + R-11** 답습 후속 cycle. brief v1 (`f305174`, 556줄) → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) 산출. **APPROVE w/ COND**, BLOCKING 16 + 권고 21 + NOTE 24, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1 / R-S2 / R-S3). 본 합의는 brief v1 의 진술을 BLOCKING 으로 정정하는 *권한* 을 가지나, **(1) ADR-011 §6 본문 정정 자격 0 + (2) Provider Liquidity 본질 약화 자격 0 + (3) MVP-1 합의 본문 정정 자격 0 + (4) 헌법 본문 정정 자격 0 + (5) 메모리 본문 정정 자격 0 + (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)** 의 **7 권한 한계 영구 답습**.
2108:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:35:| evidence "GGUF 한정" 더 좁은 한정 (시점 부정합 vs 분류 축) | A-B2 + A-S1 ⭐ / C-B1 + C-S1 ⭐ | A 시점 부정합 + C 분류 축 = 본질 부정 *분리* 동형 → R-S1 통합 |
2109:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:75:- **R-S1 (A-S1 격상)** ⭐: Phase 3 raw line 25~32 결론 verbatim 직접 확인 — "Ollama 다운로드 GGUF = 더 오래된 conversion (`.ssm_dt.bias` 미저장) + llama.cpp `c0c7e147` master = `.dt_bias` → `.dt_proj.bias` rename + `.bias` flag=0 required 강제". 본 evidence 의 본질 = **시점 부정합** (Ollama blob 동기화 미수행 + llama.cpp conversion lineage backward-incompatible 변경) ≠ "GGUF 가족 본질 부정". A-S1 = Reviewer 단독 직접 raw 확인으로 격상 BLOCKING.
2110:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:163:P3-F1 evidence 의 일반화 자격 = "GGUF 가족 한정" + "sub-차원 (1) tensor naming 한정" + **"1 conversion script lineage × 1 시점" 한정** 3 layer 답습 의무. **R-S1 통합 답습**.
2111:docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md:397:**End of consensus report** — 작성 2026-05-24, 3 Agent 병렬 독립 PASS + Reviewer 단독 격상 3건 (R-S1·R-S2·R-S3) + 정합성 매트릭스 + BLOCKING 16 + 권고 21 + NOTE 24 + 기각 0
2112:docs/architecture/mvp-1-to-6-entry-conditions-brief.md:93:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + `roadmap-mvp1.md` §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + `roadmap-mvp1.md` §4 (36번째 entry R-S1 정정 답습) |
2113:docs/architecture/hermes-not-root-of-trust-runtime.md:25:> **[Cross-reference Block — (g1-N-3-adr-008+sip+adr-012') R-7 (f) cross-ref block 만 채택 + R-S1 (CRITICAL) 답습]**: 본 line 23 (상위 권위) + line 176 (cross-ref 표) + line 1040 (영구 핵심 제약 표) 표기 "헌법 제5조 관용 (Provider Liquidity)" / "헌법 5조 (관용 — Provider Liquidity)" / "헌법 5조 (관용)" = (g1-N-1) commit `148fbbe` 후 **헌법 제5조-2: Provider Liquidity 원칙 (비협상) (line 75~80)** 직접 모법 발효 — (g1-N-1) 이전 관용 표현 답습. 본 cycle = gov §1.1 line 78 verbatim 명문 4 source ("ADR-008 / ADR-011 / system-identity-prequel / 본 v3") *외* **유일 추가 동형 source** 신규 식별 (R-S1 CRITICAL, Reviewer raw cross-check 강화 — bash grep `"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"` = ADR-012 + 본 source 단 2 파일 verify). Agent C 단독 발견 + Reviewer raw cross-check 직접 verify (line 176/1040 단독 추가 식별). (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습, **본문 verbatim 변경 0건** ((f) cross-ref block 만 채택). 정정 후 형식 = ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" (R-rec-3 답습 + 사용자 명시 직접 확인). 추가 위치 line 7/897/1073 (P3 본문) = 본질 답습, 정정 자격 약함 ((P3) 약식 통일 cycle DEFER carry-over). 본 cycle 합의 = `209f04d`.
2114:docs/phase0/mvp1-r-s1-framing-correction-brief.md:1:# MVP-1 R-S1 cross-reference 정정 + framing 정정 sub-cycle brief ((b2) + (b3) 병렬)
2115:docs/phase0/mvp1-r-s1-framing-correction-brief.md:3:> **scope**: 24번째 entry brief v1.1 carry-over (b2) R-S1 권위 chain 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 sub-cycle). 33번째 entry R-S1 raw verify (Agent B + codex 일치) + Reviewer 통합 R-3 답습 (multi-source 재기술).
2118:docs/phase0/mvp1-r-s1-framing-correction-brief.md:18:| 33번째 entry 합의 보고서 R-MVP1-PASS-2 | brief v1.1 §6 | "R-S1 정정 = cross-reference 정정 한정, ADR-008 본문 변경 영구 금지. 본문 변경 시 풀 3+1 합의 + ADR 권위 영역" |
2119:docs/phase0/mvp1-r-s1-framing-correction-brief.md:19:| 33번째 entry Reviewer R-S1 raw verify | Agent B + codex 일치 | ADR-008 본문 line 136 = §A.2 = "Hermes JSONL Export 검증" + "R1-2" + "§2.6.4" + "§2.6.2" 식별자 ADR-008 본문 0건 |
2120:docs/phase0/mvp1-r-s1-framing-correction-brief.md:31:| **scope** | (b2) R-S1 cross-reference 정정 + (b3) roadmap-mvp1 §3.6.3 line 290 framing 정정 (병렬 단일 sub-cycle, cross-reference 정정 영역 유사 = Agent C C-N-6 답습) |
2122:docs/phase0/mvp1-r-s1-framing-correction-brief.md:58:## §2 R-S1 cross-reference 정정 매트릭스 (R-3 multi-source 재기술 답습)
2134:docs/phase0/mvp1-r-s1-framing-correction-brief.md:97:| 6 | 523 | `ADR-008 §2.6.4 R1-2: 본문 변경 없음, GP-3 cross-reference 추가` | `ADR-008 cross-reference (차단조건 #1 + #6 + 부록 B): 본문 변경 없음, GP-3 cross-reference 추가 (33번째 entry R-S1 정정 답습)` |
2135:docs/phase0/mvp1-r-s1-framing-correction-brief.md:103:| 1 | 12 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 (저장 경로 secret 보호 권위)` | `ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 권위, 35번째 entry R-S1 정정 답습)` |
2136:docs/phase0/mvp1-r-s1-framing-correction-brief.md:105:| 3 | 390 | `ADR-008 §A.2 R1-2 + §2.6.2 R2-1 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건)` | `ADR-008 차단조건 #1 + #6 + 부록 B 답습 \| ✅ (cross-reference 답습 한정 — 본문 변경 0건, 35번째 entry R-S1 정정 답습)` |
2138:docs/phase0/mvp1-r-s1-framing-correction-brief.md:175:| 2 | R-S1 raw verify 답습 명문 (33번째 Reviewer + Agent B + codex 일치) + ADR-008 본문 §A.2 = "Hermes JSONL Export 검증" + R1-2 식별자 부재 cross-check | ✅ §2.1 |
2139:docs/architecture/implementation-runtime-roadmap-mvp1.md:137:| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 + R-4 + 본 §3 (36번째 entry R-S1 정정 답습) | ADR-008 차단조건 #4 + 부록 B + ADR-009 C-N §5 + ADR-011 + P1 v2 + 본 §4 (36번째 entry R-S1 정정 답습) |
2140:docs/architecture/implementation-runtime-roadmap-mvp1.md:143:> ⭐⭐⭐ **2026-05-27 발효 (32번째 entry)**: **GP-3 5/5 + GP-5 5/5 모두 충족 자격 자격 인정 + 사용자 명시 결정 = MVP-1 Implementation Evidence PASS *완전 발효* (α)**. 본 발효 = (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-6 답습).
2141:docs/architecture/implementation-runtime-roadmap-mvp1.md:205:| **ST-1** | **Hermes Dockerfile entrypoint stat 검증** (chmod 600 강제) | 컨테이너 시작 시 | ✅ 필요 (Hermes upstream Dockerfile 수정) | ❌ | 低 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
2142:docs/architecture/implementation-runtime-roadmap-mvp1.md:206:| **ST-2** | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지) | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅ | 中 (sidecar process 운영) | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
2143:docs/architecture/implementation-runtime-roadmap-mvp1.md:207:| **ST-3** | **docker secret 직접 사용** | 런타임 (file system 통한 노출 회피) | 부분 (docker-compose.yml 갱신) | ❌ | 低 | ADR-008 차단조건 #6 (Docker 격리) + GP-3 §5.3 답습 (36번째 entry R-S1 정정 답습) |
2144:docs/architecture/implementation-runtime-roadmap-mvp1.md:209:| **ST-5** | **ST-1 + ST-2 + ST-3 통합** (Defense in depth) | 시작 + 런타임 + file system | ✅ 필요 | ✅ | 中-高 | ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + GP-3 §5.3 통합 답습 (36번째 entry R-S1 정정 답습) |
2145:docs/architecture/implementation-runtime-roadmap-mvp1.md:283:| ADR-008 cross-reference 갱신 (차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011) | ADR-008 본문 답습 (cross-reference 한정, R-MVP1-PASS-2 영구 금지 답습) | ✅ 35번째 entry (b2) gov + backlog1 + 36번째 entry (b2-roadmap) roadmap-mvp1 본문 R-S1 정정 완료 답습 |
2146:docs/architecture/implementation-runtime-roadmap-mvp1.md:506:> ⭐⭐⭐ **2026-05-27 발효 완료 (32번째 entry, commit `(본 commit)`)**: 본 5/5 매트릭스 양 GP 모두 충족 자격 자격 인정 + 사용자 명시 결정 + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS 답습 = **MVP-1 Implementation Evidence PASS *완전 발효 (α)***. 답습 source: (b1) 4 sub-cycle (PC-1-T3 + S-3 + ST-2 + AR-3) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + 본 cycle 합의 (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). carry-over (PASS 효과 영향 0건): (b2) R-S1 cross-reference 정정 (별도 sub-cycle, ADR-008 본문 변경 0건 영구 의무 R-MVP1-PASS-2 답습) + PC-1-T3 PoC evidence 자율 수집 + ST-2 nightly actual run id 자율 수집 + paths-aware workflow audit (R-MVP1-PASS-8 답습 + R-6 BLOCKING 답습 = 다음 cycle 우선순위).
2147:docs/architecture/implementation-runtime-roadmap-mvp1.md:660:| **ST-3** | docker secret (저장 경로 isolation) | GP-3 저장 경로 secret 검출 (G3-1) | ADR-008 차단조건 #6 (Docker 격리) 답습 + Layer A §1.2 + Layer B §1.1 답습 (36번째 entry R-S1 정정 답습) | Vault HSM ST-4 미진입 (Backlog #7 분리) / entrypoint stat ST-1 / inotify ST-2 미진입 (Backlog #1 1.5차 보강 분리) |
2148:docs/architecture/implementation-runtime-roadmap-mvp1.md:827:| 2026-05-27 (32번째 entry) | ⭐⭐⭐ **MVP-1 Implementation Evidence PASS 완전 발효 (α)** — §2.2 (line 141 영역) + §3.6.3 (GP-3 합의 형태 권고 표) + §4.7.3 (GP-5 합의 형태 권고 표) + §5.1 (통합 PASS 권고) 각 영역에 "2026-05-27 발효 완료" 행 추가 | (b1) 4 sub-cycle 완료 (PC-1-T3 `3a63a5b` + S-3 `4451716` + ST-2 `1edc5bb` + AR-3 chain `7f57323`/`7c294bb`/`73ed20d`/`9837298`) + 31번째 entry 첫 PR (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`) 11/11 SUCCESS + mergeable CLEAN + main branch protection 7 contexts 발효 evidence + 본 cycle 풀 3+1 + 외부 LLM 1+ APPROVE WITH CONDITIONS (`docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md`, BLOCKING 6 + 권고 5 1pass 흡수). 본 흡수 = §2.2 + §3.6.3 + §4.7.3 + §5.1 + §9 갱신 한정 — §3 GP-3 / §4 GP-5 / §5.2~§5.5 / §6 / §7 본문 변경 0건. carry-over (PASS 효과 영향 0건): (b2) R-S1 + PC-1-T3 PoC 자율 + ST-2 nightly 자율 + paths-aware audit (R-6 BLOCKING 답습) |
2149:docs/architecture/implementation-runtime-roadmap-mvp1.md:837:**다음 단계** (2026-05-27 32번째 entry 후): ✅ (b) MVP-1 1.5차 보강 합의 완료 (24번째 entry) → ✅ (b1) 4 sub-cycle 완료 (PC-1-T3 + S-3 + ST-2 + AR-3) → ✅ (c) **Implementation Evidence PASS 완전 발효 완료** (32번째 entry, 본 commit) → ⏳ (D-5 재조정 R-6 BLOCKING 답습): paths-aware workflow audit (R-MVP1-PASS-8 답습) → (b2) R-S1 cross-reference 정정 + (b3) framing 정정 (병렬) → Markdown evidence 통합 (D-3 carry-over) → (b1-PC1-D6) bypass detection CI 통합 → PR #2 merge 결정 (사용자 자율) → (d) facade real → MVP-2 진입 자격 검토 (별도 합의 영역)
2150:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:3:> **본 brief v1.1 = (R4-evidence) brief v1 (`12a3191`, 381줄) 의 풀 3+1 합의 (`f7ed37d`, 346줄, APPROVE w/ COND + BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 9 verbatim 100% 반영 (R-21 답습 영구) / (2) R-S1~R-S5 정정 흡수 11+곳 / (3) 명명 일관성 통일 = "(R4-evidence)" 단일 + 후속 본문 정정 cycle = "**(R4-body)**" 변경 (R-S2 발효, (g1-N) chain 영구 종결 의무 답습 영구 framing 정합) / (4) §2.2 line 33 → **line 63** verbatim 정정 (R-S1 발효) / (5) §3.5 Phase 1 행 추가 (5-way framing, R-S5 발효) / (6) §11 v→v1.1 변경 일람 신규 / (7) 본 cycle = read-only analysis only (단 brief commit + raw report 단계 R-1 anchor 24회 sudo 1회 의무 자격 별도 분리 명문, R-S4 발효). 자동 다음 단계 진입 0건 (chain 영구 종결 의무 답습 영구).
2151:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:10:- **(R4-evidence) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-r4-framing-evidence-entry.md`, commit `f7ed37d`, 346줄, BLOCKING 9 + R-S1~R-S5 + 권고 16 + NOTE 15 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
2152:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:15:- **MVP-1 합의 보고서** (`docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`, R4 verbatim **line 63**, R-S1 발효 정정)
2153:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:25:1. MVP-1 합의 R4 본문 verbatim read (MVP-1 brief line 20/124~125/141 + MVP-1 합의 보고서 **line 63**, R-S1 발효 정정) + 현재 framing 명문
2154:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:62:  - F-2 ⭐⭐⭐: R-S1 완벽 raw evidence (Ollama 자체 standard copy + 별도 inode + content-addressable sha256)
2155:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:65:  - **R4 본문 verbatim (MVP-1 합의 보고서 line 63, R-S1 발효 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
2156:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:95:## 2. MVP-1 합의 R4 본문 verbatim (read-only, R-S1 발효 line 63 + R-S3 발효 nested quote 정직성)
2157:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:108:### 2.2 MVP-1 합의 보고서 R4 verbatim (R-S1 발효 line 63 정정)
2158:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:110:> **R4 행 verbatim (line 63, R-S1 발효 line 33 → line 63 정정 확정)**: "**R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM \"제외(#36821)\" → \"MVP-1 비채택, MVP-2 재검토\"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합"
2159:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:159:- **R-S1 발효 완벽 evidence**: **Ollama 자체 standard copy** ((h-OM) raw line 44 답습 영구, Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습)
2160:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:169:| Source | Ollama library (다른 conversion) | bartowski Q4_K_M | bartowski Q4_K_M | Ollama library blob | **(h) bartowski blob (R-S1 발효 Ollama 자체 standard copy)** |
2161:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:203:- **"동급" 단언 부적정성 자격 강함** (S1 confirmed + R-S1 완벽 raw evidence 답습 영구)
2162:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:213:  - Ollama **(h-OM) Qwen3-30B-A3B bartowski Modelfile** decode generation = **14.69 t/s** (R-S1 발효 standard copy 답습)
2163:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:238:| evidence 강도 (3 차원 a/b/c + 4 차원 격차 + model variant) | ⭐⭐⭐ HIGH (4-way + Phase 1 5-way confirmed, S1 + R-S1 답습 영구) |
2164:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:251:  - MVP-1 합의 보고서 R4 행 **line 63** 답습 (R-S1 발효 정정)
2165:docs/phase0/jarvis-mvp1-r4-framing-evidence-entry-brief.md:279:   - (h-O) ↔ (h-OM): source conversion lineage 변수 (R-S1 발효 Ollama 자체 standard copy)
2269:   100	- **`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`** (C-N 갱신 2026-05-09 후속 4 — P1 facade MVP 진입조건 명시 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference). 본 ADR-008 차단조건 #4 (provider 어댑터 추상화) 의 *Hermes PMO ↔ provider 분리* 권위 출처
2278:   109	- **`docs/decisions/ADR-012-evidence-ledger-protection.md`** (Evidence Ledger Protection — 본 ADR-008 차단조건 #2 (JSONL export 표준) 의 *Evidence Ledger 무결성* 강화 권위. 12 보호 원칙 + Layer 1~5 다층 강제 + RFC 8785 JCS + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5)
2352:/bin/bash -lc "rg -n \"RT-|E-[1-9]|Rollback|Evidence|R-S1|P-4|ADR-011 §2.1|\\(a\\)~\\(e\\)|Layer 4\" docs/phase0/mvp2-entry-brief.md" in /home/delangi/문서/project/category/AI_development_tool
2354:5:> **scope**: MVP-2 영역 (G2 GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 본격 진입 합의
2355:21:- (β) sub-수단 결정 cycle — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 별도 합의 또는 (α) 內 흡수
2356:22:- (γ) 분리 영역 결정 — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입
2357:28:1. **MVP-2 영역 정의 답습** — 51 entry audit brief §1.3 (GP-2 송신 redaction + G4 §4.4 Layer 4 CI 회귀 검증) 직접 답습 (§1)
2358:29:2. **51 entry audit brief 답습 cross-check** — 진입 자격 매트릭스 (GP-2 Entry 2/3 + Exit 2.5/5 / G4 §4.4 Layer 4 Entry 3/8 + Exit 1/5) 정합성 검증 (§2)
2362:55:| 12 | **G4 §4.4 Layer 4 sub-수단 결정** (L-1 / L-2 / L-3 / L-4 / L-5 中 채택) | 0건 ((β) 별도 cycle) |
2363:56:| 13 | **G4 §4.4 Layer 4 분리 영역 결정** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) | 0건 ((γ) 별도 cycle) |
2365:68:| 25 | G4 §4.4 Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 자동 결정 | 0건 (본 brief = Layer 4 한정, 다른 Layer = 별도 cycle 또는 의존 영역 자동) |
2366:69:| 26 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 자동 결정 | 0건 (MVP-3 ~ MVP-5 영역 답습) |
2371:93:| `implementation-runtime-roadmap.md §6` | 2026-05-09 (APPROVED) | 그룹 D (Order 4+5): G2 GP-3 + G2 GP-2. GP-3 = MVP-1 완료, **GP-2 잔존**. 그룹 C (Order 3 tie): G4 JSONL hash chain + JCS + Round-trip PoC (G4 §4.4 영역) | 본 cycle = 그룹 D 잔존 GP-2 진입 + 그룹 C G4 §4.4 Layer 4 진입 통합. |
2373:101:| **G4 §4.4 Layer 4 — CI 회귀 검증** | G4 | Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증 + canonical JSON 위반 검출 + timestamp monotonicity 검증 + R-6 workflow 답습 확장. MANDATORY 등급 (Layer 5 中 4번째, Layer 1+2+4 MANDATORY, Layer 3+5 RECOMMENDED MVP) | `provider-agnostic-memory-skill-design.md §4.4.1 line 649~653` (Layer 4 정의) + `ADR-012 §2.3` (다층 강제) + `ADR-012 §3.4` (timestamp monotonicity) |
2375:110:| **G4 §4.4 Layer 4 진입 자격** | provider-agnostic-memory-skill-design §4.4 line 624 (Layer 1~5 MANDATORY/RECOMMENDED 매트릭스) + ADR-012 §2.3 line 165 "Layer 1 MANDATORY 모든 환경" + line 182 "Layer 4 RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점" | **Layer 4 = MANDATORY 등급, MVP-2 진입 영역 채택** | **⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역. |
2376:114:→ **요약**: 본 (α) cycle = "MVP-2 영역 *진입* 합의" 한정 (수단 결정 = (β) 분리). 두 영역 모두 풀 3+1 + 외부 LLM 1+ + 사용자 명시 일관. R-S1 유형 잠재 risk (ADR-012 §2.3 line 182 verbatim 재확인) = §10 자기진단 명시 영역.
2380:155:### §2.2 G4 §4.4 Layer 4 — CI 회귀 검증 — 진입 자격
2381:161:| **목적** | Evidence Ledger 무결성 자동 회귀 검증 — Layer 1 (hash chain) + Layer 2 (history) + canonical JSON 위반 + timestamp monotonicity 위반 자동 검출 |
2382:163:| **메커니즘** | (L-1) Python stdlib 단독 (`hashlib.sha256` + `json.dumps(sort_keys=True, separators=(",",":"))`) + (L-2) RFC 8785 JCS Primary (`pyjcs` / `rfc8785`) + (L-3) Layer 4 R-6 workflow step + (L-4) L-1+L-3 병행 (MVP 권고) + (L-5) L-2+L-3 병행 (정식) |
2383:164:| **권위 출처** | provider-agnostic-memory-skill-design.md §4.4.1 line 649~653 (Layer 4 정의) + ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.7 (prev_hash 실패 처리) + §3.4 (timestamp monotonicity) |
2384:175:| Layer 4 CI step 실 구현 | ❌ gap | 실 구현 sub-cycle 영역 |
2385:183:✅ **G4 §4.4 Layer 4 영역 진입 발효 자격** — 본 (α) 합의 APPROVE 시점 발효
2386:185:✅ **(γ) 분리 영역 결정 cycle 진입 자격 발효** — Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 (별도 합의)
2389:192:❌ Layer 1 / Layer 2 / Layer 3 / Layer 5 영역 진입 결정 = (γ) 분리 영역 결정 cycle (Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 결정)
2391:202:| **목적** | GP-2 §4.6 산출 후보 (log file canary inject step) + G4 §4.4 Layer 4 (Layer 1+2 자동 회귀 + canonical 위반 + timestamp monotonicity step) **단일 R-6 workflow (`r2-canary.yml`) 확장 통합** |
2393:223:| # | 조건 | GP-2 (§2.1) | G4 §4.4 Layer 4 (§2.2) |
2396:235:- (γ) 분리 영역 결정 cycle → Layer 1+2 의존 영역 vs Layer 4 동시 결정
2402:259:| **G4 §4.4 Layer 4** | **풀 3+1 + 외부 LLM 1+** (본 (α)) | **(γ) 분리 영역 결정 = 풀 3+1** (Layer 1+2 의존 영역 우선 vs Layer 4 동시) + **(β) sub-수단 결정 = 풀 3+1** (L-1~L-5 中 L-4 MVP 권고, 51 brief §3.4 답습) + 실 구현 별도 sub-cycle | **풀 3+1 + 외부 LLM 1+ + 사용자 명시** (32 entry 답습) |
2404:270:| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴) |
2405:282:| G4 §4.4 Layer 4 | (1) 큰 결정 + (4) 잠재 R-S1 (Layer 4 vs Layer 5 혼동) + (5) 외부 LLM | 풀 3+1 + 외부 LLM 1+ |
2411:295:| RT-4 | hash chain middle entry tampering 검출 | G4 §4.4 Layer 4 | Layer 1 검증 실패 | ADR-012 §2.7 (`chain_violation_detected` ledger entry) |
2412:296:| RT-5 | canonical JSON 위반 검출 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL | ADR-012 §2.5 + §원칙 5/6 + R-6 답습 (`canonical_json_fallback` 또는 BLOCK) |
2413:297:| RT-6 | timestamp monotonicity 위반 | G4 §4.4 Layer 4 | Layer 4 CI step FAIL → BLOCK | ADR-012 §3.4 + R-6 답습 |
2426:321:| 2 | `g4_ledger_chain_verify_layer4_implementation` | G4 §4.4 Layer 4 | 동일 답습 |
2428:346:| 7 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 자동 진입 | MVP-3~MVP-5 영역 (별도 합의) |
2429:348:| 9 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit 영역 (R-S1 잠재 정정 영역 포함) |
2434:392:| 4 | 두 영역 (GP-2 + G4 §4.4 Layer 4) 진입 자격 평가 | 두 영역별 평가 본문 |
2436:395:| 7 | R-S1 잠재 risk 인식 (ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동) | §1.3 자기진단 영역 cross-reference 답습 |
2437:405:1. **(β) sub-수단 결정 cycle** — R-1/2/3/4/5 (GP-2) + L-1/2/3/4/5 (G4 §4.4 Layer 4) — 풀 3+1 합의
2438:406:   - 본 (α) 권고 (51 brief 답습): GP-2 = R-4 (R-1+R-2+R-3 병행) / G4 §4.4 Layer 4 = L-4 (L-1+L-3 병행 MVP)
2439:407:2. **(γ) 분리 영역 결정 cycle** — G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 — 풀 3+1 합의
2441:410:5. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008 차단조건 #1 보조 cross-reference 추가 + ADR-012 §2.2 event enum 신규 등록 + ADR-011 §8.5 후속 작업에 GP-2 등록 (R-S1 정정 영역 포함)
2445:457:- ADR-011 §8.5 후속 작업에 GP-2 + G4 §4.4 Layer 4 등록
2446:458:- **R-S1 정정 영역** (§1.3 ADR-012 §2.3 line 182 Layer 4 vs Layer 5 혼동 verbatim 재확인 + cross-reference 정정) — 본 (α) 합의 발효 후 사용자 명시 시 별도 cycle
2447:471:| **P-4** | **⚠️ R-S1 유형 잠재 risk 1 — ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험** | §1.3 G4 §4.4 Layer 4 항목 명시 + §4.3 trigger (4) 부분 발화 명시. 본 brief 발효 후 Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴, 권위 chain 다중 source 손상 확정 시 §9.5 별도 cycle 영역). 본 brief 의 Layer 4 정의 = G4 §4.4.1 line 649~653 답습 (Reviewer Read 확인 evidence 본 brief 작성 시점 read 완료) |
2448:474:| **P-7** | 두 영역 통합 진행이 GP-2 / G4 §4.4 Layer 4 *각각* 의 영역 특성 무시 위험 | §2.1 + §2.2 각각 별도 분석 + §3 매트릭스 별도 컬럼 + §4.2 발효 시점 합의 형태 권고 각각 명시 |
2449:480:**다음 단계**: 사용자 승인 → 외부 LLM 자격 옵션 결정 ((α) Claude tmux+codex 직접 호출 또는 (β) 사용자 직접 호출) → 외부 LLM 응답 capture → 풀 3+1 합의 (Agent A/B/C 3 병렬 독립 → Reviewer 통합 + R-S1 verify) → brief v1.1 1pass 흡수 보강 → SESSION + INDEX commit + push.
2485:2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
2546:### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요
2552:- ADR-012 §2.3 line 182: `Layer 4 — External anchor`
2553:- G4 §4.4.1 line 649: `Layer 4 — CI 회귀 검증`
2559:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
2563:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
2564:> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
2569:따라서 동일한 “Layer 4” 라벨이 서로 다른 의미를 갖습니다.
2573:- Layer 1: Hash chain
2576:- **Layer 4: CI 회귀 검증**
2581:- **ADR-012 §2.3**: 4-layer 모델, Layer 4 = External anchor
2582:- **ADR-012 §2.8 + G4 §4.4.1**: 5-layer 모델, Layer 4 = CI 회귀 검증, Layer 5 = External anchor
2588:brief가 G4 §4.4.1 line 649~653을 MVP-2 진입 대상 Layer 4 정의로 채택하는 것은 실무적으로 타당합니다.
2594:- MVP-2 진입 대상: **G4 §4.4.1 / ADR-012 §2.8 계열의 Layer 4 CI 회귀 검증**
2602:- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
2603:- “ADR-012 §2.3 line 182 = Layer 5 영역과 혼동 위험” → “ADR-012 §2.3 자체는 Layer 4를 External anchor로 명명하므로, G4 §4.4.1/ADR-012 §2.8의 5-layer 모델과 numbering divergence 발생”
2604:- “본 cycle은 G4 §4.4.1 line 649~653 및 ADR-012 §2.8 line 266~272를 MVP-2 Layer 4 CI 회귀 검증의 직접 권위로 사용한다”
2605:- “ADR-012 §2.3은 hash chain / append-only 원칙 권위로만 인용하고, Layer 4 numbering 권위로는 인용하지 않는다”
2674:51 entry audit 기준 G4 Layer 4는 `3/8 + 1 사용자 영역`입니다.
2680:다만 `G4 §4.4 Layer 4 영역 진입 발효 자격`이라는 표현은 독자가 “Layer 4 구현 착수 가능”으로 읽을 수 있습니다.
2684:- `G4 §4.4 Layer 4 planning/decision track 진입 권한 발효`
2686:- `Layer 1/hash chain, canonical corpus, genesis hash 의존성은 unresolved gap으로 유지`
2688:### N-3. RT-5의 `canonical_json_fallback 또는 BLOCK` 표현 보강 권고
2699:- `fallback canonicalizer used` → `canonical_json_fallback` ledger entry + reviewer/user review
2747:이번 MVP-2 entry brief는 R-1~R-5와 L-1~L-5 조합이 크고, G4 Layer 1+2 의존성도 있어 분리하는 것이 더 안전합니다.
2787:- §2.2: G4 §4.4 Layer 4 진입 자격
2791:- §10 P-4: R-S1 잠재 risk 자기진단
2803:> `ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험`
2831:### 4. GP-2 + G4 §4.4 Layer 4 진입 자격 평가
2833:**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**
2855:**G4 §4.4 Layer 4**
2859:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
2860:> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
2869:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
2871:따라서 “ADR-012 §2.3 + G4 §4.4.1”을 Layer 4 numbering 권위로 동시에 쓰면 충돌합니다.
2875:- Layer 4 CI 정의: G4 §4.4.1 + ADR-012 §2.8
2889:- Layer 1+2 의존 vs Layer 4 동시 = (γ)
2920:### 7. R-S1 잠재 risk 검증
2928:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
2932:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
2936:> `Layer 4: CI 회귀 검증`
2949:entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.
2951:## §5 R-S1 잠재 risk 검증 결과
2957:- `Layer 1 — Hash Chain (MANDATORY 모든 환경)`
2960:- `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
2964:- `Layer 4 — CI 회귀 검증 (MANDATORY)`
2965:- `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
2972:- `Layer 1: Hash chain`
2975:- `Layer 4: CI 회귀 검증`
2982:§2.3은 External anchor를 Layer 4로 둡니다.
2988:따라서 brief가 “G4 Layer 4 CI 회귀 검증”을 MVP-2 진입 대상으로 삼는 것은 가능합니다.
2994:- `ADR-012 §2.3` = hash chain / append-only 원칙 권위, 단 Layer 4 numbering 권위로는 사용 금지
2996:### §5.3 최종 R-S1 판정
2998:**R-S1 = CONFIRMED**
3003:- 동일 label “Layer 4”의 semantic collision
3008:1. brief v1.1에서 R-S1을 confirmed로 격상
3009:2. MVP-2 진입 대상 Layer 4를 `G4 §4.4.1 / ADR-012 §2.8` 기반으로 한정
3020:- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상
3059:2. **R-S1 Layer 4 충돌**은 잠재 risk가 아니라 실제 source divergence로 판정해야 합니다.
3120:### R-2. R-S1 Layer 4 충돌은 “잠재 risk”가 아니라 실제 source divergence로 격상 필요
3126:- ADR-012 §2.3 line 182: `Layer 4 — External anchor`
3127:- G4 §4.4.1 line 649: `Layer 4 — CI 회귀 검증`
3133:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
3137:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
3138:> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
3143:따라서 동일한 “Layer 4” 라벨이 서로 다른 의미를 갖습니다.
3147:- Layer 1: Hash chain
3150:- **Layer 4: CI 회귀 검증**
3155:- **ADR-012 §2.3**: 4-layer 모델, Layer 4 = External anchor
3156:- **ADR-012 §2.8 + G4 §4.4.1**: 5-layer 모델, Layer 4 = CI 회귀 검증, Layer 5 = External anchor
3162:brief가 G4 §4.4.1 line 649~653을 MVP-2 진입 대상 Layer 4 정의로 채택하는 것은 실무적으로 타당합니다.
3168:- MVP-2 진입 대상: **G4 §4.4.1 / ADR-012 §2.8 계열의 Layer 4 CI 회귀 검증**
3176:- “R-S1 잠재 risk” → “R-S1 confirmed source divergence”
3177:- “ADR-012 §2.3 line 182 = Layer 5 영역과 혼동 위험” → “ADR-012 §2.3 자체는 Layer 4를 External anchor로 명명하므로, G4 §4.4.1/ADR-012 §2.8의 5-layer 모델과 numbering divergence 발생”
3178:- “본 cycle은 G4 §4.4.1 line 649~653 및 ADR-012 §2.8 line 266~272를 MVP-2 Layer 4 CI 회귀 검증의 직접 권위로 사용한다”
3179:- “ADR-012 §2.3은 hash chain / append-only 원칙 권위로만 인용하고, Layer 4 numbering 권위로는 인용하지 않는다”
3248:51 entry audit 기준 G4 Layer 4는 `3/8 + 1 사용자 영역`입니다.
3254:다만 `G4 §4.4 Layer 4 영역 진입 발효 자격`이라는 표현은 독자가 “Layer 4 구현 착수 가능”으로 읽을 수 있습니다.
3258:- `G4 §4.4 Layer 4 planning/decision track 진입 권한 발효`
3260:- `Layer 1/hash chain, canonical corpus, genesis hash 의존성은 unresolved gap으로 유지`
3262:### N-3. RT-5의 `canonical_json_fallback 또는 BLOCK` 표현 보강 권고
3273:- `fallback canonicalizer used` → `canonical_json_fallback` ledger entry + reviewer/user review
3321:이번 MVP-2 entry brief는 R-1~R-5와 L-1~L-5 조합이 크고, G4 Layer 1+2 의존성도 있어 분리하는 것이 더 안전합니다.
3361:- §2.2: G4 §4.4 Layer 4 진입 자격
3365:- §10 P-4: R-S1 잠재 risk 자기진단
3377:> `ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험`
3405:### 4. GP-2 + G4 §4.4 Layer 4 진입 자격 평가
3407:**평가: GP-2 PASS / G4 PARTIAL WITH R-S1 BLOCKING**
3429:**G4 §4.4 Layer 4**
3433:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
3434:> `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
3443:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
3445:따라서 “ADR-012 §2.3 + G4 §4.4.1”을 Layer 4 numbering 권위로 동시에 쓰면 충돌합니다.
3449:- Layer 4 CI 정의: G4 §4.4.1 + ADR-012 §2.8
3463:- Layer 1+2 의존 vs Layer 4 동시 = (γ)
3494:### 7. R-S1 잠재 risk 검증
3502:> `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
3506:> `Layer 4 — CI 회귀 검증 (MANDATORY)`
3510:> `Layer 4: CI 회귀 검증`
3523:entry brief input 전에는 confirmed R-S1로 격상하고, 본 cycle이 사용하는 Layer numbering 권위를 명시해야 합니다.
3525:## §5 R-S1 잠재 risk 검증 결과
3531:- `Layer 1 — Hash Chain (MANDATORY 모든 환경)`
3534:- `Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)`
3538:- `Layer 4 — CI 회귀 검증 (MANDATORY)`
3539:- `Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증`
3546:- `Layer 1: Hash chain`
3549:- `Layer 4: CI 회귀 검증`
3556:§2.3은 External anchor를 Layer 4로 둡니다.
3562:따라서 brief가 “G4 Layer 4 CI 회귀 검증”을 MVP-2 진입 대상으로 삼는 것은 가능합니다.
3568:- `ADR-012 §2.3` = hash chain / append-only 원칙 권위, 단 Layer 4 numbering 권위로는 사용 금지
3570:### §5.3 최종 R-S1 판정
3572:**R-S1 = CONFIRMED**
3577:- 동일 label “Layer 4”의 semantic collision
3582:1. brief v1.1에서 R-S1을 confirmed로 격상
3583:2. MVP-2 진입 대상 Layer 4를 `G4 §4.4.1 / ADR-012 §2.8` 기반으로 한정
3594:- R-2: R-S1은 잠재 risk가 아니라 confirmed source divergence로 격상

exec
/bin/bash -lc "sed -n '140,300p' docs/decisions/ADR-012-evidence-ledger-protection.md" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |

**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).

**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.

### 2.3 Append-only 원칙 + Hash Chain (다층 강제)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)

**Layer 2 — Git append-only branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (Agent B C-4 권고)
- 1인 SPOF 완화 + 침해 후 발견 가능

### 2.4 Signed commit OR Git append commit (사용자 명시 답습)

**사용자 명시 결정 답습**: "signed commit 또는 git append commit (둘 중 하나) 의무".

**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.

**옵션** (사용자 결정 영역 — D-1):

| 옵션 | 정체성 | 적용 |
|-----|------|---|
| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 최소 = git append-only, signed = 권장 | 사용자 결정 |
| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
| **D-1C** (절충, Reviewer 권고) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |

**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.

### 2.5 RFC 8785 JCS Canonicalization (채택 + Fallback)

**Primary**: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증.

**구현 라이브러리 후보** (Agent C C-3 권고):
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무** (외부 LLM 2 C-6):
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시 의무**:
- `event: canonical_json_fallback` ledger entry 작성 의무
- Reviewer 알림 + 사용자 review 권장

### 2.6 Genesis Hash 정의

**MVP (schema_version 0.1) — 현 G4 §4.4 정의 유지**:

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

**0.2 진입 또는 multi-chain 도입 시 (외부 LLM 2 C-7)**:

```python
genesis_hash = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

**전이 절차**: 0.1 chain 의 첫 entry 는 MVP 정의로 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 schema_version) 생성, 기존 0.1 chain 은 read-only.

### 2.7 prev_hash 검증 실패 처리 (BLOCK + Manual Review)

**처리 절차** (4/5 합의 답습 — 합의 §2.2 #8):

1. **즉시 BLOCK** — import / export / migration 중단
2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험)
3. **새 violation entry append** — `event: chain_violation_detected` ledger entry 작성:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"chain_violation_detected","content":{"violation_type":"prev_hash_mismatch|hash_recalculation|history_rewrite","detected_at":"<ts>","affected_entry":"<id>","prev_hash_expected":"<sha256>","prev_hash_actual":"<sha256>"},...}
   ```
4. **사용자 명시 review 의무** — 자동 PASS 금지
5. **자동 revert 금지** (T3 위반 — ADR-011 §2.4)
6. **Dual write 금지** (silent failure 위험)

**검출 layer**:
- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
- Layer 2: pre-push hook (chain 전체 재검증)
- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)

### 2.8 Full Rewrite 방어 (다층)

**5 Layer 강제** (합의 §3.5 답습):

- **Layer 1**: Hash chain (middle entry tampering 차단)
- **Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
- **Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — 외부 LLM 2 §3.3)
- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag (Agent B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)

**1인 동일 호스트 SPOF 한계 명시** (외부 LLM 1 권고 5 직접 인용):

> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR 은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.

### 2.9 Round-trip Lossy 검출 (Tier-based)

**검증 PASS 조건** (4/5 합의 답습 — 합의 §3.3):

| Tier | 정체성 | PASS 조건 |
|-----|------|------|
| **Genesis (신규 chain)** | 첫 entry 작성 | (round-trip 무관) |
| **T2 (Skill/Memory promoted, 로컬)** | 로컬 promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실 BLOCK |

**Ledger entry 3 형식**:

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"<id>","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"<id>","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review-summary>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"<id>","target_provider":"openai","failure_reason":"chain_violation_detected|policy_loss|permission_loss|evidence_loss"},...}
```

**자동화 vs 사용자 review 분리**:
- `lost_fields` enumeration = 자동 (canonical JSON diff)
- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
- **의미 보존 review 자동화 절대 금지** (Agent A R-4)


codex
R-S1은 실제로 §2.3과 §2.8의 Layer numbering divergence가 확인됩니다. 마지막으로 PoC 시제의 “5 영역 모두 충족” 주장 자체를 파일 시스템과 테스트 fixture 수 기준으로 검증합니다.
exec
/bin/bash -lc "sed -n '1,260p' tools/jsonl_hash_chain.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
#!/usr/bin/env python3
"""JSONL ledger hash chain validator — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.2 (event 11번째 필드 17 enum) /
    §2.3 (Append-only + Hash Chain Layer 1) / §2.6 (Genesis Hash MVP) /
    §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.2 (11 필드) / §4.4 (hash chain)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §2 / §4.2
  - tools/canonical_json.py (Q1 합의 답습 — rfc8785 + jcs 병렬 cross-check)

핵심 강제 조건:
  - 11 필드 schema (type / scope / id / schema_version / ts / agent / event / content / evidence_refs / prev_hash / hash)
  - schema_version != "0.1" → BLOCK (ADR-012 §2.10 답습)
  - Genesis hash = sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6 MVP)
  - hash 계산 = sha256(canonical_json(entry - "hash" field))
  - prev_hash 검증 실패 = BLOCK + chain_violation_detected entry 자동 작성
  - violation_type 4종: prev_hash_mismatch / hash_recalculation / history_rewrite / genesis_mismatch
  - timestamp monotonicity: 본 entry ts >= prev_hash entry ts (ADR-012 §3.4)
  - T3 자동 정책 변경 금지 (ADR-011 §2.4) — 자동 revert 0건, BLOCK + manual

종료 코드:
  0 = 모든 검사 PASS
  1 = 1+ violation 검출
  2 = invalid input (parse 실패 등)
"""
from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import hashlib
import json
import sys
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

from canonical_json import (  # type: ignore[import-not-found]
    CanonicalizationError,
    CrossCheckMode,
    to_canonical,
)

REQUIRED_FIELDS: tuple[str, ...] = (
    "type",
    "scope",
    "id",
    "schema_version",
    "ts",
    "agent",
    "event",
    "content",
    "evidence_refs",
    "prev_hash",
    "hash",
)

ALLOWED_TYPES: tuple[str, ...] = ("memory", "skill", "meta")
ALLOWED_SCOPES: tuple[str, ...] = ("global", "project", "session")
ALLOWED_AGENTS: tuple[str, ...] = ("user", "claude-code", "hermes", "external_llm")
SUPPORTED_SCHEMA_VERSION: str = "0.1"


class ViolationType(str, Enum):
    """Chain violation 4종 (ADR-012 §2.7 답습)."""

    PREV_HASH_MISMATCH = "prev_hash_mismatch"
    HASH_RECALCULATION = "hash_recalculation"
    HISTORY_REWRITE = "history_rewrite"
    GENESIS_MISMATCH = "genesis_mismatch"


@dataclass
class Violation:
    """Single violation report."""

    entry_index: int
    entry_id: str
    violation_type: str  # ViolationType.value or "schema_*" / "monotonicity_*"
    detail: str


def compute_genesis_hash(scope: str, schema_version: str) -> str:
    """Genesis hash MVP — sha256("genesis:<scope>:<schema_version>") (ADR-012 §2.6).

    schema_version 0.2 이상 진입 시 별도 chain (별도 chain_id 또는 schema_version) — 별도 합의 영역.
    """
    return hashlib.sha256(f"genesis:{scope}:{schema_version}".encode("utf-8")).hexdigest()


def compute_entry_hash(entry: dict[str, Any]) -> str:
    """Entry hash = sha256(canonical_json(entry - "hash" field)).

    Q1 합의 답습 — runtime mode = PRIMARY_1_ONLY (rfc8785 단독), corpus 시점 cross-check 별도.
    """
    payload = {k: v for k, v in entry.items() if k != "hash"}
    result = to_canonical(payload, mode=CrossCheckMode.PRIMARY_1_ONLY)
    return result.sha256_hex


def parse_iso8601(s: str) -> dt.datetime:
    """ISO 8601 timestamp parse — 'Z' suffix 정규화."""
    if s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return dt.datetime.fromisoformat(s)


def validate_schema(entry: dict[str, Any], index: int) -> list[Violation]:
    """11 필드 schema validation."""
    vios: list[Violation] = []
    entry_id = str(entry.get("id", f"<index={index}>"))

    missing = [f for f in REQUIRED_FIELDS if f not in entry]
    if missing:
        vios.append(
            Violation(
                entry_index=index,
                entry_id=entry_id,
                violation_type="schema_missing_field",
                detail=f"missing required fields: {missing}",
            )
        )
        return vios

    if entry["type"] not in ALLOWED_TYPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_type", f"type={entry['type']!r} not in {ALLOWED_TYPES}")
        )
    if entry["scope"] not in ALLOWED_SCOPES:
        vios.append(
            Violation(index, entry_id, "schema_invalid_scope", f"scope={entry['scope']!r} not in {ALLOWED_SCOPES}")
        )
    if entry["agent"] not in ALLOWED_AGENTS:
        vios.append(
            Violation(index, entry_id, "schema_invalid_agent", f"agent={entry['agent']!r} not in {ALLOWED_AGENTS}")
        )
    if entry["schema_version"] != SUPPORTED_SCHEMA_VERSION:
        vios.append(
            Violation(
                index,
                entry_id,
                "schema_version_unsupported",
                f"schema_version={entry['schema_version']!r} != {SUPPORTED_SCHEMA_VERSION!r} (ADR-012 §2.10)",
            )
        )
    if not isinstance(entry["evidence_refs"], list):
        vios.append(
            Violation(index, entry_id, "schema_invalid_evidence_refs", "evidence_refs must be list")
        )
    if not isinstance(entry["content"], (dict, list, str, int, float, bool)) and entry["content"] is not None:
        vios.append(
            Violation(index, entry_id, "schema_invalid_content", "content must be JSON-serializable")
        )

    try:
        parse_iso8601(entry["ts"])
    except (ValueError, TypeError) as e:
        vios.append(Violation(index, entry_id, "schema_invalid_ts", f"ts parse error: {e}"))

    return vios


def validate_chain(entries: list[dict[str, Any]]) -> list[Violation]:
    """Genesis + prev_hash ↔ hash chain + timestamp monotonicity 검증."""
    vios: list[Violation] = []
    if not entries:
        return vios

    prev_ts: dt.datetime | None = None
    prev_hash_actual: str | None = None

    for i, entry in enumerate(entries):
        entry_id = str(entry.get("id", f"<index={i}>"))

        # Hash recalculation 검증
        try:
            recomputed = compute_entry_hash(entry)
        except CanonicalizationError as e:
            vios.append(
                Violation(i, entry_id, "schema_canonical_error", f"canonical_json failed: {e}")
            )
            continue

        if recomputed != entry.get("hash"):
            vios.append(
                Violation(
                    i,
                    entry_id,
                    ViolationType.HASH_RECALCULATION.value,
                    f"hash field={entry.get('hash')!r} != recomputed={recomputed!r}",
                )
            )

        # prev_hash 검증
        if i == 0:
            expected_genesis = compute_genesis_hash(entry["scope"], entry["schema_version"])
            if entry["prev_hash"] != expected_genesis:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.GENESIS_MISMATCH.value,
                        f"first entry prev_hash={entry['prev_hash']!r} != genesis={expected_genesis!r}",
                    )
                )
        else:
            if entry["prev_hash"] != prev_hash_actual:
                vios.append(
                    Violation(
                        i,
                        entry_id,
                        ViolationType.PREV_HASH_MISMATCH.value,
                        f"prev_hash={entry['prev_hash']!r} != prior entry hash={prev_hash_actual!r}",
                    )
                )

        # Timestamp monotonicity (ADR-012 §3.4)
        try:
            cur_ts = parse_iso8601(entry["ts"])
        except (ValueError, TypeError):
            cur_ts = None  # schema_invalid_ts 가 이미 등록됨
        if cur_ts is not None and prev_ts is not None and cur_ts < prev_ts:
            vios.append(
                Violation(
                    i,
                    entry_id,
                    "monotonicity_violation",
                    f"ts={entry['ts']!r} < prior ts (ADR-012 §3.4 monotonicity)",
                )
            )
        if cur_ts is not None:
            prev_ts = cur_ts

        # 다음 iteration 위해 hash field 값 (recompute 와 같으면 그대로, 아니면 chain 깨짐 → mismatch 보고됨)
        prev_hash_actual = entry.get("hash")

    return vios


def build_violation_entry(
    entries: list[dict[str, Any]],
    violations: list[Violation],
) -> dict[str, Any] | None:
    """chain_violation_detected ledger entry 자동 작성 (ADR-012 §2.7).

    Returns:
        새 ledger entry dict (caller 가 ledger 에 append 가능 형식) 또는 None (위반 0건)
    """
    if not violations:
        return None

    # 첫 violation 이 history_rewrite 가능성 ↔ 그 외 분류
    first_vio = violations[0]
    chain_violations = [
        v for v in violations
        if v.violation_type in {vt.value for vt in ViolationType}
    ]
    if not chain_violations:

exec
/bin/bash -lc "sed -n '1,240p' tools/canonical_json.py" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
#!/usr/bin/env python3
"""Canonical JSON (RFC 8785 JCS) — Group C PoC (G4 통합).

답습 출처:
  - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개)
  - docs/architecture/provider-agnostic-memory-skill-design.md §4.4.2 (Canonical JSON 보강)
  - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md §3 (사용자 명시 결정 갱신 — rfc8785 + jcs 병렬 cross-check)
  - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
  - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)

핵심 강제 조건:
  - Primary 1: rfc8785 (Trail of Bits, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Primary 2: jcs (titusz, Apache-2.0, RA-9 §B.2 11/11 sanity PASS)
  - Fallback: jq -S -c (POSIX 표준, ADR-012 §2.5 명시 답습)
  - cross-check 시점 = corpus 시점 강제 (TR-C-2 trigger 답습 — Q1 합의 D-1)
  - cross-check 시점 runtime = 본 PoC 호출자 결정 (Mode 옵션 제공, 기본 = Mode 1 단독 + corpus 시점 cross-check)
  - Fallback 사용 시 = `event: canonical_json_fallback` ledger entry 작성 의무 (caller 책임)

본 모듈 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) — POSIX + Python stdlib + provider-neutral PyPI 한정.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Any

try:
    import rfc8785  # Primary 1 (Trail of Bits)
except ImportError:
    rfc8785 = None  # type: ignore[assignment]

try:
    import jcs  # Primary 2 (titusz)
except ImportError:
    jcs = None  # type: ignore[assignment]


class CrossCheckMode(str, Enum):
    """Cross-check mode — Q1 합의 D-1 답습 (corpus 시점 강제 + runtime 호출자 결정).

    - PRIMARY_1_ONLY: rfc8785 단독 사용 (runtime 1× 권고)
    - PRIMARY_2_ONLY: jcs 단독 사용 (테스트/디버깅용)
    - CROSS_CHECK: rfc8785 + jcs 동시 호출, 출력 byte 동등성 + sha256 동등성 강제 (corpus 시점 권고)
    - FALLBACK_JQ: jq -S -c subprocess (Primary install 실패 시, canonical_json_fallback entry 의무)
    """

    PRIMARY_1_ONLY = "primary_1_only"
    PRIMARY_2_ONLY = "primary_2_only"
    CROSS_CHECK = "cross_check"
    FALLBACK_JQ = "fallback_jq"


class CanonicalizationError(Exception):
    """Canonical JSON 생성 실패 (NaN/Inf/cross-check mismatch 등)."""


class CrossCheckMismatchError(CanonicalizationError):
    """rfc8785 + jcs cross-check 출력 불일치 — TR-C-2 escalation trigger."""


@dataclass
class CanonicalResult:
    """Canonicalization 결과 + audit trail."""

    canonical: bytes
    sha256_hex: str
    mode_used: CrossCheckMode
    fallback_used: bool = False
    cross_check_passed: bool | None = None  # None = N/A, True/False = cross-check 결과


def _to_canonical_rfc8785(obj: Any) -> bytes:
    """Primary 1 — rfc8785 (Trail of Bits)."""
    if rfc8785 is None:
        raise CanonicalizationError("rfc8785 라이브러리 미설치 — `pip install rfc8785==0.1.4`")
    out = rfc8785.dumps(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jcs(obj: Any) -> bytes:
    """Primary 2 — jcs (titusz)."""
    if jcs is None:
        raise CanonicalizationError("jcs 라이브러리 미설치 — `pip install jcs==0.2.1`")
    out = jcs.canonicalize(obj)
    return out if isinstance(out, bytes) else out.encode("utf-8")


def _to_canonical_jq_fallback(obj: Any) -> bytes:
    """Fallback — jq -S -c subprocess.

    POSIX 표준 도구, ADR-012 §2.5 명시. 본 함수 호출 후 caller 는
    `event: canonical_json_fallback` ledger entry 작성 의무.
    """
    jq_path = shutil.which("jq")
    if jq_path is None:
        raise CanonicalizationError(
            "jq fallback 불가 — `jq` POSIX 도구 미설치 (apt install jq / brew install jq)"
        )
    input_json = json.dumps(obj, allow_nan=False).encode("utf-8")
    try:
        result = subprocess.run(
            [jq_path, "-S", "-c", "."],
            input=input_json,
            capture_output=True,
            check=True,
            timeout=30,
        )
    except subprocess.CalledProcessError as e:
        raise CanonicalizationError(
            f"jq fallback subprocess 실패 — rc={e.returncode} stderr={e.stderr.decode('utf-8', 'replace')[:200]}"
        ) from e
    out = result.stdout.rstrip(b"\n")
    return out


def to_canonical(obj: Any, mode: CrossCheckMode = CrossCheckMode.PRIMARY_1_ONLY) -> CanonicalResult:
    """Canonical JSON 생성 + audit trail.

    Args:
        obj: 입력 Python object (dict / list / str / int / float / bool / None)
        mode: CrossCheckMode (기본 PRIMARY_1_ONLY — rfc8785 단독, runtime 1× 권고)

    Returns:
        CanonicalResult (canonical bytes + sha256 hex + mode used + fallback/cross-check flag)

    Raises:
        CanonicalizationError: NaN/Inf reject 또는 라이브러리 미설치 또는 jq 실패
        CrossCheckMismatchError: CROSS_CHECK 모드에서 rfc8785 ↔ jcs 출력 불일치 (TR-C-2 trigger)
    """
    fallback_used = False
    cross_check_passed: bool | None = None

    if mode == CrossCheckMode.PRIMARY_1_ONLY:
        canonical = _to_canonical_rfc8785(obj)
    elif mode == CrossCheckMode.PRIMARY_2_ONLY:
        canonical = _to_canonical_jcs(obj)
    elif mode == CrossCheckMode.CROSS_CHECK:
        out_p1 = _to_canonical_rfc8785(obj)
        out_p2 = _to_canonical_jcs(obj)
        if out_p1 != out_p2:
            raise CrossCheckMismatchError(
                f"rfc8785 ↔ jcs cross-check 불일치 — TR-C-2 escalation. "
                f"rfc8785={out_p1[:80]!r} jcs={out_p2[:80]!r}"
            )
        canonical = out_p1
        cross_check_passed = True
    elif mode == CrossCheckMode.FALLBACK_JQ:
        canonical = _to_canonical_jq_fallback(obj)
        fallback_used = True
    else:
        raise CanonicalizationError(f"알 수 없는 mode: {mode}")

    sha256_hex = hashlib.sha256(canonical).hexdigest()
    return CanonicalResult(
        canonical=canonical,
        sha256_hex=sha256_hex,
        mode_used=mode,
        fallback_used=fallback_used,
        cross_check_passed=cross_check_passed,
    )


def _cli() -> int:
    """CLI — corpus 회귀 + cross-check + fallback 동등성 검증."""
    p = argparse.ArgumentParser(
        description="Canonical JSON (RFC 8785 JCS) — Group C PoC validator"
    )
    p.add_argument(
        "--mode",
        choices=[m.value for m in CrossCheckMode],
        default=CrossCheckMode.CROSS_CHECK.value,
        help="Cross-check mode (default: cross_check)",
    )
    p.add_argument(
        "--input",
        type=str,
        default="-",
        help="입력 JSON 파일 경로 (- = stdin)",
    )
    p.add_argument(
        "--expected-canonical",
        type=str,
        default=None,
        help="기대 canonical 출력 파일 (있으면 byte 비교)",
    )
    p.add_argument(
        "--expected-sha256",
        type=str,
        default=None,
        help="기대 sha256 hex 파일 (있으면 비교)",
    )
    p.add_argument(
        "--verify-fallback-equiv",
        action="store_true",
        help="jq fallback 출력과 byte 동등성 검증",
    )
    args = p.parse_args()

    try:
        if args.input == "-":
            input_text = sys.stdin.read()
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                input_text = f.read()
        obj = json.loads(input_text)
    except (OSError, json.JSONDecodeError) as e:
        print(f"INPUT_ERROR: {e}", file=sys.stderr)
        return 2

    try:
        result = to_canonical(obj, mode=CrossCheckMode(args.mode))
    except CrossCheckMismatchError as e:
        print(f"CROSS_CHECK_MISMATCH: {e}", file=sys.stderr)
        return 3
    except CanonicalizationError as e:
        print(f"CANONICAL_ERROR: {e}", file=sys.stderr)
        return 4

    sys.stdout.buffer.write(result.canonical)
    sys.stdout.buffer.write(b"\n")
    print(
        f"# mode={result.mode_used.value} sha256={result.sha256_hex} "
        f"fallback_used={result.fallback_used} cross_check_passed={result.cross_check_passed}",
        file=sys.stderr,
    )

    rc = 0

    if args.expected_canonical:
        try:
            with open(args.expected_canonical, "rb") as f:
                expected = f.read().rstrip(b"\n")
        except OSError as e:
            print(f"EXPECTED_CANONICAL_READ_ERROR: {e}", file=sys.stderr)

exec
/bin/bash -lc "find tests/canonical -maxdepth 2 -type f | sort | wc -l && find tests/canonical -maxdepth 2 -type f | sort | sed -n '1,80p'" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
72
tests/canonical/array/01.expected.canonical
tests/canonical/array/01.expected.sha256
tests/canonical/array/01.input.json
tests/canonical/array/02.expected.canonical
tests/canonical/array/02.expected.sha256
tests/canonical/array/02.input.json
tests/canonical/array/03.expected.canonical
tests/canonical/array/03.expected.sha256
tests/canonical/array/03.input.json
tests/canonical/escape/01.expected.canonical
tests/canonical/escape/01.expected.sha256
tests/canonical/escape/01.input.json
tests/canonical/escape/02.expected.canonical
tests/canonical/escape/02.expected.sha256
tests/canonical/escape/02.input.json
tests/canonical/escape/03.expected.canonical
tests/canonical/escape/03.expected.sha256
tests/canonical/escape/03.input.json
tests/canonical/hash_stability/01.expected.canonical
tests/canonical/hash_stability/01.expected.sha256
tests/canonical/hash_stability/01.input.json
tests/canonical/hash_stability/02.expected.canonical
tests/canonical/hash_stability/02.expected.sha256
tests/canonical/hash_stability/02.input.json
tests/canonical/hash_stability/03.expected.canonical
tests/canonical/hash_stability/03.expected.sha256
tests/canonical/hash_stability/03.input.json
tests/canonical/key_ordering/01.expected.canonical
tests/canonical/key_ordering/01.expected.sha256
tests/canonical/key_ordering/01.input.json
tests/canonical/key_ordering/02.expected.canonical
tests/canonical/key_ordering/02.expected.sha256
tests/canonical/key_ordering/02.input.json
tests/canonical/key_ordering/03.expected.canonical
tests/canonical/key_ordering/03.expected.sha256
tests/canonical/key_ordering/03.input.json
tests/canonical/lossy/01.expected.canonical
tests/canonical/lossy/01.expected.sha256
tests/canonical/lossy/01.input.json
tests/canonical/lossy/02.expected.canonical
tests/canonical/lossy/02.expected.sha256
tests/canonical/lossy/02.input.json
tests/canonical/lossy/03.expected.canonical
tests/canonical/lossy/03.expected.sha256
tests/canonical/lossy/03.input.json
tests/canonical/nested/01.expected.canonical
tests/canonical/nested/01.expected.sha256
tests/canonical/nested/01.input.json
tests/canonical/nested/02.expected.canonical
tests/canonical/nested/02.expected.sha256
tests/canonical/nested/02.input.json
tests/canonical/nested/03.expected.canonical
tests/canonical/nested/03.expected.sha256
tests/canonical/nested/03.input.json
tests/canonical/number/01.expected.canonical
tests/canonical/number/01.expected.sha256
tests/canonical/number/01.input.json
tests/canonical/number/02.expected.canonical
tests/canonical/number/02.expected.sha256
tests/canonical/number/02.input.json
tests/canonical/number/03.expected.canonical
tests/canonical/number/03.expected.sha256
tests/canonical/number/03.input.json
tests/canonical/unicode/01.expected.canonical
tests/canonical/unicode/01.expected.sha256
tests/canonical/unicode/01.input.json
tests/canonical/unicode/02.expected.canonical
tests/canonical/unicode/02.expected.sha256
tests/canonical/unicode/02.input.json
tests/canonical/unicode/03.expected.canonical
tests/canonical/unicode/03.expected.sha256
tests/canonical/unicode/03.input.json

exec
/bin/bash -lc "wc -c .github/workflows/g4-hash-chain.yml .github/workflows/history-anchor-verifier.yml .github/workflows/rewrite-defense.yml && sed -n '1,220p' .github/workflows/g4-hash-chain.yml" in /home/delangi/문서/project/category/AI_development_tool
 succeeded in 0ms:
10652 .github/workflows/g4-hash-chain.yml
19094 .github/workflows/history-anchor-verifier.yml
16454 .github/workflows/rewrite-defense.yml
46200 total
# G4 JSONL Hash Chain + RFC 8785 JCS + Round-trip — Group C PoC
#
# 답습 출처:
#   - docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md (본 PoC 사양 §6)
#   - docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md (Q1 풀 3+1 합의 17 조건)
#   - docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md (Q2/Q3 단축 합의 6 조건)
#   - docs/decisions/ADR-012-evidence-ledger-protection.md §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증)
#   - docs/architecture/provider-agnostic-memory-skill-design.md §4.4 (hash chain) + §4.6 (round-trip)
#   - .github/workflows/evidence-pass-gate.yml (Group B 시제 직접 답습)
#
# 본 workflow 의 양방향 검증:
#   - corpus 24 회귀 (Primary 1 rfc8785 + Primary 2 jcs cross-check + sha256 일관성)
#   - NaN/Inf reject 2건 (양 라이브러리 모두 raise 검증)
#   - PASS fixture × 2: jsonl_hash_chain.py rc=0
#   - FAIL fixture × 4: jsonl_hash_chain.py rc=1 + 4 violation_type cover
#   - Round-trip PASS fixture: jsonl_roundtrip.py rc=0 (T2 strict)
#
# 본 PoC 는 G4 *부분 충족 시제* 한정 — G4 전체 PASS 권한 0건 (사용자 명시 답습).
name: G4 Hash Chain + JCS

on:
  push:
    branches:
      - main
      - develop
      - "feature/**"
    paths:
      - "tools/canonical_json.py"
      - "tools/jsonl_hash_chain.py"
      - "tools/jsonl_roundtrip.py"
      - "tests/canonical/**"
      - "tests/fixtures/jsonl_ledger/**"
      - ".github/workflows/g4-hash-chain.yml"
      - "requirements-dev.txt"
  pull_request:
    branches:
      - main
      - develop

permissions:
  contents: read

jobs:
  enforce:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    env:
      PYTHONPATH: tools
    steps:
      - name: Checkout
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Install jq (POSIX fallback)
        run: |
          sudo apt-get update -qq
          sudo apt-get install -y jq
          jq --version

      - name: Install Primary 1 + Primary 2 (Q1 합의 R-A2 답습)
        run: |
          python -m pip install --upgrade pip
          # 본 PoC 한정 의존만 설치 (import-linter 등 G2 전용 dep 제외)
          pip install rfc8785==0.1.4 jcs==0.2.1
          python -c "import rfc8785, jcs; print('rfc8785:', rfc8785.__file__); print('jcs:', jcs.__file__)"

      - name: Corpus regression — Primary 1 (rfc8785) byte + sha256
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            exp_sha256="${base}.expected.sha256"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
                  --expected-canonical "$exp_canonical" \
                  --expected-sha256 "$exp_sha256" >/dev/null 2>err.log; then
              echo "::error::Primary 1 regression FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "Primary 1 corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::Primary 1 (rfc8785) corpus regression: $fail / $total cases failed"
            exit 1
          fi

      - name: Corpus regression — Primary 2 (jcs) cross-check (TR-C-2 답습)
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            # Primary 2 단독 + expected 비교 (Q1 합의 D-1 — corpus 시점 cross-check 강제)
            if ! python tools/canonical_json.py --mode primary_2_only --input "$inp" \
                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
              echo "::error::Primary 2 regression FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "Primary 2 corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::Primary 2 (jcs) corpus regression: $fail / $total cases failed (TR-C-2 escalation)"
            exit 1
          fi

      - name: Corpus regression — cross_check mode (Primary 1 ↔ Primary 2 byte equivalence)
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode cross_check --input "$inp" \
                  --expected-canonical "$exp_canonical" >/dev/null 2>err.log; then
              echo "::error::cross_check FAIL: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "cross_check corpus: ${total} cases, ${fail} fail"
          if [ "$fail" -ne 0 ]; then
            echo "::error::cross_check corpus: $fail / $total cases failed (TR-C-2 escalation)"
            exit 1
          fi

      - name: Fallback equivalence — jq -S -c vs Primary 1
        run: |
          set -e
          fail=0
          total=0
          for inp in tests/canonical/*/*.input.json; do
            base="${inp%.input.json}"
            exp_canonical="${base}.expected.canonical"
            total=$((total + 1))
            if ! python tools/canonical_json.py --mode primary_1_only --input "$inp" \
                  --expected-canonical "$exp_canonical" \
                  --verify-fallback-equiv >/dev/null 2>err.log; then
              echo "::warning::jq fallback equivalence DIFF: $inp"
              cat err.log
              fail=$((fail + 1))
            fi
          done
          rm -f err.log
          echo "jq fallback equivalence: ${total} cases, ${fail} differ"
          # jq fallback 동등성 실패는 warning 한정 (ADR-012 §2.5 — `Fallback 사용 빈도 > 10%` 별도 합의 trigger 답습)

      - name: NaN/Inf reject (Q1 합의 C-B8 + 본 합의 C-Q2 답습)
        run: |
          python - <<'PY'
          import sys
          import rfc8785, jcs
          fail = 0
          for label, val in [("nan", float("nan")), ("inf", float("inf")), ("-inf", float("-inf"))]:
              for libname, fn in [("rfc8785", lambda v: rfc8785.dumps({"n": v})),
                                  ("jcs", lambda v: jcs.canonicalize({"n": v}))]:
                  try:
                      fn(val)
                      print(f"FAIL: {libname} accepted {label} (RFC 8785 §3.2.2.2 violation)")
                      fail += 1
                  except (ValueError, Exception) as e:
                      print(f"OK: {libname} rejected {label}: {type(e).__name__}")
          sys.exit(1 if fail else 0)
          PY

      - name: PASS fixture — jsonl_hash_chain rc=0 (× 2)
        run: |
          set -e
          for f in tests/fixtures/jsonl_ledger/pass/*.jsonl; do
            set +e
            python tools/jsonl_hash_chain.py "$f"
            rc=$?
            set -e
            if [ "$rc" -ne 0 ]; then
              echo "::error::PASS fixture $f returned rc=$rc (expected 0)"
              exit 1
            fi
          done
          echo "PASS fixtures verified (rc=0 for all)"

      - name: FAIL fixture — jsonl_hash_chain rc=1 + 4 violation_type cover
        run: |
          set -e
          # Expected violation_type per fixture (4 패턴 cover 강제)
          declare -A EXPECTED=(
            [prev_hash_mismatch.jsonl]=prev_hash_mismatch
            [hash_recalculation.jsonl]=hash_recalculation
            [missing_event_field.jsonl]=schema_missing_field
            [genesis_mismatch.jsonl]=genesis_mismatch
          )
          for f in tests/fixtures/jsonl_ledger/fail/*.jsonl; do
            name=$(basename "$f")
            expected="${EXPECTED[$name]:-}"
            set +e
            python tools/jsonl_hash_chain.py "$f" 2> chain_out.txt
            rc=$?
            set -e
            cat chain_out.txt
            if [ "$rc" -ne 1 ]; then
              echo "::error::FAIL fixture $name returned rc=$rc (expected 1)"
              exit 1
            fi
            if [ -n "$expected" ] && ! grep -q "type=$expected" chain_out.txt; then
              echo "::error::FAIL fixture $name missing violation_type=$expected"

codex
## 검토자 / Vendor

- 검토자: 외부 LLM 검토자, cross-vendor blind review
- 응답 vendor: **OpenAI / codex CLI**
- 본 cycle 풀 3+1 Agent vendor: **Anthropic Claude**
- cross-vendor 조건: **충족**

## 직접 검토한 Working Directory 자료

- `docs/phase0/mvp2-gamma-layer-separation-brief.md`
- `docs/phase0/mvp2-entry-brief.md`
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- `docs/external-review/2026-05-28-mvp2-entry-codex-response.md`
- `docs/architecture/provider-agnostic-memory-skill-design.md`
- `docs/decisions/ADR-012-evidence-ledger-protection.md`
- `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`
- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`

## §0 총평

**판정: APPROVE WITH CONDITIONS**

본 brief v1은 `(γ) MVP-2 G4 §4.4 Layer 분리 영역 결정`의 입력 자료로 대체로 적격합니다.

핵심 이유는 다음과 같습니다.

- brief §0.2 / §0.3 / §0.4가 본 cycle의 권위 한계를 명확히 분리합니다.
- brief §1.2가 52 entry §2.2.4의 4 대안 `(γ-a/b/c/d)`를 직접 답습합니다.
- brief §2.1~§2.4가 각 대안의 의존 chain, 장단점, PASS 발효 시점 차이를 비교합니다.
- brief §2.5가 PoC 시제와 PASS 시제를 분리합니다.
- brief §3이 ADR-011 §2.1 `(a)~(d)` 4조건과 `(e)` 후속 운영조건을 각 대안별로 재매핑합니다.
- brief §5가 Rollback Trigger / Evidence를 “후보 채택”으로 제한합니다.
- brief §5.1 RT-γ-6 및 §9.4가 R-S1 후행 영향을 별도 cycle로 보존합니다.

다만 **추천 순위 표기 내부 불일치**가 있습니다.

brief §2.6 표 안에서는 `(γ-a)`가 “권고 (1)”, `(γ-c)`가 “권고 (2)”로 표기되어 있습니다.

그런데 같은 §2.6의 결론 문장 및 사용자 제공 cycle 개요는 **`(γ-c) 1순위 + (γ-a) 2순위`**입니다.

이는 본 cycle이 “4 대안 中 채택 결정”을 위한 입력 자료라는 점에서 의사결정 입력을 혼선시킬 수 있으므로, 최종 합의 입력 전에는 반드시 정정되어야 합니다.

따라서 **APPROVE WITH CONDITIONS**입니다.

## §1 BLOCKING 1건

### R-1. §2.6 권고 순위 표기 불일치 정정 필요

**위치**

- `docs/phase0/mvp2-gamma-layer-separation-brief.md` §2.6

**문제**

§2.6 권고 매트릭스 표는 다음처럼 읽힙니다.

- `(γ-a)` 본 brief 권고: `권고 (1) — 안전 + 의존 답습`
- `(γ-c)` 본 brief 권고: `권고 (2) — defense-in-depth + 효율`

하지만 바로 아래 결론 문장은 다음 방향입니다.

- `본 brief 권고 ... (γ-c) Layer 1+2+4 동시 ... 1순위 + (γ-a) ... 2순위`

사용자 제공 cycle 개요도 동일하게 `(γ-c) 1순위 + (γ-a) 2순위`를 전제합니다.

**영향**

본 cycle은 수단 구현이 아니라 **4 대안 채택 결정 cycle**입니다.

따라서 추천 순위 표기가 서로 다르면, 후속 풀 3+1 합의에서 다음 두 해석이 충돌합니다.

- 해석 1: 표 기준 `(γ-a)` 1순위
- 해석 2: 결론 문장 기준 `(γ-c)` 1순위

이는 구현 발효를 만들지는 않지만, **결정 입력 자격**에는 직접 영향을 줍니다.

**요구 정정**

둘 중 하나로 통일해야 합니다.

본 brief 및 사용자 cycle 개요의 일관된 방향을 기준으로 하면 권장 정정은 다음입니다.

| 대안 | 정정 권고 |
|---|---|
| `(γ-c)` | `권고 (1) — defense-in-depth + 효율` |
| `(γ-a)` | `권고 (2) — 안전 + 의존 답습` |

**정정 후 판정**

이 1건이 정정되면 본 brief는 `(γ)` 결정 입력 자료로 **APPROVE 가능**합니다.

## §2 권고 6건

### N-1. PoC 시제 cross-check에서 “local evidence”와 “remote/admin evidence”를 분리 권고

brief §2.5는 Layer 2 항목에 다음을 포함합니다.

- branch protection rule
- `denyNonFastForwards`
- base branch 대비 JSONL line deletion / rewrite 감지

working directory에서 직접 확인 가능한 것은 주로 다음입니다.

- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`

반면 GitHub branch protection rule 및 remote `denyNonFastForwards` 적용 여부는 working directory 파일만으로는 완전 검증되지 않습니다.

따라서 §2.5의 Layer 2 row는 다음처럼 분리하는 편이 더 정확합니다.

- local PoC evidence: workflow / script 존재 및 내용
- remote/admin evidence: branch protection / non-fast-forward 차단 설정 확인 필요

이는 blocking은 아닙니다.

brief가 “PoC 시제”와 “PASS 시제”를 분리하고 있기 때문입니다.

### N-2. “5 영역 모두 충족” 표현을 artifact 기준과 layer 기준으로 나누는 편이 안전

사용자 검토 의무는 PoC 시제 cross-check를 “5 영역”이라고 표현하지만, 괄호 안 artifact는 사실상 다음 4 묶음입니다.

- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`
- `.github/workflows/g4-hash-chain.yml`

brief §2.5는 이를 5 row로 재구성합니다.

- Layer 1 hash chain
- Layer 2 Git append-only
- canonical JSON test corpus
- genesis hash
- Layer 4 CI regression

이 재구성은 타당하지만, 독자가 artifact 수와 evidence 영역 수를 혼동할 수 있습니다.

권고 문구:

- “artifact 기준 4 묶음 + evidence 영역 기준 5 row”

### N-3. `(γ-b)`는 “자동 동시”보다 “implicit bundled scope” 위험을 더 선명히 쓰는 편이 좋음

brief §2.2는 `(γ-b)`를 다음처럼 정의합니다.

- Layer 4 단독 진입
- Layer 1+2 = 의존 영역 자동 동시 진입

평가는 대체로 정확합니다.

다만 위험은 단순히 “evidence 분리 미명확”이 아니라, 합의 문서상으로는 Layer 4 단독처럼 보이지만 실제로는 Layer 1+2+4가 묶이는 **implicit bundled scope**입니다.

권고 문구:

- `(γ-b)`는 의존 chain은 만족하지만, Layer 1+2의 evidence namespace가 Layer 4 evidence에 흡수될 위험이 있으므로 후속 PASS evidence template에서 layer별 subsection을 강제해야 한다.

### N-4. `(γ-d)`는 “사실상 `(γ-a)`와 동등”보다 “Layer 4 PASS 선발효 불가”를 주 문장으로 두는 편이 명확

brief §2.4.4는 다음 결론을 냅니다.

- `(γ-d) = 사실상 (γ-a) 와 동등`

이 판단은 방향상 맞습니다.

다만 `(γ-d)`의 본질적 결함은 “동등성”보다 먼저 다음입니다.

- Layer 4 PASS는 Layer 1+2 PASS 없이 선발효할 수 없음

따라서 권고 문구:

- `(γ-d)`가 채택되더라도 Layer 4 PASS 선발효는 금지되며, Layer 1+2 PASS 선행 또는 동시 evidence가 없으면 `(γ-d)`의 Layer 4 cycle은 planning-only로 제한된다.

### N-5. RT-γ-6은 “후행 영향”뿐 아니라 “PASS 전 선행/동시 정정 후보”로도 남겨야 함

brief §5.1 RT-γ-6은 R-S1 cross-reference 정정 후행 영향을 잘 보존합니다.

52 entry §9.5에는 MVP-2 Implementation Evidence PASS 발효 시점에 R-S1 정정이 선행 또는 동시 의무 영역으로 다뤄질 수 있다는 취지가 있습니다.

따라서 본 brief에도 다음 문장을 추가하면 더 안전합니다.

- R-S1 정정은 본 `(γ)` cycle의 자동 진입 대상은 아니나, MVP-2 Implementation Evidence PASS 발효 시점에는 선행 또는 동시 정정 필요성이 재평가되어야 한다.

### N-6. 외부 LLM 1+ 권고와 cross-vendor 비협상 조건의 관계를 더 짧게 고정 권고

brief §4.1 / §7.1은 외부 LLM 1+를 “권고 / 사용자 영역 결정”으로 둡니다.

사용자 지시에서는 이번 검토 자체가 cross-vendor 충족 조건입니다.

따라서 본 cycle 기록에는 다음을 명시하면 충분합니다.

- 본 외부 검토 응답은 OpenAI codex CLI이고, 풀 3+1 Agent vendor는 Anthropic Claude이므로 헌법 5조-2 Provider Liquidity cross-vendor 요건을 충족한다.

## §3 NOTE 5건

### NOTE-1. brief v1 직접 읽기 evidence

직접 확인한 brief 문구 / 영역은 다음입니다.

- §0.2: “본 brief 가 하는 것”
- §0.3: “본 brief 가 하지 않는 것”
- §1.2: `(γ-a/b/c/d)` 4 대안 정의
- §2.4.4: `(γ-d)` 모순 risk
- §2.5: PoC 시제 답습 cross-check
- §3: ADR-011 4조건 + `(e)` 운영조건 매트릭스
- §5.1: RT-γ-1~RT-γ-6
- §8.1: 다음 단계, 사용자 결정 영역
- §10: 자기진단 P-1~P-7

직접 인용 가능한 핵심 문구:

> `본 cycle = 4 대안 中 채택 결정 (γ-a/b/c/d 中 사용자 명시 + 풀 3+1 합의)`

> `Layer 4 = "Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증"`

> `PoC 시제 충족 / PASS 시제 미충족`

> `Rollback Trigger / Evidence *후보 채택*`

### NOTE-2. ADR-011 §2.1 확인 결과

ADR-011 §2.1은 실제로 `(a)~(d)` 4조건입니다.

- `(a)` 동등 이상의 보안 결과
- `(b)` 격리 환경 PoC로 실증
- `(c)` ADR 권위로 명시
- `(d)` 자동 회귀 검증 경로 확보

`(e)`는 ADR-011 §2.1의 원조건이 아니라 후속 합의 APPROVE 운영조건으로 다루는 것이 맞습니다.

brief §3의 framing은 이 정정을 반영하고 있습니다.

### NOTE-3. G4 §4.4.1 Layer 정의 확인 결과

`provider-agnostic-memory-skill-design.md` §4.4.1은 5-layer 모델입니다.

- Layer 1: Hash Chain
- Layer 2: Git Append-only Branch
- Layer 3: Signed Commit
- Layer 4: CI 회귀 검증
- Layer 5: External Anchor

특히 Layer 4는 다음 의미입니다.

- Layer 1 + Layer 2 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증
- R-6 workflow 답습 확장

따라서 Layer 4는 Layer 1+2의 독립 대체물이 아니라 **Layer 1+2를 대상으로 하는 regression layer**입니다.

### NOTE-4. ADR-012 R-S1 확인 결과

ADR-012 §2.3은 4-layer 모델로 보이며, Layer 4를 External anchor로 둡니다.

ADR-012 §2.8은 5-layer rewrite 방어 모델로 보이며, Layer 4를 CI 회귀 검증, Layer 5를 External anchor로 둡니다.

따라서 R-S1은 실제 divergence입니다.

brief는 이를 다음처럼 적절히 처리합니다.

- G4 §4.4.1 + ADR-012 §2.8 = Layer numbering 권위
- ADR-012 §2.3 = append-only / hash chain 원칙 권위
- cross-reference 정정 = 별도 cycle

이 처리는 타당합니다.

### NOTE-5. PoC 파일 확인 결과

확인 결과:

- `tools/jsonl_hash_chain.py`는 genesis hash 함수와 `prev_hash_mismatch`, `hash_recalculation`, `history_rewrite`, `genesis_mismatch` 4 violation type을 포함합니다.
- `tools/canonical_json.py`는 `rfc8785`, `jcs`, `jq -S -c` fallback, cross-check mode를 포함합니다.
- `tests/canonical/`은 8 카테고리 × 3 case × 3 파일 = 72 files이며, input 기준 24 fixtures입니다.
- `.github/workflows/g4-hash-chain.yml` 크기는 10652 bytes로 brief 기재와 일치합니다.
- `.github/workflows/history-anchor-verifier.yml` 크기는 19094 bytes로 brief 기재와 일치합니다.
- `.github/workflows/rewrite-defense.yml` 크기는 16454 bytes로 brief 기재와 일치합니다.

PoC 시제 존재 주장은 working directory 기준으로 충족됩니다.

## §4 4 대안별 평가

### §4.1 `(γ-a)` Layer 1+2 의존 영역 우선 진입 → Layer 4 후속

**평가: 정합**

brief의 `(γ-a)` 평가는 정확합니다.

핵심은 Layer 4가 Layer 1+2의 회귀 검증이라는 점입니다.

따라서 Layer 1+2를 먼저 PASS 격상하고, 이후 Layer 4를 PASS 격상하는 순서는 의존 chain을 가장 보수적으로 따릅니다.

장점:

- 의존 chain이 가장 명확합니다.
- Layer 1+2 evidence와 Layer 4 evidence가 분리됩니다.
- PASS 발효 단계를 작게 나눌 수 있습니다.
- R-S1 정정 후행 영향도 단계별로 흡수하기 쉽습니다.

단점:

- cycle 수가 늘어납니다.
- ceremony-inflation 위험이 있습니다.
- Layer 4 PASS 발효가 지연됩니다.

결론:

- `(γ-a)`는 **안전한 2순위**로 적합합니다.
- 단, brief §2.6 표의 “권고 (1)” 표기는 `(γ-c)` 1순위 방침과 충돌하므로 정정해야 합니다.

### §4.2 `(γ-b)` Layer 4 단독 진입, Layer 1+2 자동 동시

**평가: 조건부 정합**

brief의 `(γ-b)` 평가는 대체로 정확합니다.

Layer 4가 Layer 1+2를 검증하므로, Layer 4 단독 진입은 실제로 Layer 1+2를 자동 포함합니다.

따라서 `(γ-b)`는 표면상 단일 Layer 4 cycle이지만, 실질적으로는 Layer 1+2+4 통합 cycle입니다.

장점:

- cycle 수가 적습니다.
- ceremony-inflation을 줄입니다.
- Layer 4 착수 지연이 적습니다.

위험:

- Layer 1+2 evidence가 Layer 4 evidence에 흡수될 수 있습니다.
- PASS evidence의 ownership이 흐려질 수 있습니다.
- “Layer 4 단독”이라는 표현이 실제 bundled scope를 숨길 수 있습니다.

결론:

- `(γ-b)`는 가능하지만 `(γ-c)`보다 불리합니다.
- 채택 시 layer별 evidence subsection 강제가 필요합니다.

### §4.3 `(γ-c)` Layer 1+2+4 동시 진입

**평가: 가장 정합적**

brief의 `(γ-c)` 평가는 정확합니다.

`(γ-c)`는 `(γ-b)`와 동일하게 1 cycle 효율을 얻으면서도, Layer 1+2+4를 명시적으로 동시에 다룹니다.

따라서 implicit bundled scope 문제가 줄어듭니다.

장점:

- defense-in-depth 원칙과 가장 잘 맞습니다.
- Layer 1+2+4 evidence를 한 cycle에서 분리 명시할 수 있습니다.
- PoC 시제가 이미 존재하는 현 상태와도 잘 맞습니다.
- Layer 4의 의존 대상 부재 문제가 없습니다.
- ceremony-inflation도 `(γ-a)`보다 낮습니다.

위험:

- 합의 범위가 큽니다.
- 외부 LLM 및 풀 3+1 검토 부담이 큽니다.
- PASS evidence template이 부실하면 통합 cycle의 장점이 사라집니다.

결론:

- `(γ-c)`는 **1순위 권고**가 타당합니다.
- 단, §2.6 표 내부 순위 불일치 정정이 필요합니다.

### §4.4 `(γ-d)` Layer 4 단독 + Layer 1+2 별도 cycle 분리

**평가: 비권고**

brief의 `(γ-d)` 모순 risk 평가는 정확합니다.

Layer 4는 Layer 1+2를 자동 회귀 검증하는 layer입니다.

따라서 Layer 1+2가 PASS 발효되지 않은 상태에서 Layer 4만 PASS 발효하면 검증 대상이 없습니다.

장점:

- 문서상 분리는 가장 명확해 보입니다.
- Layer 4 논의를 독립 cycle로 세울 수 있습니다.

치명적 위험:

- Layer 4의 검증 대상인 Layer 1+2가 미발효일 수 있습니다.
- Layer 4 PASS 발효가 의미적으로 공허해질 수 있습니다.
- ADR-012 §2.8 / G4 §4.4.1의 5-layer 모델과 충돌합니다.
- 결국 Layer 1+2 PASS 선행 또는 동시가 필요해져 `(γ-a)` 또는 `(γ-c)`로 되돌아갑니다.

결론:

- `(γ-d)`는 planning-only framing으로는 가능하지만, PASS 발효 구조로는 비권고입니다.
- 채택하려면 “Layer 4 PASS 선발효 금지”를 명시해야 합니다.

## §5 `(γ-d)` 모순 risk verify 결과

**검증 결과: 모순 risk confirmed**

근거 chain은 다음입니다.

1. G4 §4.4.1 / ADR-012 §2.8 계열에서 Layer 4는 CI 회귀 검증입니다.
2. 해당 Layer 4는 Layer 1 hash chain과 Layer 2 history를 검증합니다.
3. 따라서 Layer 1+2가 없으면 Layer 4의 회귀 검증 대상이 없습니다.
4. `(γ-d)`는 Layer 4 단독과 Layer 1+2 별도 cycle을 분리합니다.
5. 이때 Layer 4 PASS가 Layer 1+2 PASS보다 먼저 발효되면 검증 대상 부재가 발생합니다.

따라서 `(γ-d)`는 다음 중 하나로만 정합화됩니다.

- Layer 4 cycle을 planning-only로 제한
- Layer 1+2 PASS를 Layer 4 PASS의 선행조건으로 둠
- Layer 1+2+4를 동시 PASS evidence로 묶음

이 중 세 번째는 사실상 `(γ-c)`입니다.

두 번째는 사실상 `(γ-a)`입니다.

따라서 brief §2.4.4의 “`(γ-d)` = 사실상 `(γ-a)`와 동등” 판단은 방향상 타당합니다.

다만 더 정확한 표현은 다음입니다.

- `(γ-d)`는 Layer 4 PASS 선발효가 불가능하므로, PASS 발효 구조에서는 `(γ-a)` 또는 `(γ-c)`로 환원된다.

## §6 권고 매트릭스

| 기준 | `(γ-a)` | `(γ-b)` | `(γ-c)` | `(γ-d)` |
|---|---:|---:|---:|---:|
| 의존 chain 정합성 | 높음 | 중간~높음 | 높음 | 낮음 |
| Layer 1+2 evidence 분리 | 높음 | 낮음~중간 | 높음 | 문서상 높음, 발효상 낮음 |
| Layer 4 의미 보존 | 높음 | 높음 | 높음 | 낮음 |
| cycle 효율 | 낮음 | 높음 | 높음 | 낮음 |
| ceremony-inflation 억제 | 낮음 | 높음 | 높음 | 낮음 |
| defense-in-depth 명시성 | 중간 | 중간 | 높음 | 낮음 |
| PoC 시제 활용성 | 높음 | 높음 | 높음 | 중간 |
| PASS 발효 정합성 | 높음 | 조건부 | 높음 | 낮음 |
| R-S1 후행 영향 흡수 | 높음 | 중간 | 중간~높음 | 낮음 |
| 총평 | 2순위 | 3순위 | 1순위 | 비권고 |

**최종 권고**

1. `(γ-c)` Layer 1+2+4 동시 진입: **1순위**
2. `(γ-a)` Layer 1+2 우선 → Layer 4 후속: **2순위**
3. `(γ-b)` Layer 4 단독 + Layer 1+2 자동 동시: **3순위**
4. `(γ-d)` Layer 4 단독 + Layer 1+2 별도: **비권고**

**조건부 승인 조건**

- brief §2.6 표의 권고 순위를 `(γ-c) 1순위`, `(γ-a) 2순위`로 통일할 것.
- Layer 2 PoC evidence는 local workflow evidence와 remote/admin branch protection evidence를 분리 표기할 것.

이 두 보강 후 본 brief는 `(γ)` 결정 입력 자료로 승인 가능합니다.
tokens used
71,552
## 검토자 / Vendor

- 검토자: 외부 LLM 검토자, cross-vendor blind review
- 응답 vendor: **OpenAI / codex CLI**
- 본 cycle 풀 3+1 Agent vendor: **Anthropic Claude**
- cross-vendor 조건: **충족**

## 직접 검토한 Working Directory 자료

- `docs/phase0/mvp2-gamma-layer-separation-brief.md`
- `docs/phase0/mvp2-entry-brief.md`
- `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- `docs/external-review/2026-05-28-mvp2-entry-codex-response.md`
- `docs/architecture/provider-agnostic-memory-skill-design.md`
- `docs/decisions/ADR-012-evidence-ledger-protection.md`
- `docs/decisions/ADR-011-means-vs-ends-redaction.md`
- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`
- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`

## §0 총평

**판정: APPROVE WITH CONDITIONS**

본 brief v1은 `(γ) MVP-2 G4 §4.4 Layer 분리 영역 결정`의 입력 자료로 대체로 적격합니다.

핵심 이유는 다음과 같습니다.

- brief §0.2 / §0.3 / §0.4가 본 cycle의 권위 한계를 명확히 분리합니다.
- brief §1.2가 52 entry §2.2.4의 4 대안 `(γ-a/b/c/d)`를 직접 답습합니다.
- brief §2.1~§2.4가 각 대안의 의존 chain, 장단점, PASS 발효 시점 차이를 비교합니다.
- brief §2.5가 PoC 시제와 PASS 시제를 분리합니다.
- brief §3이 ADR-011 §2.1 `(a)~(d)` 4조건과 `(e)` 후속 운영조건을 각 대안별로 재매핑합니다.
- brief §5가 Rollback Trigger / Evidence를 “후보 채택”으로 제한합니다.
- brief §5.1 RT-γ-6 및 §9.4가 R-S1 후행 영향을 별도 cycle로 보존합니다.

다만 **추천 순위 표기 내부 불일치**가 있습니다.

brief §2.6 표 안에서는 `(γ-a)`가 “권고 (1)”, `(γ-c)`가 “권고 (2)”로 표기되어 있습니다.

그런데 같은 §2.6의 결론 문장 및 사용자 제공 cycle 개요는 **`(γ-c) 1순위 + (γ-a) 2순위`**입니다.

이는 본 cycle이 “4 대안 中 채택 결정”을 위한 입력 자료라는 점에서 의사결정 입력을 혼선시킬 수 있으므로, 최종 합의 입력 전에는 반드시 정정되어야 합니다.

따라서 **APPROVE WITH CONDITIONS**입니다.

## §1 BLOCKING 1건

### R-1. §2.6 권고 순위 표기 불일치 정정 필요

**위치**

- `docs/phase0/mvp2-gamma-layer-separation-brief.md` §2.6

**문제**

§2.6 권고 매트릭스 표는 다음처럼 읽힙니다.

- `(γ-a)` 본 brief 권고: `권고 (1) — 안전 + 의존 답습`
- `(γ-c)` 본 brief 권고: `권고 (2) — defense-in-depth + 효율`

하지만 바로 아래 결론 문장은 다음 방향입니다.

- `본 brief 권고 ... (γ-c) Layer 1+2+4 동시 ... 1순위 + (γ-a) ... 2순위`

사용자 제공 cycle 개요도 동일하게 `(γ-c) 1순위 + (γ-a) 2순위`를 전제합니다.

**영향**

본 cycle은 수단 구현이 아니라 **4 대안 채택 결정 cycle**입니다.

따라서 추천 순위 표기가 서로 다르면, 후속 풀 3+1 합의에서 다음 두 해석이 충돌합니다.

- 해석 1: 표 기준 `(γ-a)` 1순위
- 해석 2: 결론 문장 기준 `(γ-c)` 1순위

이는 구현 발효를 만들지는 않지만, **결정 입력 자격**에는 직접 영향을 줍니다.

**요구 정정**

둘 중 하나로 통일해야 합니다.

본 brief 및 사용자 cycle 개요의 일관된 방향을 기준으로 하면 권장 정정은 다음입니다.

| 대안 | 정정 권고 |
|---|---|
| `(γ-c)` | `권고 (1) — defense-in-depth + 효율` |
| `(γ-a)` | `권고 (2) — 안전 + 의존 답습` |

**정정 후 판정**

이 1건이 정정되면 본 brief는 `(γ)` 결정 입력 자료로 **APPROVE 가능**합니다.

## §2 권고 6건

### N-1. PoC 시제 cross-check에서 “local evidence”와 “remote/admin evidence”를 분리 권고

brief §2.5는 Layer 2 항목에 다음을 포함합니다.

- branch protection rule
- `denyNonFastForwards`
- base branch 대비 JSONL line deletion / rewrite 감지

working directory에서 직접 확인 가능한 것은 주로 다음입니다.

- `.github/workflows/g4-hash-chain.yml`
- `.github/workflows/history-anchor-verifier.yml`
- `.github/workflows/rewrite-defense.yml`
- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`

반면 GitHub branch protection rule 및 remote `denyNonFastForwards` 적용 여부는 working directory 파일만으로는 완전 검증되지 않습니다.

따라서 §2.5의 Layer 2 row는 다음처럼 분리하는 편이 더 정확합니다.

- local PoC evidence: workflow / script 존재 및 내용
- remote/admin evidence: branch protection / non-fast-forward 차단 설정 확인 필요

이는 blocking은 아닙니다.

brief가 “PoC 시제”와 “PASS 시제”를 분리하고 있기 때문입니다.

### N-2. “5 영역 모두 충족” 표현을 artifact 기준과 layer 기준으로 나누는 편이 안전

사용자 검토 의무는 PoC 시제 cross-check를 “5 영역”이라고 표현하지만, 괄호 안 artifact는 사실상 다음 4 묶음입니다.

- `tools/jsonl_hash_chain.py`
- `tools/canonical_json.py`
- `tests/canonical/`
- `.github/workflows/g4-hash-chain.yml`

brief §2.5는 이를 5 row로 재구성합니다.

- Layer 1 hash chain
- Layer 2 Git append-only
- canonical JSON test corpus
- genesis hash
- Layer 4 CI regression

이 재구성은 타당하지만, 독자가 artifact 수와 evidence 영역 수를 혼동할 수 있습니다.

권고 문구:

- “artifact 기준 4 묶음 + evidence 영역 기준 5 row”

### N-3. `(γ-b)`는 “자동 동시”보다 “implicit bundled scope” 위험을 더 선명히 쓰는 편이 좋음

brief §2.2는 `(γ-b)`를 다음처럼 정의합니다.

- Layer 4 단독 진입
- Layer 1+2 = 의존 영역 자동 동시 진입

평가는 대체로 정확합니다.

다만 위험은 단순히 “evidence 분리 미명확”이 아니라, 합의 문서상으로는 Layer 4 단독처럼 보이지만 실제로는 Layer 1+2+4가 묶이는 **implicit bundled scope**입니다.

권고 문구:

- `(γ-b)`는 의존 chain은 만족하지만, Layer 1+2의 evidence namespace가 Layer 4 evidence에 흡수될 위험이 있으므로 후속 PASS evidence template에서 layer별 subsection을 강제해야 한다.

### N-4. `(γ-d)`는 “사실상 `(γ-a)`와 동등”보다 “Layer 4 PASS 선발효 불가”를 주 문장으로 두는 편이 명확

brief §2.4.4는 다음 결론을 냅니다.

- `(γ-d) = 사실상 (γ-a) 와 동등`

이 판단은 방향상 맞습니다.

다만 `(γ-d)`의 본질적 결함은 “동등성”보다 먼저 다음입니다.

- Layer 4 PASS는 Layer 1+2 PASS 없이 선발효할 수 없음

따라서 권고 문구:

- `(γ-d)`가 채택되더라도 Layer 4 PASS 선발효는 금지되며, Layer 1+2 PASS 선행 또는 동시 evidence가 없으면 `(γ-d)`의 Layer 4 cycle은 planning-only로 제한된다.

### N-5. RT-γ-6은 “후행 영향”뿐 아니라 “PASS 전 선행/동시 정정 후보”로도 남겨야 함

brief §5.1 RT-γ-6은 R-S1 cross-reference 정정 후행 영향을 잘 보존합니다.

52 entry §9.5에는 MVP-2 Implementation Evidence PASS 발효 시점에 R-S1 정정이 선행 또는 동시 의무 영역으로 다뤄질 수 있다는 취지가 있습니다.

따라서 본 brief에도 다음 문장을 추가하면 더 안전합니다.

- R-S1 정정은 본 `(γ)` cycle의 자동 진입 대상은 아니나, MVP-2 Implementation Evidence PASS 발효 시점에는 선행 또는 동시 정정 필요성이 재평가되어야 한다.

### N-6. 외부 LLM 1+ 권고와 cross-vendor 비협상 조건의 관계를 더 짧게 고정 권고

brief §4.1 / §7.1은 외부 LLM 1+를 “권고 / 사용자 영역 결정”으로 둡니다.

사용자 지시에서는 이번 검토 자체가 cross-vendor 충족 조건입니다.

따라서 본 cycle 기록에는 다음을 명시하면 충분합니다.

- 본 외부 검토 응답은 OpenAI codex CLI이고, 풀 3+1 Agent vendor는 Anthropic Claude이므로 헌법 5조-2 Provider Liquidity cross-vendor 요건을 충족한다.

## §3 NOTE 5건

### NOTE-1. brief v1 직접 읽기 evidence

직접 확인한 brief 문구 / 영역은 다음입니다.

- §0.2: “본 brief 가 하는 것”
- §0.3: “본 brief 가 하지 않는 것”
- §1.2: `(γ-a/b/c/d)` 4 대안 정의
- §2.4.4: `(γ-d)` 모순 risk
- §2.5: PoC 시제 답습 cross-check
- §3: ADR-011 4조건 + `(e)` 운영조건 매트릭스
- §5.1: RT-γ-1~RT-γ-6
- §8.1: 다음 단계, 사용자 결정 영역
- §10: 자기진단 P-1~P-7

직접 인용 가능한 핵심 문구:

> `본 cycle = 4 대안 中 채택 결정 (γ-a/b/c/d 中 사용자 명시 + 풀 3+1 합의)`

> `Layer 4 = "Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증"`

> `PoC 시제 충족 / PASS 시제 미충족`

> `Rollback Trigger / Evidence *후보 채택*`

### NOTE-2. ADR-011 §2.1 확인 결과

ADR-011 §2.1은 실제로 `(a)~(d)` 4조건입니다.

- `(a)` 동등 이상의 보안 결과
- `(b)` 격리 환경 PoC로 실증
- `(c)` ADR 권위로 명시
- `(d)` 자동 회귀 검증 경로 확보

`(e)`는 ADR-011 §2.1의 원조건이 아니라 후속 합의 APPROVE 운영조건으로 다루는 것이 맞습니다.

brief §3의 framing은 이 정정을 반영하고 있습니다.

### NOTE-3. G4 §4.4.1 Layer 정의 확인 결과

`provider-agnostic-memory-skill-design.md` §4.4.1은 5-layer 모델입니다.

- Layer 1: Hash Chain
- Layer 2: Git Append-only Branch
- Layer 3: Signed Commit
- Layer 4: CI 회귀 검증
- Layer 5: External Anchor

특히 Layer 4는 다음 의미입니다.

- Layer 1 + Layer 2 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증
- R-6 workflow 답습 확장

따라서 Layer 4는 Layer 1+2의 독립 대체물이 아니라 **Layer 1+2를 대상으로 하는 regression layer**입니다.

### NOTE-4. ADR-012 R-S1 확인 결과

ADR-012 §2.3은 4-layer 모델로 보이며, Layer 4를 External anchor로 둡니다.

ADR-012 §2.8은 5-layer rewrite 방어 모델로 보이며, Layer 4를 CI 회귀 검증, Layer 5를 External anchor로 둡니다.

따라서 R-S1은 실제 divergence입니다.

brief는 이를 다음처럼 적절히 처리합니다.

- G4 §4.4.1 + ADR-012 §2.8 = Layer numbering 권위
- ADR-012 §2.3 = append-only / hash chain 원칙 권위
- cross-reference 정정 = 별도 cycle

이 처리는 타당합니다.

### NOTE-5. PoC 파일 확인 결과

확인 결과:

- `tools/jsonl_hash_chain.py`는 genesis hash 함수와 `prev_hash_mismatch`, `hash_recalculation`, `history_rewrite`, `genesis_mismatch` 4 violation type을 포함합니다.
- `tools/canonical_json.py`는 `rfc8785`, `jcs`, `jq -S -c` fallback, cross-check mode를 포함합니다.
- `tests/canonical/`은 8 카테고리 × 3 case × 3 파일 = 72 files이며, input 기준 24 fixtures입니다.
- `.github/workflows/g4-hash-chain.yml` 크기는 10652 bytes로 brief 기재와 일치합니다.
- `.github/workflows/history-anchor-verifier.yml` 크기는 19094 bytes로 brief 기재와 일치합니다.
- `.github/workflows/rewrite-defense.yml` 크기는 16454 bytes로 brief 기재와 일치합니다.

PoC 시제 존재 주장은 working directory 기준으로 충족됩니다.

## §4 4 대안별 평가

### §4.1 `(γ-a)` Layer 1+2 의존 영역 우선 진입 → Layer 4 후속

**평가: 정합**

brief의 `(γ-a)` 평가는 정확합니다.

핵심은 Layer 4가 Layer 1+2의 회귀 검증이라는 점입니다.

따라서 Layer 1+2를 먼저 PASS 격상하고, 이후 Layer 4를 PASS 격상하는 순서는 의존 chain을 가장 보수적으로 따릅니다.

장점:

- 의존 chain이 가장 명확합니다.
- Layer 1+2 evidence와 Layer 4 evidence가 분리됩니다.
- PASS 발효 단계를 작게 나눌 수 있습니다.
- R-S1 정정 후행 영향도 단계별로 흡수하기 쉽습니다.

단점:

- cycle 수가 늘어납니다.
- ceremony-inflation 위험이 있습니다.
- Layer 4 PASS 발효가 지연됩니다.

결론:

- `(γ-a)`는 **안전한 2순위**로 적합합니다.
- 단, brief §2.6 표의 “권고 (1)” 표기는 `(γ-c)` 1순위 방침과 충돌하므로 정정해야 합니다.

### §4.2 `(γ-b)` Layer 4 단독 진입, Layer 1+2 자동 동시

**평가: 조건부 정합**

brief의 `(γ-b)` 평가는 대체로 정확합니다.

Layer 4가 Layer 1+2를 검증하므로, Layer 4 단독 진입은 실제로 Layer 1+2를 자동 포함합니다.

따라서 `(γ-b)`는 표면상 단일 Layer 4 cycle이지만, 실질적으로는 Layer 1+2+4 통합 cycle입니다.

장점:

- cycle 수가 적습니다.
- ceremony-inflation을 줄입니다.
- Layer 4 착수 지연이 적습니다.

위험:

- Layer 1+2 evidence가 Layer 4 evidence에 흡수될 수 있습니다.
- PASS evidence의 ownership이 흐려질 수 있습니다.
- “Layer 4 단독”이라는 표현이 실제 bundled scope를 숨길 수 있습니다.

결론:

- `(γ-b)`는 가능하지만 `(γ-c)`보다 불리합니다.
- 채택 시 layer별 evidence subsection 강제가 필요합니다.

### §4.3 `(γ-c)` Layer 1+2+4 동시 진입

**평가: 가장 정합적**

brief의 `(γ-c)` 평가는 정확합니다.

`(γ-c)`는 `(γ-b)`와 동일하게 1 cycle 효율을 얻으면서도, Layer 1+2+4를 명시적으로 동시에 다룹니다.

따라서 implicit bundled scope 문제가 줄어듭니다.

장점:

- defense-in-depth 원칙과 가장 잘 맞습니다.
- Layer 1+2+4 evidence를 한 cycle에서 분리 명시할 수 있습니다.
- PoC 시제가 이미 존재하는 현 상태와도 잘 맞습니다.
- Layer 4의 의존 대상 부재 문제가 없습니다.
- ceremony-inflation도 `(γ-a)`보다 낮습니다.

위험:

- 합의 범위가 큽니다.
- 외부 LLM 및 풀 3+1 검토 부담이 큽니다.
- PASS evidence template이 부실하면 통합 cycle의 장점이 사라집니다.

결론:

- `(γ-c)`는 **1순위 권고**가 타당합니다.
- 단, §2.6 표 내부 순위 불일치 정정이 필요합니다.

### §4.4 `(γ-d)` Layer 4 단독 + Layer 1+2 별도 cycle 분리

**평가: 비권고**

brief의 `(γ-d)` 모순 risk 평가는 정확합니다.

Layer 4는 Layer 1+2를 자동 회귀 검증하는 layer입니다.

따라서 Layer 1+2가 PASS 발효되지 않은 상태에서 Layer 4만 PASS 발효하면 검증 대상이 없습니다.

장점:

- 문서상 분리는 가장 명확해 보입니다.
- Layer 4 논의를 독립 cycle로 세울 수 있습니다.

치명적 위험:

- Layer 4의 검증 대상인 Layer 1+2가 미발효일 수 있습니다.
- Layer 4 PASS 발효가 의미적으로 공허해질 수 있습니다.
- ADR-012 §2.8 / G4 §4.4.1의 5-layer 모델과 충돌합니다.
- 결국 Layer 1+2 PASS 선행 또는 동시가 필요해져 `(γ-a)` 또는 `(γ-c)`로 되돌아갑니다.

결론:

- `(γ-d)`는 planning-only framing으로는 가능하지만, PASS 발효 구조로는 비권고입니다.
- 채택하려면 “Layer 4 PASS 선발효 금지”를 명시해야 합니다.

## §5 `(γ-d)` 모순 risk verify 결과

**검증 결과: 모순 risk confirmed**

근거 chain은 다음입니다.

1. G4 §4.4.1 / ADR-012 §2.8 계열에서 Layer 4는 CI 회귀 검증입니다.
2. 해당 Layer 4는 Layer 1 hash chain과 Layer 2 history를 검증합니다.
3. 따라서 Layer 1+2가 없으면 Layer 4의 회귀 검증 대상이 없습니다.
4. `(γ-d)`는 Layer 4 단독과 Layer 1+2 별도 cycle을 분리합니다.
5. 이때 Layer 4 PASS가 Layer 1+2 PASS보다 먼저 발효되면 검증 대상 부재가 발생합니다.

따라서 `(γ-d)`는 다음 중 하나로만 정합화됩니다.

- Layer 4 cycle을 planning-only로 제한
- Layer 1+2 PASS를 Layer 4 PASS의 선행조건으로 둠
- Layer 1+2+4를 동시 PASS evidence로 묶음

이 중 세 번째는 사실상 `(γ-c)`입니다.

두 번째는 사실상 `(γ-a)`입니다.

따라서 brief §2.4.4의 “`(γ-d)` = 사실상 `(γ-a)`와 동등” 판단은 방향상 타당합니다.

다만 더 정확한 표현은 다음입니다.

- `(γ-d)`는 Layer 4 PASS 선발효가 불가능하므로, PASS 발효 구조에서는 `(γ-a)` 또는 `(γ-c)`로 환원된다.

## §6 권고 매트릭스

| 기준 | `(γ-a)` | `(γ-b)` | `(γ-c)` | `(γ-d)` |
|---|---:|---:|---:|---:|
| 의존 chain 정합성 | 높음 | 중간~높음 | 높음 | 낮음 |
| Layer 1+2 evidence 분리 | 높음 | 낮음~중간 | 높음 | 문서상 높음, 발효상 낮음 |
| Layer 4 의미 보존 | 높음 | 높음 | 높음 | 낮음 |
| cycle 효율 | 낮음 | 높음 | 높음 | 낮음 |
| ceremony-inflation 억제 | 낮음 | 높음 | 높음 | 낮음 |
| defense-in-depth 명시성 | 중간 | 중간 | 높음 | 낮음 |
| PoC 시제 활용성 | 높음 | 높음 | 높음 | 중간 |
| PASS 발효 정합성 | 높음 | 조건부 | 높음 | 낮음 |
| R-S1 후행 영향 흡수 | 높음 | 중간 | 중간~높음 | 낮음 |
| 총평 | 2순위 | 3순위 | 1순위 | 비권고 |

**최종 권고**

1. `(γ-c)` Layer 1+2+4 동시 진입: **1순위**
2. `(γ-a)` Layer 1+2 우선 → Layer 4 후속: **2순위**
3. `(γ-b)` Layer 4 단독 + Layer 1+2 자동 동시: **3순위**
4. `(γ-d)` Layer 4 단독 + Layer 1+2 별도: **비권고**

**조건부 승인 조건**

- brief §2.6 표의 권고 순위를 `(γ-c) 1순위`, `(γ-a) 2순위`로 통일할 것.
- Layer 2 PoC evidence는 local workflow evidence와 remote/admin branch protection evidence를 분리 표기할 것.

이 두 보강 후 본 brief는 `(γ)` 결정 입력 자료로 승인 가능합니다.
