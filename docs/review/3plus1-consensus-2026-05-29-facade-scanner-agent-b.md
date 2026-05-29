# 3+1 합의 — Agent B (품질/안전성 검증가) 독립 분석

**일자**: 2026-05-29
**쟁점**: PR #3 CI `bypass-detect` BLOCKED — `provider_import_scanner.py` 가 `facade.py:143`
`import litellm` (lazy) 를 `direct-import:litellm` 위반으로 검출.
**제안 수단**: provider-import-scanner 에 `facade.py` allow-path (예외) 추가.
**관점**: "안전하고 견고한가?" — 보안, 엣지케이스, 문서 정합성.

---

## 결론: **APPROVE WITH CONDITIONS**

allow-path 추가는 안전을 *훼손하지 않으며*, 오히려 현재 상태가 **SDD 명세 위반**이다.
단 allow-path 의 **범위·정밀도·이중 안전망 비대칭**에 대한 조건을 충족해야 한다.

---

## 1. 핵심 근거 (보안 중심)

### 근거 1 — 현재 scanner 가 SDD 를 위반하고 있다 (정렬 방향이 반대)

제안된 allow-path 는 "새 예외를 뚫는" 것이 아니라 **이미 명세된 예외를 구현에 반영**하는 것이다.

- `docs/architecture/llm-providers-design.md` §9.3: depcruise 룰에 `from: { pathNot:
  "^src/adapters/llm/facade\\.py$" }` — **facade 는 정적 검사에서 예외**가 설계 의도.
- `docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md`:
  - §2.1/§2.2 line 79·85: `src/adapters/llm/facade.py` = **허용 import 경로 (✅ 허용)**
  - §4 line 121: `src/adapters/llm/facade.py` = **예외 경로 (Exempt)**, 사유 "§3.1 허용 경로"
- `facade.py` 헤더(line 3): "본 파일은 *유일하게* LiteLLM 직접 import 가 *허용되는 경로*".
  ADR-009 §2.2 #1 답습.

→ 즉 scanner 가 facade 를 위반으로 잡는 **현 상태가 명세 불일치**다. allow-path 미추가가
오히려 SDD 위반이며, 추가가 정합성 복구다.

### 근거 2 — Provider Liquidity (5조-2) 본질을 *보존*한다 (means/ends 정렬)

ADR-011 §2.1: 비협상 본질 = **안전 결과(목적)**, litellm 은 **수단**, provider-agnostic 이
목적. facade 의 litellm 단일 통로는 정확히 "모델/구독/오케스트레이터 교체 자유"라는 목적을
구현하는 수단이다. allow-path 는 그 단일 통로를 정상화할 뿐 통로를 *늘리지 않는다*.

오히려 scanner 가 facade 를 막으면 — facade 가 litellm 을 못 쓰고 → Router 위임 불가 →
Provider Liquidity 자체가 동작 불능. 즉 **allow-path 미추가가 5조-2 를 훼손**한다.

ADR-011 §2.1 (a)~(d) 4조건 관점에서도 이것은 "수단 *대체*"가 아니라 "기존 수단(litellm
facade)의 enforcement 정렬"이므로 4조건 트리거 대상 자체가 아니다 (수단 변경 0).

### 근거 3 — 공격 표면 증가는 "facade 1개 파일"로 한정 (제로 신규 표면이 아니라 *기존* 표면)

allow-path 가 만드는 위험: 누군가 facade.py 안에 다른 provider(openai 직접) 나 우회 import
를 숨겨도 scanner 가 못 잡는다. **그러나** 이 위험은 allow-path 의 *부산물이 아니라*
"facade 가 유일 신뢰 경로"라는 아키텍처의 *본래 전제*다. facade.py 는 이미:
- 코드 리뷰 필수 대상 (단일 파일, ~240 LOC, 변경 빈도 낮음 — Human Review Layer 6)
- import-linter `ignore_imports = facade -> *` 로 **이미 정적 검사 면제 중** (.importlinter line 35)

→ allow-path 추가는 scanner 를 import-linter 와 **동일한 신뢰 경계**로 맞추는 것일 뿐,
신뢰 경계를 *확장*하지 않는다.

### 근거 4 — 단, "이중 안전망 동시 해제"는 실재하는 우려 (조건부)

import-linter 와 scanner 가 *둘 다* facade 를 ignore 하면, facade.py 단일 파일에 대한
**계산적(Computational) 정적 검사는 0**이 된다 (CLAUDE.md 계산적 우선 원칙의 사각지대).
이것은 사실이다. 다만:
- facade.py 의 안전은 본래 **정적 검사가 아니라 단일성 + 코드 리뷰 + 런타임 redaction(RT-1)**
  으로 지켜지도록 설계됨 (design §9.5 체크리스트, facade.py `_redact_request` RT-1).
- import-linter 의 `forbidden_modules` 는 facade *외* 전 src 를 여전히 커버 → facade 외부로
  litellm 이 새는 경로는 두 도구가 모두 잡는다.

→ "facade 내부 무방비"는 수용 가능한 잔여 위험이나, **조건 C-1/C-2 로 완화 필수**.

### 근거 5 — 문서 정합성 불일치 방향: scanner 를 design 에 맞춰 정렬해야 안전

`.importlinter` 헤더 책무 명세(line 8~14): "litellm 4종 = import-linter 책무 /
google.generativeai = scanner 단독 / 동적 import = scanner 전담".

이 명세를 문자 그대로 읽으면 **scanner 는 litellm 의 facade 직접 import 를 검사하면 안 된다**
(litellm direct = import-linter 책무). 그런데 scanner 의 `FORBIDDEN_PROVIDERS` 는 litellm 을
포함하고 facade 예외도 없다 → **구현이 자기 명세를 초과**.

정렬 방향(안전한 쪽): **scanner 의 litellm 검출을 facade 에 대해서만 면제** (design §4 예외
경로 + .importlinter 책무 명세 양쪽과 일치). litellm 의 facade-외부 누출은 import-linter 가
전담하므로 enforcement 공백 0.

---

## 2. 우회 표면 평가 (allow-path 범위별)

| 범위 후보 | 공격 표면 | 평가 |
|-----------|-----------|------|
| **(권장) `facade.py` 의 `litellm` 만 면제** | facade 안에서도 `openai`/`anthropic`/`ollama`/`google.generativeai` 직접 import 는 여전히 검출. litellm 만 통과 | **최소 표면**. design §3.1 forbidden 5종 중 4종은 facade 내부에서도 계속 차단. provider 평등 위반(특정 SDK 직접) 방지 유지 |
| `facade.py` 전체 면제 (provider 토큰 무관) | facade 안에 `import openai` 숨겨도 통과. 동적 import·모델명 분기도 면제 | 中 표면. import-linter 도 `facade -> *` 전체 ignore 이므로 *현 비대칭은 import-linter 가 이미 더 넓음*. 단 scanner 까지 전체 면제 시 facade 정적 검사 0 (근거 4 우려 현실화) |
| 디렉터리 단위 (`src/adapters/llm/*` 면제) | router.py·error_classifier.py 등 미래 분리 파일까지 무검사 | **REJECT**. poc2 §2.2 가 router/error_classifier 를 "⚠️ 보류"로 명시 — 디렉터리 면제는 명세 초과. 분리 시점에 룰 갱신이 설계 |
| glob/prefix (`*facade*`) | `evil_facade.py` 같은 우회 파일명 통과 | **REJECT**. 정확 경로 매칭(`src/adapters/llm/facade.py`)만 허용 |

**권장**: 가장 좁은 범위 — **"`src/adapters/llm/facade.py` 정확 경로 × `litellm` 토큰 한정"**.
import-linter 의 전체 ignore 보다 *더 엄격*하여, 두 도구가 facade 를 완전 무방비로 두지 않는다
(scanner 가 facade 내 openai/anthropic 등은 계속 감시 → 이중망 부분 보존).

---

## 3. 엣지케이스 평가

| 엣지케이스 | 현 scanner 동작 | allow-path(litellm 한정) 후 | 위험 |
|-----------|----------------|---------------------------|------|
| facade 외 파일이 `import litellm` | 검출 (direct-import) | **여전히 검출** (면제는 facade 한정) | 없음 — 핵심 enforcement 유지 |
| facade 내 `import openai` 침투 | 검출 | **여전히 검출** (litellm 토큰만 면제) | 없음 (권장 범위 채택 시) |
| transitive (facade→내부모듈→litellm) | scanner 는 AST 단일파일 → transitive 미검출 (본래 한계, design §9.4 = import-linter `include_external_packages=True` 가 transitive 전담) | 변화 없음 | 기존 잔여 위험 (scanner 책무 외, 명세됨) |
| 동적 import `importlib.import_module("litellm")` (facade 내) | 검출 (dynamic-importlib) | facade 한정 면제 시 **litellm 동적도 면제 여부 결정 필요** — C-3 | facade 안에서 lazy `import litellm` 외에 동적 litellm 은 불필요 → 동적은 면제 *제외* 권장 (정적 lazy import 만 허용) |
| re-export (`from src.adapters.llm.facade import litellm`) | scanner 는 import 출처만 봄 → 재수출 자체는 미검출이나, 그 import 를 *쓰는* 파일이 facade 외면 검출 | 변화 없음 | import-linter 도 동일 한계 — 잔여 위험, 코드 리뷰 영역 |
| facade.py 파일명/위치 변경 | 정확 경로 매칭 깨짐 → litellm 위반 재발(fail-loud) | 동일 | **이점** — 이동 시 CI 가 fail 하여 allow-path 갱신을 강제 (silent bypass 방지) |

---

## 4. BLOCKING 안전 조건

allow-path 구현 시 아래를 **모두** 충족해야 APPROVE 유효:

- **C-1 (BLOCKING) — 최소 범위**: 면제는 **정확 경로 `src/adapters/llm/facade.py` × `litellm`
  토큰 한정**. facade 내 openai/anthropic/ollama/google.generativeai 직접 import 는 계속 검출.
  디렉터리·glob·전체 토큰 면제 금지. (근거 3·4, §2 표)

- **C-2 (BLOCKING) — 면제 회귀 테스트**: 면제가 *과잉 적용되지 않음*을 증명하는 fixture/테스트
  추가:
  (a) facade 경로 + `import openai` → **여전히 FAIL** 검증,
  (b) facade-외 경로 + `import litellm` → **여전히 FAIL** 검증,
  (c) facade 경로 + `import litellm` → PASS 검증.
  현 `pass/facade_only.py` fixture 는 litellm 을 *아예 import 안 함*으로 우회 → 실제 면제
  로직을 검증하지 못함. **음성 테스트(negative test) 필수**.

- **C-3 (BLOCKING) — 동적 import 비면제**: 면제는 정적 `import litellm` (visit_Import/
  visit_ImportFrom) 에만. `importlib.import_module`/`__import__`/`exec` 경유 litellm 은
  facade 내부라도 **면제 제외** (facade 는 lazy 정적 import 만 사용 — facade.py:143).

- **C-4 (문서 정합) — 책무 명세 동기화**: `.importlinter` 헤더 책무 명세(line 8~14)와
  scanner 가 litellm 을 검사한다는 사실의 모순을 해소. 둘 중 하나로 정렬:
  (권장) scanner 가 litellm 을 검사하되 facade 만 면제 → `.importlinter` 헤더 주석을 "litellm:
  import-linter(facade 외 전담) + scanner(facade 면제, facade-외 보조)"로 정정.
  poc2 §4 line 121 (facade = Exempt) 을 구현 근거로 인용.

- **C-5 (권고) — 답습 출처 주석**: scanner 코드에 면제 근거를 design §4.1/§9.3 + poc2 §4
  line 121 + ADR-009 §2.2 #1 로 명시하여, 미래 "왜 facade 만 예외?" 회귀 차단.

---

## 5. 요약

- 제안 수단은 **새 우회로가 아니라 기존 SDD 명세(design §9.3 pathNot, poc2 §4 Exempt)의
  지연된 구현**이다. 현 scanner 가 자기 명세를 초과하여 facade 를 잘못 차단 중.
- Provider Liquidity(5조-2) 본질은 allow-path 로 **보존**된다 (오히려 미추가가 훼손).
  means/ends(ADR-011) 상 수단 변경 0 → 4조건 트리거 대상 아님.
- 공격 표면 증가는 facade 1개 파일로 한정되며, import-linter 가 이미 동일 면제 중 →
  신뢰 경계 *확장 없음*. 단 "이중망 동시 해제" 우려는 **C-1(litellm 토큰만 면제)**로 완화 —
  scanner 가 facade 내 *다른* provider 는 계속 감시.
- **C-1~C-4 BLOCKING 충족 시 APPROVE.** 특히 C-2(음성 테스트)는 면제가 enforcement 구멍이
  되지 않음을 계산적으로 증명하므로 필수.
