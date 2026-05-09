# 3+1 합의 보고서 — G3 Evidence / PASS Gate (Group B 통합 PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group B 진입 — Hermes-originated marker + Evidence 없는 PASS 차단 통합 PoC)
> **합의 형식**: **Reviewer-only 단축** (escalation triggers TR-B-1~TR-B-4 0/4 발화 → 단축 적격)
> **검토 대상**: `tools/evidence_pass_gate.py`, `tests/fixtures/evidence_pass_gate/{pass,fail}/`, `.github/workflows/evidence-pass-gate.yml`, `docs/phase0/g3-evidence-pass-gate-poc.md`
> **상위 권위**: ADR-008 부록 C, ADR-011 §2.1 (a)~(e), ADR-012 §2.12, G3 §2.2 #20, governance-preconditions.md §1.2.6 (P10), implementation-runtime-roadmap.md §3.1
> **답습 시제**: Group A 1차 PoC 합의 (`docs/review/3plus1-consensus-2026-05-09-g2-gp5-poc-poc1-reviewer-only.md`)

---

## 1. 검토 사항

### 1.1 산출물 6건

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/evidence_pass_gate.py` | ~165 | Group A `provider_import_scanner.py` 패턴 (argparse + dataclass + iter + line-anchored regex) |
| 2 | `tests/fixtures/evidence_pass_gate/fail/{hermes_marker, evidence_less_pass, agent_origin_marker, unscoped_implementation_pass}.md` | ~5/each | Group A 1차 fixture 형식 답습 (최소 단위) |
| 3 | `tests/fixtures/evidence_pass_gate/pass/{reviewer_approved_pass, design_pass_implementation_pending}.md` | ~12/each | 정상 합의 보고서 + Design/Implementation 분리 형식 |
| 4 | `.github/workflows/evidence-pass-gate.yml` | ~85 | Group A `provider-adapter-enforcement.yml` 1차 step 답습 + 패턴 회귀 cover step 추가 |
| 5 | `docs/phase0/g3-evidence-pass-gate-poc.md` | ~210 | Group A 1차 PoC 사양 문서 형식 직접 답습 |
| 6 | 본 합의 보고서 | ~200 | Group A 1차/2차 Reviewer-only 합의 형식 답습 |

### 1.2 로컬 양방향 검증 결과 (4/4 PASS)

| 검증 | 명령 | rc | 결과 |
|------|------|-----|------|
| PASS fixture | `python3 tools/evidence_pass_gate.py tests/fixtures/evidence_pass_gate/pass/` | 0 | 위반 0건 ✅ (P1 + P2 모두 통과) |
| FAIL fixture | `python3 tools/evidence_pass_gate.py tests/fixtures/evidence_pass_gate/fail/` | 1 | 4건 위반 ✅ |
| 패턴 cover (hermes-originated-marker) | `grep -c` | — | 2 occurrence (F1 Generated-by + F3 Agent-Origin) ✅ |
| 패턴 cover (pass-without-evidence) | `grep -c` | — | 1 occurrence (F2) ✅ |
| 패턴 cover (implementation-pass-unscoped) | `grep -c` | — | 1 occurrence (F4) ✅ |

검출 raw output:

```
unscoped_implementation_pass.md:3:implementation-pass-unscoped:Implementation PASS (no Design/Implementation split marker)
hermes_marker.md:4:hermes-originated-marker:[Hermes marker] (with PASS declaration in same file)
agent_origin_marker.md:4:hermes-originated-marker:[Hermes marker] (with PASS declaration in same file)
evidence_less_pass.md:3:pass-without-evidence:Gate PASS (no evidence reference found)
```

(*marker 값 본 합의 보고서 자체 hermes-originated-marker 검출 회피 위해 카테고리 표기로 redact — 원시 raw 는 PoC 사양 §6 답습.*)

---

## 2. 검토 항목 — Reviewer 관점 8 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 안전 결과 본질 식별 | ✅ | PoC 사양 §0 — Hermes ≠ root of trust 운영 layer 1 차단 결과 |
| (b) 수단 변경 사전 인지 | ✅ | TR-B-1~TR-B-4 4 trigger 등록 (PoC 사양 §11) |
| (c) 안전 결과 보존 검증 | ✅ | §1.2 양방향 검증 4/4 PASS + 3 패턴 cover |
| (d) 폐기 경로 | ✅ | validator 1 파일 + workflow 1 파일 + fixture 6건 단순 제거 |
| (e) 외부 검증 가능성 | ✅ | CI log + validator stdout + commit SHA + Evidence Ledger entry 형식 (`event: evidence_pass_gate_layer1`) |

### 2.2 사용자 명시 8 PASS 기준 답습

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | Hermes-originated marker 탐지 | ✅ | F1 / F3 fixture rc=1 + `hermes-originated-marker` 출력 |
| 2 | Evidence 없는 PASS 탐지 | ✅ | F2 fixture rc=1 + `pass-without-evidence` 출력 |
| 3 | 정상 Reviewer-approved PASS 통과 | ✅ | P1 fixture rc=0 |
| 4 | Design / Implementation 구분 | ✅ | F4 fixture (없음) rc=1 / P2 fixture (Design 분리) rc=0 |
| 5 | CI 실패 신호 명확 | ✅ | `rc=1` + `::error::` annotation + 명시 메시지 |
| 6 | 로컬 명령 재현 가능 | ✅ | `python3 tools/evidence_pass_gate.py <target>` |
| 7 | Evidence 문서 기록 | ✅ | PoC 사양 §6 + 본 합의 §1.2 |
| 8 | Reviewer-only 합의 APPROVE | ✅ | 본 보고서 §6 결론 답습 |

### 2.3 사용자 명시 6 BLOCK 기준 답습 (자기 검증)

| # | BLOCK 기준 | 자기 검증 |
|---|----------|---------|
| 1 | Evidence 없는 PASS 놓침 | ✅ F2 fixture 양방향 검증 통과 |
| 2 | Hermes-originated approval 놓침 | ✅ F1 + F3 fixture 양방향 검증 통과 |
| 3 | 정상 합의 보고서 과도 차단 (FP) | ✅ P1 + P2 fixture rc=0 (FP 0건) |
| 4 | Implementation PASS / Design PASS 구분 부재 | ✅ F4 fixture (없음) FAIL / P2 (분리) PASS |
| 5 | CI 실패 신호 불명확 | ✅ `::error::` + `rc=1` 명시 메시지 |
| 6 | Evidence 없이 PASS 선언 | ✅ 본 PoC 자기 적용 — PoC 사양 §6 + 본 합의 §1.2 evidence 첨부 |

### 2.4 사용자 명시 7 금지 항목 0/7 위반

| # | 금지 항목 | 위반 |
|---|---------|----|
| 1 | G3 Implementation/Runtime PASS 최종 선언 | 0 (본 PoC = 부분 시제) |
| 2 | G2/G3/G4 전체 Implementation/Runtime PASS 선언 | 0 |
| 3 | Hermes PMO 격상 선언 | 0 |
| 4 | 실 GitHub branch protection 변경 | 0 (workflow 만, branch protection 미변경) |
| 5 | 실 GitHub 권한 정책 변경 | 0 |
| 6 | runtime application code 구현 | 0 (validator = 검증 도구, runtime 코드 0줄) |
| 7 | ADR 본문 자동 갱신 | 0 (본 PoC 본문 변경 0건) |

### 2.5 Group A 답습 충실도

| 영역 | Group A 1차 | Group B 본 PoC | 답습 충실 |
|------|----------|---------|---------|
| 산출물 형식 | tools/scanner.py + fixture pass×1+fail×5 + workflow + 사양 + 합의 | tools/validator.py + fixture pass×2+fail×4 + workflow + 사양 + 합의 | ✅ 직접 답습 |
| Validator 구조 | argparse + dataclass(frozen) + iter + Visitor / regex | argparse + dataclass(frozen) + iter + line-anchored regex | ✅ 답습 |
| CI workflow | PASS step + FAIL step + Evidence summary | PASS step + FAIL step + 패턴 cover step + Evidence summary | ✅ 답습 + 패턴 cover 신규 추가 |
| 합의 형식 | Reviewer-only 단축 | Reviewer-only 단축 | ✅ 답습 |
| Permissions | `contents: read` | `contents: read` | ✅ R-6 답습 |

### 2.6 책무 분담 매트릭스 (PoC 사양 §3 답습)

본 PoC 는 *2 항목 1 도구 통합* — 검사 1 (Hermes marker × governance 공동) + 검사 2 (PASS × evidence) + 검사 2 추가 (Impl PASS × Design 분리). 매트릭스 공동 발생 처리는 PoC 사양 §3 답습.

### 2.7 책무 분리 — *별도 합의 영역* 명시

| 영역 | 분리 사유 |
|------|---------|
| 실 git pre-commit hook 활성화 | 사용자 명시 — script 작성만 |
| 실 GitHub branch protection rule | 정책 변경 = T2/T3 영역 (ADR-011 §2.4) — 별도 합의 |
| 실 git log commit author 검사 | 사용자 명시 — Marker 영역 = Markdown 한정 |
| Skill `forbidden_actions` 강제 | Group G 영역 (implementation-runtime-roadmap §3.1) |
| commit signing / CODEOWNERS | T2/T3 정책 — 별도 합의 |

### 2.8 *알려진 한계* 명시

1. **Markdown code block 내부 미회피** — validator 는 ``` 코드블록 안 marker 도 검출 (line-anchored regex 한정). 본 PoC 사양 문서 자체가 marker 패턴 catalog 를 본문에 포함 → CI workflow 는 *fixtures 디렉터리 한정* 으로 회피.
2. **실 git history 외부** — fixture 시뮬레이션 한정. 실 commit author / committer / trailer 검사는 별도 합의.
3. **ambiguity** — `PASS` 단독 단어는 anchor 패턴 미포함 (FP 회피) — 명시 표현 (Gate PASS / Implementation PASS / APPROVE WITH CONDITIONS / G[1-9] PASS / GP-N PASS) 한정.
4. **evidence reference catalog 6종 한정** — JSONL / GitHub Actions / commit SHA / docs/review / docs/evidence / docs/phase0 / `event:` line-anchored. 다른 형태 (Linear / Jira / 외부 URL) 미답습 — 추가 시 별도 합의.

---

## 3. 풀 3+1 승격 trigger 0/4 발화 (사용자 명시)

| Trigger | 발화 여부 | 근거 |
|---------|--------|------|
| TR-B-1 commit auto-reject 정책이 human review 의무 수준 변경 | 0 | 본 PoC = Markdown layer 형식 차단 한정, human review 정책 미변경 |
| TR-B-2 Evidence 차단 기준이 ADR-011 / ADR-012 원칙과 충돌 | 0 | ADR-012 §2.12 + ADR-011 §2.1 (a)~(e) 5/5 정합 |
| TR-B-3 정상 문서 작성 흐름 과도 차단 (FP) | 0 | P1 + P2 fixture rc=0 (FP 0건) |
| TR-B-4 Hermes PMO 격상 절차로 오해 가능성 | 0 | 본 PoC §2.4 #3 명시 (격상 선언 0건) + §1 부분 시제 한정 |

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ Markdown governance 문서 layer 형식 차단 (Hermes marker × governance 공동) 첫 시제
- ✅ Markdown governance 문서 layer 형식 차단 (PASS × evidence) 첫 시제
- ✅ Implementation PASS scope 분리 의무 첫 시제
- ✅ G3 §2.2 #20 + ADR-012 §2.12 #3 *형식적* 답습
- ✅ Reviewer-only 단축 합의 답습 (Group A 답습)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G3 Implementation/Runtime PASS 최종 선언
- ❌ G2/G3/G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 GitHub branch protection 변경 / 실 git pre-commit hook 활성화
- ❌ 실 commit author / committer / trailer 검사
- ❌ Skill `forbidden_actions` 강제
- ❌ runtime application code 구현
- ❌ ADR 본문 자동 갱신

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group B 통합 PoC = G2 GP-5 1차 PoC 시제 답습 충실 (Reviewer 관점 8 영역 모두 충족, 4 trigger 0/4 발화, 7 금지 0/7 위반, ADR-011 §2.1 5/5 충족, FP 0건).

### 5.2 추가 조건 (C-B-1 ~ C-B-4)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-B-1 | 본 PoC = G3 *부분 충족 시제* 한정 — G3 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | PoC 사양 §0 + §10 명시, 본 합의 §2.4 #1 |
| C-B-2 | Implementation/Runtime PASS 자동 선언 미발생 | 본 합의 §4.2 명시 |
| C-B-3 | Markdown 한정 — 실 git history / 실 hook 활성화 / 실 branch protection 변경은 *별도 합의 영역* | PoC 사양 §1.2 + 본 합의 §2.7 명시 |
| C-B-4 | code block / inline code 외부 회피 미답습 — *알려진 한계* (본 합의 §2.8 #1) — CI 는 fixtures 한정으로 회피, 추후 확장 시 별도 합의 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (validator+CI / fixture / 사양·합의)
2. push (사용자 confirm 후)
3. GitHub Actions actual run 검증 (R-6 답습 — Group A 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습)
5. **다음 진입점 (사용자 결정 영역)**: Group C (G4 JSONL hash chain + JCS canonical + round-trip PoC) 또는 Group D (G2 GP-3 + GP-2 secret/redaction) 또는 Group A 3차 (URL/endpoint grep PoC, C-8 답습)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group B 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, escalation 0/4 |
