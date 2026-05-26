# 3+1 합의 보고서 — Jarvis MVP-1 format 가족별 분류 cycle entry brief

> **합의 cycle (f-K)**: Provider Liquidity deep-dive 합의 (`a9e1e88`, BLOCKING 13) 의 **R-26 (C-R2) + R-11** 답습 후속 cycle. brief v1 (`f305174`, 556줄) → 풀 3+1 합의 (Agent A/B/C 병렬 독립 → Reviewer 통합) 산출. **APPROVE w/ COND**, BLOCKING 16 + 권고 21 + NOTE 24, **기각 0**, **Reviewer 단독 격상 BLOCKING 3** (R-S1 / R-S2 / R-S3). 본 합의는 brief v1 의 진술을 BLOCKING 으로 정정하는 *권한* 을 가지나, **(1) ADR-011 §6 본문 정정 자격 0 + (2) Provider Liquidity 본질 약화 자격 0 + (3) MVP-1 합의 본문 정정 자격 0 + (4) 헌법 본문 정정 자격 0 + (5) 메모리 본문 정정 자격 0 + (6) 4 가족 분류 자체의 영구 framing 정착 자격 0 (R-12 답습) + (7) 자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)** 의 **7 권한 한계 영구 답습**.

**작성일**: 2026-05-24
**진입 근거**: 사용자 명시 "(A) 풀 3+1 합의 진입"
**대상 brief**: `docs/phase0/jarvis-mvp1-format-family-classification-consensus-entry-brief.md` v1 (`f305174`, 556줄)
**선행 합의**: Provider Liquidity deep-dive 합의 (`a9e1e88`, BLOCKING 13 + 권고 17 + NOTE 12) / Phase 3 합의 (`e76acc8`, BLOCKING 7) / M3·M4 단독 미충족 합의 (`d2d7bf9`, BLOCKING 5) / MVP-1 합의 (`15beb33` 답습)
**3 에이전트 출력 본문**: Agent A (REVISE, BLOCKING 3 + 권고 6 + NOTE 6 + 단독 3) / Agent B (REVISE, BLOCKING 7 + 권고 8 + NOTE 6 + 단독 6) / Agent C (REVISE, BLOCKING 5 + 권고 5 + NOTE 12 + 단독 4)

---

## 1. 합의 판정

**APPROVE w/ COND** — 3 에이전트 모두 **REVISE** 일치 (REJECT 0). brief v1 의 framing 합의 input 자격 자체 (R-26 + R-11 답습 후속) 충족. 단 **BLOCKING 16 정정 의무** + **권고 21 보강 의무** + **NOTE 24 carry-over** 후 brief v1.1 보강 진입 자격.

**기각 0건** = 본 합의 결과의 모든 BLOCKING/권고/NOTE 의 자동 기각 자격 0 (R-30 답습). 사용자 명시 + 별도 합의 의무.

---

## 2. 정합성 매트릭스 (3 Agent 교차 비교)

### 2.1 일치 (Consensus — 2+ Agent 동형 발견)

| 주제 | Agent A | Agent B | Agent C | 통합 BLOCKING |
|---|---|---|---|---|
| **분류 *기준* 단일축 부재 (분류 축)** | A-B1 ✓ | - | C-B1 ✓ + C-S1 ⭐ | **R-1** |
| **self-citation anchor risk 후속 cycle 답습 매핑** | - | B-B4 ✓ | C-S4 ✓ | **R-2** |
| **Phase 3 합의 R-5 (framing 약화) 답습 누락** | - | B-B6 ✓ | C-R5 ✓ | **R-3** |

### 2.2 부분 일치 (Partial — 2 Agent 인접 차원)

| 주제 | Agent | 통합 |
|---|---|---|
| evidence "GGUF 한정" 더 좁은 한정 (시점 부정합 vs 분류 축) | A-B2 + A-S1 ⭐ / C-B1 + C-S1 ⭐ | A 시점 부정합 + C 분류 축 = 본질 부정 *분리* 동형 → R-S1 통합 |
| ADR-011 본문 답습 보강 | B-B2 (§2.1 표기) / C-B3 + C-S3 ⭐ (§6 line 212 비대칭) | 다른 line 다른 차원 → 각각 처리 |

### 2.3 불일치 (Divergence)

3 Agent 모두 다른 의견 항목 = **0건**. 정면 충돌 0건 = 강한 정합성 evidence (Provider Liquidity 합의와 동일 패턴).

### 2.4 누락 (Gap — Agent 단독 발견)

**Agent A 단독** (A-S1~S3, A-B2, A-B3):
- A-S1 ⭐: Phase 3 raw `conversion/qwen.py:299-300` verbatim cross-check → "GGUF 가족 본질 부정 ≠ llama.cpp conversion lineage 시점 부정합" 분리 (BLOCKING 격상)
- A-S2: ktransformers "부분" fuzzy membership 비대칭 (4 가족 분류 fuzzy set 자격 evidence)
- A-S3: case D (means ≡ ends 분리 불가) 신규 분기 (Provider Liquidity 합의 R-4 case C 의 가족 *내부* 적용 시)
- A-B2: P3-F1 evidence GGUF 가족 한정 보다 *더 좁은* (1 conversion lineage 시점) 한정
- A-B3: 가족 내부 호환성 수학적 표현 (binary/spectrum/cell-by-cell) 자격 미평가

**Agent B 단독** (B-S1~S6, B-B1~B7):
- B-S5 ⭐⭐: §0 "하지 않는 것" 12 항목 vs §9.1 차단 6 항목 *비대칭* (정직성 risk, BLOCKING 격상)
- B-S6: 진단 의무 enum 명문 부재 (Provider Liquidity 합의 R-19 답습 미적용)
- B-S2: 선행 답습 11 항목 중 Provider Liquidity brief v1 (`9ed376a`) 누락
- B-S3: §0.1 답습 의무 행에 R-9 (헌법급 변경) 누락
- B-S4: §3.2 R4 verbatim 행 출처·등급 컬럼 ("| C | 🔴 정합") 누락
- B-S1: 메모리 본문 인용 line offset 부재 (인용 형식 비균질성)
- B-B1: §4.3 (α) "가족 내부 한정" 본질 약화 risk 차단 명문 부족 (Provider Liquidity 합의 R-10 답습 미완)
- B-B2: ADR-011 §2.1 "(a)~(d) 4조건" vs brief "(a)~(e) 5조건" 표기 carry-over (R-14 답습 미완)
- B-B3: MVP-1 R4 해석 명확화 vs 본문 정정 boundary 명문 부족
- B-B5: 메모리 본문 적용 가이드 6 항목 (line 13 "최소 2 provider always-on") 본 brief 인용 부재
- B-B7: Reviewer 권한 한계 7 항목 boundary 명문 부족

**Agent C 단독** (C-S1~S4, C-B2~B5):
- C-S3 ⭐ → C-B3: ADR-011 §6 line 212 "Provider Liquidity 영향: 무관" vs line 6/245 직접 권위 매핑의 *내부 비대칭* 답습 부재 (Provider Liquidity 합의 R-13 미답습 부분, BLOCKING 격상)
- C-S2: abstraction layer (OpenAI-compat / Ollama-compat / LiteLLM) 의 4 가족 분류 직교/포섭/배타 자격 평가 부재 + 차원 폭발 risk
- C-B2: abstraction layer 교차 축 자격 명시 부재 (5 곳 분산)
- C-B4: framing β'~ε' (양자화 / 배포 / aggregator / HW target) 상호 트레이드오프 비교표 부재
- C-B5: 중첩 후보 3종 (llamafile / MLC-LLM / OpenAI-compat) 분류 처리 의무 미명문

### 2.5 Reviewer 자체 발견 (R-S* 라벨)

3 Agent 모두 미발견, Reviewer 직접 cross-check 시 발견:

- **R-S1 (A-S1 격상)** ⭐: Phase 3 raw line 25~32 결론 verbatim 직접 확인 — "Ollama 다운로드 GGUF = 더 오래된 conversion (`.ssm_dt.bias` 미저장) + llama.cpp `c0c7e147` master = `.dt_bias` → `.dt_proj.bias` rename + `.bias` flag=0 required 강제". 본 evidence 의 본질 = **시점 부정합** (Ollama blob 동기화 미수행 + llama.cpp conversion lineage backward-incompatible 변경) ≠ "GGUF 가족 본질 부정". A-S1 = Reviewer 단독 직접 raw 확인으로 격상 BLOCKING.
- **R-S2 (C-B3 격상)** ⭐: ADR-011 line 6 + line 212 + line 245 verbatim 직접 확인 — "**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)" (line 6) + "Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관" (line 212) + "제5조 **관용** (Provider Liquidity, 비협상)" (line 245) → ADR-011 *내부* 비대칭 정착. line 6/245 = *권위 위계 의존*, line 212 = *주제 범위 한정* (redaction 수단 본질 한정). 본 cycle 답습 의무 = 두 차원 모두 명문. C-B3 = Reviewer 격상 BLOCKING.
- **R-S3 (B-S5 격상)** ⭐⭐: brief v1 §0 line 46~58 (12 항목) + §9.1 line 484~491 (6 항목) 직접 cross-check — §0 (하지 않는 것) ≠ §9.1 (차단 조건) 1:1 매핑 부재. (1) ADR-011 amendment 자동 발의 / (2) 메모리 자동 정정 / (3) 4 가족 분류 영구 framing 정착 / (4) §3·§4 진단표 후속 cycle 정정 진입 근거화 / (5) 본 cycle 합의 결과 자동 기각 / (6) 4 가족 분류 자체의 결정 *고정* 6 항목이 §9.1 미명시. brief 본문 self-consistency 약화 정직성 risk. B-S5 = Reviewer 격상 BLOCKING.

---

## 3. 통합 BLOCKING (R-1 ~ R-16)

> brief v1.1 보강 시 본 BLOCKING 16 의 verbatim 본문 직접 반영 의무 100% (Provider Liquidity 합의 R-21 답습).

### R-1 — 4 가족 분류 *분류 기준* 단일축 명시 부재 (A-B1 + C-B1 + C-S1 통합)

**근거**: brief v1 §1.3 Q1 line 87 verbatim:
> 분류 기준 (format file extension / loader 구현 path / serialization 방식 / 양자화 호환성) 의 정합성

→ 4 후보 기준이 *enum* 으로 명시되나, §2.3 (a)~(d) 표 + §4 5축 어디에도 **본 brief 채택 기준** 미명문. ktransformers "부분" (line 187) 라벨 = fuzzy membership 시사. compiled-engine 가족 = TensorRT-LLM `.engine` vs MLC-LLM `.so`/TVM compiled = file extension 다름에도 동일 가족 → 분류 기준 (i) compilation 단계 보유 / (ii) GPU SM 의존 컴파일 unclear.

**처리**: brief v1.1 §2.3 머리에 verbatim 추가:
> "본 4 가족 분류의 1차 기준 = **serialization 방식 + 동일 loader 코드 경로** 의 교집합 (Reviewer 통합 권고). 단 (i) format extension / (ii) 양자화 format / (iii) deployment 형태 / (iv) HW target 은 *직교 축* 으로 본 분류와 독립. 본 채택 기준 자체의 영구 framing 정착 자격 0 (R-12 답습), 합의 결과 후 별도 cycle 재평가 자격."

추가: §2.3 (a) 표의 "ktransformers (부분)" 라벨에 fuzzy membership 명문 + (b)/(c)/(d) 각 가족에도 fuzzy membership 가능성 평가 의무 명문 추가.

### R-2 — self-citation anchor risk 후속 cycle 답습 매핑 부재 (B-B4 + C-S4 통합)

**근거**: brief v1 §4.5 line 346 + §8 정직성 항목 10 = self-citation anchor risk *식별* PASS. 단 **anchor risk 의 후속 cycle 답습 매핑** 부재. Provider Liquidity 합의 R-3 ⭐ verbatim:
> brief v1.1 §4.1·§3.2·§7.1 본문 머리에 "본 4 수준 framing = brief v1 의 임시 framing. ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. **본 cycle 합의 결과에 따라 채택/대안 framing 자격 평가 의무. 자동 채택 0건**" 명문 추가

본 cycle 답습 미완 — "자동 채택 0건" 명문 부재.

**처리**: brief v1.1 §4.5 본문 머리에 verbatim 추가:
> "본 §4 5축 framing = brief v1 임시 framing. ADR-011·헌법·MVP-1 합의·메모리 본문 정의 부재. **본 cycle 합의 결과에 따라 채택/대안 framing 자격 평가 의무. 자동 채택 0건** (Provider Liquidity 합의 R-3 답습 강한 변형)."

추가 §9.5 신규 차단 행:
> "§9.5 본 brief 의 5축 framing self-citation anchor 차단 — §4 5축 framing 이 후속 cycle 정정 *진입 근거* 가 되는 *de facto* 압력 0건. 5축 영구 정착 자격 0 (R-12 + R-29 통합)."

### R-3 — Phase 3 합의 R-5 (framing 약화) 답습 의무 누락 (B-B6 + C-R5 통합)

**근거**: brief v1 §0.1 line 10 답습 명시 = **R-3 + R-4 + R-6 답습**, **R-5 (framing 약화) 명시 누락**. Phase 3 합의 R-5 = framing 약화 + 단정 표현 제거 패턴 = 4 가족 분류 framing 자체에 직접 적용 자격.

**처리**: brief v1.1 §0.1 line 10 verbatim:
> "R-3 (window bias) + R-4 (분기점 라벨 anchor effect) + **R-5 (framing 약화 + 단정 표현 제거)** + R-6 (PASS/FAIL framing 금지)"

§4.5 + §8 정직성 항목 10 본문에 R-5 인용 추가.

### R-4 — §4.3 (α) "가족 내부 한정" 본질 약화 risk 차단 명문 부족 (B-B1, Provider Liquidity 합의 R-10 답습 미완)

**근거**: brief v1 §4.3 line 320 + line 326 = (α) 분리 후보 + "Provider Liquidity 본질 약화 risk" 명문, 단 차단 강도가 §0 line 55 보다 약함. Provider Liquidity 합의 R-10 답습 = "(α) 암묵 정착 시 미끄러짐" 차단 의무.

**처리**: brief v1.1 §4.3 표 (α) 행 변경:
1. (α) 본문에 "**채택 자격 = 본질 약화 = 본 cycle 채택 자격 0** (R-10 답습 차단). 채택 자격 = 헌법급 변경 trigger + Provider Liquidity 본질 약화 = 메모리·헌법·ADR-011 line 245 관용 매핑 권위 변경 의무" verbatim 추가
2. §4.3 표 머리에 "본 4 분리 후보는 **자격 평가 only**, (α) 채택 자격 = 헌법급 trigger" 명문
3. §0 line 55 의 binary 본질 명문을 §4.3 (α) 행 *inline footnote* 형태로 self-citation anchor 약화
4. §9.1 차단 행에 "❌ §4.3 (α) 가족 내부 한정 분리 후보의 자동 채택" verbatim 추가

### R-5 — ADR-011 §2.1 "(a)~(d) 4조건" 표기 carry-over (B-B2, Provider Liquidity 합의 R-14 = R-S2 답습 미완)

**근거**: brief v1 §1.5 line 122 + §3.3 표 line 263 = "(a)~(e)" 표기. ADR-011 line 52~59 본문 verbatim = **(a)~(d) 4조건** 만. (e) = ADR-011 §2.1 *본문 외* 후속 패턴.

**처리**: brief v1.1 §1.5 + §3.3 verbatim 변경:
1. "(a)~(e)" → "(a)~(d) ADR-011 §2.1 본문 + (e) 후속 패턴 (CLAUDE.md line 223 + roadmap.md 등 정착)" 분리 명문
2. §3.3 표 (e) 행 머리에 "(e) = ADR-011 §2.1 *본문 외* 후속 패턴 인용 (R-S2 = R-14 답습)" footnote
3. §1.5 본문에 ADR-011 line 52~59 verbatim 표 직접 인용 추가
4. §10 N-신규 추가: "N (R-14 답습 carry-over): ADR-011 §2.1 본문 = (a)~(d) 4조건. (e) = 후속 패턴 모법 인용 자격."

### R-6 — MVP-1 R4 해석 명확화 vs 본문 정정 boundary 명문 부족 (B-B3)

**근거**: brief v1 §3.2 line 252~260 = R4 진술의 가족 한정 자격 평가, §7.4 (D3) = "본문 정정 0건" DEFER 옵션. 단 brief 본문 자체에 **해석 명확화 boundary 의 자동 발효 자격** 명문 부족. Provider Liquidity 합의 R-21 답습 = "MVP-1 합의 본문 정정 자격 0 (별도 cycle)" — 본 cycle 의 자동 발효 risk 명문 의무.

**처리**: brief v1.1 §3.2 표 직후 본문에 verbatim 추가:
> "**해석 명확화 boundary 명문**: 본 §3.2 표 = (1) R4 진술의 *적용 범위* 평가 only, (2) MVP-1 합의 본문 정정 자격 0 (R-21 답습 — 별도 cycle 의무), (3) 본 표 자체가 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0 (R-29 답습)."

§7.4 (D3) 행에 "해석 명확화 vs 본문 정정 boundary: (a) 해석 명확화 = 본 cycle 합의 산출 자격, brief v1.1 §3.2 추가 본문 한정 / (b) 본문 정정 = 별도 합의 cycle 의무" 분리 명문.

### R-7 — abstraction layer 교차 자격 (직교/포섭/배타) 명시 부재 + 차원 폭발 risk (C-B2 + C-S2 통합)

**근거**: brief v1 의 abstraction layer 언급 5 곳 분산 (§2.3 line 229 / §4.3 line 323 (δ) / §4.5 line 351 framing δ' / §7.1 (E) line 430 / §7.3 (K) line 446). 직교/포섭/배타 자격 평가 부재. 4 × 3+ = 12+ cell + R-11 (GGUF 가족 한정) cell ≤ 1 명문 부재.

**처리**: brief v1.1 §4 신규 §4.6 축 6 추가:
> "축 6 — abstraction layer 교차 자격 (OpenAI-compat / Ollama-compat / LiteLLM). 4 가족 분류와 (1) 직교 / (2) 상호 배타 / (3) 포섭 3 자격 평가. **본 brief 평가 = 외부 식별 추정 (직교 강한 후보, 라이브 verify 0)**. 4 × 3+ = 12+ cell 차원 폭발 risk + sub-차원 (1) tensor naming 한정 evidence (R-11 답습) cell ≤ 1 명문. 채택 자격 = 사용자 명시 + 별도 cycle (R-12 답습)."

추가 §2.3 (중첩 후보) OpenAI-compat 행 + §4.3 (δ) + §4.5 framing δ' + §7.1 (E) + §7.3 (K) 모두 cross-link 명문.

### R-8 — Phase 3 P3-F1 evidence 의 "GGUF 가족 한정" 보다 *더 좁은* 한정 명문 (A-B2)

**근거**: Phase 3 raw `2026-05-24T04-32-phase3-measure-attempt-blocked.log` line 25~32 verbatim:
> conversion/qwen.py:299-300: 새 conversion 은 .dt_bias → .dt_proj.bias 로 rename
> 결론: Ollama 가 다운로드한 GGUF = 더 오래된 conversion (ssm_dt.bias 미저장) + llama.cpp c0c7e147 (master) = 최근 코드에서 .bias 강제 required 변경

P3-F1 evidence 의 일반화 자격 = "GGUF 가족 한정" + "sub-차원 (1) tensor naming 한정" + **"1 conversion script lineage × 1 시점" 한정** 3 layer 답습 의무. **R-S1 통합 답습**.

**처리**: brief v1.1 §2.1 + §2.5 또는 §10 NOTE 표에 verbatim 추가:
> "P3-F1 evidence 일반화 자격 한정 *추가 layer*: GGUF 가족 한정 (R-11 답습) + sub-차원 (1) tensor naming convention 한정 (R-7 답습) + **conversion script lineage 시점 부정합 한정** (Ollama 보유 `30e51a7c` blob = 더 오래된 conversion vs llama.cpp `c0c7e147` master = 최근 `.dt_proj.bias` rename, `conversion/qwen.py:299-300`). 본 evidence = GGUF 가족 *본질* 부정이 아닌, *시점 부정합* finding. 가족 본질 부정 자격 평가 = (a) 다른 conversion lineage GGUF 측정 (옵션 G 답습) + (b) 다른 sub-차원 (2)~(5) 측정 + (c) 다른 시점 측정 — 3 차원 모두 충족 후 가족 본질 평가 자격 도래."

### R-9 — 가족 내부 호환성 *수학적 표현* (binary/spectrum/cell-by-cell) 자격 미평가 (A-B3)

**근거**: brief v1 §4.1 "단일 binary 호환 자격 X" 진술 PASS. 단 가족 내부 호환성의 *수학적 구조* 자격 평가 부재. binary 표현 (Phase 3 합의 R-6 PASS/FAIL framing 차단 위배 risk) / spectrum 표현 (Provider Liquidity 본질 약화 risk) / cell-by-cell 4-D 매트릭스 (R-12 답습) 3 후보.

**처리**: brief v1.1 §4.1 머리에 verbatim 추가:
> "가족 내부 호환성의 *수학적 표현* = (i) binary (각 (runtime, format) 쌍) / (ii) spectrum (0~100% partial 호환) / (iii) cell-by-cell 4-D 매트릭스 (sub-차원 (1)~(5) × 시점) 3 후보. 본 cycle = 채택 자격 0, 합의 결과의 명시 자격. **Phase 3 합의 R-6 답습 = binary 표현 채택 자격 신중**. **Provider Liquidity 본질 binary 보존 (메모리 line 7) ≠ 호환성 표현 binary 강제** — 본질 (provider 교체 자유 binary) 과 수단 (호환성 표현 구조) 분리 자격 (ADR-011 §2.1 means/ends 답습)."

### R-10 — ADR-011 §6 line 212 "Provider Liquidity 영향: 무관" 내부 비대칭 답습 (C-B3 + R-S2 통합)

**근거**: ADR-011 line 6 verbatim "**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)" + line 212 verbatim "Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관" + line 245 verbatim "제5조 **관용** (Provider Liquidity, 비협상)". ADR-011 *내부* 비대칭. **R-S2 통합 답습**.

**처리**: brief v1.1 §1.4 본문 끝에 verbatim 추가:
> "**ADR-011 §6 line 212 verbatim** (내부 비대칭 명문):
> > | Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
>
> 본 line 212 '무관' = ADR-011 *주제 범위 한정* (redaction 수단 본질 충족 한정), line 6/245 직접 권위 매핑 = ADR-011 *권위 위계 의존* (양립). 본 cycle 평가 자격 = ADR-011 *주제 범위 한정* + *권위 위계* 모두 답습 의무. **ADR-011 *내부* line 212 본문 정정 자격 0** (R-9 헌법급 변경 답습)."

§3.1 권위 매핑 표에 line 212 행 신규 추가.

### R-11 — framing β'~ε' (양자화/배포/aggregator/HW target) 상호 트레이드오프 비교표 부재 (C-B4)

**근거**: brief v1 §4.5 line 344~354 = 5 framing enum only. (1) Provider Liquidity 적용 강도 / (2) 시간축 의존성 / (3) 가족 분류 직교/포섭/배타 자격 / (4) R-11 답습 자격 / (5) 비례성 비교표 부재.

**처리**: brief v1.1 §4.5 표 다음에 5 framing × 5 평가축 비교표 신규 추가 (Agent C C-B4 표 동형 답습):

| framing | Provider Liquidity 적용 강도 | 시간축 의존성 | 가족 분류 관계 | R-11 답습 자격 | 비례성 (개인 툴) |
|---|---|---|---|---|---|
| α' (4 가족 + 시간축, 본 brief 채택) | 분리 자격 평가 framework 강 | 5번째 축으로 명시 | self | 가족 한정 명문 | 중 |
| β' (양자화) | cross-runtime 호환성 직접 ↑ | AWQ/GPTQ/EXL2 진화 ↑ | 4 가족 직교 | sub-차원 (5) 한정 ↓↓ | 저 |
| γ' (deployment) | 약함 (배포 도구 한정) | docker/k8s 진화 ↓ | 4 가족 + 배포 직교 | sub-차원 (5) 미해당 ↓ | 중 |
| δ' (aggregator abstraction) | 핵심 후보 (endpoint 추상화) | LiteLLM 진화 ↑ | 4 가족 + abstraction 직교 강한 후보 | 인터페이스 sub-차원 한정 | 고 |
| ε' (HW target) | HW vendor lock-in ↔ Liquidity 충돌 | HW SM 진화 (Blackwell) ↑ | 4 가족 × HW 부분 포섭 | sub-차원 (5) 부분 ↓ | 중 |

비교표 머리에 "외부 식별 추정 한정 (라이브 verify 0). 5 framing 우월성 단정 자격 0 (R-12 답습). 본 비교 자체가 framing α' *de facto* 압력화 = 차단 (R-29 답습)" verbatim 명문.

### R-12 — 중첩 후보 3종 (llamafile / MLC-LLM / OpenAI-compat) 분류 처리 의무 미명문 (C-B5)

**근거**: brief v1 §2.3 line 226~229 = 중첩 후보 3종 *식별* only. 처리 의무 (a) 양쪽 가족 동시 분류 / (b) 새 가족 신설 / (c) 4 가족 분류 폐기 + 다른 framing / (d) sub-차원 흡수 / (e) DEFER 5 자격 평가 미진입.

**처리**: brief v1.1 §2.3 중첩 후보 표 다음에 신규 처리 표 추가 (Agent C C-B5 표 동형):

| 중첩 후보 | 중첩 차원 | 처리 5 자격 | 본 cycle 평가 자격 |
|---|---|---|---|
| llamafile | (a) GGUF + γ' single-binary | (1) (a) sub-차원 / (2) 새 가족 / (3) 폐기 / (4) γ' 흡수 / (5) DEFER | (1) 강한 후보 (loader = llama.cpp 본문), 채택 자격 0 (R-12) |
| MLC-LLM | (c) + (d) + ε' 다중 | (1) (c)+(d) 동시 / (2) 새 가족 / (3) 폐기 / (4) ε' 흡수 / (5) DEFER | C-B1 답습 — 분류 기준 모호성 evidence, (5) DEFER 강한 후보 |
| OpenAI-compat | 4 가족 직교 abstraction layer | (1) 동시 적용 / (2) 새 가족 X / (3) 폐기 / (4) δ' 흡수 / (5) DEFER | C-B2 + R-7 답습 — 직교 강한 후보 |

표 머리에 "중첩 후보 처리 = 본 cycle 합의 input 한정. 채택·기각 자격 0 (R-12 + R-29 답습)" verbatim.

### R-13 — 메모리 본문 적용 가이드 6 항목 (line 13 "최소 2 provider always-on") 본 brief 인용 부재 (B-B5)

**근거**: 메모리 `feedback_provider_liquidity.md` line 11~17 적용 가이드 6 항목 (line 12 분기 코드 금지 + **line 13 "최소 2 provider always-on"** + line 14 OAuth 직결 금지 + line 15 depcruise 정적 검사 + line 16 검토 대상 5 + line 17 ...) 본 brief 인용 0건. line 13 = 본 cycle 4 가족 분류의 가족 다양성 vs 가족 단독 채택 자격 직접 적용.

**처리**: brief v1.1 §3.4 본문에 메모리 line 11~17 적용 가이드 6 항목 verbatim 인용 추가. §8 정직성 항목 8 본문에 "메모리 line 11~17 적용 가이드 6 항목 인용 의무" 명문. §10 N-신규: "본 4 가족 분류의 line 13 '최소 2 provider always-on' 적용 자격 평가 (가족 다양성 vs 가족 단독 채택)" carry-over.

### R-14 — Reviewer 권한 한계 7 항목 boundary 명문 부족 (B-B7)

**근거**: brief v1 §5.3 line 382~389 = Reviewer 한계 7 항목. 단 각 항목의 boundary 명문 부족 (항목 1 헌법급 amendment 별도 cycle 의무 명시 부족 / 항목 2 binary 본질 정의 답습 부족 / 항목 3 해석 명확화 boundary 부족 — R-6 답습 / 항목 6 (α)(β)(γ)(δ) 분리 후보 어느 후보든 영구 정착 자격 0 명시 부족 / 항목 7 자동 다음 단계 4 차원 분리 부재).

**처리**: brief v1.1 §5.3 7 항목 verbatim 강화 (B-B7 처리 권고 답습 1~5 항목 동형).

### R-15 — §0 "하지 않는 것" 12 항목 vs §9.1 차단 6 항목 비대칭 (R-S3 = B-S5 격상)

**근거**: Reviewer 직접 cross-check — brief v1 §0 line 46~58 (12 항목) ≠ §9.1 line 484~491 (6 항목) 1:1 매핑 부재. §0 12 항목 중 §9.1 미명시 6 항목: (1) ADR-011 amendment 자동 발의 / (2) 메모리 자동 정정 / (3) 4 가족 분류 영구 framing 정착 / (4) §3·§4 진단표 후속 cycle 정정 진입 근거화 / (5) 본 cycle 합의 결과 자동 기각 / (6) 4 가족 분류 자체의 결정 *고정* (§9.1 첫 항목 = "결정 *고정*" 만, 영구 framing 분리 부재). brief 본문 self-consistency 약화 정직성 risk. **R-S3 격상 BLOCKING**.

**처리**: brief v1.1 §9.1 차단 조건을 §0 "하지 않는 것" 12 항목과 1:1 매핑 정합화 — §9.1 12 항목으로 확장 명문.

### R-16 — 진단 의무 enum 명문 부재 (B-S6, Provider Liquidity 합의 R-19 답습 미적용)

**근거**: brief v1 §1.4 = ADR-011 line 6/245 + 헌법 5조 + ADR-011 §2.1 + 권위 한계 4 항목 매핑. 단 **진단 의무 enum 명문 부재**. Provider Liquidity 합의 R-19 답습 = 본 cycle 진단 의무 5+ 항목 enum 명문화 의무.

**처리**: brief v1.1 §1.4 본문에 진단 의무 enum 명문 추가:
> "진단 의무 enum (본 cycle): (1) ADR-011 line 6/212/245 관용 매핑 + 내부 비대칭 답습 / (2) MVP-1 R4 진술의 가족 한정 자격 평가 / (3) format 가족 vs 다른 가족 means/ends 분류 + case C/D 분기 / (4) ADR-011 §2.1 (a)~(d) 적용 자격 + (e) 후속 패턴 / (5) 4 가족 분류 framing 자체 평가 (R-3 답습)"

---

## 4. 통합 권고 (R-17 ~ R-37)

### R-17 ~ R-21 — ADR-011·헌법·MVP-1 verbatim 보강 (B-R1 ~ B-R5 + B-R8 + B-S3 + B-S4 통합)

- **R-17 (B-R1)**: §1.4 헌법 5조 line 40~46 verbatim 6 항목 ("내부 코드 신뢰" 포함) 직접 인용 추가 (5조 본문 절단 차단)
- **R-18 (B-R2 + R-5 통합)**: §1.5 ADR-011 line 52~59 verbatim 표 직접 인용 추가 (a)~(d) 4조건 본문
- **R-19 (B-R3)**: §3.3 표 (e) 행 머리에 "(e) = ADR-011 §2.1 본문 외 후속 패턴 모법 인용 (CLAUDE.md line 223 + roadmap.md 정착)" 명문
- **R-20 (B-S2)**: §0.1 선행 답습에 Provider Liquidity brief v1 (`9ed376a`, 407줄) 추가 (progression 추적 자격)
- **R-21 (B-S3)**: §0.1 line 9 답습 의무 행에 R-9 (헌법급 변경) + R-10 (binary 본질) + R-22 (Phase 3 BLOCKING 7 패턴) 추가
- **R-22 (B-S4)**: §3.2 line 248 R4 verbatim 인용 보강 — MVP-1 합의 line 63 행 전체 ("| C | 🔴 정합" 컬럼 포함) verbatim

### R-23 — §4.3 표 (β)(γ)(δ) 분리 후보 채택 자격 boundary 명문 (B-R4)

각 (β)(γ)(δ) 행 본문 머리에 채택 자격 footnote — (β) 자동 채택 자격 (binary 본질 답습) / (γ) layered = 별도 ADR 발의 / (δ) abstracted = 별도 cycle.

### R-24 — §7.1 (D) layered ADR 의 (D3)/(D4) 분기 명문 (B-R5 + C-R3 통합)

Provider Liquidity 합의 R-12 답습 — (D3) framing 비교 본문 포함 ADR / (D4) MVP-1 합의 본문 보강만 DEFER.

### R-25 — §8 정직성 항목 12 Reviewer 권한 한계 항목 7 "자동 다음 단계 진입 자격 0" 추가 (B-R6)

§8 항목 12 본문에 §5.3 항목 7 "자동 다음 단계 진입 자격 0 (R-29 + R-30 답습)" 추가.

### R-26 — §10 NOTE 표 머리에 합의 결과 신규 NOTE 등재 자격 명문 (B-R7)

"본 cycle 합의 결과 신규 NOTE 등재 자격 = 각 Agent (A/B/C) + Reviewer 통합 산출. 본 합의 산출 NOTE 후보 = N-13 ~ N-19 (Agent C 추가) + N-20 ~ N-24 (Agent B 추가) + N-S1 ~ N-S3 (Reviewer 추가)" 명문 추가.

### R-27 — §2.3 외부 식별 추정 본문에 각 runtime 내부 conversion script lineage 부재 명문 (A-R1)

각 가족 (a)~(d) 표에 "각 runtime 내부 conversion script lineage / 자체 fork 자격 = 외부 식별 0, 라이브 verify 0. 별도 cycle 의무 (옵션 G·I·K 답습)" 명문 추가.

### R-28 — §2.3 누락 후보 표에 양자화 format 직교 축 자격 명문 (A-R2)

AWQ/GPTQ/SmoothQuant = 4 가족과 직교 축 (cross-runtime 부분 호환). Q4_K_M = GGUF 한정, EXL2 = exllamav2 한정. 옵션 (L) 별도 cycle 답습.

### R-29 — 5 sub-차원 × 4 가족 적용 자격 매트릭스 carry-over (A-R3)

§4.1 표 또는 §10 N-신규 — sub-차원 (1)~(5) × 4 가족 매트릭스 작성 자격 = 별도 cycle.

### R-30 — case C (means+ends 양면) 의 4 가족 적용 자격 + case D (means ≡ ends 분리 불가) 신규 분기 carry-over (A-R4 + A-S3 통합)

§4.2 머리에 "case C 의 4 가족 *내부* 적용 시 case D (means ≡ ends 분리 불가) 분기 자격 평가 = 별도 cycle (R-21 답습)" 명문 + §10 N-신규.

### R-31 — Agent C 추가 누락 후보 7 가족 (PowerInfer / CTranslate2 / PETals / Triton / TensorRT-Model-Optimizer / 등) carry-over (C-R1)

§2.3 누락 후보 표에 "Agent C 추가 누락 후보 (외부 식별 추정 한정, 라이브 verify 0)" sub-표 추가.

### R-32 — 시간축 spec 진화 evidence (GGUF v3 / HF safetensors v2 / AWQ progression / Blackwell support / vLLM #36821) carry-over (C-R2)

§4.4 시간축 본문 후에 신규 sub-표 추가 (Agent C C-R2 표 동형). 머리에 "외부 식별 추정 한정 (라이브 verify 0). 4 가족 분류의 시간 불변성 = ↓ (spec 진화 의존)" 명문.

### R-33 — Q-A4 누락 가족 5 후보 (MLX/NIM/OpenAI-compat/RWKV/AWQ-GPTQ) 의 4 가족 분류 관계 매트릭스 명문 (A-R5)

§2.3 누락 후보 표에 "각 누락 후보의 4 가족 분류와의 관계 = (i) 가족 *내부* 확장 / (ii) 신규 가족 신설 / (iii) 직교 축" 명문 추가.

### R-34 — Phase 3 raw json/log line-level cross-check 의무 보강 (A-R6)

§6.2 또는 §8 정직성 항목 11 보강 — "각 가족 (a)~(d) 4 column 라이브 verify 0 + line-level cross-check 의무 Phase 3 raw + Provider Liquidity 합의 + 헌법·ADR-011 한정".

### R-35 — 메모리 line offset 명시 균질화 (B-S1)

§3.4 본문에 "메모리 본문 line 7 verbatim:" 형식으로 line offset 명시 — 다른 verbatim 인용 (ADR-011·MVP-1·헌법) 과 균질화.

### R-36 — Provider Liquidity 합의 NOTE 12 + 본 cycle 신규 NOTE 통합 표 정합화 (B-N3)

brief v1.1 보강 시점에 NOTE 표 v1 → v1.1 통합 정합화 의무.

### R-37 — Agent C 추가 NOTE 후보 (N-16 ~ N-19, aggregator/양자화 framework/distributed/vLLM 진화) carry-over (C-R4)

§10 NOTE 표에 Agent C 추가 7 항목 carry-over (별도 cycle 자격).

---

## 5. NOTE carry-over (N-1 ~ N-24)

> 본 cycle 합의 *후* 별도 cycle 의무 항목. Provider Liquidity 합의 NOTE 12 carry-over + 본 cycle 신규 12.

### Provider Liquidity 합의 NOTE 12 carry-over (N-1 ~ N-12)

brief v1 §10 표 12 항목 carry-over PASS — 본 합의 답습 의무 유지.

### 본 cycle 신규 NOTE 12 (N-13 ~ N-24)

- **N-13 (B-N1)**: ADR-011 §6 line 212 "Provider Liquidity 영향 무관" vs line 6/245 직접 권위 매핑 *적용 범위 boundary* 평가 cycle (별도)
- **N-14 (B-N2)**: 4 가족 × 메모리 line 11~17 적용 가이드 6 항목 = 24 cell 매트릭스 평가 cycle (별도, B-B5 답습)
- **N-15 (B-N4)**: SSM 명명법 정정 (Phase 2 F2 답습) + 본 cycle 답습 cycle (별도)
- **N-16 (B-N5)**: ADR-008 부록 B Amendment 패턴 답습 자격 (옵션 (D)/(E) 발의 시 의무)
- **N-17 (B-N6)**: 본 cycle 합의 후 사용자 명시 시점에 메모리 `feedback_provider_liquidity` 본문 line 7 "코드 변경 없이" 범위 보강 자격 (별도)
- **N-18 (C-N1)**: Agent C 추가 후보 7 가족 (PowerInfer/CTranslate2/PETals/Triton/TensorRT-Model-Optimizer/MLX/NIM) 라이브 verify cycle (별도)
- **N-19 (C-N2)**: 4 가족 분류 *축* 자체 평가 cycle (R-1 답습 후속)
- **N-20 (C-N4)**: ADR-011 §6 line 212 *주제 범위 한정* + line 6/245 *권위 위계 의존* 통합 답습 cycle (R-10 답습 후속)
- **N-21 (C-N5)**: framing β'~ε' 5 비교표 후속 (다른 framing 채택 자격 별도 cycle, Provider Liquidity 합의 (K) 옵션 답습)
- **N-22 (C-N7)**: spec 진화 evidence (GGUF v3 / HF safetensors v2 / AWQ / Blackwell / vLLM #36821) 라이브 verify cycle (별도, R-32 답습 후속)
- **N-23 (C-N8/N9/N10)**: aggregator runtime (Triton·OpenAI-compat) + 양자화 framework (TensorRT-Model-Optimizer) + distributed inference (PETals·Hivemind) 4 가족 직교 자격 평가 cycle (별도)
- **N-24 (C-N12)**: 본 4 가족 분류 영구 framing 정착 차단 (R-12) carry-over 의무가 후속 framing cycle 마다 답습 — Provider Liquidity 합의 R-29 (de facto 압력 차단) 답습 패턴

---

## 6. 본 합의 자체의 자격 한계 (Reviewer 정직성)

### 6.1 본 합의가 검토한 source

- brief v1 (`f305174`, 556줄, 본 cycle 분석 대상) 전체
- Provider Liquidity 합의 보고서 (`a9e1e88`, 301줄) 전체
- Provider Liquidity brief v1.1 (`8ae1ab6`, 518줄) 본문
- Phase 3 합의 보고서 (`e76acc8`, BLOCKING 7) grep
- Phase 3 raw 2 파일 line-level verbatim (`2026-05-24T04-32-phase3-measure-attempt-blocked.log` line 9·12·20~32 + `phase3-summary.json` 인용)
- 헌법 본문 line 35~79 (제5조 + 제8-2조)
- ADR-011 본문 line 6 + line 52~59 + line 212 + line 245 verbatim 직접 확인
- MVP-1 합의 line 63 R4 verbatim
- 메모리 `feedback_provider_liquidity.md` 전체 19줄 (system reminder 19일+ stale verify)
- 3 Agent 보고서 본문 전체 (Agent A 보고서 + Agent B 보고서 + Agent C 보고서)

### 6.2 본 합의가 검토하지 못한 source

- MVP-1 design brief v2 (`15beb33`) 본문 전체 (간접 인용 한정)
- Phase 3 raw 17 파일 중 본 합의 사용 2 파일 외 15 파일
- ADR-011 §2.2~§2.4 + §3·§4·§5·§7·§8.2~§8.4
- `system-identity-prequel.md` §3 (ADR-011 line 6 상위 권위)
- 메모리 다른 4 항목 (`project_jarvis_local_boss_direction` / `feedback_proportionate_security_personal_tool` / `feedback_staged_consensus_workflow` / `project_minimize_user_intervention`) 본문 전체

### 6.3 본 합의의 자격 boundary (영구 답습 7 항목)

1. ❌ **ADR-011 §6 본문 정정 자격 0** (헌법급 amendment cycle 의무 = 별도 합의 cycle + 풀 3+1 + 사용자 명시 + ADR amendment 발의 자격 평가)
2. ❌ **Provider Liquidity 본질 약화 자격 0** (binary 본질 유지 — 메모리 line 7 verbatim "코드 변경 없이" + ADR-011 line 245 verbatim "제5조 관용 (Provider Liquidity, 비협상)" 직접 권위 매핑 답습)
3. ❌ **MVP-1 합의 본문 정정 자격 0** (별도 cycle, 해석 명확화 vs 본문 정정 boundary)
4. ❌ **헌법 본문 정정 자격 0** (별도 cycle)
5. ❌ **메모리 본문 정정 자격 0** (본 cycle 합의 결과의 메모리 갱신 자격은 별도 사용자 명시)
6. ❌ **4 가족 분류 자체의 영구 framing 정착 자격 0** (R-12 답습) + (α)(β)(γ)(δ) 분리 후보의 어느 후보도 영구 정착 자격 0
7. ❌ **자동 다음 단계 진입 자격 0** (R-29 + R-30 답습 통합). 자동 다음 단계 = (a) commit·push / (b) brief v1.1 보강 / (c) 메모리 갱신 / (d) 다른 cycle 진입 4 차원 모두 분리 의무

### 6.4 Reviewer 정직성

- 본 합의 = brief v1 + 3 Agent 보고서 + 선행 답습 8 문서 + Phase 3 raw 2 파일 + 헌법·ADR-011·MVP-1 합의·메모리 cross-check
- **결정 *고정* 0건** — 본 합의 자체가 M3·M4 결정 / MVP-1 합의 본문 정정 / ADR-011 amendment / 헌법 amendment / 메모리 갱신 자격 0
- **자동 정정 0건** — brief v1.1 보강은 본 합의 산출 BLOCKING 본문 verbatim 반영 의무이나, 다른 source (MVP-1 합의·헌법·ADR-011·메모리) 본문 자동 정정 0
- **본 보고서가 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0** (R-29 답습) — 후속 cycle 정정 자격 = 사용자 명시 + 별도 합의 cycle 의무
- **본 합의의 *기각* 자격도 자동 발효 0건** (R-30 답습)

---

## 7. 다음 단계 (자동 진입 0건)

1. 본 합의 보고서 commit·push (사용자 명시 후)
2. **brief v1 → v1.1 보강** — BLOCKING 16 verbatim 본문 직접 반영 100% + 권고 21 본문 직접 반영 또는 §10 NOTE carry-over + §11 변경 일람 표 신규
3. **세션 정리 + CONTEXT.md + INDEX.md + commit·push**

각 단계 = 사용자 명시 의무 ([[feedback_staged_consensus_workflow]] 답습). 자동 진입 0건.

**합의 *후* 결정 자격**: brief v1.1 §7 옵션 (A)~(M) + DEFER (D1)~(D4) 중 사용자 명시.

---

**End of consensus report** — 작성 2026-05-24, 3 Agent 병렬 독립 PASS + Reviewer 단독 격상 3건 (R-S1·R-S2·R-S3) + 정합성 매트릭스 + BLOCKING 16 + 권고 21 + NOTE 24 + 기각 0
