# G2 GP-5 — Provider Liquidity Enforcement MVP-1 Implementation Evidence (통합)

> **본 문서 = GP-5 MVP-1 Implementation Evidence PASS 발효 (33번째 entry, 2026-05-27) evidence 통합**. ADR-011 §2.1 (a)~(e) 5 조건 + AR-3 (GP-3+GP-5 통합) + 첫 PR evidence + R-S1 cross-reference 정정 cascade 답습.
>
> **scope**: GP-5 영역 한정 (GP-3 = `g2-gp3-mvp1-evidence.md` 별도). PoC evidence (Group A 1차/2차/3차) = `g2-gp5-provider-adapter-enforcement-poc.md` + `g2-gp5-poc2-depcruise-rule-scope.md` + `g2-gp5-poc2-import-linter-implementation.md` + `g2-gp5-poc3-url-endpoint-model-name-scanner.md` 답습.

---

## §0 답습 출처

| Source | 위치 | 답습 내용 |
|---|---|---|
| 33번째 entry MVP-1 PASS 발효 합의 | `docs/review/3plus1-consensus-2026-05-27-mvp1-implementation-evidence-pass-activation.md` | APPROVE WITH CONDITIONS |
| 24번째 entry brief v1.1 | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` | MVP-1 1.5차 보강 entry brief |
| 29-31번째 entry AR-3 sub-cycle | `docs/phase0/mvp1-ar3-pr-auto-reject-brief.md` + 합의 + chain `7f57323` + `7c294bb` + `73ed20d` + `9837298` | branch protection 7 contexts 발효 (GP-3+GP-5 통합) |
| 33번째 entry PASS 발효 brief v1.1 | `docs/phase0/mvp1-implementation-evidence-pass-activation-brief.md` | GP-5 5/5 매트릭스 + R-2 (GP-5 (c) R-S1 표기 제거) + R-3 (multi-source 재기술) |
| 35-38번째 entry R-S1 cascade | 198 위치 정정 완료 (영원 종결) |
| roadmap-mvp1 §2.2 + §4 | `docs/architecture/implementation-runtime-roadmap-mvp1.md` | MVP-1 Exit 기준 + GP-5 영역 본문 |
| Group A 1차/2차/3차 PoC | `g2-gp5-*-poc.md` chain | AST 5종 + depcruise vs import-linter + URL/Model scanner |

---

## §1 GP-5 ADR-011 §2.1 (a)~(e) 5 조건 evidence 매트릭스

### 1.1 (a) 동등 이상의 보안 결과 ✅

**Provider Liquidity 5-way 답습 (헌법 5조-2 비협상)**:
- **import-linter** (T-2 contract TR-1~TR-5) — `.importlinter` 답습 (Group A 2차 PoC 답습)
- **provider-import-scanner** (T-5 부분 — AST 5종 패턴) — `tools/provider_import_scanner.py` 답습
- **provider-url-scanner** (T-5 부분 — URL + Model Tier-1 catalog) — `tools/provider_url_scanner.py` 답습
- **AR-3** (branch protection 7 contexts, 30/31번째 entry) — `provider-adapter-enforcement.yml` + `provider-url-scanner.yml` workflow 매핑

→ Provider lock-in 차단 + 어댑터 추상화 강제 충족 자격 자격.

### 1.2 (b) 격리 환경 PoC 실증 ✅

- Group A 1차 PoC — AST 5종 패턴 (direct / from / dynamic / double-underscore / model-name) verify
- Group A 2차 PoC — depcruise vs import-linter 비교 (T-2 채택 답습)
- Group A 3차 PoC — provider URL scanner (T-5 부분, URL Tier-1 10 + Model Tier-1 19)
- **31번째 entry 첫 PR PASS evidence** (head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`):
  - `enforce` x3 모두 SUCCESS (evidence-pass-gate + g4-hash-chain + provider-adapter-enforcement)
  - `scan` (provider-url-scanner) SUCCESS
  - 11/11 check_runs SUCCESS + mergeable CLEAN
  - 중복 동작 race 0 확정 ✅

### 1.3 (c) ADR / SDD 권위 명시 ✅

**multi-source 재기술 (35-38번째 R-S1 cascade 답습)**:
- ADR-008 차단조건 #4 (어댑터 추상화, line 97/149)
- ADR-008 부록 B (Hermes PMO 격상 절차 + cross-reference Amendment)
- ADR-009 C-N §5 (자체 Adapter v2.0)
- ADR-011 (수단/목적 분리 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e))
- P1 v2 (Provider Liquidity 강화)
- roadmap-mvp1 §4 (GP-5 MVP-1 Deepening)
- 헌법 5조-2 (Provider Liquidity 비협상)
- Group A 2차/3차 합의 본문
- AR-3 sub-cycle brief + 합의 (29-31번째 entry, GP-3+GP-5 통합 영역)

→ R-2 BLOCKING (33번째 entry, GP-5 (c) R-S1 표기 제거) 답습 — 차단조건 #4 = R-S1 무관 (ADR-008 line 97/149 정합 attribution).

### 1.4 (d) 자동 회귀 검증 경로 ✅

- `.github/workflows/provider-adapter-enforcement.yml` — import-linter + provider-import-scanner step
- `.github/workflows/provider-url-scanner.yml` — provider-url-scanner step
- `on:` pull_request trigger (paths 필터 0건 = 매 PR 발화 보장, 34번째 entry audit 답습)
- 31번째 entry 첫 PR actual run id evidence:
  - `enforce` x3 = `evidence-pass-gate` (run id 부분) + `g4-hash-chain` + `provider-adapter-enforcement` 모두 SUCCESS
  - `scan` (`provider-url-scanner.yml`) SUCCESS
- AR-3 branch protection rule (30/31번째 entry) — required status checks `enforce` + `scan` + `validate` 등 7 contexts, `enforce_admins: true`

### 1.5 (e) 합의 APPROVE 운영조건 ✅

- 24번째 entry brief APPROVE WITH CONDITIONS (풀 3+1 + 외부 LLM 1+, AR-3 = GP-3+GP-5 통합)
- 29번째 entry AR-3 sub-cycle APPROVE (Reviewer-only 단축 합의)
- 30번째 entry AR-3 admin scope 적용 (사용자 명시)
- 31번째 entry 첫 PR evidence 조치 (사용자 결정 2건: fixture 정정 + contexts v2)
- 33번째 entry MVP-1 PASS 발효 합의 APPROVE WITH CONDITIONS (풀 3+1 + 외부 LLM 1+)

→ **GP-5 5/5 충족 자격 자격 자격 ✅** (33번째 entry MVP-1 PASS 완전 발효 (α) 답습).

---

## §2 AR-3 통합 PR auto-reject (GP-3 + GP-5 통합, 29-31번째 entry)

본 §은 `g2-gp3-mvp1-evidence.md §2.4` 와 중복 답습 — GP-3 + GP-5 통합 영역 (AR-3 = branch protection rule = GP-3 secret check + GP-5 provider check 통합).

### 2.1 7 contexts 매핑

| context | workflow | 영역 |
|---|---|---|
| `guard` | boundary-guard.yml | GP-3/GP-4 boundary |
| `verify` | history-anchor-verifier.yml | G4 history |
| `feasibility` | memory-skill-migration-feasibility.yml | GP-6 |
| `scan` x2 | provider-url-scanner + secret-hygiene-egress-redaction | **GP-5 + GP-3** 통합 |
| `enforce` x3 | evidence-pass-gate + g4-hash-chain + provider-adapter-enforcement | G4 + **GP-5** |
| `defense` | rewrite-defense.yml | G4 |
| `validate` | schema-validation.yml | GP-4 |

→ GP-5 관련 contexts: `scan` (provider-url-scanner) + `enforce` (provider-adapter-enforcement).

### 2.2 R-MVP1-1.5-AR3 trigger 답습

| ID | trigger | 발효 형태 |
|---|---|---|
| R-MVP1-1.5-AR3-1 | branch protection rule 우회 / admin bypass 발견 | 단축 합의 + 사용자 명시 |
| R-MVP1-1.5-AR3-2a | 11 workflow 본문 변경 — 도구 변경 영향 분석 | 단축 합의 + check name catalog 정정 |
| R-MVP1-1.5-AR3-2b | 신규 status check 추가 — T3 정책 영역 | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| R-MVP1-1.5-AR3-3 | MVP-1 영역 외 다른 rule | 별도 합의 영역 (N-6 답습) |

---

## §3 첫 PR evidence (31번째 entry — GP-5 관련)

- PR #2 draft head SHA `9837298befdeda6c7e170879cc9f15e331c52bce`
- GP-5 관련 check_runs:
  - `enforce` (evidence-pass-gate) SUCCESS
  - `enforce` (g4-hash-chain) SUCCESS
  - `enforce` (provider-adapter-enforcement) SUCCESS — **GP-5 핵심**
  - `scan` (provider-url-scanner) SUCCESS — **GP-5 핵심**
- 중복 동작 race 0 확정 (`enforce` x3 모두 PASS 의무 답습)
- admin bypass 0 시도 evidence

---

## §4 R-S1 cross-reference 정정 cascade 답습 (35-38번째 entry, 영원 종결)

R-S1 정정 cascade (`g2-gp3-mvp1-evidence.md §4` 답습) = **198 위치 정정 완료 영원 종결 ✅**.

GP-5 영역 영향:
- 33번째 entry R-2 BLOCKING (GP-5 (c) R-S1 표기 제거 = 차단조건 #4 attribution 정확화) 답습
- 35번째 entry brief 정정 + 36-38번째 entry cascade 정정 모두 답습
- R-MVP1-PASS-2 영구 금지 답습 (ADR-008 본문 변경 0건)

---

## §5 carry-over

- (d) facade real (TR-1 자동 풀 3+1 trigger, 별도 trajectory) — `src/adapters/llm/facade.py` placeholder → real 본문
- MVP-2 진입 자격 검토 (별도 합의 영역, MVP-1 PASS 완전 발효 후 자격 충족)
- (b1-AR3 develop) develop branch 생성 시점 동일 7 contexts body PUT

---

## §6 본 evidence 자기진단 (5/5 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | GP-5 ADR-011 §2.1 (a)~(e) 5/5 충족 evidence 명문 | ✅ §1 |
| 2 | AR-3 통합 (GP-3 + GP-5 영역) 본문 + 7 contexts 매핑 | ✅ §2 |
| 3 | 31번째 entry 첫 PR GP-5 관련 check_runs PASS evidence | ✅ §3 |
| 4 | R-S1 cross-reference 정정 cascade 답습 + R-2 BLOCKING 답습 (GP-5 (c) R-S1 무관 정합) | ✅ §4 |
| 5 | carry-over (d) facade real + MVP-2 + develop branch 답습 | ✅ §5 |
