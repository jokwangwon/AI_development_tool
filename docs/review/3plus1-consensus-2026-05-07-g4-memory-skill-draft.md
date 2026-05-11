# 단축 검토 보고서 (Reviewer-only): G4 Provider-agnostic Memory / Skill DRAFT 채택 적격성

**날짜**: 2026-05-07
**검증 대상**: `docs/architecture/provider-agnostic-memory-skill-design.md` (DRAFT 시점 산출 — 작성일 2026-05-07 기준)
**합의 형태**: 단축 검토 (Reviewer-only) — DRAFT 적격성 한정
**상위 권위**: 헌법 5조 (관용 — Provider Liquidity), 헌법 8조 (보안), ADR-008 차단조건 #2 (JSONL export 표준), ADR-011 §2.3 (권위 위계 영구 권위), ADR-011 §2.4 (T1/T2/T3), `feedback_provider_liquidity.md` (Provider Liquidity 비협상 설계 제약), system-identity-prequel §3 / §6.3 / §8.4 (권위 위계 prequel + Evidence Ledger schema 후보 + Memory 2단계 boundary)
**관련 evidence**:
- G4 초안 본문 (옵션 B — Memory + Skill 통합 단일 문서, 사용자 명시 결정 답습)
- P2 v3 DRAFT 단축 검토 결과 (`docs/review/3plus1-consensus-2026-05-07-p2-v3-draft.md`, APPROVE AS DRAFT)
- G2 DRAFT 단축 검토 결과 (`docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md`, APPROVE AS DRAFT)
- G3 DRAFT 단축 검토 결과 (`docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md`, APPROVE AS DRAFT)
- G1b PASS evidence (R-7 SOP §7.3 단축 합의, 2026-05-07)
- system-identity-prequel §8.4 (Memory 2단계 채택 + Skill 자동 추출 T1 한정 + GPT 4단계 미채택 사유)
- 합의 §103 (Memory 2단계 + Skill 자동 추출 T1 한정) / 합의 §164 (Skill schema 17 필드 첫 명시)

**사용자 명시 결정**:
- G4 DRAFT 적격 검토 → APPROVE 시 별도 commit → G2/G3/G4 정식 채택 합의 준비 진입
- 본 검토는 *DRAFT 적격성* 한정 — G4 PASS / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 runtime 코드 / 실 migration script 모두 자동 트리거 금지

---

## 1. 사전 점검 — 검토 가동 정당성

### 1.1 가동 사유

본 G4 초안은 다음 입력을 흡수한 신규 산출:
- 헌법 5조 (Provider Liquidity 관용) + `feedback_provider_liquidity.md` 영구 권위
- ADR-008 차단조건 #2 (JSONL export 표준)
- ADR-011 §2.3 (권위 위계) + §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
- system-identity-prequel §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary) — 본 G4 답습 권위 발행으로 prequel archive 후 권위 보존
- 합의 §103 (Memory 2단계 + Skill 자동 추출 T1) + 합의 §164 (Skill schema 17 필드)
- P2 v3 DRAFT §6 (G4 정의 요청)
- G2 DRAFT §8 GP-6 (Memory/Skill Migration 가능성 — *형식 제공* 의무를 G4 에 위임)
- G3 DRAFT §6.5 / §7 (Memory / Skill *권한* 의무를 G3 에 위임 + G4 *형식* 책임 경계)

본 초안은 DRAFT 상태이며, 본 검토는 *DRAFT 적격성*을 확인하여 G2/G3/G4 정식 채택 합의 준비 진입 가능 여부를 판정한다. 검토 범위 한정:
- 사용자 명시 13 기준 충족 여부
- 9 금지 항목 위반 0건 확인
- DRAFT 상태 적격 + G2/G3/G4 정식 채택 합의 준비 진입 적격 여부

### 1.2 단축 검토 채택 사유

- 본 G4 초안 작업은 *권위 흡수 + 형식 정의*이며 새 권위 결정 0건 (ADR-008 차단조건 #2 답습 + system-identity-prequel §8.4 흡수 + 합의 §103/§164 답습)
- G4 PASS 합의는 본 검토 비대상 — 후속 PoC + (a)~(e) 충족 검증 + **격상 통합 합의 시 외부 LLM 1+ 권장 또는 필수** (G3 §4.4.2 답습 + G4 §0.3 #4)
- 직전 P2 v3 / G2 / G3 DRAFT 검토 (Reviewer-only, APPROVE AS DRAFT) 패턴 답습
- ADR-011 §2.4 T2 분류 (사용자 승인 기반 진행)

### 1.3 본 검토 자체의 메타 편향 인지 (선행)

**중요**: G4 는 *Provider Liquidity* 의 *형식 차원* 보장 — *공통 schema + JSONL + hash chain* 의 *원안* 자체를 첫 명시한 문서. 본 검토자(Reviewer)는 G4 초안 작성자와 동일 컨텍스트 → **자기참조 + 메타 편향 위험**.

본 §1.3 은 이를 명시 인지하며, §5 메타 편향 자기진단에서 다음을 통제:
- 본 검토는 *DRAFT 적격성* 한정 (G4 PASS 적격성 아님)
- §3.1 17 필드 schema 자체의 *적정성 검증* 은 외부 LLM 시야 또는 PoC 실증을 통해 보강 의무 — 본 검토 범위 외
- §4.4 canonical JSON / hash chain 사양의 *적정성 검증* 도 동일 — 본 Reviewer 시야 한계 명시

### 1.4 검토 비대상 (본 검토가 *판정하지 않는* 것)

- ❌ G4 PASS 적격성 — §1 ~ §8 각각 (a)~(e) Exit 기준 충족 검증 + 합의 (외부 LLM 권장)
- ❌ G2 / G3 PASS 적격성 — 별도 합의
- ❌ Hermes PMO 격상 적격성 — 4 게이트 통과 후 별도 결정 (외부 LLM 1+ 권장 또는 필수)
- ❌ P2 v3 정식 채택 적격성 — G2/G3/G4 완료 후 별도 합의
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 적격성
- ❌ P2 v2 / system-identity-prequel.md archive 처리 적격성
- ❌ 실 runtime 코드 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 등) 적격성
- ❌ 실 migration script (`scripts/hermes-migration/*.py`) 적격성
- ❌ Tier-2 / Tier-3 Skill catalog 확장 적격성

---

## 2. 13 기준 점검 (사용자 명시)

### 2.1 기준 #1 — Provider-agnostic Memory / Skill 형식의 정의 충실성

**확인 결과**: ✅ PASS

| 형식 측면 | G4 초안 위치 | 충실성 |
|------|---------|----|
| G4 정체성 (형식 / schema / export-import) | §1.1 + §1.3 위계 표 | ✅ G3 (권한) / GP-6 (가능성) 와의 분리 명시 |
| 옵션 B 통합 단일 문서 채택 사유 | §1.2 | ✅ Memory/Skill 공통 schema 보장 + lock-in 방지 통일 |
| Memory + Skill 통합 schema 영역 | §2 (Memory) + §3 (Skill) + §4 (공통 JSONL) | ✅ 형식 분리 명확 |
| 위계 답습 (Constitution > ADR > SDD > Harness Gates > Hermes > Worker) | §1.3 + §9 영구 핵심 제약 | ✅ ADR-011 §2.3 인용 |

→ Criterion 1 PASS, *G4 = 형식 / schema / export-import* 정체성 충실. G3 (권한) ↔ G4 (형식) ↔ GP-6 (가능성) 3-way 분리 일관.

### 2.2 기준 #2 — Memory Scope 4 단계 명확성

**확인 결과**: ✅ PASS

| Scope | 정의 | Owner | 본 초안 위치 |
|----|---|----|------|
| **Global** | cross-project 보편 원칙 / 패턴 / 헌법-동급 제약 | 사용자 (manual approval) | §2.1 + §2.2.1 |
| **Project** | 프로젝트별 목표 / 결정 / 반복 버그 / 도메인 용어 | 사용자 (manual approval) | §2.1 + §2.2.2 |
| **Session** | 본 세션 작업 추적 / 임시 결정 / 직전 상태 | Hermes (자동 기록) + 사용자 (review) | §2.1 + §2.3 |
| **Team/Agent** | Worker Agent 별 강점 / 실패 패턴 | 사용자 | §2.1 + §2.4 |

→ Criterion 2 PASS, 4 단계 모두 *목적 + Owner + 저장 가능/금지 + Promotion / Expiration / Export* 측면 명시.

### 2.3 기준 #3 — MVP 범위가 Global + Project 로 제한

**확인 결과**: ✅ PASS

| MVP 적용 | Scope | 본 초안 위치 |
|------|----|---------|
| ✅ MVP | Global / Project | §2.1 + §2.2.1 / §2.2.2 |
| ⏳ 후속 | Session / Team-Agent | §2.1 + §2.3 / §2.4 (보류, 후속 진입 조건 명시) |

MVP 채택 사유 (system-identity-prequel §8.4 + 합의 §103 답습) 도 §2.1 직하에서 명시 — Global + Project 2 단계가 충분 (3 Agent 명시 + GPT 4 단계 미채택).

→ Criterion 3 PASS, MVP 범위 Global + Project 만 명시 + 명확 enumeration.

### 2.4 기준 #4 — Session / Team-Agent Memory 가 후속 단계로 분리

**확인 결과**: ✅ PASS

| Scope | 보류 사유 | 후속 진입 조건 | 본 초안 위치 |
|----|--------|---------|---------|
| Session | 별도 scope 도입 시 이중 저장 + 정량 트리거 (파생 프로젝트 ≥ 3건) 미충족 + `docs/sessions/SESSION_*.md` 로 현 단계 충족 | 별도 ADR + 사용자 명시 결정 | §2.3.1 |
| Team / Agent | 정량 트리거 (파생 프로젝트 ≥ 3건 + 외부 도구로 부족한 기능 명확 식별) 미충족 | 별도 ADR + 정량 트리거 충족 + 사용자 명시 결정 | §2.4.1 |

후속 진입 시 사양 *예고만* (정식 정의 X) — §2.3.2 + §2.4.2. 본 초안은 *예고만* 정확.

→ Criterion 4 PASS, 정량 트리거 + 별도 ADR 의존 명시. 본 초안에서 정의 진입 0건.

### 2.5 기준 #5 — Skill schema 17 필드의 provider-neutral 정의

**확인 결과**: ✅ PASS

§3.1 + §3.2 17 필드 enumeration 점검:

| # | 필드 | 타입 | 필수 | Provider Lock-in 위험 |
|---|----|---|----|----------------|
| 1 | `id` | string | ✅ | 0 (자체 식별자) |
| 2 | `name` | string | ✅ | 0 |
| 3 | `version` | semver | ✅ | 0 |
| 4 | `scope` | enum (global/project/session/team) | ✅ | 0 |
| 5 | `owner` | string (provider-neutral identifier) | ✅ | 0 (provider 명시 금지 §3.2) |
| 6 | `description` | markdown | ✅ | 0 |
| 7 | `inputs` | JSON Schema | ✅ | 0 (JSON Schema = 표준) |
| 8 | `outputs` | JSON Schema | ✅ | 0 |
| 9 | `allowed_actions` | array (권한 등급 enum) | ✅ | 0 |
| 10 | `forbidden_actions` | array | 권장 | 0 |
| 11 | `required_evidence` | array (evidence_type) | 권장 | 0 |
| 12 | `required_tests` | array (test_ref) | 권장 | 0 |
| 13 | `promotion_status` | enum (proposed/approved/promoted/revoked/archived) | ✅ | 0 |
| 14 | `rollback_triggers` | array | 권장 | 0 |
| 15 | `provider_bindings` | object | 권장 | ⚠️ 주의 (lock-in 핵심 영역, §3.5 검증 규칙) |
| 16 | `created_from` | object (task_id / commit_sha / agent) | 권장 | 0 |
| 17 | `last_verified_at` | ISO 8601 | ✅ | 0 |

`owner` 필드는 *user identifier 또는 agent identifier (provider-neutral)* — provider 명시 금지 (§3.2). 17 필드 중 16건 Provider Lock-in 위험 0, #15 `provider_bindings` 만 주의 영역 + §3.5 검증 규칙으로 차단.

→ Criterion 5 PASS, 17 필드 enumeration + 각 필드별 검증 규칙 + Provider Lock-in 위험 평가 명시. (필드 적정성 검증은 후속 합의 또는 외부 LLM 시야 — §11.1 자기 한계 명시 답습)

### 2.6 기준 #6 — `provider_bindings` 가 lock-in 이 아니라 optional optimization 으로 제한

**확인 결과**: ✅ PASS

§3.5 검증 규칙 점검:

| 검증 규칙 | 본 초안 위치 | 강제 |
|--------|---------|---|
| `provider_bindings` 의 어떤 provider 도 *required* 또는 *exclusive* 표시 금지 | §3.5 | ✅ 명시 |
| 모든 binding 은 *optional optimization* 한정 | §3.5 + §3.1 표 | ✅ 명시 |
| 최소 2 provider 로 재해석 가능 (claude / openai / ollama 중 2+) | §3.5 + §4.3 | ✅ 명시 |
| Provider 종속 endpoint / SDK / 모델명 분기는 Skill 본문에 작성 금지 | §3.5 (G2 GP-5 + G3 §6.4 답습) | ✅ 위임 명시 |

OK 예시 + 금지 예시 (claude required + custom_endpoint 형식) §3.5 직접 yaml 명시 — 명확.

→ Criterion 6 PASS, optional optimization 한정 + required/exclusive 금지 명문화 + 예시 + 검증 규칙 4건 enumeration.

### 2.7 기준 #7 — JSONL export/import 형식이 Hermes 내부 DB 없이도 해석 가능

**확인 결과**: ✅ PASS

§4.3 Hermes 의존 0 보장 점검:

| 검증 항목 | 메커니즘 | 본 초안 위치 |
|------|------|---------|
| Hermes 의존 import 0건 | `scripts/hermes-migration/` 변환 스크립트가 `import hermes_agent` 등 의존 0건 (depcruise — G2 GP-5 답습) | §4.3 + §4.5.2 |
| 표준 도구로 검증 가능 | `jq` parse + sha256 검증 + canonical JSON 검증 (POSIX 표준) | §4.3 |
| schema_version 호환성 | 본 `0.1` 이외 버전은 명시 declaration 후만 import 가능 | §4.3 + §4.5 |
| 외부 오케스트레이터 import 가능 | claude / openai / gemini / local LLM 등 최소 2+ 재해석 가능 | §4.3 + §3.5 + GP-6 답습 |

JSONL schema 10 필드 (§4.2) — `type` / `scope` / `id` / `schema_version` / `ts` / `agent` / `content` / `evidence_refs` / `prev_hash` / `hash` 모두 provider-neutral 강제 (§4.3).

→ Criterion 7 PASS, Hermes 의존 0 + POSIX 표준 도구 + 최소 2+ provider 재해석 = *완결*.

### 2.8 기준 #8 — hash chain / canonical JSON / migration 가능성 명시

**확인 결과**: ✅ PASS

| 측면 | 본 초안 위치 | 충실성 |
|----|---------|----|
| Hash chain | §4.4 — `prev_hash` chain 형성 + canonical JSON sha256 + genesis_hash 정의 + append-only + entry 수정/삭제/재작성 T3 금지 | ✅ 5 메커니즘 |
| Canonical JSON | §4.4 — lex sort + RFC 8259 escape + IEEE 754 numeric 명시 | ✅ 기본 명시 (RFC 8785 JCS 직접 인용은 §11.1 자기 한계 + 정식 채택 시 권고) |
| Migration script 사양 | §4.5 — 4 변환 스크립트 후보 (hermes_to_claude / hermes_to_openai / hermes_to_ollama / import) + 변환 스크립트 사양 요건 5 항목 | ✅ 사양까지 (실 구현 §0.2 #8) |
| 라운드트립 검증 절차 | §4.6 — 흐름도 + PASS 조건 2 (hash 일치 OR 의미 보존) | ✅ 절차 정의 |

§11.1 자기 한계: "§4.4 canonical JSON 정의 — JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고." — 본 초안 자체가 *자기 발견* + 후속 권고 명시.

→ Criterion 8 PASS, 3 측면 모두 명시 + RFC 8785 JCS 정식 채택 시 보강 권고 자기 명시.

### 2.9 기준 #9 — Memory / Skill boundary 명확성

**확인 결과**: ✅ PASS

§5.1 정의 + 예시 점검:

| 분류 | 정의 | 예시 |
|---|---|---|
| Memory | 사실 / 결정 / 선호 / 상태 / 근거 | "Python 3.11", "한국어 소통", "G1b PASS 2026-05-07", "헌법 5조 = 관용" |
| Skill | 반복 가능한 절차 / 입력 / 출력 / 권한 / 검증 조건 | "PR 생성 스크립트 (input=branch, output=URL, action=git)", "테스트 실행 절차" |

핵심 차이 (§5.1):
- Memory = *상태 / 지식* — 시점-의존, 사실 누적
- Skill = *절차 / 행위* — 반복 가능, 입력-출력 명세

본 §5 가 *하지 않는* 것 (§5.3): ❌ 세부 구별 매트릭스 (사용자 review 영역) / ❌ Memory ↔ Skill 상호 변환 / ❌ Boundary 위반 자동 정정 (위반 검출 시 BLOCK + 사용자 명시 결정).

→ Criterion 9 PASS, 정의 + 예시 + 핵심 차이 + §5.3 비대상 명시 = boundary 명확.

### 2.10 기준 #10 — 4 금지 사항 유지

**확인 결과**: ✅ PASS

§5.2 점검:

| # | 금지 | 사유 | 강제 메커니즘 | G3/G4 위임 |
|---|---|----|----------|--------|
| 1 | Memory 가 policy 를 대체 | 권위 위계 우회 위험 | G3 §2.2 #9 / #11 (T3) + Memory write 권한 0 (사용자만) | ✅ G3 위임 + Memory write ACL |
| 2 | Skill 이 ADR / Constitution 우회 | Skill 본문이 ADR / Constitution 자동 수정 / override | G3 §2.2 #10 / #11 (T3) + skill `allowed_actions` 에 `policy_write` 등 미포함 | ✅ G3 위임 + schema enum |
| 3 | Session memory 가 global memory 로 자동 승격 | Session 임시 상태가 Global 영구 정책으로 leak | §2.5 promotion T2 강제 + filesystem ACL | ✅ §2.5 + G3 §1.2.1 |
| 4 | Hermes 가 skill 을 자기 승인 | 자기 격상 위험 (G3 §2.2 #14 / §4.5 답습) | G3 §2.2 #16 (T2) + promotion hook 차단 + 사용자 명시 강제 | ✅ G3 위임 + §3.4 |

4 금지 사항 모두 *강제 메커니즘* + *G3 위임* 분리 명시. T3 위반 영역 2건 (#1 + #2) / T2 강제 영역 2건 (#3 + #4).

→ Criterion 10 PASS, 4 금지 사항 enumeration + 사유 + 강제 메커니즘 + G3 위임 모두 명시 + 일관.

### 2.11 기준 #11 — G2 GP-6 과의 연결 명확성

**확인 결과**: ✅ PASS

§7 GP-6 인터페이스 점검:

| 항목 | G2 GP-6 (가능성 검증) | G4 (형식 제공) |
|---|---|---|
| JSONL schema | (위임 — G4 정의) | ✅ §4.2 |
| Hash chain 변조 방지 | (위임) | ✅ §4.4 |
| Schema_version 호환성 | (위임) | ✅ §4.3 |
| 변환 스크립트 사양 | (위임) | ✅ §4.5 |
| 변환 스크립트 *실 구현* | ✅ GP-6 §8.6 산출 후보 | (G4 범위 외 §0.2 #8) |
| 라운드트립 자동 테스트 | ✅ GP-6 §8.3 + R2-5 답습 | ✅ §4.6 절차 정의 |
| schema 검증 자동 테스트 | ✅ GP-6 §8.3 | ✅ §4.2 검증 규칙 |
| Hermes 메이저 업데이트 시 자동 회귀 | ✅ GP-6 §8.5 (d) | (위임) |
| 합의 보고서 (G4 + GP-6 통합 가능) | ✅ GP-6 §8.5 (e) | ✅ §8.3 |

§7.2 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 + §7.3 GP-6 후속 갱신 권고 (G2 §8.5 (e) cross-reference 추가) 명시.

→ Criterion 11 PASS, *9 항목 책임 분리 매트릭스* + 3-way 인터페이스 + GP-6 후속 갱신 권고 = 연결 명확.

### 2.12 기준 #12 — G3 권한 / 신뢰 / 무결성 설계와 충돌 없음

**확인 결과**: ✅ PASS

§6 G3 인터페이스 5 항목 점검:

| # | 항목 | G4 책임 (형식) | G3 책임 (권한) | 충돌 |
|---|----|------------|------------|---|
| 6.1 | Skill Escalation 방지 | `allowed_actions` / `forbidden_actions` / 권한 등급 enum (§3.1 #9·#10 / §3.2) | wrapper 검증 / sandbox / audit log / 자동 비활성화 (G3 §3.3.3~§3.3.5) | ❌ 충돌 0 (책임 명확 분리) |
| 6.2 | Hermes-originated Skill Auto-approval 금지 | `promotion_status` + 5 상태 + 전이 규칙 (§3.1 #13 / §3.3) | commit auto-reject / T2 사용자 승인 / Tools 검증 + Evidence (G3 §2.2 #20 + §2.2 #16 + §5.3) | ❌ 충돌 0 |
| 6.3 | Evidence 없는 Skill Promotion 금지 | `required_evidence` / `required_tests` / `last_verified_at` (§3.1 #11·#12·#17) + hash chain (§4.4) | Evidence Ledger entry 강제 / 검증 (G3 §1.3 + §5.3 (ii)) | ❌ 충돌 0 |
| 6.4 | Provider Lock-in 방지 | `provider_bindings` + §3.5 검증 규칙 + §4.3 최소 2 provider 재해석 | depcruise 룰 (G2 GP-5) + Hermes-originated 변경 차단 (G3 §6.4) | ❌ 충돌 0 (3-way 보호 완결) |
| 6.5 | Memory Poisoning Rollback | `evidence_refs` / `created_from` / `rollback_triggers` + hash chain (§4.2 / §3.1 #16 / §3.1 #14 / §4.4) | T1 분석 검출 / rollback / 사용자 alert (G3 §3.1.2 + §3.1.5 + §3.1.6) | ❌ 충돌 0 |

§6.6 통합 — G3 ↔ G4 책임 분리 매트릭스 7 행 (Memory promotion / Skill promotion / escalation / Hermes-originated commit auto-reject / Evidence 없는 promotion / Provider lock-in / Memory poisoning rollback) 모두 G3 (권한) ↔ G4 (형식) 분리.

→ Criterion 12 PASS, 5 항목 모두 *G4 형식 정의* ↔ *G3 권한 강제* 책임 분리 + 충돌 0건. 두 게이트 모두 PASS 시 격상 충분 조건 일부 충족 (4 게이트 통합 합의 후).

### 2.13 기준 #13 — G4 PASS / Hermes PMO 격상 / P2 v3 정식 채택 암시 표현 0건

**확인 결과**: ✅ PASS

| 영역 | 본 초안 위치 | 강도 |
|---|---------|---|
| 헤더 (`상태: DRAFT`) | 문서 상단 | ✅ DRAFT 명시 |
| §0.2 "본 초안이 *하지 않는* 것" 11 항목 enumeration | §0.2 #1~#11 | ✅ 11건 명시 부정 |
| §0.3 단계별 정식화 절차 (단계 1~5, 본 초안 = 단계 1 까지만) | §0.3 표 | ✅ 단계 1 한정 명시 |
| §8.4 G4 통합 Exit *선언* 절차 — "발생하지 않는 것" 6 항목 | §8.4 | ✅ 6건 부정 enumeration |
| §11.2 본 초안의 *PASS 판정 트리거하지 않는 것* 10 항목 | §11.2 | ✅ 10건 명시 부정 |
| 종료 줄 (`다음 진입점` + `금지` 7 항목) | 문서 종료 부분 | ✅ 7건 명시 부정 |

본 G4 초안 어디에도 G4 PASS / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 자동 갱신 / archive 자동 처리 / 실 runtime 코드 / 실 migration script 자동 트리거 표현 0건. 모두 *예고 / 후속 / 별도 합의 / 사용자 명시 결정* 으로 차단.

→ Criterion 13 PASS, 다중 명시 부정 (6 위치 × ≥6건) = 암시 표현 0건.

### 2.14 13 기준 합산

| # | 기준 | 결과 |
|---|---|----|
| 1 | Provider-agnostic Memory / Skill 형식 정의 충실성 | ✅ PASS |
| 2 | Memory Scope 4 단계 명확성 | ✅ PASS |
| 3 | MVP 범위 Global + Project 제한 | ✅ PASS |
| 4 | Session / Team-Agent 후속 단계 분리 | ✅ PASS |
| 5 | Skill schema 17 필드 provider-neutral 정의 | ✅ PASS |
| 6 | `provider_bindings` optional optimization 제한 | ✅ PASS |
| 7 | JSONL export/import Hermes 내부 DB 없이 해석 가능 | ✅ PASS |
| 8 | hash chain / canonical JSON / migration 가능성 명시 | ✅ PASS |
| 9 | Memory / Skill boundary 명확성 | ✅ PASS |
| 10 | 4 금지 사항 유지 | ✅ PASS |
| 11 | G2 GP-6 연결 명확성 | ✅ PASS |
| 12 | G3 권한 / 신뢰 / 무결성 설계와 충돌 없음 | ✅ PASS |
| 13 | G4 PASS / Hermes PMO 격상 / P2 v3 정식 채택 암시 표현 0건 | ✅ PASS |

**13/13 PASS**.

---

## 3. 자기 발견 잠재 위험 (DRAFT 적격성과 분리)

본 §3 은 본 검토자 시야에서 자기 발견한 후속 권고. 모두 LOW / VERY LOW 등급으로 *DRAFT 적격성* 에는 영향 없음 — *G4 PASS 합의 시점* 또는 *정식 채택 시점* 흡수 후보.

### P-1: §11.1 자기 명시 한계 — RFC 8785 JCS 미인용

- **위치**: §4.4 + §11.1
- **위험**: JSON canonicalization 표준 RFC 8785 (JCS) 가 본 초안에서 *직접 인용 안 됨* — *간단 명시* 한정 (lex sort + RFC 8259 escape + IEEE 754 numeric). 본 초안이 *자기 발견* + 정식 채택 시 인용 권고를 §11.1 에 명시 → 자기 발견 정상.
- **등급**: LOW
- **처리 시점**: G4 PASS 합의 또는 정식 채택 시점 (단축 또는 풀 3+1 합의 — §10 변경 절차 §11.4 흡수 후속)
- **처리 방법**: §4.4 본문에 RFC 8785 JCS 명시 인용 + canonical JSON 사양 보강

### P-2: §10 schema 진화 정책 — 필드 *제거* / *이름 변경* 정책 미명시

- **위치**: §10 변경 절차 표
- **위험**: §10 표는 §3.1 17 필드 *추가* (semver MINOR) 만 명시. 필드 *제거* / *이름 변경* / *타입 변경* 정책 미명시 → 후속 schema 진화 시 모호.
- **등급**: LOW
- **처리 시점**: 본 PR-1 §10 보강 (단축 합의) 또는 별도 합의
- **처리 방법**: §10 변경 절차 표에 필드 *추가 / 제거 / 이름 변경 / 타입 변경* 4 행 추가 + schema_version 증가 정책 명시

### P-3: §4.5 외부 형식 import 시 schema_version declaration 절차 약함

- **위치**: §4.3 + §4.5
- **위험**: schema_version 호환성 확인 절차가 *명시 declaration 후만 import 가능* 까지만 — 호환성 매트릭스 / migration 자동 step 미명시 → 정식 채택 시점 import script 사양 보강 필요.
- **등급**: LOW
- **처리 시점**: G4 정식 채택 합의 또는 별도 합의 (Implementation 영역)
- **처리 방법**: §4.5 import 시 schema_version 검증 + 호환성 매트릭스 명시

### P-4: §6.4 / §3.5 / §4.3 "3-way 인터페이스" 명명 정확성

- **위치**: §6.4 / §3.5 / §4.3
- **위험**: 본 초안에서 §6.4 "3-way 인터페이스" (G2 GP-5 + G3 §6.4 + G4 §3.5 + §4.3) 로 명명. 실제 G4 두 § (§3.5 + §4.3) + G2 GP-5 + G3 §6.4 = 실질 *4 위치* 이지만 *3 게이트* 로 카운트. 명명 자체는 정당하나 *Provider Liquidity 보호 layer 명명* 으로 정정 권고 후보.
- **등급**: VERY LOW
- **처리 시점**: G4 정식 채택 시점 또는 별도 합의
- **처리 방법**: §6.4 명명 "3-way" → "Provider Liquidity 4-way Multi-layer Defense" 정정 (Layer 1 GP-5 / Layer 2 G3 §6.4 / Layer 3 G4 §3.5 / Layer 4 G4 §4.3) — 본문 변경 0건, 용어만 정정

### P-5: §2.2.1 Global Memory `~/.claude/global/` Claude Code 표준 디렉토리 충돌 가능성

- **위치**: §2.2.1 저장 위치 표
- **위험**: `~/.claude/global/` 경로가 Claude Code 표준 디렉토리 구조 (`~/.claude/`) 와 충돌 가능성. 실 path 결정은 Implementation/Runtime 영역.
- **등급**: VERY LOW
- **처리 시점**: Implementation/Runtime PASS 합의 (실 path 결정 시점)
- **처리 방법**: 별도 합의 — Claude Code 표준 디렉토리 구조 점검 후 path 정정 또는 prefix 추가 (예: `~/.claude/hermes-memory/global/`)

### 3.6 본 §3 합산

| # | 위험 | 등급 | DRAFT 적격성 영향 |
|---|---|----|------------|
| P-1 | §4.4 RFC 8785 JCS 미인용 | LOW | ❌ 0 (자기 발견 + §11.1 명시) |
| P-2 | §10 schema 진화 정책 부분 | LOW | ❌ 0 |
| P-3 | §4.5 import schema_version 절차 약함 | LOW | ❌ 0 |
| P-4 | §6.4 "3-way" 명명 정확성 | VERY LOW | ❌ 0 |
| P-5 | §2.2.1 `~/.claude/global/` path 충돌 | VERY LOW | ❌ 0 |

5건 모두 **LOW / VERY LOW + BLOCK 사유 아님 + G4 PASS 합의 또는 정식 채택 시점 흡수 가능**. DRAFT 적격성 판정에 영향 없음.

---

## 4. 9 금지 항목 점검 (사용자 명시)

| # | 금지 항목 | 위반 여부 |
|---|------|-----|
| 1 | G4 PASS 선언 | ❌ 위반 0건 (헤더 DRAFT + §0.2 #1 + §0.3 단계 5 = 본 초안 외 + §8.4 + §11.2 + 종료 줄 다중 명시 부정) |
| 2 | G2 / G3 PASS 선언 | ❌ 위반 0건 (§0.2 #2 + §8.4 "G2/G3 자동 PASS 발생 ❌" + §11.2 명시) |
| 3 | Hermes PMO 격상 선언 | ❌ 위반 0건 (헤더 + §0.2 #3 + §8.4 "Hermes PMO 격상 자동 활성화 ❌" + §11.2 + 종료 줄 명시 부정) |
| 4 | P2 v3 정식 채택 선언 | ❌ 위반 0건 (§0.2 #4 + §8.4 "P2 v3 정식 채택 자동 ❌" + §11.2 + 종료 줄 명시 부정) |
| 5 | ADR-008/009/010/011 본문 자동 갱신 | ❌ 위반 0건 (§0.2 #5 + §8.4 "ADR 본문 자동 갱신 ❌ — cross-reference 만" + §11.2 + 종료 줄 명시 부정) |
| 6 | P2 v2 archive 처리 | ❌ 위반 0건 (§0.2 #6 + §8.4 "system-identity-prequel.md / P2 v2 자동 archive ❌" + §11.2 명시) |
| 7 | system-identity-prequel archive 처리 | ❌ 위반 0건 (§0.2 #6 + §11.3 즉시 강제 #1 "prequel archived 후에도 본 G4 §2.2 + §2.5 권위로 보존") |
| 8 | 실 runtime 코드 구현 | ❌ 위반 0건 (§0.2 #7 + §11.2 마지막 항 "Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 등") |
| 9 | 실 migration script 구현 | ❌ 위반 0건 (§0.2 #8 "사양까지만 (§4.5)" + §4.5 본문 명시 "구현은 본 초안 외" + §4.6.7 "실 migration script 구현 = Implementation/Runtime PASS 영역, 본 §4.6 범위 외") |

→ **9/9 금지 항목 위반 0건**.

---

## 5. 메타 편향 자기진단

### 5.1 본 검토의 메타 편향 위험 (G4 특수 조건)

**중요**: G4 는 *Provider Liquidity* 의 *형식 차원* 보장 — *공통 schema + JSONL + hash chain + canonical JSON + migration script 사양* 의 *원안* 자체를 첫 명시한 문서. 본 검토자(Reviewer)는 G4 초안 작성자와 동일 컨텍스트 → **자기참조 + 메타 편향 위험**.

본 §5.1 은 G3 §4 자기참조 차단의 *적용 대상*. 따라서 본 검토는 다음을 명시 인지:

1. 본 검토는 G3 §4.4.1 ("Reviewer-only 단축 합의 충분 조건")의 4 조건 중 *DRAFT 적격성* 한정 충족 — *G4 PASS* 합의는 G3 §4.4.2 답습으로 외부 LLM 의견 권장 또는 필수.
2. 본 검토 *PASS 판정*은 *G4 PASS 판정*이 아님 (§1.4 답습).
3. §3.1 17 필드 schema 자체의 *적정성 검증* (필드 enumeration 완전성 + 검증 규칙 적정성) 은 본 Reviewer 시야 한계 — 외부 LLM 시야 또는 PoC 실증을 통해 보강 의무, *DRAFT 적격성* 판정과 분리.
4. §4.4 canonical JSON / hash chain 사양의 *적정성 검증* 도 동일 — 본 검토 범위 외.
5. §2.1 4 scope (Global / Project / Session / Team-Agent) 의 *완전성* 도 본 Reviewer 시야 한계 — system-identity-prequel §8.4 + 합의 §103 답습이 정당하나 *추가 scope* 누락 여부는 후속 검증.

### 5.2 5 통제 답습

| # | 통제 수단 | 본 검토 적용 |
|---|---|---|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 13 기준 §2 + 9 금지 항목 §4 + DRAFT 적격 검토 한정 |
| 2 | 직전 단축 합의 패턴 답습 | ✅ P2 v3 / G2 / G3 DRAFT 검토 §1~§7 구조 답습 |
| 3 | 13 항목 답습 + 9 금지 점검 | ✅ §2 13/13 + §4 9/9 점검 |
| 4 | 자기 발견 잠재 위험 명시 (§3 P-1 ~ P-5) | ✅ 5건 자기 발견, 모두 LOW/VERY LOW + BLOCK 사유 아님 |
| 5 | 본 검토가 *하지 않는* 것 명시 (§1.4) | ✅ 9건 명시 비대상 |

### 5.3 본 검토의 한계

- 본 검토는 *자기 작성 산출 자기 검토* (P2 v3 / G2 / G3 / G4 모두 동일 컨텍스트)
- **G3 §4.4.2 + G4 §0.3 #4 답습**: 자기 작성 산출 검증은 외부 LLM 의견 *권장* — 본 검토가 외부 LLM 의견 대체 불가
- **G4 PASS 합의는 외부 LLM 의견 권장 + 격상 통합 합의는 외부 LLM 1+ 필수** (G3 §4.4.2 답습). 본 검토는 그 적격성 판정 비대상.
- §3 자기 발견 잠재 위험 5건은 본 Reviewer 의 시야 한정 — 외부 LLM 시야에서 추가 발견 가능.
- 특히 §3.1 17 필드 schema 자체 (원안) + §4.4 hash chain / canonical JSON (간단 명시 + JCS 미인용) + §2.1 4 scope enumeration 완전성 = 본 검토 자기 검증 한계. *G4 PASS 합의 또는 정식 채택 합의* 시점 외부 LLM 의견 의무.
- 본 초안의 *후속 갱신* (예: PR-2 hash chain 사양 보강 + RFC 8785 JCS 인용 + Genesis Hash 정의 + prev_hash 검증 실패 처리 + Full Rewrite 5 Layer 방어 등) 은 본 *2026-05-07 DRAFT 적격* 판정 시점 *밖* — 추후 풀 3+1 합의 또는 별도 PR 영역.

### 5.4 본 검토의 *PASS 판정이 트리거하지 않는 것*

본 §6 결론 PASS 판정은 다음을 *트리거하지 않는다*:

- ❌ G4 PASS
- ❌ G2 / G3 PASS 선언
- ❌ Hermes PMO 격상
- ❌ P2 v3 정식 채택
- ❌ ADR-008/009/010/011 본문 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 자동 갱신 (commit 후 별도 사용자 결정)
- ❌ Phase 진입 결정
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
- ❌ Tier-2 / Tier-3 Skill catalog 확장

본 검토 PASS 판정은 *오직* "G4 Provider-agnostic Memory / Skill 통합 설계 DRAFT 적격 + G2/G3/G4 정식 채택 합의 준비 진입 적격" 의미.

---

## 6. 결론

### 6.1 판정

```
✅ APPROVE AS DRAFT
```

### 6.2 사유

- **13 기준 13/13 PASS** (§2.1 ~ §2.13) — 형식 정의 충실 + Memory scope 4 단계 명확 + MVP Global+Project 제한 + Session/Team 후속 분리 + Skill schema 17 필드 provider-neutral + `provider_bindings` optional optimization 제한 + JSONL Hermes 의존 0 + hash chain/canonical/migration 명시 + boundary 명확 + 4 금지 사항 유지 + GP-6 9 항목 연결 + G3 5 인터페이스 충돌 0건 + 암시 표현 0건
- **9 금지 항목 9/9 위반 0건** (§4)
- **자기 발견 잠재 위험 5건** (§3 P-1 ~ P-5) 모두 LOW / VERY LOW 등급 + BLOCK 사유 아님 + G4 PASS 합의 또는 정식 채택 시점에 흡수 가능
- **메타 편향 5 통제 답습** (§5.2)
- **G3 §4 자기참조 차단의 *적용 대상*** 으로 본 검토 한계 명시 (§5.1 + §5.3)
- 옵션 B (Memory + Skill 통합 단일 문서) 사용자 명시 결정 답습 정당 — §1.2 채택 사유 명시 (공통 schema 보장 + lock-in 방지 통일 + GP-6 통합 처리 자연스러움)

### 6.3 후속 권고 (DRAFT 적격성과 *분리*)

본 결론은 DRAFT 적격성 판정 한정. 후속 작업 시 다음 흡수 권고 (선택):

| # | 권고 (선택) | 위치 | 처리 시점 |
|---|---|----|---------|
| 1 | §4.4 RFC 8785 JCS 명시 인용 + canonical JSON 사양 보강 | G4 §4.4 + §11.1 | G4 PASS 합의 또는 정식 채택 시점 (단축 또는 풀 3+1) |
| 2 | §10 schema 진화 정책 표 보강 (필드 추가/제거/이름 변경/타입 변경 4 행) | G4 §10 | 정식 채택 시점 (단축 가능) |
| 3 | §4.5 import schema_version 검증 + 호환성 매트릭스 보강 | G4 §4.5 | 정식 채택 시점 또는 별도 합의 |
| 4 | §6.4 "3-way 인터페이스" → "Provider Liquidity 4-way Multi-layer Defense" 명명 정정 (본문 변경 0건, 용어만) | G4 §6.4 / §3.5 / §4.3 | 정식 채택 시점 |
| 5 | §2.2.1 `~/.claude/global/` Claude Code 표준 디렉토리 충돌 점검 | G4 §2.2.1 | Implementation/Runtime PASS 영역 (별도 합의) |
| 6 | G2 §8.5 (e) Exit 기준에 G4 cross-reference 추가 (3-way 통합 합의 가능) — G2 / G4 정식 채택 시점 동시 갱신 | G2 §8.5 | G2 / G4 정식 채택 시점 |

본 권고 6건은 *G4 PASS 합의 또는 정식 채택 진입 시점* 에 함께 검토. 본 DRAFT 적격성 판정 단계에서는 처리 불필요.

### 6.4 G2 / G3 / G4 정식 채택 합의 준비 진입 적격성

본 G4 DRAFT 적격성 판정 결과 + 사용자 명시 결정 ("G4 DRAFT 검토 APPROVE 시 G2/G3/G4 정식 채택 합의 준비 진입") 답습 → **G2/G3/G4 정식 채택 합의 준비 진입 적격**.

정식 채택 합의 진입 시점 사용자 결정 후보 (G4 §8.3 답습):

| 옵션 | 합의 형태 | 비고 |
|---|---|---|
| 1 | G4 단독 단축 합의 (Reviewer-only) | 본 초안에 새 권위 결정 0건 (ADR-008 차단조건 #2 답습 + system-identity-prequel §8.4 흡수) — 단축 합의 적격 |
| 2 | G4 + G2 GP-6 통합 합의 (단축 또는 풀 3+1) | GP-6 §8.5 (e) 답습 |
| 3 | G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 1+ (PR 묶음) | 격상 통합 합의 답습 — P2 v3 §9.2 / G2 §10.2 / G3 §8.2 옵션 3 패턴, 메타 편향 통제 + PR 묶음 비용 효율 |

본 검토는 옵션 결정 비대상 — 사용자 명시 결정 후 진입.

### 6.5 본 검토 보고서 commit 절차

본 결론 APPROVE AS DRAFT에 따라 다음 단일 파일을 별도 commit으로 처리 가능:

```
docs/review/3plus1-consensus-2026-05-07-g4-memory-skill-draft.md
```

commit 메시지 (사용자 예시 답습):
```
docs(review): record G4 memory skill draft short review
```

본 commit에 포함하지 *않는* 항목 (사용자 명시 답습):
- G4 본문 갱신
- G2 / G3 본문 갱신
- ADR-008/009/010/011 본문 갱신
- P2 v2 / system-identity-prequel archive 처리
- INDEX / CONTEXT 갱신
- Hermes PMO 격상 선언
- G2 / G3 / G4 PASS 선언 / P2 v3 정식 채택 선언
- 실 runtime 코드 / 실 migration script 구현

---

## 7. 다음 진입점 (본 검토 *이후*)

본 검토 PASS 후 사용자 명시 7단계 순서 답습:

| # | 단계 | 산출 | 시점 |
|---|---|---|---|
| 1 | G4 단축 검토 완료 | 본 보고서 | 본 단계 (완료) |
| 2 | 검토 보고서 별도 commit | `docs(review): record G4 memory skill draft short review` | 본 단계 직후 |
| 3 | G2 / G3 / G4 정식 채택 합의 준비 | 사용자 명시 결정 후보 (옵션 1/2/3 — §6.4 답습) | 사용자 명시 결정 후 |
| 4 | 외부 LLM 의견 포함 여부 결정 | 사용자 명시 결정 — G3 §4.4.2 답습 (격상 통합 합의 시 외부 LLM 1+ 필수) | 단계 3 도중 |
| 5 | P2 v3 정식 채택 합의 | 합의 보고서 + 사용자 명시 결정 | G2/G3/G4 통합 합의 후 |
| 6 | ADR-008/009/010/011 갱신 여부 결정 | 별도 PR 묶음 + 사용자 명시 결정 (신규 ADR-014 후보 검토 포함) | P2 v3 정식 채택 후 |
| 7 | P2 v2 / system-identity-prequel archive 여부 결정 | 별도 처리 + 사용자 명시 결정 | ADR 갱신 후 또는 동시 |
| 8 | Hermes PMO 격상 여부 별도 결정 | 별도 합의 + 외부 LLM 1+ 필수 + 사용자 명시 결정 | 4 게이트 통합 PASS 후 별도 |

본 검토 *이후* 금지 사항은 변동 없음 — §4 9 금지 항목 + 사용자 명시 답습.

---

**검토일**: 2026-05-07
**검토자**: Reviewer-only (메타 편향 자기진단 §5 명시 + G3 §4 자기참조 차단의 적용 대상 인지 + G4 자기 작성 산출 자기 검토 한계 명시)
**판정**: ✅ APPROVE AS DRAFT
**다음 단계**: 본 검토 보고서 별도 commit → G2/G3/G4 정식 채택 합의 준비 (사용자 명시 결정 후)
