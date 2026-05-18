# Phase α-4 Stage 4 진입 brief (W-1 ~ W-4 최소 영역) (DRAFT)

> **본 문서는 Phase α-4 R-1 실 진입 *여부* 검토 합의 (`d3f6d59` APPROVE AS BRIEF — 36 조건 C-τ-1 ~ C-τ-36, Reviewer-only 단축) 발효 후속, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *Stage 4 실 진입* 의 W-1 ~ W-4 최소 영역 *수정 파일 / 검증 방법 / actual run 조건 / rollback trigger 확정* 한정 brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 1 (영역 정의, `f91ef4b` + `e59a565`) = "*Can* we enter Phase α-4?"
> - α-4 Stage 1.5 (조건 재검토, `7a289fa` + `1c365e7`) = "*Are conditions still satisfied?*"
> - α-4 Stage 2 (Step Division, `ed1d1b6` + `52a05cb`) = "*How* should it be staged?"
> - α-4 Stage 2.5 (LVE, `4ce5a0b` + `b264580`) = "*Has local validation evidence been compiled?*"
> - α-4 Stage 3 (실 진입 여부 검토, `27351ce` + `d3f6d59`) = "*Should* we enter actual implementation now?"
> - **본 brief = α-4 Stage 4 (실 진입 lockdown) DRAFT** — **"*What exactly* will Stage 4 W-1 ~ W-4 do, with which files / verifications / actual run conditions / rollback triggers, BEFORE any actual implementation begins?"**
> - α-4 Stage 4 실 구현 (본 brief 외) = "*Execute* the locked plan"
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) W-1 / W-2 / W-3 / W-4 어느 작업도 *실행* 시키지 않으며, (ii) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, (iii) Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 (parallel) 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 여부 36 = **합산 389 합의 조건** 中 어느 것도 *해소* / *변경* 시키지 않으며, (iv) 사용자 명시 3 금지 (W-5~W-10 분리 / Operational Readiness PASS / Hermes PMO 격상) + 영구 5 금지 中 #2 / #4 / #5 어느 것도 *해소* 시키지 않으며, (v) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, (vi) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-18
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-actual-entry-decision.md` (Stage 3 실 진입 여부 검토 합의, commit `d3f6d59` APPROVE AS BRIEF — 36 조건 C-τ-1 ~ C-τ-36, Reviewer-only 단축, **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-actual-entry-decision-brief.md` (commit `27351ce`, 722줄 Stage 3 brief)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-local-validation-evidence.md` (LVE 합의, commit `b264580` — 31 조건 C-σ-1 ~ C-σ-31)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-step-division.md` (Step Division 합의, commit `52a05cb` — 38 조건 C-ρ-1 ~ C-ρ-38)
- `docs/phase0/phase-alpha-4-r1-step-division-brief.md` (commit `ed1d1b6`, 871줄 Step Division brief)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-entry-condition.md` (α-4 진입 조건 점검 합의, commit `1c365e7` — 33 조건 C-π-1 ~ C-π-33)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (직전 α-4 brief 합의, commit `e59a565` — 29 조건 C-ε-1 ~ C-ε-29)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (Stage 4 PC-3 + AR-1 통합 진입 합의 APPROVE — sub-step 4.1 + 4.2 발효)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C (Hermes PMO Activation 12 조건 미진입 영구 답습)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-4 Stage 4 진입 brief를 작성해주세요. 범위는 W-1~W-4 최소 영역으로 제한합니다. 목표는 R-1 CI workflow 통합을 실제로 시작하기 전, 수정 파일, 검증 방법, actual run 조건, rollback trigger를 확정하는 것입니다. W-5~W-10, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 3 금지 답습 (본 brief 의 명시적 경계)

1. ❌ **W-5 ~ W-10 영역 진입 금지** — `permissions: contents: read` 보강 / Required check 등록 / PC-4 pre-commit / AR-2 branch protection / AR-3 자동 revert bot / Stage 5 (G3-7 4 항목) 모두 0건 (Backlog #1+#2 / Backlog #3 T3 / Stage 5 분리 영구 답습)
2. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리 영구 답습 (영구 5 금지 #4)
3. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C 12 조건 미진입 영구 답습 (영구 5 금지 #5)

### 0.3 영구 5 금지 × 본 brief 분리 매트릭스

| # | 영구 금지 영역 | 본 brief 시점 | 본 brief 발효 후 Stage 4 실 구현 시점 (사용자 명시 결정 영역) |
|---|---------|----------|------------------------------------------|
| #1 | CI workflow 변경 | ✅ 0건 (R-1 7 artifacts × 1593줄 답습 보존) | **해소 영역 (Stage 4 실 구현 시점)** — 본 brief = lockdown 한정 |
| #2 | runtime code 변경 | ✅ 0건 (`src/` + facade.py 41줄 placeholder 답습) | ✅ 0건 (Backlog #4 분리 영구 답습) |
| #3 | actual run 재실행 | ✅ 0건 (4 prerequisite runs 답습 한정) | **해소 영역 (Stage 4 실 구현 시점)** — 본 brief = lockdown 한정 |
| #4 | Operational Readiness PASS | ✅ 0건 | ✅ 0건 (사용자 명시 3 금지 #2) |
| #5 | Hermes PMO 격상 | ✅ 0건 | ✅ 0건 (사용자 명시 3 금지 #3) |
| **합산** | **5** | **✅ 5/5 영구 답습** | **2 해소 가능 영역 + 3 영구 보존** |

**중요**: 본 brief 시점 = **5/5 영구 답습** (0/5 해소). Stage 4 실 구현 시점 = **2 해소 (#1 + #3)** + **3 영구 보존 (#2 + #4 + #5)** — 본 brief = *해소 발효 0건* + *lockdown 권고 한정*.

### 0.4 본 brief 가 *하는* 것

1. Phase α-4 Stage 3 실 진입 여부 합의 (`d3f6d59`) 발효 후속 — **Stage 4 W-1 ~ W-4 lockdown 한정** (§1)
2. **W-1 ~ W-4 작업 영역 *확정 권고* 매트릭스** — W-5 ~ W-10 분리 명시 (§2)
3. **수정 파일 *확정 권고* 매트릭스** — W-1 (3 MVP-1 workflow) / W-2 (integration tool) / W-3 (3 fixture) / W-4 (수정 파일 0건 — actual run trigger 한정) (§3)
4. **검증 방법 *확정 권고* 매트릭스** — Pre-implementation / Per-W / Post-implementation / Actual run 검증 (§4)
5. **Actual run 조건 *확정 권고* 매트릭스** — Trigger event + Branch + SUCCESS 조건 + FAILURE 조건 + token/secret 영역 (§5)
6. **Rollback Trigger *확정 권고* 매트릭스** — Layer B 18 + TR-1 ~ TR-5 + Step Division 신규 후보 5 = 28 trigger × Stage 4 시점 발화 대응 절차 (§6)
7. **사용자 명시 3 금지 + 영구 5 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 389 합의 조건 답습 매트릭스** (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 3 금지 영역**:

- ❌ **W-5 ~ W-10 영역 진입 (0건)** — `permissions:` 보강 / Required check / PC-4 / AR-2 / AR-3 / Stage 5 모두 영역 외 영구 답습
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**영구 5 금지 영역 (본 brief 시점 답습 한정)**:

- ❌ **CI workflow 변경 (0건)** — R-1 7 artifacts × 1593줄 답습 보존 — 본 brief = lockdown 한정 (실 변경 = Stage 4 실 구현 영역)
- ❌ **runtime code 변경 (0건)** — `src/` + facade.py 41줄 placeholder 답습 보존 (Backlog #4 분리)
- ❌ **actual run 재실행 (0건)** — 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 답습 한정 — 본 brief = lockdown 한정 (실 trigger = Stage 4 실 구현 영역)

**추가 금지 영역 (Stage 3 brief + LVE + Step Division + α-4 진입 조건 점검 + 직전 α-4 brief + α-1+2+3 evidence 답습 패턴 보존)**:

- ❌ **W-1 ~ W-4 자동 실행 (0건)** — 본 brief = *lockdown 권고 한정* (실 실행 = Stage 4 실 구현 영역, 사용자 명시 결정 후 진입)
- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — `secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + `tools/mvp1_pc3_ar1_integration_check.py` 298 + 3 fixture 89 = 1593줄 답습 보존
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (α-1+2+3 evidence §5.1 답습)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **PC-4 / AR-2 / AR-3 진입 (0건)** — Backlog #1+#2 / Backlog #3 / Stage 5 분리 답습
- ❌ **ST-1 / ST-2 / ST-4 / ST-5 진입 (0건)** — Backlog 분리
- ❌ **S-2 gitleaks 도입 (0건)** — Backlog #1 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 답습
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 영역 별도 풀 3+1
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 0건
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 모두 0건
- ❌ **신규 workflow 신설 (0건)** + **`pull_request_target` 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습 (G3-7 (i))
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정 답습
- ❌ **실 secret material commit (0건)** — FAKE_TEST_SECRET marker 답습
- ❌ **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`951a5b1`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 ~ α-3 / Phase α-4 직전 / α-1+2+3 evidence (`7b3d40a`) / α-4 진입 조건 점검 (`1c365e7`) / Step Division (`52a05cb`) / LVE (`b264580`) / Stage 3 실 진입 여부 (`d3f6d59`) 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 (0건)**
- ❌ **Phase α-1 / α-2 / α-3 자동 재진입 (0건)** — α-1+2+3 evidence §5.2 + §8 답습
- ❌ **Layer C 재발효 (0건)** — `eb01bc4` 답습 한정 / Layer D 재선언 (0건) / MVP-1 PASS 재선언 (0건)
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)** — 별도 commit 분리 (사용자 명시 결정 후 진입)
- ❌ **git commit / push (0건)** — 사용자 명시 결정 후 진입
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **token rotation 정책 / GitHub plan 가용성 자동 결정 (0건)** — Group α C-3 + C-4 답습
- ❌ **threshold *고정* (0건)** — CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **합산 389 합의 조건 자동 변경 (0건)**

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) W-1 / W-2 / W-3 / W-4 어느 작업도 *실행* 시키지 않으며,
- (ii) 합산 389 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iii) 영구 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (iv) 사용자 명시 3 금지 영역 어느 것도 *해소* 시키지 않으며,
- (v) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (vi) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vii) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (viii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (ix) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (x) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (xi) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 어느 것도 *발생시키지 않으며*,
- (xii) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 5 trigger 어느 것도 *발화* 시키지 않으며,
- (xiii) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (xiv) W-1 ~ W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 Stage 4 W-1 ~ W-4 lockdown 권고 한정**. 모든 *확정 발효* / *실 실행* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (Stage 3 실 진입 여부 합의 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `e59a565` (2026-05-14) | Phase α-4 R-1 직전 brief 합의 — 29 조건 C-ε-1 ~ C-ε-29 | ✅ 답습 한정 |
| `f91ef4b` (2026-05-14) | Phase α-4 R-1 직전 brief DRAFT (751줄) | ✅ 답습 한정 |
| `eb01bc4` (2026-05-16) | Layer C 발효 (30 조건 C-ι-1 ~ C-ι-30) | ✅ 답습 한정 |
| `951a5b1` (2026-05-16) | Layer D 재진입 평가 (25 조건 C-λ-1 ~ C-λ-25) | ✅ 답습 한정 |
| `542e77e` (2026-05-16) | Stage 1 — Phase α 통합 계획 (25 조건 C-μ-1 ~ C-μ-25) | ✅ 답습 한정 |
| `88ccf79` (2026-05-16) | Stage 2 — α-1+2+3 1순위 계획 (25 조건 C-ν-1 ~ C-ν-25) | ✅ 답습 한정 |
| `7917e4a` (2026-05-16) | Stage 3 — α-1+2+3 parallel actual entry (25 조건 C-ξ-1 ~ C-ξ-25) | ✅ 답습 한정 |
| `7b3d40a` (2026-05-16) | α-1+2+3 Local Validation Evidence (486줄, 12/12 PASS) | ✅ 답습 한정 |
| `7a289fa` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 brief (566줄) | ✅ 답습 한정 |
| `1c365e7` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 합의 — 33 조건 C-π-1 ~ C-π-33 | ✅ 답습 한정 |
| `ed1d1b6` (2026-05-17) | Phase α-4 R-1 Step Division brief (871줄) | ✅ 답습 한정 |
| `52a05cb` (2026-05-17) | Phase α-4 R-1 Step Division 합의 — 38 조건 C-ρ-1 ~ C-ρ-38 | ✅ 답습 한정 |
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 — 31 조건 C-σ-1 ~ C-σ-31 | ✅ 답습 한정 |
| `27351ce` (2026-05-17) | Phase α-4 R-1 Stage 3 실 진입 여부 brief (722줄) | ✅ 답습 한정 |
| `d3f6d59` (2026-05-17) | Phase α-4 R-1 Stage 3 합의 — 36 조건 C-τ-1 ~ C-τ-36 | ✅ **본 brief 의 발효 trigger** |
| `630e125` (HEAD, 2026-05-17) | CONTEXT — Phase α-4 R-1 Stage 3 실 진입 여부 status entry | ✅ 답습 한정 |

### 1.2 Stage 3 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-17 (후속 27) |
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 — 16/16 풀 3+1 트리거 0건 발화) |
| 합의 조건 | **36 조건 (C-τ-1 ~ C-τ-36)** |
| Stage 4 작업 권고 영역 | **W-1 ~ W-4 최소 영역** (W-5 ~ W-10 *비*권고 — 영역 경계 불명확) |
| Pro 매트릭스 | **9/9 Pro** (technical readiness 9/9 충족) |
| Con 매트릭스 | 9 Con (governance / 5 금지 해소 risk) |
| 5 금지 해소 매트릭스 | Stage 4 시점 #1 + #3 해소 (필수) + #2 / #4 / #5 영구 보존 — **본 brief 시점 0/5 해소 영구 답습** |
| Rollback Trigger 발화 예상 | **합산 28 trigger × Stage 4 W-1+W-2 본문 변경 시 5 발화 가능성** (Layer B #13/#14 + Step Division 신규 후보 3 = 신중 영역) |
| 합의 형태 권고 (Stage 4 시점) | **W-1 ~ W-4 = 풀 3+1 합의 (필수)** (T-2 발화) / W-5 ~ W-10 = 풀 3+1 + 외부 LLM 1+ (T-2 + T-6 + T-10 + T-13 발화 가능) |
| 본 brief trigger 의미 | Stage 4 W-1 ~ W-4 *권고 시작점 권위 확정* → **lockdown 권고 (= 본 brief)** 의 framing 정당화 |

### 1.3 6 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 (C-ε-1 ~ C-ε-29) | "*Can* we enter Phase α-4?" |
| α-4 Stage 1.5 (조건 재검토) | Phase α-4 R-1 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 (C-π-1 ~ C-π-33) | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (Step 분할) | Phase α-4 R-1 Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 (C-ρ-1 ~ C-ρ-38) | "*How* should it be staged?" |
| α-4 Stage 2.5 (LVE) | Phase α-4 R-1 Local Validation Evidence | `4ce5a0b` + `b264580` | APPROVE | 31 (C-σ-1 ~ C-σ-31) | "*Has local validation evidence been compiled?*" |
| α-4 Stage 3 (실 진입 여부) | Phase α-4 R-1 Stage 3 brief | `27351ce` + `d3f6d59` | APPROVE AS BRIEF | 36 (C-τ-1 ~ C-τ-36) | "*Should* we enter actual implementation now?" |
| **α-4 Stage 4 (본 brief, lockdown)** | **Phase α-4 R-1 Stage 4 진입 brief (W-1 ~ W-4)** | (현재) | DRAFT (미확정) | (미확정) | **"*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?*"** |
| α-4 Stage 4 실 구현 (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* the locked plan" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 4 lockdown framing** (Step Division §1.3 답습 + Stage 3 §10.1 권고 시작점 답습):

- α-4 Stage 1 ↔ α-4 Stage 1.5 ↔ α-4 Stage 2 ↔ α-4 Stage 2.5 ↔ α-4 Stage 3 ↔ **α-4 Stage 4 lockdown (본 brief)** ↔ α-4 Stage 4 실 구현 (사용자 명시 결정 영역)
- 본 brief 의 단일 책무: **"W-1 ~ W-4 의 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger lockdown 권고"** + **"실 구현 자동 진입 0건"**
- 본 brief ≠ α-4 Stage 4 실 구현 (CI workflow 변경 + actual run 재실행 = 별도 cycle 영역)
- 본 brief ≠ Phase α-4 자동 진입 발효 (사용자 명시 결정 영역)
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-18 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 3 금지 #2 영구 답습) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 3 금지 #3 영구 답습) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 |
| **Phase α-4 (R-1)** | **2순위 의존 — CI workflow 통합 (PC-3 + AR-1)** | ✅ R-1 영역 본문 = 이미 구현 완료 + 4 prerequisite runs 4/4 SUCCESS + local 51/51 PASS + α-1+2+3 evidence 12/12 PASS + ⏳ **본 brief = Stage 4 W-1 ~ W-4 lockdown 한정** |

---

## 2. W-1 ~ W-4 작업 영역 확정 권고 매트릭스

### 2.1 W-1 ~ W-4 작업 영역 enumerate (Stage 3 §4.2 답습)

| # | 작업 영역 | 영구 5 금지 해소 | 사용자 명시 3 금지 위반 | 본 brief 영역 |
|---|--------|----------|------------------|----------|
| **W-1** | 3 MVP-1 workflow 본문 step 추가 / 수정 / step 순서 변경 (R-1 영역 7 artifacts 中 3 workflow = `secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml`) | #1 해소 (Stage 4 실 구현 시점) | 0건 | ✅ 본 brief = lockdown 권고 한정 |
| **W-2** | integration check tool 본문 step 추가 / 수정 / mode 추가 (R-1 영역 7 artifacts 中 1 tool = `tools/mvp1_pc3_ar1_integration_check.py`) | #1 해소 (Stage 4 실 구현 시점) | 0건 | ✅ 본 brief = lockdown 권고 한정 |
| **W-3** | 3 fixture 본문 추가 / 수정 (R-1 영역 7 artifacts 中 3 fixture = `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` + `fail/pc3_violation_continue_on_error.yml` + `fail/ar1_violation_no_fail_closed.yml`) | #1 해소 (Stage 4 실 구현 시점) | 0건 | ✅ 본 brief = lockdown 권고 한정 |
| **W-4** | 신규 actual GitHub Actions run trigger (push event / PR event on `feature/hermes-phase0` branch) | #3 해소 (Stage 4 실 구현 시점) | 0건 | ✅ 본 brief = lockdown 권고 한정 |

### 2.2 W-5 ~ W-10 분리 매트릭스 (위반 0건 영구 답습)

| # | 작업 영역 | 사용자 명시 3 금지 위반 | Backlog 분리 | 본 brief 영역 |
|---|--------|------------------|------------|----------|
| W-5 | 3 MVP-1 workflow `permissions: contents: read` 보강 | ❌ 위반 (사용자 명시 3 금지 #1 — Stage 5 cycle 4 영역) | Stage 5 cycle 4 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| W-6 | 3 MVP-1 workflow Required check 으로 등록 | ❌ 위반 (사용자 명시 3 금지 #1 — branch protection 변경 = Backlog #3 T3) | Backlog #3 T3 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| W-7 | Stage 4 sub-step 4.3 PC-4 local pre-commit hook 활성화 | ❌ 위반 (사용자 명시 3 금지 #1 — `.pre-commit-config.yaml` 신설 = Backlog #1+#2) | Backlog #1+#2 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| W-8 | Stage 4 sub-step 4.4 AR-2 branch protection rule | ❌ 위반 (사용자 명시 3 금지 #1 — branch protection API = Backlog #3 T3) | Backlog #3 T3 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| W-9 | AR-3 자동 revert bot | ❌ 위반 (사용자 명시 3 금지 #1 — CODEOWNERS + bot 설정 = Backlog #3 T3) | Backlog #3 T3 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| W-10 | Stage 5 (G3-7 4 항목) 진입 | ❌ 위반 (사용자 명시 3 금지 #1 — secret reset rotate / fork PR / pull_request_target / commit signing) | Stage 5 분리 영구 답습 | ❌ 본 brief 영역 외 (0건) |
| **합산** | **6 항목** | **6/6 위반** | **분리 명시 + 위반 0건** | **0건 영구 답습** |

### 2.3 작업 순서 권고 (직렬 / 병렬)

| 옵션 | 영역 | 권고 |
|---------|------|----|
| (i) 직렬 (W-1 → W-2 → W-3 → W-4) | 가장 안전한 토폴로지 — 단계별 검증 가능 + 회복 가능성 ↑ | **권고 (Stage 4 실 구현 시점)** |
| (ii) W-1 / W-2 / W-3 병렬 → W-4 (직렬 후행) | W-1/W-2/W-3 = 독립 (workflow / tool / fixture 영역 분리) — W-4 는 W-1/W-2/W-3 완료 의존 | 옵션 (속도 ↑) |
| (iii) W-1 + W-2 + W-3 + W-4 동시 진입 | 최단 cycle | ❌ 비권고 (디버깅 어려움 + rollback 영역 확대) |
| (iv) W-1 / W-2 / W-3 본문 변경 0건 + W-4 한정 (현재 상태 답습) | R-1 본문 = 이미 구현 완료 답습 한정 | **권고 시작점 (Stage 4 실 구현 시점 minimal scope)** |

본 brief 권고 = **(iv) → (i) 순차 적용** — Stage 4 실 구현 시점 우선 (iv) 최소 영역 (W-4 단독 = 운영 진입 trigger) → 필요 시 (i) 직렬 단계 확장. 권고 근거: R-1 본문 = 이미 구현 완료 + 4 prerequisite runs 4/4 SUCCESS + local 51/51 PASS → **본문 변경 필요성 = 0 (현재 상태 답습)** → W-1 / W-2 / W-3 = 본문 변경 0건 영역 (workflow 자체 trigger 활성화 한정).

### 2.4 본 §2 의 *범위 한계*

본 §2 = **W-1 ~ W-4 영역 *권고 한정***. 실 작업 결정 / 작업 진입 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 *권고* = 권위 권고 한정 — 실 작업 진입 발효 권위 0건.

---

## 3. 수정 파일 확정 권고 매트릭스

### 3.1 W-1: 3 MVP-1 workflow 수정 파일

| 파일 경로 | 현재 줄수 | 본 brief 권고 변경 영역 | 변경 line 수 | 답습 출처 |
|---------|-------|------------------|----------|---------|
| `.github/workflows/secret-hygiene-egress-redaction.yml` | 694 | **0건 영구 답습** (Stage 4 실 구현 시점 = ≤ 5 lines 마이크로 패치 *권고 시작점*) | 0 ~ ≤ 5 lines | LVE §3.1 답습 (현재 상태 = brief 명세 100% 일치) |
| `.github/workflows/provider-adapter-enforcement.yml` | 186 | **0건 영구 답습** (Stage 4 실 구현 시점 = ≤ 5 lines 마이크로 패치 *권고 시작점*) | 0 ~ ≤ 5 lines | LVE §3.1 답습 |
| `.github/workflows/provider-url-scanner.yml` | 326 | **0건 영구 답습** (Stage 4 실 구현 시점 = ≤ 5 lines 마이크로 패치 *권고 시작점*) | 0 ~ ≤ 5 lines | LVE §3.1 답습 |
| **합산** | **1206** | **0건 본 brief 시점 / Stage 4 실 구현 시점 ≤ 15 lines 권고 시작점** | **0 ~ ≤ 15 lines** | — |

**해석**: 현재 상태 매트릭스 답습 한정 (R-1 본문 = 이미 구현 완료) → W-1 본문 변경 *권고 시작점* = **0 ~ ≤ 15 lines** (3 workflow 합산). 변경 필요 발견 시 *마이크로 패치* (예: trigger event branch 추가 / paths 패턴 보강 / step name 정정) 한정 — *step 추가 / step 순서 변경 / 본문 재작성 = 영역 외* (Stage 4 별도 합의 요구).

### 3.2 W-2: integration check tool 수정 파일

| 파일 경로 | 현재 줄수 | 본 brief 권고 변경 영역 | 변경 line 수 | 답습 출처 |
|---------|-------|------------------|----------|---------|
| `tools/mvp1_pc3_ar1_integration_check.py` | 298 | **0건 영구 답습** (Stage 4 실 구현 시점 = ≤ 5 lines 마이크로 패치 *권고 시작점*) | 0 ~ ≤ 5 lines | LVE §3.2 답습 (현재 상태 = brief 명세 100% 일치 + `--mode integration` + `--list-checks` PASS) |
| **합산** | **298** | **0건 본 brief 시점 / Stage 4 실 구현 시점 ≤ 5 lines 권고 시작점** | **0 ~ ≤ 5 lines** | — |

**해석**: W-2 본문 변경 *권고 시작점* = **0 ~ ≤ 5 lines** — 변경 필요 발견 시 *마이크로 패치* (예: error message 정정 / log line 보강 / mode 명 정정) 한정 — *mode 추가 / step 추가 / 본문 재작성 = 영역 외* (Stage 4 별도 합의 요구).

### 3.3 W-3: 3 fixture 수정 파일

| 파일 경로 | 현재 줄수 | 본 brief 권고 변경 영역 | 변경 line 수 | 답습 출처 |
|---------|-------|------------------|----------|---------|
| `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` | 30 | **0건 영구 답습** (Stage 4 실 구현 시점 = 0 lines *권고 시작점*) | 0 lines | LVE §3.3 답습 (PASS fixture integration tool 통과) |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` | 31 | **0건 영구 답습** (Stage 4 실 구현 시점 = 0 lines *권고 시작점*) | 0 lines | LVE §3.3 답습 (FAIL fixture integration tool 적절 차단) |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` | 28 | **0건 영구 답습** (Stage 4 실 구현 시점 = 0 lines *권고 시작점*) | 0 lines | LVE §3.3 답습 (FAIL fixture integration tool 적절 차단) |
| **합산** | **89** | **0건 본 brief 시점 / Stage 4 실 구현 시점 0 lines 권고 시작점** | **0 lines** | — |

**해석**: W-3 본문 변경 *권고 시작점* = **0 lines** — 3 fixture = 100% 충족 답습 한정. 본문 추가 / 영역 보강 = 영역 외 (Stage 4 별도 합의 요구).

### 3.4 W-4: 신규 actual GitHub Actions run trigger

| trigger event | 영역 | 수정 파일 | 본 brief 권고 |
|------------|----|---------|----------|
| `push` event on `feature/hermes-phase0` branch | 3 MVP-1 workflow 신규 실 진입 | **수정 파일 0건** (git push trigger 한정) | ✅ 권고 시작점 |
| `pull_request` event on `feature/hermes-phase0 → main` PR | 3 MVP-1 workflow PR check 신규 실 진입 | **수정 파일 0건** (PR open trigger 한정) | 옵션 (W-1 ~ W-3 본문 변경 시 권고) |
| `workflow_dispatch` event (manual) | 3 MVP-1 workflow 수동 trigger | **수정 파일 0건** (UI trigger 한정) | 옵션 (디버깅 시 권고) |

**해석**: W-4 = **수정 파일 0건** (git push / PR open / manual UI trigger 中 1 = trigger event 한정) — 본 brief 권고 시작점 = `push` event on `feature/hermes-phase0` branch (W-1/W-2/W-3 본문 변경 0건 시).

### 3.5 R-4 / R-5 / R-7 / src / docker block / placeholder 본문 변경 0건 매트릭스

| 영역 | 현재 줄수 | 본 brief 권고 변경 | Stage 4 실 구현 시점 변경 |
|------|-------|----------------|------------------|
| R-4 = `tools/secret_scanner.py` 등 (Phase α-1 영역) | 1192줄 합산 13 file | **0건** | **0건 영구 답습** (Phase α-1 영역 분리) |
| R-5 = `.importlinter` (Phase α-2 영역) | INI 답습 | **0건** | **0건 영구 답습** (Phase α-2 영역 분리) |
| R-7 = `docker/gp3-st3-poc/docker-compose.yml` 등 (Phase α-3 영역) | docker block 답습 | **0건** | **0건 영구 답습** (Phase α-3 영역 분리) |
| `src/` runtime code | 답습 | **0건** | **0건 영구 답습** (영구 5 금지 #2 영구 답습) |
| `src/adapters/llm/facade.py` placeholder | 41줄 | **0건** | **0건 영구 답습** (Backlog #4 분리) |
| Hermes upstream Dockerfile | 답습 | **0건** | **0건 영구 답습** (ADR-008 §2.6.2 R2-1 영구 답습) |
| Production `docker-compose.yml` | 신설 0건 | **0건** | **0건 영구 답습** (PoC 격리 디렉토리 한정) |

### 3.6 수정 파일 영역 ↔ 사용자 명시 3 금지 분리 매트릭스

| 영역 | 사용자 명시 3 금지 #1 (W-5~W-10 분리) | #2 (Operational Readiness PASS) | #3 (Hermes PMO 격상) |
|---------|--------------------|--------------------|--------------------|
| W-1 (3 MVP-1 workflow) | ✅ 0건 (W-5 = permissions 보강 / W-6 = Required check = W-5~W-10 영역) | ✅ 0건 | ✅ 0건 |
| W-2 (integration tool) | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| W-3 (3 fixture) | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| W-4 (actual run trigger) | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| **합산** | **✅ 4/4 × 3 = 12/12 위반 0건** | — | — |

### 3.7 본 §3 의 *범위 한계*

본 §3 = **수정 파일 *권고 한정***. 실 변경 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 시점 R-1 + R-4/R-5/R-7 + `src/` 본문 = **모두 0건 영구 답습**. Stage 4 실 구현 시점 권고 시작점 = **W-1 ~ W-3 합산 ≤ 25 lines 마이크로 패치 + W-4 = 0 lines (trigger 한정)**.

---

## 4. 검증 방법 확정 권고 매트릭스

### 4.1 Pre-implementation 검증 (Stage 4 W-1 진입 *전*)

| # | 검증 영역 | 검증 명령 | 답습 출처 | 신규 actual run trigger |
|---|--------|--------|---------|---------------------|
| PRE-1 | `git status` clean 검증 — 본 brief commit 후 working tree clean | `git status` | LVE §2 답습 | 0건 |
| PRE-2 | R-1 영역 7 artifacts × 1593줄 답습 확인 — line count diff 0 | `wc -l .github/workflows/{secret-hygiene-egress-redaction,provider-adapter-enforcement,provider-url-scanner}.yml tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/**/*.yml` | LVE §3 답습 | 0건 |
| PRE-3 | 4 prerequisite runs 4/4 SUCCESS 답습 확인 — JSON conclusion 답습 | `gh run view 25728590939 --json conclusion,status` (× 4) | LVE §4 답습 | 0건 (read-only) |
| PRE-4 | local 51/51 PASS evidence 답습 확인 | LVE 본문 (`4ce5a0b`) §3 ~ §4 답습 enumerate | LVE 답습 | 0건 |
| PRE-5 | α-1+2+3 evidence 12/12 PASS 답습 확인 | α-1+2+3 evidence (`7b3d40a`) §3 ~ §4 답습 enumerate | α-1+2+3 evidence 답습 | 0건 |
| PRE-6 | 5 영구 핵심 제약 5/5 보존 확인 | LVE §5.1 답습 enumerate | LVE 답습 | 0건 |
| PRE-7 | Provider Liquidity 5-way 100% 보존 확인 | LVE §5.2 답습 enumerate | LVE 답습 | 0건 |
| PRE-8 | F-금지 #1 영구 답습 확인 | LVE §5.3 답습 + workflow secrets reference check | LVE 답습 | 0건 |
| PRE-9 | 합산 389 합의 조건 답습 확인 — 변경 0건 | §8 답습 | 본 brief §8 | 0건 |

**합산**: 9 검증 영역 × 0 신규 actual run trigger × 답습 한정.

### 4.2 Per-W 단위 검증 매트릭스 (W-1 / W-2 / W-3 각각)

#### 4.2.1 W-1 검증 (3 MVP-1 workflow)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-1-V1 | `secret-hygiene-egress-redaction.yml` 694줄 yamllint 통과 | `yamllint .github/workflows/secret-hygiene-egress-redaction.yml` (또는 `python -c "import yaml; yaml.safe_load(open(...))"`) | rc=0 |
| W-1-V2 | `provider-adapter-enforcement.yml` 186줄 yamllint 통과 | (동상) | rc=0 |
| W-1-V3 | `provider-url-scanner.yml` 326줄 yamllint 통과 | (동상) | rc=0 |
| W-1-V4 | PC-3 정합성 — 3 workflow Stage 4 step `continue-on-error` 미지정 (또는 false) grep | `grep -A2 "Stage 4.*integration check" .github/workflows/*.yml \| grep -v "continue-on-error: true"` | match 0건 |
| W-1-V5 | AR-1 정합성 — 3 workflow Stage 4 step `if: always()` 패턴 + non-zero exit propagation | `grep "Stage 4" .github/workflows/*.yml` + step 본문 정합성 | 패턴 일치 |
| W-1-V6 | 3 workflow trigger event 영역 — `feature/hermes-phase0` 매칭 검증 | `grep "feature/\*\*" .github/workflows/*.yml` | branch 매칭 |
| W-1-V7 | 3 workflow paths filter 영역 — `tools/` / `tests/fixtures/` / `.github/workflows/` 트리거 정합성 | `grep -A20 "paths:" .github/workflows/*.yml` | 트리거 정합성 |

**검증 도구**: `yamllint` (표준) + `grep` (표준) — 신규 actual run trigger 0건 (local 한정).

#### 4.2.2 W-2 검증 (integration check tool)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-2-V1 | `tools/mvp1_pc3_ar1_integration_check.py` 298줄 Python syntax 통과 | `python -c "import py_compile; py_compile.compile('tools/mvp1_pc3_ar1_integration_check.py')"` | rc=0 |
| W-2-V2 | `--list-checks` 모드 — checks enumerate | `python tools/mvp1_pc3_ar1_integration_check.py --list-checks` | rc=0 + checks ≥ 5 |
| W-2-V3 | `--mode integration` 자체 self-check | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration .github/workflows/secret-hygiene-egress-redaction.yml .github/workflows/provider-adapter-enforcement.yml .github/workflows/provider-url-scanner.yml` | rc=0 + violations=0 |
| W-2-V4 | PASS fixture (`compliant_entry_step.yml`) 통과 | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` | rc=0 |
| W-2-V5 | FAIL fixture (PC-3 violation) 적절 차단 | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` | rc=1 + violation reported |
| W-2-V6 | FAIL fixture (AR-1 violation) 적절 차단 | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` | rc=1 + violation reported |

**검증 도구**: Python interpreter (표준) — 신규 actual run trigger 0건 (local 한정).

#### 4.2.3 W-3 검증 (3 fixture)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-3-V1 | PASS fixture yaml parse | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml'))"` | rc=0 |
| W-3-V2 | FAIL fixture (PC-3) yaml parse | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml'))"` | rc=0 |
| W-3-V3 | FAIL fixture (AR-1) yaml parse | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml'))"` | rc=0 |
| W-3-V4 | PASS fixture = compliant entry step 시그니처 검증 (W-2-V4 답습) | (W-2-V4 와 동일) | rc=0 |
| W-3-V5 | FAIL fixture (PC-3) = `continue-on-error: true` 패턴 포함 검증 | `grep "continue-on-error: true" tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` | match ≥ 1 |
| W-3-V6 | FAIL fixture (AR-1) = fail-closed 패턴 미포함 검증 | `grep -L "if: always()" tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` 또는 본문 inspection | 패턴 미포함 |

**검증 도구**: Python `yaml` + `grep` (표준) — 신규 actual run trigger 0건 (local 한정).

### 4.3 Post-implementation 검증 (W-4 진입 *직전*)

| # | 검증 영역 | 검증 명령 | 답습 출처 |
|---|--------|--------|---------|
| POST-1 | W-1 ~ W-3 변경 line count 합산 검증 — 권고 시작점 (≤ 25 lines) | `git diff --stat HEAD` | §3.1 ~ §3.3 답습 |
| POST-2 | W-1 변경 line 中 PC-3 / AR-1 정합성 보존 검증 | `git diff HEAD .github/workflows/*.yml` + grep | §4.2.1 답습 |
| POST-3 | W-2 변경 line 中 self-check PASS 검증 | (W-2-V3 ~ W-2-V6 재실행) | §4.2.2 답습 |
| POST-4 | W-3 변경 line 中 fixture 시그니처 PASS / FAIL 보존 검증 | (W-3-V4 ~ W-3-V6 재실행) | §4.2.3 답습 |
| POST-5 | `git status` clean (변경 line all staged) + commit message 확정 | `git status` + `git log --oneline -1` | LVE 답습 |
| POST-6 | 5 영구 핵심 제약 5/5 보존 확인 — 변경 후 재검증 | (PRE-6 재실행) | LVE §5.1 답습 |
| POST-7 | Provider Liquidity 5-way 100% 보존 확인 — 변경 후 재검증 | (PRE-7 재실행) | LVE §5.2 답습 |
| POST-8 | F-금지 #1 영구 답습 확인 — 변경 후 재검증 (workflow 본문 secrets 신규 reference 0건) | `grep -r "secrets\." .github/workflows/*.yml` ↔ 답습 baseline diff | LVE §5.3 답습 |

**합산**: 8 검증 영역 × 0 신규 actual run trigger × 변경 후 재검증 한정.

### 4.4 Actual run 검증 (W-4 진입 *후*)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| RUN-1 | 3 MVP-1 workflow run conclusion = SUCCESS | `gh run list --workflow=secret-hygiene-egress-redaction.yml --branch=feature/hermes-phase0 --limit=1 --json conclusion,status` (× 3) | conclusion=success × 3 |
| RUN-2 | 3 workflow step-level 매트릭스 — PC-3 / AR-1 / Stage 4 step PASS | `gh run view <run-id> --json jobs` 답습 enumerate | jobs.conclusion=success |
| RUN-3 | 3 workflow runtime ≤ 후보 (mvp1.md §3.4.1 답습 — threshold 후보 한정 + 고정 0건) | run duration enumerate (gh CLI) | (threshold 후보 한정 — 고정 0건) |
| RUN-4 | artifact (group-d-logs / r5-logs / r1-logs) 답습 — 5 영구 핵심 제약 보존 검증 | `gh run download <run-id>` (옵션) | artifact 존재 + 본문 무결성 |
| RUN-5 | F-금지 #1 영구 답습 — secrets 사용 0건 (workflow self-check 결과 답습) | run log enumerate (gh CLI) + LVE §5.3 답습 | secrets 사용 0건 |
| RUN-6 | 4 prerequisite runs 답습 비교 — 신규 run conclusion 동등성 | 4 prerequisite runs JSON ↔ 신규 run JSON diff | conclusion 동등 |

**합산**: 6 검증 영역 × 1 actual run trigger (W-4 = `push` event on `feature/hermes-phase0` branch) × 통과 기준 enumerate.

### 4.5 검증 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `yamllint` / `actionlint` | YAML / GitHub Actions workflow syntax 검증 | 답습 한정 — 신규 도입 0건 |
| `python tools/mvp1_pc3_ar1_integration_check.py` | Stage 4 PC-3 + AR-1 integration check tool self-check | 답습 한정 — 신규 작성 0건 |
| Python `yaml.safe_load` / `py_compile` | YAML parse + Python syntax 검증 | 표준 도구 답습 |
| `grep` | PC-3 / AR-1 패턴 정합성 검증 | 표준 도구 답습 |
| `gh CLI` / GitHub Actions API | 4 prerequisite runs 답습 + 신규 actual run conclusion 검증 | 답습 한정 |
| `git status` / `git log` / `git diff` | 변경 line 검증 + commit 정합성 | 표준 git 답습 |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 4.6 검증 결과 threshold 후보 한정 매트릭스 (고정 0건)

| threshold | 본 brief 시점 |
|---------|----------|
| CI runtime per workflow | 후보 한정 (mvp1.md §3.4.1 + §4.3 + §4.4 답습) |
| PR check pass rate | 후보 한정 |
| fail-closed rate (AR-1) | 후보 한정 |
| PC-3 violation count per PR | 후보 한정 |
| integration check tool runtime | 후보 한정 (Stage 4 합의 §1.3 답습) |
| W-1 / W-2 변경 line count (≤ 25 lines 권고 시작점) | 후보 한정 (본 brief §3.1 ~ §3.3) |
| W-4 신규 actual run trigger 횟수 (1 권고 시작점) | 후보 한정 |
| **합산** | **7/7 후보 한정 — 고정 0건** |

### 4.7 검증 영역 ↔ 사용자 명시 3 금지 분리 매트릭스

| 검증 영역 | 사용자 명시 3 금지 #1 (W-5~W-10 분리) | #2 (Operational Readiness PASS) | #3 (Hermes PMO 격상) |
|----------|--------------------|--------------------|--------------------|
| Pre-implementation 검증 (PRE-1 ~ PRE-9) | ✅ 0 (read-only) | ✅ 0 | ✅ 0 |
| Per-W 검증 (W-1-V1 ~ W-3-V6) | ✅ 0 (local 한정) | ✅ 0 | ✅ 0 |
| Post-implementation 검증 (POST-1 ~ POST-8) | ✅ 0 | ✅ 0 | ✅ 0 |
| Actual run 검증 (RUN-1 ~ RUN-6) | ✅ 0 (read-only after trigger) | ✅ 0 | ✅ 0 |
| **합산** | **✅ 4 영역 × 3 = 12/12 충돌 0** | — | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **검증 방법 *권고 한정***. 실 검증 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 모든 검증 영역 = **local self-check + 답습 enumerate + 신규 actual run 1건 (W-4 한정)** — 신규 actual run trigger ≤ 1 영구 답습.

---

## 5. Actual run 조건 확정 권고 매트릭스

### 5.1 Trigger event 영역

| trigger event | 본 brief 권고 | 사용자 명시 3 금지 위반 |
|------------|----------|------------------|
| `push` event on `feature/hermes-phase0` branch | ✅ **권고 시작점** (W-1 ~ W-3 본문 변경 0건 시 = 답습 trigger; 변경 있을 시 = 신규 trigger) | ✅ 0건 |
| `pull_request` event on `feature/hermes-phase0 → main` PR | 옵션 (W-1 ~ W-3 변경 있을 시 권고) | ✅ 0건 |
| `workflow_dispatch` event (manual UI) | 옵션 (디버깅 시 권고) | ✅ 0건 |
| `pull_request_target` event | ❌ **비권고** (T2/T3 영역 = Stage 5 cycle 2 분리) | ❌ 위반 (사용자 명시 3 금지 #1 — Stage 5 분리) |
| `schedule` (cron) event | ❌ **비권고** (운영 진입 영역 = Layer E) | ❌ 위반 (사용자 명시 3 금지 #2 — Layer E) |
| `repository_dispatch` event | ❌ **비권고** (외부 trigger 영역 = ADR-008 부록 C 영역) | ❌ 위반 (사용자 명시 3 금지 #3 — Layer F) |

### 5.2 Branch 영역

| branch | 본 brief 권고 | 사용자 명시 3 금지 위반 |
|------|----------|------------------|
| `feature/hermes-phase0` (현재 작업 branch) | ✅ **권고 시작점** | ✅ 0건 |
| `main` | ❌ **비권고** (현재 stable 보존 — branch protection 미적용 영역 = AR-2 = Backlog #3 분리) | ❌ 위반 (사용자 명시 3 금지 #1 — Backlog #3 T3 영역) |
| `develop` | ❌ **비권고** (develop = MVP-1 stable 영역 — Layer C 발효 시점 답습) | ⚠️ 신중 (Layer C 답습 영역) |
| 신규 feature/* branch | 옵션 (디버깅 시 권고) | ✅ 0건 |

### 5.3 SUCCESS 조건 매트릭스

| # | SUCCESS 조건 | 통과 기준 | 답습 출처 |
|---|---------|---------|---------|
| S-1 | 3 MVP-1 workflow run conclusion = SUCCESS | conclusion=success × 3 | 4 prerequisite runs 답습 |
| S-2 | 3 workflow step-level — PC-3 / AR-1 / Stage 4 step PASS | jobs.conclusion=success | LVE §4 답습 |
| S-3 | Stage 4 integration check step (3 workflow) PASS — PASS fixture + FAIL fixture 양방향 검증 | step output `Stage 4 PC-3 + AR-1 integration OK` | 본 brief §3.1 답습 |
| S-4 | artifact (group-d-logs / r5-logs / r1-logs) 무결성 보존 | artifact 존재 + line count ≥ baseline | LVE 답습 |
| S-5 | F-금지 #1 영구 답습 — workflow self-check `workflow_secrets_usage_check.py` PASS | secrets 사용 0건 | LVE §5.3 답습 |
| S-6 | 5 영구 핵심 제약 5/5 보존 — workflow self-check 답습 | self-check 답습 | LVE §5.1 답습 |
| S-7 | Provider Liquidity 5-way 100% 보존 — workflow self-check 답습 | self-check 답습 | LVE §5.2 답습 |

### 5.4 FAILURE 조건 매트릭스 (rollback trigger)

| # | FAILURE 영역 | 대응 절차 | rollback trigger |
|---|---------|--------|----------------|
| F-1 | 1+ workflow run conclusion = FAILURE | (i) FAIL 본문 enumerate → (ii) Rollback trigger 발화 매트릭스 검토 (§6) → (iii) 사용자 명시 결정 영역 | Layer B #13 / #14 / Step Division 신규 후보 中 발화 |
| F-2 | step-level — PC-3 / AR-1 / Stage 4 step FAIL | (i) step output enumerate → (ii) PC-3 / AR-1 self-check 발화 → (iii) 사용자 명시 결정 영역 | Step Division 신규 후보 1 ~ 3 발화 |
| F-3 | Stage 4 integration check step FAIL — fixture 결과 미답습 | (i) fixture 결과 enumerate → (ii) integration check tool self-check FAIL 발화 → (iii) 사용자 명시 결정 영역 | Step Division 신규 후보 3 (integration tool self-check FAIL) 발화 |
| F-4 | F-금지 #1 영구 답습 위반 — workflow self-check FAIL | (i) **즉시 rollback** (`git revert HEAD` 권고) + 풀 3+1 + 외부 LLM 1+ 합의 진입 | F-금지 #1 위반 = 영구 답습 위반 → 풀 3+1 트리거 T-2 발화 |
| F-5 | 5 영구 핵심 제약 5/5 보존 위반 — workflow self-check FAIL | (i) **즉시 rollback** + 풀 3+1 합의 진입 | 풀 3+1 트리거 T-5 발화 |
| F-6 | Provider Liquidity 5-way 약화 — workflow self-check FAIL | (i) **즉시 rollback** + 풀 3+1 합의 진입 | 풀 3+1 트리거 T-4 발화 |
| F-7 | 신규 actual run trigger 횟수 > 1 (재실행 발생) | (i) 재실행 본문 enumerate → (ii) flaky test 가능성 검토 → (iii) 사용자 명시 결정 영역 | Layer B #15 (PR check unstable / flaky) 발화 가능성 |

### 5.5 Token / secret 영역 (F-금지 #1 영구 답습)

| 영역 | 본 brief 권고 | F-금지 #1 답습 |
|------|----------|------------|
| GitHub Actions `secrets.*` 사용 | ❌ 영구 0건 | ✅ 영구 답습 (Stage 5 cycle 1~4 자기 검증 답습) |
| GitHub Token (`GITHUB_TOKEN`) read-only 사용 | ✅ `permissions: contents: read` 답습 한정 (W-5 보강 0건) | ✅ 영구 답습 |
| 실 provider API key | ❌ 영구 0건 | ✅ 영구 답습 |
| 실 secret material commit | ❌ 영구 0건 (FAKE_TEST_SECRET marker 답습) | ✅ 영구 답습 |
| OIDC token | ❌ 본 brief 시점 미도입 | ✅ 영구 답습 |
| token rotation 정책 | ❌ 본 brief 시점 미결정 (Group α C-3 / C-4 답습 — 사용자 명시 결정 영역) | ✅ 영구 답습 |

### 5.6 Actual run 1건 권고 시작점 (본 brief 영역)

| 영역 | 본 brief 권고 |
|------|----------|
| Trigger event | `push` event |
| Branch | `feature/hermes-phase0` |
| Trigger 시점 | W-1 ~ W-3 commit 완료 (변경 line 0 시 = 답습 trigger; ≤ 25 lines 시 = 신규 trigger) |
| 횟수 | 1 (재실행 0건 권고 — flaky 발견 시 = 사용자 명시 결정 영역) |
| SUCCESS 조건 합산 | S-1 ~ S-7 = 7/7 통과 |
| FAILURE 시 대응 | F-1 ~ F-7 매트릭스 답습 |

### 5.7 본 §5 의 *범위 한계*

본 §5 = **Actual run 조건 *권고 한정***. 본 brief 시점 신규 actual run trigger = **0건 영구 답습**. Stage 4 실 구현 시점 trigger 발화 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 6. Rollback Trigger 확정 권고 매트릭스

### 6.1 Layer B 18 trigger × Stage 4 시점 발화 대응 매트릭스

| # | trigger 영역 | R-1 직접 영향 | Stage 4 시점 발화 가능성 | 발화 시 대응 절차 |
|---|---------|------------|------------------|---------------|
| 1 | secret leak observed in production | 영향 0 (MVP-3 P2) | 0건 | (영역 외 — MVP-3 분리) |
| 2 | secret leak observed in PR | 영향 0 (Step 1.4.1 PC-3 답습) | 0건 | (Stage 4 W-1~W-4 패스 시 0건) |
| 3 | provider key in `~/.config/...` | 영향 0 (R-7 영역) | 0건 | (Phase α-3 분리) |
| 4 | provider key in `~/Library/...` | 영향 0 (동상) | 0건 | (Phase α-3 분리) |
| 5 | provider key in CI runner env | 영향 0 (F-금지 #1) | 0건 | (F-금지 #1 영구 답습) |
| 6 | direct provider SDK import detected | 영향 0 (Phase α-2) | 0건 | (Phase α-2 분리) |
| 7 | URL endpoint to provider in code | 영향 0 (Phase α-1 R-4) | 0건 | (Phase α-1 분리) |
| 8 | Model name pattern match (PASS) | 영향 0 (Phase α-1 R-4) | 0건 | (Phase α-1 분리) |
| 9 | Tier-1 catalog under-detection | 영향 0 (R-4.1) | 0건 | (R-4.1 분리) |
| 10 | Tier-2/3 expansion needed | 영향 0 (Backlog #3) | 0건 | (Backlog #3 분리) |
| 11 | importlinter forbidden bypass | 영향 0 (Phase α-2 R-5) | 0건 | (Phase α-2 분리) |
| 12 | docker secret commit in PR | 영향 0 (Phase α-3 R-7) | 0건 | (Phase α-3 분리) |
| **13** | **CI step pass with violation present** | **R-1 직접 영향 (PC-3)** | **발화 가능성** (W-1 본문 변경 시) | **(i) workflow run log enumerate → (ii) PC-3 패턴 violation 본문 확인 → (iii) 변경 line `git revert HEAD` 권고 → (iv) 풀 3+1 합의 진입** |
| **14** | **CI step fail without auto-reject** | **R-1 직접 영향 (AR-1)** | **발화 가능성** (W-1 + W-2 본문 변경 시) | **(i) workflow run log enumerate → (ii) AR-1 fail-closed 패턴 누락 확인 → (iii) 변경 line `git revert HEAD` 권고 → (iv) 풀 3+1 합의 진입** |
| 15 | PR check unstable / flaky | 영향 0 (threshold 후보 한정) | 발화 가능성 (W-4 신규 actual run 시) | (i) flaky test 본문 enumerate → (ii) 재실행 횟수 ≤ 1 답습 검토 → (iii) 사용자 명시 결정 영역 |
| 16 | Hermes-originated commit detected | 영향 0 (Group I) | 0건 | (Group I 분리) |
| 17 | provider key adapter bypass | 영향 0 (Backlog #4) | 0건 | (Backlog #4 분리) |
| 18 | secret handling environment mismatch | 영향 0 (mvp1.md §5.4 IR-3) | 0건 | (MVP-3 영역 분리) |
| **합산** | **18 trigger** | **R-1 직접 영향 2 (#13, #14)** | **2 발화 가능성** (W-1 + W-2 시) + **1 발화 가능성** (#15, W-4 시) | **3 trigger × git revert + 풀 3+1 합의 진입 권고** |

### 6.2 TR-1 ~ TR-5 답습 매트릭스 (Group A 2차 합의 답습)

| TR # | 영역 | R-1 영향 | Stage 4 시점 발화 가능성 | 대응 절차 |
|----|----|--------|------------------|------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 필요 | 영향 0 (Phase α-2) | 0건 | (영역 외) |
| TR-2 | `include_external_packages` flag 변경 | 영향 0 (동상) | 0건 | (영역 외) |
| TR-3 | `root_packages` 영역 변경 | 영향 0 (동상) | 0건 | (영역 외) |
| TR-4 | `ignore_imports` 영역 변경 | 영향 0 (동상) | 0건 | (영역 외) |
| TR-5 | google.generativeai facade 영역 변경 | 영향 0 (Backlog #4) | 0건 | (영역 외) |
| **합산** | **5 trigger** | **R-1 직접 영향 0** | **0건 영구 답습** | — |

### 6.3 Step Division 신규 후보 5 trigger × Stage 4 시점 발화 대응 매트릭스

| # | 후보 trigger | 영역 | Stage 4 시점 발화 가능성 | 대응 절차 |
|---|----------|----|------------------|------|
| ND-1 | PC-3 self-check FAIL — local self-check 시 `continue-on-error: true` 발견 | R-1 영역 (W-1) | **발화 가능성** (W-1 본문 변경 시) | (i) self-check output enumerate → (ii) `continue-on-error: true` 본문 확인 → (iii) `git revert HEAD` 권고 |
| ND-2 | AR-1 self-check FAIL — local self-check 시 fail-closed 패턴 누락 발견 | R-1 영역 (W-1) | **발화 가능성** (W-1 + W-2 본문 변경 시) | (i) self-check output enumerate → (ii) `if: always()` 패턴 누락 본문 확인 → (iii) `git revert HEAD` 권고 |
| ND-3 | integration check tool self-check FAIL | R-1 영역 (W-2) | **발화 가능성** (W-2 본문 변경 시) | (i) self-check output enumerate → (ii) tool 본문 변경 확인 → (iii) `git revert HEAD` 권고 |
| ND-4 | 4 prerequisite runs JSON conclusion 미답습 발견 | Step 2 영역 (PRE-3) | 0건 (PRE-3 = read-only) | — |
| ND-5 | Local Validation Evidence 본문 누락 발견 | LVE 답습 영역 (PRE-4) | 0건 (PRE-4 = read-only) | — |
| **합산** | **5 후보** | — | **3 발화 가능성** (W-1 + W-2 시) | **3 trigger × git revert 권고** |

### 6.4 Stage 4 신규 후보 trigger (W-4 actual run FAIL 영역)

| 후보 trigger | 영역 | Stage 4 시점 발화 가능성 | 대응 절차 |
|----------|----|------------------|------|
| W-4 신규 actual run FAILURE | W-4 영역 | **발화 가능성** (W-4 trigger 시) | (i) workflow run log enumerate → (ii) FAIL step 본문 확인 → (iii) §5.4 F-1 ~ F-7 매트릭스 적용 → (iv) 사용자 명시 결정 영역 |
| W-4 신규 actual run flaky (재실행 ≥ 1) | W-4 영역 | **발화 가능성** (W-4 후) | (i) Layer B #15 답습 → (ii) flaky 본문 enumerate → (iii) 사용자 명시 결정 영역 |
| W-4 신규 actual run F-금지 #1 위반 발견 | W-4 영역 | 0건 (F-금지 #1 영구 답습 + self-check workflow_secrets_usage_check 답습) | (영구 답습) |
| W-4 신규 actual run 5 영구 핵심 제약 보존 위반 발견 | W-4 영역 | 0건 (LVE §5.1 답습 + self-check 답습) | (영구 답습) |
| W-4 신규 actual run Provider Liquidity 5-way 약화 발견 | W-4 영역 | 0건 (LVE §5.2 답습 + R-1 = vendor-agnostic 답습) | (영구 답습) |

### 6.5 합산 + 발화 영역 매트릭스

| 영역 | 합계 | R-1 직접 영향 | Stage 4 시점 발화 가능성 | 대응 절차 합산 |
|------|----|------------|------------------|------------|
| Layer B 18 trigger | 18 | 2 (#13, #14) + 1 (#15) | 3 (W-1 + W-2 + W-4) | git revert + 풀 3+1 진입 |
| TR-1 ~ TR-5 | 5 | 0 | 0건 영구 답습 | — |
| Step Division 신규 후보 5 | 5 | 5 | 3 (W-1 + W-2) | git revert + 풀 3+1 진입 |
| Stage 4 신규 후보 (W-4 영역) | 2 (실 발화) + 3 (영구 답습) | 2 (W-4) | 2 (W-4) | §5.4 매트릭스 적용 + 사용자 명시 결정 영역 |
| **합산** | **30 trigger** | **R-1 직접 영향 9** | **8 발화 가능성** (W-1 + W-2 + W-4 본문 변경 / actual run 시 — 신중) | **8 trigger × git revert 또는 §5.4 적용 권고** |

### 6.6 Rollback 절차 권고 매트릭스

| 절차 | 영역 | 권고 |
|----|----|----|
| (i) Rollback decision | trigger 발화 시 판단 | 사용자 명시 결정 영역 (자동 rollback 0건) |
| (ii) `git revert HEAD` | 가장 안전 — 변경 line 만 revert + 합의 본문 보존 | **권고 시작점** |
| (iii) `git revert HEAD~N..HEAD` (N ≥ 1) | 다중 commit revert | 옵션 (W-1 + W-2 + W-3 multi-commit 시) |
| (iv) `git reset --hard HEAD~N` | 강제 reset (이력 변경) | ❌ **비권고** (R-4 history rewrite layer 영역 = 별도 합의 필요) |
| (v) 신규 `fix:` commit (revert 없이 forward fix) | 변경 line forward fix | 옵션 (rollback 영역 미발화 시 — micro patch 한정) |
| (vi) commit 분리 (rollback commit + 합의 보고서 commit) | 단계별 답습 | **권고 시작점** (Stage 4 cycle 답습) |

### 6.7 Stage 4 신규 후보 trigger 등록 영역 (정식 등록 0건 — Backlog #5 분리)

| 후보 trigger | 영역 | 본 brief 시점 |
|----------|----|----------|
| W-4 신규 actual run FAILURE trigger | Stage 4 영역 | **후보 한정** (정식 등록 0건 — Backlog #5 ADR-012 §2.2 분리) |
| W-4 신규 actual run flaky trigger | Stage 4 영역 | **후보 한정** |
| W-1/W-2 micro-patch self-check FAIL trigger (5 영구 핵심 제약 / Provider Liquidity / F-금지 #1) | Stage 4 영역 | **후보 한정** |
| **합산** | — | **3 후보 한정 — 정식 등록 0건** |

### 6.8 본 §6 의 *범위 한계*

본 §6 의 어떤 항목도:

- (i) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 어느 것도 *발화* 시키지 않으며,
- (ii) threshold 어느 것도 *고정* 시키지 않으며 (5/5 후보 한정 영구 답습),
- (iii) 합의 본문 어느 줄도 *변경* 하지 않으며,
- (iv) ledger entry enum 어느 것도 *정식 등록* 시키지 않으며 (Backlog #5 분리),
- (v) Rollback 절차 어느 것도 *자동 발화* 시키지 않는다 (사용자 명시 결정 영역).

---

## 7. 사용자 명시 3 금지 + 영구 5 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 3 금지 영역 위반 0건 영구 답습 매트릭스

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 명시 결정 영역) |
|---|---------|---------------|------------------------------------|
| #1 | W-5 ~ W-10 영역 진입 (`permissions:` / Required check / PC-4 / AR-2 / AR-3 / Stage 5) | ✅ 0건 (Backlog #1+#2 / Backlog #3 T3 / Stage 5 분리 영구 답습) | ✅ 0건 (DRAFT 영역) |
| #2 | Operational Readiness PASS (Layer E) 선언 | ✅ 0건 (MVP-6 영역 분리 영구 답습) | ✅ 0건 |
| #3 | Hermes PMO 격상 (Layer F) | ✅ 0건 (ADR-008 부록 C 12 조건 미충족) | ✅ 0건 |
| **합산** | **3** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** |

### 7.2 영구 5 금지 영역 × 본 brief 시점 / Stage 4 실 구현 시점 분리 매트릭스

| # | 영구 금지 영역 | 본 brief 시점 | Stage 4 실 구현 시점 (사용자 명시 결정 후) |
|---|---------|----------|------------------------------------|
| #1 | CI workflow 변경 | ✅ 0건 (1593줄 답습 보존) | **해소 영역** (W-1/W-2/W-3 micro-patch 권고 시작점 ≤ 25 lines) |
| #2 | runtime code 변경 | ✅ 0건 (`src/` + facade.py 41줄 placeholder 답습) | ✅ 0건 영구 보존 (Backlog #4 분리) |
| #3 | actual run 재실행 | ✅ 0건 (4 prerequisite runs 답습 한정) | **해소 영역** (W-4 신규 actual run 1건 권고) |
| #4 | Operational Readiness PASS | ✅ 0건 | ✅ 0건 영구 보존 (사용자 명시 3 금지 #2) |
| #5 | Hermes PMO 격상 | ✅ 0건 | ✅ 0건 영구 보존 (사용자 명시 3 금지 #3) |
| **합산** | **5** | **5/5 영구 답습** | **2 해소 + 3 영구 보존** |

### 7.3 Backlog 분리 매트릭스

| Backlog | 영역 | 본 brief 영역 |
|---------|----|----------|
| Backlog #1 (PC-4 local pre-commit hook 활성화) | `.pre-commit-config.yaml` 신설 + `tools/doctor.py` | ❌ 본 brief 영역 외 (사용자 명시 3 금지 #1) |
| Backlog #2 (dev 환경 강제 + pre-commit install 의무화) | dev 환경 검증 강제 + `pre-commit install` 의무화 | ❌ 본 brief 영역 외 (사용자 명시 3 금지 #1) |
| Backlog #3 T3 (AR-2 branch protection + AR-3 자동 revert bot) | branch protection API + CODEOWNERS + bot 설정 | ❌ 본 brief 영역 외 (사용자 명시 3 금지 #1) |
| Backlog #4 (facade.py real 본문 작성) | `src/adapters/llm/facade.py` real 본문 | ❌ 본 brief 영역 외 (영구 5 금지 #2) |
| Backlog #5 (event enum 정식 등록 + ledger entry 정식 등록) | ADR-012 §2.2 영역 | ❌ 본 brief 영역 외 (후보 한정) |
| Backlog #6 (Hermes PMO 격상 영역) | ADR-008 부록 C 12 조건 미충족 영역 | ❌ 본 brief 영역 외 (사용자 명시 3 금지 #3) |
| Stage 5 (G3-7 4 항목) | secret reset rotate / fork PR / pull_request_target / commit signing | ❌ 본 brief 영역 외 (사용자 명시 3 금지 #1 — Stage 4 후속 권고 영역) |

### 7.4 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 3 금지 영역 + 영구 5 금지 영역 어느 것도 *해소* 시키지 않으며, Backlog 분리 영역 어느 것도 *통합* 시키지 않는다.

---

## 8. 합산 389 합의 조건 답습 매트릭스

### 8.1 합산 합의 조건 매트릭스

| 합의 | commit | 조건 수 | 본 brief 변경 |
|------|-------|------|-----------|
| Group α (Backlog #3) | `4880e88` | 12 (C-1 ~ C-12) | 0건 |
| Backlog #6 우선 진입 | `c7ddfdd` | 11 (C-α-1 ~ C-α-11) | 0건 |
| Phase α-1 (R-4) | `1b3090b` | 15 (C-β-1 ~ C-β-15) | 0건 |
| Phase α-2 (R-5) | `6a79247` | 26 (C-γ-1 ~ C-γ-26) | 0건 |
| Phase α-3 (R-7) | `3f6306d` | 28 (C-δ-1 ~ C-δ-28) | 0건 |
| Phase α-4 (R-1) — 직전 | `e59a565` | 29 (C-ε-1 ~ C-ε-29) | 0건 |
| Layer C 발효 | `eb01bc4` | 30 (C-ι-1 ~ C-ι-30) | 0건 |
| Layer D 재진입 평가 | `951a5b1` | 25 (C-λ-1 ~ C-λ-25) | 0건 |
| Stage 1 — Phase α 통합 계획 | `542e77e` | 25 (C-μ-1 ~ C-μ-25) | 0건 |
| Stage 2 — α-1+2+3 1순위 계획 | `88ccf79` | 25 (C-ν-1 ~ C-ν-25) | 0건 |
| Stage 3 (parallel) — α-1+2+3 actual entry | `7917e4a` | 25 (C-ξ-1 ~ C-ξ-25) | 0건 |
| Phase α-4 R-1 진입 조건 점검 | `1c365e7` | 33 (C-π-1 ~ C-π-33) | 0건 |
| Phase α-4 R-1 Step Division | `52a05cb` | 38 (C-ρ-1 ~ C-ρ-38) | 0건 |
| Phase α-4 R-1 LVE | `b264580` | 31 (C-σ-1 ~ C-σ-31) | 0건 |
| **Phase α-4 R-1 Stage 3 실 진입 여부** | **`d3f6d59`** | **36 (C-τ-1 ~ C-τ-36)** | **0건** ✅ |
| **합산** | **15 합의** | **389 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| C-τ-1 (Stage 3 brief 11 영역 점검 100% 채택) | ✅ 답습 한정 |
| C-τ-2 (Stage 3 framing 정합성 = "Should we enter actual implementation now?") | ✅ 본 brief = Stage 4 lockdown framing 답습 |
| C-τ-3 (R-1 현재 상태 매트릭스 = technical pre-conditions 모두 충족) | ✅ 본 brief §1.5 답습 |
| C-τ-4 (Stage 4 "실 구현" 정의 = evidence-only → 운영 진입) | ✅ 답습 한정 |
| C-τ-5 (5 금지 해소 매트릭스 = Stage 4 시점 #1 + #3 해소 + #2/#4/#5 영구 보존) | ✅ 본 brief §0.3 + §7.2 답습 |
| C-τ-6 (Pro 9/9 채택) | ✅ 답습 한정 |
| C-τ-7 (Con 9/9 채택) | ✅ 답습 한정 |
| C-τ-8 (Stage 4 작업 enumerate — W-1~W-4 최소 영역 권고 + W-5~W-10 분리 권고) | ✅ 본 brief §2.1 + §2.2 답습 |
| C-τ-9 ~ C-τ-36 (rollback trigger 매트릭스 + 합의 형태 권고 + 사용자 명시 5 금지 영구 답습 등) | ✅ 본 brief §6 + §9 + §7 답습 |
| C-σ-29 (실 진입 = 사용자 명시 결정 영역) | ✅ 본 brief = lockdown 권고 한정 |
| C-ρ-37 (Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 *권고 한정*) | ✅ 본 brief 답습 한정 |
| C-π-x (5 진입 적격성 5/5 충족 + 이중 evidence 충족) | ✅ 답습 한정 |
| C-ε-9 / C-ε-10 (Phase α-4 실 진입 = 사용자 명시 결정 영역 + R-1 영역 7 artifacts × 1593줄 변경 0건) | ✅ 답습 한정 |

### 8.3 본 §8 의 *범위 한계*

본 §8 = **389 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = §11.2 (C-υ-1 ~ C-υ-N) 한정 — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정 (합의 보고서 작성 시 정식 등록).

---

## 9. 합의 형태 권고 + 풀 3+1 승격 트리거 분석

### 9.1 본 brief 자체 합의 형태 권고

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| (a) Reviewer-only 단축 합의 | 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ⚠️ **부분 적격** — 본 brief = DRAFT 한정 + 5 금지 해소 0건 + W-1 ~ W-4 자동 실행 0건 (그러나 본 brief 발효 후 Stage 4 실 구현 = 5 금지 #1 + #3 해소 → T-2 발화) |
| **(b) 풀 3+1 합의** | 트리거 中 1+ 발화 | ✅ **권고** — Stage 4 실 구현 *lockdown* = T-2 (5 금지 영역 해소 권고) 발화 → 본 brief 자체 = 풀 3+1 트리거 발화 영역 |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | ⚠️ 부분 적격 — W-5 ~ W-10 분리 명시 + Stage 5 분리 명시 → T-6 / T-10 / T-13 미발화 예상 |

**권고**: 본 brief = **(b) 풀 3+1 합의 (필수)** — Stage 4 실 구현 lockdown 권고 = 5 금지 #1 + #3 해소 권고 발효 → T-2 발화 → 풀 3+1 트리거 발화. 외부 LLM 1+ blind 의뢰 = W-5~W-10 분리 명시로 미발화 영역 (옵션).

### 9.2 풀 3+1 승격 트리거 검토 매트릭스 (본 brief 시점)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 본 brief 가 합산 389 합의 조건 中 1+ *재결정* 권고 | 0건 — 답습 한정 |
| **T-2** | **본 brief 가 사용자 명시 영구 5 금지 영역 中 1+ *해소* 권고** | **발화** — 본 brief = Stage 4 실 구현 시점 #1 (CI workflow 변경) + #3 (actual run 재실행) 해소 권고 한정 (본 brief 시점 자체 해소 0건이지만 lockdown 권고 = 해소 권고 영역) |
| T-3 | 본 brief 가 Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 |
| T-4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | 0건 |
| T-5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | 0건 |
| T-6 | 본 brief 가 T3 영역 진입 권고 | 0건 — Backlog #3 분리 명시 |
| T-7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | 0건 |
| T-8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 | 0건 |
| T-9 | 본 brief 가 Hermes upstream root of trust 변경 권고 | 0건 |
| T-10 | 본 brief 가 PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0건 — §2.2 + §7.3 분리 명시 |
| T-11 | 본 brief 가 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | 0건 |
| T-12 | 본 brief 가 신규 workflow 신설 / `pull_request_target` 도입 권고 | 0건 |
| T-13 | 본 brief 가 Stage 5 (G3-7) 자동 진입 권고 | 0건 — §2.2 W-10 분리 명시 |
| T-14 | 본 brief 가 Phase α-1 / α-2 / α-3 actual run 재실행 권고 | 0건 |
| T-15 | 본 brief 가 α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 합의 본문 변경 권고 | 0건 |
| T-16 | 본 brief 가 Stage 4 자동 실 구현 발효 권고 | 0건 — 본 brief = lockdown DRAFT 한정 (실 구현 = 사용자 명시 결정 영역) |
| **합산** | **16** | **1/16 발화 (T-2)** — **풀 3+1 합의 트리거 발화 확정** |

### 9.3 외부 LLM 1+ blind 의뢰 적격성 매트릭스

| 영역 | 본 brief 적격성 |
|------|------------|
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | 부분 적격 — Stage 4 영역 = 5 금지 해소 권고 = 신중 영역 |
| ADR-011 §2.4 T2 영역 (외부 LLM 응답 = 입력 한정) | 답습 한정 — 외부 LLM 의뢰 시 응답 = 입력 한정 (Group α C-11 답습) |
| 본 brief 권고 | **옵션** — W-1 ~ W-4 최소 영역 분리 명시 + W-5 ~ W-10 분리 명시 → T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 (옵션 권고 — 사용자 명시 결정 영역) |

### 9.4 본 §9 의 *범위 한계*

본 §9 = **합의 형태 권고 한정**. 본 brief 자체 = 풀 3+1 합의 트리거 발화 (T-2) → **풀 3+1 합의 적격** — 외부 LLM 1+ blind 의뢰 = 옵션 (W-1~W-4 최소 영역 분리 명시로 미발화 영역).

---

## 10. 본 brief 자체 금지 + brief 발효 후 의무 금지

### 10.1 본 brief 작성 시점 금지 사항

- ❌ **W-5 ~ W-10 영역 진입** (사용자 명시 3 금지 #1) — Backlog #1+#2 / Backlog #3 T3 / Stage 5 분리
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 3 금지 #2)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 3 금지 #3)
- ❌ **CI workflow 변경** (영구 5 금지 #1) — R-1 7 artifacts × 1593줄 답습 보존
- ❌ **runtime code 변경** (영구 5 금지 #2) — `src/` + facade.py 41줄 placeholder 답습
- ❌ **actual run 재실행** (영구 5 금지 #3) — 4 prerequisite runs 답습 한정
- ❌ Phase α-4 Stage 4 실 구현 자동 진입 (본 brief = *lockdown 권고 한정*)
- ❌ Phase α-1 / α-2 / α-3 자동 재진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 합의 본문 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 trigger 자동 발화
- ❌ 합산 389 합의 조건 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ event enum 정식 등록 (Backlog #5 분리)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ commit signing / `pull_request_target` workflow 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile 변경
- ❌ Production `docker-compose.yml` 신설 / 변경
- ❌ 실 secret material commit
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ W-1 / W-2 / W-3 / W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger *최종 확정 발효* (사용자 명시 결정 영역 한정)

### 10.2 본 brief 발효 *후* 의무 금지 사항 (사용자 명시 결정 영역)

본 brief 발효 후 *자동 진입 영역* (사용자 명시 결정 *전*):

- ❌ Phase α-4 Stage 4 실 구현 자동 진입 0건 (사용자 명시 결정 후 진입)
- ❌ W-1 / W-2 / W-3 본문 변경 자동 진입 0건
- ❌ W-4 신규 actual run 자동 trigger 0건
- ❌ 합의 보고서 작성 자동 진입 0건 (사용자 명시 합의 형태 결정 후)
- ❌ W-5 ~ W-10 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 자동 진입 0건
- ❌ Backlog #1+#2 / Backlog #3 / Stage 5 자동 진입 0건
- ❌ 합산 389 합의 조건 자동 변경 0건
- ❌ Layer C / D / E / F 재발효 / 재선언 / 발효 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → 풀 3+1 합의 진입** (T-2 발화 → 풀 3+1 필수) | 풀 3+1 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → **Reviewer-only 단축 합의 진입** (T-2 발화 영역 — 사용자 명시 단축 결정 시) | Reviewer-only 단축 합의 보고서 작성 (사용자 명시 권위 단축 결정 영역) |
| (E) | 본 brief 승인 → **풀 3+1 + 외부 LLM 1+ 합의** (Group α C-14 답습 — W-5 ~ W-10 영역 확대 시 권고) | 풀 3+1 + 외부 LLM blind 의뢰 진입 |
| (F) | 본 brief 보류 → Stage 4 실 구현 직접 진입 brief 작성 (lockdown 우회) | 실 구현 brief 별도 작성 |
| (G) | 본 brief 보류 → Backlog #1+#2 / Backlog #3 / Stage 5 우선 진입 | Backlog 中 사용자 결정 영역 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 11.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 Stage 4 W-1 ~ W-4 *lockdown 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 Stage 4 W-1~W-4 lockdown (DRAFT, 본 commit)        ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → 풀 3+1 합의 보고서 작성 (옵션 (A), T-2 발화 → 풀 3+1 필수)
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-1 micro-patch (3 MVP-1 workflow) brief 작성           ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-2 micro-patch (integration tool) brief 작성             ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-3 micro-patch (3 fixture) brief 작성                    ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-4 신규 actual run trigger 진입 brief                  ← 별도 결정 영역
```

### 11.2 본 brief 새 조건 후보 (Reviewer-only / 풀 3+1 합의 시 정식 등록)

본 brief 합의 시 새 조건 enumerate 후보 (C-υ-1 ~ C-υ-N):

| # | 조건 후보 | 본 brief 영역 |
|---|--------|-----------|
| C-υ-1 | 본 brief (Phase α-4 Stage 4 W-1~W-4 lockdown DRAFT, 약 750줄) 11 영역 점검 결과 100% 채택 | §0.1 답습 |
| C-υ-2 | Stage 4 lockdown framing 정합성 채택 — Stage 3 §10.1 답습 명시 ("*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?") | §1.3 + §1.4 답습 |
| C-υ-3 | W-1 ~ W-4 최소 영역 권고 채택 — W-5 ~ W-10 분리 명시 | §2.1 + §2.2 답습 |
| C-υ-4 | 사용자 명시 3 금지 영역 5/5 영구 답습 (작성 시점 + 발효 후) | §7.1 답습 |
| C-υ-5 | 영구 5 금지 영역 × Stage 4 시점 해소 매트릭스 채택 — 본 brief 시점 0/5 해소 / Stage 4 시점 2 해소 (#1 + #3) + 3 영구 보존 (#2 + #4 + #5) | §7.2 답습 |
| C-υ-6 | W-1 수정 파일 권고 채택 — 3 MVP-1 workflow × 변경 line ≤ 15 lines micro-patch 권고 시작점 | §3.1 답습 |
| C-υ-7 | W-2 수정 파일 권고 채택 — integration tool × 변경 line ≤ 5 lines micro-patch 권고 시작점 | §3.2 답습 |
| C-υ-8 | W-3 수정 파일 권고 채택 — 3 fixture × 변경 line 0 권고 시작점 | §3.3 답습 |
| C-υ-9 | W-4 신규 actual run trigger 권고 채택 — `push` event on `feature/hermes-phase0` branch + 횟수 1 | §3.4 + §5.6 답습 |
| C-υ-10 | R-4 / R-5 / R-7 / `src/` / docker block / placeholder 본문 변경 0건 영구 답습 | §3.5 답습 |
| C-υ-11 | Pre-implementation 검증 (PRE-1 ~ PRE-9) 9 영역 채택 | §4.1 답습 |
| C-υ-12 | W-1 검증 (W-1-V1 ~ W-1-V7) 7 영역 채택 | §4.2.1 답습 |
| C-υ-13 | W-2 검증 (W-2-V1 ~ W-2-V6) 6 영역 채택 | §4.2.2 답습 |
| C-υ-14 | W-3 검증 (W-3-V1 ~ W-3-V6) 6 영역 채택 | §4.2.3 답습 |
| C-υ-15 | Post-implementation 검증 (POST-1 ~ POST-8) 8 영역 채택 | §4.3 답습 |
| C-υ-16 | Actual run 검증 (RUN-1 ~ RUN-6) 6 영역 채택 | §4.4 답습 |
| C-υ-17 | 검증 도구 영역 — `yamllint` / `actionlint` / `python` / `grep` / `gh CLI` / `git` 표준 도구 답습 한정 + 신규 도입 0건 | §4.5 답습 |
| C-υ-18 | threshold 후보 한정 매트릭스 채택 — 7/7 후보 한정 + 고정 0건 영구 답습 | §4.6 답습 |
| C-υ-19 | Actual run trigger event 권고 — `push` event 권고 시작점 + `pull_request` 옵션 + `pull_request_target` / `schedule` / `repository_dispatch` 비권고 | §5.1 답습 |
| C-υ-20 | Actual run branch 권고 — `feature/hermes-phase0` 권고 시작점 + `main` 비권고 (AR-2 영역 분리) | §5.2 답습 |
| C-υ-21 | SUCCESS 조건 매트릭스 (S-1 ~ S-7) 7 영역 채택 | §5.3 답습 |
| C-υ-22 | FAILURE 조건 매트릭스 (F-1 ~ F-7) 7 영역 채택 | §5.4 답습 |
| C-υ-23 | Token / secret 영역 F-금지 #1 영구 답습 | §5.5 답습 |
| C-υ-24 | Rollback Trigger 매트릭스 — Layer B 18 + TR-1~TR-5 + Step Division 신규 후보 5 + Stage 4 신규 후보 2 = 30 trigger 답습 | §6.1 ~ §6.4 답습 |
| C-υ-25 | Stage 4 시점 발화 가능성 8 (W-1 + W-2 + W-4 시) — git revert + 풀 3+1 진입 권고 | §6.5 답습 |
| C-υ-26 | Rollback 절차 권고 — `git revert HEAD` 권고 시작점 + `git reset --hard` 비권고 | §6.6 답습 |
| C-υ-27 | Stage 4 신규 후보 trigger 3 정식 등록 0건 (Backlog #5 분리) | §6.7 답습 |
| C-υ-28 | Backlog 분리 매트릭스 — Backlog #1+#2 / Backlog #3 T3 / Backlog #4 / Backlog #5 / Backlog #6 / Stage 5 분리 영구 답습 | §7.3 답습 |
| C-υ-29 | 합산 389 합의 조건 답습 매트릭스 변경 0건 | §8 답습 |
| C-υ-30 | 합의 형태 권고 — 본 brief 자체 = 풀 3+1 합의 (T-2 발화) 권고 + 외부 LLM 1+ 옵션 (W-5~W-10 분리 명시로 미발화) | §9.1 ~ §9.3 답습 |
| C-υ-31 | 본 brief 자체 금지 ≥ 40 + 본 brief 발효 후 의무 금지 ≥ 10 영구 답습 | §10 답습 |
| C-υ-32 | 다음 단계 옵션 (A) ~ (I) 사용자 결정 영역 — 권고 시작점 = (A) brief 그대로 승인 → 풀 3+1 합의 진입 | §11 답습 |
| C-υ-33 | 본 brief 메타 검증 ≥ 28 항목 | §12 답습 |
| C-υ-34 | 5 영구 핵심 제약 5/5 보존 답습 (Hermes ≠ root of trust / 단일 source-of-truth / 수단·목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) | LVE §5.1 답습 강화 |
| C-υ-35 | Provider Liquidity 5-way 100% 보존 답습 | LVE §5.2 답습 강화 |
| C-υ-36 | F-금지 #1 영구 답습 (GitHub Actions secrets 사용 0건 + 실 API key / provider SDK / 외부 API 호출 0건) | LVE §5.3 답습 강화 |
| C-υ-37 | W-1 ~ W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger *최종 확정 발효 0건* (사용자 명시 결정 영역 한정) | §0.6 답습 |
| **합산** | **37 조건 후보** | — |

### 11.3 본 §11 의 *범위 한계*

본 §11 = *결정 옵션 + 새 조건 후보 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 새 조건 발효 = 합의 보고서 작성 시 정식 등록 (Reviewer-only 또는 풀 3+1) — 본 brief 단독 = 새 조건 발효 0건.

---

## 12. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("Phase α-4 Stage 4 진입 brief를 작성해주세요" → "W-1~W-4 최소 영역 lockdown DRAFT 작성") |
| 사용자 명시 3 금지 답습 | ✅ (3/3 — W-5~W-10 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| 영구 5 금지 답습 | ✅ (5/5 — CI workflow 변경 0건 / runtime code 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Stage 3 합의 답습 (`d3f6d59`) | ✅ (36 조건 C-τ-1 ~ C-τ-36 변경 0건) |
| LVE 합의 답습 (`b264580`) | ✅ (31 조건 C-σ-1 ~ C-σ-31 변경 0건) |
| Step Division 합의 답습 (`52a05cb`) | ✅ (38 조건 C-ρ-1 ~ C-ρ-38 변경 0건) |
| α-4 진입 조건 점검 합의 답습 (`1c365e7`) | ✅ (33 조건 C-π-1 ~ C-π-33 변경 0건) |
| 직전 α-4 합의 답습 (`e59a565`) | ✅ (29 조건 C-ε-1 ~ C-ε-29 변경 0건) |
| α-1+2+3 local validation evidence 답습 (`7b3d40a`) | ✅ (486줄 본문 변경 0건 + 12/12 PASS 답습) |
| LVE 본문 답습 (`4ce5a0b`) | ✅ (583줄 본문 변경 0건 + 51/51 PASS 답습) |
| Stage 3 brief 본문 답습 (`27351ce`) | ✅ (722줄 본문 변경 0건) |
| 합산 389 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 parallel 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 여부 36) |
| Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 실 진입 여부 본문 변경 | ✅ 0건 |
| §5.5 9 sub-수단 본문 채택 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| W-1 / W-2 / W-3 본문 변경 | ✅ 0건 (본 brief = lockdown 권고 한정) |
| W-4 신규 actual run trigger | ✅ 0건 (본 brief 시점 영구 답습) |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| Layer B 18 Rollback Trigger + TR-1 ~ TR-5 + Step Division 신규 후보 5 + Stage 4 신규 후보 2 발화 | ✅ 0/30 발화 (본 brief 시점) |
| 풀 3+1 트리거 발화 | ✅ 1/16 발화 (T-2 — Stage 4 lockdown 권고 = 5 금지 #1 + #3 해소 권고 영역) → **풀 3+1 합의 적격** |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| Stage 4 실 구현 자동 진입 | ✅ 0건 (본 brief 영역 외) |
| W-1 ~ W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger *최종 확정 발효* | ✅ 0건 (사용자 명시 결정 영역) |
| Stage 4 lockdown framing 명시 (Stage 3 §10.1 답습) | ✅ §1.3 + §1.4 답습 |

---

## 13. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-4 R-1 Stage 3 실 진입 여부 검토 합의 (`d3f6d59` 후속 27 APPROVE AS BRIEF — Reviewer-only 단축, 36 조건 C-τ-1 ~ C-τ-36) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) Stage 4 *실 진입 lockdown* 한정 brief 준비안 (DRAFT)** = **Phase α-4 자체의 Stage 4 lockdown framing** (Stage 3 §10.1 권고 시작점 답습 명시) — "*What exactly* will Stage 4 W-1 ~ W-4 do, with which 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger, BEFORE any actual implementation begins?". **사용자 명시 3 금지** (W-5 ~ W-10 분리 / Operational Readiness PASS / Hermes PMO 격상) 3/3 답습 + **영구 5 금지** (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **W-1 ~ W-4 작업 영역 확정 권고 매트릭스** (W-1 = 3 MVP-1 workflow / W-2 = integration check tool / W-3 = 3 fixture / W-4 = 신규 actual GitHub Actions run trigger) + **W-5 ~ W-10 분리 매트릭스 6/6 위반 0건 영구 답습**. **수정 파일 확정 권고 매트릭스** — W-1 (3 MVP-1 workflow 1206줄 × ≤ 15 lines micro-patch 권고 시작점) + W-2 (integration tool 298줄 × ≤ 5 lines micro-patch 권고 시작점) + W-3 (3 fixture 89줄 × 0 lines 권고 시작점) + W-4 (수정 파일 0건 — `push` event on `feature/hermes-phase0` branch trigger 한정) — **R-4 / R-5 / R-7 / `src/` / docker block / placeholder 본문 변경 0건 영구 답습**. **검증 방법 확정 권고 매트릭스** — Pre-implementation 검증 9 영역 (PRE-1 ~ PRE-9) + W-1 검증 7 영역 (yamllint + PC-3 / AR-1 정합성 grep) + W-2 검증 6 영역 (`--list-checks` + `--mode integration` + PASS / FAIL fixture 양방향) + W-3 검증 6 영역 (yaml parse + 시그니처 검증) + Post-implementation 검증 8 영역 (POST-1 ~ POST-8) + Actual run 검증 6 영역 (RUN-1 ~ RUN-6) = 합산 42 검증 영역 × **신규 actual run trigger ≤ 1 (W-4 한정)** 영구 답습. **Actual run 조건 확정 권고 매트릭스** — Trigger event = `push` event 권고 시작점 (`pull_request_target` / `schedule` / `repository_dispatch` 비권고) + Branch = `feature/hermes-phase0` 권고 시작점 (`main` 비권고 = AR-2 = Backlog #3 분리) + SUCCESS 조건 7 (S-1 ~ S-7) + FAILURE 조건 7 (F-1 ~ F-7) + Token / secret 영역 F-금지 #1 영구 답습. **Rollback Trigger 확정 권고 매트릭스** — Layer B 18 + TR-1~TR-5 + Step Division 신규 후보 5 + Stage 4 신규 후보 2 = **합산 30 trigger × 본 brief 시점 0/30 발화 영구 답습** + Stage 4 시점 8 발화 가능성 (W-1 + W-2 + W-4 시 = Layer B #13/#14/#15 + Step Division 신규 후보 ND-1/ND-2/ND-3 + Stage 4 W-4 신규 후보 2) — **git revert + 풀 3+1 합의 진입** 권고. **합의 형태 권고**: 본 brief 자체 = **(b) 풀 3+1 합의 필수** (T-2 발화 — Stage 4 lockdown 권고 = 5 금지 #1 + #3 해소 권고 영역) + 외부 LLM 1+ 옵션 (W-5 ~ W-10 분리 명시로 T-6/T-10/T-13 미발화 영역). **사용자 명시 3 금지 + 영구 5 금지 × 본 brief 분리 매트릭스 — 3/3 + 5/5 영구 답습 (작성 시점 + 발효 후 자동 진입 영역 모두 0건)**. **합산 389 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 parallel 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 여부 36). **본 brief 자체 금지 ≥ 45 + 본 brief 발효 후 의무 금지 ≥ 10** enumerate. **본 brief 새 조건 후보 ≥ 37 (C-υ-1 ~ C-υ-37)** — 합의 보고서 작성 시 정식 등록. **본 brief 는 Phase α-4 Stage 4 W-1 / W-2 / W-3 / W-4 어느 작업도 *실행* 시키지 않으며, R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며, `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며, 사용자 명시 3 금지 + 영구 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 389 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / W-1 ~ W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger 어느 것도 *최종 확정 발효* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — (A) brief 그대로 승인 → 풀 3+1 합의 (권고 시작점 — T-2 발화) / (B) brief 수정 / (C) 부분 채택 / (D) Reviewer-only 단축 합의 (사용자 명시 단축 결정 시) / (E) 풀 3+1 + 외부 LLM 1+ / (F) lockdown 우회 실 구현 직접 진입 / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.

---

**작성일**: 2026-05-18
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §11 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **W-5 ~ W-10 영역 진입 0건** (Backlog #1+#2 / Backlog #3 T3 / Stage 5 분리)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ **CI workflow 변경 0건** (R-1 7 artifacts × 1593줄 답습 보존)
- ❌ **runtime code 변경 0건** (`src/` + facade.py 41줄 placeholder 답습 보존)
- ❌ **actual run 재실행 0건** (4 prerequisite runs PASS 답습 한정)
- ❌ Phase α-4 Stage 4 실 구현 자동 진입 0건 (본 brief = lockdown 권고 한정)
- ❌ W-1 / W-2 / W-3 본문 변경 0건 + W-4 신규 actual run trigger 0건 (본 brief 시점)
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 389 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence (`7b3d40a`) 본문 변경 0건
- ❌ α-4 진입 조건 점검 (`1c365e7`) + Step Division (`52a05cb`) + LVE (`4ce5a0b` + `b264580`) + Stage 3 (`27351ce` + `d3f6d59`) 본문 변경 0건
- ❌ Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 본문 변경 0건
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건
- ❌ Phase α-1 / α-2 / α-3 자동 재진입 0건
- ❌ Phase β / γ 자동 진입 0건
- ❌ PC-4 / AR-2 / AR-3 / Stage 5 자동 진입 0건
- ❌ Layer C / D / E / F 재발효 / 재선언 / 발효 0건
- ❌ branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 도입 0건
- ❌ 신규 workflow 신설 / `pull_request_target` 도입 0건
- ❌ 3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 0건
- ❌ Hermes upstream Dockerfile 변경 0건
- ❌ Production `docker-compose.yml` 신설 / 변경 0건
- ❌ 실 secret material commit 0건 (FAKE_TEST_SECRET marker 답습)
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 0건
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경 0건
- ❌ R-7 docker secret block / image layer check / restart recovery 본문 변경 0건
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건
- ❌ threshold *고정* 0건 (7/7 후보 한정)
- ❌ event enum 정식 등록 0건 (Backlog #5 분리)
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 5 / Stage 4 신규 후보 2 = 30 trigger 자동 발화 0건 (30/30)
- ❌ 풀 3+1 트리거 자동 발화 0/16 (1/16 = T-2 발화 권고 영역 — 합의 진입 발효 = 사용자 명시 결정 후)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ W-1 ~ W-4 수정 파일 / 검증 방법 / actual run 조건 / rollback trigger *최종 확정 발효 0건* (사용자 명시 결정 영역)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ git commit / push 0건 (사용자 명시 결정 후 진입)
