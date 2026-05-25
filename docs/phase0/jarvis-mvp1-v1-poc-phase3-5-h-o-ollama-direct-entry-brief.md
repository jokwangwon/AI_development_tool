# Jarvis MVP-1 V-1 PoC Phase 3.5-O (h-O) entry brief (v1, Ollama qwen3:30b-a3b-instruct-2507-q4_K_M 직접 측정 cycle, 합의 *전* entry plan)

> **본 brief v1 = (h-O) Phase 3.5-O Ollama 직접 측정 cycle 의 entry plan only.** v1 진입 자격 = (h) Phase 3.5-B cycle 정리 commit `fccec6a` 직후 사용자 명시 (h-O) 직접 선택 + 4 명확화 ((g)/(h) 동형 7단계 + Ollama pull 진행). 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구). 실 변경 = 본 brief v1 commit + push 만. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-B (h) cycle 정리 commit `fccec6a` 직후, 본 (h-O) cycle 단계 (1) brief v1)
**카테고리**: V-1 PoC Phase 3.5-O (h-O) entry brief v1 (Phase 3 carry-over (h) R-S1 발효 직접 후속, 본 cycle 핵심 = **inference engine 변수 단독 분리** — (h) llama.cpp ↔ (h-O) Ollama 1:1 동일 모델 동일 quant 동일 prompt 동일 hardware 비교)
**범위**: (1) Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` pull 절차 (egress 격리, ~18GB) / (2) Ollama /api/generate 측정 절차 (Phase 1 답습 + decode + prefill-2k) / (3) 분기 (G·B1~B5) / (4) (h) llama.cpp vs (h-O) Ollama 1:1 비교 framing (inference engine 변수 단독 분리 핵심) / (5) 후속 carry-over

**답습 권위**:
- **Phase 3.5-B (h) cycle 정리 commit** (`fccec6a`, SESSION 15번째 entry, F-1 classical MoE > SSM hybrid 1.44~2.19× + F-2 SSM 미포함 confirm + R-1 anchor 16회) — 본 (h-O) 직접 선행 cycle, **R-S1 발효 직접 carry-over source 영구**
- (h) brief v1.1 (`de0326b`, 467줄, BLOCKING 13 + R-S1~R-S5 흡수)
- (h) 풀 3+1 합의 (`d74d205`, 491줄)
- (g) Phase 3.5 cycle 정리 commit (`b3d4164`, 14번째 entry, F-1 ~4.07× / F-2 부분 호환 / F-3 conversion path diversity)
- Phase 3 entry brief (`docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` v1.1, `25eb008`)
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`) — qwen3-coder-next decode 7.83 ± 0.36 / prefill cache miss 58 ± 0.27 답습 영구
- (h) raw measurement (`docs/phase0/v1-poc-raw/phase3-5-h/*`) — decode 49.6 / prefill 45.4 t/s 직접 input
- MVP-1 합의 R4 "llama.cpp ↔ Ollama 동급" — input only (R-9 답습 영구)
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter` / `project_mvp_staged_roadmap`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` pull 절차 명문 — egress 격리·blob verify·R-1 anchor 17회 답습 + (h) 16회 누계 후속
2. Ollama /api/generate 측정 절차 명문 — Phase 1 답습 + decode + prefill-2k (h) 동형 prompt set
3. 분기 조건 명문 — G 성공·B1 pull 실패·B2 Ollama runtime 에러·B3 network·B4 디스크·B5 (h) 답습 가능
4. 정직성 한계 명문 17 항목 (§6) — inference engine 변수 단독 분리 자격 + 미통제 변수 (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization)
5. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
6. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구
7. (h) llama.cpp vs (h-O) Ollama 1:1 비교 framing 명문 (§9) — inference engine 변수 단독 분리 핵심 가치 + 시나리오 5

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 pull / 측정 / sudo 실행** — 본 brief = entry plan only, 합의 *전*
2. ❌ **Ollama daemon 상태 변경 (pid 3375)** — keep_alive 0 unload 만, R-1 anchor hash baseline `ce95c475...878b10` 일관 보존 (silent 교체 0건 답습 영구)
3. ❌ **(h) GGUF 파일 변경** — `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` 보존 (R-13 답습 영구, (h) 비교 baseline)
4. ❌ **(g) GGUF 파일 변경** — `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` 보존 (R-13 답습 영구)
5. ❌ **llama.cpp HEAD `c0c7e147` 변경** — (h) 측정 baseline 보존 (재측정 cycle 자격 평가 시 의무)
6. ❌ **MVP-1 합의 본문 자동 정정** — R4 "llama.cpp ↔ Ollama 동급" framing input only (R-9 답습 영구)
7. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
8. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
9. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
10. ❌ **메모리 자동 갱신** — 사용자 명시 의무
11. ❌ **(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
12. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
13. ❌ **Ollama pull 시점 = 사용자 명시 *직접* 의무** — ~18GB egress + 디스크 ~80% 누계 비례성 답습 (R-11)
14. ❌ **(g)+(h)+(h-O) 통합 본문 정정** — 본 cycle = (g)/(h) 와 *독립* 별개 cycle 단독 진행, (g)/(h) brief/합의 본문 변경 0건 ((g)+(h)+(h-O) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle, 별도 차원 carry-over)
15. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입** — chain 영구 종결 의무 답습 영구

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **Phase 3.5-B (h) cycle 완료** (`fccec6a`, SESSION 15번째 entry):
  - F-1 ⭐⭐⭐: classical MoE > SSM hybrid 모든 측정 차원 1.44~2.19× (decode 32.3→49.6 / prefill 31.5→45.4)
  - F-2 ⭐⭐⭐: SSM 미포함 가설 확정 (raw grep 0 적중 + n_tensors 579)
  - F-6 ⭐: HF API + Ollama library WebSearch raw verify = Ollama `qwen3:30b-a3b-instruct-2507-q4_K_M` 실재 ✓ (blob `78b329e716e7`)
  - **(h) 풀 3+1 합의 R-S1 ⭐⭐⭐ CRITICAL 발효 직접 carry-over** = brief §4.3 line 225 "Ollama 동일 모델 0건" 단언 정면 부정 → (h-O) Ollama 직접 측정 cycle 신규 HIGH carry-over 발효
- **본 cycle 핵심 가치 = inference engine 변수 단독 분리**:
  - (h) Qwen3-30B-A3B-Instruct-2507 Q4_K_M + llama.cpp `c0c7e147` 직접 = decode **49.6** t/s / prefill **45.4** t/s
  - (h-O) **동일 모델 + 동일 quant + 동일 prompt + 동일 hardware (GB10)** + Ollama 직접 = decode X t/s / prefill Y t/s
  - → 1 변수만 변경 (inference engine: llama.cpp ↔ Ollama) = **본 프로젝트 최초 단일 변수 분리 직접 비교**
- **Phase 1 F2 (~4.07× Ollama 느림) 답습 vs 정정 자격 결정적 input** = (h) F-1 + (h-O) F-1 종합 → MVP-1 R4 framing 강화/정정 자격 강한 evidence (단 본문 정정 별도 cycle R-9 답습 영구)
- **본 cycle 비용**: egress **~18GB** (Ollama pull, (h) ~17.353 GiB 답습 비용 동일) + 디스크 **~18GB** 임시 사용 + (g)+(h)+(h-O) 누계 ~80GB 디스크 = ~85% 유지 가능성 (Ollama 모델 cache 위치 별도)

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | Ollama pull `qwen3:30b-a3b-instruct-2507-q4_K_M` 성공 가능? | Y/N + `ollama pull` stdout/stderr + `ollama list` 직접 verify |
| **Q2** | Ollama decode/prefill tok/s = ? | Phase 1 답습 measurement protocol (cold load + warm + repetitions) — 단 본 cycle = 단일 측정 cycle 답습 ((g)/(h) 답습) |
| **Q3** | (h) llama.cpp 49.6 t/s vs (h-O) Ollama X t/s 격차 = ? | 1 변수 변경 (inference engine) — 본 프로젝트 최초 단일 변수 분리 input |
| **Q4** | Phase 1 F2 가설 (~4.07× Ollama 느림) 답습 vs 정정? | (h) decode 49.6 / (h-O) decode X 비율 직접 evidence (단 model 차이 미해소 — Phase 1 = qwen3-coder-next SSM hybrid 80B, 본 cycle = Qwen3-30B-A3B-Instruct-2507 classical MoE) |
| **Q5** | F-2 가설 (Ollama 효율성 = format-internal 차이) 답습 vs 정정? | (h-O) tok/s 결과 → Ollama 자체 효율성 정직성 명문, 단 inference engine 변수 단독 분리 자격 강함 |
| **Q6** | Provider Liquidity finding 강화 자격? | (h) F-1 + (h-O) F-1 종합 input HIGH (단 본문 정정 별도 cycle 의무 R-9 답습) |

### 1.3 본 cycle 범위 한정 (R-rec-7 답습 — 독립 cycle + Phase 3.5 sub-cycle framing 통합)

- ✅ 단일 모델 (Qwen3-30B-A3B-Instruct-2507 Q4_K_M, Ollama library version)
- ✅ 단일 source Ollama library (`qwen3:30b-a3b-instruct-2507-q4_K_M` blob `78b329e716e7`)
- ✅ 단일 measurement cycle — decode + prefill-2k 2 prompt ((g)/(h) 답습, Phase 1 답습)
- ✅ 명명 = "Phase 3.5-O" 채택 — 독립 cycle 단독 진행 + Phase 3.5 family 하위 (R-rec-7 답습)
- ❌ (h) llama.cpp 답습 = (h) cycle 완료 (변경 0건)
- ❌ (g) SSM hybrid 답습 = (g) cycle 완료 (변경 0건)
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **(g)+(h)+(h-O) 통합 본문 정정 cycle = 본 cycle 외** ((g)/(h) brief/합의 본문 변경 0건 답습 영구)
- ❌ **(g)+(h)+(h-O) 통합 *분석* cycle** ≠ 통합 *본문 정정* cycle = 별도 차원 carry-over
- ❌ MVP-1 R4 framing 본문 정정 cycle = 별도 cycle (R-9 답습 영구)
- ❌ 다른 quant (Q5_K_M / IQ4_XS / Q6_K) = 별도 cycle (R-rec-2 carry-over)
- ❌ Ollama API 외 다른 측정 도구 (llama-bench 등) = 별도 cycle (R-rec-12 격상 후보)

---

## 2. 모델 source — Ollama library 직접

### 2.1 본 cycle 확정 source (사용자 명시 2026-05-25 + (h) Agent C WebSearch raw verify)

> **본 cycle source = Ollama library `qwen3:30b-a3b-instruct-2507-q4_K_M` 단일 확정**. (h) Agent C WebSearch raw verify 답습 영구 — blob `78b329e716e7`, downloads 19.3M, qwen3 family `qwen3:30b-a3b` 의 quant variant.

| # | source | Ollama tag | 비고 |
|---|---|---|---|
| **O** | **Ollama library** | **`qwen3:30b-a3b-instruct-2507-q4_K_M`** | **✅ 본 cycle 확정 (사용자 명시 + R-S1 raw verify 답습)** |
| O-alt | Ollama library | `qwen3:30b-a3b` (default tag) | NOTE: default tag 가 본 cycle quant 동일 자격 verify 의무 (사용자 명시 별도) |
| O-modelfile | Ollama Modelfile 으로 (h) GGUF 직접 등록 | `FROM /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` | NOTE: 별도 cycle (사용자 명시) — (h) GGUF 와 Ollama library 동일 source verify 자격 |

### 2.2 source 사전 verify 의무

1. **Ollama daemon 상태 verify**: `curl -s http://127.0.0.1:11434/api/version` → version 답습 / `ollama list` → 기 다운로드 model 확인 (2026-05-25 직접 verify 결과 = `qwen3:30b-a3b-instruct-2507-q4_K_M` 기 다운로드 0건 → pull 필요)
2. **Ollama library blob verify**: `curl -sI https://registry.ollama.ai/v2/library/qwen3/blobs/sha256:<blob>` (사전 verify 자격 평가) 또는 `ollama show` (다운로드 *후* 가능)
3. **R-1 anchor 17회 추가** (mid-cycle 회차, pull *전* R-1 anchor + (h) 누계 16회 후속, R-3 답습)
4. **(h) 답습 정합성 확인** — Ollama library version 의 GGUF 가 (h) bartowski Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf 와 *동일 source 답습* 자격 verify (사전 단언 0, 단순 가설 — Ollama hub 가 bartowski conversion 답습 또는 자체 conversion 가능성, blob digest mismatch 시 다른 conversion lineage 명문 의무)

---

## 3. Ollama pull 절차

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습)

본 cycle egress = Ollama pull only. **apt install / pip install / git clone / HF egress 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구 (R-7 격리 답습). 본 cycle 도구 = `ollama pull` 단독 (Ollama daemon pid 3375 채널). **본 cycle sudo 사용 = §3.1 Step 1 단 1회 한정** (사용자 명시 임시 비밀번호 의무 답습, (g)/(h) 답습).

### 3.1 사전 조건 (egress 격리, R-7 답습, (h) §3.1 답습)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot) | `/tmp/phase3-5-h-o-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-h-o-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-h-o-disk-pre.txt` |
| 4 | **R-1 anchor 17회 추가** — `sha256sum /proc/3375/exe` ((h) 누계 16회 + 본 cycle (h-O) 사전 1회, 17번째 회차, hash baseline `ce95c475...878b10` 일관 답습 영구) | `/tmp/phase3-5-h-o-r1-anchor-17x.txt` |
| 5 | Ollama daemon status verify — `curl -s http://127.0.0.1:11434/api/version` + `ollama list` (기 다운로드 verify) | `/tmp/phase3-5-h-o-ollama-status.txt` |
| 6 | GPU + memory verify — `nvidia-smi` (idle) | `/tmp/phase3-5-h-o-gpu-pre.txt` |

### 3.2 Ollama pull 명령 (사용자 명시 후 실행)

> 🟡 **Ollama pull 채널 ≠ HF wget direct ((g)/(h) 답습)** — Ollama daemon (pid 3375) 통해 `registry.ollama.ai` egress. pid 3375 hash baseline 변경 0 의무 (mid-cycle R-1 anchor verify).

```bash
ollama pull qwen3:30b-a3b-instruct-2507-q4_K_M 2>&1 | tee /tmp/phase3-5-h-o-pull.log
# 예상 시간: ~18GB / Ollama pull throughput (시점 의존, ~5~15분 범위 가설)
```

### 3.3 Pull 후 verify

| Step | 명세 | 출력 |
|---|---|---|
| 1 | `ollama list` → `qwen3:30b-a3b-instruct-2507-q4_K_M` 적중 + size ~18GB 확인 | `/tmp/phase3-5-h-o-list-post.txt` |
| 2 | `ollama show qwen3:30b-a3b-instruct-2507-q4_K_M` → metadata (parameter_count, quantization, family, context_length) verify + (h) GGUF 답습 정합성 확인 ((h) qwen3moe arch / 30.5B/3.3B activated / 128 experts top-8 / 48 layers 답습 일치 자격) | `/tmp/phase3-5-h-o-show.txt` |
| 3 | **Ollama manifest digest verify** — Ollama models directory (`/home/delangi/.../ollama/models/manifests/registry.ollama.ai/library/qwen3/30b-a3b-instruct-2507-q4_K_M`) JSON 직접 read → blob digest 추출 + (h) WebSearch verify 답습 답습 (`78b329e716e7` prefix 일치 자격) | `/tmp/phase3-5-h-o-manifest.txt` |
| 4 | **R-1 anchor 18회 추가 (mid-cycle, R-3 답습)** — pull 후 verify 직전 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 §4 진입 자격 | `/tmp/phase3-5-h-o-r1-anchor-18x.txt` |
| 5 | egress baseline post-pull + 디스크 사용량 post-pull | `/tmp/phase3-5-h-o-egress-post-pull.txt`, `/tmp/phase3-5-h-o-disk-post-pull.txt` |

→ Step 1·2·3 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 (pull 실패 또는 metadata mismatch) 발동

---

## 4. 측정 절차 (Ollama /api/generate API, Phase 1 답습 + (h) prompt 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | 다른 model unload (`/api/generate` + `keep_alive: 0` 으로 qwen3-coder-next, qwen2.5-coder:32b 등 cleanup) — GPU 메모리 0 확인. **R-1 anchor 19회 추가** (mid-cycle, 측정 *전*) — `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 후 측정 진입 자격 |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama\|claude"` |
| 3 | GPU 상태 verify — `nvidia-smi --query-gpu=memory.used,utilization.gpu,temperature.gpu --format=csv` (idle 확인, thermal baseline) |
| 4 | Ollama daemon health — `curl -s http://127.0.0.1:11434/api/version` |

### 4.2 측정 명령 (Phase 1 답습 protocol, (h) prompt 답습)

> 🟡 **prompt 답습**: (h) decode-161tok prompt + prefill-2k prompt 동형 답습 (절대 경로 한국어 큰따옴표 인용, R-9 답습). 단 Ollama API token 분모 = `prompt_eval_count` + `eval_count` 사용 (llama-cli perf line 과 다른 분모 가능성 정직성 명문 의무).

> 🟡 **측정 protocol**:
> - 본 cycle = 단일 측정 cycle 답습 ((g)/(h) 답습) — 단 Phase 1 답습 = N=3 repetitions + mean ± std 자격 평가 (사용자 명시 별도 cycle 결정 의무)
> - 본 cycle 단계 = cold load (`keep_alive: 0` 후 첫 호출) + warm (직후 재호출) 한 쌍
> - Phase 1 `qwen3-coder-next` decode 7.83 ± 0.36 답습 (단 다른 모델 SSM hybrid 80B)
> - (h) llama.cpp decode 49.6 vs (h-O) Ollama X — 1:1 동일 모델 직접 비교 핵심

```bash
# decode-161tok prompt (Phase 1 답습 protocol)
PROMPT_DECODE=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt")
curl -s http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_DECODE" '{
        model: "qwen3:30b-a3b-instruct-2507-q4_K_M",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    2>&1 | tee /tmp/phase3-5-h-o-measure-decode-161tok.json

# prefill-2k prompt
PROMPT_PREFILL=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt")
curl -s http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_PREFILL" '{
        model: "qwen3:30b-a3b-instruct-2507-q4_K_M",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    2>&1 | tee /tmp/phase3-5-h-o-measure-prefill-2k.json
```

### 4.3 측정 항목 (Phase 1 답습 + (h) 직접 비교)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| Ollama decode tok/s | `eval_count / eval_duration * 1e9` (Phase 1 답습) | Ollama 측정 분모 = eval_count, llama.cpp 분모 = generation token count (llama-cli perf line) — 동일 자격 verify 의무 |
| Ollama prefill tok/s | `prompt_eval_count / prompt_eval_duration * 1e9` | 동상 |
| total wall-clock | `total_duration / 1e9` (nanoseconds → seconds) | 빌드·로딩·측정 합산 |
| eval_count vs llama.cpp generation count | (h) decode `n_predict 256` + Phase 1 동형, Ollama `num_predict 256` 동일 → 분모 일치 자격 강함 (단 verify 의무) | tok/s 비교 자격 정확성 |
| prompt_eval_count vs llama.cpp prompt count | (h) prompt = 153 tokens (llama.cpp re-tokenize), Ollama prompt_eval_count = ? | tokenizer 차이 가능성 정직성 명문 |
| GPU memory peak | `nvidia-smi` polling | 단일 측정 지점 |
| GPU temperature polling (R-rec-3 답습) | `nvidia-smi --query-gpu=temperature.gpu --format=csv -l 5` background, threshold 85°C 5분 명문 | 5분 이상 thermal 정직성 |
| **(h) llama.cpp 직접 비교 (핵심)** | (h) decode-161tok generation **49.6** t/s / prefill-2k generation **45.4** t/s / decode prompt **389.4** t/s / prefill prompt **1916.8** t/s ((h) F-1 답습) | 본 cycle 핵심 결과 — model + quant + prompt + hardware 통제 동일, 1 변수만 inference engine 차이 |
| **Phase 1 Ollama baseline (간접)** | qwen3-coder-next decode 7.83 ± 0.36 / qwen2.5-coder:32b decode 4.62 ± 0.18 | 본 cycle (h-O) Qwen3-30B-A3B-Instruct-2507 = Phase 1 과 다른 model (model 변수 미분리 framing) |

**측정 종료 후 R-1 anchor 20회 추가 (R-3 답습)** — 측정 직후 `sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 ((g)/(h) §5 답습, R-S3 발효 framing 약화)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | `ollama pull` 성공 + `ollama list` 적중 + 측정 완료 (tok/s 실수치 획득) | raw report → **(h) vs (h-O) 1:1 비교 framing (§9)** → inference engine 변수 단독 분리 *직접* evidence → MVP-1 R4 framing 강화/정정 input 강함 (단 본문 정정 별도 cycle R-9 답습 영구) |
| **B1 (pull 실패)** | Ollama pull 실패 (404, network, disk, manifest 미일치) | raw report → 다른 source 평가 (O-alt 또는 O-modelfile) 또는 보류 (사용자 명시 별도) |
| **B2 (runtime 에러)** | Ollama load 실패, OOM, CUDA error | raw report → Ollama Modelfile (O-modelfile) 자격 평가 또는 quant 변경 (별도 cycle) |
| **B3 (네트워크 차단)** | Ollama registry timeout | raw report → 다른 source/시간 재시도 (별도 명시) |
| **B4 (디스크 부족)** | pull 중 ENOSPC | 즉시 중단 → (g) Q4_K_M (R-13 보존) cleanup 사용자 명시 후 재시도 |
| **B5 (Ollama manifest digest mismatch, R-6 답습)** | Ollama models manifest digest ≠ Agent C WebSearch verify (`78b329e716e7`) | raw report → **Ollama 자체 sha256 verify 자동 (manual quarantine 자격 0 가능성)** + 사용자 명시 분기 의무 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 17 항목)

1. **Ollama library = bartowski (HF) 답습 자격 verify 의무** — Ollama hub 의 GGUF 가 (h) bartowski conversion 답습인지 자체 conversion 인지 사전 단언 0. manifest digest verify 답습 필요 — 다른 conversion lineage 시 inference engine 단독 분리 자격 약화
2. **inference engine 변수 단독 분리 자격 *강함*** — model + quant + prompt + hardware (GB10) 모두 동일, llama.cpp `c0c7e147` 직접 ↔ Ollama 0.20.4 (embedded llama.cpp version 별도)
3. **미통제 변수 — 측정 도구 framework**: llama-cli (interactive hang) vs Ollama /api/generate (HTTP API + JSON response) — 측정 추출 방법론 차이
4. **미통제 변수 — Ollama embedded llama.cpp version**: Ollama 0.20.4 의 내부 llama.cpp version ≠ (h) 의 llama.cpp `c0c7e147` 가능성 (Ollama release version 답습)
5. **미통제 변수 — Ollama internal caching/optimization**: Ollama 자체 KV cache 관리 + scheduling + warm-up 정책 (llama-cli `--no-warmup` 답습 대 Ollama default behavior)
6. **미통제 변수 — tokenizer 차이 가능성**: Ollama internal tokenizer vs (h) llama-cli tokenizer (Ollama prompt_eval_count vs llama.cpp re-tokenize 153 tokens 답습 verify 의무)
7. **분모 mismatch 가능성**: Ollama eval_count vs llama.cpp generation token count — 일치 자격 verify 의무
8. **R-23 위반 가능성** — pull ~5~15분 + 측정 ~5~30분 wall-clock 중 다른 활동 발생 가능
9. **egress 비례성** — **~18GB egress = (g)+(h)+(h-O) 누계 ~80GB** (Phase 1 ~10GB 답습 대비 ~8×, R-11 답습)
10. **디스크 비례성** — Ollama models cache 위치 별도 (`~/.ollama/models/` 또는 docker volume) — `df -h` 직접 verify 의무 (디스크 ~85% 유지 자격 평가)
11. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습) — Phase 1 N=3 repetitions 답습 자격 = 별도 cycle 의무
12. **GPU thermal throttling 가능성** — 5분 이상 연속 측정 시 영향 (R-rec-3 polling 명문)
13. **Ollama daemon pid 3375 hash baseline 보존** — silent 교체 0건 답습 영구 (R-1 anchor 17·18·19·20회 답습 의무)
14. **Phase 1 F2 가설 강화/약화 framing 분리**:
    - 본 cycle (h-O) tok/s < (h) tok/s → F2 가설 (Phase 1 ~4.07× Ollama 느림) *답습 강화*, (h)/(h-O) 비교는 동일 모델 → Phase 1 model 변수 분리 효과
    - 본 cycle (h-O) tok/s ≈ (h) tok/s → F2 가설 *부분 부정* (Ollama embedded llama.cpp 호환 효율성 강함)
    - 본 cycle (h-O) tok/s > (h) tok/s → F2 가설 *역방향 강화* ((g) F-1 + (h) F-1 답습 일관)
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
15. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
16. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
17. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무

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
11. ❌ (j)/(k)/(l)/(m)/(n) 자동 진입
12. ❌ brief commit 자동 진입
13. ❌ Ollama pull 시점 = 사용자 명시 *직접* 의무 (R-11 비례성 답습)
14. ❌ (g)+(h)+(h-O) 통합 본문 정정 ((g)/(h) brief/합의 본문 변경 0건) + (g)+(h)+(h-O) 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원 carry-over)
15. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 (chain 영구 종결 의무 답습 영구)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (h-O) < (h) (Ollama 느림 답습) | F2 가설 (Phase 1) 답습 강화 + MVP-1 R4 framing *정정 강한 input* → 본문 정정 별도 cycle HIGH |
| G + (h-O) ≈ (h) (Ollama embedded 효율성) | F2 가설 *부분 부정* + MVP-1 R4 framing *답습 자격* → 본문 정정 약화 |
| G + (h-O) > (h) (Ollama 빠름, 역방향) | F2 가설 *역방향 강화* ((g) F-1 + (h) F-1 답습 일관, 단 inference engine 변수 단독 분리 측면) |
| B1~B5 | 다른 source 또는 (h) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **MVP-1 합의 R4 framing 강화/정정 evidence 별도 cycle** | **HIGH** | (g) F-1 + (h) F-1 + (h-O) 결과 종합 input 강함 (R-9 답습 영구) |
| **(g)+(h)+(h-O) 3-way 통합 *분석* cycle** | MEDIUM | 변수 분리 종합 + Provider Liquidity finding 종합 |
| **llama.cpp graceful tensor name resolution 검증 cycle** | MEDIUM | (g) F-2 + (h) R-S3 답습 read-only |
| **(j) advisory wall-clock 측정** | MEDIUM | 자비스 비전 직접 진전 |
| **Phase 1 N=3 repetitions 답습 cycle** | MEDIUM | 재현성 평가 자격 강화 (단 cost ~2× 시간) |
| **(k) M3·M4 결정 *고정*** | DEFER | (h) + (h-O) input 자격 강화 후 평가 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 의무 답습 영구 |
| **bartowski 답습 vs Ollama 자체 conversion verify cycle** | LOW | manifest digest cross-check |
| **(g)+(h)+(h-O) 통합 본문 정정 cycle** | DEFER | 사용자 명시 별도 cycle, (g)/(h) brief/합의 본문 변경 0건 |
| `llama-bench` carry-over (R-rec-12 격상) | MEDIUM | 자동 통계 + interactive 차단 |
| 다른 quant 비교 (Q5_K_M / IQ4_XS) | LOW | R-rec-2 답습 |
| 다른 모델 cross-comparison (Qwen3-Next-7B / Qwen2.5 etc.) | LOW | R-12 답습 (단일 변수 분리 cycle) |
| Ollama Modelfile (h) GGUF 직접 등록 cycle | LOW | (h) GGUF = Ollama library 동일 source verify 자격 |
| (m) §12 Ollama 위생 정정 | LOW | 본 cycle 무관 (Ollama 위생 별도) |
| (n) Phase 3 brief v1.2 보강 | LOW | 본 cycle 결과 흡수 자격 별도 평가 |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((g)/(h) 동형 풀 7단계 답습, 사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| **(1) brief v1 작성 + commit (본 단계)** | 본 brief v1 entry plan only, 합의 *전* | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | Agent A/B/C 병렬 독립 + Reviewer 통합 | 사용자 명시 후 |
| (3) brief v1.1 보강 + commit | 합의 BLOCKING verbatim 100% + R-S* 흡수 + 권고/NOTE 흡수 | 사용자 명시 후 |
| (4) Ollama pull 실행 (~5~15분 wall-clock) | `ollama pull qwen3:30b-a3b-instruct-2507-q4_K_M` (R-7 답습) | **사용자 명시 *직접* 의무 (~18GB egress)** |
| (5) verify + 측정 실행 (~15~45분 wall-clock) | §3.3 + §4 절차 답습 | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (g)/(h) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (h) vs (h-O) 비교 framing (본 cycle 핵심 가치, inference engine 변수 단독 분리)

### 9.1 (h) 측정값 답습 (직접 비교 baseline)

| 항목 | (h) llama.cpp `c0c7e147` 직접 | 측정 방법 비고 |
|---|---|---|
| decode-161tok 측정 명령 perf line | `[ Prompt: 389.4 t/s \| Generation: 49.6 t/s ]` | 단일 perf line, prompt + generation 동시 |
| prefill-2k 측정 명령 perf line | `[ Prompt: 1916.8 t/s \| Generation: 45.4 t/s ]` | 동상 |
| 모델 | Qwen3-30B-A3B-Instruct-2507, ~30.5B total / ~3.3B activated | classical MoE, 128 experts top-8, SSM 미포함 |
| quant | Q4_K_M (bartowski conversion, imatrix) | (h) 답습 |
| GGUF 크기 | 17.353 GiB (18,632,183,808 bytes) | (h) 답습 |
| 측정 도구 | llama-cli `-no-cnv` + `< /dev/null` + `timeout 300s` | interactive hang (g) F-8 답습 영구 |

### 9.2 (h-O) 예상 결과 시나리오 5 (사전 가설 평가, 단정 0)

| 시나리오 | (h-O) decode tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: Ollama 느림 (~10~30 t/s)** | F2 가설 (Phase 1 ~4.07× Ollama 느림) 답습 강화. Ollama embedded llama.cpp version + 자체 caching overhead | MVP-1 R4 framing *정정 강한 input* (별도 cycle HIGH) | F2 가설 framing 정정 cycle (별도) |
| **S2: Ollama 동급 (~40~55 t/s)** | F2 가설 *부분 부정* — Ollama embedded llama.cpp 효율성 동급 | MVP-1 R4 framing *답습 자격* (정정 약화) | (g)+(h)+(h-O) 통합 *분석* cycle |
| **S3: Ollama 빠름 (~60~80 t/s)** | F2 가설 *역방향 강화* — Ollama 자체 최적화 우위 | (g) F-1 + (h) F-1 답습 측면 격차 *모델 의존* 가설 | F2 재고 + 모델 의존성 cycle |
| **S4: Pull 실패 (B1)** | source 차단 — Ollama library version 비호환 | B1 분기 발동 | 다른 source 또는 Modelfile (O-modelfile) cycle |
| **S5: tokenizer 차이 발견** | Ollama prompt_eval_count ≠ llama.cpp re-tokenize 153 tokens → tok/s 분모 mismatch | tokenizer 변수 분리 cycle | tokenizer 변수 단독 분리 cycle (R-rec-9 답습) |

### 9.3 핵심 정직성 (변수 단독 분리 강함 framing)

- ✅ **본 cycle = 본 프로젝트 최초 단일 변수 분리 직접 비교** — model + quant + prompt + hardware 모두 (h) 와 동일, 1 변수만 inference engine 차이
- ❌ **미통제 변수**: 측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이 가능성
- → **(h) vs (h-O) 단일 trial = inference engine *직접* input** (단 측정 도구 framework 미통제 부분 정직성 명문)
- **Phase 1 F2 (~4.07× Ollama 느림) 결정적 input** = (h-O) tok/s 결과 → F2 가설 강화/약화/역전 직접 evidence (단 본문 정정 별도 cycle R-9 답습 영구)

---

## 10. 본 brief v1 본 cycle 진입 자체 영구 권위

- 본 brief v1 = (h) cycle 완료 (`fccec6a`) + 사용자 명시 (h-O) 진입 형태 + Ollama pull 진행 + Phase 3.5-O 명명 직후 entry plan
- 본 brief 자체 머신 변경 0건 (pull/측정/sudo 0건)
- 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)
- (h-O) cycle = 본 프로젝트 최초 inference engine 변수 단독 분리 cycle — (g)/(h) 답습 model + quant + prompt + hardware 4 차원 통제 후 1 차원 분리

---

**본 brief v1 작성 완료** (Phase 3.5-O (h-O) Ollama 직접 측정 cycle entry plan, (g)/(h) 동형 7단계 답습 + inference engine 변수 단독 분리 핵심 가치 명문 + Ollama library `qwen3:30b-a3b-instruct-2507-q4_K_M` 단일 source + 비교 framing 5 시나리오 + 정직성 한계 17 항목. 본 cycle 머신 변경 0건. 다음 단계 = 풀 3+1 합의 진행 사용자 명시 의무.)
