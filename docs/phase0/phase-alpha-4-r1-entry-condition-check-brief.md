# Phase α-4 R-1 CI workflow 통합 진입 조건 점검 Brief (DRAFT)

> **본 문서는 Phase α-1 + α-2 + α-3 local validation evidence (`68d010a` HEAD, 2026-05-16 후속 22, 12/12 PASS) 발효 후속, Phase α-4 (R-1 CI workflow 통합 — PC-3 + AR-1) *진입 조건 점검* 한정 의 brief 준비안.**
>
> **본 brief 의 framing**: 직전 Phase α-4 진입 brief (`f91ef4b`, 751줄) + α-4 진입 합의 (`e59a565`, 29 조건 C-ε-1 ~ C-ε-29) 발효 후속, **새로 발효된 Phase α-1+2+3 local validation evidence (1192줄 = 13 file = 12/12 local PASS + 본문 변경 0건)** 이 α-4 진입 조건에 미치는 영향을 *재검토 한정* — 5 금지 (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습.
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Phase α-4 실 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) 합산 222 합의 조건 (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25) + 직전 α-4 합의 29 조건 (C-ε-1 ~ C-ε-29) + Phase α-1+2+3 local validation evidence 의 어느 줄도 *해소* 시키지 않는다.

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/phase0/phase-alpha-123-local-validation-evidence.md` (commit `68d010a`, 486줄, Phase α-1+2+3 12/12 local PASS evidence — **본 brief 의 발효 trigger**)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-123-parallel-actual-entry.md` (commit `7917e4a` APPROVE — 25 조건 C-ξ-1 ~ C-ξ-25)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (commit `e59a565` APPROVE AS BRIEF — 29 조건 C-ε-1 ~ C-ε-29, 직전 α-4 brief 합의)
- `docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (commit `f91ef4b`, 751줄 직전 α-4 brief)
- `docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md` (Layer C 발효, commit `eb01bc4` — 30 조건 C-ι-1 ~ C-ι-30)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (Stage 4 PC-3 + AR-1 통합 구현 진입 합의 APPROVE)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.4 + §5.5.1
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-4 진입 조건 점검 brief를 작성해주세요. 범위는 R-1 CI workflow 통합, 즉 PC-3 + AR-1을 기존 Phase α-1~α-3 local validation evidence 이후 어떻게 연결할 수 있는지 검토하는 것입니다. 아직 CI workflow 변경, runtime code 변경, actual run 재실행, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습

1. ❌ **CI workflow 변경 금지** — `.github/workflows/*.yml` 본문 변경 모두 0건 (3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 답습 보존)
2. ❌ **runtime code 변경 금지** — `src/` 본문 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존
3. ❌ **actual run 재실행 금지** — 4 prerequisite run (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 답습 한정 — 신규 trigger 0건
4. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리 답습
5. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C 12 조건 미진입 영구 답습

### 0.3 본 brief 가 *하는* 것

1. Phase α-1+2+3 local validation evidence (12/12 PASS, HEAD `68d010a`) 답습 — α-4 진입 조건에 미치는 *영향 한정* 검토 (§1)
2. **R-1 영역 (CI workflow 통합 = PC-3 + AR-1) ↔ Phase α-1+2+3 local validation evidence 연결 매트릭스** — 1192줄 본문 답습 ↔ 1593줄 R-1 본문 답습 일관성 검증 (§2)
3. **직전 α-4 합의 29 조건 (C-ε-1 ~ C-ε-29) 답습 매트릭스** — Phase α-1+2+3 local validation evidence 발효 후 변경 없음 확인 (§3)
4. **5 진입 적격성 조건 (C-α4-1 ~ C-α4-5) 재검토** — Phase α-1+2+3 local validation evidence 가 의존성 조건 (C-α4-3) 에 *추가 확정* 영향만 미침 (§4)
5. **사용자 명시 5 금지 영역 × R-1 본문 분리 매트릭스** — 5/5 답습 분리 명시 (§5)
6. **합산 합의 조건 답습 매트릭스** — 222 prior + 직전 α-4 29 = 251 조건 + 본 brief 발효 후 변경 0건 검증 (§6)
7. **다음 단계 결정 옵션** (사용자 결정 영역, §7)
8. **본 brief 메타 검증** (§8)
9. **본 brief 요약** (§9)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 5 금지 답습 + 사후 추가 분리 영역)

**사용자 명시 5 금지 영역 답습**:

- ❌ **CI workflow 변경 0건** — `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) / `provider-adapter-enforcement.yml` (186줄) / `provider-url-scanner.yml` (326줄) / `tools/mvp1_pc3_ar1_integration_check.py` (298줄) / `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/` (89줄) 본문 변경 모두 0건 — 합산 7 artifacts × 1593줄 PoC 답습 변경 0건
- ❌ **runtime code 변경 0건** — `src/` 본문 + `src/adapters/llm/facade.py` 41줄 placeholder 본문 변경 0건 (Backlog #4 P1 v2 facade MVP 영역 분리 답습)
- ❌ **actual run 재실행 0건** — Phase α-1 / α-2 / α-3 4 prerequisite runs (`25728590939` SUCCESS + `25728590916` SUCCESS + `25728590977` SUCCESS + `25731846625` SUCCESS) 답습 한정 — 신규 GitHub Actions actual run trigger 0건
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** — MVP-6 영역 분리 (commit signing / Vault HSM / hosting provider alternative 모두 영역 외)
- ❌ **Hermes PMO 격상 (Layer F) 0건** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미충족 영구 답습

**추가 금지 영역 (직전 α-4 brief 답습 + Phase α-1+2+3 evidence 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 0건** — `secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/` 본문 변경 모두 0건
- ❌ **R-4 / R-5 / R-7 본문 변경 0건** — Phase α-1+2+3 evidence §5.1 답습 (13 file × 1192줄)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 0건** — Phase α-1+2+3 evidence §5.3 답습
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 0건** — Phase α-1+2+3 evidence §5.3 답습 (TR-1 ~ TR-5 미발화)
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 0건** — Phase α-1+2+3 evidence §5.3 답습
- ❌ **PC-4 / AR-2 / AR-3 진입 0건** — Backlog #1+#2 / Backlog #3 / Stage 5 분리 답습
- ❌ **ST-1 / ST-2 / ST-4 / ST-5 진입 0건** — Backlog 분리
- ❌ **S-2 gitleaks 도입 0건** — Backlog #1 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 0건** — Stage 4 후속 권고 답습
- ❌ **branch protection 변경 0건** — AR-2 영역 = Backlog #3 T3 영역 별도 풀 3+1 분리
- ❌ **dev 환경 강제 0건** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 0건 (R-10 영역 분리)
- ❌ **`pre-commit install` 의무화 도입 0건** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 모두 0건 (PC-4 sub-step 4.3 = Backlog #1+#2 분리)
- ❌ **신규 workflow 신설 0건 + `pull_request_target` 도입 0건** — T2/T3 별도 합의 영역
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 0건** — `boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml` 모두 분리
- ❌ **GitHub Actions secrets 사용 도입 0건** — F-금지 #1 영구 답습 (G3-7 (i))
- ❌ **Hermes upstream Dockerfile 변경 0건** — ADR-008 차단조건 #6 + 부록 B 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 0건** — PoC 격리 디렉토리 한정 답습 (`docker/gp3-st3-poc/` 한정)
- ❌ **실 secret material commit 0건** — FAKE_TEST_SECRET marker 답습
- ❌ **Layer A / Layer B / Layer C (`eb01bc4`) / Layer D (`951a5b1`) / Group α (`4880e88`) / Backlog #6 (`c7ddfdd`) / Phase α-1 ~ α-3 본문 변경 0건** — 모든 상위 합의 답습 보존
- ❌ **§5.5 9 sub-수단 본문 채택 변경 0건** — Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 0건**
- ❌ **Phase α-1 / α-2 / α-3 자동 재진입 0건** — Phase α-1+2+3 evidence §5.2 + §8 답습 (자동 진입 0건)
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 0건**
- ❌ **합의 보고서 작성 0건** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건** — 별도 commit 분리 (사용자 명시 결정 후 진입)
- ❌ **git commit / push 0건** — 사용자 명시 결정 후 진입
- ❌ **외부 LLM 자동 호출 0건** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**
- ❌ **인간 리뷰 의무 자동 발화 0건**
- ❌ **token rotation 정책 / GitHub plan 가용성 자동 결정 0건** — Group α C-3 + C-4 답습
- ❌ **threshold *고정* 0건** — CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지
- ❌ **event enum 정식 등록 0건** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리
- ❌ **MVP-1 PASS (Layer D) 재선언 0건** — `951a5b1` Layer D 재진입 평가 답습 한정
- ❌ **Layer C (Implementation Evidence PASS) 재발효 0건** — `eb01bc4` 답습 한정
- ❌ **Phase β / γ 자동 진입 0건** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 0건**
- ❌ **MVP-2 ~ MVP-6 본문 deepening 0건**
- ❌ **17 항목 우선순위 자동 *재고정* 0건**
- ❌ **Phase α-1+2+3 local validation evidence 본문 변경 0건** — `68d010a` 답습 한정
- ❌ **신규 actual run 자동 trigger 0건** — local 검증 답습 + 4 prerequisite run 답습 한정

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-4 실 진입을 *시작* 시키지 않으며,
- (ii) 합산 222 합의 조건 + 직전 α-4 29 조건 = **251 합의 조건** 어느 것도 *해소* 시키지 않으며,
- (iii) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (iv) Layer A ~ Stage 3 / Layer C / Layer D / Phase α-1+2+3 local validation evidence / 직전 α-4 brief / 직전 α-4 합의 / Stage 4 합의 본문 어느 줄도 *변경* 하지 않으며,
- (v) R-1 영역 본문 (`.github/workflows/*.yml` + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`) 어느 줄도 *변경* 하지 않으며 (현 7 artifacts × 1593줄 답습),
- (vi) R-4 / R-5 / R-7 본문 어느 줄도 *변경* 하지 않으며 (13 file × 1192줄 답습),
- (vii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (viii) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (ix) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (x) 합의 보고서 / 새 합의 / 새 ADR / 새 P / 새 GP 어느 것도 *발행* 시키지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 CI workflow 통합 영역의 *진입 조건 점검* — Phase α-1+2+3 local validation evidence 발효 후속 PC-3 + AR-1 연결 매트릭스 + 직전 α-4 합의 29 조건 답습 + 진입 적격성 5 조건 재검토 + 5 금지 분리 매트릭스 + 다음 단계 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (Phase α-1+2+3 evidence 발효 시점)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `e59a565` (2026-05-14) | Phase α-4 R-1 brief 합의 APPROVE AS BRIEF — 29 조건 C-ε-1 ~ C-ε-29 | ✅ 답습 한정 (29 조건 변경 0건) |
| `f91ef4b` (2026-05-14) | Phase α-4 R-1 진입 brief DRAFT (751줄) | ✅ 답습 한정 (본문 변경 0건) |
| `eb01bc4` (2026-05-16) | Layer C 발효 — Implementation Evidence PASS + GP-3 / GP-5 PASS 발효 (30 조건 C-ι-1 ~ C-ι-30) | ✅ 답습 한정 |
| `951a5b1` (2026-05-16) | Layer D 재진입 평가 — MVP-1 PASS *유지* + 추가 조건 (25 조건 C-λ-1 ~ C-λ-25) | ✅ 답습 한정 |
| `542e77e` (2026-05-16) | Stage 1 — Phase α 통합 계획 합의 (25 조건 C-μ-1 ~ C-μ-25) | ✅ 답습 한정 |
| `88ccf79` (2026-05-16) | Stage 2 — Phase α-1+2+3 1순위 계획 합의 (25 조건 C-ν-1 ~ C-ν-25) | ✅ 답습 한정 |
| `7917e4a` (2026-05-16) | Stage 3 — Phase α-1+2+3 parallel actual entry 합의 APPROVE (25 조건 C-ξ-1 ~ C-ξ-25) | ✅ 답습 한정 |
| `faae826` (2026-05-16) | Phase α-1+2+3 parallel actual entry brief (920줄) | ✅ 답습 한정 |
| `7b3d40a` (2026-05-16) | **Phase α-1+2+3 Local Validation Evidence 신설 (486줄, 12/12 PASS)** | ✅ **본 brief 의 발효 trigger** |
| `2aa13ef` (2026-05-16) | CONTEXT 후속 21 entry | ✅ 답습 한정 |
| `68d010a` (HEAD, 2026-05-16 후속 22) | CONTEXT — Phase α-1+2+3 local validation evidence 기록 entry | ✅ 답습 한정 |

### 1.2 Phase α-1+2+3 local validation evidence 의 핵심 발견 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| evidence 작성 시점 | 2026-05-16 후속 22 (직전 합의 `7917e4a` 발효 후속) |
| 검증 결과 | **12/12 PASS** ✅ (Phase α-1 R-4 8/8 + Phase α-2 R-5 INI 구조 8 항목 통합 + Phase α-3 R-7 3/3) |
| 본문 line count | **1192줄** (13 file: R-4 829 + R-5 35 + R-7 328) |
| brief 명세 일치 | **100%** ✅ (829 + 35 + 328 = 1192) |
| 본문 변경 | **0건** ✅ (`git status` clean) |
| 새 도구 / fixture / docker block 추가 | **0건** ✅ |
| CI workflow 변경 | **0건** ✅ (3 MVP-1 + 8 G2/G3/G4 PoC 답습) |
| runtime code 변경 | **0건** ✅ (`src/` 본문 + facade.py 41줄 placeholder 답습) |
| Operational Readiness PASS / Hermes PMO 격상 | **0건** ✅ |
| 합산 222 합의 조건 변경 | **0건** ✅ |
| 5 영구 핵심 제약 보존 | **5/5 100%** ✅ |
| Provider Liquidity 5-way 보존 | **5/5 100%** ✅ |
| F-금지 #1 영구 답습 | **0건** ✅ |
| evidence 권위 | "**실 진입 완료 evidence**" — 합의 보고서 권위 아님, MVP-1 PASS 재선언 아님, Layer C 재발효 아님 |

**본 brief 의 trigger 의미**: Phase α-1+2+3 local validation evidence (`68d010a`) 의 발효는 **R-4 / R-5 / R-7 본문이 이미 구현되어 있고 + local 12/12 PASS 검증되어 있음** 을 evidence 권위로 고정. 본 발견은 **직전 α-4 합의 (`e59a565`, C-ε-3 ~ C-ε-5 = α-1/α-2/α-3 합의 변경 0건 + C-ε-16 = R-4/R-5/R-7 본문 변경 0건 + C-ε-20 = α-1/α-2/α-3 actual run 자동 재실행 0건) 의 조건 매트릭스를 *위반 0건* 으로 답습 — 본 brief = **직전 α-4 합의 29 조건 영구 보존** + α-1+2+3 evidence 추가 확정 영향 *enumerate 한정*.

### 1.3 6-Layer + Phase α 분리 매트릭스 (2026-05-17 후속 23 시점 답습)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, **사용자 명시 5 금지 #4**) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (**사용자 명시 5 금지 #5**) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ **local validation 12/12 PASS evidence 답습** (`68d010a`) |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ **local validation PASS evidence 답습** (`68d010a`) |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ **local validation 3/3 PASS evidence 답습** (`68d010a`) |
| **Phase α-4 (R-1)** | **2순위 의존 — CI workflow 통합 (PC-3 + AR-1)** | ⏳ **본 brief 영역 — 진입 조건 점검 한정** |

### 1.4 본 brief 의 진입점 (단계 cycle)

```
Layer A APPROVE (df20b15) ──────────────────────────────────────────────────┐
Layer B APPROVE (f40423f) + §5.5 9 sub-수단 (55c5b4b)                       │
Group α APPROVE (4880e88) — AR-3 + PC-4 T3 sub (4.3/4.4 분리)               │
Stage 4 합의 (Reviewer-only APPROVE) — sub-step 4.1 + 4.2 발효              │
Backlog #6 우선 진입 합의 APPROVE AS BRIEF (c7ddfdd)                        │
Phase α-1 R-4 brief 합의 APPROVE AS BRIEF (1b3090b)                         │
Phase α-2 R-5 brief 합의 APPROVE AS BRIEF (6a79247)                         │
Phase α-3 R-7 brief 합의 APPROVE AS BRIEF (3f6306d)                         │
■ Phase α-4 R-1 brief 합의 APPROVE AS BRIEF (e59a565, 29 조건 C-ε-1~29)      │
   (직전 α-4 brief = `f91ef4b` 751줄)                                       │
Layer C 발효 합의 APPROVE (eb01bc4, 30 조건 C-ι-1~30)                       │
Layer D 재진입 평가 (951a5b1, 25 조건 C-λ-1~25)                             │
Stage 1 Phase α 통합 계획 (542e77e, 25 조건 C-μ-1~25)                       │
Stage 2 Phase α-1+2+3 1순위 계획 (88ccf79, 25 조건 C-ν-1~25)                │
Stage 3 Phase α-1+2+3 parallel actual entry (7917e4a, 25 조건 C-ξ-1~25)     │
Phase α-1+2+3 parallel actual entry brief (faae826, 920줄)                  │
Phase α-1+2+3 Local Validation Evidence (7b3d40a, 486줄, 12/12 PASS)        │
CONTEXT 후속 21 + 후속 22 (2aa13ef + 68d010a HEAD)                          │
   │
   ▼
■ 본 brief = Phase α-4 R-1 진입 *조건 점검* (DRAFT) — α-1+2+3 evidence 후속  ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 실 진입 (R-1 CI workflow 통합 sub-step 4.1 + 4.2)                ← 본 brief 영역 외
   │
   ▼ (Phase α-4 완료 + R-1 actual run SUCCESS + 추가 evidence 후)
Layer C 재발효 / MVP-2 영역 진입 결정                                       ← 본 brief 영역 외
```

---

## 2. R-1 영역 (PC-3 + AR-1) ↔ Phase α-1+2+3 local validation evidence 연결 매트릭스

### 2.1 R-1 본문 (1593줄, 7 artifacts) ↔ R-4/R-5/R-7 본문 (1192줄, 13 file) 의존성 매트릭스

본 §은 **R-1 CI workflow 통합 = PC-3 + AR-1 영역이 Phase α-1+2+3 local validation evidence 후속 어떻게 연결되는가** 의 검증 — 본문 변경 0건 + enumerate 한정.

| R-1 본문 | R-1 영역 | 연결 R-4/R-5/R-7 본문 | Phase α-1+2+3 local PASS 답습 | 연결 검증 |
|---------|---------|------------------|------------------------|----------|
| `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) | Stage 1 R-4 secret_scanner step + Stage 2 R-7 docker check step + Stage 4 integration step | R-4 `tools/secret_scanner.py` (368줄, R-4.1 Tier-1 45 patterns) + R-7 `docker/gp3-st3-poc/` 4 file (92줄) + R-7 `tools/docker_secret_image_layer_check.sh` (99줄) + R-7 `tools/docker_secret_restart_recovery.sh` (118줄) + R-7 `tests/fixtures/gp3_st3/` 3 file (18줄) | α-1 R-4 8/8 PASS (3.1.1~3.1.2) + α-3 R-7 3/3 PASS (3.3.1~3.3.3) — **합산 11/11 PASS** ✅ | **연결 충족** — workflow 가 호출하는 도구 / fixture / docker block 모두 local 12/12 PASS evidence 답습 |
| `.github/workflows/provider-adapter-enforcement.yml` (186줄) | Stage 3 T-2 import-linter step + T-5 AST scanner step | R-5 `.importlinter` (35줄, forbidden 4 모듈) + R-4 `tools/provider_import_scanner.py` (178줄, 5 pattern direct/from/dynamic-importlib/__import__/model-name) | α-2 R-5 INI 구조 8/8 PASS + α-1 R-4 2.1+2.2 PASS — **합산 10/10 PASS** ✅ | **연결 충족** — workflow 가 호출하는 `.importlinter` + `provider_import_scanner.py` 모두 local PASS evidence 답습 |
| `.github/workflows/provider-url-scanner.yml` (326줄) | Stage 3 T-5 URL endpoint scanner step + Model name scanner step | R-4 `tools/provider_url_scanner.py` (283줄, URL Tier-1 10 + Model Tier-1 19 catalog) | α-1 R-4 3.1+3.2+3.3+3.4 PASS — **합산 4/4 PASS** ✅ | **연결 충족** — workflow 가 호출하는 `provider_url_scanner.py` (URL endpoint + model-name mode) local PASS evidence 답습 |
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) | Stage 4 cross-workflow 검증 (PC-3 + AR-1 통합 정합성 검증) | 3 MVP-1 workflow 의 step 패턴 (PC-3 = `continue-on-error: false` + non-zero exit propagation / AR-1 = `exit 1` propagation + `${{ failure() }}` 패턴) 검증 | **간접 영향**: workflow 본문이 호출하는 도구 / fixture 의 PASS evidence 답습 (12/12 PASS) → workflow 자체의 PASS 패턴 보존 가능성 강화 | **간접 연결** — local 12/12 PASS = 도구 본문 정합성 + fixture 정합성 100% 보존 → integration check 의 PASS 패턴도 보존 가능성 강화 (단, 본 brief = 실 actual run 재실행 0건 답습) |
| `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` (30줄) | PC-3 + AR-1 정합 entry step 검증 fixture | 3 MVP-1 workflow PC-3 + AR-1 패턴 답습 | 간접 영향 | 답습 한정 — local 12/12 PASS 결과 = fixture 정합성 보존 강화 |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` (31줄) | PC-3 위반 (continue-on-error) 검증 fixture | 3 MVP-1 workflow 위반 패턴 검증 | 간접 영향 | 답습 한정 |
| `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` (28줄) | AR-1 위반 (no fail-closed) 검증 fixture | 3 MVP-1 workflow 위반 패턴 검증 | 간접 영향 | 답습 한정 |
| **합산** | **7 artifacts × 1593줄** | **13 file × 1192줄** | **12/12 local PASS evidence 답습** | **연결 매트릭스 충족 (직접 + 간접)** |

### 2.2 PC-3 + AR-1 양 GP 공유 답습 ↔ α-1+2+3 evidence 의미적 연결

| 영역 | Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 본문 채택 답습 | α-1+2+3 evidence 후속 의미 |
|------|--------------------------------------|-------------------------|
| **PC-3 (CI-only enforcement)** | T2 영역 (CI step Entry) + 양 GP 공유 채택 — `continue-on-error: false` + non-zero exit propagation | R-4 / R-5 / R-7 도구 본문이 local 12/12 PASS 답습 = **CI step 안에서 호출 시 exit 0 / exit 1 정합성 보존** → PC-3 enforcement 정합성 강화 |
| **AR-1 (CI step fail-closed = PR auto-reject)** | T2 영역 + 양 GP 공유 채택 — `exit 1` propagation + `${{ failure() }}` 패턴 | R-4 / R-5 / R-7 도구 본문이 local FAIL fixture 5/5 검출 (R-4.1.2 secret_scanner FAIL + 2.2 provider_import_scanner FAIL + 3.2 provider_url_scanner url FAIL + 3.4 model-name FAIL + R-7 4.2 docker layer leak FAIL) = **CI step 의 fail-closed 정합성 = local evidence 답습** → AR-1 정합성 강화 |
| 양 GP 공유 채택 단독 답습 | PC-3 + AR-1 단독 답습 (PC-4 / AR-2 / AR-3 분리) | α-1+2+3 evidence §0.4 답습 — PC-3 / AR-1 / PC-4 / AR-2 / AR-3 분리 영역 명시 그대로 보존 |

### 2.3 의존성 충족 매트릭스 (Stage 4 합의 §1.2 답습 + Phase α-1+2+3 evidence 추가 확정)

| Phase | R-1 의존 영역 | 직전 α-4 합의 의존성 충족 (`e59a565` 시점) | 본 brief 시점 의존성 충족 (`68d010a` 시점) |
|------|---------|-------------------------------|------------------------------|
| Phase α-1 R-4 | 도구 본문 (`secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) | actual run PASS 선행 evidence (`25728590939` + `25728590916` + `25728590977`) 답습 | **+ local 8/8 PASS evidence 답습 추가 확정** (α-1+2+3 evidence §3.1) |
| Phase α-2 R-5 | `.importlinter` config | actual run PASS 선행 evidence (`25728590916` 內 import-linter step) 답습 | **+ INI 구조 8/8 PASS evidence 답습 추가 확정** (α-1+2+3 evidence §3.2) |
| Phase α-3 R-7 | docker secret block (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh`) | actual run PASS 선행 evidence (`25731846625`) 답습 | **+ local 3/3 PASS evidence 답습 추가 확정** (α-1+2+3 evidence §3.3) |

**의존성 충족 강화**: 직전 α-4 합의 시점에 이미 **4 prerequisite runs PASS 답습 (actual run evidence)** 으로 의존성 충족 완료 (`e59a565` C-α4-3 답습). 본 brief 시점에 **추가로 local 12/12 PASS evidence (`68d010a`)** 답습 — **의존성 충족 영역에 *추가 evidence* 확정 영향만 미치고, 의존성 *변경* 0건**.

### 2.4 본 §2 의 *범위 한계*

본 §2 = **R-1 ↔ α-1+2+3 evidence *연결 매트릭스 정리 한정***. 실 R-1 본문 변경 / 실 CI workflow 변경 / 실 actual run 재실행 / 실 sub-step 결정 = 사용자 명시 결정 영역 + Phase α-4 실 진입 시점 (Backlog #6 + 사용자 명시 결정 영역 — 본 brief 영역 외).

---

## 3. 직전 α-4 합의 29 조건 (C-ε-1 ~ C-ε-29) 답습 매트릭스

### 3.1 29 조건 본 brief 시점 답습 검증

| 조건 # | 조건 영역 | 본 brief 시점 답습 | α-1+2+3 evidence 영향 |
|------|---------|----------------|-------------------|
| C-ε-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-2 | Backlog #6 우선 진입 합의 11 조건 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-3 | Phase α-1 합의 15 조건 *변경 0건* | ✅ 변경 0건 | **추가 확정** (local 8/8 PASS evidence) |
| C-ε-4 | Phase α-2 합의 26 조건 *변경 0건* | ✅ 변경 0건 | **추가 확정** (INI 구조 8/8 PASS evidence) |
| C-ε-5 | Phase α-3 합의 28 조건 *변경 0건* | ✅ 변경 0건 | **추가 확정** (local 3/3 PASS evidence) |
| C-ε-6 | Stage 4 합의 본문 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-7 | 5 Stage 분할안 합의 본문 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-8 | 사용자 명시 7 금지 영역 *해소 0건* | ✅ 해소 0건 (본 brief 사용자 명시 5 금지 #1~#5 답습) | 영향 0 |
| C-ε-9 | Phase α-4 실 진입 = 사용자 명시 결정 영역 | ✅ 본 brief = 진입 조건 *점검 한정* | 영향 0 |
| C-ε-10 | R-1 영역 7 artifacts × 1593줄 본문 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-11 | PC-3 + AR-1 양 GP 공유 단독 답습 *변경 0건* — PC-4 / AR-2 / AR-3 / Stage 5 흡수 0건 | ✅ 답습 한정 | 영향 0 |
| C-ε-12 | 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC 8 workflow 흡수 0건) | ✅ 답습 한정 | 영향 0 |
| C-ε-13 | 신규 workflow 신설 0건 + `pull_request_target` 도입 0건 | ✅ 0건 | 영향 0 |
| C-ε-14 | GitHub Actions secrets 사용 도입 *0건* (F-금지 #1 영구 답습) | ✅ 영구 답습 | 영향 0 |
| C-ε-15 | Hermes upstream Dockerfile 변경 *0건* | ✅ 영구 답습 | 영향 0 |
| C-ε-16 | R-4 도구 본문 / R-5 `.importlinter` 본문 / R-7 docker secret block 어느 영역도 *변경 0건* | ✅ 변경 0건 (1192줄 답습 보존) | **답습 강화** (α-1+2+3 evidence §5.1 git status clean 답습) |
| C-ε-17 | Layer A / Layer B / §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 *변경 0건* | ✅ 변경 0건 | 영향 0 |
| C-ε-18 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | ✅ Layer C `eb01bc4` 발효 답습 한정 (재발효 0건) | **답습 강화** |
| C-ε-19 | Phase α-1 / α-2 / α-3 *자동 재진입 0건* | ✅ 자동 재진입 0건 (α-1+2+3 evidence §0.4 답습) | 영향 0 |
| C-ε-20 | Phase α-1 / α-2 / α-3 actual run *자동 재실행 0건* | ✅ 자동 재실행 0건 (본 brief 사용자 명시 5 금지 #3 답습) | **답습 강화** (4 prerequisite runs PASS 답습) |
| C-ε-21 | Phase β / γ *자동 진입 0건* | ✅ 0건 | 영향 0 |
| C-ε-22 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | ✅ 0건 | 영향 0 |
| C-ε-23 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* | ✅ 0건 | 영향 0 |
| C-ε-24 | Stage 5 (G3-7 4 항목) *자동 진입 0건* | ✅ 0건 | 영향 0 |
| C-ε-25 | R-MVP1-G3-4 / G3-5 / G5-5 / G5-6 (R-1 직접 영향 4 trigger) *자동 발화 0건* | ✅ 0/4 발화 | 영향 0 |
| C-ε-26 | 외부 LLM *응답 결론 강제 채택 0건* | ✅ 0건 | 영향 0 |
| C-ε-27 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | ✅ 5/5 보존 (α-1+2+3 evidence §6.1 답습) | **답습 강화** |
| C-ε-28 | Provider Liquidity 5-way **100% 보존** (R-1 = CI integration Layer = catalog / provider 영역과 직교) | ✅ 5/5 100% 보존 (α-1+2+3 evidence §6.2 답습) | **답습 강화** |
| C-ε-29 | 본 합의 = **수단 결정 적격성 권위 권고 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | ✅ 답습 한정 | 영향 0 |
| **합산** | **29 조건** | **29/29 답습 충족** | **변경 0건 + 일부 답습 강화 (C-ε-3/4/5/16/18/20/27/28)** |

### 3.2 본 §3 의 *범위 한계*

본 §3 = **29 조건 답습 매트릭스 *enumerate 한정***. 직전 α-4 합의 29 조건 *변경 0건* + α-1+2+3 evidence 가 발생시키는 영향 = *일부 조건의 답습 강화* (추가 evidence 확정) 한정 — *조건 자체의 변경 / 해소 / 추가 0건*. 새 조건 발효 0건.

---

## 4. 5 진입 적격성 조건 (C-α4-1 ~ C-α4-5) 재검토

### 4.1 적격성 재검토 매트릭스

| 조건 # | 조건 | 직전 α-4 brief 검토 결과 (`e59a565` 시점) | 본 brief 시점 재검토 결과 (`68d010a` 시점) | 판정 |
|------|------|----------------------------|------------------------------|----|
| **C-α4-1** | **사용자 명시 금지 영역 충돌 0** | 직전 7 금지 0/7 충돌 답습 | **본 brief 사용자 명시 5 금지 0/5 충돌** — CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상 모두 R-1 영역과 분리 명시 | ✅ **0/5 충돌** |
| **C-α4-2** | **PoC 답습 변경 0** | R-1 7 artifacts × 1593줄 답습 + Stage 4 합의 §1.3 답습 + Layer B §5.5.1 + §5.5.2 답습 모두 변경 0건 | **답습 강화** — α-1+2+3 evidence §5.1 git status clean + §5.2 8 금지 답습 위반 0/8 + §5.3 추가 영역 변경 0건 매트릭스 답습 | ✅ **답습 100% 보존 (추가 evidence 확정)** |
| **C-α4-3** | **의존성 충족 (Phase α-1 / α-2 / α-3 *완료 후* 의존)** | 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) PASS 답습 — 의존성 충족 완료 | **+ local 12/12 PASS evidence 추가 확정** (α-1+2+3 evidence `7b3d40a` 발효) — **이중 evidence 답습** (actual run + local validation) | ✅ **의존성 *이중 evidence 충족*** |
| **C-α4-4** | **Provider Liquidity 5-way 100% 보존** | R-1 = CI integration Layer (catalog / provider 영역과 직교) + CI workflow = vendor-agnostic 표준 + provider key 사용 0건 (F-금지 #1 영구 답습) | **답습 강화** — α-1+2+3 evidence §6.2 답습 (5/5 100% 보존 evidence 추가) | ✅ **5/5 100% 보존 (답습 강화)** |
| **C-α4-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존 | **답습 강화** — α-1+2+3 evidence §6.1 답습 (5/5 100% HIGH 보존 evidence 추가) | ✅ **5/5 보존 (답습 강화)** |

### 4.2 풀 3+1 승격 트리거 재검토 (직전 α-4 합의 14 트리거 답습 + α-1+2+3 evidence 후속)

| # | 트리거 | 직전 α-4 brief 발화 | 본 brief 시점 재발화 검토 | 발화 |
|---|----|---------------|--------------------|----|
| 1 | 본 brief 가 Group α / Backlog #6 / Phase α-1/α-2/α-3 / Stage 4 / α-1+2+3 evidence 어느 것의 *재결정* 권고 | 0건 | 0건 — 본 brief = 답습 한정 + 추가 evidence enumerate 한정 | ❌ 0건 |
| 2 | 본 brief 가 사용자 명시 5 금지 영역 中 1+ *해소* 권고 | 0건 (당시 7 금지 답습) | 0건 — 본 brief 사용자 명시 5 금지 5/5 답습 | ❌ 0건 |
| 3 | 본 brief 가 Layer B §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 | 0건 — 본 brief = 답습 한정 | ❌ 0건 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | 0건 | 0건 — 5/5 보존 답습 강화 (α-1+2+3 evidence §6.2 답습) | ❌ 0건 |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | 0건 | 0건 — 5/5 보존 답습 강화 (α-1+2+3 evidence §6.1 답습) | ❌ 0건 |
| 6 | 본 brief 가 T3 영역 진입 권고 | 0건 | 0건 — T3 분리 명시 한정 (AR-2 branch protection / AR-3 / Vault HSM 모두 영역 외) | ❌ 0건 |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | 0건 | 0건 — Hermes PMO 격상 분리 명시 한정 (사용자 명시 5 금지 #5 답습) | ❌ 0건 |
| 8 | 본 brief 가 secret handling 방식이 기존 정책 변경 권고 | 0건 | 0건 — F-금지 #1 영구 답습 + GitHub Actions secrets 사용 도입 0건 | ❌ 0건 |
| 9 | 본 brief 가 Hermes upstream root of trust 변경 권고 | 0건 | 0건 — CI workflow = upstream 분리 영역 (ADR-011 §2.1 (b) 수단/목적 분리 답습) | ❌ 0건 |
| 10 | 본 brief 가 PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0건 | 0건 — 경계 명확 답습 (PC-3 + AR-1 = T2 본 영역 / PC-4 = Backlog #1+#2 / AR-2 = Backlog #3 / AR-3 = Backlog #3) | ❌ 0건 |
| 11 | 본 brief 가 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | 0건 | 0건 — 3 MVP-1 workflow 한정 답습 (G2/G3/G4 PoC 8 workflow 분리 명시) | ❌ 0건 |
| 12 | 본 brief 가 신규 workflow 신설 / `pull_request_target` 도입 권고 | 0건 | 0건 — 신설 / `pull_request_target` 도입 0건 답습 | ❌ 0건 |
| 13 | 본 brief 가 Stage 5 (G3-7 4 항목) 자동 진입 권고 | 0건 | 0건 — Stage 4 후속 권고 답습 (Stage 5 별도 합의 분리) | ❌ 0건 |
| 14 | 본 brief 가 Phase α-1 / α-2 / α-3 actual run 재실행 권고 | 0건 | 0건 — 4 prerequisite runs PASS 선행 evidence 답습 한정 + α-1+2+3 evidence local 12/12 PASS 답습 강화 (재실행 0건, 사용자 명시 5 금지 #3 답습) | ❌ 0건 |
| **+ 1 (본 brief 신규)** | **본 brief 가 α-1+2+3 evidence 본문 변경 / 재작성 / 해소 권고** | — (직전 α-4 brief 시점에 evidence 미발효) | 0건 — α-1+2+3 evidence `7b3d40a` 답습 한정 (본문 변경 0건) | ❌ 0건 |

**검토 결과**: **15/15 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 유지 확정** (사용자 명시 결정 시).

### 4.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 직전 α-4 brief 시점 판정 | 본 brief 시점 재판정 |
|------|--------------------|-----------------|
| 5 조건 (C-α4-1 ~ C-α4-5) | 5/5 충족 | **5/5 충족 (3 조건 답습 강화: C-α4-2/4/5)** |
| 풀 3+1 트리거 | 14/14 0건 발화 | **15/15 0건 발화 (신규 #15 미발화 추가)** |
| 의존성 (Phase α-1 / α-2 / α-3 *완료 후*) | 4 prerequisite runs PASS — 충족 완료 | **이중 evidence 충족 (actual run + local 12/12 PASS)** |
| **Phase α-4 진입 적격성** | 적격 | **적격 (이중 evidence 강화) — 사용자 명시 결정 영역 (자동 진입 0건)** |

### 4.4 본 §4 의 *범위 한계*

본 §4 = **진입 적격성 *재검토 한정***. 실 Phase α-4 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 *적격 재판정* = 적격성 권위 권고 한정 — 실 진입 발효 권위 0건. **직전 α-4 합의 (`e59a565`) APPROVE AS BRIEF 권위는 그대로 유지** + α-1+2+3 evidence 발효는 *추가 강화* 영향만 (해소 / 변경 / 추가 조건 0건).

---

## 5. 사용자 명시 5 금지 영역 × R-1 본문 분리 매트릭스

### 5.1 금지 #1 — CI workflow 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `secret-hygiene-egress-redaction.yml` (694줄) 본문 변경 | ❌ (영역 외) | Phase α-4 실 진입 후 영역 |
| `provider-adapter-enforcement.yml` (186줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `provider-url-scanner.yml` (326줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) 본문 변경 | ❌ (영역 외) | 동상 |
| `tests/fixtures/mvp1_pc3_ar1_integration/` (89줄, 3 파일) 변경 | ❌ (영역 외) | 동상 |
| G2/G3/G4 PoC 8 workflow 변경 | ❌ (영역 외) | 별도 영역 |
| 신규 workflow 신설 | ❌ (영역 외) | 별도 합의 영역 |
| `pull_request_target` workflow 도입 | ❌ (영역 외) | T2/T3 별도 합의 영역 |
| **본 brief 영역 *내* 적격 작업** | **R-1 영역 *답습 출처 + 7 artifacts × 1593줄 enumerate + α-1+2+3 evidence 연결 매트릭스 enumerate* 한정** | — |

### 5.2 금지 #2 — runtime code 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `src/` 본문 변경 | ❌ (영역 외) | Backlog #4 P1 v2 facade MVP 영역 |
| `src/adapters/llm/facade.py` 41줄 placeholder 변경 | ❌ (영역 외) | 동상 |
| `src/adapters/llm/facade.py` real 본문 작성 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = CI workflow integration 영역, runtime code = facade MVP 영역 분리)** | — |

### 5.3 금지 #3 — actual run 재실행 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| 신규 GitHub Actions actual run trigger | ❌ (영역 외) | Phase α-4 실 진입 시 사용자 명시 결정 영역 |
| Phase α-1 / α-2 / α-3 actual run 재실행 | ❌ (영역 외) | 4 prerequisite runs PASS 답습 한정 |
| Stage 4 integration check actual run | ❌ (영역 외) | Phase α-4 실 진입 시 영역 |
| **본 brief 영역 *내* 적격 작업** | **4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) *enumerate 답습 한정* + α-1+2+3 evidence local 12/12 PASS *enumerate 답습 한정*** | — |

### 5.4 금지 #4 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| Operational parity check | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = 구현 영역, Layer E = 운영 영역 — 분리)** | — |

### 5.5 금지 #5 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| `pmo_promoted` flag 변경 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-1 = CI workflow 영역, Layer F = governance 영역 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 5.6 본 §5 의 *범위 한계*

본 §5 = **5 금지 영역 *분리 매트릭스 한정***. 5 금지 영역 어느 것도 *해소* 0건 + Phase α-4 실 진입 자동 진입 0건.

---

## 6. 합산 합의 조건 답습 매트릭스 (251 조건)

### 6.1 합산 합의 조건 매트릭스

| 합의 | commit | 조건 수 | 본 brief 변경 |
|------|-------|------|-----------|
| Group α (Backlog #3) | `4880e88` | 12 (C-1 ~ C-12) | 0건 |
| Backlog #6 우선 진입 | `c7ddfdd` | 11 (C-α-1 ~ C-α-11) | 0건 |
| Phase α-1 (R-4) | `1b3090b` | 15 (C-β-1 ~ C-β-15) | 0건 |
| Phase α-2 (R-5) | `6a79247` | 26 (C-γ-1 ~ C-γ-26) | 0건 |
| Phase α-3 (R-7) | `3f6306d` | 28 (C-δ-1 ~ C-δ-28) | 0건 |
| **Phase α-4 (R-1) — 직전** | **`e59a565`** | **29 (C-ε-1 ~ C-ε-29)** | **0건** ✅ |
| Layer C 발효 | `eb01bc4` | 30 (C-ι-1 ~ C-ι-30) | 0건 |
| Layer D 재진입 평가 | `951a5b1` | 25 (C-λ-1 ~ C-λ-25) | 0건 |
| Stage 1 — Phase α 통합 계획 | `542e77e` | 25 (C-μ-1 ~ C-μ-25) | 0건 |
| Stage 2 — Phase α-1+2+3 1순위 계획 | `88ccf79` | 25 (C-ν-1 ~ C-ν-25) | 0건 |
| Stage 3 — α-1+2+3 parallel actual entry | `7917e4a` | 25 (C-ξ-1 ~ C-ξ-25) | 0건 |
| **합산** | **11 합의** | **251 조건** | **0건 영구 답습** ✅ |

### 6.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 | 영역 | 본 brief 답습 |
|----|-----|----------|
| C-ε-3 ~ C-ε-5 | Phase α-1 / α-2 / α-3 합의 *변경 0건* | ✅ 변경 0건 + **α-1+2+3 evidence 답습 강화** |
| C-ε-9 | Phase α-4 실 진입 = 사용자 명시 결정 영역 | ✅ 본 brief = 진입 조건 *점검 한정* |
| C-ε-10 | R-1 영역 7 artifacts × 1593줄 본문 *변경 0건* | ✅ 변경 0건 |
| C-ε-16 | R-4 / R-5 / R-7 본문 *변경 0건* | ✅ 변경 0건 (α-1+2+3 evidence §5.1 답습) |
| C-ε-19 ~ C-ε-20 | Phase α-1 / α-2 / α-3 자동 재진입 / 재실행 0건 | ✅ 0/0 (본 brief 사용자 명시 5 금지 #3 답습) |
| C-ε-27 ~ C-ε-28 | 5 영구 핵심 제약 + Provider Liquidity 5-way 보존 | ✅ 5/5 + 5/5 (α-1+2+3 evidence §6 답습 강화) |
| C-ι-x (Layer C 30 조건) | Implementation Evidence PASS 발효 답습 | ✅ 답습 한정 (재발효 0건) |
| C-λ-x (Layer D 25 조건) | MVP-1 PASS *유지* 답습 | ✅ 답습 한정 (재선언 0건) |
| C-ξ-11 ~ C-ξ-22 (Stage 3) | α-1+2+3 evidence 직접 답습 매트릭스 | ✅ 답습 한정 (변경 0건) |

### 6.3 본 §6 의 *범위 한계*

본 §6 = **251 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = 본 brief 그대로 승인 합의 보고서 작성 시 도입 가능 (Reviewer-only 단축 합의 적격 후보) — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정.

---

## 7. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

본 brief 발효 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| (A) | 본 brief 그대로 승인 → 합의 보고서 작성 (Reviewer-only 단축 합의 적격 후보) | 본 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF + 새 합의 조건 도입 (C-π-1 ~ C-π-x) |
| (B) | 본 brief 수정 요청 | 사용자 명시 prohibition 추가 / 분리 영역 변경 / 표현 변경 영역 |
| (C) | Phase α-4 실 진입 step 분할 brief 작성 (sub-step 4.1 + 4.2 분할안) | 본 brief 합의 후 별도 brief (Stage 2 / Stage 3 framing 답습) |
| (D) | Phase α-4 실 진입 (R-1 CI workflow 통합 — sub-step 4.1 + 4.2 실 진입) | step 분할 brief 합의 후 사용자 명시 진입 명령 영역 (CI workflow 변경 = 사용자 명시 5 금지 #1 *해소* 영역) |
| (E) | Phase α-1+2+3 evidence 추가 보강 brief (필요 시) | α-1+2+3 evidence §8 옵션 답습 |
| (F) | Backlog #1 (PC-4 / pre-commit + S-2 gitleaks + ST-1 entrypoint stat) 1.5차 보강 brief | Backlog #1 별도 합의 |
| (G) | Backlog #3 (T3 영역 — AR-2 branch protection + AR-3 CODEOWNERS + Tier-2/3 확장) | T3 영역 별도 합의 + 외부 LLM 1+ + 인간 리뷰 의무 |
| (H) | Backlog #4 (P1 v2 facade MVP — `src/adapters/llm/facade.py` real 본문) | P1 v2 facade MVP 별도 합의 |
| (I) | Backlog #5 (event enum 정식 등록 7 후보) | ADR-012 evidence enum 별도 합의 |
| (J) | Backlog #7 (ST-2 inotify sidecar + ST-4 Vault HSM + ST-5 Defense in depth) | MVP-2 영역 별도 합의 |
| (K) | MVP-2 ~ MVP-6 deepening brief | 별도 MVP deepening 영역 |
| (L) | Group I (Hermes-originated commit auto-reject) 진입 brief | Group I 별도 합의 |
| (M) | token rotation 정책 별도 합의 | token rotation 영역 |
| (N) | GitHub plan / ruleset 가용성 확인 | GitHub plan 확인 영역 |
| (O) | 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 7.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 진입 *조건 점검 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 R-1 진입 *조건 점검* (DRAFT, 본 commit)               ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → Reviewer-only 단축 합의 보고서 작성 (옵션 (A))
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 실 진입 step 분할 brief 작성 (옵션 (C))                          ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 실 진입 (sub-step 4.1 + 4.2 실 본문 작성)                        ← 본 brief 영역 외
```

### 7.2 본 §7 의 *범위 한계*

본 §7 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 8. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("Phase α-4 진입 조건 점검 brief를 작성해주세요" + 5 금지 명시) |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — CI workflow 변경 0건 / runtime code 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| 직전 α-4 합의 답습 (`e59a565`) | ✅ (29 조건 C-ε-1 ~ C-ε-29 변경 0건) |
| α-1+2+3 local validation evidence 답습 (`68d010a`) | ✅ (486줄 본문 변경 0건, 12/12 PASS 결과 enumerate 한정) |
| 합산 251 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25) |
| Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 본문 변경 | ✅ 0건 |
| §5.5 9 sub-수단 본문 채택 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 (PoC 답습) |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 (α-1+2+3 evidence 답습) |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| α-1+2+3 evidence 본문 변경 | ✅ 0건 (`7b3d40a` 답습) |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 (α-1+2+3 evidence §6.1 답습 강화) |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 (α-1+2+3 evidence §6.2 답습 강화) |
| F-금지 #1 영구 답습 | ✅ 영구 답습 (α-1+2+3 evidence §6.3 답습) |
| Layer B 18 Rollback Trigger + TR-1 ~ TR-5 발화 | ✅ 0/23 발화 |
| 풀 3+1 트리거 발화 | ✅ 0/15 발화 (직전 14 + 본 brief 신규 1) |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 (사용자 명시 5 금지 #3 답습) |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 9. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-1 + α-2 + α-3 Local Validation Evidence (`68d010a` HEAD, 2026-05-16 후속 22, 486줄, 12/12 PASS — Phase α-1 R-4 8/8 + Phase α-2 R-5 INI 구조 8 항목 + Phase α-3 R-7 3/3, 13 file × 1192줄 본문 변경 0건) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) *진입 조건 점검 한정* 의 brief 준비안 (DRAFT)**. **사용자 명시 5 금지** (CI workflow 변경 / runtime code 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습. **직전 Phase α-4 R-1 진입 brief (`f91ef4b`, 751줄) + 직전 α-4 합의 (`e59a565` APPROVE AS BRIEF, 29 조건 C-ε-1 ~ C-ε-29) 변경 0건 + α-1+2+3 evidence 발효 영향 *enumerate 한정***. **R-1 영역 = 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 = 1206줄) + integration tool (`tools/mvp1_pc3_ar1_integration_check.py` 298줄) + integration fixture (`tests/fixtures/mvp1_pc3_ar1_integration/` 3 파일 89줄) = **7 artifacts × 1593줄 본문 답습 변경 0건**. **PC-3 + AR-1 양 GP 공유 답습 채택** (Layer B §5.5.1 + §5.5.2 sub-step 4.1 + 4.2 한정) + **PC-4 / AR-2 / AR-3 / Stage 5 분리** (sub-step 4.3 / 4.4 / Backlog #3 / Stage 4 후속 권고 분리 명시) + **3 MVP-1 workflow 한정 답습** (G2/G3/G4 PoC 8 workflow 분리). **R-1 ↔ α-1+2+3 evidence 연결 매트릭스** (§2): workflow 가 호출하는 도구 (`secret_scanner.py` 368 + `provider_import_scanner.py` 178 + `provider_url_scanner.py` 283 + `.importlinter` 35 + docker block 4 file 92 + `docker_secret_image_layer_check.sh` 99 + `docker_secret_restart_recovery.sh` 118 + `tests/fixtures/gp3_st3/` 18) = R-4/R-5/R-7 합산 **1192줄 + local 12/12 PASS evidence 답습** → PC-3 (exit 0/1 정합성) + AR-1 (fail-closed 정합성) 의미적 강화 (단, 실 actual run 재실행 0건). **5 진입 적격성 조건 (C-α4-1 ~ C-α4-5) 재검토 5/5 충족** — 특히 **C-α4-3 = 의존성 *이중 evidence 충족*** (직전 시점 4 prerequisite runs PASS actual run evidence + 본 brief 시점 추가 local 12/12 PASS evidence 답습) + **C-α4-2/4/5 = 답습 강화 (α-1+2+3 evidence §5/§6 답습)**. **15/15 풀 3+1 승격 트리거 0건 발화** (직전 14 + 본 brief 신규 #15 미발화) → **Reviewer-only 단축 합의 적격 후보 확정**. **5 영구 핵심 제약 5/5 보존** (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) + **Provider Liquidity 5-way 100% 보존** (R-1 = CI integration Layer = catalog / provider 영역과 직교, CI workflow = vendor-agnostic 표준 GitHub Actions) + **F-금지 #1 영구 답습** (GitHub Actions secrets 사용 도입 0건). **합산 251 합의 조건 변경 0건** (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + **Phase α-4 29** + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 25). **본 brief 는 Phase α-4 실 진입을 *시작* 시키지 않으며, 합산 251 합의 조건 어느 것도 *해소* 시키지 않으며, 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며, R-1 영역 본문 (1593줄, 7 artifacts) 어느 줄도 *변경* 하지 않으며, R-4 / R-5 / R-7 본문 (1192줄, 13 file) 어느 줄도 *변경* 하지 않으며, `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며, PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며, Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며, 합의 보고서 / 새 합의 / 새 ADR / 새 P / 새 GP 어느 것도 *발행* 시키지 않는다**. 본 brief 가 발생시키는 *유일한* 효과는 **Phase α-4 R-1 CI workflow 통합 영역의 *진입 조건 점검 권위 권고 한정* — α-1+2+3 evidence 발효 후속 PC-3 + AR-1 연결 매트릭스 + 직전 α-4 합의 29 조건 답습 + 진입 적격성 5 조건 재검토 + 5 금지 분리 매트릭스 + 다음 단계 권고**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건) — (A) 본 brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점) / (B) brief 수정 요청 / (C) Phase α-4 실 진입 step 분할 brief / (D) Phase α-4 실 진입 / (E)~(N) 별도 backlog/MVP 영역 / (O) 세션 종료.

---

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ O, §7 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **CI workflow 변경 0건** (3 MVP-1 workflow 1206줄 + integration tool 298줄 + integration fixture 89줄 답습 보존)
- ❌ **runtime code 변경 0건** (`src/` + facade.py 41줄 placeholder 답습 보존)
- ❌ **actual run 재실행 0건** (4 prerequisite runs PASS 답습 한정)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 251 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence 본문 변경 0건 (`7b3d40a` 답습)
- ❌ Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 3 본문 변경 0건
- ❌ §5.5 9 sub-수단 본문 채택 변경 0건
- ❌ Phase α-1 / α-2 / α-3 자동 재진입 0건
- ❌ Phase α-4 실 진입 자동 진입 0건
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
- ❌ threshold *고정* 0건 (후보 한정)
- ❌ event enum 정식 등록 0건 (Backlog #5 분리)
- ❌ Rollback Trigger / TR-1 ~ TR-5 자동 발화 0건
- ❌ 풀 3+1 트리거 자동 발화 0건 (0/15)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ git commit / push 0건 (사용자 명시 결정 후 진입)
