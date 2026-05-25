# Jarvis MVP-1 V-1 PoC Phase 3.5-O (h-O) entry brief (v1.1, Ollama qwen3:30b-a3b-instruct-2507-q4_K_M 직접 측정 cycle, 풀 3+1 합의 APPROVE w/ COND 반영)

> **본 brief v1.1 = (h-O) Phase 3.5-O Ollama 직접 측정 cycle entry brief v1 (`61cb005`, 377줄) 의 풀 3+1 합의 (`37bcd40`, 459줄, APPROVE w/ COND + BLOCKING 14 + R-S1~R-S5 + 권고 17 + NOTE 17 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 14 verbatim 100% 반영 (R-21 답습 영구 의무) / (2) R-S1~R-S5 정정 흡수 11곳 (§2.1 line 110 + §1.3 + §3.0 line 125 + §3.1 신규 2 step + §4.2 line 178 + §4.3 line 213 + §9.3 line 360 + §6 신규 3 항목) / (3) 강한 권고 흡수 (R-rec-3 / R-rec-6 / R-rec-13 / R-rec-14 / R-rec-15 / R-rec-16) / (4) §11 v→v1.1 변경 일람 신규 작성 ((h) R-rec-6 답습) / (5) 본문 변경 0 머신 변경 (pull/측정/sudo 0). 본 brief = entry plan only, 실 변경 = 본 brief v1.1 commit + push 만. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-O (h-O) 풀 3+1 합의 commit `37bcd40` 직후, 본 cycle 단계 (3) brief v1.1 보강)
**카테고리**: V-1 PoC Phase 3.5-O (h-O) entry brief v1.1 (Phase 3 carry-over (h) R-S1 발효 직접 후속, 본 cycle 핵심 = **inference engine 변수 *부분* 분리** — (h) llama.cpp ↔ (h-O) Ollama 1:1 동일 모델 동일 quant 동일 prompt 동일 hardware 비교, 단 source conversion lineage 변수 *추가* 미통제 정직성)
**범위**: (1) Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` pull 절차 (egress 격리, ~18GB) / (2) Ollama /api/generate 측정 절차 (Phase 1 답습 + decode + prefill-2k cold 측정 우선) / (3) 분기 (G·B1~B6) / (4) (h) llama.cpp vs (h-O) Ollama 1:1 비교 framing (inference engine 변수 *부분* 분리 핵심) / (5) 후속 carry-over (h-OM Ollama Modelfile cycle 신규 MEDIUM)

**답습 권위**:
- **Phase 3.5-O (h-O) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-v1-poc-phase3-5-h-o-ollama-direct-entry.md`, commit `37bcd40`, 459줄, BLOCKING 14 + R-S1~R-S5 + 권고 17 + NOTE 17 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
- (h) Phase 3.5-B cycle 정리 commit (`fccec6a`, SESSION 15번째 entry, F-1 classical MoE > SSM hybrid 1.44~2.19× + R-1 anchor 16회)
- (h) brief v1.1 (`de0326b`, 467줄, BLOCKING 13 + R-S1~R-S5 흡수)
- (h) 풀 3+1 합의 (`d74d205`, 491줄)
- (g) Phase 3.5 cycle 정리 commit (`b3d4164`, 14번째 entry)
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`)
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`) — qwen3-coder-next decode 7.83 ± 0.36 / Phase 1 raw `eval_count/eval_duration ≈ 7.11` vs summary `decode_tok_per_sec: 7.926` ~11% 격차 (R-S2 답습 영구)
- (h) raw measurement (`docs/phase0/v1-poc-raw/phase3-5-h/*`) — decode 49.6 / prefill 45.4 t/s 직접 input
- MVP-1 합의 R4 "llama.cpp ↔ Ollama 동급" — input only (R-9 답습 영구)
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter` / `project_mvp_staged_roadmap`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` (model blob digest `78b329e716e7` prefix, manifest UI commit `19e422b02313`) pull 절차 명문 — egress 격리·blob verify·R-1 anchor 17회 답습 + (h) 누계 16회 후속
2. Ollama /api/generate 측정 절차 명문 — Phase 1 답습 + decode + prefill-2k **cold 측정 우선** ((h) llama.cpp `--no-warmup` 답습 비대칭 정직성, R-S3 발효 영구)
3. 분기 조건 명문 — G 성공·B1 pull 실패 (404 model tag 부재 단독)·B2 Ollama runtime 에러·B3 network·B4 디스크·B5 quarantine·**B6 tokenizer 분모 mismatch** (R-S3 / B-B5 발효 신규)
4. 정직성 한계 명문 20 항목 (§6) — inference engine 변수 *부분* 분리 자격 + 5 미통제 변수 (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이 + **source conversion lineage R-S1 발효 추가**) + tok/s 분모 정직성 + prefix cache hit 비대칭 정직성
5. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
6. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구 + **(h-OM) Ollama Modelfile (h) GGUF 직접 등록 cycle 신규 MEDIUM carry-over** (R-S1 발효)
7. (h) 결과 대비 비교 framing 명문 (§9) — inference engine 변수 *부분* 분리 핵심 가치 + 시나리오 5 + prefill 분리 시나리오 5 (R-rec-15 발효 신규)
8. v1 → v1.1 변경 일람 (§11) — BLOCKING 14 + R-S 5 + 권고 17 흡수 매트릭스 ((h) R-rec-6 답습)

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 pull / 측정 / sudo 실행** — 본 brief = entry plan only
2. ❌ **Ollama daemon 상태 변경 (pid 3375)** — keep_alive 0 unload 만, R-1 anchor hash baseline `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` (full 64자) 일관 보존 (R-rec-11 답습)
3. ❌ **(h) GGUF 파일 변경** — `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` 보존 (R-13 답습 영구)
4. ❌ **(g) GGUF 파일 변경** — `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` 보존 (R-13 답습 영구)
5. ❌ **llama.cpp HEAD `c0c7e147` 변경** — (h) 측정 baseline 보존
6. ❌ **MVP-1 합의 본문 자동 정정** — R4 framing input only (R-9 답습 영구)
7. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
8. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
9. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
10. ❌ **메모리 자동 갱신** — 사용자 명시 의무
11. ❌ **(h-OM)/(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
12. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
13. ❌ **Ollama pull 시점 = 사용자 명시 *직접* 의무** — ~18GB egress + 디스크 누계 ~80GB 비례성 답습 (R-11)
14. ❌ **(g)+(h)+(h-O) 통합 본문 정정** — 본 cycle = (g)/(h) 와 *독립* 별개 cycle 단독 진행, (g)/(h) brief/합의 본문 변경 0건 ((g)+(h)+(h-O) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle, 별도 차원 carry-over)
15. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) prime/super-prime 자동 진입** — chain 영구 종결 의무 답습 영구 (R-13 (B-B8) 발효)

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **Phase 3.5-B (h) cycle 완료** (`fccec6a`, SESSION 15번째 entry):
  - F-1 ⭐⭐⭐: classical MoE > SSM hybrid 모든 측정 차원 1.44~2.19× (decode 32.3→**49.6** / prefill 31.5→**45.4** / decode prompt 177.9→**389.4** / prefill prompt 971.9→**1916.8** t/s)
  - F-2 ⭐⭐⭐: SSM 미포함 가설 확정 (raw grep 0 적중 + n_tensors 579)
  - F-6 ⭐: Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` 실재 ✓ (blob `78b329e716e7`)
  - **(h) 풀 3+1 합의 R-S1 ⭐⭐⭐ CRITICAL 발효 직접 carry-over** = brief §4.3 line 225 "Ollama 동일 모델 0건" 단언 정면 부정 → (h-O) Ollama 직접 측정 cycle 신규 HIGH carry-over 발효
- **본 cycle 핵심 가치 = inference engine 변수 *부분* 분리** (R-S5 발효 약화 framing):
  - (h) Qwen3-30B-A3B-Instruct-2507 Q4_K_M + llama.cpp `c0c7e147` 직접 = decode **49.6** t/s / prefill **45.4** t/s
  - (h-O) 동일 모델 + 동일 quant + 동일 prompt + 동일 hardware (GB10) + Ollama 직접 = decode X t/s / prefill Y t/s
  - → 1 차원 변경 (inference engine: llama.cpp ↔ Ollama) = **본 프로젝트 *부분* 변수 분리 시도** (단 5 미통제 변수 + R-S1 source conversion lineage 변수 추가 미통제, "최초 단일 변수 분리" 단언 0건)
- **Phase 1 F2 가설 결정적 input** = (h) F-1 + (h-O) F-1 종합 → MVP-1 R4 framing 강화/정정 자격 강한 evidence (단 본문 정정 별도 cycle R-9 답습 영구)
- **본 cycle 비용**: egress **~18GB** (Ollama pull, (h) ~17.353 GiB 답습 비용 동일) + 디스크 **~18GB** 임시 사용 + (g)+(h)+(h-O) 누계 ~80GB 디스크

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | Ollama pull `qwen3:30b-a3b-instruct-2507-q4_K_M` 성공 가능? | Y/N + `ollama pull` stdout/stderr + `ollama list` 직접 verify |
| **Q2** | Ollama decode/prefill tok/s = ? | Phase 1 답습 measurement protocol, **cold 측정 우선** (R-S3 답습 — warm = prefix cache hit 효과 분리 framing 의무) |
| **Q3** | (h) llama.cpp 49.6 t/s vs (h-O) Ollama X t/s 격차 = ? | 1 차원 변경 (inference engine) — 단 R-S1 발효 source conversion lineage 추가 미통제 (Ollama blob `78b329e716e7` ≠ (h) bartowski sha256 `382b4f5a164d...`) |
| **Q4** | Phase 1 F2 가설 (~4.07× Ollama 느림) 답습 vs 정정? | (h) decode 49.6 / (h-O) decode X 비율 직접 evidence (단 model 차이 미해소 — Phase 1 = qwen3-coder-next SSM hybrid 80B, 본 cycle = Qwen3-30B-A3B-Instruct-2507 classical MoE) |
| **Q5** | F-2 가설 (Ollama 효율성 = format-internal 차이) 답습 vs 정정? | (h-O) tok/s 결과 → Ollama 자체 효율성 정직성 명문, 단 inference engine 변수 *부분* 분리 자격 강함 |
| **Q6** | Provider Liquidity finding 강화 자격? | (h) F-1 + (h-O) F-1 종합 input HIGH (단 본문 정정 별도 cycle 의무 R-9 답습) |

### 1.3 본 cycle 범위 한정 (R-S1 발효 — O vs O-modelfile 결정 자격 명문 + R-rec-7 답습)

- ✅ 단일 모델 (Qwen3-30B-A3B-Instruct-2507 Q4_K_M, Ollama library version)
- ✅ **본 cycle source = O (library `qwen3:30b-a3b-instruct-2507-q4_K_M`) 단일 확정 (사용자 명시 답습)**, 단 **O-modelfile 대안 평가 = 사용자 명시 별도 결정 자격** ((h) GGUF Modelfile 직접 등록 = bartowski conversion lineage 100% 통제 + egress 0 + (h) ↔ (h-O-library) ↔ (h-OM) 3-way 비교 framing, R-S1 발효 + R-rec-16 발효 §8.2 MEDIUM 격상)
- ✅ 단일 measurement cycle — decode + prefill-2k 2 prompt **cold 측정 우선** ((g)/(h) 답습, Phase 1 답습), warm 측정 = 별도 단계 (cache hit 효과 분리 framing 의무, R-S3 발효)
- ✅ 명명 = "Phase 3.5-O" 채택 — 독립 cycle 단독 진행 + Phase 3.5 family 하위 (R-rec-7 답습)
- ❌ (h) llama.cpp 답습 = (h) cycle 완료 (변경 0건)
- ❌ (g) SSM hybrid 답습 = (g) cycle 완료 (변경 0건)
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **(h-OM) Ollama Modelfile 직접 등록 cycle = (R-S1 발효) MEDIUM 격상 신규 carry-over** (본 cycle 외, 사용자 명시 별도 cycle 의무 답습)
- ❌ **(g)+(h)+(h-O) 통합 본문 정정 cycle = 본 cycle 외** ((g)/(h) brief/합의 본문 변경 0건 답습 영구)
- ❌ **(g)+(h)+(h-O) 통합 *분석* cycle** ≠ 통합 *본문 정정* cycle = 별도 차원 carry-over (N-12 답습)
- ❌ MVP-1 R4 framing 본문 정정 cycle = 별도 cycle (R-9 답습 영구)
- ❌ 다른 quant (Q5_K_M / IQ4_XS / Q6_K) = 별도 cycle (R-rec-2 carry-over)
- ❌ Ollama API 외 다른 측정 도구 = 별도 cycle (llama-bench R-rec-12 격상 후보 답습)

---

## 2. 모델 source — Ollama library 직접 확정 (R-S1 발효 직접 명문)

### 2.1 본 cycle 확정 source (사용자 명시 2026-05-25 + (h) Agent C WebSearch raw verify + R-S1 발효)

> **본 cycle source = Ollama library `qwen3:30b-a3b-instruct-2507-q4_K_M` 단일 확정** (Agent C WebFetch raw verify 답습 — **model blob digest 8 octet prefix `78b329e716e7`** + manifest UI commit identifier `19e422b02313`, downloads 19.3M). (h) brief WebSearch raw verify 답습 정합 ✓. **R-S1 발효 정직성** = Ollama library blob `78b329e716e7` (8 octet prefix) ≠ (h) bartowski sha256 `382b4f5a164d200f93790ee0e339fae12852896d23485cfb203ce868fea33a95` (full 64자) = **다른 source 자격 강한 시사** (8 octet vs 64 octet 비교 자격 불완전, 단 prefix 다름 = 다른 blob).

| # | source | Ollama tag / 식별자 | 비고 |
|---|---|---|---|
| **O** | **Ollama library** | **`qwen3:30b-a3b-instruct-2507-q4_K_M`** (model blob digest prefix `78b329e716e7`, manifest UI commit `19e422b02313`) | **✅ 본 cycle 확정 (사용자 명시 + R-S1 raw verify 답습)** |
| O-alt | Ollama library | `qwen3:30b-a3b` (default tag, blob `ad815644918f` ≠ Instruct-2507 `78b329e716e7`) | NOTE: **다른 model variant 확정** (Agent C WebFetch raw verify) — 본 cycle source 답습 0건, 사용자 명시 별도 cycle |
| **O-modelfile** | **(h) GGUF Modelfile 직접 등록** | `FROM /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` | **R-S1 발효 (h-OM) MEDIUM carry-over** — **bartowski conversion lineage 100% 통제 + egress 0 + (h) ↔ (h-O-library) ↔ (h-OM) 3-way 비교 framing 자격 강함**. 사용자 명시 별도 cycle 결정 자격 강함 (단순 NOTE 격하 자격 약함) |

### 2.2 source 사전 verify 의무

1. **Ollama daemon 상태 verify**: `curl -s http://127.0.0.1:11434/api/version` → version 답습 / `ollama list` → 기 다운로드 model 확인 (2026-05-25 직접 verify 결과 = `qwen3:30b-a3b-instruct-2507-q4_K_M` 기 다운로드 0건 → pull 필요)
2. **Ollama library blob verify (사전 verify 의무 강화)**: pull *전* `curl -sI https://registry.ollama.ai/v2/library/qwen3/manifests/30b-a3b-instruct-2507-q4_K_M` 직접 verify 의무 (사용자 권한 0 시 step skip + 정직성 명문). 404 시 B1 분기 즉시 trigger framing
3. **R-1 anchor 17회 추가** (mid-cycle 회차, pull *전* R-1 anchor + (h) **누계 16회** 후속 ((h) summary line 72 `cumulative_total: 15` + 본 cycle (h-O) 사전 1회 = 16회 누계, 본 cycle 17·18·19·20회 추가 = 본 cycle 종료 시 누계 20회), R-3 답습)
4. **(h) 답습 정합성 사전 framing** — Ollama library version GGUF 가 (h) bartowski Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf 와 *다른 source* 자격 R-S1 발효 명문 정합 (Ollama hub 자체 conversion 또는 다른 bartowski release, manifest digest cross-check 의무)

---

## 3. Ollama pull 절차

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습) + sudo 사용 명문 정정 (R-S4 발효)

본 cycle egress = Ollama pull only. **apt install / pip install / git clone / HF egress 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구 (R-7 격리 답습). 본 cycle 도구 = `ollama pull` 단독 (Ollama daemon pid 3375 채널).

**본 cycle sudo 사용 (R-S4 발효 명문 정정 — (h) raw summary 5회 답습)**:
- §3.1 Step 1 (egress baseline pre, 1회) + Step 4 (R-1 anchor 17x, 1회) + §3.3 Step 4 (R-1 anchor 18x, 1회) + §3.3 Step 5 (egress baseline post-pull, 1회) + §4.1 Step 1 (R-1 anchor 19x, 1회) + §4 측정 종료 직후 (R-1 anchor 20x, 1회) + §3.1 신규 Step (cache directory verify, 1회) = **최소 5~7회 sudo 호출 예상**
- 사용자 명시 임시 비밀번호 의무 답습 ((h) `sudo_authorization` 답습 영구)

### 3.0.1 (g)/(h) GGUF 보존 정책 사용자 명시 의무 (R-13 답습)

(g) `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` (45.38 GiB) + (h) `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (17.353 GiB) 보존 답습 영구 (사용자 명시 (h) cycle 6차 세션 답습). 본 (h-O) cycle Ollama models cache = 별도 위치 (~/.ollama/ 가설), (g)/(h) GGUF 영향 0건. **cleanup = `rm` 자동 실행 0건** (비례 보안 답습).

### 3.1 사전 조건 (egress 격리, R-7 답습, (h) §3.1 답습 + R-S4 발효 2 신규 step)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot, 사용자 명시 임시 비밀번호 의무 답습) | `/tmp/phase3-5-h-o-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-h-o-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-h-o-disk-pre.txt` |
| 4 | **R-1 anchor 17회 추가** — `sudo sha256sum /proc/3375/exe` ((h) 누계 16회 + 본 cycle (h-O) 사전 1회, 17번째 회차, hash baseline `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` (full 64자) 일관 답습 영구, R-rec-11 발효) | `/tmp/phase3-5-h-o-r1-anchor-17x.txt` |
| 5 | Ollama daemon status verify — `curl -s http://127.0.0.1:11434/api/version` + `ollama list` (기 다운로드 verify) | `/tmp/phase3-5-h-o-ollama-status.txt` |
| 6 | GPU + memory verify — `nvidia-smi` (idle) | `/tmp/phase3-5-h-o-gpu-pre.txt` |
| **7 [R-S4 신규]** | **Ollama embedded llama.cpp version verify** — `ollama --version` + `curl -s http://127.0.0.1:11434/api/version` response 의 embedded llama.cpp version 추출 (가능성 평가) 또는 Ollama release note cross-check. 미노출 시 §6 #4 정직성 한계 강화 의무 ((h) llama.cpp HEAD `git rev-parse HEAD c0c7e147` 답습 직접 verify 비례) | `/tmp/phase3-5-h-o-embedded-llamacpp-version.txt` |
| **8 [R-S4 신규]** | **Ollama models cache directory + 권한 사전 verify** — `ls -la ~/.ollama/models/manifests/ 2>&1 \|\| ls -la /usr/share/ollama/.ollama/models/manifests/ 2>&1` + `stat -c '%U %G %a' <cache_dir>` + `df -h $(readlink -f <cache_dir>)` 직접 verify. cache 위치 default 가설 분기 (user-local `~/.ollama/` vs systemd-service `/usr/share/ollama/`) 분리 명문 | `/tmp/phase3-5-h-o-cache-dir-verify.txt` |

### 3.2 Ollama pull 명령 (사용자 명시 후 실행)

> 🟡 **Ollama pull 채널 ≠ HF wget direct ((g)/(h) 답습)** — Ollama daemon (pid 3375) 통해 `registry.ollama.ai` egress. pid 3375 hash baseline 변경 0 의무 (mid-cycle R-1 anchor verify, 단 daemon 실행 파일 hash baseline 한정 verify — daemon 내부 상태 변경은 verify 0건 정직성 명문 R-S4 답습).

```bash
ollama pull qwen3:30b-a3b-instruct-2507-q4_K_M 2>&1 | tee /tmp/phase3-5-h-o-pull.log
# 예상 시간: ~18GB / Ollama pull throughput (시점 의존, ~5~15분 범위 가설, (h) wget 26.4 MB/s 답습 scaling)
# CDN endpoint = cas-bridge 답습 가능성 ((h) raw line 102 답습 정합)
```

### 3.3 Pull 후 verify (R-S2/R-S3 발효 명문 + R-rec-3·R-rec-14 흡수)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | `ollama list` → `qwen3:30b-a3b-instruct-2507-q4_K_M` 적중 + size ~18GB 확인 | `/tmp/phase3-5-h-o-list-post.txt` |
| 2 | `ollama show qwen3:30b-a3b-instruct-2507-q4_K_M` → metadata (parameter_count, quantization, family, context_length) verify + (h) GGUF 답습 정합성 확인 ((h) qwen3moe arch / 30.5B/3.3B activated / 128 experts top-8 / 48 layers 답습 일치 자격) | `/tmp/phase3-5-h-o-show.txt` |
| 3 | **Ollama manifest digest verify (R-rec-3 흡수 확장)** — `cat ~/.ollama/models/manifests/registry.ollama.ai/library/qwen3/30b-a3b-instruct-2507-q4_K_M \| jq '.layers[].digest'` 직접 read → blob digest 추출 + Agent C WebSearch verify `78b329e716e7` (8 octet prefix) 가 manifest digest prefix 또는 layer digest prefix 사전 framing 명문 + cross-check 의무 | `/tmp/phase3-5-h-o-manifest.txt` |
| **4 [R-rec-14 흡수]** | **`ollama show --modelfile` TEMPLATE + PARAMETER 추출** — `ollama show qwen3:30b-a3b-instruct-2507-q4_K_M --modelfile` 출력에서 TEMPLATE + PARAMETER + SYSTEM 추출 + (h) llama-cli 호출 시 chat template 동일 자격 verify 의무 | `/tmp/phase3-5-h-o-modelfile.txt` |
| 5 | **R-1 anchor 18회 추가 (mid-cycle, R-3 답습)** — pull 후 verify 직전 `sudo sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 §4 진입 자격 | `/tmp/phase3-5-h-o-r1-anchor-18x.txt` |
| 6 | egress baseline post-pull + 디스크 사용량 post-pull (`sudo ss -tan state established` + `df -h /home/delangi`) | `/tmp/phase3-5-h-o-egress-post-pull.txt`, `/tmp/phase3-5-h-o-disk-post-pull.txt` |

→ Step 1·2·3·4 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (pull 실패 또는 metadata mismatch) 발동

---

## 4. 측정 절차 (Ollama /api/generate API, Phase 1 답습 + (h) prompt 답습, R-S3 발효 cold 측정 우선)

### 4.1 사전 조건 (R-12 (B-B7) 발효 GPU 메모리 verify command 명문)

| Step | 명세 |
|---|---|
| 1 | **다른 model unload + GPU 메모리 0 직접 verify (R-12 발효)** — `curl -s http://127.0.0.1:11434/api/generate -d '{"model":"qwen3-coder-next","prompt":"","keep_alive":0}'` (qwen3-coder-next + qwen2.5-coder:32b 등 cleanup) + `nvidia-smi --query-gpu=memory.used,utilization.gpu --format=csv` 직접 verify (idle 확인). **R-1 anchor 19회 추가** (mid-cycle, 측정 *전*) — `sudo sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 측정 진입 자격 |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama\|claude"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu,temperature.gpu --format=csv` (idle 확인, thermal baseline) |
| 4 | Ollama daemon health — `curl -s http://127.0.0.1:11434/api/version` |

### 4.2 측정 명령 (Phase 1 답습 protocol, (h) prompt 답습, R-S3 발효 cold 측정 우선 + R-rec-6 keep_alive 명문)

> 🟡 **prompt 답습**: (h) decode-161tok prompt + prefill-2k prompt 동형 답습 (절대 경로 한국어 큰따옴표 인용, R-9 답습). 단 Ollama API token 분모 = `prompt_eval_count` + `eval_count` 사용 (llama-cli perf line 과 다른 분모 가능성 정직성 명문 의무 + R-rec-13 흡수 = (h) llama.cpp re-tokenize 153 tokens cross-check 의무).

> 🟡 **R-S3 발효 cold 측정 우선 framing**:
> - **본 cycle 측정 = cold load (`keep_alive: 0` 후 첫 호출) 단독 우선** ((h) llama.cpp `--no-warmup` 답습 비대칭)
> - warm 측정 자격 평가 = **별도 단계 (cache hit 효과 분리 framing 의무)**, Phase 1 H-B1 답습 (SSM state cache reuse 불가) + qwen2.5-coder warm/cold ~628× cache hit 답습 영구
> - tok/s 비교 시 **cold 측정값 우선 사용**, warm 측정값 = 별도 framing
> - **R-rec-6 흡수**: `keep_alive: 0` 의미 = "매 호출 후 즉시 unload" — 두 prompt (decode + prefill-2k) 측정 사이 모델 재로드 비용 발생 가능성 + (h) llama-cli `--no-warmup` 답습 mismatch 가능성 정직성 명문

```bash
# decode-161tok prompt (Phase 1 답습 protocol, cold 우선)
PROMPT_DECODE=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt")
curl -s http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_DECODE" '{
        model: "qwen3:30b-a3b-instruct-2507-q4_K_M",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    2>&1 | tee /tmp/phase3-5-h-o-measure-decode-161tok-cold.json

# prefill-2k prompt (cold)
PROMPT_PREFILL=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt")
curl -s http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_PREFILL" '{
        model: "qwen3:30b-a3b-instruct-2507-q4_K_M",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    2>&1 | tee /tmp/phase3-5-h-o-measure-prefill-2k-cold.json
```

### 4.3 측정 항목 (Phase 1 답습 + (h) 직접 비교 + R-S2 발효 분모 정직성 + R-rec-13 흡수)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| Ollama decode tok/s (R-S2 발효 양 분모 raw report 의무) | **(분모 1)** `eval_count / (eval_duration / 1e9)` (Ollama API 명세 답습) + **(분모 2)** `eval_count / (total_duration - load_duration) * 1e9` (실 측정 wall-clock 분모). **Phase 1 raw verify 답습 — `eval_count: 512 / eval_duration: 72.008s ≈ 7.11 t/s` vs Phase 1 summary `decode_tok_per_sec: 7.926` = ~11% 격차** → 본 cycle 양 분모 raw report 의무 영구 | tok/s 분모 정직성 영구 명문 (§6 #19 답습) |
| Ollama prefill tok/s | `prompt_eval_count / (prompt_eval_duration / 1e9)` + 양 분모 답습 | 동상 |
| total wall-clock | `total_duration / 1e9` (nanoseconds → seconds) | 빌드·로딩·측정 합산 |
| **(R-rec-13 흡수) prompt_eval_count vs llama.cpp 153 token cross-check** | Ollama API response `prompt_eval_count` 추출 + (h) llama.cpp re-tokenize **153 tokens** 답습 직접 비교 의무. 분모 mismatch 시 raw report + tokenizer 변수 단독 분리 cycle (R-rec-9 답습) carry-over | tokenizer 변수 정직성 영구 명문 |
| eval_count vs llama.cpp generation count | (h) decode `n_predict 256` + Phase 1 동형, Ollama `num_predict 256` 동일 → 분모 일치 자격 강함 (단 verify 의무) | tok/s 비교 자격 정확성 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점 |
| GPU temperature polling (R-rec-3 답습 + R-rec-9 흡수) | `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` background. **threshold 85°C 5분 지속 시 raw report + 사용자 명시 분기, 자동 중단 0건**. 본 cycle 측정 wall-clock ~5~30분 가설 시 5분 미만 가능성 framing | 5분 이상 thermal 정직성 |
| **(h) llama.cpp 직접 비교 (핵심)** | (h) decode-161tok `[ Prompt: 389.4 t/s \| Generation: 49.6 t/s ]` + prefill-2k `[ Prompt: 1916.8 t/s \| Generation: 45.4 t/s ]` ((h) F-1 답습) | 본 cycle 핵심 결과 — 4 차원 통제 동일 (model + quant + prompt + hardware), 1 차원 변경 (inference engine) + R-S1 발효 source conversion lineage 변수 *추가* 미통제 |
| **Phase 1 Ollama baseline (간접)** | qwen3-coder-next decode 7.83 ± 0.36 / qwen2.5-coder:32b decode 4.62 ± 0.18 | 본 cycle (h-O) Qwen3-30B-A3B-Instruct-2507 = Phase 1 과 다른 model (model 변수 미분리 framing) |

**측정 종료 후 R-1 anchor 20회 추가 (R-3 답습)** — 측정 직후 `sudo sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 ((g)/(h) §5 답습 + R-10/R-11 발효 sub-trigger 분리 + R-S3 framing 약화)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | `ollama pull` 성공 + `ollama list` 적중 + 측정 완료 (tok/s 실수치 획득 cold 우선) | raw report → **(h) vs (h-O) 비교 framing (§9)** → inference engine 변수 *부분* 분리 *간접* evidence (R-S1 발효 source conversion 변수 추가 미통제) → MVP-1 R4 framing 강화/정정 input 강함 (단 본문 정정 별도 cycle R-9 답습 영구) |
| **B1 (pull 실패 — 404 model tag 부재 단독, R-10 발효)** | Ollama pull 404 model tag 부재 (Ollama Registry API 시점 변경) | raw report → 다른 source 평가 (O-alt 또는 O-modelfile (h-OM)) 또는 보류 (사용자 명시 별도) |
| **B2 (Ollama runtime 에러)** | Ollama load 실패 (GGUF format 호환 부재, embedded llama.cpp version 미지원 quant scheme), OOM, CUDA error, segfault | raw report → Ollama Modelfile (O-modelfile / (h-OM)) 자격 평가 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | Ollama registry timeout (default 30s vs 60s vs 무한 verify 의무) | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | pull 중 ENOSPC | 즉시 중단 → (g)/(h) GGUF (R-13 보존) cleanup 사용자 명시 후 재시도 |
| **B5 (Ollama manifest digest mismatch, R-11 (B-B6) 발효 R-S4 통합)** | Ollama models manifest digest ≠ Agent C WebSearch verify (`78b329e716e7`) | raw report → **Ollama daemon 자동 sha256 verify 메커니즘 신뢰도 부분 평가** — (h) R-S4 답습 multipart 가능성 명문 후 Ollama 자체 verify 가 multipart blob 처리 자격 평가. 부적 시 = **manual quarantine** ((h) §5 B5 답습 `mv` 만, `rm` 0건 자동 실행 금지 비례성 답습 영구) 사용자 명시 분기 의무 |
| **B6 (tokenizer 분모 mismatch, R-11 (B-B5) 발효 신규)** | §4.3 추출 시점 Ollama `prompt_eval_count` ≠ (h) llama.cpp re-tokenize **153 tokens** 답습 | raw report → (h) 분모 (153 tokens) 대응 token 환산 자격 평가 + 사용자 명시 별도 분기 (tokenizer 변수 단독 분리 cycle, R-rec-9 답습) |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 20 항목, (h) §6 답습 + R-S1/R-S2/R-S3/R-S4/R-S5 발효 신규 #18·#19·#20)

1. **Ollama library = bartowski (HF) 답습 자격 verify 의무 (R-S1 발효 정정)** — Ollama hub 의 GGUF 가 (h) bartowski conversion 답습인지 자체 conversion 인지 = **R-S1 raw verify 답습 — Ollama library blob `78b329e716e7` (8 octet prefix) ≠ (h) bartowski sha256 `382b4f5a164d...` (full 64자) = 다른 source 자격 강한 시사 (8 octet vs 64 octet 비교 자격 불완전)**. manifest digest cross-check 답습 의무 강함 — 다른 conversion lineage 시 inference engine 단독 분리 자격 약화
2. **inference engine 변수 *부분* 분리 자격 *강함*** (R-S5 발효 약화) — model + quant + prompt + hardware (GB10) 4 차원 통제 동일, llama.cpp `c0c7e147` 직접 ↔ Ollama 0.20.4 (embedded llama.cpp version 별도)
3. **미통제 변수 — 측정 도구 framework**: llama-cli (interactive hang) vs Ollama /api/generate (HTTP API + JSON response) — 측정 추출 방법론 차이
4. **미통제 변수 — Ollama embedded llama.cpp version (R-S4 발효 §3.1 Step 7 직접 verify 의무)**: Ollama 0.20.4 의 내부 llama.cpp version ≠ (h) 의 llama.cpp `c0c7e147` 가능성 (Ollama release version 답습) — `ollama --version` + `/api/version` 직접 verify 의무
5. **미통제 변수 — Ollama internal caching/optimization**: Ollama 자체 KV cache 관리 + scheduling + warm-up 정책 (llama-cli `--no-warmup` 답습 대 Ollama default behavior)
6. **미통제 변수 — tokenizer 차이 가능성 (R-rec-13 + B6 발효)**: Ollama internal tokenizer vs (h) llama-cli tokenizer (Ollama `prompt_eval_count` vs llama.cpp re-tokenize 153 tokens 답습 verify 의무 + 분모 mismatch 시 B6 분기 발동)
7. **분모 mismatch 가능성 (R-S2 발효 §6 #19 답습)**: Ollama eval_count vs llama.cpp generation token count — 일치 자격 verify 의무
8. **R-23 위반 가능성** — pull ~5~15분 + 측정 ~5~30분 wall-clock 중 다른 활동 발생 가능
9. **egress 비례성 (R-rec-12 답습)** — **~18GB egress = (g)+(h)+(h-O) 누계 ~80GB** (Phase 1 ~10GB 답습 대비 ~8×, R-11 답습)
10. **디스크 비례성 (R-S4 발효 §3.1 Step 8 직접 verify 의무)** — Ollama models cache 위치 별도 (`~/.ollama/models/` user-local vs `/usr/share/ollama/.ollama/models/` systemd-service) — 직접 verify 의무
11. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습) — Phase 1 N=3 repetitions 답습 자격 = 별도 cycle 의무 (C-S2 답습)
12. **GPU thermal throttling 가능성 (R-rec-9 답습)** — 5분 이상 연속 측정 시 영향 (R-rec-3 polling 명문, threshold 85°C 5분 / 본 cycle 측정 wall-clock ~5~30분 가설 시 5분 미만 가능성 framing)
13. **Ollama daemon pid 3375 hash baseline 보존 (R-rec-11 발효)** — silent 교체 0건 답습 영구 (R-1 anchor 17·18·19·20회 답습 의무, hash baseline `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` full 64자). **단 `sha256sum /proc/3375/exe` = daemon 실행 파일 hash baseline 한정 verify, daemon 내부 상태/메모리/cache 변경 verify 0건** 정직성 명문 (B-S1 답습)
14. **Phase 1 F2 가설 강화/약화 framing 분리**:
    - 본 cycle (h-O) tok/s < (h) tok/s → F2 가설 (Phase 1 ~4.07× Ollama 느림) *답습 강화*
    - 본 cycle (h-O) tok/s ≈ (h) tok/s → F2 가설 *부분 부정* (Ollama embedded llama.cpp 호환 효율성 강함)
    - 본 cycle (h-O) tok/s > (h) tok/s → F2 가설 *역방향 강화* ((g) F-1 + (h) F-1 답습 일관)
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
15. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
16. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
17. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
18. **R-S1 발효 신규 — Ollama library source conversion lineage 변수 *추가* 미통제 정직성**: Ollama library blob `78b329e716e7` ≠ (h) bartowski sha256 `382b4f5a164d...` 다른 source 자격 강한 시사 (8 octet prefix verify, 64 octet 비교 자격 불완전), conversion lineage 변수 *추가* 미통제 명문. (h-OM) Ollama Modelfile (h) GGUF 직접 등록 cycle = source conversion 100% 통제 자격 강함, 본 cycle *전* 평가 자격 강함 carry-over MEDIUM
19. **R-S2 발효 신규 — tok/s 분모 정직성 영구 명문**: Phase 1 raw verify `eval_count: 512 / eval_duration: 72.008s ≈ 7.11 t/s` ≠ Phase 1 summary `decode_tok_per_sec: 7.926` = ~11% 격차. 본 cycle 양 분모 (`eval_count/eval_duration` + `total_duration/(total_duration-load_duration)`) raw report 의무 영구
20. **R-S3 발효 신규 — Ollama warm 측정 시 prefix cache hit 자격 자동 발효 가능성**: Phase 1 H-B1 답습 (SSM state cache reuse 불가) + qwen2.5-coder warm/cold ~628× cache hit 답습 영구. 본 cycle = cold 측정 우선, warm 측정 자격 = 별도 framing (cache hit 효과 분리 의무). (h) llama.cpp `--no-warmup` 답습 비대칭, tok/s 비교 시 cold 측정값 우선 사용

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 15 항목과 §7 차단 조건은 **1:1 매핑 의무** ((g)/(h) R-15 답습).

1. ❌ 본 brief 자체 pull/측정/sudo 실행
2. ❌ Ollama daemon 변경 (pid 3375 hash baseline 보존, keep_alive 0 unload 만)
3. ❌ (h) GGUF 파일 변경 (R-13 보존)
4. ❌ (g) GGUF 파일 변경 (R-13 보존)
5. ❌ llama.cpp HEAD `c0c7e147` 변경
6. ❌ MVP-1 합의 본문 자동 정정 (R-9 답습 영구)
7. ❌ 헌법·ADR 본문 자동 정정
8. ❌ M3·M4 결정 *고정* ((k) 별도 cycle)
9. ❌ runtime backend 코드 작성 (트랙 B 별도)
10. ❌ 메모리 자동 갱신
11. ❌ (h-OM)/(j)/(k)/(l)/(m)/(n) 자동 진입
12. ❌ brief commit 자동 진입
13. ❌ Ollama pull 시점 = 사용자 명시 *직접* 의무 (R-11 비례성 답습)
14. ❌ (g)+(h)+(h-O) 통합 본문 정정 ((g)/(h) brief/합의 본문 변경 0건) + (g)+(h)+(h-O) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원 carry-over)
15. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + **(h-O-X) prime/super-prime** 자동 진입 명백 부정 (chain 영구 종결 의무 답습 영구, R-13 (B-B8) 발효)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (h-O) cold < (h) (Ollama 느림 답습) | F2 가설 답습 강화 + MVP-1 R4 framing *정정 강한 input* → 본문 정정 별도 cycle HIGH |
| G + (h-O) cold ≈ (h) (Ollama embedded 효율성) | F2 가설 *부분 부정* + MVP-1 R4 framing *답습 자격* → 본문 정정 약화 |
| G + (h-O) cold > (h) (Ollama 빠름, 역방향) | F2 가설 *역방향 강화* ((g) F-1 + (h) F-1 답습 일관, 단 inference engine 변수 *부분* 분리 측면 + R-S1 source conversion 변수 미해소) |
| B1~B6 | 다른 source / (h-OM) / 다른 tokenizer / (h) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습, R-rec-16 + R-rec-10 발효)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **(h-OM) Ollama Modelfile (h) GGUF 직접 등록 cycle** | **MEDIUM ⭐⭐ (R-S1 + R-rec-16 발효 격상)** | bartowski conversion lineage 100% 통제 + egress 0 + (h) ↔ (h-O-library) ↔ (h-OM) 3-way 비교 framing 자격 강함, source conversion 변수 추가 미통제 직접 해소 |
| **MVP-1 합의 R4 framing 강화/정정 evidence 별도 cycle** | HIGH | (g)/(h)/(h-O) 종합 input 강함 (R-9 답습 영구) |
| **(g)+(h)+(h-O) 통합 *분석* cycle (≠ 통합 *본문 정정*, N-12 격상 자격)** | MEDIUM → HIGH 격상 자격 평가 | 변수 분리 종합 + Provider Liquidity finding 종합 (사용자 비전 답습 시 격상) |
| **Phase 1 N=3 repetitions 답습 cycle (C-S2 답습)** | MEDIUM | 재현성 평가 자격 강화 (Ollama HTTP API + JSON + scheduler noise > llama-cli 단일 process, cost ~2× 시간) |
| **Ollama embedded llama.cpp version verify cycle (R-S4 + N-15)** | MEDIUM | (h) `c0c7e147` 와 commit 차이 평가, ~5분 cost |
| **bartowski conversion lineage cross-check cycle (N-14)** | MEDIUM | Ollama library blob ↔ (h) bartowski sha256 직접 cross-check |
| **llama.cpp graceful tensor name resolution 검증 cycle** | MEDIUM | (g) F-2 + (h) R-S3 답습 read-only |
| **(j) advisory wall-clock 측정** | MEDIUM | 자비스 비전 직접 진전 |
| **(k) M3·M4 결정 *고정*** | DEFER | 변수 분리 input 강화 후 평가 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 의무 답습 영구 |
| **`llama-bench` carry-over (R-rec-12 격상)** | MEDIUM | (g) F-8 + (h) F-7 답습 risk 직접 해소 자격 |
| **Ollama models cache 위치 + 권한 별도 verify cycle (R-rec-10 발효)** | LOW | cache directory user-local vs systemd-service 분리 verify |
| **다른 quant 비교 (Q5_K_M / IQ4_XS) cycle** | LOW | R-rec-2 답습 |
| **외부 benchmark cross-reference cycle (RTX 3090 Qwen3.6-35B-A3B Q4_K_M Ollama 107 / llama.cpp 135.7 +27%)** | LOW | hardware + version + model 차이 정직성 cross-ref (C-N-5 답습) |
| **tokenizer 변수 단독 분리 cycle (B6 발효 시)** | LOW | R-rec-9 답습 |
| **(g)+(h)+(h-O) 통합 본문 정정 cycle** | DEFER | 사용자 명시 별도 cycle, (g)/(h) brief/합의 본문 변경 0건 |
| **`qwen3:30b-a3b` default tag (O-alt, blob `ad815644918f` 다른 model variant) cycle** | LOW | C-N-6 답습 |
| **Phase 3 summary recommendation C 정정** | LOW | (i) falsification + (g)/(h) 성공 답습 |
| **(m) §12 Ollama 위생 정정** | LOW | 본 cycle 무관 |
| **(n) Phase 3 brief v1.2 보강** | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) prime/super-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((g)/(h) 동형 풀 7단계 답습, 사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `61cb005`, 377줄 | 명시 완료 |
| (2) 풀 3+1 합의 진행 + commit | `37bcd40`, 459줄, BLOCKING 14 + R-S1~R-S5 | 명시 완료 |
| **(3) brief v1.1 보강 + commit (본 단계)** | BLOCKING 14 verbatim 100% + R-S 5 흡수 11곳 + 권고 17 일부 + §11 신규 | **진행 중** |
| (4) Ollama pull 실행 (~5~15분 wall-clock) | `ollama pull qwen3:30b-a3b-instruct-2507-q4_K_M` (R-7 답습) | **사용자 명시 *직접* 의무 (~18GB egress)** |
| (5) verify + 측정 실행 (~15~45분 wall-clock) | §3.3 + §4 절차 답습 (cold 측정 우선) | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (g)/(h) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (h) vs (h-O) 비교 framing (본 cycle 핵심 가치, inference engine 변수 *부분* 분리 + R-rec-15 발효 prefill 시나리오 분리)

### 9.1 (h) 측정값 답습 (직접 비교 baseline)

| 항목 | (h) llama.cpp `c0c7e147` 직접 | 측정 방법 비고 |
|---|---|---|
| decode-161tok 측정 명령 perf line | `[ Prompt: 389.4 t/s \| Generation: 49.6 t/s ]` | 단일 perf line, prompt + generation 동시 |
| prefill-2k 측정 명령 perf line | `[ Prompt: 1916.8 t/s \| Generation: 45.4 t/s ]` | 동상 |
| 모델 | Qwen3-30B-A3B-Instruct-2507, ~30.5B total / ~3.3B activated | classical MoE, 128 experts top-8, SSM 미포함 |
| quant | Q4_K_M (bartowski conversion, imatrix) — sha256 `382b4f5a164d...` | (h) 답습 |
| GGUF 크기 | 17.353 GiB (18,632,183,808 bytes) | (h) 답습 |
| 측정 도구 | llama-cli `-no-cnv` + `< /dev/null` + `timeout 300s` (cold 단독, `--no-warmup`) | interactive hang (g) F-8 답습 영구 |

### 9.2 (h-O) 예상 결과 시나리오 (R-S5 발효 약화 framing + R-rec-15 prefill 분리)

**decode 시나리오 (5)**:

| 시나리오 | (h-O) decode cold tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: Ollama 느림 (~10~30 t/s)** | F2 가설 (Phase 1 ~4.07× Ollama 느림) 답습 강화. Ollama embedded llama.cpp version + 자체 caching overhead | MVP-1 R4 framing *정정 강한 input* (별도 cycle HIGH) | F2 가설 framing 정정 cycle (별도) |
| **S2: Ollama 동급 (~40~55 t/s)** | F2 가설 *부분 부정* — Ollama embedded llama.cpp 효율성 동급 | MVP-1 R4 framing *답습 자격* (정정 약화) | (g)+(h)+(h-O) 통합 *분석* cycle |
| **S3: Ollama 빠름 (~60~80 t/s)** | F2 가설 *역방향 강화* — Ollama 자체 최적화 우위 | (g) F-1 + (h) F-1 답습 측면 격차 *모델 의존* 가설 | F2 재고 + 모델 의존성 cycle |
| **S4: Pull 실패 (B1)** | source 차단 — Ollama library version 비호환 | B1 분기 발동 | 다른 source 또는 Modelfile ((h-OM)) cycle |
| **S5: tokenizer 차이 (B6)** | Ollama `prompt_eval_count` ≠ llama.cpp re-tokenize 153 tokens → tok/s 분모 mismatch | B6 분기 발동, tokenizer 변수 분리 cycle | tokenizer 변수 단독 분리 cycle (R-rec-9 답습) |

**prefill 시나리오 (5, R-rec-15 발효 신규 분리)**:

| 시나리오 | (h-O) prefill cold tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1-P: Ollama 느림 (~30~40 t/s)** | Ollama prefill 처리 framework overhead 우세 | MVP-1 R4 강화 input | decode + prefill 동방향 |
| **S2-P: Ollama 동급 (~40~50 t/s)** | (h) prefill 45.4 답습 ± noise | 동급 framing | (g)+(h)+(h-O) 통합 분석 |
| **S3-P: Ollama 빠름 (~50~70 t/s)** | Ollama prefill cache 정책 우위 | prefill cache 정직성 정정 의무 | Ollama prefill cache 정책 직접 verify cycle |
| **S4-P: Pull 실패 (B1)** | source 차단 | B1 답습 | 다른 source |
| **S5-P: tokenizer 차이 (B6)** | prompt_eval_count mismatch | B6 답습 | tokenizer 변수 분리 |

### 9.3 핵심 정직성 (R-S5 발효 약화 framing — "최초 단일 변수 분리" 단언 0건)

- ✅ **본 cycle = 본 프로젝트 *부분* 변수 분리 시도** — model + quant + prompt + hardware (h) 답습 4 차원 *부분* 통제 (R-S1 발효 source conversion lineage 추가 미통제), 단 5 미통제 변수 (§6 #3~#6 + Ollama library source conversion lineage R-S1 발효) 존재
- ❌ **단독 분리 자격 *강함* (단언 0건)**, **단일 변수 분리 자격 strict criterion 미충족** ((h) R-S3 답습 영구 R-4 framing 답습)
- ❌ **미통제 변수**: 측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이 가능성 + **Ollama library source conversion lineage R-S1 발효**
- → **(h) vs (h-O) 단일 trial = inference engine *간접 부분* input** (단 측정 도구 framework + source conversion 미통제 부분 정직성 명문)
- **Phase 1 F2 (~4.07× Ollama 느림) 결정적 input** = (h-O) cold tok/s 결과 → F2 가설 강화/약화/역전 직접 evidence (단 본문 정정 별도 cycle R-9 답습 영구)

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = (h-O) 풀 3+1 합의 (`37bcd40`, 459줄) BLOCKING 14 verbatim 100% 흡수 + R-S1~R-S5 흡수 11곳 + 권고 17 일부 흡수 + §11 v→v1.1 변경 일람 신규
- 본 cycle 진입 = (h) cycle 완료 (`fccec6a`) + 사용자 명시 (h-O) 진입 형태 + Ollama pull 진행 + Phase 3.5-O 명명 직후
- 본 brief 자체 머신 변경 0건 (pull/측정/sudo 0건)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)
- ⭐⭐⭐ R-S1 CRITICAL 흡수 = Ollama library blob `78b329e716e7` ≠ (h) bartowski sha256 `382b4f5a164d...` 다른 source 확정 + (h-OM) MEDIUM 격상 신규 carry-over 발효
- ⭐⭐ R-S2 HIGH 흡수 = Phase 1 raw eval_count/eval_duration ≈ 7.11 vs summary 7.926 ~11% 격차 양 분모 raw report 의무 영구
- ⭐⭐ R-S3 HIGH 흡수 = cold/warm 비대칭 framing + Phase 1 H-B1 답습 prefix cache hit 정직성 명문
- ⭐ R-S4 MEDIUM 흡수 = §3.1 Step 7·8 신규 (embedded llama.cpp version + cache directory verify) + §3.0 line 125 sudo 5~7회 정정
- ⭐ R-S5 MEDIUM 흡수 = §9.3 "최초 단일 변수 분리" 단언 → "*부분* 변수 분리 시도" 약화
- 본 brief v1.1 길이 = 377줄 → ~520줄 (v1 대비 +~140줄, BLOCKING 14 + R-S 5 + 권고 + §11 추가)

---

## 11. v1 → v1.1 변경 일람 ((h) R-rec-6 답습 + 본 합의 §11 답습)

### 11.1 BLOCKING 14 흡수 매트릭스 (verbatim 100%, R-21 답습 영구)

| BLOCKING | 출처 | brief v1.1 정정 위치 | 본문 변경 |
|---|---|---|---|
| **R-1 (R-S4 부분)** | A-B5 + B-B1 | §3.1 Step 8 신규 (cache directory verify) + §6 #10 정정 | 1 신규 step + #10 정정 |
| **R-2 (R-S4 부분)** | A-B3 + B-B4 + C-rec-3 | §3.1 Step 7 신규 (embedded llama.cpp version verify) + §6 #4 정정 | 1 신규 step + #4 정정 |
| **R-3 (R-S5) ⭐⭐ HIGH** | 3-way 정합 (A-B4 + B-... + C 단언 framing) | §9.3 line 360 약화 ("최초" → "*부분*" 시도) + §1.1 framing 약화 + §1.3 명문 | 3 곳 약화 framing |
| **R-4 (R-S2) ⭐⭐ HIGH** | A-S1 raw direct verify | §4.3 line 213 (양 분모 명문) + §6 #19 신규 | 2 곳 신규 명문 |
| **R-5 (R-S1) ⭐⭐⭐ CRITICAL** | C-S1 + C-B1 통합 | §2.1 row B (O-modelfile 재평가 framing) + §1.3 (O vs O-modelfile 결정 명문) + §6 #18 신규 | 3 곳 정정 |
| **R-6 (A-B1)** | Agent A 단독 | §2.2 Step 2 verify 강화 + Agent C blob digest 직접 답습 | 1 곳 강화 |
| **R-7 (A-A2)** | Agent A 단독 | §4.2 line 190 keep_alive 0 재로드 비용 정직성 (R-rec-6 흡수) | 1 곳 명문 |
| **R-8** | A + B 정합 부분 | §0 #2 + §1.1 + §3.1 R-1 anchor 누계 명확 (16 + 4 = 20) | 모든 R-1 anchor 회차 표현 명확 |
| **R-9 (R-S4 부분, B-B2)** | Agent B 단독 | §3.0 line 125 sudo 5~7회 정정 + §3.1 R-1 anchor 4회 sudo 명문 | 1 곳 정정 |
| **R-10 (B-B3)** | Agent B 단독 | §5 B1 = "404 model tag 부재 단독" 분리 + B3/B4/B5 sub-trigger 별도 | §5 분기 매트릭스 정정 |
| **R-11 (B-B5/B-B6)** | Agent B 단독 | §5 B5 정정 (Ollama 자체 sha256 verify + multipart 정직성) + §5 B6 신규 (tokenizer 분모 mismatch) | 2 곳 정정 + 1 곳 신규 |
| **R-12 (B-B7)** | Agent B 단독 | §4.1 Step 1 GPU 메모리 0 직접 verify command 명문 | 1 곳 정정 |
| **R-13 (B-B8)** | Agent B 단독 | §0 #15 + §7 #15 (h-O-X) prime/super-prime 자동 진입 명백 부정 답습 | 2 곳 명문 |
| **R-14 (R-S3) ⭐⭐ HIGH** | C-B1 + 부분 A | §4.2 line 178 cold 측정 우선 + §6 #20 신규 + §1.3 명문 | 3 곳 정정 |

### 11.2 Reviewer 단독 격상 R-S1~R-S5 흡수 매트릭스 (위 11.1 답습 통합)

- **R-S1 ⭐⭐⭐ CRITICAL** → R-5 발효 (3 곳: §2.1 row O-modelfile + §1.3 + §6 #18)
- **R-S2 ⭐⭐ HIGH** → R-4 발효 (2 곳: §4.3 + §6 #19)
- **R-S3 ⭐⭐ HIGH** → R-14 발효 (2 곳: §4.2 + §6 #20)
- **R-S4 ⭐ MEDIUM** → R-1/R-2/R-9 발효 (3 곳: §3.1 Step 7·8 + §3.0)
- **R-S5 ⭐ MEDIUM** → R-3 발효 (1 곳: §9.3)
- **총 11 곳 정정**

### 11.3 권고 17 흡수 매트릭스 (강한 권고 직접 흡수, 약한 권고 by-reference)

| 권고 | 흡수 자격 | brief v1.1 정정 위치 |
|---|---|---|
| R-rec-3 (manifest digest verify 확장) | 강함 | §3.3 Step 3 확장 |
| R-rec-6 (keep_alive 0 의미 명문) | 강함 | §4.2 line 178 R-S3 통합 |
| R-rec-9 (GPU thermal 5분 미만 framing) | 부분 | §4.3 thermal 행 명문 |
| R-rec-10 (cache 위치 별도 verify cycle) | 부분 | §8.2 carry-over LOW |
| R-rec-11 (hash baseline full 64자) | 강함 | §0 #2 + §6 #13 + §3.1 Step 4 |
| R-rec-12 (egress 비례성 framing) | 부분 | §6 #9 by-reference |
| R-rec-13 (prompt_eval_count vs 153 cross-check) | 강함 | §4.3 항목 신규 |
| R-rec-14 (`ollama show --modelfile` 추출) | 강함 | §3.3 Step 4 신규 |
| R-rec-15 (§9.2 prefill 분리 시나리오 5) | 강함 | §9.2 prefill 분리 |
| R-rec-16 (O-modelfile LOW → MEDIUM) | R-S1 통합 | §8.2 MEDIUM 격상 |
| R-rec-17 (§2.1 blob digest 직접 명문) | 강함 | §2.1 row O |
| 다른 권고 (R-rec-1/2/4/5/7/8) | 약함 | by-reference (선택적 흡수) |

### 11.4 NOTE 17 by-reference (변경 0건, §7 합의 보고서 답습)

- N-1~N-17 = 합의 보고서 §7 by-reference 한정, 본 brief v1.1 직접 흡수 0건

### 11.5 기각 5 답습 (변경 0건, §8 합의 보고서 답습)

- 기각-1~5 = 합의 보고서 §8 답습 영구, 본 brief v1.1 변경 0건

---

**본 brief v1.1 작성 완료** (Phase 3.5-O (h-O) Ollama 직접 측정 cycle entry plan, 풀 3+1 합의 APPROVE w/ COND + BLOCKING 14 verbatim 100% 반영 + R-S1~R-S5 흡수 11곳 + 권고 17 일부 흡수 + §11 v→v1.1 변경 일람 신규. ⭐⭐⭐ R-S1 CRITICAL 발효 = Ollama library blob `78b329e716e7` ≠ (h) bartowski sha256 `382b4f5a164d...` 다른 source 확정 + (h-OM) Ollama Modelfile cycle 신규 MEDIUM carry-over. 본 cycle 머신 변경 0건. 다음 단계 = 사용자 명시 의무 답습 영구.)
