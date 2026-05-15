# Reviewer-only 단축 합의 보고서 — Phase α-2 R-5 `.importlinter` 본문 진입 Brief

> **본 문서는 `docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md` (DRAFT, commit `608a046`) 의 Reviewer-only 단축 합의 보고서.** 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 `.importlinter` 수정은 아직 하지 않음.") 답습.
>
> 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** — 실 변경 0건. Phase α-2 실 진입 / `.importlinter` 본문 변경 / `requirements-dev.txt` 변경 / `src/adapters/llm/facade.py` real 본문 작성 / Phase α-1 / α-3 / α-4 자동 진입 / Layer C 발효 / MVP-1 PASS / 7 금지 영역 해소 / TR-1 ~ TR-5 발화 모두 본 합의 영역 외.

**작성일**: 2026-05-14 후속 12
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**검토 대상**: `docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md` (commit `608a046`, 710줄)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-10-g2-gp5-poc2-depcruise-full.md` (Group A 2차 풀 3+1 합의 — T-2 import-linter APPROVE WITH CONDITIONS, C-1 ~ C-10 + TR-1 ~ TR-5)
- `docs/phase0/g2-gp5-poc2-import-linter-implementation.md` (T-2 채택 구현 사양 + C-9 RA-9 PASS 답습 + 각주 1)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5.2 (T-6 = T-2 + T-5 병행, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역

---

## 0. 본 합의 범위

### 0.1 사용자 명시 진입 명령 답습

> "옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 `.importlinter` 수정은 아직 하지 않음."

사용자 명시 7 금지 답습 (Backlog #6 우선 진입 합의 + 본 brief §0.3 답습):

1. ❌ 실 `.importlinter` 수정 금지 — `.importlinter` 본문 어느 줄도 변경 0건 (현 35줄 답습)
2. ❌ CI workflow 변경 금지
3. ❌ branch protection 변경 금지
4. ❌ dev 환경 강제 금지
5. ❌ `pre-commit install` 의무화 금지
6. ❌ Operational Readiness PASS 선언 금지
7. ❌ Hermes PMO 격상 금지

### 0.2 본 합의가 *하는* 것

1. Brief `phase-alpha-2-r5-importlinter-body-entry-brief.md` (DRAFT, `608a046`) 의 **수단 결정 적격성 권위 권고** 발행
2. **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-2 영역 답습** 확인
3. **Phase α-2 = R-5 `.importlinter` 본문 영역 정의** 채택 권고 (35줄 본문 + 7 항목 + 책무 분담 매트릭스)
4. **`.importlinter` PoC 답습 변경 0건 확정** 채택 권고
5. **Phase α-2 진입 적격성 5 조건 (C-α2-1 ~ C-α2-5) 5/5 충족** 검증
6. **10/10 풀 3+1 승격 트리거 0건 발화** 검증
7. **TR-1 ~ TR-5 재합의 trigger 0/5 미발화** 검증
8. **R-5 영역 영향 Rollback Trigger 18개 분류** 채택 권고
9. **실 `.importlinter` 수정 진입 아직 아님** 답습 명시

### 0.3 본 합의가 *하지 않는* 것

- ❌ Phase α-2 실 진입 (`.importlinter` 본문 변경 0건)
- ❌ `.importlinter` 본문 (35줄) 어느 줄도 변경 0건
- ❌ `requirements-dev.txt` 본문 변경 0건 (TR-2 답습 — 미발화)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 0건 (TR-1 답습 — 미발화)
- ❌ R-4 도구 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경 0건
- ❌ R-7 docker secret block 본문 변경 0건
- ❌ R-1 CI workflow 신설 / 본문 변경 0건
- ❌ Phase α-1 / α-3 / α-4 자동 진입 0건
- ❌ Phase β / γ 자동 진입 0건
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` / `.git/hooks/*` 본문 변경 0건 — TR-5 미발화)
- ❌ Backlog #6 우선 진입 합의 §6.1 1순위 *해소* (의존성 정리 한정)
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *해소* 0건
- ❌ Group A 2차 C-1 ~ C-10 *해소* 0건
- ❌ TR-1 ~ TR-5 자동 발화 0건
- ❌ 사용자 명시 7 금지 영역 어느 것의 *해소* (분리 매트릭스 한정)
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ Group α 합의 본문 변경 / 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / §5.5.2 본문 변경 / 9 sub-수단 *재결정* (T-6 = T-2 + T-5 병행 답습 한정)
- ❌ 4 forbidden_modules (`openai` / `anthropic` / `litellm` / `ollama`) 변경 / 추가 / 삭제
- ❌ `ignore_imports = src.adapters.llm.facade -> *` 변경
- ❌ `include_external_packages = True` 변경 (C-9 RA-9 PASS 답습 — TR-3 미발화)
- ❌ `root_packages = src` 변경 (옵션 A 답습)
- ❌ `google.generativeai` 본 룰 흡수 시도 (각주 1 답습 — 1차 AST scanner 단독 책무 보존)
- ❌ URL/endpoint 차단 룰 본 룰 흡수 (T-5 영역 = `provider_url_scanner.py` 답습)
- ❌ 의미적 lock-in / 동적 import 본 룰 흡수 (MVP-3 / R-4 영역 답습)
- ❌ 책무 분담 매트릭스 임의 변경 (T-2 + T-5 분담 답습 — TR-4 미발화)
- ❌ fixture 본문 변경 (PASS + 5 FAIL + transitive_import.py 답습)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ threshold *고정* (FP / FN / latency 모두 *후보 한정* 유지)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출 (Group α C-11 답습 — 응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)

### 0.4 본 합의 후속 commit chain

| Commit | 영역 | 권위 |
|--------|------|----|
| Commit 1 (`608a046`) | brief 신설 (`docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md`, 710줄) | brief 본문 채택 |
| **Commit 2** | **본 합의 보고서 신설 (`docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md`)** | **Reviewer-only 단축 합의 — APPROVE AS BRIEF** |
| Commit 3 | 메타 갱신 (CONTEXT.md / INDEX.md / SESSION_2026-05-14.md) | 메타 답습 |

---

## 1. Phase α-2 R-5 `.importlinter` 본문 영역 정의 채택 (Brief §2 답습)

### 1.1 R-5 = `.importlinter` 본문 정의 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5.2 + Group A 2차 합의 답습)

| 영역 | 답습 출처 | 현 상태 (2026-05-15 기준) | 본 합의 채택 |
|------|---------|----------------------|----------|
| 파일 | `/.importlinter` | 35줄 (config 본문 + 답습 주석) | ✅ 답습 변경 0건 |
| 도구 | `import-linter==2.11` + `grimp 3.14` | `requirements-dev.txt` 등재 — TR-2 답습 | ✅ 답습 변경 0건 |
| 책무 (T-2 영역) | Layer 1b — Transitive import (정적 그래프) 차단 | Group A 2차 합의 §1 (T-2 채택) 답습 | ✅ 답습 채택 권고 |
| 책무 분담 (T-6 = T-2 + T-5 병행) | T-2 import-linter (transitive 강점) + T-5 custom AST scanner (1차/3차) | Layer B §5.5.2 답습 | ✅ 답습 채택 권고 |

### 1.2 `.importlinter` 본문 7 항목 답습 채택 (실 본문 변경 0건 — enumerate 한정)

| # | 항목 | 현 본문 값 | 답습 출처 | 본 합의 변경 |
|---|----|---------|---------|---------|
| 1 | `root_packages` | `src` (옵션 A 답습) | Group A 2차 합의 §1.2 답습 — `src/` 만 (future-proof) | 0건 |
| 2 | `include_external_packages` | `True` | C-9 RA-9 사전 검증 PASS (2026-05-10) | 0건 |
| 3 | contract `name` | `No direct LLM SDK imports outside facade` | Group A 2차 합의 §3.1 답습 | 0건 |
| 4 | contract `type` | `forbidden` | Group A 2차 합의 §3.1 답습 | 0건 |
| 5 | `source_modules` | `src` | 옵션 A 답습 | 0건 |
| 6 | `forbidden_modules` | `openai` / `anthropic` / `litellm` / `ollama` (4종) | Group A 2차 합의 §3.1 + 각주 1 답습 (google.generativeai 제외 — 1차 AST scanner 단독) | 0건 |
| 7 | `ignore_imports` | `src.adapters.llm.facade -> *` | Group A 2차 합의 §2.1 + §4.1 답습 — facade single allow | 0건 |

**합산**: 7/7 항목 답습 변경 0건 *확정 채택*.

### 1.3 R-5 = Layer B §5.5.2 T-6 = T-2 + T-5 병행 답습 채택

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-5 관계 | 본 합의 채택 |
|----------|------|----------------------|----------|----------|
| T-2 | import-linter (transitive 정적 그래프 차단) | Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄) APPROVE WITH CONDITIONS | **R-5 본문 = T-2 본문** | ✅ 답습 한정 |
| T-5 | custom AST scanner (동적/모델명/URL) | Group A 1차 + 3차 답습 | R-4 영역 (Phase α-1) — 본 합의 영역 외 | ✅ 영역 분리 답습 |
| T-6 | T-2 + T-5 병행 (Layer 1 정적 차단) | Layer B §5.5.2 답습 | T-2 R-5 + T-5 R-4 분리 진입 | ✅ 분리 진입 채택 |

**범위 한계**: T-5 (R-4 영역) = Phase α-1 합의 (`1b3090b`) 영역 — 본 합의 영역 외 (책무 분리 답습).

### 1.4 책무 분담 매트릭스 답습 채택 (Group A 2차 합의 §5.5 + 각주 1 답습)

| 검증 항목 | T-5 (R-4 AST scanner) | T-2 (R-5 import-linter) | 본 합의 채택 |
|----------|--------------------|---------------------|----------|
| Direct (`openai`/`anthropic`/`litellm`/`ollama`) | ✅ | ✅ (중첩 강화) | ✅ 답습 한정 |
| Direct (`google.generativeai`) | ✅ (단독) | ❌ (도구 제약 — 각주 1 답습) | ✅ 답습 한정 (TR-4 미발화) |
| From-import | ✅ | ✅ (중첩 강화) | ✅ 답습 한정 |
| **Transitive (A→B→forbidden)** | ❌ | **✅ (T-2 신규 가치)** | ✅ 답습 한정 |
| 동적 import (`importlib`, `__import__`) | ✅ (전담) | ❌ | ✅ 답습 한정 |
| 모델명 분기 (문자열) | ✅ (전담) | ❌ | ✅ 답습 한정 |
| URL/endpoint 하드코딩 | ❌ | ❌ (R-4 `provider_url_scanner.py` 영역) | ✅ 영역 분리 답습 |
| 의미적 lock-in | ❌ | ❌ (MVP-3 라운드트립 영역) | ✅ 영역 분리 답습 |

본 합의 = **책무 분담 매트릭스 답습 한정** — 변경 0건 + TR-4 발화 0건.

---

## 2. `.importlinter` PoC 답습 변경 0건 확정 (Brief §3 답습)

### 2.1 `.importlinter` 본문 답습 검증 채택

| 영역 | PoC 답습 | 현 상태 | 본 합의 변경 |
|------|--------|----------|---------|
| `/.importlinter` (35줄) | Group A 2차 합의 §3.1 + 구현 사양 (`g2-gp5-poc2-import-linter-implementation.md`) 답습 | 35줄 (config + 답습 주석) | 0건 |
| 4 forbidden_modules | Group A 2차 합의 §3.1 답습 (`openai`/`anthropic`/`litellm`/`ollama`) | 4 modules 답습 | 0건 |
| facade single allow | Group A 2차 합의 §2.1 + §4.1 답습 (`src.adapters.llm.facade -> *`) | facade allow 답습 | 0건 |
| `include_external_packages = True` | C-9 RA-9 사전 검증 PASS (2026-05-10) 답습 | `True` 답습 (TR-3 미발화) | 0건 |
| 각주 1 (`google.generativeai` 책무 분리) | Group A 2차 합의 각주 1 답습 (1차 AST scanner 단독 책무) | 1차 AST scanner 단독 답습 (TR-4 미발화) | 0건 |
| `root_packages = src` | Group A 2차 합의 §1.2 (옵션 A) 답습 | `src` 답습 | 0건 |

**합산**: `.importlinter` 35줄 × 7 항목 = **PoC 답습 100% 보존** + 본 합의 발효 시점 변경 0건 *확정 채택*.

### 2.2 의존 산출물 답습 검증 채택

| 산출물 | 답습 출처 | 본 합의 변경 |
|--------|--------|---------|
| `requirements-dev.txt` (import-linter 2.11) | Group A 2차 합의 + TR-2 답습 | 0건 |
| `src/adapters/llm/facade.py` (placeholder) | Group A 2차 구현 답습 + TR-1 답습 | 0건 |
| `tests/fixtures/provider_adapter_enforcement/{pass,fail,mvp1_entry}/` | Group A 1차/2차/3차 답습 (PASS 1 + FAIL 6 + transitive_import.py) | 0건 |
| `/.github/workflows/provider-adapter-enforcement.yml` | Group A 2차 구현 답습 (CI-A 옵션) | 0건 (R-1 = Phase α-4 영역) |

**합산**: 4 의존 산출물 답습 변경 0건 *확정 채택*.

### 2.3 R-5 × Phase α-2 sub-step 분할 매트릭스 채택 (Brief §3 답습)

| Stage | 도구 | sub-step | 본 합의 채택 |
|-------|------|---------|----------|
| Stage 3 (T-2) | `.importlinter` | 9 sub-step (본문 답습 검증 / `root_packages` 답습 / `include_external_packages` 답습 / `forbidden_modules` 답습 / `ignore_imports` 답습 / 양방향 시나리오 답습 / CI integration 답습 / ledger entry 후보 / Evidence Artifact 형식) | ✅ 답습 enumerate 한정 — 실 sub-step 결정 = Phase α-2 실 진입 시점 |

---

## 3. 5/5 진입 적격성 5 조건 충족 검증 (Brief §5.1 답습)

### 3.1 적격성 검토 매트릭스 채택

| 조건 # | 조건 | 본 합의 검증 결과 | 판정 |
|------|------|--------------|----|
| **C-α2-1** | **사용자 명시 7 금지 영역 충돌 0** | R-5 `.importlinter` = config 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0). 금지 #1 (실 `.importlinter` 수정) / #2 (CI workflow 변경) = Phase α-2 *실 진입* 시점 적용 — 본 합의 = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α2-2** | **PoC 답습 변경 0** | `.importlinter` 35줄 × 7 항목 + 4 forbidden_modules + facade single allow + `include_external_packages = True` (C-9 PASS) + 각주 1 (google.generativeai 1차 AST 단독) + 책무 분담 매트릭스 답습 + Group A 2차 합의 §1~§9 본문 변경 0건 | ✅ **답습 100% 보존** |
| **C-α2-3** | **의존성 0 (Phase α-1 / α-3 병렬 진입 적격)** | Phase α-2 R-5 ↔ Phase α-1 R-4 = 책무 분담 분리 (T-2 transitive vs T-5 direct/dynamic/model/URL — 의존 0) + Phase α-2 ↔ Phase α-3 R-7 docker secret block = 직교 (config vs deployment) + R-1 / R-6 = Phase α-4 / β 영역 (본 합의 영역 외). C-9 RA-9 사전 검증 *완료* (2026-05-10) — 의존성 해소됨. | ✅ **의존성 0 (병렬 진입 적격)** |
| **C-α2-4** | **Provider Liquidity 5-way 100% 보존** | `.importlinter` = enforcement layer Layer 1b — catalog / provider 영역과 직교 + 4 forbidden_modules 답습 한정 + facade single allow 답습 + 5-vendor 차단 패턴 (각주 1 google.generativeai 1차 AST 단독 분리 포함) 답습 변경 0건 | ✅ **5/5 100% 보존** |
| **C-α2-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-5 = config 영역, Hermes PMO 영역 분리) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-5 = 수단, 목적 = transitive provider lock-in 회피) / T1/T2/T3 분리 보존 (R-5 = T2 영역) / SPOF 의도적 수용 보존 (R-5 = enforcement single point 답습) | ✅ **5/5 보존** |

**합산**: **5/5 충족** *확정 채택* — Phase α-2 진입 적격성 검증 완료 + 실 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. 10/10 풀 3+1 승격 트리거 0건 발화 검증 (Brief §5.2 답습)

| # | 트리거 | 본 합의 발화 |
|---|----|----------|
| 1 | Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Group A 2차 C-1 ~ C-10 어느 것의 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 2 | 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 합의 = 분리 매트릭스 한정 |
| 3 | Layer B §5.5.2 T-6 (T-2 + T-5 병행) *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — enforcement layer = catalog / provider 영역과 직교 |
| 5 | 5 영구 핵심 제약 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 | ❌ 0건 — R-5 = T2 영역 (T3 분리 명시 한정) |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | 4 forbidden_modules / facade ignore / `include_external_packages` / `root_packages` 어느 것의 변경 권고 | ❌ 0건 — `.importlinter` 본문 답습 한정 |
| 9 | TR-1 ~ TR-5 어느 trigger 도 *발화* | ❌ 0건 — facade real / pyproject 신설 / include_external 동작 불가 / 책무 임의 흡수 / T-9 도입 모두 미발화 |
| 10 | `google.generativeai` 본 룰 흡수 시도 / 각주 1 책무 분리 변경 권고 | ❌ 0건 — 각주 1 답습 한정 (1차 AST scanner 단독 책무 명시 보존) |

**검증 결과**: **10/10 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정** ✅

---

## 5. TR-1 ~ TR-5 재합의 trigger 0/5 미발화 검증 (Brief §6.2 답습)

| Trigger | 발화 조건 | 본 합의 발화 |
|--------|---------|---------|
| **TR-1** | `src/adapters/llm/facade.py` real 본문 (LiteLLM 실 import) 작성 | ❌ 미발화 — 현 facade.py = placeholder (Group A 2차 구현 시점 답습) — Backlog #4 P1 v2 facade MVP 합의 영역 분리 |
| **TR-2** | `pyproject.toml` 신설 (T-2 dev-dep 등록 시점 변경) | ❌ 미발화 — `requirements-dev.txt` 답습 유지 |
| **TR-3** | C-9 RA-9 사전 검증 (`include_external_packages = True`) *동작 불가* 판명 | ❌ 미발화 — C-9 PASS (2026-05-10, import-linter 2.11 / grimp 3.14 정상 동작 검증 완료) |
| **TR-4** | depcruise 본질적 한계 3종 (URL/의미적 lock-in/동적 import) 中 1건이라도 *본 PoC 영역으로 흡수* 시도 + `google.generativeai` 상위 패키지 차단 룰 도입 | ❌ 미발화 — 각주 1 답습 (책무 분담의 명시적 갱신만, 풀 재합의 미발화) + 본 합의 = 책무 매트릭스 답습 한정 |
| **TR-5** | T-9 (pre-commit hook PC-1) 도입 별도 합의 진행 시 | ❌ 미발화 — `.pre-commit-config.yaml` 신설 = R-6 영역 (Phase β-1) — 사용자 명시 7 금지 #5 답습 |

**검증 결과**: **TR-1 ~ TR-5 5/5 미발화** → **Group A 2차 합의 발효 본문 *재결정 발화 0건*** 확정 ✅

---

## 6. R-5 영역 영향 Rollback Trigger 18개 분류 채택 (Brief §6.1 답습)

### 6.1 R-5 본문 영역 *직접* 영향 trigger (3개) — 의존성 enumerate 한정

| Trigger | 발화 조건 | R-5 영향 | 본 합의 채택 |
|--------|---------|-----------|----------|
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | `.importlinter` 본문 영향 (forbidden_modules 차단 결과) | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) | `.importlinter` 본문 영향 (T-2 결과) + R-4 영향 (T-5 결과) | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | `.importlinter` 본문 *직접* 영향 | ✅ 답습 한정 (발화 0건) |

### 6.2 R-5 영역 *간접* 영향 trigger (3개) — Phase α-1/α-4/Backlog #4 영역 의존

| Trigger | 영역 의존 | 본 합의 채택 |
|--------|---------|----------|
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) — `.importlinter` 실행 성능 *간접* 영향 (T-6 합산 latency) | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 (`.importlinter` 본문 + R-1 영역 영향) | ✅ 답습 한정 (R-1 = Phase α-4 영역) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 (`.importlinter` `ignore_imports` 영향 — TR-1 답습) | ✅ 영역 외 답습 (Backlog #4) |

### 6.3 R-5 영역 *영향 0* trigger (12개) — Phase α-1/α-3/T3/MVP-3/MVP-6/Backlog 분리

| Trigger | 분리 사유 | 본 합의 채택 |
|--------|--------|----------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G3-2 | S-2 gitleaks (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-3 | ST-3 Docker secret (R-7 = Phase α-3) | ✅ 영역 외 답습 |
| R-MVP1-G3-5 | AR-1 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 (Backlog #3) | ✅ 영역 외 답습 |
| R-MVP1-G3-7 | Tier-2 확장 (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-8 | Operational Readiness parity (Layer E, 금지 #6) | ✅ 영역 외 답습 |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G5-5 | PC-3 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G5-8 | branch protection (T3, 금지 #3) | ✅ 영역 외 답습 |
| R-MVP1-G5-9 | 의미적 lock-in (MVP-3) | ✅ 영역 외 답습 |
| R-MVP1-G5-10 | Layer 2 runtime (MVP-3/4) | ✅ 영역 외 답습 |

### 6.4 합산 채택

| 분류 | trigger 수 | 본 합의 채택 |
|------|---------|----------|
| R-5 직접 영향 | 3 | ✅ 의존성 enumerate 한정 (발화 0건) |
| R-5 간접 영향 (Phase α-1/α-4/Backlog #4 의존) | 3 | ✅ 영역 외 답습 |
| R-5 영향 0 (Phase α-1/α-3/T3/MVP-3/MVP-6/Backlog 분리) | 12 | ✅ 영역 외 답습 |
| **합산** | **18 trigger** | ✅ **본문 확정 답습 + 발화 0건** |
| **추가: Group A 2차 TR-1 ~ TR-5** | **5** | ✅ **5/5 미발화 확정** (§5 답습) |

---

## 7. 실 `.importlinter` 수정 진입 아직 아님 (답습 명시)

### 7.1 본 합의 발효 후 영역 *내* vs *외*

| 영역 | 본 합의 발효 후 *영역 내* | 본 합의 발효 후 *영역 외* (별도 합의 / 사용자 명시 결정) |
|------|-------------------|-----------------------|
| Brief 본문 채택 권고 | ✅ APPROVE AS BRIEF | — |
| `.importlinter` 35줄 본문 정의 채택 | ✅ APPROVE AS BRIEF | — |
| 7 본문 항목 답습 채택 (`root_packages` / `include_external_packages` / contract `name` `type` / `source_modules` / `forbidden_modules` 4종 / `ignore_imports`) | ✅ APPROVE AS BRIEF | — |
| 책무 분담 매트릭스 답습 채택 (T-2 + T-5 분담 + 각주 1) | ✅ APPROVE AS BRIEF | — |
| 적격성 5/5 충족 검증 | ✅ APPROVE AS BRIEF | — |
| 10/10 풀 3+1 트리거 0건 발화 검증 | ✅ APPROVE AS BRIEF | — |
| TR-1 ~ TR-5 5/5 미발화 검증 | ✅ APPROVE AS BRIEF | — |
| 18 Rollback Trigger 분류 채택 | ✅ APPROVE AS BRIEF | — |
| Phase α-2 실 진입 | ❌ | Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| `.importlinter` 본문 변경 | ❌ | 동상 |
| `requirements-dev.txt` 본문 변경 | ❌ | 동상 (TR-2 답습) |
| `src/adapters/llm/facade.py` real 본문 작성 | ❌ | Backlog #4 P1 v2 facade MVP 합의 영역 (TR-1 답습) |
| R-4 도구 본문 변경 | ❌ | Phase α-1 영역 (`1b3090b` 합의 답습) |
| R-7 docker secret block 작성 | ❌ | Phase α-3 영역 |
| R-1 CI workflow 신설 / 본문 변경 | ❌ | Phase α-4 영역 |
| R-6 / R-10 / R-2 / branch protection | ❌ | Phase β 영역 (5 금지 #1 #2 #3 해소 의존) |
| commit signing / Vault HSM / Layer E / Layer F | ❌ | Phase γ 영역 (MVP-6) |
| 7 금지 영역 해소 | ❌ | 별도 합의 + 사용자 명시 결정 영역 |
| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| Layer D MVP-1 PASS 선언 | ❌ | Layer C 발효 후 별도 합의 |
| Layer E Operational Readiness PASS | ❌ | MVP-6 영역 |
| Layer F Hermes PMO 격상 | ❌ | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| TR-1 ~ TR-5 발화 시 영역 | ❌ | Group A 2차 합의 §8 답습 (자동 풀 3+1 재합의) |

### 7.2 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

1. Phase α-3 R-7 docker secret block 진입 brief
2. Phase α-1 ~ α-3 병렬 실제 구현 계획 brief
3. Phase α-2 실 진입 step 분할 brief (실 `.importlinter` 수정 계획)
4. Phase α-4 R-1 CI workflow 통합 brief
5. Phase α-1 R-4 실 진입 step 분할 brief
6. Group α 조건 재평가 (C-1 ~ C-12 영역)
7. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief
8. token rotation 정책 별도 합의 진입 brief (Group α C-3 답습)
9. GitHub plan / ruleset 가용성 확인 단계 진입 (Group α C-4 답습)
10. 세션 종료

---

## 8. 최종 판정 + Conditions

### 8.1 종합 판정

| 영역 | 판정 |
|------|----|
| **종합 판정** | **APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격) |
| 합의 단위 | brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| 합의 형태 | (가) Reviewer-only 단축 합의 (10/10 풀 3+1 트리거 0건 발화 + TR-1 ~ TR-5 5/5 미발화) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) |

### 8.2 본 합의 조건 (Conditions, 답습 한정)

| # | 조건 | 출처 |
|---|------|----|
| C-γ-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | 본 합의 §3 답습 |
| C-γ-2 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) *변경 0건* | 본 합의 §3 답습 |
| C-γ-3 | Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *변경 0건* | 본 합의 §3 답습 |
| C-γ-4 | Group A 2차 합의 C-1 ~ C-10 *변경 0건* | 본 합의 §1 답습 |
| C-γ-5 | TR-1 ~ TR-5 *발화 0건* — 5/5 미발화 확정 | 본 합의 §5 답습 |
| C-γ-6 | 사용자 명시 7 금지 영역 (실 `.importlinter` 수정 / CI workflow 변경 / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) *해소 0건* | 본 합의 §0.1 답습 |
| C-γ-7 | Phase α-2 실 진입 = **Backlog #6 + 사용자 명시 결정 영역** (자동 진입 0건) | 본 합의 §7.1 답습 |
| C-γ-8 | `.importlinter` 본문 (35줄 × 7 항목) 어느 줄도 *변경 0건* | 본 합의 §2.1 답습 |
| C-γ-9 | 4 forbidden_modules (`openai` / `anthropic` / `litellm` / `ollama`) *변경 / 추가 / 삭제 0건* | 본 합의 §1.2 답습 |
| C-γ-10 | `ignore_imports = src.adapters.llm.facade -> *` *변경 0건* | 본 합의 §1.2 답습 |
| C-γ-11 | `include_external_packages = True` *변경 0건* (C-9 RA-9 PASS 답습 — TR-3 미발화) | 본 합의 §1.2 + §5 답습 |
| C-γ-12 | `root_packages = src` (옵션 A) *변경 0건* | 본 합의 §1.2 답습 |
| C-γ-13 | `google.generativeai` 본 룰 흡수 시도 *0건* — 각주 1 답습 (1차 AST scanner 단독 책무 보존) | 본 합의 §1.4 답습 |
| C-γ-14 | 책무 분담 매트릭스 (T-2 + T-5 분담) *변경 0건* — TR-4 미발화 | 본 합의 §1.4 + §5 답습 |
| C-γ-15 | `requirements-dev.txt` *변경 0건* (TR-2 답습) | 본 합의 §2.2 답습 |
| C-γ-16 | `src/adapters/llm/facade.py` real 본문 *작성 0건* (TR-1 답습) | 본 합의 §2.2 답습 |
| C-γ-17 | R-4 도구 본문 / R-7 docker secret / R-1 CI workflow 어느 영역도 *변경 0건* | 본 합의 §7.1 답습 |
| C-γ-18 | Layer A / Layer B / §5.5.2 9 sub-수단 본문 채택 (T-6 = T-2 + T-5 병행) *변경 0건* | 본 합의 §1.3 답습 |
| C-γ-19 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §7 답습 |
| C-γ-20 | Phase α-1 / α-3 / α-4 / β / γ *자동 진입 0건* | 본 합의 §7.1 답습 |
| C-γ-21 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | 본 합의 §0.3 답습 |
| C-γ-22 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* (Group α C-3 + C-4 답습) | 본 합의 §0.3 답습 |
| C-γ-23 | 외부 LLM *응답 결론 강제 채택 0건* (응답 = 입력 한정 — Group α C-11 답습) | 본 합의 §8.1 답습 |
| C-γ-24 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | 본 합의 §3 답습 |
| C-γ-25 | Provider Liquidity 5-way **100% 보존** (enforcement layer Layer 1b = catalog / provider 영역과 직교) | 본 합의 §3 답습 |
| C-γ-26 | 본 합의 = **수단 결정 적격성 권위 권고 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | 본 합의 §7 답습 |

**합산**: **26 조건 (C-γ-1 ~ C-γ-26) 충족 시 = 본 합의 진입 적합** + 본 합의 = "수단 결정 적격성 권위 권고 발행" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 9. 변경 0건 / 진입 0건 검증

### 9.1 본 합의 발효 시점 변경 0건 영역

| 영역 | 변경 |
|------|----|
| `/.importlinter` 본문 (35줄) | 0건 |
| `forbidden_modules` 4종 (`openai` / `anthropic` / `litellm` / `ollama`) | 0건 |
| `ignore_imports` (`src.adapters.llm.facade -> *`) | 0건 |
| `include_external_packages = True` | 0건 |
| `root_packages = src` | 0건 |
| 각주 1 (`google.generativeai` 1차 AST scanner 단독 책무) | 0건 |
| 책무 분담 매트릭스 (T-2 + T-5 분담) | 0건 |
| `requirements-dev.txt` (import-linter 2.11) | 0건 |
| `src/adapters/llm/facade.py` (placeholder) | 0건 |
| `tests/fixtures/provider_adapter_enforcement/{pass,fail,mvp1_entry}/` | 0건 |
| `/.github/workflows/provider-adapter-enforcement.yml` | 0건 |
| R-4 도구 (`secret_scanner.py` 368 / `provider_import_scanner.py` 178 / `provider_url_scanner.py` 283) | 0건 |
| R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog | 0건 |
| Phase α-1 합의 (`1b3090b`) 본문 | 0건 |
| Backlog #6 우선 진입 합의 (`c7ddfdd`) 본문 | 0건 |
| Group α 합의 (`4880e88`) 본문 | 0건 |
| Group A 2차 합의 본문 (`a6e82f1` + 후속) | 0건 |
| Layer A (`f1e0b23`) 본문 | 0건 |
| Layer B (`f40423f`) 본문 | 0건 |
| Layer D (`210c98f`) 본문 | 0건 |
| `implementation-runtime-roadmap-mvp1.md` §5.5.2 T-6 본문 채택 | 0건 |
| `g2-gp5-poc2-import-linter-implementation.md` 본문 | 0건 |
| `g2-gp5-poc2-depcruise-rule-scope.md` 본문 | 0건 |
| ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 | 0건 (cross-reference 답습 한정) |
| `.pre-commit-config.yaml` 본문 | 0건 |
| Production `docker-compose.yml` | 0건 |
| Hermes upstream Dockerfile | 0건 |
| `requirements*.txt` (dev 외) | 0건 |
| GitHub branch protection rule (Web UI / settings) | 0건 |
| GitHub Actions secrets / permissions | 0건 |

### 9.2 본 합의 발효 시점 진입 0건 영역

| 영역 | 진입 |
|------|----|
| Phase α-2 실 진입 (`.importlinter` 본문 변경) | 0건 |
| Phase α-1 / α-3 / α-4 자동 진입 | 0건 |
| Phase β / γ 자동 진입 | 0건 |
| Backlog #6 실 진입 | 0건 |
| TR-1 ~ TR-5 발화 (facade real / pyproject 신설 / include_external 동작 불가 / 책무 임의 흡수 / T-9 도입) | 0건 |
| 7 금지 영역 해소 | 0건 |
| Layer C 발효 (Implementation Evidence PASS) | 0건 |
| Layer D 발효 (MVP-1 PASS) | 0건 |
| Layer E 발효 (Operational Readiness PASS) | 0건 |
| Layer F 발효 (Hermes PMO 격상) | 0건 |
| Group I / Group β / γ-1 / γ-2 | 0건 |
| Backlog #1 / #2 / #4 / #5 / #7 | 0건 |
| MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 17 항목 우선순위 자동 *재고정* | 0건 |
| 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| event enum 정식 등록 | 0건 |
| 외부 LLM 자동 호출 | 0건 |
| 외부 LLM 응답 결론 강제 채택 | 0건 |
| 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 인간 리뷰 의무 자동 발화 | 0건 |
| token rotation 정책 자동 결정 | 0건 |
| GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| commit signing 도입 | 0건 |
| `pull_request_target` workflow 도입 | 0건 |
| Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| threshold *고정* | 0건 (모두 *후보 한정* 유지) |
| MVP-1 PASS 재선언 | 0건 |
| GP-3 / GP-5 PASS 발효 | 0건 |
| ADR 본문 자동 갱신 | 0건 |
| Layer 2 runtime block (G5-5) 진입 | 0건 |

---

## 10. 본 합의 요약 (한 단락)

본 합의는 **`docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md` (DRAFT, commit `608a046`, 710줄) 의 Reviewer-only 단축 합의 보고서** 다. 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 `.importlinter` 수정은 아직 하지 않음.") 답습. **판정 = APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격 — **10/10 풀 3+1 트리거 0건 발화** 확인 + **TR-1 ~ TR-5 5/5 미발화** 확인). 본 합의 = **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-2 답습** + **R-5 = `.importlinter` 본문 정의 채택 권고** (현 35줄 × 7 항목 답습: `root_packages = src` 옵션 A / `include_external_packages = True` C-9 RA-9 PASS / contract `forbidden` type / `source_modules = src` / `forbidden_modules` 4종 `openai`+`anthropic`+`litellm`+`ollama` / `ignore_imports = src.adapters.llm.facade -> *` / 각주 1 google.generativeai 1차 AST 단독 책무 분리 — 본문 변경 0건) + **T-6 = T-2 + T-5 병행 답습 채택** (T-2 R-5 = 본 합의 / T-5 R-4 = Phase α-1 분리) + **책무 분담 매트릭스 답습 채택** (Direct/From 양 도구 중첩 + Transitive T-2 단독 + Dynamic/Model T-5 전담 + URL/의미적 lock-in 영역 외 — TR-4 미발화) + **9 sub-step 분할 매트릭스 채택 권고** + **5/5 진입 적격성 5 조건 (C-α2-1 ~ C-α2-5) 충족 검증** + **10/10 풀 3+1 트리거 0건 발화 검증** + **TR-1 ~ TR-5 5/5 미발화 검증** (facade real / pyproject 신설 / `include_external` 동작 불가 / 책무 임의 흡수 / T-9 도입 모두 미발화) + **18 Rollback Trigger 분류 채택** (R-5 직접 영향 3 + 간접 영향 3 + 영향 0 12) + **26 합의 조건 (C-γ-1 ~ C-γ-26)** 답습. **사용자 명시 7 금지 7/7 답습** (실 `.importlinter` 수정 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **Group α 합의 본문 변경 0건** + **Backlog #6 우선 진입 합의 본문 변경 0건** + **Phase α-1 합의 본문 변경 0건** + **Group A 2차 합의 본문 변경 0건** + **Layer A / Layer B / §5.5.2 본문 변경 0건** + **`.importlinter` 본문 어느 줄도 변경 0건** (35줄 PoC 답습 100% 보존) + **`requirements-dev.txt` / `src/adapters/llm/facade.py` / R-4 도구 / fixture / CI workflow / `.pre-commit-config.yaml` 변경 0건** + **각주 1 책무 분리 변경 0건** + **외부 LLM 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **Phase α-2 실 진입 0건** + **Phase α-1 / α-3 / α-4 / β / γ 자동 진입 0건** + **7 금지 영역 *해소* 0건** + **Layer C / D / E / F 발효 0건** + **Group I / β / γ-1 / γ-2 자동 진입 0건** + **TR-1 ~ TR-5 발화 0/5** + **자동 진입 모두 0건**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건): (1) Phase α-3 R-7 docker secret block 진입 brief / (2) Phase α-1 ~ α-3 병렬 실제 구현 계획 brief / (3) Phase α-2 실 `.importlinter` 수정 step 분할 brief / (4) Phase α-4 R-1 CI workflow 통합 brief / (5) Phase α-1 R-4 실 진입 step 분할 brief / (6) Group α 조건 재평가 / (7) Group I 별도 합의 / (8) token rotation 정책 별도 합의 / (9) GitHub plan 가용성 확인 / (10) 세션 종료.

---

**작성일**: 2026-05-14 후속 12
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
**금지 (사용자 명시 답습 — 본 합의 영역)**:
- ❌ **실 `.importlinter` 수정** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ `.importlinter` 본문 (35줄 × 7 항목) 어느 줄도 변경
- ❌ 4 forbidden_modules / facade ignore / `include_external_packages` / `root_packages` 변경
- ❌ `google.generativeai` 본 룰 흡수 시도 (각주 1 답습)
- ❌ 책무 분담 매트릭스 임의 변경 (TR-4 미발화)
- ❌ `requirements-dev.txt` 본문 변경 (TR-2 미발화)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (TR-1 미발화)
- ❌ R-4 도구 본문 / R-7 docker secret block / R-1 CI workflow 변경
- ❌ Phase α-1 실 진입 자동 진입 금지
- ❌ Phase α-2 실 진입 자동 진입 금지
- ❌ Phase α-3 / α-4 자동 진입 금지
- ❌ Phase β / γ 자동 진입 금지
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 자동 변경
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경
- ❌ Group A 2차 합의 C-1 ~ C-10 자동 변경
- ❌ TR-1 ~ TR-5 자동 발화
- ❌ §5.5.2 T-6 = T-2 + T-5 병행 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출
- ❌ 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
