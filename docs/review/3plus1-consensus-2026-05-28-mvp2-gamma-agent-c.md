# 풀 3+1 합의 — (γ) MVP-2 G4 §4.4 Layer 분리 영역 결정 — Agent C (대안 탐색가) 응답

> **검토자**: Agent C — 대안 탐색가 (Anthropic Claude Opus 4.7 [1M context])
> **검토 대상**: `docs/phase0/mvp2-gamma-layer-separation-brief.md` (v1, 482줄, 53번째 entry 진입 cycle)
> **합의 형태**: 풀 3+1 + 외부 LLM 1+ (사용자 영역, §7.2 답습)
> **검토 일자**: 2026-05-28
> **핵심 질문 (CLAUDE.md §3 답습)**: **"더 나은 방법이 있는가?"** — 대안 기술, 트레이드오프
> **편향 회피**: Agent A / Agent B / codex 응답 *참조 0건* (병렬 독립 평가). 본 응답 = 53 entry brief v1 + 52 entry brief v1.1 + 52 entry Reviewer 통합 합의 + provider-agnostic-memory-skill-design §4.4.1 + ADR-012 §2.3 + §2.8 + roadmap.md §4 + §5.3 + §6 직접 read 결과 한정.

---

## 직접 read 한 자료 path 목록

본 Agent C 평가 진입 *전* 직접 read 완료 자료 (병렬 독립 평가 답습 의무):

1. `docs/phase0/mvp2-gamma-layer-separation-brief.md` (v1, 482줄) — PRIMARY 검토 대상
2. `docs/phase0/mvp2-entry-brief.md` (v1.1, 603줄) — 52 entry 답습 source
3. `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` (257줄) — 52 entry Reviewer 통합 합의 (BLOCKING 7 + 권고 13 발견 매트릭스)
4. `docs/architecture/provider-agnostic-memory-skill-design.md §4.4` (line 620~710) — G4 §4.4.1 5-layer 직접 정의 PRIMARY 권위
5. `docs/decisions/ADR-012-evidence-ledger-protection.md §2.3` (line 155~190) — 4-layer numbering (R-S1 발견 source)
6. `docs/decisions/ADR-012-evidence-ledger-protection.md §2.8` (line 264~272) — 5-layer numbering (R-S1 발견 source)
7. `docs/architecture/implementation-runtime-roadmap.md §4` (G4 7 영역) + §5.3 그룹 progression + §6 그룹 C+D 답습 분리

---

## §0 총평

**Agent C 판정**: **REVISE** (BLOCKING 3 + 권고 5 + NOTE 2)

**판정 근거 요약**:

1. **53 brief §1.2 의 (γ) 4 대안 정의 자체에 누락 알고리즘 risk** — `(γ-d)` 가 "Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle 분리" 로 정의되어 있으나, 본 brief §2.4.4 自身에서 "(γ-d) = 사실상 (γ-a) 와 동등 (시점 차이 한정)" 자기 발견. 4 대안 자체가 **3 *실질* 대안 (γ-a / γ-b / γ-c) + 1 가상 framing 대안 (γ-d)** 으로 *축약 가능* — 사용자 결정 영역 의 명확성 부담 ↑. 풀 3+1 합의 대상 4 → 실 3 축약 framing 정정 자격 영역 (R-C-1 BLOCKING).
2. **빠진 대안 (γ-e/f/g) 추가 식별 의무** — 4 대안 全 모두 "Layer 1+2 + Layer 4 *동시 또는 순서* 결정" 한정 framing. **시점 분리 + 통합 evidence (γ-g)** / **PASS 격상 격하 + PoC 시제 답습만 (γ-f)** / **(γ-a)+(γ-d) hybrid (γ-e)** 영역 추가 평가 의무 (R-C-2 BLOCKING).
3. **합의 형태 매트릭스 자체 미흡 — 본 cycle 자격이 "큰 결정" 이라는 framing 의 근거 제시 fragile** — §4.3 trigger 1/7 발화 + 1 부분 발화 (5 발화 = 사용자 영역) — 1.5/7 발화로 "풀 3+1 + 외부 LLM 1+" 권고는 ceremony-inflation 자기 진단 (MEMORY 답습) 의무 영역. 큰/작은 영역 framing 자체 정정 자격 (R-C-3 BLOCKING).

**판정 등급 정당화**:
- REVISE > APPROVE WITH CONDITIONS — 4 대안 framing 자체 가 (γ-d) 자기모순 인정 후에도 *대안 추가 없이* 풀 3+1 합의 진입 = framing 정정 후 진입 의무
- REVISE < REJECT — 본 brief v1 작성 자격은 충실 (자기진단 §10 P-1 ~ P-7 적합 + cross-reference 답습 모두 정합 + ceremony 0 추가)
- v1.1 1pass 흡수 (52 entry 답습 동형 패턴) = REVISE → APPROVE WITH CONDITIONS 격상 가능 영역

---

## §1 BLOCKING 3건

### R-C-1 ⭐ (γ-d) 가상 framing 영역 vs 실 대안 축약 자격

**영역**: brief §1.2 + §2.4 + §2.6 권고 매트릭스

**발견**:
- brief §2.4.4 자기 발견: **"(γ-d) = 사실상 (γ-a) 와 동등 (시점 차이 한정)"** 명문
- brief §2.6 권고 매트릭스에서 (γ-d) = "비권고 (모순 risk)" 처리
- 즉, **4 대안 中 (γ-d) = 가상 framing 한정 (실 대안 ≠)** — 51 entry framing 답습 (52 entry framing 답습 cascade)
- 4 대안 = "(γ-a) Layer 1+2 우선 / (γ-b) Layer 4 단독 / (γ-c) 동시 / (γ-d) Layer 4 단독 + 별도" 中 (γ-b) ≈ (γ-d) 합의 형태 동등 가능성 + (γ-d) ≈ (γ-a) 시점 동등 = **실 3 대안 축약** 영역
- 풀 3+1 합의 대상 "4 대안 中 채택" 표현 = 사용자 명확성 부담 ↑ (가상 framing + 실 대안 혼동)

**충돌 영역**:
- 52 entry brief §2.2.4 — (γ-d) 가 "현 brief framing" 답습 한정
- 본 53 brief §0.3 #25 (R-S1 cross-reference 정정 자동 진입 0건) 답습 패턴 = "framing 정정 = 별도 cycle 사용자 명시"
- 즉, **53 brief 자체 内 framing 정정 = 권위 한계 자격 = R-C-1 BLOCKING** (사용자 명시 의무)

**처리 권고** (사용자 영역):
- (a) v1.1 보강 시 §1.2 + §2.4 + §2.6 매트릭스에 "(γ-d) = 가상 framing 한정, 실 대안 ≠" 추가 명문 + 4 대안 → 실 3 대안 (γ-a / γ-b / γ-c) 축약 framing 명시
- 또는 (b) (γ-d) 유지 + "가상 framing 답습 (52 entry framing 답습 cascade) — 채택 시 실 (γ-a) 시점 분리 답습" 명문 추가
- 또는 (c) 별도 cross-reference 정정 cycle (52 entry framing 답습 정정) 사용자 명시

**BLOCKING 자격**: 실 풀 3+1 합의 대상 framing 명확성 = 본 합의 발효 자격 직접 충족 영역 (가상 framing 4 대안 = "사용자 명시 결정" 자격 부족 risk).

### R-C-2 ⭐ 추가 대안 (γ-e/f/g) 정의 + 평가 의무

**영역**: brief §1.2 + §2 + §8

**발견**:
- brief §1.2 (γ) 4 대안 정의 = "Layer 1+2 + Layer 4 *동시 또는 순서* 결정" 한정 framing
- 다음 추가 대안 영역 brief 内 평가 0건:

| 대안 | 정의 | 본 cycle 평가 자격 |
|------|-----|----------------|
| **(γ-e)** | (γ-a) + (γ-d) hybrid — Layer 4 단독 진입 권한 발효 + Layer 1+2 = MVP-2 *동시 진입 자격* 발효 + Layer 1+2 별도 sub-cycle 분리 | 사용자 영역 결정 자격 (현 (γ-a) 단계적 + (γ-d) 분리 hybrid framing) |
| **(γ-f)** | Layer 1+2 = PoC 시제 답습 보존 한정 (PASS 격상 영구 또는 후속 cycle 0) + Layer 4 PASS 격상 단독 + Layer 1+2 PoC 시제 답습 의무 | PoC 시제 보존 한정 영역 (PASS 격상 = 별도 트리거 의무) |
| **(γ-g)** | 시점 분리 vs 통합 evidence 영역 분리 — 본 (γ) cycle = *시점* 분리 / MVP-2 Implementation Evidence PASS 발효 시 = *통합 evidence* | 시점 결정 vs evidence 결정 영역 분리 framing |

- 본 brief §2.4.4 = "(γ-d) = 사실상 (γ-a) 동등 (시점 차이 한정)" 자기 발견 = 시점 결정 영역 framing 가능성 입증
- (γ-e/f/g) 中 어느 것이라도 brief 内 미평가 → 사용자 결정 영역 의 정보 부족 risk

**충돌 영역**:
- brief §0.4 권위 한계 = "(γ) 4 대안 中 채택 결정 발효" 한정 → 4 대안 自身 完整 영역 정의 의무
- brief §2.6 권고 매트릭스 = "4 대안 中 (γ-c) 1순위 + (γ-a) 2순위" 권고 → 4 대안 만 권고 영역 한정 risk

**처리 권고** (사용자 영역):
- (a) v1.1 §1.2 + §2 추가 (γ-e/f/g) 대안 매트릭스 추가 (또는 적어도 §10 자기진단 P-X 명문)
- 또는 (b) "4 대안 외 추가 대안 = 본 cycle scope 외 별도 cycle 영역" 명문 (현 brief §0.3 답습 패턴 = 권위 한계 명문)
- 또는 (c) "(γ-e) hybrid = (γ-a) 답습 시점 분리 + (γ-d) framing 영역 결정 분리 — 본 brief 내 (γ-a) 동등 영역 평가, 별도 (γ-e) 명시 0" 답습

**BLOCKING 자격**: 4 대안 中 채택 결정 합의 자격 = 4 대안 完整 영역 정의 자격 = R-C-2 BLOCKING.

### R-C-3 ⭐ 합의 형태 "큰 결정" framing 자체 근거 fragile

**영역**: brief §4.1 + §4.3 + §7.2

**발견**:
- brief §4.1 = "풀 3+1 + 외부 LLM 1+ (사용자 영역 결정)" 권고 — 정당화 출처 5개
- brief §4.3 7 풀 3+1 승격 트리거 검증 = **1/7 발화 + 1 부분 발화** → 풀 3+1 + 외부 LLM 1+ 권고
- 1/7 발화 + 1 부분 발화 = **합의 형태 fragile 명문 자격**
- MEMORY `feedback_ceremony_inflation` + `feedback_meta_cycle_warning` 답습 = "큰 영역 framing 자기 점검 의무"

**평가 영역 (Agent C 대안 탐색가 관점)**:

| 가능 합의 형태 | trigger 발화 매트릭스 | 사유 |
|----------|-------------------|----|
| **풀 3+1 + 외부 LLM 1+ (현 권고)** | 1/7 + 1 부분 = 1.5/7 | 52 entry §8.1 답습 + 큰 영역 framing |
| **풀 3+1 + 외부 LLM 0** | 1/7 + 1 부분 = 1.5/7 | 작은 영역 framing (γ 시점 결정 한정 = 4 대안 중 채택) + 52 entry α 합의 후 carry-over 영역 |
| **1-Agent + Reviewer 단축** | 1/7 + 1 부분 = 1.5/7 | 시점 결정 한정 + α 합의 답습 발효 후 |

- 본 brief §7.2 = "(γ) 외부 LLM 0 (풀 3+1만, 작은 영역 결정)" 옵션 自身 명문 → "작은 영역" framing 자격 명문
- 즉, **본 cycle = 큰 영역 vs 작은 영역 framing 자체 미결정** → 합의 형태 권고 fragile risk

**충돌 영역**:
- 52 entry brief §8.1 + §4.2 = "(γ) 분리 영역 결정 = 풀 3+1" 권고 답습 → 본 brief 풀 3+1 권고 정당화
- 그러나 trigger 검증 1.5/7 = "큰 결정" 자격 fragile
- MEMORY `feedback_ceremony_inflation` = "lint·framing·citation 정정 = 1-agent 직접" 답습 → framing 정정 영역 = 단축 자격
- 본 cycle 의 발효 효과 = "4 대안 中 채택 결정 발효" 만 → 시점 분리 결정 = "framing 영역" 자격 평가 의무

**처리 권고** (사용자 영역):
- (a) brief §4.1 + §4.3 + §7.2 = "본 cycle = 큰 영역 (52 entry §8.1 답습) vs 작은 영역 (시점 분리 결정 framing) 결정 = 사용자 영역" 명문 추가
- 또는 (b) trigger 발화 1.5/7 → "발화 부족이지만 52 entry §8.1 답습 + 큰 영역 framing 우선" 명문
- 또는 (c) 합의 형태 권고 격하 (풀 3+1 + 외부 LLM 1+ → 풀 3+1 한정) + 외부 LLM 1+ = 사용자 영역 선택 자격

**BLOCKING 자격**: 합의 형태 정당화 fragile = 본 합의 발효 자격 직접 충족 영역 = R-C-3 BLOCKING.

---

## §2 권고 5건 (대안 매트릭스 포함)

### N-C-1 권고 매트릭스 fragile — (γ-c) 1순위 권고 자격 검증 보강

**영역**: brief §2.6

**현 brief §2.6 권고 매트릭스**:
- (γ-c) 1순위 (defense-in-depth + 효율) / (γ-a) 2순위 (안전 + 의존 답습) / (γ-b) 3순위 / (γ-d) 비권고

**Agent C 발견**:
- (γ-c) "defense-in-depth" 효과 = ADR-012 §2.8 5-layer 답습 한정 (Layer 1+2+4 동시 진입)
- 단, (γ-c) "합의 부담 ↑ (Layer 1+2+4 통합 + 각 layer evidence 분리)" 명문 (§2.3.3) — 큰 영역 자격
- (γ-a) "단계적 안전 + 의존 chain 정확 답습" 명문 (§2.1.2) — 안전 자격
- **두 권고 모두 정합 (1순위 vs 2순위 결정 = trade-off 영역)** → 사용자 영역 결정 의무

**권고 보강**:
- v1.1 시점 §2.6 권고 매트릭스에 다음 명문 추가:
  - "(γ-c) 1순위 = defense-in-depth + 효율 (Layer 1+2+4 evidence 분리 시점 통합 비용 ↑)"
  - "(γ-a) 2순위 = 단계적 안전 + 합의 부담 분산 (시간 부담 ↑)"
  - "사용자 결정 영역 = '안전 vs 효율' trade-off — 본 brief 권고 ≠ 사용자 결정"

### N-C-2 ⭐ 추가 대안 (γ-e/f/g) hybrid 영역 매트릭스 추가

**영역**: brief §1.2 + §2 + §8

**발견** (R-C-2 답습 보강):

| 대안 | 정의 | 의존 chain | 합의 cycle | 효과 |
|------|----|---------|---------|----|
| **(γ-e) hybrid** | (γ-a) 단계적 + (γ-d) 분리 hybrid — Layer 4 진입 권한 발효 + Layer 1+2 = MVP-2 *동시 진입 자격* 발효 + Layer 1+2 PASS 격상 sub-cycle 분리 | 의존 답습 충실 | 2 cycle (Layer 1+2 PASS sub-cycle + Layer 4 PASS sub-cycle 동시 또는 순차) | 합의 부담 분산 + 의존 chain 답습 |
| **(γ-f) PoC 시제 한정** | Layer 1+2 = PoC 시제 답습 보존 한정 (PASS 격상 = 별도 trigger 의무) + Layer 4 PASS 격상 단독 | Layer 4 = "PoC 시제 회귀 검증" framing (PASS 시제 ≠) | 1 cycle (Layer 4 PASS 격상 + Layer 1+2 PoC 답습) | (γ-d) 모순 risk 회피 (Layer 1+2 PASS ≠ 의무) |
| **(γ-g) 시점 vs evidence 분리** | 본 (γ) cycle = *시점* 분리 결정 / MVP-2 Implementation Evidence PASS 발효 시 = *통합 evidence* (4 대안 中 어느 것 채택해도 PASS 발효 시 통합) | 본 cycle = 시점 결정 / PASS 발효 cycle = evidence 결정 | 본 cycle 1 + PASS cycle 1 | 영역 분리 명확화 |

**(γ-f) 의 특수성**:
- (γ-d) "의존 chain 모순 risk" (§2.4.3) 회피 가능
- Layer 4 = "PoC 시제 회귀 검증" framing (Layer 1+2 *PASS 시제* 의존 ≠) 가능성
- PASS 시제 = Layer 1+2 PoC 시제 + Layer 4 PASS 시제 = "최소 PASS 구성"
- 단, Layer 4 = "회귀 검증" 의미 부재 risk (회귀 *대상* = Layer 1+2 PASS) — (γ-d) 모순 risk 부분 답습

**(γ-g) 의 특수성**:
- 본 cycle scope 自身 = "시점 결정" 영역 한정 — evidence 결정 영역 ≠
- 4 대안 中 어느 것 채택해도 MVP-2 PASS 발효 시 = 통합 evidence 의무 (다층 답습)
- 즉, **본 cycle = "시점 + 합의 cycle 구조" 결정 한정 / PASS evidence 통합 = 별도 cycle** framing 가능

**권고 보강**:
- v1.1 §1.2 또는 §8 에 (γ-e/f/g) 명문 추가 (적어도 NOTE 형식)
- 또는 §10 자기진단 P-8 신설 (추가 대안 미평가 risk)

### N-C-3 외부 LLM 자격 옵션 (α / β / γ) framing 명확화

**영역**: brief §7.2

**현 brief §7.2**:

| 옵션 | 영역 | 합의 형태 |
|------|----|---------|
| (α) Claude tmux + codex bypass sandbox | 24/52 entry 답습 | 풀 3+1 + 외부 LLM 1+ |
| (β) 사용자 직접 외부 LLM 호출 (codex + Gemini) | 24 외 옵션 | 풀 3+1 + 외부 LLM 2+ |
| (γ) 외부 LLM 0 (풀 3+1만, 작은 영역 결정) | 1-Agent + Reviewer 또는 풀 3+1만 | 작은 영역 결정 시점 |

**Agent C 발견**:
- (γ) 옵션 명칭 = "(γ) 외부 LLM 0" — **본 cycle 자체 명칭 (γ) 와 충돌** (혼동 risk)
- 본 brief 全体 가 "(γ) cycle" framing 답습 → (γ) 옵션 = "(γ) cycle 內 외부 LLM 0" 혼동 가능
- 단순한 lint 정정 영역 (옵션 명칭 변경 = ceremony 0)

**권고 보강**:
- v1.1 시점 §7.2 옵션 명칭 정정: (γ) → (γ-LLM-0) 또는 (옵션 C) 등 명확화
- 또는 NOTE 명문 (혼동 risk 답습 명문 한정)

### N-C-4 R-S1 cross-reference 정정 후행 영향 (RT-γ-6) 평가 보강

**영역**: brief §5.1 RT-γ-6 + §9.4

**현 brief §5.1**: RT-γ-6 = "R-S1 cross-reference 정정 후행 영향 — ADR-012 §2.3 본문 정정 시 (γ) 결정 영향 (예: Layer 4 numbering 변경 시 본 cycle 결정 영역 변경)"

**Agent C 발견**:
- R-S1 = ADR-012 §2.3 (4-layer) vs §2.8 + G4 §4.4.1 (5-layer) divergence
- 본 brief §4.4 권위 인용 chain 정정 답습 → §2.8 + §4.4.1 5-layer numbering PRIMARY 한정
- 그러나 **§2.3 정정 = "Layer 4 = External anchor → CI 회귀 검증" 변경 시점** → 본 (γ) cycle 결정 "Layer 4 = CI 회귀 검증" framing 답습 의존
- 즉, **R-S1 정정 cycle 自身 = 본 (γ) cycle 결정 *후* 진행 시 모순 risk** (예: §2.3 → 5-layer 통합 동형 갱신 시 본 (γ) 결정 "Layer 4 = CI 회귀 검증" 답습 충돌 0건, 단 §2.3 → 4-layer 유지 갱신 시 본 cycle 결정 영역 변경 risk)

**권고 보강**:
- v1.1 시점 §5.1 RT-γ-6 보강 — "R-S1 정정 시점 = 본 (γ) cycle 결정 *후* 진행 권장 (cascade risk 회피)" 또는 "R-S1 정정 시점 = 본 (γ) cycle 결정 *선행* 의무 영역 결정 = 별도 cycle"
- 또는 N-13 (52 entry brief §9.5 답습) — "Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명문" 답습 보강

### N-C-5 roadmap.md §5.3 그룹 progression 답습 (그룹 C+D 분리) vs 본 cycle 통합 framing

**영역**: brief §1.1 권위 답습

**Agent C 직접 read 발견** (roadmap.md §5.3 line 172~186 + §5.4):
- 그룹 C (Order 3 tie) = G4 JSONL hash chain + RFC 8785 JCS + Round-trip PoC (G4 §4.4 영역 = Layer 1+2 PoC)
- 그룹 D (Order 4+5) = G2 GP-3 + G2 GP-2 (GP-2 = MVP-2 송신 redaction)
- §5.4 = 그룹 C / 그룹 D 모두 "단축 합의 + PoC evidence" 권고

**52 entry brief §1.3 항목 5 답습**:
- "roadmap.md §5.4 그룹 C+D 합의 형태 격상 ⭐ — '단축 합의 + PoC evidence' 권고 vs 본 cycle '풀 3+1 + 외부 LLM 1+' 격상"
- 정당화 = 사용자 명시 + roadmap-mvp1 §1.3 답습 + 32 entry MVP-1 PASS 발효 합의 패턴

**Agent C 평가**:
- 본 (γ) cycle = G4 §4.4 Layer 분리 영역 결정 한정 (그룹 C 內 G4 §4.4 영역만, G2 GP-2 + GP-3 그룹 D ≠)
- 즉, 본 (γ) cycle = "그룹 C 內 Layer 분리 영역 결정 한정 sub-cycle" framing 가능
- 그룹 C ≠ 그룹 D 분리 progression 답습 충실 (W-D 52 entry 답습)
- 단, brief 내 본 framing 명문 ≠ 명확 — 그룹 progression 답습 fragile

**권고 보강**:
- v1.1 시점 §1.1 권위 답습 매트릭스 + §1.3 선차 변경 매트릭스에 다음 명문 추가:
  - "본 (γ) cycle = roadmap.md §5.3 그룹 C 內 G4 §4.4 Layer 분리 영역 결정 한정 (그룹 D = GP-2 별도 (β) cycle 영역, 52 entry §2.3.2 W 5 대안 답습)"
  - "그룹 C+D 분리 progression 답습 = 본 cycle Layer 1+2 + Layer 4 영역 분리 결정 한정 (그룹 D = MVP-2 진입 자격 발효 영역, 본 cycle ≠)"

---

## §3 NOTE 2건

### NT-C-1 PoC 시제 답습 발견 (52 entry B-6 답습) 의 cascade 영향

**영역**: brief §2.5

**Agent C 직접 read 발견**:
- 본 brief §2.5 = "PoC 시제 충족 / PASS 시제 미충족" 매트릭스 명문 (모든 영역)
- tools/jsonl_hash_chain.py + canonical_json.py + tests/canonical/ + g4-hash-chain.yml 이미 운영 (52 entry Agent A 답습)
- **PoC 시제 充足 = 본 (γ) cycle 결정 단순화 risk** (PASS 격상 = 단순 합의 한정 framing 가능)

**NOTE**:
- §10 P-5 자기진단 답습 명문 충실 (PoC 시제 답습 발견이 본 cycle 결정 단순화 위험)
- 단, PoC 시제 충족 framing = "Layer 1+2+4 PASS 격상 = 최소 evidence" 답습 → (γ-c) defense-in-depth 자격 ↑
- Agent C 관점 = "PoC 시제 充足 의 후행 영향 평가 정합 (RT-γ-1 명문)"

### NT-C-2 본 brief 작성자 Claude Opus 4.7 + Agent C Claude Opus 4.7 cascade risk

**영역**: brief §10 P-7 + 본 Agent C 자기 진단

**발견**:
- 본 brief v1 작성자 = Claude Opus 4.7
- Agent C = Claude Opus 4.7 (동일 LLM)
- 52 entry brief v1 작성자 = Claude Opus 4.7
- 53 brief = 52 brief 답습 cascade
- 즉, **3-layer cascade risk** (작성자 = Agent A/B/C = Reviewer 모두 동일 vendor + 동일 LLM)

**NOTE**:
- 본 cycle 외부 LLM 1+ (codex via tmux) = cross-vendor 충족 자격 영역 (사용자 결정 의무)
- §7.2 옵션 (β) 사용자 직접 외부 LLM 호출 (codex + Gemini 등 추가 cross-vendor 강화) 자격 = 명문
- Agent C 답습 = "Claude vendor blind 충족 시점 = 외부 LLM 1+ 의무 (cross-vendor)" 답습

---

## §4 추가 대안 ((γ-e/f/g)) 식별 + 평가

### §4.1 (γ-e) hybrid 대안

**정의**: (γ-a) 단계적 + (γ-d) 분리 hybrid
- Layer 4 PASS 격상 sub-cycle 진입 권한 발효 + Layer 1+2 = MVP-2 *동시 진입 자격* 발효 + Layer 1+2 PASS 격상 sub-cycle 분리

**Trade-off**:
- ✅ 의존 chain 답습 충실 (Layer 1+2 PASS 발효 → Layer 4 PASS 발효 의존)
- ✅ 합의 부담 분산 (각 layer PASS sub-cycle 분리)
- ✅ Layer 4 진입 가능 시점 명확 (Layer 1+2 PASS 발효 후)
- ⚠️ 합의 cycle 2+ 부담 ((γ-a) 답습 답습)
- ⚠️ ceremony-inflation risk ((γ-a) 동등)

**(γ-a) 와 차이**: (γ-a) = "Layer 1+2 우선 → Layer 4 후속" 순서 결정 / (γ-e) = "Layer 4 + Layer 1+2 동시 진입 자격 발효 + Layer 1+2 PASS sub-cycle 분리" — 시점 결정 = 분리

**(γ-d) 와 차이**: (γ-d) = "Layer 4 단독 + Layer 1+2 별도 cycle 분리 (시점 미정)" / (γ-e) = "Layer 1+2 = MVP-2 *동시 진입 자격* 발효 명시 + Layer 1+2 PASS sub-cycle 분리" — 진입 자격 결정 = 동시

**평가**:
- (γ-e) ≠ (γ-a) 완전 동등 (시점 + 합의 cycle 구조 차이)
- (γ-e) ≠ (γ-d) 완전 동등 (진입 자격 결정 차이)
- 추가 대안 자격 정합 (R-C-2 답습)

### §4.2 (γ-f) PoC 시제 보존 한정 대안

**정의**: Layer 1+2 = PoC 시제 답습 보존 한정 (PASS 격상 = 별도 trigger 의무 / MVP-3 영역 분리 가능) + Layer 4 PASS 격상 단독

**Trade-off**:
- ✅ (γ-d) 의존 chain 모순 risk 회피 (Layer 4 = "PoC 시제 회귀 검증" framing 가능)
- ✅ 합의 cycle 1 (Layer 4 PASS 격상 + Layer 1+2 PoC 답습)
- ⚠️ Layer 4 = "회귀 검증" 의미 부재 risk (회귀 *대상* = Layer 1+2 PASS 시제 의무 가능)
- ⚠️ MVP-2 Implementation Evidence PASS 발효 자격 자체 fragile (Layer 1+2 PASS ≠ MVP-2 영역 = MVP-3 영역 분리 시점)

**(γ-c) 와 차이**: (γ-c) = "Layer 1+2+4 동시 PASS 발효" / (γ-f) = "Layer 4 PASS 발효 + Layer 1+2 PoC 답습 한정 (PASS 격상 = MVP-3 영역 가능)"

**평가**:
- (γ-f) = MVP-2 ↔ MVP-3 영역 결정 framing 변경 가능성 (Layer 1+2 PASS = MVP-3 영역 결정)
- 추가 대안 자격 정합 (R-C-2 답습) — 단 본 cycle = MVP-2 영역 한정 → (γ-f) MVP-3 영역 결정 = 본 cycle scope 외 가능성

### §4.3 (γ-g) 시점 분리 vs evidence 통합 분리 대안

**정의**: 본 (γ) cycle = *시점* 분리 결정 / MVP-2 Implementation Evidence PASS 발효 시 = *통합 evidence* (4 대안 中 어느 것 채택해도 PASS 발효 시 = 통합 evidence 의무)

**Trade-off**:
- ✅ 본 cycle scope 명확화 (시점 결정 한정)
- ✅ PASS 발효 = 통합 evidence (defense-in-depth 답습 자동)
- ✅ 4 대안 中 어느 것 채택해도 PASS 발효 = 동일 evidence (안전성)
- ⚠️ "시점 결정" vs "evidence 결정" 영역 분리 자체 framing 변경 (52 entry §8.1 답습 변경 risk)
- ⚠️ 사용자 결정 영역 추가 (시점 결정 = 본 cycle / evidence 결정 = MVP-2 PASS cycle)

**평가**:
- (γ-g) = 본 brief framing 자체 변경 가능성 (시점 결정 vs evidence 결정 분리)
- §10 자기진단 P-X 신설 영역 자격 (framing 정정 = 별도 cycle 사용자 명시)
- 추가 대안 자격 정합 (R-C-2 답습)

### §4.4 추가 대안 평가 매트릭스

| 대안 | 의존 chain 답습 | 합의 cycle 수 | PASS 발효 시점 | 본 brief 권고 |
|------|------------|------------|--------------|----------|
| (γ-a) | ✅ 답습 | 2+ | 단계적 | 2순위 (현 brief) |
| (γ-b) | ✅ 자동 | 1 | 동시 | 3순위 |
| (γ-c) | ✅ 답습 | 1 (큰) | 동시 | 1순위 (현 brief) |
| (γ-d) | ⚠️ 모순 | 2+ | Layer 4 우선 | 비권고 |
| **(γ-e) 추가** | ✅ 답습 | 2+ (분리) | Layer 4 우선 + Layer 1+2 후속 | 평가 미진행 |
| **(γ-f) 추가** | ⚠️ Layer 4 회귀 의미 부재 risk | 1 | Layer 4 단독 | 평가 미진행 (MVP-3 영역 가능) |
| **(γ-g) 추가** | ✅ 답습 (PASS 발효 시) | 1 (시점) + 1 (PASS) | 분리 (시점 vs evidence) | 평가 미진행 (framing 변경) |

---

## §5 4 대안 외 framing 대안 평가

### §5.1 52 entry framing 답습 ((γ-d) = "현 framing") vs 본 brief framing 정정

**발견**:
- 52 entry brief §2.2.4 = (γ-d) "현 brief framing" (Layer 4 단독 + Layer 1+2 별도 cycle 분리)
- 본 53 brief §2.4 = (γ-d) 동일 framing 답습
- 본 53 brief §2.4.4 = **"(γ-d) = 사실상 (γ-a) 와 동등 (시점 차이 한정)"** 자기 발견
- 즉, **52 entry framing 自身 = (γ-a) 동등 cascade**

**framing 정정 자격 평가**:
- 본 53 brief 内 framing 정정 = 권위 한계 위반 risk (§0.3 #25 답습 = "framing 정정 = 별도 cycle 사용자 명시")
- 그러나 본 53 brief §2.4.4 자기 발견 = framing 정정 자격 명문
- 즉, **framing 정정 = 별도 cross-reference 정정 cycle 사용자 영역** (R-C-1 BLOCKING 답습)

**권고**:
- v1.1 시점 §1.2 (γ) 4 대안 정의에 "(γ-d) = 52 entry framing 답습, §2.4.4 자기 발견 (γ-a) 동등 시점 차이 한정" 명문
- 또는 별도 cross-reference 정정 cycle (52 entry framing 자체 정정) 사용자 명시 영역 carry-over

### §5.2 본 cycle scope framing 자체 ("시점 결정" vs "evidence 결정")

**Agent C 발견** ((γ-g) 답습):
- 본 cycle 발효 효과 = "4 대안 中 채택 결정 발효" (§4.2)
- 그러나 4 대안 모두 *시점 결정* 영역 한정 (Layer 1+2 + Layer 4 동시 또는 순서 결정)
- evidence 결정 = MVP-2 PASS 발효 cycle 영역 (별도)
- 즉, **본 cycle = "시점 + 합의 cycle 구조 결정" 영역 한정 framing 가능**

**framing 변경 자격 평가**:
- 본 brief framing = "Layer 분리 영역 결정" (시점 + evidence 통합 framing)
- (γ-g) framing = "시점 결정 vs evidence 결정 분리"
- framing 변경 = 본 cycle scope 자체 변경 risk

**권고**:
- v1.1 시점 §0.1 또는 §0.4 명문 추가 — "본 cycle scope = '시점 + 합의 cycle 구조 결정' 한정, evidence 통합 = MVP-2 PASS 발효 cycle 영역" 답습
- 또는 NOTE 명문 한정 (framing 변경 = 별도 cycle 사용자 명시)

---

## §6 자기 편향 자기진단

### §6.1 Agent C 자체 잠재 편향 매트릭스

| # | 잠재 편향 | 본 응답 처리 |
|---|---------|----------|
| **AC-1** | Agent C = Claude Opus 4.7 = 본 brief 작성자 + Reviewer 동일 vendor + 동일 LLM (3-layer cascade) | NT-C-2 명문 + cross-vendor 외부 LLM 1+ (codex) 의무 답습 (사용자 영역 결정) |
| **AC-2** | Agent C "대안 탐색가" 역할 = 대안 추가 권고 편향 risk (추가 대안 의무 답습) | R-C-2 (γ-e/f/g) 추가 대안 = 본 cycle scope 평가 자격 명문 (자동 추가 0 = 사용자 결정 영역) + §4 추가 대안 평가 = 별도 cycle 영역 답습 |
| **AC-3** | Agent A (구현 분석가) / Agent B (안전성) 응답 *참조 0건* = 편향 차단 의무 답습 | 본 응답 전체 = 53 brief + 52 brief + 52 Reviewer 합의 + ADR-012 §2.3+§2.8 + provider-agnostic-memory-skill-design §4.4 + roadmap.md §4+§5.3+§6 직접 read 한정 (Agent A/B 응답 0) |
| **AC-4** | (γ-c) 권고 cascade risk (52 brief §2.2.4 답습 권고 답습 cascade) | N-C-1 = "(γ-c) 1순위 vs (γ-a) 2순위 trade-off 사용자 영역 결정" 명문 (Agent C 권고 ≠ 결정) |
| **AC-5** | R-S1 cross-reference 정정 cycle 자동 진입 risk (RT-γ-6 답습) | N-C-4 = "R-S1 정정 시점 = 본 (γ) cycle 결정 후 진행 권장 (cascade risk 회피)" 명문 + 자동 진입 0건 답습 |
| **AC-6** | (γ-d) 모순 risk 발견이 본 cycle 결정 무단 침입 risk | R-C-1 BLOCKING = "(γ-d) 가상 framing 한정, 실 대안 ≠" 명문 + 풀 3+1 합의 대상 framing 정정 = 사용자 영역 명시 |
| **AC-7** | "큰 영역" vs "작은 영역" framing 자체 결정 무단 침입 risk | R-C-3 BLOCKING = "큰 영역 framing 자체 정정 자격 = 사용자 영역" 명문 + 합의 형태 권고 격하 가능성 명시 |
| **AC-8** | 본 응답 작성 시점 (2026-05-28) state 한정 — 본 cycle 後 변경 시 evidence 변질 risk | 본 응답 = 53 brief v1 (482줄) + 52 brief v1.1 (603줄) 시점 직접 read 한정. cross-reference 검증 = filesystem state 답습 (변경 0) |

### §6.2 본 응답 자격 정직성

- 본 응답 = Agent C 단독 평가 (Agent A / Agent B / codex 응답 *참조 0건*) — 병렬 독립 평가 답습 충실
- 본 응답 = 53 brief v1 + 52 brief v1.1 + 52 Reviewer 합의 + ADR-012 §2.3 + §2.8 + provider-agnostic-memory-skill-design §4.4 + roadmap.md §4 + §5.3 + §6 직접 read 한정 (cascade source 0)
- 본 응답 판정 = REVISE (BLOCKING 3 + 권고 5 + NOTE 2) — REJECT 영역 ≠ (본 brief v1 작성 자격 충실)
- 본 응답 자격 = Reviewer 통합 합의 진입 자격 (Reviewer 영역 = 4 source cross-validation 매트릭스 + Consensus / Unique / Gap 분류 + 통합 BLOCKING + 권고 + NOTE 매트릭스)

### §6.3 후속 cycle 진입 자격 명문

- 본 Agent C 응답 = 53 entry Reviewer 통합 합의 진입 1 source 자격
- Reviewer 통합 합의 시점 = Agent A + Agent B + Agent C + codex (사용자 영역 결정 시) 4 source cross-validation
- Reviewer 통합 합의 발효 후 brief v1.1 1pass 흡수 = 52 entry 답습 동형 패턴 (ceremony-inflation 차단)
- 본 Agent C 응답 자체 = 본 cycle 진입 자격 ≠ (Agent C ≠ Reviewer)

---

## §7 본 Agent C 응답 끝

**판정 (총평 답습)**: **REVISE** (BLOCKING 3 + 권고 5 + NOTE 2)

**Reviewer 통합 합의 시점 의무 영역**:
1. Agent A (구현 분석가) 응답 + Agent B (안전성 검증가) 응답 + 본 Agent C (대안 탐색가) 응답 cross-validation
2. (사용자 영역 결정 시) 외부 LLM 1+ (codex via tmux + 추가 cross-vendor Gemini 가능) 응답 cross-validation
3. 4 source 분류 (Consensus / Unique / Gap / Divergence)
4. 통합 BLOCKING / 권고 / NOTE 매트릭스
5. 본 cycle 합의 판정 (REVISE → v1.1 1pass 흡수 → APPROVE WITH CONDITIONS 격상 또는 REJECT)

**Agent C 응답 끝.**
