# 자비스 MVP-1 V-1 PoC Phase 3 cycle (C-e 정공법) entry brief (DRAFT v1.1)

> **본 brief = M3·M4 합의 §5.3 + 3+1 합의 (`d2d7bf9`) §6 권고 (A) 정공법 답습 + 3+1 합의 (`e76acc8`) BLOCKING 7 + 권고 25 + NOTE 11 반영.** brief 자체로 **빌드 실행 / 측정 / 합의 보고서 작성 / commit / push** 발생 0건. brief = **(i) 답습** + **(ii) C-e 정공법 실행 절차** + **(iii) 정직성 한계** 식별 한정.

---

**작성일**: 2026-05-24 (v1 `cc145fd`) → 2026-05-24 (v1.1, 3+1 합의 `e76acc8` 반영)
**Status**: **DRAFT v1.1** (사용자 검토 대기). 3+1 합의 `d2d7bf9` 권고 (A) 정공법 채택. 3+1 합의 `e76acc8` BLOCKING 7 + 권고 25 + NOTE 11 반영. 실 빌드·측정 0건.
**진입 단위**: V-1 PoC Phase 1 (`9c6b578`) + Phase 2 (`c66756b`) + 3+1 합의 (`d2d7bf9`) + 3+1 합의 (`e76acc8`) 후 → **Phase 3 cycle (C-e 정공법) 운영 entry**
**cycle 자격 근거**: 3+1 합의 `d2d7bf9` §6 BLOCKING 1 (결정 *고정* 자격 미충족, Phase 3 의무) + M3·M4 §5.3 C-e 명문 + 3+1 합의 `d2d7bf9` §3 P-1 L3·L4 Phase 3 후 재 합의 + Phase 2 §9.8 (iii)(iv) 미해소 + 3+1 합의 `e76acc8` brief v1.1 진입 자격 충족 (BLOCKING 7 verbatim 반영 후)
**선행 답습**:
- Phase 1 결과 (`v1-poc-raw/2026-05-24-phase1-summary.json`) — A-진단 roofline 90~120 tok/s + C-c cache miss 분리
- Phase 2 §9 EXECUTED — F1 (i) 부정 (HF "3B activated" verbatim) + (ii) 명칭 정정 (Gated DeltaNet, NOT classical SSM) + (v) 강한 evidence
- 3+1 합의 `d2d7bf9` §6 BLOCKING 5 + §3 P-1 계층화 부분 채택 + §5 G-1 C hybrid 대안 carry-over + G-2 새 가설 #6 (sm_120/121 미지원) carry-over
- 3+1 합의 `e76acc8` BLOCKING 7 (R-1~R-7) + 권고 25 (R8~R25 + R-N1~) + NOTE 11

**답습 권위 한계**: 본 brief = *Phase 3 운영 entry* DRAFT — M3·M4 결정 *고정* / OllamaBoss·LlamaCppBoss 코드 / setup 변경 / 합의 보고서 작성 / gap-pull 실행 = 별도 단계 (사용자 명시)

---

## 0. 범위

### 0.1 사용자 진입 명령 답습 (2026-05-24)

> "T 이후 R 진행" — 3+1 합의 (`d2d7bf9`) §6 권고 (A) 정공법 채택 + 본 entry brief 작성. brief 자체 = 빌드 실행 0건. 합의 `e76acc8` 후 brief v1.1 보강.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**:
  1. Phase 3 cycle (C-e 정공법) 의 *실행 절차* 운영화 (§2)
  2. 빌드 egress 시점·범위·종료 보장 정의 (§3) + **의도-외 egress 사전 차단 거버넌스** (§3.0, R-7)
  3. §8 baseline 점검 절차 (egress 직전·직후, §4)
  4. 보고 항목 정의 — raw 한정, PASS/FAIL framing 금지 (§5)
  5. 정직성 한계 식별 (§6)
  6. 3+1 합의 BLOCKING 5건 (`d2d7bf9`) + 7건 (`e76acc8`) 답습 패턴 명문

- **하지 않는 것** (3+1 합의 §7 + 본 brief 영구 답습):
  - ❌ llama.cpp 실 빌드 / 측정 (본 brief = 절차 식별만)
  - ❌ Ollama 데몬 재시작·kill·signal (R-1 답습. **`/api/stop` runner 호출 boundary 별도 명문**, §2.3 Step 2)
  - ❌ 모델 pull (기존 qwen3-coder-next GGUF 재사용)
  - ❌ Ollama config 변경 (`OLLAMA_*` env 영구 설정 X)
  - ❌ M3·M4 결정 *고정* (Phase 3 raw 보고만, 결정은 Phase 1+2+3 종합 후 별도 합의)
  - ❌ `OllamaBoss` / `LlamaCppBoss` 코드 작성 (트랙 B = Phase 3 측정 후 별도)
  - ❌ gap-pull *실행* (R-10 SOP 통과 + P1 trigger 자격 평가 별도 cycle)
  - ❌ 합의 보고서·commit·push (Phase 3 raw → findings → 별도 합의)
  - ❌ 보안 거버넌스 (credential·4축·BI-*) 자동 재개

### 0.3 비례성 답습

본 cycle = 본인용 개인 개발 툴의 inference engine 비교 측정 한정 (~75분-3시간). `feedback_proportionate_security_personal_tool` 답습 — llama.cpp 빌드는 일상적 OSS 빌드 행위. 빌드 egress (github.com clone + apt deps 가능) 의 위생 점검 (R-11 답습) 은 *측정 정직성* 입력 목적, 보안 거버넌스 자동 재개 trigger 아님. 본 cycle 의 egress 시점 = §2.2 Step 1 (github.com clone) **only** 사전 계획. apt deps 발생 시 = R-3 시점 격리 의무 + 사용자 명시 재확인 (자동 진입 0). cmake 자체 FetchContent egress 가능성 = §3.0 사전 차단 거버넌스 (R-7).

### 0.4 정공법 채택 근거 (vs B hybrid)

3+1 합의 `d2d7bf9` §6 권고 (A) 정공법 선택 근거:
- Provider Liquidity 답습 강도 ↑ (실 빌드 = LlamaCpp endpoint 동작 *실측* 검증, B hybrid prebuilt binary = 출처 SHA 검증 의존)
- (iii) Ollama vs llama.cpp 분리 = **빌드/플래그 통제 가능** (정공법) > prebuilt binary 의 의도 미상 옵션
- (iv) router overhead 추정 강도 ↑ (정공법은 빌드 옵션 (CUDA backend + Q4_K_M kernel + KV cache size 등) 통제로 (iv) 영향 격리 가능)
- C 신규 가설 #6 (sm_120/121 미지원) 검증 = llama.cpp 도 동일 격차 시 강화 / llama.cpp 양호 시 부정 — 정공법 결과의 신뢰도 ↑
- **trade-off**: 시간 ~75분-3시간 (B hybrid 의 ~20분 대비 4-10× 이상). 단 본 cycle = **결정 *고정* 자격 평가**, 시간 비용 대비 evidence 강도 우선

**B hybrid 잔여 옵션**: 정공법 빌드 실패 / GB10 sm_120/121 미지원으로 빌드 불가 / CUDA backend 비활성화 등 contingency 발생 시 B hybrid (prebuilt binary) fallback 진입 — 별도 명시 승인 의무. B hybrid prebuilt binary 출처/sha 검증 SOP = 별도 cycle (NOTE N-5).

**정공법 *후* B hybrid 비교 cycle carry-over** (`e76acc8` 권고 R19): 정공법 측정 후 B hybrid prebuilt binary 와 격차 비교 = 빌드 옵션 영향 격리 강도 ↑. 별도 brief + 사용자 명시. → §6 옵션 (J).

---

## 1. Phase 3 cycle 목적

### 1.1 1차 목적 — (iii)(iv) 미해소 분리

**가설 (iii) Ollama 0.20.4 hybrid 효율성 (vs llama.cpp)**:
- Phase 2 §9.8: "Phase 3 C-e 측정 필요" verbatim
- 측정 대상: 동일 GGUF / 동일 prompt / 동일 환경에서 llama.cpp decode tok/s vs Ollama 7.83 tok/s
- **분기점 후보** (`e76acc8` R-4 답습 — raw 측정값 + 해석 분리 보고, 자동 평가 흐름 0건, 합의 입력 한정):
  - 격차 < 20%: (iii) 부정 *후보 입력* → (v) BW 본질 *후보 강화* + (iv) router overhead 가설 carry-over
  - 격차 20-50%: (iii) + (v) 복합 *후보 입력* (Agent C Q3 (b) 답습)
  - 격차 > 50%: (iii) *후보 강한 입력* → (v) *후보 약화* → Ollama 구현 비효율 본질 가설 우선
  - llama.cpp 빌드/실행 실패: 가설 #6 *후보 입력* (단정 framing 금지, §1.3 답습)

🔴 **R-4 답습**: 본 분기점 라벨 = **후속 합의의 입력 후보** 한정, *자동 평가 흐름 0건*. 18% / 22% 의 cliff edge 라벨 = R-6 답습 위반 risk → §4.3 raw 측정값 + 해석 분리 보고 의무.

**가설 (iv) Qwen3-Next router/gating overhead**:
- Phase 2 §9.8: "Phase 3 별도 측정"
- Phase 3 정공법으로 *직접* 측정 어려움 (Ollama·llama.cpp 모두 router timing 분해 instrumentation 미제공)
- *간접* 측정: llama.cpp 의 verbose log (--verbose / --log-disable false) 에서 token-step time breakdown 추출 시도. **빌드 옵션 의존** (`-DGGML_PERF=ON` 또는 commit-version 의존, §2.3 Step 5 사전 verify 의무, 권고 R9)
- **(iv) 단독 분해 후보 수단** (본 cycle *외*, carry-over, 권고 R10): (a) PyTorch/transformers eager mode + `torch.profiler` 의 gating module forward hook (환경 격리 trade-off 있으나 (iv) 단독 자격 ↑), (b) NSight Systems/Compute 의 CUDA kernel-level timing, (c) vLLM/SGLang built-in tracing. 본 cycle = llama.cpp verbose log *간접* 분해 한정, (iv) 단독 측정 자격 X 답습
- 한계: 직접 분해 불가 시 (iii) 와 (iv) 결합 효과만 측정 가능 → 정직성 명문 의무

### 1.2 부차 목적 — BLOCKING 입력

| BLOCKING (출처) | Phase 3 입력 |
|---------|-------------|
| `d2d7bf9` 1 (결정 고정 자격 미충족) | C-e 결과 입력 후 Phase 1+2+3 종합 합의 → 자격 평가 |
| `d2d7bf9` 2 (R-10 일반화 SOP 미정) | Phase 3 결과 자체와 무관 (별도 SOP cycle) |
| `d2d7bf9` 3 (BW 본질 단정 금지) | (iii) 분리 후 (v) 강도 재평가 입력 |
| `d2d7bf9` 4 (SSM 명명 0건) | M3 결정 문구 수정 = 결정 *고정* 단계 별도 |
| `d2d7bf9` 5 (rollback trigger 명문) | 계층화 고정 시 ADR-011 §2.1 답습, Phase 3 결과 입력 후 |
| `e76acc8` 1~7 (R-1~R-7) | 본 brief v1.1 verbatim 반영 — Qwen3-Next verify·repo URL·R-1 mid-cycle anchor·분기점 framing·#6 framing·compute_cap 실측·egress 사전 차단 |

### 1.3 새 가설 검증 (`d2d7bf9` §5 G-2 carry-over + `e76acc8` R-5)

**가설 #6 — Qwen3-Next 특수 구조 (Gated DeltaNet + MoE hybrid) GB10 sm_120/121 미지원 가능성**:
- 검증 방법: llama.cpp 빌드 + 실행 시 CUDA backend 활성·sm_120/121 kernel 컴파일 verify
- **R-5 답습** (framing 약화) — 빌드 실패 원인 6+ 분포 ((a) gcc/cmake/cuda toolkit 미달 / (b) 디스크 부족 / (c) 코드 미머지 / (d) sm_120/121 미인식 / (e) Qwen3-Next arch 미지원 / (f) Gated DeltaNet kernel 미지원). 빌드 실패 시 *원인 분리 후* #6 가설 *후보 입력* 자격. sm_120/121 *명시 거부* error message verbatim 확보 시에만 #6 *후보 강화* 입력
- **분기점 후보** (자동 평가 흐름 0건):
  - 빌드 성공 + 실행 성공: #6 *후보 약화* (sm_120/121 지원 형태로 작동)
  - 빌드 성공 + 실행 실패 (런타임 kernel 누락 등): #6 *후보 입력* → **Qwen3-30B-A3B 대조군 cycle** (R-5 변수 분리, classical MoE + dense, SSM 미포함) 별도 brief 의무. 대조군 정상 작동 시 → (e)(f) 가설 강화 / 동일 실패 시 → (d) sm_120/121 가설 강화. **별도 Phase 3.5 후보 cycle, 사용자 명시 별도**
  - 빌드 실패 (sm_120/121 미인식 명시 error): #6 *후보 강한 입력* → B hybrid fallback 또는 Phase 4

**가설 #6 변수 분리 한계** (R-5 정직성 명문): Qwen3-Next 단일 모델로 (a) sm_120/121 미지원 vs (b) Gated DeltaNet kernel 미지원 vs (c) Qwen3-Next arch 미지원 분리 불가. 빌드/실행 실패 시 대조군 모델 (Qwen3-30B-A3B 권고) 으로 sm_120/121 검증 = 별도 mini-cycle (Phase 3.5 후보, brief v1.1 carry-over). 본 cycle 단독 자격 X.

**Blackwell PTX forward-compat 한계** (R-5 정직성 명문): sm_120/121 의 PTX forward-compat 가능 여부 자체 미verify — fallback (sm_80 / sm_90) PTX JIT compile 의존 시 성능 격차 발생 가능. JIT fallback 자체가 작동하지 않을 risk (Blackwell 은 Hopper sm_90 의 PTX 직접 재사용 불가 영역 가능). cuobjdump SASS 포함 verify (R-6, §2.2 Step 6 강화) 로 간접 evidence 확보.

### 1.4 Phase 3 단독 자격 한계

- 본 cycle 결과만으로 M3·M4 결정 *고정* 자격 X (3+1 합의 §3 P-1 답습)
- Phase 1+2+3 종합 합의 cycle 별도 필수
- (iv) router overhead 직접 분해 불가 시 (iii) 와 결합 효과만 측정 — 정직성 명문 의무
- 분기점 라벨 = 후속 합의의 *입력 후보* 한정, *자동 평가 흐름 0건* (R-4 답습)

---

## 2. C-e 실행 절차

### 2.1 사전 점검 (빌드 *전*, ~10분)

| Step | 명령 / 행위 | 산출물 | 성공기준 |
|----|----|----|----|
| 1 | R-1 anchor (Phase 3 시작 시점) — `sudo sha256sum /proc/3375/exe` (사용자 명시 prompt). **회차 번호 = Phase 1·2 누계 회수 + 1** (R-23 권고, 실제 회수는 measurement 직전 검증 의무) | hash | Phase 1·2 hash `ce95c47...8877b10` 와 일치 |
| 2 | §8 baseline pre — `sudo ss -tan state established` + `date -Iseconds` | 외부 ESTABLISHED 목록 + anchor 시각 | github.com 도메인 0건 확인 (cycle-前) |
| 3 | R-23 환경 동결 — `ps -ef \| grep -E 'claude\|ollama' \| grep -v grep` + `nvidia-smi` | 본 Claude 세션 only + GB10 baseline | 다른 LLM 호출 0건 |
| 4 | **빌드 환경 verify + compute_cap 실측** (R-6) — `gcc --version`, `g++ --version`, `cmake --version`, `nvcc --version`, `nvidia-smi --query-gpu=name,driver_version,compute_cap --format=csv`. **compute_cap 단정 표현 0** (예측값 미사용, 실측값 verbatim 인용) + ccache 가용 확인 (`which ccache; ccache --version 2>/dev/null`, 권고 R14) | toolchain 버전 + GB10 compute_cap 실측값 + ccache 상태 | gcc ≥ 11, cmake ≥ 3.18, nvcc ≥ 12.4. **compute_cap 실측값 verbatim 인용 후 §2.2 Step 4 cmake variable 결정 의무** |
| 5 | 디스크 공간 — `df -h /home /tmp` | 가용 공간 | 빌드 ~10GB + GGUF 재사용 → 가용 ≥ 30GB 권고. 부족 시 §2.5 표 새 분기 발동 |
| 6 | Ollama 메타 답습 — `curl -s http://127.0.0.1:11434/api/show -d '{"name":"qwen3-coder-next:latest"}' \| jq -r '.modelfile' \| grep -i FROM` | GGUF blob 경로 | `/root/.ollama/models/blobs/sha256-30e51a7cb1cf1333b9e298b90b4c7790fe2572d8736b002482a0ac96328a2ffb` 확인 (Phase 2 §9.1 답습) |

### 2.2 llama.cpp 빌드 (egress 발생, ~30분-2시간)

| Step | 행위 | 명령 / 도구 | egress |
|----|----|----|----|
| **1** | **clone** (R-2 ggml-org canonical) | `cd ~/src && git clone https://github.com/ggml-org/llama.cpp.git llama.cpp` (canonical upstream; `ggerganov/llama.cpp` 는 historical alias로 redirect 의존). clone 직후 `cd llama.cpp && git remote -v` 로 fetch URL verbatim 기록 + `git ls-remote https://github.com/ggml-org/llama.cpp HEAD` peeled SHA cross-check | github.com (~30MB) |
| **1.5** | **submodule 사전 식별** (R-7) | `git submodule status` 로 llama.cpp submodule 식별. 추가 github.com egress *예측* 후 사용자 명시 후 `git submodule update --init --recursive` (submodule 존재 시 한정) | github.com (submodule 의존, 사용자 명시) |
| 2 | **commit anchor** | `git log -1 --format='%H %s' > /tmp/llamacpp-build-anchor.txt && git describe --tags --abbrev=8` | (egress 0) — 빌드 시점 commit 고정 |
| **3** | **Qwen3-Next 지원 verify** (R-1 강화) | (a) `grep -rniE 'qwen3.?next\|qwen3_?next' . --include='*.cpp' --include='*.h' --include='*.py' --include='*.md' \| head -40` (b) `grep -rniE 'delta.?net\|gated.?delta\|linear.?attention' src/ ggml/ --include='*.cpp' --include='*.h' \| head -20` (c) `grep -rni 'LLM_ARCH' src/llama.cpp src/llama-arch.* 2>/dev/null \| grep -i qwen \| head -10` (d) `python3 convert_hf_to_gguf.py --help 2>&1 \| grep -i qwen` (e) docs/ops.md / docs/build.md 내 supported architecture 표 검색 | (egress 0) | (a) 또는 (c) 적중 시 master 직접 지원 강한 evidence / (b) 단독 적중 시 kernel 만 있고 architecture 미지원 가능성 → §2.6 분기 |
| **4** | **CUDA backend 빌드** (R-6 compute_cap 실측값 사용 + R-7 FetchContent 차단 시도) | `cmake -B build -DGGML_CUDA=ON -DCMAKE_CUDA_ARCHITECTURES="<§2.1 Step 4 측정 compute_cap × 10 정수>" -DCMAKE_BUILD_TYPE=Release -DFETCHCONTENT_FULLY_DISCONNECTED=ON` (값 결정 = §2.1 Step 4 실측 후. 다중 nominate 시 `"120-real;120-virtual"` 또는 `"120;121"` 형식 cmake 3.24+ docs 참조. ccache 가용 시 `-DCMAKE_C_COMPILER_LAUNCHER=ccache -DCMAKE_CXX_COMPILER_LAUNCHER=ccache` 추가, 권고 R14). cmake configure 출력에서 `-- CUDA architectures: ...` 행 verbatim 기록 의무. `FETCHCONTENT_FULLY_DISCONNECTED` 적용 불가 시 = 정직성 명문 (cmake build 중 의도-외 egress 가능, R-7) | (egress 0 목표) — local toolchain. fetch 의존성 시 빌드 실패 → 의존성 식별 후 사용자 명시 진행 |
| **5** | **apt snapshot pre + 컴파일** (R-7) | (a) 빌드 시작 *전* `sudo apt list --upgradable 2>/dev/null \| wc -l` + `dpkg -l \| wc -l` snapshot. (b) `DEBIAN_FRONTEND=noninteractive cmake --build build --config Release -j$(nproc)` — apt prompt 자동 yes 회피, cmake/make 의 *non-interactive* 강제. (c) 빌드 *후* 동일 snapshot 비교 — 시스템 패키지 변동 0 확인. 변동 시 *발생 후* 격리 보고 + 사용자 보고 + cycle 일시 정지 | (egress 0 목표) — cmake/make 가 `sudo apt install` 자동 호출 시도 = 즉시 정지 + 사용자 명시 의무 |
| **6** | **빌드 산출물 verify + sm_121 SASS 포함 verify** (R-6) | `ls -la build/bin/llama-cli build/bin/llama-server 2>&1` + `./build/bin/llama-cli --version 2>&1` + `cuobjdump --list-elf build/bin/llama-cli \| grep -E 'sm_12[01]' 2>&1` (또는 `nvcc --dryrun --gpu-architecture=sm_121 ...` cross-check) | (egress 0) | binary 존재 + version 출력에서 `CUDA: 1` 또는 `with CUDA backend` 또는 `ggml-cuda` 식별자 verbatim 인용 (권고 R24) + sm_120/121 SASS 포함 verify. sm_121 SASS 미포함 시 = sm_80/sm_90 fallback 가능성 → 빌드 결과 정직성 명문 + #6 가설 *간접 후보 입력* (단정 framing 금지) |
| **6.5** | **GGUF metadata cross-check** (R-1) | `./build/bin/llama-gguf /root/.ollama/models/blobs/sha256-30e51a7cb1cf1333b9e298b90b4c7790fe2572d8736b002482a0ac96328a2ffb r 2>&1 \| head -80` (또는 `gguf-dump.py` 동등) | (egress 0) | `general.architecture` verbatim + `qwen3next.*` key 존재 인식 verify. arch 인식 0건 시 §2.6 가설 #6 *후보 입력* raw + Qwen3-30B-A3B 대조군 cycle 필요성 강화 |
| 7 | **GGUF 로딩 verify** | `./build/bin/llama-cli -m /root/.ollama/models/blobs/sha256-30e51a7cb1cf1333b9e298b90b4c7790fe2572d8736b002482a0ac96328a2ffb -p "test" -n 1 --no-display-prompt 2>&1 \| tail -20` | (egress 0) | 모델 로딩 + 1 token 생성 성공. Qwen3-Next 미지원 시 fail → §2.6 분기 |
| **8** | **R-1 anchor mid-cycle** (R-3 신규) — 빌드 종료 직후·측정 시작 *전* `sudo sha256sum /proc/3375/exe` | hash | Phase 1·2 hash 와 일치. **불일치 시 측정 단계 skip + cycle 일시 정지 + 사용자 보고** (빌드 산출물은 보존, 다음 cycle 재사용 자격 평가 별도). cycle 전체 폐기 0건 |

**egress 격리 보장 (§3 R-11 답습 + §3.0 R-7 보강)**:
- §2.2 Step 1·1.5 = github.com clone (+ submodule 의존) only — 다른 도메인 0 verify (§3 격리)
- Step 4 = local toolchain (gcc/g++/nvcc) + `FETCHCONTENT_FULLY_DISCONNECTED=ON` 시도 — egress 0 목표
- Step 5 = local compile + apt snapshot pre/post — 시스템 패키지 변동 0 확인 의무
- Step 6 ~ 8 = local file read / hash — egress 0
- 의존성 누락 시 apt install 필요한 경우 = ubuntu repo egress (Step 1·1.5 외 egress 발생 시 *cycle 일시 정지* + 사용자 명시 재확인 의무)

### 2.3 측정 (egress 0, ~30분)

| Step | 행위 | 명령 / 도구 | 측정 항목 |
|----|----|----|----|
| 1 | R-23 동결 재확인 (측정 *직전*) | `ps -ef \| grep -E 'claude\|ollama\|llama-cli' \| grep -v grep` | 본 Claude + llama-cli 만 ✓ (Ollama runner = idle 또는 자연 idle, R-8 boundary 답습) |
| **2** | **Ollama runner 자연 idle 우선** (R-8 boundary) | `/api/ps` 가 빈 상태이거나 5분 KeepAlive 자연 만료 대기. `/api/stop` 호출 = §0.2 boundary 별도 명문 — Ollama 0.20.4 의 `/api/stop` 가 PID 3375 데몬 자체 변동을 *유발 안 함* (runner subprocess 한정) 의 사전 verify (`sha256sum /proc/3375/exe` 호출 전후 일치 확인) 없는 한 호출 *금지*. 자연 idle 후 `/proc/3375/exe` hash 변동 0 확인 의무 | runner 종료 ✓ (메모리 경합 회피) + 데몬 PID 3375 불변 ✓ |
| **3** | **llama.cpp decode 측정** (R-12 + R-25 권고) | `./build/bin/llama-cli -m <GGUF> -p "<Phase 1 prompt set 답습>" -n 256 --no-display-prompt -ngl <실제 layer 수, 권고 R25 - Qwen3-Next 48 layer 가정 → `-ngl 48` 권고, build/bin/llama-cli 의 metadata dump 후 실제 layer 수 verify 의무> -c <Phase 1 답습 context size, 권고 R12 - `-c 8192`> 2>&1 \| tee /tmp/llamacpp-measure-2k-1.log` | tok/s decode (eval time / n_tokens 추출) |
| **4** | **반복 측정 (3회 × 2 prompt sub-set)** (권고 R21) | Step 3 × 3 회 × (2k Phase 1 답습 + 8k long-context sub-set). 시각 anchor 별 기록 | tok/s mean ± std, std/mean (안정성), prompt 길이별 격차 비교 |
| 5 | (선택) **router overhead 간접 측정** (권고 R9 + R10 carry-over) | `./build/bin/llama-cli ... --verbose --log-disable false 2>&1` 의 layer-step breakdown 추출. **분해 가능 여부는 빌드 옵션 (`-DGGML_PERF=ON` 또는 commit-version 의존) + master 시점 의존, *직전* 1회 dry-run 후 분해 가능 여부 확정 의무** (권고 R9). 분해 불가 시 정직성 명문 + (iv) 단독 자격 X 답습 (R10 carry-over) | per-layer time (CUDA kernel call breakdown 시도). 분해 불가 시 정직성 명문 |
| **6** | **Ollama 재측정 (cross-check, 권고 R11 한정)** | Ollama runner 재가동 (데몬 PID 3375 불변 ✓ 확인 후 `/api/generate` 호출로 자연 reload) 동일 prompt 동일 환경 1회 측정 (statistical power 낮음 명문). 별도 cycle 분리 = 권고 R11. Phase 1 mean ± std (7.83 ± 0.36) 의 ±2σ 범위 (7.11~8.55) 내 = 재현성 일관 evidence. 범위 외 = noise (측정 순서 + GPU cache state) 정직성 명문 | Phase 1 답습 — 7.83 tok/s 재현 검증 (1회, evidence 강도 약함 명문) |
| **7** | 측정 직후 anchor (R-3 회차 +1) | `sudo sha256sum /proc/3375/exe` (R-1 anchor mid-cycle 다음 회차) + `date -Iseconds` | hash 일관 ✓ |

**측정 표준 명문** (R-12 + R-21 + R-25 반영):
- 동일 GGUF (Ollama blob sha256-30e51a7cb1cf...8a2ffb)
- 동일 prompt set (Phase 1 답습) — 단, prompt 길이 sub-set 다양화 (2k + 8k, 권고 R21)
- 동일 환경 (R-23 동결, GB10 idle, 다른 LLM 호출 0)
- `-ngl <실제 layer 수>` (모든 layer GPU offload, KV cache GPU 우선). Qwen3-Next 48 layer 가정 → `-ngl 48` 권고 (build/bin/llama-cli metadata dump 후 실제 layer 수 verify 의무, 권고 R25)
- `-c 8192` (Phase 1 답습 context size, 권고 R12)
- `-n 256` token 생성 (Phase 1 답습)
- 3회 반복 × 2 sub-set (std/mean 안정성 평가)
- KV cache 메모리 (Q4_K_M 51.7GB GGUF load + KV cache ~수 GB) vs GB10 unified memory ~121GB 헤드룸 — overhead 발생 시 swap risk 0건 verify 의무 (권고 R12)

### 2.4 종료 보장 + §8 cycle-後 baseline (~5분)

| Step | 명령 | 성공기준 |
|----|----|----|
| 1 | llama-cli 종료 verify | `ps -ef \| grep llama-cli \| grep -v grep` 0건 |
| 2 | §8 baseline post | `sudo ss -tan state established` + `date -Iseconds` | cycle-前 대비 변동 분석 (cycle-中 의도 egress = github.com only) |
| **3** | R-1 anchor 종료 (R-3 회차 +1) — Phase 3 직후 | Phase 1·2 hash 와 일치 |
| 4 | R-23 환경 동결 사후 | 본 Claude 세션 only 유지 + GB10 idle 복귀 |
| 5 | Ollama 외부 egress 0 재확인 | `sudo ss -tan state established \| grep -E '11434\|34891\|34131'` localhost only |
| **6** | 빌드 산출물 디스크 사용량 + carry-over 자격 (권고 R16) | `du -sh ~/src/llama.cpp/build 2>&1` — 빌드 산출물 carry-over 자격 = *다음 cycle entry brief 에서 별도 평가* (commit SHA 일치 + binary `sha256sum` 일치 verify 의무). 본 cycle 종료 시 = 보존만, 자동 재사용 0 |

### 2.5 실패 분기 (fail-closed, advisory 진행 금지)

| 분기 | 조건 | 대응 |
|----|----|----|
| **빌드 실패 (CUDA backend)** | §2.2 Step 4-5 cmake/make 에러 (sm_120/121 미인식 / CUDA 라이브러리 누락) | 1회 재시도 (clean build) → 재실패 시 cycle 일시 중단 + 사용자 보고. B hybrid fallback 자격 평가 별도. 실패 원인 6+ 분포 분리 후 #6 가설 *후보 입력* 자격 평가 (R-5 답습) |
| **Qwen3-Next 미지원** | §2.2 Step 7 또는 §2.3 Step 3 에서 "unsupported architecture" 또는 비정상 출력 | master branch 미지원 가능 (가설 #6 *후보 입력*, 단정 framing 금지) → fork/PR 검색 별도 cycle (mini-cycle 사전 분리, 권고 R6 carry-over) |
| **GGUF 로딩 실패** | §2.2 Step 7 에서 model format error | Ollama blob format vs llama.cpp 기대 format 격차 → GGUF 직접 검증 = §2.2 Step 6.5 의 `llama-gguf <blob> r` metadata dump → `general.architecture` 값 verbatim 확인 → llama.cpp `src/llama-arch.cpp` enum 과 cross-check |
| **R-1 hash 불일치** (R-3 재작성) | §2.1 Step 1 / §2.2 Step 8 / §2.3 Step 7 / §2.4 Step 3 의 sha256sum 변동 | (i) 발견 시점에 따라 분기 대응: 빌드 *전* 불일치 = cycle 진입 자체 정지 + 사용자 보고. 빌드 *후* / 측정 *전* = 측정 skip + 빌드 산출물 보존 (다음 cycle 재사용 자격 평가 별도) + 사용자 보고. 측정 *중·후* = 측정값 raw 보존 + 자격 ↓ 명문 + 사용자 보고. (ii) V-1 entry brief §12 옵션 E trigger 자격 = 별도 cycle 평가 (사용자 명시), 본 brief 의 *강도 평가 0건* (R-6 답습) |
| **R-23 동결 위반** | 측정 중 다른 LLM 호출 / 다른 Claude 세션 / Ollama runner 동시 활성 | noise 정직성 명문 + 측정값 자격 ↓ 보고 (재측정 자격 평가 별도) |
| **github.com 외 도메인 egress** | §2.2 Step 1·1.5 외 빌드 중 의외 도메인 ESTABLISHED | §3.2 격리 trace 기록 + 사용자 보고. 결정 입력 자격 평가 별도 |
| **apt repo egress (의도-외)** (R-7) | §2.2 Step 5 컴파일 중 cmake/make 가 `sudo apt install` 자동 호출 시도 | 즉시 정지 + apt snapshot 변동 격리 보고 + 사용자 명시 (자동 진행 0). non-interactive 강제 `DEBIAN_FRONTEND=noninteractive` 회피 의무 |
| **디스크 부족** (권고 R15) | §2.1 Step 5 < 30GB 또는 빌드 중 ENOSPC | 빌드 중단 + 빌드 산출물 보존 (가능 시) + 사용자 보고. cleanup 자동 0 |

### 2.6 시간 예측 (정직성 명문)

| 단계 | 예상 시간 | 변동 |
|----|----|----|
| §2.1 사전 점검 | ~10분 | 사용자 sudo prompt 답습 |
| §2.2 빌드 (clone + cmake + make) | ~30분-2시간 | nvcc CUDA 컴파일 시간 hardware-dependent, 첫 빌드 = 2시간 가능, ccache 적중 시 ~30분. **추정 근거 = 일반 x86 환경 데이터 인용 한정, GB10 ARM + nvcc Blackwell sm_120/121 컴파일 실측 0건 — 2시간 상한 미보증** (권고 R14) |
| §2.3 측정 | ~30분 | 3회 반복 × 2 sub-set + Ollama cross-check |
| §2.4 종료 보장 | ~5분 | — |
| §2.5 분기 대응 (발생 시) | variable | 빌드 실패·미지원 분기는 시간 예측 불가, 별도 cycle |
| **총 예상** | **~75분-3시간** | 첫 빌드 가정 |

### 2.7 §2.6 분기점 표 (가설 #6, R-5 신규)

| 분기 | 조건 | 분기 후보 (자동 평가 흐름 0건) |
|----|----|----|
| 빌드 성공 + 실행 성공 (Qwen3-Next) | §2.2 Step 7 + §2.3 Step 3 OK | #6 *후보 약화* (sm_120/121 작동) |
| 빌드 성공 + Qwen3-Next 실행만 실패 | §2.2 Step 7 fail | **Qwen3-30B-A3B 대조 빌드 cycle (별도 brief)** → 정상 시 (a) Qwen3-Next 특화 미지원 강화, 실패 시 (b) sm_120/121 미지원 강화 |
| 빌드 실패 (sm_120/121 미인식 명시 error) | §2.2 Step 4-5 fail + 명시 error verbatim | #6 *후보 강한 입력* → B hybrid fallback 또는 Phase 4 |
| 빌드 실패 (sm_120/121 외 원인) | §2.2 Step 4-5 fail + 명시 error verbatim 부재 | 원인 분리 후 #6 가설 *후보 입력* 자격 평가 별도 (gcc/cmake/cuda toolkit/디스크/코드 미머지 등 6+ 원인) |

---

## 3. §8 baseline + egress 시점 격리 (R-11 답습)

### 3.0 의도-외 egress 사전 차단 거버넌스 (R-7 신규)

빌드 wall-clock 중 사용자 모니터링 minimal 가정 시:
- cmake/make 의 *non-interactive* 모드 강제: `DEBIAN_FRONTEND=noninteractive` env 회피, apt prompt 등장 시 자동 yes 0
- cmake FetchContent 차단 시도: `-DFETCHCONTENT_FULLY_DISCONNECTED=ON` (§2.2 Step 4)
- 의도-외 egress 발생 시 *cycle 일시 정지* (사용자 보고 우선, 자동 진행 0)
- §2.2 Step 5 apt snapshot pre/post = 시스템 패키지 변동 0 확인 의무

### 3.1 시점 범위 명문 (V-1 entry brief §8.1 R-3 답습)

- **본 cycle 의 egress = §2.2 Step 1 (github.com clone) + Step 1.5 (submodule 의존 시) 한정** — 그 외 egress = §3.2 격리 분리 보고
- baseline 시점 = (a) §2.1 Step 2 (cycle 직전 snapshot) + (b) §2.4 Step 2 (cycle 직후 snapshot)
- **Ollama egress = 본 cycle 한정 0 검증** (Phase 1·2 답습)

### 3.2 격리 분리 보고 (egress 발생 *기록* 의무)

cycle 종료 후 raw 에 다음 분리 보고:

| 카테고리 | 보고 항목 |
|----|----|
| **본 cycle 의도 egress** | github.com + CDN (Cloudflare/Fastly 추정) ESTABLISHED 횟수·peak 동시 연결 수 |
| **본 cycle 의도 외 egress** | 예: apt repo (의존성 설치 시) / 빌드 도구 자동 업데이트 / cmake FetchContent 등 — *발생 시 cycle 일시 정지 + 사용자 명시 후 진행* (R-7) |
| **Ollama egress** | localhost only 유지 검증 (외부 도메인 0) |
| **다른 프로세스 egress** | claude (본 세션) / sshd / tailscaled — 본 cycle 무관 baseline (Phase 1·2 답습) |

---

## 4. 보고 항목 (raw 한정, R-6 답습 + R-4 분기점 framing)

🔴 **R-6 답습**: PASS/FAIL framing 금지. raw 보고만. 3+1 합의 `d2d7bf9` BLOCKING 3 (BW 본질 단정 금지) + `e76acc8` R-4 (분기점 라벨 anchor effect) 답습.

### 4.1 빌드 결과

| 항목 | 형식 |
|----|----|
| llama.cpp commit (SHA + tag) | verbatim 인용 |
| `git remote -v` fetch URL (R-2) | verbatim 인용 |
| 빌드 환경 (gcc/g++/cmake/nvcc 버전) | verbatim |
| GB10 compute_cap 실측값 (R-6) | verbatim 인용 (예측값 미사용) |
| 빌드 옵션 (cmake flag) | verbatim — `CMAKE_CUDA_ARCHITECTURES` 값 + `FETCHCONTENT_FULLY_DISCONNECTED` 적용 여부 + ccache 적용 여부 |
| cmake configure 출력 (`-- CUDA architectures:` 행) | verbatim |
| 빌드 시간 | wall-clock 측정 (정직성 — GB10 ARM aarch64 + nvcc Blackwell 실측 0건 명문, 권고 R14) |
| 빌드 산출물 (binary 경로, 크기, sha256sum) | verbatim |
| `--version` 출력 (`CUDA: 1` / `ggml-cuda` 식별자, 권고 R24) | verbatim |
| `cuobjdump --list-elf` sm_120/121 SASS 포함 verify (R-6) | verbatim |
| GGUF metadata dump (`llama-gguf` `general.architecture`, R-1) | verbatim |
| Qwen3-Next 지원 코드 검색 결과 (R-1, grep (a)~(e) 각각) | 파일·라인 인용 |
| apt snapshot pre/post 변동 (R-7) | verbatim 비교 |

### 4.2 측정 결과 (Phase 1·2 답습 표 형식)

| 항목 | 형식 |
|----|----|
| llama.cpp decode tok/s (3회 × 2 sub-set) | mean ± std, std/mean (%) per sub-set |
| Ollama decode tok/s 재현 (1회, 권고 R11) | mean (Phase 1 7.83 ± 0.36 답습 비교, ±2σ 범위 7.11~8.55 내/외) |
| 격차 비율 (raw, R-4) | (llama.cpp - Ollama denominator) / denominator × 100% — *raw 수치만, 라벨 0*. **denominator = Phase 1 mean (7.83) + Phase 3 §2.3 Step 6 재측정값 (가능 시) *양쪽 보고*** (B-S2 통합, 선택 0건). 양값 격차 자체가 noise 평가 입력 |
| 격차 신뢰구간 | std propagation 기반 ±% — 작을수록 (iii) 분리 강도 ↑ |
| GPU 활용도 (측정 中) | nvidia-smi sm_pct / mem_pct / pwr (Phase 1 답습 한계 — 모두 0 가능) |
| 메모리 압박 (측정 中, 권고 R22) | `/proc/<pid>/status` VmRSS/VmPeak polling + `/proc/meminfo` MemAvailable (GB10 unified memory 답습, nvidia-smi 한계 분리 보완) |
| 측정 환경 (R-23 동결 / R-1 hash) | verbatim |
| layer-step breakdown (가능 시, 권고 R9) | verbatim verbose log 인용 — 빌드 옵션 의존 명문 |

### 4.3 raw 측정값 + 해석 분리 보고 (R-6 + R-4 답습, 분기점 라벨 anchor effect 제거)

🔴 **R-4 답습**: 분기점 라벨 (격차 <20% / 20-50% / >50%) 자체가 anchor effect / R-6 위반 risk. 본 brief = raw 보고 한정. 가설 평가는 *Phase 1+2+3 종합 합의 cycle* 에서 별도 진행 (3+1 합의 `d2d7bf9` §3 P-1 답습). 본 brief §1.1 의 분기점 라벨 = *후속 합의의 입력 후보* 한정, *자동 평가 흐름* 0건.

**raw 보고 형식** (라벨 0):

| 항목 | 형식 |
|----|----|
| llama.cpp decode tok/s (per sub-set) | mean ± std, std/mean (3회) |
| Ollama 재현 tok/s | mean ± std (Phase 1 답습 비교, denominator 양값) |
| 격차 비율 | raw 수치만, 라벨 0 |
| 격차 신뢰구간 | std propagation ±% |
| layer-step breakdown (가능 시) | verbose log verbatim (PASS/FAIL framing 0) |

**(iii)(iv)(v)(#6) 가설 평가**: 본 brief = raw 보고 한정. 가설 평가는 *Phase 1+2+3 종합 합의 cycle* 에서 별도 진행 (3+1 합의 `d2d7bf9` §3 P-1 답습). §1.1·§2.7 의 분기점 라벨 = *후속 합의의 입력 후보* 한정, *자동 평가 흐름* 0건.

### 4.4 raw 보존 (R-22 답습)

| 항목 | 경로 |
|----|----|
| 빌드 로그 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-build-log.txt` (clone + cmake + make + verify + cuobjdump + llama-gguf) |
| 측정 로그 (2k sub-set) | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-measure-2k-{1,2,3}.txt` (3회 반복 raw) |
| 측정 로그 (8k sub-set) | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-measure-8k-{1,2,3}.txt` (3회 반복 raw, 권고 R21) |
| Ollama 재측정 로그 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-ollama-rerun-log.txt` |
| apt snapshot pre/post | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-apt-snapshot-{pre,post}.txt` (R-7) |
| baseline 전/후 snapshot | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-egress-baseline-{pre,post}.json` |
| Phase 3 종합 | `docs/phase0/v1-poc-raw/2026-05-2X-phase3-summary.json` |

---

## 5. 정직성 한계 (R-6·B-F13 답습 + `e76acc8` R-3/R-5/R-7/R-17 신규)

| 한계 | 영향 |
|----|----|
| **llama.cpp master 빌드 시점 의존** | 빌드 commit SHA 명문 의무. 재현 시 동일 commit 사용 권고. Qwen3-Next 지원 PR merge 시점 변동 가능 (정직성 명문). fork/PR 식별 mini-cycle = 권고 R6 carry-over |
| **llama.cpp upstream repo 이관 (R-2)** | `ggerganov/llama.cpp` → `ggml-org/llama.cpp` 이관 사실 — 사용 URL 의 redirect 의존성 = clone 직후 `git remote -v` + `git log -1 commit author/committer` verbatim 기록 의무. 본 분석 = 외부 fetch 0 한정, redirect 작동 verify 0건 |
| **GB10 sm_121 검증 0 + Blackwell PTX forward-compat 미verify (R-5)** | llama.cpp master 가 sm_120/121 명시 지원 verify 0건 — 빌드 옵션 `-DCMAKE_CUDA_ARCHITECTURES` 가 실제 작동하지 않을 가능성. fallback (sm_80 / sm_90) PTX JIT compile 의존 시 성능 격차 발생 가능. Blackwell sm_120 의 PTX forward-compat boundary 자체 미verify — JIT fallback 작동 가정 0건. cuobjdump SASS 포함 verify (§2.2 Step 6 강화) 로 간접 evidence 확보 |
| **(iv) router overhead 직접 분해 불가 + 대안 후보 미실행 (R10 carry-over)** | llama.cpp verbose log 의 분해 정밀도 한계. 직접 분해 불가 시 (iii) 와 결합 효과만 측정 — 가설 (iv) 단독 자격 X. **(iv) 단독 분해 후보 수단** (본 cycle *외*): (a) PyTorch/transformers `torch.profiler` forward hook, (b) NSight Systems/Compute, (c) vLLM/SGLang tracing — 모두 본 cycle 외 carry-over. 본 cycle 의 (iv) 평가 = 간접 + 결합 효과 한정. (iv) 단독 결정 *고정* 자격 X |
| **prompt set 답습 한계** | Phase 1 prompt set 재사용 (cache miss 분리 답습). 단 권고 R21 적용 시 2k + 8k sub-set 다양화 부분 보완. 다른 prompt content 격차 변동 = 본 cycle 외 별도 cycle carry-over |
| **Ollama 재측정 noise (B-B3 + R11)** | 측정 순서 (llama.cpp 우선 vs Ollama 우선) 가 GPU 캐시·메모리 state 에 영향 가능. 본 cycle = 1회 측정 (statistical power 낮음 명문). Phase 1 mean ± std (7.83 ± 0.36) 의 ±2σ 범위 (7.11~8.55) 내/외 평가 = 재현성 일관 evidence. 범위 외 = noise 정직성 명문. *재측정 자격 평가는 별도 cycle* (권고 R11) |
| **빌드 ccache / 컴파일러 캐시** | 첫 빌드 시간 vs 재빌드 시간 격차 — wall-clock 측정 정확성 한계 (수단 영향). GB10 ARM aarch64 + nvcc sm_120/121 컴파일 실측 0건 — 2시간 상한 미보증 (권고 R14) |
| **github.com clone egress 의 redirect chain** | CDN (Cloudflare/Fastly 추정) IP range 추적 = ss 한정 (Phase 2 답습 — iptables 무효) |
| **빌드 *중* (~30분-2시간) R-1 anchor 공백 + 관찰 window 확장 statistical bias (R-3 B-S1 ⭐)** | 본 cycle 빌드 ~30분-2시간 + 측정 ~30분 = Phase 1·2 cycle (~30분-1시간) 의 ~2-3× window. R-1 hash 불일치 발견 확률이 ↑ 하는 경우, *silent 교체 빈도가 본질적으로 ↑ 한 것이 아니라 관찰 window 가 확장된 것* — V-1 entry brief §12 옵션 E trigger 자격 평가 시 본 statistical bias 분리 의무. mid-cycle anchor (§2.2 Step 8) 로 window ~75% 축소 |
| **빌드 wall-clock 중 R-23 위반 가능성 (R-17 권고)** | 빌드 ~2시간 동안 다른 LLM 호출 / 다른 사용자 작업 / 빌드 와 무관한 system load 발생 가능. 빌드 wall-clock 측정 (§4.1) 의 정확성 한계 — *재현성* 평가 시 단일 cycle 한정 |
| **빌드 egress 의도-외 확장 (R-7)** | apt repo 의존성 설치 / cmake FetchContent 자체 egress / 빌드 도구 자동 업데이트 등 의도-외 egress 발생 가능. §3.0 사전 차단 거버넌스 + §2.2 Step 5 apt snapshot pre/post + `DEBIAN_FRONTEND=noninteractive` 강제로 차단 시도, 발생 시 cycle 일시 정지 |
| **B hybrid fallback 자격 평가 별도** | 정공법 실패 시 B hybrid (prebuilt binary) fallback 진입 = 사용자 명시 의무 (자동 진입 0). prebuilt binary 출처/sha 검증 SOP = NOTE N-5 carry-over |
| **toolchain 단일 의존 (N-7)** | 현재 시스템 gcc/cmake/nvcc 한정. 다른 toolchain (gcc 13 / clang 19 / cuda 13) 변경 시 격차 = 본 cycle 외 별도 cycle carry-over |
| **Ollama runner stop vs idle trade-off (N-4)** | `/api/stop` 호출 시 다음 측정 cold start (모델 재로드 ~수십 초). 자연 idle = warm state 유지. Ollama 재측정 (§2.3 Step 6) 의 정확성 영향 분리 보고 carry-over |
| **`-ngl 999` 의 실제 layer 수 verify (N-5)** | llama.cpp `-ngl 999` = "전부" 의미. 측정 표준 명문화 시 실제 layer 수 (Qwen3-Next 48 layer 가정) verify → `-ngl <실제 layer 수>` verbatim 사용 권고 (R25). build/bin/llama-cli metadata dump 후 실제 layer 수 verify 의무 |
| **CMake `CUDA_ARCHITECTURES` shell escaping fragility (A-S3)** | `'120;121'` 단일 따옴표 표기는 bash 정합. 다른 shell wrapper (zsh / fish / tmux send-keys) 환경에서 semicolon split risk. 사용자 shell 환경 명문 의무 |

---

## 6. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 | 자격 |
|----|----|----|
| (A) | 본 brief v1.1 사용자 검토 → Phase 3 정공법 cycle 실행 명시 승인 → §2.1~§2.4 진행 | brief v1.1 commit 별도 / 또는 brief 검토 후 곧장 실행 |
| (B) | brief 보강 (누락 항목·절차 정밀화·분기 추가) | brief v1.2 → 재검토 |
| (C) | Phase 3 cycle 실행 후 → Phase 3 findings (`docs/phase0/jarvis-mvp1-v1-poc-phase3-findings.md` 또는 brief v1.2 EXECUTED §10) | findings 작성 별도 명시 |
| (D) | Phase 3 결과 후 → **M3·M4 결정 *고정* 합의** cycle (Phase 1+2+3 종합) — 3+1 합의 `d2d7bf9` §6 BLOCKING 1 해소 cycle | 별도 합의 brief + 사용자 명시 |
| (E) | Phase 3 결과 후 → R-15 gap-pull P1 trigger 자격 평가 cycle (R-10 SOP 통과 후) | 별도 brief + 사용자 명시 |
| (F) | Phase 3 결과 후 → 새 가설 #6 (sm_120/121 미지원) 검증 cycle (분기점 결과에 따라) — **Qwen3-30B-A3B 대조군 cycle 별도 brief 의무** (R-5 변수 분리) | 별도 brief + 사용자 명시 |
| (G) | B hybrid 변경 (정공법 미진입) | 사용자 명시 — 본 brief v1.2 또는 별도 brief |
| **(H)** (R-18 신규) | 본 brief v1.1 보강 (3+1 합의 결과 BLOCKING 반영) → 사용자 재검토 → Phase 3 진입 / 또는 별도 합의 cycle | 본 합의 `e76acc8` 결과 채택 자격 |
| **(I)** (R20 신규) | 다른 inference engine 후보 (MLC-LLM / llamafile / ktransformers / exllamav2 / vLLM / TensorRT-LLM) 의 GB10 sm_121 + Qwen3-Next 지원 외부 식별 cycle (egress 0, 외부 카드 한정) — Provider Liquidity 답습 강화 | 별도 brief + 사용자 명시 |
| **(J)** (R19 신규) | 정공법 cycle 후 → B hybrid (prebuilt binary) 비교 cycle (빌드 옵션 영향 격리 강도 ↑) | 별도 brief + 사용자 명시 |

**보안 거버넌스 자동 재개 금지** (비례성, `feedback_proportionate_security_personal_tool` 답습).

**단계별 명시 승인 답습** (`feedback_staged_consensus_workflow`): brief → 사용자 승인 → 실행 → findings → commit → push, 자동 다음 단계 진입 0건.

---

## 7. 산출물 (계획)

본 brief v1.1 commit 시:
- `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (본 문서, v1 → v1.1)

Phase 3 cycle 실행 *후* 작성 예정 (별도 명시 승인 후):
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-summary.json`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-build-log.txt` (R-1 grep + R-6 cuobjdump + R-1 llama-gguf 통합)
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-measure-{2k,8k}-{1,2,3}.txt` (권고 R21, sub-set 별 3회)
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-ollama-rerun-log.txt`
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-apt-snapshot-{pre,post}.txt` (R-7)
- `docs/phase0/v1-poc-raw/2026-05-2X-phase3-egress-baseline-{pre,post}.json`
- (findings 별도 명시 시) brief v1.2 EXECUTED §10 추가 또는 별도 findings 파일

본 brief 작성만으로는 위 raw / findings / commit / push 0건.

---

## 8. 답습 요약 (영구)

- **하는 것**: Phase 3 cycle (C-e 정공법) 운영 절차 식별 + 빌드 egress 시점/범위 격리 + 의도-외 egress 사전 차단 거버넌스 (R-7) + 측정 표준 명문 (R-12·R-21·R-25) + 분기점 raw 평가 (R-4 분리 framing) + 보고 항목 raw 한정 + #6 framing 약화 (R-5) + R-1 mid-cycle anchor (R-3)
- **하지 않는 것**: llama.cpp 실 빌드 / 측정 / Ollama 데몬 변경 (`/api/stop` 호출 boundary 별도 명문) / 모델 pull / config 변경 / M3·M4 결정 *고정* / OllamaBoss·LlamaCppBoss 코드 / 합의 보고서·commit·push / 보안 거버넌스 자동 재개 / gap-pull trigger / B hybrid 자동 진입 / Qwen3-30B-A3B 대조군 cycle 자동 진입
- **출처**: 3+1 합의 (`d2d7bf9`) §6 권고 (A) + §3 P-1 계층화 부분 채택 + §5 G-1 hybrid 대안 carry-over + G-2 새 가설 #6 carry-over + BLOCKING 5 / 3+1 합의 (`e76acc8`) BLOCKING 7 (R-1~R-7) + 권고 25 + NOTE 11 / M3·M4 결정 합의 `9ddec1b` §5.3 / V-1 entry brief / Phase 1 결과 `2026-05-24-phase1-summary.json` / Phase 2 brief v2 `c66756b` §9 / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `feedback_provider_liquidity` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 5조건 / 헌법 5조 (Provider Liquidity)

---

## 9. v1 → v1.1 변경 일람 (`e76acc8` BLOCKING 7 + 권고 일부 반영)

### BLOCKING 7 (verbatim 반영)

| BLOCKING | 반영 위치 | 변경 요지 |
|---------|---------|----------|
| R-1 (Qwen3-Next verify 강화) | §2.2 Step 3 재작성 + §2.2 Step 6.5 신규 (llama-gguf metadata dump) | grep keyword 5종 (a~e) + arch enum + GGUF metadata cross-check |
| R-2 (repo URL ggml-org) | §2.2 Step 1 + §5 정직성 한계 | `ggerganov` → `ggml-org` canonical, `git remote -v` + `ls-remote` verbatim |
| R-3 (R-1 mid-cycle anchor + cycle 폐기 framing 분리 + window bias) | §2.2 Step 8 신규 + §2.5 R-1 불일치 분기 재작성 + §5 신규 한계 행 | mid-cycle anchor 1회 + 발견 시점별 분기 대응 + statistical bias 명문 |
| R-4 (분기점 라벨 anchor effect 제거) | §1.1 line 70-74·§4.3 표 전면 재작성 + §1.4·§2.7 framing | "후보 입력" + "자동 평가 흐름 0건" + raw + 해석 분리 |
| R-5 (#6 framing 약화 + Qwen3-30B-A3B 대조군) | §1.3 line 99 verbatim 변경 + §2.7 분기점 표 신규 + §5 정직성 한계 | 빌드 실패 단정 framing 제거 + 대조군 cycle carry-over + PTX fallback 정직성 |
| R-6 (compute_cap 실측 + sm_121 SASS verify) | §2.1 Step 4 + §2.2 Step 4·Step 6 | 실측값 verbatim 인용 + cuobjdump SASS 포함 verify |
| R-7 (egress 사전 차단 거버넌스) | §2.2 Step 1.5·Step 4·Step 5 신규 + §3.0 신규 | submodule 사전 식별 + FETCHCONTENT_FULLY_DISCONNECTED 시도 + apt snapshot pre/post + non-interactive 강제 |

### 권고 25 중 본문 직접 반영 (8건)

- R8 (Ollama runner boundary): §2.3 Step 2 재작성
- R9 (per-layer breakdown 빌드 옵션 의존): §2.3 Step 5 + §5
- R11 (Ollama 재측정 1회 statistical power): §2.3 Step 6 + §4.2 + §5
- R12 (KV cache + context size `-c 8192`): §2.3 Step 3 + 측정 표준
- R14 (ccache 사용 권고): §2.1 Step 4 + §2.2 Step 4 + §5
- R15 (디스크 부족 분기): §2.5 표 신규행
- R16 (빌드 산출물 carry-over 자격): §2.4 Step 6
- R17 (R-23 wall-clock 정직성): §5
- R18 (§6 옵션 (H) 신규): §6
- R19 (정공법 후 B hybrid 비교 carry-over): §0.4 + §6 옵션 (J)
- R20 (다른 inference engine 외부 식별): §6 옵션 (I)
- R21 (prompt set 다양화 2k + 8k): §2.3 Step 4 + §4.4
- R22 (메모리 압박 측정 대안): §4.2
- R23 (R-1 anchor 회차 번호 검증): §2.1 Step 1 명문
- R24 (`--version` CUDA 식별자 verbatim): §2.2 Step 6 + §4.1
- R25 (`-ngl <실제 layer 수>`): §2.3 Step 3 + 측정 표준

### NOTE 11 carry-over (별도 cycle/단계 의무, 본문 명문 only)

N-1~N-11 = §0.2 + §5 + §6 다음 단계 표 + §8 답습 요약에 명문. 본 cycle 자체 0건 답습.
