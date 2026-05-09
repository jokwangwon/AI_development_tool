# Agent B — 품질/안전성 검증가 — G2 GP-5 2차 PoC depcruise rule

> **세션**: 2026-05-10 (Group A 2차 PoC — 풀 3+1 합의 입력)
> **에이전트**: Agent B (품질/안전성 검증가) — 독립 분석
> **핵심 질문**: "안전하고 견고한가? 답습 충실한가? 보안 이득 vs 도입 비용?"
> **답습 권위**: ADR-011 §2.1 (a)~(e) + ADR-009 C-N §2.3+§5 + ADR-008 부록 C + ADR-012 §원칙 5/6 + 외부 LLM 답습 (Claude L39/L51/L76)
> **분석 대상**: `docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md` 7항목 + 4 도구 옵션 (T-1~T-4)
> **편향 통제**: 다른 Agent 출력 미참조. Reviewer 사전 권고 (T-2) 답습 *금지* — 독립 분석.

---

## 0. 분석 메타

본 분석의 *출발 가정*:

1. 1차 PoC (commit a3693a0) = Layer 1 형식 차단 1차 시제 PASS (fixture 5/5, FP=0/FN=0)
2. 2차 depcruise rule = *추가 enforcement layer* 수단 결정 — 1차 *중복* + transitive *추가* 두 차원
3. 본 분석 = *품질/안전 권위 입력* 한정 (도구 PASS 결정권 없음)

핵심 출발점: §9.3 의 *명시 도구 (depcruise)* 답습 vs *시제 의도 (allow path / forbidden path)* 답습 — 어느 차원이 우월한가?

---

## 1. 답습 충실성 평가

### 1.1 §9.3 본문의 *수단 미확정* 단서

§9.3 본문 = `// .depcruise.cjs (개략, P5 문서로 상세화)` + `@anthropic-ai`/`@openai` (JS SDK — Python repo 무관) 혼재.

- **시제 의도** (강한 답습): `from.pathNot` = facade.py 단일 허용 / `to.path` = 5종 forbidden
- **명시 도구** (약한 답습): `.depcruise.cjs` 파일명 + JS DSL — *"개략, P5 문서로 상세화"* 단서로 **수단 미확정 명시**

### 1.2 ADR-009 C-N §5 "Layer 1 모법" 의미

> Layer 1 (코드 lock-in 차단) — 본 ADR-009 §2.2 + G2 GP-5 (depcruise 룰) + §9

핵심: "depcruise 룰" = *예시 표현*. Layer 1 모법 ADR = ADR-009 §2.2 *자체*. §9 인용은 §9.1+§9.3+§9.4 *전체* (§9.4 AST scanner = depcruise 가 못 잡는 영역). **"depcruise 가 *정확히* 그 도구여야 한다"는 명시 미발화**.

### 1.3 답습 충실성 비교 매트릭스

| 차원 | T-1 (depcruise JS) | T-2 (import-linter Python) | T-3 (ruff custom rule) | T-4 (1차 AST scanner 확장) |
|----|----|----|----|----|
| §9.3 명시 도구 (`.depcruise.cjs`) 답습 | ✅ 직접 답습 | ⚠️ 시제 의도 답습 (도구 다름) | ⚠️ 시제 의도 답습 (도구 다름) | ⚠️ 시제 의도 답습 (도구 다름) |
| §9.3 시제 의도 (`from.pathNot` / `to.path`) 답습 | ✅ | ✅ | ✅ | ✅ (이미 1차 PoC 에서 답습) |
| Python repo 정합성 | ❌ JS 도구 | ✅ Python 공식 | ✅ Python 공식 | ✅ stdlib |
| ADR-009 §5 Layer 1 모법 답습 | ✅ (예시 답습) | ✅ (시제 답습) | ✅ (시제 답습) | ✅ (이미 답습 중) |
| §9.3 본문 *"개략, P5 문서로 상세화"* 단서 | 미명시 → JS 그대로 | 명시 답습 → 도구 변경 | 명시 답습 → 도구 변경 | 명시 답습 → 도구 변경 |

**판정**: §9.3 *"개략, P5 문서로 상세화"* 단서 답습 시 **시제 의도 답습 우월** (수단 변경은 P5 단계에서 정상). T-1 명시 도구 답습은 *형식적 1점 / 실질적 0점* (§9.3 단서와 충돌 가능). **결론**: §9.3 *시제 의도* 답습이 더 *무게있는 답습*.

---

## 2. ADR-011 §2.1 (a)~(e) 5조건 매트릭스

본 매트릭스는 *각 옵션이 ADR-011 §2.1 5조건을 충족할 가능성*을 평가. 5/5 충족 시 도구 도입 적격.

### 2.1 (a)~(e) 차원별 평가 요약

**(a) 안전 결과 본질**: 모든 옵션 = "provider lock-in 회피" 동일 식별 가능 → 4/4 충족.

**(b) 수단 변경 사전 인지**:
- T-4 (자기 확장, *최소*) < T-2/T-3 (Python ecosystem 내) < T-1 (Node 도구 도입, *최대*)

**(c) FP/FN 측정 가능성**:
- T-1 = Python 비공식 (TypeScript-Estree 기반) → **FN 본질적 잔존** ⚠️
- T-2 = Python 공식 + 성숙 fixture 패턴 → 충족도 *최고*
- T-3 = ruff AST 기반 → 충족
- T-4 = 자체 transitive 구현 → 자체 검증 부담

**(d) 폐기 경로**: T-2 ≈ T-3 (pip dep 1) < T-4 (자체 코드) ≈ T-1 (Node 도구체인 제거)

**(e) 외부 검증 가능성**: T-1 ≈ T-2 (declarative config) < T-3 (custom plugin 코드) < T-4 (자체 Python 코드)

### 2.2 5조건 종합 매트릭스

| 옵션 | (a) | (b) | (c) | (d) | (e) | 종합 | 충족 여부 |
|---|---|---|---|---|---|---|----|
| **T-1** (depcruise) | ✅ | ⚠️ | ⚠️ FN 잔존 | 中 | ✅ | **3.5/5** | 풀 3+1 + (b)/(c) 보강 합의 필요 |
| **T-2** (import-linter) | ✅ | ✅ | ✅ | ✅ | ✅ | **5/5** | 풀 3+1 만으로 적격 |
| **T-3** (ruff custom) | ✅ | ⚠️ | ✅ | ✅ | ⚠️ | **4/5** | 풀 3+1 + ruff 사전 도입 합의 필요 |
| **T-4** (AST scanner 확장) | ✅ | ✅ | ⚠️ | 中 | ⚠️ | **3.5/5** | 풀 3+1 + 자체 검증 부담 합의 필요 |

**판정**: ADR-011 §2.1 5조건 *원칙적* 충족도는 **T-2 > T-3 ≈ T-4 > T-1** 순서.

⚠️ **본 매트릭스는 *권위 입력* 만** — 사용자 명시 결정 권한 침해 *없음*. 단순히 *5조건 충족도* 의 객관적 비교.

---

## 3. 보안 이득 vs 도입 비용 매트릭스

### 3.1 1차 AST scanner 대비 중복/추가 가치

| 패턴 | 1차 AST | 2차 depcruise | 차원 |
|---|---|---|---|
| direct/from import | ✅ | ✅ | **중복** |
| dynamic importlib / `__import__` / model branch | ✅ | ❌ (본질적 한계) | 추가 가치 0 |
| **transitive import (A → B → openai)** | ❌ | ✅ | **유일한 추가 가치** |

**추가 가치 = transitive import 차단 1건 한정**.

### 3.2 transitive 차단의 *실제* 보안 이득

**현실 진단**:
1. 본 repo `src/` *0건* (메타-템플릿) → 현 시점 검사 대상 0건
2. 미래 src/ 도입 시 — facade.py 외부 모듈은 *1차 AST scanner 가 이미 직접 import 차단* → transitive 추가 가치 = *facade.py 자체의 transitive 의존* 한정
3. facade.py = §4.1 답습 *얇은 100 LOC* → transitive 의존 발생 영역 *극히 좁음*

**결론**: 추가 보안 이득 영역 *극히 좁음 + 현 시점 절대값 0*.

### 3.3 도입 비용 정량 평가

| 옵션 | dev-dep 추가 | CI 시간 증가 | 학습 비용 | 유지보수 비용 |
|---|----|----|----|----|
| T-1 (depcruise) | 1 (npm) + Node runtime | +30~60s (setup-node + npm install) | 中 (npm + cjs DSL) | 中 (Node 도구체인) |
| T-2 (import-linter) | 1 (pip) | +5~15s (이미 Python 환경) | 低 (config TOML/INI) | 低 |
| T-3 (ruff custom) | 1 (pip) — ruff 가 미도입 시 | +5~10s (ruff 자체) | 中 (ruff plugin Python 코드) | 中 |
| T-4 (AST scanner 확장) | 0 (자체 코드) | +0s (1차 동일 환경) | 高 (transitive 분석 자체 구현) | 高 (자체 코드 유지보수) |

### 3.4 보안/비용 비율 매트릭스

본 비율 = (추가 보안 이득) / (도입 비용)

| 옵션 | 추가 보안 이득 | 도입 비용 | 비율 |
|---|----|----|----|
| T-1 (depcruise) | transitive 1건 (Python 비공식 — FN 잔존) | 高 (Node + npm + cjs) | **低** |
| T-2 (import-linter) | transitive 1건 (Python 공식) | 低 (pip dep 1) | **中** |
| T-3 (ruff custom) | transitive 1건 (Python AST) | 中 (ruff plugin) | **中** |
| T-4 (AST scanner 확장) | transitive 1건 (자체 구현 — 자체 검증 부담) | 中 (자체 코드) | **低~中** |

**판정**: T-2 가 보안/비용 비율 *최고*. T-1 은 도입 비용이 가장 큰데 *Python 비공식* FN 잔존으로 보안 이득까지 *불완전* → 비율 *최저*.

⚠️ **단, transitive 의존 자체가 *현 시점 검사 대상 0건*** (src/ 미존재) — 모든 옵션의 *현 시점 보안 이득 절대값 = 0*. *미래 대상* 한정 룰 정의 시제.

---

## 4. depcruise 본질적 한계 3종 책무 분담 평가

외부 LLM 답습 (`docs/external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 / L51) 의 *3종 한계* 가 본 PoC 의 *책무 범위* 와 어떻게 관계되는가.

### 4.1 3종 한계 책무 분담 종합 매트릭스

| 한계 | 1차 AST | 2차 depcruise | 3차 grep | Runtime egress (R-2/R-4.1) | 라운드트립 (G4 §4.6) | 책무 누락? |
|---|---|---|---|---|---|---|
| 동적 import (`importlib` / `__import__`) | ✅ 답습 | ⛔ 본질적 한계 | — | ✅ | — | **0건** (1차가 이미 잡음) |
| URL 하드코딩 (`https://api.anthropic.com/...`) | ⚠️ 미적용 | ⛔ 본질적 한계 | ✅ scope §3.2 분리 | ✅ | — | ⚠️ **현 시점 누락 — 2차 depcruise 가 해소하지 않음** |
| 의미적 lock-in (출력 포맷 가정) | — | ⛔ 본질적 한계 | — | — | ✅ | **0건** (G4 §4.6 분리 명시) |

**판정**: 동적 import / 의미적 lock-in 은 책무 *명확 분리* (누락 0건). 단 **URL 하드코딩 차단의 *현 시점 누락* 은 2차 depcruise 도입 *여부와 무관*** — 별도 3차 grep 룰 합의 필수 (외부 LLM 답습 L39 — "depcruise 는 import 만 검사, URL 문자열 검사 못 함").

---

## 5. FP / FN 위험 평가

### 5.1 False Positive — false block 위험

**시나리오**: depcruise rule 이 *정상 코드* 를 *위반* 으로 오인 → CI 차단 → 사용자 경험 손실.

| 옵션 | FP 위험 시나리오 | 영향도 | 완화 방법 |
|---|---|---|---|
| T-1 (depcruise) | Python `.py` 동적 import 분석 비공식 — false alarm 가능 | 高 | scope §1.2 옵션 A (src/ 만) + fixture 양방향 |
| T-2 (import-linter) | TOML 패턴 매칭 정상 → FP 낮음 | 低 | fixture 양방향 |
| T-3 (ruff custom) | ruff plugin 자체 버그 → FP 가능 | 中 | fixture + ruff 자체 검증 |
| T-4 (AST scanner 확장) | 1차 답습 + transitive 자체 구현 시 FP 가능 | 中 | fixture + 자체 검증 부담 |

**판정**: T-2 가 FP 위험 *최저*. T-1 의 *Python 비공식* 위험은 *false block* 까지 *직접 도달 가능* — CI 가 정상 코드를 차단하는 사용자 경험 손실 *위험 큼*.

### 5.2 False Negative — false sense of security 위험

**외부 LLM 답습 (Claude L76)**:

> "계산적 메커니즘 (regex, depcruise, SQL trigger) 은 false negative 시 조용히 실패합니다. 추론적 보조 (Reviewer pattern matching, 합의 검토) 는 더 비싸지만 unknown unknowns 에 강합니다."

| 옵션 | FN 위험 시나리오 | 영향도 | 완화 방법 |
|---|---|---|---|
| T-1 (depcruise) | Python `.py` 비공식 — *조용한 실패* 가능 | **高** | 1차 AST scanner 가 *보완* (이중 layer) |
| T-2 (import-linter) | Python 공식 — FN 본질 가능성 낮음 | 中 | 1차 AST scanner 가 *보완* |
| T-3 (ruff custom) | ruff AST 기반 — FN 본질 낮음 | 中 | 1차 AST scanner 가 *보완* |
| T-4 (AST scanner 확장) | 자체 구현 — 검증 부담 자체가 FN 영역 | 中 | 외부 LLM 검증 (e) 보강 |

**판정**: 모든 옵션이 1차 AST scanner 와의 *이중 layer* 로 FN 영역에서 *상호 보완*. 단 T-1 의 *Python 비공식 + 조용한 실패* 는 가장 위험.

### 5.3 외부 LLM 답습 (L76) — 계산적/추론적 비율

L76: "*계산적 메커니즘은 FN 시 조용히 실패. 추론적 보조는 unknown unknowns 에 강함*". 본 GP-5 = *계산적 우위* 적합 영역 (import 차단 = 형식적 패턴) → L76 답습 *위반 없음*. 단 FN 영역 보완 = *추론적 보조 layer* (§9.5 코드 리뷰 + G4 §4.6 라운드트립 + 외부 LLM 정기 검증) *별도 유지* 의무.

---

## 6. 1차 PoC R-4 권고 재검토

### 6.1 1차 PoC 합의 보고서 R-4 원문

`docs/review/3plus1-consensus-2026-05-09-g2-gp5-poc-poc1-reviewer-only.md` §3.3:

| # | 권장 | 우선순위 | 처리 시점 |
|---|------|--------|----------|
| R-4 | depcruise rule 도입 (별도 합의) | HIGH | 2차 |

### 6.2 R-4 *실질 의도* 해석

R-4 본문 = "depcruise rule" 명시. *맥락* = §9.3 *시제 의도* 답습 (transitive 차단 추가 layer). *명시 도구* 강제 아님.

| 해석 차원 | R-4 의도 |
|---|---|
| 표면 텍스트 | "depcruise rule" |
| 실질 의도 | "transitive 의존 차단 추가 layer" (§9.3 시제 답습) |

**판정**: T-2 / T-3 / T-4 채택해도 R-4 권고 *충족*. *명시 도구* 답습 강제 아님.

### 6.3 R-4 정합성 추가 조건

1. 현 시점 검사 대상 0건 → R-4 HIGH = *future-proof 룰 정의* 한정. 즉시 enforce 효과 0
2. scope §0.1 도구 정합성 모순 → T-1 채택 시 *답습 충실성 형식적 답습* 한정
3. 풀 3+1 합의 필수 (Node 도입 = T2 영역 가능)

---

## 7. 6 금지목록 위반 위험 매트릭스

각 옵션 진행 시 사용자 명시 6 금지의 *우회/위반* 가능성.

| # | 금지 항목 | T-1 | T-2 | T-3 | T-4 |
|---|---|---|---|---|---|
| 1 | G2 GP-5 최종 PASS 선언 | ⚠️ 도구 도입 = *PASS 로 해석될 위험* | ⚠️ 동상 | ⚠️ 동상 | ⚠️ 동상 |
| 2 | G2 전체 Implementation/Runtime PASS 선언 | ⚠️ *부분 충족 시제* 한정 명시 필수 | ⚠️ 동상 | ⚠️ 동상 | ⚠️ 동상 |
| 3 | Hermes PMO 격상 선언 | ✅ 무관 | ✅ 무관 | ✅ 무관 | ✅ 무관 |
| 4 | 실제 provider API key 사용 | ✅ 무관 | ✅ 무관 | ✅ 무관 | ✅ 무관 |
| 5 | 실제 외부 API 호출 | ✅ 무관 | ✅ 무관 | ✅ 무관 | ✅ 무관 |
| 6 | Provider 구현 자체 변경 | ✅ 무관 | ✅ 무관 | ✅ 무관 | ✅ 무관 |

**판정**: 6 금지목록 #3~#6 은 *모든 옵션* 무관. 위반 위험은 #1 (PASS 선언 *해석 위험*) 과 #2 (Runtime PASS *해석 위험*) 한정.

### 7.1 #1 / #2 위험 완화 — 합의 보고서 명시 답습 필수

> "본 2차 PoC = G2 GP-5 *부분 충족 시제* 한정. G2 GP-5 최종 PASS 선언 / Implementation/Runtime PASS 선언 권한 없음."

ADR-008 부록 C C.5 답습 — Implementation/Runtime PASS = **2/4** (G1b + GP-1 만), G2 GP-2~GP-6 = Pending. 본 2차 PoC = *Layer 1 추가 강화 시제* 한정.

### 7.2 T-1 부수적 위험 — Node 도입 자체

T-1 채택 시 Node 환경 도입 자체가 ADR-011 §2.4 *T2 사용자 승인 영역* 또는 *T3 자동 금지 영역* 가능 (Harness Gates 정의 변경 차원). **풀 3+1 합의 + 사용자 명시 결정 *추가* 의무**.

---

## 8. 권고

### 8.1 옵션 권고 (Agent B 독립 판정)

본 Agent B 의 5조건 매트릭스 (§2) + 보안/비용 비율 (§3) + FP/FN 위험 (§5) 종합 권고:

| 순위 | 옵션 | 권고 사유 |
|---|---|---|
| **1** | **T-2 (import-linter)** | 5조건 5/5 충족 + Python repo 정합 + FP/FN 최저 + 폐기 비용 최저 |
| 2 | T-3 (ruff custom) | 5조건 4/5 + ruff 사전 도입 시 비용 낮음 |
| 3 | T-4 (AST scanner 확장) | 5조건 3.5/5 + 자체 코드 부담 |
| **4 (비권고)** | **T-1 (depcruise)** | Python 비공식 + Node 도입 비용 高 + FN 잔존 + 보안/비용 비율 *최저* |

⚠️ **본 권고는 *Agent B 의 품질/안전 차원* 한정** — 사용자 명시 결정 권한 침해 *없음*. Reviewer 가 *최종 도구 선택 결정* 권한.

### 8.2 추가 조건

본 2차 PoC 진행 시 *공통* 추가 조건:

| # | 조건 | 사유 |
|---|---|---|
| C-1 | 본 2차 PoC = *G2 GP-5 부분 충족 시제* 한정 명시 — 최종 PASS 선언 권한 없음 | 6 금지목록 #1 |
| C-2 | Implementation/Runtime PASS 자동 선언 미발생 명시 (ADR-008 부록 C C.5 답습) | 6 금지목록 #2 |
| C-3 | scope §1.2 옵션 A (src/ 만) 채택 — 현 시점 검사 대상 0건 명시 (future-proof 룰 정의 한정) | FP 위험 최소화 |
| C-4 | 1차 fixture 재사용 + (선택) `transitive_import.py` 1건 추가 한정 | scope §5.2 답습 |
| C-5 | scope §6 CI-A 채택 — 1차 workflow 안 step 추가 (evidence 연속성) | scope §6.1 답습 |
| C-6 | depcruise 본질적 한계 3종 (동적 import / URL / 의미적 lock-in) 의 *책무 분담 명시* — 본 PoC 책무 범위 외 명시 | §4.4 답습 |
| C-7 | 외부 LLM 답습 (Claude L76) — 계산적 메커니즘 FN 위험 명시 + 추론적 보조 layer 별도 유지 답습 | §5.3 답습 |
| C-8 | URL 하드코딩 차단은 본 PoC 외 *3차 grep 분리* 합의 필수 — 본 2차 PoC 도입으로 그 책무 *해소되지 않음* 명시 | §4.2 답습 |

T-1 채택 시 *추가* 조건:

| # | 조건 | 사유 |
|---|---|---|
| C-9 (T-1 한정) | Node 환경 도입 자체의 T2/T3 영역 검토 + 사용자 명시 결정 | §7.3 답습 |
| C-10 (T-1 한정) | Python `.py` 동적 import 분석의 *비공식 한계* 명시 + FN 영역 보완 매트릭스 작성 | §5.2 답습 |

### 8.3 RED FLAG (위험 명시)

본 분석에서 발견한 *RED FLAG* — 풀 3+1 합의 시 반드시 검토:

#### RED FLAG 1: T-1 채택 시 *답습 충실성 형식적 1점 / 실질적 0점*

§9.3 본문 자체가 *"개략, P5 문서로 상세화"* 명시 — *명시 도구 (depcruise)* 답습 강제 아님. T-1 채택 시:
- 형식적 답습: ✅ (".depcruise.cjs" 파일명 일치)
- 실질적 답습: ❌ (Python repo 에 JS 도구 도입 = §0.1 도구 정합성 모순 자체)

**위험**: T-1 채택 = *답습 충실성* 의 *기계적 답습* 으로 해석되나, 실질적으로 §9.3 의 *시제 의도* 답습 (T-2/T-3) 보다 *덜 충실*.

#### RED FLAG 2: 현 시점 검사 대상 0건 — *PoC 자체의 의미*

scope §1.1 진단:

> 현 시점 검사 대상 = **0건** (실제 application runtime 코드 미존재).

**위험**: 본 2차 PoC 의 *즉시 보안 이득* = 0. *future-proof 룰 정의 시제* 한정. 그 *형식적 시제* 자체가 *G2 GP-5 PASS 로 해석* 되면 6 금지목록 #1 위반 우회.

→ 합의 보고서 §C-1 답습 명시 필수.

#### RED FLAG 3: depcruise 본질적 한계 — URL 하드코딩 차단 부재

scope §3.2 + §4.2 답습:

| 한계 | 본 PoC 가 해소? |
|---|---|
| 동적 import | ✅ 1차 AST scanner 가 *이미* 답습 |
| URL 하드코딩 | ❌ **본 2차 PoC 도입으로 해소 *되지 않음*** |
| 의미적 lock-in | ❌ G4 §4.6 라운드트립 별도 합의 |

**위험**: 본 2차 PoC 채택 시 사용자가 "GP-5 enforcement 강화 완료" 로 *과대 해석* 가능 → URL 하드코딩 차단의 *부재* 가 *조용히 통과* (FN 잔존).

→ §C-8 답습 명시 필수.

#### RED FLAG 4: T-1 채택 시 5 layer 다중 차단 *호스트 OS 의존* 강화

ADR-008 부록 C C.4 의 *5 layer 다중 차단* 답습:

| Layer | 차단 매커니즘 |
|---|---|
| 5 | filesystem ACL (governance-preconditions.md / Evidence Ledger 등) |

T-1 채택 시 Node 환경 + npm cache + node_modules 가 *호스트 OS* 에 추가 → 외부 LLM 답습 (Claude §2.3 SPOF):

> 핵심 메커니즘은 모두 동일 호스트 OS 권한 모델에 의존합니다. 컨테이너 escape, host 측 git hook 비활성화, IDE GUI를 통한 직접 편집 등은 차단되지 않습니다.

**위험**: T-1 = *공격 표면 확대* (Node 도구체인 추가) — 본 2차 PoC 의 보안 이득 (transitive 1건 차단) 보다 *부수적 위험* 이 *클 수 있음*.

#### RED FLAG 5: 1차 PoC R-4 *HIGH* 권고의 *과대 해석* 위험

1차 PoC 합의 §3.3 R-4 (HIGH) 의 *맥락* 은 *2차 시제 처리 의무* 한정. T-1 채택 강제 아님. R-4 *HIGH* 가 *T-1 채택 의무* 로 해석되면 풀 3+1 합의 권한 침해.

→ §6 답습 명시 필수.

#### RED FLAG 6: G2 §1.2.6 P10 (Evidence Forgery) 와의 cross-check 누락

본 scope 가 ADR-012 §원칙 5/6 + G2 §1.2.6 P10 cross-reference 명시 미발화. depcruise rule 도입 시 *Evidence Ledger* 에 어떤 entry 가 어떤 *agent* 필드 (provider-neutral) 로 기록되는가 — *명시 미발화*.

→ 합의 보고서에 *evidence ledger entry 형식* 답습 명시 필수.

### 8.4 본 분석의 *영역 외*

본 Agent B 분석은 다음을 *제안하지 않음* (편향 통제):

1. ❌ Hermes PMO 격상 (ADR-008 부록 C 답습)
2. ❌ G2 GP-5 최종 PASS 선언 (사용자 명시 답습)
3. ❌ Implementation/Runtime PASS 자동 선언 (1차 PoC 합의 §4.2 답습)
4. ❌ Provider 구현 자체 변경 (사용자 명시 답습)
5. ❌ ADR 본문 자동 변경 (T3 영역, ADR-011 §2.4 답습)
6. ❌ Tier-2/3 catalog 자동 확장 (사용자 명시 답습)
7. ❌ 기술적 구현 세부 (Agent A 영역)
8. ❌ Reviewer 사전 권고 (T-2) 답습 (편향 방지)

본 분석은 *권위 입력 한정*. 풀 3+1 합의의 Reviewer 가 *최종 합의 도출* 권한.

---

## 9. 합의 입력 메타

| 항목 | 값 |
|------|---|
| 작성 주체 | Agent B (품질/안전성 검증가) |
| 분석 형식 | 독립 분석 (다른 Agent 출력 미참조) |
| 답습 권위 누락 | 0건 |
| 신규 정책 발명 | 0건 |
| 사용자 명시 위반 | 0건 |
| 6 금지목록 위반 | 0건 |
| ADR-011 §2.1 5조건 매트릭스 | 5/5 (T-2) / 4/5 (T-3) / 3.5/5 (T-1, T-4) |
| RED FLAG | 6건 명시 |

본 분석은 풀 3+1 합의 입력 *3 의견 중 1*. Reviewer 가 Agent A (구현) + Agent B (품질) + Agent C (대안) 교차 비교 후 *최종 합의 도출*.

---

## 10. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차) | 신규 작성 | Agent B 품질/안전성 독립 분석 — G2 GP-5 2차 PoC depcruise rule |
