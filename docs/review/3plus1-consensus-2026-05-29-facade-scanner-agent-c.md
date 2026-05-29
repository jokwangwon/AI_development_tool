# 3+1 합의 — facade.py vs provider_import_scanner 충돌 (Agent C: 대안 탐색가)

작성: 2026-05-29 | 관점: "더 나은 방법이 있는가?" — 대안 수단, 트레이드오프
독립 분석 (A/B 출력 미참조)

---

## 0. 핵심 발견 (코드/명세 검증 결과)

이 쟁점은 단순 "새 예외를 어디에 추가하나" 문제가 **아니다**. 실제로는:

> **명세(§2.4 white-list)에 이미 facade allow-path 가 *규정*되어 있으나, scanner 구현이 그것을 빠뜨렸다.**
> **그리고 PASS fixture 가 진짜 `import litellm` 을 *하지 않아서* 이 누락을 테스트가 한 번도 잡지 못했다.**

근거 (직접 검증):

1. **`docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` §2.4 "허용 경로 (white-list)" (line 86~92)**
   - 표에 `src/adapters/llm/facade.py` 가 명시: "§4.1 — 정확히 이 파일만 LiteLLM 직접 import"
   - 즉 **scanner 자체의 allow-path 로 facade 가 규정**되어 있었다. 구현(`provider_import_scanner.py`)은 이 white-list 를 코드화하지 않음 (`FORBIDDEN_PROVIDERS` 만 있고 path 예외 0).

2. **`llm-providers-design.md` §9.3 (line 598)** depcruise 원안 자체가 `from: { pathNot: "^src/adapters/llm/facade\\.py$" }` — **path 예외(allow-path) 방식**으로 설계됨. litellm 을 forbidden 목록에서 빼는 방식이 아님.

3. **PASS fixture `tests/fixtures/.../pass/facade_only.py`** — 주석 자인:
   > "실 LiteLLM SDK 는 import 하지 않으며 ... *형식만* 모사"
   진짜 `import litellm` 이 없으니 scanner 가 위반 0 을 반환 → allow-path 누락이 영원히 안 잡힘. **테스트 oracle 결함**.

4. **scanner 에 inline-ignore 메커니즘 부재** (아래 §2 확인).

5. **`.importlinter` 헤더 책무 분담 주석**과 scanner 의 `FORBIDDEN_PROVIDERS` 가 **불일치**:
   - import-linter: litellm 4종 담당 + `facade -> *` ignore → Passed
   - scanner: litellm 포함 + facade 예외 0 → Failed
   - 명세상 litellm 동적 import 는 scanner 도 §9.4 로 담당하도록 의도됨(§2.2 line 72 `__import__("litellm")`). 따라서 **litellm 을 scanner 에서 완전히 빼면 동적 litellm import 차단 구멍이 생김**.

---

## 1. scanner inline-ignore 지원 여부 (대안 2 코드 검증)

**미지원 (확정).**

- `tools/provider_import_scanner.py` 전문 grep: `noqa` / `scanner-ignore` / `ignore` / `allow` / `skip` / `exempt` 토큰 **0건**.
- `_Visitor.visit_Import` (line 67~74) 은 `node.names` 만 보고 **주변 주석(comment)을 전혀 읽지 않음**. Python `ast` 는 기본적으로 주석을 노드로 보존하지 않으므로(주석은 토큰 단계에서 폐기), inline `# scanner-ignore` 를 지원하려면 ast 가 아닌 **별도 토큰/라인 파싱 로직을 신규 구현**해야 함.
- 결론: **대안 2 는 scanner 본문 신규 기능 추가 없이는 불가능**. "본문 변경 0건" 원칙(pre-commit config line 80, PoC §238)과도 충돌.

---

## 2. 대안 발굴 및 비교

### 대안 1 — scanner `FORBIDDEN_PROVIDERS` 에서 litellm 제거
litellm 을 import-linter 단독 책무로 정리.
- ✅ `.importlinter` 헤더 주석의 "litellm 4종 = import-linter 책무" 와 표면상 일치
- ❌ **그 주석은 정확하지 않음.** scanner §9.4 / PoC §2.2 는 **동적 litellm import** (`__import__("litellm")`, `importlib.import_module("litellm")`) 를 scanner 전담으로 규정. import-linter 는 정적 graph 만 보므로 동적 litellm import 를 못 잡음 → **차단 구멍 발생 (보안 회귀)**.
- ❌ FAIL fixture `dynamic_importlib.py:3:dynamic-importlib:litellm` (PoC line 165) 가 회귀. CI "5종 패턴 coverage" 검증(workflow line 85)도 깨짐.
- 판정: **부적합 (보안 회귀).**

### 대안 2 — facade.py:143 inline ignore 주석
- ❌ scanner 미지원 (§1). 신규 기능 구현 + 본문 변경 필요.
- △ 가산점: 예외가 위반 *지점에 국소화*되어 가독성은 좋음. 하지만 inline-ignore 는 **남용 시 어디서든 litellm import 를 뚫는 범용 백도어**가 됨 — Provider Liquidity 5조-2 enforcement 의 의도와 정면 충돌. 가장 위험한 패턴.
- 판정: **부적합 (구현 비용 + 보안 약화).**

### 대안 3 — facade allow-path 추가 (1차 수단)
facade.py 한정 예외, litellm 만 면제, 나머지 forbidden 은 계속 검출.
- ✅ **§2.4 white-list 명세를 *그대로 구현*** — 신규 정책 발명 0건. "명세를 기준으로 코드 수정"(CLAUDE.md SDD) 원칙 정합.
- ✅ §9.3 depcruise 원안의 `pathNot: facade.py` 와 동일 설계 사상.
- ✅ 동적/정적 litellm 차단 모두 facade 외부에서 유지 → 보안 회귀 0.
- △ 단, **구현 세부가 중요**: facade 안에서 *litellm 만* 면제하고 openai/anthropic/google/ollama 및 동적 import 는 계속 검출해야 함. PoC §2.4 의도("정확히 이 파일만 LiteLLM")와 일치. 단순 "facade 전체 skip" 으로 구현하면 facade 안 다른 provider import 가 뚫리므로 **provider-scoped(litellm 한정) 예외**로 좁혀야 함.
- 판정: **적합 (1차 수단, 명세 정합).**

### 대안 4 — facade 구조 변경 (litellm 격리 모듈 분리)
`_build_router` 의 litellm import 를 별도 모듈(예: `src/adapters/llm/_litellm_router.py`)로 옮기고 그 모듈만 allow.
- △ allow-path 의 *대상 파일*만 바뀔 뿐 결국 scanner 예외는 여전히 필요 → 대안 3 의 변형. 문제를 해소하지 못하고 **파일 하나만 더 만듦**.
- ❌ ADR-009 §2.2 #1 / §4.1 / facade.py:114 주석 "litellm import = 본 파일 한정" 의 **단일 진입점 invariant 를 깨뜨림** (litellm 접점이 2파일로 분산). 명세 위반.
- ❌ 구현 비용(코드 이동 + 테스트 재배선) 최대, 이득 0.
- 판정: **부적합 (invariant 훼손 + 고비용).**

### 대안 5 (Agent C 발굴) — 5a/5b

**5a (보강 권고): 대안 3 + PASS fixture 결함 동시 수정.**
근본 원인은 allow-path 누락 *그리고* 그것을 못 잡은 fixture oracle 결함이다. allow-path 만 추가하고 fixture 를 그대로 두면, 미래에 또 다른 facade-litellm 회귀가 동일하게 안 잡힌다.
- fixture 에 **실제 `import litellm` 을 포함한 facade-shaped PASS case** 를 추가(또는 real facade.py 를 PASS 대상에 포함)하여, allow-path 가 *동작함*을 양성 검증.
- ✅ 가이드(명세)와 센서(테스트)가 비로소 일치 → 회귀 재발 방지. CLAUDE.md "계산적 검증 우선" 정합.

**5b (대안): scanner 호출 scope 에서 facade 를 path-exclude.**
pre-commit entry `python3 ... src` 를 `src` 스캔하되 facade 제외하도록 변경.
- ❌ entry/호출부 변경은 "본문 변경 0건" 은 지키지만 **예외 로직이 config(yaml)에 흩어져** scanner 자체를 직접 호출(CI workflow line 81 등)할 때는 예외가 안 먹음 → single-source-of-truth 깨짐. 또 facade 전체 제외라 facade 안 다른 provider import 가 뚫림(대안 3 의 단점만 있고 장점 없음).
- 판정: **부적합.**

---

## 3. 트레이드오프 요약표

| 대안 | 보안(차단 완전성) | 유지보수 | 책무 명확성 | 구현 비용 | 명세 정합 | 종합 |
|------|------|---------|-----------|----------|----------|------|
| 1. litellm 제거 | ❌ 동적 import 구멍 | ○ | △ (주석은 일치, 실의도 위반) | 최소 | ❌ §9.4/§2.2 위반 | **부적합** |
| 2. inline ignore | △ 범용 백도어 위험 | △ | △ | 高(신규기능) | ❌ 미명세 | **부적합** |
| 3. facade allow-path (litellm 한정) | ✅ 완전 유지 | ○ | ✅ §2.4 명세 그대로 | 소 | ✅ §2.4/§9.3 정합 | **적합(1차)** |
| 4. 구조 분리 | ✅ | △ | ❌ 단일진입 invariant 훼손 | 高 | ❌ ADR-009 §4.1 위반 | **부적합** |
| 5a. 3 + fixture oracle 수정 | ✅✅ 회귀 재발 차단 | ✅ | ✅ | 소~중 | ✅✅ 가이드=센서 | **최적** |
| 5b. scope path-exclude | △ facade 전체 구멍 | △ config 분산 | △ | 소 | △ | **부적합** |

---

## 4. 1차 수단(allow-path) 대비 우열 판단

1차 수단(대안 3)은 **방향이 정확**하다 — §2.4 white-list 명세를 구현하는 것이며, 새 정책 발명이 아니라 *빠진 구현을 채우는* 일이다. 대안 1/2/4 는 모두 1차 수단보다 열등하다(보안 회귀 또는 invariant 훼손 또는 고비용).

다만 1차 수단 단독은 **두 가지 함정**이 있다:

1. **구현 범위**: "facade 전체 skip" 이 아니라 **facade 안에서 litellm import 만 면제**해야 한다. PoC §2.4 의 "정확히 이 파일만 LiteLLM" 의도가 그러하며, facade 안 다른 provider(openai 등) 직접 import 나 동적 import 는 계속 검출되어야 Provider Liquidity enforcement 가 유지된다.
2. **테스트 oracle 결함 동반 수정**: 현 PASS fixture 는 진짜 litellm import 가 없어 allow-path 동작을 검증하지 못한다(이 결함이 애초에 누락을 숨겼다). allow-path 추가와 함께 fixture/test 를 보강하지 않으면 동일 회귀가 미래에 재발한다.

→ 따라서 **1차 수단을 그대로 채택하되, 5a 로 보강**하는 것이 우월하다.

---

## 5. Agent C 최종 권고

**권고 수단 = 대안 3 + 대안 5a (조합).**

구체:
1. **scanner 에 facade.py allow-path 추가** — 단, *litellm 토큰 한정* (facade 안에서도 openai/anthropic/google/ollama 및 동적 import 는 계속 검출). PoC §2.4 white-list 명세의 미구현분을 채우는 것이므로 신규 정책 발명 0.
2. **PASS fixture(또는 별도 test) 보강** — 실제 `import litellm` 을 포함한 facade-shaped 케이스로 allow-path 가 동작함을 양성 검증. 가이드(§2.4)와 센서(fixture)를 일치시켜 회귀 재발 차단.
3. **`.importlinter` 헤더 주석 정정 검토** — "litellm = import-linter 단독 책무" 는 부정확(동적 litellm 은 scanner 담당). 책무 분담 주석을 "정적 litellm = import-linter, 동적 litellm + facade 예외 = scanner" 로 명확화 (Agent B/Reviewer 와 교차 확인 권고).

**핵심 이유**: 이 쟁점은 "예외 추가" 가 아니라 **명세에 이미 있던 allow-path(§2.4)를 구현이 빠뜨렸고, fixture 결함이 그것을 숨긴** 명세-구현-테스트 3중 정합성 문제다. 따라서 가장 비싼 수단(구조 변경)도, 가장 위험한 수단(inline ignore / litellm 제거)도 아닌, **명세대로 allow-path 를 채우고 테스트 oracle 을 고치는 것**이 유일하게 보안 회귀 0 + 명세 정합 + 회귀 재발 차단을 동시에 만족한다.
