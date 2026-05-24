# 3+1 합의 보고서 — 자비스 MVP-1 V-1 PoC Phase 3.5 (g) new GGUF entry brief v1

> **본 합의 = Phase 3.5 (g) brief v1 → v1.1 *진입 게이트* 한정** (staged consensus 답습). 실 다운로드/측정/M3·M4 결정 *고정* 자격 평가 0건. brief 갱신·commit·push 0건 (사용자 명시 별도).

---

**최종 판단**: **APPROVE w/ COND** (BLOCKING 정정 verbatim 반영 의무)
**합의 일시**: 2026-05-25T05-15+09:00
**합의 단위**: Phase 3.5 (g) entry brief v1 (`docs/phase0/jarvis-mvp1-v1-poc-phase3-5-new-gguf-entry-brief.md`, 311줄, commit `0867fee`)
**사용자 명시 입력**: 모델 source = **(B) bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF Q4_K_M** 단일 확정 / 진행 형태 = 풀 3+1 합의
**3 Agent 종합 판정**: 3 × APPROVE w/ COND (정면 충돌 1건 = D-1 변수 분리 강도 framing, 본 합의에서 통합 흡수)

---

## 0. 본 합의가 *하는* 것 / *하지 않는* 것

### 0.1 하는 것

1. Agent A/B/C 3개 독립 분석 출력 교차 비교 (일치/부분/불일치/누락 4 분류)
2. raw line-level direct cross-check 으로 Reviewer 단독 격상 R-S1~R-S4 식별 (Phase 3 R-S1~R-S6 + (g1-N-3-adr-008+sip+adr-012') R-S1~R-S3 패턴 답습)
3. BLOCKING verbatim 100% 답습 의무 채택 (Phase 3 합의 R-21 답습 영구)
4. 권고 / NOTE / 기각 분류 + 합의 도출
5. brief v1 → v1.1 보강 매트릭스 명문 (§10)
6. 후속 carry-over 매트릭스 (chain 영구 종결 의무 답습)
7. 본 합의 자체 권한 한계 명문 (§11)

### 0.2 하지 않는 것 (영구 답습)

1. ❌ brief v1.1 갱신·commit·push (사용자 명시 별도)
2. ❌ 실 다운로드 / 빌드 / 측정 / sudo 실행
3. ❌ Ollama daemon 상태 변경 (pid 3375 보존)
4. ❌ `/home/delangi/src/llama.cpp` HEAD `c0c7e147` 변경
5. ❌ MVP-1 합의 본문 / 헌법 5조-2 / ADR-011 본문 자동 정정
6. ❌ M3·M4 결정 *고정* (별도 (k) cycle 의무)
7. ❌ (h)/(j)/(k)/(l)/(m)/(n) 자동 진입 (사용자 명시 의무 답습 영구)
8. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 (chain 영구 종결 의무 답습 영구)
9. ❌ 메모리 자동 갱신
10. ❌ Reviewer 권한 한계 (1)~(11) 답습 영구 (§11)

---

## 1. 3-way Consensus (3 Agent 모두 일치, ① 카테고리)

### C-1. 전체 방향 (Phase 3.5 (g) cycle 진입 자체 + 절차 골격 + §0 12 항목 framing)

3 Agent 모두 (g) cycle 진입 *자체* 자격 = APPROVE. brief §0 (하는 것 / 하지 않는 것) 12 항목 framing + §7 1:1 매핑 self-consistency + §6 정직성 한계 17 항목 + §8 carry-over 매트릭스 (chain 영구 종결 명문) = 방향 합의. brief v1 → v1.1 BLOCKING verbatim 보강 후 사용자 명시 다음 단계 (다운로드 실행) 진입 자격.

### C-2. R-1 anchor 회차 부족 (브리프 본문 2 회만, Phase 3 brief 4 회 패턴 답습 의무)

- A-rec-3 (R-1 회차 누적 명문 추가) + B-B1 (4 회 의무, Phase 3 entry brief line 129/149/168/186 4 anchor 패턴 답습) + C 간접 동의 = 강한 합의
- 본 brief §3.1 Step 4 (9회 추가, line 115) + §4.1 Step 1 (10회 추가, line 161) = **2 회만** 명문
- 의무 회차 = 4 회 (Phase 3 entry brief 답습): (a) §3.1 사전 (9회) / (b) §3.3 다운로드 후 verify 직전 (10회) / (c) §4.1 측정 *전* (11회) / (d) §4.3 측정 *후* (12회)
- → **R-1 (BLOCKING)** 채택 verbatim 100%

### C-3. 사용자 명시 (B) bartowski 단일 source 확정 framing 부재

- B-B2 강하게 BLOCKING + A 간접 (§2.1 매트릭스 4 후보 line 89~92 vs §3.2 `<REPO>` placeholder line 123/126/135 비대칭) + C-S4 ((B) 단독 자격 + (A) unsloth fallback carry-over 명문)
- 사용자 명시 = **(B) bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF Q4_K_M** 단일 확정 (본 cycle 입력 의무)
- → **R-2 (BLOCKING)** 채택 verbatim 100%

### C-4. `llama-gguf` subcommand 정확성 (`l` → `r`)

- A-B1 강하게 BLOCKING + B/C 간접 (정확성 한계 명문)
- **Reviewer raw cross-check 확정**: `/home/delangi/src/llama.cpp/build/bin/llama-gguf --help` 직접 실행 → `usage: ... data.gguf r|w [n]` / `r: read data.gguf file` / `w: write data.gguf file` / `n: no check of tensor data` (3 subcommand 한정, `l` 부재 확정)
- 본 brief §3.3 Step 3 line 146 의 `<FILE>.gguf l` = 즉시 abort 사유
- 정정안 = `r` 사용 (Phase 3 entry brief line 147 의 `r` 답습 + (i) raw finding 의 `r` 답습 line 35~39)
- → **R-3 (BLOCKING)** 채택 verbatim 100%

### C-5. R-6 framing (PASS/FAIL 단정 금지) 답습 의무

- A (§6 NOTE 단정 framing) + B-B4 (§6 #1 "광범위 community 검증" 강도 단언) + C-B8 (§3.3 Step 4·5 tensor name pattern 단정)
- Phase 3 합의 R-6 (PASS/FAIL framing 금지) 답습 영구 의무
- → **R-4 (BLOCKING)** 채택 verbatim 100%

---

## 2. 2+ Agent 부분 일치 (② 카테고리) + 결정

### P-1. Phase 3.5 명명 충돌 (A-S1) + 변수 분리 강도 (C-B1)

- A-S1: (g) Phase 3.5 + (h) Phase 3.5 동일 호칭 → "Phase 3.5-A/B" 권고
- C-B1: (g) 단독 framing 변수 분리 강도 약화 (Phase 3 R-5 답습)
- B 간접 동의 (정직성 명문)

**결정**: 본 cycle = (g) 단독 진입 자격 유지 (사용자 명시 답습), 단 정직성 한계 명문 의무. **R-5 (BLOCKING)** = §6 정직성 한계 신규 행 추가 + §1.3 (h) carry-over 가능성 명문 강화. (g)+(h) 통합 cycle 또는 (h) trigger 명문 = 권고 격하 (사용자 명시 별도 cycle 자격).

### P-2. sha256 mismatch 분기 (B-B3) — 즉시 삭제 vs quarantine

- B-B3: §5 B5 sha256 mismatch → 즉시 삭제 = false-positive 4 case (위조 / HF race / 기대값 추출 오류 / 부분 write race). 50GB 즉시 삭제 = 비례성 약화
- A 간접 (분기 framing 정직성) + C 간접 (대안 보존)

**결정**: **R-6 (BLOCKING)** = §5 B5 분기 정정안 = quarantine 디렉토리 이동 (rm 0건) + 사용자 명시 후 삭제/재다운로드. 비례성 답습.

### P-3. 다운로드 도구 명문 (A-rec + C-B6 aria2c)

- A 간접 (huggingface-cli 미설치 명문 부재, §3.1 Step 5)
- C-B6: aria2c 누락 (multi-connection 5~10× wall-clock 단축)
- B 간접

**Reviewer raw cross-check**: `which huggingface-cli wget curl aria2c` → **wget/curl 만 존재**, huggingface-cli/aria2c 미설치 확정.

**결정**: 본 cycle = wget/curl 단독 사용 자격 (apt 의존성 egress 0건 답습 의무). huggingface-cli 미설치 분기 명문 + aria2c 후보 NOTE 격하 (비례성 — 본 cycle 50GB 단일 다운로드, multi-connection 가속 우선순위 약함). **R-7 (BLOCKING)** = §3.1 Step 5 정정 + §3.2 옵션 (a) huggingface-cli 분기 = "미설치 시 옵션 (b) wget 사용" 명문.

### P-4. `llama-bench` / `llama-perplexity` 대안 평가 (C-B3)

- C-B3 강하게 BLOCKING: §4.2 `llama-cli` 단독 의존 — `llama-bench` (자동 통계) + `llama-perplexity` (품질 검증) 부재
- A-rec 간접 (측정 도구 다양성)
- B 미언급

**결정**: 본 cycle = `llama-cli` 단독 사용 자격 유지 (Phase 3 §2.3 Step 3 답습 의무, format 호환 verify 가 핵심 목표, 정확성·재현성 평가 자격 본 cycle 외). `llama-bench` carry-over 권고 격하. **R-rec-1** 신규 (`llama-bench` carry-over 권고, (j) advisory cycle 또는 별도 정확성 cycle 입력 자격).

### P-5. quant Q4_K_M 단독 진입 정직성 (C-B4)

- C-B4 강하게 BLOCKING: Q5_K_M / IQ4_XS / Q6_K 후보 비교 매트릭스 부재
- A/B 간접 (정직성 명문)

**결정**: 본 cycle = Q4_K_M 단독 자격 유지 (사용자 명시 + 비례성 답습). 후보 quant 비교 매트릭스 = NOTE 격하 (별도 cycle). **R-rec-2** 신규 (quant 비교 cycle carry-over 권고).

### P-6. measurement 항목 추가 (C-B7) — KV cache miss rate / GPU SM utilization / thermal polling

- C-B7 강하게 BLOCKING: §4.3 측정 항목 부족
- A-rec-2 간접 (`-DGGML_PERF=ON` Phase 3 답습)
- B 미언급

**결정**: 본 cycle = §4.3 5 항목 (tok/s decode / tok/s prefill / wall-clock / GPU mem peak / Ollama 비교) 기본 유지 + GPU thermal polling 권고 격상. **R-rec-3** 신규 (`nvidia-smi --query-gpu=temperature.gpu` polling 권고, R-23 답습 보강).

---

## 3. Reviewer 단독 격상 (raw line-level direct cross-check, ⭐ 등급 부여)

> Reviewer 의 raw line-level direct cross-check 으로 Agent 단독 격상 후보 (A-S1~A-S3, B-S1~B-S3, C-S1~C-S4) 중 채택 + 신규 식별. Phase 3 합의 R-S1~R-S6 + (g1-N-3-adr-008+sip+adr-012') R-S1~R-S3 패턴 답습.

### R-S1 ⭐⭐⭐ CRITICAL — brief §4.3 line 203 "Phase 1 cache miss 56.3 mean" 값 부정확 (출처 0건)

- **A-S2 단독 격상 후보** = 56.3 vs 7.83 ~7× 격차 verify 의무
- **Reviewer raw cross-check 확정** (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json` 직접 read):
  - line 77 verdict_1: `cache miss 진정한 prefill ≈ 58 tok/s, std 0.27`
  - line 72: `Stage 4 precheck (cache miss 1회) prefill_tok_per_sec: 57.79`
  - line 78 verdict_2: `C-c 3회 mean (58.27)`
  - line 103 m4_decision_readiness: `cache miss 58 tok/s + cache hit 291 tok/s + decode 7.83 tok/s`
- **`grep -rn "56.3" docs/phase0/v1-poc-raw/`** = 결과 0건 (raw 어디에도 56.3 부재)
- → brief §4.3 line 203 의 "56.3 mean" = **출처 부재 false value 확정**
- **차원 혼동 risk**: F1·F2 가설 답습 시 비교 의도 = *decode* tok/s (7.83 ± 0.36) 비교, *prefill cache miss* (58 tok/s) 비교 아님
- **정정안 (R-21 verbatim 답습)**: line 203 = "Phase 1 답습 (decode mean 7.83 ± 0.36 tok/s)" 으로 정정 + prefill 비교 의도 분리 명문 (필요 시 §4.3 신규 행 = "prefill tok/s cache miss 비교 = Phase 1 cache miss 58 tok/s")
- **격상 사유**: F1·F2 가설 framing 정확성 = 본 cycle 측정 비교 강도의 *전제*. 56.3 false value 잔존 시 측정 후 비교 framing 오염 → MVP-1 R4 본문 정정 input 자격 약화. ⭐⭐⭐ CRITICAL 등급.

### R-S2 ⭐⭐ HIGH — brief §4.2 prompt 파일 절대 경로 부재 (Phase 3 entry brief 답습 보강 의무)

- **A-rec-4 단독 격상 후보**
- **Reviewer raw cross-check 확정**:
  - brief line 168 = `cd /home/delangi/src/llama.cpp`
  - brief line 173 = `-f docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt`
  - 결합 시 실 path = `/home/delangi/src/llama.cpp/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt`
  - `ls /home/delangi/src/llama.cpp/docs/phase0` = **존재 0건** 확정
  - 실 prompt 파일 = `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt` (확인됨, 530 bytes)
- → brief §4.2 line 173·185 = 실행 시 `error: failed to open file` 즉시 abort 사유
- **정정안 (R-21 verbatim 답습)**: line 173·185 `-f` 인자 절대 경로 변경 = `-f /home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt` (한국어 path 인용 의무)
- **격상 사유**: A-B1 (`llama-gguf l→r`) 와 동급 즉시 abort. ⭐⭐ HIGH 등급 (R-S1 보다 1단계 낮음, R-S1 은 framing 정확성, R-S2 는 명령 실행 가능성).

### R-S3 ⭐⭐ HIGH — brief §3.3 Step 3 의 `llama-gguf` subcommand `l` (A-B1 강화 + Phase 3 brief 답습 정합 의무)

- A-B1 = 본 BLOCKING (R-3)
- **Reviewer raw cross-check 추가 evidence**:
  - `/home/delangi/src/llama.cpp/build/bin/llama-gguf` 직접 실행 결과 = `usage: ... data.gguf r|w [n]` 확정 (3 subcommand: `r`/`w`/`n`)
  - Phase 3 entry brief line 147 (Step 6.5) verbatim = `./build/bin/llama-gguf /root/.ollama/models/blobs/sha256-30e51a7cb1cf... r 2>&1 | head -80` — **`r` 사용 답습**
  - (i) raw finding (line 35~39) = `git log --all -p -S 'layer.ssm_dt'` 의 read 행위 답습 (subcommand `r`)
- → A-B1 BLOCKING 의 *추가 강도* 확정 (Phase 3 brief + (i) raw 답습 직접 답습 의무)
- **격상 사유**: A-B1 단독 BLOCKING 자격 외 Phase 3 brief 답습 정합 의무 명문 = brief v1.1 정정 위치 명문 강도 ↑ (단순 `l→r` 정정 외 "Phase 3 entry brief Step 6.5 답습 의무" 명문). ⭐⭐ HIGH 등급.

### R-S4 ⭐ MEDIUM — brief §1.1 "egress ~50GB" vs §2.1 매트릭스 "~48GB" 격차 (A-S3 채택)

- A-S3 단독 격상 후보
- **Reviewer raw cross-check 확정** (`docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json` 직접 read line 37): `ollama_gguf_size_GiB: 48.18`
- brief §1.1 line 58 = "egress ~50GB", brief §2.1 line 89~92 매트릭스 = "~48GB", brief §6 #5 line 228 = "50GB egress = ...5×", §6 #6 line 229 = "82% → 87%"
- → 격차 = ~50 - 48.18 ≈ 1.82 GiB (HTTP overhead + GGUF metadata + 보수 margin 자격 평가 가능)
- **정정안**: 본 cycle = 정직성 명문 (egress = HF lfs `Content-Length` 사전 verify 후 정확값 보고 의무, ~48~50GB 범위 답습). brief §1.1 line 58 / §6 #5 / §6 #6 정정 의무 (~48GB primary + ~50GB worst-case framing).
- **격상 사유**: 단일 cycle egress 비례성 framing 정확성 = 헌법 5조-2 Provider Liquidity finding 답습 강도의 입력. ⭐ MEDIUM 등급 (R-S1/R-S2 보다 strict abort 자격 ↓, framing 정직성 차원).

---

## 4. BLOCKING (정정 필수, verbatim 100% 답습 R-21 영구 의무)

> brief v1.1 = 본 §4 verbatim 100% 흡수 의무 (Phase 3 합의 R-21 답습 영구). 답습 위치 = §10 매트릭스.

### R-1 R-1 anchor 회차 부족 (현행 2 회 → 4 회 의무)

- **원인**: brief §3.1 Step 4 (9회 추가) + §4.1 Step 1 (10회 추가) 2 회만 명문. Phase 3 entry brief line 129/149/168/186 4 anchor 패턴 답습 부족.
- **정정안 verbatim**:
  - (a) §3.1 Step 4 line 115 = "Ollama daemon 상태 verify — `sha256sum /proc/3375/exe` (R-1 anchor 9회 추가, Phase 1·2·3 누계 8회 + 본 cycle (a) 1회)" → "9회" 회차 명시 보존
  - (b) §3.3 신규 Step 7 추가 = "R-1 anchor mid-cycle (R-3 답습) — 다운로드 후 verify 직전 `sha256sum /proc/3375/exe` (10회). hash 일관 ✓ 확인 후 §4 진입 자격, 불일치 시 측정 단계 skip + cycle 일시 정지 + 사용자 보고"
  - (c) §4.1 Step 1 line 161 = "Ollama 모델 unload (`/api/generate` + `keep_alive: 0`) — GPU 메모리 0 확인 (R-1 anchor 11회 추가, mid-cycle 회차)" — "10회" → "11회" 정정 + 회차 명시
  - (d) §4.3 신규 행 또는 §5 G 분기 직후 § 추가 = "R-1 anchor 종료 (R-3 답습) — 측정 직후 `sha256sum /proc/3375/exe` (12회). hash 일관 ✓"
- **답습 위치**: brief §3.1 Step 4 / §3.3 신규 Step 7 / §4.1 Step 1 / §4.3 또는 §5 G 분기

### R-2 사용자 명시 (B) bartowski 단일 source 확정 framing 부재 (`<REPO>` placeholder 고정 의무)

- **원인**: brief §2.1 매트릭스 4 후보 (A/B/C/D) + §3.2 `<REPO>` placeholder 미고정. 사용자 명시 = **(B) bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF Q4_K_M** 단일 확정 본 cycle 입력 의무.
- **정정안 verbatim**:
  - (a) §2.1 매트릭스 line 89~92 = 헤더 직후 신규 행 추가 = "**본 cycle 확정 source (사용자 명시 2026-05-25)**: (B) `bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF` Q4_K_M 단일. (A)/(C)/(D) = 본 cycle 외 fallback 후보로 NOTE 격하 ((A) unsloth = (B) 차단 시 fallback carry-over 명문)"
  - (b) §3.2 line 123/126/135 `<REPO>` placeholder 고정 = `bartowski/Qwen3-Next-80B-A3B-Instruct-GGUF`
  - (c) §3.2 `<FILE>.gguf` placeholder = HF model card 사전 verify 후 정확 파일명 사용 (Q4_K_M 단일 .gguf 또는 split shards 분기 명문)
- **답습 위치**: brief §2.1 / §3.2 / §1.3 (본 cycle 범위 한정)

### R-3 brief §3.3 Step 3 `llama-gguf` subcommand 정정 (`l` → `r`, 즉시 abort 사유)

- **원인**: brief line 146 `./build/bin/llama-gguf <FILE>.gguf l` — `l` subcommand 실 존재 0건 (`build/bin/llama-gguf` 실 usage = `data.gguf r|w [n]`, Reviewer raw cross-check 확정). 실행 시 즉시 abort.
- **정정안 verbatim**:
  - line 146 = "GGUF tensor name dump — `./build/bin/llama-gguf <ABS_FILE_PATH>.gguf r 2>&1 | head -200` (Phase 3 entry brief Step 6.5 답습 의무)" — `l` → `r` + `head -200` 추가 (전체 tensor list 출력 cap)
  - 또는 `gguf-dump.py` 동등 사용 (Phase 3 entry brief 답습)
- **답습 위치**: brief §3.3 Step 3 line 146

### R-4 R-6 framing 답습 의무 — 단정 강도 약화 + 정직성 명문

- **원인**: brief §6 #1 "광범위 community 검증" 강도 단언 + §3.3 Step 4·5 tensor name pattern 단정 framing. Phase 3 합의 R-6 (PASS/FAIL framing 금지) 답습 영구 의무.
- **정정안 verbatim**:
  - (a) §6 #1 line 224 = "HF community GGUF = 비공식 fork conversion. unsloth/bartowski 모두 active maintainer (단 본 단일 cycle 의 호환 verify 의무 답습, (i) raw finding line 158 답습 — '현행 conversion *시사* + 호환 가능성 *강함*, 단 verify 의무'). 광범위 community 검증 단언 = 본 brief 범위 외 (정직성 한계 명문)"
  - (b) §3.3 Step 4 line 147 = "tensor name pattern verify — `grep -E '(ssm_dt\.bias|ssm_dt\s)' /tmp/phase3-5-gguf-dump.log` (grep 결과 verbatim 보고, PASS/FAIL framing 금지). 분기 분류: (i) `ssm_dt.bias` 적중 = §4 진입 자격 강한 evidence / (ii) `ssm_dt` (suffix 0) 적중 = §5 B1 (format 차단) 분기 직접 발동 / (iii) 둘 다 부재 = 별도 verify cycle (다른 SSM 변형) "
  - (c) §3.3 Step 5 line 148 = (b) 와 동일 패턴 — `ssm_beta_alpha.weight` vs `ssm_ba.weight` 분기 분류 명문
- **답습 위치**: brief §6 #1 / §3.3 Step 4·5

### R-5 (g) 단독 framing 변수 분리 강도 정직성 한계 명문 + (h) carry-over 가능성 명문

- **원인**: (g) 단독 cycle = G 성공 시 자격 약한 결론 / B 차단 시 변수 분리 불가 (C-B1 답습 + Phase 3 합의 R-5 답습). brief §6 정직성 한계 명문 부족.
- **정정안 verbatim**:
  - (a) §6 신규 #18 추가 = "**(g) 단독 cycle 변수 분리 한계 (C-B1 답습 + Phase 3 합의 R-5 답습)**: 본 cycle 결과 G (성공) 시 = Ollama (간접 측정) vs llama.cpp (직접 측정) tok/s 비교 자격 강도 *약함* (format-version 차이 + conversion 차이 + quant scheme 차이 변수 미분리). B (format 차단) 시 = (g) 자체 falsification + 다른 source 또는 (h) Qwen3-30B-A3B 대조군 전환 자격 강화 (변수 분리 직접 input)"
  - (b) §1.3 line 77 직후 추가 = "❌ (g)+(h) 통합 cycle = 본 cycle 외 (사용자 명시 별도 cycle 자격, 비용 ~2× = ~96~100GB egress 비례성 평가 의무)"
- **답습 위치**: brief §6 신규 #18 / §1.3

### R-6 §5 B5 sha256 mismatch 분기 정정 (즉시 삭제 → quarantine + 사용자 명시)

- **원인**: brief §5 B5 line 216 "즉시 삭제 → 재다운로드 또는 source 변경" — false-positive 4 case (위조 / HF race / 기대값 추출 오류 / 부분 write race) 시 50GB 즉시 삭제 = 비례성 약화. 비례 보안 답습 의무.
- **정정안 verbatim**:
  - §5 B5 line 216 = "다운로드 파일 sha256 ≠ HF metadata. **즉시 quarantine 디렉토리 이동** (`mv /home/delangi/models/phase3-5/<FILE>.gguf /home/delangi/models/phase3-5-quarantine/`). rm 0건 자동 실행 금지. raw report → 사용자 명시 후 (i) 부분 write race verify (재다운로드 -c continuation) 또는 (ii) HF metadata 기대값 재verify 또는 (iii) 위조 확정 시 삭제 + 다른 source 진입 — 사용자 명시 분기 의무"
- **답습 위치**: brief §5 B5 분기

### R-7 §3.1 Step 5 huggingface-cli 미설치 분기 명문 + §3.2 옵션 분기 명문

- **원인**: brief §3.1 Step 5 line 116 = "huggingface-cli 또는 wget/curl 설치 verify (apt egress 0건 의무, 기설치 우선)". 실측 = huggingface-cli 미설치 (Reviewer raw cross-check `which huggingface-cli` = 결과 0건), wget/curl 만 존재. 미설치 시 옵션 (a) 진입 불가, 옵션 (b) 직접 진입 의무 명문 부재.
- **정정안 verbatim**:
  - (a) §3.1 Step 5 line 116 = "다운로드 도구 verify — `which huggingface-cli wget curl aria2c`. **2026-05-25 실측 = huggingface-cli/aria2c 미설치, wget/curl 만 존재 확정** (Reviewer raw cross-check). apt egress 0건 의무 (사용자 명시 의무 답습 영구, 본 cycle 자동 apt install 0건). → 옵션 (a) huggingface-cli 사용 자격 0 → 옵션 (b) wget direct 단독 사용"
  - (b) §3.2 옵션 (a) line 121 직전 NOTE = "🟡 옵션 (a) huggingface-cli = 2026-05-25 실측 미설치 → 본 cycle 사용 자격 0건. 사용 시 사전 `pip install --user huggingface_hub[cli]` 또는 apt install 의무 (= 별도 apt/pip egress + 사용자 명시 의무). 본 cycle 권고 = **옵션 (b) wget direct 단독**"
- **답습 위치**: brief §3.1 Step 5 / §3.2 옵션 (a)

### R-8 R-S1 정정 (brief §4.3 line 203 "56.3 mean" → "decode mean 7.83 ± 0.36" + 차원 분리 명문)

- **원인**: brief §4.3 line 203 = "Phase 1 답습 (cache miss 56.3 mean)" — 56.3 출처 0건 (Reviewer raw cross-check Phase 1 summary line 72/77/78/103 + `grep -rn "56.3" docs/phase0/v1-poc-raw/` = 0건). 실 Phase 1 raw = cache miss prefill 58 tok/s (line 77), decode 7.83 tok/s (line 103). F1·F2 가설 답습 시 본 cycle 비교 의도 = *decode* tok/s 비교.
- **정정안 verbatim**:
  - §4.3 line 203 = "Ollama tok/s 비교 (decode) | Phase 1 답습 (`v1-poc-raw/2026-05-24-phase1-summary.json` line 103) decode mean **7.83 ± 0.36** tok/s | 단일 시점 비교, F1 가설 검증 자격 (활성 ~3B 정확)"
  - (선택) §4.3 신규 행 추가 = "Ollama tok/s 비교 (prefill cache miss) | Phase 1 답습 (line 77) **58 tok/s ± 0.27** | 본 cycle prefill-2k prompt 적용 시 비교 가능, 단 conversion 차이 변수 미분리"
- **답습 위치**: brief §4.3 line 203 + 신규 행

### R-9 R-S2 정정 (brief §4.2 prompt 파일 절대 경로 의무, 즉시 abort 사유)

- **원인**: brief line 168 `cd /home/delangi/src/llama.cpp` + line 173/185 `-f docs/phase0/v1-poc-raw/phase3/phase1-prompt-*.txt` 결합 시 실 path = `/home/delangi/src/llama.cpp/docs/phase0/...` (= 존재 0건 확정, Reviewer raw cross-check). 실 prompt 파일 = `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-*.txt`. 실행 시 즉시 abort.
- **정정안 verbatim**:
  - line 173 = `-f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt"` (한국어 path 큰따옴표 인용 의무)
  - line 185 = `-f "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt"` (동상)
- **답습 위치**: brief §4.2 line 173·185

### R-10 brief §4.2 prompt 파일명 vs 실 토큰 수 (`decode-161tok.txt` = 153 tokens) 정직성 명문

- **원인**: brief line 173 prompt 파일명 `decode-161tok.txt` vs 실 detokenize 결과 = 153 tokens (Phase 3 summary line 69 `decode-161tok.tokens: 153`). 파일명 "161tok" = Ollama context length 답습 (`prompt_eval_count: 161`, raw decode JSON), llama.cpp re-tokenize 시 153. 8 tokens 격차 = tokenizer 변형 (BOS/EOS/special token 처리).
- **정정안 verbatim**:
  - §4.2 line 170 직전 NOTE 추가 = "🟡 **prompt 파일명 vs 실 토큰 수 격차 (정직성 명문)**: `phase1-prompt-decode-161tok.txt` 파일명 = Ollama re-tokenize (161) 답습, llama.cpp re-tokenize = **153 tokens** (Phase 3 summary line 69 답습). 8 tokens 격차 = BOS/EOS/special token 처리 변형. 본 cycle = 동일 prompt text 답습 의무 (파일 내용 일치), tok/s 비교 시 *token 수 차이* 정직성 명문 의무 (분모 token 수 = llama.cpp re-tokenize 결과 사용)"
- **답습 위치**: brief §4.2 prompt 명령 직전 NOTE

### R-11 brief §1.1 "egress ~50GB" vs §2.1 매트릭스 "~48GB" + §6 #5·#6 정정 (R-S4 verbatim)

- **원인**: §1.1 line 58 ~50GB + §2.1 line 89~92 ~48GB + §6 #5 line 228 "50GB egress = 5×" + §6 #6 line 229 "82% → 87%" 격차. Reviewer raw cross-check `ollama_gguf_size_GiB: 48.18` 답습.
- **정정안 verbatim**:
  - §1.1 line 58 추가 = "egress ~48~50GB (HF lfs `Content-Length` 사전 verify 의무, raw = ~48.18 GiB 답습)"
  - §6 #5 line 228 정정 = "egress 비례성 — ~48~50GB egress = 본 프로젝트 단일 cycle 최대 (Phase 1 HF egress ~10GB 의 4.8~5×) — 비례성 평가 답습"
  - §6 #6 line 229 정정 = "디스크 비례성 — ~48GB 디스크 사용 = ~82% → ~84.6% 임시 증가 (50GB / 1.9TB ≈ 2.6pp, A-rec-2 답습)"
- **답습 위치**: brief §1.1 / §6 #5·#6

---

## 5. 권고 (Strong recommendation, brief v1.1 흡수 자격 평가)

### R-rec-1 `llama-bench` carry-over (C-B3 격하)

본 cycle = `llama-cli` 단독 자격 유지 (Phase 3 §2.3 답습). `llama-bench` (자동 통계, 재현성 강화) = (j) advisory cycle 또는 별도 정확성 cycle 입력 자격.

### R-rec-2 quant 비교 매트릭스 carry-over (C-B4 격하)

본 cycle = Q4_K_M 단독 (비례성). Q5_K_M / IQ4_XS / Q6_K 비교 = 별도 cycle (egress ~150~200GB 누적, 비례성 평가 의무).

### R-rec-3 GPU thermal polling 추가 (C-B7 격하)

§4.3 측정 항목 추가 = `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` polling (R-23 답습 보강, 5분 이상 연속 측정 thermal throttling 정직성 명문). 본 cycle 측정 = 2 prompt × ~1~5분 = thermal risk 낮음 단정 vs polling 정직성 명문 자격 평가.

### R-rec-4 §3.3 Step 4·5 사이 `block_count` verify step 추가 (A-rec-7 답습)

GGUF metadata `qwen3next.block_count` (Qwen3-Next-80B-A3B = 48 layer 가정) verify step 추가 → `-ngl 48` 정합 사전 확인 (Phase 3 entry brief R-25 답습).

### R-rec-5 §3.0 의도-외 egress 거버넌스 신규 추가 (C-B5 격하)

Phase 3 entry brief §3.0 패턴 답습 의무 — apt/pip 등 의도-외 egress 사전 차단 거버넌스. 본 cycle wget direct 단독 사용 시 의존성 0 → §3.0 신규 추가 자격 평가 (필요 시 brief v1.1 §3.0 신규).

### R-rec-6 §9 v1→v1.1 변경 일람 신규 추가 (C-B5 격하)

Phase 3 entry brief v1.1 패턴 답습 — BLOCKING 11 verbatim 흡수 위치 명문 + R-rec1~6 흡수 자격 명문.

### R-rec-7 Phase 3.5 명명 충돌 (g)/(h) → "Phase 3.5-A/B" 권고 (A-S1 격하)

본 cycle = (g) "Phase 3.5" 단독 호칭 유지 자격, (h) 진입 시점 = "Phase 3.5-B" 또는 별도 명명 자격 평가 (사용자 명시 별도 cycle).

---

## 6. NOTE (정직성 보존, 본 합의 외 별도 cycle 또는 carry-over)

| NOTE | 내용 |
|------|------|
| N-1 | ADR-011 §2.1 5조건 본 cycle 미진입 정합 (결정 *고정* 0건). 본 cycle 측정 raw = 향후 결정 *고정* cycle (k) 의 5조건 평가 input 자격 carry-over (Phase 3 합의 N-1 답습) |
| N-2 | Provider Liquidity finding 강화 — 본 cycle G 결과 ≠ 본문 정정 자격 (별도 cycle 의무 답습 영구). 본 cycle 의 (B) bartowski single source = "다른 GGUF source 도 호환 가능성 시사" evidence 입력 only |
| N-3 | M3·M4 결정 *고정* 자격 무관 (R-9 답습 영구) — 본 cycle = 측정 시도 + raw report 한정 |
| N-4 | MVP-1 합의 R4 본문 정정 자격 무관 — 본 cycle = input only, 본문 정정 = 헌법급 별도 cycle |
| N-5 | C-H1 (Ollama 자체 fork conversion 가설) / C-H2 (F2 간접 input 한정 가설) / C-H3 (HF perplexity vs Ollama 가설) = (i) raw finding line 137 답습 강화, 본 cycle 외 별도 가설 검증 cycle |
| N-6 | C-H4 (GB10 Gated DeltaNet kernel 미지원 가설) = Phase 3 합의 R-5 답습 강화. (h) Qwen3-30B-A3B 대조군 cycle 입력 자격 강화 (sm_120/121 + Gated DeltaNet 변수 분리) |
| N-7 | C-H5 (raw report → MVP-1 R4 framing 강화/약화 evidence) = 본 cycle G/B 분기별 input 자격. 자동 R4 본문 정정 0건 영구 답습 |
| N-8 | aria2c 미설치 (C-B6 격하) — 본 cycle 50GB 단일 다운로드, multi-connection 가속 자격 평가 비례성 약함. 별도 large-scale egress cycle 시 재평가 자격 |
| N-9 | (g)+(h) 통합 cycle 자격 = 사용자 명시 별도 cycle (~96~100GB egress, 비례성 평가 의무) |
| N-10 | §6 #17 "atomic commit" framing vs §0 #11 "자동 진입 0건" framing = 별도 차원 보존 자격 (B-S3 격하). 본 합의 통합 0건. |
| N-11 | brief 자체 머신 변경 0건 = (i) raw finding + Phase 3 entry brief 답습 영구 의무. 본 합의 자체 머신 변경 0건 답습 영구. |

---

## 7. 기각 (자격 평가 후 본 합의 제외)

| 기각 항목 | 사유 |
|---|---|
| C-B2 (MLC-LLM / llamafile / HF mirror 후보 누락) | 본 cycle = (B) bartowski 단일 source 사용자 명시. 다른 inference engine = 별도 Provider Liquidity 답습 cycle (Phase 3 N-9 답습) |
| C-S1 (j) advisory 우선 + (g) 보류 대안 | 사용자 명시 = (g) 직접 진입 확정. 본 합의 자격 외 |
| C-S2 (g)+(h) 통합 cycle 대안 | N-9 carry-over 자격, 본 cycle 외 |
| B-S3 §6 #17 vs §0 #11 framing 통합 | N-10 답습, 별도 차원 보존 자격 (본 합의 통합 0건) |
| A 단독 권고 일부 (예: A-rec-1 trace ID anchor) | 본 cycle scope 외 (Phase 3 R-23 답습 영구) |

---

## 8. 후속 carry-over 매트릭스

| 후보 | 우선순위 | 비고 |
|---|---|---|
| (g) Phase 3.5 brief v1.1 보강 + commit | **본 cycle 직후 의무** | BLOCKING 11 verbatim 100% + R-rec 흡수 자격 평가, 사용자 명시 후 |
| (g) 실 다운로드 + verify + 측정 실행 | 사용자 명시 *직접* 의무 | brief v1.1 commit 후 + (B) bartowski 50GB egress 사용자 명시 후 |
| (h) Phase 3.5 Qwen3-30B-A3B 대조군 | MEDIUM | 본 cycle 무관 진행 가능, 변수 분리 강화 (R-5 답습) |
| (j) advisory wall-clock 측정 | MEDIUM | 본 cycle 무관 진행 가능 |
| (k) M3·M4 결정 *고정* | DEFER | 본 cycle G 결과 input 자격 강화 (단 (iii)(iv) 직접 evidence 의무 답습 영구) |
| (l) MVP-1 트랙 B 구현 | DEFER | (k) 통과 의무 답습 영구 |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| Phase 3 summary recommendation C 정정 | LOW | (i) raw finding 후속, 별도 cycle |
| (g1-O') / (g1-O) / (P3) / R-S3 gov §1.1 | MEDIUM | 별도 시리즈 답습 |
| `llama-bench` carry-over (R-rec-1) | LOW | (j) 또는 별도 정확성 cycle 입력 자격 |
| quant 비교 매트릭스 carry-over (R-rec-2) | LOW | egress 비례성 평가 의무 |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime** | ❌ **자동 진입 명백 부정** | **chain 영구 종결 의무 답습 영구** ((g1-N-3-adr-008+sip+adr-012') 발효 영구) |

---

## 9. 정직성 한계 (본 합의 자체)

1. **본 합의 = brief v1 → v1.1 진입 게이트 한정** — 실 다운로드/측정/M3·M4 결정 *고정* 자격 평가 0건
2. **Reviewer raw cross-check 범위** — `llama-gguf --help` 직접 실행 + Phase 1·3 summary JSON 직접 read + prompt 파일 존재 verify + `which` 도구 verify. 다른 line-level 누락 가능
3. **BLOCKING 11 verbatim 답습 의무** 자체가 brief v1.1 *실 정정* 자격을 부여하지 않음 — 사용자 명시 후 commit 별도
4. **R-S1~R-S4 단독 격상 자격 평가** = Reviewer 1인 판단, 다른 Agent 의 single round 외 검증 0건 (Phase 3 합의 R-S 패턴 답습 영구)
5. **(B) bartowski source 정합성 verify 0건** — README/model card 직접 read 0건 (사용자 명시 후 사전 verify 의무, brief §2.2 답습)
6. **HF egress = 본 합의 자체 0건** — `curl -sI` 사전 verify 0건, 사용자 명시 후 brief §2.2 실행 의무
7. **Phase 3 entry brief 답습 정확성** = line 129/149/168/186 4 anchor 추정 기반, 실 line# verify 0건 (단 4 anchor 사실 = grep 확인 완료)
8. **본 합의 자체 머신 변경 0건** — commit/push 0건, working tree 변경 0건 (본 합의 보고서 파일 신규 추가 1건만)

---

## 10. 변경 일람 (brief v1.1 보강 의무 매트릭스)

| BLOCKING/권고 | brief 정정 위치 | verbatim 본문 (요약) |
|---|---|---|
| R-1 R-1 anchor 4 회 | §3.1 Step 4 (line 115) / §3.3 신규 Step 7 / §4.1 Step 1 (line 161) / §4.3 또는 §5 G 신규 행 | 회차 9/10/11/12 명시 + 회차 번호 + cycle 일시 정지 분기 |
| R-2 (B) bartowski 확정 | §2.1 신규 헤더 행 / §3.2 `<REPO>` 고정 (line 123/126/135) / §3.2 `<FILE>.gguf` model card verify | (B) 단일 + (A)/(C)/(D) fallback NOTE |
| R-3 `llama-gguf l→r` | §3.3 Step 3 (line 146) | `r` + `head -200` + Phase 3 entry brief Step 6.5 답습 명문 |
| R-4 R-6 framing | §6 #1 (line 224) / §3.3 Step 4·5 (line 147·148) | 단언 강도 약화 + grep 결과 verbatim + 3 분기 분류 |
| R-5 (g) 변수 분리 정직성 | §6 신규 #18 / §1.3 line 77 직후 | (g) 단독 자격 약함 명문 + (g)+(h) 통합 carry-over |
| R-6 sha256 mismatch quarantine | §5 B5 (line 216) | quarantine 이동 + rm 0건 + 사용자 명시 분기 |
| R-7 huggingface-cli 미설치 | §3.1 Step 5 (line 116) / §3.2 옵션 (a) (line 121 직전) | 실측 미설치 + 옵션 (b) wget 단독 |
| R-8 56.3 → 7.83 정정 | §4.3 (line 203) + 신규 행 | decode 7.83 ± 0.36 + (선택) prefill cache miss 58 |
| R-9 prompt 절대 경로 | §4.2 (line 173·185) | 절대 path + 한국어 큰따옴표 인용 |
| R-10 161tok vs 153 tokens | §4.2 line 170 직전 NOTE | 8 tokens 격차 정직성 + 분모 명문 |
| R-11 50GB vs 48GB | §1.1 line 58 / §6 #5 line 228 / §6 #6 line 229 | ~48~50GB 범위 + 84.6% 정확값 |
| R-rec-1 `llama-bench` carry-over | §8 carry-over | (j) 또는 별도 cycle 입력 자격 |
| R-rec-2 quant 비교 | §8 carry-over | 별도 cycle 비례성 |
| R-rec-3 GPU thermal polling | §4.3 신규 행 자격 | `nvidia-smi temperature.gpu` polling |
| R-rec-4 block_count verify | §3.3 Step 4·5 사이 신규 | `qwen3next.block_count = 48` verify |
| R-rec-5 §3.0 신규 | §3 시작 직전 | 의도-외 egress 거버넌스 |
| R-rec-6 §9 v1→v1.1 일람 | brief 말미 신규 §9 | BLOCKING 흡수 위치 |
| R-rec-7 Phase 3.5 명명 | §1.3 line 77 직후 | 본 cycle = "Phase 3.5" 유지 자격 |

---

## 11. Reviewer 권한 한계 (답습 영구 의무)

1. ❌ brief v1.1 갱신 / brief 파일 직접 수정 / commit·push (사용자 명시 별도 의무)
2. ❌ 실 다운로드 / 빌드 / 측정 / sudo 실행 / Ollama 데몬 변동 / 모델 pull / config 변경
3. ❌ M3·M4 결정 *고정* (Phase 1+2+3+3.5 종합 합의 cycle 별도)
4. ❌ MVP-1 합의 R4 본문 정정 / 헌법 5조-2 / ADR-011 본문 정정 (Provider Liquidity finding input only)
5. ❌ 메모리 자동 갱신 (사용자 명시 의무)
6. ❌ (h)/(j)/(k)/(l)/(m)/(n) 자동 진입 (사용자 명시 의무 답습 영구)
7. ❌ Phase 3 summary recommendation C 자동 정정
8. ❌ 다른 inference engine 후보 외부 식별 cycle (egress 0 답습)
9. ❌ Qwen3-30B-A3B 대조군 cycle 진입 ((h) 별도 brief)
10. ❌ `OllamaBoss`·`LlamaCppBoss`·`vLLMBoss` 코드 (트랙 B 별도)
11. ❌ 보안 거버넌스 자동 재개 (비례성 답습 영구)
12. ⚠️ 신규 sub-boundary 신설 자격 = 본 합의 1회 한정 평가 — 본 합의 신설 0건 (Reviewer 권한 한계 (1)~(11) 답습 영구 유지)

---

## 12. 답습 요약 (영구)

- **하는 것**: brief v1 진입 자격 평가 + BLOCKING 11 + 권고 7 + NOTE 11 + R-S1~R-S4 4 + 기각 5 식별 + brief v1.1 보강 매트릭스 명문 + 다음 단계 권고
- **하지 않는 것**: brief v1.1 갱신·commit·push / 실 다운로드·측정 / M3·M4 결정 *고정* / Ollama 위생 정정 trigger 발효 / MVP-1 R4 본문 정정 / 헌법·ADR 본문 정정 / 메모리 자동 갱신 / 후속 cycle 자동 진입 / chain 영구 종결 의무 (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 0
- **출처**: brief v1 (`0867fee`) / (i) raw finding (`52749ce`) / Phase 3 entry brief (`25eb008`) / Phase 3 합의 (`e76acc8`) / Phase 3 summary (`2026-05-24T04-36-phase3-summary.json`) / Phase 1 summary (`2026-05-24-phase1-summary.json`) / `llama-gguf --help` 실측 / `which` 실측 / Phase 3 entry brief R-1~R-25 답습 / Agent A·B·C 독립 분석 / 헌법 5조-2 (line 75~80) / ADR-011 §2.1 5조건 / 메모리 (provider_liquidity / staged_consensus_workflow / proportionate_security_personal_tool / jarvis_local_boss_direction / minimize_user_intervention / actual_run_trigger_paths_filter)

---

**Reviewer 최종 권고**: Phase 3.5 (g) entry brief v1 = **APPROVE w/ COND, BLOCKING 11 (R-1~R-11) + 권고 7 (R-rec-1~7) + NOTE 11 + Reviewer 단독 격상 R-S1~R-S4 + 기각 5**. brief v1 → v1.1 보강 (BLOCKING 11 verbatim 100% R-21 답습 영구 + Reviewer 단독 격상 R-S1~R-S4 흡수) 후 사용자 명시 다음 단계 (다운로드 실행 또는 보류) 진입 자격. **단계별 명시 승인 답습 영구** (brief v1.1 commit → 사용자 검토 → 실 다운로드 → verify → 측정 → raw report → 합의 → commit·push, 자동 다음 단계 0건). R-6 framing + 비례 보안 + Provider Liquidity + staged consensus + chain 영구 종결 5중 답습 의무.
