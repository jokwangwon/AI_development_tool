# 3+1 합의 보고서 — G2 GP-5 Provider Adapter Enforcement 1차 PoC (Reviewer-only 단축)

> **세션**: 2026-05-09 후속 1 (Group A 1차 PoC)
> **합의 형식**: Reviewer-only 단축 (escalation triggers 0/5 발화 → 단축 합의 적격)
> **검토 대상**: docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md, tools/provider_import_scanner.py, tests/fixtures/provider_adapter_enforcement/{pass,fail}/, .github/workflows/provider-adapter-enforcement.yml
> **답습 권위**: ADR-008 부록 C, ADR-009 C-N §2.3+§5, ADR-011 §2.1 (a)~(e), llm-providers-design.md §9, implementation-runtime-roadmap.md Group A

---

## 1. 검토 사항

### 1.1 PoC 산출물 (4건 + 본 합의 보고서)

| # | 산출물 | 라인수 | 답습 매핑 |
|---|-------|-------|----------|
| 1 | docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md | 약 230 | §9 + ADR-011 §2.1 + R-1~R-9 |
| 2 | tools/provider_import_scanner.py | 약 165 | §9.4 (AST 동적 import 차단) |
| 3 | tests/fixtures/provider_adapter_enforcement/pass/facade_only.py | 약 40 | §4.1 (facade allow path 모사) |
| 4 | tests/fixtures/provider_adapter_enforcement/fail/{direct_import,from_import,dynamic_importlib,double_underscore_import,model_name_branch}.py × 5 | 각 약 10 | §9.1 #1 + §9.4 |
| 5 | .github/workflows/provider-adapter-enforcement.yml | 약 65 | §9.3 + 본 PoC 사양 §5 |

### 1.2 로컬 검증 결과 (Evidence 5형식 — 검증 완료)

```
[PASS fixture]
$ python3 tools/provider_import_scanner.py tests/fixtures/provider_adapter_enforcement/pass/
[PASS] No violations found in: tests/fixtures/provider_adapter_enforcement/pass
exit=0  ✓ (기대값 일치)

[FAIL fixture]
$ python3 tools/provider_import_scanner.py tests/fixtures/provider_adapter_enforcement/fail/
tests/fixtures/provider_adapter_enforcement/fail/double_underscore_import.py:8:double-underscore-import:openai
tests/fixtures/provider_adapter_enforcement/fail/from_import.py:5:from-import:anthropic
tests/fixtures/provider_adapter_enforcement/fail/direct_import.py:5:direct-import:openai
tests/fixtures/provider_adapter_enforcement/fail/model_name_branch.py:8:model-name-branch:claude-opus-4-7
tests/fixtures/provider_adapter_enforcement/fail/dynamic_importlib.py:9:dynamic-importlib:litellm
[FAIL] 5 violation(s) found.
exit=1  ✓ (기대값 일치)
```

5/5 패턴 정확 매칭 — false positive 0건, false negative 0건.

---

## 2. 검토 항목 — Reviewer 관점 6 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 여부 | 근거 |
|------|---------|------|
| (a) 안전 결과 본질 식별 | ✅ | 사양 §0 — "provider lock-in 회피 = 안전 결과" 명시, ADR-009 C-N §2.3 영구 권위 인용 |
| (b) 수단 변경 사전 인지 | ✅ | 사양 §1.2 — depcruise/pre-commit/Docker 분리, 각각 별도 합의 명시 |
| (c) 안전 결과 보존 검증 | ✅ | scanner exit code + fixture 양방향 + Evidence 5형식 |
| (d) 폐기 경로 | ✅ | §6 R-1~R-9 매핑, R-8/R-9 가 핵심 방어선 명시 |
| (e) 외부 검증 가능성 | ✅ | scanner output + commit SHA + GitHub Actions log 모두 외부 등재 가능 |

### 2.2 답습 충실성 (신규 정책 발명 0건)

| 항목 | 답습 출처 | 신규 발명? |
|------|----------|----------|
| FORBIDDEN_PROVIDERS 목록 | §9.3 forbidden.to.path | 답습 (litellm/anthropic/openai/google.generativeai/ollama) |
| AST 패턴 5종 | §9.4 패턴 + §9.1 #1 | 답습 |
| 허용 경로 white-list | §4.1 (facade.py 단일) | 답습 |
| MODEL_PATTERN_REGEX | §9.3 #3 (claude-opus-/gpt-/gemini-) | 답습 (보수적 — claude-opus-/claude-sonnet-/gpt-/gemini-) |
| Evidence 5형식 | ADR-012 §원칙 6 + 본 사양 §5.4 | 답습 |
| Rollback R-1~R-9 매핑 | ADR-009 C-N §5 + ADR-011 §8 | 답습 |

**판정**: 신규 발명 0건. §9 본문을 *형식 차단 시제* 로 변환만 수행.

### 2.3 6 금지목록 충실성 (사용자 명시 답습)

| # | 금지 항목 | 위반 여부 |
|---|----------|---------|
| 1 | Hermes PMO escalation 자동 선언 | 미위반 — 본 PoC 는 Layer 1 형식 차단만, PMO escalation 무관 |
| 2 | Implementation/Runtime PASS 자동 선언 | 미위반 — 본 PoC 자체는 Implementation/Runtime *PASS 기준 충족 시제* 만, 자동 선언 없음 |
| 3 | ADR 본문 자동 변경 | 미위반 — ADR 본문 0건 변경 |
| 4 | Runtime 실 코드 작성 | 미위반 — `src/adapters/llm/facade.py` real 본문 0건 작성. fixture 만 작성 |
| 5 | Tier-2/3 카탈로그 자동 확장 | 미위반 — Tier 카탈로그 0건 변경 |
| 6 | 사용자 확인 없는 과도 구현 | 미위반 — 사용자 명시 확인 후 권장 범위로만 진행 (depcruise/pre-commit/Docker 분리) |

### 2.4 Provider Liquidity 5-way Multi-layer Defense 매핑

| Layer | 본 PoC 와의 관계 | 책무 분리 명확성 |
|-------|----------------|---------------|
| Layer 1 (Entry) | **본 PoC = Layer 1 형식 차단 1차 시제** | ✅ 명시 |
| Layer 2 (Runtime) | 미적용 (2차 이후) | ✅ 분리 명시 |
| Layer 3 (Memory/Skill) | 무관 | ✅ |
| Layer 4 (Vault) | 무관 | ✅ |
| Layer 5 (Evidence) | scanner output + commit SHA 등재 | ✅ |

### 2.5 escalation triggers 0/5 발화 확인

| # | Trigger | 발화? |
|---|---------|------|
| 1 | depcruise / pre-commit / Docker 도입 | ✗ (분리 명시) |
| 2 | runtime real `adapters/llm/facade.py` 본문 신규 작성 | ✗ (fixture 모사만) |
| 3 | tests/fixtures/ 외 real source tree 변경 | ✗ (tools/ + .github/ 만 신규) |
| 4 | Tier-2/3 카탈로그 자동 확장 | ✗ |
| 5 | ADR-013/014 본문 자동 발급 | ✗ |

**판정**: 0/5 발화 → Reviewer-only 단축 합의 적격.

### 2.6 메타-템플릿 답습성

본 PoC 는 *코드 0줄 메타-템플릿 환경* 에서 **runtime 코드 신규 발명** 의 위험 없이 진행 가능한 1차 시제로 적합:

- `tools/provider_import_scanner.py` — 도구 (Layer 0.5 자동화 보조), runtime *application* 코드 아님
- `tests/fixtures/...` — 검증 fixture, runtime 코드 아님
- `.github/workflows/...` — CI 자동화, runtime 코드 아님
- `docs/phase0/...` — 사양 문서

전체 산출물이 **하네스/거버넌스 측 코드** 이며, **application runtime** 0건.

---

## 3. 누락/이견/추가 권장 사항

### 3.1 누락 (Gap)

| # | 항목 | 영향 | 권장 처리 |
|---|------|------|----------|
| G-1 | scanner 의 `tests/fixtures/` 자체 재귀 호출 시 무한 false positive | 본 PoC 영향 ✗ (CI 가 명시 디렉터리만 검사) | 2차 — 전체 repo grep 시 white-list 디렉터리 인자 추가 |
| G-2 | `model-name-branch` 패턴이 *문서 안의 모델 ID 인용* (예: README 의 "claude-opus-4-7") 도 잡을 수 있음 | 본 PoC 영향 ✗ (.py 파일만 검사) | 2차 — yaml/md 검사 도입 시 별도 룰 |
| G-3 | LiteLLM yaml 형식 (`anthropic/claude-opus-4-7`) 의 alias 부분은 모델명 정규식과 충돌 가능 | 본 PoC 영향 ✗ (yaml 검사 미포함) | 2차 — yaml 룰 도입 시 명시적 alias 허용 |

### 3.2 이견 (Divergence)

이견 0건 — Reviewer 관점에서 본 PoC 의 *축소 범위* 는 사용자 명시 답습 + 위험 최소화로 적정.

### 3.3 추가 권장 (Recommendation)

| # | 권장 | 우선순위 | 처리 시점 |
|---|------|--------|----------|
| R-1 | scanner 에 `--allow-path` 옵션 추가 — white-list 디렉터리 호출자 외부화 가능 | LOW | 2차 |
| R-2 | scanner 출력에 JSON 모드 추가 — Evidence ledger 자동 등재 용이 | MID | 2차 |
| R-3 | `model-name-branch` 패턴을 `.py` 외 `.yaml`/`.md` 로 확장 | MID | 2차 |
| R-4 | depcruise rule 도입 (별도 합의) | HIGH | 2차 |
| R-5 | runtime egress 차단 (R-2/R-4.1 답습 Docker isolation) | HIGH | 3차 |

본 보고서는 1차 권장 사항을 *향후 처리* 로 분리 — *본 PoC 자체 PASS 판정에 영향 없음*.

---

## 4. 최종 판정

### 4.1 Design/Governance Gate (G2 GP-5 1차 PoC) — ✅ APPROVE WITH CONDITIONS

**APPROVE 조건**:

1. ✅ ADR-011 §2.1 (a)~(e) 5/5 충족
2. ✅ §9.1 #1 + §9.4 답습 충실 (신규 발명 0건)
3. ✅ 6 금지목록 0/6 위반
4. ✅ escalation triggers 0/5 발화
5. ✅ Evidence 5형식 양방향 검증 (PASS exit 0 + FAIL exit 1, 5/5 패턴 매칭)

**WITH CONDITIONS** (본 PoC 자체 PASS 와 무관 — *향후 작업 진행 시* 처리):

1. C-1: depcruise rule 도입은 *별도 합의* 필수 (풀 3+1 발화 trigger)
2. C-2: runtime egress 차단 도입 시 R-2/R-4.1 답습 Docker isolation 명시 답습
3. C-3: scanner 가 `tests/fixtures/` 외 *real source tree* 검사 대상 확장 시 본 사양 §1.2 제외 항목 재검토
4. C-4: Implementation/Runtime PASS 4 Gate 자동 선언은 본 PoC 와 *무관* — 별도 합의 trigger 발화 시점에 별도 처리

### 4.2 Implementation/Runtime PASS 자동 선언 — 미선언 (사용자 명시 답습)

본 PoC 는 *Layer 1 형식 차단 시제* 로서 G2 GP-5 의 PASS 조건 *부분 충족* 시제이며, **G2 전체 Implementation/Runtime PASS 선언 권한이 없음**. 본 보고서는 *사양 + 시제 + 검증* 의 *증거 등재* 만 수행.

---

## 5. 다음 단계 (Group A 진행)

| 단계 | 작업 | 합의 형식 |
|------|------|----------|
| Group A 후속 | 본 4 commits push (사양 + scanner + fixture + workflow + 본 합의 보고서) | 사용자 명시 |
| Group A 2차 | depcruise rule 도입 검토 (풀 3+1 발화) | 풀 3+1 |
| Group A 3차 | runtime egress 차단 (R-2/R-4.1 답습) | 풀 3+1 |
| Group A 종료 후 | Group B/C/D 병렬 작업 | implementation-runtime-roadmap.md |

---

## 6. 합의 보고서 검증 메타

| 항목 | 값 |
|------|---|
| 합의 형식 | Reviewer-only 단축 |
| escalation triggers 발화 | 0/5 (단축 적격) |
| 검토자 | Reviewer (메인 컨텍스트) |
| 답습 권위 누락 | 0건 |
| 신규 정책 발명 | 0건 |
| 사용자 명시 위반 | 0건 |
| Evidence 5형식 | 5/5 충족 |

---

## 7. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-09 (후속 1, Group A) | 신규 작성 | G2 GP-5 1차 PoC Reviewer-only 단축 합의 — APPROVE WITH CONDITIONS |
