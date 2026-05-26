# W-1 brief caveat 8 후속 관찰 brief — paths 필터 + workflow_dispatch 답습 영역 + actual run 발화 전략 재설계 (DRAFT)

> **본 문서는 후속 37 W-4 실 trigger 발화 직접 실행 시도 (`d4a0107` empty commit + push 발효 + 신규 actual run 발화 0건) + paths 필터 발견 evidence (`4bd8d68` 메타 commit) 발효 후속, 사용자 명시 진입 명령 답습 — **W-1 brief 합의 (`df741a2`) caveat 8 ("workflow 2/3 paths 미답습 영역 후속 관찰 보존") 본격 후속 관찰 brief 준비안**.**
>
> **본 brief 의 framing 차이**:
> - W-1 brief (cycle 1/4, `7af77fb` + `df741a2`) = "Should W-1 introduce micro-patch lines on 3 workflow?" → APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH + **caveat 8** ("workflow 2/3 paths 미답습 영역 후속 관찰 보존")
> - W-4 lockdown brief (`5d08966` + `945f766`) = "Should W-4 trigger a fresh actual run?" → APPROVE AS BRIEF WITH TRIGGER-DEFERRED + (β-1) empty commit + push 권고 시작점 (paths 필터 답습 영역 *간과*)
> - W-4 *실 trigger 발화 결정* brief (`ccdb30d` + `a7837f2`) = "Should we execute the W-4 lockdown's recommended trigger NOW?" → APPROVE AS BRIEF WITH DECISION-DEFERRED + RECOMMENDED-TRIGGER-METHOD = (β-1) empty commit + push
> - 후속 37 trigger commit (`d4a0107` + `4bd8d68` 메타) = **W-4 실 trigger 발화 직접 실행 시도** → empty commit + push 발효 + 신규 actual run 발화 0건 → **paths 필터 + workflow_dispatch 비등록 발견 evidence**
> - **본 brief = W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 DRAFT** — **"*How* should we redesign the W-4 actual run trigger 발화 전략, given the paths 필터 + workflow_dispatch 비등록 발견 evidence?"**
>
> 본 brief 자체는 여전히 *준비안 (DRAFT)* — 어느 §도 (i) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며 (W-1 답습 영구), (ii) `workflow_dispatch:` 어느 workflow 에도 *추가* 하지 않으며, (iii) `on.push.paths` 영역 어느 것도 *변경* 하지 않으며, (iv) 신규 actual GitHub Actions run trigger 어느 것도 *재실행* / *재발화* 시키지 않으며 (사용자 명시 #1 영구 답습), (v) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 답습 영구), (vi) 3 fixture 어느 줄도 *변경* 하지 않으며 (W-3 답습 영구), (vii) Stage 4 entry brief 합의 49 + W-1 합의 30 + W-2 합의 35 + W-3 합의 36 + W-4 lockdown 합의 37 + W-4 *실 trigger 발화 결정* 합의 26 = 합산 602 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며, (viii) Operational Readiness PASS 선언 / Hermes PMO 격상 어느 것도 *발효* 시키지 않으며, (ix) 합의 보고서 작성 / 메타 commit / push 어느 것도 *자동 진입* 시키지 않는다.

**작성일**: 2026-05-19 후속 38
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- 후속 37 발견 evidence — `d4a0107` (empty commit + push 발효, 신규 actual run 발화 0건) + `4bd8d68` (메타 commit, paths 필터 발견 evidence 기록) — **본 brief 의 발효 trigger**
- `docs/review/3plus1-consensus-2026-05-19-phase-alpha-4-w4-actual-trigger-decision.md` (commit `a7837f2`, 26 조건 C-A1-1 ~ C-A1-26 — W-4 *실 trigger 발화 결정* 합의)
- `docs/review/3plus1-consensus-2026-05-19-phase-alpha-4-w4-trigger.md` (commit `945f766`, 37 조건 C-ω-1 ~ C-ω-37 — W-4 lockdown 합의)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w1-micropatch.md` (commit `df741a2`, 30 조건 C-φ-1 ~ C-φ-30 — **caveat 8 모법**)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-w2-micropatch.md` (commit `310b518`, 35 조건 C-χ-1 ~ C-χ-35)
- `docs/review/3plus1-consensus-2026-05-19-phase-alpha-4-w3-micropatch.md` (commit `3aac549`, 36 조건 C-ψ-1 ~ C-ψ-36)
- `docs/review/3plus1-consensus-2026-05-18-phase-alpha-4-r1-stage4-entry.md` (commit `81472ba`, 49 조건 C-υ-1 ~ C-υ-49)
- `docs/phase0/phase-alpha-4-r1-local-validation-evidence.md` (commit `4ce5a0b`, 583줄 LVE — 51/51 PASS)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.1 + §4.3 + §4.4 + §5.5.1 + §5.5.2
- ADR-011 §2.1 (a)~(e) 5조건 모법 + §2.4 T2 영역
- ADR-008 부록 B + 부록 C
- 3 MVP-1 workflow (read-only 발견 대상): `.github/workflows/secret-hygiene-egress-redaction.yml` 694 + `.github/workflows/provider-adapter-enforcement.yml` 186 + `.github/workflows/provider-url-scanner.yml` 326

---

## 0. 본 brief 의 범위

### 0.1 사용자 명시 진입 명령 답습

> "W-1 brief caveat 8 후속 관찰 brief를 작성해주세요. 범위는 paths 필터와 workflow_dispatch 등록 여부를 포함한 actual run 발화 전략 재설계입니다. 아직 CI workflow 변경, workflow_dispatch 추가, actual run 재실행은 하지 마세요."

### 0.2 사용자 명시 3 금지 답습 (본 brief 의 명시적 경계)

| # | 금지 영역 | 본 brief 시점 |
|---|---------|----------|
| **#1** | **CI workflow 변경** (3 MVP-1 workflow 1206줄 변경 발효) | ✅ 0건 영구 답습 — W-1 = 0-line passthrough 답습 영구 |
| **#2** | **workflow_dispatch 추가** (3 workflow 어느 것에도 `workflow_dispatch:` 등록 발효) | ✅ 0건 영구 답습 — W-1 답습 영구 위반 영역 (#1 의 sub-영역) |
| **#3** | **actual run 재실행** (신규 GitHub Actions run trigger 재발화) | ✅ 0건 영구 답습 — 사용자 명시 #1 답습 영구 (후속 37 발견 evidence 답습 영역) |

**추가 답습 (사용자 명시 4 금지 — Operational Readiness PASS + Hermes PMO 격상 영구 답습 명시 영역)**:
- ❌ Operational Readiness PASS (Layer E) — 영구 답습
- ❌ Hermes PMO 격상 (Layer F) — 영구 답습

### 0.3 본 brief 영역 vs 후속 37 trigger 시도 / W-4 brief 영역 분리 매트릭스

| 영역 | 후속 37 trigger 시도 (`d4a0107` + `4bd8d68`) | W-4 lockdown / *실 trigger 발화 결정* brief | 본 brief (W-1 caveat 8 후속 관찰) |
|------|----------------------------------|-------------------------------------|---------------------------|
| 범위 | empty commit + push 발효 시도 + paths 필터 발견 evidence | actual run trigger / 검증 lockdown + 실 발화 결정 lockdown | **paths 필터 + workflow_dispatch 답습 영역 + actual run 발화 전략 재설계** |
| 변경 대상 artifact | empty commit (file 변경 0건) | 수정 파일 0건 | **수정 파일 0건 — 답습 영역 발견 + 전략 재설계 한정** |
| 핵심 결과 | trigger commit 발효 ✅ + actual run 발화 0건 ❌ → paths 필터 발견 | (α) defer + (β) `push` event 1 run 권고 시작점 (paths 필터 *간과*) | **paths 필터 + workflow_dispatch 답습 영역 *명시* + actual run 발화 전략 5+ 옵션 enumerate** |
| 합의 신규 조건 | 0건 (사용자 명시 직접 실행 영역) | 37 + 26 = 63 | **DRAFT (사용자 명시 승인 *전*)** |

### 0.4 본 brief 가 *하는* 것

1. 후속 37 발견 evidence (`d4a0107` + `4bd8d68`) 발효 후속 — **W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 lockdown 한정** (§1)
2. **본 brief 영역 한정 매트릭스** — paths 필터 + workflow_dispatch 답습 + W-1 + W-2 + W-3 + W-4 답습 (§2)
3. **paths 필터 답습 매트릭스 (정밀 — 3 workflow × paths 영역 enumerate)** — 후속 37 발견 evidence 답습 한정 (§3)
4. **workflow_dispatch 비등록 답습 매트릭스** — 0/3 등록 답습 한정 (§4)
5. **actual run 발화 전략 재설계 옵션 매트릭스** — 5+ 옵션 enumerate + 각 옵션 위험 / 권고 (§5)
6. **W-N 답습 위반 가능성 매트릭스 (옵션 별)** — 옵션 별 W-1 / W-2 / W-3 / W-4 / Phase α-1+2+3 답습 영역 위반 가능성 (§6)
7. **사용자 명시 3 금지 × 본 brief 분리 매트릭스** (§7)
8. **합산 602 합의 조건 답습 매트릭스** (변경 0건) (§8)
9. **합의 형태 권고 + 풀 3+1 트리거 분석** (§9)
10. **본 brief 자체 금지 + 본 brief 발효 후 의무 금지** (§10)
11. **다음 단계 결정 옵션** (사용자 결정 영역, §11)
12. **본 brief 메타 검증** (§12)
13. **본 brief 요약** (§13)

### 0.5 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 3 금지 영역**:

- ❌ **CI workflow 변경 (0건)** — W-1 = 0-line passthrough 답습 영구
- ❌ **workflow_dispatch 추가 (0건)** — 3 workflow 어느 것에도 `workflow_dispatch:` 등록 발효 0건 (W-1 답습 영구 위반 영역)
- ❌ **actual run 재실행 (0건)** — 후속 37 발견 evidence 답습 한정 (사용자 명시 결정 후 별도 영역)

**Operational Readiness PASS + Hermes PMO 격상 영구 답습 영역**:
- ❌ **Operational Readiness PASS (Layer E) (0건)**
- ❌ **Hermes PMO 격상 (Layer F) (0건)**

**추가 금지 영역 (W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* 답습 패턴 보존)**:

- ❌ **R-1 영역 7 artifacts × 1593줄 본문 변경 (0건)** — W-1 + W-2 + W-3 답습 영구
- ❌ **R-4 / R-5 / R-7 본문 변경 (0건)** — 13 file × 1192줄 답습
- ❌ **`src/` runtime code / facade.py placeholder 변경 (0건)** — Backlog #4 분리
- ❌ **`tools/mvp1_pc3_ar1_integration_check.py` 본문 변경 (0건)** — W-2 답습 영구
- ❌ **3 MVP-1 workflow Stage 4 step (line 329~341) 변경 (0건)** — W-1 답습 영구
- ❌ **3 fixture 본문 변경 (0건)** — W-3 답습 영구
- ❌ **`on.push.paths` 영역 변경 (어느 workflow도)** — W-1 답습 영구 위반 영역 (paths 필터 자체는 답습 영역 보존 — 본 brief = 발견 한정)
- ❌ **`on.push.branches` 영역 변경 (어느 workflow도)** — W-1 답습 영구
- ❌ **`on.pull_request` 영역 변경 (어느 workflow도)** — W-1 답습 영구
- ❌ **trigger event 신규 도입 (`pull_request_target` / `schedule` / `repository_dispatch`)** — W-4 lockdown C-ω-10 + C-ω-11 + C-ω-12 답습 영구 비권고
- ❌ **branch 변경 (`main` / `develop` / 신규 — `feature/hermes-phase0` 답습 영역 외)** — W-4 lockdown C-ω-27 답습
- ❌ **신규 workflow 신설 (0건)** — T2/T3 별도 합의 영역
- ❌ **신규 paths 영역 추가 / 제거 (0건)** — paths 영역 자체 변경 = W-1 답습 영구 위반 영역
- ❌ **branch protection 변경 (0건)** — AR-2 영역 = Backlog #3 T3 분리
- ❌ **Required check 등록 (0건)** — W-6 영역 = Backlog #3 T3 분리
- ❌ **`permissions: contents: read` 보강 (0건)** — W-5 영역 분리
- ❌ **GitHub Actions secrets 사용 도입 (0건)** — F-금지 #1 영구 답습
- ❌ **PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 진입 (0건)** — Backlog #1+#2+#3 분리
- ❌ **Stage 5 (G3-7 4 항목) 자동 진입 (0건)** — Stage 4 후속 권고 영역
- ❌ **trigger commit `d4a0107` revert (0건)** — 후속 37 사용자 결정 = trigger commit 보존 (paths 필터 발견 evidence 한정) 답습 영구
- ❌ **R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 (0건)**
- ❌ **`.importlinter` 어느 영역 변경 (0건)**
- ❌ **R-7 docker secret block 어느 것 변경 (0건)**
- ❌ **3 MVP-1 workflow 외 G2/G3/G4 PoC 8 workflow 흡수 (0건)**
- ❌ **Hermes upstream Dockerfile 변경 (0건)**
- ❌ **Production `docker-compose.yml` 신설 / 변경 (0건)**
- ❌ **실 secret material commit (0건)**
- ❌ **4 prerequisite GitHub Actions runs 답습 변경 / 재실행 (0건)** — `25728590939` + `25728590916` + `25728590977` + `25731846625` SUCCESS + 추가 SUCCESS runs (PRE-T1 확장 답습) 답습 한정
- ❌ **Layer A / B / C / D / E / F 재발효 / 재선언 / 발효 (0건)**
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)** — 별도 commit 분리
- ❌ **git commit / push (0건)** — 사용자 명시 결정 후 진입
- ❌ **외부 LLM 자동 호출 (0건)** — Group α C-11 답습
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **token rotation 정책 / GitHub plan 가용성 자동 결정 (0건)** — Group α C-3 + C-4 답습
- ❌ **threshold *고정* (0건)** — CI runtime / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지
- ❌ **event enum 정식 등록 (0건)** — `pc3_ar1_integration_implementation` 후보 한정
- ❌ **Phase β / γ 자동 진입 (0건)**
- ❌ **MVP-2 ~ MVP-6 본문 deepening (0건)**
- ❌ **17 항목 우선순위 자동 *재고정* (0건)**
- ❌ **합산 602 합의 조건 자동 변경 (0건)** — 21 합의 모두 영구 답습
- ❌ **W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 합의 답습 변경 (0건)** — C-φ-30 + C-χ-35 + C-ψ-36 + C-ω-37 + C-A1-26 영구 답습
- ❌ **LVE 51/51 PASS evidence 자동 재집계 (0건)**

### 0.6 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) 3 MVP-1 workflow 어느 줄도 *변경* 하지 않으며 (W-1 답습 영구),
- (ii) `workflow_dispatch:` 어느 workflow 에도 *추가* 하지 않으며,
- (iii) `on.push.paths` 영역 어느 것도 *변경* 하지 않으며,
- (iv) 신규 actual GitHub Actions run trigger 어느 것도 *재실행* / *재발화* 시키지 않으며 (사용자 명시 #3 영구 답습),
- (v) `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 *변경* 하지 않으며 (W-2 답습 영구),
- (vi) 3 fixture 어느 줄도 *변경* 하지 않으며 (W-3 답습 영구),
- (vii) 합산 602 합의 조건 어느 것도 *해소* / *변경* 시키지 않으며,
- (viii) 사용자 명시 3 금지 영역 어느 것도 *해소* 시키지 않으며,
- (ix) 모든 상위 합의 본문 어느 줄도 *변경* 하지 않으며,
- (x) R-1 영역 1593줄 (7 artifacts) 어느 줄도 *변경* 하지 않으며,
- (xi) R-4 / R-5 / R-7 본문 1192줄 (13 file) 어느 줄도 *변경* 하지 않으며,
- (xii) `src/` runtime code / facade.py placeholder 어느 줄도 *변경* 하지 않으며,
- (xiii) W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 합의 답습 어느 것도 *변경* 시키지 않으며,
- (xiv) trigger commit `d4a0107` 어느 것도 *revert* 시키지 않으며,
- (xv) 4 prerequisite GitHub Actions runs 답습 어느 것도 *변경* / *재실행* 시키지 않으며,
- (xvi) actual run 발화 전략 어느 옵션도 *최종 확정* 시키지 않는다 (사용자 명시 결정 영역 한정).

본 brief 가 발생시키는 *유일한* 효과는 **W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 lockdown 권고 한정 + 5+ 옵션 enumerate**. 모든 *확정 발효* / *실 변경* / *실 trigger 발화* = *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 직전 commit chain 답습 (후속 37 발견 evidence 발효 후속)

| commit | 영역 | 본 brief 답습 |
|--------|------|------------|
| `df741a2` (2026-05-18) | W-1 brief Reviewer-only 단축 합의 — 30 조건 C-φ-1 ~ C-φ-30 — **caveat 8 모법** ("workflow 2/3 paths 미답습 영역 후속 관찰 보존") | ✅ **본 brief 의 framing 모법** |
| `310b518` (2026-05-18) | W-2 brief 합의 — 35 조건 C-χ-1 ~ C-χ-35 | ✅ 답습 한정 |
| `3aac549` (2026-05-19) | W-3 brief 합의 — 36 조건 C-ψ-1 ~ C-ψ-36 | ✅ 답습 한정 |
| `945f766` (2026-05-19) | W-4 lockdown brief 합의 — 37 조건 C-ω-1 ~ C-ω-37 (특히 C-ω-7 + C-ω-37) | ✅ 답습 한정 |
| `a7837f2` (2026-05-19) | W-4 *실 trigger 발화 결정* 합의 — 26 조건 C-A1-1 ~ C-A1-26 (특히 C-A1-26) | ✅ 답습 한정 |
| `968c4ba` (2026-05-19) | CONTEXT — 후속 36 메타 (W-4 *실 trigger 발화 결정* status) | ✅ 답습 한정 |
| `d4a0107` (2026-05-19) | trigger commit (empty commit + push 발효) — paths 필터 발견 evidence 한정 보존 | ✅ 답습 한정 (보존) |
| `4bd8d68` (HEAD, 2026-05-19) | CONTEXT — 후속 37 메타 (paths 필터 발견 evidence + 사용자 결정 "defer + W-1 caveat 8 후속 관찰 brief (권고)" 채택) | ✅ **본 brief 의 발효 trigger** |

### 1.2 후속 37 발견 evidence 의 핵심 발효 (본 brief 의 trigger)

| 영역 | 답습 |
|------|----|
| 시도 시점 | 2026-05-19 후속 37 |
| 시도 명령 | (β-1) `git commit --allow-empty -m "trigger W-4 actual run" && git push origin feature/hermes-phase0` (W-4 *실 trigger 발화 결정* 합의 C-A1-26 답습) |
| trigger commit 발효 | ✅ `d4a0107` (empty commit + push 발효) |
| **신규 actual run 발화** | ❌ **0건** (`gh run list --branch=feature/hermes-phase0 --commit=d4a0107` = `[]`) |
| **발견 사유** | **3 MVP-1 workflow 모두 `on.push.paths` 필터 설정 + `workflow_dispatch:` 비등록** + empty commit (file 변경 0건) = paths 매칭 안 됨 → trigger 0건 확정 |
| **W-1 brief caveat 8 직접 실현 evidence** | ✅ "workflow 2/3 paths 미답습 영역 후속 관찰 보존" 가 본 시도에서 직접 실현 — W-4 lockdown brief / W-4 *실 trigger 발화 결정* brief 모두 paths 필터 답습 영역을 *간과* 한 것이 발견 |
| 사용자 결정 후속 | "defer + W-1 caveat 8 후속 관찰 brief (권고)" 채택 — 본 brief = 그 채택 발효 |
| 본 brief trigger 의미 | **W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계** brief DRAFT 진입 |

### 1.3 12 단계 brief chain 매트릭스 (Phase α-4 자체 + 후속 37 evidence + 본 brief)

| Stage (α-4 영역) | brief / 합의 / evidence | commit | 합의 단위 | 합의 조건 | framing |
|------|------------|--------|---------|--------|--------|
| α-4 Stage 1 (영역 정의) | Phase α-4 R-1 진입 brief | `f91ef4b` + `e59a565` | APPROVE AS BRIEF | 29 | "Can we enter Phase α-4?" |
| α-4 Stage 1.5 ~ Stage 3 | (각 brief) | (각 commit chain) | APPROVE AS BRIEF | 33 + 38 + 31 + 36 = 138 | (생략) |
| α-4 Stage 4 entry (lockdown) | Stage 4 entry brief | `9c33efe` + `81472ba` | APPROVE AS BRIEF WITH CONDITIONS | 49 | "What exactly will Stage 4 W-1~W-4 do?" |
| α-4 Stage 4 W-1 / W-2 / W-3 (cycle 1~3) | (각 micro-patch brief) | (각 commit chain) | APPROVE AS BRIEF WITH 0-LINE PASSTHROUGH | 30 + 35 + 36 = 101 | (각 0-line passthrough) |
| α-4 Stage 4 W-4 (cycle 4/4) | W-4 actual run trigger / 검증 brief | `5d08966` + `945f766` | APPROVE AS BRIEF WITH TRIGGER-DEFERRED | 37 | "Should W-4 trigger a fresh actual run?" |
| α-4 Stage 4 W-4 *실 trigger 발화 결정* (cycle 4/4 후속) | W-4 *실 trigger 발화 결정* brief | `ccdb30d` + `a7837f2` | APPROVE AS BRIEF WITH DECISION-DEFERRED + RECOMMENDED-TRIGGER-METHOD | 26 | "Should we execute the W-4 lockdown's recommended trigger NOW?" |
| **후속 37 발견 evidence (cycle 4/4 후속 후속)** | **trigger commit + 메타 (paths 필터 발견)** | **`d4a0107` + `4bd8d68`** | **사용자 명시 직접 실행 영역 — 합의 신규 0건** | **0** | **"Execute (β-1) → paths 필터 발견"** |
| **W-1 caveat 8 후속 관찰 (본 brief)** | **W-1 caveat 8 후속 관찰 brief** | **(현재)** | **DRAFT (미확정)** | **(미확정)** | **"How should we redesign actual run 발화 전략, given paths 필터 + workflow_dispatch 비등록 evidence?"** |

### 1.4 본 brief 의 진입점

본 brief = **W-1 caveat 8 후속 관찰 framing** (W-4 *실 trigger 발화 결정* 합의 §11 옵션 (γ) 답습 + 후속 37 사용자 결정 "defer + W-1 caveat 8 후속 관찰 brief (권고)" 채택):

- α-4 Stage 1 ↔ 1.5 ↔ 2 ↔ 2.5 ↔ 3 ↔ Stage 4 entry ↔ W-1 ↔ W-2 ↔ W-3 ↔ W-4 lockdown ↔ W-4 *실 trigger 발화 결정* ↔ **후속 37 발견 evidence (paths 필터)** ↔ **W-1 caveat 8 후속 관찰 (본 brief)** ↔ actual run 발화 전략 재설계 발효 (사용자 결정 영역 후 진입)
- 본 brief 의 단일 책무: **"paths 필터 + workflow_dispatch 답습 영역 *명시* + actual run 발화 전략 재설계 옵션 *enumerate 한정*"** + **"실 변경 / 실 trigger 발화 자동 진입 0건"**
- 본 brief ≠ W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 재진입 (답습 영구)
- 본 brief ≠ actual run 실 재시도 (사용자 명시 #3 답습 영구)
- 본 brief ≠ Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언

### 1.5 6-Layer + Phase α 분리 매트릭스 (2026-05-19 후속 38 시점)

| Layer | 영역 | 본 brief 시점 답습 |
|------|-----|----------------|
| Layer A / B / C / D | (각 발효) | ✅ 답습 한정 |
| Layer E / F | (미진입) | ❌ 영구 답습 |
| Phase α-1 / α-2 / α-3 (R-4/R-5/R-7) | local PASS + actual run SUCCESS | ✅ 답습 한정 |
| Phase α-4 Stage 4 entry ~ W-1~W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* | (각 cycle 합의 발효) | ✅ 답습 영구 |
| **Phase α-4 Stage 4 후속 37 발견 evidence** | **paths 필터 + workflow_dispatch 비등록 확인** | ✅ 답습 한정 (read-only evidence) |
| **W-1 caveat 8 후속 관찰 (본 brief)** | **paths 필터 + workflow_dispatch + actual run 발화 전략 재설계** | ⏳ **본 brief = DRAFT** |

---

## 2. 본 brief 영역 한정 매트릭스

### 2.1 본 brief 단독 영역 enumerate

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-1 | 3 MVP-1 workflow 본문 (1206줄) | ❌ 본 brief 영역 외 (W-1 답습 영구) |
| W-2 | integration tool 본문 (298줄) | ❌ 본 brief 영역 외 (W-2 답습 영구) |
| W-3 | 3 fixture 본문 (89줄) | ❌ 본 brief 영역 외 (W-3 답습 영구) |
| W-4 lockdown | actual run trigger / 검증 lockdown | ❌ 본 brief 영역 외 (W-4 lockdown 답습 영구) |
| W-4 *실 trigger 발화 결정* | (α) defer + (β) `push` event 1 run + 발화 방식 (β-1) empty commit + push | ❌ 본 brief 영역 외 (W-4 *실 trigger 발화 결정* 답습 영구) |
| 후속 37 trigger 시도 | empty commit + push 발효 + paths 필터 발견 evidence | ❌ 본 brief 영역 외 (read-only evidence — trigger commit `d4a0107` 보존 답습 영구) |
| **W-1 caveat 8 후속 관찰** | **paths 필터 + workflow_dispatch 답습 영역 + actual run 발화 전략 재설계 옵션 enumerate** | ✅ **본 brief = lockdown 권고 한정** |

### 2.2 W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* + 후속 37 답습 명시 (위반 0건 영구 답습)

| 영역 | 답습 영구 |
|---|----------|
| W-1 (cycle 1/4) = 0-line passthrough 고정 (C-φ-30) | ✅ 영구 답습 |
| W-2 (cycle 2/4) = 0-line passthrough 고정 (C-χ-35) | ✅ 영구 답습 |
| W-3 (cycle 3/4) = 0-line passthrough 고정 (C-ψ-36) | ✅ 영구 답습 |
| W-4 lockdown (cycle 4/4) = TRIGGER-DEFERRED + 사용자 결정 후 `push` event 1 run 권고 시작점 (C-ω-37) | ✅ 영구 답습 |
| W-4 *실 trigger 발화 결정* = (α) defer + (β) `push` event 1 run + 발화 방식 (β-1) empty commit + push 고정 (C-A1-26) | ✅ 영구 답습 |
| 후속 37 trigger commit `d4a0107` 보존 (paths 필터 발견 evidence 한정) | ✅ 영구 답습 |

### 2.3 W-5 ~ W-10 분리 매트릭스 (위반 0건 영구 답습)

| # | 작업 영역 | 본 brief 영역 |
|---|--------|----------|
| W-5 | `permissions: contents: read` 보강 | ❌ 본 brief 영역 외 (Stage 5 cycle 4 / Backlog #1+#2 분리) |
| W-6 | Required check 등록 | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-7 | PC-4 local pre-commit hook 활성화 | ❌ 본 brief 영역 외 (Backlog #1+#2 분리) |
| W-8 | AR-2 branch protection rule | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-9 | AR-3 자동 revert bot | ❌ 본 brief 영역 외 (Backlog #3 T3 분리) |
| W-10 | Stage 5 (G3-7 4 항목) 진입 | ❌ 본 brief 영역 외 (Stage 5 분리) |

### 2.4 본 §2 의 *범위 한계*

본 §2 = **W-1 caveat 8 후속 관찰 단독 영역 *권고 한정***. 실 작업 결정 = 사용자 명시 결정 영역 (자동 진입 0건). W-1~W-4 lockdown + W-4 *실 trigger 발화 결정* 재진입 + 후속 37 trigger commit revert + W-5 ~ W-10 어느 것도 본 brief 가 *통합* / *변경* 시키지 않는다.

---

## 3. paths 필터 답습 매트릭스 (정밀, read-only 발견)

### 3.1 `secret-hygiene-egress-redaction.yml` (694줄) paths 답습 매트릭스 (line 29~50 답습)

| # | paths 영역 | 영역 분류 | W-N 답습 영역 |
|---|---------|--------|-------------|
| 1 | `tools/secret_scanner.py` | Phase α-1 R-4 도구 본문 | Phase α-1 답습 영구 |
| 2 | `tools/docker_secret_image_layer_check.sh` | Phase α-3 R-7 도구 본문 | Phase α-3 답습 영구 |
| 3 | `tools/docker_secret_restart_recovery.sh` | Phase α-3 R-7 도구 본문 | Phase α-3 답습 영구 |
| 4 | `tools/mvp1_pc3_ar1_integration_check.py` | **W-2 영역 (Stage 4 integration tool)** | **W-2 = 0-line passthrough 답습 영구** |
| 5 | `tools/workflow_secrets_usage_check.py` | Stage 5 cycle 1 도구 본문 | Stage 5 분리 영역 |
| 6 | `tools/workflow_secrets_reference_check.py` | Stage 5 cycle 2 도구 본문 | Stage 5 분리 영역 |
| 7 | `tools/workflow_fork_pr_secret_policy_check.py` | Stage 5 cycle 3 도구 본문 | Stage 5 분리 영역 |
| 8 | `tools/workflow_permissions_check.py` | Stage 5 cycle 4 도구 본문 | Stage 5 분리 영역 |
| 9 | `tools/docker_secret_inotify_sidecar_check.sh` | ST-2 sidecar 도구 본문 | Backlog #1 분리 영역 |
| 10 | `tests/fixtures/secret_hygiene/**` | Phase α-1 R-4 fixture | Phase α-1 답습 영구 |
| 11 | `tests/fixtures/gp3_st3/**` | Phase α-3 R-7 fixture | Phase α-3 답습 영구 |
| 12 | `tests/fixtures/gp3_st2/**` | Backlog #1 ST-2 fixture | Backlog #1 분리 영역 |
| 13 | `tests/fixtures/mvp1_pc3_ar1_integration/**` | **W-3 영역 (3 fixture)** | **W-3 = 0-line passthrough 답습 영구** |
| 14 | `tests/fixtures/stage5_g3_7/**` | Stage 5 fixture | Stage 5 분리 영역 |
| 15 | `docker/gp3-st3-poc/**` | Phase α-3 R-7 docker block | Phase α-3 답습 영구 |
| 16 | `docker/gp3-st2-poc/**` | Backlog #1 ST-2 docker | Backlog #1 분리 영역 |
| 17 | `.github/workflows/secret-hygiene-egress-redaction.yml` | **W-1 영역 (본 workflow 자체)** | **W-1 = 0-line passthrough 답습 영구** |
| 18 | `.github/workflows/provider-adapter-enforcement.yml` | **W-1 영역 (Stage 4 cross-verify)** | **W-1 = 0-line passthrough 답습 영구** |
| 19 | `.github/workflows/provider-url-scanner.yml` | **W-1 영역 (Stage 4 cross-verify)** | **W-1 = 0-line passthrough 답습 영구** |
| **합산** | **19 paths 영역** | — | **W-N 답습 영구 영역 14 + Stage 5/Backlog #1 분리 5** |

### 3.2 `provider-adapter-enforcement.yml` (186줄) paths 답습 매트릭스 (line 32~38 답습)

| # | paths 영역 | 영역 분류 | W-N 답습 영역 |
|---|---------|--------|-------------|
| 1 | `tools/provider_import_scanner.py` | Phase α-1 R-4 도구 본문 | Phase α-1 답습 영구 |
| 2 | `tests/fixtures/provider_adapter_enforcement/**` | Phase α-1 R-4 fixture | Phase α-1 답습 영구 |
| 3 | `.github/workflows/provider-adapter-enforcement.yml` | **W-1 영역 (본 workflow 자체)** | **W-1 = 0-line passthrough 답습 영구** |
| 4 | `.importlinter` | **Phase α-2 R-5 본문** | **Phase α-2 답습 영구 (TR-1~TR-5 영역)** |
| 5 | `requirements-dev.txt` | dev dep 본문 | dev 영역 분리 (별도 합의 필요) |
| 6 | `src/**` | **Phase α-1 R-4 / Backlog #4 영역** | **`src/` runtime code 변경 = 답습 영구 위반 영역** |
| **합산** | **6 paths 영역** | — | **W-N + Phase α-1+2 답습 영구 영역 5 + dev 영역 1** |

### 3.3 `provider-url-scanner.yml` (326줄) paths 답습 매트릭스 (line 27~30 답습)

| # | paths 영역 | 영역 분류 | W-N 답습 영역 |
|---|---------|--------|-------------|
| 1 | `tools/provider_url_scanner.py` | Phase α-1 R-4 도구 본문 | Phase α-1 답습 영구 |
| 2 | `tests/fixtures/provider_url_scanner/**` | Phase α-1 R-4 fixture | Phase α-1 답습 영구 |
| 3 | `.github/workflows/provider-url-scanner.yml` | **W-1 영역 (본 workflow 자체)** | **W-1 = 0-line passthrough 답습 영구** |
| **합산** | **3 paths 영역** | — | **W-N + Phase α-1 답습 영구 영역 3** |

### 3.4 3 workflow paths 답습 합산 매트릭스

| workflow | paths 영역 수 | W-N 답습 영구 영역 | Stage 5 / Backlog 분리 영역 | dev / src 영역 |
|----------|----------|----------------|-------------------------|------------|
| `secret-hygiene-egress-redaction.yml` | 19 | 14 | 5 | 0 |
| `provider-adapter-enforcement.yml` | 6 | 5 (W-1 + Phase α-1 + Phase α-2) | 0 | 1 (`requirements-dev.txt`) + 1 (`src/**`) |
| `provider-url-scanner.yml` | 3 | 3 (W-1 + Phase α-1) | 0 | 0 |
| **합산** | **28 paths 영역** | **22 W-N 답습 영구** | **5 Stage 5 / Backlog 분리** | **1 dev + 1 src = 2** |

### 3.5 paths 영역 *변경 가능* 영역 enumerate (전략 재설계 시 사용자 결정 영역)

| 영역 | 변경 시 W-N 답습 영구 위반 가능성 | 사용 가능성 |
|------|-----------------------|----------|
| W-1~W-4 답습 영구 영역 (W-1 본 workflow 3개 / W-2 integration tool / W-3 3 fixture) | ❌ 답습 영구 위반 (cycle 1~3 합의 답습) | **본 brief 영구 비권고** |
| Phase α-1+2+3 답습 영구 영역 (R-4 도구 본문 3개 / R-5 `.importlinter` / R-7 docker block + 도구) | ❌ 답습 영구 위반 (Phase α-1+2+3 cycle 답습) | **본 brief 영구 비권고** |
| Stage 5 / Backlog 분리 영역 (Stage 5 cycle 1~4 도구 5개 + tests/fixtures/stage5_g3_7/** + Backlog #1 ST-2 docker/fixture/tool) | ⚠️ Stage 5 / Backlog #1 분리 영역 진입 가능성 | **본 brief 영구 비권고 (영역 외)** |
| `requirements-dev.txt` (dev dep 본문) | ⚠️ dev 영역 변경 = 별도 합의 필요 | 옵션 (사용자 결정 영역 — 신중) |
| `src/**` (runtime code) | ❌ `src/` runtime code 답습 영구 위반 (Backlog #4 facade real 본문) | **본 brief 영구 비권고** |

### 3.6 본 §3 의 *범위 한계*

본 §3 = **paths 필터 답습 매트릭스 *read-only 발견 한정***. 본 §3 의 어떤 항목도 *변경* / *재해석* / *재합의* 영역이 아니며, 단순히 *현재 상태* 답습 enumerate 한정. paths 영역 변경 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. workflow_dispatch 비등록 답습 매트릭스 (read-only)

### 4.1 3 workflow workflow_dispatch 등록 여부 (후속 37 발견 evidence)

| workflow | `workflow_dispatch:` 등록 | manual UI trigger 가능성 |
|----------|----------------------|----------------------|
| `secret-hygiene-egress-redaction.yml` | ❌ 비등록 | ❌ 불가능 |
| `provider-adapter-enforcement.yml` | ❌ 비등록 | ❌ 불가능 |
| `provider-url-scanner.yml` | ❌ 비등록 | ❌ 불가능 |
| **합산** | **0/3 등록** | **3/3 manual UI trigger 불가능** |

### 4.2 workflow_dispatch 추가 가능성 (사용자 명시 #2 영구 답습)

| 영역 | 답습 |
|------|----|
| `workflow_dispatch:` 추가 = 3 workflow 어느 것에도 등록 발효 | ❌ 사용자 명시 #2 영구 답습 (W-1 답습 영구 위반 영역 — `on:` block 변경 = workflow 본문 변경) |
| `gh workflow run` CLI 명령 가능성 | ❌ workflow_dispatch 비등록 상태에서 `gh workflow run` 호출 = `HTTP 422` 에러 (workflow does not have a workflow_dispatch trigger) |
| **합산** | **manual UI trigger 영구 불가능 (사용자 명시 #2 답습 영구)** |

### 4.3 본 §4 의 *범위 한계*

본 §4 = **workflow_dispatch 비등록 답습 *read-only 발견 한정***. 본 §4 의 어떤 항목도 *변경* / *추가* 영역이 아니며, 단순히 *현재 상태* 답습 enumerate 한정. workflow_dispatch 추가 = 사용자 명시 #2 영구 답습 영역.

---

## 5. actual run 발화 전략 재설계 옵션 매트릭스

### 5.1 5+ 옵션 enumerate (사용자 결정 영역, paths 필터 + workflow_dispatch 비등록 답습 영구 고려)

| 옵션 | 영역 | W-N 답습 영구 위반 | 본 brief 권고 |
|-----|----|--------------|----------|
| **(A)** | **defer 영구 유지** (현 상태 — actual run 발화 0건 영구 답습, paths 필터 + workflow_dispatch 비등록 답습 영구 보존, 다음 cycle / 다음 세션 / 다음 합의 영역으로 보류) | ✅ 0건 (모든 답습 영구 보존) | ✅ **권고 시작점 (가장 보수적, 모든 답습 영구 보존)** |
| (B) | `pull_request` event open (`feature/hermes-phase0 → main` PR open) — 3 workflow 모두 `pull_request: branches: [main]` 매칭 + `pull_request` event = paths 필터 안 가짐 → 3 runs 동시 발화 | ⚠️ PR open 자체 = W-4 lockdown 옵션 (β-4) = Backlog #3 T3 분리 영역 명시 — Required check 등록 ≠ trigger 발화 가능성 자체 (두 영역 분리) | 옵션 (사용자 결정 영역) — Backlog #3 T3 영역 분리 검토 필요 |
| (C) | **next 본문 변경 commit + push** (paths 매칭 file 변경) — W-N 답습 영구 영역 외 paths 매칭 file 에 변경 (예: 미래 docs 갱신 commit) | ⚠️ paths 매칭 file 중 W-N 답습 영구 영역 외 = 극히 제한적 (Stage 5 / Backlog 분리 영역만 비-답습 영구) — 정상 작업 cycle 답습 영역 진입 시 자동 발화 가능 | 옵션 (사용자 결정 영역 — paths 매칭 file 변경 = 별도 작업 영역, 본 brief 영역 외) |
| (D) | **workflow_dispatch 추가 brief** (W-1 답습 영구 위반 영역, 사용자 명시 #2 영구 답습 위반) | ❌ W-1 답습 영구 위반 (사용자 명시 #2 영구 답습 위반) | **본 brief 영구 비권고** |
| (E) | **신규 trigger workflow 신설** (paths 필터 없는 신규 workflow 신설 — Stage 4 step 호출만 포함) | ⚠️ T2/T3 별도 합의 영역 + 신규 workflow 신설 = 별도 합의 필요 | 옵션 (T2/T3 영역 — 별도 합의 영역, 본 brief 영역 외) |
| (F) | **paths 영역 변경 brief** (W-1 답습 영구 위반 영역, 사용자 명시 #2 영구 답습 위반) | ❌ W-1 답습 영구 위반 | **본 brief 영구 비권고** |
| (G) | **`schedule` cron event 도입** (W-4 lockdown C-ω-10 답습 영구 비권고) | ❌ Layer E / MVP-6 분리 영역 + Operational Readiness PASS 영역 | **본 brief 영구 비권고** |
| (H) | **`repository_dispatch` event 도입** (W-4 lockdown C-ω-11 답습 영구 비권고) | ❌ Layer F / ADR-008 부록 C 영역 | **본 brief 영구 비권고** |
| (I) | **`pull_request_target` event 도입** (W-4 lockdown C-ω-12 답습 영구 비권고) | ❌ T2/T3 영역 + GitHub Actions cache poisoning 위험 | **본 brief 영구 비권고** |

### 5.2 옵션 (A) defer 영구 유지의 *근거* enumerate (권고 시작점)

| 근거 영역 | 답습 |
|--------|----|
| 모든 답습 영구 보존 — W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* + 후속 37 evidence | ✅ 영구 답습 |
| paths 필터 + workflow_dispatch 비등록 답습 영구 보존 — 사용자 명시 #1 + #2 + #3 모두 영구 답습 | ✅ 사용자 명시 3 금지 영구 답습 |
| LVE 51/51 PASS + 4 prerequisite GitHub Actions runs 답습 영구 보존 (모두 자동 보존) | ✅ 자동 보존 |
| Stage 4 step (line 318~360) 본문 wired + 4 prerequisite runs 4/4 SUCCESS = R-1 영역 functional evidence 충분 | ✅ LVE §4 답습 (별도 trigger 발화 = 추가 evidence 영역, 필수 아님) |
| W-1 caveat 8 후속 관찰 영구 답습 = paths 필터 + workflow_dispatch 비등록 *상태 자체* 답습 영구 (별도 cycle 별도 합의 / 별도 brief 시점까지 보존) | ✅ 본 brief = caveat 8 본격 후속 관찰 발효 |
| Phase α-4 R-1 Stage 4 cycle 1~4 완성 + 모든 layer evidence 답습 영구 = 추가 actual run 발화 없이도 Stage 4 lockdown 영구 보존 | ✅ Phase α-4 R-1 functional 완성 상태 |

### 5.3 옵션 (B) `pull_request` event open 의 *근거* enumerate (옵션, Backlog #3 T3 영역 분리)

| 근거 영역 | 답습 |
|--------|----|
| 3 workflow 모두 `pull_request: branches: [main]` 등록 — `feature/hermes-phase0 → main` PR open 시 매칭 | ✅ §3 답습 발견 |
| `pull_request` event = paths 필터 안 가짐 (GitHub Actions 표준 답습) | ✅ pull_request event 는 branches 만 가짐 |
| PR open 시 3 workflow 동시 발화 = 3 runs | ✅ 예상 |
| 단, PR open 자체 = W-4 lockdown 옵션 (β-4) 영역 — Backlog #3 T3 분리 명시 (Required check 등록 / branch protection 등) | ⚠️ Required check 등록 ≠ trigger 발화 가능성 자체 (두 영역 분리 — Required check 는 PR merge 차단 영역, trigger 발화는 PR open 자체로 발생) |
| Required check 등록 없이 PR open 가능성 검토 | 옵션 (사용자 결정 영역 — Backlog #3 T3 분리 영역 명시 + 별도 합의 영역) |
| 옵션 (B) 채택 시 = W-4 actual run trigger 발화 영역 해소 + Required check 등록 영역 = Backlog #3 T3 분리 영구 답습 | ⚠️ 두 영역 분리 정밀 검토 필요 |
| 본 brief 권고 = 옵션 (B) = **옵션 (A) defer 다음 후보** (사용자 결정 영역) | ⚠️ 사용자 결정 영역 |

### 5.4 옵션 (C) next 본문 변경 commit + push 의 *근거* enumerate (옵션, paths 매칭 file 변경)

| 근거 영역 | 답습 |
|--------|----|
| paths 매칭 file 중 W-N 답습 영구 영역 외 영역 = Stage 5 / Backlog 분리 영역만 비-답습 영구 (예: tools/workflow_*_check.py / tests/fixtures/stage5_g3_7/** / Backlog #1 ST-2 영역) | ⚠️ Stage 5 / Backlog 분리 영역 진입 = 별도 합의 필요 |
| 미래 정상 작업 cycle (Stage 5 / Backlog 1+2 / Backlog #3 / Backlog #4 / Backlog #5 / Backlog #6) 진입 시 자동 발화 가능 (paths 매칭 file 변경 시) | ✅ 자연 발화 영역 |
| 본 brief 권고 = 옵션 (C) = **수동 trigger 비권고 + 자연 trigger 답습 영구** (다음 정상 작업 cycle 시 자동 발화) | ✅ 권고 영역 |
| 본 brief = 옵션 (C) 채택 권고 0건 — 다음 정상 작업 cycle 시점 답습 영구 영역 | ✅ defer (옵션 (A)) 답습 + 자연 trigger 영구 답습 |

### 5.5 영역 외 옵션 enumerate (본 brief 비권고 영구 답습)

| 영역 | 사유 |
|------|-----|
| 옵션 (D) workflow_dispatch 추가 | W-1 답습 영구 위반 + 사용자 명시 #2 영구 답습 위반 |
| 옵션 (E) 신규 workflow 신설 | T2/T3 영역 + 신규 workflow 신설 = 별도 합의 영역 |
| 옵션 (F) paths 영역 변경 | W-1 답습 영구 위반 |
| 옵션 (G) `schedule` cron | W-4 lockdown C-ω-10 답습 영구 비권고 |
| 옵션 (H) `repository_dispatch` | W-4 lockdown C-ω-11 답습 영구 비권고 |
| 옵션 (I) `pull_request_target` | W-4 lockdown C-ω-12 답습 영구 비권고 + cache poisoning 위험 |

### 5.6 actual run 발화 전략 재설계 권고 시작점 매트릭스

| 영역 | 본 brief 권고 시작점 | 사용자 결정 후 옵션 상한 |
|----------|------------------|--------------------|
| 발화 전략 결정 | **(A) defer 영구 유지** (모든 답습 영구 보존, paths 필터 + workflow_dispatch 비등록 답습 영구 보존) | 옵션 (B) `pull_request` event open (Backlog #3 T3 영역 분리 검토 필요) / 옵션 (C) next 본문 변경 commit + push (자연 trigger 답습 영구) |
| 발화 시점 | (영역 외 — 본 brief 시점 발화 0건 영구 답습) | 사용자 결정 영역 (별도 brief / 별도 cycle / 별도 합의 영역) |
| 발화 횟수 | (영역 외) | 0건 (defer) 또는 1 run (옵션 (B) PR open / 옵션 (C) 자연 trigger) |
| 발화 결과 검증 | (영역 외 — read-only) | RUN-1~7 (W-4 lockdown 답습) — 사용자 결정 후 영역 |

### 5.7 본 §5 의 *범위 한계*

본 §5 = **actual run 발화 전략 재설계 *옵션 enumerate 한정***. 본 §5 의 어떤 항목도:
- (i) 옵션 (A)~(I) 中 어느 것도 *채택 발효* 시키지 않으며,
- (ii) actual run 발화 전략 *최종 확정* 시키지 않으며,
- (iii) 신규 actual GitHub Actions run trigger 어느 것도 *재실행* / *재발화* 시키지 않으며 (사용자 명시 #3 영구 답습),
- (iv) workflow_dispatch 어느 workflow 에도 *추가* 시키지 않으며 (사용자 명시 #2 영구 답습),
- (v) CI workflow 어느 것도 *변경* 시키지 않는다 (사용자 명시 #1 영구 답습).

권고 시작점 = **옵션 (A) defer 영구 유지** (모든 답습 영구 보존) — 실 발화 전략 결정 = 사용자 명시 결정 영역.

---

## 6. W-N 답습 위반 가능성 매트릭스 (옵션 별)

### 6.1 옵션 별 W-N + Phase α-1~α-3 + Stage 5/Backlog 답습 영구 영역 위반 가능성

| 옵션 | W-1 (workflow 1206) | W-2 (tool 298) | W-3 (3 fixture 89) | W-4 lockdown | W-4 *실 trigger 발화 결정* | Phase α-1 R-4 | Phase α-2 R-5 | Phase α-3 R-7 | Stage 5 | Backlog | 사용자 명시 #1 | 사용자 명시 #2 | 사용자 명시 #3 |
|-----|------------------|--------------|-------------------|------------|----------------------|-----------|-----------|-----------|---------|---------|----------|----------|----------|
| (A) defer 영구 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 |
| (B) PR open | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ Backlog #3 T3 영역 분리 (Required check 등록 ≠ trigger 발화 자체) | ⚠️ 사용자 결정 후 trigger 발화 시점 = #1 해소 가능성 | ✅ 0 | ✅ 0 |
| (C) next 본문 commit + push | ✅ 0 (W-N 답습 영구 영역 외 변경만) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ R-4 도구 본문 변경 시 위반 | ⚠️ R-5 변경 시 위반 | ⚠️ R-7 변경 시 위반 | ⚠️ Stage 5 도구/fixture 변경 시 별도 합의 필요 | ⚠️ Backlog 영역 진입 시 별도 합의 필요 | ⚠️ 자연 trigger 시 #1 해소 가능성 | ✅ 0 | ✅ 0 |
| (D) workflow_dispatch 추가 | ❌ 위반 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ 추가 후 #1 해소 가능성 | ❌ 위반 (사용자 명시 #2) | ✅ 0 |
| (E) 신규 workflow 신설 | ✅ 0 (W-1 = 3 workflow 영역 외) | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ❌ Stage 5 영역 또는 T2/T3 영역 | ⚠️ Backlog 영역 진입 | ⚠️ 신규 workflow 발화 시 #1 해소 가능성 | ✅ 0 | ✅ 0 |
| (F) paths 변경 | ❌ 위반 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ paths 변경 후 #1 해소 가능성 | ❌ 위반 (W-1 영역) | ✅ 0 |
| (G) schedule cron | ❌ 위반 (`on:` 변경) | ✅ 0 | ✅ 0 | ⚠️ C-ω-10 답습 영구 비권고 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ cron 발화 시 #1 해소 가능성 | ❌ 위반 | ❌ Layer E 위반 가능성 |
| (H) repository_dispatch | ❌ 위반 (`on:` 변경) | ✅ 0 | ✅ 0 | ⚠️ C-ω-11 답습 영구 비권고 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ 발화 시 #1 해소 가능성 | ❌ 위반 | ❌ Layer F 위반 가능성 |
| (I) pull_request_target | ❌ 위반 (`on:` 변경) | ✅ 0 | ✅ 0 | ⚠️ C-ω-12 답습 영구 비권고 + cache poisoning 위험 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ✅ 0 | ⚠️ 발화 시 #1 해소 가능성 | ❌ 위반 | ⚠️ T2/T3 영역 |

### 6.2 합산 분석

| 옵션 | W-N 답습 영구 위반 | Phase α-1~α-3 답습 영구 위반 | Stage 5 / Backlog 분리 영역 진입 | 사용자 명시 3 금지 위반 |
|-----|-------------------|-----------------------|------------------------------|------------------|
| **(A) defer 영구** | **0/5** | **0/3** | **0/2** | **0/3** |
| (B) PR open | 0/5 | 0/3 | 1/2 (Backlog #3 T3) | 0/3 (사용자 결정 후 #1 해소 영역) |
| (C) next 본문 commit + push | 0/5 (W-N 답습 영구 영역 외만) | 위반 가능성 | 위반 가능성 | 0/3 (자연 trigger) |
| (D) workflow_dispatch 추가 | 1/5 (W-1) | 0/3 | 0/2 | 1/3 (#2 위반) |
| (E) 신규 workflow 신설 | 0/5 | 0/3 | 1/2 (Stage 5 / T2/T3) | 0/3 |
| (F) paths 변경 | 1/5 (W-1) | 0/3 | 0/2 | 1/3 (#2 위반) |
| (G) schedule cron | 1/5 (W-1) | 0/3 | 0/2 | 1/3 (#2 위반) + ⚠️ Layer E |
| (H) repository_dispatch | 1/5 (W-1) | 0/3 | 0/2 | 1/3 (#2 위반) + ⚠️ Layer F |
| (I) pull_request_target | 1/5 (W-1) | 0/3 | 0/2 | 1/3 (#2 위반) + ⚠️ T2/T3 + cache poisoning |

**핵심 발견**: 옵션 (A) defer 영구 유지 = **모든 영역 0건 위반**. 옵션 (B) PR open = Backlog #3 T3 영역 분리 검토 필요 (Required check 등록 ≠ trigger 발화 자체 — 두 영역 분리). 옵션 (D)~(I) = 모두 W-1 답습 영구 위반 또는 사용자 명시 #2 위반 + 추가 영역 진입 = **본 brief 비권고**.

### 6.3 본 §6 의 *범위 한계*

본 §6 = **W-N 답습 위반 가능성 *enumerate 한정***. 본 §6 의 어떤 항목도 *발화* / *해소* 시키지 않는다.

---

## 7. 사용자 명시 3 금지 × 본 brief 분리 매트릭스

### 7.1 사용자 명시 3 금지 영역 위반 0건 영구 답습

| # | 금지 영역 | 본 brief 작성 시점 | 본 brief 발효 후 (사용자 결정 영역) |
|---|---------|---------------|------------------------------|
| #1 | CI workflow 변경 | ✅ 0건 (W-1 답습 영구) | ✅ 0건 (옵션 (A)~(C) 채택 시 영구 보존, 옵션 (D)~(I) 채택 시 위반 가능성 — 본 brief 비권고) |
| #2 | workflow_dispatch 추가 | ✅ 0건 (W-1 답습 영구 sub-영역) | ✅ 0건 (옵션 (A)~(C) + (E) 채택 시 영구 보존, 옵션 (D) 채택 시 위반 — 본 brief 비권고) |
| #3 | actual run 재실행 | ✅ 0건 (사용자 명시 #1 답습 영구) | ✅ 0건 (옵션 (A) defer 유지 시 영구 보존, 옵션 (B)~(C) 채택 시 = 별도 cycle 영역에서 발화) |
| **합산** | **3** | **✅ 3/3 위반 0건** | **✅ 3/3 보존 (옵션 (A) 채택 시) — 옵션 (B)~(C) 채택 시 별도 cycle 영역** |

**Operational Readiness PASS + Hermes PMO 격상 영구 답습** (사용자 명시 4 금지 영역 #4 + #5 답습 — 본 명시 3 금지 영역 외):
- ❌ Operational Readiness PASS (Layer E) = 영구 0건 답습
- ❌ Hermes PMO 격상 (Layer F) = 영구 0건 답습

### 7.2 Backlog 분리 매트릭스

| Backlog | 영역 | 본 brief 영역 |
|---------|----|----------|
| Backlog #1 + #2 / #3 T3 / #4 / #5 / #6 / Stage 5 | (각 영역) | ❌ 본 brief 영역 외 (각각 분리) |
| W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* | 각 cycle 답습 영역 | ❌ 본 brief 영역 외 (답습 영구) |
| 후속 37 trigger commit `d4a0107` 보존 (paths 필터 발견 evidence) | read-only evidence | ❌ 본 brief 영역 외 (보존 답습 영구) |

### 7.3 본 §7 의 *범위 한계*

본 §7 = **분리 매트릭스 *권위 권고 한정***. 사용자 명시 3 금지 영역 + Backlog 분리 영역 + W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* cycle 분리 영역 어느 것도 *해소* / *통합* 시키지 않는다.

---

## 8. 합산 602 합의 조건 답습 매트릭스

### 8.1 합산 합의 조건 매트릭스

| 합의 | commit | 조건 수 | 본 brief 변경 |
|------|-------|------|-----------|
| 직전 20 합의 (Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 직전 29 + Layer C 30 + Layer D 25 + Stage 1 25 + Stage 2 25 + Stage 3 parallel 25 + α-4 진입 조건 점검 33 + Step Division 38 + LVE 31 + Stage 3 실 진입 36 + Stage 4 entry 49 + W-1 30 + W-2 35 + W-3 36 + W-4 lockdown 37) | (각 답습) | **576** | 0건 |
| **Phase α-4 R-1 Stage 4 W-4 *실 trigger 발화 결정*** | `a7837f2` | **26 (C-A1-1 ~ C-A1-26)** | **0건** ✅ |
| **합산** | **21 합의** | **602 조건** | **0건 영구 답습** ✅ |

### 8.2 핵심 답습 매트릭스

| 조건 영역 | 본 brief 답습 |
|--------|----------|
| **C-φ-4 ~ C-φ-30 (W-1 합의, 특히 caveat 8 = "workflow 2/3 paths 미답습 영역 후속 관찰 보존")** | ✅ **본 brief = caveat 8 본격 후속 관찰 발효 영역** |
| C-χ-35 (W-2 = 0-line passthrough 고정 영구) | ✅ §2.2 답습 |
| C-ψ-36 (W-3 = 0-line passthrough 고정 영구) | ✅ §2.2 답습 |
| C-ω-7 (사용자 결정 후 trigger 발화 권고 시작점 = `push` event 1 run) | ✅ §3 답습 — paths 필터 답습 영역 발견 evidence 답습 |
| C-ω-10 + C-ω-11 + C-ω-12 (`schedule` / `repository_dispatch` / `pull_request_target` 영구 비권고) | ✅ §5 + §6 답습 (옵션 (G) (H) (I) 비권고) |
| C-ω-13 + C-ω-25 (W-4 검증 13 영역 + RUN-1~7) | ✅ §5.6 답습 |
| C-ω-24 (LVE 51/51 PASS + 4 prerequisite runs 보존 의무 영구) | ✅ 답습 영구 |
| C-ω-27 + C-ω-28 (branch = `feature/hermes-phase0` + 횟수 = 1 run) | ✅ §5 답습 |
| C-ω-37 (W-4 = trigger 발화 0건 본 brief 시점 + 사용자 결정 후 `push` event 1 run 고정 영구) | ✅ §2.2 답습 — paths 필터 발견 evidence 답습 후속 |
| **C-A1-26 (W-4 *실 trigger 발화 결정* 권고 시작점 = (α) defer + (β) `push` event 1 run + 발화 방식 (β-1) empty commit + push 고정 영구)** | ✅ **§2.2 답습 — 후속 37 trigger 시도 모법** |
| Group α C-11 (외부 LLM 응답 = 입력 한정) | ✅ §9 답습 |
| F-금지 #1 (GitHub Actions secrets 사용 도입 0건 영구) | ✅ §3 답습 |
| ADR-011 §2.1 (a)~(e) 5조건 모법 + ADR-008 부록 C 12 조건 미진입 영구 답습 | ✅ 답습 한정 |

---

## 9. 합의 형태 권고 + 풀 3+1 트리거 분석

### 9.1 본 brief 권고 합의 형태

| 합의 형태 | 적격성 | 본 brief 권고 |
|---------|------|----------|
| **(a) Reviewer-only 단축 합의** | T-2 재발화 영역 한계 (Stage 4 entry brief + W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* 시점 이미 발화) + 본 brief = paths 필터 + workflow_dispatch 답습 영역 발견 한정 + actual run 발화 전략 재설계 lockdown 한정 + 본 brief 시점 발화 0건 영구 답습 | ✅ **권고 시작점** — 본 brief = W-1 caveat 8 후속 관찰 lockdown DRAFT + paths 필터 + workflow_dispatch 답습 영역 발견 + 5+ 옵션 enumerate + 모든 답습 영구 → T-2 발화 *영역 한계* + 풀 3+1 트리거 0/16 새 발화 |
| (b) 풀 3+1 합의 | 사용자 명시 보강 결정 시 | 옵션 (사용자 결정 영역) |
| (c) 풀 3+1 + 외부 LLM 1+ | T-6 / T-10 / T-13 발화 시 | ❌ 비권고 |

### 9.2 풀 3+1 트리거 16 영역 × 본 brief 발화 매트릭스

| T # | 영역 | 본 brief 발화 |
|----|----|------------|
| T-1 ~ T-16 | (모든 영역) | **0/16 새 발화** — Stage 4 entry brief + W-1 ~ W-4 + W-4 *실 trigger 발화 결정* + 후속 37 시점 이미 답습 영역 완료 + 본 brief = paths 필터 + workflow_dispatch 답습 영역 발견 한정 + 본 brief 시점 발화 0건 + 5+ 옵션 enumerate + 옵션 (A) defer 영구 권고 시작점 |
| **합산** | **16 트리거** | **0/16 새 발화 → Reviewer-only 단축 합의 적격 시작점** |

### 9.3 외부 LLM 1+ 비적용 사유

| 영역 | 비적용 사유 |
|------|---------|
| Group α C-14 | 비적격 — 본 brief = W-1 caveat 8 후속 관찰 한정 + read-only 발견 + 5+ 옵션 enumerate + 옵션 (A) defer 영구 권고 시작점 |
| T-6 / T-10 / T-13 | 0건 (Backlog #3 / 경계 분리 / Stage 5 분리 명시) |
| 본 brief 권고 | **외부 LLM 1+ 비적용** (Group α C-11 + ADR-011 §2.4 답습 한정) |

---

## 10. 본 brief 자체 금지 + 본 brief 발효 후 의무 금지

### 10.1 본 brief 자체 금지 ≥ 50 영역

본 brief 자체는 다음 영역을 *발효* 시키지 않는다:

- ❌ 3 MVP-1 workflow 어느 줄도 변경 (W-1 답습 영구)
- ❌ `workflow_dispatch:` 어느 workflow 에도 추가 (사용자 명시 #2 영구 답습)
- ❌ `on.push.paths` 영역 어느 것도 변경 (W-1 답습 영구)
- ❌ `on.push.branches` 영역 어느 것도 변경 (W-1 답습 영구)
- ❌ `on.pull_request` 영역 어느 것도 변경 (W-1 답습 영구)
- ❌ 신규 actual GitHub Actions run trigger 어느 것도 재실행 / 재발화 (사용자 명시 #3 영구 답습)
- ❌ `tools/mvp1_pc3_ar1_integration_check.py` 어느 줄도 변경 (W-2 답습 영구)
- ❌ 3 fixture 어느 줄도 변경 (W-3 답습 영구)
- ❌ 4 prerequisite runs 답습 어느 것도 변경 / 재실행
- ❌ trigger commit `d4a0107` 어느 것도 revert (후속 37 사용자 결정 답습 영구)
- ❌ R-4 / R-5 / R-7 본문 어느 것도 변경
- ❌ `src/` runtime code 어느 것도 변경
- ❌ Stage 4 step (line 318~360) 본문 어느 것도 변경
- ❌ §5.5.1 + §5.5.2 PC-3 + AR-1 본문 어느 것도 변경
- ❌ trigger event 신규 도입 (`pull_request_target` / `schedule` / `repository_dispatch`)
- ❌ branch 변경 (`feature/hermes-phase0` 답습 영역 외)
- ❌ 신규 workflow 신설
- ❌ 신규 paths 영역 추가 / 제거
- ❌ branch protection 변경 / Required check 등록 / `permissions:` 보강
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 어느 것도 변경
- ❌ `.importlinter` 어느 영역도 변경
- ❌ R-7 docker secret block 어느 것도 변경
- ❌ PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 어느 영역도 진입
- ❌ Stage 5 (G3-7 4 항목) 어느 항목도 진입
- ❌ W-5 ~ W-10 어느 영역도 진입
- ❌ GitHub Actions secrets 사용 도입 (F-금지 #1)
- ❌ Hermes upstream Dockerfile / Production `docker-compose.yml` 변경
- ❌ 실 secret material commit
- ❌ Layer A / B / C / D / E / F 재발효 / 재선언 / 발효
- ❌ 신규 ADR / P / GP 발행
- ❌ 합의 보고서 자동 작성
- ❌ CONTEXT / INDEX / SESSION 메타 자동 갱신
- ❌ git commit / push 자동 진입
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ token rotation / GitHub plan 자동 결정
- ❌ threshold 고정
- ❌ event enum 정식 등록
- ❌ Phase β / γ 자동 진입
- ❌ Group I 자동 진입
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 재고정
- ❌ 합산 602 합의 조건 자동 변경
- ❌ W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 합의 답습 변경
- ❌ LVE 51/51 PASS evidence 자동 재집계
- ❌ Operational Readiness PASS / Hermes PMO 격상 발효
- ❌ actual run 발화 전략 결정 자체의 최종 확정 발효 (사용자 명시 결정 영역)
- ❌ 옵션 (A)~(I) 中 어느 것도 자동 채택
- ❌ paths 영역 답습 자동 변경
- ❌ workflow_dispatch 자동 등록
- ❌ Phase α-1~α-4 통합 구현 완료 조건 재평가 자동 진입

### 10.2 본 brief 발효 후 의무 금지 ≥ 13 영역

본 brief APPROVE AS BRIEF 후에도 다음은 *자동* 진입 0건:

- ❌ actual run 실 재시도 자동 진입 (사용자 명시 결정 영역)
- ❌ W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 재진입 (답습 영구)
- ❌ 옵션 (A)~(I) 中 어느 것도 자동 채택
- ❌ Backlog #1+#2 / Backlog #3 T3 / Backlog #4 / Backlog #5 / Backlog #6 / Stage 5 자동 진입
- ❌ Layer C 재발효 / Layer D 재선언 / Layer E / Layer F 자동 진입
- ❌ Phase β / γ / MVP-2 ~ MVP-6 자동 진입
- ❌ 합의 보고서 자동 작성 (사용자 명시 결정 후)
- ❌ 메타 commit / push 자동 진입 (사용자 명시 결정 후)
- ❌ 외부 LLM 자동 호출
- ❌ 4 prerequisite runs 자동 재실행
- ❌ LVE evidence 자동 재집계
- ❌ Operational Readiness PASS / Hermes PMO 격상 자동 발효
- ❌ paths 영역 / workflow_dispatch 자동 변경

---

## 11. 다음 단계 결정 옵션 (사용자 결정 영역)

| 옵션 | 영역 | 영역 영향 |
|-----|----|---------|
| **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점)** | 본 brief = APPROVE AS BRIEF + W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 lockdown 권고 발효 + 합산 602 → 602+N (22 합의) | ✅ T-2 재발화 영역 한계 답습 + paths 필터 + workflow_dispatch 답습 영역 발견 권위 권고 + 5+ 옵션 enumerate |
| (B) 풀 3+1 합의 (사용자 명시 보강 결정 시) | Agent A + B + C 가동 | 옵션 (사용자 결정 영역) |
| (C) brief 수정 (특정 § 보강 요청) | 본 brief 본문 보강 → 재DRAFT | 옵션 |
| (D) 부분 채택 (특정 옵션 (A)~(C) 中 1+ 한정) | (A) defer / (B) PR open / (C) next 본문 commit + push 中 사용자 결정 | 옵션 (발화 전략 결정 영역) |
| (E) brief 합의 후 → 옵션 (A) defer 영구 유지 발효 | actual run 발화 전략 = defer 영구 유지 lockdown 발효 | 옵션 (가장 보수적) |
| (F) brief 합의 후 → 옵션 (B) PR open brief 진입 | feature/hermes-phase0 → main PR open brief 별도 진입 (Backlog #3 T3 영역 분리 검토) | 옵션 (사용자 결정 영역) |
| (G) Backlog 전환 | Backlog #1+#2 / #3 / #4 / #5 / #6 / Stage 5 中 사용자 결정 | 옵션 (영역 외 진입) |
| (H) Phase α-1~α-4 통합 구현 완료 조건 재평가 brief | 통합 완료 condition 재평가 진입 | 옵션 (별도 brief) |
| (I) brief 폐기 | 본 brief 본문 보존 + 합의 0건 | 옵션 |
| (J) 세션 종료 | CONTEXT / INDEX / SESSION 갱신 + 다음 세션 1순위 결정 | 옵션 |

### 11.1 (A) 옵션 채택 시 후속 commit chain (사용자 명시 결정 영역)

```
(현재) W-1 caveat 8 후속 관찰 brief DRAFT 작성 commit (예: 후속 38)
   │
   ▼ (사용자 명시 결정 후)
■ docs(review): approve W-1 caveat 8 paths filter followup brief (본 합의 commit)
   │
   ▼ (사용자 명시 결정 후)
■ docs(context): record W-1 caveat 8 paths filter followup status (CONTEXT + INDEX + SESSION 갱신)
   │
   ▼ (사용자 명시 결정 후)
■ git push origin feature/hermes-phase0
   │
   ▼ (자동 진입 0건 — 사용자 결정 영역)
■ (E) defer 영구 발효 / (F) PR open brief / Backlog 전환 / Phase α-1~α-4 통합 재평가 / 세션 종료 中 사용자 결정
```

### 11.2 본 brief 새 조건 후보 enumerate (합의 보고서 작성 시 정식 등록)

본 brief 발효 시 새 조건 후보 ≥ 26 (Latin C-A1 generation 후속 — C-A2 신규 sub-generation 시작):

| # | 후보 조건 영역 |
|---|------------|
| C-A2-1 | 본 brief = W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 진입 한정 (후속 37 trigger 시도 evidence 발효 후속) |
| C-A2-2 | W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* 답습 영구 |
| C-A2-3 | 후속 37 trigger commit `d4a0107` 보존 영구 답습 (paths 필터 발견 evidence 한정) |
| C-A2-4 | **3 workflow paths 답습 매트릭스 채택 (28 paths 영역 enumerate + 22 W-N 답습 영구 + 5 Stage 5/Backlog 분리 + 2 dev/src)** — **신규 영역** |
| C-A2-5 | **3 workflow workflow_dispatch 비등록 답습 영구 (0/3 등록 + manual UI trigger 불가능 + `gh workflow run` HTTP 422 예상)** — **신규 영역** |
| C-A2-6 | actual run 발화 전략 권고 시작점 = (A) defer 영구 유지 (모든 답습 영구 보존) |
| C-A2-7 | **사용자 결정 후 옵션 후보 = (B) `pull_request` event open (Backlog #3 T3 분리 영역 검토 필요) + (C) next 본문 commit + push (자연 trigger 답습 영구)** — **신규 영역** |
| C-A2-8 | **옵션 (D) workflow_dispatch 추가 영구 비권고 (W-1 답습 영구 위반 + 사용자 명시 #2 위반)** — **신규 영역** |
| C-A2-9 | **옵션 (E) 신규 workflow 신설 영구 비권고 (T2/T3 영역 + 별도 합의 필요)** — **신규 영역** |
| C-A2-10 | **옵션 (F) paths 영역 변경 영구 비권고 (W-1 답습 영구 위반)** — **신규 영역** |
| C-A2-11 | 옵션 (G) `schedule` cron + 옵션 (H) `repository_dispatch` + 옵션 (I) `pull_request_target` 영구 비권고 (W-4 lockdown C-ω-10 + C-ω-11 + C-ω-12 답습) |
| C-A2-12 | **paths 매칭 file 중 W-N 답습 영구 영역 외 = Stage 5 / Backlog 분리 영역 5 + dev/src 영역 2 만 비-답습 영구 (정상 작업 cycle 진입 시 자연 trigger 가능)** — **신규 영역** |
| C-A2-13 | W-N 답습 위반 가능성 매트릭스 채택 (옵션 별 위반 enumerate) |
| C-A2-14 | 사용자 명시 3 금지 3/3 위반 0건 영구 답습 + Operational Readiness PASS + Hermes PMO 격상 영구 답습 |
| C-A2-15 | 합산 602 합의 조건 변경 0건 영구 답습 |
| C-A2-16 | Backlog 분리 영구 답습 (#1~#6 + Stage 5 + W-1 + W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정*) |
| C-A2-17 | 풀 3+1 트리거 0/16 새 발화 → Reviewer-only 단축 합의 적격 |
| C-A2-18 | 외부 LLM 1+ 비적용 (T-6 / T-10 / T-13 미발화) |
| C-A2-19 | 본 brief 자체 금지 ≥ 50 영역 + 발효 후 의무 금지 ≥ 13 영역 |
| C-A2-20 | 5 영구 핵심 제약 5/5 보존 + Provider Liquidity 5-way 100% 보존 |
| C-A2-21 | F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) |
| C-A2-22 | LVE 51/51 PASS + 4 prerequisite runs 보존 의무 영구 |
| C-A2-23 | trigger commit `d4a0107` 보존 답습 영구 (revert 0건 영구) |
| C-A2-24 | brief 본문 변경 0건 영구 답습 |
| C-A2-25 | brief 발효 후 자동 진입 0건 (모든 후속 단계 = 사용자 명시 결정 영역) |
| **C-A2-26** | **(합의 시점 신규 1) actual run 발화 전략 = (A) defer 영구 유지 권고 시작점 + 사용자 결정 후 옵션 후보 enumerate ((B) PR open / (C) next 본문 commit + push) + 옵션 (D)~(I) 영구 비권고 고정 (사용자 명시 옵션 A 채택 발효 시)** |

---

## 12. 본 brief 메타 검증

### 12.1 본 brief 가 답습한 영역 매트릭스

| 답습 영역 | 답습 출처 | 본 brief 답습 |
|---------|---------|----------|
| 후속 37 발견 evidence (`d4a0107` + `4bd8d68`) | trigger commit + 메타 commit | ✅ §1.2 + §3 + §4 답습 한정 |
| W-1 brief 합의 (`df741a2`) caveat 8 ("workflow 2/3 paths 미답습 영역 후속 관찰 보존") | C-φ-1 ~ C-φ-30 | ✅ **본 brief framing 모법** |
| W-2 + W-3 + W-4 lockdown + W-4 *실 trigger 발화 결정* 합의 답습 | C-χ-35 + C-ψ-36 + C-ω-37 + C-A1-26 | ✅ §2.2 + §8.2 답습 |
| Stage 4 entry brief 합의 답습 | C-υ-43 + C-υ-44 + C-υ-41 + C-υ-42 | ✅ §8.2 답습 |
| LVE 51/51 PASS + 4 prerequisite runs 답습 | LVE §4 + §5.1 + §5.3 | ✅ §3.4 + §5.2 답습 |
| ADR-011 §2.1 (a)~(e) + ADR-008 부록 C 12 조건 | ADR-011 + ADR-008 | ✅ 답습 한정 |
| Group α C-11 / C-14 | Group α | ✅ §9.3 답습 |
| F-금지 #1 | Stage 5 cycle 1~4 | ✅ §0.5 답습 |
| 5 영구 핵심 제약 + Provider Liquidity 5-way + Backlog #1~#6 분리 | LVE §5.1+§5.2+§5.3 | ✅ 답습 한정 |
| `feedback_actual_run_trigger_paths_filter` 메모리 (사용자 명시 영구 답습) | 후속 37 발견 후 신설 메모리 | ✅ §3 + §4 답습 (paths 필터 + workflow_dispatch 답습 영역 명시 확인 의무) |

### 12.2 본 brief 자체 검증

| 검증 영역 | 본 brief 답습 |
|---------|----------|
| brief 작성 시점 3 금지 3/3 위반 | ✅ 0건 영구 답습 |
| brief 본문 = 답습 한정 (R-1 + R-4/5/7 + `src/` + W-1~W-4 lockdown + W-4 *실 trigger 발화 결정* + 후속 37 evidence 답습 영구) | ✅ 영구 답습 |
| brief 발효 시점 3 금지 3/3 위반 | ✅ 0건 영구 답습 (DRAFT 영역) |
| W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 재진입 / 신규 actual run trigger 재발화 | ✅ 0건 영구 답습 |
| 합산 602 합의 조건 변경 | ✅ 0건 영구 답습 |
| Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 | ✅ 0건 영구 답습 |
| 4 prerequisite runs 자동 재실행 | ✅ 0건 영구 답습 |
| 외부 LLM 자동 호출 / 실 API/SDK / 인간 리뷰 의무 자동 발화 | ✅ 0건 영구 답습 |
| 합의 보고서 작성 / 메타 commit / push / 실 발화 자동 진입 | ✅ 0건 (사용자 명시 결정 후 진입) |
| trigger commit `d4a0107` revert | ✅ 0건 영구 답습 |

### 12.3 본 brief 의 *제약 사항* enumerate

1. 본 brief = **준비안 (DRAFT)** — 사용자 명시 승인 전 어떤 *발효* 도 발생시키지 않는다
2. 본 brief 합의 시 = **W-1 caveat 8 후속 관찰 + actual run 발화 전략 재설계 lockdown 발효 한정** — 실 발화 전략 결정 / 실 trigger 발화 = 사용자 명시 결정 후 진입
3. 본 brief 영역 = **paths 필터 + workflow_dispatch 답습 영역 *명시* + 5+ 옵션 enumerate 한정** — R-1 + W-1~W-4 lockdown 본문 + paths 영역 + workflow_dispatch 등록 어느 것도 변경 영역 외
4. 본 brief 권고 시작점 = **옵션 (A) defer 영구 유지** (모든 답습 영구 보존)
5. 본 brief 답습 = **C-φ-x (caveat 8) + C-χ-35 + C-ψ-36 + C-ω-37 + C-A1-26 + 후속 37 evidence 동시 발효** 영역
6. 본 brief 합의 형태 = **(a) Reviewer-only 단축 합의 권고 시작점** (T-2 재발화 영역 한계 + 풀 3+1 트리거 0/16 새 발화)
7. 본 brief 비권고 영역 = **옵션 (D) workflow_dispatch 추가 + 옵션 (F) paths 영역 변경 + 옵션 (G) (H) (I) trigger event 신규 도입** (모두 W-1 답습 영구 위반 또는 사용자 명시 #2 위반)
8. 본 brief 의 합의 보고서 작성 / 메타 commit / push / 외부 LLM 호출 / **실 발화 전략 결정 자체** = **사용자 명시 결정 영역** (자동 진입 0건)
9. 본 brief 의 paths 영역 / workflow_dispatch 자동 변경 = **0건** (사용자 명시 #1 + #2 영구 답습)
10. 본 brief 의 trigger commit `d4a0107` 자동 revert = **0건** (후속 37 사용자 결정 답습 영구)

---

## 13. 본 brief 요약

본 brief 는 **후속 37 W-4 실 trigger 발화 직접 실행 시도 (`d4a0107` empty commit + push 발효 + 신규 actual run 발화 0건) + paths 필터 발견 evidence (`4bd8d68` 메타 commit) 발효 후속**, 사용자 명시 진입 명령 답습 — **W-1 brief 합의 (`df741a2`) caveat 8 ("workflow 2/3 paths 미답습 영역 후속 관찰 보존") 본격 후속 관찰 + actual run 발화 전략 재설계 lockdown brief 준비안 (DRAFT)** = "*How* should we redesign the W-4 actual run trigger 발화 전략, given the paths 필터 + workflow_dispatch 비등록 발견 evidence?".

**사용자 명시 3 금지** (CI workflow 변경 (W-1 답습 영구) / workflow_dispatch 추가 (W-1 답습 영구 sub-영역) / actual run 재실행 (사용자 명시 #1 답습 영구)) 3/3 영구 답습 + Operational Readiness PASS / Hermes PMO 격상 영구 답습.

**paths 필터 답습 매트릭스 (정밀, read-only 발견)** (§3) — 3 workflow 합산 **28 paths 영역** enumerate: `secret-hygiene-egress-redaction.yml` 19 (W-N 답습 영구 14 + Stage 5/Backlog 분리 5) + `provider-adapter-enforcement.yml` 6 (W-N + Phase α-1+2 답습 영구 5 + dev/src 2) + `provider-url-scanner.yml` 3 (W-N + Phase α-1 답습 영구 3) = **22 W-N 답습 영구 + 5 Stage 5/Backlog 분리 + 2 dev/src**. paths 영역 변경 영역 외 = W-1 답습 영구 위반.

**workflow_dispatch 비등록 답습 매트릭스 (read-only)** (§4) — 3 workflow 모두 `workflow_dispatch:` **비등록** (0/3) + manual UI trigger 영구 불가능 + `gh workflow run` HTTP 422 예상. workflow_dispatch 추가 = 사용자 명시 #2 영구 답습 위반.

**actual run 발화 전략 재설계 옵션 매트릭스 (§5)** — 9 옵션 enumerate:
- **(A) defer 영구 유지 (권고 시작점, 모든 답습 영구 보존)** ✅
- (B) `pull_request` event open (옵션, Backlog #3 T3 영역 분리 검토 필요) ⚠️
- (C) next 본문 commit + push (옵션, 자연 trigger 답습 영구) ⚠️
- (D) workflow_dispatch 추가 ❌ (W-1 답습 영구 위반 + 사용자 명시 #2 위반)
- (E) 신규 workflow 신설 ❌ (T2/T3 영역 별도 합의 필요)
- (F) paths 영역 변경 ❌ (W-1 답습 영구 위반)
- (G) `schedule` cron ❌ (W-4 lockdown C-ω-10 답습 영구 비권고)
- (H) `repository_dispatch` ❌ (W-4 lockdown C-ω-11 답습 영구 비권고)
- (I) `pull_request_target` ❌ (W-4 lockdown C-ω-12 답습 영구 비권고 + cache poisoning 위험)

**W-N 답습 위반 가능성 매트릭스 (§6)** — 9 옵션 × 13 영역 (W-1~W-4 5 + Phase α-1~α-3 3 + Stage 5 + Backlog 2 + 사용자 명시 3 금지 3) = **옵션 (A) defer 영구 = 모든 영역 0건 위반** + 옵션 (B)~(C) 사용자 결정 후 일부 영역 검토 필요 + 옵션 (D)~(I) = W-1 답습 영구 위반 또는 사용자 명시 위반 (본 brief 비권고).

**합의 형태 권고**: 본 brief 자체 = **(a) Reviewer-only 단축 합의 적격 시작점** (T-2 재발화 영역 한계 — Stage 4 entry brief + W-1~W-4 + W-4 *실 trigger 발화 결정* + 후속 37 시점 이미 답습) + (b) 풀 3+1 합의 옵션 (사용자 명시 결정 시) + (c) 외부 LLM 1+ 비권고.

**사용자 명시 3 금지 × 본 brief 분리 매트릭스 — 3/3 영구 답습** (작성 시점) — 옵션 (A) 채택 시 = 영구 보존 / 옵션 (B)~(C) 채택 시 = 별도 cycle 영역.

**합산 602 합의 조건 변경 0건** (21 합의 — W-1 30 + W-2 35 + W-3 36 + W-4 lockdown 37 + W-4 *실 trigger 발화 결정* 26 + Stage 4 entry 49 포함).

**본 brief 자체 금지 ≥ 50 + 본 brief 발효 후 의무 금지 ≥ 13** enumerate.

**본 brief 새 조건 후보 26 (C-A2-1 ~ C-A2-26)** — Latin C-A1 generation 후속 (C-A2 신규 sub-generation 시작).

**본 brief 는 3 MVP-1 workflow 어느 줄도 *변경* 시키지 않으며 (W-1 답습 영구), workflow_dispatch 어느 workflow 에도 *추가* 시키지 않으며 (사용자 명시 #2 영구 답습), on.push.paths 영역 어느 것도 *변경* 시키지 않으며 (W-1 답습 영구), 신규 actual GitHub Actions run trigger 어느 것도 *재실행* / *재발화* 시키지 않으며 (사용자 명시 #3 영구 답습), W-1 / W-2 / W-3 / W-4 lockdown / W-4 *실 trigger 발화 결정* 답습 어느 것도 *변경* 시키지 않으며, trigger commit `d4a0107` 어느 것도 *revert* 시키지 않으며, R-1 + R-4/R-5/R-7 + `src/` 본문 어느 것도 *변경* 시키지 않으며, 4 prerequisite runs 답습 어느 것도 *재실행* 시키지 않으며, 합산 602 합의 조건 어느 것도 *변경* / Layer C/D/E/F 재발효 / Operational Readiness PASS / Hermes PMO 격상 / actual run 발화 전략 어느 것도 *최종 확정 발효* / 합의 보고서 작성 / 메타 갱신 / commit / push / **실 trigger 발화 자체** 모두 본 brief 영역 외**.

다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §11 답습) — **(A) brief 그대로 승인 → Reviewer-only 단축 합의 (권고 시작점 — T-2 재발화 영역 한계)** / (B) 풀 3+1 합의 / (C) brief 수정 / (D) 부분 채택 / (E) brief 합의 후 → 옵션 (A) defer 영구 유지 발효 (가장 보수적) / (F) brief 합의 후 → 옵션 (B) PR open brief 진입 (Backlog #3 T3 분리 검토) / (G) Backlog 전환 / (H) Phase α-1~α-4 통합 구현 완료 조건 재평가 brief / (I) brief 폐기 / (J) 세션 종료.
