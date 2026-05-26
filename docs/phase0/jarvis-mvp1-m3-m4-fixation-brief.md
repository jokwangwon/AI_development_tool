# Jarvis MVP-1 M3·M4 결정 *고정* brief — (s) cycle

> **scope**: 이전 합의 (2026-05-23 `9ddec1b`) 의 **M3-D + M4-A 권고 (추가 측정 cycle 후 결정)** → (p)+(r) cycle 7 모델 evidence 확보 → 본 cycle = M3·M4 *결정 권고 고정* 후보.
> **DONE 기준 (본 brief 영역 한정)**: 풀 3+1 합의 권고 보고서 1 건. **결정 *고정* 자체 = 사용자 명시 영역** (본 합의 = 권고 한정).
> **답습**: [[v00-sprint-pending]] (s) + [[provider-liquidity]] 헌법 5조 + 이전 합의 `9ddec1b` BLOCKING 5건 + CLAUDE.md §3 풀 3+1 (아키텍처 의사결정 필수).

---

## 0. 본 합의의 결정 권한 영역

| 영역 | 권한 |
|------|------|
| M3·M4 결정 *권고* | ✅ 본 합의 산출 |
| M3·M4 결정 *고정* (코드/config 변경) | ❌ 사용자 명시 의무 (본 cycle scope 외) |
| 측정 실행 / 빌드 / 모델 재배포 | ❌ 0건 (본 cycle 범위 외) |
| Ollama 데몬 변경 / 모델 unload | ❌ 0건 |
| 헌법 / 아키텍처 본문 수정 | ❌ 0건 |
| Phase α defer-lockdown 변경 | ❌ 0건 |
| Hermes PMO 격상 / Operational Readiness PASS | ❌ 0건 |

본 합의 = brief + 권고 보고서 + 합의 commit/push 한정. 사용자 결정 *후* 별도 cycle 에서 실 코드/config 갱신 가능 (`OllamaBoss(model="...")` default 변경 등).

---

## 1. M3·M4 정의 답습 (이전 합의)

이전 합의 답습 (`docs/phase0/jarvis-mvp1-m3-m4-decision-consensus-entry-brief.md` v1.1):

- **M3** = MVP-1 트랙 B 보스 LLM 런타임/모델 결정 영역
  - M3-A: Ollama 단독 (현 baseline)
  - M3-B: llama.cpp 단독 (대안 런타임)
  - M3-C: Provider Liquidity 유지 (런타임 추상화 → 모델 *교체 가능* 보존)
  - M3-D: 결정 *연기* + 추가 측정 cycle (이전 합의 채택)
  - M3-E: 3rd 후보 카탈로그 (MLC-LLM, llamafile 등)
- **M4** = 보스 응답 속도 threshold 결정 영역
  - M4-A: threshold 결정 *연기* (이전 합의 채택)
  - M4-B: threshold 낮추기 (이전 합의 영구 거부)
  - M4-C: ~~삭제~~ 등 (이전 합의 답습)
  - M4-D: UX wall-clock metric (별도 cycle, NOTE)

본 cycle 입력 = M3-D + M4-A 권고 이후 *추가 측정* 완료 상태.

---

## 2. 새 evidence — 7 모델 통합 ranking ((p) + (r) commit log 답습)

(p) `beac955` + (r) `a20d3ca` 의 N=3 측정 결과:

| 순위 | 모델 | size | family | decode (tok/s) | prefill (tok/s) | latency (s) |
|------|------|------|--------|---------------|------------------|--------------|
| 1 | qwen3-30b-a3b-instruct | 30.5B (MoE 활성 ~3B) | qwen3moe | **15.35** | 4093 | 5.87 |
| 2 | glm-4.7-flash | 29.9B (MoE-lite) | glm4moelite | 10.77 | 2824 | **101.93** ⚠️ |
| 3 | qwen3-coder-next | 79.7B (MoE+SSM) | qwen3next | 9.17 | **70** ⚠️ | 16.80 |
| 4 | qwen2.5-coder | 32.8B (dense Q4) | qwen2 | 4.89 | 1608 | 13.67 |
| 5 | exaone3.5 | 32.0B (dense Q4) | exaone | 4.82 | 1620 | 16.12 |
| 6 | exaone4 | 32.0B (dense Q8) | exaone4 | 3.22 | 1073 | 20.66 |
| 7 | llama3.3 | 70.6B (dense Q4) | llama | 2.32 | 829 | 27.55 |

### 2.1 통계 — 측정 신뢰도

- 측정 N=3 모델당, 모델당 warmup 1 회 (cache 가열)
- 모든 모델 정상 응답 (HTTP 200 + metadata 6 필드)
- CoV (decode std/mean): qwen3-30b-a3b 3.9% (안정), 다른 모델 N=3 한정 신뢰도 약함
- 응답 길이 통제 *0건* — glm-4.7-flash 의 latency 101.9s 가 응답 길이 차이 영향 가능

### 2.2 V-1 답습 비교 (이전 합의 입력)

- V-1 답습: qwen3-coder-next = 7.83 tok/s (decode)
- 본 cycle: qwen3-coder-next = 9.17 tok/s
- 차이 ~17% = warmup 효과 / 환경 차이 (정상 범위)
- ⭐ V-1 답습의 핵심 발견 (F1 roofline 미달, F2 cache 역전, A-진단 한계) 모두 본 cycle evidence 와 정합

---

## 3. 결정 framing — M3·M4 후보 권고 (사용자 결정 입력)

### 3.1 M3 후보 (속도 압도적 → 다른 신호 통합 평가 필요)

| 옵션 | 속도 | Provider Liquidity | 격리 | 한국어 능력 | 기타 |
|------|------|---------------------|------|------------|------|
| **M3-A** (Ollama + qwen3-30b-a3b default) | 1위 압도적 | 약함 (단일 런타임) | OllamaBoss endpoint 하드코딩 보호 | 미측정 | 출처 미상 binary 답습 |
| **M3-C** (Provider Liquidity = 런타임 교체 가능) | model 인자만 변경 | 헌법 5조 최대 | 동일 | 모델 교체 시 변동 | OllamaBoss 외 LlamaCppBoss 등 후속 |
| **M3-E** (3rd 후보 카탈로그) | 미측정 | 측정 후 가능 | 미측정 | 미측정 | MLC-LLM·llamafile = 측정 0건 |

### 3.2 M4 후보 (threshold 결정 영역)

| 옵션 | 의미 | 본 cycle 의미 |
|------|------|------|
| **M4-A** (threshold 결정 연기) | 본 evidence 만으로 threshold 고정 부적합 | 이전 합의 채택, 본 cycle 도 *유지* 권고 가능 |
| M4-B (threshold 낮추기) | 영구 거부 (이전 합의) | anchor effect 답습 차단 |
| M4-D (UX wall-clock metric) | tok/s 가 아닌 응답 완료 시간 기준 | NOTE 격, 별도 cycle |

### 3.3 본 cycle 의 핵심 질문

1. **새 evidence (7 모델) 가 M3-D 연기 → M3-? 고정 권고 자격 충족?**
2. **M4-A 연기 유지 vs M4-D framing 부분 도입?**
3. **응답 길이 통제 (glm-4.7-flash latency 101.9s) 없이 비교 신뢰도 가능?**
4. **출처 미상 Ollama binary (V-1 답습) 가 M3-A 고정 신뢰도 약화?**
5. **Provider Liquidity (헌법 5조) 가 M3-A 직접 고정과 양립 가능?**

---

## 4. 풀 3+1 합의 입력

CLAUDE.md §3 답습 = 아키텍처 의사결정 → **풀 3+1 필수**.

각 Agent 시각:
- **Agent A (구현 분석가)**: 새 evidence 의 신뢰도 / qwen3-30b-a3b 운영 안정성 / 7 모델 통합 가능성 / 응답 길이 통제 부재 영향
- **Agent B (품질·안전성 검증가)**: framing 정직성 / 측정 한계 명시 / Provider Liquidity 본질 / 결정 *고정* 자격 평가 / 거짓 안전감 차단
- **Agent C (대안 탐색가)**: M3-A vs M3-C 비교 / M3-E 추가 측정 가치 / 응답 길이 통제 도입 후보 / threshold 정의 신규 후보 / M4-D UX metric 도입 가능성

각 Agent → 본 brief + 이전 합의 (`9ddec1b`) + ADR-011 (means/ends) + 새 evidence 답습 → 독립 분석.

---

## 5. 합의 산출 — 본 cycle 영역

- 풀 3+1 합의 보고서 1건 (`docs/review/3plus1-consensus-2026-05-26-jarvis-mvp1-m3-m4-fixation.md`)
- 사용자 결정 영역 명시 (본 합의 = 권고 한정)
- 후속 cycle 권고 (사용자 결정 *후* — M3·M4 *고정* / `OllamaBoss` default 갱신 / 다른 측정 / 새 모델 후보 등)

---

## 6. 비-scope (DEFER 영구)

- **M3·M4 결정 *고정* 자체** = 사용자 명시 의무 (본 cycle = 권고 보고서까지)
- 모델 재측정 / 새 모델 다운로드 — 사용자 결정 후 별도 cycle
- `OllamaBoss(model=DEFAULT)` 변경 — 사용자 결정 후 별도 cycle
- LlamaCppBoss / OpenCodeBoss 등 새 런타임 — 별도 brief 적격
- threshold 정의 schema 신규 — 별도 cycle
- 응답 길이 통제 측정 (q) — 본 cycle 권고 영역 (Agent C 검토)
- Operational Readiness PASS / Hermes PMO 격상 — 별도 cycle
- 헌법·아키텍처 본문 변경 — 별도 cycle (헌법 변경 = 풀 3+1 + 사람 게이트)

DONE 후 단일 commit + push + memory.
