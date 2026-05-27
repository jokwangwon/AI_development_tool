# Jarvis MVP-1 트랙 B (a) 로컬 보스 LLM 측정 brief

> **scope**: OllamaBoss 가 실 동작 입증 후 *측정 cycle* 진입. 단일 모델 N=3 동형 호출 → decode rate / prefill rate / latency 분포 raw evidence 1건.
> **DONE 기준**: N=3 raw 측정 결과 + Ollama metadata 추출 + p50/mean/std 통계 + raw log 보존.
> **답습**: 후속 (a) [[v00-sprint-pending]] + [[mvp_staged_roadmap]] V-1 측정 패턴 + [[ceremony-inflation]] 1-agent + 단일 모델 한정 (M3·M4 결정 *고정* 0건).

---

## 1. 측정 항목 (v0.0 한정)

Ollama `/api/chat` 응답이 제공하는 metadata (실측):

| 필드 | 단위 | 의미 |
|------|------|------|
| `total_duration` | ns | 총 처리 시간 (load + prompt + eval) |
| `load_duration` | ns | 모델 로드 시간 (cold = 큼, warm = 0~작음) |
| `prompt_eval_count` | tokens | 입력 토큰 수 |
| `prompt_eval_duration` | ns | 입력 처리 시간 |
| `eval_count` | tokens | 출력 토큰 수 |
| `eval_duration` | ns | 출력 생성 시간 |

파생 metric:
- **decode rate** = `eval_count / (eval_duration / 1e9)` [tok/s] — 응답 생성 속도
- **prefill rate** = `prompt_eval_count / (prompt_eval_duration / 1e9)` [tok/s] — 입력 처리 속도
- **end-to-end latency** = `total_duration / 1e9` [s]

## 2. 측정 시나리오 (N=3 동형)

- **모델**: `qwen3-30b-a3b-instruct-2507-bartowski:latest` (현 OllamaBoss 기본).
- **prompt**: 표준 advice prompt (boss_prompt_for("code") + 동일 user_blob) — 실제 운영 형태.
- **N=3**: 동형 호출 3 회. 첫 호출 = cold (load_duration 포함 가능), 후속 = warm.
- **호출 간 간격**: 즉시 연속 (warm cache 보존).
- **수집**: 각 호출의 6 metadata + 3 파생 metric.

## 3. 측정 stage 답습 (V-1 5 stages 패턴 축약)

| Stage | 작업 |
|-------|------|
| precheck | Ollama daemon 가용 + 모델 존재 확인 |
| warmup | 1 회 호출 (측정 외, cache 가열) |
| measure | N=3 측정 |
| stats | mean / median(p50) / std / min / max |
| report | stdout + raw JSON log |

## 4. 통계 산출

- decode rate / prefill rate / latency 각각 N=3 → mean, p50, std, min, max
- std/mean = coefficient of variation (CoV) — N=3 분산 신뢰도 약함 (참고용 한정)
- M3·M4 결정 *고정* 0건 — 본 cycle = 측정 자료 수집만, *결정* = 별도 cycle

## 5. 출력 형식

stdout:
```
=== MVP-1 트랙 B 측정 ===
모델: qwen3-30b-a3b-instruct-2507-bartowski:latest
N=3, warmup=1

샘플 metadata (ns / tokens):
  run 1: total=... load=... prompt_eval=...×... eval=...×...
  run 2: ...
  run 3: ...

파생 metric:
  decode  (tok/s): mean=X.X p50=X.X std=X.X min=X.X max=X.X
  prefill (tok/s): ...
  latency (s):     ...

[evidence] raw JSON → /tmp/jarvis-v00-boss-measurement.json
```

raw JSON: 각 호출의 6 metadata + 파생 metric + stats 집계.

## 6. 합격 조건

- precheck PASS (Ollama daemon + 모델 가용)
- N=3 모든 호출 성공 (HTTP 200 + metadata 6 필드 모두 존재)
- decode/prefill/latency 통계 산출 성공
- raw JSON log 기록

## 7. 비-scope (DEFER 영구)

- **M3·M4 결정 고정** = 본 cycle 측정 *자료* 만, 결정은 별도 cycle (헌법·아키텍처 변경 적격)
- 다중 모델 비교 (llama3.3 / qwen2.5-coder 등) — 별도 cycle (Provider Liquidity 확장)
- N=10+ 통계 신뢰도 — N=3 한정 (v0.0 evidence 답습, 신뢰도는 후속 cycle)
- prefill warm vs cold 분리 — 별도 cycle
- 동시 요청 throughput — 별도 cycle
- nvidia-smi / NVBandwidth / Nsight 정밀 측정 — 별도 cycle ([[mvp_staged_roadmap]] V-1 답습)
- 측정 자동화 (cron 등) — Layer 2+ 영역

DONE 후 단일 commit + push + PR + memory.
