# Jarvis MVP-1 format 가족별 분류 합의 cycle entry brief (v1.1, APPROVE w/ COND 반영)

> **본 brief = Provider Liquidity deep-dive 합의 cycle (`a9e1e88`, BLOCKING 13 + 권고 17 + NOTE 12) 의 권고 R-26 (C-R2) + R-11 답습 후속 cycle entry brief.** v1.1 = 풀 3+1 합의 (`d75dceb`, APPROVE w/ COND, BLOCKING 16 + 권고 21 + NOTE 24, 기각 0, Reviewer 단독 격상 3) verbatim 본문 직접 반영. 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·모델 다운로드·측정 실행·config 변경·M3/M4 결정 *고정*·MVP-1 합의 본문 자동 정정·헌법 본문 자동 정정·ADR-011 amendment 자동 발의·메모리 자동 갱신·Provider Liquidity 본질 약화** 를 발생시키지 않는다. 실 변경 0건. staged: brief v1 (`f305174`, 556줄) → 풀 3+1 합의 (`d75dceb`, 397줄) → **brief v1.1 (본 문서)** → 세션 정리·commit·push. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-24 (Provider Liquidity deep-dive cycle `8ae1ab6` 후속, 본 cycle 합의 `d75dceb` 직후)
**카테고리**: 합의 cycle entry brief v1.1 (format 가족별 분류 cycle, Provider Liquidity 합의 R-26·R-11 답습 후속)
**범위 (사용자 명시 — "(f-K) format 가족별 분류" 선택)**: **4 format 가족 분류 자체의 자격 평가 + 가족 내부/가족 간 Provider Liquidity 충족 자격 분리 가능성 평가** / **진단 + 권고 옵션 매트릭스** (결정 *고정* 0건, 사용자 명시 의무 유지)
**합의 답습** (R-22 의무):
- Provider Liquidity 합의 BLOCKING 13 의 **R-3 (4 수준 framing self-citation + 시간축 missing dimension + 비교 자격 1/4) + R-7 (model loading 5 sub-차원 분해) + R-9 (ADR-011 amendment 자동 발의 자격 0, 헌법급 변경 별도 cycle 의무) + R-10 (binary 본질 spectrum 화 차단) + R-11 (evidence GGUF 가족 한정 명문) + R-12 (cycle-specific framing 영구화 risk) + R-13 (ADR-011 line 6/245 관용 매핑 권위) + R-21 (Reviewer 권한 한계) + R-22 (Phase 3 합의 BLOCKING 7 R-3/R-4/R-5/R-6 패턴 답습 명문) + R-26 (format 가족별 분류) + R-29 (de facto 압력 차단) + R-30 (기각 자격 명시)** 답습 의무
- Phase 3 합의 BLOCKING 7 의 **R-3 (window bias) + R-4 (분기점 라벨 anchor effect) + R-5 (framing 약화 + 단정 표현 제거) + R-6 (PASS/FAIL framing 금지)** 답습 패턴 유지
- 본 cycle 합의 (`d75dceb`) BLOCKING 16 본문 직접 반영 100% (R-21 답습)

**선행 답습**:
- `docs/phase0/jarvis-mvp1-provider-liquidity-deepdive-consensus-entry-brief.md` v1 (`9ed376a`, 407줄, brief v1.1 progression 추적 자격, **R-20 답습**)
- `docs/phase0/jarvis-mvp1-provider-liquidity-deepdive-consensus-entry-brief.md` v1.1 (`8ae1ab6`, 518줄) — 본 cycle 의 *직접* 진입 근거
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-provider-liquidity-deepdive.md` (Provider Liquidity 합의, `a9e1e88`, BLOCKING 13 + 권고 17 + NOTE 12)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-format-family-classification.md` (본 cycle 합의 보고서, `d75dceb`, 397줄, BLOCKING 16 + 권고 21 + NOTE 24)
- `docs/phase0/jarvis-mvp1-local-boss-design-brief.md` (MVP-1 design v2, `15beb33`, C-2 + R4 + M3)
- `docs/review/3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md` (MVP-1 합의, R4 llama.cpp ↔ Ollama 동급)
- `docs/phase0/jarvis-mvp1-v1-poc-phase3-entry-brief.md` (Phase 3 entry v1.1, `25eb008`)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-v1-poc-phase3-entry.md` (Phase 3 합의 BLOCKING 7)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-36-phase3-summary.json` (Phase 3 실 빌드 cycle summary)
- `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log` (GGUF format 호환성 차단 raw, **R-S1 격상 evidence**)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (§2.1 means/ends 일반 원칙 + **line 6 + line 212 + line 245 verbatim 권위 매핑 (R-13 + R-10 = R-S2 통합 답습)**)
- `docs/constitution/PROJECT_CONSTITUTION.md` (제5조 line 40~46 + 제8-2조 line 67~73)
- 메모리: `feedback_provider_liquidity` (line 7 binary 본질 + **line 11~17 적용 가이드 6 항목**, R-13 답습 의무, 19일+ stale system reminder verify) / `project_jarvis_local_boss_direction` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것

1. Provider Liquidity 합의 R-26 답습 — 4 format 가족 분류 자체의 자격 평가 (§2)
2. **각 가족 내부 호환성 자격 (runtime 간 format 호환성)** vs **가족 간 호환성 자격 (format 변환 의무 강도)** 분리 가능성 평가 (§4)
3. **Provider Liquidity 충족 자격이 가족 내부 vs 가족 간 분리 가능한가** 의 자격 평가 (R-11 답습 응용)
4. MVP-1 R4 "동급" 진술의 가족 한정 자격 (R-3 + R-11 + R-7 답습)
5. SDD 정합성 매트릭스 — 헌법 5조 + ADR-011 line 6/212/245 관용 매핑 권위 + 내부 비대칭 답습 (R-13 + **R-10 = R-S2 통합**) + MVP-1 합의 R4 + 메모리 (§3)
6. 핵심 긴장 **6축** 분석 (§4) — (1) 가족 내부 호환성 / (2) 가족 간 호환성 / (3) Provider Liquidity 분리 자격 / (4) 시간축 (Provider Liquidity 합의 R-3 답습) / (5) **본 framing 임시성 명문** (R-3 + R-12 답습) / (6) **abstraction layer 교차 자격** (R-7 신규 = C-B2 + C-S2 통합)
7. 3+1 합의 분담안 — Agent A/B/C 관점·핵심 질문·출력 형식 (§5)
8. 합의 출력 형식 명문 + raw json/log line-level cross-check 의무 (§6)
9. 후속 결정 권고 옵션 매트릭스 (§7) — **권고 자격 only, 결정 *고정* 0**. 4 가족 분류 자체의 영구 framing 자격 0 (R-12 답습 — (D3)/(D4) 분기 패턴 답습)
10. 정직성 한계 (§8) — 16+ 항목
11. 차단 조건 (§9) — **12 항목 1:1 매핑 (R-15 = R-S3 답습 self-consistency 정합화)**
12. NOTE carry-over (§10) — Provider Liquidity 합의 NOTE 12 + 본 cycle 신규 12 = 24 항목
13. **변경 일람 표 (§11)** v1 → v1.1 신규 (Provider Liquidity brief v1.1 §11 패턴 답습)

### 하지 않는 것 (영구 답습, R-29 + R-30 명문 답습)

> **🔴 R-15 (R-S3) 답습 강한 변형**: 본 §0 12 항목과 §9.1 차단 조건 12 항목은 **1:1 매핑 의무** (brief self-consistency 정직성 답습). 본 cycle 합의 결과 (`d75dceb`) R-S3 격상 BLOCKING 답습.

1. ❌ **4 가족 분류 자체의 결정 *고정*** — 본 cycle = 분류 자격 *평가* only, 분류 채택·기각·확장 = 합의 *후* 사용자 명시 의무
2. ❌ **MVP-1 합의 본문 (`3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss.md`) 자동 정정** — R4·C-2 진술의 검증 자격 평가 *입력* 자격만, 본문 수정은 합의 *후* 별도 cycle (R-21 답습)
3. ❌ **헌법 본문 자동 정정** — 5조·8-2조·ADR-011 line 6/212/245 권위 답습 명문만, 헌법 amendment 는 별도 단계
4. ❌ **ADR-011 amendment 자동 발의** — §2.1 적용 자격 평가만, amendment 발의 = 본 cycle 명시 권고 *후* 사용자 명시 승인 *후* 별도 합의 cycle (R-9 헌법급 변경 답습)
5. ❌ **M3 (추론 런타임) / M4 (tok/s threshold) 결정 *고정*** — Phase 1+2+3 evidence 정직성 한계 답습
6. ❌ **OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss·기타 runtime backend 코드 작성** — 본 cycle = framing 합의 입력 deep-dive
7. ❌ **새 측정 실행 / 새 빌드 / 새 모델 다운로드 / 새 runtime 설치** — 본 cycle 시작 evidence = Phase 3 cycle + Provider Liquidity 합의 + brief 외부 식별 추정 (라이브 verify 0)
8. ❌ **메모리 `feedback_provider_liquidity` 본문 자동 정정** — 본 cycle 합의 결과가 메모리 갱신 자격을 가질 수 있으나, 자동 갱신 0건
9. ❌ **Provider Liquidity 자체 약화** — 5 영구 핵심 제약 답습. binary 본질 (락인 0) 유지, spectrum 화는 framing 도구 한정 (Provider Liquidity 합의 R-10 답습) — **본 brief §4.3 (α) "가족 내부 한정" 채택 자격 = 헌법급 trigger** (R-4 답습)
10. ❌ **본 4 가족 분류의 영구 framing 정착** (R-12 답습) — cycle-specific framing 영구화 risk 차단. 4 가족 분류 + 6축 framing = brief v1.1 의 *임시 framing* 명문 (R-2 + R-3 답습). (α)(β)(γ)(δ) 분리 후보의 어느 후보도 영구 정착 자격 0
11. ❌ **본 brief 의 진단표 (§3·§4) 가 후속 cycle 의 정정 *진입 근거* 가 되는 *de facto* 압력 발생** (R-29 답습)
12. ❌ **본 cycle 합의 결과의 *기각* 자격도 자동 발효 0건** (R-30 답습)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — Provider Liquidity deep-dive 합의 R-26 (C-R2)

Provider Liquidity 합의 보고서 (`a9e1e88`) line 207 verbatim:

> **R-26 (C-R2)** brief v1.1 §7.3 옵션 (K) 에 **format 가족별 분류** 추가 — (a) GGUF 가족 (Ollama / llama.cpp / llamafile / ktransformers 부분) / (b) HF/safetensors 가족 (vLLM / SGLang / Aphrodite) / (c) compiled-engine 가족 (TensorRT-LLM / MLC-LLM) / (d) 자체 format 가족 (exllamav2 EXL2 / mlc-llm TVM)

본 cycle = R-26 의 **별도 brief 자격** (Provider Liquidity brief v1.1 §7.3 표 자체가 "별도 brief" 컬럼 명시) 답습.

### 1.2 trigger — Provider Liquidity 합의 R-11 (C-B4 + C-S2)

Provider Liquidity 합의 보고서 (`a9e1e88`) line 159~163 verbatim:

> **R-11** — brief evidence 가 *모두 GGUF 가족 내부* 한정 명문 (C-B4 + C-S2 통합)
> **근거**: brief §2.1~§2.4 evidence 가 *모두 GGUF 가족 내부* (Ollama 0.20.4·llama.cpp `c0c7e147`) 한정. 다른 format 가족 (HF/safetensors·TensorRT-engine·EXL2·MLC-TVM) 의 동급 평가에 *입력 자격 X*. 가족 간 비교 자격 본 cycle 미평가.
> **처리**: brief v1.1 §2.5 또는 §10 NOTE 표에 "본 cycle evidence = GGUF 가족 내부 한정 (Ollama·llama.cpp). 다른 format 가족 (HF/safetensors / compiled-engine / 자체 format) 의 동급 평가 입력 자격 0, 별도 cycle 의무" 명문 추가.

본 cycle = R-11 의 "별도 cycle" 답습 (Provider Liquidity brief v1.1 §10 NOTE 9 본문 carry-over).

### 1.3 본 cycle 의 핵심 질문

**Q1**: 4 가족 분류 (GGUF / HF-safetensors / compiled-engine / 자체) 가 **정확한가 + 완정한가**?
- 누락 후보 (Apple MLX / NVIDIA NIM / OpenAI-compatible Cloud API / RWKV·MAMBA 자체 format / AWQ·GPTQ·SmoothQuant 등) 자격
- 중첩 후보 (llamafile = GGUF + 실행 바이너리 = 가족 내부 vs 새 차원) 자격
- 분류 기준 (file extension / loader 구현 path / serialization 방식 / 양자화 호환성) 의 정합성

> **🔴 R-1 답습 (본 cycle BLOCKING 통합)**: 본 §2.3 4 가족 분류의 1차 기준 = **serialization 방식 + 동일 loader 코드 경로** 의 교집합 (합의 Reviewer 통합 권고). 단 (i) format extension / (ii) 양자화 format / (iii) deployment 형태 / (iv) HW target 은 *직교 축* 으로 본 분류와 독립. 본 채택 기준 자체의 영구 framing 정착 자격 0 (R-12 답습), 합의 결과 후 별도 cycle 재평가 자격. ktransformers "부분" 라벨 = fuzzy membership 명문, 다른 (b)/(c)/(d) 가족도 동일 fuzzy 자격 평가 의무.

**Q2**: 가족 내부 호환성과 가족 간 호환성이 **분리 가능한 자격** 인가?
- 가족 내부 = runtime 간 format 호환성 후보 ↑ (예: Ollama·llama.cpp 동일 GGUF 사용)
- 가족 간 = format 변환 의무 ↑ (예: GGUF ↔ HF-safetensors = `convert_hf_to_gguf.py` 의무)
- Phase 3 P3-F1 finding (Ollama `30e51a7c` ≠ llama.cpp `c0c7e147`) 는 **가족 내부에서도 시점 의존 호환성 부재** 발견 — 분리의 *순수 binary* 자격에 균열

**Q3**: Provider Liquidity 충족 자격이 *가족 내부* vs *가족 간* **분리 가능한가**?
- 가족 내부 충족 = "GGUF 가족 안에서 모델/runtime 교체가 코드 변경 없이 가능"
- 가족 간 충족 = "다른 format 가족으로 교체 시에도 코드 변경 없이 가능 (= conversion script 가 *수단*, ends 는 동일)"
- ADR-011 §2.1 means/ends 적용: 변환 script = means, 호환성 보장 = ends. case A (means 보전) / case B (ends 보전) / **case C (means+ends 양면, Provider Liquidity 합의 R-4 신규)** / **case D (means ≡ ends 일부, 분리 불가, R-30 신규 carry-over)** 적용 자격

**Q4**: MVP-1 R4 "동급" 진술의 가족 한정 자격은?
- R4 line 63 = "llama.cpp ↔ Ollama 동급" = **GGUF 가족 내부 한정** (양쪽 GGUF runtime) — R-11 답습
- 가족 간 "동급" (예: Ollama ↔ vLLM) = R4 진술 자격 0 (별도 합의 의무)
- **R-6 답습 (본 cycle BLOCKING 통합)**: 본 자격 = *해석 명확화* only, **MVP-1 합의 본문 정정 자격 0** (R-21 답습). brief v1 §3.2 표 → 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0 (R-29 답습)

### 1.4 헌법 본문 매핑 — **R-13 + R-10 = R-S2 통합 답습** (ADR-011 line 6 + line 212 + line 245 verbatim)

> **🔴 R-10 답습 (R-S2 격상)**: Provider Liquidity 합의 R-13 의 line 6/245 답습 + 본 cycle Reviewer 단독 추가 line 212 답습 통합 의무.

Provider Liquidity 합의 R-13 (Reviewer 단독 BLOCKING) verbatim 답습:

**ADR-011 line 6 verbatim** (상위 권위 명시):
> **상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), `docs/architecture/system-identity-prequel.md` §3

**ADR-011 line 212 verbatim** (R-S2 격상 — ADR-011 *내부* 비대칭 명문):
> | Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |

**ADR-011 line 245 verbatim** (관련 문서 §8.1 상위 권위):
> `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 **관용** (Provider Liquidity, 비협상)

**해석 통합** (R-10 답습 본질):
- line 6 + line 245 = ADR-011 *권위 위계 의존* (양립) — Provider Liquidity = ADR-011 의 상위 권위
- line 212 = ADR-011 *주제 범위 한정* (redaction 수단 본질 충족 한정) — ADR-011 *주제* 가 Provider Liquidity 와 무관
- 본 cycle 평가 자격 = **두 차원 모두 답습 의무**. **ADR-011 *내부* line 212 본문 정정 자격 0** (R-9 헌법급 변경 답습)

본 cycle 매핑:
- 헌법 제5조 (관용 매핑, Provider Liquidity 비협상) — 본 cycle 의 *상위 권위* 답습
- 헌법 제5조 코드 품질 본문 (line 40~46): SRP·중복 제거·외부 입력 검증·**내부 코드 신뢰**·린터 (**R-17 답습 — 5조 본문 절단 차단**)

**헌법 제5조 line 40~46 verbatim** (R-17 답습):
> - 코드는 읽기 쉬워야 한다
> - SRP (Single Responsibility Principle)
> - 중복 제거
> - 외부 입력만 검증한다. **내부 코드는 신뢰**한다
> - 린터/포매터 자동

- 헌법 제8-2조 (하드코딩 제로) — 모델명·runtime 명·format 명·conversion script path 모두 환경 변수·config 의무
- ADR-011 §2.1 (a)~(d) 4조건 + (e) 후속 패턴 — 변환 script (means) 와 호환성 보장 (ends) 양면 case C / case D 적용
- **본 cycle 의 권위 한계**: 4 가족 분류 자체의 채택·기각·확장 자격 0 (R-12 답습)

**진단 의무 enum (R-16 답습, Provider Liquidity 합의 R-19 답습 보강)**:
1. ADR-011 line 6/212/245 관용 매핑 + 내부 비대칭 답습
2. MVP-1 R4 진술의 가족 한정 자격 평가 (R-6 답습)
3. format 가족 vs 다른 가족 means/ends 분류 + case C/D 분기 (R-30 답습)
4. ADR-011 §2.1 (a)~(d) 적용 자격 + (e) 후속 패턴 (R-5 답습)
5. 4 가족 분류 framing 자체 평가 (R-3 답습)

### 1.5 ADR-011 §2.1 적용 자격 — **R-5 = R-S2 = R-14 답습 (a)~(d) 본문 vs (e) 후속 패턴 분리**

**ADR-011 line 52~59 verbatim** (R-18 답습 — 본문 직접 인용):
> 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:
> | # | 조건 | 검증 방식 |
> |---|------|---------|
> | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
> | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
> | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
> | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

→ **ADR-011 §2.1 본문 = (a)~(d) 4조건 only. (e) 없음**. **(e) = ADR-011 §2.1 *본문 외* 후속 패턴 모법 인용** (CLAUDE.md line 223 + `implementation-runtime-roadmap.md` 등 정착, R-S2 = R-14 답습).

본 cycle 적용:
- **(a) 비교표 명문**: 본 cycle = 4 가족 × Provider Liquidity 자격 4 항목 비교표 *시도*. 단 Phase 3 evidence GGUF 가족 한정 (R-11) → 비교 자격 = 4 × 4 = 16 cell 중 GGUF 한정 충족 cell ≤ 4 개 (sub-차원 (1) tensor naming 한정)
- **(b) 적대적 시연**: 가족 간 conversion 미수행 시 "동급" 진술의 침투 시연 추상 패턴 동형 자격 평가
- **(c) BI 위반 자격**: 4 가족 중 일부의 runtime/format/loader 가 BI-3 (agent ≠ root) 격리 자격 부재 가능성 — 별도 cycle
- **(d) 비례 평가**: 4 가족 모두 동등 평가 비용 vs 비례 우선순위 (GGUF 가족 = 본 환경 우선)
- **(e) 후속 패턴** (R-S2 답습 — ADR-011 §2.1 *본문 외* 후속 패턴 모법 인용): Provider Liquidity 합의 BLOCKING 13 + 본 cycle 합의 BLOCKING 16 본문 반영 의무 (R-21 답습) — brief v1.1 보강 시점 자동 반영 자격, 본문 수정 자격 0

---

## 2. evidence 통합 (Phase 3 raw + Provider Liquidity 합의 + 외부 식별)

### 2.1 Phase 3 cycle evidence (GGUF 가족 내부 한정, R-11 답습)

**P3-F1 — GGUF format 호환성 부재 (Ollama `30e51a7c` ≠ llama.cpp `c0c7e147`)**

raw: `docs/phase0/v1-poc-raw/phase3/2026-05-24T04-32-phase3-measure-attempt-blocked.log`

**raw line 25~32 결론 verbatim** (R-S1 격상 = R-8 답습 본질 evidence):
> conversion/qwen.py:299-300:
>   elif name.endswith(".dt_bias"):
>       name = name.rpartition(".dt_bias")[0] + ".dt_proj.bias"
>   - 새 conversion 은 .dt_bias → .dt_proj.bias 로 rename
>
> 결론: Ollama 가 다운로드한 GGUF = 더 오래된 conversion 으로 생성 (ssm_dt.bias 미저장)
>       llama.cpp c0c7e147 (master) = 최근 코드에서 .bias 강제 required 변경
>       Phase 3 (iii) 직접 측정 = GGUF format 호환성 차이로 차단

- Ollama 보유 GGUF (`sha256-30e51a7c`, 오래된 conversion): `blk.X.ssm_dt` only
- llama.cpp `c0c7e147` master 요구: `blk.X.ssm_dt.bias` (flag=0 required)
- llama.cpp `convert_hf_to_gguf.py:299-300` 새 형식 `.dt_bias` → `.dt_proj.bias` rename
- llama.cpp `qwen3next.cpp:87` `.bias` flag=0 required 강제

**P3-F1 evidence 일반화 자격 한정 *추가 layer* (R-8 = R-S1 답습)**:
- GGUF 가족 한정 (R-11 답습) + sub-차원 (1) tensor naming convention 한정 (R-7 답습) + **conversion script lineage 시점 부정합 한정** (Ollama 보유 `30e51a7c` blob = 더 오래된 conversion vs llama.cpp `c0c7e147` master = 최근 `.dt_proj.bias` rename, `conversion/qwen.py:299-300`)
- 본 evidence = **GGUF 가족 *본질* 부정이 아닌, *시점 부정합* finding**
- 가족 본질 부정 자격 평가 = (a) 다른 conversion lineage GGUF 측정 (옵션 G 답습) + (b) 다른 sub-차원 (2)~(5) 측정 + (c) 다른 시점 측정 — **3 차원 모두 충족 후 가족 본질 평가 자격 도래**

**P3-F2~F7 carry-over** (Provider Liquidity brief v1.1 §2.1~§2.4 답습):
- F2: sm_120a+sm_121a SASS 모두 포함 (가설 #6 약화)
- F3: R-1 anchor 8회 일치 (silent 교체 미발생)
- F4: Phase 1 prompt 정확 detokenize
- F5: Ollama API FROM 경로 부정확
- F6: docker-proxy 11434 listening (Ollama Docker wrapper 가능성)
- F7: OLLAMA_KEEP_ALIVE=-1

### 2.2 Provider Liquidity 합의 본문 (`a9e1e88`) carry-over 핵심

**합의 BLOCKING 13 + 권고 17 + NOTE 12** (기각 0):

| 항목 | 본 cycle 답습 의무 |
|---|---|
| R-3 (4 수준 framing self-citation + 시간축 + 비교 자격 1/4) | 본 brief framing 임시성 명문 §4.5 + 시간축 5번째 축 + **R-2 (B-B4 + C-S4 통합) self-citation 후속 매핑** |
| R-7 (model loading 5 sub-차원 분해) | §2.1 P3-F1 = sub-차원 (1) 한정 명문 + R-8 conversion lineage 시점 부정합 한정 추가 layer |
| R-11 (evidence GGUF 가족 한정) | **본 cycle 의 직접 진입 근거** — §1.2 |
| R-12 (cycle-specific framing 영구화 risk) | §0 + §7 (D3)(D4) 분기 답습 + R-15 차단 12 항목 |
| R-13 (ADR-011 line 6/245 관용 매핑) | §1.4 + §3 권위 매핑 + **R-10 = R-S2 추가 line 212 답습** |
| R-21 (Reviewer 권한 한계) | §6 + §5.3 Reviewer 권한 한계 7 항목 boundary 강화 (R-14 답습) |
| R-26 (format 가족별 분류) | **본 cycle 의 직접 진입 근거** — §1.1 |
| R-29 (de facto 압력 차단) | §0 + §9 차단 |
| R-30 (기각 자격 명시) | §0 + §7.4 |

### 2.3 4 가족 외부 식별 (추정 한정, 라이브 verify 0건)

**자격 한계 명문**: 본 §2.3 은 *외부 식별 추정* 만, 각 runtime/format 의 라이브 verify (download/install/test) = 본 cycle 자체 진행 0 (§0 답습). 외부 정보 출처 = LLM 사전 지식 + 공식 repo 추정. **각 runtime 의 실제 버전·실제 format spec·실제 호환성 = 별도 cycle 의 라이브 verify 의무**.

> **🔴 R-1 답습 (분류 기준 명시)**: 본 4 가족 분류의 1차 기준 = **serialization 방식 + 동일 loader 코드 경로** 의 교집합. 단 (i) format extension / (ii) 양자화 format / (iii) deployment 형태 / (iv) HW target 은 *직교 축* 으로 본 분류와 독립. 본 채택 기준 자체의 영구 framing 정착 자격 0 (R-12 답습), 합의 결과 후 별도 cycle 재평가 자격.

> **🔴 R-27 답습 (각 runtime 내부 conversion script lineage 부재 명문)**: 각 가족 (a)~(d) 의 4 column (runtime / format / 비고) 의 *각 runtime 내부 conversion script lineage / 자체 fork 자격* = 외부 식별 0, 라이브 verify 0. 별도 cycle 의무 (옵션 G·I·K 답습).

#### (a) GGUF 가족

| runtime | format | 비고 |
|---|---|---|
| **Ollama** (v0.20.4 확인, Phase 1 R-1) | GGUF (자체 conversion) | Phase 3 evidence — 오래된 conversion 답습 |
| **llama.cpp** (`c0c7e147` 확인, Phase 3 R-2) | GGUF | Phase 3 evidence — 최신 conversion 요구 |
| **llamafile** | GGUF + 실행 바이너리 | Mozilla Builders, single-file deploy 모델 |
| **ktransformers** (부분, **fuzzy membership** — R-1 답습) | GGUF + 자체 quant | MoE 최적화 specialized, GGUF 부분 호환. fuzzy 명문 = 다른 (b)/(c)/(d) 가족도 동일 fuzzy 자격 평가 의무 |

**가족 내부 호환성 추정**: 동일 GGUF spec 버전 한정, conversion script 동일 시점 한정 호환. Phase 3 evidence = **시점 의존 호환성 부재** 입증 (R-3 시간축 답습) — 본질 부정이 아닌 시점 부정합 (R-8 = R-S1 답습).

#### (b) HF-safetensors 가족 (fuzzy 자격 평가 의무 — R-1 답습)

| runtime | format | 비고 |
|---|---|---|
| **vLLM** | HF-safetensors + paged attention | MVP-1 합의 R4 "MVP-1 비채택, MVP-2 재검토" (sm_120/121 binary-compat issue #36821, 0.17 해소 흐름) |
| **SGLang** | HF-safetensors + RadixAttention | 별도 runtime |
| **Aphrodite Engine** | HF-safetensors (vLLM fork) | community fork |

**가족 내부 호환성 추정**: HuggingFace safetensors spec 동일 시 호환. config.json + tokenizer.json 동반 의무.

#### (c) compiled-engine 가족 (fuzzy 자격 평가 의무 — R-1 답습)

| runtime | format | 비고 |
|---|---|---|
| **TensorRT-LLM** | `.engine` (TensorRT 컴파일 결과) | NVIDIA, GPU 특정 SM 의존 컴파일 |
| **MLC-LLM** | `.so` / TVM compiled | Apache TVM 기반, GPU/CPU/모바일 다양 target |

**가족 내부 호환성 추정**: **컴파일 시점·target HW 의존성 극강** — 가족 내부에서도 동일 GPU·동일 compiler 버전 한정. Provider Liquidity 충족 자격 *최약*.

#### (d) 자체 format 가족 (fuzzy 자격 평가 의무 — R-1 답습)

| runtime | format | 비고 |
|---|---|---|
| **exllamav2** | EXL2 (자체 quant format) | GPTQ 후속, group-wise quant |
| **MLC-LLM TVM** (c 와 일부 중첩) | TVM IR compiled | runtime 통합되어 있음 |

**가족 내부 호환성 추정**: 각 runtime 의 자체 format 한정, 가족 *내부* 자체가 단일 runtime 일 가능성 (Q-C1 ⭐ — 가족 정의 자격).

#### 누락 후보 (사전 식별, Q-C1 답습)

| 후보 | 4 가족 관계 (R-33 답습) | 양자화 직교 (R-28 답습) |
|---|---|---|
| **Apple MLX** | (e) 신규 가족 후보 또는 (d) 내부 확장 | - |
| **NVIDIA NIM** | 직교 축 (deployment 추상화) 또는 (e) 신규 가족 | - |
| **OpenAI-compatible Cloud API** | **직교 축** (endpoint 추상화, R-7 = §4.6 답습) | - |
| **RWKV / MAMBA 자체 format** | 직교 축 (architecture 분류) 또는 (d) 확장 | - |
| **AWQ / GPTQ / SmoothQuant** | **4 가족과 직교 축** (양자화, cross-runtime 부분 호환). Q4_K_M = GGUF 한정 / EXL2 = exllamav2 한정 / AWQ·GPTQ = cross-가족 | 옵션 (L) 별도 cycle 답습 |

#### Agent C 추가 누락 후보 (외부 식별 추정 한정, 라이브 verify 0, R-31 답습)

| 후보 | 추정 분류 |
|---|---|
| **PowerInfer / DeepSparse** | sparse activation 최적화 — GGUF 가족 sub-차원 or 새 카테고리 |
| **CTranslate2** (Helsinki-NLP·OpenNMT 후속) | Transformer 자체 컴파일 — compiled-engine 가족 sub-차원 |
| **PETals / Hivemind distributed** | 분산 추론 — 4 가족 *교차 축* (compute distribution layer) |
| **Triton Inference Server** (NVIDIA) | multi-framework backend — 4 가족 직교 (aggregator) |
| **NVIDIA TensorRT-Model-Optimizer** | 양자화 framework — β' framing sub-차원 |

#### 중첩 후보 처리 (사전 식별, Q-C2 답습 — R-12 답습 처리 표)

| 중첩 후보 | 중첩 차원 | 처리 5 자격 | 본 cycle 평가 자격 |
|---|---|---|---|
| **llamafile** | (a) GGUF + γ' 배포 framing single-binary | (1) (a) sub-차원 / (2) 새 가족 / (3) 폐기 / (4) γ' 흡수 / (5) DEFER | (1) 강한 후보 (loader = llama.cpp 본문), 채택 자격 0 (R-12) |
| **MLC-LLM** | (c) compiled-engine + (d) 자체 format + ε' HW target 다중 | (1) (c)+(d) 동시 / (2) 새 가족 (compiled-multi-target) / (3) 폐기 / (4) ε' 흡수 / (5) DEFER | R-1 답습 — 분류 기준 모호성 evidence, (5) DEFER 강한 후보 |
| **OpenAI-compat** | 4 가족 직교 abstraction layer | (1) 동시 적용 (4 가족 × abstraction) / (2) 새 가족 X (직교 축) / (3) 폐기 / (4) δ' aggregator framing 흡수 / (5) DEFER | R-7 = §4.6 답습 — 직교 강한 후보, 라이브 verify 0 |

표 머리: **중첩 후보 처리 = 본 cycle 합의 input 한정, 채택·기각 자격 0** (R-12 + R-29 답습).

---

## 3. SDD 정합성 매트릭스

### 3.1 헌법·ADR-011 권위 매핑 정합성

| 권위 | 본 cycle 자격 |
|---|---|
| **헌법 제5조 (관용 매핑, Provider Liquidity, 비협상)** (ADR-011 line 245 verbatim) | 본 cycle 상위 권위, 본질 약화 자격 0 (R-10 답습) |
| **헌법 제5조 코드 품질 본문** (line 40~46: SRP·중복 제거·**내부 코드 신뢰**·린터, R-17 답습 verbatim 인용) | 4 가족 분류의 코드 영향 = 별도 cycle |
| **헌법 제8-2조 하드코딩 제로** (line 67~73) | 모델명·runtime 명·format 명·conversion script path 모두 환경 변수 의무 |
| **ADR-011 line 6 verbatim** (상위 권위 매핑: 헌법 제5조 Provider Liquidity) | R-13 답습 — 권위 위계 의존 명문 |
| **ADR-011 line 212 verbatim** (Provider Liquidity 영향 무관 — 주제 범위 한정) | **R-10 = R-S2 답습 — ADR-011 *내부* 비대칭 명문**. ADR-011 *주제* (redaction) Provider Liquidity 무관, 권위 위계는 양립. ADR-011 §6 본문 정정 자격 0 |
| **ADR-011 line 245 verbatim** (관련 문서 §8.1 상위 권위) | R-13 답습 — 관용 매핑 권위 정착 명문 |
| **ADR-011 §2.1 (a)~(d) 4조건** (line 52~59 verbatim) + (e) 후속 패턴 | R-5 답습 — (a)~(d) 본문 + (e) 모법 인용 분리 명문 |
| **ADR-011 §6 본문** | 자동 정정 자격 0 (R-21 답습) |

### 3.2 MVP-1 R4 진술 검증 자격 (R-3 + R-7 + R-11 답습)

**MVP-1 합의 line 63 R4 verbatim 행 전체** (R-22 답습 — 행 출처·등급 컬럼 포함):
> | **R4** | M3 런타임 재조정 — **llama.cpp ↔ Ollama 동급**(MoE 실측 llama.cpp ~31 tok/s, Ollama MoE 미공개), V-1에서 둘 다 MoE 측정. **vLLM "제외(#36821)" → "MVP-1 비채택, MVP-2 재검토"**(sm_120/121 binary-compat·0.17 해소 흐름; 영구배제는 C-2 충돌) | C | 🔴 정합 |

**4 수준 + 시간축 비교 자격 (가족 한정 분리)** — Provider Liquidity 합의 R-3 + R-11 답습:

| 수준 | GGUF 가족 내부 (llama.cpp ↔ Ollama) | 가족 간 (Ollama ↔ vLLM 등) |
|---|---|---|
| 인터페이스 (`/v1/chat/completions`) | P1-F2/F4: 양쪽 endpoint 보유 (강한 후보) | 가족 간 endpoint 호환 자격 — vLLM·SGLang 도 OpenAI-compatible 추정 (라이브 verify 0) |
| model loading sub-차원 (1) tensor naming | P3-F1: **시점 부정합** (R-8 = R-S1 답습 — 본질 부정 아님, conversion script lineage + 시점 부정합 한정) | 가족 간 = format 자체 다름 (HF ↔ GGUF), conversion script 의무 (means 차원) |
| 성능 (tok/s) | Phase 1 Ollama 측정 7.83, llama.cpp 측정 0 (차단) | 가족 간 = 가족 내부 측정 부재 시 자격 0 |
| 운영성 | Ollama 측정 (Stage 1+2+3+4 + Phase 1+1.5), llama.cpp 측정 0 | 가족 간 = 양쪽 측정 부재 |
| **시간축** (R-3 답습) | 변환·빌드 시점 의존 (Ollama `30e51a7c` vs llama.cpp `c0c7e147`) | 가족 간 = 시점 의존 + 가족별 발전 cadence 의존 |

**Q4 자격**: R4 "동급" 진술의 가족 한정 자격 = **GGUF 가족 내부 한정**. 가족 간 동급 진술 자격 0 (별도 합의 의무 — R-21 답습).

> **🔴 R-6 답습 (해석 명확화 boundary 명문)**: 본 §3.2 표 = (1) R4 진술의 *적용 범위* 평가 only, (2) MVP-1 합의 본문 정정 자격 0 (R-21 답습 — 별도 cycle 의무), (3) 본 표 자체가 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0 (R-29 답습). (a) 해석 명확화 = 본 cycle 합의 산출 자격 / (b) 본문 정정 = 별도 합의 cycle 의무 + 사용자 명시 + Reviewer 권한 한계 R-21 (3) 답습.

### 3.3 ADR-011 §2.1 답습 자격 — R-5 답습 (a)~(d) 본문 vs (e) 후속 패턴 분리

| 조건 | 출처 | GGUF 가족 내부 | 가족 간 |
|---|---|---|---|
| **(a) 비교표** | ADR-011 line 52~59 본문 | sub-차원 (1) tensor naming 강한 (시점 부정합 R-8), sub-차원 (2)~(5) 미측정 | 가족 간 비교 cell ≥ 4 × 4 = 16, 충족 cell **0건** (외부 식별 추정만, 라이브 verify 0) |
| **(b) 적대적 시연** | ADR-011 line 52~59 본문 | P3-F1 = 침투 시연 (시점 차이만으로 차단) | 가족 간 conversion 부재 시 100% 차단 침투 시연 추상 패턴 동형 자격 |
| **(c) BI 위반** | ADR-011 line 52~59 본문 | runtime 격리 자격 별도 cycle | 가족별 runtime 격리 자격 별도 cycle |
| **(d) 비례 평가** | ADR-011 line 52~59 본문 | 본 환경 (GB10) = GGUF 가족 우선 (vLLM #36821 binary-compat issue) | 다른 환경 (x86_64 datacenter) = HF-safetensors·compiled-engine 비례 우선 가능 |
| **(e) 후속 패턴** | **ADR-011 §2.1 *본문 외* 후속 패턴 모법 인용 (CLAUDE.md line 223 + roadmap.md 등 정착, R-19 답습)** | Phase 3 합의 BLOCKING 7 + Provider Liquidity 합의 BLOCKING 13 본문 반영 의무 (R-21 답습) | 본 cycle 합의 결과 BLOCKING 16 본문 반영 의무 (자동) |

### 3.4 메모리 본문 정확성 (R-13 답습 — line 11~17 적용 가이드 6 항목 추가)

**메모리 `feedback_provider_liquidity` 본문 line 7 verbatim** (R-35 답습 line offset 명시):
> 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 **코드 변경 없이** 가능해야 한다.

🔴 **메모리 19일+ stale 명문** (Provider Liquidity 합의 R-20 답습) — 본 cycle 본문 인용 자격은 (1) 본 cycle 답습 의무 / (2) 신규 cycle 진입 시 메모리 재verify 의무.

**메모리 `feedback_provider_liquidity` 본문 line 11~17 적용 가이드 6 항목 verbatim** (R-13 답습 — B-B5 격상):
- line 11: LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만
- line 12: 어떤 도구든 도입 시 "교체 비용"을 명시적으로 평가, `if model == "claude-opus-4-7"` 패턴 절대 금지
- line 13: **단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙**
- line 14: OAuth 구독을 코어 의존성으로 만들지 않기
- line 15: depcruise 또는 동등한 정적 검사로 분기 코드 패턴 강제 차단
- line 16: 검토 대상: provider 어댑터, 응답 후처리, 메모리 저장 포맷, 토큰 갱신 로직, 다운스트림 파서
- line 17: ...

본 cycle 평가: "교체가 코드 변경 없이 가능" 진술의 *범위 한정* 자격 = (a) 가족 내부 한정 / (b) 가족 간 포괄 — 본질은 *전자 가족 한정도 충족 가능* 한가, *후자 포괄까지 의무* 인가의 자격 평가. **line 13 "최소 2 provider always-on" 적용** = 본 cycle 4 가족 분류의 *가족 다양성 유지* 의무 평가 의무 (단 본 평가는 메모리 본문 정정 자격 0, 합의 후 별도 cycle).

`project_jarvis_local_boss_direction` 메모리:
> provider-agnostic 개인 자비스: 로컬 LLM=사장(직접 지휘)·claude/gpt/GLM CLI=tmux 워커(교체)

본 cycle = "로컬 LLM=사장" 의 runtime 선택 자격에 직접 적용. 4 가족 분류의 사장 측 (로컬 LLM runtime) 적용 자격 평가 의무.

---

## 4. 핵심 긴장 6축 분석

> **🔴 R-2 답습 (B-B4 + C-S4 통합)**: 본 §4 5축 framing = brief v1 임시 framing. ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. **본 cycle 합의 결과에 따라 채택/대안 framing 자격 평가 의무. 자동 채택 0건** (Provider Liquidity 합의 R-3 답습 강한 변형). Phase 3 합의 R-5 (framing 약화 + 단정 표현 제거, R-3 본 cycle 답습) 답습 의무.

### 4.1 축 1 — 가족 내부 호환성 자격

> **🔴 R-9 답습 (수학적 표현)**: 가족 내부 호환성의 *수학적 표현* = (i) binary (각 (runtime, format) 쌍 = 호환/부정합) / (ii) spectrum (0~100% partial 호환) / (iii) cell-by-cell 4-D 매트릭스 (sub-차원 (1)~(5) × 시점 × 4-D) 3 후보. 본 cycle = 채택 자격 0, 합의 결과의 명시 자격. **Phase 3 합의 R-6 (PASS/FAIL framing 차단) 답습 = binary 표현 채택 자격 신중**. **Provider Liquidity 본질 binary 보존 (메모리 line 7) ≠ 호환성 표현 binary 강제** — 본질 (provider 교체 자유 binary) 과 수단 (호환성 표현 구조) 분리 자격 (ADR-011 §2.1 means/ends 답습).

**핵심 질문**: 각 가족 내부에서 runtime 간 동일 format 으로 *코드 변경 없이* 교체 가능한가?

- **GGUF 가족**: Phase 3 P3-F1 = **시점 의존 호환성 부재** (R-8 답습 — 본질 부정 아님, conversion lineage 시점 부정합). 시점 정합 시 호환 후보
- **HF-safetensors 가족**: vLLM/SGLang/Aphrodite 간 호환성 추정 (라이브 verify 0)
- **compiled-engine 가족**: GPU SM 의존 컴파일, runtime 간 호환 자격 *최약*
- **자체 format 가족**: 단일 runtime 가족이면 "내부 호환성" 개념 자체 무의미

**평가 자격**: 가족 내부 호환성 = **format spec 동일성 + conversion script 시점 정합성 + runtime 버전 정합성** 의 3 조건 교집합. 단일 binary 호환 자격 X.

### 4.2 축 2 — 가족 간 호환성 자격

> **🔴 R-30 답습 (case D 신규 분기)**: case C (means+ends 양면, Provider Liquidity 합의 R-4 답습) 의 4 가족 *내부* 적용 시 **case D (means ≡ ends 일부, 분리 불가)** 분기 자격 평가 의무. 가족 *내부* lineage 동기화 자체가 호환성 ends 달성의 직접 의무 = means 가 ends 의 일부로 흡수. 본 자격 평가 = Provider Liquidity 합의 R-4 본문 *해석* 확장 자격 X, 별도 합의 cycle 의무 (R-21 답습).

**핵심 질문**: 다른 가족으로 교체 시에도 *코드 변경 없이* 가능한가?

- **GGUF ↔ HF-safetensors**: `convert_hf_to_gguf.py` 의무 — *수단* 차원 (means)
- **GGUF ↔ compiled-engine**: GGUF → HF → TensorRT-LLM build 2단계 의무
- **HF-safetensors ↔ compiled-engine**: vLLM ↔ TensorRT-LLM = compilation step 의무
- **자체 format ↔ 다른 가족**: format 변환 의무 + 양자화 재수행 의무

**평가 자격**: 가족 간 호환성 = **conversion 의무 100%** (binary 답습). Provider Liquidity 충족 자격 = conversion script 가 *Python 코드 변경*인가 *config 변경*인가의 자격 평가 (means/ends 적용).

### 4.3 축 3 — Provider Liquidity 충족 자격의 분리 가능성

> **🔴 R-4 답습 (R-10 = Provider Liquidity 합의 R-10 차단 강화)**: 본 4 분리 후보는 **자격 평가 only**. (α) 채택 자격 = 헌법급 trigger + Provider Liquidity 본질 약화 = 메모리·헌법·ADR-011 line 245 관용 매핑 권위 변경 의무. 본 cycle 채택 자격 0.

**핵심 질문**: Provider Liquidity (헌법 5조 비협상) 의 *교체 가능* 진술이 *가족 내부 한정* vs *가족 간 포괄* 분리 가능한가?

| 분리 후보 | 진술 | 채택 자격 boundary (R-23 답습) |
|---|---|---|
| **(α) 가족 내부 한정** | "Provider Liquidity = 본 환경 선택 가족 내부의 runtime 교체 자격" (Liquidity 강도 ↓) | **채택 자격 = 본질 약화 = 본 cycle 채택 자격 0** (R-10 = R-4 답습). 채택 자격 = 헌법급 변경 trigger + 메모리·헌법·ADR-011 권위 변경 의무. **§0 line 9 binary 본질 명문 self-citation anchor 약화 의무 답습** |
| **(β) 가족 간 포괄** | "Provider Liquidity = 모든 가족 간 교체 자격 (conversion script 포함)" (Liquidity 강도 본질 유지) | 자동 채택 자격 (binary 본질 답습 — 메모리 line 7). 본 cycle 직접 영향 0 |
| **(γ) layered** | "내부 layer 강한 / 외부 layer 약한" (Provider Liquidity 합의 §7 (D) 옵션) | (R-12 답습) layered = 별도 ADR 발의 의무. **(D3)/(D4) 분기 답습 (R-24)** |
| **(δ) abstracted via API** | "OpenAI-compatible API 추상화 layer = format 가족 abstraction" (R-7 = §4.6 답습) | 별도 합의 cycle 의무 (R-26 답습 → 본 cycle / R-7 차원 폭발 risk) |

**자격 평가**:
- (α) = Provider Liquidity 본질 약화 risk (R-10 = R-4 답습 차단 강화)
- (β) = 본질 유지, conversion script 의무 명문 의무
- (γ) = R-12 답습 — framing 영구화 risk, (D3)(D4) 분기 답습
- (δ) = endpoint 추상화 차원, 4 가족 분류와 교차 축 (R-7 = §4.6 답습)

본 cycle = (α)~(δ) 자격 평가 only, 채택·기각 자격 0 (합의 *후* 사용자 명시 의무).

### 4.4 축 4 — 시간축 (Provider Liquidity 합의 R-3 답습)

**핵심 질문**: format 가족별 호환성이 *시점* 에 따라 어떻게 진화하는가?

- **GGUF spec 진화**: v1 → v2 → v3 (Provider Liquidity 합의 N-12 답습) — spec 자체 변화
- **conversion script 시점**: Ollama `30e51a7c` (≥ N개월 전) vs llama.cpp `c0c7e147` (최신) — 시점 lag (R-8 = R-S1 답습)
- **runtime 버전 정합성**: Ollama 0.20.4 (Phase 1) ↔ llama.cpp 최신 — 동시 업데이트 부재 시 호환성 disconnect
- **가족별 발전 cadence**: GGUF 가족 (활발 변경) vs compiled-engine (느린 cadence, HW dependent)

**spec 진화 evidence (Agent C 외부 식별 추정 한정, 라이브 verify 0, R-32 답습)**:

| spec 진화 후보 | 가족 | 진화 강도 (추정) | 4 가족 분류 시간 불변성 자격 |
|---|---|---|---|
| GGUF v3 | (a) | 강 (P3-F1 .bias flag 후보) | ↓ (분류 자체 spec 의존) |
| HF safetensors v2 | (b) | 중 (sharding metadata) | 중 |
| AWQ 1.x → 2.x | (b)/(d) cross | 강 (양자화 spec 진화) | β' framing 의존 |
| TensorRT-LLM Blackwell | (c) | 강 (SM 추가) | ε' framing 의존 |
| vLLM #36821 sm_120/121 | (b) | 중 (binary-compat) | 시점 의존 (해소 진행) |

표 머리: **외부 식별 추정 한정 (라이브 verify 0). 4 가족 분류의 *시간 불변성* = ↓ (spec 진화 의존). 시점 변경 시 4 가족 분류 자체 변동 자격. 본 brief = 2026-05-24 시점 스냅샷 명문.**

**평가 자격**: 시간축 = **본 cycle 평가의 missing dimension** (Provider Liquidity 합의 R-3 답습). 4 가족 분류 = 특정 시점 (2026-05-24) 스냅샷, 시점 변경 시 분류 자체 변동 자격.

### 4.5 축 5 — 본 framing 임시성 명문 (R-2 + R-3 + R-12 답습)

🔴 **본 §4 의 6축 자체가 brief v1.1 의 *임시 framing*** — ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. **본 cycle 합의 결과에 따라 채택/대안 framing 자격 평가 의무. 자동 채택 0건** (R-2 답습). Phase 3 합의 R-5 (framing 약화 + 단정 표현 제거) 답습 의무. 다른 framing 가능:

**framing α'~ε' 5 비교표 (R-11 = C-B4 답습)**:

| framing | Provider Liquidity 적용 강도 | 시간축 의존성 | 가족 분류 관계 | R-11 답습 자격 | 비례성 (개인 툴) |
|---|---|---|---|---|---|
| α' (4 가족 + 시간축, 본 brief 채택) | 분리 자격 평가 framework 강 | 5번째 축으로 명시 | self | 가족 한정 명문 ↓ | 중 |
| β' (양자화) | cross-runtime 호환성 직접 ↑ | AWQ/GPTQ/EXL2 진화 ↑ | 4 가족 직교 | sub-차원 (5) 한정 ↓↓ | 저 |
| γ' (deployment) | 약함 (배포 도구 한정) | docker/k8s 진화 ↓ | 4 가족 + 배포 직교 | sub-차원 (5) 미해당 ↓ | 중 |
| δ' (aggregator abstraction) | 핵심 후보 (endpoint 추상화) | LiteLLM 진화 ↑ | 4 가족 + abstraction 직교 강한 후보 | 인터페이스 sub-차원 한정 | 고 |
| ε' (HW target) | HW vendor lock-in ↔ Liquidity 충돌 | HW SM 진화 (Blackwell) ↑ | 4 가족 × HW 부분 포섭 | sub-차원 (5) 부분 ↓ | 중 |

표 머리: **외부 식별 추정 한정 (라이브 verify 0). 5 framing 우월성 단정 자격 0 (R-12 답습 cycle-specific framing 영구화 차단). 채택 자격 = 사용자 명시 + 별도 cycle. 본 비교 자체가 framing α' 채택의 *de facto* 압력화 = 차단 (R-29 답습).**

### 4.6 축 6 — abstraction layer 교차 자격 (R-7 신규, C-B2 + C-S2 통합)

> **🔴 R-7 답습 (신규 축)**: abstraction layer (OpenAI-compat / Ollama-compat / LiteLLM) = 4 가족 분류와 (1) 직교 / (2) 상호 배타 / (3) 포섭 3 자격 평가. **본 brief 평가 = 외부 식별 추정 (직교 강한 후보, 라이브 verify 0)**. 4 × 3+ = 12+ cell 차원 폭발 risk + sub-차원 (1) tensor naming 한정 evidence (R-11 답습) cell ≤ 1 명문. 채택 자격 = 사용자 명시 + 별도 cycle (R-12 답습).

**Cross-link 명문**:
- §2.3 (중첩 후보) OpenAI-compat 행 답습
- §4.3 (δ) abstracted via API 답습
- §4.5 framing δ' aggregator abstraction 답습
- §7.1 (E) abstracted API layer 채택 ADR 답습
- §7.3 (K) aggregator 추상화 layer 비교 cycle 답습

**평가**: aggregator runtime (Triton Inference Server·NVIDIA) = multi-framework backend (TensorRT-LLM·vLLM·FasterTransformer 호스팅) = **4 가족 분류 *흡수* abstraction layer** 강한 후보 (즉 abstraction = 포섭 framing). abstraction layer 가 (1) 직교 (2) 상호 배타 (3) 포섭 3 자격 모두 후보 — Agent C 외부 식별 추정 한정 명문 의무.

---

## 5. 3+1 합의 분담안 (v1 carry-over)

### 5.1 Agent 분담 + 핵심 질문

| 에이전트 | 관점 | 핵심 질문 |
|---|---|---|
| **Agent A** (구현 분석가) | "기술적으로 검증 가능한가? 4 가족 분류가 실 호환성 evidence 와 일치하는가?" | (Q-A1)~(Q-A4) |
| **Agent B** (품질·안전성) | "안전한가? 본 framing 이 헌법·ADR-011·MVP-1 합의·메모리 권위에 정합하는가?" | (Q-B1)~(Q-B5) |
| **Agent C** (대안 탐색가) | "더 나은 framing 이 있는가? 4 가족 분류 자체에 누락·중첩이 있는가?" | (Q-C1)~(Q-C5) |

### 5.2 분담 의무 (R-22 답습)

- 3 에이전트 **병렬 독립** — 서로의 출력 참조 0건 (편향 방지)
- 본 brief 본문 + Provider Liquidity 합의 본문 + Phase 3 raw 17 파일 + 헌법 본문 + ADR-011 본문 + MVP-1 합의 본문 cross-check 한정
- **각 에이전트 자체의 4 가족 분류 *채택*·*기각* 권한 0** — 진단 + 권고 옵션 매트릭스만
- 각 에이전트 자체의 라이브 verify (download/install/test) 권한 0

### 5.3 Reviewer 권한 + 한계 (R-14 답습 강화 — 7 항목 boundary 명문)

**Reviewer 권한**:
- 3 에이전트 출력 교차 비교 (일치 / 부분 / 불일치 / 누락)
- 합의 BLOCKING / 권고 / NOTE 분류 + 최종 판단
- **합의 결과 BLOCKING 본문이 brief v1.1 보강의 정정 자격** (R-21 답습)

**Reviewer 한계 (영구 답습, R-14 답습 boundary 명문 강화)**:
1. **ADR-011 §6 본문 정정 자격 0 (헌법급 amendment cycle 의무 = 별도 합의 cycle + 풀 3+1 + 사용자 명시 + ADR amendment 발의 자격 평가 의무, R-9 답습 강화)**
2. **Provider Liquidity 본질 약화 자격 0 (binary 본질 유지 — 메모리 line 7 verbatim "코드 변경 없이" + ADR-011 line 245 verbatim "제5조 관용 (Provider Liquidity, 비협상)" 직접 권위 매핑 답습, R-13 + R-10 통합 답습)**
3. **MVP-1 합의 본문 정정 자격 0 (별도 cycle, 해석 명확화 vs 본문 정정 boundary 명문 — R-6 답습)**
4. 헌법 본문 정정 자격 0
5. 메모리 본문 정정 자격 0 (본 cycle 합의 결과의 메모리 갱신 자격은 별도 사용자 명시)
6. **4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + (α)(β)(γ)(δ) 분리 후보의 어떤 후보도 영구 정착 자격 0 (특히 (α) 본질 약화 후보 = R-4 답습)**
7. **자동 다음 단계 진입 자격 0 (R-29 de facto 압력 차단 + R-30 기각 자격 명시 답습 통합). 자동 다음 단계 = (a) commit·push (별도 명시) / (b) brief v1.1 보강 (별도 명시) / (c) 메모리 갱신 (별도 명시) / (d) 다른 cycle 진입 (별도 명시) 4 차원 모두 분리 의무**

---

## 6. 합의 출력 형식 (v1 carry-over)

### 6.1 출력 형식 명문

각 Agent 보고서: 판정 (APPROVE/REVISE/REJECT) + BLOCKING + 권고 + NOTE + 단독 발견 + 정직성 한계.
Reviewer 통합: 정합성 매트릭스 (일치/부분/불일치/누락) + 단독 발견 격상 자격 + BLOCKING/권고/NOTE 통합 + 기각 자격 명시.

### 6.2 raw line-level cross-check 의무 (Provider Liquidity 합의 R-23 답습 + R-34 답습)

- Phase 3 raw 17 파일의 line-level 인용 (offset 명시) — 본 cycle 사용 2 파일 외 15 파일 별도 cycle 의무
- Provider Liquidity 합의 보고서 line-level 인용
- 헌법 본문 line 인용 (40~46, 67~73)
- ADR-011 본문 line 인용 (6, 52~59, 212, 245, §2.1, §6)
- MVP-1 합의 본문 line 인용 (R4 = line 63 행 전체 R-22 답습)
- 메모리 line offset 명시 (line 7 + line 11~17 R-35 답습)
- **각 가족 (a)~(d) 4 column 의 라이브 verify 0** — line-level cross-check 의무 Phase 3 raw + Provider Liquidity 합의 + 헌법·ADR-011 한정

---

## 7. 후속 결정 권고 옵션 매트릭스

### 7.1 옵션 (A)~(E) — 본 cycle 직접 결과 답습

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(A)** | 4 가족 분류 **현 상태 유지** + 본 brief framing 임시성 명문만 (R-12 답습 강한 변형) | 합의 후 사용자 명시. MVP-1 합의·메모리 본문 변경 0건 |
| **(B)** | 4 가족 분류 + 누락 가족 추가 (MLX·NIM·OpenAI-compat·RWKV·AWQ/GPTQ + Agent C 추가 7) | 합의 후 사용자 명시. R-33 + R-31 답습 |
| **(C)** | 4 가족 분류 폐기 + 다른 framing 채택 (양자화/배포/aggregator/HW target) | 합의 후 사용자 명시 + 별도 framing 합의 cycle |
| **(D)** | layered Provider Liquidity 모델 신규 ADR 발의 (Provider Liquidity 합의 §7 (D) 답습) | 헌법급 변경 trigger — 사용자 명시 + 풀 3+1 + Reviewer 권한 한계 답습 별도 cycle |
| **(D3)** | (D) 대신 framing 비교 본문 포함 ADR (α'~ε' 5 framing + 4 가족 + layered 비교 본문) — R-24 답습 | 별도 cycle, 비용 ↑, framing 결정 *고정* 차단 |
| **(D4)** | (D) ADR 발의 DEFER + 본 cycle 결과 → 헌법 5조 본문 보강만 ((C) 옵션 답습) — R-24 답습 | 가벼움, framing 결정 *고정* 0 |
| **(E)** | abstracted API layer (LiteLLM / OpenAI-compatible) 채택 ADR 발의 | 별도 합의 cycle, R-7 = §4.6 답습 |

### 7.2 옵션 (F)~(J) — 가족별 deep-dive cycle

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(F)** | GGUF 가족 deep-dive — sub-차원 (2)~(5) 측정 (MoE routing / tokenizer / chat template / quantization) | 별도 brief + 사용자 명시. 측정 cycle |
| **(G)** | HF-safetensors 가족 라이브 verify — vLLM/SGLang Qwen3-Next 호환성 측정 (sm_120/121 binary-compat 해소 흐름 추적) | 별도 brief + 사용자 명시. 다운로드/설치 cycle |
| **(H)** | compiled-engine 가족 라이브 verify — TensorRT-LLM Blackwell support 추적 | 별도 brief + 사용자 명시. NVIDIA toolchain cycle |
| **(I)** | 자체 format 가족 라이브 verify — exllamav2 / MLC-LLM 평가 | 별도 brief + 사용자 명시 |
| **(J)** | 4 가족 cross-conversion 매트릭스 — GGUF ↔ HF ↔ TensorRT ↔ EXL2 conversion script 평가 | 별도 brief + 사용자 명시 |

### 7.3 옵션 (K)~(M) — 후속 framing cycle

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(K)** | aggregator (LiteLLM / vllm-openai / Ollama-compat / OpenAI-compat) 추상화 layer 비교 cycle | 별도 brief, R-7 답습 강한 후속 |
| **(L)** | 양자화별 cross-runtime 호환성 cycle (AWQ/GPTQ/EXL2/GGUF Q4_K_M 등) | 별도 brief, R-28 답습 |
| **(M)** | HW target 별 가족 비례성 (NVIDIA / AMD / Apple Silicon / mobile) | 별도 brief |

### 7.4 DEFER / 기각 옵션 (R-30 답습 — 기각 자격도 사용자 명시)

| 옵션 | 내용 | 발생 |
|---|---|---|
| **(D1)** | 본 4 가족 분류 자체 기각 — framing 채택 자격 0 명문 | 사용자 명시 + 별도 합의 |
| **(D2)** | 본 cycle 결과의 메모리 갱신 자격 0 — `feedback_provider_liquidity` 본문 유지 | 자동 (기본값) |
| **(D3)** ※ | MVP-1 R4 진술 정정 자격 0 — 가족 한정 자격은 *해석 명확화* only, 본문 정정 0건. **해석 명확화 vs 본문 정정 boundary**: (a) 해석 명확화 = 본 cycle 합의 산출 자격, §3.2 추가 본문 한정 / (b) 본문 정정 = 별도 합의 cycle 의무 + 사용자 명시 + Reviewer 권한 한계 R-21 (3) 답습 | 사용자 명시 차단 (R-29 답습) — R-6 답습 |
| **(D4)** ※ | 4 가족 분류의 영구 framing 정착 0 — 다른 cycle 의 진입 근거화 차단 | 자동 (R-12 + R-29 답습) |

※ (D3)/(D4) 라벨은 §7.1 (D) layered ADR 의 (D3)/(D4) 분기와 동일 라벨 (R-24) 이나 별도 항목. 합의 결과 후 라벨 명확화 의무.

---

## 8. 정직성 한계

1. **본 brief = 외부 식별 추정 only** — 4 가족 8+ runtime 의 라이브 verify (download/install/test) 0건. 각 runtime 의 실제 버전·실제 format spec·실제 호환성 = 별도 cycle 의 라이브 verify 의무
2. **Phase 3 evidence GGUF 가족 한정** (R-11 답습) — 다른 3 가족 (HF/compiled-engine/자체) 의 본 cycle 평가 = *입력 자격 0* 시작점
3. **P3-F1 evidence sub-차원 (1) 한정** (R-7 답습) + **conversion script lineage 시점 부정합 한정** (R-8 = R-S1 답습) — model loading 의 sub-차원 (2)~(5) (MoE routing / tokenizer / chat template / quantization) 미측정. 가족 본질 부정 아님
4. **4 가족 분류 자체의 영구 framing 자격 0** (R-12 답습) — cycle-specific framing, 채택·기각·확장 자격 = 본 cycle 합의 + 사용자 명시 *후*
5. **시간축 missing dimension 가능성** (R-3 답습) — 본 brief 평가 = 특정 시점 (2026-05-24) 스냅샷, 시점 변경 시 분류 자체 변동 자격
6. **MVP-1 R4 진술의 가족 한정 자격 = 해석 명확화 자격**, 본문 정정 자격 0 (R-21 + R-6 답습)
7. **헌법 5조 본문 ↔ ADR-011 line 6/212/245 관용 매핑 권위 + 내부 비대칭** = 본 cycle 답습 의무, 권위 자체 변경 자격 0 (R-13 + R-10 + R-9 답습)
8. **메모리 `feedback_provider_liquidity` 19일+ stale** (R-20 답습) — 본 cycle 인용 자격 답습 후 신규 cycle 진입 시 재verify 의무. **메모리 line 11~17 적용 가이드 6 항목 인용 의무 (line 12 분기 코드 금지 + line 13 최소 2 provider always-on + line 14 OAuth 직결 금지 + line 15 depcruise + line 16 검토 대상 5 + line 17)** (R-13 답습)
9. **Phase 3 P3-F1 일반화 자격 한정** — 1 모델 (qwen3-coder-next) + 2 runtime (Ollama·llama.cpp) + 1 sub-차원 (tensor naming) + **1 conversion lineage (`.dt_bias` rename)** + 1 시점 (2026-05-24) 측정. 5 차원 일반화 자격 부재 (R-8 답습)
10. **본 brief 의 6축 framing 자체가 anchor effect risk + Phase 3 합의 R-5 (framing 약화) 답습 의무** — 다른 framing 가능 (β'/γ'/δ'/ε' Q-C1 답습), framing 채택 자격 = 본 cycle 합의 + 사용자 명시 *후* (R-2 + R-3 답습)
11. **본 brief 의 SDD 정합성 평가 = 본 cycle 시점 한정** — 메모리·MVP-1 합의·헌법·ADR-011 본문이 본 cycle 후 변경되면 본 brief 진술 자격 재평가 의무. **각 가족 (a)~(d) 4 column 의 라이브 verify 0** — line-level cross-check 의무 Phase 3 raw + Provider Liquidity 합의 + 헌법·ADR-011 한정 (R-34 답습)
12. **Reviewer 권한 한계 답습** — ADR-011 §6 본문 정정 자격 0 + Provider Liquidity 본질 약화 자격 0 + MVP-1 합의 본문 정정 자격 0 + 헌법 본문 정정 자격 0 + 메모리 본문 정정 자격 0 + **4 가족 분류 자체의 영구 framing 정착 자격 0** (R-12 + R-21 답습) + **자동 다음 단계 진입 자격 0 (R-29 + R-30 답습 통합)** (R-25 답습)
13. **본 brief 가 후속 cycle 의 *de facto* 정정 진입 근거화 0건** (R-29 답습) — 후속 cycle 의 정정 자격은 사용자 명시 + 별도 합의 의무
14. **본 cycle 합의 결과의 *기각* 자격도 자동 발효 0건** (R-30 답습)
15. **본 brief 의 누락 가족 식별 (MLX·NIM·OpenAI-compat·RWKV·AWQ/GPTQ + Agent C 추가 7) = 추정** — 라이브 verify 0, 누락 자격 자체 = Agent C 의무
16. **중첩 후보 (llamafile·MLC-LLM·OpenAI-compat) 분류 자격** = 추정, 처리 5 자격 매트릭스 (R-12 답습) 본 cycle 채택 자격 0

---

## 9. 차단 조건 (R-15 = R-S3 답습 — §0 12 항목 1:1 매핑 정합화)

### 9.1 본 brief 가 자동 발효시키지 않는 것 (§0 12 항목 1:1 매핑)

1. ❌ 4 가족 분류 자체의 결정 *고정* (모든 옵션 = 사용자 명시 의무)
2. ❌ MVP-1 합의 본문 자동 정정
3. ❌ 헌법 본문 자동 정정
4. ❌ ADR-011 amendment 자동 발의 (R-9 답습 — 헌법급 변경)
5. ❌ M3·M4 결정 *고정*
6. ❌ OllamaBoss·LlamaCppBoss·vLLMBoss·TensorRTLLMBoss·기타 runtime backend 코드 작성
7. ❌ 새 측정·새 빌드·새 다운로드·새 runtime 설치
8. ❌ 메모리 `feedback_provider_liquidity` 본문 자동 정정
9. ❌ Provider Liquidity 본질 약화 (binary 본질 유지) — **§4.3 (α) 가족 내부 한정 분리 후보의 자동 채택 차단** (R-4 답습)
10. ❌ 본 4 가족 분류의 영구 framing 정착 (R-12 답습) — (α)(β)(γ)(δ) 어느 후보도 영구 정착 자격 0
11. ❌ 본 brief 의 진단표 (§3·§4) 가 후속 cycle 의 정정 *진입 근거* 가 되는 *de facto* 압력 발생 (R-29 답습)
12. ❌ 본 cycle 합의 결과의 *기각* 자격도 자동 발효 (R-30 답습)

### 9.2 합의 BLOCKING 처리 의무 (R-21 답습)

본 cycle 합의 (`d75dceb`) BLOCKING 16 verbatim 본문 직접 반영 100% 의무. 권고 21 본문 직접 반영 또는 §10 NOTE carry-over. §11 변경 일람 표 신규.

### 9.3 본 brief 진단표 (§3·§4) → 후속 cycle 정정 진입 근거화 차단 (R-29 답습)

본 §3 · §4 의 표 자체가 후속 cycle 의 MVP-1 합의·헌법·ADR-011 본문 정정 *de facto* 진입 근거가 되는 흐름 차단.

### 9.4 본 cycle 합의 결과의 자동 기각 자격 차단 (R-30 답습)

본 cycle 합의 결과 (BLOCKING / 권고 / NOTE) 의 *기각* 자격도 자동 발효 0건.

### 9.5 본 brief 의 6축 framing self-citation anchor 차단 (R-2 = B-B4 + C-S4 통합 답습)

본 §4 6축 framing 이 후속 cycle 의 정정 *진입 근거* 가 되는 *de facto* 압력 0건. 6축 framing 자체의 *영구 정착* 자격 0 (R-12 + R-29 통합).

---

## 10. NOTE carry-over (24 항목)

> 본 cycle 합의 *후* 별도 cycle 의무 항목. Provider Liquidity 합의 NOTE 12 carry-over + 본 cycle 신규 12 = 24. **본 cycle 합의 결과 신규 NOTE 등재 자격 = 각 Agent (A/B/C) + Reviewer 통합 산출** (R-26 답습).

### Provider Liquidity 합의 NOTE 12 carry-over (N-1 ~ N-12)

| NOTE | 본 cycle 답습 |
|---|---|
| N-1 (SSM 명명법 정정 부분 적용) | Phase 1·2·3 evidence 답습 시 명명법 정합성 유지 |
| N-2 (runtime 별 implementation 차이 어법 약점) | 본 brief §2.1~§2.3 답습 |
| N-3 (P3-F1 일반화 자격 3 차원 한정) | §8 정직성 9 답습 + R-8 추가 layer (conversion lineage 시점) |
| N-4 (ADR-011 §2.1 (e) 모법 인용 자격) | §1.5 (e) 답습 + R-5 = R-S2 = R-14 본문/후속 분리 |
| N-5 (메모리 19일+ stale) | §3.4 + §8 정직성 8 답습 |
| N-6 (옵션 (K) R4 범위 확장 자격) | 본 §7 (D)/(D3) 답습 |
| N-7 (LiteLLM 인터페이스 한정) | §7 (K) (E) 답습 + R-7 = §4.6 답습 |
| N-8 (ADR-008 부록 B Amendment 패턴) | (D) 옵션 자격 답습 |
| N-9 (라이센스 차원) | §7 (M) 후보 답습 |
| N-10 (비용 차원) | §7 (M) 후보 답습 |
| N-11 (한국어 모델 호환성) | 별도 cycle |
| N-12 (외부 표준화 동향 + supply chain opacity) | §4.4 시간축 답습 |

### 본 cycle 신규 NOTE 12 (N-13 ~ N-24)

| NOTE | 내용 | 출처 |
|---|---|---|
| N-13 | ADR-011 §6 line 212 "Provider Liquidity 영향 무관" vs line 6/245 직접 권위 매핑 *적용 범위 boundary* 평가 cycle | B-N1 |
| N-14 | 4 가족 × 메모리 line 11~17 적용 가이드 6 항목 = 24 cell 매트릭스 평가 cycle (R-13 답습) | B-N2 |
| N-15 | SSM 명명법 정정 (Phase 2 F2 답습) + 본 cycle 답습 cycle | B-N4 |
| N-16 | ADR-008 부록 B Amendment 패턴 답습 자격 (옵션 (D)/(E) 발의 시 의무) | B-N5 |
| N-17 | 본 cycle 합의 후 메모리 `feedback_provider_liquidity` 본문 line 7 "코드 변경 없이" 범위 보강 자격 | B-N6 |
| N-18 | Agent C 추가 후보 7 가족 (PowerInfer/CTranslate2/PETals/Triton/TensorRT-Model-Optimizer/MLX/NIM) 라이브 verify cycle | C-N1 |
| N-19 | 4 가족 분류 *축* 자체 평가 cycle (R-1 답습 후속) | C-N2 |
| N-20 | ADR-011 §6 line 212 *주제 범위 한정* + line 6/245 *권위 위계 의존* 통합 답습 cycle (R-10 답습) | C-N4 |
| N-21 | framing β'~ε' 5 비교표 후속 (다른 framing 채택 자격 별도 cycle, R-11 답습) | C-N5 |
| N-22 | spec 진화 evidence (GGUF v3 / HF safetensors v2 / AWQ / Blackwell / vLLM #36821) 라이브 verify cycle | C-N7 |
| N-23 | aggregator runtime (Triton·OpenAI-compat) + 양자화 framework (TensorRT-Model-Optimizer) + distributed inference (PETals·Hivemind) 4 가족 직교 자격 평가 cycle | C-N8/N9/N10 |
| N-24 | 본 4 가족 분류 영구 framing 정착 차단 (R-12) carry-over 의무가 후속 framing cycle 마다 답습 — R-29 답습 패턴 | C-N12 |

---

## 11. 변경 일람 표 (v1 → v1.1)

| § | 변경 내용 | 출처 BLOCKING / 권고 |
|---|---|---|
| **헤더 + §0 머리** | v1.1 (APPROVE w/ COND 반영) 라벨. 합의 답습 R-3·R-7·R-9·R-10·R-11·R-12·R-13·R-21·R-22·R-26·R-29·R-30 명시 (R-21) + Phase 3 합의 R-5 추가 | R-3 + R-21 + R-22 |
| **§0.1 선행 답습** | Provider Liquidity brief v1 (`9ed376a`, 407줄) 추가 (R-20 답습) + 본 cycle 합의 보고서 (`d75dceb`) 추가 | R-20 |
| **§0 하지 않는 것** | 12 항목 §9.1 1:1 매핑 정합화 (R-15 = R-S3 답습). 각 항목 출처 라벨 추가 | R-15 |
| **§1.4 헌법·ADR-011 매핑** | ADR-011 line 212 verbatim 추가 (R-10 = R-S2 답습 — 내부 비대칭 명문). 헌법 5조 line 40~46 verbatim 6 항목 직접 인용 추가 (R-17). 진단 의무 enum 5 항목 명문 추가 (R-16) | R-10 + R-17 + R-16 |
| **§1.5 ADR-011 §2.1 적용** | ADR-011 line 52~59 verbatim 표 직접 인용 추가 (R-18 + R-5). (a)~(d) 본문 vs (e) 후속 패턴 분리 명문 (R-5 = R-S2 = R-14 답습) | R-5 + R-18 |
| **§2.1 evidence** | raw line 25~32 결론 verbatim 인용 추가 (R-S1 격상 evidence). P3-F1 일반화 자격 추가 layer (conversion script lineage 시점 부정합 한정, R-8 답습) | R-8 |
| **§2.3 4 가족 외부 식별** | 분류 기준 명문 추가 (R-1 답습). 각 runtime 내부 conversion script lineage 부재 명문 추가 (R-27). (a) ktransformers fuzzy 명문 + (b)(c)(d) 동일 fuzzy 자격 평가 의무 (R-1). 누락 후보 표에 4 가족 관계 + 양자화 직교 명문 추가 (R-33 + R-28). Agent C 추가 누락 후보 sub-표 신규 (R-31). 중첩 후보 처리 5 자격 표 신규 (R-12) | R-1 + R-12 + R-27 + R-28 + R-31 + R-33 |
| **§3.1 권위 매핑 정합성** | 헌법 5조 line 40~46 + ADR-011 line 6 + line 212 + line 245 + §2.1 (a)~(d) + (e) + §6 행 신규 추가 (R-10 + R-13 + R-17 + R-18) | R-10 + R-13 + R-17 + R-18 |
| **§3.2 MVP-1 R4** | R4 verbatim 행 전체 (출처·등급 컬럼 포함) 인용 보강 (R-22). 해석 명확화 vs 본문 정정 boundary 명문 추가 (R-6) | R-6 + R-22 |
| **§3.3 ADR-011 §2.1 답습** | 출처 컬럼 신규 + (a)~(d) 본문 + (e) 후속 패턴 모법 인용 분리 명문 (R-5 + R-19) | R-5 + R-19 |
| **§3.4 메모리 정확성** | 메모리 line 7 line offset 명시 (R-35). 메모리 line 11~17 적용 가이드 6 항목 verbatim 인용 추가 — 특히 line 13 "최소 2 provider always-on" (R-13 = B-B5) | R-13 + R-35 |
| **§4 머리** | self-citation 후속 매핑 명문 (R-2 = B-B4 + C-S4 통합). Phase 3 합의 R-5 답습 의무 명문 (R-3) | R-2 + R-3 |
| **§4.1 가족 내부 호환성** | 수학적 표현 (binary/spectrum/cell-by-cell) 3 후보 명문 (R-9). 본질 (binary) vs 수단 (호환성 표현 구조) 분리 명문 | R-9 |
| **§4.2 가족 간 호환성** | case D (means ≡ ends 분리 불가) 신규 분기 추가 (R-30 = A-S3 답습) | R-30 |
| **§4.3 Provider Liquidity 분리 자격** | (α) 채택 자격 boundary 강화 (R-4 = R-10 답습 차단). (β)(γ)(δ) 채택 자격 boundary 명문 (R-23) | R-4 + R-23 |
| **§4.4 시간축** | spec 진화 evidence (GGUF v3 / HF safetensors v2 / AWQ / Blackwell / vLLM #36821) sub-표 신규 (R-32) | R-32 |
| **§4.5 framing 임시성** | 6축 (v1 5축 → 6축) + framing α'~ε' 5 비교표 신규 (R-11). 자동 채택 0건 명문 강화 (R-2 + R-3) | R-2 + R-3 + R-11 |
| **§4.6 abstraction layer 신규** | 신규 축 6 — abstraction layer 교차 자격 (R-7 = C-B2 + C-S2 통합). cross-link 명문 | R-7 |
| **§5.3 Reviewer 권한 한계** | 7 항목 boundary 명문 강화 (R-14 = B-B7 답습 1~5 항목 동형) | R-14 |
| **§6.2 raw cross-check** | 메모리 line offset 명시 (R-35). 각 가족 4 column 라이브 verify 0 명문 (R-34) | R-34 + R-35 |
| **§7.1 (D)/(D3)/(D4)** | (D3)/(D4) 분기 신규 추가 (R-24 = B-R5 + C-R3 통합) | R-24 |
| **§7.4 (D3)** | 해석 명확화 vs 본문 정정 boundary 명문 (R-6) | R-6 |
| **§8 정직성 한계** | 12 → 16 항목 (항목 3 R-8 답습 / 항목 8 메모리 line 11~17 / 항목 9 conversion lineage / 항목 10 R-5 답습 / 항목 11 라이브 verify 0 / 항목 12 R-25 답습 자동 다음 단계 0). 항목 15·16 추가 | R-13 + R-25 + R-34 |
| **§9 차단 조건** | §9.1 12 항목 1:1 매핑 정합화 (R-15 = R-S3 답습). §9.5 신규 — 6축 framing self-citation anchor 차단 (R-2) | R-2 + R-15 |
| **§10 NOTE** | 12 → 24 항목 (Provider Liquidity 합의 NOTE 12 carry-over + 본 cycle 신규 12). 표 머리에 합의 결과 신규 NOTE 등재 자격 명문 (R-26 + R-37) | R-26 + R-37 |
| **§11 변경 일람** | 본 §11 자체 (Provider Liquidity brief v1.1 §11 패턴 답습) | 본 v1.1 산출 |

**변경 통계**: 556 → 약 730줄 (+~175줄). BLOCKING 16 verbatim 본문 직접 반영 100%. 권고 21 본문 직접 반영 또는 §10 NOTE carry-over. NOTE 24 §10 표 carry-over. 기각 0건.

---

**End of brief v1.1** (작성일 2026-05-24, 본 cycle 합의 `d75dceb` BLOCKING 16 verbatim 반영, 결정 *고정* 0건, Provider Liquidity 본질 약화 0건, 4 가족 분류 영구 framing 정착 0건 답습)
