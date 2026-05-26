# 자비스 MVP-1 V-1 PoC 운영 entry brief (DRAFT v1.1)

> **본 brief = V-1(MVP-1 로컬 사장 선결 검증) 운영화 한정.** 본 brief 의 어떤 §도 그 자체로 **새 패키지 설치·sudo·systemd 변경·신규 모델 pull·tok/s 측정 *실행*·OllamaBoss 코드 작성·config 변경** 을 발생시키지 않는다. 실 변경 0건. 본 brief = **(i) 사실 식별** + **(ii) V1-1~V1-5 *실행 절차/명령/성공기준/롤백* 운영화** + **(iii) M3·M4 결정 매트릭스 *권고*(고정 아님)** — staged cycle: `brief → 사용자 승인 → 3+1 합의 → brief v1.1 → 사용자 검토 → 측정 실행(별도 명시 승인) → findings → commit → push`.

---

**작성일**: 2026-05-23
**Status**: **DRAFT v1.1** (v1 + 3+1 합의 `3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md` R-1 ~ R-6 BLOCKING 6 + 권고 14 반영. NOTE 17건은 부록 B carryover. 실 측정·설치·코드 0건)
**진입 단위**: MVP-1 트랙 B 선결 — **V-1 PoC 운영 entry**. `jarvis-mvp1-local-boss-design-brief.md` (v2 §6) 합의 후 *실행 절차 구체화* 단계
**선행 답습**: brief v2 §6 V1-1~V1-5 (설계 동결, 본 brief 운영화 한정) · `3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` R4 / R5 / R11 (llama.cpp ↔ Ollama 동급, tok/s roofline·실측, egress 추론시점 한정) · **`3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md` R-1 ~ R-6 BLOCKING + 권고 14 (v1 → v1.1 보강)** · `jarvis-safety-layer-poc-findings.md` (V-1 *미*착수 — 본 brief 환경 확인에서 *부분* 정정, §1.2)
**답습 권위 한계**: 본 brief = *실행 절차 entry brief* DRAFT — M3(런타임 결정 고정)·M4(tok/s threshold 고정)·OllamaBoss 코드·setup 변경은 별도 단계(findings 후 합의 + 사용자 명시).

## v1 → v1.1 변경 이력 (3+1 합의 R-1 ~ R-23 반영)

| R-# | 항목 | 반영 위치 |
|----|----|----|
| **R-1** 🔴 | 출처 미상 Ollama silent 교체 위험 명문화 + sha256sum 의무 + §0.2 데몬 재시작/kill 금지 추가 | §0.2, §1.2 |
| **R-2** 🔴 | §2.3 실패 분기 4 추가 (데몬 죽음 / 11434 점유 / GPU OOM CPU fallback / 비정상 응답) + §5.2 `eval_count` 우회 | §2.3, §5.2 |
| **R-3** 🔴 | §8.1 끝 "측정 세션 한정" 명문 | §8.1 |
| **R-4** 🔴 | §4.2 Step 2·4 prefill 입력 토큰 사전 (`/api/tokenize`) + 사후 (`prompt_eval_count`) 검증 | §4.2 Step 2·4 |
| **R-5** 🔴 | §3.2 Step 2 → 2a (후보 5~7종 확장) + 2b (실재 검증 `/api/library`·`ollama search`) 분리 | §3.2 Step 2 |
| **R-6** 🔴 | §4.4 전면 재작성 — "성공기준" → "보고 항목". PASS/FAIL·"≥15 PASS 후보" 삭제. raw (mean·std·p50·p95) | §4.4 |
| R-7 ~ R-19, R-22, R-23 🟡 | 권고 14건 (M3 framing·temperature·outlier·pmon fallback·raw 보존·환경 동결 등) | 본문 다수 |
| R-20 ~ R-39 🟢 | NOTE 17건 carryover | 부록 B |

---

## 0. 범위

### 0.1 사용자 진입 명령 답습 (2026-05-23)

> "트랙 B + V-1 PoC 진행. Ollama·llama.cpp 둘 다 MoE tok/s 실측(R4) → OllamaBoss 실 endpoint(httpx). 설치 발생, 별도 승인 필요. 단계별 합의 cycle 패턴 답습."

본 brief = 위 명령의 *진입 step* — **V-1 PoC 실행 절차 운영화** 한정. brief 자체는 측정·설치·코드 0건.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**:
  1. 환경 사실 결과 (Ollama 기구동·5 모델 pre-pulled 발견 보고, §1)
  2. V1-1~V1-5 각각의 *실행 절차*(명령·산출물·성공기준·실패 분기) 정의 (§2~§6)
  3. llama.cpp 비교 측정 절차 (§7, R4 답습)
  4. 텔레메트리/egress 위생 점검 절차 (§8, R11)
  5. M3 (llama.cpp ↔ Ollama) 결정 매트릭스 *권고* (§9 — *고정 금지*)
  6. 환경 보존형 롤백 정책 (§10 — 기존 설치 *제거 0*, 추가분만 reversible)
- **하지 않는 것 (사용자 명시 영구 답습)**:
  - ❌ 신규 패키지 *설치 실행* (apt/snap/pip/npm/curl|sh)
  - ❌ sudo / systemd unit 작성·활성
  - ❌ 신규 모델 pull *실행* (gap-pull 후보 식별만, 실행은 별도 승인)
  - ❌ tok/s 측정 *실행* (`ollama run`·`curl /api/generate`)
  - ❌ `OllamaBoss` *코드* 작성 (트랙 B 구현 = V-1 후)
  - ❌ config 변경 (`OLLAMA_HOST`·`OLLAMA_MODELS` 등 환경변수 영구 설정)
  - ❌ M3 / M4 결정 *고정*
  - ❌ 기존 Ollama 설치 *제거* / *재설치* / 권한 변경
  - ❌ **기존 Ollama 데몬 *재시작* / kill / signal** (R-1: 데몬 상태 보존, 위생 정정 trigger 는 별도 단계 §12 옵션 E)
  - ❌ 외부 네트워크 변경·firewall 룰
  - ❌ commit / push / 합의 보고서 작성

---

## 1. 환경 사실 (read-only 점검 결과, 2026-05-23)

### 1.1 하드웨어 / 토클체인

| 항목 | 확인값 | 함의 |
|----|----|----|
| GPU | **NVIDIA GB10** (driver 580.159.03) — `nvidia-smi --query-gpu=memory.total` = `[N/A]` (GB10 = Grace+Blackwell SoC unified memory, dGPU 보고 경로 미적용) | V1-5 측정 시 `nvidia-smi` 메모리 보고 *불완전* 전제. unified memory 실측은 `/proc/meminfo` + `nvidia-smi pmon` 병행 |
| 아키텍처 | **aarch64** (Ubuntu 24.04, kernel 6.17.0-1018-nvidia) | sm_120/121, vLLM 비채택 (brief v2 M3 답습) |
| CUDA | **CUDA 13.0** toolkit(`nvcc`) 설치됨 | llama.cpp source build 시 의존 충족 |
| 디스크 | `~` 마운트 `/dev/nvme0n1p2` **1.9T (333G 가용, 82% 사용 중)** | gap-pull 모델 ≤ 100GB 안전 (운영 여유 200GB 보존 가정) |

### 1.2 ⭐ Ollama 기설치 발견 (brief v2 "V-1 미착수" 부분 정정)

| 항목 | 확인값 | 함의 |
|----|----|----|
| **Ollama 데몬** | **이미 구동** — PID 3375, `ollama serve`, version `0.20.4`, **`127.0.0.1:11434` localhost 바인딩** | V1-1 (설치·구동) **부분 완료**. M6 (localhost 한정) **우연 충족** |
| 바이너리 경로 | `pgrep`이 `/bin/ollama serve` 보고 — 현재 `stat /bin/ollama` 실패 (실행 중 inode만 잔존, 파일 시스템에서 삭제·이동된 듯). `dpkg -S` 미매칭 | **설치 출처 미상**. 위생 위험 노트. 본 brief 는 정정 *제안 0건* (사용자 결정) |
| systemd unit | `ollama.service` 부재 | 데몬은 다른 경로로 기동 (재부팅 시 자동 시작 *미보장*). 본 brief 범위 밖 |
| pre-pulled 모델 | 5종, 총 ~167GB (2026-04-09 timestamp) | 아래 §1.3 |
| 외부 노출 | **없음** (ss -tlnp 결과 `127.0.0.1:11434`만 LISTEN, 0.0.0.0 미바인딩) | R11 (추론시점 egress 0) 입력 충족 |

> **🔴 R-1 정직성 NOTE (Reviewer 권위 BLOCKING 격상)**: 출처 미상 Ollama 데몬을 V-1 *측정 대상* 으로 사용하는 결정은 다음 두 정직성 한계를 갖는다 — (i) **측정값이 표준 빌드 대비 재현 가능한지 별도 검증 불가** (binary origin 미상 → 다른 환경에서 동일 환경 구성 불가능), (ii) **silent 자동 업데이트 / origin 교체 위험 미평가** (`/bin/ollama` 가 실행 중 inode 만 잔존 = 누군가/무언가가 사후 제거 — 자기 은폐 행동의 약한 신호 또는 race condition 부산물). V-1 findings 결론이 'PASS' 라도 이 한계는 **트랙 B 구현 진입 *전* 별도 검토 필수** (§12 옵션 E).
>
> **R-1 의무 절차** (측정 단계 entry 한정, 본 brief 외): 측정 *전* 1회 `sha256sum /proc/<pid>/exe` 식별값 기록 → V-1 findings 에 첨부. 측정 *후* 재기록 → 동일 hash 확인 (silent 교체 감지). 본 brief = 절차 *식별* 만, 실행 0.

### 1.3 기존 모델 인벤토리

| 모델 | 크기 | quant | family | dense/MoE | A3B 적합? |
|----|----|----|----|----|----|
| `llama3.3:70b` | 42.5GB | Q4_K_M | llama | dense | ❌ (273GB/s 병목, brief v2 §6: dense 70B Q4 = 한자릿수 tok/s) |
| `qwen2.5-coder:32b` | 19.9GB | Q4_K_M | qwen2 | dense | ❌ (dense 32B) |
| **`qwen3-coder-next:latest`** | **51.7GB** | Q4_K_M | qwen3next | **요확인** (79.7B parameter, family `qwen3next` = potentially MoE) | **요확인** (V1-2 첫 단계 = manifest 검증) |
| `exaone3.5:32b` | 19.3GB | Q4_K_M | exaone | dense | ❌ |
| `exaone4:32b` | 34GB | Q8_0 | exaone4 | dense | ❌ |

**현황 요약**: dense 4종 + MoE 가능성 1종(qwen3-coder-next 검증 필요). brief v2 §6 1차 후보 **Qwen3.x-A3B / A10B**(MoE 활성 ~3B/~10B)와 정확히 일치하는 모델 *부재* — V1-2 = manifest 검증 → 필요 시 **gap-pull**(별도 승인).

---

## 2. V1-1 운영 절차 — 설치·구동 *확인* (설치 *실행 0*)

### 2.1 목표 (재정의)

brief v2 §6: "Ollama 설치·구동 (aarch64/CUDA13/sm_121)" → §1.2 발견으로 **설치는 스킵, 구동 *위생 점검* + GPU 인식 검증** 로 재정의.

### 2.2 절차 (read-only)

| Step | 명령 | 산출물 | 성공기준 |
|----|----|----|----|
| 1 | `curl -s http://127.0.0.1:11434/api/version` | JSON `{"version":"..."}` | 200 응답 + version ≥ 0.4 (MoE 미지원 ≤ 0.3.x 회피) + **JSON schema 검증** (R-2: HTML·플레인텍스트면 비정상, 다른 서비스 점유 의심) |
| 2 | `curl -s http://127.0.0.1:11434/api/ps` | 로드된 모델 + GPU 활용 보고 | `size_vram` > 0 if 모델 로드됨 |
| 3 | `nvidia-smi pmon -c 1` (1샘플) | GPU 프로세스 목록 | `ollama` 프로세스가 GPU 사용 중 (또는 idle 시 미표시 = 정상). **R-10 fallback**: GB10 unified memory 로 `pmon` 빈/0 보고 시 → `/api/show` `details.parameter_size` + `/api/ps` `size_vram` 을 *보조 증거*로 채택 (GB10 보고 한계 vs 실제 미사용 구분 한계 명시) |
| 4 | `ss -tlnp \| grep 11434` (재확인) | 바인딩 주소 | `127.0.0.1:11434` only — `0.0.0.0` 노출 시 **V-1 BLOCK** + 사용자 보고 |
| **5 (R-15)** | `env \| grep '^OLLAMA_'` + `curl -s http://127.0.0.1:11434/api/ps` | 환경변수 + 현재 동시 로드 모델 | `OLLAMA_NUM_PARALLEL` / `OLLAMA_MAX_LOADED_MODELS` 값 기록 (변경 X). 측정 중 동시 호출 차단 의무 (백그라운드 Claude Code·다른 셸의 ollama 호출 0) — R-23 합류 |

### 2.3 실패 분기

- version < 0.4 → MoE 미지원 우려, gap-pull 후 추론 실패 시 Ollama 업그레이드 필요 → 본 brief 범위 밖 (별도 승인)
- `0.0.0.0` 바인딩 발견 → R11 / M6 위반 → 측정 중단 + 사용자 결정 대기 (`OLLAMA_HOST=127.0.0.1` 재기동 권고만, 실행 X)

**🔴 R-2 추가 실패 분기 (fail-closed, 모법 R3 답습)**:

- **측정 중 데몬 죽음** — PID 3375 가 OOM/SIGSEGV/사용자 kill. `curl` timeout 후 `/api/version` 재polling → 응답 없음 / PID 변동 시 측정 *전체 폐기*(부분 데이터 보고 금지) + 사용자 보고. advisory 진행 금지.
- **11434 다른 프로세스 점유** — Ollama 재시작 race condition 또는 다른 서비스. Step 1 의 JSON schema 검증 실패 + `/api/version` 응답이 Ollama 형식 아니면 측정 중단 + 사용자 보고. 절대 advisory 결정 진행 금지.
- **GPU OOM → CPU fallback 감지** — 다른 프로세스가 GPU 사용 중 → Ollama 가 silent CPU 추론 (273GB/s 대역폭 가설 검증 무효). `/api/ps` `size_vram == 0` && `size > 0` 패턴 → fallback 의심 → 측정 *값 보고하되 "CPU fallback 의심" flag* 첨부, M3·M4 결정 입력 금지.
- **`/api/version` 비정상 응답** — 200 status 이나 JSON 파싱 실패 (HTML 에러 페이지·플레인텍스트 등) → 측정 중단. 일반 명령 (`curl`) 의 종료 코드만으로 success 판정 금지.

각 분기: **fail-closed (advisory 진행 금지)** + 사용자 명시 보고. 부분 데이터로 PASS 결론 도출 금지 (모법 §0.2 정직성).

---

## 3. V1-2 운영 절차 — MoE 모델 식별·gap-pull *판단*

### 3.1 목표

기존 5 모델 중 MoE A3B/A10B 활성 모델 식별 → 부재 시 후보 *식별*(pull 실행 별도 승인).

### 3.2 절차 (Step 1·2a·2b read-only / Step 3 결정 권고)

| Step | 명령 / 행위 | 산출물 | 성공기준 |
|----|----|----|----|
| 1 | `curl -s http://127.0.0.1:11434/api/show -d '{"name":"qwen3-coder-next:latest"}' \| jq '.modelfile, .parameters, .details, .model_info'` | manifest | `architectures: ["Qwen3MoE..."]` 또는 활성 파라미터 명시 = MoE 확인. dense면 §3.2 Step 2a 진행. **MoE 판별 보조 필드**: `details.parameter_size` (총), `model_info.general.architecture`, `modelfile` `PARAMETER` 라인. ambiguous 시 HuggingFace card 참조 fallback |
| **2a (R-5, C-F3)** | 후보 풀 **5~7종 식별** (read-only): `Qwen3.5-A3B-Instruct` · `Qwen3.5-Coder-A10B` · `Qwen3-Next family` (본 환경 `qwen3-coder-next` 가 Step 1 결과 따라 잔존/제외) · `DeepSeek-V3.1-Lite` · `GLM-4-MoE` · `Granite-3.5-MoE` · `OLMoE` · `mixtral:8x7b` (MoE 동작 검증용, **R-14**: 활성 ~13B = A3B 4배 → tok/s 직접 비교 X) | 후보 표 (5~7) | 활성 파라미터 ≤ 10B + Q4 ≤ 20GB 우선, 그 외 후보는 NOTE |
| **2b (R-5, A-F2)** | 각 후보 read-only 검증: `curl -s http://127.0.0.1:11434/api/show -d '{"name":"<candidate>"}'` (실재 시 manifest 반환) 또는 (실재 검색) `ollama search <keyword>` *권고만, 실 명령 별도 승인*. **`ollama search` 는 ollama.com egress 발생 — §8.1 baseline *전* 실행 시 흔적 포함** (R-11) | 후보별 실 tag 표 | 실재 ≥ 2 후보 잔존 → Step 3. 실재 0 → 검색 키워드 확장 + 사용자 보고 |
| 3 | gap-pull *권고*: 실재 후보 ≥ 1 → 사용자 명시 승인 요청 (본 brief 외) | 권고 entry | 디스크 영향 ≤ 50GB 누적 |

### 3.3 ⚠️ 디스크 가드

`~` 가용 333GB. gap-pull 1~2 후보 (최대 ~50GB) 후 잔여 ≥ 280GB → 안전 한계 200GB 위. **누적 추가 ≥ 100GB 시 사용자 재확인 의무** (롤백 단순화).

---

## 4. V1-3 운영 절차 — tok/s 측정 (decode + prefill 분리)

### 4.1 목표 (brief v2 §6 V1-3 + R5 답습)

- **decode tok/s**: 짧은 입력 + 긴 출력으로 측정 (memory-bound 영역)
- **prefill tok/s 또는 prefill 지연**: 긴 입력(`≥ 2048 tok` diff 모사) + 짧은 출력 (compute-bound 영역)
- **threshold 검증**: advisory 용도 `decode ≥ ~15 tok/s` 후보 (brief v2 M4 — *고정 금지*)

### 4.2 절차 (별도 승인 후 실행)

| Step | 명령 | 산출물 | 측정 항목 |
|----|----|----|----|
| 1 (decode) | `curl -s http://127.0.0.1:11434/api/generate -d @decode-prompt.json \| jq '.eval_count, .eval_duration, .load_duration'` — `decode-prompt.json` 본문: `{"model":"<MoE>","prompt":"<긴 출력 유도, 단락 5개 이상 한국어 코드 설명 예시>","stream":false,"options":{"num_predict":512,"temperature":0.0,"stop":[],"seed":42}}` (**R-8**: temperature 0 + stop 빈 + seed 고정 + 긴 출력 유도) | JSON | `eval_count / (eval_duration / 1e9)` = decode tok/s. `load_duration` 별도 보고 (R-21 NOTE) |
| 2 (prefill, **R-4 사전 검증**) | (i) `prefill-prompt.txt` 작성 → (ii) **사전 토큰 측정** `curl -s http://127.0.0.1:11434/api/embed -d '{"model":"<MoE>","input":"@prefill-prompt.txt"}'` 또는 (호환 시) `/api/tokenize` → 입력 토큰 수 확인 → (iii) **목표 ±10% 도달 (~2048 tok ± 200)** 까지 prompt 조정 → (iv) `curl ... /api/generate -d @prefill-prompt.json` (`{...,"options":{"num_predict":16,"temperature":0.0,"stop":[]}}`) | JSON + 토큰 수 사전/사후 비교 | (사후) `prompt_eval_count` 가 사전 측정값 ±10% → 통과. `prompt_eval_count / (prompt_eval_duration / 1e9)` = prefill tok/s. `total_duration - load_duration - eval_duration` = prefill wall-clock |
| 3 (반복, **R-9 outlier**) | Step 1·2 각 **warm-up 1 + 측정 5회**. 첫 측정값이 후속 평균의 2σ 초과 outlier → 재warm-up 1회 추가 → 재측정 5회 (총 warm-up 2). 5회 중 std/mean > 0.15 → **추가 3회 측정 + outlier 1개 trim 허용** (총 7 유효 + 1 trim 또는 raw 모두 보고) | mean·std·**p50·p95** (R-6 raw 보고) | warm-up 제외 raw 모두 §4.5 에 보존 |
| 4 (긴 diff, **R-4 사전 검증**) | Step 2 절차 그대로, 목표 **~8192 tok ± 800**. 입력 prompt 도 사전 토큰 측정 의무 | prefill 지연 (mean·std·p50·p95) | advisory UX 한계 평가 — **R-6**: PASS/FAIL 판정 X, raw 보고만 |

**보조 측정 (R-16, 옵션)**: Step 1·2 완료 후 동일 모델에 `ollama run <model> --verbose` 1회 + tok/s 출력 확인 → curl/jq 계산값과 **±5% 일치** 확인. 단일 도구 의존 (curl+jq 자체 버그·계산 차이) 회피. 보조 측정 ±5% 초과 불일치 시 양쪽 모두 raw 보고 + 사용자 결정 대기.

**Step 2 prefill 토큰 측정 fallback**: `/api/tokenize` 미지원 Ollama 버전 시 — (a) `/api/embed` 응답의 입력 토큰 수 필드 사용 (제공 시), (b) HuggingFace `tokenizers` 로 모델별 사전 토큰화 (별도 환경 필요 → NOTE R-?, 본 brief 권고 0), (c) raw 입력 글자수만 보고 + `prompt_eval_count` 실측에 의존 (한계 명시). 본 brief 권고 = (a) 우선, 불가 시 (c).

### 4.3 모델 비교 (R4 동급 측정)

같은 절차를 **§3 MoE 모델** + **`qwen2.5-coder:32b`(dense 비교 baseline)** + (gap-pull 시) **추가 MoE 후보** 에 대해 반복. **R-14**: `mixtral:8x7b` 는 활성 ~13B = A3B(~3B) 4배 → tok/s 직접 비교 X, "MoE 아키텍처 동작 검증" 한정. **C-F8 (R-30 NOTE)**: 본 baseline = *대역폭 우위* 검증용. *sparsity 본질* 검증은 isovolumetric (활성 동등) 별도 단계.

### 4.4 보고 항목 (R-6 전면 재작성 — 성공기준 X, raw 보고만)

🔴 **R-6 (B-F8 BLOCKING)**: v1 의 "성공기준" + "≥15 tok/s = PASS 후보" framing 은 모법 §9.2 ("threshold 고정 0건") 와 *자기모순*. v1.1 = anchor effect 제거 → **PASS/FAIL 판정 0건, raw 보고 only**.

| 보고 항목 | 형식 | 출처 |
|----|----|----|
| decode tok/s | mean · std · **p50 · p95** / 5회 (R-9 outlier 시 7+1trim 또는 raw 모두) | §4.2 Step 1 |
| prefill tok/s @ ~2048 tok | mean · std · p50 · p95 / 5회 + 사전/사후 토큰 수 (R-4) | §4.2 Step 2 |
| prefill tok/s @ ~8192 tok | mean · std · p50 · p95 / 5회 + 사전/사후 토큰 수 | §4.2 Step 4 |
| prefill wall-clock @ 8192 | raw 5회 + mean | §4.2 Step 4 |
| `load_duration` (첫 호출 cold) | raw 1회 (warm-up 측정 시 캡처) | §4.2 Step 1 (R-21) |
| 보조 측정 일치 | curl 계산값 vs `ollama run --verbose` ±% (R-16) | §4.2 보조 |
| 측정 환경 ID | Ollama version, binary sha256 (R-1), CUDA, kernel, 동시 프로세스 baseline | §4.5·§4.6 |

**M3·M4 결정 입력**: 본 §4 = raw 보고만, 결정은 **V-1 findings 후 별도 합의에서** (§9.2). 본 brief 어떤 행도 "PASS/FAIL" 표현 사용 금지 (B-F8 anchor 회피).

**참조 수치 (해석 X)**: 모법 §6 R5 의 roofline (A3B Q4 ~90–120 실효, dense 70B Q4 한자릿수) · 합의 R4 의 외부 실측 (llama.cpp Qwen3-Coder-30B-A3B ~31 tok/s) 은 *측정 후 해석 단계 입력* (본 brief 단계 입력 X).

### 4.5 raw 결과 보존 (R-22, C 추가권고 1)

측정 *전체 raw JSON* 을 보존. 사후 재분석·합의 입력 재현성·M3/M4 결정 단계 추적 가능성 직접.

| 항목 | 경로 / 형식 |
|----|----|
| raw JSON | `docs/phase0/v1-poc-raw/<YYYY-MM-DDTHH:MM:SS>-<model>-<scenario>.json` (scenario = `decode` / `prefill-2k` / `prefill-8k` / `aux-verbose`) |
| 환경 ID | 위 raw 파일 헤더에 inline 또는 `docs/phase0/v1-poc-raw/env-<timestamp>.json` (Ollama version, binary sha256 (R-1), `/api/version` 응답, GPU driver, CUDA, kernel, `OLLAMA_*` env 값, 동시 프로세스 baseline) |
| 누락 정책 | raw 미보존 측정 = findings 입력 자격 X (B-F13 정직성 SOP) |

### 4.6 측정 환경 동결 (R-23, C 추가권고 2 + R-15 합류)

측정 *중* 환경 변수 noise = tok/s 직접 왜곡 → 다음 모두 동결:

| 동결 항목 | 점검 방법 |
|----|----|
| 다른 GPU heavy 작업 0 | `nvidia-smi` 측정 직전 — Ollama PID 외 GPU 사용 프로세스 0 확인 |
| 다른 CPU heavy 작업 0 | `top -bn1 \| head -20` — CPU > 20% 프로세스 0 (Ollama 제외) |
| **백그라운드 Claude Code 세션 0** | 측정 중 별도 Claude Code 인스턴스 호출 0 (사용자 책임) |
| 다른 Ollama 호출 0 | `/api/ps` 로드 모델 변동 0 (R-15 합류) |
| 디스크 I/O 무거운 작업 0 | `iostat -x 1 1` `%util` < 20% (모델 로드 직후 제외) |

동결 위반 발견 시 → 측정 중단 + raw 폐기 + 사용자 보고. 부분 데이터로 결론 도출 금지.

---

## 5. V1-4 운영 절차 — `/v1/chat/completions` OpenAI-호환 확인

### 5.1 목표

`BossLLM` 추상(brief v2 §3, OpenAI-호환 endpoint) 가설 검증. Ollama + (있으면) llama.cpp 둘 다.

### 5.2 절차

| Step | 명령 | 성공기준 |
|----|----|----|
| 1 | `curl -s http://127.0.0.1:11434/v1/chat/completions -H 'Content-Type: application/json' -d '{"model":"<m>","messages":[{"role":"user","content":"ping"}]}' \| jq '.choices[0].message.content'` | 200 + 비어있지 않은 응답 |
| 2 | `usage` 필드(`prompt_tokens`·`completion_tokens`) 존재 확인. **R-2/R-12 fallback**: Ollama 0.20.4 가 `usage` 를 `None`/`0` 으로 반환 시 = NOTE (BLOCK 아님), `/api/generate` 의 `eval_count` / `prompt_eval_count` 우회 (advisory 비용 계측은 OpenAI-호환 layer 가 아닌 native API 로 측정) | advisory 비용/길이 계측 가능 (직접 또는 fallback) |
| 3 | `tools` / `tool_choice` 파라미터 미사용 검증 (advisory = 순수 텍스트, brief v2 R2) | trace 의 tool 사용 흔적 0 |
| **4 (R-38 NOTE, B-N3)** | `tools: [{"type":"function","name":"x","parameters":{}}]` 시도 → endpoint 가 *거부* 면 R2 강화 (frozen dataclass 위반 표면 차단) / *수용* 면 NOTE (코드 레벨 차단 의무, OllamaBoss 구현 시 답습) | 거부=PASS / 수용=NOTE |

---

## 6. V1-5 운영 절차 — 메모리/대역폭 실측

### 6.1 목표

273GB/s 병목 가설(brief v2 §2) 정량 재확인 → MoE 가 dense 대비 우위 재현.

### 6.2 절차 (GB10 unified memory 주의)

| Step | 명령 | 산출물 |
|----|----|----|
| 1 | 측정 직전 `cat /proc/meminfo \| grep -E "MemAvailable\|Cached"` 베이스라인 | 메모리 베이스라인 |
| 2 | §4.1 절차(decode) 실행 중 `nvidia-smi pmon -d 1 -c <decode 측정 총 시간 초>` 병행 (R-20: `-d 1 -c 85` 약 한 측정 사이클 전체 캡처. 또는 백그라운드 시작 → 측정 후 종료) | GPU SM 활용률 + 메모리 활용 |
| 3 | 측정 후 `cat /proc/meminfo` 비교 | unified memory 점유 증가량 |
| 4 (**R-18 한정**) | dense 32B vs MoE 동등 quant 의 tok/s 비교 = R5 검증 | MoE 가 ≥ 2x → **병목 가설과 *모순 안 함*** (logical leap 회피: tok/s 차이가 (a) 대역폭 (b) 활성 파라미터 수 (c) cache locality 중 어느 원인인지 분리 불가). raw 보고만, "PASS" 표현 X |
| 5 (**R-37 NOTE, B-N2**) | 모델 전환 시 `curl -X DELETE /api/ps -d '{"name":"<prev>","keep_alive":0}'` (또는 `keep_alive: 0` 으로 즉시 unload) + `/proc/meminfo` 복귀 확인 → 다음 모델 측정 cache locality 통제 | 이전 모델 잔존 영향 격리 |

### 6.3 한계 (정직성, R-10·R-18·B-F11 보강)

- GB10 unified memory 모델은 dGPU `nvidia-smi --query-gpu=memory.used` 보고 *불완전* (§1.1). 본 측정 = **간접** (점유 변화량 + tok/s 비교).
- **`/proc/meminfo` = 시스템 *전체* 메모리** (다른 프로세스 포함). Ollama 의 *순* 점유는 측정 *전후* diff 만으로 추정 가능 + 다른 프로세스 noise 제거 불가 (R-23 동결로 부분 완화).
- 정밀 대역폭(GB/s) 측정 도구(`bandwidthTest`·`stream`) 별도 빌드 필요 → 본 brief 범위 밖.
- **R-18 결론 강도 한정**: 본 §6 = **"대역폭 병목 가설과 *모순 안 함*" 까지만 검증 가능**. "병목 *재확인* PASS" 라는 강한 결론 = 정밀 대역폭 측정 도구 별도 빌드 후에만. V-1 findings 는 본 한계 명문 답습.
- **R-25 NOTE (C-F6)**: 정밀 도구 후보 = `tegrastats` (Jetson/Tegra 가족, GB10 Grace 부분 적용 가능성 — 별도 검증) / Nsight Systems (sm_120/121 지원 *미확정*, 식별만) / sm_120 PMU 직접 (ARM SBSA standardized counter — MVP-2 oversized) → 본 brief 측정 절차 변경 0.

---

## 7. llama.cpp 비교 측정 (R4 동급)

### 7.1 목표 (brief v2 R4 답습)

vLLM 영구 배제 정정 ("MVP-2 재검토"). **llama.cpp ↔ Ollama 동급** 비교. 2026-05 실측 보고서(llama.cpp Qwen3-Coder-30B-A3B ~31 tok/s Q8_0)와 본 환경 재현.

### 7.2 절차 (Phase 분리 — 빌드 발생, 별도 승인)

| Phase | 행위 | 별도 승인 |
|----|----|----|
| 7-A | **빌드 후보 식별만**: `llama.cpp` source build (CUDA 13 + sm_121) 또는 prebuilt aarch64 확인 — *식별만*, 빌드 0. **R-24 + R-39 + B-N4**: prebuilt 채택 시 공식 GitHub release SHA 확인 의무 (출처 미상 binary 위험, R-1 답습). 빌드 시스템 현행 README 확인 (**R-32**: 2024 `LLAMA_CUDA=1` → 2025 `GGML_CUDA=1` → 2026 CMake 이동 가능성, `make` vs `cmake` 정확한 명령 README 확정) | 본 brief 범위 (식별) |
| 7-B | 빌드 실행 — `~/build/llama.cpp` 디렉토리, sudo 0. **R-17 위생** (빌드 *전*): (i) `~/build/llama.cpp` 비어있음 확인 (기존 빌드 잔존 시 사용자 결정), (ii) 빌드 *실패* 시 `rm -rf ~/build/llama.cpp ~/.ccache` 전체 정리, (iii) **`make install` / `sudo` 금지** (시스템 라이브러리 `/usr/local/lib/*.so` 미설치) | **별도 승인 필수** |
| 7-C | `llama-server -m <gguf> --port 8080` + `/v1/chat/completions` 절차 §5 재현 | **별도 승인 필수** |

### 7.3 우선순위 권고 (고정 금지)

V-1 1차 목표 = Ollama 측 완측. llama.cpp 비교는 **Ollama 측 보고 후** 진행하면 M3 결정 충분. 동시 진행 시 변수 통제 어려움 (R4 답습이되 순서는 권고).

---

## 8. 텔레메트리·egress 위생 (R11 답습)

### 8.1 점검 (read-only)

| 점검 | 명령 | 기준 |
|----|----|----|
| 측정 중 외부 egress 0 | 측정 전·후 `ss -tnp \| grep ollama` | ESTABLISHED 외부 연결 0건 (localhost 만) |
| Ollama 텔레메트리 비활성 확인 | `OLLAMA_NOHISTORY` / `OLLAMA_NO_ANALYTICS` 등 환경변수 *제안만* (영구 설정 X). **변수명 자체가 Ollama 0.20.4 가 실제 인식하는지 미확정** (Agent A 정직성) — 측정 단계에서 효과 검증 | 측정 세션 export 권고 (사용자 결정) |
| 모델 pull 시 egress (해당 시) | `ollama.com` / 미러 도메인만 | 그 외 도메인 발견 시 측정 중단 + 보고 |

> **🔴 R-3 시간 범위 명문 한정 (B-F3 (b))**: 본 §8 점검 = **측정 *세션* (V1-1~V1-5 실행 윈도) 한정**. 측정 외 시점의 egress — (i) Ollama 자체 *업데이트 체크* (주기 미상) / (ii) *텔레메트리* (lazy upload 가능) / (iii) *전반 lifetime* (수 시간/일 단위 transient connection) — 는 본 §8 범위 *밖*. "egress 0 검증 완료" 라는 결론 = *측정 세션 한정* 으로 한정 표현 의무. 데몬 lifetime 전체 egress = R-11b 별도 cycle.

### 8.2 정직성 노트 (brief v2 §5 답습)

> "추론 시점 egress 0" 은 *추론* 한정. 설치/모델 pull/텔레메트리는 별개 (거짓 안전감 예방). 본 §8 = 그 *별개* 표면 점검.

### 8.3 옵션: 더 강한 점검 (R-11b, B-F3 (a))

본 §8 의 측정 세션 한정 점검을 *시간적으로* 확장하고 싶을 경우 — **별도 cycle**:

- baseline 캡처 (측정 직전 `ss -tnp` snapshot)
- 측정 중 **30s 주기 polling** (백그라운드 `while sleep 30; do ss -tnp | grep ollama; done >> egress.log`)
- 측정 *완료 후 5분 재점검* (lazy upload 가능성)
- 더 강한 도구 후보 — `tcpdump -i any port 80 or port 443 -w /tmp/v1-poc-egress.pcap` 세션 한정 capture, 사후 `tcpdump -r ... | grep -v 127.0.0.1` 분석 (C-F5 NOTE)

본 brief = 절차 *식별* 만, 실행은 별도 cycle (사용자 결정).

---

## 9. M3 / M4 결정 매트릭스 (권고 — 고정 금지)

### 9.1 M3 (llama.cpp ↔ Ollama) — **R-7 framing 정정**

🔴 v1 의 "Ollama 우선" framing 은 결정 *고정 압력* (B-F7) → v1.1 = **본 brief 0건 고정**, "V-1 findings 후 별도 합의에서 결정" 으로 강화. 둘 다 FAIL 시 3rd 후보 식별 추가 (C-F2, Provider Liquidity 답습).

| 측정 결과 | 본 brief 권위 — 결정 0건 (V-1 findings 후 별도 합의 입력만) |
|----|----|
| 둘 다 raw 보고 가능 + `/v1/` 호환 OK | **두 런타임 동시 유지 가능** (provider-agnostic, 헌법 5조 답습). 운영 default 선택은 V-1 findings 후 별도 합의 — 본 brief 어떤 행도 "우선/백업" 표현 사용 X |
| Ollama raw 보고 가능 / llama.cpp 빌드·실측 실패 | findings 에 두 결과 raw 동등 기록 — Ollama 단독 결정도 *별도 합의* (vLLM "MVP-2 재검토" 동형, llama.cpp 영구 배제 금지) |
| Ollama 실측 실패 / llama.cpp raw 보고 가능 | 위와 대칭 |
| **둘 다 실측 실패** | M2 (모델) 재선정 (A10B / A3B 다른 quant) **+** **3rd 후보 식별 단계** (R-7 추가): **MLC-LLM** (TVM-기반, aarch64 보고 다수, sm_120/121 실증 별도 검증 필요) / **llamafile** (single binary, MoE 지원) / **ktransformers** (MoE 특화) / **vLLM** (MVP-2 재검토, brief v2 R4 답습) — 식별만, 측정 별도 cycle |

### 9.2 M4 (tok/s threshold)

V-1 실측 5회 평균 + std 보고만. **본 brief 는 threshold 고정 0건**. 후속 합의에서 결정.

---

## 10. 롤백 정책 (환경 보존 우선)

| 추가 산출 | 롤백 |
|----|----|
| gap-pull 모델 | `ollama rm <model>` (디스크 회수, 즉시 reversible) |
| llama.cpp 빌드 (7-B 별도 승인 시) | `rm -rf ~/build/llama.cpp` (~ 한정, 시스템 변경 0) |
| 환경변수 export | 측정 셸 종료로 자동 소멸 (`.bashrc`·`.profile` 변경 0) |
| 측정 결과 파일 | `docs/phase0/jarvis-mvp1-v1-poc-findings.md` 작성 (commit 별도 승인) |

**기존 Ollama 설치는 본 brief 어떤 단계에서도 제거·재설치·권한 변경 0건** (출처 미상 위생 위험은 별도 단계 검토 — **R-19**: trigger = §12 옵션 (E), V-1 findings 후 트랙 B 진입 *전* 별도 검토).

**R-34 NOTE**: 측정 셸 환경변수는 fresh subshell (`bash -c '...'` 또는 `env -i bash`) 권고 — `.bashrc`·`.profile` persist 회피, `tmux`/`screen` 안에서도 셸 종료 시 변수 소멸.

---

## 11. 산출물 (계획)

V-1 PoC 실 실행 후 작성 예정:

- `docs/phase0/jarvis-mvp1-v1-poc-findings.md` — 환경·모델·측정값·M3/M4 권고
- (필요 시) `docs/phase0/jarvis-mvp1-v1-poc-llama-cpp-comparison.md` — §7-B/C 진입 시
- `docs/phase0/v1-poc-raw/<timestamp>-*.json` (R-22 raw 보존)

본 brief 작성만으로는 위 문서 생성 0건.

### 11.1 findings 정직성 SOP (R-28, B-F13)

findings 작성 시 다음 골격 의무:

```
# V-1 PoC findings (예시)
## 측정 환경 (정직성 prerequisite)
- Ollama version, binary sha256 (R-1), systemd 상태
- GPU driver, CUDA, kernel
- 동시 실행 프로세스 (CPU/GPU/메모리 baseline, R-23 동결 확인)
- 디스크 가용 변화량
- R-2 4 분기 발생 여부 (이상 시 측정 폐기)
## raw 측정값 (가공 0)
- 모델별·세션별·반복별 tok/s, mean/std/p50/p95
- raw eval_count/duration/prompt_eval_count/prompt_eval_duration
- prefill 사전 토큰 vs 사후 prompt_eval_count diff (R-4)
- 보조 측정 (ollama run --verbose) ±% 일치 (R-16)
## 가공 (분리)
- roofline 대비 ratio (해석, 결론 아님)
- M3·M4 합의 입력 (결정 0건, R-6)
## 정직성 한계 (필수)
- R-1 출처 미상 데몬 사용의 한계 (sha256 변동 여부)
- §6 unified memory 간접 측정 한계 (R-18)
- R-3 egress 점검 시간 범위 한정
- 측정 reproducibility 한계 (B-F1)
- "PASS/FAIL" 표현 금지 (R-6)
```

---

## 12. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 단계별 합의 cycle (각 단계 별도 명시 승인) |
|----|----|----|
| (A) | V1-1 §2 (read-only) 실 측정 진입 | 본 brief v1.1 → 사용자 검토 → V1-1 실행 승인 → findings → 별도 cycle |
| (B) | 본 brief 추가 보완 (누락 항목, 절차 정밀화) | brief v1.2 → 사용자 검토 → ... |
| (C) | gap-pull 사전 결정 (V1-2 단계 단축) — §3.2 Step 2b 검증 후 | brief v1.1 합의 → gap-pull 별도 승인 → V1-2 |
| (D) | llama.cpp 빌드 (§7-B) 별도 ramp 으로 분리 | Ollama 측 완측 → llama.cpp 별도 cycle |
| **(E) (R-19)** | **V-1 findings 작성 *후* 트랙 B 진입 *전* — 출처 미상 Ollama 위생 정정 trigger 검토** (R-1 답습). 4 옵션 매트릭스 (현재 유지 / user-mode 격리 / docker-isolated / sudo 교체) — 별도 합의 단계 | findings → 별도 합의 (사용자 명시 trigger) |

**보안 거버넌스 자동 재개 금지** (비례성, `feedback_proportionate_security_personal_tool` 답습). 단 옵션 (E) 의 위생 정정 trigger 는 R-1 발견 후 추가된 *새로운* 별도 단계 — 자동 진입 아님, 사용자 명시 결정.

---

## 부록 A — brief v2 §6 ↔ 본 brief 매핑

| brief v2 §6 항목 | 본 brief § | 상태 |
|----|----|----|
| V1-1 설치·구동 | §2 | 부분 완료 (위생 점검으로 재정의) |
| V1-2 모델 pull + 추론 | §3 | gap 식별 단계로 재정의 |
| V1-3 decode + prefill 측정 | §4 | 동일 (절차 구체화) + R-4 입력 토큰 검증 + R-6 보고 항목 재작성 |
| V1-4 `/v1/` 호환 | §5 | 동일 (절차 구체화) + R-2 `eval_count` 우회 + R-38 tools 거부 검증 |
| V1-5 메모리/대역폭 | §6 | GB10 unified memory 한계 명시 + R-18 결론 강도 한정 |
| R4 llama.cpp 동급 비교 | §7 | Phase 분리 추가 (빌드 별도 승인) + R-17 빌드 위생 + R-7 3rd 후보 식별 |
| R11 egress 추론시점 한정 | §8 | 위생 점검 절차 추가 + R-3 시간 한정 + R-11b polling 옵션 |

> **🔴 R-29 NOTE (B-F12)**: "부분 완료" 라벨은 brief v2 V1-1 가정 (사용자/agent 가 *통제* 하는 깨끗한 설치) 자체가 환경 사실로 *우회* 되었음을 의미. v2 가정 적용은 (R-1 위생 정정 단계 §12 옵션 E 후) 재검토 필요. 단순한 "부분 완료" 가 아니라 *근본적으로 다른 시작점* 임을 명시.

---

## 부록 B — NOTE carryover (R-20 ~ R-39, 17건)

본 brief v1.1 본문에 흡수된 NOTE (R-10·R-14·R-16·R-17·R-18·R-21·R-24·R-25·R-28·R-29·R-32·R-34·R-37·R-38·R-39) 외, 다음 항목은 추가 *별도 cycle* carryover (본 brief v1.1 본문 변동 없음):

| R-# | 항목 | 출처 | 처리 |
|----|----|----|----|
| **R-20** | §6.2 `pmon -c 5` 간격 명시 → v1.1 §6.2 Step 2 에 `-d 1 -c <측정 시간>` 으로 명시 | A-F8 | **본문 흡수** (§6.2 Step 2) |
| **R-21** | streaming/TTFT 별도 측정 (advisory 체감 ≠ decode tok/s) | A 추가권고 3 | findings 작성 시 raw 보고 항목으로 자연 포함, 별도 cycle |
| **R-26** | 출처 미상 Ollama 4 대안 트레이드오프 매트릭스 부록 (옵션 (E) 진입 시) | C-F7 | §12 (E) 단계에서 별도 brief |
| **R-27** | 디스크 가드 MoE quant 별 실제 용량 표 | A 추가권고 6 | gap-pull 별도 승인 단계 brief 에서 |
| **R-30** | isovolumetric (활성 동등) baseline 별도 단계 | C-F8 | findings 후 별도 cycle |
| **R-31** | `qwen3-coder-next` MoE 판별 필드 사전 예시 → §3.2 Step 1 manifest 조회 시 보조 (현 §3.2 Step 1 의 *MoE 판별 보조 필드* 라인으로 부분 흡수) | A-F9 | **본문 부분 흡수** (§3.2 Step 1) |
| **R-33** | `-d @file.json` 일관성 (큰 body) → §4.2 Step 1·2 가 이미 `-d @decode-prompt.json`·`-d @prefill-prompt.json` 으로 채택 | A-F11 | **본문 흡수** (§4.2) |
| **R-35** | 데몬 uptime/PID 변동 확인 → R-1 의 sha256 검증과 묶어 처리 | A 추가권고 5 | **R-1 흡수** |
| **R-36** | 측정 대상 무결성 검증 (binary hash·schema·driver) → R-1 의 sha256sum + §4.5 환경 ID 로 확장 | B-N1 | **R-1 + §4.5 흡수** |

본 부록 B = NOTE 상기 한정 / NOTE 의 본문 흡수는 각 § 에 inline 표기 / 그 외는 별도 cycle (사용자 결정).

---

**출처**: brief v2 (`jarvis-mvp1-local-boss-design-brief.md`) §6 / 합의 (`3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`) R4·R5·R11 / **합의 (`3plus1-consensus-2026-05-23-jarvis-mvp1-v1-poc-entry.md`) R-1 ~ R-23 (BLOCKING 6 + 권고 14 + NOTE 17, v1 → v1.1 보강 권위)** / `jarvis-orchestrator-mvp-design-brief.md` v4 §7 V-1 / `jarvis-safety-layer-poc-findings.md` (V-1 미착수, 본 brief 부분 정정) / `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention` / `feedback_staged_consensus_workflow`.

**금지 (영구 답습, 본 brief 0건)**: 신규 설치 실행 / sudo / systemd 변경 / 모델 pull 실행 / 측정 명령 실행 / `OllamaBoss` 코드 작성 / config 영구 설정 / M2·M3·M4 결정 고정 / 기존 Ollama 제거·재설치 / **기존 Ollama 데몬 재시작·kill·signal (R-1)** / firewall 변경 / 합의 보고서 작성 / commit·push / 보안 거버넌스 (credential·4축·BI-*) 자동 재개.
