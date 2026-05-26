# 외부 LLM 검토 의뢰 — PR-2: Evidence Ledger 보호 강화 (ADR-012 신규 + G4 §4.4/§4.6 hash chain 사양 보강)

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 판정 가능하도록 작성되었습니다. 본 의뢰 자료에는 *내부 Agent A / B / C 분석 결과는 포함되지 않습니다* (의도적 편향 통제 — 외부 LLM 의 독립 판단 확보 목적). 응답은 본 세션 또는 `docs/external-review/2026-05-XX-pr2-evidence-ledger-response.md` 에 저장될 예정입니다.

---

## 0. 검토 의뢰자의 입장 + 본 검토의 목적

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트 (주로 Claude Code) 가 SDD + TDD 로 자동 개발하도록 설계된 메타-템플릿**" 을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 검토의 목적은 다음 *단일* 질문에 외부 시각으로 답하는 것입니다:

> **PR-2 (ADR-012 Evidence Ledger 보호 강화 신규 발행 + G4 §4.4 / §4.6 hash chain 사양 보강) 의 *설계* 가 안전하고, 견고하며, 1인 개발자 메타-템플릿 스케일에 적정한가? 본 PR-2 가 P2 v3 정식 채택 합의 진입 전 단계로 적절한 수준인가?**

다음 4 판정 옵션 중 하나를 *근거와 함께* 제시해 주십시오:

1. **APPROVE** — PR-2 본 안 그대로 진행 가능. ADR-012 발행 + G4 §4.4 / §4.6 보강 적정.
2. **APPROVE WITH CONDITIONS** — 일부 문구 / 사양 / 조건 보강 후 진행 가능. (조건 명시 필수)
3. **PARTIAL** — PR-2 일부만 진행 가능 (예: ADR-012 만 / G4 보강 만). 나머지는 추가 작업 필요. (어느 부분이 부족한지 명시)
4. **BLOCK** — 중대 결함 (대안 권고 또는 추가 사전 작업 필요). (결함 명시 + 후속 조치 권고)

또한 본 검토의 *메타* 목적은 자기참조 편향 통제입니다 — 본 프로젝트의 내부 Agent A / B / C 가 모두 같은 컨텍스트 (Claude Opus 4.7 메인 컨텍스트 패밀리) 에서 작성되므로, *진정으로 다른* 시각의 외부 LLM 의견이 본 합의의 메타 편향 통제에 결정적입니다. **본 의뢰 자료에 내부 Agent 분석 결과를 포함하지 않은 것은 의도된 편향 통제** 입니다.

본 합의에서 결정 *금지* 사항 (사용자 명시 답습, 변동 없음):
- ❌ Hermes PMO 격상 선언 (별도 결정)
- ❌ P2 v3 정식 채택 자동 선언 (본 PR-2 후 별도 합의)
- ❌ ADR-008 / 009 / 010 / 011 본문 자동 갱신 (cross-reference 만 가능)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리 (P2 v3 정식 채택 시점)
- ❌ 실 runtime code / migration script / hook 구현 (Implementation/Runtime PASS 별도)
- ❌ Tier-2 / Tier-3 catalog 자동 확장

---

## 1. 시스템 정체성 (요약)

### 1.1 프로젝트 성격

- **이름**: AI Development Tool Template (AI 자동화 개발 도구 메타-템플릿)
- **사용자**: 1인 개발자 (동일 호스트, SPOF 의도적 수용 — `G3 §5.5` 답습)
- **저장소**: 코드 0줄, 약 60개 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 합의 보고서 + 가이드)
- **사용 방식**: 새 프로젝트 생성 → 본 템플릿 복사 → Phase 0 (자동화 검토 질문지) → Phase 1 (3+1 합의로 아이디어 / 스택 / 에셋 결정) → Phase 2-3 (SDD → TDD 코드)

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지)
- **하네스 엔지니어링**: 8-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
- **3+1 멀티에이전트 합의**: Agent A (구현) + Agent B (안전성) + Agent C (대안) → Reviewer 종합

### 1.3 권위 위계 (영구 권위)

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

본 위계는 **ADR-011 §2.3** 에 영구 권위로 명시되어 있습니다. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상** 입니다.

### 1.4 메타-슬로건

> "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."
>
> Agent = Model + Harness. 모델은 추론을 제공하고, 하네스 (문서 / 규칙 / 훅 / 검증) 는 나머지 전부.

---

## 2. 본 PR-2 의 *진입 컨텍스트* (현 4 게이트 상태)

### 2.1 4 게이트 현 상태 (2026-05-09)

| 게이트 | 정의 | 현 상태 |
|-------|------|--------|
| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기, ADR-011 §2.2 권위) |
| **G1b** | DB-level fallback (SQLCipher BEFORE INSERT trigger + REGEXP UDF) | ✅ **PASS** (2026-05-07, R-2 ~ R-7 6단계 + R-6 actual run `25482284523` 24초 PASS, 42/42 catalog, leak 0) |
| **G2** | 6 거버넌스 사전조건 (P1~P8 위반 경로 매핑 + GP-1 ~ GP-6) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — Implementation/Runtime PENDING |
| **G3** | "Hermes ≠ root of trust" 운영 구현 (22 권한 / 자기참조 차단 / Evidence 결정 5 운영 규칙) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — 운영 구현 PENDING |
| **G4** | Provider-agnostic Memory / Skill 형식 (4 Memory scope / 17 Skill schema 필드 / JSONL hash chain) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)** — 라운드트립 + migration script PENDING |

본 PR-2 는 **G2 / G3 / G4 PASS 후 P1 조건 흡수** 단계의 일부입니다. P1 조건은 10건 (C-C ~ C-N) 이며, 본 PR-2 는 그 중 *2건* 을 묶어 처리:
- **C-C**: Evidence Ledger 보호 강화 → ADR-012 신규 발행
- **C-G**: G4 §4.4 / §4.6 hash chain 사양 보강

PR-1 (단축 합의, Reviewer-only) 은 이미 완료되었으며 (C-D / C-E / C-F / C-I / C-K / C-L 6건 본문 흡수), 본 PR-2 는 그 다음입니다.

### 2.2 현 P2 v3 (Hermes Adoption v3) 상태

`docs/architecture/hermes-adoption-design-v3.md` (12 섹션, **DRAFT**). G2 / G3 / G4 PASS 후 별도 합의로 정식 채택 검토. **본 PR-2 머지 후 + cross-vendor 외부 LLM 추가 + P2 v3 정식 채택 합의 풀 3+1** 의 sequence (사용자 명시 결정 답습).

### 2.3 ADR 권위 정리 (현 발행)

| ADR | 제목 | 본 PR-2 와의 관계 |
|-----|------|---------------|
| **ADR-008** | Hermes 도입 결정 (Option B) — 부록 B Amendment | 차단조건 #2 (JSONL export 표준) cross-reference 후보 |
| **ADR-009** | Self-Adapter v2 진입 조건 | 별도 PR (C-N) — 본 PR-2 범위 외 |
| **ADR-010** | SQLCipher Vault 키 관리 | secret 처리 cross-reference 후보 |
| **ADR-011** | **Means-vs-Ends Redaction Principle (모법)** | 본 PR-2 의 권위 근거 — §2.1 (a)~(d) 4조건 + §2.3 권위 위계 + §2.4 T1 / T2 / T3 |
| **ADR-012** (신규) | **Evidence Ledger Protection (본 PR-2 산출)** | **본 의뢰의 핵심** |

---

## 3. ADR-011 모법 — 본 PR-2 의 권위 근거 (요약)

### 3.1 §2.1 수단/목적 분리 원칙

> 비협상 조건의 본질은 특정 구현 *수단* 이 아니라 달성해야 하는 안전 *결과* 이다.

대체 수단 채택 4조건 **(a)~(d)** + 합의 APPROVE **(e)** = 5조건 패턴:
- (a) 동등 이상의 보안 결과 (명시 비교표)
- (b) 격리 환경 PoC 실증 (Docker)
- (c) ADR 권위 명시
- (d) 자동 회귀 검증 경로 확보 (CI)
- (e) 합의 APPROVE

본 5조건 패턴은 G2 / G3 / G4 모든 § Exit 기준의 표준이며, 본 ADR-012 도 답습.

### 3.2 §2.3 권위 위계 (Hermes ≠ root of trust)

5 운영 함의:
1. Hermes 출력은 Tools 로 검증된다
2. Hermes 자체 redaction 은 로그 / 송신 방어로만 신뢰
3. DB INSERT 경로는 Hermes 외부 (G1b SQLCipher trigger) 로 보호
4. Hermes 의존성 업그레이드 자동 회귀 검증 (R-6)
5. Hermes 학습 결과의 자동 정책 반영 금지 (T3)

### 3.3 §2.4 자동 학습 vs 자동 정책 변경 분리 (T1 / T2 / T3)

- **T1 자동**: Worker 패턴 학습, 도구 사용 빈도 누적, 휴리스틱
- **T2 사용자 승인 필수**: Skill / Memory promotion, 새 도구 등록, 합의 형태 결정
- **T3 절대 금지**: Constitution / ADR / Harness Gates 정의 자체의 변경 (단축 또는 풀 3+1 합의 + ADR Amendment 필수)

본 PR-2 의 ADR-012 발행 자체는 *T3 변경* (ADR 신규 발행 = ADR 정의 자체의 변경) — 풀 3+1 합의 + 외부 LLM 1+ 가동 사유.

---

## 4. PR-2 핵심 산출 사양 (사용자 명시 12 + 4 항목)

### 4.1 ADR-012 신규 발행 — 12 항목 포함 의무

| # | 항목 | 사용자 명시 답습 | 본 의뢰 평가 영역 |
|---|------|-----------|---------------|
| (1) | Evidence Ledger 보호 원칙 | ✅ | §9.1 |
| (2) | **11 필드 구조** | ✅ | §9.2 (현 G4 §4.2 = 10 필드, +1 확장 — 어느 필드?) |
| (3) | **append-only 원칙** | ✅ | §9.3 |
| (4) | **hash chain** | ✅ | §9.3 |
| (5) | **signed commit OR git append commit** (둘 중 하나 의무) | ✅ | §9.4 |
| (6) | **RFC 8785 JCS canonicalization 채택 여부** | ✅ | §9.5 (현 G4 §4.4 = lex sort + RFC 8259, JCS 미인용) |
| (7) | **genesis hash 정의** | ✅ | §9.6 (현 G4 §4.4 = `sha256("genesis:<scope>:<schema_version>")`) |
| (8) | **prev_hash 검증 실패 처리** | ✅ | §9.7 (현 G4 §4.4 미명시) |
| (9) | **full rewrite 방어** | ✅ | §9.8 (history 통째 재작성 차단) |
| (10) | **round-trip lossy 검출** | ✅ | §9.9 (현 G4 §4.6 = hash 일치 OR 의미 보존) |
| (11) | **JSONL export / import 무결성** | ✅ | §9.10 |
| (12) | **evidence forgery 방지** (G2 §1.2.5 P10 deferred candidate cross-reference) | ✅ | §9.11 |

### 4.2 G4 §4.4 / §4.6 hash chain 사양 보강 — 4 항목

| # | 항목 | 사용자 명시 답습 | 본 의뢰 평가 영역 |
|---|------|-----------|---------------|
| (G4-A) | §4.4 hash chain 사양 보강 | ✅ | §9.5 / §9.6 / §9.7 / §9.8 |
| (G4-B) | §4.6 round-trip 검증 절차 보강 | ✅ | §9.9 |
| (G4-C) | canonical JSON 규칙 명확화 (RFC 8785 JCS 또는 동등 표준) | ✅ | §9.5 |
| (G4-D) | migration / export / import 검증 실패 시 rollback 조건 | ✅ | §9.12 |

---

## 5. 현 G4 §4.2 / §4.4 / §4.6 본문 (PR-2 보강 *전*)

### 5.1 §4.1 ~ §4.2 — 현 JSONL Schema (10 필드)

```jsonl
{"type":"memory","scope":"global","id":"<uuid>","schema_version":"0.1","ts":"2026-05-07T10:00:00Z","agent":"user","content":{...},"evidence_refs":["docs/evidence/<task-id>.md"],"prev_hash":"<sha256>","hash":"<sha256>"}
```

| 필드 | 타입 | 필수 | 검증 규칙 |
|------|-----|----|--------|
| `type` | enum | ✅ | `memory` / `skill` |
| `scope` | enum | ✅ | `global` / `project` / `session` / `team` |
| `id` | string | ✅ | UUID v4 또는 slug |
| `schema_version` | string | ✅ | semver (현 `0.1` MVP) |
| `ts` | ISO 8601 | ✅ | entry 생성 timestamp |
| `agent` | string | ✅ | provider-neutral identifier (`user` / `<worker_name>` / `hermes` 등) |
| `content` | object | ✅ | (Memory) 자유 schema, (Skill) §3.1 17 필드 schema 그대로 |
| `evidence_refs` | array\<string\> | 권장 | Markdown evidence 파일 경로 |
| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` |
| `hash` | string (sha256) | ✅ | 본 entry 의 canonical JSON sha256 (변조 방지) |

**합산 = 10 필드**. 사용자 명시 PR-2 = *11 필드 구조*. **+1 필드 후보**:

| 후보 | 필드명 | 정체성 |
|-----|------|------|
| (a) | `event` | enum (`memory_write` / `skill_proposed` / `skill_approved` / `skill_promoted` / `roundtrip_lossy` / `gate_pass` / `external_llm_received` / `evidence_forgery_detected` 등) |
| (b) | `signature` | signed commit (GPG / SSH) 서명 또는 detached signature reference |
| (c) | `chain_id` | 다중 chain 분리 (Memory chain / Skill chain / Gate chain 등) |
| (d) | `parent_event_id` | event 간 cross-reference (예: `external_llm_received` → `gate_pass` parent) |
| (e) | (추가 안 함, 10 필드 유지, hash chain 만 강화) |

> **외부 LLM 평가 요청 1 (§9.2)**: 어느 +1 필드 후보가 1인 개발자 메타-템플릿 스케일에서 *가장 단순 + 견고한 보호 강화* 인가? 또는 다른 후보 권고?

### 5.2 §4.4 — 현 Hash Chain 변조 방지 본문 (보강 *전*)

```
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
```

**미명시 영역** (PR-2 보강 대상):
- prev_hash 검증 실패 처리 절차
- full rewrite (history 통째 재작성) 방어
- canonical JSON 의 RFC 8785 JCS 또는 동등 표준 인용
- signed commit vs git append commit 의 *기준* (어느 경우 어느 매커니즘?)

### 5.3 §4.6 — 현 라운드트립 검증 절차 본문 (보강 *전*)

```
[원본 Hermes JSONL] → ① hermes_to_claude.py 변환 → [Claude 형식]
                  → ② Claude → 다시 본 G4 JSONL 형식으로 변환 → [재변환 JSONL]
                  → ③ canonical JSON sha256 비교 → [원본 hash 일치 검증]

**검증 PASS 조건**:
- hash 일치 (정확 round-trip) **또는** 의미 보존 검증 (사용자 명시 review — 손실 허용 영역 명시)
- 손실 발생 시 손실 영역 ledger entry (`event: roundtrip_lossy`)
```

**미명시 영역** (PR-2 보강 대상):
- 의미 보존 검증의 자동화 가능성 (사용자 review 의무 vs 일부 자동)
- `event: roundtrip_lossy` ledger entry 의 *형식 사양* (어느 필드 추가 / 변경)
- migration / export / import 검증 실패 시 rollback 조건 (4 후보: BLOCK + manual / 자동 revert / 원본 보존 + 새 entry / dual write)

---

## 6. 현 G3 §1.3 / §5.3 — Evidence 결정 5 운영 규칙 (요약)

`docs/architecture/hermes-not-root-of-trust-runtime.md` §5 (Evidence 결정 5 운영 규칙):

```
Agent proposes.       (제안)
Hermes orchestrates.  (조율 — 격상 후)
Tools verify.         (검증 — 계산적 우선)
Evidence decides.     (결정 — 기록 없으면 PASS 미성립)
Human overrides.      (사람이 최종 방향)
```

**PASS 성립 4 요건** (G3 §5.3):
- (i) Tools 검증 (린터 / 타입체커 / 테스트 / trigger / canary 등)
- (ii) Evidence Ledger entry (본 PR-2 ADR-012 보호 강화 대상)
- (iii) (T2 / T3) 사용자 명시 승인
- (iv) (해당 시) 합의 보고서 commit

본 PR-2 의 ADR-012 는 *(ii) Evidence Ledger entry* 의 *무결성 보호* 를 강화하는 것. (i) / (iii) / (iv) 와의 *상호 의존* 위치를 명시 평가 대상.

---

## 7. 현 G2 §1.2.5 — P9 ~ P12 deferred candidates (cross-impact)

PR-1 흡수 (C-I, 2026-05-09 후속 2):
- **P9**: Prompt Injection
- **P10**: **Evidence Forgery** ← 본 PR-2 ADR-012 가 *정식 등록 트리거*
- **P11**: Supply-chain (deps)
- **P12**: Memory Poisoning Side-channel

P10 정식 등록 시점 = **본 PR-2 ADR-012 발행 시점** (G2 §1.2.5 명시).

> **외부 LLM 평가 요청 2 (§9.11)**: 본 ADR-012 발행으로 P10 (Evidence Forgery) 이 *정식 위반 경로* 로 자동 등록되어야 하는가? 별도 PR 로 분리해야 하는가?

---

## 8. PR-2 핵심 트레이드오프 (외부 LLM 평가 영역)

### 8.1 ADR-012 별도 발행 vs 대안

| 옵션 | 정체성 | 장단점 |
|-----|------|------|
| **A** (사용자 명시 안) | ADR-012 별도 발행 + G4 §4.4 / §4.6 보강 | (+) 권위 분리 명료, P10 정식 등록 트리거 명확 / (-) ADR 갯수 증가, 1인 개발자 부담 |
| B | ADR-008 부록 C (Evidence Ledger 부록) 추가 | (+) 단일 ADR, 차단조건 #2 (JSONL) 자연 확장 / (-) ADR-008 비대화, Hermes 도입 결정과 evidence 무결성 혼재 |
| C | G3 §1.3 + §5.3 본문 보강 단독 (ADR 신규 0건) | (+) 새 권위 0건, ADR-011 §2.4 답습 / (-) Evidence 무결성의 ADR 권위 부재 (T3 변경 시 권위 약함) |
| D | G4 §4.4 / §4.6 본문 보강 단독 (ADR 신규 0건) | (+) 사양만 명시, 권위 발행 0건 / (-) 11 필드 / signed commit / forgery 방지 등의 ADR 권위 부재 |

### 8.2 11 필드의 11번째 — 단순화 vs 견고성

§5.1 의 +1 필드 후보 (a) ~ (e) 비교. 1인 개발자 + 메타-템플릿 + 4 게이트 모두 Implementation PASS 미충족 현실에서 *어느 후보가 가장 단순 + 견고* 한가?

### 8.3 Canonical JSON — RFC 8785 JCS vs 자체 정의

| 옵션 | 정체성 | 평가 |
|-----|------|------|
| 1 | RFC 8785 JCS 정식 인용 | IETF 표준, 라이브러리 가용성 (Python `pyjwt`/`jwcrypto` 의존, Node `canonicalize` npm) |
| 2 | 현 G4 §4.4 단순 정의 유지 | 구현 단순, 호환성 책임 사용자 |
| 3 | DigitalBazaar canonicalize-json 등 비-RFC 표준 | 비주류, 호환성 약함 |
| 4 | 자체 정의 minimal (lex sort + RFC 8259 + 추가 명시) | 1인 개발자 부담 ↓ |

### 8.4 Signed commit vs Git append commit vs 둘 다

| 옵션 | 정체성 | 1인 개발자 동일 호스트 SPOF 영향 |
|-----|------|-------------|
| A | signed commit (GPG / SSH) 단독 의무 | GPG / SSH key SPOF, multi-host 전환 시 강 |
| B | git append commit (append-only branch) 단독 의무 | host 단독, force-push 차단 의무 |
| C | 둘 중 하나 의무 (사용자 명시) | 유연성 ↑, 일관성 ↓ |
| D | 둘 다 동시 의무 | 강한 보장, 비용 ↑ |
| E | hash chain + signed (signed 전용 또는 보조) | hash chain 핵심, signed 보조 |

### 8.5 Round-trip Lossy 검출 — Strict vs Loose

| 옵션 | 정체성 |
|-----|------|
| (a) | hash 일치 *only* — 의미 보존 미허용 (strict, 손실 0건 강제) |
| (b) | 의미 보존 *only* — 사용자 review 의무 (loose, 운영 부담 ↑) |
| (c) | tier-별 (T2 = hash 일치 / T3 = 의미 보존) |
| (d) | 현 *OR* 유지 (사용자 명시 후보 = (a) **OR** (b)) |

### 8.6 PR-2 통합 묶음 vs 분리 (PR-2a + PR-2b)

| 옵션 | 정체성 |
|-----|------|
| 통합 (사용자 명시) | C-C + C-G 동시 묶음 1 PR + 풀 3+1 1회 |
| 분리 | PR-2a (ADR-012 만) + PR-2b (G4 §4.4 / §4.6 만) — 풀 3+1 *2회* (중복 비용) |

---

## 9. 평가 요청 사항 (필수)

다음 12 차원으로 평가해 주십시오. 각 차원에 *명확한 판정* + *근거* + *식별된 위험 / 결함 / 단순화 권고* 를 제시해 주십시오.

### 9.1 차원 1 — Evidence Ledger 보호 원칙의 적정성

- ADR-012 §1 (보호 원칙) 가 *어느 수준* 까지 명시해야 하는가?
- 헌법 8조 / 5조 / ADR-011 §2.1 / §2.3 / §2.4 와의 cross-reference 충분 조건은?
- 1인 개발자 메타-템플릿 스케일에서 *과도* 또는 *부족* 한 부분?

### 9.2 차원 2 — 11 필드 구조 (현 10 필드 + 1)

- §5.1 의 +1 필드 후보 (a) ~ (e) 중 어느 것을 권고? (또는 다른 후보?)
- 1인 개발자 메타-템플릿 운영 부담 평가
- evidence forgery 방어 / round-trip lossy 검출 / signed commit 통합 효과 비교

### 9.3 차원 3 — append-only 원칙 + hash chain

- 본 PR-2 가 *수정 / 삭제 금지* 를 어느 layer 에서 강제? (filesystem / git / pre-commit hook / CI / 합의)
- prev_hash + hash sha256 의 견고성 — 더 강한 후보 (BLAKE3, SHA-3) 가 정당한가?

### 9.4 차원 4 — signed commit OR git append commit (둘 중 하나 의무)

- §8.4 5 옵션 중 어느 것 권고? (또는 다른 후보?)
- 1인 개발자 + 동일 호스트 SPOF 와 결합한 리스크 평가
- 메타-템플릿이 다른 사용자 / 다른 호스트로 복사될 시 어느 옵션이 가장 강 / 약?

### 9.5 차원 5 — RFC 8785 JCS canonicalization 채택 여부

- §8.3 4 옵션 중 어느 것 권고?
- IETF 권위 / 라이브러리 가용성 / 1인 개발자 부담 / 호환성 책임 4 측면 평가
- canonical 위반의 자동 검출 가능성 (CI 회귀 검증)

### 9.6 차원 6 — Genesis hash 정의

- 현 `sha256("genesis:<scope>:<schema_version>")` 가 견고한가?
- 다중 chain (`chain_id`) 도입 시 genesis 정의 변경 필요?
- 첫 entry 의 prev_hash 가 genesis_hash 인 것이 충분한 보장인가?

### 9.7 차원 7 — prev_hash 검증 실패 처리

- 4 후보 (BLOCK + manual / 자동 revert / 원본 보존 + 새 entry / dual write) 중 어느 것 권고?
- silent failure 위험 (검증 실패 미감지) 차단 매커니즘
- ADR-011 §2.4 T3 (자동 정책 변경 금지) 위반 가능성

### 9.8 차원 8 — Full rewrite 방어

- 후보 매커니즘 비교 (signed tag / signed commit / append-only branch / external snapshot / pre-commit hook 차단)
- git history 통째 재작성 (force push, rebase, filter-branch) 차단의 *완결성*
- 1인 개발자 동일 호스트 SPOF 와 결합한 리스크

### 9.9 차원 9 — Round-trip lossy 검출

- §8.5 4 옵션 중 어느 것 권고?
- `event: roundtrip_lossy` ledger entry 형식 사양 — `+1 필드` (§5.1) 후보와 결합 평가
- 의미 보존 검증의 *사용자 review* 의무 — 자기참조 위험 (G3 §4.7 메타-순환 청산 답습)

### 9.10 차원 10 — JSONL export / import 무결성

- import 시 schema_version declaration 의 *의무성* (G4 검토 P-3 자기 발견 위험 답습)
- 외부 형식 (Claude / OpenAI / Ollama) 으로 변환 후 다시 import 의 무결성 보장 매커니즘
- migration script Hermes 의존 0 (depcruise 검증) 의 본 ADR-012 보호 위치

### 9.11 차원 11 — Evidence forgery 방지 (P10 정식 등록 트리거)

- 본 ADR-012 가 P10 정식 등록을 *자동 트리거* 하는 것이 정당한가?
- *공격 모델* 정의: (a) 1인 개발자 호스트 침해 / (b) Hermes container compromise / (c) git history rewrite / (d) JSONL middle entry tampering / (e) external LLM response 위조
- 각 공격 모델별 본 PR-2 산출의 방어 유효성 평가

### 9.12 차원 12 — Migration / export / import 검증 실패 시 rollback 조건

- BLOCK + manual / 자동 revert / 원본 보존 + 새 entry / dual write 중 권고?
- ADR-011 §2.4 T3 자동 정책 변경 금지 답습 — rollback 자체가 T3 위반인가?
- Implementation/Runtime PASS 별도 합의 영역과의 경계

### 9.13 차원 13 — 영구 핵심 제약 5건 본 PR-2 답습 충분성

- Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리 — 각각 본 PR-2 산출 어디서 보호?
- 부족한 cross-reference 위치는?

### 9.14 차원 14 — PR-2 통합 묶음의 정당성

- §8.6 통합 vs 분리 — 어느 것 권고?
- C-C (ADR-012) + C-G (G4 보강) 의 *상호 의존* 강도 평가

### 9.15 차원 15 — ADR-008 / 009 / 010 / 011 cross-reference 영향

- ADR-008 차단조건 #2 (JSONL export) 와 ADR-012 의 cross-reference 위치
- ADR-010 (SQLCipher Vault) 의 secret 처리 → Evidence Ledger secret 처리 cross-reference 필요?
- ADR-011 §2.1 (a)~(d) 4조건 답습이 본 ADR-012 에서 *어느 정도* 강제되어야 하는가?
- ADR-009 (Self-Adapter v2) 와의 cross-reference 후보

### 9.16 차원 16 — 메타 편향 / 자기참조 위험

- 본 PR-2 합의의 자기참조 한계가 *충분히 노출* 되는가?
- 외부 LLM 1+ 만으로 자기참조 위험이 충분히 통제되는가?
- 본 합의 후 P2 v3 정식 채택 전에 추가 외부 검증 (cross-vendor — Gemini / GPT-5.x 등) 이 필요한가?

### 9.17 최종 판정

다음 중 하나를 *명시* 해 주십시오:
- **APPROVE**
- **APPROVE WITH CONDITIONS** (조건 enumeration)
- **PARTIAL** (어느 부분 PASS, 어느 부분 조건부, 어느 부분 BLOCK)
- **BLOCK** (결함 enumeration + 후속 조치 권고)

판정 근거는 §9.1 ~ §9.16 16 차원 모두 반영해 주십시오. 본 외부 LLM 의견은 본 프로젝트의 Reviewer 가 Agent A (구현/운영) + Agent B (보안/거버넌스) + Agent C (대안/단순화) 의 3 내부 분석과 종합하여 최종 합의 보고서에 반영합니다.

---

## 10. 영구 핵심 제약 (변동 없음)

본 5건은 본 합의 결과와 무관하게 영구 유지:

1. **Provider Liquidity** — 헌법 5조 (관용) 비협상, 사용자 메모리 명시
2. **Hermes ≠ root of trust** — ADR-011 §2.3 영구 권위
3. **메타포 강제 금지** — system-identity-prequel §7
4. **자동 정책 변경 금지 (T3)** — ADR-011 §2.4
5. **수단/목적 분리 원칙** — ADR-011 §2.1 (a)~(d) 4조건

본 PR-2 가 위 5건 보호를 어느 §에서 답습하는지 §9.13 평가 영역.

---

## 11. 메타 한계 — 자기참조 위험 (의도적 노출)

본 합의 자체에 다음 한계가 있습니다 (모두 정직하게 노출):

1. **본 PR-2 가 합의 인프라 (3+1) 가 가진 자기참조 위험을 인지** 하고 있습니다 — Agent A / B / C 가 모두 같은 Claude Opus 4.7 메인 컨텍스트 패밀리.
2. **G3 §4.4.2 답습**: ADR 신규 발행 (T3 변경) 은 외부 LLM *권장*. 본 의뢰가 그 권장의 실현입니다.
3. **본 의뢰 자료에는 내부 Agent A / B / C 분석 결과 포함 0건** — 의도된 편향 통제. 본 외부 LLM 응답 후 Reviewer 가 4 입력 (A / B / C / 외부 LLM) 통합.
4. **메타-템플릿 컨텍스트** — 본 PR-2 가 *현 프로젝트* 의 evidence ledger 만 보호하는 것이 아니라 *복사된 모든 파생 프로젝트* 의 evidence ledger 도 보호. 메타-템플릿 스케일의 운영 부담 평가가 핵심.
5. **외부 LLM 1+ 의견의 *집계* 방식** — 본 의뢰는 *단일* 외부 LLM 의 의견. cross-vendor 추가 (Gemini / GPT 등 다른 vendor) 는 P2 v3 정식 채택 진입 전 사용자 결정으로 별도. 본 의뢰자는 *최소 1 외부 LLM* 으로 본 PR-2 진행 결정 후보.

---

## 12. 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습, 본 의뢰 결과와 무관 영구 유지)

- ❌ Hermes PMO 격상 선언 (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도)
- ❌ P2 v3 정식 채택 자동 선언 (본 PR-2 후 cross-vendor 추가 + 풀 3+1 별도)
- ❌ ADR-008 / 009 / 010 / 011 본문 자동 갱신 (cross-reference 만 가능, 본문 갱신은 별도 PR)
- ❌ ADR-012 발행 외 ADR 추가 발행 (예: ADR-013 / ADR-014 후보는 별도 합의)
- ❌ P2 v2 / system-identity-prequel archive 자동 처리 (P2 v3 정식 채택 시점)
- ❌ 실 runtime code 구현 (Memory boundary hook / Skill wrapper / promotion hook / JSONL writer / hash chain 검증 등)
- ❌ 실 migration script 구현 (`scripts/hermes-migration/*.py`)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 자동 (본 PR-2 가 트리거하지만 *정식 등록* 자체는 별도 §1.2 본문 갱신 합의)

---

**검토 의뢰 작성일**: 2026-05-09
**의뢰 자료 버전**: v1
**자기충족성**: 본 문서만으로 평가 가능 (첨부 자료 없음, 내부 Agent 분석 결과 0건 — 의도된 편향 통제)
**응답 저장 예정**: `docs/external-review/2026-05-XX-pr2-evidence-ledger-response.md` 또는 본 세션 직접 붙여넣기
**선행 의뢰 자료**: `docs/external-review/2026-05-09-g2g3g4-promotion-request.md` (G2/G3/G4 정식 PASS 합의 — 본 PR-2 의 진입 컨텍스트)
