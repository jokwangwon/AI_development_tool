# Jarvis (p) 다중 모델 측정 brief — 4 후보 모델 N=3 비교

> **scope**: (a) 단일 모델 (qwen3-30b-a3b) 측정 → 4 후보 모델 N=3 비교. M3·M4 결정 *고정* 0건 = 측정 자료 수집만, 결정은 별도 cycle.
> **DONE 기준**: 4 모델 × N=3 = 12 raw 측정 + 비교 표 + raw JSON evidence.
> **답습**: 후속 (p) [[v00-sprint-pending]] + (a) 답습 + [[ceremony-inflation]] 1-agent + [[provider-liquidity]] 활용.

---

## 1. 모델 후보 (4 종)

Ollama 로컬 모델 8 종 중 boss 후보로 합리적 4 종 선정:

| 모델 | 파라미터 | 크기 | family | 비고 |
|------|---------|------|--------|------|
| **qwen3-30b-a3b-instruct** | 30.5B (MoE 활성 ~3B) | 17GB | qwen3moe | **(a) baseline, 현 OllamaBoss 기본** |
| qwen2.5-coder:32b | 32.8B (dense) | 18GB | qwen2 | code 특화 dense |
| exaone3.5:32b | 32.0B (dense) | 18GB | exaone | 한국어 강함 (LG) |
| glm-4.7-flash | 29.9B (MoE-lite) | 17GB | glm4moelite | 최신 MoE-lite |

**제외**:
- llama3.3:70b (39GB) — 너무 큼 + 시간 오래
- qwen3-coder-next (79.7B MoE+SSM, 48GB) — V-1 답습 측정 완료, 다른 패밀리
- qwen3:30b-a3b-instruct-2507-q4_K_M — qwen3-30b-a3b-instruct-2507-bartowski 와 중복
- exaone4:32b (31GB) — 후속 cycle 후보

## 2. 측정 시나리오 (모델당 동일)

(a) 답습 — boss_measurement.py 의 helper 재사용:
- 표준 advice prompt (boss_prompt_for("code") + 동형 user_blob)
- warmup 1 회 + measure N=3
- Ollama metadata 6 필드 + 파생 metric 3 종 (decode/prefill/latency)

## 3. 출력 형식

**비교 표** (decode rate 내림차순):
```
=== 4 모델 N=3 비교 (decode rate 정렬) ===
모델                                      decode      prefill     latency
                                          mean p50    mean p50    mean p50
qwen3-30b-a3b-instruct-...                15.16 14.98 3042 2984   5.91 5.94
glm-4.7-flash:latest                      X.XX  X.XX  XXXX XXXX   X.XX X.XX
qwen2.5-coder:32b                         X.XX  X.XX  XXXX XXXX   X.XX X.XX
exaone3.5:32b                             X.XX  X.XX  XXXX XXXX   X.XX X.XX
```

**raw JSON evidence**: 각 모델별 N=3 metadata + 통계 + 비교 ranking.

## 4. 합격 조건

- 4 모델 모두 precheck PASS (Ollama 가용 + 모델 존재)
- 각 모델 N=3 모두 valid (HTTP 200 + metadata 6 필드)
- 비교 표 산출 + 모델별 decode rate 차이 명시
- raw JSON evidence 기록

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| 모델 로드 간 메모리 압박 (16~18GB 모델 4 종) | 순차 호출 (Ollama 가 자동 unload/load), 동시 0 |
| 측정 시간 (4 × ~30초 = ~2분) | warmup 포함 acceptable, run_in_background 가능 |
| 모델별 응답 길이 차이 → decode rate 비교 왜곡 | 동형 prompt 사용 (응답 길이는 모델 특성, 통계로 보정) |
| Q4 quantization 차이 (모델별 다를 수 있음) | 본 cycle = Ollama 기본 quant 한정. 비교 *상대값* 으로 활용 |

## 6. 비-scope (DEFER 영구)

- **M3·M4 결정 고정** = 본 cycle = 측정 *자료* 만, 결정은 별도 cycle
- N=10+ 통계 신뢰도 — N=3 한정
- cold vs warm 분리 — 별도 cycle
- 응답 *품질* 평가 (단순 속도 비교만) — Layer 2+ (사람 게이트)
- llama3.3:70b / qwen3-coder-next / exaone4:32b 측정 — 별도 cycle
- 모델 자동 라우팅 (task 별 최적 모델 선택) — Layer 2+ 영역
- nvidia-smi / NVBandwidth 정밀 측정 — 별도 cycle

DONE 후 단일 commit + push + memory.
