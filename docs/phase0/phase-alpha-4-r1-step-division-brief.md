# Phase α-4 R-1 실 진입 Step 분할 Brief (DRAFT)

> **본 문서는 Phase α-4 R-1 *진입 조건 점검* brief 합의 (`1c365e7` APPROVE AS BRIEF — 33 조건 C-π-1 ~ C-π-33) 발효 후속, Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *실 진입* 의 **Step 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준** 정리 한정 brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - 직전 α-4 진입 가능성 brief (`f91ef4b`) = "*Can* we enter Phase α-4 영역?" — 영역 정의 + 진입 적격성 5 조건 검토 한정
> - 직전 α-4 진입 조건 점검 brief (`7a289fa`, 합의 `1c365e7`) = "*Are entry conditions still satisfied after α-1+2+3 evidence?*" — 조건 재검토 한정
> - **본 brief = "*How* should Phase α-4 R-1 실 진입 be staged?"** — Step 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 (Phase α-4 자체의 Stage 2 등가 framing, α-1+2+3 Stage 2 `88ccf79` 패턴 답습)
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) Phase α-4 어느 step 도 *실 진입* 시키지 않으며, (ii) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, (iii) Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 29 (직전) + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33 = **합산 284 합의 조건** 中 어느 것도 *해소* / *변경* 시키지 않으며, (iv) 사용자 명시 5 금지 中 어느 것도 *해소* 시키지 않으며, (v) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 어느 것도 *발생시키지 않으며*, (vi) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-entry-condition.md` (α-4 진입 조건 점검 합의, commit `1c365e7` APPROVE AS BRIEF — 33 조건 C-π-1 ~ C-π-33, 후속 23 — **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-entry-condition-check-brief.md` (commit `7a289fa`, 566줄)
- `docs/phase0/phase-alpha-123-local-validation-evidence.md` (commit `7b3d40a`, 486줄 — 12/12 PASS)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (commit `e59a565` APPROVE AS BRIEF — 29 조건 C-ε-1 ~ C-ε-29, 직전 α-4 brief 합의)
- `docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (commit `f91ef4b`, 751줄 직전 α-4 brief)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-123-parallel-implementation.md` (Stage 2 α-1+2+3 1순위 *계획* brief 합의, commit `88ccf79` — 25 조건 C-ν-1 ~ C-ν-25, **본 brief 의 framing 모법**)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (Stage 4 PC-3 + AR-1 통합 진입 합의 APPROVE — sub-step 4.1 + 4.2 발효)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-4 R-1 실 진입 step 분할 brief를 작성해주세요. 범위는 R-1 CI workflow 통합을 실제 구현하기 전에 step 분할, 수정 범위, 테스트 범위, rollback trigger, evidence 기준을 정리하는 것입니다. 아직 CI workflow 변경, runtime code 변경, actual run 재실행, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습

1. ❌ **CI workflow 변경 금지** — `.github/workflows/*.yml` 본문 변경 모두 0건 (3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 = 7 artifacts × 1593줄 답습 보존)
2. ❌ **runtime code 변경 금지** — `src/` 본문 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존
3. ❌ **actual run 재실행 금지** — 4 prerequisite run (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 답습 한정 — 신규 trigger 0건
4. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리
5. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C 12 조건 미진입 영구 답습

### 0.3 본 brief 가 *하는* 것

1. Phase α-4 R-1 진입 조건 점검 합의 (`1c365e7`) 발효 후속 — **실 진입 step 분할 계획 한정** (§1)
2. **Step 0 ~ Step 6 분할 매트릭스** — 각 step 별 책무 + 자동 진입 0건 (§2)
3. **수정 범위 매트릭스 per Step** — 본문 변경 0건 영역 + 신규 작성 영역 (evidence 본문 한정) 분리 (§3)
4. **테스트 범위 매트릭스 per Step** — local self-check + 답습 enumerate + actual run 재실행 0건 분리 (§4)
5. **Rollback Trigger 매트릭스** — Layer B 18 trigger + TR-1 ~ TR-5 + 본 brief 신규 후보 trigger 0건 추가 (§5)
6. **Evidence 기준 매트릭스** — ADR-011 §2.1 (a)~(e) × R-1 영역 답습 + Evidence Artifact 형식 + ledger entry 후보 한정 (§6)
7. **사용자 명시 5 금지 × Step 분리 매트릭스** — 5/5 영구 보존 + Step 0 ~ Step 6 전체 영역 영구 답습 (§7)
8. **합산 284 합의 조건 답습 매트릭스** (§8)
9. **합의 형태 권고 + 풀 3+1 승격 트리거** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 Step 0 ~ Step 6 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **CI workflow 변경 (0건)** — 3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 = 7 artifacts × 1593줄 답습 보존 + 변경 / 추가 / 삭제 0건
- ❌ **runtime code 변경 (0건)** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 (Backlog #4 분리)
- ❌ **actual run 재실행 (0건)** — 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) SUCCESS 답습 한정 + 신규 GitHub Actions actual run trigger 0건
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (직전 α-4 brief + α-4 진입 조건 점검 + α-1+2+3 evidence 답습 패턴 보존)**:

- ❌ **Phase α-4 자동 실 진입 (0건)** — 본 brief = *step 분할 계획 한정* (실 진입 = Step 1 — 사용자 명시 결정 영역)
- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — `secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + `tools/mvp1_pc3_ar1_integration_check.py` 298 + `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` 30 + `fail/pc3_violation_continue_on_error.yml` 31 + `fail/ar1_violation_no_fail_closed.yml` 28 = 1593줄 답습 보존
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
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 차단조건 #6 + 부록 B 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정 답습 (`docker/gp3-st3-poc/` 한정)
- ❌ **실 secret material commit (0건)** — FAKE_TEST_SECRET marker 답습
- ❌ **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`951a5b1`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 ~ α-3 / Phase α-4 (직전) / α-1+2+3 evidence (`7b3d40a`) / α-4 진입 조건 점검 합의 (`1c365e7`) 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 (0건)**
- ❌ **Phase α-1 / α-2 / α-3 자동 재진입 (0건)** — α-1+2+3 evidence §5.2 + §8 답습
- ❌ **Layer C 재발효 (0건)** — `eb01bc4` 답습 한정
- ❌ **Layer D 재선언 (0건)** — `951a5b1` 답습 한정 / MVP-1 PASS 재선언 (0건)
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
- ❌ **신규 actual run 자동 trigger (0건)** — 4 prerequisite run 답습 한정
- ❌ **합산 284 합의 조건 자동 변경 (0건)**

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-4 어느 Step 도 *실 진입* 시키지 않으며,
- (ii) 합산 284 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iii) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (iv) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (v) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vi) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (vii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (viii) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (ix) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (x) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 어느 것도 *발생시키지 않으며*,
- (xi) Rollback Trigger / TR-1 ~ TR-5 어느 것도 *발화* 시키지 않으며,
- (xii) Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 실 진입의 Step 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 *권위 권고 한정***. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (Phase α-4 진입 조건 점검 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `e59a565` (2026-05-14) | Phase α-4 R-1 brief 합의 APPROVE AS BRIEF — 29 조건 C-ε-1 ~ C-ε-29 | ✅ 답습 한정 (변경 0건) |
| `f91ef4b` (2026-05-14) | Phase α-4 R-1 진입 brief DRAFT (751줄) | ✅ 답습 한정 |
| `eb01bc4` (2026-05-16) | Layer C 발효 (30 조건 C-ι-1 ~ C-ι-30) | ✅ 답습 한정 |
| `951a5b1` (2026-05-16) | Layer D 재진입 평가 (25 조건 C-λ-1 ~ C-λ-25) | ✅ 답습 한정 |
| `542e77e` (2026-05-16) | Stage 1 — Phase α 통합 계획 합의 (25 조건 C-μ-1 ~ C-μ-25) | ✅ 답습 한정 |
| `88ccf79` (2026-05-16) | Stage 2 — α-1+2+3 1순위 계획 합의 (25 조건 C-ν-1 ~ C-ν-25) | ✅ **본 brief 의 framing 모법** |
| `7917e4a` (2026-05-16) | Stage 3 — α-1+2+3 parallel actual entry 합의 (25 조건 C-ξ-1 ~ C-ξ-25) | ✅ 답습 한정 |
| `faae826` (2026-05-16) | α-1+2+3 parallel actual entry brief (920줄) | ✅ 답습 한정 |
| `7b3d40a` (2026-05-16) | α-1+2+3 Local Validation Evidence (486줄, 12/12 PASS) | ✅ 답습 한정 |
| `2aa13ef` (2026-05-16) | CONTEXT 후속 21 entry | ✅ 답습 한정 |
| `68d010a` (2026-05-16 후속 22) | CONTEXT — α-1+2+3 evidence 기록 entry | ✅ 답습 한정 |
| `7a289fa` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 brief DRAFT (566줄) | ✅ 답습 한정 |
| `1c365e7` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 합의 APPROVE AS BRIEF — 33 조건 C-π-1 ~ C-π-33 | ✅ **본 brief 의 발효 trigger** |
| `149898f` (HEAD, 2026-05-17 후속 23) | CONTEXT — Phase α-4 R-1 진입 조건 점검 기록 entry | ✅ 답습 한정 |

### 1.2 α-4 진입 조건 점검 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-17 후속 23 |
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 — 15/15 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건) |
| 합의 조건 | **33 조건 (C-π-1 ~ C-π-33)** |
| 5 진입 적격성 조건 | **5/5 충족** (C-α4-1 ~ C-α4-5 + 3 조건 답습 강화: C-α4-2/4/5) |
| 의존성 충족 | **이중 evidence 충족** (4 prerequisite runs PASS + local 12/12 PASS) |
| 사용자 명시 5 금지 위반 | **5/5 0건** |
| 5 영구 핵심 제약 보존 | **5/5 보존 (답습 강화)** |
| Provider Liquidity 5-way 보존 | **5/5 100% 보존 (답습 강화)** |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| 본 brief trigger 의미 | Phase α-4 R-1 영역 *진입 적격성 권위 확정* → **실 진입 step 분할 계획 (= 본 brief)** 의 framing 정당화 |

### 1.3 4 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 가능성 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 조건 C-ε-1 ~ C-ε-29 | "*Can* we enter Phase α-4 영역?" |
| α-4 Stage 1.5 (조건 재검토) | Phase α-4 R-1 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 조건 C-π-1 ~ C-π-33 | "*Are conditions still satisfied after α-1+2+3 evidence?*" |
| **α-4 Stage 2 (본 brief)** | **Phase α-4 R-1 *실 진입 step 분할* brief** | (현재) | DRAFT (미확정) | (미확정) | **"*How* should Phase α-4 R-1 실 진입 be staged?"** |
| α-4 Stage 3 (실 진입 여부, 본 brief 외) | Phase α-4 R-1 *실 진입 여부* brief | (미확정) | (미확정) | (미확정) | "*Should* we enter Phase α-4 R-1 actual implementation now?" |
| α-4 Stage 4 (실 구현, 본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* Phase α-4 R-1 actual implementation" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 2 framing** (= Stage 2 α-1+2+3 1순위 *계획* brief `88ccf79` 패턴 답습):

- α-4 Stage 1 (영역 정의) ↔ α-4 Stage 1.5 (조건 재검토) ↔ **α-4 Stage 2 (본 brief, Step 분할 계획)** ↔ α-4 Stage 3 (실 진입 여부, 본 brief 외) ↔ α-4 Stage 4 (실 구현, 사용자 명시 결정 영역)
- 본 brief 의 단일 책무: **"실 진입을 어떻게 단계 분할할 것인가?"** + **"각 단계 별 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준은 무엇인가?"** 정리 한정
- 본 brief ≠ α-4 Stage 3 (실 진입 여부 검토 = 별도 brief 영역)
- 본 brief ≠ α-4 Stage 4 (실 구현 = 별도 단계, 본 brief 영역 외)
- 본 brief ≠ Phase α-4 자동 진입 발효 (사용자 명시 결정 영역)
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-17 후속 24 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 5 금지 #4) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 5 금지 #5) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 (`7b3d40a`) |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local INI 구조 8/8 PASS evidence 답습 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 |
| **Phase α-4 (R-1)** | **2순위 의존 — CI workflow 통합 (PC-3 + AR-1)** | ⏳ **본 brief = α-4 Stage 2 (Step 분할 계획 한정)** |

---

## 2. Step 0 ~ Step 6 분할 매트릭스

### 2.1 본 brief 발효 후 실 진입 Step 분할 권고 (Stage 2 α-1+2+3 §3 답습 패턴)

| Step | 영역 | 본 brief 영역 | 사용자 명시 결정 후 진입 |
|------|----|----------|------------------|
| **Step 0** | 사전 점검 (본 brief 자체) — Step 분할 권고 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 | ✅ 본 brief (DRAFT) | — |
| **Step 1** | R-1 영역 1593줄 local self-check 한정 (실 본문 변경 0건) | ❌ (영역 외) | 사용자 명시 결정 영역 |
| Step 1.4.1 | PC-3 CI step 통합 답습 검증 (Stage 4 sub-step 4.1 답습) | ❌ (영역 외) | 동상 |
| Step 1.4.1.a | `secret-hygiene-egress-redaction.yml` (694줄) PC-3 정합성 local self-check | ❌ (영역 외) | 동상 |
| Step 1.4.1.b | `provider-adapter-enforcement.yml` (186줄) PC-3 정합성 local self-check | ❌ (영역 외) | 동상 |
| Step 1.4.1.c | `provider-url-scanner.yml` (326줄) PC-3 정합성 local self-check | ❌ (영역 외) | 동상 |
| Step 1.4.2 | AR-1 fail-closed 통합 답습 검증 (Stage 4 sub-step 4.2 답습) | ❌ (영역 외) | 동상 |
| Step 1.4.2.a | `tools/mvp1_pc3_ar1_integration_check.py` (298줄) `--mode integration` + `--list-checks` self-check | ❌ (영역 외) | 동상 |
| Step 1.4.2.b | PASS fixture (`compliant_entry_step.yml`, 30줄) 검증 | ❌ (영역 외) | 동상 |
| Step 1.4.2.c | FAIL fixture 2개 (`pc3_violation_continue_on_error.yml` 31 + `ar1_violation_no_fail_closed.yml` 28) 검증 | ❌ (영역 외) | 동상 |
| **Step 2** | 4 prerequisite actual run PASS evidence 답습 enumerate 한정 (재실행 0건) | ❌ (영역 외) | 동상 |
| **Step 3** | Phase α-4 R-1 *Local Validation Evidence* 본문 작성 (α-1+2+3 evidence `7b3d40a` 패턴 답습, 도구/workflow 본문 변경 0건) | ❌ (영역 외) | 동상 |
| **Step 4** | 합의 형태 결정 (사용자 명시 결정 영역) — (a) Reviewer-only 단축 / (b) 풀 3+1 / (c) 풀 3+1 + 외부 LLM 1+ | ❌ (영역 외) | 동상 |
| Step 4.옵션 | 외부 LLM 합의 (옵션) — ADR-011 §2.4 영역 (본 brief 시점 미적용 권고) | ❌ (영역 외) | 동상 |
| **Step 5** | 합의 보고서 작성 (Reviewer-only 단축 시 — 단일 문서, 풀 3+1 시 — 4 에이전트 본문 + Reviewer 본문) | ❌ (영역 외) | 동상 |
| **Step 6** | 메타 commit + push (CONTEXT / INDEX / SESSION 갱신) | ❌ (영역 외) | 동상 |

### 2.2 Step 별 의존성 토폴로지

```
Step 0 (본 brief 자체, DRAFT)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
Step 1.4.1.a → Step 1.4.1.b → Step 1.4.1.c (PC-3 정합성 self-check 직렬)
   │                  │                │
   └──────────────────┴────────────────┘
                      ▼
Step 1.4.2.a → Step 1.4.2.b → Step 1.4.2.c (AR-1 정합성 self-check 직렬)
                      │
                      ▼
Step 2 (actual run PASS evidence 답습 enumerate, 재실행 0건)
                      │
                      ▼
Step 3 (Local Validation Evidence 본문 작성, evidence 문서 신규 작성 한정)
                      │
                      ▼
Step 4 (합의 형태 결정 — 사용자 명시 결정 영역)
                      │
                      ▼
Step 5 (합의 보고서 작성)
                      │
                      ▼
Step 6 (메타 commit + push)
```

### 2.3 Step 별 cycle 옵션

| cycle 옵션 | 영역 | 권고 |
|---------|------|----|
| (i) 직렬 (Step 1.4.1.a → Step 1.4.1.b → Step 1.4.1.c → Step 1.4.2.a → Step 1.4.2.b → Step 1.4.2.c) | 가장 안전한 토폴로지 — 단계별 검증 가능 | **권고** (Stage 2 α-1+2+3 §3 답습 패턴) |
| (ii) PC-3 / AR-1 sub-step 병렬 (Step 1.4.1.* 와 Step 1.4.2.* 병렬) | 토폴로지 분리 가능 (PC-3 ↔ AR-1 직교) | 옵션 (속도 ↑, 디버깅 ↓) |
| (iii) 전 sub-step 동시 진입 (6 sub-step 일괄) | 최단 cycle | 옵션 (디버깅 어려움) |
| (iv) Step 1.4.1 + Step 1.4.2 완전 분리 합의 (2 cycle 합의) | 각 cycle 별 별도 합의 | 옵션 (오버헤드 ↑) |

본 brief 권고 = **(i) 직렬 cycle** — Stage 2 α-1+2+3 §3 답습 패턴 + 단계별 회복 가능성 ↑.

### 2.4 본 §2 의 *범위 한계*

본 §2 = **Step 분할 *권고 한정***. 실 Step 결정 / Step 진입 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 *권고* = 권위 권고 한정 — 실 Step 진입 발효 권위 0건.

---

## 3. 수정 범위 매트릭스 per Step

### 3.1 Step 별 본문 변경 범위 매트릭스

| Step | R-1 영역 1593줄 (7 artifacts) 본문 변경 | R-4/R-5/R-7 1192줄 (13 file) 본문 변경 | `src/` runtime code 본문 변경 | 신규 작성 영역 (evidence 본문 한정) |
|------|---------------------------|-------------------------|----------------------|---------------------|
| Step 0 (본 brief) | 0건 | 0건 | 0건 | 본 brief 1건 (Phase α-4 R-1 step 분할 brief DRAFT) |
| Step 1.4.1.a | 0건 (`secret-hygiene-egress-redaction.yml` 694줄 답습) | 0건 | 0건 | 0건 (local self-check 한정 — 결과 enumerate 만) |
| Step 1.4.1.b | 0건 (`provider-adapter-enforcement.yml` 186줄 답습) | 0건 | 0건 | 0건 |
| Step 1.4.1.c | 0건 (`provider-url-scanner.yml` 326줄 답습) | 0건 | 0건 | 0건 |
| Step 1.4.2.a | 0건 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 답습) | 0건 | 0건 | 0건 (self-check 결과 enumerate) |
| Step 1.4.2.b | 0건 (PASS fixture 30줄 답습) | 0건 | 0건 | 0건 |
| Step 1.4.2.c | 0건 (FAIL fixture 59줄 답습) | 0건 | 0건 | 0건 |
| Step 2 | 0건 (4 prerequisite runs JSON conclusion 답습) | 0건 | 0건 | 0건 |
| **Step 3** | 0건 | 0건 | 0건 | **Phase α-4 R-1 Local Validation Evidence 1건 신규 작성** (α-1+2+3 evidence `7b3d40a` 486줄 패턴 답습) |
| Step 4 | 0건 (결정 영역) | 0건 | 0건 | 0건 |
| Step 5 | 0건 | 0건 | 0건 | 합의 보고서 1건 신규 작성 (Reviewer-only 시) / 4 에이전트 + Reviewer 본문 신규 작성 (풀 3+1 시) |
| Step 6 | 0건 | 0건 | 0건 | CONTEXT / INDEX / SESSION 메타 갱신 (소량 — 사용자 명시 결정 후) |
| **합산** | **0건 영구 답습** | **0건 영구 답습** | **0건 영구 답습** | **본 brief 1건 + Step 3 evidence 1건 + Step 5 합의 보고서 1건 + Step 6 메타 갱신 (사용자 명시 결정 후)** |

### 3.2 사용자 명시 5 금지 충돌 매트릭스 per Step

| Step | #1 CI workflow 변경 | #2 runtime code 변경 | #3 actual run 재실행 | #4 Operational Readiness PASS | #5 Hermes PMO 격상 |
|------|---------------|------------------|----------------|------------------------|----------------|
| Step 0 (본 brief) | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 |
| Step 1.4.1.a ~ Step 1.4.2.c | ✅ 충돌 0 (self-check 한정 — 본문 변경 0건) | ✅ 충돌 0 | ✅ 충돌 0 (local 한정) | ✅ 충돌 0 | ✅ 충돌 0 |
| Step 2 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 (4 prerequisite runs 답습 enumerate 한정) | ✅ 충돌 0 | ✅ 충돌 0 |
| Step 3 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 |
| Step 4 ~ Step 6 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 | ✅ 충돌 0 |
| **합산** | **✅ 0/7 step × 5 금지 = 35/35 충돌 0** | — | — | — | — |

### 3.3 신규 작성 영역 명시 (3 종)

| 신규 작성 영역 | 답습 출처 | 본 brief 영역 |
|------------|---------|----------|
| (A) 본 brief (Phase α-4 R-1 step 분할 brief DRAFT) | Stage 2 α-1+2+3 `88ccf79` framing 답습 | ✅ 본 brief = 신규 작성 |
| (B) Phase α-4 R-1 Local Validation Evidence (Step 3) | α-1+2+3 evidence `7b3d40a` 486줄 패턴 답습 | ❌ (Step 3 — 사용자 명시 결정 후) |
| (C) 합의 보고서 (Step 5) | Reviewer-only 단축 / 풀 3+1 합의 패턴 답습 | ❌ (Step 5 — 사용자 명시 결정 후) |

### 3.4 본 §3 의 *범위 한계*

본 §3 = **수정 범위 *enumerate 한정***. 실 본문 변경 / 실 신규 작성 = 사용자 명시 결정 영역 (자동 진입 0건). R-1 + R-4/R-5/R-7 + `src/` 본문 = **Step 0 ~ Step 6 전체 영역 영구 0건 답습**.

---

## 4. 테스트 범위 매트릭스 per Step

### 4.1 Step 별 테스트 영역 매트릭스

| Step | 테스트 영역 | 검증 방법 | 답습 출처 | 신규 actual run trigger |
|------|----------|--------|---------|---------------------|
| Step 0 (본 brief) | 본 brief 메타 검증 (§12) — 본문 변경 / 신규 작성 / 합의 보고서 / 메타 갱신 영역 0건 | self-check (본 brief §12 답습) | Stage 2 α-1+2+3 `88ccf79` §12 답습 | 0건 |
| Step 1.4.1.a | `secret-hygiene-egress-redaction.yml` PC-3 정합성 — `continue-on-error: false` + non-zero exit propagation + `if: always()` 패턴 grep / yaml parse 검증 (694줄) | yaml parse + grep | Stage 4 합의 §1.3 답습 + Group D PoC 답습 | 0건 (local) |
| Step 1.4.1.b | `provider-adapter-enforcement.yml` PC-3 정합성 — T-2 import-linter step + T-5 AST step PC-3 정합 검증 (186줄) | yaml parse + grep | Group A 1차+2차 PoC 답습 | 0건 |
| Step 1.4.1.c | `provider-url-scanner.yml` PC-3 정합성 — T-5 URL + Model catalog step PC-3 정합 검증 (326줄) | yaml parse + grep | Group A 3차 PoC 답습 | 0건 |
| Step 1.4.2.a | `tools/mvp1_pc3_ar1_integration_check.py` self-check — `--mode integration` + `--list-checks` 실행 (298줄) | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration` local run | Stage 4 합의 §1.3 답습 | 0건 (local) |
| Step 1.4.2.b | PASS fixture (`compliant_entry_step.yml`, 30줄) integration tool 통과 검증 | local fixture pass check | Stage 4 합의 §1.3 답습 | 0건 |
| Step 1.4.2.c | FAIL fixture 2개 (PC-3 violation 31줄 + AR-1 violation 28줄) integration tool 적절 차단 검증 | local fixture fail check | Stage 4 합의 §1.3 답습 | 0건 |
| Step 2 | 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) JSON conclusion + duration + step-level 답습 enumerate | gh CLI / GitHub Actions API 조회 한정 (재실행 0건) | C-ε-3 ~ C-ε-5 + C-α4-3 답습 | 0건 |
| Step 3 | Local Validation Evidence 본문 완전성 검증 — 영역 / 답습 / 12/12 PASS 대응 매트릭스 / 5 영구 핵심 제약 보존 / Provider Liquidity 5-way 답습 / F-금지 #1 답습 / 합산 합의 조건 변경 0건 검증 | self-check (α-1+2+3 evidence `7b3d40a` §0 ~ §10 답습) | α-1+2+3 evidence 패턴 답습 | 0건 |
| Step 4 | 합의 형태 결정 적격성 — 풀 3+1 트리거 0건 발화 확인 + Reviewer-only 단축 적격 검증 | self-check (트리거 매트릭스 답습) | 본 brief §9.2 답습 | 0건 |
| Step 5 | 합의 보고서 본문 완전성 — 답습 / 조건 / 평가 / 판정 본문 검증 | self-check (Reviewer 본문 패턴 답습) | 직전 α-4 합의 `e59a565` / `1c365e7` 패턴 답습 | 0건 |
| Step 6 | 메타 commit + push 정합성 — CONTEXT / INDEX / SESSION 갱신 본문 검증 + git push origin feature/hermes-phase0 | git status / git log / git push | C-π-x 답습 | 0건 |
| **합산** | **12 step × 평균 1 ~ 3 검증 영역** | — | — | **✅ 0 신규 actual run trigger 영구 답습** |

### 4.2 테스트 적격 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `yamllint` / `actionlint` | YAML / GitHub Actions workflow syntax 검증 | 답습 한정 — 신규 도입 0건 |
| `python tools/mvp1_pc3_ar1_integration_check.py` | Stage 4 PC-3 + AR-1 integration check tool self-check | 답습 한정 — 신규 작성 0건 |
| `grep` / yaml parse (Python `yaml.safe_load`) | PC-3 / AR-1 패턴 정합성 검증 | 표준 도구 답습 |
| `gh CLI` / GitHub Actions API | 4 prerequisite runs 답습 enumerate | 답습 한정 — 재실행 0건 |
| `git status` / `git log` / `git push` | 메타 commit 정합성 | 표준 git 답습 |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 4.3 테스트 결과 답습 + threshold 후보 한정 매트릭스 (고정 0건)

| threshold | 본 brief 시점 |
|---------|----------|
| CI runtime per workflow | 후보 한정 (mvp1.md §3.4.1 + §4.3 + §4.4 답습) |
| PR check pass rate | 후보 한정 |
| fail-closed rate (AR-1) | 후보 한정 |
| PC-3 violation count per PR | 후보 한정 |
| integration check tool runtime | 후보 한정 (Stage 4 합의 §1.3 답습) |
| **합산** | **5/5 후보 한정 — 고정 0건** |

### 4.4 테스트 영역 vs 사용자 명시 5 금지 분리 매트릭스

| 테스트 영역 | #1 CI workflow 변경 충돌 | #2 runtime code 변경 충돌 | #3 actual run 재실행 충돌 | #4 Operational Readiness PASS 충돌 | #5 Hermes PMO 격상 충돌 |
|----------|---------------|----------------|----------------|------------------------|----------------|
| yamllint / actionlint local 실행 | ✅ 0 (read-only) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 |
| integration tool local self-check | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 |
| fixture pass/fail 검증 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 |
| 4 prerequisite runs JSON enumerate | ✅ 0 | ✅ 0 | ✅ 0 (read-only) | ✅ 0 | ✅ 0 |
| **합산** | **✅ 4 영역 × 5 금지 = 20/20 충돌 0** | — | — | — | — |

### 4.5 본 §4 의 *범위 한계*

본 §4 = **테스트 범위 *권고 한정***. 실 테스트 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 모든 테스트 영역 = **local self-check + 답습 enumerate 한정** — 신규 actual run trigger 0건.

---

## 5. Rollback Trigger 매트릭스

### 5.1 Layer B 18 Rollback Trigger 답습 매트릭스 (Layer B §1.7 + mvp1.md §3.5 + §4.6 답습)

| # | trigger 영역 | R-1 직접 영향 | 본 brief 시점 발화 | 본 brief 발효 후 Step 0 ~ 6 발화 예상 |
|---|---------|------------|-----------------|------------------------|
| 1 | secret leak observed in production | 영향 0 (MVP-1 발견 / MVP-3 P2 영역 분리) | 0건 | 0건 |
| 2 | secret leak observed in PR | 영향 0 (Step 1.4.1 PC-3 정합성 답습 한정) | 0건 | 0건 |
| 3 | provider key in `~/.config/...` | 영향 0 (R-7 영역 / Phase α-3) | 0건 | 0건 |
| 4 | provider key in `~/Library/...` | 영향 0 (동상) | 0건 | 0건 |
| 5 | provider key in CI runner env | 영향 0 (F-금지 #1 영구 답습) | 0건 | 0건 |
| 6 | direct provider SDK import detected | 영향 0 (Phase α-2 영역) | 0건 | 0건 |
| 7 | URL endpoint to provider in code | 영향 0 (Phase α-1 R-4 URL scanner 영역) | 0건 | 0건 |
| 8 | Model name pattern match (PASS) | 영향 0 (Phase α-1 R-4 model scanner 영역) | 0건 | 0건 |
| 9 | Tier-1 catalog under-detection | 영향 0 (R-4.1 영역) | 0건 | 0건 |
| 10 | Tier-2/3 expansion needed | 영향 0 (Backlog #3 분리) | 0건 | 0건 |
| 11 | importlinter forbidden bypass | 영향 0 (Phase α-2 R-5 영역) | 0건 | 0건 |
| 12 | docker secret commit in PR | 영향 0 (Phase α-3 R-7 영역) | 0건 | 0건 |
| 13 | CI step pass with violation present | **R-1 직접 영향** (PC-3 violation) | 0건 (PoC 답습 — Step 1.4.1.* 검증 영역) | 0건 (Step 1.4.1.* self-check PASS 기대) |
| 14 | CI step fail without auto-reject | **R-1 직접 영향** (AR-1 violation) | 0건 (PoC 답습 — Step 1.4.2.* 검증 영역) | 0건 (Step 1.4.2.* self-check PASS 기대) |
| 15 | PR check unstable / flaky | 영향 0 (CI runtime 답습 + threshold 후보 한정) | 0건 | 0건 |
| 16 | Hermes-originated commit detected | 영향 0 (Group I 분리) | 0건 | 0건 |
| 17 | provider key adapter bypass | 영향 0 (P1 v2 facade MVP / Backlog #4 분리) | 0건 | 0건 |
| 18 | secret handling environment mismatch | 영향 0 (mvp1.md §5.4 IR-3 영역) | 0건 | 0건 |
| **합산** | **18 trigger** | **R-1 직접 영향 2 (#13, #14) + 간접 0 + 영향 0 16** | **0건 영구 답습** | **0건 발화 예상** |

### 5.2 TR-1 ~ TR-5 답습 매트릭스 (Group A 2차 합의 답습)

| TR # | 영역 | R-1 영향 | 본 brief 시점 발화 | Step 0 ~ 6 발화 예상 |
|----|----|--------|--------------|----------------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 필요 | 영향 0 (Phase α-2 R-5 영역) | 0건 | 0건 |
| TR-2 | `include_external_packages` flag 변경 | 영향 0 (동상) | 0건 | 0건 |
| TR-3 | `root_packages` 영역 변경 | 영향 0 (동상) | 0건 | 0건 |
| TR-4 | `ignore_imports` 영역 변경 | 영향 0 (동상) | 0건 | 0건 |
| TR-5 | google.generativeai facade 영역 변경 | 영향 0 (Backlog #4 P1 v2 facade MVP 영역) | 0건 | 0건 |
| **합산** | **5 trigger** | **R-1 직접 영향 0** | **0건 영구 답습** | **0건 발화 예상** |

### 5.3 본 brief 신규 후보 trigger 답습 (정식 등록 0건, 후보 한정)

| 후보 trigger | 영역 | 본 brief 시점 |
|----------|----|----------|
| PC-3 self-check FAIL — local self-check 시 `continue-on-error: true` 발견 | R-1 영역 (Step 1.4.1.*) | **후보 한정** (정식 등록 0건 — Backlog #5 영역) |
| AR-1 self-check FAIL — local self-check 시 fail-closed 패턴 누락 발견 | R-1 영역 (Step 1.4.2.*) | **후보 한정** |
| integration check tool self-check FAIL | R-1 영역 (Step 1.4.2.a) | **후보 한정** |
| 4 prerequisite runs JSON conclusion 미답습 발견 | Step 2 영역 | **후보 한정** |
| Local Validation Evidence 본문 누락 발견 | Step 3 영역 | **후보 한정** |
| **합산** | **5 후보** | **5/5 후보 한정 — 정식 등록 0건 (Backlog #5 ADR-012 §2.2 분리)** |

### 5.4 합산 + 발화 영역 분리

| 영역 | 합계 | R-1 직접 영향 | 본 brief 시점 발화 | Step 0 ~ 6 발화 예상 |
|------|----|------------|-----------------|----------------|
| Layer B 18 trigger | 18 | 2 (#13, #14) | 0건 | 0건 |
| TR-1 ~ TR-5 | 5 | 0 | 0건 | 0건 |
| 본 brief 신규 후보 trigger | 5 | 5 | 0건 (후보 한정) | 0건 (후보 한정 — 정식 등록 0건) |
| **합산** | **28** | **7** | **0건 영구 답습** | **0건 발화 예상 영구 답습** |

### 5.5 PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger 분리 명시

| 분리 영역 | trigger | 본 brief 영역 |
|---------|------|----------|
| PC-4 local pre-commit framework 활성화 필요 trigger | sub-step 4.3 = Backlog #1 + #2 1.5차 보강 영역 | 영역 외 (사용자 명시 5 금지 분리) |
| AR-2 branch protection rule 활성화 필요 trigger | sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 | 영역 외 |
| AR-3 자동 revert bot 활성화 필요 trigger | Backlog #3 T3 영역 | 영역 외 |
| Stage 5 (G3-7 4 항목) 진입 필요 trigger | Stage 4 후속 권고 답습 | 영역 외 |

### 5.6 본 §5 의 *범위 한계*

본 §5 의 어떤 항목도:

- (i) Rollback Trigger / TR-1 ~ TR-5 / 본 brief 신규 후보 어느 것도 *발화* 시키지 않으며,
- (ii) threshold 어느 것도 *고정* 시키지 않으며,
- (iii) 합의 본문 어느 줄도 *변경* 하지 않으며,
- (iv) ledger entry enum 어느 것도 *정식 등록* 시키지 않는다 (Backlog #5 분리).

---

## 6. Evidence 기준 매트릭스

### 6.1 ADR-011 §2.1 (a)~(e) × R-1 영역 답습 매트릭스 (Layer C 발효 시점 답습)

| 조건 | 영역 | R-1 본 brief 시점 답습 | 답습 출처 |
|----|----|------------------|---------|
| (a) 기존 패턴 동등성 (5 영구 핵심 제약 보존) | Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 | ✅ 5/5 보존 (α-1+2+3 evidence §6.1 답습 강화) | C-π-29 (α-4 진입 조건 점검 합의) 답습 |
| (b) 격리 PoC 동등성 (R-1 7 artifacts × 1593줄 PoC 답습) | 3 MVP-1 workflow + integration tool + 3 fixture | ✅ PoC 답습 변경 0건 | C-π-x 답습 |
| (c) PR 매트릭스 동등성 (4 prerequisite runs PASS) | `25728590939` + `25728590916` + `25728590977` + `25731846625` SUCCESS | ✅ 4/4 PASS 답습 (재실행 0건) | C-α4-3 + C-π-x 답습 |
| (d) regression 답습 (Phase α-1+2+3 evidence 답습) | local 12/12 PASS evidence (`7b3d40a` 486줄) | ✅ 답습 강화 (이중 evidence 충족) | C-π-x 답습 |
| (e) canary 답습 (Layer C 발효 시점 답습) | Layer C `eb01bc4` 30 조건 답습 | ✅ 답습 한정 (재발효 0건) | C-π-x 답습 |
| **합산** | **5 조건** | **✅ 5/5 답습 충족 — Layer C 답습 한정 (재검증 0건)** | — |

### 6.2 Phase α-4 R-1 Local Validation Evidence 작성 기준 (Step 3 영역)

| 영역 | 기준 | 답습 출처 |
|------|----|---------|
| 본문 line count 범위 | 약 400 ~ 600줄 (α-1+2+3 evidence 486줄 패턴 답습) | `7b3d40a` 답습 |
| 섹션 구조 | 0 범위 / 1 발효 trigger / 2 작성 시점 발견 / 3 PASS 검증 매트릭스 / 4 본문 변경 0건 검증 / 5 5 영구 핵심 제약 보존 + Provider Liquidity 5-way 보존 + F-금지 #1 영구 답습 / 6 합산 합의 조건 변경 0건 / 7 다음 단계 옵션 / 8 evidence 권위 한계 / 9 메타 검증 / 10 요약 | α-1+2+3 evidence 본문 패턴 답습 |
| 신규 작성 영역 | Phase α-4 R-1 Local Validation Evidence 본문 1건 | Step 3 = α-4 evidence 신규 작성 |
| 본문 변경 영역 (R-1 / R-4 / R-5 / R-7 / src / docker block 등) | 0건 영구 답습 | 사용자 명시 5 금지 답습 |
| PASS 검증 결과 enumerate | Step 1.4.1.a ~ Step 1.4.2.c (6 sub-step PASS 결과) + Step 2 (4 prerequisite runs 답습 enumerate) | 본 brief §2.1 답습 |
| 메타 검증 항목 | ≥ 15 항목 (사용자 명시 5 금지 답습 / 합산 합의 조건 변경 0건 / R-1 본문 변경 0건 / actual run 재실행 0건 / 5 영구 핵심 제약 보존 / Provider Liquidity 5-way 보존 / F-금지 #1 영구 답습 / Rollback Trigger 발화 0건 / threshold 후보 한정 / event enum 후보 한정 / 외부 LLM 호출 0건 / 실 API key 사용 0건 / 자동 진입 0건 / Layer C 재발효 0건 / Layer D 재선언 0건) | Stage 2 α-1+2+3 §12 답습 패턴 |
| 본문 변경 검증 | `git status` clean + `git diff` 0 line (R-1 / R-4 / R-5 / R-7 / src 본문 변경 0건) | α-1+2+3 evidence §5.1 답습 |
| evidence 권위 | "**실 진입 완료 evidence**" — 합의 보고서 권위 아님, MVP-1 PASS 재선언 아님, Layer C 재발효 아님 | α-1+2+3 evidence 권위 패턴 답습 |

### 6.3 Evidence Artifact 형식 답습 매트릭스 (Stage 2 α-1+2+3 §7.3 답습)

| Artifact | 형식 | 본 brief 시점 |
|--------|----|----------|
| GitHub Actions run | JSON conclusion + duration + step-level | 답습 (4 prerequisite runs 영구 답습) |
| Local self-check result | Markdown PASS / FAIL count + assertion log | 답습 |
| Markdown evidence | Phase α-4 R-1 Local Validation Evidence (Step 3 신규 작성) | 답습 (α-1+2+3 evidence 패턴 답습) |
| Stage 4 integration check tool output | `python tools/mvp1_pc3_ar1_integration_check.py --mode integration` stdout | 답습 (Stage 4 합의 §1.3 답습) |
| ledger entry | (정식 등록 0건 — Backlog #5 ADR-012 §2.2 분리) | 후보 한정 |

### 6.4 ledger entry 후보 한정 매트릭스 (정식 등록 0건, Backlog #5 분리)

| 후보 enum | 본 brief 시점 |
|---------|----------|
| `pc3_ar1_integration_implementation` | 후보 한정 (mvp1.md §5.2 답습) |
| `pc3_violation_detected` | 후보 한정 |
| `ar1_fail_closed_triggered` | 후보 한정 |
| `mvp1_ci_integration_pass` | 후보 한정 |
| `phase_alpha_4_implementation_evidence` | 후보 한정 |
| **합산** | **5 후보 한정 — 정식 등록 0건 (Backlog #5 분리)** |

### 6.5 본 §6 의 *범위 한계*

본 §6 의 어떤 항목도:

- (i) ADR-011 §2.1 (a)~(e) 5 조건 어느 것도 *재검증* 시키지 않으며 (Layer C 답습 한정),
- (ii) Phase α-4 R-1 Local Validation Evidence 본문 어느 줄도 *작성* 시키지 않으며 (Step 3 = 사용자 명시 결정 후),
- (iii) Evidence Artifact 형식 어느 것도 *변경* 시키지 않으며,
- (iv) 5 ledger entry enum 후보 어느 것도 *정식 등록* 시키지 않는다 (Backlog #5 분리).

---

## 7. 사용자 명시 5 금지 영역 × Step 분리 매트릭스

### 7.1 본 brief 영역 5/5 위반 0건 영구 답습 매트릭스

| # | 금지 영역 | 본 brief 작성 시점 (Step 0) | Step 1.4.1.a ~ Step 1.4.2.c | Step 2 | Step 3 | Step 4 ~ Step 6 |
|---|---------|------------------|------------------------|--------|--------|------------------|
| #1 | CI workflow 변경 | ✅ 0건 | ✅ 0건 (self-check 한정) | ✅ 0건 | ✅ 0건 (evidence 신규 작성 한정) | ✅ 0건 (합의 보고서 / 메타 갱신 한정) |
| #2 | runtime code 변경 | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| #3 | actual run 재실행 | ✅ 0건 | ✅ 0건 (local 한정) | ✅ 0건 (4 prerequisite runs 답습 enumerate 한정) | ✅ 0건 | ✅ 0건 |
| #4 | Operational Readiness PASS | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| #5 | Hermes PMO 격상 | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 | ✅ 0건 |
| **합산** | **5/5** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** |

### 7.2 추가 분리 영역 위반 0건 영구 답습 매트릭스

본 §0.4 추가 분리 영역 enumerate 답습 — 본 brief 작성 시점 + 본 brief 발효 후 Step 0 ~ Step 6 전체 영역 = **분리 명시 + 위반 0건 영구 답습**:

| 분리 영역 | Step 0 ~ Step 6 영역 |
|---------|------------------|
| Phase α-4 자동 실 진입 | 영구 답습 (본 brief = 계획 한정) |
| R-1 영역 7 artifacts × 1593줄 본문 변경 | 영구 답습 |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | 영구 답습 |
| PC-4 / AR-2 / AR-3 진입 | 영구 답습 (Backlog #1+#2 / Backlog #3 분리) |
| ST-1 / ST-2 / ST-4 / ST-5 진입 | 영구 답습 (Backlog 분리) |
| S-2 gitleaks 도입 | 영구 답습 (Backlog #1 분리) |
| Stage 5 (G3-7) 자동 진입 | 영구 답습 (Stage 4 후속 권고) |
| branch protection 변경 | 영구 답습 (AR-2 = Backlog #3) |
| dev 환경 강제 / `pre-commit install` 의무화 | 영구 답습 |
| 신규 workflow 신설 / `pull_request_target` 도입 | 영구 답습 |
| GitHub Actions secrets 사용 도입 | 영구 답습 (F-금지 #1 영구 답습) |
| Hermes upstream Dockerfile 변경 | 영구 답습 |
| Production `docker-compose.yml` 신설 / 변경 | 영구 답습 |
| 실 secret material commit | 영구 답습 (FAKE_TEST_SECRET marker 답습) |
| Tier-1/2/3 catalog 변경 / 확장 | 영구 답습 |
| `.importlinter` 본문 변경 / TR-1 ~ TR-5 발화 | 영구 답습 |
| Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 | 영구 답습 |
| 합산 284 합의 조건 변경 | 영구 답습 |

### 7.3 본 §7 의 *범위 한계*

본 §7 의 어떤 항목도:

- (i) 5 사용자 명시 금지 영역 어느 것도 *진입* / *해소* 시키지 않으며,
- (ii) 추가 분리 영역 어느 것도 *진입* / *통합* 시키지 않는다.

---

## 8. 합산 284 합의 조건 답습 매트릭스

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
| Stage 3 — α-1+2+3 parallel actual entry | `7917e4a` | 25 (C-ξ-1 ~ C-ξ-25) | 0건 |
| **Phase α-4 R-1 진입 조건 점검** | **`1c365e7`** | **33 (C-π-1 ~ C-π-33)** | **0건** ✅ |
| **합산** | **12 합의** | **284 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| C-ε-9 / C-π-x (Phase α-4 실 진입 = 사용자 명시 결정 영역) | ✅ 본 brief = step 분할 계획 한정 (실 진입 자동 0건) |
| C-ε-10 / C-π-x (R-1 영역 7 artifacts × 1593줄 본문 변경 0건) | ✅ 변경 0건 |
| C-ε-16 (R-4 / R-5 / R-7 본문 변경 0건) | ✅ 변경 0건 (α-1+2+3 evidence §5.1 답습) |
| C-ε-19 ~ C-ε-20 (Phase α-1 / α-2 / α-3 자동 재진입 / 재실행 0건) | ✅ 0/0 |
| C-ε-27 ~ C-ε-28 (5 영구 핵심 제약 + Provider Liquidity 5-way 보존) | ✅ 5/5 + 5/5 |
| C-π-x (5 진입 적격성 5/5 충족 + 이중 evidence 충족) | ✅ 답습 한정 |
| C-π-x (Reviewer-only 단축 합의 적격 권위 확정) | ✅ 답습 한정 |
| C-ι-x (Layer C 30 조건) | ✅ 답습 한정 (재발효 0건) |
| C-λ-x (Layer D 25 조건) | ✅ 답습 한정 (재선언 0건) |
| C-ν-x (Stage 2 α-1+2+3 1순위 계획 25 조건) | ✅ 답습 한정 — **본 brief 의 framing 모법** |
| C-ξ-11 ~ C-ξ-22 (α-1+2+3 evidence 직접 답습 매트릭스) | ✅ 답습 한정 |

### 8.3 본 §8 의 *범위 한계*

본 §8 = **284 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = 본 brief 그대로 승인 합의 보고서 작성 시 도입 가능 (Reviewer-only 단축 합의 적격 후보) — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정.

---

## 9. 합의 형태 권고 + 풀 3+1 승격 트리거

### 9.1 본 brief 의 합의 형태 권고 매트릭스

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| **(a) Reviewer-only 단축 합의** | 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ✅ **권고** — 트리거 0건 발화 예상 + 본 brief = framing 차이 한정 (Stage 1.5 → Stage 2) + 권위 결정 0건 |
| (b) 풀 3+1 합의 | 트리거 中 1+ 발화 | 본 brief 시점 미발화 예상 |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | 본 brief 시점 적용 영역 아님 |

### 9.2 풀 3+1 승격 트리거 후보 검토 (예상 0/16 발화)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 본 brief 가 합산 284 합의 조건 中 1+ *재결정* 권고 | 0건 — 답습 한정 |
| T-2 | 본 brief 가 사용자 명시 5 금지 영역 中 1+ *해소* 권고 | 0건 |
| T-3 | 본 brief 가 Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 |
| T-4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | 0건 |
| T-5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | 0건 |
| T-6 | 본 brief 가 T3 영역 진입 권고 | 0건 |
| T-7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | 0건 |
| T-8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 | 0건 |
| T-9 | 본 brief 가 Hermes upstream root of trust 변경 권고 | 0건 |
| T-10 | 본 brief 가 PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0건 |
| T-11 | 본 brief 가 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | 0건 |
| T-12 | 본 brief 가 신규 workflow 신설 / `pull_request_target` 도입 권고 | 0건 |
| T-13 | 본 brief 가 Stage 5 (G3-7) 자동 진입 권고 | 0건 |
| T-14 | 본 brief 가 Phase α-1 / α-2 / α-3 actual run 재실행 권고 | 0건 |
| T-15 | 본 brief 가 α-1+2+3 evidence / α-4 진입 조건 점검 합의 본문 변경 권고 | 0건 |
| T-16 | 본 brief 가 Step 분할 토폴로지에서 사용자 명시 5 금지 영역 진입 권고 | 0건 — Step 0 ~ Step 6 전체 영역 5/5 위반 0건 영구 답습 |
| **합산** | **16** | **✅ 0/16 발화 예상 — Reviewer-only 단축 합의 적격 확정** |

### 9.3 본 §9 의 *범위 한계*

본 §9 의 어떤 항목도:

- (i) 합의 형태 어느 것도 *자동 결정* 하지 않으며 (사용자 명시 결정 영역),
- (ii) 풀 3+1 승격 트리거 어느 것도 *발화* 시키지 않는다.

---

## 10. 금지 사항

### 10.1 본 brief 자체 금지 사항 (사용자 명시 답습)

본 brief 작성 시점 금지 영역:

- ❌ **CI workflow 변경** (사용자 명시 5 금지 #1) — 7 artifacts × 1593줄 답습 보존
- ❌ **runtime code 변경** (사용자 명시 5 금지 #2)
- ❌ **actual run 재실행** (사용자 명시 5 금지 #3) — 4 prerequisite runs 답습 한정
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ Phase α-4 자동 실 진입 (본 brief = *step 분할 계획 한정*)
- ❌ Phase α-1 / α-2 / α-3 자동 재진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ α-1+2+3 evidence 본문 변경 (`7b3d40a` 답습)
- ❌ α-4 진입 조건 점검 합의 본문 변경 (`1c365e7` 답습)
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 / 본 brief 신규 후보 trigger 자동 발화
- ❌ 합산 284 합의 조건 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 어느 것도 *최종 확정*
- ❌ event enum 정식 등록 (Backlog #5 분리)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출 (Group α 합의 C-11 답습)
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

### 10.2 본 brief 발효 *후* Step 0 ~ Step 6 의무 금지 사항 (Stage 2 α-1+2+3 §10.2 답습)

본 brief 발효 후 Step 0 ~ Step 6 어느 단계도 (사용자 명시 결정 영역):

- ❌ **사용자 명시 5 금지 영역 진입 0건** — Step 0 ~ Step 6 전체 영역 영구 만족
- ❌ **R-1 영역 7 artifacts × 1593줄 본문 어느 줄도 변경 0건** — cycle 옵션 (i) 답습 한정
- ❌ **R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 변경 0건**
- ❌ **`src/` 본문 변경 0건** + facade.py real 본문 작성 0건 (Backlog #4 분리)
- ❌ **3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경 0건**
- ❌ **R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 0건**
- ❌ **`.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경 0건**
- ❌ **R-7 docker secret block 본문 변경 0건**
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 0건**
- ❌ **Stage 5 (G3-7) 자동 진입 0건**
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건**
- ❌ **threshold 자동 *고정* 0건**
- ❌ **Rollback Trigger / TR-1 ~ TR-5 / 본 brief 신규 후보 trigger 자동 발화 0건**
- ❌ **합산 284 합의 조건 자동 변경 0건**
- ❌ **Layer A ~ Stage 3 / Phase α-4 (직전 + 진입 조건 점검) / Group A / Group D 합의 본문 변경 0건**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 0건**
- ❌ **Group α 14 결정 영역 *재결정* 0건**
- ❌ **Group I / Group β / γ-1 / γ-2 자동 진입 0건**
- ❌ **token rotation 정책 자동 결정 0건**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 0건**
- ❌ **commit signing 도입 0건**
- ❌ **`pull_request_target` workflow 도입 0건**
- ❌ **GitHub Actions secrets 사용 도입 0건** (F-금지 #1 영구 답습)
- ❌ **Hermes upstream Dockerfile 변경 0건**
- ❌ **Production `docker-compose.yml` 신설 / 변경 0건**
- ❌ **실 secret material commit 0건** (FAKE_TEST_SECRET marker 답습)
- ❌ **event enum 정식 등록 0건** (Backlog #5 분리)
- ❌ **ADR 본문 자동 갱신 0건** (cross-reference 답습 한정)
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 0건**
- ❌ **신규 actual run 자동 trigger 0건** — Step 0 ~ Step 6 전체 영역 영구 만족
- ❌ **Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 0건**
- ❌ **Phase β / γ 자동 진입 0건**

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (16/16 풀 3+1 트리거 0건 발화 예상) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-17-phase-alpha-4-r1-step-division.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → **풀 3+1 합의 진입** (Stage 2 α-1+2+3 D-2 (b) 답습) | 풀 3+1 합의 보고서 작성 |
| (E) | 본 brief 승인 → **풀 3+1 + 외부 LLM 1+ 합의** (D-2 (c) 답습) | 풀 3+1 + 외부 LLM blind 의뢰 진입 |
| (F) | 본 brief 보류 → Phase α-4 실 진입 여부 brief (α-4 Stage 3 framing) 작성 | α-4 Stage 3 brief 영역 |
| (G) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 결정 영역 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 11.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 R-1 *실 진입 step 분할 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 R-1 실 진입 step 분할 (DRAFT, 본 commit)              ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성 (옵션 (A))
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 실 진입 여부 brief (α-4 Stage 3 framing) 작성                    ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 R-1 실 진입 (Step 1 ~ Step 6 — 본 brief §2 답습)                 ← 본 brief 영역 외
```

### 11.2 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. 풀 3+1 합의 진입."
- (E): "옵션 (E) 로 진행해주세요. 풀 3+1 + 외부 LLM 1+ 합의 진입."
- (F): "옵션 (F) 로 진행해주세요. Phase α-4 실 진입 여부 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (H): "옵션 (H) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (I): "옵션 (I) 로 진행해주세요. 세션 종료."

### 11.3 본 §11 의 *범위 한계*

본 §11 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 12. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("Phase α-4 R-1 실 진입 step 분할 brief를 작성해주세요. 범위는 R-1 CI workflow 통합을 실제 구현하기 전에 step 분할, 수정 범위, 테스트 범위, rollback trigger, evidence 기준을 정리하는 것입니다. 아직 CI workflow 변경, runtime code 변경, actual run 재실행, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요.") |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — CI workflow 변경 0건 / runtime code 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| α-4 진입 조건 점검 합의 답습 (`1c365e7`) | ✅ (33 조건 C-π-1 ~ C-π-33 변경 0건) |
| 직전 α-4 합의 답습 (`e59a565`) | ✅ (29 조건 C-ε-1 ~ C-ε-29 변경 0건) |
| α-1+2+3 local validation evidence 답습 (`7b3d40a`) | ✅ (486줄 본문 변경 0건 + 12/12 PASS 결과 enumerate 한정) |
| Stage 2 α-1+2+3 1순위 계획 합의 framing 답습 (`88ccf79`) | ✅ (25 조건 C-ν-1 ~ C-ν-25 답습 — framing 모법 답습) |
| 합산 284 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33) |
| Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 본문 변경 | ✅ 0건 |
| §5.5 9 sub-수단 본문 채택 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 (PoC 답습) |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 (α-1+2+3 evidence 답습) |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| α-1+2+3 evidence / α-4 진입 조건 점검 합의 본문 변경 | ✅ 0건 |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| Layer B 18 Rollback Trigger + TR-1 ~ TR-5 + 본 brief 신규 후보 5 trigger 발화 | ✅ 0/28 발화 |
| 풀 3+1 트리거 발화 | ✅ 0/16 발화 예상 |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 (사용자 명시 5 금지 #3 답습) |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| Step 0 ~ Step 6 × 5 금지 = 35/35 충돌 0 검증 | ✅ §7.1 답습 |
| Step 0 ~ Step 6 cycle 옵션 권고 (i) 직렬 cycle | ✅ §2.3 답습 |
| 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 *최종 확정 0건* | ✅ (사용자 명시 결정 영역) |
| framing 차이 명시 | ✅ (α-4 Stage 1.5 → α-4 Stage 2 framing 전환 명시) |

---

## 13. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-4 R-1 진입 조건 점검 합의 (`1c365e7` 후속 23 APPROVE AS BRIEF — Reviewer-only 단축, 33 조건 C-π-1 ~ C-π-33) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *실 진입 Step 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정* 의 brief 준비안 (DRAFT)** = **Phase α-4 자체의 Stage 2 등가 framing** (α-1+2+3 Stage 2 `88ccf79` 패턴 답습). **사용자 명시 5 금지** (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **Step 0 ~ Step 6 분할 권고 (§2)** = Step 0 사전 점검 (본 brief 자체) + Step 1.4.1.a/b/c (PC-3 CI step 통합 답습 검증 — 3 workflow self-check) + Step 1.4.2.a/b/c (AR-1 fail-closed 통합 답습 검증 — integration tool + PASS fixture + FAIL fixture 2개 self-check) + Step 2 (4 prerequisite runs PASS evidence 답습 enumerate 한정, 재실행 0건) + Step 3 (Phase α-4 R-1 Local Validation Evidence 본문 작성 — α-1+2+3 evidence `7b3d40a` 486줄 패턴 답습) + Step 4 (합의 형태 결정 — 사용자 명시 결정 영역) + Step 5 (합의 보고서 작성) + Step 6 (메타 commit + push) + cycle 옵션 권고 = (i) 직렬 cycle. **수정 범위 매트릭스 (§3)** = R-1 영역 1593줄 (7 artifacts) 본문 변경 0건 영구 답습 + R-4/R-5/R-7 1192줄 (13 file) 변경 0건 + `src/` runtime code 변경 0건 + 신규 작성 영역 3 종 한정 (본 brief 1건 + Step 3 evidence 1건 + Step 5 합의 보고서 1건 — Step 6 메타 갱신 소량). **테스트 범위 매트릭스 (§4)** = 12 step × 평균 1 ~ 3 검증 영역 — 모두 local self-check + 답습 enumerate 한정 + 신규 actual run trigger 0건 영구 답습 + 4 영역 × 5 금지 = 20/20 충돌 0 + threshold 5/5 후보 한정 (고정 0건). **Rollback Trigger 매트릭스 (§5)** = Layer B 18 trigger + TR-1 ~ TR-5 + 본 brief 신규 후보 5 trigger = **합산 28 trigger × 0건 발화 영구 답습** (R-1 직접 영향 7 中 발화 0건 예상) + PC-4 / AR-2 / AR-3 / Stage 5 별도 backlog trigger 4개 분리 명시. **Evidence 기준 매트릭스 (§6)** = ADR-011 §2.1 (a)~(e) × R-1 영역 = 5/5 답습 충족 (Layer C 답습 한정, 재검증 0건) + Phase α-4 R-1 Local Validation Evidence 작성 기준 (Step 3 영역 — 약 400~600줄 + 11 섹션 구조 + 본문 변경 0건 검증 + 메타 검증 ≥ 15 항목 + α-1+2+3 evidence 패턴 답습) + Evidence Artifact 형식 5 종 답습 (GitHub Actions run JSON + Local self-check Markdown + Markdown evidence + Stage 4 integration tool stdout + ledger entry 후보 한정) + ledger entry 5 후보 한정 (정식 등록 0건, Backlog #5 분리). **사용자 명시 5 금지 × Step 분리 매트릭스 (§7)** = Step 0 ~ Step 6 × 5 금지 = **35/35 충돌 0 영구 답습** + 추가 분리 영역 (Phase α-4 자동 진입 / R-1 + R-4/R-5/R-7 + src 본문 변경 / PC-4/AR-2/AR-3/Stage 5 / branch protection / dev 환경 / GitHub Actions secrets / Hermes upstream Dockerfile / Production docker-compose / 실 secret material / Tier 변경 / `.importlinter` 본문 / TR 발화 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 모두 영구 답습). **합산 284 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33). **합의 형태 권고** = (a) Reviewer-only 단축 합의 (16/16 풀 3+1 트리거 0건 발화 예상). **본 brief 자체 금지 ≥ 40 + 본 brief 발효 후 Step 0 ~ Step 6 의무 금지 ≥ 30** enumerate. **본 brief 는 Phase α-4 어느 Step 도 *실 진입* 시키지 않으며, R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며, `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며, 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 284 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 어느 것도 *최종 확정* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — (A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점) / (B) brief 수정 / (C) 부분 채택 / (D) 풀 3+1 / (E) 풀 3+1 + 외부 LLM / (F) α-4 Stage 3 brief 작성 / (G) backlog 전환 / (H) brief 폐기 / (I) 세션 종료.

---

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §11 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **CI workflow 변경 0건** (3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 = 7 artifacts × 1593줄 답습 보존)
- ❌ **runtime code 변경 0건** (`src/` + facade.py 41줄 placeholder 답습 보존)
- ❌ **actual run 재실행 0건** (4 prerequisite runs PASS 답습 한정)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ Phase α-4 자동 실 진입 0건 (본 brief = step 분할 계획 한정)
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 284 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence 본문 변경 0건 (`7b3d40a` 답습)
- ❌ α-4 진입 조건 점검 합의 본문 변경 0건 (`1c365e7` 답습)
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
- ❌ threshold *고정* 0건 (5/5 후보 한정)
- ❌ event enum 정식 등록 0건 (Backlog #5 분리)
- ❌ Rollback Trigger / TR-1 ~ TR-5 / 본 brief 신규 후보 5 trigger 자동 발화 0건 (28/28)
- ❌ 풀 3+1 트리거 자동 발화 0건 (0/16 예상)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 어느 것도 *최종 확정* 0건 (사용자 명시 결정 영역)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ git commit / push 0건
