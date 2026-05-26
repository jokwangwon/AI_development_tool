# G3 Evidence / PASS Gate — Group B 통합 PoC 사양

> **상태**: DRAFT (2026-05-10, Group B 진입 — Hermes-originated marker + Evidence 없는 PASS 차단 통합 PoC)
> **답습 출처**: `docs/architecture/implementation-runtime-roadmap.md` §3.1 (G3 매트릭스 — Hermes-originated commit auto-reject + Evidence 없는 PASS 차단), `docs/architecture/hermes-not-root-of-trust-runtime.md` §2.2 #20, `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.12 (Hermes 변조 차단 매트릭스 4항목), `docs/architecture/governance-preconditions.md` §1.2.6 (P10 Evidence Forgery)
> **PASS 조건 답습**: `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), 사용자 명시 8 PASS / 6 BLOCK / 4 trigger
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance PASS ↔ Implementation/Runtime PASS 분리 매트릭스), P2 v3 §3.1.4 (Implementation Pending 표)
> **답습 시제**: Group A 1차 PoC 산출물 형식 (`docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md`)

---

## 0. 목적

본 PoC 는 G3 *"Hermes ≠ root of trust"* 운영 구현의 첫 시제 — Markdown governance 문서 layer 에서 두 위반을 통합 차단:

1. **Hermes-originated marker 차단** — Hermes 가 governance 승인 주체로 *오해* 되는 marker (`Generated-by: Hermes`, `Agent-Origin: Hermes`, `Authored-by: Hermes`, `Co-Authored-By: Hermes`, `Approved-by: Hermes`, `Signed-off-by: Hermes`) 가 PASS 선언과 *공동 발생* 시 차단
2. **Evidence 없는 PASS 차단** — Gate PASS / Implementation PASS / Design PASS / APPROVE WITH CONDITIONS 등의 governance 표현이 *evidence reference 0건* 으로 선언되는 것 차단. Implementation PASS 선언 시 Design vs Implementation *구분 marker* 의무화 추가

본 PoC 는 *형식적 차단* (Layer 1 답습) 한정. 실 git history / 실 GitHub branch protection / 실 pre-commit hook 활성화는 별도 합의 영역.

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §3.1 + ADR-012 §2.12 + G3 §2.2 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g3-evidence-pass-gate-poc.md` | PoC 사양 + 답습 매핑 + Evidence 5형식 |
| Validator | `tools/evidence_pass_gate.py` | Markdown 문서 양방향 검사 (검사 1 + 검사 2) |
| FAIL fixture × 4 | `tests/fixtures/evidence_pass_gate/fail/{hermes_marker, evidence_less_pass, agent_origin_marker, unscoped_implementation_pass}.md` | 3 패턴 cover |
| PASS fixture × 2 | `tests/fixtures/evidence_pass_gate/pass/{reviewer_approved_pass, design_pass_implementation_pending}.md` | Reviewer 합의 + Design 분리 |
| CI workflow | `.github/workflows/evidence-pass-gate.yml` | PASS/FAIL 양방향 + 패턴 회귀 검증 |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g3-evidence-pass-gate-reviewer-only.md` | PoC 검토 + escalation 0/4 |

### 1.2 제외 (별도 합의 영역)

| 항목 | 분리 이유 |
|------|----------|
| 실 git pre-commit hook 활성화 | 사용자 명시 답습 — 본 PoC 는 script 작성만 |
| 실 GitHub branch protection rule 변경 | 사용자 명시 답습 — 정책 변경은 별도 합의 |
| 실 git log commit author 검사 | 사용자 명시 (Marker 영역 = Markdown 한정) |
| 실 commit signing / CODEOWNERS 강제 | T2/T3 정책 변경 영역 — ADR-011 §2.4 답습 별도 합의 |
| Skill `forbidden_actions` 강제 (G3 §3.3) | Group G 영역 — implementation-runtime-roadmap.md §3 답습 |

---

## 2. 차단 패턴 catalog

### 2.1 검사 1 — Hermes-originated marker (frontmatter / trailer / 본문)

```
Generated-by: Hermes
Agent-Origin: Hermes
Authored-by: Hermes
Co-Authored-By: Hermes
Approved-by: Hermes
Signed-off-by: Hermes
```

**조건부 발화**: 같은 문서에 governance PASS 표현이 동시 존재 시에만 fire (ambient noise 회피).

### 2.2 검사 2 — Evidence 없는 PASS 차단

PASS 선언 표현 anchor:

```
Gate PASS
Implementation PASS
Implementation/Runtime PASS
Design PASS
Design/Governance PASS
APPROVE WITH CONDITIONS
## APPROVE
G[1-9]\w* PASS  (e.g., G1b PASS, G3 PASS)
GP-N PASS  (e.g., GP-5 PASS)
```

Evidence reference 최소 1건 의무 — 다음 중 하나:

```
docs/review/...md
docs/evidence/...{jsonl,md}
docs/phase0/...md
actions/runs/<id> (≥6 digits)
commit SHA (7+ hex)
^event: <name>$ (line-anchored)
```

### 2.3 검사 2 추가 — Implementation PASS scope 의무

`Implementation PASS` 또는 `Implementation/Runtime PASS` 선언 시 다음 중 하나의 분리 marker 의무:

```
Implementation Pending
Design/Governance PASS
DESIGN PASS / IMPLEMENTATION PENDING
```

답습: ADR-008 부록 C §C.5 (분리 매트릭스), P2 v3 §3.1.4

---

## 3. Validator 책무 분담

| 검사 | 입력 | 출력 패턴 |
|------|------|---------|
| 검사 1 | Hermes marker × governance PASS 공동 발생 | `hermes-originated-marker` |
| 검사 2 | governance PASS × evidence 0건 | `pass-without-evidence` |
| 검사 2 추가 | Implementation PASS × Design 분리 0건 | `implementation-pass-unscoped` |

**책무 분담 매트릭스**:

| 위반 | 검사 1 | 검사 2 | 검사 2 추가 |
|------|------|------|------|
| Hermes marker + PASS + evidence | ✅ fires | (skipped) | (skipped) |
| PASS + evidence 0 | (skipped) | ✅ fires | (검사 2 추가는 Impl PASS 시) |
| Impl PASS + evidence + Design split | (skipped) | (skipped) | (skipped — 정상) |
| Impl PASS + evidence + Design split 0 | (skipped) | (skipped) | ✅ fires |
| Hermes marker + PASS + evidence 0 | ✅ fires | ✅ fires | (Impl PASS 시 추가) |

---

## 4. Fixture matrix

### 4.1 FAIL × 4

| # | fixture | 검출 패턴 |
|---|--------|---------|
| F1 | `fail/hermes_marker.md` | `hermes-originated-marker` (Generated-by) |
| F2 | `fail/evidence_less_pass.md` | `pass-without-evidence` |
| F3 | `fail/agent_origin_marker.md` | `hermes-originated-marker` (Agent-Origin) |
| F4 | `fail/unscoped_implementation_pass.md` | `implementation-pass-unscoped` |

### 4.2 PASS × 2

| # | fixture | 정합 |
|---|--------|------|
| P1 | `pass/reviewer_approved_pass.md` | Reviewer 합의 + 3 evidence reference (review / ledger / event:) |
| P2 | `pass/design_pass_implementation_pending.md` | Design/Governance PASS + Implementation Pending 분리 + 3 evidence reference |

---

## 5. CI workflow

`.github/workflows/evidence-pass-gate.yml` — Group A 1차/2차 답습:

- step 1: PASS fixture rc=0 검증 (false positive 차단)
- step 2: FAIL fixture rc=1 검증 + ≥4건 + 3 패턴 cover 모두 회귀 검사
- step 3: Evidence summary (commit / ref / run_id / event / agent / ledger_layer)
- `permissions: contents: read` (R-6 답습)

---

## 6. 양방향 검증 결과 (로컬, 2026-05-10)

| 검증 | 명령 | rc | 결과 |
|------|------|-----|------|
| PASS fixture | `python3 tools/evidence_pass_gate.py tests/fixtures/evidence_pass_gate/pass/` | 0 | 위반 0건 ✅ |
| FAIL fixture | `python3 tools/evidence_pass_gate.py tests/fixtures/evidence_pass_gate/fail/` | 1 | 4건 위반 (3 패턴 cover) ✅ |
| 패턴 회귀 cover | `grep -c hermes-originated-marker / pass-without-evidence / implementation-pass-unscoped` | 2/1/1 | 3/3 패턴 모두 출현 ✅ |

검출 raw output:

```
unscoped_implementation_pass.md:3:implementation-pass-unscoped:Implementation PASS (no Design/Implementation split marker)
hermes_marker.md:4:hermes-originated-marker:Generated-by: Hermes (with PASS declaration in same file)
agent_origin_marker.md:4:hermes-originated-marker:Agent-Origin: Hermes (with PASS declaration in same file)
evidence_less_pass.md:3:pass-without-evidence:Gate PASS (no evidence reference found)
```

---

## 7. PASS / BLOCK 기준

### 7.1 PASS 기준 (사용자 명시 8건 답습)

1. ✅ Hermes-originated governance commit / 승인 marker 탐지 (검사 1)
2. ✅ Evidence 없는 PASS 선언 탐지 (검사 2)
3. ✅ 정상 Reviewer-approved PASS 문서 통과 (P1 fixture)
4. ✅ Design/Governance PASS 와 Implementation/Runtime PASS 구분 (P2 fixture)
5. ✅ CI 실패 신호 명확 (`rc=1` + `::error::` annotation)
6. ✅ 로컬 명령 재현 가능 (`python3 tools/evidence_pass_gate.py <target>`)
7. ✅ Evidence 문서 = 본 사양 §6 + Reviewer-only 합의 §1
8. ✅ Reviewer-only 단축 합의 APPROVE / APPROVE WITH CONDITIONS

### 7.2 BLOCK 기준 (사용자 명시 6건 답습)

1. ❌ Evidence 없는 PASS 놓침 → §6 검증 fail
2. ❌ Hermes-originated approval 놓침 → §6 검증 fail
3. ❌ 정상 합의 보고서 과도 차단 (FP) → P1/P2 fixture rc≠0
4. ❌ Implementation PASS / Design PASS 구분 부재 → 검사 2 추가 미발화
5. ❌ CI 실패 신호 불명확 → rc / `::error::` 부재
6. ❌ Evidence 없이 PASS 선언 → 본 PoC 자기 적용 (본 사양 §6 + Reviewer 합의 §1 evidence)

### 7.3 ADR-011 §2.1 (a)~(e) 5조건 답습

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 안전 결과 본질 식별 | ✅ | 본 사양 §0 — Hermes ≠ root of trust 운영 layer 1 차단 결과 |
| (b) 수단 변경 사전 인지 | ✅ | §11 풀 3+1 승격 trigger 4건 등록 |
| (c) 안전 결과 보존 검증 | ✅ | §6 양방향 검증 4/4 PASS + 3 패턴 cover |
| (d) 폐기 경로 | ✅ | `tools/evidence_pass_gate.py` 1 파일 + `.github/workflows/...` 1 파일 + fixture 6건 단순 제거 |
| (e) 외부 검증 가능성 | ✅ | CI log + validator stdout + commit SHA + Evidence Ledger 형식 |

---

## 8. 답습 매핑

| 권위 | 답습 항목 |
|------|---------|
| `implementation-runtime-roadmap.md` §3.1 | Group B = G3 Hermes-originated commit auto-reject + Evidence 없는 PASS 차단, 합의 형태 = 단축 합의 (Reviewer-only) |
| `hermes-not-root-of-trust-runtime.md` §2.2 #20 | Hermes-originated commit 차단 권한 |
| `ADR-012` §2.12 | Hermes 변조 차단 매트릭스 4항목 (#3 = commit auto-reject) |
| `governance-preconditions.md` §1.2.6 (P10) | Evidence Forgery 위반 경로 |
| `ADR-008` 부록 C §C.5 | Design/Governance PASS ↔ Implementation/Runtime PASS 분리 매트릭스 |
| `P2 v3` §3.1.4 | Implementation Pending 표 답습 |
| `ADR-011` §2.1 (a)~(e) | 수단 변경 5조건 |
| Group A 1차 PoC (`g2-gp5-provider-adapter-enforcement-poc.md`) | 산출물 형식 / fixture 구조 / CI workflow 답습 |

---

## 9. Evidence 5형식

| Evidence | 형식 |
|----------|------|
| Markdown report | 본 사양 + Reviewer-only 합의 보고서 |
| JSONL ledger entry | `event: evidence_pass_gate_layer1` (CI summary) |
| 명령 결과 | §6 양방향 검증 raw output |
| Git commit | 본 PoC commit (validator / fixture / CI / 사양·합의 분리) |
| GitHub Actions run | `actions/runs/<id>` (push 후) |

---

## 10. *제외* (사용자 명시 답습)

- ❌ G3 Implementation/Runtime PASS 최종 선언
- ❌ G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 GitHub branch protection 변경
- ❌ 실 GitHub 권한 정책 변경
- ❌ runtime application code 구현
- ❌ ADR 본문 자동 갱신
- ❌ 실 git pre-commit hook 활성화 (script 작성만)

---

## 11. 풀 3+1 승격 trigger (사용자 명시 4건)

| Trigger | 발화 시 |
|---------|--------|
| TR-B-1 | commit auto-reject 정책이 human review 의무 수준 변경 |
| TR-B-2 | Evidence 차단 기준이 ADR-011 / ADR-012 원칙과 충돌 |
| TR-B-3 | 정상 문서 작성 흐름 과도 차단 (FP 발생) |
| TR-B-4 | Hermes PMO 격상 절차로 오해 가능성 |

본 PoC 본문 작성 시점 = 4 trigger 0/4 발화 → Reviewer-only 단축 합의 적격.

---

## 12. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group B 진입, Reviewer-only 단축 합의 진행 중 |
