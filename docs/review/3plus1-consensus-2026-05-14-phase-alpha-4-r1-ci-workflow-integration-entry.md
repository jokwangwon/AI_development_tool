# Reviewer-only 단축 합의 보고서 — Phase α-4 R-1 CI workflow 통합 진입 Brief

> **본 문서는 `docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (DRAFT, commit `f91ef4b`) 의 Reviewer-only 단축 합의 보고서.** 사용자 명시 진입 명령 ("옵션 A로 진행해주세요") 답습.
>
> 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** — 실 변경 0건. Phase α-4 실 진입 / R-1 CI workflow 통합 본문 변경 / 3 MVP-1 workflow 외 workflow 흡수 / 신규 workflow 신설 / `pull_request_target` 도입 / GitHub Actions secrets 사용 / Phase α-1 / α-2 / α-3 자동 재진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / Layer C 발효 / MVP-1 PASS / 7 금지 영역 해소 / PC-4 / AR-2 / AR-3 / Stage 5 흡수 / Stage 4 합의 본문 변경 모두 본 합의 영역 외.

**작성일**: 2026-05-14 후속 14
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**검토 대상**: `docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (commit `f91ef4b`, 751줄)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3 R-7 합의, commit `3f6306d` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-runtime-ci-hook-implementation-entry.md` (5 Stage 분할안 — Stage 4 = Stage 1+3 완료 후 의존, commit `c50e6a0`)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (**Stage 4 (PC-3 + AR-1 통합) 단독 구현 진입 합의 APPROVE — sub-step 4.1 ~ 4.2 발효**)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.4 IR-1/IR-2/IR-3 + §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 (commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역 (CI step Entry)

---

## 0. 본 합의 범위

### 0.1 사용자 명시 진입 명령 답습

> "옵션 A로 진행해주세요"

(Phase α-1 / α-2 / α-3 패턴 답습 — brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 R-1 CI workflow 통합 수정은 아직 하지 않음.)

사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 패턴 답습 — brief §0.2 답습):

1. ❌ 실 R-1 CI workflow 수정 금지 — `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) / `provider-adapter-enforcement.yml` (186줄) / `provider-url-scanner.yml` (326줄) / `tools/mvp1_pc3_ar1_integration_check.py` (298줄) / `tests/fixtures/mvp1_pc3_ar1_integration/` (89줄) 어느 줄도 변경 0건 (현 7 artifacts × 1593줄 답습 보존)
2. ❌ CI workflow 신규 추가 금지
3. ❌ branch protection 변경 금지
4. ❌ dev 환경 강제 금지
5. ❌ `pre-commit install` 의무화 금지
6. ❌ Operational Readiness PASS 선언 금지
7. ❌ Hermes PMO 격상 금지

### 0.2 본 합의가 *하는* 것

1. Brief `phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (DRAFT, `f91ef4b`) 의 **수단 결정 적격성 권위 권고** 발행
2. **Backlog #6 우선 진입 합의 §6.1 2순위 (Phase α-4 = α-1+α-2+α-3 완료 후) 中 Phase α-4 영역 답습** 확인
3. **Phase α-4 = R-1 CI workflow 통합 영역 정의** 채택 권고 (7 artifacts × 1593줄 + PC-3 + AR-1 양 GP 공유 답습 + 4 sub-step)
4. **R-1 PoC 답습 변경 0건 확정** 채택 권고
5. **PC-3 + AR-1 sub-step 4.1 + 4.2 한정 답습 채택** (PC-4 sub-step 4.3 / AR-2 sub-step 4.4 / AR-3 / Stage 5 분리 명시)
6. **Phase α-4 진입 적격성 5 조건 (C-α4-1 ~ C-α4-5) 5/5 충족** 검증 — Phase α-1 / α-2 / α-3 *완료 후* 의존성 충족 (4 prerequisite runs PASS)
7. **14/14 풀 3+1 승격 트리거 0건 발화** 검증
8. **R-1 영역 영향 Rollback Trigger 18개 분류** 채택 권고 + PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog 4 trigger 분리
9. **실 R-1 CI workflow 통합 수정 진입 아직 아님** 답습 명시

### 0.3 본 합의가 *하지 않는* 것

- ❌ Phase α-4 실 진입 (R-1 본문 변경 0건)
- ❌ R-1 영역 7 artifacts × 1593줄 어느 줄도 변경 0건 (`secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`)
- ❌ 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC — `boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml`) 흡수 0건
- ❌ 신규 workflow 신설 0건 / `pull_request_target` workflow 도입 0건
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile 변경 0건
- ❌ R-4 도구 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 변경 0건
- ❌ R-5 `.importlinter` 본문 변경 0건
- ❌ R-7 docker secret block 본문 변경 0건
- ❌ Phase α-1 / α-2 / α-3 자동 재진입 0건
- ❌ Phase α-1 / α-2 / α-3 actual run 자동 재실행 0건
- ❌ Phase β / γ 자동 진입 0건
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` / `.git/hooks/*` 본문 변경 0건)
- ❌ PC-4 local pre-commit framework 진입 (sub-step 4.3 = Backlog #1+#2 분리)
- ❌ AR-2 branch protection rule 진입 (sub-step 4.4 = Backlog #3 T3 분리)
- ❌ AR-3 자동 revert bot 도입 (Backlog #3 T3 분리)
- ❌ Stage 5 (G3-7 4 항목) 자동 진입 (Stage 4 후속 권고 답습)
- ❌ Backlog #6 우선 진입 합의 §6.1 2순위 *해소* (의존성 정리 한정)
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *해소* 0건
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) *해소* 0건
- ❌ Phase α-3 합의 28 조건 (C-δ-1 ~ C-δ-28) *해소* 0건
- ❌ Stage 4 합의 *재결정* 0건
- ❌ 사용자 명시 7 금지 영역 어느 것의 *해소* (분리 매트릭스 한정)
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ Group α 합의 본문 변경 / 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ PC-3 + AR-1 = PC-4 / AR-2 / AR-3 / Stage 5 흡수 시도 0건
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold *고정* (CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출 (Group α C-11 답습 — 응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ 실 GitHub API / branch protection API 자동 호출
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ event enum 정식 등록 (`pc3_ar1_integration_implementation` = Backlog #5 분리)

### 0.4 본 합의 후속 commit chain

| Commit | 영역 | 권위 |
|--------|------|----|
| Commit 1 (`f91ef4b`) | brief 신설 (`docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md`, 751줄) | brief 본문 채택 |
| **Commit 2** | **본 합의 보고서 신설 (`docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md`)** | **Reviewer-only 단축 합의 — APPROVE AS BRIEF** |
| Commit 3 | 메타 갱신 (CONTEXT.md / INDEX.md / SESSION_2026-05-14.md) | 메타 답습 |

---

## 1. Phase α-4 R-1 CI workflow 통합 영역 정의 채택 (Brief §2 답습)

### 1.1 R-1 = CI workflow 통합 영역 정의 채택 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 + Stage 4 합의 답습)

| 영역 | 답습 출처 | 현 상태 (2026-05-15 기준) | 본 합의 채택 |
|------|---------|----------------------|----------|
| 책무 (PC-3 + AR-1 공유 영역) | GP-3 + GP-5 CI step 통합 + fail-closed 통합 | Layer B §5.5.1 + §5.5.2 양 GP 공유 채택 답습 | ✅ 답습 채택 |
| 도구 | 3 MVP-1 workflow + integration check tool + integration fixture | Stage 4 합의 4 sub-step 답습 | ✅ 답습 채택 |
| 권위 | mvp1.md §3.4.1 + §4.3 + §4.4 + §5.4 IR-1/IR-2/IR-3 | T2 영역 (CI step Entry) 답습 | ✅ 답습 채택 |
| 책무 분리 (PC-3 + AR-1 공유 단독) | PC-4 local pre-commit 미진입 (Backlog #1+#2 분리) / AR-2 branch protection 미진입 (Backlog #3 분리) / AR-3 자동 revert bot 미진입 (Backlog #3 분리) / Stage 5 (G3-7) 미진입 (Stage 4 후속 권고) | Stage 4 합의 답습 | ✅ 답습 채택 |

### 1.2 R-1 본문 7 artifacts 답습 채택 (실 본문 변경 0건 — enumerate 한정)

| # | 산출물 | 경로 | 현 라인 수 | 영역 | 본 합의 변경 |
|---|--------|------|---------|------|---------|
| 1 | GP-3 secret-hygiene workflow | `.github/workflows/secret-hygiene-egress-redaction.yml` | 694 | Stage 1 + Stage 2 + Stage 4 통합 | 0건 |
| 2 | GP-5 provider-adapter workflow | `.github/workflows/provider-adapter-enforcement.yml` | 186 | Stage 3 entry (T-2 + T-5) | 0건 |
| 3 | GP-5 provider-url-scanner workflow | `.github/workflows/provider-url-scanner.yml` | 326 | Stage 3 entry (T-5 URL + Model) | 0건 |
| 4 | Stage 4 integration check tool | `tools/mvp1_pc3_ar1_integration_check.py` | 298 | Stage 4 cross-workflow 검증 | 0건 |
| 5 | Stage 4 PASS fixture | `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` | 30 | PC-3 + AR-1 정합 entry step | 0건 |
| 6 | Stage 4 FAIL fixture (PC-3 violation) | `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` | 31 | PC-3 위반 (continue-on-error) | 0건 |
| 7 | Stage 4 FAIL fixture (AR-1 violation) | `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` | 28 | AR-1 위반 (no fail-closed) | 0건 |

**합산**: 7 artifacts × **1593줄 PoC 본문 답습 변경 0건** *확정 채택*.

### 1.3 R-1 = Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 채택

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-1 관계 | 본 합의 채택 |
|----------|------|----------------------|----------|----------|
| S-1 | 코드 본문 secret 검출 | Group D PoC 답습 | R-4 영역 (Phase α-1) — Stage 1 | ✅ 영역 분리 답습 |
| ST-3 | docker secret (저장 경로 isolation) | ADR-008 차단조건 #6 + 부록 B 답습 | R-7 영역 (Phase α-3) — Stage 2 | ✅ 영역 분리 답습 |
| **PC-3** | **CI-only enforcement (pre-commit)** | **T2 영역 + 양 GP 공유 채택 답습** | **R-1 본문 = PC-3 통합 (Stage 4 sub-step 4.1)** | ✅ **답습 채택** |
| **AR-1** | **CI step fail-closed (PR auto-reject)** | **T2 영역 + 양 GP 공유 채택 답습** | **R-1 본문 = AR-1 통합 (Stage 4 sub-step 4.2)** | ✅ **답습 채택** |
| T-2 + T-5 | provider scanner | Group A 1차+2차+3차 답습 | R-4 / R-5 영역 (Phase α-1 / α-2) | ✅ 영역 분리 답습 |

**범위 한계**: PC-4 (sub-step 4.3) = Backlog #1+#2 분리 / AR-2 (sub-step 4.4) = Backlog #3 분리 / AR-3 = Backlog #3 분리 / Stage 5 (G3-7) = Stage 4 후속 권고 답습.

### 1.4 R-1 영역 = Phase α-1 / α-2 / α-3 *완료 후* 의존성 충족 (Stage 4 합의 §1.2 답습)

| Phase | 영역 | 의존성 검증 | 본 합의 채택 |
|-------|------|----------|----------|
| Phase α-1 R-4 | 도구 본문 | actual run PASS 선행 evidence (run_id `25728590939` + `25728590916` + `25728590977` 후속 — `72622409` 기준) | ✅ **충족 완료** |
| Phase α-2 R-5 | `.importlinter` config | actual run PASS (`25728590916` 內 import-linter step) | ✅ **충족 완료** |
| Phase α-3 R-7 | docker secret block | actual run PASS (`25731846625` 후속 — `6c6b208` 기준) | ✅ **충족 완료** |

**의존성 충족 상태**: **4 prerequisite runs 모두 SUCCESS — Phase α-4 진입 적격성 의존성 검증 *통과***.

### 1.5 R-1 = 3 MVP-1 workflow 한정 답습 채택 (G2/G3/G4 PoC workflow 분리)

| workflow | 영역 | 본 합의 영역 |
|---------|------|----------|
| **`secret-hygiene-egress-redaction.yml`** (694줄) | Stage 1 + Stage 2 + Stage 4 | ✅ **R-1 본 영역** |
| **`provider-adapter-enforcement.yml`** (186줄) | Stage 3 (T-2 + T-5) | ✅ **R-1 본 영역** |
| **`provider-url-scanner.yml`** (326줄) | Stage 3 (T-5 URL + Model) | ✅ **R-1 본 영역** |
| `boundary-guard.yml` (306줄) | G3 boundary guard PoC | ✅ 영역 외 (G3/G4 PoC 분리) |
| `evidence-pass-gate.yml` (95줄) | G3 evidence pass gate PoC | ✅ 영역 외 |
| `g4-hash-chain.yml` (257줄) | G4 hash chain PoC | ✅ 영역 외 |
| `history-anchor-verifier.yml` (374줄) | G4 history anchor PoC | ✅ 영역 외 |
| `memory-skill-migration-feasibility.yml` (239줄) | G2 memory/skill migration PoC | ✅ 영역 외 |
| `r2-canary.yml` (133줄) | R2 canary PoC | ✅ 영역 외 |
| `rewrite-defense.yml` (360줄) | G4 rewrite defense PoC | ✅ 영역 외 |
| `schema-validation.yml` (273줄) | G3 schema validation PoC | ✅ 영역 외 |

본 합의 = **3 MVP-1 workflow 한정 답습** (1206줄) + **8 G2/G3/G4 PoC workflow 분리** (2037줄, 본 영역 외 답습).

---

## 2. R-1 PoC 답습 변경 0건 확정 (Brief §3 답습)

### 2.1 R-1 본문 답습 검증 채택

| 영역 | PoC 답습 | 현 상태 | 본 합의 변경 |
|------|--------|----------|---------|
| `secret-hygiene-egress-redaction.yml` (694줄) | Group D 12 step + Stage 1+2+4 통합 답습 | 답습 보존 | 0건 |
| `provider-adapter-enforcement.yml` (186줄) | Group A 1차 + 2차 답습 | 답습 보존 | 0건 |
| `provider-url-scanner.yml` (326줄) | Group A 3차 답습 | 답습 보존 | 0건 |
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) | Stage 4 합의 §1.3 답습 | 답습 보존 | 0건 |
| `tests/fixtures/mvp1_pc3_ar1_integration/` (89줄, 3 파일) | Stage 4 합의 §1.3 답습 | 답습 보존 | 0건 |

**합산**: 7 artifacts × **1593줄 PoC 답습 100% 보존** + 본 합의 발효 시점 변경 0건 *확정 채택*.

### 2.2 R-1 = Layer B + Stage 4 합의 답습 채택

| 답습 항목 | 본 합의 검증 | 충족 |
|---------|--------|------|
| Layer B `f40423f` APPROVE 발효 + §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 (`55c5b4b`) | ✅ 답습 변경 0건 | ✅ |
| 5 Stage 분할안 합의 (`c50e6a0`) — Stage 4 = Stage 1+3 완료 후 의존 | ✅ 답습 변경 0건 | ✅ |
| Stage 4 합의 (Reviewer-only APPROVE) — sub-step 4.1 ~ 4.2 4 cycle 발효 | ✅ 답습 변경 0건 | ✅ |
| Phase α-1 / α-2 / α-3 actual run PASS 선행 evidence | ✅ 4 prerequisite runs SUCCESS 답습 | ✅ |
| mvp1.md §3.4.1 + §4.3 + §4.4 + §5.4 IR-1/IR-2/IR-3 답습 | ✅ 답습 변경 0건 | ✅ |

**합산**: 5/5 답습 검증 *확정 채택*.

### 2.3 R-1 × Phase α-4 sub-step 분할 매트릭스 채택 (Brief §3 답습)

| sub-step | 영역 | 답습 출처 | 본 합의 채택 |
|---------|------|---------|----------|
| 4.1 | PC-3 CI step 통합 답습 검증 | mvp1.md §4.3 + Stage 4 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 4.1.a | `secret-hygiene-egress-redaction.yml` PC-3 통합 검증 (694줄) | Group D 12 step + Stage 1+2+4 통합 답습 | ✅ 답습 enumerate 한정 |
| 4.1.b | `provider-adapter-enforcement.yml` PC-3 통합 검증 (186줄) | Group A 1차+2차 답습 | ✅ 답습 enumerate 한정 |
| 4.1.c | `provider-url-scanner.yml` PC-3 통합 검증 (326줄) | Group A 3차 답습 | ✅ 답습 enumerate 한정 |
| 4.2 | AR-1 fail-closed 통합 답습 검증 | mvp1.md §4.4 + Stage 4 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 4.2.a | Stage 4 integration check tool 답습 검증 (298줄) | Stage 4 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 4.2.b | Stage 4 PASS fixture 답습 검증 (30줄) | Stage 4 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 4.2.c | Stage 4 FAIL fixture 답습 검증 (PC-3 violation 31줄 + AR-1 violation 28줄) | Stage 4 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 4.3 | PC-4 local pre-commit (영역 외) | Backlog #1 + #2 1.5차 보강 영역 분리 | ✅ 영역 외 답습 |
| 4.4 | AR-2 branch protection (영역 외) | Backlog #3 T3 영역 별도 풀 3+1 분리 | ✅ 영역 외 답습 |
| 4.5 | Stage 5 (G3-7) 후속 권고 (영역 외) | Stage 4 후속 권고 답습 | ✅ 영역 외 답습 |
| 4.6 | ledger entry 후보 — `event: pc3_ar1_integration_implementation` | mvp1.md §5.2 enum *후보 한정* | ✅ 정식 등록 0건 (Backlog #5 분리) |
| 4.7 | Evidence Artifact 형식 답습 | Layer B §1.8 (a) 답습 | ✅ 실 생성 = Layer C 시점 (영역 외) |

**합산**: **7 sub-step (4.1 + 4.1.a + 4.1.b + 4.1.c + 4.2 + 4.2.a + 4.2.b + 4.2.c + 4.6 + 4.7) 답습 enumerate 한정** *확정 채택* — 실 sub-step 결정 = Phase α-4 실 진입 시점.

---

## 3. PC-3 + AR-1 양 GP 공유 답습 채택 (Brief §2.3 + §2.5 답습)

### 3.1 PC-3 + AR-1 양 GP 공유 답습 채택 매트릭스

| sub-수단 | 영역 | 본 합의 분리 | 영역 |
|---------|------|----------|------|
| **PC-3 (sub-step 4.1)** | **CI-only enforcement (pre-commit) 통합** | ✅ **본 합의 영역 (sub-step 4.1 답습 채택)** | T2 영역 (CI step Entry) |
| **AR-1 (sub-step 4.2)** | **CI step fail-closed (PR auto-reject) 통합** | ✅ **본 합의 영역 (sub-step 4.2 답습 채택)** | T2 영역 |
| PC-4 (sub-step 4.3) | local pre-commit framework | ✅ Backlog #1 + #2 1.5차 보강 분리 | T3 영역 (사용자 명시 7 금지 #5) |
| AR-2 (sub-step 4.4) | branch protection rule | ✅ Backlog #3 T3 영역 별도 풀 3+1 분리 | T3 영역 (사용자 명시 7 금지 #3) |
| AR-3 | 자동 revert bot | ✅ Backlog #3 T3 영역 분리 | T3 영역 |
| Stage 5 (G3-7) | CI secret management 4 항목 | ✅ Stage 4 후속 권고 답습 | 별도 합의 영역 |

**합산**: 6/6 sub-수단 분리 매트릭스 채택 — PC-3 + AR-1 (sub-step 4.1 + 4.2) 단독 진입 적격 + PC-4 / AR-2 / AR-3 / Stage 5 영역 외 답습.

### 3.2 PC-3 + AR-1 단독 답습 채택 근거

1. **Layer B §5.5.1 + §5.5.2 양 GP 공유 채택 답습** — PC-3 + AR-1 = GP-3 + GP-5 일관성 답습 (sub-수단 #4 + #5)
2. **Stage 4 합의 답습** — Stage 4 (PC-3 + AR-1 통합) 단독 구현 진입 APPROVE
3. **T2 영역 한정 답습** — CI step Entry (사용자 승인 기반) — T3 영역 (AR-2 / Vault HSM / Tier-2/3 catalog) 분리
4. **Phase α-1 / α-2 / α-3 *완료 후* 의존성 충족** — 4 prerequisite runs PASS 답습

---

## 4. 5/5 진입 적격성 5 조건 충족 검증 (Brief §5.1 답습)

### 4.1 적격성 검토 매트릭스 채택

| 조건 # | 조건 | 본 합의 검증 결과 | 판정 |
|------|------|--------------|----|
| **C-α4-1** | **사용자 명시 7 금지 영역 충돌 0** | R-1 CI workflow 통합 = CI step 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0). 금지 #1 (실 R-1 수정) / #2 (CI workflow 신규 추가) = Phase α-4 *실 진입* 시점 적용 — 본 합의 = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α4-2** | **PoC 답습 변경 0** | R-1 영역 7 artifacts × 1593줄 답습 + Stage 4 합의 §1.3 4 sub-step 답습 + Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 + mvp1.md §4.3 + §4.4 답습 모두 변경 0건 | ✅ **답습 100% 보존** |
| **C-α4-3** | **의존성 충족 (Phase α-1 / α-2 / α-3 *완료 후* 의존)** | **4 prerequisite runs PASS 선행 evidence 답습 충족 완료** (run_id `25728590939` + `25728590916` + `25728590977` + `25731846625` 후속 — `72622409` + `6c6b208` 기준) | ✅ **의존성 충족 완료 (2순위 적격)** |
| **C-α4-4** | **Provider Liquidity 5-way 100% 보존** | R-1 = CI integration Layer — catalog / provider 영역과 직교 + CI workflow = vendor-agnostic 표준 (GitHub Actions) + provider key 사용 0건 (F-금지 #1 영구 답습) | ✅ **5/5 100% 보존** |
| **C-α4-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-1 = CI integration, Hermes PMO 영역 분리) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-1 = 수단, 목적 = CI-only enforcement + fail-closed) / T1/T2/T3 분리 보존 (R-1 = T2 영역, AR-2 / Vault HSM = T3 분리) / SPOF 의도적 수용 보존 | ✅ **5/5 보존** |

**합산**: **5/5 충족** *확정 채택* — Phase α-4 진입 적격성 검증 완료 + 실 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 5. 14/14 풀 3+1 승격 트리거 0건 발화 검증 (Brief §5.2 답습)

| # | 트리거 | 본 합의 발화 |
|---|----|----------|
| 1 | Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Phase α-2 C-γ-1 ~ C-γ-26 / Phase α-3 C-δ-1 ~ C-δ-28 / Stage 4 합의 어느 것의 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 2 | 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 합의 = 분리 매트릭스 한정 |
| 3 | Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — CI workflow = vendor-agnostic 표준 (catalog / provider 영역과 직교) |
| 5 | 5 영구 핵심 제약 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 | ❌ 0건 — R-1 = T2 영역 (AR-2 / Vault HSM = T3 영역 분리) |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | secret handling 방식이 기존 정책 변경 권고 (Stage 4 합의 §1.8 #1 답습) | ❌ 0건 — F-금지 #1 영구 답습 + GitHub Actions secrets 사용 도입 0건 |
| 9 | Hermes upstream root of trust 변경 권고 (Stage 4 합의 §1.8 #2 답습) | ❌ 0건 — CI workflow = upstream 분리 영역 |
| 10 | PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 (Stage 4 합의 §1.8 #3 답습) | ❌ 0건 — 경계 명확 (sub-step 4.1 + 4.2 vs 4.3 vs 4.4 vs Backlog #3) |
| 11 | 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | ❌ 0건 — 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC 8개 분리 명시) |
| 12 | 신규 workflow 신설 / `pull_request_target` 도입 권고 | ❌ 0건 — 신설 / `pull_request_target` 도입 0건 답습 |
| 13 | Stage 5 (G3-7 4 항목) 자동 진입 권고 | ❌ 0건 — Stage 4 후속 권고 답습 (Stage 5 별도 합의 분리) |
| 14 | Phase α-1 / α-2 / α-3 actual run 재실행 권고 | ❌ 0건 — 4 prerequisite runs PASS 선행 evidence 답습 한정 (재실행 0건) |

**검증 결과**: **14/14 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정** ✅

---

## 6. R-1 영역 영향 Rollback Trigger 18개 분류 채택 (Brief §6.1 답습)

### 6.1 R-1 본문 영역 *직접* 영향 trigger (4개) — 의존성 enumerate 한정

| Trigger | 발화 조건 | R-1 영향 | 본 합의 채택 |
|--------|---------|-----------|----------|
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | 3 MVP-1 workflow 실행 시간 영향 | ✅ 답습 한정 (발화 0건 — 4 prerequisite runs PASS 답습) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | Stage 4 integration check 검출 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | Stage 4 integration check 검출 영향 | ✅ 답습 한정 (발화 0건) |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 | Stage 4 integration check 검출 영향 | ✅ 답습 한정 (발화 0건) |

### 6.2 R-1 영역 *간접* 영향 trigger (1개) — Layer E 영역 의존

| Trigger | 영역 의존 | 본 합의 채택 |
|--------|---------|----------|
| R-MVP1-G3-8 | Operational Readiness parity 필요 (Hermes runtime parity) | ✅ 영역 외 답습 (Layer E, 금지 #6 답습) |

### 6.3 R-1 영역 *영향 0* trigger (13개) — Phase α-1/α-2/α-3/T3/MVP-3/MVP-6/Backlog 분리

| Trigger | 분리 사유 | 본 합의 채택 |
|--------|--------|----------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G3-2 | S-2 gitleaks (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-3 | ST-3 Docker secret (R-7 영역 = Phase α-3) | ✅ 영역 외 답습 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 (Backlog #3) | ✅ 영역 외 답습 |
| R-MVP1-G3-7 | Tier-2 확장 (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (R-5 영역 = Phase α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G5-3 | T-6 병행 충돌 (Phase α-1 + α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 (R-5 영역 = Phase α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-7 | P1 v2 facade real (Backlog #4) | ✅ 영역 외 답습 |
| R-MVP1-G5-8 | branch protection (T3, 금지 #3 — sub-step 4.4 분리) | ✅ 영역 외 답습 |
| R-MVP1-G5-9 | 의미적 lock-in (MVP-3) | ✅ 영역 외 답습 |
| R-MVP1-G5-10 | Layer 2 runtime (MVP-3/4) | ✅ 영역 외 답습 |

### 6.4 PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger (4개) — 분리 명시

| 영역 | 진입 trigger | 본 합의 채택 |
|------|----------|----------|
| PC-4 local pre-commit framework | sub-step 4.3 = Backlog #1 + #2 1.5차 보강 영역 | ✅ 영역 외 답습 (금지 #5 답습) |
| AR-2 branch protection rule | sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 | ✅ 영역 외 답습 (금지 #3 답습) |
| AR-3 자동 revert bot | Backlog #3 T3 영역 분리 | ✅ 영역 외 답습 (Group α 합의) |
| Stage 5 (G3-7 4 항목) | Stage 4 후속 권고 답습 | ✅ 영역 외 답습 (별도 합의 영역) |

### 6.5 합산 채택

| 분류 | trigger 수 | 본 합의 채택 |
|------|---------|----------|
| R-1 직접 영향 (Layer B 18) | 4 (G3-4, G3-5, G5-5, G5-6) | ✅ 의존성 enumerate 한정 (발화 0건) |
| R-1 간접 영향 (Layer E) | 1 (G3-8) | ✅ 영역 외 답습 |
| R-1 영향 0 (Phase α-1/α-2/α-3/T3/MVP-3/MVP-6/Backlog 분리) | 13 | ✅ 영역 외 답습 |
| **합산 (Layer B 18 trigger)** | **18 trigger** | ✅ **본문 확정 답습 + 발화 0건** |
| **추가: PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger** | **4** | ✅ **분리 명시 답습** |

---

## 7. 실 R-1 CI workflow 통합 수정 진입 아직 아님 (답습 명시)

### 7.1 본 합의 발효 후 영역 *내* vs *외*

| 영역 | 본 합의 발효 후 *영역 내* | 본 합의 발효 후 *영역 외* (별도 합의 / 사용자 명시 결정) |
|------|-------------------|-----------------------|
| Brief 본문 채택 권고 | ✅ APPROVE AS BRIEF | — |
| R-1 영역 7 artifacts × 1593줄 답습 채택 | ✅ APPROVE AS BRIEF | — |
| PC-3 + AR-1 양 GP 공유 단독 답습 채택 (PC-4 / AR-2 / AR-3 / Stage 5 분리) | ✅ APPROVE AS BRIEF | — |
| 적격성 5/5 충족 검증 (의존성 충족 포함) | ✅ APPROVE AS BRIEF | — |
| 14/14 풀 3+1 트리거 0건 발화 검증 | ✅ APPROVE AS BRIEF | — |
| 18 + 4 Rollback Trigger 분류 채택 | ✅ APPROVE AS BRIEF | — |
| Phase α-4 실 진입 | ❌ | Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| R-1 영역 7 artifacts 본문 변경 | ❌ | 동상 |
| 3 MVP-1 workflow 외 workflow 흡수 | ❌ | 별도 합의 영역 |
| 신규 workflow 신설 / `pull_request_target` 도입 | ❌ | 별도 합의 영역 (T2/T3) |
| GitHub Actions secrets 사용 도입 | ❌ | 영구 금지 (F-금지 #1 G3-7 (i) 답습) |
| Hermes upstream Dockerfile 변경 | ❌ | Backlog #1 1.5차 보강 영역 (풀 3+1 합의) |
| R-4 도구 본문 변경 | ❌ | Phase α-1 영역 (`1b3090b` 합의 답습) |
| R-5 `.importlinter` 본문 변경 | ❌ | Phase α-2 영역 (`6a79247` 합의 답습) |
| R-7 docker secret block 본문 변경 | ❌ | Phase α-3 영역 (`3f6306d` 합의 답습) |
| PC-4 / AR-2 / AR-3 / Stage 5 진입 | ❌ | Backlog #1+#2 / Backlog #3 / 별도 합의 영역 |
| Phase α-1 / α-2 / α-3 자동 재진입 | ❌ | 사용자 명시 결정 영역 |
| Phase α-1 / α-2 / α-3 actual run 자동 재실행 | ❌ | 4 prerequisite runs PASS 답습 한정 (재실행 0건) |
| 7 금지 영역 해소 | ❌ | 별도 합의 + 사용자 명시 결정 영역 |
| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| Layer D MVP-1 PASS 선언 | ❌ | Layer C 발효 후 별도 합의 |
| Layer E Operational Readiness PASS | ❌ | MVP-6 영역 |
| Layer F Hermes PMO 격상 | ❌ | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |

### 7.2 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

**Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 시점**:

1. Phase α 4 단계 (α-1 + α-2 + α-3 + α-4) 통합 진입 brief
2. **Layer C 발효 합의 brief (Implementation Evidence PASS)** — Phase α 4 단계 brief 완료로 가능성 진입
3. Phase α-4 실 진입 step 분할 brief (실 R-1 CI workflow 통합 운영 단계 분할안)
4. Phase α-1 ~ α-4 통합 실제 구현 계획 brief
5. Phase α-1 R-4 실 진입 step 분할 brief
6. Phase α-2 실 `.importlinter` 수정 step 분할 brief
7. Phase α-3 실 R-7 docker secret block 운영 단계 분할 brief
8. Group α 조건 재평가 (C-1 ~ C-12 영역)
9. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief
10. token rotation 정책 별도 합의 진입 brief (Group α C-3 답습)
11. GitHub plan / ruleset 가용성 확인 단계 진입 (Group α C-4 답습)
12. 세션 종료

---

## 8. 최종 판정 + Conditions

### 8.1 종합 판정

| 영역 | 판정 |
|------|----|
| **종합 판정** | **APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격) |
| 합의 단위 | brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| 합의 형태 | (가) Reviewer-only 단축 합의 (14/14 풀 3+1 트리거 0건 발화) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) |

### 8.2 본 합의 조건 (Conditions, 답습 한정)

| # | 조건 | 출처 |
|---|------|----|
| C-ε-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | 본 합의 §4 답습 |
| C-ε-2 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) *변경 0건* | 본 합의 §4 답습 |
| C-ε-3 | Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *변경 0건* | 본 합의 §4 답습 |
| C-ε-4 | Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) *변경 0건* | 본 합의 §4 답습 |
| C-ε-5 | Phase α-3 합의 28 조건 (C-δ-1 ~ C-δ-28) *변경 0건* | 본 합의 §4 답습 |
| C-ε-6 | Stage 4 합의 본문 *변경 0건* | 본 합의 §1 답습 |
| C-ε-7 | 5 Stage 분할안 합의 (`c50e6a0`) 본문 *변경 0건* | 본 합의 §1 답습 |
| C-ε-8 | 사용자 명시 7 금지 영역 (실 R-1 CI workflow 수정 / CI workflow 신규 추가 / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) *해소 0건* | 본 합의 §0.1 답습 |
| C-ε-9 | Phase α-4 실 진입 = **Backlog #6 + 사용자 명시 결정 영역** (자동 진입 0건) | 본 합의 §7.1 답습 |
| C-ε-10 | R-1 영역 7 artifacts × 1593줄 본문 어느 줄도 *변경 0건* | 본 합의 §2.1 답습 |
| C-ε-11 | PC-3 + AR-1 양 GP 공유 단독 답습 *변경 0건* — PC-4 / AR-2 / AR-3 / Stage 5 흡수 0건 | 본 합의 §3 답습 |
| C-ε-12 | 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC 8 workflow 흡수 0건) | 본 합의 §1.5 답습 |
| C-ε-13 | 신규 workflow 신설 0건 + `pull_request_target` 도입 0건 | 본 합의 §0.3 답습 |
| C-ε-14 | GitHub Actions secrets 사용 도입 *0건* (F-금지 #1 영구 답습) | 본 합의 §0.3 답습 |
| C-ε-15 | Hermes upstream Dockerfile 변경 *0건* | 본 합의 §0.3 답습 |
| C-ε-16 | R-4 도구 본문 / R-5 `.importlinter` 본문 / R-7 docker secret block 어느 영역도 *변경 0건* | 본 합의 §7.1 답습 |
| C-ε-17 | Layer A / Layer B / §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 *변경 0건* | 본 합의 §1.3 답습 |
| C-ε-18 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §7 답습 |
| C-ε-19 | Phase α-1 / α-2 / α-3 *자동 재진입 0건* | 본 합의 §7.1 답습 |
| C-ε-20 | Phase α-1 / α-2 / α-3 actual run *자동 재실행 0건* (4 prerequisite runs PASS 선행 evidence 답습) | 본 합의 §1.4 답습 |
| C-ε-21 | Phase β / γ *자동 진입 0건* | 본 합의 §7.1 답습 |
| C-ε-22 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | 본 합의 §0.3 답습 |
| C-ε-23 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* (Group α C-3 + C-4 답습) | 본 합의 §0.3 답습 |
| C-ε-24 | Stage 5 (G3-7 4 항목) *자동 진입 0건* (Stage 4 후속 권고 답습) | 본 합의 §6.4 답습 |
| C-ε-25 | R-MVP1-G3-4 / G3-5 / G5-5 / G5-6 (R-1 직접 영향 4 trigger) *자동 발화 0건* | 본 합의 §6.1 답습 |
| C-ε-26 | 외부 LLM *응답 결론 강제 채택 0건* (응답 = 입력 한정 — Group α C-11 답습) | 본 합의 §8.1 답습 |
| C-ε-27 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | 본 합의 §4 답습 |
| C-ε-28 | Provider Liquidity 5-way **100% 보존** (R-1 = CI integration Layer = catalog / provider 영역과 직교) | 본 합의 §4 답습 |
| C-ε-29 | 본 합의 = **수단 결정 적격성 권위 권고 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | 본 합의 §7 답습 |

**합산**: **29 조건 (C-ε-1 ~ C-ε-29) 충족 시 = 본 합의 진입 적합** + 본 합의 = "수단 결정 적격성 권위 권고 발행" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 9. 변경 0건 / 진입 0건 검증

### 9.1 본 합의 발효 시점 변경 0건 영역

| 영역 | 변경 |
|------|----|
| `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) | 0건 |
| `.github/workflows/provider-adapter-enforcement.yml` (186줄) | 0건 |
| `.github/workflows/provider-url-scanner.yml` (326줄) | 0건 |
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) | 0건 |
| `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` (30줄) | 0건 |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` (31줄) | 0건 |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` (28줄) | 0건 |
| 3 MVP-1 workflow 외 G2/G3/G4 PoC workflow 8개 (2037줄) | 0건 |
| Hermes upstream Dockerfile | 0건 |
| Production `docker-compose.yml` | 0건 |
| R-4 도구 (829줄) | 0건 |
| `/.importlinter` (35줄) | 0건 |
| R-7 docker secret block 9 artifacts (328줄) | 0건 |
| `requirements*.txt` | 0건 |
| `src/adapters/llm/facade.py` | 0건 |
| `.pre-commit-config.yaml` 본문 | 0건 |
| Phase α-1 합의 (`1b3090b`) 본문 | 0건 |
| Phase α-2 합의 (`6a79247`) 본문 | 0건 |
| Phase α-3 합의 (`3f6306d`) 본문 | 0건 |
| Backlog #6 우선 진입 합의 (`c7ddfdd`) 본문 | 0건 |
| Group α 합의 (`4880e88`) 본문 | 0건 |
| Stage 4 합의 본문 | 0건 |
| 5 Stage 분할안 합의 (`c50e6a0`) 본문 | 0건 |
| Layer A (`f1e0b23`) 본문 | 0건 |
| Layer B (`f40423f`) 본문 | 0건 |
| Layer D (`210c98f`) 본문 | 0건 |
| `implementation-runtime-roadmap-mvp1.md` §5.5.1 + §5.5.2 PC-3 + AR-1 본문 채택 | 0건 |
| ADR-008 ~ ADR-012 본문 | 0건 (cross-reference 답습 한정) |
| GitHub branch protection rule / Actions secrets / permissions | 0건 |

### 9.2 본 합의 발효 시점 진입 0건 영역

| 영역 | 진입 |
|------|----|
| Phase α-4 실 진입 (R-1 CI workflow 통합 본문 변경) | 0건 |
| Phase α-1 / α-2 / α-3 자동 재진입 | 0건 |
| Phase α-1 / α-2 / α-3 actual run 자동 재실행 | 0건 |
| Phase β / γ 자동 진입 | 0건 |
| Backlog #6 실 진입 | 0건 |
| PC-4 (sub-step 4.3) / AR-2 (sub-step 4.4) / AR-3 / Stage 5 자동 진입 | 0건 |
| R-MVP1-G3-4 / G3-5 / G5-5 / G5-6 자동 발화 | 0건 |
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
| event enum 정식 등록 (`pc3_ar1_integration_implementation` = Backlog #5 분리) | 0건 |
| 외부 LLM 자동 호출 | 0건 |
| 외부 LLM 응답 결론 강제 채택 | 0건 |
| 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 실 GitHub API / branch protection API 자동 호출 | 0건 |
| GitHub Actions secrets 사용 도입 | 0건 |
| `pull_request_target` workflow 도입 | 0건 |
| 신규 workflow 신설 | 0건 |
| 3 MVP-1 workflow 외 workflow 흡수 | 0건 |
| 인간 리뷰 의무 자동 발화 | 0건 |
| token rotation 정책 자동 결정 | 0건 |
| GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| commit signing 도입 | 0건 |
| Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| threshold *고정* | 0건 (모두 *후보 한정* 유지) |
| MVP-1 PASS 재선언 | 0건 |
| GP-3 / GP-5 PASS 발효 | 0건 |
| ADR 본문 자동 갱신 | 0건 |
| Layer 2 runtime block (G5-5) 진입 | 0건 |

---

## 10. 본 합의 요약 (한 단락)

본 합의는 **`docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (DRAFT, commit `f91ef4b`, 751줄) 의 Reviewer-only 단축 합의 보고서** 다. 사용자 명시 진입 명령 ("옵션 A로 진행해주세요") + Phase α-1 / α-2 / α-3 패턴 답습. **판정 = APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격 — **14/14 풀 3+1 트리거 0건 발화** 확인). 본 합의 = **Backlog #6 우선 진입 합의 §6.1 *2순위* (Phase α-1 + α-2 + α-3 1순위 완료 후 의존) 中 Phase α-4 답습** + **R-1 = CI workflow 통합 본문 정의 채택 권고** (7 artifacts × **1593줄 답습** — `secret-hygiene-egress-redaction.yml` 694줄 (Stage 1+2+4 통합) + `provider-adapter-enforcement.yml` 186줄 (Stage 3 T-2+T-5) + `provider-url-scanner.yml` 326줄 (Stage 3 T-5 URL+Model) + `tools/mvp1_pc3_ar1_integration_check.py` 298줄 (Stage 4 cross-workflow 검증 도구) + `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` 30줄 + `fail/pc3_violation_continue_on_error.yml` 31줄 + `fail/ar1_violation_no_fail_closed.yml` 28줄 — 본문 변경 0건) + **PC-3 + AR-1 양 GP 공유 답습 채택** (Layer B §5.5.1 + §5.5.2 sub-step 4.1 + 4.2 한정) + **Stage 4 합의 답습** + **3 MVP-1 workflow 한정 답습** (G2/G3/G4 PoC 8 workflow 2037줄 분리) + **PC-4 / AR-2 / AR-3 / Stage 5 분리** (sub-step 4.3 / 4.4 / Backlog #3 / Stage 4 후속 권고 분리 명시) + **7 sub-step 분할 매트릭스 채택 권고** + **5/5 진입 적격성 5 조건 (C-α4-1 ~ C-α4-5) 충족 검증** (특히 C-α4-3 = Phase α-1 / α-2 / α-3 *완료 후* **의존성 충족 완료** — 4 prerequisite runs PASS `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습) + **14/14 풀 3+1 트리거 0건 발화 검증** + **18 + 4 Rollback Trigger 분류 채택** (R-1 직접 영향 4 + 간접 영향 1 + 영향 0 13 + PC-4/AR-2/AR-3/Stage 5 별도 backlog 4 trigger 분리) + **29 합의 조건 (C-ε-1 ~ C-ε-29)** 답습. **사용자 명시 7 금지 7/7 답습** (실 R-1 CI workflow 수정 0건 / CI workflow 신규 추가 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (R-1 = CI integration Layer = catalog / provider 영역과 직교, CI workflow = vendor-agnostic 표준) + **F-금지 #1 영구 답습 — GitHub Actions secrets 사용 도입 0건** + **Group α 합의 본문 변경 0건** + **Backlog #6 우선 진입 합의 본문 변경 0건** + **Phase α-1 / α-2 / α-3 합의 본문 변경 0건** + **Stage 4 합의 본문 변경 0건** + **5 Stage 분할안 합의 본문 변경 0건** + **Layer A / Layer B / §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 0건** + **R-1 영역 7 artifacts × 1593줄 어느 줄도 변경 0건** (PoC 답습 100% 보존) + **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 0건** + **신규 workflow 신설 0건 + `pull_request_target` 도입 0건** + **Hermes upstream Dockerfile 변경 0건** + **R-4 도구 / R-5 `.importlinter` / R-7 docker secret block / `.pre-commit-config.yaml` 변경 0건** + **PC-3 + AR-1 = PC-4 / AR-2 / AR-3 / Stage 5 흡수 0건** + **Phase α-1 / α-2 / α-3 자동 재진입 0건 + actual run 자동 재실행 0건** + **R-MVP1-G3-4 / G3-5 / G5-5 / G5-6 자동 발화 0건** + **외부 LLM 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **Phase α-4 실 진입 0건** + **Phase β / γ 자동 진입 0건** + **7 금지 영역 *해소* 0건** + **Layer C / D / E / F 발효 0건** + **Group I / β / γ-1 / γ-2 자동 진입 0건** + **자동 진입 모두 0건**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건) — **Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 시점** (α-1 + α-2 + α-3 + α-4): (1) Phase α 4 단계 통합 진입 brief / (2) **Layer C 발효 합의 brief** (Implementation Evidence PASS — Phase α 4 단계 brief 완료로 가능성 진입) / (3) Phase α-4 실 진입 step 분할 brief / (4) Phase α-1 ~ α-4 통합 실제 구현 계획 brief / (5) Phase α-1 / α-2 / α-3 실 진입 step 분할 brief / (6) Group α 조건 재평가 / (7) Group I 별도 합의 / (8) token rotation 정책 별도 합의 / (9) GitHub plan 가용성 확인 / (10) 세션 종료.

---

**작성일**: 2026-05-14 후속 14
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
**금지 (사용자 명시 답습 — 본 합의 영역)**:
- ❌ **실 R-1 CI workflow 수정** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 신규 추가** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ R-1 영역 7 artifacts × 1593줄 어느 줄도 변경
- ❌ 3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수
- ❌ 신규 workflow 신설 / `pull_request_target` workflow 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile 변경
- ❌ R-4 도구 본문 변경
- ❌ R-5 `.importlinter` 본문 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ Phase α-4 실 진입 자동 진입 금지
- ❌ Phase α-1 / α-2 / α-3 자동 재진입 금지
- ❌ Phase α-1 / α-2 / α-3 actual run 자동 재실행 금지
- ❌ Phase β / γ 자동 진입 금지
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ PC-3 + AR-1 = PC-4 (sub-step 4.3 = Backlog #1+#2 분리) / AR-2 (sub-step 4.4 = Backlog #3 분리) / AR-3 / Stage 5 흡수 시도
- ❌ Stage 5 (G3-7 4 항목) 자동 진입
- ❌ R-MVP1-G3-4 / G3-5 / G5-5 / G5-6 자동 발화
- ❌ Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경
- ❌ Stage 4 합의 §1.3 4 sub-step 분할안 변경
- ❌ 5 Stage 분할안 합의 (`c50e6a0`) 본문 변경
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 자동 변경
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경
- ❌ Phase α-3 합의 28 조건 (C-δ-1 ~ C-δ-28) 자동 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출
- ❌ 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 실 GitHub API / branch protection API 자동 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ event enum 정식 등록 (`pc3_ar1_integration_implementation` = Backlog #5 분리)
