# 3+1 합의 보고서 — G2 GP-5 2차 PoC 구현 (Reviewer-only 단축)

> **세션**: 2026-05-10 후속 (Group A 2차 — 본 PoC 구현)
> **합의 형식**: **Reviewer-only 단축** (escalation triggers TR-1~TR-5 0/5 발화 → 단축 적격)
> **검토 대상**: 본 PoC 구현 산출물 (`.importlinter`, `requirements-dev.txt`, `src/` placeholder, `tests/fixtures/.../fail/transitive_import.py`, `.github/workflows/...` 갱신, `docs/phase0/g2-gp5-poc2-import-linter-implementation.md`)
> **상위 합의**: docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md (T-2 import-linter APPROVE WITH CONDITIONS)
> **답습 권위**: ADR-008 부록 C, ADR-009 C-N §2.3+§5, ADR-011 §2.1 (a)~(e), llm-providers-design.md §9.3

---

## 1. 검토 사항

### 1.1 산출물 6건

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `.importlinter` config | ~35 | 합의 §5.2 채택 7항목 |
| 2 | `requirements-dev.txt` | ~12 | TR-2 답습 |
| 3 | `src/` placeholder (4 파일) | ~45 | C-3 답습 (옵션 A) |
| 4 | `tests/fixtures/.../fail/transitive_import.py` | ~25 | C-4 답습 (1차 fixture 재사용 + 1건 추가) |
| 5 | `.github/workflows/provider-adapter-enforcement.yml` 갱신 | +60 | C-5 답습 (CI-A) |
| 6 | `docs/phase0/g2-gp5-poc2-import-linter-implementation.md` | ~140 | 본 PoC 사양 |

### 1.2 로컬 양방향 검증 결과 (5/5 PASS)

| 검증 | 명령 | rc | 결과 |
|------|------|-----|------|
| 1차 PASS fixture | `python3 tools/provider_import_scanner.py tests/fixtures/.../pass/` | 0 | 위반 0건 ✅ |
| 1차 FAIL fixture | `python3 tools/provider_import_scanner.py tests/fixtures/.../fail/` | 1 | 5건 위반 (transitive_import.py 회귀 통과) ✅ |
| 1차 src/ 회귀 | `python3 tools/provider_import_scanner.py src/` | 0 | FP 0건 (placeholder facade.py FP 없음) ✅ |
| 2차 PASS | `PYTHONPATH=. lint-imports` | 0 | "1 kept, 0 broken" ✅ |
| 2차 FAIL probe | (probe 삽입 → `lint-imports` → 제거) | 1 | `src.__transitive_probe__ -> openai (l.1)` 정확 검출 ✅ |

---

## 2. 검토 항목 — Reviewer 관점 8 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 여부 | 근거 |
|------|---------|------|
| (a) 안전 결과 본질 식별 | ✅ | 본 PoC 사양 §0 + transitive provider lock-in 회피 명시 |
| (b) 수단 변경 사전 인지 | ✅ | TR-1~TR-5 등록 (합의 §5.4 답습) + 본 PoC 사양 §8 |
| (c) 안전 결과 보존 검증 | ✅ | 5/5 양방향 검증 PASS (§1.2) |
| (d) 폐기 경로 | ✅ | requirements-dev.txt 1줄 제거 + .importlinter 1 파일 제거 |
| (e) 외부 검증 가능성 | ✅ | CI log + import-linter stdout + commit SHA + Evidence Ledger entry 형식 |

### 2.2 합의 추가 조건 답습 (C-1~C-10)

| # | 조건 | 답습 검증 |
|---|------|---------|
| C-1 | G2 GP-5 부분 충족 시제 한정 | ✅ 본 PoC 사양 §0 + 본 보고서 §4.2 명시 |
| C-2 | Implementation/Runtime PASS 자동 선언 미발생 | ✅ 본 보고서 §4.2 명시 |
| C-3 | 옵션 A (`src/` 만, 검사 대상 0건 인식) | ✅ placeholder facade.py 만 |
| C-4 | 1차 fixture 재사용 + transitive_import.py 1건 | ✅ 신규 fixture 1건 (FAIL fixture 5건 카운트 회귀 통과) |
| C-5 | CI-A — 1차 workflow step 추가 | ✅ `.github/workflows/...` 단일 workflow 답습 |
| C-6 | 책무 분담 매트릭스 명시 | ✅ 본 PoC 사양 §1 + .importlinter 주석 |
| C-7 | 외부 LLM L76 silent fail 위험 명시 | ✅ 본 PoC 사양 §6 |
| C-8 | URL 차단 = 3차 분리 (본 PoC 미해소) | ✅ 본 PoC 사양 §7 |
| C-9 | RA-9 사전 검증 PASS | ✅ C-9 보고서 (위 §1.2 답습) |
| C-10 | TR-1~TR-5 등록 | ✅ 본 PoC 사양 §8 |

### 2.3 답습 충실성 (신규 정책 발명 0건)

| 항목 | 답습 출처 | 신규 발명? |
|------|----------|----------|
| forbidden_modules 4종 | 합의 §5.2 #3 | 답습 (5종 → 4종 명시 갱신, 각주 1) |
| ignore_imports = facade -> * | §4.1 답습 | 답습 |
| include_external_packages = True | C-9 검증 + Agent A §4.4 | 답습 |
| transitive probe 패턴 | 합의 §5.5 transitive 차단 효과 | 답습 |
| Evidence Ledger entry 형식 | 합의 §5.6 | 답습 |
| 책무 분담 매트릭스 | 합의 §5.5 + 각주 1 | 답습 (각주 1 명시 갱신) |

**판정**: 신규 발명 0건. 합의 §5 본문을 *코드/config* 로 변환만 수행.

### 2.4 6 금지목록 충실성 (사용자 명시 답습)

| # | 금지 | 위반? |
|---|------|------|
| 1 | G2 GP-5 최종 PASS 자동 선언 | ❌ 미위반 — 본 PoC = "부분 충족 시제" 답습 |
| 2 | G2 전체 Implementation/Runtime PASS 자동 선언 | ❌ 미위반 |
| 3 | Hermes PMO 격상 선언 | ❌ 미위반 |
| 4 | 실제 provider API key 사용 | ❌ 미위반 |
| 5 | 실제 외부 API 호출 | ❌ 미위반 (lint-imports 정적 분석만) |
| 6 | Provider 구현 자체 변경 | ❌ 미위반 (Layer 1 형식 차단만, facade placeholder) |

### 2.5 escalation triggers 0/5 발화

| # | Trigger | 발화? | 비고 |
|---|---------|------|-----|
| TR-1 | facade.py real 본문 작성 | ❌ | placeholder 만 |
| TR-2 | pyproject.toml 신설 | ❌ | requirements-dev.txt 만 (단순 dev-dep 등재) |
| TR-3 | `include_external_packages = True` 동작 불가 | ❌ | C-9 PASS |
| TR-4 | 책무 분담 임의 흡수 | ❌ | 명시 갱신만 (각주 1, 사용자 답습) |
| TR-5 | T-9 pre-commit hook 도입 | ❌ | 미발화 |

**판정**: 0/5 발화 → **Reviewer-only 단축 합의 적격**.

### 2.6 책무 분담 명시 검증 (C-6)

| 검증 항목 | 1차 | 2차 | 3차 | 라운드트립 |
|---------|-----|-----|------|----------|
| Direct (4종) | ✅ | ✅ 중첩 | — | — |
| Direct (`google.generativeai`) | ✅ 단독 | ❌ 도구 제약 | — | — |
| From-import | ✅ | ✅ 중첩 | — | — |
| **Transitive** | ❌ | **✅ 신규** | — | — |
| 동적 import | ✅ 전담 | ❌ | — | — |
| 모델명 분기 | ✅ 전담 | ❌ | — | — |
| URL 하드코딩 | ❌ | ❌ | ✅ 별도 | — |
| 의미적 lock-in | ❌ | ❌ | ❌ | ✅ |

✅ 명시 충실. .importlinter 주석 + 본 PoC 사양 §1 + CI workflow 주석 3곳에 답습.

### 2.7 Evidence Ledger entry 형식 (합의 §5.6)

CI workflow 의 Evidence summary step 에 답습:
- `event: provider_adapter_enforcement_layer1_static`
- `agent: user`
- `ledger_layer: Layer 1 (Entry) — 1차 AST scanner + 2차 import-linter`

✅ 합의 §5.6 답습.

### 2.8 메타-템플릿 답습성

| 영역 | 추가 항목 | runtime application 코드? |
|------|----------|------------------------|
| `src/` 신설 | placeholder facade.py | ✗ (NotImplementedError stub) |
| `requirements-dev.txt` | dev-dep 1개 | ✗ (도구 manifest) |
| `.importlinter` | config | ✗ (도구 설정) |
| fixture 신규 1건 | transitive_import.py | ✗ (검증 fixture) |
| CI workflow | step 추가 | ✗ (자동화) |

✅ 전체 산출물이 *하네스/거버넌스 측 코드*. **application runtime 0건**.

---

## 3. 누락/이견/추가 권장 사항

### 3.1 누락 (Gap)

| # | 항목 | 영향 | 권장 처리 |
|---|------|------|---------|
| G-1 | `src/__transitive_probe__.py` 가 CI 실패 시 *cleanup 보장* — 현재 `rm -f` 로 처리 단, CI step 중간 실패 시 잔존 위험 | 中 | `if: always()` cleanup step 추가 (2차 후속) |
| G-2 | `.gitignore` 갱신 — `src/__transitive_probe__.py` 우발적 commit 차단 | 低 | 2차 후속 |
| G-3 | C-9 검증 환경 (venv `/tmp/c9-ra9-verify/`) cleanup | 低 | 본 PoC commit 후 정리 |

### 3.2 이견 (Divergence)

이견 0건 — Reviewer 관점에서 본 PoC 구현은 합의 §5 답습 충실.

### 3.3 추가 권장 (Recommendation)

| # | 권장 | 우선순위 | 처리 시점 |
|---|------|--------|---------|
| R-1 | `.gitignore` 추가 — `src/__transitive_probe__.py` + `.venv-*` | LOW | 본 PoC commit 후 보조 |
| R-2 | C-9 검증 venv 정리 | LOW | 본 PoC commit 후 보조 |
| R-3 | CI cleanup `if: always()` | MID | 2차 후속 (별도 합의 trigger 미발화) |
| R-4 | `pyproject.toml` (PEP 621) 도입 검토 | HIGH | TR-2 발화 시점 (현재 미진입) |
| R-5 | 3차 PoC (URL/endpoint 하드코딩 grep) 별도 합의 | HIGH | C-8 답습 (별도 합의 trigger 발화) |

본 보고서는 권장 사항을 *향후 처리* 로 분리 — *본 PoC 자체 PASS 판정에 영향 없음*.

---

## 4. 최종 판정

### 4.1 Design/Governance Gate (G2 GP-5 2차 PoC 구현) — ✅ APPROVE WITH CONDITIONS

**APPROVE 조건**:

1. ✅ ADR-011 §2.1 (a)~(e) 5/5 충족
2. ✅ 합의 추가 조건 C-1~C-10 10/10 답습
3. ✅ 5/5 양방향 검증 PASS
4. ✅ 6 금지목록 0/6 위반
5. ✅ escalation triggers 0/5 발화
6. ✅ 신규 정책 발명 0건
7. ✅ Evidence Ledger entry 형식 답습

**WITH CONDITIONS** (본 PoC 자체 PASS 와 무관 — *향후 작업 처리*):

1. **C-Imp-1**: TR-1 발화 (facade.py real 본문) 시 풀 3+1 재합의
2. **C-Imp-2**: 3차 PoC (URL 차단) 별도 합의 — 본 PoC 채택이 *URL 책무 해소* 로 해석되지 않음
3. **C-Imp-3**: TR-2 (pyproject.toml) 발화 시 별도 합의
4. **C-Imp-4**: G-1 (probe cleanup) 보강 — 2차 후속 보조

### 4.2 Implementation/Runtime PASS 자동 선언 — 미선언 (사용자 명시 답습)

본 PoC 는 *Layer 1 형식 차단 강화 시제* 로서 G2 GP-5 의 PASS 조건 *부분 충족 시제* 이며, **G2 전체 Implementation/Runtime PASS 선언 권한이 없음**. 본 보고서는 *사양 + 시제 + 양방향 검증* 의 *증거 등재* 만.

---

## 5. 다음 단계

| 단계 | 작업 | 합의 형식 |
|------|------|---------|
| 1 | 본 PoC 산출물 6건 + 본 보고서 commit + push | 사용자 명시 |
| 2 | Group A 종료 판단 — 다음 진입점 (Group B/C/D 또는 3차 grep PoC, Group A 추가 보강) | 사용자 명시 |
| 3 | (별도 합의) 3차 grep PoC — URL/endpoint 하드코딩 차단 | 별도 trigger |

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
| 합의 추가 조건 답습 | 10/10 (C-1~C-10) |
| 양방향 검증 | 5/5 PASS |
| Evidence 5형식 | 답습 |

---

## 7. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 (Group A 2차 후속) | 신규 작성 | G2 GP-5 2차 PoC 구현 Reviewer-only 단축 합의 — APPROVE WITH CONDITIONS |
