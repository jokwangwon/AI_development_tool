# 자비스 MVP-1 V-1 PoC findings (DRAFT — Stage 1: read-only)

> **본 findings = V-1 PoC의 *1차 단계*(R-1 anchor + §2 V1-1 + §3 V1-2 Step 1) read-only 결과 한정.** tok/s 측정·gap-pull·llama.cpp 빌드·M3/M4 결정 = **0건** (별도 명시 승인 단계).

**작성일**: 2026-05-23
**Status**: DRAFT — Stage 1/N (read-only 위생 점검 + manifest 검증)
**선행 답습**: `jarvis-mvp1-v1-poc-entry-brief.md`(v1.1, HEAD `9e68fbb`, BLOCKING 6 반영) / `3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md` / brief v2 §6
**raw**: `docs/phase0/v1-poc-raw/2026-05-23T11-53-v1-1-readonly.json` + `2026-05-23T11-53-qwen3-coder-next-manifest.json`

---

## 0. 본 findings 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. R-1 anchor 식별값 기록 (측정 *전* baseline, §1)
2. §2 V1-1 5 steps read-only 결과 정리 (§2)
3. §3 V1-2 Step 1 `qwen3-coder-next` manifest 해석 (§3)
4. 정직성 한계 명시 (§4)
5. 다음 단계 권고 (§5)

### 하지 않는 것 (entry brief §0.2 영구 답습)

- ❌ tok/s 측정 (decode·prefill 0건)
- ❌ 모델 pull / 빌드 / install
- ❌ M3 / M4 결정 *고정* — 본 findings 는 raw 보고만, 결정 입력 자격 X (entry brief §4.4 답습)
- ❌ Ollama 데몬 재시작 / kill / signal / 설정 변경
- ❌ §3 Step 2a/2b (후보 5~7종 식별·실재 검증) — 본 findings 단계 0건
- ❌ §8 egress baseline — 본 findings 단계 0건
- ❌ commit·push (별도 명시 승인)

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

## 4. 정직성 한계 (entry brief §0.2 + Reviewer 권한 한계 답습)

1. **측정 0건** — tok/s/decode/prefill/메모리 점유/SM 활용 결과 = 전부 *부재*. 본 findings 어떤 행도 "성능 PASS" 결론 도출 자격 X.
2. **활성 파라미터 정량 미확인** — manifest 필드만으로 *활성* 파라미터 정확 계산 불가. 모델 카드 또는 측정 후 `prompt_eval_count`·`eval_count` 역추론 필요.
3. **출처 미상 Ollama anchor** — §1.2 한계 동일. 본 hash = 현 시점 식별값, 표준 빌드 재현성 검증 0.
4. **데몬 환경 미확인** — root `/proc/3375/environ` 미점검. 데몬 *내부* 설정(예: `OLLAMA_HOST`·`OLLAMA_MODELS`)이 delangi shell env 와 다를 가능성 잔존.
5. **다른 4 모델 manifest 미검증** — `qwen2.5-coder:32b` / `llama3.3:70b` / `exaone3.5:32b` / `exaone4:32b` = dense 가정 유지 (entry brief §1.3). 정밀 확인은 V1-2 Step 2a/2b 단계.
6. **hybrid SSM 발견은 *manifest 해석* 수준** — Ollama 0.20.4 가 실제로 SSM 레이어를 정상 실행하는지 (혹은 placeholder 인지) = 측정 후 검증.
7. **Capabilities `tools` 보고는 *능력* 선언일 뿐** — 실제 endpoint 거부/수용 동작 = §5 Step 4 측정에서 확인.

---

## 5. 다음 단계 권고 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(A)** | **§3 Step 2a/2b** 진행 — 후보 5~7종 식별 + 기존 4 모델 `/api/show` 검증 (localhost·read-only). `ollama search` 제외 (egress) | 추가 변경 0, raw 보존 |
| **(B)** | **§8 egress baseline** 점검 (read-only) — 측정 진입 *전* baseline 확보 | 추가 변경 0, raw 보존 |
| **(C)** | **§4 측정 진입** (qwen3-coder-next 단일) — decode 5회 + prefill 2k 5회 + prefill 8k 5회. R-1 hash 재기록 + §4.6 환경 동결 의무 | **LLM 호출 발생, GPU 사용, ~분 단위 시간, sudo 0 가능, 별도 명시 승인 필수** |
| **(D)** | **본 findings 확정 commit + push** → 다음 세션 §4 진입 | 머신 변경 0 |
| **(E)** | §12 옵션 E — 출처 미상 Ollama 위생 정정 trigger 검토 (별도 cycle, R-1 한계 정정) | 보안 거버넌스 재개 = 비례성 평가 필요 |

### 5.1 Reviewer 권한 한계 (entry brief §6 답습)

- 본 findings = **read-only 단계 raw 보고**. M3·M4 결정 *고정* 0.
- 본 findings 가 §4 측정 진입을 *권고* 하더라도 = 별도 명시 승인 단계.
- silent 교체 평가 = 본 단계 권한 밖. 측정 *후* 재기록 + (E) 옵션이 결합되어야 의미.

---

## 6. raw 보존 (entry brief §4.5)

| 항목 | 경로 |
|---|---|
| 환경 ID + V1-1 5 steps + R-1 + V1-2 Step 1 핵심 | `docs/phase0/v1-poc-raw/2026-05-23T11-53-v1-1-readonly.json` |
| qwen3-coder-next full manifest | `docs/phase0/v1-poc-raw/2026-05-23T11-53-qwen3-coder-next-manifest.json` (82645 bytes) |

raw 미보존 측정 = findings 입력 자격 X (entry brief §4.5 정직성 SOP, B-F13 답습).

---

**출처**: entry brief v1.1 (HEAD `9e68fbb`) / brief v2 §6 / 합의 R-1~R-39 / raw 2 파일.

**답습**: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow`.

**금지 (영구 답습, 본 findings 0건)**: 측정 실행 / 설치 / sudo (R-1 1회 사용자 명시 외) / 모델 pull / 데몬 변경 / M3/M4 결정 고정 / commit (별도 단계) / push (별도 단계) / 합의 본문 자동 정정 / 보안 거버넌스 자동 재개.
