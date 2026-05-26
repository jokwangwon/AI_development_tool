# (4-way) MVP-1 4 차원 통합 *분석* cycle entry brief v1.1

**일자**: 2026-05-26 (v1 `af7ac8b` 371줄 → v1.1 보강 본)
**유형**: 진입 brief (Phase 0, 6단계 변형 entry form, R-rec-16 답습)
**선행**: (R4-body) 19번째 entry cycle 완주 (chain 영구 종결 의무 답습 영구) + 본 cycle 풀 3+1 합의 (`5dcbbdb`) APPROVE w/ COND BLOCKING 15 + R-S1~R-S4 답습
**자격**: (R4-body) §8 carry-over HIGH ⭐⭐ 상위 scope, 사용자 명시 "(4-way) 통합 *분석* cycle HIGH (상위 scope)" + 2 명확화 (scope 4 차원 모두 포함 + 수단 read-only + Boss 추상화 design 코드 0)

---

## 0. 본 brief 의 *하지 않는 것* (16 항목, R-15 self-consistency 영구)

1. ❌ **R4 / F2 / Provider Liquidity / (j) 4 차원 본문 *직접* 정정** (R-9 답습 영구 — 본 cycle = read-only 통합 *분석* + Boss 추상화 design doc only, 본문 정정 = 별도 cycle 의무)
2. ❌ **헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경** (R-9 답습 영구)
3. ❌ **Boss 추상화 *신규* 코드 작성 0건 + 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`, 2026-05-22) 변경 0건 + 신규 `src/jarvis/boss/` 디렉토리 0건 + 신규 Backend class 코드 0건** (BLOCKING-1 + R-S1 흡수, 본 cycle = design doc *추출* + Backend 후보 매트릭스 *신규* only, 실제 구현 = (l) MVP-1 트랙 B 별도 cycle)
4. ❌ **테스트 작성/실행** (TDD RED-GREEN-REFACTOR = (l) 별도 cycle)
5. ❌ **(k) M3·M4 결정 *고정*** (변수 분리 input 강화 후 별도 cycle)
6. ❌ **(j) advisory wall-clock *측정*** (본 cycle = (j) 진입 자격 *평가* only, 측정 = (j) 별도 cycle)
7. ❌ **측정 / Modelfile / ollama / 외부 source 코드 변경** (read-only)
8. ❌ **Ollama daemon 변경** (pid 3375 보존, 답습 영구)
9. ❌ **GGUF + Ollama library/Modelfile blob 변경** (R-13 답습 영구)
10. ❌ **llama.cpp HEAD `c0c7e147` 변경**
11. ❌ **vLLM 부분 정정** (line 126 verbatim 보존 영구, 별도 vLLM verify cycle LOW carry-over)
12. ❌ **cascade 검토** ((R4-body) 완료 후 cascade 검토 cycle LOW carry-over 답습)
13. ❌ **메모리 자동 갱신** (사용자 명시 의무)
14. ❌ **brief commit / 분석 결과 commit / SESSION commit / push 자동 진입** (단계 단위 사용자 명시 의무)
15. ❌ **(g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + (4-way-X) prime/super-prime 자동 진입** (chain 영구 종결 의무 답습 영구)
16. ❌ **password literal 직접 사용** (R-S2 발효 영구, summary/raw report 모두 redact 의무)

---

## 1. 본 cycle scope 4 차원 (R4 + F2 + Provider Liquidity + (j))

### 1.1 4 차원 매트릭스 (사용자 명시 "4 차원 모두 포함", BLOCKING-13 + R-S1 흡수)

| 차원 | scope | input source | output 자격 |
|---|---|---|---|
| **R4** | MVP-1 R4 framing 정정 *후속* 재검증 | (R4-evidence) raw + (R4-body) Edit 4건 결과 | R4 정정 후 일관성 평가 + 후속 보강 자격 평가 |
| **F2** | classical MoE > SSM hybrid 가설 강화 평가 | (g) Qwen3-Next-80B SSM 32.3 vs (h) Qwen3-30B-A3B classical 49.6 = ~1.54× | 가설 강화 정도 + 변수 미해소 정직성 + (g)/(h) carry-over 종합 |
| **Provider Liquidity** | **BossLLM Protocol (기존 `src/jarvis/boss.py:54` 구현, commit `83aebad`) design doc 추출 + Backend 후보 매트릭스 (OllamaBoss/LlamaCppBoss/vLLMBoss) 신규** (헌법 5조-2 비협상) | [[project_jarvis_local_boss_direction]] + [[feedback_provider_liquidity]] + 본 brief §1 (h)/(h-O)/(h-OM) 답습 + boss.py 99줄 verbatim | design doc 분리 + Backend 후보 매트릭스 + Boss 신뢰 경계 명문 (R-S2 발효) — 신규 코드 0건 |
| **(j)** | advisory wall-clock 측정 cycle 진입 자격 평가 | (R4-body) M3 매트릭스 정정안 + decode generation ~3.24~3.38× + prefill generation ~3.65~3.77× + Phase 1 ~4.07× | (j) 진입 자격 충족도 + 선결 cycle 4 carry-over 종합 (Phase 1 N=3 + (h)' bartowski direct N=3 + Ollama embedded llama.cpp version + Ollama prefill framework overhead) + threshold 후보 매트릭스 + (j)→(k)→(l) chain 명시 |

### 1.2 4 차원 *교차 의존성* 명문 (R-9 답습 영구 정직성)

- R4 ↔ F2: R4 정정 결과 ((R4-body) M3 정정 framing) 는 F2 가설 강화 *근거* (decode generation ~3.24~3.38× = Ollama framework overhead 본질, source conversion 무관, S1 confirmed)
- R4 ↔ Provider Liquidity: R4 정정 후 framing = "llama.cpp > Ollama 확정" → Boss 추상화 시 LlamaCppBoss 우선 후보 + OllamaBoss = MVP-1 비채택 자격 약화 (단, *고정* (k) 별도 cycle 의존)
- R4 ↔ (j): R4 decode generation 격차 (~3.24~3.38×) + prefill generation 격차 (~3.65~3.77×) = (j) advisory wall-clock budget 평가 *결정적* input (BLOCKING-9: wall-clock = decode + prefill 합산 의무)
- F2 ↔ Provider Liquidity: SSM hybrid vs classical MoE 가설 = 모델 교체 자격 평가 input (헌법 5조-2 함의)
- F2 ↔ (j): F2 가설 미해소 변수 (model size + expert routing + 도구 version) = (j) 측정 cycle 의존성 의무
- Provider Liquidity ↔ (j): Boss 추상화 interface = (j) advisory wall-clock 측정 시 OllamaBoss/LlamaCppBoss 모두 측정 자격 충족 의무

→ **본 cycle = 4 차원 교차 의존성 종합 *분석* + Boss 추상화 design doc 추출 + Backend 후보 매트릭스**

---

## 2. 분석 대상 verbatim (read-only, R-S 답습)

### 2.1 R4 차원 분석 대상

**(R4-body) 본문 정정 4 위치 결과 (commit `34c096c`)**:
- MVP-1 brief line 141 (M3 매트릭스): "llama.cpp > Ollama" + 4 차원 격차 명문
- MVP-1 brief line 124~125 (🔴 R4 section): "llama.cpp > Ollama 확정" + Qwen3-30B-A3B 49.6 vs Ollama 14.69~15.29
- MVP-1 brief line 126 (vLLM section): verbatim 100% 보존 (R-S1 발효)
- MVP-1 brief line 20 (R4 표): 4 차원 격차 분리
- MVP-1 합의 보고서 line 63 (R4 행): ~4% 정합 + (k) 별도

**(R4-evidence) raw report 답습 input**:
- `docs/phase0/v1-poc-raw/r4-evidence/2026-05-26T08-30-r4-evidence-summary.json`
- R4 framing 부적정성 evidence 3 차원 (a/b/c) + model variant 별 framing

### 2.2 F2 차원 분석 대상

**(g) 14번째 entry raw**:
- Qwen3-Next-80B SSM hybrid Q4_K_M decode generation **32.3 t/s** (DGX Spark, llama.cpp `c0c7e147`)
- SSM tensor 존재 (`ssm_dt` flag=0 required)

**(h) 15번째 entry raw**:
- Qwen3-30B-A3B classical MoE Q4_K_M decode generation **49.6 t/s** (DGX Spark, llama.cpp `c0c7e147`, bartowski direct)
- SSM tensor 0건 (classical MoE confirmed)

**(g) vs (h) 매트릭스** (15번째 entry §F-3 답습):
- decode prompt 177.9 → 389.4 (~2.19×)
- decode generation 32.3 → 49.6 (~1.54×)
- prefill prompt 971.9 → 1916.8 (~1.97×)
- prefill generation 31.5 → 45.4 (~1.44×)
- → classical MoE > SSM hybrid 모든 측정 차원 빠름 (S2 강화 시나리오 일부 답습)

**미해소 변수** (N-7 답습 영구 정직성):
- model size (80B vs 30B)
- expert routing (Qwen3-Next 별도 sparse routing vs Qwen3-30B 표준)
- 도구 version (Qwen3-Next branch vs `c0c7e147` master)

### 2.3 Provider Liquidity 차원 분석 대상 (R-S1 발효 boss.py verbatim 답습)

**기존 `src/jarvis/boss.py` 99줄 verbatim** (commit `83aebad`, 2026-05-22, "feat(jarvis): MVP-1 트랙 A — Boss LLM advisory 판단 지점 (TDD)"):
- 본 brief §9.3 에서 핵심 4 부분 verbatim 인용 (AdviceRequest + BossAdvice + BossLLM Protocol + merge_flags)
- 본 cycle = 기존 구현 변경 0건 + 신규 Backend class 코드 0건 (BLOCKING-1 + BLOCKING-12 답습)

**[[project_jarvis_local_boss_direction]] memory verbatim**:
- provider-agnostic 개인 자비스: 로컬 LLM=사장, CLI=tmux 워커, HW=GB10/121GB
- Boss = 로컬 LLM (Qwen3.x-A3B MoE / 30B이하 양자화)
- 워커 = 외부 LLM CLI (Claude Code / Gemini CLI / 등 tmux 격리)

**[[feedback_provider_liquidity]] memory verbatim**:
- Provider Liquidity 하드 요구 — 모델/구독/오케스트레이터 교체가 코드 변경 없이 가능해야 함. 헌법 제5조-2 비협상

**헌법 5조-2 직접 reference** (read-only, 본문 변경 0건 의무):
- 락인 0
- 최소 2 provider always-on
- 모델 교체 = config 변경만, 코드 변경 0건

**(h)/(h-O)/(h-OM) 답습 input** (4-way 측정 evidence):
- llama.cpp 49.6 t/s (bartowski direct, N=1 정직성 — LlamaCppBoss N=3 carry-over MEDIUM)
- Ollama 14.69~15.29 t/s (qwen3:30b-a3b-instruct-2507-q4_K_M)
- vLLM = MVP-1 비채택, MVP-2 재검토 (line 126 verbatim 보존)

### 2.4 (j) 차원 분석 대상

**advisory wall-clock budget input**:
- R5 권고 ~15 t/s threshold (MoE 2~8배 여유, brief v2) — 단일 후보 framing 정정 (BLOCKING-10)
- 결정적 flag 분리 + Boss advisory (R1~R3 답습)
- prefill 입력 상한 / 요약 (R5 권고)

**선결 cycle carry-over 4 의무** (BLOCKING-15 + R-S4 발효):
- Phase 1 N=3 repetitions Ollama 답습 MEDIUM (Ollama 분산 검증)
- **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle MEDIUM (REC-3 신규)**
- Ollama embedded llama.cpp version verify MEDIUM
- Ollama prefill processing framework overhead 검증 MEDIUM (F-4 (h-OM) 답습)

---

## 3. 분석 절차 (R-rec-16 + R-S4 + R-11 발효)

### 3.1 분석 도구 + 적용 의무

- **Read tool 의무** (read-only, 본문 변경 0건)
- **Edit tool 적용 0건 의무** (본 cycle scope 외, 별도 cycle)
- **Write tool 적용** = (4) 분석 결과 + Boss 추상화 design doc only (`docs/architecture/jarvis-mvp1-boss-abstraction-design.md` 신규)
- **grep / find / git 의무** (cross-check)

### 3.2 분석 순서

| 단계 | 내용 | 형식 |
|---|---|---|
| (1) brief v1 작성 + commit | `af7ac8b`, 371줄 | 완료 |
| (2) 풀 3+1 합의 + commit | `5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4 | 완료 |
| (3) brief v1.1 보강 + commit (본 단계) | BLOCKING 15 verbatim 100% + R-S1~R-S4 흡수 + 권고 5 일부 + §11 신규 | **진행 중** |
| (4) 분석 결과 + Boss 추상화 design doc commit | 4 차원 종합 분석 + Boss 추상화 design doc (`docs/architecture/jarvis-mvp1-boss-abstraction-design.md`, 기존 boss.py design doc 추출 + Backend 후보 매트릭스 신규) | 사용자 명시 후 |
| (5) SESSION 20번째 + INDEX + commit | R-1 anchor 26회 sudo 1회 R-S4 발효 자격 별도 분리 + chain (1)~(4) 답습 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

### 3.3 분석 후 cross-check 의무 (R-S2 + R-S5 답습 cascade scope 확장 + BLOCKING-12)

- 분석 본문 evidence raw 답습 정합성 verify (4-way + Phase 1 5-way 핵심 숫자 grep)
- Boss 추상화 design = 코드 0건 verify
- **`git diff src/jarvis/boss.py src/jarvis/orchestrator.py src/jarvis/approval.py tests/jarvis/test_boss_advisory.py` = 0** (BLOCKING-12 흡수, 기존 boss.py + 통합 + 테스트 변경 0건)
- **`src/jarvis/boss/` 디렉토리 0건 verify** (`ls -d src/jarvis/boss/ 2>&1 | grep "그런 파일이나 디렉터리가 없습니다" 적중`)
- **헌법/ADR cascade 0건 verify**: `git diff docs/constitution/ docs/decisions/ docs/architecture/ docs/guides/ CLAUDE.md` = 0 (단 본 cycle commit 자체 = brief + 합의 + 분석 결과 + Boss 추상화 design doc 신규 제외)
- **cascade verify scope 확장 (R-S5 답습)**: `git diff /home/delangi/.claude/projects/.../memory/ docs/phase0/ docs/review/ docs/sessions/ docs/INDEX.md` = 0 (단 본 cycle commit 자체 제외)
- **R4 referent 보존 verify** ((R4-body) 답습): MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85 = **4 위치** (BLOCKING-14 + R-S3, "5 위치" 산술 자기모순 정정) + (R4-body) Edit 결과 4 위치 모두 보존
- **vLLM 부분 보존 verify**: line 126 vLLM section verbatim 유지 (R-S1 답습)
- **비밀번호 누출 verify (R-S2 발효 영구)**: 본 brief + 분석 결과 + Boss 추상화 design 모두 grep `<REDACTED-PWD-PATTERN>` = 0건

---

## 4. 분석 후 영향 평가 (헌법/ADR cascade 0건 + Provider Liquidity 본질 답습)

### 4.1 헌법 5조-2 (Provider Liquidity, 비협상) 답습 정합

- 헌법 5조-2 본문 변경 0건 의무 답습 영구
- Provider Liquidity 원칙 = 모델/구독/오케스트레이터 교체 코드 변경 0 + 락인 0 + 최소 2 provider always-on
- 본 cycle Boss 추상화 design = Provider Liquidity 원칙 *직접 실현* 의무 (BossLLM Protocol + 다중 backend 교체 자격)
- 본 cycle = Provider 선택 의사결정 input only, 원칙 *변경* 0건

### 4.2 ADR-011 §2.1 5조건 답습 정합

- ADR-011 §2.1 5조건 (a)~(e) 답습 권위
- 본 cycle = R4 정정 후 일관성 평가 + (k) M3·M4 결정 *고정* 자격 평가 = (k) 별도 cycle 진입 자격 input only
- (a) "동등 이상의 보안 결과" 조건 = 본 cycle scope 내 ((R4-evidence) R-8 발효 답습)
- (b)~(e) cascade 검토 자격 = 본 cycle scope 내
- **ADR-011 본문 변경 0건 의무 답습 영구**

### 4.3 다른 ADR 답습 정합

- ADR-001~ADR-010 + ADR-012 본문 변경 0건 의무 답습 영구

### 4.4 다른 문서 답습 정합 (R-S5 답습 cascade scope 확장)

- CLAUDE.md / docs/architecture/ (단 신규 `jarvis-mvp1-boss-abstraction-design.md` 제외) / docs/guides/ / 메모리 본문 변경 0건 의무 답습 영구
- 다른 phase0/ brief / review/ 합의 보고서 본문 변경 0건 의무 답습 영구
- docs/sessions/ + INDEX.md 본문 변경 0건 의무 답습 영구 (단 본 cycle SESSION 20번째 entry 추가 + INDEX 추가는 별도)

---

## 5. 분석 본문 사전 명문 (§9 답습 의무, 본 v1.1 = 합의 BLOCKING + R-S* 흡수 후 *확정안*)

본 brief v1.1 §9 = 합의 BLOCKING 15 + R-S1~R-S4 흡수 후 *확정안*. 단계 (4) 분석 결과 + Boss 추상화 design doc commit 시 §9 확정안 답습.

---

## 6. 정직성 한계 (R-6 답습, 16 항목)

1. 본 cycle = 4 차원 통합 *분석* cycle (R-9 답습 영구 본문 정정 자격 0건, 별도 cycle 의무) — sensitivity 매우 높음 (4 차원 묶음)
2. scope 한정 = R4 framing 정정 *후속* 재검증 + F2 가설 강화 평가 + Provider Liquidity Boss 추상화 design doc 추출 + (j) 진입 자격 평가
3. 헌법/ADR cascade 0건 의무 답습 영구
4. Provider Liquidity 본질 답습 영구 (Boss 추상화 design = config 변경만 / 락인 0 / 최소 2 provider always-on 직접 실현 의무)
5. 4-way + Phase 1 5-way evidence 답습 정직성
6. F2 가설 미해소 변수 (model size + expert routing + 도구 version) = 본 cycle 내 해소 0건, 별도 측정 cycle 의무
7. 결정 *고정* 자격 무관 ((k) 별도 cycle)
8. 6단계 변형 entry form (R-rec-16 답습)
9. 본 cycle = (R4-body) 직접 후속 *상위* scope ((g)/(h)/(h-O)/(h-OM)/(R4-evidence)/(R4-body) chain 영구 종결)
10. (4-way-X) prime/super-prime 자동 진입 명백 부정 답습 영구
11. 본 cycle 결과 메모리 등재 자격 = 사용자 명시 의무
12. 본 cycle 본문 정정 0건 (별도 cycle 의무)
13. **Boss 추상화 design = 기존 `src/jarvis/boss.py` 99줄 (commit `83aebad`) design doc 추출 + Backend 후보 매트릭스 신규 only** (실제 신규 코드 0건, 기존 변경 0건, (l) MVP-1 트랙 B 별도 cycle, BLOCKING-1 + R-S1 흡수)
14. (j) advisory wall-clock = 진입 자격 *평가* only (측정 = (j) 별도 cycle)
15. R-S2 발효 — password literal redact 답습 영구 (본 brief + 분석 결과 + Boss 추상화 design 모두)
16. **본 cycle 4 차원 교차 의존성 명문 (§1.2) = 정직성 핵심** — 단일 차원 단독 결론 추출 금지, 4 차원 종합 *분석* 의무

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 *하지 않는 것* 16 항목과 §7 차단 조건은 **1:1 매핑 의무**.

1. ❌ R4 / F2 / Provider Liquidity / (j) 4 차원 본문 *직접* 정정
2. ❌ 헌법 / ADR-011 / 다른 ADR / 다른 문서 본문 정정 (R-9 답습 영구)
3. ❌ **Boss 추상화 *신규* 코드 작성 + 기존 `src/jarvis/boss.py` 99줄 변경 + 신규 `src/jarvis/boss/` 디렉토리 + 신규 Backend class 코드** (BLOCKING-1 + R-S1 답습 영구)
4. ❌ 테스트 작성/실행
5. ❌ (k) M3·M4 결정 *고정*
6. ❌ (j) advisory wall-clock *측정*
7. ❌ 측정 / Modelfile / ollama / 외부 source 코드 변경
8. ❌ Ollama daemon 변경 (pid 3375 보존)
9. ❌ GGUF + Ollama library/Modelfile blob 변경 (R-13)
10. ❌ llama.cpp HEAD `c0c7e147` 변경
11. ❌ vLLM 부분 정정 (line 126 verbatim 보존 영구, 별도 LOW carry-over)
12. ❌ cascade 검토
13. ❌ 메모리 자동 갱신
14. ❌ brief commit / 분석 결과 commit / SESSION commit / push 자동 진입
15. ❌ (g1-N-3-adr-008+sip+adr-012'') + (h-X) + (h-O-X) + (h-OM-X) + (R4-evidence-X) + (R4-body-X) + **(4-way-X)** prime/super-prime 자동 진입 (chain 영구 종결)
16. ❌ password literal 직접 사용

---

## 8. 본 cycle 진입 자격 평가 (R-rec-12 답습)

### 8.1 carry-over 자격 매트릭스

| carry-over | 출처 | scope | 본 cycle 적합도 |
|---|---|---|---|
| (4-way) 통합 *분석* cycle HIGH | (R4-body) §8 + (R4-evidence) §8 | 4 차원 상위 scope | ⭐⭐⭐ 본 cycle 자체 |
| (R4-body) 완료 후 cascade 검토 cycle LOW | (R4-body) §8 R-10 발효 #19 | 정정 후 cascade verify + R4 referent "5 위치" 산술 자기모순 정정 (R-S3 발효 본 cycle 답습 cascade) | ❌ 본 cycle scope 외 (별도 LOW cycle) |
| vLLM verify cycle LOW | (R4-body) §8 R-9 답습 | vLLM 부분 external reference | ❌ 본 cycle scope 외 (별도 LOW cycle) |
| (h-OL) llama.cpp Ollama library blob 측정 MEDIUM | (h-O)/(h-OM) R-15 답습 | 5-way 측정 | ❌ 본 cycle scope 외 (별도 측정 cycle, 본 cycle = read-only) |
| **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 MEDIUM (REC-3 신규)** | 본 합의 REC-3 | (h) bartowski direct N=1 분산 미확인 → N=3 carry-over | ❌ 본 cycle scope 외 (별도 측정 cycle) |
| (j) advisory wall-clock 측정 MEDIUM | (R4-body) §8 | (j) 측정 cycle | 🟡 본 cycle = (j) 진입 자격 *평가* only |
| (k) M3·M4 결정 *고정* DEFER | 답습 영구 | (k) 별도 cycle | ❌ 변수 분리 input 강화 후 (본 cycle = input 강화 자격) |
| (l) MVP-1 트랙 B 구현 DEFER | 답습 영구 | (k) 통과 후 | ❌ 본 cycle = design doc 추출 + Backend 매트릭스 신규 only |
| **(m) F2 model size 단독 분리 cycle MEDIUM (REC-1 신규)** | 본 합의 REC-1 | F2 미해소 변수 model size 단독 분리 측정 | ❌ 본 cycle scope 외 (carry-over 명명 후보) |

### 8.2 본 cycle 자격 충족 verify

- ✅ (R4-body) §8 HIGH carry-over 직접 후속 자격
- ✅ 사용자 명시 "(4-way) 통합 *분석* cycle HIGH (상위 scope)" 답습
- ✅ 사용자 명시 scope 4 차원 모두 포함
- ✅ 사용자 명시 수단 read-only + Boss 추상화 design (코드 0) — **단계 (4) design doc = 기존 boss.py design doc *추출* + Backend 후보 매트릭스 *신규* only** (BLOCKING-1 + R-S1 흡수, "design draft" 단어 정정)
- ✅ chain 영구 종결 의무 답습 영구 ((4-way) 단독 명명, X prime/super-prime 금지)
- ✅ R-9 답습 영구 (본문 정정 0건 의무)
- ✅ 6단계 변형 entry form (R-rec-16 답습)

### 8.3 본 brief 자체 후속 단계 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit | `af7ac8b`, 371줄 | 명시 완료 |
| (2) 풀 3+1 합의 진행 + commit | `5dcbbdb`, 267줄, APPROVE w/ COND BLOCKING 15 + R-S1~R-S4 | 명시 완료 |
| **(3) brief v1.1 보강 + commit (본 단계)** | BLOCKING 15 verbatim 100% + R-S1~R-S4 흡수 + 권고 5 일부 + §11 신규 | **진행 중** |
| (4) 분석 결과 + Boss 추상화 design doc commit | §9 확정안 답습 + Boss 추상화 design doc 신규 (기존 boss.py design doc 추출 + Backend 후보 매트릭스 신규, 코드 0) | 합의 + 사용자 명시 후 |
| (5) SESSION 20번째 + INDEX + commit (R-1 anchor 26회 sudo 1회 R-S4 발효) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. 분석 본문 확정안 4 차원 매트릭스 (BLOCKING 15 + R-S1~R-S4 흡수)

### 9.1 R4 차원 분석 확정안 (BLOCKING-14 + R-S3 흡수)

**R4 정정 후 일관성 평가**:
- (R4-body) Edit 4건 = MVP-1 brief 3 위치 + MVP-1 합의 보고서 1 위치, line 126 vLLM verbatim 보존
- **R4 referent 보존 = 4 위치 (산술 정합)**: MVP-1 brief line 161 (1) + MVP-1 합의 보고서 line 52/79/85 (3) = 합계 **4 위치** (BLOCKING-14 + R-S3 발효 — (R4-body) brief 자체 "5 위치" 산술 자기모순 *(R4-body) cascade 검토 cycle (LOW) 별도 정정 자격*, 본 cycle 정정 0건 R-9 답습 영구)
- 정정 후 framing = "llama.cpp > Ollama 확정" + 4 차원 격차 명문 + (k) 별도 + Provider Liquidity 약화 0건

**후속 보강 자격**:
- 본 cycle 분석 = R4 정정 *후속* 일관성 확정 ✓
- 추가 cascade 검토 = LOW carry-over (별도 cycle, R-10 발효 정직성 #19)
- R4 후속 보강 다른 dimension 후보 (REC-13): t/s threshold 동적 조정 / batch size scaling / context length scaling — *후보* only, 본 cycle 결정 0건

### 9.2 F2 차원 분석 확정안 (REC-1 + REC-6 흡수)

**F2 가설 강화 정도**:
- (g) Qwen3-Next-80B SSM hybrid 32.3 vs (h) Qwen3-30B-A3B classical 49.6 = ~1.54× (decode generation, **단일 측정 N=1 정직성**)
- classical MoE > SSM hybrid 모든 차원 빠름 (S2 강화 시나리오 일부 답습)

**미해소 변수 정직성 (N-7 답습 영구)**:
- model size (80B vs 30B) — 단독 변수 분리 cycle = **(m) F2 model size 단독 분리 cycle MEDIUM (REC-1 신규)**
- expert routing (Qwen3-Next sparse vs Qwen3-30B 표준) — 별도 cycle
- 도구 version (Qwen3-Next branch vs `c0c7e147` master) — 별도 cycle
- → F2 가설 *간접* input only (N-7 답습 영구)

**변수 분리 측정 cycle 우선순위 후보 (REC-6 합산)**:
1. **model size 우선** (가장 영향 큼 + 외부 evidence 강함 "with only ~3B active params 3-5x faster") ⭐⭐⭐ — **(m) 명명 carry-over**
2. **도구 version 우선** (가장 통제 가능, mainline merge 후 재측정) ⭐⭐
3. **expert routing 우선** (가장 미지수, 마지막 분리) ⭐

**(g)/(h) carry-over 종합**:
- F2 가설 = (k) M3·M4 결정 *고정* 자격 *간접* input
- (l) MVP-1 트랙 B 구현 시 model size 30B 우선 후보 (50% 빠름 + classical MoE evidence)

### 9.3 Provider Liquidity 차원 분석 확정안 (BLOCKING-1~8 + R-S1 + R-S2 + REC-5 흡수, design doc 추출 framing)

⭐⭐⭐ **본 §9.3 framing 전면 정정 (R-S1 + BLOCKING-1 흡수)**:
- "BossLLM ABC draft" → **"BossLLM Protocol (기존 `src/jarvis/boss.py:54` 구현, commit `83aebad`) design doc 추출 + Backend 후보 매트릭스 신규"**
- "ABC" 단어 모두 삭제 → "Protocol (@runtime_checkable)" 로 교체
- code block = `src/jarvis/boss.py` verbatim 인용 (핵심 4 부분, BLOCKING-2 + BLOCKING-3 흡수)
- "design draft, 코드 0" → "**기존 boss.py 99줄 design doc 추출 + Backend 후보 매트릭스 신규 (신규 코드 0건, 기존 변경 0건)**"

#### 9.3.1 BossLLM Protocol verbatim (boss.py:24~98 verbatim 인용, BLOCKING-2 + R-S1 흡수)

```python
# src/jarvis/boss.py:24~35 verbatim
@dataclass(frozen=True)
class AdviceRequest:
    """Boss 가 검토할 입력 — 모두 untrusted(워커 출력 포함, prompt injection 표적).
    Boss 는 이 입력으로 *텍스트만* 생성한다. 실행·게이트 통과·workdir·argv 에
    대한 어떤 제어 정보도 여기서 도출되지 않는다(§5 신뢰 경계).
    """
    prompt: str
    worker_alias: str
    output: str
    deterministic_flags: list[str] = field(default_factory=list)

# src/jarvis/boss.py:38~50 verbatim
@dataclass(frozen=True)
class BossAdvice:
    """Boss advisory 결과 — *텍스트 전용*(R2). 제어 흐름 필드 금지.
    - summary: 사람에게 보여줄 자연어 검토 요약(표시용 — 게이트 결정에 자동 반영 0).
    - extra_flags: 결정적 flag 에 *추가*할 위험 태그(union, 감산 불가 = R1 fail-safe).
    - advisory_failed: advisory 가 실패(누락)했는지 표지(R3 명시 경고용 *상태* — 게이트
      통과를 좌우하지 않는 표시 메타데이터). confidence 없음(R6).
    """
    summary: str
    extra_flags: list[str] = field(default_factory=list)
    advisory_failed: bool = False

# src/jarvis/boss.py:53~64 verbatim
@runtime_checkable
class BossLLM(Protocol):
    """로컬 사장 추상 — provider 교체 단위(헌법 5조). 순수 추론(부작용 0).
    name = 교체 키. advise() = MVP-1 유일 판단 지점(결과 검토). 실패 시 예외를
    던질 수 있다(R3: 호출측이 누락→경고로 처리).
    """
    name: str
    def advise(self, req: AdviceRequest) -> BossAdvice: ...

# src/jarvis/boss.py:92~98 verbatim
def merge_flags(deterministic: list[str], extra: list[str]) -> list[str]:
    """결정적 flag ∪ advisory flag — *추가만*, 감산 불가(R1 fail-safe 불변식).
    결정적 flag 는 전부 보존되고, extra 중 새것만 뒤에 덧붙는다(중복 없음).
    advisory 가 결정적 flag 를 줄이는 경로는 구조적으로 존재하지 않는다.
    """
    return [*deterministic, *(f for f in extra if f not in deterministic)]
```

**핵심 verify (BLOCKING-3 흡수)**:
- BossAdvice 필드 = `summary: str / extra_flags: list[str] / advisory_failed: bool = False` (3 필드 only)
- **confidence 필드 0건** (R6 답습 영구 — LLM 자기보고 = 거짓 안전감)
- **콜백·경로·명령 필드 금지** (R2 답습 — 텍스트 전용 frozen)
- AdviceRequest = `prompt / worker_alias / output / deterministic_flags` (4 필드, 모두 untrusted)
- `@runtime_checkable Protocol` (ABC 아님 — duck typing, provider 교체 외부 class 정의 자유)
- merge_flags = `[*deterministic, *(f for f in extra if f not in deterministic)]` (R1 fail-safe 불변식 — 감산 구조적 불가)

#### 9.3.2 Boss 신뢰 경계 절 신규 (R-S2 발효 + BLOCKING-5 흡수)

⭐⭐⭐ **R-S2 CRITICAL — Boss 입력 = untrusted (prompt injection 표적)**:

**Boss 입력 신뢰 경계 (R10 + R8 답습)**:
- AdviceRequest 모든 필드 = untrusted (워커 출력 포함, prompt injection 표적, boss.py:26~30 docstring verbatim)
- AdviceRequest.output = 워커 stdout, prompt injection 직접 표면 (워커 자체 침해 시 Boss advisory 침해 자격 = injection 표면 확장)

**Boss 출력 신뢰 경계 (R2 답습)**:
- BossAdvice = 텍스트 전용 (콜백·경로·명령 필드 금지)
- 실행·게이트 통과·workdir·argv 도출 0건 (boss.py:28~29 docstring verbatim)
- BossAdvice.summary = 표시용 only, 게이트 결정에 자동 반영 0건 (boss.py:42 verbatim)

**Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5 답습)**:
- 결정적 flag + raw diff + ReviewGuard 권위만 게이트 좌우
- BossAdvice.summary 종속 금지 (R10 답습 — 사람 게이트 = 결정적 flag + raw diff 직접 확인 의무)
- 의미적 green washing (summary 오도) 방어 = 3중 방어 (결정적 flag 분리 표시 + raw diff 직접 확인 + ReviewGuard 권위, R1 답습)
- 기계적 flag 감산만 차단 (merge_flags fail-safe 불변식), 의미적 우회는 못 막음 (boss.py:9~11 docstring verbatim)

**워커 실패 시 advise 미호출 (R8 답습, BLOCKING-6 흡수)**:
- `result.is_error` 면 BossLLM.advise 호출 0건 (실패 출력 = 침해된 워커 advisory injection 표면, 회피 의무)
- StubBoss.calls 답습 verify (boss.py:71/83 — 호출 여부 관찰)

**advisory failure ≠ health_check failure 분리** (B-rec-3 답습, BLOCKING-8 흡수):
- advise 실패 = **fail-open** (R3, 비차단 + 경고 — boss.py:12~13 verbatim "advisory 실패는 게이트 진행(비차단) + 명시 경고")
- merge_flags = **fail-safe** (R1, 감산 구조적 불가, 결정적 flag 합집합 강제)
- health_check 실패 = (k) 별도 cycle 결정 후보 (현재 boss.py 미존재)
- ⚠️ "**fail-closed 정신**" 표현 부정확 (BLOCKING-8) — R3 = fail-open + R1 = fail-safe 분리 명문, "fail-closed" 단어 삭제

#### 9.3.3 Backend 후보 매트릭스 (4-way 측정 evidence + OpenAI-compatible endpoint 통일, BLOCKING-7 + BLOCKING-11 흡수)

| backend | 측정 t/s (decode gen) | **OpenAI-compatible endpoint** | 우선순위 | MVP-2 재검토 trigger | 비고 |
|---|---|---|---|---|---|
| **LlamaCppBoss** | 49.6 (Qwen3-30B-A3B classical, bartowski direct, **N=1 정직성**) | `http://localhost:8080/v1/chat/completions` (llama-server) ✓ | ⭐⭐⭐ MVP-1 우선 | N/A (MVP-1 채택) | 빠름 / N=3 분산 검증 carry-over MEDIUM ((h)' REC-3 신규) |
| **OllamaBoss** | 14.69~15.29 (qwen3:30b-a3b-instruct-2507-q4_K_M) | `http://localhost:11434/v1/chat/completions` (Ollama OpenAI mode) ✓ | ⭐⭐ MVP-1 보조 | N/A (MVP-1 채택) | Provider Liquidity 보조 + Modelfile 호환 + Phase 1 N=3 carry-over MEDIUM |
| **vLLMBoss** | (MVP-1 비채택) | `/v1/chat/completions` (vLLM OpenAI mode) ✓ | MVP-2 재검토 | **vLLM 공식 sm_121 native support release + DGX Spark binary wheel 제공 + sm_121f SCALED_MM_ARCHS 포함 시** (BLOCKING-11 외부 evidence: vllm Issue #36821/#31128 "No sm_121 (Blackwell) support on aarch64", 0.17 일부 fix BUT SCALED_MM_ARCHS 미포함) | **영구 배제 금지 (line 126 답습 영구, C-2 충돌 회피)** |

**OpenAI-compatible 통일 자격 (BLOCKING-7 흡수, 외부 evidence 답습)**:
- 3 backend 모두 OpenAI-compatible `/v1/chat/completions` 지원 confirmed (llama-server 2026 / Ollama 공식 docs / vLLM OpenAI mode)
- → **BossLLM Protocol 내부 = HTTPClient + base_url 만 차이, Provider Liquidity 직접 입증** ⭐⭐⭐
- **httpx 표준 클라이언트** (외부 LLM SDK 0건, boss.py:15 verbatim "트랙 B 에서 httpx/OpenAI-호환")
- 추상화 layer 매우 얇음 자격 + 헌법 5조-2 비협상 직접 실현

**보안 의무 (M6 + R11 답습 영구, BLOCKING-4 흡수)**:
- OllamaBoss / LlamaCppBoss endpoint = **127.0.0.1 localhost 한정** (외부 노출 금지)
- 추론 시점 egress 0 (단 설치/모델 pull/텔레메트리 별개)
- (j) 측정 cycle 에서 실측 확인 의무

#### 9.3.4 LiteLLM 4 후보 대안 architecture 매트릭스 (REC-5 footnote 흡수, MVP-1 결정 *후보* only)

본 cycle 결정 0건 = **(k) M3·M4 결정 *고정* cycle carry-over input only**. 본 §9.3.4 = 외부 evidence 답습 footnote 자격.

| # | 후보 architecture | 의존성 | Provider Liquidity | DGX Spark 적합도 | MVP-1 결정 자격 |
|---|---|---|---|---|---|
| A | **BossLLM Protocol 직접** (현재 boss.py:54) | 0건 | 코드 의존 (실현) | ⭐⭐ | ⭐⭐⭐ (기존 구현 + 외부 의존 0) |
| B | **LiteLLM 게이트웨이** | LiteLLM | config 의존 (자격 매우 강) | ⭐⭐⭐ | (k) carry-over, **LiteLLM lock-in 우려 정직성** (NOTE-7) |
| C | **Hybrid** (BossLLM 얇은 wrapper + LiteLLM 내부 client) | LiteLLM | 양쪽 자격 | ⭐⭐⭐ | (k) carry-over |
| D | **BossLLM + llama-swap** (NVIDIA DGX Spark GB10 stack 답습, 2026-05) | llama-swap (Go) | config + 자동 model swap | ⭐⭐⭐ (GB10 production stack 표준) | (k) carry-over |

**외부 evidence 답습 footer (NOTE-7 lock-in 우려 정직성)**:
- NVIDIA Developer Forum 2026-05: DGX Spark GB10 production stack = `Client → LiteLLM (OpenAI-compatible gateway) → llama-swap (model swap) → vLLM/llama.cpp/Ollama` (본 project HW 동일)
- 본 cycle = design doc *추출* + Backend 후보 매트릭스 only, (k) 결정 *고정* 자격 0건 (R-9 답습 영구)
- LiteLLM 자체 lock-in 우려 정직성 = NOTE-7 답습 영구

### 9.4 (j) 차원 분석 확정안 (BLOCKING-9 + BLOCKING-10 + BLOCKING-15 + R-S4 + REC-2 + REC-4 흡수)

**(j) advisory wall-clock 진입 자격 충족도**:
- ⚠️ **wall-clock = decode generation + prefill generation 합산 의무 (BLOCKING-9 흡수)**: decode-only 정의 부정확 (Ollama prefill 격차 ~3.65~3.77× 답습, (R4-body) M3 매트릭스 4 차원 격차)
- LlamaCppBoss decode generation 49.6 t/s + prefill ~45.4 t/s (합산 자격) ⭐⭐⭐
- OllamaBoss decode generation 14.69~15.29 t/s + prefill ~12.04~12.43 t/s (합산 자격 약화)

**threshold 후보 매트릭스 (BLOCKING-10 흡수, T1~T6 다중 후보 only, 본 cycle 결정 *고정* 0건)**:

| # | threshold | 보수성 | Ollama 통과 | llama.cpp 통과 | false positive risk | false negative risk |
|---|---|---|---|---|---|---|
| T1 | ~10 t/s | 매우 보수 | ✓ | ✓ (5×) | 高 | 매우 낮음 |
| T2 | ~15 t/s (R5 권고) | 표준 | 경계 (-2% ~ +2% 진동) | ✓ (3.3×) | 中 | 低 |
| T3 | ~20 t/s | 적정 | ✗ | ✓ (2.5×) | 低 | 中 |
| T4 | ~30 t/s | 공격 | ✗ | ✓ (1.65×) | 매우 낮음 | 高 |
| T5 | 동적 (latency budget × context length) | N/A | 조건부 | 조건부 | 低 | 低 |
| T6 | 다중 tier (short ~30 / mid ~20 / long ~15) | 절충 | short context ✗ | ✓ | 低 | 低 |

→ **(j) 별도 cycle 측정 후 결정 *후보* only (본 cycle 내 *고정* 0건)**

**prefill 입력 상한 후보 + 요약 (REC-4 흡수, 외부 evidence 2026 답습)**:

| 입력 상한 | 요약 방법 | 트레이드오프 |
|---|---|---|
| ~512 tokens | TextRank | 빠름 + 의미 손실 가능 |
| ~1024 tokens | LLM summary | 정확 + latency 비용 |
| ~2048 tokens | Sliding window | 균형 + cache 효과 |
| ~4096 tokens | Hybrid (TextRank → LLM 요약) | 최선 BUT 복잡도 (외부 evidence: "Hybrid 접근 production 표준") |

**선결 cycle carry-over 4 의무 (BLOCKING-15 + R-S4 흡수, (j) 진입 *선결* 강화)**:
- Phase 1 N=3 repetitions Ollama 답습 MEDIUM (Ollama 분산 검증 필수)
- **(h)' LlamaCppBoss bartowski direct N=3 별도 측정 cycle MEDIUM (REC-3 신규)** — (h) 단일 측정 49.6 t/s 분산 미확인
- Ollama embedded llama.cpp version verify MEDIUM (변수 분리)
- (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM (5-way confirm)
- Ollama prefill processing framework overhead 검증 MEDIUM (F-4 (h-OM) 답습)

**(j)→(k)→(l) cycle chain 명시 (REC-2 흡수)**:
- (j) advisory wall-clock 측정 → (k) M3·M4 결정 *고정* → (l) MVP-1 트랙 B 구현 (OllamaBoss/LlamaCppBoss 실제 Backend class 코드)

**(j) 진입 자격 결론 강화 (R-S4 발효 BLOCKING-15)**:
- **선결 cycle carry-over MEDIUM 4건 모두 (j) 진입 *전* 충족 의무**
- Phase 1 N=3 repetitions Ollama 답습 = 분산 검증 필수, **단일 측정 = (j) 진입 자격 충족 0건**
- LlamaCppBoss bartowski direct N=3 별도 측정 ((h)') 후 (j) 진입 자격 충족 자격 평가

### 9.5 분석 후 cross-check 의무 (R-S2 + R-S5 답습 cascade scope 확장 + BLOCKING-12)

- 4 차원 evidence raw 답습 정합성 verify (4-way + Phase 1 5-way 핵심 숫자 grep)
- Boss 추상화 design doc = 코드 0건 verify
- **`git diff src/jarvis/boss.py src/jarvis/orchestrator.py src/jarvis/approval.py tests/jarvis/test_boss_advisory.py` = 0** (BLOCKING-12 흡수 — 기존 boss.py + 통합 + 테스트 변경 0건)
- **`src/jarvis/boss/` 디렉토리 0건 verify** (REC-8 합산)
- 헌법/ADR/다른 문서 본문 변경 0건 verify
- **cascade verify scope 확장 (R-S5 답습)**: 메모리 + 다른 phase0/review/sessions/INDEX 본문 변경 0건
- R4 referent 보존 verify = **4 위치 산술 정합** (BLOCKING-14 + R-S3) + line 126 vLLM verbatim 보존 verify
- **비밀번호 누출 verify (R-S2 발효 영구)**: grep `<REDACTED-PWD-PATTERN>` = 0건 (literal password pattern 직접 사용 0건)

---

## 10. 본 brief v1.1 본 cycle 진입 자체 영구 권위

- 본 brief v1.1 = (R4-body) 19번째 entry cycle 완주 후 carry-over HIGH ⭐⭐ 상위 scope (4-way) 통합 *분석* cycle entry 단계 (3) 브리프 보강 (풀 3+1 합의 `5dcbbdb` APPROVE w/ COND BLOCKING 15 + R-S1~R-S4 흡수)
- ⭐⭐⭐ **R-S1 CRITICAL 흡수** — brief §9.3 코드 블록 = `src/jarvis/boss.py:24~98` verbatim 인용 (commit `83aebad`), "ABC" → "Protocol (@runtime_checkable)" 정정 + framing 전면 정정 (8 흡수 항목)
- ⭐⭐⭐ **R-S2 CRITICAL 흡수** — Boss 신뢰 경계 §9.3.2 신규 (Boss 입력 untrusted + Boss = root of trust 아님 + R10 + R1 + R8 + advisory failure ≠ health_check failure 분리, 5 흡수 항목)
- ⭐⭐ R-S3 HIGH 흡수 — R4 referent 4 위치 (산술 정합, "5 위치" → "4 위치") (R4-body cascade)
- ⭐⭐ R-S4 HIGH 흡수 — Phase 1 N=3 + (h)' LlamaCppBoss N=3 (j) 진입 선결 의무 강화
- ⭐⭐⭐ scope 4 차원 모두 포함 (R4 + F2 + Provider Liquidity + (j)) — 본 cycle = *상위* scope 종합 *분석*
- ⭐⭐⭐ 수단 = read-only analysis only + Boss 추상화 design doc *추출* (기존 boss.py 99줄 design doc + Backend 후보 매트릭스 신규, 신규 코드 0건, 기존 변경 0건) — R-9 답습 영구 본문 정정 0건
- ⭐⭐ 4 차원 교차 의존성 명문 (§1.2) — 단일 차원 단독 결론 추출 금지
- ⭐⭐ R-15 self-consistency 영구 — §0 16 항목 ↔ §7 차단 조건 1:1 매핑
- ⭐ R-1 anchor 26회 누계 자격 (chain (g)/(h)/(h-O)/(h-OM)/(R4-evidence)/(R4-body)/(4-way), sudo 1회 의무 R-S4 발효 자격 별도 분리)
- 본 brief 자체 머신 변경 0건 (측정/Modelfile/ollama/sudo/본문 정정 0)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구
- **(4-way-X) prime/super-prime 자동 진입 명백 부정 답습 영구**

---

## 11. v1 → v1.1 변경 일람 ((R4-evidence)/(R4-body) §10/§11 답습)

### 11.1 BLOCKING 15 흡수 매트릭스 (verbatim 100%, R-21 답습 영구)

| # | 위치 | 흡수 결과 |
|---|---|---|
| BLOCKING-1 (⭐⭐⭐ CRITICAL) | §0 #3 / §1.1 Provider Liquidity 행 / §6 #13 / §7 #3 / §8.2 / §8.3 (4) / §9.3 header | "Boss 추상화 *신규* 코드 작성 0건 + 기존 boss.py 99줄 변경 0건 + 신규 디렉토리/Backend class 0건" 명문 (7 위치) |
| BLOCKING-2 (⭐⭐⭐ CRITICAL) | §9.3.1 | boss.py:24~98 verbatim 인용 (AdviceRequest + BossAdvice + BossLLM Protocol + merge_flags), "ABC"/"@abstractmethod" 단어 모두 삭제 |
| BLOCKING-3 (⭐⭐⭐ CRITICAL) | §9.3.1 footer | BossAdvice 필드 3개 명문 (summary/extra_flags/advisory_failed) + confidence 0건 (R6) + 콜백·경로·명령 필드 금지 (R2) + AdviceRequest 4 필드 명문 |
| BLOCKING-4 (⭐⭐⭐ CRITICAL) | §9.3.3 footer | localhost 127.0.0.1 바인딩 의무 명문 (M6 + R11 답습 영구) + 추론 시점 egress 0 + (j) 실측 확인 의무 |
| BLOCKING-5 (⭐⭐⭐ CRITICAL) | §9.3.2 신규 | Boss 신뢰 경계 절 = 입력 untrusted + 출력 텍스트 전용 + Boss = root of trust 아님 + summary 종속 금지 + 3중 방어 |
| BLOCKING-6 (⭐⭐ HIGH) | §9.3.2 | 워커 실패 시 advise 미호출 (R8 답습, StubBoss.calls 답습 verify) |
| BLOCKING-7 (⭐⭐ HIGH) | §9.3.3 OpenAI-compatible 열 + footer | 3 backend `/v1/chat/completions` 통일 채택 + httpx 표준 클라이언트 + "HTTPClient + base_url 만 차이" footer |
| BLOCKING-8 (⭐⭐ HIGH) | §9.3.2 advisory failure handling | "fail-closed 정신" 단어 삭제 → R3 fail-open + R1 fail-safe + health_check 별도 (k) 분리 |
| BLOCKING-9 (⭐⭐ HIGH) | §9.4 wall-clock | "wall-clock = decode generation + prefill generation 합산 의무" 명문 + decode-only 정의 부정확 |
| BLOCKING-10 (⭐⭐ HIGH) | §9.4 threshold 매트릭스 | T1~T6 (~10/~15/~20/~30/동적/다중 tier) 매트릭스 + 본 cycle 결정 *고정* 0건 |
| BLOCKING-11 (⭐⭐ HIGH) | §9.3.3 vLLMBoss MVP-2 재검토 trigger 열 | "vLLM 공식 sm_121 native support + DGX Spark binary wheel + SCALED_MM_ARCHS 포함" trigger + "영구 배제 금지 line 126 답습" 비고 |
| BLOCKING-12 (⭐⭐ HIGH) | §3.3 + §9.5 | `git diff src/jarvis/boss.py orchestrator.py approval.py tests/jarvis/test_boss_advisory.py = 0` verify 의무 + `src/jarvis/boss/` 디렉토리 0건 verify (REC-8 합산) |
| BLOCKING-13 (⭐⭐ HIGH) | §1.1 R4 행 input / Provider Liquidity 행 output | "BossLLM ABC 정의" → "BossLLM Protocol (boss.py 기존 구현) design doc 분리 + Backend 후보 매트릭스 신규" framing 정정 |
| BLOCKING-14 (⭐⭐ HIGH) | §3.3 + §9.1 + §9.5 | "5 위치" → "4 위치" (산술 정합, line 161 + line 52/79/85) + (R4-body) cascade 검토 cycle (LOW) 별도 정정 자격 명문 |
| BLOCKING-15 (⭐⭐ HIGH) | §9.4 (j) 진입 자격 결론 강화 + carry-over 4 | Phase 1 N=3 + (h)' LlamaCppBoss N=3 별도 (REC-3 신규) + Ollama embedded llama.cpp version + Ollama prefill framework overhead = (j) 진입 선결 의무 |

### 11.2 Reviewer 단독 격상 R-S* 4 흡수 매트릭스

| R-S | 위치 | 흡수 결과 |
|---|---|---|
| R-S1 (⭐⭐⭐ CRITICAL) | §9.3.1 + §0 #3 + §1.1 + §6 #13 + §7 #3 + §8.2 + §9.3 header | boss.py:24~98 verbatim 인용 + "ABC" → "Protocol" + "신규 코드 작성 0건 + 기존 boss.py 99줄 변경 0건 + 신규 디렉토리/Backend class 0건" framing 전면 정정 (8 흡수 항목) |
| R-S2 (⭐⭐⭐ CRITICAL) | §9.3.2 신규 | Boss 신뢰 경계 절 5 흡수: Boss 입력 untrusted + Boss 출력 텍스트 전용 + Boss ≠ root of trust + R8 워커 실패 advise 미호출 + advisory failure ≠ health_check 분리 |
| R-S3 (⭐⭐ HIGH) | §9.1 + §3.3 + §9.5 | R4 referent 4 위치 산술 정합 ("5 위치" → "4 위치") + (R4-body) cascade 검토 cycle (LOW) 별도 정정 자격 |
| R-S4 (⭐⭐ HIGH) | §9.4 + §2.4 | Phase 1 N=3 = (j) 진입 *선결* 의무 강화 + (h)' LlamaCppBoss N=3 별도 측정 carry-over MEDIUM (REC-3 신규) |

### 11.3 권고 8 흡수 매트릭스 (5 흡수 + 3 합산)

| REC | 흡수 결과 |
|---|---|
| REC-1 | §9.2 footer = (m) F2 model size 단독 분리 cycle MEDIUM 명명 후보 carry-over |
| REC-2 | §9.4 footer = (j)→(k)→(l) chain 명시 |
| REC-3 | BLOCKING-15 합산 흡수 = (h)' LlamaCppBoss N=3 carry-over MEDIUM |
| REC-4 | §9.4 prefill 입력 상한 후보 매트릭스 + 요약 (TextRank/LLM/sliding window/Hybrid) |
| REC-5 | §9.3.4 footnote 신규 = LiteLLM 4 후보 architecture 매트릭스 (A/B/C/D) + lock-in 우려 정직성 (NOTE-7) + MVP-1 결정 *후보* only |
| REC-6 | REC-1 합산 흡수 (변수 분리 우선순위 매트릭스) |
| REC-7 | BLOCKING-11 합산 흡수 (sm_121 stability trigger) |
| REC-8 | BLOCKING-12 합산 흡수 (`src/jarvis/boss/` 디렉토리 0건 verify) |

### 11.4 NOTE 7 정직성 명문 (footer)

| NOTE | 정직성 명문 자격 |
|---|---|
| NOTE-1 | design draft framing 정정 후 정직성 ((R4-body) 답습 자격) |
| NOTE-2 | (j) → (k) → (l) cycle 분리 의무 정직성 |
| NOTE-3 | R-15 verify ✓ |
| NOTE-4 | OllamaBoss N=3 미수행 carry-over MEDIUM |
| NOTE-5 | password redact 강함 (R-S2 발효 영구) |
| NOTE-6 | 추가 backend 후보 (exllamav2/TabbyAPI/MLX/Triton) LOW carry-over |
| NOTE-7 | LiteLLM lock-in 우려 정직성 (§9.3.4 footnote 답습) |

### 11.5 기각 3 매트릭스 (정직성 의무)

| 기각 # | 출처 | 기각 근거 |
|---|---|---|
| 기각-1 | C-B-C1 LiteLLM/llama-swap ⭐⭐⭐ CRITICAL → REC-5 강등 | 본 cycle = design doc *추출* + (k) carry-over 자격 충족, MVP-1 결정 *고정* 0건, lock-in 우려 정직성 (NOTE-7) |
| 기각-2 | C-B-C3 threshold 단일 채택 거부 | BLOCKING-10 (HIGH 유지) + T1~T6 다중 tier 포함 + (j) 별도 cycle 측정 후 결정 *후보* |
| 기각-3 | (4-way-X) 추가 흡수 의무 0 | §0 #15 + §7 #15 + §10 답습 완전 |

### 11.6 분량 비교

- v1: 371줄
- v1.1: ~600줄 (예상)
- 핵심 신규 절: §9.3.1 (boss.py verbatim) + §9.3.2 (Boss 신뢰 경계) + §9.3.3 (Backend 매트릭스 OpenAI-compatible) + §9.3.4 (LiteLLM 4 후보 footnote) + §11 (변경 일람)
