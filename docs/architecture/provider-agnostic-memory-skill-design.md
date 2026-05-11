# Provider-agnostic Memory / Skill Design (G4) — Design/Governance Gate PASS (Bundled, 2026-05-09)

> **상태: Design/Governance Gate PASS (Bundled, 2026-05-09)**. Hermes PMO 격상 4 게이트 중 **G4** — Memory 와 Skill 이 특정 provider / 특정 DB / 특정 내부 포맷에 lock-in 되지 않도록 *공통 schema + 운영 규칙 + JSONL export/import 형식* 을 정의하는 통합 설계 문서. **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접 컨텍스트) APPROVE WITH CONDITIONS** (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`).
>
> **PASS 범위 한정 (P0 조건 C-A, 5/5 입력 일치)**: 본 PASS 는 *Design/Governance Gate PASS* 한정 — Memory scope 4 단계 (MVP Global+Project) / Skill schema 17 필드 / JSONL export hash chain 변조 방지 / Memory/Skill boundary 4 금지 / G3 인터페이스 5 항목 / G2 GP-6 인터페이스의 *설계 승인* 에 한정한다. **Implementation/Runtime PASS 는 본 PASS 에 포함되지 않는다** — 실 migration script (`hermes_to_claude.py` / `hermes_to_openai.py` 등) 구현 + 라운드트립 PoC 실증 + hash chain canonical JSON 사양 보강 (canonical / newline / encoding / field ordering / genesis / prev_hash 검증 실패 처리 / full rewrite 방어 / round-trip lossy ledger) + provider_bindings lint 룰 강제는 *별도 합의* 로만 발생.
>
> **G4 라운드트립 / migration script 상태 (P0 조건 C-B, 5/5 입력 일치)**: **DESIGN PASS / IMPLEMENTATION PENDING** (§4 변환 스크립트 사양까지만, 실 PoC 미실증 — 합의 보고서 §6 갱신 권고 흡수 시점에 별도 합의).
>
> **PR-2 보강 흡수 (2026-05-09 풀 3+1 합의 + 외부 LLM 2건)**: **§4.2 schema 11 필드 (10 → 10 + `event` 신규) + §4.4 hash chain 사양 보강 (Layer 1~5 다층 강제 + RFC 8785 JCS Primary + fallback + Genesis Hash + prev_hash 검증 실패 BLOCK + manual + Full Rewrite 5 Layer 방어) + §4.6 round-trip 검증 절차 보강 (Tier-based + 3 ledger entry 형식 + Migration 검증 실패 rollback 조건) — `docs/decisions/ADR-012-evidence-ledger-protection.md` 와 동일 PR commit. 합의 권위: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS). G4 §11.4 P-1 (RFC 8785 JCS) + P-2 (schema 진화 정책) + P-3 (import schema_version) 처리 완료** — P-4 / P-5 는 PR-1 또는 후속 합의 영역 (PR-1 §11.4 답습).
>
> **ADR-012 (Evidence Ledger Protection) Mandatory Reference (2026-05-09 후속 3 PR-2 신규 발행)**: 본 G4 §4.2 11 필드 schema (`event` 신규) + §4.4 hash chain 사양 (Layer 1~5 + RFC 8785 JCS Primary + Genesis Hash + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer) + §4.6 round-trip 검증 절차 (Tier-based + 3 ledger entry 형식 + Migration rollback) 의 *권위 출처*. **G4 §4 = ADR-012 §2.1 ~ §3.5 답습 권위**.
>
> **P2 v3 (`hermes-adoption-design-v3.md`) = Adopted (Design Adoption only, 2026-05-09 후속 6)** 후속 권위. 본 G4 = P2 v3 §6 (G4 정의 + ADR-012 Mandatory Reference cross-reference) + §10.1 #1 (Provider Liquidity 5-way Multi-layer Defense 5 Layer — 본 G4 §3.5 + §4.3 Layer 3/4 + ADR-012 §원칙 6 Layer 5) + §10.2 Archive Migration Note + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화 답습.
>
> **P2 v2 (`hermes-adoption-design.md`) = Archived (옵션 A 최소 침습, 2026-05-09 후속 7)** + **`system-identity-prequel.md` = Archived (옵션 A, 2026-05-09 후속 8 — 본 G4 §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary) 의 *원본 권위 출처* prequel §6.3 + §8.4 → 본 G4 + ADR-012 §1.4 답습 권위 발행으로 archive 후에도 권위 보존)** — 본 G4 cross-reference 영향 0건 (path 변경 0건).
>
> **Hermes PMO 격상은 본 PASS 에 포함되지 않는다** (사용자 명시 답습) — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 (Human-in-the-loop) + 사용자 명시 결정 후 별도 (P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 답습). G4 운영 구현 PASS / ADR 본문 자동 갱신 (신규 ADR-014 후보 검토 포함) / archive 자동 처리도 본 PASS 미포함.

**작성일**: 2026-05-07
**Status (2026-05-07 통합 합의)**: **Design/Governance Gate PASS (Bundled, 2026-05-07)** — `docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md` (4/4 입력 만장일치 APPROVE WITH CONDITIONS — Agent A/B/C + 외부 LLM GPT-5.5 Thinking, 12 통합 조건 + Gap-N 6건 흡수 처리). 본 PASS 는 Design/Governance Gate 한정 — Implementation/Runtime PASS / Operational Readiness PASS / Hermes PMO 격상 / P2 v3 정식 채택 모두 미포함.
**정식 PASS 일자**: 2026-05-09 (Design/Governance Gate PASS, Bundled with G2 + G3 — 2026-05-07 통합 합의의 후속 reaffirmation)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C 내부 + GPT cross-vendor + Claude 인접 컨텍스트)
**§4 hash chain 보강 합의**: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (PR-2 풀 3+1 + 외부 LLM 2건 — ADR-012 발행 + G4 §4.2/§4.4/§4.6 보강, 2026-05-09 후속 3 PR-2)
**산출 방식**: 옵션 B (Memory + Skill 통합 단일 문서) — 사용자 명시 결정 답습. 사유: G4 핵심은 *Memory/Skill 공통 형식 — provider-agnostic schema*. 분리 작성 시 lock-in 방지 *공통 보장*이 약화될 위험.
**상위 권위**: 헌법 제5조 관용 (Provider Liquidity), 헌법 제8조 (보안), ADR-008 차단조건 #2 (JSONL export 표준), **ADR-009 C-N §5 (Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1, 2026-05-09 후속 4 갱신)**, **ADR-012 §원칙 5 + §원칙 6 (Provider Liquidity 5-way Layer 5 — Evidence 형식 차원 provider-neutral 강제)**
**상위 결정**: ADR-008 (Hermes 도입 Option B), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리), **ADR-012 (Evidence Ledger Protection — 본 G4 §4 권위 출처)**
**관련 설계**: **`hermes-adoption-design-v3.md` §6 (G4 정의 — P2 v3 Adopted Design Adoption only, 2026-05-09 후속 6)**, `governance-preconditions.md` §8 (GP-6 Memory/Skill Migration) + §1.2.6 P10 Evidence Forgery 정식 등록, `hermes-not-root-of-trust-runtime.md` §6.5 / §7 (GP-6 ↔ G3 ↔ G4 3-way 인터페이스), `hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7**), `system-identity-prequel.md` §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary) (**Archived 2026-05-09 후속 8** — 본 G4 답습 권위 발행으로 권위 보존), `llm-providers-design.md` (P1 v2 — Option β LiteLLM facade)
**근거 합의**: `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (Memory 2단계 채택 + Skill 자동 추출 T1 한정 + GPT 4단계 미채택 사유), `docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md` (G3 §7 G4 경계 인용), `docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md` (G4 정식 PASS 합의), **`docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (G4 §4 hash chain 보강 — ADR-012 동일 PR commit)**, **`docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (P2 v3 정식 채택 — 본 G4 = P2 v3 §6 답습 권위)**
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
allowed_actions:     # (9)  array<permission_category>, 필수 — §3.7 12-category enum (T1/T2 한정, T3 진입 금지)
forbidden_actions:   # (10) array<permission_category>, MVP-권장 — T3 7-category 자동 포함 강제 (§3.7.3 답습)
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
| 9 | `allowed_actions` | array\<permission_category\> | ✅ | **12 카테고리 semantic enum** (§3.7 답습): `READ_ONLY` / `SUGGEST_ONLY` / `WRITE_DRAFT` / `WRITE_DOCS` / `WRITE_CODE` / `RUN_TESTS` / `RUN_LOCAL_TOOLS` / `NETWORK_ACCESS` / `SECRET_ACCESS` / `POLICY_CHANGE` / `ADR_CHANGE` / `SELF_PROMOTION`. **T1 (자동 가능) 5종 + T2 (사용자 승인) 5종 + T3 (절대 금지) 7종 분류 — `allowed_actions` 에 T3 카테고리 진입 시 schema validation BLOCK** (§3.7 + §3.8 답습) | ⚠️ **T3 카테고리 schema-level 차단 핵심 영역** |
| 10 | `forbidden_actions` | array\<permission_category\> | MVP-권장 | (i) `allowed_actions` 와 disjoint (ii) **T3 7-category 자동 포함 강제** — `SECRET_ACCESS` / `POLICY_CHANGE` / `ADR_CHANGE` (자동 수행) / `SELF_PROMOTION` / `PROVIDER_LOCK_IN_ENFORCE` / `REDACTION_POLICY_RELAX` / `CONSTITUTION_BYPASS` 모두 *명시 작성 여부 불문 강제 포함* (§3.7.3 답습) (iii) 사용자 명시 override 불가 (T3 영역, ADR-011 §2.4) | 0 (T3 강제 차단) |
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

#### 3.4.1 상태 전이 권한 분류

| 단계 | 권한 | 분류 |
|------|-----|------|
| Skill 후보 *추출* (반복 패턴 → `proposed`) | ✅ Hermes / Worker T1 자동 (G3 §2.1 #3) | T1 |
| Skill `proposed` → `approved` | ❌ Hermes 자동 금지 — **사용자 명시 승인 강제** | T2 (G3 §2.2 #16) |
| Skill `approved` → `promoted` | ❌ Hermes 자동 금지 — **Tools 검증 + Evidence ledger entry** 필수 + 사용자 명시 가능 | T2 + Evidence (G3 §5.3 답습) |
| Skill `promoted` → `revoked` | ✅ rollback_trigger 매치 시 자동 revoke (T3 위반 차단 = 자동 안전 동작) | T3 자동 안전 |
| Skill `*` → `archived` | ❌ Hermes 자동 금지 — 사용자 명시 결정 강제 | T2 |

#### 3.4.2 promotion_status × allowed_actions 범위 매트릭스 (**Permission Granularity 세분화 — 2026-05-11**)

> **본 §3.4.2 는 Permission Granularity 세분화 작업 흡수** (§3.7 12 카테고리 + §3.8 self-escalation 차단 답습). promotion_status 별 *허용 가능 permission category 범위* 본문화. **T3 7 카테고리는 모든 promotion_status 에서 차단 — 본 매트릭스 의 *상한*은 T1+T2 한정**.

| `promotion_status` | 허용 가능 카테고리 범위 | 차단 카테고리 | 추가 검증 의무 |
|---------------|----------------|----------|--------|
| `proposed` | **T1 only** (`READ_ONLY` / `SUGGEST_ONLY` / `WRITE_DRAFT` — §3.7.1 답습) | T1 외 모두 차단 (T2 사용 시 schema validation BLOCK + `event: skill_proposed_t2_attempt` ledger entry) | `inputs` + `outputs` schema 정합성 / `description` 본문 / `provider_bindings` §3.5 검증 |
| `approved` | **T1 + T2 일부** (`WRITE_DOCS` / `RUN_TESTS` 추가 — 사용자 명시 승인 후) | T2 중 `WRITE_CODE` / `RUN_LOCAL_TOOLS` / `NETWORK_ACCESS` / `SELF_PROMOTION` 등은 `promoted` 이후만 / T3 전체 차단 | T2 사용자 명시 승인 (G3 §2.2 #16) + Skill schema 통과 |
| `promoted` | **T1 + T2 전체** (T2 5 카테고리 전부 — `WRITE_CODE` / `RUN_LOCAL_TOOLS` / `NETWORK_ACCESS` / provider-specific optimization / skill promotion) | T3 전체 차단 (§3.7.3 + §3.8 답습) | (i) `required_evidence` 모두 통과 (§5.3 답습) (ii) `required_tests` 모두 통과 (iii) Evidence ledger entry append 의무 (`event: skill_promoted` + §4.2 답습) (iv) `last_verified_at` 갱신 (v) §3.8 self-escalation 검증 통과 |
| `revoked` | **READ_ONLY only** (운영 차단 — Skill 본문 / Evidence trail 조회만 가능) | T1 (SUGGEST_ONLY 이상) + T2 + T3 모두 차단 | rollback_trigger 매치 evidence (§6.5 답습) + revocation event ledger entry (`event: skill_revoked` + §4.2 답습) |
| `archived` | **READ_ONLY only** (영구 비활성 — 역사적 조회만 가능) | T1 (SUGGEST_ONLY 이상) + T2 + T3 모두 차단 | 사용자 명시 archive 결정 evidence + archive event ledger entry (`event: skill_archived` + §4.2 답습) |

#### 3.4.3 required_evidence × required_tests × promotion_status 강화 조건 (**Permission Granularity 세분화 — 2026-05-11**)

> **본 §3.4.3 = §3.4.2 의 `promoted` 진입 시 추가 검증 의무 정밀화**. Skill 이 `promoted` 진입 (즉 T2 5 카테고리 전체 권한 활성화) 시 *모든 required_evidence + required_tests 통과 의무* + ledger evidence trail 의무.

**`promoted` 진입 검증 조건 (5/5 충족 의무)**:

1. **`required_evidence` 전체 통과** — enum 모두 (예: `test_pass` + `lint` + `secret_scan` + `consensus` + `review` 등) ledger entry 매치
2. **`required_tests` 전체 통과** — 모든 test_ref 가 PASS verdict (test_result entry)
3. **Skill schema 통과** — `allowed_actions` ⊆ T1+T2 / `forbidden_actions` ⊇ T3 7-category / `provider_bindings` §3.5 검증
4. **§3.8 self-escalation 검증 통과** — 이전 상태 (`approved`) 의 권한 범위에서 *vendor / scope / agent 변경 없음* (§3.8 답습)
5. **Evidence ledger entry append** — `event: skill_promoted` + `content.required_evidence_satisfied: [...]` + `content.required_tests_satisfied: [...]` + `evidence_refs: [...]` (§4.2 답습)

**`promoted` 운영 중 검증** (`last_verified_at` 갱신 의무):

- `required_evidence` 의 하나라도 stale (예: test 실패 / lint 위반 / secret 검출) → **rollback_trigger 매치** → §3.4.2 `revoked` 자동 전이 (T3 자동 안전 동작 — ADR-011 §2.4)
- `last_verified_at` 갱신 주기 = `required_tests` 마지막 PASS 시점 답습 (Implementation/Runtime PASS 영역 — 실 갱신 hook 별도 합의)

**Skill 실행 *전* 검증 의무** (`promoted` 상태):

- 본 §3.4.3 검증 5/5 통과 ledger entry 존재 확인 + `last_verified_at` ≤ TTL (Implementation 영역 — 본 §은 *조건 사양*까지)
- 미통과 시 Skill 실행 BLOCK (`event: skill_execution_blocked` + 사용자 명시 review 의무)

**본 §3.4.3 이 *하지 않는* 것**:
- ❌ TTL 값 자동 결정 (Implementation/Runtime PASS 영역, 별도 합의)
- ❌ 실 ledger entry 자동 작성 (runtime hook 영역)
- ❌ `last_verified_at` 자동 갱신 hook 구현
- ❌ Skill 실행 BLOCK runtime 강제 (Skill wrapper 영역 — G3 §3.3 답습)

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

### 3.7 Permission Granularity Matrix (**Permission Granularity 세분화 — 2026-05-11**)

> **본 §3.7 은 Permission Granularity 세분화 작업 신설**. §3.2 #9 `allowed_actions` / #10 `forbidden_actions` 의 12 카테고리 semantic enum 정의 + T1/T2/T3 분류 매트릭스 + 카테고리별 정의 / 예시 / 권한 범위. **schema-level 차단 layer** (G3 §3.3 runtime wrapper 차단 layer 와 책무 분리 — §6.1 답습). **본 §3.7 = *형식 정의*까지 — 실 schema validator / Skill wrapper runtime hook 구현 = Implementation/Runtime PASS 영역 별도 합의**.

#### 3.7.1 T1 — 자동 가능 카테고리 (5 종)

> Hermes / Worker / Skill 모두 사용자 명시 승인 *없이* 사용 가능. 단, 본 §3.4.2 매트릭스 의 promotion_status 별 범위 한정.

| # | 카테고리 | 정의 | 예시 | promotion_status 진입 시점 |
|---|--------|----|----|-------------------|
| 1 | `READ_ONLY` | 파일 / DB / Memory / Skill / Evidence Ledger 조회만, 변경 0건 | `cat`, `grep`, `git log`, JSONL parse | `proposed` 부터 |
| 2 | `SUGGEST_ONLY` | 출력 / 제안만, commit / write / 실행 0건 | LLM 응답 생성, diff 제안 (적용 X), test plan 제안 | `proposed` 부터 |
| 3 | `WRITE_DRAFT` | 임시 / draft 파일 작성 (`.draft.*` / `/tmp/*` / scratchpad) — 영구 commit 0건 | scratch note, intermediate buffer, dry-run output | `proposed` 부터 |
| 4 | `WRITE_DOCS` (일부) | `docs/sessions/` / `docs/scratch/` 등 *낮은 위험* 문서 영역 작성. **`docs/decisions/` (ADR) / `docs/constitution/` 영역 진입 시 T3 `ADR_CHANGE` / `CONSTITUTION_BYPASS` 로 자동 분류** | session log, scratch memo | `approved` 부터 (사용자 명시 승인 후) |
| 5 | `RUN_TESTS` (일부) | 격리된 test runner 실행 (Docker / venv) — *외부 effect 0건* / *write code 0건* | `pytest`, `cargo test`, `npm test` — read-only test execution | `approved` 부터 |

**T1 강제 제한**:
- 본 5 카테고리 *내부* 도 promotion_status 별 범위 한정 (§3.4.2 매트릭스 답습)
- `WRITE_DOCS` (일부) — `docs/decisions/` / `docs/constitution/` 진입 시 *자동 T3 분류* (ADR-011 §2.4 + ADR-008 부록 C §C.2 답습)
- `RUN_TESTS` (일부) — write effect 동반 test (예: DB migration test) 는 T2 `WRITE_CODE` 로 분류

#### 3.7.2 T2 — 사용자 명시 승인 필요 카테고리 (5 종)

> Hermes / Worker / Skill 사용 *전* 사용자 명시 승인 의무 (ADR-011 §2.4 T2 답습). Skill `promotion_status: promoted` 진입 후 활성화 가능.

| # | 카테고리 | 정의 | 예시 | 승인 절차 |
|---|--------|----|----|--------|
| 6 | `WRITE_CODE` | `src/` / `tools/` / `scripts/` 등 코드 영역 작성. 영구 commit 동반 | Python module 작성, refactor, bug fix | 사용자 명시 결정 (PR review / 단축 합의) |
| 7 | `RUN_LOCAL_TOOLS` | 로컬 shell / git / docker / kubectl / 기타 CLI 실행 | `git commit`, `docker build`, `make`, `npm install` | 사용자 명시 결정 + Skill wrapper sandbox (G3 §3.3 runtime) |
| 8 | `NETWORK_ACCESS` | HTTP / WebSocket / SSH / 기타 outbound 통신 | API 호출, package install, git push | 사용자 명시 결정 + Egress redaction (G2 GP-2 답습) |
| 9 | `PROVIDER_SPECIFIC_OPTIMIZATION` | provider-specific 최적화 (provider_bindings §3.5 답습) | claude prompt cache, openai function calling | 사용자 명시 결정 + provider_bindings *optional optimization* 한정 강제 (§3.5 답습) |
| 10 | `SKILL_PROMOTION` | Skill `proposed` → `approved` / `approved` → `promoted` 상태 전이 trigger | promotion 결정, evidence collection trigger | 사용자 명시 결정 (G3 §2.2 #16 답습) — **자기 Skill promotion 은 T3 `SELF_PROMOTION` 으로 분류 (§3.7.3 답습)** |

**T2 강제 제한**:
- Hermes 가 본 5 카테고리 자동 호출 시도 = `event: t2_unauthorized_attempt` ledger entry + Skill 자동 비활성화 (G3 §2.2 #20 답습)
- 사용자 명시 승인 = 단축 합의 / Reviewer 승인 / 사용자 명시 결정 중 하나 — *Hermes 자기 승인 0건* (G3 §2.2 #16 답습)
- Skill `promotion_status: promoted` 미진입 상태 = T2 카테고리 사용 BLOCK

#### 3.7.3 T3 — 절대 금지 카테고리 (7 종)

> **모든 Skill 의 `forbidden_actions` 자동 포함 강제** (§3.2 #10 답습). 사용자 명시 override *불가* (T3 영역, ADR-011 §2.4). `allowed_actions` 에 T3 카테고리 진입 시 schema validation 즉시 BLOCK.

| # | 카테고리 | 정의 | 차단 사유 | schema-level 차단 |
|---|--------|----|--------|---------------|
| 11 | `SECRET_ACCESS` | API key / credential / private key / token 직접 접근 | 보안 헌법 (ADR-010 + ADR-011 §2.4) + R-1~R-7 redaction 정책 답습 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_secret_access_attempt` |
| 12 | `POLICY_CHANGE` | Constitution / ADR / SDD / Harness Gates 본문 변경 | 권위 위계 (ADR-011 §2.3) — Constitution > ADR > SDD > Harness Gates > Hermes > Workers | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_policy_change_attempt` |
| 13 | `ADR_CHANGE` (자동 수행) | `docs/decisions/ADR-*` 본문 *자동* 변경 (수동 사용자 명시 결정은 T2) | ADR Amendment 절차 강제 (ADR-008 부록 C §C.2 + ADR-011 §2.4 T3) — 풀 3+1 합의 + 외부 LLM 의견 의무 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_adr_change_attempt` |
| 14 | `SELF_PROMOTION` | 자기 Skill `proposed` → `approved` / `promoted` 자동 전이 | Hermes 가 자기 Skill 격상 시도 = G3 §2.2 #14 자기 격상 / G3 §4 합의 자기참조 차단 위반 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_self_promotion_attempt` (§3.8 답습) |
| 15 | `PROVIDER_LOCK_IN_ENFORCE` | provider_bindings `required: true` / `exclusive: true` / lock-in 강제 코드 작성 | Provider Liquidity (헌법 5조 관용) 위반 + 4-way Multi-layer Defense 회피 (GP-5 + G3 §6.4 + G4 §3.5 + GP-6) | `allowed_actions` 진입 시 즉시 BLOCK + provider_bindings §3.5 검증 BLOCK + `event: t3_provider_lockin_attempt` |
| 16 | `REDACTION_POLICY_RELAX` | R-4.1 Tier-1 42 catalog / baseline 5 redaction 정책 완화 / 우회 | ADR-011 §2.1 본질 (DB 평문 저장 차단 결과) + R-1~R-7 redaction 6단계 답습 | `allowed_actions` 진입 시 즉시 BLOCK + `event: t3_redaction_relax_attempt` |
| 17 | `CONSTITUTION_BYPASS` | Constitution 본문 우회 (memory / skill 로 정책 이전 시도) | G4 §5.2 #1 Memory 가 policy 대체 / §5.2 #2 Skill 이 ADR 우회 위반 + 권위 위계 (ADR-011 §2.3) 위반 | `allowed_actions` 진입 시 즉시 BLOCK + Memory/Skill boundary §5.2 검증 BLOCK + `event: t3_constitution_bypass_attempt` |

**T3 강제 메커니즘**:
- **schema-level**: `allowed_actions` validation 시 본 7 카테고리 진입 시 즉시 BLOCK (G4 §3.2 #9 + §3.7.3 답습)
- **runtime-level**: G3 §3.3 Skill wrapper + Memory write boundary + promotion hook (별도 합의 — Implementation/Runtime PASS 영역)
- **Evidence-level**: T3 attempt 모두 ledger entry append 의무 (`event: t3_*_attempt` + 사용자 명시 review)
- **자동 비활성화**: T3 attempt 검출 시 Skill `promotion_status: revoked` 자동 전이 (T3 자동 안전 동작 — ADR-011 §2.4 + §6.5 답습)

#### 3.7.4 본 §3.7 의 권위 한계

- 본 §3.7 = *schema-level enum 정의 + T 분류* 까지
- ❌ 실 schema validator runtime 구현 (Implementation/Runtime PASS 영역, 별도 합의)
- ❌ Skill wrapper runtime hook (G3 §3.3 영역, 별도 합의)
- ❌ Memory write boundary runtime hook (G4 §5.2 영역, 별도 합의)
- ❌ T3 attempt ledger entry 자동 작성 (runtime hook 영역)
- ❌ Skill `revoked` 자동 전이 runtime 강제 (runtime hook 영역)
- ❌ G3 §2.2 22 권한 분해 합의 (Group I 영역, 풀 3+1 + 외부 LLM 1+ 의무)
- ❌ ADR-014 발행 (Group H 영역, 풀 3+1 + 외부 LLM 1+ 의무)

### 3.8 Self-Permission Escalation 차단 + Revocation Chain (**Permission Granularity 세분화 — 2026-05-11**)

> **본 §3.8 은 Permission Granularity 세분화 작업 신설**. Skill 이 자기 `allowed_actions` 확장 시도 차단 + `promotion_status` 격상 시 권한 검증 + `rollback_triggers` ↔ permission revocation 연결. **§3.7 schema-level 차단 + G3 §3.3 runtime 차단 + 본 §3.8 자기 격상 차단 = 3-layer Permission Defense**.

#### 3.8.1 Self-Permission Escalation 차단 규칙

**원칙**: Skill 은 자기 `allowed_actions` / `forbidden_actions` / `provider_bindings` / `promotion_status` 를 *직접 수정* 또는 *간접 우회* 불가.

| 차단 메커니즘 | 정의 | 강제 layer |
|----------|----|--------|
| 자기 Skill 본문 수정 차단 | Skill A 가 Skill A 의 `skill.yaml` 본문 수정 시도 시 BLOCK | schema-level + runtime |
| 권한 확장 patch 차단 | Skill A 가 Skill A 의 `allowed_actions` 에 T2 / T3 카테고리 추가 시도 시 BLOCK | schema-level + ledger evidence |
| Forbidden override 차단 | Skill A 가 Skill A 의 `forbidden_actions` 에서 T3 카테고리 제거 시도 시 BLOCK + T3 영역 (ADR-011 §2.4) | schema-level + T3 절대 강제 |
| 자기 promotion 차단 | Skill A 가 자기 `promotion_status: proposed → approved / promoted` 자동 전이 시도 시 BLOCK | T3 `SELF_PROMOTION` 카테고리 (§3.7.3) |
| 간접 우회 차단 (Memory 통한 권한 누설) | Skill A 가 자기 권한 정보를 Memory 에 작성 후 Memory 를 통해 Skill B 의 권한 확장 시도 시 BLOCK | Memory/Skill boundary §5.2 #1 답습 |
| 간접 우회 차단 (Skill chain 통한 권한 확장) | Skill A (T1 한정) 가 Skill B (T2 권한 보유) 를 호출하여 효과적 T2 권한 획득 시도 시 BLOCK | Skill chain 검증 (별도 합의 — Implementation/Runtime PASS 영역) |

**검증 시점**:
- **Skill schema 등록 시점**: `allowed_actions` ⊆ T1+T2 / `forbidden_actions` ⊇ T3 7-category / `provider_bindings` §3.5 검증
- **`promotion_status` 전이 시점**: 이전 상태 권한 범위 ≤ 신규 상태 권한 범위 — *권한 축소만 자동 가능, 확장은 사용자 명시 승인*
- **Skill 실행 시점**: `last_verified_at` ≤ TTL + 권한 매칭 검증 (Implementation/Runtime PASS 영역)

**Self-Escalation 검출 시 처리**:
1. 즉시 BLOCK
2. `event: skill_self_escalation_attempt` ledger entry append (§4.2 답습) — `content.skill_id` / `content.attempted_category` / `content.from_state` / `content.to_state`
3. Skill `promotion_status: revoked` 자동 전이 (T3 자동 안전 동작)
4. 사용자 명시 review 의무 (G3 §3.1.6 + §3.3.6 답습)
5. 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
6. **Hermes 자기 검토 금지** — Self-escalation 검토 = 합의 자기참조 차단 영역 (G3 §4 답습) — 외부 Reviewer (사용자 / 외부 LLM) 의무

#### 3.8.2 Rollback Triggers ↔ Permission Revocation 연결

> **§3.2 #14 `rollback_triggers` ↔ §3.4.2 `revoked` 상태 전이 매트릭스 본문화** (Permission Granularity 세분화 — 2026-05-11). rollback_trigger 매치 시 Skill 의 *모든 권한* 자동 revoke + READ_ONLY 한정 (운영 차단).

**`rollback_triggers` enum 확장** (§3.2 #14 답습 + Permission Granularity 카테고리 신규):

| # | rollback_trigger | 정의 | 자동 revoke 권한 범위 | 후속 절차 |
|---|--------------|----|--------------|--------|
| 1 | `escalation_detected` | Skill 권한 escalation 시도 검출 (§3.8.1) | 모든 T1+T2 권한 자동 revoke → READ_ONLY only (§3.4.2 `revoked` 답습) | 사용자 명시 review + escalation 분석 |
| 2 | `evidence_missing` | `required_evidence` 의 하나라도 ledger entry 부재 / stale | 모든 T1+T2 권한 자동 revoke | 사용자 명시 review + Evidence 보완 |
| 3 | `t3_violation` | T3 카테고리 attempt 검출 (§3.7.3) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + ADR-011 §2.4 책임 분석 |
| 4 | `test_failure` | `required_tests` 의 하나라도 FAIL | 모든 T1+T2 권한 자동 revoke | 사용자 명시 review + 테스트 수정 |
| 5 | `secret_leak_detected` | Skill 본문 / Evidence ledger / Memory 에 R-4.1 Tier-1 42 catalog 검출 | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + R-7 SOP 답습 |
| 6 | `provider_lockin_detected` | `provider_bindings` §3.5 검증 위반 (required: true / exclusive: true / lock-in 코드) | 모든 T1+T2 권한 자동 revoke | 사용자 명시 review + Provider Liquidity 보호 분석 |
| 7 | `consensus_self_reference_detected` | Skill 본문에 Hermes 자기 합의 marker / 자기 reviewer 격상 marker 검출 (G3 §4 답습) | 모든 T1+T2 권한 자동 revoke | 사용자 명시 review + 합의 자기참조 분석 |
| 8 | `chain_violation_detected` | Evidence Ledger hash chain 위반 (§4.4.4 답습) | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + ADR-012 §2.7 답습 |
| 9 | `policy_drift_detected` | Memory 가 policy 대체 시도 (§5.2 #1) / Skill 이 ADR 우회 시도 (§5.2 #2) 검출 | 모든 T1+T2 권한 자동 revoke + Skill 완전 비활성화 | 사용자 명시 review + Memory/Skill boundary 분석 |

**Revocation Chain 자동 전이** (T3 자동 안전 동작 — ADR-011 §2.4):

```
[promoted] ──rollback_trigger 매치──→ [revoked]
   │                                       │
   │                                       │ 모든 T1+T2 권한 자동 revoke
   │                                       │ READ_ONLY only (운영 차단)
   │                                       ↓
   │                                  사용자 명시 review 의무
   │                                       │
   │                                       ├──→ [approved] (재활성화 — T2 사용자 명시 결정 + 재검증 §3.4.3)
   │                                       │
   │                                       └──→ [archived] (영구 폐기 — T2 사용자 명시 결정)
   │
   └──直 [archived] (사용자 명시 archive — revoke 없이 직접 폐기)
```

**자동 revoke 시점 ledger entry 의무**:

```jsonl
{"type":"skill","scope":"<scope>","id":"<skill_uuid>","schema_version":"0.1","ts":"<ts>","agent":"user|hermes","event":"skill_revoked","content":{"rollback_trigger":"<enum>","previous_state":"promoted","new_state":"revoked","revoked_permissions":["WRITE_CODE","RUN_LOCAL_TOOLS",...],"reason":"<detected violation>","evidence_refs":["<ledger entry id>",...]},...}
```

#### 3.8.3 본 §3.8 의 권위 한계

- 본 §3.8 = *schema-level 차단 규칙 + revocation chain 사양*까지
- ❌ 실 Skill wrapper runtime hook (G3 §3.3 영역, 별도 합의)
- ❌ 실 rollback_trigger 자동 검출 runtime (별도 합의 — Implementation/Runtime PASS 영역)
- ❌ 실 자동 revoke runtime (별도 합의)
- ❌ TTL / `last_verified_at` 자동 갱신 hook (별도 합의)
- ❌ Skill chain 검증 runtime (별도 합의)
- ❌ 외부 Reviewer (사용자 / 외부 LLM) 자동 호출 (T3 영역, ADR-011 §2.4)
- ❌ G3 §2.2 22 권한 분해 합의 (Group I 영역, 풀 3+1 + 외부 LLM 1+ 의무)

---

## 4. Provider-agnostic Export Format

### 4.1 JSONL 표준

본 §4 는 Memory + Skill 양쪽에 적용되는 *공통* JSONL export/import 형식.

```jsonl
{"type":"memory","scope":"global","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","event":"memory_write","content":{...},"evidence_refs":["docs/evidence/<task-id>.md"],"prev_hash":"<sha256>","hash":"<sha256>"}
{"type":"memory","scope":"project","id":"<uuid>",...}
{"type":"skill","scope":"project","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","event":"skill_promoted","content":{<skill.yaml as JSON>},"evidence_refs":[...],"prev_hash":"<sha256>","hash":"<sha256>"}
{"type":"meta","scope":"project","id":"<uuid>","schema_version":"0.1","ts":"2026-05-09T11:00:00Z","agent":"user","event":"external_llm_received","content":{"source_vendor":"gpt-5.x","verdict":"APPROVE_WITH_CONDITIONS"},"evidence_refs":["docs/external-review/<file>.md"],"prev_hash":"<sha256>","hash":"<sha256>"}
...
```

### 4.2 Schema (1 줄 = 1 entry, **11 필드 — ADR-012 §2.2 갱신**)

> **ADR-012 §2.2 갱신 (2026-05-09 PR-2 풀 3+1 합의)**: schema 10 필드 → **11 필드** (`event` 신규 추가). 본 §4.2 = ADR-012 §2.2 답습.

| 필드 | 타입 | 필수 | 검증 규칙 |
|------|-----|----|--------|
| `type` | enum | ✅ | `memory` / `skill` / **`meta`** (ADR-012 §2.2 — round-trip / migration / forgery / external_llm 영역) |
| `scope` | enum | ✅ | `global` / `project` / `session` / `team` |
| `id` | string | ✅ | UUID v4 또는 slug |
| `schema_version` | string | ✅ | semver (본 G4 schema 의 버전 — 현 `0.1` MVP, ADR-012 §3.2 진화 정책 답습) |
| `ts` | ISO 8601 | ✅ | entry 생성 timestamp + **monotonicity 의무** (본 entry `ts` ≥ `prev_hash` entry `ts`, ADR-012 §3.4) |
| `agent` | string | ✅ | provider-neutral identifier (`user` / `<worker_name>` / `hermes` 등). **External LLM response 적재 시 `agent="user"` 강제** (ADR-012 §2.1 원칙 7 + §2.12 #4) |
| **`event`** | **enum** | **✅ (ADR-012 §2.2 — 신규 11번째 필드)** | **17 enum 후보 (MVP 12 의무 + 5 후속 확장)** — `memory_write` / `skill_proposed` / `skill_approved` / `skill_promoted` / `skill_revoked` / `gate_pass` / `gate_fail` / `external_llm_received` / `evidence_forgery_detected` / `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` / `migration_failed` / `chain_violation_detected` / `hash_chain_broken` / `policy_change_attempted` / `canonical_json_fallback`. 자세한 분류 + T1/T2/T3 매핑 = ADR-012 §2.2 답습 |
| `content` | object | ✅ | (Memory) 자유 schema, (Skill) §3.1 17 필드 schema 그대로, (Meta) event-specific schema (ADR-012 §3.1 + §2.9 + §2.10 답습) |
| `evidence_refs` | array\<string\> | 권장 | Markdown evidence 파일 경로 |
| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` (§4.4) |
| `hash` | string (sha256) | ✅ | 본 entry 의 canonical JSON sha256 (변조 방지) — sha256 hardcode (schema_version 0.1), `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2) |

**합산 = 11 필드** (ADR-012 §2.2 답습). **모든 필드 provider-neutral 강제** (ADR-012 §2.1 원칙 6).

### 4.3 Hermes 의존 0 보장

**원칙**: Hermes 내부 DB / SDK / plugin 없이도 JSONL entry 를 *읽고 / 검증하고 / import* 할 수 있어야 한다.

| 검증 항목 | 메커니즘 | 권위 |
|---------|--------|-----|
| Hermes 의존 import 0건 | `scripts/hermes-migration/` 변환 스크립트가 `import hermes_agent` 등 의존 0건 | depcruise (G2 GP-5 답습) |
| 표준 도구로 검증 가능 | `jq` 로 parse + sha256 검증 + canonical JSON 검증 가능 (RFC 8785 reference output 동등성, §4.4.2 답습) | POSIX 표준 + RFC 8785 |
| schema_version 호환성 | 본 `0.1` 이외 버전은 **명시 declaration 후만 import 가능** (T2 사용자 승인 + §10.2 합의 절차 충족 + §4.5.3 import 검증 절차 통과 의무) | §4.5 + §10.2 + §4.6.5 답습 |
| 외부 오케스트레이터 import 가능 | claude / openai / gemini / local LLM 등 최소 2+ 로 재해석 가능 | §3.5 + GP-6 답습 |

**P-3 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-3 (자기 발견 잠재 위험 — "§4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재") 흡수 완료. **schema_version declaration 절차 = T2 사용자 명시 승인 + §10.2 합의 절차 + §4.5.3 정밀 import 검증 단계**. 본 절차 충족 *전* import = BLOCK (§4.6.5 #1~#3 답습).

### 4.4 Hash Chain 변조 방지 (**ADR-012 §2.3 + §2.5 + §2.6 + §2.7 + §2.8 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강 + 2026-05-11 P-1 흡수 완료**)

> **ADR-012 §2.3~§2.8 갱신**: 본 §4.4 = ADR-012 §2.3 (Append-only + Hash Chain 다층 강제) + §2.5 (RFC 8785 JCS) + §2.6 (Genesis Hash) + §2.7 (prev_hash 검증 실패 처리) + §2.8 (Full Rewrite 방어) 답습. 이전 (보강 전) "둘 중 하나 의무" 약 사양 → 다층 강제 사양 + canonical JSON 표준 인용 + 실패 처리 + full rewrite 방어 명시.
>
> **P-1 흡수 완료** (2026-05-11): G4 DRAFT 검토 §3.1 P-1 (자기 발견 잠재 위험 — "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함") 흡수 완료. **canonical JSON 표준 = RFC 8785 (JCS) IETF informational track 명시 인용** — §4.4.2 Primary 정의 + ADR-012 §2.5 권위. 본 §4.4 의 모든 hash 계산은 RFC 8785 (https://www.rfc-editor.org/rfc/rfc8785) 기준 canonical 형식에 SHA-256 적용. fallback (RFC 8259 escape + lex sort + `jq -S -c` 등) 은 RFC 8785 reference output 동등성 의무 (§4.4.2 답습).

#### 4.4.1 다층 강제 (Layer 1 ~ Layer 5)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§4.4.3)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (ADR-012 §3.2 답습)
- JSONL append-only — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4)

**Layer 2 — Git Append-only Branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — ADR-012 §2.8 답습)
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (G3 §5.5 SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — CI 회귀 검증 (MANDATORY)**:
- Layer 1 (hash chain) + Layer 2 (history) 자동 회귀 검증
- canonical JSON 위반 검출
- timestamp monotonicity 검증 (ADR-012 §3.4)
- R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장 (별도 PR — Implementation 영역)

**Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (ADR-012 §2.8 답습)
- 1인 SPOF 완화 + 침해 후 발견 가능

**사용자 명시 옵션 답습 (D-1, ADR-012 §2.4)**: "signed commit OR git append commit (둘 중 하나) 의무" — 사용자 결정 영역. 5/5 입력 권고는 *다층 동시 의무* (Layer 1 + 2 MANDATORY, Layer 3 RECOMMENDED). **본 §4.4 = Layer 1 + Layer 2 MANDATORY 답습** (D-1A / D-1B / D-1C 모두 호환).

#### 4.4.2 Canonical JSON — RFC 8785 JCS Primary + Fallback

**Primary**: **RFC 8785 JCS** (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증 (ADR-012 §2.5 답습).

**구현 라이브러리 후보**:
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무**:
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시**:
- `event: canonical_json_fallback` ledger entry 작성 의무 (§4.2 + ADR-012 §2.5 답습)
- Reviewer 알림 + 사용자 review 권장

**참고 (이전 정의 — 보강 전)**: lex sort + RFC 8259 escape + IEEE 754 numeric — 본 정의는 fallback 동등 보장의 *최소 기준*. 본 §4.4.2 갱신으로 RFC 8785 JCS 우선 채택.

#### 4.4.3 Genesis Hash

**MVP (schema_version 0.1) — 현 정의 유지** (ADR-012 §2.6):

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

**0.2 진입 또는 multi-chain 도입 시 (ADR-012 §2.6 + 외부 LLM 2 C-7 답습)**:

```python
genesis_hash = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

**전이 절차**: 0.1 chain 의 첫 entry 는 MVP 정의로 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 `schema_version`) 생성, 기존 0.1 chain 은 read-only (ADR-012 §3.2 답습).

#### 4.4.4 prev_hash 검증 실패 처리 (BLOCK + Manual Review)

**처리 절차** (ADR-012 §2.7 답습):

1. **즉시 BLOCK** — import / export / migration 중단
2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
3. **새 violation entry append** — `event: chain_violation_detected` ledger entry 작성:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"chain_violation_detected","content":{"violation_type":"prev_hash_mismatch|hash_recalculation|history_rewrite","detected_at":"<ts>","affected_entry":"<id>","prev_hash_expected":"<sha256>","prev_hash_actual":"<sha256>"},...}
   ```
4. **사용자 명시 review 의무** — 자동 PASS 금지
5. **자동 revert 금지** (T3 위반)
6. **Dual write 금지** (silent failure 위험)

**검출 layer**:
- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
- Layer 2: pre-push hook (chain 전체 재검증)
- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)

#### 4.4.5 Full Rewrite 방어 (5 Layer)

**Layer 1**: Hash chain (middle entry tampering 차단)
**Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
**Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
**Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
**Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag 또는 월 1회 external snapshot

**1인 동일 호스트 SPOF 한계 명시** (ADR-012 §2.8 + 외부 LLM 1 권고 5):

> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR / 본 §4.4 는 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.

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
- 라운드트립 검증: `export → 변환 → import → re-export → 원본 hash 일치` (또는 의미 보존 검증, §4.6.2 Tier-based 답습)
- **schema_version 명시 의무** — 변환 input / output 양쪽 모두 `schema_version` 필드 존재 확인 (§4.5.3 답습)
- `--dry-run` flag 지원 (검증 only — 실 import / write 0건)
- **`--declare-schema-version <version>` flag 지원** — 비표준 `schema_version` import 시 사용자 명시 declaration 통로 (§4.5.3 답습)
- canonical JSON RFC 8785 (JCS) 기준 (§4.4.2 답습)

#### 4.5.3 Import 시 schema_version 검증 절차 (**P-3 흡수 — 2026-05-11**)

> **본 §4.5.3 는 G4 DRAFT 검토 §3.1 P-3 흡수** (출처: `3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` §3.1 P-3 — "§4.5 외부 형식 import 시 schema_version declaration 절차 약함"). §4.3 #3 + §4.6.5 와 결합하여 *정밀 검증 절차* 본문화. **본 §4.5.3 = *절차 사양*까지 — 실 import 코드 구현 = Implementation/Runtime PASS 영역 별도 합의**.

외부 오케스트레이터 (claude / openai / gemini / local LLM) 또는 다른 `schema_version` JSONL 을 본 G4 형식으로 import 시 다음 단계를 통과 의무:

**Step 1 — `schema_version` 필드 존재 확인**:
- 필드 부재 = **즉시 BLOCK** (ADR-012 §2.10 답습)
- `event: import_block_missing_schema_version` ledger entry append 의무 (§4.2 답습)
- 사용자 명시 manual review 의무 (자동 default 부여 금지 — T3 위반)

**Step 2 — `schema_version` 호환성 매트릭스 조회**:
- 현 MVP `0.1` only. 본 매트릭스 = §10.2 답습.
- `schema_version` 일치 (`0.1` == `0.1`) → Step 3 진입
- `schema_version` 호환 (예: MVP `0.1` ⊂ `0.2` MINOR 호환 — backward compat 보장 시) → Step 3 진입 + `event: import_compat_minor` ledger entry
- `schema_version` 비호환 (MAJOR 차이 / 호환성 매트릭스 미등록) → **BLOCK** + Step 4 진입

**Step 3 — schema validation + canonical JSON 재해석**:
- §4.6.5 #4 + §4.4.2 답습
- canonical JSON RFC 8785 기준 재계산 + hash chain 검증 통과
- 검증 통과 → import 허용 + `event: import_pass` ledger entry
- 검증 실패 → BLOCK + `event: chain_violation_detected` ledger entry (§4.4.4 답습) + 사용자 명시 review

**Step 4 — 비호환 `schema_version` Declaration 절차** (T2 사용자 승인):
1. **사용자 명시 declaration 의무** — `--declare-schema-version <version>` flag (§4.5.2 답습) 또는 별도 합의 보고서 작성
2. **합의 절차** — declaration 형태 분기:
   - MINOR 호환 (backward compat 가능) → **단축 합의 (Reviewer-only)** + §10.2 답습
   - MAJOR 비호환 → **풀 3+1 합의 + ADR Amendment 절차** + §10.2 답습
3. **호환성 매트릭스 갱신** — declaration 결과 매트릭스 등록 (Implementation/Runtime PASS 영역 별도 합의)
4. **`event: schema_version_declared` ledger entry append** — declaration 의 evidence trail 형성 (§4.2 답습)
5. **`event: import_pass_after_declaration` 또는 `event: import_block_after_declaration`** — Step 3 재검증 결과 ledger entry

**금지 사항** (T3 영역 — ADR-011 §2.4 + ADR-012 §3.2 답습):
- ❌ schema_version 자동 default 부여 (필드 부재 시)
- ❌ schema_version silent drift (Hermes-originated 변경 — G3 §6.4 답습)
- ❌ 비호환 `schema_version` 자동 import (사용자 명시 declaration 없이)
- ❌ Step 1~3 통과 ledger entry 부재 상태에서 PASS 선언 (G3 §1.3 + §5.3 답습)

**본 §4.5.3 가 *하지 않는* 것**:
- ❌ 호환성 매트릭스 *내용* 자동 생성 (현 MVP `0.1` only 명시, 외부 형식 매핑은 별도 합의)
- ❌ 실 import 코드 구현 (Implementation/Runtime PASS 영역, §4.6.7 답습)
- ❌ 자동 declaration 발급 (T3 위반 — 모든 declaration = 사용자 명시 T2)
- ❌ Hermes 자기 declaration 발급 (G3 §6.4 + §2.2 #18 답습)

### 4.6 라운드트립 검증 절차 (**ADR-012 §2.9 + §2.10 답습 — 2026-05-09 PR-2 풀 3+1 합의 보강**)

> **ADR-012 §2.9~§2.10 갱신**: 본 §4.6 = ADR-012 §2.9 (Round-trip Lossy 검출 — Tier-based) + §2.10 (JSONL Export/Import 무결성) 답습. 이전 (보강 전) "hash 일치 OR 의미 보존" 단순 OR 약 사양 → tier-based + 3 ledger entry 형식 + migration 검증 실패 시 rollback 조건 명시.

#### 4.6.1 라운드트립 검증 흐름

```
[원본 Hermes JSONL]
       │
       │ ① hermes_to_<provider>.py 변환
       ↓
[<provider> 형식]
       │
       │ ② <provider> → 다시 본 G4 JSONL 형식으로 변환
       ↓
[재변환 JSONL]
       │
       │ ③ canonical JSON sha256 비교 (RFC 8785 JCS — §4.4.2 답습)
       ↓
[검증 — Tier-based]   ← Provider-agnostic 보장
```

#### 4.6.2 검증 PASS 조건 (Tier-based — ADR-012 §2.9 답습)

| Tier | 정체성 | PASS 조건 |
|-----|------|------|
| **Genesis (신규 chain)** | 첫 entry 작성 | (round-trip 무관) |
| **T2 (Skill / Memory promoted, 로컬)** | 로컬 promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) **정책 / 권한 / 증거 손실 BLOCK** |

#### 4.6.3 Ledger Entry 3 형식 (ADR-012 §2.9 답습)

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"<id>","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"<id>","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review-summary>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"<id>","target_provider":"openai","failure_reason":"chain_violation_detected|policy_loss|permission_loss|evidence_loss"},...}
```

#### 4.6.4 자동화 vs 사용자 Review 분리 (ADR-012 §2.9 답습)

- `lost_fields` enumeration = **자동** (canonical JSON diff)
- `semantic_diff` 판단 = **사용자 명시 review** (ADR-011 §2.4 T2/T3 사용자 승인)
- **의미 보존 review 자동화 절대 금지** (Agent A R-4 답습)

#### 4.6.5 JSONL Export / Import 무결성 (ADR-012 §2.10 답습)

**Export** (Hermes 의존 0 — ADR-008 차단조건 #2 답습):
- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증, G2 GP-5 답습)
- 표준 도구 (`jq` + `sha256sum`) 만으로 검증 가능
- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능

**Import 의무 검증** (**§4.5.3 정밀 절차 답습 — 2026-05-11 P-3 흡수**):
1. `schema_version` 필드 존재 확인 (없으면 BLOCK — ADR-012 §2.10 + §4.5.3 Step 1)
2. 호환성 매트릭스 조회 — 현 MVP 0.1 only, 외부 형식 매핑은 별도 (Implementation 영역, §4.5.3 Step 2)
3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구 (§4.5.3 Step 4 declaration 절차 — T2 사용자 승인 + §10.2 합의 절차)
4. Hash chain 검증 (§4.4.4 답습, §4.5.3 Step 3)
5. **Step 1~4 결과 ledger entry 의무** — `event: import_pass` / `import_block_*` / `schema_version_declared` (§4.5.3 답습)

#### 4.6.6 Migration 검증 실패 시 Rollback 조건 (ADR-012 §2.10 답습)

**처리 절차**:

1. **BLOCK**
2. **원본 보존** — 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
3. **새 `event: migration_failed` entry append**:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"migration_failed","content":{"source_provider":"hermes","target_provider":"openai","failure_step":"export|conversion|import|reverify","error_summary":"..."},...}
   ```
4. **사용자 명시 manual review 의무**
5. **자동 revert 금지** (T3 위반)
6. **Dual write 금지** (silent failure 위험 — schema_version drift)

**4 후보 처리 비교** (ADR-012 §2.10 + 합의 §4.3 답습):

| 후보 | 평가 | 채택 |
|----|----|----|
| (a) BLOCK + manual review | 안전, 운영 부담 ↑ | ✅ 채택 |
| (b) 자동 revert | T3 위반 위험 (ADR-011 §2.4) | ❌ 비채택 |
| (c) 원본 보존 + 새 violation entry | (a) 와 결합 — 본 §4.6.6 답습 | ✅ (a) 와 결합 채택 |
| (d) Dual write | silent failure 위험 + schema_version drift | ❌ 비채택 |

#### 4.6.7 본 §4.6 의 권한 한계

본 §4.6 = Round-trip 검증 *절차 사양* 까지. 실 migration script 구현 (`scripts/hermes-migration/*.py`) + R-6 workflow ledger 검증 step 추가 = **Implementation/Runtime PASS 영역** (별도 합의, 본 §4.6 범위 외 — ADR-012 §10.2 답습).

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

### 6.1 Skill Escalation 방지 (**Permission Granularity 세분화 답습 — 2026-05-11**)

**G3 §3.3 답습**: Skill 이 정의된 권한 등급 (`allowed_actions`) 을 *넘어* 작동 시 차단. **2026-05-11 Permission Granularity 세분화 후 = 3-layer Permission Defense** (schema-level §3.7 + self-escalation §3.8 + runtime G3 §3.3).

| 메커니즘 | G4 책임 (형식) | G3 책임 (권한) |
|--------|------------|--------------|
| Skill schema `allowed_actions` 필드 | ✅ §3.1 #9 + §3.2 #9 + **§3.7 12 카테고리 semantic enum** | (위임) |
| Skill schema `forbidden_actions` 필드 | ✅ §3.1 #10 + §3.2 #10 + **§3.7.3 T3 7-category 자동 포함 강제** | (위임) |
| 권한 등급 enum 정의 | ✅ **§3.7 12 카테고리 — T1 5 (자동) / T2 5 (사용자 승인) / T3 7 (절대 금지)** (이전 coarse 7 종 → 세분화) | (위임) |
| T3 카테고리 schema-level 즉시 BLOCK | ✅ **§3.7.3 + §3.2 #9 — `allowed_actions` 진입 시 schema validation BLOCK** | (위임) |
| `promotion_status` × 권한 범위 매트릭스 | ✅ **§3.4.2 — proposed (T1 only) / approved (T1+T2 일부) / promoted (T1+T2 전체) / revoked·archived (READ_ONLY only)** | (위임) |
| Self-Permission Escalation 차단 | ✅ **§3.8.1 6 차단 메커니즘 (자기 본문 수정 / 권한 확장 patch / Forbidden override / 자기 promotion / Memory 우회 / Skill chain 우회)** | (위임 — runtime hook G3 §3.3) |
| Rollback Triggers ↔ Permission Revocation 연결 | ✅ **§3.8.2 9 rollback_trigger × 자동 revoke 매트릭스 + revocation chain 자동 전이** | (위임 — runtime trigger G3 §3.1.5 / §3.3.5) |
| Wrapper 권한 검증 (실 runtime) | (위임) | ✅ G3 §3.3.3 |
| Sandbox cap_drop / read_only / tmpfs noexec | (위임) | ✅ G3 §3.3.3 |
| Audit log on escalation 시도 | ✅ **§3.7.3 + §3.8.1 — `event: t3_*_attempt` / `event: skill_self_escalation_attempt` ledger entry 형식** | ✅ G3 §3.3.4 (실 audit log 작성) |
| 자동 비활성화 + 사용자 alert | ✅ **§3.4.2 + §3.8.2 — `promotion_status: revoked` 자동 전이 형식** | ✅ G3 §3.3.5 (실 revoke runtime + alert) |

**인터페이스 (3-layer Permission Defense)**:
- **Layer 1 (schema-level)** — G4 §3.7 12-category enum + §3.2 #9/#10 schema validation 필드 *정의* + T3 7-category 자동 차단 *형식*
- **Layer 2 (self-escalation)** — G4 §3.8.1 6 차단 메커니즘 *규칙* + §3.8.2 9 rollback_trigger × revoke 매트릭스 *연결*
- **Layer 3 (runtime)** — G3 §3.3 wrapper + sandbox + audit log + 자동 revoke *runtime 강제*

3 layer 모두 결합 시 escalation 차단의 *완결성*. 1 layer 만 깨져도 escalation 위험 잔존 (예: schema OK + self-escalation OK 이지만 runtime wrapper 부재 시 격리 실패).

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

### 10.1 일반 변경 절차

| 변경 유형 | 절차 |
|---------|------|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| §2 ~ §4 본문 갱신 (Memory scope / Skill schema / JSONL 형식) | 단축 합의 (Reviewer-only) |
| §3.1 17 필드 schema 본문 갱신 | 단축 합의 — 단, 필드 *추가* 는 schema_version 증가 (semver MINOR, §10.2 답습) |
| §3.5 `provider_bindings` 검증 규칙 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — Provider Liquidity 핵심) |
| §4.4 hash chain 변조 방지 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — Evidence 무결성 핵심) |
| §5.2 4 금지 사항 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경) |
| §6 G3 인터페이스 5 항목 갱신 | 단축 합의 — G3 본문 변경 시 동시 갱신 |
| §7 G2 GP-6 인터페이스 갱신 | 단축 합의 — GP-6 본문 변경 시 동시 갱신 |
| **DRAFT 상태 해제 → 정식 채택** | **단축 합의 또는 풀 3+1 합의 APPROVE** + 각 § (a)~(e) 충족 검증 + 외부 LLM 의견 권장 (G3 §4.4.2 답습) |
| §9 영구 핵심 제약 변경 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 매우 신중) |

### 10.2 Schema 진화 정책 (**P-2 흡수 — 2026-05-11**)

> **본 §10.2 는 G4 DRAFT 검토 §3.1 P-2 흡수** (출처: `3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` §3.1 P-2 — "§10 schema 진화 정책 — 필드 *제거* / *변경* 정책 미명시"). §11.4.1 권고 사양을 §10 본문으로 정식 흡수. **schema_version pin** (§4.2 답습) 이 변경 시점에 증가. import 시 `schema_version` 호환성 검증 의무 (§4.5 + §4.6.5 답습).

본 §10.2 는 §3.1 17 필드 Skill schema + §4.2 JSONL entry 11 필드 schema 의 진화 (필드 추가 / 제거 / 이름 변경 / 타입 변경) 에 공통 적용된다. **semver 정책 = `MAJOR.MINOR.PATCH`** (MVP 시작점 `schema_version = 0.1`, ADR-012 §3.2 답습).

| 변경 유형 | semver 증가 | 합의 절차 | 추가 의무 |
|---------|-----------|---------|---------|
| **필드 *추가*** (선택 필드, 기존 entry 호환) | MINOR (예: `0.1` → `0.2`) | 단축 합의 (Reviewer-only) | import 시 backward compatibility 보장 (구 schema_version entry 도 import 가능 — 추가 필드는 `null` / 기본값) |
| **필드 *추가*** (필수 필드, 기존 entry 비호환) | MAJOR (예: `0.1` → `1.0`) | **풀 3+1 합의 + ADR Amendment 절차** | migration script 의무 (§4.5 답습) + 구 schema_version entry 는 read-only |
| **필드 *제거*** | MAJOR (예: `0.1` → `1.0`) | **풀 3+1 합의 + ADR Amendment 절차** | migration script 의무 (§4.5 답습) + 제거 필드 보존 ledger entry append (`event: schema_field_removed`) + 사용자 명시 review |
| **필드 *이름 변경*** | MAJOR (예: `0.1` → `1.0`) | **풀 3+1 합의 + ADR Amendment 절차** | alias 호환성 *최소 1 release* 유지 (구 이름 alias → 신 이름) + `event: schema_field_renamed` ledger entry + 사용자 명시 review |
| **필드 *타입 변경*** | MAJOR (예: `0.1` → `1.0`) | **풀 3+1 합의 + ADR Amendment 절차** | migration script 의무 (§4.5 답습) + 타입 변환 손실 enumeration + `event: schema_field_type_changed` ledger entry + 사용자 명시 review |
| **필드 *검증 규칙 강화*** (예: `provider_bindings` exclusive 금지 강화) | MINOR (예: `0.1` → `0.2`) — 단, 기존 entry 검증 통과 가능 시 / MAJOR — 기존 entry 비호환 시 | 단축 합의 (MINOR) / **풀 3+1 합의** (MAJOR) | 비호환 entry import 시 BLOCK + 사용자 명시 review |
| **`hash_algo` 변경** (예: SHA-256 → SHA-3) | MAJOR (전 chain 영향) | **풀 3+1 합의 + ADR Amendment 절차** | 새 chain 생성 (§4.4.3 Genesis 답습) + 구 chain read-only + 외부 LLM 의견 의무 |

**schema_version 발급 권한** (ADR-011 §2.4 T1/T2/T3 답습):
- **T1 (자동)**: 본 §10.2 *적용 자체* 는 본 G4 PASS / 본 G4 정식 채택 후 가능 (DRAFT 상태에서는 사양 명시 한정)
- **T2 (사용자 승인)**: `schema_version` MINOR / MAJOR 증가 발생 시 사용자 명시 결정 의무
- **T3 (금지)**: schema_version 자동 증가 / Hermes-originated schema_version 증가 / silent drift 모두 금지 (ADR-012 §3.2 + G3 §6.4 답습)

**import 호환성 매트릭스** (§4.5 + §4.6.5 답습):
- 현 MVP `0.1` only. 외부 형식 (claude / openai / gemini / local LLM) 매핑 + 다른 `schema_version` 호환성 매트릭스 = Implementation/Runtime PASS 영역 별도 합의.
- import 시 `schema_version` 미일치 = BLOCK + 사용자 명시 manual approval 의무 (§4.6.5 #3 답습).

**본 §10.2 가 *하지 않는* 것**:
- ❌ schema_version 자동 증가 (T3 금지)
- ❌ Implementation/Runtime 호환성 매트릭스 자동 생성 (별도 합의)
- ❌ migration script 자동 실행 (T3 금지)
- ❌ DRAFT 상태에서 본 §10.2 강제 적용 (DRAFT 상태 = 사양 명시 한정, G4 PASS 후 강제)

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
- ~~§4.4 canonical JSON 정의 — JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고.~~ **✅ 흡수 완료** (2026-05-11 P-1, §4.4 헤더 + §4.4.2 본문 RFC 8785 IETF 직접 인용 — `https://www.rfc-editor.org/rfc/rfc8785` + ADR-012 §2.5 권위. fallback 동등성 의무 + test corpus 의무 + canonical_json_fallback ledger entry 의무).
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

### 11.4 G4 후속 권고 P-1 ~ P-5 흡수 진행 상태 (C-L 흡수 — 2026-05-09 후속 2, **P-1/P-2/P-3 RESOLVED — 2026-05-11**)

> **본 §11.4 는 합의 보고서 §11.2 P1 조건 C-L 흡수** (출처: `3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md` §3.1 자기 발견 잠재 위험 5건). G4 DRAFT 검토 시점 (2026-05-09 첫 검토) 자기 발견 5 후속 권고 P-1 ~ P-5 의 *처리 시점·방법* 을 명시 기록.
>
> **2026-05-11 갱신**: P-1 / P-2 / P-3 **본문 흡수 완료 (RESOLVED)** — 사용자 명시 범위 한정 (RFC 8785 JCS 인용 + schema 진화 정책 + import schema_version 절차 보강). Hermes PMO 격상 / Operational Readiness PASS / runtime 구현 = **본 흡수 작업 범위 외** (사용자 명시 답습).

| # | 위험 (G4 검토 §3.1) | 처리 시점 | 처리 방법 | 상태 |
|---|------------|--------|--------|----|
| **P-1** | §11.1 자기 명시 한계 — RFC 8785 JCS 미인용 (self-disclosed) | PR-2 풀 3+1 (§4.4.2 본문) + **2026-05-11 §4.4 헤더 / §11.1 갱신** | §4.4 헤더 P-1 흡수 완료 명시 + §4.4.2 본문 RFC 8785 IETF 직접 인용 (`https://www.rfc-editor.org/rfc/rfc8785`) + ADR-012 §2.5 권위 + fallback 동등성 의무 + canonical_json_fallback ledger entry 의무 + §11.1 자기 명시 한계 strikethrough + 흡수 완료 표기 | ✅ **RESOLVED** (2026-05-11) |
| **P-2** | §10 schema 진화 정책 — 필드 *제거* / *변경* 정책 미명시 | §11.4.1 권고 사양 → **2026-05-11 §10.2 본문 흡수** | §10 → §10.1 (일반 변경 절차) + §10.2 신설 (schema 진화 정책 — 7 행 매트릭스 + T1/T2/T3 발급 권한 + import 호환성 매트릭스 + 본 §10.2 가 *하지 않는* 것 4건) | ✅ **RESOLVED** (2026-05-11) |
| **P-3** | §4.5 외부 형식 import 시 schema_version declaration 절차 약함 | §4.3 #3 단순 명시 → **2026-05-11 §4.3 #3 보강 + §4.5.2 보강 + §4.5.3 신설 + §4.6.5 cross-reference 보강** | §4.3 #3 schema_version 호환성 행 T2 + §10.2 + §4.5.3 cross-reference 명시 + §4.5.2 `--declare-schema-version` flag + canonical JSON RFC 8785 의무 + §4.5.3 신설 (Step 1~4 정밀 절차 + 5 ledger entry 형식 + 4 금지 사항 + 4 본 §4.5.3 가 *하지 않는* 것) + §4.6.5 Step 1~5 답습 cross-reference 보강 | ✅ **RESOLVED** (2026-05-11) |
| **P-4** | §6.4 "3-way 인터페이스" 명명 정확성 — 실제 G4 두 § (§3.5 + §4.3) + GP-5 + G3 §6.4 = 4-way | **PR-1 본문 보강** (현 §11.4.2 흡수) | §6.4 명명 "3-way" → "4-way" 정정 또는 *별 명명* (예: "Provider Liquidity Multi-layer Defense") — 본 §11.4.2 답습 | ✅ RESOLVED (2026-05-09 PR-1, §11.4.2 답습) |
| **P-5** | §2.2.1 Global Memory `~/.claude/global/` Claude Code 표준 디렉토리 충돌 가능성 | **Implementation/Runtime PASS** 합의 (실 path 결정 시점) | 별도 합의 — Claude Code 표준 디렉토리 구조 점검 후 path 정정 또는 prefix 추가 | ⏳ **PENDING** (Implementation/Runtime PASS 영역, 본 2026-05-11 흡수 범위 외) |

**2026-05-11 P-1/P-2/P-3 흡수 범위 명시 한계** (사용자 명시 답습):
- ✅ 본 흡수 작업 = G4 설계 문서 본문 정합화 한정
- ❌ Hermes PMO 격상 = 본 흡수 범위 외 (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 인간 리뷰 + 사용자 명시 결정 후 별도)
- ❌ Operational Readiness PASS / Implementation/Runtime PASS = 본 흡수 범위 외 (별도 합의)
- ❌ runtime 구현 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 / migration script) = 본 흡수 범위 외
- ❌ ADR 본문 자동 갱신 = 본 흡수 범위 외
- ❌ P2 v3 / G2 / G3 / G4 PASS 자동 격상 = 본 흡수 범위 외
- ❌ P-5 (Global path) 자동 처리 = 본 흡수 범위 외 (Implementation/Runtime PASS 영역)

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

- ~~❌ §4.4 RFC 8785 JCS 본문 인용 (PR-2 풀 3+1 영역 — C-G 흡수와 *동시*)~~ **✅ 흡수 완료** (2026-05-09 PR-2 §4.4.2 + 2026-05-11 §4.4 헤더 / §11.1 보강)
- ~~❌ §10 본문 자동 갱신 (본 §11.4.1 은 *권고 사양* 명시까지, §10 본문 변경은 PR-2 또는 별도 합의)~~ **✅ 흡수 완료** (2026-05-11 §10.2 신설 — §11.4.1 권고 사양 본문화)
- ❌ §6.4 / §3.5 / §4.3 본문 *용어 자동 갱신* (본 §11.4.2 는 *명명 정정 명시 기록* 까지)
- ❌ P-5 (`~/.claude/global/` path 정정) 자동 처리 (Implementation/Runtime PASS 영역, 별도 합의)
- ~~❌ P-3 (§4.5 import schema_version 검증) 자동 구현 (PR-2 또는 별도 합의)~~ **✅ *사양*까지 흡수 완료** (2026-05-11 §4.5.3 신설 — 실 import 코드 구현은 여전히 Implementation/Runtime PASS 영역 별도 합의)
- ❌ Hermes PMO 격상 자동 (4 게이트 Implementation/Runtime PASS + 외부 LLM 2 + 인간 리뷰 + 사용자 명시 결정 후 별도)
- ❌ Operational Readiness PASS / Implementation/Runtime PASS 자동 (별도 합의)
- ❌ runtime 코드 자동 구현 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 / migration script — 모두 Implementation/Runtime PASS 영역)
- ❌ ADR 본문 자동 갱신 (별도 PR 묶음)
- ❌ P2 v3 / G2 / G3 / G4 PASS 자동 격상 (Design/Governance Gate PASS ↔ Implementation/Runtime PASS 분리 유지 — ADR-008 부록 C §C.5 답습)

### 11.5 Permission Granularity 세분화 작업 흡수 기록 (2026-05-11)

> **본 §11.5 는 Permission Granularity 세분화 작업** (사용자 명시 7 항목 답습 — `allowed_actions` 권한 category 분류 / `forbidden_actions` T3 명시 / `provider_bindings` lock-in 제한 / `promotion_status` 별 권한 범위 / self-escalation 차단 / `required_evidence`·`required_tests` 강화 / `rollback_triggers` ↔ permission revocation 연결) 의 *처리 위치·방법·상태* 본문화. **본 작업 = G4 Skill schema 의 permission granularity 보강 한정 — Hermes PMO 격상 / Operational Readiness PASS / Implementation/Runtime PASS / runtime 구현 / ADR 본문 갱신 모두 본 작업 범위 외** (사용자 명시 답습).

#### 11.5.1 7 항목 흡수 매트릭스

| # | 사용자 명시 항목 | 흡수 위치 | 흡수 방법 | 상태 |
|---|----------|--------|--------|----|
| 1 | `allowed_actions` 를 coarse-grained 문자열이 아니라 권한 category 로 분류 | §3.1 #9 + §3.2 #9 + **§3.7 신설** | 이전 coarse 7 종 (`read` / `write` / `shell` / `network` / `db` / `git` / `docker`) → **§3.7 12 카테고리 semantic enum** (T1 5 + T2 5 + T3 7 분류). §3.2 #9 schema validation BLOCK 규칙 명시 | ✅ **RESOLVED** (2026-05-11) |
| 2 | `forbidden_actions` 에 T3 절대 금지 권한 명시 | §3.2 #10 + §3.7.3 | §3.2 #10 — T3 7 카테고리 (`SECRET_ACCESS` / `POLICY_CHANGE` / `ADR_CHANGE` / `SELF_PROMOTION` / `PROVIDER_LOCK_IN_ENFORCE` / `REDACTION_POLICY_RELAX` / `CONSTITUTION_BYPASS`) 자동 포함 강제 + 사용자 명시 override 불가 (T3 영역) | ✅ **RESOLVED** (2026-05-11) |
| 3 | `provider_bindings` 가 provider lock-in 으로 변질되지 않도록 제한 | §3.5 (기존) + §3.7.3 #15 `PROVIDER_LOCK_IN_ENFORCE` T3 분류 추가 | §3.5 `required: true` / `exclusive: true` 표시 금지 (기존) + §3.7.3 T3 카테고리화 (`PROVIDER_LOCK_IN_ENFORCE` allowed_actions 진입 시 schema BLOCK) + Provider Liquidity 4-way Multi-layer Defense (§11.4.2 답습) 답습 | ✅ **RESOLVED** (2026-05-11) |
| 4 | `promotion_status` 별 허용 권한 범위 명시 | §3.4.2 신설 + §3.4.3 신설 | §3.4.2 — 5 promotion_status × 권한 범위 매트릭스 (proposed=T1 only / approved=T1+T2 일부 / promoted=T1+T2 전체 / revoked·archived=READ_ONLY only). §3.4.3 — `promoted` 진입 검증 5/5 조건 + 운영 중 검증 + Skill 실행 전 검증 | ✅ **RESOLVED** (2026-05-11) |
| 5 | Skill 이 자기 권한을 확장하지 못하도록 escalation 방지 규칙 추가 | §3.8.1 신설 | §3.8.1 — 6 차단 메커니즘 (자기 본문 수정 / 권한 확장 patch / Forbidden override / 자기 promotion / Memory 우회 / Skill chain 우회) + 검증 시점 3 (등록 / 전이 / 실행) + Self-Escalation 검출 시 처리 6 단계 (BLOCK / ledger entry / revoke / review / revert 금지 / 자기 검토 금지) | ✅ **RESOLVED** (2026-05-11) |
| 6 | Skill 실행 전 `required_evidence` / `required_tests` 확인 조건 강화 | §3.4.3 신설 + §3.4.2 매트릭스 추가 검증 의무 column | §3.4.3 — `promoted` 진입 5/5 조건 (required_evidence 전체 + required_tests 전체 + schema 통과 + §3.8 self-escalation 통과 + Evidence ledger entry append) + 운영 중 검증 + Skill 실행 전 검증 (TTL + last_verified_at + rollback_trigger 매치 시 자동 revoke) | ✅ **RESOLVED** (2026-05-11) |
| 7 | `rollback_triggers` 와 permission revocation 절차 연결 | §3.8.2 신설 | §3.8.2 — `rollback_triggers` enum 9 종 (escalation_detected / evidence_missing / t3_violation / test_failure / secret_leak_detected / provider_lockin_detected / consensus_self_reference_detected / chain_violation_detected / policy_drift_detected) × 자동 revoke 권한 범위 × 후속 절차 매트릭스 + Revocation Chain 자동 전이 (promoted → revoked / approved / archived) + ledger entry 형식 의무 | ✅ **RESOLVED** (2026-05-11) |

#### 11.5.2 권한 분류 채택 매트릭스 (사용자 권장 답습)

| Tier | 카테고리 (12 종 총) | §3.7 위치 | 채택 |
|------|---------------|--------|----|
| **T1 자동 가능** | READ_ONLY / SUGGEST_ONLY / WRITE_DRAFT / WRITE_DOCS (일부) / RUN_TESTS (일부) — 5 종 | §3.7.1 | ✅ 채택 |
| **T2 사용자 명시 승인** | WRITE_CODE / RUN_LOCAL_TOOLS / NETWORK_ACCESS / PROVIDER_SPECIFIC_OPTIMIZATION / SKILL_PROMOTION — 5 종 | §3.7.2 | ✅ 채택 |
| **T3 절대 금지** | SECRET_ACCESS / POLICY_CHANGE / ADR_CHANGE (자동 수행) / SELF_PROMOTION / PROVIDER_LOCK_IN_ENFORCE / REDACTION_POLICY_RELAX / CONSTITUTION_BYPASS — 7 종 | §3.7.3 | ✅ 채택 |

**합산 = 17 카테고리** — 단, T1 의 `WRITE_DOCS` 와 `RUN_TESTS` 는 *일부* 표시 (각각 일부 영역에서만 T1, 다른 일부는 T2/T3 자동 분류). 따라서 **고유 카테고리 = 12 종** (사용자 권장 답습).

#### 11.5.3 본 §11.5 가 *하지 않는* 것 (사용자 명시 답습 7 영역)

- ❌ **runtime code 구현** — Skill wrapper / sandbox / cap_drop / audit log 자동 작성 / rollback_trigger 자동 검출 등 (Implementation/Runtime PASS 영역, 별도 합의)
- ❌ **migration script 구현** — 기존 Skill schema 의 coarse enum → 12 카테고리 자동 변환 script (별도 합의)
- ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 인간 리뷰 + 사용자 명시 결정 후 별도
- ❌ **Operational Readiness PASS 선언** — 별도 합의
- ❌ **Implementation/Runtime PASS 선언** — 별도 합의
- ❌ **G4 전체 PASS 재선언** — 본 작업 = Permission Granularity 세분화 한정, G4 Design/Governance Gate PASS 권위 변경 0건
- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신** — Permission Granularity 와 ADR 본문 cross-reference 가 깨지지 않음 (본 작업 = G4 본문 보강 한정)

#### 11.5.4 본 §11.5 의 권위 한계

- 본 §11.5 = *설계 문서 수준 permission granularity 보강* 까지
- ❌ Schema validator runtime 구현 (Implementation/Runtime PASS 영역, 별도 합의)
- ❌ Skill wrapper runtime hook (G3 §3.3 영역, 별도 합의)
- ❌ Memory write boundary runtime hook (G4 §5.2 영역, 별도 합의)
- ❌ 자동 rollback_trigger 검출 + 자동 revoke runtime (별도 합의)
- ❌ G3 §2.2 22 권한 분해 합의 (Group I 영역, 풀 3+1 + 외부 LLM 1+ 의무) — 본 §11.5 12 카테고리 ↔ G3 22 권한 매핑은 Group I 합의 영역
- ❌ ADR-014 발행 (Group H 영역, 풀 3+1 + 외부 LLM 1+ 의무)
- 본 §11.5 변경 (T1/T2/T3 카테고리 추가/제거/이동) 자체는 풀 3+1 합의 + ADR Amendment 절차 (T3 변경 — 권한 위계 핵심)

#### 11.5.5 본 §11.5 의 합의 형태 (사용자 명시 결정 대기)

- 본 §11.5 = §10.1 *§2~§4 본문 갱신* 영역 (Skill schema §3 + G3 인터페이스 §6.1 본문 보강) — **단축 합의 (Reviewer-only) 적격 영역**
- T3 카테고리 신설 (§3.7.3) 은 §10.1 *§5.2 4 금지 사항 본문 갱신* 영역과 유사한 무게 — 단, 본 §3.7.3 은 *4 금지 사항 본문 변경 0건* + Skill schema enum 형식 확장 한정 → 단축 합의 영역 유지
- 별도 합의 보고서 작성 = 후속 사용자 명시 결정 영역 (본 §11.5 본문 흡수 자체는 §11.4.1 권고 사양 → §10.2 본문화 답습 패턴)

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
