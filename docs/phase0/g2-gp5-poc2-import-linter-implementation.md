# G2 GP-5 2차 PoC — import-linter 구현 사양 (T-2 채택)

> **상태**: DRAFT (2026-05-10 후속, Group A 2차)
> **선행**: 1차 PoC (commit a3693a0 + 0f503a4) + 2차 합의 (commit cfa0db0 + scope b683e15)
> **합의 권위**: docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md (T-2 import-linter APPROVE WITH CONDITIONS)
> **C-9 검증**: PASS (2026-05-10) — `include_external_packages = True` 정상 동작

---

## 0. 본 PoC 산출물

| 산출물 | 경로 | 책무 |
|--------|------|------|
| `.importlinter` config | `/.importlinter` | 4종 forbidden + facade allow |
| dev-dep manifest | `/requirements-dev.txt` | import-linter 2.11 등재 |
| placeholder src/ | `/src/{__init__.py, adapters/__init__.py, adapters/llm/__init__.py, adapters/llm/facade.py}` | future-proof 시제 (PASS fixture) |
| transitive 문서화 fixture | `/tests/fixtures/provider_adapter_enforcement/fail/transitive_import.py` | 1차 검사 대상 (위반 0건 — transitive 시뮬레이션) |
| CI workflow | `/.github/workflows/provider-adapter-enforcement.yml` | 1차 + 2차 양방향 검증 통합 |
| 본 사양 | `/docs/phase0/g2-gp5-poc2-import-linter-implementation.md` | 본 PoC 사양 + Evidence 5형식 |

---

## 1. 책무 분담 매트릭스 (합의 §5.5 + 각주 1 답습)

| 검증 항목 | 1차 AST scanner | 2차 import-linter |
|----------|---------------|-----------------|
| Direct (`openai`/`anthropic`/`litellm`/`ollama`) | ✅ | ✅ (중첩 강화) |
| Direct (`google.generativeai`) | ✅ (단독) | ❌ (도구 제약 — 각주 1 답습) |
| From-import | ✅ | ✅ (중첩 강화) |
| **Transitive (A→B→forbidden)** | ❌ | **✅ (2차 신규 가치)** |
| 동적 import (`importlib`, `__import__`) | ✅ (전담) | ❌ |
| 모델명 분기 (문자열) | ✅ (전담) | ❌ |
| URL/endpoint 하드코딩 | ❌ | ❌ (3차 영역 — 별도 합의) |
| 의미적 lock-in | ❌ | ❌ (라운드트립 영역) |

---

## 2. 양방향 검증 시나리오

### 2.1 PASS (정상 src/)

```
$ PYTHONPATH=. lint-imports
Analyzed N files, M dependencies.
No direct LLM SDK imports outside facade KEPT
Contracts: 1 kept, 0 broken.
exit=0
```

### 2.2 FAIL (임시 transitive probe)

```
$ cat > src/__transitive_probe__.py <<EOF
import openai
EOF
$ PYTHONPATH=. lint-imports
Contracts: 0 kept, 1 broken.
src.__transitive_probe__ -> openai (l.2)
exit=1
$ rm src/__transitive_probe__.py
```

CI workflow 가 자동으로 probe 삽입/제거 (`.github/workflows/provider-adapter-enforcement.yml`).

---

## 3. PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 본 PoC 충족 |
|------|----------|
| (a) 안전 결과 본질 식별 | "transitive provider lock-in 회피 = 안전 결과" |
| (b) 수단 변경 사전 인지 | TR-1~TR-5 등록 (합의 §5.4 답습) |
| (c) 안전 결과 보존 검증 | PASS exit 0 + FAIL probe exit 1 양방향 |
| (d) 폐기 경로 | requirements-dev.txt 1줄 제거 + .importlinter 1 파일 제거 |
| (e) 외부 검증 | CI log + import-linter stdout + commit SHA |

---

## 4. Evidence Ledger entry 형식 (합의 §5.6 답습)

| 필드 | 본 PoC 값 |
|------|---------|
| event | `provider_adapter_enforcement_layer1_static` |
| agent | `user` |
| violation_type | `direct-import` (4종) / `transitive-import` (cascading) |
| tool | `import-linter==2.11` (T-2) |
| commit_sha | (실 commit) |
| ledger_layer | `Layer 1 (Entry)` |

---

## 5. 추가 조건 답습 (합의 §5.3 C-1~C-10)

| # | 조건 | 본 PoC 답습 |
|---|------|----------|
| C-1 | G2 GP-5 부분 충족 시제 한정 — 최종 PASS 권한 없음 | 본 사양 §0 명시 |
| C-2 | Implementation/Runtime PASS 자동 선언 미발생 | 본 사양 §0 + 합의 답습 |
| C-3 | 옵션 A (`src/` 만) — 검사 대상 0건 인식 | placeholder facade.py 만 |
| C-4 | 1차 fixture 재사용 + transitive_import.py 1건 | tests/fixtures/.../fail/transitive_import.py |
| C-5 | CI-A — 1차 workflow step 추가 | .github/workflows/provider-adapter-enforcement.yml 갱신 |
| C-6 | 책무 분담 매트릭스 명시 | 본 사양 §1 |
| C-7 | 외부 LLM L76 silent fail 위험 명시 | 본 사양 §6 |
| C-8 | URL 차단 = 3차 분리 (본 PoC 미해소) | 본 사양 §7 |
| C-9 | RA-9 사전 검증 PASS | C-9 보고서 (2026-05-10) |
| C-10 | TR-1~TR-5 등록 | 합의 §5.4 + 본 사양 §8 |

---

## 6. 외부 LLM L76 답습 — silent fail 위험 (C-7)

본 PoC 채택 시 *2 도구 운영* (1차 AST scanner + 2차 import-linter) — silent fail 위험 ↑.

완화 매커니즘:
1. **CI fail-closed** — 어느 도구가 정상 동작 안 하면 CI 실패 (rc 검증)
2. **책무 분담 명시** — 어떤 위반을 어느 도구가 담당하는지 §1 매트릭스 답습
3. **PR review 보조** — *추론적 보조 layer* 별도 유지 (외부 LLM L76 답습)

---

## 7. URL 하드코딩 차단 — 본 PoC 영역 외 (C-8)

본 PoC 가 *URL/endpoint 하드코딩* (예: `https://api.anthropic.com/v1/messages` 직접 박는 코드) 을 차단하지 *않는다*. 이는 **별도 3차 PoC** 합의 영역.

본 PoC 채택이 *URL 차단 책무 해소* 로 *과대 해석* 되지 않도록 명시.

---

## 8. 재합의 trigger 등록 (C-10)

| Trigger | 발화 조건 | 재합의 의제 |
|--------|---------|-----------|
| TR-1 | `src/adapters/llm/facade.py` real 본문 (LiteLLM 실 import) 작성 | T-2 룰 ignore_imports 검증 + LiteLLM 정상 동작 |
| TR-2 | `pyproject.toml` 신설 | dev-dep 도입 영향 분석 (현 시점 `requirements-dev.txt` 만) |
| TR-3 | `include_external_packages = True` 옵션 *동작 불가* 판명 | 도구 재선택 (C-9 검증 PASS, 현 시점 미발화) |
| TR-4 | 책무 분담 매트릭스 *임의 흡수* 시도 | 책무 분리 재합의 (`google.generativeai` 부분 발화 — 명시 갱신만, 사용자 답습) |
| TR-5 | T-9 (pre-commit hook) 도입 별도 합의 | 본 2차 PoC 와의 책무 분리 |

---

## 9. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차 후속) | 신규 작성 | 본 PoC 구현 사양 — T-2 import-linter 채택 + 양방향 검증 + Evidence 5형식 |
