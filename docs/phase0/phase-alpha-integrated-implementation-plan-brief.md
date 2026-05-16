# Phase α-1 ~ α-4 통합 실제 구현 계획 Brief (준비안 — DRAFT)

> **본 문서는 Phase α 4 단계 (α-1 R-4 도구 본문 / α-2 R-5 `.importlinter` / α-3 R-7 docker secret block / α-4 R-1 CI workflow 통합) 의 *실제 구현 단계 분할 정리* 한정 brief 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / Phase α-3 합의 28 조건 C-δ-1 ~ C-δ-28 / Phase α-4 합의 29 조건 C-ε-1 ~ C-ε-29 / Layer C 발효 합의 30 조건 C-ι-1 ~ C-ι-30 / Layer D 재진입 가능성 합의 25 조건 C-λ-1 ~ C-λ-25 / 사용자 명시 5 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-16
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md` (Layer C 발효, commit `eb01bc4` APPROVE — MVP-1 Implementation Evidence PASS + GP-3 + GP-5 PASS 실 발효, 30 조건 C-ι-1 ~ C-ι-30)
- `docs/review/3plus1-consensus-2026-05-16-layer-d-reentry-assessment.md` (Layer D 재진입 가능성 검토, APPROVE AS BRIEF — 기존 `210c98f` Layer D 권위 답습 유지, 25 조건 C-λ-1 ~ C-λ-25)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF, 15 조건 C-β-1 ~ C-β-15)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF, 26 조건 C-γ-1 ~ C-γ-26)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3 R-7 합의, commit `3f6306d` APPROVE AS BRIEF, 28 조건 C-δ-1 ~ C-δ-28)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (Phase α-4 R-1 합의, commit `e59a565` APPROVE AS BRIEF, 29 조건 C-ε-1 ~ C-ε-29)
- `docs/phase0/phase-alpha-1-r4-tools-body-entry-brief.md` (`e7cdb21`)
- `docs/phase0/phase-alpha-2-r5-importlinter-body-entry-brief.md` (`608a046`)
- `docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md` (`8da3273`)
- `docs/phase0/phase-alpha-4-r1-ci-workflow-integration-entry-brief.md` (`38eb013`)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치, C-1 ~ C-12)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-1 ~ α-4 통합 실제 구현 계획 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter, R-7 docker secret block, R-1 CI workflow 통합을 실제 구현하기 전 단계 분할로 정리하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습

본 brief 진입 명령 시 사용자가 명시한 5 금지 (이전 Phase α-1 ~ α-4 entry brief 의 7 금지 패턴과 *축소 framing* — 사용자 명시 결정):

1. ❌ **실제 파일 수정 금지** — R-4 (829줄) + R-5 (35줄) + R-7 (328줄) + R-1 (1593줄) 합산 **2785줄 답습 보존** + 변경 / 추가 / 삭제 0건
2. ❌ **CI workflow 변경 금지** — 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` 694줄 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄) + 8 G2/G3/G4 PoC workflow 본문 변경 / 신설 / 삭제 0건
3. ❌ **runtime code 변경 금지** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 (Backlog #4 P1 v2 facade MVP 합의 영역 분리)
4. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리 답습
5. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

본 5 금지 답습 = 사용자 명시 패턴 보존 — 사용자가 본 brief 검토 시 prohibition 추가/축소 권위 영역 (옵션 (B) 수정 요청 답습).

**Phase α-N (N=1,2,3,4) entry brief 의 7 금지 패턴과의 차이**: 이전 entry brief = "사용자 명시 7 금지" (branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 추가) 답습. 본 brief = 5 금지 framing (사용자 명시 강조 영역 한정) — 단, branch protection / dev 환경 / `pre-commit install` 의무화 = **여전히 본 brief 영역 외** (Backlog #1 + #2 + #3 + Group α 합의 별도 영역 분리 — 답습 명시 한정, §4.6 + §4.7 답습).

### 0.3 본 brief 가 *하는* 것

1. Layer C 발효 (`eb01bc4` 2026-05-16) + Layer D 권위 (`210c98f` 2026-05-13 + 후속 18 재진입 검토) 답습 後 — Phase α-1 ~ α-4 *통합 실제 구현 단계 분할 정리 한정* (§1)
2. **Phase α 4 단계 영역 합산 정의** — 4 영역 본문 합산 매트릭스 (2785줄) + 의존성 토폴로지 (1순위 병렬 α-1+α-2+α-3, 2순위 의존 α-4) + Layer B §5.5 9 sub-수단 답습 매트릭스 (§2)
3. **통합 실제 구현 단계 분할 매트릭스** — Phase α-1 11 sub-step + Phase α-2 6 항목 + Phase α-3 4 sub-step + Phase α-4 4 sub-step + 통합 cycle 패턴 + actual run 답습 매트릭스 (§3)
4. **사용자 명시 5 금지 영역 × 4 Phase 분리 매트릭스** (§4)
5. **통합 실제 구현 진입 적격성 검토** — Layer C 발효 후속 적격성 5 조건 + 의존성 의무 검토 + 풀 3+1 승격 트리거 검토 + 합산 적격성 판정 (§5)
6. **Rollback Trigger 의존성 답습 (통합)** — 4 Phase 영역 영향 받는 trigger enumerate + 발화 0건 + threshold 후보 한정 (§6)
7. 본 brief + 본 brief 발효 후 통합 실 진입 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **실제 파일 수정 (0건)** — 합산 2785줄 답습 보존 + Phase α-1 ~ α-4 어느 본문도 변경 0건:
  - R-4: `tools/secret_scanner.py` (368) + `tools/provider_import_scanner.py` (178) + `tools/provider_url_scanner.py` (283) = 829줄 답습
  - R-5: `/.importlinter` (35) = 35줄 답습
  - R-7: `docker/gp3-st3-poc/{docker-compose.gp3-st3.yml,Dockerfile,app.py,secrets/api_key.placeholder}` (34+12+46+1) + `tools/docker_secret_image_layer_check.sh` (99) + `tools/docker_secret_restart_recovery.sh` (118) + `tests/fixtures/gp3_st3/{pass,fail}/` (18) = 328줄 답습
  - R-1: `.github/workflows/{secret-hygiene-egress-redaction.yml,provider-adapter-enforcement.yml,provider-url-scanner.yml}` (694+186+326) + `tools/mvp1_pc3_ar1_integration_check.py` (298) + `tests/fixtures/mvp1_pc3_ar1_integration/` (89) = 1593줄 답습
- ❌ **CI workflow 변경 (0건)** — 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경 / 신설 / 삭제 0건
- ❌ **runtime code 변경 (0건)** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 (Backlog #4 분리)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **branch protection 변경 (0건)** — AR-2 (CODEOWNERS + required status check) / direct push 차단 / force push 차단 / admin bypass OFF / required PR review count / linear history / deployments 모두 변경 0건 (Group α 합의 5.1 #6 답습 + Backlog #3 T3 영역 분리)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 0건 (Backlog #2 영역)
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 / `default_install_hook_types` 본문 결정 모두 0건 (Group α 합의 5.2 #9 답습 + Backlog #1 + #2 분리)
- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 / `.pre-commit-config.yaml` 본문 변경 0건
- ❌ **실 git commit / push 자동 진입 (0건)** — 본 brief = 준비안 한정 (commit / push 모두 사용자 명시 결정 영역)
- ❌ **Phase α-1 / α-2 / α-3 / α-4 자동 실 진입 (0건)** — 본 brief = 통합 실제 구현 *단계 분할 정리 한정* (실 진입 결정 = 사용자 명시 결정 영역)
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / commit signing / Vault HSM / Layer E / Layer F 모두 영역 외
- ❌ **MVP-1 PASS (Layer D) 재선언 (0건)** — Layer D 권위 = `210c98f` 답습 유지 (후속 18 합의 답습)
- ❌ **Layer C 재발효 (0건)** — Layer C 발효 = `eb01bc4` 답습 유지
- ❌ **9 evidence 파일 재생성 (0건)** — evidence 답습 보존 (Layer C 발효 시점 evidence 답습 유지)
- ❌ **4 prerequisite actual run 자동 재실행 (0건)** — run_id `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정
- ❌ **신규 actual run 자동 trigger (0건)**
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)** — Group α 합의 5.1 #8 + Backlog #3 별도 합의 영역
- ❌ **`.importlinter` forbidden 4 모듈 변경 / `include_external_packages` 변경 / `root_packages` 변경 / `ignore_imports` 변경 (0건)** — Group A 2차 합의 답습 + TR-1 ~ TR-5 재합의 trigger 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)** — GP-3 Stage 2 합의 답습
- ❌ **PC-4 local pre-commit framework 진입 (0건)** — sub-step 4.3 = Backlog #1 + #2 1.5차 보강 분리 (dev 환경 영향 정책 영역 = T3)
- ❌ **AR-2 branch protection rule 진입 (0건)** — sub-step 4.4 = Backlog #3 T3 영역 별도 풀 3+1 분리
- ❌ **AR-3 자동 revert bot 도입 (0건)** — Backlog #3 T3 영역 분리
- ❌ **ST-1 entrypoint stat / ST-2 inotify sidecar 진입 (0건)** — Backlog #1 1.5차 보강 영역 분리
- ❌ **ST-4 Vault HSM 진입 (0건)** — Backlog #7 영역 분리
- ❌ **ST-5 Defense in depth 진입 (0건)** — MVP-2 이후 영역 분리
- ❌ **S-2 gitleaks 도입 (0건)** — Backlog #1 1.5차 보강 영역 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 답습 한정
- ❌ **`pull_request_target` workflow 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **commit signing 도입 (0건)** — MVP-6 영역 답습
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습 (G3-7 (i))
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 답습 = upstream 변경 회피 영구 보존
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 (`docker/gp3-st3-poc/`) 한정
- ❌ **실 secret material commit (0건)** — `secrets/api_key.placeholder` = FAKE_TEST_SECRET marker 답습 (Group D F-금지 #1 marker 정책 답습)
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 (0건)**
- ❌ **threshold *고정* (0건)** — FP / FN / latency / CI runtime / image layer leak count / restart recovery rate / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지
- ❌ **Group α 14 결정 영역 *재결정* (0건)**
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 ~ α-4 합의 / Stage 2 합의 / Stage 4 합의 / Group A 1차/2차/3차 합의 / Group D 합의 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)**
- ❌ **R-MVP1-G3-1 ~ G3-8 / G5-1 ~ G5-10 / AR-3 STAGE / PC-4 STAGE Rollback Trigger 어느 것도 *발화* 0건**
- ❌ **TR-1 ~ TR-5 (Group A 2차) 자동 발화 (0건)**
- ❌ **C-1 ~ C-12 (Group α) / C-α-1 ~ C-α-11 (Backlog #6) / C-β-1 ~ C-β-15 (Phase α-1) / C-γ-1 ~ C-γ-26 (Phase α-2) / C-δ-1 ~ C-δ-28 (Phase α-3) / C-ε-1 ~ C-ε-29 (Phase α-4) / C-ι-1 ~ C-ι-30 (Layer C) / C-λ-1 ~ C-λ-25 (Layer D 재진입) 자동 변경 (0건)**
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)**
- ❌ **event enum 정식 등록 (0건)** — Backlog #5 ADR-012 §2.2 분리 (Layer D C-2 = ✅ Satisfied 답습 한정 — 본 brief 영역 외)
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 (0건)** — Backlog #4 분리 (Layer D C-8 = ⏳ Deferred 답습)
- ❌ **Layer 2 runtime block (G5-5) 진입 (0건)** — MVP-3/4 영역 분리
- ❌ **의미적 lock-in 검사 (G4 §4.6 라운드트립 검증) 진입 (0건)** — MVP-3 영역 분리
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-1 / α-2 / α-3 / α-4 *실 진입* 어느 것도 *시작* 시키지 않으며,
- (ii) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 C-α-1 ~ C-α-11 / Phase α-1 합의 C-β-1 ~ C-β-15 / Phase α-2 합의 C-γ-1 ~ C-γ-26 / Phase α-3 합의 C-δ-1 ~ C-δ-28 / Phase α-4 합의 C-ε-1 ~ C-ε-29 / Layer C 발효 합의 C-ι-1 ~ C-ι-30 / Layer D 재진입 합의 C-λ-1 ~ C-λ-25 의 어느 조건도 *해소* 시키지 않으며,
- (iii) 사용자 명시 5 금지 영역 어느 것도 진입시키지 않으며,
- (iv) Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 ~ α-4 합의 / Stage 2 합의 / Stage 4 합의 / Group A 1차/2차/3차 합의 / Group D 합의 / §5.5 9 sub-수단 본문 채택 어느 줄도 *변경* 하지 않으며,
- (v) 합산 2785줄 (R-4 829 + R-5 35 + R-7 328 + R-1 1593) 어느 줄도 *변경* 하지 않으며,
- (vi) `src/` 본문 어느 줄도 *변경* 하지 않으며,
- (vii) Layer C 발효 (`eb01bc4`) / Layer D 권위 (`210c98f`) 어느 것도 *재발효* / *재선언* / *재진입* 하지 않으며,
- (viii) Rollback Trigger / TR-1 ~ TR-5 어느 것도 *발화* 시키지 않으며,
- (ix) MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않으며*,
- (x) Phase α-1 ~ α-4 합의 본문 / 합의 형태 / 합의 조건 어느 것도 *변경* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-1 ~ α-4 통합 실제 구현의 *단계 분할 정리* — 4 영역 합산 정의 + 의존성 토폴로지 + 통합 단계 분할 매트릭스 + 5 금지 분리 매트릭스 + 적격성 검토 + Rollback Trigger 의존성 + 금지 영역 enumeration + 합의 형태 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Layer C 발효 답습 (`eb01bc4` — 2026-05-16)

| 영역 | 답습 |
|------|----|
| 합의 판정 | **APPROVE — MVP-1 Implementation Evidence PASS (Layer C) + GP-3 PASS + GP-5 PASS 실 발효** |
| 합의 형태 | Reviewer-only 단축 합의 (옵션 A) |
| 합의 조건 | 30 조건 (C-ι-1 ~ C-ι-30) |
| 풀 3+1 트리거 발화 | 0/33 |
| 발효 시점 | 2026-05-16 |
| 보고서 라인 수 | 610줄, 12 섹션 |
| evidence 적격성 | 양 GP × 5 조건 (a)~(e) = **10/10 PASS** (ADR-011 §2.1 (a)~(e) 5조건 패턴 답습) |
| evidence file count | 8/8 정확 일치 + 9/9 재생성 0건 |
| 4 prerequisite actual run | `25728590939` (GP-3 secret-hygiene PASS) + `25728590916` (GP-5 provider-adapter PASS) + `25728590977` (GP-5 provider-url PASS) + `25731846625` (GP-3 ST-3 docker secret PASS) — 4/4 PASS |
| 사용자 명시 7 금지 위반 | #1 = 사용자 명시 Step 5 결정 답습 / #2 ~ #7 = 0건 |

**본 brief 관계**: Layer C 발효 후속 — Phase α-1 ~ α-4 = **evidence 답습 한정 + Implementation 진입 *결정 권위 = Backlog #6 실 진입 + 사용자 명시 결정 영역***. 본 brief = **통합 실제 구현 *단계 분할 정리 한정***.

### 1.2 Layer D 권위 답습 (`210c98f` — 2026-05-13 + 후속 18 재진입 검토 합의)

| 영역 | 답습 |
|------|----|
| Layer D 발효 시점 | 2026-05-13 (`210c98f` APPROVE WITH CONDITIONS, 8 조건 C-1~C-8) |
| Layer D 본문 변경 | **0건** (본 brief 시점까지 보존) |
| 후속 18 재진입 검토 합의 | APPROVE AS BRIEF (Reviewer-only 단축, 25 조건 C-λ-1 ~ C-λ-25) |
| 후속 18 5 발효 문구 답습 | (i) 기존 `210c98f` 권위 유지 / (ii) Layer C 재발효 (`eb01bc4`) ≠ Layer D 재선언 / (iii) Layer D 본문 변경 0건 / (iv) MVP-1 PASS 재선언 0건 / (v) Layer E / Layer F 진입 0건 |
| C-1 ~ C-8 현 satisfaction (2026-05-16) | C-1 ✅ Satisfied / C-2 ✅ Satisfied / C-3 ⏳ Deferred (MVP-6) / C-4 ⏳ Deferred (MVP-6) / C-5 ⚠️ Partially Satisfied (C-5a ✅ + C-5b ⏳ + C-5c ⚠️) / C-6 ⚠️ Partially Satisfied (PC-4 T2 sub only) / C-7 ⏳ Requires separate full 3+1 / C-8 ⏳ Deferred (Backlog #4) |

**본 brief 관계**: Layer D 권위 = 기존 답습 유지 (재발효 / 재선언 0건). Phase α-1 ~ α-4 통합 실제 구현 = **Layer D 본문 변경 0건** + **C-5b / C-5c / C-6 / C-7 / C-8 satisfaction *자동 변경 0건*** (실 진입 단계 별도 결정 영역).

### 1.3 Phase α 4 단계 합의 답습 (C-β / C-γ / C-δ / C-ε)

| Phase | 합의 commit | 합의 형태 | 합의 조건 | 답습 line count | 본 brief 관계 |
|-------|----------|---------|----------|--------------|------------|
| Phase α-1 | `1b3090b` | Reviewer-only 단축 APPROVE AS BRIEF | 15 조건 C-β-1 ~ C-β-15 | 829줄 | 답습 한정 (실 진입 *결정 권위 영역 외*) |
| Phase α-2 | `6a79247` | Reviewer-only 단축 APPROVE AS BRIEF | 26 조건 C-γ-1 ~ C-γ-26 | 35줄 | 답습 한정 |
| Phase α-3 | `3f6306d` | Reviewer-only 단축 APPROVE AS BRIEF | 28 조건 C-δ-1 ~ C-δ-28 | 328줄 | 답습 한정 |
| Phase α-4 | `e59a565` | Reviewer-only 단축 APPROVE AS BRIEF | 29 조건 C-ε-1 ~ C-ε-29 | 1593줄 | 답습 한정 |
| **합산** | — | 4 × Reviewer-only | **98 조건** | **2785줄** | — |

### 1.4 6-Layer 분리 매트릭스 현 상태 (2026-05-16 후속 18 後)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + §5.5 `55c5b4b`) | 답습 한정 |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 | ✅ APPROVE WITH CONDITIONS (`4880e88`) | 답습 한정 |
| Backlog #6 우선 진입 | Runtime + CI-hook 영역 정의 + Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) | 답습 한정 |
| Phase α-1 R-4 진입 | R-4 (S-1 + T-2 + T-5) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`1b3090b`) | 답습 한정 |
| Phase α-2 R-5 진입 | R-5 (T-2 import-linter) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`6a79247`) | 답습 한정 |
| Phase α-3 R-7 진입 | R-7 (ST-3 docker secret) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`3f6306d`) | 답습 한정 |
| Phase α-4 R-1 진입 | R-1 (PC-3 + AR-1 CI 통합) 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`e59a565`) | 답습 한정 |
| **Layer C** | **Implementation Evidence PASS 발효** | ✅ **APPROVE (`eb01bc4` 2026-05-16) — GP-3 + GP-5 PASS** | **답습 한정 (재발효 0건)** |
| **Layer D** | **MVP-1 PASS 선언** | ✅ **APPROVE WITH CONDITIONS (`210c98f` 2026-05-13) + 후속 18 재진입 검토 답습** | **답습 한정 (재선언 0건)** |
| **Phase α-1 ~ α-4 통합 실제 구현 단계 분할** | **본 brief 영역** | ⏳ **DRAFT (본 brief = 준비안)** | **본 brief = *단계 분할 정리 한정*** |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 5 금지 #4) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 5 금지 #5) |

### 1.5 본 brief 의 framing

**Layer C 발효 後 Phase α-N 실 진입의 의미**:

| 단계 | 답습 |
|----|----|
| Layer C 발효 시점 (2026-05-16) 까지 | R-4 + R-5 + R-7 + R-1 = **PoC 본문 답습 + actual run PASS** (evidence 5/5 PASS) |
| **Phase α-1 ~ α-4 *실 진입* (본 brief 영역 외)** | PoC artifacts → **MVP-1 Backlog #6 production runtime / CI-hook 영역 격상 진입** (단, 격상 형태 = 사용자 명시 결정 영역) |
| 격상 형태 (사용자 명시 결정 영역 — 본 brief 영역 외) | 옵션 1: 답습 한정 (본문 변경 0건 한정 — production stable 격상) / 옵션 2: minor 인터페이스 정렬 한정 (CLI / exit code / 출력 포맷 답습 검증) / 옵션 3: branch protection / pre-commit / doctor 의무화 영역 진입 (사용자 명시 5 금지 #2 ~ #5 충돌 — 별도 합의 영역) |

**본 brief = 옵션 1 ~ 3 中 어느 것도 *결정하지 않음* — 단계 분할 *정리 한정***.

### 1.6 본 brief 의 진입점

```
Layer A APPROVE (f1e0b23) ──────────────────────────────────────────┐
Layer B APPROVE (f40423f)                                           │
§5.5 9 sub-수단 (55c5b4b)                                            │
Group α APPROVE (4880e88) ──────────────────────────────────────────┤
Backlog #6 우선 진입 합의 (c7ddfdd) APPROVE AS BRIEF                  │
Phase α-1 R-4 brief (e7cdb21) + 합의 (1b3090b) APPROVE AS BRIEF      │
Phase α-2 R-5 brief (608a046) + 합의 (6a79247) APPROVE AS BRIEF      │
Phase α-3 R-7 brief (8da3273) + 합의 (3f6306d) APPROVE AS BRIEF      │
Phase α-4 R-1 brief (38eb013) + 합의 (e59a565) APPROVE AS BRIEF
4 prerequisite actual run PASS (25728590939 + 25728590916 + 25728590977 + 25731846625)
Layer C 발효 (eb01bc4 2026-05-16) — MVP-1 Implementation Evidence PASS + GP-3 + GP-5 PASS
Layer D 권위 답습 (210c98f 2026-05-13 + 후속 18 재진입 검토 APPROVE AS BRIEF)
   │
   ▼
■ 본 brief = Phase α-1 ~ α-4 통합 실제 구현 *단계 분할 정리* (DRAFT)         ← 현 위치
   │
   ▼ (사용자 명시 승인 後 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 後 — 자동 진입 0건)
■ Phase α-1 ~ α-4 *통합 실 진입* (격상 형태 = 사용자 명시 결정 영역)         ← 본 brief 영역 외
   │
   ▼ (실 진입 형태 / 단계 / 합의 형태 모두 사용자 명시 결정 영역)
■ MVP-1 본문 격상 완료 (단계 분할 形 답습)                                  ← 본 brief 영역 외
```

---

## 2. Phase α 4 단계 영역 합산 정의

### 2.1 4 영역 본문 합산 매트릭스 (2785줄 답습)

| Phase | 영역 | artifact 수 | line count | 답습 출처 | sub-수단 (§5.5) |
|-------|----|----------|---------|---------|--------------|
| **α-1 (R-4)** | 3 도구 본문 | 3 file | **829** | Group D PoC + Group A 1차 + Group A 3차 | S-1 (`secret_scanner.py` 368) + T-2 (`provider_import_scanner.py` 178) + T-5 (`provider_url_scanner.py` 283) |
| **α-2 (R-5)** | `.importlinter` 본문 | 1 file | **35** | Group A 2차 합의 (`a6e82f1`) + C-9 RA-9 사전 검증 PASS (2026-05-10) + 각주 1 google.generativeai | T-6 (T-2 + T-5 병행 中 T-2 import-linter 측면) |
| **α-3 (R-7)** | docker secret block | 9 file | **328** | GP-3 Stage 2 합의 (Reviewer-only APPROVE) + ADR-008 §2.6.2 R2-1 | ST-3 (Hermes upstream 변경 0건 보존) |
| **α-4 (R-1)** | CI workflow 통합 | 7 file | **1593** | Stage 4 합의 (Reviewer-only APPROVE) + Layer B §5.5.1 PC-3 + AR-1 | PC-3 + AR-1 (양 GP 공유) |
| **합산** | **4 영역** | **20 file** | **2785** | — | **5 sub-수단** (S-1 + T-2 + T-5 + ST-3 + PC-3 + AR-1) |

**§5.5 9 sub-수단 매트릭스 中 본 brief 영역**: 6 sub-수단 (S-1 + T-2 + T-5 + ST-3 + PC-3 + AR-1) — **나머지 3 sub-수단 (PC-4 + AR-2 + AR-3) = 본 brief 영역 외 (Backlog #1 + #2 + #3 + Group α T3 sub 분리)**.

### 2.2 의존성 토폴로지 — 1순위 병렬 + 2순위 의존

본 §은 Backlog #6 우선 진입 합의 §6.1 답습 + Phase α-4 brief §1.1 답습 — 통합 매트릭스:

```
┌─────────────────────────────────────────────────────────────┐
│ 1순위 병렬 그룹 (Backlog #6 §6.1 답습)                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Phase α-1    │  │ Phase α-2    │  │ Phase α-3    │      │
│  │ R-4 도구 본문  │  │ R-5 importlin│  │ R-7 docker   │      │
│  │ (829줄)       │  │ (35줄)        │  │ secret (328) │      │
│  │ Stage 1+3     │  │ Stage 3 T-2  │  │ Stage 2 ST-3 │      │
│  └───────┬──────┘  └──────┬───────┘  └───────┬──────┘      │
│          │                │                  │              │
└──────────┼────────────────┼──────────────────┼──────────────┘
           │                │                  │
           ▼                ▼                  ▼
    [actual run PASS 답습]  [actual run PASS 답습]  [actual run PASS 답습]
    25728590916+977       25728590916 (T-2)     25731846625 (Stage 2)
    25728590939 (Stage 1)                       
           │                │                  │
           └────────┬───────┴──────────────────┘
                    ▼
┌─────────────────────────────────────────────────────────────┐
│ 2순위 의존 그룹 (Backlog #6 §6.1 + Stage 4 합의 답습)            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│         ┌─────────────────────────────┐                     │
│         │ Phase α-4                   │                     │
│         │ R-1 CI workflow 통합 (1593줄)│                     │
│         │ Stage 4 (PC-3 + AR-1)       │                     │
│         │                             │                     │
│         │ ⚠️ 의존: α-1 + α-2 + α-3     │                     │
│         │   actual run PASS 선행 evidence│                  │
│         └─────────────────────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**의존성 매트릭스 (논리적)**:

| 의존 방향 | 답습 |
|---------|----|
| Phase α-1 ↔ α-2 | **부분 의존** (T-6 T-2 + T-5 병행 답습 — α-1 의 `provider_import_scanner.py` ↔ α-2 의 `.importlinter` 양 도구 보완 답습) — **단, 본문 *수정* 시 양측 영향 미발생 0건** (T-2 import-linter = transitive, T-5 AST = runtime / 모델명 / URL — 책무 분리 답습) |
| Phase α-1 ↔ α-3 | **독립** (Stage 1 + Stage 3 = 양 GP 독립, Group D ↔ Group A 1차/3차 독립) |
| Phase α-2 ↔ α-3 | **독립** (`.importlinter` ↔ docker secret block 직교) |
| Phase α-4 ↔ α-1 + α-2 + α-3 | **선행 의존** (Stage 4 = Stage 1 + Stage 3 actual run PASS 선행 evidence 의무 답습) |
| Phase α-4 → Layer C | **이미 발효 完** (`eb01bc4` 2026-05-16) |
| 양 GP 의존성 | GP-3 = S-1 + ST-3 + PC-3 + AR-1 (Layer B §5.5.1 답습) / GP-5 = T-2 + T-5 + T-6 + PC-3 + AR-1 (Layer B §5.5.2 답습) — **PC-3 + AR-1 양 GP 공유** |

### 2.3 4 영역 = Layer B §5.5 9 sub-수단 답습 매트릭스

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | 본 brief 4 Phase 영역 매트릭스 | 분리 영역 |
|----------|------|----------------------|------------------------|---------|
| **S-1** | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | **Phase α-1 R-4** | — |
| S-2 | gitleaks 보조 | 비채택 (MVP-1 1차) | — | Backlog #1 1.5차 보강 영역 분리 |
| **ST-3** | docker secret isolation + image layer + restart recovery | GP-3 Stage 2 합의 답습 | **Phase α-3 R-7** | — |
| ST-1 / ST-2 / ST-4 / ST-5 | entrypoint stat / inotify sidecar / Vault HSM / Defense in depth | 비채택 (MVP-1 1차) | — | Backlog #1 + #7 + MVP-2 영역 분리 |
| **PC-3** | CI-only enforcement (양 GP 공유) | Layer B §5.5.1 + §5.5.2 답습 | **Phase α-4 R-1** | — |
| PC-4 | local pre-commit framework | Group α T3 sub 단독 풀 3+1 (영역 권위 권고 한정) | — | Backlog #1 + #2 + Group α 분리 (사용자 명시 #5 답습) |
| **AR-1** | PR auto-reject fail-closed | Layer B §5.5.1 + §5.5.2 답습 | **Phase α-4 R-1** | — |
| AR-2 | branch protection rule | Group α C-1 + C-4 권위 권고 한정 (실 활성화 = T3) | — | Backlog #3 + Group α 분리 (사용자 명시 #2 답습) |
| AR-3 | 자동 revert bot | Group α 단독 풀 3+1 (T3 영역 권위 권고) | — | Backlog #3 분리 |
| **T-2** | Layer 1 정적 차단 (custom AST) | Group A 1차 답습 | **Phase α-1 R-4** | — |
| **T-2 import-linter** | Layer 1b transitive import 차단 | Group A 2차 합의 답습 | **Phase α-2 R-5** | — |
| **T-5** | URL/Model 정적 차단 | Group A 3차 답습 | **Phase α-1 R-4** | — |
| T-6 | T-2 + T-5 병행 | Group A 2차 + 3차 답습 | **Phase α-1 + α-2 R-4 + R-5** | — |

**합산**: 본 brief 4 Phase 영역 = **6 sub-수단** (S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1) — **9 sub-수단 中 3 sub-수단 (PC-4 + AR-2 + AR-3) = 본 brief 영역 외 (Backlog #1 + #2 + #3 + Group α T3 sub 분리)**.

### 2.4 Layer B 9 sub-수단 본문 채택 변경 0건 답습

본 §은 `55c5b4b` 답습 한정 — 본 brief 시점까지 § 5.5 9 sub-수단 본문 채택 변경 0건:

| 답습 영역 | 본 brief 변경 |
|--------|----------|
| 9 sub-수단 본문 채택 (`55c5b4b`) | 0건 |
| 6 sub-수단 (S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1) 답습 매트릭스 | enumerate 한정 |
| 3 sub-수단 (PC-4 + AR-2 + AR-3) 분리 매트릭스 | 분리 명시 한정 |

---

## 3. 통합 실제 구현 단계 분할 매트릭스

### 3.1 Phase α-1 단계 분할 (11 sub-step — 답습 한정)

Phase α-1 R-4 entry brief §3.1 ~ §3.4 답습 한정 (실 진입 시점 결정 = 사용자 명시 결정 영역):

| Stage | 도구 | sub-step | sub-step 영역 | 답습 출처 | 본 brief 영역 |
|-------|------|---------|------------|---------|------------|
| Stage 1 | `secret_scanner.py` | 1.1 | 본문 답습 검증 (368줄) | Group D PoC §2.1 (A) | enumerate 한정 |
| Stage 1 | `secret_scanner.py` | 1.2 | MVP-1 entry CI 통합 인터페이스 정렬 (CLI / exit code / 출력 포맷 답습 검증) | Group D 12 step + Layer B §1.1 | 실 workflow 변경 = R-1 영역 (Phase α-4) |
| Stage 1 | `secret_scanner.py` | 1.3 | ledger entry 형식 (`event: secret_scan_layer1_implementation` 후보 한정) | mvp1.md §5.2 enum 후보 | 정식 등록 0건 (Backlog #5 분리) |
| Stage 1 | `secret_scanner.py` | 1.4 | Evidence Artifact 형식 (Markdown report 출력 후보) | Layer B §1.8 (a) | 실 생성 = Layer C 시점 (이미 완) |
| Stage 3 | `provider_import_scanner.py` (T-2) | 3.2 | 본문 답습 검증 (178줄, AST 5 패턴) | Group A 1차 PoC | enumerate 한정 |
| Stage 3 | `provider_import_scanner.py` (T-2) | 3.2.a | CLI 인자 / exit code / 출력 포맷 답습 검증 | Group A 1차 | 실 workflow 변경 = R-1 영역 |
| Stage 3 | `provider_import_scanner.py` (T-2) | 3.2.b | facade exemption (`src/adapters/llm/facade.py`) 답습 검증 | Group A 1차 §5 | 실 facade 본문 = Backlog #4 분리 |
| Stage 3 | `provider_url_scanner.py` (T-5) | 3.3 | 본문 답습 검증 (283줄, URL Tier-1 10 + Model Tier-1 19) | Group A 3차 PoC | enumerate 한정 |
| Stage 3 | `provider_url_scanner.py` (T-5) | 3.3.a | URL Tier-1 catalog 답습 검증 | Group A 3차 §4 | 실 catalog 변경 = Backlog #3 분리 |
| Stage 3 | `provider_url_scanner.py` (T-5) | 3.3.b | Model Tier-1 catalog 답습 검증 | Group A 3차 §5 | 실 catalog 변경 = Backlog #3 분리 |
| Stage 3 | `provider_url_scanner.py` (T-5) | 3.3.c | CLI 인자 / exit code / 출력 포맷 답습 검증 | Group A 3차 | 실 workflow 변경 = R-1 영역 |
| **합산** | **3 도구** | **11 sub-step** | — | — | **단계 분할 정리 한정** |

### 3.2 Phase α-2 단계 분할 (`.importlinter` 본문 6 항목 — 답습 한정)

Phase α-2 R-5 entry brief §2 답습 한정:

| # | 항목 | 현 본문 값 (답습) | 답습 출처 | 본 brief 영역 |
|---|----|------------|---------|------------|
| 1 | `root_packages` | `src` (옵션 A) | Group A 2차 합의 §1.2 — `src/` 만 (미래 대상 + future-proof) | enumerate 한정 (변경 0건) |
| 2 | `include_external_packages` | `True` | C-9 RA-9 사전 검증 PASS (2026-05-10) + Group A 2차 §1.3 | enumerate 한정 (TR-3 답습) |
| 3 | forbidden 4 module | `openai` + `anthropic` + `litellm` + `ollama` | Group A 2차 §1.4 (transitive import 강점 답습) | enumerate 한정 (forbidden 추가 / 삭제 = Backlog #2 1.5차 보강) |
| 4 | facade single allow (`ignore_imports`) | `src.adapters.llm.facade -> *` | Group A 2차 §1.5 (TR-1 답습 — facade real 본문 작성 시 재합의) | enumerate 한정 (TR-1 답습) |
| 5 | google.generativeai 각주 1 (책무 분리) | 1차 AST scanner 단독 책무 (`.importlinter` 본 룰 흡수 0건) | Group A 2차 §1.6 (TR-4 답습) | enumerate 한정 (TR-4 답습) |
| 6 | docstring + 답습 주석 | 답습 한정 (실 본문 변경 0건) | 35줄 본문 답습 | enumerate 한정 |
| **합산** | **6 항목** | **35줄** | Group A 2차 답습 | **단계 분할 정리 한정** |

**TR-1 ~ TR-5 재합의 trigger 답습** (Phase α-2 brief §6 답습 — 본 brief 영역 외):

| Trigger | 발화 조건 | 본 brief 영역 |
|--------|---------|------------|
| TR-1 | facade real 본문 작성 시 (Backlog #4 진입 시) | Backlog #4 분리 (Layer D C-8 답습) |
| TR-2 | import-linter 라이브러리 버전 / 호환성 변화 | enumerate 한정 (발화 0건) |
| TR-3 | `include_external_packages = True` 동작 불일치 발생 | enumerate 한정 (발화 0건) |
| TR-4 | google.generativeai 본 룰 흡수 시도 | enumerate 한정 (발화 0건) |
| TR-5 | URL/endpoint 본 룰 흡수 시도 (T-5 영역 흡수) | enumerate 한정 (발화 0건) |

### 3.3 Phase α-3 단계 분할 (4 sub-step — 답습 한정)

Phase α-3 R-7 entry brief §3 답습 한정:

| sub-step | 영역 | 답습 출처 | 현 artifact (답습 한정) | 본 brief 영역 |
|---------|----|---------|---------------------|------------|
| 2.1 | docker-compose secret block | GP-3 Stage 2 §2.1 답습 | `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` (34줄) + `Dockerfile` (12줄) + `app.py` (46줄) + `secrets/api_key.placeholder` (1줄) | enumerate 한정 (변경 0건) |
| 2.2 | image layer 검증 | GP-3 Stage 2 §2.2 답습 | `tools/docker_secret_image_layer_check.sh` (99줄) | enumerate 한정 (변경 0건) |
| 2.3 | container restart recovery | GP-3 Stage 2 §2.3 답습 | `tools/docker_secret_restart_recovery.sh` (118줄) | enumerate 한정 (변경 0건) |
| 2.4 | CI Stage 2 entry step + Evidence | GP-3 Stage 2 §2.4 답습 | `tests/fixtures/gp3_st3/{pass,fail}/` (18줄) + `secret-hygiene-egress-redaction.yml` Stage 2 entry steps | enumerate 한정 (변경 0건, R-1 영역) |
| **합산** | **4 sub-step** | — | **9 artifact × 328줄** | **단계 분할 정리 한정** |

### 3.4 Phase α-4 단계 분할 (4 sub-step — 답습 한정)

Phase α-4 R-1 entry brief §3 답습 한정:

| sub-step | 영역 | 답습 출처 | 현 artifact (답습 한정) | 본 brief 영역 |
|---------|----|---------|---------------------|------------|
| 4.1 | PC-3 CI step 통합 | Stage 4 §4.1 답습 + Layer B §5.5.1 PC-3 답습 | `secret-hygiene-egress-redaction.yml` (694줄) + `provider-adapter-enforcement.yml` (186줄) + `provider-url-scanner.yml` (326줄) + `tools/mvp1_pc3_ar1_integration_check.py` (298줄) | enumerate 한정 (변경 0건) |
| 4.2 | AR-1 fail-closed 통합 | Stage 4 §4.2 답습 + Layer B §5.5.1 AR-1 답습 | 동상 (workflow `continue-on-error: false` 답습 + AR-1 fail-closed step 답습) | enumerate 한정 (변경 0건) |
| 4.3 | PC-4 local pre-commit framework | **본 brief 영역 외** — Backlog #1 + #2 1.5차 보강 분리 (사용자 명시 5 금지 #2 ~ #5 영향 영역) | `.pre-commit-config.yaml` 본문 작성 0건 / `default_install_hook_types` 결정 0건 | **분리 명시 한정** |
| 4.4 | AR-2 branch protection rule | **본 brief 영역 외** — Backlog #3 T3 영역 별도 풀 3+1 분리 (Group α 합의 + 사용자 명시 5 금지 #2 ~ #5 영향) | CODEOWNERS / required status check / direct push / force push / admin bypass / required PR review / linear history / deployments 모두 변경 0건 | **분리 명시 한정** |
| **합산** | **4 sub-step** | — | **7 artifact × 1593줄 (4.1 + 4.2 한정)** | **단계 분할 정리 한정** |

**Phase α-4 sub-step 4.3 / 4.4 = 본 brief 영역 외 (분리 명시 한정)** — 사용자 명시 5 금지 #2 (CI workflow 변경) / #3 (runtime code 변경) 외에도 추가 영역 (branch protection / dev 환경 / pre-commit install 의무화) 모두 본 brief 영역 외.

### 3.5 통합 실제 구현 cycle 패턴 (단계 분할 한정)

본 §은 *실 진입 시점 cycle 패턴 권위 권고 한정* — 실 진입 결정 = 사용자 명시 결정 영역:

**옵션 (i)**: 1순위 병렬 — 2순위 의존 cycle:

```
[Step 0] 사전 점검 — 9 evidence + 4 actual run PASS 답습 검증 (Layer C 발효 답습)
                                             │
[Step 1] 1순위 병렬 진입 — Phase α-1 + α-2 + α-3 (병렬)
            │ Phase α-1: 11 sub-step (Stage 1 4 + Stage 3 T-2 3 + Stage 3 T-5 4)
            │ Phase α-2: 6 항목 (root + include + 4 forbidden + facade single allow + 각주 1 + docstring)
            │ Phase α-3: 4 sub-step (2.1 + 2.2 + 2.3 + 2.4)
                                             │
[Step 2] 1순위 actual run PASS 답습 (4 prerequisite run 답습 한정 — 재실행 0건)
                                             │
[Step 3] 2순위 진입 — Phase α-4 R-1
            │ sub-step 4.1 PC-3 CI step 통합
            │ sub-step 4.2 AR-1 fail-closed 통합
            │ ⚠️ sub-step 4.3 + 4.4 = 본 brief 영역 외 (분리 명시)
                                             │
[Step 4] 2순위 actual run PASS 답습
                                             │
[Step 5] 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
                                             │
[Step 6] 메타 갱신 + commit + push (CONTEXT / INDEX / SESSION)
```

**옵션 (ii)**: 4 Phase 모두 1순위 → 단일 cycle:

```
[Step 0] 사전 점검
[Step 1] 4 Phase (α-1 + α-2 + α-3 + α-4) 모두 진입 (단, α-4 는 α-1 ~ α-3 prerequisite actual run PASS 선행 evidence 답습 의무)
[Step 2] actual run PASS 답습
[Step 3] 합의 보고서 작성
[Step 4] 메타 갱신 + commit + push
```

**옵션 (iii)**: 4 Phase 각각 독립 cycle:

```
[Phase α-1 cycle] Step 0 ~ Step 4 (cycle 1)
[Phase α-2 cycle] Step 0 ~ Step 4 (cycle 2)
[Phase α-3 cycle] Step 0 ~ Step 4 (cycle 3)
[Phase α-4 cycle] Step 0 ~ Step 4 (cycle 4) — α-1 ~ α-3 actual run PASS 선행 evidence 답습 의무
```

**본 §3.5 = 옵션 (i) ~ (iii) 권고 한정 — 사용자 명시 결정 영역**. 본 brief = 어느 옵션도 *결정하지 않음*.

### 3.6 actual run 답습 매트릭스

| Stage | workflow | run_id | commit SHA | 결과 | 본 brief 영역 |
|-------|---------|--------|-----------|------|------------|
| Stage 1 GP-3 secret-hygiene | `secret-hygiene-egress-redaction.yml` | `25728590939` | `72622409` | PASS | 답습 한정 (재실행 0건) |
| Stage 3 GP-5 provider-adapter | `provider-adapter-enforcement.yml` | `25728590916` | `72622409` | PASS | 답습 한정 (재실행 0건) |
| Stage 3 GP-5 provider-url-scanner | `provider-url-scanner.yml` | `25728590977` | `72622409` | PASS | 답습 한정 (재실행 0건) |
| Stage 2 GP-3 ST-3 docker secret | `secret-hygiene-egress-redaction.yml` Stage 2 entry | `25731846625` | `6c6b208` | PASS | 답습 한정 (재실행 0건) |
| **합산** | — | **4 run** | — | **4/4 PASS** | **답습 한정** |

**Layer C 발효 (`eb01bc4`) 합의 §4.3 답습**: 4/4 PASS + 5 source cross-reference 일관 + 재실행 0건 + 신규 trigger 0건.

### 3.7 본 §3 의 *범위 한계*

본 §3 = **단계 분할 *정리 한정***. 실 sub-step / 실 항목 / 실 sub-step 결정 / 실 cycle 옵션 결정 / 실 본문 변경 = 사용자 명시 결정 영역 + Phase α-N 실 진입 시점 (Backlog #6 + 사용자 명시 결정 영역 — 본 brief 영역 외).

---

## 4. 사용자 명시 5 금지 영역 × 4 Phase 분리 매트릭스

### 4.1 금지 #1 — 실제 파일 수정 (4 Phase 분리)

| Phase | 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|-------|----|----------------|------------------------|
| α-1 | R-4 829줄 | ❌ (영역 외) | 실 진입 후 본문 변경 = 사용자 명시 결정 영역 |
| α-2 | R-5 35줄 | ❌ (영역 외) | 동상 |
| α-3 | R-7 328줄 | ❌ (영역 외) | 동상 |
| α-4 | R-1 1593줄 (4.1 + 4.2) | ❌ (영역 외) | 동상 |
| α-4 | R-1 sub-step 4.3 + 4.4 | ❌ (영역 외) | Backlog #1 + #2 + #3 분리 |
| **본 brief 영역 *내* 적격 작업** | **4 Phase 본문 답습 *enumerate 한정* + 단계 분할 정리 한정** | — |

### 4.2 금지 #2 — CI workflow 변경 (4 Phase 분리)

| Phase | 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|-------|----|----------------|------------------------|
| α-1 | R-4 도구 = CI step 측면 | ❌ (영역 외) | 실 workflow 변경 = R-1 영역 (Phase α-4) |
| α-2 | R-5 = CI step 측면 (`provider-adapter-enforcement.yml` import-linter step) | ❌ (영역 외) | 동상 |
| α-3 | R-7 = `secret-hygiene-egress-redaction.yml` Stage 2 entry step | ❌ (영역 외) | 동상 |
| α-4 | R-1 = 3 MVP-1 workflow 본문 (4.1 + 4.2) | ❌ (영역 외) | 사용자 명시 결정 영역 |
| α-4 | 3 MVP-1 workflow 외 신설 | ❌ (영역 외) | 사용자 명시 5 금지 #2 영구 답습 |
| **본 brief 영역 *내* 적격 작업** | **3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 답습 *enumerate 한정*** | — |

### 4.3 금지 #3 — runtime code 변경 (4 Phase 분리)

| Phase | 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|-------|----|----------------|------------------------|
| α-1 | R-4 = `tools/` 영역 (runtime ≠ `tools/`) | ❌ (영역 외) | `tools/` 본문 변경 = 실 진입 시점 결정 영역 |
| α-2 | R-5 = `.importlinter` config 영역 (runtime 영향 0) | ❌ (영역 외) | 동상 |
| α-3 | R-7 = `docker/` 영역 (runtime ≠ `src/`) | ❌ (영역 외) | 동상 |
| α-4 | R-1 = `.github/workflows/` + `tools/` 영역 | ❌ (영역 외) | 동상 |
| 4 Phase 통합 | `src/` 본문 | ❌ (영역 외) | `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 = Backlog #4 분리 (Layer D C-8 답습) |
| **본 brief 영역 *내* 적격 작업** | **`src/` 본문 = `facade.py` placeholder 답습 *enumerate 한정* (변경 0건)** | — |

### 4.4 금지 #4 — Operational Readiness PASS (4 Phase 분리)

| Phase | 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|-------|----|----------------|------------------------|
| α-1 ~ α-4 | Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| α-1 ~ α-4 | MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (4 Phase = 구현 영역, Layer E = 운영 영역 — 분리)** | — |

### 4.5 금지 #5 — Hermes PMO 격상 (4 Phase 분리)

| Phase | 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|-------|----|----------------|------------------------|
| α-1 ~ α-4 | Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (4 Phase = 코드 / config / workflow 영역, Layer F = governance 영역 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.6 추가 분리 영역 (사용자 명시 5 금지 외 — 본 brief 영역 외 명시 답습)

본 §은 사용자 명시 5 금지 *외* 추가 영역 — 본 brief 영역 외 (분리 명시 한정):

| # | 영역 | 분리 답습 |
|---|----|--------|
| 6 | branch protection 변경 (AR-2) | Group α 합의 5.1 #6 답습 + Backlog #3 T3 영역 분리 |
| 7 | dev 환경 강제 (`tools/doctor.py`) | Backlog #2 영역 분리 |
| 8 | `pre-commit install` 의무화 | Group α 합의 5.2 #9 답습 + Backlog #1 + #2 1.5차 보강 분리 |
| 9 | `.pre-commit-config.yaml` 본문 작성 | 동상 (Backlog #1 + #2) |
| 10 | `.git/hooks/pre-commit` 본문 작성 | 동상 |
| 11 | AR-3 자동 revert bot | Backlog #3 T3 영역 분리 |
| 12 | ST-1 entrypoint stat / ST-2 inotify sidecar / ST-4 Vault HSM / ST-5 Defense in depth | Backlog #1 + #7 + MVP-2 분리 |
| 13 | S-2 gitleaks | Backlog #1 1.5차 보강 분리 |
| 14 | R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 | Group α 합의 5.1 #8 + Backlog #3 분리 |
| 15 | Tier-2 / Tier-3 catalog 자동 확장 | 동상 |
| 16 | Hermes upstream Dockerfile 변경 | ADR-008 §2.6.2 R2-1 영구 답습 |
| 17 | Production `docker-compose.yml` 신설 / 변경 | PoC 격리 디렉토리 한정 (R-7 답습) |
| 18 | 실 secret material commit | F-금지 #1 영구 답습 (Group D §1.2 #1 답습) |
| 19 | GitHub Actions secrets 사용 도입 | F-금지 #1 영구 답습 (G3-7 (i)) |
| 20 | `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 21 | commit signing 도입 | MVP-6 영역 답습 |
| 22 | Stage 5 (G3-7 4 항목) 자동 진입 | Stage 4 후속 권고 답습 한정 |
| 23 | event enum 정식 등록 (`event:` field) | Backlog #5 ADR-012 §2.2 분리 (Layer D C-2 ✅ Satisfied 답습) |
| 24 | `src/adapters/llm/facade.py` real 본문 작성 | Backlog #4 분리 (Layer D C-8 답습) |
| 25 | Group I (Hermes-originated commit auto-reject) | 별도 합의 영역 (Group α C-2 답습) |
| 26 | token rotation 정책 결정 | 별도 합의 영역 (Group α C-3 답습) |
| 27 | GitHub plan / ruleset 가용성 확인 | 별도 합의 영역 (Group α C-4 답습) |
| 28 | Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 29 | 의미적 lock-in 검사 (G4 §4.6 라운드트립 검증) | MVP-3 영역 분리 |

### 4.7 본 §4 의 *범위 한계*

본 §4 = **5 금지 + 추가 24 분리 영역 *분리 매트릭스 한정***. 어느 영역도 *해소* 0건 + Phase α-N 실 진입 자동 진입 0건.

---

## 5. 통합 실제 구현 진입 적격성 검토

### 5.1 Layer C 발효 후속 적격성 5 조건 (본 brief 시점 = 2026-05-16)

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-π-1** | **사용자 명시 5 금지 영역 충돌 0** | 4 Phase 영역 = 코드 / config / workflow / docker secret 영역 — 금지 #4 (Layer E) / #5 (Layer F) 모두 직교 (충돌 0). 금지 #1 (실 파일 수정) / #2 (CI workflow 변경) / #3 (runtime code 변경) = Phase α-N *실 진입* 시점 적용 — 본 brief = *단계 분할 정리 한정* (충돌 0). | ✅ **0/5 충돌** |
| **C-π-2** | **Layer C 발효 (`eb01bc4`) evidence 답습 100% 보존** | 양 GP × 5 조건 = 10/10 PASS 답습 + 9/9 evidence 재생성 0건 + 4/4 prerequisite actual run 재실행 0건 + 8/8 evidence file line count 정확 일치 | ✅ **답습 100% 보존** |
| **C-π-3** | **Layer D 권위 (`210c98f` + 후속 18) 답습 100% 보존** | Layer D 본문 변경 0건 + C-1 ~ C-8 satisfaction 자동 변경 0건 + MVP-1 PASS 재선언 0건 | ✅ **답습 100% 보존** |
| **C-π-4** | **Provider Liquidity 5-way 100% 보존** | R-4 + R-5 + R-7 + R-1 = enforcement / config / docker secret / workflow 영역 — catalog / provider 영역과 직교 + Tier-1 답습 한정 + 5-vendor 차단 패턴 답습 변경 0건 | ✅ **5/5 100% 보존** |
| **C-π-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (4 Phase = 코드 영역, Hermes PMO 영역 분리) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (4 Phase = 수단, 목적 = secret 검출 + provider 차단 + docker secret + CI enforcement) / T1/T2/T3 분리 보존 (4 Phase = T2 영역 → T3 영역 진입 0건) / SPOF 의도적 수용 보존 (4 Phase = enforcement 영역 답습) | ✅ **5/5 보존** |

### 5.2 의존성 의무 검토 (Phase α-4 = α-1 ~ α-3 선행 evidence 의무)

| 의존성 영역 | 답습 |
|----------|----|
| Phase α-1 / α-2 / α-3 actual run PASS | ✅ **답습 完** (4/4 PASS — `25728590939` + `25728590916` + `25728590977` + `25731846625`) |
| Phase α-4 sub-step 4.1 + 4.2 진입 적격성 | ✅ **선행 evidence 100% 答** (Stage 4 합의 발효 시점 답습) |
| Phase α-4 sub-step 4.3 + 4.4 | ⚠️ **본 brief 영역 외 분리 명시** (Backlog #1 + #2 + #3 분리) |
| 1순위 병렬 그룹 (α-1 + α-2 + α-3) ↔ 2순위 (α-4) 의존성 | 충돌 0건 — Layer C 발효 시점 의무 100% 답습 (Stage 4 합의 답습) |

### 5.3 풀 3+1 승격 트리거 검토 (8/8 미발화 확정)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 어느 것의 *재결정* 을 권고하는 경우 | ❌ 0건 — 본 brief = Group α 답습 한정 |
| 2 | 본 brief 가 사용자 명시 5 금지 영역 中 1+ 의 *해소* 를 권고하는 경우 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 3 | 본 brief 가 Layer B §5.5 9 sub-수단 *재결정* 을 권고하는 경우 | ❌ 0건 — 본 brief = 답습 한정 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 — 4 Phase = catalog / provider 영역과 직교 |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 의 약화를 포함하는 경우 | ❌ 0건 — 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입을 권고하는 경우 | ❌ 0건 — T3 분리 명시 한정 (4 Phase = T2 영역) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 의 충족을 발생시키는 경우 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 (사용자 명시 5 금지 #5 답습) |
| 8 | 본 brief 가 Layer C / Layer D 재발효 / 재선언 / 재진입 권고 | ❌ 0건 — Layer C 발효 답습 / Layer D 권위 답습 한정 (후속 18 답습) |

**검토 결과**: **8/8 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 확정** (사용자 명시 결정 시).

### 5.4 합산 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| C-π-1 ~ C-π-5 5 조건 | **5/5 충족** |
| 의존성 의무 검토 | **100% 답습 보존** |
| 8 풀 3+1 트리거 | **0/8 발화** |
| **Phase α-1 ~ α-4 통합 실제 구현 진입 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.5 본 §5 의 *범위 한계*

본 §5 = **진입 적격성 *검토 한정***. 실 Phase α-1 ~ α-4 통합 실제 구현 진입 결정 / 실 cycle 옵션 결정 / 실 합의 형태 결정 / 실 본문 변경 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 적격 판정 = 적격성 권위 권고 한정 — 실 진입 발효 권위 0건.

---

## 6. Rollback Trigger 의존성 답습 (통합)

### 6.1 4 Phase 영역 영향 받는 trigger 답습 매트릭스 (발화 0건)

본 §은 Phase α-1 ~ α-4 entry brief §6 합산 답습 — 18+ Rollback Trigger 中 4 Phase 본문 영역 *영향* 받는 trigger enumerate 한정 — 발화 0건:

| Trigger | 발화 조건 | Phase 영역 | 본 brief 영역 |
|--------|---------|---------|------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | α-1 (R-4) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 | — (Backlog #1) | 영역 외 |
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | α-3 (R-7) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | α-1 + α-4 (R-4 + R-1) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | α-4 (R-1) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | α-1 (R-4) | 영역 외 (Backlog #3) |
| R-MVP1-G3-7 | Tier-2 확장 필요 | α-1 (R-4) | 영역 외 (Backlog #1) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 | — (Layer E) | 영역 외 (금지 #4 답습) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | α-1 + α-2 (R-4 + R-5) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | α-1 (R-4) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) | α-1 + α-2 (R-4 + R-5) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | α-2 (R-5) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | α-4 (R-1) | 영역 외 (Backlog #3) |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 | α-4 (R-1) | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 | α-1 + α-2 (R-4 + R-5) | 영역 외 (Backlog #4 — Layer D C-8 답습) |
| R-MVP1-G5-8 | branch protection 필요 trigger | — (Backlog #3) | 영역 외 (금지 #2 답습 + 추가 #6 분리) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 | — (MVP-3) | 영역 외 |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 | — (MVP-3/4) | 영역 외 |
| R-MVP1-G5-AR3-STAGE 1차 | required status check 도입 | — (Backlog #3) | 영역 외 (Phase α-4 sub-step 4.4 분리) |
| R-MVP1-G3-PC4T3-STAGE 1차 | opt-in → doctor warning | — (Backlog #1+2) | 영역 외 (Phase α-4 sub-step 4.3 분리) |

### 6.2 TR-1 ~ TR-5 재합의 trigger 답습 매트릭스 (Group A 2차 — α-2 R-5 한정)

| Trigger | 발화 조건 | 본 brief 발화 |
|--------|---------|----------|
| TR-1 | facade real 본문 작성 시 (Backlog #4 진입 시) | ❌ 0건 (영역 외) |
| TR-2 | import-linter 라이브러리 버전 / 호환성 변화 | ❌ 0건 (발화 0건) |
| TR-3 | `include_external_packages = True` 동작 불일치 발생 | ❌ 0건 (발화 0건) |
| TR-4 | google.generativeai 본 룰 흡수 시도 | ❌ 0건 (발화 0건) |
| TR-5 | URL/endpoint 본 룰 흡수 시도 (T-5 영역 흡수) | ❌ 0건 (발화 0건) |

### 6.3 합산 매트릭스

| 영역 | trigger 수 | 본 brief 영역 |
|------|---------|------------|
| **4 Phase 본문 영역 *직접* 영향** | 10 (G3-1, G3-3, G3-4, G3-5, G5-1, G5-2, G5-3, G5-4, G5-6 + 부분) | 의존성 *enumerate 한정* — 발화 0건 |
| 4 Phase 영역 *간접* 영향 | 3 (G3-7, G5-7, G5-AR3/PC4T3 STAGE 부분) | 영역 외 (Backlog #1 / #3 / #4) |
| 4 Phase 영역 *영향 0* (T3/MVP-3/MVP-6/Backlog 분리) | 7 | 영역 외 |
| TR-1 ~ TR-5 (Group A 2차 α-2 R-5 한정) | 5 | 의존성 *enumerate 한정* — 발화 0건 |
| **합산 발화** | — | **0건 (영구 답습)** |

### 6.4 threshold 후보 한정 답습

본 §은 **threshold *고정* 0건 영구 답습** — 4 Phase 영역 영향 threshold 모두 *후보 한정* 유지:

| threshold 영역 | 후보 값 답습 (고정 0건) |
|-------------|------------------|
| S-1 FP_rate | >5% (후보) |
| T-2 FP_rate | >5% (후보) |
| T-5 FN_rate | 후보 한정 |
| PC-3 CI runtime | >2분 (후보) |
| ST-3 image layer leak count | 후보 한정 |
| ST-3 container restart recovery rate | 후보 한정 |
| AR-1 PR check pass rate / fail-closed rate | 후보 한정 |

### 6.5 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* + 신규 trigger 추가 0건.

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|----------|
| 1 | **실제 파일 수정** (사용자 명시 5 금지 #1) | 0건 (합산 2785줄 답습 보존) |
| 2 | **CI workflow 변경** (사용자 명시 5 금지 #2) | 0건 (3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 답습 보존) |
| 3 | **runtime code 변경** (사용자 명시 5 금지 #3) | 0건 (`src/` 본문 + `facade.py` 41줄 placeholder 답습 보존) |
| 4 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4) | 0건 |
| 5 | **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5) | 0건 |
| 6 | branch protection 변경 (추가 분리) | 0건 |
| 7 | dev 환경 강제 (추가 분리) | 0건 |
| 8 | `pre-commit install` 의무화 (추가 분리) | 0건 |
| 9 | 실 hook 구현 | 0건 |
| 10 | Phase α-1 / α-2 / α-3 / α-4 자동 실 진입 | 0건 |
| 11 | Phase β / γ 자동 진입 | 0건 |
| 12 | Layer C 재발효 / Layer D 재선언 | 0건 |
| 13 | MVP-1 PASS (Layer D) 재선언 | 0건 |
| 14 | 9 evidence 파일 재생성 | 0건 |
| 15 | 4 prerequisite actual run 자동 재실행 | 0건 |
| 16 | 신규 actual run 자동 trigger | 0건 |
| 17 | R-4 + R-5 + R-7 + R-1 합산 2785줄 어느 줄도 변경 | 0건 |
| 18 | R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 | 0건 |
| 19 | `.importlinter` forbidden 4 / `include_external_packages` / `root_packages` / `ignore_imports` / 각주 1 변경 | 0건 |
| 20 | R-7 docker-compose secret block / image layer check / restart recovery 변경 | 0건 |
| 21 | PC-4 / AR-2 / AR-3 진입 | 0건 |
| 22 | ST-1 / ST-2 / ST-4 / ST-5 진입 | 0건 |
| 23 | S-2 gitleaks 진입 | 0건 |
| 24 | Stage 5 (G3-7 4 항목) 진입 | 0건 |
| 25 | `pull_request_target` workflow 도입 | 0건 |
| 26 | commit signing 도입 | 0건 |
| 27 | GitHub Actions secrets 사용 도입 | 0건 (F-금지 #1 영구 답습) |
| 28 | Hermes upstream Dockerfile 변경 | 0건 |
| 29 | Production `docker-compose.yml` 변경 | 0건 |
| 30 | 실 secret material commit | 0건 |
| 31 | Tier-2 / Tier-3 catalog 확장 | 0건 |
| 32 | threshold *고정* | 0건 |
| 33 | Rollback Trigger / TR-1 ~ TR-5 발화 | 0건 |
| 34 | Group α 14 결정 영역 *재결정* | 0건 |
| 35 | C-1 ~ C-12 (Group α) / C-α-1 ~ C-α-11 (Backlog #6) / C-β-1 ~ C-β-15 (Phase α-1) / C-γ-1 ~ C-γ-26 (Phase α-2) / C-δ-1 ~ C-δ-28 (Phase α-3) / C-ε-1 ~ C-ε-29 (Phase α-4) / C-ι-1 ~ C-ι-30 (Layer C) / C-λ-1 ~ C-λ-25 (Layer D) 자동 변경 | 0건 (합산 **156 조건** 답습 보존) |
| 36 | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1 ~ α-4 합의 / Stage 2 합의 / Stage 4 합의 본문 변경 | 0건 |
| 37 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 38 | Group I (Hermes-originated commit auto-reject) 자동 진입 | 0건 |
| 39 | token rotation 정책 자동 결정 | 0건 |
| 40 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 41 | event enum 정식 등록 | 0건 |
| 42 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 43 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 44 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 45 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 46 | git commit / push | 0건 |
| 47 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습) | 0건 |
| 48 | 외부 LLM 응답 결론 강제 채택 | 0건 |
| 49 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 50 | 인간 리뷰 의무 자동 발화 | 0건 |
| 51 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |
| 52 | Layer 2 runtime block (G5-5) 진입 | 0건 |
| 53 | 의미적 lock-in 검사 진입 | 0건 |
| 54 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 55 | MVP-2 ~ MVP-6 본문 deepening | 0건 |

### 7.2 본 brief 발효 *후* 통합 실 진입 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | 통합 실 진입 시 9 sub-수단 외 수단 도입 (gitleaks / detect-secrets / trufflehog 등) | Backlog #1 1.5차 보강 영역 분리 |
| 2 | 통합 실 진입 시 R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 catalog 변경 | Backlog #3 별도 합의 영역 |
| 3 | 통합 실 진입 시 `.importlinter` forbidden / facade allow / google.generativeai 흡수 / URL 흡수 | Group A 2차 합의 답습 + TR-1 ~ TR-5 발화 시 별도 재합의 |
| 4 | 통합 실 진입 시 R-7 docker secret 본문 *재설계* | GP-3 Stage 2 합의 답습 + 실 사용자 명시 결정 영역 |
| 5 | 통합 실 진입 시 sub-step 4.3 (PC-4) / 4.4 (AR-2) 진입 | Backlog #1 + #2 + #3 분리 영구 답습 |
| 6 | 통합 실 진입 시 `src/adapters/llm/facade.py` real 본문 작성 | Backlog #4 영역 분리 (Layer D C-8 답습) |
| 7 | 통합 실 진입 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 + ADR-008 §2.6.2 R2-1 영구 답습 |
| 8 | 통합 실 진입 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 |
| 9 | 통합 실 진입 시 event enum 정식 등록 (`event:` field) | Backlog #5 ADR-012 §2.2 분리 |
| 10 | 통합 실 진입 시 `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 11 | 통합 실 진입 시 local pre-commit framework 활성화 | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 5 금지 추가 분리 #8 답습) |
| 12 | 통합 실 진입 시 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 13 | 통합 실 진입 시 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 14 | 통합 실 진입 시 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 15 | 통합 실 진입 시 실 secret 본문 commit | 영구 금지 (R-4.1 + Group D §1.2 #1 답습) |
| 16 | 통합 실 진입 시 F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 17 | 통합 실 진입 시 Operational Readiness PASS 자동 발효 (Layer E) | 사용자 명시 5 금지 #4 영구 답습 + MVP-6 영역 분리 |
| 18 | 통합 실 진입 시 Hermes PMO 격상 자동 발효 (Layer F) | 사용자 명시 5 금지 #5 영구 답습 + ADR-008 부록 C 12 조건 영역 분리 |
| 19 | 통합 실 진입 시 Phase β / γ 자동 진입 | Phase α 4 단계 = 사용자 명시 결정 영역 + Backlog #6 실 진입 영역 |
| 20 | 통합 실 진입 시 Group I (Hermes-originated commit auto-reject) 자동 진입 | Group α 합의 C-2 답습 (Group I 별도 합의 영역) |
| 21 | 통합 실 진입 시 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |
| 22 | 통합 실 진입 시 GitHub plan / ruleset 가용성 자동 확인 | Group α 합의 C-4 답습 |
| 23 | 통합 실 진입 시 Layer C 자동 재발효 | Layer C 발효 = `eb01bc4` 답습 한정 (재발효 0건) |
| 24 | 통합 실 진입 시 Layer D 자동 재선언 | Layer D 권위 = `210c98f` 답습 한정 (후속 18 합의 답습) |
| 25 | 통합 실 진입 시 9 evidence 파일 자동 재생성 | Layer C 발효 시점 evidence 답습 한정 |
| 26 | 통합 실 진입 시 4 prerequisite actual run 자동 재실행 | run_id 답습 한정 (재실행 0건) |
| 27 | 통합 실 진입 시 신규 actual run 자동 trigger | 사용자 명시 결정 영역 |
| 28 | 통합 실 진입 시 합의 형태 / cycle 옵션 / step 분할 자동 결정 | 사용자 명시 결정 영역 (옵션 (i) ~ (iii) 권고 한정) |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 통합 실 진입 단계에서 위 28 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격** | Layer C 발효 답습 + Layer D 권위 답습 + Phase α-1 ~ α-4 합의 답습 + 5 금지 영역 *재결정* 0건 + 본 brief = 통합 *단계 분할 정리 한정* (적격성 *해소* 0건) + 8/8 풀 3+1 트리거 0건 발화 (§5.3) |
| Phase α-1 ~ α-4 통합 실 진입 시 합의 | **별도 합의 — cycle 옵션 (i)/(ii)/(iii) 中 사용자 결정 영역** | (i) 1순위 병렬 — 2순위 의존 cycle / (ii) 단일 cycle / (iii) 4 Phase 각각 독립 cycle — 각각 합의 형태 별도 결정 영역 |
| 통합 실 진입 후 Layer C 답습 재확인 합의 | **별도 합의 — Reviewer-only 단축 또는 풀 3+1** | Layer C 발효 = `eb01bc4` 답습 한정 (재발효 0건) — 답습 재확인 한정 |
| 통합 실 진입 후 Layer D satisfaction 갱신 합의 | **별도 합의 — C-5b / C-5c / C-6 / C-7 / C-8 satisfaction 갱신 영역 (사용자 명시 결정 영역)** | Layer D 본문 변경 0건 + satisfaction 갱신 = 별도 후속 합의 영역 (Layer D 재진입 가능성 검토 후속 18 답습) |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

§5.3 답습 — **8/8 트리거 0건 발화** 확정.

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 / 실 cycle 옵션 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-16-phase-alpha-integrated-implementation-plan.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α-1 통합 실 진입 step 분할 brief 작성** (R-4 829줄 한정 cycle) | Phase α-1 단독 실 진입 brief (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Phase α-1 + α-2 + α-3 1순위 병렬 진입 step 분할 brief 작성** | 1순위 병렬 진입 brief (cycle 옵션 (i) 답습) |
| (F) | 본 brief 승인 → **Phase α-4 R-1 단독 실 진입 step 분할 brief 작성** (1순위 prerequisite actual run PASS 선행 evidence 답습 후) | Phase α-4 단독 실 진입 brief |
| (G) | 본 brief 승인 → **Phase α 4 단계 단일 cycle 통합 실 진입 brief 작성** (cycle 옵션 (ii)) | 4 Phase 단일 cycle 진입 brief |
| (H) | 본 brief 승인 → **Phase α 4 단계 4 cycle 분리 진입 brief 작성** (cycle 옵션 (iii)) | 4 Phase 4 cycle 분리 진입 brief |
| (I) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 (C-5b ST-1 / C-5c PC-4 T3 / C-6 잔여 sub-수단 / C-7 T3 / C-8 facade 등) |
| (J) | 본 brief 보류 → Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief | Group α C-2 답습 |
| (K) | 본 brief 보류 → token rotation 정책 별도 합의 진입 brief | Group α C-3 답습 |
| (L) | 본 brief 보류 → GitHub plan / ruleset 가용성 확인 단계 진입 brief | Group α C-4 답습 |
| (M) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (N) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α-1 단독 실 진입 step 분할 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Phase α-1 + α-2 + α-3 1순위 병렬 진입 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Phase α-4 단독 실 진입 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Phase α 4 단계 단일 cycle 통합 실 진입 brief 작성."
- (H): "옵션 (H) 로 진행해주세요. Phase α 4 단계 4 cycle 분리 진입 brief 작성."
- (I): "옵션 (I) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (J) ~ (L): "옵션 (X) 로 진행해주세요. 별도 합의 brief 작성."
- (M): "옵션 (M) 으로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (N): "옵션 (N) 으로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — Phase α-1 ~ α-4 통합 실제 구현 계획 brief — 단계 분할 정리 한정) |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — 실제 파일 수정 0건 / CI workflow 변경 0건 / runtime code 변경 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| 추가 분리 영역 답습 (사용자 명시 5 금지 외) | ✅ (24/24 — branch protection / dev 환경 강제 / `pre-commit install` 의무화 / 실 hook 구현 / PC-4 / AR-2 / AR-3 / ST-1 / ST-2 / ST-4 / ST-5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 모두 분리) |
| Layer C 발효 답습 (`eb01bc4`) | ✅ (재발효 0건 + evidence 재생성 0건 + actual run 재실행 0건 + 30 조건 C-ι-1 ~ C-ι-30 변경 0건) |
| Layer D 권위 답습 (`210c98f` + 후속 18) | ✅ (재선언 0건 + 본문 변경 0건 + C-1 ~ C-8 satisfaction 자동 변경 0건 + 25 조건 C-λ-1 ~ C-λ-25 변경 0건) |
| Phase α-1 ~ α-4 합의 답습 | ✅ (C-β-1 ~ C-β-15 + C-γ-1 ~ C-γ-26 + C-δ-1 ~ C-δ-28 + C-ε-1 ~ C-ε-29 합산 98 조건 변경 0건) |
| Group α 합의 답습 (`4880e88`) | ✅ (C-1 ~ C-12 답습 — 자동 해소 0건 + 자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Backlog #6 우선 진입 합의 답습 (`c7ddfdd`) | ✅ (C-α-1 ~ C-α-11 11 조건 변경 0건 + 1순위 병렬 + 2순위 의존 토폴로지 답습) |
| Layer A / Layer B / §5.5 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 + TR-1 ~ TR-5 답습 | ✅ (발화 0건 — §6 답습) |
| Group α 7 단계 승격 Trigger 답습 | ✅ (발화 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (4 Phase = enforcement / config / docker secret / workflow 영역 = catalog / provider 영역과 직교) |
| F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) | ✅ (영구 보존) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/8 발화 | ✅ (§5.3 답습) |
| 통합 진입 적격성 5/5 충족 | ✅ (§5.1 답습 — C-π-1 ~ C-π-5) |
| 의존성 의무 검토 통과 | ✅ (§5.2 답습 — 4 prerequisite actual run PASS 답습 完) |
| 합산 2785줄 본문 변경 0건 | ✅ (R-4 829 + R-5 35 + R-7 328 + R-1 1593 답습 100% 보존) |
| `src/` 본문 변경 0건 | ✅ (facade.py 41줄 placeholder 답습 보존) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| 합의 조건 합산 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 29 + Layer C 30 + Layer D 25 = **합산 176 조건 + ADR-011 §2.1 모법 변경 0건**) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Layer C 발효 (`eb01bc4` 2026-05-16 — MVP-1 Implementation Evidence PASS + GP-3 + GP-5 PASS 실 발효, 30 조건 C-ι-1 ~ C-ι-30) + Layer D 권위 답습 (`210c98f` 2026-05-13 + 후속 18 재진입 가능성 검토 APPROVE AS BRIEF, 25 조건 C-λ-1 ~ C-λ-25) 후속**, Phase α 4 단계 (α-1 R-4 도구 본문 / α-2 R-5 `.importlinter` / α-3 R-7 docker secret block / α-4 R-1 CI workflow 통합) 의 **통합 실제 구현 *단계 분할 정리 한정* 준비안 (DRAFT)** 이다. **사용자 명시 5 금지** (실제 파일 수정 / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습 + **추가 24 분리 영역** (branch protection / dev 환경 강제 / `pre-commit install` 의무화 / PC-4 / AR-2 / AR-3 / ST-1 / ST-2 / ST-4 / ST-5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 등) 24/24 분리 명시. **4 영역 본문 합산 매트릭스** = R-4 829 + R-5 35 + R-7 328 + R-1 1593 = **합산 2785줄 답습 보존** (4 Phase 6 sub-수단 = S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1, Layer B §5.5 9 sub-수단 中 3 sub-수단 PC-4 + AR-2 + AR-3 = 본 brief 영역 외 분리 명시) + **의존성 토폴로지** (1순위 병렬 α-1+α-2+α-3 + 2순위 의존 α-4 = Stage 4 = Stage 1 + Stage 3 actual run PASS 선행 evidence 의무) + **통합 실제 구현 단계 분할 매트릭스** (Phase α-1 11 sub-step + Phase α-2 6 항목 + Phase α-3 4 sub-step + Phase α-4 4 sub-step — 단, 4.3 PC-4 + 4.4 AR-2 = 분리 명시) + **통합 cycle 패턴** (옵션 (i) 1순위 병렬 — 2순위 의존 / 옵션 (ii) 단일 cycle / 옵션 (iii) 4 cycle 분리 — 모두 권고 한정, 사용자 명시 결정 영역) + **actual run 답습 매트릭스** (4/4 PASS — `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정, 재실행 0건) + **5 금지 × 4 Phase 분리 매트릭스** (5/5 분리 — 충돌 0) + **통합 실제 구현 진입 적격성 5 조건 검토** (C-π-1 5 금지 충돌 0/5 + C-π-2 Layer C evidence 답습 100% 보존 + C-π-3 Layer D 권위 답습 100% 보존 + C-π-4 Provider Liquidity 5-way 100% 보존 + C-π-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **의존성 의무 검토 통과** (4 prerequisite actual run PASS 답습 100% 答) + **8 풀 3+1 승격 트리거 0/8 발화** + **4 Phase 영역 영향 Rollback Trigger 의존성 답습** (18+5 trigger 中 4 Phase 직접 영향 10 + 간접 영향 3 + 영향 0 7 + TR-1~TR-5 5 — 발화 0건 + threshold 후보 한정 유지) + **본 brief 자체 금지 55 + 통합 실 진입 단계 금지 28** + **합의 형태 권고** (Reviewer-only 단축 — 8/8 트리거 0건 발화) 를 정리한다. **본 brief 는 Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않으며, 합산 2785줄 본문 어느 줄도 *변경* 하지 않으며, `src/` 본문 어느 줄도 *변경* 하지 않으며, 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 176 합의 조건 어느 것도 *변경* / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / cycle 옵션 *결정* / 합의 형태 *결정* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~N, §9 답습).

---

**작성일**: 2026-05-16
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~N, §9 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **실제 파일 수정** (사용자 명시 5 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 5 금지 #2)
- ❌ **runtime code 변경** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ branch protection 변경 (추가 분리)
- ❌ dev 환경 강제 (추가 분리)
- ❌ `pre-commit install` 의무화 (추가 분리)
- ❌ 실 hook 구현
- ❌ Phase α-1 / α-2 / α-3 / α-4 자동 실 진입
- ❌ Phase β / γ 자동 진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ 9 evidence 파일 재생성 / 4 prerequisite actual run 재실행
- ❌ R-4 + R-5 + R-7 + R-1 합산 2785줄 어느 줄도 변경
- ❌ `src/` 본문 변경 / `facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1 / ST-2 / ST-4 / ST-5 / S-2 진입
- ❌ Stage 5 (G3-7 4 항목) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 자동 발화
- ❌ 합산 176 합의 조건 (Group α 12 + Backlog #6 11 + Phase α-1~α-4 98 + Layer C 30 + Layer D 25) 자동 변경
- ❌ Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1~α-4 / Stage 2 / Stage 4 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile 변경
- ❌ Production `docker-compose.yml` 신설 / 변경
- ❌ 실 secret material commit
- ❌ event enum 정식 등록
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ Layer 2 runtime block (G5-5) 진입
- ❌ 의미적 lock-in 검사 진입
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출 (Group α 합의 C-11 답습)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
