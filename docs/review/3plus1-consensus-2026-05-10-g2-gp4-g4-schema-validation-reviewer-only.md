# 3+1 합의 보고서 — G2 GP-4 + G4 Schema Validation (Group E PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group E 진입 — External Input Validation (E-1) + Memory/Skill schema validation (E-2) 통합 PoC)
> **PASS scope**: G2 GP-4 / G4 *형식적 검증 layer 시제* 한정 — **Implementation Pending** (G2 GP-4 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 6 = 0/6 발화 → 단축 적격, 사용자 명시 답습)
> **검토 대상**:
> - `tools/schema_validator.py`
> - `tests/fixtures/schema_validation/{external_input,skill_schema}/{pass,fail}/*`
> - `.github/workflows/schema-validation.yml`
> - `docs/phase0/g2-gp4-g4-schema-validation-poc.md`
> - `.gitignore` (`group-e-logs/` 추가)
> **상위 권위**: ADR-008 부록 C, ADR-011 §2.1 (a)~(e) + §2.3 운영 함의 #1, ADR-012 §2.2 + §3.1 + §3.2, governance-preconditions.md §6 (GP-4), provider-agnostic-memory-skill-design.md §3.1 (17-field) + §3.2 (검증 규칙) + §3.3 (promotion_status) + §4.2 (11-field), implementation-runtime-roadmap.md §3.1 (Order 6 tie)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group D + Group F PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md` 직접 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/schema_validator.py` | ~520 | **stdlib `re` + `json` + `dataclasses` 단독** (외부 의존 0건, pydantic/jsonschema/pyyaml 미도입). 2 mode CLI (`--mode external-input` E-1 / `--mode skill-schema` E-2) + `--list-skill-fields` self-check + 17-field 정의 (G4 §3.1 직접 복사) + 11-field 검증 (`jsonl_hash_chain.validate_schema` import 직접) + injection canary 26 patterns (12 prompt-injection + 8 unauthorized-policy + 6 injection-payload) + ENUM (`ALLOWED_ACTIONS_ENUM` 7 / `PROMOTION_STATUS_ENUM` 5 / `ALLOWED_SCOPE_ENUM` 4) + transition 매트릭스 (G4 §3.3 답습) + provider lock-in marker (`required: true` / `exclusive: true`) + custom YAML mini-parser (stdlib 단독). |
| 2 | `tests/fixtures/schema_validation/external_input/pass/safe_worker_output.json` | 9 lines | E-1 PASS — 정상 Worker 출력 (FP 검증) |
| 3 | `tests/fixtures/schema_validation/external_input/fail/{prompt_injection.txt, unauthorized_policy.json, malformed_json.txt, injection_payload.json}` | 4 fixture | E-1 FAIL — 4 패턴 cover (prompt-injection + unauthorized-policy + malformed-json + injection-payload) |
| 4 | `tests/fixtures/schema_validation/skill_schema/pass/valid_skill.yaml` | 33 lines | E-2 PASS — Group F `skill_project.jsonl` 17-field content YAML 재구성 답습 (필수 12 + MVP-권장 5 모두 포함) |
| 5 | `tests/fixtures/schema_validation/skill_schema/fail/{missing_required, invalid_action, invalid_promotion_status, provider_lockin}.yaml` | 4 fixture | E-2 FAIL — 4 pattern_ids cover (missing-required + invalid-action + invalid-promotion-status + provider-lockin) |
| 6 | `.github/workflows/schema-validation.yml` | ~250 | 12 step (3 setup + 6 검증 + summary.json + artifact + Evidence summary). artifact path = `group-e-logs/` (Group F 후속 답습, leading dot 미사용) |
| 7 | `docs/phase0/g2-gp4-g4-schema-validation-poc.md` | 495 | PoC 사양 (14 섹션 — 목적 / 범위 / 도구 근거 / Group C/F 재사용 / 17-field / 11-field / provider_bindings / fixture / 검증 매트릭스 / PASS 기준 / 한계 / CI 설계 / trigger 6 / Evidence 5 / 변경이력) |
| 8 | 본 합의 보고서 | ~310 | Group A 1차/2차 + Group B + Group C + Group D + Group F Reviewer-only 합의 형식 답습 |

**합산 = 8 파일** (Group D/F 답습 평균).

### 1.2 fixture 9건 검증 결과

| Fixture | 위치 | rc | 매칭 패턴 |
|---|---|---|---|
| `safe_worker_output.json` | external_input/pass/ | 0 | 0 (FP 0) |
| `prompt_injection.txt` | external_input/fail/ | (집계) | prompt-injection × 9 |
| `unauthorized_policy.json` | external_input/fail/ | (집계) | unauthorized-policy × 6 |
| `malformed_json.txt` | external_input/fail/ | (집계) | malformed-json × 1 |
| `injection_payload.json` | external_input/fail/ | (집계) | injection-payload × 6 |
| `valid_skill.yaml` | skill_schema/pass/ | 0 | 0 (17/17 fields 통과) |
| `missing_required.yaml` | skill_schema/fail/ | (집계) | missing-required × 9 (id/scope/owner/inputs/outputs/allowed_actions/promotion_status/provider_bindings/last_verified_at) |
| `invalid_action.yaml` | skill_schema/fail/ | (집계) | invalid-action × 2 |
| `invalid_promotion_status.yaml` | skill_schema/fail/ | (집계) | invalid-promotion-status × 1 |
| `provider_lockin.yaml` | skill_schema/fail/ | (집계) | provider-lockin × 4 |

### 1.3 Pattern 등록 확인 (`--list-skill-fields` 출력)

```
total=17
  required=12
  mvp_recommended=5
  required_fields=['id', 'name', 'version', 'scope', 'owner', 'description', 'inputs', 'outputs', 'allowed_actions', 'promotion_status', 'provider_bindings', 'last_verified_at']
  mvp_recommended_fields=['forbidden_actions', 'required_evidence', 'required_tests', 'rollback_triggers', 'created_from']
  provider_bindings_required=True (C-K 격상 답습)
  promotion_status_enum=['proposed', 'approved', 'promoted', 'archived', 'revoked']
  allowed_actions_enum=['read', 'write', 'shell', 'network', 'db', 'git', 'docker']
  scope_enum=['global', 'project', 'session', 'team']
  jsonl_11_field_required=['type', 'scope', 'id', 'schema_version', 'ts', 'agent', 'event', 'content', 'evidence_refs', 'prev_hash', 'hash']
  schema_total_compliant=True
```

### 1.4 E-1 / E-2 로컬 검증 결과 (6/6 PASS)

| # | 검증 | 명령 | rc | 결과 |
|---|------|------|-----|------|
| 1 | E-1 PASS | `--mode external-input pass/` | **0** | 위반 0건 (FP 0) |
| 2 | E-1 FAIL | `--mode external-input fail/` | **1** | 22 violations + **4 카테고리 cover** (prompt-injection + unauthorized-policy + malformed-json + injection-payload) |
| 3 | E-2 PASS | `--mode skill-schema pass/` | **0** | 17/17 fields 통과 (FP 0) |
| 4 | E-2 FAIL | `--mode skill-schema fail/` | **1** | 16 violations + **4 pattern_ids cover** (missing-required + invalid-action + invalid-promotion-status + provider-lockin) |
| 5 | 17-field count | `--list-skill-fields` | **0** | total=17 + required=12 + mvp_recommended=5 + provider_bindings_required=True + schema_total_compliant=True |
| 6 | F-금지 grep | scanner + fixture grep | **0** | 실 LLM API / provider SDK / production data 0건 |

### 1.5 CI workflow 12 step 구조

| # | Step | 책무 | 검증 |
|---|------|------|------|
| 1 | Checkout | actions/checkout@v4 | — |
| 2 | Set up Python | actions/setup-python@v5 (3.12) | — |
| 3 | Prepare log directory | `mkdir -p group-e-logs` (leading dot 미사용) | — |
| 4 | 17-field count self-check | `--list-skill-fields` rc=0 + total=17 + required=12 + mvp_recommended=5 + provider_bindings_required=True + schema_total_compliant=True grep | §1.4 #5 |
| 5 | E-1 PASS | rc=0 + violations=0 grep | §1.4 #1 |
| 6 | E-1 FAIL | rc=1 + 4 카테고리 cover grep | §1.4 #2 |
| 7 | E-2 PASS | rc=0 + violations=0 grep | §1.4 #3 |
| 8 | E-2 FAIL | rc=1 + 4 pattern_ids cover grep | §1.4 #4 |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 LLM API / provider SDK / production data 0건 grep | §1.4 #6 |
| 10 | Build summary.json | step output 집계 → `group-e-logs/summary.json` 16 항목 | — |
| 11 | Upload artifact | `actions/upload-artifact@v4` `schema-validation-evidence` retention 30일 | Group F 후속 답습 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` 14 항목 | R-6 답습 |

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | G4 §3.1 17-field + §4.2 11-field + GP-4 §6.3 injection canary 26 patterns 직접 답습 (변경 0건) |
| (b) 격리 환경 PoC 실증 | ✅ | fixture 한정 (실 LLM API 0건, fake injection payload) + 외부 의존 0건 (stdlib 단독) + CI ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / ADR-011 §2.1 + §2.3 / ADR-012 §2.2 / GP-4 §6 / G4 §3 + §4.2 / roadmap §3.1 cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 12 step + paths trigger 4 영역 + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 6 (사양 §9 답습)

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | E-1 PASS scan | ✅ | rc=0 + 위반 0건 (FP 0) |
| 2 | E-1 FAIL scan | ✅ | rc=1 + 22 violations + 4 카테고리 cover |
| 3 | E-2 PASS scan | ✅ | rc=0 + 17/17 fields 통과 |
| 4 | E-2 FAIL scan | ✅ | rc=1 + 16 violations + 4 pattern_ids cover |
| 5 | 17-field count self-check | ✅ | total=17 + required=12 + mvp_recommended=5 + provider_bindings_required=True + schema_total_compliant=True |
| 6 | F-금지 grep | ✅ | 실 LLM API / provider SDK / production data 0건 |

**합산 6/6 충족.**

### 2.3 사용자 명시 10 금지 자기 검증 (0/10 위반)

| # | 금지 | 위반 | 근거 |
|---|------|----|------|
| 1 | G2 GP-4 최종 PASS 선언 | 0 | 본 PoC = *형식적 검증 layer 시제* 한정 (사양 §0 + §1.2 명시) |
| 2 | G4 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 (meta 갱신 시 *부분 충족 시제* 한정) |
| 3 | G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | 0 | 변경 0건 |
| 4 | Hermes PMO 격상 선언 | 0 | 변경 0건 |
| 5 | 실 LLM API 호출 | 0 | scanner 본문 `openai.` / `anthropic.` / `completions.create` 0건 — F-금지 grep step 자동 강제 |
| 6 | 실 provider SDK 호출 | 0 | scanner 본문 `import (openai\|anthropic\|google.generativeai\|litellm\|ollama)` 0건 |
| 7 | production memory/skill 데이터 사용 | 0 | fixture 한정 (`tests/fixtures/schema_validation/`), `~/.claude/` / `production_` 패턴 0건 |
| 8 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/` 본문 변경 0건 (cross-reference 답습 한정) |
| 9 | Memory boundary hook 구현 | 0 | Group G 영역 (G4 §5 4 금지 runtime 강제) — 본 PoC 미진입 |
| 10 | Skill wrapper 구현 | 0 | Group G 영역 (G3 §3.3 escalation 차단) — 본 PoC 미진입 |

**합산 0/10 위반.**

### 2.4 사용자 명시 풀 3+1 승격 trigger 6 자기 검증 (0/6 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | Memory/Skill schema 자체 변경 필요 | 0 | G4 §3.1 / §4.2 답습만 (변경 0건) |
| 2 | G4 17-field skill schema 변경 필요 | 0 | G4 §3.1 직접 복사 (변경 0건) |
| 3 | provider_bindings 정책 변경 필요 | 0 | C-K 흡수 (필수 + lock-in marker 표시 금지) 답습만 |
| 4 | 외부 입력 검증 기준이 정상 LLM/Worker 출력 흐름 과도 차단 | ⚠️ 부분 위험 (fixture 한정으로 회피) | safe_worker_output.json PASS 검증 — 정상 흐름 미차단 |
| 5 | P9~P12 정식화 필요 | 0 | 본 PoC = canary 검출 한정 (정식 등록 별도 합의) |
| 6 | ADR-011 / ADR-012 / G4 와 충돌 | 0 | cross-reference 답습 한정 |

**합산 0/6 발화** → **Reviewer-only 단축 합의 적격**.

### 2.5 G4 §3.1 + §4.2 답습 충실도

| 영역 | G4 답습 방식 | 신규 작성 |
|---|---|---|
| 17-field 정의 (필수 12 + MVP-권장 5) | G4 §3.1 직접 복사 | 0 |
| 필드별 검증 규칙 (UUID/slug/semver/scope enum/...) | G4 §3.2 답습 | 0 |
| promotion_status 5 enum + transition 매트릭스 | G4 §3.3 답습 | 0 |
| allowed_actions 7 enum | G4 §3.2 #9 답습 | 0 |
| forbidden_actions disjoint | G4 §3.2 #10 답습 | 0 |
| provider_bindings C-K 격상 + lock-in marker | G4 §3.2 #15 답습 | 0 |
| 11-field schema 검증 | `jsonl_hash_chain.validate_schema` import 직접 (Group C) | 0 |
| Group F skill_project.jsonl 17-field content YAML 재구성 | Group F PASS fixture 답습 | 0 (semantic 동일, 형식만 YAML) |
| Custom validator 본 PoC 신규 (~520줄) | — | 2 mode CLI + injection canary 26 patterns + custom YAML mini-parser + violation reporter + field validator |
| 9 fixture | — | 9 |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건** (pydantic/jsonschema/pyyaml 미도입).

### 2.6 Group A/B/C/D/F 답습 충실

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + 2 mode + `--list-*` self-check) | Group A 1차 + Group D + Group F |
| Fixture 디렉토리 구조 (PASS / FAIL 분리) | Group A 1차 + Group D |
| CI workflow 12 step (4 mode + count self-check + F-금지 grep + summary.json + artifact + Evidence summary) | Group D 직접 답습 |
| Reviewer-only 단축 합의 형식 | Group A 1차 + Group B + Group D + Group F |
| **artifact path (leading dot 미사용)** | **Group F 후속 + Group D (group-e-logs/) 직접 답습** |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group D + Group F |

### 2.7 17-field schema 검증 책무 분담 (사양 §4 답습)

| 영역 | E-2 (G4) | 분리 영역 |
|------|------------|----------|
| Skill 17-field 형식 검증 | ✅ | — |
| 11-field JSONL entry 검증 | ✅ (Group C reuse) | — |
| inputs / outputs JSON Schema top-level 형식 | ✅ (object 여부만) | 재귀 의미 검증 = 별도 |
| Memory boundary 4 금지 runtime 강제 | ❌ | Group G 영역 |
| Skill wrapper escalation 차단 | ❌ | Group G 영역 |
| pydantic / jsonschema 도구 도입 | ❌ | 별도 합의 |

### 2.8 책무 분리 — 별도 합의 영역

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| Memory boundary 4 금지 runtime 강제 (Memory→policy / Skill→ADR / Session→Global / Hermes→skill 자기 승인) | 사용자 명시 — Group G 영역 (G4 §5) | 별도 합의 |
| Skill wrapper runtime escalation 차단 (G3 §3.3) | 사용자 명시 — Group G 영역 | 별도 합의 |
| 재귀 JSON Schema 의미 검증 (`inputs`/`outputs` 재귀) | 사용자 명시 — top-level 형식만 | 별도 합의 |
| Reviewer Agent 추론적 prompt injection 감지 | Layer 5 (3+1 합의) — GP-4 §6.3 추론적 보조 | 별도 합의 |
| sqlite bind variable / shlex.quote runtime escape 통합 | runtime hook 영역 | 별도 합의 |
| 실 LLM API 호출 + 응답 검증 | Layer 0 / runtime | 별도 합의 |
| pydantic / jsonschema / pyyaml 도구 도입 | 사용자 명시 — stdlib 단독 (Group D 답습) | 별도 합의 |
| P9~P12 정식 등록 (prompt injection / evidence forgery / memory poisoning) | 풀 3+1 trigger #5 위험 | 별도 합의 + 외부 LLM 1+ |
| provider_bindings lint 룰 강제 (depcruise + schema validation) | C-H 별도 합의 영역 (G4 §3.6) | 별도 합의 |

### 2.9 알려진 한계 (사양 §10 답습)

1. **Memory boundary 4 금지 runtime 강제 미구현** — Group G 영역 (G4 §5).
2. **Skill wrapper runtime escalation 차단 미구현** — Group G 영역 (G3 §3.3).
3. **재귀 JSON Schema 의미 검증 미커버** — top-level `type` / `properties` 존재만.
4. **Reviewer Agent 추론적 prompt injection 감지 미통합** — Layer 5 (3+1 합의).
5. **runtime escape (sqlite bind / shlex.quote) 미통합**.
6. **실 LLM API 호출 0건** — fixture 한정.
7. **pydantic / jsonschema 도구 미도입** — stdlib 단독 (Group D 답습).
8. **YAML 라이브러리 (`pyyaml`) 미도입** — custom mini-parser 한정.
9. **P9~P12 정식 등록 0건** — 본 PoC = canary 검출 한정.
10. **provider_bindings lint 룰 강제 미통합** — C-H 별도 합의 영역.
11. **Markdown 본문 자기 검출** (Group D 답습 패턴) — CI 는 `tests/fixtures/schema_validation/` 한정 scan 으로 회피.

### 2.10 책무 분담 매트릭스 (사양 §0 답습)

| 영역 | E-1 (GP-4) | E-2 (G4) | 분리 영역 |
|------|------------|------------|----------|
| 외부 입력 schema 검증 | ✅ external-input mode | — | — |
| injection canary 정적 검출 | ✅ 26 patterns | — | — |
| Skill 17-field 검증 | — | ✅ skill-schema mode | — |
| 11-field JSONL 검증 | — | ✅ (Group C reuse) | — |
| provider_bindings lock-in marker | — | ✅ | C-H 별도 합의 (lint 룰 강제) |
| Memory boundary 4 금지 runtime | ❌ | ❌ | Group G 영역 |
| Skill wrapper escalation 차단 | ❌ | ❌ | Group G 영역 |
| Reviewer Agent 추론 layer | ❌ | ❌ | Layer 5 별도 합의 |

---

## 3. 풀 3+1 승격 trigger 6 자기 검증 (재명시)

§2.4 와 동일 — 0/6 미발화. **Reviewer-only 단축 합의 적격 (사용자 명시 답습)**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ G4 §3.1 17-field Skill schema + §4.2 11-field JSONL entry schema 의 *정적 검증* 운영 적용 첫 시제
- ✅ GP-4 §6 외부 입력 검증의 *형식적 layer* 첫 시제 (injection canary 26 patterns)
- ✅ Custom validator 단독 채택 (pydantic/jsonschema/pyyaml 미도입) 답습 검증
- ✅ Group F `skill_project.jsonl` 17-field content YAML 재구성 답습 검증
- ✅ Group F 후속 artifact path 답습 (`group-e-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A/B/C/D/F)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G2 GP-4 최종 Implementation/Runtime PASS 선언
- ❌ G4 전체 Implementation/Runtime PASS 선언
- ❌ G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ G4 17-field schema 변경 (답습만)
- ❌ G4 11-field schema 변경 (답습만)
- ❌ provider_bindings 정책 변경 (C-K 흡수 답습만)
- ❌ Memory boundary 4 금지 runtime 강제 (Group G 영역)
- ❌ Skill wrapper runtime escalation 차단 (Group G 영역)
- ❌ 실 LLM API / provider SDK / 외부 API 호출 / production data 사용
- ❌ pydantic / jsonschema / pyyaml 도구 도입

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group E PoC = G2 GP-4 / G4 *형식적 검증 layer 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, 10 금지 0/10 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 6/6 충족, 로컬 6/6 검증 PASS, CI workflow 12 step 형식 검증 PASS, G4 §3.1 + §4.2 직접 답습 (변경 0건 / 외부 의존 0건)).

### 5.2 추가 조건 (C-E-1 ~ C-E-7)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-E-1 | 본 PoC = G2 GP-4 / G4 *형식적 검증 layer 시제* 한정 — G2 GP-4 / G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.3 #1~#4 명시 |
| C-E-2 | Memory boundary 4 금지 runtime 강제 + Skill wrapper escalation 차단 = Group G 영역 (별도 합의) | 사양 §1.2 + §10 #1~#2 + 본 합의 §2.8 명시 |
| C-E-3 | 재귀 JSON Schema 의미 검증 = top-level 형식만, 재귀 의미 검증 별도 | 사양 §10 #3 + 본 합의 §2.7 명시 |
| C-E-4 | pydantic / jsonschema / pyyaml 도입 = 장기 schema 정책 결정 시점 별도 합의 (풀 3+1 trigger #4 위험) | 사양 §2.1 + §10 #7~#8 + 본 합의 §2.5 명시 |
| C-E-5 | P9~P12 정식 등록 = 별도 합의 + 외부 LLM 1+ (풀 3+1 trigger #5 위험) | 사양 §10 #9 + 본 합의 §2.4 #5 명시 |
| C-E-6 | provider_bindings lint 룰 강제 = C-H 별도 합의 영역 (G4 §3.6) | 사양 §10 #10 + 본 합의 §2.8 명시 |
| C-E-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §14 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (PoC 본문 / CI workflow / 사양 / 합의 / .gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습 — Group A/B/C/D/F 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group G (G3 Skill escalation 차단 + 합의 자기참조 차단 + G4 Memory boundary hook) — 단축 합의 + PoC
   - (b) Group A 3차 — URL/endpoint grep PoC (C-8) — 풀 3+1
   - (c) Group F 후속 — `hermes_to_openai` 또는 Skill 변환 feasibility 추가
   - (d) Group C 후속 — `history_rewrite` Layer 5 PoC (ADR-012 §2.8)
   - (e) cross-vendor LLM 의뢰 (Group D 또는 Group E 산출물)
   - (f) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)
   - (g) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group E 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 6 0/6 발화, 10 금지 0/10 위반, PASS 기준 6/6 + ADR-011 §2.1 5/5 충족, 로컬 6/6 PASS, CI workflow 12 step 형식 검증 PASS, G4 §3.1 + §4.2 직접 답습 (변경 0건 / 외부 의존 0건). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C/D/F 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
