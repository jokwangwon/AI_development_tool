# (γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 brief (v1.1)

> **작성**: 2026-05-28 (53번째 entry 진입 cycle)
>
> **v1 → v1.1 갱신**: 풀 3+1 + 외부 LLM 1+ (codex gpt-5.5 cross-vendor) 통합 합의 (`docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md`) BLOCKING 8 + 권고 16 1pass 흡수 (별도 v2 cycle 0, ceremony-inflation 차단). §11 v1.1 보강 매트릭스 추가.
>
> **scope**: G4 §4.4 Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입 결정 — 4 대안 (γ-a/b/c/d) 中 채택
>
> **본 cycle = 큰 cycle** (52 entry (α) 발효 후 carry-over 5번, 풀 3+1 + 외부 LLM 1+)
>
> **본 cycle 발효 자격** = **풀 3+1 합의 + 외부 LLM 1+ (cross-vendor codex 답습) + 사용자 명시 결정**
>
> **본 cycle 발효 효과** = (γ) 4 대안 평가 권고 발효 + (γ-d) 모순 CONFIRMED 발효 + 후속 sub-cycle 진입 자격 발효 (수단 *결정* = 별도 cycle)

---

## §0 본 brief 의 범위

### §0.1 사용자 진입 명령 답습 (carry-over from 52 entry, commit `c739c53`)

52 entry `mvp2-entry-brief.md` (v1.1) §8.1 다음 단계 답습. 본 (γ) cycle 진입 사용자 명시 (2026-05-28) — "5번 (γ) 진입". 본 brief = (γ) 영역 한정.

### §0.2 본 brief 가 *하는* 것

1. (γ) 4 대안 정의 답습 (52 entry brief §2.2.4 + Reviewer 합의 §8.1 직접 인용) (§1)
2. 각 대안 trade-off 분석 (4 대안 + (γ-e/f/g) 추가 hybrid 평가) (§2)
3. 현 PoC 시제 답습 cross-check (52 entry Agent A N-A-1 + B-6 답습) (§2.5)
4. **ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 합의 APPROVE 후속 운영조건 매트릭스 — 각 대안별** (§3)
5. 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (52 entry §4.2 답습) (§4.1)
6. (γ) 채택 결정 발효 자격 명문 (§4.2)
7. 7 풀 3+1 승격 트리거 발화 검증 (§4.3)
8. **Rollback Trigger / Evidence *후보 채택*** (구현 발효 ≠ 본 합의) (§5)
9. 외부 LLM 응답 요구 영역 (§7)
10. 후속 sub-cycle 진입 자격 명문 (§8)

### §0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습 + 본 brief 영역 한계)

| # | 영역 | 위반 시점 |
|---|------|----------|
| 1 | 실 코드 / runtime code 구현 | 0건 |
| 2 | `tools/jsonl_hash_chain.py` / `tools/canonical_json.py` 본문 변경 | 0건 (PoC 시제 답습 보존) |
| 3 | `tests/canonical/` test corpus 본문 변경 | 0건 |
| 4 | `.github/workflows/*.yml` 본문 변경 | 0건 |
| 5 | ledger 첫 entry (genesis hash) 작성 | 0건 |
| 6 | G4 §4.4 Layer sub-수단 결정 (L-1~L-5) | 0건 ((β) 별도) |
| 7 | GP-2 sub-수단 결정 (R-1~R-5) | 0건 ((β) 별도) |
| 8 | W 통합 결정 (W-A~E) | 0건 ((β) 별도) |
| 9 | 외부 library (`pyjcs` / `rfc8785`) 도입 결정 | 0건 |
| 10 | threshold 고정 | 0건 |
| 11 | Tier-2/3 vendor catalog 본문 확장 | 0건 |
| 12 | MVP-2 Implementation Evidence PASS 발효 | 0건 |
| 13 | MVP-1 PASS 재선언 | 0건 |
| 14 | Operational Readiness PASS | 0건 |
| 15 | Hermes PMO 격상 | 0건 |
| 16 | ADR / 헌법 / roadmap / governance / G4 / ADR-012 본문 갱신 | 0건 (cross-reference 답습 한정) |
| 17 | `adapters/llm/facade.py` placeholder → real 본문 (TR-1) | 0건 |
| 18 | G4 §4.4 Layer 3 (Signed commit) / Layer 5 (External anchor) 영역 진입 결정 | 0건 (본 cycle = Layer 1+2+4 한정) |
| 19 | GP-1 / GP-4 / GP-6 / G3 / G4 (Layer 4 외) 영역 진입 결정 | 0건 |
| 20 | R-S1 cross-reference 정정 자동 진입 (ADR-012 §2.3 vs §2.8) | 0건 (별도 cycle) |
| 21 | Hermes upstream `agent/redact.py` 본 repo 內 import 결정 | 0건 |
| 22 | (γ-e/f/g) hybrid 대안 결정 ⭐ (B-8 흡수) | 0건 (§2.7 평가만, 결정 = 별도 cycle 사용자 영역) |
| 23 | **(γ) 4 대안 中 채택 *결정*** (본 brief = 평가 + 권고 한정, 결정 = 합의 발효 후 사용자 명시) ⭐ (Reviewer 합의 §6.2 답습) | 0건 |
| 24 | Layer 4 PASS 선발효 (Layer 1+2 PASS 부재 시) ⭐ (B-1 + N-2 흡수) | 0건 (모순 CONFIRMED, planning-only 제한) |
| 25 | 자동 후속 sub-cycle 진입 ((β) / Layer 1+2 PASS 격상 / 통합 / 실 구현) | 0건 |
| 26 | 본 brief 자체 영구화 / 권위 chain 등재 | 0건 |
| 27 | ADR-012 §2.2 event enum 신규 등록 자동 진입 | 0건 (52 entry §9.5 답습) |

### §0.4 본 brief 의 권위 한계

- ✅ 본 brief 발효 자격 = **풀 3+1 합의 + 외부 LLM 1+ (cross-vendor) + 사용자 명시 결정**
- ✅ 본 brief 발효 결과 = (γ) 4 대안 평가 권고 발효 + (γ-d) 모순 CONFIRMED 발효 + 후속 sub-cycle 진입 자격 발효 + Rollback Trigger / Evidence *후보 채택*
- ❌ 본 brief 자체에서 (γ) 4 대안 中 *채택 결정* 0건 (Reviewer 통합 권고 ≠ 결정)
- ❌ 본 brief 자체에서 sub-수단 결정 0건
- ❌ 본 brief 자체에서 실 구현 0건
- ❌ 본 brief 자체에서 MVP-2 Implementation Evidence PASS 발효 0건
- ❌ 본 brief 자체에서 ADR-011 §2.1 (a)~(d) 4조건 자동 충족 선언 0건
- ⚠️ 본 brief 합의 후 *자동 sub-수단 결정 / 실 구현 진입 금지* — 사용자 명시 결정 의무

---

## §1 진입 컨텍스트 답습

### §1.1 선행 권위 답습

| 합의 / 권위 | 본 cycle 답습 영역 |
|----------|-----------------|
| 52 entry brief v1.1 + Reviewer 합의 (`c739c53` 발효) | 본 (γ) brief 의 **직접 입력 자료**. §2.2.4 + §8.1 항목 2 답습 |
| 52 entry brief §2.2.4 (γ) 4 대안 매트릭스 (N-12 흡수) | (γ-a/b/c/d) 4 대안 정의 source |
| 52 entry brief Agent A N-A-1 + B-6 PoC 시제 발견 | tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml PoC 시제 충족 |
| G4 §4.4.1 line 629~660 (PRIMARY, 5-layer) | Layer 1~5 정의 |
| ADR-012 §2.8 line 264~272 (SUPPORTING, 5-layer) | G4 동형 |
| ADR-012 §2.3 line 165~185 (PRINCIPLE ONLY, 4-layer) | Append-only + Hash Chain 원칙 (numbering 근거 아님, R-S1 답습) |
| ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 (52 entry B-2 답습) | 5조건 매트릭스 §3 |
| ⭐ 본 cycle Reviewer 통합 합의 (`3plus1-consensus-2026-05-28-mvp2-gamma.md`, 264줄, BLOCKING 8 + 권고 16) | 본 v1.1 = 1pass 흡수 답습 |

### §1.2 (γ) 4 대안 정의 (52 entry §2.2.4 답습 verbatim)

| 대안 | 정의 |
|------|----|
| **(γ-a)** | Layer 1+2 의존 영역 우선 진입 후 Layer 4 후속 (단계적, 안전) |
| **(γ-b)** | Layer 4 단독 진입 (Layer 1+2 = 자동 의존 영역 동시) |
| **(γ-c)** | Layer 1+2+4 동시 진입 (defense-in-depth) |
| **(γ-d)** | Layer 4 단독 + Layer 1+2 = 별도 cycle 분리 (52 entry framing) — ⚠️ **모순 CONFIRMED** (5 source verify, §4.4 답습) |

### §1.3 ⭐ 선차 변경 매트릭스 (52 entry framing vs 본 (γ) cycle 결정)

| # | 영역 | 52 entry framing | 본 (γ) cycle 결정 | 권위 정당성 |
|---|------|------------------|------------------|------------|
| 1 | Layer 1+2 의존 영역 framing | "(γ-d) 현 framing" | **4 대안 평가 + Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위 + (γ-d) 비권고)** | ✅ 정당 (52 entry §8.1 답습 + 4 source consensus) |
| 2 | PoC 시제 vs PASS 시제 | "PoC 시제 충족 / PASS 시제 미충족" 격상 | **본 cycle = PoC 시제 답습 보존 + PASS 시제 격상 영역 결정** | ✅ 정당 |
| 3 | 합의 형태 | 풀 3+1 (52 entry §8.1) + 외부 LLM 1+ 권고 | **풀 3+1 + 외부 LLM 1+ (cross-vendor codex 답습 완료)** | ✅ 정당 |
| 4 ⭐ (N-12 흡수) | R-S1 후행 영향 (RT-γ-6) | 별도 cycle 영역 | **본 (γ) cycle = RT-γ-6 평가 + MVP-2 PASS 발효 시점 선행/동시 정정 의무 평가 (N-3 답습)** | ✅ 정당 (52 entry §9.5 답습) |

---

## §2 4 대안 분석 + 추가 hybrid 평가

### §2.1 (γ-a) Layer 1+2 우선 → Layer 4 후속

#### §2.1.1 영역 정의

순서: (1) Layer 1 PoC → PASS 격상 + (2) Layer 2 PoC → PASS 격상 + (3) canonical JSON test corpus PoC → PASS + (4) genesis hash 첫 entry → (5) Layer 4 PASS 격상 후속.

#### §2.1.2 장점

- ✅ 의존 chain 가장 명확 (Layer 4 = Layer 1+2 회귀 검증 대상)
- ✅ Layer 1+2 evidence와 Layer 4 evidence 분리
- ✅ 단계적 안전
- ✅ R-S1 후행 영향 흡수 용이

#### §2.1.3 단점 + 정량 (B-4 흡수)

- ⚠️ **합의 cycle 수 = 4 cycle** (Layer 1 + Layer 2 + canonical corpus + Layer 4) — cycle 수 ↑
- ⚠️ ceremony-inflation risk
- ⚠️ Layer 4 PASS 발효 지연

### §2.2 (γ-b) Layer 4 단독 (Layer 1+2 자동 동시)

#### §2.2.1 영역 정의

Layer 4 합의 cycle 진입 → Layer 1+2 의존 영역 자동 동시 진입 → 한 cycle 內 모두 진입.

#### §2.2.2 장점

- ✅ 단순 (1 cycle 진입)
- ✅ 시간 효율
- ✅ ceremony-inflation 차단

#### §2.2.3 단점

- ⚠️ Layer 1+2 separate scope 미인식 (evidence 합산 risk)
- ⚠️ "Layer 4 단독" 표현이 실제 bundled scope 숨김 (codex N-3 + Agent B 답습)
- ⚠️ **합의 cycle 수 = 1 cycle**, 단 evidence ownership 흐려질 risk

### §2.3 (γ-c) Layer 1+2+4 동시 진입

#### §2.3.1 영역 정의 (B-4 + N-5 흡수)

Layer 1+2+4 동시 합의 cycle 진입. **합의 cycle 수 = 3 cycle 등가** (Layer 1+2 통합 + canonical corpus + Layer 4 통합 evidence 분리). 실 구현 = `g4-hash-chain.yml` 7 step 답습 시 step prefix `[Layer N]` 권고 (N-5 흡수).

#### §2.3.2 장점 + framing 정정 (B-6 흡수)

- ✅ **defense-in-depth *부분 답습*** (Layer 1+2+4 한정, Layer 3 Signed commit + Layer 5 External anchor = 본 cycle scope 외) — (γ-c) "충실 답습" framing 정정 답습 (B-6)
- ✅ 각 layer evidence 명시 분리 ((γ-b) 와 차이)
- ✅ MVP-2 Implementation Evidence PASS 발효 시점 = (a)~(d) 4조건 모두 layer 별 명시 evidence
- ✅ PoC 시제 = 이미 운영 (g4-hash-chain.yml 7 step + tools/jsonl_hash_chain.py 14038B + canonical_json.py 10055B)

#### §2.3.3 단점 + N-1 흡수

- ⚠️ 합의 부담 ↑ (Layer 1+2+4 통합 + 각 layer evidence 분리)
- ⚠️ 외부 LLM 1+ + 사용자 명시 부담
- 📌 N-1 답습: (γ-c) 채택 시 PASS evidence template = Layer 1/Layer 2/Layer 4 subsection 강제 명문 의무

### §2.4 (γ-d) Layer 4 단독 + Layer 1+2 별도 cycle (52 entry framing) — 비권고

#### §2.4.1 영역 정의

Layer 4 단독 합의 + Layer 1+2 별도 cycle 분리. **합의 cycle 수 = 2+ cycle**.

#### §2.4.2 장점

- 본격 분리 framing
- Layer 4 진입 즉시 가능

#### §2.4.3 단점

- ⚠️ **의존 chain 모순** (Layer 4 = Layer 1+2 회귀 검증 → Layer 1+2 미발효 시 회귀 대상 부재)
- ⚠️ ADR-012 §2.3 + §2.8 다층 강제 답습 미충족
- ⚠️ ADR-011 §2.1 (c)+(d) 모순

#### §2.4.4 (γ-d) 결정 자격 framing 정정 (B-7 흡수)

본 (γ-d) = 52 entry brief framing 자체이지만 **(γ-d) PASS 발효 구조 환원 분석** (B-7 답습):
- Layer 4 PASS 선발효 불가 → planning-only 또는 (γ-a)/(γ-c) 환원

**본 cycle 결정 자격** = 풀 3+1 + 사용자 명시 영역 (§2.6 "비권고" 표현 답습 보존, B-7 흡수).

#### §2.4.5 ⭐ (γ-d) 모순 risk CONFIRMED 격상 + Layer 4 PASS 선발효 금지 명문 (B-1 + N-2 흡수)

**(γ-d) 모순 = CONFIRMED** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer 단독 verify, §4 답습).

**환원 정합화**:
1. Layer 4 cycle = planning-only 제한
2. Layer 1+2 PASS = Layer 4 PASS 선행조건 → 사실상 (γ-a)
3. Layer 1+2+4 동시 PASS evidence → 사실상 (γ-c)

**명문 (N-2 흡수)**: (γ-d) 채택 시 **Layer 4 PASS 선발효 금지** (planning-only 제한 또는 Layer 1+2 PASS 선행/동시 evidence 의무). 본 명문 = §5.1 RT-γ-5 답습.

### §2.5 PoC 시제 답습 cross-check (52 entry Agent A N-A-1 + B-6 답습 + B-3 + B-5 + N-6 흡수)

| 영역 | PoC 시제 (현 상태) | PASS 시제 (격상 영역) | violation_type 매핑 (N-6 흡수) |
|------|--------------|-------------------|------------------|
| Layer 1 (hash chain) | ✅ `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type) | PASS 격상 = R-6 workflow 답습 통합 + actual run PASS | **PREV_HASH_MISMATCH + HASH_RECALCULATION + GENESIS_MISMATCH** |
| Layer 2a — local workflow (B-3 흡수) | ⚠️ `git config receive.denyNonFastForwards` **활성화 evidence 명문 의무** (현 상태 미확정 — 본 cycle 後 별도 verify) | PASS 격상 = base branch 대비 JSONL line deletion / rewrite 감지 CI step | **HISTORY_REWRITE** |
| Layer 2b — remote/admin (B-3 흡수) | ✅ branch protection rule (43 entry 8 contexts 답습) | PASS 격상 = admin scope 추가 contexts (사용자 영역) | (Layer 2 동일) |
| canonical JSON test corpus (B-5 흡수) | ⚠️ `tests/canonical/` **8 카테고리 verify 충족 / 24 fixture 정량 = 52 entry Agent A carry-over** (본 cycle 직접 count 1-pass 부재 정직 명시) | PASS 격상 = CI step 內 reference 동등성 검증 + 위반 BLOCK | (corpus 영역) |
| genesis hash (첫 entry) | ✅ `tools/jsonl_hash_chain.py` 內 genesis hash 함수 | PASS 격상 = 실 ledger 첫 entry 작성 + audit log | GENESIS_MISMATCH |
| Layer 4 (CI 회귀 검증) | ✅ `.github/workflows/g4-hash-chain.yml` (10652B) PoC 시제 운영, 7 step 분리 (N-A-3 답습) | PASS 격상 = R-6 답습 통합 또는 단독 PASS 격상 + actual run PASS | (회귀 검증 영역) |

→ **모든 영역 PoC 시제 *대체로* 충족** (Layer 2a `denyNonFastForwards` 활성화 evidence 1 영역 = B-3 답습 별도 verify 필요). PASS 격상 = 본 (γ) 결정 후 후속 sub-cycle 영역.

### §2.6 (γ) 4 대안 권고 매트릭스 (Reviewer 통합, B-2 + B-6 + N-10 + N-14 흡수)

**핵심 답습**: 본 §2.6 = **Reviewer 통합 권고 (수단 *결정* = 풀 3+1 합의 발효 + 사용자 명시 영역, N-10 답습)**.

| 대안 | 의존 chain | 합의 cycle 수 | ceremony-inflation 억제 | defense-in-depth | PoC 시제 | PASS 발효 정합성 | **Reviewer 통합 순위** |
|------|---------|------------|-----|--------------|------|--------------|-------------------|
| (γ-c) Layer 1+2+4 동시 | 높음 | 3 (등가) | 높음 | **부분 답습** (Layer 1+2+4) | 높음 | 높음 | **1순위** (4 source consensus, B-6 framing 정정 답습) |
| (γ-a) Layer 1+2 우선 → Layer 4 후속 | 높음 | 4 | 낮음 | 중간 | 높음 | 높음 | **2순위** (4 source consensus) |
| (γ-b) Layer 4 단독 (auto 1+2) | 중간~높음 | 1 | 높음 | 중간 | 높음 | 조건부 (evidence 합산 risk) | 3순위 |
| (γ-d) Layer 4 단독 + Layer 1+2 별도 | **낮음 (모순 CONFIRMED, B-1 답습)** | 2+ | 낮음 | 낮음 | 중간 | **낮음 (Layer 4 PASS 선발효 불가, B-7 답습)** | **비권고** (4 source consensus + 5 source 모순 verify) |

### §2.7 ⭐ (γ-e/f/g) 추가 hybrid 대안 평가 (B-8 흡수 신규)

본 §2.7 = 4 대안 외 추가 hybrid 대안 평가 한정 (결정 ≠ 본 cycle, 별도 cycle 사용자 영역).

| 대안 | 정의 | 분석 |
|------|----|----|
| **(γ-e)** | (γ-a)+(γ-d) hybrid — Layer 1+2 우선 진입 + Layer 4 cycle 동시 planning (PASS 발효 = Layer 1+2 후) | (γ-d) 모순 회피 + (γ-a) 단계적 안전. Layer 4 cycle = planning-only 限定 |
| **(γ-f)** | PoC 시제 보존 한정 (PASS 격상 0) + Layer 4 단독 PASS | PoC 시제 답습 한정 = MVP-2 Implementation Evidence PASS 발효 시점 Layer 1+2 PASS evidence 부재 risk → MVP-2 PASS 발효 자격 미충족 |
| **(γ-g)** | 시점 vs evidence 분리 — 본 (γ) cycle = 시점 분리 결정 + MVP-2 PASS = evidence 통합 | (γ-a)+(γ-c) hybrid, MVP-2 PASS 발효 시점 evidence 통합 정합 |

→ 본 §2.7 = 평가만, 결정 = 별도 cycle 사용자 영역 (B-8 흡수).

---

## §3 ADR-011 §2.1 (a)~(d) 4조건 모법 + (e) 후속 운영조건 — 5조건 매트릭스 (각 대안별, B-2 framing 답습)

| # | 조건 | (γ-c) | (γ-a) | (γ-b) | (γ-d) |
|---|------|------|------|------|------|
| (a) | 동등 이상 보안 결과 | Layer 1+2+4 동시 PASS evidence (분리 명시) | Layer 1+2 PASS + Layer 4 PASS (단계적) | Layer 4 PASS (Layer 1+2 자동 통합) | Layer 4 PASS (Layer 1+2 미발효 시 모순) |
| (b) | 격리 환경 PoC 실증 | ✅ PoC 시제 충족 (모든 영역, Layer 2a 1 영역 별도 verify) | ✅ 동일 | ✅ 동일 | ✅ 동일 |
| (c) | ADR / SDD 권위 명시 | ✅ G4 §4.4.1 + ADR-012 §2.8 | ✅ 동일 | ✅ 동일 | ⚠️ Layer 4 단독 + Layer 1+2 부재 시 ADR-012 §2.3 다층 강제 답습 미충족 |
| (d) | 자동 회귀 검증 경로 확보 | R-6 답습 (각 layer step 분리) | R-6 답습 (단계적) | R-6 답습 (1 cycle 통합) | R-6 답습 (Layer 4 한정, 회귀 대상 부재 모순) |
| (e) | 합의 APPROVE | 1 합의 (풀 3+1 + 외부 LLM 1+) | 단계별 N회 | 1 합의 | 2+ 합의 + 모순 risk |

→ **(γ-c) + (γ-a) = 5조건 모두 충족 자격 정합**. (γ-b) = (c)+(d) Layer 1+2 evidence 분리 risk. **(γ-d) = (c)+(d) 모순 CONFIRMED** (§4.4 + §2.4.5 답습).

---

## §4 합의 형태 + 풀 3+1 승격 트리거 검증

### §4.1 본 cycle 합의 형태 = 풀 3+1 + 외부 LLM 1+ (cross-vendor codex 답습 완료, N-4 흡수)

**합의 형태**: **풀 3+1 + 외부 LLM 1+ (cross-vendor)**

**cross-vendor 형식 충족 (N-4 + N-13 흡수)**:
- 응답 vendor 분포: **OpenAI codex (gpt-5.5) 1 + Anthropic (Agent A/B/C + Reviewer) 4 = cross-vendor 형식 충족** (헌법 5조-2 Provider Liquidity 비협상 답습)

### §4.2 본 (γ) cycle 발효 효과

본 (γ) 합의 APPROVE WITH CONDITIONS → brief v1.1 보강 commit + push 후 발효:

1. **(γ) 4 대안 평가 권고 발효** (Reviewer 통합 권고: (γ-c) 1순위 + (γ-a) 2순위)
2. **(γ-d) 모순 risk CONFIRMED 발효** + Layer 4 PASS 선발효 금지 명문
3. **후속 sub-cycle 진입 자격 발효** (사용자 명시 시점 (γ-c) 또는 (γ-a) 채택 결정 cycle 진입 자격)
4. **Rollback Trigger 본문 *후보 채택*** (구현 발효 ≠ 본 합의)
5. **Evidence 형식 본문 *후보 채택***

### §4.3 7 풀 3+1 승격 트리거 검증 (N-8 framing 정밀화 답습)

| # | trigger | 본 (γ) 발화 | 근거 |
|---|---------|---------|------|
| 1 | 큰 결정 (영역 결정) | ✅ 발화 | (γ) 4 대안 평가 = MVP-2 Implementation Evidence PASS 발효 *시점/방식* 평가 |
| 2 | 아키텍처 / SDD / 보안 본문 변경 | ❌ 미발화 | brief = phase0 신규 1 파일 |
| 3 | ADR 본문 변경 | ❌ 미발화 | brief = ADR 본문 0 |
| 4 | 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화** (R-S1 후행 영향 RT-γ-6, 52 entry 발견 cascade) | 본 cycle = 후행 영향 평가 한정 |
| 5 ⭐ (N-8 framing 정밀화) | 외부 LLM 응답 통합 필요성 | ✅ **사용자 영역 결정 발화** (52 entry §8.1 답습 + cross-vendor 권고) | 본 cycle = 사용자 명시 (α) Claude tmux+codex 직접 호출 답습 발효 |
| 6 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | §0.3 #11 명시 금지 |
| 7 | Hermes PMO 격상 | ❌ 미발화 | §0.3 #15 명시 금지 |

→ **1/7 발화 + 1 부분 발화 + 1 사용자 영역 결정 발화 → 풀 3+1 + 외부 LLM 1+ 합의 적격 (정당화)**.

### §4.4 ⭐ (γ-d) 모순 risk CONFIRMED — 5 source verify (B-1 답습)

본 §4.4 = `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` §4 답습.

#### §4.4.1 Verbatim 직접 read 결과 (Reviewer 단독, 4 source cross-confirm)

**G4 §4.4.1 line 650 verbatim**: "Layer 4 — CI 회귀 검증 (MANDATORY)" + "Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증"

**ADR-012 §2.8 line 271 verbatim**: "Layer 4: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지"

→ Layer 4 = Layer 1+2 의 *회귀 검증 대상* → Layer 1+2 미발효 시 Layer 4 회귀 검증 대상 부재.

#### §4.4.2 (γ-d) 환원 정합화 (codex §5 + Agent A NT-A-1 + Agent B §5 답습)

(γ-d) 정합화 = 다음 中 하나:
1. Layer 4 cycle = planning-only 제한
2. Layer 1+2 PASS = Layer 4 PASS 선행조건 → 사실상 **(γ-a)**
3. Layer 1+2+4 동시 PASS evidence → 사실상 **(γ-c)**

#### §4.4.3 판정

**(γ-d) 모순 = CONFIRMED** (5 source verify: codex + Agent A + Agent B + Agent C + Reviewer 단독 verbatim verify = 5/5).

본 cycle 처리: (γ-d) "비권고" 표현 보존 (§2.6) + 모순 CONFIRMED 격상 (§2.4.5) + Layer 4 PASS 선발효 금지 명문.

---

## §5 Rollback Trigger / Evidence *후보 채택* (구현 발효 ≠ 본 합의, 52 entry N-1 답습 + N-9 흡수)

### §5.1 (γ) 채택 결정 후 Rollback Trigger 후보 (N-9 발화 시점 칼럼 추가)

| # | Trigger | 영역 | 발화 조건 | 발화 시점 (N-9 흡수) | 권위 답습 |
|---|---------|----|---------|------------------|---------|
| RT-γ-1 | Layer 1+2 PoC 시제 회귀 | 모든 (γ) 대안 | tools/* 본문 변경 시 PoC 시제 미작동 | 본 cycle 후 어느 cycle | 본 brief §2.5 답습 |
| RT-γ-2 | (γ-a) Layer 1+2 PASS 발효 지연 | (γ-a) | 합의 cycle 4회 지연 → Layer 4 PASS 발효 대기 | (γ-a) 채택 cycle 발효 시점 | §2.1.3 답습 |
| RT-γ-3 | (γ-b) Layer 1+2 evidence 분리 미명확 | (γ-b) | Layer 4 evidence 內 Layer 1+2 evidence 합산 | (γ-b) 채택 cycle 후 실 구현 sub-cycle 시점 | §2.2.3 답습 |
| RT-γ-4 ⭐ (N-6 흡수) | Layer 1+2 violation_type 검출 실패 | 모든 (γ) | PREV_HASH/HASH_RECALC/GENESIS_MISMATCH/HISTORY_REWRITE 4 violation_type 미작동 | 실 구현 sub-cycle 시점 | Agent A N-A-2 답습 |
| RT-γ-5 ⭐ (N-2 흡수) | (γ-d) Layer 4 PASS 선발효 시도 | (γ-d) | Layer 4 PASS 발효 + Layer 1+2 미발효 (모순 위반) | (γ-d) 채택 시 (비권고 답습) | §2.4.5 + B-1 답습 |
| RT-γ-6 ⭐ (N-3 흡수) | R-S1 cross-reference 정정 후행 영향 + **MVP-2 PASS 시점 선행/동시 정정 필요성 재평가** | 모든 (γ) | ADR-012 §2.3 본문 정정 시 (γ) 결정 영향 + MVP-2 Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 평가 | 본 cycle 후 + MVP-2 PASS 발효 cycle 시점 | 52 entry §9.5 + codex N-5 답습 |

### §5.2 Evidence Required (구현 발효 ≠ 본 합의, N-1 흡수)

(γ-c) 채택 시 PASS evidence template = **Layer 1/Layer 2/Layer 4 subsection 강제** (N-1 흡수).

| # | Evidence | 출처 |
|---|---------|------|
| E-γ-1 | (γ) 4 대안 평가 권고 합의 보고서 | 본 cycle Reviewer 통합 합의 |
| E-γ-2 | PoC 시제 답습 cross-check evidence | 본 brief §2.5 답습 |
| E-γ-3 | 외부 LLM 1+ 응답 (cross-vendor) | `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` |
| E-γ-4 | 후속 sub-cycle 진입 자격 발효 명문 | 본 cycle commit + push 후 자동 |

---

## §6 금지 사항

### §6.1 본 brief 자체 금지 사항

§0.3 답습 (27 항목).

### §6.2 본 brief 발효 후 후속 cycle 진입 시점 금지 사항

| # | 금지 영역 | 의무 답습 |
|---|---------|---------|
| 1 | 자동 후속 sub-cycle 진입 ((γ-c) 또는 (γ-a) 채택 결정 → 실 구현) | 사용자 명시 의무 |
| 2 | 자동 (β) sub-수단 결정 cycle 진입 | 사용자 명시 의무 |
| 3 | (γ-d) Layer 4 PASS 선발효 (Layer 1+2 PASS 부재 시) ⭐ (B-1 답습) | 영구 금지 (planning-only 제한) |
| 4 | MVP-2 Implementation Evidence PASS 자동 선언 | 별도 합의 |
| 5 | 외부 library 자동 도입 | 별도 cycle |
| 6 | G4 §4.4 Layer 3 + Layer 5 자동 진입 | 별도 cycle |
| 7 | branch protection contexts 자동 추가 | 사용자 admin scope |
| 8 | ADR 본문 갱신 자동 cross-reference 변경 | 별도 commit |
| 9 | R-S1 cross-reference 정정 자동 진입 | 별도 cycle (RT-γ-6 답습) |
| 10 | (γ-e/f/g) hybrid 대안 결정 자동 진입 ⭐ (B-8 답습) | 별도 cycle 사용자 명시 |

---

## §7 외부 LLM 응답 요구 영역 (사용자 영역)

### §7.1 외부 LLM 1+ 권고 출처

1. 52 entry brief §8.1 + §4.2 + Reviewer 합의 §4.2 답습
2. 헌법 5조-2 Provider Liquidity (비협상)
3. ADR-011 §2.1 (a)~(d) + (e) + §2.4 T3 영역
4. cross-vendor 형식 충족 (OpenAI ≠ Anthropic)

### §7.2 외부 LLM 자격 옵션 (N-15 명칭 충돌 정정 답습)

| 옵션 | 영역 | 합의 형태 |
|------|----|---------|
| **(E-α)** Claude tmux + codex bypass sandbox 직접 호출 | 24/52 entry 답습 | 풀 3+1 + 외부 LLM 1+ |
| **(E-β)** 사용자 직접 외부 LLM 호출 (codex + Gemini 등 추가) | 24 entry 외 옵션 | 풀 3+1 + 외부 LLM 2+ |
| **(E-γ)** 외부 LLM 0 (작은 영역 결정 시점) | 1-Agent + Reviewer 또는 풀 3+1만 | 작은 영역 |

본 (γ) cycle 실 호출: **(E-α) 답습 발효 완료** (2026-05-28).

### §7.3 외부 LLM 응답 *입력 자료* (호출 시점, N-11 흡수)

| 필수 입력 | 자료 위치 |
|---------|---------|
| 본 (γ) brief v1 | `docs/phase0/mvp2-gamma-layer-separation-brief.md` |
| 52 entry (α) brief v1.1 | `docs/phase0/mvp2-entry-brief.md` |
| 52 entry Reviewer 통합 합의 | `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` |
| 51 entry audit brief | `docs/phase0/mvp2-entry-eligibility-audit-brief.md` |
| `provider-agnostic-memory-skill-design.md §4.4.1` | 답습 source |
| `ADR-012 §2.3 + §2.8` (R-S1) | 답습 source |
| **`ADR-011 §2.1` + `PROJECT_CONSTITUTION` (헌법 8조 + 5조-2)** ⭐ (N-11 흡수) | 답습 source |

---

## §8 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 (γ) 합의 APPROVE WITH CONDITIONS → brief v1.1 보강 commit + push 후 발효:

1. **(γ) 4 대안 中 채택 결정** — Reviewer 통합 권고 ((γ-c) 1순위 + (γ-a) 2순위) 답습 + 사용자 명시 결정 (별도 cycle)
2. **(β) sub-수단 결정 cycle** — R-1~R-5 + L-1~L-5 + W-A~E (별도 합의)
3. **Layer 1+2 PASS 격상 sub-cycle** ((γ-a) 채택 시) 또는 **Layer 1+2+4 통합 PASS 격상 cycle** ((γ-c) 채택 시)
4. **실 구현 sub-cycle** — Hermes upstream + 본 repo P1 facade + Layer 1+2+4 PoC → PASS + R-6 workflow 확장
5. **MVP-2 Implementation Evidence PASS 발효 합의** — (a)~(d) 4조건 evidence + (e) 후속 운영조건 + 사용자 명시 (32 entry 답습 + RT-γ-6 R-S1 정정 사전조건 평가)
6. **R-S1 cross-reference 정정 cycle** — ADR-012 §2.3 본문 정정 또는 §2.8 동형 답습 cross-reference 강화
7. **ADR 본문 cross-reference 갱신 별도 commit** — ADR-008/012/011

본 brief 합의는 다음 단계 진입을 *발생시키지 않음* — 사용자 명시 의무.

---

## §9 답습 참조

### §9.1 상위 권위

- 헌법 제8조 (보안) — `docs/constitution/PROJECT_CONSTITUTION.md`
- 헌법 제5조-2 (Provider Liquidity 비협상) — 동상
- ADR-011 §2.1 (a)~(d) 4조건 모법 + §3 후속 권위 (e) — `docs/decisions/ADR-011-means-vs-ends-redaction.md`

### §9.2 직접 선행 자료

- 본 cycle Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` (264줄, BLOCKING 8 + 권고 16)
- 본 cycle codex 응답 — `docs/external-review/2026-05-28-mvp2-gamma-codex-response.md` (3284줄)
- 52 entry (α) entry brief v1.1 — `docs/phase0/mvp2-entry-brief.md`
- 52 entry Reviewer 통합 합의 — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md`
- 51 entry audit brief — `docs/phase0/mvp2-entry-eligibility-audit-brief.md`
- `implementation-runtime-roadmap-mvp1.md`
- `governance-preconditions.md §4`
- `provider-agnostic-memory-skill-design.md §4.4`
- `ADR-012-evidence-ledger-protection.md §2.3 + §2.5 + §2.7 + §2.8 + §3.4`

### §9.3 메타 영역 (52 entry Agent A 답습 + B-5 답습 정직 명시)

실 repo PoC 시제 (filesystem evidence, 본 cycle 시점 2026-05-28):
- `tools/jsonl_hash_chain.py` (14038B, genesis hash + 4 violation_type: PREV_HASH_MISMATCH + HASH_RECALCULATION + HISTORY_REWRITE + GENESIS_MISMATCH)
- `tools/canonical_json.py` (10055B, rfc8785 + jcs + jq -S -c fallback + cross-check mode)
- `tests/canonical/` (8 카테고리 verify 충족 / 24 fixture 정량 = 52 entry Agent A carry-over, 본 cycle 직접 count 1-pass 부재 정직 명시 — B-5 흡수)
- `.github/workflows/g4-hash-chain.yml` (10652B, 7 step 분리)
- `.github/workflows/history-anchor-verifier.yml` (19094B)
- `.github/workflows/rewrite-defense.yml` (16454B)
- `.github/workflows/r2-canary.yml` (5476B) ⭐ (N-7 추가, Agent A 답습)

### §9.4 cross-reference 갱신 영역 (N-16 + N-7 흡수)

- (γ-c) 채택 시 = Layer 1+2+4 통합 evidence cross-reference (Layer 4 evidence 內 분리 명시, N-1 답습)
- (γ-a) 채택 시 = Layer 1+2 PASS 격상 + Layer 4 PASS 격상 evidence cross-reference (단계적)
- (γ-d) 채택 시 = Layer 4 단독 + Layer 1+2 별도 cycle (planning-only 제한, B-1 답습)
- R-S1 cross-reference 정정 (52 entry §9.5 답습)
- ⭐ **roadmap.md §5.3 그룹 C+D 분리 progression 답습 명문 보강** (N-16 흡수) — 본 (γ) cycle = 그룹 C 內 Layer 분리 영역 결정 한정, 그룹 D (GP-2) 와의 통합 가능성 = W-D 답습

---

## §10 본 brief v1 작성 자격 자기진단 (메타 편향 회피)

| # | 위험 | 본 brief 의 처리 |
|---|------|--------------|
| P-1 | 본 brief 가 (γ) 특정 대안 (γ-c) 권고 방향으로 편향 | §0.3 + §6.2 27+10 금지 + §2.6 권고 매트릭스 = Reviewer 통합 권고 한정 (수단 결정 ≠ 본 cycle, §0.4 답습) |
| P-2 ⭐ (B-1 답습 격상) | **(γ-d) 모순 risk CONFIRMED 격상** — 본 brief 자체에서 결정 무단 침입 risk | §2.4.5 + §4.4 답습 = 5 source verify (codex + Agent A + Agent B + Agent C + Reviewer 단독). 본 cycle 처리 = "비권고" 표현 보존 (§2.6) + 모순 CONFIRMED 격상 + Layer 4 PASS 선발효 금지 명문 (planning-only 제한) |
| P-3 | 52 entry framing ((γ-d) 현 framing) 단방향 답습 cascade | §2.4 (γ-d) 단점 명시 + §2.6 비권고 + §4.4 모순 CONFIRMED 답습 |
| P-4 | R-S1 cross-reference 정정 후행 영향 (RT-γ-6) 본 cycle 결정 영향 | §5.1 RT-γ-6 명시 + §9.4 = 별도 cycle 영역 답습 |
| P-5 | PoC 시제 답습 발견 (§2.5) 이 본 cycle 결정 단순화 risk | §2.5 PoC 시제 충족 / PASS 시제 미충족 격상 답습 + Layer 2a `denyNonFastForwards` 활성화 evidence 1 영역 별도 verify 명시 (B-3 답습) + 24 fixture 정량 carry-over 정직 명시 (B-5 답습) |
| P-6 | 외부 LLM 1+ 권고 사용자 영역 침입 risk | §7.2 자격 옵션 3 (사용자 영역 결정) + 본 cycle 실 호출 (E-α) 답습 발효 완료 |
| P-7 ⭐ (N-4 + N-13 흡수) | **본 brief 작성자 = 52 entry brief 작성자 (Claude Opus 4.7) → 답습 cascade risk + cross-vendor blind 의문** | §1.3 선차 변경 매트릭스 명시 + §4.4 모순 risk 발견 (52 entry framing 답습 한정) + Reviewer 통합 합의 시 cross-check 영역 (Agent A/B/C 3 병렬 독립 + **외부 LLM codex (OpenAI gpt-5.5) cross-vendor 검증** = 4 source vendor 분포: Claude 3 + OpenAI 1 = cross-vendor 형식 충족, 헌법 5조-2 답습) |

---

## §11 v1.1 보강 매트릭스 (BLOCKING 8 + 권고 16 1pass 흡수)

본 v1.1 = `docs/review/3plus1-consensus-2026-05-28-mvp2-gamma.md` §5 답습 1pass 흡수 (별도 v2 cycle 0).

### §11.1 BLOCKING 8 흡수 매트릭스

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| B-1 ((γ-d) CONFIRMED 격상) | §2.4.5 신규 + §2.6 + §4.4 신규 + §5.1 RT-γ-5 + §6.2 #3 + §10 P-2 | "잠재 risk" → "CONFIRMED divergence" 격상 + 5 source verify + Layer 4 PASS 선발효 금지 명문 (planning-only 제한, 환원 분석) |
| B-2 (§2.6 표 순위 통일) | §2.6 | "본 brief 권고" → "Reviewer 통합 순위" 표기 통일 + (γ-c) 1순위 + (γ-a) 2순위 + (γ-b) 3순위 + (γ-d) 비권고 |
| B-3 (Layer 2 PoC evidence 분리) | §2.5 Layer 2 row 분리 (2a + 2b) | local workflow PoC (denyNonFastForwards 활성화 evidence 별도 verify 명문) + remote/admin branch protection rule (43 entry 8 contexts 답습) |
| B-4 ((γ-a) "N회" 정량) | §2.1.3 + §2.6 매트릭스 | (γ-a) = 4 cycle / (γ-b) = 1 cycle / (γ-c) = 3 cycle 등가 / (γ-d) = 2+ cycle (비권고) |
| B-5 (24 fixture 정량 carry-over) | §2.5 + §9.3 | "tests/canonical/ 24 fixtures" → "8 카테고리 verify 충족 / 24 fixture 정량 = 52 entry Agent A carry-over (본 cycle 직접 count 1-pass 부재 정직 명시)" |
| B-6 ((γ-c) "부분 답습" 정정) | §2.3.2 + §2.6 | "defense-in-depth 답습 충실" → "defense-in-depth *부분 답습* (Layer 1+2+4 한정, Layer 3+5 = 본 cycle scope 외)" |
| B-7 (§2.4.4 영역 침입 정정) | §2.4.4 + §2.4.5 | "(γ-d) = 사실상 (γ-a) 동등" → "(γ-d) PASS 발효 구조 환원 분석" + "결정 자격 = 풀 3+1 + 사용자 명시 영역 (§2.6 비권고 답습 보존)" |
| B-8 ((γ-e/f/g) 추가 hybrid 매트릭스) | §2.7 신규 | (γ-e) (γ-a)+(γ-d) hybrid + (γ-f) PoC 시제 보존 한정 + (γ-g) 시점 vs evidence 분리 = 평가만, 결정 = 별도 cycle |

### §11.2 권고 16 흡수 매트릭스

| # | 흡수 영역 | 답습 |
|---|---------|-----|
| N-1 ((γ-c) layer subsection 강제) | §2.3.3 + §5.2 | (γ-c) PASS evidence template Layer 1/2/4 subsection 강제 |
| N-2 ((γ-d) PASS 선발효 금지 명문) | §2.4.5 + §5.1 RT-γ-5 + §6.2 #3 | B-1 답습 |
| N-3 (RT-γ-6 R-S1 PASS 시점 선행/동시 정정) | §5.1 RT-γ-6 | "본 (γ) cycle 자동 진입 대상 아님 / MVP-2 PASS 발효 시점 선행/동시 정정 필요성 재평가" |
| N-4 (cross-vendor 명시) | §4.1 + §7.1 + §10 P-7 | 본 외부 검토 = OpenAI codex / 풀 3+1 Agent = Anthropic Claude / cross-vendor 형식 충족 |
| N-5 (step prefix [Layer N]) | §2.3.1 + §9.3 | g4-hash-chain.yml 7 step 답습 시 step prefix `[Layer N]` |
| N-6 (4 violation_type Layer 매핑) | §2.5 + §5.1 RT-γ-4 | PREV_HASH/HASH_RECALC/GENESIS_MISMATCH = Layer 1, HISTORY_REWRITE = Layer 2 |
| N-7 (r2-canary 추가) | §9.3 | r2-canary.yml 5476B 추가 |
| N-8 (trigger (5) framing 정밀화) | §4.3 (5) | "부분 발화" → "사용자 영역 결정 발화" |
| N-9 (RT-γ 발화 시점 칼럼) | §5.1 표 | 각 RT-γ-X 발화 시점 칼럼 |
| N-10 ("수단 결정 0" 강화) | §2.6 | "Reviewer 통합 권고 한정, 수단 *결정* = 풀 3+1 + 사용자 명시 영역" 강조 |
| N-11 (외부 LLM 입력 자료 보강) | §7.3 | ADR-011 + 헌법 추가 |
| N-12 (R-S1 후행 영향 row) | §1.3 항목 4 | R-S1 후행 영향 row 추가 |
| N-13 (cross-vendor blind 명문) | §10 P-7 | 4 source = Claude 3 + OpenAI 1 명문 |
| N-14 ((γ-c) 1순위 검증 보강) | §2.6 | B-6 부분 답습 정합 후 (γ-c) 1순위 |
| N-15 (외부 LLM 자격 옵션 명칭 충돌 정정) | §7.2 | (α)/(β)/(γ) → (E-α)/(E-β)/(E-γ) 명칭 분리 |
| N-16 (roadmap §5.3 그룹 분리) | §9.4 | roadmap.md §5.3 그룹 C+D 분리 progression 답습 |

### §11.3 v1.1 1pass 흡수 정직성

- 본 cycle = 1pass 흡수 (ceremony-inflation 차단 메모리 답습, 24/52 entry 동형 패턴)
- 별도 v2 cycle 0건
- 본 v1.1 보강 시 추가 신규 자기 발견 잠재 risk = §10 P-2 + P-7 추가 (B-1 + N-4/13 답습) 한정

---

**본 brief v1.1 끝.**

**다음 단계**: SESSION + INDEX commit + push (53 entry) → 본 cycle 합의 발효 (APPROVE WITH CONDITIONS 격상 자동) → (γ) 4 대안 中 채택 결정 + (β) + 실 구현 + MVP-2 PASS 발효 = 사용자 명시 별도 cycle.
