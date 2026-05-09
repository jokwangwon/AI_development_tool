# Agent C — 대안 탐색가 — G2 GP-5 2차 PoC depcruise rule

> **작성**: 2026-05-10 (Group A 2차 — 풀 3+1 합의 입력 #3 of 3)
> **관점**: 대안 탐색가 (Alternatives Explorer) — *근본 의문 + 반대 방향 적극 검토*
> **답습 절대성**: ❌ Hermes PMO 격상 / G2 GP-5 최종 PASS / Implementation·Runtime PASS / Provider 구현 변경 *제안 금지*. ❌ ADR 본문 자동 변경 / Tier-2·3 카탈로그 확장 / ADR-013·014 자동 발행 *제안 금지*. ✅ *Reviewer 사전 권고 (T-2)* 그대로 따르지 않음 — *반대 방향 (보류 / T-9 / T-10)* 적극 검토.
> **Reviewer 영역 침범 금지**: 본 보고서는 *대안 후보 목록 + 트레이드오프 평가* 만. 최종 결정은 Reviewer.

---

## 0. 핵심 결론 선언 (대안 탐색가 입장)

본 합의에서 *가장 강하게 누락된 선택지* 는 다음 두 가지다:

1. **2차 자체 보류** — 1차 PoC 가 *src/* 미존재 환경에서 이미 5/5 패턴 검출에 성공한 상태에서, depcruise 가 *추가* 잡는 가치(=transitive 의존)는 *src/ 가 채워지기 시작한 후* 에야 발현된다. 즉 *현 시점 도구 가치 ≈ 0*.
2. **T-9 (1차 AST scanner 자체를 pre-commit hook 으로 등록)** + **T-10 (룰을 문서로 유지 + PR review)** — 외부 LLM L76 ("계산적 = 우월 가정의 허점") 답습 시, *추가 도구 도입* 보다 *기존 시제 형식 강화* 가 *false-negative-silent-fail* 위험을 *덜* 키운다.

**Reviewer 사전 권고 (T-2 import-linter)** 는 정합성 측면에서 합리적이나, *대안 탐색가* 관점에서는 *옵션을 도구 4종 중 하나에 가둔 framing 자체* 가 차원 1 결함을 답습한 외부 LLM L96 의 "framework 외부 결함을 제기할 인센티브 약화" 패턴과 동일하다. 즉 본 합의에서 *T-1~T-4 중 어느 하나를 고르는 것이 답이다* 라는 framing 자체를 한 번 깨야 한다.

이하 §1~§6 에서 *근거* + *반박* + *권고*.

---

## 1. T-1~T-4 비교 (대안 관점)

### 1.1 4 옵션 *답습 충실성 vs 실용성* 트레이드오프 매트릭스

| 옵션 | 답습 충실성 | Python 정합 | FP 위험 | FN 위험 (depcruise 본질적 한계) | 도구체인 확장 | 1차 AST scanner 와의 중첩 |
|------|---|---|---|---|---|---|
| **T-1** dependency-cruiser (JS native) | ✅ §9.3 *문자 그대로* 답습 | ❌ Python 비공식 (TS-Estree 기반) | ⚠️ Python 표준 lib 매치 가능 | 동적 import / URL / 의미 lock-in 모두 검출 불가 | Node + npm + 1 dev-dep | 동적 import 영역 *완전 분리* (보완 관계) |
| **T-2** import-linter (Python native) | ⚠️ *시제 의도* 만 답습 (도구 변경) | ✅ 공식 | 中 (`google` 단독 vs `google.generativeai` 분기 가능) | 동적 import / URL / 의미 lock-in 모두 검출 불가 | pip 1 dev-dep | 동적 import 영역 *완전 분리* (보완) |
| **T-3** ruff custom rule | ⚠️ *AST 해석 문법* 답습 | ✅ 공식 | 低 (ruff 자체 FP 매우 낮음) | 동적 import / URL / 의미 lock-in 모두 검출 불가 | 0 dev-dep (ruff 既 도입 가능) — *이미 있다면* | 동적 import 영역 *부분 중복* (1차 scanner 와 패턴 중복) |
| **T-4** 1차 AST scanner 확장 (transitive) | ❌ §9.3 의 *도구* 미답습 | ✅ stdlib | 低 (자체 룰 통제 가능) | 동적 import O (1차에서 이미) / URL X / 의미 lock-in X | 0 dev-dep | *완전 통합* — scanner 가 transitive 까지 흡수 |

### 1.2 *조합 가능성* 검토 (1차 합의에서 누락)

`docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md` §8.1 의 4 옵션 표는 *옵션을 단일 선택* 으로 framing 했으나, *조합* 도 가능하다:

| 조합 | 의미 | 평가 |
|------|------|------|
| **T-1 + T-4** | depcruise (정적 graph) + AST scanner (동적/모델명) 양쪽 유지 | 답습 충실성 +1, 운영비 ×2, FN 영역 동일 |
| **T-2 + T-4** | import-linter + AST scanner | Python 정합 + 도구체인 단순. T-4 가 scanner 자체에 transitive 흡수하면 T-2 가 *불필요* — 즉 비효율 |
| **T-3 + T-4** | ruff custom rule + AST scanner | 1차 scanner 와 *패턴 중복* — 동일 룰을 두 도구가 검사 → silent fail 시 *어느 도구가 깨졌는지* 분간 어려움 (외부 LLM L76 silent fail 위험 ↑) |
| **T-4 단독 (확장)** | 1차 scanner 가 *직접* transitive 의존 분석 (`importlib` graph traversal) | 답습 -1 (§9.3 의 *도구* 명시 미답습), 도구체인 0 추가, scanner 책무 ↑ |
| **모두 도입** | 4 도구 모두 CI step | 운영 부담 폭증, 책임 분산 |
| **모두 보류 (= 본 PoC 미진행)** | 1차 scanner 만 유지, 2차는 src/ 등장 후로 연기 | §1.3 별도 분석 |

### 1.3 *부분 도입* / *모두 보류* 비교

| 시나리오 | 즉시 enforcement | 미래 src/ 등장 시 대응 | 도구 도입 비용 | 외부 LLM L76 silent fail 위험 |
|----------|----|----|----|----|
| **모두 보류** | 1차 scanner 만 (이미 5/5) | src/ 등장 시 *그 시점에* 도구 결정 (옵션 폭 보존) | 0 | 1차 scanner 1개 — 위험 단일 (관리 단순) |
| **T-2 단일** | + import-linter 룰 | T-2 그대로 사용 가능 | pip 1 추가 | 2개 도구 — 둘 중 하나 silent 깨짐 가능 |
| **T-1 + T-4 (조합)** | depcruise + scanner 강화 | depcruise 가 transitive, scanner 가 동적 | npm + Node | 3개 검사 경로 — 가장 위험 |

→ **본 보고서의 핵심 의문**: 1차 scanner 가 *이미* PASS/FAIL 양방향 검증에 성공한 환경에서, **2차 도입의 한계 가치(marginal value)** 는 무엇인가?

답: **transitive 의존만**. 그런데 src/ 가 비어 있으므로 transitive 도 0건. 즉 *현재* 한계 가치 = 0.

---

## 2. 추가 옵션 탐색 (T-5~T-10)

### 2.1 후보 5종 평가 매트릭스

| 옵션 | 도구 / 방식 | Python 정합 | 답습 충실성 | 비용 | 답습 출처 (§9.3 와의 관계) | RED FLAG |
|------|--|---|---|---|---|---|
| **T-5** | `pydeps` + 자체 정적 분석 (의존 그래프 시각화 + 자체 룰) | ✅ 공식 (Python) | ⚠️ 시제 의도 답습 (graphviz 형식) | 中 (pydeps + 자체 룰 작성) | depcruise 의 *그래프 추적 강점* 답습 가능 | pydeps 자체는 *시각화 도구* — 룰 차단 기능은 별도 작성 의무 (T-4 와 사실상 동일) |
| **T-6** | `tach` (Python modular boundary tool, 신규) | ✅ 공식 (Rust 백엔드 + Python 인터페이스) | ⚠️ 시제 의도 답습 (modular boundary 형식) | 中 (학습 비용 + 신생 도구 위험) | depcruise 와 가장 유사한 의도 (cross-module 의존 규칙) | **신생 도구 — 의존 안정성 미검증** (Provider Liquidity 의존성 추가 = 자기모순). ADR-009 C-N §2.3 (수단 변경 사전 인지) 답습 의무 ↑ |
| **T-7** | depcruise + Python tree-sitter parser (실험적) | ❌ 비공식 확장 | ✅ §9.3 *도구* 답습 + Python 적용 | 高 (실험적 — 프로젝트 fork 위험) | §9.3 의 *직접 답습* 시도 | **실험적 — 본 repo 가 도구 fork 책임 부담**. PoC 외 운영 진입 시 risk 폭증 |
| **T-8** | pytest plugin 기반 enforcement (테스트 시점 검증) | ✅ Python 공식 | ⚠️ §9.3 시제 의도 → *test 시점* 으로 변환 | 中 | depcruise 의 *CI 통합* 답습 → pytest 통합으로 변환 | 검사 시점이 *늦음* — pre-commit 시점 차단 안 됨. 1차 scanner CI step 답습 弱 |
| **T-9** | pre-commit hook 직접 (1차 scanner 를 hook 으로 등록 — 별도 도구 도입 0건) | ✅ stdlib | ⚠️ §9.3 *도구* 미답습 | 低 (`.pre-commit-config.yaml` 1건 추가) | §9.4 답습 + 검사 *시점 강화* (commit time) | 새 도구 도입 0건. 1차 scanner 의 *시점* 만 강화 |
| **T-10** | 룰 자체를 *문서* 로 유지 + PR review 만 (도구 도입 없음 — 추론적 검증) | N/A | ❌ §9.3 도구 미답습 | 0 | 외부 LLM L76 답습 — *추론적 보조* 우위 | 자동화 0건 — 1차 scanner *외* 의 추가 enforcement 없음. CLAUDE.md §2 "계산적 우선" 답습 ↓ |

### 2.2 T-9 / T-10 가 *Reviewer 사전 권고 T-2* 보다 강한 이유 (반박)

#### T-9 의 강점

1. **신규 도구 도입 0건** — Provider Liquidity 의 본질 ("의존 추가 회피") 를 *enforcement 도구 자체에도* 답습. 즉 *enforcement 가 의존을 추가하지 않는* meta-원칙 정합.
2. **§9.4 답습 + 시점 강화** — 1차 scanner 가 *CI 시점* 만 검사하던 것을 *commit 시점* 으로 앞당김. 이는 외부 LLM L76 의 "silent fail 위험" 을 *층 늘려서* 완화 (commit 차단 → push 차단 → CI 차단 = 3중 layer).
3. **답습 충실성**: §9.3 의 *도구* 는 답습하지 않으나, §9.4 + §9.1 #1 + ADR-009 C-N §5 (Layer 1 모법) 은 그대로 답습 — *의도* 는 답습.
4. **운영 단순**: 1차 scanner 1개 도구 + pre-commit framework 만. 2차에서 *새* 도구 0개.

#### T-10 의 강점 (외부 LLM L76 답습)

> 계산적 메커니즘 (regex, depcruise, SQL trigger)은 false negative 시 조용히 실패합니다. 추론적 보조는 더 비싸지만 unknown unknowns에 강합니다.

T-10 은 *추론적 보조 우위* 를 답습. 즉:
- depcruise 가 잡지 못하는 *URL 하드코딩 (P10) / 의미 lock-in / Memory poisoning (P9)* 같은 unknown unknowns 에 *추론적* (PR review) 가 더 강함.
- 단 T-10 단독은 위험 — *T-9 + T-10* 조합이 합리적 (계산적 시점 강화 + 추론적 보조).

#### Reviewer 사전 권고 T-2 의 약점

1. **새 도구 도입** — Python repo 에 import-linter 추가 = dev-dep 1개 + 학습 비용 + 도구 갱신 책임. 자기모순 위험 (Provider Liquidity 가 의존 추가 회피인데 enforcement 가 의존 추가).
2. **답습 충실성 弱** — §9.3 의 *도구 명시* 는 어차피 답습하지 못함. §9.3 의 *시제 의도* 만 답습한다면 T-9 도 동등 충실 (시제만 commit 시점으로 변환).
3. **1차 scanner 와 책무 분리 모호** — import-linter 가 import graph 를 검사하는데, 1차 scanner 도 import 검사. 두 도구의 *역할 경계* 가 모호 → silent fail 시 *어느 도구가 깨졌는지* 분간 어려움 (외부 LLM L76).

→ **Reviewer 사전 권고 T-2 는 *최선이 아니라 default* 일 가능성** — 본 합의에서 검증 의무.

---

## 3. 2차 보류 시나리오

### 3.1 시나리오 비교 매트릭스

| 시나리오 | 2차 진행 | 즉시 enforcement 강화 | 한계 가치 (현재) | 한계 가치 (미래 src/) | RED FLAG |
|---|---|---|---|---|---|
| **S-A: 지금 도입** (T-1~T-4 중 하나) | ✅ | ✅ | **0 (transitive 0건)** | ↑ (src/ 등장 시 즉시 작동) | 도구 도입 비용 高, 정작 검사 대상 0건 |
| **S-B: 3차 우선 (runtime egress 차단 R-2/R-4.1)** | ❌ (연기) | ⚠️ runtime 차원 | depcruise 와 분리 차원 → 검사 대상 미존재 영향 ↓ | runtime 발생 시 즉시 작동 | 2차 자체 *영구 보류* 위험 (ROI 누적) |
| **S-C: 영구 보류 + T-9 (pre-commit 강화)** | ❌ (영구) | ✅ T-9 시점 강화 | T-9 의 *시점 이득* 만 (transitive 0) | src/ 등장 후 *그 시점* 에 다시 합의 | 답습 충실성 弱 — §9.3 도구 명시 무시 |
| **S-D: 보류 + 외부 LLM 추가 검토** | ❌ (조건부) | ⚠️ 외부 LLM 답변 후 결정 | 0 (대기) | 외부 LLM 답변에 의존 | 합의 대기 비용 (시간) |

### 3.2 *지금 도입 vs 3차 우선* 비교

외부 LLM L51 답습:

> P2-5 라운드트립 검증이 진짜 enforcement — 그것이 PoC 미실증이라는 것이 다시 차원 1 결함

→ depcruise 는 *코드 수준* 정적 차단, 라운드트립 검증은 *의미 수준* 검증. 본질이 다르다. 라운드트립 검증 (G4 round-trip PoC, Order 3 tie) 이 *진짜 enforcement* 라면, 본 2차 (depcruise) 는 *부수적*. 따라서:

**S-B (3차 우선)** 가 *실효 보안* 측면에서 더 효과적일 가능성. 근거:
1. depcruise 는 *src/* 가 비어 있으므로 *현재* 검사 대상 0건.
2. runtime egress 차단 (R-4.1 답습) 은 *src/* 유무와 무관하게 *Docker 격리* 차원에서 즉시 작동.
3. 1차 scanner (이미 PASS) + 3차 (runtime 차원) 만으로 Layer 1 + Layer 2 의 *최소 다층 방어* 가 성립.
4. 2차 (depcruise) 는 src/ 가 채워질 때 *그 시점* 에 도구 결정 → 그 때 도구 ecosystem 이 변해 있을 수 있음 (예: tach 가 stable 되어 있을 수 있음).

### 3.3 *보류* 시 어떤 위험이 *지속* 되는가?

| 위험 | 보류 시 지속 여부 | 1차 scanner 가 잡는가? |
|---|---|---|
| 정적 직접 import (5종) | 아니오 (1차 scanner 가 잡음) | ✅ |
| 동적 import (importlib / __import__) | 아니오 | ✅ |
| 모델명 분기 (claude-/gpt-/gemini-) | 아니오 | ✅ |
| **Transitive 의존 (A → B → openai)** | **예 — depcruise 의 본래 강점** | ❌ — 1차 미커버 |
| URL 하드코딩 (api.anthropic.com) | 예 (depcruise 도 못 잡음) | ❌ |
| 의미 lock-in (모델 출력 가정) | 예 (depcruise 도 못 잡음) | ❌ |

→ **보류 시 지속 위험 = transitive 의존 1건만**. 그러나 *src/ 미존재* 이므로 transitive 자체가 0. 즉 보류 시 *현재* 발생 위험 = 0, *미래* 발생 위험은 src/ 채워질 때 발현.

→ **결론**: *보류는 완전 안전*. 단 보류 *시점* 에 src/ 등장 시 *재합의 trigger* 를 명시해야 함 (예: src/adapters/llm/facade.py real 본문 작성 시 → 자동 풀 3+1 합의).

---

## 4. 근본 의문

### 4.1 §9.3 답습의 *절대성* 의문

`llm-providers-design.md` §9.3 헤더:

> 9.3 정적 검사 — depcruise (단순화, Bβ-2)

핵심 단어: **"Bβ-2"**. Bβ-2 = LiteLLM facade 승격 *시점* 의 시제. 즉:
- §9.3 의 `.depcruise.cjs` 는 *Bβ-2 활성 시점에 적용되는 룰의 시제* 이다.
- 본 repo 는 *현재 Bβ-1 미만* (P1 facade MVP 미진입 — ADR-009 §2.1 답습).
- 따라서 **§9.3 답습 의무 자체가 시점 의존적** — 본 repo 는 아직 §9.3 의 *현재 시제 답습 대상* 이 아니다.

→ **의문**: 본 2차 PoC 가 §9.3 을 답습 대상으로 삼는 *시점 정당성* 자체가 모호. *Bβ-2 시점* 에 답습하면 충분할 가능성.

### 4.2 depcruise 의 *현재 가치* 의문

| 검사 | 1차 scanner (이미) | depcruise (2차) | 현재 가치 |
|------|-----|-----|------|
| 정적 직접 import | ✅ | ✅ (중복) | 0 |
| 동적 import | ✅ | ❌ | -1 (depcruise 가 잡지 못함) |
| 모델명 분기 | ✅ | ❌ | -1 |
| **Transitive 의존** | ❌ | ✅ (강점) | **+1 (단 src/ 미존재 → 실효 0)** |
| URL 하드코딩 | ❌ | ❌ | 0 (둘 다 못 잡음) |
| 의미 lock-in | ❌ | ❌ | 0 |

→ **depcruise 의 *현재* 한계 가치 = +1 - 0 (실효 0) = 0**. *src/ 가 비어 있는 한* 본 도구는 *형식적 시제* 에 그친다.

### 4.3 *도구 변경 자체* ADR 등재 의무 의문

ADR-011 §2.1 (b) 답습:

> (b) 수단의 불가피한 변경에 대한 사전 인지

본 2차 PoC 가 *도구를 T-2 (import-linter) 등으로 변경* 하는 결정 자체가 §9.3 의 *수단 (depcruise) 변경* 이다. 즉:
- §9.3 = *수단으로 depcruise 명시*
- T-2 채택 = *수단을 import-linter 로 변경*
- ADR-011 §2.1 (a)~(e) 5조건 답습 의무 발화

→ **의문**: 본 합의 결과 (T-? 채택) 가 *별도 ADR* (예: ADR-013 안에 부록 또는 ADR-014 안에 부록 — *본문 자동 발행 금지* 답습 시 각하) 에 등재될 의무가 있는가?

답습 절대성: ❌ ADR-013/014 자동 발행 금지. 따라서 *본 합의 보고서 안* 에 *수단 변경* 의 (a)~(e) 충족 여부를 *명시 기록* 의무. 외부 LLM C-2 답습 (PoC 의무 + Evidence Ledger 등재) 와 정합.

---

## 5. 트레이드오프 분석

### 5.1 답습 충실 (T-1) vs Python 정합 (T-2/T-3) vs 자체 확장 (T-4/T-9)

| 트레이드오프 축 | T-1 | T-2 | T-3 | T-4 | T-9 | T-10 |
|---|---|---|---|---|---|---|
| §9.3 *도구* 답습 | ✅✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| §9.3 *시제 의도* 답습 | ✅ | ✅ | ✅ | ⚠️ | ⚠️ | ❌ |
| Python 정합 | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| 도구체인 단순 | ❌ (Node) | ⚠️ (+1) | ⚠️ (+1 if not yet) | ✅ | ✅✅ | ✅✅ |
| FN silent fail 위험 (외부 LLM L76) | 高 (3 도구) | 中 | 中 | 低 | 低 | 中 (추론적 보조) |
| Provider Liquidity *meta 원칙 정합* (의존 추가 회피) | ❌ | ❌ | ❌ (ruff 既 설치 시 ✅) | ✅ | ✅ | ✅ |

### 5.2 자동화 (T-1~T-4) vs 단순 (T-9/T-10)

CLAUDE.md §2 답습:

> 계산적 검증이 가능한 곳에서는 항상 계산적 검증을 우선 사용. 추론적 검증은 진정으로 모호한 상황에서만 사용.

→ T-9 가 *계산적* (1차 scanner 그대로 + 시점 강화). T-10 만 *추론적*. 따라서:
- *계산적 우위* 답습 시 → T-1~T-4 + T-9 모두 후보, T-10 보조.
- 단 외부 LLM L76 의 "계산적 = silent fail 위험" 답습 시 → T-10 의 *추론적 보조* 도 가치 있음.

→ **균형점**: T-9 (계산적, 시점 강화) + T-10 (추론적 보조 PR review) 조합.

### 5.3 지금 도입 vs 보류

| 축 | 지금 도입 | 보류 (S-B 3차 우선 또는 S-C T-9 만) |
|---|---|---|
| 즉시 enforcement 강화 | ✅ | ⚠️ (시점 의존) |
| 한계 가치 (현재) | 0 (src/ 미존재) | 0 |
| 한계 가치 (미래) | ↑ | ↑ (단 그 시점에 다시 결정) |
| 도구 도입 비용 | ↑ | 0 |
| 도구 lock-in 위험 | ↑ (도구 자체 deprecated 가능) | 0 |
| 답습 충실성 | ↑ | ↓ |
| 외부 LLM C-9 답습 (Adapter v2.0 진입 조건 명시) | 부분 충족 | 미충족 |

---

## 6. 권고 (대안 탐색가 — 1~2 안)

### 6.1 권고 안 #1 — **2차 자체 보류 + T-9 (pre-commit 시점 강화)** ⭐ 강력 추천

**근거**:
1. *현재* depcruise 한계 가치 = 0 (src/ 미존재)
2. 1차 scanner 가 *이미* 5/5 패턴 PASS
3. T-9 는 *새 도구 도입 0건* — Provider Liquidity 의 meta 원칙 정합
4. 보류 = 옵션 폭 보존 (미래 src/ 등장 시 그 시점 도구 ecosystem 으로 재결정 가능 — tach stable 화 가능성 등)
5. 외부 LLM L76 silent fail 위험 최소 (도구 1개 유지)

**조건**:
- *src/adapters/llm/facade.py real 본문 작성 시* 자동 풀 3+1 합의 trigger 명시 (재합의 trigger 등록)
- T-9 형식: `.pre-commit-config.yaml` 에 `tools/provider_import_scanner.py` 등록 — 1차 scanner 그대로 사용
- 본 합의 보고서에 *§9.3 답습 의무 시점 = Bβ-2* 명시 (현재는 답습 대상 *시점 미진입* 명시)

**RED FLAG**:
- 답습 충실성 측면에서 §9.3 의 *도구 명시* 는 답습하지 않음 — 단 §9.3 헤더 "Bβ-2" 시제 답습 시 *현재* 답습 대상 외임을 정당화
- 외부 LLM 가 *재검토* 시 "depcruise 미도입" 자체에 의문 제기 가능 → 본 합의 보고서에 *시점 정당성* 명시 의무

### 6.2 권고 안 #2 — **T-2 (import-linter, Reviewer 사전 권고 그대로)** + T-4 (1차 scanner 확장 transitive)

**근거**:
1. §9.3 *시제 의도* 답습
2. Python 정합
3. T-4 가 *transitive* 까지 흡수하면 Reviewer 권고 T-2 보다 *답습 의도* 충실 (depcruise 의 핵심 가치 = transitive)

**조건**:
- import-linter 룰 정의 (allow path / forbidden path) 작성
- 1차 scanner 에 transitive 의존 분석 추가 (`importlib.util.find_spec` 또는 graph traversal)
- 두 도구의 *책무 분리* 명시 (import-linter = static graph, scanner = AST 동적)

**RED FLAG**:
- *2 도구 운영 부담* — silent fail 위험 ↑ (외부 LLM L76)
- *src/ 미존재* — 즉시 가치 0 (S-A 와 동일 RED FLAG)
- 도구체인 확장 (pip + Python dev-dep)

### 6.3 *권고 후보에 포함하지 않은* 옵션 + 사유

| 옵션 | 비포함 사유 |
|------|----------|
| T-1 (depcruise JS) | Python 비공식 + Node 도입 = Provider Liquidity meta 원칙 위반. 답습 충실성 ↑ 만으로 정당화 약 |
| T-3 (ruff custom rule) | ruff 既 도입 여부 미확인. 既 도입 시 강력 후보 (0 dev-dep) — Reviewer 가 *환경 확인 후* 권고 안 #1·#2 의 변형으로 검토 가능 |
| T-5 (pydeps) | T-4 와 사실상 동일 (자체 룰 작성 의무). pydeps 자체는 시각화 |
| T-6 (tach) | 신생 도구 — 의존 안정성 미검증. ADR-009 §2.3 (수단 변경 사전 인지) 답습 의무 ↑ |
| T-7 (depcruise + tree-sitter) | 실험적 — 본 repo 가 도구 fork 책임 부담 |
| T-8 (pytest plugin) | 시점 늦음 — pre-commit 시점 차단 안 됨 |
| T-10 단독 | 자동화 0 — CLAUDE.md §2 "계산적 우선" 답습 ↓. 단 권고 안 #1 의 *보조* 로 사용 가능 |

### 6.4 *최종 입장* (대안 탐색가)

**Reviewer 사전 권고 T-2 는 합리적이나 최선이 아닐 가능성**. 본 합의에서 *반드시 검토 의무* 인 항목 3건:

1. *2차 자체 보류* 가능성 — *src/ 미존재 → 현재 가치 0* 사실의 합의 반영
2. *T-9 (pre-commit 시점 강화) 단독* 으로 충분한가의 검증
3. §9.3 헤더 "Bβ-2" 시제의 *현 시점 답습 의무 여부*

이 3건의 합의가 *없는 상태* 에서 T-2 채택은 *framing 답습* (외부 LLM L96) 의 위험.

본 보고서는 *최종 결정* 을 내리지 않는다 — Reviewer 영역. 단 Reviewer 가 T-2 채택 시 위 3건의 *명시 반박 근거* 를 합의 보고서에 등재해야 한다.

---

## 7. 답습 절대성 자가 검증

| 절대 답습 | 본 보고서 위반 여부 |
|----|----|
| Hermes PMO 격상 제안 금지 | ✅ 미위반 |
| G2 GP-5 최종 PASS 제안 금지 | ✅ 미위반 (오히려 보류 권고) |
| Implementation/Runtime PASS 제안 금지 | ✅ 미위반 |
| Provider 구현 변경 제안 금지 | ✅ 미위반 (도구 차원만) |
| ADR 본문 자동 변경 제안 금지 | ✅ 미위반 (§4.3 에서 "본문 자동 발행 금지" 명시) |
| Tier-2/3 카탈로그 자동 확장 제안 금지 | ✅ 미위반 |
| ADR-013/014 자동 발행 제안 금지 | ✅ 미위반 |
| 다른 Agent 출력 참조 금지 | ✅ 미위반 (독립 분석 — 1차 PoC 산출물 + 입력 문서만 참조) |
| Reviewer 사전 권고 (T-2) 그대로 따르기 금지 | ✅ 미위반 — 권고 안 #1 (보류 + T-9) 을 우선 제시, T-2 는 보조 |

---

## 8. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차) | 신규 작성 | 풀 3+1 합의 입력 #3 (Agent C — 대안 탐색가) |
