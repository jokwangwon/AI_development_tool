# Phase α-4 R-1 Stage 4 W-3 micro-patch brief (3 fixture 한정, cycle 3/4) (DRAFT)

> **본 문서는 Phase α-4 R-1 Stage 4 W-2 micro-patch brief Reviewer-only 단축 합의 (`310b518` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 35 조건 C-χ-1 ~ C-χ-35, 합산 503 합의 조건) 발효 후속, 사용자 명시 진입 명령 답습 — **Phase α-4 R-1 Stage 4 *W-3 단독* 영역 (3 fixture `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄 한정) *최소 micro-patch 가능성 검토* brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 4 entry (W-1~W-4 lockdown, `9c33efe` + `81472ba`) = "*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?"
> - α-4 Stage 4 W-1 brief (`7af77fb` + `df741a2`, cycle 1/4) = "*Should* W-1 introduce micro-patch lines on 3 workflow?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - α-4 Stage 4 W-2 brief (`557c607` + `310b518`, cycle 2/4) = "*Should* W-2 introduce micro-patch lines on integration tool?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - **본 brief = α-4 Stage 4 W-3 micro-patch *possibility* 검토 DRAFT (cycle 3/4)** — **"*Should* W-3 introduce micro-patch lines on 3 fixture (and which ones), or is *0-line passthrough* the correct posture for the fixtures at this gate?"**
> - α-4 Stage 4 W-3 실 micro-patch (본 brief 외) = "*Execute* the chosen patch (if any)"
> - W-4 = 영역 외 영구 답습 (cycle 4/4 별도 brief 영역)
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) 3 fixture (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml`) 어느 줄도 *변경* 하지 않으며, (ii) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며 (W-1 = 0-line passthrough 답습 영구), (iii) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 = 0-line passthrough 답습 영구), (iv) W-4 어느 작업도 *진입* 시키지 않으며, (v) Stage 4 entry brief 합의 49 + W-1 합의 30 + W-2 합의 35 = 합산 503 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며, (vi) 사용자 명시 5 금지 (fixture 본문 실 변경 / CI workflow 변경 / integration tool 변경 / actual run 재실행 / Operational Readiness PASS 선언 / Hermes PMO 격상) 어느 것도 *해소* 시키지 않으며, (vii) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, (viii) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-19 후속 31
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w2-micropatch.md` (commit `310b518` — W-2 brief Reviewer-only 단축 합의 APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 35 조건 C-χ-1 ~ C-χ-35, **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-stage4-w2-micropatch-brief.md` (commit `557c607`, 1009줄 — W-2 brief DRAFT)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w1-micropatch.md` (commit `df741a2` — W-1 brief Reviewer-only 단축 합의, 30 조건 C-φ-1 ~ C-φ-30)
- `docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md` (commit `7af77fb`, 868줄 — W-1 brief DRAFT)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md` (commit `81472ba` — Stage 4 entry brief 풀 3+1 합의, 49 조건 C-υ-1 ~ C-υ-49)
- `docs/phase0/phase-alpha-4-r1-stage4-entry-brief.md` (commit `9c33efe`, 1032줄 — Stage 4 W-1~W-4 lockdown brief)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS, **3 fixture 3/3 PASS 포함**)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C (Hermes PMO Activation 12 조건 미진입 영구 답습)
- `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` (30줄 — **본 brief 의 대상 1/3**, 답습 한정 read-only)
- `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` (31줄 — **본 brief 의 대상 2/3**, 답습 한정 read-only)
- `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` (28줄 — **본 brief 의 대상 3/3**, 답습 한정 read-only)

---

## 0. 본 brief 의 범위

### 0.1 사용자 명시 진입 명령 답습

> "W-4 actual run trigger / 검증 brief를 작성해주세요. 단, W-3 fixture 검증이 먼저 필요한지 사전 평가해주세요."
>
> (사전 평가 응답: W-3 fixture brief 선행 = 권고 시작점 — Stage 4 entry brief §2.2 cycle (i) 직렬 토폴로지 + W-4 actual run RUN-1~6 검증의 fixture 무결성 전제 + cycle 비용 최소(89줄). 사용자 결정: **W-3 fixture brief 먼저 (권고)** 채택.)

### 0.2 사용자 명시 5 금지 답습 (본 brief 의 명시적 경계)

| # | 금지 영역 | 본 brief 시점 |
|---|---------|----------|
| **#1** | **3 fixture 실 변경** (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄 변경 발효) | ✅ 0건 영구 답습 — 본 brief = *후보 검토 한정* |
| **#2** | **CI workflow 변경** (3 MVP-1 workflow 1206줄 변경 발효) | ✅ 0건 영구 답습 — W-1 cycle 1/4 합의 답습 (0-line passthrough 고정 영구) |
| **#3** | **integration tool 변경** (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 발효) | ✅ 0건 영구 답습 — W-2 cycle 2/4 합의 답습 (0-line passthrough 고정 영구) |
| **#4** | **actual run 재실행** (신규 GitHub Actions run trigger) | ✅ 0건 영구 답습 — W-4 영역 분리 (cycle 4/4 별도) |
| **#5** | **Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F)** | ✅ 0건 영구 답습 — MVP-6 / ADR-008 부록 C 12 조건 미진입 |

**주**: 본 brief 의 #2 + #3 영역은 W-1 + W-2 합의 답습 (W-1 = 3 workflow 1206줄 변경 0건 영구 / W-2 = integration tool 298줄 변경 0건 영구) — W-3 영역 (3 fixture) 과는 별도 영역. 본 brief = W-3 단독 영역 한정 → #1 ~ #5 모두 영구 답습.

### 0.3 본 brief 영역 vs Stage 4 entry / W-1 / W-2 brief 영역 분리 매트릭스

| 영역 | Stage 4 entry brief (`9c33efe`+`81472ba`) | W-1 brief (`7af77fb`+`df741a2`) | W-2 brief (`557c607`+`310b518`) | 본 brief (W-3) |
|------|------------------------------------------|--------------------------------|--------------------------------|--------------|
| 범위 | W-1 + W-2 + W-3 + W-4 lockdown 권고 | W-1 단독 micro-patch 가능성 검토 | W-2 단독 micro-patch 가능성 검토 | **W-3 단독 micro-patch 가능성 검토 (3 fixture 한정)** |
| 변경 대상 artifact | 7 artifacts × 1593줄 | 3 MVP-1 workflow 1206줄 | integration tool 298줄 | **3 fixture 89줄 (PASS 30 + FAIL PC-3 31 + FAIL AR-1 28)** |
| 권고 영역 | 수정 파일 + 검증 방법 + actual run 조건 + rollback trigger | 변경 0 lines 우선 + 후보 영역 ≤ 15 lines (paths-only) enumerate | 변경 0 lines 우선 + 후보 영역 ≤ 15 lines (comment/help/error-message) enumerate | **변경 0 lines 우선 + 후보 영역 ≤ 6 lines (comment/blank/header-only) enumerate** |
| 변경 line 권고 결과 | 0 ~ ≤ 25 lines micro-patch *권고 시작점* | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **0 lines 우선 권고 + 후보 영역 ≤ 6 lines enumerate** |
| W-4 영역 | 권고 영역 포함 (분리 명시) | 분리 명시 (cycle 4/4 별도) | 분리 명시 (cycle 4/4 별도) | ❌ **본 brief 영역 외 (사용자 명시 #4 답습 cycle 4/4 분리)** |
| 검증 방법 | Pre / Per-W / Post / Actual run 4 단계 (42 검증) | W-1 단독 검증 7 영역 + PRE-0 | W-2 단독 검증 8 영역 + PRE-0 | **W-3 단독 검증 7 영역 (W-3-V1 ~ W-3-V7) + PRE-0 도구 가용성 답습** |
| 합의 결과 발효 | APPROVE AS BRIEF WITH CONDITIONS (49 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (30 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (35 조건) | DRAFT (사용자 명시 승인 *전*) |

### 0.4 본 brief 가 *하는* 것

1. W-2 brief 합의 (`310b518` — 35 조건 C-χ-1 ~ C-χ-35) 발효 후속 — **W-3 단독 micro-patch *가능성 검토* 한정** (§1)
2. **W-3 영역 한정 매트릭스** — 3 fixture 한정 + W-1 + W-2 답습 + W-4 분리 명시 (§2)
3. **3 fixture 현재 상태 매트릭스 (read-only)** — 89줄 구조 / 3 fixture expected behavior / 호출 인터페이스 / LVE 3/3 PASS 답습 (§3)
4. **Micro-patch 후보 영역 *enumerate 한정*** — 변경 line 0 lines 우선 권고 + ≤ 6 lines 후보 (comment / blank-line / header 한정, semantics 변경 비권고) (§4)
5. **W-3 검증 방법 권고** — W-3-V1 ~ W-3-V7 답습 + PRE-0 도구 가용성 사전 점검 (C-υ-38 답습) (§5)
6. **W-3 시점 rollback trigger 발화 가능성 매트릭스** (§6)
7. **사용자 명시 5 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 503 합의 조건 답습 매트릭스** (변경 0건) (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **3 fixture 실 변경 (0건)** — `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄 변경 발효 = 별도 cycle 영역
- ❌ **CI workflow 변경 (0건)** — W-1 = 0-line passthrough 고정 답습 (사용자 명시 #2)
- ❌ **integration tool 변경 (0건)** — W-2 = 0-line passthrough 고정 답습 (사용자 명시 #3)
- ❌ **actual run 재실행 (0건)** — W-4 신규 trigger = 별도 cycle 영역 (사용자 명시 #4)
- ❌ **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) (0건)** — MVP-6 / ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (W-2 합의 35 + W-1 합의 30 + Stage 4 entry brief 49 + α-1+2+3 evidence + LVE 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — 3 workflow 1206 + integration tool 298 + 3 fixture 89 = 1593줄 답습 보존
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (α-1+2+3 evidence §5.1 답습)
- ❌ **`src/` runtime code / facade.py placeholder 변경 (0건)** — Backlog #4 분리
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 본문 채택 변경 (0건)** — C-υ-44 답습 강화
- ❌ **fixture semantics 변경 (0건)** — PASS rc=0 / FAIL rc=1 expected 답습 위반 영역
- ❌ **fixture entry step name 변경 (0건)** — `ENTRY_NAME_PATTERNS` 매칭 답습 위반 영역 ("MVP-1 entry" prefix 답습)
- ❌ **PASS fixture 에 `continue-on-error: true` 추가 (0건)** — PC-3 expected pass 답습 위반 영역
- ❌ **PASS fixture 의 `set -e` / `exit 1` 제거 (0건)** — AR-1 expected pass 답습 위반 영역
- ❌ **FAIL fixture (PC-3) 의 `continue-on-error: true` 제거 (0건)** — PC-3 expected fail 답습 위반 영역
- ❌ **FAIL fixture (AR-1) 의 `set -e` / `exit 1` 추가 (0건)** — AR-1 expected fail 답습 위반 영역
- ❌ **신규 fixture 추가 (0건)** — 3 fixture 외 확장 = 별도 합의 영역 (LVE 3/3 PASS 영역 확장 = 재집계 의무 발화)
- ❌ **fixture 삭제 (0건)** — 3 fixture 中 1+ 삭제 = LVE 영역 변경 (재집계 의무 발화)
- ❌ **fixture YAML schema 변경 (0건)** — `on:` / `jobs:` / `steps:` 구조 변경 = `extract_steps()` 답습 위반 가능성
- ❌ **fixture 의 `on.push.branches` 영역 변경 (0건)** — `"fixture-only/**"` 답습 보존 (실 trigger 0건 보장)
- ❌ **`tools/mvp1_pc3_ar1_integration_check.py` 본문 변경 (0건)** — W-2 합의 답습 영구
- ❌ **3 MVP-1 workflow Stage 4 step (line 329~341) 변경 (0건)** — W-1 합의 답습 영구
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **신규 workflow 신설 (0건)** + **`pull_request_target` 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 분리
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습
- ❌ **`permissions: contents: read` 보강 (0건)** — W-5 영역 = Stage 5 cycle 4 / Backlog #1+#2 분리
- ❌ **Required check 등록 (0건)** — W-6 영역 = Backlog #3 T3 분리
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 (0건)** — Backlog #1+#2+#3 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 영역
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정 답습
- ❌ **실 secret material commit (0건)** — fixture 의 모든 sample command = 정적 verifier 입력 한정 (실 실행 0건)
- ❌ **Layer A / B / C / D / E / F 재발효 / 재선언 / 발효 (0건)** — Stage 4 entry brief §1.5 답습
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)** — 별도 commit 분리 (사용자 명시 결정 후 진입)
- ❌ **git commit / push (0건)** — 사용자 명시 결정 후 진입
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **token rotation 정책 / GitHub plan 가용성 자동 결정 (0건)** — Group α C-3 + C-4 답습
- ❌ **threshold *고정* (0건)** — coverage / FAIL rate / runtime 모두 *후보 한정* 유지 (C-υ-18 답습)
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **합산 503 합의 조건 자동 변경 (0건)** — 35 신규 (C-χ-1 ~ C-χ-35) + 468 기존 모두 영구 답습
- ❌ **W-1 = 0-line passthrough 고정 (C-φ-30) 변경 (0건)** — W-1 합의 답습 한정
- ❌ **W-2 = 0-line passthrough 고정 (C-χ-35) 변경 (0건)** — W-2 합의 답습 한정
- ❌ **W-2 brief 10 caveat 변경 (0건)** — W-2 합의 §2.3 답습
- ❌ **LVE 3/3 fixture PASS evidence 자동 재집계 (0건)** — `4ce5a0b` 답습 한정

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) 3 fixture (`compliant_entry_step.yml` 30 + `pc3_violation_continue_on_error.yml` 31 + `ar1_violation_no_fail_closed.yml` 28) 어느 줄도 *변경* 하지 않으며,
- (ii) W-4 어느 작업도 *진입* 시키지 않으며,
- (iii) 합산 503 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iv) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (v) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (vi) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vii) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (viii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (ix) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 답습 영구),
- (x) 3 MVP-1 workflow 본문 1206줄 어느 줄도 *변경* 하지 않으며 (W-1 답습 영구),
- (xi) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (xii) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (xiii) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 어느 것도 *발화* 시키지 않으며,
- (xiv) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (xv) W-3 micro-patch 변경 line / 수정 영역 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정),
- (xvi) fixture semantics (entry step name / PASS rc=0 / FAIL rc=1 expected / fixture-only branch / YAML schema) 어느 것도 *변경* / *재해석* 하지 않으며,
- (xvii) 신규 fixture 추가 / fixture 삭제 어느 것도 *발효* 시키지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **W-3 단독 micro-patch *가능성* (= 변경 0 lines 우선 vs 후보 ≤ 6 lines comment/blank/header 한정) 검토 권고 한정**. 모든 *확정 발효* / *실 변경* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (W-2 brief 합의 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS — **3 fixture 3/3 PASS 포함**) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 — 31 조건 C-σ-1 ~ C-σ-31 | ✅ 답습 한정 |
| `27351ce` (2026-05-17) | Phase α-4 R-1 Stage 3 실 진입 여부 brief (722줄) | ✅ 답습 한정 |
| `d3f6d59` (2026-05-17) | Phase α-4 R-1 Stage 3 합의 — 36 조건 C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| `630e125` (2026-05-17) | CONTEXT — Stage 3 entry status | ✅ 답습 한정 |
| `9c33efe` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief (1032줄 DRAFT) | ✅ 답습 한정 |
| `81472ba` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief 풀 3+1 합의 — 49 조건 C-υ-1 ~ C-υ-49 | ✅ 답습 한정 |
| `e279958` (2026-05-18) | CONTEXT — Stage 4 entry status | ✅ 답습 한정 |
| `7af77fb` (2026-05-18) | Phase α-4 R-1 Stage 4 W-1 micro-patch brief (868줄 DRAFT) | ✅ 답습 한정 |
| `df741a2` (2026-05-18) | Phase α-4 R-1 Stage 4 W-1 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 30 조건 C-φ-1 ~ C-φ-30 | ✅ 답습 한정 |
| `637a8cf` (2026-05-18) | CONTEXT — W-1 micropatch status | ✅ 답습 한정 |
| `557c607` (2026-05-18) | Phase α-4 R-1 Stage 4 W-2 micro-patch brief (1009줄 DRAFT) | ✅ 답습 한정 |
| `310b518` (2026-05-18) | Phase α-4 R-1 Stage 4 W-2 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 35 조건 C-χ-1 ~ C-χ-35 | ✅ **본 brief 의 발효 trigger** |
| `096e15a` (HEAD, 2026-05-18) | CONTEXT — W-2 micropatch status | ✅ 답습 한정 |

### 1.2 W-2 brief 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-18 후속 30 |
| 합의 형태 | **Reviewer-only 단축 합의** (Agent A + B + C 미가동 — T-2 재발화 영역 한계 + 풀 3+1 트리거 새 발화 0/16) |
| 합의 판정 | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** — BLOCK 사유 0건 |
| 합의 조건 | **35 조건 (C-χ-1 ~ C-χ-35)** — W-2 brief §11.2 답습 34 + 합의 신규 1 (C-χ-35 "W-2 = 0-line passthrough 고정") |
| W-3 핵심 답습 (cycle 3/4 발효 영역) | C-χ-1 ~ C-χ-35 모두 답습 + 본 brief = cycle 3/4 진입 (C-υ-43 답습 — "W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록") |
| 10 caveat 명시 의무 (사용자 명시) | (1) W-2 범위 = integration tool 298줄 micro-patch 검토 + (2) 권고 결론 = 0-line passthrough + (3) 실 tool 변경 0건 + (4) 실 CI workflow 변경 0건 (W-1 답습 영구) + (5) actual run 재실행 0건 + (6) W-3/W-4 진입 0건 + (7) W-5~W-10 진입 0건 + (8) tool behavior 변경 영구 비권고 (C-χ-31) + (9) tool dependency/entry point 변경 영구 비권고 (C-χ-32+33) + (10) LVE 12/12 PASS evidence 보존 의무 영구 (C-χ-34) |
| 풀 3+1 트리거 발화 | 0/16 새 발화 (T-2 = Stage 4 entry brief 시점 + W-1 합의 시점 이미 답습 영역 완료) |
| 본 brief trigger 의미 | **W-2 cycle 2/4 = 0-line passthrough 합의 발효** → cycle 3/4 (W-3 3 fixture) 진입 = 본 brief DRAFT |

### 1.3 9 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 | "*Can* we enter Phase α-4?" |
| α-4 Stage 1.5 (조건 재검토) | 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (Step 분할) | Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 | "*How* should it be staged?" |
| α-4 Stage 2.5 (LVE) | Local Validation Evidence | `4ce5a0b` + `b264580` | APPROVE | 31 | "*Has local validation evidence been compiled?*" |
| α-4 Stage 3 (실 진입 여부) | Stage 3 brief | `27351ce` + `d3f6d59` | APPROVE AS BRIEF | 36 | "*Should* we enter actual implementation now?" |
| α-4 Stage 4 entry (lockdown) | Stage 4 entry brief | `9c33efe` + `81472ba` | APPROVE AS BRIEF WITH CONDITIONS | 49 | "*What exactly* will Stage 4 W-1~W-4 do?" |
| α-4 Stage 4 W-1 (cycle 1/4) | W-1 micro-patch brief | `7af77fb` + `df741a2` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 30 | "*Should* W-1 introduce micro-patch lines, or is 0-line passthrough correct?" |
| α-4 Stage 4 W-2 (cycle 2/4) | W-2 integration tool micro-patch brief | `557c607` + `310b518` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 35 | "*Should* W-2 introduce micro-patch lines on integration tool, or is 0-line passthrough correct?" |
| **α-4 Stage 4 W-3 (본 brief, cycle 3/4)** | **W-3 3 fixture micro-patch brief** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* W-3 introduce micro-patch lines on 3 fixture, or is 0-line passthrough correct for the fixtures at this gate?"** |
| α-4 Stage 4 W-3 실 micro-patch (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* the chosen patch (if any)" |
| α-4 Stage 4 W-4 (cycle 4/4) | W-4 actual run trigger brief | (미정) | (미정) | (미정) | "*Should* W-4 trigger a fresh actual run?" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 4 W-3 cycle 3/4 framing** (Stage 4 entry brief §8 권고 시작점 답습 + C-υ-43 4 cycle 옵션 정식 등록 답습 + W-1 + W-2 합의 발효 후속):

- α-4 Stage 1 ↔ 1.5 ↔ 2 ↔ 2.5 ↔ 3 ↔ Stage 4 entry ↔ **W-1 (cycle 1/4, 0-line passthrough 확정)** ↔ **W-2 (cycle 2/4, 0-line passthrough 확정)** ↔ **W-3 micro-patch (본 brief, cycle 3/4)** ↔ W-3 실 micro-patch (사용자 결정) ↔ W-4 trigger brief (cycle 4/4)
- 본 brief 의 단일 책무: **"3 fixture 의 minimum micro-patch *possibility* 검토 + 변경 0 lines 우선 권고 vs 후보 ≤ 6 lines (comment / blank-line / header 한정) enumerate"** + **"실 변경 자동 진입 0건"** + **"fixture semantics 변경 0건 영구 답습"**
- 본 brief ≠ W-3 실 micro-patch (fixture 본문 변경 + commit = 별도 cycle 영역)
- 본 brief ≠ W-1 / W-2 재진입 (W-1 / W-2 = 0-line passthrough 고정 답습)
- 본 brief ≠ W-4 brief
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-19 후속 31 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 5 금지 #5 영구 답습) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 5 금지 #5 영구 답습) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 |
| Phase α-4 Stage 4 entry (R-1) | W-1~W-4 lockdown 합의 발효 | ✅ `81472ba` 답습 (49 조건) |
| Phase α-4 Stage 4 W-1 | 3 MVP-1 workflow = 0-line passthrough 합의 발효 | ✅ `df741a2` 답습 (30 조건) |
| Phase α-4 Stage 4 W-2 | integration tool = 0-line passthrough 합의 발효 | ✅ `310b518` 답습 (35 조건) |
| **Phase α-4 Stage 4 W-3 (본 brief)** | **3 fixture micro-patch *가능성 검토*** | ⏳ **본 brief = DRAFT (cycle 3/4)** |

---

## 2. W-3 영역 한정 매트릭스

### 2.1 W-3 단독 영역 enumerate (Stage 4 entry brief §2.1 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-1 | 3 MVP-1 workflow 본문 (`secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 = 1206줄) | ❌ 본 brief 영역 외 (W-1 = **0-line passthrough 고정** 답습, `df741a2` C-φ-30) |
| W-2 | integration check tool 본문 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄) | ❌ 본 brief 영역 외 (W-2 = **0-line passthrough 고정** 답습, `310b518` C-χ-35) |
| **W-3** | **3 fixture 본문 (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄)** | ✅ **본 brief = micro-patch *가능성 검토* 한정 (cycle 3/4)** |
| W-4 | 신규 actual GitHub Actions run trigger (push event) | ❌ 본 brief 영역 외 (사용자 명시 #4 — cycle 4/4 별도 brief 영역) |

### 2.2 W-1 + W-2 답습 + W-4 분리 명시 (위반 0건 영구 답습)

| 영역 | W-1 brief 시점 (cycle 1/4) | W-2 brief 시점 (cycle 2/4) | 본 brief 시점 (cycle 3/4) |
|---|------------|------------|------------|
| W-1 | 단독 cycle = 가능성 검토 | ✅ 0-line passthrough 합의 답습 영구 | ✅ 0-line passthrough 합의 답습 영구 (재진입 0건) |
| W-2 | 분리 명시 | 단독 cycle = 가능성 검토 | ✅ 0-line passthrough 합의 답습 영구 (재진입 0건) |
| **W-3** | 분리 명시 | 분리 명시 | ✅ **본 brief 영역** |
| W-4 | 분리 명시 | 분리 명시 | ❌ 본 brief 영역 외 (cycle 4/4 별도) |
| **합산** | W-1 = 0-line passthrough 확정 | W-1 + W-2 = 0-line passthrough 확정 | **W-3 = 본 brief 영역 + W-1 + W-2 답습 + W-4 분리 ✅** |

### 2.3 W-5 ~ W-10 분리 매트릭스 (Stage 4 entry brief §2.2 답습 — 위반 0건 영구 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-5 | 3 MVP-1 workflow `permissions: contents: read` 보강 | ❌ 본 brief 영역 외 (Stage 5 cycle 4 — Backlog #1+#2 분리) |
| W-6 | 3 MVP-1 workflow Required check 등록 | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-7 | PC-4 local pre-commit hook 활성화 | ❌ 본 brief 영역 외 (Backlog #1+#2 분리) |
| W-8 | AR-2 branch protection rule | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-9 | AR-3 자동 revert bot | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-10 | Stage 5 (G3-7 4 항목) 진입 | ❌ 본 brief 영역 외 (Stage 5 분리) |

### 2.4 본 §2 의 *범위 한계*

본 §2 = **W-3 단독 영역 *권고 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). W-1 + W-2 재진입 + W-4 + W-5 ~ W-10 어느 것도 본 brief 가 *통합* 시키지 않는다.

---

## 3. 3 fixture 현재 상태 매트릭스 (read-only)

### 3.1 3 fixture 본문 구조 매트릭스 (89줄 답습)

#### 3.1.1 `tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml` (30줄)

| 영역 | line 범위 | 줄수 | 답습 내용 |
|------|---------|----|--------|
| 답습 출처 주석 헤더 | 1~8 | 8 | fixture 의도 + PASS expected + entry step 식별 trigger + `continue-on-error: true` 부재 + `set -e` / `exit 1` 양방향 fail-closed semantics |
| blank line | 9 | 1 | 헤더와 본문 분리 |
| `name:` | 10 | 1 | "Fixture — PC-3 + AR-1 compliant entry step (PASS)" |
| blank line | 11 | 1 | name 과 trigger 분리 |
| `on:` trigger block | 12~15 | 4 | `push.branches: ["fixture-only/**"]` (실 trigger 0건 영구 보장) |
| blank line | 16 | 1 | trigger 와 jobs 분리 |
| `jobs:` block (job `fixture_pass`) | 17~30 | 14 | `runs-on: ubuntu-latest` + `steps:` × 1 step (`MVP-1 entry — sample compliant scanner check` + `set -e` + `exit 1` 명시 — AR-1 PASS) |
| **합산** | — | **30** | **✅ 100% read-only 답습** |

#### 3.1.2 `tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` (31줄)

| 영역 | line 범위 | 줄수 | 답습 내용 |
|------|---------|----|--------|
| 답습 출처 주석 헤더 | 1~8 | 8 | fixture 의도 + FAIL expected (PC-3 violation) + `continue-on-error: true` 적용 → PC-3 FAIL + `set -e` 존재 (AR-1 PASS) — PC-3 단일 검출 시연 |
| blank line | 9 | 1 | 헤더와 본문 분리 |
| `name:` | 10 | 1 | "Fixture — PC-3 violation (continue-on-error true)" |
| blank line | 11 | 1 | name 과 trigger 분리 |
| `on:` trigger block | 12~15 | 4 | `push.branches: ["fixture-only/**"]` (실 trigger 0건 영구 보장) |
| blank line | 16 | 1 | trigger 와 jobs 분리 |
| `jobs:` block (job `fixture_fail_pc3`) | 17~31 | 15 | `runs-on: ubuntu-latest` + `steps:` × 1 step (`MVP-1 entry — broken pc3 scanner` + **`continue-on-error: true`** + `set -e` (AR-1 OK)) |
| **합산** | — | **31** | **✅ 100% read-only 답습** |

#### 3.1.3 `tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml` (28줄)

| 영역 | line 범위 | 줄수 | 답습 내용 |
|------|---------|----|--------|
| 답습 출처 주석 헤더 | 1~8 | 8 | fixture 의도 + FAIL expected (AR-1 violation) + `continue-on-error: true` 부재 (PC-3 PASS) + `set -e` / `exit 1` 부재 → AR-1 FAIL |
| blank line | 9 | 1 | 헤더와 본문 분리 |
| `name:` | 10 | 1 | "Fixture — AR-1 violation (no fail-closed pattern)" |
| blank line | 11 | 1 | name 과 trigger 분리 |
| `on:` trigger block | 12~15 | 4 | `push.branches: ["fixture-only/**"]` (실 trigger 0건 영구 보장) |
| blank line | 16 | 1 | trigger 와 jobs 분리 |
| `jobs:` block (job `fixture_fail_ar1`) | 17~28 | 12 | `runs-on: ubuntu-latest` + `steps:` × 1 step (`MVP-1 entry — broken ar1 scanner` + `set -e` 부재 + `exit 1` 부재 + `\|\| echo "ignored"` fail-closed 무력화 패턴) |
| **합산** | — | **28** | **✅ 100% read-only 답습** |

#### 3.1.4 3 fixture 합산

| fixture | line | 답습 |
|--------|----|----|
| `pass/compliant_entry_step.yml` | 30 | PASS expected (rc=0) |
| `fail/pc3_violation_continue_on_error.yml` | 31 | FAIL expected (rc=1, PC-3 violation) |
| `fail/ar1_violation_no_fail_closed.yml` | 28 | FAIL expected (rc=1, AR-1 violation) |
| **합산** | **89** | **3/3 LVE PASS 답습** |

### 3.2 fixture 호출 인터페이스 매트릭스 (Stage 4 step 답습)

| 인터페이스 | 호출 위치 | 본 brief 답습 |
|---------|--------|----------|
| `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml --mode integration` | 3 MVP-1 workflow Stage 4 step line 330 (자동 검증) + LVE §3.2.3 self-check | ✅ 답습 — Stage 4 step wired |
| `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml --mode integration` (expected rc=1) | 3 MVP-1 workflow Stage 4 step line 334~338 (FAIL expected guard) + LVE §3.2.3 self-check | ✅ 답습 — Stage 4 step wired (`set -e` + `if rc != 1; then exit 1`) |
| `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml --mode integration` (expected rc=1) | 동상 line 339~341 + LVE §3.2.3 self-check | ✅ 답습 — Stage 4 step wired |
| **합산** | **3 호출 인터페이스** | **✅ 3/3 wired + 4 prerequisite run SUCCESS 답습** |

### 3.3 3 fixture expected behavior 매트릭스

| fixture | 분류 | entry step name | PC-3 (continue-on-error) | AR-1 (fail-closed) | tool expected rc | Stage 4 step 답습 |
|--------|-----|---------------|----------------------|------------------|---------------|--------------|
| `compliant_entry_step.yml` | PASS | "MVP-1 entry — sample compliant scanner check" (✅ 매칭) | ❌ 부재 (PASS) | ✅ `set -e` + `exit 1` (PASS) | **0** | rc=0 expected |
| `pc3_violation_continue_on_error.yml` | FAIL (PC-3) | "MVP-1 entry — broken pc3 scanner" (✅ 매칭) | ✅ `continue-on-error: true` (FAIL) | ✅ `set -e` (PASS) | **1** | rc=1 expected (PC-3 violation 단독) |
| `ar1_violation_no_fail_closed.yml` | FAIL (AR-1) | "MVP-1 entry — broken ar1 scanner" (✅ 매칭) | ❌ 부재 (PASS) | ❌ `set -e` 부재 + `exit 1` 부재 (FAIL) | **1** | rc=1 expected (AR-1 violation 단독) |
| **합산** | — | **3/3 entry pattern 매칭** | **PC-3 검출 1/3** | **AR-1 검출 1/3** | **0+1+1** | **3/3 Stage 4 step expected rc 답습** |

### 3.4 LVE 3/3 fixture PASS evidence 답습 매트릭스 (`4ce5a0b` LVE §3.2.3 답습)

| 검증 영역 | LVE 결과 | 본 brief 답습 |
|---------|-------|----------|
| PASS fixture verify (`compliant_entry_step.yml`, mode=integration) | ✅ PASS (rc=0) | ✅ 답습 한정 |
| FAIL fixture (PC-3) verify (`pc3_violation_continue_on_error.yml`, mode=integration) | ✅ FAIL detected (rc=1, PC-3 violation reported) | ✅ 답습 한정 |
| FAIL fixture (AR-1) verify (`ar1_violation_no_fail_closed.yml`, mode=integration) | ✅ FAIL detected (rc=1, AR-1 violation reported) | ✅ 답습 한정 |
| **합산** | **3/3 PASS** | **✅ 100% 답습 한정** |

추가 답습 (LVE 12/12 PASS 중 fixture 관련 영역):
- 한국어 shell comment FAIL fixture 안전성 ✅ PASS (`_strip_comments` heuristic 답습)
- missing file 처리 ✅ rc=1 + `::error::file not found:`
- no entry step 처리 ✅ rc=1 + `::error::no entry steps found`

### 3.5 4 prerequisite run answer 답습 (W-2 brief §3.6 답습)

| 영역 | 답습 |
|------|----|
| Stage 4 step 본문 = 이미 wired (`secret-hygiene-egress-redaction.yml` line 318~360 + 2 workflow 동일) | ✅ W-1 = 0-line passthrough 합의 답습 |
| 3 MVP-1 workflow 4 prerequisite run SUCCESS (Phase α-1/α-2/α-3) | ✅ LVE §4 답습 |
| integration tool 본문 답습 (298줄) | ✅ W-2 = 0-line passthrough 합의 답습 |
| **fixture 본문 변경 = LVE 3/3 PASS evidence + integration tool behavior 답습 변경 가능성 영역** | ⚠️ **본 brief 핵심 평가 영역** — semantics 변경 시 → 3/3 PASS evidence 변경 위험 |

### 3.6 본 §3 의 *범위 한계*

본 §3 = **read-only 답습 매트릭스 한정**. 본 §3 의 어떤 항목도 *변경* / *재해석* / *재합의* 영역이 아니며, 단순히 *현재 상태* 답습 enumerate 한정. fixture 본문 변경 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. Micro-patch 후보 영역 *enumerate 한정*

### 4.1 변경 line 결정 옵션 매트릭스 (C-υ-44 + C-φ-30 + C-χ-35 동시 답습)

C-υ-44 답습 결정 영역 (Stage 4 entry brief 합의 §5.3 답습) + C-φ-30 답습 (W-1 = 0-line passthrough 고정) + C-χ-35 답습 (W-2 = 0-line passthrough 고정) = **4 영역 동시 발효**:

| Agent 영역 | 권고 | 본 brief 채택 영역 |
|---------|----|---------------|
| Agent A (절차) — C-A6 | W-N micro-patch 범위 결정 = *별도 brief 후 합의* | ✅ **본 brief = cycle 3/4 별도 brief 진입** (C-A6 발효) |
| Agent B (안전성) — C-B6 | PC-3 / AR-1 step 순서 변경 = §5.5.1+§5.5.2 본문 변경 시도 *권고 0건* 영구 답습 (T-3 발화 영역 모호성 청산) | ✅ **본 brief = fixture semantics 변경 0건 영구 답습 + 변경 영역 = comment / blank-line / header 한정 영구 답습** |
| Agent C (단순성) — C-C1 | 변경 line *0 lines 우선 권고 강화* | ✅ **본 brief 권고 시작점 = (i) 변경 0 lines 우선 권고** |
| **W-1 + W-2 합의 답습 C-φ-30 + C-χ-35** | W-1 + W-2 = 0-line passthrough 고정 (LVE evidence + 4 prerequisite run SUCCESS) | ✅ **본 brief 권고 시작점 = (i) fixture 본문 변경 0 lines 우선 (LVE 3/3 PASS evidence + 답습 패턴 영구 답습)** |

### 4.2 변경 line 결정 옵션 (사용자 결정 영역)

| 옵션 | 변경 line | 적격 영역 | 본 brief 권고 |
|-----|--------|--------|----------|
| **(i)** | **0 lines** | 3 fixture (89줄) = 현재 상태 답습 (Stage 4 step wired + LVE 3/3 PASS + 4 prerequisite run SUCCESS) | ✅ **권고 시작점 (C-υ-44 + C-φ-30 + C-χ-35 답습 — 변경 0 lines 우선)** |
| (ii) | ≤ 2 lines | 답습 출처 주석 헤더 보강 — W-1 + W-2 합의 commit (`df741a2` + `310b518`) 답습 추가 (boilerplate 2 라인) | 옵션 (사용자 결정 영역) — comment-only 변경 한정 (3 fixture 中 1+ 선택 가능) |
| (iii) | ≤ 4 lines | (ii) + fixture 시그니처 일관성 보강 (예: 3 fixture 모두 동일 `# 본 fixture 는 실 workflow 가 아니며` 보강) | 옵션 (사용자 결정 영역) — comment-only 변경 한정 |
| (iv) | ≤ 6 lines | (iii) + `name:` 필드 일관성 정정 (예: prefix 통일 — 단, entry step 의 `name` 변경 ≠ entry step body 의 `name` 변경) | 옵션 (사용자 결정 영역) — fixture name top-level 변경 한정 (entry step name 변경 0건 영구 답습) |
| (v) | ≥ 7 lines | Stage 4 entry brief §3.3 답습 영역 외 (별도 합의 필요) | ❌ **비권고** |
| (vi) | **entry step name / continue-on-error / set -e / exit 1 / fail-closed 패턴 변경** (semantics change) | 3 fixture expected behavior (PC-3 / AR-1 detect / rc=0/1) 변경 영역 | ❌ **비권고** (C-υ-44 답습 — T-3 발화 영역 — **3/3 PASS evidence 변경 위험 + Stage 4 step rc=1 expected 답습 위반**) |
| (vii) | **신규 fixture 추가 OR fixture 삭제** | 3 fixture → 2 또는 4+ 변경 = LVE 영역 변경 (재집계 의무 발화) | ❌ **비권고** (LVE 3/3 PASS evidence 변경 위험 + Stage 4 step 호출 인터페이스 답습 위반 가능성) |
| (viii) | **`on.push.branches` 영역 변경** | `"fixture-only/**"` 답습 보존 ↔ 실 trigger 0건 보장 위반 | ❌ **비권고** (fixture = 정적 verifier 입력 한정 답습 위반 영역) |
| (ix) | **YAML schema 변경** (예: `jobs:` 구조 / `steps:` 구조 / `runs-on:` 변경) | `extract_steps()` heuristic 답습 위반 영역 | ❌ **비권고** (integration tool W-2 답습 + LVE evidence 변경 위험) |

### 4.3 옵션 (ii)~(iv) 의 *근거 영역* enumerate (참고 한정)

본 §4.3 = 옵션 (ii)~(iv) 의 *근거 enumerate 한정* — 채택 권고 0건. 변경 line 결정 = 사용자 명시 결정 영역.

**옵션 (ii) 근거 (답습 출처 헤더 주석 보강 가능성)**:
- 현재 3 fixture 답습 출처 헤더 (line 1~8) = fixture 의도 + expected behavior 명시 — W-1 + W-2 합의 답습 미반영
- W-2 합의 발효 후 답습 출처 갱신 가능성 = 1~2 lines 추가 (boilerplate comment 한정, 예: `# W-1 0-line passthrough 답습 (`df741a2`) + W-2 0-line passthrough 답습 (`310b518`)`)
- 본 brief 권고: ❌ **비권고 (default)** — 답습 출처 = 새 합의 시점 별도 갱신 영역 (자동 진입 X) + behavior 변경 0건 보장 가능 시에만 검토

**옵션 (iii) 근거 (fixture 시그니처 일관성 보강 가능성)**:
- 현재 3 fixture 모두 헤더 line 8 에 동일 패턴 `# 본 fixture 는 실 workflow 가 아니며 (CI 실행 0건) — 정적 verifier 입력 데이터 한정` (PASS) 또는 `# 본 fixture 는 실 workflow 가 아니며 — 정적 verifier negative case 데이터` (FAIL × 2)
- PASS fixture 와 FAIL fixture 간 미세 차이 ("CI 실행 0건" 부재 in FAIL) — 일관성 보강 가능성 1~2 lines (comment-only)
- 본 brief 권고: 옵션 (사용자 결정 영역) — comment-only 변경 한정 → behavior 변경 0건

**옵션 (iv) 근거 (top-level `name:` 일관성 정정 가능성)**:
- 현재 3 fixture top-level `name:` = "Fixture — PC-3 + AR-1 compliant entry step (PASS)" / "Fixture — PC-3 violation (continue-on-error true)" / "Fixture — AR-1 violation (no fail-closed pattern)"
- 패턴 일관성 미세 차이 — 일관성 정정 가능성 ≤ 2 lines (예: 모두 동일 `[expected: ...]` suffix 추가)
- 단, **entry step 의 `- name:` 필드는 `ENTRY_NAME_PATTERNS` 매칭 영역** → 변경 시 옵션 (vi) (semantics change) 영역 진입 → 본 brief 비권고
- 본 brief 권고: 옵션 (사용자 결정 영역) — **top-level `name:` 한정** (entry step `name:` 변경 0건 영구 답습)

### 4.4 영역 외 변경 enumerate (본 brief 비권고 영구 답습)

| 영역 | 사유 |
|------|-----|
| entry step `- name:` 필드 변경 (예: "MVP-1 entry" prefix 제거 / 변경) | `ENTRY_NAME_PATTERNS` 매칭 답습 위반 — LVE 3/3 PASS evidence 변경 위험 (T-3 발화 영역) |
| `continue-on-error: true` 추가 / 제거 | PC-3 expected behavior 변경 영역 — PASS fixture rc 변경 위험 + FAIL fixture detection 변경 위험 (T-3 발화 영역) |
| `set -e` / `exit 1` 추가 / 제거 / 변형 | AR-1 expected behavior 변경 영역 — PASS fixture rc 변경 위험 + FAIL fixture detection 변경 위험 (T-3 발화 영역) |
| `\|\| echo "ignored"` 패턴 변경 (FAIL AR-1 fixture) | AR-1 fail-closed 무력화 시연 영역 — semantics 변경 영역 |
| step `run:` body logic 변경 (예: scanner 호출 변경 / echo 메시지 변경 中 fail-closed 관련 영역) | semantics 변경 영역 — LVE 3/3 PASS evidence 변경 위험 |
| `id:` 필드 변경 | step extraction heuristic 답습 영역 (W-2 = `extract_steps()` 답습 위반 가능성) |
| `jobs:` 구조 변경 (예: 새 job 추가 / job 명 변경 / `runs-on` 변경) | YAML schema 변경 영역 — `extract_steps()` heuristic 답습 위반 영역 |
| `steps:` 다중화 (예: PASS fixture 에 2+ step 추가) | entry step 개수 답습 영역 — LVE 3/3 PASS evidence 변경 위험 (mode=integration 의 ≥ 1 entry step 답습) |
| `on:` event 변경 (예: `pull_request` / `workflow_dispatch` 추가) | 실 trigger 0건 보장 영역 — `"fixture-only/**"` branch 답습 위반 가능성 |
| `on.push.branches` 영역 변경 (예: `"main"` / `"feature/**"` 등 추가) | 실 trigger 0건 보장 영역 위반 — fixture 가 실 CI run 발화 위험 |
| 신규 fixture 추가 (예: PASS fixture 2 / FAIL fixture 3+) | LVE 영역 변경 (3/3 → N/N 재집계 의무 발화) + Stage 4 step 호출 인터페이스 답습 위반 가능성 (현재 = 3 fixture 한정) |
| 기존 fixture 삭제 | 동상 (LVE 영역 축소 + Stage 4 step rc=1 expected 답습 위반) |
| fixture 파일 위치 이동 (예: `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/` 외 디렉토리) | Stage 4 step path 답습 위반 영역 — `tools/mvp1_pc3_ar1_integration_check.py` 인자 path 변경 의무 발화 (W-1 / W-2 0-line passthrough 답습 위반) |
| `tools/mvp1_pc3_ar1_integration_check.py` 본문 변경 (어느 줄도) | W-2 합의 답습 영구 |
| 3 MVP-1 workflow Stage 4 step (line 329~341) 변경 (어느 줄도) | W-1 합의 답습 영구 |
| `permissions: contents: read` 보강 | W-5 영역 = 본 brief 영역 외 |
| Required check / branch protection 등록 | W-6 / W-8 영역 = 본 brief 영역 외 |
| `pull_request_target` event 도입 | Stage 5 cycle 2 영역 = 본 brief 영역 외 |
| `secrets.*` reference 도입 | F-금지 #1 영구 답습 |
| 신규 trigger event (`workflow_dispatch` / `schedule` / `repository_dispatch`) | W-4 영역 = 본 brief 영역 외 |
| 신규 tool / 신규 workflow 신설 | T2/T3 별도 합의 영역 |

### 4.5 변경 line 권고 시작점 매트릭스

| 영역 | 변경 line 권고 시작점 | 사용자 결정 옵션 상한 |
|----------|------------------|-------------------|
| `pass/compliant_entry_step.yml` (30줄) | **0 lines** | ≤ 2 lines (옵션 (iv) — comment-only / top-level name 한정 영구 답습) |
| `fail/pc3_violation_continue_on_error.yml` (31줄) | **0 lines** | ≤ 2 lines (동상) |
| `fail/ar1_violation_no_fail_closed.yml` (28줄) | **0 lines** | ≤ 2 lines (동상) |
| **합산 (3 fixture 89줄)** | **0 lines (권고 시작점)** | **≤ 6 lines (옵션 (iv) 상한, semantics 변경 0건 + entry step name 변경 0건 영구 답습)** |

### 4.6 본 §4 의 *범위 한계*

본 §4 = **변경 line 결정 *옵션 enumerate 한정***. 본 §4 의 어떤 항목도:
- (i) 옵션 (i)~(iv) 中 어느 것도 *채택 발효* 시키지 않으며,
- (ii) 변경 line *최종 확정* 시키지 않으며,
- (iii) 3 fixture 어느 줄도 *변경* 하지 않으며,
- (iv) fixture semantics (entry step name / PC-3 패턴 / AR-1 패턴 / rc expected) 어느 것도 *변경* 하지 않으며,
- (v) 신규 fixture / fixture 삭제 어느 것도 *발효* 시키지 않으며,
- (vi) fixture 파일 위치 어느 것도 *이동* 시키지 않는다.

권고 시작점 = **옵션 (i) 변경 0 lines** (C-υ-44 + C-φ-30 + C-χ-35 답습 + LVE 3/3 PASS evidence 답습 + W-1 + W-2 답습 패턴 영구 답습) — 실 변경 결정 = 사용자 명시 결정 영역.

---

## 5. W-3 검증 방법 권고

### 5.1 PRE-0 도구 가용성 사전 점검 (C-υ-38 답습)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| PRE-0-1 | Python version ≥ 3.12 | `python --version` | rc=0 + ≥ 3.12 |
| PRE-0-2 | `yaml.safe_load` 가용성 (PyYAML, stdlib 대체) | `python -c "import yaml; print(yaml.__version__)"` | rc=0 + version enumerate (W-3 = YAML parse 검증 의존) |
| PRE-0-3 | `git` version | `git --version` | rc=0 + version enumerate |
| PRE-0-4 | `gh CLI` 인증 상태 (옵션) | `gh auth status` | rc=0 + 인증 답습 (PRE 영역 한정 — 신규 actual run trigger 0건) |
| PRE-0-5 | `grep` 가용성 (semantics pattern 답습 검증) | `grep --version` | rc=0 |
| PRE-0-6 | `tools/mvp1_pc3_ar1_integration_check.py` 답습 (W-2 = 0-line passthrough 답습) | `python -m py_compile tools/mvp1_pc3_ar1_integration_check.py` | rc=0 (W-2 답습 영구) |

### 5.2 W-3-V1 ~ W-3-V7 검증 (Stage 4 entry brief §4.2.3 답습 + fixture 특화 확장)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-3-V1 | PASS fixture YAML parse 검증 | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml'))"` | rc=0 + parse 성공 |
| W-3-V2 | FAIL fixture (PC-3) YAML parse 검증 | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml'))"` | rc=0 + parse 성공 |
| W-3-V3 | FAIL fixture (AR-1) YAML parse 검증 | `python -c "import yaml; yaml.safe_load(open('tests/fixtures/mvp1_pc3_ar1_integration/fail/ar1_violation_no_fail_closed.yml'))"` | rc=0 + parse 성공 |
| W-3-V4 | PASS fixture = compliant entry step 시그니처 검증 (W-2 답습) | `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml --mode integration` | rc=0 + violations=0 (LVE §3.2.3 답습) |
| W-3-V5 | FAIL fixture (PC-3) = `continue-on-error: true` 패턴 포함 검증 + tool 통과 | `grep -c "continue-on-error: true" tests/fixtures/mvp1_pc3_ar1_integration/fail/pc3_violation_continue_on_error.yml` + `python tools/mvp1_pc3_ar1_integration_check.py ... --mode integration` | grep match ≥ 1 + tool rc=1 + PC-3 violation reported |
| W-3-V6 | FAIL fixture (AR-1) = `set -e` 부재 + `exit 1` 부재 검증 + tool 통과 | `grep -L "set -e" .../ar1_violation_no_fail_closed.yml` + `grep -L "exit 1" .../ar1_violation_no_fail_closed.yml` + `python tools/...` | grep 미매칭 (둘 다) + tool rc=1 + AR-1 violation reported |
| W-3-V7 | 3 fixture entry step name = "MVP-1 entry" prefix 검증 (`ENTRY_NAME_PATTERNS` 매칭) | `grep -c "name: MVP-1 entry" tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` | 3 fixture 中 3 매칭 |

### 5.3 신규 actual run trigger 검증 매트릭스

| 영역 | 본 brief 권고 |
|------|----------|
| W-4 신규 actual run trigger | ❌ **0건 영구 답습** (사용자 명시 #4 답습) |
| Pre-implementation 검증 = local 한정 | ✅ 신규 actual run trigger 0건 (PRE-0-1 ~ W-3-V7 모두 local 표준 도구 한정) |
| 본 brief 시점 신규 actual run trigger | **0건** |

### 5.4 검증 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `python -c "import yaml; yaml.safe_load(...)"` | YAML parse 검증 (W-3-V1~V3) | 답습 한정 — 신규 도입 0건 (PyYAML 의존 답습) |
| `python tools/mvp1_pc3_ar1_integration_check.py` | tool 자체 fixture 검증 (W-3-V4~V6) | 답습 한정 — 본 brief 시점 변경 0건 (W-2 답습 영구) |
| `grep` | semantics 패턴 답습 검증 (W-3-V5~V7) | 표준 도구 답습 |
| `diff` (옵션) | fixture 본문 답습 변경 확인 (옵션 (i) 채택 시 변경 0 lines verify) | 표준 도구 답습 |
| `gh CLI` (옵션) | 4 prerequisite runs 답습 시점 ↔ 본 brief 시점 시간 경과 재검증 | 답습 한정 (read-only) |
| `yamllint` (옵션) | fixture YAML lint 검증 (W-3-V1~V3 보강) | 답습 한정 — 신규 도입 0건 |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 5.5 LVE 3/3 fixture PASS evidence 답습 검증 (read-only)

| 영역 | 답습 |
|------|----|
| LVE §3.2.3 3/3 PASS | ✅ 답습 한정 — 본 brief 시점 재실행 0건 (옵션 (i) 0 lines = 자동 답습) |
| 본 brief 변경 = LVE 3/3 PASS evidence 변경 위험 | ⚠️ **본 brief 핵심 평가 영역** — 옵션 (vi)~(ix) semantics 변경 시 → LVE 재집계 필요 영역 (T-3 발화 영역) |
| 옵션 (i)~(iv) (comment/blank/top-level name 한정) 변경 시 LVE 영향 | ✅ **0건 영구 답습** (semantics 변경 0건 → 3/3 PASS evidence 보존) |

### 5.6 본 §5 의 *범위 한계*

본 §5 = **W-3 검증 방법 *권고 한정***. 실 검증 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 본 §5 의 어떤 항목도 신규 actual run trigger 0건 영구 답습 + W-1 / W-2 / W-4 검증 영역 *통합 0건*.

---

## 6. W-3 시점 rollback trigger 발화 가능성 매트릭스

### 6.1 Layer B 18 trigger × W-3 시점 발화 매트릭스 (Stage 4 entry brief §6.1 답습)

| # | trigger 영역 | W-3 본문 변경 0 lines 시점 발화 | W-3 본문 변경 ≤ 6 lines (comment/blank/header 한정) 시점 발화 | W-3 본문 변경 옵션 (vi) (semantics change) 시점 발화 |
|---|---------|---------------------------|----------------------------|----------------------------|
| 13 | CI step pass with violation present (PC-3) | 0건 (fixture semantics 변경 0건) | 0건 (semantics 변경 0건) | **발화 가능성** (옵션 (vi) — `continue-on-error: true` 패턴 변경 시 = 비권고 영역) |
| 14 | CI step fail without auto-reject (AR-1) | 0건 (fixture semantics 변경 0건) | 0건 (semantics 변경 0건) | **발화 가능성** (옵션 (vi) — `set -e` / `exit 1` 패턴 변경 시 = 비권고 영역) |
| 15 | PR check unstable / flaky | 0건 (신규 actual run trigger 0건) | 0건 (W-4 영역 외) | 0건 (W-4 영역 외) |
| **합산 (18 중)** | **18 trigger** | **0/18 발화** | **0/18 발화** (comment/blank/header 한정 — semantics 변경 0건) | **2/18 발화 가능성 (옵션 (vi) 한정 — 본 brief 비권고)** |

### 6.2 TR-1 ~ TR-5 × W-3 시점 발화 매트릭스

| TR # | 영역 | W-3 시점 발화 |
|----|----|------------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 | 0건 (Phase α-2 영역) |
| TR-2 | `include_external_packages` flag | 0건 |
| TR-3 | `root_packages` 변경 | 0건 |
| TR-4 | `ignore_imports` 변경 | 0건 |
| TR-5 | google.generativeai facade | 0건 |
| **합산** | **5 trigger** | **0/5 발화 영구 답습** |

### 6.3 Step Division + Stage 4 신규 후보 × W-3 시점 발화 매트릭스

| # | trigger | W-3 본문 변경 0 lines | W-3 본문 변경 ≤ 6 lines (comment/blank/header) | W-3 본문 변경 옵션 (vi)~(ix) (semantics/schema/추가/삭제 change) |
|---|-------|-------------------|-----------------------|-----------------------|
| ND-1 | PC-3 self-check FAIL (local) | 0건 | 0건 (semantics 변경 0건) | **발화 가능성** (옵션 (vi) `continue-on-error` 변경 시 — 비권고) |
| ND-2 | AR-1 self-check FAIL (local) | 0건 | 0건 (semantics 변경 0건) | **발화 가능성** (옵션 (vi) `set -e` / `exit 1` 변경 시 — 비권고) |
| ND-3 | integration check tool self-check FAIL | 0건 (tool 변경 0건 + fixture semantics 변경 0건) | 0건 (comment/blank/header 변경 시 tool behavior 영향 0건) | **발화 가능성** (옵션 (vi)~(ix) 시 — 비권고) |
| ND-4 | 4 prerequisite runs JSON conclusion 미답습 | 0건 (PRE 영역) | 0건 | 0건 |
| ND-5 | LVE 본문 누락 | 0건 (PRE 영역) | 0건 | 0건 |
| **합산** | **5 후보** | **0/5 발화** | **0/5 발화** (comment/blank/header 한정 — tool behavior 영향 0건) | **3/5 발화 가능성 (옵션 (vi)~(ix) 한정 — 본 brief 비권고)** |

### 6.4 W-3 시점 발화 합산 매트릭스

| 옵션 | Layer B | TR-1~5 | Step Division 신규 | 합산 발화 가능성 |
|-----|---------|------|----------------|--------------|
| **(i) 0 lines (권고 시작점)** | 0/18 | 0/5 | 0/5 | **0/28 발화 영구 답습** |
| (ii) ≤ 2 lines (답습 출처 헤더 보강) | 0/18 | 0/5 | 0/5 | **0/28 발화** (comment-only — semantics 0건) |
| (iii) ≤ 4 lines (fixture 시그니처 일관성) | 0/18 | 0/5 | 0/5 | **0/28 발화** (comment-only — semantics 0건) |
| (iv) ≤ 6 lines (top-level `name:` 일관성) | 0/18 | 0/5 | 0/5 | **0/28 발화** (top-level `name:` = `extract_steps()` 영향 0건 — entry step `name:` 변경 0건 보장 시) |
| (v) ≥ 7 lines | (영역 외 — 별도 합의) | (영역 외) | (영역 외) | **본 brief 비권고** |
| (vi) semantics change (entry step name / continue-on-error / set -e / exit 1) | 2/18 (#13 + #14) | 0/5 | 3/5 (ND-1 + ND-2 + ND-3) | **5/28 발화 가능성 — 본 brief 비권고 영역** |
| (vii) 신규 fixture 추가 / fixture 삭제 | 0/18 (직접 영향 0) | 0/5 | 1/5 (ND-3) + LVE 영역 변경 (재집계) | **본 brief 비권고** |
| (viii) `on.push.branches` 변경 | (영역 외 — fixture 실 trigger 0건 보장 위반) | (영역 외) | (영역 외) | **본 brief 비권고** |
| (ix) YAML schema 변경 | (영역 외 — `extract_steps()` 답습 위반) | (영역 외) | 1/5 (ND-3) | **본 brief 비권고** |

**핵심 발견**: 옵션 (i)+(ii)+(iii)+(iv) 영역 = **0/28 발화 영구 답습**. 옵션 (vi) (semantics change) 영역 = 5/28 발화 가능성 — **본 brief 비권고** (C-υ-44 + C-φ-30 + C-χ-35 답습 + Agent B C-B6 + Agent C C-C1 + Reviewer §4.4 답습 + LVE 3/3 PASS evidence 답습). 옵션 (vii)~(ix) = 추가 영역 비권고.

### 6.5 Rollback 절차 권고 (C-υ-41 답습 — "즉시 rollback" 권고 한정)

| 절차 | 영역 | 권고 |
|----|----|----|
| (i) Rollback decision | trigger 발화 시 판단 | **사용자 명시 결정 영역** (자동 rollback 0건 영구 답습) |
| (ii) `git revert HEAD` | 가장 안전 — 변경 line 만 revert | **권고 시작점** |
| (iii) `git reset --hard HEAD~N` | 강제 reset (이력 변경) | ❌ **비권고** (R-4 history rewrite layer 영역) |
| (iv) 신규 `fix:` commit (revert 없이 forward fix) | micro patch forward fix | 옵션 (comment/blank/header 한정 변경 시) |
| (v) 본 brief 시점 = 변경 line 0 = rollback 영역 0건 영구 답습 | — | **답습 한정** |
| (vi) LVE 3/3 PASS evidence 재집계 의무 발화 시점 | 옵션 (vi)~(ix) semantics/schema 변경 채택 시 = LVE 재집계 의무 발화 (T-3 영역) | ❌ **비권고** (본 brief = semantics 변경 0건 영구 답습) |

### 6.6 본 §6 의 *범위 한계*

본 §6 = **rollback trigger *발화 가능성 enumerate 한정***. 본 §6 의 어떤 항목도 *발화* / *rollback 절차 자동 발효* / *threshold 고정* 시키지 않는다.

---

## 7. 사용자 명시 5 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 5 금지 영역 위반 0건 영구 답습

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 결정 영역) |
|---|---------|---------------|------------------------------|
| #1 | 3 fixture 실 변경 | ✅ 0건 (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄 변경 0건 — 본 brief = *후보 검토 한정*) | ✅ 0건 (DRAFT 영역, 사용자 결정 후 진입) |
| #2 | CI workflow 변경 | ✅ 0건 (W-1 = 0-line passthrough 고정 답습 영구) | ✅ 0건 (W-1 합의 답습 영구) |
| #3 | integration tool 변경 | ✅ 0건 (W-2 = 0-line passthrough 고정 답습 영구) | ✅ 0건 (W-2 합의 답습 영구) |
| #4 | actual run 재실행 | ✅ 0건 (신규 trigger 0건) | ✅ 0건 (W-4 영역 외 영구 답습) |
| #5 | Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) | ✅ 0건 (MVP-6 / ADR-008 부록 C 12 조건 미진입) | ✅ 0건 |
| **합산** | **5** | **✅ 5/5 위반 0건** | **✅ 5/5 위반 0건** |

### 7.2 W-3 옵션별 5 금지 위반 매트릭스

| 옵션 | #1 | #2 | #3 | #4 | #5 | 합산 |
|-----|----|----|----|----|----|-----|
| (i) 0 lines | ✅ 0 (현재 상태 답습) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건** |
| (ii)~(iv) comment/blank/header ≤ 6 lines | ✅ 0 (본 brief 시점) — Stage 4 실 구현 시점 = #1 해소 (사용자 결정) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건 (본 brief 시점)** |
| (v) ≥ 7 lines | ❌ **위반 가능성** (Stage 4 entry brief §3.3 답습 영역 외 — 별도 합의 필요) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (vi) semantics change | ❌ **위반 가능성** (§5.5.1+§5.5.2 본문 변경 영역 — C-υ-44 답습 비권고 + LVE evidence 변경 위험) | ✅ 0 | ⚠️ 위반 가능성 (tool behavior 답습 변경 = W-2 답습 위반) | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (vii) 신규 fixture 추가 / 삭제 | ❌ **위반 가능성** (LVE 영역 변경 = 재집계 의무) | ✅ 0 | ⚠️ 위반 가능성 (tool 호출 인터페이스 답습 변경 = W-2 답습 위반 가능) | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (viii) `on.push.branches` 변경 | ❌ **위반 가능성** (실 trigger 0건 보장 위반) | ⚠️ 위반 가능성 | ✅ 0 | ⚠️ 위반 가능성 (W-4 영역 자동 trigger 위험) | ✅ 0 | **본 brief 비권고** |
| (ix) YAML schema 변경 | ❌ **위반 가능성** (`extract_steps()` 답습 위반) | ✅ 0 | ⚠️ 위반 가능성 (tool behavior 변경 가능) | ✅ 0 | ✅ 0 | **본 brief 비권고** |

### 7.3 Backlog 분리 매트릭스

| Backlog | 영역 | 본 brief 영역 |
|---------|----|----------|
| Backlog #1 (PC-4 local pre-commit hook 활성화) | `.pre-commit-config.yaml` 신설 | ❌ 본 brief 영역 외 (W-7) |
| Backlog #2 (dev 환경 강제 + pre-commit install 의무화) | dev 환경 검증 강제 | ❌ 본 brief 영역 외 (W-7 영역) |
| Backlog #3 T3 (AR-2 branch protection + AR-3 자동 revert bot) | branch protection API + CODEOWNERS | ❌ 본 brief 영역 외 (W-6 + W-8 + W-9 영역) |
| Backlog #4 (facade.py real 본문 작성) | `src/adapters/llm/facade.py` real 본문 | ❌ 본 brief 영역 외 |
| Backlog #5 (event enum / ledger entry 정식 등록) | ADR-012 §2.2 영역 | ❌ 본 brief 영역 외 (후보 한정) |
| Backlog #6 (Hermes PMO 격상 영역) | ADR-008 부록 C 12 조건 영역 | ❌ 본 brief 영역 외 |
| Stage 5 (G3-7 4 항목) | secret reset rotate / fork PR / pull_request_target / commit signing | ❌ 본 brief 영역 외 (W-10 영역) |
| **W-1 cycle 1/4 (3 MVP-1 workflow micro-patch)** | 3 workflow 1206줄 | ❌ 본 brief 영역 외 (cycle 1/4 답습 — 0-line passthrough 고정 영구) |
| **W-2 cycle 2/4 (integration tool micro-patch)** | tool 298줄 | ❌ 본 brief 영역 외 (cycle 2/4 답습 — 0-line passthrough 고정 영구) |
| **W-4 cycle 4/4 (actual run trigger)** | 신규 trigger | ❌ 본 brief 영역 외 (cycle 4/4 별도) |

### 7.4 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 5 금지 영역 + Backlog 분리 영역 + W-1 / W-2 / W-4 cycle 분리 영역 어느 것도 *해소* / *통합* 시키지 않는다.

---

## 8. 합산 503 합의 조건 답습 매트릭스

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
| Phase α-4 R-1 Stage 3 실 진입 여부 | `d3f6d59` | 36 (C-τ-1 ~ C-τ-36) | 0건 |
| Phase α-4 R-1 Stage 4 entry | `81472ba` | 49 (C-υ-1 ~ C-υ-49) | 0건 |
| Phase α-4 R-1 Stage 4 W-1 | `df741a2` | 30 (C-φ-1 ~ C-φ-30) | 0건 |
| **Phase α-4 R-1 Stage 4 W-2** | **`310b518`** | **35 (C-χ-1 ~ C-χ-35)** | **0건** ✅ |
| **합산** | **18 합의** | **503 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| C-υ-43 (W-1/W-2/W-3 4 cycle 옵션 정식 등록) 발효 — 본 brief = cycle 3/4 진입 | ✅ §1.4 + §8.2 답습 |
| C-υ-44 (Agent A + B + C 동시 발효 — micro-patch 별도 brief + 본문 변경 시도 권고 0건 + 변경 line 0 lines 우선 권고 강화) | ✅ §4.1 + §4.2 답습 (변경 0 lines 우선 권고 시작점) |
| C-υ-38 (PRE-0 도구 가용성 사전 점검 의무) | ✅ §5.1 답습 |
| C-φ-30 (W-1 = 0-line passthrough 고정 영구) | ✅ §1.2 + §8.2 답습 (3 workflow 1206줄 변경 0건 영구) |
| **C-χ-35 (W-2 = 0-line passthrough 고정 영구)** | ✅ **§1.2 + §8.2 답습 (integration tool 298줄 변경 0건 영구)** |
| C-χ-31 (tool behavior 변경 영구 비권고) | ✅ §4.4 답습 — fixture semantics 변경도 동일 비권고 (cross-reference) |
| C-χ-34 (LVE evidence 보존 의무 영구) | ✅ §3.4 + §5.5 답습 (3 fixture 3/3 PASS evidence 보존) |
| C-υ-41 (즉시 rollback 권고 한정 = 사용자 결정 영역) | ✅ §6.5 답습 |
| C-υ-42 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) | ✅ Post-implementation 검증 시점 답습 한정 (cycle 4/4 영역) |
| C-τ-3 (R-1 현재 상태 매트릭스 = technical pre-conditions 모두 충족) | ✅ §1.5 답습 |
| C-ρ-x (Step Division — local self-check 한정 + 본문 변경 0건) | ✅ §5.2 답습 |
| C-σ-x (LVE 51/51 PASS — 3 fixture 3/3 PASS 포함) | ✅ §3.4 답습 |
| Group α C-11 (외부 LLM 응답 = 입력 한정) | ✅ §10 답습 (외부 LLM 자동 호출 0건) |
| F-금지 #1 (GitHub Actions secrets 사용 도입 0건 영구 답습) | ✅ §0.5 답습 |
| ADR-011 §2.1 (a)~(e) 5조건 모법 | ✅ 답습 한정 |
| ADR-008 부록 C Hermes PMO Activation 12 조건 미진입 | ✅ 답습 한정 |

---

## 9. 합의 형태 권고 + 풀 3+1 트리거 분석

### 9.1 본 brief 권고 합의 형태

| 합의 형태 | 적격성 | 본 brief 권고 |
|---------|------|----------|
| **(a) Reviewer-only 단축 합의** | T-2 재발화 영역 한계 (Stage 4 entry brief `81472ba` + W-1 `df741a2` + W-2 `310b518` 시점 이미 발화 영역 완료) + 풀 3+1 트리거 새 발화 0/16 | ✅ **권고 시작점** — 본 brief = W-3 단독 micro-patch *가능성 검토* DRAFT + W-1 + W-2 = 0-line passthrough 답습 + W-4 분리 + W-5~W-10 분리 + 변경 0 lines 권고 시작점 + comment/blank/header ≤ 6 lines 한정 → T-2 발화 *영역 한계* (Stage 4 entry brief + W-1 + W-2 합의 시점 이미 발화 완료 — 본 brief = 그 권위 답습 한정) |
| (b) 풀 3+1 합의 | 사용자 명시 보강 결정 시 (T-N 신규 발화 발견 시) | 옵션 (사용자 결정 영역) |
| (c) 풀 3+1 + 외부 LLM 1+ | T-6 / T-10 / T-13 발화 시 (T3 영역 / 경계 불명확 / Stage 5 권고) | ❌ 비권고 (본 brief = T-6/T-10/T-13 미발화) |

### 9.2 풀 3+1 트리거 16 영역 × 본 brief 발화 매트릭스

| T # | 영역 | 본 brief 발화 |
|----|----|------------|
| T-1 | 새 권위 결정 (ADR / P / GP 신규 발행) | 0 (본 brief = 답습 한정) |
| T-2 | 사용자 명시 영구 5 금지 영역 中 1+ 해소 권고 | ⚠️ **재발화 영역 한계** — Stage 4 entry brief 합의 시점 (`81472ba`) 이미 T-2 발화 + W-1 합의 시점 (`df741a2`) + W-2 합의 시점 (`310b518`) 답습 영역 완료 → 본 brief = cycle 3/4 권위 답습 한정 + comment/blank/header ≤ 6 lines 영역 → **새 T-2 발화 0건** |
| T-3 | §5.5.1+§5.5.2 본문 변경 시도 / fixture semantics 변경 시도 | 0 (본 brief = semantics 변경 0건 영구 답습 — 옵션 (vi) 비권고) |
| T-4 | Provider Liquidity 5-way 약화 위험 | 0 (R-1 = vendor-agnostic 답습 + fixture = generic shell 한정) |
| T-5 | 5 영구 핵심 제약 5/5 보존 위반 | 0 (LVE §5.1 + 본 brief 옵션 (i)~(iv) 보존 한정) |
| T-6 | T3 영역 진입 권고 | 0 (Backlog #3 분리 명시) |
| T-7 | 합산 503 합의 조건 中 1+ 변경 권고 | 0 (본 brief = 0건 영구 답습) |
| T-8 | F-금지 #1 위반 권고 (GitHub Actions secrets 도입) | 0 |
| T-9 | Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 | 0 |
| T-10 | PC-3+AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0 (§2.3 + §7.3 분리 명시) |
| T-11 | Phase α-1 / α-2 / α-3 actual run 자동 재실행 | 0 (PRE 영역 = read-only) |
| T-12 | Hermes PMO 격상 권고 | 0 (영구 답습) |
| T-13 | Stage 5 자동 진입 권고 | 0 (§2.3 W-10 분리 명시) |
| T-14 | Operational Readiness PASS 선언 권고 | 0 (영구 답습) |
| T-15 | W-1 + W-2 재진입 / 0-line passthrough 고정 변경 권고 | 0 (cycle 1/4 + cycle 2/4 답습 영구) |
| T-16 | 신규 fixture 추가 / fixture 삭제 권고 | 0 (옵션 (vii) 비권고 영구 답습) |
| **합산** | **16 트리거** | **0/16 새 발화 → Reviewer-only 단축 합의 적격 시작점** |

### 9.3 외부 LLM 1+ 비적용 사유

| 영역 | 비적용 사유 |
|------|---------|
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | 비적격 — 본 brief = cycle 3/4 한정 + comment/blank/header ≤ 6 lines 영역 + W-3 단독 영역 |
| T-6 (T3 영역 진입 권고) | 0건 (Backlog #3 분리) |
| T-10 (경계 불명확) | 0건 (§2.3 + §7.3 분리 명시) |
| T-13 (Stage 5 자동 진입 권고) | 0건 (§2.3 W-10 분리) |
| 본 brief 권고 | **외부 LLM 1+ 비적용** (Group α C-11 답습 + ADR-011 §2.4 답습 한정) |

---

## 10. 본 brief 자체 금지 + 본 brief 발효 후 의무 금지

### 10.1 본 brief 자체 금지 ≥ 50 영역

본 brief 자체는 다음 영역을 *발효* 시키지 않는다:

- ❌ 3 fixture (89줄) 어느 줄도 변경
- ❌ `tools/mvp1_pc3_ar1_integration_check.py` (298줄) 어느 줄도 변경 (W-2 답습 영구)
- ❌ 3 MVP-1 workflow (1206줄) 어느 줄도 변경 (W-1 답습 영구)
- ❌ R-4 / R-5 / R-7 본문 (1192줄, 13 file) 어느 줄도 변경
- ❌ `src/` runtime code / facade.py placeholder 어느 줄도 변경
- ❌ fixture semantics (entry step name / `continue-on-error` / `set -e` / `exit 1` / fail-closed 패턴 / rc expected) 어느 것도 변경 / 재해석
- ❌ 신규 fixture 추가 / 기존 fixture 삭제 / fixture 파일 위치 이동
- ❌ `on.push.branches` 영역 어느 것도 변경
- ❌ YAML schema (`jobs:` / `steps:` / `runs-on:` 구조) 어느 것도 변경
- ❌ Stage 4 step (line 318~360) 본문 어느 것도 변경
- ❌ §5.5.1 + §5.5.2 PC-3 + AR-1 본문 어느 것도 변경
- ❌ R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 어느 것도 변경
- ❌ `.importlinter` 어느 영역도 변경
- ❌ R-7 docker secret block / image layer check / restart recovery 어느 것도 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 어느 영역도 진입
- ❌ Stage 5 (G3-7 4 항목) 어느 항목도 진입
- ❌ W-5 ~ W-10 어느 영역도 진입
- ❌ W-4 어느 작업도 진입
- ❌ branch protection 어느 영역도 변경
- ❌ 신규 workflow 신설 / `pull_request_target` 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile / Production `docker-compose.yml` 어느 것도 변경
- ❌ 실 secret material commit (fixture sample command 모두 정적 verifier 입력 한정)
- ❌ Layer A / B / C / D / E / F 재발효 / 재선언 / 발효
- ❌ 신규 ADR / P / GP 발행
- ❌ 합의 보고서 자동 작성
- ❌ CONTEXT / INDEX / SESSION 메타 자동 갱신
- ❌ git commit / push 자동 진입
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정
- ❌ threshold 고정
- ❌ event enum 정식 등록
- ❌ Phase β / γ 자동 진입
- ❌ Group I 자동 진입
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 재고정
- ❌ 합산 503 합의 조건 자동 변경
- ❌ W-1 = 0-line passthrough 고정 변경 (C-φ-30)
- ❌ W-2 = 0-line passthrough 고정 변경 (C-χ-35)
- ❌ W-2 brief 10 caveat 변경
- ❌ LVE 3/3 fixture PASS evidence 자동 재집계
- ❌ 4 prerequisite runs 자동 재실행
- ❌ Stage 4 step line 318~360 grep 답습 변경
- ❌ Operational Readiness PASS / Hermes PMO 격상 발효
- ❌ 신규 actual GitHub Actions run trigger 발화
- ❌ W-3 micro-patch 변경 line 최종 확정 발효
- ❌ W-3 실 micro-patch 자동 진입

### 10.2 본 brief 발효 후 의무 금지 ≥ 13 영역

본 brief APPROVE AS BRIEF 후에도 다음은 *자동* 진입 0건:

- ❌ W-3 실 micro-patch 자동 진입 (사용자 명시 결정 영역)
- ❌ W-1 / W-2 재진입 (cycle 1/4 + 2/4 답습 영구)
- ❌ W-4 brief 자동 작성 진입
- ❌ Backlog #1+#2 / Backlog #3 T3 / Backlog #4 / Backlog #5 / Backlog #6 / Stage 5 자동 진입
- ❌ Layer C 재발효 / Layer D 재선언 / Layer E / Layer F 자동 진입
- ❌ Phase β / γ / MVP-2 ~ MVP-6 자동 진입
- ❌ 합의 보고서 자동 작성 (사용자 명시 결정 후)
- ❌ 메타 commit / push 자동 진입 (사용자 명시 결정 후)
- ❌ 외부 LLM 자동 호출 (사용자 명시 결정 시에만)
- ❌ 신규 actual run trigger 자동 발화
- ❌ LVE evidence 자동 재집계
- ❌ 4 prerequisite runs 자동 재실행
- ❌ Operational Readiness PASS / Hermes PMO 격상 자동 발효

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 영역 영향 |
|-----|----|---------|
| **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점)** | 본 brief = APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH → C-ψ-1 ~ C-ψ-N 정식 등록 + 합산 503 → 503+N (19 합의) | ✅ T-2 재발화 영역 한계 답습 + W-3 = 0-line passthrough 고정 |
| (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) | Agent A + B + C 가동 → 4 에이전트 본문 + Reviewer 본문 작성 | 옵션 (사용자 결정 영역 — 본 brief = 풀 3+1 트리거 0/16 새 발화) |
| (C) brief 수정 (특정 § 보강 요청) | 본 brief 본문 보강 → 재DRAFT | 옵션 |
| (D) 부분 채택 (특정 옵션 (ii)~(iv) 中 1+ 한정) | 옵션 (ii) / (iii) / (iv) 中 사용자 결정 | 옵션 (변경 line 결정 영역) |
| (E) W-3 실 micro-patch 직접 진입 brief | 본 brief 폐기 + 실 micro-patch brief 작성 | 옵션 (본 brief = 가능성 검토 한정 — 실 micro-patch = 별도 brief 영역) |
| (F) 본 brief 보류 → W-4 cycle 우선 진입 | cycle 4/4 W-4 trigger brief 작성 | 옵션 (cycle 분리 영구 답습 — 순서 변경) |
| (G) Backlog 전환 | Backlog #1+#2 / #3 / #4 / #5 / #6 / Stage 5 中 사용자 결정 | 옵션 (영역 외 진입) |
| (H) brief 폐기 | 본 brief 본문 보존 + 합의 0건 | 옵션 |
| (I) 세션 종료 | CONTEXT / INDEX / SESSION 갱신 + 다음 세션 1순위 결정 | 옵션 |

### 11.1 (A) 옵션 채택 시 후속 commit chain (사용자 명시 결정 영역)

```
(현재) W-3 brief DRAFT 작성 commit (예: 후속 31)
   │
   ▼ (사용자 명시 결정 후)
■ docs(review): approve Phase alpha-4 W-3 micropatch brief (본 합의 commit, 사용자 결정)
   │
   ▼ (사용자 명시 결정 후)
■ docs(context): record Phase alpha-4 W-3 micropatch status (CONTEXT + INDEX + SESSION 갱신 commit)
   │
   ▼ (사용자 명시 결정 후)
■ git push origin feature/hermes-phase0
   │
   ▼ (자동 진입 0건 — 사용자 결정 영역)
■ W-4 brief (cycle 4/4) / W-3 실 micro-patch / 세션 종료 中 사용자 결정
```

### 11.2 본 brief 새 조건 후보 enumerate (합의 보고서 작성 시 정식 등록)

본 brief 발효 시 새 조건 후보 ≥ 34 (C-χ-1 ~ C-χ-34 답습 패턴 답습, W-3 특화 5+ 신규 — 신규 영역: fixture semantics 변경 영구 비권고 + 신규 fixture 추가/삭제 영구 비권고 + `on.push.branches` 변경 영구 비권고 + YAML schema 변경 영구 비권고 + LVE 3/3 PASS evidence 보존 의무):

| # | 후보 조건 영역 |
|---|------------|
| C-ψ-1 | 본 brief = cycle 3/4 (W-3 단독) 진입 한정 (C-υ-43 발효 답습) |
| C-ψ-2 | W-1 + W-2 답습 영구 (`df741a2` C-φ-30 + `310b518` C-χ-35) |
| C-ψ-3 | W-3 단독 영역 + W-1 + W-2 답습 + W-4 분리 + W-5~W-10 분리 |
| C-ψ-4 | 3 fixture 현재 상태 매트릭스 채택 (89줄 + 3 expected behavior + LVE 3/3 PASS) |
| C-ψ-5 | 변경 line 권고 시작점 = 0 lines (옵션 (i)) |
| C-ψ-6 | 사용자 결정 옵션 상한 ≤ 6 lines (옵션 (iv) — comment/blank/top-level name 한정) |
| C-ψ-7 | 옵션 (v) ≥ 7 lines 영역 외 영구 답습 |
| C-ψ-8 | 옵션 (vi) semantics change 영구 비권고 (entry step name / continue-on-error / set -e / exit 1 / fail-closed 패턴) — **신규** |
| C-ψ-9 | 옵션 (vii) 신규 fixture 추가 / 기존 fixture 삭제 영구 비권고 — **신규** |
| C-ψ-10 | 옵션 (viii) `on.push.branches` 변경 영구 비권고 — **신규** |
| C-ψ-11 | 옵션 (ix) YAML schema 변경 영구 비권고 — **신규** |
| C-ψ-12 | W-3 검증 7 영역 (W-3-V1 ~ W-3-V7) 채택 |
| C-ψ-13 | PRE-0 도구 가용성 사전 점검 6 영역 채택 (C-υ-38 답습) |
| C-ψ-14 | rollback trigger 28 영역 × W-3 시점 발화 0/28 (옵션 (i)~(iv) 한정) |
| C-ψ-15 | 사용자 명시 5 금지 5/5 위반 0건 영구 답습 |
| C-ψ-16 | 합산 503 합의 조건 변경 0건 영구 답습 |
| C-ψ-17 | Backlog 분리 영구 답습 (#1~#6 + Stage 5 + W-1 + W-2 + W-4) |
| C-ψ-18 | 풀 3+1 트리거 0/16 새 발화 → Reviewer-only 단축 합의 적격 |
| C-ψ-19 | 외부 LLM 1+ 비적용 (T-6 / T-10 / T-13 미발화) |
| C-ψ-20 | 본 brief 자체 금지 ≥ 50 영역 + 발효 후 의무 금지 ≥ 13 영역 |
| C-ψ-21 | 5 영구 핵심 제약 5/5 보존 + Provider Liquidity 5-way 100% 보존 |
| C-ψ-22 | F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) |
| C-ψ-23 | LVE 3/3 fixture PASS evidence 보존 의무 영구 (옵션 (i)~(iv) 한정) — **신규 영역** |
| C-ψ-24 | entry step `- name:` 필드 변경 영구 비권고 (`ENTRY_NAME_PATTERNS` 매칭 답습) — **신규 영역** |
| C-ψ-25 | fixture `on.push.branches: ["fixture-only/**"]` 답습 영구 (실 trigger 0건 보장) — **신규 영역** |
| C-ψ-26 | tool behavior (regex / logic / mode / rc / dataclass schema) 변경 = W-2 답습 위반 영역 영구 비권고 |
| C-ψ-27 | 3 MVP-1 workflow Stage 4 step (line 329~341) 변경 = W-1 답습 위반 영역 영구 비권고 |
| C-ψ-28 | fixture sample command (예: `tools/sample_scanner.py`) = 실 실행 0건 (정적 verifier 입력 한정) — **신규 영역** |
| C-ψ-29 | C-υ-43 답습 cycle 3/4 진입 — cycle 4/4 (W-4) 별도 영구 답습 |
| C-ψ-30 | C-υ-41 답습 "즉시 rollback" 권고 = 사용자 결정 영역 |
| C-ψ-31 | C-υ-42 답습 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) — cycle 4/4 영역 |
| C-ψ-32 | brief 본문 변경 0건 영구 답습 |
| C-ψ-33 | brief 발효 후 자동 진입 0건 (모든 후속 단계 = 사용자 명시 결정 영역) |
| C-ψ-34 | event enum (`pc3_ar1_integration_implementation`) 후보 한정 영구 답습 (Backlog #5 ADR-012 §2.2 분리) |
| C-ψ-35 | (합의 시점 신규 1) W-3 = 0-line passthrough 고정 영구 (사용자 명시 결정 시 발효) |
| **합산** | **35 후보** (W-2 답습 패턴 30 + W-3 특화 5 신규: C-ψ-8 + C-ψ-23 + C-ψ-24 + C-ψ-25 + C-ψ-28) |

---

## 12. 본 brief 메타 검증

### 12.1 본 brief 가 답습한 영역 매트릭스

| 답습 영역 | 답습 출처 | 본 brief 답습 |
|---------|---------|----------|
| W-2 brief 합의 (`310b518`) APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH 35 조건 | C-χ-1 ~ C-χ-35 | ✅ §1.2 + §8.2 답습 한정 |
| W-1 brief 합의 (`df741a2`) APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH 30 조건 | C-φ-1 ~ C-φ-30 | ✅ §1.2 + §8.2 답습 한정 |
| Stage 4 entry brief 합의 (`81472ba`) APPROVE AS BRIEF WITH CONDITIONS 49 조건 | C-υ-1 ~ C-υ-49 | ✅ 답습 한정 (C-υ-38 + C-υ-41 + C-υ-42 + C-υ-43 + C-υ-44 강화) |
| Stage 3 합의 (`d3f6d59`) APPROVE AS BRIEF 36 조건 | C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| LVE 합의 (`b264580`) APPROVE 31 조건 + LVE 본문 (`4ce5a0b`) 51/51 PASS (3 fixture 3/3 PASS 포함) | C-σ-1 ~ C-σ-31 | ✅ §3.4 + §5.5 답습 한정 |
| ADR-011 §2.1 (a)~(e) 5 조건 모법 | ADR-011 | ✅ 답습 한정 |
| ADR-008 부록 B + 부록 C 12 조건 | ADR-008 | ✅ 답습 한정 |
| Group α C-11 / C-14 (외부 LLM 응답 = 입력 한정 + 1+ blind 의뢰 의무) | Group α | ✅ §9.3 답습 |
| F-금지 #1 (GitHub Actions secrets 사용 도입 0건 영구) | Stage 5 cycle 1~4 | ✅ §0.5 답습 |
| 5 영구 핵심 제약 + Provider Liquidity 5-way + Backlog #1~#6 분리 | LVE §5.1 + §5.2 + §5.3 | ✅ 답습 한정 |

### 12.2 본 brief 자체 검증

| 검증 영역 | 본 brief 답습 |
|---------|----------|
| brief 작성 시점 5 금지 5/5 위반 | ✅ 0건 영구 답습 |
| brief 본문 = 답습 한정 (R-1 + R-4/5/7 + `src/` + tool + 3 workflow + 3 fixture 본문 어느 줄도 변경 0건) | ✅ 영구 답습 |
| brief 발효 시점 5 금지 5/5 위반 | ✅ 0건 영구 답습 (DRAFT 영역) |
| W-1 + W-2 재진입 / W-3 / W-4 진입 (본 brief 시점) | ✅ 0건 (cycle 1/4 + 2/4 = 답습 / cycle 4/4 분리) |
| 합산 503 합의 조건 변경 | ✅ 0건 영구 답습 |
| Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 | ✅ 0건 영구 답습 |
| Operational Readiness PASS / Hermes PMO 격상 | ✅ 0건 영구 답습 |
| 신규 actual GitHub Actions run trigger | ✅ 0건 영구 답습 |
| 외부 LLM 자동 호출 / 실 API/SDK / 인간 리뷰 의무 자동 발화 | ✅ 0건 영구 답습 |
| 합의 보고서 작성 / 메타 commit / push 자동 진입 | ✅ 0건 (사용자 명시 결정 후 진입) |

### 12.3 본 brief 의 *제약 사항* enumerate

본 brief 의 *권위 제약*:

1. 본 brief = **준비안 (DRAFT)** — 사용자 명시 승인 전 어떤 *발효* 도 발생시키지 않는다
2. 본 brief 합의 시 = **W-3 단독 micro-patch 가능성 검토 발효 한정** — 실 micro-patch / W-1 + W-2 재진입 / W-4 진입 = 사용자 명시 결정 후 진입
3. 본 brief 영역 = **fixture (89줄) 한정** — 3 MVP-1 workflow / integration tool / runtime code / R-4/5/7 / Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 어느 것도 변경 영역 외
4. 본 brief 권고 시작점 = **변경 0 lines** (옵션 (i)) + 사용자 결정 옵션 상한 = ≤ 6 lines (옵션 (iv))
5. 본 brief 답습 = **C-χ-35 + C-φ-30 + C-υ-44 + Agent B C-B6 + Agent C C-C1 동시 발효** 영역
6. 본 brief 합의 형태 = **(a) Reviewer-only 단축 합의 권고 시작점** (T-2 재발화 영역 한계 + 풀 3+1 트리거 0/16 새 발화)
7. 본 brief 비권고 영역 = **옵션 (v) ≥ 7 lines + 옵션 (vi)~(ix) semantics/추가/삭제/branches/schema 변경** (LVE 3/3 PASS evidence 변경 위험 + W-1 + W-2 답습 위반 + Stage 4 step 호출 인터페이스 답습 위반)
8. 본 brief 의 합의 보고서 작성 / 메타 commit / push / 외부 LLM 호출 = **사용자 명시 결정 영역** (자동 진입 0건)
9. 본 brief 의 W-4 brief 자동 진입 = **0건** (cycle 4/4 별도 brief 영역 — 사용자 결정 후 진입)
10. 본 brief 의 LVE 3/3 PASS evidence 자동 재집계 = **0건** (옵션 (i)~(iv) 한정 = 자동 보존 + 옵션 (vi)~(ix) 채택 시 재집계 의무 발화 — 비권고)

---

## 13. 본 brief 요약

본 brief 는 **Phase α-4 R-1 Stage 4 W-2 micro-patch brief Reviewer-only 단축 합의 (`310b518` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 35 조건 C-χ-1 ~ C-χ-35, 합산 503 합의 조건) 발효 후속**, 사용자 명시 진입 명령 답습 (W-3 사전 평가 결과 = "W-3 fixture brief 먼저 (권고)" 채택 후속) — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) Stage 4 *W-3 단독* 영역 (3 fixture `tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄 한정) *최소 micro-patch 가능성 검토* brief 준비안 (DRAFT)** = **C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션) 정식 등록 답습 cycle 3/4 진입** ("*Should* W-3 introduce micro-patch lines on 3 fixture (and which ones), or is *0-line passthrough* the correct posture for the fixtures at this gate?").

**사용자 명시 5 금지** (3 fixture 실 변경 / CI workflow 변경 (W-1 = 0-line passthrough 답습) / integration tool 변경 (W-2 = 0-line passthrough 답습) / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 영구 답습.

**3 fixture 현재 상태 매트릭스** (read-only, §3) — `pass/compliant_entry_step.yml` 30 + `fail/pc3_violation_continue_on_error.yml` 31 + `fail/ar1_violation_no_fail_closed.yml` 28 = **89줄** / 3 expected behavior (PASS rc=0 + FAIL PC-3 rc=1 + FAIL AR-1 rc=1) / 3 호출 인터페이스 (Stage 4 step line 329~341 wired) / **LVE 3/3 PASS evidence 답습** (`4ce5a0b` §3.2.3 — PASS rc=0 + PC-3 FAIL rc=1 + AR-1 FAIL rc=1 + 한국어 shell comment 안전성 + missing/no-entry 에러 처리).

**Micro-patch 후보 영역 *enumerate 한정*** (§4) — **C-υ-44 + C-φ-30 + C-χ-35 답습 4 영역 동시 발효** (Agent A 절차 + Agent B 안전성 + Agent C 단순성 + W-1 + W-2 답습) → **권고 시작점 = 옵션 (i) 변경 0 lines** + 옵션 (ii) ≤ 2 lines (답습 출처 헤더 보강) + 옵션 (iii) ≤ 4 lines (fixture 시그니처 일관성) + 옵션 (iv) ≤ 6 lines (top-level `name:` 일관성) = 사용자 결정 영역 + 옵션 (v) ≥ 7 lines 비권고 + **옵션 (vi) semantics change 비권고 (entry step name / continue-on-error / set -e / exit 1 / fail-closed 패턴 — §5.5.1+§5.5.2 본문 답습 + LVE 3/3 PASS evidence 변경 위험)** + **옵션 (vii) 신규 fixture 추가 / 기존 fixture 삭제 비권고 (LVE 영역 변경 = 재집계 의무)** + **옵션 (viii) `on.push.branches` 변경 비권고 (실 trigger 0건 보장 위반)** + **옵션 (ix) YAML schema 변경 비권고 (`extract_steps()` 답습 위반)**.

**W-3 검증 방법 권고** (§5) — **PRE-0 도구 가용성 사전 점검 6 영역** (C-υ-38 답습 — Python ≥ 3.12 + PyYAML + git + gh CLI 옵션 + grep + integration tool py_compile) + **W-3-V1 ~ W-3-V7 7 검증** (3 fixture YAML parse + PASS fixture verify rc=0 + FAIL PC-3 fixture verify rc=1 + FAIL AR-1 fixture verify rc=1 + entry step name "MVP-1 entry" prefix 검증) = **신규 actual run trigger 0건 영구 답습** (local 한정) + **LVE 3/3 PASS evidence 보존** (옵션 (i)~(iv) 시 자동 보존 + 옵션 (vi)~(ix) 시 재집계 의무 영역 = 비권고).

**W-3 시점 rollback trigger 발화 매트릭스** (§6) — Layer B 18 + TR-1~5 + Step Division 신규 후보 5 = 28 trigger × 옵션별 발화 가능성 → **옵션 (i)+(ii)+(iii)+(iv) = 0/28 발화 영구 답습** + 옵션 (vi) = 5/28 발화 가능성 (비권고) + 옵션 (vii)~(ix) = 추가 비권고 — `git revert HEAD` 권고 시작점 (C-υ-41 답습).

**합의 형태 권고**: 본 brief 자체 = **(a) Reviewer-only 단축 합의 적격 시작점** (T-2 재발화 영역 한계 — Stage 4 entry brief + W-1 + W-2 합의 시점 이미 답습) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 (T-6/T-10/T-13 미발화).

**사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 영구 답습** (작성 시점 + 발효 후 자동 진입 영역 모두 0건).

**합산 503 합의 조건 변경 0건** (18 합의 — W-1 합의 30 + W-2 합의 35 + Stage 4 entry brief 49 포함).

**본 brief 자체 금지 ≥ 50 + 본 brief 발효 후 의무 금지 ≥ 13** enumerate.

**본 brief 새 조건 후보 35 (C-ψ-1 ~ C-ψ-35)** — 합의 보고서 작성 시 정식 등록 (W-2 합의 30+ 답습 패턴 답습 + fixture 특화 5 신규: C-ψ-8 + C-ψ-23 + C-ψ-24 + C-ψ-25 + C-ψ-28 + 합의 시점 신규 C-ψ-35 = 35).

**본 brief 는 3 fixture (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄) 어느 줄도 *변경* 시키지 않으며, fixture semantics (entry step name / continue-on-error / set -e / exit 1 / fail-closed 패턴 / rc expected) / 신규 fixture 추가 / 기존 fixture 삭제 / fixture 파일 위치 / `on.push.branches` / YAML schema 어느 것도 *변경* 시키지 않으며, W-1 = 0-line passthrough 고정 (`df741a2` C-φ-30) / W-2 = 0-line passthrough 고정 (`310b518` C-χ-35) 어느 것도 *변경* 시키지 않으며, `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 시키지 않으며 (W-2 답습 영구), 3 MVP-1 workflow 어느 줄도 *변경* 시키지 않으며 (W-1 답습 영구), W-4 어느 작업도 *진입* 시키지 않으며, Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 어느 것도 *변경* 시키지 않으며, 사용자 명시 5 금지 + 영구 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 503 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / W-3 변경 line / 수정 영역 어느 것도 *최종 확정 발효* / LVE 3/3 PASS evidence 자동 재집계 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**.

다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점 — T-2 재발화 영역 한계)** / (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) / (C) brief 수정 / (D) 부분 채택 / (E) W-3 실 micro-patch 직접 진입 brief / (F) W-4 cycle 우선 / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.
