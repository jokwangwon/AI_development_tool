# Jarvis MVP-1 V-1 PoC Phase 3.5-OM (h-OM) entry brief (v1.1, Ollama Modelfile bartowski GGUF 등록 cycle, 풀 3+1 합의 APPROVE w/ COND 반영)

> **본 brief v1.1 = (h-OM) brief v1 (`3d02edb`, 469줄) 의 풀 3+1 합의 (`bcc4974`, 440줄, APPROVE w/ COND + BLOCKING 15 + R-S1~R-S5 + 권고 16 + NOTE 18 + 기각 5) verbatim 본문 직접 반영.** v1.1 진입 자격 = (1) BLOCKING 15 verbatim 100% 반영 (R-21 답습 영구 의무) / (2) R-S1~R-S5 정정 흡수 21+ 곳 / (3) 강한 권고 흡수 (R-rec-1·2·3·4·10·13·15) / (4) §11 v→v1.1 변경 일람 신규 작성 / (5) 본문 변경 0 머신 변경 (Modelfile/create/측정/sudo 0). 본 brief = entry plan only. 자동 다음 단계 진입 0건 ([[feedback_staged_consensus_workflow]] + chain 영구 종결 의무 답습 영구).

**작성일**: 2026-05-25 (Phase 3.5-OM (h-OM) 풀 3+1 합의 commit `bcc4974` 직후, 본 cycle 단계 (3) brief v1.1 보강)
**카테고리**: V-1 PoC Phase 3.5-OM (h-OM) entry brief v1.1 (Phase 3 carry-over (h-O) R-S1 발효 직접 후속, 본 cycle 핵심 = **source 통제 *최대화* + inference engine *부분* 단독 분리 시도** — R-S3 발효 약화 framing)
**범위**: (1) (h) bartowski GGUF → Ollama Modelfile 등록 절차 (host hard link **또는 Ollama 자체 blob copy +17.3 GiB 추가 가능성** R-S1 발효) / (2) Ollama /api/generate 측정 ((h-O) cold 답습) / (3) 분기 (G·B1~B8) / (4) (h) ↔ (h-O) ↔ (h-OM) 3-way 비교 framing / (5) 후속 carry-over ((h-OL) MEDIUM 신규)

**답습 권위**:
- **(h-OM) 풀 3+1 합의** (`docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-v1-poc-phase3-5-h-om-ollama-modelfile-bartowski-entry.md`, commit `bcc4974`, 440줄, BLOCKING 15 + R-S1~R-S5 + 권고 16 + NOTE 18 + 기각 5) — **본 brief v1.1 의 직접 input 자격 영구**
- (h-O) Phase 3.5-O cycle 정리 commit (`9685ae3`, 16번째 entry, S1 confirmed Ollama < llama.cpp ~3.24~23.89× + R-S1 발효)
- (h-O) brief v1.1 (`e77e8d7`, 476줄) + 풀 3+1 합의 (`37bcd40`, 459줄)
- (h) Phase 3.5-B cycle 정리 commit (`fccec6a`, 15번째 entry, bartowski sha256 `382b4f5a164d...33a95`)
- (g) Phase 3.5 cycle 정리 commit (`b3d4164`, 14번째 entry)
- **외부 raw evidence (R-S1 발효)**: Ollama issue #1450 (closed-as-not-planned) + docs.ollama.com/import "**ollama create performs a regular copy**" 답습 영구
- MVP-1 합의 R4 (input only, R-9 답습 영구) + ADR-011 §2.1 5조건 + 헌법 5조-2
- 메모리: `feedback_provider_liquidity` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_jarvis_local_boss_direction` / `project_minimize_user_intervention` / `feedback_actual_run_trigger_paths_filter` / `project_mvp_staged_roadmap`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (1:1 매핑 self-consistency 영구)

### 하는 것

1. (h) bartowski GGUF (sha256 `382b4f5a164d...33a95`, 17.353 GiB) Ollama Modelfile 등록 절차 명문 — host hard link + Modelfile 작성 + `ollama create` (**R-S1 발효 정직성**: hard link 후 `ollama create` = Ollama 자체 blob copy 표준 동작 가능성 강함, 디스크 +17.3 GiB 추가 risk)
2. Modelfile TEMPLATE + 6 PARAMETER = (h-O) library 답습 (ChatML + temp 0.7 + top_k 20 + top_p 0.8 + repeat_penalty 1 + 2 stop). **LICENSE block 의도적 부분 답습 0건** (R-S5 발효)
3. 측정 절차 명문 — (h-O) cold 측정 답습 + Phase 1 답습 protocol
4. 분기 조건 명문 — G 성공·B1 Modelfile syntax·B2 `ollama create` sub-trigger 3 분리·B3 model load·B4 디스크 부족 또는 **Ollama blob copy +17.3 GiB 추가** (R-S1 발효 강화)·B5 Ollama runtime·B6 tokenizer 분모 mismatch·B7 HTTP error·B8 hard link permission / Ollama daemon access 거부 (신규)
5. 정직성 한계 명문 20 항목 (§6) — source 통제 *최대화* (R-S3 발효 약화) + 5 미통제 변수 (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이 + **Ollama Modelfile FROM 처리 모드 unknown R-S1 발효 추가**)
6. 차단 조건 명문 (§7) — §0 항목 1:1 매핑 (R-15 답습)
7. 후속 carry-over 매트릭스 (§8) — chain 영구 종결 의무 답습 영구 + **(h-OL) llama.cpp Ollama blob 직접 측정 cycle 신규 MEDIUM carry-over** (R-15 발효)
8. (h) ↔ (h-O) ↔ (h-OM) 3-way 비교 framing (§9) — 시나리오 6 + prefill 분리 자격 평가

### 하지 않는 것 (영구 답습)

1. ❌ **본 brief 자체로 Modelfile / ollama create / 측정 / sudo 실행**
2. ❌ **Ollama daemon 상태 변경 (pid 3375)** — keep_alive 0 unload 만, R-1 anchor hash baseline `ce95c475...878b10` 일관 보존 ((h-O) 누계 19회 + 본 cycle 4회 = **23회 누계 종료**, R-S2 발효)
3. ❌ **(h) GGUF 파일 변경 또는 cleanup** — hard link source 보존 의무 (R-13 답습 영구)
4. ❌ **(g) GGUF 파일 변경** — R-13 답습 영구
5. ❌ **(h-O) Ollama library blob 변경** — R-13 답습 영구
6. ❌ **llama.cpp HEAD `c0c7e147` 변경**
7. ❌ **MVP-1 합의 본문 자동 정정** — R-9 답습 영구
8. ❌ **헌법 5조-2 / ADR-011 본문 자동 정정** — R-9 답습 영구
9. ❌ **M3·M4 결정 *고정*** — (k) 별도 cycle
10. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss 코드 작성** — 트랙 B 별도
11. ❌ **메모리 자동 갱신** — 사용자 명시 의무
12. ❌ **(h-OL)/(j)/(k)/(l)/(m)/(n) 자동 진입**
13. ❌ **본 brief 자동 commit 진입**
14. ❌ **Ollama create 시점 = 사용자 명시 *직접* 의무** (R-S1 발효 디스크 +17.3 GiB 추가 risk 답습)
15. ❌ **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정** — 본 cycle = 별도 cycle 단독 진행 + 4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원 carry-over)
16. ❌ **(g1-N-3-adr-008+sip+adr-012'') prime-prime + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime 자동 진입** — chain 영구 종결 의무 답습 영구

---

## 1. 본 cycle 진입 근거

### 1.1 직접 trigger (R-S3 발효 framing 약화)

- **(h-O) cycle 완료** (`9685ae3`, SESSION 16번째 entry):
  - F-1 ⭐⭐⭐: S1 confirmed — Ollama < llama.cpp ~3.24~23.89× (decode 49.6→15.29 / prefill 45.4→12.43 / prefill prompt 1916.8→80.25)
  - F-3 ⭐⭐⭐: R-S1 완전 raw evidence (Ollama blob `78b329e716e7...ba9cc` ≠ (h) bartowski `382b4f5a164d...33a95`)
  - (h-O) 합의 R-S1 발효 → (h-OM) HIGH carry-over
- **본 cycle 핵심 가치 = source 통제 *최대화* + inference engine *부분* 단독 분리 시도** (R-S3 발효 약화 framing):
  - (h) Q4_K_M (bartowski sha256 `382b4f5a164d...33a95`) + llama.cpp `c0c7e147` direct = decode **49.6** / prefill **45.4** t/s
  - (h-O) Q4_K_M (Ollama library blob `78b329e716e7...ba9cc`, **다른 source**) + Ollama 0.20.4 = decode **15.29** / prefill **12.43** t/s
  - (h-OM) **(h) bartowski GGUF 답습 (sha256 `382b4f5a164d...33a95`)** + Ollama 0.20.4 = decode X / prefill Y t/s
  - → 3-way 비교: Δ(h, h-OM) source 통제 *최대화* / Δ(h-O, h-OM) Ollama internal optimization 변수
- **R-S1 발효 외부 raw evidence 답습 영구**:
  - Ollama issue #1450 ("Use hard link to import GGUF") = **closed as not planned**
  - docs.ollama.com/import = "**ollama create performs a regular copy** of the .gguf file ... first step of a GGUF import is copying the binary to the model directory with a hashed name"
  - → **`ollama create` 시 자체 blob copy 표준 동작 강한 가능성** + content-addressable sha256 답습 시 (h) sha256 일치 자격 강함 (단 디스크 두 곳 발생)
- **본 cycle 비용 (R-S1 발효 정정)**: egress **0건** (host (h) GGUF 답습 hard link) + 디스크 **0건 또는 ~17.3 GiB 추가** (Ollama 자체 blob copy 동작 시, 사전 평가 0)

### 1.2 본 cycle 핵심 질문

| Q# | 질문 | 답 형식 |
|---|---|---|
| **Q1** | hard link + Modelfile + `ollama create` 성공 가능? Ollama 자체 blob copy 발생 가능성? | Y/N + `ollama list` 직접 verify + `ollama show --modelfile` blob path + inode 비교 (host (h) GGUF inode 와 동일 시 hard link 실효 / 다름 시 standard copy) |
| **Q2** | (h-OM) decode/prefill tok/s = ? | (h-O) 답습 cold 측정 protocol |
| **Q3** | Δ(h, h-OM) = inference engine *부분* 단독 분리 (R-S3 발효 약화) | (h) 49.6 vs (h-OM) X 격차 + 5 미통제 변수 정직성 명문 |
| **Q4** | Δ(h-O, h-OM) = Ollama internal optimization 변수 | (h-O) 15.29 vs (h-OM) X 격차 |
| **Q5** | Provider Liquidity finding 결정적 평가 자격? | (g)/(h)/(h-O)/(h-OM) 4-way 종합 input HIGH (단 본문 정정 별도 cycle R-9 답습 영구) |
| **Q6** | Ollama blob digest = (h) bartowski sha256 일치? | post-create `ollama show --modelfile` + `sudo docker exec stat -c '%i %s' <blob>` cross-check (content-addressable 답습 시 일치 자격 강함) |

### 1.3 본 cycle 범위 한정 (R-rec-7 답습 + R-S5 발효)

- ✅ 단일 source = (h) bartowski GGUF (`/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf`)
- ✅ host hard link 방식 (단 Ollama 자체 blob copy 시 +17.3 GiB 추가 risk 명문, R-S1 발효)
- ✅ **Modelfile TEMPLATE + 6 PARAMETER = (h-O) library 답습 (의도적 부분 답습, LICENSE block 의도적 0건 = Ollama Modelfile create 시 optional)** (R-S5 발효)
- ✅ 단일 measurement cycle — decode + prefill-2k cold 우선
- ✅ 명명 = "Phase 3.5-OM" (R-rec-7 답습)
- ❌ (h)/(h-O)/(g) cycle 답습 = 변경 0건
- ❌ advisory wall-clock 측정 = (j) 별도 cycle
- ❌ M3·M4 결정 = (k) 별도 cycle
- ❌ **Modelfile 다른 TEMPLATE/PARAMETER 변경 cycle = 본 cycle 외**
- ❌ **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정 cycle = 본 cycle 외** + 4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원)
- ❌ **(h-OL) llama.cpp Ollama blob 직접 측정 cycle = 본 cycle 외 (R-15 발효 신규 MEDIUM carry-over)**

---

## 2. 모델 source — (h) bartowski GGUF 직접 답습 (R-S5 발효 ownership 명문)

### 2.1 본 cycle 확정 source

> **본 cycle source = (h) bartowski GGUF 답습 (host hard link)**. (h) cycle raw verify 답습 — sha256 `382b4f5a164d200f93790ee0e339fae12852896d23485cfb203ce868fea33a95` (full 64자 답습 영구), 17.353 GiB, **owner `delangi:delangi`, mode 0664** (R-S5 발효 명문). bartowski conversion lineage *최대화* 통제 자격 강함 (단 Ollama `ollama create` 표준 동작 blob copy 시 디스크 두 곳 발생).

| # | source | path / 식별자 | 비고 |
|---|---|---|---|
| **OM** | **(h) bartowski GGUF hard link** | host: `/home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf` (`delangi:delangi 0664`, sha256 `382b4f5a164d...33a95`, 17.353 GiB) → container: `/root/.ollama/imports/<file>` (via `/home/delangi/문서/.../bootcamp_game/ollama-data/imports/`) | **✅ 본 cycle 확정 (사용자 명시 + R-S1 답습)**. **R-S1 발효 정직성**: hard link 후 `ollama create` 시 Ollama 자체 blob copy 가능성 강함 (Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습) → 디스크 +17.3 GiB 추가 risk |
| OM-alt | (h) bartowski GGUF copy | 동상, cp (디스크 추가 17.353 GiB 명시) | NOTE: hard link 차단 시 fallback (사용자 명시 별도). **R-S1 발효 = OM 과 결과 동등 가능성 (Ollama blob copy 표준 동작)** |
| OM-symlink | (h) bartowski GGUF symlink | symlink (container 내 host root path access 0건 가능성) | NOTE: 사전 verify 의무 (별도 cycle) |
| **OM-direct-blob (R-rec-14 발효 신규)** | 직접 blobs/sha256-<bartowski hash> hard link + manifest manual 작성 | Ollama manifest 작성 우회 | NOTE: Ollama 권장 path 외, daemon verify 실패 risk (별도 cycle) |

### 2.2 source 사전 verify 의무

1. **(h) bartowski GGUF 존재 verify**: `ls -la <host_path>` → 17.353 GiB / 18,632,183,808 bytes / `delangi:delangi 0664` / inode (raw direct verify) 일치
2. **Filesystem hard link 가능 verify**: `df -T <host_path>` + `df -T ollama-data/` → 동일 filesystem (`/dev/nvme0n1p2 ext4`) 확인 (Agent A raw verify ✓)
3. **Container mount 답습 verify**: `sudo docker inspect oracle-game-ollama` → mount source/destination 답습
4. **`imports/` directory 생성 + 권한 명문 의무**: `sudo mkdir -p /home/delangi/문서/.../bootcamp_game/ollama-data/imports && sudo chmod 755 imports/` → ownership `root:root 0755`
5. **R-1 anchor 20회 추가** ((h-O) 누계 19회 + 본 cycle 1회 = **20회 누계**, R-S2 발효, R-3 답습)

---

## 3. Modelfile + ollama create 절차 (R-S1 발효 정직성 + R-S5 발효 권한 verify)

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-rec-5 답습)

본 cycle egress = **0건 의무** (host (h) GGUF 답습 hard link, Ollama pull 0건). **apt install / pip install / git clone / HF egress / Ollama pull 0건 의무**. 본 cycle sudo 사용 = **최소 8~10회 호출 예상** (R-rec-9 발효): egress baseline pre + R-1 anchor 20·21·22·23x (4회) + cache directory verify + Modelfile cp + hard link + container exec + egress baseline mid + post (R-6 발효 R-rec-6 답습 password 누출 grep verify 포함).

### 3.0.1 (g)/(h)/(h-O) preservation 답습 (R-13 답습 영구)

(g) + (h) + (h-O) Ollama library blob 모두 보존 답습 영구. 본 cycle hard link source = (h) GGUF inode 보존 의무.

### 3.1 사전 조건 (egress 격리 + R-1 anchor 20회 + R-rec-1 신규 step, R-S4 발효)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | egress baseline pre (`sudo ss -tan state established`) | `/tmp/phase3-5-h-om-egress-baseline-pre.txt` |
| 2 | apt snapshot pre | `/tmp/phase3-5-h-om-apt-snapshot-pre.txt` |
| 3 | 디스크 사용량 pre + **추가 capacity verify (~17.3 GiB R-S1 발효 추가 자격)** — `df -h /home/delangi` + ollama-data filesystem 답습 | `/tmp/phase3-5-h-om-disk-pre.txt` |
| 4 | (h) GGUF + Ollama mount path verify (§2.2 답습) + (h) GGUF inode + ownership + sha256 답습 명문 | `/tmp/phase3-5-h-om-paths-verify.txt` |
| 5 | **R-1 anchor 20회 추가** ((h-O) cumulative_total 19 + 본 cycle 1 = 20회, hash baseline `ce95c475...878b10` 일관, R-S2 발효) | `/tmp/phase3-5-h-om-r1-anchor-20x.txt` |
| 6 | Ollama daemon status + 기 다운로드 list verify | `/tmp/phase3-5-h-om-ollama-status.txt` |
| **7 [R-S4 / R-rec-1 발효 신규]** | **Ollama embedded llama.cpp version verify** — `curl -s http://127.0.0.1:11434/api/version` + `sudo docker exec oracle-game-ollama ollama --version` 답습 (사용 가능 시) 명문 ((h-O) brief v1.1 §3.1 Step 7 답습). 미노출 시 §6 #4 정직성 한계 강화 의무 | `/tmp/phase3-5-h-om-embedded-llamacpp.txt` |
| 8 | GPU + memory + thermal verify (idle baseline) | `/tmp/phase3-5-h-om-gpu-pre.txt` |
| **9 [R-rec-5 발효 신규]** | **`ollama list \| grep -i bartowski` model 명칭 conflict pre-verify** (R-13 발효) — `qwen3-30b-a3b-instruct-2507-bartowski` 기존 사용 0건 확인 | `/tmp/phase3-5-h-om-name-conflict-pre.txt` |

### 3.2 Modelfile 작성 + hard link 절차 (R-S5 발효 권한 verify 추가)

**Step 1: Container mount path 내 imports directory 생성**:
```bash
sudo mkdir -p /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports
sudo chmod 755 /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports
sudo ls -la /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports
```

**Step 2: (h) bartowski GGUF hard link 생성 + 권한 verify (R-S5 발효 신규)**:
```bash
sudo ln /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
    /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf

# inode + 권한 verify 의무
ls -li /home/delangi/models/phase3-5/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
sudo ls -li /home/delangi/문서/project/category/bootcamp_game/ollama-data/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
# → 동일 inode 답습 + 동일 size 답습 + 동일 ownership `delangi:delangi 0664` (link 자체)

# Container 내 read 가능성 직접 verify (R-S5 발효 신규)
sudo docker exec oracle-game-ollama stat /root/.ollama/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf
sudo docker exec oracle-game-ollama head -c 16 /root/.ollama/imports/Qwen_Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf | xxd | head -1
```

**Step 3: Modelfile 작성** ((h-O) library 답습, LICENSE 의도적 부분 답습 0건, R-S5 발효 명문):
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

**Step 4: `ollama create` via docker exec + tag 자동 부여 명문 (R-S5 발효)**:
```bash
sudo docker exec oracle-game-ollama ollama create qwen3-30b-a3b-instruct-2507-bartowski -f /root/.ollama/imports/Modelfile 2>&1 | tee /tmp/phase3-5-h-om-create.log
```
**R-S5 발효 명문**: Ollama 가 model name 으로 `:latest` 자동 부여 가능성, §3.3 Step 1 verify 의무.

### 3.3 Create 후 verify (R-S4/R-S5 발효 명문 + R-rec-4 강화)

| Step | 명세 | 출력 |
|---|---|---|
| 1 | `ollama list` (HTTP API) → `qwen3-30b-a3b-instruct-2507-bartowski` 신규 model 적중 + size verify + **tag 자동 부여 (`:latest`) 정확 식별자 확인 (R-S5 발효)** + §4.2 model name 일치성 verify 의무 | `/tmp/phase3-5-h-om-list-post.txt` |
| 2 | `ollama show` metadata verify — qwen3moe arch / block_count 48 / 30.5B / 128 experts top-8 ((h)/(h-O) 답습 일치) | `/tmp/phase3-5-h-om-show.txt` |
| 3 | **Ollama Modelfile blob digest verify + inode 비교 (R-S4 + R-rec-4 발효 강화)** — `ollama show --modelfile` 출력에서 FROM blob path 추출 + `sudo docker exec oracle-game-ollama stat -c '%i %s' <blob_path>` 답습 inode 비교 (host (h) GGUF inode 와 동일 시 hard link 실효 ✓ / 다름 시 standard copy 답습 + 디스크 추가 정직성 명문) + (h) bartowski sha256 `382b4f5a164d...33a95` cross-check (content-addressable 답습 시 일치 자격 강함) | `/tmp/phase3-5-h-om-modelfile-blob.txt` |
| 4 | `ollama show --modelfile` + `--parameters` + `--template` 추출 + (h-O) library 답습 정합성 확인 | `/tmp/phase3-5-h-om-show-detailed.txt` |
| 5 | **R-1 anchor 21회 추가** (mid-cycle post-create, R-3 답습) | `/tmp/phase3-5-h-om-r1-anchor-21x.txt` |
| 6 | **디스크 사용량 post-create + Ollama blob storage 변화 확인 (R-S1 발효 정직성 명문)** — `df -h /home/delangi` + `sudo du -sh /home/delangi/문서/.../bootcamp_game/ollama-data/blobs/` 답습 (hard link 답습 시 추가 0건, **Ollama 자체 standard copy 시 +17.3 GiB 추가**). 변화량 > 0 시 B4 분기 발효 의무 | `/tmp/phase3-5-h-om-disk-post-create.txt` |
| 7 | **egress baseline mid (R-6 발효 신규)** — `sudo ss -tan state established` snapshot | `/tmp/phase3-5-h-om-egress-baseline-mid.txt` |

→ Step 1·2·3·4 통과 시 §4 측정 진입 자격, 미통과 시 §5 분기 발동

---

## 4. 측정 절차 (Ollama /api/generate, (h-O) cold 답습)

### 4.1 사전 조건 (R-1 anchor 22회 + R-12 발효 GPU verify)

| Step | 명세 |
|---|---|
| 1 | **다른 model unload (`keep_alive: 0`) + GPU 메모리 0 직접 verify (R-12 답습)** — `nvidia-smi --query-gpu=memory.used --format=csv` 직접 verify. **R-1 anchor 22회 추가** (mid-cycle, 측정 *전*, R-S2 발효) |
| 2 | R-23 사전 (LLM 프로세스 격리) — `ps aux \| grep -E "llama\|ollama\|claude"` |
| 3 | GPU 상태 verify (idle + thermal baseline) |
| 4 | Ollama daemon health (`/api/version`) |

### 4.2 측정 명령 ((h-O) cold 답습 + R-rec-6 keep_alive 명문)

```bash
# decode-161tok prompt (cold) — model 명칭 정확 일치 의무 (R-S5 발효)
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

### 4.3 측정 항목 ((h-O) §4.3 답습 + 3-way 비교 + R-S2 발효 분모 정직성)

| 항목 | 추출 방법 | 정직성 한계 |
|---|---|---|
| Ollama decode tok/s | (분모 1) `eval_count / (eval_duration / 1e9)` + (분모 2) `eval_count / ((total_duration - load_duration - prompt_eval_duration) / 1e9)` 양 분모 raw report 의무 | (h-O) R-S2 답습 영구 |
| Ollama prefill tok/s | `prompt_eval_count / (prompt_eval_duration / 1e9)` + 양 분모 | 동상 |
| total wall-clock | `total_duration / 1e9` | 빌드·로딩·측정 합산 |
| **3-way 비교 (h vs h-O vs h-OM)** | (h) llama.cpp decode 49.6 / prefill 45.4 ↔ (h-O) Ollama library decode 15.29 / prefill 12.43 ↔ (h-OM) Ollama bartowski decode X / prefill Y | source 통제 *최대화* evidence (R-S3 발효 약화) |
| **Δ(h, h-OM) = inference engine *부분* 단독 분리** | (h) 49.6 / (h-OM) X | source 통제 *최대화* (단 5 미통제 변수 + R-S1 Ollama Modelfile FROM 처리 모드 unknown 추가) |
| **Δ(h-O, h-OM) = Ollama internal optimization 변수** | (h-O) 15.29 / (h-OM) X | 동일 engine + 다른 source (library vs bartowski) |
| prompt_eval_count vs llama.cpp 153 cross-check (R-rec-13 답습) | (h-O) 답습 161 가설 자격 강함 | tokenizer 변수 정직성 |
| GPU memory peak + thermal polling (R-rec-3 답습) | 85°C 5분 명문 | 5분 이상 thermal 정직성 |

**측정 종료 후 R-1 anchor 23회 추가 (R-3 답습)** — R-S2 발효 ((h-O) 19 + 본 cycle 4 = 23회 누계 종료 시점) — `sudo sha256sum /proc/3375/exe`. hash 일관 ✓ → raw report 진입 자격.

---

## 5. 분기 조건 ((h-O) §5 답습 + R-S1 발효 B4 강화 + B2 sub-trigger 분리 R-7 + B8 신규)

| 분기 | trigger | 후속 처리 |
|---|---|---|
| **G (성공)** | hard link + Modelfile + `ollama create` 성공 + 측정 완료 (tok/s cold 우선) + Modelfile blob digest verify ((h) sha256 일치 자격 평가) | raw report → **3-way 비교 framing (§9)** → MVP-1 R4 framing 정정 결정적 input |
| **B1 (Modelfile syntax)** | TEMPLATE 또는 PARAMETER 문법 error | raw report → Modelfile 정정 + 사용자 명시 별도 |
| **B2-a (R-7 발효 분리, FROM path 미발견)** | container 내 `/root/.ollama/imports/<file>` 부재 | raw report → hard link 재verify (sym link / ownership / mount) |
| **B2-b (R-7 발효 분리, GGUF parse 에러)** | Ollama 가 GGUF format 파싱 실패 | raw report → (h) GGUF 무결성 verify + OM-alt fallback |
| **B2-c (R-7 발효 분리, Ollama internal 검증 실패)** | Ollama daemon 자체 verify 거부 | raw report → 별도 diagnosis cycle |
| **B3 (model load 실패)** | `/api/generate` 호출 시 model load 에러 (embedded llama.cpp version 미지원 quant scheme 가능성 R-S4 발효) | raw report → (h-O) library version 답습 (호환 verify) |
| **B4-a (디스크 부족)** | hard link/cp 시 ENOSPC | 즉시 중단 → cleanup 사용자 명시 |
| **B4-b (R-S1 발효 강화 신규, Ollama blob copy +17.3 GiB 추가)** | `ollama create` 후 `df -h` 측정 시 디스크 사용량 > 0 증가 (Ollama 자체 standard copy 동작 시) | raw report (정직성 명문 의무) → 본 cycle measurement 진행 정합 (cycle 자체 차단 0) + B4-b 발효 명문 영구 (Ollama issue #1450 + docs.ollama.com 답습) |
| **B5 (Ollama runtime)** | OOM, CUDA error, segfault | raw report → quant 변경 또는 별도 cycle |
| **B6 (tokenizer 분모 mismatch)** | `prompt_eval_count` ≠ (h)/(h-O) 답습 161 | raw report → tokenizer 변수 분리 cycle (R-rec-9 답습) |
| **B7 (HTTP error)** | curl POST timeout, JSON parse error | raw report → 재시도 |
| **B8 (R-rec-8 발효 신규, hard link permission / Ollama daemon access 거부)** | hard link 시 permission denied 또는 Ollama daemon (Docker root) file read 거부 (ACL/SELinux 격리 시) | raw report → ownership/ACL verify + OM-alt fallback (cp 사용) |

각 분기 모두 **자동 다음 단계 진입 0건**, raw report 후 사용자 명시 의무 답습 영구.

---

## 6. 정직성 한계 (R-6 답습 + 20 항목, (h-O) §6 답습 + R-S1/R-S3/R-S4/R-S5 발효)

1. **source 통제 *최대화* 자격 (R-S3 발효 약화)** — (h) bartowski GGUF sha256 답습 hard link, 단 **R-S1 발효 정직성**: Ollama `ollama create` FROM local file 처리 모드 3종 — (1) 그대로 참조 / **(2) 자체 blob 으로 copy 후 sha256 (content-addressable, 표준 동작)** / (3) re-quantize. 사전 평가 0 (Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import 답습)
2. **inference engine 변수 *부분* 단독 분리 시도 자격 강함 (R-S3 발효 약화)** — (h) llama.cpp ↔ (h-OM) Ollama 비교, source + quant + prompt + hardware *최대화* 통제, 단 5 미통제 변수 잔존
3. **5 미통제 변수 잔존 (R-S1/R-S3 발효 추가)**:
   - 측정 도구 framework (llama-cli vs Ollama /api/generate)
   - Ollama embedded llama.cpp version (R-S4 답습)
   - Ollama internal caching/optimization
   - tokenizer 차이 가능성 ((h-O) 답습 161 vs llama.cpp 153)
   - **Ollama Modelfile FROM 처리 모드 unknown (R-S1 발효 신규)**: hard link 그대로 vs 자체 blob copy vs re-quantize, content-addressable sha256 답습 시 (h) sha256 일치 자격 강함, 단 디스크 두 곳 발생 정직성
4. **Ollama `ollama create` FROM local file 처리 모드 정직성 (R-S4 + R-S1 통합)** — 3종 모드 사전 평가 0, post-create direct verify 의무 (`ollama show --modelfile` + `stat -c '%i %s' <blob>` + (h) sha256 cross-check)
5. **R-23 위반 가능성** — Modelfile + create + 측정 ~10~30분 wall-clock
6. **egress 0건 의무 답습** — 본 cycle 의도-외 egress 0건, Ollama daemon internal metadata fetch 가능성 (registry.ollama.ai 접속 0건 verify 의무 §3.3 Step 7 답습)
7. **R-S1 발효 정직성 — 디스크 추가 0건 또는 ~17.3 GiB** — hard link 동일 inode (디스크 추가 0건) **또는** Ollama 자체 blob copy 표준 동작 시 디스크 +17.3 GiB 추가 강한 가능성 (Ollama issue #1450 closed-as-not-planned + docs.ollama.com 답습 영구). 본 cycle 자체 차단 0 (디스크 251G free 답습), 단 framing 정직성 명문 영구
8. **단일 측정 cycle** — 재현성 평가 0 (R-17 답습)
9. **GPU thermal throttling 가능성** — R-rec-3 polling 명문 (85°C 5분 / 본 cycle 5분 미만 가능)
10. **Ollama daemon pid 3375 hash baseline 보존** — silent 교체 0건 영구 답습 (R-1 anchor 20·21·22·23회 일관)
11. **분모 정직성 영구 ((h-O) R-S2 답습)** — 양 분모 raw report 의무
12. **cold 측정 우선 ((h-O) R-S3 답습)** — warm 측정 = 별도 단계 cache hit 효과 분리
13. **F2 가설 평가**:
    - (h-OM) ≈ (h-O) → source conversion 차이 무관, inference engine framework 자체 격차 strong evidence → MVP-1 R4 framing 정정 강한 input HIGH
    - (h-OM) > (h-O) → bartowski conversion 우세, source 변수 단독 분리 cycle 자격
    - (h-OM) < (h-O) → Ollama library internal optimization 우세, Modelfile vs library pipeline 차이 verify cycle
    - (h-OM) ≈ (h) → 가능성 매우 낮음 (Ollama < llama.cpp ~3.24× 답습), F2 *역방향 강화*
    - **어느 경우든 본문 정정은 별도 cycle (R-9 답습 영구)**
14. **M3 결정 *고정* 자격 무관** — (k) 별도 cycle 영구
15. **MVP-1 합의 R4 본문 정정 자격 무관** — input only
16. **본 brief 가 후속 cycle 자동 진입 trigger 0**
17. **본 brief commit 자체 = 단일 atomic commit 의무** — brief 본문만
18. **Ollama Modelfile vs library internal pipeline 차이 가능성 (R-S4 답습 부분)** — Ollama 가 Modelfile 등록 model 을 library model 과 *동일 internal pipeline* 사용 자격 단언 0
19. **R-S5 발효 정직성 — Modelfile 부분 답습 정직성** — TEMPLATE + 6 PARAMETER 답습, LICENSE block 의도적 0건 (Ollama Modelfile create 시 optional, functional risk 0)
20. **R-S5 발효 정직성 — Hard link 권한 verify 의무** — (h) GGUF `delangi:delangi 0664` ↔ ollama-data `root:root 0755`, hard link 후 link 자체 권한 = inode 답습 `delangi:delangi 0664` → Ollama daemon (Docker root) read 가능 자격 강함 (o+r=4), 단 명문 verify 의무

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 16 항목과 §7 차단 조건은 **1:1 매핑 의무**.

1. ❌ 본 brief 자체 Modelfile/create/측정/sudo 실행
2. ❌ Ollama daemon 변경 (pid 3375 hash baseline 보존)
3. ❌ (h) GGUF 파일 변경 또는 cleanup (hard link source 보존)
4. ❌ (g) GGUF 파일 변경
5. ❌ (h-O) Ollama library blob 변경
6. ❌ llama.cpp HEAD `c0c7e147` 변경
7. ❌ MVP-1 합의 본문 자동 정정 (R-9 답습 영구)
8. ❌ 헌법·ADR 본문 자동 정정
9. ❌ M3·M4 결정 *고정* ((k) 별도)
10. ❌ runtime backend 코드 작성
11. ❌ 메모리 자동 갱신
12. ❌ (h-OL)/(j)/(k)/(l)/(m)/(n) 자동 진입
13. ❌ brief commit 자동 진입
14. ❌ Ollama create 시점 = 사용자 명시 *직접* 의무 (R-S1 발효 디스크 +17.3 GiB risk 답습)
15. ❌ (g)+(h)+(h-O)+(h-OM) 통합 본문 정정 + 4-way 통합 *분석* cycle ≠ 통합 *본문 정정* cycle (별도 차원 carry-over)
16. ❌ (g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime 자동 진입 (chain 영구 종결 의무 답습 영구)

---

## 8. 후속 carry-over (자동 진입 0건, 사용자 명시 의무 답습 영구)

### 8.1 본 cycle 결과 분기별 carry-over

| 분기 | 후속 cycle |
|---|---|
| G + (h-OM) ≈ (h-O) | source conversion 차이 무관 → inference engine framework 자체 격차 strong evidence → MVP-1 R4 framing 정정 강한 input HIGH |
| G + (h-OM) > (h-O) | bartowski conversion 우세 → source 변수 단독 분리 cycle 자격 평가 |
| G + (h-OM) < (h-O) | Ollama library internal optimization 우세 → Modelfile vs library internal pipeline 차이 verify cycle |
| G + (h-OM) ≈ (h) | (h-O) S4 답습 — 가능성 매우 낮음, F2 역방향 강한 input |
| **B4-b (Ollama blob copy +17.3 GiB)** | R-S1 발효 raw evidence 강화 → Ollama 표준 동작 답습 영구 input (cycle 진행 정합 + 정직성 명문) |
| B1~B3, B5~B8 | 다른 절차 또는 (h-O) 답습 처리 (사용자 명시 별도) |

### 8.2 본 cycle 무관 carry-over (R-15 + R-rec-15 발효 신규)

| 후보 cycle | 우선순위 | 비고 |
|---|---|---|
| **MVP-1 합의 R4 framing 정정 evidence 별도 cycle** | **HIGH** | (g)/(h)/(h-O)/(h-OM) 4-way 종합 input 결정적 (R-9 답습 영구) |
| **(g)+(h)+(h-O)+(h-OM) 4-way 통합 *분석* cycle** | **HIGH ⭐⭐** | scope 4 차원 (R-rec-16 발효): (1) MVP-1 R4 framing 정정 input + (2) F2 가설 강화/약화 + (3) Provider Liquidity finding 종합 + (4) (j) 진입 자격 평가 |
| **(h-OL) llama.cpp Ollama blob `78b329e716e7...ba9cc` 직접 측정 cycle (R-15 발효 신규)** | **MEDIUM ⭐** | egress 0 + 디스크 0 + 시간 ~30분, source 통제 차원 *역방향* 단독 분리 (engine = llama.cpp 통제, source = Ollama library blob 변경). C-rec-7 답습 |
| **Ollama prefill 처리 framework overhead 검증 cycle** | MEDIUM | (h-O) F-2 23.89× outlier 답습 |
| **Phase 1 N=3 repetitions Ollama 답습 cycle** | MEDIUM | (h-O) C-S2 답습 |
| **Ollama embedded llama.cpp version verify cycle** | MEDIUM | (h-O) R-S4 + N-15 답습 |
| **Ollama Modelfile vs library internal pipeline cross-check cycle** | MEDIUM | §6 #18 답습 |
| **llama.cpp graceful tensor name resolution 검증** | MEDIUM | (g) F-2 + (h) R-S3 답습 |
| **(j) advisory wall-clock 측정 cycle** | MEDIUM | 자비스 비전 직접 진전 |
| **`llama-bench` carry-over (R-rec-12 격상)** | MEDIUM | (g)/(h)/(h-O) 답습 |
| **bartowski conversion lineage cross-check cycle** | MEDIUM | (h-O) C-N-3 답습 |
| **Modelfile PARAMETER 변경 단독 cycle** | LOW | (h-O) C-rec 답습 |
| **OM-direct-blob (Ollama manifest 우회) 신규 source 등록 방식 cycle** | LOW | R-rec-14 발효 신규 |
| **GGUF tokenizer.chat_template 직접 read cycle** | LOW | (h-O) C-S3 답습 |
| **(k) M3·M4 결정 *고정*** | DEFER | 변수 분리 input 강화 후 |
| **(l) MVP-1 트랙 B 구현** | DEFER | (k) 통과 의무 답습 영구 |
| **다른 quant 비교 (Q5_K_M / IQ4_XS)** | LOW | R-rec-2 답습 |
| **외부 benchmark cross-reference cycle** | LOW | (h-O) C-N-5 답습 |
| **tokenizer 변수 단독 분리 cycle (B6 발생 시)** | LOW | R-rec-9 답습 |
| **(g)+(h)+(h-O)+(h-OM) 통합 본문 정정 cycle** | DEFER | 기존 본문 변경 0건 |
| **(m) §12 Ollama 위생 정정** | LOW | 본 cycle 무관 |
| **(n) Phase 3 brief v1.2 보강** | LOW | 별도 |
| **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) prime/super-prime** | ❌ **자동 진입 명백 부정** | chain 영구 종결 의무 답습 영구 |

### 8.3 본 brief 자체 후속 단계 ((h-O) 동형 풀 7단계 답습)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `3d02edb`, 469줄 | 명시 완료 |
| (2) 풀 3+1 합의 진행 + commit | `bcc4974`, 440줄, BLOCKING 15 + R-S1~R-S5 | 명시 완료 |
| **(3) brief v1.1 보강 + commit (본 단계)** | BLOCKING 15 verbatim 100% + R-S1~R-S5 흡수 21+곳 + 권고 16 일부 + §11 신규 | **진행 중** |
| (4) Modelfile 작성 + ollama create (~5분) | hard link + Modelfile + `ollama create` (R-S1 발효 정직성: blob copy +17.3 GiB 가능성) | **사용자 명시 *직접* 의무** |
| (5) verify + 측정 실행 (~30분) | §3.3 + §4 절차 답습 (cold 우선) | 사용자 명시 후 |
| (6) raw report + SESSION + INDEX + commit | (h-O) 답습 | 결과 확인 후 |
| (7) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. (h) ↔ (h-O) ↔ (h-OM) 3-way 비교 framing (R-S3 발효 약화)

### 9.1 (h) + (h-O) baseline 답습

| 항목 | (h) llama.cpp direct | (h-O) Ollama library |
|---|---|---|
| source | bartowski sha256 `382b4f5a164d...33a95` | Ollama library blob `78b329e716e7...ba9cc` (다른 source R-S1 발효) |
| inference engine | llama-cli `c0c7e147` direct | Ollama 0.20.4 (Docker container) |
| decode-161tok prompt / generation | 389.4 / 49.6 t/s | 118.43 / 15.29 t/s (~3.29× / ~3.24× 느림) |
| prefill-2k prompt / generation | 1916.8 / 45.4 t/s | 80.25 / 12.43 t/s (~23.89× / ~3.65× 느림) |

### 9.2 (h-OM) 예상 결과 시나리오 (사전 가설 평가, 단정 0)

| 시나리오 | (h-OM) decode cold tok/s 가설 | 해석 자격 | 후속 |
|---|---|---|---|
| **S1: (h-OM) ≈ (h-O) (~13~17 t/s)** | source conversion 차이 무관 — Ollama framework 자체 격차 본질 | MVP-1 R4 framing 정정 강한 input HIGH | F2 framing 정정 cycle |
| **S2: (h-OM) > (h-O) (~17~25 t/s)** | bartowski conversion 우세 — Ollama library 부분 약화 | source 변수 평가 cycle | library vs bartowski cycle |
| **S3: (h-OM) < (h-O) (~8~13 t/s)** | Ollama library internal optimization 우세 | Modelfile vs library internal pipeline 차이 verify cycle | 별도 verify |
| **S4: (h-OM) ≈ (h) (~45~50 t/s)** | inference engine 동일 자격 (가능성 매우 낮음) | F2 *역방향 강화* | F2 재고 cycle |
| **S5: Modelfile create 실패 (B1~B3)** | TEMPLATE / FROM path / GGUF format 호환 미흡 | 대안 자격 평가 | OM-alt (copy) 또는 library 답습 |
| **S6: tokenizer 분모 mismatch (B6)** | Ollama tokenizer ≠ Modelfile 등록 후 변경 | tokenizer 변수 분리 cycle | R-rec-9 답습 |
| **S7: B4-b 발효 (Ollama blob copy +17.3 GiB, R-S1 발효)** | R-S1 발효 raw evidence 강화, 본 cycle measurement 진행 정합 | 정직성 명문 영구 + Ollama 표준 동작 답습 영구 input | (cycle 자체 차단 0) |

### 9.3 핵심 정직성 (R-S3 발효 framing 약화)

- ✅ **본 cycle = source 통제 *최대화* + inference engine *부분* 단독 분리 시도** (R-S3 발효 약화 framing)
- ❌ 단 **5 미통제 변수 잔존** (측정 도구 framework + Ollama embedded llama.cpp version + Ollama internal caching/optimization + tokenizer 차이 + **Ollama Modelfile FROM 처리 모드 unknown R-S1 발효 추가**)
- → **(h, h-OM) 1:1 비교 = inference engine framework 자체 격차 evidence *부분* 강함** (source 통제 *최대화*, 단 Modelfile 처리 모드 unknown)
- → **(h-O, h-OM) 1:1 비교 = Ollama internal optimization 변수 (source 다름)**
- → **4-way (g)/(h)/(h-O)/(h-OM) 통합 분석 cycle HIGH ⭐⭐ carry-over** + **(h-OL) MEDIUM 신규 carry-over (R-15 발효)**

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = (h-OM) 풀 3+1 합의 (`bcc4974`, 440줄) BLOCKING 15 verbatim 100% 흡수 + R-S1~R-S5 흡수 21+ 곳 + 권고 16 일부 흡수 + §11 v→v1.1 변경 일람 신규
- 본 cycle 진입 = (h-O) cycle 완료 (`9685ae3`) + 사용자 명시 (h-OM) 진입 형태 + Modelfile TEMPLATE (h-O) 답습 + Phase 3.5-OM 명명 직후
- 본 brief 자체 머신 변경 0건 (Modelfile/create/측정/sudo 0)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (chain 영구 종결 의무 답습 영구)
- ⭐⭐⭐ R-S1 CRITICAL 흡수 = Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습 영구 → hard link 가정 falsified, 디스크 +17.3 GiB 추가 risk 명문
- ⭐⭐ R-S2 HIGH 흡수 = R-1 anchor 20·21·22·23회 명문 정정 (3 위치 self-inconsistency 해소)
- ⭐⭐ R-S3 HIGH 흡수 = "*진짜* 단독 분리" → "*부분* 단독 분리 시도" 약화 framing
- ⭐ R-S4 MEDIUM 흡수 = §3.1 Step 7 신규 + §3.3 Step 3 강화 + §6 #4 강화
- ⭐ R-S5 MEDIUM 흡수 = LICENSE 의도적 부분 답습 명문 + tag 자동 부여 verify + 권한 verify 신규
- 본 brief v1.1 길이 = 469줄 → ~580~620줄 예상

---

## 11. v1 → v1.1 변경 일람

### 11.1 BLOCKING 15 흡수 매트릭스 (verbatim 100%, R-21 답습 영구)

| BLOCKING | 출처 | brief v1.1 정정 위치 | 본문 변경 |
|---|---|---|---|
| **R-1 (R-S1) ⭐⭐⭐ CRITICAL** | 3-way Consensus (A-B2 + B-S1 + C-S1) + 외부 Ollama #1450 evidence | §1.1 line 74 + §0 #16 + §3.0.1 + §6 #7 + §5 B4-b 신규 분기 | 5 곳 정정, "디스크 0건 또는 +17.3 GiB" 양 framing |
| **R-2 (R-S3) ⭐⭐ HIGH** | 3-way Consensus | §1.1 line 66 + §0 #1 + §9.3 약화 | 3 곳 약화 ("*진짜*" → "*부분*") |
| **R-3 (R-S4) ⭐⭐ HIGH** | A-B5 + B-B3 + C-B3 | §6 #4 강화 + §3.1 Step 7 신규 + §3.3 Step 3 강화 | 3 곳 |
| **R-4 (R-S2) ⭐⭐ HIGH** | Agent A direct + Reviewer raw | 모든 R-1 anchor 회차 (§0 #2 + §3.1 + §3.3 + §4.1 + §4.3) 20·21·22·23 verbatim 정정 | 6+ 곳 |
| **R-5 (R-S5) ⭐ MEDIUM** | A-B4/A-S2 + A-B7 + A-S3 통합 | §1.3 LICENSE 명문 + §3.2 Step 4 tag verify + §3.3 Step 1 + §3.2 Step 2 후속 권한 verify | 4 곳 |
| **R-6** | 2+ Agent (A-B8 + B) | §3.1 신규 step + §4 측정 종료 후 egress baseline post | 2 곳 |
| **R-7** | Agent B 단독 | §5 B2 sub-trigger 3 묶음 분리 (B2-a, B2-b, B2-c) | §5 분기 매트릭스 |
| **R-8** | Agent A 단독 (R-S4 통합) | §6 #4 강화 (R-3 통합) | 흡수 완료 |
| **R-9** | Agent B 단독 (R-S1 통합) | §5 B4 분기 강화 (R-1 통합) | 흡수 완료 |
| **R-10** | Agent A 단독 (R-S5 통합) | §3.2 Step 3 LICENSE 의도적 부분 답습 명문 (R-5 통합) | 흡수 완료 |
| **R-11** | Agent B 단독 | §0 *하는* 것 8 항목 + §6 정직성 한계 18 항목 cross-check 명문 | 1 곳 명문 강화 |
| **R-12** | Agent B 단독 | §3.3 Step + §4 password 누출 grep verify 명문 | 2 곳 명문 |
| **R-13** | Agent B 단독 | §3.1 신규 Step 9 (`ollama list \| grep -i bartowski` model 명칭 conflict pre-verify) | 1 곳 신규 step |
| **R-14** | Agent A 단독 (R-S5 통합) | §3.2 Step 2 후속 권한 verify (R-5 통합) | 흡수 완료 |
| **R-15** | Agent C 단독 | §8.2 (h-OL) llama.cpp Ollama blob 직접 측정 cycle MEDIUM 신규 carry-over | §8.2 신규 행 |

### 11.2 Reviewer 단독 격상 R-S1~R-S5 흡수 매트릭스 (위 11.1 답습 통합)

- **R-S1 ⭐⭐⭐ CRITICAL** → R-1 발효 (5 곳)
- **R-S2 ⭐⭐ HIGH** → R-4 발효 (6+ 곳)
- **R-S3 ⭐⭐ HIGH** → R-2 발효 (3 곳)
- **R-S4 ⭐ MEDIUM** → R-3 발효 (3 곳)
- **R-S5 ⭐ MEDIUM** → R-5 발효 (4 곳) + R-10/R-14 통합
- **총 21+ 곳 정정**

### 11.3 권고 16 흡수 매트릭스 (강한 권고 직접 흡수)

| 권고 | 흡수 자격 | brief v1.1 정정 위치 |
|---|---|---|
| R-rec-1 (embedded llama.cpp version) | 강함 | §3.1 Step 7 신규 (R-3 통합) |
| R-rec-2 (§5 B2 sub-trigger) | 강함 | §5 분기 매트릭스 (R-7 통합) |
| R-rec-3 (§6 #2 framing 약화) | 강함 | §6 #2 + §1.1/§9.3 (R-2 통합) |
| R-rec-4 (blob storage verify) | 강함 | §3.3 Step 3·6 강화 (R-3/R-1 통합) |
| R-rec-5 (model 명칭 conflict) | 강함 | §3.1 Step 9 (R-13 통합) |
| R-rec-6 (password 누출 grep) | 강함 | §3.3·§4 (R-12 통합) |
| R-rec-7 (sudo 근거 명문) | 부분 | §3.2 Step 1·2 |
| R-rec-8 (B 분기 신규) | 부분 | §5 B8 신규 |
| R-rec-9 (sudo 8~10회) | 부분 | §3.0 line 134 정정 |
| R-rec-10 (§5 B4 강화) | 강함 | §5 B4-b (R-1 통합) |
| R-rec-11 (tag 자동 부여) | 강함 | §3.3 Step 1 (R-5 통합) |
| R-rec-12 (FROM 처리 모드 3종) | 강함 | §6 #4 (R-3 통합) |
| R-rec-13 (§1.1 framing 약화) | 강함 | §1.1 line 66 (R-2 통합) |
| R-rec-14 (OM-direct-blob 신규) | 부분 | §2.1 표 신규 행 |
| R-rec-15 ((h-OL) cycle) | 강함 | §8.2 신규 (R-15 통합) |
| R-rec-16 (4-way 통합 scope) | 강함 | §8.2 4 차원 명문 |

### 11.4 NOTE 18 by-reference (변경 0건, §7 합의 보고서 답습)

### 11.5 기각 5 답습 (변경 0건)

---

**본 brief v1.1 작성 완료** (Phase 3.5-OM (h-OM) Ollama Modelfile bartowski 등록 cycle entry plan, 풀 3+1 합의 APPROVE w/ COND + BLOCKING 15 verbatim 100% 반영 + R-S1~R-S5 흡수 21+곳 + 권고 16 일부 흡수 + §11 v→v1.1 변경 일람 신규. ⭐⭐⭐ R-S1 CRITICAL 발효 = Ollama issue #1450 closed-as-not-planned + docs.ollama.com/import "regular copy" 답습 영구 + 디스크 +17.3 GiB 추가 risk 명문 + (h-OL) MEDIUM 신규 carry-over. 본 cycle 머신 변경 0건. 다음 단계 = 사용자 명시 의무 답습 영구.)
