# Phase 1 Acceptance SOP — Redaction Verification (R-7)

> **G1b 정식 충족 절차의 SOP 화. R-1 ~ R-6 산출을 운영자/리뷰어가 따라야 할 *체크리스트* + *판정 기준* + *증거 제출 양식* 으로 통합. R-6 GitHub Actions 실제 run 성공 후 G1b PASS 승격.**

**상태**: 작성 완료 (R-7) — 본 R-7 발행 시점 = G1b **CONDITIONALLY PASS** (R-6 push 전, GitHub Actions 실제 run 미확인)
**날짜**: 2026-05-06
**상위 권위**: ADR-008 부록 B.6 6단계 마지막 + ADR-011 §3 R-7 매핑
**입력 자료**: R-1 / R-2 / R-3 / R-4 / R-4.1 / R-5 / R-6 산출 전체

---

## 0. 핵심 선언 (사용자 명시 답습)

> **R-6 workflow 의 GitHub Actions 실제 run 성공은 Phase 1 합격 조건이다. 로컬 17/17 검증만으로 G1b 최종 충족을 선언하지 않는다.**

본 SOP 는 위 선언을 모든 § 의 *판정 기준*에 강제한다. 본 R-7 발행 자체가 G1b PASS 를 선언하지 않으며, R-6 actual run PASS 검증 후에만 G1b 가 PASS 로 승격된다.

---

## 1. 작업 정의

### 1.1 본 R-7 의 본질

R-7 = **Phase 1 acceptance SOP**. R-1 ~ R-6 의 모든 evidence + 판정 + 절차를 *운영자가 단일 체크리스트로 따라할 수 있는 SOP* 양식으로 통합.

본 R-7 자체가 Phase 1 acceptance 를 *판정*하지 않는다. R-7 은 *판정 절차*만 정의한다. 실제 판정은 R-7 SOP 를 따라 운영자/리뷰어가 수행.

### 1.2 ADR-008 부록 B.6 6단계 — 본 R-7 발행 후 상태

```
R-3   ✅ 본 Amendment 발행 (2026-05-06)
R-4   ✅ 패턴 동등성 비교 + gap 식별 + 보충 권고 (2026-05-06)
R-4.1 ✅ Tier-1 42종 trigger UDF 확장 + 격리 환경 PoC PASS (2026-05-06)
R-5   ✅ canary 재검증 트리거 설계 (2026-05-06)
R-6   ✅ CI/nightly canary regression workflow 구현 (2026-05-06, commit bbcc1af)
R-7   ✅ Phase 1 합격 SOP (본 문서, 2026-05-06)
```

**6단계 모두 작성 완료**. 그러나 G1b 정식 PASS 는 *6단계 작성 ✅ + R-6 GitHub Actions 실제 run PASS* 까지 요구.

### 1.3 본 R-7 이 *하지 않는* 것 (사용자 명시 금지 사항)

- ❌ G1b 최종 PASS 선언 — R-6 actual run 미확인 시점
- ❌ Hermes PMO 격상 선언 — 4 게이트 통과 후 별도 결정
- ❌ P2 v3 본문 작성 — Phase 1 acceptance PASS 후 별도 작업
- ❌ 실제 secret 사용 / Tier-2 / Tier-3 catalog 확장 — ADR-011 §2.4 + 사용자 명시 범위 외
- ❌ CI 자동 정책 변경 허용 — ADR-011 §2.4 T3 절대 금지

---

## 2. Phase 1 Acceptance Checklist (13 항목)

운영자가 Phase 1 acceptance 판정 시 다음 13 항목을 순차 검증.

### 2.1 R-1 / G1a 기록 보존

- [ ] **C1**: R-1 FAIL evidence 보존 — `docs/phase0/day2-r1-redaction-location-verification.md`
- [ ] **C2**: G1a (Hermes native redaction → DB INSERT) FAIL 명시 — `agent/redact.py` docstring "for logs and tool output", redact import 25개 비-DB, hermes_state.py redact import 0건

### 2.2 R-2 / G1b 기준선

- [ ] **C3**: R-2 SQLCipher trigger PoC PASS evidence — `docs/phase0/day3-r2-sqlite-trigger-poc.md` (5 prefix patterns, 6 자동 검증 PASS)
- [ ] **C4**: G1b (DB-level fallback) 대체 게이트 정의 — ADR-011 §2.2 / ADR-008 부록 B.2

### 2.3 R-3 ~ R-5 산출 완료

- [ ] **C5**: R-3 ADR-011 + ADR-008 Amendment 완료 — `docs/decisions/ADR-011-means-vs-ends-redaction.md` + 부록 B + 단축 합의 보고서
- [ ] **C6**: R-4 pattern equivalence 완료 — `docs/architecture/redaction-pattern-equivalence.md`
- [ ] **C7**: R-4.1 Tier-1 42 canary 42/42 BLOCK 완료 — `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/`
- [ ] **C8**: R-5 canary recheck design 완료 — `docs/architecture/canary-recheck-design.md`

### 2.4 R-6 검증 (로컬 + 실제 run)

- [ ] **C9**: R-6 workflow 로컬 검증 완료 — `.github/workflows/r2-canary.yml` + 17/17 자동 검증 PASS (본 SOP § 6.2)
- [ ] **C10**: R-6 GitHub Actions 실제 run 성공 ← **본 SOP 발행 시점 미충족 (push 전)**

### 2.5 보안 원칙 검증

- [ ] **C11**: 실제 secret 미사용 확인 — workflow `${{ secrets.* }}` 참조 0건 + Tier-1 fake canary marker `R41T` 만 사용 (R-4.1 §1.3)
- [ ] **C12**: 로그/에러/DB 에 canary 평문 미노출 확인 — R-4.1 evidence § 7 C5/C6 PASS + R-5 § 6 안전장치 4 항목

### 2.6 Evidence 존재

- [ ] **C13**: Evidence 문서 + artifact 존재 — 본 SOP § 6 의 7 항목 (E1 ~ E7) 모두 충족

---

## 3. PASS / PARTIAL / FAIL 판정 기준

### 3.1 PASS

다음 조건 *모두* 충족:

| # | 조건 |
|---|------|
| 1 | ADR-008 부록 B.6 6단계 (R-3 ~ R-7) 모두 ✅ |
| 2 | R-6 GitHub Actions 실제 run PASS (verdict = "PASS", tier1_pass_rate = "42/42") |
| 3 | Phase 1 Acceptance Checklist § 2 의 13 항목 (C1 ~ C13) 모두 체크 |
| 4 | Evidence § 6 의 E1 ~ E7 모두 존재 |
| 5 | ROLLBACK 조건 § 5 의 R1 ~ R9 *어느 것도* 발화 안 함 |

→ **G1b PASS 승격** + Phase 1 acceptance 통과.

### 3.2 PARTIAL

(다음 중 하나):

- 문서/로컬 검증 (R-3 ~ R-7) 완료, GitHub Actions 실제 run 미확인 (push 전)
- GitHub Actions run PASS 인데 Evidence 일부 미흡
- Tier-1 catalog 갱신 진행 중 (catalog version mismatch — R-5 § 2.3 drift 감지)

→ **G1b CONDITIONALLY PASS**. Phase 1 acceptance 차단. 미흡 항목 정정 후 재판정.

### 3.3 FAIL

다음 중 *하나라도* 발생:

- canary 차단 실패 (Tier-1 42/42 미달)
- DB 에 canary 평문 저장 검출 (raw byte scan 매칭)
- 로그/에러에 canary 평문 노출 검출
- GitHub Actions workflow run 실패
- workflow 에 실제 secret 참조 발견
- CI 가 문서/ADR/정책 자동 수정 시도 발견
- safe message INSERT 과도 차단 (false-positive rate > 10%, R-5 § 5.5 ROLLBACK trigger)
- 정책 자동 변경 발생 (ADR-011 §2.4 T3 위반)

→ **G1b PASS 절대 차단**. § 5 ROLLBACK 절차 + ADR-011 §2.4 T3 (단축/풀 합의 의무).

### 3.4 본 R-7 발행 시점 판정

> **Current status before push: PARTIAL — waiting for GitHub Actions actual run after push.**

(사용자 명시 답습. § 1.2 의 6단계 작성 ✅ 와 § 0 의 핵심 선언이 결합한 결과.)

---

## 4. G1a / G1b 최종 정리

### 4.1 G1a — FAIL (폐기)

```
G1a: Hermes native redaction applies before DB INSERT
Result: FAIL
Evidence: docs/phase0/day2-r1-redaction-location-verification.md
폐기 사유: agent/redact.py 가 로그/도구/송신 전용. DB INSERT 미적용 확정.
권위: ADR-011 §2.2 + ADR-008 부록 B.2
```

### 4.2 G1b — CONDITIONALLY PASS (본 R-7 발행 시점)

```
G1b: DB-level fallback prevents plaintext secret persistence
Result: CONDITIONALLY PASS

Conditions for full PASS:
  1. R-3 ~ R-7 모두 ✅ (ADR-008 부록 B.6 6단계 충족)
     → 본 R-7 발행 시점 ✅ 충족
  2. R-6 GitHub Actions actual run PASS
     → ⏳ push 후 검증 대기

Status mapping:
  - 본 R-7 발행 시점 (push 전): CONDITIONALLY PASS
  - R-6 push + actual run PASS 후: PASS (단축 합의 후 본 SOP §7.3 절차)
  - R-6 actual run FAIL 시: G1b 재판정 + § 5 ROLLBACK + 단축/풀 합의

권위: ADR-011 §2.2 + ADR-008 부록 B.6 + 본 SOP § 0 핵심 선언
```

### 4.3 G1b 승격 절차

R-6 push → GitHub Actions run trigger → workflow 결과 확인 →
- **PASS** → 본 SOP § 7.3 단축 합의 → G1b PASS 선언 + ADR-008 부록 B.6 갱신
- **FAIL** → § 5 ROLLBACK trigger 매핑 → 단축/풀 합의 + ADR-011 §2.4 T3 절차

승격 자체도 ADR-011 §2.4 T2 (사용자 승인 필요) 적용 — **자동 승격 금지**.

---

## 5. 자동 ROLLBACK 조건 (사용자 명시 9건)

다음 중 *하나라도* 발생 시 Phase 1 acceptance 차단 + ROLLBACK 또는 재검토 trigger.

| # | 조건 | ROLLBACK 종류 | 권한 |
|---|------|---------|------|
| **R1** | canary insert 가 DB 에 commit 됨 | trigger UDF 갱신 PR revert + 이전 commit 복원 | automatic (R-5 § 5.5 답습) |
| **R2** | DB raw byte scan 에서 canary marker `R41T` 발견 | 동상 | automatic |
| **R3** | 에러/로그에 canary 평문 노출 | 동상 + 보안 incident report | automatic |
| **R4** | Tier-1 42 canary 중 하나라도 BLOCK 실패 | trigger UDF 갱신 PR revert + ADR-011 §2.4 T3 절차 강제 | automatic |
| **R5** | safe message insert 가 과도하게 차단 (false-positive rate > 10%) | trigger UDF PR revert | automatic |
| **R6** | GitHub Actions workflow 실패 | PR merge 차단 | automatic (R-6 workflow exit code) |
| **R7** | workflow 에서 실제 secret 참조 발견 | workflow PR revert + 보안 incident | automatic + manual |
| **R8** | CI 가 문서/ADR/정책 자동 수정 시도 | workflow PR revert + ADR-011 §2.4 T3 위반 alert | automatic + manual |
| **R9** | Hermes upstream 변경 후 R-6 regression 실패 | hermes-agent 버전 핀 복원 + 단축 합의 | manual + 단축 합의 |

ROLLBACK 후에는 ADR-011 §2.4 T3 절차 (단축 또는 풀 합의) 거쳐 재진입 결정.

---

## 6. Evidence 요구사항 (E1 ~ E7)

### 6.1 필수 Evidence 매핑

| # | Evidence | 경로 | 본 R-7 발행 시점 상태 |
|---|---------|------|------|
| **E1** | R-2 PoC report | `docs/phase0/day3-r2-sqlite-trigger-poc.md` | ✅ |
| **E2** | R-4 pattern equivalence report | `docs/architecture/redaction-pattern-equivalence.md` | ✅ |
| **E3** | R-4.1 trigger extension evidence | `docs/phase0/r4-1-trigger-extension-evidence.md` | ✅ |
| **E4** | R-5 canary recheck design | `docs/architecture/canary-recheck-design.md` | ✅ |
| **E5** | R-6 workflow file | `.github/workflows/r2-canary.yml` | ✅ |
| **E6** | R-6 local validation result | 본 SOP § 6.2 (commit `bbcc1af` 메시지 + 17/17 PASS) | ✅ |
| **E7** | R-6 GitHub Actions artifact (`r2-r4-canary-evidence`) | GitHub Actions UI > workflow run > Artifacts | ⏳ push 후 |

### 6.2 R-6 Local Validation Result (E6 본문 기록)

| 항목 | 값 |
|------|-----|
| 검증 시점 | 2026-05-06 (R-6 commit `bbcc1af` 직전) |
| 검증 도구 | Python `yaml.safe_load` + Acceptance Criteria 자동 점검 inline 스크립트 |
| 검증 결과 | **17/17 PASS** |

**상세 카테고리**:

| 카테고리 | 항목 수 | 결과 |
|------|------|------|
| 사용자 명시 9 (workflow_dispatch / nightly schedule / push & PR paths / Docker 실행 / exit code 실패 차단 / JSON evidence 추출 / artifact 업로드 / 실 secret 미사용 / CI 자동 commit/push 없음) | 9/9 | PASS |
| 추가 정합 8 (`--exit-code-from` propagation / `set -o pipefail` / artifact `if: always()` / artifact name 정확 / `permissions.contents = read` / verdict PASS 검증 / Tier-1 42/42 검증 / push & PR paths 5종 일치) | 8/8 | PASS |

### 6.3 R-6 GitHub Actions Artifact (E7 — push 후)

**Artifact 이름**: `r2-r4-canary-evidence`
**필수 포함 파일**:
- `canary-output.log` — PoC stdout 전체 (Tier-1 42 결과 표 + 자동 검증 6항목 + JSON_EVIDENCE_BEGIN/END 마커)
- `canary-evidence.json` — JSON 본문 추출 (verdict, tier1_pass_rate, p3_db_clean, p4_error_clean, p5_drift_count 등 R-5 § 7.1.2 schema)

**보존 정책**: 30일 retention (R-6 workflow `retention-days: 30`)
**접근 경로**: GitHub Actions UI > workflow run > Artifacts > `r2-r4-canary-evidence`

**보존 기간 후 evidence 보강 권고** (별도 PR — R-7 미포함):
- R-5 § 7.1.1 Markdown summary 본문화 — `docs/operations/canary-recheck/{YYYY-MM-DD}-{trigger-id}.md`
- R-5 § 7.1.2 JSONL append-only — `docs/operations/canary-recheck/events.jsonl`
- 30일 후 GitHub Actions artifact 손실 시에도 영구 evidence 보존

---

## 7. Push 전/후 작업 분리

### 7.1 Push 전 (본 R-7 발행 시점, 2026-05-06)

| 작업 | 상태 | Commit |
|------|------|------|
| R-3 ~ R-6 모든 commit 생성 | ✅ | `3e2be57`, `3b005f0`, `e1fb4be`, `62d2a95`, `5a6049d`, `bbcc1af` |
| R-7 SOP 작성 (본 문서) | ✅ | (이번 commit) |
| 로컬 working tree clean | ✅ | (이번 commit 전) |
| `.claude/settings.local.json` untrack | ✅ | `c6fe1ab` |
| R-6 로컬 검증 17/17 PASS | ✅ | 본 SOP § 6.2 |

→ **현재 판정**: **PARTIAL** (G1b CONDITIONALLY PASS).

### 7.2 Push 트리거 절차

운영자가 Phase 1 acceptance 시도 시 다음 순서 실행:

1. 사용자 명시 push 보류 해제 결정
2. `git push -u origin feature/hermes-phase0` (또는 PR 생성)
3. GitHub Actions 자동 trigger:
   - `push` event + paths 매칭 (`.github/workflows/r2-canary.yml` 변경 감지)
   - `pull_request` event + paths 매칭 (PR 생성 시)
4. workflow 결과 확인 (Actions UI):
   - **PASS** → § 7.3 진입
   - **FAIL** → § 5 ROLLBACK 절차

### 7.3 Push 후 (R-6 actual run PASS 시)

| 작업 | 책임 |
|------|------|
| R-6 GitHub Actions artifact 다운로드 + evidence 보존 (E7 충족) | 운영자 + 본 SOP § 6.3 |
| 본 SOP § 4.2 G1b status 갱신 — CONDITIONALLY PASS → PASS | 단축 합의 (Reviewer-only, ADR-011 §2.4 T2) + 별도 docs commit |
| ADR-008 부록 B.6 갱신 — 6단계 모두 ✅ + G1b PASS 도달 명시 | 동 단축 합의 |
| Phase 1 Acceptance Checklist § 2 의 C10 ✅ 체크 | 운영자 |
| Phase 1 acceptance PASS 선언 | 사용자 명시 결정 |
| **P2 v3 신규 작성 진입** | Phase 1 acceptance PASS 후 별도 작업 |

### 7.4 본 R-7 발행 시점 *금지* 사항 (사용자 명시 답습)

| 금지 항목 | 사유 |
|---------|------|
| G1b PASS 선언 | R-6 actual run 미확인 — 본 SOP § 0 핵심 선언 위반 |
| Hermes PMO 격상 선언 | 4 게이트 (G1b/G2/G3/G4) 통과 후 별도 결정 |
| P2 v3 본문 작성 | Phase 1 acceptance PASS 후 별도 작업 |
| ADR-008 부록 B.6 6단계 *G1b PASS* 갱신 | R-6 actual run 미확인 — § 7.3 단축 합의 후만 가능 |
| 실제 secret 사용 | 본 SOP § 5 R7 ROLLBACK trigger |
| Tier-2 / Tier-3 catalog 확장 | ADR-011 §2.4 + 사용자 명시 R-7 범위 외 |
| CI 자동 정책 변경 허용 | ADR-011 §2.4 T3 절대 금지 |

---

## 8. 후속 작업 매핑

### 8.1 Phase 1 acceptance PASS 후 (P2 v3)

R-7 SOP PASS 판정 + push 후 R-6 actual run PASS → Phase 1 acceptance 통과 → 다음:

- **P2 v3 신규 작성**: `docs/architecture/hermes-adoption-design-v3.md`
  - 입력: P2 v2 §2.1.3 가정 코드 미존재 사실 (Day 1) + R-2 ~ R-7 evidence 흡수
  - 동시 갱신: ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신 PR 묶음
  - 권위: P2 v3 R-7 후 신규 작성 (system-identity-prequel + 풀 합의 결과)
- **Hermes PMO 격상 후보** — 4 게이트 (G1b/G2/G3/G4) 통과 시 사용자 명시 결정으로 격상

### 8.2 G2 / G3 / G4 작성 (병행 가능)

R-7 발행 후 G1b 외 다른 게이트 작성 병행 가능:
- **G2** 6 거버넌스 사전조건 (Provider Liquidity / Skill Memory 등) — 별도 작업
- **G3** "Hermes ≠ root of trust" 운영 구현 — ADR-011 §2.3 운영 함의 5항목의 *실제 구현*
- **G4** Provider-agnostic Memory/Skill 형식 — ADR-009 / ADR-010 적용

R-7 SOP 자체는 G2/G3/G4 미포함 (R-7 = G1b 정식 충족 SOP 한정).

---

## 9. 결과 (Consequences)

### 9.1 긍정적

- ADR-008 부록 B.6 6단계 모두 작성 완료 도달 (R-7 발행으로)
- Phase 1 acceptance 절차의 *체크리스트화* — 운영자가 단일 SOP 따라 판정 가능
- 13 checklist + 9 ROLLBACK 조건 + 7 Evidence 요구 명시로 판정 비용 0
- push 전/후 작업 분리 (§ 7) — G1b PASS 승격 절차 명시
- R-7 자체로는 G1b PASS 선언 안 함 — 사용자 명시 *조건부* 정합 (§ 0 핵심 선언)
- R-6 actual run 결과를 *유일한 G1b PASS 트리거*로 명시 — 로컬 검증의 한계 인정

### 9.2 부정적

- 본 R-7 시점 G1b 는 **CONDITIONALLY PASS** — push + R-6 actual run 까지 G1b 정식 PASS 미달 (의도된 비용)
- R-7 checklist 13 + ROLLBACK 9 + Evidence 7 = 운영자 부담 (의도된 비용)
- GitHub Actions UI 의존 (artifact 30일 retention) — 30일 후 evidence 손실 가능성. § 6.3 보존 기간 후 evidence 보강 권고 (별도 PR)

### 9.3 주의사항

- **본 R-7 SOP 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 답습) — 검증 절차 정의에 한정
- Tier-2 / Tier-3 catalog 본 R-7 미포함
- R-6 actual run 결과가 PASS 외 verdict (PARTIAL/FAIL) 시 본 SOP § 5 ROLLBACK 절차 적용 — Phase 1 acceptance 차단 + ADR-011 §2.4 T3 절차
- R-6 의 GitHub Actions schedule (nightly UTC 18:00) 가 Hermes upstream 변경 / pattern drift 자동 감지의 *재현 가능 evidence 메커니즘* — 본 SOP § 5 R9 와 결합

---

## 10. 관련 문서

### 10.1 상위 권위
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §3 R-7 매핑
- `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B.6 6단계

### 10.2 입력 자료 (R-1 ~ R-6 산출 전체)
- **R-1**: `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL evidence)
- **R-2**: `docs/phase0/day3-r2-sqlite-trigger-poc.md` + `docker/r2-poc/` (baseline 5 patterns)
- **R-3**: `docs/decisions/ADR-011-means-vs-ends-redaction.md` + `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B + `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
- **R-4**: `docs/architecture/redaction-pattern-equivalence.md`
- **R-4.1**: `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/`
- **R-5**: `docs/architecture/canary-recheck-design.md`
- **R-6**: `.github/workflows/r2-canary.yml` (commit `bbcc1af`)

### 10.3 본 R-7 산출
- `docs/phase0/redaction-verification-sop.md` (본 문서)

### 10.4 후속 작업
- Push 후 R-6 GitHub Actions actual run PASS → § 7.3 절차
- P2 v3 신규 작성 (Phase 1 acceptance PASS 후) — `docs/architecture/hermes-adoption-design-v3.md`
- ADR-008 / 009 / 010 / 011 갱신 PR 묶음 (P2 v3 와 동시)

---

**본 SOP 발행 시점**: 2026-05-06
**판정**: **PARTIAL** (G1b CONDITIONALLY PASS — push 전, R-6 actual run 미확인)
**다음 진입점**: 사용자 결정으로 push 진행 → R-6 actual run 확인 → 본 SOP § 7.3 절차 → R-6 actual run PASS 시 G1b PASS 승격 단축 합의 → Phase 1 acceptance PASS 선언 시 P2 v3 진입.
