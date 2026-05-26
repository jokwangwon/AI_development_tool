# (h)' LlamaCppBoss bartowski direct N=3 분산 측정 cycle entry brief v1.1

**일자**: 2026-05-26 (v1 `0fc26fb` 341줄 → v1.1 보강 본)
**유형**: 진입 brief (Phase 0, 6단계 변형 entry form, R-rec-16 답습)
**선행**: (4-way) 20번째 entry cycle 완주 (chain 영구 종결 의무 답습 영구) + REC-3 신규 carry-over MEDIUM + R-S4 발효 (j) 진입 선결 의무 강화 + 본 cycle 풀 3+1 합의 (`6dcd8c9`) APPROVE w/ COND BLOCKING 11 + R-S1~R-S4 답습
**자격**: (4-way) §9 carry-over MEDIUM ⭐⭐ "(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle (REC-3 신규)", 사용자 명시 + 2 명확화 (scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 측정 + 수단 sudo 포함 R-1 anchor 27회 임시 비밀번호 발급 필요)

---

## 0. 본 brief 의 *하지 않는 것* (15 항목, R-15 self-consistency 영구)

1. ❌ **(h) bartowski GGUF 변경** (`382b4f5a164d...33a95`, 17.353 GiB, R-13 답습 영구)
2. ❌ **llama.cpp HEAD `c0c7e147` 변경** (R-13 답습 영구)
3. ❌ **(h)/(h-O)/(h-OM) raw report 변경** (read-only 답습)
4. ❌ **헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경** (R-9 답습 영구)
5. ❌ **MVP-1 brief / 합의 보고서 / (4-way) brief / Boss 추상화 design doc 본문 변경** (R-9 답습 영구)
6. ❌ **Ollama daemon 변경** (pid 3375 보존, 답습 영구)
7. ❌ **Ollama library/Modelfile blob 변경** (R-13 답습 영구)
8. ❌ **(k) M3·M4 결정 *고정*** (변수 분리 input 강화 후 별도 cycle)
9. ❌ **(j) advisory wall-clock *측정*** ((j) 별도 cycle, 본 cycle = (j) 진입 *선결* 의무 답습 only)
10. ❌ **테스트 작성/실행** (TDD RED-GREEN-REFACTOR = (l) 별도 cycle)
11. ❌ **`src/jarvis/` 코드 변경** (기존 boss.py 98줄 + orchestrator.py + approval.py + tests/jarvis/test_boss_advisory.py 변경 0건, R-S1 답습 영구. **(4-way) brief 답습 "99줄" vs 실측 "98줄" 1줄 차이는 본 cycle 정정 0건, NOTE only**)
12. ❌ **메모리 자동 갱신** (사용자 명시 의무)
13. ❌ **brief commit / 합의 commit / raw report commit / SESSION commit / push 자동 진입** (단계 단위 사용자 명시 의무)
14. ❌ **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) + (h)'-X prime/super-prime 자동 진입** (chain 영구 종결 의무 답습 영구 — **8 chain 전체 자동 진입 금지 1:1 매핑 verbatim 답습 영구**, BLOCKING-10 + R-S1 흡수)
15. ❌ **password literal 직접 사용** (R-S2 발효 영구, summary/raw report 모두 redact 의무, BLOCKING-9 흡수)

---

## 1. 본 cycle scope ((h) 동형 N=3 cold, (4-way) REC-3 직접 후속)

### 1.1 측정 매트릭스 (사용자 명시 "(h) 동형 prompt 2 종 × N=3 cold = 총 6 측정") + cold 절차 명문 (BLOCKING-3 흡수)

| 측정 # | prompt | run | 목적 |
|---|---|---|---|
| 1 | decode-161tok generation | cold-1 | decode generation t/s 분산 검증 |
| 2 | decode-161tok generation | cold-2 | (반복) |
| 3 | decode-161tok generation | cold-3 | (반복) |
| 4 | prefill-2k prompt | cold-1 | prefill prompt t/s 분산 검증 |
| 5 | prefill-2k prompt | cold-2 | (반복) |
| 6 | prefill-2k prompt | cold-3 | (반복) |

**총 6 measurement runs (각 prompt N=3 cold)**.

**cold 절차 명문 (B-CONS-3 흡수, A-B-A3 + C-B-C3 합의)**:
1. **process kill**: `pkill -9 llama-cli` (또는 `kill -9 [PID]`)
2. **GPU memory 0 confirm**: `nvidia-smi --query-gpu=memory.used --format=csv` 0 또는 idle baseline 확인 (wait 최대 30s)
3. **page cache drop (sudo 필요)**: `sync && sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'` (B-CONS-3 흡수, mmap GGUF page cache 비대칭 회피)
4. **(권고) thermal cooldown wait**: 60s sleep (B-CONS-3 + craftrigs 외부 evidence 답습, thermal 12-18% swing 회피, 단 권고 R-CONS-1 자격)
5. **cold load + first decode** 실행

⚠️ **cold 비대칭 risk 정직성 (B-CONS-3)**: page cache drop 미적용 시 cold-2/3 = warm GGUF I/O = cold-1 과 비대칭 → CV 측정 신뢰성 invalidate. thermal 미적용 시 cold-1 = GPU idle / cold-2/3 = warm 상태 → 분산 자체 thermal artifact 가능.

### 1.2 측정 대상 (h) 동형 영구 답습 + prompt source 정정 (BLOCKING-7 흡수)

- **모델**: Qwen3-30B-A3B classical MoE Q4_K_M
- **GGUF**: bartowski direct (sha256 `382b4f5a164d...33a95`, 17.353 GiB, R-13 답습 영구)
- **runtime**: llama.cpp `c0c7e147` master (R-13 답습 영구)
- **HW**: DGX Spark GB10 (121GB unified memory, 답습 영구)
- **container/host**: (h) 답습 패턴 (host 직접)
- **prompt source 실제 (B-CONS-7 정정)**:
  - decode-161tok = `/tmp/v1-poc-prompts/decode-prompt.json` (705 bytes, mtime 2026-05-23 13:02, 호스트 `/tmp` 임시)
  - prefill-2k = `/tmp/v1-poc-prompts/prefill-2k-precheck.json` (11524 bytes, mtime 2026-05-23 21:02, 호스트 `/tmp` 임시)
  - **R-7 격리 외 자격 정직성 명문 영구** (reboot 시 소실 위험)
  - **본 cycle raw report 디렉토리에 cp 영구 보존 + sha256 anchor 의무** (`2026-05-26THH-MM-phase3-5-h-prime-decode-prompt-input.json` + `*-prefill-2k-prompt-input.json` + sha256 텍스트)

### 1.3 분산 분석 산출 multi-metric (BLOCKING-5 흡수)

- **mean (μ)**: N=3 평균 t/s
- **stddev (σ)**: 표본 표준편차 (Bessel's correction, N-1=2)
- **min/max**: N=3 중 최솟값/최댓값
- **CV (변동계수)**: σ/μ × 100% (%)
- **(h) 비교 multi-metric** (B-CONS-5 흡수, B-C4 외부 evidence 답습):
  - (h) ∈ [μ - σ, μ + σ] (≈68% inclusion, normality 가정)
  - (h) ∈ [μ - 2σ, μ + 2σ] (≈95% inclusion, normality 가정)
  - (h) ∈ [min, max] (range inclusion, non-parametric)
  - delta% = ((h) - μ) / μ × 100% (단위 percent)
- ⚠️ **Welch's t-test (N=1 vs N=3) 부적격 명문 (B-CONS-5)**: (h) = N=1 single → 분산 미정 → t-test 자체 부적격. 본 cycle 비교 = **inclusion test only**, statistical equivalence test 자격 0건

---

## 2. 분석 대상 verbatim (read-only, R-13 + R-S 답습)

### 2.1 (h) raw report 답습 (read-only)

**(h) raw report 17번째 entry**:
- `docs/phase0/v1-poc-raw/phase3-5-h/2026-05-25T17-58-phase3-5-h-summary.json`
- decode-161tok generation = **49.6 t/s** (single, N=1)
- prefill-2k prompt = **1916.8 t/s** (single, N=1)
- decode-161tok prompt = 389.4 t/s (single, N=1)
- prefill-2k generation = 45.4 t/s (single, N=1)

### 2.2 (4-way) REC-3 신규 carry-over verbatim

**(4-way) brief v1.1 §9.4 + Boss 추상화 design doc §7.4**:
- "(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle MEDIUM (REC-3 신규)" — (h) 단일 측정 49.6 t/s 분산 미확인 정직성

**(4-way) R-S4 발효 — (j) 진입 선결 4 carry-over verbatim 답습 영구 (BLOCKING-10 흡수)**:
1. **Phase 1 N=3 repetitions Ollama 답습 MEDIUM** (C-S2 답습, Ollama 분산 검증 필수)
2. **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle MEDIUM** (REC-3 신규, 본 cycle 충족 자격)
3. **Ollama embedded llama.cpp version verify MEDIUM** (변수 분리)
4. **Ollama prefill processing framework overhead 검증 MEDIUM** (F-4 (h-OM) 답습)

→ **본 cycle = 4 carry-over 중 (2) 충족**, 나머지 3 carry-over = 별도 cycle 의무 + (j) 진입 자격 = 4/4 모두 충족 *후*

### 2.3 (h)/(h-O)/(h-OM) 답습 영구 의무 cross-check input

- **R-1 anchor**: Ollama daemon pid 3375 + sudo /proc/3375/exe hash `ce95c475...878b10` 답습 영구
- **R-13**: GGUF + Ollama library/Modelfile blob 변경 0건 답습 영구
- **R-S2**: password literal redact (summary/raw report 모두) 답습 영구
- **R-S4**: sudo 1회 의무 자격 별도 분리 (read-only analysis 단계 sudo 0 + raw report 단계 sudo 1회 + page cache drop sudo 추가는 동일 sudo 세션 내 처리, BLOCKING-3 합산)
- **R-15**: self-consistency 영구 (§0 ↔ §7 1:1 매핑)

---

## 3. 측정 절차 (R-rec-16 + R-S2 + R-S4 발효)

### 3.1 측정 도구 + 적용 의무

- **llama.cpp `llama-cli` direct (h) 답습 영구** (B-CONS-2 흡수, llama-server 도입 0건)
- **bash script wrapper** (R-CONS-6 권고, 재현성 + sha256 anchor 자동화)
- **`nvidia-smi` telemetry** (R-CONS-4 권고, GPU clock + power + temp 동시 채취 → `*-telemetry.csv`)
- **Write tool** = (4) raw report commit only
- **R-S2 발효 영구**: password literal redact (summary JSON + raw report 모두)

### 3.2 측정 순서 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 형식 |
|---|---|---|
| (1) brief v1 작성 + commit | `0fc26fb`, 341줄 | 완료 |
| (2) 풀 3+1 합의 + commit | `6dcd8c9`, 270줄, APPROVE w/ COND BLOCKING 11 + R-S1~R-S4 + 권고 6 + NOTE 10 | 완료 |
| (3) brief v1.1 보강 + commit (본 단계) | BLOCKING 11 verbatim 100% + R-S1~R-S4 흡수 + 권고 6 일부 + §11 v→v1.1 일람 신규 | **진행 중** |
| (4) 측정 실행 + raw report commit | §9 확정안 답습 + 측정 (sudo 1회 + 임시 비밀번호 + N=3 × 2 prompt = 6 runs + 분산 분석 + R-S2 발효 redact 3-spot verify) | 합의 + 사용자 명시 후 (임시 비밀번호 발급) |
| (5) SESSION 21번째 + INDEX + commit (R-1 anchor 27회 sudo 1회 R-S4 발효) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

### 3.3 측정 후 cross-check 의무 (R-S2 + R-S4 + R-S5 답습 + BLOCKING-3/6/12 흡수)

- 측정 raw report (txt/log/json) 모두 정합성 verify (분모/단위/timestamp 일관)
- **R-1 anchor 27회 누계 일관 verify**: sudo /proc/3375/exe sha256 = `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` 일치 (silent 교체 0건). 산술 verify (A-N-A4): (h)=15 → (h-O)=19 → (h-OM)=23 → (R4-evidence)=24 → (R4-body)=25 → (4-way)=26 → (h)'=**27** ✓
- **R-13 답습 영구 verify**: GGUF sha256 = `382b4f5a164d...33a95` (R-13) + 17.353 GiB 디스크 사용 보존
- **R-7 격리 verify**: apt snapshot 변동 0 + Ollama egress 자연 변동 only (h)/(h-O)/(h-OM) 답습
- **헌법/ADR/다른 문서 본문 변경 0건 verify (R-9 답습 영구)**: `git diff docs/constitution/ docs/decisions/ docs/architecture/ docs/guides/ CLAUDE.md` = 0 (단 본 cycle commit = brief + 합의 + raw report + SESSION + INDEX 제외)
- **`src/jarvis/` 코드 변경 0건 verify (R-S1 답습 영구, BLOCKING-12 답습)**: `git diff src/jarvis/boss.py src/jarvis/orchestrator.py src/jarvis/approval.py tests/jarvis/test_boss_advisory.py` = 0
- **GPU/system telemetry verify (R-CONS-4)**: `*-telemetry.csv` 채취, thermal cold-1 vs cold-3 swing < 12% 확인 (craftrigs 외부 evidence 답습)
- **비밀번호 누출 verify 3-spot (R-S2 발효 영구, B-CONS-6 흡수)**:
  - **timing 1 — 측정 *직후***: 1차 적중 시 즉시 redact → 0건 재verify
  - **timing 2 — commit *전***: `grep -ri 'epff' docs/phase0/v1-poc-raw/phase3-5-h-prime/` = 0건 (case-insensitive)
  - **timing 3 — push *전***: 동일 grep + `git log -p HEAD -- docs/phase0/v1-poc-raw/phase3-5-h-prime/` history grep 0건

### 3.4 임시 비밀번호 life-cycle 의무 (B-CONS-1 ⭐⭐⭐ CRITICAL 흡수, 헌법 8조 본질 답습 영구)

본 cycle 측정 단계 (4) 시 sudo 1회 (page cache drop + R-1 anchor /proc/3375/exe sha256 readlink) 의무 → 사용자 명시 임시 비밀번호 발급 의무. **임시 비밀번호 = 일회용 (one-time) + 사용 후 즉시 폐기 의무 영구**:

1. **사용 *전* (발급 단계)**:
   - 사용자 직접 발급 (Claude 메모리/log/history 0건 의무)
   - 사용자 → Claude prompt input 직접 전달 (intermediate storage 0건)

2. **사용 *중* (측정 단계 (4) 실행)**:
   - sudo authentication 1회 only
   - shell history 차단: `unset HISTFILE` 또는 `export HISTCONTROL=ignorespace` + 명령 앞 space 1개 prefix
   - bash script 사용 시 = env var (literal 직접 사용 0건) 또는 `sudo -S` stdin pipe (echo 사용 시 `HISTCONTROL=ignoreboth` 필수)

3. **사용 *후* (즉시 폐기)**:
   - 사용자 직접 OS-level 변경 또는 만료 (사용자 의무, Claude 권한 0건)
   - chain 영구 종결 의무 답습 = 재사용 0건 의무 영구

4. **누출 verify (R-S2 발효 영구 cascade)**:
   - summary JSON + raw report + bash log + journal + history 모두 grep `<password-prefix-4자>` = 0건 verify (B-CONS-8 흡수)
   - 1차 적중 시 즉시 redact → 0건 재verify ((R4-evidence)/(R4-body)/(4-way) 답습 영구)

5. **재사용 0건 의무 영구**:
   - 본 cycle 측정 1회 사용 *일회용* (one-time)
   - 후속 cycle 진입 시 = 별도 신규 임시 비밀번호 발급 의무
   - chain 영구 종결 의무 답습 영구

---

## 4. 측정 후 영향 평가 (헌법/ADR cascade 0건 + Provider Liquidity 본질 답습)

### 4.1 헌법 5조-2 (Provider Liquidity, 비협상) 답습 정합

- 헌법 5조-2 본문 변경 0건 의무 답습 영구
- Provider Liquidity 원칙 약화 0건 (본 cycle = LlamaCppBoss 단독 분산 검증, OllamaBoss / vLLMBoss 비교 0건)
- (h)' 결과 = LlamaCppBoss N=3 분산 input only, Provider 선택 *결정* 0건 ((k) 별도 cycle)

### 4.2 ADR-011 §2.1 5조건 답습 정합

- ADR-011 §2.1 5조건 (a)~(e) 답습 권위
- 본 cycle = LlamaCppBoss 단독 분산 검증 = (j) 진입 선결 의무 충족 input
- **ADR-011 본문 변경 0건 의무 답습 영구**

### 4.3 헌법 8조 (보안 원칙) 답습 정합 (B-CONS-1 흡수)

- 헌법 8조 본질 = 보안 결과 달성 의무
- 본 cycle = 임시 비밀번호 life-cycle 5 항목 답습 영구 (§3.4) = 헌법 8조 본질 직접 실현

### 4.4 다른 ADR 답습 정합

- ADR-001~ADR-010 + ADR-012 본문 변경 0건 의무 답습 영구

### 4.5 다른 문서 답습 정합 (R-S5 답습 cascade scope 확장)

- CLAUDE.md / docs/architecture/ / docs/guides/ / 메모리 본문 변경 0건 의무 답습 영구
- 다른 phase0/ brief / review/ 합의 보고서 본문 변경 0건 의무 답습 영구
- docs/sessions/ + INDEX.md 본문 변경 0건 의무 답습 영구 (단 본 cycle SESSION 21번째 entry 추가 + INDEX 추가는 별도)

---

## 5. 측정 결과 사전 명문 (§9 답습 의무, 본 v1.1 = 합의 BLOCKING + R-S* 흡수 후 확정안)

본 brief v1.1 §9 = 합의 BLOCKING 11 + R-S1~R-S4 흡수 후 *확정안*. 단계 (4) 측정 실행 + raw report commit 시 §9 확정안 답습.

---

## 6. 정직성 한계 (R-6 답습, 19 항목)

1. 본 cycle = LlamaCppBoss N=3 분산 측정 cycle ((h) 답습) — sensitivity 중간 (단일 변수 분산 검증)
2. scope 한정 = decode-161tok generation + prefill-2k prompt 각 N=3 cold (총 6 measurement runs)
3. 헌법/ADR cascade 0건 의무 답습 영구
4. Provider Liquidity 본질 답습 영구 (본 cycle = LlamaCppBoss 단독, OllamaBoss/vLLMBoss 비교 0건)
5. (h) raw evidence 답습 정직성 (49.6 t/s = N=1 single, (h)' = N=3 분산 검증 — (h) 자체 invalidate 0건 의무, mean ± CV bound 비교 자격 only)
6. 결정 *고정* 자격 무관 ((k) 별도 cycle)
7. 6단계 변형 entry form (R-rec-16 답습)
8. 본 cycle = (4-way) REC-3 신규 carry-over 직접 후속 + R-S4 발효 (j) 진입 선결 의무 1/4 충족
9. (h)'-X prime/super-prime 자동 진입 명백 부정 답습 영구
10. 본 cycle 결과 메모리 등재 자격 = 사용자 명시 의무
11. 본 cycle 본문 정정 0건 (별도 cycle 의무)
12. (j) advisory wall-clock 측정 자격 0건 ((j) 별도 cycle, 본 cycle = 선결 의무 충족 input only)
13. **R-S2 발효 영구** — password literal redact 답습 (summary/raw report 모두, 1차 적중 시 즉시 redact → 0건 재verify 답습, B-CONS-1 + B-CONS-6 + B-CONS-8 흡수)
14. **R-S4 발효** — R-1 anchor 27회 sudo 1회 의무 자격 별도 분리 (read-only analysis 단계 sudo 0 + raw report 단계 sudo 1회, page cache drop sudo 추가는 동일 sudo 세션 내 처리)
15. **R-S1 답습 영구** — 기존 `src/jarvis/boss.py` 변경 0건 의무 ((4-way) 답습 영구). **(4-way) brief 답습 "99줄" vs 실측 "98줄" 1줄 차이는 본 cycle 정정 0건, 별도 cascade cycle (LOW) 자격 (N-CONS-3)**
16. **[B-CONS-4 흡수 신규] N=3 sample std 자체 통계적 한계 정직성 영구** — N=3 sample std (Bessel's N-1=2) = stddev point estimate (95% CI for σ at N=3 = chi-square `[0.52σ, 6.28σ]` 광범). CV threshold (5%/10% 등) 자격 = informal heuristic only, formal hypothesis test 자격 0. **외부 best-practice N=10 minimum (craftrigs 답습, "3 reps → stddev 6-8%, 10 reps → 2-4%, 10 = minimum that survives scrutiny")** — 본 cycle = 분산 *exploratory* 검증 only, *confirmatory* 0건 정직성. **후속 N=10 escalation carry-over LOW** 신규
17. **[B-CONS-3 흡수 신규] thermal/GPU state 변동 정직성 영구** — run-1 vs run-3 분산 원천 가능 (craftrigs 외부 reference: thermal throttling 12-18% swing cold vs stabilized). delta% 통한 thermal vs intrinsic 분리 자격 0건, raw report telemetry log 답습 only (R-CONS-4)
18. **[B-CONS-5 흡수 신규] (h) 비교 = inclusion test only 정직성 영구** — (h) N=1 vs (h)' N=3 = Welch's t-test 부적격 (N=1 분산 미정). 본 cycle 비교 = inclusion test multi-metric ([μ-σ] + [μ-2σ] + [min,max] + delta%) qualitative input only, statistical equivalence test 자격 0건
19. **[B-CONS-1 흡수 신규] 임시 비밀번호 life-cycle 의무 영구** — 일회용 + 사용 *전* 사용자 직접 발급 + 사용 *중* HISTCONTROL=ignorespace + 사용 *후* 즉시 폐기 + grep 0건 verify + 재사용 0건 = 헌법 8조 본질 보안 결과 직접 실현 의무 (§3.4 답습 영구)

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 *하지 않는 것* 15 항목과 §7 차단 조건은 **1:1 매핑 의무**.

1. ❌ (h) bartowski GGUF 변경 (R-13)
2. ❌ llama.cpp HEAD 변경 (R-13)
3. ❌ (h)/(h-O)/(h-OM) raw report 변경 (read-only)
4. ❌ 헌법 / ADR / 다른 문서 본문 변경 (R-9)
5. ❌ MVP-1 brief / 합의 보고서 / (4-way) brief / Boss 추상화 design doc 본문 변경 (R-9)
6. ❌ Ollama daemon 변경 (pid 3375 보존)
7. ❌ Ollama library/Modelfile blob 변경 (R-13)
8. ❌ (k) M3·M4 결정 *고정*
9. ❌ (j) advisory wall-clock 측정
10. ❌ 테스트 작성/실행
11. ❌ `src/jarvis/` 코드 변경 (R-S1 답습 영구, "98줄" 실측 본 cycle 정정 0건)
12. ❌ 메모리 자동 갱신
13. ❌ brief commit / 합의 commit / raw report commit / SESSION commit / push 자동 진입
14. ❌ **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) + (h)'-X prime/super-prime 자동 진입** (chain 영구 종결 — **8 chain 전체 자동 진입 금지 1:1 매핑 verbatim 답습 영구**, R-S1 + BLOCKING-10 흡수)
15. ❌ **password literal 직접 사용** (R-S2 발효 영구, summary/raw report 모두 redact 의무, BLOCKING-9 흡수)

---

## 8. 본 cycle 진입 자격 평가 (R-rec-12 답습)

### 8.1 carry-over 자격 매트릭스 + (j) 진입 선결 4 verbatim (BLOCKING-10 + R-S4 흡수)

| carry-over | 출처 | scope | 본 cycle 적합도 |
|---|---|---|---|
| **(h)' LlamaCppBoss N=3 분산 측정 MEDIUM** | (4-way) REC-3 신규 + R-S4 발효 | (h) 단일 측정 분산 미확인 → N=3 검증 | ⭐⭐⭐ 본 cycle 자체 |
| **(j) 진입 선결 4 carry-over verbatim 답습 영구 (R-S4 + BLOCKING-10 흡수)** | | | |
| ・ Phase 1 N=3 repetitions Ollama 답습 MEDIUM | C-S2 답습 | Ollama 분산 검증 필수 | ❌ 본 cycle scope 외 (별도 MEDIUM cycle, (j) 선결 4/4 중 1번째) |
| ・ **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 MEDIUM** (본 cycle) | REC-3 신규 | (h) 단일 측정 분산 미확인 | ⭐⭐⭐ **(j) 선결 4/4 중 2번째 충족 자격** |
| ・ Ollama embedded llama.cpp version verify MEDIUM | (h-O) R-S4 답습 | 변수 분리 | ❌ 본 cycle scope 외 (3번째) |
| ・ Ollama prefill processing framework overhead 검증 MEDIUM | F-4 (h-OM) 답습 | prefill 격차 본질 | ❌ 본 cycle scope 외 (4번째) |
| (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM | (h-O)/(h-OM) R-15 답습 | 5-way confirm | ❌ 본 cycle scope 외 |
| (m) F2 model size 단독 분리 cycle MEDIUM | (4-way) REC-1 신규 | F2 model size 변수 분리 | ❌ 본 cycle scope 외 |
| (R4-body) 완료 후 cascade 검토 cycle LOW | (R4-body) §8 R-10 + (4-way) R-S3 답습 | cascade verify | ❌ 본 cycle scope 외 |
| vLLM verify cycle LOW | (R4-body) §8 R-9 답습 | vLLM 부분 evidence | ❌ 본 cycle scope 외 |
| (j) advisory wall-clock 측정 MEDIUM | (4-way) §7.5 | (j) 측정 cycle | ❌ 본 cycle scope 외 ((j) 진입 선결 4 충족 후) |
| (k) M3·M4 결정 *고정* DEFER | 답습 영구 | (k) 별도 cycle | ❌ 변수 분리 input 강화 후 |
| (l) MVP-1 트랙 B 구현 DEFER | 답습 영구 | (k) 통과 후 | ❌ (k) 통과 의무 |

### 8.2 본 cycle 자격 충족 verify

- ✅ (4-way) §9 REC-3 신규 carry-over MEDIUM 직접 후속 자격
- ✅ (4-way) R-S4 발효 (j) 진입 선결 의무 1/4 충족 자격 (수행 *완료* 자체가 input, R-CONS-3 흡수)
- ✅ 사용자 명시 "(h)' LlamaCppBoss N=3 분산 측정 MEDIUM (REC-3 신규, (j) 진입 선결)" 답습
- ✅ 사용자 명시 scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 measurement runs
- ✅ 사용자 명시 수단 = sudo 포함 (R-1 anchor 27회, 임시 비밀번호 발급 필요)
- ✅ chain 영구 종결 의무 답습 영구 ((h)' 단독 명명, 8 chain 전체 자동 진입 금지 verbatim)
- ✅ R-9 답습 영구 (본문 정정 0건 의무)
- ✅ R-S1 답습 영구 (기존 boss.py 98줄 변경 0건 의무)
- ✅ 6단계 변형 entry form (R-rec-16 답습)

### 8.3 본 brief 자체 후속 단계 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `0fc26fb`, 341줄 | 명시 완료 |
| (2) 풀 3+1 합의 진행 + commit | `6dcd8c9`, 270줄, APPROVE w/ COND BLOCKING 11 + R-S1~R-S4 + 권고 6 + NOTE 10 | 명시 완료 |
| **(3) brief v1.1 보강 + commit (본 단계)** | BLOCKING 11 verbatim 100% + R-S1~R-S4 흡수 + 권고 6 일부 + §11 v→v1.1 일람 신규 | **진행 중** |
| (4) 측정 실행 + raw report commit | §9 확정안 답습 + 측정 (sudo 1회 + 임시 비밀번호 + N=3 × 2 prompt = 6 runs + 분산 분석 + R-S2 발효 redact 3-spot) | 합의 + 사용자 명시 후 (임시 비밀번호 발급) |
| (5) SESSION 21번째 + INDEX + commit (R-1 anchor 27회 sudo 1회 R-S4 발효) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. 측정 본문 확정안 (BLOCKING 11 + R-S1~R-S4 흡수, 단계 (4) 실행 시 답습)

### 9.1 측정 명령 확정안 (BLOCKING-2 흡수, (h) 실 답습 명령 verbatim)

**(h) 실 답습 명령 verbatim 100% 고정 (B-CONS-2 흡수, A-B-A1 verbatim)**:

```bash
# (h) raw 답습: llama-cli interactive mode + stdin pipe + F8 hang + timeout 300s
# 새 명령 도입 0건 (변수 추가 = N=3 분산 본질 침범 회피)

# 매 측정 *전* cold 절차 (BLOCKING-3):
#   pkill -9 llama-cli
#   nvidia-smi --query-gpu=memory.used --format=csv  # 0 또는 idle 확인
#   sync && sudo sh -c 'echo 3 > /proc/sys/vm/drop_caches'  # page cache drop
#   sleep 60  # (권고 R-CONS-1) thermal cooldown wait

# decode-161tok generation (input = /tmp/v1-poc-prompts/decode-prompt.json, 705 bytes)
timeout 300 ./llama-cli \
  --model /path/to/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  -no-cnv \
  --temp 0 --seed 42 \
  --n-predict 161 \
  < /dev/null \
  > measure-decode-cold-N.log 2>&1

# F8 답습 영구 (R-CONS-1): -no-cnv flag 의도 미작동, < /dev/null stdin 차단 +
# timeout 300s 적용 후에도 perf line 출력 후 interactive hang 발생. exit 124
# (timeout) 또는 EOF. perf line은 hang 발생 *전* 정상 출력.

# prefill-2k prompt (input = /tmp/v1-poc-prompts/prefill-2k-precheck.json, 11524 bytes)
timeout 300 ./llama-cli \
  --model /path/to/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  -no-cnv \
  --temp 0 --seed 42 \
  --n-predict 1 \
  < /dev/null \
  > measure-prefill-cold-N.log 2>&1
```

**대안 도구 매트릭스 (R-CONS-2 격하 권고, 본 cycle 채택 0건, 후속 carry-over LOW)**:

| 도구 | 측정 자격 | 트레이드오프 | 본 cycle 채택 |
|---|---|---|---|
| `llama-cli` direct + bash wrapper (본 cycle) | ⭐⭐⭐ (h) 동형 prompt 답습 자격 | + (h) 답습 정합성 / - 분산 산출 = custom bash | ⭐⭐⭐ |
| `llama-bench --reps 5` | ⭐⭐ 표준 도구 | + JSON 내장 (avg_ts/stddev_ts) / - synthetic pp/tg only ((h) prompt 답습 부적격) | ❌ (후속 carry-over LOW) |
| 양쪽 동시 측정 | ⭐⭐ 추가 자격 | + cross-check 자격 / - cycle 시간 +30~50% | ❌ (후속 carry-over LOW) |

### 9.2 분산 분석 산출 multi-metric 확정안 (BLOCKING-5 흡수)

**산출 metrics**:

| metric | 정의 | 단위 |
|---|---|---|
| **mean (μ)** | (t₁ + t₂ + t₃) / 3 | t/s |
| **stddev (σ)** | sample std (Bessel's correction, N-1=2) | t/s |
| **min** | min(t₁, t₂, t₃) | t/s |
| **max** | max(t₁, t₂, t₃) | t/s |
| **CV (변동계수)** | σ/μ × 100% | % |
| **(h) ∈ [μ - σ, μ + σ]** | ≈68% inclusion (normality 가정) | bool |
| **(h) ∈ [μ - 2σ, μ + 2σ]** | ≈95% inclusion (normality 가정) | bool |
| **(h) ∈ [min, max]** | range inclusion (non-parametric) | bool |
| **delta% ((h) - μ)** | ((h) - μ) / μ × 100% | % |

**Welch's t-test (N=1 vs N=3) 부적격 명문 (B-CONS-5)**: (h) = N=1 single → 분산 미정 → t-test 자체 부적격. 본 cycle 비교 = **inclusion test only**, statistical equivalence test 자격 0건.

**raw samples 보존 (REC-C2 권고 흡수)**: t₁, t₂, t₃ 값 자체 summary JSON `samples_ts` 배열 보존 → 후속 cycle median/IQR/MAD (non-parametric robust statistics) 재산출 자격.

**예상 결과 매트릭스 (사전 명문, 측정 후 확정)**:

| prompt | t₁ | t₂ | t₃ | μ | σ | min | max | CV% | (h) [μ±σ] | (h) [μ±2σ] | (h) [min,max] | delta% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| decode-161tok generation | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | (h)=49.6 | bool | bool | TBD |
| prefill-2k prompt | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | (h)=1916.8 | bool | bool | TBD |

### 9.3 raw report 파일 사전 명문 (BLOCKING-7 + BLOCKING-11 흡수)

**raw report 디렉토리**: `docs/phase0/v1-poc-raw/phase3-5-h-prime/` ((h)/(h-O)/(h-OM) 답습 패턴 일관, R-S2 발효 답습 영구)

**파일 list (사전 명문)**:
- `2026-05-26THH-MM-phase3-5-h-prime-summary.json` (분산 분석 종합, multi-metric)
- `2026-05-26THH-MM-phase3-5-h-prime-decode-prompt-input.json` (prompt cp 영구 보존, B-CONS-7)
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-2k-prompt-input.json` (prompt cp 영구 보존, B-CONS-7)
- `2026-05-26THH-MM-phase3-5-h-prime-prompt-sha256.txt` (prompt sha256 anchor, B-CONS-7)
- `2026-05-26THH-MM-phase3-5-h-prime-decode-cold-1.{log,json}` (run-1)
- `2026-05-26THH-MM-phase3-5-h-prime-decode-cold-2.{log,json}` (run-2)
- `2026-05-26THH-MM-phase3-5-h-prime-decode-cold-3.{log,json}` (run-3)
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-cold-1.{log,json}` (run-1)
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-cold-2.{log,json}` (run-2)
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-cold-3.{log,json}` (run-3)
- `2026-05-26THH-MM-phase3-5-h-prime-telemetry.csv` (nvidia-smi GPU clock + power + temp, R-CONS-4)
- `2026-05-26THH-MM-phase3-5-h-prime-r1-anchor-27x.txt` (R-1 anchor sudo /proc/3375/exe sha256 verify)
- `2026-05-26THH-MM-phase3-5-h-prime-r7-isolation.{txt,log}` (apt 변동 + Ollama egress verify)
- `2026-05-26THH-MM-phase3-5-h-prime-cascade-verify.txt` (헌법/ADR/src/jarvis 변경 0건 git diff verify)
- (선택) bash script wrapper 자체 = `2026-05-26THH-MM-phase3-5-h-prime-measure.sh` (R-CONS-6 권고)

**약 ~14~16 파일** ((h)/(h-O)/(h-OM) 답습 답습 패턴)

### 9.4 R-S2 발효 영구 password redact 의무 확정안 (BLOCKING-6 + BLOCKING-8 흡수)

**redact placeholder + grep pattern 사전 명문 (B-CONS-8)**:
- **redact placeholder string (고정)**: `***REDACTED-SUDO-PWD***`
- **grep pattern (case-insensitive)**:
  - prefix 4자 grep: `grep -ri 'epff' docs/phase0/v1-poc-raw/phase3-5-h-prime/ = 0건`
  - 전체 literal grep: `grep -ri '<literal-pwd>' docs/phase0/v1-poc-raw/phase3-5-h-prime/ = 0건`

**verify 3-spot timing (B-CONS-6 흡수, R-S3)**:
1. **timing 1 — 측정 *직후***:
   - bash script 종료 직후 자동 grep verify
   - 1차 적중 시 즉시 redact → 0건 재verify
2. **timing 2 — commit *전***:
   - `git add` 직전 `grep -ri 'epff' docs/phase0/v1-poc-raw/phase3-5-h-prime/ = 0건` (case-insensitive) 강제
   - 적중 시 commit 차단 + 즉시 redact → 재verify
3. **timing 3 — push *전***:
   - `git push` 직전 `git log -p HEAD --all -- docs/phase0/v1-poc-raw/phase3-5-h-prime/ | grep -i 'epff'` = 0건 강제
   - 적중 시 push 차단 + history rewrite (별도 절차 명시 의무)

**summary JSON `sudo_authorization` field 사전 명문**:
```json
{
  "sudo_authorization": "***REDACTED-SUDO-PWD***",
  "password_leak_verification": {
    "method": "grep -ri 'epff' docs/phase0/v1-poc-raw/phase3-5-h-prime/",
    "timing_1_post_measurement": "PASS (0 matches)",
    "timing_2_pre_commit": "PASS (0 matches)",
    "timing_3_pre_push": "PASS (0 matches)"
  }
}
```

### 9.5 (j) 진입 선결 의무 충족 평가 (R-S4 + R-CONS-3 흡수)

- 본 cycle 결과 = LlamaCppBoss N=3 분산 검증 *완료* → **(j) 진입 선결 4 중 2번째 충족** (REC-3 답습)
- **충족 조건 = 수행 자체 (CV 결과 무관, 분산 검증 *완료* 자체가 input, R-CONS-3 흡수)**
- 나머지 3 carry-over (Phase 1 N=3 / Ollama embedded llama.cpp version / Ollama prefill framework overhead) = 별도 cycle 의무
- 본 cycle 완료 ≠ (j) 진입 자격 충족 (4 carry-over 모두 충족 후)
- 후속 보강 자격: CV% > 8% 시 후속 N=10 escalation cycle MEDIUM carry-over 신규 (B-CONS-4 흡수, NOTE-9)

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = (4-way) 20번째 entry cycle 완주 후 REC-3 신규 carry-over MEDIUM 직접 후속 + R-S4 발효 (j) 진입 선결 의무 1/4 충족 자격 + 본 cycle 풀 3+1 합의 (`6dcd8c9`) BLOCKING 11 + R-S1~R-S4 흡수
- ⭐⭐⭐ **B-CONS-1 CRITICAL 흡수** = 임시 비밀번호 life-cycle 5 항목 영구 (§3.4) — 헌법 8조 본질 보안 결과 직접 실현
- ⭐⭐ B-CONS-2~B-CONS-11 HIGH/MEDIUM 흡수 = (h) 실 답습 명령 + cold 절차 + N=3 통계 한계 + multi-metric + verify 3-spot + prompt source 정정 + redact placeholder + §7 verbatim + chain 8 verbatim + raw report 디렉토리 명명
- ⭐⭐ R-S1~R-S4 Reviewer 단독 격상 흡수
- ⭐⭐ scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 measurement runs (LlamaCppBoss bartowski direct 분산 검증)
- ⭐⭐ 수단 = sudo + R-1 anchor 27회 + 임시 비밀번호 life-cycle 5 항목 + R-S2 발효 redact 3-spot
- ⭐⭐ (j) 진입 선결 의무 1/4 충족 자격 = 수행 자체 (CV 결과 무관, R-CONS-3 흡수)
- ⭐ R-15 self-consistency 영구 — §0 15 항목 ↔ §7 차단 조건 1:1 매핑 (§7 #14 + #15 verbatim 답습)
- ⭐ R-1 anchor 27회 누계 자격 (chain (g)/(h)/(h-O)/(h-OM)/(R4-evidence)/(R4-body)/(4-way)/(h)', sudo 1회 의무 R-S4 발효 자격 별도 분리)
- ⭐ R-S1 답습 영구 — 기존 `src/jarvis/boss.py` 변경 0건 의무
- ⭐ R-9 답습 영구 — 헌법/ADR/다른 문서 본문 변경 0건 의무
- 본 brief 자체 머신 변경 0건 (측정/Modelfile/ollama/sudo/본문 정정 0)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구 (단계 (4) 시 임시 비밀번호 발급 의무)
- **(h)'-X prime/super-prime 자동 진입 명백 부정 답습 영구**

---

## 11. v1 → v1.1 변경 일람 ((4-way)/(R4-body) §11 답습)

### 11.1 BLOCKING 11 흡수 매트릭스 (verbatim 100%, R-21 답습 영구)

| # | 위치 | 흡수 결과 |
|---|---|---|
| BLOCKING-1 (⭐⭐⭐ CRITICAL) | §3 신규 §3.4 + §6 #19 + §4.3 신규 | 임시 비밀번호 life-cycle 5 항목 verbatim (일회용 / 사용 *전* 직접 / 사용 *중* HISTCONTROL / 사용 *후* 즉시 폐기 / 누출 verify cascade / 재사용 0건) + 헌법 8조 본질 답습 |
| BLOCKING-2 (⭐⭐ HIGH) | §9.1 | (h) 실 답습 명령 verbatim 100% (llama-cli + -no-cnv + < /dev/null + timeout 300s + F8 hang) + 새 명령 도입 0건 명문 |
| BLOCKING-3 (⭐⭐ HIGH) | §1.1 + §3.3 + §6 #17 | cold 절차 5 단계 명문 (kill -9 → GPU 0 confirm → page cache drop sudo → 60s thermal cooldown → cold load) + thermal 12-18% swing 정직성 + nvidia-smi telemetry |
| BLOCKING-4 (⭐⭐ HIGH) | §6 #16 신규 | N=3 sample std 통계 한계 (chi-square 95% CI [0.52σ, 6.28σ]) + 외부 best-practice N=10 미달 + CV threshold informal + 후속 N=10 escalation carry-over LOW |
| BLOCKING-5 (⭐⭐ HIGH) | §1.3 + §9.2 + §6 #18 | multi-metric ([μ-σ] + [μ-2σ] + [min,max] + delta%) + Welch's t-test N=1 vs N=3 부적격 명문 + inclusion test only 정직성 |
| BLOCKING-6 (⭐⭐ HIGH) | §3.3 + §9.4 | R-S2 verify 3-spot (측정 *직후* + commit *전* + push *전*) verbatim |
| BLOCKING-7 (⭐⭐ HIGH) | §1.2 + §9.3 | prompt source 정정 (실제 = /tmp/v1-poc-prompts/decode-prompt.json + prefill-2k-precheck.json) + R-7 격리 외 정직성 + cp 영구 보존 + sha256 anchor |
| BLOCKING-8 (⭐⭐ HIGH) | §9.4 | redact placeholder `***REDACTED-SUDO-PWD***` 고정 + grep pattern (prefix 4자 'epff' case-insensitive + 전체 literal) 사전 명문 |
| BLOCKING-9 (⭐ MEDIUM) | §0 #15 + §7 #15 | §7 #15 verbatim 답습 (R-S2 발효 영구, summary/raw report 모두 redact 의무) - §0 ↔ §7 1:1 매핑 강화 |
| BLOCKING-10 (⭐⭐ HIGH) | §0 #14 + §7 #14 + §8.1 | chain 8 chain 전체 자동 진입 금지 verbatim ((g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) + (h)'-X) + (j) 진입 선결 4 carry-over verbatim 답습 영구 |
| BLOCKING-11 (⭐ MEDIUM) | §9.3 | raw report 디렉토리 명명 `phase3-5-h-prime/` 답습 영구 + (h)/(h-O)/(h-OM) 답습 패턴 일관 verify 명문 |

### 11.2 Reviewer 단독 격상 R-S* 4 흡수 매트릭스

| R-S | 위치 | 흡수 결과 |
|---|---|---|
| R-S1 | §0 #14 + §7 #14 + §10 | chain 8 chain 전체 자동 진입 금지 verbatim 1:1 매핑 (BLOCKING-10 합산) |
| R-S2 | §9.3 + §10 | raw report 디렉토리 명명 `phase3-5-h-prime/` 답습 영구 (BLOCKING-11 합산) |
| R-S3 | §3.3 + §9.4 | R-S2 발효 영구 verify 3-spot timing (측정 *직후* + commit *전* + push *전*) (BLOCKING-6 합산) |
| R-S4 | §2.2 + §8.1 + §9.5 | (j) 진입 선결 4 carry-over verbatim 답습 영구 (BLOCKING-10 합산) |

### 11.3 권고 6 흡수 매트릭스 (5 흡수 + 1 명시)

| REC | 흡수 결과 |
|---|---|
| R-CONS-1 | §9.1 F8 interactive hang 답습 영구 명문 + thermal cooldown 60s (R-CONS-1 권고 자격) |
| R-CONS-2 | §9.1 대안 도구 매트릭스 (llama-cli + bash 본 cycle / llama-bench --reps 5 후속 LOW / 양쪽 측정 후속 LOW) |
| R-CONS-3 | §8.2 + §9.5 (j) 충족 조건 = 수행 자체 (CV 결과 무관) 명문 |
| R-CONS-4 | §3.1 + §9.3 nvidia-smi telemetry 채취 (`*-telemetry.csv`) |
| R-CONS-5 | §1.1 측정 매트릭스 4 metric 자격 명문 (decode prompt + generation + prefill prompt + generation 모두 산출 가능) |
| R-CONS-6 | §3.1 + §9.3 bash script wrapper 권고 (재현성 + sha256 anchor 자동화) |

### 11.4 NOTE 10 정직성 명문 (footer)

| NOTE | 정직성 명문 자격 |
|---|---|
| N-CONS-1 | §3.2 (4) sub-step 명문 (R-CONS-1 합산) |
| N-CONS-2 | §2.1 (h) 49.6 답습 정확 verify 완료 |
| N-CONS-3 | §0 #11 boss.py 실측 98줄 vs (4-way) brief "99줄" 1줄 차이 (본질 정합, 별도 cascade cycle LOW 자격) |
| N-CONS-4 | §3.3 R-1 anchor 27회 산술 verify 완료 |
| N-CONS-5 | §1.2 R-13 GGUF sha256 verify 정합 |
| N-CONS-6 | §9.3 raw report 디렉토리 `-prime` 답습 정합 |
| N-CONS-7 | §8.1 (j) 4 carry-over verbatim 매트릭스 답습 정합 |
| N-CONS-8 | §6 #5 (h) invalidate 0건 정직성 |
| N-CONS-9 | §9.5 후속 N=10 escalation carry-over LOW (CV% > 8% trigger) + multi-length prompt carry-over LOW |
| N-CONS-10 | §9.5 외부 benchmark suite (lm-eval/FastChat/LiteBench) MVP-2+ 자격 carry-over |

### 11.5 기각 0 매트릭스

3 Agent 적출 항목 중 기각 0건 (Reviewer 합의 보고서 §10).

C-B-C2 llama-bench BLOCKING 만 격하 권고 R-CONS-2 처리 (기각 아님, 본 cycle 도구 변경 0건 본질 = (h) 답습 우선).

### 11.6 분량 비교

- v1: 341줄
- v1.1: ~590줄 (예상)
- 핵심 신규 절: §3.4 (임시 비밀번호 life-cycle) + §6 #16~#19 신규 정직성 4건 + §9.1 (h) 실 답습 verbatim + §9.2 multi-metric + §9.4 password redact 3-spot + §11 변경 일람
