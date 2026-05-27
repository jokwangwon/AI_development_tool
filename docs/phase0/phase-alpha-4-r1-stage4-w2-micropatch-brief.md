# Phase α-4 R-1 Stage 4 W-2 micro-patch brief (integration tool 한정, cycle 2/4) (DRAFT)

> **본 문서는 Phase α-4 R-1 Stage 4 W-1 micro-patch brief Reviewer-only 단축 합의 (`df741a2` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 30 조건 C-φ-1 ~ C-φ-30, 합산 468 합의 조건) 발효 후속, 사용자 명시 진입 명령 답습 — **Phase α-4 R-1 Stage 4 *W-2 단독* 영역 (integration check tool `tools/mvp1_pc3_ar1_integration_check.py` 298줄 한정) *최소 micro-patch 가능성 검토* brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 4 entry (W-1~W-4 lockdown, `9c33efe` + `81472ba`) = "*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?"
> - α-4 Stage 4 W-1 brief (`7af77fb` + `df741a2`, cycle 1/4) = "*Should* W-1 introduce micro-patch lines (and which ones), or is *0-line passthrough* correct?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - **본 brief = α-4 Stage 4 W-2 micro-patch *possibility* 검토 DRAFT (cycle 2/4)** — **"*Should* W-2 introduce micro-patch lines on `tools/mvp1_pc3_ar1_integration_check.py` (and which ones), or is *0-line passthrough* the correct posture for the integration tool at this gate?"**
> - α-4 Stage 4 W-2 실 micro-patch (본 brief 외) = "*Execute* the chosen patch (if any)"
> - W-3 / W-4 = 영역 외 영구 답습 (사용자 명시 단독 영역 한정)
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며, (ii) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며, (iii) W-3 / W-4 어느 작업도 *진입* 시키지 않으며, (iv) Stage 4 entry brief 합의 49 + W-1 합의 30 = 합산 468 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며, (v) 사용자 명시 5 금지 (tool 본문 실 변경 / CI workflow 변경 / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 어느 것도 *해소* 시키지 않으며, (vi) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, (vii) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-18 후속 29
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w1-micropatch.md` (commit `df741a2` — W-1 brief Reviewer-only 단축 합의 APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 30 조건 C-φ-1 ~ C-φ-30, **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md` (commit `7af77fb`, 868줄 — W-1 brief DRAFT)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md` (commit `81472ba` — Stage 4 entry brief 풀 3+1 합의, 49 조건 C-υ-1 ~ C-υ-49)
- `docs/phase0/phase-alpha-4-r1-stage4-entry-brief.md` (commit `9c33efe`, 1032줄 — Stage 4 W-1~W-4 lockdown brief)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-actual-entry-decision.md` (commit `d3f6d59` — Stage 3 실 진입 합의, 36 조건 C-τ-1 ~ C-τ-36)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS, integration tool 12/12 PASS 포함)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C (Hermes PMO Activation 12 조건 미진입 영구 답습)
- `tools/mvp1_pc3_ar1_integration_check.py` (298줄 — **본 brief 의 대상**, 답습 한정 read-only)

---

## 0. 본 brief 의 범위

### 0.1 사용자 명시 진입 명령 답습

> "W-2 integration tool micro-patch brief를 작성해주세요. 범위는 Phase α-4 Stage 4 cycle 2/4, integration tool micro-patch 가능성 검토입니다. 아직 실제 tool 수정, CI workflow 변경, actual run 재실행, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습 (본 brief 의 명시적 경계)

| # | 금지 영역 | 본 brief 시점 |
|---|---------|----------|
| **#1** | **integration tool 실 변경** (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 발효) | ✅ 0건 영구 답습 — 본 brief = *후보 검토 한정* |
| **#2** | **CI workflow 변경** (3 MVP-1 workflow 1206줄 변경 발효) | ✅ 0건 영구 답습 — W-1 cycle 1/4 합의 답습 (0-line passthrough 고정) |
| **#3** | **actual run 재실행** (신규 GitHub Actions run trigger) | ✅ 0건 영구 답습 — W-4 영역 분리 |
| **#4** | **Operational Readiness PASS (Layer E) 선언** | ✅ 0건 영구 답습 — MVP-6 영역 분리 |
| **#5** | **Hermes PMO 격상 (Layer F)** | ✅ 0건 영구 답습 — ADR-008 부록 C 12 조건 미진입 |
| **합산** | **5 금지** | **5/5 영구 답습** |

**주**: 본 brief 의 #2 영역은 W-1 합의 답습 (W-1 = 0-line passthrough 고정 → 3 MVP-1 workflow 1206줄 변경 0건 영구 답습) — W-2 영역 (tool 본문) 과는 별도 영역. 본 brief = W-2 단독 영역 한정 → #1 ~ #5 모두 영구 답습.

### 0.3 본 brief 영역 vs Stage 4 entry brief / W-1 brief 영역 분리 매트릭스

| 영역 | Stage 4 entry brief (`9c33efe`+`81472ba`) | W-1 brief (`7af77fb`+`df741a2`) | 본 brief (W-2) |
|------|------------------------------------------|--------------------------------|--------------|
| 범위 | W-1 + W-2 + W-3 + W-4 lockdown 권고 | W-1 단독 micro-patch *가능성 검토* (3 MVP-1 workflow 한정) | **W-2 단독 micro-patch *가능성 검토*** (integration tool 한정) |
| 변경 대상 artifact | 7 artifacts × 1593줄 (3 workflow + tool + 3 fixture) | 3 MVP-1 workflow 1206줄 (workflow 한정) | **`tools/mvp1_pc3_ar1_integration_check.py` 298줄 (tool 한정)** |
| 권고 영역 | 수정 파일 + 검증 방법 + actual run 조건 + rollback trigger (4 영역) | 변경 0 lines 우선 권고 + 후보 영역 ≤ 15 lines (paths-only) enumerate | **변경 0 lines 우선 권고 + 후보 영역 ≤ 15 lines (comment/help/error-message 한정) enumerate** |
| W-1 변경 line 권고 | 0 ~ ≤ 15 lines micro-patch *권고 시작점* | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **0 lines 우선 권고 + 후보 영역 ≤ 15 lines enumerate** |
| W-3 / W-4 영역 | 권고 영역 포함 (분리 명시) | 분리 명시 (cycle 3/4 / 4/4 별도) | ❌ **본 brief 영역 외 (사용자 명시 #3 답습 cycle 3/4 / 4/4 분리)** |
| 검증 방법 | Pre / Per-W / Post / Actual run 4 단계 (42 검증) | W-1 단독 검증 7 영역 (W-1-V1 ~ W-1-V7) + PRE-0 도구 가용성 | **W-2 단독 검증 8 영역 (W-2-V1 ~ W-2-V8) + PRE-0 도구 가용성 답습** |
| 합의 결과 발효 | APPROVE AS BRIEF WITH CONDITIONS (49 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (30 조건) | DRAFT (사용자 명시 승인 *전*) |

### 0.4 본 brief 가 *하는* 것

1. W-1 brief 합의 (`df741a2` — 30 조건) 발효 후속 — **W-2 단독 micro-patch *가능성 검토* 한정** (§1)
2. **W-2 영역 한정 매트릭스** — integration tool 한정 + W-1 답습 + W-3/W-4 분리 명시 (§2)
3. **integration tool 현재 상태 매트릭스** (read-only) — 298줄 구조 / 3 mode / --list-checks / rc 의미 / LVE 12/12 PASS 답습 (§3)
4. **Micro-patch 후보 영역 *enumerate 한정*** — 변경 line 0 lines 우선 권고 + ≤ 15 lines 후보 (comment/help/error-message 한정, behavior 변경 비권고) (§4)
5. **W-2 검증 방법 권고** — W-2-V1 ~ W-2-V8 답습 + PRE-0 도구 가용성 사전 점검 (C-υ-38 답습) (§5)
6. **W-2 시점 rollback trigger 발화 가능성 매트릭스** (§6)
7. **사용자 명시 5 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 468 합의 조건 답습 매트릭스** (변경 0건) (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **integration tool 실 변경 (0건)** — `tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 발효 = 별도 cycle 영역
- ❌ **CI workflow 변경 (0건)** — W-1 = 0-line passthrough 고정 답습 (사용자 명시 #2)
- ❌ **actual run 재실행 (0건)** — W-4 신규 trigger = 별도 cycle 영역 (사용자 명시 #3)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (W-1 합의 30 조건 + Stage 4 entry brief 49 조건 + α-1+2+3 evidence + LVE 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — `secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + `tools/mvp1_pc3_ar1_integration_check.py` 298 + 3 fixture 89 = 1593줄 답습 보존
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (α-1+2+3 evidence §5.1 답습)
- ❌ **`src/` runtime code / facade.py placeholder 변경 (0건)** — Backlog #4 분리
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 (0건)** — C-υ-44 답습 (T-3 발화 영역 모호성 청산 명시 강화)
- ❌ **integration tool behavior change (regex / logic / mode set / rc semantics 변경 0건)** — §5.5.1 + §5.5.2 답습 변경 영역 = T-3 발화 영역 → **본 brief 비권고**
- ❌ **integration tool 의존성 변경 (0건)** — stdlib-only 답습 (re + dataclasses + argparse + sys + pathlib + typing) — pyyaml / 외부 패키지 도입 = T-3 영역
- ❌ **integration tool entry point / 호출 인터페이스 변경 (0건)** — 3 MVP-1 workflow Stage 4 step 의 `--mode integration` + `--list-checks` 호출 답습 보존
- ❌ **`ENTRY_NAME_PATTERNS` / `PC3_VIOLATION_PATTERN` / `AR1_EXIT_PATTERN` / `AR1_SET_E_PATTERN` / `STEP_HEAD_PATTERN` regex 변경 (0건)** — behavior 변경 영역
- ❌ **`extract_steps` / `is_entry_step` / `check_pc3` / `check_ar1` / `_strip_comments` / `run_checks` / `print_report` / `list_checks` / `main` 함수 본문 logic 변경 (0건)** — behavior 변경 영역
- ❌ **CheckResult / StepBlock / IntegrationReport dataclass 필드 변경 (0건)** — schema 변경 영역
- ❌ **Stage 4 step 본문 (line 318~360 답습) 변경 (0건)** — 이미 wired 상태 답습 한정 (W-1 = 0-line passthrough 고정 답습)
- ❌ **PC-3 / AR-1 step 순서 변경 (0건)** — Stage 4 entry brief §5.5.1+§5.5.2 본문 변경 시도 권고 0건 (C-B6 + C-υ-44 답습)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **신규 workflow 신설 (0건)** + **`pull_request_target` 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 영역 별도 풀 3+1
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습
- ❌ **`permissions: contents: read` 보강 (0건)** — W-5 영역 = Stage 5 cycle 4 / Backlog #1+#2 분리 영구 답습
- ❌ **Required check 등록 (0건)** — W-6 영역 = Backlog #3 T3 분리
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 (0건)** — Backlog #1+#2+#3 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 영역
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 차단조건 #6 + 부록 B 영구 답습
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)** — PoC 격리 디렉토리 한정 답습
- ❌ **실 secret material commit (0건)** — FAKE_TEST_SECRET marker 답습
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
- ❌ **합산 468 합의 조건 자동 변경 (0건)** — 30 신규 (C-φ-1 ~ C-φ-30) + 438 기존 모두 영구 답습
- ❌ **W-1 = 0-line passthrough 고정 (C-φ-30) 변경 (0건)** — W-1 합의 답습 한정
- ❌ **W-1 brief 9 caveat 변경 (0건)** — W-1 합의 §2.3 답습

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며,
- (ii) W-3 / W-4 어느 작업도 *진입* 시키지 않으며,
- (iii) 합산 468 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iv) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (v) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (vi) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vii) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (viii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (ix) Stage 4 step (line 318~360) / PC-3 / AR-1 step 순서 어느 것도 *변경* 하지 않으며,
- (x) 3 MVP-1 workflow 본문 1206줄 어느 줄도 *변경* 하지 않으며 (W-1 = 0-line passthrough 고정 답습),
- (xi) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (xii) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (xiii) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 어느 것도 *발화* 시키지 않으며,
- (xiv) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (xv) W-2 micro-patch 변경 line / 수정 영역 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정),
- (xvi) integration tool behavior (regex / logic / mode / rc / dataclass schema) 어느 것도 *변경* / *재해석* 하지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **W-2 단독 micro-patch *가능성* (= 변경 0 lines 우선 vs 후보 ≤ 15 lines comment/help/error-message 한정) 검토 권고 한정**. 모든 *확정 발효* / *실 변경* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (W-1 brief 합의 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS — integration tool 12/12 PASS 포함) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 — 31 조건 C-σ-1 ~ C-σ-31 | ✅ 답습 한정 |
| `27351ce` (2026-05-17) | Phase α-4 R-1 Stage 3 실 진입 여부 brief (722줄) | ✅ 답습 한정 |
| `d3f6d59` (2026-05-17) | Phase α-4 R-1 Stage 3 합의 — 36 조건 C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| `630e125` (2026-05-17) | CONTEXT — Phase α-4 R-1 Stage 3 entry status | ✅ 답습 한정 |
| `9c33efe` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief (1032줄 DRAFT) | ✅ 답습 한정 |
| `81472ba` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief 풀 3+1 합의 — 49 조건 C-υ-1 ~ C-υ-49 | ✅ 답습 한정 |
| `e279958` (2026-05-18) | CONTEXT — Phase α-4 R-1 Stage 4 entry status | ✅ 답습 한정 |
| `7af77fb` (2026-05-18) | Phase α-4 R-1 Stage 4 W-1 micro-patch brief (868줄 DRAFT) | ✅ 답습 한정 |
| `df741a2` (2026-05-18) | Phase α-4 R-1 Stage 4 W-1 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 30 조건 C-φ-1 ~ C-φ-30 | ✅ **본 brief 의 발효 trigger** |
| `637a8cf` (HEAD, 2026-05-18) | CONTEXT — Phase α-4 R-1 Stage 4 W-1 micropatch status | ✅ 답습 한정 |

### 1.2 W-1 brief 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-18 후속 28 |
| 합의 형태 | **Reviewer-only 단축 합의** (Agent A + B + C 미가동 — T-2 재발화 영역 한계 + 풀 3+1 트리거 새 발화 0/16) |
| 합의 판정 | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** — BLOCK 사유 0건 |
| 합의 조건 | **30 조건 (C-φ-1 ~ C-φ-30)** — W-1 brief §11.2 답습 29 + 합의 신규 1 (C-φ-30 "W-1 = 0-line passthrough 고정") |
| W-2 핵심 답습 (cycle 2/4 발효 영역) | C-φ-1 ~ C-φ-30 모두 답습 + 본 brief = cycle 2/4 진입 (C-υ-43 답습 — "4 cycle 옵션 정식 등록") |
| 9 caveat 명시 의무 (사용자 명시) | (1) W-1 범위 = 3 MVP-1 workflow micro-patch 검토 + (2) 권고 결론 = 0-line passthrough + (3) 실 CI workflow 변경 0건 + (4) actual run 재실행 0건 + (5) W-2~W-4 진입 0건 + (6) W-5~W-10 진입 0건 + (7) workflow 1 단독 cross-workflow re-verify 한계 + (8) workflow 2/3 paths 미답습 영역 후속 관찰 보존 + (9) Operational Readiness PASS / Hermes PMO 격상 없음 |
| 풀 3+1 트리거 발화 | 0/16 새 발화 (T-2 = Stage 4 entry brief 시점 이미 발화 — 본 brief 답습 한정) |
| 본 brief trigger 의미 | **W-1 cycle 1/4 = 0-line passthrough 합의 발효** → cycle 2/4 (W-2 integration tool) 진입 = 본 brief DRAFT |

### 1.3 8 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 | "*Can* we enter Phase α-4?" |
| α-4 Stage 1.5 (조건 재검토) | 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (Step 분할) | Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 | "*How* should it be staged?" |
| α-4 Stage 2.5 (LVE) | Local Validation Evidence | `4ce5a0b` + `b264580` | APPROVE | 31 | "*Has local validation evidence been compiled?*" |
| α-4 Stage 3 (실 진입 여부) | Stage 3 brief | `27351ce` + `d3f6d59` | APPROVE AS BRIEF | 36 | "*Should* we enter actual implementation now?" |
| α-4 Stage 4 entry (lockdown) | Stage 4 entry brief | `9c33efe` + `81472ba` | APPROVE AS BRIEF WITH CONDITIONS | 49 | "*What exactly* will Stage 4 W-1~W-4 do?" |
| α-4 Stage 4 W-1 (cycle 1/4) | W-1 micro-patch brief | `7af77fb` + `df741a2` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 30 | "*Should* W-1 introduce micro-patch lines, or is 0-line passthrough correct?" |
| **α-4 Stage 4 W-2 (본 brief, cycle 2/4)** | **W-2 integration tool micro-patch brief** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* W-2 introduce micro-patch lines on integration tool, or is 0-line passthrough correct for the tool at this gate?"** |
| α-4 Stage 4 W-2 실 micro-patch (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* the chosen patch (if any)" |
| α-4 Stage 4 W-3 (cycle 3/4) | W-3 3 fixture brief | (미정) | (미정) | (미정) | "*Should* W-3 introduce micro-patch lines on fixtures?" |
| α-4 Stage 4 W-4 (cycle 4/4) | W-4 actual run trigger brief | (미정) | (미정) | (미정) | "*Should* W-4 trigger a fresh actual run?" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 4 W-2 cycle 2/4 framing** (Stage 4 entry brief 합의 §8 권고 시작점 답습 + C-υ-43 4 cycle 옵션 정식 등록 답습 + W-1 합의 (`df741a2`) 발효 후속):

- α-4 Stage 1 ↔ 1.5 ↔ 2 ↔ 2.5 ↔ 3 ↔ Stage 4 entry ↔ **W-1 (cycle 1/4, 0-line passthrough 확정)** ↔ **W-2 micro-patch (본 brief, cycle 2/4)** ↔ W-2 실 micro-patch (사용자 결정) ↔ W-3 brief (cycle 3/4) ↔ W-4 trigger brief (cycle 4/4)
- 본 brief 의 단일 책무: **"integration tool 의 minimum micro-patch *possibility* 검토 + 변경 0 lines 우선 권고 vs 후보 ≤ 15 lines (comment/help/error-message 한정) enumerate"** + **"실 변경 자동 진입 0건"** + **"behavior 변경 0건 영구 답습"**
- 본 brief ≠ W-2 실 micro-patch (tool 본문 변경 + commit = 별도 cycle 영역)
- 본 brief ≠ W-1 재진입 (W-1 = 0-line passthrough 고정 답습)
- 본 brief ≠ W-3 / W-4 brief
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-18 후속 29 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 5 금지 #4 영구 답습) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 5 금지 #5 영구 답습) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local 8/8 PASS evidence 답습 |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 |
| Phase α-4 Stage 4 entry (R-1) | W-1~W-4 lockdown 합의 발효 | ✅ `81472ba` 답습 (49 조건) |
| Phase α-4 Stage 4 W-1 | 3 MVP-1 workflow = 0-line passthrough 합의 발효 | ✅ `df741a2` 답습 (30 조건) |
| **Phase α-4 Stage 4 W-2 (본 brief)** | **integration tool micro-patch *가능성 검토*** | ⏳ **본 brief = DRAFT (cycle 2/4)** |

---

## 2. W-2 영역 한정 매트릭스

### 2.1 W-2 단독 영역 enumerate (Stage 4 entry brief §2.1 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-1 | 3 MVP-1 workflow 본문 (`secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 = 1206줄) | ❌ 본 brief 영역 외 (W-1 = **0-line passthrough 고정** 답습, `df741a2` C-φ-30) |
| **W-2** | **integration check tool 본문 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄)** | ✅ **본 brief = micro-patch *가능성 검토* 한정 (cycle 2/4)** |
| W-3 | 3 fixture 본문 (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄) | ❌ 본 brief 영역 외 (사용자 명시 #3 — cycle 3/4 별도 brief 영역) |
| W-4 | 신규 actual GitHub Actions run trigger (push event) | ❌ 본 brief 영역 외 (사용자 명시 #3 — cycle 4/4 별도 brief 영역) |

### 2.2 W-1 답습 + W-3 / W-4 분리 명시 (위반 0건 영구 답습)

| 영역 | W-1 brief 시점 (cycle 1/4) | 본 brief 시점 (cycle 2/4) |
|---|--------------------------|------------------------|
| W-1 | 단독 cycle = micro-patch *가능성 검토* | ✅ **0-line passthrough 합의 답습 영구 답습** (재진입 0건) |
| **W-2** | 분리 명시 (cycle 2/4 별도) | ✅ **본 brief 영역** |
| W-3 | 분리 명시 (cycle 3/4 별도) | ❌ 본 brief 영역 외 (cycle 3/4 별도) |
| W-4 | 분리 명시 (cycle 4/4 별도) | ❌ 본 brief 영역 외 (cycle 4/4 별도) |
| **합산** | **W-1 = 0-line passthrough 확정** | **W-2 = 본 brief 영역** + **W-1 답습 + W-3 / W-4 분리 ✅** |

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

본 §2 = **W-2 단독 영역 *권고 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). W-1 재진입 + W-3 / W-4 + W-5 ~ W-10 어느 것도 본 brief 가 *통합* 시키지 않는다.

---

## 3. integration tool 현재 상태 매트릭스 (read-only)

### 3.1 tool 본문 구조 매트릭스 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 답습)

| 영역 | line 범위 | 줄수 | 본 brief 답습 |
|------|---------|----|----------|
| Shebang + 답습 출처 헤더 주석 | 1~23 | 23 | ✅ read-only 답습 |
| `__future__` + imports (stdlib only — re/dataclasses/argparse/sys/pathlib/typing) | 25~32 | 8 | ✅ stdlib 전용 답습 — 외부 dependency 0건 |
| 5 regex pattern 상수 (`ENTRY_NAME_PATTERNS` + 4 검출 패턴) | 37~47 | 11 | ✅ read-only 답습 |
| `StepBlock` dataclass | 50~56 | 7 | ✅ read-only 답습 |
| `CheckResult` dataclass (`is_violation` method 포함) | 59~68 | 10 | ✅ read-only 답습 |
| `IntegrationReport` dataclass (`violations` property 포함) | 71~79 | 9 | ✅ read-only 답습 |
| `extract_steps()` 함수 (YAML step 추출 heuristic) | 82~121 | 40 | ✅ read-only 답습 |
| `is_entry_step()` 함수 (entry pattern 매칭) | 124~125 | 2 | ✅ read-only 답습 |
| `check_pc3()` 함수 (PC-3 검증) | 128~139 | 12 | ✅ read-only 답습 |
| `_strip_comments()` helper (shell `#` 주석 제거) | 142~171 | 30 | ✅ read-only 답습 |
| `check_ar1()` 함수 (AR-1 fail-closed 검증 — `exit 1` OR `set -e`) | 174~205 | 32 | ✅ read-only 답습 |
| `run_checks()` 함수 (전체 실행) | 208~219 | 12 | ✅ read-only 답습 |
| `print_report()` 함수 (출력) | 222~239 | 18 | ✅ read-only 답습 |
| `list_checks()` 함수 (--list-checks self-check) | 242~258 | 17 | ✅ read-only 답습 |
| `main()` 함수 (CLI entry point + argparse) | 261~294 | 34 | ✅ read-only 답습 |
| `if __name__ == "__main__":` block | 297~298 | 2 | ✅ read-only 답습 |
| **합산** | — | **298** | **✅ 100% read-only 답습** |

### 3.2 tool 호출 인터페이스 매트릭스 (Stage 4 step 답습)

| 인터페이스 | 호출 방식 | 본 brief 답습 |
|---------|--------|----------|
| `python tools/mvp1_pc3_ar1_integration_check.py <workflow1.yml> <workflow2.yml> <workflow3.yml> --mode integration` | 3 workflow 동시 호출 (cross-workflow integration check) | ✅ 답습 — 3 MVP-1 workflow Stage 4 step line 323~327 wired |
| `python tools/mvp1_pc3_ar1_integration_check.py <fixture.yml> --mode integration` | PASS fixture 1 + FAIL fixture 2 verify | ✅ 답습 — 3 MVP-1 workflow Stage 4 step line 329~341 wired |
| `python tools/mvp1_pc3_ar1_integration_check.py --list-checks` | self-check 항목 출력 | ✅ 답습 — 3 MVP-1 workflow Stage 4 step line 354 wired |
| **합산** | **3 호출 인터페이스** | **✅ 3/3 wired + 4 prerequisite run SUCCESS 답습** |

### 3.3 tool 3 mode 매트릭스

| Mode | 영역 | 본 brief 답습 |
|----|-----|----------|
| `--mode pc3` | PC-3 단독 (CI-only enforcement — `continue-on-error: true` 위반 검출) | ✅ read-only 답습 |
| `--mode ar1` | AR-1 단독 (fail-closed pattern — `exit 1` OR `set -e` 부재 검출) | ✅ read-only 답습 |
| `--mode integration` | **PC-3 + AR-1 양 검증** (Stage 4 step 답습 — default) | ✅ Stage 4 step 답습 — default mode |
| **합산** | **3 mode** | **✅ 3/3 read-only 답습 — Stage 4 step = integration mode 한정** |

### 3.4 tool rc (exit code) semantics 매트릭스

| 조건 | rc | 본 brief 답습 |
|----|---|----------|
| PASS (entry step 1+ + violation 0건) | 0 | ✅ Stage 4 step 답습 — Stage 4 step pass 기준 |
| FAIL (violation 1+) | 1 | ✅ Stage 4 step 답습 — FAIL fixture 의 expected rc=1 답습 |
| no entry steps found | 1 | ✅ `::error::no entry steps found` 메시지 출력 + rc=1 답습 (line 291~293) |
| file not found | 1 | ✅ `::error::file not found: ...` 메시지 출력 + rc=1 답습 (line 283~287) |
| --list-checks 단독 호출 | 0 | ✅ self-check 출력 후 rc=0 (line 275~277) |
| 인자 부재 + --list-checks 부재 | 2 (argparse error) | ✅ `parser.error()` 답습 (line 280) |

### 3.5 LVE 12/12 PASS evidence 답습 매트릭스 (`4ce5a0b` LVE §6.1 답습)

| 검증 영역 | LVE 결과 | 본 brief 답습 |
|---------|-------|----------|
| `python -m py_compile tools/mvp1_pc3_ar1_integration_check.py` | ✅ PASS | ✅ 답습 한정 |
| `python tools/mvp1_pc3_ar1_integration_check.py --list-checks` | ✅ PASS (rc=0) | ✅ 답습 한정 |
| 3 MVP-1 workflow Stage 4 cross-verify | ✅ PASS (rc=0) | ✅ 답습 한정 |
| PASS fixture verify (`tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml`) | ✅ PASS (rc=0) | ✅ 답습 한정 |
| FAIL fixture verify — PC-3 violation | ✅ FAIL detected (rc=1) | ✅ 답습 한정 |
| FAIL fixture verify — AR-1 violation | ✅ FAIL detected (rc=1) | ✅ 답습 한정 |
| `--mode pc3` 단독 | ✅ PASS | ✅ 답습 한정 |
| `--mode ar1` 단독 | ✅ PASS | ✅ 답습 한정 |
| `--mode integration` (default) | ✅ PASS | ✅ 답습 한정 |
| 한국어 shell comment FAIL fixture 안전성 | ✅ PASS (`_strip_comments` heuristic 답습) | ✅ 답습 한정 |
| missing file 처리 | ✅ rc=1 + `::error::file not found:` 답습 | ✅ 답습 한정 |
| no entry step 처리 | ✅ rc=1 + `::error::no entry steps found` 답습 | ✅ 답습 한정 |
| **합산** | **12/12 PASS** | **✅ 100% 답습 한정** |

### 3.6 4 prerequisite run answer 답습 (W-1 brief §3.3 답습)

| 영역 | 답습 |
|------|----|
| Stage 4 step 본문 = 이미 wired (`secret-hygiene-egress-redaction.yml` line 318~360) | ✅ W-1 = 0-line passthrough 합의 답습 |
| 3 MVP-1 workflow 4 prerequisite run SUCCESS (Phase α-1/α-2/α-3) | ✅ LVE §4 답습 |
| tool 본문 변경 = 4 prerequisite run JSON conclusion 변경 가능성 영역 | ⚠️ **본 brief 핵심 평가 영역** — behavior 변경 시 → 12/12 PASS evidence 변경 위험 |

### 3.7 본 §3 의 *범위 한계*

본 §3 = **read-only 답습 매트릭스 한정**. 본 §3 의 어떤 항목도 *변경* / *재해석* / *재합의* 영역이 아니며, 단순히 *현재 상태* 답습 enumerate 한정. tool 본문 변경 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. Micro-patch 후보 영역 *enumerate 한정*

### 4.1 변경 line 결정 옵션 매트릭스 (C-υ-44 답습 — 3 영역 동시 발효 + C-φ-30 답습)

C-υ-44 답습 결정 영역 (Stage 4 entry brief 합의 §5.3 답습) + C-φ-30 답습 (W-1 = 0-line passthrough 고정) = **3 영역 동시 발효**:

| Agent 영역 | 권고 | 본 brief 채택 영역 |
|---------|----|---------------|
| Agent A (절차) — C-A6 | W-N micro-patch 범위 결정 = *별도 brief 후 합의* | ✅ **본 brief = cycle 2/4 별도 brief 진입** (C-A6 발효) |
| Agent B (안전성) — C-B6 | PC-3 / AR-1 step 순서 변경 = §5.5.1+§5.5.2 본문 변경 시도 *권고 0건* 영구 답습 (T-3 발화 영역 모호성 청산) | ✅ **본 brief = behavior 변경 0건 영구 답습 + 변경 영역 = comment / help-text / error-message 한정 영구 답습** |
| Agent C (단순성) — C-C1 | 변경 line *0 lines 우선 권고 강화* (옵션 (iv)) | ✅ **본 brief 권고 시작점 = (i) 변경 0 lines 우선 권고** |
| **W-1 합의 답습 C-φ-30** | W-1 = 0-line passthrough 고정 (LVE 12/12 PASS + 4 prerequisite run SUCCESS) | ✅ **본 brief 권고 시작점 = (i) tool 본문 변경 0 lines 우선 (LVE 12/12 PASS evidence 답습)** |

### 4.2 변경 line 결정 옵션 (사용자 결정 영역)

| 옵션 | 변경 line | 적격 영역 | 본 brief 권고 |
|-----|--------|--------|----------|
| **(i)** | **0 lines** | `tools/mvp1_pc3_ar1_integration_check.py` = 현재 상태 답습 (Stage 4 step wired + 4 prerequisite run SUCCESS + LVE 12/12 PASS) | ✅ **권고 시작점 (C-υ-44 답습 + C-φ-30 답습 — 변경 0 lines 우선)** |
| (ii) | ≤ 3 lines | 답습 출처 헤더 주석 (line 1~23) 보강 — W-1 합의 commit `df741a2` 답습 추가 (보강 3 라인) | 옵션 (사용자 결정 영역) — comment-only 변경 한정 |
| (iii) | ≤ 5 lines | `list_checks()` (line 242~258) self-check 출력 보강 — 답습 메시지 추가 (W-1 0-line passthrough 답습 참조) | 옵션 (사용자 결정 영역) — print-string-only 변경 한정 |
| (iv) | ≤ 10 lines | (ii) + (iii) + 에러 메시지 보강 (line 286 `::error::file not found:` + line 292 `::error::no entry steps found`) | 옵션 (사용자 결정 영역) — error-message-only 변경 한정 |
| (v) | ≤ 15 lines | (iv) + argparse `description` / `help` 텍스트 보강 (line 263 + line 268~272) | 옵션 (Stage 4 entry brief §3.1 답습 — 권고 한계 상한, comment/help/error-message 한정) |
| (vi) | ≥ 16 lines | Stage 4 entry brief §3.1 답습 영역 외 (별도 합의 필요) | ❌ **비권고** |
| (vii) | **regex / logic / mode / rc / dataclass schema 변경** (behavior change) | `ENTRY_NAME_PATTERNS` / `PC3_VIOLATION_PATTERN` / `AR1_EXIT_PATTERN` / `AR1_SET_E_PATTERN` / `STEP_HEAD_PATTERN` 변경 OR `extract_steps` / `check_pc3` / `check_ar1` 본문 logic 변경 OR dataclass 필드 변경 OR rc semantics 변경 | ❌ **비권고** (C-υ-44 답습 — T-3 발화 영역 — **12/12 PASS evidence 변경 위험**) |
| (viii) | **dependency 추가** (pyyaml / 외부 패키지 도입) | stdlib-only 답습 변경 = T-3 영역 (의존성 풍선 + α-1+2+3 evidence 패턴 답습 위반) | ❌ **비권고** (영구 답습) |
| (ix) | **entry point 변경** (CLI 인자 의미 / `--mode` choices 변경 / 새 sub-command 추가) | 3 MVP-1 workflow Stage 4 step 호출 인터페이스 답습 위반 영역 | ❌ **비권고** (W-1 = 0-line passthrough 답습 위반 영역) |

### 4.3 옵션 (ii)~(v) 의 *근거 영역* enumerate (참고 한정)

본 §4.3 = 옵션 (ii)~(v) 의 *근거 enumerate 한정* — 채택 권고 0건. 변경 line 결정 = 사용자 명시 결정 영역.

**옵션 (ii) 근거 (답습 출처 헤더 주석 보강 가능성)**:
- 현재 답습 출처 헤더 (line 4~8) = 4개 doc 답습 — W-1 합의 (`df741a2`) 미답습 영역
- W-1 합의 발효 후 답습 출처 갱신 가능성 = 3 lines 추가 (boilerplate comment 한정)
- 본 brief 권고: ❌ **비권고** — 답습 출처 = 새 합의 시점 별도 갱신 영역 (자동 진입 X)

**옵션 (iii) 근거 (`list_checks()` 출력 보강 가능성)**:
- 현재 `list_checks()` 출력 = "Out of scope" 4 영역 enumerate (line 254~258)
- W-1 합의 후 추가 영역 enumerate 가능성: "W-1 = 0-line passthrough 답습" 라인 1+ 추가 가능성 (≤ 5 lines)
- 본 brief 권고: 옵션 (사용자 결정 영역) — print-string-only 변경 한정 → behavior 변경 0건

**옵션 (iv) 근거 (에러 메시지 보강 가능성)**:
- 현재 에러 메시지 2 영역: line 286 `::error::file not found: {m}` + line 292 `::error::no entry steps found — Stage 4 통합 검증 부적격 (Stage 1/2/3 PASS 선행 의무)`
- 메시지 자체 한국어 + 영어 mixed — 일관성 미세 정정 가능성 (단, behavior = exit code 변경 0건)
- 본 brief 권고: 옵션 (사용자 결정 영역) — error-message-only 변경 한정 → behavior 변경 0건

**옵션 (v) 근거 (argparse description/help 보강 가능성)**:
- 현재 argparse description (line 263) = "Stage 4 PC-3 + AR-1 통합 정적 검증 도구 (CI-only enforcement + fail-closed)"
- `--mode` help (line 268~272) + `files` help (line 265) + `--list-checks` help (line 272) — 모두 한 줄
- Stage 4 entry brief §3.1 답습 권고 한계 상한 = ≤ 15 lines micro-patch 권고 시작점
- 단 C-υ-44 + C-φ-30 답습 = 변경 0 lines 우선 권고 강화 → 옵션 (v) 까지 도달은 사용자 명시 결정 영역

### 4.4 영역 외 변경 enumerate (본 brief 비권고 영구 답습)

| 영역 | 사유 |
|------|-----|
| `ENTRY_NAME_PATTERNS` 변경 (entry step 식별 regex) | LVE 12/12 PASS evidence 답습 영역 — T-3 발화 영역 (C-υ-44 답습) |
| `PC3_VIOLATION_PATTERN` 변경 (PC-3 검출 regex) | 동상 — behavior 변경 영역 |
| `AR1_EXIT_PATTERN` / `AR1_SET_E_PATTERN` 변경 | 동상 — fail-closed 인정 패턴 = §5.5.2 본문 답습 영역 (`set -e` 답습 — C-υ-44 답습 T-3 발화 영역) |
| `STEP_HEAD_PATTERN` 변경 | 동상 — step extraction heuristic 답습 영역 |
| `extract_steps()` body logic 변경 | LVE §6.1 12/12 PASS evidence 변경 위험 |
| `_strip_comments()` body logic 변경 | 한국어 shell comment 안전성 답습 (LVE §6.1 답습) — T-3 발화 영역 |
| `check_pc3()` / `check_ar1()` body logic 변경 | PC-3 / AR-1 검증 본질 변경 영역 — §5.5.1+§5.5.2 본문 변경 (T-3 발화 영역) |
| `run_checks()` / `print_report()` body logic 변경 | report 구조 / 출력 형식 변경 영역 — Stage 4 step grep 답습 변경 위험 |
| dataclass `StepBlock` / `CheckResult` / `IntegrationReport` 필드 변경 | schema 변경 영역 — Stage 4 step grep 답습 변경 위험 |
| `main()` argparse 구조 변경 | CLI 인터페이스 변경 — 3 MVP-1 workflow Stage 4 step 호출 답습 위반 |
| dependency 추가 (pyyaml / 외부 패키지) | stdlib-only 답습 위반 (α-1+2+3 evidence 패턴 답습 위반) |
| 새 `--mode` choice 추가 | CLI 인터페이스 변경 — Stage 4 step 호출 답습 위반 |
| 새 sub-command 추가 | 동상 |
| rc semantics 변경 | Stage 4 step 의 `rc=1 expected for FAIL fixtures` 답습 위반 |
| Stage 4 step (line 318~360) 본문 변경 | W-1 = 0-line passthrough 합의 답습 위반 영역 (cycle 2/4 ≠ cycle 1/4 영역) |
| 3 MVP-1 workflow 본문 변경 | W-1 = 0-line passthrough 합의 답습 영구 (사용자 명시 #2 답습) |
| `permissions: contents: read` 보강 | W-5 영역 = 본 brief 영역 외 (사용자 명시 #3 + #4 답습) |
| Required check / branch protection 등록 | W-6 / W-8 영역 = 본 brief 영역 외 |
| `pull_request_target` event 도입 | Stage 5 cycle 2 영역 = 본 brief 영역 외 |
| `secrets.*` reference 도입 | F-금지 #1 영구 답습 |
| 신규 trigger event (`workflow_dispatch` / `schedule` / `repository_dispatch`) | W-4 영역 = 본 brief 영역 외 (사용자 명시 #3) |
| 신규 tool 신설 | T2/T3 별도 합의 영역 |
| 신규 fixture 추가 | W-3 영역 = 본 brief 영역 외 (cycle 3/4 별도) |

### 4.5 변경 line 권고 시작점 매트릭스

| 영역 | 변경 line 권고 시작점 | 사용자 결정 옵션 상한 |
|----------|------------------|-------------------|
| `tools/mvp1_pc3_ar1_integration_check.py` (298줄) | **0 lines** | ≤ 15 lines (옵션 (v) — comment/help/error-message 한정 영구 답습) |
| **합산** | **0 lines (권고 시작점)** | **≤ 15 lines (옵션 (v) 상한, behavior 변경 0건 영구 답습)** |

### 4.6 본 §4 의 *범위 한계*

본 §4 = **변경 line 결정 *옵션 enumerate 한정***. 본 §4 의 어떤 항목도:
- (i) 옵션 (i)~(v) 中 어느 것도 *채택 발효* 시키지 않으며,
- (ii) 변경 line *최종 확정* 시키지 않으며,
- (iii) tool 본문 어느 줄도 *변경* 하지 않으며,
- (iv) behavior (regex / logic / mode / rc / dataclass schema) 어느 것도 *변경* 하지 않으며,
- (v) dependency 어느 것도 *추가* 하지 않는다.

권고 시작점 = **옵션 (i) 변경 0 lines** (C-υ-44 + C-φ-30 답습 + LVE 12/12 PASS evidence 답습) — 실 변경 결정 = 사용자 명시 결정 영역.

---

## 5. W-2 검증 방법 권고

### 5.1 PRE-0 도구 가용성 사전 점검 (C-υ-38 답습)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| PRE-0-1 | Python version ≥ 3.12 | `python --version` | rc=0 + ≥ 3.12 (`from __future__ import annotations` + `dataclasses` + `re` 답습) |
| PRE-0-2 | `python -m py_compile` 가용성 | `python -m py_compile --help` | rc=0 |
| PRE-0-3 | `git` version | `git --version` | rc=0 + version enumerate |
| PRE-0-4 | `gh CLI` 인증 상태 (옵션) | `gh auth status` | rc=0 + 인증 답습 (PRE 영역 한정 — 신규 actual run trigger 0건) |
| PRE-0-5 | `yamllint` 가용성 (W-1 답습 — fixture YAML 검증 영역 옵션) | `yamllint --version` | rc=0 (옵션 — W-2 검증 = py_compile + --list-checks 단독 한정) |

### 5.2 W-2-V1 ~ W-2-V8 검증 (W-1 brief §5.2 답습 + tool 특화 확장)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-2-V1 | `tools/mvp1_pc3_ar1_integration_check.py` Python syntax 검증 | `python -m py_compile tools/mvp1_pc3_ar1_integration_check.py` | rc=0 + stderr 비어 있음 |
| W-2-V2 | `--list-checks` self-check 동작 검증 | `python tools/mvp1_pc3_ar1_integration_check.py --list-checks` | rc=0 + 8+ 영역 enumerate (PC-3 + AR-1 + entry pattern 2 + out-of-scope 4 영역) |
| W-2-V3 | 3 MVP-1 workflow integration mode 통합 검증 | `python tools/mvp1_pc3_ar1_integration_check.py .github/workflows/secret-hygiene-egress-redaction.yml .github/workflows/provider-adapter-enforcement.yml .github/workflows/provider-url-scanner.yml --mode integration` | rc=0 + violations=0 (PASS 답습 — LVE §6.1 답습) |
| W-2-V4 | PASS fixture 검증 — `compliant_entry_step.yml` | `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/pass/compliant_entry_step.yml --mode integration` | rc=0 + violations=0 |
| W-2-V5 | FAIL fixture PC-3 검증 — `continue_on_error_violation.yml` | `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/fail/continue_on_error_violation.yml --mode integration` | rc=1 + PC-3 FAIL detected |
| W-2-V6 | FAIL fixture AR-1 검증 — `missing_fail_closed.yml` | `python tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/fail/missing_fail_closed.yml --mode integration` | rc=1 + AR-1 FAIL detected |
| W-2-V7 | `--mode pc3` + `--mode ar1` 단독 mode 검증 (각 mode 답습) | `python tools/mvp1_pc3_ar1_integration_check.py <3 workflow> --mode pc3` + (동상 `--mode ar1`) | rc=0 + violations=0 (각 mode) |
| W-2-V8 | missing file + no entry steps 에러 처리 검증 | `python tools/mvp1_pc3_ar1_integration_check.py /nonexistent.yml --mode integration` + `python tools/mvp1_pc3_ar1_integration_check.py /dev/null --mode integration` | rc=1 + 적절한 `::error::...` 메시지 출력 (stderr) |

### 5.3 신규 actual run trigger 검증 매트릭스

| 영역 | 본 brief 권고 |
|------|----------|
| W-4 신규 actual run trigger | ❌ **0건 영구 답습** (사용자 명시 #3 답습) |
| Pre-implementation 검증 = local 한정 | ✅ 신규 actual run trigger 0건 (PRE-0-1 ~ W-2-V8 모두 local 표준 도구 한정) |
| 본 brief 시점 신규 actual run trigger | **0건** |

### 5.4 검증 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `python -m py_compile` | Python syntax 검증 | stdlib 한정 답습 — 신규 도입 0건 |
| `python tools/mvp1_pc3_ar1_integration_check.py` | tool 자체 self-check + 3 mode + --list-checks | 답습 한정 — 본 brief 시점 변경 0건 |
| `grep` | --list-checks 출력 영역 enumerate | 표준 도구 답습 |
| `diff` (옵션) | tool 본문 답습 변경 확인 (옵션 (i) 채택 시 변경 0 lines verify) | 표준 도구 답습 |
| `gh CLI` (옵션) | 4 prerequisite runs 답습 시점 ↔ 본 brief 시점 시간 경과 재검증 (PRE-3 영역 — Stage 4 entry brief 답습) | 답습 한정 (read-only) |
| `yamllint` | (W-1 영역 — 본 brief 영역 외) | ❌ 0건 (cycle 1/4 답습 — W-1 = 0-line passthrough 고정) |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 5.5 LVE 12/12 PASS evidence 답습 검증 (read-only)

| 영역 | 답습 |
|------|----|
| LVE §6.1 12/12 PASS | ✅ 답습 한정 — 본 brief 시점 재실행 0건 (옵션 (i) 0 lines = 자동 답습) |
| 본 brief 변경 = LVE 12/12 PASS evidence 변경 위험 | ⚠️ **본 brief 핵심 평가 영역** — 옵션 (vii) behavior 변경 시 → LVE 재집계 필요 영역 (T-3 발화 영역) |
| 옵션 (i)~(v) (comment/help/error-message 한정) 변경 시 LVE 영향 | ✅ **0건 영구 답습** (behavior 변경 0건 → 12/12 PASS evidence 보존) |

### 5.6 본 §5 의 *범위 한계*

본 §5 = **W-2 검증 방법 *권고 한정***. 실 검증 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 본 §5 의 어떤 항목도 신규 actual run trigger 0건 영구 답습 + W-1 / W-3 / W-4 검증 영역 *통합 0건*.

---

## 6. W-2 시점 rollback trigger 발화 가능성 매트릭스

### 6.1 Layer B 18 trigger × W-2 시점 발화 매트릭스 (Stage 4 entry brief §6.1 답습)

| # | trigger 영역 | W-2 본문 변경 0 lines 시점 발화 | W-2 본문 변경 ≤ 15 lines (comment/help/error-message 한정) 시점 발화 | W-2 본문 변경 옵션 (vii) (behavior change) 시점 발화 |
|---|---------|---------------------------|----------------------------|----------------------------|
| 13 | CI step pass with violation present (PC-3) | 0건 (tool behavior 변경 0건) | 0건 (behavior 변경 0건) | **발화 가능성** (옵션 (vii) — `PC3_VIOLATION_PATTERN` 변경 시 = 비권고 영역) |
| 14 | CI step fail without auto-reject (AR-1) | 0건 (tool behavior 변경 0건) | 0건 (behavior 변경 0건) | **발화 가능성** (옵션 (vii) — `AR1_EXIT_PATTERN` / `AR1_SET_E_PATTERN` 변경 시 = 비권고 영역) |
| 15 | PR check unstable / flaky | 0건 (신규 actual run trigger 0건) | 0건 (W-4 영역 외) | 0건 (W-4 영역 외) |
| **합산 (18 중)** | **18 trigger** | **0/18 발화** | **0/18 발화** (comment/help/error-message 한정 — behavior 변경 0건) | **2/18 발화 가능성 (옵션 (vii) 한정 — 본 brief 비권고)** |

### 6.2 TR-1 ~ TR-5 × W-2 시점 발화 매트릭스

| TR # | 영역 | W-2 시점 발화 |
|----|----|------------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 | 0건 (Phase α-2 영역) |
| TR-2 | `include_external_packages` flag | 0건 |
| TR-3 | `root_packages` 변경 | 0건 |
| TR-4 | `ignore_imports` 변경 | 0건 |
| TR-5 | google.generativeai facade | 0건 |
| **합산** | **5 trigger** | **0/5 발화 영구 답습** |

### 6.3 Step Division + Stage 4 신규 후보 × W-2 시점 발화 매트릭스

| # | trigger | W-2 본문 변경 0 lines | W-2 본문 변경 ≤ 15 lines (comment/help/error-message) | W-2 본문 변경 옵션 (vii) (behavior change) |
|---|-------|-------------------|-----------------------|-----------------------|
| ND-1 | PC-3 self-check FAIL (local) | 0건 | 0건 (behavior 변경 0건) | **발화 가능성** (옵션 (vii) 시 — 비권고) |
| ND-2 | AR-1 self-check FAIL (local) | 0건 | 0건 (behavior 변경 0건) | **발화 가능성** (옵션 (vii) 시 — 비권고) |
| ND-3 | **integration check tool self-check FAIL** | 0건 (tool 변경 0건) | **발화 가능성 (LVE 12/12 PASS evidence 답습 변경 위험)** | **발화 가능성** (옵션 (vii) 시 — 비권고) |
| ND-4 | 4 prerequisite runs JSON conclusion 미답습 | 0건 (PRE 영역) | 0건 | 0건 |
| ND-5 | LVE 본문 누락 | 0건 (PRE 영역) | 0건 | 0건 |
| **합산** | **5 후보** | **0/5 발화** | **1/5 발화 가능성 (ND-3 한정 — comment/help/error-message 영역에서도 self-check 출력 형식 변경 시 grep 답습 위반 가능성 영역)** | **3/5 발화 가능성 (옵션 (vii) 한정)** |

### 6.4 W-2 시점 발화 합산 매트릭스

| 옵션 | Layer B | TR-1~5 | Step Division 신규 | 합산 발화 가능성 |
|-----|---------|------|----------------|--------------|
| **(i) 0 lines (권고 시작점)** | 0/18 | 0/5 | 0/5 | **0/28 발화 영구 답습** |
| (ii) ≤ 3 lines (답습 출처 헤더 보강) | 0/18 | 0/5 | 0/5 | **0/28 발화** (comment-only — behavior 0건) |
| (iii) ≤ 5 lines (`list_checks()` 출력 보강) | 0/18 | 0/5 | **1/5 (ND-3 발화 가능성)** | **1/28 발화 가능성** — `--list-checks` 출력 형식 변경 시 Stage 4 step grep 답습 위반 가능성 영역 (단, output line append 한정 시 발화 0건 영구 답습) |
| (iv) ≤ 10 lines (에러 메시지 보강) | 0/18 | 0/5 | **1/5 (ND-3 발화 가능성)** | **1/28 발화 가능성** — `::error::` 형식 변경 시 Stage 4 step grep 답습 위반 가능성 영역 (단, 메시지 텍스트 보강 한정 시 발화 0건 영구 답습) |
| (v) ≤ 15 lines (argparse desc/help 보강) | 0/18 | 0/5 | 0/5 | **0/28 발화** (argparse desc/help = grep 답습 영역 외) |
| (vi) ≥ 16 lines | (영역 외 — 별도 합의) | (영역 외) | (영역 외) | **본 brief 비권고** |
| (vii) behavior change (regex / logic / mode / rc / dataclass schema) | 2/18 (#13 + #14) | 0/5 | 3/5 (ND-1 + ND-2 + ND-3) | **5/28 발화 가능성 — 본 brief 비권고 영역** |
| (viii) dependency 추가 | (영역 외 — stdlib-only 답습 위반) | (영역 외) | (영역 외) | **본 brief 비권고** |
| (ix) entry point 변경 | (영역 외 — Stage 4 step 호출 답습 위반) | (영역 외) | (영역 외) | **본 brief 비권고** |

**핵심 발견**: 옵션 (i)+(ii)+(v) 영역 = **0/28 발화 영구 답습**. 옵션 (iii)+(iv) 영역 = 1/28 발화 가능성 — output / error-message append 한정 시 0/28 답습 가능 영역. 옵션 (vii) (behavior change) 영역 = 5/28 발화 가능성 — **본 brief 비권고** (C-υ-44 답습 + C-φ-30 답습 — Agent B C-B6 + Agent C C-C1 + Reviewer §4.4 답습 + LVE 12/12 PASS evidence 답습).

### 6.5 Rollback 절차 권고 (C-υ-41 답습 — "즉시 rollback" 권고 한정)

| 절차 | 영역 | 권고 |
|----|----|----|
| (i) Rollback decision | trigger 발화 시 판단 | **사용자 명시 결정 영역** (자동 rollback 0건 영구 답습) |
| (ii) `git revert HEAD` | 가장 안전 — 변경 line 만 revert | **권고 시작점** |
| (iii) `git reset --hard HEAD~N` | 강제 reset (이력 변경) | ❌ **비권고** (R-4 history rewrite layer 영역) |
| (iv) 신규 `fix:` commit (revert 없이 forward fix) | micro patch forward fix | 옵션 (comment/help/error-message 한정 변경 시) |
| (v) 본 brief 시점 = 변경 line 0 = rollback 영역 0건 영구 답습 | — | **답습 한정** |
| (vi) LVE 12/12 PASS evidence 재집계 의무 발화 시점 | 옵션 (vii) behavior change 채택 시 = LVE 재집계 의무 발화 (T-3 영역) | ❌ **비권고** (본 brief = behavior 변경 0건 영구 답습) |

### 6.6 본 §6 의 *범위 한계*

본 §6 = **rollback trigger *발화 가능성 enumerate 한정***. 본 §6 의 어떤 항목도 *발화* / *rollback 절차 자동 발효* / *threshold 고정* 시키지 않는다.

---

## 7. 사용자 명시 5 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 5 금지 영역 위반 0건 영구 답습

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 결정 영역) |
|---|---------|---------------|------------------------------|
| #1 | integration tool 실 변경 | ✅ 0건 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 0건 — 본 brief = *후보 검토 한정*) | ✅ 0건 (DRAFT 영역, 사용자 결정 후 진입) |
| #2 | CI workflow 변경 | ✅ 0건 (W-1 = 0-line passthrough 고정 답습) | ✅ 0건 (W-1 합의 답습 영구) |
| #3 | actual run 재실행 | ✅ 0건 (신규 trigger 0건) | ✅ 0건 (W-4 영역 외 영구 답습) |
| #4 | Operational Readiness PASS (Layer E) | ✅ 0건 (MVP-6 영역 분리) | ✅ 0건 |
| #5 | Hermes PMO 격상 (Layer F) | ✅ 0건 (ADR-008 부록 C 12 조건 미충족) | ✅ 0건 |
| **합산** | **5** | **✅ 5/5 위반 0건** | **✅ 5/5 위반 0건** |

### 7.2 W-2 옵션별 5 금지 위반 매트릭스

| 옵션 | #1 | #2 | #3 | #4 | #5 | 합산 |
|-----|----|----|----|----|----|-----|
| (i) 0 lines | ✅ 0 (현재 상태 답습) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건** |
| (ii)~(v) comment/help/error-message ≤ 15 lines | ✅ 0 (본 brief 시점) — Stage 4 실 구현 시점 = #1 해소 (사용자 결정) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건 (본 brief 시점)** |
| (vi) ≥ 16 lines | ❌ **위반 가능성** (Stage 4 entry brief §3.1 답습 영역 외 — 별도 합의 필요) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (vii) behavior change | ❌ **위반 가능성** (§5.5.1+§5.5.2 본문 변경 영역 — C-υ-44 답습 비권고 + LVE evidence 변경 위험) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (viii) dependency 추가 | ❌ **위반 가능성** (stdlib-only 답습 위반) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (ix) entry point 변경 | ❌ **위반 가능성** (Stage 4 step 호출 답습 위반 — W-1 = 0-line passthrough 답습 위반 영역 가능) | ⚠️ 위반 가능성 (Stage 4 step 호출 답습 영역) | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |

### 7.3 Backlog 분리 매트릭스

| Backlog | 영역 | 본 brief 영역 |
|---------|----|----------|
| Backlog #1 (PC-4 local pre-commit hook 활성화) | `.pre-commit-config.yaml` 신설 | ❌ 본 brief 영역 외 (사용자 명시 #3 답습 — W-7) |
| Backlog #2 (dev 환경 강제 + pre-commit install 의무화) | dev 환경 검증 강제 | ❌ 본 brief 영역 외 (W-7 영역) |
| Backlog #3 T3 (AR-2 branch protection + AR-3 자동 revert bot) | branch protection API + CODEOWNERS | ❌ 본 brief 영역 외 (W-6 + W-8 + W-9 영역) |
| Backlog #4 (facade.py real 본문 작성) | `src/adapters/llm/facade.py` real 본문 | ❌ 본 brief 영역 외 |
| Backlog #5 (event enum / ledger entry 정식 등록) | ADR-012 §2.2 영역 | ❌ 본 brief 영역 외 (후보 한정) |
| Backlog #6 (Hermes PMO 격상 영역) | ADR-008 부록 C 12 조건 영역 | ❌ 본 brief 영역 외 (사용자 명시 #5 답습) |
| Stage 5 (G3-7 4 항목) | secret reset rotate / fork PR / pull_request_target / commit signing | ❌ 본 brief 영역 외 (W-10 영역) |
| **W-1 cycle 1/4 (3 MVP-1 workflow micro-patch)** | 3 workflow 1206줄 | ❌ 본 brief 영역 외 (cycle 1/4 답습 — 0-line passthrough 고정) |
| **W-3 / W-4 cycle 3/4 / 4/4** | 3 fixture / actual run trigger | ❌ 본 brief 영역 외 (사용자 명시 #3 답습) |

### 7.4 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 5 금지 영역 + Backlog 분리 영역 + W-1 / W-3 / W-4 cycle 분리 영역 어느 것도 *해소* / *통합* 시키지 않는다.

---

## 8. 합산 468 합의 조건 답습 매트릭스

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
| **Phase α-4 R-1 Stage 4 W-1 (cycle 1/4)** | **`df741a2`** | **30 (C-φ-1 ~ C-φ-30)** | **0건** ✅ |
| **합산** | **17 합의** | **468 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| **C-φ-30** (W-1 = 0-line passthrough 고정) | ✅ §1.2 + §2.1 + §2.2 + §4.1 + §7.1 답습 (영구 답습 — W-1 재진입 0건) |
| **C-υ-43** (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록) | ✅ **본 brief = cycle 2/4 (W-2 단독) 진입 — C-υ-43 발효** |
| **C-υ-44** (W-N micro-patch 범위 결정 3 영역 동시 발효 — 절차 A + 안전성 B + 단순성 C) | ✅ §4.1 + §4.2 답습 — 변경 0 lines 우선 권고 시작점 + behavior 변경 비권고 |
| C-υ-6 (W-N ≤ 15 lines micro-patch 권고 시작점) | ✅ §4.2 옵션 (v) 답습 (상한 한정 — comment/help/error-message 한정) |
| C-υ-12 (W-N 검증 영역) | ✅ §5.2 답습 (W-2-V1 ~ W-2-V8 확장) |
| C-υ-38 (PRE-0 도구 가용성 사전 점검) | ✅ §5.1 답습 (Python 3.12 + py_compile + git + gh + yamllint 옵션) |
| C-υ-41 ("즉시 rollback" 권고 한정 명시 강화) | ✅ §6.5 답습 |
| C-υ-42 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) | ✅ Post-implementation 검증 시점 답습 한정 (cycle 3/4 + cycle 4/4 영역) |
| C-υ-1 (brief 11 영역 점검 100% 채택) | ✅ §0.1 답습 |
| C-υ-3 (W-1~W-4 최소 영역 + W-5~W-10 분리) | ✅ §2.3 답습 |
| C-υ-4 (사용자 명시 3 금지 3/3 영구 답습) | ✅ §7.1 답습 (5 금지로 확장 + 3 금지 답습) |
| C-υ-5 (영구 5 금지 Stage 4 시점 해소 매트릭스) | ✅ §7.1 답습 |
| C-υ-10 (R-4 / R-5 / R-7 / src / docker block / placeholder 변경 0건) | ✅ §0.5 답습 |
| C-υ-19 (Actual run trigger event 권고) | ✅ §5.3 답습 (W-4 영역 외 명시) |
| C-υ-29 (합산 합의 조건 변경 0건) | ✅ §8.1 답습 |
| C-υ-34 (5 영구 핵심 제약 5/5 보존) | ✅ §9 + §12 답습 |
| C-υ-35 (Provider Liquidity 5-way 100% 보존) | ✅ §9 + §12 답습 |
| C-υ-36 (F-금지 #1 영구 답습) | ✅ §0.5 + §12 답습 |
| C-υ-37 (W-N 최종 확정 발효 0건) | ✅ §0.6 답습 |
| C-υ-45 (cache poisoning 후보 한정) | ✅ §10.2 답습 |
| C-υ-46 (artifact 사후 변조 후보 한정) | ✅ §10.2 답습 |
| C-υ-49 (30 trigger combined fire 후보 한정) | ✅ §6.4 답습 |
| **C-φ-1 ~ C-φ-29** (W-1 brief §11.2 답습 29 조건) | ✅ §8.1 + §10 답습 — 본 brief 영역 답습 한정 |

### 8.3 본 §8 의 *범위 한계*

본 §8 = **468 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = §11.2 (C-χ-1 ~ C-χ-N) 한정 — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정 (합의 보고서 작성 시 정식 등록).

---

## 9. 합의 형태 권고 + 풀 3+1 승격 트리거 분석

### 9.1 본 brief 자체 합의 형태 권고

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| **(a) Reviewer-only 단축 합의** | 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ✅ **권고 시작점** — 본 brief = W-2 단독 micro-patch *가능성 검토* DRAFT + W-1 = 0-line passthrough 답습 + W-3/W-4 분리 + W-5~W-10 분리 + 변경 0 lines 권고 시작점 + comment/help/error-message ≤ 15 lines 한정 → T-2 발화 *영역 한계* (Stage 4 entry brief 합의 시점 이미 발화 완료 — 본 brief = 그 권위 답습 한정) |
| (b) 풀 3+1 합의 | 트리거 中 1+ 발화 | ⚠️ **부분 적격** — 본 brief = Stage 4 entry brief 합의 §8 답습 cycle 2/4 영역 한정 → T-2 발화 *재발화 영역 한계* (Stage 4 entry brief 합의 시점 이미 발화) — 풀 3+1 합의 권위 답습 가능 (옵션) |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | ❌ **비권고** — W-2 단독 영역 + comment/help/error-message ≤ 15 lines 한정 → T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 |

**권고**: 본 brief = **(a) Reviewer-only 단축 합의 (권고 시작점)** — Stage 4 entry brief 합의 시점 (`81472ba`) 이미 T-2 발화 + W-1 합의 시점 (`df741a2`) 답습 영역 권위 답습 완료. 본 brief = cycle 2/4 한정 + comment/help/error-message ≤ 15 lines 영역 한계 + 변경 0 lines 권고 시작점 + behavior 변경 비권고 → 풀 3+1 트리거 재발화 *영역 한계* — Reviewer-only 단축 합의 *적격 시작점*. 단 사용자 명시 결정 시 풀 3+1 합의 (옵션 (b)) 진입 가능 영역.

### 9.2 풀 3+1 승격 트리거 검토 매트릭스 (본 brief 시점)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 본 brief 가 합산 468 합의 조건 中 1+ *재결정* 권고 | 0건 — 답습 한정 |
| T-2 | 본 brief 가 사용자 명시 영구 5 금지 영역 中 1+ *해소* 권고 | ⚠️ **재발화 영역 한계** — Stage 4 entry brief 시점 (`81472ba`) 이미 T-2 발화 완료. 본 brief = cycle 2/4 *권위 답습 한정* + comment/help/error-message ≤ 15 lines 영역 한계 → 새 T-2 발화 0건 |
| T-3 | §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 — 옵션 (vii) behavior change 비권고 명시 (§4.2 답습) — `AR1_EXIT_PATTERN` / `AR1_SET_E_PATTERN` 변경 = §5.5.2 본문 답습 변경 영역 = 본 brief 비권고 |
| T-4 | Provider Liquidity 5-way 약화 가능성 포함 | 0건 |
| T-5 | 5 영구 핵심 제약 中 1+ 약화 포함 | 0건 |
| T-6 | T3 영역 진입 권고 | 0건 — Backlog #3 분리 명시 |
| T-7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | 0건 |
| T-8 | secret handling 방식이 기존 정책 변경 권고 | 0건 |
| T-9 | Hermes upstream root of trust 변경 권고 | 0건 |
| T-10 | PC-3 + AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0건 — §2.3 + §7.3 분리 명시 |
| T-11 | 3 MVP-1 workflow 외 workflow 흡수 시도 권고 | 0건 |
| T-12 | 신규 workflow 신설 / `pull_request_target` 도입 권고 | 0건 |
| T-13 | Stage 5 (G3-7) 자동 진입 권고 | 0건 — §2.3 W-10 분리 명시 |
| T-14 | Phase α-1 / α-2 / α-3 actual run 재실행 권고 | 0건 |
| T-15 | α-1+2+3 evidence / α-4 합의 본문 변경 권고 | 0건 |
| T-16 | Stage 4 자동 실 구현 발효 권고 | 0건 — 본 brief = cycle 2/4 DRAFT 한정 |
| **합산** | **16** | **0/16 새 발화 + T-2 재발화 영역 한계** → **Reviewer-only 단축 합의 적격 시작점** |

### 9.3 외부 LLM 1+ blind 의뢰 적격성 매트릭스

| 영역 | 본 brief 적격성 |
|------|------------|
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | 비적격 — 본 brief = cycle 2/4 한정 + comment/help/error-message ≤ 15 lines 영역 + W-2 단독 영역 |
| ADR-011 §2.4 T2 영역 | 답습 한정 — 외부 LLM 의뢰 미필수 영역 |
| 본 brief 권고 | ❌ **비권고** — T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 |

### 9.4 본 §9 의 *범위 한계*

본 §9 = **합의 형태 권고 한정**. 본 brief 자체 = Reviewer-only 단축 합의 적격 시작점 (T-2 재발화 영역 한계) — 풀 3+1 합의 (옵션 (b)) 진입 = 사용자 명시 결정 영역. 외부 LLM 1+ blind 의뢰 = 비권고 (W-2 단독 영역 분리 명시).

---

## 10. 본 brief 자체 금지 + brief 발효 후 의무 금지

### 10.1 본 brief 작성 시점 금지 사항

- ❌ **integration tool 실 변경** (사용자 명시 #1) — `tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 0건
- ❌ **CI workflow 변경** (사용자 명시 #2) — 3 MVP-1 workflow 1206줄 변경 0건 (W-1 = 0-line passthrough 답습)
- ❌ **actual run 재실행** (사용자 명시 #3) — 신규 trigger 0건
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 #5)
- ❌ W-1 재진입 / W-1 합의 30 조건 변경 / W-1 = 0-line passthrough 고정 변경
- ❌ W-3 / W-4 진입 (cycle 3/4 / 4/4 분리)
- ❌ tool behavior 변경 (regex / logic / mode / rc / dataclass schema 모두 영역 외)
- ❌ tool dependency 추가 (stdlib-only 답습)
- ❌ tool entry point / CLI 인터페이스 변경
- ❌ Stage 4 step (line 318~360) 본문 변경
- ❌ §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 변경 / step 순서 변경 (옵션 (vii) — C-υ-44 답습)
- ❌ Phase α-1 / α-2 / α-3 자동 재진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 / Stage 4 entry / W-1 합의 본문 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 trigger 자동 발화
- ❌ 합산 468 합의 조건 자동 변경
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
- ❌ W-2 변경 line / 수정 영역 *최종 확정 발효* (사용자 명시 결정 영역 한정)
- ❌ `permissions: contents: read` 보강 (W-5 영역)
- ❌ Required check / branch protection 등록 (W-6 + W-8 영역)
- ❌ artifact 사후 변조 검증 도구 본문 작성 (C-υ-46 후보 한정)
- ❌ GitHub Actions cache poisoning 검증 도구 본문 작성 (C-υ-45 후보 한정)
- ❌ LVE 12/12 PASS evidence 자동 재집계 발효

### 10.2 본 brief 발효 *후* 의무 금지 사항 (사용자 명시 결정 영역)

본 brief 발효 후 *자동 진입 영역* (사용자 명시 결정 *전*):

- ❌ W-2 micro-patch 실 변경 자동 진입 0건 (사용자 명시 결정 후 진입)
- ❌ W-1 재진입 자동 0건 (W-1 = 0-line passthrough 고정 영구 답습)
- ❌ W-3 / W-4 brief 자동 작성 진입 0건
- ❌ 신규 actual run 자동 trigger 0건
- ❌ 합의 보고서 작성 자동 진입 0건 (사용자 명시 합의 형태 결정 후)
- ❌ W-5 ~ W-10 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 자동 진입 0건
- ❌ Backlog #1+#2 / Backlog #3 / Stage 5 자동 진입 0건
- ❌ 합산 468 합의 조건 자동 변경 0건
- ❌ Layer C / D / E / F 재발효 / 재선언 / 발효 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 변경 자동 진입 0건
- ❌ tool behavior / dependency / entry point 변경 자동 진입 0건

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (T-2 재발화 영역 한계 → Reviewer-only 적격 시작점) | Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-XX-phase-alpha-4-w2-micropatch.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 그대로 승인 → 풀 3+1 합의 진입 (사용자 명시 보강 결정 시) | 풀 3+1 합의 보고서 작성 |
| (C) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (D) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 |
| (E) | 본 brief 승인 → W-2 실 micro-patch 직접 진입 brief 작성 (옵션 (i) 0 lines 채택 시) | W-2 실 micro-patch (또는 변경 0건 답습) brief 별도 작성 |
| (F) | 본 brief 보류 → W-3 / W-4 cycle 우선 진입 | cycle 3/4 / 4/4 中 사용자 결정 영역 |
| (G) | 본 brief 보류 → Backlog #1+#2 / Backlog #3 / Stage 5 우선 진입 | Backlog 中 사용자 결정 영역 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 11.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 Stage 4 W-2 *micro-patch 가능성 검토 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 Stage 4 W-2 micro-patch (DRAFT, 본 commit)              ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → Reviewer-only 단축 합의 (옵션 (A), T-2 재발화 영역 한계)
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-2 실 micro-patch (옵션 (i) 0 lines 채택 시 = 변경 0건 답습 commit) 별도 brief
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-3 micro-patch (3 fixture) brief 작성 (cycle 3/4)             ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-4 신규 actual run trigger brief (cycle 4/4)                  ← 별도 결정 영역
```

### 11.2 본 brief 새 조건 후보 (Reviewer-only / 풀 3+1 합의 시 정식 등록)

본 brief 합의 시 새 조건 enumerate 후보 (C-χ-1 ~ C-χ-N):

| # | 조건 후보 | 본 brief 영역 |
|---|--------|-----------|
| C-χ-1 | 본 brief (Phase α-4 Stage 4 W-2 micro-patch *가능성 검토* DRAFT) 13 영역 점검 결과 100% 채택 | §0.1 답습 |
| C-χ-2 | W-2 cycle 2/4 framing 정합성 채택 — C-υ-43 답습 ("4 cycle 옵션 정식 등록" 발효 cycle 2/4 진입) + C-φ-30 답습 (W-1 = 0-line passthrough 고정 영구 답습) | §1.3 + §1.4 답습 |
| C-χ-3 | W-2 단독 영역 + W-1 답습 + W-3/W-4 분리 명시 + W-5~W-10 분리 명시 | §2 답습 |
| C-χ-4 | 사용자 명시 5 금지 5/5 영구 답습 (작성 시점 + 발효 후) | §7.1 답습 |
| C-χ-5 | integration tool 현재 상태 read-only 매트릭스 채택 — 298줄 답습 + 15 영역 구조 enumerate + 3 mode + 3 호출 인터페이스 + rc semantics + LVE 12/12 PASS | §3 답습 |
| C-χ-6 | 변경 line 결정 옵션 (i)~(ix) enumerate — **권고 시작점 = (i) 0 lines 우선 (C-υ-44 + C-φ-30 답습 + LVE 12/12 PASS evidence 답습)** | §4.2 답습 |
| C-χ-7 | 옵션 (ii)~(v) comment/help/error-message ≤ 15 lines = 5 금지 위반 0건 + Rollback trigger 발화 0~1/28 영구 답습 | §4.2 + §6.4 답습 |
| C-χ-8 | 옵션 (vi) ≥ 16 lines + 옵션 (vii) behavior change + 옵션 (viii) dependency 추가 + 옵션 (ix) entry point 변경 = 본 brief 비권고 (Stage 4 entry brief §3.1 영역 외 + §5.5.1+§5.5.2 본문 변경 영역 + stdlib-only 답습 위반 + Stage 4 step 호출 답습 위반) | §4.2 답습 |
| C-χ-9 | PRE-0 도구 가용성 사전 점검 5 영역 (C-υ-38 답습) — Python ≥ 3.12 / py_compile / git / gh CLI (옵션) / yamllint (옵션) | §5.1 답습 |
| C-χ-10 | W-2 검증 8 영역 (W-2-V1 ~ W-2-V8) 채택 — py_compile + --list-checks + 3 workflow integration + PASS fixture + FAIL PC-3 fixture + FAIL AR-1 fixture + pc3/ar1 단독 mode + missing/no-entry 에러 처리 | §5.2 답습 |
| C-χ-11 | 신규 actual run trigger 0건 영구 답습 — 본 brief = local 한정 (W-4 영역 외) | §5.3 답습 |
| C-χ-12 | 검증 도구 영역 — 표준 도구 답습 한정 + 신규 도입 0건 (py_compile + tool 자체 self-check + grep + diff (옵션) + gh CLI (옵션)) | §5.4 답습 |
| C-χ-13 | LVE 12/12 PASS evidence 답습 — 옵션 (i)~(v) (behavior 변경 0건) 시 LVE 재집계 의무 0건 영구 답습 | §5.5 답습 |
| C-χ-14 | Rollback Trigger 매트릭스 28 (Layer B 18 + TR-1~5 + Step Division 신규 후보 5) × W-2 시점 옵션별 발화 가능성 enumerate | §6.1 ~ §6.4 답습 |
| C-χ-15 | 옵션 (i)+(ii)+(v) 영역 = 0/28 발화 영구 답습 + 옵션 (iii)+(iv) 영역 = 1/28 발화 가능성 (ND-3 한정) + 옵션 (vii) 영역 = 5/28 발화 가능성 = 본 brief 비권고 | §6.4 답습 |
| C-χ-16 | Rollback 절차 권고 — `git revert HEAD` 권고 시작점 (C-υ-41 답습 — "즉시 rollback" 사용자 결정 영역) + behavior 변경 시 LVE 재집계 의무 발화 시점 명시 | §6.5 답습 |
| C-χ-17 | 사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 위반 0건 영구 답습 (작성 시점 + 발효 후) | §7.1 + §7.2 답습 |
| C-χ-18 | Backlog 분리 매트릭스 — #1 + #2 + #3 T3 + #4 + #5 + #6 + Stage 5 + W-1 cycle 1/4 + W-3/W-4 cycle 분리 영구 답습 | §7.3 답습 |
| C-χ-19 | 합산 468 합의 조건 답습 매트릭스 변경 0건 (17 합의 합산) | §8 답습 |
| C-χ-20 | C-φ-30 (W-1 = 0-line passthrough 고정) + C-υ-43 (4 cycle 옵션) + C-υ-44 (3 영역 동시 발효) 발효 한정 — 본 brief = cycle 2/4 (W-2) 진입 | §8.2 답습 |
| C-χ-21 | 합의 형태 권고 — 본 brief 자체 = (a) Reviewer-only 단축 합의 권고 시작점 (T-2 재발화 영역 한계) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 | §9.1 ~ §9.3 답습 |
| C-χ-22 | 본 brief 자체 금지 ≥ 50 + 본 brief 발효 후 의무 금지 ≥ 13 영구 답습 | §10 답습 |
| C-χ-23 | 다음 단계 옵션 (A) ~ (I) 사용자 결정 영역 — 권고 시작점 = (A) brief 그대로 승인 → Reviewer-only 단축 합의 | §11 답습 |
| C-χ-24 | 본 brief 메타 검증 ≥ 35 항목 | §12 답습 |
| C-χ-25 | 5 영구 핵심 제약 5/5 보존 답습 (Hermes ≠ root of trust / 단일 source-of-truth / 수단·목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) | §12 답습 |
| C-χ-26 | Provider Liquidity 5-way 100% 보존 답습 | §12 답습 |
| C-χ-27 | F-금지 #1 영구 답습 (GitHub Actions secrets 0건 + 실 API key 0건) | §12 답습 |
| C-χ-28 | W-2 변경 line / 수정 영역 *최종 확정 발효 0건* (사용자 명시 결정 영역 한정) | §0.6 답습 |
| C-χ-29 | C-υ-45 (cache poisoning) + C-υ-46 (artifact 사후 변조) 후보 한정 답습 — 본 brief 시점 정식 등록 0건 | §10.1 답습 |
| C-χ-30 | C-υ-49 (30 trigger combined fire) 후보 한정 답습 | §6.4 답습 |
| C-χ-31 | **tool behavior 변경 영구 비권고** (regex / logic / mode / rc / dataclass schema 모두 본 brief 영역 외 — §5.5.1+§5.5.2 본문 변경 영역 + LVE 12/12 PASS evidence 답습 변경 위험) | §4.2 옵션 (vii) + §4.4 답습 |
| C-χ-32 | **tool dependency 추가 영구 비권고** (stdlib-only 답습 영구 — α-1+2+3 evidence 패턴 답습 영구) | §4.2 옵션 (viii) + §4.4 답습 |
| C-χ-33 | **tool entry point / CLI 인터페이스 변경 영구 비권고** (3 MVP-1 workflow Stage 4 step 호출 답습 영역 — W-1 = 0-line passthrough 답습 위반 가능 영역) | §4.2 옵션 (ix) + §4.4 답습 |
| C-χ-34 | **LVE 12/12 PASS evidence 답습 보존 의무 영구** — 본 brief 시점 자동 재집계 발효 0건 + 옵션 (i)~(v) 시 evidence 보존 + 옵션 (vii) 시 evidence 재집계 의무 발화 영역 (비권고) | §5.5 + §6.5 답습 |
| **합산** | **34 조건 후보** | — |

### 11.3 본 §11 의 *범위 한계*

본 §11 = *결정 옵션 + 새 조건 후보 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 새 조건 발효 = 합의 보고서 작성 시 정식 등록 (Reviewer-only 또는 풀 3+1) — 본 brief 단독 = 새 조건 발효 0건.

---

## 12. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("W-2 integration tool micro-patch brief 작성, Phase α-4 Stage 4 cycle 2/4, integration tool 최소 micro-patch *가능성 검토*") |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — integration tool 실 변경 0건 / CI workflow 변경 0건 / actual run 재실행 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| W-1 합의 답습 (`df741a2`) | ✅ (30 조건 C-φ-1 ~ C-φ-30 변경 0건 + W-1 = 0-line passthrough 고정 영구 답습) |
| Stage 4 entry brief 합의 답습 (`81472ba`) | ✅ (49 조건 C-υ-1 ~ C-υ-49 변경 0건) |
| Stage 3 합의 답습 (`d3f6d59`) | ✅ (36 조건 C-τ-1 ~ C-τ-36 변경 0건) |
| LVE 합의 답습 (`b264580`) | ✅ (31 조건 C-σ-1 ~ C-σ-31 변경 0건) |
| LVE 12/12 PASS evidence 답습 (`4ce5a0b` §6.1) | ✅ 답습 한정 — 본 brief 시점 재집계 0건 (옵션 (i) 0 lines = 자동 답습) |
| Step Division 합의 답습 (`52a05cb`) | ✅ (38 조건 C-ρ-1 ~ C-ρ-38 변경 0건) |
| α-4 진입 조건 점검 합의 답습 (`1c365e7`) | ✅ (33 조건 C-π-1 ~ C-π-33 변경 0건) |
| W-1 brief 본문 답습 (`7af77fb`) | ✅ (868줄 본문 변경 0건) |
| Stage 4 entry brief 본문 답습 (`9c33efe`) | ✅ (1032줄 본문 변경 0건) |
| LVE 본문 답습 (`4ce5a0b`) | ✅ (583줄 본문 변경 0건 + 51/51 PASS 답습) |
| α-1+2+3 LVE 답습 (`7b3d40a`) | ✅ (486줄 본문 변경 0건 + 12/12 PASS 답습) |
| 합산 468 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + α-2 26 + α-3 28 + α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 parallel 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 36 + Stage 4 entry 49 + W-1 30 = 17 합의 합산) |
| C-υ-43 (W-1/W-2/W-3 4 cycle 옵션 정식 등록) 발효 — 본 brief = cycle 2/4 진입 | ✅ §1.4 + §8.2 답습 |
| C-υ-44 (W-N micro-patch 범위 결정 3 영역 동시 발효) 답습 | ✅ §4.1 + §4.2 답습 (변경 0 lines 우선 권고 시작점 + behavior 변경 비권고) |
| C-φ-30 (W-1 = 0-line passthrough 고정) 영구 답습 — W-1 재진입 0건 | ✅ §1.2 + §2.1 + §2.2 + §8.2 답습 |
| Layer A / B / C / D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ W-1 cycle 1/4 본문 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 (3 workflow 1206줄 + integration tool 298줄 + 3 fixture 89줄) |
| `tools/mvp1_pc3_ar1_integration_check.py` 298줄 본문 변경 | ✅ 0건 (본 brief = micro-patch *가능성 검토* 한정) |
| tool behavior (regex / logic / mode / rc / dataclass schema) 변경 | ✅ 0건 영구 답습 |
| tool dependency (stdlib-only) 변경 | ✅ 0건 영구 답습 |
| tool entry point / CLI 인터페이스 변경 | ✅ 0건 영구 답습 |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| 3 MVP-1 workflow 본문 변경 (본 brief 시점) | ✅ 0건 (W-1 = 0-line passthrough 답습 영구) |
| W-1 재진입 / W-3 / W-4 진입 (본 brief 시점) | ✅ 0건 (cycle 1/4 = 답습 / cycle 3/4 / 4/4 분리) |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| Rollback Trigger × W-2 시점 발화 | ✅ 옵션 (i)+(ii)+(v) = 0/28 영구 답습 / 옵션 (iii)+(iv) = 1/28 발화 가능성 (ND-3 한정) / 옵션 (vii) = 5/28 발화 가능성 (본 brief 비권고) |
| 풀 3+1 트리거 발화 | ✅ 0/16 새 발화 (T-2 = Stage 4 entry brief 시점 이미 발화 + 본 brief = 권위 답습 한정 — Reviewer-only 단축 합의 적격 시작점) |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| W-2 micro-patch 자동 실 변경 | ✅ 0건 (사용자 명시 결정 영역) |
| W-2 변경 line / 수정 영역 *최종 확정 발효* | ✅ 0건 (사용자 명시 결정 영역) |
| 본 brief framing 명시 (cycle 2/4, C-υ-43 + C-φ-30 답습) | ✅ §1.3 + §1.4 답습 |

---

## 13. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-4 R-1 Stage 4 W-1 micro-patch brief Reviewer-only 단축 합의 (`df741a2` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 30 조건 C-φ-1 ~ C-φ-30, 합산 468 합의 조건) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) Stage 4 *W-2 단독* 영역 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 한정) *최소 micro-patch 가능성 검토* brief 준비안 (DRAFT)** = **C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션) 정식 등록 답습 cycle 2/4 진입** ("*Should* W-2 introduce micro-patch lines on integration tool (and which ones), or is *0-line passthrough* the correct posture for the tool at this gate?"). **사용자 명시 5 금지** (integration tool 실 변경 / CI workflow 변경 (W-1 = 0-line passthrough 답습) / actual run 재실행 / Operational Readiness PASS / Hermes PMO 격상) 5/5 영구 답습. **integration tool 현재 상태 매트릭스** (read-only, §3) — `tools/mvp1_pc3_ar1_integration_check.py` 298줄 (stdlib-only — re/dataclasses/argparse/sys/pathlib/typing) / 15 영역 구조 enumerate (shebang/imports/5 regex/3 dataclass/9 function/main entry) / 3 mode (`--mode pc3` + `--mode ar1` + `--mode integration` default) / 3 호출 인터페이스 (3 workflow integration + fixture verify + --list-checks) / rc semantics (0=PASS / 1=violation OR missing OR no-entry) / **LVE 12/12 PASS evidence 답습** (4ce5a0b §6.1 — py_compile + --list-checks + 3 workflow integration + PASS fixture + 2 FAIL fixture + 3 mode + missing file + no entry step + 한국어 shell comment 안전성). **Micro-patch 후보 영역 *enumerate 한정*** (§4) — **C-υ-44 + C-φ-30 답습 4 영역 동시 발효** (Agent A 절차 + Agent B 안전성 + Agent C 단순성 + W-1 = 0-line passthrough 답습) → **권고 시작점 = 옵션 (i) 변경 0 lines** + 옵션 (ii) ≤ 3 lines (답습 출처 헤더 보강) + 옵션 (iii) ≤ 5 lines (`list_checks()` 출력 보강) + 옵션 (iv) ≤ 10 lines (에러 메시지 보강) + 옵션 (v) ≤ 15 lines (argparse desc/help 보강) = 사용자 결정 영역 + 옵션 (vi) ≥ 16 lines 비권고 (영역 외) + **옵션 (vii) behavior change 비권고 (regex / logic / mode / rc / dataclass schema — §5.5.1+§5.5.2 본문 변경 영역 + LVE 12/12 PASS evidence 변경 위험)** + **옵션 (viii) dependency 추가 비권고 (stdlib-only 답습 위반)** + **옵션 (ix) entry point 변경 비권고 (Stage 4 step 호출 답습 위반 — W-1 = 0-line passthrough 답습 위반 영역)**. **W-2 검증 방법 권고** (§5) — **PRE-0 도구 가용성 사전 점검 5 영역** (C-υ-38 답습 — Python ≥ 3.12 + py_compile + git + gh CLI 옵션 + yamllint 옵션) + **W-2-V1 ~ W-2-V8 8 검증** (py_compile + --list-checks + 3 workflow integration + PASS fixture + 2 FAIL fixture + pc3/ar1 단독 mode + missing/no-entry 에러 처리) = **신규 actual run trigger 0건 영구 답습** (local 한정) + **LVE 12/12 PASS evidence 보존** (옵션 (i)~(v) 시 자동 보존 + 옵션 (vii) 시 재집계 의무 영역 = 비권고). **W-2 시점 rollback trigger 발화 매트릭스** (§6) — Layer B 18 + TR-1~5 + Step Division 신규 후보 5 = 28 trigger × 옵션별 발화 가능성 → **옵션 (i)+(ii)+(v) = 0/28 발화 영구 답습** + 옵션 (iii)+(iv) = 1/28 발화 가능성 (ND-3 한정 — output/error-message append 한정 시 0/28 답습 가능) + 옵션 (vii) = 5/28 발화 가능성 (비권고) — `git revert HEAD` 권고 시작점 (C-υ-41 답습 — "즉시 rollback" = 사용자 결정 영역). **합의 형태 권고**: 본 brief 자체 = **(a) Reviewer-only 단축 합의 적격 시작점** (T-2 재발화 영역 한계 — Stage 4 entry brief + W-1 합의 시점 이미 답습) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 (T-6/T-10/T-13 미발화). **사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 영구 답습 (작성 시점 + 발효 후 자동 진입 영역 모두 0건)**. **합산 468 합의 조건 변경 0건** (17 합의 — W-1 합의 30 조건 + Stage 4 entry brief 49 조건 포함). **본 brief 자체 금지 ≥ 50 + 본 brief 발효 후 의무 금지 ≥ 13** enumerate. **본 brief 새 조건 후보 34 (C-χ-1 ~ C-χ-34)** — 합의 보고서 작성 시 정식 등록 (W-1 합의 29 답습 패턴 답습 + tool 특화 5 신규: C-χ-31 ~ C-χ-34 + LVE 12/12 PASS evidence 보존 의무). **본 brief 는 `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 시키지 않으며, behavior (regex / logic / mode / rc / dataclass schema) / dependency / entry point 어느 것도 *변경* 시키지 않으며, W-1 = 0-line passthrough 고정 어느 것도 *변경* 시키지 않으며, W-3 / W-4 어느 작업도 *진입* 시키지 않으며, Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 어느 것도 *변경* 시키지 않으며, 3 MVP-1 workflow 어느 줄도 *변경* 시키지 않으며 (W-1 답습 영구), 사용자 명시 5 금지 + 영구 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 468 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / W-2 변경 line / 수정 영역 어느 것도 *최종 확정 발효* / LVE 12/12 PASS evidence 자동 재집계 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점 — T-2 재발화 영역 한계)** / (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) / (C) brief 수정 / (D) 부분 채택 / (E) W-2 실 micro-patch 직접 진입 brief / (F) W-3/W-4 cycle 우선 / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.

---

**작성일**: 2026-05-18 후속 29
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §11 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **integration tool 실 변경 0건** (`tools/mvp1_pc3_ar1_integration_check.py` 298줄 변경 발효 — 별도 cycle)
- ❌ **CI workflow 변경 0건** (W-1 = 0-line passthrough 고정 답습 영구)
- ❌ **actual run 재실행 0건** (신규 trigger — W-4 영역 외)
- ❌ **W-3 / W-4 진입 0건** (cycle 3/4 / 4/4 분리)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ W-2 micro-patch 실 변경 자동 진입 0건 (본 brief = *가능성 검토* 한정)
- ❌ W-1 재진입 / W-1 = 0-line passthrough 고정 변경 0건
- ❌ tool behavior 변경 0건 (regex / logic / mode / rc / dataclass schema)
- ❌ tool dependency 추가 0건 (stdlib-only 영구 답습)
- ❌ tool entry point / CLI 인터페이스 변경 0건
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 468 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 / Stage 4 entry / W-1 합의 본문 변경 0건
- ❌ Layer A / B / C / D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ W-1 cycle 1/4 본문 변경 0건
- ❌ §5.5 9 sub-수단 / §5.5.1+§5.5.2 본문 채택 변경 0건
- ❌ Stage 4 step (line 318~360) 본문 변경 0건
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
- ❌ threshold *고정* 0건 (C-υ-18 답습)
- ❌ event enum 정식 등록 0건 (Backlog #5 분리)
- ❌ Rollback Trigger 28 자동 발화 0건 (옵션 (i)+(ii)+(v) 영역 = 0/28 영구 답습)
- ❌ 풀 3+1 트리거 자동 발화 0/16 (T-2 = Stage 4 entry brief + W-1 합의 시점 이미 발화 + 본 brief = 권위 답습 한정 → 새 발화 0건 → Reviewer-only 단축 합의 적격 시작점)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ `permissions: contents: read` 보강 0건 (W-5 영역)
- ❌ Required check / branch protection 등록 0건 (W-6 + W-8 영역)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ LVE 12/12 PASS evidence 자동 재집계 발효 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ W-2 변경 line / 수정 영역 *최종 확정 발효 0건* (사용자 명시 결정 영역)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ artifact 사후 변조 검증 도구 본문 작성 0건 (C-υ-46 후보 한정)
- ❌ GitHub Actions cache poisoning 검증 도구 본문 작성 0건 (C-υ-45 후보 한정)
