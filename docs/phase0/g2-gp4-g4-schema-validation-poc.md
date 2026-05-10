# G2 GP-4 + G4 Schema Validation — Group E PoC 사양

> **상태**: DRAFT (2026-05-10, Group E 진입 — External Input Validation (E-1) + Memory/Skill schema validation (E-2) 통합 PoC)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §2.1 Order 6 tie (GP-4 + G4 Memory/Skill schema validation) / §3.1 매트릭스 / §5.3 의존성 (그룹 B + 그룹 C 완료 후) / §5.4 (단축 합의 + PoC evidence)
> - `docs/architecture/governance-preconditions.md` §6 (GP-4 외부 입력 검증)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §3.1 (Skill 17-field schema) / §3.2 (필드별 검증 규칙) / §3.3 (promotion_status 5 enum + transition) / §4.2 (JSONL entry 11-field) / §5 (Memory/Skill boundary 4 금지 — *분리 영역*)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) + §2.3 운영 함의 #1 (Tools verify Hermes 출력)
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (11-field schema enum) / §3.1 + §3.2 (schema 진화 정책)
> - `tools/jsonl_hash_chain.py` (Group C `validate_schema` 11-field — import 직접 답습)
> - `tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` (Group F 17-field skill content — YAML 재구성 답습 출처)
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 6 풀 3+1 승격 trigger / 10 금지 / 6 PASS 검증
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group D + Group F PoC 사양 형식 (`g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` 직접 답습)

---

## 0. 목적

본 PoC 는 G2 GP-4 (External Input Validation) 와 G4 (Memory/Skill schema validation) 의 *형식적 검증 layer* 첫 시제 — Hermes / Worker / LLM 출력의 *외부 입력 schema* 검증과 G4 §3.1 17-field Skill schema + §4.2 11-field JSONL entry schema 의 정적 검증을 통합 적용.

**범위 한정 핵심 결정** (사용자 명시 "최소 PoC 단위" 답습):

- **E-1 (GP-4)** = code-side *external input schema* 검증만 (`tools/schema_validator.py --mode external-input`). 실 LLM API 호출 / Reviewer Agent 추론적 prompt injection 감지 / runtime escape 통합 = **별도 합의 영역**, 본 PoC 미진입.
- **E-2 (G4 schema)** = G4 §3.1 17-field Skill + §4.2 11-field JSONL entry 의 **정적 검증만**. Memory boundary 4 금지 runtime 강제 / Skill wrapper escalation 차단 / 재귀 JSON Schema 의미 검증 = **Group G 영역** (별도 합의).

본 PoC 는 **형식적 검증 layer 한정** — 의미적 검증 / runtime hook / 정책 정식화 (P9~P12) = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §3.1 + GP-4 §6 + G4 §3 + §4.2 + ADR-011/012 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g2-gp4-g4-schema-validation-poc.md` | PoC 사양 + 답습 매핑 + 사용자 명시 10 금지 / 6 trigger / 6 PASS 매트릭스 |
| Validator | `tools/schema_validator.py` | 단일 도구 + 2 mode (external-input / skill-schema) + 17-field def + 11-field def (Group C `validate_schema` import 직접) + injection canary regex (~26+) + ENUM 정의 (allowed_actions / promotion_status / promotion_transitions) + provider lock-in marker grep + violation reporter |
| E-1 PASS fixture × 1 | `tests/fixtures/schema_validation/external_input/pass/safe_worker_output.json` | 정상 Worker 출력 (FP 검증) |
| E-1 FAIL fixture × 4 | `tests/fixtures/schema_validation/external_input/fail/{prompt_injection.txt, unauthorized_policy.json, malformed_json.txt, injection_payload.json}` | 4 패턴 cover (prompt-injection / unauthorized-policy / malformed-json / injection-payload) |
| E-2 PASS fixture × 1 | `tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml` | Group F `skill_project.jsonl` 17-field content 의 YAML 재구성 답습 (필수 12 + MVP-권장 5 모두 포함) |
| E-2 FAIL fixture × 4 | `tests/fixtures/schema_validation/skill_schema/fail/{missing_required.yaml, invalid_action.yaml, invalid_promotion_status.yaml, provider_lockin.yaml}` | 4 패턴 cover (missing-required / invalid-action / invalid-promotion-transition / provider-lockin C-K 위반) |
| CI workflow | `.github/workflows/schema-validation.yml` | PASS/FAIL 양방향 + 17-field count 자기 검증 + F-금지 grep + summary.json + artifact (`group-e-logs/` Group F 후속 답습) + Evidence summary |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g2-gp4-g4-schema-validation-reviewer-only.md` | PoC 검토 + 6 trigger 0/6 자기 검증 + evidence 매트릭스 통합 (Group D/F 답습) |

**합산 = 8 파일** (Group D/F 답습 평균).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 10 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| G2 GP-4 최종 PASS 선언 | **사용자 명시** — 본 PoC = *형식적 검증 layer 시제* 한정 |
| G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** |
| G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** |
| Hermes PMO 격상 선언 | **사용자 명시** |
| 실 LLM API 호출 | **사용자 명시** — fixture 한정 |
| 실 provider SDK 호출 | **사용자 명시** |
| production memory/skill 데이터 사용 | **사용자 명시** — fixture 한정 (Group F skill 답습) |
| ADR 본문 자동 갱신 | **사용자 명시** — cross-reference 답습 한정 |
| Memory boundary hook 구현 | **사용자 명시** — Group G 영역 (G4 §5 4 금지 runtime 강제) |
| Skill wrapper 구현 | **사용자 명시** — Group G 영역 (G3 §3.3 escalation 차단) |
| Reviewer Agent 추론적 prompt injection 감지 | Layer 5 (3+1 합의) — 별도 합의 (GP-4 §6.3 추론적 보조) |
| sqlite bind variable / shlex.quote runtime escape 통합 | runtime hook 영역 — 별도 합의 |
| 재귀 JSON Schema 의미 검증 | 본 PoC = top-level 형식만, 재귀 JSON Schema 의미 검증 별도 |
| pydantic / jsonschema 도구 도입 | 사용자 명시 — stdlib 단독 채택 (Group D 답습), 도입 = 별도 합의 |
| P9 / P10 / P11 / P12 (prompt injection / evidence forgery / memory poisoning 등) 정식 등록 | 풀 3+1 trigger #5 위험 — 별도 합의 |

---

## 2. 도구 선택 근거

### 2.1 stdlib 기반 custom validator 채택 (사용자 명시)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom validator (stdlib `re` + `json` + `dataclasses` 단독)** | **✅ 채택** | Group D 답습 (외부 의존 0건) + Tier-2/3 catalog 확장 위험 0건 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) pydantic | ❌ 제외 | 외부 의존 1건 추가 + dev requirement 갱신 + pydantic v1/v2 호환성 결정 = 풀 3+1 trigger #4 위험 (장기 정책 고정) |
| (C) jsonschema | ❌ 제외 | 외부 의존 1건 + JSON Schema draft 버전 결정 = 별도 합의 |

**채택 = (A) 단독**. pydantic / jsonschema 도입은 *별도 합의* (장기 schema 정책 결정 시점, 풀 3+1 + 외부 LLM 1+ 영역).

### 2.2 본 PoC 의 stdlib 답습 영역

| stdlib 모듈 | 책무 |
|------|------|
| `re` | 17-field schema regex 검증 + injection canary 검출 + provider lock-in marker grep |
| `json` | malformed JSON 검출 + JSON well-formed 검증 |
| `dataclasses` | `Violation` reporter (Group D 답습) |
| `argparse` | 2 mode CLI + `--list-skill-fields` self-check |
| `enum` (선택) | `AllowedAction` / `PromotionStatus` enum 정의 |
| `pathlib` | 재귀 file iterator (Group D 답습) |

**외부 의존 0건** (`requirements-dev.txt` 변경 0건).

### 2.3 YAML 처리 결정

E-2 fixture 가 YAML 형식 (`valid_skill.yaml`). YAML 처리:

- **본 PoC 채택**: stdlib + custom YAML mini-parser (간단한 key-value 파싱만) **또는** 별도 의존 없이 `tests/fixtures/.../valid_skill.yaml` 을 *YAML-shaped JSON-like* 작성 후 `json.loads` 가 처리 가능한 부분집합 사용.
- **대안 1**: `pyyaml` 도입 — 외부 의존 1건 추가, 사용자 명시 풀 3+1 trigger #4 위험 검토 필요.
- **대안 2**: YAML 형식 포기 → JSON 형식 (`valid_skill.json`).

**권고 (본 PoC)**: 대안 2 — fixture 형식을 JSON 으로 통일 (`valid_skill.json` 등). YAML 답습은 G4 §3.1 *문서 표기*만이며, 실 운영 형식 = JSON (G4 §4.2 JSONL = JSON line). 본 PoC fixture YAML 표기는 사용자 명시 directive 답습이므로 그대로 유지하되, scanner 는 simple line-based key-value 파싱 (stdlib 만, no `pyyaml`).

### 2.4 Custom validator 의 본 PoC 답습 책무

| 책무 | 근거 |
|------|------|
| G4 §3.1 17-field schema 직접 정의 (변경 0건) | G4 §3.1 + §3.2 답습 |
| G4 §4.2 11-field JSONL entry validation | `jsonl_hash_chain.validate_schema` import 직접 (Group C 답습) |
| promotion_status 5 enum (`proposed`/`approved`/`promoted`/`archived`/`revoked`) | G4 §3.3 답습 |
| promotion_status transition 규칙 | G4 §3.3 (`proposed → approved → promoted → revoked → archived`) |
| allowed_actions 7 enum (`read`/`write`/`shell`/`network`/`db`/`git`/`docker`) | G4 §3.2 #9 답습 |
| forbidden_actions ∩ allowed_actions = ∅ | G4 §3.2 #10 답습 |
| provider_bindings lock-in marker (`required: true` / `exclusive: true` 표시 금지) | G4 §3.2 #15 (C-K 흡수) 답습 |
| injection canary 26+ regex (prompt injection / unauthorized policy / SQL/cmd/path traversal) | GP-4 §6.3 답습 |
| 2 mode CLI dispatch (external-input / skill-schema) | Group D 답습 |
| violation reporter (file / line / pattern_id / category / detail) | Group A 1차 + Group D 답습 |
| 17-field count 자기 검증 (`--list-skill-fields`) | Group D `--list-patterns` 답습 |

---

## 3. Group C / F 산출물 재사용 (사용자 명시)

### 3.1 import 직접 (리팩토링 0건)

```python
# tools/schema_validator.py
from jsonl_hash_chain import (  # type: ignore[import-not-found]
    REQUIRED_FIELDS,           # 11-field tuple
    ALLOWED_TYPES,             # ("memory", "skill", "meta")
    ALLOWED_SCOPES,            # ("global", "project", "session")
    ALLOWED_AGENTS,            # ("user", "claude-code", "hermes", "external_llm")
    SUPPORTED_SCHEMA_VERSION,  # "0.1"
    validate_schema,           # 11-field schema validation 함수
)
```

### 3.2 답습 분포

| Group E 영역 | Group C/F 답습 | 신규 작성 |
|---|---|---|
| 11-field JSONL schema 검증 | `jsonl_hash_chain.validate_schema` import 직접 | 0 |
| 11-field 정의 (`REQUIRED_FIELDS` + 3 ENUM) | import 직접 | 0 |
| Skill 17-field schema 정의 | — | ~30 줄 (G4 §3.1 직접 복사) |
| promotion_status 5 enum + transition rules | — | ~15 줄 |
| allowed_actions 7 enum + disjoint 검증 | — | ~10 줄 |
| provider_bindings lock-in marker grep | — | ~10 줄 |
| injection canary 26+ regex | — | ~50 줄 (GP-4 §6.3 답습) |
| 2 mode CLI dispatch | — | ~80 줄 (Group D 답습) |
| violation reporter | — | ~30 줄 (Group D 답습) |
| 9 fixture | — | 9 (Group F skill_project.jsonl YAML 재구성 1건 포함) |

**리팩토링 0건 / 복제 0건 / 신규 ~225 줄** (Group D 답습 평균).

### 3.3 Group F skill_project.jsonl YAML 재구성 답습

`tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml` = Group F `tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` entry 3 의 `content` 필드 17-field 를 YAML 형식으로 재구성. 변경 0건 (semantic 동일, 형식만 YAML 표기).

---

## 4. Skill 17-field 검증 기준 (G4 §3.1 답습)

### 4.1 17-field 정의 (변경 0건)

| # | 필드 | 타입 | 필수 | 본 PoC 검증 |
|---|------|-----|----|----------|
| 1 | `id` | string | ✅ 필수 | UUID v4 또는 글로벌 unique slug `[a-z][a-z0-9_-]{2,63}` |
| 2 | `name` | string | ✅ 필수 | 1~100자 length |
| 3 | `version` | string | ✅ 필수 | semver `MAJOR.MINOR.PATCH` regex |
| 4 | `scope` | enum | ✅ 필수 | `global` / `project` / `session` / `team` |
| 5 | `owner` | string | ✅ 필수 | provider lock-in marker grep (`openai`/`anthropic`/`gpt-4`/`claude` 등) |
| 6 | `description` | string | ✅ 필수 | length ≥ 1 |
| 7 | `inputs` | JSON Schema (object) | ✅ 필수 | top-level `type` 또는 `properties` 존재 (재귀 검증 분리) |
| 8 | `outputs` | JSON Schema (object) | ✅ 필수 | top-level `type` 또는 `properties` 존재 |
| 9 | `allowed_actions` | array<string> | ✅ 필수 | enum: `read` / `write` / `shell` / `network` / `db` / `git` / `docker` |
| 10 | `forbidden_actions` | array<string> | MVP-권장 | `allowed_actions` 와 disjoint (∅ 검증) |
| 11 | `required_evidence` | array<evidence_type> | MVP-필수 (C-K) | enum: `test_pass` / `lint` / `secret_scan` / `consensus` / `review` |
| 12 | `required_tests` | array<test_ref> | MVP-권장 | string list |
| 13 | `promotion_status` | enum | ✅ 필수 | `proposed` / `approved` / `promoted` / `archived` / `revoked` (§4.3 transition) |
| 14 | `rollback_triggers` | array<rollback_trigger> | MVP-권장 | enum: `escalation_detected` / `evidence_missing` / `t3_violation` |
| 15 | `provider_bindings` | object | **✅ 필수 (C-K 격상)** | `required: true` / `exclusive: true` 표시 *금지* (lint) |
| 16 | `created_from` | object | MVP-권장 | `task_id` / `commit_sha` / `agent` 키 권장 |
| 17 | `last_verified_at` | ISO 8601 | ✅ 필수 | `YYYY-MM-DDTHH:MM:SSZ` 형식 |

**합산 = 17-field** (필수 12 + MVP-권장 5).

### 4.2 `--list-skill-fields` 자기 검증 형식

```
total=17
  required=12
  mvp_recommended=5
  required_fields=['id', 'name', 'version', 'scope', 'owner', 'description', 'inputs', 'outputs', 'allowed_actions', 'required_evidence', 'promotion_status', 'provider_bindings', 'last_verified_at']
  mvp_recommended_fields=['forbidden_actions', 'required_tests', 'rollback_triggers', 'created_from']
  provider_bindings_required=True (C-K 격상 답습)
  promotion_status_enum=['proposed', 'approved', 'promoted', 'archived', 'revoked']
  allowed_actions_enum=['read', 'write', 'shell', 'network', 'db', 'git', 'docker']
```

> **각주**: `required` 12 + `mvp_recommended` 5 = 17. C-K 흡수에 따라 `required_evidence` 와 `provider_bindings` 가 `required` 로 격상됨 (G4 §3.1 답습).

### 4.3 promotion_status transition 규칙

```
   [proposed] ──── 사용자 승인 (T2) ────→ [approved]
       │                                      │
       │                                      │ Tools 검증 PASS + Evidence
       │                                      ↓
       │                                  [promoted]
       │                                      │
       │                                      │ rollback_trigger 발생
       │                                      ↓
       │                                  [revoked]
       │                                      │
       └─── 사용자 명시 archive ──────────→ [archived]
```

**허용 transitions**:
- `proposed → approved`
- `approved → promoted`
- `promoted → revoked`
- `proposed → archived` (사용자 명시)
- `revoked → archived` (사용자 명시)

**차단**: `proposed → promoted` (approved 우회), `promoted → approved` (역행), 모든 → `proposed` (재진입), 등.

본 PoC 검증 = JSONL chain 내 promotion_status 가 위 매트릭스 외 transition 시 violation. Group F `skill_project.jsonl` 답습 (3 entries: proposed → approved → promoted) = PASS.

---

## 5. JSONL 11-field 검증 기준 (G4 §4.2 답습)

### 5.1 11-field 정의 (Group C `jsonl_hash_chain.py` 직접 답습)

```
type / scope / id / schema_version / ts / agent / event / content /
evidence_refs / prev_hash / hash
```

**enum**:
- `type`: `memory` / `skill` / `meta`
- `scope`: `global` / `project` / `session`
- `agent`: `user` / `claude-code` / `hermes` / `external_llm`
- `event`: 17 enum 후보 (ADR-012 §2.2)

본 PoC 검증 = `jsonl_hash_chain.validate_schema` 함수 직접 호출 (재구현 0건).

### 5.2 본 PoC 의 11-field 적용 영역

| 영역 | 적용 |
|---|---|
| skill_schema PASS fixture (`valid_skill.yaml`) | 17-field 검증 한정 (단일 Skill 정의, 11-field JSONL 미적용) |
| skill_schema FAIL fixture | 17-field 검증 한정 |
| **JSONL 11-field 검증** | **본 PoC = G4 §3.1 17-field 한정**. 11-field 검증은 Group C `jsonl_hash_chain.py` 가 이미 강제 (`tests/fixtures/jsonl_ledger/` + `tests/fixtures/memory_skill_migration/`). 본 PoC 에서 신규 fixture 미작성, *import 직접 답습으로 cross-reference* 만. |

---

## 6. provider_bindings lock-in 차단 기준 (G4 §3.2 #15 C-K 흡수 답습)

### 6.1 검증 규칙

```yaml
provider_bindings:
  # ✅ 정상 형식 — 최소 2 provider 로 재해석 가능
  anthropic: {}
  openai: {}

  # ❌ 차단 — required: true 표시
  anthropic:
    required: true       # ← lock-in marker 차단

  # ❌ 차단 — exclusive: true 표시
  openai:
    exclusive: true      # ← lock-in marker 차단
```

### 6.2 검증 메커니즘

| 메커니즘 | 본 PoC |
|---|---|
| `provider_bindings` 필드 존재 의무 (필수 격상, C-K 답습) | ✅ |
| `required: true` literal grep | ✅ (line-anchored regex) |
| `exclusive: true` literal grep | ✅ |
| 최소 2 provider 재해석 가능성 검증 | ⚠️ 부분 (provider 키 ≥ 1 의무, 2+ 권장 — 본 PoC = warning) |

본 PoC = literal grep 한정. C-H *별도 합의 영역* (depcruise + schema lint 강제) = 별도.

---

## 7. fixture 9건 사양

### 7.1 E-1 PASS × 1 (정상 Worker 출력, FP 검증)

`tests/fixtures/schema_validation/external_input/pass/safe_worker_output.json`:

```json
{
  "task_id": "task-2026-05-10-001",
  "agent": "claude-code",
  "result": "completed",
  "summary": "All tests passed. 100% coverage achieved.",
  "next_step": "ready for review"
}
```

**예상**: rc=0 + 위반 0건 (FP 0).

### 7.2 E-1 FAIL × 4 (4 패턴 cover 강제)

| 파일 | 패턴 cover | canary |
|------|----------|--------|
| `external_input/fail/prompt_injection.txt` | **prompt-injection** | `IGNORE ALL PREVIOUS INSTRUCTIONS` + `<<<SYSTEM:` markers |
| `external_input/fail/unauthorized_policy.json` | **unauthorized-policy** | `{"action": "update ADR-008"}` + `disable Hermes` 등 |
| `external_input/fail/malformed_json.txt` | **malformed-json** | broken JSON syntax (missing brace / unquoted keys) |
| `external_input/fail/injection_payload.json` | **injection-payload** | SQL `'; DROP TABLE`, command `$(whoami)`, path traversal `../../etc/passwd` |

**예상**: rc=1 + ≥4 violations + 4 패턴 cover.

### 7.3 E-2 PASS × 1 (Group F skill_project.jsonl YAML 재구성 답습)

`tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml`:

```yaml
id: skill-tdd-runner
name: TDD Runner
version: 0.1.0
scope: project
owner: user
description: Runs TDD cycle (RED-GREEN-REFACTOR)
inputs:
  type: object
  properties:
    target_file:
      type: string
outputs:
  type: object
  properties:
    passed:
      type: boolean
allowed_actions:
  - shell
  - read
forbidden_actions:
  - network
  - db
required_evidence:
  - test_pass
  - lint
required_tests:
  - tests/test_skill_tdd_runner.py
promotion_status: promoted
rollback_triggers:
  - escalation_detected
  - evidence_missing
provider_bindings:
  anthropic: {}
  openai: {}
created_from:
  task_id: task-poc-group-e
  commit_sha: 1719a01
  agent: user
last_verified_at: 2026-05-10T11:10:00Z
```

**예상**: rc=0 + 17/17 fields 통과 (필수 12 + MVP-권장 5) + provider_bindings 2 키 + lock-in marker 0건.

### 7.4 E-2 FAIL × 4 (4 패턴 cover 강제)

| 파일 | 패턴 cover | violation |
|------|----------|-----------|
| `skill_schema/fail/missing_required.yaml` | **missing-required** | `id` / `name` / `promotion_status` 누락 (필수 12 위반) |
| `skill_schema/fail/invalid_action.yaml` | **invalid-action** | `allowed_actions: [shell, network]` + `forbidden_actions: [shell]` (∩ ≠ ∅) + 또는 enum 외 (`hack` 등) |
| `skill_schema/fail/invalid_promotion_status.yaml` | **invalid-promotion-transition** | `promotion_status: pending` (5 enum 외) 또는 transition 위반 |
| `skill_schema/fail/provider_lockin.yaml` | **provider-lockin (C-K 위반)** | `provider_bindings.openai.required: true` (lock-in marker) |

**예상**: rc=1 + ≥4 violations + 4 패턴 cover.

---

## 8. 검증 매트릭스 (사용자 명시 6 검증 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 예상 결과 |
|---|------|------|------|---------|----------|
| 1 | E-1 PASS | `external_input/pass/` | `python tools/schema_validator.py --mode external-input pass/` | 0 | 위반 0건 (FP 0) |
| 2 | E-1 FAIL | `external_input/fail/` | `python tools/schema_validator.py --mode external-input fail/` | 1 | ≥4 violations + 4 패턴 cover (prompt-injection / unauthorized-policy / malformed-json / injection-payload) |
| 3 | E-2 PASS | `skill_schema/pass/` | `python tools/schema_validator.py --mode skill-schema pass/` | 0 | 17/17 fields 통과 + provider_bindings 2 키 + lock-in marker 0건 |
| 4 | E-2 FAIL | `skill_schema/fail/` | `python tools/schema_validator.py --mode skill-schema fail/` | 1 | ≥4 violations + 4 패턴 cover (missing-required / invalid-action / invalid-promotion-transition / provider-lockin) |
| 5 | 17-field count self-check | `--list-skill-fields` | `python tools/schema_validator.py --list-skill-fields` | 0 | total=17 + required=12 + mvp_recommended=5 + provider_bindings_required=True + promotion_status enum 5 + allowed_actions enum 7 |
| 6 | F-금지 자기 검증 | scanner / fixture / workflow | grep 실 LLM API 호출 / provider SDK import / production data 0건 | 0 | 0 (fake fixture 답습) |

**합산 6 검증** (E-1 PASS/FAIL + E-2 PASS/FAIL + 17-field count + F-금지 grep).

---

## 9. PASS 기준 자기 검증 매트릭스

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | E-1 PASS scan | rc=0 + 위반 0건 |
| 2 | E-1 FAIL scan | rc=1 + ≥4 + 4 패턴 cover |
| 3 | E-2 PASS scan | rc=0 + 17/17 fields 통과 |
| 4 | E-2 FAIL scan | rc=1 + ≥4 + 4 패턴 cover |
| 5 | 17-field count self-check | total=17 (required=12 + mvp_recommended=5) |
| 6 | F-금지 grep | 0건 (실 LLM API / provider SDK / production data 부재) |

**합산 6/6 충족 적격**.

---

## 10. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | Memory boundary 4 금지 runtime 강제 (Memory→policy / Skill→ADR / Session→Global / Hermes→skill 자기 승인) | 사용자 명시 — Group G 영역 (G4 §5) | 별도 합의 |
| 2 | Skill wrapper runtime escalation 차단 (G3 §3.3) | 사용자 명시 — Group G 영역 | 별도 합의 |
| 3 | 재귀 JSON Schema 의미 검증 (`inputs`/`outputs` 재귀) | 사용자 명시 — top-level 형식만 | 별도 합의 |
| 4 | Reviewer Agent 추론적 prompt injection 감지 | Layer 5 (3+1 합의) — GP-4 §6.3 추론적 보조 | 별도 합의 |
| 5 | sqlite bind variable / shlex.quote runtime escape 통합 | runtime hook 영역 | 별도 합의 |
| 6 | 실 LLM API 호출 + 응답 검증 | Layer 0 / runtime | 별도 합의 |
| 7 | pydantic / jsonschema 도구 도입 | 사용자 명시 — stdlib 단독 (Group D 답습) | 별도 합의 (장기 schema 정책 결정 시점) |
| 8 | YAML 처리 라이브러리 (`pyyaml`) 도입 | stdlib 단독 답습 — line-based mini-parser 한정 | 별도 합의 |
| 9 | P9~P12 (prompt injection / evidence forgery / memory poisoning 등) 정식 등록 | 풀 3+1 trigger #5 위험 | 별도 합의 + 외부 LLM 1+ |
| 10 | provider_bindings lint 룰 강제 (depcruise + schema validation) | C-H 별도 합의 영역 (G4 §3.6) | 별도 합의 |
| 11 | Markdown 본문 자기 검출 (Group D 답습 패턴) | CI 는 `tests/fixtures/schema_validation/` 한정 scan 으로 회피 | Group B PoC 사양 §2.8 #1 답습 |

---

## 11. CI workflow 설계

### 11.1 12 step 구조 (Group D/F 답습 형식)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Prepare log directory | `mkdir -p group-e-logs` (Group F 후속 답습 — leading dot 미사용) |
| 4 | 17-field count self-check | `--list-skill-fields` rc=0 + total=17 + required=12 + mvp_recommended=5 + provider_bindings_required=True grep |
| 5 | E-1 PASS — external-input pass/ | rc=0 + 위반 0건 grep |
| 6 | E-1 FAIL — external-input fail/ | rc=1 + ≥4 + 4 패턴 cover (prompt-injection / unauthorized-policy / malformed-json / injection-payload) grep |
| 7 | E-2 PASS — skill-schema pass/ | rc=0 + 17/17 fields 통과 grep |
| 8 | E-2 FAIL — skill-schema fail/ | rc=1 + ≥4 + 4 패턴 cover (missing-required / invalid-action / invalid-promotion-transition / provider-lockin) grep |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 LLM API / provider SDK / production data 0건 grep |
| 10 | Build summary.json | step output 집계 → `group-e-logs/summary.json` |
| 11 | Upload feasibility logs (artifact) | `actions/upload-artifact@v4` `schema-validation-evidence` retention 30일 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-e-logs/`** (Group F 후속 답습 — leading dot 미사용).

### 11.2 paths trigger

```yaml
paths:
  - tools/schema_validator.py
  - tools/jsonl_hash_chain.py     # Group C 모듈 변경 시 trigger (Group F 후속 답습)
  - tests/fixtures/schema_validation/**
  - .github/workflows/schema-validation.yml
```

---

## 12. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 6 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | Memory/Skill schema 자체 변경 필요 | ❌ 미발화 | G4 §3.1 / §4.2 답습만 (변경 0건) |
| 2 | G4 17-field skill schema 변경 필요 | ❌ 미발화 | G4 §3.1 직접 복사 (변경 0건) |
| 3 | provider_bindings 정책 변경 필요 | ❌ 미발화 | C-K 흡수 (필수 + lock-in marker 표시 금지) 답습만 |
| 4 | 외부 입력 검증 기준이 정상 LLM/Worker 출력 흐름을 과도하게 차단 | ⚠️ 부분 위험 | fixture 한정으로 회피, 실 runtime 시 영향 별도 합의 |
| 5 | P9~P12 정식화 필요 | ❌ 미발화 | 본 PoC = canary 검출 한정 (정식 등록 별도 합의) |
| 6 | ADR-011 / ADR-012 / G4 와 충돌 | ❌ 미발화 | cross-reference 답습 한정 |

**합산 0/6 발화 (#4 부분 위험은 fixture 한정으로 통제)** → **Reviewer-only 단축 합의 적격**.

---

## 13. Evidence 형식 (5종 — Group A/B/C/D/F 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g2-gp4-g4-...`) | 본 문서 |
| JSONL ledger entry | summary.json (단순화 — Group D 답습) | summary.json 14 항목 |
| 격리 검증 | fixture 한정 + 실 LLM API 0건 + custom validator 단독 (외부 의존 0건) | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `schema-validation.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g2-gp4-g4-...`) | 본 PoC 산출물 #8 |

---

## 14. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group E 진입 사양 — 사용자 명시 10 금지 / 6 trigger / 6 PASS / 9 fixture / 17-field + 11-field + provider_bindings + promotion_status transition / stdlib 단독 채택. Group A 1차/2차 + Group B + Group C + Group D + Group F 사양 형식 직접 답습. G4 §3.1 17-field + §4.2 11-field + GP-4 §6 답습 (변경 0건). custom validator 단독 채택 (pydantic/jsonschema 0건). artifact path `group-e-logs/` (Group F 후속 답습, leading dot 미사용). Group F `skill_project.jsonl` 17-field content YAML 재구성 답습. |
