# Phase 3 carry-over (i) — llama.cpp 이전 commit checkout 자격 평가 read-only 조사 결과

**조사 일시**: 2026-05-25T04:01:31+09:00
**조사자**: 본 세션 (12번째 entry 정리 후, 사용자 명시 "Phase 3 carry-over (g)~(n)" 진입 → "측정 트랙 (i)+(j)" 선택 → "(i) 단독 쪽 단순" 형태 선택)
**진입 근거**: `docs/sessions/SESSION_2026-05-24.md` line 253 "(i) llama.cpp 이전 commit checkout — `.ssm_dt.bias` optional 였던 commit 식별 + 재빌드. ~10분"
**카테고리**: Phase 3 raw artifact 추가 (read-only investigation, 머신 변경 0건, checkout/build 0건)
**clone 경로**: `/home/delangi/src/llama.cpp` (Phase 3 빌드 상태 보존, HEAD = `c0c7e147e7efa6c5858754b47259ba4880f8a906` = `b9297-1-gc0c7e147`)

---

## 0. 본 조사 가 *하는* 것 / *하지 않는* 것

### 하는 것
1. (i) 의 *전제* — "llama.cpp 에 `.ssm_dt.bias` optional 였던 commit 이 존재" — 의 자격 평가
2. `/home/delangi/src/llama.cpp` exhaustive `git log --all -S` raw evidence 기반 판정
3. Ollama GGUF 실제 tensor naming 과 llama.cpp 전체 history 의 mismatch 매트릭스
4. (i) 진입 자격 결론 + Phase 3 summary `next_cycle_recommendations.C` 정정 자격 자료

### 하지 않는 것
1. ❌ checkout — 본 조사 read-only, working tree 변경 0건
2. ❌ rebuild — 빌드 0건
3. ❌ 측정 시도 — Phase 3 §2.3 Step 3 재시도 0건
4. ❌ Ollama daemon 상태 변경 — pid 3375 보존
5. ❌ Phase 3 summary `2026-05-24T04-36-phase3-summary.json` 본문 정정 — 별도 자격 평가
6. ❌ MVP-1 합의 / 헌법 / ADR / brief 본문 정정 — 별도 cycle 의무
7. ❌ Provider Liquidity finding 본문 약화 — 강한 evidence 유지
8. ❌ (g)/(h)/(j)~(n) 자동 진입 — 사용자 명시 의무 답습 영구

---

## 1. (i) 전제 falsification 요약

| 항목 | 결과 |
|---|---|
| `layer.ssm_dt = create_tensor(...)` 가 `"bias"` suffix 없이 호출된 commit | **0건** (`git log --all -p -S 'layer.ssm_dt'` exhaustive) |
| `create_tensor(tn(LLM_TENSOR_SSM_DT, i)` (suffix kind 0) 호출 패턴 | **0건** |
| `LLM_TENSOR_SSM_DT` name 매핑이 `"blk.%d.ssm_dt"` 외 다른 형식 | **0건** (현행) |
| qwen3next.cpp / llama-model.cpp 의 모든 ssm_dt 로딩 | `"bias"` 또는 `"weight"` suffix kind 항상 사용 |
| **결론: (i) 진입 자격** | ❌ **본질적 미충족** — 어느 commit 으로 checkout 해도 `blk.X.ssm_dt` (no suffix) GGUF 호환 불가 |

---

## 2. Raw evidence — qwen3next.cpp 의 ssm_dt 로딩 history

### 2.1 최초 생성 commit (PR merge)
```
ff55414c4 model : Qwen3 Next (#16095)
Date: 2025-11-28 12:02:56 +0100
```

```cpp
layer.ssm_dt = create_tensor(tn(LLM_TENSOR_SSM_DT, "bias", i), { hparams.ssm_dt_rank }, 0);
```
- flag=0 (required)
- `tn(LLM_TENSOR_SSM_DT, "bias", i)` = `"blk." + i + ".ssm_dt" + ".bias"` = `blk.X.ssm_dt.bias`

### 2.2 First draft (PR 의 작업 branch 초기 commit)
```
344331c2b First draft
Date: 2025-09-18 00:21:17 +0200
```

```cpp
layer.ssm_dt = create_tensor(tn(LLM_TENSOR_SSM_DT, "bias", i), { hparams.ssm_dt_rank }, 0);
```
- 동일 코드, 동일 flag=0

### 2.3 전체 history exhaustive grep
```bash
git log --all --oneline -p -S 'layer.ssm_dt' | grep -E '^\+.*layer\.ssm_dt\s*='
```

결과 (sort -u 후 12 unique pattern):
- `layer.ssm_dt = create_tensor(tn(LLM_TENSOR_SSM_DT, "bias", i), ...)` (qwen3next, mamba 일부)
- `layer.ssm_dt = create_tensor(tn(LLM_TENSOR_SSM_DT, "weight", i), ...)` (mamba2, plamo2, granite, nemotronh, kimi-linear)
- `layer.ssm_dt = ml.create_tensor(ctx_split, tn(LLM_TENSOR_SSM_DT, "weight", i), ...)` (구식 API, mamba/falcon-mamba 등)
- `layer.ssm_dt = nullptr;` (architecture 미사용 분기)

**→ `tn(LLM_TENSOR_SSM_DT, i)` (suffix 0) 호출 *0건***

---

## 3. Ollama GGUF tensor naming raw evidence

### 3.1 Ollama GGUF 경로 + 크기 (Phase 3 답습)
- 경로: `/home/delangi/문서/project/category/bootcamp_game/ollama-data/models/blobs/sha256-30e51a7cb1cf1333b9e298b90b4c7790fe2572d8736b002482a0ac96328a2ffb`
- 크기: 48.18 GiB
- 모델: `qwen3-coder-next` (Ollama pull, 정확 origin 추적 별도 cycle)

### 3.2 SSM layer tensor name raw dump (`docs/phase0/v1-poc-raw/phase3/2026-05-24T03-26-phase3-gguf-dump.log` 답습)
```
blk.X.ssm_a              ← (suffix 0)
blk.X.ssm_ba.weight      ← (ba 줄임, .weight 명시)
blk.X.ssm_conv1d.weight
blk.X.ssm_dt             ← (suffix 0, size=128 = ssm_dt_rank)
blk.X.ssm_norm.weight
blk.X.ssm_out.weight
```

### 3.3 llama.cpp 가 *기대* 하는 naming (`src/llama-arch.cpp:398` + qwen3next.cpp:87)
```
blk.X.ssm_a              ← OK 일치
blk.X.ssm_beta_alpha.weight  ← MISMATCH (Ollama 는 ssm_ba.weight)
blk.X.ssm_conv1d.weight  ← OK
blk.X.ssm_dt.bias        ← MISMATCH (Ollama 는 ssm_dt suffix 0)
blk.X.ssm_norm.weight    ← OK
blk.X.ssm_out.weight     ← OK
```

### 3.4 Mismatch 매트릭스
| llama.cpp 기대 | Ollama GGUF | 일치 commit |
|---|---|---|
| `ssm_dt.bias` | `ssm_dt` (suffix 0) | **0건** (전체 history exhaustive) |
| `ssm_beta_alpha.weight` | `ssm_ba.weight` | First draft `344331c2b` 한정 (~70일 window, 2025-09-18 ~ 2025-11-28 merge 전) |

→ 두 mismatch 동시 충족 commit **0건**. 어느 commit 으로 checkout 해도 *최소* `ssm_dt.bias` mismatch 잔존.

---

## 4. ssm_ba ↔ ssm_beta_alpha 부분 일치 evidence (보조 finding)

### 4.1 First draft 의 tensor name 정의
`git show 344331c2b` 의 일부:
```
+    MODEL_TENSOR.SSM_BETA_ALPHA:            "blk.{bid}.ssm_ba",
+            { LLM_TENSOR_SSM_BETA_ALPHA,     "blk.%d.ssm_ba" },
+            layer.ssm_beta_alpha = create_tensor(tn(LLM_TENSOR_SSM_BETA_ALPHA, "weight", i), ...);
```

→ First draft 에서 enum `LLM_TENSOR_SSM_BETA_ALPHA` 가 tensor name `"blk.%d.ssm_ba"` 로 매핑 (변수명 ↔ tensor name 불일치 의도적).

### 4.2 PR merge 의 rename
`ff55414c4` 에서 `"blk.%d.ssm_ba"` → `"blk.%d.ssm_beta_alpha"` 로 일관성 정정.

### 4.3 Ollama GGUF 의 출처 시사
- `ssm_ba.weight` 명명 일치 = First draft 시기 (~9~11월 2025) 의 conversion 사용 강한 시사
- 단 `ssm_dt` (suffix 0) 는 First draft 도 일치하지 않음 → Ollama 가 자체 fork/modified conversion 사용 가능성 강함
- llama.cpp `convert_hf_to_gguf.py` First draft 에는 `.dt_bias` → `.dt_proj.bias` rename 처리 존재, `.dt_bias` → `.ssm_dt` (suffix 제거) 처리 0건

→ Ollama GGUF = llama.cpp 와 *분기* 된 별도 conversion path 산출물 강한 결론

---

## 5. (i) 진입 자격 결론

### 5.1 Phase 3 summary `next_cycle_recommendations.C` 정정 자격
원문 (`2026-05-24T04-36-phase3-summary.json` line "C_llamacpp_older_commit"):
> "llama.cpp .ssm_dt.bias optional 였던 commit checkout + 재빌드. git log 검색 ~10분. 단 측정 의도 (master 본질 비교) 부분 손상"

본 조사 결과:
- "`.ssm_dt.bias` optional 였던 commit" 의 *존재* 자체가 raw git evidence 에 의해 부정
- "git log 검색 ~10분" 의 *예상 결과* = "찾을 수 있다" 라는 함의 자체가 부정
- 단 본 *조사* 자체는 ~10분 내 완료 (예상 비용 정합)

→ Phase 3 summary recommendation matrix 의 C 항목 = **falsified by raw git evidence**. 정정 자격 *후보* (별도 cycle, 자동 정정 0건).

### 5.2 (g)/(h) 권고 강화
- (g) Phase 3.5 (new GGUF, unsloth/bartowski Qwen3-Next-80B-A3B-Q4_K_M) = HF community GGUF, **현행 conversion 사용 강한 시사** → llama.cpp 호환 가능성 강함 (단 verify 의무)
- (h) Qwen3-30B-A3B 대조군 = classical MoE + dense, SSM 미포함 → 본 mismatch 발생 0 자격

본 조사 결과 = (g)/(h) 권고 *근거 강화* (Ollama GGUF 자체가 llama.cpp 호환 0건 확정 → 새 GGUF 다운로드 의무 명확)

### 5.3 Provider Liquidity finding 강화
Phase 3 summary `implication_for_provider_liquidity` 답습:
> "헌법 5조 Provider Liquidity 답습 강도 ↑ — 모델 교체 = GGUF 변환 호환성 의무. llama.cpp ↔ Ollama 동급 비교 = format-version 일치 필수."

본 조사 추가 강화:
- Ollama GGUF = llama.cpp 와 *분기* 된 별도 conversion 산출물 = "llama.cpp ↔ Ollama 동급" 자격이 *format 차원에서* 약화
- MVP-1 합의 R4 "llama.cpp ↔ Ollama 동급" 의 *runtime 비교* 자격 평가 시 **GGUF format-version 일치 의무** 가 사전 조건 (별도 cycle 의무, 본 조사 자체 입력 자격만)

---

## 6. 정직성 한계

1. **clone 범위 한정**: `/home/delangi/src/llama.cpp` clone (`origin = github.com/ggml-org/llama.cpp`) 한정. 다른 fork (Ollama 자체 fork, 비공식 branch 등) 0 확인.
2. **`git log --all -S` exhaustive 의 한계**: `-S` 는 string addition/deletion 검색 — semantic 코드 변경 (e.g., 매크로 정의 변경으로 `tn` 함수 동작 자체 변경) 누락 가능. 다만 본 patterns 의 본질은 string-level 변경이므로 누락 확률 낮음.
3. **`tn` 함수 동작 가정**: 본 조사는 `tn(ENUM, "bias", i)` = `"<arch_format>.bias"` 라는 현행 `tn` 정의 답습. 과거 commit 에서 `tn` 동작 자체가 달랐을 가능성 별도 verify 0.
4. **Ollama GGUF 본문 직접 dump 0**: 본 조사는 Phase 3 `2026-05-24T03-26-phase3-gguf-dump.log` 답습. 새 dump 0건.
5. **conversion 스크립트 추적 부분 한정**: `convert_hf_to_gguf.py` / `qwen.py` 의 `ssm_dt` 명명 처리 전체 history 추적 0건 (`.dt_bias` rename 만 확인).
6. **`-S` 검색의 false negative 가능성**: 변수명 변경 (e.g., `layer.ssm_dt` → `layer.ssm_dt_in`) 등으로 인한 누락. 단 본 cycle 의 범위 (qwen3next.cpp 전체 history) 는 짧음 (Sep 2025 ~ Nov 2025 ~) 으로 누락 risk 낮음.

---

## 7. 본 조사 결과 carry-over (자동 진입 0건, 사용자 명시 의무)

| 후보 | 우선순위 | 비고 |
|---|---|---|
| **(g) Phase 3.5 brief (new GGUF, unsloth/bartowski Qwen3-Next-80B-A3B-Q4_K_M)** | **본 cycle 권고 강화** | egress ~50GB + 디스크 +50GB. 별도 entry brief 의무 (Phase 3 brief 패턴 답습). 본 조사 = (g) 권고 근거 *강화* |
| (h) Phase 3.5 brief (Qwen3-30B-A3B 대조군) | MEDIUM | classical MoE, SSM 미포함 → format mismatch 0 자격. 변수 분리 강화. egress + 디스크 별도 평가 |
| (j) advisory wall-clock 측정 | MEDIUM | (i) 와 독립, Phase 3 결과 무관 진행 가능. advisory config 명세 별도 brief 의무 |
| (k) M3·M4 결정 *고정* 합의 cycle | MEDIUM | Phase 3 직접 측정 0건 답습 → 자격 미충족 유지. (iii)(iv) 직접 evidence 후 별도 평가 |
| (l) MVP-1 트랙 B 구현 진입 | DEFER | (k) 통과 의무 답습 영구 |
| (m) §12 옵션 E (Ollama 위생 정정) | LOW | 본 cycle 무관 (단 본 finding 이 R-1 8회 evidence 추가 강화 가능성) |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 finding 흡수 자격 *후보* (정정 자격 별도 cycle) |
| **Phase 3 summary `2026-05-24T04-36-phase3-summary.json` recommendation C 정정** | LOW | 본 finding 자체 evidence — 별도 자격 평가 cycle, 자동 정정 0건 |

---

## 8. 본 조사 본 세션 후 영구 권위

- 본 finding = (i) 진입 자격 *부정* 의 raw evidence — 향후 어떤 cycle 에서도 (i) "checkout + rebuild" 권고 시 본 raw 답습 의무
- Provider Liquidity finding 강화 evidence — Ollama GGUF format 의 llama.cpp 호환 0건 확정 (단 본 단일 모델 한정, 다른 Ollama 모델 별도 verify)
- Phase 3 summary recommendation matrix C 항목 = *raw evidence falsified* 분류 (별도 자격 평가 cycle 의무)
- 본 조사 자체 머신 변경 0건 — checkout/build/측정 0건, working tree 변경 0건 (본 raw 추가 commit 만 변경)

---

**본 조사 종료** ((i) 진입 자격 read-only 평가 완료, falsification 확정. 머신 변경 0건. checkout/rebuild/측정 0건. `tests/jarvis/` 59 green, `src/jarvis/` 커버리지 100% (불변, 본 조사 무관).)
