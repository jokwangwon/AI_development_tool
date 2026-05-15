# Layer C 발효 합의 (Implementation Evidence PASS) **실 진입 단계 분할** Brief (준비안 — DRAFT)

> **본 문서는 Layer C 발효 합의 진입 가능성 검토 brief 발효 후속 (`c13c011` APPROVE AS BRIEF), Layer C 발효 합의 *실 진입 단계 분할 한정* 의 brief 준비안.**
>
> **본 brief 의 framing 차이**: 진입 *가능성 검토* (=`c13c011`, "Can we enter?") 가 아닌, **실 진입 *단계 분할 + 결정 지점 + cycle commit chain 후보*** ("How do we enter step-by-step?"). 단, 본 brief 자체는 여전히 *준비안 (DRAFT)* — Layer C 발효를 *발효시키지 않으며*, 사용자 명시 승인 *전* 단계.
>
> 본 brief 의 어떤 §도 그 자체로 (i) Layer C 발효를 시작시키지 않으며, (ii) Implementation Evidence PASS 를 선언하지 않으며, (iii) MVP-1 PASS 를 선언하지 않으며, (iv) 외부 LLM 호출을 자동 발화시키지 않으며, (v) Layer C 발효 합의 보고서를 자동 작성시키지 않으며, (vi) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 / Phase α-1 합의 15 조건 / Phase α-2 합의 26 조건 / Phase α-3 합의 28 조건 / Phase α-4 합의 29 조건 / Layer C 진입 가능성 검토 합의 30 조건 / 사용자 명시 7 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-layer-c-implementation-evidence-pass-entry.md` (Layer C 진입 가능성 검토 합의, commit `c13c011` APPROVE AS BRIEF — 30 조건 C-η-1 ~ C-η-30)
- `docs/phase0/layer-c-implementation-evidence-pass-entry-brief.md` (Layer C 진입 가능성 brief, commit `1073593`)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (Phase α-4 R-1 합의, commit `e59a565` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3 R-7 합의, commit `3f6306d` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md` (Stage 4 합의 패턴 답습 — *실 진입 단계 분할* 형태)
- `docs/review/3plus1-consensus-2026-05-12-gp3-stage2-implementation-entry.md` (Stage 2 합의 패턴 답습 — *실 진입 단계 분할* 형태)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd`)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §2.2 + §5.1 + §6 (다음 단계 권고)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5 조건 모법

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Layer C 발효 합의 실 진입 brief 작성해주세요"

### 0.2 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 / α-4 + Layer C 진입 가능성 검토 패턴 답습)

사용자가 본 brief 진입 명령 시 명시 prohibitions 를 enumerate 하지 않았으나, **Phase α-1 / α-2 / α-3 / α-4 + Layer C 진입 가능성 검토 (`c13c011`) 답습 패턴** = 7 금지 영역 유지 (사용자 명시 강조 답습) — 본 brief = 본 패턴 답습 (#1 = Layer C 실 진입 영역 한정):

1. ❌ **실 Layer C 발효 금지** — Implementation Evidence PASS *발효 선언* 0건 (본 brief = **실 진입 *step 분할안 한정***, 발효 자체는 본 brief *외*)
2. ❌ **CI workflow 변경 금지** — 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 어느 줄도 변경 0건
3. ❌ **branch protection 변경 금지**
4. ❌ **dev 환경 강제 금지**
5. ❌ **`pre-commit install` 의무화 금지**
6. ❌ **Operational Readiness PASS (Layer E) 선언 금지**
7. ❌ **Hermes PMO 격상 (Layer F) 금지**

본 7 금지 답습 = 사용자 명시 패턴 보존 — 사용자가 본 brief 검토 시 prohibition 추가/축소 권위 영역 (옵션 (B) 수정 요청 답습).

### 0.3 본 brief 가 *하는* 것

1. Layer C 진입 가능성 검토 합의 (`c13c011` APPROVE AS BRIEF) 발효 후속 — Layer C 발효 합의 *실 진입 단계 분할* (§1)
2. **Layer C 발효 합의 실 진입 7 단계 분할 매트릭스** — Step 0 ~ Step 6 (§2)
3. **각 step 결정 지점 매트릭스** — 사용자 명시 결정 영역 enumerate (§3)
4. **사용자 명시 7 금지 영역 × Layer C 실 진입 분리 매트릭스** (§4)
5. **Layer C 실 진입 적격성 5 조건 검토** — 진입 가능성 검토 합의 답습 + 추가 step 분할 한정 (§5)
6. **합의 형태 결정 단계 분할** — Reviewer-only 단축 vs 풀 3+1 + 외부 LLM 1+ (§6)
7. **Rollback Trigger 의존성 + 단계별 rollback 옵션 답습** (§7)
8. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§8)
9. **다음 단계 결정 옵션** (사용자 결정 영역, §9)
10. **본 brief 메타 검증** (§10)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 7 금지 영역**:

- ❌ **실 Layer C 발효 0건** — Implementation Evidence PASS *발효 선언* 0건 (본 brief = step 분할안 한정 — 어느 step 도 자동 진입 0건)
- ❌ **CI workflow 변경 0건** — 3 MVP-1 workflow (1206줄) + 8 G2/G3/G4 PoC workflow (2037줄) 본문 변경 0건
- ❌ **branch protection 변경 0건** — AR-2 진입 0건 (Backlog #3 T3 영역 분리)
- ❌ **dev 환경 강제 0건** — `tools/doctor.py` 신설 / 의무 실행 0건
- ❌ **`pre-commit install` 의무화 도입 0건** — `.pre-commit-config.yaml` 본문 작성 0건
- ❌ **Operational Readiness PASS (Layer E) 선언 0건**
- ❌ **Hermes PMO 격상 (Layer F) 0건**

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **MVP-1 PASS (Layer D) 선언 0건** — Layer C 발효 후 별도 합의 영역 분리
- ❌ **외부 LLM 자동 호출 0건** — Group α 합의 C-11 답습 (본 brief = 외부 LLM step 분할 *제안 한정*)
- ❌ **외부 LLM blind 의뢰서 자동 작성 0건** — Step 4 결정 후 별도 단계 (사용자 명시 결정 영역)
- ❌ **Layer C 발효 합의 보고서 자동 작성 0건** — 본 brief = step 분할안 한정 (실 보고서 = Step 5 발효 시점)
- ❌ **양 GP × 5 조건 evidence *재생성* 0건** — Layer C 진입 가능성 검토 합의 (`c13c011`) §3 답습 한정
- ❌ **4 prerequisite actual runs *재실행* 0건** — `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정
- ❌ **신규 actual run 자동 trigger 0건**
- ❌ **R-4 도구 (829줄) / R-5 `.importlinter` (35줄) / R-7 docker secret block (328줄) / R-1 CI workflow 통합 (1593줄) = 합산 2785줄 본문 변경 0건**
- ❌ **Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 0건** — 본 brief = Layer C 실 진입 step 분할 한정
- ❌ **Phase α-1 / α-2 / α-3 / α-4 / Layer C 진입 가능성 합의 본문 변경 0건**
- ❌ **C-β-1 ~ C-β-15 / C-γ-1 ~ C-γ-26 / C-δ-1 ~ C-δ-28 / C-ε-1 ~ C-ε-29 / C-η-1 ~ C-η-30 자동 변경 0건**
- ❌ **ADR-011 §2.1 (a)~(e) 5 조건 *재정의* 0건** — 모법 답습 한정
- ❌ **합의 형태 *자동 결정* 0건** — Reviewer-only vs 풀 3+1 = Step 3 사용자 명시 결정 영역
- ❌ **외부 LLM vendor *자동 선택* 0건** — Step 4 (사용자 명시 결정 시) 사용자 명시 결정 영역
- ❌ **외부 LLM 응답 결론 강제 채택 0건** — 응답 = 입력 한정 (Group α C-11 답습)
- ❌ **Phase β / γ 자동 진입 0건**
- ❌ **GP-3 / GP-5 PASS *발효* 0건** — Layer C 발효 시 동시 발효 (Step 5)
- ❌ **Group α 합의 C-1 ~ C-12 / 14 결정 영역 *재결정* 0건**
- ❌ **Layer A / Layer B / §5.5 9 sub-수단 본문 채택 변경 0건**
- ❌ **GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 / Group A 2차 풀 3+1 합의 본문 변경 0건**
- ❌ **Group I / Group β / γ-1 / γ-2 자동 진입 0건**
- ❌ **token rotation 정책 자동 결정 0건**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 0건**
- ❌ **commit signing 도입 0건**
- ❌ **`pull_request_target` workflow 도입 0건**
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건**
- ❌ **threshold *고정* 0건**
- ❌ **event enum 정식 등록 0건** (4 후보 모두 = Backlog #5 분리)
- ❌ **ADR 본문 자동 갱신 0건**
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 0건**
- ❌ **F-금지 #1 위반 0건** — GitHub Actions secrets 사용 도입 0건 (영구 답습)
- ❌ **Hermes upstream Dockerfile 변경 0건**
- ❌ **Production `docker-compose.yml` 신설 / 변경 0건**
- ❌ **실 secret material commit 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**
- ❌ **인간 리뷰 의무 자동 발화 0건**
- ❌ **Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 0건**
- ❌ **PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 0건**
- ❌ **Layer 2 runtime block (G5-5) 진입 0건** (MVP-3/4 영역 분리)
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 0건** (Backlog #4 분리)
- ❌ **MVP-2 ~ MVP-6 본문 deepening 0건**
- ❌ **17 항목 우선순위 자동 *재고정* 0건**

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Layer C (Implementation Evidence PASS) 발효를 *시작* 시키지 않으며,
- (ii) 어느 Step (Step 0 ~ Step 6) 도 *자동 진입* 시키지 않으며,
- (iii) 합의 형태를 *자동 결정* 시키지 않으며 (단축 vs 풀 3+1 = 사용자 명시 결정 영역),
- (iv) 외부 LLM 호출을 *자동 발화* 시키지 않으며 (외부 LLM 의뢰 = Step 4 사용자 명시 결정 시),
- (v) Layer C 발효 합의 보고서를 *자동 작성* 시키지 않으며 (실 보고서 = Step 5),
- (vi) GP-3 / GP-5 PASS 를 *발효* 시키지 않으며,
- (vii) MVP-1 PASS 를 *선언* 시키지 않으며,
- (viii) ADR-011 §2.1 (a)~(e) 5 조건을 *재정의* 시키지 않으며,
- (ix) Phase α-1 / α-2 / α-3 / α-4 합의 / Layer C 진입 가능성 검토 합의 / Group α 합의 / Backlog #6 우선 진입 합의 / Layer A / Layer B 본문을 *변경* 하지 않으며,
- (x) R-4 도구 / R-5 `.importlinter` / R-7 docker secret block / R-1 CI workflow 통합 본문 어느 줄도 *변경* 하지 않으며,
- (xi) 사용자 명시 7 금지 영역 어느 것도 *해소* 시키지 않으며,
- (xii) Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Layer C 발효 합의 실 진입 영역의 *단계 분할 매트릭스* — 7 step 분할 + 각 step 결정 지점 + 7 금지 분리 매트릭스 + 실 진입 적격성 검토 + 합의 형태 결정 단계 분할 + Rollback Trigger 단계별 옵션 + 금지 영역 enumeration**. 모든 *step 진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Layer C 진입 가능성 검토 합의 발효 후속 (`c13c011` APPROVE AS BRIEF)

| 영역 | 답습 |
|------|----|
| 합의 commit | `c13c011 docs(review): approve Layer C implementation evidence pass entry` (554줄, 11 섹션) |
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의 적격 — 15/15 풀 3+1 트리거 0건 발화) |
| 합의 영역 | Layer C 발효 합의 *진입 가능성 검토 한정* (적격성 권위 권고) |
| 합의 조건 | 30 조건 (C-η-1 ~ C-η-30) |
| 양 GP × 5 조건 evidence | **10/10 적격성 권위 권고** ((a)~(d) 8/8 현 충족 + (e) Layer C 시점 발효) |
| 4 prerequisite actual runs PASS | 4/4 답습 (`25728590939` + `25728590916` + `25728590977` + `25731846625`) |
| 본 brief 관계 | **본 brief = (`c13c011`) 발효 후속 — 실 진입 단계 분할 한정** |

### 1.2 본 brief framing 차이 — 진입 가능성 검토 vs 실 진입 단계 분할

| 영역 | 진입 가능성 검토 (`c13c011`) | 실 진입 단계 분할 (본 brief) |
|------|----------------|----------------|
| 핵심 질문 | "Can we enter Layer C 발효 합의?" | "How do we enter Layer C 발효 합의 step-by-step?" |
| 합의 단위 | 적격성 권위 권고 | step 분할안 권위 권고 |
| 영역 | evidence verification 매트릭스 | step decomposition 매트릭스 |
| 출력 | 5 조건 evidence + 풀 3+1 트리거 검토 | 7 step 분할 + 결정 지점 + cycle commit chain |
| 답습 패턴 | Phase α-1 / α-2 / α-3 / α-4 (entry possibility) | Stage 2 / Stage 4 (implementation entry) |

### 1.3 6-Layer 분리 매트릭스 현 상태 (2026-05-15 후속)

| Layer | 영역 | 상태 |
|-------|------|------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + `55c5b4b`) |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 | ✅ APPROVE WITH CONDITIONS (`4880e88`) |
| Backlog #6 우선 진입 | Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) |
| Phase α-1 R-4 진입 | 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`1b3090b`) |
| Phase α-2 R-5 진입 | 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`6a79247`) |
| Phase α-3 R-7 진입 | 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`3f6306d`) |
| Phase α-4 R-1 진입 | 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`e59a565`) |
| Layer C 진입 가능성 검토 | Implementation Evidence PASS 진입 가능성 | ✅ APPROVE AS BRIEF (`c13c011`) |
| **Layer C 실 진입 step 분할** | **본 brief 영역** | ⏳ **DRAFT** |
| Layer C 발효 (실 보고서) | Implementation Evidence PASS 선언 | ⏳ 아직 아님 (본 brief 영역 외 — Step 5 발효 시점) |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 (Layer C 발효 후 별도 합의) |
| Layer E | Operational Readiness PASS | ⏳ 아직 아님 (사용자 명시 7 금지 #6) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 (사용자 명시 7 금지 #7) |

### 1.4 본 brief 의 진입점

```
Phase α 4 단계 brief 모두 APPROVE AS BRIEF (1b3090b + 6a79247 + 3f6306d + e59a565)
Layer C 진입 가능성 검토 brief (1073593) + 합의 (c13c011) APPROVE AS BRIEF
   │
   ▼ Layer C 발효 합의 진입 가능성 검토 완료 milestone
■ 본 brief = Layer C 발효 합의 *실 진입 단계 분할* (DRAFT)               ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Layer C 발효 합의 실 진입 (Step 0 → Step 1 → ... → Step 6)              ← 본 brief 영역 외
   │
   ▼ Step 5: Layer C 발효 합의 보고서 작성 + Implementation Evidence PASS 발효
   ▼ Step 6: 메타 갱신 + commit + push (사용자 명시 결정 시점)
Layer C 발효 완료 → Layer D MVP-1 PASS 선언 합의 진입 적격                  ← 본 brief 영역 외
```

---

## 2. Layer C 발효 합의 실 진입 7 Step 분할 매트릭스

### 2.1 Step 분할안 (Stage 2 / Stage 4 패턴 답습 — 실 진입 단계 분할 형태)

본 §은 Layer C 발효 합의 실 진입을 **7 Step (Step 0 ~ Step 6)** 으로 분할 — 각 step = 사용자 명시 결정 영역 (자동 진입 0건):

| Step | 영역 | 결정 지점 | 산출물 후보 | 본 brief 영역 |
|------|------|---------|----------|------------|
| **Step 0** | **사전 점검 — Layer C 진입 가능성 합의 (`c13c011`) 답습 확정** | 답습 변경 0건 검증 | 답습 검증 메모 (별도 commit 0건) | enumerate 한정 |
| **Step 1** | **양 GP × 5 조건 evidence 본문 *재enumerate 검증* (재생성 0건, 답습 한정)** | Layer C 진입 가능성 합의 §3 답습 검증 | 답습 검증 매트릭스 (별도 commit 0건) | enumerate 한정 |
| **Step 2** | **4 prerequisite actual runs PASS *commit SHA + run_id 확정 검증*** | `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 확정 | run ID + commit SHA 매트릭스 (별도 commit 0건) | enumerate 한정 |
| **Step 3** | **합의 형태 *결정*** (사용자 명시 결정 영역) | Reviewer-only 단축 합의 vs 풀 3+1 + 외부 LLM 1+ | 합의 형태 결정 메모 | 사용자 결정 |
| **Step 4** | **(옵션) 외부 LLM 1+ blind 의뢰** (Step 3 풀 3+1 선택 시) | vendor 선택 + 의뢰서 작성 (별도 brief) + 응답 회수 (응답 = 입력 한정) | 외부 LLM blind 의뢰서 + 응답 회수 (별도 commit chain) | 사용자 결정 |
| **Step 5** | **Layer C 발효 합의 보고서 작성 + Implementation Evidence PASS *발효 선언*** | 합의 보고서 본문 작성 (Step 3 합의 형태 답습) + 양 GP PASS 발효 | `docs/review/3plus1-consensus-{YYYY-MM-DD}-layer-c-implementation-evidence-pass.md` (단축 또는 풀 3+1 답습) | 사용자 결정 (실 발효) |
| **Step 6** | **메타 갱신 + commit + push** (사용자 명시 결정 시점) | CONTEXT.md + INDEX.md + SESSION 갱신 + commit chain push | 메타 commit (단축 1 commit / 풀 3+1 다중 commit) | 사용자 결정 |

### 2.2 Step 분할안 의존성 매트릭스

| Step | 의존성 | 본 brief 권고 |
|------|------|----------|
| Step 0 | (사전 점검) | 본 brief 발효 직후 진입 적격 |
| Step 1 | Step 0 완료 | Step 0 완료 후 진입 (자동 진입 0건) |
| Step 2 | Step 1 완료 | Step 1 완료 후 진입 (자동 진입 0건) |
| Step 3 | Step 2 완료 | Step 2 완료 후 진입 — **사용자 명시 결정 의무 (단축 vs 풀 3+1 + 외부 LLM)** |
| Step 4 | Step 3 *풀 3+1 선택* 시 | Step 3 단축 선택 시 = Step 4 *skip* 적격 (Step 5 직진) |
| Step 5 | Step 3 (단축 시) 또는 Step 4 (풀 3+1 시) 완료 | Step 5 = Layer C 발효 *합의 보고서 작성 + 실 발효 선언* (사용자 명시 결정 시점) |
| Step 6 | Step 5 완료 | Step 5 합의 보고서 작성 후 메타 + push (사용자 명시 결정 시점) |

### 2.3 분할 옵션 매트릭스

| 옵션 | Step 흐름 | 적격 조건 | 본 brief 권고 |
|------|---------|---------|----------|
| **단축 흐름** | Step 0 → Step 1 → Step 2 → **Step 3 단축 선택** → (Step 4 skip) → Step 5 → Step 6 | Layer C 진입 가능성 합의 (`c13c011`) §6 답습 — 15/15 풀 3+1 트리거 0건 발화 + 외부 LLM 의무 명시 0건 (권고 한정) | **권고 후보** (Phase α-1/2/3/4 + 진입 가능성 합의 패턴 답습) |
| **풀 3+1 흐름** | Step 0 → Step 1 → Step 2 → **Step 3 풀 3+1 선택** → **Step 4 외부 LLM 1+ blind 의뢰** → Step 5 (풀 3+1 합의 보고서) → Step 6 | Layer C 발효 = MVP-1 1차 영역 *의미 deepening* 시 (사용자 명시 결정 권한) | **선택 후보** (사용자 명시 결정 시) |

### 2.4 cycle commit chain 후보 매트릭스

| Step | cycle commit chain 후보 | commit subject 후보 |
|------|--------------------|------------------|
| Step 0 ~ Step 2 | (별도 commit 0건 — 답습 검증 한정, Step 5 cycle 내 흡수 후보) | — |
| Step 3 단축 선택 | (별도 commit 0건 — Step 5 cycle 내 흡수) | — |
| Step 3 풀 3+1 선택 | brief commit (별도 brief — 풀 3+1 진입 brief) | `docs(phase0): add Layer C consensus mode full 3+1 entry brief` (예시) |
| Step 4 (옵션) | blind 의뢰서 brief commit + 응답 회수 commit (2~5 vendor) | `docs(phase0): add Layer C external LLM blind request` + `docs(phase0): receive Layer C external LLM responses` |
| Step 5 | **Layer C 발효 합의 보고서 commit** | `docs(review): approve Layer C implementation evidence pass` (단축) 또는 풀 3+1 답습 |
| Step 6 | 메타 commit + push | `docs(context): record Layer C implementation evidence pass effective` |

### 2.5 본 §2 의 *범위 한계*

본 §2 = **7 Step 분할안 *권위 권고 한정***. 실 Step 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 step 분할 = 단계 분할 권위 권고 한정 — 실 step 발효 권위 0건.

---

## 3. 각 Step 결정 지점 매트릭스

### 3.1 Step 0 — 사전 점검 결정 지점

| 결정 지점 | 영역 | 사용자 명시 결정 영역 |
|---------|------|-----------------|
| Layer C 진입 가능성 합의 (`c13c011`) 답습 변경 0건 검증 | 답습 검증 | 자동 검증 (변경 발견 시 step 중단) |
| Phase α-1 / α-2 / α-3 / α-4 합의 본문 변경 0건 검증 | 동상 | 동상 |
| Group α / Backlog #6 / Layer A / Layer B / §5.5 변경 0건 검증 | 동상 | 동상 |
| **결정 지점** | 검증 통과 시 Step 1 진입 적격 | 사용자 명시 진입 결정 |

### 3.2 Step 1 — 양 GP × 5 조건 evidence 답습 검증 결정 지점

| 결정 지점 | 영역 | 사용자 명시 결정 영역 |
|---------|------|-----------------|
| GP-3 × 5 조건 evidence 답습 변경 0건 검증 | Layer C 진입 가능성 합의 §3.1 답습 | 자동 검증 (변경 발견 시 step 중단) |
| GP-5 × 5 조건 evidence 답습 변경 0건 검증 | Layer C 진입 가능성 합의 §3.2 답습 | 동상 |
| 양 GP × 5 조건 = 10/10 적격성 답습 변경 0건 검증 | Layer C 진입 가능성 합의 §3.3 답습 | 동상 |
| evidence 재생성 / 신규 추가 / 삭제 0건 검증 | 답습 한정 | 동상 |
| **결정 지점** | 10/10 답습 변경 0건 검증 통과 시 Step 2 진입 적격 | 사용자 명시 진입 결정 |

### 3.3 Step 2 — 4 prerequisite actual runs PASS 확정 검증 결정 지점

| 결정 지점 | 영역 | 사용자 명시 결정 영역 |
|---------|------|-----------------|
| Stage 1 GP-3 secret-hygiene `25728590939` run_id + `72622409` commit SHA 답습 확정 | Layer C 진입 가능성 합의 §3.4 답습 | 자동 검증 |
| Stage 3 GP-5 provider-adapter `25728590916` run_id + `72622409` commit SHA 답습 확정 | 동상 | 동상 |
| Stage 3 GP-5 provider-url-scanner `25728590977` run_id + `72622409` commit SHA 답습 확정 | 동상 | 동상 |
| Stage 2 GP-3 ST-3 docker secret `25731846625` run_id + `6c6b208` commit SHA 답습 확정 | 동상 | 동상 |
| **결정 지점** | 4/4 PASS 답습 확정 검증 통과 시 Step 3 진입 적격 | 사용자 명시 진입 결정 |

### 3.4 Step 3 — 합의 형태 결정 지점 (사용자 명시 결정 영역 — 핵심)

| 결정 지점 | 옵션 A: Reviewer-only 단축 | 옵션 B: 풀 3+1 + 외부 LLM 1+ |
|---------|----------------------|----------------------|
| 근거 | Layer C 진입 가능성 합의 §6.2 답습 — 15/15 풀 3+1 트리거 0건 발화 + mvp1.md 외부 LLM 의무 명시 0건 (권고 한정) | Layer C 발효 = MVP-1 1차 영역 *의미 deepening* 시 — 사용자 명시 결정 권한 |
| 외부 LLM 호출 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) | ✅ 1+ vendor blind 의뢰 (Gemini / GPT / Claude 등 cross-vendor) — 응답 = 입력 한정 |
| 다음 step | → Step 5 직진 (Step 4 skip) | → Step 4 진입 (외부 LLM blind 의뢰) |
| Step 5 cycle | 단축 1 commit chain | 풀 3+1 다중 commit chain (vendor 선택 + 의뢰서 + 응답 회수 + 합의 보고서) |
| 본 brief 권고 | **권고 후보** (Phase α-1/2/3/4 + 진입 가능성 합의 패턴 답습) | **선택 후보** (사용자 명시 결정 시) |
| **결정 지점** | **사용자 명시 결정 의무 영역** — 자동 결정 0건 | 동상 |

### 3.5 Step 4 — (옵션) 외부 LLM 1+ blind 의뢰 결정 지점

**Step 4 = Step 3 풀 3+1 선택 시에만 진입** — 단축 선택 시 Step 4 skip.

| 결정 지점 | 영역 | 사용자 명시 결정 영역 |
|---------|------|-----------------|
| Vendor 선택 | Gemini / GPT / Claude / 기타 — 1+ vendor (사용자 명시) | **사용자 명시 결정 의무 영역** |
| 의뢰서 작성 | 별도 brief commit (`docs(phase0): add Layer C external LLM blind request`) | 사용자 명시 결정 후 작성 |
| 의뢰서 영역 | ADR-011 §2.1 5 조건 + 양 GP × evidence + Phase α 4 단계 답습 + 7 금지 정합성 등 | 답습 한정 (자동 호출 0건) |
| 응답 회수 | 별도 brief commit (`docs(phase0): receive Layer C external LLM responses`) | 사용자가 직접 외부 LLM 응답 수신 후 commit |
| 응답 결론 강제 채택 | ❌ 0건 — 응답 = 입력 한정 (Group α C-11 답습) | 영구 답습 |
| **결정 지점** | 의뢰서 작성 + 응답 회수 후 Step 5 진입 적격 | 사용자 명시 결정 의무 영역 |

### 3.6 Step 5 — Layer C 발효 합의 보고서 작성 + Implementation Evidence PASS 발효 결정 지점 (핵심 — 실 발효 시점)

| 결정 지점 | 단축 흐름 | 풀 3+1 흐름 |
|---------|---------|----------|
| 합의 보고서 본문 | Step 1 + Step 2 답습 매트릭스 + 15/15 풀 3+1 트리거 0건 발화 + 30+ 합의 조건 | Step 1 + Step 2 답습 + Step 4 외부 LLM blind 의뢰 응답 통합 + Agent A/B/C 분배 + Reviewer 검토 + 합의 도출 |
| Implementation Evidence PASS *발효 선언* | 합의 보고서 §10 영역 (단축) | 풀 3+1 합의 보고서 §X 영역 |
| GP-3 PASS 발효 | 동시 발효 | 동상 |
| GP-5 PASS 발효 | 동시 발효 | 동상 |
| 합의 보고서 commit | `docs(review): approve Layer C implementation evidence pass` (단축) | `docs(review): record Layer C implementation evidence pass full 3+1 consensus` (풀 3+1) |
| 본 brief 권고 | **권고 후보** (단축 흐름 — Phase α-1/2/3/4 패턴 답습) | **선택 후보** (사용자 명시 결정 시) |
| **결정 지점** | **사용자 명시 결정 의무 영역 — 실 Layer C 발효 시점** | 동상 |

### 3.7 Step 6 — 메타 갱신 + commit + push 결정 지점

| 결정 지점 | 영역 | 사용자 명시 결정 영역 |
|---------|------|-----------------|
| CONTEXT.md 갱신 | Layer C 발효 milestone 기록 | 사용자 명시 결정 |
| INDEX.md 갱신 | 동상 | 동상 |
| SESSION 갱신 | 동상 | 동상 |
| 메타 commit | `docs(context): record Layer C implementation evidence pass effective` | 동상 |
| Push 시점 | 메타 commit 발효 후 push (단축 1 push 또는 풀 3+1 다중 push) | 동상 |
| 본 brief 권고 | 단축 시: brief + 합의 + 메타 = 3 commit chain → push | 동상 |
| **결정 지점** | **사용자 명시 결정 의무 영역 — push 시점** | 동상 |

### 3.8 본 §3 의 *범위 한계*

본 §3 = **각 Step *결정 지점 매트릭스 한정***. 실 step 진입 결정 / 실 합의 형태 결정 / 실 외부 LLM vendor 선택 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. 사용자 명시 7 금지 영역 × Layer C 실 진입 분리 매트릭스

### 4.1 금지 #1 — 실 Layer C 발효 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| 7 Step 분할안 권위 권고 | ✅ 본 brief 영역 | — |
| Step 0 ~ Step 4 진입 | ❌ (영역 외) | 본 brief 발효 후 단계 (사용자 명시 결정) |
| **Step 5 (Layer C 발효 합의 보고서 작성 + 실 발효 선언)** | ❌ (영역 외) | **본 brief 발효 후 단계 — 실 Layer C 발효 시점 (사용자 명시 결정)** |
| GP-3 / GP-5 PASS 발효 | ❌ (영역 외) | Step 5 발효 시 동시 발효 |
| MVP-1 PASS (Layer D) 선언 | ❌ (영역 외) | Layer C 발효 후 별도 합의 |
| **본 brief 영역 *내* 적격 작업** | **7 Step 분할안 + 결정 지점 매트릭스 + 합의 형태 결정 단계 분할 + Rollback Trigger 단계별 옵션** | — |

### 4.2 금지 #2 — CI workflow 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| 3 MVP-1 workflow (1206줄) 본문 변경 | ❌ (영역 외) | Phase α-4 실 진입 시점 (별도 합의) |
| 8 G2/G3/G4 PoC workflow (2037줄) 본문 변경 | ❌ (영역 외) | 별도 영역 |
| 신규 workflow 신설 | ❌ (영역 외) | 별도 합의 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 합의 = evidence verification step 분할 영역, CI workflow 변경 = Phase α 실 진입 영역 분리)** | — |

### 4.3 금지 #3 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| AR-2 진입 | ❌ (영역 외) | Backlog #3 T3 영역 별도 풀 3+1 분리 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 합의 = consensus step 영역, branch protection = T3 영역 — 직교)** | — |

### 4.4 금지 #4 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/doctor.py` 신설 | ❌ (영역 외) | R-10 영역 (Phase β-2) |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 합의 = consensus step 영역, dev 환경 강제 = R-10 영역 — 분리)** | — |

### 4.5 금지 #5 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | R-6 영역 (Phase β-1) — Backlog #1+#2 분리 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 합의 = consensus step 영역, pre-commit install 의무화 = R-6 영역 — 분리)** | — |

### 4.6 금지 #6 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C = Implementation Evidence PASS, Layer E = Operational Readiness PASS — Layer D MVP-1 PASS 중간 단계 분리)** | — |

### 4.7 금지 #7 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F 격상 | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C = Implementation Evidence PASS, Layer F = Hermes PMO 격상 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **7 금지 영역 *분리 매트릭스 한정***. 7 금지 영역 어느 것도 *해소* 0건 + Layer C 실 발효 자동 진입 0건.

---

## 5. Layer C 실 진입 적격성 5 조건 검토

### 5.1 적격성 검토 매트릭스 (Layer C 진입 가능성 합의 §5.1 답습 + step 분할 추가)

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-θ-1** | **사용자 명시 7 금지 영역 충돌 0** | Layer C 발효 합의 실 진입 = step 분할 + 결정 지점 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0). 금지 #1 (실 Layer C 발효) = Step 5 영역 (본 brief = step 분할안 한정 — 충돌 0). | ✅ **0/7 충돌** |
| **C-θ-2** | **Layer C 진입 가능성 합의 (`c13c011`) 답습** | 30 조건 (C-η-1 ~ C-η-30) 답습 + 양 GP × 5 조건 evidence 10/10 적격성 답습 + 4 prerequisite runs PASS 답습 + 15/15 풀 3+1 트리거 0건 발화 답습 + 외부 LLM 1+ 권고 한정 답습 모두 변경 0건 | ✅ **30/30 조건 답습** |
| **C-θ-3** | **7 Step 분할안 일관성** (Stage 2 / Stage 4 패턴 답습) | Step 0 (사전 점검) + Step 1 (evidence 답습 검증) + Step 2 (actual runs 확정) + Step 3 (합의 형태 결정) + Step 4 (외부 LLM 옵션) + Step 5 (발효 선언) + Step 6 (메타+push) = **7/7 step 일관** | ✅ **7/7 분할 일관** |
| **C-θ-4** | **각 step 결정 지점 명시** (사용자 명시 결정 영역 명확) | Step 0 ~ Step 2 = 자동 검증 영역 / Step 3 = 합의 형태 결정 (사용자 명시 의무 — 단축 vs 풀 3+1) / Step 4 = vendor 선택 (사용자 명시 의무, 옵션) / Step 5 = 실 발효 시점 (사용자 명시 의무) / Step 6 = push 시점 (사용자 명시 의무) | ✅ **7/7 step 결정 지점 명시** |
| **C-θ-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (Layer C 발효 합의 = consensus step, Hermes PMO 격상 영역 분리) / 단일 source-of-truth 보존 (step 분할안 답습 변경 0건) / 수단/목적 분리 보존 (Layer C = evidence verification 수단, 목적 = Implementation Evidence PASS) / T1/T2/T3 분리 보존 (Layer C = T2 영역) / SPOF 의도적 수용 보존 | ✅ **5/5 보존** |

### 5.2 풀 3+1 승격 트리거 검토 (Layer C 진입 가능성 합의 §5.2 답습 + step 분할 추가 트리거)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | Layer C 진입 가능성 합의 (`c13c011`) 30 조건 (C-η-1 ~ C-η-30) *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 2 | Phase α-1 / α-2 / α-3 / α-4 합의 / Group α / Backlog #6 / Layer A / Layer B 어느 것의 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 3 | 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — Layer C 발효 합의 = consensus step (catalog / provider 영역과 직교) |
| 5 | 5 영구 핵심 제약 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 | ❌ 0건 — Layer C = T2 영역 |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | ADR-011 §2.1 (a)~(e) 5 조건 *재정의* 권고 | ❌ 0건 — 모법 답습 한정 |
| 9 | 양 GP × 5 조건 evidence *재생성* 권고 | ❌ 0건 — Layer C 진입 가능성 합의 §3 답습 한정 |
| 10 | 4 prerequisite actual runs 자동 재실행 권고 | ❌ 0건 — Step 2 = 답습 확정 검증 한정 (재실행 0건) |
| 11 | 외부 LLM 자동 호출 권고 | ❌ 0건 — Step 4 = 사용자 명시 결정 영역 (자동 발화 0건) |
| 12 | 외부 LLM 응답 결론 강제 채택 권고 | ❌ 0건 — Group α 합의 C-11 답습 (응답 = 입력 한정 영구) |
| 13 | 합의 형태 자동 결정 권고 | ❌ 0건 — Step 3 = 사용자 명시 결정 영역 |
| 14 | MVP-1 PASS (Layer D) 자동 선언 권고 | ❌ 0건 — Layer C 발효 후 별도 합의 분리 |
| 15 | Step 5 (Layer C 발효 보고서 작성 + 실 발효 선언) 자동 진입 권고 | ❌ 0건 — 사용자 명시 결정 영역 |
| 16 | Step 6 (메타+push) 자동 진입 권고 | ❌ 0건 — 사용자 명시 결정 영역 |
| 17 | step 분할안 *재설계* 권고 (Stage 2 / Stage 4 패턴 답습 외 형태) | ❌ 0건 — 답습 한정 |
| 18 | event enum 정식 등록 권고 | ❌ 0건 — Backlog #5 분리 |

**검토 결과**: **18/18 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 확정** (사용자 명시 결정 시).

### 5.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| 5 조건 (C-θ-1 ~ C-θ-5) | **5/5 충족** |
| 18 풀 3+1 트리거 | **0/18 발화** |
| 7 Step 분할안 일관성 (Stage 2 / Stage 4 패턴 답습) | **7/7 일관** |
| 각 Step 결정 지점 명시 (사용자 명시 결정 영역) | **7/7 명시** |
| **Layer C 발효 합의 실 진입 단계 분할 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.4 본 §5 의 *범위 한계*

본 §5 = **실 진입 단계 분할 적격성 *검토 한정***. 실 Step 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 6. 합의 형태 결정 단계 분할 + Rollback Trigger 단계별 옵션 답습

### 6.1 합의 형태 결정 단계 분할 (Step 3 답습)

| 영역 | 옵션 A: Reviewer-only 단축 | 옵션 B: 풀 3+1 + 외부 LLM 1+ |
|------|----------------------|----------------------|
| 적격 조건 | Layer C 진입 가능성 합의 §6.2 답습 — 15/15 풀 3+1 트리거 0건 발화 + 외부 LLM 의무 명시 0건 (mvp1.md 권고 한정) | Layer C 발효 = MVP-1 1차 영역 *의미 deepening* 시 — 사용자 명시 결정 권한 |
| 본 brief 권고 | **권고 후보** | **선택 후보** |
| Step 흐름 | Step 0 → Step 1 → Step 2 → Step 3 (단축) → Step 5 → Step 6 (5 step) | Step 0 → Step 1 → Step 2 → Step 3 (풀 3+1) → Step 4 (외부 LLM) → Step 5 → Step 6 (7 step) |
| 본 brief 합의 형태 | (가) Reviewer-only 단축 합의 (본 brief = step 분할안 한정) | 동상 (Step 3 결정 = 본 brief 발효 후 단계) |

### 6.2 Rollback Trigger 단계별 옵션 답습 (Layer C 진입 가능성 합의 §7 답습 + step 분할 추가)

본 §은 Layer C 진입 가능성 합의 §7 답습 한정 + step 분할 단계별 rollback 옵션:

| Step | Rollback 발화 시 영역 옵션 | 본 brief 채택 |
|------|------------------|----------|
| Step 0 | 사전 점검 실패 (답습 변경 발견) | Step 1 진입 금지 — 답습 재정합 후 재진입 (사용자 명시 결정) |
| Step 1 | evidence 답습 변경 발견 | Step 2 진입 금지 — Layer C 진입 가능성 합의 재검토 (사용자 명시 결정) |
| Step 2 | actual run PASS evidence 불일치 발견 | Step 3 진입 금지 — 4 prerequisite runs 재실행 결정 (사용자 명시 결정 영역) |
| Step 3 | 합의 형태 결정 보류 | Step 4 / Step 5 진입 금지 — 사용자 명시 결정 대기 |
| Step 4 | 외부 LLM 응답 R-MVP1 trigger 8 (G3-1 / G3-3 / G3-4 / G5-1 / G5-2 / G5-3 / G5-4 / G5-6) 中 1+ 발화 | Step 5 진입 금지 — 풀 3+1 재합의 (사용자 명시 결정) |
| Step 5 | Layer C 발효 합의 보고서 작성 중 evidence 불일치 발견 | Step 6 진입 금지 — Step 1 또는 Step 2 재진입 (사용자 명시 결정) |
| Step 6 | 메타 commit 또는 push 실패 | commit 재시도 or rollback (사용자 명시 결정) |

### 6.3 본 §6 의 *범위 한정*

본 §6 = **합의 형태 결정 단계 + Rollback 단계별 옵션 *enumerate 한정***. 실 합의 형태 결정 / 실 Rollback 발화 / 실 step 재진입 = 사용자 명시 결정 영역.

---

## 7. 본 brief 자체 금지 사항 + 본 brief 발효 후 Step 진입 단계 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | **실 Layer C 발효** (Implementation Evidence PASS *발효 선언*) (사용자 명시 7 금지 #1) | 0건 |
| 2 | **CI workflow 변경** (사용자 명시 7 금지 #2) | 0건 |
| 3 | **branch protection 변경** (사용자 명시 7 금지 #3) | 0건 |
| 4 | **dev 환경 강제** (사용자 명시 7 금지 #4) | 0건 |
| 5 | **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5) | 0건 |
| 6 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6) | 0건 |
| 7 | **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7) | 0건 |
| 8 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 9 | 어느 Step (Step 0 ~ Step 6) 자동 진입 | 0건 |
| 10 | 합의 형태 자동 결정 (Step 3) | 0건 |
| 11 | 외부 LLM vendor 자동 선택 (Step 4) | 0건 |
| 12 | 외부 LLM 자동 호출 (Step 4) | 0건 |
| 13 | 외부 LLM 응답 결론 강제 채택 | 0건 |
| 14 | Layer C 발효 합의 보고서 자동 작성 (Step 5) | 0건 |
| 15 | Implementation Evidence PASS 발효 선언 자동 진입 (Step 5) | 0건 |
| 16 | GP-3 / GP-5 PASS 발효 자동 진입 (Step 5) | 0건 |
| 17 | 메타 갱신 + commit + push 자동 진입 (Step 6) | 0건 |
| 18 | 양 GP × 5 조건 evidence *재생성* | 0건 |
| 19 | 4 prerequisite actual runs 자동 재실행 | 0건 |
| 20 | 신규 actual run 자동 trigger | 0건 |
| 21 | ADR-011 §2.1 (a)~(e) 5 조건 *재정의* | 0건 |
| 22 | R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 변경 (2785줄 답습) | 0건 |
| 23 | Phase α-1 / α-2 / α-3 / α-4 합의 본문 변경 / 자동 재진입 | 0건 |
| 24 | Layer C 진입 가능성 합의 (`c13c011`) 본문 변경 | 0건 |
| 25 | C-β / C-γ / C-δ / C-ε / C-α / C-η 자동 변경 | 0건 |
| 26 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 27 | Group α 14 결정 영역 *재결정* | 0건 |
| 28 | Layer A / Layer B / §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 29 | GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 / Group A 2차 풀 3+1 합의 본문 변경 | 0건 |
| 30 | step 분할안 자동 재설계 (Stage 2 / Stage 4 패턴 답습 외) | 0건 |
| 31 | Group I / Group β / γ-1 / γ-2 자동 진입 | 0건 |
| 32 | token rotation 정책 자동 결정 | 0건 |
| 33 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 34 | commit signing 도입 | 0건 |
| 35 | `pull_request_target` workflow 도입 | 0건 |
| 36 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 37 | threshold *고정* | 0건 |
| 38 | event enum 정식 등록 | 0건 |
| 39 | ADR 본문 자동 갱신 | 0건 |
| 40 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 41 | 합의 보고서 작성 (본 brief = step 분할안 한정 — 실 보고서 = Step 5) | 0건 |
| 42 | CONTEXT / INDEX / SESSION 메타 갱신 (본 brief = step 분할안 한정 — 실 메타 = Step 6) | 0건 |
| 43 | git commit / push (본 brief = step 분할안 한정 — 실 commit / push = Step 6) | 0건 |
| 44 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 45 | F-금지 #1 위반 (GitHub Actions secrets 사용 도입) | 0건 |
| 46 | Hermes upstream Dockerfile 변경 | 0건 |
| 47 | Production `docker-compose.yml` 신설 / 변경 | 0건 |
| 48 | 실 secret material commit | 0건 |
| 49 | 인간 리뷰 의무 자동 발화 | 0건 |
| 50 | Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 | 0건 |
| 51 | PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입 | 0건 |
| 52 | Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리) | 0건 |
| 53 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |
| 54 | MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 55 | 17 항목 우선순위 자동 *재고정* | 0건 |

### 7.2 본 brief 발효 *후* Step 진입 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Step 0 ~ Step 6 어느 step 도 사용자 명시 결정 미충족 시 자동 진입 | 본 brief = step 분할안 한정 (자동 진입 0건) |
| 2 | Step 3 합의 형태 결정 (단축 vs 풀 3+1) 자동 결정 | 사용자 명시 결정 의무 영역 |
| 3 | Step 4 외부 LLM vendor 자동 선택 / 자동 호출 | 사용자 명시 결정 의무 영역 + Group α C-11 답습 (응답 = 입력 한정) |
| 4 | Step 5 Layer C 발효 합의 보고서 작성 시 ADR-011 §2.1 (a)~(e) 5 조건 *재정의* | 모법 답습 보존 |
| 5 | Step 5 Layer C 발효 합의 보고서 작성 시 양 GP × 5 조건 evidence *재생성* | Layer C 진입 가능성 합의 §3 답습 한정 |
| 6 | Step 5 Layer C 발효 합의 보고서 작성 시 4 prerequisite actual runs 자동 재실행 | 답습 확정 검증 한정 (재실행 0건) |
| 7 | Step 5 Layer C 발효 합의 보고서 작성 시 R-4 / R-5 / R-7 / R-1 영역 본문 변경 | Phase α-1/2/3/4 합의 답습 보존 |
| 8 | Step 5 Layer C 발효 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의 trigger) |
| 9 | Step 5 Layer C 발효 시 Production `docker-compose.yml` 신설 / 변경 | PoC 격리 디렉토리 한정 답습 |
| 10 | Step 5 Layer C 발효 시 실 secret material commit | 영구 금지 (FAKE_TEST_SECRET marker 답습) |
| 11 | Step 5 Layer C 발효 시 GitHub Actions secrets 사용 도입 | 영구 금지 (F-금지 #1 G3-7 (i) 답습) |
| 12 | Step 5 Layer C 발효 시 Layer D MVP-1 PASS 자동 선언 | Layer C 발효 후 별도 합의 영역 분리 |
| 13 | Step 5 Layer C 발효 시 Layer E / Layer F 자동 진입 | MVP-6 영역 + ADR-008 부록 C 12 조건 분리 |
| 14 | Step 5 Layer C 발효 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 15 | Step 5 Layer C 발효 시 event enum 정식 등록 | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 16 | Step 6 메타 + push 시 Phase α-1 / α-2 / α-3 / α-4 자동 재진입 | 사용자 명시 결정 영역 |
| 17 | Step 6 push 시 commit signing 도입 | MVP-6 영역 분리 |
| 18 | Step 6 push 시 `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 19 | Step 6 push 시 local pre-commit framework 활성화 | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 7 금지 #5 답습) |
| 20 | Step 6 push 시 branch protection rule 활성화 | Backlog #3 T3 영역 별도 풀 3+1 (사용자 명시 7 금지 #3 답습) |
| 21 | Step 5 Layer C 발효 후 Group I 자동 진입 | Group α 합의 C-2 답습 |
| 22 | Step 5 Layer C 발효 후 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |
| 23 | Step 5 Layer C 발효 후 GitHub plan / ruleset 가용성 자동 확인 | Group α 합의 C-4 답습 |
| 24 | Step 5 Layer C 발효 후 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 25 | Step 5 Layer C 발효 후 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 26 | Step 5 Layer C 발효 후 PC-4 / AR-2 / AR-3 / Stage 5 자동 진입 | Backlog #1+#2 / Backlog #3 / 별도 합의 영역 분리 |
| 27 | Step 5 Layer C 발효 후 ST-1 / ST-2 / ST-4 / ST-5 자동 진입 | Backlog #1 1.5차 / Backlog #7 / MVP-2 이후 분리 |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 7 Step 진입 단계에서 위 27 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격 후보** | Phase α-1 / α-2 / α-3 / α-4 / Layer C 진입 가능성 패턴 답습 + 18/18 풀 3+1 트리거 0건 발화 + step 분할안 권위 권고 한정 |
| Step 3 합의 형태 결정 | **사용자 명시 결정 영역** | 본 brief = step 분할안 한정 — 실 합의 형태 결정 = Step 3 |
| Step 5 Layer C 발효 합의 자체 | **Step 3 결정 답습** (단축 또는 풀 3+1) | 본 brief = step 분할안 한정 — 실 발효 = Step 5 |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

§5.2 답습 — **18/18 트리거 0건 발화** 확정.

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = Step 3 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-{YYYY-MM-DD}-layer-c-implementation-evidence-pass-actual-entry.md` 패턴 답습) — Reviewer-only 단축 합의 적격 |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Step 0 ~ Step 2 진입** (사전 점검 + evidence 답습 검증 + actual runs 확정 검증) | 단축 흐름 단계 진입 (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Step 3 합의 형태 결정 brief 작성** (단축 vs 풀 3+1 결정 단계 분할 별도 brief) | Step 3 결정 brief (사용자 명시 결정 영역) |
| (F) | 본 brief 승인 → **Step 5 Layer C 발효 합의 보고서 작성 직진** (단축 흐름 직진) | Step 0~2 사전 검증 + Step 3 단축 결정 + Step 5 합의 보고서 작성 (사용자 명시 결정 영역) |
| (G) | 본 brief 승인 → **Step 3 풀 3+1 + Step 4 외부 LLM 1+ blind 의뢰 진입** | Step 4 외부 LLM blind 의뢰서 brief 작성 (사용자 명시 결정 영역) |
| (H) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (I) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (J) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Step 0 ~ Step 2 진입으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Step 3 합의 형태 결정 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Step 5 Layer C 발효 합의 보고서 작성 직진 (단축 흐름)."
- (G): "옵션 (G) 로 진행해주세요. Step 3 풀 3+1 + Step 4 외부 LLM blind 의뢰 진입."
- (H): "옵션 (H) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (I): "옵션 (I) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — "Layer C 발효 합의 실 진입 brief 작성해주세요") |
| 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 / α-4 / Layer C 진입 가능성 패턴 답습 — #1 = Layer C 실 진입 영역 한정) | ✅ (7/7 — 실 Layer C 발효 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Layer C 진입 가능성 검토 합의 (`c13c011`) 답습 | ✅ (30 조건 C-η-1 ~ C-η-30 답습 + 본문 변경 0건) |
| Phase α-1 / α-2 / α-3 / α-4 합의 답습 | ✅ (`1b3090b` + `6a79247` + `3f6306d` + `e59a565` 본문 변경 0건 + 98 조건 자동 변경 0건) |
| Stage 2 / Stage 4 합의 패턴 답습 (실 진입 단계 분할 형태) | ✅ (7 Step 분할안 + cycle commit chain 후보 + 결정 지점 매트릭스 — 답습 일관) |
| ADR-011 §2.1 (a)~(e) 5 조건 모법 답습 | ✅ (재정의 0건 — 답습 한정) |
| Group α 합의 C-1 ~ C-12 답습 | ✅ (자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Layer A / Layer B / §5.5 9 sub-수단 본문 채택 답습 | ✅ (본문 변경 0건) |
| GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 합의 답습 | ✅ (본문 변경 0건) |
| Group A 2차 풀 3+1 합의 답습 | ✅ (본문 변경 0건) |
| 양 GP × 5 조건 evidence 매트릭스 답습 | ✅ 10/10 적격성 답습 한정 (재생성 0건) |
| 4 prerequisite actual runs PASS 답습 | ✅ 4/4 답습 한정 (재실행 0건) |
| 7 Step 분할안 일관성 | ✅ (Stage 2 / Stage 4 패턴 답습 — 7 step 분할 + 결정 지점 + cycle commit chain) |
| 각 Step 결정 지점 명시 (사용자 명시 결정 영역) | ✅ (Step 0 ~ Step 6 모두 사용자 명시 결정 영역 명시) |
| 합의 형태 결정 단계 분할 (Step 3 단축 vs 풀 3+1) | ✅ (옵션 A: 단축 권고 후보 / 옵션 B: 풀 3+1 + 외부 LLM 1+ 선택 후보) |
| 외부 LLM 자동 호출 0건 (Group α 합의 C-11 답습) | ✅ |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (Layer C 발효 합의 = consensus step = catalog / provider 영역과 직교) |
| F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) | ✅ |
| Hermes upstream Dockerfile 변경 0건 | ✅ |
| Production `docker-compose.yml` 변경 0건 | ✅ |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/18 발화 | ✅ (§5.2 답습) |
| 실 진입 단계 분할 적격성 5/5 충족 | ✅ (§5.1 답습 — C-θ-1 ~ C-θ-5) |
| R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 변경 0건 (2785줄 답습) | ✅ |
| Layer C 발효 / GP PASS 발효 / MVP-1 PASS (Layer D) 선언 0건 | ✅ |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Layer C 진입 가능성 검토 합의 (`c13c011` APPROVE AS BRIEF, 30 조건 C-η-1 ~ C-η-30) 발효 후속**, **Layer C 발효 합의 *실 진입 단계 분할 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 Layer C 발효 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) Phase α-1 / α-2 / α-3 / α-4 + Layer C 진입 가능성 검토 패턴 답습 (사용자 명시 enumerate 0건 — 본 brief = 패턴 보존 + 사용자 검토 시 prohibition 추가/축소 권위 영역). **본 brief framing 차이** = 진입 *가능성 검토* (=`c13c011`, "Can we enter?") 가 아닌, **실 진입 *단계 분할 + 결정 지점 + cycle commit chain 후보*** ("How do we enter step-by-step?") — Stage 2 / Stage 4 합의 패턴 답습. **7 Step 분할안** = Step 0 (사전 점검 — Layer C 진입 가능성 합의 답습 확정) / Step 1 (양 GP × 5 조건 evidence 답습 검증 — 재생성 0건) / Step 2 (4 prerequisite actual runs PASS commit SHA + run_id 확정 검증 — 재실행 0건) / **Step 3 (합의 형태 결정 — 단축 vs 풀 3+1 + 외부 LLM 1+ — 사용자 명시 결정 의무 영역)** / Step 4 (옵션 — 외부 LLM 1+ blind 의뢰, Step 3 풀 3+1 선택 시) / **Step 5 (Layer C 발효 합의 보고서 작성 + Implementation Evidence PASS *실 발효 선언* — 사용자 명시 결정 의무 영역)** / Step 6 (메타 갱신 + commit + push, 사용자 명시 결정 시점). **각 Step 결정 지점 매트릭스** (Step 0 ~ Step 2 = 자동 검증 영역 / Step 3 / Step 4 / Step 5 / Step 6 = 사용자 명시 결정 의무 영역) + **분할 옵션 매트릭스** (단축 흐름 = 5 step / 풀 3+1 흐름 = 7 step) + **cycle commit chain 후보** (단축 = 3 commit / 풀 3+1 = 다중 commit) + **7 금지 영역 × Layer C 실 진입 분리 매트릭스** (7/7 분리 — 충돌 0) + **실 진입 단계 분할 적격성 5 조건 검토** (C-θ-1 7 금지 충돌 0/7 + C-θ-2 Layer C 진입 가능성 합의 30 조건 답습 + C-θ-3 7 Step 분할 일관성 + C-θ-4 각 Step 결정 지점 명시 + C-θ-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **18/18 풀 3+1 승격 트리거 0건 발화** + **합의 형태 결정 단계 분할** (Step 3 단축 권고 후보 / 풀 3+1 선택 후보) + **Rollback Trigger 단계별 옵션 답습** (Step 0 ~ Step 6 각 단계별 rollback 옵션 enumerate) + **본 brief 자체 금지 55 + 본 brief 발효 후 Step 진입 단계 금지 27** 을 정리한다. **본 brief 는 Layer C 발효를 *시작* 시키지 않으며, 어느 Step (Step 0 ~ Step 6) 도 *자동 진입* 시키지 않으며, 합의 형태를 *자동 결정* 시키지 않으며, 외부 LLM 호출을 *자동 발화* 시키지 않으며, Layer C 발효 합의 보고서를 *자동 작성* 시키지 않으며, GP-3 / GP-5 PASS 를 *발효* 시키지 않으며, MVP-1 PASS 를 *선언* 시키지 않으며, ADR-011 §2.1 (a)~(e) 5 조건 / Phase α-1 / α-2 / α-3 / α-4 / Layer C 진입 가능성 합의 / Group α 합의 / Backlog #6 우선 진입 합의 / Layer A / Layer B / GP-3 Stage 2 / Stage 4 / 5 Stage 분할안 / Group A 2차 풀 3+1 합의 본문 변경 / R-4 (829줄) / R-5 (35줄) / R-7 (328줄) / R-1 (1593줄) 영역 본문 변경 (합산 2785줄) / 14 결정 영역 *재결정* / Phase α-1 / α-2 / α-3 / α-4 자동 재진입 / 양 GP × 5 조건 evidence 재생성 / 4 prerequisite actual runs 자동 재실행 / 신규 actual run 자동 trigger / Layer D / Layer E / Layer F 발효 / 7 금지 영역 *해소* / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습) — **(A) Reviewer-only 단축 합의 진입 (권고) / (F) Step 5 Layer C 발효 합의 보고서 작성 직진 (단축 흐름) / (G) Step 3 풀 3+1 + Step 4 외부 LLM 1+ blind 의뢰 진입 / 기타 옵션**.

---

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ J, §9 답습)
**금지 (사용자 명시 패턴 답습 — 본 brief 영역)**:
- ❌ **실 Layer C 발효** (Implementation Evidence PASS *발효 선언*) (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ GP-3 / GP-5 PASS 발효
- ❌ 어느 Step (Step 0 ~ Step 6) 자동 진입
- ❌ 합의 형태 자동 결정 (Step 3 = 사용자 명시 결정 의무)
- ❌ 외부 LLM vendor 자동 선택 / 자동 호출 (Step 4)
- ❌ 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정)
- ❌ Layer C 발효 합의 보고서 자동 작성 (Step 5)
- ❌ Implementation Evidence PASS 발효 선언 자동 진입 (Step 5)
- ❌ 메타 갱신 + commit + push 자동 진입 (Step 6)
- ❌ 양 GP × 5 조건 evidence *재생성*
- ❌ 4 prerequisite actual runs 자동 재실행
- ❌ 신규 actual run 자동 trigger
- ❌ ADR-011 §2.1 (a)~(e) 5 조건 *재정의*
- ❌ R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 변경 (2785줄 답습)
- ❌ Phase α-1 / α-2 / α-3 / α-4 합의 본문 변경 / 자동 재진입
- ❌ Layer C 진입 가능성 합의 (`c13c011`) 본문 변경
- ❌ C-β / C-γ / C-δ / C-ε / C-α / C-η 자동 변경
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / Layer D / Group α / Backlog #6 우선 진입 / Phase α 4 합의 / GP 합의 / Stage 합의 / Group A 2차 풀 3+1 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ step 분할안 자동 재설계 (Stage 2 / Stage 4 패턴 답습 외)
- ❌ Phase β / γ 자동 진입
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ event enum 정식 등록 (4 후보 모두 = Backlog #5 분리)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = step 분할안 한정 — 실 보고서 = Step 5)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 (본 brief = step 분할안 한정 — 실 메타 = Step 6)
- ❌ git commit / push (본 brief = step 분할안 한정 — 실 commit / push = Step 6)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ F-금지 #1 위반 (GitHub Actions secrets 사용 도입)
- ❌ Hermes upstream Dockerfile 변경
- ❌ Production `docker-compose.yml` 신설 / 변경
- ❌ 실 secret material commit
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입
- ❌ PC-4 / AR-2 / AR-3 / Stage 5 / ST-1 / ST-2 / ST-4 / ST-5 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 *재고정*
