# (4-way) MVP-1 4 차원 통합 *분석* cycle entry brief v1

**일자**: 2026-05-26
**유형**: 진입 brief (Phase 0, 6단계 변형 entry form, R-rec-16 답습)
**선행**: (R4-body) 19번째 entry cycle 완주 (chain 영구 종결 의무 답습 영구)
**자격**: (R4-body) §8 carry-over HIGH ⭐⭐ 상위 scope, 사용자 명시 "(4-way) 통합 *분석* cycle HIGH (상위 scope)" + 2 명확화 (scope 4 차원 모두 포함 + 수단 read-only + Boss 추상화 design 코드 0)

---

## 0. 본 brief 의 *하지 않는 것* (16 항목, R-15 self-consistency 영구)

1. ❌ **R4 / F2 / Provider Liquidity / (j) 4 차원 본문 *직접* 정정** (R-9 답습 영구 — 본 cycle = read-only 통합 *분석* + Boss 추상화 design draft only, 본문 정정 = 별도 cycle 의무)
2. ❌ **헌법 / ADR-011 / 다른 ADR / 다른 architecture / guides / CLAUDE.md 본문 변경** (R-9 답습 영구)
3. ❌ **Boss 추상화 *실제 코드 작성*** (`src/jarvis/boss/*.py` 0건 — 본 cycle = design doc draft only, 실제 구현 = (l) MVP-1 트랙 B 별도 cycle)
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

### 1.1 4 차원 매트릭스 (사용자 명시 "4 차원 모두 포함")

| 차원 | scope | input source | output 자격 |
|---|---|---|---|
| **R4** | MVP-1 R4 framing 정정 *후속* 재검증 | (R4-evidence) raw + (R4-body) Edit 4건 결과 | R4 정정 후 일관성 평가 + 후속 보강 자격 평가 |
| **F2** | classical MoE > SSM hybrid 가설 강화 평가 | (g) Qwen3-Next-80B SSM 32.3 vs (h) Qwen3-30B-A3B classical 49.6 = ~1.54× | 가설 강화 정도 + 변수 미해소 정직성 + (g)/(h) carry-over 종합 |
| **Provider Liquidity** | Boss 추상화 interface design draft (헌법 5조-2 비협상) | [[project_jarvis_local_boss_direction]] + [[feedback_provider_liquidity]] + 본 brief §1 (h)/(h-O)/(h-OM) 답습 | BossLLM ABC 정의 + OllamaBoss/LlamaCppBoss/vLLMBoss 교체 자격 평가 (코드 0, design only) |
| **(j)** | advisory wall-clock 측정 cycle 진입 자격 평가 | (R4-body) M3 매트릭스 정정안 + decode generation ~3.24~3.38× + Phase 1 ~4.07× | (j) 진입 자격 충족도 + 선결 cycle 종합 (Phase 1 N=3 repetitions + Ollama embedded llama.cpp version verify 등 carry-over 의존성) |

### 1.2 4 차원 *교차 의존성* 명문 (R-9 답습 영구 정직성)

- R4 ↔ F2: R4 정정 결과 ((R4-body) M3 정정 framing) 는 F2 가설 강화 *근거* (decode generation ~3.24~3.38× = Ollama framework overhead 본질, source conversion 무관, S1 confirmed)
- R4 ↔ Provider Liquidity: R4 정정 후 framing = "llama.cpp > Ollama 확정" → Boss 추상화 시 LlamaCppBoss 우선 후보 + OllamaBoss = MVP-1 비채택 자격 약화 (단, *고정* (k) 별도 cycle 의존)
- R4 ↔ (j): R4 decode generation 격차 (~3.24~3.38×) = (j) advisory wall-clock budget 평가 *결정적* input (~15 t/s threshold 답습 자격 평가)
- F2 ↔ Provider Liquidity: SSM hybrid vs classical MoE 가설 = 모델 교체 자격 평가 input (헌법 5조-2 함의)
- F2 ↔ (j): F2 가설 미해소 변수 (model size + expert routing + 도구 version) = (j) 측정 cycle 의존성 의무
- Provider Liquidity ↔ (j): Boss 추상화 interface = (j) advisory wall-clock 측정 시 OllamaBoss/LlamaCppBoss 모두 측정 자격 충족 의무

→ **본 cycle = 4 차원 교차 의존성 종합 *분석* + Boss 추상화 design draft**

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

### 2.3 Provider Liquidity 차원 분석 대상

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
- llama.cpp 49.6 t/s (bartowski direct)
- Ollama 14.69~15.29 t/s (qwen3:30b-a3b-instruct-2507-q4_K_M)
- vLLM = MVP-1 비채택, MVP-2 재검토 (line 126 verbatim 보존)

### 2.4 (j) 차원 분석 대상

**advisory wall-clock budget input**:
- R5 권고 ~15 t/s threshold (MoE 2~8배 여유, brief v2)
- 결정적 flag 분리 + Boss advisory (R1~R3 답습)
- prefill 입력 상한 / 요약 (R5 권고)

**선결 cycle carry-over**:
- Phase 1 N=3 repetitions Ollama 답습 MEDIUM
- Ollama embedded llama.cpp version verify MEDIUM
- (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM
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
| (1) brief v1 작성 + commit (본 단계) | scope 4 차원 + 수단 read-only + Boss 추상화 design draft + 6단계 변형 | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) + Reviewer 통합 합의 | 사용자 명시 후 |
| (3) brief v1.1 보강 + commit | BLOCKING verbatim 100% + R-S* 흡수 + §11 v→v1.1 일람 신규 | 합의 후 |
| (4) 분석 결과 + Boss 추상화 design doc commit | 4 차원 종합 분석 + Boss 추상화 design (`docs/architecture/jarvis-mvp1-boss-abstraction-design.md`, 코드 0) | 합의 + 사용자 명시 후 |
| (5) SESSION 20번째 + INDEX + commit | R-1 anchor 26회 sudo 1회 R-S4 발효 자격 별도 분리 + chain (1)~(4) 답습 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

### 3.3 분석 후 cross-check 의무 (R-S2 + R-S5 답습 cascade scope 확장)

- 분석 본문 evidence raw 답습 정합성 verify (4-way + Phase 1 5-way 핵심 숫자 grep)
- Boss 추상화 design = 코드 0건 verify (`src/jarvis/` 변경 0건)
- **헌법/ADR cascade 0건 verify**: `git diff docs/constitution/ docs/decisions/ docs/architecture/ docs/guides/ CLAUDE.md` = 0 (단 본 cycle commit 자체 = brief + 합의 + 분석 결과 + Boss 추상화 design doc 신규 제외)
- **cascade verify scope 확장 (R-S5 답습)**: `git diff /home/delangi/.claude/projects/.../memory/ docs/phase0/ docs/review/ docs/sessions/ docs/INDEX.md` = 0 (단 본 cycle commit 자체 제외)
- **R4 referent 보존 verify** ((R4-body) 답습): MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85 + (R4-body) Edit 결과 4 위치 모두 보존
- **vLLM 부분 보존 verify**: line 126 vLLM section verbatim 유지 (R-S1 답습)
- **비밀번호 누출 verify (R-S2 발효 영구)**: 본 brief + 분석 결과 + Boss 추상화 design 모두 grep `<REDACTED-PWD-PATTERN>` = 0건

---

## 4. 분석 후 영향 평가 (헌법/ADR cascade 0건 + Provider Liquidity 본질 답습)

### 4.1 헌법 5조-2 (Provider Liquidity, 비협상) 답습 정합

- 헌법 5조-2 본문 변경 0건 의무 답습 영구
- Provider Liquidity 원칙 = 모델/구독/오케스트레이터 교체 코드 변경 0 + 락인 0 + 최소 2 provider always-on
- 본 cycle Boss 추상화 design = Provider Liquidity 원칙 *직접 실현* 의무 (BossLLM ABC + 다중 backend 교체 자격)
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

## 5. 분석 본문 사전 명문 (§9 답습 의무, 합의 후 v1.1 보강 후 확정안)

본 brief v1 §9 = 합의 *전* 사전 명문 4 차원 매트릭스. 단계 (3) brief v1.1 보강 시 합의 BLOCKING + R-S* 흡수 후 *확정안*. 단계 (4) 분석 결과 + Boss 추상화 design doc commit 시 §9 확정안 답습.

---

## 6. 정직성 한계 (R-6 답습, 16 항목)

1. 본 cycle = 4 차원 통합 *분석* cycle (R-9 답습 영구 본문 정정 자격 0건, 별도 cycle 의무) — sensitivity 매우 높음 (4 차원 묶음)
2. scope 한정 = R4 framing 정정 *후속* 재검증 + F2 가설 강화 평가 + Provider Liquidity Boss 추상화 design draft + (j) 진입 자격 평가
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
13. Boss 추상화 design = design doc only (실제 코드 0건, (l) MVP-1 트랙 B 별도 cycle)
14. (j) advisory wall-clock = 진입 자격 *평가* only (측정 = (j) 별도 cycle)
15. R-S2 발효 — password literal redact 답습 영구 (본 brief + 분석 결과 + Boss 추상화 design 모두)
16. **본 cycle 4 차원 교차 의존성 명문 (§1.2) = 정직성 핵심** — 단일 차원 단독 결론 추출 금지, 4 차원 종합 *분석* 의무

---

## 7. 차단 조건 (§0 1:1 매핑 답습, R-15 self-consistency 영구)

본 §0 *하지 않는 것* 16 항목과 §7 차단 조건은 **1:1 매핑 의무**.

1. ❌ R4 / F2 / Provider Liquidity / (j) 4 차원 본문 *직접* 정정
2. ❌ 헌법 / ADR-011 / 다른 ADR / 다른 문서 본문 정정 (R-9 답습 영구)
3. ❌ Boss 추상화 *실제 코드 작성*
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
| (R4-body) 완료 후 cascade 검토 cycle LOW | (R4-body) §8 R-10 발효 #19 | 정정 후 cascade verify | ❌ 본 cycle scope 외 (별도 LOW cycle) |
| vLLM verify cycle LOW | (R4-body) §8 R-9 답습 | vLLM 부분 external reference | ❌ 본 cycle scope 외 (별도 LOW cycle) |
| (h-OL) llama.cpp Ollama library blob 측정 MEDIUM | (h-O)/(h-OM) R-15 답습 | 5-way 측정 | ❌ 본 cycle scope 외 (별도 측정 cycle, 본 cycle = read-only) |
| (j) advisory wall-clock 측정 MEDIUM | (R4-body) §8 | (j) 측정 cycle | 🟡 본 cycle = (j) 진입 자격 *평가* only |
| (k) M3·M4 결정 *고정* DEFER | 답습 영구 | (k) 별도 cycle | ❌ 변수 분리 input 강화 후 (본 cycle = input 강화 자격) |
| (l) MVP-1 트랙 B 구현 DEFER | 답습 영구 | (k) 통과 후 | ❌ 본 cycle = design draft only |

### 8.2 본 cycle 자격 충족 verify

- ✅ (R4-body) §8 HIGH carry-over 직접 후속 자격
- ✅ 사용자 명시 "(4-way) 통합 *분석* cycle HIGH (상위 scope)" 답습
- ✅ 사용자 명시 scope 4 차원 모두 포함
- ✅ 사용자 명시 수단 read-only + Boss 추상화 design (코드 0)
- ✅ chain 영구 종결 의무 답습 영구 ((4-way) 단독 명명, X prime/super-prime 금지)
- ✅ R-9 답습 영구 (본문 정정 0건 의무)
- ✅ 6단계 변형 entry form (R-rec-16 답습)

### 8.3 본 brief 자체 후속 단계 (6단계 변형 R-rec-16 답습)

| 단계 | 내용 | 사용자 명시 |
|---|---|---|
| (1) brief v1 작성 + commit (본 단계) | scope 4 차원 + 수단 read-only + Boss 추상화 design draft + 6단계 변형 | **진행 중** |
| (2) 풀 3+1 합의 진행 + commit | 3+1 합의 + BLOCKING + R-S* | 결과 확인 후 |
| (3) brief v1.1 보강 + commit | BLOCKING verbatim 100% + R-S* 흡수 + §11 v→v1.1 일람 신규 | 합의 후 |
| (4) 분석 결과 + Boss 추상화 design doc commit | §9 확정안 답습 + Boss 추상화 design doc 신규 (코드 0) | 합의 + 사용자 명시 후 |
| (5) SESSION 20번째 + INDEX + commit (R-1 anchor 26회 sudo 1회 R-S4 발효) | 답습 패턴 | 결과 확인 후 |
| (6) push | origin/feature/jarvis-mvp0 | 결과 확인 후 |

---

## 9. 분석 본문 사전 명문 4 차원 매트릭스 (합의 후 v1.1 흡수, 단계 (4) commit 시 답습)

### 9.1 R4 차원 분석 사전 명문

**R4 정정 후 일관성 평가**:
- (R4-body) Edit 4건 = MVP-1 brief 3 위치 + MVP-1 합의 보고서 1 위치, line 126 vLLM verbatim 보존
- R4 referent 5 위치 (MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85) 보존 verify ✓
- 정정 후 framing = "llama.cpp > Ollama 확정" + 4 차원 격차 명문 + (k) 별도 + Provider Liquidity 약화 0건

**후속 보강 자격**:
- 본 cycle 분석 = R4 정정 *후속* 일관성 확정 ✓
- 추가 cascade 검토 = LOW carry-over (별도 cycle, R-10 발효 정직성 #19)

### 9.2 F2 차원 분석 사전 명문

**F2 가설 강화 정도**:
- (g) Qwen3-Next-80B SSM hybrid 32.3 vs (h) Qwen3-30B-A3B classical 49.6 = ~1.54× (decode generation)
- classical MoE > SSM hybrid 모든 차원 빠름 (S2 강화 시나리오 일부 답습)

**미해소 변수 정직성 (N-7 답습 영구)**:
- model size (80B vs 30B) — 단독 변수 분리 cycle 별도
- expert routing (Qwen3-Next sparse vs Qwen3-30B 표준) — 별도 cycle
- 도구 version (Qwen3-Next branch vs `c0c7e147` master) — 별도 cycle
- → F2 가설 *간접* input only (N-7 답습 영구)

**(g)/(h) carry-over 종합**:
- F2 가설 = (k) M3·M4 결정 *고정* 자격 *간접* input
- (l) MVP-1 트랙 B 구현 시 model size 30B 우선 후보 (50% 빠름 + classical MoE evidence)

### 9.3 Provider Liquidity 차원 분석 사전 명문 (Boss 추상화 interface design draft)

**BossLLM ABC 정의 (design draft, 코드 0)**:
```python
# docs/architecture/jarvis-mvp1-boss-abstraction-design.md 명문 후보
class BossLLM(ABC):
    @abstractmethod
    def advise(self, request: AdvisoryRequest) -> BossAdvice: ...
    @abstractmethod
    def health_check(self) -> bool: ...
```

**Backend 후보 매트릭스 (4-way 측정 evidence 답습)**:
| backend | 측정 t/s (decode gen) | 우선순위 | 비고 |
|---|---|---|---|
| **LlamaCppBoss** | 49.6 (Qwen3-30B-A3B classical, bartowski direct) | ⭐⭐⭐ MVP-1 우선 | 빠름 / API direct |
| **OllamaBoss** | 14.69~15.29 (qwen3:30b-a3b-instruct-2507-q4_K_M) | ⭐⭐ MVP-1 보조 | Provider Liquidity 보조 + Modelfile 호환 |
| vLLMBoss | (MVP-1 비채택) | MVP-2 재검토 | line 126 verbatim 보존, sm_120/121 binary-compat |

**Provider Liquidity 직접 실현 (헌법 5조-2 비협상)**:
- BossLLM ABC = 모델/backend 교체 = config 변경만, 코드 변경 0건
- 최소 2 backend always-on (LlamaCppBoss + OllamaBoss) → Provider Liquidity 만족
- vLLMBoss = MVP-2 진화 경로 (영구 배제 금지, line 126 verbatim 답습)

**advisory failure handling (R3 답습 fail-closed 정신)**:
- advisory 실패 시 결정적 flag·게이트 진행 (비차단)
- 사람에게 "Boss advisory 실패" 명시 경고 (R3 답습)
- BossAdvice frozen dataclass (R2 답습, 콜백·경로·명령 필드 금지)

### 9.4 (j) 차원 분석 사전 명문

**(j) advisory wall-clock 진입 자격 충족도**:
- R5 권고 ~15 t/s threshold = (h-O) Ollama 14.69~15.29 ≈ threshold, (h) llama.cpp 49.6 = 3.3× 여유
- LlamaCppBoss 우선 시 = ~15 t/s threshold 충족 ⭐⭐⭐
- OllamaBoss 우선 시 = ~15 t/s threshold 경계 🟡 (Phase 1 N=3 repetitions 검증 의무)

**선결 cycle carry-over 의존성**:
- Phase 1 N=3 repetitions Ollama 답습 MEDIUM (Ollama 분산 검증)
- Ollama embedded llama.cpp version verify MEDIUM (변수 분리)
- (h-OL) llama.cpp Ollama library blob 직접 측정 MEDIUM (5-way confirm)
- Ollama prefill processing framework overhead 검증 MEDIUM (F-4 (h-OM) 답습)

**(j) 진입 자격 결론**:
- LlamaCppBoss 우선 + Phase 1 N=3 verify 후 → (j) 진입 자격 충족 가능
- 본 cycle 결과 = (j) 진입 자격 *평가* only, 측정 = (j) 별도 cycle 의무

### 9.5 분석 후 cross-check 의무 (R-S2 + R-S5 답습 cascade scope 확장)

- 4 차원 evidence raw 답습 정합성 verify (4-way + Phase 1 5-way 핵심 숫자 grep)
- Boss 추상화 design doc = 코드 0건 verify (`src/jarvis/` 변경 0건)
- 헌법/ADR/다른 문서 본문 변경 0건 verify
- **cascade verify scope 확장 (R-S5 답습)**: 메모리 + 다른 phase0/review/sessions/INDEX 본문 변경 0건
- R4 referent 보존 verify + line 126 vLLM verbatim 보존 verify
- **비밀번호 누출 verify (R-S2 발효 영구)**: grep `<REDACTED-PWD-PATTERN>` = 0건 (literal password pattern 직접 사용 0건)

---

## 10. 본 brief v1 본 cycle 진입 자체 영구 권위

- 본 brief v1 = (R4-body) 19번째 entry cycle 완주 후 carry-over HIGH ⭐⭐ 상위 scope (4-way) 통합 *분석* cycle entry 단계 (1)
- ⭐⭐⭐ scope 4 차원 모두 포함 (R4 + F2 + Provider Liquidity + (j)) — 본 cycle = *상위* scope 종합 *분석*
- ⭐⭐⭐ 수단 = read-only analysis only + Boss 추상화 design doc draft (코드 0) — R-9 답습 영구 본문 정정 0건
- ⭐⭐ 4 차원 교차 의존성 명문 (§1.2) — 단일 차원 단독 결론 추출 금지
- ⭐⭐ R-15 self-consistency 영구 — §0 16 항목 ↔ §7 차단 조건 1:1 매핑
- ⭐ R-1 anchor 26회 누계 자격 (chain (g)/(h)/(h-O)/(h-OM)/(R4-evidence)/(R4-body)/(4-way), sudo 1회 의무 R-S4 발효 자격 별도 분리)
- 본 brief 자체 머신 변경 0건 (측정/Modelfile/ollama/sudo/본문 정정 0)
- 다음 단계 진입 = 사용자 명시 의무 답습 영구
- **(4-way-X) prime/super-prime 자동 진입 명백 부정 답습 영구**
