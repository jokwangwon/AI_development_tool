# 외부 LLM 검토 의뢰 — G2 + G3 + G4 통합 게이트 PASS 승격 가능성 평가 (2026-05-07)

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 판정 가능하도록 자기충족적으로 작성되었습니다. 응답은 `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response{,-<vendor>}.md` 에 저장될 예정입니다.

---

## 0. 본 검토 의뢰의 *현재 목표* 와 *범위 밖* 항목

### 0.1 현재 목표

본 외부 검토의 *단일* 목적:

> **현재 DRAFT 상태인 G2 / G3 / G4 세 게이트를 동시에 정식 PASS 로 승격할 수 있는지 외부 시각에서 평가한다.**

다음 4 판정 옵션 중 하나를 *근거와 함께* 제시해 주십시오:

1. **APPROVE** — 3 게이트 모두 PASS 승격 가능
2. **APPROVE WITH CONDITIONS** — 일부 문구 / 조건 보강 후 PASS 승격 가능 (조건 명시 필수)
3. **PARTIAL** — 일부 게이트만 PASS 가능. 나머지는 DRAFT / PARTIAL 유지 (어떤 게이트 / 무엇 / 왜)
4. **BLOCK** — 중대 결함이 있어 PASS 승격 불가 (결함 명시 + 후속 조치 권고)

본 검토의 *메타* 목적은 자기참조 편향 통제입니다. G2/G3/G4 DRAFT 가 모두 같은 Claude 컨텍스트에서 작성되었고, DRAFT 검토 (Reviewer-only) 도 같은 컨텍스트에서 수행되었습니다. 외부 LLM 의견은 G3 §4 자기참조 차단 원칙 (§4 하단 답습) 의 *실현* 입니다.

### 0.2 본 검토의 *범위 밖* (외부 LLM 에게도 명시 부탁)

다음 결정은 본 검토 범위 밖이며 별도 후속 단계에서 처리됩니다:

- ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 PASS + 외부 LLM 1+ 필수 + 사용자 명시 결정 후 별도
- ❌ **P2 v3 정식 채택 선언** — G2/G3/G4 통합 PASS 후 별도 합의
- ❌ **ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신** — P2 v3 정식 채택 후 별도 PR
- ❌ **P2 v2 (`hermes-adoption-design.md`) archive 처리** — 정식 채택 시점에 별도 결정
- ❌ **`system-identity-prequel.md` archive 처리** — 정식 채택 시점에 별도 결정
- ❌ **실 runtime 코드 구현** (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 등)
- ❌ **실 migration script 구현** (`scripts/hermes-migration/*.py`)

본 검토는 *G2 / G3 / G4 게이트 승격 합의* 의 *외부 LLM 의견 입력* 한정입니다.

---

## 1. 시스템 정체성 (요약)

### 1.1 프로젝트 성격

- **이름**: AI Development Tool Template (AI 자동화 개발 도구 메타-템플릿)
- **사용자**: 1인 개발자
- **현 저장소 상태**: 실 코드 0줄, 약 50개 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 합의 보고서 + 가이드)
- **사용 방식**: 새 프로젝트 생성 → 본 템플릿 복사 → Phase 0 (자동화 검토 질문지) → Phase 1 (3+1 합의로 아이디어 / 스택 / 에셋 결정) → Phase 2-3 (SDD → TDD 코드)

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지 목표)
- **하네스 엔지니어링**: 7-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
- **3+1 멀티에이전트 합의**: Agent A (구현) + Agent B (안전성) + Agent C (대안) → Reviewer 종합

### 1.3 권위 위계 (영구 권위)

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

이 위계는 **ADR-011 §2.3** 에 영구 권위로 명시되어 있습니다. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상** 입니다.

### 1.4 메타-슬로건

> "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."
>
> Agent = Model + Harness. 모델은 추론을 제공하고, 하네스(문서/규칙/훅/검증)는 나머지 전부.

---

## 2. 현재 상태 (2026-05-07 시점)

| 항목 | 상태 | 비고 |
|----|----|---|
| **G1b** | ✅ PASS (2026-05-07) | DB-level fallback — SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog, R-2~R-7 6단계 evidence, R-6 actual run PASS, leak 0 |
| **Phase 1 acceptance** | ✅ PASS (2026-05-07) | Phase 1 진입 적격 단축 합의 |
| **P2 v3** (`hermes-adoption-design-v3.md`) | 🟡 DRAFT | 작성 완료, 정식 채택 합의 미진행 |
| **G2** (`governance-preconditions.md`) | 🟡 DRAFT + APPROVE AS DRAFT | Reviewer-only 단축 검토 APPROVE (2026-05-07) |
| **G3** (`hermes-not-root-of-trust-runtime.md`) | 🟡 DRAFT + APPROVE AS DRAFT | Reviewer-only 단축 검토 APPROVE (2026-05-07) |
| **G4** (`provider-agnostic-memory-skill-design.md`) | 🟡 DRAFT + APPROVE AS DRAFT | Reviewer-only 단축 검토 APPROVE (2026-05-07, 13/13 기준 PASS + 9/9 금지 0 위반) |

본 검토 대상: **G2 + G3 + G4 동시 정식 PASS 승격 가능 여부**. G1b 는 이미 PASS (본 검토 대상 외).

### 2.1 폐기 게이트 — G1a

| 게이트 | 상태 | 사유 |
|----|----|---|
| ~~G1a~~ | ❌ FAIL 확정 (폐기) | Hermes v0.12.0 에 `pre_record` hook 부재 (15종 hook 중 DB 기록 직전 가로채기 0건). ADR-011 §2.2 영구 권위로 폐기 확정. G1a (Hermes native redaction → DB) 의 *목적* 은 G1b 가 DB-level fallback 으로 흡수. |

---

## 3. G2 요약 — 6 거버넌스 사전조건

문서: `docs/architecture/governance-preconditions.md` (13 섹션, 작성일 2026-05-07).

### 3.1 핵심 출발점: 위반 경로 P1~P8

#### 헌법 8조 (보안) 위반 경로 5건

- **P1**: DB INSERT 평문 secret 누적 (Worker → SessionDB / Memory DB / Skill DB)
- **P2**: 로그 / LLM 송신 경로 평문 노출
- **P3**: Credential / OAuth 파일 권한 노출
- **P4**: 비밀값 하드코딩 (git commit / env default / docker-compose / Skill 정의)
- **P5**: 외부 입력 미검증 / 이스케이프 부재 (SQL / command / path injection)

#### Provider Liquidity (관용 헌법 5조) 위반 경로 3건

- **P6**: Hermes 자체 SDK 직접 import (P1 facade 우회)
- **P7**: 모델명 / Provider 분기 코드 (`if model == "claude": ...`)
- **P8**: Memory / Skill Hermes 종속 형식

> **명명 정정**: 본 프로젝트는 관용적으로 "헌법 5조 (Provider Liquidity)" 라 부르지만, 실제 헌법 5조는 *코드 품질 원칙*. Provider Liquidity 의 실제 권위 출처는 사용자 비협상 메모리 (`feedback_provider_liquidity.md`) + ADR-008 본문. G2 §1.1 에서 1회 명시 정정 후 관용 답습.

### 3.2 GP-1 ~ GP-6 매핑 + 강제 메커니즘

| GP | 명칭 | 위반 경로 | 핵심 강제 메커니즘 | 계산적/추론적/자동롤백 |
|----|----|----|----|----|
| **GP-1** | DB-level Secret Persistence 차단 | P1 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | 계산적 ✅ (G1b 흡수) |
| **GP-2** | Egress Redaction (로그 / LLM 송신) | P2 | Hermes native redaction (보조) + LLM facade redaction filter | 계산적 ✅ |
| **GP-3** | Credential / Secret Hygiene (저장 + 코드) | P3, P4 | docker secret + chmod 600 + entrypoint stat + inotify (런타임) / gitleaks + detect-secrets pre-commit (코드) | 계산적 ✅ |
| **GP-4** | 외부 입력 검증 (Hermes / Worker 출력 포함) | P5 | pydantic schema + regex sanitizer + escape (sql / shell) + Reviewer 보조 | 계산적 ✅ + 추론적 보조 |
| **GP-5** | Provider Adapter 강제 (코드 lock-in 차단) | P6, P7 | depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject | 계산적 ✅ |
| **GP-6** | Memory / Skill Migration 가능성 | P8 | JSONL append-only + 변환 스크립트 + 라운드트립 PoC | 계산적 ✅ + 추론적 보조 |

**합산**: 계산적 가능 6/6, 추론적 보조 4/6, 자동 롤백 6/6. 계산적 우선 — ADR-011 §2.1 수단/목적 분리 원칙 답습.

### 3.3 각 GP 의 Exit 기준 (a)~(e) 5조건

ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 패턴 답습:

- (a) 동등 이상의 보안 결과 (비교표)
- (b) 격리 환경 PoC 실증 (Docker)
- (c) ADR / SDD 권위 명시
- (d) 자동 회귀 검증 경로 확보 (CI step)
- (e) 합의 APPROVE (단축 또는 풀 3+1)

**현 충족 상태 (2026-05-07)**:

- GP-1: (a)~(e) 모두 G1b PASS evidence 로 *흡수*
- GP-2 ~ GP-6: (a)~(e) 미충족 — *형식 정의*까지만 본 G2 DRAFT 에 명시. 실 PoC + 합의는 *G2 PASS 합의 이후* 별도 산출 영역

### 3.4 G2 §9 메타 안전장치 (G3 위임)

본 6 GP 자체가 Hermes 에 의해 변경 / 우회되지 않도록 보호. G2 §9 는 *interface* 까지만, 본격 운영 구현은 **G3 위임**:

1. filesystem read-only on `governance-preconditions.md`
2. 본 문서 변경은 git commit 으로만 권위 인정 (Hermes-originated commit auto-reject)
3. 변경 audit log
4. T3 변경 감지 hook → 자동 reject + 사용자 alert

### 3.5 G3 / G4 인터페이스

- **G2 GP-5 ↔ G3 §6.4**: GP-5 = 모든 작성 주체의 코드 lock-in 차단 (depcruise) / G3 §6.4 = Hermes-originated 변경 차단. 두 보호가 결합 시 Provider Liquidity 코드 측면 완결.
- **G2 GP-6 ↔ G4 §4**: GP-6 = 마이그레이션 *가능성* (라운드트립 PoC) / G4 = 형식 *제공* (JSONL + hash chain + 변환 스크립트 사양). 둘 결합 시 Memory/Skill lock-in 차단.

---

## 4. G3 요약 — Hermes ≠ Root of Trust 운영 구현

문서: `docs/architecture/hermes-not-root-of-trust-runtime.md` (11 섹션, 작성일 2026-05-07).

ADR-011 §2.3 (영구 권위) 의 *운영 가능 메커니즘* 화.

### 4.1 §1 권위 위계 운영 — 충돌 해결 매트릭스

| 시나리오 | 처리 |
|---|---|
| Hermes 가 ADR / SDD 와 모순되는 결정 제안 | 자동 reject + 사용자 alert |
| Hermes 가 ADR / SDD 본문 자동 수정 시도 | filesystem read-only 차단 + audit log + 컨테이너 정지 |
| Hermes 가 새 ADR 작성 제안 | 제안 가능, 작성·승인은 사용자 명시 only |
| Worker 출력을 Hermes 가 *내부* 처럼 신뢰 (검증 우회) | GP-4 외부 입력 검증으로 차단 |
| 3+1 합의에서 Reviewer 결과 vs Hermes orchestration | Reviewer 결과 우선 (Hermes 는 *기록* 만, *승인* 불가) |
| Layer 1~6 hook 실패 시 Hermes 가 다음 단계 진행 | 자동 큐 차단 |

**Evidence 없는 PASS 금지** (Hard Rule): 모든 PASS = (i) Tools 검증 + (ii) Evidence Ledger entry + (iii) (T2/T3) 사용자 명시 승인 + (iv) (해당 시) 합의 보고서 commit 모두 충족 의무.

### 4.2 §2 Hermes 권한 22 항목 분류 (T1 / T2 / T3)

**허용 (T1 자동) 8건**:
1. 작업 분배 (오케스트레이션)
2. Memory 조회 (read-only)
3. Skill 후보 제안
4. 합의 실행 보조 (orchestrate)
5. Evidence 위치 정리
6. 다음 작업 제안
7. 자체 학습 (T1 한정)
8. Hermes 자체 redaction (로그 / 송신 한정)

**T2 사용자 승인 필수 2건**:
- #15 Memory write (Project → Global 자동 promotion)
- #16 Skill 자동 등록

**T3 절대 금지 12건**:
- #9 정책 자동 변경 (Constitution / ADR / SDD / Gate 정의)
- #10 ADR 자동 수정 / 승인
- #11 Constitution 우회
- #12 Harness Gate 실패 무시
- #13 G2 / G3 / G4 PASS 자동 선언
- #14 Hermes PMO 자기 격상
- #17 자체 학습 결과의 자동 정책 반영
- #18 Provider lock-in 유도
- #19 Secret redaction 정책 완화
- #20 합의 결과 silent override / 수정
- #21 Tier-1 / Tier-2 / Tier-3 canary catalog 자동 확장
- #22 사용자 override 자동 reject 시도

**강제 메커니즘 합산**: 계산적 22/22 (전부), 추론적 보조 6/22, 자동 롤백 14/22.

### 4.3 §3 3 위험 차단

- **Learning silent drift** (학습 → 정책 변경 silent leak): CI nightly diff + R-5 canary + R-6 actual run + 컨테이너 정지
- **Upstream silent breakage** (Hermes upstream 변경 silent 깨짐): version pin + PR PoC 재실행 + R-6 PASS branch protection + healthcheck
- **Skill permission escalation**: wrapper 권한 검증 + Docker cap_drop + 자동 비활성화 + 사용자 alert

### 4.4 §4 합의 인프라 순환 권위 해결 (자기참조 차단)

**문제**: Hermes 가 3+1 합의 *실행 인프라* 라면 Hermes 자기 격상 / Hermes 정책 변경 / G2/G3/G4 PASS 등 결정을 Hermes 단독 합의로 결정 → 자기참조 역설.

**원칙 4건**:
1. Hermes 관련 결정은 Hermes 단독 합의 금지
2. Reviewer-only 또는 외부 LLM 의견이 Hermes 관련 결정의 합의에 필수
3. 사용자 승인이 모든 T2 / T3 결정의 *최종* 권위
4. Hermes 는 합의 결과 *기록* 만 가능, *승인 주체* 가 될 수 없음

**합의 형태 매트릭스 발췌**:

| 결정 유형 | Hermes 단독? | 합의 형태 | 외부 LLM | 사용자 승인 |
|----|----|----|----|----|
| **G2 / G3 / G4 PASS** | orchestrate 만 | 단축 또는 풀 3+1 | 권장 (메타 편향) | ✅ |
| **Hermes PMO 격상** | ❌ 자기참조 | 풀 3+1 + **외부 LLM 1+ 필수** | ✅ 필수 | ✅ |
| **Hermes 정책 변경** | ❌ | 풀 3+1 + 외부 LLM 1+ 권장 | ✅ 권장 | ✅ + ADR Amendment |
| **Constitution / ADR 본문** | ❌ 작성 불가 | 풀 3+1 | 권장 | ✅ + ADR Amendment |

> **본 외부 검토 의뢰는 매트릭스 "G2 / G3 / G4 PASS" 행의 *외부 LLM 권장* 의 실현입니다.**

### 4.5 §5 Evidence 결정 5 운영 규칙

```
Agent proposes.    (제안)
Hermes orchestrates. (조율 — 격상 후)
Tools verify.      (검증 — 계산적 우선)
Evidence decides.  (결정 — 기록 없으면 PASS 미성립)
Human overrides.   (사람이 최종 방향)
```

PASS 성립 4 요건: (i) Tools + (ii) Evidence Ledger + (iii) 사용자 승인 (T2 / T3) + (iv) 합의 보고서 commit (해당 시).

### 4.6 §6 G2 인터페이스 + §7 G4 경계

- **§6**: GP-2 / GP-3 / GP-4 / GP-5 / GP-6 각각 G2 (메커니즘) ↔ G3 (권한·신뢰·무결성) 분리
- **§7**: G4 (형식 / schema) ↔ G3 (권한 / promotion / escalation) 분리

---

## 5. G4 요약 — Provider-agnostic Memory / Skill 형식

문서: `docs/architecture/provider-agnostic-memory-skill-design.md` (11 섹션, 작성일 2026-05-07, **옵션 B 통합 단일 문서**).

### 5.1 §2 Memory Scope 4 단계 + MVP

| Scope | MVP | 정체성 | Owner |
|---|---|---|---|
| **Global** | ✅ MVP | cross-project 보편 원칙 / 헌법-동급 제약 | 사용자 (manual approval) |
| **Project** | ✅ MVP | 프로젝트별 목표 / 결정 / 도메인 용어 | 사용자 (manual approval) |
| Session | ⏳ 후속 | 본 세션 작업 추적 (현 단계 `docs/sessions/SESSION_*.md` 로 충족) | 정량 트리거 (파생 프로젝트 ≥ 3건) |
| Team / Agent | ⏳ 후속 | Worker 별 강점 / 실패 패턴 | 정량 트리거 |

**Boundary 강제 (5 layer)**:
1. filesystem 분리 (`~/.claude/global/` vs `<project>/.claude/project/`)
2. 환경변수 (`CLAUDE_MEMORY_SCOPE=global|project`)
3. Hermes plugin scope 검증
4. manual promotion (T2 강제)
5. Hermes container Memory write 권한 0 (제안만, 실 write 는 사용자)

### 5.2 §3 Skill Schema — 17 필드

`skill.yaml`:

1. `id` (UUID v4 또는 slug)
2. `name`
3. `version` (semver)
4. `scope` (Memory scope 와 일치)
5. `owner` (provider-neutral identifier)
6. `description` (markdown)
7. `inputs` (JSON Schema)
8. `outputs` (JSON Schema)
9. `allowed_actions` (`read` / `write` / `shell` / `network` / `db` / `git` / `docker`)
10. `forbidden_actions` (disjoint from allowed)
11. `required_evidence` (`test_pass` / `lint` / `secret_scan` / `consensus` / `review`)
12. `required_tests`
13. `promotion_status` (`proposed` / `approved` / `promoted` / `archived` / `revoked`)
14. `rollback_triggers`
15. `provider_bindings` ⚠️ (lock-in 핵심 — *optional optimization* 한정, *required* / *exclusive* 금지, 최소 2 provider 재해석 가능)
16. `created_from` (출처 추적)
17. `last_verified_at`

### 5.3 §3.4 핵심 원칙: Skill 자동 생성 vs 자동 승격 분리

| 단계 | 권한 | 분류 |
|----|----|----|
| 후보 *추출* (반복 패턴 → `proposed`) | Hermes 자동 OK | T1 |
| `proposed` → `approved` | ❌ Hermes 자동 금지, **사용자 명시 강제** | T2 |
| `approved` → `promoted` | Tools 검증 + Evidence ledger 필수 + 사용자 명시 | T2 + Evidence |
| `promoted` → `revoked` | rollback_trigger 자동 | T3 자동 안전 |
| `*` → `archived` | 사용자 명시 강제 | T2 |

### 5.4 §3.5 `provider_bindings` 필드 — Provider Lock-in 차단 핵심

**원칙**: `provider_bindings` 에 provider 이름이 있어도 *provider 에 종속되지 않아야 한다*.

```yaml
# OK (provider-neutral 보장)
provider_bindings:
  claude:
    optional_optimization: true   # 선택 최적화 — 다른 provider 에서 fallback 가능
  openai:
    optional_optimization: true
  ollama:
    optional_optimization: false  # 미지원 — fallback 명시
```

```yaml
# 금지 (Provider lock-in 위반)
provider_bindings:
  claude:
    required: true                # ❌ Provider lock-in
    custom_endpoint: "anthropic://..."  # ❌ Provider 종속 endpoint
```

**검증 규칙**:
- 어떤 provider 도 *required* / *exclusive* 표시 금지
- 모든 binding 은 *optional optimization* 한정
- 최소 2 provider 로 재해석 가능
- Provider 종속 endpoint / SDK / 모델명 분기는 Skill 본문에 작성 금지 (G2 GP-5 + G3 §6.4 위임)

### 5.5 §4 JSONL Export Format + Hash Chain

```jsonl
{"type":"skill","scope":"project","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","content":{...},"evidence_refs":[...],"prev_hash":"<sha256>","hash":"<sha256>"}
```

**Hermes 의존 0 보장**:
- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증)
- `jq` + sha256 으로 표준 도구만으로 검증 가능
- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능

**Hash Chain**: `prev_hash` + `hash` (canonical JSON sha256) — append-only 변조 방지. Genesis hash = `sha256("genesis:<scope>:<schema_version>")`.

**Migration script 사양** (구현 본 초안 외): `hermes_to_claude.py`, `hermes_to_openai.py`, `hermes_to_ollama.py`, `import.py`. 라운드트립 검증 = `export → 변환 → import → re-export → 원본 hash 일치` (또는 의미 보존 + 손실 영역 ledger entry).

### 5.6 §5 Memory / Skill Boundary — 4 금지

1. **Memory 가 policy 를 대체** (Constitution / ADR 가 Memory 로 옮겨지면 권위 위계 우회)
2. **Skill 이 ADR / Constitution 우회** (Skill 본문이 ADR 자동 수정 시도)
3. **Session memory 가 global memory 로 자동 승격**
4. **Hermes 가 skill 을 자기 승인** (`proposed` → `approved` / `promoted` 자동 진행)

### 5.7 §6 G3 인터페이스 5 항목

- Skill Escalation 방지 (G4 = `allowed_actions` 필드, G3 = wrapper 검증)
- Hermes-originated Skill Auto-approval 금지
- Evidence 없는 promotion 차단
- Provider lock-in 차단
- Memory poisoning rollback

---

## 6. 3-Way 상호 의존성 (G2 ↔ G3 ↔ G4)

```
G2 GP-6 (마이그레이션 가능성) ─── G4 §4 (JSONL 형식 / 17 schema)
                              ╲
                               × ── G3 §6.5 / §7 (권한 / Promotion / Escalation)
                              ╱
G2 §9 (메타 안전장치 interface) ─ G3 §1 + §2 (자기참조 차단 운영 구현)
```

**핵심 의존**:
- G2 §9 메타 안전장치는 G3 운영 구현이 없으면 *interface 만* 으로 무력화 가능
- G4 JSONL hash chain + 17 schema 는 G3 권한 (Memory write 권한 0, Skill `proposed` → `approved` 사용자 명시) 없이는 무결성 보장 어려움
- G2 GP-5 / GP-6 (lock-in 코드 차단 + 마이그레이션 가능성) + G3 §6.4 (Hermes-originated 변경 차단) + G4 §3.5 + §4.3 (provider_bindings + JSONL Hermes 의존 0) — 모두 결합해야 Provider Liquidity 완결성

본 시스템 내부 평가에서는 *동시 PASS (옵션 3)* 가 단계별 PASS 보다 인터페이스 정합성에 유리하다는 견해가 있으나, 본 외부 검토는 그 견해 자체를 평가 대상으로 합니다.

---

## 7. P2 v3 — 정식 채택 *진입 후보* (본 검토 범위 밖)

`docs/architecture/hermes-adoption-design-v3.md` (DRAFT). G2/G3/G4 PASS 후 별도 합의로 정식 채택 검토.

본 외부 검토는 P2 v3 정식 *채택* 자체를 결정하지 않습니다. 본 검토 결과는:
- APPROVE / APPROVE WITH CONDITIONS → 시스템 내부에서 P2 v3 정식 채택 *합의 단계 진입* 검토 가능 (별도 후속)
- PARTIAL → 일부 게이트 PASS + P2 v3 진입 보류
- BLOCK → P2 v3 진입 불가

---

## 8. 메타 한계 — 자기참조 위험 (정직한 노출)

본 합의 자체에 다음 한계가 있습니다 (모두 명시):

1. **4 DRAFT 검토가 모두 같은 컨텍스트** (Claude 자기 작성 + Reviewer-only 단축 검토). 외부 검증 부재가 메타 편향 유발 가능.
2. **G3 §4.4.2 가 Hermes PMO 격상에 외부 LLM 1+ *필수*, 본 G2 / G3 / G4 PASS 에는 *권장*** 으로 명시. 본 검토 의뢰는 권장의 *실현* 입니다. *필수* 요건이 적용되는 Hermes PMO 격상은 본 검토 범위 밖.
3. **G2 §1.2 P1~P8 enumeration / §2.1 6 GP / G3 §2.2 22 권한 / G4 §3.1 17 schema 필드 / Memory scope 4 단계** 등 모두 *원안* — DRAFT 가 처음 표현. 외부 LLM 이 적정성 + 누락 + 과잉을 평가해 주십시오.
4. **계산적 vs 추론적 비율**: G2 6/6 계산적, G3 22/22 계산적, G4 강제 메커니즘 다수 계산적. "계산적 비중이 너무 높아서 실제 운영 시 추론적 보조가 더 필요한가?" 도 평가 대상.
5. **G4 DRAFT 검토에서 자기 발견된 LOW / VERY LOW 위험 5건** (P-1 ~ P-5):
   - P-1 LOW — §4.4 canonical JSON 정의에서 RFC 8785 (JCS) 직접 인용 부재 (간단 명시 한정)
   - P-2 LOW — §10 schema 진화 정책 표가 필드 *추가* 정책만 명시, *제거 / 이름 변경 / 타입 변경* 정책 부재
   - P-3 LOW — §4.5 외부 형식 import 시 schema_version declaration 절차 약함
   - P-4 VERY LOW — §6.4 "3-way 인터페이스" 명명이 실질 4 위치 (GP-5 + G3 §6.4 + G4 §3.5 + G4 §4.3) 이지만 3 게이트로 카운트, 명명 정정 후보
   - P-5 VERY LOW — §2.2.1 Global Memory `~/.claude/global/` 경로가 Claude Code 표준 디렉토리 구조 (`~/.claude/`) 와 충돌 가능성

이 5건은 본 시스템 내부 평가로는 *BLOCK 사유 아님* 으로 판정되었으나, 외부 LLM 이 *정식 PASS 합의 또는 P2 v3 정식 채택 전 흡수 의무 여부* 를 별도 판단해 주십시오.

---

## 9. 영구 핵심 제약 (변동 없음)

본 합의 결과와 무관하게 다음 5건은 영구 유지됩니다:

1. **Provider Liquidity** — 사용자 비협상 메모리 + ADR-008 본문
2. **Hermes ≠ root of trust** — ADR-011 §2.3 영구 권위
3. **메타포 강제 금지** — system-identity-prequel §7
4. **자동 정책 변경 금지 (T3)** — ADR-011 §2.4
5. **수단 / 목적 분리 원칙** — ADR-011 §2.1 (a)~(d) 4조건

---

## 10. 외부 LLM 에게 물어볼 7 질문 (필수)

다음 7 질문 각각에 *명확한 판정* + *근거* + *식별된 위험 또는 결함* 을 제시해 주십시오.

### Q1. G2 / G3 / G4 가 Hermes PMO 격상 전 게이트로 *충분*한가?

- 4 게이트 (G1b / G2 / G3 / G4) 구성이 Hermes PMO 격상 전 게이트로 *충분*한가?
- *누락된 게이트* 가 있는가? (예: 데이터 보존 / 외부 통신 / 사용자 인증 / 권한 위임 / 에러 처리 등의 영역에서 별도 게이트가 필요한가?)
- *과잉 게이트* 가 있는가? (4 게이트 중 일부가 통합되거나 축소될 수 있는가?)

### Q2. G2 / G3 / G4 를 *통합 PASS* 로 승격해도 되는가?

- 3 게이트를 동시에 PASS 로 승격하는 *옵션 3 (G2 + G3 + G4 통합 풀 3+1 합의)* 이 단계별 PASS (옵션 1, 2) 보다 *실제로* 안전하고 효율적인가?
- 통합 합의가 *각 게이트의 개별 결함* 을 가릴 위험은 없는가?
- 각 게이트의 entry / exit 기준 (a)~(e) 5조건이 *통합 PASS* 에 적합한가?

### Q3. 일부 게이트는 PASS 가 아니라 PARTIAL 로 유지해야 하는가?

- G2 / G3 / G4 중 *어느 게이트* 가 *PASS 가 아니라 PARTIAL* 로 유지되어야 하는가?
- 그 사유는?
- PARTIAL 상태에서 *어떤 조건 충족 시* 정식 PASS 로 승격 가능한가?

### Q4. Provider lock-in / Memory lock-in / Skill escalation 위험이 충분히 통제되는가?

- **Provider lock-in 위험**: G2 GP-5 (depcruise) + G3 §6.4 (Hermes-originated 변경 차단) + G4 §3.5 (`provider_bindings` 검증) + G4 §4.3 (JSONL Hermes 의존 0) 의 4 layer 보호가 *충분*한가?
- **Memory lock-in 위험**: G4 §4 JSONL + hash chain + migration script 사양 + GP-6 라운드트립 검증이 *충분*한가? canonical JSON 정의에서 RFC 8785 (JCS) 직접 인용 부재 (G4 검토 P-1) 가 lock-in 위험을 증가시키는가?
- **Skill escalation 위험**: G4 `allowed_actions` / `forbidden_actions` schema + G3 §3.3 wrapper 검증 + sandbox cap_drop + 자동 비활성화의 결합이 *충분*한가?

### Q5. Hermes ≠ root of trust 원칙이 *실제 운영 구조*로 충분히 구현되었는가?

- G3 §2.2 22 권한 항목 (T1 8 / T2 2 / T3 12) 이 *모호하지 않고* 구현 인계 가능한가?
- G3 §4 자기참조 차단 (4 원칙 + 합의 형태 매트릭스) 이 *실제로* 자기참조를 차단하는가? *우회 경로* 는?
- *Evidence 없는 PASS 금지* Hard Rule + 4 요건 (Tools + Evidence Ledger + 사용자 승인 + 합의 보고서) 이 *현실에서 운영 가능한 부담* 인가?
- G3 §5.5 (1인 동일 호스트 SPOF 면책 — signed commit SHOULD, Multi-host 전환 시 MUST 승격) 이 *단일 실패점* 위험을 충분히 명시 + 완화하는가?

### Q6. 1인 개발자 기준으로 거버넌스 오버헤드가 *과한가*?

- G2 6 GP × (a)~(e) 5조건 = 30 PoC + G3 22 권한 × 강제 메커니즘 + G4 17 schema 필드 + Memory scope 4 단계 + JSONL hash chain + migration script 사양 = *실제 구현 가능* 한 부담인가?
- "코드 0줄 + 50 마크다운" 규모 1인 개발자 메타-템플릿에서 이 거버넌스 구조가 *적정* 한가, *과도* 한가, *부족* 한가?
- *축소 후보* 또는 *통합 후보* 가 있는가? (예: G2 6 GP → 4 GP / G3 22 권한 → 12 권한 / G4 17 필드 → 12 필드)
- *추가 필요* 항목이 있는가?

### Q7. P2 v3 정식 채택 전에 *반드시 보강해야 할* 항목은 무엇인가?

- G2 / G3 / G4 PASS 후 P2 v3 정식 채택 합의 단계로 넘어가기 전 *반드시 보강* 해야 할 항목이 있는가?
- G4 검토 자기 발견 5 위험 (P-1 ~ P-5) 중 *정식 PASS 합의 또는 P2 v3 정식 채택 전 흡수 의무* 인 것은 어느 것인가? (각각의 처리 시점 권고)
- 본 의뢰서 §8 메타 한계 5건 중 *추가 외부 검증 필요* 항목은?
- *기타* 보강 항목 (본 의뢰서에서 명시 안 된 영역) 이 있는가?

---

## 11. 최종 판정 (필수)

위 Q1 ~ Q7 답변을 종합하여 다음 중 하나를 *명시* 해 주십시오:

- **APPROVE** — G2 / G3 / G4 모두 PASS 승격 가능
- **APPROVE WITH CONDITIONS** — 일부 문구 / 조건 보강 후 PASS 승격 가능 (조건 enumeration 필수)
- **PARTIAL** — 어느 게이트가 PASS, 어느 게이트가 PARTIAL, 어느 게이트가 BLOCK 인지 명시
- **BLOCK** — G2 / G3 / G4 PASS 승격 불가 (결함 enumeration + 후속 조치 권고 필수)

판정 근거는 Q1 ~ Q7 모두 반영해 주십시오.

본 외부 LLM 의견은 본 프로젝트의 Reviewer 가 Agent A (구현 / 운영) + Agent B (보안 / 거버넌스) + Agent C (대안 / 단순화) 의 3 내부 분석과 종합하여 최종 합의 보고서 (`docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md`) 에 반영합니다.

---

## 12. 외부 LLM 응답 형식 권장

응답은 다음 구조를 따라 주시면 본 시스템 흡수가 용이합니다 (필수는 아님):

```
## 0. 응답자 정체
- vendor / model 명시
- 본 의뢰서 외 참고 자료 사용 여부

## 1. Q1 — 4 게이트 충분성 평가
## 2. Q2 — 통합 PASS 적합성 평가
## 3. Q3 — PARTIAL 유지 필요 게이트 여부
## 4. Q4 — Provider / Memory lock-in / Skill escalation 위험 평가
## 5. Q5 — Hermes ≠ root of trust 운영 구현 평가
## 6. Q6 — 1인 개발자 거버넌스 오버헤드 평가
## 7. Q7 — P2 v3 정식 채택 전 보강 항목

## 8. G4 자기 발견 5 위험 (P-1 ~ P-5) 처리 시점 권고

## 9. 최종 판정 (APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK)
- 조건 / 결함 / 후속 조치 enumeration

## 10. 메타 노트
- 본 의뢰서에서 *결론 유도* 가 발견되었는가?
- 본 의뢰서에서 *누락된 정보* 가 있는가?
- 본 의뢰서가 *과도하게 길거나 짧은가*?
```

---

## 13. Blind 검토 강도 (의도)

본 의뢰서는 다음을 *의도적으로 미포함* 했습니다 — 외부 LLM 의 독립 판정을 위한 blind 강도 보장:

- ❌ G2 / G3 / G4 DRAFT 검토 (Reviewer-only) 의 *내부 판정 결과* (APPROVE AS DRAFT) 가 *외부 검토 결론 유도* 로 작용하지 않도록 분리 명시 — §2 표의 *DRAFT 적격성* 정보로 제한
- ❌ *옵션 3 (통합 풀 3+1) 권고 결론* — §6 3-way 상호 의존성에서 *견해 존재* 만 명시, 결론 유도 0건
- ❌ Agent A / B / C 의 *예상 결론* — 본 검토 후 별도 내부 합의로 종합 예정 (외부 의견은 *독립* 입력)
- ❌ 사용자가 선호하는 결론 (APPROVE / PARTIAL / BLOCK 중 어느 것) — 사용자는 *외부 판정에 따라* 후속 단계 결정

본 의뢰서 §3 ~ §5 의 G2 / G3 / G4 요약은 *각 DRAFT 의 원문 enumeration* 한정 — 결론 유도 표현 0건. §8 메타 한계 5건은 *정직한 자기 노출* 한정 — *외부 판정 결과 유도* 와 분리.

---

## 14. 외부 응답 회수 전까지 본 시스템 내부 금지 사항 (재명시)

외부 LLM 응답 회수 전까지 본 시스템은 다음을 *수행하지 않습니다*:

- ❌ G2 / G3 / G4 PASS 선언
- ❌ G2 + G3 + G4 통합 풀 3+1 최종 합의 발행
- ❌ P2 v3 정식 채택 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신
- ❌ P2 v2 (`hermes-adoption-design.md`) archive 처리
- ❌ `system-identity-prequel.md` archive 처리
- ❌ 실 runtime 코드 / 실 migration script 구현

본 외부 검토 의뢰는 위 결정의 *입력* 중 하나이며 *결정 자체* 가 아닙니다.

---

**검토 의뢰 작성일**: 2026-05-07
**의뢰 자료 버전**: v1
**자기충족성**: 본 문서만으로 평가 가능 (첨부 자료 없음)
**응답 저장 예정**: `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response{,-<vendor>}.md`
**다음 단계**: 사용자가 ChatGPT / Gemini / 기타 강력한 LLM 에 본 의뢰서 전체를 붙여넣고 응답 회수 → 다음 세션에서 응답 흡수 후 G2 + G3 + G4 통합 풀 3+1 합의 진행
