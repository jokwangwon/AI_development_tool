# Jarvis MVP-1 V-1 PoC Phase 3.5-OM (h-OM) entry brief (v1, Ollama Modelfile bartowski GGUF 직접 등록 cycle, 합의 *전* entry plan)

> **본 brief v1 = (h-OM) Phase 3.5-OM Ollama Modelfile (h) GGUF 직접 등록 cycle 의 entry plan only.** v1 진입 자격 = (h-O) Phase 3.5-O cycle 정리 commit `9685ae3` 직후 사용자 명시 (h-OM) 직접 선택 + 4 명확화 ((h-O) 동형 7단계 + Modelfile TEMPLATE (h-O) library 답습 (ChatML + temp 0.7 + top_k 20 + top_p 0.8)). 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구). 실 변경 = 본 brief v1 commit + push 만. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-O (h-O) cycle 정리 commit `9685ae3` 직후, 본 (h-OM) cycle 단계 (1) brief v1)
**카테고리**: V-1 PoC Phase 3.5-OM (h-OM) entry brief v1 (Phase 3 carry-over (h-O) R-S1 발효 직접 후속, 본 cycle 핵심 = **source conversion lineage 100% 통제 + inference engine 변수 *진짜* 단독 분리** — (h) bartowski GGUF (sha256 `382b4f5a164d...33a95`) 를 Ollama Modelfile 로 직접 등록, (h) ↔ (h-O) ↔ (h-OM) 3-way 비교 framing 완성)
**범위**: (1) bartowski GGUF → Ollama Modelfile 등록 절차 (host hard link + Modelfile 작성 + ollama create) / (2) Ollama /api/generate 측정 절차 ((h-O) cold 측정 답습) / (3) 분기 (G·B1~B7) / (4) (h) llama.cpp + (h-O) library + (h-OM) bartowski 3-way 비교 framing / (5) 후속 carry-over

**답습 권위**:
- **Phase 3.5-O (h-O) cycle 정리 commit** (`9685ae3`, SESSION 16번째 entry, F-1 S1 confirmed ~3.24~23.89× + F-3 R-S1 완전 raw evidence + R-1 anchor 19회 누계) — 본 (h-OM) 직접 선행 cycle, R-S1 발효 직접 carry-over source 영구
- **Phase 3.5-O (h-O) brief v1.1** (`e77e8d7`, 476줄, BLOCKING 14 + R-S1~R-S5 흡수)
- **Phase 3.5-O (h-O) 풀 3+1 합의** (`37bcd40`, 459줄)
- **Phase 3.5-O (h-O) raw summary** (`docs/phase0/v1-poc-raw/phase3-5-h-o/2026-05-25T21-03-phase3-5-h-o-summary.json`)
- Phase 3.5-B (h) cycle 정리 commit (`fccec6a`, 15번째 entry, F-1 classical MoE > SSM hybrid + bartowski GGUF sha256 `382b4f5a164d...33a95`)
- (h) raw measurement (`docs/phase0/v1-poc-raw/phase3-5-h/2026-05-25T17-58-phase3-5-h-summary.json`)
- Phase 1 summary (`docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json`)
- MVP-1 합의 R4 "llama.cpp ↔ Ollama 동급" — input only (R-9 답습 영구)
- ADR-011 §2.1 5조건 + 헌법 5조-2 (Provider Liquidity, 비협상)
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter` / `project_mvp_staged_roadmap`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. (h) bartowski GGUF (`/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf`, sha256 `382b4f5a164d...33a95`, 17.353 GiB) 를 Ollama Modelfile 로 직접 등록 절차 명문 — host hard link (동일 filesystem `/dev/nvme0n1p2 ext4` 답습, 디스크 추가 0건) + Modelfile 작성 + `ollama create` 절차
2. Modelfile TEMPLATE + PARAMETER = (h-O) library `qwen3:30b-a3b-instruct-2507-q4_K_M` 답습 (ChatML + temp 0.7 + top_k 20 + top_p 0.8 + repeat_penalty 1 + stop `<|im_start|>` `<|im_end|>`)
3. 측정 절차 명문 — (h-O) cold 측정 답습 + Phase 1 답습 protocol (decode + prefill-2k)
4. 분기 조건 명문 — G 성공·B1 Modelfile syntax 에러·B2 ollama create 실패·B3 model load 실패·B4 디스크·B5 Ollama runtime 에러·B6 tokenizer 분모 mismatch·B7 measurement HTTP error
5. 정직성 한계 명문 18 항목 (§6) — source conversion lineage 100% 통제 자격 강함 + 단 4 미통제 변수 잔존 (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이) + Ollama Modelfile 생성 시 internal optimization 변경 가능성 정직성
6. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
7. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구 + 3-way 통합 분석 cycle HIGH 자격 격상
8. (h) ↔ (h-O) ↔ (h-OM) 3-way 비교 framing 명문 (§9) — source conversion 통제 직접 evidence + Δ(h-O, h-OM) = Ollama internal optimization 분리, Δ(h, h-OM) = inference engine *진짜* 단독 분리

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 Modelfile 작성 / ollama create / 측정 / sudo 실행** — 본 brief = entry plan only, 합의 *전*
2. ❌ **Ollama daemon 상태 변경 (pid 3375)** — keep_alive 0 unload 만, R-1 anchor hash baseline `ce95c475...878b10` 일관 보존 (19회 누계 답습 영구)
3. ❌ **(h) GGUF 파일 변경 또는 cleanup** — `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` 보존 (R-13 답습 영구, hard link source 의무)
4. ❌ **(g) GGUF 파일 변경** — `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` 보존
5. ❌ **(h-O) Ollama library blob 변경** — `qwen3:30b-a3b-instruct-2507-q4_K_M` (blob `78b329e716e7...ba9cc`) 보존
6. ❌ **llama.cpp HEAD `c0c7e147` 변경** — (h) 측정 baseline 보존
7. ❌ **MVP-1 합의 본문 자동 정정** — R4 framing input only (R-9 답습 영구)
8. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — Provider Liquidity finding evidence input only (R-9 답습 영구)
9. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle 의무 답습 영구
10. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
11. ❌ **메모리 자동 갱신** — 사용자 명시 의무
12. ❌ **(j)/(k)/(l)/(m)/(n) 자동 진입** — 사용자 명시 의무 답습 영구
13. ❌ **본 brief 자동 commit 진입** — 사용자 명시 후
14. ❌ **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정** — 본 cycle = 별도 cycle 단독 진행, 기존 brief/합의 본문 변경 0건
15. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime 자동 진입** — chain 영구 종결 의무 답습 영구
16. ❌ **새 bartowski GGUF 다운로드** — 본 cycle = host (h) GGUF 답습 hard link only, egress 0 의무

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger

- **Phase 3.5-O (h-O) cycle 완료** (`9685ae3`, SESSION 16번째 entry):
  - F-1 ⭐⭐⭐: S1 시나리오 confirmed — Ollama < llama.cpp 모든 차원 ~3.24~23.89× (decode 49.6→15.29 / prefill 45.4→12.43 / prefill prompt 1916.8→80.25)
  - F-2 ⭐⭐⭐: prefill prompt 23.89× outlier (Ollama framework overhead 우세 가설)
  - F-3 ⭐⭐⭐: R-S1 완전 raw evidence (Ollama blob sha256 full 64자 = `78b329e716e7e9775973d392cd132b1f1ff1c8287a992887caeb6fd6c56ba9cc` ≠ (h) bartowski sha256 `382b4f5a164d...33a95` = 다른 source 확정)
  - (h-O) 풀 3+1 합의 **R-S1 발효 (h-OM) HIGH carry-over** = O-modelfile 대안 (bartowski conversion lineage 100% 통제 + egress 0 + 3-way 비교 framing)
- **본 cycle 핵심 가치 = source conversion lineage 100% 통제 + inference engine *진짜* 단독 분리**:
  - (h) Qwen3-30B-A3B-Instruct-2507 Q4_K_M (bartowski sha256 `382b4f5a164d...33a95`) + llama.cpp `c0c7e147` direct = decode **49.6** / prefill **45.4** t/s
  - (h-O) Qwen3-30B-A3B-Instruct-2507 Q4_K_M (Ollama library, blob `78b329e716e7...ba9cc`, **다른 source**) + Ollama 0.20.4 (Docker) = decode **15.29** / prefill **12.43** t/s
  - (h-OM) **(h) bartowski GGUF 답습 (sha256 `382b4f5a164d...33a95`)** + Ollama 0.20.4 (Docker) = decode X / prefill Y t/s
  - → **3-way 비교 가능**:
    - Δ(h, h-OM) = inference engine *진짜* 단독 분리 (source 100% 동일)
    - Δ(h-O, h-OM) = Ollama internal optimization 변수 (source 다름, engine 동일 Ollama 0.20.4)
    - Δ(h, h-O) = (h-O) 답습 = inference engine + source 2 차원 변경 (이미 답습)
- **본 cycle 비용**: egress **0건** (host (h) GGUF 답습 hard link) + 디스크 **0건** (hard link 동일 inode, 동일 filesystem `/dev/nvme0n1p2 ext4` 답습) + Ollama models cache blob storage 증가 가능성 verify 의무
- **사용자 비전 직접 진전** = [[project_jarvis_local_boss_direction]] + [[project_minimize_user_intervention]] + [[feedback_provider_liquidity]] (model + inference engine 양차원 통제, 단일 변수 분리)

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | (h) bartowski GGUF (host path) 의 Ollama Modelfile 등록 절차 = container mount path 답습 + ollama create 성공 가능? | Y/N + Modelfile + `ollama create` stdout/stderr + `ollama list` 직접 verify |
| **Q2** | (h-OM) decode/prefill tok/s = ? (h-O cold 측정 동형) | Phase 1 답습 measurement protocol, cold 측정 우선 (R-S3 답습 영구) |
| **Q3** | Δ(h, h-OM) = inference engine *진짜* 단독 분리 — (h) 49.6 vs (h-OM) X 격차 = inference engine framework 자체 차이? | 단순 inference engine 단독 변수 분리 evidence (source 100% 통제, (h)/(h-OM) 동일 bartowski GGUF) |
| **Q4** | Δ(h-O, h-OM) = Ollama internal optimization 변수 — (h-O) 15.29 vs (h-OM) X 격차 = source conversion lineage 차이 (Ollama library version vs bartowski) ? | 동일 engine + 다른 source = conversion 변수 evidence (단 동일 quant scheme, 단 imatrix dataset 차이 가능) |
| **Q5** | Provider Liquidity finding 강화 자격 결정적 평가? | (g)/(h)/(h-O)/(h-OM) 4-way 종합 input → MVP-1 R4 framing 정정 결정적 evidence (단 본문 정정 별도 cycle 의무 R-9 답습 영구) |
| **Q6** | F2 가설 (Ollama 효율성 = format-internal 차이) 답습 vs 정정 결정적 평가? | (h-OM) source 통제 후 격차 = Ollama framework overhead 단독 자격 평가 |

### 1.3 본 cycle 범위 한정 (R-rec-7 답습)

- ✅ 단일 source = (h) bartowski GGUF (`/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf`, sha256 `382b4f5a164d...33a95`)
- ✅ host hard link 방식 (egress 0 + 디스크 추가 0건)
- ✅ Modelfile TEMPLATE + PARAMETER = (h-O) library 답습 (ChatML + 6 PARAMETER 정확 답습)
- ✅ 단일 measurement cycle — decode + prefill-2k cold 측정 우선 ((h-O) 답습)
- ✅ 명명 = "Phase 3.5-OM" 채택 — 독립 cycle 단독 진행 + Phase 3.5 family 하위 (R-rec-7 답습)
- ❌ (h) llama.cpp 답습 = (h) cycle 완료 (변경 0건)
- ❌ (h-O) Ollama library 답습 = (h-O) cycle 완료 (변경 0건)
- ❌ (g) SSM hybrid 답습 = (g) cycle 완료 (변경 0건)
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **다른 Modelfile TEMPLATE/PARAMETER 변경 cycle = 본 cycle 외** (Modelfile setting 변수 단독 분리 cycle 별도)
- ❌ **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정 cycle = 본 cycle 외** (기존 brief/합의 본문 변경 0건 답습 영구)
- ❌ **4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle** = 별도 차원 carry-over
- ❌ MVP-1 R4 framing 본문 정정 cycle = 별도 cycle (R-9 답습 영구)
- ❌ 다른 quant 비교 = 별도 cycle (R-rec-2 carry-over)

---

## 2. 모델 source — (h) bartowski GGUF 직접 답습 (R-S1 발효 직접 통제)

### 2.1 본 cycle 확정 source (사용자 명시 + R-S1 답습)

> **본 cycle source = (h) bartowski/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf 답습 (host hard link)**. (h) cycle raw verify 답습 — sha256 `382b4f5a164d200f93790ee0e339fae12852896d23485cfb203ce868fea33a95` (full 64자 답습 영구), 17.353 GiB (18,632,183,808 bytes). bartowski conversion lineage 100% 통제 자격 강함.

| # | source | path / 식별자 | 비고 |
|---|---|---|---|
| **OM** | **(h) bartowski GGUF hard link** | host: `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (sha256 `382b4f5a164d...33a95`, 17.353 GiB) → container: `/root/.ollama/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (hard link via host `/home/delangi/문서/.../bootcamp_game/ollama-data/imports/`) | **✅ 본 cycle 확정 (사용자 명시 + R-S1 답습)** |
| OM-alt | (h) bartowski GGUF copy | 동상, 단 hard link 대신 cp (디스크 추가 17.353 GiB) | NOTE: hard link 차단 시 fallback (사용자 명시 별도) |
| OM-symlink | (h) bartowski GGUF symlink | symlink (단 container 내 host root path access 0건 가능성) | NOTE: 사전 verify 의무 (별도 cycle), 본 cycle 부적정 가능성 |

### 2.2 source 사전 verify 의무

1. **(h) bartowski GGUF 존재 verify**: `ls -la /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` → 17.353 GiB / 18,632,183,808 bytes 일치 확인 + sha256 verify (`sha256sum` = `382b4f5a164d...33a95` 답습)
2. **Filesystem hard link 가능 verify**: `df -T <host_path>` + `df -T /home/delangi/문서/.../bootcamp_game/ollama-data/` → 동일 filesystem (`/dev/nvme0n1p2 ext4`) 확인 (직접 verify 답습 ✓)
3. **Container mount 답습 verify**: `sudo docker inspect oracle-game-ollama` → `/home/delangi/문서/.../bootcamp_game/ollama-data` → `/root/.ollama` mount 답습 확인
4. **`imports/` directory 생성 의무**: `mkdir -p /home/delangi/문서/.../bootcamp_game/ollama-data/imports/` (Ollama daemon access 권한 답습 의무)
5. **R-1 anchor 21회 추가** (mid-cycle pre-create, (h-O) 누계 19회 + 본 cycle (h-OM) 사전 1회 가설 = ... 단 (h) summary line 72 답습 = 누계 15 + (h-O) 4회 = 19회 + 본 cycle (h-OM) 4회 추가 = 23회 누계 종료 시점). hash baseline `ce95c475...878b10` 일관 답습 영구

---

## 3. Modelfile + ollama create 절차 (R-S1 발효 직접 통제)

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습)

본 cycle egress = **0건 의무** (host (h) GGUF 답습 hard link, Ollama pull 0건). **apt install / pip install / git clone / HF egress / Ollama pull 0건 의무**. 사용자 명시 후 의도-외 추가 egress 0건 답습 영구. 본 cycle sudo 사용 = §3.1 Step 1 (egress baseline pre) + Step 5 (R-1 anchor 21x) + §3.2 (mkdir + hard link) + §3.4 (R-1 anchor 22x) + §4.1 (R-1 anchor 23x) + 측정 종료 (R-1 anchor 24x) + 측정 후 baseline = **최소 6~8회 sudo 호출 예상** (사용자 명시 임시 비밀번호 의무 답습 ((h)/(h-O) 답습)).

### 3.0.1 (g)/(h)/(h-O) preservation 답습 (R-13 답습 영구)

(g) `/home/delangi/models/phase3-5/Qwen_Qwen3-Next-80B-A3B-Instruct-Q4_K_M.gguf` (45.38 GiB) + (h) `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (17.353 GiB) + (h-O) Ollama library blob (17.28 GiB, Docker volume) 모두 보존 답습 영구. **본 cycle hard link = (h) GGUF 의 동일 inode 사용 (디스크 추가 0건)**.

### 3.1 사전 조건 (egress 격리 + R-1 anchor 21회)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established` snapshot) | `/tmp/phase3-5-h-om-egress-baseline-pre.txt` |
| 2 | apt snapshot pre (`dpkg -l \| wc -l` + `apt list --upgradable`) | `/tmp/phase3-5-h-om-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre (`df -h /home/delangi`) | `/tmp/phase3-5-h-om-disk-pre.txt` |
| 4 | (h) GGUF + Ollama mount path verify (§2.2 답습) | `/tmp/phase3-5-h-om-paths-verify.txt` |
| 5 | **R-1 anchor 21회 추가** — `sudo sha256sum /proc/3375/exe` (누계 20회 + 본 cycle 1회 = 21회, hash baseline `ce95c475...878b10` 일관 답습 영구) | `/tmp/phase3-5-h-om-r1-anchor-21x.txt` |
| 6 | Ollama daemon status + 기 다운로드 list verify | `/tmp/phase3-5-h-om-ollama-status.txt` |
| 7 | GPU + memory verify (idle, R-rec-3 thermal baseline) | `/tmp/phase3-5-h-om-gpu-pre.txt` |

### 3.2 Modelfile 작성 + hard link 절차

**Step 1: Container mount path 내 imports directory 생성**:
```bash
sudo mkdir -p /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports
sudo chmod 755 /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports
```

**Step 2: (h) bartowski GGUF hard link 생성** (디스크 추가 0건):
```bash
# 동일 filesystem (`/dev/nvme0n1p2 ext4`) → hard link 가능
sudo ln /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
    /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
# inode 확인 (양 path 동일 inode 자격 verify)
ls -li /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
ls -li /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
```

**Step 3: Modelfile 작성 (host path 내, container 내 read-only 답습)**:
```bash
cat > /tmp/Modelfile-h-om <<'MODELFILE_EOF'
FROM /root/.ollama/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
TEMPLATE """{{- $lastUserIdx := -1 -}}
{{- range $idx, $msg := .Messages -}}
{{- if eq $msg.Role "user" }}{{ $lastUserIdx = $idx }}{{ end -}}
{{- end }}
{{- if or .System .Tools }}<|im_start|>system
{{ if .System }}{{ .System }}

{{ end }}
{{- if .Tools }}# Tools

You may call one or more functions to assist with the user query.

You are provided with function signatures within <tools></tools> XML tags:
<tools>
{{- range .Tools }}
{"type": "function", "function": {{ .Function }}}
{{- end }}
</tools>

For each function call, return a json object with function name and arguments within <tool_call></tool_call> XML tags:
<tool_call>
{"name": <function-name>, "arguments": <args-json-object>}
</tool_call>
{{- end -}}
<|im_end|>
{{ end }}
{{- range $i, $_ := .Messages }}
{{- $last := eq (len (slice $.Messages $i)) 1 -}}
{{- if eq .Role "user" }}<|im_start|>user
{{ .Content }}<|im_end|>
{{ else if eq .Role "assistant" }}<|im_start|>assistant
{{ if .Content }}{{ .Content }}{{ end }}
{{- if .ToolCalls }}
{{- range .ToolCalls }}
<tool_call>
{"name": "{{ .Function.Name }}", "arguments": {{ .Function.Arguments }}}
</tool_call>
{{- end }}
{{- end }}{{ if not $last }}<|im_end|>
{{ end }}
{{- else if eq .Role "tool" }}<|im_start|>user
<tool_response>
{{ .Content }}
</tool_response><|im_end|>
{{ end }}
{{- if and (ne .Role "assistant") $last }}<|im_start|>assistant
{{ end }}
{{- end }}"""
PARAMETER temperature 0.7
PARAMETER top_k 20
PARAMETER top_p 0.8
PARAMETER repeat_penalty 1
PARAMETER stop <|im_start|>
PARAMETER stop <|im_end|>
MODELFILE_EOF
sudo cp /tmp/Modelfile-h-om /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports/Modelfile
```

**Step 4: `ollama create` via docker exec**:
```bash
sudo docker exec oracle-game-ollama ollama create qwen3-30b-a3b-instruct-2507-bartowski -f /root/.ollama/imports/Modelfile 2>&1 | tee /tmp/phase3-5-h-om-create.log
```

### 3.3 Create 후 verify

| Step | 명세 | 출력 |
|---|---|---|
| 1 | `ollama list` (HTTP API) → `qwen3-30b-a3b-instruct-2507-bartowski` 신규 model 적중 + size verify | `/tmp/phase3-5-h-om-list-post.txt` |
| 2 | `ollama show` metadata verify — qwen3moe arch / block_count 48 / 30.5B / 128 experts top-8 ((h)/(h-O) 답습 일치) | `/tmp/phase3-5-h-om-show.txt` |
| 3 | **Ollama Modelfile blob digest verify** — `ollama show --modelfile` 출력에서 FROM blob path 추출 + (h) bartowski sha256 `382b4f5a164d...33a95` cross-check 의무 (Ollama 자체 blob digest 표시 자격) | `/tmp/phase3-5-h-om-modelfile.txt` |
| 4 | `ollama show --parameters` + `--template` 추출 + (h-O) library 답습 정합성 확인 | `/tmp/phase3-5-h-om-params-template.txt` |
| 5 | **R-1 anchor 22회 추가** (mid-cycle, R-3 답습) | `/tmp/phase3-5-h-om-r1-anchor-22x.txt` |
| 6 | 디스크 사용량 post-create + Ollama blob storage 변화 확인 (hard link 답습 시 추가 0건 자격) | `/tmp/phase3-5-h-om-disk-post-create.txt` |

→ Step 1·2·3·4 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 발동

---

## 4. 측정 절차 (Ollama /api/generate API, (h-O) cold 측정 답습)

### 4.1 사전 조건

| Step | 명세 |
|---|---|
| 1 | 다른 model unload (`keep_alive: 0`) + GPU 메모리 0 verify. **R-1 anchor 23회 추가** (mid-cycle, 측정 *전*) |
| 2 | R-23 사전 (LLM 프로세스 격리) |
| 3 | GPU 상태 verify (idle + thermal baseline) |
| 4 | Ollama daemon health (`/api/version`) |

### 4.2 측정 명령 ((h-O) 답습 cold 측정 우선)

```bash
# decode-161tok prompt (cold)
PROMPT_DECODE=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-decode-161tok.txt")
curl -s -X POST http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_DECODE" '{
        model: "qwen3-30b-a3b-instruct-2507-bartowski",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    -o /tmp/phase3-5-h-om-measure-decode-161tok-cold.json

# prefill-2k prompt (cold)
PROMPT_PREFILL=$(cat "/home/delangi/문서/project/category/AI_development_tool/docs/phase0/v1-poc-raw/phase3/phase1-prompt-prefill-2k.txt")
curl -s -X POST http://127.0.0.1:11434/api/generate \
    -d "$(jq -n --arg p "$PROMPT_PREFILL" '{
        model: "qwen3-30b-a3b-instruct-2507-bartowski",
        prompt: $p,
        stream: false,
        keep_alive: 0,
        options: {num_predict: 256, seed: 42, num_ctx: 8192}
    }')" \
    -o /tmp/phase3-5-h-om-measure-prefill-2k-cold.json
```

### 4.3 측정 항목 ((h-O) §4.3 답습 + 3-way 비교 추가)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| Ollama decode tok/s | `eval_count / (eval_duration / 1e9)` + 양 분모 답습 ((h-O) R-S2 답습 영구) | 분모 정직성 영구 명문 |
| Ollama prefill tok/s | `prompt_eval_count / (prompt_eval_duration / 1e9)` + 양 분모 답습 | 동상 |
| total wall-clock | `total_duration / 1e9` | 빌드·로딩·측정 합산 |
| **3-way 비교 (h vs h-O vs h-OM, 핵심)** | (h) llama.cpp decode 49.6 / prefill 45.4 / (h-O) Ollama library decode 15.29 / prefill 12.43 / (h-OM) Ollama bartowski decode X / prefill Y | source conversion lineage 통제 evidence |
| **Δ(h, h-OM) = inference engine *진짜* 단독 분리** | (h) decode 49.6 / (h-OM) decode X | source 100% 동일, llama.cpp ↔ Ollama framework 단독 차이 |
| **Δ(h-O, h-OM) = Ollama internal optimization 변수** | (h-O) decode 15.29 / (h-OM) decode X | 동일 engine + 다른 source (library vs bartowski) |
| prompt_eval_count vs llama.cpp 153 tokens | (h-O) 답습 = 161 답습 자격 (Ollama tokenizer 동일) | tokenizer 변수 정직성 |
| GPU memory peak + thermal polling | `nvidia-smi` polling + R-rec-3 답습 (85°C 5분) | 5분 이상 thermal 정직성 |

**측정 종료 후 R-1 anchor 24회 추가 (R-3 답습)** — 측정 직후 `sudo sha256sum /proc/3375/exe`. hash 일관 ✓ 확인 → raw report 진입 자격.

---

## 5. 분기 조건 ((h-O) §5 답습 + Modelfile 특화 신규)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | hard link + Modelfile + `ollama create` 성공 + 측정 완료 (tok/s 실수치 획득 cold 우선) | raw report → **(h) vs (h-O) vs (h-OM) 3-way 비교 framing (§9)** → source conversion 통제 evidence + MVP-1 R4 framing 정정 결정적 input |
| **B1 (Modelfile syntax 에러)** | TEMPLATE 또는 PARAMETER 문법 error | raw report → Modelfile 정정 + 사용자 명시 별도 |
| **B2 (`ollama create` 실패)** | container 내 FROM path 미발견 또는 GGUF parse 에러 | raw report → hard link 재verify 또는 OM-alt (copy) 자격 평가 |
| **B3 (Modelfile create 후 model load 실패)** | `/api/generate` 호출 시 model load 에러 (GGUF format 호환 부재 등) | raw report → (h-O) library version 답습 (Ollama embedded llama.cpp 호환 verify) |
| **B4 (디스크 부족)** | hard link 시 ENOSPC (hard link = 디스크 추가 0건 자격, 사실 발생 0 가설) | 즉시 중단 → (g)/(h)/(h-O) cleanup 사용자 명시 |
| **B5 (Ollama runtime 에러)** | OOM, CUDA error, segfault | raw report → quant 변경 또는 별도 cycle |
| **B6 (tokenizer 분모 mismatch)** | `prompt_eval_count` ≠ (h)/(h-O) 답습 161 | raw report → tokenizer 변수 단독 분리 cycle carry-over |
| **B7 (measurement HTTP error)** | curl POST timeout, JSON parse error | raw report → 재시도 또는 사용자 명시 별도 |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 18 항목, (h-O) §6 답습 + (h-OM) source 통제 특화)

1. **source conversion lineage 100% 통제 자격 강함** — (h) bartowski GGUF (sha256 `382b4f5a164d...33a95`) 답습 hard link, (h)/(h-OM) 동일 inode = source 변수 *완전* 통제
2. **inference engine 변수 *진짜* 단독 분리 자격 강함** ((h) llama.cpp ↔ (h-OM) Ollama 비교, source + quant + prompt + hardware 모두 동일)
3. **단 4 미통제 변수 잔존**:
   - 측정 도구 framework (llama-cli vs Ollama /api/generate)
   - Ollama embedded llama.cpp version (Ollama 0.20.4 의 내부 llama.cpp commit ≠ (h) HEAD `c0c7e147` 가능성, R-S4 답습)
   - Ollama internal caching/optimization (Ollama 자체 KV cache + scheduling)
   - tokenizer 차이 가능성 ((h-O) 답습 = Ollama 161 vs llama.cpp 153 = 8 tokens 5.2% 격차 evidence 답습)
4. **Ollama Modelfile create 시 internal optimization 변경 가능성** — Ollama 가 hard link blob 을 자체 storage 형식으로 변환 가능성 (verify 의무, blob digest cross-check)
5. **R-23 위반 가능성** — Modelfile + create + 측정 ~5~30분 wall-clock 중 다른 활동 발생 가능
6. **egress 0건 답습** — 본 cycle = (h) GGUF 답습 hard link, Ollama pull 0건 의무
7. **디스크 추가 0건 답습** — hard link 동일 inode, 단 Ollama blob storage 자체 변환 시 추가 가능성 verify 의무
8. **단일 측정 cycle** — 재현성 평가 자격 0 (Phase 3 R-17 답습)
9. **GPU thermal throttling 가능성** — R-rec-3 polling 명문
10. **Ollama daemon pid 3375 hash baseline 보존** — silent 교체 0건 답습 영구
11. **분모 정직성 영구 명문 ((h-O) R-S2 답습)** — 양 분모 raw report 의무
12. **cold 측정 우선 ((h-O) R-S3 답습)** — warm 측정 = 별도 단계 cache hit 효과 분리 framing
13. **F2 가설 평가**:
    - (h-OM) ≈ (h-O) → Ollama internal optimization 변수 무관, source conversion 차이 미미 → inference engine framework 자체 격차 (~3.24×) 강한 evidence
    - (h-OM) > (h-O) → bartowski conversion 이 Ollama library 보다 유리, source conversion lineage 변수 단독 분리 input
    - (h-OM) < (h-O) → Ollama internal optimization 우세 또는 bartowski conversion 불리, 별도 verify cycle
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구) — 본 cycle = input only**
14. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 의무 답습 영구
15. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
16. **본 brief 가 후속 cycle 자동 진입 trigger 0** — 모든 단계 사용자 명시 의무
17. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만, 코드/측정 변경 0
18. **Ollama Modelfile vs library 의 internal 처리 차이** — Ollama 가 Modelfile 등록 model 을 library model 과 *동일 internal pipeline* 사용 자격 단언 0, 별도 verify cycle 자격

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 16 항목과 §7 차단 조건은 **1:1 매핑 의무** ((h-O) R-15 답습).

1. ❌ 본 brief 자체 Modelfile/create/측정/sudo 실행
2. ❌ Ollama daemon 변경 (pid 3375 hash baseline 보존)
3. ❌ (h) GGUF 파일 변경 또는 cleanup (hard link source 보존 의무)
4. ❌ (g) GGUF 파일 변경 (R-13 보존)
5. ❌ (h-O) Ollama library blob 변경 (R-13 보존)
6. ❌ llama.cpp HEAD `c0c7e147` 변경
7. ❌ MVP-1 합의 본문 자동 정정 (R-9 답습 영구)
8. ❌ 헌법·ADR 본문 자동 정정
9. ❌ M3·M4 결정 *고정* ((k) 별도 cycle)
10. ❌ runtime backend 코드 작성 (트랙 B 별도)
11. ❌ 메모리 자동 갱신
12. ❌ (j)/(k)/(l)/(m)/(n) 자동 진입
13. ❌ brief commit 자동 진입
14. ❌ (g)+(h)+(h-O)+(h-OM) 통합 본문 정정 (기존 brief/합의 본문 변경 0건) + 4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원 carry-over)
15. ❌ (g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime 자동 진입 명백 부정 (chain 영구 종결 의무 답습 영구)
16. ❌ 새 bartowski GGUF 다운로드 (host (h) GGUF 답습 only, egress 0 의무)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (h-OM) ≈ (h-O) | source conversion 차이 무관 → inference engine framework 자체 격차 strong evidence → MVP-1 R4 framing 정정 강한 input HIGH (별도 cycle 의무) |
| G + (h-OM) > (h-O) | bartowski conversion 우세 → source conversion 변수 단독 분리 cycle 자격 평가 + library version 답습 verify |
| G + (h-OM) < (h-O) | Ollama internal optimization 우세 → library version 답습 vs Modelfile create 처리 차이 verify cycle |
| B1~B7 | 다른 절차 또는 (h-O) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (변경 0건 답습)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **MVP-1 합의 R4 framing 정정 evidence 별도 cycle** | **HIGH** | (g)/(h)/(h-O)/(h-OM) 4-way 종합 input 결정적 (R-9 답습 영구) |
| **(g)+(h)+(h-O)+(h-OM) 4-way 통합 *분석* cycle** | **HIGH ⭐⭐ (격상 자격)** | source conversion + inference engine 양차원 통제 종합 분석 (사용자 비전 답습) |
| **Ollama prefill 처리 framework overhead 검증 cycle** | MEDIUM | (h-O) F-2 23.89× outlier 답습 |
| **(j) advisory wall-clock 측정 cycle** | MEDIUM | 자비스 비전 직접 진전 |
| **Phase 1 N=3 repetitions Ollama 답습 cycle** | MEDIUM | C-S2 답습 |
| **Ollama embedded llama.cpp version verify cycle** | MEDIUM | R-S4 답습 |
| **Ollama Modelfile vs library internal pipeline cross-check cycle** | MEDIUM | 본 cycle §6 #18 답습 (Modelfile vs library 처리 차이) |
| **llama.cpp graceful tensor name resolution 검증** | MEDIUM | (g) F-2 + (h) R-S3 답습 |
| **`llama-bench` carry-over (R-rec-12 격상)** | MEDIUM | (g) F-8 + (h) F-7 답습 |
| **(k) M3·M4 결정 *고정* cycle** | DEFER | 변수 분리 input 강화 후 평가 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 의무 답습 영구 |
| **다른 quant 비교 (Q5_K_M / IQ4_XS)** | LOW | R-rec-2 답습 |
| **외부 benchmark cross-reference cycle** | LOW | C-N-5 답습 |
| **tokenizer 변수 단독 분리 cycle (B6 발생 시)** | LOW | R-rec-9 답습 |
| **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정 cycle** | DEFER | 사용자 명시 별도 cycle, 기존 본문 변경 0건 |
| **(m) §12 Ollama 위생 정정** | LOW | 본 cycle 무관 |
| **(n) Phase 3 brief v1.2 보강** | LOW | 본 cycle 결과 흡수 자격 별도 |
| **(g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((h-O) 동형 풀 7단계 답습, 사용자 명시 의무)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| **(1) brief v1 작성 + commit (본 단계)** | 본 brief v1 entry plan only, 합의 *전* | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | Agent A/B/C 병렬 독립 + Reviewer 통합 | 사용자 명시 후 |
| (3) brief v1.1 보강 + commit | 합의 BLOCKING verbatim 100% + R-S* 흡수 | 사용자 명시 후 |
| (4) Modelfile 작성 + ollama create (~5분 wall-clock) | hard link + Modelfile + `ollama create` (R-7 답습, egress 0) | 사용자 명시 후 |
| (5) verify + 측정 실행 (~10~30분 wall-clock) | §3.3 + §4 절차 답습 (cold 측정 우선) | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (h-O) 패턴 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (h) vs (h-O) vs (h-OM) 3-way 비교 framing (본 cycle 핵심 가치)

### 9.1 (h) + (h-O) baseline 답습

| 항목 | (h) llama.cpp direct | (h-O) Ollama library | 비고 |
|---|---|---|---|
| source | bartowski GGUF sha256 `382b4f5a164d...33a95` | Ollama library blob `78b329e716e7...ba9cc` | 다른 source (R-S1 발효) |
| inference engine | llama-cli `c0c7e147` direct | Ollama 0.20.4 (Docker container) | 다른 engine |
| decode-161tok prompt / generation | 389.4 / 49.6 | 118.43 / 15.29 | (h-O) ~3.29× / ~3.24× 느림 |
| prefill-2k prompt / generation | 1916.8 / 45.4 | 80.25 / 12.43 | (h-O) ~23.89× / ~3.65× 느림 |

### 9.2 (h-OM) 예상 결과 시나리오 (사전 가설 평가, 단정 0)

| 시나리오 | (h-OM) decode cold tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: (h-OM) ≈ (h-O) (~13~17 t/s)** | source conversion 차이 무관 — Ollama framework 자체 격차 본질 | inference engine 변수 단독 분리 evidence 강한 자격 | MVP-1 R4 framing 정정 강한 input HIGH |
| **S2: (h-OM) > (h-O) (~17~25 t/s)** | bartowski conversion 우세 — Ollama library version 답습 부분 약화 | source conversion 변수 평가 cycle | library vs bartowski cycle |
| **S3: (h-OM) < (h-O) (~8~13 t/s)** | Ollama library internal optimization 우세 — Modelfile create 처리 차이 | Modelfile vs library internal pipeline 차이 verify cycle | 별도 verify |
| **S4: (h-OM) ≈ (h) (~45~50 t/s)** | inference engine 동일 자격 — Ollama framework overhead 미미 (가능성 매우 낮음) | F2 가설 *역방향 강화* | F2 재고 cycle |
| **S5: Modelfile create 실패 (B1~B3)** | TEMPLATE / FROM path / GGUF format 호환 미흡 | 대안 cycle 자격 평가 | OM-alt (copy) 또는 library 답습 |
| **S6: tokenizer 분모 mismatch (B6)** | Ollama tokenizer ≠ Modelfile 등록 후 변경 | tokenizer 변수 분리 cycle | R-rec-9 답습 |

### 9.3 핵심 정직성 (3-way 통제 framing)

- ✅ **본 cycle = source conversion 100% 통제 + inference engine *진짜* 단독 분리 시도**
- ❌ 단 4 미통제 변수 잔존 (측정 도구 framework + embedded llama.cpp version + internal caching + tokenizer)
- → **(h, h-OM) 1:1 비교 = inference engine framework 자체 격차 evidence 강함** (source 동일 sha256 답습 영구)
- → **(h-O, h-OM) 1:1 비교 = Ollama internal optimization 변수 (source 다름)** + Δ = library vs bartowski conversion 차이 자격
- → **4-way (g)/(h)/(h-O)/(h-OM) 통합 분석 cycle 자격 HIGH** carry-over 발효

---

## 10. 본 brief v1 본 cycle 진입 자체 영구 권위

- 본 brief v1 = (h-O) cycle 완료 (`9685ae3`) + 사용자 명시 (h-OM) 진입 형태 + Modelfile TEMPLATE (h-O) 답습 + Phase 3.5-OM 명명 직후 entry plan
- 본 brief 자체 머신 변경 0건 (Modelfile/create/측정/sudo 0건)
- 본 brief = 합의 *전* entry plan, BLOCKING verbatim 흡수 0건 (합의 후 v1.1 보강 의무 답습 영구)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)
- (h-OM) cycle = R-S1 발효 직접 후속 + 본 프로젝트 최초 source conversion 100% 통제 cycle

---

**본 brief v1 작성 완료** (Phase 3.5-OM (h-OM) Ollama Modelfile bartowski 등록 cycle entry plan, (h-O) 동형 7단계 답습 + source conversion 100% 통제 핵심 가치 명문 + hard link 절차 + Modelfile TEMPLATE (h-O) library 답습 + 3-way 비교 framing 6 시나리오 + 정직성 한계 18 항목. 본 cycle 머신 변경 0건. 다음 단계 = 풀 3+1 합의 진행 사용자 명시 의무.)
