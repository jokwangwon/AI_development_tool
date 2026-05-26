# 3+1 합의 보고서 — Jarvis MVP-1 설계 brief v1 (로컬 사장 + 판단 지점)

**작성일**: 2026-05-22 (세션 3)
**대상**: `docs/phase0/jarvis-mvp1-local-boss-design-brief.md` (DRAFT v1)
**프로토콜**: **풀 3+1** (CLAUDE.md §3 — MVP-1 = 아키텍처 + 보안 동시 변경)
**구성**: Agent A(구현 분석가) · Agent B(품질/안전성 검증가) · Agent C(대안 탐색가) 병렬 독립 → Reviewer 교차 비교
**최종 판정**: **APPROVE w/ COND — brief v2 수정 반영 후 트랙 A 구현 진입 가능 (트랙 B = V-1 통과 후)**

---

## 0. 3개 판정 요약

| Agent | 판정 | 한 줄 |
|-------|------|------|
| **A (구현)** | APPROVE w/ COND | 기존 `Worker`/`Orchestrator` 패턴에 깔끔히 통합. union flag 강제는 데이터 흐름상 구조적 보장. roofline 상 tok/s 여유. Ollama sm_121만 V-1 검증 필요 |
| **B (안전)** | APPROVE w/ COND | 안전 골격 견고. 단 "green washing 구조적 차단" *과대 진술*(의미적 우회 못 막음) + advisory 실패 거동 *미정의* 정정 필요 |
| **C (대안)** | APPROVE w/ COND | 핵심 선택 2026 현황 검증됨. 단 M3 런타임 우선순위 현실과 어긋남(llama.cpp 격상·vLLM 강등) + advisory 패턴 단순화 대안 존재 |

**3개 모두 APPROVE w/ COND, BLOCKING 0.** 방향(advisory-first 판단 지점·로컬 사장·OpenAI-호환 추상·MoE)에 합의. 조건 = 아래 brief 수정.

---

## 1. 교차 비교 (4분류)

### ① 일치 (Consensus — 3개 동의)
- **APPROVE w/ COND, BLOCKING 0** — 구현 진입 가능(조건부).
- **풀 3+1 적정** (B·C 명시, A 암묵) — 단축 Reviewer-only 부적합. CLAUDE.md §3 "보안 변경=3+1 필수" 정합.
- **~15 tok/s threshold 는 MoE 로 여유 충족** — A roofline(A3B Q4 ~90–120 실효) + C 실측(llama.cpp Qwen3-30B-A3B ~31). "273GB/s 병목→MoE 필수"(brief §2/Q-1) 정량 검증됨.
- **비례성 적합** — advisory 1개·httpx 직접·localhost 한정 = 과설계 없음.
- **Provider Liquidity(C-2) 정합** — OpenAI-호환 endpoint + config 주입 + httpx(SDK import 회피, `worker.py` 동형).

### ② 부분 일치 (Partial — 2개 동의)
- **2-트랙 분할** (A: `boss=None` 하위호환으로 추상화 선행 가능 시사 / C: 명시적 2-트랙 권고) — 추상화+advisory는 V-1 무관 TDD 선행 가능.
- **advisory 데이터 모델 제약** (A: `ApprovalRequest.advice` 필드 + union 식 / B: `BossAdvice` 텍스트 전용 frozen + 테스트 고정) — 같은 방향(실행권 0을 데이터 구조로 강제).
- **결정적 flag/raw diff 사람 직접 확인** (B: output_preview 비대칭 → flag 분리표시 / 암묵적으로 A의 union "감산 불가"와 연결).

### ③ 불일치 (Divergence) — advisory 통합 패턴 (층위 차이)
세 의견이 *충돌*이 아니라 **층위가 다름**:
- **A**: `extra_flags` 합집합(union)은 코드로 자명하게 안전 — 게이트가 flag로 차단 안 하므로 advisory가 flag 줄여도 사람 게이트는 어차피 열림. → 기계적으로 안전 ✅
- **B**: 그 union이 막는 범위를 *과대 진술* 말 것 — `summary` 자유 텍스트가 flag 안 건드리고도 사람을 오도해 승인 유도(*의미적* green washing). "구조적 차단" 단정 자체가 거짓 안전감.
- **C**: 아예 LLM 출력을 flag로 *승격하지 말고* 순수 자연어 요약으로만 → union 불변식 검증 자체가 불필요(더 단순+안전).

**Reviewer 해소**: **union(additive) 유지 + B 정직성 적용** 채택. 근거:
- A가 union의 구조적 안전 입증 + LLM이 정규식 미포착 위험을 caution으로 *추가*만 하는 가치(추론적 보조) 실재 → union 유지가 기능 손실 없음.
- C의 "순수 요약(flag 미승격)"은 *summary 오도* 문제를 해결 못 함(요약 자체가 오도 가능) → union 폐기가 단독 우위 아님.
- **단 B의 정정 필수**: "green washing 구조적 차단" → "*기계적* flag 감산만 차단, *의미적* 우회는 못 막음. 방어=결정적 flag 분리표시 + raw diff 사람 직접 확인 + ReviewGuard 권위." (R1)
- C의 순수-요약안 = 구현자 선택 가능 fallback로 brief에 기록(둘 다 안전, union이 기능 우위).

### ④ 누락 (Gap — 1개만 언급, 중요도 평가 후 채택)
- **A**: 워커 실패 시 advise 미호출(injection 표면·비용 회피) / prefill(긴 diff) 지연 별도·입력 truncation / `boss=None` 하위호환 → **채택**(R7·R8·R5).
- **B**: advisory 실패 fail-closed 명시경고 / `output_preview[:200]` vs Boss 입력 비대칭 / Ollama pull·텔레메트리 egress 한정 → **채택**(R3·R10·R11).
- **C**: vLLM 제외→MVP-2 강등 / llama.cpp 격상 / `confidence` 제거 / advisory 비전임팩트 트레이드오프 / LiteLLM=MVP-2 진화경로 → **채택**(R4·R6·R12·R13).

---

## 2. 합의 수정 (brief v2 반영 — COND 조건)

| # | 수정 | 출처 | 등급 |
|---|------|------|------|
| **R1** | §4·§5 "green washing 구조적 차단" → "*기계적* flag 감산만 차단; *의미적* 우회(summary 오도)는 못 막음. 방어=결정적 flag 분리표시 + raw diff 사람 직접 확인 + ReviewGuard 권위" 정정 | B | 🔴 정직성 |
| **R2** | `BossAdvice` = 텍스트 전용 frozen dataclass 명문화(콜백·경로·명령 필드 금지; 게이트 통과·argv·workdir에 영향 0 — 테스트로 고정) | B·A | 🔴 안전 |
| **R3** | advisory 실패(timeout/다운/비정상) = advisory 누락 처리, 결정적 flag·게이트는 진행(비차단), **단 사람에게 "Boss advisory 실패" 명시 경고**(부재를 안전으로 오해 금지). 게이트는 항상 fail-closed, advisory는 부재 시 명시 | B | 🔴 안전 |
| **R4** | M3 런타임 재조정 — **llama.cpp > Ollama**(V-1 실측 2026-05-25: llama.cpp Qwen3-30B-A3B classical ~49.6 / Qwen3-Next-80B SSM ~32.3 t/s, Ollama 동일 모델 ~14.7~15.3 = ~3.24~3.38× llama.cpp 빠름, prefill prompt ~24× outlier, **Ollama MoE 공개 confirmed**; R4 원본 "~31 t/s" = (g) Qwen3-Next-80B SSM hybrid variant ~4% 격차 정합). V-1 측정 충족, 결정(M3) = (k) 별도 cycle. **vLLM "제외(#36821)" → "MVP-1 비채택, MVP-2 재검토"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합 |
| **R5** | §6에 tok/s 기대치 첨부(roofline A3B Q4 ~90–120 실효 / llama.cpp 실측 ~31 / ~15 2배 여유 = de-risk 신호). prefill(긴 diff) 지연 별도 → **advisory 입력 길이 상한/요약**을 V1-3 측정 항목에 추가 | A·C | 권고 |
| **R6** | `BossAdvice.confidence` 삭제(또는 "표시만, 게이트 결정 미반영") — LLM 자기보고 confidence = injection 표적의 거짓 안전감 | C | 권고 |
| **R7** | `Orchestrator.__init__(boss: BossLLM | None = None)` 주입 — `None`이면 advisory 없이 MVP-0 동작 보존(하위 호환). `ApprovalRequest.advice: BossAdvice | None = None` 필드 추가(frozen, default → 무파손) | A | 권고 |
| **R8** | 워커 실패(`result.is_error`) 시 advise 미호출 명문화(실패 출력에 LLM 비용/지연 + injection 표면 회피). 현 early-return(`orchestrator.py:83`) 위치와 정합 | A | 권고 |
| **R9** | MVP-1 **2-트랙 명시**(MVP-0 패턴 재사용): 트랙 A(BossLLM 추상+advisory, StubBoss TDD, V-1 무관 선행) / 트랙 B(로컬 런타임 연결, V-1 통과 후) | C·A | 권고 |
| **R10** | §4에 "사람은 결정적 flag + raw diff 를 직접 확인, Boss summary 에만 의존 금지" 명문(현 `output_preview[:200]` 절단이 Boss 해석 종속 위험) | B | 권고 |
| **R11** | §5 egress "*추론 시점* egress 0, 단 설치/모델 pull/텔레메트리는 별개" 한정. Ollama localhost 바인딩 = V-1 실측 확인 대상으로 명시 | B | 권고 |
| **R12** | §1에 advisory 트레이드오프 명시(안전 위험 최저 ↔ 비전 시연 임팩트 최저) — 첫 지점으로 여전히 옳으나 정직한 기록 | C | 권고 |
| **R13** | §3에 "다중 provider 라우팅 필요 시 LiteLLM 게이트웨이 = 진화 경로(MVP-2); 지금 도입은 과설계" 한 줄 | C | 메모 |

---

## 3. 최종 판정 — APPROVE w/ COND

- **3개 독립 분석 모두 APPROVE w/ COND, BLOCKING 0.** 설계 방향(advisory-first·로컬 사장·OpenAI-호환·MoE)이 (a) 기존 MVP-0 인터페이스에 구조적으로 정합(A) (b) 안전 골격 견고·답습 정합(B) (c) 2026 현황·비례성 검증(C).
- **COND = R1~R13 brief v2 반영.** 실질 변경 = R4(런타임 재조정)·R1·R3(안전 정직성/실패 거동) 3건이 핵심, 나머지는 명문화.
- **잔여 불확실성 1개**: Ollama/llama.cpp **sm_121 out-of-box 동작 + MoE tok/s** = V-1 PoC 블로커. brief가 이미 V-1로 정확히 격리, llama.cpp 대안으로 헷지.

### 진입 경로 (합의 권고)
1. **brief v2** — R1~R13 반영.
2. **트랙 A 구현** (BossLLM 추상 + advisory + StubBoss TDD) — **V-1 무관, 즉시 진입 가능**(R9).
3. **V-1 PoC** — Ollama·llama.cpp 둘 다 MoE tok/s 실측(R4), threshold 확정(M4).
4. **트랙 B 통합** — V-1 통과 후 로컬 런타임 연결.

**범위 한정**: 본 합의 = "MVP-1 설계 brief 승인 + 구현 진입 가능 여부". 모델 *결정 고정*(M2)·런타임 *결정 고정*(M3)·tok/s threshold *고정*(M4)은 V-1 실측 후 별도 단계. 코드/설치 0건(본 합의는 분석만).

---

**출처**: brief v1 / Agent A·B·C 독립 보고(병렬, 상호 미참조) / MVP-0 코드(`src/jarvis/*`) / brief v4 / V-2 findings / 웹 조사(C: Ollama·llama.cpp DGX Spark 실측·Qwen3.6-35B-A3B·vLLM #36821·LiteLLM). 답습: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention` / `feedback_staged_consensus_workflow`.
