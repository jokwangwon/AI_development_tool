# Agent B — 보안/거버넌스 분석 (G2 + G3 + G4 통합)

**작성일**: 2026-05-09
**Agent 역할**: 보안/거버넌스 검증 (3+1 풀 합의)
**검토 범위**: G2 + G3 + G4 정식 PASS 승격 + P2 v3 정식 채택 진입 가능 여부
**검토자 컨텍스트**: 본 분석은 메인 컨텍스트와 동일 클로드 인스턴스가 작성 — 자기참조 + 메타 편향 위험 인지하며 §6 / §9 에서 통제
**격상 범위 외**: Hermes PMO 격상 선언 / P2 v3 자동 채택 / ADR 본문 자동 갱신 / archive 자동 처리는 본 합의 범위 외 (사용자 명시 결정 답습)

---

## 0. 요약 (Executive Summary)

### 0.1 핵심 결론 (보안/거버넌스 관점)

| 항목 | 판정 | 근거 |
|------|------|------|
| Hermes ≠ root of trust 운영 충족도 | **APPROVE WITH CONDITIONS** | G3 §1~§5 권위 위계·22 권한 분류·자기참조 차단·Evidence 결정 모두 ADR-011 §2.3 / system-identity-prequel §3 권위 직접 흡수. 단 *설계 한정* — 실 hook/wrapper 코드 0건은 Exit (b)/(d) 잔여 |
| ADR-011 §2.4 T1/T2/T3 일관성 | **APPROVE** | 본 통합 PASS 가 T3 영역 변경 0건. T2 (G2/G3/G4 PASS 합의 + GP 진입 + Skill/Memory promotion) 모두 사용자 명시 강제 명시 |
| Provider Liquidity 무결성 | **APPROVE WITH CONDITIONS** | G4 §3.5 `provider_bindings` *required/exclusive 금지* + §4.6 라운드트립 + GP-5 depcruise 룰 3-way 보호. 단 라운드트립 PoC + 변환 스크립트 실 산출 0건 (G4 PASS 기준 (a)~(b) 잔여) |
| Memory/Skill lock-in / escalation 통제 | **APPROVE WITH CONDITIONS** | 17 schema 필드 + JSONL hash chain + 4 boundary + Skill 자동 생성 vs 자동 승격 분리 + G3 §3.3 wrapper escalation 모두 정의. 단 자동 승격 차단 hook 실 코드 0건, Skill `created_from` 가 *Hermes-originated* 검증 항목으로 직접 활용되지 않음 (Gap-2) |
| 헌법 8조 위반 경로 P1~P8 충분성 | **APPROVE WITH GAPS** | P1~P8 합의 §29~§30 enumeration 정합. 단 §1.2.4 가 본 G2 범위 외로 명시적으로 *배제*한 항목 중 §1.2.1 8조 #4 (보안 변경은 3+1 합의) *프로세스 강제* 가 GP 매트릭스 본문에 누락 — Gap-1 |
| 메타 안전장치 단일 실패점 | **APPROVE WITH NOTE** | G2 §9 + G3 §4 + G3 §5.5 가 *상호 보강* (서로 다른 차원: §9=interface 선언 / G3 §4=합의 자기참조 / G3 §5.5=PASS 성립 요건). 단 *모두 동일 컨텍스트 자기 작성 산출* — 외부 LLM 1+ 가 격상 합의 시점 필수 (G3 §4.4.2) |
| Evidence 결정 5 운영 규칙 + 위조 차단 | **APPROVE WITH CONDITIONS** | §5.3 (i)~(iv) Hard Rule + JSONL append-only + hash chain + Hermes-originated commit auto-reject. 단 hash chain 검증 hook + ledger 검증 step 실 코드 0건 |

### 0.2 본 분석의 *판정하지 않는* 것

- ❌ Hermes PMO 격상 선언/권유
- ❌ P2 v3 정식 채택 자동 선언
- ❌ ADR 본문 자동 갱신 권유
- ❌ archive 자동 처리 권유
- ❌ 실 runtime code / migration script 작성
- ❌ G2/G3/G4 PASS 합의 자동 발화 (본 분석은 *Reviewer 의 종합 판정* 입력 한정)
- ❌ 다른 Agent (A, C) 출력 참조

---

## 1. Hermes ≠ root of trust 충족도 검증

### 1.1 G3 §4 자기참조 차단 효력 분석

**§4.1 문제 정의**: Hermes 가 합의 *실행 인프라* 라면, Hermes 관련 결정의 합의를 Hermes 가 실행 → 자기참조 역설. 합의 §90 (Agent B 단독 발견) 흡수.

**§4.2 4 차단 원칙**:
1. Hermes 관련 결정은 Hermes 단독 합의 금지 (system-identity-prequel §3.3 #2 + §4.3 매트릭스)
2. Reviewer-only 또는 외부 LLM 의견이 Hermes 관련 결정 합의에 필수 (§4.4.2)
3. 사용자 승인이 모든 T2/T3 결정의 *최종* 권위 (ADR-011 §2.4 + §2.3 #5)
4. Hermes 는 합의 결과 *기록*만 가능, *승인 주체*가 될 수 없음 (system-identity-prequel §3.3 #2)

**효력 판정**: **충실** — 4 원칙이 ADR-011 §2.3 운영 함의 #5 ("Human overrides") + system-identity-prequel §3.3 #2 (git commit 강제 보존) 양대 권위에 정확 매핑. 합의 §90 핵심 흡수.

**§4.3 결정 유형 13건 매트릭스**: T1 자동 (3건), T2 사용자 명시 (8건), T3 절대 금지 (2건). **본 통합 합의 자체** = T2 영역 (G2/G3/G4 PASS) — 매트릭스 row 명시. 자기참조 차단 정합.

**§4.5 Hermes 합의 결과 처리 권한**: 합의 결과 보존을 *git commit immutable* 로 강제 + Hermes-originated commit auto-reject (Hermes 관련 결정 한정). **fox guarding the henhouse 차단** 메커니즘 명확.

### 1.2 G3 §5.5 합의 인프라 순환 권위 해결 효력

본 항목은 §5.5 라기보다 §5.3 (PASS 성립 요건) + §1.3 (Evidence 없는 PASS 차단) + §4 (자기참조 차단) 의 *결합*:

| 측면 | 메커니즘 | 권위 |
|------|--------|-----|
| Evidence Ledger entry 의무 | JSONL append-only + hash chain (G4 §4.4) | system-identity-prequel §6.3 |
| 합의 보고서 commit 의무 | git commit (Hermes-originated 시 reject) | system-identity-prequel §3.3 #2 |
| 사용자 명시 승인 의무 | T2/T3 영역 commit author 검증 | ADR-011 §2.4 |
| Tools 검증 통과 의무 | Layer 1~4 hook + CI | CLAUDE.md §피드백 루프 |

**효력 판정**: **상호 보강** — 4 메커니즘이 *각각 다른 차원* 에서 PASS 성립을 강제. 어느 하나 우회 시 다른 3개로 차단. 단일 실패점 회피.

### 1.3 우회 경로 식별

본 검토자가 *명시적 자기참조 + 적대적 사고* 로 식별한 우회 후보:

| # | 후보 우회 경로 | 차단 메커니즘 | 잔여 위험 |
|---|----------------|--------------|---------|
| U-1 | Hermes 가 *user 가장* 으로 사용자 명시 commit 모방 | git commit author 검증 + audit log | **잔여 LOW** — DRAFT 단계에서 git author 검증 hook 코드 0건. 운영 환경 git config 정확성 의존 |
| U-2 | Hermes 가 *Worker Agent 출력* 으로 자기 결정 우회 (Worker → Hermes 권위 escalation) | G3 §1.2.2 (Worker 출력 ≠ Hermes 위) + GP-4 (Hermes/Worker 출력 = 외부 입력) | **잔여 LOW** — sanitizer + escape 강제는 명확. 단 PoC 0건 |
| U-3 | Hermes 가 *Tools 결과* 위조 (CI run ID / artifact / verdict 본문 위조) | Evidence Ledger hash chain + GitHub Actions run ID 외부 검증 | **잔여 MEDIUM** — hash chain 본문 위조는 chain 끊어짐으로 검출. 단 *이전 chain 전체 재계산 후 위조* 시 검출 어려움 — append-only filesystem (chattr +a) 권고 |
| U-4 | Hermes 가 *합의 보고서* commit 을 user-author 로 위조 (git config 변경) | filesystem read-only on `.git/config` + audit log on `.git/` 변경 | **잔여 MEDIUM** — `.git/` read-only 강제 미명시 (G3 §2.2 #11 Constitution 우회 차단의 확장 필요) |
| U-5 | Hermes 가 *외부 LLM 의견* 을 위조 (`docs/external-review/` 본문 자동 생성) | system-identity-prequel §3.3 #2 (사용자 명시 commit) + 외부 LLM 호출 audit | **잔여 MEDIUM** — `docs/external-review/` 가 Hermes write 가능 영역인지 명시 부재 (Gap-3) |

**판정**: U-1, U-2 는 명시적 차단. U-3, U-4, U-5 는 **DRAFT 한계** — 격상 통합 합의 시점 외부 LLM 1+ 의견으로 추가 검증 권장.

### 1.4 "Hermes-originated commit auto-reject" 강제 메커니즘 견고성

G3 §3.1 (Learning silent drift) + §4.5 매트릭스에서 명시:
- git commit author / committer + Hermes audit log cross-reference (every commit)
- pre-commit hook on 정책 파일 — Hermes-originated commit 자동 reject
- nightly diff + Hermes-originated detection

**견고성**: **설계 충실, 구현 잔여**. 강제 메커니즘 표 (§2.4 매트릭스 22 권한) 는 계산적 22/22 + 자동 롤백 14/22 — *설계 측면* 완결성 확보. 단 실 hook / pre-commit / CI step 코드는 본 PASS 합의 후 산출 (G3 §0.2 #7 명시 — 본 초안 범위 외).

**G3 PASS 가 정당한 시점**: §1~§7 각각 (a)~(e) Exit 충족 시. 본 분석 시점에는 (a)/(c)/(e) 일부 충족 가능, (b) PoC + (d) 자동 회귀 잔여.

---

## 2. ADR-011 §2.4 T1/T2/T3 일관성

### 2.1 본 통합 PASS 가 T3 영역에 영향 주는가?

**T3 = "정책/헌법/ADR/Constitution 본문 자동 변경 절대 금지"** (ADR-011 §2.4).

본 통합 PASS 합의가 트리거하는 결과 (G2 §10.3 / G3 §8.3 / G4 §8.4 명시):
- ✅ G2/G3/G4 status 갱신 (CONTEXT.md 4 게이트 진행)
- ✅ 본 문서들 헤더 "DRAFT" 제거 + 합의 보고서 cross-reference 추가
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신 → **별도 PR 명시**
- ❌ ADR-014 신규 후보 자동 작성 → **별도 PR 명시**
- ❌ Constitution 본문 변경 → **0건**
- ❌ Harness Gate 정의 자체 변경 → **0건**

**판정**: **T3 위반 0건**. cross-reference 갱신 / status 갱신은 T3 영역 외 (ADR-011 §2.4 T2 영역, 사용자 명시 결정 결과 실행).

### 2.2 T2 (사용자 승인) 경로 명확성

| 영역 | T2 경로 명시 위치 | 명확성 |
|------|---------------|------|
| G2/G3/G4 PASS 합의 형태 결정 | G2 §10.2 / G3 §8.2 / G4 §8.3 옵션 1/2/3 (사용자 결정) | ✅ |
| GP-1~GP-6 진입 결정 | G2 §3.4~§8.4 ⏳ "사용자 명시 진입" | ✅ |
| Skill 등록 (proposed → approved) | G3 §2.2 #16 + G4 §3.4 | ✅ |
| Memory promotion (Project → Global) | G3 §2.2 #15 + G4 §2.2.1 / §2.2.2 manual only | ✅ |
| 의존성 업그레이드 PR merge | G3 §3.2.6 | ✅ |
| 사용자 override (Tools/Evidence/합의 결과) | G3 §5.4 | ✅ |
| Skill `approved` → `promoted` (Tools+Evidence) | G4 §3.4 + G3 §5.3 | ✅ |
| Skill `revoked` → `approved` 재활성화 | G4 §3.3 + G3 §3.3.6 | ✅ |

**판정**: **T2 경로 모두 명시**. 사용자 명시 강제 부재 영역 식별 0건.

### 2.3 T1 (자동 학습) 경계 — Memory/Skill 자동 갱신

**T1 자동 허용 영역** (G3 §2.1):
- 작업 분배 / Memory 조회 (read-only) / Skill 후보 *제안* / 합의 orchestrate 보조 / Evidence 위치 *정리* / 다음 작업 *제안* / 자체 학습 (도구 사용 빈도 / 실패 회피 휴리스틱) / Hermes 자체 redaction (로그/송신 한정)

**T1 vs T2 경계 (Memory/Skill 자동 갱신 측면)**:

| 동작 | T 분류 | 명시 위치 | 경계 명확성 |
|------|------|--------|----------|
| Memory read | T1 | G3 §2.1 #2 | ✅ read-only 한정 |
| Memory write (Project/Global 어디든) | T2 (사용자 명시) | G3 §2.2 #15 + G4 §2.2.1/§2.2.2 (Owner=사용자) | ✅ filesystem ACL 강제 |
| Skill 후보 *추출* (proposed) | T1 | G4 §3.4 1행 | ✅ |
| Skill `proposed` → `approved` | T2 | G4 §3.4 2행 + G3 §2.2 #16 | ✅ |
| Skill `approved` → `promoted` | T2 + Evidence | G4 §3.4 3행 + G3 §5.3 | ✅ |
| Skill `promoted` → `revoked` (rollback_trigger) | T3 자동 안전 | G4 §3.4 4행 | ✅ rollback = 자동 차단 안전 동작 (T3 위반 차단) |
| 자체 학습 결과의 *정책 파일* 반영 | T3 절대 금지 | G3 §2.2 #17 + §3.1 (silent drift) | ✅ filesystem read-only + 컨테이너 정지 |

**판정**: **T1/T2/T3 경계 명확**. 단 *자체 학습 → Skill 후보 추출* 사이의 inference (예: "이 패턴은 정책 변경을 *암시*") 가 *암시적 T3 트리거* 가능성 — G3 §3.3.2 audit log T1 분석으로 일부 검출 명시. **잔여 위험 LOW**.

---

## 3. Provider Liquidity 무결성

### 3.1 G4 schema 17 필드 lock-in 위험 평가

| 필드 | Lock-in 위험 | 차단 메커니즘 |
|------|----------|----------|
| #1~#14 + #16~#17 (16건) | **0** | provider-neutral 표준 (UUID / semver / JSON Schema / ISO 8601 / enum) |
| #15 `provider_bindings` | **MEDIUM** | §3.5 *required / exclusive 금지* + 최소 2 provider 재해석 + provider 종속 endpoint 본문 작성 금지 (G2 GP-5 + G3 §6.4 답습) |

**§3.5 검증 규칙 견고성**:
- "어떤 provider 도 *required* 또는 *exclusive* 표시 금지" — **금지 enumeration 명시**
- "모든 binding 은 *optional optimization* 한정" — **의미 강제**
- "최소 2 provider 로 재해석 가능 (예: claude / openai / ollama 중 2+)" — **숫자 강제**
- "Provider 종속 endpoint / SDK / 모델명 분기는 Skill 본문에 작성 금지 (G2 GP-5 + G3 §6.4 답습)" — **다른 게이트 cross-reference**

**잔여 위험**: §3.5 의 검증을 *계산적 도구* 로 강제하는 메커니즘 (예: skill schema validator 에서 `required: true` 자동 reject) 의 *실 코드* 0건. **G4 PASS 기준 (b)~(d) 잔여**.

### 3.2 G2 GP-5 (depcruise) / GP-6 (마이그레이션) 보강성

**GP-5** (G2 §7): `import hermes_agent` / `import litellm` / `import anthropic` / `import openai` 직접 import + 모델명 분기 코드 정적 차단.
- 강제 메커니즘: depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject
- Exit (a)~(e): (c) ADR-008 차단조건 #4 권위 ✅ / 나머지 ⏳

**GP-6** (G2 §8): JSONL append-only 표준 + 변환 스크립트 (Hermes ↔ Claude/GPT) 1회 시연 (R2-5 답습) + 라운드트립 검증.
- 강제 메커니즘: JSONL schema 검증 + 변환 스크립트 자동 테스트 + 라운드트립 검증
- Exit (a)~(e): (c) ADR-008 차단조건 #2 권위 ✅ / 나머지 ⏳

**보강 관계**:
- GP-5 = *코드 lock-in* 차단 (모든 작성 주체)
- GP-6 = *학습 자산 lock-in* 차단 (마이그레이션 가능성)
- G3 §6.4 = *Hermes-originated lock-in 변경* 차단 (작성 주체 = Hermes 한정)
- G4 §3.5 + §4.3 = *형식/schema 자체* lock-in 차단

**3-way (GP-5 + G3 §6.4 + G4 §3.5) + GP-6 = 4-way 보호**. 한 layer 우회 시 다른 3개로 차단. 단일 실패점 회피.

### 3.3 변환 스크립트 + JSONL export 출구 검증 가능성

**G4 §4.6 라운드트립 검증 절차**:
```
원본 Hermes JSONL → hermes_to_claude.py → Claude 형식
       → 다시 G4 JSONL 로 변환 → canonical JSON sha256 비교
       → 원본 hash 일치 검증 (또는 의미 보존 review)
```

**검증 가능성**:
- ✅ 절차 명확 (R2-5 답습)
- ✅ PASS 조건 명시 (정확 hash 일치 또는 의미 보존 + 손실 영역 ledger entry)
- ⏳ 실 PoC 산출 0건 (G4 §0.2 #8 명시 — 본 초안 범위 외)
- ⏳ `scripts/hermes-migration/*.py` 실 코드 0건

**판정**: **출구 명시 + 검증 절차 정의 충실, 실 산출 잔여**. **G4 PASS 기준 (b) 격리 환경 PoC 잔여**.

---

## 4. Memory / Skill lock-in + escalation 위험

### 4.1 17 schema 필드 보안 측면 분석

| 보안 측면 | G4 필드 | 판정 |
|---------|--------|----|
| Skill 권한 enumeration | #9 `allowed_actions` (read/write/shell/network/db/git/docker) + #10 `forbidden_actions` (disjoint) | ✅ G3 §3.3 wrapper escalation 차단의 *형식 입력* |
| Evidence 강제 (PASS 조건) | #11 `required_evidence` + #12 `required_tests` + #17 `last_verified_at` | ✅ G3 §1.3 / §5.3 Hard Rule 흡수 |
| 출처 추적 (poisoning 방어) | #16 `created_from` (task_id / commit_sha / agent) + Memory entry `evidence_refs` | ✅ G3 §3.1 silent drift detection 의 *형식 입력* |
| Rollback trigger | #14 `rollback_triggers` enum (escalation_detected / evidence_missing / t3_violation) | ✅ G3 §3 답습 |
| Promotion 5 상태 (자동 승격 차단) | #13 `promotion_status` (proposed/approved/promoted/revoked/archived) | ✅ G3 §2.2 #16 + §3.4 답습 |

**판정**: **17 필드 모두 보안 측면 명확**. Provider lock-in 위험 영역 #15 외 보안 위험 0건.

### 4.2 JSONL append-only hash chain 변조 방지 효력

**G4 §4.4 메커니즘**:
- entry 수정/삭제 금지 (append-only)
- hash chain — `prev_hash` + `hash` (sha256)
- 또는 git append commit (둘 중 하나 의무)
- Canonical JSON 정의 (key 정렬 / whitespace / numeric / RFC 8259)
- Genesis hash 정의

**변조 방지 강도**:

| 공격 시나리오 | 차단 강도 | 잔여 위험 |
|------------|--------|--------|
| 단일 entry 본문 위조 | **HIGH** — chain 끊어짐 즉시 검출 | 0 |
| 단일 entry 삭제 | **HIGH** — chain 끊어짐 즉시 검출 | 0 |
| chain 재계산 후 전체 위조 (시점 t 이후 모든 entry 재작성 + hash 재계산) | **MEDIUM** — git commit hash 또는 외부 timestamp 없이 검출 어려움 | git append commit 또는 외부 timestamp 권고 |
| Genesis hash 위조 | **MEDIUM** — Genesis 정의 (`sha256("genesis:<scope>:<schema_version>")`) 결정적이지만 *원본 chain 전체 재구성 가능* | 외부 chain anchor (예: git tag) 권고 |

**§4.4 명시**: "git append commit 으로 변조 방지 (둘 중 하나 의무)". **git option 채택 시 chain 재계산 위조 차단** — git history 자체가 외부 anchor 역할.

**판정**: **변조 방지 정의 충실, git option 권고**. **격상 통합 합의 시점 git option 명시 권고**.

### 4.3 Memory scope 4 단계 권한 escalation 위험

**MVP scope (Global + Project)** + **보류 scope (Session + Team/Agent)**:

| Scope | Owner | Promotion 권한 | Escalation 위험 |
|-------|------|-----------|--------------|
| Global | 사용자 (manual) | (없음 — 최상위) | 0 |
| Project | 사용자 (manual) | Project → Global = manual only (T2) | LOW (manual 강제) |
| Session (보류) | Hermes 자동 + 사용자 review | Session → Project / Global = manual only (T2) | LOW — 단, *후속 진입 시* Hermes 자동 기록의 sensitive content 유출 위험 (G4 §2.3.2 "저장 금지 secret/T3 변경" 예고) |
| Team/Agent (보류) | 사용자 | Team → Global = manual only (T2) | LOW — 단, *후속 진입 시* per-agent 학습 결과의 다른 Agent 권한 변경 시도 차단 (G4 §2.4.2 "다른 Agent 의 *권한* 변경 금지") |

**5-layer Boundary 강제** (§2.5):
1. Filesystem 분리 (1차)
2. 환경변수 `CLAUDE_MEMORY_SCOPE` (2차)
3. Plugin scope 검증 (3차)
4. Promotion manual only — promotion hook 차단 (T2)
5. Filesystem ACL — Hermes container Memory write 권한 0

**판정**: **Escalation 위험 LOW** (모든 scope 가 *사용자 owner*). 단:
- **Gap-2**: Hermes 가 *Skill 후보 제안* 시 Memory write 권한 부재 + Skill `created_from` 가 *Hermes 작성 시 자동 audit* 명시 부재. G3 §2.2 #20 (합의 결과 silent override) 와 별도로, *Skill 본문이 Hermes-originated 인지 검증* 항목 명시 권고.

### 4.4 Skill 정의 자동 학습 경로의 정책 변경 유발 가능성

**G4 §5.2 4 금지 사항**:
1. Memory 가 policy 를 대체 — Constitution / ADR / SDD 가 Memory 로 옮겨가면 정책 변경
2. Skill 이 ADR / Constitution 우회 — Skill 본문이 자동 수정 / override
3. Session memory 가 global memory 로 자동 승격 — 임시 상태가 영구 정책으로 leak
4. Hermes 가 skill 을 자기 승인 — `proposed` → `approved/promoted` 자동 진행

**강제 메커니즘** (각 금지마다):
1. G3 §2.2 #9/#11 (T3) + Memory write 권한 0 (사용자만) ✅
2. G3 §2.2 #10/#11 (T3) + skill `allowed_actions` 에 `policy_write` 등 미포함 ✅
3. §2.5 promotion T2 강제 + filesystem ACL ✅
4. G3 §2.2 #16 (T2) + promotion hook 차단 + 사용자 명시 강제 ✅

**잔여 위험**:
- **Gap-4 (LOW)**: §5.2 #2 강제 메커니즘 "skill `allowed_actions` 에 `policy_write` 등 미포함" — `policy_write` 가 §3.2 #9 enum (`read/write/shell/network/db/git/docker`) 에 *포함되어 있지 않음*. 즉, 미래 *새로운 권한 enum 추가 시* `policy_write` 가 등록되면 §5.2 #2 차단 우회 가능. **권한 enum 자체의 변경이 T3 (정책 변경) 으로 분류되어야 함** — G4 §10 "schema_version 변경" 절차 (semver MINOR) 와 별도로, 권한 enum *추가* 는 T3 명시 권고.

---

## 5. 헌법 8조 위반 경로 P1~P8 충분성

### 5.1 누락된 위반 경로 (있을 경우)

**P1~P5 (8조)**:
- P1 DB INSERT 평문 secret → GP-1 ✅
- P2 로그/LLM 송신 평문 → GP-2 ✅
- P3 Credential 파일 권한 → GP-3 ✅
- P4 비밀값 하드코딩 → GP-3 ✅
- P5 외부 입력 미검증 → GP-4 ✅

**P6~P8 (5조 관용 — Provider Liquidity)**:
- P6 Hermes SDK 직접 import → GP-5 ✅
- P7 모델명/Provider 분기 → GP-5 ✅
- P8 Memory/Skill Hermes 종속 형식 → GP-6 + G4 ✅

**G2 §1.2.4 명시 *배제* 항목**:
- 헌법 1조 (SDD) / 2조 (TDD) 위반 — Layer 1~4 hook 영역
- 헌법 4조 (3+1 합의) 위반 — Layer 5 + 사용자
- 헌법 7조 (투명성) 위반 — Layer 0 + ADR
- 헌법 10조 (문서 일관성) — `docs/INDEX.md` + 의존 매트릭스
- ADR-011 §2.4 T3 위반 자체 — G3 영역

**Gap-1 (식별)**: 헌법 8조 #4 ("**보안 변경은 3+1 합의**") 의 *프로세스 강제* 가 P1~P8 enumeration 또는 GP 매트릭스 본문에 누락. 즉, 누군가 (사용자 또는 Hermes/Worker) 가 *redaction 정책 변경 / Tier-1 catalog 확장 / 새 Skill 권한 enum 추가* 를 시도할 때, **3+1 합의 절차 자체가 강제되어야 한다는 위반 경로** 가 명시 매핑 없음.
- 부분 흡수: G3 §2.2 #19 (redaction 정책 완화 T3) + #21 (Tier-1 catalog 자동 확장 T3) 가 *Hermes-originated* 차단으로는 흡수. 단 *사용자 명시 변경* 시점의 *3+1 합의 강제* 는 ADR-011 §2.4 T3 절차 본문 ("사용자도 ADR Amendment 절차") 답습 한정 — G2 본문 강제 메커니즘 표 미흡수.
- **권고**: G2 §11 영구 핵심 제약 표에 "**보안 변경 3+1 합의 강제 (헌법 8조 #4)**" 추가 row.

### 5.2 GP-1~GP-6 매핑 적정성

| GP | 매핑된 위반 경로 | 적정성 판정 |
|----|---------------|---------|
| GP-1 | P1 | ✅ 직접 매핑 (G1b PASS 흡수) |
| GP-2 | P2 | ✅ 직접 매핑 (Hermes native + P1 facade 보조) |
| GP-3 | P3 + P4 | ✅ 통합 매핑 (저장 + 코드 양 측면) |
| GP-4 | P5 | ✅ 직접 매핑 (Hermes/Worker 출력 = 외부 입력 확장) |
| GP-5 | P6 + P7 | ✅ 통합 매핑 (Hermes SDK + 모델명 분기) |
| GP-6 | P8 | ✅ 직접 매핑 (G4 와 공동) |

**판정**: 6 GP × 8 P 매핑 모두 적정. Gap-1 (헌법 8조 #4 프로세스 강제) 는 *별도 row* 권고이지, GP-1~GP-6 의 P 매핑 자체는 정합.

---

## 6. 메타 안전장치 견고성 (단일 실패점 검증)

### 6.1 G2 §9 + G3 §4 + G3 §5.5 의 상호 의존 vs 보강

| 메타 안전장치 | 책임 차원 | 구현 위치 |
|------------|--------|--------|
| **G2 §9** | 6 GP 자체의 무결성 보호 — *interface 선언* (filesystem read-only, Hermes-originated commit auto-reject, audit log, T3 변경 감지 hook) | G2 본문 §9.2 4 항목 |
| **G3 §4** | 합의 인프라 자기참조 차단 — *결정 유형 13건 매트릭스* + *Reviewer-only/외부 LLM 조건* + *Hermes 합의 결과 처리 권한 분리* | G3 §4.1~§4.6 |
| **G3 §5.5** (사실은 §1.3 + §5.3) | Evidence 없는 PASS 차단 — Hard Rule (i)~(iv) + JSONL ledger + 합의 보고서 commit | G3 §1.3 + §5.3 |

**상호 보강 vs 단일 실패점 판정**:

| 차원 | G2 §9 | G3 §4 | G3 §5.3 | 단일 실패점 여부 |
|------|------|------|--------|----------|
| 정책 파일 변경 차단 | filesystem read-only | (위임) | Hard Rule (i) Tools verify | **3중 보호** — 어느 layer 우회 시 다른 2개로 차단 |
| 합의 자기참조 차단 | (위임) | 13 매트릭스 + 외부 LLM | (위임) | **단일 layer (G3 §4)** — 격상 통합 합의 시점 외부 LLM 1+ 필수가 *외부 anchor* |
| Evidence 위조 차단 | (위임) | (위임) | hash chain + git commit + ledger entry 의무 | **단일 layer (G3 §5.3 + G4 §4.4)** — git option + hash chain 결합으로 강화 |
| Hermes-originated 변경 차단 | Hermes-originated commit auto-reject (interface) | §2.2 #20 (T3 매트릭스 항목) + §3.1 (silent drift) | (위임) | **2중 보호** |
| T3 변경 감지 | T3 변경 감지 hook (interface) | §2.2 #9/#11/#17/#19/#21 매트릭스 | (위임) | **2중 보호** |

**판정**:
- **상호 보강 강함** (정책 파일 / Hermes-originated / T3 변경 — 2~3중 보호)
- **합의 자기참조 차단** + **Evidence 위조 차단** 은 *단일 layer 영역* — *외부 anchor* (외부 LLM / git history) 결합으로 강화
- **단일 실패점 회피** 충족 — 단, *모두 동일 컨텍스트 자기 작성 산출* 이라는 메타 한계는 **G3 §4.4.2 외부 LLM 1+ 필수** 로 격상 합의 시점에 통제

### 6.2 본 통합 PASS 시점에 단일 실패점 잔여 위험

| 위험 | 통제 |
|-----|----|
| 모두 동일 클로드 컨텍스트 자기 작성 | **격상 통합 합의 시점 외부 LLM 1+ 필수** (G3 §4.4.2) — 본 *통합 PASS* 도 격상 통합 합의의 *전 단계* 이므로 **외부 LLM 1+ 강력 권장** |
| Hash chain 위조 (chain 재계산) | git append commit option 채택 권고 |
| `.git/config` 변경 (git author 위조) | filesystem read-only on `.git/` 명시 권고 (G3 §2.2 #11 확장) |
| 외부 LLM 의견 위조 (`docs/external-review/`) | 사용자 명시 commit 강제 + 외부 LLM 호출 audit 권고 |

---

## 7. Evidence 결정 5 운영 규칙 + Evidence 위조 차단

### 7.1 5 운영 규칙 (G3 §5.2)

| 규칙 | 명제 | 강제 메커니즘 |
|------|------|----------|
| #1 Agent proposes | Worker Agent 가 결과/PASS 제안 가능, *제안 자체는 PASS 아님* | §5.3 PASS 성립 요건 |
| #2 Hermes orchestrates | 격상 후 합의 진행 + Worker 호출 + Evidence 정리 *orchestrate* | §2.1 #1, #4, #5 + §5.3 (PASS 결정 불가) |
| #3 Tools verify | 모든 PASS 판정 = Tools 검증 통과 의무 | Layer 1~4 hook + CI |
| #4 Evidence decides | Evidence Ledger 기록 의무 + 변조 방지 | JSONL append-only + hash chain |
| #5 Human overrides | 사용자가 최종 격상/정책 변경 승인 | T2/T3 결정 권한 + override 자체도 audit |

### 7.2 PASS 성립 요건 (Hard Rule, §5.3)

**모든 PASS 판정 = (i) Tools 검증 + (ii) Evidence Ledger entry + (iii) (T2/T3) 사용자 명시 승인 + (iv) (해당 시) 합의 보고서 commit** — 모두 충족 의무.

**미충족 시**:
- (i) → Layer 1~4 hook 차단
- (ii) → ledger 검증 step 차단
- (iii) → T2/T3 영역 자동 reject + 사용자 alert
- (iv) → PASS verdict 본문에 cross-reference 부재로 §5.3 위반

**판정**: **운영 규칙 5 + Hard Rule 4 = 9 항목 강제** — 정의 충실. 단 hook / ledger 검증 step 실 코드 0건 (G3 §0.2 #7 명시).

### 7.3 Evidence 위조 경로 차단

| 위조 시나리오 | 차단 메커니즘 | 잔여 위험 |
|------------|----------|--------|
| ledger entry 본문 위조 (단일 entry) | hash chain — chain 끊어짐 검출 | 0 |
| ledger entry 누락 시도 (PASS verdict 만 작성) | §5.3 (ii) ledger 검증 step | LOW (실 hook 0건) |
| ledger entry 시간 역순 삽입 | append-only + ts ISO 8601 검증 | LOW |
| hash chain 전체 재계산 위조 | git append commit option | MEDIUM (git option 명시 권고) |
| Hermes-originated commit author=user 위조 | git author 검증 + audit log | MEDIUM (filesystem read-only on `.git/` 권고) |
| 합의 보고서 commit Hermes-originated 위조 | system-identity-prequel §3.3 #2 + G3 §4.5 (Hermes-originated commit auto-reject) | MEDIUM (실 git pre-commit hook 0건) |
| 외부 LLM 의견 위조 (`docs/external-review/` 자동 작성) | Hermes write 권한 명시 부재 (Gap-3) | **MEDIUM** (Gap-3 — 명시 강제 권고) |

**판정**: **위조 차단 정의 충실, 실 hook 0건 + 3 gap (git option / `.git/` read-only / `docs/external-review/` 보호)**. 격상 통합 합의 시점 흡수 권고.

---

## 8. 식별된 보안/거버넌스 결함 / Gap

### 8.1 종합 Gap 매트릭스

| # | Gap | 영역 | 심각도 | 권고 처리 |
|---|-----|----|------|--------|
| **Gap-1** | 헌법 8조 #4 ("보안 변경은 3+1 합의") *프로세스 강제* 가 P1~P8 또는 GP 매트릭스에 누락. ADR-011 §2.4 T3 답습으로는 *Hermes-originated 변경 차단* 흡수, 단 *사용자 명시 보안 변경* 시점 3+1 합의 강제 본문 부재. | G2 §1.2 + §11 | **MEDIUM** | G2 §11 영구 핵심 제약 표에 row 추가 (정식 채택 시점) |
| **Gap-2** | Skill `created_from` 필드 (G4 §3.1 #16) 가 *Hermes-originated 검증* 항목으로 직접 활용 명시 부재. G3 §2.2 #20 (합의 결과 silent override) 와 별도로, *Skill 본문 Hermes-originated 자동 audit* 강제 권고. | G4 §3 + G3 §2.2 | **LOW** | G4 §3 + G3 §3.1.2 cross-reference 추가 |
| **Gap-3** | `docs/external-review/` 디렉토리에 대한 Hermes write 권한 명시 부재. 외부 LLM 의견 위조 차단 메커니즘 부재. | G3 §2.2 + §4.4.2 | **MEDIUM** | G3 §2.2 #11 (Constitution 우회) 확장으로 `docs/external-review/` 추가 권고 |
| **Gap-4** | Skill `allowed_actions` enum (`read/write/shell/network/db/git/docker`) 자체의 변경 절차 명시 부재. G4 §10 "schema_version 변경" (semver MINOR) 와 별도로, **권한 enum *추가* 는 T3 분류** 명시 권고 (예: 미래 `policy_write` 등록 시 §5.2 #2 차단 우회 차단). | G4 §3.2 + §5.2 + §10 | **LOW** | G4 §10 변경 절차 표에 권한 enum 추가 row 권고 |
| **Gap-5** | Hash chain 변조 방지 — git append commit *option 명시 권고*. §4.4 "둘 중 하나 의무" 양자택일이지만, *chain 재계산 위조* 차단을 위한 git option 권장 명시 부재. | G4 §4.4 | **LOW-MEDIUM** | G4 §4.4 권고 본문 추가 (정식 채택 시점) |
| **Gap-6** | `.git/` filesystem read-only 강제 명시 부재. G3 §2.2 #11 (Constitution 우회) 가 `.git/config` (Hermes git author 위조 경로) 를 명시 cover 하지 않음. | G3 §2.2 | **MEDIUM** | G3 §2.2 #11 확장 — `.git/` (특히 `.git/config`, `.git/HEAD`) read-only on Hermes container 명시 권고 |
| **Gap-7** | 자기 작성 산출 검증 — G2/G3/G4 모두 동일 클로드 컨텍스트 작성. **격상 통합 합의 시점 외부 LLM 1+ 필수** (G3 §4.4.2) 가 본 *통합 PASS* 합의에도 적용되는지 명시 부재. *통합 PASS = 격상 합의 전 단계* 이므로 동일 메타 편향 위험. | 본 합의 형태 자체 | **MEDIUM** | 본 통합 PASS 합의 형태 결정 시 외부 LLM 1+ 강력 권장 (사용자 결정 영역) |

### 8.2 Gap 종합 평가

- **MEDIUM 4건** (Gap-1, Gap-3, Gap-6, Gap-7) — 격상 통합 합의 시점 흡수 또는 외부 LLM 의견으로 검증 권고
- **LOW-MEDIUM 1건** (Gap-5)
- **LOW 2건** (Gap-2, Gap-4)
- **HIGH 0건** — 본 통합 PASS 차단 사유 0건

**판정**: 식별된 7 Gap 모두 **본 통합 PASS 차단 사유는 아님** — DRAFT → 정식 채택 사이의 *후속 갱신 권고* 로 흡수 가능. 단 Gap-7 (외부 LLM 1+) 는 *합의 형태 결정* 영역으로 사용자 명시 결정 필요.

---

## 9. Agent B 판정

### 9.1 종합 판정

**APPROVE WITH CONDITIONS**

### 9.2 판정 근거

#### APPROVE 영역 (조건 없이 적격)

1. **Hermes ≠ root of trust 운영 구조 충실** — G3 §1~§5 권위 위계·22 권한·자기참조 차단·Evidence 결정 모두 ADR-011 §2.3 / system-identity-prequel §3 권위 직접 흡수, 우회 경로 명시적 차단
2. **ADR-011 §2.4 T1/T2/T3 일관성** — 본 통합 PASS 가 T3 위반 0건, T2 경로 모두 명시
3. **위반 경로 P1~P8 ↔ GP-1~GP-6 매핑 적정** — 6 GP × 8 P 모두 정합
4. **메타 안전장치 상호 보강** — G2 §9 + G3 §4 + G3 §5.3 정책/Hermes-originated/T3 차원 2~3중 보호, 단일 실패점 회피
5. **Provider Liquidity 4-way 보호** — GP-5 (depcruise) + GP-6 (마이그레이션) + G3 §6.4 (Hermes-originated lock-in) + G4 §3.5 (`provider_bindings` provider-neutral 강제) 결합

#### CONDITIONS (격상 통합 합의 또는 정식 채택 시점 흡수 권고)

1. **Gap-1**: G2 §11 영구 핵심 제약 표에 "보안 변경 3+1 합의 강제 (헌법 8조 #4)" row 추가
2. **Gap-3**: G3 §2.2 #11 확장 — `docs/external-review/` 디렉토리 Hermes write 권한 차단 명시
3. **Gap-6**: G3 §2.2 #11 확장 — `.git/` filesystem read-only 강제 명시 (특히 `.git/config`)
4. **Gap-7**: 본 통합 PASS 합의 형태 결정 시 **외부 LLM 1+ 강력 권장** — 격상 통합 합의 답습 (G3 §4.4.2) — *사용자 명시 결정 영역*

#### NOTES (LOW/LOW-MEDIUM Gap, 후속 권고)

5. Gap-2: G4 §3.1 #16 + G3 §3.1.2 cross-reference 추가 (Skill `created_from` Hermes-originated 검증 활용)
6. Gap-4: G4 §10 변경 절차 표에 권한 enum 추가 row (T3 분류)
7. Gap-5: G4 §4.4 git append commit option 권고 명시

### 9.3 본 판정의 *발화하지 않는* 것

- ❌ G2 PASS 자동 발화 (Reviewer 종합 판정 입력 한정)
- ❌ G3 PASS 자동 발화 (동일)
- ❌ G4 PASS 자동 발화 (동일)
- ❌ Hermes PMO 격상 권유
- ❌ P2 v3 정식 채택 자동 권유
- ❌ ADR 본문 자동 갱신 권유
- ❌ archive 자동 처리 권유

본 판정은 **Reviewer 의 종합 합의 보고서 입력** 한정. 최종 합의 형태 (옵션 1/2/3) + 외부 LLM 1+ 의견 형식 + 정식 채택 절차는 **사용자 명시 결정 + Reviewer 종합** 영역.

---

## 10. P2 v3 정식 채택 진입 가능 여부 판정 (보안 관점)

### 10.1 P2 v3 정식 채택 = 본 통합 PASS 의 *결과* 영역

P2 v3 정식 채택은 G2/G3/G4 PASS 합의 + ADR PR 묶음 + INDEX/CONTEXT 갱신 + system-identity-prequel/P2 v2 archive 처리의 *통합 산출*. 본 합의 자체가 트리거하는 것은 아니며, **별도 사용자 명시 결정** 영역.

### 10.2 보안 관점 진입 적격 여부

| 조건 | 충족 | 비고 |
|------|----|----|
| Provider Liquidity 4-way 보호 정의 | ✅ | GP-5 + GP-6 + G3 §6.4 + G4 §3.5 |
| Hermes ≠ root of trust 운영 구조 정의 | ✅ | G3 §1~§5 |
| 헌법 8조 위반 경로 P1~P5 매핑 + 강제 메커니즘 정의 | ✅ | GP-1~GP-4 |
| 자동 정책 변경 차단 (T3) 운영 정의 | ✅ | G3 §2.2 12 T3 항목 + G2 §9 메타 안전장치 |
| Evidence 위조 차단 정의 | ✅ (조건부) | §5.3 + §4.4, git option 권고 |
| 자기참조 차단 정의 | ✅ (조건부) | G3 §4, 외부 LLM 1+ 권고 |
| 식별된 7 Gap 흡수 경로 | ⏳ | 격상 통합 합의 또는 정식 채택 시점 흡수 |

**판정**: **보안 관점 P2 v3 정식 채택 진입 적격 — APPROVE WITH CONDITIONS** (위 9.2 4 CONDITIONS 흡수 후).

단, **본 판정은 P2 v3 정식 채택 *발화* 가 아니라 *진입 가능 여부* 판정** — 정식 채택 절차 자체는 **사용자 명시 결정 + Reviewer 종합 합의** 영역. 본 분석 시점에는:
- ✅ G2/G3/G4 DRAFT 모두 보안 측면 충실
- ✅ Gap 7건 모두 본 PASS 차단 사유 아님
- ⏳ 정식 채택 시점에 Gap 흡수 + 외부 LLM 의견 (Gap-7) + ADR PR 묶음

---

**작성일**: 2026-05-09
**Agent B 판정**: **APPROVE WITH CONDITIONS** (4 CONDITIONS — Gap-1/3/6/7)
**다음 단계 (Agent B 권고)**: Reviewer 가 Agent A / C 출력 종합 + 본 판정 + 7 Gap + 격상 통합 합의 시점 외부 LLM 1+ 필수 (G3 §4.4.2) 답습 — 본 통합 PASS 합의 형태 결정은 사용자 명시 결정 영역
**금지 (본 분석 영구 답습)**:
- ❌ Hermes PMO 격상 자동 권유
- ❌ P2 v3 정식 채택 자동 발화
- ❌ ADR 본문 자동 갱신 권유
- ❌ archive 자동 처리 권유
- ❌ 실 runtime code / migration script 작성
- ❌ 다른 Agent (A, C) 출력 참조
