# 3+1 합의 보고서 — Phase α-1 ~ α-4 통합 실제 구현 계획 brief (Reviewer-only 단축 합의)

> **본 문서는 `docs/phase0/phase-alpha-integrated-implementation-plan-brief.md` (commit `96891eb`, DRAFT) 의 *Reviewer-only 단축 합의 보고서*. 본 문서 = 합의 보고서 권위 — APPROVE AS BRIEF (Reviewer-only 단축).**
>
> **합의 단위**: Phase α-1 ~ α-4 통합 실제 구현 *계획 brief 본문 채택* — 단계 분할 정리 권위 권고 한정.
>
> **본 합의 = Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않으며, 합산 2785줄 본문 어느 줄도 *변경* 하지 않으며, Layer C 재발효 / Layer D 재선언 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / 합산 176 합의 조건 어느 것도 *변경* 하지 않는다.**

---

**합의 시작일**: 2026-05-16
**합의 형태**: Reviewer-only 단축 합의 (옵션 (A) 답습 — 사용자 명시 결정)
**합의 단위**: Phase α-1 ~ α-4 통합 실제 구현 계획 brief 본문 채택 (DRAFT → APPROVE AS BRIEF 격상)
**합의 조건**: 25 조건 (C-μ-1 ~ C-μ-25)
**풀 3+1 트리거 발화**: 0/8

---

## 1. 합의 범위 정의

### 1.1 합의 대상

`docs/phase0/phase-alpha-integrated-implementation-plan-brief.md` (commit `96891eb`, 949줄, 11 섹션, DRAFT) — Phase α-1 ~ α-4 통합 실제 구현 *단계 분할 정리 한정* 준비안.

### 1.2 합의 적용 framing

| 영역 | 답습 |
|------|----|
| 합의 시점 | 2026-05-16 (Layer C 발효 `eb01bc4` 후속 + Layer D 재진입 가능성 검토 `951a5b1` 후속) |
| 합의 권위 | Reviewer-only 단축 합의 (옵션 (A) — 사용자 명시 결정 답습) |
| 합의 효력 | brief DRAFT → APPROVE AS BRIEF 격상 — 단계 분할 정리 권위 권고 한정 |
| **합의 *하지 않는* 것** | (i) Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않음 / (ii) 합산 2785줄 본문 어느 줄도 *변경* 하지 않음 / (iii) Layer C 재발효 / Layer D 재선언 0건 / (iv) MVP-1 PASS 재선언 0건 / (v) Operational Readiness PASS (Layer E) 0건 / (vi) Hermes PMO 격상 (Layer F) 0건 / (vii) 합산 176 합의 조건 어느 것도 *변경* 0건 / (viii) §5.5 9 sub-수단 본문 채택 변경 0건 / (ix) branch protection / dev 환경 강제 / `pre-commit install` 의무화 진입 0건 |

### 1.3 사용자 명시 5 금지 영역 답습 매트릭스

| # | 금지 영역 | 본 합의 위반 |
|---|---------|----------|
| 1 | 실제 파일 수정 | ❌ 0건 (합산 2785줄 답습 보존) |
| 2 | CI workflow 변경 | ❌ 0건 (3 MVP-1 + 8 PoC workflow 답습 보존) |
| 3 | runtime code 변경 | ❌ 0건 (`src/` 본문 변경 0건 + facade.py 41줄 placeholder 답습 보존) |
| 4 | Operational Readiness PASS (Layer E) 선언 | ❌ 0건 |
| 5 | Hermes PMO 격상 (Layer F) | ❌ 0건 |

**합산**: **5/5 위반 0건 — 영구 답습 보존** ✅

---

## 2. Phase α-1 ~ α-4 통합 실제 구현 계획의 범위 답습

### 2.1 Phase α 4 단계 영역 합산 정의 (brief §2 답습)

| Phase | 영역 | artifact 수 | line count | 답습 출처 | sub-수단 (§5.5) |
|-------|----|----------|---------|---------|--------------|
| **α-1 (R-4)** | 3 도구 본문 | 3 file | **829** | Group D PoC + Group A 1차 + Group A 3차 | S-1 (`secret_scanner.py` 368) + T-2 (`provider_import_scanner.py` 178) + T-5 (`provider_url_scanner.py` 283) |
| **α-2 (R-5)** | `.importlinter` 본문 | 1 file | **35** | Group A 2차 합의 + C-9 RA-9 사전 검증 PASS | T-2 import-linter (T-6 = T-2 + T-5 병행 中 transitive 측면) |
| **α-3 (R-7)** | docker secret block | 9 file | **328** | GP-3 Stage 2 합의 + ADR-008 §2.6.2 R2-1 | ST-3 (Hermes upstream 변경 0건 보존) |
| **α-4 (R-1)** | CI workflow 통합 | 7 file | **1593** | Stage 4 합의 + Layer B §5.5.1 | PC-3 + AR-1 (양 GP 공유) |
| **합산** | **4 영역** | **20 file** | **2785** | — | **5 sub-수단** (S-1 + T-2 + T-5 + ST-3 + PC-3 + AR-1) |

### 2.2 §5.5 9 sub-수단 中 본 합의 영역 매트릭스

| 영역 | sub-수단 | 본 합의 매트릭스 |
|------|--------|------------|
| **본 합의 영역 *내*** (6 sub-수단) | S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1 | Phase α-1 ~ α-4 본문 영역 |
| **본 합의 영역 *외*** (3 sub-수단) | PC-4 + AR-2 + AR-3 | Backlog #1 + #2 + #3 + Group α T3 sub 분리 |

---

## 3. R-4 / R-5 / R-7 / R-1 의존성 정리 답습 (brief §2.2 답습)

### 3.1 의존성 토폴로지

```
┌─────────────────────────────────────────────────────────────┐
│ 1순위 병렬 그룹                                                 │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ Phase α-1    │  │ Phase α-2    │  │ Phase α-3    │      │
│  │ R-4 도구 본문  │  │ R-5 importlin│  │ R-7 docker   │      │
│  │ (829줄)       │  │ (35줄)        │  │ secret (328) │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼ (prerequisite actual run PASS 의무)
┌─────────────────────────────────────────────────────────────┐
│ 2순위 의존 그룹                                                 │
├─────────────────────────────────────────────────────────────┤
│         ┌─────────────────────────────┐                     │
│         │ Phase α-4                   │                     │
│         │ R-1 CI workflow 통합 (1593줄)│                     │
│         │ Stage 4 (PC-3 + AR-1)       │                     │
│         └─────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 의존성 매트릭스 (논리적, brief §2.2 답습)

| 의존 방향 | 답습 |
|---------|----|
| Phase α-1 ↔ α-2 | **부분 의존** (T-6 T-2 + T-5 병행 — T-2 import-linter = transitive, T-5 AST = runtime / 모델명 / URL — 책무 분리 답습) |
| Phase α-1 ↔ α-3 | **독립** (Stage 1 + Stage 3 = 양 GP 독립) |
| Phase α-2 ↔ α-3 | **독립** (`.importlinter` ↔ docker secret block 직교) |
| Phase α-4 ↔ α-1 + α-2 + α-3 | **선행 의존** (Stage 4 = Stage 1 + Stage 3 actual run PASS 선행 evidence 의무 답습) |
| Phase α-4 → Layer C | **이미 발효 完** (`eb01bc4` 2026-05-16) |
| 양 GP 의존성 | GP-3 = S-1 + ST-3 + PC-3 + AR-1 / GP-5 = T-2 + T-5 + T-6 + PC-3 + AR-1 — **PC-3 + AR-1 양 GP 공유** |

---

## 4. 1순위 병렬 = α-1 + α-2 + α-3 (brief §3 + §5.2 답습)

### 4.1 1순위 병렬 그룹 합의 권위 권고

| Phase | sub-step 합산 | 답습 합의 | 합의 조건 |
|-------|------------|---------|---------|
| α-1 | 11 sub-step (Stage 1 4 + Stage 3 T-2 3 + Stage 3 T-5 4) | `1b3090b` APPROVE AS BRIEF | C-β-1 ~ C-β-15 (15 조건) |
| α-2 | 6 항목 (root + include + 4 forbidden + facade allow + 각주 1 + docstring) | `6a79247` APPROVE AS BRIEF | C-γ-1 ~ C-γ-26 (26 조건) |
| α-3 | 4 sub-step (2.1 + 2.2 + 2.3 + 2.4) | `3f6306d` APPROVE AS BRIEF | C-δ-1 ~ C-δ-28 (28 조건) |
| **합산** | **21 sub-step / 항목** | **3 합의 (Reviewer-only 단축)** | **69 조건 답습** |

### 4.2 1순위 병렬 진입 적격성

| 조건 | 답습 |
|------|----|
| 양 GP 독립성 | ✅ (S-1 + ST-3 = GP-3 / T-2 + T-5 = GP-5 — 독립) |
| actual run PASS 답습 | ✅ (4/4 PASS — `25728590939` + `25728590916` + `25728590977` + `25731846625`) |
| evidence 적격성 | ✅ (Layer C 발효 시점 양 GP × 5 조건 = 10/10 PASS) |
| 의존성 충돌 | ✅ **0건** |

---

## 5. 2순위 의존 = α-4 (brief §3 + §5.2 답습)

### 5.1 2순위 의존 그룹 합의 권위 권고

| Phase | sub-step 합산 | 답습 합의 | 합의 조건 |
|-------|------------|---------|---------|
| α-4 | 4 sub-step (4.1 PC-3 CI step 통합 + 4.2 AR-1 fail-closed 통합 + 4.3 PC-4 [분리] + 4.4 AR-2 [분리]) | `e59a565` APPROVE AS BRIEF | C-ε-1 ~ C-ε-29 (29 조건) |

### 5.2 2순위 의존성 의무

| 영역 | 답습 |
|------|----|
| Phase α-1 / α-2 / α-3 actual run PASS 선행 evidence | ✅ **답습 完** (4/4 PASS) |
| Stage 4 합의 발효 시점 의무 | ✅ **100% 答** |
| α-4 sub-step 4.1 + 4.2 본 합의 영역 | ✅ 적격 |
| α-4 sub-step 4.3 + 4.4 (PC-4 + AR-2) | ⚠️ **본 합의 영역 외 분리 명시** (Backlog #1 + #2 + #3 분리) |

---

## 6. 5/5 적격성 조건 충족 (brief §5.1 답습)

### 6.1 통합 실제 구현 진입 적격성 5 조건 검토 매트릭스

| 조건 # | 조건 | 검토 결과 | 판정 |
|------|------|----------|----|
| **C-π-1** | 사용자 명시 5 금지 영역 충돌 0 | 4 Phase = 코드 / config / workflow / docker secret 영역 — 금지 #4 (Layer E) / #5 (Layer F) 직교 (충돌 0) + 금지 #1 ~ #3 = *실 진입* 시점 적용, 본 합의 = *단계 분할 정리 한정* (충돌 0) | ✅ **0/5 충돌** |
| **C-π-2** | Layer C 발효 (`eb01bc4`) evidence 답습 100% 보존 | 양 GP × 5 조건 10/10 PASS + 9/9 evidence 재생성 0건 + 4/4 prerequisite actual run 재실행 0건 + 8/8 evidence file line count 정확 일치 | ✅ **답습 100% 보존** |
| **C-π-3** | Layer D 권위 (`210c98f` + 후속 18) 답습 100% 보존 | Layer D 본문 변경 0건 + C-1 ~ C-8 satisfaction 자동 변경 0건 + MVP-1 PASS 재선언 0건 | ✅ **답습 100% 보존** |
| **C-π-4** | Provider Liquidity 5-way 100% 보존 | 4 Phase = enforcement / config / docker secret / workflow 영역 — catalog / provider 영역과 직교 + Tier-1 답습 한정 + 5-vendor 차단 패턴 답습 변경 0건 | ✅ **5/5 100% 보존** |
| **C-π-5** | 5 영구 핵심 제약 보존 | Hermes ≠ root of trust 보존 + 단일 source-of-truth 보존 + 수단/목적 분리 보존 + T1/T2/T3 분리 보존 + SPOF 의도적 수용 보존 | ✅ **5/5 보존** |

**합산 판정**: **C-π-1 ~ C-π-5 5/5 충족** ✅

---

## 7. 8/8 풀 3+1 트리거 0건 발화 (brief §5.3 답습)

### 7.1 8 풀 3+1 승격 트리거 검토 매트릭스

| # | 트리거 | 발화 |
|---|----|----|
| 1 | Group α 합의 C-1 ~ C-12 어느 것의 *재결정* 권고 | ❌ 0건 |
| 2 | 사용자 명시 5 금지 영역 中 1+ 의 *해소* 권고 | ❌ 0건 |
| 3 | Layer B §5.5 9 sub-수단 *재결정* 권고 | ❌ 0건 |
| 4 | Provider Liquidity 5-way 약화 가능성 포함 | ❌ 0건 |
| 5 | 5 영구 핵심 제약 中 1+ 의 약화 포함 | ❌ 0건 |
| 6 | T3 영역 진입 권고 | ❌ 0건 |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 의 충족 발생 | ❌ 0건 |
| 8 | Layer C / Layer D 재발효 / 재선언 / 재진입 권고 | ❌ 0건 |

**합산**: **8/8 트리거 0건 발화 — Reviewer-only 단축 합의 적격 확정** ✅

---

## 8. 사용자 명시 5 금지 영역 영구 답습

### 8.1 금지 #1 — 실제 파일 수정 (아직 하지 않음)

| 영역 | 본 합의 변경 |
|------|----------|
| R-4 = 829줄 (`secret_scanner.py` 368 + `provider_import_scanner.py` 178 + `provider_url_scanner.py` 283) | **0건** |
| R-5 = 35줄 (`/.importlinter`) | **0건** |
| R-7 = 328줄 (`docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/`) | **0건** |
| R-1 = 1593줄 (3 MVP-1 workflow + `tools/mvp1_pc3_ar1_integration_check.py` + `tests/fixtures/mvp1_pc3_ar1_integration/`) | **0건** |
| **합산 2785줄** | **0건 영구 답습** ✅ |

### 8.2 금지 #2 — CI workflow 변경 (아직 하지 않음)

| workflow | 본 합의 변경 |
|---------|----------|
| 3 MVP-1 workflow (`secret-hygiene-egress-redaction.yml` + `provider-adapter-enforcement.yml` + `provider-url-scanner.yml`) | **0건** |
| 8 G2/G3/G4 PoC workflow (`boundary-guard.yml` / `evidence-pass-gate.yml` / `g4-hash-chain.yml` / `history-anchor-verifier.yml` / `memory-skill-migration-feasibility.yml` / `r2-canary.yml` / `rewrite-defense.yml` / `schema-validation.yml`) | **0건** |
| **합산 11 workflow** | **0건 영구 답습** ✅ |

### 8.3 금지 #3 — runtime code 변경 (아직 하지 않음)

| 영역 | 본 합의 변경 |
|------|----------|
| `src/` 본문 | **0건** |
| `src/adapters/llm/facade.py` 41줄 placeholder | **0건 (답습 보존)** |

### 8.4 금지 #4 — Operational Readiness PASS (Layer E) 없음

| 영역 | 본 합의 |
|------|------|
| Layer E 선언 | ❌ 0건 (MVP-6 영역 분리 영구 답습) |
| MVP-6 진입 (commit signing / Vault HSM / hosting provider alternative) | ❌ 0건 |

### 8.5 금지 #5 — Hermes PMO 격상 (Layer F) 없음

| 영역 | 본 합의 |
|------|------|
| Layer F (Hermes PMO 격상) | ❌ 0건 (ADR-008 부록 C 12 조건 영역 분리) |
| Hermes ≠ root of trust 보존 | ✅ 영구 보존 |

### 8.6 추가 분리 영역 (사용자 명시 5 금지 *외* — 본 합의 영역 외 분리 명시)

| 영역 | 분리 답습 |
|------|--------|
| branch protection 변경 (AR-2) | ❌ 0건 (Backlog #3 T3 영역) |
| dev 환경 강제 (`tools/doctor.py`) | ❌ 0건 (Backlog #2) |
| `pre-commit install` 의무화 | ❌ 0건 (Backlog #1 + #2) |
| `.pre-commit-config.yaml` 본문 작성 | ❌ 0건 |
| `.git/hooks/pre-commit` 본문 작성 | ❌ 0건 |
| AR-3 자동 revert bot | ❌ 0건 (Backlog #3) |
| ST-1 / ST-2 / ST-4 / ST-5 진입 | ❌ 0건 (Backlog #1 + #7 + MVP-2) |
| S-2 gitleaks 진입 | ❌ 0건 (Backlog #1) |
| R-4.1 Tier-1 / URL Tier-1 / Model Tier-1 catalog 변경 | ❌ 0건 (Backlog #3) |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ 0건 |
| Hermes upstream Dockerfile 변경 | ❌ 0건 (ADR-008 §2.6.2 R2-1 영구 답습) |
| Production `docker-compose.yml` 변경 | ❌ 0건 |
| 실 secret material commit | ❌ 0건 (F-금지 #1 영구 답습) |
| GitHub Actions secrets 사용 도입 | ❌ 0건 (F-금지 #1 영구 답습) |
| `pull_request_target` workflow 도입 | ❌ 0건 |
| commit signing 도입 | ❌ 0건 (MVP-6) |
| Stage 5 (G3-7 4 항목) 자동 진입 | ❌ 0건 |
| event enum 정식 등록 | ❌ 0건 (Backlog #5) |
| `src/adapters/llm/facade.py` real 본문 작성 | ❌ 0건 (Backlog #4) |
| Group I (Hermes-originated commit auto-reject) | ❌ 0건 (Group α C-2) |
| token rotation 정책 결정 | ❌ 0건 (Group α C-3) |
| GitHub plan / ruleset 가용성 확인 | ❌ 0건 (Group α C-4) |
| Layer 2 runtime block (G5-5) 진입 | ❌ 0건 (MVP-3/4) |
| 의미적 lock-in 검사 진입 | ❌ 0건 (MVP-3) |

**합산**: **24 추가 분리 영역 위반 0건 영구 답습** ✅

---

## 9. 25 합의 조건 (C-μ-1 ~ C-μ-25)

본 합의 발효 시 영구 보존 합의 조건 — 자동 변경 0건:

| # | 조건 | 영역 |
|---|------|------|
| **C-μ-1** | brief `phase-alpha-integrated-implementation-plan-brief.md` (commit `96891eb`, 949줄, 11 섹션) 본문 채택 — APPROVE AS BRIEF (단계 분할 정리 권위 권고 한정) | 합의 단위 |
| **C-μ-2** | 합의 형태 = Reviewer-only 단축 합의 (옵션 (A) — 사용자 명시 결정 답습) | 합의 형태 |
| **C-μ-3** | 합의 *하지 않는* 것 = Phase α-1 / α-2 / α-3 / α-4 어느 것도 실 진입 시키지 않음 + 합산 2785줄 본문 어느 줄도 변경하지 않음 + Layer C 재발효 / Layer D 재선언 0건 + MVP-1 PASS 재선언 0건 + Operational Readiness PASS 0건 + Hermes PMO 격상 0건 | 권위 한계 |
| **C-μ-4** | 4 영역 본문 합산 매트릭스 답습 — R-4 829 + R-5 35 + R-7 328 + R-1 1593 = 2785줄 답습 보존 | brief §2.1 답습 |
| **C-μ-5** | 6 sub-수단 (S-1 + T-2 + T-2 import-linter + T-5 + ST-3 + PC-3 + AR-1) 본 합의 영역 + 3 sub-수단 (PC-4 + AR-2 + AR-3) 본 합의 영역 외 분리 매트릭스 답습 | brief §2.3 답습 |
| **C-μ-6** | 의존성 토폴로지 = 1순위 병렬 (α-1 + α-2 + α-3) + 2순위 의존 (α-4 = Stage 4 prerequisite PASS 의무) | brief §2.2 답습 |
| **C-μ-7** | Phase α-1 11 sub-step + Phase α-2 6 항목 + Phase α-3 4 sub-step + Phase α-4 4 sub-step 단계 분할 답습 (단, 4.3 PC-4 + 4.4 AR-2 = 본 합의 영역 외 분리 명시) | brief §3.1 ~ §3.4 답습 |
| **C-μ-8** | 통합 cycle 옵션 (i) 1순위 병렬 — 2순위 의존 / (ii) 단일 cycle / (iii) 4 cycle 분리 — 모두 *권고 한정* 사용자 명시 결정 영역 | brief §3.5 답습 |
| **C-μ-9** | actual run 답습 매트릭스 4/4 PASS — `25728590939` + `25728590916` + `25728590977` + `25731846625` 답습 한정 (재실행 0건) | brief §3.6 답습 |
| **C-μ-10** | 통합 진입 적격성 5/5 충족 — C-π-1 5 금지 충돌 0/5 + C-π-2 Layer C evidence 답습 100% + C-π-3 Layer D 권위 답습 100% + C-π-4 Provider Liquidity 5-way 100% + C-π-5 5 영구 핵심 제약 5/5 | brief §5.1 답습 |
| **C-μ-11** | 의존성 의무 검토 통과 — 4 prerequisite actual run PASS 답습 100% 答 (Stage 4 합의 답습) | brief §5.2 답습 |
| **C-μ-12** | 8/8 풀 3+1 승격 트리거 0건 발화 — Reviewer-only 단축 합의 적격 확정 | brief §5.3 답습 |
| **C-μ-13** | Rollback Trigger 의존성 답습 (18+5 trigger 中 4 Phase 직접 영향 10 + 간접 영향 3 + 영향 0 7 + TR-1~TR-5 5) — 발화 0건 | brief §6 답습 |
| **C-μ-14** | threshold *고정* 0건 — FP / FN / latency / CI runtime / image layer leak count / restart recovery rate / PR check pass rate / fail-closed rate 모두 *후보 한정* 유지 | brief §6.4 답습 |
| **C-μ-15** | 사용자 명시 5 금지 5/5 위반 0건 영구 답습 — 실제 파일 수정 0건 + CI workflow 변경 0건 + runtime code 변경 0건 + Operational Readiness PASS 0건 + Hermes PMO 격상 0건 | brief §4 답습 |
| **C-μ-16** | 추가 24 분리 영역 위반 0건 영구 답습 — branch protection / dev 환경 강제 / `pre-commit install` 의무화 / PC-4 / AR-2 / AR-3 / ST-1/2/4/5 / S-2 / Tier-2/3 / commit signing / `pull_request_target` / Stage 5 / event enum / facade / Group I / token rotation / GitHub plan / Layer 2 runtime / 의미적 lock-in 모두 분리 | brief §4.6 + §7.2 답습 |
| **C-μ-17** | 합산 176 합의 조건 자동 변경 0건 — Group α 12 + Backlog #6 11 + Phase α-1 15 + Phase α-2 26 + Phase α-3 28 + Phase α-4 29 + Layer C 30 + Layer D 25 + 본 합의 25 = **합산 201 조건** 영구 답습 | 본 합의 답습 |
| **C-μ-18** | Layer A / Layer B / Layer C / Layer D / Group α 합의 / Backlog #6 우선 진입 합의 / Phase α-1~α-4 합의 / Stage 2 합의 / Stage 4 합의 / Group A 1차/2차/3차 합의 / Group D 합의 본문 어느 줄도 변경 0건 | 본 합의 답습 |
| **C-μ-19** | §5.5 9 sub-수단 본문 채택 (`55c5b4b`) 변경 0건 + Group α 14 결정 영역 재결정 0건 | 본 합의 답습 |
| **C-μ-20** | 5 영구 핵심 제약 5/5 보존 — Hermes ≠ root of trust + 단일 source-of-truth + 수단/목적 분리 + T1/T2/T3 분리 + SPOF 의도적 수용 | 본 합의 답습 |
| **C-μ-21** | Provider Liquidity 5-way 100% 보존 — 4 Phase = enforcement / config / docker secret / workflow = catalog / provider 영역과 직교 | 본 합의 답습 |
| **C-μ-22** | F-금지 #1 (GitHub Actions secrets 사용 도입) 영구 답습 0건 | 본 합의 답습 |
| **C-μ-23** | 본 합의 발효 후 자동 진입 0건 — Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않음 + Phase β / γ 자동 진입 0건 + 실 cycle 옵션 / 실 합의 형태 / 실 step 분할 = 사용자 명시 결정 영역 | 본 합의 답습 |
| **C-μ-24** | 본 합의 발효 후 외부 LLM 자동 호출 0건 + 실 API key / provider SDK / 외부 API 호출 0건 + 인간 리뷰 의무 자동 발화 0건 (Group α 합의 C-11 답습 — 응답 = 입력 한정 영구) | 본 합의 답습 |
| **C-μ-25** | 본 합의 발효 후 다음 단계 = 사용자 명시 결정 영역 (옵션 A~N, brief §9 답습) — 자동 진입 0건 | 본 합의 답습 |

---

## 10. 합의 종합 판정

### 10.1 판정

# 🎯 **APPROVE AS BRIEF — Phase α-1 ~ α-4 통합 실제 구현 계획 brief (Reviewer-only 단축 합의)**

| 영역 | 판정 |
|------|----|
| brief 본문 채택 | ✅ **APPROVE AS BRIEF (DRAFT → APPROVE AS BRIEF 격상)** |
| 합의 형태 | Reviewer-only 단축 합의 (옵션 (A) 답습) |
| 합의 조건 | 25 조건 (C-μ-1 ~ C-μ-25) |
| 풀 3+1 트리거 발화 | 0/8 |
| 사용자 명시 5 금지 위반 | 0/5 |
| 추가 분리 영역 위반 | 0/24 |
| 합산 합의 조건 답습 | 201 조건 + ADR-011 §2.1 모법 변경 0건 |

### 10.2 권위 한계 영구 답습

| 영역 | 답습 |
|------|----|
| 본 합의 **하는** 것 | brief DRAFT → APPROVE AS BRIEF 격상 (단계 분할 정리 권위 권고 한정) |
| 본 합의 **하지 않는** 것 | (i) Phase α-1 / α-2 / α-3 / α-4 어느 것도 *실 진입* 시키지 않음 / (ii) 합산 2785줄 어느 줄도 변경 0건 / (iii) Layer C 재발효 / Layer D 재선언 0건 / (iv) MVP-1 PASS 재선언 0건 / (v) Operational Readiness PASS 0건 / (vi) Hermes PMO 격상 0건 / (vii) 합산 201 합의 조건 변경 0건 / (viii) §5.5 9 sub-수단 변경 0건 / (ix) branch protection / dev 환경 강제 / `pre-commit install` 의무화 진입 0건 / (x) 실 cycle 옵션 / 실 합의 형태 / 실 step 분할 결정 0건 |

### 10.3 발효 시점

**2026-05-16** — 본 합의 보고서 commit 시점.

### 10.4 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

brief §9 답습 — 옵션 (A) ~ (N) 사용자 명시 결정 영역:

1. Phase α-1 + α-2 + α-3 1순위 병렬 구현 진입 brief 작성
2. Phase α-1 단독 구현 진입 brief
3. Phase α-2 단독 구현 진입 brief
4. Phase α-3 단독 구현 진입 brief
5. Phase α-4 진입 조건 점검 brief
6. cycle 옵션 (ii) 단일 cycle 통합 실 진입 brief
7. cycle 옵션 (iii) 4 cycle 분리 진입 brief
8. 다른 Backlog 진입 (C-5b ST-1 / C-5c PC-4 T3 / C-6 잔여 sub-수단 / C-7 T3 / C-8 facade / Group I / token rotation / GitHub plan 등)
9. 세션 종료

**금지 사항 영구 답습**:
- ❌ 실제 파일 수정 금지
- ❌ CI workflow 변경 금지
- ❌ runtime code 변경 금지
- ❌ Operational Readiness PASS 선언 금지
- ❌ Hermes PMO 격상 금지
- ❌ branch protection 변경 금지
- ❌ dev 환경 강제 금지
- ❌ `pre-commit install` 의무화 금지
- ❌ Phase α 실제 구현 자동 진입 금지

---

## 11. 합의 메타 정보

| 메타 | 값 |
|------|----|
| 합의 보고서 파일 | `docs/review/3plus1-consensus-2026-05-16-phase-alpha-integrated-implementation-plan.md` |
| 합의 대상 brief | `docs/phase0/phase-alpha-integrated-implementation-plan-brief.md` (commit `96891eb`, 949줄, 11 섹션) |
| 합의 발효일 | 2026-05-16 |
| 합의 형태 | Reviewer-only 단축 합의 (옵션 (A)) |
| 합의 단위 | brief 본문 채택 — 단계 분할 정리 권위 권고 한정 |
| 합의 조건 | 25 조건 (C-μ-1 ~ C-μ-25) |
| 풀 3+1 트리거 발화 | 0/8 |
| Phase 영역 합산 | 4 Phase × 20 artifact × 2785줄 본문 답습 |
| 6-Layer 분리 매트릭스 | Layer A ✅ + Layer B ✅ + Layer C ✅ (`eb01bc4`) + Layer D ✅ (`210c98f` + 후속 18) + Phase α-1~α-4 ✅ APPROVE AS BRIEF + **본 합의 = 통합 실제 구현 *계획* APPROVE AS BRIEF** + Layer E ⏳ + Layer F ⏳ |
| 합산 합의 조건 (영구 답습) | 201 조건 + ADR-011 §2.1 모법 |
| 자동 진입 0건 | 모든 다음 단계 = 사용자 명시 결정 영역 |

---

**합의 종료일**: 2026-05-16
**판정**: 🎯 **APPROVE AS BRIEF — Reviewer-only 단축 합의** (옵션 (A) 답습)
**다음 단계**: 사용자 명시 결정 영역 (자동 진입 0건)
