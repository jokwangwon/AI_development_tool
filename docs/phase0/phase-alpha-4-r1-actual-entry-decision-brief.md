# Phase α-4 R-1 *실 진입 여부* Brief (DRAFT — Stage 3 framing)

> **본 문서는 Phase α-4 R-1 Local Validation Evidence 합의 (`b264580` APPROVE — Reviewer-only 단축, 31 조건 C-σ-1 ~ C-σ-31) 발효 후속, Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *실 진입 *여부* 검토* 한정 brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 1 (`f91ef4b` + `e59a565`) = "*Can* we enter Phase α-4 영역?" — 영역 정의 + 진입 적격성 5 조건 검토 한정
> - α-4 Stage 1.5 (`7a289fa` + `1c365e7`) = "*Are entry conditions still satisfied after α-1+2+3 evidence?*" — 조건 재검토 한정
> - α-4 Stage 2 (`ed1d1b6` + `52a05cb`) = "*How* should Phase α-4 R-1 실 진입 be staged?" — Step 0 ~ Step 6 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정
> - α-4 LVE (`4ce5a0b` + `b264580`) = "*Is local validation complete?*" — Step 1 + Step 2 + Step 3 local 검증 51/51 PASS evidence 한정
> - **본 brief = "*Should* we enter Phase α-4 R-1 actual implementation (Stage 4) now?"** — 실 진입 *여부 검토 한정* (Step Division §1.3 답습 명시한 Stage 3 framing)
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) Phase α-4 Stage 4 (실 구현) 을 *발효* 시키지 않으며, (ii) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, (iii) Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 = **합산 353 합의 조건** 中 어느 것도 *해소* / *변경* 시키지 않으며, (iv) 사용자 명시 5 금지 中 어느 것도 *해소* 시키지 않으며, (v) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 어느 것도 *발생시키지 않으며*, (vi) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-local-validation-evidence.md` (commit `b264580` APPROVE, 31 조건 C-σ-1 ~ C-σ-31 — **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄, 51/51 PASS)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-step-division.md` (commit `52a05cb`, 38 조건 C-ρ-1 ~ C-ρ-38 — Stage 3 framing 모법)
- `docs/phase0/phase-alpha-4-r1-step-division-brief.md` (commit `ed1d1b6`, 871줄)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-entry-condition.md` (commit `1c365e7`, 33 조건 C-π-1 ~ C-π-33)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (commit `e59a565`, 29 조건 C-ε-1 ~ C-ε-29)
- `docs/phase0/phase-alpha-123-local-validation-evidence.md` (commit `7b3d40a`, 486줄, 12/12 PASS)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (Stage 4 PC-3 + AR-1 합의 APPROVE)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 C (Hermes PMO Activation 12 조건)

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "1 번 작업으로 진행 — Phase α-4 R-1 실제 CI workflow 통합 진입" → "Stage 3 실 진입 여부 brief 작성 (DRAFT — 5 금지 모두 보존)"

### 0.2 사용자 명시 5 금지 답습

1. ❌ **CI workflow 변경 금지** — 7 artifacts × 1593줄 답습 보존 (본 brief = DRAFT 영역 한정)
2. ❌ **runtime code 변경 금지** — `src/` + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존
3. ❌ **actual run 재실행 금지** — 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 답습 한정 — 신규 trigger 0건
4. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리
5. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C 12 조건 미진입 영구 답습

### 0.3 본 brief 가 *하는* 것

1. LVE 합의 (`b264580` APPROVE, 31 조건 C-σ-1 ~ C-σ-31) 발효 후속 — **Stage 3 실 진입 여부 검토 한정** (§1)
2. **Phase α-4 R-1 실 진입 (Stage 4) 정의** + 현재 상태 매트릭스 (§2)
3. **5 금지 영역 해소 매트릭스** (실 진입 시점 — 권고 한정, 본 brief 발효 시점 해소 0건) (§3)
4. **실 진입 Pro / Con 매트릭스** (§4)
5. **실 진입 시 필요한 작업 후보 enumerate** — Stage 4 직접 작업 + 간접 backlog (§5)
6. **Rollback Trigger 분석 매트릭스** — Layer B 18 + TR-1~TR-5 + Step Division 신규 후보 5 trigger 발화 가능성 (§6)
7. **합의 형태 권고 + 풀 3+1 승격 트리거 분석** — 본 brief 자체 + Stage 4 실 진입 시점 별도 분석 (§7)
8. **사용자 명시 5 금지 × 본 brief 분리 매트릭스** — 본 brief 영역 5/5 위반 0건 영구 답습 (§8)
9. **합산 353 합의 조건 답습 매트릭스** (§9)
10. **본 brief 자체 금지 + brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역) (§11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **CI workflow 변경 (0건)** — 3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 = 7 artifacts × 1593줄 답습 보존 + 변경 / 추가 / 삭제 0건
- ❌ **runtime code 변경 (0건)** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존
- ❌ **actual run 재실행 (0건)** — 4 prerequisite runs SUCCESS 답습 한정 + 신규 GitHub Actions actual run trigger 0건
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (직전 LVE + Step Division + α-4 진입 조건 점검 답습 패턴 보존)**:

- ❌ **Phase α-4 Stage 4 (실 구현) 자동 진입 (0건)** — 본 brief = *실 진입 여부 검토 한정* (실 진입 = 사용자 명시 결정 영역)
- ❌ **5 금지 영역 *해소* (0건)** — 본 brief 자체 = DRAFT — 5 금지 모두 영구 보존
- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — `secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + `tools/mvp1_pc3_ar1_integration_check.py` 298 + 3 fixture 89 = 1593줄 답습 보존
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (LVE §5.4 답습)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **PC-4 / AR-2 / AR-3 / Stage 5 진입 (0건)** — Backlog #1+#2 / Backlog #3 / Stage 4 후속 권고 분리 답습
- ❌ **ST-1 / ST-2 / ST-4 / ST-5 진입 (0건)** — Backlog 분리
- ❌ **S-2 gitleaks 도입 (0건)** — Backlog #1 분리
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 영역 별도 풀 3+1
- ❌ **dev 환경 강제 (0건) + `pre-commit install` 의무화 도입 (0건)**
- ❌ **신규 workflow 신설 (0건) + `pull_request_target` 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습 (G3-7 (i))
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정 답습
- ❌ **실 secret material commit (0건)** — FAKE_TEST_SECRET marker 답습
- ❌ **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`951a5b1`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 ~ α-3 / Phase α-4 (직전 + 진입 조건 점검 + Step Division) / α-1+2+3 evidence (`7b3d40a`) / LVE (`4ce5a0b` + `b264580`) 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **Phase α-1 / α-2 / α-3 자동 재진입 (0건)** — α-1+2+3 evidence + LVE 답습
- ❌ **Layer C 재발효 (0건) / Layer D 재선언 (0건) / MVP-1 PASS 재선언 (0건)**
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)** — 별도 commit 분리 (사용자 명시 결정 후 진입)
- ❌ **git commit / push (0건)** — 사용자 명시 결정 후 진입
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **token rotation 정책 / GitHub plan 가용성 자동 결정 (0건)**
- ❌ **threshold *고정* (0건)** — 후보 한정 유지
- ❌ **event enum 정식 등록 (0건)** — Backlog #5 ADR-012 §2.2 분리
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **신규 actual run 자동 trigger (0건)** — 4 prerequisite runs 답습 한정
- ❌ **합산 353 합의 조건 자동 변경 (0건)**

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-4 Stage 4 (실 구현) 을 *발효* 시키지 않으며,
- (ii) 합산 353 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iii) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (iv) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (v) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vi) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (vii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (viii) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (ix) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (x) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 어느 것도 *발생시키지 않으며*,
- (xi) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 trigger 어느 것도 *발화* 시키지 않으며,
- (xii) 실 진입 여부 결정 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 실 진입 여부 *권위 권고 한정***. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (Phase α-4 LVE 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `e59a565` (2026-05-14) | Phase α-4 R-1 직전 brief 합의 APPROVE AS BRIEF — 29 조건 C-ε-1 ~ C-ε-29 | ✅ 답습 한정 |
| `f91ef4b` (2026-05-14) | Phase α-4 R-1 진입 brief DRAFT (751줄) | ✅ 답습 한정 |
| `eb01bc4` (2026-05-16) | Layer C 발효 (30 조건 C-ι-1 ~ C-ι-30) | ✅ 답습 한정 |
| `951a5b1` (2026-05-16) | Layer D 재진입 평가 (25 조건 C-λ-1 ~ C-λ-25) | ✅ 답습 한정 |
| `542e77e` (2026-05-16) | Stage 1 — Phase α 통합 계획 합의 (25 조건 C-μ-1 ~ C-μ-25) | ✅ 답습 한정 |
| `88ccf79` (2026-05-16) | Stage 2 — α-1+2+3 1순위 계획 합의 (25 조건 C-ν-1 ~ C-ν-25) | ✅ 답습 한정 |
| `7917e4a` (2026-05-16) | Stage 3 — α-1+2+3 parallel actual entry 합의 (25 조건 C-ξ-1 ~ C-ξ-25) | ✅ 답습 한정 |
| `7b3d40a` (2026-05-16) | α-1+2+3 Local Validation Evidence (486줄, 12/12 PASS) | ✅ 답습 한정 |
| `7a289fa` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 brief DRAFT (566줄) | ✅ 답습 한정 |
| `1c365e7` (2026-05-17) | Phase α-4 R-1 진입 조건 점검 합의 APPROVE AS BRIEF — 33 조건 C-π-1 ~ C-π-33 | ✅ 답습 한정 |
| `ed1d1b6` (2026-05-17) | Phase α-4 R-1 Step Division brief DRAFT (871줄) | ✅ 답습 한정 |
| `52a05cb` (2026-05-17) | Phase α-4 R-1 Step Division 합의 APPROVE AS BRIEF — 38 조건 C-ρ-1 ~ C-ρ-38 | ✅ 답습 한정 |
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 APPROVE — 31 조건 C-σ-1 ~ C-σ-31 | ✅ **본 brief 의 발효 trigger** |
| `22b5c1c` (HEAD, 2026-05-17) | CONTEXT — Phase α-4 R-1 LVE status 기록 entry | ✅ 답습 한정 |

### 1.2 LVE 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-17 후속 25 |
| 합의 판정 | APPROVE (Reviewer-only 단축 — 16/16 풀 3+1 트리거 0건 발화) |
| 합의 조건 | **31 조건 (C-σ-1 ~ C-σ-31)** |
| 합산 51/51 Local 검증 PASS | ✅ (PC-3 14/14 + AR-1 37/37) |
| 4 prerequisite runs 답습 | ✅ 4/4 SUCCESS (재실행 0건) |
| 사용자 명시 5 금지 위반 | **5/5 0건** |
| 5 영구 핵심 제약 보존 | **5/5 100% 보존** |
| Provider Liquidity 5-way 보존 | **5/5 100% 보존** |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| 본 brief trigger 의미 | Phase α-4 R-1 영역 *실 진입 직전 local 검증 권위 확정* → **실 진입 여부 결정 (= 본 brief)** 의 framing 정당화 |

### 1.3 5 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 가능성 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 조건 C-ε-1 ~ C-ε-29 | "*Can* we enter Phase α-4 영역?" |
| α-4 Stage 1.5 (조건 재검토) | Phase α-4 R-1 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 조건 C-π-1 ~ C-π-33 | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (실 진입 step 분할) | Phase α-4 R-1 Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 조건 C-ρ-1 ~ C-ρ-38 | "*How* should Phase α-4 R-1 실 진입 be staged?" |
| α-4 Stage 2.5 (Local Validation Evidence) | Phase α-4 R-1 LVE | `4ce5a0b` + `b264580` | APPROVE | 31 조건 C-σ-1 ~ C-σ-31 | "*Is local validation complete?*" |
| **α-4 Stage 3 (본 brief)** | **Phase α-4 R-1 *실 진입 여부* brief** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* we enter Phase α-4 R-1 actual implementation (Stage 4) now?"** |
| α-4 Stage 4 (실 구현, 본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* Phase α-4 R-1 actual implementation" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 3 framing** (= Step Division §1.3 답습 명시):

- α-4 Stage 1 ↔ α-4 Stage 1.5 ↔ α-4 Stage 2 ↔ α-4 Stage 2.5 ↔ **α-4 Stage 3 (본 brief, 실 진입 여부 검토)** ↔ α-4 Stage 4 (실 구현, 사용자 명시 결정 영역)
- 본 brief 의 단일 책무: **"실 진입 (Stage 4) 을 지금 시작할 것인가?"** + **"실 진입 시 5 금지 #1 / #3 어떻게 해소?"** + **"실 진입 Pro / Con / Rollback Trigger 어떻게 분석?"** 정리 한정
- 본 brief ≠ α-4 Stage 4 (실 구현 = 별도 단계, 본 brief 영역 외)
- 본 brief ≠ Phase α-4 자동 진입 발효 (사용자 명시 결정 영역)
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-17 후속 26 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 5 금지 #4) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 5 금지 #5) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local INI 구조 8/8 PASS evidence 답습 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 |
| **Phase α-4 (R-1)** | **2순위 의존 — CI workflow 통합 (PC-3 + AR-1)** | ✅ local 51/51 PASS evidence 답습 + ⏳ **본 brief = α-4 Stage 3 (실 진입 여부 검토 한정)** |

---

## 2. Phase α-4 R-1 실 진입 (Stage 4) 정의

### 2.1 R-1 영역 = 현재 상태 매트릭스

| 영역 | 현재 상태 | 본 brief 시점 |
|------|--------|----------|
| R-1 영역 7 artifacts × 1593줄 본문 | ✅ 이미 구현 완료 (brief 명세 100% 일치) | 답습 한정 |
| `secret-hygiene-egress-redaction.yml` 694줄 | ✅ commit `ffa0cbf` | 답습 |
| `provider-adapter-enforcement.yml` 186줄 | ✅ commit `6d95cad` | 답습 |
| `provider-url-scanner.yml` 326줄 | ✅ commit `c3c54ef` | 답습 |
| `mvp1_pc3_ar1_integration_check.py` 298줄 | ✅ commit `34b50db` | 답습 |
| 3 fixture (PASS 30 + FAIL pc3 31 + FAIL ar1 28 = 89줄) | ✅ commit `34b50db` | 답습 |
| 4 prerequisite GitHub Actions runs | ✅ 4/4 SUCCESS (Layer C `eb01bc4` 발효 시점 답습) | 답습 한정 — 재실행 0건 |
| local validation evidence | ✅ 51/51 PASS (LVE `4ce5a0b` 답습) | 답습 한정 |
| α-1+2+3 evidence 답습 | ✅ 12/12 PASS (`7b3d40a` 답습) | 답습 한정 |

**결론**: R-1 영역 본문은 **이미 구현 + 4 prerequisite runs PASS + local 51/51 PASS + α-1+2+3 evidence 12/12 PASS** — 본 brief 시점 *실 진입 가능 상태* (technical pre-conditions 모두 충족).

### 2.2 "실 진입 (Stage 4)" 의 정의

Stage 4 "실 구현" = R-1 영역 *evidence-only 상태* → **운영 진입 상태** 전환. 구체적 작업 후보 (Stage 4 영역 — 본 brief 외):

| Stage 4 작업 후보 | 영역 | 5 금지 영역 해소 여부 |
|---------------|----|------------------|
| (a) 3 MVP-1 workflow 본문 step 추가 / 수정 (예: 신규 entry step 추가, 의존성 보강) | CI workflow 변경 | ✅ 5 금지 #1 해소 |
| (b) integration check tool 본문 step 추가 / 수정 | CI workflow 변경 | ✅ 5 금지 #1 해소 |
| (c) Stage 4 sub-step 4.3 PC-4 local pre-commit hook 활성화 | `.pre-commit-config.yaml` 신설 + `tools/doctor.py` 신설 | ⚠️ Backlog #1+#2 영역 (별도) |
| (d) Stage 4 sub-step 4.4 AR-2 branch protection rule | GitHub branch protection API 호출 | ⚠️ Backlog #3 T3 영역 (별도) |
| (e) AR-3 자동 revert bot | CODEOWNERS + bot 설정 | ⚠️ Backlog #3 T3 영역 (별도) |
| (f) 신규 actual GitHub Actions run trigger (PR open / push event) | GitHub Actions 실행 | ✅ 5 금지 #3 해소 |
| (g) 3 MVP-1 workflow Required check 으로 등록 (AR-2 영역 일부) | branch protection 변경 | ⚠️ Backlog #3 T3 영역 (별도) |
| (h) Stage 5 (G3-7 4 항목 후속 권고) 진입 | secret reset rotate / forking / pull_request_target / commit signing | ⚠️ Stage 4 후속 권고 영역 (별도) |

**해석**: Stage 4 "실 진입" 의 *최소 영역* = (a) + (b) (CI workflow 본문 변경) — 5 금지 #1 해소. *최대 영역* = (a) ~ (h) 모두 — 5 금지 #1 + #3 + branch protection + Backlog #1/#2/#3 흡수.

### 2.3 5 금지 해소 매트릭스 (실 진입 시점 — 권고 한정, 본 brief 시점 해소 0건)

| # | 금지 영역 | 실 진입 시 해소 여부 | 본 brief 시점 |
|---|---------|----------------|----------|
| 1 | CI workflow 변경 | **✅ 해소 (필수)** — Stage 4 작업 (a) + (b) | ❌ 해소 0건 (본 brief = DRAFT) |
| 2 | runtime code 변경 | ❌ 해소 0건 (Backlog #4 영역 — facade.py real 본문은 별도) | ❌ 해소 0건 |
| 3 | actual run 재실행 | **✅ 해소 (필수)** — Stage 4 작업 (f) | ❌ 해소 0건 |
| 4 | Operational Readiness PASS (Layer E) | ❌ 해소 0건 (MVP-6 영역) | ❌ 해소 0건 |
| 5 | Hermes PMO 격상 (Layer F) | ❌ 해소 0건 (ADR-008 부록 C 12 조건 미충족) | ❌ 해소 0건 |
| **합산** | **5** | **2 해소 (5 금지 #1 + #3)** | **0 해소 영구 답습** |

**중요**: 실 진입 시점 *해소 영역 = 2 / 5* — 5 금지 #1 (CI workflow 변경) + #3 (actual run 재실행). 5 금지 #2 / #4 / #5 = 영구 보존 (별도 영역).

### 2.4 본 §2 의 *범위 한계*

본 §2 = **실 진입 정의 *권위 권고 한정***. 실 진입 결정 / 5 금지 해소 = 사용자 명시 결정 영역. 본 brief = *권고* 한정 — 실 진입 발효 권위 0건.

---

## 3. 실 진입 Pro / Con 매트릭스

### 3.1 진입 Pro (실 진입 권고 근거)

| # | Pro | 답습 출처 |
|---|---|---------|
| P-1 | R-1 영역 7 artifacts × 1593줄 본문 = 이미 구현 완료 + local 51/51 PASS + 4 prerequisite runs 4/4 SUCCESS | LVE §3 + §4 답습 |
| P-2 | α-1+2+3 evidence 12/12 PASS 답습 한정 | LVE §1.3 답습 (`7b3d40a` 답습) |
| P-3 | Stage 4 PC-3 + AR-1 통합 진입 합의 (`docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md`) APPROVE 답습 | Stage 4 합의 답습 |
| P-4 | ADR-011 §2.1 (a)~(e) × R-1 = 5/5 답습 충족 (Layer C 답습 한정) | LVE §C-σ-x 답습 |
| P-5 | 5 진입 적격성 조건 (C-α4-1 ~ C-α4-5) 5/5 충족 (α-4 진입 조건 점검 답습) | `1c365e7` 답습 |
| P-6 | Step 0 ~ Step 6 분할 매트릭스 확정 (`52a05cb` 답습) | Step Division 답습 |
| P-7 | 합산 353 합의 조건 변경 0건 영구 답습 | §9 답습 |
| P-8 | 5 영구 핵심 제약 5/5 보존 (Hermes ≠ root of trust / 단일 source-of-truth / 수단·목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) | LVE §5.1 답습 |
| P-9 | Provider Liquidity 5-way 100% 보존 (R-1 = vendor-agnostic 표준 GitHub Actions = catalog / provider 직교) | LVE §5.2 답습 |

### 3.2 진입 Con (실 진입 *비*권고 / 신중 근거)

| # | Con | 답습 출처 |
|---|---|---------|
| C-1 | **5 금지 #1 (CI workflow 변경) 해소** — 사용자 명시 5 금지 中 첫 번째 해소 시점 — 신중 결정 필요 | 사용자 명시 5 금지 영구 답습 |
| C-2 | **5 금지 #3 (actual run 재실행) 해소** — 신규 GitHub Actions trigger 필요 | 사용자 명시 5 금지 영구 답습 |
| C-3 | 풀 3+1 합의 트리거 발화 가능성 — 본 brief = DRAFT 영역 한정이지만 Stage 4 실 진입 시점 = 트리거 발화 가능 (특히 T-2 "5 금지 영역 해소 권고" 발화) | §7.2 답습 |
| C-4 | branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / 신규 workflow / `pull_request_target` 영역 분리 명시 필요 — 영역 경계 불명확 시 트리거 T-10 발화 가능 | Step Division §5.5 답습 |
| C-5 | Backlog #1+#2 (PC-4) / Backlog #3 (AR-2/AR-3 T3) / Stage 5 (G3-7) 진입과 *분리* 또는 *흡수* 결정 필요 — 영역 흡수 시 T-13 발화 가능 | Step Division §5.5 답습 |
| C-6 | Hermes upstream Dockerfile 변경 0건 + Production `docker-compose.yml` 신설 0건 영구 답습 — Stage 4 시점에서도 보존 필요 | 영구 답습 |
| C-7 | F-금지 #1 영구 답습 — GitHub Actions secrets 사용 도입 0건 — Stage 4 시점에서도 보존 필요 (Stage 5 cycle 1~4 자기 검증 답습) | LVE §5.3 답습 |
| C-8 | Group α 합의 C-11 (외부 LLM 응답 = 입력 한정) + Group α C-14 (cross-vendor blind 의뢰 1+ 의무) 답습 — Stage 4 시점 외부 LLM 의뢰 필요 가능성 검토 필요 | Group α 답습 |
| C-9 | 인간 리뷰 의무 (Group α T3 영역) 자동 발화 가능성 — Stage 4 시점 검토 필요 | Group α 답습 |

### 3.3 Pro / Con 합산 평가 (권고 한정)

| 영역 | Pro | Con |
|------|---|---|
| Technical readiness | **9/9** (P-1~P-9) | 0/9 |
| 5 금지 해소 risk | 0/9 | **2/9** (C-1 + C-2) |
| Workflow / governance risk | 0/9 | **6/9** (C-3 ~ C-8) |
| Human review risk | 0/9 | 1/9 (C-9) |
| **합산** | **9 Pro** | **9 Con** |

**해석**: Pro = technical readiness 9/9 (실 진입 적격성 확정) / Con = 9 (대부분 governance / 5 금지 해소 risk). **Pro = Stage 4 작업 자체 가능성** + **Con = Stage 4 진입 결정 시점 신중 필요 영역**.

### 3.4 본 §3 의 *범위 한계*

본 §3 = **Pro / Con 매트릭스 *권위 권고 한정***. 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. 실 진입 시 필요한 작업 후보 enumerate

### 4.1 Stage 4 직접 작업 후보 매트릭스 (실 진입 시점)

| # | 작업 영역 | 5 금지 해소 | Backlog 분리 |
|---|--------|----------|------------|
| W-1 | 3 MVP-1 workflow 본문 step 추가 / 수정 / step 순서 변경 | #1 해소 | — |
| W-2 | integration check tool 본문 step 추가 / 수정 / mode 추가 | #1 해소 | — |
| W-3 | 3 fixture 본문 추가 / 수정 (PASS / FAIL 영역 보강) | #1 해소 | — |
| W-4 | 신규 actual GitHub Actions run trigger (push event / PR event) | #3 해소 | — |
| W-5 | 3 MVP-1 workflow `permissions: contents: read` 보강 | #1 해소 | Stage 5 cycle 4 영역 |
| W-6 | 3 MVP-1 workflow Required check 으로 등록 | (branch protection 변경) | Backlog #3 T3 영역 |
| W-7 | Stage 4 sub-step 4.3 PC-4 local pre-commit hook 활성화 | (`.pre-commit-config.yaml` 신설) | Backlog #1+#2 영역 |
| W-8 | Stage 4 sub-step 4.4 AR-2 branch protection rule | (branch protection API 호출) | Backlog #3 T3 영역 |
| W-9 | AR-3 자동 revert bot | (CODEOWNERS + bot 설정) | Backlog #3 T3 영역 |
| W-10 | Stage 5 (G3-7 4 항목) 진입 — secret reset rotate / fork PR / pull_request_target / commit signing | (각 영역 별 5 금지 해소) | Stage 4 후속 권고 영역 |

### 4.2 Stage 4 최소 영역 권고 (실 진입 *최소* 작업)

| # | 작업 영역 | 본 brief 권고 |
|---|--------|------------|
| W-1 | 3 MVP-1 workflow 본문 step 추가 / 수정 | ✅ **포함 권고** (R-1 영역 본문 영역) |
| W-2 | integration check tool 본문 step 추가 / 수정 | ✅ **포함 권고** (Stage 4 영역) |
| W-3 | 3 fixture 본문 추가 / 수정 | ✅ **포함 권고** (Stage 4 영역) |
| W-4 | 신규 actual GitHub Actions run trigger | ✅ **포함 권고** (실 진입 = 운영 진입 = actual run 필요) |
| W-5 ~ W-10 | 권한 / branch protection / pre-commit / Backlog 영역 | ❌ **분리 권고** (영역 외 — 별도 합의 / 별도 backlog) |

### 4.3 Stage 4 최대 영역 권고 (실 진입 *최대* 작업)

본 brief = Stage 4 최대 영역 권고 = ❌ **권고 안 함** (영역 경계 불명확 → T-10 + T-13 + T-6 트리거 발화 가능 → 풀 3+1 합의 + 외부 LLM blind 의뢰 필요 → 신중 결정 영역).

### 4.4 본 §4 의 *범위 한계*

본 §4 = **Stage 4 작업 후보 *enumerate 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 권고 = 최소 영역 (W-1 ~ W-4) 한정 — 최대 영역 (W-5 ~ W-10) 분리 권고.

---

## 5. Rollback Trigger 분석 매트릭스

### 5.1 Layer B 18 trigger 답습 매트릭스 (실 진입 시점 발화 예상)

| # | trigger 영역 | R-1 직접 영향 | 본 brief 시점 | 실 진입 후 발화 예상 |
|---|---------|------------|----------|----------------|
| 1 | secret leak observed in production | 영향 0 | 0건 | 0건 (MVP-3 P2 영역) |
| 2 | secret leak observed in PR | 영향 0 | 0건 | 0건 (Stage 4 W-1~W-4 패스 시) |
| 3 | provider key in `~/.config/...` | 영향 0 | 0건 | 0건 |
| 4 | provider key in `~/Library/...` | 영향 0 | 0건 | 0건 |
| 5 | provider key in CI runner env | 영향 0 (F-금지 #1) | 0건 | 0건 (F-금지 #1 영구 답습) |
| 6 | direct provider SDK import detected | 영향 0 (Phase α-2) | 0건 | 0건 |
| 7 | URL endpoint to provider in code | 영향 0 (Phase α-1 R-4) | 0건 | 0건 |
| 8 | Model name pattern match (PASS) | 영향 0 (Phase α-1 R-4) | 0건 | 0건 |
| 9 | Tier-1 catalog under-detection | 영향 0 (R-4.1) | 0건 | 0건 |
| 10 | Tier-2/3 expansion needed | 영향 0 (Backlog #3) | 0건 | 0건 |
| 11 | importlinter forbidden bypass | 영향 0 (Phase α-2 R-5) | 0건 | 0건 |
| 12 | docker secret commit in PR | 영향 0 (Phase α-3 R-7) | 0건 | 0건 |
| 13 | CI step pass with violation present | **R-1 직접 영향** (PC-3 violation) | 0건 | **발화 가능성** (Stage 4 W-1 본문 변경 시) — 신중 |
| 14 | CI step fail without auto-reject | **R-1 직접 영향** (AR-1 violation) | 0건 | **발화 가능성** (Stage 4 W-1 + W-2 본문 변경 시) — 신중 |
| 15 | PR check unstable / flaky | 영향 0 (CI runtime threshold 후보 한정) | 0건 | 0건 |
| 16 | Hermes-originated commit detected | 영향 0 (Group I) | 0건 | 0건 |
| 17 | provider key adapter bypass | 영향 0 (Backlog #4) | 0건 | 0건 |
| 18 | secret handling environment mismatch | 영향 0 (mvp1.md §5.4 IR-3) | 0건 | 0건 |
| **합산** | **18 trigger** | **R-1 직접 영향 2 (#13, #14)** | **0건 영구 답습** | **2 발화 가능성** (W-1 + W-2 본문 변경 시 — 신중) |

### 5.2 TR-1 ~ TR-5 답습 매트릭스 (Group A 2차 합의 답습)

| TR # | 영역 | R-1 영향 | 본 brief 시점 | 실 진입 후 |
|----|----|--------|----------|---------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 필요 | 영향 0 (Phase α-2) | 0건 | 0건 |
| TR-2 | `include_external_packages` flag 변경 | 영향 0 | 0건 | 0건 |
| TR-3 | `root_packages` 영역 변경 | 영향 0 | 0건 | 0건 |
| TR-4 | `ignore_imports` 영역 변경 | 영향 0 | 0건 | 0건 |
| TR-5 | google.generativeai facade 영역 변경 | 영향 0 (Backlog #4) | 0건 | 0건 |
| **합산** | **5 trigger** | **R-1 직접 영향 0** | **0건 영구 답습** | **0건 발화 예상** |

### 5.3 Step Division 신규 후보 5 trigger 매트릭스 (정식 등록 0건 — 후보 한정)

| 후보 trigger | 영역 | 본 brief 시점 | 실 진입 후 발화 예상 |
|----------|----|----------|----------------|
| PC-3 self-check FAIL — local self-check 시 `continue-on-error: true` 발견 | R-1 영역 | 0건 | **발화 가능성** (W-1 본문 변경 시) |
| AR-1 self-check FAIL — local self-check 시 fail-closed 패턴 누락 발견 | R-1 영역 | 0건 | **발화 가능성** (W-1 + W-2 본문 변경 시) |
| integration check tool self-check FAIL | R-1 영역 | 0건 | **발화 가능성** (W-2 본문 변경 시) |
| 4 prerequisite runs JSON conclusion 미답습 발견 | Step 2 영역 | 0건 | 0건 |
| Local Validation Evidence 본문 누락 발견 | Step 3 영역 | 0건 | 0건 |
| **합산** | **5 후보** | **0건 영구 답습** | **3 발화 가능성** (W-1 + W-2 본문 변경 시 — 신중) |

### 5.4 합산 28 trigger × 발화 예상 매트릭스

| 영역 | 합계 | R-1 직접 영향 | 본 brief 시점 발화 | 실 진입 후 발화 예상 |
|------|----|------------|-----------------|----------------|
| Layer B 18 trigger | 18 | 2 (#13, #14) | 0건 | **2 발화 가능성** (W-1 + W-2 시) |
| TR-1 ~ TR-5 | 5 | 0 | 0건 | 0건 |
| Step Division 신규 후보 5 | 5 | 5 | 0건 (후보 한정) | **3 발화 가능성** (W-1 + W-2 시) |
| **합산** | **28** | **7** | **0건 영구 답습** | **5 발화 가능성** (W-1 + W-2 본문 변경 시 — 신중) |

### 5.5 본 §5 의 *범위 한계*

본 §5 = **Rollback Trigger 분석 *권위 권고 한정***. 어느 trigger 도 *발화* 시키지 않으며 (본 brief 시점 0/28), Stage 4 실 진입 시점 발화 가능성 분석 한정 (W-1 + W-2 본문 변경 시 5 trigger 발화 가능성).

---

## 6. 합의 형태 권고 + 풀 3+1 승격 트리거 분석

### 6.1 본 brief 자체 합의 형태 권고

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| **(a) Reviewer-only 단축 합의** | 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ✅ **권고** — 본 brief = DRAFT 한정 + 5 금지 해소 0건 + Stage 4 자동 진입 0건 + 트리거 0/18 발화 예상 |
| (b) 풀 3+1 합의 | 트리거 中 1+ 발화 | 본 brief 시점 미발화 예상 |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | 본 brief 시점 적용 영역 아님 |

### 6.2 풀 3+1 승격 트리거 검토 매트릭스 (본 brief 시점)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 본 brief 가 합산 353 합의 조건 中 1+ *재결정* 권고 | 0건 — 답습 한정 |
| T-2 | 본 brief 가 사용자 명시 5 금지 영역 中 1+ *해소* 권고 | 0건 — 본 brief = DRAFT 영역 한정 (Stage 4 시점 #1 + #3 해소 권고 = 본 brief 의 의도지만 본 brief 자체 = 결정 발효 아님) |
| T-3 | 본 brief 가 Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 |
| T-4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | 0건 |
| T-5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | 0건 |
| T-6 | 본 brief 가 T3 영역 진입 권고 | 0건 — Backlog #3 분리 명시 |
| T-7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | 0건 |
| T-8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 | 0건 |
| T-9 | 본 brief 가 Hermes upstream root of trust 변경 권고 | 0건 |
| T-10 | 본 brief 가 PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0건 — §2.2 + §4.1 분리 명시 |
| T-11 | 본 brief 가 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | 0건 |
| T-12 | 본 brief 가 신규 workflow 신설 / `pull_request_target` 도입 권고 | 0건 |
| T-13 | 본 brief 가 Stage 5 (G3-7) 자동 진입 권고 | 0건 — §4.1 W-10 분리 명시 |
| T-14 | 본 brief 가 Phase α-1 / α-2 / α-3 actual run 재실행 권고 | 0건 |
| T-15 | 본 brief 가 α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE 합의 본문 변경 권고 | 0건 |
| T-16 | 본 brief 가 Stage 4 자동 진입 발효 권고 | 0건 — 본 brief = DRAFT 영역 한정 |
| **합산** | **16** | **✅ 0/16 발화 예상 — Reviewer-only 단축 합의 적격 확정** |

### 6.3 Stage 4 실 진입 *시점* 합의 형태 권고 (본 brief 발효 후 별도 분석)

| Stage 4 영역 | 합의 형태 권고 | 근거 |
|----------|---------|----|
| W-1 ~ W-4 최소 영역 (3 MVP-1 workflow + integration tool + fixture + 신규 actual run) | **풀 3+1 합의 (필수)** | 5 금지 #1 + #3 해소 = T-2 발화 → 풀 3+1 트리거 발화 |
| W-5 ~ W-10 최대 영역 (권한 / branch protection / pre-commit / Backlog 흡수) | **풀 3+1 + 외부 LLM 1+ blind 의뢰 (Group α C-14 + ADR-011 §2.4 + 인간 리뷰 의무)** | T-2 + T-6 + T-10 + T-13 발화 가능성 + Backlog #3 T3 영역 |
| **본 brief 권고 시작점** | W-1 ~ W-4 최소 영역 한정 — **풀 3+1 합의 (외부 LLM 1+ 없이)** | Backlog #3 / Stage 5 분리 + 5 금지 #2 / #4 / #5 영구 보존 |

### 6.4 본 §6 의 *범위 한계*

본 §6 = **합의 형태 권고 한정**. 본 brief 자체 = Reviewer-only 단축 합의 적격 (0/16 트리거 발화 예상). Stage 4 실 진입 시점 = 풀 3+1 합의 (필수) — 외부 LLM blind 의뢰 여부 = W-5 ~ W-10 흡수 영역 결정에 따라 결정.

---

## 7. 사용자 명시 5 금지 영역 × 본 brief 분리 매트릭스

### 7.1 본 brief 영역 5/5 위반 0건 영구 답습 매트릭스

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 명시 결정 영역 - 자동 진입 0건) |
|---|---------|---------------|--------------------------------------|
| #1 | CI workflow 변경 | ✅ 0건 (`secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + integration tool 298 + 3 fixture 89 = 1593줄 답습 보존) | ✅ 0건 (DRAFT 영역) |
| #2 | runtime code 변경 | ✅ 0건 (`src/` + facade.py 41줄 placeholder 답습) | ✅ 0건 |
| #3 | actual run 재실행 | ✅ 0건 (4 prerequisite runs 답습 한정) | ✅ 0건 |
| #4 | Operational Readiness PASS | ✅ 0건 | ✅ 0건 |
| #5 | Hermes PMO 격상 | ✅ 0건 | ✅ 0건 |
| **합산** | **5/5** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** |

### 7.2 추가 분리 영역 위반 0건 영구 답습

본 §0.4 추가 분리 영역 enumerate 답습 — 본 brief 작성 시점 + 본 brief 발효 후 자동 진입 영역 = **분리 명시 + 위반 0건 영구 답습**.

### 7.3 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 5 금지 영역 어느 것도 *해소* 시키지 않으며, 추가 분리 영역 어느 것도 *통합* 시키지 않는다.

---

## 8. 합산 353 합의 조건 답습 매트릭스

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
| Phase α-4 R-1 진입 조건 점검 | `1c365e7` | 33 (C-π-1 ~ C-π-33) | 0건 |
| Phase α-4 R-1 Step Division | `52a05cb` | 38 (C-ρ-1 ~ C-ρ-38) | 0건 |
| **Phase α-4 R-1 LVE** | **`b264580`** | **31 (C-σ-1 ~ C-σ-31)** | **0건** ✅ |
| **합산** | **14 합의** | **353 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| C-σ-29 (Phase α-4 R-1 실 진입 = 사용자 명시 결정 영역) | ✅ 본 brief = Stage 3 실 진입 여부 검토 한정 (실 진입 자동 0건) |
| C-σ-30 (Phase α-4 Stage 4 자동 진입 0건) | ✅ 본 brief 영역 외 |
| C-σ-31 (LVE 권위 = 실 진입 직전 local 검증 완료 권위 권고 한정) | ✅ 답습 한정 |
| C-ρ-37 (Step 분할 / 수정 범위 / 테스트 범위 / Rollback Trigger / Evidence 기준 최종 확정 0건) | ✅ 답습 한정 |
| C-π-x (5 진입 적격성 5/5 충족 + 이중 evidence 충족) | ✅ 답습 한정 |
| C-ε-9 / C-ε-10 (Phase α-4 실 진입 = 사용자 명시 결정 영역 + R-1 영역 7 artifacts × 1593줄 변경 0건) | ✅ 답습 한정 |

### 8.3 본 §8 의 *범위 한계*

본 §8 = **353 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = 본 brief 그대로 승인 합의 보고서 작성 시 도입 가능 (Reviewer-only 단축 합의 적격 후보) — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정.

---

## 9. 본 brief 자체 금지 + brief 발효 후 의무 금지

### 9.1 본 brief 작성 시점 금지 사항

- ❌ **CI workflow 변경** (사용자 명시 5 금지 #1) — 7 artifacts × 1593줄 답습 보존
- ❌ **runtime code 변경** (사용자 명시 5 금지 #2)
- ❌ **actual run 재실행** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ Phase α-4 Stage 4 자동 진입 (본 brief = *실 진입 여부 검토 한정*)
- ❌ Phase α-1 / α-2 / α-3 자동 재진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE 합의 본문 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 trigger 자동 발화
- ❌ 합산 353 합의 조건 자동 변경
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
- ❌ 실 진입 여부 결정 *최종 확정* (사용자 명시 결정 영역)

### 9.2 본 brief 발효 *후* 의무 금지 사항 (사용자 명시 결정 영역)

본 brief 발효 후 *자동 진입 영역* (사용자 명시 결정 *전*):

- ❌ Phase α-4 Stage 4 (실 구현) 자동 진입 0건
- ❌ 합의 보고서 작성 자동 진입 0건 (사용자 명시 합의 형태 결정 후)
- ❌ CI workflow 변경 자동 진입 0건
- ❌ 신규 actual run 자동 trigger 0건
- ❌ branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 자동 진입 0건
- ❌ Backlog #1+#2 / Backlog #3 / Stage 5 자동 진입 0건
- ❌ 합산 353 합의 조건 자동 변경 0건
- ❌ Layer C / D / E / F 재발효 / 재선언 / 발효 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건

---

## 10. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (16/16 풀 3+1 트리거 0건 발화 예상) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-actual-entry-decision.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → **풀 3+1 합의 진입** (Stage 4 시점 풀 3+1 권고 답습) | 풀 3+1 합의 보고서 작성 |
| (E) | 본 brief 승인 → **풀 3+1 + 외부 LLM 1+ 합의** (Group α C-14 답습) | 풀 3+1 + 외부 LLM blind 의뢰 진입 |
| (F) | 본 brief 보류 → Stage 4 실 진입 (W-1 ~ W-4 최소 영역) 직접 진입 brief 작성 | Stage 4 작업 영역 별도 brief |
| (G) | 본 brief 보류 → Backlog #1+#2 / Backlog #3 / Stage 5 우선 진입 | Backlog 中 사용자 결정 영역 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 10.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 R-1 *실 진입 여부 검토 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 R-1 실 진입 여부 (Stage 3, DRAFT, 본 commit)        ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성 (옵션 (A))
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 (실 구현) 진입 brief 작성 (W-1 ~ W-4 최소 영역)           ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 실 구현 — 풀 3+1 합의 (CI workflow 변경 + actual run 재실행)  ← 본 brief 영역 외
```

### 10.2 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. 풀 3+1 합의 진입."
- (E): "옵션 (E) 로 진행해주세요. 풀 3+1 + 외부 LLM 1+ 합의 진입."
- (F): "옵션 (F) 로 진행해주세요. Stage 4 실 진입 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (H): "옵션 (H) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (I): "옵션 (I) 로 진행해주세요. 세션 종료."

### 10.3 본 §10 의 *범위 한계*

본 §10 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 11. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("1 번 작업으로 진행" → "Stage 3 실 진입 여부 brief 작성 (DRAFT — 5 금지 모두 보존)") |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — CI workflow 변경 0건 / runtime code 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| LVE 합의 답습 (`b264580`) | ✅ (31 조건 C-σ-1 ~ C-σ-31 변경 0건) |
| Step Division 합의 답습 (`52a05cb`) | ✅ (38 조건 C-ρ-1 ~ C-ρ-38 변경 0건) |
| α-4 진입 조건 점검 합의 답습 (`1c365e7`) | ✅ (33 조건 C-π-1 ~ C-π-33 변경 0건) |
| 직전 α-4 합의 답습 (`e59a565`) | ✅ (29 조건 C-ε-1 ~ C-ε-29 변경 0건) |
| α-1+2+3 local validation evidence 답습 (`7b3d40a`) | ✅ (486줄 본문 변경 0건 + 12/12 PASS 답습) |
| LVE 본문 답습 (`4ce5a0b`) | ✅ (583줄 본문 변경 0건 + 51/51 PASS 답습) |
| 합산 353 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31) |
| Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 / α-4 진입 조건 점검 / Step Division / LVE 본문 변경 | ✅ 0건 |
| §5.5 9 sub-수단 본문 채택 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| Layer B 18 Rollback Trigger + TR-1 ~ TR-5 + Step Division 신규 후보 5 trigger 발화 | ✅ 0/28 발화 (본 brief 시점) |
| 풀 3+1 트리거 발화 | ✅ 0/16 발화 예상 |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| Stage 4 자동 진입 | ✅ 0건 (본 brief 영역 외) |
| 실 진입 여부 *최종 확정 0건* | ✅ (사용자 명시 결정 영역) |
| Stage 3 framing 명시 (Step Division §1.3 답습) | ✅ §1.3 답습 |

---

## 12. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-4 R-1 Local Validation Evidence 합의 (`b264580` 후속 25 APPROVE — Reviewer-only 단축, 31 조건 C-σ-1 ~ C-σ-31) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *실 진입 (Stage 4) *여부* 검토* 한정 brief 준비안 (DRAFT)** = **Phase α-4 자체의 Stage 3 framing** (Step Division §1.3 답습 명시) — "*Should* we enter Phase α-4 R-1 actual implementation (Stage 4) now?". **사용자 명시 5 금지** (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **R-1 영역 = 현재 상태 매트릭스 채택** (R-1 7 artifacts × 1593줄 본문 = 이미 구현 완료 + 4 prerequisite runs 4/4 SUCCESS + local 51/51 PASS + α-1+2+3 evidence 12/12 PASS — *technical pre-conditions 모두 충족*). **"실 진입 (Stage 4)" 정의 매트릭스** (Stage 4 작업 후보 W-1 ~ W-10 enumerate — 최소 영역 W-1~W-4 (CI workflow 변경 + integration tool + fixture + 신규 actual run = 5 금지 #1 + #3 해소) / 최대 영역 W-5~W-10 (권한 / branch protection / pre-commit / Backlog 흡수 = Backlog #1+#2 / Backlog #3 / Stage 5 분리). **5 금지 해소 매트릭스 (실 진입 시점 권고 한정)** — 실 진입 시점 5 금지 #1 + #3 해소 (필수) + #2 + #4 + #5 영구 보존 — 본 brief 시점 0/5 해소 영구 답습. **실 진입 Pro / Con 매트릭스** — Pro 9 (technical readiness P-1~P-9: R-1 본문 + α-1+2+3 evidence + Stage 4 합의 + ADR-011 + 5 진입 적격성 + Step Division + 353 합의 조건 + 5 영구 핵심 제약 + Provider Liquidity) / Con 9 (5 금지 해소 risk C-1+C-2 + governance risk C-3~C-8 + human review risk C-9). **Stage 4 작업 enumerate** — W-1~W-4 최소 영역 권고 + W-5~W-10 최대 영역 *비*권고 (영역 경계 불명확 → T-10/T-13/T-6 트리거 발화 → 풀 3+1 + 외부 LLM 1+ 필요). **Rollback Trigger 분석 매트릭스** — Layer B 18 + TR-1~TR-5 + Step Division 신규 후보 5 = **합산 28 trigger × 본 brief 시점 0/28 발화 영구 답습** + 실 진입 후 W-1+W-2 본문 변경 시 5 trigger 발화 가능성 (Layer B #13/#14 + Step Division 신규 후보 3 = 신중 영역). **합의 형태 권고**: 본 brief 자체 = (a) Reviewer-only 단축 합의 (16/16 풀 3+1 트리거 0건 발화 예상) — Stage 4 실 진입 시점 = (b) 풀 3+1 합의 (필수, W-1~W-4 최소 영역) / (c) 풀 3+1 + 외부 LLM 1+ (W-5~W-10 최대 영역 흡수 시). **사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 영구 답습 (작성 시점 + 발효 후 자동 진입 영역 모두 0건)**. **합산 353 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31). **본 brief 자체 금지 ≥ 40 + 본 brief 발효 후 의무 금지 ≥ 10** enumerate. **본 brief 는 Phase α-4 Stage 4 어느 작업 도 *발효* 시키지 않으며, R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며, R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며, `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며, 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 353 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / 실 진입 여부 결정 어느 것도 *최종 확정* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §10 답습) — (A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점) / (B) brief 수정 / (C) 부분 채택 / (D) 풀 3+1 / (E) 풀 3+1 + 외부 LLM / (F) Stage 4 실 진입 brief 작성 / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.

---

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §10 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **CI workflow 변경 0건** (7 artifacts × 1593줄 답습 보존)
- ❌ **runtime code 변경 0건** (`src/` + facade.py 41줄 placeholder 답습 보존)
- ❌ **actual run 재실행 0건** (4 prerequisite runs PASS 답습 한정)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ Phase α-4 Stage 4 (실 구현) 자동 진입 0건 (본 brief = 실 진입 여부 검토 한정)
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 353 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence (`7b3d40a`) 본문 변경 0건
- ❌ α-4 진입 조건 점검 (`1c365e7`) + Step Division (`52a05cb`) + LVE (`4ce5a0b` + `b264580`) 본문 변경 0건
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
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 5 trigger 자동 발화 0건 (28/28)
- ❌ 풀 3+1 트리거 자동 발화 0건 (0/16 예상)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ 실 진입 여부 *최종 확정 0건* (사용자 명시 결정 영역)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ git commit / push 0건 (사용자 명시 결정 후 진입)
