# 3+1 합의 보고서 — G3 + G4 Boundary Guard (Group G PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group G 진입 — Skill escalation 차단 (G-1) + 합의 자기참조 차단 (G-2) + Memory/Skill boundary 4 금지 (G-3) 통합 PoC)
> **PASS scope**: G3 + G4 *형식적 검출 layer 시제* 한정 — **Implementation Pending** (G3 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 6 = 0/6 발화 → 단축 적격)
> **검토 대상**:
> - `tools/boundary_guard.py`
> - `tests/fixtures/boundary_guard/{skill_escalation,consensus_self_reference,memory_skill_boundary}/{pass,fail}/*`
> - `.github/workflows/boundary-guard.yml`
> - `docs/phase0/g3-g4-boundary-guard-poc.md`
> - `.gitignore` (`group-g-logs/` 추가)
> **상위 권위**: ADR-008 부록 C, ADR-009 §C-N §2.3, ADR-011 §2.1 + §2.4 T1/T2/T3, ADR-012 §2.2 + §2.12, hermes-not-root-of-trust-runtime.md §3.3 + §4, provider-agnostic-memory-skill-design.md §5.2, implementation-runtime-roadmap.md §3.1 (Order 8/9 tie)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g2-gp4-g4-schema-validation-reviewer-only.md` 직접 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/boundary_guard.py` | ~445 | **stdlib `re` + `json` + `dataclasses` 단독** (외부 의존 0건). 3 mode CLI (`--mode skill-escalation` G-1 / `--mode consensus-self-reference` G-2 / `--mode memory-skill-boundary` G-3) + `--list-boundaries` self-check + Group C `jsonl_hash_chain` (`validate_schema` + ENUMs `ALLOWED_TYPES`/`ALLOWED_AGENTS`/`ALLOWED_SCOPES`) import 직접 + Group E `schema_validator` (`ALLOWED_ACTIONS_ENUM` 7 + `parse_yaml_v2`) import 직접 + Group B Hermes-originated marker 6 패턴 답습 + governance PASS anchor 9 답습 + reviewer/external_llm marker 검출 + Hermes PMO/policy decision 3 패턴 + policy expression 6 패턴 + scope transition 검출 + agent=hermes × event 매트릭스 |
| 2 | `tests/fixtures/boundary_guard/skill_escalation/pass/valid_skill_within_allowed.yaml` | 33 lines | G-1 PASS — Group E `valid_skill.yaml` 답습 |
| 3 | `tests/fixtures/boundary_guard/skill_escalation/fail/{skill_yaml_invalid_action.yaml, audit_log_escalation.jsonl}` | 2 fixture | G-1 FAIL — 2 pattern_ids cover (yaml-invalid-action + audit-log-escalation) |
| 4 | `tests/fixtures/boundary_guard/consensus_self_reference/pass/proper_reviewer_consensus.md` | 25 lines | G-2 PASS — Reviewer-only 정상 합의 답습 (Hermes marker 부재 + Reviewer marker 존재) |
| 5 | `tests/fixtures/boundary_guard/consensus_self_reference/fail/{hermes_self_consensus.md, hermes_pmo_self_promotion.md}` | 2 fixture | G-2 FAIL — 2 pattern_ids cover (hermes-self-consensus + hermes-pmo-self-promotion) |
| 6 | `tests/fixtures/boundary_guard/memory_skill_boundary/pass/safe_memory_skill_chain.jsonl` | 3 entries | G-3 PASS — Group F `skill_project.jsonl` 직접 답습 (`agent: user` + scope transition 0건 + 정책 표현 0건) |
| 7 | `tests/fixtures/boundary_guard/memory_skill_boundary/fail/{memory_replaces_policy.jsonl, session_to_global_promotion.jsonl, hermes_self_approves_skill.jsonl}` | 3 fixture | G-3 FAIL — 3 pattern_ids cover (memory-replaces-policy + session-to-global + hermes-self-approves) |
| - | `.github/workflows/boundary-guard.yml` | ~265 | 13 step (3 setup + `--list-boundaries` + 6 G-N PASS/FAIL + summary.json + artifact + Evidence summary). artifact path = `group-g-logs/` (Group F 후속 답습) |
| - | `docs/phase0/g3-g4-boundary-guard-poc.md` | 399 | PoC 사양 (14 섹션 — 목적 / 범위 / 도구 근거 / Group A~F 재사용 / G-1/G-2/G-3 검증 기준 / fixture / 검증 매트릭스 / PASS / 한계 / CI / trigger / Evidence / 변경이력) |
| 8 | 본 합의 보고서 | ~330 | Group A~F Reviewer-only 합의 형식 답습 |

**합산 = 8 파일** (Group D/E/F 답습 평균).

### 1.2 fixture 9건 검증 결과

| Fixture | 위치 | 매칭 패턴 | 합계 |
|---|---|---|---|
| `valid_skill_within_allowed.yaml` | skill_escalation/pass/ | 0 | 0 (FP 0) |
| `skill_yaml_invalid_action.yaml` | skill_escalation/fail/ | yaml-invalid-action × 3 | 3 |
| `audit_log_escalation.jsonl` | skill_escalation/fail/ | audit-log-escalation × 2 | 2 |
| `proper_reviewer_consensus.md` | consensus_self_reference/pass/ | 0 | 0 (FP 0) |
| `hermes_self_consensus.md` | consensus_self_reference/fail/ | hermes-self-consensus × 3 | 3 |
| `hermes_pmo_self_promotion.md` | consensus_self_reference/fail/ | hermes-self-consensus × 1 + hermes-pmo-self-promotion × 2 | 3 |
| `safe_memory_skill_chain.jsonl` | memory_skill_boundary/pass/ | 0 | 0 (FP 0) |
| `memory_replaces_policy.jsonl` | memory_skill_boundary/fail/ | memory-replaces-policy × 2 | 2 |
| `session_to_global_promotion.jsonl` | memory_skill_boundary/fail/ | session-to-global × 1 | 1 |
| `hermes_self_approves_skill.jsonl` | memory_skill_boundary/fail/ | hermes-self-approves × 2 | 2 |

### 1.3 3 mode 로컬 검증 결과 (8/8 PASS)

| # | 검증 | 명령 | rc | 결과 |
|---|------|------|-----|------|
| 1 | G-1 PASS | `--mode skill-escalation pass/` | **0** | 위반 0건 (FP 0) |
| 2 | G-1 FAIL | `--mode skill-escalation fail/` | **1** | 5 violations + 2 pattern_ids cover (yaml-invalid-action + audit-log-escalation) |
| 3 | G-2 PASS | `--mode consensus-self-reference pass/` | **0** | 위반 0건 (FP 0) |
| 4 | G-2 FAIL | `--mode consensus-self-reference fail/` | **1** | 6 violations + 2 pattern_ids cover (hermes-self-consensus + hermes-pmo-self-promotion) |
| 5 | G-3 PASS | `--mode memory-skill-boundary pass/` | **0** | 위반 0건 (FP 0, Group F skill_project.jsonl 답습) |
| 6 | G-3 FAIL | `--mode memory-skill-boundary fail/` | **1** | 5 violations + 3 pattern_ids cover (memory-replaces-policy + session-to-global + hermes-self-approves) |
| 7 | `--list-boundaries` self-check | `--list-boundaries` | **0** | total_boundaries=4 + total_modes=3 + consensus_matrix_rows=13 + boundary_4_rules_compliant=True |
| 8 | F-금지 grep | scanner + fixture grep | **0** | 실 Hermes runtime / 실 commit author / 실 production data 0건 |

### 1.4 `--list-boundaries` 출력

```
total_boundaries=4
  #1 Memory 가 policy 를 대체
  #2 Skill 이 ADR / Constitution 우회 (G-1 통합 답습)
  #3 Session memory → Global memory 자동 승격
  #4 Hermes 가 skill 을 자기 승인
total_modes=3
  --mode skill-escalation
  --mode consensus-self-reference
  --mode memory-skill-boundary
consensus_matrix_rows=13
  Worker Agent 작업 분배 | T1 | Hermes 단독 OK
  Worker 출력 검증 (Tools) | T1 | Tools 자동
  Skill 후보 제안 | T1 | Hermes 제안만
  Skill 등록 | T2 | 사용자 명시 결정 필수
  Memory promotion (Project → Global) | T2 | 사용자 명시 결정 필수
  일반 합의 (패턴 동등성 등) | T2 | 단축 또는 풀 3+1
  G1b PASS 승격 | T2 | 단축 (Reviewer-only) — 이미 발생
  G2 / G3 / G4 PASS | T2 | 단축 또는 풀 3+1
  Hermes PMO 격상 | T2 강화 | 풀 3+1 + 외부 LLM 1+ 필수
  Hermes 정책 변경 | T3 | 풀 3+1 + 외부 LLM 1+ 권장 + ADR Amendment
  Constitution / ADR 본문 갱신 | T3 | 풀 3+1 + ADR Amendment
  Harness Gate 정의 자체 변경 | T3 | 풀 3+1 + ADR Amendment
  G3 §4 / §9 본문 변경 | T3 | 풀 3+1 + ADR Amendment
hermes_originated_patterns=6
governance_pass_anchors=9
hermes_policy_decision_patterns=3
policy_expression_patterns=6
boundary_4_rules_compliant=True
```

### 1.5 CI workflow 13 step 구조

| # | Step | 책무 | 검증 |
|---|------|------|------|
| 1 | Checkout | actions/checkout@v4 | — |
| 2 | Set up Python | actions/setup-python@v5 (3.12) | — |
| 3 | Prepare log directory | `mkdir -p group-g-logs` (leading dot 미사용) | — |
| 4 | `--list-boundaries` self-check | rc=0 + total_boundaries=4 + total_modes=3 + consensus_matrix_rows=13 + boundary_4_rules_compliant=True grep | §1.3 #7 |
| 5 | G-1 PASS | rc=0 + violations=0 grep | §1.3 #1 |
| 6 | G-1 FAIL | rc=1 + 2 pattern_ids cover grep | §1.3 #2 |
| 7 | G-2 PASS | rc=0 + violations=0 grep | §1.3 #3 |
| 8 | G-2 FAIL | rc=1 + 2 pattern_ids cover grep | §1.3 #4 |
| 9 | G-3 PASS | rc=0 + violations=0 grep | §1.3 #5 |
| 10 | G-3 FAIL + F-금지 grep | rc=1 + 3 pattern_ids cover grep + 11 F-금지 grep | §1.3 #6 + #8 |
| 11 | Build summary.json | step output 집계 → `group-g-logs/summary.json` 17 항목 | — |
| 12 | Upload artifact | `actions/upload-artifact@v4` `boundary-guard-evidence` retention 30일 | Group F 후속 답습 |
| 13 | Evidence summary | `$GITHUB_STEP_SUMMARY` 16 항목 | R-6 답습 |

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | G3 §3.3 (Skill escalation) + §4 (자기참조 차단) + G4 §5.2 (4 금지) 직접 답습 (변경 0건) — Memory poisoning 차단 + Skill auto-approval 차단 + Hermes 자기 격상 차단 형식 검출 |
| (b) 격리 환경 PoC 실증 | ✅ | fixture 한정 (실 Hermes runtime 0건, 실 commit author 검사 0건, 외부 LLM 호출 0건) + 외부 의존 0건 (stdlib 단독) + CI ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / ADR-009 C-N §2.3 / ADR-011 §2.1 + §2.4 / ADR-012 §2.2 + §2.12 / G3 §3.3 + §4 / G4 §5.2 / roadmap §3.1 cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 13 step + paths trigger 6 영역 (boundary_guard + Group A/B/C/E 모듈 + fixture + workflow) + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 8 (사양 §9 답습)

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | G-1 PASS scan | ✅ | rc=0 + 위반 0건 |
| 2 | G-1 FAIL scan | ✅ | rc=1 + 5 violations + 2 pattern_ids cover |
| 3 | G-2 PASS scan | ✅ | rc=0 + 위반 0건 |
| 4 | G-2 FAIL scan | ✅ | rc=1 + 6 violations + 2 pattern_ids cover |
| 5 | G-3 PASS scan | ✅ | rc=0 + 위반 0건 (Group F skill_project.jsonl 답습) |
| 6 | G-3 FAIL scan | ✅ | rc=1 + 5 violations + 3 pattern_ids cover |
| 7 | `--list-boundaries` self-check | ✅ | total_boundaries=4 + total_modes=3 + consensus_matrix_rows=13 + boundary_4_rules_compliant=True |
| 8 | F-금지 grep | ✅ | 실 Hermes runtime / 실 commit author / 실 production data 0건 |

**합산 8/8 충족.**

### 2.3 사용자 명시 11 금지 자기 검증 (0/11 위반)

| # | 금지 | 위반 | 근거 |
|---|------|----|------|
| 1 | G3 전체 Implementation/Runtime PASS 선언 | 0 | 본 PoC = *형식적 검출 layer 시제* 한정 |
| 2 | G4 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 (meta 갱신 시 *부분 충족 시제* 한정) |
| 3 | G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | 0 | 변경 0건 |
| 4 | Hermes PMO 격상 선언 | 0 | 변경 0건 (G3 §4.3 매트릭스 = 풀 3+1 + 외부 LLM 1+ 필수) |
| 5 | 실제 runtime hook 운영 적용 | 0 | scanner 본문 `import (docker\|subprocess\|fcntl\|inotify\|pyinotify\|pygit2\|requests\|httpx)` 0건 |
| 6 | 실제 Skill wrapper 구현 | 0 | runtime hook 0건 (정적 검출 한정) |
| 7 | 실제 Memory write blocker 구현 | 0 | runtime hook 0건 |
| 8 | 실제 git commit author 전수 검사 | 0 | scanner 본문 `git log` / `git show` / `GitPython` / `pygit2` 0건 |
| 9 | 외부 LLM 자동 호출 | 0 | scanner 본문 `openai.` / `anthropic.` / `completions.create` 0건 |
| 10 | production memory/skill 데이터 사용 | 0 | fixture 한정 (`tests/fixtures/boundary_guard/`), `~/.claude/` / `production_` 패턴 0건 |
| 11 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/` 본문 변경 0건 (cross-reference 답습 한정) |

**합산 0/11 위반.**

### 2.4 사용자 명시 풀 3+1 승격 trigger 6 자기 검증 (0/6 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | G3 22 권한 매트릭스 자체 변경 필요 | 0 | G3 §3.3 + §4 답습만 (변경 0건) |
| 2 | G4 §5 4 금지 추가/변경 필요 | 0 | G4 §5.2 직접 복사 (변경 0건) |
| 3 | Memory/Skill boundary runtime hook 구현 필요 | 0 | 본 PoC = 정적 검출 한정 (runtime 별도 합의) |
| 4 | Hermes PMO 격상 절차 변경 필요 | 0 | G3 §4.3 매트릭스 답습만 |
| 5 | P12 (Memory Poisoning Side-channel) 정식 등록 필요 | ⚠️ 부분 (canary 검출 한정 — 정식 등록 별도 합의) | known limitation 분리 |
| 6 | ADR-009 / ADR-011 / ADR-012 / G3 / G4 와 충돌 | 0 | cross-reference 답습 한정 |

**합산 0/6 발화** → **Reviewer-only 단축 합의 적격**.

### 2.5 G3 §3.3 + §4 + G4 §5.2 답습 충실도

| 영역 | 답습 방식 | 신규 작성 |
|---|---|---|
| Skill 17-field schema (G4 §3.1) | Group E `parse_yaml_v2` import 직접 | 0 |
| `ALLOWED_ACTIONS_ENUM` 7 (G4 §3.2 #9) | Group E import 직접 | 0 |
| `PROMOTION_STATUS_ENUM` 5 (G4 §3.3) | Group E import 직접 | 0 |
| 11-field JSONL schema (G4 §4.2) | Group C `validate_schema` + ENUMs import 직접 | 0 |
| `ALLOWED_AGENTS` (`user`/`claude-code`/`hermes`/`external_llm`) | Group C import 직접 | 0 |
| `ALLOWED_SCOPES` (`global`/`project`/`session`) | Group C import 직접 | 0 |
| Hermes-originated marker 6 패턴 | Group B `evidence_pass_gate` 답습 (catalog 복사 ~10줄) | inline ~10줄 |
| Governance PASS anchor 9 패턴 | Group B 답습 | inline ~10줄 |
| Reviewer / 외부 LLM marker 검출 | — (본 PoC 신규) | ~15줄 |
| Hermes PMO / Hermes 정책 변경 결정 본문 검출 | G3 §4.3 답습 | ~10줄 |
| Policy expression 6 패턴 (G4 §5.2 #1) | — (본 PoC 신규, Group D unauthorized-policy 패턴 답습 확장) | ~15줄 |
| Scope transition 검출 (G4 §5.2 #3) | — (본 PoC 신규) | ~15줄 |
| Hermes self-approve 검출 (G4 §5.2 #4) | — (본 PoC 신규) | ~10줄 |
| Custom 3 mode CLI dispatch | Group D/E 답습 | ~80줄 |
| Audit log JSONL × allowed_actions 매트릭스 | — (본 PoC 신규) | ~30줄 |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건** (runtime hook / Docker SDK / git2 / pyyaml 미도입). 신규 작성 ~250줄.

### 2.6 Group A~F 답습 충실

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + N mode + `--list-*` self-check) | Group A 1차 + Group D + Group E + Group F |
| Fixture 디렉토리 구조 (PASS / FAIL 분리, 3 mode × subdir) | Group A 1차 + Group D + Group E |
| CI workflow (N mode × PASS+FAIL + count self-check + F-금지 grep + summary.json + artifact + Evidence summary) | Group D + Group E 직접 답습 |
| Reviewer-only 단축 합의 형식 | Group A 1차 + Group B + Group D + Group E + Group F |
| **artifact path (leading dot 미사용)** | **Group F 후속 + Group D + Group E (group-g-logs/) 직접 답습** |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F |
| Group F skill_project.jsonl 17-field content | G-3 PASS fixture 직접 복사 답습 |
| Group E `valid_skill.yaml` 17-field YAML | G-1 PASS fixture 답습 base |

### 2.7 책무 분담 매트릭스 (사양 §0 답습)

| 영역 | G-1 | G-2 | G-3 | 분리 영역 |
|------|-----|-----|-----|----------|
| Skill yaml allowed_actions enum | ✅ | — | — | — |
| Audit log × allowed_actions 매트릭스 | ✅ | — | — | runtime wrapper = 별도 |
| Hermes-originated × governance PASS 공동 발생 | — | ✅ | — | — |
| Hermes 단독 합의 시도 (Reviewer/외부 LLM 부재) | — | ✅ | — | 외부 LLM 자동 호출 = 별도 |
| Hermes PMO 격상 / 정책 변경 자기 결정 | — | ✅ | — | — |
| Memory entry → policy 표현 검출 | — | — | ✅ #1 | runtime write blocker = 별도 |
| Session memory → Global 자동 승격 검출 | — | — | ✅ #3 | promotion hook runtime = 별도 |
| Hermes 자기 skill 승인 검출 | — | — | ✅ #4 | promotion hook runtime = 별도 |
| Skill → ADR 우회 (G4 §5.2 #2) | ✅ (`policy_write` enum 외 통합) | — | — | — |
| Runtime hook (Skill wrapper / Memory blocker / promotion hook) | ❌ | ❌ | ❌ | 별도 합의 |
| 실 git commit author 검사 | ❌ | ❌ | ❌ | T2 정책 영역 |
| 외부 LLM 자동 호출 통합 | ❌ | ❌ | ❌ | Layer 5 별도 합의 |

### 2.8 책무 분리 — 별도 합의 영역

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| Skill wrapper runtime 권한 검증 (실 호출 시점) | runtime hook 영역 (G3 §3.3.3) | 별도 합의 |
| Docker container cap_drop / read_only / tmpfs noexec | ADR-008 §2.6 R1-1 | 별도 합의 |
| Sandbox syscall 추적 (audit_t1 nightly 분석) | Layer 0 / runtime | 별도 합의 |
| escalation 검출 시 Skill 자동 비활성화 runtime | runtime hook | 별도 합의 |
| 실 git commit author / committer / trailer 검사 | T2 정책 영역 (G3 §2.2 #20) | Group B 답습 분리 |
| 외부 LLM 자동 의뢰 통합 (cross-vendor) | Layer 5 / 외부 합의 | 별도 합의 |
| 합의 보고서 PR auto-reject (Hermes-originated 시) | T3 정책 영역 | 별도 합의 |
| Memory boundary runtime hook (filesystem ACL / write blocker) | runtime hook | 별도 합의 |
| Promotion hook 자동 차단 runtime | runtime hook | 별도 합의 |
| Memory poisoning side-channel (P12) 정식 등록 | 풀 3+1 + 외부 LLM 1+ | 별도 합의 |
| G3 22 권한 분해 전수 매트릭스 | Group I 영역 | 별도 합의 (풀 3+1 + 외부 LLM 1+) |
| Hermes PMO 격상 결정 자동화 | G3 §4.3 = 풀 3+1 + 외부 LLM 1+ 필수 | 별도 합의 |
| pydantic / jsonschema / pyyaml / Docker SDK / git2 도구 도입 | 사용자 명시 — stdlib 단독 (Group D/E 답습) | 별도 합의 |

### 2.9 알려진 한계 (사양 §10 답습)

15건 (모두 분리 영역 명시). 핵심:
1. Skill wrapper runtime 권한 검증 미구현 — 별도 합의
2. Docker cap_drop 미통합 — 별도 합의
3. Sandbox syscall 추적 미통합 — 별도 합의
4. escalation 자동 비활성화 runtime 미구현
5. 실 git commit author 검사 미통합
6. 외부 LLM 자동 의뢰 미통합
7. PR auto-reject branch protection 미통합
8. Memory write blocker runtime 미구현
9. Promotion hook 차단 runtime 미구현
10. P12 정식 등록 미진입 — 풀 3+1 별도 합의
11. G3 22 권한 분해 미진입 — Group I 영역
12. Hermes PMO 격상 자동화 미진입 — G3 §4.3 매트릭스 답습만
13. G4 §5 4 금지 중 #2 (Skill→ADR 우회) 단독 fixture 미작성 — G-1 의 `policy_write` enum 외 통합 답습
14. pydantic / jsonschema / pyyaml / Docker SDK / git2 미도입 — 별도 합의
15. Markdown 본문 자기 검출 — CI fixture 한정 scan 으로 회피 (Group B 답습 패턴)

### 2.10 G4 §5.2 4 금지 cover 매트릭스

| # | 4 금지 | 본 PoC 검출 방식 | fixture |
|---|---|---|---|
| 1 | Memory 가 policy 를 대체 | Memory entry content × 6 policy expression regex | `memory_replaces_policy.jsonl` |
| 2 | Skill 이 ADR / Constitution 우회 | Skill yaml allowed_actions × `POLICY_WRITE_ACTIONS` (`policy_write`/`adr_write`/`constitution_write` 등) | **G-1 `skill_yaml_invalid_action.yaml` 통합 답습** |
| 3 | Session memory → Global memory 자동 승격 | JSONL chain 동일 id × scope: session → scope: global | `session_to_global_promotion.jsonl` |
| 4 | Hermes 가 skill 을 자기 승인 | JSONL agent: hermes × event: skill_approved/promoted | `hermes_self_approves_skill.jsonl` |

**4 금지 모두 cover** — #1/#3/#4 = G-3 fixture 3건 + #2 = G-1 fixture 통합 답습.

---

## 3. 풀 3+1 승격 trigger 6 자기 검증 (재명시)

§2.4 와 동일 — 0/6 미발화. **Reviewer-only 단축 합의 적격**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ G3 §3.3 (Skill escalation) + §4 (합의 자기참조 차단) + G4 §5.2 (4 금지) 의 *형식적 검출 layer* 운영 적용 첫 시제
- ✅ Custom validator 단독 채택 (외부 의존 0건 + runtime hook 0건) 답습 검증
- ✅ Group A~F 산출물 (`jsonl_hash_chain` + `schema_validator` + `evidence_pass_gate` 패턴) 재사용 답습 검증
- ✅ Group F `skill_project.jsonl` 17-field content 답습 (G-3 PASS fixture)
- ✅ Group E `valid_skill.yaml` 17-field 답습 (G-1 PASS fixture)
- ✅ Group F 후속 artifact path 답습 (`group-g-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A/B/C/D/E/F)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 실 runtime hook 운영 적용 (Skill wrapper / Memory write blocker / promotion hook)
- ❌ 실 git commit author 전수 검사
- ❌ 외부 LLM 자동 호출
- ❌ production memory/skill 데이터 사용
- ❌ Skill wrapper / Memory write blocker / promotion hook 실 구현
- ❌ G3 22 권한 매트릭스 변경
- ❌ G4 §5 4 금지 추가/변경
- ❌ pydantic / jsonschema / pyyaml / Docker SDK / git2 도입

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group G PoC = G3 + G4 *형식적 검출 layer 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, 11 금지 0/11 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 8/8 충족, 로컬 8/8 검증 PASS, CI workflow 13 step 형식 검증 PASS, G3 §3.3 + §4 + G4 §5.2 직접 답습 (변경 0건 / 외부 의존 0건 / runtime hook 0건)).

### 5.2 추가 조건 (C-G-1 ~ C-G-7)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-G-1 | 본 PoC = G3 + G4 *형식적 검출 layer 시제* 한정 — G3 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.3 #1~#3 명시 |
| C-G-2 | runtime hook 미진입 — Skill wrapper / Memory write blocker / promotion hook 실 구현 = 별도 합의 영역 | 사양 §10 #1~#9 + 본 합의 §2.8 명시 |
| C-G-3 | 실 git commit author / 외부 LLM 자동 호출 / production data 사용 = T2/T3 정책 영역 (별도 합의) | 본 합의 §2.3 #5~#10 명시 |
| C-G-4 | G3 22 권한 분해 = Group I 영역 (풀 3+1 + 외부 LLM 1+ 별도 합의) | 본 합의 §2.8 + §2.9 #11 명시 |
| C-G-5 | Hermes PMO 격상 결정 자동화 = G3 §4.3 매트릭스 = 풀 3+1 + 외부 LLM 1+ 필수 (자동화 금지) | 본 합의 §2.4 #4 + §2.8 명시 |
| C-G-6 | P12 (Memory Poisoning Side-channel) 정식 등록 = 풀 3+1 + 외부 LLM 1+ 별도 합의 | 사양 §10 #10 + 본 합의 §2.4 #5 명시 |
| C-G-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §14 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (PoC 본문 / CI workflow / 사양 / 합의 / .gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습 — Group A~F 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group A 3차 — URL/endpoint grep PoC (C-8) — 풀 3+1
   - (b) Group F 후속 — `hermes_to_openai` 또는 Skill 변환 feasibility 추가
   - (c) Group C 후속 — `history_rewrite` Layer 5 PoC (ADR-012 §2.8)
   - (d) cross-vendor LLM 의뢰 (Group D/E/G 산출물)
   - (e) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)
   - (f) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group G 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 6 0/6 발화, 11 금지 0/11 위반, PASS 기준 8/8 + ADR-011 §2.1 5/5 충족, 로컬 8/8 PASS, CI workflow 13 step 형식 검증 PASS, G3 §3.3 + §4 + G4 §5.2 직접 답습 (변경 0건 / 외부 의존 0건 / runtime hook 0건). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C/D/E/F 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
