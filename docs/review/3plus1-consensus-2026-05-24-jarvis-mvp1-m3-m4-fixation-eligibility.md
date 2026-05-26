# 3+1 합의 보고서 — 자비스 MVP-1 V-1 PoC Phase 2 완료 후 M3·M4 결정 *고정* 자격 평가

> **본 합의 = 자격 평가 한정** (staged consensus 답습). 결정 *고정* 0건, commit·push 0건 (사용자 명시 별도).

---

**작성일**: 2026-05-24
**합의 단위**: V-1 PoC Phase 1 cycle (`9c6b578`) + Phase 2 cycle (`c66756b`) 완료 후 M3·M4 결정 *고정* 자격 평가
**선행 답습**: M3·M4 결정 합의 (`9ddec1b` 풀 3+1 APPROVE w/ COND BLOCKING 5) + Phase 1 결과 (`v1-poc-raw/2026-05-24-phase1-summary.json`) + Phase 2 brief v2 EXECUTED (`docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md` §9)
**참여 Agent**: A (구현 분석가, 기술적 충분성) / B (품질·안전성 검증가, 정직성 한계) / C (대안 탐색가, 트레이드오프) / Reviewer (Phase 3-4 교차 비교 + 합의)
**답습 권위 한계**: 본 합의 = 결정 *권고* 한정. 결정 *고정* / brief 갱신 / Phase 3 진입 / commit·push = 사용자 명시 별도

---

## 0. 검토 대상

**검토 대상 결정**: M3·M4 결정 (M3 = 모델 선정, M4 = 런타임 default tok/s threshold). 선행 합의 `9ddec1b` = 풀 3+1 APPROVE with COND, BLOCKING 5건 (R-1 원인 분리 / R-2 권고 자격 검증 framing / R-3 옵션 E cross-ref / R-4 M4-B 영구 거부 / R-5 Phase 1+2+3 cycle 명문) 명시.

**V-1 PoC F1 가설 5종 갱신 상태 (Phase 2 §9.8 후)**:
- (i) 활성 ~3B 가정 초과 → **부정** (HF 모델 카드 verbatim "3B activated" + 3중 cross-check)
- (ii) SSM state 메모리 압박 → **명칭 정정** (architecture = Gated DeltaNet linear attention, NOT classical SSM/Mamba)
- (iii) Ollama 0.20.4 hybrid 효율성 (vs llama.cpp) → **미해소**
- (iv) Qwen3-Next router/gating overhead → **미해소**
- (v) GB10/Ollama effective BW spec 1/3 (~85 GB/s) → **강한 evidence** (qwen2.5 dense 역산)

**5 핵심 질문 (3 Agent 공통)**:
- Q1: M3·M4 결정 *고정* 자격
- Q2: Phase 3 (C-e llama.cpp) 필요성
- Q3: F1 본질 재평가 (결론 도출 범위)
- Q4: R-10 일반화 (Agent A manifest 산정 +43% 과대)
- Q5: R-15 gap-pull 8종 trigger 자격

---

## 1. 교차 비교 매트릭스 (5 Q × 4 분류)

### Q1: M3·M4 결정 *고정* 자격

| Agent | 결론 | 핵심 근거 | 신뢰도 |
|-------|------|----------|--------|
| A | 미충족 (HIGH) | R-5 명시 Phase 3 미진입 + R-1 원인 분리 미완 + R-3 옵션 E 미진입 | 명시 |
| B | 단독 미충족 + critical 1건 (SSM→Gated DeltaNet 명명) → Phase 3 해소 또는 **연기 단계 명문 고정** | 정직성 6종 中 1 critical, framing 답습 의무 | 명시 |
| C | **(e) 계층화 고정** (L1/L2 즉시 / L3/L4 Phase 3 후) — 신규 대안 | rollback trigger 명문, 결정 *고정* vs *권고* 비례성 | 0.65 |

**분류**: ② 부분 일치. 다음 단계 모양 = ② → ① 수렴 (Phase 3 진입 전 결정 *고정* 자격 미충족 답습).

### Q2: Phase 3 (C-e llama.cpp) 필요성

| Agent | 결론 | 핵심 근거 |
|-------|------|----------|
| A | non-fatal but **필수** (MEDIUM-HIGH) | (iii)(iv) 미해소, BW 단정 자격 잔존 |
| B | skip risk = medium, 결정 고정 *이후* 후속 작업 품질 직접 | (c) gap-pull framework + (d) Provider Liquidity 실측 |
| C | **(e) 단계적 hybrid** 신규 (prebuilt binary ~15+5분 + 분기점) | 정공법 거부 아님, 자격 평가 cycle 분리, 신뢰도 0.70 |

**분류**: ① 일치 (필요성) + ④ 누락 (방법론 — C 만 hybrid 제안).

### Q3: F1 본질 재평가 (결론 도출 범위)

| Agent | 결론 | 핵심 근거 |
|-------|------|----------|
| A | 부분 자격 (HIGH) — "BW 영역 공통" + "(i) 부정" 충분 / "본질 = BW" 단정 0 | dense vs MoE 3.96× 추가 격차 (Ollama 7.83 vs 외부 llama.cpp ~31) |
| B | Link 3 (BW 본질) = weakest — Link 1 strong / Link 2 medium-strong / Link 3 weakest | MoE active read BW 가정 + (iii)(iv) 미해소 |
| C | **(b) 복합 결론 framing + (c) 새 가설 carry-over** — BW + router/SSM-like recomputation 복합 + GB10 sm_120/121 미지원 가설 | Qwen3-Next 특수 구조 (Gated DeltaNet + MoE hybrid) |

**분류**: ① 일치 (BW 단정 자격 0 + (i) 부정 자격 충분) + ④ 누락 (C 의 새 가설 #6).

### Q4: R-10 일반화 (Agent A manifest +43% 과대)

| Agent | 결론 | 핵심 근거 |
|-------|------|----------|
| A | 정의 불일치 가설 가장 가능성 (MEDIUM), systemic bias 가능성, roofline ~30% 영향 | HF "3B activated" 산정 verbatim 0 |
| B | gap-pull framework = critical / M3 결정 자체 = non-critical, 거버넌스 강화 권고 (산정 명시 + 격차 추적 + ±20% borderline 보수성) | R-10 = framework 결함, 단일 결정 통과 시도 무관 |
| C | **(e) cross-check SOP 명문화 + (c) verbatim 우선 + (a) config fallback + (b) over-estimate 보정** — 8종 SOP, 격차 > 30% → NOTE 후보, 신뢰도 0.80 | systemic bias 보정 가드 (활성 ≤ 10B + Q4 ≤ 20GB 보강) |

**분류**: ② 부분 일치. C 가 가장 operational (실행 가능 SOP 제시).

### Q5: R-15 gap-pull 8종 trigger 자격

| Agent | 결론 | 핵심 근거 |
|-------|------|----------|
| A | Phase 3 후 trigger (β) 기술적 효율 우선 (MEDIUM) | (iii)(iv) 미해소 상태 gap-pull = noise 추가 |
| B | HF egress cycle 안전, borderline 5종 verbatim 사전 확보 + 사용자 재확인 의무 | 비례 보안 답습, 자동 재개 0건 |
| C | **(c) 일부 후보 우선 pull (P1/P2/P3 SOP)** — P1 (Qwen3.5-A3B-Instruct) Phase 2 직후 자격, P2 Phase 3 후, P3 carry-over | 가족 일관성, Provider Liquidity 답습, 신뢰도 0.65 |

**분류**: ③ 불일치 (3 분기). 하한선 일치: gap-pull 자동 trigger 0건.

---

## 2. 일치 항목 (Consensus)

### C-1. M3·M4 단독 *결정 고정* 자격 미충족 (Q1, Q2)

3 Agent 모두 동의:
- Phase 1+2 측정만으로 M3 (모델 선정) / M4 (런타임 default) 결정 *고정* 자격 미충족
- Phase 3 (C-e llama.cpp 측정) 또는 **명문 *연기 단계 고정*** 필수
- M3-C (모델 후보 권고) + M3-D (advisory) **권고 형태** = Phase 1+2 후 자격 충분

**채택**: 그대로 채택. **결정 *고정* 자격 미충족 = BLOCKING 1**.

### C-2. F1 "본질 = BW" 단정 자격 0 (Q3)

3 Agent 모두 동의:
- (i) "활성 ~3B 초과" 가설 *부정* = 자격 충분
- (v) BW spec 1/3 → roofline 산정 일치 = **강화** evidence (단정 아님)
- (iii) Ollama vs llama.cpp + (iv) router overhead 미해소 → "본질 = BW" 단정 = R-6 위반 risk

**채택**: 그대로 채택. brief §9.8 "(v) 강화" 표현 = raw 한정 적절. "BW 본질 확정" / "uniquely identified" / "PASS" framing = R-6 위반 금지.

### C-3. (ii) SSM → Gated DeltaNet 명칭 정정 자격 충분 (Q1, Q3)

A/B/C 모두 자격 충분 인정 (B = critical 1건으로 brief framing 답습 의무 명시).

**채택**: 그대로 채택. M3 결정 *문구* 에서 "SSM" 표현 0건, "Gated DeltaNet" verbatim 의무.

### C-4. R-10 일반화 필요성 + Agent A 산정 결함 (Q4)

3 Agent 모두 동의 — manifest +43% 과대 = framework 신뢰도 영향 / R-15 gap-pull framework 재고 trigger.

**채택**: 그대로 채택. **R-10 일반화 = BLOCKING 2**.

### C-5. 비례 보안 + Provider Liquidity 답습 (Q5)

3 Agent 모두 동의:
- gap-pull 자동 trigger 0건 (자동 재개 0 — 비례 보안 답습)
- Provider Liquidity 헌법 5조 = 하드 요구, gap-pull 폐기 거부

**채택**: 그대로 채택.

---

## 3. 부분 일치 항목 (Partial) + 결정

### P-1. Q1 "결정 *고정* 단계화 가능성" (A/B vs C)

| 입장 | Agent | 근거 |
|------|-------|------|
| 단일 결정 *고정* 미충족 → Phase 3 또는 *연기* | A, B | R-5 + R-1 + R-3 명시 의무, framing 답습 |
| **계층화 고정** (L1=사실, L2=가설 상태, L3=런타임 default Phase 3 후, L4=threshold Phase 3+advisory 후) | C | rollback trigger 명문, 비례성 |

**Reviewer 결정**: **C 의 계층화 고정 *부분* 채택**.
- L1 (i) 부정 + (ii) 명칭 정정 + R-10 격차 = **이미 brief §9.6+§9.8 명문**, 즉시 고정 = brief 명문 답습 한정 (별도 결정 *고정* 0건)
- L2 가설 갱신 *상태* (v) 강화 + (iii)(iv) 미해소 = **상태 기록 한정**, "본질 = BW" 단정 금지 (C-2 답습)
- L3 런타임 default = **Phase 3 후 *재* 합의** (A/B 일치점, 단독 *고정* 미충족)
- L4 threshold = Phase 3 + advisory 후 (B 거버넌스 강화 권고 답습)

**모양**: Reviewer = **계층화 + Phase 3 의무**의 hybrid 권고 (C 신규 + A/B 답습). 본 합의 자체로는 L1/L2 도 *고정* 0건 — 사용자 명시 승인 별도 cycle.

### P-2. Q4 R-10 강도 (A=systemic bias / B=critical for gap-pull only / C=SOP+가드)

**Reviewer 결정**: **C 의 SOP 명문화 + B 의 거버넌스 강화 종합 채택**.
- A = 가능성 식별 (정의 불일치 가장 가능) → 가설 carry-over
- B = framework 결함 격리 (단일 결정 자체는 non-critical) → 거버넌스 강화 의무
- C = operational SOP (산정 명시 + 격차 추적 + ±20% borderline 보수성 + 활성 ≤ 10B + Q4 ≤ 20GB) → **즉시 실행 가능**

**3개 종합** = R-10 일반화 SOP 형태 권고.

---

## 4. 불일치 항목 (Divergence) + 결정

### D-1. Q5 R-15 gap-pull trigger 자격 (3 분기)

| 입장 | Agent | 근거 강도 |
|------|-------|---------|
| (α) Phase 3 후 일괄 trigger | A | 기술적 효율 우선 (noise 회피) |
| (β) borderline 5종 verbatim 사전 확보 + 사용자 재확인 | B | 비례 보안 + 정직성 |
| (γ) P1/P2/P3 단계화 (P1 Qwen3.5-A3B 즉시) | C | Provider Liquidity 답습, 가족 일관성, 신뢰도 0.65 |

**Reviewer 결정**: **(β) + (γ) hybrid 채택**.
- A (α) = technically clean but Provider Liquidity 답습 강도 부족 (Phase 3 까지 모든 후보 carry-over → 다음 결정 cycle 지연 risk)
- B (β) = 정직성 + 비례 보안 우선 but operational SOP 부족 (verbatim 확보 의무만 명시, 어느 후보부터 인지 불명)
- C (γ) = operational + Provider Liquidity but P1 trigger 자격 강도 (신뢰도 0.65) — **R-10 일반화 SOP 적용 후** 자격 평가 필요

**최선**: B 의 verbatim 확보 의무 (사전) + C 의 P1/P2/P3 단계화 (실행) **결합**. P1 (Qwen3.5-A3B) trigger 자격 = **R-10 SOP (Q4 합의) 통과 후** 별도 cycle. 본 합의 자체로는 gap-pull trigger 0건.

---

## 5. 누락 항목 (Gap) + 채택/제외 평가

### G-1. C 의 (e) 단계적 hybrid Phase 3 (Q2)

C 만 제안 — prebuilt aarch64 binary SHA 검증 (~15분) + 단일 decode 측정 (~5분) + 분기점 (격차 < 20% / > 50%).

**평가**: **채택 권고** (중요도 = MEDIUM-HIGH). 근거:
- 정공법 (full build) 거부 아님, **자격 평가 cycle 분리** 답습
- 시간 효율 (~20분) — Phase 3 진입 부담 ↓ (staged consensus 답습 친화)
- 분기점 명문 = SDD 답습 친화

단, A/B 미언급 = 방법론 trade-off 미평가. **사용자 명시 승인 별도** — Phase 3 진입 시 정공법 vs hybrid 본인 결정.

### G-2. C 의 새 가설 #6 (sm_120/121 미지원) (Q3)

C 만 식별 — Qwen3-Next 특수 구조 (Gated DeltaNet + MoE hybrid) GB10 sm_120/121 미지원 가능성.

**평가**: **채택 (carry-over)** (중요도 = MEDIUM). 근거:
- 가설 (iii)(iv) 미해소 상태에서 **누락된 가설 식별 자체 = 가치**
- Phase 3 (llama.cpp 측정) 시 자연 검증 (llama.cpp 도 동일 격차 시 → sm_120/121 미지원 가설 강화)
- A 의 "systemic bias 가능성" + C 의 #6 = **F1 본질 재평가의 미해소 영역 확장**

**조치**: 가설 carry-over 명문 (brief §9.8 갱신 권고 — 단, 본 합의 자체 0건, 사용자 명시 별도).

### G-3. B 의 거버넌스 강화 3종 (Q4)

B 만 명시 — (i) 산정 방식 명시 의무, (ii) 격차 추적 의무, (iii) ±20% borderline 보수성 의무.

**평가**: **채택** (중요도 = HIGH, 이미 P-2 결정에 통합).

### G-4. C 의 rollback trigger 명문 (Q1, ADR-011 §2.1 답습)

C 만 명시 — 계층화 고정에 rollback trigger 명문 의무.

**평가**: **채택** (중요도 = HIGH). 근거:
- ADR-011 §2.1 5조건 답습 = CLAUDE.md 명시 의무
- 계층화 고정 *어떤 형태로든* 진입 시 rollback trigger 0건 = R-6 framing 위반

---

## 6. 합의 결론

### M3·M4 결정 *고정* 자격: **단독 미충족** (Phase 1+2 완료 후)

- **결정 *고정* 자격 평가** = 본 합의의 목적, **자격 평가 한정** (staged consensus 답습)
- M3 (모델 선정) / M4 (런타임 default) = **Phase 3 진입 또는 *연기 단계 명문 고정* 의무**
- M3-C (모델 후보 권고) + M3-D (advisory) **권고 형태** = Phase 1+2 후 자격 충분

### 권고 다음 단계 (3 분기, 사용자 명시 승인)

| Option | 내용 | 답습 강도 |
|--------|------|---------|
| **(A) Phase 3 진입 (정공법)** | C-e llama.cpp full build → (iii)(iv) 해소 → 결정 *고정* | A/B 일치점, 시간 비용 ↑ |
| **(B) Phase 3 진입 (C hybrid)** | prebuilt aarch64 binary + 단일 decode + 분기점 | C 신규 (G-1), 시간 ~20분 |
| **(C) *연기 단계 명문 고정*** | Phase 3 미진입 + (iii)(iv) 미해소 명문 + M3-C+M3-D 권고 한정 채택 + R-15 carry-over | B 권고 강도 ↑, Provider Liquidity 후속 cycle |

### BLOCKING 조건 (3 Agent 종합)

1. **결정 *고정* 자격 미충족** (Phase 1+2 단독) — **BLOCKING 1**
2. **R-10 일반화 SOP 미정** — Agent A 산정 +43% systemic bias 가능성, framework 신뢰도 영향 — **BLOCKING 2**
3. **F1 "본질 = BW" 단정 금지** — (iii)(iv) 미해소 상태 R-6 framing 위반 — **BLOCKING 3**
4. **(ii) "SSM" 명명 0건 의무** — M3 결정 문구 "Gated DeltaNet" verbatim — **BLOCKING 4**
5. **rollback trigger 명문 의무** — 계층화 *어떤 형태로든* 고정 시 ADR-011 §2.1 답습 — **BLOCKING 5**

### 권고 조건 (non-blocking)

- R-1: A-진단 + C-c cache miss 분리 (Phase 1 완료, 추가 분리 0건)
- R-3 옵션 E (Ollama origin 위생): 결정 *고정* 시 명문 / 결정 *연기* 시 carry-over
- R-15 gap-pull SOP: P1/P2/P3 단계화 (B verbatim + C operational hybrid)
- F1 새 가설 #6 (sm_120/121 미지원): brief §9.8 carry-over
- C-2 BW 단정 자격 0 = framing 답습 (raw 한정)

### 답습 (Reviewer 의무)

| 답습 | 적용 | 답습 결과 |
|------|------|---------|
| R-6 (PASS/FAIL framing 금지) | C-2, BLOCKING 3 | "BW 본질 확정" / "uniquely identified" / "PASS" 금지, raw 한정 |
| 비례 보안 (`feedback_proportionate_security_personal_tool`) | G-1, D-1, C-5 | 자동 재개 0건, gap-pull 자동 trigger 0건, 사용자 명시 의무 |
| staged consensus (`feedback_staged_consensus_workflow`) | 본 합의 자체 | 결정 *고정* 0건, commit·push 0건, 사용자 명시 승인 의무 |
| Provider Liquidity (헌법 5조) | C-5, D-1 (γ) | gap-pull 폐기 거부, P1/P2/P3 carry-over |
| 정직성 (약한 link 명문화) | C-2, BLOCKING 3, B 6종 | "Link 3 (BW 본질) = weakest" 명문, framing 의무 |
| ADR-011 §2.1 5조건 | G-4, BLOCKING 5 | 계층화 고정 시 rollback trigger 명문 |
| SDD (코드보다 문서 우선) | 본 합의 ≠ 코드 변경 | 0건 코드 변경 |

---

## 7. 자체 0건 답습

본 합의 보고서 = **자격 평가 한정** (Phase 3-4 출력).

| 항목 | 상태 |
|------|------|
| 결정 *고정* | **0건** (Q1 = 미충족, 권고 다음 단계 3 분기 = 사용자 명시 승인 별도) |
| commit | **0건** (`git commit` 호출 0건, 사용자 명시 별도) |
| push | **0건** (`git push` 호출 0건, 사용자 명시 별도) |
| brief 문서 수정 | **0건** (`docs/phase0/jarvis-mvp1-v1-poc-phase2-entry-brief.md` 수정 0건) |
| `docs/sessions/*` 세션 로그 작성 | **0건** (사용자 명시 별도) |
| Phase 3 진입 (C-e llama.cpp 측정) | **0건** (자격 평가 한정) |
| R-15 gap-pull trigger (모델 pull) | **0건** (D-1 결정 = trigger 미충족, P1 자격은 R-10 SOP 통과 후) |
| 모델 / 런타임 / threshold default 변경 | **0건** (M3 L3/L4 = Phase 3 후 재 합의, M4 동일) |
| HF / 외부 LLM egress | **0건** (Agent 출력 evidence 인용 한정) |

본 합의 = **다음 cycle 진입 자격 평가**. 사용자 명시 승인 후 별도 cycle에서 결정 *고정* / brief 갱신 / Phase 3 진입 / commit·push 진행.

---

## 8. 답습 요약 (영구)

- **하는 것**: M3·M4 결정 *고정* 자격 평가 + BLOCKING 5건 식별 + 다음 단계 3 분기 권고
- **하지 않는 것**: 결정 *고정* / brief 갱신 / Phase 3 진입 실행 / gap-pull trigger / 모델·런타임·threshold 변경 / commit·push / 보안 거버넌스 자동 재개
- **출처**: M3·M4 결정 합의 `9ddec1b` + Phase 1 결과 `2026-05-24-phase1-summary.json` + Phase 2 brief v2 `c66756b` §9 + V-1 entry brief + ADR-011 §2.1 5조건 + 헌법 5조 (Provider Liquidity) + CLAUDE.md §3 (3+1 합의 프로토콜) + `feedback_proportionate_security_personal_tool` + `feedback_staged_consensus_workflow` + `feedback_provider_liquidity` + `project_jarvis_local_boss_direction`

---

**Reviewer 최종 권고**: M3·M4 결정 *고정* 자격 = **단독 미충족 (BLOCKING 5건)**. 다음 단계 = **(A/B/C) 3 분기 사용자 명시 승인 의무**. R-6 framing + 비례 보안 + Provider Liquidity + staged consensus 4중 답습 의무.
