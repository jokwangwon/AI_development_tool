# Jarvis MVP-1 V-1 PoC Phase 3.5-B (h) entry brief (v1.1, Qwen3-30B-A3B 대조군 cycle, 풀 3+1 합의 APPROVE w/ COND 반영)

> **본 brief v1.1 = (h) Phase 3.5-B Qwen3-30B-A3B 대조군 cycle entry brief v1 (`a504352`, 382줄) 의 풀 3+1 합의 (`d74d205`, 491줄, APPROVE w/ COND + BLOCKING 13 + R-S1~R-S5 + 권고 12 + NOTE 13 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 13 verbatim 100% 반영 (R-21 답습 영구 의무) / (2) R-S1~R-S5 정정 흡수 12곳 (§2.1 row B + (A) row + §2.1 line 100 + §2.2 Step 1 + §3.2 wget URL + §3.3 Step 2 + Step 4 + Step 5 + Step 6 + §4.3 line 225 + §6 #20 + §6 #21) / (3) 강한 권고 흡수 (R-rec-3 / R-rec-5 / R-rec-9 / R-rec-12) / (4) §11 v1→v1.1 변경 일람 신규 작성 ((g) R-rec-6 답습) / (5) 본문 변경 0 머신 변경 (다운로드/빌드/측정/sudo 0). 본 brief = entry plan only, 실 변경 = 본 brief v1.1 commit + push 만. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-B (h) 풀 3+1 합의 commit `d74d205` 직후, 본 cycle 단계 (3) brief v1.1 보강)
**카테고리**: V-1 PoC Phase 3.5-B (h) entry brief v1.1 (Phase 3 carry-over (h), 본 cycle 핵심 = SSM 변수 분리 대조군 — classical MoE + sparse activation A3B, SSM 미포함)
**범위**: (1) (B) bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF Q4_K_M 단일 source 다운로드 절차 (R-S1 발효, 18.63GB single file) / (2) 측정 절차 ((g) §4 답습, decode + prefill-2k) / (3) 분기 (G·B1~B5) / (4) (g) 결과 대비 비교 framing (SSM 변수 분리 핵심) / (5) 후속 carry-over (h-O Ollama 직접 측정 cycle 신규 HIGH)

**답습 권위**:
- **Phase 3.5-B (h) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-v1-poc-phase3-5-h-qwen3-30b-control-entry.md`, commit `d74d205`, 491줄, APPROVE w/ COND + BLOCKING 13 + R-S1~R-S5 + 권고 12 + NOTE 13 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
- **Phase 3.5 (g) cycle 정리 commit** (`b3d4164`, SESSION 14번째 entry, F-1/F-2/F-3 raw evidence)
- **Phase 3.5 (g) brief v1.1** (`c4457fa`, 370줄) — 구조 답습 source 영구
- **Phase 3.5 (g) 풀 3+1 합의** (`2dad32a`, 423줄, BLOCKING 11 + R-S1~R-S4)
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`)
- Phase 3 합의 (BLOCKING 7, R-1~R-7 답습 영구)
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`)
- (g) raw measurement (`docs/phase0/v1-poc-raw/phase3-5/*`) — 20 files raw evidence
- M3·M4 결정 합의 (`9ddec1b`)
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter` / `project_mvp_staged_roadmap` (R-rec-11 답습)

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. (B) bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF Q4_K_M single file (18.63GB) 다운로드 절차 명문 — egress 격리·sha256 verify·GGUF tensor name 사전 verify (§3) + R-1 anchor 13~16회 답습
2. 측정 절차 명문 — (g) §4 답습 + Phase 1 prompt 절대 경로 답습 (§4)
3. 분기 조건 명문 — G 성공·B1 format 차단·B2 runtime 에러·B3 network·B4 디스크·B5 quarantine (§5)
4. 정직성 한계 명문 21 항목 (§6) — (h) 단독 결과 단정 금지 + (g) vs (h) 비교 변수 분리 framing + Provider Liquidity finding 강화/약화 framing + sha256 multipart upload 한계 (#20) + bartowski conversion 시점 ~3~4개월 격차 (#21)
5. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
6. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구 + **(h-O) Ollama 직접 측정 cycle 신규 HIGH carry-over** (R-S1 발효)
7. (g) 결과 대비 비교 framing 명문 (§9) — SSM 변수 분리 핵심 가치 + 격차 framing 분리 + 시나리오 7 (S1~S7)
8. v1 → v1.1 변경 일람 (§11) — BLOCKING 13 + R-S 5 + 권고 12 흡수 매트릭스 ((g) R-rec-6 답습)

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 다운로드 / 빌드 / 측정 / sudo 실행** — 본 brief = entry plan only
2. ❌ **Ollama daemon 상태 변경** — pid 3375 보존 (R-1 anchor 답습 영구, (g) 12회 누계 보존)
3. ❌ **`/home/delangi/src/llama.cpp` HEAD `c0c7e147` 변경** — Phase 3 빌드 상태 보존 (g) 답습
4. ❌ **새 빌드** — Phase 3 `build/bin/llama-cli` (367MB) 재사용 (g) 답습
5. ❌ **MVP-1 합의 본문 자동 정정** — R4 "llama.cpp ↔ Ollama 동급" input only
6. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
7. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
8. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
9. ❌ **메모리 자동 갱신** — 사용자 명시 의무
10. ❌ **(h-O)/(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
11. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
12. ❌ **다운로드 시점 = 사용자 명시 *직접* 의무** — ~18.63GB egress + ~18.63GB 디스크 비례성 답습 (R-11)
13. ❌ **(g)+(h) 통합 본문 정정** — 본 cycle = (g) 와 *독립* 별개 cycle 단독 진행, (g) brief/합의 본문 변경 0건 ((g)+(h) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle, N-12 답습)
14. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입** — chain 영구 종결 의무 답습 영구

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **Phase 3.5 (g) cycle 완료** (`b3d4164`, SESSION 14번째 entry):
  - F-1 ⭐⭐⭐: Ollama vs llama.cpp decode **~4.07×** (llama.cpp 더 빠름) → F2 가설 ('Ollama 효율성') *역방향* 강한 evidence
  - F-2 ⭐⭐⭐: bartowski Q4_K_M = 부분 tensor mismatch (ssm_ba/ssm_conv) 에도 model load + 측정 성공 → llama.cpp **graceful tensor name resolution / fallback 가설** (별도 verify cycle 의무, R-S3 답습)
  - F-3 ⭐⭐: conversion path diversity (Ollama ≠ bartowski ≠ llama.cpp `c0c7e147`) → Provider Liquidity finding 강화
  - **honesty 한계**: format 차이 + conversion 차이 + quant scheme 차이 + imatrix 영향 + **SSM hybrid 변수** 미분리 (C-H2/C-H3 답습)
  - (g) §8 carry-over 매트릭스 line 485: **"(h) Phase 3.5-B Qwen3-30B-A3B 대조군 cycle = HIGH"** (변수 분리 강화 자격 명문, classical MoE + dense + SSM 미포함 = format mismatch 0 자격)
- **본 cycle 핵심 가치 = SSM 변수 분리**:
  - Qwen3-Next-80B-A3B-Instruct = MoE (512 experts top-10) + **SSM (Mamba) hybrid** (`full_attention_interval: 4` = 48 layers 중 12 full attention + 36 SSM)
  - Qwen3-30B-A3B-Instruct-2507 = MoE (128 experts top-8) + classical attention, **SSM 미포함** (~3.3B activated, ~30.5B total, classical transformer, R-S1 raw verify)
  - 본 (h) cycle = (g) 의 SSM 변수를 제거한 대조군 → (g) F-1 격차 (~4.07×) 가 *SSM 기인* 인지 *classical MoE 자체 기인* 인지 변수 분리 input 자격 강함
- **본 cycle 비용**: egress **~18.63GB** (HF 직접 verify, R-S1 답습) + 디스크 **~18.63GB** 임시 사용

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF Q4_K_M 가 llama.cpp `c0c7e147` 와 호환 자격 있는가? | Y/N + tensor name dump 직접 verify (§3.3 Step 4·5 grep 결과 verbatim) |
| **Q2** | classical MoE + SSM 미포함 → tensor mismatch 0 자격 강한가? | tensor name dump verbatim — `attn_*` / `ffn_*` / `ffn_*_exps` (MoE) 만 + `ssm_*` 0건 confirm (R-S3 답습 — falsification 단정 금지) |
| **Q3** | 측정 성공 시, Ollama 동일 모델 (`qwen3:30b-a3b-instruct-2507-q4_K_M` 실재 ✓, R-S1) vs llama.cpp (직접) tok/s 비교 자격 강도? | 본 (h) cycle = llama.cpp 직접 측정 한정 + Ollama 직접 측정 = 별도 cycle 자격 평가 ((h-O) HIGH carry-over) |
| **Q4** | (g) F-1 격차 (~4.07×) 가 (h) 에서 *답습* / *약화* / *강화* / *역전* 중 어느 방향? | (g) decode 31.5~32.3 → (h) decode X tok/s 직접 비교 + F-2 (SSM 기인 vs classical MoE 자체 기인) 변수 분리 *간접* input (단 4 변수 동시 변경 → 단정 자격 strict single-variable cycle 의무) |
| **Q5** | F1 가설 (활성 ~3B 추정) 강화·약화 자격? | A3B 명목 활성 ~3.3B (raw verify 확정) vs 실 tok/s roofline 비교 = *간접* input only (C-H2 답습) |
| **Q6** | M3·M4 결정 *고정* 자격 변경 evidence input 자격? | (k) 별도 cycle 입력 자격만 (본 cycle 결정 0건) |

### 1.3 본 cycle 범위 한정 (R-rec-7 답습 — 독립 cycle + Phase 3.5 sub-cycle framing 통합)

- ✅ 단일 모델 (Qwen3-30B-A3B-Instruct-2507 Q4_K_M)
- ✅ 단일 source (B) **bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF** (사용자 명시 2026-05-25 + R-S1 raw verify 확정)
- ✅ 단일 measurement cycle — decode + prefill-2k 2 prompt ((g) 답습, Phase 1 답습)
- ✅ 명명 = "Phase 3.5-B" 채택 — **독립 cycle 단독 진행 + (g) 와 동일 phase 하위 sub-명명, (g) brief/합의 본문 변경 0건** 통합 framing (R-rec-7 답습)
- ❌ Qwen3-Next-80B-A3B (g) 답습 = 별도 cycle 완료 (변경 0건)
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **Ollama 직접 측정 = (h-O) 별도 cycle 신규 HIGH carry-over (R-S1 발효)** — 본 cycle 은 llama.cpp 직접 측정 한정
- ❌ **(g)+(h) 통합 본문 정정 cycle = 본 cycle 외** ((g) brief/합의 본문 변경 0건 답습 영구)
- ❌ **(g)+(h) 통합 *분석* cycle** ≠ 통합 *본문 정정* cycle = 별도 차원 carry-over (N-12 답습)
- ❌ 다른 quant (Q5_K_M / IQ4_XS / Q6_K) = 별도 cycle (R-rec-2 carry-over)
- ❌ unsloth / Qwen 공식 source = (B) 차단 시 fallback 후보 NOTE 격하

---

## 2. 모델 source — (B) bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF 단일 확정 (R-S1 발효)

### 2.1 본 cycle 확정 source (사용자 명시 2026-05-25 + 풀 3+1 합의 R-S1 raw verify 직접 확정)

> **본 cycle source = (B) `bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF` Q4_K_M 단일 확정** (Agent C WebFetch 직접 verify 2025-07-28 created, 7,009 downloads, 18.63GB single file split:false, qwen3moe arch, 30.5B total / 3.3B activated, 128 experts top-8, R-S1 ⭐⭐⭐ CRITICAL 발효). 본 v1.1 = R-S1 흡수 — brief v1 가정 두 후보 (`bartowski/Qwen_Qwen3-30B-A3B-Instruct-GGUF` + `bartowski/Qwen3-30B-A3B-Instruct-GGUF`) 모두 HF 실재 0건 확정, "**-Instruct-2507-**" 날짜 suffix 누락 정정. (A)/(C)/(D) = 본 cycle 외 fallback 후보 NOTE 격하 (사용자 명시 별도, 자동 진입 0건).

| # | repo (R-S1 raw verify 확정) | quant | 실 크기 (raw verify) | 본 cycle 자격 |
|---|---|---|---|---|
| **B** | **`bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF`** | **Q4_K_M** | **18.63GB single file (split:false)** | **✅ 본 cycle 확정 (사용자 명시 + R-S1 raw verify)** |
| A | `unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF` (Agent C WebFetch verify) | Q4_K_M | 18.6GB single | NOTE: (B) 차단 시 fallback carry-over (사용자 명시 별도). **Unsloth Dynamic 2.0 quantization 사용** = bartowski 와 quant 알고리즘 다름 가능성, conversion 변수 통제 자격 약화 (N-11 답습) |
| C | `Qwen/Qwen3-30B-A3B-Instruct-2507-GGUF` (공식, Agent C WebFetch verify 0건 = 실재 자격 불명) | Q4_K_M | 미verify | NOTE: 별도 cycle (사용자 명시 + 직접 verify 의무, N-3 답습) |
| D | 직접 conversion (HF safetensors → llama.cpp convert_hf_to_gguf.py) | Q4_K_M | egress ~60GB + conversion ~30~60분 | NOTE: DEFER (비례성, ~60GB egress = 본 cycle 18.63GB 의 3.2×) |

### 2.1.1 bartowski 동일 maintainer 변수 통제 자격 (R-S5 정정 — 부분 통제 약화 framing)

bartowski 동일 maintainer = conversion lineage **부분 통제** 자격, 단 (g) Qwen3-Next-80B-A3B-Instruct-GGUF createdAt ~2025-11~12 vs (h) Qwen3-30B-A3B-Instruct-2507-GGUF createdAt 2025-07-28 = **~3~4개월 격차** = convert_hf_to_gguf.py + llama.cpp HEAD + imatrix 알고리즘 version 변수 미통제 가능성 명문 (R-S5 발효 + N-11 답습). §2.2 Step 4 model card + conversion 시점 + 도구 version 사전 verify 의무 답습 영구.

### 2.2 source 사전 verify 의무 (R-4 답습 — PASS/FAIL framing 금지, grep 결과 verbatim)

1. **HF repo 존재 verify**: `curl -sI https://huggingface.co/bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF/resolve/main/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` → HTTP 200/302 확인. (R-S1 raw verify 답습 — Qwen_ prefix + Instruct-2507 suffix 정확 form)
2. **파일 크기 verify**: `Content-Length` header 추출 → ~18.63GB / 20,003,495,872 bytes 일치 확인 (R-S1 raw verify 답습)
3. **sha256/etag verify**: HF API `/api/models/bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF/tree/main` JSON 응답에서 lfs.pointer sha256 또는 etag 추출. **(g) F finding 답습 — multipart upload 시 HF API `lfs.sha256 = null` 가능성 강함** (Q4_K_M ~18.63GB 도 multipart 가능성 ≥ 50%, R-S4 발효). 대체 verify = `Content-Length + ETag + GGUF metadata`. lfs.sha256 None 시 B5 quarantine 분기 trigger 자격 0 = 정직성 한계 명문 (§6 #20 답습)
4. **README + model card 직접 verify**: tensor naming 명시 (classical MoE confirmation, `ssm_*` 0건 확인), GGUF 버전, base model = `Qwen3-30B-A3B-Instruct-2507` 확인, split shards 여부 (R-S1 verify = split:false 확정), **imatrix variant 분리 식별** ((g) `additional_findings_during_phase3_5` line 205~208 답습, R-rec-4 정정), **conversion 시점 + 도구 version** ((R-S5 + N-11 답습) — Unsloth Dynamic 2.0 vs bartowski 알고리즘 차이 식별 의무)
5. → 4 항목 통과 시 실 다운로드 진입 자격, 미통과 시 다른 후보 (사용자 명시 별도) 또는 보류

---

## 3. 다운로드 절차 ((g) §3 답습)

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습)

본 cycle egress = HF download only. **apt install / pip install / git clone 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구 (R-7 격리 답습). 본 cycle 도구 = wget direct 단독 ((g) §3.2 옵션 (b) 답습, huggingface-cli 미설치 확정). **본 cycle sudo 사용 = §3.1 Step 1 단 1회 한정** (`sudo ss -tan state established` snapshot), 사용자 명시 임시 비밀번호 의무 답습 ((g) `sudo_authorization` 답습, R-9 발효).

### 3.0.1 (g) Q4_K_M GGUF 보존 정책 사용자 명시 의무 (R-13 발효)

(g) `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` (45.38 GiB) 보존 / cleanup 사용자 명시 의무 — 보존 시 디스크 ~86% + (h) 18.63GB → ~87%, cleanup 시 ~83% + (h) 18.63GB → ~84%. **cleanup = `rm` 자동 실행 0건 (비례 보안 답습)**. 사용자 명시 후 분기 의무.

### 3.1 사전 조건 (egress 격리, R-7 답습, (g) §3.1 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot, 본 cycle sudo 단 1회 한정, 사용자 명시 임시 비밀번호 의무 답습) | `/tmp/phase3-5-h-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-h-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) — (g) Q4_K_M 보존 / cleanup 명시 후 baseline | `/tmp/phase3-5-h-disk-pre.txt` |
| 4 | **R-1 anchor 13회 추가** — `sha256sum /proc/3375/exe` ((g) 누계 12회 + 본 cycle (h) 사전 1회, 13번째 회차, hash baseline = `ce95c47...8877b10` 일관 답습) | `/tmp/phase3-5-h-r1-anchor-13x.txt` |
| 5 | 다운로드 도구 verify — `which wget curl` ((g) 답습, huggingface-cli/aria2c 미설치 확정 답습) | `/tmp/phase3-5-h-tooling-verify.txt` |

### 3.2 다운로드 명령 (사용자 명시 후 실행, R-S1 발효 — placeholder 0건)

> 🟡 **옵션 (a) `huggingface-cli` = 미설치 (g) 답습 → 본 cycle 사용 자격 0**. 본 cycle 권고 = 옵션 (b) wget direct 단독.

**옵션 (b) wget direct** (본 cycle 권고, R-S1 발효 — `<REPO>` placeholder 0건):
```bash
mkdir -p /home/delangi/models/phase3-5/
# R-S1 raw verify 확정 = bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF Q4_K_M single file split:false
wget -c "https://huggingface.co/bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF/resolve/main/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf" \
    -O /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
    2>&1 | tee /tmp/phase3-5-h-download.log
```

**예상 시간**: (R-6 발효) 18.63GB / 26.4 MB/s ≈ **~11.8분** ((g) avg_speed 답습 scaling, 범위 ~10~15분).

### 3.3 다운로드 후 verify ((g) §3.3 답습 + R-S2/R-S3/R-S4 정정)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | 파일 크기 verify — `ls -l /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` vs HF metadata (18.63GB / 20,003,495,872 bytes) | `/tmp/phase3-5-h-size-verify.txt` |
| 2 | **sha256 verify (R-S4 발효 정직성 명문)** — `sha256sum vs HF lfs pointer`. **(g) F finding 답습 — HF API lfs.sha256 = null 가능 (multipart upload, Q4_K_M ~18.63GB 도 multipart 가능성 ≥ 50%)**. 대체 verify = `Content-Length + ETag + GGUF metadata`. lfs.sha256 None 시 B5 quarantine 분기 trigger 자격 0 = 정직성 한계 명문 (§6 #20 답습) | `/tmp/phase3-5-h-sha256.txt` |
| 3 | **GGUF tensor name dump** — `./build/bin/llama-gguf <ABS_FILE_PATH>.gguf r 2>&1 \| head -200` ((g) R-S3 답습, `r` = read subcommand, `--help` 직접 verify 확정) | `/tmp/phase3-5-h-gguf-dump.log` |
| 4 | **tensor name pattern verify — classical MoE 가설 평가 (R-4 답습 + R-S3 발효 약화 framing, grep 결과 verbatim)** — `grep -E '(ssm_|mamba_)' /tmp/phase3-5-h-gguf-dump.log` → **0건 적중 = 가설 답습 강한 evidence (단 verify 의무 보존, 다른 SSM 변형명 가능성 별도)**. 적중 시 = §5 B1 분기 trigger 자격 평가 (단 (g) F-2 graceful resolution 답습 시 model load 자체 부정 0건 가능성 명문). grep 결과 verbatim 보고 후 별도 분기 평가 | `/tmp/phase3-5-h-tensor-ssm-verify.txt` |
| 5 | **MoE + attention tensor name verify (R-S2 + R-S3 발효, grep 패턴 광범위화)** — `grep -E '(ffn_gate_exps\|ffn_up_exps\|ffn_down_exps\|attn_qkv\|attn_q\|attn_k\|attn_v\|attn_q_norm\|attn_k_norm)' /tmp/phase3-5-h-gguf-dump.log` → expert tensor + standard attention tensor (combined `attn_qkv` 또는 split `attn_q/attn_k/attn_v` 어느 쪽인지 사전 unknown — 양 패턴 모두 grep 의무, (g) gguf-dump line 61/117 raw verify — Qwen3-Next 는 combined+split 혼재). MoE tensor 부재 시 = §5 B1 분기 자격 평가 (단 (g) F-2 답습 = 부분 mismatch 에도 model load 가능성, 따라서 *MoE tensor 일부 적중* = G 분기 자격 강한 evidence, 전체 정확 패턴 일치 의무 0). grep 결과 verbatim 보고 후 실 측정 진입 별도 분기 평가 | `/tmp/phase3-5-h-tensor-moe-verify.txt` |
| 6 | **block_count + expert_count verify (R-S2 발효, namespace 광범위화 grep)** — `grep -E '\.block_count\|\.expert_count\|\.expert_used_count\|general\.architecture' /tmp/phase3-5-h-gguf-dump.log` → namespace 무관 모든 key catch. **Qwen3-30B-A3B-Instruct-2507 namespace 사전 unknown** ((g) Qwen3-Next 는 `qwen3next.*`, 본 (h) 가설 = `qwen3moe.*` 또는 `qwen3.*`, raw verify 후 확정 의무). `general.architecture` 값으로 namespace 확정 후 `-ngl <block_count>` 결정. 예상 block_count = 48 (R-S1 raw verify) | `/tmp/phase3-5-h-block-count-verify.txt` |
| 7 | **tokenizer verify (R-rec-9 발효)** — `grep -E '(tokenizer\.ggml\.model\|tokenizer\.ggml\.tokens)' /tmp/phase3-5-h-gguf-dump.log` → tokenizer family 확정. Qwen3-30B-A3B-Instruct-2507 tokenizer = Qwen3-Next 동일 가정 verify 의무 (분모 token 수 차이 = tok/s 비교 framing 변경 의무) | `/tmp/phase3-5-h-tokenizer-verify.txt` |
| 8 | **R-1 anchor 14회 추가 (mid-cycle, R-3 답습)** — 다운로드 후 verify 직전 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 §4 진입 자격 | `/tmp/phase3-5-h-r1-anchor-14x.txt` |
| 9 | egress baseline post + disk 사용량 post | `/tmp/phase3-5-h-egress-baseline-post.txt`, `/tmp/phase3-5-h-disk-post.txt` |

→ Step 4·5·6·7 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (format 차단 또는 별도 verify) 발동

---

## 4. 측정 절차 ((g) §4 답습 + Phase 3 §2.3 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | Ollama 모델 unload (`/api/generate` + `keep_alive: 0`) — GPU 메모리 0 확인. **R-1 anchor 15회 추가** (mid-cycle, 측정 *전*) — `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 측정 진입 자격 |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu,temperature.gpu --format=csv` (idle 확인, R-rec-3 발효 thermal baseline) |
| 4 | llama.cpp HEAD verify — `cd /home/delangi/src/llama.cpp && git rev-parse HEAD` = `c0c7e147...` (Phase 3 빌드 상태 보존 확인) |
| 5 | **`< /dev/null` stdin 차단 사전 dry-run (R-rec-1 발효)** — 1 short prompt (n=8 token) 으로 `< /dev/null` 효과 verify + log 누적 0 자격 확인 후 본 측정 진입 자격 |

### 4.2 측정 명령 (R-9 + R-10 답습, R-rec-6 timeout 명문 보강)

> 🟡 **prompt 파일명 vs 실 토큰 수 격차 정직성 명문 (R-10 답습, (g) §4.2 답습)**: `phase1-prompt-decode-161tok.txt` 파일명 = Ollama re-tokenize 답습, llama.cpp re-tokenize = **153 tokens** 답습 가능 (Qwen3-30B-A3B-Instruct-2507 tokenizer = Qwen3-Next 동일 가능성 §3.3 Step 7 verify 의무). 본 cycle = 동일 prompt text 답습 의무 (파일 내용 일치), tok/s 비교 시 *token 수 차이* 정직성 명문 의무 (분모 token 수 = llama.cpp re-tokenize 결과 사용).

> 🟡 **interactive mode 차단 (g) F-8 답습**: llama-cli default = interactive mode, `-no-cnv` flag 의도 미작동 → **`< /dev/null` stdin 차단** + **`-no-cnv` 명시** + **timeout 의무** ((g) F-8 답습). prefill-2k log 6.9GB 누적 위험 → cleanup 의무. **timeout 도달 + perf line 부재 = 측정 실패 분기 (별도 명시, R-rec-6 발효), perf line 적중 = 측정 성공 (interactive hang 영향 0건)**.

```bash
cd /home/delangi/src/llama.cpp

# decode-161tok prompt (Phase 1 답습, 절대 경로 한국어 큰따옴표 인용)
timeout 300 ./build/bin/llama-cli \
    -m /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
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
    -m /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
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

### 4.3 측정 항목 (R-8 + R-rec-3 답습, (g) §4.3 답습, R-S1 발효 Ollama 동일 모델 실재 framing 정정)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| tok/s decode | `[ Prompt: X.X t/s \| Generation: Y.Y t/s ]` perf line 1차 generation 종료 직후 (각 측정 명령 = 단일 perf line 출력, prompt + generation 동시, R-7 정정 framing) | 단일 cycle 한정, GPU thermal·system load 변수 |
| tok/s prefill | 동상, prefill-2k prompt | 동상 |
| total wall-clock | `llama_perf_context_print: total time` | 빌드·로딩·측정 합산 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점 |
| **GPU temperature polling (R-rec-3 발효 보강)** | `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` background. **threshold = 85°C 5분 지속 시 raw report + 사용자 명시 분기, 자동 중단 0건** | 5분 이상 연속 측정 thermal throttling 정직성 명문 |
| **(g) decode 비교 (직접 비교 가능, R-7 정정 framing)** | (g) bartowski Qwen3-Next-80B-A3B Q4_K_M `[ Prompt: 177.9 t/s \| Generation: 32.3 t/s ]` (decode-161tok 측정 명령 단일 perf line, line 37) + `[ Prompt: 971.9 t/s \| Generation: 31.5 t/s ]` (prefill-2k 측정 명령 단일 perf line, line 4~5) ((g) F-1 답습) | 본 cycle (h) Qwen3-30B-A3B-Instruct-2507 Q4_K_M 직접 비교 — model size 변수 80B vs 30B + SSM 변수 분리 핵심 가치. generation tok/s 격차 (32.3 vs 31.5) = 측정 noise 범위 (~2.5%) 또는 prompt 길이 의존성 미분리 |
| **(R-S1 발효) Ollama 동일 모델 실재 framing** | Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` 실재 ✓ (Agent C WebSearch raw verify, blob `78b329e716e7`). **본 cycle scope = llama.cpp 직접 측정 한정. Ollama 직접 측정 = 별도 cycle 자격 평가 ((h-O) HIGH carry-over, 사용자 명시 별도 cycle)** | 본 cycle = Phase 1 *간접* baseline + (g) 비교 한정. (h-O) 진입 시 Ollama 동일 모델 직접 baseline 가능 = 본 cycle 비교 framing 자격 강도 ↑ (별도 cycle, R-S1 발효 carry-over) |
| **Phase 1 Ollama 비교 (간접 baseline)** | qwen3-coder-next decode 7.83 ± 0.36 (단 다른 모델 SSM hybrid 80B) / qwen2.5-coder:32b dense decode 4.62 ± 0.18 (dense 32B baseline) | 본 cycle (h) 와 *간접* 비교 — model 차이 + activation 차이 + tokenizer 차이 + size 차이 변수 미분리 |

**측정 종료 후 R-1 anchor 16회 추가 (R-3 답습)** — 측정 직후 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 ((g) §5 답습 + R-S3 발효 framing 약화)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | tensor verify §3.3 Step 4·5·6·7 통과 + 측정 완료 (tok/s 실수치 획득) | raw report → **(g) vs (h) 격차 비교 framing (§9)** → F-1·F-2·F-3 (SSM 변수 분리) *간접* input → (k) M3·M4 cycle input 자격 (단 4 변수 동시 변경 + conversion 시점 격차 미해소, 간접 evidence 한정) |
| **B1 (format 차단, R-S3 발효 framing 약화)** | §3.3 Step 4 `ssm_*` 적중 (가설 falsification *시사*) 또는 Step 5 (i) MoE tensor 부재 또는 측정 시 `missing tensor` error. **(g) F-2 답습 — 부분 mismatch 에도 model load 가능성 명문, 따라서 B1 = format *완전* 차단 한정 (부분 mismatch + model load 성공 = G 분기 자격 강한 evidence)** | raw report → 본 cycle 자체 falsification *시사* → 후보 모델 변경 또는 (A) unsloth fallback 자격 강화 |
| **B2 (runtime 에러)** | OOM, CUDA error, segfault | raw report → **`-ngl` 조정 = 사용자 명시 후 별도 측정 단계 (자동 진입 0건)** 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | HF 403/429/network timeout | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | 다운로드 중 ENOSPC | 즉시 중단 → **partial file 보존 자격** (wget `-c` continuation 가능성, B-B8 답습) → 정리 → 디스크 확보 후 재시도 (별도 명시) |
| **B5 (sha256 mismatch, R-6 quarantine + R-S4 발효 정직성)** | 다운로드 파일 sha256 ≠ HF metadata. **(R-S4 발효) HF API lfs.sha256 = null 시 B5 trigger 자격 0 = 정직성 한계 명문**. 대체 verify = `Content-Length + ETag + GGUF metadata` 답습 | **즉시 quarantine 디렉토리 이동** (`mv` 만, **rm 0건 자동 실행 금지** 비례성 답습 영구). raw report → 사용자 명시 분기 의무 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 21 항목, (g) §6 답습 + (h) 신규 #4·#18·#19·#20·#21)

1. **HF community GGUF = 비공식 fork conversion** ((g) #1 답습) — bartowski active maintainer 답습, (g) cycle 검증 결과 (Qwen3-Next-80B 부분 호환에도 model load 성공) 답습 가능성 *시사* 만 (단 본 단일 cycle 의 호환 verify 의무 답습 영구). **(R-10 발효) (g) cycle evidence = SSM hybrid conversion 한정, (h) classical MoE conversion 신뢰도는 (h) cycle §3.3 Step 5·6 직접 verify 의무 (별개 차원)** framing 분리
2. **conversion 차이** ((g) #2 답습) — quantization 알고리즘 미세 차이 가능
3. **F2 가설 *역방향* 강화 framing 한계** — (g) F-1 격차 (~4.07× llama.cpp 더 빠름) = F2 가설 ('Ollama 효율성') *역방향* 강한 evidence. 본 (h) cycle = 변수 분리 input — SSM 기인 격차 vs classical MoE 자체 격차 분리. **(R-S1 발효 정정) Ollama 동일 모델 `qwen3:30b-a3b-instruct-2507-q4_K_M` 실재 ✓ → 본 cycle scope 외 (h-O) 별도 cycle 직접 baseline 자격 강함**. 본 (h) cycle = llama.cpp 직접 측정 + Phase 1 *간접* baseline + (g) 비교 한정
4. **(g) vs (h) 비교 변수 분리 한계 (본 cycle 신규 #4)**:
   - ✅ 통제 변수: conversion lineage *부분* (bartowski 동일, 단 시점 격차 ~3~4개월, R-S5 답습) + quant (Q4_K_M 동일) + llama.cpp HEAD (`c0c7e147` 동일) + tokenizer family (Qwen, verify 의무) + 측정 도구 (llama-cli 동일) + 측정 prompt (Phase 1 동일)
   - ❌ 미통제 변수: model size (80B vs 30B) + SSM hybrid (포함 vs 미포함) + expert count (512 top-10 vs 128 top-8) + training corpus (시점 + dataset 차이 가능) + **conversion 시점 ~3~4개월 격차 (R-S5 답습)** + **convert_hf_to_gguf.py + llama.cpp HEAD + imatrix 알고리즘 version 변수 미통제**
   - → (g) F-1 격차 ≠ (h) X 격차 결과 = SSM *또는* model size *또는* expert routing *또는* conversion 도구 version 차이 — 단일 변수 분리 자격 0 (5+ 변수 동시 변경)
5. **R-23 위반 가능성** ((g) #4 답습) — 다운로드 ~10~15분 wall-clock 중 다른 활동 발생 가능
6. **egress 비례성** — **~18.63GB egress = (g) ~48GB 의 ~39%** (R-11 답습) — 비례성 평가 답습
7. **디스크 비례성** — **~18.63GB 디스크 사용 = (g) 누적 후 ~85% → ~87% (보존 시) 또는 ~84% (cleanup 시) 임시 증가** (18.63GB / 1.9TB ≈ 0.98pp, R-11 + R-13 답습)
8. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습)
9. **GPU thermal throttling 가능성** — 5분 이상 연속 측정 시 영향 (R-rec-3 polling 명문, threshold = 85°C 5분 지속)
10. **llama.cpp HEAD `c0c7e147` 고정** — (g) 동일, Phase 3 와 직접 비교 자격 보존
11. **prompt set 답습 정확성 의존 + tokenizer 변수 (R-rec-9 발효)** — Phase 1 detokenize 정확성 (R-10 답습 — Qwen3-30B-A3B-Instruct-2507 tokenizer = Qwen3-Next 동일 가능성 §3.3 Step 7 사전 verify 의무). **동일하지 않을 시 token 수 분모 변경 → tok/s 비교 framing 변경 의무, 별도 처리 분기 명문 (예: §3.3 Step 7 결과 mismatch 시 raw report + 사용자 명시 분기)**
12. **N=1 결과 단정 금지** — 측정 결과 = *후속 cycle input* only (Phase 3 R-3 framing 답습)
13. **Provider Liquidity finding 강화/약화 framing 분리 (C-H5 답습)**:
    - 본 cycle G 성공 + (g) 격차 답습 (~4.07× 유사) → SSM 비기인 시사 → classical MoE = Ollama vs llama.cpp 격차 본질 *강화* evidence (단 4+ 변수 동시 변경 → "강화" 단정 자격 strict single-variable cycle 의무, N-7 답습)
    - 본 cycle G 성공 + (g) 격차 약화 (~1~2×) → SSM 기인 시사 → MVP-1 R4 framing *복잡화* (SSM 한정 차이)
    - 본 cycle B1 차단 → 다른 source 또는 가설 재고 (R-S3 답습 — 단정 자격 약화)
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
14. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
15. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
16. **HF egress = github.com / huggingface.co 의도 외 추가 source 0건 의무**
17. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
18. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만, 코드/측정 변경 0
19. **bartowski Qwen3-30B-A3B-Instruct-2507-GGUF repo *실재 verify* 완료 (R-S1 발효)** — 본 v1.1 = `bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF` Q4_K_M 18.63GB single file split:false qwen3moe arch 30.5B/3.3B activated 128 top-8 created 2025-07-28 직접 verify 답습 영구. v1 가정 두 후보 모두 HF 실재 0건 확정 정정
20. **sha256 verify 자격 부분 미충족 가능성 (R-S4 발효, (g) F finding 답습)** — multipart upload 시 HF API lfs.sha256 = None, 대체 verify = `Content-Length + ETag + GGUF metadata` 자격으로 부분 검증 한정. lfs.sha256 None 시 B5 quarantine 분기 trigger 자격 0
21. **bartowski conversion 시점 ~3~4개월 격차 정직성 한계 (R-S5 발효)** — (g) Qwen3-Next-80B-A3B-Instruct-GGUF createdAt ~2025-11~12 vs (h) Qwen3-30B-A3B-Instruct-2507-GGUF createdAt 2025-07-28 = ~3~4개월 격차 = convert_hf_to_gguf.py + llama.cpp HEAD + imatrix 알고리즘 version 변수 미통제 가능성. conversion lineage 변수 통제 *부분 한정* framing

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구, R-8 발효 §0 #1 4 동사 확장)

본 §0 14 항목과 §7 차단 조건은 **1:1 매핑 의무** ((g) R-15 답습).

1. ❌ 본 brief 자체 다운로드/빌드/측정/sudo 실행 (R-8 발효 — 4 동사 확장)
2. ❌ Ollama daemon 변경 (pid 3375 보존)
3. ❌ llama.cpp HEAD 변경 (`c0c7e147` 보존)
4. ❌ 새 빌드 (`build/bin/llama-cli` 재사용)
5. ❌ MVP-1 합의 본문 자동 정정
6. ❌ 헌법·ADR 본문 자동 정정
7. ❌ M3·M4 결정 *고정* ((k) 별도 cycle)
8. ❌ runtime backend 코드 작성 (트랙 B 별도)
9. ❌ 메모리 자동 갱신
10. ❌ (h-O)/(j)/(k)/(l)/(m)/(n) 자동 진입
11. ❌ brief commit 자동 진입
12. ❌ 다운로드 시점 = 사용자 명시 *직접* 의무 (R-11 비례성 답습)
13. ❌ (g)+(h) 통합 본문 정정 ((g) brief/합의 본문 변경 0건) + (g)+(h) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (N-12 답습, 별도 차원 carry-over)
14. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 (chain 영구 종결 의무 답습 영구)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (g) 격차 답습 (~4.07× 유사) | classical MoE 자체 격차 본질 strong evidence (단 4+ 변수 동시 변경, N-7 답습) → MVP-1 R4 framing *강화* (별도 cycle) + (k) M3·M4 cycle input 자격 강화 + **(h-O) Ollama 직접 측정 cycle 자격 강함** |
| G + (g) 격차 약화 (~1~2×) | SSM 기인 격차 strong evidence → MVP-1 R4 framing *복잡화* (SSM 한정) + (g) F-1 재해석 cycle (별도) + **(h-O) Ollama 직접 측정으로 변수 추가 통제** |
| G + (g) 격차 역전 (Ollama 빠름) | SSM 기인 다른 방향 → F2 가설 재고 cycle (별도) + **(h-O) 직접 baseline 자격 결정적** |
| B1 (format 차단, R-S3 약화) | 가설 falsification *시사* → (A) unsloth fallback 자격 강화 + 가설 재고 |
| B2~B5 | (g) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습, R-12 발효 6 후보 추가)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **(h-O) Ollama qwen3:30b-a3b-instruct-2507-q4_K_M 직접 측정 cycle** | **HIGH ⭐⭐⭐ (R-S1 발효 신규)** | brief §4.3 framing 정정 후 별도 cycle. Ollama 동일 모델 직접 baseline 자격 강도 ↑ |
| MVP-1 합의 R4 framing 강화 evidence cycle | HIGH | (g) F-1 + 본 cycle 결과 종합 input |
| llama.cpp graceful tensor name resolution 검증 cycle | MEDIUM | (g) F-2 + R-S3 답습 read-only (`src/llama-model-loader.cpp` 분석) |
| (j) advisory wall-clock 측정 | MEDIUM | 자비스 비전 직접 진전 |
| (k) M3·M4 결정 *고정* | DEFER | 변수 분리 강화 input 후 자격 평가 |
| (l) MVP-1 트랙 B 구현 | DEFER | (k) 통과 의무 답습 영구 |
| **Qwen3-Next-7B 변종 cycle** (R-12 발효 신규) | LOW | model size 단독 변수 분리 |
| **다른 expert config 모델 비교 cycle** (R-12 발효 신규) | LOW | expert routing 단독 변수 분리 |
| **imatrix variant 단독 비교 cycle** (R-12 발효 신규) | LOW | quant scheme 변수 분리 |
| **(g)+(h) 통합 *분석* cycle** (R-12 발효 신규, ≠ 통합 *본문 정정*) | DEFER | 변수 분리 종합 + Provider Liquidity finding 종합 |
| **외부 benchmark cross-reference cycle (GB10 vs RTX/A100/H100)** (R-12 + N-13 발효 신규) | LOW | hardware + version 차이 cross-check |
| bartowski conversion 시점 + imatrix 출처 verify cycle | LOW | R-S5 + N-11 답습 |
| Phase 3 summary recommendation C 정정 | LOW | (i) falsification + (g) 성공 답습 |
| 다른 quant 비교 (Q5_K_M / IQ4_XS) cycle | LOW | R-rec-2 답습 |
| (g)+(h) 통합 본문 정정 cycle | DEFER | 사용자 명시 별도 cycle, (g) brief/합의 본문 변경 0건 |
| `llama-bench` carry-over | **MEDIUM (R-rec-12 발효 LOW → MEDIUM 격상 평가)** | (g) F-8 risk 직접 해소 자격 — 자동 통계 + interactive 차단 by-design |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| (A) unsloth fallback carry-over (R-2 답습) | LOW | (B) 차단 시 fallback (사용자 명시 별도, N-11 답습) |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((g) 동형 풀 7단계 답습, 사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `a504352`, 382줄 | 명시 완료 |
| (2) 풀 3+1 합의 진행 + commit | `d74d205`, 491줄, BLOCKING 13 + R-S1~R-S5 | 명시 완료 |
| **(3) brief v1.1 보강 + commit (본 단계)** | BLOCKING 13 verbatim 100% + R-S 5 흡수 12곳 + 권고 12 + §11 v1→v1.1 일람 신규 | **진행 중** |
| (4) 다운로드 실행 (~10~15분 wall-clock, R-6 발효) | §3.2 옵션 (b) wget direct (R-7 답습) + (g) Q4_K_M 보존/cleanup 사용자 명시 (R-13 발효) | **사용자 명시 *직접* 의무 (~18.63GB egress)** |
| (5) verify + 측정 실행 (~30~60분 wall-clock) | §3.3 + §4 절차 답습 | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (g) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (g) vs (h) 비교 framing (본 cycle 핵심 가치, 정직성 명문 + 시나리오 7 R-11 발효)

### 9.1 (g) 측정값 답습 (직접 비교 baseline, R-7 정정 framing — 단일 perf line 출력)

| 항목 | (g) bartowski Qwen3-Next-80B-A3B Q4_K_M | 측정 방법 비고 |
|---|---|---|
| decode-161tok 측정 명령 perf line | **`[ Prompt: 177.9 t/s \| Generation: 32.3 t/s ]`** (line 37 verbatim) | 단일 perf line — prompt + generation 동시 출력 |
| prefill-2k 측정 명령 perf line | **`[ Prompt: 971.9 t/s \| Generation: 31.5 t/s ]`** (line 4~5 verbatim) | 동상 |
| 모델 크기 | ~80B total, ~3B activated (top-10 of 512 experts) | MoE + SSM hybrid (48 layers 중 12 attention + 36 SSM) |
| GGUF 크기 | 45.38 GiB | |
| 비고 | generation tok/s 격차 (32.3 vs 31.5) = 측정 noise 범위 (~2.5%) 또는 prompt 길이 의존성 미분리 정직성 | R-7 정정 framing |

### 9.2 (h) 예상 결과 시나리오 7 (R-11 발효 — 사전 가설 평가, 단정 0)

| 시나리오 | (h) decode tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: 답습 (~30~35 t/s)** | classical MoE 자체 격차 본질 — SSM 비기인 strong evidence | MVP-1 R4 framing *강화* (단 *간접* input only, 4+ 변수 미분리) | (h-O) Ollama 직접 측정 + F-2 별도 cycle |
| **S2: 강화 (~40~85 t/s, R-rec-2 발효 범위 확장)** | classical MoE + small size 추가 advantage. memory-bandwidth roofline framing — 단순 size scaling 1/0.375 ≈ 2.67× 가정 시 (g) 32.3 → ~86 t/s | SSM 미포함 + size 변수 미해소 (*간접* input only) | model size 변수 분리 cycle (~7B 모델 별도, R-12 발효) |
| **S3: 약화 (~15~25 t/s)** | SSM 기인 격차 부분 + model size 영향 | (g) F-1 격차 SSM 기인 가설 *부분* support (*간접* input only) | SSM 한정 차이 framing 별도 cycle |
| **S4: 역전 (Ollama 빠름)** | classical MoE 만으로 Ollama advantage | F2 가설 재고 + 측정 도구 변수 평가 (*간접* input only) | F2 재고 cycle (별도) + (h-O) 결정적 |
| **S5: tokenizer 변수 (R-11 발효 신규)** | Qwen3-30B-A3B-Instruct-2507 tokenizer ≠ Qwen3-Next 시 분모 token 수 차이 | tok/s 비교 자격 약화 (*분모 불일치* framing 의무) | §3.3 Step 7 결과 답습 + tokenizer 변수 분리 cycle |
| **S6: GPU memory 부족 부분 offload (R-11 발효 신규, risk LOW)** | -ngl 48 자동 조정 risk (Q4_K_M 18.63GB + KV cache, GB10 unified 121GB 충분 → risk LOW 자격 정합) | §5 B2 분기 답습 | risk 낮음, raw report 시 OOM 발생 시 사용자 명시 별도 |
| **S7: 다른 tensor mismatch (R-11 발효 신규)** | (g) F-2 답습 — 부분 호환 model load 성공 자격. (h) classical MoE 가설 = SSM mismatch 0, 단 다른 mismatch 가능성 (예: GQA head_count_kv 차이) | falsification 자격 약화, model load 가능성 강함 (R-S3 답습) | §3.3 Step 5·6 결과 + (g) F-2 graceful resolution 가설 input |

### 9.3 핵심 정직성 (변수 미분리 명문)

- ❌ **단일 변수 분리 자격 0** — (g) → (h) 변화 5+ 변수 동시: model size (80B→30B) + SSM (포함→미포함) + expert routing (512 top-10 → 128 top-8) + **conversion 시점 ~3~4개월 격차 (R-S5 답습)** + **도구 version 변수 미통제**
- ✅ **통제 변수 *부분* 강함** — conversion lineage *부분* (bartowski 동일 maintainer, 단 시점 격차) / quant / llama.cpp HEAD / tokenizer family (verify 의무) / 측정 도구 / prompt 동일
- → **(g)+(h) 단일 trial = SSM 변수 *간접* input only**, 단일 변수 분리는 별도 후속 cycle (~7B classical MoE 또는 80B classical 모델 별도 비교 필요, R-12 발효)
- **(R-S1 발효) Ollama 동일 모델 직접 baseline 가능** = (h-O) cycle 진입 시 본 (h) 결과 + Ollama 동일 모델 결과 종합 → 비교 framing 자격 강도 ↑

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = (h) 풀 3+1 합의 (`d74d205`, 491줄) BLOCKING 13 verbatim 100% 흡수 + R-S1~R-S5 흡수 12곳 + 권고 12 일부 흡수 + §11 v1→v1.1 변경 일람 신규
- 본 cycle 진입 = (g) cycle 완료 (`b3d4164`) + 사용자 명시 (h) 4 명확화 + 풀 3+1 합의 직후
- 본 brief 자체 머신 변경 0건 (다운로드/빌드/측정/Ollama 변경/sudo 0건)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)
- ⭐⭐⭐ R-S1 CRITICAL 흡수 = repo ID `bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF` 단일 확정 + Ollama 동일 모델 실재 framing 정정 + (h-O) Ollama 직접 측정 cycle 신규 HIGH carry-over 발효
- 본 brief v1.1 길이 = 382줄 → ~520줄 (v1 대비 +~140줄, BLOCKING 13 + R-S 5 + 권고 + §11 추가)

---

## 11. v1 → v1.1 변경 일람 ((g) R-rec-6 답습 + 본 합의 §11 답습)

### 11.1 BLOCKING 13 흡수 매트릭스 (verbatim 100%, R-21 답습 영구)

| BLOCKING | 출처 | brief v1.1 정정 위치 | 본문 변경 |
|---|---|---|---|
| **R-1 (R-S1 발효) ⭐⭐⭐ CRITICAL** | 3-way Consensus (A-B5 + B-B1/B-S2 + C-B1/C-S1) | §2.1 매트릭스 row B (Qwen_Qwen3-30B-A3B-Instruct-**2507**-GGUF 단일 확정) + §2.1 (A) row (unsloth Instruct-2507 정정 + Dynamic 2.0 quant) + §2.2 Step 1 example URL + §3.2 wget URL (placeholder 0건 직접 fill) + §4.3 line 225 (Ollama 실재 + (h-O) HIGH carry-over) | 4 곳 verbatim 정정, repo ID -2507 suffix 추가 + Ollama 동일 모델 실재 framing 정정 |
| **R-2 (R-S2 발효) ⭐⭐ HIGH** | 3-way Consensus (A-B1 + A-B2 + B-B10 + C-B4) | §3.3 Step 5 grep 패턴 확장 (`attn_qkv` 추가 + Qwen3-Next 답습 명문) + Step 6 grep 패턴 광범위화 (namespace 무관 + `general.architecture`) | 2 곳 grep 패턴 + 정직성 명문 |
| **R-3 (R-S3 발효) ⭐⭐ HIGH** | 2+ Agent 일치 (B-B7 + B-B10 + A-rec-6) | §3.3 Step 4 framing 약화 ("강한 evidence" + (g) F-2 가능성 명문) + Step 5 framing 약화 ("부분 mismatch 에도 model load 가능성" 명문) + §5 B1 분기 framing 약화 | 2 곳 약화 |
| **R-4 (R-S4 발효) ⭐ MEDIUM** | 2+ Agent 일치 (A-B3 + B-B6) | §3.3 Step 2 ((g) F finding 답습 multipart upload 명문 + 대체 verify) + §6 #20 신규 | 2 곳 신규 명문 |
| **R-5 (R-S5 발효) ⭐ MEDIUM** | 2+ Agent 일치 (B-B12 + C-S3) | §2.1.1 신규 § (bartowski 동일 maintainer 부분 통제 + 시점 격차) + §2.1 line 100 framing 약화 + §6 #21 신규 | 3 곳 신규 명문 |
| **R-6** | 2+ Agent 일치 (A-B6 + C-N-5) | §1.1 + §3.2 시간 예상 (~11.8분, 범위 ~10~15분) + §8.3 (4) 시간 정정 + §6 정직성 한계 외부 benchmark cross-ref 자격 | 3 곳 시간 + 외부 reference 정직성 |
| **R-7** | Agent A 단독 | §4.3 (g) decode 비교 행 perf line 단일 출력 framing + §9.1 표 framing | 2 곳 framing 정직성 |
| **R-8** | Agent B 단독 | §7 #1 4 동사 확장 (`다운로드/빌드/측정/sudo 실행`) | 1 곳 확장 |
| **R-9** | Agent B 단독 | §3.0 sudo 사용 명문 (단 1회 한정, 사용자 명시 임시 비밀번호 의무 답습) | 1 곳 명문 |
| **R-10** | Agent B 단독 | §6 #1 framing 분리 ((g) SSM hybrid evidence 한정 + (h) classical MoE 별도 차원) | 1 곳 framing 분리 |
| **R-11** | Agent C 단독 | §9.2 S5/S6/S7 3 시나리오 추가 + 각 시나리오 "*간접* input only" 강도 표기 | §9.2 3 시나리오 + 강도 표기 |
| **R-12** | Agent C 단독 | §8.2 6 후보 추가 ((h-O) HIGH + Qwen3-Next-7B + 다른 expert config + imatrix + (g)+(h) 통합 *분석* + 외부 benchmark cross-ref) | §8.2 6 후보 추가 |
| **R-13** | Agent C 단독 (R-rec-6 + A-rec-1 답습) | §3.0.1 신규 § ((g) Q4_K_M GGUF 보존/cleanup 사용자 명시 의무 명문) | 1 곳 신규 § |

### 11.2 Reviewer 단독 격상 R-S1~R-S5 흡수 매트릭스 (위 11.1 답습 통합)

- **R-S1 ⭐⭐⭐ CRITICAL** → R-1 발효 (4 곳)
- **R-S2 ⭐⭐ HIGH** → R-2 발효 (2 곳)
- **R-S3 ⭐⭐ HIGH** → R-3 발효 (2 곳)
- **R-S4 ⭐ MEDIUM** → R-4 발효 (2 곳)
- **R-S5 ⭐ MEDIUM** → R-5 발효 (3 곳)
- **총 13 곳 정정**

### 11.3 권고 12 흡수 매트릭스 (강한 권고 직접 흡수, 약한 권고 by-reference)

| 권고 | 흡수 자격 | brief v1.1 정정 위치 |
|---|---|---|
| R-rec-1 (< /dev/null dry-run) | 강함 | §4.1 Step 5 신규 |
| R-rec-2 (S2 memory-bandwidth roofline) | 강함 | §9.2 S2 범위 확장 (~40~85) + framing |
| R-rec-3 (GPU thermal threshold 85°C 5분) | 강함 | §4.1 Step 3 + §4.3 R-rec-3 항목 |
| R-rec-4 (F-7 reference 정정) | 약함 | §2.2 Step 4 reference 정정 |
| R-rec-5 (§3.3 Step 4 framing 약화) | R-S3 통합 | R-3 발효 |
| R-rec-6 (timeout 명문 보강) | 강함 | §4.2 timeout 직후 명문 |
| R-rec-7 (Phase 3.5-B 명명 통합) | 강함 | §0 #13 + §1.3 통합 framing |
| R-rec-8 (§6 (g) → (h) 답습 출처 명문) | 부분 | §6 #1·#2·#3·#4 출처 명문 (선택적) |
| R-rec-9 (tokenizer 변수 분기) | 강함 | §3.3 Step 7 신규 + §6 #11 보강 |
| R-rec-10 (model variant 식별) | R-S1 발효 | R-1 발효 |
| R-rec-11 (project_mvp_staged_roadmap 메모리 추가) | 약함 | 답습 권위 line 19 추가 |
| R-rec-12 (llama-bench LOW → MEDIUM 격상) | 강함 | §8.2 llama-bench 우선순위 격상 |

### 11.4 NOTE 13 by-reference (변경 0건, §7 합의 보고서 답습)

- N-1~N-13 = 합의 보고서 §7 by-reference 한정, 본 brief v1.1 직접 흡수 0건

### 11.5 기각 5 답습 (변경 0건, §8 합의 보고서 답습)

- 기각-1~5 = 합의 보고서 §8 답습 영구, 본 brief v1.1 변경 0건

---

**본 brief v1.1 작성 완료** (Phase 3.5-B (h) Qwen3-30B-A3B 대조군 cycle entry plan, 풀 3+1 합의 APPROVE w/ COND + BLOCKING 13 verbatim 100% 반영 + R-S1~R-S5 흡수 12곳 + 권고 12 일부 흡수 + §11 v1→v1.1 변경 일람 신규. ⭐⭐⭐ R-S1 CRITICAL 발효 = repo ID `bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-GGUF` 단일 확정 + Ollama 동일 모델 실재 framing 정정 + (h-O) Ollama 직접 측정 cycle 신규 HIGH carry-over. 본 cycle 머신 변경 0건. 다음 단계 = 사용자 명시 의무 답습 영구.)
