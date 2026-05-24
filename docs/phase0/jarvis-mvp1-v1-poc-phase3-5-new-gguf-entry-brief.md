# Jarvis MVP-1 V-1 PoC Phase 3.5 entry brief (v1, new GGUF cycle, 본 4차 세션 후속 (g) 답습)

> **본 brief = Phase 3 carry-over (g) "Phase 3.5 brief (new GGUF) — HF community GGUF (unsloth/bartowski Qwen3-Next-80B-A3B-Q4_K_M) 다운로드 → llama.cpp 재시도" 직접 진입 entry brief v1.** 본 cycle 진입 근거 = 본 세션 4차 entry raw finding (`docs/phase0/v1-poc-raw/phase3/2026-05-25T04-01-phase3-carryover-i-llamacpp-checkout-falsification.md`, `52749ce`) — (i) llama.cpp checkout 자격 falsification 확정 후 (g) 권고 근거 *강화* 답습. 본 brief 자체는 **다운로드·빌드·측정·sudo·Ollama 변경·MVP-1 합의 본문·헌법·ADR·메모리 변경 0건**. 실 변경 = 본 brief 작성 + commit + push 만. 자동 다음 단계 진입 0건 (사용자 명시 의무 답습 영구).

**작성일**: 2026-05-25 (본 세션 4차 entry (i) falsification commit `52749ce` 직후)
**카테고리**: V-1 PoC Phase 3.5 entry brief v1 (Phase 3 carry-over (g), Ollama GGUF 호환성 차단 후 HF community GGUF 직접 다운로드 + llama.cpp 재측정 시도)
**범위**: (1) HF community GGUF source 후보 식별 + 비교 매트릭스 (unsloth vs bartowski) / (2) 다운로드 절차 (egress 격리, sha256 verify, GGUF format 사전 verify) / (3) 측정 절차 (Phase 3 §2.3 답습) / (4) 분기 조건 (성공·차단·error 종류별) / (5) 후속 carry-over

**답습 권위**:
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`) — 본 brief = Phase 3.5 = Phase 3 의 직접 후속 *measurement attempt 재진입* cycle
- Phase 3 합의 (`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-v1-poc-phase3-entry.md`, BLOCKING 7) — R-1~R-7 답습 영구 (특히 R-1 mid-cycle anchor + R-7 egress 격리 + R-12 측정 표준)
- Phase 3 summary (`docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json`) — 본 brief 입력 evidence (blocking finding + R-1 누계 8회 anchor)
- 본 세션 4차 entry raw finding (`docs/phase0/v1-poc-raw/phase3/2026-05-25T04-01-phase3-carryover-i-llamacpp-checkout-falsification.md`) — (i) falsification + (g) 권고 근거 강화 직접 답습
- M3·M4 결정 합의 (`9ddec1b`, 풀 3+1 APPROVE w/ COND BLOCKING 5) — M3·M4 결정 *고정* 자격 미충족 영구 답습
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상) — 본 cycle 머신 변경 자격 평가 영구 모법
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. HF community GGUF source 후보 2 식별 + 비교 매트릭스 (§2)
2. 다운로드 절차 명문 — egress 격리·sha256 verify·GGUF format 사전 verify (§3)
3. 측정 절차 명문 — Phase 3 §2.3 Step 3 답습 + Phase 1 prompt 답습 (§4)
4. 분기 조건 명문 — 성공·format 차단·runtime 에러·tok/s 측정 (§5)
5. 정직성 한계 명문 (§6) — 17+ 항목
6. 차단 조건 명문 (§7) — §0 1:1 매핑
7. 후속 carry-over 매트릭스 (§8)

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 다운로드 / 빌드 / 측정 / sudo 실행** — 본 brief = entry plan only, 실행은 사용자 명시 *후* 별도 단계
2. ❌ **Ollama daemon 상태 변경** — pid 3375 보존 (Phase 3 R-1 anchor 답습 영구)
3. ❌ **`/home/delangi/src/llama.cpp` HEAD `c0c7e147` 변경** — Phase 3 빌드 상태 보존 (rebuild 0건, checkout 0건)
4. ❌ **새 빌드** — Phase 3 빌드 `build/bin/llama-cli` (367MB) 재사용
5. ❌ **MVP-1 합의 본문 자동 정정** — R4 "llama.cpp ↔ Ollama 동급" 본문 변경 0건, format-version 일치 의무 명문은 별도 cycle
6. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding 추가 evidence 만, 본문 변경은 헌법급 별도 cycle (R-9 답습 영구)
7. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구, 본 cycle = 측정 *시도* only
8. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 본 cycle = framing + 측정, runtime backend 코드 0건
9. ❌ **메모리 자동 갱신** — 본 cycle 결과 메모리 등재 자격 = 별도 사용자 명시 의무
10. ❌ **(h)/(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
11. ❌ **본 brief commit 자동 진입** — 작성 후 사용자 승인 *후* commit, 자동 진입 0건
12. ❌ **새 모델 다운로드 시점 = 사용자 명시 *직접* 의무** — 본 cycle 50GB egress + 50GB 디스크 = 비례성 평가 답습

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **본 세션 4차 entry raw finding** (`2026-05-25T04-01-phase3-carryover-i-llamacpp-checkout-falsification.md`, `52749ce`):
  - (i) 진입 자격 *falsification 확정* — `git log --all -S` exhaustive grep 결과 `tn(LLM_TENSOR_SSM_DT, i)` (suffix 0) 호출 commit **0건**
  - Ollama GGUF (`blk.X.ssm_dt` suffix 0) = llama.cpp 와 *분기* 된 별도 conversion 산출물 확정
  - **(g) Phase 3.5 권고 근거 강화** — Ollama GGUF 호환 0건 확정 → 새 GGUF 다운로드 의무 명확
- **Phase 3 summary `next_cycle_recommendations.A`** (`2026-05-24T04-36-phase3-summary.json`):
  - "HF community GGUF (unsloth/bartowski Qwen3-Next-80B-A3B-Q4_K_M) 다운로드 → llama.cpp 재시도. egress ~50GB + 디스크 +50GB. 별도 brief + 사용자 명시."
- **Phase 3 §2.5 분기 발동** (`2026-05-24T04-32-phase3-measure-attempt-blocked.log`):
  - `missing tensor 'blk.0.ssm_dt.bias'` → (iii)(iv) 직접 측정 *0건* 답습 → 본 cycle = 측정 *재진입* 시도

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | HF community GGUF (현행 conversion) 가 llama.cpp `c0c7e147` 와 호환 자격 있는가? | Y/N + tensor name dump 직접 verify |
| **Q2** | 호환 시, Phase 3 §2.3 Step 3 측정 *진입 자격* 충족하는가? | Y/N + tok/s decode 측정 결과 |
| **Q3** | 측정 성공 시, Ollama (간접) vs llama.cpp (직접) 동급 비교 자격 강도는? | tok/s 비교 + framing 정직성 (format 차이 = 측정 변수) |
| **Q4** | F1 가설 (활성 ~3B 정확) + F2 가설 (Ollama 효율성 = format-internal 차이) 의 강화·약화 자격은? | Phase 1+2+3 종합 + 본 cycle 결과 |
| **Q5** | M3·M4 결정 *고정* 자격 변경 evidence 입력 자격은? | (k) 별도 cycle 입력 자격만 (본 cycle 결정 0건) |

### 1.3 본 cycle 범위 한정

- ✅ 단일 모델 (Qwen3-Next-80B-A3B-Instruct-Q4_K_M) — 다른 quant (Q5/Q6/Q8) 0건
- ✅ 단일 measurement cycle — prefill-2k + decode-161tok 2 prompt 답습 (Phase 1 prompt set 직접 답습)
- ✅ HF 공식 또는 community repo 2 후보 비교 (§2.1 매트릭스)
- ❌ Qwen3-30B-A3B 대조군 (= 별도 (h) cycle)
- ❌ advisory wall-clock 측정 (= 별도 (j) cycle)
- ❌ M3·M4 결정 (= 별도 (k) cycle)

---

## 2. 모델 source 후보 매트릭스 (사용자 명시 의무)

### 2.1 후보 비교

| # | repo | quant | 예상 크기 | 본 cycle 진입 자격 |
|---|---|---|---|---|
| **A** | `unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF` | Q4_K_M | ~48GB | 강한 후보 (unsloth = active maintainer, 자체 conversion) |
| **B** | `bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF` | Q4_K_M | ~48GB | 강한 후보 (bartowski = 광범위 community 신뢰) |
| C | `Qwen/Qwen3-Next-80B-A3B-Instruct-GGUF` (공식) | Q4_K_M (또는 K_M-variant) | ~48GB | 후보 (official, 단 release 시점·정합성 별도 verify) |
| D | 직접 conversion (HF safetensors → llama.cpp convert_hf_to_gguf.py) | Q4_K_M | egress ~160GB (safetensors) + conversion ~1~2h | DEFER (비례성 약화, ~160GB egress 부담) |

→ **본 brief 권고** = (A) 또는 (B) 중 사용자 명시 1개 + 디스크/egress 비례성 평가. 디스크 현황 = 331GB free → 48GB 다운로드 후 ~283GB free (74% 사용), 안전 margin.

### 2.2 source 선택 사전 verify 의무 (실 다운로드 *전*)

1. **HuggingFace repo 접근성 verify**: `curl -sI https://huggingface.co/<repo>/resolve/main/<file>.gguf` → HTTP 200/302 확인 (egress 최소)
2. **파일 크기 verify**: `Content-Length` header 추출 → 예상 ~48GB 일치 확인
3. **sha256/etag verify**: HF 의 `lfs.pointer` sha256 또는 etag 추출
4. **README + model card 직접 verify**: tensor naming 명시 (`ssm_dt.bias` 또는 `ssm_dt`), GGUF 버전, base model = Qwen3-Next-80B-A3B-Instruct 확인
5. → 4 항목 통과 시 실 다운로드 진입 자격, 미통과 시 다른 후보 또는 보류

---

## 3. 다운로드 절차 (Phase 3 R-7 격리 답습)

### 3.1 사전 조건 (egress 격리 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot) | `/tmp/phase3-5-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-disk-pre.txt` |
| 4 | Ollama daemon 상태 verify — `sha256sum /proc/3375/exe` (R-1 anchor 9회 추가) | `/tmp/phase3-5-r1-anchor-9x.txt` |
| 5 | huggingface-cli 또는 wget/curl 설치 verify (apt egress 0건 의무, 기설치 우선) | `which huggingface-cli; which wget; which curl` |

### 3.2 다운로드 명령 (사용자 명시 후 실행)

**옵션 (a) huggingface-cli** (권고, 권한 분리 명확):
```bash
# 사전 verify (egress ~수KB)
curl -sI "https://huggingface.co/<REPO>/resolve/main/<FILE>.gguf" | head -5

# 실 다운로드 (~50GB egress, ~10~30분 wall-clock, 네트워크 의존)
huggingface-cli download <REPO> <FILE>.gguf \
    --local-dir /home/delangi/models/phase3-5/ \
    --local-dir-use-symlinks False \
    2>&1 | tee /tmp/phase3-5-download.log
```

**옵션 (b) wget direct** (의존성 최소):
```bash
mkdir -p /home/delangi/models/phase3-5/
wget -c "https://huggingface.co/<REPO>/resolve/main/<FILE>.gguf" \
    -O /home/delangi/models/phase3-5/<FILE>.gguf \
    2>&1 | tee /tmp/phase3-5-download.log
```

### 3.3 다운로드 후 verify

| Step | 명세 | 출력 |
|---|---|---|
| 1 | 파일 크기 verify — `ls -l /home/delangi/models/phase3-5/<FILE>.gguf` vs HF metadata | `/tmp/phase3-5-size-verify.txt` |
| 2 | sha256 verify — `sha256sum <FILE>.gguf` vs HF lfs pointer | `/tmp/phase3-5-sha256.txt` |
| 3 | GGUF tensor name dump — `./build/bin/llama-gguf <FILE>.gguf l` (또는 `gguf_dump.py`) | `/tmp/phase3-5-gguf-dump.log` |
| 4 | tensor name pattern verify — `blk.X.ssm_dt.bias` 존재 확인 (suffix 명시) | `grep "ssm_dt.bias" /tmp/phase3-5-gguf-dump.log` |
| 5 | tensor name pattern verify — `blk.X.ssm_beta_alpha.weight` 존재 (suffix `ba` 가 아닌 `beta_alpha`) | `grep "ssm_beta_alpha" /tmp/phase3-5-gguf-dump.log` |
| 6 | egress baseline post + disk 사용량 post | `/tmp/phase3-5-egress-baseline-post.txt`, `/tmp/phase3-5-disk-post.txt` |

→ Step 4·5 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (format 차단) 발동

---

## 4. 측정 절차 (Phase 3 §2.3 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | Ollama 모델 unload (`/api/generate` + `keep_alive: 0`) — GPU 메모리 0 확인 (R-1 anchor 10회 추가) |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv` (idle 확인) |

### 4.2 측정 명령 (Phase 3 §2.3 Step 3 답습)

```bash
cd /home/delangi/src/llama.cpp

# decode-161tok prompt (Phase 1 답습)
./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt \
    -n 256 \
    --no-display-prompt \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    2>&1 | tee /tmp/phase3-5-measure-decode-161tok.log

# prefill-2k prompt
./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt \
    -n 256 \
    --no-display-prompt \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    2>&1 | tee /tmp/phase3-5-measure-prefill-2k.log
```

### 4.3 측정 항목

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| tok/s decode | `eval time` / `n_tokens` from llama-cli stderr | 단일 cycle 한정, GPU thermal·system load 변수 |
| tok/s prefill | `prompt eval time` / `prompt n_tokens` | 동상 |
| total wall-clock | `total time` | 빌드·로딩·측정 합산, R-17 답습 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점, 정확성 한계 |
| Ollama tok/s 비교 | Phase 1 답습 (cache miss 56.3 mean) | 단일 시점 비교, F1 가설 검증 자격 |

---

## 5. 분기 조건 (Phase 3 §2.5 답습)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | tensor verify 통과 + 측정 완료 (tok/s 실수치 획득) | raw report → F1·F2 가설 입력 → (k) M3·M4 cycle 입력 자격 |
| **B1 (format 차단)** | `missing tensor` error 재발생 | raw report → (g) 자체 falsification → 후보 모델 변경 또는 보류 |
| **B2 (runtime 에러)** | OOM, CUDA error, segfault | raw report → `-ngl` 조정 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | HF 403/429/network timeout | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | 다운로드 중 ENOSPC | 즉시 중단 → 정리 → 디스크 확보 후 재시도 (별도 명시) |
| **B5 (sha256 mismatch)** | 다운로드 파일 sha256 ≠ HF metadata | 즉시 삭제 → 재다운로드 또는 source 변경 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6·R-17 답습)

1. **HF community GGUF = 비공식 fork conversion** — 공식 Qwen 팀 산출물이 아닐 가능성 (단 unsloth/bartowski 모두 active maintainer + 광범위 community 검증)
2. **conversion 차이** = quantization 알고리즘 미세 차이 가능 → Ollama (간접) vs llama.cpp (본 cycle, 직접) tok/s 비교는 *동일 quant scheme* 보장 0
3. **F2 가설 직접 검증 자격 부분** — Ollama 가 더 빠르다면 *format-internal* 차이가 부분 원인일 수 있으나, 본 cycle 은 *서로 다른* GGUF 비교 → 직접 결론 0
4. **R-23 위반 가능성** — 다운로드 ~10~30분 wall-clock 중 다른 활동 발생 가능 (R-17 답습)
5. **egress 비례성** — 50GB egress = 본 프로젝트 단일 cycle 최대 (Phase 1 HF egress ~10GB의 5×) — 비례성 평가 답습
6. **디스크 비례성** — 50GB 디스크 사용 = 82% → 87% 임시 증가 (안전 margin 유지)
7. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습)
8. **GPU thermal throttling 가능성** — 5 분 이상 연속 측정 시 영향, 측정 분리 의무
9. **llama.cpp HEAD `c0c7e147` 고정** — 최신 master 미답습, 단 Phase 3 와 직접 비교 자격 보존
10. **prompt set 답습 정확성 의존** — Phase 1 detokenize 정확성 (`phase1-prompt-decode-161tok.txt` 등) 에 직접 의존
11. **N=1 결과 단정 금지** — 측정 결과는 *후속 cycle 입력* only, 단정 0건 (Phase 3 R-3 framing 답습)
12. **Provider Liquidity finding 강화 자격** — 본 cycle 결과 무관, "다른 GGUF source 도 llama.cpp 호환" 결과조차도 Ollama 와 동급 자격 평가는 별도 cycle
13. **M3 결정 *고정* 자격 무관** — 본 cycle = 측정 *시도* + raw report, M3·M4 결정 자격은 (k) 별도 cycle
14. **MVP-1 합의 R4 본문 정정 자격 무관** — 본 cycle = input only
15. **HF egress = github.com / huggingface.co 의도 외 추가 source 0건 의무** — apt/pip 등 추가 egress 차단 (R-7 격리 답습)
16. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
17. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만, 코드/측정 변경 0 (Phase 3 brief 답습)

---

## 7. 차단 조건 (§0 1:1 매핑 답습)

본 §0 12 항목과 §7 차단 조건은 **1:1 매핑 의무** (Phase 3 R-15 답습 self-consistency).

1. ❌ 본 brief 자체 다운로드 실행 — 본 brief = entry plan only
2. ❌ Ollama daemon 변경 — pid 3375 보존
3. ❌ llama.cpp HEAD 변경 — `c0c7e147` 보존
4. ❌ 새 빌드 — `build/bin/llama-cli` 재사용
5. ❌ MVP-1 합의 본문 자동 정정 — input only
6. ❌ 헌법·ADR 본문 자동 정정 — Provider Liquidity finding 추가 evidence 만
7. ❌ M3·M4 결정 *고정* — (k) 별도 cycle
8. ❌ runtime backend 코드 작성 — framing + 측정 only
9. ❌ 메모리 자동 갱신 — 사용자 명시 의무
10. ❌ (h)/(j)/(k)/(l)/(m)/(n) 자동 진입 — 사용자 명시 의무
11. ❌ brief commit 자동 진입 — 사용자 승인 후
12. ❌ 다운로드 시점 = 사용자 명시 *직접* 의무

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G (성공) | (k) M3·M4 결정 *고정* cycle 입력 자격 강화 + F1/F2 가설 검증 evidence carry-over |
| B1 (format 차단) | (g) 자체 falsification → 다른 source 후보 또는 (h) Qwen3-30B-A3B 대조군 전환 |
| B2 (runtime 에러) | `-ngl` 조정 또는 다른 quant (별도 명시) |
| B3~B5 (network/디스크/sha256) | 정리 후 재시도 또는 보류 (별도 명시) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| (h) Phase 3.5 Qwen3-30B-A3B 대조군 | MEDIUM | 본 cycle 무관 진행 가능 |
| (j) advisory wall-clock 측정 | MEDIUM | 본 cycle 무관 진행 가능 |
| (k) M3·M4 결정 *고정* | DEFER | 본 cycle G 결과 입력 자격, 단 (iii)(iv) 직접 evidence 의무 |
| (l) MVP-1 트랙 B 구현 | DEFER | (k) 통과 의무 답습 영구 |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| Phase 3 summary recommendation C 정정 | LOW | 본 세션 4차 entry raw finding 후속, 별도 cycle |
| (g1-O') / (g1-O) / (P3) / R-S3 gov §1.1 | MEDIUM | 별도 시리즈 답습 |
| (g1-N-3-adr-008+sip+adr-012'') prime-prime | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 (사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief 작성 (본 단계) | 본 brief v1 | 명시 완료 ("네 진행해주세요") |
| (2) brief 승인 + 진행 형태 명시 | 풀 3+1 합의 / 경량 합의 / 합의 생략 직접 실행 / 보류 + source 선택 (unsloth vs bartowski) | **사용자 명시 의무, 다음 단계** |
| (3) (합의 진행 시) 풀 3+1 합의 또는 경량 평가 | Agent A/B/C + Reviewer / 또는 1인 review | 사용자 명시 후 |
| (4) brief v1.1 (합의 진행 시 보강) | BLOCKING verbatim + 정정 흡수 | 합의 진행 후 |
| (5) 다운로드 실행 | §3 절차 답습 | 사용자 명시 *직접* 의무 (50GB egress) |
| (6) verify + 측정 실행 | §3.3 + §4 절차 답습 | 사용자 명시 후 |
| (7) raw report + commit + push | Phase 3 패턴 답습 | 결과 확인 후 |

---

## 9. 본 brief 본 cycle 진입 자체 영구 권위

- 본 brief = Phase 3 carry-over (g) 직접 entry brief (Phase 3 entry brief 패턴 답습)
- 본 cycle 진입 = 본 세션 4차 entry raw finding (`52749ce`) + (g) 권고 근거 강화 직접 답습
- 본 brief 자체 머신 변경 0건 (다운로드/빌드/측정/Ollama 변경/sudo 0건)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 ((10.6-i) 답습 + chain 영구 종결 의무 답습)

---

**본 brief v1 작성 완료** (Phase 3.5 (g) cycle entry plan. 본 cycle 머신 변경 0건. 다음 단계 = 사용자 명시 의무 답습 영구.)
