# Jarvis (r) 남은 대형 모델 N=3 측정 brief

> **scope**: (p) 4 후보 (30-32B) 측정 → 대형 모델 3 종 (70B+) 추가 측정. M3·M4 결정 *고정* 0건 = 측정 자료 수집만.
> **DONE 기준**: 3 대형 모델 × N=3 = 9 raw 측정 + 비교 표 + raw JSON evidence.
> **답습**: 후속 (r) [[v00-sprint-pending]] + (p) 답습 + [[ceremony-inflation]] 1-agent.

---

## 1. 모델 후보 (3 종, 대형)

| 모델 | 파라미터 | 크기 | family | 비고 |
|------|---------|------|--------|------|
| **llama3.3:70b** | 70.6B (dense) | 39GB | llama | 가장 큰 dense |
| **qwen3-coder-next:latest** | 79.7B (MoE+SSM) | 48GB | qwen3next | V-1 답습 측정 모델 (7.83 tok/s) — 재측정 비교 |
| **exaone4:32b** | 32.0B (dense, Q8) | 31GB | exaone4 | (p) exaone3.5 (Q4) 와 Q level 차이 비교 |

총 디스크 = 118GB 이미 다운로드 됨. 추가 다운로드 0.

## 2. 측정 시나리오

(p) 답습 — `jarvis_v00_multi_model_measurement.py` 의 `--models` 인자로 재사용:

```bash
python examples/jarvis_v00_multi_model_measurement.py \
    --models "llama3.3:70b,qwen3-coder-next:latest,exaone4:32b"
```

각 모델 warmup 1 + measure N=3. 신규 script 0 — 기존 helper + 측정 패턴 완전 동일.

## 3. 예상 elapsed (참고)

- llama3.3:70b: warmup ~120s + measure 3 × ~30s = ~210s
- qwen3-coder-next: warmup ~150s + measure 3 × ~30s = ~240s
- exaone4:32b: warmup ~100s + measure 3 × ~20s = ~160s
- **총 ~10-15분** (Ollama 가 자동 unload/load, 메모리 압박 0)

## 4. 합격 조건

(p) 답습 — 합격 조건 동일:
- 3 모델 모두 precheck PASS
- 각 모델 N=3 valid
- decode > 0
- evidence 기록

## 5. 비교 관심 항목

| 비교 | 신호 |
|------|------|
| llama3.3:70b vs qwen3-30b-a3b | dense 70B vs MoE 활성 3B (~10배 파라미터 차이) |
| qwen3-coder-next vs V-1 답습 | 동일 모델 재측정 (V-1: 7.83 tok/s) → 환경 변화 검증 |
| exaone4 (Q8) vs exaone3.5 (Q4) | Q level 영향 (quantization 비용 vs 품질) |

## 6. 위험 + 완화

| 위험 | 완화 |
|------|------|
| 대형 모델 load 가 메모리 swap 유발 | Ollama 자동 unload 의존, 동시 0 모델 (순차) |
| 측정 시간 길어짐 (>10분) | run_in_background 실행, 알림 대기 |
| 응답 길이 차이 (glm-4.7-flash 답습) | N=3 raw rate 한정 — 응답 길이 통제 = (q) cycle |
| Q8 모델 (exaone4) 가 다른 Q4 와 비교 불공정 | brief §1 명시 (Q level 비교 의도, 같은 모델 family Q4 vs Q8 비교) |

## 7. 비-scope (DEFER 영구)

- **M3·M4 결정 고정** = 측정 자료만, 결정은 별도 cycle
- 응답 길이 통제 — (q) cycle 영역
- N≥10 신뢰도 — 별도 cycle
- cold vs warm 분리 — 별도 cycle
- 모델 응답 품질 평가 (정확성·코딩 능력) — Layer 2+
- nvidia-smi 정밀 측정 — 별도 cycle ([[mvp_staged_roadmap]] V-1 답습)

DONE 후 단일 commit + push + memory.
