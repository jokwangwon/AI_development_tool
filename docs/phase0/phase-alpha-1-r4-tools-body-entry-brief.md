# Phase α-1 R-4 도구 본문 진입 Brief (준비안 — DRAFT)

> **본 문서는 Backlog #6 Runtime + CI-hook 우선 진입 합의 (`docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md`, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) 발효 후속, Phase α 4 단계 中 α-1 (R-4 도구 본문) *진입 가능성 검토* 한정 의 brief 준비안.**
>
> 본 brief = *준비안 (DRAFT)* — 사용자 명시 승인 *전* 단계. 본 brief 의 어떤 §도 그 자체로 (i) Phase α-1 실 진입을 발효시키지 않으며, (ii) 합의 보고서 권위를 갖지 않으며, (iii) Group α 합의 C-1 ~ C-12 / 사용자 명시 5 금지 中 어느 것도 *해소* 시키지 않는다.

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF)
- `docs/phase0/backlog6-runtime-ci-hook-priority-entry-brief.md` (commit `233892b`)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/phase0/backlog6-implementation-step-brief.md` §2.2.1 + §2.2.3 (Stage 1 + Stage 3 sub-step 답습)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §5.5 (9 sub-수단 본문 채택, commit `55c5b4b`)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T3 영역

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습

> "Phase α-1 R-4 도구 본문 진입 brief를 작성해주세요. 범위는 Backlog #6 Runtime + CI-hook priority 합의의 Phase α-1, 즉 R-4 도구 본문 진입 가능성 검토입니다. 실 runtime code 구현, CI workflow 변경, branch protection 변경, dev 환경 강제, pre-commit install 의무화, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

### 0.2 본 brief 가 *하는* 것

1. Backlog #6 우선 진입 합의 §6.1 1순위 답습 — Phase α-1 = R-4 도구 본문 영역 *진입 가능성 검토 한정* (§1)
2. **R-4 영역 = 3 도구 (`secret_scanner.py` + `provider_import_scanner.py` + `provider_url_scanner.py`) 정의** + 현 상태 enumeration (§2)
3. **3 도구 × Phase α-1 본문 작업 후보 분할 매트릭스** (§3)
4. **사용자 명시 7 금지 영역 × R-4 도구 본문 분리 매트릭스** (§4)
5. **Phase α-1 진입 적격성 5 조건 검토** (5 금지 충돌 0 + PoC 답습 변경 0 + 의존성 + Provider Liquidity 보존 + 풀 3+1 트리거 미발화, §5)
6. **Rollback Trigger 의존성 답습** — R-4 영역에 영향 받는 trigger enumerate (§6)
7. 본 brief + 본 brief 발효 후 단계의 *금지 사항* enumerate (§7)
8. 본 brief 의 *합의 형태 권고* + 풀 3+1 승격 트리거 후보 (§8)
9. 다음 단계 결정 옵션 (사용자 결정 영역, §9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 답습)

**사용자 명시 7 금지 영역**:

- ❌ **실 runtime code 구현 (0건)** — `tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py` 본문 변경 / 추가 / 삭제 0건
- ❌ **CI workflow 변경 (0건)** — `.github/workflows/*.yml` 신설 / 본문 변경 / 삭제 0건
- ❌ **branch protection 변경 (0건)** — AR-2 (CODEOWNERS + required status check) / direct push 차단 / force push 차단 / admin bypass OFF / required PR review count / linear history / deployments 모두 변경 0건 (Group α 합의 5.1 #6 답습)
- ❌ **dev 환경 강제 (0건)** — `tools/doctor.py` 신규 도구 본문 작성 / dev 환경 검증 강제 / `pre-commit run` 의무 실행 모두 0건
- ❌ **`pre-commit install` 의무화 도입 (0건)** — `.pre-commit-config.yaml` 본문 작성 / opt-in → doctor → required 단계 진입 / `default_install_hook_types` 본문 결정 모두 0건 (Group α 합의 5.2 #9 답습)
- ❌ **Operational Readiness PASS (Layer E) 선언 (0건)** — MVP-6 영역 분리 답습
- ❌ **Hermes PMO 격상 (Layer F) (0건)** — ADR-008 부록 C Hermes PMO Activation Cross-Reference 12 조건 미진입 답습

**추가 금지 영역 (본 brief 영역 외)**:

- ❌ **실 hook 구현 (0건)** — `.git/hooks/pre-commit` 본문 작성 / `.importlinter` 본문 변경 0건
- ❌ **Phase α-2 / α-3 / α-4 자동 진입 (0건)** — R-5 `.importlinter` 본문 / R-7 docker secret block / R-1 CI workflow 통합 모두 영역 외
- ❌ **Phase β / γ 자동 진입 (0건)** — R-6 / R-10 / R-2 / branch protection / commit signing / Vault HSM / Layer E / Layer F 모두 영역 외
- ❌ **Implementation Evidence PASS (Layer C) 발효 0건** + **MVP-1 PASS (Layer D) 선언 0건**
- ❌ **R-4 도구 본문 *재설계* (0건)** — Group D 261줄 + Group A 1차 + Group A 3차 PoC 답습 한정 (현 라인 수: secret 368 / import 178 / url 283 — 답습 본문 변경 0건)
- ❌ **R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 (0건)** — Group α 합의 5.1 #8 + Backlog #3 별도 합의 영역
- ❌ **Tier-2 / Tier-3 catalog 자동 확장 (0건)**
- ❌ **threshold *고정* (0건)** — FP / FN / latency 모두 *후보 한정* 유지
- ❌ **Group α 14 결정 영역 *재결정* (0건)**
- ❌ **Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 본문 변경 (0건)**
- ❌ **§5.5 9 sub-수단 본문 채택 변경 (0건)**
- ❌ **Group I (Hermes-originated commit auto-reject) 자동 진입 (0건)**
- ❌ **token rotation 정책 자동 결정 (0건)**
- ❌ **GitHub plan / ruleset 가용성 자동 확인 (0건)**
- ❌ **commit signing 도입 (0건)** — MVP-6 영역 답습
- ❌ **`pull_request_target` workflow 도입 (0건)**
- ❌ **ADR 본문 자동 갱신 (0건)** — cross-reference 답습 한정
- ❌ **신규 ADR / 신규 P / 신규 GP 발행 (0건)**
- ❌ **합의 보고서 작성 (0건)** — 본 brief = *준비안 한정*
- ❌ **CONTEXT / INDEX / SESSION 메타 갱신 (0건)**
- ❌ **git commit / push (0건)**
- ❌ **외부 LLM 자동 호출 (0건)** — Group α 합의 C-11 답습 (응답 = 입력 한정)
- ❌ **실 API key / provider SDK / 외부 API 호출 (0건)**
- ❌ **인간 리뷰 의무 자동 발화 (0건)**
- ❌ **`src/adapters/llm/facade.py` real 본문 작성 (0건)** — Backlog #4 영역 분리

### 0.4 본 brief 의 권위 한계

본 brief = **준비안 (DRAFT)**. 본 brief 의 어떤 §도:

- (i) Phase α-1 실 진입을 *시작* 시키지 않으며,
- (ii) Group α 합의 C-1 ~ C-12 의 어느 조건도 *해소* 시키지 않으며,
- (iii) 사용자 명시 7 금지 영역 어느 것도 진입시키지 않으며,
- (iv) Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 본문을 *변경* 하지 않으며,
- (v) R-4 도구 본문 (`tools/secret_scanner.py` / `tools/provider_import_scanner.py` / `tools/provider_url_scanner.py`) 어느 줄도 *변경* 하지 않으며,
- (vi) Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 을 *발생시키지 않는다*.

본 brief 가 발생시키는 *유일한* 효과는 **Phase α-1 R-4 도구 본문 영역의 *진입 가능성 검토* — 3 도구 정의 + 본문 작업 후보 분할 매트릭스 + 7 금지 분리 매트릭스 + 진입 적격성 5 조건 검토 + Rollback Trigger 의존성 + 금지 영역 enumeration + 합의 형태 권고**. 모든 *진입 결정* 은 *사용자 명시 결정 영역*.

---

## 1. 진입 컨텍스트 답습

### 1.1 Backlog #6 우선 진입 합의 §6.1 1순위 답습 (`c7ddfdd`)

| 영역 | 답습 |
|------|----|
| 합의 판정 | APPROVE AS BRIEF (Reviewer-only 단축 합의, 7/7 풀 3+1 트리거 0건 발화) |
| 합의 단위 | Backlog #6 우선 진입 brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| Phase α 4 단계 | α-1 (R-4) / α-2 (R-5) / α-3 (R-7) / α-4 (R-1) |
| Phase α-1 정의 (합의 §5.2 답습) | R-4 도구 본문 (Stage 1 + Stage 3) — Stage 1 (S-1 `secret_scanner.py`) + Stage 3 (T-6 `provider_import_scanner.py` + `provider_url_scanner.py`) 병렬 진입 적격 |
| 진입 우선순위 (합의 §6.1) | **1순위** — Phase α-1 + α-2 + α-3 병렬 진입 적격 |
| 진입 결정 권위 | **Backlog #6 실 진입 + 사용자 명시 결정 영역** (본 합의 영역 외) |

### 1.2 Backlog #6 우선 진입 합의 §6.2 권고 한계 답습

> 본 합의 = **Phase α 우선 진입 *권위 권고 발행 한정***
> 실 Phase α 진입 = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
> 자동 진입 0건

본 brief 의 의미:

- (a) Backlog #6 우선 진입 합의 발효 *자체* = 완료 (`c7ddfdd`)
- (b) Phase α-1 R-4 도구 본문 *실 진입* = **Backlog #6 실 진입 + 사용자 명시 결정 영역**
- (c) 본 brief = (b) *진입 가능성 검토 한정* — 실 진입 *직전* 의사결정 사전 정비 영역
- (d) 본 brief = Backlog #6 우선 진입 합의의 5 금지 영역 *해소* 가 아님

### 1.3 6-Layer 분리 매트릭스 현 상태 (2026-05-15)

| Layer | 영역 | 상태 | 본 brief 관계 |
|-------|------|------|------------|
| Layer A | Backlog #6 Implementation Entry 기준 정의 | ✅ APPROVE (`f1e0b23`) | 답습 한정 |
| Layer B | 9 sub-수단 본문 채택 격상 | ✅ APPROVE (`f40423f` + §5.5 `55c5b4b`) | 답습 한정 (재결정 0건) |
| Group α | AR-3 + PC-4 T3 sub 단독 풀 3+1 (T3 영역 권위 권고) | ✅ APPROVE WITH CONDITIONS (`4880e88`, 3/3 만장일치) | 답습 한정 (C-1 ~ C-12 해소 0건) |
| Backlog #6 우선 진입 | Runtime + CI-hook 영역 정의 + Phase α 권고 | ✅ APPROVE AS BRIEF (`c7ddfdd`) | **본 brief = §6.1 1순위 *진입 가능성 검토*** |
| Layer C | Implementation Evidence PASS 발효 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer D | MVP-1 PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 |
| Layer E | Operational Readiness PASS 선언 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #6) |
| Layer F | Hermes PMO 격상 | ⏳ 아직 아님 | 본 brief 영역 외 (사용자 명시 7 금지 #7) |

### 1.4 본 brief 의 진입점

```
Layer A APPROVE (f1e0b23) ─────┐
Layer B APPROVE (f40423f)      │
§5.5 9 sub-수단 (55c5b4b)       │
Group α APPROVE (4880e88) ─────┤
backlog6 priority brief (233892b)
Backlog #6 우선 진입 합의 (c7ddfdd) APPROVE AS BRIEF
   │
   ▼
■ 본 brief = Phase α-1 R-4 도구 본문 *진입 가능성 검토* (DRAFT)    ← 현 위치
   │
   ▼ (사용자 명시 승인 후 — 자동 진입 0건)
brief 그대로 승인 합의 보고서 작성 (Reviewer-only 단축 적격 후보)
   │
   ▼ (사용자 명시 결정 후 — 자동 진입 0건)
■ Phase α-1 실 진입 (R-4 도구 본문 변경)                            ← 본 brief 영역 외
   │
   ▼ (R-4 + R-5 + R-7 + R-1 완료 + actual run SUCCESS + evidence 5/5 후)
Layer C 발효 합의 — Implementation Evidence PASS                   ← 본 brief 영역 외
```

---

## 2. R-4 영역 정의 (Phase α-1 한정)

### 2.1 R-4 = 3 도구 정의 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5 답습)

| 도구 | 영역 | 답습 출처 | 현 라인 수 (2026-05-15 기준) | Stage |
|------|----|----------|---------------------------|-------|
| `tools/secret_scanner.py` | GP-3 S-1 — 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC (`docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md`) 답습 | 368 | Stage 1 |
| `tools/provider_import_scanner.py` | GP-5 T-2 — Layer 1 정적 차단 (5-vendor AST 패턴) | Group A 1차 PoC (`docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md`) 답습 | 178 | Stage 3 |
| `tools/provider_url_scanner.py` | GP-5 T-5 — URL/Model Tier-1 정적 차단 (URL Tier-1 10 + Model Tier-1 19) | Group A 3차 PoC (`docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md`) 답습 | 283 | Stage 3 |

**합산**: 3 도구 × 829줄 PoC 본문 답습 (Group D 368 + Group A 1차 178 + Group A 3차 283).

### 2.2 R-4 도구 = Layer B §5.5 9 sub-수단 中 S-1 + T-2 + T-5 (T-6 합산) 답습

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-4 도구 |
|----------|------|----------------------|----------|
| S-1 | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | `secret_scanner.py` |
| T-2 | Layer 1 정적 차단 (custom AST) | Group A 1차 답습 | `provider_import_scanner.py` |
| T-5 | URL/Model 정적 차단 | Group A 3차 답습 | `provider_url_scanner.py` |
| T-6 | T-2 + T-5 통합 (import-linter 병행 = R-5 영역, Phase α-2) | Group A 2차 답습 | — (R-5 영역) |

본 brief 영역 = R-4 (S-1 + T-2 + T-5) 한정. **R-5 (`.importlinter` 본문) = Phase α-2 영역 — 본 brief 영역 외**.

### 2.3 R-4 도구 본문 = Phase α-1 영역 *내* vs *외*

| 영역 | 본 brief 영역 *내* (진입 가능성 검토) | 본 brief 영역 *외* (실 진입 = Backlog #6 + 사용자 명시 결정 영역) |
|------|----------------------------|--------------------------------------|
| 3 도구 본문 답습 검증 | ✅ enumerate 한정 (변경 0건) | 실 본문 변경 (MVP-1 entry 확장 / CI workflow 호환 / ledger entry 형식) |
| R-4.1 Tier-1 45 patterns 답습 | ✅ enumerate 한정 | 실 패턴 추가 / 변경 (= Tier-2 확장 영역 분리) |
| URL Tier-1 10 + Model Tier-1 19 답습 | ✅ enumerate 한정 | 실 catalog 변경 (= Group α 합의 5.1 #8 별도 합의 영역) |
| 의존성 매트릭스 정리 | ✅ 의존성 enumerate 한정 | — |
| 진입 적격성 5 조건 검토 | ✅ 검토 한정 | 실 진입 결정 = 사용자 명시 결정 영역 |

---

## 3. 3 도구 × Phase α-1 본문 작업 후보 분할 매트릭스

### 3.1 Stage 1 — `secret_scanner.py` (S-1) sub-step 분할 (Layer B §2.2.1 답습)

| sub-step | 영역 | 답습 출처 | Phase α-1 진입 시 본 작업 후보 (본 brief 영역 외 — 실 진입 시점 결정) |
|---------|------|---------|---------------------------------------|
| 1.1 | 본문 답습 검증 | Group D PoC §2.1 (A) — 261줄 → 368줄 (이미 확장됨) | 답습 변경 0건 — 현 368줄 답습 검증 |
| 1.2 | MVP-1 entry CI 통합 인터페이스 정렬 (Stage 1 본 도구 측면 한정) | Group D 12 step 답습 + Layer B §1.1 답습 | CLI 인자 / exit code / 출력 포맷 답습 검증 — 실 workflow 변경은 R-1 영역 (Phase α-4) |
| 1.3 | ledger entry 형식 답습 — `event: secret_scan_layer1_implementation` 후보 | mvp1.md §5.2 enum *후보 한정* 답습 | 정식 등록 0건 (Backlog #5 별도 합의 영역) |
| 1.4 | Evidence Artifact 형식 답습 (Markdown report 출력 후보) | Layer B §1.8 (a) 답습 | 실 생성 = Layer C 시점 (본 brief 영역 외) |

### 3.2 Stage 3 — `provider_import_scanner.py` (T-2) sub-step 분할 (Layer B §2.2.3 부분 답습)

| sub-step | 영역 | 답습 출처 | Phase α-1 진입 시 본 작업 후보 (본 brief 영역 외) |
|---------|------|---------|---------------------------------------|
| 3.2 | 본문 답습 검증 | Group A 1차 PoC 답습 (AST 5 패턴) — 현 178줄 답습 검증 | 답습 변경 0건 |
| 3.2.a | CLI 인자 / exit code / 출력 포맷 답습 검증 | Group A 1차 답습 | 실 workflow 변경은 R-1 영역 (Phase α-4) |
| 3.2.b | facade exemption (`src/adapters/llm/facade.py`) 답습 검증 | Group A 1차 §5 답습 | 실 facade 본문 = Backlog #4 영역 (본 brief 영역 외) |

### 3.3 Stage 3 — `provider_url_scanner.py` (T-5) sub-step 분할 (Layer B §2.2.3 부분 답습)

| sub-step | 영역 | 답습 출처 | Phase α-1 진입 시 본 작업 후보 (본 brief 영역 외) |
|---------|------|---------|---------------------------------------|
| 3.3 | 본문 답습 검증 | Group A 3차 PoC 답습 (URL Tier-1 10 + Model Tier-1 19) — 현 283줄 답습 검증 | 답습 변경 0건 |
| 3.3.a | URL Tier-1 catalog 답습 검증 | Group A 3차 §4 답습 | 실 catalog 변경 = Backlog #3 별도 합의 영역 (Tier-2/3 확장 분리) |
| 3.3.b | Model Tier-1 catalog 답습 검증 | Group A 3차 §5 답습 | 동상 |
| 3.3.c | CLI 인자 / exit code / 출력 포맷 답습 검증 | Group A 3차 답습 | 실 workflow 변경은 R-1 영역 (Phase α-4) |

### 3.4 합산 매트릭스

| Stage | 도구 | sub-step | 신규 작업 비율 (실 진입 시점) | PoC 답습 비율 | 본 brief 영역 |
|-------|------|---------|------------------------|------------|------------|
| Stage 1 | `secret_scanner.py` | 4 | 中 (CI 통합 인터페이스 + ledger 형식) | 高 (Group D 답습) | enumerate 한정 |
| Stage 3 (T-2) | `provider_import_scanner.py` | 3 | 低 (PoC 답습 변경 0건) | 高 (Group A 1차 답습) | 동상 |
| Stage 3 (T-5) | `provider_url_scanner.py` | 4 | 低 (PoC 답습 변경 0건) | 高 (Group A 3차 답습) | 동상 |
| **합산** | **3 도구** | **11 sub-step** | — | — | — |

### 3.5 본 §3 의 *범위 한계*

본 §3 = **본문 작업 후보 *분할 매트릭스 정리 한정***. 실 sub-step 결정 / 실 도구 본문 변경 = 사용자 명시 결정 영역 + Phase α-1 실 진입 시점 (Backlog #6 + 사용자 명시 결정 영역 — 본 brief 영역 외).

---

## 4. 사용자 명시 7 금지 영역 × R-4 도구 본문 분리 매트릭스

### 4.1 금지 #1 — 실 runtime code 구현 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/secret_scanner.py` 본문 변경 | ❌ (영역 외) | Phase α-1 실 진입 후 영역 |
| `tools/provider_import_scanner.py` 본문 변경 | ❌ (영역 외) | 동상 |
| `tools/provider_url_scanner.py` 본문 변경 | ❌ (영역 외) | 동상 |
| `src/adapters/llm/facade.py` 본문 작성 | ❌ (영역 외) | Backlog #4 영역 분리 |
| **본 brief 영역 *내* 적격 작업** | **3 도구 *답습 출처 + 현 라인 수 enumerate 한정* + sub-step 후보 enumerate** | — |

### 4.2 금지 #2 — CI workflow 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.github/workflows/*.yml` 신설 | ❌ (영역 외) | Phase α-4 영역 (R-1) |
| 기존 workflow 본문 변경 | ❌ (영역 외) | 동상 |
| CI step `pre-commit run --all-files` 추가 | ❌ (영역 외) | R-2 영역 (Phase β-3, 금지 #5 해소 의존) |
| **본 brief 영역 *내* 적격 작업** | **3 도구 CLI 인터페이스 답습 *enumerate 한정* (workflow 호환성 답습 한정 — 실 변경 0건)** | — |

### 4.3 금지 #3 — branch protection 변경 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| AR-2 형태 (e) CODEOWNERS + required check 실 활성화 | ❌ (영역 외) | Group α 합의 발효 후 Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| direct push 차단 / force push 차단 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-4 도구 본문 = 코드 영역, branch protection = GitHub Web UI 영역 — 직교)** | — |

### 4.4 금지 #4 — dev 환경 강제 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `tools/doctor.py` 신규 도구 본문 작성 | ❌ (영역 외) | R-10 영역 (Phase β-2) |
| dev 환경 검증 강제 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-4 도구 = scanner 영역, R-10 = doctor 영역 — 분리)** | — |

### 4.5 금지 #5 — `pre-commit install` 의무화 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| `.pre-commit-config.yaml` 본문 작성 | ❌ (영역 외) | R-6 영역 (Phase β-1) |
| `default_install_hook_types` 본문 결정 | ❌ (영역 외) | 동상 |
| `pre-commit install` opt-in → doctor → required 단계 진입 | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **3 도구 hook framework 호환성 답습 *enumerate 한정* (실 hook 등록 0건)** | — |

### 4.6 금지 #6 — Operational Readiness PASS (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer E 선언 | ❌ (영역 외) | MVP-6 영역 / Backlog #7 영역 |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ (영역 외) | 동상 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-4 도구 = 구현 영역, Layer E = 운영 영역 — 분리)** | — |

### 4.7 금지 #7 — Hermes PMO 격상 (분리 매트릭스)

| 영역 | 본 brief 영역 *내* | 본 brief 영역 *외* (별도 결정) |
|------|----------------|------------------------|
| Layer F (Hermes PMO 격상) | ❌ (영역 외) | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |
| **본 brief 영역 *내* 적격 작업** | **0건 (R-4 도구 = 코드 영역, Layer F = governance 영역 — 직교) + Hermes ≠ root of trust 보존 답습** | — |

### 4.8 본 §4 의 *범위 한계*

본 §4 = **7 금지 영역 *분리 매트릭스 한정***. 7 금지 영역 어느 것도 *해소* 0건 + Phase α-1 실 진입 자동 진입 0건.

---

## 5. Phase α-1 진입 적격성 5 조건 검토

### 5.1 적격성 검토 매트릭스

| 조건 # | 조건 | 본 brief 검토 결과 | 판정 |
|------|------|------------------|----|
| **C-α1-1** | **사용자 명시 7 금지 영역 충돌 0** | R-4 도구 본문 = 코드 영역 — 금지 #3 (branch protection) / #4 (dev 환경 강제) / #5 (pre-commit install 의무화) / #6 (Layer E) / #7 (Layer F) 모두 직교 (충돌 0). 금지 #1 (실 code 구현) / #2 (CI workflow 변경) = Phase α-1 *실 진입* 시점 적용 — 본 brief = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α1-2** | **PoC 답습 변경 0** | 3 도구 (Group D 368 + Group A 1차 178 + Group A 3차 283) PoC 답습 한정 + R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 0건 | ✅ **답습 100% 보존** |
| **C-α1-3** | **의존성 0 (Stage 1 + Stage 3 병렬 진입 적격)** | Stage 1 (S-1) ↔ Stage 3 (T-2 + T-5) = 양 GP 독립 (의존성 0) + R-5 / R-7 / R-1 = Phase α-2 / α-3 / α-4 영역 (본 brief 영역 외 — Phase α-1 진입 적격성 영향 0) | ✅ **의존성 0 (병렬 진입 적격)** |
| **C-α1-4** | **Provider Liquidity 5-way 100% 보존** | R-4 도구 = enforcement layer 영역 — catalog / provider 영역과 직교 + Tier-1 답습 한정 + 5-vendor 차단 패턴 답습 변경 0건 | ✅ **5/5 100% 보존** |
| **C-α1-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-4 = 코드 영역, Hermes PMO 영역 분리) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-4 = 수단, 목적 = secret 검출 + provider 차단) / T1/T2/T3 분리 보존 (R-4 = T2 영역 → T3 영역 진입 0건) / SPOF 의도적 수용 보존 (R-4 = enforcement single point 답습) | ✅ **5/5 보존** |

### 5.2 풀 3+1 승격 트리거 검토 (Backlog #6 우선 진입 합의 §7 답습)

| # | 트리거 | 본 brief 발화 |
|---|----|----------|
| 1 | 본 brief 가 Group α 합의 C-1 ~ C-12 어느 것의 *재결정* 을 권고하는 경우 | ❌ 0건 — 본 brief = Group α 답습 한정 |
| 2 | 본 brief 가 사용자 명시 7 금지 영역 中 1+ 의 *해소* 를 권고하는 경우 | ❌ 0건 — 본 brief = 분리 매트릭스 한정 |
| 3 | 본 brief 가 Layer B §5.5 9 sub-수단 *재결정* 을 권고하는 경우 | ❌ 0건 — 본 brief = 답습 한정 |
| 4 | 본 brief 가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 — enforcement layer = catalog / provider 영역과 직교 |
| 5 | 본 brief 가 5 영구 핵심 제약 中 1+ 의 약화를 포함하는 경우 | ❌ 0건 — 5/5 보존 답습 |
| 6 | 본 brief 가 T3 영역 진입을 권고하는 경우 | ❌ 0건 — T3 분리 명시 한정 (R-4 = T2 영역) |
| 7 | 본 brief 가 ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 의 충족을 발생시키는 경우 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | 본 brief 가 R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 catalog 변경을 권고하는 경우 | ❌ 0건 — catalog 답습 한정 (Tier-2/3 확장 분리) |

**검토 결과**: **8/8 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 후보 확정** (사용자 명시 결정 시).

### 5.3 종합 적격성 판정 (본 brief 권고 한정)

| 영역 | 판정 |
|------|----|
| 5 조건 (C-α1-1 ~ C-α1-5) | **5/5 충족** |
| 8 풀 3+1 트리거 | **0/8 발화** |
| **Phase α-1 진입 적격성** | **적격 (사용자 명시 결정 영역 — 자동 진입 0건)** |

### 5.4 본 §5 의 *범위 한계*

본 §5 = **진입 적격성 *검토 한정***. 실 Phase α-1 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건). 본 brief 의 적격 판정 = 적격성 권위 권고 한정 — 실 진입 발효 권위 0건.

---

## 6. Rollback Trigger 의존성 답습

### 6.1 R-4 영역에 영향 받는 Rollback Trigger 답습 (Layer B §1.7 + mvp1.md §3.5 + §4.6 답습)

본 §은 **18 Rollback Trigger 中 R-4 도구 본문 영역 *영향* 받는 trigger enumerate 한정** — 발화 0건 + 본 brief 영역 *내 의존성 정리 한정*:

| Trigger | 발화 조건 | R-4 도구 영향 | 본 brief 영역 |
|--------|---------|-----------|------------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (>5%) | `secret_scanner.py` 본문 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-2 | S-2 gitleaks 라이선스 변경 | 영향 0 (MVP-1 = S-1 단독 답습) | 영역 외 (Backlog #1 1.5차 보강 영역) |
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | 영향 0 (R-7 영역) | 영역 외 (Phase α-3) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | `secret_scanner.py` 성능 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G3-5 | AR-1 hook 우회 시도 패턴 검출 | 영향 0 (T3 영역) | 영역 외 (Backlog #3) |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 | `secret_scanner.py` 본문 영향 | 영역 외 (Backlog #3 별도 합의) |
| R-MVP1-G3-7 | Tier-2 확장 필요 | `secret_scanner.py` 본문 영향 | 영역 외 (Backlog #1 1.5차 보강) |
| R-MVP1-G3-8 | Operational Readiness parity 필요 | 영향 0 (Layer E 영역) | 영역 외 (금지 #6 답습) |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (>5%) | `provider_import_scanner.py` 본문 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 | `provider_url_scanner.py` 본문 영향 | 의존성 *enumerate 한정* (발화 0건) |
| R-MVP1-G5-3 | T-6 병행 충돌 (T-2 ↔ T-5 결과 불일치) | 양 도구 + R-5 영역 영향 | 의존성 *enumerate 한정* (R-5 = Phase α-2) |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 | 영향 0 (R-5 영역) | 영역 외 (Phase α-2) |
| R-MVP1-G5-5 | PC-3 hook 우회 시도 | 영향 0 (T3 영역) | 영역 외 (Backlog #3) |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 | 양 도구 + R-1 영역 영향 | 의존성 *enumerate 한정* (R-1 = Phase α-4) |
| R-MVP1-G5-7 | P1 v2 facade real 본문 필요 | `provider_import_scanner.py` facade exemption 영향 | 영역 외 (Backlog #4) |
| R-MVP1-G5-8 | branch protection 필요 trigger | 영향 0 (T3 영역) | 영역 외 (금지 #3 답습) |
| R-MVP1-G5-9 | 의미적 lock-in 검출 | 영향 0 (MVP-3 영역) | 영역 외 |
| R-MVP1-G5-10 | Layer 2 runtime 진입 필요 | 영향 0 (MVP-3/4 영역) | 영역 외 |

### 6.2 Group α 7 단계 승격 Trigger 답습 (R-4 영역 영향 — 답습 한정)

| Trigger | R-4 도구 영향 | 본 brief 영역 |
|--------|-----------|------------|
| R-MVP1-G5-AR3-STAGE 1차 (required status check 도입) | 영향 0 (R-1 영역) | 영역 외 (Phase α-4 + 금지 #3) |
| R-MVP1-G3-PC4T3-STAGE 1차 (opt-in → doctor warning) | 영향 0 (R-6 + R-10 영역) | 영역 외 (Phase β + 금지 #4 #5) |

### 6.3 합산

| 영역 | trigger 수 | 본 brief 영역 |
|------|---------|------------|
| **R-4 도구 본문 영역 *직접* 영향** | 5 (G3-1, G3-4, G5-1, G5-2, G5-3 부분) | 의존성 *enumerate 한정* — 발화 0건 |
| R-4 영역 *간접* 영향 (R-5/R-7/R-1/R-6/R-10 통합 trigger) | 3 (G5-3, G5-6 부분, AR3 STAGE) | 영역 외 (Phase α-2/α-3/α-4/β) |
| R-4 영역 *영향 0* (T3/MVP-3/MVP-6/Backlog 분리) | 10 | 영역 외 |

### 6.4 본 §6 의 *범위 한계*

본 §6 = **Rollback Trigger *본문 확정 답습 한정***. 발화 0건 + threshold 정량 *고정 0건* (>5% / >2분 모두 *후보 한정* 유지) + 신규 trigger 추가 0건.

---

## 7. 금지 사항

### 7.1 본 brief 자체 금지 사항 (사용자 명시 답습)

| # | 금지 영역 | 본 brief 위반 |
|---|---------|------------|
| 1 | **실 runtime code 구현** (사용자 명시 7 금지 #1) | 0건 |
| 2 | **CI workflow 변경** (사용자 명시 7 금지 #2) | 0건 |
| 3 | **branch protection 변경** (사용자 명시 7 금지 #3) | 0건 |
| 4 | **dev 환경 강제** (사용자 명시 7 금지 #4) | 0건 |
| 5 | **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5) | 0건 |
| 6 | **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6) | 0건 |
| 7 | **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7) | 0건 |
| 8 | 실 hook 구현 (`.git/hooks/pre-commit` 본문 / `.importlinter` 본문 변경) | 0건 |
| 9 | Phase α-2 / α-3 / α-4 자동 진입 | 0건 |
| 10 | Phase β / γ 자동 진입 | 0건 |
| 11 | Implementation Evidence PASS (Layer C) 발효 | 0건 |
| 12 | MVP-1 PASS (Layer D) 선언 | 0건 |
| 13 | R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경 | 0건 |
| 14 | R-4.1 Tier-1 45 patterns / URL Tier-1 10 / Model Tier-1 19 catalog 변경 | 0건 |
| 15 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 16 | threshold *고정* (FP / FN / latency 등 = 후보 한정) | 0건 |
| 17 | Group α 합의 C-1 ~ C-12 자동 변경 | 0건 |
| 18 | Group α 14 결정 영역 *재결정* | 0건 |
| 19 | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 본문 변경 | 0건 |
| 20 | §5.5 9 sub-수단 본문 채택 변경 | 0건 |
| 21 | Group I (Hermes-originated commit auto-reject) 자동 진입 | 0건 |
| 22 | token rotation 정책 자동 결정 | 0건 |
| 23 | GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| 24 | commit signing 도입 | 0건 |
| 25 | `pull_request_target` workflow 도입 | 0건 |
| 26 | ADR 본문 자동 갱신 (cross-reference 답습 한정) | 0건 |
| 27 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 28 | 합의 보고서 작성 (본 brief = 준비안 한정) | 0건 |
| 29 | CONTEXT / INDEX / SESSION 메타 갱신 | 0건 |
| 30 | git commit / push | 0건 |
| 31 | 외부 LLM 자동 호출 (Group α 합의 C-11 답습 — 응답 = 입력 한정) | 0건 |
| 32 | 외부 LLM 응답 결론 강제 채택 (Group α 합의 C-11 답습) | 0건 |
| 33 | 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 34 | 인간 리뷰 의무 자동 발화 | 0건 |
| 35 | `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리) | 0건 |
| 36 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 37 | MVP-2 ~ MVP-6 본문 deepening | 0건 |

### 7.2 본 brief 발효 *후* Phase α-1 실 진입 단계 금지 사항 (의무 답습)

| # | 금지 영역 | 사유 |
|---|---------|------|
| 1 | Phase α-1 진입 시 9 sub-수단 외 수단 도입 (gitleaks / detect-secrets / trufflehog 등) | Backlog #1 1.5차 보강 영역 분리 |
| 2 | Phase α-1 진입 시 R-4.1 Tier-1 / URL Tier-1 10 / Model Tier-1 19 catalog 변경 | Backlog #3 별도 합의 영역 (Group α 합의 5.1 #8 답습) |
| 3 | Phase α-1 진입 시 `src/adapters/llm/facade.py` real 본문 작성 | Backlog #4 P1 v2 facade MVP 합의 영역 분리 |
| 4 | Phase α-1 진입 시 Hermes upstream Dockerfile 변경 | Backlog #1 1.5차 보강 영역 분리 (풀 3+1 합의) |
| 5 | Phase α-1 진입 시 ADR 본문 자동 갱신 | cross-reference 답습 한정 — Layer C 발효 후 별도 commit 영역 |
| 6 | Phase α-1 진입 시 event enum 정식 등록 (`event:` field) | Backlog #5 ADR-012 §2.2 schema 진화 정책 별도 합의 |
| 7 | Phase α-1 진입 시 `pull_request_target` workflow 도입 | T2/T3 별도 합의 영역 |
| 8 | Phase α-1 진입 시 local pre-commit framework 활성화 | Backlog #1 + #2 1.5차 보강 영역 분리 (사용자 명시 7 금지 #5 답습) |
| 9 | Phase α-1 진입 시 Layer 2 runtime block (G5-5) 진입 | MVP-3/4 영역 분리 |
| 10 | Phase α-1 진입 시 의미적 lock-in (G4 §4.6 라운드트립 검증) 진입 | MVP-3 영역 분리 |
| 11 | Phase α-1 진입 시 실 API key / provider SDK / 외부 API 호출 | 영구 금지 (fake canary 의무 답습) |
| 12 | Phase α-1 진입 시 실 secret 본문 commit | 영구 금지 (R-4.1 + Group D §1.2 #1 답습) |
| 13 | Phase α-1 진입 시 F-금지 위반 (workflow 본문 secret 토큰 사용 등) | 영구 금지 (G3-7 (i) 답습) |
| 14 | Phase α-1 진입 시 Layer C 자동 발효 (사용자 명시 결정 미충족 시) | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |
| 15 | Phase α-1 진입 시 Phase α-2 / α-3 / α-4 자동 진입 | Phase α 단계 = 사용자 명시 결정 영역 + Backlog #6 실 진입 영역 |
| 16 | Phase α-1 진입 시 Group I (Hermes-originated commit auto-reject) 자동 진입 | Group α 합의 C-2 답습 (Group I 별도 합의 영역) |
| 17 | Phase α-1 진입 시 token rotation 정책 자동 결정 | Group α 합의 C-3 답습 |

본 §7 = **사용자 명시 답습 한정** — 본 brief 발효 후 Phase α-1 실 진입 단계에서 위 17 금지 영역 위반 0건 유지 의무.

---

## 8. 합의 형태 권고 + 풀 3+1 승격 트리거

### 8.1 본 brief 의 합의 형태 권고

| 합의 영역 | 합의 형태 권고 | 사유 |
|---------|----------|------|
| 본 brief 자체 (DRAFT — 준비안) | **사용자 명시 승인 한정 (합의 보고서 0건)** | 본 brief = 준비안 한정 — 합의 보고서 권위 갖지 않음 |
| brief 승인 후 합의 진입 | **Reviewer-only 단축 합의 적격** | Backlog #6 우선 진입 합의 답습 한정 + 7 금지 영역 *재결정* 0건 + 본 brief = 진입 적격성 *검토 한정* (적격성 *해소* 0건) + 8/8 풀 3+1 트리거 0건 발화 (§5.2) |
| Phase α-1 실 진입 시 합의 | **별도 합의 — Reviewer-only 단축 또는 풀 3+1** | Layer B §5.5 9 sub-수단 본문 채택 답습 + Phase α-1 = 5 금지 충돌 0 영역 한정 (사용자 명시 결정 영역) |
| Layer C 발효 합의 | **별도 합의 — 단축 또는 풀 3+1 + 외부 LLM 1+** | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 |

### 8.2 풀 3+1 승격 트리거 후보 (본 brief 영역)

§5.2 답습 — **8/8 트리거 0건 발화** 확정.

→ 본 brief 승인 후 합의 = **Reviewer-only 단축 합의 적격** (사용자 명시 결정 시).

### 8.3 본 §8 의 *범위 한계*

본 §8 = *합의 형태 권고 한정*. 실 합의 형태 결정 = 사용자 명시 결정 영역.

---

## 9. 다음 단계 결정 옵션 (사용자 결정 영역)

본 brief 작성 후 다음 작업 (사용자 결정 영역, 자동 진입 0건):

| 옵션 | 영역 | 다음 단계 |
|-----|------|--------|
| **(A)** | **본 brief 그대로 승인 → Reviewer-only 단축 합의 진입** | 합의 보고서 작성 (`docs/review/3plus1-consensus-2026-05-15-phase-alpha-1-r4-tools-body-entry.md`) |
| (B) | 본 brief 수정 요청 → 수정 후 승인 | brief v2 작성 (사용자 명시 수정 영역 반영) |
| (C) | 본 brief 일부만 채택 → 부분 합의 | brief 부분 채택 영역 명시 + 합의 보고서 작성 |
| (D) | 본 brief 승인 → 합의 보류 → **Phase α-2 R-5 `.importlinter` 본문 진입 brief 작성** | Phase α-2 진입 가능성 검토 brief (사용자 명시 결정 영역) |
| (E) | 본 brief 승인 → **Phase α-3 R-7 docker secret block 진입 brief 작성** | Phase α-3 진입 가능성 검토 brief |
| (F) | 본 brief 승인 → **Phase α 4 단계 (α-1 + α-2 + α-3 + α-4) 통합 진입 brief 작성** | Phase α 통합 진입 brief (병렬 진입 적격 답습) |
| (G) | 본 brief 승인 → **Phase α-1 실 진입 brief 작성** (DRAFT — 실 R-4 도구 본문 변경 step 분할안) | Phase α-1 실 진입 step 분할 brief (사용자 명시 결정 영역) |
| (H) | 본 brief 보류 → 다른 backlog 우선 진입 | Backlog 中 사용자 명시 결정 영역 진입 |
| (I) | 본 brief 폐기 → 별도 접근 | 별도 brief 또는 별도 합의 영역 |
| (J) | 본 brief 작성 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

### 9.1 권고 시작 명령 (사용자 권한 영역)

- **(A) 권고**: "옵션 (A) 로 진행해주세요. 본 brief 를 그대로 승인하고, Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."
- (B): "옵션 (B) 로 진행해주세요. 본 brief 의 §X 를 다음과 같이 수정해주세요: ..."
- (C): "옵션 (C) 로 진행해주세요. 본 brief 中 §X, §Y 만 채택하고 합의 보고서를 작성해주세요."
- (D): "옵션 (D) 로 진행해주세요. Phase α-2 R-5 `.importlinter` 본문 진입 brief 작성으로 전환합니다."
- (E): "옵션 (E) 로 진행해주세요. Phase α-3 R-7 docker secret block 진입 brief 작성."
- (F): "옵션 (F) 로 진행해주세요. Phase α 4 단계 통합 진입 brief 작성."
- (G): "옵션 (G) 로 진행해주세요. Phase α-1 실 진입 step 분할 brief 작성."
- (H): "옵션 (H) 로 진행해주세요. Backlog #X 진입 brief 작성으로 전환합니다."
- (I): "옵션 (I) 로 진행해주세요. 본 brief 폐기 + 별도 brief 작성."
- (J): "옵션 (J) 로 진행해주세요. 세션 종료."

### 9.2 본 §9 의 *범위 한계*

본 §9 = *결정 옵션 enumeration 한정*. 실 다음 단계 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 10. 본 brief 메타 검증

| 메타 검증 | 본 brief |
|---------|--------|
| 사용자 명시 진입 명령 답습 | ✅ (2/2 — Backlog #6 우선 진입 합의 §6.1 1순위 답습 / Phase α-1 R-4 도구 본문 *진입 가능성 검토*) |
| 사용자 명시 7 금지 답습 | ✅ (7/7 — 실 runtime code 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) |
| Backlog #6 우선 진입 합의 §6.1 1순위 답습 | ✅ (Phase α-1 = R-4 도구 본문 — 진입 가능성 *검토 한정*, 적격성 *해소* 0건) |
| Group α 합의 C-1 ~ C-12 답습 | ✅ (C-1 ~ C-12 답습 — 자동 해소 0건 + 자동 변경 0건) |
| Group α 14 결정 영역 답습 | ✅ (재결정 0건) |
| Layer A / Layer B / §5.5 답습 | ✅ (본문 변경 0건) |
| Layer B 18 Rollback Trigger 답습 | ✅ (발화 0건 — §6 답습) |
| Group α 7 단계 승격 Trigger 답습 | ✅ (발화 0건) |
| 5 영구 핵심 제약 보존 | ✅ (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용 5/5 보존) |
| Provider Liquidity 5-way 100% 보존 | ✅ (R-4 = enforcement layer = catalog / provider 영역과 직교) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #1 / #2 / #3 / #4 / #5 / #7 모두 분리 명시) |
| 풀 3+1 승격 트리거 0/8 발화 | ✅ (§5.2 답습) |
| Phase α-1 진입 적격성 5/5 충족 | ✅ (§5.1 답습 — C-α1-1 ~ C-α1-5) |
| R-4 도구 본문 라인 변경 0건 (현 secret 368 / import 178 / url 283) | ✅ (PoC 답습 변경 0건) |
| 자동 진입 0건 | ✅ (모든 다음 단계 = 사용자 명시 결정 영역) |

---

## 11. 본 brief 요약 (한 단락)

본 brief 는 **Backlog #6 Runtime + CI-hook 우선 진입 합의 (`c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축) 발효 후속**, 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬 진입 적격) 中 **Phase α-1 = R-4 도구 본문 영역 *진입 가능성 검토 한정* 준비안 (DRAFT)** 이다. **사용자 명시 7 금지** (실 runtime code 구현 / CI workflow 변경 / branch protection 변경 / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) 7/7 답습. **R-4 = 3 도구 정의** (`tools/secret_scanner.py` Group D 368줄 답습 / `tools/provider_import_scanner.py` Group A 1차 178줄 답습 / `tools/provider_url_scanner.py` Group A 3차 283줄 답습 — 합산 829줄 PoC 답습 변경 0건) + **3 도구 × Phase α-1 본문 작업 후보 분할 매트릭스** (Stage 1 4 sub-step + Stage 3 T-2 3 sub-step + Stage 3 T-5 4 sub-step = 11 sub-step) + **7 금지 영역 × R-4 분리 매트릭스** (7/7 분리 — 충돌 0) + **Phase α-1 진입 적격성 5 조건 검토** (C-α1-1 7 금지 충돌 0/7 + C-α1-2 PoC 답습 100% 보존 + C-α1-3 의존성 0 병렬 진입 적격 + C-α1-4 Provider Liquidity 5-way 100% 보존 + C-α1-5 5 영구 핵심 제약 5/5 보존 = 5/5 충족) + **8 풀 3+1 승격 트리거 0/8 발화** + **R-4 영역 영향 Rollback Trigger 의존성 답습** (18 trigger 中 R-4 직접 영향 5 + 간접 영향 3 + 영향 0 10 — 발화 0건) + **본 brief 자체 금지 37 + Phase α-1 실 진입 단계 금지 17** + **합의 형태 권고** (Reviewer-only 단축 — 8/8 트리거 0건 발화) 를 정리한다. **본 brief 는 Phase α-1 실 진입을 *시작* 시키지 않으며, R-4 도구 본문 어느 줄도 *변경* 하지 않으며, 7 금지 영역 *해소* / Layer C 발효 / MVP-1 PASS / Operational Readiness PASS / Hermes PMO 격상 / Group α 합의 본문 변경 / 14 결정 영역 *재결정* / Phase α-2 / α-3 / α-4 자동 진입 / 합의 보고서 작성 / 메타 갱신 / commit / push 모두 본 brief 영역 외**. 다음 단계는 사용자 명시 결정 영역 (옵션 A~J, §9 답습).

---

**작성일**: 2026-05-15
**상태**: DRAFT (사용자 명시 승인 *전*)
**다음 단계**: 사용자 명시 결정 영역 (옵션 A~J, §9 답습)
**금지 (사용자 명시 답습 — 본 brief 영역)**:
- ❌ **실 runtime code 구현** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ 실 hook 구현
- ❌ Phase α-2 / α-3 / α-4 자동 진입
- ❌ Phase β / γ 자동 진입
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ R-4 도구 본문 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 어느 줄도 변경
- ❌ R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Group α 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 본문 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 합의 보고서 작성 (본 brief = 준비안 한정)
- ❌ CONTEXT / INDEX / SESSION 메타 갱신
- ❌ git commit / push
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
