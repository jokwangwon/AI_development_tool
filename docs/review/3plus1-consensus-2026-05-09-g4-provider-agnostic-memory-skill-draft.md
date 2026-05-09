# 단축 검토 보고서 (Reviewer-only): G4 Provider-agnostic Memory / Skill Design DRAFT 채택 적격성

**날짜**: 2026-05-09
**검증 대상**: `docs/architecture/provider-agnostic-memory-skill-design.md` (DRAFT, commit `079bc6c`)
**합의 형태**: 단축 검토 (Reviewer-only) — DRAFT 적격성 한정
**상위 권위**: 헌법 5조 (관용 — Provider Liquidity), ADR-008 차단조건 #2 (JSONL export 표준), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 자동 정책 변경 분리) + 본 세션 사용자 명시 결정 (G4 정식 채택 합의 진입 전 G4 DRAFT 적격 검토)
**관련 evidence**:
- G4 초안 (commit `079bc6c`) — 11 섹션 + 부록, 754 insertions
- P2 v3 DRAFT 단축 검토 결과 (commit `12d7609`, APPROVE AS DRAFT)
- G2 DRAFT 단축 검토 결과 (commit `957cddc`, APPROVE AS DRAFT)
- G3 DRAFT 단축 검토 결과 (commit `d42886b`, APPROVE AS DRAFT)
- G3 §6.5 / §7 (GP-6 ↔ G3 ↔ G4 3-way 인터페이스 — 본 G4 §6 / §7 흡수 대상)
- 합의 §103 (Memory 2단계 + Skill 자동 추출 T1 한정 + GPT 4단계 미채택 사유)
- system-identity-prequel §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary)
- G1b PASS evidence (R-7 SOP §7.3 단축 합의, 2026-05-07)
**사용자 명시 결정**:
- G4 DRAFT 적격 검토 → APPROVE 시 별도 commit → G2/G3/G4 정식 채택 합의 준비
- G4 PASS / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 runtime 코드 / 실 migration script 모두 자동 트리거 금지

---

## 1. 사전 점검 — 검토 가동 정당성

### 1.1 가동 사유

본 G4 초안은 다음 입력을 흡수한 신규 산출 (commit `079bc6c`):
- 헌법 5조 (관용 — Provider Liquidity 비협상 제약) + ADR-008 차단조건 #2 (JSONL export 표준)
- ADR-011 §2.3 (권위 위계 영구 권위) + §2.4 (T1/T2/T3 분류)
- system-identity-prequel §6.3 (Evidence Ledger schema 후보) + §8.4 (Memory 2단계 boundary)
- 합의 §103 (Memory 2단계 + Skill 자동 추출 T1 한정 + GPT 4단계 미채택 사유)
- P2 v3 DRAFT §6 (G4 정의)
- G2 DRAFT §8 (GP-6 Memory/Skill Migration)
- G3 DRAFT §6.5 / §7 (GP-6 ↔ G3 ↔ G4 3-way 인터페이스 — G4 = *형식*, G3 = *권한*)

본 초안은 **옵션 B (Memory + Skill 통합 단일 문서)** 채택 — 사용자 명시 결정 답습. 사유: G4 핵심 = *공통 schema 보장* (Memory + Skill 양쪽에 적용되는 provider-agnostic 보장).

본 초안은 *DRAFT 상태로 commit 완료* (`079bc6c`) 상태이며, 본 검토는 *DRAFT 적격성*을 확인하여 G2/G3/G4 정식 채택 합의 준비 진입 가능 여부를 판정. 검토 범위 한정:
- 사용자 명시 10 기준 충족 여부 (G3 답습 + G4 §0.1 7 작업 항목 + §8.1 8 Exit 조건 매핑)
- 8 금지 사항 위반 0건 확인
- DRAFT 상태 적격 + G2/G3/G4 정식 채택 합의 준비 진입 적격 여부

### 1.2 단축 검토 채택 사유

- 본 G4 초안 작업은 *권위 흡수 + 형식·schema 정의*이며 새 권위 결정 0건 (헌법 5조 / ADR-008 차단조건 #2 / ADR-011 §2.4 답습 + system-identity-prequel §6.3 / §8.4 흡수)
- G4 PASS 합의는 본 검토 비대상 — 후속 PoC + (a)~(e) 충족 검증 (특히 §4 라운드트립 PoC) + **G3 §4.4.2 답습으로 외부 LLM 의견 권장**
- 직전 P2 v3 / G2 / G3 DRAFT 검토 (Reviewer-only, APPROVE AS DRAFT) 패턴 답습
- ADR-011 §2.4 T2 분류 (사용자 승인 기반 진행)

### 1.3 본 검토 자체의 메타 편향 인지 (선행)

**중요**: G4 는 *옵션 B 통합 문서* 로 *G3 §6.5 / §7 답습 + 자체 17 필드 schema 원안 + JSONL hash chain 원안* 을 동시 보유. 본 검토자(Reviewer)는 G4 초안 작성자와 동일 컨텍스트 → **자기 작성 산출 자기 검토 + 메타 편향 위험**.

본 §1.3 은 이를 명시 인지하며, §5 메타 편향 자기진단에서 다음을 통제:
- 본 검토는 *DRAFT 적격성* 한정 (G4 PASS 적격성 아님)
- G3 §4.4.2 ("Hermes PMO 격상 통합 합의 시 외부 LLM 1+ 필수")는 본 검토에 *DRAFT 적격성 한정* 으로는 적용되지 않으나, **G4 PASS 합의 시점 외부 LLM 의견 권장 + 격상 통합 합의 시 외부 LLM 1+ 필수**.
- G4 자체가 G3 §4 자기참조 차단의 *적용 대상* (§5.1 답습)

### 1.4 검토 비대상 (본 검토가 *판정하지 않는* 것)

- ❌ G4 PASS 적격성 — §1 ~ §8 각각 (a)~(e) Exit 기준 충족 검증 + 합의 (외부 LLM 권장)
- ❌ Hermes PMO 격상 적격성 — 4 게이트 통과 후 별도 결정 (외부 LLM 1+ 필수)
- ❌ G2 / G3 PASS 적격성 — 별도 합의 (G4 와 묶음 가능)
- ❌ P2 v3 정식 채택 적격성 — G2/G3/G4 완료 후 별도 합의
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신 적격성 + ADR-014 신규 후보 적격성
- ❌ P2 v2 / system-identity-prequel.md archive 처리 적격성
- ❌ 실 runtime 코드 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증) 적격성
- ❌ 실 migration script (`scripts/hermes-migration/*.py`) 적격성

---

## 2. 10 기준 점검 (G3 답습 + G4 §0.1 7 항목 + §8.1 8 Exit 매핑)

### 2.1 기준 #1 — Memory Scope 4 단계 정의 충실성

**확인 결과**: ✅ PASS

| 측면 | G4 위치 | 충실성 |
|------|--------|------|
| 4 scope 개요 (Global / Project / Session / Team-Agent) | §2.1 4-row 표 (Owner / MVP 적용 / 정체성) | ✅ |
| MVP scope 명시 (Global + Project) | §2.1 ✅ MVP + §2.2 본문 | ✅ |
| Global Memory 8 항목 (목적 / 저장 가능 / 금지 / Promotion / Retention / Export / Owner / 위치) | §2.2.1 8-row 표 | ✅ |
| Project Memory 8 항목 동일 구조 | §2.2.2 8-row 표 | ✅ |
| 환경변수 boundary (`CLAUDE_MEMORY_SCOPE`) | §2.2.3 + §2.5 2차 boundary | ✅ |
| 메타-템플릿 복사 시 오염 방지 (`.gitignore` + `init-project.sh`) | §2.2.3 답습 (system-identity-prequel §8.4) | ✅ |
| Session Memory 보류 + 후속 진입 사양 예고 | §2.3.1 + §2.3.2 | ✅ |
| Team/Agent Memory 보류 + 후속 진입 사양 예고 | §2.4.1 + §2.4.2 | ✅ |
| Boundary 5-layer 강제 메커니즘 (Filesystem / 환경변수 / Plugin / Promotion / Filesystem ACL) | §2.5 5-row 표 | ✅ |

**합의 §103 답습 확인**:
- "Memory 2단계 (Global + Project) 채택" ✅ §2.1 + §2.2
- "GPT 4단계 미채택 사유 (정량 트리거 미충족)" ✅ §2.1 본문 + §2.3.1 / §2.4.1 보류 사유
- "조건부 후속 (파생 프로젝트 ≥ 3건)" ✅ §2.3.1 / §2.4.1 후속 진입 조건

→ Criterion 1 PASS, Memory scope 4 단계 정의 충실 + MVP 명시 + boundary 5-layer 강제 + 합의 §103 답습.

### 2.2 기준 #2 — Skill Schema 17 필드 적절성

**확인 결과**: ✅ PASS

§3.1 17 필드:

| # | 필드 | 타입 | 필수 | Provider Lock-in 위험 | 적절성 |
|---|------|-----|----|-----------------|------|
| 1 | `id` | string | ✅ | 0 | ✅ UUID v4 또는 slug — provider-neutral |
| 2 | `name` | string | ✅ | 0 | ✅ human-readable |
| 3 | `version` | string | ✅ | 0 | ✅ semver |
| 4 | `scope` | enum | ✅ | 0 | ✅ Memory scope 와 일치 |
| 5 | `owner` | string | ✅ | 0 | ✅ provider-neutral identifier |
| 6 | `description` | string (md) | ✅ | 0 | ✅ 사용자 검토 가능 본문 |
| 7 | `inputs` | JSON Schema | ✅ | 0 | ✅ 표준 (RFC 인용 가능) |
| 8 | `outputs` | JSON Schema | ✅ | 0 | ✅ 동일 |
| 9 | `allowed_actions` | array | ✅ | 0 | ✅ 권한 등급 enum (read/write/shell/network/db/git/docker) — G3 §3.3 책임 분리 |
| 10 | `forbidden_actions` | array | 권장 | 0 | ✅ disjoint 검증 |
| 11 | `required_evidence` | array | 권장 | 0 | ✅ G3 §1.3 Hard Rule 흡수 |
| 12 | `required_tests` | array | 권장 | 0 | ✅ Phase 1 acceptance SOP 답습 |
| 13 | `promotion_status` | enum | ✅ | 0 | ✅ 5 상태 전이 (§3.3) |
| 14 | `rollback_triggers` | array | 권장 | 0 | ✅ G3 §3 답습 |
| 15 | `provider_bindings` | object | 권장 | ⚠️ 핵심 영역 | ✅ §3.5 검증 규칙 명시 |
| 16 | `created_from` | object | 권장 | 0 | ✅ 출처 추적 |
| 17 | `last_verified_at` | ISO 8601 | ✅ | 0 | ✅ 마지막 검증 시점 |

**필드 구조 평가**:
- 필수 9건 (#1~#9 + #13 + #17) — Skill 식별 + 동작 명세 + 권한 + 상태 + 검증 시점 모두 강제
- 권장 8건 (#10~#12 + #14~#16) — 운영·보안 강화 영역 (G3 흡수 영역)
- Provider Lock-in 위험 영역 1건 (#15) — §3.5 검증 규칙으로 *provider-neutral 보장* 강제

**합의 §103 답습 확인**:
- "Skill 자동 추출 T1 한정" ✅ §3.4 (T1 자동) + (T2 사용자 명시 승인 강제)
- "Skill 자동 등록·승격 금지" ✅ §3.4 + §5.2 #4

→ Criterion 2 PASS, 17 필드 정의 적절 + 검증 규칙 명시 + 합의 §103 답습.

### 2.3 기준 #3 — JSONL Export/Import 형식 충실성

**확인 결과**: ✅ PASS

| 측면 | G4 위치 | 충실성 |
|------|--------|------|
| 1 줄 = 1 entry 표준 | §4.1 + §4.2 (10 필드) | ✅ |
| Hash chain 변조 방지 | §4.4 (`prev_hash` + `hash` + genesis) | ✅ system-identity-prequel §6.3 답습 |
| Append-only 강제 | §4.4 entry 수정/삭제 금지 | ✅ |
| Canonical JSON 정의 | §4.4 (key 정렬 + whitespace 제거 + numeric 정규화 + RFC 8259 escape) | ✅ |
| Hermes 의존 0건 보장 | §4.3 4-row 표 (depcruise + jq 검증 + schema_version + 외부 오케스트레이터) | ✅ |
| Migration script 사양 | §4.5.1 4 후보 + §4.5.2 5 사양 요건 | ✅ |
| 라운드트립 검증 절차 | §4.6 (5단계 + PASS 조건) | ✅ R2-5 답습 |
| 의존성 형식 | `evidence_refs` 배열 / `schema_version` | ✅ §4.2 |

**Hermes 의존 0 4-검증** (§4.3):
1. `import hermes_agent` 등 의존 0건 (depcruise) ✅
2. `jq` + sha256 + canonical JSON ✅
3. schema_version 명시 declaration 후만 ✅
4. 외부 오케스트레이터 (claude/openai/gemini/local LLM) 최소 2+ 재해석 ✅

**손실 처리 명시** (§4.6):
- hash 일치 (정확) **또는** 의미 보존 검증 (사용자 명시 review — 손실 영역 명시)
- 손실 발생 시 ledger entry (`event: roundtrip_lossy`) ✅

**ADR-008 차단조건 #2 답습 확인**:
- "JSONL export 표준" ✅ §4 본문 자체 = 차단조건 #2 의 *형식 정의*

→ Criterion 3 PASS, JSONL 형식 충실 + hash chain + Hermes 의존 0 + 라운드트립 검증.

### 2.4 기준 #4 — Provider Lock-in 차단 핵심 메커니즘 (3-way)

**확인 결과**: ✅ PASS

§3.5 + §4.3 + §6.4 3-way 인터페이스:

| 메커니즘 | G4 형식 (§3.5 + §4.3) | G2 GP-5 코드 lock-in 차단 | G3 §6.4 Hermes-originated 변경 차단 |
|--------|------------|---------------------|------------------------|
| Skill `provider_bindings` 필드 | ✅ §3.1 #15 + §3.5 | (위임) | (위임) |
| Required / exclusive 금지 | ✅ §3.5 검증 규칙 | (위임) | (위임) |
| Optional optimization 한정 | ✅ §3.5 본문 + 예시 | (위임) | (위임) |
| 최소 2 provider 재해석 가능 | ✅ §4.3 + §3.5 | (위임) | (위임) |
| Provider SDK 직접 import 차단 (모든 작성 주체) | (위임) | ✅ depcruise 룰 | (위임) |
| Hermes-originated lock-in 변경 차단 | (위임) | (위임) | ✅ G3 §2.2 #18 + §6.4 |
| 모델명 분기 코드 차단 | (위임) | ✅ depcruise 룰 | (위임) |
| Migration script Hermes 의존 0 | ✅ §4.3 + §4.5.2 | ✅ depcruise | (위임) |

**예시 명시 정확성** (§3.5):
- OK 예시: `optional_optimization: true/false` — fallback 가능 명시 ✅
- 금지 예시: `required: true` + `custom_endpoint` — provider 종속 명시 ✅

**헌법 5조 (관용) 답습 확인**:
- 본 G4 §11 영구 핵심 제약 표 1행 "Provider Liquidity" 헌법 5조 + `feedback_provider_liquidity.md` + ADR-008 차단조건 #2 권위 인용 ✅
- 보호 위치 §3.5 + §4.3 + §6.4 (3-way 보호) 명시 ✅

→ Criterion 4 PASS, Provider lock-in 차단 3-way 보호 + 검증 규칙 명시 + 헌법 5조 답습.

### 2.5 기준 #5 — Promotion / Revocation 규칙 적절성 (5 상태 전이)

**확인 결과**: ✅ PASS

§3.3 5 상태 전이:

```
[proposed] → [approved] (T2 사용자) → [promoted] (Tools+Evidence)
                ↓                          ↓
             [archived] (T2)          [revoked] (rollback)
                                          ↓
                                      [archived] (T2)
                                          또는
                                      [approved] (재활성화 + 재검증)
```

| 상태 | 진입 조건 | 분류 | T 분류 적절성 |
|------|--------|------|----------|
| `proposed` | T1 자동 추출 (G3 §2.1 #3) | T1 | ✅ Hermes 자동 — 제안 한정 |
| `approved` | T2 사용자 명시 + schema 통과 | T2 | ✅ ADR-011 §2.4 직접 매핑 |
| `promoted` | Tools 검증 + Evidence ledger | T2 + Evidence | ✅ G3 §5.3 (i)~(iv) 답습 |
| `revoked` | rollback_trigger 매치 | T3 자동 안전 | ✅ T3 위반 차단 = 자동 안전 동작 |
| `archived` | T2 사용자 명시 | T2 | ✅ |

**§3.4 자동 생성 vs 자동 승격 분리 (핵심 원칙)**:
- "Skill 은 자동 생성될 수 있지만, 자동 승격되어서는 안 된다" ✅ 명시
- 5 단계 권한 분류 표 — 모두 ADR-011 §2.4 T 분류 매핑 정확
- §3.4 #5 `promoted` → `revoked` = T3 자동 안전 (rollback_trigger 자동 차단)
- §3.4 #4 `proposed` → `approved` = T2 (Hermes 자동 금지) — system-identity-prequel §8 답습

**§2.2 Promotion 조건 (Memory 측면)**:
- Project → Global = manual only (T2) ✅
- Session → Project = manual only (T2, Session 후속 시) ✅
- 자동 promotion 절대 금지 (T3 위반) ✅

→ Criterion 5 PASS, 5 상태 전이 + T 분류 + manual only 강제 충실.

### 2.6 기준 #6 — Memory/Skill Boundary 4 금지 사항 충실성

**확인 결과**: ✅ PASS

§5.2 4 금지:

| # | 금지 | 사유 | 강제 메커니즘 | 본 G4 위치 |
|---|-----|-----|----------|----------|
| 1 | Memory 가 policy 를 대체 | Constitution / ADR / SDD 본문 → Memory leak | G3 §2.2 #9 #11 (T3) + Memory write 권한 0 (사용자만) | §5.2 #1 |
| 2 | Skill 이 ADR / Constitution 우회 | Skill 본문이 정책 자동 수정 시도 | G3 §2.2 #10 #11 (T3) + `allowed_actions` 에 `policy_write` 미포함 | §5.2 #2 |
| 3 | Session memory 가 global memory 로 자동 승격 | Session 임시 → Global 영구 leak | §2.5 promotion T2 강제 + filesystem ACL | §5.2 #3 |
| 4 | Hermes 가 skill 을 자기 승인 | Hermes `proposed` → `approved` 자동 진행 시 자기 격상 | G3 §2.2 #16 (T2) + promotion hook 차단 | §5.2 #4 |

**§5.1 정의 명확성**:
- Memory = *상태 / 지식* (시점-의존, 사실 누적) — 예시 4건 ✅
- Skill = *절차 / 행위* (반복 가능, 입력-출력 명세) — 예시 2건 ✅

**§5.3 본 §5 가 *하지 않는* 것** 명시:
- Memory vs Skill 세부 구별 매트릭스 (사용자 review 영역) ❌ 본 초안 외
- 상호 변환 ❌ 본 초안 외 (분리된 경우만 다룸)
- Boundary 위반 자동 정정 ❌ (BLOCK + 사용자 명시 결정)

→ Criterion 6 PASS, 4 금지 명시 + 강제 메커니즘 + 정의 명확성 + 비대상 명시 충실.

### 2.7 기준 #7 — G3 인터페이스 5 항목 책임 분리 명확성

**확인 결과**: ✅ PASS

§6 G3 5 인터페이스:

| 항목 | G4 책임 (형식) | G3 책임 (권한) | §6 위치 |
|------|------------|------------|------|
| §6.1 Skill Escalation | `allowed_actions` / `forbidden_actions` 필드 + 권한 등급 enum | wrapper 권한 검증 + cap_drop / read_only / tmpfs noexec + audit log + 자동 비활성화 | §6.1 7-row 표 |
| §6.2 Hermes-originated Auto-approval 금지 | `promotion_status` 필드 + 5 상태 전이 + 상태 전이 규칙 | Hermes-originated commit auto-reject + `approved` T2 + `promoted` Evidence 강제 | §6.2 5-row 표 |
| §6.3 Evidence 없는 Promotion 금지 | `required_evidence` / `required_tests` / `last_verified_at` 필드 | Evidence Ledger entry 강제 + ledger 존재 검증 + hash chain 운영 강제 | §6.3 6-row 표 |
| §6.4 Provider Lock-in 차단 | `provider_bindings` 필드 + 검증 규칙 + 최소 2 provider | Provider SDK import 차단 + Hermes-originated 변경 차단 + 모델명 분기 차단 + Migration script Hermes 의존 0 | §6.4 7-row 표 (3-way) |
| §6.5 Memory Poisoning Rollback | `evidence_refs` / `created_from` / `rollback_triggers` 필드 + hash chain | Memory poisoning 검출 (T1 분석) + rollback (revert / `revoked`) + 사용자 alert | §6.5 7-row 표 |

**§6.6 통합 매트릭스** — 7-row 표로 G3 §6.5 / §7 책임 ↔ G4 §6 인터페이스 매핑.

**원칙 명시** (§6.6):
- G4 = *형식 / schema / export-import*
- G3 = *권한 / 신뢰 / 무결성*
- 두 게이트 모두 PASS 시 (4 게이트 통합 합의 후) 격상 충분 조건 일부 충족

**G3 §6.5 / §7 답습 정확성**:
- G3 §6.5 = "GP-6 ↔ G3 ↔ G4 3-way 인터페이스" 명시 → 본 G4 §6 + §7 흡수 정확 ✅
- G3 §7 = "G4 경계 — G3 6 책임 + G4 5 책임 + 공동 5 인터페이스" 답습 → 본 G4 §6 / §7 답습 정확 ✅

→ Criterion 7 PASS, 5 G3 인터페이스 책임 분리 명확 + G4 = 형식 / G3 = 권한 원칙 명시 + G3 §6.5 / §7 답습 정확.

### 2.8 기준 #8 — G2 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 명확성

**확인 결과**: ✅ PASS

§7.1 G2 GP-6 ↔ G4 책임 분리 (9-row 표):

| 항목 | G2 GP-6 (가능성) | G4 (형식) |
|------|------------|-------|
| JSONL schema | (위임) | ✅ §4.2 |
| Hash chain 변조 방지 | (위임) | ✅ §4.4 |
| Schema_version 호환성 | (위임) | ✅ §4.3 |
| 변환 스크립트 사양 | (위임) | ✅ §4.5 |
| 변환 스크립트 *실 구현* | ✅ GP-6 §8.6 산출 | (G4 범위 외) |
| 라운드트립 자동 테스트 | ✅ GP-6 §8.3 + R2-5 | ✅ §4.6 절차 |
| schema 검증 자동 테스트 | ✅ GP-6 §8.3 | ✅ §4.2 검증 규칙 |
| Hermes 메이저 업데이트 시 자동 회귀 | ✅ GP-6 §8.5 (d) | (위임) |
| 합의 보고서 (G4 + GP-6 통합 가능) | ✅ GP-6 §8.5 (e) | ✅ §8.3 |

§7.2 GP-6 ↔ G3 ↔ G4 3-way 인터페이스 (G3 §6.5 답습):

| 측면 | GP-6 (가능성) | G3 (권한) | G4 (형식) |
|------|------------|------|------|
| JSONL 형식 + 변환 스크립트 사양 | ✅ | (위임) | ✅ §4 |
| 라운드트립 검증 절차 | ✅ R2-5 | (위임) | ✅ §4.6 |
| Memory promotion **manual only** | (위임) | ✅ §2.2 #15 | (위임) |
| Skill 등록 **T2** | (위임) | ✅ §2.2 #16 + §3.4 | (위임) |
| Skill 권한 escalation 차단 | (위임) | ✅ §3.3 | (위임) |
| Memory / Skill schema 정의 | (위임) | (위임) | ✅ §2 + §3 |
| Memory / Skill export / import 구조 | ✅ Migration | (위임) | ✅ Schema |

**3-way 결합 명시** (§7.2):
- GP-6 *가능성* + G3 *권한* + G4 *형식* = Memory/Skill lock-in 차단의 *완결성*

**§7.3 GP-6 후속 갱신 권고**:
- GP-6 §8.5 (e) Exit 기준에 G4 cross-reference 추가 권고
- "(e) | 합의 APPROVE | 단축 또는 풀 3+1 합의 (G2 GP-6 + **G3 §6.5** + **G4** 통합 가능)"
- G3 단축 검토 §3.1 P-2 답습 — 일관 ✅

→ Criterion 8 PASS, 3-way 인터페이스 명확 + G3 §6.5 답습 정확 + GP-6 후속 갱신 권고 일관.

### 2.9 기준 #9 — Evidence 무결성 (Hash Chain + Canonical JSON)

**확인 결과**: ✅ PASS

| 측면 | G4 위치 | 충실성 |
|------|--------|------|
| Append-only 강제 | §4.4 (entry 수정/삭제 금지) | ✅ |
| Hash chain 형성 (`prev_hash` + `hash`) | §4.2 + §4.4 | ✅ |
| Genesis hash | §4.4 (`sha256("genesis:<scope>:<schema_version>")`) | ✅ |
| Canonical JSON — key 정렬 lexicographic | §4.4 | ✅ |
| Canonical JSON — whitespace 제거 (separator `","` / `":"`) | §4.4 | ✅ |
| Canonical JSON — numeric 정규화 (integer / float IEEE 754) | §4.4 | ✅ |
| Canonical JSON — string escape RFC 8259 | §4.4 | ✅ |
| Git append commit 대안 | §4.4 (둘 중 하나 의무) | ✅ |
| `evidence_refs` 출처 추적 | §4.2 + §6.5 | ✅ |
| `created_from` 출처 추적 (Skill) | §3.1 #16 | ✅ |
| `rollback_triggers` 필드 | §3.1 #14 | ✅ |

**system-identity-prequel §6.3 답습 확인**:
- "JSONL append-only" ✅ §4.4
- "hash chain — `prev_hash` + `hash` 변조 검출" ✅ §4.4
- "또는 git append commit" ✅ §4.4
- "둘 중 하나 의무" ✅ §4.4

**메타 한계 자기 명시** (§11.1):
- "JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고." ✅ 자기 발견 + 후속 권고

→ Criterion 9 PASS, hash chain + canonical JSON + 출처 추적 + git append 대안 + 메타 한계 자기 명시.

### 2.10 기준 #10 — G4 PASS / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive / 실 코드 / 실 migration script 암시 부재

**확인 결과**: ✅ PASS (암시 0건, 명시 부정 다수)

**명시 부정 위치**:

| 위치 | 부정 문구 |
|------|--------|
| 헤더 첫 줄 | "**G4 PASS 선언 / G2·G3 PASS / Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive 처리 / 실 runtime 코드 / 실 migration script 모두 본 초안 범위 외**" |
| §0.2 #1~#11 | 11건 명시 부정 |
| §0.3 단계 표 | 단계 1 (현 단계) ~ 단계 5 (정식 채택 후 ADR PR 묶음) — 시점 명시 분리 |
| §8.4 *발생* | "G4 status: 미작성 → PASS (CONTEXT.md 4 게이트 진행 상태 갱신)" — *합의 APPROVE 시점* 한정 |
| §8.4 *발생하지 않는 것* | G2 / G3 자동 PASS / Hermes PMO 자동 / P2 v3 정식 채택 자동 / archive 자동 / ADR 본문 자동 갱신 (cross-reference 만) / 실 runtime 코드 자동 / migration script 자동 |
| §11.2 | "본 초안은 G4 PASS 판정을 *준비* 만 하며 *발생시키지 않는다*" + 10건 명시 부정 |
| §11.3 즉시 강제 | "본 G4 가 정식 채택되지 않더라도" — DRAFT 상태 자체에서도 즉시 강제 5건 명시 (정식 채택은 별도) |
| 종료 줄 | 8건 명시 부정 |

**G4 PASS 합의 시점 명시 분리**:
- §8.1 (i)~(viii) Exit 조건 — 본 초안 *충족 영역* (8/8 ✅)
- §8.1 (a)~(e) 추가 G4 PASS 한정 조건 — 본 초안 *외* (PoC + 합의 + 외부 LLM)
- §8.3 G4 PASS 합의 형태 (옵션 1/2/3) — 사용자 결정 후보, 권고 단정 금지
- §8.4 G4 PASS *발생* vs *발생하지 않는 것* 명시 분리
- §10 변경 절차 DRAFT → 정식 채택 = 합의 + 각 § (a)~(e) 충족 + 외부 LLM 의견 권장

**잠재 암시 검색** (Reviewer 자기 검토):
- "충족" 단어: §8.1 표 "✅ 본 초안에서 충족" — *(i)~(viii) 8 Exit 조건* 한정. *(a)~(e) G4 PASS 추가 조건*에서는 명시 *외* 표기. 정직.
- "PASS" 단어: G1b PASS / G2/G3 DRAFT 적격 검토 APPROVE 등 *기존 권위 결정* 인용 + §8.1 entry 기준 + §8.4 G4 PASS 합의 시점 명시 *분리*. *G4 PASS / 격상 PASS / 정식 채택 PASS* 자동 인용 0건.
- "활성화" 단어: §0.3 단계 5 (G4 PASS 선언 + ADR cross-reference 갱신, G2/G3와 묶음 가능) — *합의 APPROVE 후* 라고 시점 명시. 자동 트리거 없음.
- "격상" 단어: 모두 §0.2 #3 / §11.2 / §11.3 등 *부정* 또는 *4 게이트 통과 후 별도 결정* 맥락에서 사용.
- "채택" 단어: §10 "DRAFT 상태 해제 → 정식 채택" — *별도 합의 APPROVE + 각 § (a)~(e) 충족 + 외부 LLM 의견 권장* 시점 명시. 자동 트리거 없음.

→ Criterion 10 PASS, 암시 0건, 명시 부정 다수 (헤더 + §0.2 11건 + §8.4 발생/비발생 분리 + §11.2 10건 + 종료 줄 8건).

---

## 3. 추가 점검 항목 (Reviewer 자기 발견)

본 §3은 사용자 명시 10 기준 외 Reviewer가 자기 발견한 잠재 위험 항목.

### 3.1 P-1 — §11.1 자기 명시 한계 (RFC 8785 JCS 미인용) (소프트 관찰, self-disclosed)

**위치**: 본 G4 §11.1 메타 한계 4번째 항목
> "§4.4 canonical JSON 정의 — JSON canonicalization 표준은 RFC 8785 (JCS) 등 명시 표준 존재. 본 초안은 JCS 직접 인용 안 함 (간단 명시 한정). 정식 채택 시 JCS RFC 인용 권고."

**관찰**:
- 본 한계는 **본 초안 자체가 self-disclosed** — Reviewer 자기 발견이 아닌 *원안 자기 인지* (적절)
- §4.4 본문은 4 항목 (key 정렬 / whitespace / numeric / string escape RFC 8259) 명시 — JCS 핵심 요건과 일치
- JCS RFC 직접 인용 부재는 *간이 명시* 한정이며 hash 일치 검증의 *결정성* 자체는 본문 4 항목으로 보장

**위험 등급**: 매우 낮음 (VERY LOW) — self-disclosed + 본문 4 항목 자체로 결정성 충분

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #1** 등록 — G4 PASS 합의 시점 또는 정식 채택 시점에 §4.4 본문에 RFC 8785 (JCS) 인용 추가 (또는 RFC 8259 escape 만으로 충분 명시).

### 3.2 P-2 — §10 schema 진화 정책 — 필드 *제거* / *변경* 정책 미명시 (소프트 관찰)

**위치**: 본 G4 §10 변경 절차 표
> "§3.1 17 필드 schema 본문 갱신 | 단축 합의 — 단, 필드 *추가* 는 schema_version 증가 (semver MINOR)"

**관찰**:
- 필드 *추가* 정책은 명시 (MINOR 증가)
- 필드 *제거* / *변경* / *필수→권장* 등 정책 미명시
- §4.5 외부 형식 → 본 G4 import 시 schema_version 호환성 (§4.3 #3) — 호환 부재 시 처리 절차 부재

**잠재 영향**:
- schema 진화 시 G4 PASS 후 필드 변경 발생 가능 (예: `provider_bindings` 검증 규칙 강화 / `required_evidence` 필수 승격)
- 필드 *제거* = Breaking change → semver MAJOR 증가 + migration 절차 필요 (현 본문 부재)

**위험 등급**: 낮음 (LOW)
- DRAFT 상태이며 후속 합의 시점에 정밀화 가능
- §3.1 17 필드 자체는 *MVP 0.1* 명시 (§4.2 schema_version), 진화 정책 후속 정의 가능

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #2** 등록 — G4 PASS 합의 시점에 §10 schema 진화 정책 보강 (필드 추가/제거/변경 각각 semver 정책 + migration 절차 명시).

### 3.3 P-3 — §4.5 외부 형식 import 시 schema_version 검증 절차 약함 (확인 사항)

**위치**: 본 G4 §4.5.1 변환 스크립트 후보
> "`scripts/hermes-migration/import.py` | 외부 형식 → 본 G4 JSONL | round-trip + checksum 검증"

**관찰**:
- 외부 형식 → 본 G4 JSONL import 절차는 `import.py` 사양만 명시
- §4.3 #3 "schema_version 호환성" 명시 — 본 `0.1` 이외 버전은 *명시 declaration 후만 import 가능*
- *명시 declaration* 의 절차 / 산출 / 합의 형태 미정의

**잠재 영향**:
- 외부 오케스트레이터 (claude / openai / gemini / local LLM) 에서 schema_version 다른 형식 import 시 검증 절차 불명확
- declaration 의 *권한* 분리 (사용자 명시 T2 / 자동 T1 가능 여부) 미정의

**위험 등급**: 낮음 (LOW)
- DRAFT 상태이며 §4.5.2 5 사양 요건에 schema_version 명시 + `--dry-run` flag 지원 명시되어 있어 *실 구현 시* 정밀화 가능
- import 자체는 G4 PASS *후* migration script 실 구현 (§0.2 #8) 단계의 일부

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #3** 등록 — G4 PASS 합의 시점 또는 migration script 실 구현 시점에 §4.3 #3 declaration 절차 정밀화 (사용자 명시 T2 + 합의 절차 명시).

### 3.4 P-4 — §6.4 "3-way 인터페이스" 명명 정확성 (확인 사항)

**위치**: 본 G4 §6.4 마지막 줄
> "**3-way 인터페이스**: G4 = `provider_bindings` *형식*, G2 GP-5 = *코드 lock-in 차단* (모든 작성 주체), G3 §6.4 = *Hermes-originated 변경 차단*. 셋이 결합 시 Provider Liquidity 의 *완결성*."

**관찰**:
- 본문은 G4 / G2 GP-5 / G3 §6.4 세 게이트 인용 → "3-way" 명명 정확
- 단, G4 책임은 §3.5 (`provider_bindings` 필드 정의) + §4.3 (Hermes 의존 0 + 최소 2 provider 재해석) **두 § 분산** — §6.4 7-row 표 첫 4 행 모두 G4 ✅
- 따라서 사실상 G4 두 § (§3.5 + §4.3) + G2 GP-5 + G3 §6.4 = "4 § across 3 gates" 구조이며 *3-way* 명명은 *게이트 단위* 기준에서 정확

**위험 등급**: 매우 낮음 (VERY LOW) — *게이트 단위* 명명 정확 + 본 §6.4 7-row 표 자체가 G4 두 § 명시로 분산 구조 명확

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #4** 등록 (선택) — G4 PASS 합의 시점에 §6.4 마지막 줄에 "(G4 두 § §3.5 + §4.3 결합)" cross-reference 추가 (정확성 강화). *처리 필수 아님* — 현 본문 자체가 7-row 표로 충분 분산 표시.

### 3.5 P-5 — §2.2.1 Global Memory `~/.claude/global/` Claude Code 표준 디렉토리 충돌 가능성 (소프트 관찰)

**위치**: 본 G4 §2.2.1 Global Memory 마지막 행
> "**저장 위치** | `~/.claude/global/` — filesystem 분리 (1차 boundary)"

**관찰**:
- Claude Code 는 이미 `~/.claude/projects/` / `~/.claude/.config/` 등 표준 디렉토리 사용 중
- `~/.claude/global/` 신규 디렉토리는 충돌 위험 *낮음* (기존 표준 디렉토리에 미존재)
- 단, *구체적 파일명* (예: `~/.claude/global/memory.jsonl`) 미명시 — implementation 시점에 정의 필요
- Claude Code 가 향후 `~/.claude/global/` 표준 명명 사용 시 충돌 가능 (현 시점 미발생)

**위험 등급**: 매우 낮음 (VERY LOW) — Claude Code 현 표준 미충돌 + implementation 시점 정밀화 가능

**권고 처리**: BLOCK 사유 아님 / **본 검토 후속 권고 #5** 등록 (선택) — implementation 시점에 `CLAUDE_GLOBAL_MEMORY_PATH` 환경변수 도입 검토 (override 가능성 + 충돌 회피). *처리 필수 아님* — 본 G4 *형식 / schema* 정의 단계에서는 path 명시만으로 충분.

---

## 4. 금지 사항 위반 점검 (사용자 명시 답습)

| # | 금지 항목 | 본 초안 위반 여부 |
|---|---------|---------------|
| 1 | G4 PASS 선언 | ❌ 위반 0건 (§2.10 기준 점검 결과 + 명시 부정 다수) |
| 2 | G2 / G3 PASS 자동 선언 | ❌ 위반 0건 (§6 / §7 인터페이스 한정 + §0.2 #2 + §8.4) |
| 3 | Hermes PMO 격상 선언 | ❌ 위반 0건 (헤더 + §0.2 #3 + §11.2 + §11.3 + 종료 줄 다중 명시 부정) |
| 4 | P2 v3 정식 채택 선언 | ❌ 위반 0건 (§0.2 #4 + §8.4 + 종료 줄 명시 부정) |
| 5 | ADR-008/009/010/011 본문 자동 갱신 + ADR-014 신규 자동 | ❌ 위반 0건 (§0.2 #5 + §8.4 "ADR 본문 자동 갱신 ❌ — cross-reference 만") |
| 6 | P2 v2 archive 처리 | ❌ 위반 0건 (§0.2 #6) |
| 7 | system-identity-prequel archive 처리 | ❌ 위반 0건 (§0.2 #6 + §11.3 즉시 강제 #1 "prequel archived 후에도 본 G4 §2.2 + §2.5 권위로 보존") |
| 8 | 실 runtime 코드 / 실 migration script 자동 구현 | ❌ 위반 0건 (§0.2 #7 #8 + §11.2 마지막 2건) |

→ 8/8 금지 항목 위반 0건.

---

## 5. 메타 편향 자기진단

### 5.1 본 검토의 자기 작성 산출 자기 검토 위험 (G3 §4 적용 대상)

**중요**: G4 는 *G3 §6.5 / §7 답습 + 자체 17 필드 schema 원안 + JSONL hash chain 원안* 을 동시 보유. 본 검토자(Reviewer)는 G4 초안 작성자와 동일 컨텍스트 → **자기 작성 산출 자기 검토 + 메타 편향 위험**.

본 §5.1 은 G3 §4 (합의 인프라 자기참조 차단) 자체에 의해 *적용 대상* 임을 명시:

1. 본 검토는 G3 §4.4.1 ("Reviewer-only 단축 합의 충분 조건")의 4 조건 중 *DRAFT 적격성* 한정 충족 — *G4 PASS* 합의는 G3 §4.4.2 답습으로 외부 LLM 의견 추가 권장.
2. 본 검토 *PASS 판정*은 *G4 PASS 판정*이 아님 (§1.4 답습).
3. 본 검토 자체가 G3 §4 자기참조 차단의 *적용 대상* — Reviewer-only 단축 합의는 ADR-011 §2.4 T2 영역에서 정당하나 *G4 PASS* 영역은 본 검토 비대상.
4. 특히 **G4 §3.1 17 필드 schema** + **§4.4 hash chain canonical JSON** + **§6 G3 5 인터페이스 + §7 GP-6 3-way 책임 분리 매트릭스** 모두 *원안* — 외부 LLM 시야에서 추가 검증 권장.

### 5.2 5 통제 답습

| # | 통제 수단 | 본 검토 적용 |
|---|---------|---------|
| 1 | 사용자 명시 절차 답습 | ✅ G2/G3 검토 패턴 답습 + 사용자 명시 10 기준 §2 + 8 금지 항목 §4 + DRAFT 적격 검토 한정 |
| 2 | 직전 단축 합의 패턴 답습 | ✅ P2 v3 / G2 / G3 DRAFT 검토 §1/§2/§3/§4/§5/§6 구조 답습 |
| 3 | 10 항목 답습 + 8 금지 점검 | ✅ §2 10/10 + §4 8/8 점검 |
| 4 | 자기 발견 잠재 위험 명시 (§3 P-1 ~ P-5) | ✅ 5건 자기 발견, 모두 LOW/VERY LOW + BLOCK 사유 아님 |
| 5 | 본 검토가 *하지 않는* 것 명시 (§1.4) | ✅ 8건 명시 비대상 |

### 5.3 본 검토의 한계

- 본 검토는 *자기 작성 산출 자기 검토* (P2 v3 / G2 / G3 / G4 모두 동일 컨텍스트)
- **G3 §4.4.2 답습**: 자기 작성 산출 검증은 외부 LLM 의견 *권장* — 본 검토가 외부 LLM 의견 대체 불가
- **G4 PASS 합의는 외부 LLM 의견 권장 + 격상 통합 합의는 외부 LLM 1+ 필수** (G3 §4.4.2). 본 검토는 그 적격성 판정 비대상.
- §3 자기 발견 잠재 위험 5건은 본 Reviewer 의 시야 한정 — 외부 LLM 시야에서 추가 발견 가능.
- 특히 **§3.1 17 필드 schema 원안** + **§4.4 canonical JSON 원안** + **§6 G3 5 인터페이스 매트릭스 원안** + **§7 GP-6 3-way 매트릭스 원안** 4건은 본 검토가 *적정성*을 완전 판정하기 어려움 (자기 검증 한계). G4 PASS 합의 시점 외부 LLM 의견 권장.
- 본 G4 §11.1 메타 한계 6건 (자기 작성 / 17 필드 / Session·Team 후속 / canonical JSON / 6.4 3-way / 7.2 3-way) 자기 명시 — 적절. Reviewer 추가 발견 5건 (P-1 ~ P-5) 과 일부 중첩 (P-1 = §11.1 #4 self-disclosed) 또는 보강 (P-2 ~ P-5 신규).

### 5.4 본 검토의 *PASS 판정이 트리거하지 않는 것*

본 §6 결론 PASS 판정은 다음을 *트리거하지 않는다*:

- ❌ G4 PASS
- ❌ G2 / G3 PASS 선언
- ❌ Hermes PMO 격상
- ❌ ADR-008/009/010/011 갱신 + ADR-014 신규
- ❌ P2 v2 / system-identity-prequel archive
- ❌ INDEX / CONTEXT 갱신
- ❌ Phase 진입 결정
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ G2/G3/G4 정식 채택 합의 자동 시작 (사용자 명시 결정 대기)

본 검토 PASS 판정은 *오직* "G4 형식 / schema / export-import 설계 DRAFT 적격 + G2/G3/G4 정식 채택 합의 준비 진입 적격" 의미.

---

## 6. 결론

### 6.1 판정

```
✅ APPROVE AS DRAFT
```

### 6.2 사유

- **10 기준 10/10 PASS** (§2.1 ~ §2.10) — Memory scope 4 단계 + Skill schema 17 필드 + JSONL 형식 + Provider lock-in 3-way + Promotion 5 상태 + Boundary 4 금지 + G3 5 인터페이스 + GP-6 3-way + Evidence 무결성 + 암시 0건
- **8 금지 항목 8/8 위반 0건** (§4)
- **자기 발견 잠재 위험 5건** (§3 P-1 ~ P-5) 모두 LOW / VERY LOW 등급 + BLOCK 사유 아님 + G4 PASS 합의 시점 또는 정식 채택 시점에 흡수 가능
- **메타 편향 5 통제 답습** (§5.2)
- **G3 §4 자기참조 차단의 *적용 대상*** 으로 본 검토 한계 명시 (§5.1 + §5.3)
- **G4 §11.1 메타 한계 6건 자기 명시** (적절) + Reviewer 추가 발견 5건 (P-1 = §11.1 #4 중첩, P-2 ~ P-5 보강)

### 6.3 후속 권고 (DRAFT 적격성과 *분리*)

본 결론은 DRAFT 적격성 판정 한정. 후속 작업 시 다음 표현 정밀화 권고 (선택):

| # | 권고 (선택) | 위치 | 처리 시점 |
|---|---------|-----|---------|
| 1 | §4.4 canonical JSON 정의에 RFC 8785 (JCS) 인용 추가 (또는 RFC 8259 escape 만으로 충분 명시) | G4 §4.4 | G4 PASS 합의 시점 또는 정식 채택 시점 |
| 2 | §10 schema 진화 정책 보강 — 필드 추가/제거/변경 각각 semver 정책 + migration 절차 명시 | G4 §10 | G4 PASS 합의 시점 |
| 3 | §4.3 #3 schema_version declaration 절차 정밀화 (사용자 명시 T2 + 합의 절차 명시) | G4 §4.3 / §4.5 | G4 PASS 합의 시점 또는 migration script 실 구현 시점 |
| 4 | §6.4 마지막 줄에 "(G4 두 § §3.5 + §4.3 결합)" cross-reference 추가 (선택, 처리 필수 아님) | G4 §6.4 | G4 PASS 합의 시점 |
| 5 | implementation 시점 `CLAUDE_GLOBAL_MEMORY_PATH` 환경변수 override 검토 (선택) | implementation | G4 PASS 후 실 runtime 코드 구현 시점 |

본 권고 5건은 *G4 PASS 합의 또는 정식 채택 진입 시점* 에 함께 검토. 본 DRAFT 적격성 판정 단계에서는 처리 불필요.

### 6.4 G2/G3/G4 정식 채택 합의 준비 진입 적격성

본 G4 DRAFT 적격성 판정 결과 + 사용자 명시 결정 ("G4 DRAFT 검토 APPROVE 시 G2/G3/G4 정식 채택 합의 준비 진입") 답습 → **G2/G3/G4 정식 채택 합의 준비 진입 적격**.

정식 채택 합의 형태 후보 (사용자 결정 대기, 권고 단정 금지):

| 옵션 | 합의 형태 | 비고 |
|-----|---------|-----|
| 1 | G4 단독 단축 합의 (Reviewer-only) | 새 권위 결정 0건 — 단축 합의 적격 (단, 외부 LLM 의견 권장) |
| 2 | G4 + G2 GP-6 통합 합의 (단축 또는 풀 3+1) | GP-6 §8.5 (e) 답습 + G3 §6.5 / §7.3 답습 |
| 3 | **G2 + G3 + G4 통합 풀 3+1 합의 + 외부 LLM 1+ (PR 묶음)** | **격상 통합 합의 답습** — P2 v3 §9.2 / G2 §10.2 / G3 §8.2 / G4 §8.3 옵션 3 패턴 |

**참고** (사용자 결정 후보, 권고 단정 금지):
- 옵션 3 = G2/G3/G4 통합 풀 3+1 + 외부 LLM 1+ 가 메타 편향 통제 + PR 묶음 + Hermes PMO 격상 통합 합의 답습 시 비용 효율적
- 단, 옵션 1 / 2 도 사용자 결정 시 정당
- 옵션 3 채택 시 외부 LLM 1+ 필수 (G3 §4.4.2 영구 권위)

### 6.5 본 검토 보고서 commit 절차

본 결론 APPROVE AS DRAFT에 따라 다음 단일 파일을 별도 commit으로 처리 가능:

```
docs/review/3plus1-consensus-2026-05-09-g4-provider-agnostic-memory-skill-draft.md
```

commit 메시지 (G2/G3 패턴 답습):
```
docs(review): record G4 provider-agnostic memory/skill draft short review
```

본 commit에 포함하지 *않는* 항목 (사용자 명시 답습):
- G4 본문 갱신
- G2 / G3 본문 갱신 (P-2 G2 §8.5 / P-4 §6.4 cross-reference 등)
- ADR-008/009/010/011 본문 갱신 + ADR-014 신규
- P2 v2 / system-identity-prequel archive 처리
- INDEX / CONTEXT 갱신 (다음 세션 housekeeping 영역)
- Hermes PMO 격상 선언
- G2 / G3 / G4 PASS 선언
- 실 runtime 코드 / 실 migration script 구현

---

## 7. 다음 진입점 (본 검토 *이후*)

본 검토 PASS 후 사용자 명시 단계 답습:

| # | 단계 | 산출 | 시점 |
|---|------|------|------|
| 1 | G4 초안 Reviewer-only 단축 검토 | 본 보고서 | 본 단계 (완료) |
| 2 | 검토 보고서 별도 commit | `docs(review): record G4 provider-agnostic memory/skill draft short review` | 본 단계 직후 |
| 3 | G2/G3/G4 정식 채택 합의 형태 결정 | 사용자 결정 — 옵션 1 (G4 단독 단축) / 옵션 2 (G4 + GP-6 통합) / 옵션 3 (G2+G3+G4 풀 3+1 + 외부 LLM 1+) | 사용자 명시 결정 후 |
| 4 | (옵션 3 채택 시) 풀 3+1 통합 합의 + **외부 LLM 1+ 필수** | `docs/review/3plus1-consensus-YYYY-MM-DD-g234-integrated.md` + 외부 검토 의뢰 자료 (`docs/external-review/` 패턴 답습) | 사용자 명시 결정 후 |
| 5 | 정식 채택 후 ADR PR 묶음 | ADR-008/009/010/011 cross-reference 갱신 + 신규 ADR-014 (Provider-agnostic Memory/Skill Format) 후보 검토 + P2 v2 / system-identity-prequel archive + INDEX/CONTEXT 갱신 | 합의 APPROVE 후 |

본 검토 *이후* 금지 사항은 변동 없음 — §4 8 금지 항목 + 사용자 명시 답습.

---

**검토일**: 2026-05-09
**검토자**: Reviewer-only (메타 편향 자기진단 §5 명시 + G3 §4 자기참조 차단의 적용 대상 인지)
**판정**: ✅ APPROVE AS DRAFT
**다음 단계**: 본 검토 보고서 별도 commit → G2/G3/G4 정식 채택 합의 형태 결정 (사용자 명시 결정 후)
