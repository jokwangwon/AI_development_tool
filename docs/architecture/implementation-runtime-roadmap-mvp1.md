# Implementation/Runtime PASS Roadmap — MVP-1 Deepening (GP-3 + GP-5)

> **본 문서는 `implementation-runtime-roadmap.md` (17 항목 *전체* 우선순위 매트릭스, 2026-05-09 후속 15) 의 *MVP-1 영역 deepening* 이다.**
>
> *MVP-1 = G2 GP-3 (Credential / Secret Hygiene) + GP-5 (Provider Adapter Enforcement) 실 구현* 으로 이미 합의됨 (`docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` §C-7 / 외부 LLM 응답 `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md` line 242).
>
> 본 문서 = MVP-1 진입 *직전* 의사결정을 위한 사전 정리 한정. **수단 *결정* 은 별도 합의 영역, 본 문서는 *수단 후보 비교 + threshold 후보 + 합의 형태 권고* 까지만**.

**작성일**: 2026-05-12
**상태**: DRAFT — Reviewer-only 단축 합의 진행 예정 (`docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` 후속 작성)
**상위 권위**: ADR-011 §2.1 (a)~(e), ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending), 외부 LLM GPT-5.5 Thinking 응답 §6 (3-layer PASS 분리)
**근거 합의**:
- `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` §C-7 (MVP-0 ~ MVP-6 단계화 권고 등록)
- `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md` §6 권장 MVP 단계 (line 237-262) + §7 PASS 의미 분리 (line 264-276)
- `docs/architecture/implementation-runtime-roadmap.md` §2 (G2 5 항목 매트릭스) + §5 (종합 우선순위 매트릭스) — Order 1 = GP-5, Order 4 = GP-3
- `docs/architecture/governance-preconditions.md` §5 (GP-3) + §7 (GP-5) Entry/Exit 기준
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) 5조건 패턴

---

## 0. 본 문서 범위

### 0.1 본 문서가 *하는* 것

1. MVP-1 정의의 **단일 source-of-truth** 통합 (외부 LLM line 242 + C-7 line 378 + 본 문서 §1)
2. 3-layer PASS 분리 (Design Gate / Implementation Evidence / Operational Readiness) **재명시 + MVP-1 위치 매핑**
3. GP-3 / GP-5 PoC 완료 상태 → MVP-1 진입 *gap 분석* (어떤 항목이 PoC 영역에 머물러 있고, MVP-1 으로 격상되려면 무엇이 추가되어야 하는지)
4. 각 GP 별 **수단 후보 비교** (gitleaks / detect-secrets / trufflehog / custom + 본 PoC scanner 확장 / depcruise / import-linter (PoC 채택) / grimp / ruff custom rule / custom AST scanner 확장) — 채택 결정 X, 후보 비교 + 권고 한정
5. 각 GP 별 **측정 metric 후보 + threshold 후보** — 합의 영역 정량 결정 입력
6. 각 GP 별 **Rollback Trigger + Evidence Required + 의존성 + 합의 형태 권고**
7. MVP-1 → MVP-2 진입 조건 *권고 수준* (Implementation Evidence PASS 의 정의)

### 0.2 본 문서가 *하지 않는* 것 (사용자 명시 답습 — 2026-05-12 진입 명령)

- ❌ 실제 runtime code 구현 (gitleaks/detect-secrets pre-commit hook 본문 / `src/adapters/llm/facade.py` 본문 / inotify sidecar / chmod 600 entrypoint script 등)
- ❌ CI/hook 구현 (`.github/workflows/secret-scan.yml` 신설 / `.pre-commit-config.yaml` 신설 / GitHub branch protection rule 변경 / depcruise/`.dependency-cruiser.cjs` 신설)
- ❌ Hermes PMO 격상 선언
- ❌ Operational Readiness PASS 선언
- ❌ Implementation/Runtime PASS 자동 선언 (각 항목 PASS = 별도 합의 + PoC evidence + 사용자 명시 결정)
- ❌ G2 / G3 / G4 Implementation PASS 일괄 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 수단 *결정* (gitleaks 채택 / detect-secrets 채택 / depcruise vs import-linter 최종 결정 등 — 모두 별도 합의 영역)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (R-4.1 Tier-1 42 catalog 답습 한정)
- ❌ threshold *고정* (FN rate 목표 1% 라거나 FP rate 목표 0.5% 등 정량 *결정* — 본 문서는 *후보* 까지만)
- ❌ MVP-2 ~ MVP-6 본문 deepening (별도 합의 영역, 본 문서는 MVP-1 → MVP-2 *진입 조건 권고* 까지만)
- ❌ 17 항목 우선순위 자동 *재고정* (`implementation-runtime-roadmap.md` §5.1 권고 답습 — 사용자 명시 결정 영역 유지)

### 0.3 본 문서의 권위 한계

본 문서는 **DRAFT — 권고 한정**. Reviewer-only 단축 합의 후 사용자 명시 결정으로 *권고 권위* 발행. 본 문서의 어떤 §도 그 자체로:

- (i) GP-3 / GP-5 의 수단을 *결정* 하지 않으며,
- (ii) MVP-1 의 PASS 를 *선언* 하지 않으며,
- (iii) `implementation-runtime-roadmap.md` 의 17 항목 우선순위를 *변경* 하지 않으며,
- (iv) 신규 ADR / 신규 P / 신규 GP 를 *발행* 하지 않으며,
- (v) Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS 를 *발생시키지 않는다*.

본 문서가 발생시키는 *유일한* 효과는 **MVP-1 진입 직전 의사결정 입력 정비 — 수단 후보 비교 + threshold 후보 + Rollback Trigger + Evidence + 합의 형태 권고**. 모든 *결정* 은 *별도 합의*.

---

## 1. MVP-1 정의 (기존 합의 답습)

### 1.1 MVP-1 = GP-3 + GP-5 — 합의 권위 cross-reference

| 출처 | 정의 |
|------|------|
| `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md` line 242 | "MVP-1 \| G1b, GP-2 redaction, GP-3 secret scan, GP-5 provider facade" |
| `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` §C-7 line 378 | "MVP-1 \| G2 GP-3 + GP-5 (gitleaks + detect-secrets + depcruise/import-linter 실 구현) \| Implementation 1차 합의" |
| 본 문서 §1.1 (통합) | **MVP-1 = G2 GP-3 (Credential / Secret Hygiene) + GP-5 (Provider Adapter Enforcement) 실 구현 + R-7 SOP / G1b 회귀 유지** |

**MVP-1 본질** (3 합의 출처 통합):
- (i) **GP-3 + GP-5** 두 GP 의 *Implementation Evidence PASS* 를 1차로 확보
- (ii) **G1b** (R-7 redaction SOP) 회귀 유지 (이미 PASS 상태, MVP-1 *기준선*)
- (iii) **GP-2 redaction** (외부 LLM 답습) = MVP-1 vs MVP-2 사이의 *경계* — 본 문서는 GP-2 = MVP-2 로 분리 답습 (C-7 line 379 답습 — "MVP-2 \| G2 GP-2 + G4 §4.4 Layer 4")
  - 두 출처 간 미세 충돌: 외부 LLM line 242 = GP-2 포함 / C-7 line 378 = GP-3 + GP-5 한정. 본 문서는 **C-7 답습** (GP-2 = MVP-2 로 분리), 사유 §1.3 답습.

### 1.2 3-layer PASS 분리 (외부 LLM 답습 §7.1)

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 1: Design/Governance Gate PASS                          │
│  → 문서 정의 + 권위 위계 + GP/Skill/Schema *설계* 승인         │
│  → 4 게이트 모두 = ✅ 2026-05-07 + 2026-05-09 후속 (Bundled)    │
│  → 본 문서 = 본 PASS 답습 한정 (변경 0건)                       │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2: Implementation Evidence PASS  ← MVP-1 = 본 layer 1차  │
│  → 각 GP 별 실 구현 + PoC evidence + 자동 회귀 + 합의 APPROVE  │
│  → MVP-1 = GP-3 + GP-5 의 본 PASS 진입                          │
│  → MVP-2 ~ MVP-5 = GP-2 / GP-4 / GP-6 / G3 / G4 의 본 PASS 단계 │
├─────────────────────────────────────────────────────────────────┤
│  Layer 3: Operational Readiness PASS                           │
│  → 4 게이트 모두 Implementation Evidence PASS + 외부 LLM 1+    │
│  → 인간 전문 리뷰 + 사용자 명시 + Multi-host external service  │
│  → 본 문서 범위 외 (MVP-6 = PMO 격상 검토, 별도 합의)          │
└─────────────────────────────────────────────────────────────────┘
```

**본 문서 = Layer 2 (Implementation Evidence PASS) 의 *MVP-1 단계* deepening 한정.** Layer 3 (Operational Readiness PASS) / Hermes PMO 격상 / 4 게이트 일괄 PASS = 본 문서 범위 외.

### 1.3 GP-2 = MVP-1 vs MVP-2 분리 사유 (C-7 답습)

본 문서는 GP-2 (Egress Redaction) 를 **MVP-2** 로 분리. 사유:

1. **R-4 / R-4.1 답습 책임 분담** — GP-2 의 송신 redaction = R-4.1 Tier-1 42 catalog 의 *런타임 적용* 영역. 본 PoC (Group D) 는 *형식적 검출 layer 한정* (D-2 = redacted output 잔존 검증). 실 송신 redaction = Hermes upstream 영역 (Group D PoC §1.2 #6 답습) + P1 facade RedactionFilter 본문 (Group D PoC §1.2 마지막 항목 답습).
2. **MVP-1 부담 경감** — GP-3 + GP-5 만으로도 의사결정 부담 충분. GP-2 추가 시 4 영역 동시 진입 (GP-3 source + GP-3 storage + GP-5 + GP-2) — 1인 개발자 환경에서 운영 부담 ↑.
3. **외부 LLM line 242 vs C-7 line 378 충돌 해소 = C-7 답습** — 본 문서 §1.1 답습. 단, GP-2 는 **MVP-2** 의 Implementation Evidence PASS 영역 *우선순위 1* (C-7 line 379 답습) — 본 분리는 *시점* 분리이지 *영구 제외* 아님.

---

## 2. MVP-1 Entry / Exit 기준

### 2.1 MVP-1 Entry 기준

본 문서의 MVP-1 진입은 다음 5 조건이 모두 충족되어야 적격:

| # | 조건 | 현 상태 (2026-05-12) | 검증 |
|---|------|---------------------|------|
| 1 | Layer 1 (Design/Governance Gate) PASS 발효 | ✅ G2/G3/G4 = PASS Bundled (2026-05-09) | `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` |
| 2 | GP-3 PoC 완료 (형식적 검출 layer 시제) | ✅ Group D 통합 PoC PASS 6/6 (2026-05-10) | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` |
| 3 | GP-5 PoC 완료 (Layer 1a/1b/1c 시제) | ✅ Group A 1차/2차/3차 PASS (2026-05-09 ~ 2026-05-10) | `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` + `g2-gp5-poc2-import-linter-implementation.md` + `g2-gp5-poc3-url-endpoint-model-name-scanner.md` |
| 4 | R-4.1 Tier-1 42 catalog 등록 PASS | ✅ R-4.1 PoC PASS (2026-05-07) | `docs/phase0/r4-1-trigger-extension-evidence.md` |
| 5 | 본 문서 (MVP-1 roadmap) Reviewer-only 단축 합의 APPROVE | ⏳ 본 문서 작성 후 후속 합의 | `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` (작성 예정) |

**현 시점 충족 = 4/5** (#5 만 본 문서 후속 작성 후 발효).

### 2.2 MVP-1 Exit 기준 (= Implementation Evidence PASS 진입 조건)

MVP-1 exit = GP-3 + GP-5 두 GP 의 **Implementation Evidence PASS** 발효. 본 문서 범위에서는 *진입 조건 권고* 한정 (실 PASS 발효 = 별도 합의 영역).

각 GP 별 Implementation Evidence PASS 진입 5 조건 = ADR-011 §2.1 (a)~(e) 답습 (§5 답습):

| # | 조건 | GP-3 | GP-5 |
|---|------|------|------|
| (a) | 동등 이상의 보안 결과 | gitleaks/detect-secrets/custom scanner 결과 R-4.1 Tier-1 42 catalog 답습 동등 이상 | depcruise/import-linter 결과 §9.3 답습 동등 이상 |
| (b) | 격리 환경 PoC 실증 | docker secret + chmod 600 + inotify (저장) PoC + gitleaks PR auto-reject (코드) PoC | depcruise/import-linter PR auto-reject + facade single entry point PoC |
| (c) | ADR / SDD 권위 명시 | ADR-008 §A.2 R1-2 + ADR-010 + R-4 + 본 §3 | ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + 본 §4 |
| (d) | 자동 회귀 검증 경로 확보 | `.github/workflows/secret-scan.yml` (또는 R-6 통합) + nightly | `.github/workflows/provider-adapter-enforcement.yml` 기존 + depcruise/import-linter step 추가 + 매 PR + nightly |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 (수단 결정 시 풀 3+1 권고 — §3.6 답습) | 단축 또는 풀 3+1 (T-1 vs T-2 vs T-9 결정 시 풀 3+1 권고 — §4.6 답습) |

**MVP-1 exit = (GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정**. 어느 한쪽이라도 미충족 시 MVP-1 부분 PASS 처리 (Implementation Evidence PASS *부분 발효* — 별도 합의 영역).

---

## 3. GP-3 — Credential / Secret Hygiene MVP-1 Deepening

### 3.1 PoC 완료 상태 + MVP-1 진입 gap 분석

#### 3.1.1 PoC 완료 영역 (2026-05-10 Group D)

| 영역 | PoC 상태 | 산출물 |
|------|---------|--------|
| code-side secret 검출 (D-1, source scan) | ✅ PASS 6/6 | `tools/secret_scanner.py --mode scan-source` (R-4.1 Tier-1 45 patterns 직접 답습) |
| redacted output 잔존 secret 검증 (D-2) | ✅ PASS 6/6 (partial leak 검출 + base64 evasion known limitation) | `tools/secret_scanner.py --mode scan-log` |
| Custom scanner 단독 채택 (4 옵션 中 A) | ✅ Group D §2.1 답습 | gitleaks/detect-secrets 도입 0건 |
| CI workflow 형식적 검증 layer | ✅ `secret-hygiene-egress-redaction.yml` 12 step | actual run `25623028888` |

#### 3.1.2 MVP-1 진입 gap (PoC → Implementation Evidence PASS 사이의 *추가* 작업)

| Gap # | PoC 영역 | MVP-1 추가 작업 | 책무 분리 (분리 영역 명시) |
|-------|---------|---------------|------------------------|
| G3-1 | 저장 경로 (P3) — Hermes 컨테이너 chmod 600 / entrypoint stat / inotify | **MVP-1 진입 의사결정 영역** — Hermes upstream 변경 가능성 vs sidecar 패턴 vs Vault HSM (ADR-010) 직접 통합 中 어느 수단? | Group D PoC §1.2 #6 답습 — Hermes upstream 영역 → MVP-1 에서는 *수단 후보 비교* + *분리 책무 결정* 한정 |
| G3-2 | 코드 본문 (P4) — gitleaks/detect-secrets pre-commit hook | **MVP-1 진입 의사결정 영역** — gitleaks vs detect-secrets vs trufflehog vs Group D custom scanner 확장 中 어느 수단? Tier-2/3 catalog 자동 확장 위험 회피 vs 외부 검증 도구 채택 trade-off | Group D PoC §2.1 답습 — 4 옵션 비교, 본 문서 §3.2 추가 확장 |
| G3-3 | PR auto-reject (CI step) | **MVP-1 진입 의사결정 영역** — `.github/workflows/secret-scan.yml` 신설 vs `.pre-commit-config.yaml` 신설 vs Group D 기존 workflow 확장 中 어느 통합 형태? | Group D PoC §1.2 #7 + #8 답습 |
| G3-4 | base64 / URL-encoded / 압축 evasion | **MVP-1 → MVP-2/3 영역** — Hermes upstream R2-6 또는 P1 facade RedactionFilter 영역 (Group D PoC §8 #1 답습) | 본 문서 범위 외 (분리 영역 명시) |
| G3-5 | log file canary inject + grep nightly | **MVP-1 → MVP-2 영역** — R-6 workflow 확장 영역, R-7 SOP §5 ROLLBACK trigger R5 답습 (Group D PoC §8 #5 답습) | 본 문서 범위 외 (분리 영역 명시) |
| G3-6 | Tier-2 / Tier-3 catalog 확장 (Slack / GCP / Azure 등) | **MVP-1 → 별도 합의 영역** — gitleaks/detect-secrets 도입 시점 결정 + 풀 3+1 합의 + 외부 LLM 1+ (Group D PoC §8 #7 답습) | 본 문서 범위 외 (분리 영역 명시) |
| **G3-7** | **CI secret 관리 (GitHub Actions secret boundary)** | **MVP-1 진입 의사결정 영역 — 6 검토 항목 분리** — (i) GitHub Actions secrets 사용 0건 검증 (F-금지 grep step 답습) + (ii) `secrets.*` 참조 감지 (workflow grep step 또는 S-1 확장) + (iv) fork PR secret 접근 차단 default 정책 보존 + (v) workflow `permissions: contents: read` 명시 강제 (R-6 답습) + (vi) `event: ci_secret_access_attempted` 신규 enum 후보 (ADR-012 §2.2 답습) = **MVP-1 영역 4 항목** / (iii) CI 로그 secret 노출 방지 (전체 책무) = **MVP-2 (GP-2 송신 redaction 영역)** + GitHub Actions log mask 부분 활용은 MVP-1 적격 / `pull_request_target` workflow 도입 = **별도 합의 영역** (secret 접근 활성화 trigger = T2/T3) | `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` §2 (Observation O-1 흡수, GP-3 진입 합의 Condition C-1) — Group D PoC + ADR-012 §2.2 + R-6 `r2-canary.yml` 답습 |

**MVP-1 deepening 핵심 = G3-1 + G3-2 + G3-3 + G3-7 의 *수단 후보 비교 + threshold 후보 + 합의 형태 권고*** (G3-4/5/6 = MVP-2 이후 또는 별도 합의 영역).

### 3.2 수단 후보 비교 — 코드 본문 secret 검출 (G3-2)

#### 3.2.1 5 수단 후보 매트릭스

| # | 수단 | 패턴 catalog | Tier-2/3 자동 확장 위험 | FP 위험 | FN 위험 | 도입 비용 | Python 호환 | baseline file silenceability | 본 PoC 호환성 |
|---|------|------------|-----------------------|--------|--------|----------|------------|---------------------------|--------------|
| **S-1** | **Group D custom scanner 확장** (R-4.1 Tier-1 42 catalog 직접 답습) | 45 patterns (Prefix 36 + regex 7 + alternation 2) | **0** (Tier-1 답습 한정 — 사용자 명시 답습) | 中 (Group D §8 #10 fixture 확장 후보 18종 답습 가능) | 中 (base64 evasion 미커버 — known limitation) | 低 (PoC 직접 재사용) | ✅ stdlib 단독 | ❌ (silenceable 0 — fail-closed) | ✅ Group D 직접 답습 |
| **S-2** | **gitleaks** | gitleaks default ruleset (~150 patterns) + custom rule | **HIGH** (default ruleset 에 Tier-2/3 패턴 — Slack token / GCP service account 자동 포함, Group D §2.1 (B) 답습) | 高 (default ruleset 광범위) | 低 (광범위 catalog) | 低-中 (binary or GitHub Action) | ✅ language-agnostic | ⚠️ `.gitleaksignore` 가능 | 부분 (Group D scanner 와 결과 형식 다름) |
| **S-3** | **detect-secrets** | plugin-based (~20+ plugins, 활성화 선택) | **MEDIUM** (plugin 자동 활성화 시 Tier-2/3 확장 위험, Group D §2.1 (C) 답습) | 中 (plugin 별 차이) | 中 (plugin 미활성화 시 누락) | 低 (`pip install detect-secrets`) | ✅ Python | ⚠️ baseline file `silenceable` (Group D §2.1 (C) 답습 — false negative 위험 명시) | 부분 |
| **S-4** | **trufflehog** | OSS/SaaS catalog + entropy-based | **HIGH** (catalog 광범위 + entropy 기반 → Tier-2/3 자동 확장 + entropy heuristic FP) | 高 (entropy 기반) | 低 (광범위) | 中 (binary + 운영 학습 비용) | ✅ language-agnostic | ⚠️ allowlist 가능 | 부분 |
| **S-5** | **gitleaks + detect-secrets 병행** | S-2 + S-3 합산 | **HIGH** (도구 2개 = scope 2 배 확장, Group D §2.1 (D) 답습 — 사용자 명시 풀 3+1 trigger #4 발화 위험) | 高 | 低 | 中-高 | ✅ | ⚠️ 양쪽 silenceable | ❌ (Group D 사용자 명시 회피) |

#### 3.2.2 권고 (수단 *결정* 아님 — 별도 합의 영역)

본 문서 권고:

- **MVP-1 1차 = S-1 단독** (Group D PoC 답습 충실 + Tier-2/3 자동 확장 위험 0 + 외부 의존성 0)
- **MVP-1 1.5차 (보강)** = S-1 + **S-3 detect-secrets 부분 통합** (plugin 명시 활성화 한정 — Tier-1 답습 plugin 만, baseline file 사용 금지)
  - 사유: gitleaks (S-2) 의 default ruleset Tier-2/3 자동 확장 위험 회피 + Python 환경 정합성 우선
  - 단, **plugin 명시 활성화 + baseline file 금지** 의 *2 조건* 강제 시에만 채택 적격 — 두 조건 미충족 시 S-3 미채택
- **MVP-1 미채택** = S-2 (gitleaks) + S-4 (trufflehog) + S-5 (병행)
  - 사유: 모두 Tier-2/3 자동 확장 위험 HIGH + Group D §2.1 답습 위반 + 사용자 명시 풀 3+1 trigger #4 발화 위험

본 권고는 **수단 *결정* 이 아님**. 본 권고를 *실 채택* 하려면 별도 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 후 채택 trigger 가 필요. 본 문서는 *권고 한정*.

### 3.3 수단 후보 비교 — 저장 경로 secret 검출 (G3-1)

#### 3.3.1 5 수단 후보 매트릭스

| # | 수단 | 검증 시점 | Hermes upstream 변경 | sidecar 가능성 | 운영 부담 | 현 ADR 권위 |
|---|------|---------|---------------------|--------------|---------|-----------|
| **ST-1** | **Hermes Dockerfile entrypoint stat 검증** (chmod 600 강제) | 컨테이너 시작 시 | ✅ 필요 (Hermes upstream Dockerfile 수정) | ❌ | 低 | ADR-008 §A.2 R1-2 + GP-3 §5.3 답습 |
| **ST-2** | **inotify sidecar** (mtime/perm 변경 → 컨테이너 정지) | 런타임 지속 | ❌ (sidecar 분리 가능) | ✅ | 中 (sidecar process 운영) | ADR-008 §A.2 R1-2 + GP-3 §5.3 답습 |
| **ST-3** | **docker secret 직접 사용** | 런타임 (file system 통한 노출 회피) | 부분 (docker-compose.yml 갱신) | ❌ | 低 | ADR-008 §2.6.2 R2-1 + GP-3 §5.3 답습 |
| **ST-4** | **Vault HSM 통합** (ADR-010) | 런타임 (외부 HSM) | ❌ (Hermes 가 Vault 클라이언트 호출, Hermes upstream 변경 없음) | 부분 (Vault 자체가 외부 service) | **高** (Vault 인프라 운영 비용) | ADR-010 §2 답습 — Multi-host 환경 권고 |
| **ST-5** | **ST-1 + ST-2 + ST-3 통합** (Defense in depth) | 시작 + 런타임 + file system | ✅ 필요 | ✅ | 中-高 | ADR-008 §A.2 R1-2 + ADR-008 §2.6.2 + GP-3 §5.3 통합 답습 |

#### 3.3.2 권고

본 문서 권고:

- **MVP-1 1차 = ST-3 단독** (docker secret) — Hermes upstream 변경 회피 + 운영 부담 최소 + ADR-008 §2.6.2 답습 충실
- **MVP-1 1.5차 (보강)** = ST-3 + **ST-2 inotify sidecar** (Hermes upstream 변경 회피 유지)
- **MVP-2 이후** = ST-5 (Defense in depth) 단계적 진입
- **Operational Readiness PASS 시점 (Multi-host 전환)** = ST-4 (Vault HSM) 진입 검토 — ADR-010 답습

본 권고는 **수단 *결정* 이 아님**. ST-1 / ST-2 / ST-4 진입 시점 = 별도 합의 (Hermes upstream 변경 = 풀 3+1 합의 trigger / Vault HSM 도입 = ADR-010 §X 진입 합의).

### 3.4 측정 metric 후보 + threshold 후보 (정량 *결정* 아님)

#### 3.4.1 코드 본문 secret 검출 (G3-2) metric / threshold

| Metric | 후보 정의 | threshold 후보 | 본 문서 권고 |
|--------|---------|--------------|-----------|
| **PASS_rate (D-1)** | `pass/` fixture 검사 시 violation 0건 비율 | 100% (현 PoC 답습) | 100% 강제 (변경 0건) |
| **FAIL_detection_rate (D-1)** | `fail/` fixture 검사 시 ≥4 패턴 cover 비율 | ≥4 patterns / 6 fixtures (현 PoC 답습) | ≥4 패턴 cover (현 PoC 답습) |
| **FP_rate** | 정상 코드 (실 src/) 1000 line 당 false positive 건수 | < 0.5건 / 1000 line (권고) | **threshold *결정* 영역 — 별도 합의** (실 src/ 0건 환경 시 측정 불가) |
| **FN_rate** | 의도된 fake canary catalog (R-4.1) 의 미검출 건수 | 0건 / 45 patterns (R-4.1 답습 강제) | 0건 / 45 patterns 강제 (현 PoC 답습) |
| **scan_latency** | scanner 실행 시간 (1000 file 입력) | < 5초 (PoC + CI 답습) | **threshold *결정* 영역 — 별도 합의** (현 PoC actual run 6초 답습 — 12 step 합산) |
| **CI_step_PASS_rate** | CI workflow 12 step 中 PASS 비율 | 12/12 (현 PoC 답습) | 12/12 강제 (현 PoC 답습) |

#### 3.4.2 저장 경로 secret 검출 (G3-1) metric / threshold

| Metric | 후보 정의 | threshold 후보 | 본 문서 권고 |
|--------|---------|--------------|-----------|
| **chmod_violation_detection** | chmod 644 등 644+ 권한 시 컨테이너 정지 발생 비율 | 100% (PoC 격리 환경) | 100% 강제 |
| **inotify_event_response_time** | mtime/perm 변경 → 컨테이너 정지까지 latency | < 1초 (권고) | **threshold *결정* 영역 — 별도 합의** |
| **docker_secret_isolation_check** | secret 파일이 image layer 에 포함되지 않음 검증 | 0건 leak (강제) | 0건 강제 |
| **container_restart_recovery** | 컨테이너 정지 후 재시작 시 secret 재주입 정상 | 100% (PoC 격리 환경) | 100% 강제 |

본 §3.4 의 모든 threshold 후보 = *권고 한정*. 정량 *결정* (예: FP_rate < 0.5%) = 별도 합의 영역 (실 src/ 도입 후 측정 baseline 확보 후 결정).

### 3.5 Rollback Trigger (GP-3 MVP-1 한정)

`implementation-runtime-roadmap.md` §6.2 R-1 ~ R-9 中 GP-3 관련 trigger 답습 + MVP-1 specific trigger 추가:

| Trigger | 발화 조건 | 발화 시 행동 |
|--------|---------|-------------|
| **R-1** (`implementation-runtime-roadmap.md` §6.2) | secret pattern catalog 변경 (Tier-1 42 catalog 답습) — Tier-2/Tier-3 확장 trigger | catalog 변경 = 풀 3+1 합의 + 외부 LLM 1+ |
| **R-MVP1-G3-1** | gitleaks/detect-secrets/trufflehog 도입 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 후 채택 trigger (Group D PoC §10 trigger #4 답습) |
| **R-MVP1-G3-2** | base64/URL-encoded/압축 evasion 검출 책무 변경 (Hermes upstream R2-6 영역 → MVP-1 영역으로 흡수 시) | 책무 분리 재합의 (Group D PoC §8 #1 답습) |
| **R-MVP1-G3-3** | 실 secret 처리 정책 변경 (ADR-008 §A.2 / ADR-010 본문 변경) | T3 영역 → 풀 3+1 합의 + 외부 LLM 1+ + 인간 리뷰 + 사용자 명시 |
| **R-MVP1-G3-4** | redaction 정책 완화 (Tier-1 catalog 일부 비활성화 결정) | T3 영역 → 풀 3+1 합의 (Group D PoC §10 trigger #3 답습) |
| **R-MVP1-G3-5** | FP 가 정상 개발 흐름을 과도하게 막음 (실 src/ 도입 후 측정) | threshold 재결정 합의 (단축 합의 적격) |
| **R-MVP1-G3-6** | FN 으로 secret 누출 가능성 잔존 (canary 검증 실패) | 풀 3+1 합의 + 결함 수정 후 재검증 (Group D PoC §10 trigger #6 답습) |
| **R-MVP1-G3-7** | Hermes upstream Dockerfile 변경 결정 (ST-1 / ST-5 진입 시) | 풀 3+1 합의 + Hermes upstream PR 검토 |
| **R-MVP1-G3-8** | Vault HSM 도입 결정 (ST-4 진입 시) | ADR-010 §X 진입 합의 + Multi-host 인프라 검토 |

### 3.6 Evidence Required + 의존성 + 합의 형태 권고

#### 3.6.1 Evidence Required (5 형식 — `implementation-runtime-roadmap.md` §6.3 답습)

| Evidence | 형식 (GP-3 MVP-1) |
|----------|------------------|
| Markdown report | `docs/phase0/g2-gp3-mvp1-evidence.md` (PoC evidence + MVP-1 추가 evidence 통합) |
| JSONL ledger entry | `docs/evidence/ledger.jsonl` (`event: gate_pass` 또는 `event: secret_scan_layer1_implementation` — ADR-012 §2.2 답습) |
| Docker isolation log | (저장) chmod 644 / mtime 변경 시뮬레이션 + 컨테이너 정지 evidence + (코드) gitleaks/detect-secrets PR auto-reject 시뮬레이션 evidence |
| GitHub Actions run | secret-scan.yml (또는 R-6 통합) actual run id + 12+ step PASS |
| 합의 보고서 | `docs/review/3plus1-consensus-<date>-mvp1-gp3-implementation.md` |

#### 3.6.2 의존성

| 의존 | 영역 | 상태 |
|------|------|------|
| R-4.1 Tier-1 42 catalog 답습 | Group D PoC + R-4.1 PoC 답습 | ✅ |
| Group D PoC `tools/secret_scanner.py` 직접 재사용 | Group D PoC 산출물 | ✅ |
| `implementation-runtime-roadmap.md` Order 4 (GP-3) 권고 답습 | 본 roadmap 답습 | ✅ |
| GP-5 MVP-1 진입 (Order 1, 그룹 A 완료 후 그룹 D) | 본 문서 §4 + roadmap 답습 | ⏳ 본 문서 동시 진입 |
| ADR-010 (Vault HSM) | ADR-010 본문 답습 (ST-4 진입 시점에만) | ⏳ MVP-2 이후 또는 Operational Readiness 영역 |
| ADR-008 §A.2 R1-2 cross-reference 갱신 | ADR-008 본문 답습 (cross-reference 한정) | ⏳ MVP-1 PASS 후 별도 commit (본 문서 범위 외) |

#### 3.6.3 합의 형태 권고

| 합의 영역 | 합의 형태 | 사유 |
|---------|---------|------|
| 본 문서 (GP-3 MVP-1 roadmap deepening) 자체 | **Reviewer-only 단축 합의** | `implementation-runtime-roadmap.md` (DRAFT 단축 합의 영역) + 17 항목 우선순위 답습 + 새 권위 결정 0건 |
| MVP-1 진입 결정 (S-1 단독 채택) | **Reviewer-only 단축 합의** + PoC evidence | Group D PoC §2.1 답습 + Tier-2/3 자동 확장 0건 |
| MVP-1 1.5차 (S-3 detect-secrets 부분 통합) | **풀 3+1 합의 + 외부 LLM 1+** | Tier-2/3 catalog 확장 영역 + 사용자 명시 풀 3+1 trigger #4 발화 (Group D §2.1 (D) 답습) |
| ST-1 / ST-2 / ST-5 진입 (Hermes upstream 변경) | **풀 3+1 합의 + Hermes upstream PR 검토** | Hermes upstream 영역 진입 = 책무 경계 변경 |
| ST-4 (Vault HSM) 진입 | **ADR-010 §X 진입 합의 + 외부 LLM 1+** | T3 영역 + Multi-host 인프라 |
| Implementation Evidence PASS 발효 (GP-3 한정) | **별도 합의 + 사용자 명시 결정** + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | 본 문서 §2.2 답습 |

---

## 4. GP-5 — Provider Adapter Enforcement MVP-1 Deepening

### 4.1 PoC 완료 상태 + MVP-1 진입 gap 분석

#### 4.1.1 PoC 완료 영역 (2026-05-09 ~ 2026-05-10 Group A 1차/2차/3차)

| 영역 | PoC 상태 | 산출물 |
|------|---------|--------|
| Layer 1a — 정적 import (AST 5 패턴) | ✅ Group A 1차 PASS | `tools/provider_import_scanner.py` (AST 5 패턴) |
| Layer 1b — Transitive import (정적 그래프) | ✅ Group A 2차 PASS (T-2 import-linter 채택) | `.importlinter` + `requirements-dev.txt` + `src/` placeholder |
| Layer 1c — URL endpoint + model name 직접 사용 | ✅ Group A 3차 PASS | `tools/provider_url_scanner.py` (URL Tier-1 catalog 10 + Model Tier-1 catalog 19) |
| 책무 분담 매트릭스 (1차 vs 2차) | ✅ `g2-gp5-poc2-import-linter-implementation.md` §1 | direct/transitive/dynamic/model-name/URL 분담 명시 |
| CI workflow 통합 | ✅ `.github/workflows/provider-adapter-enforcement.yml` (Group A 1차 + 2차 통합 + 3차 별도 workflow) | actual run `25629390384` (3차) |

#### 4.1.2 MVP-1 진입 gap (PoC → Implementation Evidence PASS 사이의 *추가* 작업)

| Gap # | PoC 영역 | MVP-1 추가 작업 | 책무 분리 |
|-------|---------|---------------|---------|
| G5-1 | Layer 1 형식 차단 (1a/1b/1c) | **MVP-1 진입 의사결정 영역** — depcruise vs import-linter (PoC 채택) vs grimp vs ruff custom rule vs custom AST scanner 확장 中 어느 도구 *통합 운영* 형태? | `g2-gp5-poc2-depcruise-rule-scope.md` §8 + 본 문서 §4.2 추가 확장 |
| G5-2 | pre-commit hook (T-9, 별도 합의) | **MVP-1 진입 의사결정 영역** — pre-commit framework 도입 vs git native pre-commit script vs CI-only enforcement 中 어느 통합 형태? | Group A 2차 PoC §1.2 + 본 문서 §4.3 |
| G5-3 | PR auto-reject GitHub branch protection | **MVP-1 진입 의사결정 영역** — branch protection rule 변경 (T3) vs CI step fail-closed 한정 (T2) 中 어느 layer? | T3 영역 → 풀 3+1 합의 + 사용자 명시 |
| G5-4 | facade single entry point (`src/adapters/llm/facade.py` 본문) | **MVP-1 → 별도 합의 영역** — P1 v2 facade real 본문 = `g2-gp5-poc2-import-linter-implementation.md` §8 TR-1 답습 (재합의 trigger) | 본 문서 범위 외 (P1 v2 영역 분리) |
| G5-5 | runtime egress 차단 (Layer 2, R-2/R-4.1 답습 Docker isolation) | **MVP-1 → MVP-3/4 영역** — `g2-gp5-provider-adapter-enforcement-poc.md` §9 3차 ~ 5차 영역 답습 | 본 문서 범위 외 (Layer 2 분리) |
| G5-6 | 의미적 lock-in (특정 모델 출력 가정) | **MVP-1 → MVP-3 영역** — depcruise/import-linter 영역 외, 라운드트립 검증 (P2-5 답습) 영역 | 본 문서 범위 외 (라운드트립 영역 분리) |
| G5-7 | OAuth 응답 후처리 / 메타 저장 / 파서 차단 (§9.1 #2~#6) | **MVP-1 → MVP-3 영역** — runtime 도입 시 보강 (1차 PoC §9 답습) | 본 문서 범위 외 |

**MVP-1 deepening 핵심 = G5-1 + G5-2 + G5-3 의 *수단 후보 비교 + threshold 후보 + 합의 형태 권고*** (G5-4/5/6/7 = MVP-3 이후 또는 별도 합의 영역).

### 4.2 수단 후보 비교 — Layer 1 정적 차단 도구 (G5-1)

#### 4.2.1 6 수단 후보 매트릭스

| # | 수단 | direct import | transitive import | 동적 import | URL endpoint | model name | Python 호환 | 도입 비용 | 본 PoC 답습 |
|---|------|--------------|------------------|-----------|-----------|----------|----------|---------|-----------|
| **T-1** | **dependency-cruiser** (JS native) | ✅ | ✅ (강점) | ❌ | ❌ | ❌ | ⚠️ 비공식 | **高** (Node 환경 + npm 의존) | §9.3 직접 답습 (`.depcruise.cjs`) |
| **T-2** | **import-linter** (Python native, **Group A 2차 채택**) | ✅ | ✅ (강점) | ❌ | ❌ | ❌ (`google.generativeai` 도구 제약) | ✅ 공식 | 低 (`pip install import-linter`) | Group A 2차 합의 §5.5 답습 |
| **T-3** | **grimp** (import-linter 의 lower-level) | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ 공식 | 低 | `g2-gp5-poc2-depcruise-rule-scope.md` §8 미언급 — 본 문서 신규 후보 |
| **T-4** | **ruff custom rule** (AST plugin) | ✅ | ❌ (ruff = file-level, transitive 미지원) | ✅ | 부분 (custom plugin) | 부분 (custom plugin) | ✅ 공식 | 中 (ruff plugin 작성) | `g2-gp5-poc2-depcruise-rule-scope.md` §8 (T-3) 답습 |
| **T-5** | **Group A 1차 AST scanner 확장** (transitive 의존 분석 추가) | ✅ | 부분 (custom 구현 부담 高) | ✅ | ✅ (Group A 3차 답습) | ✅ (Group A 1차 답습) | ✅ stdlib | 高 (자체 구현 transitive 분석) | Group A 1차/3차 답습 |
| **T-6** | **T-2 + T-5 병행 운영** (Group A 2차 채택 형태) | T-5 ✅ + T-2 ✅ | T-2 ✅ | T-5 ✅ | T-5 ✅ (Group A 3차) | T-5 ✅ | ✅ | 中 (도구 2개 운영) | **현 PoC 채택 답습** (Group A 2차 §5.5 #C-7 답습 — silent fail 위험 명시) |

#### 4.2.2 책무 분담 매트릭스 (Group A 2차 §1 답습 + MVP-1 확장)

| 검증 영역 | T-1 (depcruise) | T-2 (import-linter, **PoC 채택**) | T-3 (grimp) | T-4 (ruff) | T-5 (custom AST) |
|---------|---------------|---------------------------------|------------|----------|----------------|
| Direct import (`openai`/`anthropic`/`litellm`/`ollama`) | ✅ | ✅ | ✅ | ✅ | ✅ |
| Direct (`google.generativeai`) | ✅ | ❌ (각주 1) | ✅ | ✅ | ✅ |
| From-import | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Transitive (A→B→forbidden)** | ✅ | ✅ | ✅ | ❌ | 부분 (custom) |
| 동적 import (`importlib`, `__import__`) | ❌ | ❌ | ❌ | ✅ | ✅ |
| 모델명 분기 (문자열) | ❌ | ❌ | ❌ | 부분 (custom plugin) | ✅ |
| URL/endpoint 하드코딩 | ❌ | ❌ | ❌ | 부분 (custom plugin) | ✅ |
| 의미적 lock-in | ❌ | ❌ | ❌ | ❌ | ❌ (라운드트립 영역) |

#### 4.2.3 권고 (수단 *결정* 아님 — 별도 합의 영역)

본 문서 권고:

- **MVP-1 1차 = T-6 (현 PoC 채택 형태 유지)** = T-2 import-linter (transitive 강점) + T-5 custom AST scanner (1차/3차 — 동적 import + 모델명 + URL)
  - 사유: Group A 2차 합의 답습 + silent fail 위험 명시 (Group A 2차 §6 답습) + 책무 분담 매트릭스 명시
- **MVP-1 미채택**:
  - T-1 (depcruise) — Node 환경 도입 비용 高 + Python repo 정합성 저하
  - T-3 (grimp) 단독 — import-linter 보다 lower-level, 본 PoC 답습 충실성 ↓
  - T-4 (ruff custom rule) 단독 — transitive 미지원, T-2 의 강점 손실
  - T-5 단독 — transitive 분석 자체 구현 부담 高 + import-linter 답습 충실성 ↓

본 권고는 **수단 *결정* 이 아님**. T-6 채택 시점 = Implementation Evidence PASS 합의 영역. T-1 / T-3 / T-4 / T-5 단독 진입 = 풀 3+1 합의 trigger (Group A 2차 §5.4 TR-3 답습).

### 4.3 수단 후보 비교 — pre-commit hook 통합 (G5-2)

#### 4.3.1 4 수단 후보 매트릭스

| # | 수단 | 통합 형태 | 운영 부담 | T2/T3 영역 | 본 PoC 답습 |
|---|------|---------|---------|----------|-----------|
| **PC-1** | **pre-commit framework** (`.pre-commit-config.yaml` + `pre-commit install`) | hook 정의 통일 + dev 환경 자동 설치 | 中 (framework 도입 + dev 환경 강제) | T2 (정책 영역, ADR-011 §2.4 답습) | Group D PoC §1.2 #7 + Group A 2차 §1.2 답습 |
| **PC-2** | **git native pre-commit script** (`.git/hooks/pre-commit`) | shell script + 수동 설치 | 低 (framework 미도입) | T2 | 부분 답습 |
| **PC-3** | **CI-only enforcement** (pre-commit 미도입, PR push 시 CI step 만 차단) | CI step + PR auto-reject | 低 (dev 환경 영향 0) | T2 (CI step) + T3 (branch protection rule 변경 시) | Group A 1차/2차/3차 PoC 답습 |
| **PC-4** | **PC-1 + PC-3 병행** (Defense in depth) | dev 환경 + CI 양쪽 차단 | 中-高 | T2 + T3 | 본 문서 신규 후보 |

#### 4.3.2 권고

본 문서 권고:

- **MVP-1 1차 = PC-3 단독** (CI-only enforcement, 현 PoC 답습) — dev 환경 영향 0 + Group A 1차/2차/3차 PoC 답습 충실
- **MVP-1 1.5차 (보강)** = PC-4 (PC-1 + PC-3 병행) — dev 환경 강제 추가 시 Defense in depth
- **MVP-1 미채택** = PC-2 (git native script) — framework 미도입의 장점은 PC-3 가 더 우월 (CI 통합 + dev 환경 영향 0)

본 권고는 **수단 *결정* 아님**. PC-1 (pre-commit framework) 도입 = T2 정책 영역 (ADR-011 §2.4 답습) → 단축 합의 적격 (사용자 명시 결정).

### 4.4 수단 후보 비교 — PR auto-reject layer (G5-3)

#### 4.4.1 3 수단 후보 매트릭스

| # | 수단 | layer | T2/T3 | 우회 가능성 | 본 PoC 답습 |
|---|------|------|-------|----------|-----------|
| **AR-1** | **CI step fail-closed 한정** (현 PoC 답습) | T2 (CI 수준) | T2 | CI bypass 가능 (T3 영역) | Group A 1차/2차/3차 PoC 답습 |
| **AR-2** | **GitHub branch protection rule** (CODEOWNERS / required check / commit signing) | T3 (repo policy 수준) | T3 | T3 영역 → 사용자 명시 강제 | Group D PoC §1.2 #8 답습 — T3 정책 영역 |
| **AR-3** | **AR-1 + AR-2 통합** (Defense in depth) | T2 + T3 | T3 (포함) | 우회 차단 강화 | 본 문서 신규 후보 |

#### 4.4.2 권고

본 문서 권고:

- **MVP-1 1차 = AR-1 단독** (현 PoC 답습) — CI step fail-closed 한정, T3 영역 진입 회피
- **MVP-1 1.5차 (보강) = AR-3** (AR-1 + AR-2 통합) — T3 영역 진입 + branch protection rule 변경 + 사용자 명시 결정
  - 사유: Hermes-originated commit auto-reject (G3 §2.2 #20 답습) 와 통합 시 AR-2 단계적 진입 권고
- **MVP-1 미채택** = AR-2 단독 — AR-1 보강 없이는 시스템 외부 PR 우회 위험 잔존

본 권고는 **수단 *결정* 아님**. AR-2 진입 = T3 영역 (사용자 명시 강제) → 풀 3+1 합의 + 외부 LLM 1+ 권고.

### 4.5 측정 metric 후보 + threshold 후보 (정량 *결정* 아님)

#### 4.5.1 Layer 1 정적 차단 도구 (G5-1) metric / threshold

| Metric | 후보 정의 | threshold 후보 | 본 문서 권고 |
|--------|---------|--------------|-----------|
| **direct_import_block_rate** | 5 패턴 (direct / from / dynamic / double-underscore / model-name) 검출 비율 | 5/5 (Group A 1차 답습) | 5/5 강제 |
| **transitive_import_block_rate** | A→B→forbidden cascading 검출 비율 | 1/1 (Group A 2차 답습 — `transitive_import.py` fixture) | 1/1 강제 (현 PoC 답습) |
| **url_endpoint_block_rate** | 10 vendor URL Tier-1 catalog 검출 비율 | 4/4 (Group A 3차 PASS, 4 vendor pattern_ids cover) | ≥4 vendor cover (현 PoC 답습) |
| **model_name_block_rate** | 19 모델 Tier-1 catalog 검출 비율 | 11/11 pattern_ids (Group A 3차 답습) | ≥11 pattern_ids (현 PoC 답습) |
| **FP_rate (실 src/)** | 정상 facade 코드 1000 line 당 false positive 건수 | < 0.5건 / 1000 line (권고) | **threshold *결정* 영역 — 별도 합의** (실 src/ 0건 환경 시 측정 불가) |
| **FN_rate** | 의도된 fixture 미검출 건수 | 0건 / 9 fixtures (Group A 3차 답습) | 0건 / 9 fixtures 강제 |
| **scan_latency** | scanner + import-linter 합산 실행 시간 | < 30초 (Group A 2차 actual run 답습) | **threshold *결정* 영역 — 별도 합의** |
| **CI_step_PASS_rate** | CI workflow step PASS 비율 | 12/12 (Group A 1차) + 16/16 (Group A 3차) | 양쪽 100% 강제 |

#### 4.5.2 pre-commit hook (G5-2) metric / threshold

| Metric | 후보 정의 | threshold 후보 | 본 문서 권고 |
|--------|---------|--------------|-----------|
| **commit_block_rate** | 의도된 violation commit 차단 비율 (PC-1/PC-4 채택 시) | 100% (PoC 격리 환경) | 100% 강제 |
| **dev_env_install_rate** | `pre-commit install` 적용된 dev 환경 비율 | ≥90% (권고, dev 환경 측정) | **threshold *결정* 영역 — 별도 합의** (PC-1 채택 시점 결정) |
| **hook_runtime** | pre-commit hook 실행 시간 (commit 1회 당) | < 10초 (권고) | **threshold *결정* 영역 — 별도 합의** |

본 §4.5 의 모든 threshold 후보 = *권고 한정*. 정량 *결정* (예: FP_rate < 0.5%) = 별도 합의 영역.

### 4.6 Rollback Trigger (GP-5 MVP-1 한정)

`implementation-runtime-roadmap.md` §6.2 R-1 ~ R-9 中 GP-5 관련 trigger 답습 + MVP-1 specific trigger 추가:

| Trigger | 발화 조건 | 발화 시 행동 |
|--------|---------|-------------|
| **R-5** (`implementation-runtime-roadmap.md` §6.2) | provider_bindings 위반 PR 검출 — G2 GP-5 답습 | 해당 PR auto-reject + alert |
| **R-9** (G2 GP-5 1차 PoC §6 답습) | provider lock-in 재발 (#1 + #2 + #5 패턴) | scanner 무력화 시 CI fail-closed |
| **R-MVP1-G5-1** | T-1 (depcruise) / T-3 (grimp) / T-4 (ruff) / T-5 단독 진입 결정 | 풀 3+1 합의 + 도구 변경 영향 분석 |
| **R-MVP1-G5-2** | T-2 import-linter `include_external_packages = True` 옵션 동작 불가 판명 | 도구 재선택 (Group A 2차 §8 TR-3 답습 — 현 시점 미발화) |
| **R-MVP1-G5-3** | `src/adapters/llm/facade.py` real 본문 작성 (Group A 2차 §8 TR-1 답습) | T-2 룰 ignore_imports 검증 + LiteLLM 정상 동작 |
| **R-MVP1-G5-4** | `pyproject.toml` 신설 (Group A 2차 §8 TR-2 답습) | dev-dep 도입 영향 분석 (현 시점 `requirements-dev.txt` 만) |
| **R-MVP1-G5-5** | 책무 분담 매트릭스 *임의 흡수* 시도 (Group A 2차 §8 TR-4 답습) | 책무 분리 재합의 |
| **R-MVP1-G5-6** | T-9 (pre-commit hook PC-1) 도입 별도 합의 (Group A 2차 §8 TR-5 답습) | 본 PoC 와의 책무 분리 재합의 |
| **R-MVP1-G5-7** | URL Tier-2 / Tier-3 vendor 추가 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 |
| **R-MVP1-G5-8** | 모델 Tier-2 / Tier-3 vendor 추가 결정 | 풀 3+1 합의 + Tier-2/3 catalog 확장 결정 |
| **R-MVP1-G5-9** | branch protection rule 변경 결정 (AR-2 진입) | T3 영역 + 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| **R-MVP1-G5-10** | LiteLLM license 변경 (R-3 답습) | scanner rule 재검토 + Layer 1 자체 의미 변경 검토 |

### 4.7 Evidence Required + 의존성 + 합의 형태 권고

#### 4.7.1 Evidence Required

| Evidence | 형식 (GP-5 MVP-1) |
|----------|------------------|
| Markdown report | `docs/phase0/g2-gp5-mvp1-evidence.md` (Group A 1차/2차/3차 PoC evidence + MVP-1 추가 evidence 통합) |
| JSONL ledger entry | `docs/evidence/ledger.jsonl` (`event: provider_adapter_enforcement_layer1_static` — `g2-gp5-poc2-import-linter-implementation.md` §4 답습) |
| Docker isolation log | depcruise/import-linter PR auto-reject 시뮬레이션 evidence (격리 환경 0 — scanner stateless · network-free) |
| GitHub Actions run | provider-adapter-enforcement.yml + provider-url-scanner workflow actual run id |
| 합의 보고서 | `docs/review/3plus1-consensus-<date>-mvp1-gp5-implementation.md` |

#### 4.7.2 의존성

| 의존 | 영역 | 상태 |
|------|------|------|
| Group A 1차/2차/3차 PoC 직접 재사용 | Group A PoC 산출물 | ✅ |
| `implementation-runtime-roadmap.md` Order 1 (GP-5) 권고 답습 | 본 roadmap 답습 | ✅ |
| GP-3 MVP-1 (Order 4) 동시 진입 가능 | 본 문서 §3 답습 | ⏳ 본 문서 동시 진입 |
| P1 v2 facade real 본문 (G5-4 분리 영역) | P1 v2 (`llm-providers-design.md`) | ⏳ 별도 합의 영역 (본 문서 범위 외) |
| ADR-008 차단조건 #4 cross-reference 갱신 | ADR-008 본문 답습 (cross-reference 한정) | ⏳ MVP-1 PASS 후 별도 commit (본 문서 범위 외) |
| ADR-009 (자체 Adapter v2.0) cross-reference 갱신 | ADR-009 본문 답습 (cross-reference 한정) | ⏳ MVP-1 PASS 후 별도 commit (본 문서 범위 외) |

#### 4.7.3 합의 형태 권고

| 합의 영역 | 합의 형태 | 사유 |
|---------|---------|------|
| 본 문서 (GP-5 MVP-1 roadmap deepening) 자체 | **Reviewer-only 단축 합의** | `implementation-runtime-roadmap.md` (DRAFT 단축 합의 영역) + 17 항목 우선순위 답습 + 새 권위 결정 0건 |
| MVP-1 진입 결정 (T-6 채택) | **Reviewer-only 단축 합의** + PoC evidence | Group A 1차/2차/3차 PoC 답습 + 책무 분담 매트릭스 답습 |
| MVP-1 1.5차 (PC-1 pre-commit framework 도입) | **단축 합의 + 사용자 명시** | T2 정책 영역 (ADR-011 §2.4 답습) |
| AR-2 / AR-3 진입 (branch protection rule 변경) | **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** | T3 영역 |
| T-1 / T-3 / T-4 / T-5 단독 진입 결정 | **풀 3+1 합의 + 도구 변경 영향 분석** | Group A 2차 §8 TR-3 답습 |
| URL / 모델 Tier-2 / Tier-3 vendor 추가 결정 | **풀 3+1 합의 + Tier-2/3 catalog 확장 결정** | R-MVP1-G5-7 / R-MVP1-G5-8 답습 |
| Implementation Evidence PASS 발효 (GP-5 한정) | **별도 합의 + 사용자 명시 결정** + ADR-011 §2.1 (a)~(e) 5/5 충족 evidence | 본 문서 §2.2 답습 |

---

## 5. MVP-1 통합 PASS 기준 (GP-3 + GP-5)

### 5.1 ADR-011 §2.1 (a)~(e) 5조건 답습 (양 GP 공통)

| # | 조건 | GP-3 충족 방식 | GP-5 충족 방식 |
|---|------|--------------|--------------|
| (a) | 동등 이상의 보안 결과 | R-4.1 Tier-1 42 catalog 답습 + 도구 결과 동등 이상 | §9.3 답습 + 도구 결과 동등 이상 |
| (b) | 격리 환경 PoC 실증 | docker secret + chmod 644 시뮬레이션 + PR auto-reject 시뮬레이션 | depcruise/import-linter PR auto-reject + facade 단일 진입 |
| (c) | ADR / SDD 권위 명시 | ADR-008 §A.2 + ADR-010 + R-4 + GP-3 §5 + 본 §3 | ADR-008 차단조건 #4 + ADR-009 C-N §5 + P1 v2 + GP-5 §7 + 본 §4 |
| (d) | 자동 회귀 검증 경로 확보 | secret-scan.yml (또는 R-6 통합) + nightly | provider-adapter-enforcement.yml + provider-url-scanner + 매 PR + nightly |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 (수단 결정 시 풀 3+1 권고) | 단축 또는 풀 3+1 (T-1 vs T-2 vs T-9 결정 시 풀 3+1) |

**MVP-1 PASS = (GP-3 5/5 + GP-5 5/5) 두 GP 모두 충족 + 사용자 명시 결정 + Implementation Evidence PASS 발효 합의**.

### 5.2 통합 Evidence Ledger entry 형식 (ADR-012 §2.2 답습)

| event enum (MVP-1 신규 후보) | trigger | T1/T2/T3 |
|----------------------------|---------|---------|
| `secret_scan_layer1_implementation` | GP-3 코드 본문 secret 검출 (G3-2) | T2 (CI step) |
| `secret_storage_isolation_implementation` | GP-3 저장 경로 (G3-1) | T2 (Hermes upstream sidecar) |
| `provider_adapter_enforcement_layer1_static` | GP-5 Layer 1a/1b/1c 통합 | T2 (CI step) |
| `mvp1_gate_pass` | MVP-1 = GP-3 + GP-5 양쪽 PASS | T3 (사용자 명시 + ADR-011 §2.1 5/5 evidence) |

본 4 enum 후보는 **본 문서 권고 한정** — `event` enum 정식 등록 = ADR-012 §2.2 답습 + G4 §10.2 schema 진화 정책 (추가 필드 MINOR 호환 영역) 답습 별도 합의. **본 4 enum 외 §5.4 통합 위험 매트릭스 IR-1 / IR-2 / IR-3 의 3 enum 후보** (`provider_key_adapter_bypass_risk_detected` / `direct_sdk_with_secret_leakage_detected` / `secret_handling_environment_mismatch_detected`) **추가 = 합산 7 enum 후보** (정식 등록 = 동일 별도 합의 영역).

### 5.3 통합 Rollback Trigger 매트릭스

| Trigger | GP-3 | GP-5 | 발화 시 행동 |
|--------|------|------|-------------|
| Tier-1 catalog 변경 (R-1) | ✅ | (R-MVP1-G5-7 / G5-8) | 풀 3+1 합의 + 외부 LLM 1+ |
| 도구 변경 (gitleaks 도입 / depcruise 도입) | (R-MVP1-G3-1) | (R-MVP1-G5-1) | 풀 3+1 합의 + 도구 변경 영향 분석 |
| Hermes upstream 변경 (G3-7) / facade real 본문 (G5-3) | ✅ | ✅ | 풀 3+1 합의 + Hermes/P1 v2 영역 진입 |
| T3 영역 (정책 변경 / branch protection) | ✅ | ✅ | 풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시 |
| FP/FN 측정 결과 threshold 미달 | ✅ | ✅ | threshold 재결정 합의 (단축 합의 적격) |

### 5.4 GP-3 + GP-5 Integrated Risk Matrix (Observation O-2 흡수 — Condition C-4)

본 §5.4 = **GP-3 + GP-5 양 GP 진입 합의 (`6dc5bdc` + `6808d17`) 후속, MVP-1 roadmap 단축 합의 (`95be2e5`) Observation O-2 흡수 영역**. 사용자 명시 진입 명령 답습 (2026-05-12 여섯 번째 명령 — "MVP-1 roadmap §5.4 통합 위험 sub-section 신설"). GP-3 / GP-5 각각은 진입 적격성 발효 완료, 둘이 *함께 적용될 때* 발생하는 결합 위험 3 영역을 본 §5.4 에 명시.

#### 5.4.0 통합 위험 매트릭스 표 (사용자 명시 형식 답습)

| ID | Integrated Risk | GP-3 Side | GP-5 Side | MVP-1 Handling | Deferred Handling | Evidence Enum |
|----|----------------|-----------|-----------|----------------|------------------|---------------|
| IR-1 | Provider key adapter bypass | Provider key exists (S-1 detect) | P1 facade bypass (T-6 detect direct/transitive/dynamic) | Detect combined signal in CI report | Runtime enforcement (G5-5 Layer 2 영역, MVP-3/4) | `provider_key_adapter_bypass_risk_detected` |
| IR-2 | Direct SDK + secret leakage | Secret scanner hit (S-1 D-1 mode) | Direct SDK import hit (T-2 / T-5 cover) | Combined fail in report (same file/module) | Runtime block (G5-5 Layer 2) + 자동 alert | `direct_sdk_with_secret_leakage_detected` |
| IR-3 | Local/CI/Docker mismatch | Secret source differs (.env / `secrets.*` / docker secret) | Enforcement differs (local CI miss / Docker SDK 부재) | CI-only baseline + evidence 기록 | Operational parity check (Operational Readiness PASS 영역) | `secret_handling_environment_mismatch_detected` |

#### 5.4.1 IR-1 — Provider key 가 adapter 를 우회하는 경로

**위험**:

Provider API key 가 존재하면 개발자/에이전트가 P1 facade 를 우회하여 직접 provider SDK 를 사용할 수 있음.

**예시**:

```
OPENAI_API_KEY 존재
→ openai SDK 직접 import
→ P1 facade 우회
→ GP-5 위반 + GP-3 secret 노출 위험 결합
```

**대응** (MVP-1 영역):

- GP-3 secret scanner (S-1) 에서 provider key 존재 여부 감지 — 본 PoC fixture 답습 (Group D fake canary 의무, 실 secret 0건)
- GP-5 T-6 (T-2 + T-5 병행) 에서 direct provider SDK import 감지 — Group A 1차/2차/3차 PoC 답습
- 둘이 *동시 발생* 시 combined-risk event 로 분류 — CI report 통합 (별도 보고서 또는 단일 step 에서 cross-reference)
- Evidence enum 후보 = `provider_key_adapter_bypass_risk_detected` (T2 + T3 영역 — combined 분류 시 사용자 명시 결정 영역)

**deferred 영역** (MVP-3/4):

- Runtime enforcement (G5-5 Layer 2 영역) — `g2-gp5-provider-adapter-enforcement-poc.md` §9 Layer 2 답습
- Provider key 자동 revoke (T3 영역, 별도 합의)

#### 5.4.2 IR-2 — Direct SDK import + secret leakage 결합 위험

**위험**:

direct SDK import 자체는 provider lock-in 위험 (GP-5),
secret leakage 자체는 credential hygiene 위험 (GP-3),
둘이 *결합* 되면 provider-specific secret 사용 경로가 직접 코드에 고정됨 — 단일 위험보다 *높은 심각도*.

**대응** (MVP-1 영역):

- direct SDK import 감지 결과 (T-6 출력) 와 secret scanner 결과 (S-1 출력) 를 *같은 report* 에서 교차 확인 — CI 통합 step (`combined_check.py` 또는 별도 grep step)
- 같은 *파일* 또는 같은 *module boundary* 에서 둘 다 발견되면 GP-3/GP-5 *combined fail* 로 기록 — 별도 보고서 분류
- GP-3 단독 또는 GP-5 단독보다 *높은 심각도* 로 분류 — Evidence ledger 우선순위 ↑
- Evidence enum 후보 = `direct_sdk_with_secret_leakage_detected` (T2 + T3 영역)

**deferred 영역** (MVP-3/4):

- Runtime block (G5-5 Layer 2) + 자동 alert
- Combined fail 시 자동 PR auto-reject (T3 영역, AR-2 + AR-3 답습)

#### 5.4.3 IR-3 — Local / CI / Docker secret handling 불일치

**위험**:

local 에서는 `.env` 를 사용하고,
CI 에서는 GitHub Actions secret (`secrets.*`) 을 사용하고,
Docker 에서는 docker secret 을 사용하는 식으로 환경별 secret handling 이 달라지면,
GP-3 검증과 GP-5 adapter enforcement 가 서로 다른 결과를 낼 수 있음.

**예시**:

```
local: .env 에 provider key 존재
CI: secrets.* 미사용 (G3-7 (i) 답습)
Docker: docker secret 사용 (ST-3 답습)
→ 한 환경에서는 direct SDK import 가 실패하지만 다른 환경에서는 성공
→ enforcement 결과 불일치
```

**대응** (MVP-1 영역):

- local / CI / Docker 각각의 secret source boundary 를 명시 — 본 §5.4 표 + Group D §1.2 #6 (Hermes upstream 분리) + ST-3 (docker secret) + G3-7 (CI secret) 답습
- MVP-1 에서는 최소한 **CI-only enforcement 기준을 우선** (PC-3 + AR-1 답습)
- 환경별 차이는 evidence 에 기록 — `event: secret_handling_environment_mismatch_detected` 신규 enum 후보 + secret source boundary 명시 (local / CI / Docker 별 enforcement 결과)
- Evidence enum 후보 = `secret_handling_environment_mismatch_detected` (T2 + T3 영역)

**deferred 영역** (Operational Readiness 단계):

- Multi-environment parity 검증으로 승격 — local/CI/Docker 모두 동일 enforcement 결과 보장
- Vault HSM (ST-4, ADR-010 답습) 통합 시 단일 secret source 로 수렴

#### 5.4.4 본 §5.4 의 *범위 한계*

본 §5.4 = **사양 한정** (mvp1.md §5 통합 PASS 기준 内부 sub-section). 본 §5.4 는:

- **하지 *않는* 것**:
  - 실 combined check 도구 구현 (예: `tools/combined_check.py` 본문 작성) 0건 — MVP-1 진입 합의 시점 별도 작업 영역
  - Evidence enum 정식 등록 (3 신규 enum 모두 *후보 한정* — ADR-012 §2.2 + G4 §10.2 별도 합의)
  - Runtime enforcement 자동 구현 (G5-5 Layer 2 영역, MVP-3/4 분리)
  - Operational parity 자동 강제 (Operational Readiness PASS 영역, MVP-6 분리)
  - Provider key 자동 revoke (T3 영역, 별도 합의)
  - Combined fail 시 자동 PR auto-reject (T3 영역, AR-2 + AR-3 별도 합의)

- **하는 것**:
  - 통합 위험 3 영역 (IR-1 / IR-2 / IR-3) *영역 분리* + *MVP-1 vs deferred handling* 명시
  - 3 evidence enum 후보 권위 권고
  - GP-3 / GP-5 양 GP 진입 합의 후속 *통합 책무* 명시
  - 후속 작업 (MVP-1 진입 합의 / Operational Readiness 단계 / G5-5 Layer 2 / Vault HSM) 분리 영역 명시

### 5.5 9 sub-수단 본문 채택 매트릭스 (Layer B `f40423f` 발효 결과 행사 — Backlog #6 Implementation Entry 합의 §1 답습)

본 §은 Backlog #6 Layer B Implementation Entry 합의 (`docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md`, commit `f40423f` push 완료, APPROVE 발효) 의 *결과 행사* — **9 sub-수단 *권고 → 본문 채택* 격상 *문서상 확정* 한정**.

#### 5.5.0 본문 채택 의미 명시 (사용자 명시 강조 답습)

```
본문 채택 = MVP-1 implementation entry 에서 사용할 수단을 *문서상 확정*
본문 채택 ≠ runtime code 구현
본문 채택 ≠ CI workflow 구현
본문 채택 ≠ hook 구현
본문 채택 ≠ Implementation Evidence PASS
```

본 §5.5 *발효 후*에도 다음은 **별도 사용자 명시 결정 의무 영역**:
- runtime code / CI workflow / hook 실 구현 (사용자 명시 결정 후 별도 commit 진입)
- Layer C (Implementation Evidence PASS) 진입 (별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)

#### 5.5.1 GP-3 본문 채택 4 sub-수단 매트릭스

| ID | 수단 | 영역 | 본문 채택 권위 | 본문 채택 *범위 한계* |
|----|------|------|----------|--------------|
| **S-1** | custom regex secret scanner (R-4.1 Tier-1 45 patterns) | GP-3 코드 본문 secret 검출 (G3-2) | Group D PoC `tools/secret_scanner.py` 261줄 답습 + actual run `25623028888` SUCCESS + Layer A §1.2 + Layer B §1.1 답습 | Tier-2/3 catalog 확장 0건 / 외부 의존 도입 0건 / runtime code *실 구현* 0건 (별도 단계) |
| **ST-3** | docker secret (저장 경로 isolation) | GP-3 저장 경로 secret 검출 (G3-1) | ADR-008 §2.6.2 R2-1 답습 + Layer A §1.2 + Layer B §1.1 답습 | Vault HSM ST-4 미진입 (Backlog #7 분리) / entrypoint stat ST-1 / inotify ST-2 미진입 (Backlog #1 1.5차 보강 분리) |
| **PC-3** | CI-only enforcement (pre-commit) | GP-3 pre-commit hook 통합 (G3-2 부분 / G5-2 부분 공유) | T2 영역 답습 + Group D actual run SUCCESS 답습 + Layer A §1.2 + Layer B §1.1 답습 | local pre-commit framework PC-4 미진입 (Backlog #1 1.5차 보강 분리) |
| **AR-1** | CI step fail-closed (PR auto-reject) | GP-3 PR auto-reject layer (G3-3 부분 / G5-3 부분 공유) | T2 영역 답습 + Layer A §1.2 + Layer B §1.1 답습 | branch protection AR-2 미진입 (Backlog #3 T3 영역 별도 풀 3+1 분리) |

**추가 본문 채택 영역 (G3-7 row — `secret` MVP-1 영역 4 항목)**:
- (i) GitHub Actions secrets 사용 0건 검증 (F-금지 grep step) — 본문 채택
- (ii) `secrets.*` 참조 감지 (workflow grep step or S-1 확장) — 본문 채택
- (iv) fork PR secret 접근 차단 default 정책 보존 — 본문 채택
- (v) workflow `permissions: contents: read` 명시 강제 (R-6 답습) — 본문 채택

**분리 영역 (G3-7 row 2 항목 — MVP-1 영역 외)**:
- (iii) CI 로그 secret 노출 방지 (전체 책무) = MVP-2 (GP-2 송신 redaction 영역) — 분리
- `pull_request_target` workflow 도입 = 별도 합의 영역 (T2/T3) — 분리

#### 5.5.2 GP-5 본문 채택 3 sub-수단 매트릭스 (PC-3 + AR-1 = GP-3 와 일관성 답습)

| ID | 수단 | 영역 | 본문 채택 권위 | 본문 채택 *범위 한계* |
|----|------|------|----------|--------------|
| **T-6 = T-2 + T-5 병행** | T-2 import-linter + T-5 custom AST 병행 (Layer 1 정적 차단) | GP-5 Layer 1 정적 차단 도구 (G5-1) | Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄) T-2 채택 답습 + Group A 1차/3차 답습 T-5 답습 + `.importlinter` TR-1~TR-5 답습 + actual run `25605665191` + `25629390384` SUCCESS + Layer A §1.3 + Layer B §1.2 답습 | T-1 dependency-cruiser / T-3 grimp / T-4 ruff / T-5 단독 미진입 (Backlog #2 1.5차 보강 분리) + Layer 2 runtime block G5-5 미진입 (MVP-3 분리) + 의미적 lock-in (G4 §4.6) 미진입 (MVP-3 분리) |
| **PC-3** | CI-only enforcement (pre-commit) | GP-5 pre-commit hook 통합 (G5-2) — GP-3 동일 채택 답습 | T2 영역 답습 + 양 GP 일관성 답습 + Layer A §1.3 + Layer B §1.2 답습 | local pre-commit framework PC-4 미진입 (Backlog #2 분리) |
| **AR-1** | CI step fail-closed (PR auto-reject) | GP-5 PR auto-reject layer (G5-3) — GP-3 동일 채택 답습 | T2 영역 답습 + 양 GP 일관성 답습 + Layer A §1.3 + Layer B §1.2 답습 | branch protection AR-2 미진입 (Backlog #3 T3 영역 별도 풀 3+1 분리) |

**추가 본문 채택 영역 (Group A 1차/2차/3차 답습 — Layer 1a + 1b + 1c 분리 답습 완결)**:
- `tools/provider_import_scanner.py` (Group A 1차 답습, AST 5종 패턴) — Layer 1a 본문 채택
- `.importlinter` (Group A 2차 답습, TR-1~TR-5) — Layer 1b 본문 채택
- `tools/provider_url_scanner.py` (Group A 3차 답습, URL Tier-1 10 + Model Tier-1 19) — Layer 1c 본문 채택

**분리 영역**:
- P1 v2 facade real 본문 (G5-4 = `src/adapters/llm/facade.py` LiteLLM 실 import) — Backlog #4 별도 P1 v2 facade MVP 합의 분리
- Layer 2 runtime block (G5-5) — MVP-3 분리
- 의미적 lock-in (G4 §4.6) — MVP-3 분리

#### 5.5.3 본문 채택 합산 매트릭스

| GP | 단독 sub-수단 | 공유 sub-수단 (양 GP 동일) | 합산 |
|----|----------|----------|------|
| GP-3 | S-1 + ST-3 = 2 단독 | PC-3 + AR-1 = 2 공유 | 4 |
| GP-5 | T-6 (T-2 + T-5 병행) = 1 단독 | PC-3 + AR-1 = 2 공유 | 3 |
| 합산 | 3 단독 + 2 공유 = 5 unique + 2 일관성 | — | **9 (7 unique + 2 일관성 중복)** |

본 합산 = **9 sub-수단 본문 채택** (Layer B 합의 §1.1 + §1.2 답습 — 양 GP 5/5 + 5/5 충족 + 7 sub-수단 본문 채택 적격 + 2 sub-수단 일관성 검증).

#### 5.5.4 18 Rollback Trigger 본문 확정 답습 (Layer B §1.7 답습)

본 §은 §3.5 + §4.6 답습 — Rollback Trigger *본문 확정* (발화 시연 = Layer C 영역 분리):

- **GP-3 8개 trigger** = §3.5 답습 (S-1 FP_rate 폭증 / S-2 라이선스 변경 / ST-3 Docker secret 도입 실패 / PC-3 CI runtime 폭증 / AR-1 hook 우회 시도 / R-4.1 Tier-1 catalog 변경 / Tier-2 확장 필요 / Operational Readiness parity 필요)
- **GP-5 10개 trigger** = §4.6 답습 (T-2 FP_rate 폭증 / T-5 단독 FN 폭증 / T-6 병행 충돌 / `.importlinter` rule 충돌 / PC-3 hook 우회 / AR-1 fail-closed 폭증 / P1 v2 facade real 본문 필요 / branch protection 필요 / 의미적 lock-in 검출 / Layer 2 runtime 진입 필요)

**합산: 18/18 Rollback Trigger 본문 확정** (Layer B 합의 §1.7 답습).

#### 5.5.5 본 §5.5 *범위 한계* (사용자 명시 답습 — 본문 채택 ≠ 구현)

본 §5.5 = **9 sub-수단 본문 채택 *문서상 확정* 한정**. 다음은 본 §5.5 *영역 외*:

- ❌ runtime code *실 구현* (Layer B 결과 *행사* 별도 단계 — 사용자 명시 결정 의무)
- ❌ CI workflow *실 신설* / hook *실 구현* (동상)
- ❌ Implementation Evidence PASS *발효* (Layer C 별도 합의)
- ❌ MVP-1 PASS *선언* (Layer D)
- ❌ Operational Readiness PASS *선언* (Layer E)
- ❌ Hermes PMO 격상 *선언* (Layer F)
- ❌ 7 backlog 자동 진입 (1.5차 보강 / T3 / P1 v2 facade / ADR-012 enum / Operational Readiness)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 / ADR-009 / ADR-010 / ADR-011 / ADR-012 본문 변경 0건)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 (Tier-1 답습 한정)
- ❌ threshold *고정* (FP/FN/latency 모두 *후보 한정* 유지)
- ❌ event enum 정식 등록 (4 + 3 = 7 enum *후보 한정*)
- ❌ 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출
- ❌ §3.5 + §4.6 Rollback Trigger 발화 시연 (Layer C 영역 분리)
- ❌ Group A 1차/2차/3차 PoC + Group D PoC 본문 변경 (답습 한정)
- ❌ §3 GP-3 / §4 GP-5 / §5.1 / §5.2 / §5.3 / §5.4 / §6 / §7 본문 변경 (cross-reference 답습 한정)

본 §5.5 *발효 후*에도 다음은 **별도 사용자 명시 결정 의무 영역**:
- runtime code / CI workflow / hook 실 구현 → 별도 commit + 사용자 명시 결정
- Layer C (Implementation Evidence PASS) 진입 → 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시

---

## 6. MVP-1 → MVP-2 진입 조건 권고

본 §은 *MVP-1 exit = Implementation Evidence PASS 발효 후* 의 다음 단계 진입 *권고 수준* 한정. MVP-2 본문 deepening = 별도 합의 영역.

### 6.1 MVP-1 → MVP-2 진입 5 조건

| # | 조건 | 검증 |
|---|------|------|
| 1 | GP-3 Implementation Evidence PASS 발효 | 본 문서 §3.6 답습 + 별도 합의 |
| 2 | GP-5 Implementation Evidence PASS 발효 | 본 문서 §4.7 답습 + 별도 합의 |
| 3 | MVP-1 통합 Evidence Ledger entry 4 enum 등록 (ADR-012 §2.2 답습) | 별도 합의 (G4 §10.2 schema 진화 정책 영역) |
| 4 | MVP-2 영역 (GP-2 + G4 §4.4 Layer 4) 진입 권고 합의 | C-7 line 379 답습 + 별도 합의 |
| 5 | 사용자 명시 결정 (MVP-1 → MVP-2 진입 시점) | 사용자 명시 |

### 6.2 MVP-2 영역 미리 보기 (본 문서 범위 외, 권고 한정)

C-7 line 379 답습 — MVP-2 = G2 GP-2 + G4 §4.4 Layer 4 (log canary + canonical JSON + R-6 workflow ledger 검증):

- **GP-2 (Egress Redaction)** — 본 문서 §1.3 분리 사유 답습. MVP-2 진입 시 본 문서 §3 형식 답습한 별도 deepening 작성 권고.
- **G4 §4.4 Layer 4** — JSONL hash chain + RFC 8785 JCS canonicalization + R-6 workflow ledger 검증. Group C 통합 PoC 답습 (`g4-jsonl-hash-chain-jcs-poc-spec.md`).

본 §6.2 = *권고 한정*. MVP-2 본문 deepening = 본 문서 범위 외 (별도 합의 영역).

---

## 7. 본 문서가 *발생시키는* / *발생시키지 않는* 사항

### 7.1 본 문서가 *발생시키는* 것

- ✅ MVP-1 정의 단일 source-of-truth 통합 (외부 LLM line 242 + C-7 line 378 + 본 문서 §1)
- ✅ 3-layer PASS 분리 (Design Gate / Implementation Evidence / Operational Readiness) 재명시 + MVP-1 위치 매핑
- ✅ GP-3 + GP-5 PoC → MVP-1 진입 *gap 분석* (G3-1 ~ G3-6 + G5-1 ~ G5-7)
- ✅ GP-3 코드 본문 secret 검출 5 수단 후보 비교 (S-1 ~ S-5) + 권고
- ✅ GP-3 저장 경로 secret 검출 5 수단 후보 비교 (ST-1 ~ ST-5) + 권고
- ✅ GP-5 Layer 1 정적 차단 6 수단 후보 비교 (T-1 ~ T-6) + 책무 분담 매트릭스 + 권고
- ✅ GP-5 pre-commit hook 4 수단 후보 비교 (PC-1 ~ PC-4) + 권고
- ✅ GP-5 PR auto-reject 3 수단 후보 비교 (AR-1 ~ AR-3) + 권고
- ✅ GP-3 + GP-5 측정 metric 후보 + threshold 후보 매트릭스
- ✅ GP-3 + GP-5 Rollback Trigger 통합 매트릭스 (8 + 10 = 18 trigger)
- ✅ GP-3 + GP-5 Evidence Required + 의존성 + 합의 형태 권고
- ✅ MVP-1 통합 PASS 기준 (ADR-011 §2.1 (a)~(e) 답습)
- ✅ MVP-1 → MVP-2 진입 조건 5 조건 권고
- ✅ Evidence Ledger entry 4 enum 후보 (ADR-012 §2.2 답습)

### 7.2 본 문서가 *발생시키지 않는* 것 (사용자 명시 답습 — 2026-05-12 진입 명령)

- ❌ 실제 runtime code 구현 (gitleaks/detect-secrets pre-commit hook 본문 / `src/adapters/llm/facade.py` 본문 / inotify sidecar / chmod 600 entrypoint script 등 0건)
- ❌ CI/hook 구현 (`.github/workflows/secret-scan.yml` 신설 / `.pre-commit-config.yaml` 신설 / GitHub branch protection rule 변경 / depcruise/`.dependency-cruiser.cjs` 신설 0건)
- ❌ Hermes PMO 격상 선언 0건
- ❌ Operational Readiness PASS 선언 0건
- ❌ Implementation/Runtime PASS 자동 선언 0건
- ❌ G2 / G3 / G4 Implementation PASS 일괄 선언 0건
- ❌ ADR 본문 자동 갱신 0건 (cross-reference 답습 한정 — 본 문서 §3.6.2 / §4.7.2 의 "MVP-1 PASS 후 별도 commit (본 문서 범위 외)" 답습)
- ❌ 수단 *결정* 0건 (S-1/S-3/T-6/PC-3/AR-1 등 모두 *권고 한정* — *결정* = 별도 합의)
- ❌ Tier-2 / Tier-3 catalog 자동 확장 0건 (R-4.1 Tier-1 42 catalog 답습 한정)
- ❌ threshold *고정* 0건 (FP_rate / scan_latency / hook_runtime 등 모두 *후보 한정*)
- ❌ MVP-2 ~ MVP-6 본문 deepening 0건 (별도 합의 영역)
- ❌ 17 항목 우선순위 자동 *재고정* 0건 (`implementation-runtime-roadmap.md` §5.1 권고 답습 — 사용자 명시 결정 영역 유지)
- ❌ 신규 ADR / 신규 P / 신규 GP 발행 0건
- ❌ ADR-012 §2.2 `event` enum 정식 등록 0건 (본 문서 §5.2 4 enum 후보 = *후보 한정*)
- ❌ 외부 LLM 자동 호출 0건
- ❌ 실 API key / provider SDK / 외부 API 호출 0건

---

## 8. 다음 진입점 (사용자 결정 영역)

본 문서 작성 후 다음 작업 (사용자 결정 영역):

1. **본 문서 Reviewer-only 단축 합의 보고서 작성** (`docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md`) — DRAFT → 권고 권위 발효
2. **GP-3 MVP-1 진입 합의** — S-1 단독 채택 + ST-3 단독 채택 (저장) + PC-3 단독 채택 (CI-only) + AR-1 단독 채택 시 단축 합의 적격
3. **GP-5 MVP-1 진입 합의** — T-6 채택 (현 PoC 답습) + PC-3 + AR-1 단독 시 단축 합의 적격
4. **MVP-1 1.5차 보강 합의** — S-3 detect-secrets 부분 통합 / ST-2 inotify sidecar / PC-1 pre-commit framework / AR-3 통합 = 단축 합의 또는 풀 3+1 (수단별 §3.6.3 / §4.7.3 답습)
5. **MVP-1 PASS 발효** — GP-3 + GP-5 양쪽 ADR-011 §2.1 (a)~(e) 5/5 충족 + 사용자 명시 + Implementation Evidence PASS 발효 합의
6. **MVP-1 → MVP-2 진입 합의** — §6.1 답습 5 조건 충족 후 사용자 명시 결정

**권고 시작 명령 (사용자 권한 영역)**:
- (a) "본 MVP-1 roadmap 의 Reviewer-only 단축 합의 보고서를 작성해주세요" → 본 문서 권위 발효
- (b) "GP-3 MVP-1 진입 합의 (S-1 + ST-3 + PC-3 + AR-1) 시작" → GP-3 MVP-1 1차 합의
- (c) "GP-5 MVP-1 진입 합의 (T-6 + PC-3 + AR-1) 시작" → GP-5 MVP-1 1차 합의
- (d) "MVP-1 1.5차 보강 합의 진입" → 풀 3+1 합의 영역
- (e) "MVP-2 영역 (GP-2 + G4 §4.4 Layer 4) deepening 작성" → MVP-2 영역 진입 (별도 합의)

---

## 9. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-27 | 본 문서 DRAFT → APPROVED 권위 발효 (Reviewer-only 단축 합의) | `docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md` APPROVE (단축 합의 — Reviewer-only). 입력 = `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (2026-05-27 audit). **5/5 풀 3+1 승격 트리거 0건 발화 검증** (① 새 권위 결정 0 / ② Tier-2/3 catalog 자동 확장 0 / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0). 후속 3 합의 본문 흡수 완료 cross-check (line 819~821 = gp3 + gp5 + backlog #6) + ADR-011 §2.1 (a)~(e) 답습 정확. **본 합의 = 권위 표시 격상 한정 — line 826/827 상태 표시 + §9 변경 이력 line 1건 추가 한정 — 본문 §1~§8 변경 0건 (cross-reference 답습 한정). 실 runtime code / CI / hook 변경 0건 / Implementation Evidence PASS / Operational Readiness PASS / ADR 본문 갱신 / 수단 결정 / threshold 고정 / Tier-2/3 자동 확장 모두 본 합의 영역 외 (사용자 명시 결정 의무 영역)**. |
| 2026-05-12 후속 4 | §5.5 9 sub-수단 본문 채택 매트릭스 신설 — Layer B `f40423f` 발효 결과 행사 | Backlog #6 Layer B Implementation Entry 합의 (`docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` APPROVE, commit `f40423f` push 완료) §1.1 + §1.2 + §1.7 답습 + 사용자 명시 진입 명령 (2026-05-12 열한 번째 — "9 sub-수단 본문 채택 commit 진입"). §5.5 신설 = §5.5.0 본문 채택 의미 명시 (본문 채택 ≠ runtime code 구현 / CI workflow 구현 / hook 구현 / Implementation Evidence PASS) + §5.5.1 GP-3 4 sub-수단 (S-1 + ST-3 + PC-3 + AR-1) + G3-7 row 4 항목 + §5.5.2 GP-5 3 sub-수단 (T-6 = T-2 + T-5 / PC-3 + AR-1) + Group A 1차/2차/3차 답습 + §5.5.3 합산 매트릭스 (9 = 7 unique + 2 일관성 중복) + §5.5.4 18 Rollback Trigger 본문 확정 답습 + §5.5.5 *범위 한계* (runtime code / CI workflow / hook 실 구현 0건 / Layer C 발효 0건 / 7 backlog 자동 진입 0건 / ADR 본문 갱신 0건 / Tier-2/3 자동 확장 0건 / threshold 고정 0건 / event enum 정식 등록 0건). **본 흡수 = §5.5 신설 + 변경 이력 추가 한정 — §3 GP-3 / §4 GP-5 / §5.1 / §5.2 / §5.3 / §5.4 / §6 / §7 본문 변경 0건 (cross-reference 답습 한정)**. **본문 채택 = 문서상 확정 한정 — runtime code 실 구현 / CI workflow 실 신설 / hook 실 구현 모두 본 흡수 영역 외 (사용자 명시 결정 의무 영역)**. |
| 2026-05-12 후속 2 | §5.4 GP-3 + GP-5 Integrated Risk Matrix 신설 — Observation O-2 흡수 (GP-5 진입 합의 Condition C-4) | GP-5 MVP-1 진입 합의 (`3plus1-consensus-2026-05-12-gp5-mvp1-entry.md` APPROVE WITH CONDITIONS) §6.3 + §7.4 답습 + 사용자 명시 진입 명령 (2026-05-12 여섯 번째). §5.4 신설 = 3 통합 위험 (IR-1 Provider key adapter bypass / IR-2 Direct SDK + secret leakage 결합 / IR-3 Local-CI-Docker mismatch) + 3 신규 evidence enum 후보 (`provider_key_adapter_bypass_risk_detected` / `direct_sdk_with_secret_leakage_detected` / `secret_handling_environment_mismatch_detected`) + MVP-1 handling vs Deferred handling 분리 + §5.4.4 *범위 한계* (실 combined check 도구 구현 0건 / enum 정식 등록 0건 / Runtime enforcement 0건 / Operational parity 0건 / Provider key auto revoke 0건 / Combined fail PR auto-reject 0건). §5.2 cross-reference 갱신 — 4 enum → 7 enum 후보 합산. **본 흡수 = §5.4 신설 + §5.2 cross-reference 갱신 + 변경 이력 추가 한정 — §3 GP-3 / §4 GP-5 / §5.1 / §5.3 / §6 / §7 본문 변경 0건**. |
| 2026-05-12 후속 | §3.1.2 G3-7 row 추가 (CI secret 관리) — Condition C-1 흡수 | GP-3 MVP-1 진입 합의 (`3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` APPROVE WITH CONDITIONS) §2 (Observation O-1 흡수) + §6.1 + §7.1 답습. G3-7 = 6 항목 中 (i)(ii)(iv)(v)(vi) = MVP-1 영역 4 항목 + (iii) = MVP-2 (GP-2 영역) + (`pull_request_target` 도입) = 별도 합의 영역 분리. 핵심 요약 (line 169) 갱신 — "G3-1 + G3-2 + G3-3 + G3-7" 영역 명시. **본 흡수 = §3.1.2 본문 갱신 + 핵심 요약 갱신 한정 — §3.5 Rollback / §3.6 Evidence / §5 통합 PASS / §6 / §7 본문 변경 0건 (cross-reference 답습 한정)**. |
| 2026-05-12 | 신규 작성 (DRAFT) | MVP-1 deepening (GP-3 + GP-5) — 사용자 명시 답습: 단일 새 문서 + 수단 후보 비교 + threshold 후보 + Reviewer-only 단축 합의 진행 예정. 실 runtime code 구현 / CI/hook 구현 / Hermes PMO 격상 / Operational Readiness PASS 선언 모두 본 작업 범위 외. `implementation-runtime-roadmap.md` 17 항목 우선순위 매트릭스 (Order 1 = GP-5, Order 4 = GP-3) 의 MVP-1 영역 deepening 한정. 외부 LLM 응답 line 242 + C-7 line 378 + 본 문서 §1 통합 = MVP-1 = G2 GP-3 + GP-5 (GP-2 = MVP-2 분리 답습). 3-layer PASS 분리 (Design Gate / Implementation Evidence / Operational Readiness) 재명시 + MVP-1 위치 = Implementation Evidence PASS 1차. GP-3 PoC (Group D) + GP-5 PoC (Group A 1차/2차/3차) 답습. GP-3 코드 본문 5 수단 (S-1~S-5) + 저장 경로 5 수단 (ST-1~ST-5) + GP-5 Layer 1 도구 6 수단 (T-1~T-6) + pre-commit 4 수단 (PC-1~PC-4) + PR auto-reject 3 수단 (AR-1~AR-3). Rollback Trigger 통합 18 + Evidence Ledger 4 enum 후보 + 합의 형태 권고. |

---

**작성일**: 2026-05-12 (DRAFT) — 2026-05-27 APPROVED
**상태**: ✅ **APPROVED** (2026-05-27 Reviewer-only 단축 합의 — `docs/review/3plus1-consensus-2026-05-27-implementation-runtime-roadmap-mvp1-authority.md`, 5/5 풀 3+1 승격 트리거 0건 발화, 후속 3 합의 본문 흡수 완료)
**다음 단계**: §8 권고 순서 (b) MVP-1 1.5차 보강 합의 → (c) Implementation Evidence PASS 발효 합의 (사용자 결정 영역)
**금지 (사용자 명시 답습 — 2026-05-12 진입 명령, 변동 없음)**:
- ❌ 실제 runtime code 구현
- ❌ CI/hook 구현
- ❌ Hermes PMO 격상
- ❌ Operational Readiness PASS 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ ADR 본문 자동 갱신
- ❌ 수단 *결정*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold *고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ 17 항목 우선순위 자동 *재고정*
