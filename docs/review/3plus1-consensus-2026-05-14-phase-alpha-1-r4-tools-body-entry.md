# Reviewer-only 단축 합의 보고서 — Phase α-1 R-4 도구 본문 진입 Brief

> **본 문서는 `docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md` (DRAFT, commit `e7cdb21`) 의 Reviewer-only 단축 합의 보고서.** 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 R-4 도구 본문 수정은 아직 하지 않음.") 답습.
>
> 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** — 실 변경 0건. Phase α-1 실 진입 / R-4 도구 본문 변경 / Phase α-2 ~ α-4 자동 진입 / Layer C 발효 / MVP-1 PASS / 7 금지 영역 해소 모두 본 합의 영역 외.

**작성일**: 2026-05-14 후속 11
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**검토 대상**: `docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md` (commit `e7cdb21`, 584줄)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- `docs/phase0/backlog6-implementation-step-brief.md` §2.2.1 + §2.2.3 (Stage 1 + Stage 3 sub-step 답습)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역

---

## 0. 본 합의 범위

### 0.1 사용자 명시 진입 명령 답습

> "옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 R-4 도구 본문 수정은 아직 하지 않음."

사용자 명시 7 금지 답습 (Backlog #6 우선 진입 합의 + 본 brief §0.3 답습):

1. ❌ 실 runtime code 구현 금지 — R-4 도구 본문 어느 줄도 변경 0건
2. ❌ CI workflow 변경 금지
3. ❌ branch protection 변경 금지
4. ❌ dev 환경 강제 금지
5. ❌ `pre-commit install` 의무화 금지
6. ❌ Operational Readiness PASS 선언 금지
7. ❌ Hermes PMO 격상 금지

### 0.2 본 합의가 *하는* 것

1. Brief `phase-alpha-1-r4-tools-body-entry-brief.md` (DRAFT, `e7cdb21`) 의 **수단 결정 적격성 권위 권고** 발행
2. **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-1 영역 답습** 확인
3. **Phase α-1 = R-4 도구 본문 영역 정의** 채택 권고 (3 도구)
4. **3 도구 PoC 답습 변경 0건** 확정 채택 권고
5. **Phase α-1 진입 적격성 5 조건 (C-α1-1 ~ C-α1-5) 5/5 충족** 검증
6. **8/8 풀 3+1 승격 트리거 0건 발화** 검증
7. **R-4 영역 영향 Rollback Trigger 18개 분류** 채택 권고
8. **실 도구 본문 수정 진입 아직 아님** 답습 명시

### 0.3 본 합의가 *하지 않는* 것

- ❌ Phase α-1 실 진입 (R-4 도구 본문 변경 0건)
- ❌ R-4 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 어느 줄도 변경 0건
- ❌ Phase α-2 / α-3 / α-4 자동 진입 0건
- ❌ Phase β / γ 자동 진입 0건
- ❌ 실 CI workflow 구현 (`.github/workflows/*.yml` 신설 / 본문 변경 0건)
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` / `.importlinter` / `.git/hooks/*` 본문 변경 0건)
- ❌ Backlog #6 우선 진입 합의 §6.1 1순위 *해소* (의존성 정리 한정)
- ❌ 사용자 명시 7 금지 영역 어느 것의 *해소* (분리 매트릭스 한정)
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ Group α 합의 본문 변경 / 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / §5.5 본문 변경 / 9 sub-수단 *재결정*
- ❌ R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경
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
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)

### 0.4 본 합의 후속 commit chain

| Commit | 영역 | 권위 |
|--------|------|----|
| Commit 1 (`e7cdb21`) | brief 신설 (`docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md`, 584줄) | brief 본문 채택 |
| **Commit 2** | **본 합의 보고서 신설 (`docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md`)** | **Reviewer-only 단축 합의 — APPROVE AS BRIEF** |
| Commit 3 | 메타 갱신 (CONTEXT.md / INDEX.md / SESSION_2026-05-14.md) | 메타 답습 |

---

## 1. Phase α-1 R-4 도구 본문 영역 정의 채택 (Brief §2 답습)

### 1.1 R-4 = 3 도구 정의 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5 답습)

| 도구 | 영역 | 답습 출처 | 현 라인 수 | Stage | 본 합의 채택 |
|------|----|----------|----------|-------|----------|
| `tools/secret_scanner.py` | GP-3 S-1 — 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC | 368 | Stage 1 | ✅ 채택 권고 |
| `tools/provider_import_scanner.py` | GP-5 T-2 — Layer 1 정적 차단 (5-vendor AST 패턴) | Group A 1차 PoC | 178 | Stage 3 | ✅ 채택 권고 |
| `tools/provider_url_scanner.py` | GP-5 T-5 — URL/Model Tier-1 정적 차단 (URL Tier-1 10 + Model Tier-1 19) | Group A 3차 PoC | 283 | Stage 3 | ✅ 채택 권고 |

**합산**: 3/3 도구 = 829줄 PoC 본문 답습 변경 0건 *채택 권고*.

### 1.2 R-4 도구 = Layer B §5.5 9 sub-수단 中 S-1 + T-2 + T-5 (T-6 합산) 답습 채택

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-4 도구 | 본 합의 채택 |
|----------|------|----------------------|----------|----------|
| S-1 | 코드 본문 secret 검출 | Group D PoC 답습 | `secret_scanner.py` | ✅ 답습 한정 |
| T-2 | Layer 1 정적 차단 (custom AST) | Group A 1차 답습 | `provider_import_scanner.py` | ✅ 답습 한정 |
| T-5 | URL/Model 정적 차단 | Group A 3차 답습 | `provider_url_scanner.py` | ✅ 답습 한정 |

**범위 한계**: T-6 (import-linter 병행) = R-5 영역 (Phase α-2) — 본 합의 영역 외.

---

## 2. 기존 PoC 본문 답습 변경 0건 확정 (Brief §3 답습)

### 2.1 3 도구 PoC 답습 검증 채택

| 도구 | PoC 답습 | 현 라인 수 | 본 합의 변경 |
|------|--------|----------|---------|
| `tools/secret_scanner.py` | Group D (`g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md`) 답습 | 368 | 0건 |
| `tools/provider_import_scanner.py` | Group A 1차 (`g2-gp5-provider-adapter-enforcement-poc.md`) 답습 | 178 | 0건 |
| `tools/provider_url_scanner.py` | Group A 3차 (`g2-gp5-poc3-url-endpoint-model-name-scanner.md`) 답습 | 283 | 0건 |

**합산**: 3 도구 × 829줄 = **PoC 답습 100% 보존** + 본 합의 발효 시점 변경 0건 *확정 채택*.

### 2.2 catalog 답습 검증 채택

| catalog | 출처 | 본 합의 변경 |
|---------|------|---------|
| R-4.1 Tier-1 45 patterns | Group D §1.2 #1 답습 | 0건 |
| URL Tier-1 10 | Group A 3차 §4 답습 | 0건 |
| Model Tier-1 19 | Group A 3차 §5 답습 | 0건 |

**합산**: 3 catalog 답습 변경 0건 *확정 채택* — Tier-2 / Tier-3 확장은 Backlog #3 별도 합의 영역 (Group α 합의 5.1 #8 답습).

### 2.3 3 도구 × Phase α-1 sub-step 분할 매트릭스 채택 (Brief §3 답습)

| Stage | 도구 | sub-step | 본 합의 채택 |
|-------|------|---------|----------|
| Stage 1 | `secret_scanner.py` | 4 sub-step (본문 답습 검증 / CI 통합 인터페이스 / ledger entry 후보 / Evidence Artifact 형식) | ✅ 답습 한정 |
| Stage 3 (T-2) | `provider_import_scanner.py` | 3 sub-step (본문 답습 검증 / CLI 인터페이스 / facade exemption 답습) | ✅ 답습 한정 |
| Stage 3 (T-5) | `provider_url_scanner.py` | 4 sub-step (본문 답습 검증 / URL Tier-1 catalog / Model Tier-1 catalog / CLI 인터페이스) | ✅ 답습 한정 |
| **합산** | **3 도구** | **11 sub-step** | ✅ **답습 enumerate 한정 — 실 sub-step 결정 = Phase α-1 실 진입 시점** |

---

## 3. 5/5 진입 적격성 5 조건 충족 검증 (Brief §5.1 답습)

### 3.1 적격성 검토 매트릭스 채택

| 조건 # | 조건 | 본 합의 검증 결과 | 판정 |
|------|------|--------------|----|
| **C-α1-1** | **사용자 명시 7 금지 영역 충돌 0** | R-4 도구 본문 = 코드 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0) | ✅ **0/7 충돌** |
| **C-α1-2** | **PoC 답습 변경 0** | 3 도구 × 829줄 PoC 답습 + 3 catalog (R-4.1 / URL / Model) 답습 변경 0건 | ✅ **답습 100% 보존** |
| **C-α1-3** | **의존성 0 (Stage 1 + Stage 3 병렬 진입 적격)** | Stage 1 (S-1) ↔ Stage 3 (T-2 + T-5) = 양 GP 독립 (의존성 0) + R-5 / R-7 / R-1 = Phase α-2 / α-3 / α-4 영역 (본 합의 영역 외) | ✅ **의존성 0 (병렬 진입 적격)** |
| **C-α1-4** | **Provider Liquidity 5-way 100% 보존** | R-4 도구 = enforcement layer 영역 — catalog / provider 영역과 직교 + 5-vendor 차단 패턴 답습 변경 0건 | ✅ **5/5 100% 보존** |
| **C-α1-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존 답습 | ✅ **5/5 보존** |

**합산**: **5/5 충족** *확정 채택* — Phase α-1 진입 적격성 검증 완료 + 실 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. 8/8 풀 3+1 승격 트리거 0건 발화 검증 (Brief §5.2 답습)

| # | 트리거 | 본 합의 발화 |
|---|----|----------|
| 1 | Group α 합의 C-1 ~ C-12 *재결정* 권고 | ❌ 0건 — 본 합의 = Group α 답습 한정 |
| 2 | 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 합의 = 분리 매트릭스 한정 |
| 3 | Layer B §5.5 9 sub-수단 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — enforcement layer = catalog / provider 영역과 직교 |
| 5 | 5 영구 핵심 제약 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 | ❌ 0건 — R-4 = T2 영역 (T3 분리 명시 한정) |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 catalog 변경 권고 | ❌ 0건 — catalog 답습 한정 |

**검증 결과**: **8/8 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정** ✅

---

## 5. R-4 영역 영향 Rollback Trigger 18개 분류 채택 (Brief §6 답습)

### 5.1 R-4 도구 본문 영역 *직접* 영향 trigger (5개) — 의존성 enumerate 한정

| Trigger | 발화 조건 | R-4 도구 영향 | 본 합의 채택 |
|--------|---------|-----------|----------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | `secret_scanner.py` 본문 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | `secret_scanner.py` 성능 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | `provider_import_scanner.py` 본문 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | `provider_url_scanner.py` 본문 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 불일치) | 양 도구 + R-5 영역 영향 | ✅ 답습 한정 (R-5 = Phase α-2) |

### 5.2 R-4 영역 *간접* 영향 trigger (3개) — Phase α-2/α-3/α-4/β 영역 의존

| Trigger | 영역 의존 | 본 합의 채택 |
|--------|---------|----------|
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 (R-1 영역 = Phase α-4 의존) | ✅ 영역 외 답습 |
| R-MVP1-G5-AR3-STAGE 1차 | required status check 도입 (R-1 영역 = Phase α-4 + 금지 #3 의존) | ✅ 영역 외 답습 |
| R-MVP1-G3-PC4T3-STAGE 1차 | opt-in → doctor warning (R-6 + R-10 영역 = Phase β + 금지 #4 #5 의존) | ✅ 영역 외 답습 |

### 5.3 R-4 영역 *영향 0* trigger (10개) — T3/MVP-3/MVP-6/Backlog 분리

| Trigger | 분리 사유 | 본 합의 채택 |
|--------|--------|----------|
| R-MVP1-G3-2 | S-2 gitleaks (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-3 | ST-3 Docker secret (R-7 = Phase α-3) | ✅ 영역 외 답습 |
| R-MVP1-G3-5 | AR-1 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 (Backlog #3) | ✅ 영역 외 답습 |
| R-MVP1-G3-7 | Tier-2 확장 (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-8 | Operational Readiness parity (Layer E, 금지 #6) | ✅ 영역 외 답습 |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 (R-5 = Phase α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-5 | PC-3 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G5-7 | P1 v2 facade real (Backlog #4) | ✅ 영역 외 답습 |
| R-MVP1-G5-8 | branch protection (T3, 금지 #3) | ✅ 영역 외 답습 |
| R-MVP1-G5-9 | 의미적 lock-in (MVP-3) | ✅ 영역 외 답습 |
| R-MVP1-G5-10 | Layer 2 runtime (MVP-3/4) | ✅ 영역 외 답습 |

### 5.4 합산 채택

| 분류 | trigger 수 | 본 합의 채택 |
|------|---------|----------|
| R-4 직접 영향 | 5 | ✅ 의존성 enumerate 한정 (발화 0건) |
| R-4 간접 영향 (Phase α-2/α-3/α-4/β 의존) | 3 | ✅ 영역 외 답습 |
| R-4 영향 0 (T3/MVP-3/MVP-6/Backlog 분리) | 10 | ✅ 영역 외 답습 |
| **합산** | **18 trigger** | ✅ **본문 확정 답습 + 발화 0건** |

---

## 6. 실 도구 본문 수정 진입 아직 아님 (답습 명시)

### 6.1 본 합의 발효 후 영역 *내* vs *외*

| 영역 | 본 합의 발효 후 *영역 내* | 본 합의 발효 후 *영역 외* (별도 합의 / 사용자 명시 결정) |
|------|-------------------|-----------------------|
| Brief 본문 채택 권고 | ✅ APPROVE AS BRIEF | — |
| 3 도구 정의 채택 | ✅ APPROVE AS BRIEF | — |
| 적격성 5/5 충족 검증 | ✅ APPROVE AS BRIEF | — |
| 8/8 트리거 0건 발화 검증 | ✅ APPROVE AS BRIEF | — |
| 18 Rollback Trigger 분류 채택 | ✅ APPROVE AS BRIEF | — |
| Phase α-1 실 진입 | ❌ | Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| `tools/secret_scanner.py` 본문 변경 | ❌ | 동상 |
| `tools/provider_import_scanner.py` 본문 변경 | ❌ | 동상 |
| `tools/provider_url_scanner.py` 본문 변경 | ❌ | 동상 |
| R-5 `.importlinter` 본문 변경 | ❌ | Phase α-2 영역 |
| R-7 docker secret block 작성 | ❌ | Phase α-3 영역 |
| R-1 CI workflow 신설 / 본문 변경 | ❌ | Phase α-4 영역 |
| R-6 / R-10 / R-2 / branch protection | ❌ | Phase β 영역 (5 금지 #1 #2 #3 해소 의존) |
| commit signing / Vault HSM / Layer E / Layer F | ❌ | Phase γ 영역 (MVP-6) |
| 7 금지 영역 해소 | ❌ | 별도 합의 + 사용자 명시 결정 영역 |
| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| Layer D MVP-1 PASS 선언 | ❌ | Layer C 발효 후 별도 합의 |
| Layer E Operational Readiness PASS | ❌ | MVP-6 영역 |
| Layer F Hermes PMO 격상 | ❌ | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |

### 6.2 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

1. Phase α-1 R-4 실제 도구 본문 수정 계획 brief
2. Phase α-2 R-5 `.importlinter` 본문 진입 brief
3. Phase α-3 R-7 docker secret block 진입 brief
4. Phase α-1 ~ α-3 병렬 진입 계획 brief
5. Phase α-4 R-1 CI workflow 통합 brief
6. Group α 조건 재평가 (C-1 ~ C-12 영역)
7. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief
8. token rotation 정책 별도 합의 진입 brief (Group α C-3 답습)
9. GitHub plan / ruleset 가용성 확인 단계 진입 (Group α C-4 답습)
10. 세션 종료

---

## 7. 최종 판정 + Conditions

### 7.1 종합 판정

| 영역 | 판정 |
|------|----|
| **종합 판정** | **APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격) |
| 합의 단위 | brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| 합의 형태 | (가) Reviewer-only 단축 합의 (8/8 풀 3+1 트리거 0건 발화) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) |

### 7.2 본 합의 조건 (Conditions, 답습 한정)

| # | 조건 | 출처 |
|---|------|----|
| C-β-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | 본 합의 §3 답습 |
| C-β-2 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) *변경 0건* | 본 합의 §3 답습 |
| C-β-3 | 사용자 명시 7 금지 영역 (실 runtime code / CI workflow 변경 / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) *해소 0건* | 본 합의 §0.1 답습 |
| C-β-4 | Phase α-1 실 진입 = **Backlog #6 + 사용자 명시 결정 영역** (자동 진입 0건) | 본 합의 §6.1 답습 |
| C-β-5 | R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 *변경 0건* | 본 합의 §2.1 답습 |
| C-β-6 | R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 catalog *변경 0건* | 본 합의 §2.2 답습 |
| C-β-7 | Layer A / Layer B / §5.5 9 sub-수단 본문 채택 *변경 0건* | 본 합의 §1.2 답습 |
| C-β-8 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §6 답습 |
| C-β-9 | Phase α-2 / α-3 / α-4 / β / γ *자동 진입 0건* | 본 합의 §6.1 답습 |
| C-β-10 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | 본 합의 §0.3 답습 |
| C-β-11 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* (Group α C-3 + C-4 답습) | 본 합의 §0.3 답습 |
| C-β-12 | 외부 LLM *응답 결론 강제 채택 0건* (응답 = 입력 한정 — Group α C-11 답습) | 본 합의 §7.1 답습 |
| C-β-13 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | 본 합의 §3 답습 |
| C-β-14 | Provider Liquidity 5-way **100% 보존** (enforcement layer = catalog / provider 영역과 직교) | 본 합의 §3 답습 |
| C-β-15 | 본 합의 = **수단 결정 적격성 권위 권고 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | 본 합의 §6 답습 |

**합산**: **15 조건 (C-β-1 ~ C-β-15) 충족 시 = 본 합의 진입 적합** + 본 합의 = "수단 결정 적격성 권위 권고 발행" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 8. 변경 0건 / 진입 0건 검증

### 8.1 본 합의 발효 시점 변경 0건 영역

| 영역 | 변경 |
|------|----|
| `tools/secret_scanner.py` 본문 (368줄) | 0건 |
| `tools/provider_import_scanner.py` 본문 (178줄) | 0건 |
| `tools/provider_url_scanner.py` 본문 (283줄) | 0건 |
| R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog | 0건 |
| Backlog #6 우선 진입 합의 (`c7ddfdd`) 본문 | 0건 |
| Group α 합의 (`4880e88`) 본문 | 0건 |
| Layer A (`f1e0b23`) 본문 | 0건 |
| Layer B (`f40423f`) 본문 | 0건 |
| Layer D (`210c98f`) 본문 | 0건 |
| `implementation-runtime-roadmap-mvp1.md` §5.5 9 sub-수단 본문 채택 | 0건 |
| `backlog6-implementation-step-brief.md` 본문 | 0건 |
| `backlog6-runtime-ci-hook-priority-entry-brief.md` 본문 | 0건 |
| ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 | 0건 (cross-reference 답습 한정) |
| `.importlinter` 본문 | 0건 |
| `.pre-commit-config.yaml` 본문 | 0건 |
| CI workflow (`.github/workflows/*.yml`) | 0건 |
| Production `docker-compose.yml` | 0건 |
| Hermes upstream Dockerfile | 0건 |
| `src/adapters/llm/facade.py` | 0건 |
| `requirements*.txt` | 0건 |
| GitHub branch protection rule (Web UI / settings) | 0건 |
| GitHub Actions secrets / permissions | 0건 |

### 8.2 본 합의 발효 시점 진입 0건 영역

| 영역 | 진입 |
|------|----|
| Phase α-1 실 진입 (R-4 도구 본문 변경) | 0건 |
| Phase α-2 / α-3 / α-4 자동 진입 | 0건 |
| Phase β / γ 자동 진입 | 0건 |
| Backlog #6 실 진입 | 0건 |
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

---

## 9. 본 합의 요약 (한 단락)

본 합의는 **`docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md` (DRAFT, commit `e7cdb21`, 584줄) 의 Reviewer-only 단축 합의 보고서** 다. 사용자 명시 진입 명령 ("옵션 A로 진행해주세요. brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실제 R-4 도구 본문 수정은 아직 하지 않음.") 답습. **판정 = APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격 — **8/8 풀 3+1 트리거 0건 발화** 확인). 본 합의 = **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-1 답습** + **R-4 = 3 도구 (`secret_scanner.py` Group D 368줄 + `provider_import_scanner.py` Group A 1차 178줄 + `provider_url_scanner.py` Group A 3차 283줄 — 합산 829줄 PoC 답습 변경 0건) 정의 채택 권고** + **3 catalog (R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19) 변경 0건 확정 채택** + **11 sub-step 분할 매트릭스 채택 권고** (Stage 1 4 + Stage 3 T-2 3 + Stage 3 T-5 4) + **5/5 진입 적격성 5 조건 (C-α1-1 ~ C-α1-5) 충족 검증** + **8/8 풀 3+1 트리거 0건 발화 검증** + **18 Rollback Trigger 분류 채택** (R-4 직접 영향 5 + 간접 영향 3 + 영향 0 10) + **15 합의 조건 (C-β-1 ~ C-β-15)** 답습. **사용자 명시 7 금지 7/7 답습** (실 runtime code 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** + **Group α 합의 본문 변경 0건** + **Backlog #6 우선 진입 합의 본문 변경 0건** + **Layer A / Layer B / §5.5 본문 변경 0건** + **R-4 도구 본문 어느 줄도 변경 0건** (829줄 PoC 답습 100% 보존) + **R-4.1 / URL / Model catalog 변경 0건** + **외부 LLM 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **Phase α-1 실 진입 0건** + **Phase α-2 / α-3 / α-4 / β / γ 자동 진입 0건** + **7 금지 영역 *해소* 0건** + **Layer C / D / E / F 발효 0건** + **Group I / β / γ-1 / γ-2 자동 진입 0건** + **자동 진입 모두 0건**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건): (1) Phase α-1 R-4 실제 도구 본문 수정 계획 brief / (2) Phase α-2 R-5 `.importlinter` 본문 진입 brief / (3) Phase α-3 R-7 docker secret block 진입 brief / (4) Phase α-1 ~ α-3 병렬 진입 계획 brief / (5) Phase α-4 R-1 CI workflow 통합 brief / (6) Group α 조건 재평가 / (7) Group I 별도 합의 / (8) token rotation 정책 별도 합의 / (9) GitHub plan 가용성 확인 / (10) 세션 종료.

---

**작성일**: 2026-05-14 후속 11
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
**금지 (사용자 명시 답습 — 본 합의 영역)**:
- ❌ **실 runtime code 구현** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경
- ❌ Phase α-1 실 진입 자동 진입 금지
- ❌ Phase α-2 / α-3 / α-4 자동 진입 금지
- ❌ Phase β / γ 자동 진입 금지
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 자동 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
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
