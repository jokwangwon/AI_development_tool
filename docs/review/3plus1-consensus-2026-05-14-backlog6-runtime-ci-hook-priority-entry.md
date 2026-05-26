# Reviewer-only 단축 합의 보고서 — Backlog #6 Runtime + CI-hook 우선 진입 Brief

> **본 문서는 `docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (DRAFT) 의 Reviewer-only 단축 합의 보고서.** 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 Runtime / CI-hook 구현은 아직 하지 않음.") 답습.
>
> 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** — 실 변경 0건. Backlog #6 실 진입 / Phase α 진입 / Layer C 발효 / MVP-1 PASS / 5 금지 영역 해소 모두 본 합의 영역 외.

**작성일**: 2026-05-14 후속 10
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의)
**검토 대상**: `docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (커밋 후 hash 본 합의 §0.4 참조)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역

---

## 0. 본 합의 범위

### 0.1 사용자 명시 진입 명령 답습

> "옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 Runtime / CI-hook 구현은 아직 하지 않음."

사용자 명시 5 금지 답습 (Group α 합의 + 본 brief §0.3 답습):

1. ❌ branch protection 변경 금지
2. ❌ dev 환경 강제 금지
3. ❌ `pre-commit install` 의무화 금지
4. ❌ Operational Readiness PASS 선언 금지
5. ❌ Hermes PMO 격상 금지

### 0.2 본 합의가 *하는* 것

1. Brief `backlog6-runtime-ci-hook-priority-entry-brief.md` (DRAFT) 의 **수단 결정 적격성 권위 권고** 발행
2. **Group α 합의 C-1 조건 답습** 확인 — Runtime + CI-hook 의존성 *정리 한정* (해소 0건)
3. **Runtime + CI-hook = R-1 ~ R-10 정의** 채택 권고
4. **Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스** 채택 권고
5. **5 금지 영역 × Runtime+CI-hook 분리 매트릭스** 채택 권고
6. **Phase α / β / γ 구분** 채택 권고
7. **Phase α 우선 진입 권고** 답습 (5 금지 충돌 0 영역 한정)
8. **7/7 풀 3+1 트리거 0건 발화** 검증
9. **실 구현 진입 아직 아님** 답습 명시

### 0.3 본 합의가 *하지 않는* 것

- ❌ Backlog #6 실 진입 (Phase α / β / γ 어느 것도 진입 0건)
- ❌ 실 runtime code 구현 (`tools/*.py` / `src/*` 본문 작성 0건)
- ❌ 실 CI workflow 구현 (`.github/workflows/*.yml` 신설 / 본문 변경 0건)
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` / `.importlinter` / `.git/hooks/*` 본문 변경 0건)
- ❌ Group α 합의 C-1 *해소* (의존성 *정리 한정*)
- ❌ 사용자 명시 5 금지 영역 어느 것의 *해소* (분리 매트릭스 한정)
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ Group α 합의 본문 변경 / 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / §5.5 본문 변경 / 9 sub-수단 *재결정*
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정 (Group α C-3 답습)
- ❌ GitHub plan / ruleset 가용성 자동 확인 (Group α C-4 답습)
- ❌ commit signing 도입 (MVP-6 영역)
- ❌ `pull_request_target` workflow 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold *고정* (`dev_env_install_rate ≥ 90%` 포함 모두 *후보 한정* 유지)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출 (Group α C-11 답습 — 응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화

### 0.4 본 합의 후속 commit chain

| Commit | 영역 | 권위 |
|--------|------|----|
| Commit 1 | brief 신설 (`docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md`) | brief 본문 채택 |
| **Commit 2** | **본 합의 보고서 신설 (`docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md`)** | **Reviewer-only 단축 합의 — APPROVE AS BRIEF** |
| Commit 3 | 메타 갱신 (CONTEXT.md / INDEX.md / SESSION_2026-05-14.md) | 메타 답습 |

---

## 1. Group α 합의 C-1 조건 답습

### 1.1 C-1 조건 본문 답습

> **C-1**: Backlog #6 (Runtime + CI-hook) 미진입 시 ***실 강제 적용 시점*** 의존성 명시
> — A + B + C 일치 (3/3 만장일치 — Group α 합의 §4.2 답습)

### 1.2 본 합의의 C-1 답습 한계

| 영역 | 본 합의 답습 |
|------|----------|
| C-1 의존성 *명시* (정리 한정) | ✅ 채택 — brief §3 14 결정 영역 × R-1 ~ R-10 의존성 매트릭스 |
| C-1 *해소* (실 강제 적용) | ❌ 본 합의 영역 외 — Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| Group α 합의 발효 자체 | ✅ 답습 (`4880e88` APPROVE WITH CONDITIONS 3/3 만장일치) — 변경 0건 |
| C-2 ~ C-12 답습 | ✅ 답습 — 자동 진입 0건 + 자동 해소 0건 |

**합산**: 본 합의 = Group α C-1 조건 *답습 한정* — 의존성 *정리 권위 권고 발행* + 실 *해소 0건*.

---

## 2. Runtime + CI-hook = R-1 ~ R-10 정의 (Brief §2 채택 권고)

| 영역 | 정의 | 본 합의 채택 |
|------|----|----------|
| R-1 | CI workflow 영역 (`.github/workflows/*.yml`) | ✅ 채택 권고 |
| R-2 | CI step `pre-commit run --all-files` | ✅ 채택 권고 |
| R-3 | CI step `pre-commit run --files <changed>` (로컬 영역 분리) | ✅ 채택 권고 |
| R-4 | 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) | ✅ 채택 권고 |
| R-5 | `.importlinter` 본문 (TR-1~TR-5 답습) | ✅ 채택 권고 |
| R-6 | `.pre-commit-config.yaml` 본문 | ✅ 채택 권고 (사용자 명시 5 금지 #3 답습) |
| R-7 | docker secret block (`docker-compose.yml` 또는 동등) | ✅ 채택 권고 |
| R-8 | Evidence Artifact 생성 (Markdown + JSONL + actual run SUCCESS URL) | ✅ 채택 권고 |
| R-9 | hook 실행 환경 (`pre-commit` framework 4.6.0) | ✅ 채택 권고 |
| R-10 | `tools/doctor.py` 신규 도구 | ✅ 채택 권고 (사용자 명시 5 금지 #2 답습) |

**합산**: **10/10 채택 권고** — Group α 합의 §6.2 + Layer A / Layer B 답습 + 사용자 명시 5 금지 분리 영역 한정.

---

## 3. Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스 (Brief §3 채택 권고)

### 3.1 AR-3 8 결정 영역 × R-1~R-10 의존성

| Group α 결정 # | 영역 | R 영역 의존 | 5 금지 충돌 | 본 합의 채택 |
|------------|------|-----------|---------|----------|
| #1 AR-2 (e) | CODEOWNERS + required check | R-1 | **금지 #1** | ✅ 답습 한정 |
| #2 AR-1 + AR-2 (e) 단계적 승격 | (e)→(g) trigger | R-1 + Rollback | **금지 #1** | ✅ 답습 한정 |
| #3 Hermes auto-reject (β) | Group I 별도 합의 | R-1 (후속 가능성) | 영향 0 (자동 진입 0건) | ✅ 답습 한정 |
| #4 commit signing (Y) MVP-6 | 미진입 | 영향 0 | **금지 #4 #5** | ✅ 답습 한정 |
| #5 fork PR (3) default | `pull_request_target` BLOCK | R-1 | 영향 0 (default 답습) | ✅ 답습 한정 |
| #6 branch protection 6 옵션 | (i)~(vi) 권고 | 영향 0 | **금지 #1** | ✅ 답습 한정 |
| #7 AI agent (b) GitHub App | 최소 권한 + 서명 미적용 | 영향 0 | 영향 0 (현 시점) | ✅ 답습 한정 |
| #8 CODEOWNERS 핵심 경로 + (d) | 10 경로 + plan 확인 | R-1 (후속 가능성) | 영향 0 (확인 영역) | ✅ 답습 한정 |

### 3.2 PC-4 T3 sub 6 결정 영역 × R-1~R-10 의존성

| Group α 결정 # | 영역 | R 영역 의존 | 5 금지 충돌 | 본 합의 채택 |
|------------|------|-----------|---------|----------|
| #9 `pre-commit install` 단계적 | opt-in → doctor → required + STAGE 1~3차 | R-6 + R-9 + R-10 | **금지 #3** | ✅ 답습 한정 |
| #10 `default_install_hook_types` | `pre-commit` + `commit-msg` 중심 + smoke-only `pre-push` | R-6 | **금지 #3** | ✅ 답습 한정 |
| #11 `fail_fast: false` | 로컬 `--files <changed>` + CI `--all-files` | R-2 + R-6 | **금지 #3** | ✅ 답습 한정 |
| #12 `minimum_pre_commit_version` | 4.6.0 명시 | R-6 + R-9 | **금지 #3** | ✅ 답습 한정 |
| #13 로컬 hook 실패 정책 | 빠른 실패 + 복구 명령 | R-6 (또는 doctor) | **금지 #2 #3** | ✅ 답습 한정 |
| #14 `--no-verify` 차단 | branch protection + required CI 결합 | R-1 | **금지 #1** | ✅ 답습 한정 |

### 3.3 합산

| 분류 | 결정 # 합산 | 본 합의 채택 |
|-----|---------|----------|
| 5 금지 충돌 0 영역 (본 brief 영역 *내 의존성 정리 적격*) | #3 / #5 / #7 / #8 = 4건 | ✅ R-1 / R-4 / R-5 / R-7 / R-8 답습 enumerate 한정 |
| 5 금지 충돌 영역 (별도 합의 필요) | #1 / #2 / #4 / #6 / #9 / #10 / #11 / #12 / #13 / #14 = 10건 | ✅ 의존성 *정리 한정* (실 작업 = 별도 합의 영역) |

**합산**: 14/14 결정 영역 답습 + 재결정 0건 + 의존성 매트릭스 *채택 권고*.

---

## 4. 5 금지 영역과의 분리 (Brief §4 채택 권고)

### 4.1 5 금지 분리 매트릭스 — 본 합의 채택

| 금지 영역 | R-1 ~ R-10 *영향 0 영역* | R-1 ~ R-10 *영향 영역* (분리 대상) | 본 합의 채택 |
|---------|------------------|----------------------------|----------|
| #1 branch protection 변경 | R-4 / R-5 / R-7 / R-8 / R-9 (코드 영역 분리) | R-1 (GitHub Web UI / settings / ruleset 영역 분리) | ✅ 채택 |
| #2 dev 환경 강제 | R-1 / R-4 / R-5 / R-7 / R-8 / R-9 | R-10 (`tools/doctor.py` 본문 작성 / dev 강제 = 영역 외) | ✅ 채택 |
| #3 `pre-commit install` 의무화 | R-1 / R-4 / R-5 / R-7 / R-8 | R-2 / R-6 / R-9 (`.pre-commit-config.yaml` 본문 / 실 install = 영역 외) | ✅ 채택 |
| #4 Operational Readiness PASS | R-1 ~ R-10 모두 | (Layer E = 운영 영역 분리 — 코드 영역과 직교) | ✅ 채택 |
| #5 Hermes PMO 격상 | R-1 ~ R-10 모두 | (Layer F = governance 영역 분리 — 코드 영역과 직교) | ✅ 채택 |

**합산**: 5/5 금지 영역 분리 매트릭스 *채택 권고* — 본 brief = 분리 매트릭스 정리 한정 + 해소 0건.

---

## 5. Phase α / β / γ 구분 (Brief §5 채택 권고)

### 5.1 3 Phase 정의 채택

| Phase | 영역 | 5 금지 충돌 | 본 합의 채택 |
|-------|------|----------|----------|
| **Phase α** | R-4 + R-5 + R-7 + R-1 (5 금지 충돌 0 영역) | 0건 | ✅ **우선 진입 권고 채택** |
| Phase β | R-6 + R-10 + R-2 + branch protection (5 금지 #1 #2 #3 해소 의존) | 충돌 3건 | ✅ 별도 합의 영역 분리 채택 |
| Phase γ | commit signing + Vault HSM + Layer E + Layer F (MVP-6 영역) | 충돌 2건 (#4 #5) | ✅ 영역 외 분리 채택 |

### 5.2 Phase α 4 단계 채택

| 단계 | 영역 | 본 합의 채택 |
|-----|------|----------|
| α-1 | R-4 도구 본문 (Stage 1 + Stage 3) | ✅ 채택 — Stage 1 + Stage 3 병렬 진입 적격 (backlog6-implementation-step-brief §3 순서 A 답습) |
| α-2 | R-5 `.importlinter` 본문 (Stage 3) | ✅ 채택 — α-1 R-4 (provider_import_scanner) 와 동시 진입 적격 |
| α-3 | R-7 docker secret block (Stage 2) | ✅ 채택 — α-1 / α-2 와 독립 진입 적격 |
| α-4 | R-1 CI workflow 통합 (Stage 4) | ✅ 채택 — α-1 ~ α-3 완료 후 진입 |

**합산**: Phase α 4 단계 (α-1 ~ α-4) *채택 권고* — 5 금지 충돌 0 영역 + 실 진입 = Backlog #6 + 사용자 명시 결정 영역.

---

## 6. Phase α 우선 진입 권고 (Brief §5.5 채택 권고)

### 6.1 진입 우선순위 채택

| 우선순위 | 영역 | 본 합의 채택 |
|--------|------|----------|
| 1순위 | Phase α-1 + α-2 + α-3 (병렬 진입 적격) | ✅ 채택 권고 |
| 2순위 | Phase α-4 (R-1 CI workflow 통합) | ✅ 채택 권고 |
| 3순위 | Layer C 발효 합의 진입 (Implementation Evidence PASS) | ✅ 별도 합의 영역 답습 |
| 4순위 | Phase β (5 금지 #1~#3 해소 의존) | ✅ 별도 합의 영역 답습 — 본 합의 권고 0건 |
| 5순위 | Phase γ (MVP-6 영역) | ✅ 영역 외 답습 |

### 6.2 권고 한계

- 본 합의 = **Phase α 우선 진입 *권위 권고 발행 한정***
- 실 Phase α 진입 = **Backlog #6 실 진입 + 사용자 명시 결정 영역** (본 합의 영역 외)
- 자동 진입 0건

---

## 7. 7/7 풀 3+1 트리거 0건 발화 검증 (Brief §8.2 답습)

| # | 트리거 | 본 합의 발화 |
|---|----|----------|
| 1 | Group α 합의 C-1 ~ C-12 *재결정* 권고 | ❌ 0건 — 본 합의 = Group α 답습 한정 |
| 2 | 사용자 명시 5 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 합의 = 분리 매트릭스 한정 |
| 3 | Layer B §5.5 9 sub-수단 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — enforcement layer = catalog / provider 영역과 직교 |
| 5 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 (branch protection / Vault HSM / Tier-2/3 catalog 확장 등) | ❌ 0건 — T3 분리 명시 한정 |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |

**검증 결과**: **7/7 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정** ✅

---

## 8. 실 구현 진입 아직 아님 (답습 명시)

### 8.1 본 합의 발효 후 영역 *내* vs *외*

| 영역 | 본 합의 발효 후 *영역 내* | 본 합의 발효 후 *영역 외* (별도 합의) |
|------|-------------------|-----------------------|
| Brief 본문 채택 권고 | ✅ APPROVE AS BRIEF | — |
| 의존성 매트릭스 채택 권고 | ✅ APPROVE AS BRIEF | — |
| Phase α 우선 진입 권고 | ✅ APPROVE AS BRIEF (수단 결정 적격성 권위 권고) | — |
| Phase α 실 진입 | ❌ | Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| R-4 도구 본문 변경 | ❌ | 동상 |
| R-5 `.importlinter` 본문 변경 | ❌ | 동상 |
| R-7 docker secret block 작성 | ❌ | 동상 |
| R-1 CI workflow 신설 / 본문 변경 | ❌ | 동상 |
| 5 금지 영역 해소 | ❌ | 별도 합의 + 사용자 명시 결정 영역 |
| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| Layer D MVP-1 PASS 선언 | ❌ | Layer C 발효 후 별도 합의 |
| Layer E Operational Readiness PASS | ❌ | MVP-6 영역 |
| Layer F Hermes PMO 격상 | ❌ | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |

### 8.2 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

1. Phase α-1 R-4 도구 본문 진입 brief
2. Phase α-2 R-5 `.importlinter` 본문 진입 brief
3. Phase α-3 R-7 docker secret block 진입 brief
4. Phase α-4 R-1 CI workflow 통합 brief
5. Group α 조건 재평가 (C-1 ~ C-12 영역)
6. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief
7. token rotation 정책 별도 합의 진입 brief (Group α C-3 답습)
8. GitHub plan / ruleset 가용성 확인 단계 진입 (Group α C-4 답습)
9. 세션 종료

---

## 9. 최종 판정 + Conditions

### 9.1 종합 판정

| 영역 | 판정 |
|------|----|
| **종합 판정** | **APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격) |
| 합의 단위 | brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| 합의 형태 | (가) Reviewer-only 단축 합의 (7/7 풀 3+1 트리거 0건 발화) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) |

### 9.2 본 합의 조건 (Conditions, 답습 한정)

| # | 조건 | 출처 |
|---|------|----|
| C-α-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | 본 합의 §1 답습 |
| C-α-2 | 5 금지 영역 (branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) *해소 0건* | 본 합의 §4 답습 |
| C-α-3 | Phase α 실 진입 = **Backlog #6 + 사용자 명시 결정 영역** (자동 진입 0건) | 본 합의 §6 답습 |
| C-α-4 | Layer A / Layer B / §5.5 9 sub-수단 본문 채택 *변경 0건* | 본 합의 §2 + §3 답습 |
| C-α-5 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §8 답습 |
| C-α-6 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | 본 합의 §0.3 답습 |
| C-α-7 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* (Group α C-3 + C-4 답습) | 본 합의 §0.3 답습 |
| C-α-8 | 외부 LLM *응답 결론 강제 채택 0건* (응답 = 입력 한정 — Group α C-11 답습) | 본 합의 §9.1 답습 |
| C-α-9 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | 본 합의 §7 답습 |
| C-α-10 | Provider Liquidity 5-way **100% 보존** (enforcement layer = catalog / provider 영역과 직교) | 본 합의 §7 답습 |
| C-α-11 | 본 합의 = **DRAFT 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | 본 합의 §8 답습 |

**합산**: **11 조건 (C-α-1 ~ C-α-11) 충족 시 = 본 합의 진입 적합** + 본 합의 = "수단 결정 적격성 권위 권고 발행" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 10. 변경 0건 / 진입 0건 검증

### 10.1 본 합의 발효 시점 변경 0건 영역

| 영역 | 변경 |
|------|----|
| Group α 합의 (`4880e88`) 본문 | 0건 |
| Layer A (`f1e0b23`) 본문 | 0건 |
| Layer B (`f40423f`) 본문 | 0건 |
| Layer D (`210c98f`) 본문 | 0건 |
| `implementation-runtime-roadmap-mvp1.md` §5.5 9 sub-수단 본문 채택 | 0건 |
| `backlog6-implementation-step-brief.md` 본문 | 0건 |
| Group α brief (`db0e3ac`) 본문 | 0건 |
| ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 | 0건 (cross-reference 답습 한정) |
| 도구 본문 (`tools/*.py`) | 0건 |
| `.importlinter` 본문 | 0건 |
| `.pre-commit-config.yaml` 본문 | 0건 |
| CI workflow (`.github/workflows/*.yml`) | 0건 |
| Production `docker-compose.yml` | 0건 |
| Hermes upstream Dockerfile | 0건 |
| `src/adapters/llm/facade.py` | 0건 |
| `requirements*.txt` | 0건 |
| GitHub branch protection rule (Web UI / settings) | 0건 |
| GitHub Actions secrets / permissions | 0건 |

### 10.2 본 합의 발효 시점 진입 0건 영역

| 영역 | 진입 |
|------|----|
| Backlog #6 실 진입 (Phase α / β / γ) | 0건 |
| 5 금지 영역 (branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 해소 | 0건 |
| Layer C 발효 (Implementation Evidence PASS) | 0건 |
| Layer D 발효 (MVP-1 PASS) | 0건 |
| Layer E 발효 (Operational Readiness PASS) | 0건 |
| Layer F 발효 (Hermes PMO 격상) | 0건 |
| Group I (Hermes-originated commit auto-reject) | 0건 |
| Group β / γ-1 / γ-2 | 0건 |
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
| Implementation Evidence PASS 자동 발효 | 0건 |
| GP-3 / GP-5 PASS 발효 | 0건 |
| ADR 본문 자동 갱신 | 0건 |

---

## 11. 본 합의 요약 (한 단락)

본 합의는 **`docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (DRAFT) 의 Reviewer-only 단축 합의 보고서** 다. 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 Runtime / CI-hook 구현은 아직 하지 않음.") 답습. **판정 = APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격 — **7/7 풀 3+1 트리거 0건 발화** 확인). 본 합의 = **Group α 합의 C-1 조건 답습** + **Runtime + CI-hook = R-1 ~ R-10 정의 채택 권고** + **Group α 14 결정 영역 × Runtime/CI-hook 의존성 매트릭스 채택 권고** (5 금지 충돌 0 영역 4건 + 충돌 영역 10건) + **5 금지 영역 분리 매트릭스 채택 권고** (5/5) + **Phase α / β / γ 구분 채택 권고** + **Phase α 우선 진입 권고** (4 단계 α-1 ~ α-4 + 병렬 진입 권고) + **11 합의 조건 (C-α-1 ~ C-α-11)** 답습. **사용자 명시 5 금지 5/5 답습** (branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **Group α 합의 본문 변경 0건** + **Layer A / Layer B / §5.5 본문 변경 0건** + **14 결정 영역 *재결정* 0건** + **9 sub-수단 본문 채택 변경 0건** + **외부 LLM 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **Backlog #6 실 진입 0건** + **5 금지 영역 *해소* 0건** + **Layer C / D / E / F 발효 0건** + **Group I / β / γ-1 / γ-2 자동 진입 0건** + **자동 진입 모두 0건**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건): (1) Phase α-1 R-4 도구 본문 진입 brief / (2) Phase α-2 R-5 `.importlinter` 본문 진입 brief / (3) Phase α-3 R-7 docker secret block 진입 brief / (4) Phase α-4 R-1 CI workflow 통합 brief / (5) Group α 조건 재평가 / (6) Group I 별도 합의 / (7) token rotation 정책 별도 합의 / (8) GitHub plan 가용성 확인 / (9) 세션 종료.

---

**작성일**: 2026-05-14 후속 10
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
**금지 (사용자 명시 답습 — 본 합의 영역)**:
- ❌ **branch protection 변경** (사용자 명시 5 금지 #1)
- ❌ **dev 환경 강제** (사용자 명시 5 금지 #2)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ Backlog #6 실 구현 자동 진입 금지
- ❌ T3 영역 자동 진입 금지
- ❌ 실 runtime code 구현 / 실 CI workflow 구현 / 실 hook 구현
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
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
