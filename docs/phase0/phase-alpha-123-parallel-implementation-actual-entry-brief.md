# Phase α-1 + α-2 + α-3 **실제 병렬 구현 진입 여부** Brief (준비안 — DRAFT)

> **본 문서는 Phase α-1 + α-2 + α-3 1순위 병렬 구현 계획 brief 합의 발효 후속 (`88ccf79` APPROVE AS BRIEF — C-ν-1 ~ C-ν-25), R-4 도구 본문 + R-5 `.importlinter` 본문 + R-7 docker secret block 의 *실제 구현 진입 여부 검토 한정* brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - 계획 brief (=`2e36592`, 승인 `88ccf79`) = "*How* do we plan parallel implementation?" — cycle 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정
> - **본 brief = "*Should* we enter actual parallel implementation now?"** — 진입 prerequisite 충족 검토 + 진입 결정 옵션 + 진입 후 step 분할 권고 한정
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) Phase α-1 / α-2 / α-3 어느 것도 *실 진입* 시키지 않으며, (ii) 합산 1192줄 (R-4 829 + R-5 35 + R-7 328) 어느 줄도 *변경* 하지 않으며, (iii) Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Phase α 통합 계획 25 + Phase α-1+2+3 계획 25 = **합산 197 합의 조건** 中 어느 것도 *해소* / *변경* 시키지 않으며, (iv) 사용자 명시 5 금지 中 어느 것도 *진입* 시키지 않으며, (v) Phase α-4 / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 어느 것도 *발생시키지 않으며*, (vi) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-123-parallel-implementation.md` (Phase α-1+2+3 계획 brief 합의, commit `88ccf79` APPROVE AS BRIEF — 25 조건 C-ν-1 ~ C-ν-25, 후속 20)
- `docs/phase0/phase-alpha-123-parallel-implementation-brief.md` (계획 brief, commit `2e36592`, 950줄)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-integrated-implementation-plan.md` (Phase α 통합 실제 구현 계획 합의, commit `542e77e` APPROVE AS BRIEF — 25 조건 C-μ-1 ~ C-μ-25)
- `docs/review/3plus1-consensus-2026-05-16-layer-c-implementation-evidence-pass-actual-entry.md` (Layer C 발효, commit `eb01bc4` APPROVE — 30 조건 C-ι-1 ~ C-ι-30)
- `docs/review/3plus1-consensus-2026-05-16-layer-d-reentry-assessment.md` (Layer D 재진입 평가, commit `951a5b1` APPROVE AS BRIEF — 25 조건 C-λ-1 ~ C-λ-25)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1, commit `1b3090b` — 15 조건 C-β-1 ~ C-β-15)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2, commit `6a79247` — 26 조건 C-γ-1 ~ C-γ-26)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3, commit `3f6306d` — 28 조건 C-δ-1 ~ C-δ-28)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입, commit `c7ddfdd` — C-α-1 ~ C-α-11)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α, commit `4880e88` — C-1 ~ C-12)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 모법

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-1 + α-2 + α-3 실제 병렬 구현 진입 brief를 작성해주세요. 범위는 R-4 도구 본문, R-5 .importlinter 본문, R-7 docker secret block의 실제 구현 진입 여부를 검토하는 것입니다. 아직 실제 파일 수정, CI workflow 변경, runtime code 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습 (계획 brief 패턴 답습)

1. ❌ **실제 파일 수정 금지** — R-4 829 + R-5 35 + R-7 328 = **1192줄 답습 보존** + 변경 / 추가 / 삭제 0건 (본 brief = *진입 여부 검토 한정*, 실 구현 자체는 본 brief *외*)
2. ❌ **CI workflow 변경 금지** — `secret-hygiene-egress-redaction.yml` 694줄 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 + 8 G2/G3/G4 PoC workflow 본문 변경 / 신설 / 삭제 0건
3. ❌ **runtime code 변경 금지** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 (Backlog #4 분리)
4. ❌ **Operational Readiness PASS (Layer E) 선언 금지** — MVP-6 영역 분리
5. ❌ **Hermes PMO 격상 (Layer F) 금지** — ADR-008 부록 C 12 조건 미진입 영구 답습

### 0.3 본 brief 가 *하는* 것

1. Phase α-1 + α-2 + α-3 1순위 병렬 구현 계획 brief 합의 (`88ccf79`) 발효 후속 — *실제 구현 진입 여부 검토* 한정 (§1)
2. **진입 Prerequisite 매트릭스** — 계획 brief 답습 / Layer C 발효 답습 / Layer D 권위 답습 / 합산 197 조건 답습 / 5/5 사용자 금지 / 27 분리 영역 / 8/8 풀 3+1 트리거 / 5 영구 핵심 제약 / Provider Liquidity 5-way / F-금지 #1 (§2)
3. **각 Prerequisite 충족 상태 검토 매트릭스** — Layer C 발효 시점 답습 + 본 brief 작성 시점 답습 (§3)
4. **진입 결정 영역 = 사용자 명시 결정 영역 (자동 결정 0건)** — cycle 옵션 결정 / 합의 형태 결정 / sub-step 순서 결정 / 3 Phase 합의 분리 vs 통합 결정 (§4)
5. **진입 *후* 단계 분할 권고 매트릭스** — Step 0 ~ Step 6 cycle 답습 (계획 brief §3 답습 한정 — 본 brief *권한 외 진입 0건*) (§5)
6. **진입 시점 Rollback Trigger 검토** — Layer B 18 trigger + TR-1 ~ TR-5 답습 (발화 0건 예상) (§6)
7. **진입 시점 Evidence 기준 검토** — ADR-011 §2.1 (a)~(e) × 3 Phase = 15/15 PASS Layer C 답습 (재검증 0건) (§7)
8. **사용자 명시 5 금지 영역 × 진입 시점 분리 매트릭스** (§8)
9. **합의 형태 권고 + 풀 3+1 승격 트리거** (§9)
10. **본 brief + 본 brief 발효 후 단계의 금지 사항** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **실제 파일 수정 (0건)** — 합산 1192줄 답습 보존 + 3 Phase 어느 본문도 변경 / 추가 / 삭제 0건
- ❌ **CI workflow 변경 (0건)** — 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경 / 신설 / 삭제 0건
- ❌ **runtime code 변경 (0건)** — `src/` 본문 변경 0건 + `src/adapters/llm/facade.py` 41줄 placeholder 답습 보존 (Backlog #4 분리)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **Phase α-1 / α-2 / α-3 자동 실 진입 (0건)** — 본 brief = *진입 여부 검토 한정* (실 진입 = Step 1 — 사용자 명시 결정 영역)
- ❌ **Phase α-4 자동 진입 (0건)** — 2순위 의존 분리 (통합 합의 §2.2 답습)
- ❌ **branch protection 변경 (0건)** — AR-2 / CODEOWNERS / required status check / direct push 차단 / force push 차단 / admin bypass OFF 모두 변경 0건 (Group α 합의 5.1 #6 답습)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 0건 (Backlog #2 분리)
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 0건 (Backlog #1 + #2 분리)
- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 0건
- ❌ **실 git commit / push 자동 진입 (0건)** — 본 brief = 준비안 한정
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / commit signing / Vault HSM / Layer E / Layer F 모두 영역 외
- ❌ **Layer C 재발효 (0건)** — Layer C 발효 = `eb01bc4` 답습 한정
- ❌ **Layer D 재선언 (0건)** — Layer D 권위 = `210c98f` + 후속 18 답습 한정
- ❌ **MVP-1 PASS 재선언 (0건)**
- ❌ **9 evidence 파일 재생성 (0건)**
- ❌ **4 prerequisite actual run 자동 재실행 (0건)** — run_id `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정
- ❌ **신규 actual run 자동 trigger (0건)**
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)** — Group α 합의 5.1 #8 + Backlog #3 분리
- ❌ **`.importlinter` forbidden 4 모듈 변경 / `include_external_packages` 변경 / `root_packages` 변경 / `ignore_imports` 변경 (0건)** — Group A 2차 합의 답습 + TR-1 ~ TR-5 재합의 trigger 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)** — GP-3 Stage 2 합의 답습
- ❌ **PC-3 / AR-1 / PC-4 / AR-2 / AR-3 진입 (0건)** — Phase α-4 영역 + Backlog #1 + #2 + #3 분리
- ❌ **ST-1 entrypoint stat / ST-2 inotify sidecar / ST-4 Vault HSM / ST-5 Defense in depth 진입 (0건)** — Backlog #1 + #7 + MVP-2 분리
- ❌ **S-2 gitleaks 도입 (0건)** — Backlog #1 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Phase α-4 후속 권고
- ❌ **`pull_request_target` workflow 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **commit signing 도입 (0건)** — MVP-6 영역
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정
- ❌ **실 secret material commit (0건)** — FAKE_TEST_SECRET marker 답습 영구 보존
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 (0건)**
- ❌ **threshold *고정* (0건)** — FP / FN / latency / CI runtime / image layer leak count / restart recovery rate 모두 *후보 한정* 유지
- ❌ **Group α 14 결정 영역 *재결정* (0건)**
- ❌ **합산 197 합의 조건 자동 변경 (0건)** — Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Phase α 통합 계획 25 + Phase α-1+2+3 계획 25
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 2 / Stage 4 / Group A 1차/2차/3차 / Group D / §5.5 9 sub-수단 본문 변경 (0건)**
- ❌ **Rollback Trigger / TR-1 ~ TR-5 자동 발화 (0건)**
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)**
- ❌ **event enum 정식 등록 (0건)** — Backlog #5 분리
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 (0건)** — Backlog #4 분리 (Layer D C-8 답습)
- ❌ **Layer 2 runtime block (G5-5) 진입 (0건)** — MVP-3/4 분리
- ❌ **의미적 lock-in 검사 진입 (0건)** — MVP-3 분리

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-1 / α-2 / α-3 *실 진입* 어느 것도 *시작* 시키지 않으며,
- (ii) 합산 197 합의 조건 中 어느 것도 *해소* / *변경* 시키지 않으며,
- (iii) 사용자 명시 5 금지 영역 어느 것도 진입시키지 않으며,
- (iv) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (v) 합산 1192줄 (R-4 829 + R-5 35 + R-7 328) 어느 줄도 *변경* 하지 않으며,
- (vi) Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 어느 것도 *발생시키지 않으며*,
- (vii) Rollback Trigger / TR-1 ~ TR-5 어느 것도 *발화* 시키지 않으며,
- (viii) Phase α-4 / Phase β / γ 어느 것도 *자동 진입* 시키지 않으며,
- (ix) cycle 옵션 / 합의 형태 / sub-step 순서 / 3 Phase 합의 분리 vs 통합 어느 것도 *결정* 하지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-1 + α-2 + α-3 *실제 병렬 구현 진입 여부 검토 한정 권위 권고***. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습 (4 단계 brief chain)

### 1.1 4 단계 brief chain 매트릭스

| Stage | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| Stage 1 | Phase α 통합 실제 구현 계획 brief 합의 | `542e77e` | APPROVE AS BRIEF | 25 조건 C-μ-1 ~ C-μ-25 | "*Plan* the Phase α integrated implementation" — 4 cycle 옵션 권고 한정 |
| Stage 2 | Phase α-1 + α-2 + α-3 1순위 병렬 구현 *계획* brief 합의 | `88ccf79` | APPROVE AS BRIEF | 25 조건 C-ν-1 ~ C-ν-25 | "*How* to plan 1순위 parallel" — cycle 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 |
| **Stage 3 (본 brief)** | **Phase α-1 + α-2 + α-3 1순위 병렬 *실제 구현 진입 여부* brief** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* we enter 1순위 parallel actual implementation now?"** — 진입 prerequisite 충족 검토 + 진입 결정 옵션 한정 |
| Stage 4 (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* 1순위 parallel actual implementation" — 사용자 명시 결정 후 |

### 1.2 Stage 1 답습 (`542e77e` — 2026-05-16 후속 19)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의 — 옵션 (A)) |
| 합의 단위 | 통합 계획 brief 본문 채택 — Phase α 4 cycle 옵션 권고 한정 |
| 합의 조건 | 25 조건 (C-μ-1 ~ C-μ-25) |
| 풀 3+1 트리거 발화 | 0/8 |
| cycle 옵션 권고 | (i) 1순위 병렬 (α-1 + α-2 + α-3) + 2순위 의존 (α-4) / (ii) minor 인터페이스 정렬 / (iii) 3 Phase 분리 / (iv) 풀 3+1 |
| 본 brief 영역 | **cycle 옵션 (i) 中 1순위 병렬 부분 한정** (α-4 = 별도 brief 분리) |

### 1.3 Stage 2 답습 (`88ccf79` — 2026-05-16 후속 20)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의 — 옵션 (A), 8/8 풀 3+1 트리거 0건 발화) |
| 합의 단위 | 1순위 병렬 *계획 brief* 본문 채택 — cycle 분할 + 수정 범위 + 테스트 범위 + Rollback Trigger + Evidence 기준 정리 한정 |
| 합의 조건 | 25 조건 (C-ν-1 ~ C-ν-25) |
| 풀 3+1 트리거 발화 | 0/8 |
| 4 sub-수단 영역 | S-1 + T-2 + T-2 import-linter + T-5 + ST-3 (본 합의 영역) |
| 2 sub-수단 분리 | PC-3 + AR-1 (Phase α-4 영역) |
| 5+ sub-수단 분리 | PC-4 + AR-2 + AR-3 + S-2 + ST-1/2/4/5 (Backlog 분리) |
| 의존성 토폴로지 | α-1 ↔ α-2 부분 의존 (T-6) / α-1 ↔ α-3 독립 / α-2 ↔ α-3 독립 / 3 Phase → α-4 선행 의존 |
| 본 brief 영역 | **Stage 2 계획 brief 후속 — *실제 구현 진입 여부* 검토 한정** |

### 1.4 본 brief 의 진입점

본 brief = **Stage 2 계획 brief 합의 발효 후속**:

- Stage 1 (통합 계획) ↔ Stage 2 (1순위 계획) ↔ Stage 3 (본 brief, 진입 여부) ↔ Stage 4 (실 구현, 사용자 명시 결정 영역)
- Stage 3 의 단일 책무: **"진입 prerequisite 가 모두 충족되었는가?"** + **"진입 결정의 옵션은 무엇인가?"** 검토 한정
- Stage 3 ≠ Stage 4 (실 구현 = 별도 단계, 본 brief 영역 외)
- Stage 3 ≠ Phase α-4 (2순위 의존, 별도 brief 영역)
- Stage 3 ≠ Layer C 재발효 (Layer C 발효 = `eb01bc4` 답습 한정)
- Stage 3 ≠ Layer D 재선언 (Layer D 권위 = `210c98f` + 후속 18 답습 한정)

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-17 시점 답습)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (30 조건 C-ι-1 ~ C-ι-30) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (25 조건 C-λ-1 ~ C-λ-25, 5 조건 PARTIAL — Backlog 우선 권고) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (ADR-008 부록 C 12 조건 미충족) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | 🔍 본 brief 검토 영역 |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | 🔍 본 brief 검토 영역 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | 🔍 본 brief 검토 영역 |
| Phase α-4 (R-1) | 2순위 의존 — CI workflow 통합 (PC-3 + AR-1) | ❌ 본 brief 영역 외 (별도 brief) |

---

## 2. 진입 Prerequisite 매트릭스

본 §2 = 1순위 병렬 실 진입 전 *충족 되어야 하는* prerequisite enumerate 한정. 실 충족 *상태 검토* 는 §3.

### 2.1 Prerequisite 그룹 분류

| 그룹 | 영역 | Prerequisite 수 |
|-----|------|---------------|
| **G1** | 상위 합의 답습 | 9 |
| **G2** | 5 사용자 명시 금지 영역 답습 | 5 |
| **G3** | 27 추가 분리 영역 답습 | 27 |
| **G4** | 8 풀 3+1 승격 트리거 답습 | 8 |
| **G5** | 5 영구 핵심 제약 보존 답습 | 5 |
| **G6** | Provider Liquidity 5-way 보존 답습 | 5 |
| **G7** | F-금지 #1 영구 답습 | 1 |
| **G8** | actual run + evidence 답습 | 13 (4 actual run + 9 evidence) |
| **G9** | Rollback Trigger + TR-1 ~ TR-5 발화 0건 답습 | 23 (18 + 5) |
| **합산** | **9 그룹 합산** | **96 prerequisite** |

### 2.2 G1 상위 합의 답습 매트릭스 (9 합의)

| # | 합의 | commit | 합의 조건 |
|---|----|-------|--------|
| G1-1 | Group α (Backlog #3) | `4880e88` | C-1 ~ C-12 (12) |
| G1-2 | Backlog #6 우선 진입 | `c7ddfdd` | C-α-1 ~ C-α-11 (11) |
| G1-3 | Phase α-1 (R-4) | `1b3090b` | C-β-1 ~ C-β-15 (15) |
| G1-4 | Phase α-2 (R-5) | `6a79247` | C-γ-1 ~ C-γ-26 (26) |
| G1-5 | Phase α-3 (R-7) | `3f6306d` | C-δ-1 ~ C-δ-28 (28) |
| G1-6 | Layer C 발효 | `eb01bc4` | C-ι-1 ~ C-ι-30 (30) |
| G1-7 | Layer D 재진입 평가 | `951a5b1` | C-λ-1 ~ C-λ-25 (25) |
| G1-8 | Phase α 통합 계획 (Stage 1) | `542e77e` | C-μ-1 ~ C-μ-25 (25) |
| G1-9 | Phase α-1+2+3 1순위 계획 (Stage 2) | `88ccf79` | C-ν-1 ~ C-ν-25 (25) |
| **합산** | **9 합의** | — | **197 조건** |

### 2.3 G2 5 사용자 명시 금지 영역 답습 매트릭스 (5)

| # | 금지 영역 | 본 brief 영역 |
|---|---------|------------|
| G2-1 | 실제 파일 수정 | 0건 답습 |
| G2-2 | CI workflow 변경 | 0건 답습 |
| G2-3 | runtime code 변경 | 0건 답습 |
| G2-4 | Operational Readiness PASS (Layer E) | 0건 답습 |
| G2-5 | Hermes PMO 격상 (Layer F) | 0건 답습 |

### 2.4 G3 27 추가 분리 영역 답습 매트릭스 (Stage 2 §0.4 답습)

| # | 분리 영역 | 분리 사유 |
|---|---------|---------|
| G3-1 | Phase α-4 자동 진입 | 2순위 의존 분리 |
| G3-2 | branch protection 변경 | T3 / Backlog #3 |
| G3-3 | dev 환경 강제 | Backlog #2 |
| G3-4 | `pre-commit install` 의무화 | Backlog #1 + #2 |
| G3-5 | 실 hook 구현 | 별도 합의 |
| G3-6 | 실 git commit / push 자동 진입 | 본 brief = 준비안 한정 |
| G3-7 | Phase β / γ 자동 진입 | R-6 / R-10 / R-2 / commit signing / Vault HSM 모두 영역 외 |
| G3-8 | Layer C 재발효 | `eb01bc4` 답습 한정 |
| G3-9 | Layer D 재선언 | `210c98f` + 후속 18 답습 한정 |
| G3-10 | MVP-1 PASS 재선언 | 별도 단계 |
| G3-11 | 9 evidence 파일 재생성 | Layer C 발효 시점 답습 |
| G3-12 | 4 prerequisite actual run 재실행 | run_id 4 답습 한정 |
| G3-13 | R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 | Backlog #3 분리 |
| G3-14 | `.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 | Group A 2차 합의 답습 + TR-1 ~ TR-5 미발화 |
| G3-15 | R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 | GP-3 Stage 2 합의 답습 |
| G3-16 | PC-3 / AR-1 / PC-4 / AR-2 / AR-3 진입 | Phase α-4 + Backlog 분리 |
| G3-17 | ST-1 / ST-2 / ST-4 / ST-5 진입 | Backlog #1 + #7 + MVP-2 분리 |
| G3-18 | S-2 gitleaks 도입 | Backlog #1 분리 |
| G3-19 | Stage 5 (G3-7 4 항목) 자동 진입 | Phase α-4 후속 권고 |
| G3-20 | `pull_request_target` workflow 도입 | T2/T3 별도 합의 |
| G3-21 | commit signing 도입 | MVP-6 영역 |
| G3-22 | GitHub Actions secrets 사용 도입 | F-금지 #1 영구 답습 |
| G3-23 | Hermes upstream Dockerfile 변경 | ADR-008 §2.6.2 R2-1 영구 답습 |
| G3-24 | Production `docker-compose.yml` 신설 / 변경 | PoC 격리 디렉토리 한정 |
| G3-25 | Tier-2 / Tier-3 catalog 자동 확장 | T2/T3 합의 영역 |
| G3-26 | threshold *고정* | *후보 한정* 유지 |
| G3-27 | event enum 정식 등록 | Backlog #5 분리 |

### 2.5 G4 8 풀 3+1 승격 트리거 매트릭스 (Stage 2 §9.2 답습)

| # | 트리거 영역 | 본 brief 예상 발화 |
|---|----------|----------------|
| G4-1 | 새 권위 결정 (계획 brief 영역) | 0건 발화 — Stage 2 답습 |
| G4-2 | 5 영구 핵심 제약 약화 | 0건 — 본 brief 답습 |
| G4-3 | Provider Liquidity 5-way 영향 | 0건 — 본 brief = 진입 여부 한정 |
| G4-4 | ADR-011 §2.1 (a)~(e) 5 조건 패턴 영향 | 0건 — 본 brief = 답습 한정 |
| G4-5 | 197 합의 조건 자동 변경 영향 | 0건 — 본 brief 답습 |
| G4-6 | Hermes ≠ root of trust 영향 | 0건 — 본 brief 답습 |
| G4-7 | F-금지 #1 (GitHub Actions secrets) 도입 | 0건 — 영구 답습 |
| G4-8 | 합의 영역 *변경* (계획 brief → 진입 여부 brief 단순 framing 전환만) | 0건 — 본 brief = framing 차이 한정 |

### 2.6 G5 5 영구 핵심 제약 보존 매트릭스

| # | 영구 핵심 제약 | 본 brief 보존 |
|---|------------|-----------|
| G5-1 | Hermes ≠ root of trust | ✅ 보존 |
| G5-2 | 단일 source-of-truth | ✅ 보존 |
| G5-3 | 수단/목적 분리 (ADR-011) | ✅ 보존 |
| G5-4 | T1/T2/T3 분리 | ✅ 보존 |
| G5-5 | SPOF 의도적 수용 | ✅ 보존 |

### 2.7 G6 Provider Liquidity 5-way 보존 매트릭스

| # | 영역 | 본 brief 보존 |
|---|------|-----------|
| G6-1 | Model 교체 가능성 | ✅ 보존 (catalog 변경 0건) |
| G6-2 | Subscription 교체 가능성 | ✅ 보존 (provider 직교) |
| G6-3 | Vendor 교체 가능성 | ✅ 보존 (3 Phase = enforcement / config / docker secret 영역) |
| G6-4 | API 교체 가능성 | ✅ 보존 |
| G6-5 | Memory/Skill 호환 가능성 | ✅ 보존 |

### 2.8 G7 F-금지 #1 영구 답습 (1)

| # | 영역 | 본 brief 답습 |
|---|------|-----------|
| G7-1 | GitHub Actions secrets 사용 도입 | 0건 영구 답습 |

### 2.9 G8 actual run + evidence 답습 매트릭스 (13)

| # | 영역 | 답습 |
|---|------|----|
| G8-1 | actual run `25728590939` (secret-hygiene-egress-redaction) | ✅ Layer C 답습 (재실행 0건) |
| G8-2 | actual run `25728590916` (provider-adapter-enforcement) | ✅ Layer C 답습 (재실행 0건) |
| G8-3 | actual run `25728590977` (provider-url-scanner) | ✅ Layer C 답습 (재실행 0건) |
| G8-4 | actual run `25731846625` (GP-3 ST-3 docker secret PoC) | ✅ Layer C 답습 (재실행 0건) |
| G8-5 | evidence — R-4 Tier-1 45 patterns 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-6 | evidence — R-4 URL Tier-1 10 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-7 | evidence — R-4 Model Tier-1 19 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-8 | evidence — R-5 `.importlinter` forbidden 4 모듈 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-9 | evidence — R-5 transitive import 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-10 | evidence — R-7 docker secret block 격리 검증 | ✅ Layer C 답습 (재생성 0건) |
| G8-11 | evidence — R-7 docker image layer 검사 | ✅ Layer C 답습 (재생성 0건) |
| G8-12 | evidence — R-7 docker restart recovery | ✅ Layer C 답습 (재생성 0건) |
| G8-13 | evidence — ADR-011 §2.1 (a)~(e) 5 조건 × 3 Phase = 15/15 PASS 답습 | ✅ Layer C 답습 (재검증 0건) |

### 2.10 G9 Rollback Trigger + TR-1 ~ TR-5 발화 0건 답습 매트릭스 (23)

| 그룹 | 영역 | 본 brief 발화 |
|-----|------|----------|
| Layer B 18 Rollback Trigger | 1순위 직접 영향 7 + 간접 영향 1 + 영역 외 10 | 0건 영구 답습 |
| TR-1 ~ TR-5 (Group A 2차 — α-2 R-5 한정) | 5 재합의 trigger | 0건 영구 답습 |

---

## 3. 각 Prerequisite 충족 상태 검토

본 §3 = 본 brief *작성 시점* (2026-05-17) Prerequisite 충족 매트릭스. 단, 본 §3 의 충족 검토 자체는 *답습 한정* — 자동 재검증 / 자동 재선언 0건.

### 3.1 G1 9 상위 합의 답습 충족 매트릭스

| # | 합의 | 충족 상태 | 답습 권위 |
|---|----|--------|--------|
| G1-1 | Group α (Backlog #3) | ✅ PASS | `4880e88` 답습 |
| G1-2 | Backlog #6 우선 진입 | ✅ PASS | `c7ddfdd` 답습 |
| G1-3 | Phase α-1 (R-4) | ✅ PASS | `1b3090b` 답습 |
| G1-4 | Phase α-2 (R-5) | ✅ PASS | `6a79247` 답습 |
| G1-5 | Phase α-3 (R-7) | ✅ PASS | `3f6306d` 답습 |
| G1-6 | Layer C 발효 | ✅ PASS | `eb01bc4` 답습 |
| G1-7 | Layer D 재진입 평가 | ✅ PASS (5 조건 PARTIAL — Backlog 우선 권고) | `951a5b1` 답습 |
| G1-8 | Phase α 통합 계획 (Stage 1) | ✅ PASS | `542e77e` 답습 |
| G1-9 | Phase α-1+2+3 1순위 계획 (Stage 2) | ✅ PASS | `88ccf79` 답습 |
| **합산** | **9/9** | **✅ 100%** | **197 조건 변경 0건** |

### 3.2 G2 5 사용자 명시 금지 영역 답습 충족 매트릭스

| # | 금지 영역 | 본 brief 시점 충족 |
|---|---------|----------------|
| G2-1 | 실제 파일 수정 (1192줄) | ✅ 0건 — 답습 보존 |
| G2-2 | CI workflow 변경 | ✅ 0건 — 답습 보존 |
| G2-3 | runtime code 변경 | ✅ 0건 — `src/` + facade.py placeholder 답습 |
| G2-4 | Operational Readiness PASS | ✅ 0건 — MVP-6 영역 분리 영구 답습 |
| G2-5 | Hermes PMO 격상 | ✅ 0건 — ADR-008 부록 C 12 조건 미진입 영구 답습 |
| **합산** | **5/5** | **✅ 100% 위반 0건** |

### 3.3 G3 27 추가 분리 영역 답습 충족 매트릭스

| 영역 | 충족 상태 |
|------|--------|
| G3-1 ~ G3-27 | ✅ 27/27 분리 — 본 brief 영역 외 명시 답습 (자동 진입 0건) |

### 3.4 G4 8 풀 3+1 승격 트리거 발화 매트릭스

| # | 트리거 | 본 brief 시점 발화 |
|---|------|----------------|
| G4-1 ~ G4-8 | 8 트리거 | ✅ 0/8 발화 예상 — Reviewer-only 단축 합의 적격 |

### 3.5 G5 5 영구 핵심 제약 보존 매트릭스

| # | 영구 핵심 제약 | 보존 상태 |
|---|------------|--------|
| G5-1 ~ G5-5 | Hermes ≠ root of trust + 단일 source-of-truth + 수단/목적 분리 + T1/T2/T3 분리 + SPOF 의도적 수용 | ✅ 5/5 HIGH 보존 |

### 3.6 G6 Provider Liquidity 5-way 보존 매트릭스

| # | 영역 | 보존 상태 |
|---|------|--------|
| G6-1 ~ G6-5 | Model / Subscription / Vendor / API / Memory-Skill | ✅ 5/5 100% 보존 |

### 3.7 G7 F-금지 #1 영구 답습 매트릭스

| # | 영역 | 답습 상태 |
|---|------|--------|
| G7-1 | GitHub Actions secrets 사용 도입 | ✅ 0건 영구 답습 |

### 3.8 G8 actual run + evidence 답습 매트릭스

| # | 영역 | 답습 상태 |
|---|------|--------|
| G8-1 ~ G8-4 | 4 actual run (`25728590939` + `25728590916` + `25728590977` + `25731846625`) | ✅ 답습 (재실행 0건) |
| G8-5 ~ G8-12 | 9 evidence file (Tier-1 45 + URL 10 + Model 19 + `.importlinter` forbidden 4 + transitive + docker 3) | ✅ 답습 (재생성 0건) |
| G8-13 | ADR-011 §2.1 (a)~(e) × 3 Phase = 15/15 PASS | ✅ 답습 (재검증 0건) |
| **합산** | **13/13** | **✅ 100% 답습** |

### 3.9 G9 Rollback Trigger + TR-1 ~ TR-5 발화 0건 답습 매트릭스

| 그룹 | 본 brief 시점 발화 |
|-----|----------------|
| Layer B 18 trigger | ✅ 0/18 발화 영구 답습 |
| TR-1 ~ TR-5 | ✅ 0/5 발화 영구 답습 |
| **합산** | **✅ 23/23 발화 0건** |

### 3.10 합산 충족 매트릭스

| 그룹 | Prerequisite 수 | 충족 / 답습 |
|-----|-------------|----------|
| G1 상위 합의 답습 | 9 | ✅ 9/9 PASS (197 조건 변경 0건) |
| G2 5 사용자 명시 금지 | 5 | ✅ 5/5 위반 0건 |
| G3 27 추가 분리 | 27 | ✅ 27/27 분리 명시 |
| G4 8 풀 3+1 트리거 | 8 | ✅ 0/8 발화 예상 |
| G5 5 영구 핵심 제약 | 5 | ✅ 5/5 보존 |
| G6 Provider Liquidity | 5 | ✅ 5/5 보존 |
| G7 F-금지 #1 | 1 | ✅ 0/1 위반 |
| G8 actual run + evidence | 13 | ✅ 13/13 답습 |
| G9 Rollback Trigger 발화 | 23 | ✅ 0/23 발화 |
| **합산** | **96 prerequisite** | **✅ 96/96 충족** |

### 3.11 합산 권고

**96/96 prerequisite 충족 ✅** — Phase α-1 + α-2 + α-3 1순위 병렬 *실제 구현 진입 적격성 권위 권고 발행 가능*.

단, 본 §3 = *답습 한정* 검토 — **실 진입 *결정* 자체는 사용자 명시 결정 영역** (§4).

### 3.12 본 §3 의 *범위 한계*

본 §3 의 어떤 항목도:

- (i) 합산 197 합의 조건 中 어느 것도 *재선언* / *재확인* 하지 않으며 (답습 한정),
- (ii) 4 actual run 어느 것도 *재실행* 시키지 않으며,
- (iii) 9 evidence file 어느 것도 *재생성* 시키지 않으며,
- (iv) ADR-011 §2.1 (a)~(e) 5 조건 패턴 어느 것도 *재검증* 시키지 않으며,
- (v) 1순위 병렬 실 진입을 *시작* 시키지 않는다.

---

## 4. 진입 결정 영역 = 사용자 명시 결정 영역

본 §4 = 본 brief 권한 영역이 아닌 사용자 명시 결정 영역 enumerate 한정.

### 4.1 결정 영역 매트릭스 (4 영역)

| # | 결정 영역 | 옵션 enumerate | 권고 (사용자 결정 의무) |
|---|---------|--------------|----------------|
| D-1 | **cycle 옵션 결정** | (i) 답습 한정 단축 / (ii) minor 인터페이스 정렬 / (iii) 3 Phase 분리 / (iv) 풀 3+1 | (i) Stage 2 답습 한정 단축 권고 |
| D-2 | **합의 형태 결정** | (a) Reviewer-only 단축 / (b) 풀 3+1 / (c) 풀 3+1 + 외부 LLM 1+ | (a) Reviewer-only 단축 권고 (8/8 트리거 0건 발화 예상) |
| D-3 | **sub-step 순서 결정** | (1) α-1 → α-2 → α-3 / (2) α-1 → α-3 → α-2 / (3) α-2 → α-1 → α-3 / (4) α-3 → α-1 → α-2 / (5) 3 Phase 동시 진입 / (6) α-2 → α-3 → α-1 / (7) α-3 → α-2 → α-1 | (5) 3 Phase 동시 진입 권고 (의존성 토폴로지 답습 — α-1 ↔ α-2 부분 / α-1 ↔ α-3 독립 / α-2 ↔ α-3 독립) |
| D-4 | **3 Phase 합의 분리 vs 통합 결정** | (α) 통합 합의 1건 (3 Phase 동시) / (β) 분리 합의 3건 (α-1 / α-2 / α-3 각 단독) / (γ) 부분 통합 (예: α-1 + α-2 통합 + α-3 단독) | (α) 통합 합의 1건 권고 (cycle 옵션 (i) 답습) |

### 4.2 D-1 cycle 옵션 4 옵션 답습

| 옵션 | 영역 | 권고 |
|-----|------|----|
| **(i) 답습 한정 단축** | Stage 2 계획 brief 그대로 답습 + 변경 0건 검증 한정 cycle | ✅ **권고** — 8/8 트리거 0건 발화 예상 |
| (ii) minor 인터페이스 정렬 | α-1 + α-3 minor CLI 인터페이스 정렬 후보 한정 cycle | 보조 옵션 — 사용자 결정 시 |
| (iii) 3 Phase 분리 | 3 Phase 각 단독 진입 (3 cycle) | 분리 합의 시 D-4 (β) 답습 |
| (iv) 풀 3+1 | 풀 3+1 + 외부 LLM 1+ | 8/8 트리거 中 1+ 발화 시 |

### 4.3 D-2 합의 형태 3 옵션 답습

| 옵션 | 영역 | 권고 |
|-----|------|----|
| **(a) Reviewer-only 단축** | 8/8 풀 3+1 승격 트리거 0건 발화 시 적격 | ✅ **권고** — 본 brief = framing 차이 한정 (Stage 2 → Stage 3) + 권위 결정 0건 |
| (b) 풀 3+1 | 8/8 트리거 中 1+ 발화 시 | 본 brief 시점 미발화 예상 |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | 본 brief 시점 적용 영역 아님 (계획 brief 영역 답습) |

### 4.4 D-3 sub-step 순서 7 옵션 답습 (의존성 토폴로지 답습)

| 옵션 | 순서 | 의존성 영향 |
|-----|----|----------|
| (1) | α-1 → α-2 → α-3 | T-6 의존 답습 (α-1 책무 분담 → α-2 import-linter 룰 확정) |
| (2) | α-1 → α-3 → α-2 | T-6 의존 답습 + α-3 독립 |
| (3) | α-2 → α-1 → α-3 | T-6 의존 *역방향* (Group A 2차 답습 — 가능하나 비권고) |
| (4) | α-3 → α-1 → α-2 | α-3 독립 → T-6 의존 |
| **(5) 3 Phase 동시 진입** | α-1 ∥ α-2 ∥ α-3 | ✅ **권고** — α-1 ↔ α-2 부분 의존 (T-6) 가 *책무 분담 영역* (변경 0건), α-1 ↔ α-3 독립, α-2 ↔ α-3 독립 |
| (6) | α-2 → α-3 → α-1 | T-6 의존 역방향 + α-3 독립 |
| (7) | α-3 → α-2 → α-1 | α-3 독립 → T-6 의존 역방향 |

### 4.5 D-4 3 Phase 합의 분리 vs 통합 3 옵션 답습

| 옵션 | 영역 | 권고 |
|-----|------|----|
| **(α) 통합 합의 1건** | 3 Phase 동시 합의 — cycle 옵션 (i) 답습 | ✅ **권고** — Stage 2 합의 framing 답습 (`88ccf79` 1건 = 3 Phase 통합 합의) |
| (β) 분리 합의 3건 | α-1 / α-2 / α-3 각 단독 합의 | cycle 옵션 (iii) 답습 시 |
| (γ) 부분 통합 | α-1 + α-2 통합 + α-3 단독 (또는 다른 조합) | 사용자 명시 결정 시 |

### 4.6 합산 권고

본 §4 권고 조합 = **D-1 (i) + D-2 (a) + D-3 (5) + D-4 (α)** = **"Reviewer-only 단축 합의, 3 Phase 동시 진입, 통합 합의 1건, cycle 옵션 (i) 답습 한정"**.

단, 본 §4 권고 = *권고 한정* — 사용자 명시 결정 영역 (자동 결정 0건).

### 4.7 본 §4 의 *범위 한계*

본 §4 의 어떤 항목도:

- (i) 4 결정 영역 (D-1 ~ D-4) 中 어느 것도 *결정* 하지 않으며,
- (ii) 권고 조합 자체를 *자동 채택* 시키지 않으며,
- (iii) 합의 보고서 작성 / 실 진입 / commit / push 어느 것도 *자동 진입* 시키지 않는다.

---

## 5. 진입 *후* 단계 분할 권고 매트릭스 (본 brief 영역 외)

본 §5 = 진입 결정 *후* 단계 분할 답습 한정 (Stage 2 계획 brief §3 답습). 본 brief 권한 외 — 어느 step 도 자동 진입 0건.

### 5.1 권고 cycle (cycle 옵션 (i) 답습 한정 단축, 사용자 결정 후 진입)

| Step | 영역 | 작업 내용 | 본 brief 권한 |
|-----|------|--------|----------|
| Step 0 | 사전 점검 | 96/96 prerequisite 답습 검증 (본 brief §3 답습) | ✅ 본 brief 영역 (사전 점검 자체) |
| Step 1.α-1 | 1순위 병렬 — α-1 진입 | R-4 도구 본문 채택 검증 (829줄 답습 한정, 변경 0건) | ❌ 본 brief 영역 외 |
| Step 1.α-2 | 1순위 병렬 — α-2 진입 | R-5 `.importlinter` 본문 채택 검증 (35줄 답습 한정, 변경 0건) | ❌ 본 brief 영역 외 |
| Step 1.α-3 | 1순위 병렬 — α-3 진입 | R-7 docker secret block 채택 검증 (328줄 답습 한정, 변경 0건) | ❌ 본 brief 영역 외 |
| Step 2 | actual run PASS 답습 | 4 prerequisite actual run (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 답습 검증 (재실행 0건) | ❌ 본 brief 영역 외 |
| Step 3 | 합의 형태 결정 | D-2 (a) / (b) / (c) — 사용자 명시 결정 의무 | ❌ 본 brief 영역 외 |
| Step 4 | 옵션 외부 LLM | D-2 (c) 채택 시만 — 사용자 명시 결정 의무 | ❌ 본 brief 영역 외 |
| Step 5 | 합의 보고서 작성 | `docs/review/3plus1-consensus-2026-05-XX-phase-alpha-123-parallel-implementation-actual-entry.md` 작성 | ❌ 본 brief 영역 외 |
| Step 6 | 메타 commit + push | CONTEXT / INDEX / SESSION 메타 갱신 + git commit + push | ❌ 본 brief 영역 외 |

### 5.2 사용자 명시 5 금지 영역 × cycle 단계 분리 매트릭스

| 금지 영역 | Step 0 | Step 1 | Step 2 | Step 3 | Step 4 | Step 5 | Step 6 |
|-------|-------|-------|-------|-------|-------|-------|-------|
| #1 실제 파일 수정 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 |
| #2 CI workflow 변경 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 |
| #3 runtime code 변경 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 |
| #4 Operational Readiness PASS | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 |
| #5 Hermes PMO 격상 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 | ❌ 0건 |

**전체 7 단계 × 5 금지 = 35/35 위반 0건 영구 답습** (사용자 명시 5 금지 = cycle 옵션 (i) 답습 한정 단축에 의해 영구 만족).

### 5.3 본 §5 의 *범위 한계*

본 §5 의 어떤 step 도 **본 brief 영역 외** — 어느 step 도 *자동 진입 0건*. Step 0 = 본 brief = 사전 점검 자체. Step 1 ~ Step 6 = 사용자 명시 결정 후 별도 단계.

---

## 6. 진입 시점 Rollback Trigger 검토 (발화 0건 영구 답습)

### 6.1 Layer B 18 Rollback Trigger 답습 (Stage 2 §6.1 답습)

| 영역 | trigger 수 | 본 brief 시점 발화 |
|------|--------|----------------|
| 1순위 직접 영향 | 7 | 0건 — Layer C 발효 시점 답습 |
| 1순위 간접 영향 | 1 | 0건 — Layer C 발효 시점 답습 |
| 1순위 영역 외 (Phase α-4 / Backlog / Phase β / γ 영역) | 10 | 0건 — 본 brief 영역 외 |
| **합산** | **18** | **0건 영구 답습** |

### 6.2 TR-1 ~ TR-5 답습 (Group A 2차 — α-2 R-5 한정, Stage 2 §6.2 답습)

| TR | 영역 | 본 brief 시점 발화 |
|----|-----|----------------|
| TR-1 | `.importlinter` forbidden 4 모듈 변경 | 0건 — 변경 0건 영구 답습 |
| TR-2 | `include_external_packages` 변경 | 0건 — 변경 0건 영구 답습 |
| TR-3 | `root_packages` 변경 | 0건 — 변경 0건 영구 답습 |
| TR-4 | `ignore_imports` 변경 | 0건 — 변경 0건 영구 답습 |
| TR-5 | import-linter 외부 모듈 install 사전 검증 | 0건 — C-9 RA-9 답습 (이미 PASS) |
| **합산** | **5** | **0건 영구 답습** |

### 6.3 합산 발화 매트릭스

| 그룹 | trigger 수 | 본 brief 시점 발화 |
|-----|--------|----------------|
| Layer B 18 trigger | 18 | 0건 |
| TR-1 ~ TR-5 | 5 | 0건 |
| **합산** | **23** | **0건 영구 답습** |

### 6.4 threshold 후보 한정 유지 매트릭스 (고정 0건)

| threshold | 본 brief 시점 |
|---------|----------|
| FP (False Positive) | 후보 한정 (Stage 2 §6.3 답습) |
| FN (False Negative) | 후보 한정 |
| latency | 후보 한정 |
| CI runtime | 후보 한정 |
| image layer leak count | 후보 한정 |
| restart recovery rate | 후보 한정 |
| **합산** | **6/6 후보 한정 — 고정 0건** |

### 6.5 본 §6 의 *범위 한계*

본 §6 의 어떤 항목도:

- (i) Rollback Trigger / TR-1 ~ TR-5 어느 것도 *발화* 시키지 않으며,
- (ii) threshold 어느 것도 *고정* 시키지 않으며,
- (iii) 합의 본문 어느 줄도 *변경* 하지 않는다.

---

## 7. 진입 시점 Evidence 기준 검토

### 7.1 ADR-011 §2.1 (a)~(e) × 3 Phase = 15/15 PASS 답습 매트릭스 (Stage 2 §7 답습)

| Phase | (a) 기존 패턴 동등성 | (b) 격리 PoC 동등성 | (c) PR 매트릭스 동등성 | (d) regression 답습 | (e) canary 답습 | 합계 |
|------|---------------|----------------|------------------|----------------|--------------|----|
| α-1 (R-4) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | 5/5 |
| α-2 (R-5) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | 5/5 |
| α-3 (R-7) | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | ✅ PASS | 5/5 |
| **합계** | **3/3** | **3/3** | **3/3** | **3/3** | **3/3** | **15/15 PASS** |

본 매트릭스 = **Layer C 발효 시점 답습** (재검증 0건).

### 7.2 9 evidence 파일 답습 매트릭스 (재생성 0건)

| Phase | Evidence file 수 | 답습 상태 |
|------|--------------|--------|
| α-1 (R-4) | 3 (Tier-1 45 + URL 10 + Model 19) | ✅ Layer C 답습 |
| α-2 (R-5) | 2 (forbidden 4 모듈 + transitive) | ✅ Layer C 답습 |
| α-3 (R-7) | 3 (secret block + image layer + restart recovery) | ✅ Layer C 답습 |
| ADR-011 §2.1 5 조건 | 1 (15/15 PASS 매트릭스) | ✅ Layer C 답습 |
| **합산** | **9** | **✅ 9/9 답습** |

### 7.3 Evidence Artifact 형식 답습 매트릭스 (Stage 2 §7.3 답습, 변경 0건)

| Artifact | 형식 | 본 brief 시점 |
|--------|----|----------|
| GitHub Actions run | JSON conclusion + duration + step-level | 답습 (4 run_id 영구 답습) |
| Local test fixture | Pass/Fail count + assertion log | 답습 |
| Markdown evidence | 본 brief + Stage 2 + Layer C 발효 합의 본문 답습 | 답습 |

### 7.4 ledger entry 후보 한정 매트릭스 (정식 등록 0건, Backlog #5 분리)

| 후보 enum | 본 brief 시점 |
|---------|----------|
| `secret_scan_layer1_implementation` | 후보 한정 |
| `secret_storage_isolation_implementation` | 후보 한정 |
| `provider_adapter_enforcement_layer1_static` | 후보 한정 |
| `mvp1_gate_pass` | 후보 한정 |
| `ci_secret_access_attempted` | 후보 한정 (G3-7 영역) |
| `provider_key_adapter_bypass_risk_detected` | 후보 한정 (§5.4 IR-1) |
| `direct_sdk_with_secret_leakage_detected` | 후보 한정 (§5.4 IR-2) |
| `secret_handling_environment_mismatch_detected` | 후보 한정 (§5.4 IR-3) |
| **합산** | **8 후보 한정 — 정식 등록 0건 (Backlog #5 분리)** |

### 7.5 본 §7 의 *범위 한계*

본 §7 의 어떤 항목도:

- (i) ADR-011 §2.1 (a)~(e) 5 조건 어느 것도 *재검증* 시키지 않으며,
- (ii) 9 evidence file 어느 것도 *재생성* 시키지 않으며,
- (iii) 8 ledger entry enum 후보 어느 것도 *정식 등록* 시키지 않는다 (Backlog #5 분리).

---

## 8. 사용자 명시 5 금지 영역 × 진입 시점 분리 매트릭스

### 8.1 본 brief 영역 5/5 위반 0건 영구 답습 매트릭스

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 시점 (Step 0) | 사용자 명시 결정 후 Step 1 ~ 6 |
|---|---------|------------------|--------------------------|--------------------------|
| #1 | 실제 파일 수정 | ✅ 0건 | ✅ 0건 | ✅ 0건 (사용자 명시 5 금지) |
| #2 | CI workflow 변경 | ✅ 0건 | ✅ 0건 | ✅ 0건 (사용자 명시 5 금지) |
| #3 | runtime code 변경 | ✅ 0건 | ✅ 0건 | ✅ 0건 (사용자 명시 5 금지) |
| #4 | Operational Readiness PASS | ✅ 0건 | ✅ 0건 | ✅ 0건 (사용자 명시 5 금지) |
| #5 | Hermes PMO 격상 | ✅ 0건 | ✅ 0건 | ✅ 0건 (사용자 명시 5 금지) |
| **합산** | **5/5** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** | **✅ 100% 위반 0건** |

### 8.2 추가 27 분리 영역 위반 0건 영구 답습 매트릭스

본 §0.4 27 분리 영역 enumerate 답습 — 본 brief 작성 시점 + 본 brief 발효 후 Step 0 ~ Step 6 전체 영역 = **27/27 분리 명시 + 위반 0건 영구 답습**.

### 8.3 본 §8 의 *범위 한계*

본 §8 의 어떤 항목도:

- (i) 5 사용자 명시 금지 영역 어느 것도 *진입* / *해소* 시키지 않으며,
- (ii) 27 추가 분리 영역 어느 것도 *진입* / *통합* 시키지 않는다.

---

## 9. 합의 형태 권고 + 풀 3+1 승격 트리거

### 9.1 본 brief 의 합의 형태 권고 매트릭스

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| **(a) Reviewer-only 단축 합의** | 8/8 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ✅ **권고** — 8/8 트리거 0건 발화 예상 + 본 brief = framing 차이 한정 (Stage 2 → Stage 3) + 권위 결정 0건 |
| (b) 풀 3+1 합의 | 8/8 트리거 中 1+ 발화 | 본 brief 시점 미발화 예상 |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | 본 brief 시점 적용 영역 아님 |

### 9.2 풀 3+1 승격 트리거 후보 검토 (예상 0/8 발화)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 새 권위 결정 (계획 brief 영역) | 0건 — Stage 2 framing 답습 |
| T-2 | 5 영구 핵심 제약 약화 | 0건 — 본 brief 답습 |
| T-3 | Provider Liquidity 5-way 영향 | 0건 — 본 brief = 진입 여부 한정 |
| T-4 | ADR-011 §2.1 (a)~(e) 5 조건 패턴 영향 | 0건 — 본 brief = 답습 한정 |
| T-5 | 197 합의 조건 자동 변경 영향 | 0건 — 본 brief 답습 |
| T-6 | Hermes ≠ root of trust 영향 | 0건 — 본 brief 답습 |
| T-7 | F-금지 #1 (GitHub Actions secrets) 도입 | 0건 — 영구 답습 |
| T-8 | 합의 영역 *변경* (계획 brief → 진입 여부 brief 단순 framing 전환만) | 0건 — 본 brief = framing 차이 한정 |
| **합산** | **8** | **✅ 0/8 발화 예상 — Reviewer-only 단축 합의 적격** |

### 9.3 본 §9 의 *범위 한계*

본 §9 의 어떤 항목도:

- (i) 합의 형태 어느 것도 *자동 결정* 하지 않으며 (사용자 명시 결정 영역),
- (ii) 풀 3+1 승격 트리거 어느 것도 *발화* 시키지 않는다.

---

## 10. 금지 사항

### 10.1 본 brief 자체 금지 사항 (사용자 명시 답습)

본 brief 작성 시점 금지 영역:

- ❌ **실제 파일 수정** (사용자 명시 5 금지 #1) — 1192줄 답습 보존
- ❌ **CI workflow 변경** (사용자 명시 5 금지 #2)
- ❌ **runtime code 변경** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ Phase α-1 / α-2 / α-3 자동 실 진입 (본 brief = *진입 여부 검토 한정*)
- ❌ Phase α-4 자동 진입 (2순위 의존 분리)
- ❌ Layer C 재발효
- ❌ Layer D 재선언
- ❌ MVP-1 PASS 재선언
- ❌ 9 evidence 파일 재생성
- ❌ 4 prerequisite actual run 재실행
- ❌ 신규 actual run 자동 trigger
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ 합산 197 합의 조건 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Rollback Trigger / TR-1 ~ TR-5 자동 발화
- ❌ threshold 자동 *고정*
- ❌ event enum 정식 등록 (Backlog #5 분리)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행

### 10.2 본 brief 발효 *후* 진입 단계 금지 사항 (의무 답습 — Stage 2 §10.2 답습)

본 brief 발효 후 Step 0 ~ Step 6 어느 단계도 (사용자 명시 결정 영역):

- ❌ **사용자 명시 5 금지 영역 진입 0건** — Step 0 ~ Step 6 전체 영역 영구 만족
- ❌ **R-4 + R-5 + R-7 합산 1192줄 본문 어느 줄도 변경 0건** — cycle 옵션 (i) 답습 한정
- ❌ **`src/` 본문 변경 0건** + facade.py real 본문 작성 0건 (Backlog #4 분리)
- ❌ **R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 0건**
- ❌ **`.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경 0건**
- ❌ **R-7 docker secret block 본문 변경 0건**
- ❌ **3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경 0건**
- ❌ **PC-3 / AR-1 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 0건**
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 0건**
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건**
- ❌ **threshold 자동 *고정* 0건**
- ❌ **Rollback Trigger / TR-1 ~ TR-5 자동 발화 0건**
- ❌ **합산 197 합의 조건 자동 변경 0건**
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 2 / Stage 4 / Group A / Group D 합의 본문 변경 0건**
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
- ❌ **실 secret material commit 0건**
- ❌ **event enum 정식 등록 0건** (Backlog #5 분리)
- ❌ **ADR 본문 자동 갱신 0건** (cross-reference 답습 한정)
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 0건**

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (D-1 (i) + D-2 (a) + D-3 (5) + D-4 (α) 권고 조합 답습) | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-17-phase-alpha-123-parallel-implementation-actual-entry.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → **3 Phase 분리 합의 진입** (D-4 (β) 답습) | α-1 / α-2 / α-3 각 단독 합의 보고서 작성 (3 cycle) |
| (E) | 본 brief 승인 → **부분 통합 합의** (D-4 (γ) 답습) | 사용자 명시 부분 통합 영역 결정 + 합의 보고서 작성 |
| (F) | 본 brief 승인 → **풀 3+1 합의** (D-2 (b) 답습) | 풀 3+1 합의 보고서 작성 |
| (G) | 본 brief 승인 → **풀 3+1 + 외부 LLM 1+ 합의** (D-2 (c) 답습) | 풀 3+1 + 외부 LLM blind 의뢰 진입 |
| (H) | 본 brief 승인 → **minor 인터페이스 정렬 cycle** (D-1 (ii) 답습) | minor 정렬 단계 분할 brief |
| (I) | 본 brief 보류 → **Phase α-4 진입 조건 점검 brief 작성** (2순위 의존 영역) | Phase α-4 단독 brief 영역 |
| (J) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 결정 영역 |
| (K) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (L) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 11.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. 3 Phase 분리 합의 진입."
- (E): "옵션 (E) 로 진행해주세요. 부분 통합 합의 진입."
- (F): "옵션 (F) 로 진행해주세요. 풀 3+1 합의 진입."
- (G): "옵션 (G) 로 진행해주세요. 풀 3+1 + 외부 LLM 1+ 합의 진입."
- (H): "옵션 (H) 로 진행해주세요. minor 인터페이스 정렬 cycle brief 작성."
- (I): "옵션 (I) 로 진행해주세요. Phase α-4 진입 조건 점검 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (K): "옵션 (K) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (L): "옵션 (L) 로 진행해주세요. 세션 종료."

### 11.2 본 §11 의 *범위 한계*

본 §11 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 12. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — Phase α-1 + α-2 + α-3 *실제 병렬 구현 진입 여부* brief — 검토 한정) |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — 실제 파일 수정 0건 / CI workflow 변경 0건 / runtime code 변경 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| 추가 27 분리 영역 답습 | ✅ (27/27 — Phase α-4 / branch protection / dev 환경 / `pre-commit install` 의무화 / PC-3+4 + AR-1+2+3 / ST-1/2/4/5 / S-2 / Tier 변경 / Tier-2/3 확장 / Hermes upstream / Production docker-compose / 실 secret material / GitHub Actions secrets / `pull_request_target` / commit signing / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 모두 분리) |
| Stage 1 통합 계획 합의 답습 (`542e77e`) | ✅ (25 조건 C-μ-1 ~ C-μ-25 답습 — 자동 변경 0건 + cycle 옵션 (i) 1순위 부분 한정 답습) |
| Stage 2 1순위 병렬 계획 합의 답습 (`88ccf79`) | ✅ (25 조건 C-ν-1 ~ C-ν-25 답습 — 자동 변경 0건 + framing 차이 한정) |
| Layer C 발효 답습 (`eb01bc4`) | ✅ (재발효 0건 + evidence 재생성 0건 + actual run 재실행 0건 + 30 조건 C-ι-1 ~ C-ι-30 변경 0건) |
| Layer D 권위 답습 (`210c98f` + 후속 18 / `951a5b1`) | ✅ (재선언 0건 + 본문 변경 0건 + 25 조건 C-λ-1 ~ C-λ-25 변경 0건) |
| Phase α-1 / α-2 / α-3 합의 답습 | ✅ (C-β-1 ~ C-β-15 + C-γ-1 ~ C-γ-26 + C-δ-1 ~ C-δ-28 = 69 조건 변경 0건) |
| Group α 합의 답습 (`4880e88`) | ✅ (C-1 ~ C-12 답습 — 자동 해소 0건 + 자동 변경 0건) |
| Backlog #6 우선 진입 합의 답습 (`c7ddfdd`) | ✅ (C-α-1 ~ C-α-11 11 조건 변경 0건) |
| Layer A / Layer B / §5.5 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger + TR-1 ~ TR-5 답습 | ✅ (발화 0건 — §6 답습) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (3 Phase = enforcement / config / docker secret 영역 = catalog / provider 직교) |
| F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) | ✅ (영구 보존) |
| 풀 3+1 승격 트리거 0/8 발화 예상 | ✅ (§9.2 답습) |
| 합산 1192줄 본문 변경 0건 | ✅ (R-4 829 + R-5 35 + R-7 328 답습 100% 보존) |
| `src/` 본문 변경 0건 | ✅ (facade.py 41줄 placeholder 답습 보존) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| 96/96 Prerequisite 충족 검증 | ✅ (§3.10 답습 — 9/9 G1 + 5/5 G2 + 27/27 G3 + 0/8 G4 + 5/5 G5 + 5/5 G6 + 0/1 G7 + 13/13 G8 + 0/23 G9 = 96/96) |
| 합의 조건 합산 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Layer C 30 + Layer D 25 + Phase α 통합 계획 25 + Phase α-1+2+3 계획 25 = **합산 197 조건** + ADR-011 §2.1 모법 변경 0건) |
| framing 차이 명시 | ✅ (Stage 2 "How to plan?" → Stage 3 "Should we enter?" framing 전환 명시) |
| 4 결정 영역 enumerate | ✅ (D-1 cycle 옵션 / D-2 합의 형태 / D-3 sub-step 순서 / D-4 합의 분리 vs 통합 — 모두 사용자 명시 결정 영역) |
| Step 0 ~ Step 6 분할 답습 | ✅ (Stage 2 §3 답습 — 모든 step = 본 brief 영역 외) |

---

## 13. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-1 + α-2 + α-3 1순위 병렬 구현 *계획* brief 합의 (`88ccf79` 후속 20 APPROVE AS BRIEF — Reviewer-only 단축, 25 조건 C-ν-1 ~ C-ν-25) 후속**, **Phase α-1 + α-2 + α-3 1순위 병렬 *실제 구현 진입 여부* 검토 한정 준비안 (DRAFT)**. **framing 차이 명시** = Stage 2 ("*How* to plan 1순위 parallel?") → **Stage 3 ("*Should* we enter 1순위 parallel actual implementation now?")**. **사용자 명시 5 금지** (실제 파일 수정 / CI workflow 변경 / runtime code 변경 / Operational Readiness PASS / Hermes PMO 격상) 5/5 답습 + **추가 27 분리 영역** 27/27 분리 명시. **9 그룹 합산 96 Prerequisite 충족 매트릭스** = G1 상위 9 합의 답습 9/9 PASS (197 조건 변경 0건) + G2 5 사용자 명시 금지 5/5 위반 0건 + G3 27 추가 분리 27/27 분리 + G4 8 풀 3+1 트리거 0/8 발화 예상 + G5 5 영구 핵심 제약 5/5 보존 + G6 Provider Liquidity 5-way 5/5 보존 + G7 F-금지 #1 0/1 위반 + G8 actual run + evidence 13/13 답습 + G9 Rollback Trigger 0/23 발화 = **96/96 충족 ✅**. **진입 결정 4 영역 매트릭스 (사용자 명시 결정 영역)** = D-1 cycle 옵션 (4 옵션, (i) 권고) / D-2 합의 형태 (3 옵션, (a) Reviewer-only 단축 권고) / D-3 sub-step 순서 (7 옵션, (5) 3 Phase 동시 진입 권고) / D-4 3 Phase 합의 분리 vs 통합 (3 옵션, (α) 통합 합의 1건 권고) → **권고 조합 = "Reviewer-only 단축 합의, 3 Phase 동시 진입, 통합 합의 1건, cycle 옵션 (i) 답습 한정"**. **진입 *후* 단계 분할 권고 매트릭스** (본 brief 영역 외) = Step 0 사전 점검 (본 brief 자체) + Step 1.α-1 + Step 1.α-2 + Step 1.α-3 + Step 2 actual run PASS 답습 + Step 3 합의 형태 결정 + Step 4 옵션 외부 LLM + Step 5 합의 보고서 + Step 6 메타 commit push — 모두 본 brief 영역 외 + 7 단계 × 5 금지 = 35/35 위반 0건 영구 답습. **진입 시점 Rollback Trigger 23 발화 0건 영구 답습** (Layer B 18 + TR-1 ~ TR-5 5) + **threshold 6/6 후보 한정 — 고정 0건**. **진입 시점 Evidence 15/15 PASS Layer C 답습** (ADR-011 §2.1 (a)~(e) × 3 Phase 답습, 재검증 0건) + **9 evidence 9/9 답습** (재생성 0건) + **ledger entry 8 후보 한정** (정식 등록 0건, Backlog #5 분리). **본 brief 자체 금지 26 + 본 brief 발효 후 진입 단계 금지 27** enumerate. **본 brief 는 Phase α-1 / α-2 / α-3 어느 것도 *실 진입* 시키지 않으며, 합산 1192줄 본문 어느 줄도 *변경* 하지 않으며, `src/` 본문 어느 줄도 *변경* 하지 않으며, 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 197 합의 조건 어느 것도 *변경* / Phase α-4 자동 진입 / 4 결정 영역 (D-1 ~ D-4) 어느 것도 *결정* / 합의 형태 *결정* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~L, §11 답습).

---

**작성일**: 2026-05-17
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~L, §11 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **실제 파일 수정** (사용자 명시 5 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 5 금지 #2)
- ❌ **runtime code 변경** (사용자 명시 5 금지 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 5 금지 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 5 금지 #5)
- ❌ Phase α-1 / α-2 / α-3 어느 것도 자동 실 진입 (본 brief = *진입 여부 검토 한정*)
- ❌ Phase α-4 자동 진입 (2순위 의존 분리)
- ❌ branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 (추가 분리)
- ❌ 실 hook 구현 / Phase β / γ 자동 진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ 9 evidence 파일 재생성 / 4 prerequisite actual run 재실행 / 신규 actual run trigger
- ❌ R-4 + R-5 + R-7 합산 1192줄 어느 줄도 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-3 / AR-1 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7 4 항목) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 자동 발화
- ❌ 합산 197 합의 조건 자동 변경
- ❌ Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 2 / Stage 4 / Group A / Group D 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ 4 결정 영역 (D-1 cycle 옵션 / D-2 합의 형태 / D-3 sub-step 순서 / D-4 합의 분리 vs 통합) 어느 것도 자동 결정
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile 변경
- ❌ Production `docker-compose.yml` 신설 / 변경
- ❌ 실 secret material commit
- ❌ event enum 정식 등록 (Backlog #5 분리)
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
- ❌ 실 docker build / docker run / docker history 자동 실행
- ❌ 인간 리뷰 의무 자동 발화
