# Jarvis MVP-1 V-1 PoC Phase 3.5-B (h) entry brief (v1, Qwen3-30B-A3B 대조군 cycle, 합의 *전* entry plan)

> **본 brief v1 = (h) Phase 3.5-B Qwen3-30B-A3B 대조군 cycle 의 entry plan only.** v1 진입 자격 = (g) Phase 3.5 cycle `b3d4164` 완료 직후 사용자 명시 (h) 직접 선택 + (g) 동형 풀 7단계 진입 + bartowski single source + Q4_K_M quant 답습 4 명확화 완료. 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구). 실 변경 = 본 brief v1 commit + push 만. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] 답습 + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5 (g) cycle 정리 commit `b3d4164` 직후, 본 (h) cycle 단계 (1) brief v1)
**카테고리**: V-1 PoC Phase 3.5-B (h) entry brief v1 (Phase 3 carry-over (h), 본 cycle 핵심 = SSM 변수 분리 대조군 — classical MoE + sparse activation A3B, SSM 미포함)
**범위**: (1) (B) bartowski/Qwen3-30B-A3B-Instruct-GGUF Q4_K_M 단일 source verify + 다운로드 절차 / (2) 측정 절차 ((g) §4 답습, decode + prefill-2k) / (3) 분기 (G·B1~B5) / (4) (g) 결과 대비 비교 framing (SSM 변수 분리 핵심) / (5) 후속 carry-over

**답습 권위**:
- **Phase 3.5 (g) cycle 정리 commit** (`b3d4164`, SESSION 14번째 entry) — 본 (h) 직접 선행 cycle, F-1 (~4.07× 격차) + F-2 (부분 호환 model load) + F-3 (conversion path diversity) + R-1 anchor 12회 + R-7 격리 직접 input 영구
- **Phase 3.5 (g) brief v1.1** (`c4457fa`, 370줄) — 본 brief v1 의 직접 구조 답습 source (§0 1:1 매핑 + §1~§10 구조 동형)
- **Phase 3.5 (g) 풀 3+1 합의** (`2dad32a`, 423줄, BLOCKING 11 + R-S1~R-S4) — 본 (h) v1.1 흡수 후보 BLOCKING 답습 영구
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`) — 본 (h) framing 의 measurement attempt 재진입 답습 영구
- Phase 3 합의 (BLOCKING 7, R-1~R-7) — R-1 mid-cycle anchor + R-7 egress 격리 + R-12 측정 표준 + R-21 BLOCKING verbatim 답습 영구
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`) — qwen3-coder-next decode 7.83 ± 0.36 / prefill cache miss 58 ± 0.27 답습 영구
- (g) raw measurement (`docs/phase0/v1-poc-raw/phase3-5/*`) — bartowski Q4_K_M Qwen3-Next-80B decode 31.5~32.3 / prefill 177.9~971.9 직접 input
- M3·M4 결정 합의 (`9ddec1b`) — M3·M4 결정 *고정* 자격 미충족 영구 답습
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. (B) bartowski single source 다운로드 절차 명문 — egress 격리·sha256 verify·GGUF tensor name 사전 verify (§3) + R-1 anchor 13~16회 답습 ((g) 12회 누계 후속)
2. 측정 절차 명문 — (g) §4 답습 + Phase 1 prompt 절대 경로 답습 (§4)
3. 분기 조건 명문 — G 성공·B1 format 차단·B2 runtime 에러·B3 network·B4 디스크·B5 quarantine (§5)
4. 정직성 한계 명문 18+ 항목 (§6) — (h) 단독 결과 단정 금지 + (g) vs (h) 비교 변수 분리 framing + Provider Liquidity finding 강화/약화 framing
5. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
6. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구
7. (g) 결과 대비 비교 framing 명문 (§9) — SSM 변수 분리 핵심 가치 + 격차 framing 분리

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 다운로드 / 빌드 / 측정 / sudo 실행** — 본 brief = entry plan only, 합의 *전*
2. ❌ **Ollama daemon 상태 변경** — pid 3375 보존 (R-1 anchor 답습 영구, (g) 12회 누계 보존)
3. ❌ **`/home/delangi/src/llama.cpp` HEAD `c0c7e147` 변경** — Phase 3 빌드 상태 보존 (g) 답습
4. ❌ **새 빌드** — Phase 3 `build/bin/llama-cli` (367MB) 재사용 (g) 답습
5. ❌ **MVP-1 합의 본문 자동 정정** — R4 "llama.cpp ↔ Ollama 동급" input only
6. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
7. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
8. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
9. ❌ **메모리 자동 갱신** — 사용자 명시 의무
10. ❌ **(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
11. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
12. ❌ **다운로드 시점 = 사용자 명시 *직접* 의무** — ~18~20GB egress + ~18GB 디스크 비례성 답습 (R-11)
13. ❌ **(g)+(h) 통합 본문 정정** — 본 cycle = (g) 와 *독립* 별개 cycle 단독 진행, (g) brief/합의 본문 변경 0건
14. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입** — chain 영구 종결 의무 답습 영구

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **Phase 3.5 (g) cycle 완료** (`b3d4164`, SESSION 14번째 entry):
  - F-1 ⭐⭐⭐: Ollama vs llama.cpp decode **~4.07×** (llama.cpp 더 빠름) → F2 가설 ('Ollama 효율성') *역방향* 강한 evidence
  - F-2 ⭐⭐⭐: bartowski Q4_K_M = 부분 tensor mismatch (ssm_ba/ssm_conv) 에도 model load + 측정 성공 → llama.cpp fallback 가설 (별도 verify cycle 의무)
  - F-3 ⭐⭐: conversion path diversity (Ollama ≠ bartowski ≠ llama.cpp `c0c7e147`) → Provider Liquidity finding 강화
  - **honesty 한계**: format 차이 + conversion 차이 + quant scheme 차이 + imatrix 영향 + **SSM hybrid 변수** 미분리 (C-H2/C-H3 답습)
  - (g) §8 carry-over 매트릭스 line 485: **"(h) Phase 3.5-B Qwen3-30B-A3B 대조군 cycle = HIGH"** (변수 분리 강화 자격 명문, classical MoE + dense + SSM 미포함 = format mismatch 0 자격)
- **본 cycle 핵심 가치 = SSM 변수 분리**:
  - Qwen3-Next-80B-A3B-Instruct = MoE (512 experts top-10) + **SSM (Mamba) hybrid** (`full_attention_interval: 4` = 48 layers 중 12 full attention + 36 SSM)
  - Qwen3-30B-A3B-Instruct = MoE (128 experts top-8) + classical attention, **SSM 미포함** (~3B activated, ~30B total, classical transformer)
  - 본 (h) cycle = (g) 의 SSM 변수를 제거한 대조군 → (g) F-1 격차 (~4.07×) 가 *SSM 기인* 인지 *classical MoE 자체 기인* 인지 변수 분리 input 자격 강함
- **본 cycle 비용**: egress **~18~20GB** (HF lfs `Content-Length` 사전 verify 의무, Qwen3-30B-A3B Q4_K_M ~18GB 예상, R-11 답습) + 디스크 **~18GB** 임시 사용

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | bartowski 의 Qwen3-30B-A3B-Instruct-GGUF Q4_K_M 가 HF 에 *실재* + llama.cpp `c0c7e147` 와 호환 자격 있는가? | Y/N + repo verify (§2.2) + tensor name dump 직접 verify (§3.3 Step 4·5 grep 결과 verbatim) |
| **Q2** | classical MoE + SSM 미포함 → tensor mismatch 0 자격 강한가? | tensor name dump verbatim — `attn_*` / `ffn_*` / `ffn_*_exps` (MoE) 만 + `ssm_*` 0건 confirm |
| **Q3** | 측정 성공 시, Ollama (간접, qwen2.5-coder:32b dense baseline 답습 가능) vs llama.cpp (직접, Qwen3-30B-A3B Q4_K_M) tok/s 비교 자격 강도? | tok/s 비교 + framing 정직성 (model size 변수 80B vs 30B + training corpus 변수 + conversion 차이 변수 = 측정 변수) |
| **Q4** | (g) F-1 격차 (~4.07×) 가 (h) 에서 *답습* / *약화* / *강화* / *역전* 중 어느 방향? | (g) decode 31.5~32.3 → (h) decode X tok/s 직접 비교 + F-2 (SSM 기인 vs classical MoE 자체 기인) 변수 분리 *간접* input |
| **Q5** | F1 가설 (활성 ~3B 추정) 강화·약화 자격? | A3B 명목 활성 ~3B (Q3 가정) vs 실 tok/s roofline 비교 = *간접* input only (C-H2 답습) |
| **Q6** | M3·M4 결정 *고정* 자격 변경 evidence input 자격? | (k) 별도 cycle 입력 자격만 (본 cycle 결정 0건) |

### 1.3 본 cycle 범위 한정

- ✅ 단일 모델 (Qwen3-30B-A3B-Instruct Q4_K_M)
- ✅ 단일 source (B) bartowski (사용자 명시 2026-05-25 확정, (g) 동형 source 답습 — conversion lineage 변수 통제 강한 자격)
- ✅ 단일 measurement cycle — decode + prefill-2k 2 prompt ((g) 답습, Phase 1 답습)
- ❌ Qwen3-Next-80B-A3B (g) 답습 = 별도 cycle 완료 (변경 0건)
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **(g)+(h) 통합 본문 정정 cycle = 본 cycle 외 (사용자 명시 별도 cycle, (g) brief/합의 본문 변경 0건 답습 영구)**
- ❌ 다른 quant (Q5_K_M / IQ4_XS / Q6_K) = 별도 cycle (R-rec-2 carry-over)
- ❌ unsloth / Qwen 공식 source = (B) 차단 시 fallback 후보 NOTE 격하 (사용자 명시 별도)
- ❌ **명명**: 본 cycle = "Phase 3.5-B" 명명 ((g) brief v1.1 §1.3 R-rec-7 carry-over 답습 — "(h) 진입 시점에 Phase 3.5-B 또는 별도 명명 평가"). 본 brief = "Phase 3.5-B" 채택 (사용자 명시 의무 답습 자격, v1.1 보강 시 확정 또는 정정)

---

## 2. 모델 source — (B) bartowski 단일 확정

### 2.1 본 cycle 확정 source (사용자 명시 2026-05-25 직접 확정, (g) 답습)

> **본 cycle source = (B) `bartowski/Qwen_Qwen3-30B-A3B-Instruct-GGUF` (혹은 동등 repo, §2.2 Step 1 실재 verify 후 확정) Q4_K_M 단일 확정**. (g) (B) source 동형 답습 — conversion lineage 변수 통제 강한 자격 (bartowski 단일 maintainer = Qwen3-Next-80B (g) 와 Qwen3-30B-A3B (h) 동일 conversion 도구·시점 답습 자격 가능, §2.2 Step 4 verify). (A)/(C)/(D) = 본 cycle 외 fallback 후보 NOTE 격하 (사용자 명시 별도, 자동 진입 0건).

| # | repo (가정, §2.2 verify 후 확정) | quant | 예상 크기 | 본 cycle 자격 |
|---|---|---|---|---|
| **B** | **`bartowski/Qwen_Qwen3-30B-A3B-Instruct-GGUF` (또는 `bartowski/Qwen3-30B-A3B-Instruct-GGUF`)** | **Q4_K_M** | **~18GB** | **✅ 본 cycle 확정 (사용자 명시)** |
| A | `unsloth/Qwen3-30B-A3B-Instruct-GGUF` | Q4_K_M | ~18GB | NOTE: (B) 차단 시 fallback carry-over (사용자 명시 별도) |
| C | `Qwen/Qwen3-30B-A3B-Instruct-GGUF` (공식, release 시점 verify 의무) | Q4_K_M | ~18GB | NOTE: 별도 cycle (사용자 명시) |
| D | 직접 conversion (HF safetensors → llama.cpp convert_hf_to_gguf.py) | Q4_K_M | egress ~60GB + conversion ~30~60분 | NOTE: DEFER (비례성, ~60GB egress) |

### 2.2 source 사전 verify 의무 ((g) §2.2 답습 + R-4 답습 framing — PASS/FAIL 금지, grep 결과 verbatim)

1. **HF repo 존재 verify**: `curl -sI https://huggingface.co/bartowski/<REPO>/resolve/main/<FILE>.gguf` → HTTP 200/302 확인. (g) 진입 시점 `Qwen_` prefix 답습 (`bartowski/Qwen_Qwen3-Next-80B-A3B-Instruct-GGUF` 가 실제 repo ID 였음 — (h) 도 동형 변형 가능성 verify 의무)
2. **파일 크기 verify**: `Content-Length` header 추출 → ~18GB 일치 확인
3. **sha256/etag verify**: HF API `/api/models/bartowski/<REPO>/tree/main` JSON 응답에서 lfs.pointer sha256 또는 etag 추출 (multipart upload 시 None 가능, (g) 답습)
4. **README + model card 직접 verify**: tensor naming 명시 (classical MoE confirmation, `ssm_*` 0건 확인), GGUF 버전, base model = `Qwen3-30B-A3B-Instruct` 확인, split shards 여부, **imatrix variant 분리 식별** ((g) F-7 답습)
5. → 4 항목 통과 시 실 다운로드 진입 자격, 미통과 시 다른 후보 (사용자 명시 별도) 또는 보류

---

## 3. 다운로드 절차 ((g) §3 답습)

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습)

본 cycle egress = HF download only. **apt install / pip install / git clone 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구 (R-7 격리 답습). 본 cycle 도구 = wget direct 단독 ((g) §3.2 옵션 (b) 답습, huggingface-cli 미설치 확정).

### 3.1 사전 조건 (egress 격리, R-7 답습, (g) §3.1 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot) | `/tmp/phase3-5-h-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-h-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-h-disk-pre.txt` |
| 4 | **R-1 anchor 13회 추가** — `sha256sum /proc/3375/exe` ((g) 누계 12회 + 본 cycle (h) 사전 1회, 13번째 회차) | `/tmp/phase3-5-h-r1-anchor-13x.txt` |
| 5 | 다운로드 도구 verify — `which wget curl` ((g) 답습, huggingface-cli/aria2c 미설치 확정 답습) | `/tmp/phase3-5-h-tooling-verify.txt` |

### 3.2 다운로드 명령 (사용자 명시 후 실행)

> 🟡 **옵션 (a) `huggingface-cli` = 미설치 (g) 답습 → 본 cycle 사용 자격 0**. 본 cycle 권고 = 옵션 (b) wget direct 단독.

**옵션 (b) wget direct** (본 cycle 권고):
```bash
mkdir -p /home/delangi/models/phase3-5/
# <REPO>/<FILE>.gguf = §2.2 Step 1·4 verify 후 정확 파일명 사용 (split shards 가능성)
wget -c "https://huggingface.co/bartowski/<REPO>/resolve/main/<FILE>.gguf" \
    -O /home/delangi/models/phase3-5/<FILE>.gguf \
    2>&1 | tee /tmp/phase3-5-h-download.log
```

### 3.3 다운로드 후 verify ((g) §3.3 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | 파일 크기 verify — `ls -l` vs HF metadata | `/tmp/phase3-5-h-size-verify.txt` |
| 2 | sha256 verify — `sha256sum` vs HF lfs pointer (B5 분기 = quarantine, R-6 답습) | `/tmp/phase3-5-h-sha256.txt` |
| 3 | **GGUF tensor name dump** — `./build/bin/llama-gguf <ABS_FILE_PATH>.gguf r 2>&1 \| head -200` ((g) R-S3 답습, `r` = read subcommand) | `/tmp/phase3-5-h-gguf-dump.log` |
| 4 | **tensor name pattern verify — classical MoE confirmation (R-4 답습, grep 결과 verbatim)** — `grep -E '(ssm_|mamba_)' /tmp/phase3-5-h-gguf-dump.log` → **0건 적중 = 본 cycle 핵심 가설 confirm (SSM 미포함 classical MoE)**. 적중 시 = 가설 falsification (별도 verify cycle) | `/tmp/phase3-5-h-tensor-ssm-verify.txt` |
| 5 | **MoE tensor name verify (R-rec-4 답습)** — `grep -E '(ffn_gate_exps\|ffn_up_exps\|ffn_down_exps\|attn_q\|attn_k\|attn_v)' /tmp/phase3-5-h-gguf-dump.log` → expert tensor + standard attention tensor 동시 존재 확인. 적중 패턴 verbatim 보고, 부재 시 classical MoE 가설 falsification | `/tmp/phase3-5-h-tensor-moe-verify.txt` |
| 6 | **block_count + expert_count verify (R-rec-4 답습)** — `grep -E '(qwen3\.block_count\|qwen3moe\.block_count\|\.expert_count\|\.expert_used_count)' /tmp/phase3-5-h-gguf-dump.log` → 예상 block_count = 48, expert_count = 128, expert_used_count = 8 (Qwen3-30B-A3B 가정). `-ngl <값>` 결정 | `/tmp/phase3-5-h-block-count-verify.txt` |
| 7 | **R-1 anchor 14회 추가 (mid-cycle, R-3 답습)** — 다운로드 후 verify 직전 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 §4 진입 자격 | `/tmp/phase3-5-h-r1-anchor-14x.txt` |
| 8 | egress baseline post + disk 사용량 post | `/tmp/phase3-5-h-egress-baseline-post.txt`, `/tmp/phase3-5-h-disk-post.txt` |

→ Step 4·5·6 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (format 차단 또는 별도 verify) 발동

---

## 4. 측정 절차 ((g) §4 답습 + Phase 3 §2.3 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | Ollama 모델 unload (`/api/generate` + `keep_alive: 0`) — GPU 메모리 0 확인. **R-1 anchor 15회 추가** (mid-cycle, 측정 *전*) — `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 측정 진입 자격 |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv` (idle 확인) |
| 4 | llama.cpp HEAD verify — `cd /home/delangi/src/llama.cpp && git rev-parse HEAD` = `c0c7e147...` (Phase 3 빌드 상태 보존 확인) |

### 4.2 측정 명령 (R-9 + R-10 답습)

> 🟡 **prompt 파일명 vs 실 토큰 수 격차 정직성 명문 (R-10 답습, (g) §4.2 답습)**: `phase1-prompt-decode-161tok.txt` 파일명 = Ollama re-tokenize 답습, llama.cpp re-tokenize = **153 tokens** 답습 가능 (Qwen3-30B-A3B tokenizer = Qwen3-Next 동일 가능성 사전 verify 의무). 본 cycle = 동일 prompt text 답습 의무 (파일 내용 일치), tok/s 비교 시 *token 수 차이* 정직성 명문 의무 (분모 token 수 = llama.cpp re-tokenize 결과 사용).

> 🟡 **interactive mode 차단 (g) F finding 답습**: llama-cli default = interactive mode, `-no-cnv` flag 의도 미작동 → **`< /dev/null` stdin 차단** + **`-no-cnv` 명시** + **timeout 의무** ((g) F-8 답습). prefill-2k log 6.9GB 누적 위험 → cleanup 의무.

```bash
cd /home/delangi/src/llama.cpp

# decode-161tok prompt (Phase 1 답습, 절대 경로 한국어 큰따옴표 인용)
timeout 300 ./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt" \
    -n 256 \
    --no-display-prompt \
    -no-cnv \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    < /dev/null \
    2>&1 | tee /tmp/phase3-5-h-measure-decode-161tok.log

# prefill-2k prompt
timeout 600 ./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/<FILE>.gguf \
    -f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt" \
    -n 256 \
    --no-display-prompt \
    -no-cnv \
    -ngl 48 \
    -c 8192 \
    --no-warmup \
    --seed 42 \
    < /dev/null \
    2>&1 | tee /tmp/phase3-5-h-measure-prefill-2k.log
```

### 4.3 측정 항목 (R-8 + R-rec-3 답습, (g) §4.3 답습)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| tok/s decode | `[ Prompt: X.X t/s \| Generation: Y.Y t/s ]` perf line 1차 generation 종료 직후 | 단일 cycle 한정, GPU thermal·system load 변수 |
| tok/s prefill | 동상, prefill-2k prompt | 동상 |
| total wall-clock | `llama_perf_context_print: total time` | 빌드·로딩·측정 합산 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점 |
| GPU temperature polling (R-rec-3) | `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` background | 5분 이상 연속 측정 thermal throttling 정직성 명문 |
| **(g) decode 비교 (직접 비교 가능)** | (g) bartowski Qwen3-Next-80B-A3B Q4_K_M decode-161tok generation **32.3 tok/s** / prefill-2k generation **31.5 tok/s** ((g) F-1 답습) | 본 cycle (h) Qwen3-30B-A3B Q4_K_M 직접 비교 — model size 변수 80B vs 30B + SSM 변수 분리 핵심 가치 |
| **(g) prefill 비교** | (g) decode-161tok prompt **177.9 t/s** / prefill-2k prompt **971.9 t/s** ((g) F-1 답습) | 동상 |
| **Phase 1 Ollama 비교 (간접)** | qwen3-coder-next decode 7.83 ± 0.36 (단 다른 모델 SSM hybrid 80B) / qwen2.5-coder:32b dense decode 4.62 ± 0.18 (dense 32B baseline) | **(h) Qwen3-30B-A3B 와 Ollama 동일 모델 0건 답습 영구 — Phase 1 비교 자격 *간접* 한정** |

**측정 종료 후 R-1 anchor 16회 추가 (R-3 답습)** — 측정 직후 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 ((g) §5 답습)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | tensor verify §3.3 Step 4·5·6 통과 + 측정 완료 (tok/s 실수치 획득) | raw report → **(g) vs (h) 격차 비교 framing (§9)** → F-1·F-2·F-3 (SSM 변수 분리) *간접* input → (k) M3·M4 cycle input 자격 (단 model size 변수 미해소, 간접 evidence 한정) |
| **B1 (format 차단)** | §3.3 Step 4 (i) `ssm_*` 적중 (가설 falsification) 또는 Step 5 (ii) MoE tensor 부재 또는 측정 시 `missing tensor` error | raw report → 본 cycle 자체 falsification → 후보 모델 변경 또는 (A) unsloth fallback 자격 강화 |
| **B2 (runtime 에러)** | OOM, CUDA error, segfault | raw report → **`-ngl` 조정 = 사용자 명시 후 별도 측정 단계 (자동 진입 0건)** 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | HF 403/429/network timeout | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | 다운로드 중 ENOSPC | 즉시 중단 → 정리 → 디스크 확보 후 재시도 (별도 명시) |
| **B5 (sha256 mismatch, R-6 quarantine)** | 다운로드 파일 sha256 ≠ HF metadata | **즉시 quarantine 디렉토리 이동** (`mv` 만, **rm 0건 자동 실행 금지** 비례성 답습 영구). raw report → 사용자 명시 분기 의무 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 19 항목, (g) §6 답습 + (h) 본 cycle 신규)

1. **HF community GGUF = 비공식 fork conversion** ((g) #1 답습) — bartowski active maintainer 답습, (g) cycle 검증 결과 (Qwen3-Next-80B 부분 호환에도 model load 성공) 답습 가능성 *시사* 만 (단 본 단일 cycle 의 호환 verify 의무 답습 영구)
2. **conversion 차이** ((g) #2 답습) — quantization 알고리즘 미세 차이 가능
3. **F2 가설 *역방향* 강화 framing 한계** — (g) F-1 격차 (~4.07× llama.cpp 더 빠름) = F2 가설 ('Ollama 효율성') *역방향* 강한 evidence. 본 (h) cycle = 변수 분리 input — SSM 기인 격차 vs classical MoE 자체 격차 분리. 단 **(h) Qwen3-30B-A3B 와 Ollama 동일 모델 0건 답습 영구** → Phase 1 비교 자격 *간접* 한정 (C-H2 답습 강화)
4. **(g) vs (h) 비교 변수 분리 한계 (본 cycle 신규 #4)**:
   - ✅ 통제 변수: conversion lineage (bartowski 동일) + quant (Q4_K_M 동일) + llama.cpp HEAD (`c0c7e147` 동일) + tokenizer family (Qwen) + 측정 도구 (llama-cli 동일) + 측정 prompt (Phase 1 동일)
   - ❌ 미통제 변수: model size (80B vs 30B) + SSM hybrid (포함 vs 미포함) + expert count (512 top-10 vs 128 top-8) + training corpus (시점 + dataset 차이 가능)
   - → (g) F-1 격차 ≠ (h) X 격차 결과 = SSM *또는* model size *또는* expert routing 차이 — 단일 변수 분리 자격 0 (3 변수 동시 변경)
5. **R-23 위반 가능성** ((g) #4 답습) — 다운로드 ~5~10분 wall-clock 중 다른 활동 발생 가능
6. **egress 비례성** — **~18~20GB egress = (g) ~48GB 의 ~38%** (R-11 답습) — 비례성 평가 답습
7. **디스크 비례성** — **~18GB 디스크 사용 = (g) 누적 후 ~85% → ~86% 임시 증가** (18GB / 1.9TB ≈ 0.95pp, R-11 답습)
8. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습)
9. **GPU thermal throttling 가능성** — 5분 이상 연속 측정 시 영향 (R-rec-3 polling 명문)
10. **llama.cpp HEAD `c0c7e147` 고정** — (g) 동일, Phase 3 와 직접 비교 자격 보존
11. **prompt set 답습 정확성 의존** — Phase 1 detokenize 정확성 (R-10 답습 — Qwen3-30B-A3B tokenizer = Qwen3-Next 동일 가능성 사전 verify 의무 추가)
12. **N=1 결과 단정 금지** — 측정 결과 = *후속 cycle input* only (Phase 3 R-3 framing 답습)
13. **Provider Liquidity finding 강화/약화 framing 분리 (C-H5 답습)**:
    - 본 cycle G 성공 + (g) 격차 답습 (~4.07× 유사) → SSM 비기인 시사 → classical MoE = Ollama vs llama.cpp 격차 본질 *강화* evidence
    - 본 cycle G 성공 + (g) 격차 약화 (~1~2× 또는 역전) → SSM 기인 시사 → MVP-1 R4 framing *복잡화* (SSM 한정 차이)
    - 본 cycle B1 차단 → 다른 source 또는 가설 재고
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
14. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
15. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
16. **HF egress = github.com / huggingface.co 의도 외 추가 source 0건 의무**
17. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
18. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만, 코드/측정 변경 0
19. **bartowski Qwen3-30B-A3B-Instruct-GGUF repo *실재 verify* 의무 (본 cycle 신규 #19)** — bartowski 의 Qwen3-Next-80B 답습 자격은 단언 0, repo ID + Q4_K_M variant 실재 §2.2 Step 1 verify 의무 답습 영구. unverified 가정 = (B) fallback trigger 가능성 명문

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 14 항목과 §7 차단 조건은 **1:1 매핑 의무** ((g) R-15 답습).

1. ❌ 본 brief 자체 다운로드 실행
2. ❌ Ollama daemon 변경 (pid 3375 보존)
3. ❌ llama.cpp HEAD 변경 (`c0c7e147` 보존)
4. ❌ 새 빌드 (`build/bin/llama-cli` 재사용)
5. ❌ MVP-1 합의 본문 자동 정정
6. ❌ 헌법·ADR 본문 자동 정정
7. ❌ M3·M4 결정 *고정* ((k) 별도 cycle)
8. ❌ runtime backend 코드 작성 (트랙 B 별도)
9. ❌ 메모리 자동 갱신
10. ❌ (j)/(k)/(l)/(m)/(n) 자동 진입
11. ❌ brief commit 자동 진입
12. ❌ 다운로드 시점 = 사용자 명시 *직접* 의무 (R-11 비례성 답습)
13. ❌ (g)+(h) 통합 본문 정정 ((g) brief/합의 본문 변경 0건)
14. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 (chain 영구 종결 의무 답습 영구)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (g) 격차 답습 (~4.07× 유사) | classical MoE 자체 격차 본질 strong evidence → MVP-1 R4 framing *강화* (별도 cycle) + (k) M3·M4 cycle input 자격 강화 |
| G + (g) 격차 약화 (~1~2×) | SSM 기인 격차 strong evidence → MVP-1 R4 framing *복잡화* (SSM 한정) + (g) F-1 재해석 cycle (별도) |
| G + (g) 격차 역전 (Ollama 빠름) | SSM 기인 다른 방향 → F2 가설 재고 cycle (별도) |
| B1 (format 차단) | 가설 falsification → (A) unsloth fallback 자격 강화 + 가설 재고 |
| B2~B5 | (g) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| MVP-1 합의 R4 framing 강화 evidence cycle | HIGH | (g) F-1 + 본 cycle 결과 종합 input |
| llama.cpp fallback tensor name resolution 검증 cycle | MEDIUM | (g) F-2 답습 read-only |
| (j) advisory wall-clock 측정 | MEDIUM | 자비스 비전 직접 진전 |
| (k) M3·M4 결정 *고정* | DEFER | 변수 분리 강화 input 후 자격 평가 |
| (l) MVP-1 트랙 B 구현 | DEFER | (k) 통과 의무 답습 영구 |
| bartowski conversion 시점 + imatrix 출처 verify cycle | LOW | (g) F-4 답습 |
| Phase 3 summary recommendation C 정정 | LOW | (i) falsification + (g) 성공 답습 |
| 다른 quant 비교 (Q5_K_M / IQ4_XS) cycle | LOW | R-rec-2 답습 |
| (g)+(h) 통합 본문 정정 cycle | DEFER | 사용자 명시 별도 cycle, (g) brief/합의 본문 변경 0건 |
| `llama-bench` carry-over (R-rec-1) | LOW | 측정 표준화 + interactive 차단, (j) 또는 별도 정확성 cycle input 자격 |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| (A) unsloth fallback carry-over (R-2 답습) | LOW | (B) 차단 시 fallback (사용자 명시 별도) |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((g) 동형 풀 7단계 답습, 사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| **(1) brief v1 작성 + commit (본 단계)** | 본 brief v1 (~370줄 예상) entry plan only, 합의 *전* | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | Agent A/B/C 병렬 독립 + Reviewer 통합, BLOCKING X + R-S* + 권고 X + NOTE X | 사용자 명시 후 |
| (3) brief v1.1 보강 + commit | 합의 BLOCKING verbatim 100% + R-S* 흡수 + 권고/NOTE 흡수 | 사용자 명시 후 |
| (4) 다운로드 실행 (~5~10분 wall-clock) | §3.2 옵션 (b) wget direct (R-7 답습) | **사용자 명시 *직접* 의무 (18~20GB egress)** |
| (5) verify + 측정 실행 (~30~60분 wall-clock) | §3.3 + §4 절차 답습 | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (g) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (g) vs (h) 비교 framing (본 cycle 핵심 가치, 정직성 명문)

### 9.1 (g) 측정값 답습 (직접 비교 baseline)

| 항목 | (g) bartowski Qwen3-Next-80B-A3B Q4_K_M | 비고 |
|---|---|---|
| decode-161tok generation tok/s | **32.3** | SSM hybrid 48 layers (12 attention + 36 SSM) |
| decode-161tok prompt tok/s | 177.9 | (153 tokens 분모) |
| prefill-2k generation tok/s | 31.5 | 동상 |
| prefill-2k prompt tok/s | 971.9 | (2001 tokens 분모) |
| 모델 크기 | ~80B total, ~3B activated (top-10 of 512 experts) | MoE + SSM |
| GGUF 크기 | 45.38 GiB | |

### 9.2 (h) 예상 결과 시나리오 (사전 가설 평가 — 단정 0)

| 시나리오 | (h) decode tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: 답습 (~30~35 t/s)** | classical MoE 자체 격차 본질 — SSM 비기인 strong evidence | MVP-1 R4 framing *강화* | F-2 (SSM 기인 다른 방향) 별도 cycle |
| **S2: 강화 (~40~60 t/s)** | classical MoE + small size 추가 advantage | SSM 미포함 으로 인한 격차 + size 변수 미해소 | model size 변수 분리 cycle (~7B 모델 별도) |
| **S3: 약화 (~15~25 t/s)** | SSM 기인 격차 부분 + model size 영향 | (g) F-1 격차 SSM 기인 가설 *부분* support | SSM 한정 차이 framing 별도 cycle |
| **S4: 역전 (Ollama 빠름)** | classical MoE 만으로 Ollama advantage | F2 가설 재고 + 측정 도구 변수 평가 | F2 재고 cycle (별도) |

### 9.3 핵심 정직성 (변수 미분리 명문)

- ❌ **단일 변수 분리 자격 0** — (g) → (h) 변화 3 변수 동시: model size (80B→30B) + SSM (포함→미포함) + expert routing (512 top-10 → 128 top-8)
- ✅ **통제 변수 강함** — conversion lineage / quant / llama.cpp HEAD / tokenizer family / 측정 도구 / prompt 동일
- → **(g)+(h) 단일 trial = SSM 변수 *간접* input only**, 단일 변수 분리는 별도 후속 cycle (~7B classical MoE 또는 80B classical 모델 별도 비교 필요)

---

## 10. 본 brief v1 본 cycle 진입 자체 영구 권위

- 본 brief v1 = (g) cycle 완료 (`b3d4164`) + 사용자 명시 (h) 4 명확화 (진입 형태 = (g) 동형 7단계 / source = bartowski / quant = Q4_K_M / 명명 = Phase 3.5-B) 직후 entry plan
- 본 brief 자체 머신 변경 0건 (다운로드/빌드/측정/Ollama 변경/sudo 0건)
- 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)

---

**본 brief v1 작성 완료** (Phase 3.5-B (h) Qwen3-30B-A3B 대조군 cycle entry plan, (g) 동형 7단계 답습 + SSM 변수 분리 핵심 가치 명문 + bartowski Q4_K_M 단일 source + 비교 framing 4 시나리오 + 정직성 한계 19 항목. 본 cycle 머신 변경 0건. 다음 단계 = 풀 3+1 합의 진행 사용자 명시 의무.)
