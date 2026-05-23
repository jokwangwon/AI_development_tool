# 3+1 합의 보고서 — Jarvis MVP-1 M3·M4 결정 합의 entry brief v1

**작성일**: 2026-05-23
**대상**: `docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md` (DRAFT v1)
**프로토콜**: **풀 3+1** (CLAUDE.md §3 — 아키텍처 큰 결정 + V-1 PoC Stage 4 의외 발견 3건 = 풀 3+1 필수)
**구성**: Agent A(구현 분석가) · Agent B(품질/안전성 검증가) · Agent C(대안 탐색가) 병렬 독립 → Reviewer 교차 비교
**최종 판정**: **APPROVE w/ COND (HIGH) — brief v1.1 보강 후 합의 결과로 진입 가능. BLOCKING 5건 미반영 시 결정 권고 자격 0.**

---

## 0. 3개 판정 요약

| Agent | 판정 | 한 줄 |
|-------|------|------|
| **A (구현)** | **REVISE** | F1 implied 활성 ~62B (역산) + manifest 산정 ~4.3B = 13배 격차 → "MoE sparse activation 효과 거의 무력화". ⭐ dense qwen2.5 effective BW 85GB/s = **273GB/s 의 31%** → **F1 anomaly의 2/3가 dense에서도 공통** ("MoE 가 문제다" framing 거부) |
| **B (안전)** | **REVISE** | brief 표면 정직성 PASS, 그러나 옵션 매트릭스 형식 자체가 "이 중 하나 선택" anchor → 결함 3종(활성 파라미터 미확인·cache miss 미분리·출처 미상 binary) silent화. **M3-D + M4-A 외 권고 자격 0**. §12 옵션 E cross-ref 약함 |
| **C (대안)** | **APPROVE w/ COND** | M3-C framing 유지 + M3-D (추가 측정 cycle) 선행. 3rd 후보 카탈로그(MLC-LLM·llamafile)는 *식별만*, 측정/채택 0. F1/F2 검증 cycle 우선순위 = Phase 1 (C-c cache miss 분리 + C-a 활성 파라미터 HF egress) → Phase 2 (C-e llama.cpp) → Phase 3 (C-d gap-pull) |

**3개 모두 본 brief 의 결정 *고정* 0건 답습 정합 + M3-D + M4-A 우선 권고 일치. agent-level BLOCKING 합 8건 → Reviewer 권위로 5건 통합·격상 (R-1~R-5).** 방향 (cache 역전·roofline 미달 해석 + 결정 권고 *온전* 자격 평가) 자체에 합의. 조건 = 아래 brief v1.1 보강 + 합의 결과 채택.

---

## 1. 교차 비교 (4 분류)

### ① 일치 (Consensus, 3/3)

- **C-1**: **본 합의에서 M3·M4 결정 *고정* 0건** — entry brief §6.1 영구 답습 강화. 본 합의 = 결정 *권고* 한정.
- **C-2**: **M3-D (트랙 B 진입 연기 + 추가 측정 cycle) + M4-A (threshold 결정 연기) 우선 권고** — 3개 Agent 모두 동의. raw 결함 (활성 파라미터 미확인·cache miss 미분리·출처 미상 binary) 위에서 결정 *권고* 자격 *온전* 옵션 = M3-D + M4-A.
- **C-3**: **M4-B (threshold 낮추기) anchor effect 영구 거부** — 3개 모두 명시. B-F8 답습 (entry brief 합의 R-6).
- **C-4**: **F1/F2 검증 cycle 추가 권고** — 활성 파라미터 정량 + cache miss 영역 분리 측정 필수 입력.
- **C-5**: **M3-A (Ollama 단독) 권고 자격 부족** — Provider Liquidity (헌법 5조) 약화 + F1 anomaly 미규명 + 출처 미상 Ollama 영속화 risk.
- **C-6**: **anchor 회피 / framing 정직성** — PASS/FAIL 단어는 사용 0건이나, "1.70× R-18 미달" 표현 / 옵션 매트릭스 형식 / "advisory 패턴 = 동일 prompt 반복" 가정 등이 *약한 anchor* 로 작용. SOP 강화 의무.
- **C-7**: **측정 실행 0 / 빌드 0 / 결정 고정 0 / Ollama 데몬 변경 0 / 보안 거버넌스 자동 재개 0** — 본 합의 자체의 영구 답습.

### ② 부분 일치 (Partial, 2/3)

- **P-1 (A·B)**: **옵션 매트릭스 형식 자체가 anchor** — A의 §4.3 매트릭스 평가 + B의 R-B-1 ("이 중 하나 골라야 한다" anchor) → Reviewer 통합 **R-2** (BLOCKING).
- **P-2 (A·C)**: **Provider Liquidity (헌법 5조) → M3-C framing 유지** — A의 R-A-8 + C의 R-C-6. B는 안전성 관점 직접 권고 X, 단 §6.1 Provider Liquidity 정합 표 (M3-A 약함 / M3-C 최대) 답습. **삼각 합의 → 권고 채택**.
- **P-3 (A·C)**: **F1/F2 검증 cycle 우선순위** — A의 R-A-7 (진단 cycle 권고: nvidia-smi dmon·OLLAMA_DEBUG·dense effective BW) + C의 R-C-5 (Phase 1 = C-c cache miss + C-a 활성 파라미터). 약간 다른 cycle 형태이나 방향 일치. **통합 R-5**.
- **P-4 (B·C)**: **§12 옵션 E cross-ref 강화** — B의 R-B-2 (BLOCKING: M3-A/M3-C 권고 시 위생 정정 *선행* 의무 명문) + C의 R-C-9 (권고: trigger 강도 증가 보고). B 격상 강도 우선 → Reviewer **R-3** (BLOCKING).
- **P-5 (A·C)**: **M3-E 3rd 후보 식별** — A의 R-A-10 (4 후보 모두 qwen3next+aarch64+sm_120 동시 충족 검증된 후보 0) + C의 R-C-4 (카탈로그 작성, 측정/채택 0, MLC-LLM·llamafile 만 Provider Liquidity 정합). 평가 일치. **통합 권고 (R-7)**.

### ③ 불일치 (Divergence, 3개 다른 방향)

- **D-1 (판정)**: A=REVISE / B=REVISE / C=APPROVE w/ COND. A·B 의 REVISE 근거 = *brief framing 보강* (옵션 매트릭스 anchor + §12 옵션 E cross-ref 추가), C 의 APPROVE w/ COND = *권고 사항 추가 단계 권고*.
  - **Reviewer 분석**: 충돌이 아닌 표현 차이. A·B 가 *brief 본문 의무 보강* 요구, C 가 *권고 단계 결과 채택* 권고. 본 합의 보고서 = (1) brief v1.1 보강 의무 (BLOCKING 5건 반영) + (2) 합의 결과 채택 으로 *합치* 가능.
  - **Reviewer 선택**: **최종 판정 = APPROVE w/ COND (HIGH)** — brief v1.1 보강 후 합의 결과로 진입 가능. BLOCKING 5건 = boundary 명확. (A·B 의 REVISE 강도 답습 + C 의 APPROVE w/ COND 답습 동시 충족)
- **D-2 (M4-D framing 폐지)**: A 미언급 / B 미강조 (안전성 관점 외) / C-R-C-7 (M4-D 별도 cycle 권고 - tok/s → UX wall-clock metric).
  - **Reviewer 선택**: **C-R-C-7 단독, NOTE 격하** — 본 합의 시점 범위 초과. 별도 advisory UX 설계 brief 단계.
- **D-3 (advisory 패턴 prompt prefix 구조 가정)**: B-R-B-4 (검증 0 가정 명문화 권고) / A 미언급 / C 미언급.
  - **Reviewer 선택**: **B-R-B-4 권고 채택**.

### ④ 누락 (Gap, 1 agent 만)

- **G-1 (A 단독, 가장 critical)**: ⭐ **dense qwen2.5 effective BW 85GB/s = 273GB/s 의 31%** 발견. F1 anomaly 의 2/3 가 dense 에서도 공통 → "MoE 가 문제다" framing 거부 + "GB10/Ollama effective BW 자체가 spec 의 1/3" 가설 추가. **A 의 R-A-B3 BLOCKING**. B·C 미발견 → Reviewer 격상 **BLOCKING (R-1, 본 합의 가장 critical 의외 발견 #4 추가 의무)**.
- **G-2 (A 단독)**: **manifest 필드 활성 파라미터 ~4.3B 1차 산정** — lower-bound. F1 가설 정량화. **Reviewer 격상 권고 (brief F1 가설 (i) 정량화)**.
- **G-3 (B 단독)**: **F2 = 안전 risk 아니라 UX risk** — R3 fail-closed 답습 위에서 advisory 부재 = 결정적 flag + 사람 게이트 그대로 → 안전 침식 0. 거짓 *위험감* (반대 방향 거짓 안전감) 차단. **B 의 R-B-8 NOTE → Reviewer 권고 격상**.
- **G-4 (B 단독)**: **brief 의 옵션 매트릭스 형식 자체가 anchor** (R-B-1) → Reviewer 격상 **BLOCKING (R-2)**.
- **G-5 (B 단독)**: **§12 옵션 E cross-ref 강화** (R-B-2) → Reviewer 격상 **BLOCKING (R-3, V-1 entry 합의 R-1 의 연장선)**.
- **G-6 (B 단독)**: **Boss advisory timeout 정책** = brief v2 합의 R3 분기 합류. **권고 채택**.
- **G-7 (B 단독)**: **anchor 회피 SOP 4 카테고리** (비율 표현·옵션 선택·"권고" 단어·가설 언급). **권고 채택 (부록)**.
- **G-8 (C 단독)**: **M4-D (tok/s → UX wall-clock metric)** 별도 cycle 권고. **NOTE 채택**.
- **G-9 (C 단독)**: **3rd 후보 카탈로그 MLC-LLM·llamafile** — Provider Liquidity 정합 후보. 측정·채택 0. **권고 채택**.
- **G-10 (C 단독)**: **gap-pull 본 합의 시점 *고정 0*** — C-a (활성 파라미터 HF egress) 결과 후 trigger. **권고 채택**.
- **G-11 (A 단독)**: **MVP-1 트랙 A 는 본 합의와 무관** — 이미 `83aebad` 진행. 본 합의가 트랙 A 차단 X 명시. **권고 채택**.
- **G-12 (A 단독)**: **advisory 패턴 wall-clock 측정** (TTFT + 출력 256 tok end-to-end). tok/s 자체는 user-facing metric 아님. **권고 채택 (M4-D 와 연결)**.
- **G-13 (B 단독)**: **M3 결정 고정 단계 = ADR-011 §2.1 (a)~(d) 답습 의무** (R-B-7). **NOTE 채택**.
- **G-14 (C 단독)**: **ktransformers · SGLang · TGI · Hermes/LiteLLM** = NOTE 한정, MVP-1 진입 0. **NOTE 채택**.

---

## 2. 합의 결정 사항 (R-# = brief v1.1 반영 의무 또는 본 합의 결과 명문)

### 🔴 BLOCKING (brief v1.1 보강 + 본 합의 결과 명문 필수)

| R-# | 출처 | 요지 | 반영 위치 |
|----|----|----|----|
| **R-1** | A-R-A-B3 (Reviewer 격상, 본 합의 가장 critical) | ⭐ **brief §2 의외 발견 #4 추가 의무**: dense qwen2.5-coder decode 4.62 tok/s × 18.5GB = effective BW ~**85GB/s** (273GB/s 의 **31%**). F1 anomaly 의 2/3 가 dense 에서도 공통 → **"GB10/Ollama effective BW 자체가 spec 의 1/3" 가설 추가** (가설 (v)). "MoE 가 문제다" framing 거부 + F1 anomaly 의 *원인 분리* (Ollama 구현 효율 vs effective BW vs MoE 본질) 명문 의무 | brief §2 (F4 추가) + §3.1 (M3-A·M3-B 단점 칼럼 강화) |
| **R-2** | B-R-B-1 (Reviewer 격상) + P-1 (A·B 통합) | **옵션 매트릭스 위에 "권고 자격 검증" 단계 명문 필요**: 본 brief §3·§4 첫 줄에 "권고 *온전* 자격 옵션 = M3-D + M4-A 한정. M3-A/B/C 는 §3.2 결함 3종 미해소 시 권고 자격 0" 명시. §5.4 Reviewer 권위 한계 강화 (3개 결함 silent 화 방지) | brief §3 첫 줄 + §4 첫 줄 + §5.4 |
| **R-3** | B-R-B-2 (Reviewer 격상, V-1 entry 합의 R-1 연장선) + P-4 (B·C 통합) | **§12 옵션 E cross-ref 강화 의무**: M3-A 또는 M3-C 권고 도출 시 위생 정정 합의 *선행* 의무 명문. brief §3.2 결정 의무 사항에 Q-M3-5 추가 ("M3-A/M3-C 권고 시 §12 옵션 E 합의 *선행* 의무 명문 필요?"). §3.1 M3-A 단점 칼럼에 "§12 옵션 E 합의 *선행* 의무" 추가 | brief §3.1 M3-A 단점 + §3.2 Q-M3-5 신규 + §6.2 §12 옵션 E 직접 cross-ref |
| **R-4** | A·B·C 통합 (C-3) | **M4-B (threshold 낮추기) framing 영구 거부 명문**: "현 측정 7.83 tok/s 에 맞춘 새 threshold" 류 표현 합의 보고서 본문·brief 본문 영구 금지. B-F8 anchor effect 답습 (entry brief 합의 R-6). C-4 framing 압력 회피 동형 | brief §4.1 M4-B 행 강화 + 합의 보고서 §3 명문 |
| **R-5** | A-R-A-7 + C-R-C-5 통합 (P-3) | **F1/F2 검증 cycle 우선순위 명문**: Phase 1 (egress 0 + 빌드 0) = **C-c (cache miss 영역 분리, unique prompt seed)** + **C-a (활성 파라미터 정량 HF egress, 30분 1회, R-11 답습 baseline *전* 실행 시 §8 trace 포함 의무)** + **A-진단 (nvidia-smi dmon GB10 effective BW 직접 측정·OLLAMA_DEBUG=1 expert prefetch 관찰·dense effective BW 확정)**. Phase 2 = C-e (llama.cpp 빌드·측정). Phase 3 = C-d (gap-pull) + C-b (SSM golden) + C-f (isovolumetric). 각 cycle 별도 명시 승인 필수 | brief §7 진행 흐름 강화 + 본 합의 보고서 §5 추가 cycle 명문 |

### 🟡 권고 (brief v1.1 또는 본 합의 결과 권고, 미반영도 합의 진입 비차단)

| R-# | 출처 | 요지 |
|----|----|----|
| **R-6** | A-R-A-8 + C-R-C-6 (P-2) | **M3 *결정 권고* = M3-C framing 유지** (Provider Liquidity 헌법 5조 답습 최대) + **M3-D (추가 측정 cycle) 우선 진입**. M3-A 단독 운영 default 결정 표현 영구 금지 (anchor effect 강) |
| **R-7** | A-R-A-10 + C-R-C-4 (P-5) | **M3-E 3rd 후보 카탈로그**: MLC-LLM·llamafile (Provider Liquidity 정합 + §12 옵션 E 정합 후보) **식별 한정**, 측정·채택 0. trigger = (a) M3-A + M3-B 둘 다 측정 후에도 F1 roofline 미달 *공통* 확인 또는 (b) §12 옵션 E trigger 발효. ktransformers·SGLang·TGI·Hermes/LiteLLM = NOTE 한정 |
| **R-8** | B-R-B-3 | **옵션 매트릭스 위치 anchor 회피** — M3-D 를 1번째 또는 별도 분류 ("default = 연기 + 추가 측정") |
| **R-9** | A-R-A-11 + G-11 | **MVP-1 트랙 A 는 본 합의와 무관 진행 가능** (이미 `83aebad`). 본 합의 결과가 트랙 A 차단 X 명시 |
| **R-10** | A-G-2 (Reviewer 격상) | **manifest 활성 파라미터 ~4.3B 1차 산정** brief §2.1 F1 가설 (i) 정량화. 단 "검증 가능성 명시" + 보정 4종 (router/gating overhead, GQA, dense FFN, attention proj GQA) 모두 *측정과의 격차를 더 키우는 방향* 명문 |
| **R-11** | B-R-B-4 | **advisory 패턴 prompt prefix 구조 가정 명문화** — brief §2.2 "동일/유사 prompt 다회 호출" 가정 검증 0 명시. 검증 cycle (advisory 실 prompt 구조 분석) 별도 |
| **R-12** | B-R-B-5 + A-R-A-11 + G-12 | **F2 production 영향 평가 = wall-clock 단위 재구성** — tok/s 단독 비교가 advisory UX 결정에 직접 매핑되지 않음. (prefill wall-clock + decode wall-clock × tokens) 합 단위 평가 |
| **R-13** | B-R-B-6 | **Boss advisory timeout 정책** — brief v2 합의 R3 ("다운/비정상" 분기) 에 timeout 분기 합류. 본 합의 범위 밖이면 별도 cycle |
| **R-14** | A-R-A-N2 + G-3 (B 단독) | **F2 framing 정확화**: "90× 역전" → "qwen2.5 dense 는 prefix-hit 으로 prompt_eval≈0.3초·qwen3cnext 는 prefix-hit 거의 미작동 26초 잔존". + **F2 = 안전 risk 아니라 UX risk 명시** (R3 fail-closed 침식 0, 거짓 *위험감* 차단) |
| **R-15** | C-R-C-8 | **gap-pull 본 합의 시점 *고정 0*** — C-a (HF egress) 결과 후 trigger. trigger 시 (a) 디스크 가드 ≤ 50GB 누적 (b) egress 별도 명시 승인 (c) raw 보존 R-22 답습 (d) 활성 ~3B + Q4 ≤ 20GB 우선·mixtral 직접 비교 금지 (R-14 답습) |
| **R-16** | C-R-C-9 | **§12 옵션 E trigger 강도 *증가* 보고** — F1·F2 가 Ollama 출처 미상 + 0.20.4 SSM quirk 와 간접 연결. *발효* 결정 = 사용자 명시 (본 합의 범위 밖), *trigger 강도 증가* 는 정직성 보고 |
| **R-17** | A-R-A-N1 | **manifest `attention.head_count_kv` null 의미 해석** — GQA 여부 미해석. 활성 파라미터 정확도 ↑ 필요 시 모델 카드 또는 소스 확인. C-a cycle 에 포함 |
| **R-18** | A-R-A-N3 | **H-B3 가설 정성적 일치**: attention 12/48 (=25%) KV cache hit + SSM 36/48 dominant compute → warm 28초 / cold 135초 = 21% ≈ 25% 일치. 가설 강도 ↑, 단 측정 추가 검증 별도. C-c cycle 에 통합 |

### 🟢 NOTE (선택, 향후 답습)

R-19 ~ R-30:
- **R-19** (B-R-B-7): M3 *결정 고정* 단계 = ADR-011 §2.1 (a)~(d) 답습 의무. 본 합의 §6.1 "결정 *고정* = 별도 단계" 와 결합
- **R-20** (B-R-B-9): anchor 회피 SOP 4 카테고리 (비율 표현·옵션 선택·"권고" 단어·가설 언급) brief 부록 명문 검토
- **R-21** (C-R-C-7 + G-8): M4-D (tok/s → UX wall-clock metric) framing 별도 cycle. advisory UX 설계 brief 신규
- **R-22** (C-R-C-10): ktransformers · SGLang · TGI = NOTE 한정, MVP-1 진입 0
- **R-23** (C-R-C-11): C-d (다른 MoE 비교) · C-f (isovolumetric) = MVP-2 단계
- **R-24** (C-R-C-12): R-30 isovolumetric baseline 별도 단계
- **R-25** (C-R-C-13): M4-D 진입 시 user-perceived latency 측정 절차 별도 brief
- **R-26** (C-R-C-14): Hermes / LiteLLM = MVP-2 진화 경로 (brief v2 R13 답습)
- **R-27** (A 추가): GB10 effective BW 직접 측정 도구 후보 (`nvidia-smi dmon -s mu` + custom microbench `bandwidthTest` etc) MVP-2 단계
- **R-28** (B 추가): 거짓 *위험감* 차단 — F2 = 안전 risk 아님 명시 (R-14 강화)
- **R-29** (C 추가): TensorRT-LLM = NVIDIA 종속 + 답습 약함, 비권고
- **R-30** (Reviewer): 본 합의 보고서 자체가 *anchor* 가 될 risk — "REVISE 가 2개라 brief 재작성 의무" 단순 채택 회피. **REVISE 의 근거 (R-1~R-5 보강) 가 실제 단순** = brief v1 → v1.1 *축약* 패턴 (V-1 entry 합의 답습)

---

## 3. 합의 결과 통계

| 분류 | 건수 |
|----|----|
| 🔴 BLOCKING (R-1 ~ R-5) | **5** |
| 🟡 권고 (R-6 ~ R-18) | **13** |
| 🟢 NOTE (R-19 ~ R-30) | **12** |
| 기각 | **0** |
| **합계** | **30** |

**3개 Agent 출력 모두 답습 권위 (entry brief v1.1 + 합의 R-1~R-6 + brief v2 §6 + MVP-1 합의 R1~R13 + CLAUDE.md + ADR-011) 와 모순 없음.** 판정 분기 (A·B REVISE / C APPROVE w/ COND) = 표현 차이, *brief v1.1 보강 의무 + 합의 결과 채택* 으로 합치.

---

## 4. 본 합의 결정 권고 (사용자 명시 단계 입력 한정)

### 4.1 M3 결정 권고 (★ 합의 권고, 결정 *고정* 0건)

- **M3-C framing 유지** (Provider Liquidity 헌법 5조 답습 최대) + **M3-D (추가 측정 cycle) 우선 진입**
- **M3-A 단독 권고 자격 0** (F1 anomaly 미규명 + 출처 미상 binary 영속화 risk + §12 옵션 E cross-ref 의무)
- **M3-B 단독 권고 자격 0** (Ollama 기 설치 폐기 비례성 위반)
- **M3-E 3rd 후보** = 카탈로그 한정 (MLC-LLM·llamafile), 측정·채택 0 (R-7)
- **M3 *결정 고정*** = 본 합의 권한 밖. F1/F2 검증 cycle (R-5) 후 별도 합의 + 사용자 명시

### 4.2 M4 결정 권고 (★ 합의 권고, 결정 *고정* 0건)

- **M4-A (threshold 결정 *연기*) 단독 채택**
- **M4-B (낮추기) framing 영구 거부** (R-4 BLOCKING)
- **M4-C (유지)** = "FAIL" 결론도 결정 *고정* 형식, 본 합의 권한 밖
- **M4-D (tok/s → UX wall-clock metric)** = 별도 cycle (R-21 NOTE)

### 4.3 다음 cycle 권고 (★ Phase 1 우선)

**Phase 1 (egress 0 + 빌드 0, 즉시 가능 권고)**:
- **C-c**: cache miss 영역 분리 측정 (unique prompt seed, ~1-2시간)
- **A-진단**: nvidia-smi dmon GB10 effective BW + OLLAMA_DEBUG=1 expert prefetch (~30분)

**Phase 2 (egress 발생, 별도 명시 승인)**:
- **C-a**: 활성 파라미터 정량 HF egress (30분, R-11 답습 → §8 baseline 의무)

**Phase 3 (큰 cost, 별도 cycle)**:
- **C-e**: llama.cpp 빌드 + 동일 측정 (R4 답습)
- **C-d**: gap-pull (Qwen3.5-A3B-Instruct 등)
- **C-b**: SSM golden output 검증
- **C-f**: isovolumetric baseline (MVP-2)

### 4.4 본 합의 자격 한계

- 본 합의 = M3·M4 결정 *권고* 한정. **결정 *고정* 0건**
- 본 합의 결과 채택 = 사용자 명시 + brief v1.1 (R-1~R-5 보강) 작성 + 다음 cycle 진입 단계
- 본 합의 결과가 **MVP-1 트랙 A 차단 X** (이미 진행 `83aebad`)
- 본 합의 결과가 **트랙 B 진입 차단 X / 권고 X** — 진입 시점 = F1/F2 검증 cycle 결과 + 사용자 명시 별도

---

## 5. 추가 cycle 권고 상세 (R-5 BLOCKING 답습)

### 5.1 Phase 1 — egress 0 + 빌드 0

| cycle | 명령 | 자원 | egress | 권한 |
|---|---|---|---|---|
| **C-c (cache miss 분리)** | `curl /api/generate` with unique prompt seed (timestamp suffix) × 5 + prefix 변형 + LRU eviction 강제 (다른 prefix 호출 끼워넣기) | ~1-2시간 측정 + R-1 hash 3회 + R-23 freeze | 0 (localhost) | 별도 명시 승인 |
| **A-진단** | `nvidia-smi dmon -s mu -c 100` 백그라운드 + decode 측정 동시 → DRAM read BW 직접 관측. + `OLLAMA_DEBUG=1` env 적용 시도 (R-34 fresh subshell·데몬 환경 변경 X) | ~30분 | 0 | 별도 명시 승인 |

### 5.2 Phase 2 — egress 발생, 별도 명시 승인

| cycle | 명령 | 자원 | egress | 권한 |
|---|---|---|---|---|
| **C-a (활성 파라미터 정량)** | HF 페이지 조회 (`https://huggingface.co/Qwen/Qwen3-Next-80B-A3B-Instruct` 등 추정 URL) read-only | ~30분 | 발생 (HF) | 별도 명시 승인 (R-11 답습 + §8 baseline 시점 포함 의무) |

### 5.3 Phase 3 — 큰 cost, 별도 cycle

| cycle | 명령 | 자원 | egress | 권한 |
|---|---|---|---|---|
| **C-e (llama.cpp)** | brief v1.1 §7-B/C 절차: source build (CUDA 13.0 + sm_120/121) 또는 prebuilt aarch64. R-17 위생 (~/build/llama.cpp 비어있음 + 실패 시 정리 + `make install` 금지). R-39 prebuilt SHA 확인 | ~5-8시간 + 빌드 cost | 0 (로컬 빌드) | 별도 brief + 사용자 명시 승인 |
| **C-d (gap-pull)** | Qwen3.5-A3B-Instruct 등 `ollama pull` + 동일 §4 측정 절차 | ~3-5시간 + 디스크 ~50GB | 발생 (ollama.com) | 별도 brief + 사용자 명시 승인 |
| **C-b (SSM golden)** | unique fresh prompts + 응답 quality 평가 | ~1-2시간 측정 + 별도 quality baseline | 0 (또는 reference 비교 시 egress) | 별도 brief |
| **C-f (isovolumetric)** | 활성 파라미터 동등 (~3B) dense 모델 비교 | gap-pull 추가 | 발생 | MVP-2 단계 |

### 5.4 본 합의의 권위 한계

- 본 합의 = 다음 cycle *식별 + 우선순위 권고* 한정. cycle *실행 시점* = 사용자 명시 + 별도 brief.
- 각 cycle 결과 = M3·M4 결정 *고정* 입력. 결정 *고정* 자체는 추가 합의 + 사용자 명시.

---

## 6. Reviewer 정직성 노트

### 6.1 Reviewer 가 *직접 검증하지 못한* 것

1. **3개 Agent 의 raw 인용 정확성** — 본 Reviewer 가 Stage 4 raw 30 JSON 파일 직접 재검증 0. Agent A·B·C 의 인용은 summary JSON (`2026-05-23T21-30-v1-3-measurement-summary.json`) 와의 일치 한정.
2. **Agent A 의 활성 파라미터 ~4.3B 산정 재검증** — manifest 필드 직접 계산. Reviewer 가 *같은 산정* 수행 0 = Agent A 의 *추정 가능성* 평가 한정.
3. **Agent A 의 dense effective BW 85GB/s 역산 재검증** — 측정값 + memory-bound 가정 역산. *완전 memory-bound 가정* 자체 별도 검증 필요.
4. **Agent C 의 후보 4종 (MLC-LLM 등) 외부 문서 추정 재검증** — Reviewer 가 외부 페이지 조회 0 (R-11 답습). C 의 정직성 노트 한정.
5. **Agent B 의 옵션 매트릭스 anchor 강도 평가** — *주관적 정직성* 평가. Reviewer 가 동의 ("이 중 하나 골라야 한다" 함의는 옵션 매트릭스의 본질) 하나 *강도* 측정 X.

### 6.2 본 합의 권위 한계

- 본 합의 = brief v1 → v1.1 *진입 게이트* 한정. **M3·M4 결정 *고정* 0건**. brief v1.1 작성 → 사용자 검토 → 추가 cycle 진입 = 각각 별도 명시 승인.
- 본 합의의 BLOCKING 5건 = brief 본문 보강 의무. brief v1.1 보강 = 합의 결과 채택 자격 충족.
- 본 합의 결과가 *Phase 1 cycle 진입* 권고 → 진입 시점 = 사용자 명시 + 추가 brief.

### 6.3 본 합의가 생성한 것 / 생성하지 않은 것

- **생성한 것**: R-# 30 결정 (BLOCKING 5 + 권고 13 + NOTE 12), brief v1.1 보강 의무 목록, 다음 cycle 우선순위 (R-5), M3-C framing + M3-D 우선 진입 권고 (R-6), M4-A 단독 채택 (R-4).
- **생성하지 않은 것**: brief 직접 수정 0 / commit·push 0 / 실 명령 실행 0 / 측정 실행 0 / 빌드 0 / pull 0 / M3·M4 결정 *고정* 0 / 트랙 B 코드 작성 0 / 보안 거버넌스 재개 0 / §12 옵션 E 발효 0 / Provider Liquidity 약화 0.

---

## 7. 합의 후 단계 권고 (사용자 명시 승인)

| 단계 | 내용 | 권한 |
|---|---|---|
| **A** | **brief v1.1 보강** (R-1 ~ R-5 BLOCKING 반영 + R-6 ~ R-18 권고 13건 반영) → 사용자 검토 | 본 합의 후 *직접* 권고 |
| **B** | **합의 보고서 + brief v1.1 commit + push** | 사용자 명시 승인 |
| **C** | **Phase 1 cycle 진입 권고** (C-c + A-진단, egress 0 + 빌드 0) | 사용자 명시 승인 + R-1 hash 의무 + R-23 freeze |
| **D** | **Phase 2 cycle 진입** (C-a HF egress) | 사용자 명시 승인 + R-11 답습 (§8 baseline 시점 포함 의무) |
| **E** | **Phase 3 cycle 진입** (C-e llama.cpp 빌드·측정) | 별도 brief + 사용자 명시 승인 |
| **F** | **M3·M4 *결정 고정*** 합의 | Phase 1+2 cycle 결과 + 추가 합의 + 사용자 명시 |
| **G** | **§12 옵션 E 위생 정정 trigger 발효 검토** | 별도 brief + 사용자 명시 + 비례성 평가 |
| **H** | **MVP-1 트랙 B 구현 진입** | M3 결정 *고정* + 사용자 명시 (본 합의 무관 진입 X) |

**자동 다음 단계 진입 0건** (CLAUDE.md feedback_staged_consensus_workflow 답습).

---

**출처**: Agent A 출력 (구현, 12K tokens) + Agent B 출력 (안전, 11K tokens) + Agent C 출력 (대안, 9K tokens), 모두 본 합의 entry brief v1 + V-1 findings + Stage 4 raw 30 JSON + summary + entry brief v1.1 + V-1 entry 합의 + MVP-1 brief v2 + MVP-1 합의 + CLAUDE.md + ADR-011 §2.1 기반. **편향 방지 답습**: Agent A·B·C 상호 출력 참조 0건 (병렬 독립).

**답습**: `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `project_minimize_user_intervention` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 (a)~(d).

**금지 (영구 답습, 본 합의 0건)**: M3·M4 결정 *고정* / 측정 *실행* / 빌드 *실행* / pull / sudo / 데몬 변경 / 코드 작성 / 파일 작성 외 본 합의 보고서 / commit (별도 단계) / push (별도 단계) / 보안 거버넌스 자동 재개 / Provider Liquidity 약화 / 합의 본문 자동 정정 / 트랙 B 진입 자동 권고 / §12 옵션 E 자동 발효 / Agent 출력 자동 수정.
