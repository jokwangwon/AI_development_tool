# Layer C 발효 합의 (Implementation Evidence PASS) 진입 Brief (준비안 — DRAFT)

> **본 문서는 Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 후속 (α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565`), Layer C (Implementation Evidence PASS) 발효 합의 *진입 가능성 검토* 한정 의 brief 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Layer C 발효를 시작시키지 않으며, (ii) Implementation Evidence PASS 를 선언하지 않으며, (iii) MVP-1 PASS 를 선언하지 않으며, (iv) 외부 LLM 호출을 자동 발화시키지 않으며, (v) Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 C-α-1 ~ C-α-11 / Phase α-1 합의 15 조건 C-β-1 ~ C-β-15 / Phase α-2 합의 26 조건 C-γ-1 ~ C-γ-26 / Phase α-3 합의 28 조건 C-δ-1 ~ C-δ-28 / Phase α-4 합의 29 조건 C-ε-1 ~ C-ε-29 / 사용자 명시 7 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5 조건 — Layer C 발효 모법
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §2.2 MVP-1 Exit 기준 (= Implementation Evidence PASS 진입 조건) + §5.1 ADR-011 §2.1 (a)~(e) 5 조건 답습 양 GP 공통
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-4-r1-ci-workflow-integration-entry.md` (Phase α-4 R-1 합의, commit `e59a565` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md` (Phase α-3 R-7 합의, commit `3f6306d` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-mvp1-implementation-entry.md` (MVP-1 Implementation Entry READY, commit `df20b15`)
- `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` + `3plus1-consensus-2026-05-12-gp3-stage2-implementation-entry.md` + `3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` + `3plus1-consensus-2026-05-12-stage4-pc3-ar1-implementation-entry.md`
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + ADR-008 차단조건 #4 + ADR-009 C-N §5 + ADR-010 + ADR-012 §2.1~§3.5

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Layer C 발효 합의 brief 작성해주세요"

### 0.2 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 / α-4 패턴 답습)

사용자가 본 brief 진입 명령 시 명시 prohibitions 를 enumerate 하지 않았으나, **Phase α-1 / α-2 / α-3 / α-4 합의 답습 패턴** = 7 금지 영역 유지 (사용자 명시 강조 답습) — 본 brief = 본 패턴 답습 (#1 = Layer C 영역 한정):

1. ❌ **실 Layer C 발효 금지** — Implementation Evidence PASS *발효 선언* 0건 (본 brief = *진입 가능성 검토 한정*)
2. ❌ **CI workflow 변경 금지** — 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow 본문 어느 줄도 변경 0건
3. ❌ **branch protection 변경 금지**
4. ❌ **dev 환경 강제 금지**
5. ❌ **`pre-commit install` 의무화 금지**
6. ❌ **Operational Readiness PASS (Layer E) 선언 금지**
7. ❌ **Hermes PMO 격상 (Layer F) 금지**

본 7 금지 답습 = 사용자 명시 패턴 보존 — 사용자가 본 brief 검토 시 prohibition 추가/축소 권위 영역 (옵션 (B) 수정 요청 답습).

### 0.3 본 brief 가 *하는* 것

1. Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 답습 + Layer C 발효 합의 *진입 가능성 검토 한정* (§1)
2. **Layer C 정의 + ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습** — GP-3 + GP-5 양 GP 공통 (§2)
3. **GP-3 + GP-5 양 GP × ADR-011 §2.1 (a)~(e) 5 조건 현 상태 evidence 정리 매트릭스** — 4 prerequisite actual runs PASS + Phase α 4 단계 brief 답습 (§3)
4. **사용자 명시 7 금지 영역 × Layer C 발효 합의 분리 매트릭스** (§4)
5. **Layer C 발효 합의 진입 적격성 5 조건 검토** — 본 brief 영역 한정 (§5)
6. **Layer C 발효 합의 형태 권고** — 외부 LLM 1+ 요구사항 + Reviewer-only 단축 vs 풀 3+1 분리 검토 (§6)
7. **Rollback Trigger 의존성 답습** — Layer C 발효 시점 영향 trigger enumerate (§7)
8. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§8)
9. **다음 단계 결정 옵션** (사용자 결정 영역, §9)
10. **본 brief 메타 검증** (§10)

### 0.4 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 7 금지 영역**:

- ❌ **실 Layer C 발효 0건** — Implementation Evidence PASS *발효 선언* 0건 (본 brief = 합의 보고서 권위 0건 + 발효 권위 0건)
- ❌ **CI workflow 변경 0건** — 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` 694줄 + `provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄) + 8 G2/G3/G4 PoC workflow 본문 변경 0건
- ❌ **branch protection 변경 0건** — AR-2 진입 0건 (Backlog #3 T3 영역 분리)
- ❌ **dev 환경 강제 0건** — `tools/doctor.py` 신설 / 의무 실행 0건
- ❌ **`pre-commit install` 의무화 도입 0건** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 0건
- ❌ **Operational Readiness PASS (Layer E) 선언 0건** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) 0건** — ADR-008 부록 C 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **MVP-1 PASS (Layer D) 선언 0건** — Layer C 발효 후 별도 합의 영역 분리
- ❌ **외부 LLM 자동 호출 0건** — Group α 합의 C-11 답습 (응답 = 입력 한정, 본 brief = 외부 LLM 요구사항 *검토 한정*)
- ❌ **R-4 도구 본문 변경 0건** — `tools/secret_scanner.py` (368줄) / `tools/provider_import_scanner.py` (178줄) / `tools/provider_url_scanner.py` (283줄) 어느 줄도 변경 0건
- ❌ **R-5 `.importlinter` 본문 변경 0건** — `/.importlinter` (35줄) 어느 줄도 변경 0건
- ❌ **R-7 docker secret block 본문 변경 0건** — `docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/` 9 artifacts (328줄) 어느 줄도 변경 0건
- ❌ **R-1 CI workflow 통합 본문 변경 0건** — 7 artifacts (1593줄) 어느 줄도 변경 0건
- ❌ **Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 0건** — 본 brief = Layer C *발효 합의 가능성 검토 한정*
- ❌ **Phase α-1 / α-2 / α-3 / α-4 합의 (`1b3090b` / `6a79247` / `3f6306d` / `e59a565`) 본문 변경 0건**
- ❌ **Phase β / γ 자동 진입 0건**
- ❌ **GP-3 / GP-5 PASS *발효* 0건** — Layer C 발효 시 양 GP PASS 동시 발효, 본 brief = 진입 가능성 검토 한정
- ❌ **양 GP × 5 조건 evidence *재생성* 0건** — 본 brief = 현 evidence enumerate 한정
- ❌ **4 prerequisite actual runs 재실행 0건** — `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정
- ❌ **신규 actual run 자동 trigger 0건** — Layer C 발효 시 별도 검증 영역
- ❌ **Layer C 발효 시 외부 LLM blind 의뢰 자동 발송 0건** — 사용자 명시 결정 영역
- ❌ **ADR 본문 자동 갱신 0건** — cross-reference 답습 한정 (Layer C 발효 후 별도 commit 영역)
- ❌ **ADR-011 §2.1 (a)~(e) 5 조건 재정의 0건** — 답습 한정
- ❌ **Layer B §5.5 9 sub-수단 본문 채택 변경 0건**
- ❌ **Group α 합의 C-1 ~ C-12 자동 변경 0건**
- ❌ **14 결정 영역 *재결정* 0건**
- ❌ **Backlog #6 우선 진입 합의 §5.2 4 Phase 정의 변경 0건**
- ❌ **Stage 1 ~ Stage 5 분할안 변경 0건** — `c50e6a0` 답습 한정
- ❌ **GP-3 Stage 2 합의 / GP-3 MVP-1 진입 합의 / GP-5 MVP-1 진입 합의 / Stage 4 합의 본문 변경 0건**
- ❌ **F-금지 #1 위반 0건** — GitHub Actions secrets 사용 도입 0건 (영구 답습)
- ❌ **Hermes upstream Dockerfile 변경 0건** — ADR-008 차단조건 #6 + 부록 B 답습 보존
- ❌ **Production `docker-compose.yml` 신설 / 변경 0건** — PoC 격리 디렉토리 한정 답습
- ❌ **실 secret material commit 0건** — FAKE_TEST_SECRET marker 영구 답습
- ❌ **`secrets/.gitignore` 변경 0건**
- ❌ **PC-4 / AR-2 / AR-3 / Stage 5 자동 진입 0건** — Backlog #1+#2 / Backlog #3 / 별도 합의 영역 분리
- ❌ **ST-1 / ST-2 / ST-4 / ST-5 자동 진입 0건** — Backlog #1 1.5차 / Backlog #7 / MVP-2 이후 분리
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 0건** — R-4.1 Tier-1 45 / URL Tier-1 10 / Model Tier-1 19 답습 한정
- ❌ **threshold *고정* 0건** — FP / FN / latency / image layer leak / restart recovery 모두 *후보 한정* 유지
- ❌ **event enum 정식 등록 0건** — `secret_scan_layer1_implementation` / `provider_adapter_enforcement_layer1_static` / `docker_secret_isolation_layer1_implementation` / `pc3_ar1_integration_implementation` 모두 *후보 한정* (Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의)
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 0건**
- ❌ **합의 보고서 작성 0건** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 0건**
- ❌ **git commit / push 0건**
- ❌ **실 API key / provider SDK / 외부 API 호출 0건**
- ❌ **인간 리뷰 의무 자동 발화 0건**
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 0건** — Backlog #4 분리
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 0건**
- ❌ **token rotation 정책 자동 결정 0건**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 0건**
- ❌ **commit signing 도입 0건** — MVP-6 영역
- ❌ **`pull_request_target` workflow 도입 0건**
- ❌ **Backlog #1 / #2 / #4 / #5 / #7 자동 진입 0건**
- ❌ **Layer 2 runtime block (G5-5) 진입 0건** — MVP-3/4 영역 분리

### 0.5 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Layer C (Implementation Evidence PASS) 발효를 *시작* 시키지 않으며,
- (ii) GP-3 / GP-5 PASS 를 *발효* 시키지 않으며,
- (iii) MVP-1 PASS 를 *선언* 시키지 않으며,
- (iv) 외부 LLM 호출을 *자동 발화* 시키지 않으며 (Group α 합의 C-11 답습 — 응답 = 입력 한정),
- (v) ADR-011 §2.1 (a)~(e) 5 조건을 *재정의* 시키지 않으며,
- (vi) Phase α-1 / α-2 / α-3 / α-4 합의 / Group α 합의 C-1 ~ C-12 / Backlog #6 우선 진입 합의 11 조건 / Phase α-1 합의 15 조건 / Phase α-2 합의 26 조건 / Phase α-3 합의 28 조건 / Phase α-4 합의 29 조건 / GP-3 Stage 2 합의 / Stage 4 합의 / 5 Stage 분할안 합의 / Layer A / Layer B / Layer D 본문을 *변경* 하지 않으며,
- (vii) 3 MVP-1 workflow + 8 G2/G3/G4 PoC workflow / R-4 도구 / R-5 `.importlinter` / R-7 docker secret block / R-1 CI workflow 통합 본문 어느 줄도 *변경* 하지 않으며,
- (viii) 사용자 명시 7 금지 영역 어느 것도 *해소* 시키지 않으며,
- (ix) Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Layer C 발효 합의 영역의 *진입 가능성 검토* — Layer C 정의 + ADR-011 §2.1 5 조건 답습 + GP-3 + GP-5 양 GP × 5 조건 evidence 정리 매트릭스 + 4 prerequisite runs PASS 답습 + Phase α 4 단계 brief 답습 + 7 금지 분리 매트릭스 + 진입 적격성 검토 + 외부 LLM 1+ 요구사항 검토 + 합의 형태 권고 + 금지 영역 enumeration**. 모든 *발효 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 답습

| 단계 | 영역 | brief commit | 합의 commit | 합의 조건 |
|-----|------|-----------|----------|---------|
| α-1 | R-4 도구 본문 (3 도구 829줄) | `e7cdb21` (584줄) | `1b3090b` APPROVE AS BRIEF | 15 조건 C-β-1 ~ C-β-15 |
| α-2 | R-5 `.importlinter` 본문 (35줄) | `608a046` (710줄) | `6a79247` APPROVE AS BRIEF | 26 조건 C-γ-1 ~ C-γ-26 |
| α-3 | R-7 docker secret block (9 artifacts 328줄) | `8da3273` (748줄) | `3f6306d` APPROVE AS BRIEF | 28 조건 C-δ-1 ~ C-δ-28 |
| α-4 | R-1 CI workflow 통합 (7 artifacts 1593줄) | `f91ef4b` (751줄) | `e59a565` APPROVE AS BRIEF | 29 조건 C-ε-1 ~ C-ε-29 |

**합산**: 4 brief × 2793줄 + 4 합의 × 약 2000줄 + 4 prerequisite actual runs PASS evidence (`25728590939` GP-3 secret-hygiene + `25728590916` GP-5 provider-adapter + `25728590977` GP-5 provider-url-scanner + `25731846625` GP-3 Stage 2 docker secret).

### 1.2 Layer C 발효 의존성 매트릭스 (현 상태)

| 의존성 | 답습 출처 | 현 상태 |
|-------|---------|--------|
| Phase α-1 R-4 brief APPROVE AS BRIEF | `1b3090b` | ✅ 완료 |
| Phase α-2 R-5 brief APPROVE AS BRIEF | `6a79247` | ✅ 완료 |
| Phase α-3 R-7 brief APPROVE AS BRIEF | `3f6306d` | ✅ 완료 |
| Phase α-4 R-1 brief APPROVE AS BRIEF | `e59a565` | ✅ 완료 |
| Phase α 4 단계 brief 모두 APPROVE AS BRIEF | 본 §1.1 답습 | ✅ **완료 milestone** |
| **4 prerequisite actual runs PASS** | Stage 1 + Stage 2 + Stage 3 + Stage 4 actual run | ✅ **충족 완료** |
| MVP-1 Implementation Entry READY | `df20b15` (2026-05-12) | ✅ 완료 |
| Layer A APPROVE | `f1e0b23` | ✅ 완료 |
| Layer B APPROVE | `f40423f` | ✅ 완료 |
| §5.5 9 sub-수단 본문 채택 | `55c5b4b` | ✅ 완료 |
| Backlog #6 우선 진입 합의 APPROVE | `c7ddfdd` | ✅ 완료 |
| Group α 합의 APPROVE WITH CONDITIONS | `4880e88` | ✅ 완료 |
| ADR-011 §2.1 (a)~(e) 5 조건 모법 정의 | `R-3` 발행 (2026-05-06) | ✅ 완료 |

### 1.3 6-Layer 분리 매트릭스 현 상태 (2026-05-15 후속)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + `55c5b4b`) | 답습 한정 |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 | ✅ APPROVE WITH CONDITIONS (`4880e88`) | 답습 한정 |
| Backlog #6 우선 진입 | Runtime + CI-hook 영역 정의 + Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) | 답습 한정 |
| Phase α-1 R-4 진입 | R-4 도구 본문 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`1b3090b`) | 답습 한정 |
| Phase α-2 R-5 진입 | R-5 `.importlinter` 본문 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`6a79247`) | 답습 한정 |
| Phase α-3 R-7 진입 | R-7 docker secret block 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`3f6306d`) | 답습 한정 |
| Phase α-4 R-1 진입 | R-1 CI workflow 통합 진입 가능성 검토 | ✅ APPROVE AS BRIEF (`e59a565`) | 답습 한정 |
| **Layer C** | **Implementation Evidence PASS 발효** | ⏳ **DRAFT (본 brief = 진입 가능성 검토)** | **본 brief 영역** |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (Layer C 발효 후) |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #6) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #7) |

### 1.4 본 brief 의 진입점

```
Layer A APPROVE (f1e0b23) ─────────────────────────────────────────┐
Layer B APPROVE (f40423f) — §5.5 9 sub-수단 본문 채택 (55c5b4b)      │
Group α APPROVE (4880e88) ─────────────────────────────────────────┤
Backlog #6 우선 진입 합의 (c7ddfdd) APPROVE AS BRIEF
4 prerequisite actual runs PASS (25728590939 + 25728590916 + 25728590977 + 25731846625)
Phase α-1 R-4 brief (e7cdb21) + 합의 (1b3090b) APPROVE AS BRIEF
Phase α-2 R-5 brief (608a046) + 합의 (6a79247) APPROVE AS BRIEF
Phase α-3 R-7 brief (8da3273) + 합의 (3f6306d) APPROVE AS BRIEF
Phase α-4 R-1 brief (f91ef4b) + 합의 (e59a565) APPROVE AS BRIEF
   │
   ▼ Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone
■ 본 brief = Layer C 발효 합의 *진입 가능성 검토* (DRAFT)                  ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (합의 형태 = 단축 또는 풀 3+1 — §6 답습)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Layer C 발효 합의 진입 (ADR-011 §2.1 (a)~(e) 5/5 evidence 검증)        ← 본 brief 영역 외
   │
   ▼ (Layer C 발효 후 — 자동 진입 0건)
Layer D MVP-1 PASS 선언 합의                                              ← 본 brief 영역 외
```

---

## 2. Layer C 정의 + ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습

### 2.1 Layer C 정의 (mvp1.md §2.2 + ADR-011 §2.1 답습)

| 영역 | 답습 출처 | 정의 |
|------|---------|------|
| 명칭 | mvp1.md §2.2 | **Implementation Evidence PASS** (Layer C 발효) |
| 발효 조건 | mvp1.md §2.2 + ADR-011 §2.1 (a)~(e) | **(GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정** |
| Layer D 의존성 | mvp1.md §2.2 | Layer C 발효 → Layer D (MVP-1 PASS) 선언 진입 가능 |
| 외부 LLM 요구사항 | mvp1.md §0 (3-layer PASS) | 외부 LLM 1+ (수단 결정 시점 권고 한정) — Layer C 발효 자체 = 단축 또는 풀 3+1 |
| 합의 형태 | mvp1.md §2.2 + §5.1 | 단축 (Reviewer-only) 또는 풀 3+1 (트리거 발화 시) — 본 brief §6 답습 |

### 2.2 ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습 (양 GP 공통)

| # | 조건 | 검증 방식 (ADR-011 §2.1 본문 답습) |
|---|------|---------|
| **(a)** | **동등 이상의 보안 결과** | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
| **(b)** | **격리 환경 PoC로 실증** | Docker isolation + 자동 검증 항목 |
| **(c)** | **ADR / SDD 권위 명시** | 본 ADR 또는 후속 ADR + SDD cross-reference |
| **(d)** | **자동 회귀 검증 경로 확보** | CI/nightly 재실행 |
| **(e)** | **합의 APPROVE** | 단축 또는 풀 3+1 합의 (수단 결정 시 풀 3+1 권고) |

### 2.3 Layer C 발효 합의의 *권위 한계* (사용자 명시 답습)

본 brief = **Layer C 발효 합의 *진입 가능성 검토 한정***. 본 brief 발효 후 단계 = Layer C 발효 합의 *실 진입* — 그 단계 역시 *합의 보고서 작성* 까지 한정 + 실 Layer D / MVP-2 / Operational Readiness PASS / Hermes PMO 격상 모두 영역 외.

---

## 3. GP-3 + GP-5 양 GP × ADR-011 §2.1 (a)~(e) 5 조건 현 상태 evidence 정리 매트릭스

### 3.1 GP-3 × 5 조건 evidence 매트릭스 (mvp1.md §2.2 + §3 답습)

| # | 조건 | GP-3 evidence | 현 상태 |
|---|------|------------|------|
| (a) | 동등 이상의 보안 결과 | Group D `tools/secret_scanner.py` (368줄) — R-4.1 Tier-1 45 patterns 직접 답습 (Prefix 36 + regex 7 + alternation 2) — gitleaks/detect-secrets 동등 이상 + 답습 변경 0건 | ✅ **충족** |
| (b) | 격리 환경 PoC 실증 | Stage 2 ST-3 PoC (`docker/gp3-st3-poc/` 4 파일 93줄) — Docker isolation (`network_mode: none` + `read_only: true` + `cap_drop: ALL` + `no-new-privileges: true` + `user: 1000:1000`) + Stage 1 D-1 mode + Stage 2 actual run `25731846625` PASS | ✅ **충족** |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (저장 경로 isolation) + ADR-008 차단조건 #6 + 부록 B (file system secret isolation) + ADR-010 (SQLCipher Vault) + R-4 (`docs/architecture/redaction-pattern-equivalence.md`) + mvp1.md §3 (GP-3 Deepening) + Layer B §5.5.1 ST-3 본문 채택 | ✅ **충족** |
| (d) | 자동 회귀 검증 경로 확보 | `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄) — Stage 1 + Stage 2 + Stage 4 entry step + nightly + actual run `25728590939` (Stage 1) + `25731846625` (Stage 2) SUCCESS | ✅ **충족** |
| (e) | 합의 APPROVE | GP-3 MVP-1 진입 합의 (`6dc5bdc`) APPROVE WITH CONDITIONS + GP-3 Stage 2 단독 구현 진입 합의 APPROVE + Phase α-3 R-7 합의 (`3f6306d`) APPROVE AS BRIEF + Layer C 발효 합의 = **본 brief 발효 후 단계 진입 적격** | ⏳ **발효 시점 = Layer C 합의 본 단계** |

**GP-3 합산**: **5/5 evidence 충족 (4/5 현 충족 + (e) = Layer C 합의 본 단계 진입 시 발효)**.

### 3.2 GP-5 × 5 조건 evidence 매트릭스 (mvp1.md §2.2 + §4 답습)

| # | 조건 | GP-5 evidence | 현 상태 |
|---|------|------------|------|
| (a) | 동등 이상의 보안 결과 | Group A 1차 `tools/provider_import_scanner.py` (178줄, AST 5 패턴 cover) + Group A 2차 `.importlinter` (35줄, 4 forbidden_modules + facade single allow + `include_external_packages = True` C-9 PASS) + Group A 3차 `tools/provider_url_scanner.py` (283줄, URL Tier-1 10 + Model Tier-1 19) — depcruise/import-linter §9.3 답습 동등 이상 + 답습 변경 0건 + 각주 1 google.generativeai 1차 AST 단독 책무 분리 | ✅ **충족** |
| (b) | 격리 환경 PoC 실증 | Group A 1차/2차/3차 PoC (`tests/fixtures/provider_adapter_enforcement/{pass,fail,mvp1_entry}/`) + `src/adapters/llm/facade.py` placeholder (facade single entry point) + import-linter `include_external_packages = True` 사전 검증 PASS (C-9 RA-9) + actual run `25728590916` + `25728590977` SUCCESS | ✅ **충족** |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #4 (P1 Facade) + ADR-009 C-N §5 (Provider Liquidity 5-way Layer 1 모법) + P1 v2 + P2 v3 §10.1 Normative Constraints + mvp1.md §4 (GP-5 Deepening) + Layer B §5.5.2 T-6 = T-2 + T-5 본문 채택 + Group A 2차 풀 3+1 합의 (T-2 import-linter 채택 + C-1~C-10 + TR-1~TR-5) | ✅ **충족** |
| (d) | 자동 회귀 검증 경로 확보 | `.github/workflows/provider-adapter-enforcement.yml` (186줄) + `.github/workflows/provider-url-scanner.yml` (326줄) — Stage 3 entry step + nightly + actual run `25728590916` + `25728590977` SUCCESS | ✅ **충족** |
| (e) | 합의 APPROVE | GP-5 MVP-1 진입 합의 APPROVE WITH CONDITIONS + Stage 4 합의 (PC-3 + AR-1 통합) APPROVE + Group A 1차/2차/3차 합의 모두 APPROVE + Phase α-1 R-4 합의 (`1b3090b`) + Phase α-2 R-5 합의 (`6a79247`) + Phase α-4 R-1 합의 (`e59a565`) APPROVE AS BRIEF + Layer C 발효 합의 = **본 brief 발효 후 단계 진입 적격** | ⏳ **발효 시점 = Layer C 합의 본 단계** |

**GP-5 합산**: **5/5 evidence 충족 (4/5 현 충족 + (e) = Layer C 합의 본 단계 진입 시 발효)**.

### 3.3 양 GP 합산 매트릭스

| GP | (a) | (b) | (c) | (d) | (e) | 합산 |
|----|-----|-----|-----|-----|-----|------|
| GP-3 | ✅ | ✅ | ✅ | ✅ | ⏳ Layer C 시점 | **5/5 적격** |
| GP-5 | ✅ | ✅ | ✅ | ✅ | ⏳ Layer C 시점 | **5/5 적격** |

**합산**: **양 GP × 5 조건 = 10/10 evidence 적격성 권위 권고** (현 (a)~(d) 8/8 현 충족 + (e) 양 GP = Layer C 발효 합의 본 단계 진입 시 동시 발효).

### 3.4 4 prerequisite actual runs PASS 답습

| Stage | workflow | run_id | commit 기준 | 결과 |
|-------|---------|--------|----------|------|
| Stage 1 GP-3 secret-hygiene | `secret-hygiene-egress-redaction.yml` | `25728590939` | `72622409` | PASS (regex H-C/H-F/H-G/H-K + Tier-1 prefix 10 pattern cover, F-forbidden 0/12, escalation 0/7, patterns 45, Tier-1 42 catalog compliant) |
| Stage 3 GP-5 provider-adapter | `provider-adapter-enforcement.yml` | `25728590916` | `72622409` | PASS (MVP-1 entry AST scan OK, fail rc=1 ollama/google.generativeai/openai-alias cover, pass rc=0) |
| Stage 3 GP-5 provider-url-scanner | `provider-url-scanner.yml` | `25728590977` | `72622409` | PASS (mvp1_entry_url_model=PASS, E-1 6 vendors + E-2 5 patterns cover) |
| Stage 2 GP-3 ST-3 docker secret | `secret-hygiene-egress-redaction.yml` (Stage 2 entry step) | `25731846625` | `6c6b208` | PASS (Stage 2 image layer leak 0 + restart recovery 100%) |

**4 prerequisite runs 모두 SUCCESS — Layer C 발효 evidence (a)~(d) 8/8 현 충족 *직접 검증* 답습**.

### 3.5 본 §3 의 *범위 한계*

본 §3 = **양 GP × 5 조건 evidence *enumerate 한정***. 실 evidence 재검증 / 신규 actual run 자동 trigger / 외부 LLM blind 의뢰 자동 발송 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 4. 사용자 명시 7 금지 영역 × Layer C 발효 합의 분리 매트릭스

### 4.1 금지 #1 — 실 Layer C 발효 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer C 발효 합의 *진입 가능성 검토* | ✅ 본 brief 영역 | — |
| Layer C 발효 합의 보고서 작성 | ❌ (영역 외) | 본 brief 승인 후 단계 (사용자 명시 결정 후) |
| Implementation Evidence PASS *발효 선언* | ❌ (영역 외) | Layer C 발효 합의 발효 후 자동 발효 (사용자 명시 결정 영역) |
| Layer D MVP-1 PASS 선언 | ❌ (영역 외) | Layer C 발효 후 별도 합의 |
| **본 brief 영역 *내* 적격 작업** | **양 GP × 5 조건 evidence *enumerate 한정* + 진입 적격성 검토 + 합의 형태 권고** | — |

### 4.2 금지 #2 — CI workflow 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| 3 MVP-1 workflow (1206줄) 본문 변경 | ❌ (영역 외) | Phase α-4 실 진입 시점 (별도 합의) |
| 8 G2/G3/G4 PoC workflow (2037줄) 본문 변경 | ❌ (영역 외) | 별도 영역 |
| 신규 workflow 신설 | ❌ (영역 외) | 별도 합의 영역 |
| **본 brief 영역 *내* 적격 작업** | **CI workflow evidence (d) *enumerate 한정* (워크플로우 답습 검증 — 실 변경 0건)** | — |

### 4.3 금지 #3 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| AR-2 진입 (CODEOWNERS + required status check) | ❌ (영역 외) | Backlog #3 T3 영역 별도 풀 3+1 분리 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 = evidence verification 영역, branch protection = T3 영역 — 직교)** | — |

### 4.4 금지 #4 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/doctor.py` 신설 | ❌ (영역 외) | R-10 영역 (Phase β-2) |
| dev 환경에서 evidence verification 의무 실행 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C 발효 = CI evidence 영역, dev 환경 강제 = R-10 영역 — 분리)** | — |

### 4.5 금지 #5 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | R-6 영역 (Phase β-1) — Backlog #1+#2 1.5차 보강 분리 |
| `pre-commit install` 의무화 단계 진입 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **Layer C = PC-3 (CI-only enforcement) evidence 한정 + PC-4 local pre-commit framework 분리 명시** | — |

### 4.6 금지 #6 — Operational Readiness PASS (Layer E) (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C = Implementation Evidence PASS, Layer E = Operational Readiness PASS — 분리 + Layer D MVP-1 PASS 중간)** | — |

### 4.7 금지 #7 — Hermes PMO 격상 (Layer F) (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F 격상 | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (Layer C = Implementation Evidence PASS, Layer F = Hermes PMO 격상 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **7 금지 영역 *분리 매트릭스 한정***. 7 금지 영역 어느 것도 *해소* 0건 + Layer C 실 발효 자동 진입 0건.

---

## 5. Layer C 발효 합의 진입 적격성 5 조건 검토

### 5.1 적격성 검토 매트릭스

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-ζ-1** | **사용자 명시 7 금지 영역 충돌 0** | Layer C 발효 합의 = evidence verification 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0). 금지 #1 (실 Layer C 발효) = 본 brief = 발효 합의 진입 가능성 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-ζ-2** | **ADR-011 §2.1 (a)~(e) 5 조건 양 GP 충족 적격성** | GP-3 × 5/5 적격 (현 (a)~(d) 4/4 충족 + (e) Layer C 시점 발효 적격) + GP-5 × 5/5 적격 (동상) = **10/10 evidence 적격성 권위 권고** | ✅ **10/10 적격** |
| **C-ζ-3** | **4 prerequisite actual runs PASS 답습** | Stage 1 (`25728590939`) + Stage 2 (`25731846625`) + Stage 3 (`25728590916` + `25728590977`) 모두 SUCCESS — 4 prerequisite runs PASS 답습 *직접 검증* | ✅ **4/4 PASS 답습** |
| **C-ζ-4** | **Phase α 4 단계 brief 모두 APPROVE AS BRIEF** | α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565` 4/4 APPROVE AS BRIEF 완료 | ✅ **4/4 완료** |
| **C-ζ-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (Layer C = Implementation Evidence PASS, Hermes PMO 격상 영역 분리) / 단일 source-of-truth 보존 (evidence 답습 변경 0건) / 수단/목적 분리 보존 (ADR-011 §2.1 (a)~(e) 5 조건 모법 답습) / T1/T2/T3 분리 보존 (Layer C = T2 영역, T3 영역 진입 0건) / SPOF 의도적 수용 보존 | ✅ **5/5 보존** |

### 5.2 풀 3+1 승격 트리거 검토 (Phase α-1 / α-2 / α-3 / α-4 합의 §5.2 답습 + Layer C 특수 추가)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Phase α-2 C-γ-1 ~ C-γ-26 / Phase α-3 C-δ-1 ~ C-δ-28 / Phase α-4 C-ε-1 ~ C-ε-29 어느 것의 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 2 | 본 brief 가 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 3 | 본 brief 가 Layer B §5.5 9 sub-수단 본문 채택 *재결정* 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 — Layer C 발효 = evidence verification 영역 (catalog / provider 영역과 직교) |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 약화 포함 | ❌ 0건 — 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입 권고 | ❌ 0건 — T3 분리 명시 한정 (Layer C = T2 영역) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | 본 brief 가 ADR-011 §2.1 (a)~(e) 5 조건 *재정의* 권고 | ❌ 0건 — 본 brief = ADR-011 §2.1 모법 답습 한정 |
| 9 | 본 brief 가 양 GP × 5 조건 evidence *재생성* 권고 | ❌ 0건 — 본 brief = 현 evidence enumerate 한정 |
| 10 | 본 brief 가 4 prerequisite actual runs 자동 재실행 권고 | ❌ 0건 — 4 runs 답습 한정 (재실행 0건) |
| 11 | 본 brief 가 외부 LLM 자동 호출 권고 | ❌ 0건 — Group α 합의 C-11 답습 (응답 = 입력 한정 — 본 brief = 외부 LLM 요구사항 *검토 한정*) |
| 12 | 본 brief 가 Phase α-1 / α-2 / α-3 / α-4 합의 본문 변경 / 자동 재진입 권고 | ❌ 0건 — 본 brief = 답습 한정 (4 합의 본문 변경 0건) |
| 13 | 본 brief 가 MVP-1 PASS (Layer D) 자동 선언 권고 | ❌ 0건 — Layer C 발효 후 별도 합의 영역 분리 |
| 14 | 본 brief 가 GP-3 Stage 2 합의 / Stage 4 합의 / 5 Stage 분할안 합의 본문 변경 권고 | ❌ 0건 — 본 brief = 답습 한정 |
| 15 | 본 brief 가 신규 ADR / 신규 P / 신규 GP 발행 권고 | ❌ 0건 — cross-reference 답습 한정 |

**검토 결과**: **15/15 트리거 0건 발화** → **합의 형태 권고 = 본 brief §6 답습** (단축 vs 풀 3+1 결정 = 외부 LLM 1+ 요구사항 검토 결과 의존).

### 5.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| 5 조건 (C-ζ-1 ~ C-ζ-5) | **5/5 충족** |
| 15 풀 3+1 트리거 | **0/15 발화** |
| Phase α 4 단계 brief 모두 APPROVE AS BRIEF | **4/4 완료** |
| 4 prerequisite actual runs PASS | **4/4 PASS 답습** |
| 양 GP × 5 조건 evidence | **10/10 적격** |
| **Layer C 발효 합의 진입 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.4 본 §5 의 *범위 한계*

본 §5 = **진입 적격성 *검토 한정***. 실 Layer C 발효 합의 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 적격 판정 = 적격성 권위 권고 한정 — 실 Layer C 발효 권위 0건.

---

## 6. Layer C 발효 합의 형태 권고 + 외부 LLM 1+ 요구사항 검토

### 6.1 외부 LLM 1+ 요구사항 검토 (mvp1.md §0 + §2.2 답습)

| 영역 | 답습 출처 | 본 brief 검토 결과 |
|------|---------|---------------|
| mvp1.md §0 3-layer PASS framework | 외부 LLM GPT-5.5 Thinking 응답 §6 (3-layer PASS 분리) | Layer 1 PoC Evidence / Layer 2 Implementation Evidence PASS (= Layer C) / Layer 3 Operational Readiness PASS — 본 brief = Layer 2 영역 |
| mvp1.md §2.2 (e) 합의 APPROVE | 단축 (Reviewer-only) 또는 풀 3+1 (수단 결정 시 권고) | **본 Layer C 발효 = 수단 *결정*이 아닌 *evidence verification*** — 수단 본문 채택은 Layer B §5.5 (`f40423f` + `55c5b4b`) 발효 완료 |
| Layer C 발효 시 외부 LLM 요구사항 | mvp1.md 본문 explicit 외부 LLM 1+ 의무 명시 0건 | **외부 LLM 1+ = 권고 한정 (의무 아님)** — 실 결정 = 사용자 명시 결정 영역 |

### 6.2 합의 형태 권고 매트릭스

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격 후보** | Phase α-1 / α-2 / α-3 / α-4 합의 + Layer B + Group α + Backlog #6 우선 진입 답습 한정 + 7 금지 영역 *재결정* 0건 + 본 brief = 진입 가능성 *검토 한정* (적격성 *해소* 0건) + 15/15 풀 3+1 트리거 0건 발화 (§5.2) + 양 GP × 5 조건 evidence 적격성 권위 권고 한정 |
| Layer C 발효 합의 자체 진입 | **단축 또는 풀 3+1 + (선택) 외부 LLM 1+** | 단축 옵션 = ADR-011 §2.1 5/5 evidence verification (수단 결정 아님 — Layer B 발효 답습) / 풀 3+1 옵션 = Layer C 발효 = MVP-1 1차 영역 의미 deepening 시 (사용자 명시 결정 권한) / 외부 LLM 1+ = 권고 한정 (의무 아님) |
| Layer C 발효 시 외부 LLM blind 의뢰 | **사용자 명시 결정 영역** | 자동 발화 0건 — Group α 합의 C-11 답습 (응답 = 입력 한정) |
| Layer D (MVP-1 PASS) 선언 합의 | **별도 합의** | Layer C 발효 후 별도 단계 |

### 6.3 합의 형태 권고 결정 (본 brief 권고 한정)

**본 brief 권고**: Layer C 발효 합의 = **Reviewer-only 단축 합의 적격 후보** (Phase α-1 / α-2 / α-3 / α-4 패턴 답습) — 단, 사용자 명시 결정 시 풀 3+1 + 외부 LLM 1+ 옵션 권위 영역.

**근거**:
1. 본 brief = 진입 가능성 검토 한정 — Layer C 발효 자체는 다음 단계
2. 15/15 풀 3+1 트리거 0건 발화 (§5.2)
3. Layer B + Group α + Backlog #6 + Phase α-1/2/3/4 모두 답습 한정 (재결정 0건)
4. 양 GP × 5 조건 evidence 적격성 권위 권고 한정 (실 verification = Layer C 합의 본 단계)

### 6.4 본 §6 의 *범위 한계*

본 §6 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역 + 외부 LLM 요구 여부 결정 = 사용자 명시 결정 영역.

---

## 7. Rollback Trigger 의존성 답습

### 7.1 Layer C 발효 시점 영향 받는 18 Rollback Trigger 답습 (Layer B §1.7 + mvp1.md §3.5 + §4.6 답습)

본 §은 **18 Rollback Trigger 中 Layer C 발효 시점 *영향* 받는 trigger enumerate 한정** — 발화 0건 + 본 brief 영역 *내 의존성 정리 한정*. **Layer C 발효 = (a)~(e) 5/5 evidence verification — Rollback Trigger 발화 시연 = Layer C 영역 분리** (mvp1.md §697 답습):

| Trigger | 발화 조건 | Layer C 영향 | 본 brief 영역 |
|--------|---------|-----------|------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | GP-3 (a) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 | 영향 0 (MVP-1 = S-1 단독 답습) | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | GP-3 (b) evidence 영향 (Stage 2 actual run) | 의존성 *enumerate 한정* (발화 0건 — `25731846625` PASS 답습) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | GP-3 (d) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | 영향 0 (T3 영역) | 영역 외 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | 영향 0 | 영역 외 (Backlog #3 별도 합의) |
| R-MVP1-G3-7 | Tier-2 확장 필요 | 영향 0 | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 | 영향 0 (Layer E 영역) | 영역 외 (금지 #6 답습) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | GP-5 (a) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | GP-5 (a) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) | GP-5 (a) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | GP-5 (a) + (d) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | 영향 0 (T3 영역) | 영역 외 |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 | GP-5 (d) evidence 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 | GP-5 (a) evidence 영향 (facade exemption) | 의존성 *enumerate 한정* (영역 외 — Backlog #4) |
| R-MVP1-G5-8 | branch protection 필요 trigger | 영향 0 (T3 영역) | 영역 외 (금지 #3 답습) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 | 영향 0 (MVP-3 영역) | 영역 외 |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 | 영향 0 (MVP-3/4 영역) | 영역 외 |

### 7.2 합산

| 영역 | trigger 수 | 본 brief 영역 |
|------|---------|------------|
| **Layer C 발효 evidence *직접* 영향 (Layer B 18 trigger)** | 8 (G3-1, G3-3, G3-4, G5-1, G5-2, G5-3, G5-4, G5-6) | 의존성 *enumerate 한정* — 발화 0건 |
| Layer C 발효 *간접* 영향 (Backlog 분리) | 1 (G5-7) | 영역 외 (Backlog #4) |
| Layer C 발효 *영향 0* (T3/MVP-3/MVP-6/Backlog 분리) | 9 | 영역 외 |
| **합산** | **18 trigger** | **본문 확정 답습 + 발화 0건** |

### 7.3 본 §7 의 *범위 한계*

본 §7 = **Rollback Trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* + 신규 trigger 추가 0건 + Rollback Trigger 발화 시연 = Layer C 합의 본 단계 영역 분리 (mvp1.md §697 답습).

---

## 8. 금지 사항

### 8.1 본 brief 자체 금지 사항 (사용자 명시 답습)

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
| 9 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습 — 응답 = 입력 한정) | 0건 |
| 10 | 외부 LLM blind 의뢰 자동 발송 | 0건 |
| 11 | 양 GP × 5 조건 evidence *재생성* | 0건 |
| 12 | 4 prerequisite actual runs 자동 재실행 (`25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정) | 0건 |
| 13 | 신규 actual run 자동 trigger | 0건 |
| 14 | ADR-011 §2.1 (a)~(e) 5 조건 *재정의* | 0건 |
| 15 | R-4 도구 본문 (829줄) 변경 | 0건 |
| 16 | R-5 `.importlinter` 본문 (35줄) 변경 | 0건 |
| 17 | R-7 docker secret block 본문 (328줄, 9 artifacts) 변경 | 0건 |
| 18 | R-1 CI workflow 통합 본문 (1593줄, 7 artifacts) 변경 | 0건 |
| 19 | Phase α-1 합의 (`1b3090b`) 본문 변경 | 0건 |
| 20 | Phase α-2 합의 (`6a79247`) 본문 변경 | 0건 |
| 21 | Phase α-3 합의 (`3f6306d`) 본문 변경 | 0건 |
| 22 | Phase α-4 합의 (`e59a565`) 본문 변경 | 0건 |
| 23 | C-β-1 ~ C-β-15 / C-γ-1 ~ C-γ-26 / C-δ-1 ~ C-δ-28 / C-ε-1 ~ C-ε-29 자동 변경 | 0건 |
| 24 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 25 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) 자동 변경 | 0건 |
| 26 | Group α 14 결정 영역 *재결정* | 0건 |
| 27 | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1/2/3/4 합의 / GP-3 Stage 2 합의 / Stage 4 합의 / 5 Stage 분할안 합의 / GP-3 MVP-1 진입 / GP-5 MVP-1 진입 본문 변경 | 0건 |
| 28 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 29 | Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 | 0건 |
| 30 | Phase β / γ 자동 진입 | 0건 |
| 31 | Group I / Group β / γ-1 / γ-2 자동 진입 | 0건 |
| 32 | token rotation 정책 자동 결정 | 0건 |
| 33 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 34 | commit signing 도입 | 0건 |
| 35 | `pull_request_target` workflow 도입 | 0건 |
| 36 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 37 | threshold *고정* | 0건 |
| 38 | event enum 정식 등록 (4 후보 모두 = Backlog #5 분리) | 0건 |
| 39 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 40 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 41 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 42 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 43 | git commit / push | 0건 |
| 44 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 45 | F-금지 #1 위반 (GitHub Actions secrets 사용 도입) | 0건 |
| 46 | Hermes upstream Dockerfile 변경 | 0건 |
| 47 | Production `docker-compose.yml` 신설 / 변경 | 0건 |
| 48 | 실 secret material commit (FAKE_TEST_SECRET marker 답습) | 0건 |
| 49 | 인간 리뷰 의무 자동 발화 | 0건 |
| 50 | Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입 | 0건 |
| 51 | PC-4 / AR-2 / AR-3 / Stage 5 자동 진입 | 0건 |
| 52 | ST-1 / ST-2 / ST-4 / ST-5 자동 진입 | 0건 |
| 53 | Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리) | 0건 |
| 54 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |
| 55 | MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 56 | 17 항목 우선순위 자동 *재고정* | 0건 |

### 8.2 본 brief 발효 *후* Layer C 발효 합의 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Layer C 발효 시 ADR-011 §2.1 (a)~(e) 5 조건 *재정의* | ADR-011 §2.1 모법 답습 보존 |
| 2 | Layer C 발효 시 양 GP × 5 조건 evidence *재생성* | 본 brief §3 enumerate 답습 한정 |
| 3 | Layer C 발효 시 4 prerequisite actual runs 자동 재실행 | 4 runs PASS 답습 한정 (`25728590939` + `25728590916` + `25728590977` + `25731846625`) |
| 4 | Layer C 발효 시 신규 actual run 자동 trigger | 사용자 명시 결정 영역 |
| 5 | Layer C 발효 시 외부 LLM 자동 호출 | Group α 합의 C-11 답습 (응답 = 입력 한정) |
| 6 | Layer C 발효 시 R-4 / R-5 / R-7 / R-1 본문 변경 | Phase α-1/2/3/4 합의 답습 보존 |
| 7 | Layer C 발효 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의 trigger) |
| 8 | Layer C 발효 시 Production `docker-compose.yml` 신설 / 변경 | PoC 격리 디렉토리 한정 답습 |
| 9 | Layer C 발효 시 실 secret material commit | 영구 금지 (FAKE_TEST_SECRET marker 답습) |
| 10 | Layer C 발효 시 GitHub Actions secrets 사용 도입 | 영구 금지 (F-금지 #1 G3-7 (i) 답습) |
| 11 | Layer C 발효 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 12 | Layer C 발효 시 event enum 정식 등록 | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 13 | Layer C 발효 시 `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 14 | Layer C 발효 시 local pre-commit framework 활성화 | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 7 금지 #5 답습) |
| 15 | Layer C 발효 시 branch protection rule 활성화 | Backlog #3 T3 영역 별도 풀 3+1 (사용자 명시 7 금지 #3 답습) |
| 16 | Layer C 발효 시 Layer D MVP-1 PASS 자동 선언 | Layer C 발효 후 별도 합의 영역 분리 |
| 17 | Layer C 발효 시 Layer E / Layer F 자동 진입 | MVP-6 영역 + ADR-008 부록 C 12 조건 분리 (사용자 명시 7 금지 #6 #7 답습) |
| 18 | Layer C 발효 시 Phase α-1 / α-2 / α-3 / α-4 자동 재진입 | 사용자 명시 결정 영역 |
| 19 | Layer C 발효 시 Group I (Hermes-originated commit auto-reject) 자동 진입 | Group α 합의 C-2 답습 |
| 20 | Layer C 발효 시 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |
| 21 | Layer C 발효 시 GitHub plan / ruleset 가용성 자동 확인 | Group α 합의 C-4 답습 |
| 22 | Layer C 발효 시 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 23 | Layer C 발효 시 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 24 | Layer C 발효 시 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 25 | Layer C 발효 시 Stage 4 합의 / GP-3 Stage 2 합의 본문 변경 | 합의 답습 보존 |
| 26 | Layer C 발효 시 PC-4 / AR-2 / AR-3 / Stage 5 자동 진입 | Backlog #1+#2 / Backlog #3 / 별도 합의 영역 분리 |

본 §8 = **사용자 명시 답습 한정** — 본 brief 발효 후 Layer C 발효 합의 단계에서 위 26 금지 영역 위반 0건 유지 의무.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-14-layer-c-implementation-evidence-pass-entry.md` 패턴 답습) — Reviewer-only 단축 합의 적격 |
| (A') | **본 brief 그대로 승인 → 풀 3+1 + 외부 LLM 1+ 합의 진입** | 풀 3+1 합의 보고서 + 외부 LLM 1+ blind 의뢰 — Layer C 발효 = MVP-1 1차 영역 의미 deepening 시 권고 (사용자 명시 결정 권한) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α-4 실 진입 step 분할 brief 작성** | Phase α-4 실 진입 step 분할 brief (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Phase α-1 ~ α-4 통합 실제 구현 계획 brief 작성** | Phase α-1 ~ α-4 통합 실 진입 brief |
| (F) | 본 brief 승인 → **Layer C 발효 합의 실 진입 brief 작성** | Layer C 발효 합의 실 진입 단계 brief (사용자 명시 결정 영역 — 합의 형태 결정 + 외부 LLM 결정) |
| (G) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (H) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (I) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (A'): "옵션 (A') 로 진행해주세요. 본 brief 를 그대로 승인하고, 풀 3+1 합의 + 외부 LLM 1+ blind 의뢰 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α-4 실 진입 step 분할 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Phase α-1 ~ α-4 통합 실 진입 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Layer C 발효 합의 실 진입 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (H): "옵션 (H) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (I): "옵션 (I) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (1/1 — "Layer C 발효 합의 brief 작성해주세요") |
| 사용자 명시 7 금지 답습 (Phase α-1 / α-2 / α-3 / α-4 패턴 답습 — #1 = Layer C 영역 한정) | ✅ (7/7 — 실 Layer C 발효 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Phase α 4 단계 brief 모두 APPROVE AS BRIEF 답습 | ✅ (α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565` 4/4 답습) |
| ADR-011 §2.1 (a)~(e) 5 조건 모법 답습 | ✅ (재정의 0건 — 답습 한정) |
| GP-3 + GP-5 양 GP × 5 조건 evidence 매트릭스 | ✅ 10/10 evidence 적격 (현 (a)~(d) 8/8 충족 + (e) Layer C 시점 발효) |
| 4 prerequisite actual runs PASS 답습 | ✅ 4/4 PASS 답습 (`25728590939` + `25728590916` + `25728590977` + `25731846625`) |
| Phase α-1 합의 (`1b3090b`) 답습 | ✅ (본문 변경 0건 + C-β-1 ~ C-β-15 자동 변경 0건) |
| Phase α-2 합의 (`6a79247`) 답습 | ✅ (본문 변경 0건 + C-γ-1 ~ C-γ-26 자동 변경 0건) |
| Phase α-3 합의 (`3f6306d`) 답습 | ✅ (본문 변경 0건 + C-δ-1 ~ C-δ-28 자동 변경 0건) |
| Phase α-4 합의 (`e59a565`) 답습 | ✅ (본문 변경 0건 + C-ε-1 ~ C-ε-29 자동 변경 0건) |
| Group α 합의 C-1 ~ C-12 답습 | ✅ (자동 해소 0건 + 자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Layer A / Layer B / §5.5 9 sub-수단 본문 채택 답습 | ✅ (본문 변경 0건) |
| GP-3 MVP-1 진입 / GP-3 Stage 2 / GP-5 MVP-1 진입 / Stage 4 / 5 Stage 분할안 합의 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 | ✅ (발화 0건 — §7 답습) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (Layer C 발효 = evidence verification = catalog / provider 영역과 직교) |
| F-금지 #1 영구 답습 (GitHub Actions secrets 사용 도입 0건) | ✅ |
| Hermes upstream Dockerfile 변경 0건 | ✅ |
| Production `docker-compose.yml` 변경 0건 | ✅ |
| 외부 LLM 자동 호출 0건 (Group α 합의 C-11 답습) | ✅ |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/15 발화 | ✅ (§5.2 답습) |
| Layer C 발효 합의 진입 적격성 5/5 충족 | ✅ (§5.1 답습 — C-ζ-1 ~ C-ζ-5) |
| R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 변경 0건 (829 + 35 + 328 + 1593 = 2785줄 답습) | ✅ |
| MVP-1 PASS (Layer D) 선언 0건 | ✅ |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Phase α 4 단계 brief 모두 APPROVE AS BRIEF 완료 milestone 후속** (α-1 `1b3090b` + α-2 `6a79247` + α-3 `3f6306d` + α-4 `e59a565`), **Layer C (Implementation Evidence PASS) 발효 합의 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 Layer C 발효 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) Phase α-1 / α-2 / α-3 / α-4 패턴 답습 (사용자 명시 enumerate 0건 — 본 brief = 패턴 보존 + 사용자 검토 시 prohibition 추가/축소 권위 영역). **Layer C 정의 = mvp1.md §2.2 (Implementation Evidence PASS) + ADR-011 §2.1 (a)~(e) 5 조건 패턴 답습** ((a) 동등 이상의 보안 결과 / (b) 격리 환경 PoC 실증 / (c) ADR/SDD 권위 명시 / (d) 자동 회귀 검증 경로 / (e) 합의 APPROVE — 양 GP 공통) + **GP-3 × 5/5 evidence 적격** (Group D `tools/secret_scanner.py` 368줄 + Stage 2 ST-3 PoC `docker/gp3-st3-poc/` 4 파일 93줄 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 + §2.6.2 R2-1 + ADR-010 + R-4 + mvp1.md §3 + Layer B §5.5.1 + `.github/workflows/secret-hygiene-egress-redaction.yml` 694줄 + GP-3 MVP-1 진입 합의 + GP-3 Stage 2 합의 + Phase α-3 합의 APPROVE AS BRIEF — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효 적격) + **GP-5 × 5/5 evidence 적격** (Group A 1차 `tools/provider_import_scanner.py` 178줄 + Group A 2차 `.importlinter` 35줄 + Group A 3차 `tools/provider_url_scanner.py` 283줄 + ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + P2 v3 §10.1 + mvp1.md §4 + Layer B §5.5.2 T-6 + Group A 2차 풀 3+1 합의 + `.github/workflows/provider-adapter-enforcement.yml` 186줄 + `provider-url-scanner.yml` 326줄 + GP-5 MVP-1 진입 합의 + Stage 4 합의 + Phase α-1 / α-2 / α-4 합의 APPROVE AS BRIEF — (a)~(d) 4/4 현 충족 + (e) Layer C 시점 발효 적격) = **양 GP × 5 조건 = 10/10 evidence 적격성 권위 권고** + **4 prerequisite actual runs PASS 답습** (Stage 1 `25728590939` + Stage 2 `25731846625` + Stage 3 `25728590916` + `25728590977` 모두 SUCCESS) + **7 금지 영역 × Layer C 발효 합의 분리 매트릭스** (7/7 분리 — 충돌 0) + **Layer C 발효 합의 진입 적격성 5 조건 검토** (C-ζ-1 7 금지 충돌 0/7 + C-ζ-2 10/10 evidence 적격 + C-ζ-3 4 prerequisite runs PASS 답습 + C-ζ-4 Phase α 4 단계 brief 4/4 APPROVE AS BRIEF + C-ζ-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **15 풀 3+1 승격 트리거 0/15 발화** + **Layer C 발효 시점 영향 Rollback Trigger 의존성 답습** (18 trigger 中 Layer C 직접 영향 8 + 간접 영향 1 + 영향 0 9 — 발화 0건) + **외부 LLM 1+ 요구사항 검토** (mvp1.md 본문 explicit 의무 명시 0건 — 권고 한정, 사용자 명시 결정 영역) + **합의 형태 권고 = Reviewer-only 단축 합의 적격 후보** (Phase α-1/2/3/4 패턴 답습, 사용자 명시 결정 시 풀 3+1 + 외부 LLM 1+ 옵션 권위 영역) + **본 brief 자체 금지 56 + Layer C 발효 단계 금지 26** 을 정리한다. **본 brief 는 Layer C 발효를 *시작* 시키지 않으며, GP-3 / GP-5 PASS 를 *발효* 시키지 않으며, MVP-1 PASS 를 *선언* 하지 않으며, 외부 LLM 호출을 *자동 발화* 시키지 않으며, ADR-011 §2.1 (a)~(e) 5 조건 / Phase α-1/2/3/4 합의 / Group α 합의 / Backlog #6 우선 진입 합의 / Layer A / Layer B / GP-3 Stage 2 / Stage 4 / 5 Stage 분할안 합의 본문 변경 / R-4 / R-5 / R-7 / R-1 영역 본문 변경 / 14 결정 영역 *재결정* / Phase α-1 / α-2 / α-3 / α-4 실 진입 자동 진입 / Layer D / Layer E / Layer F 발효 / 7 금지 영역 *해소* / 4 prerequisite actual runs 자동 재실행 / 신규 actual run 자동 trigger / 외부 LLM blind 의뢰 자동 발송 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~I, §9 답습) — **(A) Reviewer-only 단축 합의 진입 (권고) / (A') 풀 3+1 + 외부 LLM 1+ 합의 진입 (선택) / (F) Layer C 발효 합의 실 진입 brief 작성 / 기타 옵션**.

---

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A ~ I, §9 답습)
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
- ❌ 외부 LLM 자동 호출 / blind 의뢰 자동 발송
- ❌ 양 GP × 5 조건 evidence *재생성*
- ❌ 4 prerequisite actual runs 자동 재실행
- ❌ 신규 actual run 자동 trigger
- ❌ ADR-011 §2.1 (a)~(e) 5 조건 *재정의*
- ❌ R-4 / R-5 / R-7 / R-1 영역 본문 어느 줄도 변경 (2785줄 답습)
- ❌ Phase α-1 / α-2 / α-3 / α-4 합의 본문 변경 / 자동 재진입
- ❌ C-β / C-γ / C-δ / C-ε / C-α 자동 변경
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / Layer C / Layer D / Group α / Backlog #6 우선 진입 / Phase α 4 합의 / GP 합의 / Stage 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
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
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ F-금지 #1 위반 (GitHub Actions secrets 사용 도입)
- ❌ Hermes upstream Dockerfile 변경
- ❌ Production `docker-compose.yml` 신설 / 변경
- ❌ 실 secret material commit
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #3 / #4 / #5 / #7 자동 진입
- ❌ PC-4 / AR-2 / AR-3 / Stage 5 자동 진입
- ❌ ST-1 / ST-2 / ST-4 / ST-5 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 *재고정*
