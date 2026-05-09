# Agent A — 구현/운영 가능성 분석 (PR-2: ADR-012 신규 발행 + G4 §4.4/§4.6 hash chain 사양 보강)

**작성일**: 2026-05-09
**Agent 역할**: 구현/운영 가능성 (Implementation / Operability)
**검토 범위**: PR-2 풀 3+1 합의 — P1 조건 C-C (Evidence Ledger 보호 강화) + C-G (G4 hash chain 사양 보강) 통합 흡수
**관점 기준 질문**: "실제로 동작하는가? — 기술적 구현 가능성, 의존성, 성능, 1인 개발자 메타-템플릿 운영 부담"
**상위 권위**: ADR-011 §2.1 (수단/목적 분리, (a)~(d) 4조건) + (e) 합의 APPROVE = 5조건 패턴, ADR-011 §2.3 권위 위계, ADR-011 §2.4 T1/T2/T3, system-identity-prequel §6.3 (Evidence Ledger MVP)
**금지 (사용자 명시 답습)**: ❌ Hermes PMO 격상 / ❌ P2 v3 정식 채택 자동 선언 / ❌ ADR-008/009/010/011 본문 자동 갱신 (cross-reference 만 가능) / ❌ P2 v2 / system-identity-prequel archive 자동 처리 / ❌ 실 runtime code / migration script 구현 / ❌ Tier-2 / Tier-3 catalog 자동 확장 / ❌ 다른 Agent 출력 참조 / ❌ 메타포 강제

---

## 0. 요약 (Executive Summary) — 본 입력의 입장 + 메타 한계

### 0.1 입장

본 Agent A 분석은 PR-2 (ADR-012 신규 발행 + G4 §4.4/§4.6 hash chain 사양 보강) 의 **운영 가능성 (Operability)** 만을 본다 (보안/품질은 Agent B, 대안은 Agent C 영역). 핵심 결론:

1. **PR-2 6 핵심 산출 (ADR-012 11 필드 / hash chain / signed commit OR git append / RFC 8785 JCS / round-trip lossy / migration script 사양) 은 모두 *Design/Governance Gate PASS* 수준에서 사양화 가능** — 신규 발명 0건, 기성 도구 (sha256 / `jq` / git pre-commit hook / canonical JSON 라이브러리 / GPG 서명) 답습.
2. **그러나 11 필드 후보 4건 (`event` / `signature` / `chain_id` / `parent_event_id`) 의 *어느 것이 11번째인가* 는 본 PR-2 가 명시 결정해야 함** — 운영상 단순성 + system-identity-prequel §6.3 schema 답습 + Evidence Ledger 11 필드 enumeration (g2g3g4 합의 §4.4 GPT 단독 제시) 의 *교차 매핑* 결과 권고.
3. **signed commit vs git append commit 의무 (둘 중 하나) 는 1인 개발자 + 동일 호스트 SPOF 환경에서 *git append commit (append-only branch + pre-commit hook)* 이 MVP 권고** — signed commit (GPG/SSH) 은 SPOF 동일 + 운영 부담 추가, append-only 는 표준 git 인프라 답습 가능.
4. **RFC 8785 JCS 채택은 운영 가능** — Python (`pyjcs`) / Node (`canonicalize`) / Go (`gowebpki/jcs`) 모두 production-grade 라이브러리 가용, 1인 개발자 부담 LOW. 단, `jq -S -c` 정도의 *lex sort + RFC 8259 escape* 로도 G4 §4.4 현 정의가 결정성 충분 — JCS 는 *권고 보강* 수준.
5. **round-trip lossy 검출 + `event: roundtrip_lossy` ledger entry 형식 사양은 사양 가능** — 단, *의미 보존 검증* 은 사용자 review 의무 영역 (자동화 절대 금지, ADR-011 §2.4 T2).
6. **migration/export/import 검증 실패 시 rollback 조건 4 후보 중 운영 권고 = "BLOCK + 원본 보존 + 새 entry"** — dual write 는 schema_version drift 유발, 자동 revert 는 T3 위반 위험.
7. **본 PR-2 의 *Design/Governance Gate PASS* 한정 시점에 11 필드 schema + hash chain 사양 + signed/append commit 선택 + JCS 채택 여부 + round-trip lossy 형식 + migration rollback 조건 = 6 사양은 모두 *문서 차원* 까지. 실 runtime code (JSONL writer / hash chain validator / migration script 실 PoC) 는 별도 합의** (사용자 명시 답습).
8. **판정**: **APPROVE WITH CONDITIONS** — PR-2 풀 3+1 합의 진입 적격. 단, 8 조건 충족 필요 (§4 참조).

### 0.2 메타 한계

본 Agent A 는 **메인 컨텍스트와 동일 패밀리 (Claude)**. 본 분석의 자기참조 위험은 본 합의 §0.3 / Reviewer 종합 §메타 편향 자기진단 에서 외부 LLM 1+ 의견으로 통제. 본 입력은 *합의 본부* 가 아니라 *Reviewer 가 종합할 한 입력* — APPROVE / BLOCK 판정도 본 입력의 *Agent A 관점에서의 판정* 임 (단일 권위 아님).

본 Agent A 는 *G4 본문 작성자* (직전 PR-1 흡수 작업) 와 동일 컨텍스트 — `provider-agnostic-memory-skill-design.md` §4.4 canonical JSON 정의 + §11.1 P-1 자기 발견 (RFC 8785 JCS 미인용) 의 *작성자 측면* 에서 본 PR-2 검토는 자기 산출 자기 검토 위험 잔존. 외부 LLM 1+ (GPT cross-vendor 권장 + Claude 인접 컨텍스트) 의무 답습 (g2g3g4 합의 C-T 패턴).

---

## 1. PR-2 6 핵심 산출의 구현 가능성 평가

PR-2 의 *최소 필수 산출* (사용자 명시) 6 항목을 본 Agent A 가 운영 가능성 측면에서 개별 평가:

### 1.1 산출 1 — ADR-012 11 필드 schema

**운영 가능성**: ✅ **HIGH** — 11 필드 모두 표준 타입 (UUID / enum / ISO 8601 / sha256 / JSON), 신규 발명 0건.

**11 필드 후보 매핑 (system-identity-prequel §6.3 schema 9 필드 + G4 §4.2 schema 10 필드 + GPT g2g3g4 합의 §4.4 11 필드 enumeration 의 교차)**:

| # | 필드 후보 | 출처 | 자동 생성? | 운영 부담 |
|---|--------|-----|--------|--------|
| 1 | `ts` (ISO 8601 timestamp) | prequel §6.3 + G4 §4.2 + GPT enumeration | ✅ 자동 (`datetime.utcnow().isoformat()`) | 0 |
| 2 | `task_id` 또는 `id` (UUID v4) | prequel §6.3 + G4 §4.2 | ✅ 자동 (`uuid.uuid4()`) | 0 |
| 3 | `event` (enum: test_pass/test_fail/lint/secret_scan/consensus/review/rollback/memory_write/skill_promotion/roundtrip_lossy/gate_pass/external_llm_received) | prequel §6.3 + GPT enumeration | ⚠️ 반자동 (event 종류는 caller 명시) | 저 |
| 4 | `agent` (provider-neutral: user/Hermes/Worker_X/PM/Reviewer) | prequel §6.3 + G4 §4.2 | ✅ 자동 (Hermes / runtime 식별) | 0 |
| 5 | `result` (enum: PASS/FAIL/BLOCK/ROLLBACK) | prequel §6.3 + GPT (pass-fail status) | ⚠️ 반자동 (caller 명시) | 0 |
| 6 | `tool` 또는 `gate_id` (어느 게이트 / 어느 도구 발화) | GPT enumeration (gate_id / tool) | ✅ 자동 (runtime context) | 0 |
| 7 | `command` (실행 command line 또는 작업 식별) | GPT enumeration | ✅ 자동 (또는 caller 명시) | 0 |
| 8 | `expected` / `actual` (검증 기대/실제 — 별도 2 필드 또는 통합 객체) | GPT enumeration (expected result + actual result = 2 필드) | ⚠️ caller 명시 | 저 |
| 9 | `artifact_path` 또는 `evidence_md` 또는 `ref` (evidence 파일/commit/PR 경로) | prequel §6.3 (`ref` + `evidence_md`) + GPT (`artifact path`) | ✅ 자동 (또는 caller) | 0 |
| 10 | `prev_hash` (sha256 — chain 형성) | prequel §6.3 + G4 §4.2 | ✅ 자동 (직전 entry hash 조회) | 0 |
| 11 | `hash` (sha256 — 본 entry canonical JSON sha256) | prequel §6.3 + G4 §4.2 | ✅ 자동 (canonical JSON serialize + sha256) | 0 |

**11 필드 = prequel §6.3 9 필드 + GPT enumeration 6 추가 후보 = 매핑 후 핵심 11 = (ts, id, event, agent, result, tool/gate_id, expected, actual, artifact_path, prev_hash, hash)**

**운영 권고**: 11 필드 중 **`event` (3) + `result` (5) + `expected/actual` (8) + `artifact_path` (9) = 4 필드는 caller 명시**, 나머지 7 필드는 *자동 생성*. 사용자 직접 수동 작성 부담 = 4 필드만 (run-time 시점에 게이트/도구가 자동 채움 가능 — Phase 2 PoC 시점에 helper library 도입 가능).

**잠재 risk**: GPT enumeration 의 11 필드 중 `reviewer` / `rollback_trigger` / `pass-fail status` 와 prequel §6.3 의 `result` / `summary` 와 G4 §4.2 의 `evidence_refs` (array) 가 *다른 추상화 레벨* — ADR-012 본문에서 **단일 정합 schema** 로 통합 명시 의무. 본 합의에서 단일 권고 도출 불가능 (Reviewer 영역).

### 1.2 산출 2 — Hash Chain 사양 보강

**운영 가능성**: ✅ **HIGH** — sha256 + canonical JSON 표준, 모든 mainstream 언어 지원.

**G4 §4.4 현 정의 vs PR-2 보강 항목**:

| 항목 | G4 §4.4 현 정의 | PR-2 보강 권고 |
|----|------------|-----------|
| key 정렬 | lex sort 명시 | RFC 8785 JCS 명시 인용 (lex sort = JCS 부분집합) |
| whitespace | separator `","` / `":"` 한정 | JCS 답습 — `"` 와 `:` separator, 외 whitespace 0 |
| numeric 정규화 | "integer 정수 / float IEEE 754" 명시 | JCS 의 *number serialization* 답습 — IEEE 754 round-half-to-even, scientific notation 금지, trailing zero 제거 |
| string escape | RFC 8259 명시 | JCS = RFC 8785 = RFC 8259 + 추가 정밀화 |
| Unicode | (미명시) | JCS *NFC normalization* 권고 (G4 §4.4 미명시 — PR-2 흡수 영역) |
| genesis hash | `sha256("genesis:<scope>:<schema_version>")` 명시 | (현 G4 §4.4 충분) |
| prev_hash 검증 실패 처리 | (G4 §4.4 미명시) | **PR-2 핵심 보강** — BLOCK + 사용자 알림 + 합의 결정 |
| full rewrite 방어 | (G4 §4.4 미명시) | **PR-2 핵심 보강** — git append-only branch + signed tag 또는 외부 snapshot |

**운영 부담 추정**:
- canonical JSON 라이브러리 도입 = 1일 (Python `pyjcs` 또는 자체 구현 50 LOC)
- prev_hash 검증 자동화 (`scripts/verify_ledger.py`) = 0.5일
- full rewrite 방어 = git pre-commit hook + branch protection rule = 1일 (GitHub branch protection rule 설정 기 사용 시 0.5일)
- CI 회귀 검증 (R-6 workflow 확장 또는 신규) = 1일

**합산**: 3.5~4일 (Implementation 영역, 본 PR-2 *Design/Governance Gate PASS* 시점에는 사양까지)

### 1.3 산출 3 — Signed Commit OR Git Append Commit (둘 중 하나 의무)

**운영 가능성**: ✅ **HIGH (option 2)** — git append commit + branch protection 권고.

**옵션 비교 (1인 개발자 + 동일 호스트 SPOF 환경)**:

| 옵션 | 운영 부담 | 보장 강도 | SPOF 영향 |
|----|--------|------|--------|
| 옵션 1 — Signed commit (GPG / SSH key) | **중** — GPG 키 생성 + 등록 + 서명 강제 + branch protection rule | ⚠️ 중 — 1인 동일 호스트 시 GPG 키 자체가 SPOF (호스트 침해 시 변조 + 서명 모두 가능) | **중** — 호스트 침해 시 동일 SPOF |
| 옵션 2 — Git append commit (append-only branch + pre-commit hook + branch protection) | **저** — pre-commit hook + GitHub branch protection rule 설정 (force push 금지 + history rewrite 금지) | ✅ 강 — git history 자체가 변조 불가 (rebase/amend 차단) | **중** — 호스트 침해 시 commit 자체는 가능하나 history rewrite 차단 |
| 옵션 3 (보너스) — 둘 다 | **고** — 옵션 1 + 옵션 2 부담 합산 | ✅ 매우 강 | **저** — multi-host 운영 전환 시 권고 |

**MVP 권고 (1인 개발자 + 동일 호스트 SPOF 환경)**: **옵션 2 (git append commit)** — pre-commit hook 50 LOC + GitHub branch protection rule 5 분 설정. 보장 강도 충분, 운영 부담 최소.

**운영 권고 추가**: ADR-012 본문에 **"옵션 2 MVP 채택, multi-host 운영 전환 시 옵션 3 의무 발동 트리거"** 명시 (g2g3g4 C-K SPOF accepted risk 패턴 답습).

### 1.4 산출 4 — RFC 8785 JCS 채택 여부

**운영 가능성**: ✅ **HIGH** — production-grade 라이브러리 가용, 1인 개발자 부담 LOW.

**언어별 라이브러리 가용성**:

| 언어 | 라이브러리 | 상태 | 1인 개발자 부담 |
|----|--------|----|-----------|
| Python | `pyjcs` (PyPI) 또는 자체 50 LOC 구현 | production-ready | 저 |
| Node.js | `canonicalize` (npm) | production-ready | 저 |
| Go | `github.com/gowebpki/jcs` | production-ready | 저 |
| Shell | `jq -S -c` (lex sort + minify) — JCS 의 *부분집합* | 표준 도구 | 0 |

**채택 권고**: ✅ **채택** — G4 §4.4 현 정의는 결정성 *충분* (lex sort + RFC 8259 escape) 이지만 JCS 채택 시:
1. 다른 구현과의 *상호 운용성* 보장 (예: 외부 오케스트레이터 import 시 해시 일치)
2. Unicode NFC normalization 명시 — 한국어 등 멀티바이트 입력의 hash drift 차단
3. Numeric 정규화 명확 (IEEE 754 round-half-to-even, scientific notation 금지)

**잠재 risk**:
- JCS 자체 라이브러리 의존 추가 = depcruise 룰 위반 가능성 (G4 §4.3 *Hermes 의존 0 + 표준 라이브러리만*) — JCS 라이브러리는 *표준 후보* 수준이나 *POSIX 표준* 아님.
- **권고**: ADR-012 본문에 **"JCS 채택, 단 fallback 으로 `jq -S -c` 동등 동작 명시"** — 외부 오케스트레이터가 JCS 라이브러리 미보유 시 `jq -S -c` 로도 hash 일치 가능 (NFC normalization 제외).

### 1.5 산출 5 — Round-trip Lossy 검출 + `event: roundtrip_lossy` ledger entry

**운영 가능성**: ✅ **MEDIUM-HIGH** — 자동 검출 가능, 단 의미 보존 검증은 사용자 review 의무.

**G4 §4.6 현 절차 vs PR-2 보강**:

```
[G4 §4.6 현 절차]
  export → 변환 → 재변환 → canonical JSON sha256 비교
  PASS = hash 일치 OR 의미 보존 검증 (사용자 명시 review)
  FAIL = roundtrip_lossy ledger entry (형식 사양 부재)
```

**PR-2 보강 권고 — `event: roundtrip_lossy` ledger entry 형식 사양**:

```json
{
  "ts": "2026-05-09T15:00:00Z",
  "id": "<uuid>",
  "event": "roundtrip_lossy",
  "agent": "user",  // 의미 보존 review 는 사용자만 가능 (T2)
  "result": "PASS_WITH_LOSS" | "FAIL",
  "tool": "hermes_to_claude.py",
  "command": "python scripts/hermes-migration/hermes_to_claude.py --dry-run",
  "expected": {"hash": "<original sha256>"},
  "actual": {"hash": "<roundtrip sha256>", "lossy_fields": ["<field1>", "<field2>"]},
  "artifact_path": "docs/evidence/roundtrip-2026-05-09.md",
  "prev_hash": "<sha256>",
  "hash": "<sha256>"
}
```

**핵심 추가 필드 (lossy 영역)**: `actual.lossy_fields` 는 어느 필드가 손실되었는지 명시 (사용자 review 가능).

**운영 가능성 평가**:
- ✅ 자동 검출 (hash 비교) — 0.1초 / entry
- ⚠️ 의미 보존 검증 — *사용자 review 의무*, 자동화 절대 금지 (T2 ADR-011 §2.4)
- ✅ ledger entry 자동 생성 — caller (migration script) 가 lossy 필드 enumerate

**잠재 risk**: lossy_fields 가 *비어있으나 hash 불일치* 시점 — caller 가 lossy detection 미완 결과 hash drift 발생. 본 시나리오 처리 절차 PR-2 본문 명시 권고 (BLOCK + 사용자 alert).

### 1.6 산출 6 — Migration / Export / Import 검증 실패 시 Rollback 조건

**운영 가능성**: ✅ **MEDIUM-HIGH** — 4 후보 중 권고 = "BLOCK + 원본 보존 + 새 entry".

**4 후보 비교**:

| 후보 | 운영 부담 | T3 위반 위험 | 권고 |
|----|--------|----------|----|
| **(a) BLOCK + manual** | 저 | 0 | ✅ 권고 (단순) |
| **(b) 자동 revert** | 중 | ⚠️ T3 위반 위험 (자동 정책 변경) | ❌ 비권고 |
| **(c) 원본 보존 + 새 entry** ⭐ | 저 | 0 | ✅ **권고 (best)** — append-only 답습 |
| **(d) Dual write** | 고 | ⚠️ schema_version drift 위험 | ❌ 비권고 |

**MVP 권고 = (a) + (c) 결합**: **검증 실패 시 BLOCK + 원본 ledger 보존 + `event: migration_failed` 새 append-only entry** — git append commit 답습, 운영 부담 최소, T3 위반 0.

**운영 절차 권고**:
```
1. Migration script 실행 → 검증 실패 검출
2. BLOCK — migration 결과 import 차단
3. 원본 JSONL 보존 (변경 0)
4. 새 append-only entry 생성: {"event": "migration_failed", "result": "BLOCK", ...}
5. 사용자 alert + 명시 결정 후 다음 단계 (수정된 script 재실행 또는 archive)
```

---

## 2. 6 차원 평가

### 2.1 차원 1 — 11 필드 구조의 구현 가능성

#### 2.1.1 11 필드 enumeration 권고

본 Agent A 권고 (prequel §6.3 + G4 §4.2 + GPT enumeration 의 *교차 매핑*):

| # | 필드 | 자동? | 출처 |
|---|----|----|----|
| 1 | `ts` | ✅ | 모든 출처 일치 |
| 2 | `id` (UUID v4) | ✅ | G4 §4.2 + prequel §6.3 (`task_id`) |
| 3 | `event` | caller | prequel §6.3 + GPT |
| 4 | `agent` | ✅ | 모든 출처 일치 |
| 5 | `result` | caller | prequel §6.3 + GPT |
| 6 | `tool` 또는 `gate_id` | ✅ | GPT (G4 §4.2 미명시) |
| 7 | `scope` | ✅ | G4 §4.2 (prequel §6.3 / GPT 미명시) |
| 8 | `schema_version` | ✅ | G4 §4.2 (prequel §6.3 / GPT 미명시) |
| 9 | `evidence_refs` (array) | caller | G4 §4.2 |
| 10 | `prev_hash` | ✅ | 모든 출처 일치 |
| 11 | `hash` | ✅ | 모든 출처 일치 |

**11 필드 중 자동 = 7, caller 명시 = 4** (event / result / evidence_refs / 일부 tool).

#### 2.1.2 4 후보 (`event` / `signature` / `chain_id` / `parent_event_id`) 평가

본 Agent A 권고:
- `event` ⭐ **권고 (이미 prequel §6.3 + GPT enumeration 명시)** — 11번째가 아니라 *이미 1~10 핵심 필드의 일부*. ADR-012 schema 권고 본 §2.1.1 답습.
- `signature` — 옵션 1 (signed commit) 채택 시만 필요. 옵션 2 (git append) 권고 채택 시 *불필요*. **비권고 — 별도 필드 추가 부담**.
- `chain_id` — multi-chain 운영 시 (Global / Project Memory 별 chain) 의미. MVP Global+Project 2 chain 운영 시 *유의미* — `scope` 필드 (§2.1.1 #7) 가 chain 분리 충족 가능. **별도 필드 비권고** (scope 필드로 충분).
- `parent_event_id` — DAG ledger 운영 시 의미. MVP linear chain (prev_hash) 시 *불필요*. **비권고**.

**최종 권고**: 11번째 필드는 **별도 후보 추가 0건** — 본 §2.1.1 enumeration 의 11 필드 자체로 충족 (prequel §6.3 9 필드 + G4 §4.2 추가 `scope` + `schema_version` = 11).

#### 2.1.3 자동 생성 부담

11 필드 중 **caller 명시 4 (event / result / evidence_refs / 부분 tool)** 만 사용자 부담. 7 필드는 helper library (예: `evidence_ledger.py` 50 LOC) 로 자동 생성 가능. **운영 부담 LOW**.

### 2.2 차원 2 — Hash Chain 사양 보강의 구현 부담

#### 2.2.1 RFC 8785 JCS 채택 (§1.4 답습)

운영 가능, 부담 LOW. fallback `jq -S -c` 명시 권고.

#### 2.2.2 canonical JSON 위반 검출 자동화

CI 회귀 검증 가능 — `scripts/verify_canonical.py` 50 LOC + R-6 workflow 확장 (또는 신규 `evidence-ledger-canary.yml`). **부담 1일**.

#### 2.2.3 prev_hash 검증 실패 처리 (4 옵션)

| 옵션 | 운영 부담 | T3 위반 | 권고 |
|----|--------|----|----|
| BLOCK | 저 | 0 | ✅ 권고 (MVP) |
| WARN | 저 | 0 | ❌ (위반 silent 통과 위험) |
| 자동 fork | 고 | ⚠️ | ❌ |
| rollback (자동 revert) | 중 | ⚠️ T3 | ❌ |

**MVP 권고**: **BLOCK + 사용자 alert + 합의 결정**.

#### 2.2.4 Full Rewrite 방어 메커니즘 (4 후보)

| 후보 | 운영 부담 | 권고 |
|----|--------|----|
| signed tag | 중 (GPG 의존) | ❌ (SPOF) |
| annotated commit | 저 | ✅ 보조 |
| append-only file system | 매우 고 | ❌ (인프라 의존) |
| ledger external snapshot | 중 | ✅ 보조 (multi-host 시) |
| **git append-only branch + branch protection rule** ⭐ | 저 | ✅ **MVP 권고** |

**MVP 권고**: **git append-only branch + branch protection rule (force push 금지 + history rewrite 금지)** — GitHub 표준 기능, 5분 설정. multi-host 전환 시 *ledger external snapshot* 추가 의무 발동 트리거 (g2g3g4 C-K SPOF accepted risk 패턴).

### 2.3 차원 3 — Round-trip 검증 + Migration script 사양

#### 2.3.1 G4 §4.6 절차의 실 PoC 가능성

✅ 가능 — R2-5 (R-2 PoC) 답습 패턴. Docker isolation + canary inject + sha256 비교 = 1~2일 PoC.

#### 2.3.2 의미 보존 검증의 자동화 vs 사용자 review

- **자동화 가능 영역**: hash 비교 / 필드 enumeration / lossy_fields 검출
- **사용자 review 의무 영역**: *의미 보존* 자체 — 어느 필드 손실이 *허용 가능한지* 결정. T2 ADR-011 §2.4 답습.

**권고**: ADR-012 본문에 **"의미 보존 review 자동화 절대 금지 (T2)"** 명시.

#### 2.3.3 `event: roundtrip_lossy` ledger entry 형식 사양 (§1.5 답습)

본 §1.5 권고 답습. `actual.lossy_fields` 추가 1 필드.

#### 2.3.4 Migration / Export / Import 검증 실패 시 Rollback 조건 (§1.6 답습)

**MVP 권고**: **(a) BLOCK + (c) 원본 보존 + 새 `event: migration_failed` entry**.

### 2.4 차원 4 — Signed Commit vs Git Append Commit (§1.3 답습)

**MVP 권고**: **옵션 2 (git append commit + branch protection rule)** — 1인 개발자 + 동일 호스트 SPOF 환경에 가장 단순.

**multi-host 전환 시**: 옵션 3 (둘 다) 의무 발동 트리거.

### 2.5 차원 5 — Implementation / Runtime PASS 영역 분리

#### 2.5.1 본 PR-2 *Design/Governance Gate PASS* 한정 영역

본 PR-2 가 *사양화* 가능한 범위:
- ADR-012 본문 (11 필드 schema + 보호 원칙 + append-only + hash chain + signed/append 선택 + JCS 채택 + roundtrip lossy 형식 + migration rollback 조건)
- G4 §4.4 본문 보강 (RFC 8785 JCS 인용 + Unicode NFC + numeric 정규화 명확 + prev_hash 검증 실패 처리 + full rewrite 방어)
- G4 §4.6 본문 보강 (rollback 조건 명시 + roundtrip_lossy ledger entry 형식)

#### 2.5.2 Implementation/Runtime PASS 영역 (별도 합의)

다음은 본 PR-2 범위 외:
- 실 `evidence_ledger.py` 구현 (50~100 LOC)
- 실 hash chain validator (`scripts/verify_ledger.py`)
- 실 migration script (`scripts/hermes-migration/*.py`)
- 실 round-trip PoC (R2-5 답습)
- CI workflow 신규 또는 R-6 확장 (`evidence-ledger-canary.yml`)
- branch protection rule 실제 설정 + GPG 키 등록 (옵션 1 채택 시)

#### 2.5.3 1인 개발자 + 메타-템플릿 + 4 게이트 모두 Implementation PASS 미충족 현실

**현 상태** (2026-05-09):
- G1b: Implementation/Runtime PASS = 1/4 ✅
- G2/G3/G4: Design/Governance Gate PASS (Bundled) = 3/4
- ADR-012: 본 PR-2 진입 시점 = Design/Governance Gate PASS 후보

**ADR-012 의 운영 부담** (1인 개발자 메타-템플릿):
- ADR-012 본문 작성 = 1일
- G4 §4.4 / §4.6 보강 = 0.5일
- 합의 보고서 = 0.5일
- PR 묶음 = 0.5일
- **합산 2.5일 (Design/Governance Gate PASS 한정)**
- Implementation/Runtime 영역 (별도 합의) = 5~7일 (§2.5.2 합산)

**부담 정당성 평가**:
| 평가 차원 | 결과 |
|---------|----|
| 현 1인 개발자 스케일 대비 | **무거움** — 7~10일 합산 |
| 메타-템플릿 답습 가정 대비 | **합리적** — 한 번 발생, 분산 |
| Hermes PMO 격상 후 자동화 가치 | **장기적으로 정당** — Evidence Ledger 는 모든 PASS 판정의 권위 근거 |
| 현 4 게이트 1/4 Implementation PASS 미충족 현실 | **비례 적정** — Design/Governance Gate PASS 만 본 PR-2, Implementation 은 별도 |

### 2.6 차원 6 — ADR-008/009/010/011 cross-reference 영향

#### 2.6.1 ADR-008 차단조건 #2 (JSONL export 표준) 와 ADR-012 cross-reference

ADR-008 부록 A.2 = "Hermes JSONL Export 검증" — *export 가능성* 검증. ADR-012 = *Evidence Ledger 보호 강화* — Hermes export 가 사용하는 *형식 보장*. **Cross-reference 위치**: ADR-012 §1.X (관련 ADR) + ADR-008 부록 B (Amendment) cross-reference 권고. 단, **ADR-008 본문 자동 갱신 금지** (사용자 명시 답습) — cross-reference 만.

#### 2.6.2 ADR-011 §2.1 (a)~(d) 4조건 + 합의 APPROVE (e) 패턴 답습

ADR-012 본문은 **(a)~(e) 5조건 패턴 답습**:
- (a) 동등 이상의 보안 결과 — Evidence Ledger 무결성 보장 (변조 검출 + append-only)
- (b) 격리 환경 PoC 실증 — 라운드트립 PoC + canary inject (별도 합의)
- (c) ADR / SDD 권위 명시 — 본 ADR-012 자체 + G4 §4.4 / §4.6 cross-reference
- (d) 자동 회귀 검증 경로 확보 — CI workflow (별도 합의)
- (e) 합의 APPROVE — 본 PR-2 풀 3+1 합의

#### 2.6.3 ADR-009 (자체 Adapter v2.0) cross-reference

ADR-009 진입 조건 검증 시 Evidence Ledger entry 의무 — ADR-012 가 *형식 정의*. **Cross-reference 권고**.

#### 2.6.4 ADR-010 (SQLCipher Vault) cross-reference

ADR-010 = SQLCipher 키 관리 (secret 처리). Evidence Ledger 의 secret 처리 cross-reference:
- Evidence Ledger entry 자체에 secret 포함 금지 — Tier-1 42 catalog 답습 (G2 GP-1 + GP-2)
- Evidence Ledger 는 *plain JSONL* (SQLite 미사용) — SQLCipher 미적용 영역. *이중 보호 미필요* — Evidence 자체가 *공개 검증 대상*.

**잠재 risk**: 사용자가 *secret 포함 evidence* 작성 시 — Evidence Ledger 가 secret 평문 저장 위험. **권고**: ADR-012 본문에 **"Evidence Ledger entry 작성 시 Tier-1 42 catalog 적용 강제 (GP-2 답습)"** 명시.

---

## 3. 식별된 위험 / 의존성 / 운영 부담

본 Agent A 가 운영 가능성 관점에서 식별한 risk / gap (R-N 형식 — g2g3g4 합의 Agent A R-1 ~ R-10 답습 형식):

| # | 위험 / Gap | 등급 | 처리 권고 |
|---|---------|----|--------|
| **R-1** | 11 필드 enumeration 의 *어느 11번째* 결정 부재 — 본 Agent A §2.1.1 권고 (`event` / `signature` / `chain_id` / `parent_event_id` 모두 비권고, prequel §6.3 9 필드 + G4 §4.2 +scope+schema_version = 11) 와 GPT g2g3g4 §4.4 enumeration 차이 존재 | **MEDIUM** | ADR-012 본문에서 단일 정합 schema 명시 — Reviewer 종합 영역 |
| **R-2** | RFC 8785 JCS 채택 시 라이브러리 의존 추가 — G4 §4.3 *표준 라이브러리만* 위반 risk | **LOW** | fallback `jq -S -c` 명시 (§1.4 답습) — JCS 라이브러리 미보유 환경에서도 hash 일치 |
| **R-3** | signed commit 옵션 1 채택 시 GPG 키 자체가 SPOF — 1인 동일 호스트 환경 | **MEDIUM** | MVP 옵션 2 (git append) 권고 (§1.3 답습), multi-host 전환 시 옵션 3 의무 발동 트리거 |
| **R-4** | 의미 보존 검증의 자동화 시도 risk — T2 ADR-011 §2.4 위반 위험 | **MEDIUM** | ADR-012 본문에 "의미 보존 review 자동화 절대 금지" 명시 |
| **R-5** | Migration 검증 실패 시 자동 revert 또는 dual write 채택 risk — T3 위반 또는 schema_version drift | **MEDIUM** | (a) BLOCK + (c) 원본 보존 + 새 entry 권고 (§1.6 답습) |
| **R-6** | Evidence Ledger entry 자체에 secret 평문 저장 risk — Tier-1 42 catalog 미적용 시 | **HIGH** | ADR-012 본문에 GP-2 답습 강제 명시 (§2.6.4 답습) |
| **R-7** | Full rewrite 방어 — branch protection rule 미설정 시 history rewrite 차단 부재 | **HIGH** | MVP 권고 git append-only branch + branch protection rule (§2.2.4 답습) — Implementation 영역, PoC 진입 시점 의무 |
| **R-8** | ADR-012 / G4 §4.4 / §4.6 갱신의 동시 PR 묶음 부재 시 cross-reference drift risk | **MEDIUM** | 본 PR-2 = ADR-012 + G4 §4.4 + §4.6 + 합의 보고서 *동일 PR 묶음* 의무 |
| **R-9** | Evidence forgery 방지 (G2 §1.2.5 P10 deferred candidate) cross-reference 부재 risk | **MEDIUM** | ADR-012 본문에 P10 cross-reference (P10 정식 등록 시점 = ADR-012 발행 시점 답습 — g2g3g4 합의 §3.7) |
| **R-10** | 11 필드 schema 진화 정책 (필드 추가/제거/이름 변경/타입 변경) 부재 risk — G4 §10 §11.4.1 답습 미답습 시 | **LOW** | ADR-012 본문에 §10 schema 진화 정책 답습 — semver MAJOR/MINOR 분리 |
| **R-11** | 외부 LLM 1+ 충족 여부 — 본 PR-2 풀 3+1 의 메타 편향 통제 binary 조건 (g2g3g4 합의 C-T 답습) | **HIGH** | **본 PR-2 합의에서 외부 LLM 의견 의뢰 + 수집 의무화** |
| **R-12** | 메타-순환 청산 — ADR-012 자체가 자기 작성 산출 (Claude 패밀리 검토) risk | **MEDIUM** | g2g3g4 합의 C-J 메타-순환 청산 패턴 답습 — 외부 LLM evidence 명시 |

**HIGH 위험 3건 (R-6, R-7, R-11)** = 본 PR-2 PASS 의 binary 조건. **MEDIUM 6건 (R-1, R-3, R-4, R-5, R-8, R-9, R-12)** = PASS 후 흡수 가능. **LOW 2건 (R-2, R-10)** = ADR-012 본문 흡수.

---

## 4. 권고 조건 (조건부 APPROVE 시 명시)

본 Agent A 가 **APPROVE WITH CONDITIONS** 판정의 8 조건 enumeration:

1. **외부 LLM 1+ 의견 수집** (R-11) — g2g3g4 합의 C-T 답습. GPT cross-vendor + Claude 인접 컨텍스트 = 2건 권고.
2. **11 필드 schema 단일 정합 명시** (R-1) — ADR-012 본문에서 prequel §6.3 + G4 §4.2 + GPT enumeration 의 *교차 매핑* 결과 단일 schema 명시. 본 Agent A §2.1.1 권고 (11 필드 = ts/id/event/agent/result/tool/scope/schema_version/evidence_refs/prev_hash/hash) 검토 영역.
3. **Signed commit OR git append commit MVP 옵션 결정** (R-3) — 본 Agent A 권고 = 옵션 2 (git append + branch protection rule). multi-host 전환 시 옵션 3 의무 발동 트리거 명시.
4. **RFC 8785 JCS 채택 + fallback 명시** (R-2) — `jq -S -c` 동등 동작 명시 (Unicode NFC 제외).
5. **`event: roundtrip_lossy` ledger entry 형식 사양 명시** (§1.5 답습) — `actual.lossy_fields` 추가 + 의미 보존 review 자동화 절대 금지 명시 (R-4).
6. **Migration 검증 실패 시 rollback 조건 = (a) BLOCK + (c) 원본 보존 + 새 entry** (R-5) — `event: migration_failed` 형식 사양.
7. **Evidence Ledger entry 작성 시 Tier-1 42 catalog 적용 강제** (R-6) — GP-2 답습 명시.
8. **ADR-012 + G4 §4.4 + §4.6 + 합의 보고서 동일 PR 묶음 의무** (R-8) — cross-reference drift 차단.

**P0 조건 (필수, PR-2 PASS 차단)**:
- 조건 1 (외부 LLM 1+) — 본 합의 시점 충족 명시
- 조건 7 (Tier-1 catalog 강제)
- 조건 8 (PR 묶음 의무)

**P1 조건 (강력 권고, PR-2 PASS 직후 흡수)**:
- 조건 2 (11 필드 schema)
- 조건 3 (signed/append 결정)
- 조건 5 (roundtrip_lossy 형식)
- 조건 6 (migration rollback 조건)

**P2 조건 (PASS 후 별도 합의 가능)**:
- 조건 4 (JCS 채택 + fallback) — Implementation 시점

---

## 5. 영구 핵심 제약 보호 점검 (5 제약)

본 PR-2 가 *답습해야 하는* 5 영구 핵심 제약 점검:

| 제약 | 권위 근거 | 본 PR-2 보호 위치 | 점검 결과 |
|------|--------|-----------|--------|
| **Provider Liquidity** (헌법 5조 관용) | 헌법 5조 + ADR-008 차단조건 #2 + G4 §3.5 + §4.3 + §6.4 (4-way) | ADR-012 11 필드 schema 의 *agent* 필드 = provider-neutral identifier (`user`/`Hermes`/`Worker_X`). Provider lock-in 차단 답습 | ✅ PASS — provider 중립 schema |
| **Hermes ≠ root of trust** (ADR-011 §2.3) | ADR-011 §2.3 영구 권위 | ADR-012 = Hermes 출력의 *Tools 검증* 권위 근거. Hermes 가 자기 ledger entry 작성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 | ✅ PASS — Hermes 검증 대상 답습 |
| **메타포 강제 금지** (system-identity-prequel §7) | prequel §7 (P2 v3 §10 흡수) | ADR-012 = *Evidence Ledger* 메타포 답습 — 회사 메타포 ("기록 체계") 의 활용 한정 (강제 인플레이션 0). 11 필드 schema 자체가 *기존 prequel §6.3 + G4 §4.2* 답습, 신규 발명 0 | ✅ PASS — 메타포 강제 0 |
| **자동 정책 변경 금지 (T3)** (ADR-011 §2.4) | ADR-011 §2.4 | ADR-012 본문 변경 = 풀 3+1 합의 + ADR Amendment 절차 (T3). Hermes 자동 ledger entry 작성 = T1 (자동 학습) — *정책 변경 아님*. Migration 검증 실패 시 rollback = BLOCK + 사용자 명시 (T2), 자동 revert 비권고 (T3 위반 위험) | ✅ PASS — T1/T2/T3 분리 답습 |
| **수단/목적 분리 원칙** (ADR-011 §2.1 (a)~(d) 4조건) | ADR-011 §2.1 | ADR-012 = *Evidence Ledger 보호 강화* — 수단 (hash chain / signed-or-append commit / JCS / Tier-1 catalog) 자유, 목적 (변조 차단 + 무결성 + Provider Liquidity) 검증 의무. (a)~(e) 5조건 답습 (§2.6.2) | ✅ PASS — (a)~(e) 5조건 답습 |

**5 영구 핵심 제약 모두 보호됨** (5/5).

---

## 6. 본 입력이 *하지 않는* 것 (사용자 명시 답습)

본 Agent A 입력은 다음 모두 *발생시키지 않는다*:

1. ❌ **Hermes PMO 격상 선언** — 본 PR-2 풀 3+1 합의 PASS ≠ Hermes PMO 격상. 격상은 별도 합의 + 사용자 명시 결정 + 외부 LLM 1+ 필수
2. ❌ **P2 v3 정식 채택 자동 선언** — 본 PR-2 ≠ P2 v3 정식 채택. P2 v3 헤더 DRAFT 그대로 유지
3. ❌ **ADR-008 / 009 / 010 / 011 본문 자동 갱신** — cross-reference 만 가능 (§2.6 답습). 본문 변경은 별도 PR
4. ❌ **P2 v2 / system-identity-prequel.md archive 자동 처리** — 별도 사용자 명시 결정
5. ❌ **실 runtime code / migration script 구현** — `evidence_ledger.py` / `verify_ledger.py` / `scripts/hermes-migration/*.py` 모두 본 PR-2 범위 외 (Implementation/Runtime PASS 별도 합의)
6. ❌ **Tier-2 / Tier-3 catalog 자동 확장** — 별도 합의
7. ❌ **다른 Agent (B, C) 출력 참조** — 본 입력은 Agent A 단독 분석. Reviewer 종합 영역
8. ❌ **메타포 강제** — system-identity-prequel §7 답습. Evidence Ledger 메타포 활용 한정, 강제 인플레이션 0
9. ❌ **단일 권위 판정** — 본 입력의 APPROVE / BLOCK 판정은 *Agent A 관점에서의 판정*. 합의 본부는 Reviewer 종합 + 외부 LLM 1+ 영역

---

## 7. 최종 판정

```
APPROVE WITH CONDITIONS
```

### 7.1 핵심 조건 1줄 요약

**PR-2 (ADR-012 신규 발행 + G4 §4.4/§4.6 hash chain 사양 보강) 풀 3+1 합의 진입 적격 — 8 조건 (외부 LLM 1+ + 11 필드 단일 schema + signed/append 결정 + JCS+fallback + roundtrip_lossy 형식 + migration rollback 조건 + Tier-1 catalog 강제 + PR 묶음 의무) 충족 시 APPROVE.**

### 7.2 판정 근거

운영 가능성 측면에서 PR-2 6 핵심 산출 (11 필드 schema / hash chain 보강 / signed-or-append commit 의무 / RFC 8785 JCS 채택 / round-trip lossy / migration rollback) 모두 *Design/Governance Gate PASS* 수준에서 사양화 가능 + 신규 발명 0건 + 기성 도구 (sha256 / canonical JSON / git pre-commit hook / branch protection rule / `jq`) 답습 + 1인 개발자 메타-템플릿 부담 합산 2.5일 (사양 한정, Implementation 별도 5~7일).

5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / 자동 정책 변경 금지 T3 / 수단/목적 분리) 모두 보호 (5/5).

### 7.3 본 판정의 한계

- 본 Agent A 는 *다른 Agent (B, C) 출력 미참조* — 보안 / 품질 / 대안 측면 미평가. Reviewer 종합 시 보강.
- 본 Agent A 는 *자기 작성 산출 자기 검토* (G4 §4.4 작성 컨텍스트와 동일). 외부 LLM 의견은 본 Agent A 대체 불가 (R-11 + R-12).
- 운영 부담 추정 (2.5일 사양 + 5~7일 Implementation = 7~10일 합산) 은 *메타-템플릿 작성 자체* 한정 — 메타-템플릿 사용 새 프로젝트마다 발생하는 운영 비용은 별도 계산.
- 11 필드 단일 정합 schema 는 본 §2.1.1 권고 — Reviewer 종합 + 외부 LLM 1+ 검토 영역 (단일 권위 아님).

---

**작성일**: 2026-05-09
**작성자**: Agent A (구현/운영 가능성 분석가)
**판정**: ✅ **APPROVE WITH CONDITIONS** (8 조건 — §4)
**핵심 조건 1줄 요약**: PR-2 풀 3+1 합의 진입 적격 — 외부 LLM 1+ + 11 필드 단일 schema + signed/append 결정 + JCS+fallback + roundtrip_lossy 형식 + migration rollback 조건 + Tier-1 catalog 강제 + PR 묶음 의무 8 조건 충족 시 APPROVE.
**상위 Reviewer 인계 사항**:
- HIGH 위험 3건 (R-6 Tier-1 catalog 강제, R-7 branch protection rule 의무, R-11 외부 LLM 1+ 충족) 은 본 PR-2 PASS 의 binary 조건
- MEDIUM 6건 (R-1 11 필드 schema, R-3 signed/append, R-4 의미 보존 review 자동화 금지, R-5 migration rollback, R-8 PR 묶음, R-9 P10 cross-ref, R-12 메타-순환 청산) 은 PASS 후 흡수 가능
- LOW 2건 (R-2 JCS fallback, R-10 schema 진화 정책) 은 ADR-012 본문 동시 흡수
- 본 Agent A 는 *운영 가능성* 측면 한정 — 보안 (Agent B) / 대안 (Agent C) / 외부 LLM 검증 종합 의무
