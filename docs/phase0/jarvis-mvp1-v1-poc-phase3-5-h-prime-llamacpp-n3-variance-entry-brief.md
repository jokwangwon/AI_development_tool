# (h)' LlamaCppBoss bartowski direct N=3 분산 측정 cycle entry brief v1

**일자**: 2026-05-26
**유형**: 진입 brief (Phase 0, 6단계 변형 entry form, R-rec-16 답습)
**선행**: (4-way) 20번째 entry cycle 완주 (chain 영구 종결 의무 답습 영구) + REC-3 신규 carry-over MEDIUM + R-S4 발효 (j) 진입 선결 의무 강화
**자격**: (4-way) §9 carry-over MEDIUM ⭐⭐ "(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle (REC-3 신규)", 사용자 명시 "(h)' LlamaCppBoss N=3 분산 측정 MEDIUM (REC-3 신규, (j) 진입 선결)" + 2 명확화 (scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 측정 + 수단 sudo 포함 R-1 anchor 27회 임시 비밀번호 발급 필요)

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
11. ❌ **`src/jarvis/` 코드 변경** (기존 boss.py 99줄 + orchestrator.py + approval.py + tests/jarvis/test_boss_advisory.py 변경 0건, R-S1 답습 영구)
12. ❌ **메모리 자동 갱신** (사용자 명시 의무)
13. ❌ **brief commit / 합의 commit / raw report commit / SESSION commit / push 자동 진입** (단계 단위 사용자 명시 의무)
14. ❌ **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) + (h)'-X prime/super-prime 자동 진입** (chain 영구 종결 의무 답습 영구)
15. ❌ **password literal 직접 사용** (R-S2 발효 영구, summary/raw report 모두 redact 의무)

---

## 1. 본 cycle scope ((h) 동형 N=3 cold, (4-way) REC-3 직접 후속)

### 1.1 측정 매트릭스 (사용자 명시 "(h) 동형 prompt 2 종 × N=3 cold = 총 6 측정")

| 측정 # | prompt | run | 목적 |
|---|---|---|---|
| 1 | decode-161tok generation | cold-1 | decode generation t/s 분산 검증 |
| 2 | decode-161tok generation | cold-2 | (반복) |
| 3 | decode-161tok generation | cold-3 | (반복) |
| 4 | prefill-2k prompt | cold-1 | prefill prompt t/s 분산 검증 |
| 5 | prefill-2k prompt | cold-2 | (반복) |
| 6 | prefill-2k prompt | cold-3 | (반복) |

**총 6 measurement runs (각 prompt N=3 cold)**:
- cold = 매 측정 *전* model unload (KV cache + prefix cache 초기화) → cold load + first decode
- Ollama prefix cache 비대칭 회피 (h-O R-S3 답습)
- (h) single 49.6 t/s 분산 미확인 → mean + stddev + min/max + CV (coefficient of variation) 산출

### 1.2 측정 대상 (h) 동형 영구 답습

- **모델**: Qwen3-30B-A3B classical MoE Q4_K_M
- **GGUF**: bartowski direct (sha256 `382b4f5a164d...33a95`, 17.353 GiB, R-13 답습 영구)
- **runtime**: llama.cpp `c0c7e147` master (R-13 답습 영구)
- **HW**: DGX Spark GB10 (121GB unified memory, 답습 영구)
- **container/host**: (h) 답습 패턴 (host 직접 또는 동일 container)
- **prompt source**: (h) raw 답습 (`docs/phase0/v1-poc-raw/phase3-5-h/2026-05-25T17-58-phase3-5-h-*.txt` decode-161tok + prefill-2k)

### 1.3 분산 분석 산출

- **mean (μ)**: decode generation + prefill prompt 각 N=3 평균 t/s
- **stddev (σ)**: 표본 표준편차 (sample std)
- **min/max**: N=3 중 최솟값/최댓값
- **CV (변동계수)**: σ/μ × 100% (%) — 분산 정직성 지표
- **(h) single 49.6 t/s 와 비교**: (h)' mean ± CV bound 범위 내 적합도

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

**(4-way) R-S4 발효**:
- "선결 cycle carry-over MEDIUM 4건 모두 (j) 진입 *전* 충족 의무"
- 본 cycle = (j) 진입 선결 4 중 1건 충족

### 2.3 (h)/(h-O)/(h-OM) 답습 영구 의무 cross-check input

- **R-1 anchor**: Ollama daemon pid 3375 + sudo /proc/3375/exe hash `ce95c475...878b10` 답습 영구
- **R-13**: GGUF + Ollama library/Modelfile blob 변경 0건 답습 영구
- **R-S2**: password literal redact (summary/raw report 모두) 답습 영구
- **R-S4**: sudo 1회 의무 자격 별도 분리 (read-only analysis 단계 sudo 0 + raw report 단계 sudo 1회)
- **R-15**: self-consistency 영구 (§0 ↔ §7 1:1 매핑)

---

## 3. 측정 절차 (R-rec-16 + R-S2 + R-S4 발효)

### 3.1 측정 도구 + 적용 의무

- **llama.cpp `llama-server` 또는 `llama-cli`** (h) 답습 패턴 + `--no-warmup` (cold)
- **bash script** + `time` + `jq` (출력 parsing)
- **Write tool** = (4) raw report commit only
- **R-S2 발효 영구**: password literal redact (summary JSON + raw report 모두)

### 3.2 측정 순서 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 형식 |
|---|---|---|
| (1) brief v1 작성 + commit (본 단계) | scope + 수단 + 6단계 변형 + 측정안 사전 명문 | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | Agent A + B + C + Reviewer 통합 합의 + BLOCKING + R-S* | 사용자 명시 후 |
| (3) brief v1.1 보강 + commit | BLOCKING verbatim 100% + R-S* 흡수 + §11 v→v1.1 일람 신규 | 합의 후 |
| (4) 측정 실행 + raw report commit | sudo 1회 (R-1 anchor 27회) + 임시 비밀번호 사용 (R-S2 발효 redact 영구) + (h) 동형 prompt 2 종 × N=3 cold = 총 6 measurement runs + 분산 분석 산출 (mean/stddev/min/max/CV) + summary JSON + raw txt/log/json files | 합의 + 사용자 명시 후 (임시 비밀번호 발급) |
| (5) SESSION 21번째 + INDEX + commit (R-1 anchor 27회 sudo 1회 R-S4 발효 자격) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

### 3.3 측정 후 cross-check 의무 (R-S2 + R-S4 + R-S5 답습)

- 측정 raw report (txt/log/json) 모두 정합성 verify (분모/단위/timestamp 일관)
- **R-1 anchor 27회 누계 일관 verify**: sudo /proc/3375/exe sha256 = `ce95c475432376728311695163fae21c7406998e4c05450e48b7908b78877b10` 일치 (silent 교체 0건)
- **R-13 답습 영구 verify**: GGUF sha256 = `382b4f5a164d...33a95` (R-13) + 17.353 GiB 디스크 사용 보존
- **R-7 격리 verify**: apt snapshot 변동 0 + Ollama egress 자연 변동 only (h)/(h-O)/(h-OM) 답습
- **헌법/ADR/다른 문서 본문 변경 0건 verify**: `git diff docs/constitution/ docs/decisions/ docs/architecture/ docs/guides/ CLAUDE.md` = 0 (단 본 cycle commit = brief + 합의 + raw report + SESSION + INDEX 신규 제외)
- **`src/jarvis/` 코드 변경 0건 verify** (R-S1 답습 영구): `git diff src/jarvis/boss.py orchestrator.py approval.py tests/jarvis/test_boss_advisory.py` = 0
- **비밀번호 누출 verify (R-S2 발효 영구)**: summary JSON + raw report grep `<REDACTED-PWD-PATTERN>` = 0건 (literal password pattern 직접 사용 0건, 1차 적중 시 즉시 redact → 0건 재verify 답습)

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

### 4.3 다른 ADR 답습 정합

- ADR-001~ADR-010 + ADR-012 본문 변경 0건 의무 답습 영구

### 4.4 다른 문서 답습 정합 (R-S5 답습 cascade scope 확장)

- CLAUDE.md / docs/architecture/ / docs/guides/ / 메모리 본문 변경 0건 의무 답습 영구
- 다른 phase0/ brief / review/ 합의 보고서 본문 변경 0건 의무 답습 영구
- docs/sessions/ + INDEX.md 본문 변경 0건 의무 답습 영구 (단 본 cycle SESSION 21번째 entry 추가 + INDEX 추가는 별도)

---

## 5. 측정 결과 사전 명문 (§9 답습 의무, 합의 후 v1.1 보강 후 확정안)

본 brief v1 §9 = 합의 *전* 사전 명문 측정 매트릭스. 단계 (3) brief v1.1 보강 시 합의 BLOCKING + R-S* 흡수 후 *확정안*. 단계 (4) 측정 실행 + raw report commit 시 §9 확정안 답습.

---

## 6. 정직성 한계 (R-6 답습, 15 항목)

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
13. **R-S2 발효 영구** — password literal redact 답습 (summary/raw report 모두, 1차 적중 시 즉시 redact → 0건 재verify 답습)
14. **R-S4 발효** — R-1 anchor 27회 sudo 1회 의무 자격 별도 분리 (read-only analysis 단계 sudo 0 + raw report 단계 sudo 1회)
15. **R-S1 답습 영구** — 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) 변경 0건 의무 ((4-way) 답습 영구)

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
11. ❌ `src/jarvis/` 코드 변경 (R-S1 답습 영구)
12. ❌ 메모리 자동 갱신
13. ❌ brief commit / 합의 commit / raw report commit / SESSION commit / push 자동 진입
14. ❌ (g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) + **(h)'-X** prime/super-prime 자동 진입 (chain 영구 종결)
15. ❌ password literal 직접 사용 (R-S2 발효 영구)

---

## 8. 본 cycle 진입 자격 평가 (R-rec-12 답습)

### 8.1 carry-over 자격 매트릭스

| carry-over | 출처 | scope | 본 cycle 적합도 |
|---|---|---|---|
| (h)' LlamaCppBoss N=3 분산 측정 MEDIUM | (4-way) REC-3 신규 + R-S4 발효 | (h) 단일 측정 분산 미확인 → N=3 검증 | ⭐⭐⭐ 본 cycle 자체 |
| Phase 1 N=3 repetitions Ollama 답습 MEDIUM | C-S2 답습 | Ollama 분산 검증 | ❌ 본 cycle scope 외 (별도 MEDIUM cycle, (j) 선결 4/4 중 2번째) |
| Ollama embedded llama.cpp version verify MEDIUM | (h-O) R-S4 답습 | 변수 분리 | ❌ 본 cycle scope 외 |
| Ollama prefill processing framework overhead 검증 MEDIUM | F-4 (h-OM) 답습 | prefill 격차 본질 | ❌ 본 cycle scope 외 |
| (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM | (h-O)/(h-OM) R-15 답습 | 5-way confirm | ❌ 본 cycle scope 외 |
| (m) F2 model size 단독 분리 cycle MEDIUM | (4-way) REC-1 신규 | F2 model size 변수 분리 | ❌ 본 cycle scope 외 |
| (R4-body) 완료 후 cascade 검토 cycle LOW | (R4-body) §8 R-10 + (4-way) R-S3 답습 | cascade verify | ❌ 본 cycle scope 외 |
| vLLM verify cycle LOW | (R4-body) §8 R-9 답습 | vLLM 부분 evidence | ❌ 본 cycle scope 외 |
| (j) advisory wall-clock 측정 MEDIUM | (4-way) §7.5 | (j) 측정 cycle | ❌ 본 cycle scope 외 ((j) 진입 선결 4 충족 후) |
| (k) M3·M4 결정 *고정* DEFER | 답습 영구 | (k) 별도 cycle | ❌ 변수 분리 input 강화 후 |
| (l) MVP-1 트랙 B 구현 DEFER | 답습 영구 | (k) 통과 후 | ❌ (k) 통과 의무 |

### 8.2 본 cycle 자격 충족 verify

- ✅ (4-way) §9 REC-3 신규 carry-over MEDIUM 직접 후속 자격
- ✅ (4-way) R-S4 발효 (j) 진입 선결 의무 1/4 충족 자격
- ✅ 사용자 명시 "(h)' LlamaCppBoss N=3 분산 측정 MEDIUM (REC-3 신규, (j) 진입 선결)" 답습
- ✅ 사용자 명시 scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 measurement runs
- ✅ 사용자 명시 수단 = sudo 포함 (R-1 anchor 27회, 임시 비밀번호 발급 필요)
- ✅ chain 영구 종결 의무 답습 영구 ((h)' 단독 명명, (h)'-X prime/super-prime 금지)
- ✅ R-9 답습 영구 (본문 정정 0건 의무)
- ✅ R-S1 답습 영구 (기존 boss.py 99줄 변경 0건 의무)
- ✅ 6단계 변형 entry form (R-rec-16 답습)

### 8.3 본 brief 자체 후속 단계 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit (본 단계) | scope + 수단 + 6단계 변형 + 측정안 사전 명문 | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | 3+1 합의 + BLOCKING + R-S* | 결과 확인 후 |
| (3) brief v1.1 보강 + commit | BLOCKING verbatim 100% + R-S* 흡수 + §11 v→v1.1 일람 신규 | 합의 후 |
| (4) 측정 실행 + raw report commit | §9 확정안 답습 + 측정 (sudo 1회 + 임시 비밀번호 + N=3 × 2 prompt = 6 runs) + 분산 분석 + R-S2 발효 redact | 합의 + 사용자 명시 후 (임시 비밀번호 발급) |
| (5) SESSION 21번째 + INDEX + commit (R-1 anchor 27회 sudo 1회 R-S4 발효) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. 측정 본문 사전 명문 (합의 후 v1.1 흡수, 단계 (4) 실행 시 답습)

### 9.1 측정 명령 사전 명문 (h) 답습 패턴

**llama.cpp 측정 명령 후보** (실 명령 = (h) raw report 답습 영구):

```bash
# (h) 답습 패턴 (실 명령은 (h) raw 답습)
# decode-161tok generation
./llama-server \
  --model /path/to/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  --ctx-size N --batch-size N --no-warmup \
  --port 8080 &

# 또는 llama-cli direct
./llama-cli \
  --model /path/to/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  --prompt-file /path/to/decode-161tok-prompt.txt \
  --n-predict 161 --no-warmup --temp 0 --seed 42

# prefill-2k prompt
./llama-cli \
  --model /path/to/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  --prompt-file /path/to/prefill-2k-prompt.txt \
  --n-predict 1 --no-warmup --temp 0 --seed 42
```

**핵심 옵션 답습**:
- `--no-warmup`: cold load + first decode 답습 (Ollama prefix cache 비대칭 회피)
- `--temp 0` + `--seed 42`: 결정적 출력
- model unload (process kill) 매 측정 *전* 의무

### 9.2 분산 분석 산출 사전 명문

**산출 metrics**:

| metric | 정의 | 단위 |
|---|---|---|
| **mean (μ)** | (t₁ + t₂ + t₃) / 3 | t/s |
| **stddev (σ)** | sample std (Bessel's correction, N-1=2) | t/s |
| **min** | min(t₁, t₂, t₃) | t/s |
| **max** | max(t₁, t₂, t₃) | t/s |
| **CV (변동계수)** | σ/μ × 100% | % |
| **(h) 비교** | (h) 49.6 t/s ∈ [μ - σ, μ + σ] 적합도 | bool + delta% |

**예상 결과 매트릭스** (사전 명문, 측정 후 확정):

| prompt | run-1 | run-2 | run-3 | mean (μ) | stddev (σ) | min | max | CV% | (h) 비교 |
|---|---|---|---|---|---|---|---|---|---|
| decode-161tok generation | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | (h)=49.6, delta% |
| prefill-2k prompt | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | (h)=1916.8, delta% |

### 9.3 raw report 파일 사전 명문

**raw report 디렉토리**: `docs/phase0/v1-poc-raw/phase3-5-h-prime/`

**파일 list (사전 명문)**:
- `2026-05-26THH-MM-phase3-5-h-prime-summary.json` (분산 분석 종합)
- `2026-05-26THH-MM-phase3-5-h-prime-decode-161tok-cold-1.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-decode-161tok-cold-2.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-decode-161tok-cold-3.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-2k-cold-1.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-2k-cold-2.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-prefill-2k-cold-3.{txt,log}`
- `2026-05-26THH-MM-phase3-5-h-prime-r1-anchor-27x.txt` (R-1 anchor sudo /proc/3375/exe sha256 verify)
- `2026-05-26THH-MM-phase3-5-h-prime-r7-isolation.{txt,log}` (apt 변동 + Ollama egress verify)

**약 ~10~14 파일** ((h)/(h-O)/(h-OM) 답습 답습 패턴)

### 9.4 R-S2 발효 영구 password redact 의무

- summary JSON sudo_authorization 필드 = `<REDACTED-PWD-PATTERN>` 답습 영구
- raw report 모든 파일 grep `<password-prefix>` = 0건 verify 의무
- 1차 적중 시 즉시 redact → 0건 재verify 답습 ((R4-evidence)/(R4-body)/(4-way) 답습 영구)

### 9.5 (j) 진입 선결 의무 충족 평가

- 본 cycle 결과 = LlamaCppBoss N=3 분산 검증 완료 → **(j) 진입 선결 4 중 1번째 충족** (REC-3 답습)
- 나머지 3 carry-over (Phase 1 N=3 / Ollama embedded llama.cpp version / Ollama prefill framework overhead) = 별도 cycle 의무
- 본 cycle 완료 ≠ (j) 진입 자격 충족 (4 carry-over 모두 충족 후)

---

## 10. 본 brief v1 본 cycle 진입 자체 영구 권위

- 본 brief v1 = (4-way) 20번째 entry cycle 완주 후 REC-3 신규 carry-over MEDIUM 직접 후속 + R-S4 발효 (j) 진입 선결 의무 1/4 충족 자격
- ⭐⭐⭐ scope = (h) 동형 prompt 2 종 × N=3 cold = 총 6 measurement runs (LlamaCppBoss bartowski direct 분산 검증)
- ⭐⭐⭐ 수단 = sudo + R-1 anchor 27회 + 임시 비밀번호 발급 + R-S2 발효 redact 영구
- ⭐⭐ (j) 진입 선결 의무 1/4 충족 자격 (R-S4 발효 답습)
- ⭐⭐ R-15 self-consistency 영구 — §0 15 항목 ↔ §7 차단 조건 1:1 매핑
- ⭐ R-1 anchor 27회 누계 자격 (chain (g)/(h)/(h-O)/(h-OM)/(R4-evidence)/(R4-body)/(4-way)/(h)', sudo 1회 의무 R-S4 발효 자격 별도 분리)
- ⭐ R-S1 답습 영구 — 기존 `src/jarvis/boss.py` 99줄 변경 0건 의무
- ⭐ R-9 답습 영구 — 헌법/ADR/다른 문서 본문 변경 0건 의무
- 본 brief 자체 머신 변경 0건 (측정/Modelfile/ollama/sudo/본문 정정 0)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구
- **(h)'-X prime/super-prime 자동 진입 명백 부정 답습 영구**
