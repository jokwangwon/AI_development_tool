# 자비스 MVP-1 V-1 PoC Phase 3 cycle (C-e 정공법) entry brief (DRAFT v1)

> **본 brief = M3·M4 합의 §5.3 + 3+1 합의 (`d2d7bf9`) §6 권고 (A) 정공법 답습.** brief 자체로 **빌드 실행 / 측정 / 합의 보고서 작성 / commit / push** 발생 0건. brief = **(i) 답습** + **(ii) C-e 정공법 실행 절차** + **(iii) 정직성 한계** 식별 한정.

---

**작성일**: 2026-05-24
**Status**: **DRAFT v1** (사용자 검토 대기). 3+1 합의 `d2d7bf9` 권고 (A) 정공법 채택. M3·M4 §5.3 + BLOCKING 5건 답습. 실 빌드·측정 0건.
**진입 단위**: V-1 PoC Phase 1 (`9c6b578`) + Phase 2 (`c66756b`) + 3+1 합의 (`d2d7bf9`) 후 → **Phase 3 cycle (C-e 정공법) 운영 entry**
**cycle 자격 근거**: 3+1 합의 §6 BLOCKING 1 (결정 *고정* 자격 미충족, Phase 3 의무) + M3·M4 §5.3 C-e 명문 + 3+1 합의 §3 P-1 L3·L4 Phase 3 후 재 합의 + Phase 2 §9.8 (iii)(iv) 미해소
**선행 답습**:
- Phase 1 결과 (`v1-poc-raw/2026-05-24-phase1-summary.json`) — A-진단 roofline 90~120 tok/s + C-c cache miss 분리
- Phase 2 §9 EXECUTED — F1 (i) 부정 (HF "3B activated" verbatim) + (ii) 명칭 정정 (Gated DeltaNet, NOT classical SSM) + (v) 강한 evidence
- 3+1 합의 §6 BLOCKING 5 + §3 P-1 계층화 부분 채택 + §5 G-1 C hybrid 대안 carry-over + G-2 새 가설 #6 (sm_120/121 미지원) carry-over
**답습 권위 한계**: 본 brief = *Phase 3 운영 entry* DRAFT — M3·M4 결정 *고정* / OllamaBoss·LlamaCppBoss 코드 / setup 변경 / 합의 보고서 작성 / gap-pull 실행 = 별도 단계 (사용자 명시)

---

## 0. 범위

### 0.1 사용자 진입 명령 답습 (2026-05-24)

> "T 이후 R 진행" — 3+1 합의 (`d2d7bf9`) §6 권고 (A) 정공법 채택 + 본 entry brief 작성. brief 자체 = 빌드 실행 0건.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**:
  1. Phase 3 cycle (C-e 정공법) 의 *실행 절차* 운영화 (§2)
  2. 빌드 egress 시점·범위·종료 보장 정의 (§3)
  3. §8 baseline 점검 절차 (egress 직전·직후, §4)
  4. 보고 항목 정의 — raw 한정, PASS/FAIL framing 금지 (§5)
  5. 정직성 한계 식별 (§6)
  6. 3+1 합의 BLOCKING 5건 답습 패턴 명문

- **하지 않는 것** (3+1 합의 §7 + 본 brief 영구 답습):
  - ❌ llama.cpp 실 빌드 / 측정 (본 brief = 절차 식별만)
  - ❌ Ollama 데몬 재시작·kill·signal (R-1 답습)
  - ❌ 모델 pull (기존 qwen3-coder-next GGUF 재사용)
  - ❌ Ollama config 변경 (`OLLAMA_*` env 영구 설정 X)
  - ❌ M3·M4 결정 *고정* (Phase 3 raw 보고만, 결정은 Phase 1+2+3 종합 후 별도 합의)
  - ❌ `OllamaBoss` / `LlamaCppBoss` 코드 작성 (트랙 B = Phase 3 측정 후 별도)
  - ❌ gap-pull *실행* (R-10 SOP 통과 + P1 trigger 자격 평가 별도 cycle)
  - ❌ 합의 보고서·commit·push (Phase 3 raw → findings → 별도 합의)
  - ❌ 보안 거버넌스 (credential·4축·BI-*) 자동 재개

### 0.3 비례성 답습

본 cycle = 본인용 개인 개발 툴의 inference engine 비교 측정 한정 (~2-4시간). `feedback_proportionate_security_personal_tool` 답습 — llama.cpp 빌드는 일상적 OSS 빌드 행위. 빌드 egress (github.com clone + apt deps 가능) 의 위생 점검 (R-11 답습) 은 *측정 정직성* 입력 목적, 보안 거버넌스 자동 재개 trigger 아님. 단 github.com 외부 egress 발생 = R-3 시점 격리 의무.

### 0.4 정공법 채택 근거 (vs B hybrid)

3+1 합의 §6 권고 (A) 정공법 선택 근거:
- Provider Liquidity 답습 강도 ↑ (실 빌드 = LlamaCpp endpoint 동작 *실측* 검증, B hybrid prebuilt binary = 출처 SHA 검증 의존)
- (iii) Ollama vs llama.cpp 분리 = **빌드/플래그 통제 가능** (정공법) > prebuilt binary 의 의도 미상 옵션
- (iv) router overhead 추정 강도 ↑ (정공법은 빌드 옵션 (CUDA backend + Q4_K_M kernel + KV cache size 등) 통제로 (iv) 영향 격리 가능)
- C 신규 가설 #6 (sm_120/121 미지원) 검증 = llama.cpp 도 동일 격차 시 강화 / llama.cpp 양호 시 부정 — 정공법 결과의 신뢰도 ↑
- **trade-off**: 시간 ~2-4시간 (B hybrid 의 ~20분 대비 10× 이상). 단 본 cycle = **결정 *고정* 자격 평가**, 시간 비용 대비 evidence 강도 우선

**B hybrid 잔여 옵션**: 정공법 빌드 실패 / GB10 sm_120/121 미지원으로 빌드 불가 / CUDA backend 비활성화 등 contingency 발생 시 B hybrid (prebuilt binary) fallback 진입 — 별도 명시 승인 의무.

---

## 1. Phase 3 cycle 목적

### 1.1 1차 목적 — (iii)(iv) 미해소 분리

**가설 (iii) Ollama 0.20.4 hybrid 효율성 (vs llama.cpp)**:
- Phase 2 §9.8: "Phase 3 C-e 측정 필요" verbatim
- 측정 대상: 동일 GGUF / 동일 prompt / 동일 환경에서 llama.cpp decode tok/s vs Ollama 7.83 tok/s
- 분기점:
  - 격차 < 20%: (iii) 가설 부정 → (v) BW 본질 강화 + (iv) router overhead 가설 carry-over
  - 격차 20-50%: (iii) + (v) 복합 가설 강화 (Agent C Q3 (b) 답습)
  - 격차 > 50%: (iii) 강한 evidence → (v) 약화 → Ollama 구현 비효율 본질 가설 우선
  - llama.cpp 빌드/실행 실패: 새 가설 #6 (sm_120/121 미지원) 강화 → 별도 cycle

**가설 (iv) Qwen3-Next router/gating overhead**:
- Phase 2 §9.8: "Phase 3 별도 측정"
- Phase 3 정공법으로 *직접* 측정 어려움 (Ollama·llama.cpp 모두 router timing 분해 instrumentation 미제공)
- *간접* 측정: llama.cpp 의 verbose log (--verbose / --log-disable false) 에서 token-step time breakdown 추출 시도. 빌드 옵션에 따라 분해 가능 여부 verify 필요
- 한계: 직접 분해 불가 시 (iii) 와 (iv) 결합 효과만 측정 가능 → 정직성 명문 의무

### 1.2 부차 목적 — BLOCKING 5건 입력

| BLOCKING | Phase 3 입력 |
|---------|-------------|
| 1 (결정 고정 자격 미충족) | C-e 결과 입력 후 Phase 1+2+3 종합 합의 → 자격 평가 |
| 2 (R-10 일반화 SOP 미정) | Phase 3 결과 자체와 무관 (별도 SOP cycle, 3+1 합의 §3 P-2 답습) |
| 3 (BW 본질 단정 금지) | (iii) 분리 후 (v) 강도 재평가 입력 |
| 4 (SSM 명명 0건) | M3 결정 문구 수정 = 결정 *고정* 단계 별도 |
| 5 (rollback trigger 명문) | 계층화 고정 시 ADR-011 §2.1 답습, Phase 3 결과 입력 후 |

### 1.3 새 가설 검증 (3+1 합의 §5 G-2 carry-over)

**가설 #6 — Qwen3-Next 특수 구조 (Gated DeltaNet + MoE hybrid) GB10 sm_120/121 미지원 가능성**:
- 검증 방법: llama.cpp 빌드 + 실행 시 CUDA backend 활성·sm_120/121 kernel 컴파일 verify
- 분기점:
  - llama.cpp 빌드 성공 + 실행 성공: #6 가설 약화 (sm_120/121 지원 형태로 작동)
  - 빌드 성공 + 실행 실패 (런타임 kernel 누락 등): #6 강화 → 별도 cycle (Phase 4 후보)
  - 빌드 실패 (sm_120/121 미인식): #6 강한 강화 → B hybrid fallback 또는 Phase 4

### 1.4 Phase 3 단독 자격 한계

- 본 cycle 결과만으로 M3·M4 결정 *고정* 자격 X (3+1 합의 §3 P-1 답습)
- Phase 1+2+3 종합 합의 cycle 별도 필수
- (iv) router overhead 직접 분해 불가 시 (iii) 와 결합 효과만 측정 — 정직성 명문 의무

---

## 2. C-e 실행 절차

### 2.1 사전 점검 (빌드 *전*, ~10분)

| Step | 명령 / 행위 | 산출물 | 성공기준 |
|----|----|----|----|
| 1 | R-1 anchor 8회차 — `sudo sha256sum /proc/3375/exe` (사용자 명시 prompt) | hash | Phase 1·2 hash `ce95c47...8877b10` 와 일치 |
| 2 | §8 baseline pre — `sudo ss -tan state established` + `date -Iseconds` | 외부 ESTABLISHED 목록 + anchor 시각 | github.com 도메인 0건 확인 (cycle-前) |
| 3 | R-23 환경 동결 — `ps -ef \| grep -E 'claude\|ollama' \| grep -v grep` + `nvidia-smi` | 본 Claude 세션 only + GB10 baseline | 다른 LLM 호출 0건 |
| 4 | 빌드 환경 verify — `gcc --version`, `g++ --version`, `cmake --version`, `nvcc --version`, `nvidia-smi --query-gpu=name,driver_version,compute_cap --format=csv` | toolchain 버전 + GB10 compute cap (sm_121 확인) | gcc ≥ 11, cmake ≥ 3.18, nvcc ≥ 12.4, compute_cap = 12.1 |
| 5 | 디스크 공간 — `df -h /home /tmp` | 가용 공간 | 빌드 ~10GB + GGUF 재사용 → 가용 ≥ 30GB 권고 |
| 6 | Ollama 메타 답습 — `curl -s http://127.0.0.1:11434/api/show -d '{"name":"qwen3-coder-next:latest"}' \| jq -r '.modelfile' \| grep -i FROM` | GGUF blob 경로 | `/root/.ollama/models/blobs/sha256-30e51a7c...` 확인 (Phase 2 §9.1 답습) |

### 2.2 llama.cpp 빌드 (egress 발생, ~30분-2시간)

| Step | 행위 | 명령 / 도구 | egress |
|----|----|----|----|
| **1** | **clone** | `cd ~/src && git clone https://github.com/ggerganov/llama.cpp.git llama.cpp` (또는 사용자 선호 경로) | github.com (~30MB) |
| 2 | **commit anchor** | `cd llama.cpp && git log -1 --format='%H %s' > /tmp/llamacpp-build-anchor.txt && git describe --tags --abbrev=8` | (egress 0) — 빌드 시점 commit 고정 |
| 3 | **Qwen3-Next 지원 verify** | `grep -r 'qwen3.next\|qwen3-next\|qwen3_next' . --include='*.cpp' --include='*.h' --include='*.py' \| head -20` | (egress 0) | 지원 코드 존재 여부 확인. 미존재 시 → §2.6 분기 (master branch 미지원 가능) |
| 4 | **CUDA backend 빌드** | `cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES='120;121' -DCMAKE_BUILD_TYPE=Release` (sm_120/121 명시) | (egress 0) — local toolchain |
| 5 | **컴파일** | `cmake --build build --config Release -j$(nproc)` | (egress 0) |
| 6 | **빌드 산출물 verify** | `ls -la build/bin/llama-cli build/bin/llama-server 2>&1` + `./build/bin/llama-cli --version` | (egress 0) | binary 존재 + CUDA backend "build with cuda" 확인 |
| 7 | **GGUF 로딩 verify** | `./build/bin/llama-cli -m /root/.ollama/models/blobs/sha256-30e51a7c...ffb -p "test" -n 1 --no-display-prompt 2>&1 \| tail -20` | (egress 0) | 모델 로딩 + 1 token 생성 성공. Qwen3-Next 미지원 시 fail → §2.6 분기 |

**egress 격리 보장 (§3 R-11 답습)**:
- §2.2 Step 1 = github.com clone only — 다른 도메인 0 verify (§3 격리)
- Step 4-6 = local toolchain (gcc/g++/nvcc) — egress 0
- Step 7 = local file read — egress 0
- 의존성 누락 시 apt install 필요한 경우 = ubuntu repo egress (Step 1 외 egress 발생 시 사용자 재확인 의무)

### 2.3 측정 (egress 0, ~30분)

| Step | 행위 | 명령 / 도구 | 측정 항목 |
|----|----|----|----|
| 1 | R-23 동결 재확인 (측정 *직전*) | `ps -ef \| grep -E 'claude\|ollama\|llama-cli' \| grep -v grep` | 본 Claude + llama-cli 만 ✓ (Ollama runner = idle 또는 stop 권고) |
| 2 | Ollama runner stop (선택) | `curl -X POST http://127.0.0.1:11434/api/stop -d '{"name":"qwen3-coder-next:latest"}'` 또는 사용자 명시 후 자연 idle | runner 종료 ✓ (메모리 경합 회피) |
| 3 | **llama.cpp decode 측정** | `./build/bin/llama-cli -m <GGUF> -p "<Phase 1 prompt set 답습>" -n 256 --no-display-prompt -ngl 999 2>&1 \| tee /tmp/llamacpp-measure-1.log` | tok/s decode (eval time / n_tokens 추출) |
| 4 | 반복 측정 (3회) | Step 3 × 3 회, 시각 anchor 별 기록 | tok/s mean ± std, std/mean (안정성) |
| 5 | (선택) **router overhead 간접 측정** | `./build/bin/llama-cli ... --verbose --log-disable false 2>&1` 의 layer-step breakdown 추출 | per-layer time (CUDA kernel call breakdown 시도). 분해 불가 시 정직성 명문 |
| 6 | **Ollama 재측정 (cross-check)** | Ollama 재시작 후 동일 prompt 동일 환경 measurement | Phase 1 답습 — 7.83 tok/s 재현 검증 |
| 7 | 측정 직후 anchor | `sudo sha256sum /proc/3375/exe` (R-1 anchor 9회차) + `date -Iseconds` | hash 일관 ✓ |

**측정 표준 명문**:
- 동일 GGUF (Ollama blob sha256-30e51a7c...ffb)
- 동일 prompt set (Phase 1 답습)
- 동일 환경 (R-23 동결, GB10 idle, 다른 LLM 호출 0)
- `-ngl 999` (모든 layer GPU offload, KV cache GPU 우선)
- `-n 256` token 생성 (Phase 1 답습)
- 3회 반복 (std/mean 안정성 평가)

### 2.4 종료 보장 + §8 cycle-後 baseline (~5분)

| Step | 명령 | 성공기준 |
|----|----|----|
| 1 | llama-cli 종료 verify | `ps -ef \| grep llama-cli \| grep -v grep` 0건 |
| 2 | §8 baseline post | `sudo ss -tan state established` + `date -Iseconds` | cycle-前 대비 변동 분석 (cycle-中 의도 egress = github.com only) |
| 3 | R-1 anchor 10회차 (Phase 3 직후) | Phase 1·2 hash 와 일치 |
| 4 | R-23 환경 동결 사후 | 본 Claude 세션 only 유지 + GB10 idle 복귀 |
| 5 | Ollama 외부 egress 0 재확인 | `sudo ss -tan state established \| grep -E '11434\|34891\|34131'` localhost only |
| 6 | 빌드 산출물 디스크 사용량 | `du -sh ~/src/llama.cpp/build 2>&1` (carry-over, 다음 cycle 재사용) |

### 2.5 실패 분기 (fail-closed, advisory 진행 금지)

| 분기 | 조건 | 대응 |
|----|----|----|
| **빌드 실패 (CUDA backend)** | §2.2 Step 4-5 cmake/make 에러 (sm_120/121 미인식 / CUDA 라이브러리 누락) | 1회 재시도 (clean build) → 재실패 시 cycle 일시 중단 + 사용자 보고. B hybrid fallback 자격 평가 별도 |
| **Qwen3-Next 미지원** | §2.2 Step 7 또는 §2.3 Step 3 에서 "unsupported architecture" 또는 비정상 출력 | master branch 미지원 가능 (가설 #6 강화) → fork/PR 검색 별도 cycle |
| **GGUF 로딩 실패** | §2.2 Step 7 에서 model format error | Ollama blob format vs llama.cpp 기대 format 격차 → GGUF 직접 검증 별도 |
| **R-1 hash 불일치** | §2.1 Step 1 또는 §2.4 Step 3 의 sha256sum 변동 | cycle 전체 폐기 + V-1 entry brief §12 옵션 E trigger 강도 ↑ 보고 |
| **R-23 동결 위반** | 측정 중 다른 LLM 호출 / 다른 Claude 세션 / Ollama runner 동시 활성 | noise 정직성 명문 + 측정값 자격 ↓ 보고 (재측정 자격 평가 별도) |
| **github.com 외 도메인 egress** | §2.2 Step 1 외 빌드 중 의외 도메인 ESTABLISHED | §3.2 격리 trace 기록 + 사용자 보고. 결정 입력 자격 평가 별도 |

### 2.6 시간 예측 (정직성 명문)

| 단계 | 예상 시간 | 변동 |
|----|----|----|
| §2.1 사전 점검 | ~10분 | 사용자 sudo prompt 답습 |
| §2.2 빌드 (clone + cmake + make) | ~30분-2시간 | nvcc CUDA 컴파일 시간 hardware-dependent, 첫 빌드 = 2시간 가능, ccache 적중 시 ~30분 |
| §2.3 측정 | ~30분 | 3회 반복 + Ollama cross-check |
| §2.4 종료 보장 | ~5분 | — |
| §2.5 분기 대응 (발생 시) | variable | 빌드 실패·미지원 분기는 시간 예측 불가, 별도 cycle |
| **총 예상** | **~75분-3시간** | 첫 빌드 가정 |

---

## 3. §8 baseline + egress 시점 격리 (R-11 답습)

### 3.1 시점 범위 명문 (V-1 entry brief §8.1 R-3 답습)

- **본 cycle 의 egress = §2.2 Step 1 (github.com clone) 한정** — 그 외 egress = §3.2 격리 분리 보고
- baseline 시점 = (a) §2.1 Step 2 (cycle 직전 snapshot) + (b) §2.4 Step 2 (cycle 직후 snapshot)
- **Ollama egress = 본 cycle 한정 0 검증** (Phase 1·2 답습)

### 3.2 격리 분리 보고 (egress 발생 *기록* 의무)

cycle 종료 후 raw 에 다음 분리 보고:

| 카테고리 | 보고 항목 |
|----|----|
| **본 cycle 의도 egress** | github.com + CDN (Cloudflare/Fastly 추정) ESTABLISHED 횟수·peak 동시 연결 수 |
| **본 cycle 의도 외 egress** | 예: apt repo (의존성 설치 시) / 빌드 도구 자동 업데이트 등 |
| **Ollama egress** | localhost only 유지 검증 (외부 도메인 0) |
| **다른 프로세스 egress** | claude (본 세션) / sshd / tailscaled — 본 cycle 무관 baseline (Phase 1·2 답습) |

---

## 4. 보고 항목 (raw 한정, R-6 답습)

🔴 **R-6 답습**: PASS/FAIL framing 금지. raw 보고만. 3+1 합의 BLOCKING 3 (BW 본질 단정 금지) 답습.

### 4.1 빌드 결과

| 항목 | 형식 |
|----|----|
| llama.cpp commit (SHA + tag) | verbatim 인용 |
| 빌드 환경 (gcc/g++/cmake/nvcc 버전) | verbatim |
| GB10 compute_cap | verbatim |
| 빌드 옵션 (cmake flag) | verbatim |
| 빌드 시간 | wall-clock 측정 |
| 빌드 산출물 (binary 경로, 크기) | verbatim |
| Qwen3-Next 지원 코드 검색 결과 | 파일·라인 인용 |

### 4.2 측정 결과 (Phase 1·2 답습 표 형식)

| 항목 | 형식 |
|----|----|
| llama.cpp decode tok/s (3회) | mean ± std, std/mean (%) |
| Ollama decode tok/s 재현 | mean ± std (Phase 1 7.83 답습 비교) |
| 격차 비율 | (llama.cpp - Ollama) / Ollama × 100% |
| GPU 활용도 (측정 中) | nvidia-smi sm_pct / mem_pct / pwr (Phase 1 답습 한계 — 모두 0 가능) |
| 측정 환경 (R-23 동결 / R-1 hash) | verbatim |
| layer-step breakdown (가능 시) | verbatim verbose log 인용 |

### 4.3 분기점 평가 입력 (raw 한정)

| 분기 | 격차 | (iii) 평가 | (iv) 평가 | (v) 평가 | 새 가설 #6 |
|----|----|----|----|----|----|
| 격차 < 20% | — | (iii) 부정 | carry-over | 강화 | 약화 (llama.cpp 양호) |
| 격차 20-50% | — | (iii) 부분 | carry-over | 부분 | 부분 |
| 격차 > 50% | — | (iii) 강화 | carry-over | 약화 | 부분 |
| 빌드/실행 실패 | — | 격차 미측정 | 격차 미측정 | 격차 미측정 | **강한 강화** |

### 4.4 raw 보존 (R-22 답습)

| 항목 | 경로 |
|----|----|
| 빌드 로그 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-build-log.txt` (clone + cmake + make + verify) |
| 측정 로그 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-measure-log-{1,2,3}.txt` (3회 반복 raw) |
| Ollama 재측정 로그 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-ollama-rerun-log.txt` |
| baseline 전/후 snapshot | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-egress-baseline-{pre,post}.json` |
| Phase 3 종합 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-summary.json` |

---

## 5. 정직성 한계 (R-6·B-F13 답습)

| 한계 | 영향 |
|----|----|
| **llama.cpp master 빌드 시점 의존** | 빌드 commit SHA 명문 의무. 재현 시 동일 commit 사용 권고. Qwen3-Next 지원 PR merge 시점 변동 가능 (정직성 명문) |
| **GB10 sm_121 검증 0** | llama.cpp master 가 sm_120/121 명시 지원 verify 0건 — 빌드 옵션 `-DCMAKE_CUDA_ARCHITECTURES='120;121'` 가 실제 작동하지 않을 가능성. fallback (sm_80 / sm_90) PTX JIT compile 의존 시 성능 격차 발생 가능 |
| **(iv) router overhead 직접 분해 불가** | llama.cpp verbose log 의 분해 정밀도 한계. 직접 분해 불가 시 (iii) 와 결합 효과만 측정 — 가설 (iv) 단독 자격 X |
| **prompt set 답습 한계** | Phase 1 prompt set 재사용 (cache miss 분리 답습) — 다른 prompt 길이·content 에서 격차 변동 가능 |
| **Ollama 재측정 시 noise** | 측정 순서 (llama.cpp 우선 vs Ollama 우선) 가 GPU 캐시·메모리 state 에 영향 가능 — 1회만 측정 또는 별도 cycle |
| **빌드 ccache / 컴파일러 캐시** | 첫 빌드 시간 vs 재빌드 시간 격차 — wall-clock 측정 정확성 한계 (수단 영향) |
| **github.com clone egress 의 redirect chain** | CDN (Cloudflare/Fastly 추정) IP range 추적 = ss 한정 (Phase 2 답습 — iptables 무효) |
| **B hybrid fallback 자격 평가 별도** | 정공법 실패 시 B hybrid (prebuilt binary) fallback 진입 = 사용자 명시 의무 (자동 진입 0) |

---

## 6. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 자격 |
|----|----|----|
| (A) | 본 brief 사용자 검토 → Phase 3 정공법 cycle 실행 명시 승인 → §2.1~§2.4 진행 | brief v1 commit 별도 / 또는 brief 검토 후 곧장 실행 |
| (B) | brief 보강 (누락 항목·절차 정밀화·분기 추가) | brief v2 → 재검토 |
| (C) | Phase 3 cycle 실행 후 → Phase 3 findings (`docs/phase0/jarvis-mvp1-v1-poc-phase3-findings.md` 또는 brief v2 EXECUTED §10) | findings 작성 별도 명시 |
| (D) | Phase 3 결과 후 → **M3·M4 결정 *고정* 합의** cycle (Phase 1+2+3 종합) — 3+1 합의 §6 BLOCKING 1 해소 cycle | 별도 합의 brief + 사용자 명시 |
| (E) | Phase 3 결과 후 → R-15 gap-pull P1 trigger 자격 평가 cycle (R-10 SOP 통과 후) | 별도 brief + 사용자 명시 |
| (F) | Phase 3 결과 후 → 새 가설 #6 (sm_120/121 미지원) 검증 cycle (분기점 결과에 따라) | 별도 brief + 사용자 명시 |
| (G) | B hybrid 변경 (정공법 미진입) | 사용자 명시 — 본 brief v2 또는 별도 brief |

**보안 거버넌스 자동 재개 금지** (비례성, `feedback_proportionate_security_personal_tool` 답습).

**단계별 명시 승인 답습** (`feedback_staged_consensus_workflow`): brief → 사용자 승인 → 실행 → findings → commit → push, 자동 다음 단계 진입 0건.

---

## 7. 산출물 (계획)

본 brief commit 시:
- `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (본 문서)

Phase 3 cycle 실행 *후* 작성 예정 (별도 명시 승인 후):
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-summary.json`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-build-log.txt`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-measure-log-{1,2,3}.txt`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-ollama-rerun-log.txt`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-egress-baseline-{pre,post}.json`
- (findings 별도 명시 시) brief v2 EXECUTED §10 추가 또는 별도 findings 파일

본 brief 작성만으로는 위 raw / findings / commit / push 0건.

---

## 8. 답습 요약 (영구)

- **하는 것**: Phase 3 cycle (C-e 정공법) 운영 절차 식별 + 빌드 egress 시점/범위 격리 + 측정 표준 명문 + 분기점 raw 평가 + 보고 항목 raw 한정
- **하지 않는 것**: llama.cpp 실 빌드 / 측정 / Ollama 데몬 변경 / 모델 pull / config 변경 / M3·M4 결정 *고정* / OllamaBoss·LlamaCppBoss 코드 / 합의 보고서·commit·push / 보안 거버넌스 자동 재개 / gap-pull trigger / B hybrid 자동 진입
- **출처**: 3+1 합의 (`d2d7bf9`) §6 권고 (A) + §3 P-1 계층화 부분 채택 + §5 G-1 hybrid 대안 carry-over + G-2 새 가설 #6 carry-over / M3·M4 결정 합의 `9ddec1b` §5.3 / V-1 entry brief / Phase 1 결과 `2026-05-24-phase1-summary.json` / Phase 2 brief v2 `c66756b` §9 / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `feedback_provider_liquidity` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 5조건 / 헌법 5조 (Provider Liquidity)
