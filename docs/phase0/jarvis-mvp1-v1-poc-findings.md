# 자비스 MVP-1 V-1 PoC findings (DRAFT — Stage 1~5: read-only + 측정 + Phase 1 검증)

> **본 findings = V-1 PoC의 *1~5차 단계* + M3·M4 합의 Phase 1 cycle.** Stage 1~3 = read-only, Stage 4 = §4 측정 (qwen3-coder-next + qwen2.5-coder:32b), Stage 5 = Phase 1 cycle (A-진단 + C-c cache miss 분리). gap-pull·llama.cpp 빌드·M3/M4 결정 = **0건**. `ollama search` egress = **0건** (R-11 답습). 데몬 변경 0건. R-1 anchor 5회 일치 (silent 교체 미발생 확정).

**작성일**: 2026-05-23
**Status**: DRAFT — Stage 1+2+3+4+5/N
**선행 답습**: `jarvis-mvp1-v1-poc-entry-brief.md`(v1.1, HEAD `9e68fbb`, BLOCKING 6 반영) / `3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md` / brief v2 §6
**raw**:
- Stage 1: `docs/phase0/v1-poc-raw/2026-05-23T11-53-v1-1-readonly.json` + `2026-05-23T11-53-qwen3-coder-next-manifest.json`
- Stage 2: `docs/phase0/v1-poc-raw/2026-05-23T12-15-v1-2-step2-readonly.json`
- Stage 3: `docs/phase0/v1-poc-raw/2026-05-23T13-00-v1-egress-baseline-readonly.json`
- Stage 4: `docs/phase0/v1-poc-raw/2026-05-23T21-30-v1-3-measurement-summary.json` + 측정 30개 JSON
- Stage 5 (Phase 1): `docs/phase0/v1-poc-raw/2026-05-24-phase1-summary.json` + A-진단 raw (`2026-05-24-a-diagnosis-decode-result.json` + `2026-05-24-a-diagnosis-dmon-qwen3cnext-decode.txt`) + C-c raw 3개 (`2026-05-24-cc-{1,2,3}-qwen3cnext-prefill8k-unique.json`)

---

## 0. 본 findings 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. R-1 anchor 식별값 기록 — 3회 일치 확인 (§1)
2. §2 V1-1 5 steps read-only 결과 정리 (§2)
3. §3 V1-2 Step 1 `qwen3-coder-next` manifest 해석 (§3)
4. §3 V1-2 Step 2a 후보 풀 식별표 (§3a)
5. §3 V1-2 Step 2b 로컬 후보 부재 확인 + 기존 4 모델 dense 검증 (§3b)
6. §8 egress baseline (§3c)
7. **§4 V1-3 tok/s 측정** — qwen3-coder-next + qwen2.5-coder:32b baseline (§3d)
8. 정직성 한계 명시 (§4)
9. 다음 단계 권고 (§5)

### 하지 않는 것 (entry brief §0.2 영구 답습)

- ❌ M3 / M4 결정 *고정* — 본 findings 는 raw 보고만, 결정 입력 자격 X (entry brief §4.4 답습)
- ❌ Ollama 데몬 재시작 / kill / signal / 설정 변경 (3회 R-1 hash 일치로 검증)
- ❌ 모델 pull / gap-pull / 빌드 / install
- ❌ `ollama search` (ollama.com egress 발생 — R-11 답습, 별도 cycle)
- ❌ Ollama Hub 실재성 검증 (egress 필요)
- ❌ V-1 findings *후* 별도 합의 진행 (M3·M4 결정 입력)
- ❌ llama.cpp 비교 측정 (별도 명시 승인)
- ❌ §12 옵션 E 위생 정정 trigger 발효

---

## 1. R-1 binary anchor (BLOCKING 의무, 측정 *전*)

| 항목 | 값 |
|---|---|
| PID | `3375` (entry brief §1.2 발견과 동일, 데몬 재시작 0) |
| `/proc/3375/exe` owner | root (UID 0) |
| `/bin/ollama` fs 상태 | **stat 실패** (실행 중 inode 잔존, fs 삭제됨 — entry brief §1.2 재확인) |
| sha256sum (sudo 1회) | **`ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10`** |
| 실행 방법 | 사용자 명시 prompt 입력 (`! sudo sha256sum /proc/3375/exe`, read-only, 데몬 변경 0) |

### 1.1 anchor 의미

- **현 시점** binary 식별값 = 측정 cycle anchor. §4 측정 *직전* + *직후* 재기록 → 동일 hash 확인 = silent 교체 감지.
- 본 findings 단계 = 측정 0 → 본 hash 는 *read-only 단계* anchor 한정. §4 측정 진입 시 *새* sha256sum (측정 직전 1회) 갱신 + 측정 *후* 재기록 의무 (R-1).

### 1.2 정직성 한계 (entry brief §1.2 R-1 NOTE 답습)

- 본 hash = **출처 미상 binary 의 현 시점 식별값**. 표준 Ollama 빌드 대비 재현 가능성 *별도* 검증 0 (binary origin 미상 → 다른 환경에서 동일 환경 구성 불가능).
- silent 자동 업데이트 / origin 교체 위험 = **본 hash 만으로 평가 불가**. 측정 *후* 동일 hash 확인은 *해당 측정 세션 내* 무결성만 보장.
- 진정한 위생 정정 (origin 표준화) = entry brief §12 옵션 E (V-1 findings *후* 별도 cycle).

---

## 2. §2 V1-1 — Ollama 구동 위생 점검 (5 steps)

### 2.1 결과 표

| Step | 명령 | 결과 | 판정 |
|---|---|---|---|
| 1 | `curl -s /api/version` | `{"version":"0.20.4"}` HTTP 200, JSON valid | **PASS** (≥ 0.4, MoE 지원, R-2 schema 검증 충족) |
| 2 | `curl -s /api/ps` | `{"models":[]}` | idle baseline 정상 (`size_vram` 미적용 — 로드 모델 0) |
| 3 | `nvidia-smi pmon -c 1` | Xorg(2551) + gnome-shell(2915) only | ollama GPU 미사용 (idle 정상). R-10 fallback 미적용 |
| 4 | `ss -tln \| grep 11434` | `LISTEN 127.0.0.1:11434` only | **PASS** (M6 localhost 충족, `0.0.0.0` 미바인딩, R11 추론시점 egress 입력 충족) |
| 5 | `env \| grep '^OLLAMA_'` + `/api/ps` | unset (기본값), 동시 로드 0 | OLLAMA_* 기본값. **데몬 *환경* (root `/proc/3375/environ`) 별도 확인 권고** (§4.1 한계) |

### 2.2 실패 분기 (R-2 fail-closed)

| 실패 분기 | 트리거 | 본 단계 결과 |
|---|---|---|
| 데몬 죽음 | `/api/version` timeout 또는 PID 변동 | 트리거 0 (PID 3375 변동 0) |
| 11434 다른 프로세스 점유 | JSON schema 검증 실패 | 트리거 0 (정상 Ollama JSON) |
| GPU OOM CPU fallback | `size_vram == 0 && size > 0` 패턴 | 트리거 0 (모델 미로드) |
| `/api/version` 비정상 응답 | JSON 파싱 실패 | 트리거 0 |

**fail-closed 분기 0건 트리거**. 측정 단계 진입 *전* baseline 위생 충족.

### 2.3 한계

- Step 5 의 `OLLAMA_*` 환경변수 점검 = **`delangi` shell 한정**. 데몬 자체 환경(root `/proc/3375/environ`)은 root 권한 필요 → 본 단계 미확인. 측정 단계 진입 시 (a) 데몬 환경 sudo 확인 또는 (b) `OLLAMA_HOST=127.0.0.1` 등이 *내부* 설정 가능성 인지 + raw 에 명시.
- `nvidia-smi pmon` idle 결과 = "ollama 가 GPU 미사용" 결정적 증거 X (모델 미로드 = pmon 표시 0 의 정상 결과). 측정 *중* pmon 동시 캡처(R-20)에서 의미 발생.

---

## 3. §3 V1-2 Step 1 — `qwen3-coder-next` MoE 확인

### 3.1 manifest 핵심 필드

| 분류 | 키 | 값 |
|---|---|---|
| **architecture** | `general.architecture` | `qwen3next` |
| **총 파라미터** | `general.parameter_count` | `79,674,391,296` (≈ 79.7B) |
| **양자화** | `details.quantization_level` | `Q4_K_M` (~51.7GB on disk) |
| **MoE expert 수** | `qwen3next.expert_count` | **`512`** |
| **MoE 활성 expert** | `qwen3next.expert_used_count` | **`10`** (top-10) |
| **MoE FFN 폭** | `qwen3next.expert_feed_forward_length` | `512` |
| **MoE shared FFN** | `qwen3next.expert_shared_feed_forward_length` | `512` |
| **dense FFN 폭** | `qwen3next.feed_forward_length` | `5120` |
| **layer 수** | `qwen3next.block_count` | `48` |
| **embedding 차원** | `qwen3next.embedding_length` | `2048` |
| **context length** | `qwen3next.context_length` | `262144` (256k) |
| **attention head** | `qwen3next.attention.head_count` | `16` (kv_head_count null) |
| **full attention 간격** | `qwen3next.full_attention_interval` | **`4`** (4 레이어 중 1개) |
| **SSM conv kernel** | `qwen3next.ssm.conv_kernel` | `4` |
| **SSM group** | `qwen3next.ssm.group_count` | `16` |
| **SSM inner size** | `qwen3next.ssm.inner_size` | `4096` |
| **SSM state size** | `qwen3next.ssm.state_size` | `128` |
| **capabilities** | `.capabilities` | `["completion", "tools"]` |

### 3.2 ✅ MoE 확인 (brief §1.3 "요확인" 정정)

- `expert_count: 512` + `expert_used_count: 10` = **sparse top-10 activation** = MoE 본질.
- brief v2 §6 "1차 후보 Qwen3.x-A3B/A10B" 와 family 일치 (`qwen3next` = Qwen3-Next family).
- **§4 측정 1차 후보 자격 충족** — gap-pull 없이 본 모델만으로 V1-3 진입 가능.

### 3.3 ⭐ 추가 발견 — Qwen3-Next hybrid SSM+Attention (brief v2 §6 미명시)

- `full_attention_interval: 4` → 48 레이어 중 **12개만 full attention**, 나머지 **36개는 SSM/Mamba**(`ssm.*` 필드 존재).
- SSM = fixed-size hidden state → **KV cache 부담 감소**.
- 함의 (가설, 측정 후 검증):
  - 273GB/s 대역폭 병목 가설(brief v2 §2) 우호적 — prefill 단계에서 KV cache 메모리 압박 감소.
  - 긴 context(256k) 시 dense attention 대비 메모리 우위.
- ⚠️ **가설 한정**: 측정 0건. tok/s · 메모리 점유 실측은 §4·§6 단계.

### 3.4 활성 파라미터 추정

| 구분 | 추정 |
|---|---|
| dense 부분 (attention + embedding + SSM + shared FFN + LM head) | 별도 계산 필요 |
| MoE sparse 부분 (10/512 expert FFN per token) | ~10/512 × (expert_FFN × layer 수) |
| **활성 합계** | **모델 카드 참조 권고** (본 단계 정량 0) |

> brief v2 §6 R5 의 roofline 수치(A3B Q4 ~90–120 실효, dense 70B Q4 한자릿수)는 **활성 ~3B 가정**. qwen3-coder-next 활성 파라미터가 ~3B 인지 ~10B 인지 별도 검증 필수 — 측정값 해석 분기(M4 결정 입력) 직접 영향.

### 3.5 `capabilities: tools` NOTE (entry brief §5 Step 4 / R-38)

- Ollama manifest 가 `"tools"` 능력 보고 → `/v1/chat/completions` 가 `tools` 파라미터 *수용* 가능성 ↑.
- brief v2 R2 (BossAdvice 텍스트 전용 frozen) **답습 보강**: OllamaBoss 구현 시 *코드 레벨* tool 차단 의무 (endpoint 거부 의존 X).
- §5 Step 4 측정에서 `tools` 요청 → 거부/수용 binary 확인 후 R-38 NOTE 진행.

---

## 3a. §3 V1-2 Step 2a — 후보 풀 식별 (brief §3.2 답습)

### 3a.1 후보 8종 식별표

| # | 후보 | family | 활성 추정 (외부) | 목적 | 로컬 |
|---|---|---|---|---|---|
| 1 | Qwen3.5-A3B-Instruct | qwen3.5 | ~3B | 1차 후보 (활성 ≤10B 우선) | ❌ |
| 2 | Qwen3.5-Coder-A10B | qwen3.5 | ~10B | 코딩 특화 MoE | ❌ |
| 3 | **qwen3-coder-next** | qwen3next | top-10/512 (별도) | **본 환경 1차 후보** (Step 1 MoE 확인) | ✅ |
| 4 | DeepSeek-V3.1-Lite | deepseek-v3 | ~3B | 후보 확장 (R-5) | ❌ |
| 5 | GLM-4-MoE | glm4 | 외부 미확정 | 후보 확장 (R-5) | ❌ |
| 6 | Granite-3.5-MoE | granite | 외부 미확정 | 후보 확장 (R-5) | ❌ |
| 7 | OLMoE | olmo | 외부 미확정 | 후보 확장 (R-5) | ❌ |
| 8 | mixtral:8x7b | mixtral | ~13B | **R-14**: MoE 동작 검증 한정 (A3B 4배 → tok/s 직접 비교 X) | ❌ |

### 3a.2 선정 논리

- 활성 ≤ 10B + Q4 ≤ 20GB **우선**.
- 그 외 = NOTE (R-5).
- 활성 파라미터 추정 = **외부 모델 카드 의존** (본 진입 검증 0).

---

## 3b. §3 V1-2 Step 2b — 로컬 후보 부재 확인 + 기존 4 dense 검증

### 3b.1 인벤토리 재확인

`curl -s /api/tags` (localhost·read-only) — brief §1.3 5종과 **일치**, 추가 모델 0. 총 ~156GB(API 보고, GiB 환산 기준).

### 3b.2 후보 11종 로컬 부재 확인

`curl -s /api/show -d '{"name":"<candidate>"}'` (localhost, **egress 0**):

| 시도 tag | HTTP | 결과 |
|---|---|---|
| `qwen3:30b-a3b` / `qwen3:30b` / `qwen3-coder:30b-a3b` / `qwen3.5:a3b` / `qwen3-coder:a10b` / `mixtral:8x7b` / `deepseek-v3.1-lite:latest` / `deepseek-v3:lite` / `granite-3.5-moe:latest` / `olmoe:latest` / `glm-4-moe:latest` | **404 모두** | `model '...' not found` (로컬 부재) |

**결론**: 로컬 MoE = `qwen3-coder-next:latest` **단 1종**. 다른 후보 0종 로컬. Hub 실재성 = `ollama search` egress = 별도 cycle.

### 3b.3 ⚠️ tag format 한계

404 = *시도한 해당 tag* 부재일 뿐. 동일 모델의 다른 tag(예: `qwen3:30b-a3b-instruct-q4_K_M`·family-specific 형식) 가 Hub 에 실재할 가능성 잔존. 외부 cycle 답습 필요.

### 3b.4 기존 4 dense 모델 manifest 검증

| 모델 | arch | param | block | context | quant | capabilities | dense | baseline 자격 |
|---|---|---|---|---|---|---|---|---|
| `qwen2.5-coder:32b` | qwen2 | 32.8B | 64 | 32k | Q4_K_M | completion·tools·insert | ✅ | **✅ §4.3 dense baseline 권고** (qwen 계열·Q4_K_M·tools, MoE 직접 비교군 자격) |
| `llama3.3:70b` | llama | 70.6B | 80 | 128k | Q4_K_M | completion·tools | ✅ | △ 273GB/s 한계 측정용(*bandwidth ceiling*) — MoE 비교 baseline 아님 |
| `exaone3.5:32b` | exaone | 32.0B | 64 | 32k | Q4_K_M | completion | ✅ | ❌ tools 미지원 → BossAdvice 호환 ↓ |
| `exaone4:32b` | exaone4 | 32.0B | 64 | 128k | **Q8_0** | completion | ✅ | ❌ 다른 양자화 + tools 미지원 |

- **4/4 dense 확인** (`moe_fields = {}` 전부 empty). brief §1.3 dense 가정 정합.
- **§4.3 baseline 권고**: `qwen2.5-coder:32b` **단일** (qwen3-coder-next 와 family 가깝고 Q4_K_M·tools 동일).

---

## 3c. §8 — egress baseline (측정 *전* snapshot, R-3 시간 한정)

### 3c.1 방법

| 점검 | 명령 | 권한 |
|---|---|---|
| 전체 ESTABLISHED + process info | `sudo ss -tnp state established` (사용자 명시 prompt 입력, 1회, read-only) | sudo 1회 |
| 일반 ESTABLISHED + 외부만 filter | `ss -tn state established '! ( src 127.0.0.0/8 or dst 127.0.0.0/8 )'` | delangi |
| LISTEN 재확인 | `ss -tlnp \| grep 11434` | delangi |
| `sport :11434` ESTABLISHED | `ss -tnp sport :11434` | delangi |

### 3c.2 ⭐ Ollama PID 3375 egress 검증

| 항목 | 결과 |
|---|---|
| Ollama ESTABLISHED 외부 연결 | **0건** |
| Ollama ESTABLISHED 로컬 연결 | 0건 |
| Ollama LISTEN | `127.0.0.1:11434` only |
| Ollama sport :11434 발신 | 0건 |

> **✅ §8.1 기준 충족** (*Ollama 한정* — baseline snapshot 시점).

### 3c.3 외부 ESTABLISHED 9개 분류 (Ollama 비관련)

| Peer | Process | 정체 |
|---|---|---|
| `160.79.104.10:443` ×2 | `claude` (pid 3999024) | **Claude Code 본 세션** Anthropic API |
| `34.149.66.137:443` | `claude` (pid 3999024) | Claude Code misc (GCP likely) |
| `192.168.45.21:54612` / `:56907` ← `:22` | `sshd` ×2 | 사용자 inbound SSH 2 세션 |
| `172.238.6.34:443` / `199.165.136.101:443` / `192.200.0.112:443` | `tailscaled` (pid 2122) ×3 | Tailscale VPN |
| `52.204.199.125:443` | `node` (pid 3911129) | Claude Code Node 컴포넌트 (AWS likely) |

→ **모든 9개 = Ollama 무관**. brief §8.1 "측정 중 외부 egress 0" 검증 = Ollama 한정 충족.

### 3c.4 🔴 R-23 finding (측정 환경 동결, actionable)

본 baseline 시점 활성 Claude Code 인스턴스 ≥ **3개**(pid 3999024 본 세션·3912298·2803969). brief §4.6 R-23 = **"백그라운드 Claude Code 세션 0"** → **§4 측정 진입 *전* 다른 Claude Code 세션 종료 의무**(사용자 책임). tailscaled = GPU/CPU 영향 ↓ 가능, 동결 불필요 판단. sshd inbound = 동결 불필요.

### 3c.5 텔레메트리 환경변수 (식별 한정, export 0)

brief §8.1 명시: Ollama 0.20.4 가 `OLLAMA_NOHISTORY` / `OLLAMA_NO_ANALYTICS` 실제 인식 여부 **미확정** (Agent A 정직성).

| 변수 | 목적(외부 문서) | v0.20.4 인식 |
|---|---|---|
| `OLLAMA_NOHISTORY` | history 비활성 | 미확정 |
| `OLLAMA_NO_ANALYTICS` | analytics 비활성 | 미확정 |
| `OLLAMA_NOPRUNE` | blob prune 비활성 | 확정 (egress 직접 X) |
| `OLLAMA_HOST` | 바인딩 주소 | 확정 (egress X·M6 관련) |
| `OLLAMA_ORIGINS` | CORS origin | 확정 (egress X) |

**현재 export 0** (delangi shell `OLLAMA_*` unset, Stage 1 §2 Step 5). **데몬 자체 환경** (`/proc/3375/environ`) = root 권한 미점검. **측정 진입 권고**: fresh subshell(R-34) 에서 `OLLAMA_NOHISTORY=1` + `OLLAMA_NO_ANALYTICS=1` export 시도 → 데몬 로그·동작 변경 관찰로 인식 검증. **영구 설정 ❌**(`.bashrc`·`.profile` 변경 0건).

### 3c.6 한계 (R-3·R-11b 답습)

- 본 baseline = **단일 snapshot**. 측정 *중* polling(30s)·측정 *직후*·5분 후 lazy upload 재점검 = 미적용 (별도 cycle R-11b).
- Ollama 자체 update check / 텔레메트리 lazy upload = 본 snapshot 미커버.
- 출처 미상 Ollama(R-1) → 표준 빌드와 동일한 egress 정책 적용 미확정. silent 교체는 측정 *후* sha256sum 재기록으로만 감지.
- 외부 IP 9개 reverse DNS = DNS query egress 발생 → **본 진입 R-11 답습 0건**. IP 정체 = process 식별로 추정.

---

## 3d. §4 V1-3 — tok/s 측정 (raw 보고 only, R-6 답습)

### 3d.1 측정 조건

- temperature 0.0, stop=[], seed=42, num_predict=512(decode)/16(prefill)
- decode prompt 입력 토큰 ~161/182 (model tokenizer 차이)
- prefill 2k = decode prompt × 13 → 2009/2030 토큰 (목표 2048, ±10% 안)
- prefill 8k = decode prompt × 51 → 7823/7844 토큰 (목표 8192, ±10% 안)
- R-23 충족: 측정 중 본 세션 단일 Claude (3999024) 외 0
- R-1 hash: 측정 *직전* + *직후* `ce95c475...878b10` (Stage 1 일치, **silent 교체 미발생**)

### 3d.2 핵심 결과 표 (raw, PASS/FAIL framing X)

| 모델 | scenario | mean tok/s | std | std/mean | p50 | p95 | 비고 |
|---|---|---:|---:|---:|---:|---:|---|
| qwen3-coder-next (MoE 79.7B+SSM, Q4) | decode (5회) | **7.83** | 0.36 | 4.6% | 7.99 | 8.02 | run #1 outlier 경계(2σ) |
| qwen3-coder-next | prefill 2k cold (precheck) | 66.46 | — | — | — | — | KV cache empty |
| qwen3-coder-next | prefill 2k warm (5회) | 91.58 | 2.91 | 3.2% | 91.84 | 94.15 | 부분 cache(24초 prefill 잔존) |
| qwen3-coder-next | prefill 8k cold (precheck) | 57.79 | — | — | — | — | 135초 prefill |
| qwen3-coder-next | prefill 8k warm (5회) | 291.55 | 5.76 | 2.0% | 291.50 | 295.42 | 부분 cache |
| qwen2.5-coder:32b (dense Q4) | decode (5회) | **4.62** | 0.18 | 4.0% | 4.53 | 4.53 | run #5 outlier 경계 |
| qwen2.5-coder:32b | prefill 2k cold (precheck) | 13.19 | — | — | — | — | 154초 prefill |
| qwen2.5-coder:32b | prefill 2k warm (5회) | **~8290** | 996 | 12.0% | 8252 | 8268 | 🔴 **거의 완전 cache hit** |
| qwen2.5-coder:32b | prefill 8k cold (precheck) | 11.75 | — | — | — | — | 667초 prefill, quadratic |
| qwen2.5-coder:32b | prefill 8k warm (5회) | **~27465** | 1731 | 6.3% | 26885 | 28504 | 🔴 cache hit lookup only |

### 3d.3 비교 관찰 (raw 보고, R-18 답습)

| 비교 | qwen3-coder-next | qwen2.5-coder:32b | ratio | 해석 (R-6/R-18 답습) |
|---|---:|---:|---:|---|
| decode (memory-bound) | 7.83 | 4.62 | MoE/dense = **1.70×** | R-18 ≥2× threshold *미달*, "병목 가설과 *모순 안 함*" 까지만, "MoE 우위 PASS" 표현 X |
| prefill cold 2k (compute) | 66.46 | 13.19 | MoE/dense = **5.04×** | sparse activation 효과 명백, 단 SSM cold 동작 검증 별도 |
| prefill cold 8k (compute) | 57.79 | 11.75 | MoE/dense = **4.92×** | 일관, dense attention quadratic 부담 매우 큼 |
| prefill warm cache hit 2k | 91.58 | 8290.93 | dense/MoE = **90.5×** | 🔴 의외 역전 |
| prefill warm cache hit 8k | 291.55 | 27465.21 | dense/MoE = **94.2×** | 🔴 의외 역전 |

### 3d.4 🔴 결정적 발견 — prefix cache 영역 dense ≫ MoE+SSM (~90×)

prefill warm 5회 측정에서 dense(qwen2.5-coder:32b)가 MoE+SSM(qwen3-coder-next)보다 ~90×배 빠름. 가설(검증 별도):
- **SSM state 는 KV cache lookup 만으로 재사용 불가** — 매 호출 partial recomputation 필요 (state space 의 transition 재계산)
- 또는 **Ollama 0.20.4 의 SSM prefix cache 최적화 미완성**
- 또는 SSM 의 *전체* prefix 가 *부분적*으로만 cache 가능

⚠️ **production 동일 prefix 반복 query 시**: dense ≫ MoE+SSM (역전). brief v2 §6 "MoE = 코딩 작업 다회 호출 시 우위" 가설 *부분* 도전. **M3 결정 입력 별도 합의** 필수.

단 *cold prefill* (compute-bound 영역) 에서는 MoE 5× 우위 유지 — 모델 첫 로드 후 신규 prompt 처리 시 sparse activation 효과 명백.

### 3d.5 roofline / 외부 실측 비교 (참조 only, 해석 X)

- brief v2 §6 R5 roofline: A3B Q4 ~**90–120** tok/s decode 가정 → 실측 7.83 = **~7-9%**
- 합의 R4 외부 실측: llama.cpp Qwen3-Coder-30B-A3B ~**31** tok/s → 본 측정 ~**25%**
- 가설 (검증 별도):
  - qwen3-coder-next 활성 파라미터가 ~3B 가정 *초과* (top-10/512 + SSM state)
  - GB10 unified memory 273GB/s 병목 + SSM state recomputation 합쳐 메모리 압박
  - Ollama 0.20.4 의 hybrid SSM+MoE 구현 효율성 (vs llama.cpp)

### 3d.6 측정 직후 baseline

- `/api/ps`: qwen2.5-coder:32b VRAM 잔존(30.7GB), qwen3-coder-next size_vram=0 swap-out
- `/api/version`: 0.20.4 정상
- LISTEN: `127.0.0.1:11434` only (M6 유지)
- ESTABLISHED 외부: Anthropic API/Tailscale/SSH only — **Ollama 외부 연결 0건 유지**
- pmon: GPU idle (모델 로드된 상태에서도 호출 0이라 활성 0%)
- claude 인스턴스: 본 세션 only (R-23 유지)

### 3d.7 R-6/B-F8 정직성 답습

- PASS/FAIL framing 사용 0건
- "≥15 PASS 후보" 등 anchor 표현 0건
- raw 모두 보고 (5회 + outlier 경계 명시)
- M3·M4 결정 입력 자격 = 본 findings 의 어떤 행에도 X
- 결정 *고정* 은 V-1 findings *후 별도 합의*

---

## 3e. Stage 5 — M3·M4 합의 Phase 1 cycle (A-진단 + C-c)

### 3e.1 R-1 anchor 5회 일치 + R-23 freeze 유지

- Stage 1 = Stage 4 pre = Stage 4 post = Phase 1 pre = Phase 1 post = `ce95c475...878b10` ✅
- 5회 sudo 사용자 명시 prompt 입력, read-only. silent 교체 미발생 *최종* 확정.

### 3e.2 A-진단 결과 — nvidia-smi GB10 한계 확인

| 항목 | 결과 |
|---|---|
| 명령 | `nvidia-smi dmon -s pum -d 1 -c 100` 백그라운드 + qwen3-coder-next decode 1회 동시 |
| decode 결과 | mean **7.93 tok/s** (Stage 4 평균 7.83 와 일치, 재현성 확인) |
| dmon 100 samples sm% | **0% 모두** |
| dmon 100 samples mem% | **0% 모두** |
| dmon power | **4W** (거의 idle 보고) |

🔴 **결론**: nvidia-smi dmon 이 GB10 unified memory 환경에서 GPU activity 보고 *완전 불가*. Stage 1 §2 Step 3 pmon idle 결과 동일 한계 재확인 (brief R-25 NOTE 답습).

**F1 가설 (v) 영향**: "GB10/Ollama effective BW 자체가 spec 의 1/3" 가설 → **nvidia-smi 직접 측정 불가**. *역산* (dense 4.62 × 18.5GB ≈ 85GB/s = 273GB/s 의 31%) 만이 가능한 evidence. 직접 측정 = NVBandwidth/tegrastats/Nsight Systems 등 별도 cycle (Phase 3+).

### 3e.3 C-c cache miss 분리 — F2 가설 직접 답

`prefill 8k` × 3회, 매 회 다른 nonce(timestamp+random) 를 prompt prefix 시작에 추가 → prefix cache lookup 강제 miss.

| run | nonce | prefill tok/s | prefill duration | prompt tokens |
|---|---|---:|---:|---:|
| 1 | 1779544042526946854-18716 | 58.51 | 134254ms | 7855 |
| 2 | 1779544179052105015-16349 | 57.89 | 135693ms | 7855 |
| 3 | 1779544317110123102-2768 | 58.42 | 134433ms | 7854 |
| **mean** | — | **58.27** | 134793ms | 7855 |
| **std** | — | **0.27** | — | — |
| **std/mean** | — | **0.47%** | — | — |

### 3e.4 ⭐ 결정적 비교 (cache miss vs cache hit)

| scenario | prefill tok/s | prefill duration | 비고 |
|---|---:|---:|---|
| Stage 4 precheck (cache miss 1회) | 57.79 | 135367ms | 7823 tokens (nonce 없음) |
| **Stage 5 C-c unique 3회 mean** | **58.27** | 134793ms | 7855 tokens (nonce 추가) — **Stage 4 precheck 와 0.8% 일치** |
| Stage 4 warm 5회 (cache hit) | 291.55 | 26852ms | 7823 tokens |
| **cache hit / cache miss ratio** | **5.01×** | — | — |

✅ **Stage 4 precheck (57.79) = 정직한 cache miss 측정 확정** (우연 아닌 정확한 cold prefill, C-c 3회 mean 58.27 와 일치).

### 3e.5 🎯 F2 가설 직접 답 (cache 역전 원인)

| 가설 | 검증 결과 |
|---|---|
| **H-B1 (SSM state 가 KV cache lookup 만으로 재사용 불가)** | ✅ **강한 evidence** — cache hit 시점에도 27초 prefill 잔존 = SSM state recomputation 의 본질적 cost |
| **H-B3 (attention 12/48 cache hit + SSM 36/48 dominant compute)** | ✅ **정성적 일치** — warm 27000ms / cold 134800ms = **20.0%** vs attention layer 비율 12/48 = **25.0%** (오차 5%p, 정성적 강한 매칭) |
| **H-B2 (Ollama SSM 구현 최적화 미완성)** | △ **H-B1 과 분리 불가** — llama.cpp 동일 측정 필요 (Phase 3 C-e) |

### 3e.6 production 영향 재평가

MVP-1 advisory 패턴 = boss 동일 system prompt + 변경 worker output. **cache hit ratio = system_prompt_tokens / total_tokens**. SSM 부분은 *전체 cache miss* 가능성(H-B1 강한 신호) → cache hit 의 *부분 효과* 만 활용 가능.

→ **MVP-1 트랙 B 진입 *전* advisory 패턴 wall-clock 측정 필수** (합의 R-12 답습).

### 3e.7 Phase 1 완료 상태

| 항목 | 상태 |
|---|---|
| A-진단 | ✅ 완료 — nvidia-smi GB10 한계 확인 (정밀 도구 별도 cycle 권고) |
| C-c (qwen3-coder-next) | ✅ 완료 — F2 가설 H-B1·H-B3 강한 evidence |
| qwen2.5-coder cache miss | ❌ 본 Phase 1 미수행 (cold prefill 8k 667초 × 3 = 33분 과대) — 별도 cycle |
| 데몬 변경 / pull / 빌드 | 0건 |

### 3e.8 결정 입력 자격

- **F2 (cache 역전)**: 🎯 본질적 SSM 한계 강한 evidence — M3 결정 시 *MVP-1 advisory wall-clock 평가 필수* 명문 의무 (합의 R-12 답습)
- **F1 (roofline 미달)**: ❌ 미해소 — Phase 2 (C-a 활성 파라미터 HF egress) + Phase 3 (C-e llama.cpp) 필수
- **M3 결정 고정 자격**: Phase 1 단독 미충족 — Phase 2/3 진행 후 *재합의*
- **M4 결정 고정 자격**: M4-A (연기) 답습 유지. M4-D (wall-clock UX metric) 권고 강도 ↑

---

## 4. 정직성 한계 (entry brief §0.2 + Reviewer 권한 한계 답습)

1. **측정 0건** — tok/s/decode/prefill/메모리 점유/SM 활용 결과 = 전부 *부재*. 본 findings 어떤 행도 "성능 PASS" 결론 도출 자격 X.
2. **활성 파라미터 정량 미확인** — manifest 필드만으로 *활성* 파라미터 정확 계산 불가. 모델 카드 또는 측정 후 `prompt_eval_count`·`eval_count` 역추론 필요.
3. **출처 미상 Ollama anchor** — §1.2 한계 동일. 본 hash = 현 시점 식별값, 표준 빌드 재현성 검증 0.
4. **데몬 환경 미확인** — root `/proc/3375/environ` 미점검. 데몬 *내부* 설정(예: `OLLAMA_HOST`·`OLLAMA_MODELS`)이 delangi shell env 와 다를 가능성 잔존.
5. **다른 4 모델 dense 검증 = manifest 한정** (Stage 2 완료). `moe_fields = {}` empty 확인. 실 dense 실행은 측정 후 검증.
6. **hybrid SSM 발견은 *manifest 해석* 수준** — Ollama 0.20.4 가 실제로 SSM 레이어를 정상 실행하는지 (혹은 placeholder 인지) = 측정 후 검증.
7. **Capabilities `tools` 보고는 *능력* 선언일 뿐** — 실제 endpoint 거부/수용 동작 = §5 Step 4 측정에서 확인.
8. **Ollama Hub 실재성 미검증** (Stage 2) — `ollama search` egress = 별도 cycle. 11종 404 = *시도한 해당 tag* 부재일 뿐, 다른 tag 형식의 Hub 실재 가능성 잔존.
9. **Step 2a 활성 파라미터 추정은 외부 의존** — 본 환경 검증 0, Reviewer 정직성 노트 §6 답습.
10. **egress baseline = 단일 snapshot** (Stage 3) — 측정 중·후 polling / lazy upload 재점검 = 별도 cycle. 본 baseline 의 "Ollama egress 0" 결론 = *해당 snapshot 시점 한정*.
11. **텔레메트리 변수 인식 미확정** (Stage 3) — 5종 식별만, export·검증 0. 본 측정에서 export 0건 (R-34 fresh subshell 미사용 — 클라이언트측 export 는 데몬 동작 영향 X).
12. **데몬 자체 환경 미점검** (Stage 1·3 공통) — `/proc/3375/environ` root 권한 미접근. 데몬 *내부* OLLAMA_* 설정 = delangi shell env 와 다를 가능성 잔존.
13. **🔴 prefix cache hit 효과 우세** (Stage 4) — prefill warm 5회 = cache lookup 영역. *실 compute prefill* 성능 = precheck (cold) 만 정확. R-9 5회 power 보장은 cache miss 영역에서 의미, cache hit 영역에선 noise 분포 측정.
14. **활성 파라미터 정량 미확인** (Stage 1·4 공통) — qwen3-coder-next decode 7.83 tok/s 가 roofline ~90-120 가정 7-9% 수준 → 활성 ~3B 가정 위배 신호. 활성 파라미터 정확 산정 = 모델 카드 또는 별도 cycle.
15. **SSM 실 동작 검증 0** (Stage 4) — qwen3next hybrid SSM 의 실제 SSM 레이어 동작 정상성 = 응답 한국어 출력 가능 정도까지만, golden output·numerical correctness 검증 별도.
16. **cache 동작 SSM vs dense 차이 = manifest/measurement 해석 수준** (Stage 4 §3d.4) — SSM state 가 KV cache 와 다른 동작 = 가설, Ollama 0.20.4 SSM cache 구현 inspection 별도 필요.
17. **5회 = 통계 power 한정** — environment noise (다른 process tail latency, IO 부하 등) 완전 제거 불가. brief §4.6 동결 *최선 효과* 적용해도 단일 세션 한계.

---

## 5. 다음 단계 권고 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 발생 |
|---|---|---|
| ~~(A)~~ | ~~§3 Step 2a/2b~~ — **Stage 2 완료** | — |
| ~~(B)~~ | ~~§8 egress baseline~~ — **Stage 3 완료** | — |
| ~~(C)~~ | ~~§4 측정 진입~~ — **Stage 4 완료** (qwen3-coder-next + qwen2.5-coder:32b 각 decode + prefill 2k/8k 5회) | — |
| **(D)** | **M3·M4 결정 합의** (별도 cycle) — raw 입력하여 풀 3+1 또는 단축 합의. ⭐ 본 findings cache hit 발견 등 *해석* 단계 | 비측정, 합의 작성 |
| **(E)** | cache miss 영역 분리 측정 (별도 cycle) — unique prompt seed 또는 prefix 변형으로 cache 영향 분리 | LLM 호출 발생, 별도 승인 |
| **(F)** | SSM golden output 검증 (별도 cycle) — 응답 정확성 검증 | LLM 호출 + 외부 reference 필요 |
| **(G)** | gap-pull entry brief — Qwen3.5-A3B-Instruct (활성 ~3B) 비교 측정 후보 | 디스크 ↑, egress, 별도 명시 승인 |
| **(H)** | llama.cpp 비교 측정 — brief §7-B/C | 빌드 발생, 별도 명시 승인 |
| **(I)** | §12 옵션 E 출처 미상 Ollama 위생 정정 | 보안 거버넌스 재개=비례성 평가 |
| **(J)** | **본 findings 확정 commit + push** → 세션 종료 | 머신 변경 0 |

### 5.1 Reviewer 권한 한계 (entry brief §6 답습)

- 본 findings = **read-only 단계 raw 보고**. M3·M4 결정 *고정* 0.
- 본 findings 가 §4 측정 진입을 *권고* 하더라도 = 별도 명시 승인 단계.
- silent 교체 평가 = 본 단계 권한 밖. 측정 *후* 재기록 + (E) 옵션이 결합되어야 의미.

---

## 6. raw 보존 (entry brief §4.5)

| 항목 | 경로 |
|---|---|
| Stage 1: 환경 ID + V1-1 5 steps + R-1 + V1-2 Step 1 핵심 | `docs/phase0/v1-poc-raw/2026-05-23T11-53-v1-1-readonly.json` |
| Stage 1: qwen3-coder-next full manifest | `docs/phase0/v1-poc-raw/2026-05-23T11-53-qwen3-coder-next-manifest.json` (82645 bytes) |
| Stage 2: 인벤토리 재확인 + dense 4 검증 + Step 2b 11종 404 + Step 2a 후보표 | `docs/phase0/v1-poc-raw/2026-05-23T12-15-v1-2-step2-readonly.json` |
| Stage 3: §8 egress baseline (ESTABLISHED 외부 9 + Ollama 0 + R-23 활성 process + 텔레메트리 변수 식별) | `docs/phase0/v1-poc-raw/2026-05-23T13-00-v1-egress-baseline-readonly.json` |
| Stage 4: §4 V1-3 측정 종합 (R-1 anchor 3회·R-23 freeze·decode·prefill 2k/8k cold·warm 각 5회 × 2모델 + 비교 + caveat) | `docs/phase0/v1-poc-raw/2026-05-23T21-30-v1-3-measurement-summary.json` + 측정 raw 30 JSON (`2026-05-23T13-{1..5}-qwen3cnext-decode.json` + `2026-05-23T21-{1..5}-qwen{3cnext,25coder}-{decode,prefill2k,prefill8k}.json`) |

raw 미보존 측정 = findings 입력 자격 X (entry brief §4.5 정직성 SOP, B-F13 답습).

---

**출처**: entry brief v1.1 (HEAD `9e68fbb`) / brief v2 §6 / 합의 R-1~R-39 / raw 2 파일.

**답습**: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow`.

**금지 (영구 답습, 본 findings 0건)**: 측정 실행 / 설치 / sudo (R-1 1회 사용자 명시 외) / 모델 pull / 데몬 변경 / M3/M4 결정 고정 / commit (별도 단계) / push (별도 단계) / 합의 본문 자동 정정 / 보안 거버넌스 자동 재개.
