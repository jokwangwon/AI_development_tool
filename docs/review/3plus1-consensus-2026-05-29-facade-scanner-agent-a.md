# 3+1 합의 — Agent A (구현 분석가) 분석

**일자**: 2026-05-29
**쟁점**: PR #3 — CI `bypass-detect` (`pre-commit run --all-files`) FAIL
**관점**: "실제로 동작하는가?" — 기술적 구현 가능성, 의존성, 회귀
**대상 1차 수단**: provider-import-scanner 에 `facade.py` allow-path 예외 추가

---

## 0. 결론

**APPROVE WITH CONDITIONS**

제안된 1차 수단(scanner 에 facade allow-path 추가)은 기술적으로 정확하고 회귀 안전하게 구현 가능하다.
단, **구현 위치를 scanner 본문이 아니라 "호출자(caller)" 측에 두는 것이 설계(PoC §4.3)와 정합**한다는 조건이 붙는다.
현 PR FAIL 의 실제 root cause 는 "scanner 가 litellm 을 검사하는 것" 이 아니라
**pre-commit hook entry 가 `src` 전체를 allow-path 제외 없이 scanner 에 넘긴 것**이다.

---

## 1. 재현 및 root cause 실측

```
$ python3 tools/provider_import_scanner.py src
[FAIL] 1 violation(s) found.
src/adapters/llm/facade.py:143:direct-import:litellm
```

- `facade.py:143` = `_build_router()` 내부 `import litellm` (lazy). ADR-009 §2.2 #1 + design §4.1 의 *의도된 유일 허용* 코드.
- scanner `FORBIDDEN_PROVIDERS` 에 `litellm` 포함, allow-path 무지 → 검출.
- **언제부터 충돌했나** (git 실측):
  - `import litellm` 도입 = `56a650c` (69 entry, real Router 위임). 이전엔 facade fixture-only.
  - `bypass-detect` workflow = 2026-05-27 추가 (`pre-commit run --all-files`).
  - 두 조건이 동시 존재한 *지금* 처음 표면화 (잠복 충돌, 회귀 아님).

---

## 2. 책무 경계 — 코드/명세상 정의와 불일치의 실체

### 2.1 명세상 책무 분담 (3 source 일치)

| source | 진술 |
|--------|------|
| `.importlinter` 헤더 §책무 분담 | 4종(openai/anthropic/litellm/ollama) = **import-linter 책무**, google.generativeai = AST scanner 단독, 동적 import = AST scanner 전담 |
| `llm-providers-design.md` §9.3 depcruise | `from: { pathNot: "^src/adapters/llm/facade\\.py$" }` — **facade 경로는 forbidden SDK 검사에서 제외** (litellm 포함 4종 전부) |
| PoC `g2-gp5-provider-adapter-enforcement-poc.md` §2.4 | 허용 경로 white-list 에 `src/adapters/llm/facade.py` 명시 |

→ 명세상 litellm direct import 의 facade 제외는 **import-linter 가 `src.adapters.llm.facade -> *` ignore 로 이미 처리**. (실측: `lint-imports` PASS.)

### 2.2 불일치의 실체 (이중 결함)

1. **scanner FORBIDDEN_PROVIDERS 중복**: litellm 은 명세상 import-linter 책무인데 scanner 도 검사 → 책무 중복.
   - 단 이 중복은 *그 자체로는* 무해했다 — 왜냐하면…
2. **PoC §4.3 호출 계약 위반 (진짜 root cause)**:
   > "scanner 는 입력 경로 인자를 그대로 검사 — 허용 경로 white-list 는 **호출자(CI workflow)가 입력에서 제외**. 즉 scanner 자체는 white-list 무지(단순화)."

   - 전용 workflow `provider-adapter-enforcement.yml` 은 scanner 를 **fixture 에만** 적용 (real `src` 미적용) → §4.3 준수 → facade 미노출.
   - 그러나 pre-commit hook `provider-import-scanner` 의 entry = `python3 tools/provider_import_scanner.py src` → real `src` 전체를 **allow-path 제외 없이** 투입 → §4.3 위반.
   - 즉 불일치의 본질 = "scanner 가 litellm 을 본다" 가 아니라 **"호출자가 allow-path 를 제외하지 않았다"**. 설계는 호출자 책임을 명시했으나 hook entry 가 이를 구현하지 않음.

---

## 3. allow-path 추가 후 회귀 검증 (facade 외부 litellm 검출 유지 여부)

핵심 회귀 질문: allow-path 추가가 facade *외부*의 litellm/기타 direct import 차단을 무력화하지 않는가?

| 검출 경로 | allow-path 추가 후 |
|-----------|-------------------|
| facade 외부 `import litellm` (src/) | **import-linter 가 검출** (`facade -> *` 만 ignore, 그 외 src→litellm 차단). 실측: transitive probe 검증 step 존재 (workflow line 109~133) |
| facade 외부 `import openai/anthropic/ollama` | import-linter + scanner(allow-path 가 litellm 외 forbidden 은 facade 에서도 계속 검사하도록 좁히면) 양쪽 |
| facade 외부 동적 import / 모델명 분기 | scanner 전담 — allow-path 가 *facade.py 한정*이면 영향 0 |

→ allow-path 를 **facade.py 단일 경로 + (가능하면) litellm 토큰 한정**으로 좁히면 회귀 표면 0.
   facade 외부 litellm 은 import-linter 가 독립적으로 차단하므로 다층 방어(5-way) 손실 없음.

---

## 4. 1차 수단의 기술적 함정/엣지케이스

1. **over-broad allow-path 위험 (가장 중요)**: facade.py 전체를 *모든* forbidden 에 대해 면제하면,
   누군가 facade.py 안에 `import openai` (litellm 아닌 직접 SDK) 를 숨겨도 scanner 가 통과시킨다.
   - 단 import-linter 가 `facade -> *` 전체를 ignore 하므로 openai 도 import-linter 는 못 잡음.
   - → facade.py 내부의 litellm 외 SDK 직접 import 는 **현재도 양 도구 모두 사각**. allow-path 가 이 사각을 *새로 만들지는* 않지만 좁히지도 않음. (수단 선택 무관한 기존 gap — 별도 추적 권고.)
2. **동적 import / 모델명**: facade.py 는 `_load_config` 에 `import yaml`(forbidden 아님)뿐. 모델명은 `litellm_model` 을 config 에서 읽음(하드코딩 0). allow-path 가 facade 한정이면 동적/모델명 패턴 회귀 없음.
3. **transitive**: scanner 는 AST 단일 파일 기반 — transitive 무지(설계대로). transitive 는 import-linter 책무 → allow-path 와 무관.
4. **경로 매칭 정확성**: allow-path 구현 시 OS 경로 구분자(`/` vs `\`), 절대/상대 경로, `src/adapters/llm/facade.py` vs `./src/...` 정규화 필요. `Path.as_posix()` 로 정규화하지 않으면 매칭 누락(= facade 가 여전히 FAIL) 또는 과매칭 위험.
5. **fixture 경로 충돌 주의**: `tests/fixtures/.../pass/facade_only.py` 도 facade 명명 — 경로 매칭을 파일명이 아닌 *전체 경로*로 해야 fixture 검증(전용 workflow)이 깨지지 않음.

---

## 5. 대안 수단 기술적 실현성 평가

| 대안 | 실현성 | 평가 |
|------|--------|------|
| **A. scanner 본문에 facade allow-path 추가** (1차 제안) | 높음 | 구현 단순. 단 PoC §4.3 "scanner = white-list 무지" 설계 철학과 충돌. scanner 가 정책 경로를 알게 됨. |
| **B. 호출자(hook entry) 측 제외** — hook entry 를 `src` 대신 facade 제외 디렉터리 집합으로 변경하거나, scanner 에 `--exclude` 플래그 추가 후 hook 에서 facade 지정 | 높음 | **§4.3 설계 정합** (호출자가 white-list 제외). scanner 본문 철학 보존. `--exclude` 는 일반화 가능 + fixture workflow 무영향. **A 보다 설계 충실.** |
| **C. scanner FORBIDDEN 에서 litellm 제거** (import-linter 단독 책무로) | 중간 | 명세 책무 분담과 가장 정합(litellm = import-linter 책무). 그러나 scanner fixture(`fail/dynamic_importlib.py:litellm`, line 165)가 litellm dynamic import 검출을 기대 → fixture/workflow 회귀. 동적 litellm import 는 import-linter 가 못 잡으므로 scanner 가 litellm 동적은 계속 봐야 함 → 단순 제거 불가. |
| **D. facade lazy import 를 회피**(litellm 미참조 구조) | 낮음 | Provider Liquidity 단일 통로 파괴. ADR-009 §2.2 위반. REJECT 대상. |

**기술적 권고 순위**: B ≳ A ≫ C ≫ D.
B(호출자 제외 / `--exclude` 플래그)가 설계 §4.3 에 가장 충실하고 scanner 본문 불변(PoC "본문 변경 0건" 답습 유지)을 가능케 함.
A 도 동작하나 scanner 가 정책 경로를 내장하게 되어 PoC §4.3 철학과 마찰.

---

## 6. 권고 구현 형태

1. **범위**: allow-path 는 **`src/adapters/llm/facade.py` 단일 경로 한정**. 디렉터리/glob 광역 금지.
2. **위치**: 가능하면 **B안** — scanner 에 `--exclude PATH...` 플래그 추가, pre-commit hook entry 를
   `python3 tools/provider_import_scanner.py src --exclude src/adapters/llm/facade.py` 로 변경.
   (PoC §4.3 "white-list 는 호출자가 제외" 답습. scanner 는 여전히 white-list 무지 — 단지 제외 인자를 받음.)
3. **토큰 좁히기(선택, A안 채택 시)**: facade 면제를 *litellm 토큰 한정*으로 좁혀, facade 내 openai/anthropic 등 다른 SDK 직접 import 는 계속 검출(§4 함정 #1 완화).
4. **경로 정규화**: `Path.as_posix()` 비교 + repo-root 상대 정규화 (§4 엣지케이스 #4/#5).
5. **회귀 가드(필수)**: 새 fixture 또는 테스트 — facade 외부 `src/...x.py` 의 `import litellm` 이 여전히 검출됨을 증명(scanner 또는 import-linter). transitive probe(workflow line 109)는 이미 facade 외부 차단을 cover.

---

## 7. 발견한 기술적 리스크

- **R1 (중)**: A안 over-broad 면제 시 facade.py 내부 litellm-외 SDK 직접 import 가 scanner+import-linter 양쪽 사각이 됨(기존 gap이지만 명시 추적 필요). → 토큰 한정으로 완화.
- **R2 (저)**: 경로 매칭 미정규화 시 facade 미면제(FAIL 지속) 또는 fixture facade_only.py 과면제(전용 workflow 검증 약화).
- **R3 (저)**: C안(litellm 제거) 선택 시 fixture `dynamic_importlib.py:litellm` 회귀 — 동적 litellm 은 import-linter 미검출이므로 단순 제거 불가.
- **R4 (정보)**: 근본 원인은 hook entry 의 호출 스코프(`src` 전체)이지 scanner FORBIDDEN 정의가 아님. 1차 수단이 A(scanner 본문)로 가면 설계 §4.3 의 "scanner white-list 무지" 원칙이 침식됨 — 차후 다른 allow-path(예: docker PoC 경로) 요구 시 scanner 본문이 정책 카탈로그화될 위험. B안이 이 미끄럼 방지.
