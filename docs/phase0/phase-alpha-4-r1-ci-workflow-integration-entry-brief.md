# Phase α-4 R-1 CI workflow 통합 진입 Brief (준비안 — DRAFT)

> **본 문서는 Backlog #6 Runtime + CI-hook 우선 진입 합의 (`docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md`, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) §6.1 2순위 §5.2 α-4 답습 후속, Phase α 4 단계 中 α-4 (R-1 CI workflow 통합) *진입 가능성 검토* 한정 의 brief 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Phase α-4 실 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / Phase α-3 합의 28 조건 C-δ-1 ~ C-δ-28 / Stage 4 합의 / 사용자 명시 7 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF)
- `docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (commit `233892b`)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3 R-7 합의, commit `3f6306d` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-runtime-ci-hook-implementation-entry.md` (5 Stage 분할안 — Stage 4 = Stage 1 + Stage 3 *완료 후* 통합 가능 적격성, commit `c50e6a0`)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (**Stage 4 (PC-3 + AR-1 통합) 단독 구현 진입 합의 APPROVE — sub-step 4.1 ~ 4.2 발효**)
- `docs/phase0/backlog6-implementation-step-brief.md` §2.2.4 (Stage 4 sub-step 4.1 ~ 4.4 분할안) + §3.1 (Stage 4 = Stage 1 + Stage 3 *완료 후* 의존)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 (G3-2 secret_scanner CI 통합) + §4.3 (GP-5 PC-3 CI-only enforcement) + §4.4 (GP-5 AR-1 PR auto-reject) + §5.4 (GP-3 + GP-5 Integrated Risk Matrix IR-1/IR-2/IR-3) + §5.5.1 PC-3 + AR-1 본문 채택 (commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역 (CI step Entry)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-4 R-1 CI workflow 통합 진입 brief를 작성해주세요."

### 0.2 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 패턴 답습)

사용자가 본 brief 진입 명령 시 명시 prohibitions 를 enumerate 하지 않았으나, **Backlog #6 우선 진입 합의 §6.1 2순위 답습 + Phase α-1 (`1b3090b`) + Phase α-2 (`6a79247`) + Phase α-3 (`3f6306d`) 답습 패턴** = 7 금지 영역 유지 (사용자 명시 강조 답습) — 본 brief = 본 패턴 답습 (#1 = R-1 영역 한정):

1. ❌ **실 R-1 CI workflow 수정 금지** — `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) / `provider-adapter-enforcement.yml` (186줄) / `provider-url-scanner.yml` (326줄) / `tools/mvp1_pc3_ar1_integration_check.py` (298줄) / `tests/fixtures/mvp1_pc3_ar1_integration/` (89줄) 본문 변경 모두 0건
2. ❌ **CI workflow 신규 추가 금지** — `.github/workflows/*.yml` 신설 (3 MVP-1 workflow 외) 0건
3. ❌ **branch protection 변경 금지**
4. ❌ **dev 환경 강제 금지**
5. ❌ **`pre-commit install` 의무화 금지**
6. ❌ **Operational Readiness PASS (Layer E) 선언 금지**
7. ❌ **Hermes PMO 격상 (Layer F) 금지**

본 7 금지 답습 = 사용자 명시 패턴 보존 — 사용자가 본 brief 검토 시 prohibition 추가/축소 권위 영역 (옵션 (B) 수정 요청 답습).

### 0.3 본 brief 가 *하는* 것

1. Backlog #6 우선 진입 합의 §6.1 2순위 + §5.2 α-4 답습 — Phase α-4 = R-1 CI workflow 통합 영역 *진입 가능성 검토 한정* (§1)
2. **R-1 영역 = CI workflow 통합 (Stage 4 PC-3 + AR-1) 본문 정의** + 현 상태 enumeration (§2)
3. **R-1 × Phase α-4 본문 작업 후보 분할 매트릭스** — 4 sub-step (4.1 PC-3 CI step 통합 / 4.2 AR-1 fail-closed 통합 / 4.3 PC-4 local pre-commit (Backlog #1+#2 분리) / 4.4 AR-2 branch protection (Backlog #3 분리)) (§3)
4. **사용자 명시 7 금지 영역 × R-1 본문 분리 매트릭스** (§4)
5. **Phase α-4 진입 적격성 5 조건 검토** — Phase α-1 / α-2 / α-3 actual run PASS 선행 evidence 의존성 검토 포함 (§5)
6. **Rollback Trigger 의존성 답습** — R-1 영역에 영향 받는 trigger enumerate (§6)
7. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 7 금지 영역**:

- ❌ **실 R-1 CI workflow 수정 (0건)** — `secret-hygiene-egress-redaction.yml` 694줄 / `provider-adapter-enforcement.yml` 186줄 / `provider-url-scanner.yml` 326줄 / `tools/mvp1_pc3_ar1_integration_check.py` 298줄 / `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/` 89줄 본문 변경 0건 — **합산 7 artifacts × 1593줄 PoC 답습 변경 0건**
- ❌ **CI workflow 신규 추가 (0건)** — `.github/workflows/*.yml` 3 MVP-1 workflow 외 신설 0건
- ❌ **branch protection 변경 (0건)** — AR-2 (CODEOWNERS + required status check) / direct push 차단 / force push 차단 / admin bypass OFF / required PR review count / linear history / deployments 모두 변경 0건 (Group α 합의 5.1 #6 답습 + 사용자 명시 5 금지 #1 답습)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 0건
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 / `default_install_hook_types` 본문 결정 모두 0건 (Group α 합의 5.2 #9 답습)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 / `.pre-commit-config.yaml` 본문 변경 0건 (PC-4 = Backlog #1+#2 분리)
- ❌ **PC-4 local pre-commit framework 진입 (0건)** — sub-step 4.3 = Backlog #1 + #2 1.5차 보강 분리 (dev 환경 영향 정책 영역 = T3)
- ❌ **AR-2 branch protection rule 진입 (0건)** — sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 분리
- ❌ **AR-3 자동 revert bot 도입 (0건)** — Backlog #3 T3 영역 분리
- ❌ **R-4 도구 본문 변경 (0건)** — Phase α-1 R-4 영역 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 본문 변경 모두 0건 (Phase α-1 = 별도 영역, `1b3090b` 합의 답습)
- ❌ **R-5 `.importlinter` 본문 변경 (0건)** — Phase α-2 영역 분리 (`6a79247` 합의 답습)
- ❌ **R-7 docker secret block 본문 변경 (0건)** — Phase α-3 영역 분리 (`3f6306d` 합의 답습)
- ❌ **Phase α-1 / α-2 / α-3 자동 진입 (0건)** — 본 brief = Phase α-4 *진입 가능성 검토 한정*
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM / Layer E / Layer F 모두 영역 외
- ❌ **Implementation Evidence PASS (Layer C) 발효 (0건)** + **MVP-1 PASS (Layer D) 선언 (0건)**
- ❌ **CI workflow 룰 *재설계* (0건)** — Stage 4 합의 답습 한정 (sub-step 4.1 + 4.2 답습)
- ❌ **3 MVP-1 workflow 외 workflow 의 Stage 4 step 흡수 시도 (0건)** — `boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml` 등 G2/G3/G4 PoC workflow 는 R-1 영역 외 — 분리 명시
- ❌ **`pull_request_target` workflow 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **commit signing 도입 (0건)** — MVP-6 영역 답습
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습 (G3-7 (i))
- ❌ **Stage 4 integration tool 본문 *재설계* (0건)** — `tools/mvp1_pc3_ar1_integration_check.py` 298줄 답습 변경 0건
- ❌ **Stage 4 integration fixture 본문 *재설계* (0건)** — `compliant_entry_step.yml` 30줄 / `pc3_violation_continue_on_error.yml` 31줄 / `ar1_violation_no_fail_closed.yml` 28줄 답습 변경 0건
- ❌ **Group α 14 결정 영역 *재결정* (0건)**
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / Phase α-3 합의 / Stage 4 합의 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 답습 한정
- ❌ **3 MVP-1 workflow actual run 자동 재실행 (0건)** — Phase α-1 / α-2 / α-3 actual run PASS 선행 evidence 답습 한정 (run_id `25728590939` + `25728590916` + `25728590977` + `25731846625` 후속)
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)**
- ❌ **threshold *고정* (0건)** — CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **git commit / push (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **실 GitHub API / branch protection API 호출 자동 진입 (0건)** — 본 brief = 영역 정의 검토 한정 (실 actual run = 사용자 명시 결정 영역)
- ❌ **Layer 2 runtime block (G5-5) 진입 (0건)** — MVP-3/4 영역 분리
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 (0건)** — Backlog #4 분리
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-4 실 진입을 *시작* 시키지 않으며,
- (ii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / Phase α-3 합의 28 조건 C-δ-1 ~ C-δ-28 / Stage 4 합의 의 어느 조건도 *해소* 시키지 않으며,
- (iii) 사용자 명시 7 금지 영역 어느 것도 진입시키지 않으며,
- (iv) Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / Phase α-3 합의 / Stage 4 합의 본문을 *변경* 하지 않으며,
- (v) R-1 영역 본문 (`.github/workflows/secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`) 어느 줄도 *변경* 하지 않으며 (현 7 artifacts × 1593줄 답습),
- (vi) PC-4 / AR-2 / AR-3 어느 영역도 *진입* 시키지 않으며,
- (vii) Stage 5 (G3-7 4 항목) 어느 것도 *자동 진입* 시키지 않으며,
- (viii) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (ix) Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 CI workflow 통합 영역의 *진입 가능성 검토* — 본문 정의 + Phase α-4 본문 작업 후보 분할 매트릭스 + 7 금지 분리 매트릭스 + 진입 적격성 5 조건 검토 + Rollback Trigger 의존성 + 금지 영역 enumeration + 합의 형태 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Backlog #6 우선 진입 합의 §5.2 α-4 답습 (`c7ddfdd`)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의, 7/7 풀 3+1 트리거 0건 발화) |
| 합의 단위 | Backlog #6 우선 진입 brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| Phase α 4 단계 | α-1 (R-4) / α-2 (R-5) / α-3 (R-7) / α-4 (R-1) |
| Phase α-4 정의 (합의 §5.2 답습) | **R-1 CI workflow 통합 (Stage 4) — α-1 ~ α-3 *완료 후* 진입** |
| 진입 우선순위 (합의 §6.1) | **2순위** — Phase α-1 + α-2 + α-3 (1순위 병렬) 완료 후 진입 적격 |
| 진입 결정 권위 | **Backlog #6 실 진입 + 사용자 명시 결정 영역** (본 합의 영역 외) |

**Phase α-1 / α-2 / α-3 와 의 차이**: Phase α-4 = **2순위** + **α-1 ~ α-3 *완료 후* 의존** (의존성 측면에서 1순위 병렬 그룹과 분리 — Backlog #6 §5.2 답습 + backlog6-implementation-step-brief §3.1 답습).

### 1.2 Stage 4 합의 답습 (`3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md`)

본 brief 는 Stage 4 합의 *발효 후속* — Stage 4 (공유 PC-3 + AR-1 통합) 단독 구현 진입 합의 (APPROVE, Reviewer-only 단축 — 5/5 트리거 0건 발화) 답습 한정:

| 합의 영역 | 답습 |
|---------|----|
| 합의 판정 | APPROVE — Stage 4 (공유 PC-3 + AR-1 통합) 구현 진입 READY |
| 합의 형태 | Reviewer-only 단축 합의 (5/5 트리거 0건 발화 확정) |
| 발효 시점 | 2026-05-12 후속 15 (Stage 2 단독 진입 commit `09edd9d` 후속 + actual run `25731846625` SUCCESS 후) |
| 4 sub-step 분할 | 4.1 PC-3 CI step 통합 / 4.2 AR-1 fail-closed 통합 / 4.3 PC-4 local pre-commit (Backlog #1+#2 분리) / 4.4 AR-2 branch protection (Backlog #3 분리) |
| 본문 채택 | Stage 4 = Stage 1 + Stage 2 + Stage 3 actual run PASS 선행 evidence 보존 (3 prerequisite run 모두 SUCCESS) |
| 발효 영역 | Stage 4 *구현 진입 적격성* 한정 — Implementation Evidence PASS 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 모두 영역 외 |

**본 brief 관계**: Stage 4 합의는 *Stage 단위* 진입 적격성 권위 권고 (Layer B 흡수 영역). 본 brief = Phase α-4 = **Backlog #6 우선 진입 합의의 4 Phase 분할 中 2순위 1단계** *진입 가능성 검토 한정* (별도 framing — Layer A/B → Backlog #6 우선 진입 → Phase α 4단계 framing).

### 1.3 Backlog #6 우선 진입 합의 §6.2 권고 한계 답습

> 본 합의 = **Phase α 우선 진입 *권위 권고 발행 한정***
> 실 Phase α 진입 = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
> 자동 진입 0건

본 brief 의 의미:

- (a) Backlog #6 우선 진입 합의 발효 *자체* = 완료 (`c7ddfdd`)
- (b) Phase α-1 R-4 brief = 완료 (`e7cdb21` + `1b3090b` APPROVE AS BRIEF)
- (c) Phase α-2 R-5 brief = 완료 (`608a046` + `6a79247` APPROVE AS BRIEF)
- (d) Phase α-3 R-7 brief = 완료 (`8da3273` + `3f6306d` APPROVE AS BRIEF)
- (e) Phase α-4 R-1 CI workflow 통합 *실 진입* = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
- (f) 본 brief = (e) *진입 가능성 검토 한정* — 실 진입 *직전* 의사결정 사전 정비 영역
- (g) 본 brief = Backlog #6 우선 진입 합의의 7 금지 영역 *해소* 가 아님 + Phase α-1 / α-2 / α-3 합의 *해소* 도 아님 + Stage 4 합의 *재결정* 도 아님

### 1.4 6-Layer 분리 매트릭스 현 상태 (2026-05-15 후속)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + §5.5 `55c5b4b`) | 답습 한정 (PC-3 + AR-1 양 GP 공유 답습) |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 | ✅ APPROVE WITH CONDITIONS (`4880e88`) | 답습 한정 (AR-2 / AR-3 / PC-4 = sub-step 4.3 / 4.4 분리) |
| Backlog #6 우선 진입 | Runtime + CI-hook 영역 정의 + Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) | 답습 한정 |
| Phase α-1 R-4 도구 본문 진입 | R-4 (S-1 + T-2 + T-5) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`1b3090b`) | 답습 한정 (15 조건 C-β-1 ~ C-β-15 해소 0건) |
| Phase α-2 R-5 `.importlinter` 본문 진입 | R-5 (T-2 import-linter) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`6a79247`) | 답습 한정 (26 조건 C-γ-1 ~ C-γ-26 해소 0건) |
| Phase α-3 R-7 docker secret block 진입 | R-7 (ST-3 docker secret) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`3f6306d`) | 답습 한정 (28 조건 C-δ-1 ~ C-δ-28 해소 0건) |
| Stage 4 PC-3 + AR-1 통합 구현 진입 | Stage 4 (PC-3 + AR-1) 4 sub-step 진입 적격성 | ✅ APPROVE (Reviewer-only) | **본 brief = R-1 CI workflow 통합 *Phase α-4 framing 진입 가능성 검토*** |
| Phase α-4 R-1 진입 | **본 brief 영역** | ⏳ DRAFT (본 brief = 준비안) | **본 brief = §6.1 2순위 *진입 가능성 검토*** |
| Layer C | Implementation Evidence PASS 발효 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #6) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #7) |

### 1.5 본 brief 의 진입점

```
Layer A APPROVE (f1e0b23) ─────────────────────────────────────────┐
Layer B APPROVE (f40423f)                                          │
§5.5 9 sub-수단 (55c5b4b) — PC-3 + AR-1 양 GP 공유 채택              │
Group α APPROVE (4880e88) — AR-3 + PC-4 T3 sub (4.3/4.4 분리)      │
5 Stage 분할안 합의 (c50e6a0) — Stage 4 = Stage 1+3 완료 후 의존     │
Stage 4 합의 (Reviewer-only APPROVE) — sub-step 4.1 ~ 4.2 발효
3 prerequisite actual run PASS (25728590939 + 25728590916 + 25728590977 + 25731846625)
backlog6 priority brief (233892b)                                  │
Backlog #6 우선 진입 합의 (c7ddfdd) APPROVE AS BRIEF                │
Phase α-1 R-4 brief (e7cdb21) + 합의 (1b3090b) APPROVE AS BRIEF
Phase α-2 R-5 brief (608a046) + 합의 (6a79247) APPROVE AS BRIEF
Phase α-3 R-7 brief (8da3273) + 합의 (3f6306d) APPROVE AS BRIEF
   │
   ▼
■ 본 brief = Phase α-4 R-1 CI workflow 통합 *진입 가능성 검토* (DRAFT)        ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 실 진입 (R-1 CI workflow 통합 운영 진입)                          ← 본 brief 영역 외
   │
   ▼ (R-4 + R-5 + R-7 + R-1 완료 + actual run SUCCESS + evidence 5/5 후)
Layer C 발효 합의 — Implementation Evidence PASS                            ← 본 brief 영역 외
```

---

## 2. R-1 영역 정의 (Phase α-4 한정)

### 2.1 R-1 = CI workflow 통합 영역 정의 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5.1 PC-3 + AR-1 + Stage 4 합의 답습)

| 영역 | 답습 출처 | 현 상태 (2026-05-15 기준) |
|------|---------|----------------------|
| 책무 (PC-3 + AR-1 공유 영역) | GP-3 + GP-5 CI step 통합 + fail-closed 통합 | Layer B §5.5.1 + §5.5.2 양 GP 공유 채택 답습 |
| 도구 | 3 MVP-1 workflow + integration check tool + integration fixture | Stage 4 합의 4 sub-step 답습 |
| 권위 | mvp1.md §3.4.1 + §4.3 + §4.4 + §5.4 IR-1/IR-2/IR-3 | T2 영역 (CI step Entry) 답습 |
| 책무 분리 (PC-3 + AR-1 공유 단독) | PC-4 local pre-commit 미진입 (Backlog #1+#2 분리) / AR-2 branch protection 미진입 (Backlog #3 분리) / AR-3 자동 revert bot 미진입 (Backlog #3 분리) / Stage 5 (G3-7) 미진입 (Stage 4 후속 권고 답습) | Stage 4 합의 답습 (sub-step 4.1 + 4.2 한정) |

### 2.2 R-1 본문 7 artifacts 답습 (현 라인 수 — 실 본문 변경 0건, enumerate 한정)

| # | 산출물 | 경로 | 현 라인 수 | 영역 | 답습 출처 |
|---|--------|------|---------|------|---------|
| 1 | GP-3 secret-hygiene workflow | `.github/workflows/secret-hygiene-egress-redaction.yml` | 694 | Stage 1 entry + Stage 2 entry + Stage 4 integration | Group D PoC + Stage 1+2+4 답습 |
| 2 | GP-5 provider-adapter workflow | `.github/workflows/provider-adapter-enforcement.yml` | 186 | Stage 3 entry (T-2 import-linter + T-5 AST) | Group A 1차+2차 PoC 답습 |
| 3 | GP-5 provider-url-scanner workflow | `.github/workflows/provider-url-scanner.yml` | 326 | Stage 3 entry (T-5 URL + Model catalog) | Group A 3차 PoC 답습 |
| 4 | Stage 4 integration check tool | `tools/mvp1_pc3_ar1_integration_check.py` | 298 | Stage 4 cross-workflow 검증 (PC-3 + AR-1 통합) | Stage 4 합의 §1.3 답습 |
| 5 | Stage 4 PASS fixture | `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` | 30 | PC-3 + AR-1 정합 entry step 검증 | Stage 4 합의 §1.3 답습 |
| 6 | Stage 4 FAIL fixture (PC-3 violation) | `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` | 31 | PC-3 위반 (continue-on-error) 검증 | Stage 4 합의 §1.3 답습 |
| 7 | Stage 4 FAIL fixture (AR-1 violation) | `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` | 28 | AR-1 위반 (no fail-closed) 검증 | Stage 4 합의 §1.3 답습 |

**합산**: 7 artifacts × **1593줄 PoC 본문 답습**.

### 2.3 R-1 영역 = Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 채택

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-1 관계 |
|----------|------|----------------------|----------|
| S-1 | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | R-4 영역 (Phase α-1) — Stage 1 |
| ST-3 | docker secret (저장 경로 isolation) | ADR-008 차단조건 #6 + 부록 B 답습 | R-7 영역 (Phase α-3) — Stage 2 |
| **PC-3** | **CI-only enforcement (pre-commit)** | **T2 영역 답습 + 양 GP 공유 채택** | **R-1 본문 = PC-3 통합 (Stage 4 sub-step 4.1)** |
| **AR-1** | **CI step fail-closed (PR auto-reject)** | **T2 영역 답습 + 양 GP 공유 채택** | **R-1 본문 = AR-1 통합 (Stage 4 sub-step 4.2)** |
| T-2 + T-5 | provider scanner | Group A 1차+2차+3차 답습 | R-4 / R-5 영역 (Phase α-1 / α-2) |

본 brief 영역 = **R-1 PC-3 + AR-1 통합 한정** (Stage 4 sub-step 4.1 + 4.2). **PC-4 (sub-step 4.3) = Backlog #1+#2 분리 / AR-2 (sub-step 4.4) = Backlog #3 분리 / Stage 5 (G3-7) = Stage 4 후속 권고 답습** 분리.

### 2.4 R-1 영역 = Phase α-1 / α-2 / α-3 *완료 후* 의존 (Stage 4 합의 §1.2 답습)

| Phase | 영역 | 의존성 검증 |
|-------|------|----------|
| Phase α-1 R-4 | 도구 본문 (`tools/secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) | Phase α-4 = α-1 actual run PASS 선행 evidence 의존 (run_id `25728590939` + `25728590916` + `25728590977` 후속 — `72622409` 기준 — 답습 완료) |
| Phase α-2 R-5 | `.importlinter` config (`/.importlinter`) | Phase α-4 = α-2 actual run PASS 선행 evidence 의존 (run_id `25728590916` 內 import-linter step 후속 — 답습 완료) |
| Phase α-3 R-7 | docker secret block (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh`) | Phase α-4 = α-3 actual run PASS 선행 evidence 의존 (run_id `25731846625` 후속 — `6c6b208` 기준 — 답습 완료) |

**의존성 충족 상태**: Phase α-1 / α-2 / α-3 *actual run PASS 선행 evidence 답습 충족* (4 prerequisite runs 모두 SUCCESS) — Stage 4 합의 §1.1 답습. **Phase α-4 진입 적격성 의존성 검증 = 통과**.

### 2.5 R-1 본문 = Phase α-4 영역 *내* vs *외*

| 영역 | 본 brief 영역 *내* (진입 가능성 검토) | 본 brief 영역 *외* (실 진입 = Backlog #6 + 사용자 명시 결정 영역) |
|------|----------------------------|--------------------------------------|
| 3 MVP-1 workflow 본문 답습 검증 (1206줄) | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (step 추가/삭제/순서 변경) |
| Stage 4 integration check tool 본문 답습 (298줄) | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (검증 logic 변경) |
| Stage 4 integration fixture 본문 답습 (89줄, 3 파일) | ✅ enumerate 한정 (변경 0건) | 실 fixture 변경 / 추가 |
| sub-step 4.1 PC-3 CI step 통합 답습 | ✅ enumerate 한정 | 실 step 통합 변경 |
| sub-step 4.2 AR-1 fail-closed 통합 답습 | ✅ enumerate 한정 | 실 fail-closed logic 변경 |
| sub-step 4.3 PC-4 local pre-commit | ❌ (영역 외 — Backlog #1+#2 분리) | Backlog #1 + #2 1.5차 보강 영역 |
| sub-step 4.4 AR-2 branch protection | ❌ (영역 외 — Backlog #3 T3 분리) | Backlog #3 T3 영역 별도 풀 3+1 |
| 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC) | ❌ (영역 외 — 분리 명시) | 별도 영역 |
| Stage 5 (G3-7 4 항목) | ❌ (영역 외 — Stage 4 후속 권고 답습) | Stage 5 별도 합의 영역 |
| 의존성 매트릭스 정리 | ✅ 의존성 enumerate 한정 | — |
| 진입 적격성 5 조건 검토 | ✅ 검토 한정 | 실 진입 결정 = 사용자 명시 결정 영역 |

---

## 3. R-1 × Phase α-4 본문 작업 후보 분할 매트릭스

### 3.1 Phase α-4 R-1 sub-step 분할 (Stage 4 합의 §1.3 + backlog6-implementation-step-brief §2.2.4 답습)

| sub-step | 영역 | 답습 출처 | Phase α-4 진입 시 본 작업 후보 (본 brief 영역 외 — 실 진입 시점 결정) |
|---------|------|---------|---------------------------------------|
| 4.1 | PC-3 CI step 통합 답습 검증 | mvp1.md §4.3 + Stage 4 합의 §1.3 답습 | 답습 변경 0건 — PC-3 (`continue-on-error: false` + non-zero exit propagation + `if: always()` 패턴) 3 workflow 검증 답습 |
| 4.1.a | `secret-hygiene-egress-redaction.yml` PC-3 통합 검증 (694줄) | Group D 12 step + Stage 1+2+4 통합 답습 | 답습 변경 0건 — Stage 1 + Stage 2 + Stage 4 step 모두 PC-3 정합 |
| 4.1.b | `provider-adapter-enforcement.yml` PC-3 통합 검증 (186줄) | Group A 1차+2차 답습 | 답습 변경 0건 — T-2 import-linter + T-5 AST step PC-3 정합 |
| 4.1.c | `provider-url-scanner.yml` PC-3 통합 검증 (326줄) | Group A 3차 답습 | 답습 변경 0건 — T-5 URL + Model catalog step PC-3 정합 |
| 4.2 | AR-1 fail-closed 통합 답습 검증 | mvp1.md §4.4 + Stage 4 합의 §1.3 답습 | 답습 변경 0건 — AR-1 (`exit 1` propagation + `${{ failure() }}` 패턴) 3 workflow 검증 답습 |
| 4.2.a | Stage 4 integration check tool 답습 검증 (298줄) | Stage 4 합의 §1.3 답습 | 답습 변경 0건 — `--mode integration` + `--list-checks` self-check 답습 |
| 4.2.b | Stage 4 PASS fixture 답습 검증 | Stage 4 합의 §1.3 답습 | 답습 변경 0건 — `compliant_entry_step.yml` 30줄 답습 |
| 4.2.c | Stage 4 FAIL fixture 답습 검증 (PC-3 violation + AR-1 violation) | Stage 4 합의 §1.3 답습 | 답습 변경 0건 — `pc3_violation_continue_on_error.yml` 31줄 + `ar1_violation_no_fail_closed.yml` 28줄 답습 |
| 4.3 | PC-4 local pre-commit (영역 외) | Backlog #1 + #2 1.5차 보강 영역 분리 | 영역 외 (사용자 명시 7 금지 #5 답습) |
| 4.4 | AR-2 branch protection (영역 외) | Backlog #3 T3 영역 별도 풀 3+1 분리 | 영역 외 (사용자 명시 7 금지 #3 답습) |
| 4.5 | Stage 5 (G3-7) 후속 권고 (영역 외) | Stage 4 후속 권고 답습 | 영역 외 (별도 합의 영역) |
| 4.6 | ledger entry 형식 답습 — `event: pc3_ar1_integration_implementation` 후보 | mvp1.md §5.2 enum *후보 한정* 답습 | 정식 등록 0건 (Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 영역) |
| 4.7 | Evidence Artifact 형식 답습 (Markdown step summary + JSONL stub + actual run URL) | Layer B §1.8 (a) 답습 | 실 생성 = Layer C 시점 (본 brief 영역 외) |

### 3.2 합산 매트릭스

| Stage | 영역 | sub-step | 신규 작업 비율 (실 진입 시점) | PoC 답습 비율 | 본 brief 영역 |
|-------|------|---------|------------------------|------------|------------|
| Stage 4 (PC-3 + AR-1) | 7 artifacts (1593줄) | 7 sub-step (4.1 + 4.1.a + 4.1.b + 4.1.c + 4.2 + 4.2.a + 4.2.b + 4.2.c + 4.6 + 4.7) | 低 (Stage 4 합의 답습 변경 0건 + sub-step 4.1 + 4.2 cycle 완료 답습) | 高 (Stage 4 합의 + Group D + Group A PoC 답습) | enumerate 한정 |

### 3.3 Phase α-1 / α-2 / α-3 / α-4 분리 매트릭스

| 영역 | Phase α-1 R-4 (`1b3090b` 별도) | Phase α-2 R-5 (`6a79247` 별도) | Phase α-3 R-7 (`3f6306d` 별도) | Phase α-4 R-1 (본 brief) |
|------|------------------------|------------------------|---------------------|------------------|
| sub-수단 영역 | S-1 (R-4.1 Tier-1) + T-5 (custom AST) | T-2 (import-linter) | ST-3 (docker secret) | **PC-3 + AR-1 (CI step 통합)** |
| 검사 영역 | 코드 본문 secret + Direct/Dynamic/Model/URL 차단 | Transitive 정적 그래프 차단 | 저장 경로 secret isolation | **CI-only enforcement + fail-closed** |
| Stage | Stage 1 + Stage 3 | Stage 3 (T-2) | Stage 2 (단독) | **Stage 4 (sub-step 4.1 + 4.2)** |
| 본문 라인 수 | 829줄 (368 + 178 + 283) | 35줄 | 328줄 (9 artifacts) | **1593줄 (7 artifacts)** |
| 책무 | code-level Layer 1a + 1c | code-level Layer 1b | file-system Layer (R2-1) | **CI integration Layer (PC-3 + AR-1 통합)** |
| 의존성 | Phase α-2/α-3 ↔ 의존성 0 (병렬) | Phase α-1/α-3 ↔ 의존성 0 (병렬) | Phase α-1/α-2 ↔ 의존성 0 (병렬) | **α-1 + α-2 + α-3 *완료 후* 의존 (2순위)** |
| 진입 우선순위 | 1순위 (병렬) | 1순위 (병렬) | 1순위 (병렬) | **2순위** |

### 3.4 본 §3 의 *범위 한계*

본 §3 = **본문 작업 후보 *분할 매트릭스 정리 한정***. 실 sub-step 결정 / 실 R-1 본문 변경 = 사용자 명시 결정 영역 + Phase α-4 실 진입 시점 (Backlog #6 + 사용자 명시 결정 영역 — 본 brief 영역 외).

---

## 4. 사용자 명시 7 금지 영역 × R-1 본문 분리 매트릭스

### 4.1 금지 #1 — 실 R-1 CI workflow 수정 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `secret-hygiene-egress-redaction.yml` (694줄) 본문 변경 | ❌ (영역 외) | Phase α-4 실 진입 후 영역 |
| `provider-adapter-enforcement.yml` (186줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `provider-url-scanner.yml` (326줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `tests/fixtures/mvp1_pc3_ar1_integration/` (89줄, 3 파일) 변경 | ❌ (영역 외) | 동상 |
| 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC) 변경 | ❌ (영역 외) | 별도 영역 (`boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml`) |
| 신규 workflow 신설 | ❌ (영역 외) | 별도 합의 영역 |
| `pull_request_target` workflow 도입 | ❌ (영역 외) | T2/T3 별도 합의 영역 |
| **본 brief 영역 *내* 적격 작업** | **R-1 영역 *답습 출처 + 7 artifacts × 1593줄 enumerate 한정* + 7 sub-step 후보 enumerate** | — |

### 4.2 금지 #2 — CI workflow 신규 추가 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.github/workflows/*.yml` 신설 (3 MVP-1 외) | ❌ (영역 외) | 별도 합의 영역 |
| 기존 workflow 본문 변경 | ❌ (영역 외) | Phase α-4 실 진입 후 영역 |
| CI step `pre-commit run --all-files` 추가 | ❌ (영역 외) | R-2 영역 (Phase β-3, 금지 #5 해소 의존) |
| **본 brief 영역 *내* 적격 작업** | **Stage 4 integration step 답습 *enumerate 한정* (workflow 호환성 답습 — 실 변경 0건)** | — |

### 4.3 금지 #3 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| AR-2 형태 (e) CODEOWNERS + required check 실 활성화 | ❌ (영역 외) | sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 |
| direct push 차단 / force push 차단 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = CI workflow 영역 = AR-1 fail-closed 한정 / branch protection = AR-2 영역 분리 — Group α 합의 답습)** | — |

### 4.4 금지 #4 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/doctor.py` 신규 도구 본문 작성 | ❌ (영역 외) | R-10 영역 (Phase β-2) |
| dev 환경에서 CI 검증 의무 실행 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = CI workflow 영역 = CI-only enforcement 한정 / dev 환경 강제 = R-10 영역 분리)** | — |

### 4.5 금지 #5 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | sub-step 4.3 = Backlog #1 + #2 1.5차 보강 분리 (PC-4 local pre-commit) |
| `default_install_hook_types` 본문 결정 | ❌ (영역 외) | 동상 |
| `pre-commit install` opt-in → doctor → required 단계 진입 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **R-1 = PC-3 CI-only enforcement 한정 (sub-step 4.1) — PC-4 local pre-commit framework (sub-step 4.3) 분리 명시** | — |

### 4.6 금지 #6 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = 구현 영역, Layer E = 운영 영역 — 분리)** | — |

### 4.7 금지 #7 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = CI workflow 영역, Layer F = governance 영역 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **7 금지 영역 *분리 매트릭스 한정***. 7 금지 영역 어느 것도 *해소* 0건 + Phase α-4 실 진입 자동 진입 0건.

---

## 5. Phase α-4 진입 적격성 5 조건 검토

### 5.1 적격성 검토 매트릭스

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-α4-1** | **사용자 명시 7 금지 영역 충돌 0** | R-1 CI workflow 통합 = CI step 영역 — 금지 #3 (branch protection) / #4 (dev 환경 강제) / #6 (Layer E) / #7 (Layer F) 모두 직교 (충돌 0). 금지 #5 (pre-commit install 의무화) = sub-step 4.3 분리 명시 (영역 외). 금지 #1 (실 R-1 수정) / #2 (CI workflow 신규 추가) = Phase α-4 *실 진입* 시점 적용 — 본 brief = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α4-2** | **PoC 답습 변경 0** | R-1 영역 7 artifacts × 1593줄 답습 + Stage 4 합의 §1.3 4 sub-step 답습 + Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 + mvp1.md §4.3 + §4.4 답습 + 3 MVP-1 workflow + integration tool + integration fixture 답습 모두 변경 0건 | ✅ **답습 100% 보존** |
| **C-α4-3** | **의존성 충족 (Phase α-1 / α-2 / α-3 *완료 후* 의존)** | R-1 ↔ R-4 (Phase α-1) = actual run PASS 선행 evidence 의존 (run_id `25728590939` + `25728590916` + `25728590977` 후속 답습 — `72622409` 기준 — *충족 완료*) + R-1 ↔ R-5 (Phase α-2) = actual run PASS 선행 evidence 의존 (T-2 import-linter step `25728590916` 內 후속 — *충족 완료*) + R-1 ↔ R-7 (Phase α-3) = actual run PASS 선행 evidence 의존 (Stage 2 actual run `25731846625` 후속 — `6c6b208` 기준 — *충족 완료*). **4 prerequisite runs 모두 SUCCESS 답습 — 의존성 충족** | ✅ **의존성 충족 (2순위 적격)** |
| **C-α4-4** | **Provider Liquidity 5-way 100% 보존** | R-1 = CI integration Layer (PC-3 + AR-1 통합) — catalog / provider 영역과 직교 + CI workflow = vendor-agnostic 표준 (GitHub Actions) + provider key 사용 0건 (F-금지 #1 영구 답습) | ✅ **5/5 100% 보존** |
| **C-α4-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-1 = CI integration, Hermes PMO 영역 분리) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-1 = 수단, 목적 = CI-only enforcement + fail-closed) / T1/T2/T3 분리 보존 (R-1 = T2 영역 — PC-3 + AR-1 / AR-2 / Vault HSM = T3 영역 분리) / SPOF 의도적 수용 보존 (R-1 = enforcement single point 답습) | ✅ **5/5 보존** |

### 5.2 풀 3+1 승격 트리거 검토 (Backlog #6 우선 진입 합의 §7 + Phase α-1 R-4 합의 §5.2 + Phase α-2 R-5 합의 §5.2 + Phase α-3 R-7 합의 §5.2 + Stage 4 합의 §1.8 답습)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Phase α-2 C-γ-1 ~ C-γ-26 / Phase α-3 C-δ-1 ~ C-δ-28 / Stage 4 합의 어느 것의 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 2 | 본 brief 가 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 3 | 본 brief 가 Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 — CI workflow = vendor-agnostic 표준 (catalog / provider 영역과 직교) |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | ❌ 0건 — 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입 권고 | ❌ 0건 — T3 분리 명시 한정 (R-1 = T2 영역, AR-2 branch protection = sub-step 4.4 T3 분리) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 (Stage 4 합의 §1.8 #1 답습) | ❌ 0건 — F-금지 #1 영구 답습 + GitHub Actions secrets 사용 도입 0건 |
| 9 | 본 brief 가 Hermes upstream root of trust 변경 권고 (Stage 4 합의 §1.8 #2 답습) | ❌ 0건 — CI workflow = upstream 분리 영역 (ADR-011 §2.1 (b) 수단/목적 분리 답습) |
| 10 | 본 brief 가 PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 (Stage 4 합의 §1.8 #3 답습) | ❌ 0건 — PC-3 + AR-1 (sub-step 4.1 + 4.2 = T2 본 영역) / PC-4 (sub-step 4.3 = Backlog #1+#2) / AR-2 (sub-step 4.4 = Backlog #3) / AR-3 (Backlog #3) 경계 명확 |
| 11 | 본 brief 가 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | ❌ 0건 — 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC workflow 분리 명시) |
| 12 | 본 brief 가 신규 workflow 신설 / `pull_request_target` 도입 권고 | ❌ 0건 — 신설 / `pull_request_target` 도입 0건 답습 |
| 13 | 본 brief 가 Stage 5 (G3-7 4 항목) 자동 진입 권고 | ❌ 0건 — Stage 4 후속 권고 답습 (Stage 5 별도 합의 분리) |
| 14 | 본 brief 가 Phase α-1 / α-2 / α-3 actual run 재실행 권고 | ❌ 0건 — 4 prerequisite runs PASS 선행 evidence 답습 한정 (재실행 0건) |

**검토 결과**: **14/14 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 확정** (사용자 명시 결정 시).

### 5.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| 5 조건 (C-α4-1 ~ C-α4-5) | **5/5 충족** |
| 14 풀 3+1 트리거 | **0/14 발화** |
| Phase α-1 / α-2 / α-3 *완료 후* 의존 (의존성 충족) | **4 prerequisite runs PASS — 충족 완료** |
| **Phase α-4 진입 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.4 본 §5 의 *범위 한계*

본 §5 = **진입 적격성 *검토 한정***. 실 Phase α-4 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 적격 판정 = 적격성 권위 권고 한정 — 실 진입 발효 권위 0건.

---

## 6. Rollback Trigger 의존성 답습

### 6.1 R-1 영역에 영향 받는 18 Rollback Trigger 답습 (Layer B §1.7 + mvp1.md §3.5 + §4.6 답습)

본 §은 **18 Rollback Trigger 中 R-1 CI workflow 통합 영역 *영향* 받는 trigger enumerate 한정** — 발화 0건 + 본 brief 영역 *내 의존성 정리 한정*:

| Trigger | 발화 조건 | R-1 영향 | 본 brief 영역 |
|--------|---------|-----------|------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | 영향 0 (R-4 영역) | 영역 외 (Phase α-1) |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 | 영향 0 | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | 영향 0 (R-7 영역) | 영역 외 (Phase α-3) |
| **R-MVP1-G3-4** | **PC-3 CI runtime 폭증 (>2분)** | **R-1 영역 *직접* 영향 (3 MVP-1 workflow 실행 시간)** | 의존성 *enumerate 한정* (발화 0건 — 4 prerequisite runs PASS 답습) |
| **R-MVP1-G3-5** | **AR-1 hook 우회 시도 패턴 검출** | **R-1 영역 *직접* 영향 (Stage 4 integration check 검출)** | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | 영향 0 (R-4 영역) | 영역 외 (Backlog #3 별도 합의) |
| R-MVP1-G3-7 | Tier-2 확장 필요 | 영향 0 (R-4 영역) | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 | R-1 영역 *간접* 영향 (Hermes runtime parity) | 영역 외 (Layer E, 금지 #6 답습) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | 영향 0 (R-5 영역) | 영역 외 (Phase α-2) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | 영향 0 (R-4 영역) | 영역 외 (Phase α-1) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 불일치) | 영향 0 | 영역 외 (Phase α-1 + α-2) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | 영향 0 (R-5 영역) | 영역 외 (Phase α-2) |
| **R-MVP1-G5-5** | **PC-3 hook 우회 시도** | **R-1 영역 *직접* 영향 (Stage 4 integration check 검출)** | 의존성 *enumerate 한정* (발화 0건) |
| **R-MVP1-G5-6** | **AR-1 fail-closed 폭증** | **R-1 영역 *직접* 영향 (Stage 4 integration check 검출)** | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 | 영향 0 | 영역 외 (Backlog #4) |
| R-MVP1-G5-8 | branch protection 필요 trigger | 영향 0 (T3 영역 — AR-2 sub-step 4.4) | 영역 외 (금지 #3 답습) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 | 영향 0 (MVP-3 영역) | 영역 외 |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 | 영향 0 (MVP-3/4 영역) | 영역 외 |

### 6.2 PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger (4개) — 분리 명시

| 영역 | 진입 trigger | 본 brief 영역 |
|------|----------|------------|
| PC-4 local pre-commit framework | sub-step 4.3 = Backlog #1 + #2 1.5차 보강 영역 (dev 환경 영향 정책 = T3) | 영역 외 (금지 #5 답습) |
| AR-2 branch protection rule | sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 | 영역 외 (금지 #3 답습) |
| AR-3 자동 revert bot | Backlog #3 T3 영역 분리 | 영역 외 (Group α 합의 답습) |
| Stage 5 (G3-7 4 항목) | Stage 4 후속 권고 답습 (G3-7 (i) workflow 검증 / (ii) secrets.* 참조 감지 / (iv) fork PR secret 차단 default / (v) permissions: contents: read 강제) | 영역 외 (별도 합의 영역) |

### 6.3 합산

| 영역 | trigger 수 | 본 brief 영역 |
|------|---------|------------|
| **R-1 본문 영역 *직접* 영향 (Layer B 18 trigger)** | 4 (G3-4, G3-5, G5-5, G5-6) | 의존성 *enumerate 한정* — 발화 0건 |
| R-1 영역 *간접* 영향 (Layer E 영역) | 1 (G3-8) | 영역 외 (금지 #6 답습) |
| R-1 영역 *영향 0* (R-4/R-5/R-7/T3/MVP-3/MVP-6/Backlog 분리) | 13 | 영역 외 |
| **추가: PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger** | **4** | **영역 외 (Backlog #1+#2 1.5차 보강 / Backlog #3 / Stage 5 별도 합의)** |

### 6.4 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger + PC-4/AR-2/AR-3/Stage 5 별도 backlog trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* (CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지) + 신규 trigger 추가 0건.

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | **실 R-1 CI workflow 수정** (사용자 명시 7 금지 #1) | 0건 |
| 2 | **CI workflow 신규 추가** (사용자 명시 7 금지 #2) | 0건 |
| 3 | **branch protection 변경** (사용자 명시 7 금지 #3) | 0건 |
| 4 | **dev 환경 강제** (사용자 명시 7 금지 #4) | 0건 |
| 5 | **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5) | 0건 |
| 6 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6) | 0건 |
| 7 | **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7) | 0건 |
| 8 | 실 hook 구현 (`.git/hooks/pre-commit` 본문 / `.pre-commit-config.yaml` 본문 변경 / sub-step 4.3 PC-4) | 0건 |
| 9 | sub-step 4.4 AR-2 branch protection rule 진입 | 0건 |
| 10 | AR-3 자동 revert bot 도입 | 0건 |
| 11 | 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC) 흡수 | 0건 |
| 12 | 신규 workflow 신설 / `pull_request_target` workflow 도입 | 0건 |
| 13 | R-4 도구 본문 변경 (`tools/*.py`) | 0건 |
| 14 | R-5 `.importlinter` 본문 변경 | 0건 |
| 15 | R-7 docker secret block 본문 변경 | 0건 |
| 16 | Phase α-1 / α-2 / α-3 자동 진입 | 0건 |
| 17 | Phase β / γ 자동 진입 | 0건 |
| 18 | Implementation Evidence PASS (Layer C) 발효 | 0건 |
| 19 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 20 | R-1 영역 7 artifacts × 1593줄 본문 어느 줄도 변경 (`secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`) | 0건 |
| 21 | Stage 5 (G3-7 4 항목) 자동 진입 | 0건 |
| 22 | Phase α-1 / α-2 / α-3 actual run 자동 재실행 | 0건 |
| 23 | PC-3 + AR-1 = PC-4 / AR-2 / AR-3 / Stage 5 흡수 시도 | 0건 |
| 24 | GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습) | 0건 |
| 25 | `pull_request_target` workflow 도입 | 0건 |
| 26 | Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 | 0건 |
| 27 | Stage 4 합의 §1.3 4 sub-step 분할안 변경 | 0건 |
| 28 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 29 | threshold *고정* (CI runtime / PR check pass rate / fail-closed rate 등 = 후보 한정) | 0건 |
| 30 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 31 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) 자동 변경 | 0건 |
| 32 | Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경 | 0건 |
| 33 | Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경 | 0건 |
| 34 | Phase α-3 합의 28 조건 (C-δ-1 ~ C-δ-28) 자동 변경 | 0건 |
| 35 | Stage 4 합의 본문 변경 | 0건 |
| 36 | Group α 14 결정 영역 *재결정* | 0건 |
| 37 | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / Phase α-3 합의 / Stage 4 합의 본문 변경 | 0건 |
| 38 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 39 | Group I (Hermes-originated commit auto-reject) 자동 진입 | 0건 |
| 40 | token rotation 정책 자동 결정 | 0건 |
| 41 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 42 | commit signing 도입 | 0건 |
| 43 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 44 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 45 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 46 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 47 | git commit / push | 0건 |
| 48 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습 — 응답 = 입력 한정) | 0건 |
| 49 | 외부 LLM 응답 결론 강제 채택 (Group α 합의 C-11 답습) | 0건 |
| 50 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 51 | 인간 리뷰 의무 자동 발화 | 0건 |
| 52 | 실 GitHub API / branch protection API 자동 호출 (본 brief = 영역 정의 검토 한정) | 0건 |
| 53 | Backlog #1 / #2 / #4 / #5 / #7 자동 진입 | 0건 |
| 54 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 55 | MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 56 | Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리) | 0건 |
| 57 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |
| 58 | event enum 정식 등록 (`pc3_ar1_integration_implementation` = Backlog #5 분리) | 0건 |

### 7.2 본 brief 발효 *후* Phase α-4 실 진입 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Phase α-4 진입 시 PC-3 + AR-1 외 sub-수단 도입 (PC-4 / AR-2 / AR-3) | Backlog #1+#2 1.5차 보강 / Backlog #3 영역 분리 |
| 2 | Phase α-4 진입 시 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC) 흡수 | 별도 영역 분리 |
| 3 | Phase α-4 진입 시 신규 workflow 신설 / `pull_request_target` workflow 도입 | 별도 합의 영역 + T2/T3 분리 |
| 4 | Phase α-4 진입 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의 trigger) |
| 5 | Phase α-4 진입 시 GitHub Actions secrets 사용 도입 | 영구 금지 (F-금지 #1 G3-7 (i) 답습) |
| 6 | Phase α-4 진입 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 7 | Phase α-4 진입 시 event enum 정식 등록 (`event: pc3_ar1_integration_implementation`) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 8 | Phase α-4 진입 시 Stage 5 (G3-7 4 항목) 자동 진입 | Stage 4 후속 권고 답습 한정 (별도 합의 영역) |
| 9 | Phase α-4 진입 시 Phase α-1 / α-2 / α-3 actual run 자동 재실행 | 4 prerequisite runs PASS 선행 evidence 답습 한정 (재실행 0건) |
| 10 | Phase α-4 진입 시 local pre-commit framework 활성화 | sub-step 4.3 = Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 7 금지 #5 답습) |
| 11 | Phase α-4 진입 시 branch protection rule 활성화 | sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 (사용자 명시 7 금지 #3 답습) |
| 12 | Phase α-4 진입 시 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 13 | Phase α-4 진입 시 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 14 | Phase α-4 진입 시 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 15 | Phase α-4 진입 시 F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 16 | Phase α-4 진입 시 Layer C 자동 발효 (사용자 명시 결정 미충족 시) | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |
| 17 | Phase α-4 진입 시 Phase α-1 / α-2 / α-3 자동 재진입 | Phase α 단계 = 사용자 명시 결정 영역 + Backlog #6 실 진입 영역 |
| 18 | Phase α-4 진입 시 Group I (Hermes-originated commit auto-reject) 자동 진입 | Group α 합의 C-2 답습 (Group I 별도 합의 영역) |
| 19 | Phase α-4 진입 시 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |
| 20 | Phase α-4 진입 시 GitHub plan / ruleset 가용성 자동 확인 | Group α 합의 C-4 답습 |
| 21 | Phase α-4 진입 시 Stage 4 합의 본문 변경 / sub-step 분할 변경 | Stage 4 합의 답습 보존 |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 Phase α-4 실 진입 단계에서 위 21 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격** | Backlog #6 우선 진입 합의 + Phase α-1 / α-2 / α-3 합의 + Stage 4 합의 답습 한정 + 7 금지 영역 *재결정* 0건 + 본 brief = 진입 가능성 *검토 한정* (적격성 *해소* 0건) + 14/14 풀 3+1 트리거 0건 발화 (§5.2) |
| Phase α-4 실 진입 시 합의 | **별도 합의 — Reviewer-only 단축 또는 풀 3+1** | Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 + Phase α-4 = 7 금지 충돌 0 영역 한정 (사용자 명시 결정 영역) |
| Layer C 발효 합의 | **별도 합의 — 단축 또는 풀 3+1 + 외부 LLM 1+** | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

§5.2 답습 — **14/14 트리거 0건 발화** 확정.

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` 패턴 답습) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α 4 단계 (α-1 + α-2 + α-3 + α-4) 통합 진입 brief 작성** | Phase α 통합 진입 brief (병렬 + 2순위 진입 적격 답습, 사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Phase α-4 실 진입 brief 작성** (DRAFT — 실 R-1 CI workflow 운영 단계 분할안) | Phase α-4 실 진입 step 분할 brief (사용자 명시 결정 영역) |
| (F) | 본 brief 승인 → **Phase α-1 ~ α-4 통합 실 진입 계획 brief 작성** | Phase α-1 ~ α-4 통합 실제 구현 계획 brief |
| (G) | 본 brief 승인 → **Layer C 발효 합의 진입 brief 작성** (Implementation Evidence PASS 발효 준비) | Layer C 발효 합의 brief (ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역) |
| (H) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (I) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (J) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α 4 단계 통합 진입 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Phase α-4 실 진입 step 분할 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Phase α-1 ~ α-4 통합 실 진입 계획 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Layer C 발효 합의 brief 작성."
- (H): "옵션 (H) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (I): "옵션 (I) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — "Phase α-4 R-1 CI workflow 통합 진입 brief를 작성해주세요") |
| 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 패턴 답습 — #1 = R-1 영역 한정) | ✅ (7/7 — 실 R-1 CI workflow 수정 0건 / CI workflow 신규 추가 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Backlog #6 우선 진입 합의 §6.1 2순위 + §5.2 α-4 답습 | ✅ (Phase α-4 = R-1 CI workflow 통합 — 진입 가능성 *검토 한정*, 적격성 *해소* 0건) |
| Phase α-1 합의 (`1b3090b`) 답습 | ✅ (Phase α-1 R-4 합의 본문 변경 0건 + C-β-1 ~ C-β-15 자동 변경 0건) |
| Phase α-2 합의 (`6a79247`) 답습 | ✅ (Phase α-2 R-5 합의 본문 변경 0건 + C-γ-1 ~ C-γ-26 자동 변경 0건) |
| Phase α-3 합의 (`3f6306d`) 답습 | ✅ (Phase α-3 R-7 합의 본문 변경 0건 + C-δ-1 ~ C-δ-28 자동 변경 0건) |
| Stage 4 합의 답습 | ✅ (Stage 4 §1.3 4 sub-step 답습 + §1.8 5 트리거 0건 발화 답습) |
| Group α 합의 C-1 ~ C-12 답습 | ✅ (자동 해소 0건 + 자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Layer A / Layer B / §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 | ✅ (발화 0건 — §6 답습) |
| Group α 7 단계 승격 Trigger 답습 | ✅ (발화 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (R-1 = CI integration Layer (PC-3 + AR-1 통합) = catalog / provider 영역과 직교, CI workflow = vendor-agnostic 표준) |
| **Phase α-1 / α-2 / α-3 *완료 후* 의존성 충족** | ✅ **4 prerequisite runs PASS 선행 evidence 답습** (run_id `25728590939` + `25728590916` + `25728590977` + `25731846625` 후속) |
| PC-3 + AR-1 양 GP 공유 답습 (PC-4 / AR-2 / AR-3 분리) | ✅ (sub-step 4.1 + 4.2 = T2 본 영역 / sub-step 4.3 + 4.4 = Backlog #1+#2 / Backlog #3 T3 분리) |
| 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC workflow 분리) | ✅ 분리 명시 |
| Stage 5 (G3-7) 분리 명시 (Stage 4 후속 권고 답습) | ✅ 분리 명시 |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/14 발화 | ✅ (§5.2 답습) |
| Phase α-4 진입 적격성 5/5 충족 | ✅ (§5.1 답습 — C-α4-1 ~ C-α4-5) |
| R-1 영역 7 artifacts × 1593줄 본문 어느 줄도 변경 0건 | ✅ (PoC 답습 변경 0건) |
| Hermes upstream Dockerfile / `pull_request_target` workflow / GitHub Actions secrets 사용 도입 0건 | ✅ (영구 금지 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #6 Runtime + CI-hook 우선 진입 합의 (`c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) §5.2 α-4 답습 후속**, 합의 §6.1 **2순위** (Phase α-1 + α-2 + α-3 1순위 완료 후 의존) 中 **Phase α-4 = R-1 CI workflow 통합 영역 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 R-1 CI workflow 수정 / CI workflow 신규 추가 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) Phase α-1 / α-2 / α-3 패턴 답습 (사용자 명시 enumerate 0건 — 본 brief = 패턴 보존 + 사용자 검토 시 prohibition 추가/축소 권위 영역). **R-1 = CI workflow 통합 본문 정의** (7 artifacts × **1593줄 답습** — `secret-hygiene-egress-redaction.yml` 694줄 (Stage 1 entry + Stage 2 entry + Stage 4 integration) + `provider-adapter-enforcement.yml` 186줄 (Stage 3 entry T-2+T-5) + `provider-url-scanner.yml` 326줄 (Stage 3 entry T-5 URL+Model) + `tools/mvp1_pc3_ar1_integration_check.py` 298줄 (Stage 4 cross-workflow 검증 도구) + `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` 30줄 (Stage 4 PASS fixture) + `fail/pc3_violation_continue_on_error.yml` 31줄 (PC-3 위반 fixture) + `fail/ar1_violation_no_fail_closed.yml` 28줄 (AR-1 위반 fixture) — 본문 변경 0건) + **PC-3 + AR-1 양 GP 공유 답습 채택** (Layer B §5.5.1 + §5.5.2) + **Stage 4 합의 답습** (sub-step 4.1 PC-3 CI step 통합 / 4.2 AR-1 fail-closed 통합 / 4.3 PC-4 local pre-commit = Backlog #1+#2 분리 / 4.4 AR-2 branch protection = Backlog #3 분리) + **3 MVP-1 workflow 한정 답습** (G2/G3/G4 PoC workflow 8개 분리 명시) + **Stage 5 분리** (Stage 4 후속 권고 답습) + **7 sub-step Phase α-4 본문 작업 후보 분할 매트릭스** + **7 금지 영역 × R-1 분리 매트릭스** (7/7 분리 — 충돌 0) + **Phase α-4 진입 적격성 5 조건 검토** (C-α4-1 7 금지 충돌 0/7 + C-α4-2 PoC 답습 100% 보존 + C-α4-3 **Phase α-1 / α-2 / α-3 *완료 후* 의존성 충족** (4 prerequisite runs PASS 선행 evidence 답습 — `25728590939` + `25728590916` + `25728590977` + `25731846625` 후속) + C-α4-4 Provider Liquidity 5-way 100% 보존 (CI workflow = vendor-agnostic 표준) + C-α4-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **14 풀 3+1 승격 트리거 0/14 발화** + **R-1 영역 영향 Rollback Trigger 의존성 답습** (18 trigger 中 R-1 직접 영향 4 + 간접 영향 1 + 영향 0 13 — 발화 0건 + PC-4/AR-2/AR-3/Stage 5 별도 backlog 4 trigger 분리) + **본 brief 자체 금지 58 + Phase α-4 실 진입 단계 금지 21** + **합의 형태 권고** (Reviewer-only 단축 — 14/14 트리거 0건 발화) 를 정리한다. **본 brief 는 Phase α-4 실 진입을 *시작* 시키지 않으며, R-1 영역 7 artifacts × 1593줄 어느 줄도 *변경* 하지 않으며, 3 MVP-1 workflow 외 workflow / Hermes upstream Dockerfile / `pull_request_target` workflow / GitHub Actions secrets 사용 도입 / R-4 도구 / R-5 `.importlinter` / R-7 docker secret block / 7 금지 영역 *해소* / Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / Backlog #6 우선 진입 합의 본문 변경 / Phase α-1 / α-2 / α-3 합의 본문 변경 / Stage 4 합의 본문 변경 / Layer B §5.5.1 + §5.5.2 본문 변경 / PC-3 + AR-1 = PC-4 / AR-2 / AR-3 / Stage 5 흡수 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / Phase α-1 / α-2 / α-3 자동 진입 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습).

---

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~J, §9 답습)
**금지 (사용자 명시 패턴 답습 — 본 brief 영역)**:
- ❌ **실 R-1 CI workflow 수정** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 신규 추가** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ R-1 영역 7 artifacts × 1593줄 본문 어느 줄도 변경 (`.github/workflows/secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`)
- ❌ 3 MVP-1 workflow 외 workflow (G2/G3/G4 PoC) 흡수
- ❌ 신규 workflow 신설 / `pull_request_target` workflow 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ R-4 도구 본문 변경 (`tools/*.py`)
- ❌ R-5 `.importlinter` 본문 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ Phase α-4 실 진입 자동 진입 금지
- ❌ Phase α-1 / α-2 / α-3 자동 재진입 금지
- ❌ Phase α-1 / α-2 / α-3 actual run 자동 재실행 금지
- ❌ Phase β / γ 자동 진입 금지
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ PC-3 + AR-1 = PC-4 (sub-step 4.3 = Backlog #1+#2 분리) / AR-2 (sub-step 4.4 = Backlog #3 분리) / AR-3 / Stage 5 흡수 시도
- ❌ Stage 5 (G3-7 4 항목) 자동 진입
- ❌ Hermes upstream Dockerfile 변경
- ❌ Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경
- ❌ Stage 4 합의 §1.3 4 sub-step 분할안 변경
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) 자동 변경
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경
- ❌ Phase α-3 합의 28 조건 (C-δ-1 ~ C-δ-28) 자동 변경
- ❌ Stage 4 합의 본문 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / Phase α-3 합의 / Stage 4 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
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
