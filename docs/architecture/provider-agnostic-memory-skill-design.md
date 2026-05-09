# Provider-agnostic Memory / Skill Design (G4) — Design/Governance Gate PASS (Bundled, 2026-05-09)

> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 **G4** — Memory 와 Skill 이 특정 provider / 특정 DB / 특정 내부 포맷에 lock-in 되지 않도록 *공통 schema + 운영 규칙 + JSONL export/import 형식* 을 정의하는 통합 설계 문서. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
>
> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — Memory scope 4 단계 (MVP Global+Project) / Skill schema 17 필드 / JSONL export hash chain 변조 방지 / Memory/Skill boundary 4 금지 / G3 인터페이스 5 항목 / G2 GP-6 인터페이스의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — 실 migration script (`hermes_to_claude.py` / `hermes_to_openai.py` 등) 구현 + 라운드트립 PoC 실증 + hash chain canonical JSON 사양 보강 (canonical / newline / encoding / field ordering / genesis / prev_hash 검증 실패 처리 / full rewrite 방어 / round-trip lossy ledger) + provider_bindings lint 룰 강제는 *별도 합의* 로만 발생.
>
> **G4 라운드트립 / migration script 상태 (P0 조건 C-B, 5/5 입력 일치)**: **DESIGN PASS / IMPLEMENTATION PENDING** (§4 변환 스크립트 사양까지만, 실 PoC 미실증 — 합의 보고서 §6 갱신 권고 흡수 시점에 별도 합의).
>
> **Hermes PMO 격상 / G4 운영 구현 PASS / P2 v3 정식 채택 / ADR 본문 자동 갱신 (신규 ADR-014 후보 검토 포함) / archive 자동 처리는 본 PASS 에 포함되지 않는다** (사용자 명시 답습).

**작성일**: 2026-05-07
**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G2 + G3)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
**산출 방식**: 옵션 B (Memory + Skill 통합 단일 문서) — 사용자 명시 결정 답습. 사유: G4 핵심은 *Memory/Skill 공통 형식 — provider-agnostic schema*. 분리 작성 시 lock-in 방지 *공통 보장*이 약화될 위험.
**상위 권위**: 헌법 제5조 관용 (Provider Liquidity), 헌법 제8조 (보안), ADR-008 차단조건 #2 (JSONL export 표준)
**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리)
**관련 설계**: `hermes-adoption-design-v3.md` §6 (G4 정의), `governance-preconditions.md` §8 (GP-6 Memory/Skill Migration), `hermes-not-root-of-trust-runtime.md` §6.5 / §7 (GP-6 ↔ G3 ↔ G4 3-way 인터페이스), `system-identity-prequel.md` §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Memory 2단계 채택 + Skill 자동 추출 T1 한정 + GPT 4단계 미채택 사유), `docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` (G3 §7 G4 경계 인용), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G4 정식 PASS 합의)
**관련 evidence**: G1b PASS (R-7 SOP §7.3 단축 합의, 2026-05-07), G2 DRAFT 적격 검토 APPROVE (`957cddc`), G3 DRAFT 적격 검토 APPROVE (`d42886b`)

---

## 0. 본 초안의 범위

### 0.1 본 초안이 *하는* 것 (사용자 명시 7 항목 답습)

1. **Memory Scope 4 단계 정의** (Global / Project / Session / Team-Agent) + MVP scope (Global + Project) 명시 (§2)
2. **Skill Schema 17 필드** provider-neutral 정의 + 필드별 검증 규칙 (§3)
3. **Provider-agnostic JSONL Export/Import 형식** + hash chain 변조 방지 + migration script 사양 (구현은 본 초안 외) (§4)
4. **Memory/Skill Boundary** — *사실/결정/선호/상태/근거* (Memory) vs *반복 절차/입력/출력/권한/검증* (Skill) + 4 금지 사항 (§5)
5. **G3 인터페이스 5 항목** — Skill escalation / Hermes-originated auto-approval / evidence 없는 promotion / Provider lock-in / Memory poisoning rollback (§6)
6. **G2 GP-6 인터페이스** — G4 = GP-6 의 실제 형식/schema 제공 (§7)
7. **Acceptance Criteria** — 8 Exit 조건 (§8)

### 0.2 본 초안이 *하지 않는* 것 (사용자 명시 답습)

1. ❌ **G4 PASS 선언** — 본 초안은 *설계*까지만, (a)~(e) Exit 기준 충족 검증은 후속
2. ❌ **G2 / G3 PASS 선언**
3. ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 통과 + 사용자 명시 결정 후 별도
4. ❌ **P2 v3 정식 채택 선언** — `hermes-adoption-design-v3.md` 헤더 DRAFT 그대로 유지
5. ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — 별도 PR 묶음 (ADR-014 신규 후보 포함)
6. ❌ **P2 v2 / system-identity-prequel.md archive 처리** — v3 정식 채택 시점에
7. ❌ **실 runtime 코드 구현** — Memory boundary 강제 / Skill wrapper / promotion hook / JSONL writer 등 모두 별도 작업
8. ❌ **실 migration script 구현** — `scripts/hermes-migration/hermes_to_claude.py` 등 사양까지만 (§4.4)
9. ❌ **자동 정책 변경 (ADR-011 §2.4 T3)** — 절대 금지
10. ❌ **Hermes 자기 승인** — Skill / Memory promotion / revocation 모두 사용자 승인 강제 (§3 + §6.2)
11. ❌ **Tier-2 / Tier-3 catalog 확장** — 별도 합의

### 0.3 본 초안의 단계별 정식화 절차 (예정)

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | 본 초안 작성 (현 단계) | 본 문서 (DRAFT) | 2026-05-07 |
| 2 | 사용자 검토 + Reviewer-only 단축 검토 (DRAFT 적격) | 검토 보고서 별도 commit | 사용자 명시 결정 후 |
| 3 | 각 §의 PoC + (a)~(e) Exit 기준 충족 검증 (특히 §4 변환 스크립트 라운드트립 시연 — R2-5 답습) | PoC 산출 + evidence | §별 순차 또는 병행 |
| 4 | G4 PASS 합의 가동 (단축 또는 풀 3+1 / **G3 §4.4.2 답습** — 외부 LLM 의견 권장) | `docs/review/3plus1-consensus-YYYY-MM-DD-g4.md` | 단계 3 완료 후 |
| 5 | G4 PASS 선언 + ADR cross-reference 갱신 (G2/G3와 묶음 가능) + 신규 ADR-014 후보 검토 | 별도 PR | 단계 4 후 |

본 초안 자체는 단계 1까지만 처리. 단계 2~5는 본 초안 범위 외.

---

## 1. 통합 설계 원칙

### 1.1 G4 정체성

**G4 = Provider-agnostic Memory / Skill 형식**

```
헌법 5조 (관용 — Provider Liquidity)
  ↓
ADR-008 차단조건 #2 (JSONL export 표준)
  ↓
G4 (본 문서) — Memory / Skill 공통 schema + JSONL export/import + lock-in 차단
  ↓
GP-6 (G2) — 마이그레이션 *가능성* 검증 (라운드트립 PoC)
  ↓
G3 §6.5 / §7 — Memory / Skill *권한* + *Promotion* + *Escalation* 차단
```

**원칙**: G4 = *어떻게 표현되는가* (형식 / schema / export-import). G3 = *누가 무엇을 할 수 있는가* (권한 / 신뢰 / 무결성). GP-6 = *마이그레이션 가능성* (JSONL + 변환 스크립트 + 라운드트립).

### 1.2 본 통합 문서 채택 이유 (옵션 B)

사용자 명시 결정 답습 — Memory 와 Skill 을 **단일 문서로 통합** 작성 (옵션 B).

**채택 사유**:
- G4 핵심 = *공통 schema 보장* (Memory + Skill 양쪽에 적용되는 provider-agnostic 보장)
- 분리 작성 시 양 문서 간 *lock-in 방지 보장* 이 silent 다를 위험
- JSONL export 형식 + hash chain 변조 방지 + migration script 사양 등은 Memory 와 Skill 에 *동일* 적용 — 한 문서에 명시
- G2 GP-6 (마이그레이션 가능성) 도 Memory + Skill 통합 처리 — G4 통합 문서가 자연스러움

### 1.3 G3 / G2 와의 위계 명시

| 게이트 | 책임 | 본 문서와의 관계 |
|-------|------|--------------|
| **헌법 5조 (관용)** | Provider Liquidity 비협상 제약 | 본 문서 §11 영구 핵심 제약 + 모든 § 의 권위 근거 |
| **G2 GP-6** | 마이그레이션 *가능성* (라운드트립 PoC) | 본 G4 §4 형식 제공 + §7 인터페이스 |
| **G3 §6.5 / §7** | *권한* / *Promotion* / *Escalation* 차단 | 본 G4 §6 인터페이스 (5 항목) |
| **G4 (본 문서)** | *형식* / *schema* / *export-import* | 본 문서 자체 |

**위계 답습** (ADR-011 §2.3 영구 권위):
```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

본 G4 자체는 SDD / Harness Gates 등급 — Hermes / Worker 가 *수정* 또는 *우회* 시도 시 G3 §2.2 #9 / #11 / #17 / #19 / #21 (T3) 으로 차단.

---

## 2. Memory Scope 정의

### 2.1 4 Scope 개요

| Scope | MVP 적용 | 정체성 | Owner |
|-------|--------|------|------|
| **Global** | ✅ MVP | cross-project 보편 원칙 / 패턴 / 헌법-동급 제약 | 사용자 (manual approval) |
| **Project** | ✅ MVP | 프로젝트별 목표 / 결정 / 반복 버그 / 도메인 용어 | 사용자 (manual approval) |
| Session | ⏳ 후속 | 본 세션 작업 추적 / 임시 결정 / 직전 상태 | Hermes (자동 기록) + 사용자 (review) |
| Team/Agent | ⏳ 후속 | Worker Agent 별 강점 / 실패 패턴 (파생 프로젝트 ≥ 3건 누적 후 의미 발생) | 사용자 |

**MVP 채택 사유** (system-identity-prequel §8.4 + 합의 §103 답습):
- Global + Project 2 단계가 충분 (3 Agent 명시 + GPT 4 단계 미채택)
- Session/Team 은 *조건부 후속* — 정량 트리거 (파생 프로젝트 ≥ 3건 / 실 프로젝트 코드 ≥ 1000 줄) 충족 시 별도 ADR

### 2.2 MVP Scope (Global + Project)

#### 2.2.1 Global Memory

| 항목 | 내용 |
|------|------|
| **목적** | 모든 프로젝트에 적용되는 보편 원칙 / 패턴 / 정의 — 사용자가 *cross-project 표준* 으로 승격한 항목만 |
| **저장 가능 정보** | (i) 헌법 본문 / ADR 작성 방식 / SDD/TDD 원칙 / 검증 원칙 / 금지 사항 / 역할 정의 (cross-project 보편), (ii) 사용자 일반 선호 (보편 적용 가능, 예: 한국어 소통 / 검증 우선 등), (iii) 일반 도메인 용어 / 패턴 (보편 적용) |
| **저장 금지 정보** | secret / API 키 / 토큰 / OAuth credentials / 프로젝트-specific 사실 / Session 임시 상태 / 외부 입력 raw data |
| **Promotion 조건** | Project → Global = **manual only** (사용자 명시 승인 강제, T2). 자동 promotion 절대 금지 (T3 위반) |
| **Expiration / Retention** | 영구 (사용자 명시 revoke 시점까지) |
| **Export / Import 방식** | JSONL append-only (§4 형식 답습) — Hermes 의존 0건 |
| **Owner / Approval Authority** | **사용자 (manual approval 강제)**. Hermes 는 *제안* 만 가능 (G3 §2.1 #3 답습), *등록·수정·revoke* 모두 T2 사용자 명시 |
| **저장 위치** | `~/.claude/global/` — filesystem 분리 (1차 boundary) |

#### 2.2.2 Project Memory

| 항목 | 내용 |
|------|------|
| **목적** | 본 프로젝트의 목표 / 기술 스택 / 도메인 용어 / 주요 결정 / 반복 버그 / 테스트 전략 / Phase 진행 상태 |
| **저장 가능 정보** | (i) 프로젝트 목표 / 기술 스택 / 도메인 용어 / 주요 결정 (Project-specific), (ii) 반복 버그 / 회피 휴리스틱, (iii) 테스트 전략 / Phase 진행 상태 |
| **저장 금지 정보** | secret / API 키 / 토큰 / OAuth credentials / cross-project 보편 정보 (Global 후보) / Session 임시 상태 (Session 후속) |
| **Promotion 조건** | Session → Project = manual only (T2, Session 후속 시) / Project → Global = manual only (T2, §2.2.1 답습) |
| **Expiration / Retention** | 프로젝트 종료 시까지 + 사용자 명시 archive 결정 시 보관 (T2). 자동 삭제 절대 금지 |
| **Export / Import 방식** | JSONL append-only (§4 형식) — Hermes 의존 0건 |
| **Owner / Approval Authority** | **사용자 (manual approval)**. Hermes / Worker 는 *제안* 만 가능. 등록·수정·revoke 모두 T2 사용자 명시 |
| **저장 위치** | `<project>/.claude/project/` — filesystem 분리 (1차 boundary) |

#### 2.2.3 환경 변수 boundary (2차)

| 변수 | 값 | 용도 |
|-----|---|-----|
| `CLAUDE_MEMORY_SCOPE` | `global` 또는 `project` | 현재 작업의 scope 명시 (boundary leak 차단) |

**메타-템플릿 복사 시 오염 방지** (system-identity-prequel §8.4 답습):
- 본 템플릿 `.gitignore` 에 `.claude/project/memory.jsonl` 추가
- 복사 후 init script (`init-project.sh`) 로 Project Memory 초기화 (실 코드 구현은 본 초안 외)

### 2.3 Session Memory (보류, 후속)

#### 2.3.1 정의 + 보류 사유

| 항목 | 내용 |
|------|------|
| **목적** | 본 세션 작업 추적 / 임시 결정 / 직전 상태 (다음 세션 진입 시 컨텍스트) |
| **현 처리** | `docs/sessions/SESSION_<날짜>.md` 로 충족 (system-identity-prequel §8.4 "보류" 답습) |
| **보류 사유** | 별도 scope 도입 시 이중 저장 + 정량 트리거 (파생 프로젝트 ≥ 3건) 미충족 |
| **후속 진입 조건** | 별도 ADR + 사용자 명시 결정 |

#### 2.3.2 후속 진입 시 사양 (예고만 — 본 초안에서 정식 정의 X)

| 항목 | 후속 사양 후보 |
|------|----------|
| **저장 가능** | in-progress 작업 / 임시 결정 / 직전 상태 / 본 세션 학습 결과 후보 |
| **저장 금지** | secret / 정책 변경 / Constitution / ADR / SDD 본문 변경 (T3) |
| **Promotion** | Session → Project / Global = **manual only** (T2 사용자 명시) |
| **Retention** | 세션 종료 시 자동 archive 또는 명시 삭제 결정 |
| **Owner** | Hermes (자동 기록) + 사용자 (review·promotion 결정) |

### 2.4 Team / Agent Memory (보류, 후속)

#### 2.4.1 정의 + 보류 사유

| 항목 | 내용 |
|------|------|
| **목적** | Worker Agent 별 강점 / 실패 패턴 (모델별 비교 시 의미 발생) |
| **현 처리** | 미적용 |
| **보류 사유** | 정량 트리거 (파생 프로젝트 ≥ 3건 + LiteLLM 등 외부 도구로 부족한 기능 명확 식별) 미충족 |
| **후속 진입 조건** | 별도 ADR + 정량 트리거 충족 + 사용자 명시 결정 |

#### 2.4.2 후속 진입 시 사양 (예고만)

| 항목 | 후속 사양 후보 |
|------|----------|
| **저장 가능** | per-agent 학습 결과 / 강점 패턴 / 실패 회피 휴리스틱 |
| **저장 금지** | secret / 정책 변경 / 다른 Agent 의 *권한* 변경 |
| **Promotion** | Team → Global = manual only (T2) |
| **Retention** | 영구 (사용자 명시 revoke 시점까지) |
| **Owner** | 사용자 |

### 2.5 Boundary 강제 메커니즘

| Layer | 메커니즘 | 강제 |
|------|--------|----|
| Filesystem | `~/.claude/global/` vs `<project>/.claude/project/` 디렉토리 분리 | 1차 boundary |
| 환경변수 | `CLAUDE_MEMORY_SCOPE=global|project` | 2차 boundary |
| Plugin | Hermes memory plugin scope 검증 (G4 의존) | 3차 boundary |
| Promotion | manual only — promotion hook 차단 (G3 §2.2 #15 답습) | T2 강제 |
| Filesystem ACL | Hermes container — Global / Project Memory write 권한 *없음* (제안만 가능, 실 write 는 사용자) | G3 §1.2.1 답습 |

---

## 3. Skill Schema 정의

### 3.1 17 필드 schema

```yaml
# skill.yaml — provider-neutral schema
# 필수성 표기: 필수 / MVP-필수 (C-K 흡수, 2026-05-09 후속 2) / MVP-권장 / 후속
id:                  # (1)  string, 필수, UUID v4 또는 slug
name:                # (2)  string, 필수, human-readable
version:             # (3)  string, 필수, semver
scope:               # (4)  enum, 필수
owner:               # (5)  string, 필수
description:         # (6)  string, 필수, markdown
inputs:              # (7)  JSON Schema, 필수
outputs:             # (8)  JSON Schema, 필수
allowed_actions:     # (9)  array<string>, 필수
forbidden_actions:   # (10) array<string>, MVP-권장
required_evidence:   # (11) array<evidence_type>, MVP-필수 (Skill promotion T2 검증 의무)
required_tests:      # (12) array<test_ref>, MVP-권장
promotion_status:    # (13) enum, 필수
rollback_triggers:   # (14) array<rollback_trigger>, MVP-권장
provider_bindings:   # (15) object, **필수** (C-K 흡수 — Provider Liquidity lock-in 차단 핵심, 권장→필수 격상)
created_from:        # (16) object, MVP-권장
last_verified_at:    # (17) ISO 8601 timestamp, 필수
```

### 3.2 필드별 정의 + 검증 규칙

| # | 필드 | 타입 | 필수 | 검증 규칙 | Provider Lock-in 위험 |
|---|------|-----|----|--------|-----------------|
| 1 | `id` | string | ✅ | UUID v4 또는 글로벌 unique slug `[a-z][a-z0-9_-]{2,63}` | 0 (자체 식별자) |
| 2 | `name` | string | ✅ | 1~100자, human-readable | 0 |
| 3 | `version` | string | ✅ | semver `MAJOR.MINOR.PATCH` | 0 |
| 4 | `scope` | enum | ✅ | `global` / `project` / `session` / `team` (Memory scope 와 일치) | 0 |
| 5 | `owner` | string | ✅ | user identifier 또는 agent identifier (provider-neutral) | 0 (provider 명시 금지) |
| 6 | `description` | string (markdown) | ✅ | 사용자 검토 가능한 본문 — 사용 방법 / 예시 / 트레이드오프 | 0 |
| 7 | `inputs` | JSON Schema | ✅ | 입력 형식 — 타입 / 검증 / 필수 표시 | 0 (JSON Schema = 표준) |
| 8 | `outputs` | JSON Schema | ✅ | 출력 형식 | 0 |
| 9 | `allowed_actions` | array\<string\> | ✅ | 권한 등급 enum: `read` / `write` / `shell` / `network` / `db` / `git` / `docker` (확장 가능) | 0 (action 종류는 표준) |
| 10 | `forbidden_actions` | array\<string\> | MVP-권장 | `allowed_actions` 와 disjoint | 0 |
| 11 | `required_evidence` | array\<evidence_type\> | MVP-필수 (C-K) | enum: `test_pass` / `lint` / `secret_scan` / `consensus` / `review` 등. `promotion_status: promoted` 진입 시 ledger 검증 의무 (§3.4) | 0 |
| 12 | `required_tests` | array\<test_ref\> | MVP-권장 | 테스트 파일 경로 또는 ID | 0 |
| 13 | `promotion_status` | enum | ✅ | `proposed` / `approved` / `promoted` / `archived` / `revoked` (§3.3 답습) | 0 |
| 14 | `rollback_triggers` | array\<rollback_trigger\> | MVP-권장 | enum: `escalation_detected` / `evidence_missing` / `t3_violation` 등 | 0 |
| 15 | `provider_bindings` | object | **✅ 필수 (C-K 격상)** | `{ "<provider_name>": { ...optional bindings... } }` — **provider 이름이 있어도 provider 에 종속되지 않아야 함**. 최소 2 provider 로 재해석 가능. `required: true` / `exclusive: true` 표시 *금지* (lint 룰 강제 = C-H 별도 합의 영역) | ⚠️ 주의 (lock-in 핵심 영역) |
| 16 | `created_from` | object | MVP-권장 | `{ "task_id": "...", "commit_sha": "...", "agent": "..." }` — 출처 추적 | 0 |
| 17 | `last_verified_at` | ISO 8601 | ✅ | 마지막 검증 시점 — `required_evidence` + `required_tests` 통과 시점 | 0 |

### 3.3 Promotion Status 상태 전이

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

| 상태 | 의미 | 진입 조건 | 다음 상태 후보 |
|------|------|--------|-----------|
| `proposed` | Hermes / Worker 가 추출한 Skill 후보 | T1 자동 추출 (G3 §2.1 #3) | `approved` (사용자 승인) / `archived` (사용자 거부) |
| `approved` | 사용자 명시 승인 — 사용 가능, 단 검증 미통과 | T2 사용자 명시 결정 + Skill schema 통과 | `promoted` (검증 통과) / `revoked` (검증 실패) / `archived` |
| `promoted` | Tools 검증 + Evidence 통과 — 정식 운영 | `required_evidence` + `required_tests` 모두 통과 + ledger entry | `revoked` (rollback 발생) / `archived` |
| `revoked` | rollback_trigger 발생 — 사용 차단 | rollback_trigger 매치 | `archived` (사용자 명시 폐기) / `approved` (사용자 명시 재활성화 + 재검증) |
| `archived` | 사용자 명시 폐기 — 영구 비활성 | T2 사용자 명시 archive | (terminal) |

### 3.4 Skill 자동 생성 vs 자동 승격 분리 (핵심 원칙)

> **Skill 은 자동 생성될 수 있지만, 자동 승격되어서는 안 된다.**

| 단계 | 권한 | 분류 |
|------|-----|------|
| Skill 후보 *추출* (반복 패턴 → `proposed`) | ✅ Hermes / Worker T1 자동 (G3 §2.1 #3) | T1 |
| Skill `proposed` → `approved` | ❌ Hermes 자동 금지 — **사용자 명시 승인 강제** | T2 (G3 §2.2 #16) |
| Skill `approved` → `promoted` | ❌ Hermes 자동 금지 — **Tools 검증 + Evidence ledger entry** 필수 + 사용자 명시 가능 | T2 + Evidence (G3 §5.3 답습) |
| Skill `promoted` → `revoked` | ✅ rollback_trigger 매치 시 자동 revoke (T3 위반 차단 = 자동 안전 동작) | T3 자동 안전 |
| Skill `*` → `archived` | ❌ Hermes 자동 금지 — 사용자 명시 결정 강제 | T2 |

### 3.5 `provider_bindings` 필드 — Provider Lock-in 차단 핵심

**원칙**: `provider_bindings` 에 provider 이름이 있어도 **provider 에 종속되지 않아야 한다**. 최소 2 provider 로 재해석 가능 (§4.2 답습).

```yaml
# 예시 — OK (provider-neutral 보장)
provider_bindings:
  claude:
    optional_optimization: true     # 선택 최적화 — 다른 provider 에서 fallback 가능
  openai:
    optional_optimization: true
  ollama:
    optional_optimization: false    # 미지원 — fallback 명시
# Skill 자체는 provider 무관하게 동작 — provider_bindings 는 *최적화 힌트* 한정
```

```yaml
# 예시 — 금지 (Provider lock-in 위반)
provider_bindings:
  claude:
    required: true                  # ❌ Provider lock-in
    custom_endpoint: "anthropic://..."  # ❌ Provider 종속 endpoint
# Skill 동작이 claude 에만 가능 → Provider Liquidity 위반 (G3 §6.4 답습)
```

**검증 규칙**:
- `provider_bindings` 의 어떤 provider 도 *required* 또는 *exclusive* 표시 금지
- 모든 binding 은 *optional optimization* 한정
- 최소 2 provider 로 재해석 가능 (예: claude / openai / ollama 중 2+)
- Provider 종속 endpoint / SDK / 모델명 분기는 Skill 본문에 작성 금지 (G2 GP-5 + G3 §6.4 답습)
- **C-K 격상 (2026-05-09 후속 2)**: `provider_bindings` 자체가 *필수 필드* — 즉 모든 Skill 은 본 §3.5 검증 규칙 통과 의무 (이전: 권장 → 필수)
- **C-H 별도 합의 영역**: lint 룰 (depcruise + schema lint) 강제 = 본 §3.5 검증 규칙의 *기계적 강제* — Implementation/Runtime PASS 영역, 별도 합의

### 3.6 MVP 필수 / MVP 권장 / 후속 분리 (C-K 흡수 — 2026-05-09 후속 2)

> **본 §3.6 은 합의 보고서 §11.2 P1 조건 C-K 흡수** (출처: Agent C 권고 + GPT 단순화 권고 + Claude §3.2 4/5 동의). §3.1 / §3.2 17 필드의 *필수성* 을 **MVP 진입 시점** 기준으로 분리 표기한다. *권장* 표기를 **MVP-필수 / MVP-권장 / 후속** 3 단계로 정련.

#### 3.6.1 분류 매트릭스 (17 필드)

| 분류 | 의미 | 필드 (총 17) | 검증 시점 |
|------|------|----------|--------|
| **필수** | Skill schema 통과 의무, 모든 단계에서 강제 | (1) id / (2) name / (3) version / (4) scope / (5) owner / (6) description / (7) inputs / (8) outputs / (9) allowed_actions / (13) promotion_status / **(15) provider_bindings (C-K 격상)** / (17) last_verified_at — **12 건** | Skill 등록 시점 (T2 사용자 명시 승인 §2.2 #16 답습) |
| **MVP-필수** | MVP 범위 내 강제, 후속 *완화 불가* | (11) required_evidence (Skill `promotion_status: promoted` 진입 시 ledger entry 의무, §3.4 답습) — **1 건** | `promoted` 상태 전이 시점 (T2 + Evidence §5.3 답습) |
| **MVP-권장** | MVP 권장, 격상 *후* 필수 격상 가능 | (10) forbidden_actions / (12) required_tests / (14) rollback_triggers / (16) created_from — **4 건** | Skill 운영 시점 (best-effort) |
| **후속** | 본 G4 정식 채택 시점 *추가* 필드 후보 | (없음 — 17 필드 enumeration 자체 변경은 별도 합의) | (해당 없음) |

#### 3.6.2 격상 이력 (C-K 흡수 결과)

| 필드 | 이전 (DRAFT) | 이후 (C-K 격상 — 2026-05-09 후속 2) | 사유 |
|------|---------|--------|----|
| (15) `provider_bindings` | 권장 (Skill 작성 시 optional) | **필수** (모든 Skill 의무) | Provider Liquidity (헌법 5조 관용) lock-in 차단 *4-way 보호* (GP-5 + G3 §6.4 + G4 §3.5 + GP-6) 의 *진입점 핵심* — 권장 시 미작성 Skill 의 lock-in 위험 잔존 |
| (11) `required_evidence` | 권장 | MVP-필수 (`promoted` 진입 시) | Evidence Ledger (system-identity-prequel §6.3) 권위 답습 — Skill `promotion_status: promoted` 는 §5.3 PASS 성립 요건 (i)~(iv) 충족 의무. evidence enumeration 의 *형식* 부재는 검증 불가 |

#### 3.6.3 본 §3.6 의 권위 한계

- 본 §3.6 은 *§3.1 schema 본문* 의 표기 정련 까지 — 17 필드 *추가/삭제/이름 변경 0건*
- C-H (provider_bindings lint 룰 강제) 는 본 §3.6 *후속* 영역 — 본 §3.6 은 *schema 차원* 까지, lint 룰 강제 (depcruise + schema validation 자동 차단) 는 Implementation/Runtime PASS 별도 합의
- 본 §3.6 변경 (격상/하향) 자체는 풀 3+1 합의 + ADR Amendment 절차 (T3 변경)

---

## 4. Provider-agnostic Export Format

### 4.1 JSONL 표준

본 §4 는 Memory + Skill 양쪽에 적용되는 *공통* JSONL export/import 형식.

```jsonl
{"type":"memory","scope":"global","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","content":{...},"evidence_refs":["docs/evidence/<task-id>.md"],"prev_hash":"<sha256>","hash":"<sha256>"}
{"type":"memory","scope":"project","id":"<uuid>",...}
{"type":"skill","scope":"project","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","content":{<skill.yaml as JSON>},"evidence_refs":[...],"prev_hash":"<sha256>","hash":"<sha256>"}
...
```

### 4.2 Schema (1 줄 = 1 entry)

| 필드 | 타입 | 필수 | 검증 규칙 |
|------|-----|----|--------|
| `type` | enum | ✅ | `memory` / `skill` |
| `scope` | enum | ✅ | `global` / `project` / `session` / `team` |
| `id` | string | ✅ | UUID v4 또는 slug |
| `schema_version` | string | ✅ | semver (본 G4 schema 의 버전 — 현 `0.1` MVP) |
| `ts` | ISO 8601 | ✅ | entry 생성 timestamp |
| `agent` | string | ✅ | provider-neutral identifier (`user` / `<worker_name>` / `hermes` 등) |
| `content` | object | ✅ | (Memory) 자유 schema, (Skill) §3.1 17 필드 schema 그대로 |
| `evidence_refs` | array\<string\> | 권장 | Markdown evidence 파일 경로 |
| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` |
| `hash` | string (sha256) | ✅ | 본 entry 의 canonical JSON sha256 (변조 방지) |

### 4.3 Hermes 의존 0 보장

**원칙**: Hermes 내부 DB / SDK / plugin 없이도 JSONL entry 를 *읽고 / 검증하고 / import* 할 수 있어야 한다.

| 검증 항목 | 메커니즘 | 권위 |
|---------|--------|-----|
| Hermes 의존 import 0건 | `scripts/hermes-migration/` 변환 스크립트가 `import hermes_agent` 등 의존 0건 | depcruise (G2 GP-5 답습) |
| 표준 도구로 검증 가능 | `jq` 로 parse + sha256 검증 + canonical JSON 검증 가능 | POSIX 표준 |
| schema_version 호환성 | 본 `0.1` 이외 버전은 명시 declaration 후만 import 가능 | §4.5 답습 |
| 외부 오케스트레이터 import 가능 | claude / openai / gemini / local LLM 등 최소 2+ 로 재해석 가능 | §3.5 + GP-6 답습 |

### 4.4 Hash Chain 변조 방지

**원칙** (system-identity-prequel §6.3 답습):
- JSONL append-only — entry 수정 / 삭제 금지
- hash chain — `prev_hash` + `hash` 로 변조 검출
- 또는 git append commit 으로 변조 방지 (둘 중 하나 의무)

**Canonical JSON 정의** (hash 계산 일관성):
- key 정렬: lexicographic
- whitespace 제거 (separator `","` / `":"` 한정)
- numeric 정규화: integer 는 정수 형식 / float 는 IEEE 754
- string escape: 표준 RFC 8259

**Genesis hash**: `sha256("genesis:<scope>:<schema_version>")` — 첫 entry 의 `prev_hash`

### 4.5 Migration Script 사양 (구현은 본 초안 외)

> **본 §4.5 는 *사양*까지만 정의** — 실 migration script 구현은 본 초안 범위 외 (§0.2 #8 답습).

#### 4.5.1 변환 스크립트 후보

| 산출 후보 | 방향 | 검증 |
|---------|-----|-----|
| `scripts/hermes-migration/hermes_to_claude.py` | Hermes JSONL → Claude Code 형식 | 라운드트립 PoC (R2-5 답습) |
| `scripts/hermes-migration/hermes_to_openai.py` | Hermes JSONL → OpenAI 형식 | 라운드트립 PoC |
| `scripts/hermes-migration/hermes_to_ollama.py` | Hermes JSONL → Ollama 형식 (선택) | 라운드트립 PoC |
| `scripts/hermes-migration/import.py` | 외부 형식 → 본 G4 JSONL | round-trip + checksum 검증 |

#### 4.5.2 변환 스크립트 사양 요건

- Hermes 의존 0건 (depcruise 검증)
- 표준 라이브러리 + 표준 dependencies 만 사용 (provider SDK 직접 import 금지 — §6.4 답습)
- 라운드트립 검증: `export → 변환 → import → re-export → 원본 hash 일치` (또는 의미 보존 검증)
- schema_version 명시
- `--dry-run` flag 지원 (검증 only)

### 4.6 라운드트립 검증 절차

```
[원본 Hermes JSONL]
       │
       │ ① hermes_to_claude.py 변환
       ↓
[Claude 형식]
       │
       │ ② Claude → 다시 본 G4 JSONL 형식으로 변환
       ↓
[재변환 JSONL]
       │
       │ ③ canonical JSON sha256 비교
       ↓
[원본 hash 일치 검증]   ← Provider-agnostic 보장
```

**검증 PASS 조건**:
- hash 일치 (정확 round-trip) **또는** 의미 보존 검증 (사용자 명시 review — 손실 허용 영역 명시)
- 손실 발생 시 손실 영역 ledger entry (`event: roundtrip_lossy`)

---

## 5. Memory / Skill Boundary

### 5.1 정의

| 분류 | 정의 | 예시 |
|------|------|------|
| **Memory** | 사실 / 결정 / 선호 / 상태 / 근거 | "이 프로젝트는 Python 3.11 사용", "사용자는 한국어 소통 선호", "G1b PASS 2026-05-07", "헌법 5조 = Provider Liquidity 관용" |
| **Skill** | 반복 가능한 절차 / 입력 / 출력 / 권한 / 검증 조건 | "PR 생성 스크립트 (input=branch, output=URL, action=git)", "테스트 실행 절차 (input=test_path, output=verdict)" |

**핵심 차이**:
- Memory 는 *상태* / *지식* — 시점-의존, 사실 누적
- Skill 은 *절차* / *행위* — 반복 가능, 입력-출력 명세

### 5.2 4 금지 사항 (사용자 명시 답습)

| # | 금지 | 사유 | 강제 메커니즘 |
|---|-----|-----|----------|
| 1 | **Memory 가 policy 를 대체** | Constitution / ADR / SDD 본문이 Memory 로 *옮겨가면* 권위 위계 우회 (Hermes 가 Memory write 가능 시 정책 변경 위험) | G3 §2.2 #9 / #11 (T3) + Memory write 권한 0 (사용자만) |
| 2 | **Skill 이 ADR / Constitution 우회** | Skill 본문이 ADR / Constitution 본문을 자동 수정 / override 시도 | G3 §2.2 #10 / #11 (T3) + skill `allowed_actions` 에 `policy_write` 등 미포함 |
| 3 | **Session memory 가 global memory 로 자동 승격** | Session 임시 상태가 Global 영구 정책 으로 leak | §2.5 promotion T2 강제 + filesystem ACL |
| 4 | **Hermes 가 skill 을 자기 승인** | Hermes 가 `proposed` → `approved` / `promoted` 자동 진행 시 자기 격상 (G3 §2.2 #14 / §4.5 답습) | G3 §2.2 #16 (T2) + promotion hook 차단 + 사용자 명시 강제 |

### 5.3 본 §5 가 *하지 않는* 것

- ❌ Memory 와 Skill 의 *세부 구별 매트릭스* (예: "이 항목은 Memory 인가 Skill 인가" 분류 도구) — 사용자 review 영역
- ❌ Memory 와 Skill 의 *상호 변환* — 본 G4 는 양쪽이 *분리된* 경우만 다룸
- ❌ Boundary 위반 자동 정정 — 위반 검출 시 BLOCK + 사용자 명시 결정

---

## 6. G3 인터페이스 (5 항목)

> **본 §6 은 G3 (`hermes-not-root-of-trust-runtime.md`) §6.5 / §7 답습** — G4 = *형식*, G3 = *권한* 분리.

### 6.1 Skill Escalation 방지

**G3 §3.3 답습**: Skill 이 정의된 권한 등급 (`allowed_actions`) 을 *넘어* 작동 시 차단.

| 메커니즘 | G4 책임 (형식) | G3 책임 (권한) |
|--------|------------|--------------|
| Skill schema `allowed_actions` 필드 | ✅ §3.1 #9 | (위임) |
| Skill schema `forbidden_actions` 필드 | ✅ §3.1 #10 | (위임) |
| 권한 등급 enum 정의 | ✅ §3.2 (`read` / `write` / `shell` / `network` / `db` / `git` / `docker`) | (위임) |
| Wrapper 권한 검증 (실 runtime) | (위임) | ✅ G3 §3.3.3 |
| Sandbox cap_drop / read_only / tmpfs noexec | (위임) | ✅ G3 §3.3.3 |
| Audit log on escalation 시도 | (위임) | ✅ G3 §3.3.4 |
| 자동 비활성화 + 사용자 alert | (위임) | ✅ G3 §3.3.5 |

**인터페이스**: G4 = `allowed_actions` / `forbidden_actions` 필드 *정의*, G3 = wrapper *검증* + 자동 비활성화. 둘이 결합 시 escalation 차단의 *완결성*.

### 6.2 Hermes-originated Skill Auto-approval 금지

**G3 §2.2 #16 + §3.4 답습**: Hermes 가 Skill `proposed` → `approved` / `promoted` 자동 진행 시도 차단.

| 메커니즘 | G4 책임 (형식) | G3 책임 (권한) |
|--------|------------|--------------|
| Skill `promotion_status` 필드 + 5 상태 | ✅ §3.1 #13 + §3.3 | (위임) |
| 상태 전이 규칙 명시 | ✅ §3.3 | (위임) |
| Hermes-originated commit auto-reject (Skill 본문) | (위임) | ✅ G3 §2.2 #20 + §3.1 |
| `approved` 진입 시 사용자 명시 승인 강제 | (위임) | ✅ G3 §2.2 #16 (T2) |
| `promoted` 진입 시 Tools 검증 + Evidence 강제 | (위임) | ✅ G3 §5.3 (i)~(iv) |

**인터페이스**: G4 = 상태 전이 *형식*, G3 = 상태 전이 *권한* (사용자 명시 / Evidence 강제). 둘이 결합 시 auto-approval 차단의 *완결성*.

### 6.3 Evidence 없는 Skill Promotion 금지

**G3 §1.3 + §5.3 답습**: 모든 PASS 판정 = Evidence Ledger 기록 의무.

| 메커니즘 | G4 책임 (형식) | G3 책임 (권한) |
|--------|------------|--------------|
| Skill `required_evidence` 필드 | ✅ §3.1 #11 | (위임) |
| Skill `required_tests` 필드 | ✅ §3.1 #12 | (위임) |
| Skill `last_verified_at` 필드 | ✅ §3.1 #17 | (위임) |
| Evidence Ledger entry 생성 강제 | (위임) | ✅ G3 §1.3 + §5.3 |
| Promotion 시 ledger entry 존재 검증 | (위임) | ✅ G3 §5.3 (ii) |
| Hash chain 변조 방지 | ✅ §4.4 (G4 형식) | ✅ G3 §1.3 (운영 강제) |

**인터페이스**: G4 = Evidence reference *형식*, G3 = Evidence 존재 *강제*. 둘이 결합 시 promotion 의 *완결성*.

### 6.4 Provider Lock-in 방지

**G2 GP-5 + G3 §6.4 답습**: Hermes / litellm / anthropic / openai 직접 import 또는 모델명 분기 코드 차단.

| 메커니즘 | G4 책임 (형식) | G2 GP-5 (코드 lock-in) | G3 §6.4 (Hermes-originated) |
|--------|------------|---------------------|------------------------|
| Skill `provider_bindings` 필드 (provider-neutral 보장) | ✅ §3.1 #15 + §3.5 | (위임) | (위임) |
| `provider_bindings` 검증 규칙 (required / exclusive 금지) | ✅ §3.5 | (위임) | (위임) |
| 최소 2 provider 재해석 가능 | ✅ §4.3 | (위임) | (위임) |
| Provider SDK 직접 import 차단 (모든 작성 주체) | (위임) | ✅ depcruise 룰 | (위임) |
| Hermes-originated lock-in 변경 차단 (작성 주체 = Hermes 한정) | (위임) | (위임) | ✅ G3 §2.2 #18 + §6.4 |
| 모델명 분기 코드 차단 | (위임) | ✅ depcruise 룰 | (위임) |
| Migration script Hermes 의존 0건 | ✅ §4.3 + §4.5.2 | ✅ depcruise | (위임) |

**3-way 인터페이스**: G4 = `provider_bindings` *형식*, G2 GP-5 = *코드 lock-in 차단* (모든 작성 주체), G3 §6.4 = *Hermes-originated 변경 차단*. 셋이 결합 시 Provider Liquidity 의 *완결성*.

### 6.5 Memory Poisoning Rollback

**G3 §3.1 (Learning silent drift) + §3.3 (Skill escalation) 답습**: Memory / Skill 본문에 악성/잘못된 정보 누적 시 차단 + rollback.

| 메커니즘 | G4 책임 (형식) | G3 책임 (권한) |
|--------|------------|--------------|
| Memory entry 의 `evidence_refs` 필드 (출처 추적) | ✅ §4.2 | (위임) |
| Skill `created_from` 필드 (출처 추적) | ✅ §3.1 #16 | (위임) |
| Skill `rollback_triggers` 필드 | ✅ §3.1 #14 | (위임) |
| Hash chain 변조 방지 | ✅ §4.4 | ✅ G3 §3.1 |
| Memory poisoning 검출 (T1 분석) | (위임) | ✅ G3 §3.1.2 + §3.3.2 |
| Rollback (Memory revert / Skill `revoked`) | (위임) | ✅ G3 §3.1.5 + §3.3.5 |
| 사용자 alert + 명시 결정 | (위임) | ✅ G3 §3.1.6 + §3.3.6 |

**인터페이스**: G4 = 출처 추적 *형식* + rollback trigger *형식*, G3 = 검출 + rollback *권한*. 둘이 결합 시 Memory poisoning 차단의 *완결성*.

### 6.6 §6 통합 — G3 ↔ G4 책임 분리 매트릭스

| G3 §6.5 / §7 책임 | G4 본 §6 인터페이스 |
|---------------|---------------|
| Memory promotion 권한 (T2 사용자 명시) | §2.2 promotion 조건 (manual only) |
| Skill promotion 권한 (T2) | §3.4 자동 생성 vs 자동 승격 분리 |
| Skill escalation 차단 | §6.1 `allowed_actions` / `forbidden_actions` |
| Hermes-originated commit auto-reject (Skill) | §6.2 `promotion_status` 전이 |
| Evidence 없는 promotion 금지 | §6.3 `required_evidence` / `required_tests` |
| Provider lock-in 차단 (Hermes-originated) | §6.4 `provider_bindings` |
| Memory poisoning rollback | §6.5 `evidence_refs` / `created_from` / `rollback_triggers` |

→ G3 = *권한 / 신뢰 / 무결성*, G4 = *형식 / schema / export-import*. 두 게이트 모두 PASS 시 (4 게이트 통합 합의 후) 격상 충분 조건 일부 충족.

---

## 7. G2 GP-6 인터페이스

### 7.1 G2 GP-6 ↔ G4 책임 분리

**G2 GP-6** (`governance-preconditions.md` §8) 책임: Memory / Skill 의 *마이그레이션 가능성* 검증 (JSONL 표준 + 변환 스크립트 + 라운드트립 검증).

**G4** (본 문서) 책임: GP-6 의 *실제 형식 / schema 제공*.

| 항목 | G2 GP-6 (가능성 검증) | G4 (형식 제공) |
|------|---------------------|------------|
| JSONL schema | (위임 — G4 정의) | ✅ §4.2 |
| Hash chain 변조 방지 | (위임) | ✅ §4.4 |
| Schema_version 호환성 | (위임) | ✅ §4.3 |
| 변환 스크립트 사양 | (위임) | ✅ §4.5 |
| 변환 스크립트 *실 구현* | ✅ GP-6 §8.6 산출 후보 | (G4 범위 외 — §0.2 #8) |
| 라운드트립 자동 테스트 | ✅ GP-6 §8.3 강제 메커니즘 + R2-5 답습 | ✅ §4.6 절차 정의 |
| schema 검증 자동 테스트 | ✅ GP-6 §8.3 | ✅ §4.2 검증 규칙 |
| Hermes 메이저 업데이트 시 자동 회귀 | ✅ GP-6 §8.5 (d) | (위임) |
| 합의 보고서 (G4 + GP-6 통합 가능) | ✅ GP-6 §8.5 (e) | ✅ 본 §8.3 |

### 7.2 GP-6 ↔ G3 ↔ G4 3-way 인터페이스

G3 §6.5 답습:

| 측면 | G2 GP-6 (Migration 가능성) | G3 (권한 + Promotion + Escalation) | G4 (형식 + Schema, 본 문서) |
|------|------------|------|------|
| JSONL 형식 + 변환 스크립트 사양 | ✅ | (위임) | ✅ §4 |
| 라운드트립 검증 절차 | ✅ R2-5 답습 | (위임) | ✅ §4.6 |
| Memory promotion **manual only** | (위임) | ✅ §2.2 #15 | (위임) |
| Skill 등록 **T2 사용자 명시 승인** | (위임) | ✅ §2.2 #16 + §3.4 | (위임) |
| Skill 권한 escalation 차단 | (위임) | ✅ §3.3 | (위임) |
| Memory / Skill schema 정의 | (위임) | (위임) | ✅ §2 + §3 |
| Memory / Skill export / import 구조 | ✅ Migration 측면 | (위임) | ✅ Schema 측면 |

**3-way 결합 시**: GP-6 *가능성* + G3 *권한* + G4 *형식* = Memory/Skill lock-in 차단의 *완결성*.

### 7.3 G2 GP-6 후속 갱신 권고

본 G4 정식 채택 시점에 GP-6 §8.5 (e) Exit 기준에 G4 cross-reference 추가 권고:
> "(e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-6 + **G3 §6.5** + **G4** 통합 가능)"

(G3 단축 검토 §3.1 P-2 답습 — G2 후속 갱신 권고와 통합)

---

## 8. Acceptance Criteria (Exit)

### 8.1 8 Exit 조건 (사용자 명시 답습)

| # | 조건 | 검증 방식 | 본 초안 충족 여부 |
|---|------|---------|---------------|
| (i) | Memory scope 4 단계 정의 완료 | §2 본문 (Global / Project / Session / Team-Agent 모두 정의) | ✅ 본 초안에서 충족 |
| (ii) | MVP scope (Global + Project) 명시 | §2.1 + §2.2 | ✅ |
| (iii) | Skill schema 17 필드 정의 완료 | §3.1 + §3.2 | ✅ |
| (iv) | JSONL export / import 형식 정의 완료 | §4.1 + §4.2 + §4.4 | ✅ |
| (v) | Provider lock-in 방지 조건 명시 | §3.5 + §4.3 + §6.4 | ✅ |
| (vi) | Promotion / revocation 규칙 명시 | §3.3 + §3.4 + §2.2 (manual only) | ✅ |
| (vii) | G2 / G3 인터페이스 명시 | §6 (G3 5 항목) + §7 (G2 GP-6) | ✅ |
| (viii) | **Hermes PMO 격상 선언 없음** | 헤더 + §0.2 #3 + 종료 줄 명시 부정 | ✅ 격상 선언 0건 |

본 (i) ~ (viii) 8 조건은 **본 초안 자체에서 충족**. G4 PASS 합의는 추가로 다음 조건 필요:

| # | 추가 조건 (G4 PASS 한정, 본 초안 외) | 산출 |
|---|------------|-----|
| (a) | 동등 이상의 보안 결과 (Provider Liquidity 측면) | provider-neutral schema PoC |
| (b) | 격리 환경 PoC 실증 — 라운드트립 검증 (R2-5 답습) | `scripts/hermes-migration/*` 구현 + 라운드트립 테스트 |
| (c) | ADR / SDD 권위 명시 | ADR-008 차단조건 #2 cross-reference + 신규 ADR-014 후보 |
| (d) | 자동 회귀 검증 경로 확보 | CI step (export → 변환 → schema 검증) |
| (e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (외부 LLM 의견 권장) |

### 8.2 Entry 기준

- ✅ ADR-008 차단조건 #2 (JSONL export 표준) 명시 (충족됨)
- ✅ ADR-008 부록 A.2 (Hermes sessions export 공식 명령 검증) (충족됨)
- ✅ G1b PASS (2026-05-07, 충족됨)
- ✅ G2 DRAFT 적격 검토 APPROVE (2026-05-07, 충족됨)
- ✅ G3 DRAFT 적격 검토 APPROVE (2026-05-07, 충족됨)
- ⏳ 사용자 명시 G4 작업 진입 결정 (현 단계 — 본 초안 작성)

### 8.3 G4 PASS 합의 형태 (사용자 결정 후보, 본 초안은 *권고 단정 금지*)

| 옵션 | 합의 형태 | 비고 |
|-----|---------|-----|
| 1 | G4 단독 단축 합의 (Reviewer-only) | 본 초안에 새 권위 결정 0건 (ADR-008 차단조건 #2 답습 + system-identity-prequel §8.4 흡수) — 단축 합의 적격 |
| 2 | G4 + G2 GP-6 통합 합의 (단축 또는 풀 3+1) | GP-6 §8.5 (e) 답습 |
| 3 | G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 1+ (PR 묶음) | **격상 통합 합의 답습** — P2 v3 §9.2 / G2 §10.2 / G3 §8.2 옵션 3 패턴 |

**참고** (사용자 결정 후보, 권고 단정 금지): 옵션 3 = G2/G3/G4 통합 풀 3+1 + 외부 LLM 1+ 가 메타 편향 통제 + PR 묶음 + Hermes PMO 격상 통합 합의 답습 시 비용 효율적. 단, 옵션 1 / 2 도 사용자 결정 시 정당.

### 8.4 G4 통합 Exit *선언* 절차 (사용자 명시 답습)

본 G4 PASS 합의 APPROVE 시점에 다음이 *발생*:
- ✅ G4 status: 미작성 → PASS (CONTEXT.md 4 게이트 진행 상태 갱신)
- ✅ 본 문서 헤더 "DRAFT" 제거 + 합의 보고서 cross-reference 추가
- ✅ ADR-008 차단조건 #2 cross-reference 갱신 + ADR-009 cross-reference 갱신 + 신규 ADR-014 후보 검토 (별도 PR)

본 G4 PASS 합의 APPROVE 시점에 *발생하지 않는* 것:
- ❌ G2 / G3 자동 PASS
- ❌ Hermes PMO 격상 자동 활성화
- ❌ P2 v3 정식 채택 자동
- ❌ system-identity-prequel.md / P2 v2 자동 archive
- ❌ ADR 본문 자동 갱신 (cross-reference 만)
- ❌ 실 runtime 코드 / migration script 자동 구현

---

## 9. 영구 핵심 제약 (변동 없음)

본 G4 작업 + G4 PASS + Hermes PMO 격상(미래) 전 과정에서 다음은 **무조건 영구 유지**:

| 제약 | 권위 근거 | 본 G4 보호 위치 |
|------|---------|----------|
| **Provider Liquidity** | 헌법 5조 (관용) + `feedback_provider_liquidity.md` + ADR-008 차단조건 #2 | §3.5 + §4.3 + §6.4 (3-way 보호) |
| **Hermes ≠ root of trust** | ADR-011 §2.3 (영구 권위) | §2 (Memory 사용자 owner) + §3.4 (Skill 사용자 승인) + §5.2 (4 금지) + §6 (G3 인터페이스) |
| **메타포 강제 금지** | system-identity-prequel §7 (P2 v3 §10 흡수) | §2.4 Team/Agent 보류 (메타포 인플레이션 차단) |
| **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 | §2.5 promotion T2 강제 + §3.4 Skill 자동 승격 금지 + §5.2 4 금지 |
| **수단/목적 분리 원칙** | ADR-011 §2.1 (a)~(d) → 본 §8.1 (a)~(e) 패턴 답습 | §8.1 |

---

## 10. 본 초안의 변경 절차

본 G4 통합 설계 초안은 DRAFT 상태에서 다음 절차를 따른다:

| 변경 유형 | 절차 |
|---------|------|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| §2 ~ §4 본문 갱신 (Memory scope / Skill schema / JSONL 형식) | 단축 합의 (Reviewer-only) |
| §3.1 17 필드 schema 본문 갱신 | 단축 합의 — 단, 필드 *추가* 는 schema_version 증가 (semver MINOR) |
| §3.5 `provider_bindings` 검증 규칙 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — Provider Liquidity 핵심) |
| §4.4 hash chain 변조 방지 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — Evidence 무결성 핵심) |
| §5.2 4 금지 사항 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경) |
| §6 G3 인터페이스 5 항목 갱신 | 단축 합의 — G3 본문 변경 시 동시 갱신 |
| §7 G2 GP-6 인터페이스 갱신 | 단축 합의 — GP-6 본문 변경 시 동시 갱신 |
| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 § (a)~(e) 충족 검증 + 외부 LLM 의견 권장 (G3 §4.4.2 답습) |
| §9 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |

---

## 11. 메타 편향 자기진단

본 초안은 다음 5 통제 수단을 명시 답습한다:

1. **사용자 명시 절차 답습**: G4 PASS 선언 / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 runtime 코드 / 실 migration script 모두 본 초안 범위 외 (§0.2).
2. **R-7 SOP §0 핵심 선언 답습**: §8.1 8 Exit 조건 + §8 (a)~(e) 추가 G4 PASS 조건 — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 패턴 답습.
3. **ADR-011 §2.4 T1/T2/T3 답습**: §2.5 Memory promotion T2, §3.4 Skill 자동 생성 T1 / 자동 승격 T2 / Tools 검증 T2+Evidence, §5.2 4 금지 (T3 영역).
4. **수단/목적 분리 원칙 답습**: §3.5 `provider_bindings` *provider-neutral 보장* (수단=binding, 목적=Provider Liquidity), §4 JSONL 형식 (수단=JSONL, 목적=Hermes 의존 0).
5. **본 초안이 *하지 않는* 것 명시 (§0.2 + §8.4)**: 11건 명시 부정.

본 5 통제는 P2 v3 / G2 / G3 DRAFT 검토 5 통제 + G1b PASS 단축 합의 5 통제 답습 — G2 → G3 → G4 → Hermes PMO 격상 전 과정 동일 패턴 유지.

### 11.1 본 초안의 메타 한계

- 본 초안은 *자기 작성 산출* (P2 v3 / G2 / G3 / G4 모두 동일 컨텍스트). **G3 §4.4.2 답습**: 자기 작성 산출 검증은 외부 LLM 의견 *권장* — 본 초안 정식 채택 시점에 외부 LLM 의견 의무화 가능.
- §3.1 17 필드 schema 는 *본 초안 원안* — 합의 §164 / 합의 §103 (Memory 2단계) / 합의 §103 (Skill 자동 추출 T1) 흡수했으나 *17 필드 자체* 는 본 초안 첫 명시. 후속 합의에서 필드 분류 / 검증 규칙 적정성 검증 대상.
- §2.3 Session Memory + §2.4 Team/Agent Memory 는 *후속 진입 사양 예고* 한정 — 정식 정의는 후속 ADR + 정량 트리거 충족 후. 본 초안에서는 *예고만* 정확.
- §4.4 canonical JSON 정의 — JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고.
- §6.4 3-way 인터페이스 (G2 GP-5 + G3 §6.4 + G4 §3.5 + §4.3) — 본 초안 첫 명시. 후속 합의 검증 대상.
- §7.2 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 — G3 §6.5 와 본 §7.2 동시 명시. G3 단축 검토 §3.1 P-2 와 일관 — GP-6 후속 갱신 권고.

### 11.2 본 초안의 *PASS 판정 트리거하지 않는 것*

본 초안은 G4 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*. 다음 모두 본 초안 범위 외:
- ❌ G4 PASS 선언
- ❌ G2 / G3 PASS 선언
- ❌ Hermes PMO 격상
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ 실 runtime 코드 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 등)
- ❌ 실 migration script (`scripts/hermes-migration/*.py`)

본 초안 정식 채택 (§10 절차) 도 *G4 PASS* 가 아니라 *G4 통합 설계 문서* 의 채택 한정.

### 11.3 본 초안이 *지금 강제하는* 것 (DRAFT 상태에서도)

본 초안 자체는 *임시 권위* (DRAFT) 이지만, 다음을 *즉시 강제* 한다:

1. system-identity-prequel §8.4 (Memory 2단계 + Project → Global manual only) 답습 — prequel archived 후에도 본 G4 §2.2 + §2.5 권위로 보존
2. ADR-008 차단조건 #2 (JSONL export) 답습 — 본 G4 §4 가 차단조건 #2 의 *형식 정의*
3. ADR-011 §2.4 T1/T2/T3 답습 — 본 G4 §2.5 + §3.4 + §5.2 모두 T 분류 강제
4. G3 §6.5 / §7 답습 — 본 G4 §6 / §7 가 G3 책임 분리의 *형식 측면 흡수*
5. G2 GP-6 답습 — 본 G4 §7 이 GP-6 의 *형식 제공* 측면 흡수

본 5건 즉시 강제는 **본 G4 가 정식 채택되지 않더라도** 현 시점에서 유효 — *Hermes 가 4 게이트 통과 전 ADR-008 합의 자동화 + R-6 CI 회귀 검증* 책임 한정으로 작동하는 현 상태에 적용.

### 11.4 G4 후속 권고 P-1 ~ P-5 흡수 진행 상태 (C-L 흡수 — 2026-05-09 후속 2)

> **본 §11.4 는 합의 보고서 §11.2 P1 조건 C-L 흡수** (출처: `3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` §3.1 자기 발견 잠재 위험 5건). G4 DRAFT 검토 시점 (2026-05-09 첫 검토) 자기 발견 5 후속 권고 P-1 ~ P-5 의 *처리 시점·방법* 을 명시 기록.

| # | 위험 (G4 검토 §3.1) | 처리 시점 | 처리 방법 |
|---|------------|--------|--------|
| **P-1** | §11.1 자기 명시 한계 — RFC 8785 JCS 미인용 (self-disclosed) | **PR-2 풀 3+1** (ADR-012 + G4 §4.4 hash chain 사양 보강 — C-G 흡수와 *동시*) | §4.4 본문에 RFC 8785 JCS 명시 인용 + canonical JSON 사양 보강 (별도 PR-2) |
| **P-2** | §10 schema 진화 정책 — 필드 *제거* / *변경* 정책 미명시 | **PR-2 풀 3+1** (ADR-012 와 *동시*) 또는 **본 PR-1 §10 보강** | §10 변경 절차 표에 "필드 *추가* / *제거* / *이름 변경* / *타입 변경*" 4 행 추가 + schema_version 증가 정책 명시 (본 §11.4.1 권고) |
| **P-3** | §4.5 외부 형식 import 시 schema_version declaration 절차 약함 | **PR-2 풀 3+1** (G4 §4.5 보강과 *동시*) 또는 별도 합의 | §4.5 import 시 schema_version 검증 + 호환성 매트릭스 명시 |
| **P-4** | §6.4 "3-way 인터페이스" 명명 정확성 — 실제 G4 두 § (§3.5 + §4.3) + GP-5 + G3 §6.4 = 4-way | **PR-1 본문 보강** (현 §11.4.2 흡수) | §6.4 명명 "3-way" → "4-way" 정정 또는 *별 명명* (예: "Provider Liquidity Multi-layer Defense") — 본 §11.4.2 답습 |
| **P-5** | §2.2.1 Global Memory `~/.claude/global/` Claude Code 표준 디렉토리 충돌 가능성 | **Implementation/Runtime PASS** 합의 (실 path 결정 시점) | 별도 합의 — Claude Code 표준 디렉토리 구조 점검 후 path 정정 또는 prefix 추가 |

#### 11.4.1 P-2 schema 진화 정책 보강 (본 §10 흡수)

§10 변경 절차 표에 다음 4 행 *추가* (본 §11.4.1 = §10 답습 답습):

| 변경 유형 | 절차 |
|---------|------|
| §3.1 17 필드 schema *추가* | semver MINOR 증가 (예: 1.0.0 → 1.1.0) + 단축 합의 + import 시 backward compatibility 보장 |
| §3.1 17 필드 schema *제거* | semver MAJOR 증가 (예: 1.0.0 → 2.0.0) + **풀 3+1 합의 + ADR Amendment 절차** + migration script 의무 (§4.5 답습) |
| §3.1 17 필드 schema *이름 변경* | semver MAJOR 증가 + **풀 3+1 합의 + ADR Amendment 절차** + alias 호환성 1 release 유지 |
| §3.1 17 필드 schema *타입 변경* | semver MAJOR 증가 + **풀 3+1 합의 + ADR Amendment 절차** + migration script 의무 |

**schema_version 핀**: §4.2 JSONL `schema_version` 필드 (본 §4.2 답습) 가 변경 시점에 증가. import 시 `schema_version` 호환성 검증 의무 (§4.5 답습).

#### 11.4.2 P-4 "3-way" 명명 정정 (본 §6.4 + §3.5 + §4.3 흡수)

**이전 명명**: "3-way 인터페이스" (G2 GP-5 + G3 §6.4 + G4 §3.5 + §4.3 → 4 위치이지만 3 게이트로 카운트)

**정정 명명**: **"Provider Liquidity 4-way Multi-layer Defense"**:
- Layer 1: G2 GP-5 (depcruise 룰 + P1 facade 단일 진입점) — *모든 작성 주체* 의 코드 lock-in 차단
- Layer 2: G3 §6.4 (Hermes-originated lock-in 변경 시도 차단) — *Hermes 작성 주체* 한정
- Layer 3: G4 §3.5 (`provider_bindings` schema *required*/*exclusive* 금지) — *Skill 메타데이터* 차원
- Layer 4: G4 §4.3 (JSONL Hermes 의존 0 + 최소 2 provider 재해석 가능) — *export format* 차원

**4 layer 모두 충족** 시 Provider Liquidity 의 *완결성* 확보. 1 layer 만 깨져도 lock-in 위험 잔존 (예: schema OK + JSONL OK 이지만 P1 facade 우회 코드 작성 = lock-in 가능).

본 §6.4 / §3.5 / §4.3 본문 자체는 *용어* 갱신 외 변경 0건 (본 §11.4.2 가 **명명 정정 명시 기록** 한정).

#### 11.4.3 G3 4 후속 권고 잔여 (G3 검토 §3.1 P-1~P-4) 흡수 진행 상태

> **본 §11.4.3 은 합의 보고서 §11.2 P1 조건 C-L 의 G3 4건 부분** (출처: `3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` §3.1 자기 발견 P-1~P-4). G3 DRAFT 검토 (2026-05-07) 시점 자기 발견 4건 처리 진행 상태.

| # | G3 검토 §3.1 후속 권고 | 처리 시점 | 흡수 위치 |
|---|--------------|--------|--------|
| G3 P-1 | §1.2.4 추가 위반 경로 후보 명시 권고 | 본 PR-1 G3 §3 (이미 G3 §3.1~§3.3 으로 흡수 완료, 2026-05-07 단축 검토 §6.1 답습) | (이미 흡수) |
| G3 P-2 | §6 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 후속 갱신 | 본 PR-1 G3 §6.5 + G2 §10 (이미 §6.5 / §7.2 GP-6 cross-reference 명시 완료) | (이미 흡수) |
| G3 P-3 | §4.4.2 외부 LLM 권장/필수 적용 시점 명확화 | 본 PR-1 G3 §4.7 (C-E 흡수와 *동시*) — 메타-순환 청산 §4.7.1 (a) | §4.7.1 (a) |
| G3 P-4 | §5.2 #5 G2 §9 메타 안전장치 ↔ G3 §5.5 위임 명확화 | 본 PR-1 G3 §5.5 (C-F 흡수와 *동시*) — SPOF accepted risk 본문 G3 §5.5 + G2 §9.5 분리 | §5.5 + G2 §9.5 |

G3 4건 후속 권고 모두 **본 PR-1 흡수 완료** (별도 후속 권고 잔여 0건).

#### 11.4.4 본 §11.4 가 *하지 않는* 것

- ❌ §4.4 RFC 8785 JCS 본문 인용 (PR-2 풀 3+1 영역 — C-G 흡수와 *동시*)
- ❌ §10 본문 자동 갱신 (본 §11.4.1 은 *권고 사양* 명시까지, §10 본문 변경은 PR-2 또는 별도 합의)
- ❌ §6.4 / §3.5 / §4.3 본문 *용어 자동 갱신* (본 §11.4.2 는 *명명 정정 명시 기록* 까지)
- ❌ P-5 (`~/.claude/global/` path 정정) 자동 처리 (Implementation/Runtime PASS 영역, 별도 합의)
- ❌ P-3 (§4.5 import schema_version 검증) 자동 구현 (PR-2 또는 별도 합의)

---

**작성일**: 2026-05-07
**상태**: DRAFT (초안)
**다음 진입점**: 사용자 결정 — Reviewer-only 단축 검토 (DRAFT 적격 판정) → DRAFT 보고서 별도 commit → G2/G3/G4 정식 채택 합의 준비
**금지 (사용자 명시 답습, 변동 없음)**:
- ❌ G4 PASS 선언 자동
- ❌ G2 / G3 PASS 선언 자동
- ❌ Hermes PMO 격상 선언 자동
- ❌ P2 v3 정식 채택 자동
- ❌ ADR 본문 자동 갱신
- ❌ P2 v2 / prequel archive 자동 처리
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
