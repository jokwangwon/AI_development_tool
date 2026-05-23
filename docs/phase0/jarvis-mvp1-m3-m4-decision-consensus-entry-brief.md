# Jarvis MVP-1 M3·M4 결정 합의 entry brief (DRAFT v1)

> **본 brief = V-1 PoC Stage 4 raw 입력으로 M3 (런타임) · M4 (tok/s threshold) 결정 합의 *진입 단계* 한정.** 본 brief 자체 = 결정 *고정* 0건. 합의 결과 = 결정 *권고*. 결정 *고정* 은 합의 보고서 + 사용자 명시 후 별도 단계.

**작성일**: 2026-05-23
**Status**: DRAFT v1 (entry brief, 합의 진입 자격 검토용)
**선행 답습**:
- entry brief v1.1 `jarvis-mvp1-v1-poc-entry-brief.md` §9.1 (M3 매트릭스 권고)·§9.2 (M4 raw 보고만)
- 합의 보고서 `3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md` (BLOCKING 6 + 권고 14)
- findings `jarvis-mvp1-v1-poc-findings.md` (DRAFT Stage 1+2+3+4)
- MVP-1 brief v2 `jarvis-mvp1-local-boss-design-brief.md` §6 + 합의 R1~R13 (R4 vLLM "MVP-2 재검토"·llama.cpp↔Ollama 동급·tok/s roofline·실측 등)
- ADR-011 §2.1 5조건 (a)~(e) 답습

**프로토콜**: **풀 3+1** (CLAUDE.md §3 — 아키텍처 큰 결정 + 의외 발견 = 풀 3+1 필수)

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. Stage 4 raw 핵심 종합 (§1)
2. ⭐ Stage 4 의 **의외 발견 3건** 명시 (§2)
3. M3 결정 후보 옵션 식별 + 트레이드오프 (§3)
4. M4 결정 후보 옵션 식별 + 정직성 한계 (§4)
5. 풀 3+1 분담 + 각 Agent 핵심 질문 (§5)
6. 답습 권위 한계 / 영구 금지 명시 (§6)

### 하지 않는 것 (영구 답습)

- ❌ M3 결정 *고정* (런타임 선택·트랙 B 구현 진입)
- ❌ M4 threshold *고정*
- ❌ 추가 측정 실행 (cache miss 영역·llama.cpp·gap-pull 등)
- ❌ Ollama 데몬 변경 / pull / 설치
- ❌ 트랙 B `OllamaBoss` 코드 작성
- ❌ 보안 거버넌스 자동 재개
- ❌ Provider Liquidity 약화 (헌법 5조 답습)

---

## 1. Stage 4 raw 종합

### 1.1 측정 환경 (정직성 prerequisite)

| 항목 | 값 |
|---|---|
| host | promaxgb10-f3c4 (Linux 6.17.0-1018-nvidia aarch64) |
| GPU | NVIDIA GB10 (driver 580.159.03), unified memory 273GB/s |
| CUDA | 13.0 |
| Ollama | 0.20.4 (PID 3375, **출처 미상**, sha256 `ce95c475...878b10` 3회 일치) |
| R-23 | 본 세션 only (orphan claude 3개 SIGKILL 후) |
| R-1 | 측정 *전*·*후* hash 동일 (silent 교체 미발생) |

### 1.2 raw 측정값 (R-6 답습, PASS/FAIL framing X)

| 모델 | scenario | mean tok/s | std (std/mean) | 비고 |
|---|---|---:|---:|---|
| qwen3-coder-next (MoE 79.7B+SSM Q4 48.2GB) | decode 5회 | **7.83** | 0.36 (4.6%) | run #1 outlier 2σ 경계 |
| qwen3-coder-next | prefill 2k cold (precheck) | 66.46 | — | KV cache empty |
| qwen3-coder-next | prefill 2k warm 5회 | 91.58 | 2.91 (3.2%) | 부분 cache (24초 prefill 잔존) |
| qwen3-coder-next | prefill 8k cold (precheck) | 57.79 | — | 135초 prefill |
| qwen3-coder-next | prefill 8k warm 5회 | 291.55 | 5.76 (2.0%) | 부분 cache |
| qwen2.5-coder:32b (dense Q4 18.5GB) | decode 5회 | **4.62** | 0.18 (4.0%) | run #5 outlier 경계 |
| qwen2.5-coder:32b | prefill 2k cold | 13.19 | — | 154초 prefill |
| qwen2.5-coder:32b | prefill 2k warm 5회 | **~8290** | 996 (12%) | 🔴 거의 완전 cache hit (~200ms) |
| qwen2.5-coder:32b | prefill 8k cold | **11.75** | — | 667초 (quadratic compute) |
| qwen2.5-coder:32b | prefill 8k warm 5회 | **~27465** | 1731 (6.3%) | 🔴 cache lookup only |

### 1.3 비교 (raw 비율, 해석은 합의 본문)

| 비교 | qwen3-coder-next | qwen2.5-coder | ratio |
|---|---:|---:|---|
| decode (memory-bound) | 7.83 | 4.62 | MoE/dense = **1.70×** |
| prefill cold 2k | 66.46 | 13.19 | MoE/dense = **5.04×** |
| prefill cold 8k | 57.79 | 11.75 | MoE/dense = **4.92×** |
| prefill warm cache hit 2k | 91.58 | 8290.93 | dense/MoE+SSM = **90.5×** |
| prefill warm cache hit 8k | 291.55 | 27465.21 | dense/MoE+SSM = **94.2×** |

---

## 2. ⭐ Stage 4 의외 발견 3건 (합의 핵심 입력)

### 2.1 F1 — decode roofline 7-9% 수준

- brief v2 §6 R5 roofline 가정: A3B Q4 ~90-120 tok/s
- 외부 실측 (합의 R4): llama.cpp Qwen3-Coder-30B-A3B ~31 tok/s
- 본 측정: qwen3-coder-next decode **7.83 tok/s** = roofline **~7-9%**, 외부 실측의 **~25%**
- 가설 (검증 별도, 본 brief 결론 X):
  - (i) 활성 파라미터가 ~3B 가정 *초과* (top-10/512 + SSM state 합쳐 ~10B 가능)
  - (ii) GB10 unified memory 273GB/s 가 SSM state + KV cache + expert weight 동시 압박
  - (iii) Ollama 0.20.4 의 hybrid SSM+MoE 구현 효율성 (llama.cpp vs Ollama 차이)
  - (iv) 측정 환경 특성 (단일 세션·warm-up 효과·prompt 토큰 분포 등)

### 2.2 F2 — prefill warm cache hit dense ≫ MoE+SSM (~90× 역전)

- prefill warm 5회: qwen2.5-coder ~8290-27465 tok/s (사실상 cache lookup, 200-300ms) vs qwen3-coder-next 91.6-291.5 tok/s (부분 cache, 24-27초 prefill 잔존)
- 가설 (검증 별도):
  - (i) **SSM state 가 KV cache lookup 만으로 재사용 불가** — 매 호출 partial recomputation (state transition 재계산)
  - (ii) Ollama 0.20.4 의 SSM prefix cache 최적화 미완성
  - (iii) hybrid SSM+attention 의 cache 동작이 dense attention 과 본질적으로 다름
- **production 동일 prefix 반복 query 시 dense 가 유리한 의외 결과** — MVP-1 advisory 패턴 (boss 가 동일/유사 prompt 다회 호출) 에 직접 영향

### 2.3 F3 — prefill cold compute MoE/dense ~5×

- cold prefill (cache empty): MoE/dense = ~5× → sparse activation 효과 명백
- *cold* prefill = compute-bound 영역, MoE 활성 ~3B 가정에 부합
- 단 SSM 의 cold 동작 = full compute 가정 (KV cache + SSM state 모두 초기화), 별도 검증 필요

---

## 3. M3 결정 후보 옵션 (런타임)

### 3.1 후보 매트릭스

| 옵션 | 런타임 | 장점 | 단점 / 정직성 |
|---|---|---|---|
| **M3-A** | **Ollama 단독** | 본 측정 환경 = Ollama → 즉시 운영 가능. SSM 동작 가능 (응답 한국어 정상) | F1 roofline 미달 (~25% 외부 실측). F2 cache hit dense ≫ MoE. Ollama 0.20.4 SSM 구현 효율성 미검증. 출처 미상 binary (§12 옵션 E DEFER) |
| **M3-B** | **llama.cpp 단독** | brief v2 R4 + 외부 실측 (~31 tok/s) → roofline 더 가까움 가능. Ollama 출처 미상 회피 | 빌드 발생 (별도 명시 승인). SSM 지원 미검증 (qwen3next 빌드 필요). 본 환경 측정 0 (Stage 4 부재) |
| **M3-C** | **Ollama + llama.cpp 동시 유지** (provider-agnostic) | 헌법 5조 답습 최대. 런타임 교체 가능 | 운영 복잡도 ↑. 둘 다 측정 필요 (트랙 B 시간 ↑) |
| **M3-D** | **MVP-1 트랙 B 진입 *연기* + 추가 측정** | F1/F2/F3 가설 검증 우선 (활성 파라미터·SSM 동작·cache miss 영역) | MVP-1 진척 ↓. V-1 cycle 길어짐 |
| **M3-E** | **다른 후보 (MLC-LLM / llamafile / ktransformers / vLLM MVP-2 재검토)** (R-7 답습) | brief v2 합의 R4·"3rd 후보 식별" 답습 | 본 환경 측정 0. 추가 빌드·설치·검증 필요 |

### 3.2 결정 의무 사항 (합의에서 답해야 할 질문)

| Q | 내용 |
|---|---|
| Q-M3-1 | **MVP-1 트랙 B 진입 자격**: F1/F2/F3 가설 검증 *없이* 진입 가능? 또는 가설 검증 *후* 진입? |
| Q-M3-2 | **런타임 *우선* 선택**: M3-A vs M3-B vs M3-C — Provider Liquidity 답습 (M3-C 권고 강도) |
| Q-M3-3 | **F2 (cache hit dense ≫ MoE+SSM) 의 production 영향**: advisory 패턴 (boss 동일 prompt 반복) 에서 MoE 가 dense 보다 *느림*. M2 (모델) 재선정 필요? |
| Q-M3-4 | **R-7 답습 3rd 후보**: 본 측정 결과를 토대로 3rd 후보 *식별* 시점 (지금 vs V-1 추가 cycle 후) |

---

## 4. M4 결정 후보 옵션 (tok/s threshold)

### 4.1 후보 매트릭스 (R-6/B-F8 답습, framing 주의)

| 옵션 | 내용 | 정직성 |
|---|---|---|
| **M4-A** | **threshold 결정 *연기*** — Stage 4 raw 만으로는 결정 입력 불충분 (cache miss 영역 미분리·SSM 동작 미검증) → 추가 cycle 후 결정 | ★ 권고 (정직성 최대) |
| **M4-B** | **threshold *낮추기*** — decode ≥ 5 tok/s 등 (현 실측 7.83 기반) | F1 roofline 미달 = 가정 자체 위배 → threshold 변경 가능. 단 "낮춰서 PASS" = anchor effect (B-F8 답습) |
| **M4-C** | **threshold *유지*** — brief v2 §6 "advisory ~15 tok/s" 유지 → 본 측정 (7.83) FAIL | "FAIL" 결론도 결정 *고정* 형식. 본 brief 권한 밖 |
| **M4-D** | **threshold *제거*** — tok/s framing 자체 폐지, 사용자 경험 metric 으로 대체 (응답 wall-clock·UX delay 등) | 본 brief 범위 초과 (별도 cycle) |

### 4.2 결정 의무 사항

| Q | 내용 |
|---|---|
| Q-M4-1 | **threshold 결정 *지금* vs *연기***: M4-A 권고 강도 |
| Q-M4-2 | **threshold 결정 *고정* vs *권고***: 본 합의 = 결정 *권고* 한정, 결정 *고정* 은 사용자 명시 후 |
| Q-M4-3 | **F1 활성 파라미터 가정 미검증 상태에서 threshold 결정의 정직성**: 가정 위배 = threshold 의미 자체 흔들림 |

---

## 5. 풀 3+1 분담

### 5.1 Agent A — 구현 분석가

**관점**: "실제로 동작하는가? 측정값으로 무엇이 가능한가?"

**핵심 질문**:
1. F1 roofline 미달의 *기술적* 원인 추정 (활성 파라미터 산정·SSM compute cost·Ollama 구현)
2. F2 cache 역전의 *기술적* 원인 추정 (SSM state vs KV cache 동작 차이)
3. M3-A/B/C 의 *기술적* 실현 가능성 + MVP-1 트랙 B 진입 자격
4. M4 raw 데이터 만으로 결정 *가능한지* 평가

### 5.2 Agent B — 안전성/품질 검증가

**관점**: "안전하고 견고한가? 거짓 안전감은 없는가? 정직성은?"

**핵심 질문**:
1. 본 raw 가 결정 *고정* 자격 있는지 (정직성·재현성 한계)
2. F1/F2/F3 가설 *검증 없이* 결정 시 risk
3. R-6 PASS/FAIL framing 회피의 *실제* 적용 (본 brief 어디에도 anchor effect 잔존?)
4. 출처 미상 Ollama (§12 옵션 E DEFER) 위에 M3 결정 고정의 거짓 안전감
5. F2 production 영향 (advisory 패턴) 의 안전성 평가

### 5.3 Agent C — 대안 탐색가

**관점**: "더 나은 방법이 있는가? 답습 권위와의 정합은?"

**핵심 질문**:
1. M3 5 옵션 외 *3rd 후보* 식별 (MLC-LLM·llamafile·ktransformers·vLLM MVP-2 등 R-7 답습)
2. F1/F2 가설 검증 *cycle* 의 우선순위 (활성 파라미터·SSM 동작·cache miss·다른 모델 등)
3. Provider Liquidity (헌법 5조) 답습 강도 — M3-C 가 답습에 가장 정합한지
4. M4 threshold framing 자체 재검토 (M4-D 등)
5. gap-pull entry brief 진입 권고 강도 (Qwen3.5-A3B-Instruct ~3B 비교)

### 5.4 Reviewer — 통합

- 3개 출력 교차 비교 → 일치 / 부분 일치 / 불일치 / 누락 분류
- 합의 R-# 도출 (BLOCKING / 권고 / NOTE)
- 본 brief 권위 한계 명시 (결정 *고정* 0건)

---

## 6. 답습 권위 한계 / 영구 금지

### 6.1 본 brief / 본 합의 권위 한계

- **결정 *고정* 0건** — 본 합의 = 결정 *권고* 한정. 결정 고정 = 사용자 명시 + 별도 단계 (브리프 +1)
- **추가 측정 실행 0건** — cache miss 분리·SSM golden output·llama.cpp 측정·gap-pull = 별도 cycle
- **트랙 B 구현 진입 자격 *권고* 만** — 진입 *시점* 사용자 명시 별도
- **Ollama 데몬 변경 0건** — pull / 재시작 / kill 절대 금지
- **보안 거버넌스 자동 재개 0건** — §12 옵션 E 비례성 평가는 별도

### 6.2 영구 답습 (이전 합의 권위)

- `feedback_provider_liquidity` — Provider Liquidity = 하드 요구 (코드 변경 없이 모델/구독 교체 가능)
- `feedback_staged_consensus_workflow` — 단계별 명시 승인 패턴
- `feedback_proportionate_security_personal_tool` — 본인용 solo 개인 툴 비례 보안
- `project_minimize_user_intervention` — 사용자 개입 최소화
- ADR-011 §2.1 (a)~(e) — 수단/목적 분리

### 6.3 정직성 caveats (본 brief 작성 자체)

- 본 brief 의 가설 (F1/F2/F3 원인 추정) = **추정 한정**, 검증 0
- raw 비율 (1.70×·5×·90×) = 측정값 직접 비교, 단일 세션 한정
- entry brief §1.2 출처 미상 Ollama 위에서 측정 = 모든 결과의 재현성 한계
- 본 brief 작성 자체 = 합의 *진입 단계* (결정 *권고* 아님)

---

## 7. 진행 흐름 (사용자 명시 승인 패턴)

```
사용자 brief 검토
    ↓
승인 시 → Agent A/B/C 병렬 독립 호출 (Task 도구 / general-purpose)
    ↓
3 출력 → Reviewer 통합 (메인 컨텍스트가 직접 수행)
    ↓
합의 보고서 작성 (`3plus1-consensus-2026-05-23-jarvis-mvp1-m3-m4-decision.md`)
    ↓
사용자 검토 → commit + push (별도 명시 승인)
    ↓
(다음 cycle) — 결정 *고정* 단계 또는 추가 측정/검증 cycle
```

---

**출처**: Stage 4 raw (`docs/phase0/v1-poc-raw/`) + findings (`jarvis-mvp1-v1-poc-findings.md` DRAFT Stage 1+2+3+4) + brief v1.1 + 합의 보고서 + MVP-1 brief v2 + ADR-011 §2.1.

**금지 (영구 답습, 본 brief 0건)**: 측정 실행 / 빌드 / 설치 / pull / sudo / 데몬 변경 / M3·M4 결정 고정 / 트랙 B 코드 작성 / 보안 거버넌스 자동 재개 / Provider Liquidity 약화 / 합의 본문 자동 정정.
