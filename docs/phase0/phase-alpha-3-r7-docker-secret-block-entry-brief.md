# Phase α-3 R-7 docker secret block 진입 Brief (준비안 — DRAFT)

> **본 문서는 Backlog #6 Runtime + CI-hook 우선 진입 합의 (`docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md`, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) §6.1 1순위 §5.2 α-3 답습 후속, Phase α 4 단계 中 α-3 (R-7 docker secret block) *진입 가능성 검토* 한정 의 brief 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Phase α-3 실 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / GP-3 Stage 2 합의 / 사용자 명시 7 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF)
- `docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (commit `233892b`)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF)
- `docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md` (commit `e7cdb21`)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF)
- `docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md` (commit `608a046`)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (GP-3 MVP-1 진입 합의 — ST-3 단독 채택 권위 권고, commit `6dc5bdc`)
- `docs/review/3plus1-consensus-2026-05-12-gp3-stage2-implementation-entry.md` (**GP-3 Stage 2 (ST-3 docker secret) 단독 구현 진입 합의 APPROVE — sub-step 2.1 ~ 2.4 4 cycle**)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.2 (`docker_secret_isolation_check` + `container_restart_recovery`) + §5.3 (ST-3 MVP-1 1차 단독 — Hermes upstream 변경 회피) + §5.5.1 ST-3 본문 채택 (commit `55c5b4b`)
- ADR-008 차단조건 #6 + 부록 B (file system secret isolation — docker secret) + §A.2 R1-2 (저장 경로 isolation)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역 (CI step Entry)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-3 R-7 docker secret block 진입 brief를 작성해주세요."

### 0.2 사용자 명시 7 금지 답습 (Phase α-1 / α-2 패턴 답습)

사용자가 본 brief 진입 명령 시 명시 prohibitions 를 enumerate 하지 않았으나, **Backlog #6 우선 진입 합의 §6.1 1순위 답습 + Phase α-1 (`1b3090b`) + Phase α-2 (`6a79247`) 답습 패턴** = 7 금지 영역 유지 (사용자 명시 강조 답습) — 본 brief = 본 패턴 답습 (제 #1 = R-7 영역 한정):

1. ❌ **실 R-7 docker secret block 수정 금지** — `docker/gp3-st3-poc/` 본문 변경 / `tools/docker_secret_image_layer_check.sh` 본문 변경 / `tools/docker_secret_restart_recovery.sh` 본문 변경 / `tests/fixtures/gp3_st3/` 본문 변경 모두 0건
2. ❌ **CI workflow 변경 금지** — `.github/workflows/secret-hygiene-egress-redaction.yml` Stage 2 step 본문 변경 / 신설 / 삭제 모두 0건
3. ❌ **branch protection 변경 금지**
4. ❌ **dev 환경 강제 금지**
5. ❌ **`pre-commit install` 의무화 금지**
6. ❌ **Operational Readiness PASS (Layer E) 선언 금지**
7. ❌ **Hermes PMO 격상 (Layer F) 금지**

본 7 금지 답습 = 사용자 명시 패턴 보존 — 사용자가 본 brief 검토 시 prohibition 추가/축소 권위 영역 (옵션 (B) 수정 요청 답습).

### 0.3 본 brief 가 *하는* 것

1. Backlog #6 우선 진입 합의 §6.1 1순위 + §5.2 α-3 답습 — Phase α-3 = R-7 docker secret block 영역 *진입 가능성 검토 한정* (§1)
2. **R-7 영역 = docker secret block (Stage 2) 본문 정의** + 현 상태 enumeration (§2)
3. **R-7 × Phase α-3 본문 작업 후보 분할 매트릭스** — 4 sub-step (2.1 docker-compose secret block + 2.2 image layer 검증 + 2.3 container restart recovery + 2.4 CI Stage 2 entry step) (§3)
4. **사용자 명시 7 금지 영역 × R-7 본문 분리 매트릭스** (§4)
5. **Phase α-3 진입 적격성 5 조건 검토** (7 금지 충돌 0 + PoC 답습 변경 0 + 의존성 + Provider Liquidity 보존 + 풀 3+1 트리거 미발화, §5)
6. **Rollback Trigger 의존성 답습** — R-7 영역에 영향 받는 trigger enumerate (§6)
7. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 7 금지 영역**:

- ❌ **실 R-7 docker secret block 수정 (0건)** — `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` (34줄) / `Dockerfile` (12줄) / `app.py` (46줄) / `secrets/api_key.placeholder` (1줄) / `tools/docker_secret_image_layer_check.sh` (99줄) / `tools/docker_secret_restart_recovery.sh` (118줄) / `tests/fixtures/gp3_st3/{pass,fail}/` (18줄) 본문 변경 0건 — **합산 328줄 PoC 답습 변경 0건**
- ❌ **CI workflow 변경 (0건)** — `secret-hygiene-egress-redaction.yml` Stage 2 step 본문 변경 / 신설 / 삭제 0건
- ❌ **branch protection 변경 (0건)** — AR-2 (CODEOWNERS + required status check) / direct push 차단 / force push 차단 / admin bypass OFF / required PR review count / linear history / deployments 모두 변경 0건 (Group α 합의 5.1 #6 답습)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `docker-compose up` 의무 실행 모두 0건
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 / `default_install_hook_types` 본문 결정 모두 0건 (Group α 합의 5.2 #9 답습)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 / `.pre-commit-config.yaml` 본문 변경 0건
- ❌ **Production `docker-compose.yml` 변경 (0건)** — PoC 격리 디렉토리 (`docker/gp3-st3-poc/`) 한정 — production docker-compose 변경 0건 보존
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 차단조건 #6 + 부록 B 답습 = upstream 변경 회피 (Backlog #1 1.5차 보강 ST-1 entrypoint stat / ST-2 inotify sidecar 분리 영역)
- ❌ **R-4 도구 본문 변경 (0건)** — Phase α-1 R-4 영역 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 본문 변경 모두 0건 (Phase α-1 = 별도 영역, `1b3090b` 합의 답습)
- ❌ **R-5 `.importlinter` 본문 변경 (0건)** — Phase α-2 영역 분리 (`6a79247` 합의 답습)
- ❌ **R-1 CI workflow 통합 (0건)** — Phase α-4 영역 분리
- ❌ **Phase α-1 / α-2 / α-4 자동 진입 (0건)** — 본 brief = Phase α-3 *진입 가능성 검토 한정*
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM / Layer E / Layer F 모두 영역 외
- ❌ **Implementation Evidence PASS (Layer C) 발효 (0건)** + **MVP-1 PASS (Layer D) 선언 (0건)**
- ❌ **docker secret 룰 *재설계* (0건)** — GP-3 Stage 2 합의 답습 한정 (4 sub-step 답습)
- ❌ **ST-3 = ST-1 / ST-2 / ST-5 흡수 시도 (0건)** — ST-3 단독 답습 (MVP-1 1차 ST-3 단독 답습 + ST-1 entrypoint stat = Backlog #1 1.5차 보강 / ST-2 inotify sidecar = Backlog #1 분리 / ST-5 Defense in depth = MVP-2 이후)
- ❌ **ST-4 Vault HSM 진입 (0건)** — Backlog #7 영역 분리
- ❌ **`inotify` sidecar 본 영역 흡수 (0건)** — `tools/docker_secret_inotify_sidecar_check.sh` (258줄) = Backlog #1 1.5차 보강 ST-2 영역 (본 brief 영역 외)
- ❌ **실 secret material commit (0건)** — `secrets/api_key.placeholder` = FAKE_TEST_SECRET marker 답습 (Group D F-금지 #1 marker 정책 답습)
- ❌ **`secrets/` 디렉토리 `.gitignore` 변경 (0건)** — placeholder 한정 (실 secret commit 금지 영구 답습)
- ❌ **`secret-hygiene-egress-redaction.yml` F-금지 grep step 본문 변경 (0건)** — Stage 2 fixture scope 답습 (Group D §1.7-N1 답습)
- ❌ **threshold *고정* (0건)** — FP / FN / image layer leak count / restart recovery rate 모두 *후보 한정* 유지
- ❌ **Group α 14 결정 영역 *재결정* (0건)**
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / GP-3 진입 합의 / GP-3 Stage 2 합의 본문 변경 (0건)**
- ❌ **§5.5.1 GP-3 4 sub-수단 본문 채택 변경 (0건)** — S-1 + ST-3 + PC-3 + AR-1 답습 한정
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)**
- ❌ **R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) trigger 자동 발화 (0건)**
- ❌ **G3-7 row 4 항목 자동 흡수 (0건)** — Stage 5 별도 영역 분리
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)**
- ❌ **commit signing 도입 (0건)** — MVP-6 영역 답습
- ❌ **`pull_request_target` workflow 도입 (0건)**
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **git commit / push (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)** — `secrets/api_key.placeholder` = FAKE marker 답습 보존
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **실 docker build / docker run / docker history 실행 자동 진입 (0건)** — 본 brief = 영역 정의 검토 한정 (실 actual run = Phase α-3 실 진입 시점)
- ❌ **Layer 2 runtime block (G5-5) 진입 (0건)** — MVP-3/4 영역 분리

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-3 실 진입을 *시작* 시키지 않으며,
- (ii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / GP-3 Stage 2 합의 의 어느 조건도 *해소* 시키지 않으며,
- (iii) 사용자 명시 7 금지 영역 어느 것도 진입시키지 않으며,
- (iv) Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / GP-3 진입 합의 / GP-3 Stage 2 합의 본문을 *변경* 하지 않으며,
- (v) R-7 영역 본문 (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/`) 어느 줄도 *변경* 하지 않으며 (현 9 artifacts × 328줄 답습),
- (vi) `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 어느 줄도 *변경* 하지 않으며,
- (vii) Hermes upstream Dockerfile / Production `docker-compose.yml` / `secrets/` 디렉토리 어느 줄도 *변경* 하지 않으며,
- (viii) R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) trigger 어느 것도 *발화* 시키지 않으며,
- (ix) Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-3 R-7 docker secret block 영역의 *진입 가능성 검토* — 본문 정의 + Phase α-3 본문 작업 후보 분할 매트릭스 + 7 금지 분리 매트릭스 + 진입 적격성 5 조건 검토 + Rollback Trigger 의존성 + 금지 영역 enumeration + 합의 형태 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Backlog #6 우선 진입 합의 §5.2 α-3 답습 (`c7ddfdd`)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의, 7/7 풀 3+1 트리거 0건 발화) |
| 합의 단위 | Backlog #6 우선 진입 brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| Phase α 4 단계 | α-1 (R-4) / α-2 (R-5) / α-3 (R-7) / α-4 (R-1) |
| Phase α-3 정의 (합의 §5.2 답습) | **R-7 docker secret block (Stage 2) — α-1 / α-2 와 *독립 진입 적격*** |
| 진입 우선순위 (합의 §6.1) | **1순위** — Phase α-1 + α-2 + α-3 병렬 진입 적격 |
| 진입 결정 권위 | **Backlog #6 실 진입 + 사용자 명시 결정 영역** (본 합의 영역 외) |

### 1.2 GP-3 Stage 2 합의 답습 (`3plus1-consensus-2026-05-12-gp3-stage2-implementation-entry.md`)

본 brief 는 GP-3 Stage 2 합의 *발효 후속* — Stage 2 (ST-3 docker secret) 단독 구현 진입 합의 (APPROVE, Reviewer-only 단축 — 5/5 트리거 0건 발화) 답습 한정:

| 합의 영역 | 답습 |
|---------|----|
| 합의 판정 | APPROVE — Stage 2 (ST-3) 단독 구현 진입 READY |
| 합의 형태 | Reviewer-only 단축 합의 (5/5 트리거 0건 발화 확정) |
| 발효 시점 | 2026-05-12 후속 13 (Stage 1 + Stage 3 actual run PASS 후속 — `7262240` 기준) |
| 4 sub-step 분할 | 2.1 docker-compose secret block / 2.2 image layer 검증 / 2.3 container restart recovery / 2.4 CI Stage 2 entry step + Evidence |
| 본문 채택 | ST-3 = Hermes upstream 변경 0건 보존 (ADR-008 차단조건 #6 + 부록 B 답습) |
| 발효 영역 | Stage 2 *구현 진입 적격성* 한정 — Implementation Evidence PASS 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 모두 영역 외 |

**본 brief 관계**: GP-3 Stage 2 합의는 *Stage 단위* 진입 적격성 권위 권고 (Layer B 흡수 영역). 본 brief = Phase α-3 = **Backlog #6 우선 진입 합의의 4 Phase 분할 中 1순위 1단계** *진입 가능성 검토 한정* (별도 framing — Layer A/B → Backlog #6 우선 진입 → Phase α 4단계 framing).

### 1.3 Backlog #6 우선 진입 합의 §6.2 권고 한계 답습

> 본 합의 = **Phase α 우선 진입 *권위 권고 발행 한정***
> 실 Phase α 진입 = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
> 자동 진입 0건

본 brief 의 의미:

- (a) Backlog #6 우선 진입 합의 발효 *자체* = 완료 (`c7ddfdd`)
- (b) Phase α-1 R-4 brief = 완료 (`e7cdb21` + `1b3090b` APPROVE AS BRIEF)
- (c) Phase α-2 R-5 brief = 완료 (`608a046` + `6a79247` APPROVE AS BRIEF)
- (d) Phase α-3 R-7 docker secret block *실 진입* = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
- (e) 본 brief = (d) *진입 가능성 검토 한정* — 실 진입 *직전* 의사결정 사전 정비 영역
- (f) 본 brief = Backlog #6 우선 진입 합의의 7 금지 영역 *해소* 가 아님 + Phase α-1 / α-2 합의 *해소* 도 아님 + GP-3 Stage 2 합의 *재결정* 도 아님

### 1.4 6-Layer 분리 매트릭스 현 상태 (2026-05-15 후속)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + §5.5 `55c5b4b`) | 답습 한정 (ST-3 §5.5.1 본문 채택 답습) |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 | ✅ APPROVE WITH CONDITIONS (`4880e88`) | 답습 한정 |
| Backlog #6 우선 진입 | Runtime + CI-hook 영역 정의 + Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) | 답습 한정 |
| Phase α-1 R-4 도구 본문 진입 | R-4 (S-1 + T-2 + T-5) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`1b3090b`) | 답습 한정 (15 조건 C-β-1 ~ C-β-15 해소 0건) |
| Phase α-2 R-5 `.importlinter` 본문 진입 | R-5 (T-2 import-linter) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`6a79247`) | 답습 한정 (26 조건 C-γ-1 ~ C-γ-26 해소 0건) |
| GP-3 Stage 2 단독 구현 진입 | Stage 2 (ST-3) 4 sub-step 진입 적격성 | ✅ APPROVE (Reviewer-only) | **본 brief = R-7 docker secret block *Phase α-3 framing 진입 가능성 검토*** |
| Phase α-3 R-7 진입 | **본 brief 영역** | ⏳ DRAFT (본 brief = 준비안) | **본 brief = §6.1 1순위 *진입 가능성 검토*** |
| Layer C | Implementation Evidence PASS 발효 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #6) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #7) |

### 1.5 본 brief 의 진입점

```
Layer A APPROVE (f1e0b23) ─────────────────────────────────────────┐
Layer B APPROVE (f40423f)                                          │
§5.5 9 sub-수단 (55c5b4b) — GP-3 §5.5.1 (S-1 + ST-3 + PC-3 + AR-1) │
Group α APPROVE (4880e88) ─────────────────────────────────────────┤
GP-3 MVP-1 진입 합의 (6dc5bdc) — ST-3 단독 채택 권위 권고
GP-3 Stage 2 합의 (Reviewer-only APPROVE) — sub-step 2.1 ~ 2.4 발효
Stage 2 actual run PASS (run_id 25728590939 secret-hygiene 答 GP-3 Stage 2 entry steps)
backlog6 priority brief (233892b)                                  │
Backlog #6 우선 진입 합의 (c7ddfdd) APPROVE AS BRIEF                │
Phase α-1 R-4 brief (e7cdb21) + 합의 (1b3090b) APPROVE AS BRIEF
Phase α-2 R-5 brief (608a046) + 합의 (6a79247) APPROVE AS BRIEF
   │
   ▼
■ 본 brief = Phase α-3 R-7 docker secret block *진입 가능성 검토* (DRAFT)    ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-3 실 진입 (R-7 docker secret block 운영 진입)                       ← 본 brief 영역 외
   │
   ▼ (R-4 + R-5 + R-7 + R-1 완료 + actual run SUCCESS + evidence 5/5 후)
Layer C 발효 합의 — Implementation Evidence PASS                            ← 본 brief 영역 외
```

---

## 2. R-7 영역 정의 (Phase α-3 한정)

### 2.1 R-7 = docker secret block 영역 정의 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5.1 + GP-3 Stage 2 합의 답습)

| 영역 | 답습 출처 | 현 상태 (2026-05-15 기준) |
|------|---------|----------------------|
| 책무 (ST-3 영역) | GP-3 저장 경로 secret 검출 (G3-1) — file system secret isolation | Layer B §5.5.1 ST-3 본문 채택 답습 |
| 도구 | docker-compose secret block + image layer 검증 + container restart recovery | GP-3 Stage 2 합의 4 sub-step 답습 |
| 권위 | ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 | upstream 변경 회피 답습 |
| 책무 분리 (ST-3 단독) | Vault HSM ST-4 미진입 (Backlog #7) / entrypoint stat ST-1 / inotify sidecar ST-2 미진입 (Backlog #1 1.5차 보강) / ST-5 Defense in depth (MVP-2 이후) | GP-3 진입 합의 답습 (ST-3 단독 채택) |

### 2.2 R-7 본문 9 artifacts 답습 (현 라인 수 — 실 본문 변경 0건, enumerate 한정)

| # | 산출물 | 경로 | 현 라인 수 | sub-step | 답습 출처 |
|---|--------|------|---------|---------|---------|
| 1 | docker-compose secret block | `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` | 34 | 2.1 | ADR-008 차단조건 #6 + 부록 B + mvp1.md §3.4.2 + §5.3 답습 |
| 2 | Dockerfile (PoC) | `docker/gp3-st3-poc/Dockerfile` | 12 | 2.1 | PoC 격리 영역 한정 |
| 3 | 응용 (secret read) | `docker/gp3-st3-poc/app.py` | 46 | 2.1 | PoC 격리 영역 한정 |
| 4 | placeholder secret material | `docker/gp3-st3-poc/secrets/api_key.placeholder` | 1 | 2.1 | FAKE_TEST_SECRET marker 답습 (Group D F-금지 #1) |
| 5 | image layer 검증 도구 | `tools/docker_secret_image_layer_check.sh` | 99 | 2.2 | mvp1.md §3.4.2 `docker_secret_isolation_check` (0건 leak 강제) 답습 |
| 6 | container restart recovery 도구 | `tools/docker_secret_restart_recovery.sh` | 118 | 2.3 | mvp1.md §3.4.2 `container_restart_recovery` (100% 강제) 답습 |
| 7 | PASS fixture (Dockerfile) | `tests/fixtures/gp3_st3/pass/Dockerfile` | 9 | 2.2 | 정상 secret 분리 검증 fixture |
| 8 | FAIL fixture (Dockerfile) | `tests/fixtures/gp3_st3/fail/Dockerfile` | 8 | 2.2 | baked secret 위반 검증 fixture |
| 9 | FAIL fixture (secret material) | `tests/fixtures/gp3_st3/fail/baked_secret.txt` | 1 | 2.2 | FAKE_TEST_SECRET marker 답습 |

**합산**: 9 artifacts × 328줄 PoC 본문 답습.

### 2.3 R-7 영역 = Layer B §5.5.1 GP-3 4 sub-수단 中 ST-3 답습

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-7 관계 | 본 brief 영역 |
|----------|------|----------------------|----------|------------|
| S-1 | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | R-4 영역 (Phase α-1) — Stage 1 | 영역 외 (별도 Phase) |
| **ST-3** | **docker secret (저장 경로 isolation)** | **ADR-008 차단조건 #6 + 부록 B 답습 + Layer A §1.2 + Layer B §1.1 답습** | **R-7 본문 = ST-3 본문 (Stage 2)** | **본 brief 영역 내** |
| PC-3 | CI-only enforcement (pre-commit) | T2 영역 답습 | Stage 4 영역 (양 GP 공유 — PC-4 T3 분리) | 영역 외 (별도 Stage) |
| AR-1 | CI step fail-closed (PR auto-reject) | T2 영역 답습 | Stage 4 영역 (양 GP 공유 — AR-2 T3 분리) | 영역 외 (별도 Stage) |

본 brief 영역 = **R-7 ST-3 한정** (Stage 2). **S-1 (R-4) = Phase α-1 영역 / PC-3 + AR-1 (Stage 4) = Phase α-4 또는 별도 영역 분리** 답습.

### 2.4 R-7 영역 = ST 5 후보 中 ST-3 단독 답습 (MVP-1 1차 답습 — mvp1.md §5.3)

| ST 후보 | 영역 | 본 brief 영역 |
|--------|------|------------|
| ST-1 | entrypoint stat (시작 시점) | 영역 외 (Backlog #1 1.5차 보강 + Hermes upstream 변경 필요) |
| ST-2 | inotify sidecar (런타임 지속, mtime/perm 변경 → 컨테이너 정지) | 영역 외 (Backlog #1 분리 — `tools/docker_secret_inotify_sidecar_check.sh` 258줄 존재) |
| **ST-3** | **docker secret (저장 경로 isolation)** | **본 brief 영역 내** (MVP-1 1차 답습) |
| ST-4 | Vault HSM (외부 키 관리) | 영역 외 (Backlog #7 분리 + MVP-6 이후) |
| ST-5 | ST-1 + ST-2 + ST-3 통합 (Defense in depth) | 영역 외 (MVP-2 이후) |

본 brief = **ST-3 단독 답습 한정** (MVP-1 1차 — Hermes upstream 변경 회피 보존).

### 2.5 R-7 본문 = Phase α-3 영역 *내* vs *외*

| 영역 | 본 brief 영역 *내* (진입 가능성 검토) | 본 brief 영역 *외* (실 진입 = Backlog #6 + 사용자 명시 결정 영역) |
|------|----------------------------|--------------------------------------|
| docker-compose secret block 본문 답습 검증 | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (production docker-compose 도입 / secret 정의 추가 / mode 변경) |
| Dockerfile (PoC) + app.py + placeholder 답습 | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (응용 코드 통합) |
| `tools/docker_secret_image_layer_check.sh` 답습 (99줄) | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (검증 logic 변경 / threshold 변경) |
| `tools/docker_secret_restart_recovery.sh` 답습 (118줄) | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (recovery logic 변경) |
| `tests/fixtures/gp3_st3/{pass,fail}/` 답습 | ✅ enumerate 한정 (변경 0건) | 실 fixture 변경 / 추가 |
| `secret-hygiene-egress-redaction.yml` Stage 2 entry step 답습 | ✅ enumerate 한정 (R-1 영역 = Phase α-4 영역 외) | 실 workflow 본문 변경 (R-1 영역) |
| ST-3 단독 답습 (ST-1/2/4/5 분리) | ✅ enumerate 한정 | 실 ST-1/2/4/5 진입 (별도 backlog 영역) |
| 의존성 매트릭스 정리 | ✅ 의존성 enumerate 한정 | — |
| 진입 적격성 5 조건 검토 | ✅ 검토 한정 | 실 진입 결정 = 사용자 명시 결정 영역 |

---

## 3. R-7 × Phase α-3 본문 작업 후보 분할 매트릭스

### 3.1 Phase α-3 R-7 sub-step 분할 (GP-3 Stage 2 합의 §1.3 + mvp1.md §3.4.2 + §5.3 답습)

| sub-step | 영역 | 답습 출처 | Phase α-3 진입 시 본 작업 후보 (본 brief 영역 외 — 실 진입 시점 결정) |
|---------|------|---------|---------------------------------------|
| 2.1 | docker-compose secret block 본문 답습 검증 (34줄) | ADR-008 차단조건 #6 + 부록 B + mvp1.md §3.4.2 답습 | 답습 변경 0건 — `secrets:` block + `file:` source + mode 0400 + cap_drop ALL + read_only + tmpfs noexec/nosuid + no-new-privileges + network_mode none + user 1000:1000 답습 검증 |
| 2.1.a | Dockerfile (12줄) + app.py (46줄) + placeholder (1줄) 답습 검증 | PoC 격리 영역 답습 | 답습 변경 0건 — PoC 격리 디렉토리 (`docker/gp3-st3-poc/`) 한정 |
| 2.1.b | `secrets/.gitignore` 답습 검증 (placeholder 한정) | F-금지 #1 marker 답습 | 답습 검증 한정 — 실 secret commit 금지 영구 답습 |
| 2.2 | image layer 검증 도구 답습 (99줄) | mvp1.md §3.4.2 `docker_secret_isolation_check` (0건 leak 강제) | 답습 변경 0건 — docker build → docker history / docker save tar → secret material grep → 0 leak 강제 답습 검증 |
| 2.2.a | PASS / FAIL fixture (Dockerfile) 답습 검증 | Stage 2 합의 §1.3 답습 | 답습 변경 0건 — PASS = 정상 secret 분리 / FAIL = baked secret 위반 답습 |
| 2.3 | container restart recovery 도구 답습 (118줄) | mvp1.md §3.4.2 `container_restart_recovery` (100% 강제) | 답습 변경 0건 — compose up → secret 마운트 확인 → restart → 재주입 100% 답습 검증 |
| 2.4 | CI Stage 2 entry step 답습 (R-1 영역) | Stage 2 합의 §1.3 답습 | 답습 검증 한정 — 실 workflow 변경은 R-1 영역 (Phase α-4) — `summary.json` 필드 (`stage2_image_layer`, `stage2_restart_recovery`, `mvp1_entry_ledger_event_candidate`, `mvp1_entry_evidence_form`) 답습 |
| 2.4.a | ledger entry 형식 답습 — `event: docker_secret_isolation_layer1_implementation` 후보 | mvp1.md §5.2 enum *후보 한정* 답습 | 정식 등록 0건 (Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 영역) |
| 2.4.b | Evidence Artifact 형식 답습 (Markdown step summary + JSONL stub + actual run URL) | Layer B §1.8 (a) 답습 | 실 생성 = Layer C 시점 (본 brief 영역 외) |

### 3.2 합산 매트릭스

| Stage | 도구 | sub-step | 신규 작업 비율 (실 진입 시점) | PoC 답습 비율 | 본 brief 영역 |
|-------|------|---------|------------------------|------------|------------|
| Stage 2 (ST-3) | 9 artifacts (328줄) | 9 sub-step (2.1 + 2.1.a + 2.1.b + 2.2 + 2.2.a + 2.3 + 2.4 + 2.4.a + 2.4.b) | 低 (GP-3 Stage 2 합의 답습 변경 0건 + 4 cycle commit 완료 답습) | 高 (GP-3 Stage 2 합의 + ADR-008 차단조건 #6 + 부록 B 답습) | enumerate 한정 |

### 3.3 Phase α-1 / α-2 / α-3 분리 매트릭스

| 영역 | Phase α-1 R-4 (`1b3090b` 별도) | Phase α-2 R-5 (`6a79247` 별도) | Phase α-3 R-7 (본 brief) |
|------|------------------------|------------------------|---------------------|
| sub-수단 영역 | S-1 (R-4.1 Tier-1) + T-5 (custom AST) | T-2 (import-linter) | **ST-3 (docker secret)** |
| 검사 영역 | 코드 본문 secret + Direct/Dynamic/Model/URL 차단 | Transitive 정적 그래프 차단 | **저장 경로 secret isolation** |
| Stage | Stage 1 + Stage 3 | Stage 3 (T-2) | **Stage 2 (단독)** |
| 본문 라인 수 | 829줄 (368 + 178 + 283) | 35줄 | **328줄 (9 artifacts)** |
| 책무 | code-level Layer 1a + 1c | code-level Layer 1b | **file-system Layer (R2-1)** |
| 동시 진입 적격성 | Phase α-1 + α-2 + α-3 병렬 진입 적격 (§6.1 답습) | 동상 | 동상 (Stage 2 합의 §1.2 답습 — 0 의존성) |
| Hermes upstream 변경 | 0건 | 0건 | **0건 (ADR-008 차단조건 #6 + 부록 B 답습)** |

### 3.4 본 §3 의 *범위 한계*

본 §3 = **본문 작업 후보 *분할 매트릭스 정리 한정***. 실 sub-step 결정 / 실 R-7 본문 변경 = 사용자 명시 결정 영역 + Phase α-3 실 진입 시점 (Backlog #6 + 사용자 명시 결정 영역 — 본 brief 영역 외).

---

## 4. 사용자 명시 7 금지 영역 × R-7 본문 분리 매트릭스

### 4.1 금지 #1 — 실 R-7 docker secret block 수정 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` 본문 변경 | ❌ (영역 외) | Phase α-3 실 진입 후 영역 |
| `docker/gp3-st3-poc/Dockerfile` + `app.py` 변경 | ❌ (영역 외) | 동상 |
| `docker/gp3-st3-poc/secrets/api_key.placeholder` 변경 | ❌ (영역 외) | 영구 금지 (실 secret commit 금지) |
| `tools/docker_secret_image_layer_check.sh` 본문 변경 | ❌ (영역 외) | Phase α-3 실 진입 후 영역 |
| `tools/docker_secret_restart_recovery.sh` 본문 변경 | ❌ (영역 외) | 동상 |
| `tests/fixtures/gp3_st3/{pass,fail}/` 변경 | ❌ (영역 외) | 동상 |
| Production `docker-compose.yml` 신설 / 변경 | ❌ (영역 외) | 별도 합의 영역 (PoC 격리 디렉토리 한정 답습) |
| Hermes upstream Dockerfile 변경 | ❌ (영역 외) | Backlog #1 1.5차 보강 영역 (ST-1 / ST-2 / ST-5) |
| **본 brief 영역 *내* 적격 작업** | **R-7 영역 *답습 출처 + 9 artifacts × 328줄 enumerate 한정* + 9 sub-step 후보 enumerate** | — |

### 4.2 금지 #2 — CI workflow 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 변경 | ❌ (영역 외) | Phase α-4 영역 (R-1) |
| 새 CI workflow 신설 (`.github/workflows/docker-secret-*.yml`) | ❌ (영역 외) | 동상 |
| CI step `pre-commit run --all-files` 추가 | ❌ (영역 외) | R-2 영역 (Phase β-3, 금지 #5 해소 의존) |
| **본 brief 영역 *내* 적격 작업** | **Stage 2 entry step 답습 *enumerate 한정* (workflow 호환성 답습 — 실 변경 0건)** | — |

### 4.3 금지 #3 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| AR-2 형태 (e) CODEOWNERS + required check 실 활성화 | ❌ (영역 외) | Group α 합의 발효 후 Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| direct push 차단 / force push 차단 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-7 = file-system 격리 영역, branch protection = GitHub Web UI 영역 — 직교)** | — |

### 4.4 금지 #4 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/doctor.py` 신규 도구 본문 작성 | ❌ (영역 외) | R-10 영역 (Phase β-2) |
| dev 환경에서 `docker-compose up gp3-st3-poc` 의무 실행 | ❌ (영역 외) | 동상 (dev 환경 강제 = R-10 의존) |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-7 = file-system 격리 영역, R-10 = doctor 영역 — 분리)** | — |

### 4.5 금지 #5 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | R-6 영역 (Phase β-1) |
| `.pre-commit-config.yaml` 에 docker secret hook 등록 | ❌ (영역 외) | 동상 |
| `pre-commit install` opt-in → doctor → required 단계 진입 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **R-7 hook framework 호환성 답습 *enumerate 한정* (실 hook 등록 0건)** | — |

### 4.6 금지 #6 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| ST-4 Vault HSM 진입 | ❌ (영역 외) | Backlog #7 분리 (MVP-6) |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-7 = 구현 영역, Layer E = 운영 영역 — 분리)** | — |

### 4.7 금지 #7 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-7 = file-system 격리 영역, Layer F = governance 영역 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **7 금지 영역 *분리 매트릭스 한정***. 7 금지 영역 어느 것도 *해소* 0건 + Phase α-3 실 진입 자동 진입 0건.

---

## 5. Phase α-3 진입 적격성 5 조건 검토

### 5.1 적격성 검토 매트릭스

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-α3-1** | **사용자 명시 7 금지 영역 충돌 0** | R-7 docker secret block = file-system 격리 영역 — 금지 #3 (branch protection) / #4 (dev 환경 강제) / #5 (pre-commit install 의무화) / #6 (Layer E) / #7 (Layer F) 모두 직교 (충돌 0). 금지 #1 (실 R-7 수정) / #2 (CI workflow 변경) = Phase α-3 *실 진입* 시점 적용 — 본 brief = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α3-2** | **PoC 답습 변경 0** | R-7 영역 9 artifacts × 328줄 답습 + GP-3 Stage 2 합의 §1.3 4 sub-step 답습 + ADR-008 차단조건 #6 + 부록 B 답습 + ST-3 단독 채택 답습 + Layer B §5.5.1 ST-3 본문 채택 답습 모두 변경 0건 | ✅ **답습 100% 보존** |
| **C-α3-3** | **의존성 0 (Phase α-1 / α-2 / α-3 병렬 진입 적격)** | R-7 ↔ R-4 = 영역 분리 (S-1 코드 본문 vs ST-3 저장 경로 — 의존 0, Stage 2 합의 §1.2 답습) + R-7 ↔ R-5 = 영역 분리 (provider import vs file-system isolation — 의존 0) + R-7 ↔ R-1 = Phase α-4 영역 (본 brief 영역 외) + Stage 2 actual run PASS 검증 답습 (run_id `25728590939` 후속) — 의존성 해소됨 | ✅ **의존성 0 (병렬 진입 적격)** |
| **C-α3-4** | **Provider Liquidity 5-way 100% 보존** | R-7 = file-system secret isolation Layer (R2-1) — catalog / provider 영역과 직교 + docker secret = vendor-agnostic 표준 (Docker BuildKit / Docker Compose) + secret material = placeholder 답습 (실 vendor SDK 무관) | ✅ **5/5 100% 보존** |
| **C-α3-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-7 = file-system isolation, Hermes PMO 영역 분리 + Hermes upstream 변경 0건) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-7 = 수단, 목적 = 저장 경로 secret isolation) / T1/T2/T3 분리 보존 (R-7 = T2 영역, ST-4 Vault HSM = T3 영역 분리) / SPOF 의도적 수용 보존 (R-7 = enforcement single point 답습) | ✅ **5/5 보존** |

### 5.2 풀 3+1 승격 트리거 검토 (Backlog #6 우선 진입 합의 §7 + Phase α-1 R-4 합의 §5.2 + Phase α-2 R-5 합의 §5.2 + GP-3 Stage 2 합의 §1.8 답습)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Phase α-2 C-γ-1 ~ C-γ-26 / GP-3 Stage 2 합의 어느 것의 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 2 | 본 brief 가 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 3 | 본 brief 가 Layer B §5.5.1 GP-3 4 sub-수단 (S-1 + ST-3 + PC-3 + AR-1) *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 (ST-3 영역 한정) |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 — docker secret = vendor-agnostic 표준 (catalog / provider 영역과 직교) |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | ❌ 0건 — 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입 권고 | ❌ 0건 — T3 분리 명시 한정 (R-7 = T2 영역, ST-4 Vault HSM = T3 영역 분리) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 (GP-3 Stage 2 §1.8 #1 답습) | ❌ 0건 — ADR-008 차단조건 #6 + 부록 B 답습 변경 0건 + Hermes upstream 변경 0건 |
| 9 | 본 brief 가 Hermes upstream root of trust 변경 권고 (GP-3 Stage 2 §1.8 #2 답습) | ❌ 0건 — docker secret = upstream 분리 영역 (ADR-011 §2.1 (b) 수단/목적 분리 답습) |
| 10 | 본 brief 가 Docker secret / local config / CI secret 경계 불명확 (GP-3 Stage 2 §1.8 #3 답습) | ❌ 0건 — ST-3 (Docker secret) + S-1 (local config + 코드 본문 secret) + G3-7 (CI secret — Stage 5 분리) 경계 명확 |
| 11 | 본 brief 가 ST-3 = ST-1/2/4/5 흡수 시도 권고 | ❌ 0건 — ST-3 단독 답습 한정 (mvp1.md §5.3 답습) |
| 12 | 본 brief 가 실 secret material commit / `secrets/.gitignore` 변경 권고 | ❌ 0건 — placeholder 한정 영구 답습 (F-금지 #1 marker 답습) |

**검토 결과**: **12/12 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 확정** (사용자 명시 결정 시).

### 5.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| 5 조건 (C-α3-1 ~ C-α3-5) | **5/5 충족** |
| 12 풀 3+1 트리거 | **0/12 발화** |
| **Phase α-3 진입 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.4 본 §5 의 *범위 한계*

본 §5 = **진입 적격성 *검토 한정***. 실 Phase α-3 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 적격 판정 = 적격성 권위 권고 한정 — 실 진입 발효 권위 0건.

---

## 6. Rollback Trigger 의존성 답습

### 6.1 R-7 영역에 영향 받는 18 Rollback Trigger 답습 (Layer B §1.7 + mvp1.md §3.5 + §4.6 답습)

본 §은 **18 Rollback Trigger 中 R-7 docker secret block 영역 *영향* 받는 trigger enumerate 한정** — 발화 0건 + 본 brief 영역 *내 의존성 정리 한정*:

| Trigger | 발화 조건 | R-7 영향 | 본 brief 영역 |
|--------|---------|-----------|------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | 영향 0 (R-4 영역) | 영역 외 (Phase α-1) |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 | 영향 0 | 영역 외 (Backlog #1 1.5차 보강) |
| **R-MVP1-G3-3** | **ST-3 Docker secret 도입 실패** | **`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` 본문 영향** | 의존성 *enumerate 한정* (발화 0건 — Stage 2 actual run PASS 답습) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | image layer 검증 + restart recovery 실행 시간 *간접* 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | 영향 0 (T3 영역) | 영역 외 (Backlog #3) |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | 영향 0 (R-4 영역) | 영역 외 (Backlog #3 별도 합의) |
| R-MVP1-G3-7 | Tier-2 확장 필요 | 영향 0 (R-4 영역) | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 | **R-7 영역 *간접* 영향 (Hermes runtime parity)** | 영역 외 (Layer E, 금지 #6 답습) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | 영향 0 (R-5 영역) | 영역 외 (Phase α-2) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | 영향 0 (R-4 영역) | 영역 외 (Phase α-1) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 불일치) | 영향 0 | 영역 외 (Phase α-1 + α-2) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | 영향 0 (R-5 영역) | 영역 외 (Phase α-2) |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | 영향 0 (T3 영역) | 영역 외 (Backlog #3) |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 | 영향 0 | 영역 외 (Stage 4 + R-1 영역) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 | 영향 0 | 영역 외 (Backlog #4) |
| R-MVP1-G5-8 | branch protection 필요 trigger | 영향 0 (T3 영역) | 영역 외 (금지 #3 답습) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 | 영향 0 (MVP-3 영역) | 영역 외 |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 | 영향 0 (MVP-3/4 영역) | 영역 외 |

### 6.2 ST-3 = ST-1 / ST-2 / ST-4 / ST-5 답습 (별도 backlog trigger)

본 §은 **MVP-1 1차 = ST-3 단독 답습** 한정 — ST-1 / ST-2 / ST-4 / ST-5 진입 trigger = 별도 backlog 영역 (본 brief 영역 외):

| ST 후보 | 진입 trigger | 본 brief 영역 |
|--------|----------|------------|
| ST-1 | entrypoint stat 검증 필요 (시작 시점) — Hermes upstream Dockerfile 변경 의존 | 영역 외 (Backlog #1 1.5차 보강, 풀 3+1 합의 trigger) |
| ST-2 | inotify sidecar 운영 필요 (런타임 지속) — `tools/docker_secret_inotify_sidecar_check.sh` 258줄 존재 | 영역 외 (Backlog #1 분리) |
| ST-4 | Vault HSM 외부 키 관리 필요 | 영역 외 (Backlog #7 분리, MVP-6 이후) |
| ST-5 | Defense in depth (ST-1 + ST-2 + ST-3 통합) 필요 | 영역 외 (MVP-2 이후) |

### 6.3 합산

| 영역 | trigger 수 | 본 brief 영역 |
|------|---------|------------|
| **R-7 본문 영역 *직접* 영향 (Layer B 18 trigger)** | 2 (G3-3, G3-4) | 의존성 *enumerate 한정* — 발화 0건 |
| R-7 영역 *간접* 영향 (Layer E 영역) | 1 (G3-8) | 영역 외 (금지 #6 답습) |
| R-7 영역 *영향 0* (R-4/R-5/R-1/T3/MVP-3/MVP-6/Backlog 분리) | 15 | 영역 외 |
| **추가: ST-1/2/4/5 별도 backlog trigger** | **4** | **영역 외 (Backlog #1 1.5차 보강 / Backlog #7 / MVP-2 이후)** |

### 6.4 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger + ST 별도 backlog trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* (image layer leak count = 0건 / restart recovery rate = 100% / 모두 *후보 한정* 유지) + 신규 trigger 추가 0건.

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | **실 R-7 docker secret block 수정** (사용자 명시 7 금지 #1) | 0건 |
| 2 | **CI workflow 변경** (사용자 명시 7 금지 #2) | 0건 |
| 3 | **branch protection 변경** (사용자 명시 7 금지 #3) | 0건 |
| 4 | **dev 환경 강제** (사용자 명시 7 금지 #4) | 0건 |
| 5 | **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5) | 0건 |
| 6 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6) | 0건 |
| 7 | **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7) | 0건 |
| 8 | 실 hook 구현 (`.git/hooks/pre-commit` 본문 / `.pre-commit-config.yaml` 본문 변경) | 0건 |
| 9 | Production `docker-compose.yml` 신설 / 변경 (PoC 격리 디렉토리 한정 답습) | 0건 |
| 10 | Hermes upstream Dockerfile 변경 (ADR-008 차단조건 #6 + 부록 B 답습 보존) | 0건 |
| 11 | R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 변경 | 0건 |
| 12 | R-5 `.importlinter` 본문 변경 | 0건 |
| 13 | R-1 CI workflow 통합 (`.github/workflows/*.yml` 신설/변경) | 0건 |
| 14 | Phase α-1 / α-2 / α-4 자동 진입 | 0건 |
| 15 | Phase β / γ 자동 진입 | 0건 |
| 16 | Implementation Evidence PASS (Layer C) 발효 | 0건 |
| 17 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 18 | R-7 영역 9 artifacts × 328줄 본문 어느 줄도 변경 (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/`) | 0건 |
| 19 | ST-3 = ST-1 / ST-2 / ST-4 / ST-5 흡수 시도 (단독 답습) | 0건 |
| 20 | ST-4 Vault HSM 진입 (Backlog #7 분리) | 0건 |
| 21 | `inotify` sidecar (`tools/docker_secret_inotify_sidecar_check.sh` 258줄) 본 영역 흡수 (Backlog #1 ST-2 분리) | 0건 |
| 22 | 실 secret material commit (`secrets/api_key.placeholder` placeholder 답습) | 0건 |
| 23 | `secrets/` 디렉토리 `.gitignore` 변경 (placeholder 한정 영구 답습) | 0건 |
| 24 | `secret-hygiene-egress-redaction.yml` F-금지 grep step 본문 변경 | 0건 |
| 25 | `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 변경 (R-1 영역 = Phase α-4) | 0건 |
| 26 | G3-7 row 4 항목 자동 흡수 (Stage 5 별도 영역 분리) | 0건 |
| 27 | R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) trigger 자동 발화 | 0건 |
| 28 | Layer B §5.5.1 GP-3 4 sub-수단 본문 채택 변경 | 0건 |
| 29 | GP-3 Stage 2 합의 §1.3 4 sub-step 분할안 변경 | 0건 |
| 30 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 31 | threshold *고정* (image layer leak 0 / restart recovery 100% / latency 등 = 후보 한정) | 0건 |
| 32 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 33 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) 자동 변경 | 0건 |
| 34 | Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경 | 0건 |
| 35 | Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경 | 0건 |
| 36 | GP-3 Stage 2 합의 본문 변경 | 0건 |
| 37 | GP-3 MVP-1 진입 합의 (`6dc5bdc`) 본문 변경 | 0건 |
| 38 | Group α 14 결정 영역 *재결정* | 0건 |
| 39 | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 본문 변경 | 0건 |
| 40 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 41 | Group I (Hermes-originated commit auto-reject) 자동 진입 | 0건 |
| 42 | token rotation 정책 자동 결정 | 0건 |
| 43 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 44 | commit signing 도입 | 0건 |
| 45 | `pull_request_target` workflow 도입 | 0건 |
| 46 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 47 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 48 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 49 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 50 | git commit / push | 0건 |
| 51 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습 — 응답 = 입력 한정) | 0건 |
| 52 | 외부 LLM 응답 결론 강제 채택 (Group α 합의 C-11 답습) | 0건 |
| 53 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 54 | 인간 리뷰 의무 자동 발화 | 0건 |
| 55 | 실 docker build / docker run / docker history 자동 실행 (본 brief = 영역 정의 검토 한정) | 0건 |
| 56 | Backlog #1 / #2 / #4 / #5 / #7 자동 진입 | 0건 |
| 57 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 58 | MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 59 | Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리) | 0건 |
| 60 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |

### 7.2 본 brief 발효 *후* Phase α-3 실 진입 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Phase α-3 진입 시 ST-3 외 수단 도입 (ST-1 entrypoint stat / ST-2 inotify sidecar / ST-4 Vault HSM / ST-5 Defense in depth) | Backlog #1 1.5차 보강 / Backlog #7 / MVP-2 이후 영역 분리 |
| 2 | Phase α-3 진입 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의 trigger — ST-1 / ST-5 진입 시 의무) |
| 3 | Phase α-3 진입 시 Production `docker-compose.yml` 신설 / 변경 | PoC 격리 디렉토리 (`docker/gp3-st3-poc/`) 한정 답습 (별도 합의 영역) |
| 4 | Phase α-3 진입 시 실 secret material commit | 영구 금지 (`secrets/api_key.placeholder` = FAKE_TEST_SECRET marker 답습) |
| 5 | Phase α-3 진입 시 `.gitignore` 변경 (placeholder 한정 보존) | 영구 금지 (실 secret commit 금지 영구 답습) |
| 6 | Phase α-3 진입 시 secret material marker 위반 (실 vendor prefix 사용) | 영구 금지 (Group D §1.7-N1 답습 — `FAKE_TEST_SECRET_*` prefix 한정) |
| 7 | Phase α-3 진입 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 8 | Phase α-3 진입 시 event enum 정식 등록 (`event: docker_secret_isolation_layer1_implementation`) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 9 | Phase α-3 진입 시 `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 10 | Phase α-3 진입 시 local pre-commit framework 활성화 | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 7 금지 #5 답습) |
| 11 | Phase α-3 진입 시 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 12 | Phase α-3 진입 시 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 13 | Phase α-3 진입 시 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 14 | Phase α-3 진입 시 F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 15 | Phase α-3 진입 시 Layer C 자동 발효 (사용자 명시 결정 미충족 시) | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |
| 16 | Phase α-3 진입 시 Phase α-1 / α-2 / α-4 자동 진입 | Phase α 단계 = 사용자 명시 결정 영역 + Backlog #6 실 진입 영역 |
| 17 | Phase α-3 진입 시 Group I (Hermes-originated commit auto-reject) 자동 진입 | Group α 합의 C-2 답습 (Group I 별도 합의 영역) |
| 18 | Phase α-3 진입 시 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |
| 19 | Phase α-3 진입 시 ST-4 Vault HSM 진입 | Backlog #7 분리 (MVP-6 이후) |
| 20 | Phase α-3 진입 시 `inotify` sidecar (ST-2) 진입 | Backlog #1 1.5차 보강 분리 |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 Phase α-3 실 진입 단계에서 위 20 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격** | Backlog #6 우선 진입 합의 + Phase α-1 합의 + Phase α-2 합의 + GP-3 Stage 2 합의 답습 한정 + 7 금지 영역 *재결정* 0건 + 본 brief = 진입 가능성 *검토 한정* (적격성 *해소* 0건) + 12/12 풀 3+1 트리거 0건 발화 (§5.2) |
| Phase α-3 실 진입 시 합의 | **별도 합의 — Reviewer-only 단축 또는 풀 3+1** | Layer B §5.5.1 ST-3 본문 채택 답습 + Phase α-3 = 7 금지 충돌 0 영역 한정 (사용자 명시 결정 영역) |
| Layer C 발효 합의 | **별도 합의 — 단축 또는 풀 3+1 + 외부 LLM 1+** | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

§5.2 답습 — **12/12 트리거 0건 발화** 확정.

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-15-phase-alpha-3-r7-docker-secret-block-entry.md` 또는 `2026-05-14` 답습) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α-4 R-1 CI workflow 통합 진입 brief 작성** | Phase α-4 진입 가능성 검토 brief (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Phase α 4 단계 (α-1 + α-2 + α-3 + α-4) 통합 진입 brief 작성** | Phase α 통합 진입 brief (병렬 진입 적격 답습) |
| (F) | 본 brief 승인 → **Phase α-3 실 진입 brief 작성** (DRAFT — 실 R-7 docker secret block 운영 단계 분할안) | Phase α-3 실 진입 step 분할 brief (사용자 명시 결정 영역) |
| (G) | 본 brief 승인 → **Phase α-1 ~ α-3 병렬 실제 구현 계획 brief 작성** | Phase α-1 + α-2 + α-3 통합 실 진입 brief (Backlog #6 §6.1 1순위 답습) |
| (H) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (I) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (J) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α-4 R-1 CI workflow 통합 진입 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Phase α 4 단계 통합 진입 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Phase α-3 실 진입 step 분할 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Phase α-1 ~ α-3 병렬 실제 구현 계획 brief 작성."
- (H): "옵션 (H) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (I): "옵션 (I) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — "Phase α-3 R-7 docker secret block 진입 brief를 작성해주세요") |
| 사용자 명시 7 금지 답습 (Phase α-1 / α-2 패턴 답습 — #1 = R-7 영역 한정) | ✅ (7/7 — 실 R-7 docker secret block 수정 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Backlog #6 우선 진입 합의 §6.1 1순위 + §5.2 α-3 답습 | ✅ (Phase α-3 = R-7 docker secret block — 진입 가능성 *검토 한정*, 적격성 *해소* 0건) |
| Phase α-1 합의 (`1b3090b`) 답습 | ✅ (Phase α-1 R-4 합의 본문 변경 0건 + C-β-1 ~ C-β-15 자동 변경 0건) |
| Phase α-2 합의 (`6a79247`) 답습 | ✅ (Phase α-2 R-5 합의 본문 변경 0건 + C-γ-1 ~ C-γ-26 자동 변경 0건) |
| GP-3 Stage 2 합의 답습 | ✅ (Stage 2 §1.3 4 sub-step 답습 + §1.8 5 트리거 0건 발화 답습) |
| GP-3 MVP-1 진입 합의 (`6dc5bdc`) 답습 | ✅ (ST-3 단독 채택 권위 권고 답습) |
| Group α 합의 C-1 ~ C-12 답습 | ✅ (자동 해소 0건 + 자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Layer A / Layer B / §5.5.1 ST-3 본문 채택 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 | ✅ (발화 0건 — §6 답습) |
| Group α 7 단계 승격 Trigger 답습 | ✅ (발화 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust + Hermes upstream 변경 0건 / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (R-7 = file-system secret isolation = catalog / provider 영역과 직교, docker secret = vendor-agnostic 표준) |
| ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 답습 | ✅ (Hermes upstream 변경 회피 보존) |
| ST-3 단독 답습 (ST-1/2/4/5 분리) | ✅ (MVP-1 1차 ST-3 단독 답습 — mvp1.md §5.3) |
| Vault HSM ST-4 미진입 (Backlog #7 분리) | ✅ 분리 명시 |
| inotify sidecar ST-2 미진입 (Backlog #1 분리) | ✅ 분리 명시 (`tools/docker_secret_inotify_sidecar_check.sh` 258줄 = 영역 외) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/12 발화 | ✅ (§5.2 답습) |
| Phase α-3 진입 적격성 5/5 충족 | ✅ (§5.1 답습 — C-α3-1 ~ C-α3-5) |
| R-7 영역 9 artifacts × 328줄 본문 어느 줄도 변경 0건 | ✅ (PoC 답습 변경 0건) |
| Hermes upstream Dockerfile / Production `docker-compose.yml` / `secrets/` 변경 0건 | ✅ (영구 금지 답습) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #6 Runtime + CI-hook 우선 진입 합의 (`c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) §5.2 α-3 답습 후속**, 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬 진입 적격) 中 **Phase α-3 = R-7 docker secret block 영역 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 R-7 docker secret block 수정 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) Phase α-1 / α-2 패턴 답습 (사용자 명시 enumerate 0건 — 본 brief = 패턴 보존 + 사용자 검토 시 prohibition 추가/축소 권위 영역). **R-7 = docker secret block 본문 정의** (9 artifacts × 328줄 답습 — `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` 34줄 + `Dockerfile` 12줄 + `app.py` 46줄 + `secrets/api_key.placeholder` 1줄 = sub-step 2.1 / `tools/docker_secret_image_layer_check.sh` 99줄 = sub-step 2.2 / `tools/docker_secret_restart_recovery.sh` 118줄 = sub-step 2.3 / `tests/fixtures/gp3_st3/pass/Dockerfile` 9줄 + `fail/Dockerfile` 8줄 + `fail/baked_secret.txt` 1줄 = sub-step 2.2 — 본문 변경 0건) + **ST-3 단독 답습 채택** (MVP-1 1차 — ST-1 entrypoint stat / ST-2 inotify sidecar = Backlog #1 1.5차 보강 분리 / ST-4 Vault HSM = Backlog #7 분리 / ST-5 Defense in depth = MVP-2 이후 분리) + **Layer B §5.5.1 GP-3 4 sub-수단 中 ST-3 답습** (S-1 = R-4 영역 / PC-3 + AR-1 = Stage 4 영역 분리) + **9 sub-step Phase α-3 본문 작업 후보 분할 매트릭스** + **7 금지 영역 × R-7 분리 매트릭스** (7/7 분리 — 충돌 0) + **Phase α-3 진입 적격성 5 조건 검토** (C-α3-1 7 금지 충돌 0/7 + C-α3-2 PoC 답습 100% 보존 + C-α3-3 의존성 0 (R-4 / R-5 / R-1 분리 + Stage 2 actual run PASS 답습) 병렬 진입 적격 + C-α3-4 Provider Liquidity 5-way 100% 보존 (docker secret = vendor-agnostic 표준) + C-α3-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **12 풀 3+1 승격 트리거 0/12 발화** + **R-7 영역 영향 Rollback Trigger 의존성 답습** (18 trigger 中 R-7 직접 영향 2 + 간접 영향 1 + 영향 0 15 — 발화 0건 + ST-1/2/4/5 별도 backlog 4 trigger 분리) + **본 brief 자체 금지 60 + Phase α-3 실 진입 단계 금지 20** + **합의 형태 권고** (Reviewer-only 단축 — 12/12 트리거 0건 발화) 를 정리한다. **본 brief 는 Phase α-3 실 진입을 *시작* 시키지 않으며, R-7 영역 9 artifacts × 328줄 어느 줄도 *변경* 하지 않으며, `secret-hygiene-egress-redaction.yml` Stage 2 entry step / Hermes upstream Dockerfile / Production `docker-compose.yml` / `secrets/` 디렉토리 / R-4 도구 / R-5 `.importlinter` / R-1 CI workflow / 7 금지 영역 *해소* / Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / Backlog #6 우선 진입 합의 본문 변경 / Phase α-1 / α-2 합의 본문 변경 / GP-3 Stage 2 합의 본문 변경 / GP-3 MVP-1 진입 합의 본문 변경 / Layer B §5.5.1 본문 변경 / ST-3 = ST-1/2/4/5 흡수 / R-MVP1-G3-3 자동 발화 / 실 secret material commit / `.gitignore` 변경 / Phase α-1 / α-2 / α-4 자동 진입 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습).

---

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~J, §9 답습)
**금지 (사용자 명시 패턴 답습 — 본 brief 영역)**:
- ❌ **실 R-7 docker secret block 수정** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` 본문 / `.git/hooks/pre-commit` 본문)
- ❌ Production `docker-compose.yml` 신설 / 변경 (PoC 격리 디렉토리 한정 답습)
- ❌ Hermes upstream Dockerfile 변경 (ADR-008 차단조건 #6 + 부록 B 답습)
- ❌ R-7 영역 9 artifacts × 328줄 본문 어느 줄도 변경 (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/`)
- ❌ R-4 도구 본문 변경 (`tools/*.py`)
- ❌ R-5 `.importlinter` 본문 변경
- ❌ R-1 CI workflow 통합 (`.github/workflows/*.yml`)
- ❌ Phase α-1 / α-2 / α-4 자동 진입
- ❌ Phase β / γ 자동 진입
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ ST-3 = ST-1 / ST-2 / ST-4 / ST-5 흡수 시도 (단독 답습)
- ❌ ST-4 Vault HSM 진입 (Backlog #7 분리)
- ❌ inotify sidecar (`tools/docker_secret_inotify_sidecar_check.sh` 258줄) 본 영역 흡수
- ❌ 실 secret material commit
- ❌ `secrets/.gitignore` 변경 (placeholder 한정 영구 답습)
- ❌ secret material marker 위반 (실 vendor prefix 사용 금지 — `FAKE_TEST_SECRET_*` prefix 한정)
- ❌ G3-7 row 4 항목 자동 흡수 (Stage 5 분리)
- ❌ R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) 자동 발화
- ❌ Layer B §5.5.1 GP-3 4 sub-수단 본문 채택 변경
- ❌ GP-3 Stage 2 합의 §1.3 4 sub-step 분할안 변경
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) 자동 변경
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경
- ❌ GP-3 Stage 2 합의 본문 변경
- ❌ GP-3 MVP-1 진입 합의 (`6dc5bdc`) 본문 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 합의 / Phase α-2 합의 / GP-3 진입 합의 / GP-3 Stage 2 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ 실 docker build / docker run / docker history 자동 실행
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
