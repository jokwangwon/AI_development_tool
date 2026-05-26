# G2 GP-5 Provider Adapter Enforcement — 1차 PoC 사양

> **상태**: DRAFT (2026-05-09 후속 1, Group A 1차 PoC)
> **답습 출처**: `docs/architecture/llm-providers-design.md` §9 (Liquidity 위반 패턴 차단), `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` §2.3·§5, `docs/architecture/implementation-runtime-roadmap.md` Group A
> **PASS 조건 답습 출처**: `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), Rollback Triggers R-1~R-9
> **상위 권위**: ADR-008 부록 C, ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리 영구 권위)

---

## 0. 목적

본 PoC 는 Provider Liquidity (5-way Multi-layer Defense) **Layer 1 (Entry: provider 진입 차단)** 의 1차 시제를 메타-템플릿 환경에서 검증한다. 신규 정책 발명 0건을 원칙으로 하며, P1 facade `llm-providers-design.md` §9 의 명세 그대로 답습한다.

핵심 차단 대상:

1. **§9.1 패턴 #1** — provider SDK 직접 import (`import openai`, `import anthropic`, `import litellm`, `import google.generativeai`, `import ollama`)
2. **§9.4 패턴** — 동적 import (`importlib.import_module("openai")`, `__import__("anthropic")`)
3. **§9.1 패턴 #1 (보조)** — 모델명 분기 코드 (`if model == "claude-opus-..."` / `if "gpt-" in model_name`)

본 PoC 는 *Layer 1 의 형식적 차단* 만 검증하며, *runtime 실 호출 차단* (R-2/R-4.1 답습) 은 2차 이후 분리.

---

## 1. 1차 PoC 범위 (사용자 확인 — 2026-05-09)

### 1.1 포함 산출물

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` | PoC 사양 + 답습 매핑 + Evidence 5형식 |
| AST scanner | `tools/provider_import_scanner.py` | §9.4 답습 — AST 파싱 기반 위반 탐지 |
| Fixture (PASS × 1) | `tests/fixtures/provider_adapter_enforcement/pass/facade_only.py` | 가상의 facade 본문 (allow path 답습) |
| Fixture (FAIL × 5) | `tests/fixtures/provider_adapter_enforcement/fail/*.py` | 5종 위반 패턴 |
| CI workflow | `.github/workflows/provider-adapter-enforcement.yml` | scanner + PASS/FAIL 양방향 검증 |
| Reviewer-only 단축 합의 보고서 | `docs/review/3plus1-consensus-2026-05-09-g2-gp5-poc-poc1-reviewer-only.md` | PoC 완성도 검토 |

### 1.2 제외 (2차 이후 분리)

| 항목 | 분리 이유 |
|------|----------|
| `.dependency-cruiser.js` (depcruise rule) | JS 도구체인 도입 → 별도 합의 |
| `.pre-commit-config.yaml` | pre-commit framework 도입 → 별도 합의 |
| Docker isolation 답습 (R-2/R-4.1 패턴) | scanner 자체는 stateless · network-free → isolation 불필요 |
| §9.1 #2~#6 (응답 후처리/메타 저장/OAuth/파서 차단) | runtime 코드 0줄 환경에서 미적용 — runtime 도입 시 보강 |
| 모델명 하드코딩 전수 grep | fixture #5 단일 case 만 1차 포함 |

---

## 2. 차단 패턴 카탈로그 (§9 답습)

### 2.1 정적 import 차단 (§9.1 #1)

```python
# 차단 대상
import openai
import anthropic
import litellm
import google.generativeai
import ollama

from openai import OpenAI
from anthropic import Anthropic
from litellm import completion
```

### 2.2 동적 import 차단 (§9.4)

```python
# 차단 대상
importlib.import_module("openai")
importlib.import_module("anthropic")
__import__("litellm")
__import__("openai")
```

### 2.3 모델명 분기 차단 (§9.1 #1 보조)

```python
# 차단 대상 (단순화 — 1차는 fixture 1건만 검증)
if model == "claude-opus-4-7":
    ...
if "gpt-" in model_name:
    ...
```

### 2.4 허용 경로 (white-list)

| 경로 | 허용 사유 |
|------|----------|
| `src/adapters/llm/facade.py` | §4.1 — 정확히 이 파일만 LiteLLM 직접 import |
| `tests/fixtures/provider_adapter_enforcement/` | 검증 fixture (의도적 위반) |
| `docker/r2-poc/`, `docker/r4-1-poc/` | 기존 Docker isolation PoC (LLM 호출 0건 — false positive 회피) |

---

## 3. PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 의미 | 본 PoC 충족 방법 |
|------|------|-----------------|
| (a) 안전 결과를 본질로 식별 | "provider lock-in 회피 = 안전 결과" 본질 식별 | §0 목적 + ADR-009 C-N §2.3 영구 권위 인용 |
| (b) 수단의 불가피한 변경에 대한 사전 인지 | depcruise/AST/pre-commit 등 수단 변경 시점에 *별도 합의* 필요 | §1.2 제외 항목 분리 명세 |
| (c) 안전 결과 보존 검증 가능성 | scanner exit code + fixture 양방향 검증 + Evidence ledger | §5 검증 시나리오 |
| (d) 폐기 경로 명시 (Rollback) | R-1~R-9 매핑 + scanner 자체 무력화 시 CI step 자체 fail-closed | §6 Rollback 매핑 |
| (e) 외부 검증 가능성 | scanner 입출력 + fixture + CI log = 모두 evidence ledger 등재 | §5.4 Evidence 5형식 |

---

## 4. AST scanner 사양

### 4.1 입출력 명세

```
입력: 디렉터리 경로 (위반 검사 대상)
출력:
  - stdout: 위반 발견 시 각 파일 별 (파일경로:라인번호:패턴명:노드)
  - exit code:
      0 = 위반 0건
      1 = 위반 ≥1건
      2 = 입력 오류 (디렉터리 미존재 등)
```

### 4.2 차단 패턴 (구현 사양)

| # | 패턴명 | AST 노드 | 매칭 조건 |
|---|-------|---------|----------|
| 1 | `direct-import` | `ast.Import` | `name in FORBIDDEN_PROVIDERS` |
| 2 | `from-import` | `ast.ImportFrom` | `module in FORBIDDEN_PROVIDERS` 또는 `module.split(".")[0] in FORBIDDEN_PROVIDERS` |
| 3 | `dynamic-importlib` | `ast.Call` | `func` 가 `importlib.import_module`, args[0] 가 `Constant(str)` ∈ FORBIDDEN_PROVIDERS |
| 4 | `double-underscore-import` | `ast.Call` | `func.id == "__import__"`, args[0] 가 `Constant(str)` ∈ FORBIDDEN_PROVIDERS |
| 5 | `model-name-branch` | `ast.Compare` 또는 `ast.Constant` | 값이 `MODEL_PATTERN_REGEX` (예: `r"^(claude-|gpt-|gemini-).*"`) 와 매치 |

```python
FORBIDDEN_PROVIDERS = frozenset({
    "openai", "anthropic", "litellm",
    "google.generativeai", "google",  # google 단독은 google.generativeai 차단
    "ollama",
})

MODEL_PATTERN_REGEX = r"^(claude-opus-|claude-sonnet-|gpt-|gemini-)"
```

### 4.3 허용 경로 처리

scanner 는 입력 경로 인자를 그대로 검사 — 허용 경로 white-list 는 **호출자 (CI workflow) 가 입력에서 제외**. 즉 scanner 자체는 white-list 무지 (단순화).

---

## 5. 검증 시나리오

### 5.1 PASS fixture 검증

```
$ python tools/provider_import_scanner.py tests/fixtures/provider_adapter_enforcement/pass/
[PASS] No violations found in: tests/fixtures/provider_adapter_enforcement/pass/
$ echo $?
0
```

### 5.2 FAIL fixture 검증

```
$ python tools/provider_import_scanner.py tests/fixtures/provider_adapter_enforcement/fail/
tests/fixtures/provider_adapter_enforcement/fail/direct_import.py:1:direct-import:openai
tests/fixtures/provider_adapter_enforcement/fail/from_import.py:1:from-import:anthropic
tests/fixtures/provider_adapter_enforcement/fail/dynamic_importlib.py:3:dynamic-importlib:litellm
tests/fixtures/provider_adapter_enforcement/fail/double_underscore_import.py:2:double-underscore-import:openai
tests/fixtures/provider_adapter_enforcement/fail/model_name_branch.py:5:model-name-branch:claude-opus-4-7
[FAIL] 5 violation(s) found.
$ echo $?
1
```

### 5.3 CI workflow 검증

`.github/workflows/provider-adapter-enforcement.yml` 의 두 step:

1. **PASS step** — `pass/` 검사, exit 0 확인 (`continue-on-error: false`)
2. **FAIL step** — `fail/` 검사, exit 1 확인 후 *역전* (FAIL fixture 가 *위반 ≥1* 을 보장해야 PoC 가 정확히 동작)

### 5.4 Evidence 5형식

| 형식 | 내용 |
|------|------|
| 1. scanner stdout | 위반 보고 lines |
| 2. scanner exit code | 0 또는 1 |
| 3. fixture 디렉터리 경로 | 검사 대상 |
| 4. commit SHA | 본 PoC 커밋 SHA |
| 5. workflow run URL (CI 실행 시) | GitHub Actions log |

---

## 6. Rollback 매핑 (R-1~R-9)

| Rollback Trigger | 본 PoC 와의 관계 | 발화 시 행동 |
|-----------------|----------------|-------------|
| R-1 (provider 가용성 붕괴) | scanner 무관 | 해당 없음 |
| R-2 (redaction 실패) | scanner 무관 | 해당 없음 |
| R-3 (license 변경) | scanner 무관 (LiteLLM license 변경 시 Layer 1 자체 의미 변경) | scanner rule 재검토 |
| R-4 / R-4.1 (egress / trigger 우회) | scanner 무관 | 해당 없음 |
| R-5 (cost 폭증) | scanner 무관 | 해당 없음 |
| R-6 (auth 노출) | scanner 무관 | 해당 없음 |
| R-7 (메모리/스킬 dual-write 실패) | scanner 무관 | 해당 없음 |
| R-8 (동적 import 우회) | scanner #3 + #4 패턴 — **본 PoC 핵심 방어선** | scanner 무력화 시 CI fail-closed |
| R-9 (provider lock-in 재발) | scanner #1 + #2 + #5 패턴 — **본 PoC 핵심 방어선** | scanner 무력화 시 CI fail-closed |

scanner 자체가 무력화되면 (예: 누군가 CI step 을 silently 우회) — Layer 5 (Evidence ledger) 가 *commit SHA + scanner output* 을 기록하므로 사후 감지 가능.

---

## 7. 답습 출처 매핑 (5-Layer Provider Liquidity Multi-layer Defense)

| Layer | 출처 | 본 PoC 와의 관계 |
|-------|------|----------------|
| Layer 1 (Entry) | ADR-009 C-N §5 모법 + GP-5 | **본 PoC = Layer 1 형식 차단 1차 시제** |
| Layer 2 (Runtime) | G3 §6.4 | 2차 이후 (R-2/R-4.1 답습 runtime 차단) |
| Layer 3 (Memory/Skill) | G4 §3.5 | 본 PoC 무관 |
| Layer 4 (Vault) | G4 §4.3 | 본 PoC 무관 |
| Layer 5 (Evidence) | ADR-012 §원칙 6 | scanner output + commit SHA 등재 |

본 PoC 는 *Layer 1 만* 시제. Layer 2~5 는 별도 PoC.

---

## 8. 합의 escalation 규칙

본 PoC 는 **Reviewer-only 단축 합의** 로 검토. 단, 다음 5종 trigger 중 1건이라도 발화하면 **풀 3+1 합의** 로 전환:

1. depcruise / pre-commit / Docker 도입 발생
2. AST 외 *runtime* 코드 작성 (real `adapters/llm/facade.py` 본문 신규 작성)
3. `tests/fixtures/` 외 *real source tree* 변경
4. Tier-2/3 카탈로그 자동 확장
5. ADR-013/014 본문 자동 발급

---

## 9. 확장 경로 (2차 이후)

| 단계 | 추가 항목 | 책무 |
|------|---------|------|
| 2차 | depcruise rule + pre-commit hook | 빌드 시점 차단 (Layer 0.5) |
| 3차 | runtime egress 차단 (R-4 답습 Docker isolation) | Layer 2 |
| 4차 | §9.1 #2~#6 (응답 후처리/메타/OAuth/파서) | runtime 도입 시 |
| 5차 | LiteLLM Router 실 통합 + facade.py real 구현 | full P1 facade |

---

## 10. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-09 (후속 1, Group A) | 신규 작성 | 1차 PoC 사양, AST scanner + fixture + CI step 답습 |
