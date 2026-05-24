# Jarvis MVP-1 V-1 PoC Phase 3.5 entry brief (v1.1, new GGUF cycle, 풀 3+1 합의 APPROVE w/ COND 반영)

> **본 brief v1.1 = Phase 3.5 (g) cycle 의 풀 3+1 합의 (`2dad32a`, APPROVE w/ COND + BLOCKING 11 + 권고 7 + NOTE 11 + Reviewer 단독 격상 R-S1~R-S4 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 11 verbatim 100% 반영 (R-21 답습 영구 의무) / (2) R-S1~R-S4 정정 흡수 / (3) 사용자 명시 (B) bartowski 단일 source 확정 framing / (4) 본문 변경 0 머신 변경 (다운로드/빌드/측정/sudo 0). 본 brief = entry plan only, 실 변경 = 본 brief v1.1 commit + push 만. 자동 다음 단계 진입 0건 (사용자 명시 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5 (g) 풀 3+1 합의 commit `2dad32a` 직후, 본 cycle 단계 (4-a) brief v1.1 보강)
**카테고리**: V-1 PoC Phase 3.5 entry brief v1.1 (Phase 3 carry-over (g), 본 cycle source = bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF Q4_K_M 단일 확정)
**범위**: (1) (B) bartowski 단일 source 다운로드 절차 (egress 격리, sha256 verify, GGUF tensor name 사전 verify, R-1 anchor 4 회 답습) / (2) 측정 절차 (Phase 3 §2.3 답습, decode-161tok + prefill-2k 답습) / (3) 분기 (G·B1~B5, B5 = quarantine + 사용자 명시 분기) / (4) 후속 carry-over

**답습 권위**:
- Phase 3.5 (g) 풀 3+1 합의 (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-v1-poc-phase3-5-new-gguf-entry.md`, commit `2dad32a`, 423줄, BLOCKING 11 + R-S1~R-S4 + 권고 7 + NOTE 11) — **본 brief 의 직접 input 자격 영구**
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`) — Phase 3.5 = Phase 3 의 직접 후속 *measurement attempt 재진입* cycle
- Phase 3 합의 (`docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-v1-poc-phase3-entry.md`, BLOCKING 7) — R-1~R-7 답습 영구 (특히 R-1 mid-cycle anchor + R-7 egress 격리 + R-12 측정 표준 + R-21 BLOCKING verbatim)
- Phase 3 summary (`docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json`)
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`) — Phase 1 측정값 답습 (decode 7.83 ± 0.36, prefill cache miss 58 tok/s)
- 본 세션 4차 entry raw finding ((i) falsification `52749ce`) — (i) 자격 부정 + (g) 권고 강화 직접 답습
- M3·M4 결정 합의 (`9ddec1b`) — M3·M4 결정 *고정* 자격 미충족 영구 답습
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. (B) bartowski 단일 source 다운로드 절차 명문 — egress 격리·sha256 verify·GGUF tensor name 사전 verify (§3) + R-1 anchor 4 회 답습 (Phase 3 entry brief 답습 영구)
2. 측정 절차 명문 — Phase 3 §2.3 Step 3 답습 + Phase 1 prompt 절대 경로 답습 (§4)
3. 분기 조건 명문 — G 성공·B1 format 차단·B2 runtime 에러·B3 network·B4 디스크·B5 quarantine (§5)
4. 정직성 한계 명문 18+ 항목 (§6) — (g) 단독 framing 변수 분리 한계 + Provider Liquidity finding 강화/약화 framing
5. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
6. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구
7. v1 → v1.1 변경 일람 (§9) — BLOCKING 11 + R-S1~R-S4 + 권고 7 흡수 매트릭스 (R-rec-6 답습)

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 다운로드 / 빌드 / 측정 / sudo 실행** — 본 brief = entry plan only
2. ❌ **Ollama daemon 상태 변경** — pid 3375 보존 (R-1 anchor 답습 영구)
3. ❌ **`/home/delangi/src/llama.cpp` HEAD `c0c7e147` 변경** — Phase 3 빌드 상태 보존
4. ❌ **새 빌드** — Phase 3 `build/bin/llama-cli` (367MB) 재사용
5. ❌ **MVP-1 합의 본문 자동 정정** — R4 "llama.cpp ↔ Ollama 동급" input only
6. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
7. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
8. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
9. ❌ **메모리 자동 갱신** — 사용자 명시 의무
10. ❌ **(h)/(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
11. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
12. ❌ **다운로드 시점 = 사용자 명시 *직접* 의무** — ~48~50GB egress + ~48GB 디스크 비례성 답습 (R-11)
13. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입** — chain 영구 종결 의무 답습 영구

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **본 세션 4차 entry raw finding** (`52749ce`, `2026-05-25T04-01-phase3-carryover-i-llamacpp-checkout-falsification.md`):
  - (i) 진입 자격 *falsification 확정* — `git log --all -S` exhaustive grep 결과 `tn(LLM_TENSOR_SSM_DT, i)` (suffix 0) 호출 commit **0건**
  - Ollama GGUF = llama.cpp 와 *분기* 된 별도 conversion 산출물 확정
  - **(g) Phase 3.5 권고 근거 강화** — Ollama GGUF 호환 0건 확정 → 새 GGUF 다운로드 의무 명확
- **Phase 3.5 풀 3+1 합의** (`2dad32a`):
  - APPROVE w/ COND, BLOCKING 11 verbatim 100% 본 brief v1.1 흡수 의무
- **본 cycle 비용**: egress **~48~50GB** (HF lfs `Content-Length` 사전 verify 의무, Phase 3 raw 답습 `ollama_gguf_size_GiB: 48.18` — R-11 답습) + 디스크 **~48GB** 임시 사용

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | bartowski 의 HF community GGUF 가 llama.cpp `c0c7e147` 와 호환 자격 있는가? | Y/N + tensor name dump 직접 verify (§3.3 Step 4·5 grep 결과 verbatim) |
| **Q2** | 호환 시, Phase 3 §2.3 Step 3 측정 *진입 자격* 충족? | Y/N + tok/s decode 측정 결과 |
| **Q3** | 측정 성공 시, Ollama (간접) vs llama.cpp (직접) 동급 비교 자격 강도? | tok/s 비교 + framing 정직성 (format 차이 + conversion 차이 + quant scheme 차이 = 측정 변수) |
| **Q4** | F1 가설 (활성 ~3B) + F2 가설 (Ollama 효율성) 강화·약화 자격? | Phase 1+2+3 종합 + 본 cycle 결과 = *간접* input only (C-H2 답습) |
| **Q5** | M3·M4 결정 *고정* 자격 변경 evidence input 자격? | (k) 별도 cycle 입력 자격만 (본 cycle 결정 0건) |

### 1.3 본 cycle 범위 한정

- ✅ 단일 모델 (Qwen3-Next-80B-A3B-Instruct Q4_K_M)
- ✅ 단일 source (B) bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF (사용자 명시 2026-05-25 확정)
- ✅ 단일 measurement cycle — decode-161tok + prefill-2k 2 prompt (Phase 1 답습)
- ❌ Qwen3-30B-A3B 대조군 = (h) 별도 cycle
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **(g)+(h) 통합 cycle = 본 cycle 외 (사용자 명시 별도 cycle 자격, 비용 ~2× = ~96~100GB egress 비례성 평가 의무, R-5 답습)**
- ❌ 다른 quant (Q5_K_M / IQ4_XS / Q6_K) = 별도 cycle (R-rec-2 carry-over)
- ❌ **명명**: 본 cycle = "Phase 3.5" 단독 호칭 유지 (사용자 명시 추가 시 (h) 진입 시점에 "Phase 3.5-B" 또는 별도 명명 평가, R-rec-7 답습)

---

## 2. 모델 source — (B) bartowski 단일 확정

### 2.1 본 cycle 확정 source (사용자 명시 2026-05-25, R-2 답습)

> **본 cycle source = (B) `bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF` Q4_K_M 단일 확정**. (A)/(C)/(D) = 본 cycle 외 fallback 후보 NOTE 격하 — (A) unsloth = (B) 차단 시 fallback carry-over 명문 (사용자 명시 직접 의무, 자동 진입 0건). (B) 의 `<FILE>.gguf` 정확 파일명 = HF model card 사전 verify 후 결정 (split shards 분기 명문, §2.2 Step 1·4 답습).

| # | repo | quant | 예상 크기 | 본 cycle 자격 |
|---|---|---|---|---|
| **B** | **`bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF`** | **Q4_K_M** | **~48GB** | **✅ 본 cycle 확정 (사용자 명시)** |
| A | `unsloth/Qwen3-Next-80B-A3B-Instruct-GGUF` | Q4_K_M | ~48GB | NOTE: (B) 차단 시 fallback carry-over (사용자 명시 별도) |
| C | `Qwen/Qwen3-Next-80B-A3B-Instruct-GGUF` (공식, release 시점 verify 의무) | Q4_K_M | ~48GB | NOTE: 별도 cycle (사용자 명시) |
| D | 직접 conversion (HF safetensors → llama.cpp convert_hf_to_gguf.py) | Q4_K_M | egress ~160GB + conversion ~1~2h | NOTE: DEFER (비례성, ~160GB egress) |

### 2.2 source 사전 verify 의무 (R-4 답습 — PASS/FAIL framing 금지, grep 결과 verbatim)

1. **HF repo 접근성 verify**: `curl -sI https://huggingface.co/bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF/resolve/main/<FILE>.gguf` → HTTP 200/302 확인 (egress 최소 ~수KB)
2. **파일 크기 verify**: `Content-Length` header 추출 → ~48GB (~48.18 GiB ± HTTP overhead) 일치 확인
3. **sha256/etag verify**: HF API `/api/models/bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF/tree/main` JSON 응답에서 lfs.pointer sha256 또는 etag 추출
4. **README + model card 직접 verify**: tensor naming 명시 (`ssm_dt.bias` 또는 `ssm_dt`, **단언 강도 약화 framing**, (i) raw finding line 158 답습 — "현행 conversion *시사* + 호환 가능성 *강함*, 단 verify 의무"), GGUF 버전, base model = `Qwen3-Next-80B-A3B-Instruct` 확인, split shards 여부
5. → 4 항목 통과 시 실 다운로드 진입 자격, 미통과 시 다른 후보 (사용자 명시 별도) 또는 보류

---

## 3. 다운로드 절차

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습, Phase 3 §3.0 답습)

본 cycle egress = HF download only. **apt install / pip install / git clone 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구 (R-7 격리 답습). 본 cycle 도구 = wget direct 단독 (R-7 답습, §3.1 Step 5 + §3.2 옵션 (a) NOTE 답습).

### 3.1 사전 조건 (egress 격리, R-7 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot) | `/tmp/phase3-5-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-disk-pre.txt` |
| 4 | **R-1 anchor 9회 추가** — `sha256sum /proc/3375/exe` (Phase 1·2·3 누계 8회 + 본 cycle (a) 사전 1회, R-1 회차 9번째) | `/tmp/phase3-5-r1-anchor-9x.txt` |
| 5 | **다운로드 도구 verify — `which huggingface-cli wget curl aria2c`. 2026-05-25 실측 = huggingface-cli/aria2c 미설치, wget/curl 만 존재 확정** (Reviewer raw cross-check, R-7 답습). apt egress 0건 의무 (사용자 명시 의무 답습 영구, 본 cycle 자동 apt install 0건). → 옵션 (a) huggingface-cli 사용 자격 0 → 옵션 (b) wget direct 단독 사용 | `/tmp/phase3-5-tooling-verify.txt` |

### 3.2 다운로드 명령 (사용자 명시 후 실행)

> 🟡 **옵션 (a) `huggingface-cli` = 2026-05-25 실측 미설치 → 본 cycle 사용 자격 0건** (R-7 답습). 사용 시 사전 `pip install --user huggingface_hub[cli]` 또는 apt install 의무 (= 별도 apt/pip egress + 사용자 명시 의무). **본 cycle 권고 = 옵션 (b) wget direct 단독**.

**옵션 (a) huggingface-cli** (본 cycle 미사용, NOTE carry-over):
```bash
# 본 cycle 미설치 → 사용자 명시 후 별도 진입
# (참고용 만)
huggingface-cli download bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF <FILE>.gguf \
    --local-dir /home/delangi/models/phase3-5/ \
    --local-dir-use-symlinks False
```

**옵션 (b) wget direct** (본 cycle 권고):
```bash
mkdir -p /home/delangi/models/phase3-5/
# <FILE>.gguf = HF model card §2.2 Step 4 verify 후 정확 파일명 사용 (split shards 가능성)
wget -c "https://huggingface.co/bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF/resolve/main/<FILE>.gguf" \
    -O /home/delangi/models/phase3-5/<FILE>.gguf \
    2>&1 | tee /tmp/phase3-5-download.log
```

### 3.3 다운로드 후 verify

| Step | 명세 | 출력 |
|---|---|---|
| 1 | 파일 크기 verify — `ls -l /home/delangi/models/phase3-5/<FILE>.gguf` vs HF metadata | `/tmp/phase3-5-size-verify.txt` |
| 2 | sha256 verify — `sha256sum <FILE>.gguf` vs HF lfs pointer (B5 분기 = quarantine, R-6 답습) | `/tmp/phase3-5-sha256.txt` |
| 3 | **GGUF tensor name dump — `./build/bin/llama-gguf <ABS_FILE_PATH>.gguf r 2>&1 \| head -200`** (R-3 답습 — Phase 3 entry brief Step 6.5 답습 의무, `r` = read subcommand, `l` 부재 확정 Reviewer raw cross-check `--help` 직접 실행). 또는 `gguf-dump.py` 동등 사용 | `/tmp/phase3-5-gguf-dump.log` |
| 4 | **tensor name pattern verify — `grep -E '(ssm_dt\.bias\|ssm_dt\s)' /tmp/phase3-5-gguf-dump.log`** (R-4 답습 — grep 결과 verbatim 보고, **PASS/FAIL framing 금지**). 분기 분류: (i) `ssm_dt.bias` 적중 = §4 진입 자격 강한 evidence / (ii) `ssm_dt` (suffix 0) 적중 = §5 B1 (format 차단) 분기 직접 발동 / (iii) 둘 다 부재 = 별도 verify cycle (다른 SSM 변형) | `/tmp/phase3-5-tensor-verify.txt` |
| 5 | **tensor name pattern verify — `grep -E '(ssm_beta_alpha\.weight\|ssm_ba\.weight)' /tmp/phase3-5-gguf-dump.log`** (R-4 답습 — grep 결과 verbatim). 분기 분류: (i) `ssm_beta_alpha.weight` 적중 = (B) bartowski conversion 현행 정합 강한 evidence / (ii) `ssm_ba.weight` (First draft 시기) 적중 = §5 B1 분기 직접 발동 / (iii) 둘 다 부재 = 별도 verify cycle | `/tmp/phase3-5-tensor-verify-ba.txt` |
| 6 | **block_count verify (R-rec-4 답습)** — `grep -E '(qwen3next\.block_count\|llama\.block_count)' /tmp/phase3-5-gguf-dump.log` → 48 (Qwen3-Next-80B-A3B 가정) 일치 확인. `-ngl <값>` 결정. | `/tmp/phase3-5-block-count-verify.txt` |
| 7 | **R-1 anchor 10회 추가 (mid-cycle, R-3 답습)** — 다운로드 후 verify 직전 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 §4 진입 자격, 불일치 시 측정 단계 skip + cycle 일시 정지 + 사용자 보고 | `/tmp/phase3-5-r1-anchor-10x.txt` |
| 8 | egress baseline post + disk 사용량 post | `/tmp/phase3-5-egress-baseline-post.txt`, `/tmp/phase3-5-disk-post.txt` |

→ Step 4·5·6 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (format 차단 또는 별도 verify) 발동

---

## 4. 측정 절차 (Phase 3 §2.3 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | Ollama 모델 unload (`/api/generate` + `keep_alive: 0`) — GPU 메모리 0 확인. **R-1 anchor 11회 추가** (mid-cycle 회차, 측정 *전*, R-3 답습) — `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 측정 진입 자격 |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv` (idle 확인) |
| 4 | llama.cpp HEAD verify — `cd /home/delangi/src/llama.cpp && git rev-parse HEAD` = `c0c7e147...` (Phase 3 빌드 상태 보존 확인) |

### 4.2 측정 명령 (R-9 + R-10 답습 — 절대 경로 + 토큰 수 정직성)

> 🟡 **prompt 파일명 vs 실 토큰 수 격차 (정직성 명문, R-10 답습)**: `phase1-prompt-decode-161tok.txt` 파일명 = Ollama re-tokenize (`prompt_eval_count: 161`) 답습, llama.cpp re-tokenize = **153 tokens** (Phase 3 summary `phase1_prompt_detokenize_executed.detokenized_prompts.decode-161tok.tokens` 답습). 8 tokens 격차 = BOS/EOS/special token 처리 변형. 본 cycle = 동일 prompt text 답습 의무 (파일 내용 일치), tok/s 비교 시 *token 수 차이* 정직성 명문 의무 (분모 token 수 = llama.cpp re-tokenize 결과 사용).

```bash
cd /home/delangi/src/llama.cpp

# decode-161tok prompt (Phase 1 답습, 절대 경로 한국어 큰따옴표 인용, R-9 답습)
./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt" \
    -n 256 \
    --no-display-prompt \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    2>&1 | tee /tmp/phase3-5-measure-decode-161tok.log

# prefill-2k prompt (R-9 답습)
./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt" \
    -n 256 \
    --no-display-prompt \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    2>&1 | tee /tmp/phase3-5-measure-prefill-2k.log
```

### 4.3 측정 항목 (R-8 + R-rec-3 답습)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| tok/s decode | `llama_perf_context_print: eval time = ... / ... tokens / ... tokens per second` from llama-cli stderr | 단일 cycle 한정, GPU thermal·system load 변수 |
| tok/s prefill | `llama_perf_context_print: prompt eval time = ... / ... tokens / ... tokens per second` | 동상 |
| total wall-clock | `llama_perf_context_print: total time` | 빌드·로딩·측정 합산, R-17 답습 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점 |
| **GPU temperature polling (R-rec-3 답습)** | `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` background | R-23 답습 보강, 5분 이상 연속 측정 thermal throttling 정직성 명문 |
| **Ollama tok/s 비교 (decode)** | **Phase 1 답습 (`v1-poc-raw/2026-05-24-phase1-summary.json` line 103) decode mean 7.83 ± 0.36 tok/s** (R-8 답습 — 본 brief v1 의 "56.3 mean" 출처 0건 false value 정정) | 단일 시점 비교, F1 가설 검증 자격 (활성 ~3B 정확), 격차 framing = conversion 차이 변수 미분리 |
| **Ollama tok/s 비교 (prefill cache miss)** | Phase 1 답습 (line 77) 58 tok/s ± 0.27 (R-8 답습 보조) | 본 cycle prefill-2k prompt 적용 시 비교 가능, 단 conversion 차이 변수 미분리 |

**측정 종료 후 R-1 anchor 12회 추가 (R-3 답습)** — 측정 직후 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 (Phase 3 §2.5 답습, R-6 답습 quarantine)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | tensor verify §3.3 Step 4·5·6 통과 + 측정 완료 (tok/s 실수치 획득) | raw report → F1·F2 가설 *간접* input (C-H2 답습) → (k) M3·M4 cycle input 자격 (단 conversion 차이 변수 미해소, 간접 evidence 한정) |
| **B1 (format 차단)** | §3.3 Step 4 (ii) `ssm_dt` suffix 0 또는 Step 5 (ii) `ssm_ba.weight` 적중 또는 측정 시 `missing tensor` error | raw report → (g) 자체 falsification → 후보 모델 변경 또는 (h) Qwen3-30B-A3B 대조군 전환 자격 강화 (변수 분리 강한 input, R-5 답습) |
| **B2 (runtime 에러)** | OOM, CUDA error, segfault | raw report → **`-ngl` 조정 = 사용자 명시 후 별도 측정 단계 (자동 진입 0건)** 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | HF 403/429/network timeout | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | 다운로드 중 ENOSPC | 즉시 중단 → 정리 → 디스크 확보 후 재시도 (별도 명시) |
| **B5 (sha256 mismatch, R-6 답습 quarantine)** | 다운로드 파일 sha256 ≠ HF metadata | **즉시 quarantine 디렉토리 이동** (`mv /home/delangi/models/phase3-5/<FILE>.gguf /home/delangi/models/phase3-5-quarantine/`). **rm 0건 자동 실행 금지** (비례성 답습 영구). raw report → 사용자 명시 후 (i) 부분 write race verify (재다운로드 `-c` continuation) 또는 (ii) HF metadata 기대값 재 verify 또는 (iii) 위조 확정 시 삭제 + 다른 source 진입 — 사용자 명시 분기 의무 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 18 항목, R-5 신규 #18)

1. **HF community GGUF = 비공식 fork conversion**. unsloth/bartowski 모두 active maintainer (단 본 단일 cycle 의 호환 verify 의무 답습, (i) raw finding line 158 답습 — "현행 conversion *시사* + 호환 가능성 *강함*, 단 verify 의무"). 광범위 community 검증 단언 = 본 brief 범위 외 (정직성 한계 명문, R-4 답습)
2. **conversion 차이** = quantization 알고리즘 미세 차이 가능 → Ollama (간접) vs llama.cpp (본 cycle, 직접) tok/s 비교는 *동일 quant scheme* 보장 0
3. **F2 가설 직접 검증 자격 부분** — Ollama 가 더 빠르다면 *format-internal* 차이가 부분 원인일 수 있으나, 본 cycle 은 *서로 다른* GGUF 비교 → 직접 결론 0. C-H2 답습 — F2 *간접 input* 한정
4. **R-23 위반 가능성** — 다운로드 ~10~30분 wall-clock 중 다른 활동 발생 가능 (R-17 답습)
5. **egress 비례성** — **~48~50GB egress = 본 프로젝트 단일 cycle 최대** (Phase 1 HF egress ~10GB 의 4.8~5×, R-11 답습) — 비례성 평가 답습
6. **디스크 비례성** — **~48GB 디스크 사용 = ~82% → ~84.6% 임시 증가** (50GB / 1.9TB ≈ 2.6pp, R-11 + A-rec-2 답습)
7. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습)
8. **GPU thermal throttling 가능성** — 5분 이상 연속 측정 시 영향 (R-rec-3 polling 명문)
9. **llama.cpp HEAD `c0c7e147` 고정** — 최신 master 미답습, Phase 3 와 직접 비교 자격 보존. commit date ≈ 2025-11-28 직후 (PR #16095 ff55414c4 직후) 추정
10. **prompt set 답습 정확성 의존** — Phase 1 detokenize 정확성 (R-10 답습 — 파일명 vs 실 토큰 수 격차 153/161, 8 tokens 격차)
11. **N=1 결과 단정 금지** — 측정 결과 = *후속 cycle input* only (Phase 3 R-3 framing 답습)
12. **Provider Liquidity finding 강화/약화 framing 분리 (C-H5 + R-rec-7 답습)**:
    - 본 cycle G 성공 + tok/s 격차 작음 → MVP-1 R4 "동급" *강화* evidence
    - 본 cycle B1 차단 → MVP-1 R4 *약화* evidence (format-version 일치 의무 강한 input)
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
13. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
14. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
15. **HF egress = github.com / huggingface.co 의도 외 추가 source 0건 의무** — apt/pip/git clone 등 추가 egress 차단 (R-7 격리 답습 + §3.0 거버넌스 답습)
16. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
17. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만, 코드/측정 변경 0
18. **(g) 단독 cycle 변수 분리 한계 (R-5 답습 — C-B1 + Phase 3 합의 R-5 답습)**: 본 cycle 결과 G (성공) 시 = Ollama (간접 측정) vs llama.cpp (직접 측정) tok/s 비교 자격 강도 *약함* (format-version 차이 + conversion 차이 + quant scheme 차이 변수 미분리). B (format 차단) 시 = (g) 자체 falsification + 다른 source 또는 (h) Qwen3-30B-A3B 대조군 전환 자격 강화 (변수 분리 직접 input). **(g)+(h) 통합 cycle = 본 cycle 외 (사용자 명시 별도 cycle, 비용 ~2× = ~96~100GB egress 비례성 평가 의무)**

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 13 항목과 §7 차단 조건은 **1:1 매핑 의무** (Phase 3 R-15 답습).

1. ❌ 본 brief 자체 다운로드 실행
2. ❌ Ollama daemon 변경 (pid 3375 보존)
3. ❌ llama.cpp HEAD 변경 (`c0c7e147` 보존)
4. ❌ 새 빌드 (`build/bin/llama-cli` 재사용)
5. ❌ MVP-1 합의 본문 자동 정정
6. ❌ 헌법·ADR 본문 자동 정정
7. ❌ M3·M4 결정 *고정* ((k) 별도 cycle)
8. ❌ runtime backend 코드 작성 (트랙 B 별도)
9. ❌ 메모리 자동 갱신
10. ❌ (h)/(j)/(k)/(l)/(m)/(n) 자동 진입
11. ❌ brief commit 자동 진입
12. ❌ 다운로드 시점 = 사용자 명시 *직접* 의무 (R-11 비례성 답습)
13. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 (chain 영구 종결 의무 답습 영구)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G (성공) | (k) M3·M4 결정 *고정* cycle 의 *간접* input 자격 강화 (단 conversion 차이 변수 미해소, C-H2 답습) + F1·F2 가설 *간접* evidence carry-over + MVP-1 R4 framing *강화* evidence (별도 cycle) |
| B1 (format 차단) | (g) 자체 falsification → (A) unsloth fallback 또는 (h) Qwen3-30B-A3B 대조군 전환 자격 강화 (변수 분리 강한 input, R-5 답습) + MVP-1 R4 framing *약화* evidence |
| B2 (runtime 에러) | `-ngl` 조정 (사용자 명시 별도) 또는 quant 변경 (별도 cycle) |
| B3~B5 (network/디스크/sha256) | 정리 (B5 = quarantine 보존) 후 재시도 또는 보류 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| (h) Phase 3.5 Qwen3-30B-A3B 대조군 | MEDIUM | 본 cycle 무관 진행 가능, 변수 분리 강화 (R-5 답습) |
| (j) advisory wall-clock 측정 | MEDIUM | 본 cycle 무관 진행 가능 |
| (k) M3·M4 결정 *고정* | DEFER | 본 cycle G input 자격 강화 (단 (iii)(iv) 직접 evidence 의무 답습 영구) |
| (l) MVP-1 트랙 B 구현 | DEFER | (k) 통과 의무 답습 영구 |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| Phase 3 summary recommendation C 정정 | LOW | (i) raw finding 후속, 별도 cycle |
| (g1-O') / (g1-O) / (P3) / R-S3 gov §1.1 | MEDIUM | 별도 시리즈 답습 |
| **(g)+(h) 통합 cycle** | DEFER | 사용자 명시 별도 cycle (~96~100GB egress, 비례성 평가 의무, R-5 답습) |
| **`llama-bench` carry-over (R-rec-1)** | LOW | (j) 또는 별도 정확성 cycle input 자격 |
| **quant 비교 매트릭스 carry-over (R-rec-2)** | LOW | egress 비례성 평가 의무 |
| **Phase 3.5 명명 (R-rec-7)** | LOW | (h) 진입 시점에 "Phase 3.5-B" 또는 별도 명명 평가 |
| **(A) unsloth fallback carry-over (R-2 답습)** | LOW | (B) 차단 시 fallback (사용자 명시 별도) |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 (사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `0867fee` 311줄 | 명시 완료 |
| (2) brief 승인 + 진행 형태 + source 명시 | 풀 3+1 합의 + (B) bartowski | 명시 완료 |
| (3) 풀 3+1 합의 진행 + commit | `2dad32a` 423줄 BLOCKING 11 + R-S1~R-S4 | 명시 완료 |
| **(4-a) brief v1.1 보강 + commit (본 단계)** | BLOCKING 11 verbatim 100% + R-S1~R-S4 흡수 | 진행 중 |
| (5) 다운로드 실행 (~10~30분 wall-clock) | §3.2 옵션 (b) wget direct (R-7 답습) | **사용자 명시 *직접* 의무 (50GB egress)** |
| (6) verify + 측정 실행 (~30~60분 wall-clock) | §3.3 + §4 절차 답습 | 사용자 명시 후 |
| (7) raw report + SESSION + INDEX + commit + push | Phase 3 패턴 답습 | 결과 확인 후 |

---

## 9. v1 → v1.1 변경 일람 (R-rec-6 답습)

| BLOCKING/권고 | brief 정정 위치 | 본문 변경 |
|---|---|---|
| **R-1** R-1 anchor 4 회 | §3.1 Step 4 (9회) / §3.3 신규 Step 7 (10회) / §4.1 Step 1 (11회) / §4.3 종료 anchor (12회) | 회차 4 회 명시 + hash 불일관 시 cycle 일시 정지 분기 |
| **R-2** (B) bartowski 확정 | §2.1 헤더 + 매트릭스 / §3.2 `<REPO>` 고정 | (B) 단일 + (A)/(C)/(D) fallback NOTE |
| **R-3** `llama-gguf l→r` | §3.3 Step 3 | `r` + `head -200` + Phase 3 entry brief Step 6.5 답습 명문 |
| **R-4** R-6 framing 답습 | §6 #1 / §3.3 Step 4·5 | 단언 강도 약화 + grep 결과 verbatim + 3 분기 분류 |
| **R-5** (g) 변수 분리 정직성 | §6 신규 #18 / §1.3 (g)+(h) 통합 carry-over | (g) 단독 자격 약함 명문 |
| **R-6** sha256 mismatch quarantine | §5 B5 | quarantine 이동 + rm 0건 + 사용자 명시 분기 |
| **R-7** huggingface-cli 미설치 | §3.1 Step 5 / §3.2 옵션 (a) NOTE | 실측 미설치 + 옵션 (b) wget 단독 |
| **R-8** 56.3 → 7.83 정정 (R-S1 ⭐⭐⭐) | §4.3 Ollama 비교 항목 | decode 7.83 ± 0.36 + (선택) prefill cache miss 58 |
| **R-9** prompt 절대 경로 (R-S2 ⭐⭐) | §4.2 명령 -f 인자 | 절대 path + 한국어 큰따옴표 인용 |
| **R-10** 161tok vs 153 tokens | §4.2 명령 직전 NOTE | 8 tokens 격차 정직성 + 분모 명문 |
| **R-11** 50GB vs 48GB (R-S4 ⭐) | §1.1 / §6 #5·#6 | ~48~50GB 범위 + 84.6% 정확값 |
| **R-rec-1** `llama-bench` carry-over | §8.2 carry-over | (j) 또는 별도 cycle input 자격 |
| **R-rec-2** quant 비교 | §8.2 carry-over | 별도 cycle 비례성 |
| **R-rec-3** GPU thermal polling | §4.3 신규 행 | `nvidia-smi temperature.gpu` polling |
| **R-rec-4** block_count verify | §3.3 신규 Step 6 | `qwen3next.block_count = 48` verify |
| **R-rec-5** §3.0 신규 | §3 시작 직전 | 의도-외 egress 거버넌스 |
| **R-rec-6** §9 v1→v1.1 일람 | brief 말미 | 본 § |
| **R-rec-7** Phase 3.5 명명 | §1.3 명명 자격 / §8.2 carry-over | "Phase 3.5" 유지, (h) 진입 시점 "Phase 3.5-B" 평가 |

**Reviewer 단독 격상 R-S1~R-S4 답습 영구**:
- R-S1 ⭐⭐⭐ CRITICAL = R-8 (line 203 56.3 → 7.83 정정)
- R-S2 ⭐⭐ HIGH = R-9 (prompt 절대 경로)
- R-S3 ⭐⭐ HIGH = R-3 (llama-gguf l→r + Phase 3 답습 의무)
- R-S4 ⭐ MEDIUM = R-11 (50GB vs 48GB)

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = Phase 3.5 (g) 풀 3+1 합의 (`2dad32a`) BLOCKING 11 verbatim 100% 흡수 + R-S1~R-S4 흡수 + R-rec 7 흡수
- 본 cycle 진입 = 본 세션 4차 entry raw finding (`52749ce`) + (g) 권고 근거 강화 직접 답습
- 본 brief 자체 머신 변경 0건 (다운로드/빌드/측정/Ollama 변경/sudo 0건)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)

---

**본 brief v1.1 작성 완료** (Phase 3.5 (g) cycle entry plan + BLOCKING 11 verbatim 100% 반영 + R-S1~R-S4 흡수 + R-rec 7 흡수 + 사용자 명시 (B) bartowski 확정 framing. 본 cycle 머신 변경 0건. 다음 단계 = 사용자 명시 의무 답습 영구.)
