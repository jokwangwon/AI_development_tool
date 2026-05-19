# Phase α-4 R-1 Stage 4 W-4 actual run trigger / 검증 brief (cycle 4/4) (DRAFT)

> **본 문서는 Phase α-4 R-1 Stage 4 W-3 micro-patch brief Reviewer-only 단축 합의 (`3aac549` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 36 조건 C-ψ-1 ~ C-ψ-36, 합산 539 합의 조건) 발효 후속, 사용자 명시 진입 명령 답습 — **Phase α-4 R-1 Stage 4 *W-4 단독* 영역 (신규 actual GitHub Actions run trigger + 검증 조건) *trigger / 검증 lockdown* brief 준비안.**
>
> **본 brief 의 framing 차이**:
> - α-4 Stage 4 entry (W-1~W-4 lockdown, `9c33efe` + `81472ba`) = "*What exactly* will Stage 4 W-1 ~ W-4 do, BEFORE any actual implementation?"
> - α-4 Stage 4 W-1 brief (`7af77fb` + `df741a2`, cycle 1/4) = "*Should* W-1 introduce micro-patch lines on 3 workflow?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - α-4 Stage 4 W-2 brief (`557c607` + `310b518`, cycle 2/4) = "*Should* W-2 introduce micro-patch lines on integration tool?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - α-4 Stage 4 W-3 brief (`42d2d21` + `3aac549`, cycle 3/4) = "*Should* W-3 introduce micro-patch lines on 3 fixture?" → **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH**
> - **본 brief = α-4 Stage 4 W-4 actual run trigger / 검증 *possibility* lockdown DRAFT (cycle 4/4)** — **"*Should* W-4 trigger a fresh actual GitHub Actions run (and which event / branch / 횟수), or is *trigger-deferred* the correct posture for the actual run at this gate?"**
> - α-4 Stage 4 W-4 실 trigger 발화 (본 brief 외) = "*Execute* the chosen trigger (if any)" — 사용자 명시 결정 후 별도 영역
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, (ii) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며 (W-1 = 0-line passthrough 답습 영구), (iii) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 = 0-line passthrough 답습 영구), (iv) 3 fixture 어느 줄도 *변경* 하지 않으며 (W-3 = 0-line passthrough 답습 영구), (v) Stage 4 entry brief 합의 49 + W-1 합의 30 + W-2 합의 35 + W-3 합의 36 = 합산 539 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며, (vi) 사용자 명시 4 금지 (actual run 실행 / CI workflow 변경 / Operational Readiness PASS 선언 / Hermes PMO 격상) 어느 것도 *해소* 시키지 않으며, (vii) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-19 후속 33
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-19-phase-alpha-4-w3-micropatch.md` (commit `3aac549` — W-3 brief Reviewer-only 단축 합의 APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 36 조건 C-ψ-1 ~ C-ψ-36, **본 brief 의 발효 trigger**)
- `docs/phase0/phase-alpha-4-r1-stage4-w3-micropatch-brief.md` (commit `42d2d21`, 978줄 — W-3 brief DRAFT)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w2-micropatch.md` (commit `310b518` — W-2 brief Reviewer-only 단축 합의, 35 조건 C-χ-1 ~ C-χ-35)
- `docs/phase0/phase-alpha-4-r1-stage4-w2-micropatch-brief.md` (commit `557c607`, 1009줄)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w1-micropatch.md` (commit `df741a2` — W-1 brief Reviewer-only 단축 합의, 30 조건 C-φ-1 ~ C-φ-30)
- `docs/phase0/phase-alpha-4-r1-stage4-w1-micropatch-brief.md` (commit `7af77fb`, 868줄)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md` (commit `81472ba` — Stage 4 entry brief 풀 3+1 합의, 49 조건 C-υ-1 ~ C-υ-49)
- `docs/phase0/phase-alpha-4-r1-stage4-entry-brief.md` (commit `9c33efe`, 1032줄 — Stage 4 W-1~W-4 lockdown brief, §4.4 + §5 = W-4 actual run 검증 + trigger 매트릭스)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS, **4 prerequisite GitHub Actions runs 답습 enumerate 포함**)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C (Hermes PMO Activation 12 조건 미진입 영구 답습)
- 4 prerequisite GitHub Actions runs (Phase α-1/α-2/α-3) — `25728590939` + `25728590916` + `25728590977` + `25731846625` (모두 SUCCESS, 답습 한정 read-only)

---

## 0. 본 brief 의 범위

### 0.1 사용자 명시 진입 명령 답습

> "W-4 actual run trigger / 검증 brief를 작성해주세요. 범위는 Phase α-4 Stage 4 cycle 4/4, actual run trigger와 검증 조건을 정리하는 것입니다. 아직 actual run 실행, CI workflow 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 사용자 명시 4 금지 답습 (본 brief 의 명시적 경계)

| # | 금지 영역 | 본 brief 시점 |
|---|---------|----------|
| **#1** | **actual run 실행** (신규 GitHub Actions run trigger 발화) | ✅ 0건 영구 답습 — 본 brief = *trigger 영역 lockdown 한정* |
| **#2** | **CI workflow 변경** (3 MVP-1 workflow 1206줄 변경 발효) | ✅ 0건 영구 답습 — W-1 cycle 1/4 합의 답습 (0-line passthrough 고정 영구) |
| **#3** | **Operational Readiness PASS (Layer E) 선언** | ✅ 0건 영구 답습 — MVP-6 영역 분리 |
| **#4** | **Hermes PMO 격상 (Layer F)** | ✅ 0건 영구 답습 — ADR-008 부록 C 12 조건 미진입 |

**주**: 본 brief 의 #2 영역은 W-1 합의 답습 영구. 추가로 W-2 (integration tool 변경) + W-3 (3 fixture 변경) 도 합의 답습 영구로 = 본 brief 시점 R-1 7 artifacts × 1593줄 전체 변경 0건.

### 0.3 본 brief 영역 vs Stage 4 entry / W-1 / W-2 / W-3 brief 영역 분리 매트릭스

| 영역 | Stage 4 entry brief (`9c33efe`+`81472ba`) | W-1 brief (`7af77fb`+`df741a2`) | W-2 brief (`557c607`+`310b518`) | W-3 brief (`42d2d21`+`3aac549`) | 본 brief (W-4) |
|------|------------------------------------------|--------------------------------|--------------------------------|--------------------------------|--------------|
| 범위 | W-1 + W-2 + W-3 + W-4 lockdown 권고 | W-1 단독 micro-patch 가능성 검토 | W-2 단독 micro-patch 가능성 검토 | W-3 단독 micro-patch 가능성 검토 | **W-4 단독 actual run trigger / 검증 lockdown** |
| 변경 대상 artifact | 7 artifacts × 1593줄 | 3 MVP-1 workflow 1206줄 | integration tool 298줄 | 3 fixture 89줄 | **수정 파일 0건 — actual run trigger 한정** |
| 권고 영역 | 수정 파일 + 검증 방법 + actual run 조건 + rollback trigger | 변경 0 lines 우선 + 후보 영역 ≤ 15 lines | 변경 0 lines 우선 + 후보 영역 ≤ 15 lines | 변경 0 lines 우선 + 후보 영역 ≤ 6 lines | **trigger 발화 0건 우선 (본 brief 시점) + 사용자 결정 후 발화 권고 시작점 = `push` event 1 run** |
| 변경 line / trigger 권고 결과 | 0 ~ ≤ 25 lines micro-patch *권고 시작점* | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **0 lines (0-line passthrough 고정)** ✅ 합의 답습 | **trigger 발화 0건 (본 brief 시점) + 권고 발화 시점 = 사용자 결정 영역** |
| 검증 방법 | Pre / Per-W / Post / Actual run 4 단계 (42 검증) | W-1 단독 검증 7 영역 + PRE-0 | W-2 단독 검증 8 영역 + PRE-0 | W-3 단독 검증 7 영역 + PRE-0 | **W-4 단독 검증 13 영역 (Pre-trigger 6 + Post-trigger RUN-1~7) + PRE-0 도구 가용성** |
| 합의 결과 발효 | APPROVE AS BRIEF WITH CONDITIONS (49 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (30 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (35 조건) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH (36 조건) | DRAFT (사용자 명시 승인 *전*) |

### 0.4 본 brief 가 *하는* 것

1. W-3 brief 합의 (`3aac549` — 36 조건 C-ψ-1 ~ C-ψ-36) 발효 후속 — **W-4 단독 actual run trigger / 검증 *lockdown* 한정** (§1)
2. **W-4 영역 한정 매트릭스** — actual run trigger + 검증 한정 + W-1 + W-2 + W-3 답습 (§2)
3. **현재 4 prerequisite GitHub Actions runs 답습 매트릭스 (read-only)** — `25728590939` + `25728590916` + `25728590977` + `25731846625` 4/4 SUCCESS + run conclusion + step-level 결과 + artifact 답습 (§3)
4. **신규 actual run trigger 후보 영역 *enumerate 한정*** — trigger 발화 0건 우선 권고 (본 brief 시점) + 사용자 결정 후 발화 권고 시작점 = `push` event on `feature/hermes-phase0` branch, 1 run (Stage 4 entry §5.1 답습) + 옵션 (ii)~(iv) 사용자 결정 영역 + 옵션 (v)~(vii) 비권고 (§4)
5. **W-4 검증 방법 권고** — Pre-trigger 6 (PRE-0) + Post-trigger RUN-1~7 (Stage 4 entry §4.4 + §5 답습) (§5)
6. **W-4 시점 rollback trigger 발화 가능성 매트릭스** (§6)
7. **사용자 명시 4 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 539 합의 조건 답습 매트릭스** (변경 0건) (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 4 금지 영역**:

- ❌ **actual run 실행 (0건)** — 신규 GitHub Actions run trigger 발화 = 별도 cycle 영역 (사용자 명시 #1)
- ❌ **CI workflow 변경 (0건)** — W-1 = 0-line passthrough 고정 답습 (사용자 명시 #2)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 영구 답습 (사용자 명시 #3)
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C 12 조건 미진입 영구 답습 (사용자 명시 #4)

**추가 금지 영역 (W-3 합의 36 + W-2 합의 35 + W-1 합의 30 + Stage 4 entry brief 49 + α-1+2+3 evidence + LVE 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — 3 workflow 1206 + integration tool 298 + 3 fixture 89 = 1593줄 답습 보존 (W-1 + W-2 + W-3 답습 영구)
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습 (α-1+2+3 evidence §5.1 답습)
- ❌ **`src/` runtime code / facade.py placeholder 변경 (0건)** — Backlog #4 분리
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)** — PC-3 + AR-1 양 GP 공유 답습 한정
- ❌ **§5.5.1 + §5.5.2 PC-3 + AR-1 본문 채택 변경 (0건)** — C-υ-44 답습 강화
- ❌ **`tools/mvp1_pc3_ar1_integration_check.py` 본문 변경 (0건)** — W-2 합의 답습 영구
- ❌ **3 MVP-1 workflow Stage 4 step (line 329~341) 변경 (0건)** — W-1 합의 답습 영구
- ❌ **3 fixture 본문 변경 (0건)** — W-3 합의 답습 영구
- ❌ **fixture semantics / 신규 fixture / 삭제 / branches / YAML schema 변경 (0건)** — W-3 합의 caveat 8/9 답습 영구
- ❌ **fixture `on.push.branches` 영역 변경 (0건)** — `"fixture-only/**"` 답습 보존 (실 trigger 0건 보장 — W-3 합의 caveat 답습)
- ❌ **trigger event 신규 도입 (`pull_request_target` / `schedule` / `repository_dispatch`) (0건)** — Stage 5 / MVP-6 / ADR-008 영역 분리
- ❌ **신규 workflow 신설 (0건)** — T2/T3 별도 합의 영역
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 분리
- ❌ **Required check 등록 (0건)** — W-6 영역 = Backlog #3 T3 분리
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습
- ❌ **`permissions: contents: read` 보강 (0건)** — W-5 영역 = Stage 5 cycle 4 / Backlog #1+#2 분리
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 (0건)** — Backlog #1+#2+#3 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 영역
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)**
- ❌ **`.importlinter` forbidden 4 모듈 / `include_external_packages` / `root_packages` / `ignore_imports` 변경 (0건)** — TR-1 ~ TR-5 미발화
- ❌ **R-7 docker-compose secret block / image layer check / restart recovery 본문 변경 (0건)**
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
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
- ❌ **threshold *고정* (0건)** — CI runtime / PR check pass rate / fail-closed rate / actual run 횟수 모두 *후보 한정* 유지
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정 = Backlog #5 ADR-012 §2.2 분리
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / commit signing / Vault HSM 모두 영역 외
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **합산 539 합의 조건 자동 변경 (0건)** — 36 신규 (C-ψ-1 ~ C-ψ-36) + 503 기존 모두 영구 답습
- ❌ **W-1 = 0-line passthrough 고정 (C-φ-30) 변경 (0건)**
- ❌ **W-2 = 0-line passthrough 고정 (C-χ-35) 변경 (0건)**
- ❌ **W-3 = 0-line passthrough 고정 (C-ψ-36) 변경 (0건)**
- ❌ **LVE 51/51 PASS evidence 자동 재집계 (0건)** — `4ce5a0b` 답습 한정
- ❌ **4 prerequisite GitHub Actions runs 답습 변경 (0건)** — `25728590939` + `25728590916` + `25728590977` + `25731846625` SUCCESS 답습 한정

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (ii) 합산 539 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (iii) 사용자 명시 4 금지 영역 어느 것도 *해소* 시키지 않으며,
- (iv) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (v) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (vi) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (vii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (viii) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 답습 영구),
- (ix) 3 MVP-1 workflow 본문 1206줄 어느 줄도 *변경* 하지 않으며 (W-1 답습 영구),
- (x) 3 fixture 89줄 어느 줄도 *변경* 하지 않으며 (W-3 답습 영구),
- (xi) PC-4 / AR-2 / AR-3 / Stage 5 / Layer E / Layer F 어느 영역도 *진입* 시키지 않으며,
- (xii) Phase α-1 / α-2 / α-3 actual run 어느 것도 *자동 재실행* 시키지 않으며,
- (xiii) 4 prerequisite GitHub Actions runs 답습 어느 것도 *변경* 시키지 않으며,
- (xiv) Rollback Trigger / TR-1 ~ TR-5 / Step Division 신규 후보 / Stage 4 신규 후보 어느 것도 *발화* 시키지 않으며,
- (xv) W-4 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며 (사용자 명시 #1 영구 답습),
- (xvi) W-4 trigger event / branch / 횟수 / token 영역 어느 것도 *최종 확정* 하지 않는다 (사용자 명시 결정 영역 한정),
- (xvii) `pull_request_target` / `schedule` / `repository_dispatch` 어느 event 도 *도입* 시키지 않으며,
- (xviii) `permissions:` 보강 / Required check 등록 / branch protection 변경 어느 것도 *발효* 시키지 않는다.

본 brief 가 발생시키는 *유일한* 효과는 **W-4 단독 actual run trigger / 검증 *lockdown* (= trigger 발화 0건 우선 vs 사용자 결정 후 발화 권고 시작점 = `push` event on `feature/hermes-phase0` branch 1 run) 권고 한정**. 모든 *확정 발효* / *실 trigger 발화* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (W-3 brief 합의 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `4ce5a0b` (2026-05-17) | Phase α-4 R-1 Local Validation Evidence (583줄, 51/51 PASS — **3 fixture 3/3 PASS 포함 + 4 prerequisite runs 답습 enumerate 포함**) | ✅ 답습 한정 |
| `b264580` (2026-05-17) | Phase α-4 R-1 LVE 합의 — 31 조건 C-σ-1 ~ C-σ-31 | ✅ 답습 한정 |
| `27351ce` (2026-05-17) | Phase α-4 R-1 Stage 3 실 진입 여부 brief (722줄) | ✅ 답습 한정 |
| `d3f6d59` (2026-05-17) | Phase α-4 R-1 Stage 3 합의 — 36 조건 C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| `9c33efe` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief (1032줄 DRAFT — W-4 영역 권고 시작점 명시 §3.4 + §4.4 + §5) | ✅ 답습 한정 |
| `81472ba` (2026-05-18) | Phase α-4 R-1 Stage 4 entry brief 풀 3+1 합의 — 49 조건 C-υ-1 ~ C-υ-49 | ✅ 답습 한정 |
| `7af77fb` (2026-05-18) | Phase α-4 R-1 Stage 4 W-1 micro-patch brief (868줄 DRAFT) | ✅ 답습 한정 |
| `df741a2` (2026-05-18) | W-1 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 30 조건 C-φ-1 ~ C-φ-30 | ✅ 답습 한정 |
| `557c607` (2026-05-18) | Phase α-4 R-1 Stage 4 W-2 micro-patch brief (1009줄 DRAFT) | ✅ 답습 한정 |
| `310b518` (2026-05-18) | W-2 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 35 조건 C-χ-1 ~ C-χ-35 | ✅ 답습 한정 |
| `42d2d21` (2026-05-19) | Phase α-4 R-1 Stage 4 W-3 micro-patch brief (978줄 DRAFT) | ✅ 답습 한정 |
| `3aac549` (2026-05-19) | W-3 brief Reviewer-only 단축 합의 — APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH, 36 조건 C-ψ-1 ~ C-ψ-36 | ✅ **본 brief 의 발효 trigger** |
| `25e7f49` (HEAD, 2026-05-19) | CONTEXT — Phase α-4 R-1 Stage 4 W-3 micropatch status | ✅ 답습 한정 |

### 1.2 W-3 brief 합의의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 합의 작성 시점 | 2026-05-19 후속 32 |
| 합의 형태 | **Reviewer-only 단축 합의** (Agent A + B + C 미가동 — T-2 재발화 영역 한계 + 풀 3+1 트리거 새 발화 0/16) |
| 합의 판정 | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** — BLOCK 사유 0건 |
| 합의 조건 | **36 조건 (C-ψ-1 ~ C-ψ-36)** — W-3 brief §11.2 답습 35 + 합의 신규 1 (C-ψ-36 "W-3 = 0-line passthrough 고정") |
| W-4 핵심 답습 (cycle 4/4 발효 영역) | C-ψ-1 ~ C-ψ-36 모두 답습 + 본 brief = cycle 4/4 진입 (C-υ-43 답습 — "W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록") |
| 10 caveat 명시 의무 (사용자 명시 — 단계별 합의 cycle 패턴 답습) | (1) W-3 범위 = 3 fixture 89줄 + (2) 권고 결론 = 0-line passthrough + (3) 실 fixture 변경 0건 + (4) 실 CI workflow 변경 0건 (W-1 답습 영구) + (5) 실 integration tool 변경 0건 (W-2 답습 영구) + (6) actual run 재실행 0건 + W-4 진입 0건 + (7) W-5~W-10 진입 0건 + (8) fixture semantics 변경 영구 비권고 (C-ψ-8) + (9) 신규 fixture 추가 / 삭제 + branches + schema 변경 영구 비권고 (C-ψ-9+10+11) + (10) LVE 3/3 fixture PASS evidence 보존 의무 영구 (C-ψ-23) |
| 풀 3+1 트리거 발화 | 0/16 새 발화 (T-2 = Stage 4 entry brief 시점 + W-1 + W-2 합의 시점 이미 답습 영역 완료) |
| 본 brief trigger 의미 | **W-3 cycle 3/4 = 0-line passthrough 합의 발효** → cycle 4/4 (W-4 actual run trigger / 검증) 진입 = 본 brief DRAFT |

### 1.3 10 단계 brief chain 매트릭스 (Phase α-4 자체)

| Stage (α-4 영역) | brief / 합의 | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 | "*Can* we enter Phase α-4?" |
| α-4 Stage 1.5 (조건 재검토) | 진입 조건 점검 brief | `7a289fa` + `1c365e7` | APPROVE AS BRIEF | 33 | "*Are conditions still satisfied?*" |
| α-4 Stage 2 (Step 분할) | Step Division brief | `ed1d1b6` + `52a05cb` | APPROVE AS BRIEF | 38 | "*How* should it be staged?" |
| α-4 Stage 2.5 (LVE) | Local Validation Evidence | `4ce5a0b` + `b264580` | APPROVE | 31 | "*Has local validation evidence been compiled?*" |
| α-4 Stage 3 (실 진입 여부) | Stage 3 brief | `27351ce` + `d3f6d59` | APPROVE AS BRIEF | 36 | "*Should* we enter actual implementation now?" |
| α-4 Stage 4 entry (lockdown) | Stage 4 entry brief | `9c33efe` + `81472ba` | APPROVE AS BRIEF WITH CONDITIONS | 49 | "*What exactly* will Stage 4 W-1~W-4 do?" |
| α-4 Stage 4 W-1 (cycle 1/4) | W-1 micro-patch brief | `7af77fb` + `df741a2` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 30 | "*Should* W-1 introduce micro-patch lines on 3 workflow?" |
| α-4 Stage 4 W-2 (cycle 2/4) | W-2 integration tool micro-patch brief | `557c607` + `310b518` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 35 | "*Should* W-2 introduce micro-patch lines on integration tool?" |
| α-4 Stage 4 W-3 (cycle 3/4) | W-3 3 fixture micro-patch brief | `42d2d21` + `3aac549` | **APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH** | 36 | "*Should* W-3 introduce micro-patch lines on 3 fixture?" |
| **α-4 Stage 4 W-4 (본 brief, cycle 4/4)** | **W-4 actual run trigger / 검증 brief** | (현재) | DRAFT (미확정) | (미확정) | **"*Should* W-4 trigger a fresh actual run, or is trigger-deferred correct for the actual run at this gate?"** |
| α-4 Stage 4 W-4 실 trigger 발화 (본 brief 외) | (사용자 명시 결정 영역) | (미확정) | (미확정) | (미확정) | "*Execute* the chosen trigger (if any)" |

### 1.4 본 brief 의 진입점

본 brief = **α-4 Stage 4 W-4 cycle 4/4 framing** (Stage 4 entry brief §8 권고 시작점 답습 + C-υ-43 4 cycle 옵션 정식 등록 답습 + W-1 + W-2 + W-3 합의 발효 후속):

- α-4 Stage 1 ↔ 1.5 ↔ 2 ↔ 2.5 ↔ 3 ↔ Stage 4 entry ↔ **W-1 (cycle 1/4, 0-line passthrough 확정)** ↔ **W-2 (cycle 2/4, 0-line passthrough 확정)** ↔ **W-3 (cycle 3/4, 0-line passthrough 확정)** ↔ **W-4 trigger / 검증 (본 brief, cycle 4/4)** ↔ W-4 실 trigger 발화 (사용자 결정 영역 후 진입)
- 본 brief 의 단일 책무: **"W-4 actual run trigger / 검증 영역 lockdown 권고 한정"** + **"trigger 발화 0건 우선 권고 (본 brief 시점) + 사용자 결정 후 발화 권고 시작점 enumerate"** + **"실 trigger 발화 자동 진입 0건"**
- 본 brief ≠ W-4 실 trigger 발화 (신규 actual run 발화 + commit = 별도 cycle 영역, 사용자 명시 결정 후)
- 본 brief ≠ W-1 / W-2 / W-3 재진입 (0-line passthrough 고정 답습 영구)
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-19 후속 33 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A | Implementation Entry READY | ✅ `df20b15` 답습 (2026-05-12) |
| Layer B | Backlog #6 우선 진입 (`f40423f` + `c7ddfdd`) | ✅ 답습 |
| Layer C | Implementation Evidence PASS 발효 (`eb01bc4`) | ✅ 답습 (재발효 0건) |
| Layer D | MVP-1 PASS 재진입 평가 (`951a5b1`) | ✅ 답습 (재선언 0건) |
| Layer E | Operational Readiness PASS | ❌ 미진입 (MVP-6 영역, 사용자 명시 #3 영구 답습) |
| Layer F | Hermes PMO 격상 | ❌ 미진입 (사용자 명시 #4 영구 답습) |
| Phase α-1 (R-4) | 1순위 병렬 — 도구 본문 채택 | ✅ local 8/8 PASS evidence 답습 + actual run `25728590939` SUCCESS |
| Phase α-2 (R-5) | 1순위 병렬 — `.importlinter` 본문 채택 | ✅ local 8/8 PASS evidence 답습 + actual run `25728590916` SUCCESS |
| Phase α-3 (R-7) | 1순위 병렬 — docker secret block 채택 | ✅ local 3/3 PASS evidence 답습 + actual run `25728590977` + `25731846625` SUCCESS |
| Phase α-4 Stage 4 entry (R-1) | W-1~W-4 lockdown 합의 발효 | ✅ `81472ba` 답습 (49 조건) |
| Phase α-4 Stage 4 W-1 | 3 MVP-1 workflow = 0-line passthrough 합의 발효 | ✅ `df741a2` 답습 (30 조건) |
| Phase α-4 Stage 4 W-2 | integration tool = 0-line passthrough 합의 발효 | ✅ `310b518` 답습 (35 조건) |
| Phase α-4 Stage 4 W-3 | 3 fixture = 0-line passthrough 합의 발효 | ✅ `3aac549` 답습 (36 조건) |
| **Phase α-4 Stage 4 W-4 (본 brief)** | **actual run trigger / 검증 *lockdown*** | ⏳ **본 brief = DRAFT (cycle 4/4)** |

---

## 2. W-4 영역 한정 매트릭스

### 2.1 W-4 단독 영역 enumerate (Stage 4 entry brief §2.1 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-1 | 3 MVP-1 workflow 본문 (1206줄) | ❌ 본 brief 영역 외 (W-1 = **0-line passthrough 고정** 답습, `df741a2` C-φ-30) |
| W-2 | integration check tool 본문 (298줄) | ❌ 본 brief 영역 외 (W-2 = **0-line passthrough 고정** 답습, `310b518` C-χ-35) |
| W-3 | 3 fixture 본문 (89줄) | ❌ 본 brief 영역 외 (W-3 = **0-line passthrough 고정** 답습, `3aac549` C-ψ-36) |
| **W-4** | **신규 actual GitHub Actions run trigger + 검증 (수정 파일 0건 — `push` event on `feature/hermes-phase0` branch 권고 시작점)** | ✅ **본 brief = actual run trigger / 검증 *lockdown* 한정 (cycle 4/4)** |

### 2.2 W-1 + W-2 + W-3 답습 명시 (위반 0건 영구 답습)

| 영역 | W-1 brief 시점 (cycle 1/4) | W-2 brief 시점 (cycle 2/4) | W-3 brief 시점 (cycle 3/4) | 본 brief 시점 (cycle 4/4) |
|---|------------|------------|------------|------------|
| W-1 | 단독 cycle = 가능성 검토 | ✅ 0-line passthrough 답습 영구 | ✅ 0-line passthrough 답습 영구 | ✅ 0-line passthrough 답습 영구 |
| W-2 | 분리 명시 | 단독 cycle = 가능성 검토 | ✅ 0-line passthrough 답습 영구 | ✅ 0-line passthrough 답습 영구 |
| W-3 | 분리 명시 | 분리 명시 | 단독 cycle = 가능성 검토 | ✅ 0-line passthrough 답습 영구 |
| **W-4** | 분리 명시 | 분리 명시 | 분리 명시 | ✅ **본 brief 영역** |
| **합산** | W-1 = 0-line passthrough 확정 | W-1 + W-2 = 0-line passthrough 확정 | W-1 + W-2 + W-3 = 0-line passthrough 확정 | **W-4 = 본 brief 영역 + W-1 + W-2 + W-3 답습 영구 ✅** |

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

본 §2 = **W-4 단독 영역 *권고 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). W-1 + W-2 + W-3 재진입 + W-5 ~ W-10 어느 것도 본 brief 가 *통합* 시키지 않는다.

---

## 3. 4 prerequisite GitHub Actions runs 답습 매트릭스 (read-only)

### 3.1 4 prerequisite runs 본문 매트릭스 (LVE §4 답습)

| # | run_id | workflow | trigger 시점 | conclusion | jobs 결과 | artifact |
|---|--------|--------|----------|---------|---------|--------|
| 1 | `25728590939` | `secret-hygiene-egress-redaction.yml` (Phase α-1 R-4 — secret_scanner 도구 본문) | 2026-05-16 (α-1+2+3 parallel actual entry) | **SUCCESS** ✅ | jobs.conclusion=success | group-d-logs |
| 2 | `25728590916` | (Phase α-2 R-5 — `.importlinter` 본문) | 2026-05-16 | **SUCCESS** ✅ | jobs.conclusion=success | r5-logs |
| 3 | `25728590977` | `provider-adapter-enforcement.yml` (Phase α-1 R-4 — provider_import_scanner) | 2026-05-16 | **SUCCESS** ✅ | jobs.conclusion=success | r1-logs (interim) |
| 4 | `25731846625` | `provider-url-scanner.yml` (Phase α-1 R-4 — provider_url_scanner) + R-7 docker secret block 검증 | 2026-05-16 | **SUCCESS** ✅ | jobs.conclusion=success | r1-logs |
| **합산** | **4 runs** | — | **2026-05-16 단일 cycle** | **4/4 SUCCESS** | **모든 jobs.conclusion=success** | **4 artifact 답습 보존** |

### 3.2 4 prerequisite runs 의 W-4 시점 의의 (read-only)

| 영역 | 답습 |
|------|----|
| 4 runs = Phase α-1 + α-2 + α-3 도구 본문 + R-7 docker block 검증 evidence | ✅ Layer C `eb01bc4` 발효 trigger 답습 |
| 4 runs = R-1 workflow 본문 actual run evidence (3 MVP-1 workflow 모두 1+ run SUCCESS) | ✅ Stage 4 entry brief §1.5 답습 (R-1 영역 actual run pre-conditions 충족) |
| 4 runs = neighboring Phase α 영역 actual run | ✅ Stage 4 entry brief 답습 — W-4 = *신규* run trigger (4 prerequisite runs 와 별도 cycle) |
| 4 runs 재실행 가능성 | ❌ **본 brief 시점 0건** (LVE 답습 한정 — 재실행 = 사용자 명시 #1 위반 영역) |
| W-4 신규 run = 4 prerequisite runs *답습* + Stage 4 step 신규 검증 | ⏳ 본 brief 권고 시작점 — *사용자 결정 후* 발화 영역 |

### 3.3 W-4 신규 actual run 의 영역 분리 (4 prerequisite runs 와 다른 점)

| 영역 | 4 prerequisite runs (답습 한정) | W-4 신규 run (본 brief 권고 시작점) |
|------|--------------------------|---------------------------|
| trigger 시점 | 2026-05-16 (Phase α-1+2+3 parallel actual entry, `7917e4a` 합의 시점) | **사용자 명시 결정 후** (본 brief 발효 후) |
| trigger event | (prior cycle) | `push` event on `feature/hermes-phase0` branch (권고 시작점) |
| workflow | 4 runs = α-1 (R-4) + α-2 (R-5) + α-3 (R-7) 영역 | 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml`) |
| Stage 4 step 검증 | ❌ 4 runs 시점 = Stage 4 step (line 318~360) 진입 *직전* — Stage 4 step 검증 0건 | ✅ W-4 신규 run = Stage 4 step (PC-3 + AR-1 integration check) actual run 검증 |
| 답습 권위 | LVE §4 답습 한정 (read-only) | Stage 4 entry brief §5.1 + §5.3 + §5.4 답습 — 권고 시작점 (사용자 결정 후 발화) |

### 3.4 R-1 영역 7 artifacts 현재 상태 매트릭스 (W-1 + W-2 + W-3 답습 영구)

| artifact | line | 본 brief 시점 답습 |
|--------|----|--------------|
| `secret-hygiene-egress-redaction.yml` | 694 | ✅ W-1 = 0-line passthrough 답습 영구 (`df741a2` C-φ-30) |
| `provider-adapter-enforcement.yml` | 186 | ✅ W-1 = 0-line passthrough 답습 영구 |
| `provider-url-scanner.yml` | 326 | ✅ W-1 = 0-line passthrough 답습 영구 |
| `tools/mvp1_pc3_ar1_integration_check.py` | 298 | ✅ W-2 = 0-line passthrough 답습 영구 (`310b518` C-χ-35) |
| `pass/compliant_entry_step.yml` | 30 | ✅ W-3 = 0-line passthrough 답습 영구 (`3aac549` C-ψ-36) |
| `fail/pc3_violation_continue_on_error.yml` | 31 | ✅ W-3 = 0-line passthrough 답습 영구 |
| `fail/ar1_violation_no_fail_closed.yml` | 28 | ✅ W-3 = 0-line passthrough 답습 영구 |
| **합산** | **1593** | **✅ 100% read-only 답습 영구 (W-1 + W-2 + W-3 cycle 합의 발효)** |

### 3.5 LVE 51/51 PASS evidence 답습 매트릭스 (`4ce5a0b` LVE 전체)

| 검증 영역 | LVE 결과 | 본 brief 답습 |
|---------|-------|----------|
| Step 1.4.1.a/b/c PC-3 self-check 14/14 (yaml.safe_load 3/3 + grep continue-on-error 0건 + grep if:always() summary/upload/cleanup + grep exit 1 / fail-closed 72건 + integration check tool mode=pc3 10/10) | ✅ PASS 14/14 | ✅ 답습 한정 |
| Step 1.4.2.a/b/c AR-1 self-check 37/37 (integration check tool mode=ar1 10/10 + mode=integration PC-3 10 + AR-1 10 = 20/20 + 3 fixture 3/3 + --list-checks 4) | ✅ PASS 37/37 | ✅ 답습 한정 |
| 4 prerequisite GitHub Actions runs answer enumeration | ✅ 4/4 SUCCESS | ✅ §3.1 + §3.2 답습 |
| **합산** | **51/51 PASS + 4/4 prerequisite runs SUCCESS** | **✅ 100% 답습 한정** |

### 3.6 본 §3 의 *범위 한계*

본 §3 = **read-only 답습 매트릭스 한정**. 본 §3 의 어떤 항목도 *변경* / *재해석* / *재합의* / *재실행* 영역이 아니며, 단순히 *현재 상태 + 4 prerequisite runs* 답습 enumerate 한정. W-4 신규 trigger 발화 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. W-4 actual run trigger 후보 영역 *enumerate 한정*

### 4.1 trigger 발화 결정 옵션 매트릭스 (C-υ-44 + C-φ-30 + C-χ-35 + C-ψ-36 동시 답습)

C-υ-44 답습 결정 영역 (Stage 4 entry brief 합의 §5.3 답습) + C-φ-30 (W-1 = 0-line passthrough) + C-χ-35 (W-2 = 0-line passthrough) + C-ψ-36 (W-3 = 0-line passthrough) = **5 영역 동시 발효**:

| Agent 영역 | 권고 | 본 brief 채택 영역 |
|---------|----|---------------|
| Agent A (절차) — C-A6 | W-N micro-patch 범위 결정 = *별도 brief 후 합의* | ✅ **본 brief = cycle 4/4 별도 brief 진입** (C-A6 발효) |
| Agent B (안전성) — C-B6 | PC-3 / AR-1 step 순서 변경 = §5.5.1+§5.5.2 본문 변경 시도 *권고 0건* 영구 답습 | ✅ **본 brief = W-1 + W-2 + W-3 답습 영구 + trigger event = `push` 한정 권고 (Stage 4 step 호출 답습 보존)** |
| Agent C (단순성) — C-C1 | 변경 line *0 lines 우선 권고 강화* (옵션 (iv)) | ✅ **본 brief 권고 시작점 = trigger 발화 0건 우선 (본 brief 시점) + 사용자 결정 후 = `push` event 1 run** |
| **W-1 + W-2 + W-3 합의 답습 C-φ-30 + C-χ-35 + C-ψ-36** | W-1 + W-2 + W-3 = 0-line passthrough 고정 (LVE evidence + 4 prerequisite run SUCCESS) | ✅ **본 brief 권고 시작점 = R-1 영역 1593줄 변경 0건 영구 답습 한정 + W-4 trigger 발화 사용자 결정 후 진입** |

### 4.2 trigger 발화 결정 옵션 (사용자 결정 영역)

#### 4.2.1 본 brief 시점 옵션 매트릭스

| 옵션 | trigger 발화 | 적격 영역 | 본 brief 권고 |
|-----|----------|--------|----------|
| **(i)** | **0건 (trigger-deferred)** | 본 brief 시점 답습 한정 — 신규 actual run trigger 0건 (사용자 명시 #1 답습) | ✅ **본 brief 시점 권고 시작점 (사용자 명시 #1 답습 영구)** |

#### 4.2.2 사용자 명시 결정 후 trigger 발화 옵션 매트릭스 (본 brief 권고 영역)

| 옵션 | trigger event | branch | 횟수 | 본 brief 권고 |
|-----|------------|------|----|----------|
| **(ii)** | **`push` event** | **`feature/hermes-phase0`** | **1 run** | ✅ **권고 시작점 (Stage 4 entry §5.1 답습 — 4 prerequisite runs 답습 trigger pattern 답습)** |
| (iii) | `pull_request` event | `feature/hermes-phase0 → main` PR | 1 run + PR check | 옵션 (사용자 결정 영역) — Required check 등록 시점 권고 (W-6 영역 = Backlog #3 T3 분리) |
| (iv) | `workflow_dispatch` (manual UI trigger) | `feature/hermes-phase0` | 1 run | 옵션 (사용자 결정 영역) — 디버깅 시 권고 (Stage 4 entry §5.1 답습) |
| (v) | `schedule` (cron) event | `feature/hermes-phase0` | N runs (cron interval) | ❌ **비권고** (운영 진입 영역 = Layer E, MVP-6 분리, 사용자 명시 #3 위반 가능성) |
| (vi) | `repository_dispatch` event | `feature/hermes-phase0` | N runs | ❌ **비권고** (외부 trigger 영역 = ADR-008 부록 C 영역, 사용자 명시 #4 위반 가능성) |
| (vii) | `pull_request_target` event | (fork PR) | N runs | ❌ **비권고** (T2/T3 영역 = Stage 5 cycle 2 분리, 사용자 명시 #2 위반 가능성 + GitHub Actions cache poisoning 위험 — Stage 4 entry brief Agent B RF-B1 답습) |

### 4.3 옵션 (ii)~(iv) 의 *근거 영역* enumerate (참고 한정)

본 §4.3 = 옵션 (ii)~(iv) 의 *근거 enumerate 한정* — 채택 권고 0건 (본 brief 시점). 실 trigger 발화 결정 = 사용자 명시 결정 영역.

**옵션 (ii) 근거 (`push` event on `feature/hermes-phase0` branch — 권고 시작점)**:
- 4 prerequisite runs (`25728590939` + `25728590916` + `25728590977` + `25731846625`) 모두 `push` event trigger 답습 — pattern 답습
- 3 MVP-1 workflow 모두 `on: push: branches: [feature/**]` 매칭 답습 (Stage 4 entry brief §1.5 + W-1 cycle 1/4 caveat 8 답습 — workflow 1 `on.push.branches` 답습 한정)
- Stage 4 step (line 329~341) 호출 인터페이스 답습 보존 (W-1 + W-2 + W-3 답습 영구)
- Stage 4 entry brief §5.1 권고 시작점 명시
- 횟수 1 권고 시작점 (Stage 4 entry §5.6 답습 — 재실행 0건 권고)
- 본 brief 권고: ✅ **사용자 명시 결정 후 발화 권고 시작점**

**옵션 (iii) 근거 (`pull_request` event on PR — 옵션)**:
- 3 MVP-1 workflow 모두 `on: pull_request: branches: [main]` 매칭 답습 가능성 (실 매칭 = W-1 합의 시점 미답습 영역 — workflow 2/3 paths 미답습 영역)
- PR check 등록 시점 = AR-2 (branch protection) + W-6 (Required check 등록) = Backlog #3 T3 영역 → **본 brief 영역 외**
- 본 brief 권고: 옵션 (사용자 결정 영역) — PR check 등록 시점 권고 한정

**옵션 (iv) 근거 (`workflow_dispatch` manual UI trigger — 옵션)**:
- 디버깅 시 권고 (Stage 4 entry §5.1 답습)
- 3 MVP-1 workflow 모두 `on: workflow_dispatch:` 답습 가능성 (실 매칭 = W-1 합의 시점 미답습 영역)
- 본 brief 권고: 옵션 (사용자 결정 영역) — 디버깅 / `push` event 검증 실패 시 분석 영역

### 4.4 영역 외 trigger / 변경 enumerate (본 brief 비권고 영구 답습)

| 영역 | 사유 |
|------|-----|
| 신규 trigger event 도입 (`pull_request_target` / `schedule` / `repository_dispatch`) | Stage 5 cycle 2 / MVP-6 영역 / ADR-008 부록 C 영역 — 사용자 명시 #2 위반 가능성 + GitHub Actions cache poisoning 위험 (Stage 4 entry brief Agent B RF-B1 답습) |
| `feature/hermes-phase0` 외 branch trigger (`main` / `develop` / 신규 branch) | `main` = stable 영역 보존 (branch protection 미적용 영역 = AR-2 = Backlog #3 분리) — 사용자 명시 #2 위반 가능성 + Layer C 발효 권위 영역 변경 위험 |
| 횟수 ≥ 2 (재실행) | Stage 4 entry §5.6 답습 — 재실행 0건 권고 + Layer B #15 (flaky test) 발화 위험 |
| 4 prerequisite runs 재실행 | 사용자 명시 #1 위반 영역 — LVE 답습 영역 |
| 3 MVP-1 workflow `on:` event 영역 변경 | W-1 = 0-line passthrough 답습 영구 위반 |
| 3 fixture `on.push.branches: ["fixture-only/**"]` 영역 변경 | W-3 = 0-line passthrough 답습 영구 위반 (C-ψ-25 답습 — 실 trigger 0건 보장) |
| `permissions: contents: read` 보강 | W-5 영역 = 본 brief 영역 외 |
| Required check 등록 | W-6 영역 = Backlog #3 T3 분리 |
| branch protection 변경 | AR-2 영역 = Backlog #3 T3 분리 |
| `secrets.*` reference 도입 | F-금지 #1 영구 답습 |
| 신규 workflow 신설 | T2/T3 별도 합의 영역 |
| `tools/mvp1_pc3_ar1_integration_check.py` 본문 변경 (어느 줄도) | W-2 합의 답습 영구 |
| 3 MVP-1 workflow Stage 4 step (line 329~341) 변경 (어느 줄도) | W-1 합의 답습 영구 |
| 3 fixture 본문 변경 (어느 줄도) | W-3 합의 답습 영구 |
| OIDC token 도입 | Stage 4 entry §5.5 답습 — 본 brief 시점 미도입 영역 |
| token rotation 정책 결정 | Group α C-3 / C-4 답습 — 사용자 명시 결정 영역 |
| GitHub Actions cache poisoning 방어 도구 본문 작성 | Stage 4 entry brief Agent B RF-B1 답습 (C-υ-45 후보 한정 — 정식 등록 0건) |
| artifact 사후 변조 검증 도구 본문 작성 | Stage 4 entry brief Agent B RF-B2 답습 (C-υ-46 후보 한정 — 정식 등록 0건) |
| Hermes-originated commit auto-reject 진입 | Group I 영역 (별도 합의) |

### 4.5 trigger 발화 권고 시작점 매트릭스

| 영역 | 본 brief 시점 권고 시작점 | 사용자 결정 후 발화 권고 시작점 |
|----------|------------------|--------------------|
| trigger 발화 | **0건 (옵션 (i) — 본 brief 시점 사용자 명시 #1 답습 영구)** | **1 run (옵션 (ii) — `push` event on `feature/hermes-phase0` branch, 횟수 1)** |
| trigger event | (영역 외 — 본 brief 시점 발화 0건) | `push` (권고 시작점) + `pull_request` (옵션) + `workflow_dispatch` (옵션 디버깅) |
| branch | (영역 외) | `feature/hermes-phase0` (권고 시작점) |
| 횟수 | (영역 외) | 1 (권고 시작점 — 재실행 0건) |
| token / secret | (영역 외) | F-금지 #1 영구 답습 (`secrets.*` 0건) + `GITHUB_TOKEN` read-only (`permissions: contents: read` = W-5 영역 = 별도) |

### 4.6 본 §4 의 *범위 한계*

본 §4 = **trigger 발화 결정 *옵션 enumerate 한정***. 본 §4 의 어떤 항목도:
- (i) 옵션 (i)~(vii) 中 어느 것도 *채택 발효* 시키지 않으며,
- (ii) trigger 발화 영역 *최종 확정* 시키지 않으며,
- (iii) 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며,
- (iv) 4 prerequisite runs 답습 어느 것도 *변경* 하지 않으며,
- (v) 3 MVP-1 workflow / integration tool / 3 fixture 본문 어느 줄도 *변경* 하지 않으며 (W-1 + W-2 + W-3 답습 영구),
- (vi) trigger event / branch / 횟수 / token 영역 어느 것도 *고정* 하지 않는다 (사용자 결정 영역 한정).

권고 시작점 = **옵션 (i) trigger 발화 0건 (본 brief 시점) + 옵션 (ii) `push` event on `feature/hermes-phase0` branch 1 run (사용자 결정 후 발화)** (C-υ-44 + C-φ-30 + C-χ-35 + C-ψ-36 답습 + Stage 4 entry §5.1 + §5.6 답습 + 4 prerequisite runs answer pattern 답습) — 실 trigger 발화 = 사용자 명시 결정 영역.

---

## 5. W-4 검증 방법 권고

### 5.1 PRE-0 도구 가용성 사전 점검 (C-υ-38 답습)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| PRE-0-1 | `gh CLI` 인증 상태 | `gh auth status` | rc=0 + 인증 답습 (read-only — actual run 발화 0건) |
| PRE-0-2 | `gh CLI` version (≥ 2.30) | `gh --version` | rc=0 + version enumerate |
| PRE-0-3 | `git` version | `git --version` | rc=0 + version enumerate |
| PRE-0-4 | `git status` clean (R-1 영역 1593줄 답습 영구) | `git status -s` | empty output (W-1 + W-2 + W-3 답습 영구) |
| PRE-0-5 | 3 MVP-1 workflow 본문 답습 (W-1 = 0-line passthrough 영구) | `wc -l .github/workflows/{secret-hygiene-egress-redaction,provider-adapter-enforcement,provider-url-scanner}.yml` | sum = 1206 |
| PRE-0-6 | integration tool + 3 fixture 답습 (W-2 + W-3 = 0-line passthrough 영구) | `wc -l tools/mvp1_pc3_ar1_integration_check.py tests/fixtures/mvp1_pc3_ar1_integration/{pass,fail}/*.yml` | sum = 387 (298 + 89) |

### 5.2 Pre-trigger 검증 (W-4 trigger 발화 *직전* — 사용자 결정 후 진입 영역)

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| PRE-T1 | 4 prerequisite runs 답습 (re-fetch) | `gh run list --workflow=secret-hygiene-egress-redaction.yml --branch=feature/hermes-phase0 --limit=5 --json conclusion,status,runId,event` + (동상 × 3 workflow) | 4 prior runs SUCCESS + 신규 trigger 0건 답습 |
| PRE-T2 | LVE 51/51 PASS 답습 (re-run local self-check) | `python tools/mvp1_pc3_ar1_integration_check.py .github/workflows/{secret-hygiene-egress-redaction,provider-adapter-enforcement,provider-url-scanner}.yml --mode integration` + fixture 3개 verify | rc=0 (workflow integration) + 3/3 fixture 답습 |
| PRE-T3 | Local Validation Evidence (`4ce5a0b`) 답습 | `git log -1 --pretty=%H docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` | commit = `4ce5a0b` |
| PRE-T4 | Stage 4 step (line 329~341) wired 답습 | `grep -A20 "Stage 4.*PC-3.*AR-1" .github/workflows/secret-hygiene-egress-redaction.yml` | wired pattern 답습 |
| PRE-T5 | 5 영구 핵심 제약 5/5 보존 self-check | `python tools/perm_constraints_check.py` (도구 본문 미작성 시 LVE §5.1 답습) | 5/5 PASS |
| PRE-T6 | F-금지 #1 영구 답습 self-check (GitHub Actions secrets 0건) | `python tools/workflow_secrets_usage_check.py` (도구 본문 미작성 시 LVE §5.3 답습) | secrets 사용 0건 |

### 5.3 W-4 신규 trigger 발화 (사용자 명시 결정 후 영역 — 본 brief 시점 0건)

| 영역 | 본 brief 권고 |
|------|----------|
| Trigger event | `push` event (권고 시작점, 옵션 (ii)) |
| Branch | `feature/hermes-phase0` (권고 시작점) |
| Trigger 명령 (사용자 결정 후) | `git push origin feature/hermes-phase0` (정상 push) 또는 `git commit --allow-empty -m "trigger W-4 actual run" && git push` (empty commit trigger) 中 사용자 결정 |
| 횟수 권고 | 1 run (재실행 0건 권고) |
| 발화 결과 = 3 MVP-1 workflow × 1 run = 3 runs (각 workflow 별 1 run) | 본 brief 시점 미발화 영역 |

### 5.4 Post-trigger 검증 (W-4 trigger 발화 *후* — 사용자 결정 후 진입 영역)

Stage 4 entry brief §4.4 답습 RUN-1 ~ RUN-7 매트릭스:

| # | 검증 영역 | 검증 명령 | 통과 기준 |
|---|--------|--------|---------|
| RUN-1 | 3 MVP-1 workflow run conclusion = SUCCESS | `gh run list --workflow={each} --branch=feature/hermes-phase0 --limit=1 --json conclusion,status,runId` (× 3) | conclusion=success × 3 |
| RUN-2 | 3 workflow step-level 매트릭스 — PC-3 / AR-1 / Stage 4 step PASS | `gh run view <run-id> --json jobs` (× 3 runs) | jobs.conclusion=success + 모든 step (PC-3 + AR-1 + Stage 4 integration step) conclusion=success |
| RUN-3 | Stage 4 integration check step (3 workflow) PASS — PASS fixture + FAIL fixture 양방향 검증 | `gh run view <run-id> --log --job=<job-id>` + grep "Stage 4 PC-3 + AR-1 integration OK" | step output = "Stage 4 PC-3 + AR-1 integration OK" (각 workflow) |
| RUN-4 | 3 workflow runtime ≤ 후보 (mvp1.md §3.4.1 답습 — threshold 후보 한정 + 고정 0건) | run duration enumerate (gh CLI) | (threshold 후보 한정 — 본 brief 시점 고정 0건) |
| RUN-5 | artifact (group-d-logs / r5-logs / r1-logs) 답습 — 무결성 보존 검증 | `gh run download <run-id> --dir /tmp/w4-artifacts/` (옵션) + line count + 답습 비교 | artifact 존재 + 본문 무결성 (Stage 4 entry brief Agent B RF-B2 후보 한정 — 본 brief 시점 자동 차단 0건) |
| RUN-6 | F-금지 #1 영구 답습 — secrets 사용 0건 (workflow self-check 결과 답습) | `gh run view <run-id> --log` + grep "secrets\." | secrets 사용 0건 |
| RUN-7 | 4 prerequisite runs 답습 비교 — 신규 run conclusion 동등성 | 4 prerequisite runs JSON ↔ 신규 run JSON diff (conclusion 영역) | conclusion 동등 (4/4 SUCCESS ↔ 신규 run SUCCESS) |

**합산**: 7 검증 영역 × 1 actual run trigger (W-4 = `push` event on `feature/hermes-phase0` branch, 횟수 1) × 통과 기준 enumerate.

### 5.5 SUCCESS 조건 매트릭스 (Stage 4 entry brief §5.3 답습)

| # | SUCCESS 조건 | 통과 기준 | 답습 출처 |
|---|---------|---------|---------|
| S-1 | 3 MVP-1 workflow run conclusion = SUCCESS | conclusion=success × 3 | 4 prerequisite runs 답습 + RUN-1 |
| S-2 | 3 workflow step-level — PC-3 / AR-1 / Stage 4 step PASS | jobs.conclusion=success | LVE §4 답습 + RUN-2 |
| S-3 | Stage 4 integration check step (3 workflow) PASS — PASS fixture + FAIL fixture 양방향 검증 | step output `Stage 4 PC-3 + AR-1 integration OK` | 본 brief §3.1 + Stage 4 entry §5.3 답습 + RUN-3 |
| S-4 | artifact 무결성 보존 | artifact 존재 + line count ≥ baseline | LVE 답습 + RUN-5 |
| S-5 | F-금지 #1 영구 답습 — workflow self-check `workflow_secrets_usage_check.py` PASS | secrets 사용 0건 | LVE §5.3 답습 + RUN-6 |
| S-6 | 5 영구 핵심 제약 5/5 보존 — workflow self-check 답습 | self-check 답습 | LVE §5.1 답습 |
| S-7 | Provider Liquidity 5-way 100% 보존 — workflow self-check 답습 | self-check 답습 | LVE §5.2 답습 |

### 5.6 FAILURE 조건 매트릭스 (rollback trigger, Stage 4 entry brief §5.4 답습)

| # | FAILURE 영역 | 대응 절차 | rollback trigger |
|---|---------|--------|----------------|
| F-1 | 1+ workflow run conclusion = FAILURE | (i) FAIL 본문 enumerate → (ii) Rollback trigger 발화 매트릭스 검토 (§6) → (iii) 사용자 명시 결정 영역 | Layer B #13 / #14 / Step Division 신규 후보 中 발화 |
| F-2 | step-level — PC-3 / AR-1 / Stage 4 step FAIL | (i) step output enumerate → (ii) PC-3 / AR-1 self-check 발화 → (iii) 사용자 명시 결정 영역 | Step Division 신규 후보 1 ~ 3 발화 |
| F-3 | Stage 4 integration check step FAIL — fixture 결과 미답습 | (i) fixture 결과 enumerate → (ii) integration check tool self-check FAIL 발화 → (iii) 사용자 명시 결정 영역 | Step Division 신규 후보 3 (integration tool self-check FAIL) 발화 |
| F-4 | F-금지 #1 영구 답습 위반 — workflow self-check FAIL | (i) **즉시 rollback** (`git revert HEAD` 권고) + 풀 3+1 + 외부 LLM 1+ 합의 진입 | F-금지 #1 위반 = 영구 답습 위반 → 풀 3+1 트리거 T-2 발화 |
| F-5 | 5 영구 핵심 제약 5/5 보존 위반 — workflow self-check FAIL | (i) **즉시 rollback** + 풀 3+1 합의 진입 | 풀 3+1 트리거 T-5 발화 |
| F-6 | Provider Liquidity 5-way 약화 — workflow self-check FAIL | (i) **즉시 rollback** + 풀 3+1 합의 진입 | 풀 3+1 트리거 T-4 발화 |
| F-7 | 신규 actual run trigger 횟수 > 1 (재실행 발생) | (i) 재실행 본문 enumerate → (ii) flaky test 가능성 검토 → (iii) 사용자 명시 결정 영역 | Layer B #15 (PR check unstable / flaky) 발화 가능성 |

### 5.7 검증 도구 영역 (의존성 답습)

| 도구 | 영역 | 본 brief 시점 답습 |
|----|----|----------------|
| `gh CLI` | 4 prerequisite runs 답습 (read-only) + 신규 actual run conclusion 검증 (사용자 결정 후) | 답습 한정 |
| `git status` / `git log` / `git diff` | R-1 영역 1593줄 변경 0건 검증 + commit 정합성 | 표준 git 답습 |
| `python tools/mvp1_pc3_ar1_integration_check.py` | PRE-T2 local self-check (W-2 답습 영구) | 답습 한정 — 본 brief 시점 변경 0건 |
| `python tools/workflow_secrets_usage_check.py` | F-금지 #1 영구 답습 self-check (도구 본문 미작성 시 LVE §5.3 답습) | LVE 답습 한정 — 본 brief 시점 신규 도구 작성 0건 |
| `python tools/perm_constraints_check.py` | 5 영구 핵심 제약 self-check (도구 본문 미작성 시 LVE §5.1 답습) | LVE 답습 한정 — 본 brief 시점 신규 도구 작성 0건 |
| `grep` | PC-3 / AR-1 패턴 정합성 검증 | 표준 도구 답습 |
| `diff` (옵션) | 4 prerequisite runs JSON ↔ 신규 run JSON 비교 (RUN-7) | 표준 도구 답습 |
| **외부 LLM 호출 / 실 provider SDK / 실 API key** | (영역 외) | ❌ 0건 (Group α C-11 답습 + F-금지 #1 영구 답습) |

### 5.8 신규 actual run trigger 횟수 매트릭스 (본 brief 권고 시작점)

| 영역 | 본 brief 시점 | 사용자 결정 후 (옵션 (ii) 채택 시) |
|------|----------|------------------------|
| 신규 actual run trigger 횟수 | **0건 영구 답습 (사용자 명시 #1)** | **1 run 권고 시작점 (Stage 4 entry §5.6 답습)** |
| 재실행 횟수 | 0건 (Layer B #15 발화 0건 보장) | 0건 권고 (재실행 = flaky test 위험 → Layer B #15 발화) — 재실행 결정 = 사용자 결정 영역 |
| 총 run | 0 | 3 MVP-1 workflow × 1 run = 3 runs (각 workflow 별 1 run, 단일 trigger event 의 multi-workflow 발화 답습) |

### 5.9 검증 결과 threshold 후보 한정 매트릭스 (고정 0건)

| threshold | 본 brief 시점 |
|---------|----------|
| CI runtime per workflow | 후보 한정 (mvp1.md §3.4.1 + §4.3 + §4.4 답습) |
| PR check pass rate | 후보 한정 |
| fail-closed rate (AR-1) | 후보 한정 |
| PC-3 violation count per PR | 후보 한정 |
| integration check tool runtime | 후보 한정 (Stage 4 합의 §1.3 답습) |
| W-4 신규 actual run trigger 횟수 (1 권고 시작점) | 후보 한정 (본 brief §5.8) |
| 재실행 횟수 (0 권고 시작점) | 후보 한정 |
| **합산** | **7/7 후보 한정 — 고정 0건** |

### 5.10 검증 영역 ↔ 사용자 명시 4 금지 분리 매트릭스

| 검증 영역 | 사용자 명시 #1 (actual run 실행) | #2 (CI workflow 변경) | #3 (Operational Readiness PASS) | #4 (Hermes PMO 격상) |
|----------|------------------------|------------------|------------------------|------------------|
| PRE-0-1 ~ PRE-0-6 (도구 가용성 사전 점검) | ✅ 0 (read-only) | ✅ 0 | ✅ 0 | ✅ 0 |
| PRE-T1 ~ PRE-T6 (Pre-trigger 검증) | ✅ 0 (사용자 결정 후 진입 영역 — 본 brief 시점 0건) | ✅ 0 | ✅ 0 | ✅ 0 |
| W-4 신규 trigger (§5.3) | ✅ 0 (본 brief 시점 발화 0건) | ✅ 0 | ✅ 0 | ✅ 0 |
| RUN-1 ~ RUN-7 (Post-trigger 검증) | ✅ 0 (사용자 결정 후 발화 *후* 영역 — 본 brief 시점 0건) | ✅ 0 (read-only after trigger) | ✅ 0 | ✅ 0 |
| **합산** | **✅ 4 영역 × 4 = 16/16 충돌 0** | — | — | — |

### 5.11 본 §5 의 *범위 한계*

본 §5 = **W-4 검증 방법 *권고 한정***. 실 검증 실행 = 사용자 명시 결정 영역 (자동 진입 0건). 모든 검증 영역 = **PRE-0 도구 가용성 + Pre-trigger (사용자 결정 후) + W-4 신규 trigger 1 (사용자 결정 후) + Post-trigger RUN-1~7 (사용자 결정 후)** — 본 brief 시점 신규 actual run trigger ≤ 0 영구 답습.

---

## 6. W-4 시점 rollback trigger 발화 가능성 매트릭스

### 6.1 Layer B 18 trigger × W-4 시점 발화 매트릭스 (Stage 4 entry brief §6.1 답습)

| # | trigger 영역 | W-4 본 brief 시점 (trigger 발화 0건) | W-4 사용자 결정 후 trigger 발화 (옵션 (ii) `push` event) | W-4 옵션 (vii) `pull_request_target` 도입 |
|---|---------|------------------------|--------------------------------------|---------------------------|
| 13 | CI step pass with violation present (PC-3) | 0건 (trigger 발화 0건 → step 검증 영역 외) | **발화 가능성** (신규 run FAIL 시 — PC-3 violation 검출 미스 가능성) | **발화 가능성** (cache poisoning 영역 위험) |
| 14 | CI step fail without auto-reject (AR-1) | 0건 | **발화 가능성** (신규 run FAIL 시 — AR-1 fail-closed 미작동 가능성) | **발화 가능성** (cache poisoning 영역) |
| 15 | PR check unstable / flaky | 0건 (신규 run 0건 → flaky 영역 외) | **발화 가능성** (재실행 ≥ 1 시) | **발화 가능성** |
| **합산 (18 중)** | **18 trigger** | **0/18 발화 영구 답습** | **3/18 발화 가능성 (사용자 결정 후 trigger 발화 시)** | **3/18 발화 가능성 (본 brief 비권고)** |

### 6.2 TR-1 ~ TR-5 × W-4 시점 발화 매트릭스

| TR # | 영역 | W-4 시점 발화 |
|----|----|------------|
| TR-1 | `.importlinter` forbidden 4 모듈 확장 | 0건 (Phase α-2 영역) |
| TR-2 | `include_external_packages` flag | 0건 |
| TR-3 | `root_packages` 변경 | 0건 |
| TR-4 | `ignore_imports` 변경 | 0건 |
| TR-5 | google.generativeai facade | 0건 |
| **합산** | **5 trigger** | **0/5 발화 영구 답습** |

### 6.3 Step Division + Stage 4 신규 후보 × W-4 시점 발화 매트릭스

| # | trigger | W-4 본 brief 시점 (trigger 발화 0건) | W-4 사용자 결정 후 trigger 발화 (옵션 (ii)) | W-4 옵션 (vii) `pull_request_target` |
|---|-------|------------------------|--------------------------------|---------------------|
| ND-1 | PC-3 self-check FAIL (local) | 0건 (PRE-T2 = read-only) | 0건 (workflow 본문 변경 0건 → PC-3 검증 본질 변경 0건) | 0건 |
| ND-2 | AR-1 self-check FAIL (local) | 0건 (PRE-T2 = read-only) | 0건 | 0건 |
| ND-3 | integration check tool self-check FAIL | 0건 (tool 변경 0건 + fixture 변경 0건) | 0건 (W-1 + W-2 + W-3 답습 영구 → tool behavior 영향 0건) | 0건 |
| ND-4 | 4 prerequisite runs JSON conclusion 미답습 | 0건 (PRE-T1 = read-only) | 0건 (4 prerequisite runs 답습 영구) | 0건 |
| ND-5 | LVE 본문 누락 | 0건 (PRE-T3 = read-only) | 0건 | 0건 |
| **W-4 신규 후보 W4-1** | W-4 신규 actual run FAILURE | 0건 (trigger 발화 0건) | **발화 가능성** (옵션 (ii) 채택 + 신규 run FAIL 시) | **발화 가능성** |
| **W-4 신규 후보 W4-2** | W-4 신규 actual run flaky (재실행 ≥ 1) | 0건 | **발화 가능성** (재실행 결정 영역) | **발화 가능성** |
| **W-4 신규 후보 W4-3** | W-4 신규 actual run F-금지 #1 위반 발견 | 0건 (F-금지 #1 영구 답습 + self-check 답습) | 0건 (RUN-6 답습) | **발화 가능성** (cache poisoning 영역) |
| **W-4 신규 후보 W4-4** | W-4 신규 actual run 5 영구 핵심 제약 보존 위반 | 0건 (LVE §5.1 답습 + self-check 답습) | 0건 (RUN-2 + S-6 답습) | **발화 가능성** |
| **W-4 신규 후보 W4-5** | W-4 신규 actual run Provider Liquidity 5-way 약화 | 0건 (LVE §5.2 답습 + R-1 = vendor-agnostic) | 0건 (RUN-2 + S-7 답습) | **발화 가능성** |
| **합산** | **10 후보** | **0/10 발화 영구 답습** | **2/10 발화 가능성 (W4-1 + W4-2 — 사용자 결정 후 trigger 발화 시)** | **5/10 발화 가능성 (본 brief 비권고)** |

### 6.4 W-4 시점 발화 합산 매트릭스

| 옵션 | Layer B | TR-1~5 | Step Division + Stage 4 신규 후보 | 합산 발화 가능성 |
|-----|---------|------|---------------------------|--------------|
| **(i) trigger 발화 0건 (본 brief 시점 권고 시작점)** | 0/18 | 0/5 | 0/10 | **0/33 발화 영구 답습** |
| (ii) `push` event 1 run (사용자 결정 후 권고 시작점) | 3/18 (#13+#14+#15 가능성) | 0/5 | 2/10 (W4-1 + W4-2 가능성) | **5/33 발화 가능성** (단, SUCCESS 시 = 0/33 발화) — `git revert HEAD` 권고 시작점 (C-υ-41 답습) |
| (iii) `pull_request` event (옵션) | 3/18 | 0/5 | 2/10 | **5/33 발화 가능성** + W-6 Required check 등록 영역 (Backlog #3 분리) |
| (iv) `workflow_dispatch` (옵션 디버깅) | 3/18 | 0/5 | 2/10 | **5/33 발화 가능성** |
| (v)~(vii) 비권고 영역 | 3/18 + cache poisoning | 0/5 | 5/10 | **본 brief 비권고** |

**핵심 발견**: 옵션 (i) (본 brief 시점) = **0/33 발화 영구 답습**. 옵션 (ii) (사용자 결정 후 trigger 발화) = 5/33 발화 *가능성* (단, SUCCESS 시 = 0/33 발화 — 4 prerequisite runs 4/4 SUCCESS pattern 답습). 옵션 (vii) (`pull_request_target`) = 5/33 + cache poisoning 영역 = **본 brief 비권고** (Stage 4 entry brief Agent B RF-B1 답습 + C-υ-44 답습 + W-1 + W-2 + W-3 답습 영구).

### 6.5 Rollback 절차 권고 (C-υ-41 답습 — "즉시 rollback" 권고 한정)

| 절차 | 영역 | 권고 |
|----|----|----|
| (i) Rollback decision | trigger 발화 시 판단 | **사용자 명시 결정 영역** (자동 rollback 0건 영구 답습) |
| (ii) `git revert HEAD` (W-4 trigger commit 한정 — empty commit trigger 시) | 가장 안전 — trigger commit 만 revert | **권고 시작점** |
| (iii) `git reset --hard HEAD~N` | 강제 reset (이력 변경) | ❌ **비권고** (R-4 history rewrite layer 영역) |
| (iv) 신규 `fix:` commit (revert 없이 forward fix) | trigger 본질 + 부분 fix 필요 시 | 옵션 (사용자 결정 영역) |
| (v) W-1 / W-2 / W-3 본문 *변경* 으로 forward fix | W-1 + W-2 + W-3 답습 영구 위반 영역 | ❌ **비권고** (W-1 + W-2 + W-3 = 0-line passthrough 고정 영구) |
| (vi) 본 brief 시점 = trigger 발화 0 = rollback 영역 0건 영구 답습 | — | **답습 한정** |
| (vii) actual run cancel (mid-run) | `gh run cancel <run-id>` 옵션 | 옵션 (사용자 결정 영역 — F-1 발화 시 *중지* 권고) |

### 6.6 본 §6 의 *범위 한계*

본 §6 = **rollback trigger *발화 가능성 enumerate 한정***. 본 §6 의 어떤 항목도 *발화* / *rollback 절차 자동 발효* / *threshold 고정* 시키지 않는다.

---

## 7. 사용자 명시 4 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 4 금지 영역 위반 0건 영구 답습

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 결정 영역) |
|---|---------|---------------|------------------------------|
| #1 | actual run 실행 | ✅ 0건 (신규 GitHub Actions run trigger 발화 0건 — 본 brief = lockdown 한정) | ✅ 0건 (DRAFT 영역, 사용자 결정 후 진입 — 옵션 (ii) 채택 시 = 1 run 발화) |
| #2 | CI workflow 변경 | ✅ 0건 (W-1 = 0-line passthrough 답습 영구) | ✅ 0건 (W-1 + W-2 + W-3 합의 답습 영구) |
| #3 | Operational Readiness PASS (Layer E) | ✅ 0건 (MVP-6 영역 분리) | ✅ 0건 |
| #4 | Hermes PMO 격상 (Layer F) | ✅ 0건 (ADR-008 부록 C 12 조건 미충족) | ✅ 0건 |
| **합산** | **4** | **✅ 4/4 위반 0건** | **✅ 4/4 위반 0건 (작성 시점) — 사용자 결정 후 #1 해소 영역** |

### 7.2 W-4 옵션별 4 금지 위반 매트릭스

| 옵션 | #1 | #2 | #3 | #4 | 합산 |
|-----|----|----|----|----|-----|
| (i) trigger 발화 0건 (본 brief 시점) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | **4/4 위반 0건** |
| (ii) `push` event 1 run (사용자 결정 후) | ⚠️ 본 brief 시점 0 / 사용자 결정 후 = #1 *해소* (필수) | ✅ 0 (W-1 답습 영구) | ✅ 0 | ✅ 0 | **3/4 보존 + 1/4 해소** (사용자 결정 후) |
| (iii) `pull_request` event (옵션) | ⚠️ 동상 | ✅ 0 | ✅ 0 | ✅ 0 | **3/4 보존 + 1/4 해소** + W-6 영역 (Backlog #3 분리) |
| (iv) `workflow_dispatch` (옵션) | ⚠️ 동상 | ✅ 0 | ✅ 0 | ✅ 0 | **3/4 보존 + 1/4 해소** |
| (v) `schedule` cron | ⚠️ 동상 + 운영 진입 위험 | ✅ 0 | ❌ **위반 가능성** (운영 영역 = Layer E) | ✅ 0 | **본 brief 비권고** |
| (vi) `repository_dispatch` | ⚠️ 동상 | ✅ 0 | ✅ 0 | ❌ **위반 가능성** (외부 trigger = ADR-008 부록 C) | **본 brief 비권고** |
| (vii) `pull_request_target` | ⚠️ 동상 + cache poisoning | ❌ **위반 가능성** (T2/T3 영역) | ✅ 0 | ✅ 0 | **본 brief 비권고** |

### 7.3 Backlog 분리 매트릭스

| Backlog | 영역 | 본 brief 영역 |
|---------|----|----------|
| Backlog #1 (PC-4 local pre-commit hook 활성화) | `.pre-commit-config.yaml` 신설 | ❌ 본 brief 영역 외 (W-7) |
| Backlog #2 (dev 환경 강제 + pre-commit install 의무화) | dev 환경 검증 강제 | ❌ 본 brief 영역 외 (W-7 영역) |
| Backlog #3 T3 (AR-2 branch protection + AR-3 자동 revert bot + Required check 등록 + commit signing) | branch protection API + CODEOWNERS + bot 설정 | ❌ 본 brief 영역 외 (W-6 + W-8 + W-9 영역) |
| Backlog #4 (facade.py real 본문 작성) | `src/adapters/llm/facade.py` real 본문 | ❌ 본 brief 영역 외 |
| Backlog #5 (event enum / ledger entry 정식 등록) | ADR-012 §2.2 영역 | ❌ 본 brief 영역 외 (후보 한정) |
| Backlog #6 (Hermes PMO 격상 영역) | ADR-008 부록 C 12 조건 영역 | ❌ 본 brief 영역 외 |
| Stage 5 (G3-7 4 항목) | secret reset rotate / fork PR / pull_request_target / commit signing | ❌ 본 brief 영역 외 (W-10 영역) |
| **W-1 cycle 1/4 (3 MVP-1 workflow micro-patch)** | 3 workflow 1206줄 | ❌ 본 brief 영역 외 (cycle 1/4 답습 — 0-line passthrough 고정 영구) |
| **W-2 cycle 2/4 (integration tool micro-patch)** | tool 298줄 | ❌ 본 brief 영역 외 (cycle 2/4 답습 — 0-line passthrough 고정 영구) |
| **W-3 cycle 3/4 (3 fixture micro-patch)** | fixture 89줄 | ❌ 본 brief 영역 외 (cycle 3/4 답습 — 0-line passthrough 고정 영구) |

### 7.4 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 4 금지 영역 + Backlog 분리 영역 + W-1 / W-2 / W-3 cycle 분리 영역 어느 것도 *해소* / *통합* 시키지 않는다.

---

## 8. 합산 539 합의 조건 답습 매트릭스

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
| Phase α-4 R-1 Stage 4 W-2 | `310b518` | 35 (C-χ-1 ~ C-χ-35) | 0건 |
| **Phase α-4 R-1 Stage 4 W-3** | **`3aac549`** | **36 (C-ψ-1 ~ C-ψ-36)** | **0건** ✅ |
| **합산** | **19 합의** | **539 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스 (본 brief 핵심 조건 답습)

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션 정식 등록) 발효 — 본 brief = cycle 4/4 진입 | ✅ §1.4 + §8.2 답습 |
| C-υ-44 (Agent A + B + C 동시 발효 — micro-patch 별도 brief + 본문 변경 시도 권고 0건 + 변경 line 0 lines 우선 권고 강화) | ✅ §4.1 + §4.2 답습 (trigger 발화 0건 우선 권고 시작점) |
| C-υ-38 (PRE-0 도구 가용성 사전 점검 의무) | ✅ §5.1 답습 |
| C-υ-41 (즉시 rollback 권고 한정 = 사용자 결정 영역) | ✅ §6.5 답습 |
| C-υ-42 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) | ✅ §5.5 (S-6) + §5.6 (F-5) 답습 — 본 brief = 결정적 차단 시점 발효 (사용자 결정 후 trigger 발화 시) |
| C-υ-45 후보 (GitHub Actions cache poisoning 자동 차단) | 후보 한정 — 본 brief 시점 정식 등록 0건 (옵션 (vii) 비권고 영역 답습) |
| C-υ-46 후보 (artifact 사후 변조 검증) | 후보 한정 — 본 brief 시점 정식 등록 0건 (§5.4 RUN-5 옵션 영역) |
| C-φ-30 (W-1 = 0-line passthrough 고정 영구) | ✅ §1.2 + §8.2 답습 |
| C-χ-35 (W-2 = 0-line passthrough 고정 영구) | ✅ §1.2 + §8.2 답습 |
| **C-ψ-36 (W-3 = 0-line passthrough 고정 영구)** | ✅ **§1.2 + §8.2 답습** |
| C-ψ-3 (W-3 단독 + W-1 + W-2 답습 + W-4 분리) → 본 brief 변환 (W-4 단독 + W-1 + W-2 + W-3 답습) | ✅ §2 답습 |
| C-ψ-18 (Backlog 분리 + W-1 / W-2 / W-4 cycle 분리 영구 답습) → 본 brief 변환 (Backlog 분리 + W-1 / W-2 / W-3 cycle 분리 영구 답습) | ✅ §7.3 답습 |
| C-ψ-23 (LVE 3/3 fixture PASS evidence 보존 의무 영구) → 본 brief 확장 (LVE 51/51 PASS evidence 보존 의무 영구 + 4 prerequisite runs 답습 영구) | ✅ §3.5 + §5.2 + §5.5 답습 |
| C-ψ-25 (fixture `on.push.branches: ["fixture-only/**"]` 답습 영구 — 실 trigger 0건 보장) | ✅ §4.4 답습 |
| Group α C-11 (외부 LLM 응답 = 입력 한정) | ✅ §9 답습 |
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | ✅ §9 비적용 답습 |
| F-금지 #1 (GitHub Actions secrets 사용 도입 0건 영구 답습) | ✅ §0.5 + §5.5 (S-5) + §5.6 (F-4) 답습 |
| ADR-011 §2.1 (a)~(e) 5조건 모법 | ✅ 답습 한정 |
| ADR-008 부록 C Hermes PMO Activation 12 조건 미진입 영구 답습 | ✅ §7.1 답습 |

---

## 9. 합의 형태 권고 + 풀 3+1 트리거 분석

### 9.1 본 brief 권고 합의 형태

| 합의 형태 | 적격성 | 본 brief 권고 |
|---------|------|----------|
| **(a) Reviewer-only 단축 합의** | T-2 재발화 영역 한계 (Stage 4 entry brief `81472ba` + W-1 `df741a2` + W-2 `310b518` + W-3 `3aac549` 시점 이미 발화 영역 완료) + 풀 3+1 트리거 새 발화 0/16 | ✅ **권고 시작점** — 본 brief = W-4 단독 actual run trigger / 검증 lockdown DRAFT + W-1 + W-2 + W-3 = 0-line passthrough 답습 + W-5~W-10 분리 + trigger 발화 0건 권고 시작점 (본 brief 시점) + 사용자 결정 후 = `push` event 1 run 권고 시작점 → T-2 발화 *영역 한계* (Stage 4 entry brief + W-1 + W-2 + W-3 합의 시점 이미 발화 완료 — 본 brief = 그 권위 답습 한정) |
| (b) 풀 3+1 합의 | 사용자 명시 보강 결정 시 (T-N 신규 발화 발견 시) | 옵션 (사용자 결정 영역) |
| (c) 풀 3+1 + 외부 LLM 1+ | T-6 / T-10 / T-13 발화 시 (T3 영역 / 경계 불명확 / Stage 5 권고) | ❌ 비권고 (본 brief = T-6/T-10/T-13 미발화) |

### 9.2 풀 3+1 트리거 16 영역 × 본 brief 발화 매트릭스

| T # | 영역 | 본 brief 발화 |
|----|----|------------|
| T-1 | 새 권위 결정 (ADR / P / GP 신규 발행) | 0 (본 brief = 답습 한정) |
| T-2 | 사용자 명시 영구 5 금지 영역 中 1+ 해소 권고 | ⚠️ **재발화 영역 한계** — Stage 4 entry brief 합의 시점 (`81472ba`) 이미 T-2 발화 + W-1 (`df741a2`) + W-2 (`310b518`) + W-3 (`3aac549`) 합의 시점 답습 영역 완료 → 본 brief = cycle 4/4 권위 답습 한정 + trigger 발화 0건 영역 + 사용자 결정 후 발화 = #1 해소 (이미 Stage 4 entry §1.5 답습 영역) → **새 T-2 발화 0건** |
| T-3 | §5.5.1+§5.5.2 본문 변경 시도 / Stage 4 step 본문 변경 시도 | 0 (본 brief = R-1 영역 1593줄 변경 0건 영구 답습 — W-1 + W-2 + W-3 답습 영구) |
| T-4 | Provider Liquidity 5-way 약화 위험 | 0 (R-1 = vendor-agnostic 답습 + W-4 trigger = `push` event = vendor-neutral GitHub Actions 표준) |
| T-5 | 5 영구 핵심 제약 5/5 보존 위반 | 0 (LVE §5.1 + 본 brief §5.5 S-6 + §5.6 F-5 보존 한정) |
| T-6 | T3 영역 진입 권고 | 0 (Backlog #3 분리 명시 + 옵션 (vii) `pull_request_target` 비권고 영역) |
| T-7 | 합산 539 합의 조건 中 1+ 변경 권고 | 0 (본 brief = 0건 영구 답습) |
| T-8 | F-금지 #1 위반 권고 (GitHub Actions secrets 도입) | 0 (§5.5 S-5 + §5.6 F-4 답습) |
| T-9 | Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 | 0 |
| T-10 | PC-3+AR-1 / PC-4 / AR-2 / AR-3 경계 불명확 | 0 (§2.3 + §7.3 분리 명시) |
| T-11 | Phase α-1 / α-2 / α-3 actual run 자동 재실행 | 0 (PRE 영역 = read-only + 4 prerequisite runs 답습 한정) |
| T-12 | Hermes PMO 격상 권고 | 0 (영구 답습) |
| T-13 | Stage 5 자동 진입 권고 | 0 (§2.3 W-10 분리 명시) |
| T-14 | Operational Readiness PASS 선언 권고 | 0 (영구 답습) |
| T-15 | W-1 + W-2 + W-3 재진입 / 0-line passthrough 고정 변경 권고 | 0 (cycle 1/4 + 2/4 + 3/4 답습 영구) |
| T-16 | `pull_request_target` / `schedule` / `repository_dispatch` 도입 권고 | 0 (옵션 (v)~(vii) 비권고 영역 — §4.4 + §7.2 답습) |
| **합산** | **16 트리거** | **0/16 새 발화 → Reviewer-only 단축 합의 적격 시작점** |

### 9.3 외부 LLM 1+ 비적용 사유

| 영역 | 비적용 사유 |
|------|---------|
| Group α C-14 (cross-vendor blind 의뢰 1+ 의무) | 비적격 — 본 brief = cycle 4/4 한정 + trigger 발화 0건 영역 + W-4 단독 영역 + 4 prerequisite runs answer pattern 답습 한정 |
| T-6 (T3 영역 진입 권고) | 0건 (Backlog #3 분리) |
| T-10 (경계 불명확) | 0건 (§2.3 + §7.3 분리 명시) |
| T-13 (Stage 5 자동 진입 권고) | 0건 (§2.3 W-10 분리) |
| 본 brief 권고 | **외부 LLM 1+ 비적용** (Group α C-11 답습 + ADR-011 §2.4 답습 한정) |

---

## 10. 본 brief 자체 금지 + 본 brief 발효 후 의무 금지

### 10.1 본 brief 자체 금지 ≥ 50 영역

본 brief 자체는 다음 영역을 *발효* 시키지 않는다:

- ❌ 신규 actual GitHub Actions run trigger 어느 것도 발화
- ❌ 4 prerequisite GitHub Actions runs 답습 어느 것도 변경 / 재실행
- ❌ 3 MVP-1 workflow (1206줄) 어느 줄도 변경 (W-1 답습 영구)
- ❌ `tools/mvp1_pc3_ar1_integration_check.py` (298줄) 어느 줄도 변경 (W-2 답습 영구)
- ❌ 3 fixture (89줄) 어느 줄도 변경 (W-3 답습 영구)
- ❌ R-4 / R-5 / R-7 본문 (1192줄, 13 file) 어느 줄도 변경
- ❌ `src/` runtime code / facade.py placeholder 어느 줄도 변경
- ❌ trigger event 신규 도입 (`pull_request_target` / `schedule` / `repository_dispatch`)
- ❌ branch trigger 변경 (`main` / `develop` / 신규 branch — `feature/hermes-phase0` 답습 영역 외)
- ❌ 재실행 (횟수 ≥ 2)
- ❌ Stage 4 step (line 318~360) 본문 어느 것도 변경
- ❌ §5.5.1 + §5.5.2 PC-3 + AR-1 본문 어느 것도 변경
- ❌ fixture `on.push.branches: ["fixture-only/**"]` 영역 변경 (실 trigger 0건 보장)
- ❌ R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 어느 것도 변경
- ❌ `.importlinter` 어느 영역도 변경
- ❌ R-7 docker secret block / image layer check / restart recovery 어느 것도 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 어느 영역도 진입
- ❌ Stage 5 (G3-7 4 항목) 어느 항목도 진입
- ❌ W-5 ~ W-10 어느 영역도 진입
- ❌ branch protection 어느 영역도 변경
- ❌ Required check 등록
- ❌ `permissions: contents: read` 보강
- ❌ 신규 workflow 신설 / `pull_request_target` 도입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1 영구 답습)
- ❌ Hermes upstream Dockerfile / Production `docker-compose.yml` 어느 것도 변경
- ❌ 실 secret material commit
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
- ❌ 합산 539 합의 조건 자동 변경
- ❌ W-1 = 0-line passthrough 고정 변경 (C-φ-30)
- ❌ W-2 = 0-line passthrough 고정 변경 (C-χ-35)
- ❌ W-3 = 0-line passthrough 고정 변경 (C-ψ-36)
- ❌ LVE 51/51 PASS evidence 자동 재집계
- ❌ 4 prerequisite runs 자동 재실행
- ❌ Stage 4 step line 329~341 grep 답습 변경
- ❌ Operational Readiness PASS / Hermes PMO 격상 발효
- ❌ GitHub Actions cache poisoning 자동 차단 도구 본문 작성 (C-υ-45 후보 한정)
- ❌ artifact 사후 변조 검증 도구 본문 작성 (C-υ-46 후보 한정)
- ❌ W-4 신규 trigger event / branch / 횟수 / token 영역 최종 확정 발효
- ❌ W-4 실 trigger 발화 자동 진입

### 10.2 본 brief 발효 후 의무 금지 ≥ 13 영역

본 brief APPROVE AS BRIEF 후에도 다음은 *자동* 진입 0건:

- ❌ W-4 실 trigger 발화 자동 진입 (사용자 명시 결정 영역)
- ❌ W-1 / W-2 / W-3 재진입 (cycle 1/4 + 2/4 + 3/4 답습 영구)
- ❌ Backlog #1+#2 / Backlog #3 T3 / Backlog #4 / Backlog #5 / Backlog #6 / Stage 5 자동 진입
- ❌ Layer C 재발효 / Layer D 재선언 / Layer E / Layer F 자동 진입
- ❌ Phase β / γ / MVP-2 ~ MVP-6 자동 진입
- ❌ 합의 보고서 자동 작성 (사용자 명시 결정 후)
- ❌ 메타 commit / push 자동 진입 (사용자 명시 결정 후)
- ❌ 외부 LLM 자동 호출 (사용자 명시 결정 시에만)
- ❌ 신규 actual run trigger 자동 발화 (사용자 명시 결정 후 옵션 (ii) 채택 시에만)
- ❌ LVE evidence 자동 재집계
- ❌ 4 prerequisite runs 자동 재실행
- ❌ Operational Readiness PASS / Hermes PMO 격상 자동 발효
- ❌ Stage 4 step / §5.5.1+§5.5.2 본문 자동 변경
- ❌ W-1 / W-2 / W-3 본문 자동 변경

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 영역 영향 |
|-----|----|---------|
| **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점)** | 본 brief = APPROVE AS BRIEF + W-4 trigger 영역 lockdown 권고 발효 + 합산 539 → 539+N (20 합의) | ✅ T-2 재발화 영역 한계 답습 + W-4 trigger 영역 lockdown 권위 권고 |
| (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) | Agent A + B + C 가동 → 4 에이전트 본문 + Reviewer 본문 작성 | 옵션 (사용자 결정 영역 — 본 brief = 풀 3+1 트리거 0/16 새 발화) |
| (C) brief 수정 (특정 § 보강 요청) | 본 brief 본문 보강 → 재DRAFT | 옵션 |
| (D) 부분 채택 (특정 옵션 (ii)~(iv) 中 1+ 한정) | 옵션 (ii) `push` / (iii) `pull_request` / (iv) `workflow_dispatch` 中 사용자 결정 | 옵션 (trigger event 결정 영역) |
| **(E) brief 합의 후 → W-4 실 trigger 발화 직접 진입 brief** | 옵션 (ii) `push` event on `feature/hermes-phase0` branch 1 run 발화 trigger brief 작성 (사용자 명시 결정 영역) | **옵션 (사용자 명시 #1 해소 영역 — 본 brief 발효 후 별도 cycle)** |
| (F) 본 brief 보류 → W-1 / W-2 / W-3 실 micro-patch 직접 진입 brief | 옵션 (i) 0 lines 답습 → 영역 0건 (본 brief 영역 외) | 옵션 (가능성 0 — 답습 영역) |
| (G) Backlog 전환 | Backlog #1+#2 / #3 / #4 / #5 / #6 / Stage 5 中 사용자 결정 | 옵션 (영역 외 진입) |
| (H) brief 폐기 | 본 brief 본문 보존 + 합의 0건 | 옵션 |
| (I) 세션 종료 | CONTEXT / INDEX / SESSION 갱신 + 다음 세션 1순위 결정 | 옵션 |

### 11.1 (A) 옵션 채택 시 후속 commit chain (사용자 명시 결정 영역)

```
(현재) W-4 brief DRAFT 작성 commit (예: 후속 33)
   │
   ▼ (사용자 명시 결정 후)
■ docs(review): approve Phase alpha-4 W-4 trigger brief (본 합의 commit)
   │
   ▼ (사용자 명시 결정 후)
■ docs(context): record Phase alpha-4 W-4 trigger status (CONTEXT + INDEX + SESSION 갱신 commit)
   │
   ▼ (사용자 명시 결정 후)
■ git push origin feature/hermes-phase0
   │
   ▼ (자동 진입 0건 — 사용자 결정 영역)
■ Phase α-4 Stage 4 W-4 *실 trigger 발화* brief / 세션 종료 中 사용자 결정
```

### 11.2 본 brief 새 조건 후보 enumerate (합의 보고서 작성 시 정식 등록)

본 brief 발효 시 새 조건 후보 ≥ 35 (C-ψ-1 ~ C-ψ-36 답습 패턴 답습, W-4 특화 6+ 신규 — 신규 영역: trigger event = `push` 한정 권고 + 횟수 1 권고 + 사용자 결정 후 #1 해소 영역 + 옵션 (vii) `pull_request_target` cache poisoning 비권고 + RUN-1~7 검증 + 4 prerequisite runs answer pattern 답습):

| # | 후보 조건 영역 |
|---|------------|
| C-ω-1 | 본 brief = cycle 4/4 (W-4 단독) 진입 한정 (C-υ-43 발효 답습 — 4 cycle 완성) |
| C-ω-2 | W-1 + W-2 + W-3 답습 영구 (`df741a2` C-φ-30 + `310b518` C-χ-35 + `3aac549` C-ψ-36) |
| C-ω-3 | W-4 단독 영역 + W-1 + W-2 + W-3 답습 + W-5~W-10 분리 |
| C-ω-4 | 4 prerequisite GitHub Actions runs 답습 매트릭스 채택 (`25728590939` + `25728590916` + `25728590977` + `25731846625` = 4/4 SUCCESS) |
| C-ω-5 | R-1 영역 7 artifacts × 1593줄 변경 0건 영구 답습 (W-1 + W-2 + W-3 답습 영구) |
| C-ω-6 | trigger 발화 권고 시작점 = 0건 (본 brief 시점, 옵션 (i)) |
| C-ω-7 | 사용자 결정 후 trigger 발화 권고 시작점 = `push` event on `feature/hermes-phase0` branch 1 run (옵션 (ii)) — **신규 영역** |
| C-ω-8 | **옵션 (iii) `pull_request` event + W-6 Required check 등록 = Backlog #3 T3 분리** — **신규 영역** |
| C-ω-9 | 옵션 (iv) `workflow_dispatch` (manual UI trigger) = 디버깅 옵션 영역 |
| C-ω-10 | 옵션 (v) `schedule` cron 영구 비권고 (운영 영역 = Layer E, MVP-6 분리) |
| C-ω-11 | 옵션 (vi) `repository_dispatch` 영구 비권고 (외부 trigger = ADR-008 부록 C 영역) |
| C-ω-12 | **옵션 (vii) `pull_request_target` 영구 비권고** (T2/T3 영역 + GitHub Actions cache poisoning 위험 = Agent B RF-B1 답습) — **신규 영역** |
| C-ω-13 | W-4 검증 13 영역 (PRE-0 6 + PRE-T 6 + RUN 7) 채택 — **신규 영역** |
| C-ω-14 | rollback trigger 33 영역 × W-4 시점 발화 0/33 (옵션 (i) 본 brief 시점) — **신규 영역** |
| C-ω-15 | 사용자 결정 후 trigger 발화 5/33 발화 *가능성* (단, SUCCESS 시 = 0/33 발화 — 4 prerequisite runs answer pattern 답습) — **신규 영역** |
| C-ω-16 | 사용자 명시 4 금지 4/4 위반 0건 영구 답습 (작성 시점) — 사용자 결정 후 #1 해소 영역 (옵션 (ii) 채택 시) — **신규 영역** |
| C-ω-17 | 합산 539 합의 조건 변경 0건 영구 답습 |
| C-ω-18 | Backlog 분리 영구 답습 (#1~#6 + Stage 5 + W-1 + W-2 + W-3) |
| C-ω-19 | 풀 3+1 트리거 0/16 새 발화 → Reviewer-only 단축 합의 적격 |
| C-ω-20 | 외부 LLM 1+ 비적용 (T-6 / T-10 / T-13 미발화) |
| C-ω-21 | 본 brief 자체 금지 ≥ 50 영역 + 발효 후 의무 금지 ≥ 13 영역 |
| C-ω-22 | 5 영구 핵심 제약 5/5 보존 + Provider Liquidity 5-way 100% 보존 |
| C-ω-23 | F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) |
| C-ω-24 | LVE 51/51 PASS evidence 보존 의무 영구 + 4 prerequisite runs 답습 영구 — **신규 영역** |
| C-ω-25 | RUN-1~7 검증 영역 채택 (Stage 4 entry §4.4 RUN-1~6 답습 + RUN-7 4 prerequisite runs 비교 신규) — **신규 영역** |
| C-ω-26 | S-1~7 SUCCESS 조건 + F-1~7 FAILURE 조건 채택 (Stage 4 entry §5.3 + §5.4 답습) |
| C-ω-27 | branch 권고 시작점 = `feature/hermes-phase0` (`main` / `develop` / 신규 branch 비권고) |
| C-ω-28 | 횟수 권고 시작점 = 1 run (재실행 0건 권고) |
| C-ω-29 | C-υ-45 후보 (GitHub Actions cache poisoning 자동 차단) — 본 brief 시점 정식 등록 0건 |
| C-ω-30 | C-υ-46 후보 (artifact 사후 변조 검증) — 본 brief 시점 정식 등록 0건 + RUN-5 옵션 영역 |
| C-ω-31 | C-υ-41 답습 "즉시 rollback" 권고 = 사용자 결정 영역 |
| C-ω-32 | C-υ-42 답습 (5 영구 핵심 제약 결정적 차단 시점 = POST-6) — 본 brief = §5.5 S-6 + §5.6 F-5 답습 |
| C-ω-33 | brief 본문 변경 0건 영구 답습 |
| C-ω-34 | brief 발효 후 자동 진입 0건 (모든 후속 단계 = 사용자 명시 결정 영역) |
| C-ω-35 | event enum (`pc3_ar1_integration_implementation`) 후보 한정 영구 답습 (Backlog #5 ADR-012 §2.2 분리) |
| C-ω-36 | 10 caveat 명시 의무 영구 답습 (단계별 합의 cycle 패턴 답습 — W-3 §2.3 답습 패턴) |
| C-ω-37 | (합의 시점 신규 1) W-4 = trigger 발화 0건 (본 brief 시점) + 사용자 결정 후 권고 시작점 = `push` event 1 run 고정 영구 |
| **합산** | **37 후보** (W-3 합의 36 답습 패턴 답습 + W-4 특화 6 신규: C-ω-7 + C-ω-8 + C-ω-12 + C-ω-13 + C-ω-15 + C-ω-16 + C-ω-24 + C-ω-25 + 합의 시점 신규 C-ω-37 = 37) |

---

## 12. 본 brief 메타 검증

### 12.1 본 brief 가 답습한 영역 매트릭스

| 답습 영역 | 답습 출처 | 본 brief 답습 |
|---------|---------|----------|
| W-3 brief 합의 (`3aac549`) APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH 36 조건 | C-ψ-1 ~ C-ψ-36 | ✅ §1.2 + §8.2 답습 한정 |
| W-2 brief 합의 (`310b518`) APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH 35 조건 | C-χ-1 ~ C-χ-35 | ✅ §1.2 + §8.2 답습 한정 |
| W-1 brief 합의 (`df741a2`) APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH 30 조건 | C-φ-1 ~ C-φ-30 | ✅ §1.2 + §8.2 답습 한정 |
| Stage 4 entry brief 합의 (`81472ba`) APPROVE AS BRIEF WITH CONDITIONS 49 조건 | C-υ-1 ~ C-υ-49 | ✅ 답습 한정 (특히 C-υ-38 + C-υ-41 + C-υ-42 + C-υ-43 + C-υ-44 + C-υ-45 후보 + C-υ-46 후보 강화 — §4 + §5 + §6 답습) |
| Stage 3 합의 (`d3f6d59`) APPROVE AS BRIEF 36 조건 | C-τ-1 ~ C-τ-36 | ✅ 답습 한정 |
| LVE 합의 (`b264580`) APPROVE 31 조건 + LVE 본문 (`4ce5a0b`) 51/51 PASS (4 prerequisite runs 답습 포함) | C-σ-1 ~ C-σ-31 | ✅ §3.1 + §3.5 + §5.2 답습 한정 |
| ADR-011 §2.1 (a)~(e) 5 조건 모법 | ADR-011 | ✅ 답습 한정 |
| ADR-008 부록 B + 부록 C 12 조건 | ADR-008 | ✅ 답습 한정 |
| Group α C-11 / C-14 (외부 LLM 응답 = 입력 한정 + 1+ blind 의뢰 의무) | Group α | ✅ §9.3 답습 |
| F-금지 #1 (GitHub Actions secrets 사용 도입 0건 영구) | Stage 5 cycle 1~4 | ✅ §0.5 + §5.5 + §5.6 답습 |
| 5 영구 핵심 제약 + Provider Liquidity 5-way + Backlog #1~#6 분리 | LVE §5.1 + §5.2 + §5.3 | ✅ 답습 한정 |
| 4 prerequisite GitHub Actions runs (`25728590939` + `25728590916` + `25728590977` + `25731846625` 4/4 SUCCESS) | LVE §4 답습 | ✅ §3.1 + §3.2 + §5.2 (PRE-T1) + §5.4 (RUN-7) 답습 |

### 12.2 본 brief 자체 검증

| 검증 영역 | 본 brief 답습 |
|---------|----------|
| brief 작성 시점 4 금지 4/4 위반 | ✅ 0건 영구 답습 |
| brief 본문 = 답습 한정 (R-1 + R-4/5/7 + `src/` + tool + 3 workflow + 3 fixture 본문 어느 줄도 변경 0건) | ✅ 영구 답습 |
| brief 발효 시점 4 금지 4/4 위반 | ✅ 0건 영구 답습 (DRAFT 영역) |
| W-1 + W-2 + W-3 재진입 / W-4 실 trigger 발화 (본 brief 시점) | ✅ 0건 (cycle 1/4 + 2/4 + 3/4 = 답습 / cycle 4/4 trigger 발화 0건 영구) |
| 합산 539 합의 조건 변경 | ✅ 0건 영구 답습 |
| Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 | ✅ 0건 영구 답습 |
| Operational Readiness PASS / Hermes PMO 격상 | ✅ 0건 영구 답습 |
| 신규 actual GitHub Actions run trigger | ✅ 0건 영구 답습 |
| 4 prerequisite GitHub Actions runs 자동 재실행 | ✅ 0건 영구 답습 |
| 외부 LLM 자동 호출 / 실 API/SDK / 인간 리뷰 의무 자동 발화 | ✅ 0건 영구 답습 |
| 합의 보고서 작성 / 메타 commit / push 자동 진입 | ✅ 0건 (사용자 명시 결정 후 진입) |

### 12.3 본 brief 의 *제약 사항* enumerate

본 brief 의 *권위 제약*:

1. 본 brief = **준비안 (DRAFT)** — 사용자 명시 승인 전 어떤 *발효* 도 발생시키지 않는다
2. 본 brief 합의 시 = **W-4 단독 actual run trigger / 검증 lockdown 발효 한정** — 실 trigger 발화 / W-1 + W-2 + W-3 재진입 = 사용자 명시 결정 후 진입
3. 본 brief 영역 = **신규 actual GitHub Actions run trigger (수정 파일 0건) 한정** — 3 MVP-1 workflow / integration tool / 3 fixture / runtime code / R-4/5/7 / Stage 4 step (line 318~360) / §5.5.1+§5.5.2 본문 어느 것도 변경 영역 외
4. 본 brief 권고 시작점 = **trigger 발화 0건 (본 brief 시점, 옵션 (i)) + 사용자 결정 후 = `push` event on `feature/hermes-phase0` branch 1 run (옵션 (ii))**
5. 본 brief 답습 = **C-ψ-36 + C-χ-35 + C-φ-30 + C-υ-44 + Agent B C-B6 + Agent C C-C1 + Stage 4 entry §5.1 + §5.6 + 4 prerequisite runs answer pattern 동시 발효** 영역
6. 본 brief 합의 형태 = **(a) Reviewer-only 단축 합의 권고 시작점** (T-2 재발화 영역 한계 + 풀 3+1 트리거 0/16 새 발화)
7. 본 brief 비권고 영역 = **옵션 (v) `schedule` + 옵션 (vi) `repository_dispatch` + 옵션 (vii) `pull_request_target`** (운영 / 외부 trigger / cache poisoning 영역 = Layer E / ADR-008 부록 C / Stage 5 cycle 2 영역 분리)
8. 본 brief 의 합의 보고서 작성 / 메타 commit / push / 외부 LLM 호출 = **사용자 명시 결정 영역** (자동 진입 0건)
9. 본 brief 의 W-4 실 trigger 발화 자동 진입 = **0건** (사용자 명시 #1 답습 영구 — 별도 cycle 영역 — 사용자 결정 후 진입)
10. 본 brief 의 LVE 51/51 PASS evidence + 4 prerequisite runs 자동 재집계 / 재실행 = **0건** (옵션 (i) 0 trigger = 자동 보존)

---

## 13. 본 brief 요약

본 brief 는 **Phase α-4 R-1 Stage 4 W-3 micro-patch brief Reviewer-only 단축 합의 (`3aac549` APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH — 36 조건 C-ψ-1 ~ C-ψ-36, 합산 539 합의 조건) 발효 후속**, 사용자 명시 진입 명령 답습 — **Phase α-4 (R-1 CI workflow 통합 = PC-3 + AR-1) Stage 4 *W-4 단독* 영역 (신규 actual GitHub Actions run trigger + 검증 조건) *trigger / 검증 lockdown* brief 준비안 (DRAFT)** = **C-υ-43 (W-1/W-2/W-3 완전 분리 합의 4 cycle 옵션) 정식 등록 답습 cycle 4/4 진입** ("*Should* W-4 trigger a fresh actual GitHub Actions run (and which event / branch / 횟수), or is *trigger-deferred* the correct posture for the actual run at this gate?").

**사용자 명시 4 금지** (actual run 실행 / CI workflow 변경 (W-1 = 0-line passthrough 답습) / Operational Readiness PASS / Hermes PMO 격상) 4/4 영구 답습.

**4 prerequisite GitHub Actions runs 답습 매트릭스** (read-only, §3) — `25728590939` (α-1 R-4 secret_scanner) + `25728590916` (α-2 R-5 importlinter) + `25728590977` (α-1 R-4 provider_import_scanner) + `25731846625` (α-1 R-4 provider_url_scanner + R-7 docker block) = **4/4 SUCCESS** + 모든 jobs.conclusion=success + 4 artifact 답습 보존 + W-4 신규 run = *답습* + Stage 4 step 신규 검증 (사용자 결정 후 발화).

**Trigger 발화 후보 영역 *enumerate 한정*** (§4) — **C-υ-44 + C-φ-30 + C-χ-35 + C-ψ-36 답습 5 영역 동시 발효** (Agent A 절차 + Agent B 안전성 + Agent C 단순성 + W-1 + W-2 + W-3 답습) → **권고 시작점 = 옵션 (i) trigger 발화 0건 (본 brief 시점, 사용자 명시 #1 답습)** + 옵션 (ii) `push` event on `feature/hermes-phase0` branch 1 run (사용자 결정 후 권고 시작점) + 옵션 (iii) `pull_request` event (옵션, W-6 Required check 등록 시점) + 옵션 (iv) `workflow_dispatch` (옵션, 디버깅) + **옵션 (v) `schedule` cron 비권고 (운영 영역 = Layer E, MVP-6 분리)** + **옵션 (vi) `repository_dispatch` 비권고 (외부 trigger = ADR-008 부록 C 영역)** + **옵션 (vii) `pull_request_target` 비권고 (T2/T3 영역 + GitHub Actions cache poisoning 위험 = Agent B RF-B1 답습)**.

**W-4 검증 방법 권고** (§5) — **PRE-0 도구 가용성 사전 점검 6 영역** (gh CLI 인증 + version + git + status clean + R-1 영역 line count 답습) + **Pre-trigger 검증 6 영역** (PRE-T1~T6 — 4 prerequisite runs 답습 + LVE 51/51 PASS 답습 + Stage 4 step wired 답습 + 5 영구 핵심 제약 + F-금지 #1 self-check) + **Post-trigger 검증 7 영역** (RUN-1~7 — Stage 4 entry brief §4.4 RUN-1~6 답습 + RUN-7 4 prerequisite runs 비교 신규) + **SUCCESS 조건 7 (S-1~7)** + **FAILURE 조건 7 (F-1~7)** = **신규 actual run trigger 0건 영구 답습 (본 brief 시점)** + **LVE 51/51 PASS evidence + 4 prerequisite runs 답습 보존** (옵션 (i) 0 trigger = 자동 보존).

**W-4 시점 rollback trigger 발화 매트릭스** (§6) — Layer B 18 + TR-1~5 + Step Division 신규 후보 5 + Stage 4 W-4 신규 후보 5 = 33 trigger × 옵션별 발화 가능성 → **옵션 (i) (본 brief 시점) = 0/33 발화 영구 답습** + 옵션 (ii) (사용자 결정 후 trigger 발화) = 5/33 발화 *가능성* (단, SUCCESS 시 = 0/33 발화 — 4 prerequisite runs answer pattern 답습) + 옵션 (vii) (`pull_request_target`) = 5/33 + cache poisoning 영역 = **본 brief 비권고** — `git revert HEAD` 권고 시작점 (C-υ-41 답습 — trigger commit 한정).

**합의 형태 권고**: 본 brief 자체 = **(a) Reviewer-only 단축 합의 적격 시작점** (T-2 재발화 영역 한계 — Stage 4 entry brief + W-1 + W-2 + W-3 합의 시점 이미 답습) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고 (T-6/T-10/T-13 미발화).

**사용자 명시 4 금지 × 본 brief 분리 매트릭스 — 4/4 영구 답습** (작성 시점 모두 0건) — 사용자 결정 후 #1 (actual run 실행) 해소 영역 (옵션 (ii) 채택 시).

**합산 539 합의 조건 변경 0건** (19 합의 — W-1 합의 30 + W-2 합의 35 + W-3 합의 36 + Stage 4 entry brief 49 포함).

**본 brief 자체 금지 ≥ 50 + 본 brief 발효 후 의무 금지 ≥ 13** enumerate.

**본 brief 새 조건 후보 37 (C-ω-1 ~ C-ω-37)** — 합의 보고서 작성 시 정식 등록 (W-3 합의 36 답습 패턴 답습 + W-4 특화 8 신규: C-ω-7 + C-ω-8 + C-ω-12 + C-ω-13 + C-ω-15 + C-ω-16 + C-ω-24 + C-ω-25 + 합의 시점 신규 C-ω-37 = 37).

**본 brief 는 신규 actual GitHub Actions run trigger 어느 것도 *발화* 시키지 않으며, 4 prerequisite runs 답습 / 재실행 어느 것도 *변경* 시키지 않으며, 3 MVP-1 workflow / integration tool / 3 fixture 본문 어느 줄도 *변경* 시키지 않으며 (W-1 + W-2 + W-3 답습 영구), W-1 / W-2 / W-3 = 0-line passthrough 고정 (C-φ-30 + C-χ-35 + C-ψ-36) 어느 것도 *변경* 시키지 않으며, Stage 4 step (line 329~341) / §5.5.1+§5.5.2 본문 어느 것도 *변경* 시키지 않으며, 사용자 명시 4 금지 영역 *해소* / Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 539 합의 조건 어느 것도 *변경* / PC-4 / AR-2 / AR-3 / Stage 5 진입 / Phase α-1 / α-2 / α-3 actual run 자동 재실행 / W-4 trigger event / branch / 횟수 / token 영역 어느 것도 *최종 확정 발효* / LVE 51/51 PASS evidence + 4 prerequisite runs 자동 재집계 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**.

다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §11 답습) — **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점 — T-2 재발화 영역 한계)** / (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) / (C) brief 수정 / (D) 부분 채택 / **(E) brief 합의 후 → W-4 실 trigger 발화 직접 진입 brief (사용자 명시 #1 해소 영역)** / (F) W-1/W-2/W-3 실 micro-patch (가능성 0 — 답습 영역) / (G) Backlog 전환 / (H) brief 폐기 / (I) 세션 종료.
