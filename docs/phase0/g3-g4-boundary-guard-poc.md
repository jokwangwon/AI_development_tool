# G3 + G4 Boundary Guard — Group G PoC 사양

> **상태**: DRAFT (2026-05-10, Group G 진입 — Skill escalation 차단 (G-1) + 합의 자기참조 차단 (G-2) + Memory/Skill boundary 4 금지 (G-3) 통합 PoC)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §2.1 Order 8 (G3 Skill escalation 차단) + Order 9 tie (G3 합의 자기참조 차단 + G4 Memory boundary hook) / §3.1 매트릭스 / §5.3 의존성 (그룹 B + 그룹 E 완료 후) / §5.4 (단축 합의 + PoC evidence)
> - `docs/architecture/hermes-not-root-of-trust-runtime.md` §3.3 (Skill Permission Escalation — 정의 + 감지 + 차단 + Evidence + Rollback) / §4 (합의 인프라 순환 권위 해결 — 4.2 자기참조 차단 원칙 + 4.3 합의 형태 매트릭스 + 4.4 Reviewer-only / 외부 LLM / 사용자 승인 조건)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §5 (Memory/Skill Boundary — §5.2 4 금지 사항 + §5.3 본 §5 가 *하지 않는* 것)
> - `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` §C-N §2.3 (자동 학습 ≠ 자동 정책 변경 — Layer 3)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) + §2.3 운영 함의 #5 (사용자 승인 = 모든 T2/T3 결정의 최종 권위) + §2.4 (T1/T2/T3 분류)
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (11-field schema enum) / §2.12 (Hermes 변조 차단 매트릭스)
> - **Group A~F 산출물**: `tools/jsonl_hash_chain.py` (Group C — `validate_schema` + ENUMs `ALLOWED_TYPES` / `ALLOWED_AGENTS` / `ALLOWED_SCOPES`), `tools/evidence_pass_gate.py` (Group B — Hermes-originated marker + governance PASS anchor), `tools/schema_validator.py` (Group E — `ALLOWED_ACTIONS_ENUM` 7 + `PROMOTION_STATUS_ENUM` 5 + `parse_yaml_v2`), `tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` (Group F)
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 6 풀 3+1 승격 trigger / 8 검증 / 외부 의존 0건 / runtime hook 미진입
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F PoC 사양 형식 (`g2-gp4-g4-schema-validation-poc.md` 직접 답습)

---

## 0. 목적

본 PoC 는 G3 *Hermes ≠ root of trust 운영 layer* 의 핵심 3 영역 + G4 *Memory/Skill Boundary 4 금지* 의 형식적 검출 layer 첫 시제 — 3 mode 통합 도구 (`tools/boundary_guard.py`) 로 다음 검증:

1. **G-1 (Skill Permission Escalation)** — Skill yaml `allowed_actions` enum 위반 + audit log JSONL × `allowed_actions` 매트릭스 정적 검출 (G3 §3.3.2 답습 — *wrapper / audit / sandbox* 3 channel 중 *audit log 분석* layer 한정)
2. **G-2 (합의 자기참조 차단)** — 합의 보고서 본문에서 *Hermes-originated marker × G2/G3/G4 PASS 결정 공동 발생* + *Reviewer/외부 LLM 부재* 정적 검출 (G3 §4.2 자기참조 차단 원칙 답습)
3. **G-3 (Memory/Skill Boundary 4 금지)** — G4 §5.2 4 금지 사항 (Memory→policy / Skill→ADR / Session→Global / Hermes→skill 자기 승인) 정적 검출

**범위 한정 핵심 결정** (사용자 명시 "최소 PoC" 답습):

- **runtime hook 미진입** — Skill wrapper runtime / Docker cap_drop / sandbox syscall 추적 / 실 git commit author 검사 / Memory write blocker / promotion hook 자동 차단 = **별도 합의 영역** (Group I 또는 ADR-014 발행 후속).
- **외부 의존 0건** — pydantic / jsonschema / pyyaml / Docker SDK / git2 등 도구 도입 0건 (Group D/E 답습).
- **외부 LLM 자동 의뢰 통합 미진입** — cross-vendor 자동 호출 = Layer 5 영역.

본 PoC 는 **형식적 검출 layer 한정** — runtime 강제 / 정책 정식화 (P9~P12) / Hermes PMO 격상 = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §3.1 + G3 §3.3 + §4 + G4 §5 + ADR-009/011/012 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g3-g4-boundary-guard-poc.md` | PoC 사양 + 답습 매핑 + 사용자 명시 8 검증 / 6 trigger / 9 fixture 매트릭스 |
| Validator | `tools/boundary_guard.py` | 단일 도구 + 3 mode (skill-escalation / consensus-self-reference / memory-skill-boundary) + `--list-boundaries` self-check + Group A~F import 직접 (`jsonl_hash_chain.validate_schema` + Group E `ALLOWED_ACTIONS_ENUM` + Group B Hermes-originated marker 패턴 답습) + audit log × allowed_actions 매트릭스 + 합의 보고서 marker 검출 + JSONL chain transition 검출 |
| G-1 PASS fixture × 1 | `tests/fixtures/boundary_guard/skill_escalation/pass/valid_skill_within_allowed.yaml` | Group E `valid_skill.yaml` 답습 (allowed_actions 정합) |
| G-1 FAIL fixture × 2 | `tests/fixtures/boundary_guard/skill_escalation/fail/{skill_yaml_invalid_action.yaml, audit_log_escalation.jsonl}` | yaml-invalid-action (enum 외) + audit-log-escalation (호출 권한 위반) |
| G-2 PASS fixture × 1 | `tests/fixtures/boundary_guard/consensus_self_reference/pass/proper_reviewer_consensus.md` | Group D Reviewer-only 합의 답습 (Reviewer marker + 외부 LLM 부재 OK) |
| G-2 FAIL fixture × 2 | `tests/fixtures/boundary_guard/consensus_self_reference/fail/{hermes_self_consensus.md, hermes_pmo_self_promotion.md}` | hermes-self-consensus + hermes-pmo-self-promotion |
| G-3 PASS fixture × 1 | `tests/fixtures/boundary_guard/memory_skill_boundary/pass/safe_memory_skill_chain.jsonl` | 4 금지 위반 0건 (Group F skill_project.jsonl 답습) |
| G-3 FAIL fixture × 3 | `tests/fixtures/boundary_guard/memory_skill_boundary/fail/{memory_replaces_policy.jsonl, session_to_global_promotion.jsonl, hermes_self_approves_skill.jsonl}` | G4 §5 4 금지 중 3건 cover (#1 memory→policy + #3 session→global + #4 hermes→skill 자기 승인). #2 (Skill→ADR 우회) = G-1 의 `policy_write` enum 위반 답습으로 통합 |
| CI workflow | `.github/workflows/boundary-guard.yml` | PASS/FAIL 양방향 + boundaries-list 자기 검증 + F-금지 grep + summary.json + artifact (`group-g-logs/` Group F 후속 답습) + Evidence summary |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g3-g4-boundary-guard-reviewer-only.md` | PoC 검토 + 6 trigger 0/6 자기 검증 + evidence 매트릭스 통합 (Group D/E/F 답습) |

**합산 = 8 파일** (Group D/E/F 답습 평균).

### 1.2 제외 (별도 합의 영역)

| 항목 | 분리 이유 |
|------|----------|
| Skill wrapper runtime 권한 검증 (실 호출 시점) | G3 §3.3.3 wrapper layer = runtime hook 영역 — 별도 합의 |
| Docker container cap_drop / read_only / tmpfs noexec 활성화 | ADR-008 §2.6 R1-1 — 별도 합의 |
| Sandbox syscall 추적 (audit_t1 nightly 분석) | Layer 0 / runtime — 별도 합의 |
| escalation 검출 시 Skill 자동 비활성화 runtime | runtime hook — 별도 합의 |
| 실 git commit author / committer / trailer 검사 | T2 정책 영역 (G3 §2.2 #20) — Group B 답습 분리 |
| 외부 LLM 자동 의뢰 통합 (cross-vendor) | Layer 5 / 외부 합의 — 별도 합의 |
| 합의 보고서 PR auto-reject (Hermes-originated 시) | T3 정책 영역 — 별도 합의 |
| Memory boundary runtime hook (filesystem ACL / write blocker) | runtime hook — 별도 합의 |
| Promotion hook 자동 차단 runtime | runtime hook — 별도 합의 |
| Memory poisoning side-channel (P12) 정식 등록 | 풀 3+1 + 외부 LLM 1+ — 별도 합의 |
| pydantic / jsonschema / pyyaml / Docker SDK / git2 도구 도입 | 사용자 명시 — stdlib 단독 (Group D/E 답습), 도입 = 별도 합의 |
| G3 22 권한 분해 (전수 매트릭스 분해) | Group I 영역 — 별도 합의 (풀 3+1 + 외부 LLM 1+) |
| Hermes PMO 격상 결정 자동화 | G3 §4.3 매트릭스 = 풀 3+1 + 외부 LLM 1+ 필수 |
| ADR-014 발행 (Migration script) | Group H 영역 |
| G3 §3.3 / §4 / G4 §5 본문 변경 | T3 영역 (G3 §4.3 매트릭스 답습) — 별도 합의 |

---

## 2. 도구 선택 근거

### 2.1 stdlib 단독 채택 (Group D/E 답습)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom validator (stdlib `re` + `json` + `dataclasses` 단독)** | **✅ 채택** | Group D/E 답습 (외부 의존 0건) + Tier-2/3 catalog 확장 위험 0건 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) pydantic | ❌ 제외 | Group E 영역 (장기 schema 정책 결정 별도 합의) |
| (C) pyyaml | ❌ 제외 | Group E `parse_yaml_v2` import 직접 답습 |
| (D) Docker SDK / git2 / runtime hook 라이브러리 | ❌ 제외 | runtime 영역 진입 위험 (사용자 명시 분리) |

**채택 = (A) 단독**.

### 2.2 본 PoC 의 stdlib 답습 영역

| stdlib 모듈 | 책무 |
|------|------|
| `re` | Hermes-originated marker / governance PASS anchor / policy 표현 grep / 4 금지 regex |
| `json` | JSONL ledger entry parse + audit log JSONL parse |
| `dataclasses` | `Violation` reporter (Group D/E 답습) |
| `argparse` | 3 mode CLI + `--list-boundaries` self-check |
| `pathlib` | 재귀 file iterator |

**외부 의존 0건** (`requirements-dev.txt` 변경 0건).

### 2.3 Group A~F 답습 영역 (import 직접)

```python
from jsonl_hash_chain import (  # Group C
    ALLOWED_AGENTS,         # ('user', 'claude-code', 'hermes', 'external_llm')
    ALLOWED_SCOPES,         # ('global', 'project', 'session')
    ALLOWED_TYPES,          # ('memory', 'skill', 'meta')
    parse_jsonl,            # JSONL parser
    validate_schema,        # 11-field schema validation
)

from schema_validator import (  # Group E (단, 모듈 import 가능 여부 확인 필요 — alternative: re-define)
    ALLOWED_ACTIONS_ENUM,   # ('read', 'write', 'shell', 'network', 'db', 'git', 'docker')
    PROMOTION_STATUS_ENUM,  # ('proposed', 'approved', 'promoted', 'archived', 'revoked')
    parse_yaml_v2,          # YAML mini-parser (stdlib only)
)
```

> **각주**: Group E `schema_validator` import 가 안정적으로 동작하지 않을 경우 (예: tools/ PYTHONPATH 차이), 본 PoC 는 ENUM 정의 (~10줄) 만 inline 복사. 답습 의도는 동일 (G4 §3.1 + §3.2 변경 0건).

---

## 3. Group A~F 산출물 재사용 매트릭스

### 3.1 import 직접 (리팩토링 0건)

| 영역 | Group 답습 | 신규 작성 |
|---|---|---|
| 11-field JSONL schema 검증 | Group C `jsonl_hash_chain.validate_schema` import 직접 | 0 |
| ENUM 정의 (`ALLOWED_AGENTS` / `ALLOWED_SCOPES` / `ALLOWED_TYPES`) | Group C import 직접 | 0 |
| `ALLOWED_ACTIONS_ENUM` 7 / `PROMOTION_STATUS_ENUM` 5 | Group E import 직접 (또는 inline) | 0 (inline 시 ~10줄) |
| YAML mini-parser | Group E `parse_yaml_v2` import 직접 (또는 inline) | 0 (inline 시 ~80줄) |
| Hermes-originated marker 6 패턴 | Group B 답습 (catalog 복사) | ~10줄 |
| Governance PASS anchor 9 패턴 | Group B 답습 | ~10줄 |
| Custom boundary 정적 검출 logic | — | ~250줄 (3 mode + 4 G4 §5 boundary + violation reporter + CLI dispatch) |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건**. 신규 작성 ~250 줄 (stdlib + Group A~F import 직접 + boundary 검출 logic).

### 3.2 fixture 답습

| Group F/E fixture | 본 PoC 답습 |
|---|---|
| `tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` (Group F — 17-field skill content) | G-3 PASS fixture (`safe_memory_skill_chain.jsonl`) 답습 base |
| `tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml` (Group E — 17-field YAML) | G-1 PASS fixture (`valid_skill_within_allowed.yaml`) 답습 base |

---

## 4. G-1 Skill Escalation 검증 기준 (G3 §3.3 답습)

### 4.1 검증 layer

| Layer | 본 PoC 검증 | 분리 영역 |
|---|---|---|
| Skill yaml `allowed_actions` enum 검증 | ✅ Group E `ALLOWED_ACTIONS_ENUM` 답습 (7 enum) | — |
| Skill yaml `forbidden_actions` ∩ `allowed_actions` = ∅ | ✅ Group E 답습 | — |
| `policy_write` / `adr_write` / `constitution_write` 등 *정책 변경 권한* 검출 (G4 §5 #2 답습) | ✅ enum 외 항목으로 검출 | — |
| Audit log JSONL × allowed_actions 매트릭스 검증 | ✅ audit log entry 의 호출 action 이 yaml allowed_actions 외 시 violation | — |
| `event: skill_escalation` ledger entry 형식 (ADR-012 §2.2 enum) | ✅ `validate_schema` Group C 답습 | — |
| Skill wrapper runtime 호출 검증 (실 시점) | ❌ | runtime hook 영역 |
| Docker cap_drop / sandbox syscall | ❌ | runtime 영역 |

### 4.2 검증 명령

```bash
python tools/boundary_guard.py --mode skill-escalation tests/fixtures/boundary_guard/skill_escalation/pass/   # rc=0
python tools/boundary_guard.py --mode skill-escalation tests/fixtures/boundary_guard/skill_escalation/fail/   # rc=1, ≥2 패턴 cover
```

---

## 5. G-2 합의 자기참조 차단 검증 기준 (G3 §4 답습)

### 5.1 검증 layer

| Layer | 본 PoC 검증 | 분리 영역 |
|---|---|---|
| 합의 보고서 본문 Hermes-originated marker 6 패턴 (Group B 답습) | ✅ Generated-by/Agent-Origin/Authored-by/Co-Authored-By/Approved-by/Signed-off-by Hermes | — |
| Governance PASS anchor 9 패턴 (Group B 답습) | ✅ Gate PASS / Implementation PASS / G[1-9]\w* PASS / GP-N PASS / APPROVE WITH CONDITIONS | — |
| Hermes-originated × Governance PASS 공동 발생 = 자기참조 시도 violation | ✅ | — |
| Reviewer marker 부재 (`Reviewer-only` / `풀 3+1` / `Agent A/B/C` 등) + 외부 LLM marker 부재 (`외부 LLM` / `cross-vendor` / `GPT` / `Gemini`) → Hermes 단독 합의 시도 violation | ✅ | — |
| Hermes PMO 격상 / Hermes 정책 변경 결정 본문 (`Hermes PMO 격상` / `Hermes 정책 변경` / `redaction-policy.yaml` 등) 의 Hermes-originated 시도 violation | ✅ | — |
| 실 git commit author 검사 | ❌ | T2 정책 영역 (G3 §2.2 #20) |
| 외부 LLM 자동 호출 통합 | ❌ | Layer 5 / 외부 합의 |

### 5.2 검증 명령

```bash
python tools/boundary_guard.py --mode consensus-self-reference tests/fixtures/boundary_guard/consensus_self_reference/pass/   # rc=0
python tools/boundary_guard.py --mode consensus-self-reference tests/fixtures/boundary_guard/consensus_self_reference/fail/   # rc=1, ≥2 패턴 cover
```

---

## 6. G-3 Memory/Skill Boundary 4 금지 검증 기준 (G4 §5.2 답습)

### 6.1 4 금지 사항 매핑

| # | G4 §5.2 4 금지 | 본 PoC 검증 방식 | fixture cover |
|---|---|---|---|
| 1 | **Memory 가 policy 를 대체** | Memory entry content 의 정책 표현 grep (`update ADR` / `modify Constitution` / `policy:` / `disable Hermes` / `bypass redaction` 등) | `memory_replaces_policy.jsonl` |
| 2 | **Skill 이 ADR / Constitution 우회** | Skill yaml `allowed_actions` 에 `policy_write` / `adr_write` / `constitution_write` 등 enum 외 정책 변경 권한 포함 | **G-1 의 `skill_yaml_invalid_action.yaml` 답습 통합** (ALLOWED_ACTIONS_ENUM 외) |
| 3 | **Session memory → global memory 자동 승격** | JSONL chain 의 동일 `id` × `scope: session` → `scope: global` transition 검출 | `session_to_global_promotion.jsonl` |
| 4 | **Hermes 가 skill 을 자기 승인** | JSONL chain 의 `agent: hermes` × `event: skill_approved` / `skill_promoted` 공동 발생 검출 | `hermes_self_approves_skill.jsonl` |

**총 4 금지 모두 cover** — #1/#3/#4 = G-3 fixture 3건 + #2 = G-1 fixture 통합 답습.

### 6.2 검증 명령

```bash
python tools/boundary_guard.py --mode memory-skill-boundary tests/fixtures/boundary_guard/memory_skill_boundary/pass/   # rc=0
python tools/boundary_guard.py --mode memory-skill-boundary tests/fixtures/boundary_guard/memory_skill_boundary/fail/   # rc=1, ≥3 패턴 cover (#1 + #3 + #4)
```

---

## 7. fixture 9건 사양 (사용자 명시 최소 PoC 답습)

### 7.1 G-1 PASS × 1

`tests/fixtures/boundary_guard/skill_escalation/pass/valid_skill_within_allowed.yaml`:

Group E `valid_skill.yaml` 답습 — 17-field 통과 + `allowed_actions: [shell, read]` (enum 정합) + `forbidden_actions: [network, db]` (disjoint).

### 7.2 G-1 FAIL × 2

| 파일 | violation |
|------|----------|
| `skill_yaml_invalid_action.yaml` | `allowed_actions: [shell, network, policy_write]` (enum 외 `policy_write` = G4 §5 #2 통합 답습) + `forbidden_actions: [shell]` (∩ ≠ ∅) |
| `audit_log_escalation.jsonl` | Skill yaml allowed_actions=[shell, read] 인데 audit log 의 호출 action 이 `network` 시도 (allowed_actions 외) |

**예상**: rc=1 + ≥2 violations + 2 패턴 cover.

### 7.3 G-2 PASS × 1

`tests/fixtures/boundary_guard/consensus_self_reference/pass/proper_reviewer_consensus.md`:

Group D Reviewer-only 합의 답습 — Reviewer marker (`Reviewer-only`) + 명시 PASS 표기 + Hermes-originated marker 부재.

### 7.4 G-2 FAIL × 2

| 파일 | violation |
|------|----------|
| `hermes_self_consensus.md` | `Generated-by: Hermes` + `G2 PASS` + Reviewer marker 부재 + 외부 LLM marker 부재 |
| `hermes_pmo_self_promotion.md` | `Authored-by: Hermes` + `Hermes PMO 격상` 결정 본문 + Reviewer 부재 |

**예상**: rc=1 + ≥2 violations + 2 패턴 cover.

### 7.5 G-3 PASS × 1

`tests/fixtures/boundary_guard/memory_skill_boundary/pass/safe_memory_skill_chain.jsonl`:

Group F `skill_project.jsonl` 답습 + `agent: user` 한정 + scope transition 0건 + Memory content 정책 표현 0건.

### 7.6 G-3 FAIL × 3

| 파일 | G4 §5.2 # | violation |
|------|----------|----------|
| `memory_replaces_policy.jsonl` | #1 | Memory entry content = `{"action": "update ADR-008"}` (정책 표현) |
| `session_to_global_promotion.jsonl` | #3 | 동일 `id` × `scope: session` → `scope: global` chain transition |
| `hermes_self_approves_skill.jsonl` | #4 | `agent: hermes` × `event: skill_promoted` 공동 발생 |

**예상**: rc=1 + ≥3 violations + 3 패턴 cover.

### 7.7 fake canary 의무

본 PoC fixture 의 모든 secret / canary 는 **fake** 의무. 사용자 명시 형식 답습 (Group D 답습):
- `R41T-fakecanary-G-not-real` (R-4.1 marker 답습)
- audit log fixture 의 호출 인자 = fake string

**실 API key / 실 production data 0건** — F-금지 grep 자동 강제.

---

## 8. 검증 매트릭스 (사용자 명시 8 검증 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 결과 |
|---|------|------|------|---------|------|
| 1 | G-1 PASS | `skill_escalation/pass/` | `--mode skill-escalation` | 0 | violations=0 |
| 2 | G-1 FAIL | `skill_escalation/fail/` | `--mode skill-escalation` | 1 | ≥2 violations + 2 패턴 cover (yaml-invalid-action / audit-log-escalation) |
| 3 | G-2 PASS | `consensus_self_reference/pass/` | `--mode consensus-self-reference` | 0 | violations=0 |
| 4 | G-2 FAIL | `consensus_self_reference/fail/` | `--mode consensus-self-reference` | 1 | ≥2 violations + 2 패턴 cover (hermes-self-consensus / hermes-pmo-self-promotion) |
| 5 | G-3 PASS | `memory_skill_boundary/pass/` | `--mode memory-skill-boundary` | 0 | violations=0 |
| 6 | G-3 FAIL | `memory_skill_boundary/fail/` | `--mode memory-skill-boundary` | 1 | ≥3 violations + 3 패턴 cover (memory-replaces-policy / session-to-global / hermes-self-approves) |
| 7 | `--list-boundaries` self-check | `--list-boundaries` | `--list-boundaries` | 0 | total=4 G4 §5 boundaries + 3 modes + G3 §4.3 합의 매트릭스 13 row |
| 8 | F-금지 grep | scanner + fixture grep | grep | 0 | 실 Hermes runtime / 실 commit author / 실 production data 0건 |

**합산 8 검증** (3 mode × PASS+FAIL + boundaries-list + F-금지 grep).

---

## 9. PASS 기준 자기 검증 매트릭스

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | G-1 PASS scan | rc=0 + 위반 0건 |
| 2 | G-1 FAIL scan | rc=1 + ≥2 + 2 패턴 cover |
| 3 | G-2 PASS scan | rc=0 + 위반 0건 |
| 4 | G-2 FAIL scan | rc=1 + ≥2 + 2 패턴 cover |
| 5 | G-3 PASS scan | rc=0 + 위반 0건 |
| 6 | G-3 FAIL scan | rc=1 + ≥3 + 3 패턴 cover (G4 §5 4 금지 중 #1/#3/#4 cover, #2 = G-1 통합) |
| 7 | `--list-boundaries` self-check | total=4 boundaries + 3 modes + 13 합의 매트릭스 row |
| 8 | F-금지 grep | 0건 (실 Hermes runtime / 실 commit author / 실 production data 부재) |

**합산 8/8 충족 적격**.

---

## 10. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | Skill wrapper runtime 권한 검증 (실 호출 시점) | runtime hook 영역 | 별도 합의 |
| 2 | Docker container cap_drop / read_only / tmpfs noexec | ADR-008 §2.6 R1-1 | 별도 합의 |
| 3 | Sandbox syscall 추적 (audit_t1 nightly 분석) | Layer 0 / runtime | 별도 합의 |
| 4 | escalation 검출 시 Skill 자동 비활성화 runtime | runtime hook | 별도 합의 |
| 5 | 실 git commit author / committer / trailer 검사 | T2 정책 영역 | Group B 답습 분리 |
| 6 | 외부 LLM 자동 의뢰 통합 (cross-vendor) | Layer 5 / 외부 합의 | 별도 합의 |
| 7 | 합의 보고서 PR auto-reject (Hermes-originated 시) | T3 정책 영역 | 별도 합의 |
| 8 | Memory boundary runtime hook (filesystem ACL / write blocker) | runtime hook | 별도 합의 |
| 9 | Promotion hook 자동 차단 runtime | runtime hook | 별도 합의 |
| 10 | Memory poisoning side-channel (P12) 정식 등록 | 풀 3+1 + 외부 LLM 1+ | 별도 합의 |
| 11 | G3 22 권한 분해 전수 매트릭스 | Group I 영역 | 별도 합의 (풀 3+1 + 외부 LLM 1+) |
| 12 | Hermes PMO 격상 결정 자동화 | G3 §4.3 = 풀 3+1 + 외부 LLM 1+ 필수 | 별도 합의 |
| 13 | G4 §5 4 금지 중 #2 (Skill→ADR 우회) 단독 fixture | G-1 의 `skill_yaml_invalid_action.yaml` 통합 답습 (`policy_write` enum 외) | 별도 fixture 확장 영역 |
| 14 | pydantic / jsonschema / pyyaml / Docker SDK / git2 도구 도입 | 사용자 명시 — stdlib 단독 (Group D/E 답습) | 별도 합의 |
| 15 | Markdown 본문 자기 검출 (Group D/E 답습 패턴) | CI 는 `tests/fixtures/boundary_guard/` 한정 scan 으로 회피 | Group B PoC 사양 §2.8 #1 답습 |

---

## 11. CI workflow 설계

### 11.1 12 step 구조 (Group D/E/F 답습)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Prepare log directory | `mkdir -p group-g-logs` (Group F 후속 답습 — leading dot 미사용) |
| 4 | `--list-boundaries` self-check | rc=0 + total=4 boundaries + 3 modes + 13 합의 매트릭스 row grep |
| 5 | G-1 PASS — skill-escalation pass/ | rc=0 + violations=0 grep |
| 6 | G-1 FAIL — skill-escalation fail/ | rc=1 + ≥2 + 2 패턴 cover (yaml-invalid-action / audit-log-escalation) grep |
| 7 | G-2 PASS — consensus-self-reference pass/ | rc=0 + violations=0 grep |
| 8 | G-2 FAIL — consensus-self-reference fail/ | rc=1 + ≥2 + 2 패턴 cover (hermes-self-consensus / hermes-pmo-self-promotion) grep |
| 9 | G-3 PASS — memory-skill-boundary pass/ | rc=0 + violations=0 grep |
| 10 | G-3 FAIL — memory-skill-boundary fail/ + F-금지 grep | rc=1 + ≥3 + 3 패턴 cover (memory-replaces-policy / session-to-global / hermes-self-approves) grep + F-금지 grep (실 Hermes runtime / 실 commit author / 실 production data 0건) |
| 11 | Build summary.json + Upload artifact | `actions/upload-artifact@v4` `boundary-guard-evidence` retention 30일 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-g-logs/`** (Group F 후속 답습 — leading dot 미사용).

### 11.2 paths trigger

```yaml
paths:
  - tools/boundary_guard.py
  - tools/jsonl_hash_chain.py     # Group C 모듈 변경 시 trigger
  - tools/schema_validator.py     # Group E 모듈 변경 시 trigger
  - tools/evidence_pass_gate.py   # Group B 모듈 변경 시 trigger (패턴 답습)
  - tests/fixtures/boundary_guard/**
  - .github/workflows/boundary-guard.yml
```

---

## 12. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 6 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | G3 22 권한 매트릭스 자체 변경 필요 | ❌ 미발화 | G3 §3.3 + §4 답습만 (변경 0건) |
| 2 | G4 §5 4 금지 추가/변경 필요 | ❌ 미발화 | G4 §5.2 직접 복사 (변경 0건) |
| 3 | Memory/Skill boundary runtime hook 구현 필요 | ❌ 미발화 | 본 PoC = 정적 검출 한정 (runtime 별도 합의) |
| 4 | Hermes PMO 격상 절차 변경 필요 | ❌ 미발화 | G3 §4.3 매트릭스 답습만 |
| 5 | P12 (Memory Poisoning Side-channel) 정식 등록 필요 | ⚠️ 부분 — 본 PoC = canary 검출 한정 (정식 등록 별도 합의) | 본 한계 = §10 #10 분리 명시 |
| 6 | ADR-009 / ADR-011 / ADR-012 / G3 / G4 와 충돌 | ❌ 미발화 | cross-reference 답습 한정 |

**합산 0/6 발화 (#5 부분은 known limitation 분리)** → **Reviewer-only 단축 합의 적격**.

---

## 13. Evidence 형식 (5종 — Group A/B/C/D/E/F 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g3-g4-boundary-guard-poc.md`) | 본 문서 |
| JSONL ledger entry | summary.json (단순화 — Group D/E 답습) | summary.json 16 항목 |
| 격리 검증 | fixture 한정 + 실 Hermes runtime 0건 + 외부 의존 0건 | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `boundary-guard.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g3-g4-boundary-guard-reviewer-only.md`) | 본 PoC 산출물 #8 |

---

## 14. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group G 진입 사양 — 사용자 명시 8 검증 / 6 trigger / 9 fixture / 3 mode (G-1 Skill escalation + G-2 합의 자기참조 차단 + G-3 Memory/Skill boundary 4 금지) / stdlib 단독 채택. Group A 1차/2차 + Group B + Group C + Group D + Group E + Group F 사양 형식 직접 답습. G3 §3.3 + §4 + G4 §5 + ADR-009/011/012 답습 (변경 0건). Custom validator 단독 채택 (외부 의존 0건). artifact path `group-g-logs/` (Group F 후속 답습, leading dot 미사용). Group E `valid_skill.yaml` 17-field + Group F `skill_project.jsonl` content + Group B Hermes-originated marker 답습. |
