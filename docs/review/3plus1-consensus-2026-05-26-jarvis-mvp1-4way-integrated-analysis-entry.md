# (4-way) MVP-1 4 차원 통합 분석 cycle entry brief v1 — 3+1 합의 보고서

**일자**: 2026-05-26
**대상 brief**: `docs/phase0/jarvis-mvp1-4way-integrated-analysis-entry-brief.md` (commit `af7ac8b`, 371줄)
**합의 형식**: 3+1 (Agent A 구현 + Agent B 품질/안전성 + Agent C 대안 + Reviewer 통합)
**Reviewer 직접 verify**: `src/jarvis/boss.py` 99줄 read + git log 답습 — A-B-A1/B-A2/B-A3 핵심 주장 100% 사실 confirmed (commit `83aebad`, 2026-05-22, @runtime_checkable Protocol + BossAdvice frozen(summary/extra_flags/advisory_failed) + AdviceRequest + StubBoss + merge_flags)

---

## 1. 3 Agent 판정 매트릭스

| Agent | 판정 | BLOCKING | 권고 | NOTE |
|---|---|---|---|---|
| A 구현 | APPROVE w/ COND | 11 | 4 (P-A1~P-A4) | 5 (N-A1~N-A5) |
| B 안전 | APPROVE w/ COND | 4 | 5 (B-rec-1~5) | 10 (B-N1~B-N10) |
| C 대안 | APPROVE w/ COND | 4 | 5 (P-1~P-5) | 7 (N-1~N-7) |
| **합산** | **APPROVE w/ COND (3/3)** | **19 raw** | **14 raw** | **22 raw** |

판정 = 3/3 만장일치 APPROVE w/ COND. REJECT 0건. 정정 후 진입 자격 = 충분.

---

## 2. 일치 (Consensus, 3개 동의)

| # | 항목 | 출처 |
|---|---|---|
| C-1 | **OpenAI-compatible `/v1/chat/completions` endpoint 통일 채택 + 명문 의무** | A-B-A4 + B-N10 간접 + C-B-C2 |
| C-2 | **brief §9.3 BossLLM "ABC" 코드 블록 = 실제 코드와 부정합** (실제 = Protocol, 필드 불일치) | A-B-A1+B-A2+B-A3 + B-B-B1 (BossAdvice 필드 누락) + C 묵시 (verify 대상) |
| C-3 | **6단계 변형 + read-only + design draft only + chain 영구 종결 = scope 자격 충분** | A-N-A1~5 + B-B-N7 + C-N-1~7 |
| C-4 | **threshold ~15 t/s 단일 후보 framing = 보강 의무** ((j) 별도 cycle 측정 후 결정) | A-B-A10 + B-B-rec-5 cousin + C-B-C3 |
| C-5 | **vLLMBoss MVP-1 비채택 / MVP-2 재검토 / line 126 verbatim 보존 자격 명문 의무** | A-B-A7 + B-B-N5 + C-B-C4 |
| C-6 | **"fail-closed 정신" framing 부정확 / 정정 의무** | A-B-A5 (fail-open + fail-safe 분리) + B-B-rec-3 (health_check fail-closed 별개) + C-P-2 (fail-closed 비차단 framing 명료화) |

**채택**: 6건 모두 BLOCKING-1~6 으로 그대로 채택 (3개 동의 = 강한 합의).

---

## 3. 부분 일치 (Partial, 2+1)

| # | 항목 | 다수 (2) | 소수 (1) | 결정 |
|---|---|---|---|---|
| P-1 | **boss.py 이미 존재 (commit `83aebad`) → brief framing "코드 0" 정정 의무** | A (B-A1 CRITICAL) + Reviewer 직접 verify | B/C 묵시 (verify 미수행) | **채택** (Reviewer 직접 verify 로 격상 = 다수+1) |
| P-2 | **localhost 127.0.0.1 바인딩 의무 명문 (M6 + R11 답습)** | B (B-B2 CRITICAL) + C 묵시 (security 우려) | A 미언급 | **채택** (보안 의무 = 단독 적출이어도 CRITICAL 자격) |
| P-3 | **워커 실패 시 advise 미호출 (R8 답습) 명문** | B (B-B4 HIGH) + 코드 (StubBoss.calls 답습) | A/C 미언급 | **채택** (코드 docstring R8 직접 명문, brief 누락 부정합) |
| P-4 | **R10 + R1 의미적 green washing 방어 명문 (BossAdvice.summary 종속 금지)** | B (B-B3 HIGH) + 코드 docstring 답습 | A/C 미언급 | **채택** (코드 line 11 직접 명문, brief 누락) |
| P-5 | **LiteLLM + llama-swap 대안 layer 명문** | C (B-C1 CRITICAL) + 외부 evidence (NVIDIA Dev Forum 2026-05) | A/B 미언급 | **부분 채택** (대안 매트릭스 §9.3 footnote 신규, MVP-1 결정 *후보* only, lock-in 우려 정직성 N-7 답습) |
| P-6 | **prefill overhead 별도 cycle / wall-clock = decode + prefill 모두 포함** | A (B-A10 + P-A3) + B (B-N4 R4-body cascade) | C 권고 P-3 부분 | **채택** (advisory wall-clock = decode-only 정의 부정확) |

---

## 4. 불일치 (Divergence, 3개 모두 다른 의견)

| # | 항목 | A | B | C | 결정 |
|---|---|---|---|---|---|
| D-1 | **boss.py framing 처리 방안** | "기존 구현 design doc 분리 + backend 후보 매트릭스 신규" | (미언급, 코드 verify 미수행) | (미언급) | **A 채택** + Reviewer 보강: 단계 (4) "Boss 추상화 design doc 신규" = "기존 boss.py 의 design doc 추출 + backend 후보 매트릭스 신규" 로 framing 변경 |
| D-2 | **(j) ~15 t/s threshold 처리** | MEDIUM (prefill 포함 명문) | 묵시 (sm_121 stability) | T1~T6 다중 후보 (~10/~15/~20/~30/동적/다중 tier) | **C 채택** + A/B 보강: §9.4 "threshold 후보 매트릭스" 신규 + (j) 별도 cycle 측정 후 결정 *후보* only |
| D-3 | **(4-way-X) chain 종결 강조** | P-A4 "(4-way-X) chain 영구 종결" | 묵시 | N-5 "(4-way-X) prime 부정" | **3 모두 일치 본질** (D 아닌 C 자격) — §0 #15 + §7 #15 + §10 line 371 답습 완전 (브리프 자체 충족, 추가 흡수 의무 0) |

D-1, D-2 = 분명한 불일치 → 합의 채택. D-3 = 사실 만장일치 → BLOCKING 흡수 의무 0건 (이미 brief 답습).

---

## 5. 누락 (Gap, 특정 Agent 단독)

| # | 항목 | Agent | 중요도 평가 | 채택 자격 |
|---|---|---|---|---|
| G-1 | model size 단독 분리 cycle 명명 (P-A1) | A 단독 | MEDIUM (F2 미해소 변수) | **권고 흡수** ((m) 명명 후보) |
| G-2 | worker.py 원칙 동형 답습 (P-A2) | A 단독 | LOW (직접 영향 0) | NOTE 흡수 |
| G-3 | (j) → (k) → (l) chain 의존성 명시 (B-A11) | A 단독 | MEDIUM (cycle 순서 정직성) | **권고 흡수** (§9.4 footer) |
| G-4 | sm_121 stability "실동작 보고" 정직성 (B-rec-1) | B 단독 | MEDIUM (외부 evidence 답습) | **권고 흡수** (vLLMBoss "MVP-2 재검토 trigger" 열) |
| G-5 | Boss prompt injection 방어 표면 평가 (B-rec-2) | B 단독 | HIGH (보안) | **권고 흡수 → BLOCKING 격상** (Reviewer R-S2 자격) |
| G-6 | health_check 실패 시 fail-closed (B-rec-3) | B 단독 | MEDIUM (advise vs health_check 분리) | **권고 흡수** |
| G-7 | R4 referent "5 위치" 산술 자기모순 (B-rec-4 + B-N1) | B 단독 | HIGH (정직성 핵심) | **권고 흡수 → BLOCKING 격상** (Reviewer R-S3 자격) |
| G-8 | Boss LLM 도 신뢰 안 함 (B-rec-5) | B 단독 | HIGH (R10 답습) | **권고 흡수** (P-4 합산 강화) |
| G-9 | OllamaBoss N=3 미수행 (B-N3) | B 단독 | MEDIUM (Phase 1 carry-over) | NOTE 흡수 |
| G-10 | 추가 backend 후보 (exllamav2/TabbyAPI/MLX/Triton) LOW carry-over (P-1) | C 단독 | LOW | NOTE 흡수 |
| G-11 | prefill 입력 상한 후보 (~512/~1024/~2048/~4096) + 요약 (TextRank/LLM/sliding window) (P-3) | C 단독 | MEDIUM ((j) input 강화) | **권고 흡수** |
| G-12 | F2 변수 분리 cycle 우선순위 후보 (P-4) | C 단독 | MEDIUM | **권고 흡수** (G-1 합산) |
| G-13 | R4 후속 보강 dimension (P-5) | C 단독 | LOW | NOTE 흡수 |
| G-14 | src/jarvis/boss/ vs boss.py path 혼동 risk (N-A5) | A 단독 | MEDIUM (design doc path) | **권고 흡수** (design doc 신규 = `docs/architecture/jarvis-mvp1-boss-abstraction-design.md` 명문 답습 ✓, src/ path 0건 verify) |
| G-15 | LlamaCppBoss N=1 정직성 (N-A2) | A 단독 | MEDIUM | **권고 흡수** ((h) bartowski direct N=3 분산 검증 carry-over) |

---

## 6. Reviewer 단독 격상 (R-S*)

Reviewer 직접 코드 verify + 4-way 답습 cross-check 결과, 3 Agent 모두 미적출 또는 부분 격상 자격 사항 격상:

### R-S1 ⭐⭐⭐ CRITICAL: brief §9.3 코드 블록 = 실제 `src/jarvis/boss.py` 와 verbatim cross-check 의무

**근거**:
- Reviewer 직접 verify 결과 `src/jarvis/boss.py` 99줄 = commit `83aebad` (2026-05-22) 로 이미 구현 존재
- 실제 = `@runtime_checkable` Protocol (line 53), `class BossLLM(Protocol)` (line 54), advise 메소드 signature `def advise(self, req: AdviceRequest) -> BossAdvice` (line 63)
- 실제 BossAdvice = `summary: str / extra_flags: list[str] / advisory_failed: bool = False` (line 38~50), confidence 필드 0건 (R6 답습)
- 실제 AdviceRequest = `prompt / worker_alias / output / deterministic_flags` (line 24~35)
- 실제 StubBoss = `calls` 답습 (R8 verify 자격, line 67~89), `fail=True` 시 `RuntimeError` (R3 검증 경로)
- 실제 merge_flags = `[*deterministic, *(f for f in extra if f not in deterministic)]` (R1 fail-safe 불변식, line 92~98)
- brief §9.3 line 308~314 ABC 코드 블록 = 실제와 100% 부정합

**흡수 의무**: §9.3 "BossLLM ABC 정의 (design draft, 코드 0)" framing 전면 변경:
1. 제목 변경: "BossLLM Protocol (기존 구현 design doc 추출, src/jarvis/boss.py:54 답습)"
2. 코드 블록 = `src/jarvis/boss.py` verbatim 인용 (line 18~98, 또는 핵심 4 부분 = AdviceRequest + BossAdvice + BossLLM Protocol + merge_flags)
3. "ABC" 단어 모두 삭제 → "Protocol (@runtime_checkable)" 로 교체
4. BossAdvice 필드 verbatim 명문 (summary + extra_flags + advisory_failed) + confidence 삭제 답습 R6 명문
5. AdviceRequest 필드 verbatim 명문 (prompt + worker_alias + output + deterministic_flags)
6. merge_flags 함수 = R1 fail-safe 불변식 명문 (감산 불가)
7. **§0 #3 "Boss 추상화 *실제 코드 작성* 0건" framing 변경**: "Boss 추상화 *신규* 코드 작성 0건 (기존 `src/jarvis/boss.py` 99줄 = commit `83aebad` 답습, 본 cycle 변경 0건)"
8. **§3.3 + §9.5 cross-check 의무 추가**: `git diff src/jarvis/boss.py src/jarvis/orchestrator.py src/jarvis/approval.py = 0` verify 의무

### R-S2 ⭐⭐⭐ CRITICAL: Boss 입력 = untrusted (prompt injection 표적) 명문 — 4 차원 보안 의무

**근거**:
- `src/jarvis/boss.py` line 26~30 AdviceRequest docstring 직접 명문: "모두 untrusted(워커 출력 포함, prompt injection 표적). Boss 는 이 입력으로 *텍스트만* 생성한다. 실행·게이트 통과·workdir·argv 에 대한 어떤 제어 정보도 여기서 도출되지 않는다(§5 신뢰 경계)."
- Agent B B-rec-2 "Boss prompt injection 방어 표면 평가" 부분 적출 (권고 자격으로만)
- B-B4 "워커 실패 시 advise 미호출 (R8)" = 침해된 워커 advisory injection 표면 회피 의무 직접 명문 (실패 출력 = 침해 표면)
- 본 brief §9.3 Provider Liquidity 차원 = Boss 추상화 design = 신뢰 경계 명문 의무 (B-B3 R10 + R1 의미적 green washing 방어와 합산)
- 코드 line 5~13 docstring R1/R2/R3/R6 답습 모두 보안 의도 명문

**흡수 의무**: §9.3 BossLLM Protocol 코드 블록 직후 추가:
1. "Boss 입력 신뢰 경계 (R10 + R8 답습)": AdviceRequest 모든 필드 = untrusted (워커 출력 포함, prompt injection 표적)
2. "Boss 출력 신뢰 경계 (R2 답습)": BossAdvice = 텍스트 전용 — 콜백/경로/명령 필드 금지, 실행·게이트 통과·workdir·argv 도출 0건
3. "Boss = root of trust 아님 (ADR-011 §2.1 + MVP-1 brief v2 §5 답습)": 결정적 flag + raw diff + ReviewGuard 권위만 게이트 좌우, BossAdvice.summary 종속 금지
4. "워커 실패 시 advise 미호출 (R8)": `result.is_error` → BossLLM.advise 호출 0건 (침해된 워커 advisory injection 표면 회피 의무)
5. "advisory failure ≠ health_check failure 분리" (B-rec-3 답습): advise 실패 = fail-open (R3, 비차단 + 경고), health_check 실패 = (k) 별도 cycle 결정 후보

### R-S3 ⭐⭐ HIGH: R4 referent "5 위치" 산술 자기모순 정직성

**근거**:
- B-rec-4 + B-N1 단독 적출: brief §9.1 line 281 "R4 referent 5 위치 (MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85) 보존 verify ✓"
- 산술 = 1 + 3 = 4 위치 (산술적 자기모순)
- (R4-body) cycle 답습 = 4 위치 (3 + 1) 의도 가능
- 정직성 = brief v1.1 보강 의무

**흡수 의무**: §9.1 line 281 정정:
- "R4 referent 4 위치 (MVP-1 brief line 161 + MVP-1 합의 보고서 line 52/79/85) 보존 verify ✓"
- 또는 5번째 referent 명문 (만약 별도 referent 존재 시) — Reviewer 직접 verify 후 결정 의무
- (R4-body) 19번째 entry chain raw report 답습 cross-check 의무

### R-S4 ⭐⭐ HIGH: Phase 1 N=3 repetitions Ollama 답습 carry-over MEDIUM = (j) 진입 자격 선결 의무 명문

**근거**:
- brief §2.4 + §9.4 "Phase 1 N=3 repetitions Ollama 답습 MEDIUM" 답습 ✓
- B-N3 "OllamaBoss N=3 미수행" + N-A2 "LlamaCppBoss N=1 정직성" 합산
- (j) 진입 자격 결론 (line 347) = "LlamaCppBoss 우선 + Phase 1 N=3 verify 후 → (j) 진입 자격 충족 가능"
- "충족 가능" framing = N=3 verify *선결* 의무 명시 강화 필요

**흡수 의무**: §9.4 "(j) 진입 자격 결론" 강화:
- "선결 cycle carry-over 의존성 = MEDIUM 4건 모두 (j) 진입 *전* 충족 의무"
- "Phase 1 N=3 repetitions Ollama 답습 = 분산 검증 필수, 단일 측정 = (j) 진입 자격 충족 0건"
- "LlamaCppBoss bartowski direct N=3 별도 측정 cycle (h)' carry-over MEDIUM" 명문

---

## 7. 통합 BLOCKING (brief v1.1 흡수 의무 매트릭스)

총 BLOCKING **15건** (3 Agent BLOCKING 19 raw + R-S* 4 → 중복 제거 + 격상 후 15건)

| # | 위치 | 항목 | 등급 | 출처 (Agent) | 흡수 방안 |
|---|---|---|---|---|---|
| **BLOCKING-1** | §9.3 framing | brief §9.3 "Boss 추상화 *실제 코드 작성* 0건" framing = boss.py 이미 commit `83aebad` 99줄 존재와 부정합 | ⭐⭐⭐ CRITICAL | A-B-A1 + Reviewer verify | §9.3 + §0 #3 + §1.1 Provider Liquidity 행 framing 전면 변경 "design draft" → "기존 구현 design doc 분리 + backend 후보 매트릭스 신규" |
| **BLOCKING-2** | §9.3 코드 블록 | 실제 = `@runtime_checkable Protocol` (ABC ≠ Protocol) | ⭐⭐⭐ CRITICAL | A-B-A2 + R-S1 | §9.3 line 308~314 코드 블록 = `src/jarvis/boss.py` verbatim 인용 (BossLLM Protocol + AdviceRequest + BossAdvice + merge_flags), "ABC"/"@abstractmethod" 단어 삭제 |
| **BLOCKING-3** | §9.3 코드 블록 | BossAdvice 필드 (summary + extra_flags + advisory_failed) + AdviceRequest 필드 + R6 confidence 삭제 답습 명문 부재 | ⭐⭐⭐ CRITICAL | A-B-A3 + B-B-B1 + R-S1 | §9.3 BossLLM Protocol 직후 BossAdvice/AdviceRequest dataclass verbatim 인용, R6 confidence 금지 명문 + R2 콜백·경로·명령 필드 금지 명문 |
| **BLOCKING-4** | §9.3 보안 의무 | localhost 127.0.0.1 바인딩 의무 명문 누락 (M6 + R11 답습) | ⭐⭐⭐ CRITICAL | B-B-B2 + R-S2 cousin | §9.3 Backend 매트릭스 직후 "보안 의무 (M6 + R11 답습 영구): OllamaBoss/LlamaCppBoss endpoint = 127.0.0.1 localhost 한정, 외부 노출 금지, 추론 시점 egress 0, (j) 측정 cycle 실측 확인" |
| **BLOCKING-5** | §9.3 Boss 신뢰 경계 | Boss 입력 = untrusted (prompt injection 표적) + Boss = root of trust 아님 + R10 + R1 의미적 green washing 방어 명문 누락 | ⭐⭐⭐ CRITICAL | B-B-B3 + B-rec-2 + B-rec-5 + R-S2 | §9.3 Boss 신뢰 경계 절 신규: AdviceRequest untrusted + BossAdvice 텍스트 전용 + Boss ≠ root of trust + summary 종속 금지 + 3중 방어 (결정적 flag + raw diff + ReviewGuard) |
| **BLOCKING-6** | §9.3 R8 답습 | 워커 실패 시 advise 미호출 (R8 답습) 명문 누락 | ⭐⭐ HIGH | B-B-B4 + R-S2 (4) | §9.3 advisory failure handling 직후 "R8 답습: result.is_error 면 BossLLM.advise 호출 0건 (침해된 워커 advisory injection 표면 회피 의무, StubBoss.calls 답습 verify)" |
| **BLOCKING-7** | §9.3 endpoint | OpenAI-compatible /v1/chat/completions endpoint 통일 명문 부재 | ⭐⭐ HIGH | A-B-A4 + C-B-C2 | §9.3 OllamaBoss/LlamaCppBoss 둘 다 OpenAI-호환 통일 채택 명문 + httpx 표준 클라이언트 + Backend 매트릭스 "OpenAI-compatible endpoint 자격" 열 신규 (llama-server ✓ / Ollama ✓ / vLLM ✓) + footer "3 backend 모두 지원 → BossLLM Protocol 내부 = HTTPClient + base_url 만 차이" |
| **BLOCKING-8** | §9.3 failure framing | "fail-closed 정신" framing 부정확. R3 = fail-open (advisory 실패 → 게이트 진행 비차단 + 명시 경고) + R1 합집합 강제 = fail-safe (의미 다름) | ⭐⭐ HIGH | A-B-A5 + B-rec-3 + C-P-2 | §9.3 advisory failure handling = "(R3) fail-open + (R1) 합집합 강제 fail-safe + (B-rec-3) health_check 실패 시 별도 fail-closed 후보 (k) 별도 cycle 결정" 분리 명문. "fail-closed 정신" 단어 삭제 |
| **BLOCKING-9** | §9.3 + §9.4 wall-clock | advisory wall-clock = decode + prefill 모두 포함 의무 명문 추가 (Ollama prefill 격차 ~3.65~3.77× 답습) | ⭐⭐ HIGH | A-B-A10 + B-N4 (R4-body cascade) | §9.4 (j) 진입 자격 절 "advisory wall-clock budget = decode generation + prefill generation 합산 의무, decode-only 정의 부정확 (R4-body M3 매트릭스 4 차원 격차 답습)" |
| **BLOCKING-10** | §9.4 threshold | T1~T6 (~10/~15/~20/~30/동적/다중 tier) 단일 후보 framing | ⭐⭐ HIGH | C-B-C3 + (Morph 2026 evidence) | §9.4 "threshold 후보 매트릭스" 신규 + (j) 별도 cycle 측정 후 결정 *후보* only (본 cycle 내 *고정* 0건 명문) |
| **BLOCKING-11** | §9.3 vLLMBoss | vLLM sm_121 binary-compat 외부 evidence + "MVP-2 재검토 trigger" 열 + "영구 배제 금지 (line 126 답습, C-2 충돌 회피)" 비고 명문 | ⭐⭐ HIGH | A-B-A7 + C-B-C4 + B-rec-1 | §9.3 vLLMBoss "MVP-2 재검토 trigger" 열 신규: "vLLM 공식 sm_121 native support release + DGX Spark binary wheel 제공 + sm_121f SCALED_MM_ARCHS 포함 시" + "영구 배제 금지 line 126 답습" 비고 |
| **BLOCKING-12** | §3.3 + §9.5 verify | src/jarvis/ 변경 0건 verify 의무 명시 추가 (`git diff src/jarvis/boss.py orchestrator.py approval.py tests/jarvis/test_boss_advisory.py = 0`) | ⭐⭐ HIGH | A-B-A8 + R-S1 (8) | §3.3 + §9.5 verify 의무 절에 명문 추가 |
| **BLOCKING-13** | §1.1 R4 행 input | "BossLLM ABC 정의" → "BossLLM Protocol (boss.py 기존 구현) design doc 분리 + Backend 후보 매트릭스 신규" framing 정정 | ⭐⭐ HIGH | A-B-A9 + R-S1 cousin | §1.1 Provider Liquidity 행 "output 자격" 열 정정 |
| **BLOCKING-14** | §9.1 R4 산술 | R4 referent "5 위치" 산술 자기모순 (1 + 3 = 4) | ⭐⭐ HIGH | B-rec-4 + B-N1 + R-S3 | §9.1 line 281 "5 위치" → "4 위치" 정정 또는 5번째 referent 직접 verify 후 명문 |
| **BLOCKING-15** | §9.4 (j) 선결 | Phase 1 N=3 repetitions Ollama 답습 = (j) 진입 *선결* 의무 명시 강화 | ⭐⭐ HIGH | B-N3 + N-A2 + R-S4 | §9.4 "(j) 진입 자격 결론" 강화 + LlamaCppBoss bartowski direct N=3 별도 측정 carry-over MEDIUM 명문 |

**합산 격수**: CRITICAL ⭐⭐⭐ = 5건 / HIGH ⭐⭐ = 10건 / 총 15건. brief v1.1 verbatim 100% 흡수 의무.

---

## 8. 권고 (brief v1.1 일부 흡수 자격, 8건)

| # | 항목 | 출처 | 처리 |
|---|---|---|---|
| REC-1 | model size 단독 분리 cycle 명명 ((m) 후보) | A-P-A1 + C-P-4 | §9.2 footer 흡수 |
| REC-2 | (j) → (k) → (l) chain 의존성 명시 | A-B-A11 | §9.4 footer 흡수 |
| REC-3 | LlamaCppBoss bartowski direct N=3 carry-over MEDIUM 명문 | A-B-A6 + N-A2 | BLOCKING-15 합산 흡수 |
| REC-4 | prefill 입력 상한 후보 (~512/~1024/~2048/~4096) + 요약 (TextRank/LLM/sliding window) | C-P-3 | §9.4 (j) input 강화 절 흡수 |
| REC-5 | LiteLLM + llama-swap 대안 architecture 4 후보 매트릭스 (A/B/C/D) | C-B-C1 (CRITICAL → 권고 강등) | §9.3 footnote 대안 매트릭스 + MVP-1 결정 *후보* only + lock-in 우려 정직성 (Reviewer 강등 이유: 본 cycle = design draft only + (k) carry-over 자격 명문이 이미 충족, MVP-1 결정 *고정* 의무 0건) |
| REC-6 | F2 변수 분리 cycle 우선순위 후보 | C-P-4 | REC-1 합산 |
| REC-7 | sm_121 stability "실동작 보고" trigger | B-rec-1 | BLOCKING-11 합산 |
| REC-8 | src/jarvis/boss/ vs boss.py path 혼동 risk verify | A-N-A5 | BLOCKING-12 합산 (`src/jarvis/boss/` 경로 = 0건, `src/jarvis/boss.py` = 단일 파일) |

---

## 9. NOTE (정직성 명문 자격, 흡수 의무 0건, 7건)

| # | 항목 | 출처 |
|---|---|---|
| NOTE-1 | design draft framing 정정 후 정직성 ((R4-body) 답습 자격) | A-N-A1 |
| NOTE-2 | (j) → (k) → (l) cycle 분리 의무 정직성 | A-N-A3 |
| NOTE-3 | R-15 verify ✓ | A-N-A4 |
| NOTE-4 | OllamaBoss N=3 미수행 carry-over MEDIUM | B-N3 |
| NOTE-5 | password redact 강함 (R-S2 발효 영구) | B-N6 |
| NOTE-6 | 추가 backend 후보 (exllamav2/TabbyAPI/MLX/Triton) LOW carry-over | C-P-1 |
| NOTE-7 | LiteLLM lock-in 우려 정직성 | C-N-7 |

---

## 10. 기각 (반영 0건 + 근거, 3건)

| # | 항목 | 출처 | 기각 근거 |
|---|---|---|---|
| 기각-1 | C-B-C1 LiteLLM/llama-swap = ⭐⭐⭐ CRITICAL 자격 | C-B-C1 | 본 cycle = design draft only + read-only + (k) carry-over 자격 명문 충족. MVP-1 결정 *고정* 자격 0건 ((k) 별도 cycle). 외부 evidence 답습 의무 = 권고 자격 충분. 격수 강등 REC-5 흡수 |
| 기각-2 | C-B-C3 threshold T1~T6 = ⭐⭐ HIGH 단일 채택 | C-B-C3 | 채택 BLOCKING-10 (HIGH 유지) 하되 "단일 후보 only" framing 채택 거부 — 다중 tier 후보 포함 의무 + (j) 별도 cycle 측정 후 결정 *후보* only 명문 |
| 기각-3 | (4-way-X) prime/super-prime 자동 진입 부정 = 추가 흡수 의무 | A-P-A4 + C-N-5 | §0 #15 + §7 #15 + §10 line 371 답습 완전 = 추가 흡수 의무 0건 (D-3 합의) |

---

## 11. 최종 판정 — APPROVE w/ COND

**핵심 근거**:
1. 3 Agent 만장일치 APPROVE w/ COND + Reviewer 직접 verify 후 동의
2. brief v1 = scope 4 차원 모두 포함 + 수단 read-only + 6단계 변형 + chain 영구 종결 의무 답습 충족
3. R-15 self-consistency 영구 (§0 16 ↔ §7 16) 1:1 매핑 verify ✓
4. R-9 본문 정정 0건 의무 + R-S1 line 126 vLLM 보존 + R-S2 password redact 답습 영구 ✓
5. ⭐⭐⭐ Reviewer 직접 verify 핵심: `src/jarvis/boss.py` commit `83aebad` 99줄 = 본 brief §9.3 framing "코드 0" 와 부정합 → brief v1.1 보강 후 framing 정정 의무

**COND = brief v1.1 보강 의무**:
- BLOCKING 15건 verbatim 100% 흡수
- R-S1~R-S4 흡수
- 권고 5건 일부 흡수 (REC-1, REC-2, REC-4, REC-5, REC-7 → BLOCKING/footer 흡수)
- §11 v→v1.1 변경 일람 신규
- NOTE 7건 정직성 명문 자격

---

## 12. 합의 후 brief v1.1 단계 (3) 의무 매트릭스

| 의무 | 건수 | 처리 |
|---|---|---|
| **BLOCKING verbatim 100% 흡수** | **15건** | CRITICAL 5 + HIGH 10, 모든 BLOCKING-N 항목 §위치 명시 + 흡수 방안 직접 반영 |
| **Reviewer 단독 격상 R-S* 흡수** | **4건** | R-S1 (코드 verbatim 인용) + R-S2 (Boss 신뢰 경계 절 신규) + R-S3 (R4 산술 정정) + R-S4 ((j) 선결 강화) |
| **권고 일부 흡수** | **5건** | REC-1 + REC-2 + REC-4 + REC-5 + REC-7 (REC-3/REC-6/REC-8 = 다른 BLOCKING 합산) |
| **NOTE 정직성 명문** | **7건** | 흡수 의무 0, brief footer 정직성 자격 명문 |
| **기각 매트릭스 명문** | **3건** | brief §11 신규 절에 기각 근거 명문 (정직성 의무) |
| **§11 v→v1.1 변경 일람 신규** | 1건 | 답습 패턴 (R4-body brief v1.1 § 답습) |
| **단계 (4) Boss 추상화 design doc framing 변경** | 1건 | `docs/architecture/jarvis-mvp1-boss-abstraction-design.md` = "기존 `src/jarvis/boss.py` 99줄 design doc 추출 + Backend 후보 매트릭스 신규" framing 답습 |
| **§0 #3 + §1.1 R4 행 framing 정정** | 2건 | BLOCKING-1 + BLOCKING-13 합산 |
| **§3.3 + §9.5 cross-check 의무 강화** | 1건 | BLOCKING-12 합산 (`git diff src/jarvis/boss.py orchestrator.py approval.py tests/jarvis/test_boss_advisory.py = 0`) |

---

**합의 종결 권위**: 본 합의 보고서 = 3+1 풀 합의 (Agent A 11 + B 4 + C 4 BLOCKING raw → Reviewer 통합 15 BLOCKING + R-S* 4) APPROVE w/ COND. brief v1.1 보강 단계 (3) 진입 의무 답습. **단계 (3) 진입 = 사용자 명시 후 의무 답습 영구** (chain 영구 종결 + (4-way-X) prime/super-prime 자동 진입 명백 부정 답습 영구).

---

**Reviewer 보고 종결**.

핵심 사실 confirmed:
- `src/jarvis/boss.py` 99줄 = commit `83aebad` (2026-05-22) 로 이미 존재
- 실제 = `@runtime_checkable Protocol` (ABC 아님)
- BossAdvice = `summary / extra_flags / advisory_failed` (confidence 0건)
- AdviceRequest = `prompt / worker_alias / output / deterministic_flags`
- StubBoss.calls + merge_flags (R1 fail-safe) 모두 답습 완료
- brief §9.3 line 308~314 ABC 코드 블록 = 실제와 100% 부정합 → BLOCKING-1~3 + R-S1 핵심 근거

최종 판정: **APPROVE w/ COND** (만장일치 3/3 + Reviewer 동의), BLOCKING 15건 + R-S* 4건 흡수 의무.
