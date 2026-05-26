# 3+1 합의 보고서 — 자비스 MVP-1 V-1 PoC Phase 3 (C-e 정공법) entry brief 진입 자격 평가

> **본 합의 = brief v1 → v1.1 *진입 게이트* 한정** (staged consensus 답습). 실 빌드/측정/M3·M4 결정 *고정* 자격 평가 0건. brief 갱신·commit·push 0건 (사용자 명시 별도).

---

**작성일**: 2026-05-24
**합의 단위**: V-1 PoC Phase 3 (C-e llama.cpp 정공법) entry brief DRAFT v1 (`cc145fd`) 진입 자격 평가
**선행 답습**:
- 합의 `d2d7bf9` (M3·M4 결정 *고정* 자격 미충족, BLOCKING 5) §6 권고 (A) 정공법 채택 + G-1 hybrid carry-over + G-2 새 가설 #6 carry-over
- M3·M4 결정 합의 `9ddec1b` §5.3 (C-e 명문)
- V-1 entry brief §1.2 (R-1 silent 교체 위험) + §8 (egress baseline) + §12 옵션 E (Ollama 위생 정정 trigger)
- Phase 1 raw (`v1-poc-raw/2026-05-24-phase1-summary.json`) — A-진단 roofline 90~120 + C-c cache miss 분리
- Phase 2 brief v2 EXECUTED §9 (F1 (i) 부정 + (ii) Gated DeltaNet 명명 정정 + (v) 강한 evidence)

**참여 Agent**: A (구현 분석가, 기술적 충분성) / B (품질·안전성 검증가, 정직성/거버넌스) / C (대안 탐색가, trade-off/누락) / Reviewer (Phase 3-4 교차 비교 + 합의)

**답습 권위 한계**: 본 합의 = brief 진입 게이트 *권고* 한정. brief v1 → v1.1 보강 / 실 빌드 / 측정 / M3·M4 결정 고정 / Ollama 위생 정정 trigger 발효 / OllamaBoss·LlamaCppBoss 코드 = **모두 사용자 명시 별도**.

---

## 0. 검토 대상 + Agent 출력 종합

**검토 대상**: `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (DRAFT v1, 318줄, `cc145fd`)

**3 Agent 종합 판정**:

| Agent | 판정 | BLOCKING | 권고 | NOTE | 단독 발견 |
|-------|------|---------|------|------|---------|
| A (구현) | APPROVE w/ COND | 4 (A-B1~B4) | 5 (A-R1~R5) | 3 (A-N1~N3) | 4 (A-S1~S4) |
| B (안전성) | APPROVE w/ COND | 5 (B-B1~B5) | 6 (B-R1~R6) | 3 (B-N1~N3) | 3 (B-S1~S3) |
| C (대안) | APPROVE w/ COND | 3 (C-B1~B3) | 6 (C-R1~R6) | 5 (C-N1~N5) | 3 (C-S1~S3) |
| **소계 (raw)** | 3 × APPROVE w/ COND | **12** | **17** | **11** | **10** |
| **기각** | 0 | — | — | — | — |

→ **방향 (정공법 채택, 절차 운영화, 빌드+측정 격리, raw 한정 보고) 에 3개 모두 합의.** brief v1 → v1.1 보강 BLOCKING 통합 후 진입 자격 충분.

---

## 1. 교차 비교 매트릭스 (8 영역 × 4 분류)

### Q1: llama.cpp upstream repo 정확성 + Qwen3-Next 지원 verify

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | **BLOCKING** A-B1 (repo URL `ggerganov` → `ggml-org` 이관) + A-B2 (grep keyword 빈약, `qwen3next` arch identifier 답습) + A-B4 (GGUF metadata `llama-gguf` cross-check) | manifest §9.1 의 `qwen3next.expert_count` verbatim = arch identifier hyphen/underscore 0, brief grep 변형 3종 적중률 ↓. `convert_hf_to_gguf.py` 의 `LLM_ARCH_NAMES` 매핑 = 핵심 검증 지점 |
| B | 부분 입장 (B-S3 cuobjdump SASS verify 와 결합, 정공법 fallback 작동 verify 의무) | sm_120/121 PTX 미포함 시 빌드 결과 정직성 명문 |
| C | **BLOCKING** C-B1 (fork/PR 식별 사전 mini-cycle, master 미지원 시 시간 ~3시간 손실 회피) | Provider Liquidity 답습, 단일 upstream 의존 회피 |

**분류**: ② 부분 일치 (A·C 강하게 BLOCKING, B 간접). **통합 채택 → R-1, R-2**.

### Q2: R-1 anchor 빌드 *중* (~2시간) 공백

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 미언급 (구현 관점 외) | — |
| B | **BLOCKING** B-B1 + B-S1 (관찰 window 확장 statistical bias) | Phase 1·2 cycle (~30분-1시간) 의 3-4× window, silent 교체 발견 자격 평가 input bias |
| C | 미언급 (대안 관점 외) | — |

**분류**: ④ 누락 (B 단독). 채택 — **R-3**. B 단독 발견 = ⭐ critical (V-1 entry brief R-1 silent 교체 위험 답습 강도 ↑).

### Q3: §4.3 분기점 라벨 (격차 <20%/20-50%/>50%) anchor effect

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 미언급 | — |
| B | **BLOCKING** B-B2 | R-6 답습 (PASS/FAIL framing 금지), Phase 1·2 raw 한정 답습 vs Phase 3 분기 라벨 격차, 18% vs 22% 의 cliff edge anchor |
| C | 미언급 | — |

**분류**: ④ 누락 (B 단독). 채택 — **R-4**. B 단독 발견, R-6 답습 critical.

### Q4: 가설 #6 (sm_120/121 미지원) 검증 framing

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 부분 (A-B3 문제 3, PTX fallback 작동 미verify) | Blackwell sm_120 의 PTX forward-compat boundary 미verify |
| B | **권고** B-R1 (빌드 실패 = #6 강한 강화 단정 framing) + B-S3 (cuobjdump SASS verify) | 빌드 실패 원인 6+ 분포 (gcc/cmake/cuda toolkit/디스크/코드 미머지/sm 미인식), "#6 강한 강화" 사전 단정 |
| C | **BLOCKING** C-B2 (Qwen3-30B-A3B 대조군 변수 분리) | Qwen3-Next 단일 모델 = (a) sm_120/121 vs (b) Gated DeltaNet kernel vs (c) Qwen3-Next arch 미지원 분리 불가 |

**분류**: ① 일치 (3개 모두 #6 framing 약점 식별, 각 다른 측면) — **통합 채택 R-5**.

### Q5: cmake variable + compute_cap 실측 + PTX SASS verify

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | **BLOCKING** A-B3 (`CMAKE_CUDA_ARCHITECTURES` 값 결정 의무 + `compute_cap = 12.1` 단정 표현 제거) | 빌드 옵션 적정성 = compute_cap 실측 후 결정 |
| B | 부분 (B-S3) | cuobjdump `--list-elf` 로 binary 내 sm_121 SASS/PTX 존재 verify |
| C | 미언급 | — |

**분류**: ② 부분 일치 (A·B 강도 차이). A의 실측 의무 + B의 SASS verify 결합 — **R-6**.

### Q6: GGUF metadata cross-check (`llama-gguf` dump)

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | **BLOCKING** A-B4 (Step 6.5 신규, `general.architecture` verbatim verify) | manifest §9.1 arch identifier `qwen3next` 와 llama.cpp `src/llama-arch.cpp` enum cross-check |
| B | 미언급 | — |
| C | 미언급 | — |

**분류**: ④ 누락 (A 단독). 채택 — Q1 의 R-1 통합 적용 (A-B2/B4 결합).

### Q7: 빌드 egress 의도-외 확장 (apt deps / cmake FetchContent) 사전 차단

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 권고 A-R4 (apt 의존성 명문 강화) | §0.3 "github.com clone + apt deps 가능" 표현 약함 |
| B | **BLOCKING** B-B4 (사전 차단 거버넌스 명문) | 빌드 wall-clock ~2시간 = 사용자 모니터링 minimal, apt prompt 자동 yes 답습 시 침묵 진행 risk, cmake FetchContent 자체 egress 가능성 |
| C | 미언급 | — |

**분류**: ② 부분 일치 (A 권고 + B BLOCKING). B 채택 — **R-7**.

### Q8: Ollama runner stop "선택" 모호성 + 데몬 변동 0 evidence + 재측정 noise

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 권고 A-R3 (`/api/stop` = runner 종료, 데몬 영향 0, Step 6 "재가동" 명시) | 데몬 PID 3375 불변 가정, 자연 reload |
| B | **BLOCKING** B-B3 (자연 idle 우선, `/api/stop` 사전 verify 없이는 호출 금지, 재측정 별도 cycle 분리) + B-S2 (Ollama denominator 양값 보고) | §0.2 "Ollama 데몬 재시작/kill/signal 금지" boundary 명문 0, Ollama 0.20.4 `/api/stop` 코드 verify 0 |
| C | NOTE C-N4 (runner stop vs idle trade-off) | stop = cold start, idle = warm state |

**분류**: ③ 불일치 (A 유연 / B 보수 / C trade-off). 안전성 우선 — **R-8** (B 강도 채택, A 권고 부분 흡수).

### Q9: (iv) router overhead 측정 대안 (PyTorch profiler / NSight)

| Agent | 입장 | 핵심 근거 |
|-------|------|----------|
| A | 권고 A-R1 (per-layer breakdown 빌드 옵션 의존, `-DGGML_PERF=ON` 사전 verify) | llama-print-timings default 미포함 |
| B | 미언급 | — |
| C | **BLOCKING** C-B3 + C-S2 (PyTorch forward hook 으로 (iv) 단독 측정) | llama.cpp verbose log = 간접, PyTorch eager mode = (iv) 단독 자격 |

**분류**: ② 부분 일치. C BLOCKING 격하 → 권고로 통합 (본 cycle 자체에는 미포함, carry-over) — **권고 R10**.

### Q10: 누락 단독 발견 (각 Agent ⭐)

- **A-S1 (BLOCKING 격상)**: `ggerganov` → `ggml-org` upstream 이관 사실 — repo URL 의 정확성이 빌드 evidence 강도의 *전제*. → R-2
- **A-S2**: GGUF metadata arch identifier `qwen3next` 와 grep keyword 변형 적중률 분석 → R-1 통합
- **A-S3**: CMake semicolon-list shell escaping fragility → R-6 통합
- **A-S4**: llama-print-timings default per-layer 미포함 → 권고 R10
- **B-S1 (NOTE 격상)**: 빌드 ~2시간 wall-clock = 관찰 window 4× 확장 → silent 교체 발견 자격에 statistical bias introduce. 옵션 E trigger 평가 시 분리 의무 → R-3 통합 + 정직성 한계 명문
- **B-S2**: §4.3 Ollama denominator (Phase 1 mean vs Phase 3 재측정값) 양값 보고 의무 → R-4 통합
- **B-S3**: cuobjdump SASS sm_121 포함 verify → R-6 통합
- **C-S1**: Qwen3-30B-A3B 대조군 cycle (변수 분리, Gated DeltaNet kernel 미지원 가설 분화) → R-5 통합
- **C-S2**: PyTorch forward hook 으로 (iv) 단독 측정 → 권고 R10
- **C-S3**: fork/PR mini-cycle 사전 분리 (Provider Liquidity 답습 + 시간 손실 회피) → R-1 통합

---

## 2. 일치 항목 (Consensus)

### C-1. 정공법 채택 + 절차 골격 (3 Agent 일치)

3 Agent 모두 brief 의 §2 절차 골격 (사전 점검 → 빌드 → 측정 → 종료 보장) + §3 egress 격리 + §4 raw 한정 보고 + §5 정직성 한계 명문 + §6 다음 단계 7 옵션 = **방향 합의**. brief v1 → v1.1 보강 후 진입 자격 충분.

### C-2. 가설 #6 framing 약점 (A·B·C 각 다른 측면)

3 Agent 모두 가설 #6 (sm_120/121 미지원) 검증의 framing/단정/변수 분리 약점 식별. **각 측면 통합 채택 = R-5 (framing 약화 + 대조군 cycle + PTX fallback 미verify 명문)**.

### C-3. R-6 framing 답습 의무 + raw 한정 보고 (3 Agent 일치)

3 Agent 모두 PASS/FAIL framing 금지 + raw 한정 보고 의무 명문. brief §4 보고 항목 정합 (B-B2 의 §4.3 분기점 라벨 anchor effect 만 BLOCKING 으로 보강).

---

## 3. 부분 일치 (Partial) + 결정

### P-1. Q1 (Qwen3-Next 지원 verify) 강도

A (grep keyword + GGUF metadata + repo URL) ↔ C (fork/PR mini-cycle 사전 분리, Provider Liquidity) ↔ B (PTX SASS verify 간접 결합).

**채택**: 3 측면 **통합** — R-1 (grep 강화 + `convert_hf_to_gguf.py` 매핑 + GGUF metadata cross-check) + 별도 R-2 (repo URL) + 권고 R6 (fork mini-cycle carry-over). Provider Liquidity 답습.

### P-2. Q9 ((iv) 측정 대안) 본 cycle 포함 자격

C (BLOCKING, PyTorch forward hook 본 cycle 외 carry-over 의무) ↔ A (권고, `-DGGML_PERF=ON` 사전 verify) ↔ B (미언급).

**채택**: 본 cycle 외 carry-over 권고로 격하 (R10). 본 cycle 의 (iv) 자격 = "결합 효과만, 단독 자격 X" 명문 답습 유지. brief §5 정직성 한계 표 신규행 (대안 후보 carry-over) 명문 의무.

---

## 4. 불일치 (Divergence) + 결정

### D-1. Q8 (Ollama runner stop boundary)

- A: `/api/stop` = runner 종료, 데몬 영향 0, Step 6 재가동 명시
- B: `/api/stop` 사전 verify 없이는 호출 금지, 자연 idle 우선, 재측정 별도 cycle
- C: trade-off (stop = cold start, idle = warm state)

**평가 + 결정**: 양립 가능. **안전성 우선 + A 권고 부분 흡수** — R-8 (자연 idle 우선 / `/api/stop` 호출 = §0.2 boundary 명문 + 데몬 PID 불변 evidence 명문 후만 / 재측정 = mid-cycle anchor 결합 + 1회 한정 명문 + statistical power 정직성 명문). **Ollama 재측정 별도 cycle 분리는 권고로 격하** (R11) — 본 cycle 내 1회 cross-check 자격 유지하되 evidence 강도 약함 명문.

---

## 5. 누락 항목 (Gap) + 채택/제외 평가

### G-1. A-S1 — repo URL 이관 (ggerganov → ggml-org)

**채택** (HIGH). 빌드 evidence 강도의 *전제*. 본 분석 = 외부 fetch 0 (`feedback_proportionate_security_personal_tool` 답습) 한정, redirect 작동 verify 0건의 정직성 명문 의무. → R-2

### G-2. B-S1 — 관찰 window 확장 statistical bias

**채택** (MEDIUM-HIGH). 옵션 E trigger 자격 평가 입력 bias 분리 의무. → R-3 통합 + 정직성 한계 명문.

### G-3. C-S1 — Qwen3-30B-A3B 대조군 (변수 분리)

**채택** (MEDIUM). 본 cycle 자체에는 미포함, carry-over cycle (Phase 3.5 후보) 명문. → R-5 통합.

### G-4. Provider Liquidity 답습 강화 (C-R2 / C-N1)

**채택** (HIGH). 헌법 5조 답습. 본 cycle 외 다른 inference engine 후보 (MLC-LLM·llamafile·ktransformers·exllamav2·vLLM·TensorRT-LLM) 외부 식별 cycle carry-over. → 권고 R6.

### G-5. ADR-011 §2.1 5조건 답습 의무 (B-N1)

**carry-over**. 본 cycle = 결정 *고정* 0건 → 5조건 발효 미진입 정합. 단 본 cycle 측정 raw 가 향후 결정 *고정* cycle 의 5조건 평가 input 자격이 됨을 명문. → NOTE N-1.

---

## 6. 합의 결론

### Phase 3 entry brief 진입 자격: **단독 미충족** (BLOCKING 7 보강 후 진입)

- **방향 (정공법 채택, 절차 운영화, 빌드+측정 격리, raw 한정 보고) = 충분 자격**
- **brief v1 → v1.1 보강 = 진입 게이트 의무**
- **실 빌드/측정 진입 = brief v1.1 commit + 사용자 명시 별도**

### BLOCKING 조건 (3 Agent 종합 통합)

| BLOCKING | 영역 | 출처 | 권고 verbatim 위치 |
|---------|------|------|------------------|
| **R-1** | Qwen3-Next 지원 verify 강화 (grep 강화 + `convert_hf_to_gguf.py` 매핑 + GGUF metadata cross-check) | A-B2 + A-B4 + C-S3 | §2.2 Step 3 재작성 + §2.2 Step 6.5 신규 |
| **R-2** | llama.cpp upstream repo 정확성 (`ggml-org` 채택, `git remote -v` + `ls-remote` verbatim 기록) | A-B1 + A-S1 ⭐ | §2.2 Step 1 + §6 정직성 한계 |
| **R-3** | R-1 anchor mid-cycle 추가 (빌드 종료 직후·측정 시작 전 9회차) + cycle 폐기 framing 분리 (발견 시점별 분기) + 관찰 window 확장 statistical bias 명문 | B-B1 + B-B5 + B-S1 ⭐ | §2.2 Step 8 신규 + §2.5 line 178 재작성 + §5 신규 한계 행 |
| **R-4** | §1.1·§4.3 분기점 라벨 anchor effect 제거 (raw 측정값 + 해석 분리 보고, R-6 답습) + Ollama denominator 양값 보고 | B-B2 + B-S2 ⭐ | §1.1 line 70-74·§4.3 표 전면 재작성 |
| **R-5** | 가설 #6 framing 약화 ("빌드 실패 = #6 강한 강화" 단정 제거) + Qwen3-30B-A3B 대조군 carry-over cycle 명문 + PTX fallback 미verify 정직성 | A-B3 문제3 + B-R1 + C-B2 + C-S1 ⭐ | §1.3 line 99 verbatim 변경 + §2.6 분기점 표 신규행 + §5 신규 한계 행 |
| **R-6** | compute_cap 실측 의무 (`nvidia-smi --query-gpu=compute_cap` 실측 후 cmake variable 결정) + sm_120/121 SASS 포함 verify (`cuobjdump --list-elf`) | A-B3 + B-S3 ⭐ | §2.1 Step 4 + §2.2 Step 4 + §2.2 Step 6 강화 |
| **R-7** | 빌드 egress 의도-외 확장 *사전* 차단 거버넌스 (submodule 사전 식별 + `FETCHCONTENT_FULLY_DISCONNECTED` 시도 + apt snapshot pre/post + non-interactive 강제) | B-B4 ⭐ | §2.2 Step 1.5·Step 4·Step 5 신규 + §3.0 신규 |

### 권고 조건 (non-blocking)

| 권고 | 영역 | 출처 |
|------|------|------|
| R8 | Ollama runner stop boundary 명문 (자연 idle 우선, `/api/stop` 호출 = 데몬 PID 불변 evidence 명문 후만) + 재측정 statistical power 정직성 명문 | A-R3 + B-B3 + B-R2 + C-N4 |
| R9 | per-layer breakdown 빌드 옵션 의존 (`-DGGML_PERF=ON` 사전 verify) | A-R1 + A-S4 |
| R10 | (iv) router overhead 측정 대안 carry-over (PyTorch forward hook / NSight Compute / vLLM tracing) | C-B3 격하 + C-S2 ⭐ |
| R11 | Ollama 재측정 별도 cycle 분리 권고 (본 cycle 내 1회 cross-check 자격은 유지하되 evidence 강도 약함 명문) | B-B3 격하 |
| R12 | KV cache 메모리 + GB10 121GB 헤드룸 명문 + context size 명문 (`-c 8192` Phase 1 답습) | A-R2 |
| R13 | apt 의존성 egress 강화 + DEBIAN_FRONTEND noninteractive 회피 | A-R4 + B-B4 부분 흡수 |
| R14 | ccache 사용 권고 격상 + nvcc Blackwell wall-clock 실측 0건 명문 | A-R5 + C-R3 |
| R15 | 디스크 부족 분기 §2.5 표 추가 | B-R3 |
| R16 | 빌드 산출물 carry-over 자격 검증 (다음 cycle entry brief 평가) | B-R4 |
| R17 | R-23 wall-clock 정직성 (빌드 ~2시간 중 다른 LLM 호출 / system load 정직성 명문) | B-R5 |
| R18 | §6 옵션 (H) "brief v1.1 보강 (합의 결과 반영)" 신규 옵션 | B-R6 |
| R19 | 정공법 *후* B hybrid 비교 cycle carry-over (빌드 옵션 영향 격리) | C-R1 |
| R20 | 다른 inference engine 후보 외부 식별 cycle carry-over (Provider Liquidity 강화) | C-R2 + C-N1 |
| R21 | prompt set 다양화 (Phase 3 내부 2k + 8k sub-set) | C-R4 |
| R22 | 메모리 압박 측정 대안 (`/proc/<pid>/status` VmRSS, `/proc/meminfo` MemAvailable) | C-R5 |
| R23 | R-1 anchor 회차 번호 검증 (Phase 1+2 누계 회수 재확정) | C-R6 |
| R24 | `--version` 출력 "CUDA: 1" / `ggml-cuda` 식별자 verbatim 인용 | A-N1 |
| R25 | `-ngl 999` 의 실제 layer 수 verify (Qwen3-Next 48 layer → `-ngl 48` 권고) | C-N5 |

### NOTE (carry-over, 다음 cycle 입력)

| NOTE | 내용 |
|------|------|
| N-1 | ADR-011 §2.1 5조건 본 cycle 미진입 정합 (결정 *고정* 0건), 향후 결정 *고정* cycle 의 input 자격 carry-over |
| N-2 | M3 결정 문구 "SSM" → "Gated DeltaNet" verbatim 의무 (Phase 2 §9 EXECUTED + 합의 d2d7bf9 BLOCKING 4 답습), 결정 *고정* cycle 별도 |
| N-3 | `OllamaBoss`·`LlamaCppBoss` 코드 0건 답습 (§0.2 line 41) — 트랙 B 진입 차단 자격 유지, M3·M4 결정 *고정* 후 carry-over |
| N-4 | R-15 gap-pull P1 trigger 자격 평가 = 별도 cycle (합의 d2d7bf9 §4 D-1 답습) |
| N-5 | B hybrid fallback SOP 미수립 — 정공법 실패 시 prebuilt binary 출처/sha 검증 cycle 별도 |
| N-6 | github.com redirect chain (CDN Cloudflare/Fastly 추정) IP range 추적 = ss 한정 (Phase 2 답습, iptables 무효) |
| N-7 | toolchain 변경 (gcc 13 / clang 19 / cuda 13) cycle carry-over |
| N-8 | V-1 entry brief §12 옵션 E (Ollama 위생 정정) trigger 자격 = 본 cycle 결과 입력 후 *별도* 평가, 본 brief 의 *강도 평가 0건* (R-6 답습) |
| N-9 | Provider Liquidity (헌법 5조) 답습 강화 trace — 본 cycle = Ollama + llama.cpp 2종 한정, 결정 *고정* 전 다른 engine 식별 cycle carry-over |
| N-10 | Blackwell PTX forward-compat boundary (sm_120 PTX → sm_121 device 실행 가능성) verify 0건 — Reviewer/Agent A 일반 지식 기반 추정 한정 |
| N-11 | C-R6 R-1 anchor 회차 번호 검증 — Phase 1·2 누계 회수 미명시, brief v1.1 정정 의무 |

### 답습 (Reviewer 의무)

| 답습 | 적용 위치 |
|------|---------|
| R-6 (PASS/FAIL framing 금지) | R-4 (분기점 라벨), R-5 (#6 framing), 본 합의 전체 |
| 비례 보안 (`feedback_proportionate_security_personal_tool`) | R-7 (egress), R-8 (Ollama runner), R-19 (B hybrid carry-over), 보안 거버넌스 자동 재개 0건 |
| Provider Liquidity (헌법 5조) | R-1·R-2 (repo URL + fork mini-cycle), R-20 (다른 engine), 영구 배제 0건 |
| 정직성 (약한 link 명문화) | R-3 (관찰 window bias), R-5 (PTX fallback 미verify), R-6 (compute_cap 실측), R-17 (wall-clock noise) |
| 단계별 명시 승인 (`feedback_staged_consensus_workflow`) | brief v1.1 → 사용자 승인 → 실 빌드 진입 → 측정 → findings → commit → push, 자동 다음 단계 0건 |
| ADR-011 §2.1 5조건 | N-1 (본 cycle 미진입 정합, carry-over) |

---

## 7. 자체 0건 답습 (Reviewer)

본 합의 자체:
- ❌ brief v1.1 갱신 / brief 파일 직접 수정 / commit·push (사용자 명시 별도)
- ❌ 실 빌드 / 측정 / Ollama 데몬 변동 / 모델 pull / config 변경
- ❌ M3·M4 결정 *고정* (Phase 1+2+3 종합 합의 cycle 별도)
- ❌ V-1 entry brief §12 옵션 E trigger 발효 (자격 평가 별도)
- ❌ R-15 gap-pull *실행* (R-10 SOP 통과 + P1 trigger 자격 평가 별도)
- ❌ 다른 inference engine 후보 외부 식별 cycle (egress 0 답습, 사용자 명시 별도)
- ❌ Qwen3-30B-A3B 대조군 cycle 진입 (Phase 3.5 후보, 별도 brief)
- ❌ `OllamaBoss`·`LlamaCppBoss` 코드 (트랙 B 별도)
- ❌ 보안 거버넌스 자동 재개 (비례성)

---

## 8. 답습 요약 (영구)

- **하는 것**: brief v1 진입 자격 평가 + BLOCKING 7건 + 권고 25건 + NOTE 11건 식별 + 다음 단계 권고
- **하지 않는 것**: brief v1.1 갱신·commit·push / 실 빌드·측정 / M3·M4 결정 *고정* / Ollama 위생 정정 trigger 발효 / gap-pull 실행 / 다른 engine 식별 cycle / 대조군 cycle / 트랙 B 코드 / 보안 거버넌스 자동 재개
- **출처**: 합의 `d2d7bf9` §6 권고 (A) + G-1·G-2 carry-over + BLOCKING 5 / M3·M4 결정 합의 `9ddec1b` §5.3 / V-1 entry brief / Phase 1 raw / Phase 2 brief §9 / Agent A·B·C 독립 분석 / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `feedback_provider_liquidity` / `project_jarvis_local_boss_direction` / ADR-011 §2.1 5조건 / 헌법 5조

---

**Reviewer 최종 권고**: Phase 3 entry brief = **APPROVE w/ COND, BLOCKING 7 + 권고 25 + NOTE 11**. brief v1 → v1.1 보강 (BLOCKING 7 verbatim 반영) 후 실 빌드 진입 자격 충분. **단계별 명시 승인 답습** (brief v1.1 commit → 사용자 검토 → 실 빌드 진입 → 측정 → findings → 합의 → commit·push, 자동 다음 단계 0건). R-6 framing + 비례 보안 + Provider Liquidity + staged consensus 4중 답습 의무.
