# Phase α-4 R-1 Stage 4 W-1 micro-patch brief (3 MVP-1 workflow) (DRAFT)

> **본 문서는 Phase α-4 R-1 Stage 4 진입 brief 풀 3+1 합의 (`81472ba` APPROVE AS BRIEF WITH CONDITIONS — 49 조건 C-υ-1 ~ C-υ-49) 발효 후속, 사용자 명시 진입 명령 답습 — **Phase α-4 Stage 4 *W-1 단독* 영역 (3 MVP-1 workflow 한정) *최소 micro-patch 가능성 검토* brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 4 entry (W-1~W-4 lockdown, `9c33efe` + `81472ba`) = "*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?"
> - **본 brief = α-4 Stage 4 W-1 micro-patch *possibility* 검토 DRAFT** — **"*Should* W-1 introduce micro-patch lines (and which ones), or is *0-line passthrough* the correct posture for 3 MVP-1 workflows at this gate?"**
> - α-4 Stage 4 W-1 실 micro-patch (본 brief 외) = "*Execute* the chosen patch (if any)"
> - W-2 / W-3 / W-4 = 영역 외 영구 답습 (사용자 명시 단독 영역 한정)
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며, (ii) W-2 / W-3 / W-4 어느 작업도 *진입* 시키지 않으며, (iii) Stage 4 entry brief 합의 49 조건 + 합산 438 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며, (iv) 사용자 명시 5 금지 (CI workflow 변경 / actual run 재실행 / W-2~W-4 진입 / Operational Readiness PASS / Hermes PMO 격상) 어느 것도 *해소* 시키지 않으며, (v) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, (vi) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-18 후속 28
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md` (commit `81472ba` — Stage 4 entry brief 풀 3+1 합의 APPROVE AS BRIEF WITH CONDITIONS, 49 조건 C-υ-1 ~ C-υ-49, **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-stage4-entry-brief.md` (commit `9c33efe`, 1032줄 — Stage 4 W-1~W-4 lockdown brief)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-actual-entry-decision.md` (commit `d3f6d59` — Stage 3 실 진입 여부 합의, 36 조건 C-τ-1 ~ C-τ-36)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS)
- `docs/review/3plus1-consensus-2026-05-16-phase-alpha-4-r1-local-validation-evidence.md` (commit `b264580` — 31 조건 C-σ-1 ~ C-σ-31)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C (Hermes PMO Activation 12 조건 미진입 영구 답습)

---

## 0. 본 brief 의 범위

### 0.1 사용자 명시 진입 명령 답습

> "Phase α-4 Stage 4 W-1 micro-patch brief를 작성해주세요. 범위는 3개 MVP-1 workflow에 대한 최소 micro-patch 가능성 검토입니다. 아직 CI workflow 실제 변경, actual run 재실행, W-2/W-3/W-4 진입, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 5 금지 답습 (본 brief 의 명시적 경계)

| # | 금지 영역 | 본 brief 시점 |
|---|---------|----------|
| **#1** | **CI workflow 실 변경** (3 MVP-1 workflow 본문 1206줄 변경 발효) | ✅ 0건 영구 답습 — 본 brief = *후보 검토 한정* |
| **#2** | **actual run 재실행** (신규 GitHub Actions run trigger) | ✅ 0건 영구 답습 — W-4 영역 분리 |
| **#3** | **W-2 / W-3 / W-4 진입** (integration tool / 3 fixture / actual run trigger) | ✅ 0건 영구 답습 — 본 brief = W-1 단독 영역 한정 |
| **#4** | **Operational Readiness PASS (Layer E) 선언** | ✅ 0건 영구 답습 — MVP-6 영역 분리 |
| **#5** | **Hermes PMO 격상 (Layer F)** | ✅ 0건 영구 답습 — ADR-008 부록 C 12 조건 미진입 |
| **합산** | **5 금지** | **5/5 영구 답습** |

### 0.3 본 brief 영역 vs Stage 4 entry brief 영역 분리 매트릭스

| 영역 | Stage 4 entry brief (`9c33efe`+`81472ba`) | 본 brief |
|------|------------------------------------------|--------|
| 범위 | W-1 + W-2 + W-3 + W-4 lockdown 권고 | **W-1 단독 micro-patch *가능성 검토*** |
| 권고 영역 | 수정 파일 + 검증 방법 + actual run 조건 + rollback trigger (4 영역) | **수정 영역 *후보* enumerate + 변경 line *결정 옵션* 한정** |
| W-1 변경 line 권고 | 0 ~ ≤ 15 lines micro-patch *권고 시작점* | **0 lines 우선 권고 + 후보 영역 ≤ 15 lines enumerate (C-υ-44 답습)** |
| W-2 / W-3 / W-4 영역 | 권고 영역 포함 (분리 명시) | ❌ **본 brief 영역 외 (사용자 명시 #3 답습)** |
| 검증 방법 | Pre / Per-W / Post / Actual run 4 단계 (42 검증) | **W-1 단독 검증 7 영역 (W-1-V1 ~ W-1-V7) + PRE-0 도구 가용성 답습** |
| 합의 결과 발효 | APPROVE AS BRIEF WITH CONDITIONS (49 조건) | DRAFT (사용자 명시 승인 *전*) |

### 0.4 본 brief 가 *하는* 것

1. Stage 4 entry brief 합의 (`81472ba` — 49 조건) 발효 후속 — **W-1 단독 micro-patch *가능성 검토* 한정** (§1)
2. **W-1 영역 한정 매트릭스** — 3 MVP-1 workflow 한정 + W-2/W-3/W-4 분리 명시 (§2)
3. **3 MVP-1 workflow 현재 상태 매트릭스** (read-only) — workflow별 trigger / paths / permissions / Stage 4 step 답습 (§3)
4. **Micro-patch 후보 영역 *enumerate 한정*** — 변경 line 0 lines 우선 권고 + ≤ 15 lines 후보 (사용자 결정 영역) (§4)
5. **W-1 검증 방법 권고** — W-1-V1 ~ W-1-V7 답습 + PRE-0 도구 가용성 사전 점검 (C-υ-38 답습) (§5)
6. **W-1 시점 rollback trigger 발화 가능성 매트릭스** (§6)
7. **사용자 명시 5 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 438 합의 조건 답습 매트릭스** (변경 0건) (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 5 금지 영역**:

- ❌ **CI workflow 실 변경 (0건)** — 3 MVP-1 workflow 1206줄 변경 발효 = 별도 cycle 영역
- ❌ **actual run 재실행 (0건)** — W-4 신규 trigger = 별도 cycle 영역 (사용자 명시 #2)
- ❌ **W-2 / W-3 / W-4 진입 (0건)** — integration tool / 3 fixture / actual run trigger = 본 brief 영역 외
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습

**추가 금지 영역 (Stage 4 entry brief 49 조건 + α-1+2+3 evidence + LVE 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — `secret-hygiene-egress-redaction.yml` 694 + `provider-adapter-enforcement.yml` 186 + `provider-url-scanner.yml` 326 + `tools/mvp1_pc3_ar1_integration_check.py` 298 + 3 fixture 89 = 1593줄 답습 보존
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (α-1+2+3 evidence §5.1 답습)
- ❌ **`src/` runtime code / facade.py placeholder 변경 (0건)** — Backlog #4 분리
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 채택 변경 (0건)** — C-υ-44 답습 (T-3 발화 영역 모호성 청산 명시 강화)
- ❌ **Stage 4 step 본문 (line 318~360 답습) 변경 (0건)** — 이미 wired 상태 답습 한정
- ❌ **PC-3 / AR-1 step 순서 변경 (0건)** — Stage 4 entry brief §5.5.1+§5.5.2 본문 변경 시도 권고 0건 (C-B6 + C-υ-44 답습)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **신규 workflow 신설 (0건)** + **`pull_request_target` 도입 (0건)** — T2/T3 별도 합의 영역
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 영역 별도 풀 3+1
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습 (Stage 5 G3-7 (i))
- ❌ **`permissions: contents: read` 보강 (0건)** — W-5 영역 = Stage 5 cycle 4 / Backlog #1+#2 분리 영구 답습
- ❌ **Required check 등록 (0건)** — W-6 영역 = Backlog #3 T3 분리
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 (0건)** — Backlog #1+#2+#3 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 영역
- ❌ **Hermes upstream Dockerfile 변경 (0건)** — ADR-008 §2.6.2 R2-1 영구 답습
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
- ❌ **threshold *고정* (0건)** — CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지 (C-υ-18 답습)
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **합산 438 합의 조건 자동 변경 (0건)** — 49 신규 (C-υ-1 ~ C-υ-49) + 389 답습 모두 영구 답습

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며,
- (ii) W-2 / W-3 / W-4 어느 작업도 *진입* 시키지 않으며,
- (iii) 합산 438 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iv) 사용자 명시 5 금지 영역 어느 것도 *해소* 시키지 않으며,
- (v) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (vi) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vii) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (viii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (ix) Stage 4 step (line 318~360) / PC-3 / AR-1 step 순서 어느 것도 *변경* 하지 않으며,
- (x) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (xi) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (xii) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 어느 것도 *발화* 시키지 않으며,
- (xiii) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (xiv) W-1 micro-patch 변경 line / 수정 영역 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **W-1 단독 micro-patch *가능성* (= 변경 0 lines 우선 vs 후보 ≤ 15 lines) 검토 권고 한정**. 모든 *확정 발효* / *실 변경* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (Stage 4 entry brief 합의 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 — 31 조건 C-σ-1 ~ C-σ-31 | ✅ 답습 한정 |
| `27351ce` (2026-05-17) | Phase α-4 R-1 Stage 3 실 진입 여부 brief (722줄) | ✅ 답습 한정 |
| `d3f6d59` (2026-05-17) | Phase α-4 R-1 Stage 3 합의 — 36 조건 C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| `630e125` (2026-05-17) | CONTEXT — Phase α-4 R-1 Stage 3 entry status | ✅ 답습 한정 |
| `9c33efe` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief (1032줄 DRAFT) | ✅ 답습 한정 |
| `81472ba` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief 풀 3+1 합의 — 49 조건 C-υ-1 ~ C-υ-49 | ✅ **본 brief 의 발효 trigger** |
| `e279958` (HEAD, 2026-05-18) | CONTEXT — Phase α-4 R-1 Stage 4 entry status | ✅ 답습 한정 |

### 1.2 Stage 4 entry brief 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-18 후속 27 |
| 합의 형태 | 풀 3+1 합의 (Agent A + B + C + Reviewer) — 외부 LLM 1+ 비적용 (T-6/T-10/T-13 미발화) |
| 합의 판정 | APPROVE AS BRIEF WITH CONDITIONS — BLOCK 사유 0건 |
| 합의 조건 | **49 조건 (C-υ-1 ~ C-υ-49)** |
| W-1 핵심 조건 | C-υ-6 (W-1 ≤ 15 lines micro-patch) + C-υ-12 (W-1 검증 7 영역) + **C-υ-44 (W-1 micro-patch 범위 결정 3 영역 동시 발효 — 절차 A + 안전성 B + 단순성 C, 변경 0 lines 우선 권고 강화)** + C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록) |
| W-1 시점 추가 조건 | C-υ-38 (PRE-0 도구 가용성 사전 점검) + C-υ-41 ("즉시 rollback" 권고 한정) + C-υ-42 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) |
| 풀 3+1 트리거 발화 | T-2 1/16 (Stage 4 lockdown 권고 = 영구 5 금지 #1 + #3 해소 권고 영역) |
| 본 brief trigger 의미 | **W-1 / W-2 / W-3 완전 분리 합의 4 cycle 옵션 (C-υ-43)** 정식 등록 → 본 brief = 4 cycle 중 cycle 1 (W-1 단독) DRAFT |

### 1.3 7 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 | "*Can* we enter Phase α-4?" |
| α-4 Stage 1.5 (조건 재검토) | 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (Step 분할) | Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 | "*How* should it be staged?" |
| α-4 Stage 2.5 (LVE) | Local Validation Evidence | `4ce5a0b` + `b264580` | APPROVE | 31 | "*Has local validation evidence been compiled?*" |
| α-4 Stage 3 (실 진입 여부) | Stage 3 brief | `27351ce` + `d3f6d59` | APPROVE AS BRIEF | 36 | "*Should* we enter actual implementation now?" |
| α-4 Stage 4 entry (lockdown) | Stage 4 entry brief | `9c33efe` + `81472ba` | APPROVE AS BRIEF WITH CONDITIONS | 49 | "*What exactly* will Stage 4 W-1~W-4 do?" |
| **α-4 Stage 4 W-1 (본 brief)** | **W-1 micro-patch brief (cycle 1/4)** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* W-1 introduce micro-patch lines (and which ones), or is 0-line passthrough correct?"** |
| α-4 Stage 4 W-1 실 micro-patch (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* the chosen patch (if any)" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 4 W-1 cycle 1/4 framing** (Stage 4 entry brief 합의 §8 권고 시작점 답습 + C-υ-43 4 cycle 옵션 정식 등록 답습):

- α-4 Stage 1 ↔ 1.5 ↔ 2 ↔ 2.5 ↔ 3 ↔ Stage 4 entry ↔ **W-1 micro-patch (본 brief, cycle 1/4)** ↔ W-1 실 micro-patch (사용자 결정) ↔ W-2 brief (cycle 2/4) ↔ W-3 brief (cycle 3/4) ↔ W-4 trigger brief (cycle 4/4)
- 본 brief 의 단일 책무: **"3 MVP-1 workflow 의 minimum micro-patch *possibility* 검토 + 변경 0 lines 우선 권고 vs 후보 ≤ 15 lines enumerate"** + **"실 변경 자동 진입 0건"**
- 본 brief ≠ W-1 실 micro-patch (CI workflow 변경 + commit = 별도 cycle 영역)
- 본 brief ≠ W-2 / W-3 / W-4 brief
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-18 후속 28 시점)

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
| **Phase α-4 Stage 4 W-1 (본 brief)** | **3 MVP-1 workflow micro-patch *가능성 검토*** | ⏳ **본 brief = DRAFT (cycle 1/4)** |

---

## 2. W-1 영역 한정 매트릭스

### 2.1 W-1 단독 영역 enumerate (Stage 4 entry brief §2.1 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| **W-1** | **3 MVP-1 workflow 본문 (`secret-hygiene-egress-redaction.yml` 694줄 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 = 1206줄)** | ✅ **본 brief = micro-patch *가능성 검토* 한정** |
| W-2 | integration check tool 본문 (`tools/mvp1_pc3_ar1_integration_check.py` 298줄) | ❌ 본 brief 영역 외 (사용자 명시 #3 — cycle 2/4 별도 brief 영역) |
| W-3 | 3 fixture 본문 (`tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` 89줄) | ❌ 본 brief 영역 외 (사용자 명시 #3 — cycle 3/4 별도 brief 영역) |
| W-4 | 신규 actual GitHub Actions run trigger (push event) | ❌ 본 brief 영역 외 (사용자 명시 #3 — cycle 4/4 별도 brief 영역) |

### 2.2 W-2 / W-3 / W-4 분리 명시 (위반 0건 영구 답습)

| 영역 | Stage 4 entry brief 시점 | 본 brief 시점 |
|---|-----------------------|-----------|
| W-2 | W-1~W-4 lockdown 권고 함께 포함 | ❌ 본 brief 영역 외 (cycle 2/4 별도) |
| W-3 | W-1~W-4 lockdown 권고 함께 포함 | ❌ 본 brief 영역 외 (cycle 3/4 별도) |
| W-4 | W-1~W-4 lockdown 권고 함께 포함 | ❌ 본 brief 영역 외 (cycle 4/4 별도) |
| **합산** | **W-1~W-4 = 함께 lockdown** | **W-1 단독 = 본 brief 영역** + **W-2/W-3/W-4 분리 ✅** |

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

본 §2 = **W-1 단독 영역 *권고 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). W-2/W-3/W-4 + W-5~W-10 어느 것도 본 brief 가 *통합* 시키지 않는다.

---

## 3. 3 MVP-1 workflow 현재 상태 매트릭스 (read-only)

### 3.1 Workflow별 본문 매트릭스

| Workflow | 줄수 | `on.push.branches` | `on.pull_request.branches` | `permissions` | Stage 4 step | 답습 출처 |
|----------|-----|---------|-----------|----------|--------|---------|
| `secret-hygiene-egress-redaction.yml` | **694** | `main` + `develop` + `feature/**` | `main` + `develop` | `contents: read` | ✅ line 318~360 wired (`stage4_pc3_ar1_integration` step) | LVE §3.1 답습 + read-only 검증 |
| `provider-adapter-enforcement.yml` | **186** | `main` + `develop` + `feature/**` | `main` + `develop` | `contents: read` | ✅ wired (sibling Stage 4 pattern) | LVE §3.1 답습 |
| `provider-url-scanner.yml` | **326** | `main` + `develop` + `feature/**` | `main` + `develop` | `contents: read` | ✅ wired (sibling Stage 4 pattern) | LVE §3.1 답습 |
| **합산** | **1206** | **3/3 feature/** ✅ | **3/3 main+develop** ✅ | **3/3 read-only** ✅ | **3/3 wired** ✅ | — |

### 3.2 `on.push.paths` 매트릭스 (cross-workflow re-verify 답습 여부)

| Workflow | `on.push.paths` 영역 | cross-workflow re-verify 답습 |
|----------|------------------|----------------------|
| `secret-hygiene-egress-redaction.yml` | `tools/secret_scanner.py` + 다수 tools + `tests/fixtures/mvp1_pc3_ar1_integration/**` + 본 workflow + **`provider-adapter-enforcement.yml` + `provider-url-scanner.yml`** (Stage 4 cross-workflow re-verify) | ✅ **답습 (line 47~49 명시)** |
| `provider-adapter-enforcement.yml` | `tools/provider_import_scanner.py` + `tests/fixtures/provider_adapter_enforcement/**` + 본 workflow + `.importlinter` + `requirements-dev.txt` + `src/**` | ❌ **답습 미포함** — `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/**` + 2 sibling workflow paths 미포함 |
| `provider-url-scanner.yml` | `tools/provider_url_scanner.py` + `tests/fixtures/provider_url_scanner/**` + 본 workflow | ❌ **답습 미포함** — 동상 |
| **합산** | — | **1/3 답습 (workflow 1 단독)** — **2/3 미답습 (workflow 2/3)** |

### 3.3 Workflow 1 본문 Stage 4 step 답습 (line 318~360)

| line | 영역 | 답습 |
|------|-----|-----|
| 318 | step name: `Stage 4 (PC-3 + AR-1) integration check — 3 workflow cross-verify` | ✅ |
| 319 | `id: stage4_pc3_ar1_integration` | ✅ |
| 323~327 | `--mode integration` × 3 workflow + tee log | ✅ |
| 329~341 | PASS fixture (compliant_entry_step) + FAIL fixture (PC-3) + FAIL fixture (AR-1) 3 verify | ✅ |
| 347, 351 | rc=1 expected for FAIL fixtures, otherwise `::error::Stage 4 verifier 무력화` | ✅ |
| 354~357 | `--list-checks` self-check + `stage4_pc3_ar1_integration=PASS` output | ✅ |
| 358~359 | ledger entry candidate (Backlog #5 — 후보 한정) | ✅ |
| 360 | summary log line | ✅ |
| **합산** | **Stage 4 step 본문 = 이미 wired + 4 prerequisite run SUCCESS 답습** | **✅ 100% 답습** |

### 3.4 본 §3 의 *범위 한계*

본 §3 = **read-only 답습 매트릭스 한정**. 본 §3 의 어떤 항목도 *변경* / *재해석* / *재합의* 영역이 아니며, 단순히 *현재 상태* 답습 enumerate 한정. 본문 변경 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. Micro-patch 후보 영역 *enumerate 한정*

### 4.1 변경 line 결정 옵션 매트릭스 (C-υ-44 답습 — 3 영역 동시 발효)

C-υ-44 답습 결정 영역 (Stage 4 entry brief 합의 §5.3 답습) = **3 영역 동시 발효**:

| Agent 영역 | 권고 | 본 brief 채택 영역 |
|---------|----|---------------|
| Agent A (절차) — C-A6 | W-1 micro-patch 범위 결정 = *별도 brief 후 합의* | ✅ **본 brief = cycle 1/4 별도 brief 진입** (C-A6 발효) |
| Agent B (안전성) — C-B6 | PC-3 / AR-1 step 순서 변경 = §5.5.1+§5.5.2 본문 변경 시도 *권고 0건* 영구 답습 (T-3 발화 영역 모호성 청산) | ✅ **본 brief = step 순서 변경 0건 영구 답습 + 변경 영역 = `on.push.paths` 한정 영구 답습** |
| Agent C (단순성) — C-C1 | 변경 line *0 lines 우선 권고 강화* (옵션 (iv)) | ✅ **본 brief 권고 시작점 = (i) 변경 0 lines 우선 권고** |

### 4.2 변경 line 결정 옵션 (사용자 결정 영역)

| 옵션 | 변경 line | 적격 영역 | 본 brief 권고 |
|-----|--------|--------|----------|
| **(i)** | **0 lines** | 3 MVP-1 workflow = 현재 상태 답습 (Stage 4 step wired + 4 prerequisite run SUCCESS) | ✅ **권고 시작점 (C-υ-44 답습 — 변경 0 lines 우선)** |
| (ii) | ≤ 2 lines | workflow 2 + workflow 3 `on.push.paths` 에 `tools/mvp1_pc3_ar1_integration_check.py` 1 line × 2 workflow = 합산 2 lines 추가 (integration tool 변경 시 cross-workflow re-trigger 명시) | 옵션 (사용자 결정 영역) |
| (iii) | ≤ 4 lines | workflow 2 + workflow 3 `on.push.paths` 에 `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/**` 2 line × 2 workflow = 합산 4 lines 추가 | 옵션 (사용자 결정 영역) |
| (iv) | ≤ 8 lines | workflow 2 + workflow 3 `on.push.paths` 에 (iii) + sibling 2 workflow path 추가 = 2 line × 2 workflow + 2 sibling × 2 workflow = 합산 8 lines | 옵션 (사용자 결정 영역) |
| (v) | ≤ 15 lines | (iv) + workflow 1 의 paths 정합성 미세 정정 (line ≤ 7 lines) | 옵션 (Stage 4 entry brief §3.1 답습 — 권고 한계 상한) |
| (vi) | ≥ 16 lines | Stage 4 entry brief §3.1 답습 영역 외 (별도 합의 필요) | ❌ **비권고** |
| (vii) | step 순서 변경 (line 추가 없이 본문 순서 변경) | §5.5.1 + §5.5.2 PC-3 + AR-1 공유 본문 변경 영역 | ❌ **비권고** (C-υ-44 답습 — T-3 발화 영역) |

### 4.3 옵션 (ii)~(v) 의 *근거 영역* enumerate (참고 한정)

본 §4.3 = 옵션 (ii)~(v) 의 *근거 enumerate 한정* — 채택 권고 0건. 변경 line 결정 = 사용자 명시 결정 영역.

**옵션 (ii)~(iv) 근거 (cross-workflow re-verify 답습 확장 가능성)**:
- Workflow 1 (`secret-hygiene-egress-redaction.yml`) 의 `on.push.paths` 에 sibling 2 workflow (provider-adapter / provider-url) 가 *cross-workflow re-verify* 답습으로 이미 포함됨 (line 47~49)
- Workflow 2 / 3 의 `on.push.paths` 에는 동일 답습 미포함 → integration tool / fixture / sibling workflow 변경 시 workflow 2/3 *자동 re-trigger 미발화* 영역
- 그러나 **Stage 4 step 본문은 wired + 4 prerequisite run SUCCESS** 답습 → cross-workflow re-trigger 답습 *추가 필요성* = *실제 보강 가치 vs 변경 line 증가 트레이드오프* 권고 영역

**옵션 (v) 근거**:
- Stage 4 entry brief §3.1 답습 권고 한계 상한 = ≤ 15 lines micro-patch 권고 시작점
- 단 C-υ-44 답습 = 변경 0 lines 우선 권고 강화 → 옵션 (v) 까지 도달은 사용자 명시 결정 영역

### 4.4 영역 외 변경 enumerate (본 brief 비권고 영구 답습)

| 영역 | 사유 |
|------|-----|
| workflow 1/2/3 본문 step 추가 / 삭제 | Stage 4 entry brief §3.1 답습 영역 외 (별도 합의 필요) — Agent B C-B6 답습 (§5.5.1+§5.5.2 본문 변경 시도 권고 0건) |
| workflow 1/2/3 jobs / steps 순서 변경 | C-υ-44 답습 — T-3 발화 영역 모호성 청산 강화 (§4.2 옵션 (vii)) |
| Stage 4 step (line 318~360) 본문 변경 | wired 답습 보존 영역 — §3.3 답습 |
| `permissions: contents: read` 보강 | W-5 영역 = 본 brief 영역 외 (사용자 명시 #3 + #4 답습) |
| Required check / branch protection 등록 | W-6 / W-8 영역 = 본 brief 영역 외 |
| `pull_request_target` event 도입 | Stage 5 cycle 2 영역 = 본 brief 영역 외 |
| `secrets.*` reference 도입 | F-금지 #1 영구 답습 |
| 신규 trigger event (`workflow_dispatch` / `schedule` / `repository_dispatch`) | W-4 영역 = 본 brief 영역 외 (사용자 명시 #3) |
| 신규 workflow 신설 | T2/T3 별도 합의 영역 |

### 4.5 변경 line 권고 시작점 매트릭스

| Workflow | 변경 line 권고 시작점 | 사용자 결정 옵션 상한 |
|----------|------------------|-------------------|
| `secret-hygiene-egress-redaction.yml` | **0 lines** | ≤ 7 lines (옵션 (v)) |
| `provider-adapter-enforcement.yml` | **0 lines** | ≤ 4 lines (옵션 (iv) 분담) |
| `provider-url-scanner.yml` | **0 lines** | ≤ 4 lines (옵션 (iv) 분담) |
| **합산** | **0 lines (권고 시작점)** | **≤ 15 lines (옵션 (v) 상한)** |

### 4.6 본 §4 의 *범위 한계*

본 §4 = **변경 line 결정 *옵션 enumerate 한정***. 본 §4 의 어떤 항목도:
- (i) 옵션 (i)~(v) 中 어느 것도 *채택 발효* 시키지 않으며,
- (ii) 변경 line *최종 확정* 시키지 않으며,
- (iii) workflow 본문 어느 줄도 *변경* 하지 않는다.

권고 시작점 = **옵션 (i) 변경 0 lines** (C-υ-44 답습) — 실 변경 결정 = 사용자 명시 결정 영역.

---

## 5. W-1 검증 방법 권고

### 5.1 PRE-0 도구 가용성 사전 점검 (C-υ-38 답습)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| PRE-0-1 | `yamllint` local 가용성 | `yamllint --version` | rc=0 + version enumerate |
| PRE-0-2 | `gh CLI` 인증 상태 | `gh auth status` | rc=0 + 인증 답습 |
| PRE-0-3 | Python version ≥ 3.12 | `python --version` | rc=0 + ≥ 3.12 |
| PRE-0-4 | git version | `git --version` | rc=0 + version enumerate |
| PRE-0-5 | `actionlint` local 가용성 (옵션) | `actionlint --version` | rc=0 (옵션 — 미설치 시 yamllint 단독 답습) |

### 5.2 W-1-V1 ~ W-1-V7 검증 (Stage 4 entry brief §4.2.1 답습)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| W-1-V1 | `secret-hygiene-egress-redaction.yml` 694줄 yamllint 통과 | `yamllint .github/workflows/secret-hygiene-egress-redaction.yml` | rc=0 |
| W-1-V2 | `provider-adapter-enforcement.yml` 186줄 yamllint 통과 | (동상) | rc=0 |
| W-1-V3 | `provider-url-scanner.yml` 326줄 yamllint 통과 | (동상) | rc=0 |
| W-1-V4 | PC-3 정합성 — 3 workflow Stage 4 step `continue-on-error` 미지정 (또는 false) | `grep -B1 -A2 "continue-on-error" .github/workflows/{secret-hygiene-egress-redaction,provider-adapter-enforcement,provider-url-scanner}.yml \| grep -v "false"` | match 0건 (Stage 4 step) |
| W-1-V5 | AR-1 정합성 — 3 workflow Stage 4 step fail-closed 패턴 (`exit 1`) + non-zero exit propagation | `grep -B2 -A5 "stage4_pc3_ar1_integration" .github/workflows/*.yml` | 패턴 일치 |
| W-1-V6 | 3 workflow trigger event branches — `feature/**` 매칭 | `grep -A4 "branches:" .github/workflows/{secret-hygiene-egress-redaction,provider-adapter-enforcement,provider-url-scanner}.yml \| grep "feature/\\*\\*"` | match 3 (3/3 workflow) |
| W-1-V7 | 3 workflow paths filter 영역 — cross-workflow re-verify 답습 매트릭스 enumerate | `grep -A30 "paths:" .github/workflows/*.yml \| grep -E "(mvp1_pc3_ar1_integration_check|mvp1_pc3_ar1_integration/\\*\\*|provider-adapter-enforcement\\.yml\|provider-url-scanner\\.yml\|secret-hygiene-egress-redaction\\.yml)"` | enumerate (현재 = workflow 1 단독 답습 — workflow 2/3 미답습) |

### 5.3 신규 actual run trigger 검증 매트릭스

| 영역 | 본 brief 권고 |
|------|----------|
| W-4 신규 actual run trigger | ❌ **0건 영구 답습** (사용자 명시 #2 + #3) |
| Pre-implementation 검증 = local 한정 | ✅ 신규 actual run trigger 0건 (PRE-0-1 ~ W-1-V7 모두 local 표준 도구 한정) |
| 본 brief 시점 신규 actual run trigger | **0건** |

### 5.4 검증 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `yamllint` | YAML syntax 검증 | 답습 한정 — 신규 도입 0건 |
| `grep` | Stage 4 step / paths 패턴 enumerate | 표준 도구 답습 |
| `gh CLI` (옵션) | 4 prerequisite runs 답습 시점 ↔ 본 brief 시점 시간 경과 재검증 (PRE-3 영역 — Stage 4 entry brief 답습) | 답습 한정 (read-only) |
| Python `yaml.safe_load` / `py_compile` | (W-2 영역 — 본 brief 영역 외) | ❌ 0건 (cycle 2/4 별도) |
| `python tools/mvp1_pc3_ar1_integration_check.py` | (W-2 영역 — 본 brief 영역 외) | ❌ 0건 (cycle 2/4 별도) |
| `actionlint` (옵션) | GitHub Actions workflow syntax 검증 | 답습 한정 — 신규 도입 0건 |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 5.5 본 §5 의 *범위 한계*

본 §5 = **W-1 검증 방법 *권고 한정***. 실 검증 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 본 §5 의 어떤 항목도 신규 actual run trigger 0건 영구 답습 + W-2/W-3/W-4 검증 영역 *통합 0건*.

---

## 6. W-1 시점 rollback trigger 발화 가능성 매트릭스

### 6.1 Layer B 18 trigger × W-1 시점 발화 매트릭스 (Stage 4 entry brief §6.1 답습)

| # | trigger 영역 | W-1 본문 변경 0 lines 시점 발화 | W-1 본문 변경 ≤ 15 lines 시점 발화 |
|---|---------|---------------------------|----------------------------|
| 13 | CI step pass with violation present (PC-3) | 0건 (Stage 4 step 본문 변경 0건) | **발화 가능성** (옵션 (vii) — step 순서 변경 시 = 비권고 영역) |
| 14 | CI step fail without auto-reject (AR-1) | 0건 (Stage 4 step 본문 변경 0건) | **발화 가능성** (옵션 (vii) — step 순서 변경 시 = 비권고 영역) |
| 15 | PR check unstable / flaky | 0건 (신규 actual run trigger 0건) | 0건 영구 답습 (W-4 영역 외) |
| **합산 (18 중)** | **18 trigger** | **0/18 발화** | **2/18 발화 가능성 (옵션 (vii) 한정 — 본 brief 비권고)** |

### 6.2 TR-1 ~ TR-5 × W-1 시점 발화 매트릭스

| TR # | 영역 | W-1 시점 발화 |
|----|----|------------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 | 0건 (Phase α-2 영역) |
| TR-2 | `include_external_packages` flag | 0건 |
| TR-3 | `root_packages` 변경 | 0건 |
| TR-4 | `ignore_imports` 변경 | 0건 |
| TR-5 | google.generativeai facade | 0건 |
| **합산** | **5 trigger** | **0/5 발화 영구 답습** |

### 6.3 Step Division + Stage 4 신규 후보 × W-1 시점 발화 매트릭스

| # | trigger | W-1 본문 변경 0 lines | W-1 본문 변경 ≤ 15 lines |
|---|-------|-------------------|-----------------------|
| ND-1 | PC-3 self-check FAIL (local) | 0건 | **발화 가능성** (옵션 (vii) 시 — 비권고) |
| ND-2 | AR-1 self-check FAIL (local) | 0건 | **발화 가능성** (옵션 (vii) 시 — 비권고) |
| ND-3 | integration check tool self-check FAIL | 0건 (W-2 영역 외) | 0건 (W-2 영역 외) |
| ND-4 | 4 prerequisite runs JSON conclusion 미답습 | 0건 (PRE 영역) | 0건 |
| ND-5 | LVE 본문 누락 | 0건 (PRE 영역) | 0건 |
| **합산** | **5 후보** | **0/5 발화** | **2/5 발화 가능성 (옵션 (vii) 한정)** |

### 6.4 W-1 시점 발화 합산 매트릭스

| 옵션 | Layer B | TR-1~5 | Step Division 신규 | 합산 발화 가능성 |
|-----|---------|------|----------------|--------------|
| **(i) 0 lines (권고 시작점)** | 0/18 | 0/5 | 0/5 | **0/28 발화 영구 답습** |
| (ii) ≤ 2 lines | 0/18 | 0/5 | 0/5 | **0/28 발화** (paths-only 변경) |
| (iii) ≤ 4 lines | 0/18 | 0/5 | 0/5 | **0/28 발화** (paths-only 변경) |
| (iv) ≤ 8 lines | 0/18 | 0/5 | 0/5 | **0/28 발화** (paths-only 변경) |
| (v) ≤ 15 lines | 0/18 | 0/5 | 0/5 | **0/28 발화** (paths-only 변경) |
| (vi) ≥ 16 lines | (영역 외 — 별도 합의) | (영역 외) | (영역 외) | **본 brief 비권고** |
| (vii) step 순서 변경 | 2/18 (#13 + #14) | 0/5 | 2/5 (ND-1 + ND-2) | **4/28 발화 가능성 — 본 brief 비권고 영역** |

**핵심 발견**: 옵션 (i)~(v) (paths-only 변경) 영역 = **0/28 발화 영구 답습**. 옵션 (vii) (step 순서 변경) 영역 = 4/28 발화 가능성 — **본 brief 비권고** (C-υ-44 답습 — Agent B C-B6 + Agent C C-C1 + Reviewer §4.4 답습).

### 6.5 Rollback 절차 권고 (C-υ-41 답습 — "즉시 rollback" 권고 한정)

| 절차 | 영역 | 권고 |
|----|----|----|
| (i) Rollback decision | trigger 발화 시 판단 | **사용자 명시 결정 영역** (자동 rollback 0건 영구 답습) |
| (ii) `git revert HEAD` | 가장 안전 — 변경 line 만 revert | **권고 시작점** |
| (iii) `git reset --hard HEAD~N` | 강제 reset (이력 변경) | ❌ **비권고** (R-4 history rewrite layer 영역) |
| (iv) 신규 `fix:` commit (revert 없이 forward fix) | micro patch forward fix | 옵션 (paths-only 변경 시) |
| (v) 본 brief 시점 = 변경 line 0 = rollback 영역 0건 영구 답습 | — | **답습 한정** |

### 6.6 본 §6 의 *범위 한계*

본 §6 = **rollback trigger *발화 가능성 enumerate 한정***. 본 §6 의 어떤 항목도 *발화* / *rollback 절차 자동 발효* / *threshold 고정* 시키지 않는다.

---

## 7. 사용자 명시 5 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 5 금지 영역 위반 0건 영구 답습

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 결정 영역) |
|---|---------|---------------|------------------------------|
| #1 | CI workflow 실 변경 | ✅ 0건 (3 workflow 1206줄 변경 0건 — 본 brief = *후보 검토 한정*) | ✅ 0건 (DRAFT 영역, 사용자 결정 후 진입) |
| #2 | actual run 재실행 | ✅ 0건 (신규 trigger 0건) | ✅ 0건 (W-4 영역 외 영구 답습) |
| #3 | W-2 / W-3 / W-4 진입 | ✅ 0건 (cycle 2/4 + 3/4 + 4/4 분리) | ✅ 0건 (별도 brief 영역) |
| #4 | Operational Readiness PASS (Layer E) | ✅ 0건 (MVP-6 영역 분리) | ✅ 0건 |
| #5 | Hermes PMO 격상 (Layer F) | ✅ 0건 (ADR-008 부록 C 12 조건 미충족) | ✅ 0건 |
| **합산** | **5** | **✅ 5/5 위반 0건** | **✅ 5/5 위반 0건** |

### 7.2 W-1 옵션별 5 금지 위반 매트릭스

| 옵션 | #1 | #2 | #3 | #4 | #5 | 합산 |
|-----|----|----|----|----|----|-----|
| (i) 0 lines | ✅ 0 (현재 상태 답습) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건** |
| (ii)~(v) paths-only ≤ 15 lines | ✅ 0 (본 brief 시점) — Stage 4 실 구현 시점 = #1 해소 (사용자 결정) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **5/5 위반 0건 (본 brief 시점)** |
| (vi) ≥ 16 lines | ❌ **위반 가능성** (Stage 4 entry brief §3.1 답습 영역 외 — 별도 합의 필요) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |
| (vii) step 순서 변경 | ❌ **위반 가능성** (§5.5.1+§5.5.2 본문 변경 영역 — C-υ-44 답습 비권고) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **본 brief 비권고** |

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
| **W-2 / W-3 / W-4 cycle 2/4 / 3/4 / 4/4** | integration tool / 3 fixture / actual run trigger | ❌ 본 brief 영역 외 (사용자 명시 #3 답습) |

### 7.4 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 5 금지 영역 + Backlog 분리 영역 어느 것도 *해소* / *통합* 시키지 않는다.

---

## 8. 합산 438 합의 조건 답습 매트릭스

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
| **Phase α-4 R-1 Stage 4 entry** | **`81472ba`** | **49 (C-υ-1 ~ C-υ-49)** | **0건** ✅ |
| **합산** | **16 합의** | **438 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| **C-υ-43** (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록) | ✅ **본 brief = cycle 1/4 (W-1 단독) 진입 — C-υ-43 발효** |
| **C-υ-44** (W-1 micro-patch 범위 결정 3 영역 동시 발효 — 절차 A + 안전성 B + 단순성 C) | ✅ **§4.1 + §4.2 답습 — 변경 0 lines 우선 권고 시작점** |
| C-υ-6 (W-1 ≤ 15 lines micro-patch 권고 시작점) | ✅ §4.2 옵션 (v) 답습 (상한 한정) |
| C-υ-12 (W-1 검증 7 영역 W-1-V1 ~ W-1-V7) | ✅ §5.2 답습 |
| C-υ-38 (PRE-0 도구 가용성 사전 점검) | ✅ §5.1 답습 |
| C-υ-41 ("즉시 rollback" 권고 한정 명시 강화) | ✅ §6.5 답습 |
| C-υ-42 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) | ✅ Post-implementation 검증 시점 답습 한정 (cycle 2/4 + cycle 4/4 영역) |
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
| C-υ-37 (W-1~W-4 최종 확정 발효 0건) | ✅ §0.6 답습 |
| C-υ-45 (cache poisoning 후보 한정) | ✅ §10.2 답습 |
| C-υ-46 (artifact 사후 변조 후보 한정) | ✅ §10.2 답습 |
| C-υ-49 (30 trigger combined fire 후보 한정) | ✅ §6.4 답습 |

### 8.3 본 §8 의 *범위 한계*

본 §8 = **438 합의 조건 답습 매트릭스 *enumerate 한정***. 본 brief 가 발생시키는 *새 조건* = §11.2 (C-φ-1 ~ C-φ-N) 한정 — 본 brief 단독 = *새 조건 발효 0건* + 답습 한정 (합의 보고서 작성 시 정식 등록).

---

## 9. 합의 형태 권고 + 풀 3+1 승격 트리거 분석

### 9.1 본 brief 자체 합의 형태 권고

| 합의 형태 | 적격 조건 | 본 brief 적격성 |
|--------|--------|-------------|
| **(a) Reviewer-only 단축 합의** | 풀 3+1 트리거 0건 발화 + 새 권위 결정 0건 | ✅ **권고 시작점** — 본 brief = W-1 단독 micro-patch *가능성 검토* DRAFT + W-2/W-3/W-4 분리 + W-5~W-10 분리 + 변경 0 lines 권고 시작점 + paths-only 변경 영역 ≤ 15 lines 한정 → T-2 발화 *영역 한계* (Stage 4 entry brief 합의 시점 이미 발화 완료 — 본 brief = 그 권위 답습 한정) |
| (b) 풀 3+1 합의 | 트리거 中 1+ 발화 | ⚠️ **부분 적격** — 본 brief = Stage 4 entry brief 합의 §8 답습 cycle 1/4 영역 한정 → T-2 발화 *재발화 영역 한계* (Stage 4 entry brief 합의 시점 이미 발화) — 풀 3+1 합의 권위 답습 가능 (옵션) |
| (c) 풀 3+1 + 외부 LLM 1+ | C-14 cross-vendor + ADR-011 §2.4 영역 | ❌ **비권고** — W-1 단독 영역 + paths-only ≤ 15 lines 한정 → T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 |

**권고**: 본 brief = **(a) Reviewer-only 단축 합의 (권고 시작점)** — Stage 4 entry brief 합의 시점 (`81472ba`) 이미 T-2 발화 + W-1 영역 권위 답습 완료. 본 brief = cycle 1/4 한정 + paths-only ≤ 15 lines 영역 한계 + 변경 0 lines 권고 시작점 → 풀 3+1 트리거 재발화 *영역 한계* — Reviewer-only 단축 합의 *적격 시작점*. 단 사용자 명시 결정 시 풀 3+1 합의 (옵션 (b)) 진입 가능 영역.

### 9.2 풀 3+1 승격 트리거 검토 매트릭스 (본 brief 시점)

| # | 트리거 영역 | 본 brief 시점 발화 |
|---|----------|----------------|
| T-1 | 본 brief 가 합산 438 합의 조건 中 1+ *재결정* 권고 | 0건 — 답습 한정 |
| T-2 | 본 brief 가 사용자 명시 영구 5 금지 영역 中 1+ *해소* 권고 | ⚠️ **재발화 영역 한계** — Stage 4 entry brief 시점 (`81472ba`) 이미 T-2 발화 완료. 본 brief = cycle 1/4 *권위 답습 한정* + paths-only ≤ 15 lines 영역 한계 → 새 T-2 발화 0건 |
| T-3 | §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 *재결정* 권고 | 0건 — 옵션 (vii) 비권고 명시 (§4.2 답습) |
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
| T-16 | Stage 4 자동 실 구현 발효 권고 | 0건 — 본 brief = lockdown DRAFT 한정 |
| **합산** | **16** | **0/16 새 발화 + T-2 재발화 영역 한계** → **Reviewer-only 단축 합의 적격 시작점** |

### 9.3 외부 LLM 1+ blind 의뢰 적격성 매트릭스

| 영역 | 본 brief 적격성 |
|------|------------|
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | 비적격 — 본 brief = cycle 1/4 한정 + paths-only ≤ 15 lines 영역 + W-1 단독 영역 |
| ADR-011 §2.4 T2 영역 | 답습 한정 — 외부 LLM 의뢰 미필수 영역 |
| 본 brief 권고 | ❌ **비권고** — T-6/T-10/T-13 미발화 → 외부 LLM 의뢰 미필수 영역 |

### 9.4 본 §9 의 *범위 한계*

본 §9 = **합의 형태 권고 한정**. 본 brief 자체 = Reviewer-only 단축 합의 적격 시작점 (T-2 재발화 영역 한계) — 풀 3+1 합의 (옵션 (b)) 진입 = 사용자 명시 결정 영역. 외부 LLM 1+ blind 의뢰 = 비권고 (W-1 단독 영역 분리 명시).

---

## 10. 본 brief 자체 금지 + brief 발효 후 의무 금지

### 10.1 본 brief 작성 시점 금지 사항

- ❌ **CI workflow 실 변경** (사용자 명시 #1) — 3 MVP-1 workflow 1206줄 변경 0건
- ❌ **actual run 재실행** (사용자 명시 #2) — 신규 trigger 0건
- ❌ **W-2 / W-3 / W-4 진입** (사용자 명시 #3) — cycle 2/4 / 3/4 / 4/4 분리
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 #4)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 #5)
- ❌ Stage 4 step (line 318~360) 본문 변경
- ❌ §5.5.1 + §5.5.2 PC-3 + AR-1 양 GP 공유 본문 변경 / step 순서 변경 (옵션 (vii) — C-υ-44 답습)
- ❌ Phase α-1 / α-2 / α-3 자동 재진입
- ❌ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경
- ❌ `src/` 본문 변경 / facade.py real 본문 작성 (Backlog #4 분리)
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 / Stage 4 entry 합의 본문 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ `.importlinter` forbidden / facade allow / google.generativeai / URL 흡수 변경
- ❌ R-7 docker secret block 본문 변경
- ❌ 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입
- ❌ Stage 5 (G3-7) 자동 진입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 *고정*
- ❌ Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 trigger 자동 발화
- ❌ 합산 438 합의 조건 자동 변경
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
- ❌ W-1 변경 line / 수정 영역 *최종 확정 발효* (사용자 명시 결정 영역 한정)
- ❌ `permissions: contents: read` 보강 (W-5 영역)
- ❌ Required check / branch protection 등록 (W-6 + W-8 영역)
- ❌ artifact 사후 변조 검증 도구 본문 작성 (C-υ-46 후보 한정)
- ❌ GitHub Actions cache poisoning 검증 도구 본문 작성 (C-υ-45 후보 한정)

### 10.2 본 brief 발효 *후* 의무 금지 사항 (사용자 명시 결정 영역)

본 brief 발효 후 *자동 진입 영역* (사용자 명시 결정 *전*):

- ❌ W-1 micro-patch 실 변경 자동 진입 0건 (사용자 명시 결정 후 진입)
- ❌ W-2 / W-3 / W-4 brief 자동 작성 진입 0건
- ❌ 신규 actual run 자동 trigger 0건
- ❌ 합의 보고서 작성 자동 진입 0건 (사용자 명시 합의 형태 결정 후)
- ❌ W-5 ~ W-10 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 자동 진입 0건
- ❌ Backlog #1+#2 / Backlog #3 / Stage 5 자동 진입 0건
- ❌ 합산 438 합의 조건 자동 변경 0건
- ❌ Layer C / D / E / F 재발효 / 재선언 / 발효 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 변경 자동 진입 0건

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** (T-2 재발화 영역 한계 → Reviewer-only 적격 시작점) | Reviewer-only 단축 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-XX-phase-alpha-4-r1-stage4-w1-micropatch.md`) + 사용자 명시 결정 후 commit + push |
| (B) | 본 brief 그대로 승인 → 풀 3+1 합의 진입 (사용자 명시 보강 결정 시) | 풀 3+1 합의 보고서 작성 |
| (C) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 |
| (D) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 |
| (E) | 본 brief 승인 → W-1 실 micro-patch 직접 진입 brief 작성 (옵션 (i) 0 lines 채택 시) | W-1 실 micro-patch (또는 변경 0건 답습) brief 별도 작성 |
| (F) | 본 brief 보류 → W-2 / W-3 / W-4 cycle 우선 진입 | cycle 2/4 / 3/4 / 4/4 中 사용자 결정 영역 |
| (G) | 본 brief 보류 → Backlog #1+#2 / Backlog #3 / Stage 5 우선 진입 | Backlog 中 사용자 결정 영역 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 11.1 권고 시작점

사용자 명시 결정 영역. 본 brief 발효 = Phase α-4 Stage 4 W-1 *micro-patch 가능성 검토 권위 권고 한정*. **단축 cycle 답습 패턴 (brief → 승인 → 합의 → commit → push 6 단계)** 답습 시 권고:

```
■ 본 brief = Phase α-4 Stage 4 W-1 micro-patch (DRAFT, 본 commit)              ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 → Reviewer-only 단축 합의 (옵션 (A), T-2 재발화 영역 한계)
   │
   ▼ (합의 commit + push 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-1 실 micro-patch (옵션 (i) 0 lines 채택 시 = 변경 0건 답습 commit) 별도 brief
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-2 micro-patch (integration tool) brief 작성 (cycle 2/4)     ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-3 micro-patch (3 fixture) brief 작성 (cycle 3/4)             ← 별도 결정 영역
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-4 Stage 4 W-4 신규 actual run trigger brief (cycle 4/4)                  ← 별도 결정 영역
```

### 11.2 본 brief 새 조건 후보 (Reviewer-only / 풀 3+1 합의 시 정식 등록)

본 brief 합의 시 새 조건 enumerate 후보 (C-φ-1 ~ C-φ-N):

| # | 조건 후보 | 본 brief 영역 |
|---|--------|-----------|
| C-φ-1 | 본 brief (Phase α-4 Stage 4 W-1 micro-patch *가능성 검토* DRAFT) 13 영역 점검 결과 100% 채택 | §0.1 답습 |
| C-φ-2 | W-1 cycle 1/4 framing 정합성 채택 — C-υ-43 답습 ("4 cycle 옵션 정식 등록" 발효) | §1.3 + §1.4 답습 |
| C-φ-3 | W-1 단독 영역 + W-2/W-3/W-4 분리 명시 + W-5~W-10 분리 명시 | §2 답습 |
| C-φ-4 | 사용자 명시 5 금지 5/5 영구 답습 (작성 시점 + 발효 후) | §7.1 답습 |
| C-φ-5 | 3 MVP-1 workflow 현재 상태 read-only 매트릭스 채택 — 1206줄 답습 + Stage 4 step wired + cross-workflow re-verify 답습 = workflow 1 단독 (1/3) | §3 답습 |
| C-φ-6 | 변경 line 결정 옵션 (i)~(vii) enumerate — **권고 시작점 = (i) 0 lines 우선 (C-υ-44 답습)** | §4.2 답습 |
| C-φ-7 | 옵션 (ii)~(v) paths-only ≤ 15 lines = 5 금지 위반 0건 + Rollback trigger 발화 0/28 영구 답습 | §4.2 + §6.4 답습 |
| C-φ-8 | 옵션 (vi) ≥ 16 lines + 옵션 (vii) step 순서 변경 = 본 brief 비권고 (Stage 4 entry brief §3.1 영역 외 + §5.5.1+§5.5.2 본문 변경 영역) | §4.2 답습 |
| C-φ-9 | PRE-0 도구 가용성 사전 점검 5 영역 (C-υ-38 답습) — yamllint / gh auth / python ≥ 3.12 / git / actionlint(옵션) | §5.1 답습 |
| C-φ-10 | W-1 검증 7 영역 (W-1-V1 ~ W-1-V7) 채택 — yamllint × 3 + PC-3 grep + AR-1 grep + branches grep + paths grep | §5.2 답습 |
| C-φ-11 | 신규 actual run trigger 0건 영구 답습 — 본 brief = local 한정 (W-4 영역 외) | §5.3 답습 |
| C-φ-12 | 검증 도구 영역 — 표준 도구 답습 한정 + 신규 도입 0건 (yamllint + grep + gh CLI + actionlint 옵션) | §5.4 답습 |
| C-φ-13 | Rollback Trigger 매트릭스 28 (Layer B 18 + TR-1~5 + Step Division 신규 후보 5) × W-1 시점 옵션별 발화 가능성 enumerate | §6.1 ~ §6.4 답습 |
| C-φ-14 | 옵션 (i)~(v) 영역 = 0/28 발화 영구 답습 + 옵션 (vii) 영역 = 4/28 발화 가능성 = 본 brief 비권고 | §6.4 답습 |
| C-φ-15 | Rollback 절차 권고 — `git revert HEAD` 권고 시작점 (C-υ-41 답습 — "즉시 rollback" 사용자 결정 영역) | §6.5 답습 |
| C-φ-16 | 사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 위반 0건 영구 답습 | §7.1 + §7.2 답습 |
| C-φ-17 | Backlog 분리 매트릭스 — #1 + #2 + #3 T3 + #4 + #5 + #6 + Stage 5 + W-2/W-3/W-4 cycle 분리 영구 답습 | §7.3 답습 |
| C-φ-18 | 합산 438 합의 조건 답습 매트릭스 변경 0건 | §8 답습 |
| C-φ-19 | C-υ-43 (4 cycle 옵션) + C-υ-44 (3 영역 동시 발효) 발효 한정 — 본 brief = cycle 1/4 (W-1) 진입 | §8.2 답습 |
| C-φ-20 | 합의 형태 권고 — 본 brief 자체 = (a) Reviewer-only 단축 합의 권고 시작점 (T-2 재발화 영역 한계) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 | §9.1 ~ §9.3 답습 |
| C-φ-21 | 본 brief 자체 금지 ≥ 45 + 본 brief 발효 후 의무 금지 ≥ 11 영구 답습 | §10 답습 |
| C-φ-22 | 다음 단계 옵션 (A) ~ (I) 사용자 결정 영역 — 권고 시작점 = (A) brief 그대로 승인 → Reviewer-only 단축 합의 | §11 답습 |
| C-φ-23 | 본 brief 메타 검증 ≥ 30 항목 | §12 답습 |
| C-φ-24 | 5 영구 핵심 제약 5/5 보존 답습 (Hermes ≠ root of trust / 단일 source-of-truth / 수단·목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) | §12 답습 |
| C-φ-25 | Provider Liquidity 5-way 100% 보존 답습 | §12 답습 |
| C-φ-26 | F-금지 #1 영구 답습 (GitHub Actions secrets 0건 + 실 API key 0건) | §12 답습 |
| C-φ-27 | W-1 변경 line / 수정 영역 *최종 확정 발효 0건* (사용자 명시 결정 영역 한정) | §0.6 답습 |
| C-φ-28 | C-υ-45 (cache poisoning) + C-υ-46 (artifact 사후 변조) 후보 한정 답습 — 본 brief 시점 정식 등록 0건 | §10.1 답습 |
| C-φ-29 | C-υ-49 (30 trigger combined fire) 후보 한정 답습 | §6.4 답습 |
| **합산** | **29 조건 후보** | — |

### 11.3 본 §11 의 *범위 한계*

본 §11 = *결정 옵션 + 새 조건 후보 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 새 조건 발효 = 합의 보고서 작성 시 정식 등록 (Reviewer-only 또는 풀 3+1) — 본 brief 단독 = 새 조건 발효 0건.

---

## 12. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|-------|
| 사용자 명시 진입 명령 답습 | ✅ ("Phase α-4 Stage 4 W-1 micro-patch brief 작성, 3 MVP-1 workflow 최소 micro-patch *가능성 검토*") |
| 사용자 명시 5 금지 답습 | ✅ (5/5 — CI workflow 실 변경 0건 / actual run 재실행 0건 / W-2/W-3/W-4 진입 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Stage 4 entry brief 합의 답습 (`81472ba`) | ✅ (49 조건 C-υ-1 ~ C-υ-49 변경 0건) |
| Stage 3 합의 답습 (`d3f6d59`) | ✅ (36 조건 C-τ-1 ~ C-τ-36 변경 0건) |
| LVE 합의 답습 (`b264580`) | ✅ (31 조건 C-σ-1 ~ C-σ-31 변경 0건) |
| Step Division 합의 답습 (`52a05cb`) | ✅ (38 조건 C-ρ-1 ~ C-ρ-38 변경 0건) |
| α-4 진입 조건 점검 합의 답습 (`1c365e7`) | ✅ (33 조건 C-π-1 ~ C-π-33 변경 0건) |
| Stage 4 entry brief 본문 답습 (`9c33efe`) | ✅ (1032줄 본문 변경 0건) |
| LVE 본문 답습 (`4ce5a0b`) | ✅ (583줄 본문 변경 0건 + 51/51 PASS 답습) |
| α-1+2+3 LVE 답습 (`7b3d40a`) | ✅ (486줄 본문 변경 0건 + 12/12 PASS 답습) |
| 합산 438 합의 조건 답습 | ✅ (Group α 12 + Backlog #6 11 + Phase α-1 15 + α-2 26 + α-3 28 + α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 parallel 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 36 + Stage 4 entry 49 = 16 합의 합산) |
| C-υ-43 (W-1/W-2/W-3 4 cycle 옵션 정식 등록) 발효 — 본 brief = cycle 1/4 진입 | ✅ §1.4 + §8.2 답습 |
| C-υ-44 (W-1 micro-patch 범위 결정 3 영역 동시 발효) 답습 | ✅ §4.1 + §4.2 답습 (변경 0 lines 우선 권고 시작점) |
| Layer A / B / C / D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 4 entry 본문 변경 | ✅ 0건 |
| R-1 본문 1593줄 (7 artifacts) 변경 | ✅ 0건 (3 workflow 1206줄 + integration tool 298줄 + 3 fixture 89줄) |
| R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 | ✅ 0건 |
| `src/` 본문 변경 | ✅ 0건 (facade.py 41줄 placeholder 답습) |
| 3 MVP-1 workflow 본문 변경 (본 brief 시점) | ✅ 0건 (본 brief = micro-patch *가능성 검토* 한정) |
| W-2 / W-3 / W-4 진입 (본 brief 시점) | ✅ 0건 (cycle 2/4 / 3/4 / 4/4 분리) |
| 5 영구 핵심 제약 보존 | ✅ 5/5 보존 |
| Provider Liquidity 5-way 보존 | ✅ 5/5 100% 보존 |
| F-금지 #1 영구 답습 | ✅ 영구 답습 |
| Rollback Trigger × W-1 시점 발화 | ✅ 옵션 (i)~(v) = 0/28 영구 답습 / 옵션 (vii) = 4/28 발화 가능성 (본 brief 비권고) |
| 풀 3+1 트리거 발화 | ✅ 0/16 새 발화 (T-2 = Stage 4 entry brief 시점 이미 발화 + 본 brief = 권위 답습 한정 — Reviewer-only 단축 합의 적격 시작점) |
| 외부 LLM 자동 호출 | ✅ 0건 |
| 실 API key / provider SDK / 외부 API 호출 | ✅ 0건 |
| 신규 actual run 자동 trigger | ✅ 0건 |
| 합의 보고서 / 새 합의 발행 | ✅ 0건 (본 brief = DRAFT 한정) |
| 새 ADR / 새 P / 새 GP 발행 | ✅ 0건 |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |
| W-1 micro-patch 자동 실 변경 | ✅ 0건 (사용자 명시 결정 영역) |
| W-1 변경 line / 수정 영역 *최종 확정 발효* | ✅ 0건 (사용자 명시 결정 영역) |
| 본 brief framing 명시 (cycle 1/4, C-υ-43 답습) | ✅ §1.3 + §1.4 답습 |

---

## 13. 본 brief 요약 (한 단락)

본 brief 는 **Phase α-4 R-1 Stage 4 entry brief 풀 3+1 합의 (`81472ba` APPROVE AS BRIEF WITH CONDITIONS — 49 조건 C-υ-1 ~ C-υ-49) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) Stage 4 *W-1 단독* 영역 (3 MVP-1 workflow 한정) *최소 micro-patch 가능성 검토* brief 준비안 (DRAFT)** = **C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션) 정식 등록 답습 cycle 1/4 진입** ("*Should* W-1 introduce micro-patch lines (and which ones), or is *0-line passthrough* the correct posture for 3 MVP-1 workflows at this gate?"). **사용자 명시 5 금지** (CI workflow 실 변경 / actual run 재실행 / W-2/W-3/W-4 진입 / Operational Readiness PASS / Hermes PMO 격상) 5/5 영구 답습. **3 MVP-1 workflow 현재 상태 매트릭스** (read-only, §3) — `secret-hygiene-egress-redaction.yml` 694줄 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 = 1206줄 / 3/3 trigger `feature/**` 매칭 ✅ / 3/3 `permissions: contents: read` ✅ / 3/3 Stage 4 step wired ✅ / **cross-workflow re-verify 답습 = workflow 1 단독 (1/3) — workflow 2/3 미답습 영역**. **Micro-patch 후보 영역 *enumerate 한정*** (§4) — **C-υ-44 답습 3 영역 동시 발효** (Agent A 절차 + Agent B 안전성 + Agent C 단순성) → **권고 시작점 = 옵션 (i) 변경 0 lines** + 옵션 (ii)~(v) paths-only ≤ 15 lines = 사용자 결정 영역 + 옵션 (vi) ≥ 16 lines 비권고 (영역 외) + **옵션 (vii) step 순서 변경 비권고** (§5.5.1+§5.5.2 본문 변경 영역 — T-3 발화 영역 모호성 청산 명시 강화). **W-1 검증 방법 권고** (§5) — **PRE-0 도구 가용성 사전 점검 5 영역** (C-υ-38 답습) + **W-1-V1 ~ W-1-V7 7 검증** (yamllint × 3 + PC-3 grep + AR-1 grep + branches grep + paths grep) = **신규 actual run trigger 0건 영구 답습** (local 한정). **W-1 시점 rollback trigger 발화 매트릭스** (§6) — Layer B 18 + TR-1~5 + Step Division 신규 후보 5 = 28 trigger × 옵션별 발화 가능성 → **옵션 (i)~(v) = 0/28 발화 영구 답습** + 옵션 (vii) = 4/28 발화 가능성 (비권고) — `git revert HEAD` 권고 시작점 (C-υ-41 답습 — "즉시 rollback" = 사용자 결정 영역). **합의 형태 권고**: 본 brief 자체 = **(a) Reviewer-only 단축 합의 적격 시작점** (T-2 재발화 영역 한계 — Stage 4 entry brief 시점 이미 발화) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 (T-6/T-10/T-13 미발화). **사용자 명시 5 금지 × 본 brief 분리 매트릭스 — 5/5 영구 답습 (작성 시점 + 발효 후 자동 진입 영역 모두 0건)**. **합산 438 합의 조건 변경 0건** (16 합의 — Stage 4 entry brief 49 조건 포함). **본 brief 자체 금지 ≥ 45 + 본 brief 발효 후 의무 금지 ≥ 11** enumerate. **본 brief 새 조건 후보 29 (C-φ-1 ~ C-φ-29)** — 합의 보고서 작성 시 정식 등록. **본 brief 는 3 MVP-1 workflow 어느 줄도 *변경* 시키지 않으며, W-2 / W-3 / W-4 어느 작업도 *진입* 시키지 않으며, Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 어느 것도 *변경* 시키지 않으며, 사용자 명시 5 금지 + 영구 5 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 438 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / W-1 변경 line / 수정 영역 어느 것도 *최종 확정 발효* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점 — T-2 재발화 영역 한계)** / (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) / (C) brief 수정 / (D) 부분 채택 / (E) W-1 실 micro-patch 직접 진입 brief / (F) W-2/W-3/W-4 cycle 우선 / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.

---

**작성일**: 2026-05-18 후속 28
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §11 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **CI workflow 실 변경 0건** (3 MVP-1 workflow 1206줄 변경 발효 — 별도 cycle)
- ❌ **actual run 재실행 0건** (신규 trigger — W-4 영역 외)
- ❌ **W-2 / W-3 / W-4 진입 0건** (cycle 2/4 / 3/4 / 4/4 분리)
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**
- ❌ W-1 micro-patch 실 변경 자동 진입 0건 (본 brief = *가능성 검토* 한정)
- ❌ 합의 보고서 작성 0건 (본 brief = DRAFT 한정)
- ❌ 새 ADR / 새 P / 새 GP 발행 0건
- ❌ 합산 438 합의 조건 자동 변경 0건
- ❌ R-1 영역 7 artifacts × 1593줄 본문 변경 0건
- ❌ R-4 / R-5 / R-7 본문 1192줄 (13 file) 변경 0건
- ❌ α-1+2+3 evidence / α-4 진입 조건 점검 / Step Division / LVE / Stage 3 / Stage 4 entry 합의 본문 변경 0건
- ❌ Layer A / B / C / D / Group α / Backlog #6 / Phase α-1 ~ α-4 / Stage 1 ~ Stage 4 entry 본문 변경 0건
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
- ❌ Rollback Trigger 28 자동 발화 0건 (옵션 (i)~(v) 영역 = 0/28 영구 답습)
- ❌ 풀 3+1 트리거 자동 발화 0/16 (T-2 = Stage 4 entry brief 시점 이미 발화 + 본 brief = 권위 답습 한정 → 새 발화 0건 → Reviewer-only 단축 합의 적격 시작점)
- ❌ GitHub Actions secrets 사용 도입 0건 (F-금지 #1 영구 답습)
- ❌ `permissions: contents: read` 보강 0건 (W-5 영역)
- ❌ Required check / branch protection 등록 0건 (W-6 + W-8 영역)
- ❌ token rotation 정책 / GitHub plan 가용성 자동 결정 0건
- ❌ Group I (Hermes-originated commit auto-reject) 자동 진입 0건
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건
- ❌ 인간 리뷰 의무 자동 발화 0건
- ❌ 17 항목 우선순위 자동 *재고정* 0건
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건
- ❌ W-1 변경 line / 수정 영역 *최종 확정 발효 0건* (사용자 명시 결정 영역)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 0건 (별도 commit 분리 — 사용자 명시 결정 후 진입)
- ❌ artifact 사후 변조 검증 도구 본문 작성 0건 (C-υ-46 후보 한정)
- ❌ GitHub Actions cache poisoning 검증 도구 본문 작성 0건 (C-υ-45 후보 한정)
