# 3+1 합의 보고서 — facade.py vs provider_import_scanner 충돌 (Reviewer)

**일자**: 2026-05-29
**관점**: Reviewer — "최선의 합의는?" (CLAUDE.md §3 Phase 3-4 교차 비교 + 합의 도출)
**입력**: Agent A(구현) / Agent B(안전) / Agent C(대안) 독립 분석 3건
**검증**: PoC §2.4/§4.3, `.importlinter`, `provider_import_scanner.py`, `facade.py:143`,
`.pre-commit-config.yaml`, `provider-adapter-enforcement.yml`, PASS/FAIL fixture 직접 실측

---

## 0. 쟁점

PR #3 머지가 CI `bypass-detect`(`pre-commit run --all-files`) FAIL 로 BLOCKED.

```
src/adapters/llm/facade.py:143:direct-import:litellm
```

`facade.py:143` = `_build_router()` 내부 lazy `import litellm` (ADR-009 §2.2 #1 의 *유일 허용*
경로). import-linter 는 `src.adapters.llm.facade -> *` ignore 로 이미 Passed.
scanner 만 facade 를 위반 검출. 1차 제안 수단 = scanner 에 facade allow-path 추가.

---

## 1. 교차 비교 매트릭스

### 1.1 Consensus (3개 모두 동의) — 그대로 채택

| # | 합의 사항 | 근거 (실측 확인) |
|---|----------|-----------------|
| CS-1 | **방향은 정확**: allow-path 는 "새 예외 발명"이 아니라 *이미 명세된* facade 예외(design §9.3 pathNot, PoC §2.4 white-list)의 미구현분 구현. SDD "문서 기준 코드 수정" 정합 | A§2.1, B근거1, C§0 — 셋 다 §9.3/§2.4 인용. 실측 일치 |
| CS-2 | **범위 = litellm 토큰 한정** (정확 경로 `src/adapters/llm/facade.py` × litellm 만 면제). facade 내 openai/anthropic/ollama/google.generativeai 직접 import 는 계속 검출 | A§6.3, B C-1, C§4.1 — 셋 다 "facade 전체 skip 금지, litellm 토큰 한정" 명시 |
| CS-3 | **alt 1 (litellm 을 FORBIDDEN 에서 제거) REJECT**: 동적 litellm(`importlib.import_module("litellm")`)은 import-linter 미검출 → scanner 전담. 제거 시 `dynamic_importlib.py:litellm` FAIL fixture 회귀 + 보안 구멍 | A§5-C, B(암묵), C 대안1. 실측: fail fixture line 9 `importlib.import_module("litellm")` 존재 확인 |
| CS-4 | **alt (facade 구조 분리) REJECT**: 단일 진입점 invariant(ADR-009 §4.1) 훼손 + 고비용, 이득 0 | A§5-D, C 대안4. (B 미언급 = Gap 아님, 명백 합의) |
| CS-5 | **Provider Liquidity(5조-2) 보존**: allow-path 는 단일 통로 정상화일 뿐 통로 확장 0. 오히려 미추가가 facade→Router 위임 불가 → 5조-2 훼손. ADR-011 4조건 = 수단 변경 0 → 트리거 대상 아님 | B근거2 명시, A/C 암묵 동의 (REJECT 근거에 5조-2 보존 전제) |

### 1.2 Partial (2개 동의, 1개 이견 또는 미언급)

| # | 사항 | 동의 | 이견/미언급 | Reviewer 판정 |
|---|------|------|-----------|--------------|
| PT-1 | **PASS fixture oracle 결함 동반 수정** (`facade_only.py` 가 실 litellm 미import → 면제 누락을 영영 못 잡음) | C(§0,§5 — 핵심 발견), B(C-2 (c) PASS 검증 = 사실상 동일 요구) | A 미언급 | **채택**. 실측 확정: fixture 주석 "실 LiteLLM SDK 는 import 하지 않으며". 게다가 fixture 는 `tests/fixtures/` 자체가 white-list 경로 → 면제 로직 검증 **구조적 불가**. 회귀 재발 차단의 핵심 |
| PT-2 | **`.importlinter` 헤더 책무 주석 정정** ("litellm = import-linter 책무" 는 부정확 — 동적 litellm 은 scanner 담당) | B(C-4), C(§5.3) | A 미언급 | **채택**. 실측: 헤더 line 9~11 "litellm = 본 룰 / 동적 import = AST scanner 전담" → 정적/동적 분담 명문화 필요 |
| PT-3 | **동적 import 면제 제외** (면제는 정적 `import litellm` 만; importlib/__import__ 경유 litellm 은 facade 내부라도 검출 유지) | B(C-3), A(§4.2 암묵) | C 명시 안 함(범위로 흡수) | **채택**. 실측: facade.py:143 = 정적 lazy import. 동적 litellm 은 facade 에 불필요 → 면제 제외가 안전 |

### 1.3 Divergence (핵심 불일치) — §2 에서 해소

| # | 쟁점 | A | B | C |
|---|------|---|---|---|
| **DV-1** | **구현 위치** | **호출자 측 우선** — scanner 에 `--exclude PATH` 플래그 추가, hook entry 에 `--exclude facade.py`. 근거 = PoC §4.3 "white-list 는 호출자가 제외". 차선 = scanner 본문 allow-path | scanner 본문 면제 (litellm 토큰) 암묵 전제 | scanner 본문 allow-path. **5b(scope path-exclude)를 명시 REJECT** ("config 분산 + SSOT 깨짐 + facade 전체 구멍") |

### 1.4 Gap (특정 에이전트만 언급)

| # | 사항 | 출처 | Reviewer 판정 |
|---|------|------|--------------|
| GP-1 | fixture oracle 결함이 누락을 *숨긴* 근본 원인 (명세-구현-테스트 3중 정합성 문제) | C 단독 | **중요 — 채택**. PT-1 과 통합 |
| GP-2 | over-broad 면제 시 facade 내 litellm-외 SDK 가 scanner+import-linter 양쪽 사각(기존 gap, 별도 추적) | A 단독(R1) | **정보로 기록**. CS-2(토큰 한정)로 완화. import-linter 는 `facade -> *` 전체 ignore 라 facade 내 openai 를 어차피 못 잡음 → scanner 토큰 한정이 오히려 *더 엄격* (B§2 표 일치) |
| GP-3 | 경로 매칭 정규화 필요 (`Path.as_posix()`, fixture `facade_only.py` 동명 충돌 주의) | A 단독(§4.4/4.5) | **채택**. 구현 조건에 포함 |
| GP-4 | facade.py 이동/개명 시 정확 경로 매칭이 fail-loud → allow-path 갱신 강제(silent bypass 방지) = 이점 | B 단독(§3 표) | **정보로 기록**. 정확 경로 매칭의 부수 이점 |

---

## 2. 핵심 불일치 해소 (DV-1: 구현 위치)

### 2.1 양측 근거 정리

- **A (호출자 측 `--exclude`)**: PoC §4.3 명문 — *"scanner 는 입력 경로 인자를 그대로 검사 —
  허용 경로 white-list 는 **호출자(CI workflow)가 입력에서 제외**. 즉 scanner 자체는 white-list
  무지(단순화)."* → scanner 본문 불변, "본문 변경 0건" 원칙(pre-commit config line 80) 답습.
- **C (scanner 본문 allow-path)**: 5b(호출자 scope 제외)를 REJECT — "예외가 config 에 흩어져
  SSOT 깨짐 + facade 전체 제외라 facade 내 다른 provider 가 뚫림."

### 2.2 실측으로 양측 주장 검증

**(1) §4.3 은 실재하고 명백히 호출자 책임을 규정** (A 정확). 그러나—

**(2) §4.3 의 caller-exclusion 은 *경로 단위*(whole-file)다.** 경로 제외는 토큰을 구분 못 함.
즉 §4.3 그대로면 facade.py *전체*가 제외되어 **CS-2(litellm 토큰 한정)를 만족할 수 없다.**
facade 내 `import openai` 침투가 무검사로 통과 → C 의 "facade 전체 구멍" 지적이 **§4.3 caller
방식의 실제 결함**이다.

**(3) C 의 5b REJECT 근거 "CI workflow 가 scanner 를 직접 호출 → SSOT 깨짐"은 사실 오류.**
실측: 전용 workflow `provider-adapter-enforcement.yml` 은 scanner 를 **fixture 에만** 적용
(line 64/76/146/148 — `pass/`, `fail/`, `mvp1_entry/`). real `src` 를 스캔하는 호출자는
**pre-commit hook entry(`...py src`) 단 하나**. 따라서 caller-exclusion 은 *분산되지 않으며*
단일 지점이다. C 의 SSOT 우려는 전제가 틀렸다.

**(4) 그러나 (2)가 결정적.** §4.3 caller-exclusion(경로 단위)은 CS-2(토큰 한정)와 양립 불가.
세 에이전트가 *공통으로* 요구한 CS-2(facade 내 openai/anthropic 계속 검출)는 **토큰 인지가
필요**하고, 토큰 인지는 *scanner 만* 할 수 있다(호출자는 파일 경로만 안다).

### 2.3 Reviewer 판정 — **scanner 본문 allow-path (토큰 한정) 채택, §4.3 은 *명시적 보완* 으로 흡수**

| 평가축 | 호출자 `--exclude`(경로) | scanner 본문 allow-path(litellm 토큰) |
|--------|------------------------|-------------------------------------|
| §4.3 "scanner=white-list 무지" 철학 | ✅ 충실 | △ scanner 가 1개 면제 경로를 알게 됨 |
| **CS-2 (litellm 토큰 한정, 3개 합의)** | ❌ **불가** (경로 단위라 facade 전체 제외) | ✅ 가능 |
| facade 내 openai/anthropic 검출 유지 | ❌ 뚫림 | ✅ 유지 |
| 보안(차단 완전성) | △ facade 전체 사각 | ✅ litellm 만 면제 |
| "본문 변경 0건" | ✅ | ❌ 본문 변경 |
| 미끄럼(scanner 정책 카탈로그화, A R4) | ✅ 방지 | △ 리스크 존재 → MT 조건으로 완화 |

**결론**: CS-2(세 에이전트 만장일치 요구)가 §4.3(단일 에이전트가 인용한 단순화 원칙)보다
우선한다. CS-2 = 보안 본질(facade 내 provider 평등 enforcement 유지)이고, §4.3 = scanner
*단순화* 편의다. **보안 결과 > 구현 단순화** (CLAUDE.md 계산적 검증 우선 + ADR-011 안전 결과
= 본질). 토큰 한정 면제는 호출자 경로 제외로 *구현 불가능*하므로, **scanner 본문에 litellm
토큰 한정 allow-path 를 두는 것이 유일하게 CS-2 를 만족**한다.

§4.3 "본문 변경 0건"·"호출자 책임" 원칙은 폐기가 아니라 **명시적 예외로 흡수**:
PoC §4.3 를 *"단순 경로 제외는 호출자, 단 토큰-scoped 면제(facade×litellm)는 scanner 가
정확 경로 매칭으로 보유 — 토큰 인지가 호출자 레이어에서 불가하기 때문"* 으로 보강 기록.
A 의 R4(미끄럼 방지)는 **조건 MT-2(정확 경로 + 단일 토큰 + 답습 주석)**로 카탈로그화 방지.

> 주: A 도 본문 allow-path 를 "차선(동작함)"으로 인정했고, 1차 제안 수단 자체가 본문
> allow-path 였다. 본 판정은 A 의 §4.3 통찰(호출자 철학)을 MT-2 카탈로그화-방지 조건으로
> 보존하면서, CS-2(3개 합의) 충족 가능성을 우선한 절충이다.

---

## 3. 최종 합의 조건 (BLOCKING — 중복 제거 + 우선순위)

C-1~C-4(B) + fixture(C 5a) + 회귀가드(A 5) + 동적 면제 제외(B C-3) 를 통합:

| 번호 | 조건 | 우선순위 | 출처 통합 |
|------|------|---------|----------|
| **MT-1** | **litellm 토큰 한정 면제**: 면제 대상은 정확 경로 `src/adapters/llm/facade.py` × `litellm` 토큰 **만**. facade 내 openai/anthropic/ollama/google(.generativeai) 직접 import 는 계속 검출. 디렉터리·glob(`*facade*`)·전체 토큰 면제 금지 | BLOCKING | CS-2 (A§6.3 + B C-1 + C§4.1) |
| **MT-2** | **정확 경로 매칭 + 답습 주석**: `Path.as_posix()` repo-root 상대 정규화 정확 매칭(부분/glob 금지). 면제 근거 주석(design §4.1/§9.3 + PoC §2.4 + ADR-009 §2.2 #1)을 scanner 코드에 명시 → 미끄럼/카탈로그화 방지 | BLOCKING | A R4+GP-3 + B C-5 (정보→BLOCKING 승격: §2.3 미끄럼 완화 핵심) |
| **MT-3** | **동적 import 면제 제외**: 면제는 정적 `import litellm`(visit_Import/visit_ImportFrom)에만. importlib/`__import__`/exec 경유 litellm 은 facade 내부라도 검출 유지 | BLOCKING | B C-3 + PT-3. 실측: facade.py:143 = 정적 lazy |
| **MT-4** | **음성(negative) 회귀 테스트 3종** — 면제 과잉 적용 차단을 *계산적으로* 증명: (a) facade 경로 + `import openai` → **FAIL 유지**, (b) facade-외 경로 + `import litellm` → **FAIL 유지**, (c) facade 경로 + `import litellm` → **PASS** | BLOCKING | B C-2 + A§6.5 회귀가드 |
| **MT-5** | **PASS fixture oracle 결함 수정**: `facade_only.py` 가 실 `import litellm` 을 안 해 면제 누락을 못 잡았고, 또 fixture 가 white-list 경로라 구조적으로 검증 불가. → MT-4 의 negative test 를 **fixture 경로가 아닌** 검증 경로(예: scanner 단위 테스트로 facade.py 정확 경로를 직접 입력)에 배치하여 가이드=센서 일치 | BLOCKING | C 5a + GP-1. (MT-4 와 결합: MT-4 가 fixture 디렉터리에 들어가면 white-list 로 무력화되므로 MT-5 가 배치 위치를 규정) |
| **MT-6** | **`.importlinter` 헤더 책무 주석 정정**: line 8~14 의 "litellm = import-linter 책무"를 *"정적 litellm = import-linter(facade 외 전담) + facade 예외 = scanner 정확경로 면제 / 동적 litellm = scanner 전담"* 으로 동기화 | BLOCKING(문서 정합) | B C-4 + C§5.3. CLAUDE.md §7 문서 의존: `.importlinter` 책무 주석 ↔ scanner FORBIDDEN 정합 |

**우선순위 요약**: MT-1(범위) → MT-3(동적 제외) → MT-2(정확매칭+주석) = 면제 로직 정밀도.
MT-4+MT-5 = 계산적 회귀 증명(가장 중요한 센서). MT-6 = 문서 정합.

---

## 4. 최종 판단

### 4.1 전체 결론

**APPROVE WITH CONDITIONS** (세 에이전트 만장일치 결론 = APPROVE WITH CONDITIONS, Reviewer 동의)

### 4.2 채택 수단의 정확한 형태

1. **구현 위치 = scanner 본문 allow-path** (호출자 `--exclude` 아님).
   - 이유: 세 에이전트 만장일치 요구인 **litellm 토큰 한정(CS-2)**은 경로 단위 호출자 제외로는
     구현 불가능. 토큰 인지는 scanner 만 가능. 보안 결과(CS-2) > 구현 단순화(§4.3).
   - A 의 §4.3 호출자 철학은 폐기가 아니라 MT-2(정확경로+답습주석)로 카탈로그화-방지 흡수.
   - C 의 5b REJECT 근거(SSOT 분산)는 사실 오류였으나(real src 호출자는 pre-commit hook 단일),
     결론(본문 allow-path)은 다른 이유(토큰 인지 불가)로 동일하게 유효.
2. **allow-path 범위** = 정확 경로 `src/adapters/llm/facade.py` × `litellm` 토큰 한정, 정적
   import 만 (MT-1·MT-2·MT-3).
3. **fixture 수정** = MT-4 negative test 3종을 white-list 가 아닌 검증 경로(scanner 단위
   테스트)에 배치 + `facade_only.py` oracle 결함 보강 (MT-5).
4. **문서 동기화** = `.importlinter` 헤더 책무 주석 정정(MT-6) + PoC §4.3 보강 기록(토큰-scoped
   면제는 scanner 예외).

### 4.3 채택/기각 수단 요약

| 수단 | 판정 | 근거 |
|------|------|------|
| scanner 본문 facade×litellm allow-path (정적, 토큰 한정) | **채택** | CS-1, §2.3 |
| 호출자 `--exclude PATH`(경로 단위) | 기각 | CS-2(토큰 한정) 구현 불가 (§2.2-(2)) |
| litellm 을 FORBIDDEN 에서 제거 | 기각 | CS-3 (동적 litellm 회귀) |
| inline `# scanner-ignore` 주석 | 기각 | scanner 미지원 + 범용 백도어 (C§1, §2) |
| facade 구조 분리 | 기각 | CS-4 (단일 진입점 invariant 훼손) |
| facade lazy import 회피 | 기각 | A§5-D (Provider Liquidity 파괴) |

---

## 5. 사용자 결정 필요 잔여 항목

1. **(권고 채택 확인) 구현 위치 = scanner 본문 allow-path**. §4.3 단순화 원칙을 토큰-scoped
   예외로 보강하는 데 동의하는가? (대안: §4.3 문자 그대로 호출자 경로 제외 — 단 이 경우
   facade 내 openai/anthropic 검출 포기 = CS-2 미충족, Reviewer 비권장)
2. **MT-2/MT-5 의 "정확 경로" 단일 진실원**: 면제 경로 상수를 scanner 코드 내 상수로 둘지,
   PoC §2.4 white-list 표를 단일 출처로 참조할지(미래 docker PoC 경로 등 확장 대비). Reviewer
   권고 = 현 시점 facade 1경로 코드 상수 + 답습 주석(과설계 회피, 비례성). 확장 trigger 시 재논의.
3. **MT-6 문서 정정 주체**: `.importlinter` 헤더 주석 정정을 본 PR 에 포함할지, 별도 docs 커밋으로
   분리할지 (CLAUDE.md §7 연쇄 확인 — scanner FORBIDDEN ↔ `.importlinter` 책무 주석).
4. **GP-2 (facade 내 litellm-외 SDK 양쪽 사각) 별도 추적 여부**: import-linter `facade -> *`
   전체 ignore + scanner litellm-외만 검출 → facade 내 *동적* openai 등은 여전히 코드 리뷰
   영역. 별도 이슈로 추적할지 (비BLOCKING, 기존 gap).

---

## 6. 구현 진입 가능 여부

**가능 — 단 MT-1~MT-6 BLOCKING 6조건 충족 전제 + 잔여 결정 #1(구현 위치 확정) 사용자 승인 후.**

- 단순 버그 fix 아님(보안 enforcement + SDD 정합 + 문서 연쇄) → CLAUDE.md §3 매트릭스상 3+1
  합의 적용 정당. 본 합의로 다관점 검증 완료.
- TDD: MT-4 negative test(RED) 먼저 작성 → allow-path 구현(GREEN) → MT-2 주석/정규화
  (REFACTOR) 순서 권고.
- 구현 위치(잔여 #1) 확정만 사용자 승인 받으면 별도 작업 브랜치에서 즉시 진입 가능.
