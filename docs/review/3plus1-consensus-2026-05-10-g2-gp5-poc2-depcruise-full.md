# 3+1 합의 보고서 (풀) — G2 GP-5 2차 PoC depcruise rule 도입

> **세션**: 2026-05-10 (Group A 2차)
> **합의 형식**: **풀 3+1** (Agent A 구현 분석가 + Agent B 품질/안전성 검증가 + Agent C 대안 탐색가 + Reviewer 검토 에이전트)
> **사유**: 보안 관련 변경 (Provider Liquidity Layer 1 모법 강화) + 아키텍처 의사결정 (도구체인 도입 결정) — CLAUDE.md §3 "보안 관련 변경 → 3+1 (필수)" 답습
> **검토 대상**: docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md (7항목 + 4 도구 옵션 T-1~T-4)
> **답습 권위**: ADR-008 부록 C, ADR-009 C-N §2.3+§5, ADR-011 §2.1 (a)~(e), ADR-012 §원칙 5/6
> **Phase 2 산출물**: docs/review/agents-2026-05-10-g2-gp5-poc2-depcruise/{agent-a-implementation,agent-b-quality,agent-c-alternatives}.md (총 1206줄)

---

## 1. Phase 1 — 분배 (Distribution)

### 1.1 의제

7항목 (적용 대상 / 허용 / 금지 / 예외 / fixture / CI / FP-FN) + 4 도구 옵션 (T-1 dependency-cruiser / T-2 import-linter / T-3 ruff custom / T-4 1차 AST 확장).

### 1.2 분배

| Agent | 관점 | 핵심 질문 |
|-------|------|---------|
| A | 구현 분석가 | 실제로 동작하는가? 기술적 구현 가능성? |
| B | 품질/안전성 검증가 | 안전하고 견고한가? 답습 충실? 보안 이득 vs 도입 비용? |
| C | 대안 탐색가 | 더 나은 방법이 있는가? 2차 자체 보류는? |

### 1.3 편향 통제

3 Agent 모두:
- ✅ 다른 Agent 출력 미참조 (독립 분석)
- ✅ Reviewer 사전 권고 (T-2) 그대로 답습 거부 (각자 독립 결론)
- ✅ 사용자 명시 6 금지목록 0/6 위반 (자가 검증)

---

## 2. Phase 2 — 독립 분석 (Independent Analysis) 결과 요약

### 2.1 Agent A — 구현 분석가 (515줄)

**1순위 권고**: T-2 (import-linter)
- T-1 (dependency-cruiser) **CRITICAL — Python 미지원, 동작 불가** (RA-1)
- T-2 = Python 호환 ✅ + transitive ✅ (grimp 그래프) + dev-dep 1개 + CI 통합 단순
- T-3 (ruff TID) = direct import 만 = 1차 scanner 의 *부분집합*
- T-4 (AST 확장) = grimp 의 재발명

**핵심 발견 (RA-9 CRITICAL)**: import-linter 의 grimp 가 forbidden 모듈 실 install 요구 가능성 — `include_external_packages = True` 옵션으로 해결 가능하나 *PoC CI 1회 사전 검증* 필수.

**2차 PoC 의 *유일한 신규 가치*** = **transitive 의존 차단** (`a.py → b.py → openai`). 1차 scanner 는 per-file 검사라 transitive 미검출.

### 2.2 Agent B — 품질/안전성 검증가 (381줄)

**1순위 권고**: T-2 (import-linter) — ADR-011 §2.1 (a)~(e) 5/5 충족.

**답습 충실성 핵심 판정**:
- §9.3 본문 자체 *"개략, P5 문서로 상세화"* 명시 → *시제 의도 답습* 이 *명시 도구 답습* 보다 우월
- ADR-009 C-N §5 의 "depcruise 룰" 표현 = *예시* — 정확한 도구 강제 미발화

**RED FLAG 6건**:
1. T-1 답습 충실성 *형식적 1점 / 실질적 0점*
2. 현 시점 검사 대상 0건 — PoC 즉시 보안 이득 0
3. URL 하드코딩 차단 부재 — 본 PoC 미해소 (3차 분리 필수)
4. T-1 채택 시 Node 도구체인 = 공격 표면 확대
5. 1차 R-4 HIGH 의 *T-1 채택 의무* 과대 해석 위험
6. ADR-012 §원칙 5/6 + G2 P10 cross-reference 누락 — Evidence Ledger entry 형식 명시 필수

**8 추가 조건 (C-1~C-8)** — T-1 채택 시 *추가* C-9/C-10.

### 2.3 Agent C — 대안 탐색가 (310줄)

**권고 안 #1 ⭐ 강력 추천**: **2차 자체 보류 + T-9 (pre-commit 시점 강화)**
- *현재* depcruise 한계 가치 = 0 (src/ 미존재)
- T-9 = *새 도구 도입 0건* — Provider Liquidity meta 원칙 정합
- 외부 LLM L76 silent fail 위험 최소 (도구 1개 유지)
- *src/adapters/llm/facade.py real 본문 작성 시* 자동 풀 3+1 합의 trigger 등록

**권고 안 #2**: T-2 (Reviewer 사전 권고) + T-4 (1차 scanner 확장 transitive)

**근본 의문 3건** (Reviewer 가 T-2 채택 시 *명시 반박 근거 등재 의무*):
1. *2차 자체 보류* 가능성 — src/ 미존재 → 현재 가치 0
2. T-9 단독 충분한가의 검증
3. §9.3 헤더 "Bβ-2" 시제의 *현 시점 답습 의무 여부*

---

## 3. Phase 3 — 교차 비교 (Cross-Comparison)

### 3.1 일치 (Consensus) — 3/3 모두 동의

| # | 항목 | A | B | C |
|---|------|---|---|---|
| 1 | **T-1 (dependency-cruiser) 비권고** | ✅ CRITICAL 동작 불가 | ✅ 5조건 3.5/5 최저 | ✅ Provider Liquidity meta 위반 |
| 2 | **§9.3 답습 = *시제 의도* 우월** | ✅ §4.4 | ✅ §1.1 | ✅ §4.1 |
| 3 | **2차 PoC 핵심 신규 가치 = transitive 차단** | ✅ §4.3 | ✅ §3.2 | ✅ §1.1 |
| 4 | **현 시점 src/ 미존재 → 즉시 보안 이득 0** | ✅ RA-2 | ✅ RED FLAG 2 | ✅ §4.2 |
| 5 | **URL 하드코딩 차단 부재 — 본 PoC 영역 외 (3차 분리)** | ✅ §4.3 | ✅ RED FLAG 3 | ✅ §1.1 |
| 6 | **6 금지목록 0/6 위반 (자가 검증)** | ✅ | ✅ §8.4 | ✅ §7 |

### 3.2 부분 일치 (Partial) — 2 vs 1

| # | 항목 | A | B | C | 분류 |
|---|------|---|---|---|------|
| 7 | **T-2 (import-linter) 채택** | ✅ 1순위 | ✅ 1순위 | ⚠️ #2 안 (보조) | A+B vs C |
| 8 | **2차 *지금* 진행** | ✅ T-2 진행 | ✅ T-2 진행 | ❌ 보류 강력 추천 | A+B vs C — **핵심 쟁점** |

### 3.3 불일치 (Divergence)

| # | 항목 | A | B | C |
|---|------|---|---|---|
| 9 | **2차 도구 선택 시점** | 지금 (T-2) | 지금 (T-2) | 미루기 (T-9 보류) |

### 3.4 누락 (Gap) — 단일 Agent 만 언급

| # | 항목 | 출처 | Reviewer 평가 |
|---|------|------|-------------|
| G-1 | **RA-9 — grimp 가 forbidden 모듈 실 install 요구 가능성** | A | **CRITICAL — PoC 첫 단계 사전 검증 의무 등재** |
| G-2 | **C-7 외부 LLM L76 silent fail 위험 — 계산적/추론적 비율 명시** | B | 필수 등재 |
| G-3 | **C-8 URL 하드코딩 3차 분리 명시 — 본 PoC 미해소 명시 의무** | B | 필수 등재 |
| G-4 | **RED FLAG 6 — Evidence Ledger entry 형식 + G2 P10 cross-reference** | B | 필수 등재 |
| G-5 | **§9.3 헤더 "Bβ-2" 시제 의문 — 현 시점 답습 정당성** | C | **반박 답습 필수** (§5.2) |
| G-6 | **T-3 (ruff TID) 환경 확인 — ruff 既 도입 여부** | C | 보조 검토 (현재 미도입 확인) |
| G-7 | **재합의 trigger 등록** — src/adapters/llm/facade.py real 본문 작성 시 자동 풀 3+1 | C | 필수 등재 |

---

## 4. Phase 4 — 합의 도출 (Consensus Resolution)

### 4.1 일치 항목 (#1~#6) — 그대로 채택

- ✅ **T-1 (dependency-cruiser) 각하** — Python 미지원 (RA-1) + Provider Liquidity meta 위반
- ✅ **§9.3 답습 방식**: *시제 의도 답습* (allow path / forbidden path) — *명시 도구 답습* (depcruise) 보다 우월
- ✅ **2차 PoC 핵심 가치** = transitive 의존 차단 (1차 scanner 미답습 영역의 유일한 신규)
- ✅ **현 시점 src/ 미존재** = 사실 인식 (PoC 의 *future-proof 시제* 한정 명시 의무)
- ✅ **URL 하드코딩 차단** = 본 PoC 영역 외, 3차 분리 명시 의무
- ✅ **6 금지목록 0/6 위반** = 본 합의 보고서 자체가 답습 강제

### 4.2 부분 일치 (#7~#8) — 근거 평가 후 결정

#### 4.2.1 핵심 쟁점: *2차 *지금* 진행 vs 보류*

**A+B 진행 근거**:
- T-2 가 transitive 차단으로 1차 scanner 빈자리 보완
- Future-proof 룰 정의 시제로서 src/ 신설 시점에 즉시 enforcement 가능
- Python 호환 + dev-dep 1개 = 비용 최저
- 1차 PoC §3 R-4 (HIGH) 권고와 정합

**C 보류 근거**:
- src/ 미존재 → 현재 가치 0
- 도구 도입 자체 = Provider Liquidity meta 원칙 자기모순
- 외부 LLM L76 silent fail (도구 ≥2 = 책임 분산 → 누락 시 조용히 실패)
- §9.3 헤더 "Bβ-2" 시제 — 답습 *시점 미진입* 가능성

#### 4.2.2 Reviewer 의 명시 반박 (Agent C 안 #1 에 대한)

Agent C 의 §6.4 *최종 입장* 답습 — Reviewer 가 T-2 채택 시 *반드시 반박 근거* 등재 의무.

**반박 1 — *src/ 미존재* 자체가 보류 사유로 충분하지 않다**:
- 본 repo 는 *메타-템플릿* (코드 0줄 답습) — 이 상태에서 도구를 *지금* 도입하지 않으면 *src/ 신설 후* 도구 선택 풀 3+1 합의가 *별도로* 필요. 즉 보류 = 의사결정 *지연* 비용.
- *future-proof 시제* 가 즉시 보안 이득 0 이라도 *룰 정의 자체* 가 future src/ 추가 시점에 *적용 즉시 enforcement* 가능 → 시제 가치 ≠ 0.
- placeholder `__init__.py` + transitive_import.py 1 fixture 만으로 *룰 검증 양방향* 가능 (Agent A §1-5 답습).

**반박 2 — T-9 (pre-commit 시점 강화) 단독 으로는 R-9 책무 미답습**:
- 1차 scanner 는 *per-file AST* 만 → transitive 의존 (`a.py → b.py → openai`) 미검출 (Agent A §4.3 답습).
- T-9 (pre-commit hook 등록) = 1차 scanner *시점만* 강화. 책무 영역은 동일 → R-9 (provider lock-in 재발) *transitive 형태* 미답습.
- 즉 T-9 *단독* 으로는 1차 scanner 의 한계를 *지금* 보완하지 않는다. 시점 강화는 옵션 A 의 *부속 조치* 로 채택 가능 (4.4 추가 조건 답습).

**반박 3 — §9.3 헤더 "Bβ-2" 시제 답습은 일관성 있게 *시제 의도* 답습**:
- 1차 PoC (commit a3693a0) 자체가 *§9.3 시제 의도 답습* 으로 진행 — 1차 PoC 합의 (commit 0f503a4) 에서 *명시* 검증.
- 1차가 *시제 의도 답습* 이면 2차도 동일 — 일관성 측면에서 보류 시 *1차의 답습 근거 자체* 도 의문 제기 됨.
- Bβ-2 가 *현 시점 미진입* 이라는 해석은 1차 PoC 성립 자체와 충돌.

**결론**: Agent C 의 권고 안 #1 (보류) 은 *근본 의문* 으로서 가치 있으나, 위 3 반박 답습 시 *T-2 채택 + 시제 시제로서 진행* 이 합리적.

#### 4.2.3 채택: T-2 (import-linter) — APPROVE WITH CONDITIONS

### 4.3 불일치 (#9) — 시점 결정

**Reviewer 결정**: **지금 진행** (T-2 채택)
- 단 *최소 PoC* (1차 scanner 와 동일 *축소 형식*)
- 사용자 명시 답습 — "최소 PoC 부터 진행, 사용자 확인 없이 과도 확장 금지"

### 4.4 누락 (#G-1~#G-7) — 모두 합의 보고서 등재

| Gap | 처리 |
|-----|------|
| G-1 RA-9 grimp 외부 모듈 install | **PoC 첫 단계 사전 검증** — `pip install import-linter` 후 *forbidden 모듈 미설치 환경* 에서 fixture 검증 1회 실행. `include_external_packages = True` 옵션 사용 |
| G-2 외부 LLM L76 silent fail | 본 합의 §6.2 답습 |
| G-3 URL 하드코딩 3차 분리 | 본 합의 §5.5 답습 — *3차 PoC* 별도 합의 등록 |
| G-4 Evidence Ledger entry 형식 | 본 합의 §5.6 답습 — Evidence ledger 5형식 + agent="user" 필드 |
| G-5 §9.3 Bβ-2 시제 의문 | 4.2.2 반박 3 답습 |
| G-6 ruff 既 도입 확인 | 환경 확인 — 현재 ruff 미도입 (T-3 비권고 유지) |
| G-7 재합의 trigger 등록 | 본 합의 §5.4 답습 — *src/adapters/llm/facade.py real 본문 작성 시* 자동 풀 3+1 합의 trigger |

---

## 5. 합의 — 채택 결정 + 추가 조건

### 5.1 채택 도구 — **T-2 (import-linter)** ⭐

근거:
- ADR-011 §2.1 (a)~(e) 5/5 (Agent B §2 매트릭스 답습)
- Python 호환 ✅ + transitive ✅ + dev-dep 1개 (Agent A §4.1 답습)
- §9.3 *시제 의도 답습* (allow path / forbidden path) 충실 (Agent A §4.4 + Agent B §1.1 답습)
- 1차 scanner 와 *역할 분담* 명확 (Agent A §4.3 답습)

### 5.2 채택 7항목

| # | 항목 | 채택 |
|---|------|------|
| 1 | 적용 대상 경로 | **옵션 A — `src/` 만** (placeholder `__init__.py` 동반) |
| 2 | 허용 import 경로 | **`src/adapters/llm/facade.py` 단일** |
| 3 | 금지 import 경로 | **`litellm`, `anthropic`, `openai`, `google.generativeai`, `ollama`** (5종) |
| 4 | 예외 경로 | facade / `tests/fixtures/` / `tools/` / `docker/r2-poc/` / `docker/r4-1-poc/` |
| 5 | 테스트 fixture | **1차 fixture 6건 재사용 + `transitive_import.py` 신규 1건** (총 7건) |
| 6 | CI 연결 | **CI-A — 1차 workflow 안에 step 추가** (evidence 연속성) |
| 7 | FP/FN 방지 | `pathNot` 정규식 + white-list / 동적 import 는 *1차 scanner 가 보완* (역할 분담) |

### 5.3 추가 조건 (C-1~C-10) — *PoC 진행 의무 답습*

| # | 조건 | 답습 출처 |
|---|------|----------|
| C-1 | 본 2차 PoC = *G2 GP-5 부분 충족 시제* 한정 명시 — **최종 PASS 선언 권한 없음** | Agent B §8.2 + 사용자 명시 6 금지목록 #1 |
| C-2 | **Implementation/Runtime PASS 자동 선언 미발생** 명시 (ADR-008 부록 C C.5 답습) | Agent B §8.2 + 사용자 명시 6 금지목록 #2 |
| C-3 | scope §1.2 옵션 A (`src/` 만) 채택 — 현 시점 검사 대상 0건 명시 (future-proof 룰 정의 한정) | Agent B §8.2 |
| C-4 | 1차 fixture 재사용 + `transitive_import.py` 1건 추가 한정 | scope §5.2 |
| C-5 | scope §6 CI-A 채택 — 1차 workflow step 추가 (evidence 연속성) | scope §6.1 |
| C-6 | depcruise 본질적 한계 3종 (동적 import / URL / 의미적 lock-in) **책무 분담 매트릭스 명시** | Agent B §4.4 |
| C-7 | 외부 LLM L76 답습 — 계산적 메커니즘 FN 위험 명시 + 추론적 보조 layer 별도 유지 | Agent B §5.3 |
| C-8 | **URL 하드코딩 차단 = 본 PoC 외 3차 grep 분리 합의 필수** — 본 2차 PoC 도입으로 그 책무 *해소되지 않음* 명시 | Agent B §4.2 |
| C-9 | **RA-9 사전 검증** — `pip install import-linter` 후 forbidden 모듈 미설치 환경에서 `include_external_packages = True` 옵션으로 fixture 검증 1회 실 실행 | Agent A RA-9 |
| C-10 | **재합의 trigger 등록** — `src/adapters/llm/facade.py` real 본문 작성 시 자동 풀 3+1 합의 발화 | Agent C §6.1 |

### 5.4 재합의 trigger 등록 (C-10 답습)

본 합의는 다음 trigger 발화 시 *자동 풀 3+1* 재합의:

| Trigger | 발화 조건 | 재합의 의제 |
|--------|---------|-----------|
| TR-1 | `src/adapters/llm/facade.py` real 본문 신규 작성 | T-2 룰 룰 검증 + LiteLLM 실 import 정상 동작 + transitive 검증 |
| TR-2 | `pyproject.toml` 신설 (T-2 dev-dep 등록 시점) | dev-dep 도입 영향 분석 |
| TR-3 | RA-9 사전 검증 시 `include_external_packages = True` 가 *동작 불가* 판명 | 도구 재선택 (T-3 또는 T-4 후보) |
| TR-4 | depcruise 본질적 한계 3종 중 1건이라도 *본 PoC 영역으로 흡수* 시도 | 책무 분리 재합의 |
| TR-5 | T-9 (pre-commit hook) 도입 별도 합의 진행 시 | 본 2차 PoC 과의 책무 분리 |

### 5.5 책무 분담 매트릭스 (C-6 답습)

| 검증 항목 | 1차 AST scanner | 2차 T-2 (import-linter) | 3차 (별도 합의 — grep + egress) | 라운드트립 (P2-5) |
|----------|---------------|----------------------|----------------------------|-----------------|
| Direct import (`openai`/`anthropic`/`litellm`/`ollama`) | ✅ | ✅ (중첩 강화) | — | — |
| Direct import (`google.generativeai`)[^1] | ✅ (단독 책무) | ❌ (도구 제약) | — | — |
| From-import | ✅ | ✅ (중첩 강화) | — | — |
| **Transitive (A→B→openai)** | ❌ | **✅ (2차 신규 가치)** | — | — |
| 동적 import (`importlib`, `__import__`) | ✅ (1차 전담) | ❌ | — | — |
| 모델명 분기 (문자열) | ✅ (1차 전담) | ❌ | — | — |
| **URL/endpoint 하드코딩** | ❌ | ❌ | **✅ (3차 영역 — 별도 합의)** | — |
| 의미적 lock-in (출력 포맷 가정) | ❌ | ❌ | ❌ | ✅ 라운드트립 |

[^1]: **각주 1 (2026-05-10 후속, C-9 검증 발견)**: `google.generativeai` 는 import-linter 의 `forbidden_modules` contract 가 받지 못 함 — `Invalid forbidden module google.generativeai: subpackages of external packages are not valid` 에러 (import-linter 2.11 / grimp 3.14, 본 검증 환경). 따라서 본 모듈은 **1차 AST scanner 단독 책무** 로 명시 분리. 2차 import-linter `forbidden_modules` 는 4종 (`openai`, `anthropic`, `litellm`, `ollama`) 만 등재. TR-4 부분 발화로 판단되었으나 *책무 분담의 명시적 갱신* 으로 처리 (사용자 명시 답습 — 풀 3+1 재합의 미발화). 단 미래에 `google.generativeai` *최상위 패키지* 차단 룰이 도입되면 (예: top-level `google` 차단 시 `google.protobuf` 등 false positive 위험 발생) TR-4 풀 재합의 발화.

**핵심**: 본 2차 PoC 채택 시 **URL 하드코딩 차단의 *부재* 가 *조용히 통과* (FN 잔존)** 을 *과대 해석* 하지 말 것 (C-8 답습).

### 5.6 Evidence Ledger entry 형식 (C-Add — Agent B RED FLAG 6 답습)

본 PoC 의 evidence 등재 시:

| 필드 | 값 |
|------|---|
| event | `provider_adapter_enforcement_layer1_static` |
| agent | `user` (Hermes 자동 선언 금지 — ADR-008 부록 C C.4 답습) |
| violation_type | `direct-import` / `from-import` / `transitive-import` / `dynamic-importlib` / `__import__` / `model-name-branch` |
| tool | `import-linter` (T-2) 또는 `provider_import_scanner` (1차) |
| commit_sha | (실 commit) |
| ledger_layer | `Layer 1 (Entry)` (5-way Multi-layer Defense Layer 1) |

ADR-012 §원칙 5/6 + G2 §1.2.6 P10 cross-reference 명시 의무.

---

## 6. RED FLAG 종합 (각 Agent 발화 + Reviewer 추가)

### 6.1 Agent 발화 RED FLAG (집계)

| ID | 출처 | 위험 | 본 합의 대응 |
|----|------|------|-----------|
| RA-1 | A | T-1 동작 불가 | T-1 각하 (4.1) |
| RA-2 | A | src/ 부재 | C-3 명시 (5.3) |
| RA-9 | A | grimp 외부 모듈 install | **C-9 사전 검증 의무** (5.3) |
| B-RF1 | B | T-1 답습 충실성 형식적 1점 / 실질적 0점 | 4.2.2 반박 답습 |
| B-RF2 | B | 즉시 보안 이득 0 | C-1 + C-3 명시 |
| B-RF3 | B | URL 하드코딩 부재 | **C-8 명시** (5.5) |
| B-RF4 | B | T-1 Node 도입 공격 표면 확대 | T-1 각하 (4.1) |
| B-RF5 | B | R-4 HIGH 의 T-1 의무 과대 해석 | 4.2.3 + C-1 답습 |
| B-RF6 | B | Evidence Ledger entry 누락 | **5.6 명시** |
| C-Q1 | C | §9.3 Bβ-2 시제 의문 | 4.2.2 반박 3 답습 |
| C-Q2 | C | 보류 옵션 미검토 위험 | 4.2.2 반박 1+2 답습 |

### 6.2 Reviewer 추가 RED FLAG

| ID | 위험 | 대응 |
|----|------|-----|
| **R-RF1** | C-9 (RA-9) 사전 검증 결과 *FAIL* 시 — T-2 자체 채택 *철회* 가능. 본 합의는 *조건부 채택* | TR-3 발화 시 *자동 풀 3+1* 재합의 |
| **R-RF2** | T-2 의 `pyproject.toml` 신설 = Python 패키징 표준 도입 — 별도 영향 분석 미발화 | TR-2 답습 |
| **R-RF3** | 1차 scanner + T-2 *2 도구 운영* — silent fail 위험 ↑ (Agent C §6.2 RED FLAG 답습) | C-7 외부 LLM L76 답습 + 책무 분담 매트릭스 (5.5) 로 완화 |

---

## 7. 최종 판정

### 7.1 Design/Governance Gate (G2 GP-5 2차 PoC) — ✅ APPROVE WITH CONDITIONS

**APPROVE 조건**:
1. ✅ ADR-011 §2.1 (a)~(e) 5/5 충족
2. ✅ §9.3 *시제 의도 답습* 충실
3. ✅ 6 금지목록 0/6 위반
4. ✅ 3 Agent 일치 항목 6/6 채택
5. ✅ 부분 일치 항목 (T-2) 채택 + Agent C 반박 3건 명시 답습
6. ✅ 누락 7건 (G-1~G-7) 모두 합의 보고서 등재

**WITH CONDITIONS** (PoC 진행 의무):

C-1~C-10 모두 답습 의무. 특히:
- **C-9 (RA-9 사전 검증)** = PoC *첫 단계*
- **C-10 (재합의 trigger)** = TR-1~TR-5 자동 발화 의무
- **C-8 (URL 차단 3차 분리)** = 본 2차 PoC 채택이 *URL 차단 책무 해소* 로 해석되지 않음

### 7.2 Implementation/Runtime PASS 자동 선언 — 미선언 (사용자 명시 답습)

본 PoC 는 *Layer 1 형식 차단 강화 시제* 로서 G2 GP-5 의 PASS 조건 *부분 충족 시제* 이며, **G2 전체 Implementation/Runtime PASS 선언 권한이 없음**.

### 7.3 escalation triggers 0/N 발화

본 풀 3+1 합의 자체가 사용자 명시 답습 (보안 + 도구 도입 결정). 추가 escalation 미발화.

---

## 8. 다음 단계

| 단계 | 작업 | 합의 형식 |
|------|------|----------|
| 1 | 본 합의 보고서 + Phase 2 Agent 출력 (3건) commit + push | 사용자 명시 |
| 2 | **C-9 RA-9 사전 검증** — `pip install import-linter` + grimp `include_external_packages` 옵션 동작 확인 (1회) | 단독 (PoC 첫 단계) |
| 3 | C-9 결과 사용자 보고 — *PASS* 시 본 PoC 진행, *FAIL* 시 TR-3 발화 풀 3+1 재합의 | 사용자 확인 |
| 4 | 본 PoC 산출물 작성 — `.importlinter` config + `transitive_import.py` fixture + CI step 추가 + 본 합의 답습 | TDD 답습 |
| 5 | 양방향 검증 (PASS exit 0 + FAIL exit 1) | 1차 PoC 답습 |
| 6 | Reviewer-only 단축 합의 (escalation 0/N 발화 시) | 단축 적격 검증 |
| 7 | 합의 결과 commit + push + 다음 진입점 결정 | 사용자 명시 |

---

## 9. 합의 보고서 검증 메타

| 항목 | 값 |
|------|---|
| 합의 형식 | **풀 3+1** (Agent A + B + C + Reviewer) |
| Phase 2 Agent 출력 분량 | 1206줄 (A 515 + B 381 + C 310) |
| 본 합의 보고서 분량 | 약 380줄 |
| 일치 항목 | 6 |
| 부분 일치 | 2 (핵심 쟁점 1건) |
| 불일치 | 1 |
| 누락 | 7 |
| 6 금지목록 위반 | 0/6 |
| 신규 정책 발명 | 0건 |
| 사용자 명시 위반 | 0건 |
| Agent 편향 통제 | 3/3 (독립 분석 + Reviewer 사전 권고 그대로 답습 거부) |
| Reviewer T-2 사전 권고 vs 합의 결과 | 결과 일치 — 단 Agent A/B/C 의 *3 차원 독립 근거* 답습 + Agent C 반박 3건 명시 |

---

## 10. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차) | 신규 작성 | 풀 3+1 합의 — T-2 (import-linter) APPROVE WITH CONDITIONS, C-1~C-10 + TR-1~TR-5 답습 |
| 2026-05-10 (Group A 2차, 후속) | §5.5 책무 분담 매트릭스 각주 1 추가 | C-9 RA-9 사전 검증 PASS — `include_external_packages = True` 정상 동작 확인. 단 `google.generativeai` 가 import-linter forbidden contract 제약으로 받지 못 함 → 1차 AST scanner 단독 책무 명시 분리. 사용자 명시 답습 (풀 재합의 미발화, 책무 분담 명시 갱신만) |
