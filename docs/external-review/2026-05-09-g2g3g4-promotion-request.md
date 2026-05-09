# 외부 LLM 검토 의뢰 — G2 + G3 + G4 정식 PASS 승격 합의 (2026-05-09)

> **이 문서를 통째로 ChatGPT(GPT-5.x), Gemini, 또는 다른 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 판정 가능하도록 작성되었습니다. 응답은 본 세션 또는 `docs/external-review/2026-05-09-g2g3g4-promotion-response.md` 에 저장될 예정입니다.

---

## 0. 검토 의뢰자의 입장 + 본 검토의 목적

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트(주로 Claude Code)가 SDD+TDD로 자동 개발하도록 설계된 메타-템플릿**"을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 검토의 목적은 다음 *단일* 질문에 외부 시각으로 답하는 것입니다:

> **현재 DRAFT 상태인 G2 / G3 / G4 세 게이트를 동시에 정식 PASS 로 승격하고, P2 v3 정식 채택 합의 단계로 넘어가도 안전한가?**

다음 4 판정 옵션 중 하나를 *근거와 함께* 제시해 주십시오:

1. **APPROVE** — 3 게이트 모두 PASS 승격 가능. P2 v3 정식 채택 합의로 진행 가능.
2. **APPROVE WITH CONDITIONS** — 일부 문구/조건 보강 후 PASS 승격 가능. (조건 명시 필수)
3. **PARTIAL** — 일부 게이트만 PASS 가능. 나머지는 추가 작업 필요. (어떤 게이트가, 무엇이 부족한지 명시)
4. **BLOCK** — 중대 결함이 있어 P2 v3 정식 채택 합의로 진행 불가. (결함 명시 + 후속 조치 권고)

또한 본 검토의 *메타* 목적은 자기참조 편향 통제입니다 — Claude 가 자기 작성 산출 (G2/G3/G4 DRAFT 모두 같은 컨텍스트) 을 자기 검토하는 한계를 외부 LLM 의견으로 보강합니다.

본 합의에서 결정 *금지* 사항:
- ❌ Hermes PMO 격상 선언 (별도 결정)
- ❌ P2 v3 정식 채택 자동 선언 (본 합의는 *진입 가능 여부* 까지)
- ❌ ADR-008/009/010/011 본문 자동 갱신 (별도 PR)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리 (정식 채택 시점에)
- ❌ 실 runtime code / migration script 구현

---

## 1. 시스템 정체성 (요약)

### 1.1 프로젝트 성격

- **이름**: AI Development Tool Template (AI 자동화 개발 도구 메타-템플릿)
- **사용자**: 1인 개발자
- **저장소**: 코드 0줄, 약 50개 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 합의 보고서 + 가이드)
- **사용 방식**: 새 프로젝트 생성 → 본 템플릿 복사 → Phase 0 (자동화 검토 질문지) → Phase 1 (3+1 합의로 아이디어/스택/에셋 결정) → Phase 2-3 (SDD → TDD 코드)

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지)
- **하네스 엔지니어링**: 8-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
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

## 2. Hermes 도입 결정 (ADR-008) 과 4 게이트 (G1b/G2/G3/G4)

### 2.1 Hermes 란?

Hermes 는 "오케스트레이션 (작업 분배 / Worker Agent 호출 / 합의 진행 / Memory orchestration)" 책임을 맡길 후보 도구입니다 (현 v0.12.0). ADR-008 (Hermes 도입 Option B) 에서 6 차단조건 충족 시 도입 결정:

1. Hermes native redaction 이 LLM 송신/도구 출력 차단
2. JSONL export 표준 (lock-in 방지)
3. Hermes 의존성 자동 회귀 검증
4. Provider Adapter 강제 (모델/구독 교체 자유)
5. 격리 환경 (Docker)
6. Hermes ≠ root of trust

### 2.2 ADR-011 (수단/목적 분리 원칙) — 모법

R-1 사실 확인에서 Hermes v0.12.0 에 `pre_record` hook 이 부재 (15종 hook 중 DB 기록 직전 가로채기 0건) 확정 → **G1a (Hermes native redaction → DB) FAIL** 확정. 이에 ADR-011 발행:

#### 2.2.1 §2.1 수단/목적 분리 원칙

> 헌법 8조의 본질은 특정 hook 존재가 아니라 **DB 평문 저장 차단 결과**.

대체 수단 채택 4조건 **(a)~(d)**:
- (a) 동등 이상의 보안 결과 (명시 비교표)
- (b) 격리 환경 PoC 실증 (Docker)
- (c) ADR 권위 명시
- (d) 자동 회귀 검증 경로 확보 (CI)

후속 합의에서 **(e) 합의 APPROVE** 가 추가되어 본 G2/G3/G4 모든 § 의 Exit 5조건 패턴이 됨.

#### 2.2.2 §2.3 권위 위계 (Hermes ≠ root of trust)

5 운영 함의:
1. Hermes 출력은 Tools 로 검증된다
2. Hermes 자체 redaction 은 로그/송신 방어로만 신뢰
3. DB INSERT 경로는 Hermes 외부 (G1b SQLCipher trigger) 로 보호
4. Hermes 의존성 업그레이드 자동 회귀 검증 (R-6)
5. Hermes 학습 결과의 자동 정책 반영 금지 (T3)

#### 2.2.3 §2.4 자동 학습 vs 자동 정책 변경 분리 (T1/T2/T3)

- **T1 자동**: Worker 패턴 학습, 도구 사용 빈도 누적, 휴리스틱 (자동)
- **T2 사용자 승인 필수**: Skill/Memory promotion, 새 도구 등록, 합의 형태 결정
- **T3 절대 금지**: Constitution / ADR / Harness Gates 정의 자체의 변경 (단축 또는 풀 3+1 합의 + ADR Amendment)

### 2.3 4 게이트 정의 + 현 상태

| 게이트 | 정의 | 현 상태 (2026-05-09) |
|-------|------|---------------------|
| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기, ADR-011 §2.2 권위) |
| **G1b** | DB-level fallback (SQLCipher BEFORE INSERT trigger + REGEXP UDF) | ✅ **PASS** (2026-05-07, R-2~R-7 6단계 + R-6 actual run `25482284523` 24초 PASS, 42/42 catalog, leak 0) |
| **G2** | 6 거버넌스 사전조건 (P1~P8 위반 경로 매핑 + GP-1~GP-6 강제 메커니즘) | 🟡 **DRAFT 검토 APPROVE AS DRAFT** (Reviewer-only, 2026-05-07) |
| **G3** | "Hermes ≠ root of trust" 운영 구현 (22 권한 / 자기참조 차단 / Evidence 결정 5 운영 규칙) | 🟡 **DRAFT 검토 APPROVE AS DRAFT** (Reviewer-only, 2026-05-07) |
| **G4** | Provider-agnostic Memory/Skill 형식 (4 Memory scope / 17 Skill schema 필드 / JSONL hash chain) | 🟡 **DRAFT 검토 APPROVE AS DRAFT** (Reviewer-only, 2026-05-09) |

본 검토 대상: **G2 + G3 + G4 동시 정식 PASS 가능 여부**. (G1b 는 이미 PASS, 본 검토 대상 외.)

---

## 3. G2 — 6 거버넌스 사전조건 (요약)

`docs/architecture/governance-preconditions.md` (13 섹션, 작성일 2026-05-07).

### 3.1 핵심 출발점: 위반 경로 P1~P8

#### 헌법 8조 (보안) 위반 경로 5건
- **P1**: DB INSERT 평문 secret 누적 (Worker → SessionDB / Memory DB / Skill DB)
- **P2**: 로그/LLM 송신 경로 평문 노출
- **P3**: Credential / OAuth 파일 권한 노출
- **P4**: 비밀값 하드코딩 (git commit / env default / docker-compose / Skill 정의)
- **P5**: 외부 입력 미검증/이스케이프 (SQL/command/path injection)

#### Provider Liquidity (관용 헌법 5조) 위반 경로 3건
- **P6**: Hermes 자체 SDK 직접 import (P1 facade 우회)
- **P7**: 모델명 / Provider 분기 코드 (`if model == "claude": ...`)
- **P8**: Memory / Skill Hermes 종속 형식

> **명명 정정**: 프로젝트는 관용적으로 "헌법 5조 (Provider Liquidity)" 라 부르지만, 실제 헌법 5조는 "코드 품질 원칙". Provider Liquidity 의 실제 권위 출처는 사용자 비협상 메모리 (`feedback_provider_liquidity.md`) + ADR-008 본문. G2 §1.1 에서 1회 명시 정정 후 관용 답습.

### 3.2 GP-1 ~ GP-6 매핑 + 강제 메커니즘

| GP | 명칭 | 위반 경로 | 핵심 강제 메커니즘 | 계산적/추론적/자동롤백 |
|----|------|---------|----------------|--------------|
| **GP-1** | DB-level Secret Persistence 차단 | P1 | SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog | 계산적 ✅ (G1b 흡수) |
| **GP-2** | Egress Redaction (로그/LLM 송신) | P2 | Hermes native redaction (보조) + LLM facade redaction filter | 계산적 ✅ |
| **GP-3** | Credential / Secret Hygiene (저장+코드) | P3, P4 | docker secret + chmod 600 + entrypoint stat + inotify (런타임) / gitleaks + detect-secrets pre-commit (코드) | 계산적 ✅ |
| **GP-4** | 외부 입력 검증 (Hermes/Worker 출력 포함) | P5 | pydantic schema + regex sanitizer + escape (sql/shell) + Reviewer 보조 | 계산적 ✅ + 추론적 보조 |
| **GP-5** | Provider Adapter 강제 (코드 lock-in 차단) | P6, P7 | depcruise 룰 + P1 facade 단일 진입점 + PR auto-reject | 계산적 ✅ |
| **GP-6** | Memory / Skill Migration 가능성 | P8 | JSONL append-only + 변환 스크립트 + 라운드트립 PoC (R2-5 답습) | 계산적 ✅ + 추론적 보조 |

**합산**: 계산적 가능 6/6, 추론적 보조 4/6, 자동 롤백 6/6. 계산적 우선 — ADR-011 §2.1 수단/목적 분리 원칙 답습.

### 3.3 각 GP 의 Exit 기준 (a)~(e) 5조건

ADR-011 §2.1 (a)~(d) + 합의 APPROVE (e) 패턴 답습:
- (a) 동등 이상의 보안 결과 (비교표)
- (b) 격리 환경 PoC 실증 (Docker)
- (c) ADR / SDD 권위 명시
- (d) 자동 회귀 검증 경로 확보 (CI step)
- (e) 합의 APPROVE (단축 또는 풀 3+1)

**현 충족 상태**:
- GP-1: (a)~(e) 모두 G1b PASS evidence 로 *흡수* (R-4, R-2 Docker, ADR-011 §2.1, R-6 actual run, R-7 SOP §7.3 단축 합의)
- GP-2 ~ GP-6: (a)~(e) 미충족 — PoC + 합의 필요

### 3.4 §9 메타 안전장치 (G3 위임)

본 6 GP 자체가 Hermes 에 의해 변경/우회되지 않도록 보호. G2 §9 는 *interface* 까지만, 본격 운영 구현은 **G3 위임**:
1. filesystem read-only on `governance-preconditions.md`
2. 본 문서 변경은 git commit 으로만 권위 인정 (Hermes-originated commit auto-reject)
3. 변경 audit log
4. T3 변경 감지 hook → 자동 reject + 사용자 alert

### 3.5 G2 통합 PASS 합의 형태 (사용자 결정 영역)

옵션 1: GP-1 ~ GP-6 각각 별도 단축 합의 → G2 통합 단축 합의 1건
옵션 2: GP-1 ~ GP-6 통합 풀 3+1 합의 1건
**옵션 3 (권고 후보)**: GP-1 ~ GP-6 + G3 + G4 통합 풀 3+1 합의 1건 (PR 묶음, 외부 LLM 1+ 권장) ← *본 검토가 이 옵션 3 의 외부 LLM 의견*

---

## 4. G3 — Hermes ≠ Root of Trust 운영 구현 (요약)

`docs/architecture/hermes-not-root-of-trust-runtime.md` (11 섹션, 작성일 2026-05-07).

ADR-011 §2.3 (영구 권위) 의 *운영 가능 메커니즘* 화.

### 4.1 §1 권위 위계 운영 — 충돌 해결 매트릭스

| 시나리오 | 처리 |
|---------|-----|
| Hermes 가 ADR/SDD 와 모순되는 결정 제안 | 자동 reject + 사용자 alert |
| Hermes 가 ADR/SDD 본문 자동 수정 시도 | filesystem read-only 차단 + audit log + 컨테이너 정지 |
| Hermes 가 새 ADR 작성 제안 | 제안 가능, 작성·승인은 사용자 명시 only |
| Worker 출력을 Hermes 가 *내부* 처럼 신뢰 (검증 우회) | GP-4 외부 입력 검증으로 차단 |
| 3+1 합의에서 Reviewer 결과 vs Hermes orchestration | Reviewer 결과 우선 (Hermes 는 *기록* 만, *승인* 불가) |
| Layer 1~6 hook 실패 시 Hermes 가 다음 단계 진행 | 자동 큐 차단 |

**Evidence 없는 PASS 금지** (Hard Rule): 모든 PASS 는 (i) Tools 검증 + (ii) Evidence Ledger entry + (iii) (T2/T3) 사용자 명시 승인 + (iv) (해당 시) 합의 보고서 commit 모두 충족 의무.

### 4.2 §2 Hermes 권한 22 항목

#### 허용 (T1 자동) 8건
1. 작업 분배 (오케스트레이션)
2. Memory 조회 (read-only)
3. Skill 후보 제안
4. 합의 실행 보조 (orchestrate)
5. Evidence 위치 정리
6. 다음 작업 제안
7. 자체 학습 (T1 한정)
8. Hermes 자체 redaction (로그/송신 한정)

#### T2 사용자 승인 필수 2건
- #15 Memory write (Project → Global 자동 promotion)
- #16 Skill 자동 등록

#### T3 절대 금지 12건
- #9 정책 자동 변경 (Constitution / ADR / SDD / Gate 정의)
- #10 ADR 자동 수정/승인
- #11 Constitution 우회
- #12 Harness Gate 실패 무시
- #13 G2/G3/G4 PASS 자동 선언
- #14 Hermes PMO 자기 격상
- #17 자체 학습 결과의 자동 정책 반영
- #18 Provider lock-in 유도
- #19 Secret redaction 정책 완화
- #20 합의 결과 silent override / 수정
- #21 Tier-1/Tier-2/Tier-3 canary catalog 자동 확장
- #22 사용자 override 자동 reject 시도

**강제 메커니즘 합산**: 계산적 22/22 (전부), 추론적 보조 6/22, 자동 롤백 14/22.

### 4.3 §3 3 위험 차단

- **Learning silent drift** (학습 → 정책 변경 silent leak): CI nightly diff + R-5 canary + R-6 actual run + 컨테이너 정지
- **Upstream silent breakage** (Hermes upstream 변경 silent 깨짐): version pin + PR PoC 재실행 + R-6 PASS branch protection + healthcheck
- **Skill permission escalation**: wrapper 권한 검증 + Docker cap_drop + 자동 비활성화 + 사용자 alert

### 4.4 §4 합의 인프라 순환 권위 해결 (자기참조 차단)

**문제**: Hermes 가 3+1 합의 *실행 인프라* 라면 Hermes 자기 격상 / Hermes 정책 변경 / G2/G3/G4 PASS 등 결정을 Hermes 단독 합의로 결정 → 자기참조 역설.

**원칙**:
1. Hermes 관련 결정은 Hermes 단독 합의 금지
2. Reviewer-only 또는 외부 LLM 의견이 Hermes 관련 결정의 합의에 필수
3. 사용자 승인이 모든 T2/T3 결정의 *최종* 권위
4. Hermes 는 합의 결과 *기록* 만 가능, *승인 주체*가 될 수 없음

**합의 형태 매트릭스 발췌**:

| 결정 유형 | Hermes 단독? | 합의 형태 | 외부 LLM | 사용자 승인 |
|---------|-----------|--------|---------|---------|
| **G2/G3/G4 PASS** | orchestrate 만 | 단축 또는 풀 3+1 | 권장 (메타 편향) | ✅ |
| **Hermes PMO 격상** | ❌ 자기참조 | 풀 3+1 + **외부 LLM 1+ 필수** | ✅ 필수 | ✅ |
| **Hermes 정책 변경** | ❌ | 풀 3+1 + 외부 LLM 1+ 권장 | ✅ 권장 | ✅ + ADR Amendment |
| **Constitution / ADR 본문** | ❌ 작성 불가 | 풀 3+1 | 권장 | ✅ + ADR Amendment |

### 4.5 §5 Evidence 결정 5 운영 규칙

```
Agent proposes.    (제안)
Hermes orchestrates. (조율 — 격상 후)
Tools verify.      (검증 — 계산적 우선)
Evidence decides.  (결정 — 기록 없으면 PASS 미성립)
Human overrides.   (사람이 최종 방향)
```

PASS 성립 4 요건: (i) Tools + (ii) Evidence Ledger + (iii) 사용자 승인 (T2/T3) + (iv) 합의 보고서 commit (해당 시).

### 4.6 §6 G2 인터페이스 + §7 G4 경계

**§6**: GP-2 / GP-3 / GP-4 / GP-5 / GP-6 각각 G2 (메커니즘) ↔ G3 (권한·신뢰·무결성) 분리.
**§7**: G4 (형식 / schema) ↔ G3 (권한 / promotion / escalation) 분리.

---

## 5. G4 — Provider-agnostic Memory / Skill 형식 (요약)

`docs/architecture/provider-agnostic-memory-skill-design.md` (11 섹션, 작성일 2026-05-07, **옵션 B 통합 단일 문서**).

### 5.1 §2 Memory Scope 4 단계 + MVP

| Scope | MVP | 정체성 | Owner |
|-------|----|------|------|
| **Global** | ✅ MVP | cross-project 보편 원칙 / 헌법-동급 제약 | 사용자 (manual approval) |
| **Project** | ✅ MVP | 프로젝트별 목표 / 결정 / 도메인 용어 | 사용자 (manual approval) |
| Session | ⏳ 후속 | 본 세션 작업 추적 | 정량 트리거 (파생 ≥ 3건) |
| Team/Agent | ⏳ 후속 | Worker별 강점/실패 패턴 | 정량 트리거 |

**Boundary 강제**: filesystem 분리 (`~/.claude/global/` vs `<project>/.claude/project/`) + 환경변수 (`CLAUDE_MEMORY_SCOPE`) + Hermes plugin scope 검증 + manual promotion + Hermes container Memory write 권한 0.

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
9. `allowed_actions` (`read`/`write`/`shell`/`network`/`db`/`git`/`docker`)
10. `forbidden_actions` (disjoint from allowed)
11. `required_evidence` (`test_pass`/`lint`/`secret_scan`/`consensus`/`review`)
12. `required_tests`
13. `promotion_status` (`proposed`/`approved`/`promoted`/`archived`/`revoked`)
14. `rollback_triggers`
15. `provider_bindings` ⚠️ (lock-in 핵심 — `optional optimization` 한정, `required`/`exclusive` 금지, 최소 2 provider 재해석 가능)
16. `created_from` (출처 추적)
17. `last_verified_at`

### 5.3 §3.4 핵심 원칙: Skill 자동 생성 vs 자동 승격 분리

| 단계 | 권한 | 분류 |
|------|-----|------|
| 후보 *추출* (반복 패턴 → `proposed`) | Hermes 자동 OK | T1 |
| `proposed` → `approved` | ❌ Hermes 자동 금지, **사용자 명시 강제** | T2 |
| `approved` → `promoted` | Tools 검증 + Evidence ledger 필수 + 사용자 명시 | T2 + Evidence |
| `promoted` → `revoked` | rollback_trigger 자동 | T3 자동 안전 |
| `*` → `archived` | 사용자 명시 강제 | T2 |

### 5.4 §4 JSONL Export Format + Hash Chain

```jsonl
{"type":"skill","scope":"project","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","content":{...},"evidence_refs":[...],"prev_hash":"<sha256>","hash":"<sha256>"}
```

**Hermes 의존 0 보장**:
- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증)
- `jq` + sha256 으로 표준 도구만으로 검증 가능
- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능

**Hash Chain**: `prev_hash` + `hash` (canonical JSON sha256) — append-only 변조 방지. Genesis hash = `sha256("genesis:<scope>:<schema_version>")`.

**Migration script 사양** (구현 본 초안 외): `hermes_to_claude.py`, `hermes_to_openai.py`, `hermes_to_ollama.py`, `import.py`. 라운드트립 검증 = `export → 변환 → import → re-export → 원본 hash 일치` (또는 의미 보존 + 손실 영역 ledger entry).

### 5.5 §5 Memory / Skill Boundary — 4 금지

1. **Memory 가 policy 를 대체** (Constitution / ADR 가 Memory 로 옮겨지면 권위 위계 우회)
2. **Skill 이 ADR / Constitution 우회** (Skill 본문이 ADR 자동 수정 시도)
3. **Session memory 가 global memory 로 자동 승격**
4. **Hermes 가 skill 을 자기 승인** (`proposed` → `approved`/`promoted` 자동 진행)

### 5.6 §6 G3 인터페이스 5 항목

- Skill Escalation 방지 (G4 = `allowed_actions` 필드, G3 = wrapper 검증)
- Hermes-originated Skill Auto-approval 금지
- Evidence 없는 promotion 차단
- Provider lock-in 차단
- Memory poisoning rollback

---

## 6. P2 v3 (Hermes Adoption v3) — 정식 채택 진입 후보

`docs/architecture/hermes-adoption-design-v3.md` (12 섹션, DRAFT). G2/G3/G4 PASS 후 별도 합의로 정식 채택 검토.

### 6.1 P2 v3 의 위치

P2 v2 §2.1.3 가정 ("외부 pre-record hook 공식 지원") 폐기 → R-2 ~ R-7 흡수 → Hermes PMO 구조 사전 정의 + G2/G3/G4 entry/exit 명세. **P2 v3 정식 채택 = ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 + P2 v2 + system-identity-prequel archive 검토 진입 의미** (실 archive 는 별도 결정).

### 6.2 P2 v3 채택의 *진입 가능 여부* 만 본 합의 대상

본 합의는 P2 v3 정식 *채택* 자체를 결정하지 않습니다. 본 합의 결과는:
- APPROVE / APPROVE WITH CONDITIONS → P2 v3 정식 채택 *합의 단계 진입 가능*
- PARTIAL → 일부 게이트 PASS + P2 v3 진입 보류
- BLOCK → P2 v3 진입 불가

---

## 7. G2 / G3 / G4 의 상호 의존성 (3-way)

```
G2 GP-6 (마이그레이션 가능성) ─── G4 (JSONL 형식 / 17 schema 필드)
                              ╲
                               × ── G3 §6.5 / §7 (권한 / Promotion / Escalation)
                              ╱
G2 §9 (메타 안전장치 interface) ─ G3 §1 + §2 (자기참조 차단 운영 구현)
```

**핵심 의존**:
- G2 §9 메타 안전장치는 G3 운영 구현이 없으면 *interface 만* 으로 무력화 가능
- G4 JSONL hash chain + 17 schema 는 G3 권한 (Memory write 권한 0, Skill `proposed`→`approved` 사용자 명시) 없이는 무결성 보장 어려움
- G2 GP-5 / GP-6 = lock-in 코드 차단 + 마이그레이션 가능성, G3 §6.4 = Hermes-originated 변경 차단 — 둘 다 있어야 Provider Liquidity 완결성

→ **3 게이트 단계별 PASS 보다 묶음 PASS 가 인터페이스 정합성에 유리** 라는 것이 G2 §10.2 / G3 §8.2 / G4 §8.3 / P2 v3 §9.2 모두 옵션 3 (3 게이트 통합 풀 3+1 + 외부 LLM 1+) 권고 근거.

---

## 8. 메타 한계 — 자기참조 위험

본 합의 자체에 다음 한계가 있습니다 (모두 정직하게 노출):

1. **4 DRAFT 검토가 모두 같은 컨텍스트** (Claude 자기 작성 + Reviewer-only 단축 검토). 외부 검증 부재가 메타 편향 유발 가능.
2. **G3 §4.4.2 가 Hermes PMO 격상에 외부 LLM 1+ *필수*, 본 G2/G3/G4 PASS 에는 *권장*** 으로 명시. 본 검토는 권장의 *실현* 입니다.
3. **G2 §1.2 P1~P8 enumeration / §2.1 6 GP / G3 §2.2 22 권한 / G4 §3.1 17 schema 필드** 등 모두 *원안* — 합의 보고서 자체에 명시되지 않은 enumeration 을 DRAFT 가 처음 표현. 외부 LLM 이 적정성을 평가해 주십시오.
4. **계산적 vs 추론적 비율**: G2 6/6 계산적, G3 22/22 계산적, G4 강제 메커니즘 다수 계산적. "계산적 비중이 너무 높아서 실제 운영 시 추론적 보조가 더 필요한가?" 도 평가 대상.

---

## 9. 영구 핵심 제약 (변동 없음)

1. **Provider Liquidity** — 헌법 5조 (관용) 비협상, 사용자 메모리 명시
2. **Hermes ≠ root of trust** — ADR-011 §2.3 영구 권위
3. **메타포 강제 금지** — system-identity-prequel §7
4. **자동 정책 변경 금지 (T3)** — ADR-011 §2.4
5. **수단/목적 분리 원칙** — ADR-011 §2.1 (a)~(d) 4조건

본 5건은 본 합의 결과와 무관하게 영구 유지.

---

## 10. 평가 요청 사항 (필수)

다음 4 차원으로 평가해 주십시오. 각 차원에 *명확한 판정* + *근거* + *식별된 위험 또는 결함* 을 제시해 주십시오.

### 10.1 차원 1 — 운영 가능성 (Operability)

- G2 6 GP / G3 22 권한 / G4 17 schema 필드가 *모호하지 않고* 구현 인계 가능한가?
- 1인 개발자 메타-템플릿 스케일에서 운영 가능한 부담인가, 과도한가?
- Entry / Exit 기준 (a)~(e) 5조건이 *검증 가능* (verifiable) 한가?

### 10.2 차원 2 — 보안 / 거버넌스 견고성

- G3 §4 자기참조 차단이 *실제로* 자기참조를 차단하는가? 우회 경로는?
- Provider Liquidity 가 G4 17 schema (특히 #15 `provider_bindings`) + JSONL 형식으로 충분히 보장되는가?
- §9 메타 안전장치 (G2) + G3 §4 + G3 §5.5 의 상호 의존이 *단일 실패점* 이 되지는 않는가?
- 헌법 8조 위반 경로 P1~P8 가 *충분한가* — 빠진 경로는?
- Memory/Skill lock-in 또는 escalation 우회 경로는?

### 10.3 차원 3 — 단순화 / 대안

- 동시 PASS (옵션 3) 가 단계별 PASS (옵션 1, 2) 보다 *실제로* 안전하고 효율적인가?
- 부분 PASS 시나리오 (어떤 게이트만 PASS, 어떤 게이트 조건부) 가 더 적합한가?
- G2 6 GP → 4 GP 통합 / G3 22 권한 → 12 권한 축소 / G4 17 필드 → 12 필드 축소 등 *단순화 후보* 가 있는가?
- P2 v3 채택 전 *누락된 영역* (예: ADR-009 자체 Adapter v2.0 진입조건, P1 v2 facade MVP 의존성) 이 있는가?

### 10.4 차원 4 — 메타 편향 / 자기참조 위험

- 본 합의가 자기참조 한계를 *충분히 노출* 하는가, 아니면 숨기는가?
- 외부 LLM 1+ 만으로 자기참조 위험이 충분히 통제되는가?
- 본 합의 후 P2 v3 정식 채택 전에 추가 외부 검증 (예: 다른 LLM 이나 다른 사용자) 이 필요한가?

### 10.5 최종 판정

다음 중 하나를 *명시* 해 주십시오:
- **APPROVE**
- **APPROVE WITH CONDITIONS** (조건 enumeration)
- **PARTIAL** (어느 게이트 PASS, 어느 게이트 조건부, 어느 게이트 BLOCK)
- **BLOCK** (결함 enumeration + 후속 조치 권고)

판정 근거는 §10.1 ~ §10.4 4 차원 모두 반영해 주십시오. 본 외부 LLM 의견은 본 프로젝트의 Reviewer 가 Agent A (구현/운영) + Agent B (보안/거버넌스) + Agent C (대안/단순화) 의 3 내부 분석과 종합하여 최종 합의 보고서에 반영합니다.

---

**검토 의뢰 작성일**: 2026-05-09
**의뢰 자료 버전**: v1
**자기충족성**: 본 문서만으로 평가 가능 (첨부 자료 없음)
**응답 저장 예정**: `docs/external-review/2026-05-09-g2g3g4-promotion-response.md` 또는 본 세션 직접 붙여넣기
