# G4 JSONL Hash Chain + RFC 8785 JCS + Round-trip — Group C 통합 PoC 사양

> **상태**: DRAFT (2026-05-10, Group C 진입 — JSONL hash chain + RFC 8785 JCS canonicalization + round-trip validation 통합 PoC)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §4.1 (G4 7 영역 — Order 3 tie 3건: hash chain / JCS / round-trip)
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.3 (Append-only + Hash Chain 다층 강제) / §2.5 (RFC 8785 JCS Primary + jq fallback) / §2.6 (Genesis Hash) / §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry) / §2.9 (3 ledger entry 형식 — `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §4.2 (11 필드 schema — `event` 11번째 필드 신규) / §4.4 (hash chain 보강) / §4.6 (round-trip 검증 절차 — Tier-based)
> **PASS 조건 답습**: `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), 사용자 명시 4 결정 (Q1 rfc8785+pyjcs 병렬 / Q2 24개 / Q3 6 영역 / Q4 Q1 풀 3+1 + Q2/Q3 단축)
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance PASS ↔ Implementation/Runtime PASS 분리 매트릭스), P2 v3 §3.1.4 (Implementation Pending 표), ADR-008 차단조건 #2 (Evidence Ledger = Hermes 의존 0)
> **답습 시제**: Group A 1차 (`g2-gp5-provider-adapter-enforcement-poc.md`) + Group A 2차 (`g2-gp5-poc2-import-linter-implementation.md`) + Group B (`g3-evidence-pass-gate-poc.md`) 산출물 형식

---

## 0. 목적

본 PoC 는 G4 *Provider-agnostic Memory/Skill 형식* 의 **Evidence Ledger 무결성 layer** 첫 시제 — JSONL ledger entry 형식의 형식적 무결성을 3 축에서 통합 검증:

1. **Hash chain** — `prev_hash` ↔ `hash` chain 의 sha256 + canonical JSON 일관성 검증 (ADR-012 §2.3 Layer 1 답습)
2. **RFC 8785 JCS canonicalization** — Provider-neutral 형식 표준 (Primary `rfc8785` + `pyjcs` 병렬 → 1개 채택, Fallback `jq -S -c`) (ADR-012 §2.5 답습)
3. **Round-trip validation** — JSONL export → 재 import → 재 export 가 hash 일치 (T2 strict) 또는 의미 보존 + lossy entry (T3) 검증 (ADR-012 §2.9 + G4 §4.6 답습)

본 PoC 는 **형식적 무결성 한정** (ADR-012 §11 한계 답습) — *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 PoC 방어 범위 외.

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §4.1 + ADR-012 §2 + G4 §4 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` | PoC 사양 + 답습 매핑 + Evidence 5형식 + RA-9 부록 |
| Canonical JSON 모듈 | `tools/canonical_json.py` | RFC 8785 JCS Primary — `rfc8785` (Trail of Bits) + `jcs` (titusz) 병렬 cross-check (사용자 결정 갱신 답습 — RA-9 §B.3) + `jq -S -c` fallback + `event: canonical_json_fallback` ledger entry 자동 작성 |
| JSONL hash chain 검증기 | `tools/jsonl_hash_chain.py` | 11 필드 schema 검증 + `prev_hash` ↔ `hash` chain 검증 + Genesis hash + chain violation 검출 + `event: chain_violation_detected` 자동 작성 |
| Round-trip 검증기 | `tools/jsonl_roundtrip.py` | export → import → re-export hash 비교 (T2 strict) + 의미 보존 + lossy 영역 + `event: roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` 3 형식 ledger entry 자동 작성 (ADR-012 §2.9 답습) |
| Test corpus (24개) | `tests/canonical/{unicode,number,key_ordering,escape,nested,array,hash_stability,lossy}/{01,02,03}.{json,canonical,sha256}` | 8 카테고리 × 3 = 24 reference output. ADR-012 §2.5 ≥20개 답습 |
| PASS fixture × 2 | `tests/fixtures/jsonl_ledger/pass/{minimal_chain, roundtrip_t2_strict}.jsonl` | Genesis + 2 entry chain / round-trip T2 hash 일치 |
| FAIL fixture × 4 | `tests/fixtures/jsonl_ledger/fail/{prev_hash_mismatch, hash_recalculation, missing_event_field, roundtrip_lossy_no_entry}.jsonl` | 4 chain violation 패턴 cover (ADR-012 §2.7 violation_type 답습) |
| CI workflow | `.github/workflows/g4-hash-chain.yml` | PASS/FAIL 양방향 + corpus 회귀 + round-trip nightly + Evidence summary |
| Reviewer-only 단축 합의 (Q2/Q3) | `docs/review/3plus1-consensus-2026-05-XX-g4-corpus-poc-scope-short.md` | corpus 24개 + PoC 6 영역 사양 검토 + escalation 0/N |
| 풀 3+1 합의 (Q1) | `docs/review/3plus1-consensus-2026-05-XX-g4-jcs-library-selection.md` | rfc8785 vs pyjcs Primary 1개 채택 + jq fallback + RA-9 evidence 흡수 |

### 1.2 제외 (별도 합의 영역 — 사용자 명시 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| 실 migration script (`hermes_to_claude.py` / `hermes_to_openai.py` 등) 본 구현 | **사용자 명시 금지** — Group H 영역 (ADR-014 발행 trigger 후 별도 합의, roadmap §3.4 답습) |
| Memory boundary hook (4 금지 강제) | Group G 영역 — roadmap §4.1 답습 |
| Skill wrapper (`forbidden_actions` 강제) | Group G 영역 — roadmap §3 답습 |
| `provider_bindings` lint rule | G2 GP-5 통합 — Group A 답습 |
| Memory/Skill schema validation (pydantic) | Group E 영역 — roadmap §4.1 답습 |
| Full Rewrite 5 Layer 방어 (ADR-012 §2.8) | 별도 PoC — git append commit + signed commit + branch protection 영역 |
| 실 SQLCipher BEFORE INSERT trigger 활성화 | G1b 답습 영역 (이미 PASS) |
| Hermes PMO 격상 선언 | **사용자 명시 금지** — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 또는 인간 리뷰 + 사용자 명시 결정 후 별도 |
| ADR 본문 자동 갱신 | **사용자 명시 금지** — 별도 PR 묶음 합의 영역 |
| G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 | **사용자 명시 금지** — 본 PoC = G4 *부분 충족 시제* 한정 |

---

## 2. JSONL Ledger Entry Schema (11 필드 — G4 §4.2 답습)

```json
{
  "type": "memory|skill|meta",
  "scope": "global|project|session",
  "id": "<uuid>",
  "schema_version": "0.1",
  "ts": "2026-05-10T12:00:00Z",
  "agent": "user|claude-code|hermes|external_llm",
  "event": "<17 enum 후보 중 1>",
  "content": {...},
  "evidence_refs": ["docs/evidence/<task-id>.md"],
  "prev_hash": "<sha256>",
  "hash": "<sha256>"
}
```

### 2.1 본 PoC 의무 검증 필드 11개

| # | 필드 | 검증 |
|---|------|------|
| 1 | `type` | enum (`memory` / `skill` / `meta`) |
| 2 | `scope` | enum (`global` / `project` / `session`) |
| 3 | `id` | string (UUID v4 권고, 본 PoC 형식 검증만) |
| 4 | `schema_version` | semver, MVP `0.1` 한정 (외 BLOCK — ADR-012 §2.10 답습) |
| 5 | `ts` | ISO 8601 + monotonicity (본 entry `ts` ≥ `prev_hash` entry `ts` — ADR-012 §3.4 답습) |
| 6 | `agent` | enum (`user` / `claude-code` / `hermes` / `external_llm`) |
| 7 | `event` | enum 17 후보 중 1 (ADR-012 §2.2 답습 — 본 PoC MVP 4종 한정 검증: `canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) |
| 8 | `content` | object (canonical JSON 적용 대상) |
| 9 | `evidence_refs` | array of string (path) |
| 10 | `prev_hash` | sha256 hex (첫 entry = `genesis_hash` — §3.3 답습) |
| 11 | `hash` | sha256 hex (본 entry canonical JSON sha256) |

### 2.2 hash 계산 정의

```
hash = sha256(canonical_json({본 entry - "hash" field 자체}))
```

- `hash` 필드 자체는 canonical JSON 입력에서 제외 (recursive 회피)
- canonical JSON = §3 RFC 8785 JCS Primary + `jq -S -c` Fallback

---

## 3. Canonical JSON — RFC 8785 JCS Primary + Fallback (ADR-012 §2.5 답습)

### 3.1 Primary 채택

**Q1 사용자 명시 결정 갱신 답습** (2026-05-10, RA-9 §B.3 발견 후) — `rfc8785` 0.1.4 (Trail of Bits, Apache-2.0) + `jcs` 0.2.1 (titusz, Apache-2.0) **병렬 corpus 24개 cross-check** 채택. 본 PoC 는 *두 라이브러리 모두 사용* — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제. 양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2 trigger).

> **사용자 명시 원본 후보 폐기 사유** (RA-9 §B.3 답습): `pyjcs` = PyPI 미존재 (`No matching distribution found`). 대안 `jcs` (titusz) PyPI 발굴 + 11/11 sanity vector 동등성 PASS — 사용자 명시 결정 갱신으로 흡수.

본 사양 §B (RA-9 사전 검증 evidence) + Q1 풀 3+1 합의 보고서 (`docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 권위 답습.

### 3.2 Fallback — `jq -S -c`

```bash
jq -S -c . input.json
```

- `-S` lex sort + `-c` compact + UTF-8 (POSIX 표준 답습)
- 사용 시 `event: canonical_json_fallback` ledger entry 자동 작성 의무 (ADR-012 §2.5 답습)
- subprocess overhead — Primary 사용 권고, Fallback 은 Primary 라이브러리 install 실패 시 한정

### 3.3 Genesis Hash (MVP — schema_version 0.1)

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

ADR-012 §2.6 답습. schema_version 0.2 진입 시 새 chain (별도 `chain_id` 또는 `schema_version`) 생성 정책은 별도 합의.

### 3.4 corpus 24개 (Q2 결정 답습 — 8 카테고리 × 3)

| 카테고리 | 디렉토리 | case 3개 (각 카테고리) |
|----------|----------|----------------------|
| unicode | `tests/canonical/unicode/` | 한글 NFC / 일본어 카타카나 / Emoji surrogate pair (BMP 외부 codepoint U+1F600 등) |
| number normalization | `tests/canonical/number/` | `1.0` vs `1` (ECMA-262 IEEE 754) / `1e10` vs `10000000000` / `-0` vs `0`. NaN/Infinity 입력 = reject (corpus 별도 reject case 2건 추가 의무 — Q1 합의 C-B8 답습, `nan_reject.json` + `inf_reject.json`, 양 라이브러리 모두 reject 검증) |
| object key ordering | `tests/canonical/key_ordering/` | flat key 다수 (sort) / 비-ASCII key (UTF-16 codepoint 순) / 숫자 형 key (ASCII 순) |
| escape handling | `tests/canonical/escape/` | ` `~`` control chars / ` ` line separator / `"`, `\\`, `/` |
| nested object | `tests/canonical/nested/` | depth 3 / depth 10 / mixed dict+list 교차 |
| array | `tests/canonical/array/` | empty `[]` / homogeneous `[1,2,3]` / heterogeneous mixed type `[1,"a",true,null,{"k":1}]` |
| hash stability | `tests/canonical/hash_stability/` | 동일 입력 100회 → 동일 hash / key 입력 순서 무관 / whitespace 무관 |
| lossy round-trip | `tests/canonical/lossy/` | float precision loss / unicode normalization (NFC vs NFD) / number→string |

**각 case 3 파일**:
- `<case>.json` — 입력 JSON
- `<case>.canonical` — 기대 canonical JSON (RFC 8785 reference output)
- `<case>.sha256` — 기대 sha256 hex

**CI 회귀**: `rfc8785(input) == expected.canonical` + `sha256(canonical) == expected.sha256` + `jq -S -c fallback` 동등성 비교.

---

## 4. Validator 동작 명세

### 4.1 `tools/canonical_json.py`

```
입력: JSON dict / list (Python object)
출력: canonical bytes (UTF-8)
실패 처리: Primary 라이브러리 ImportError → Fallback `jq -S -c` subprocess + `canonical_json_fallback` ledger entry 자동 작성
```

API:
```python
def to_canonical(obj: Any) -> bytes: ...
def to_canonical_with_fallback(obj: Any, ledger_writer) -> bytes: ...
```

### 4.2 `tools/jsonl_hash_chain.py`

검사 1 — **Schema validation** (11 필드 존재 + 형식):
- 누락 필드 → BLOCK (특히 `event` 필드 누락 = ADR-012 §2.2 답습)
- `schema_version != "0.1"` → BLOCK (ADR-012 §2.10 답습)

검사 2 — **Genesis hash 검증**:
- 첫 entry 의 `prev_hash` == `genesis_hash(scope, schema_version)` 일치

검사 3 — **Hash chain 검증**:
- 각 entry 의 `hash` == sha256(canonical_json(entry - "hash"))
- 각 entry 의 `prev_hash` == 직전 entry 의 `hash`
- 불일치 검출 시 → BLOCK + `chain_violation_detected` ledger entry 자동 작성 (ADR-012 §2.7 답습, violation_type 4종: `prev_hash_mismatch` / `hash_recalculation` / `history_rewrite` / `genesis_mismatch`)

검사 4 — **Timestamp monotonicity**:
- 본 entry `ts` ≥ `prev_hash` entry `ts` (ADR-012 §3.4 답습)

종료 코드:
- 0 = 모든 검사 PASS
- 1 = 1+ violation (위반 entry id + violation_type 출력)

### 4.3 `tools/jsonl_roundtrip.py`

```
입력: JSONL ledger 파일 (path)
절차:
  1. JSONL parse → Python list of dict
  2. canonical re-export → bytes
  3. SHA-256 비교 (export 1 vs export 2)
  4. T2 strict (hash 일치 100%) → `roundtrip_pass` ledger entry 작성
  5. 의미 보존 (lossy 영역 명시) → `roundtrip_lossy` ledger entry 작성 (lost_fields enumeration 자동)
  6. parse 실패 / 의미 보존 실패 → `roundtrip_fail` ledger entry 작성
출력: ledger entry 3 형식 중 1 + 종료 코드
```

본 PoC 는 **JSONL → JSONL 동일 형식 round-trip** 한정. 외부 형식 (Hermes / Claude / OpenAI) ↔ JSONL migration 은 **Group H 영역** (사용자 명시 금지 답습).

종료 코드:
- 0 = T2 strict PASS
- 1 = T3 lossy (lossy entry 자동 작성)
- 2 = T2/T3 모두 실패 (`roundtrip_fail` entry 자동 작성)

---

## 5. Fixture 명세

### 5.1 PASS × 2

| 파일 | 내용 |
|------|------|
| `pass/minimal_chain.jsonl` | Genesis (entry 1) + 2 후속 entry. 11 필드 + 정확한 `prev_hash` chain + `event: memory_write` |
| `pass/roundtrip_t2_strict.jsonl` | 위 + canonical JSON re-export 시 hash 100% 일치 |

### 5.2 FAIL × 4 (chain violation 4 패턴 cover)

| 파일 | violation_type | 기대 detection |
|------|---------------|---------------|
| `fail/prev_hash_mismatch.jsonl` | `prev_hash_mismatch` | entry 2 의 `prev_hash` 가 entry 1 의 `hash` 와 불일치 |
| `fail/hash_recalculation.jsonl` | `hash_recalculation` | entry 2 의 `hash` 가 sha256(canonical(entry 2 - "hash")) 와 불일치 |
| `fail/missing_event_field.jsonl` | (schema BLOCK) | `event` 11번째 필드 누락 → BLOCK (chain 검증 진입 전) |
| `fail/roundtrip_lossy_no_entry.jsonl` | (round-trip 영역) | lossy round-trip 발생 시 `roundtrip_lossy` entry 미작성 → BLOCK |

---

## 6. CI workflow 명세 (`.github/workflows/g4-hash-chain.yml`)

| step | 책무 | 종료 |
|------|------|------|
| setup | Python 3.11+ + `rfc8785==0.1.4` install + `jcs==0.2.1` install (Q1 합의 R-A2 답습 — 양 라이브러리 cross-check 강제) + `jq` install | 실패 시 BLOCK |
| corpus 회귀 (Primary 1) | `tests/canonical/**/*.json` 24개 → `rfc8785.dumps(input) == expected.canonical` 100% | 실패 시 rc=1 |
| corpus 회귀 (Primary 2 cross-check) | `tests/canonical/**/*.json` 24개 → `jcs.canonicalize(input) == rfc8785.dumps(input)` 100% (Q1 합의 corpus 시점 cross-check 강제 답습 — TR-C-2 trigger) | 실패 시 rc=1 + escalation |
| fallback 동등성 | `rfc8785` vs `jq -S -c` 24개 동등 | 실패 시 rc=1 (Q1 합의 trigger fallback 충돌) |
| PASS fixture | `pass/*.jsonl` × 2 → `jsonl_hash_chain.py` rc=0 | 실패 시 BLOCK |
| FAIL fixture | `fail/*.jsonl` × 4 → `jsonl_hash_chain.py` rc=1 + 4 violation_type cover | 실패 시 BLOCK |
| Round-trip | `pass/roundtrip_t2_strict.jsonl` → `jsonl_roundtrip.py` rc=0 | 실패 시 BLOCK |
| Evidence summary | corpus 24/24 + chain 4/4 cover + round-trip T2 + fallback 동등성 | summary text → CI artifact |
| probe cleanup | `if: always()` step 분리 (Group A G-1 답습) | — |

---

## 7. 답습 강제 조건 매트릭스

| 영역 | 답습 출처 | 본 PoC 적용 |
|------|----------|------------|
| ADR-011 §2.1 (a) 결과 동등성 | 헌법 8조 본질 = "Evidence 무결성 결과" | corpus 24개 + chain 4 violation cover |
| ADR-011 §2.1 (b) 격리 환경 PoC | R-2 / R-4.1 답습 | venv 격리 (`.poc-prep/jcs-ra9-venv/`) + Docker 격리 권고 (별도) |
| ADR-011 §2.1 (c) ADR/SDD 본문 갱신 | (별도 PR — 본 PoC 외) | ADR-012 / G4 본문 변경 0건 |
| ADR-011 §2.1 (d) 자동 회귀 | CI workflow | `.github/workflows/g4-hash-chain.yml` |
| ADR-011 §2.1 (e) 합의 APPROVE | Q1 풀 3+1 + Q2/Q3 단축 | 별도 합의 보고서 2건 |
| ADR-011 §2.4 (T1/T2/T3) | T3 위반 자동 revert 금지 | chain violation = BLOCK + manual + violation entry (자동 revert 0건) |
| ADR-008 차단조건 #2 | Evidence Ledger = Hermes 의존 0 | `jq` + `sha256sum` + Python stdlib + `rfc8785` (provider-neutral PyPI) |
| ADR-012 §2.3 Layer 1 | Append-only + Hash Chain | `jsonl_hash_chain.py` Layer 1 한정 (Layer 2~5 별도) |
| ADR-012 §2.5 JCS Primary + jq fallback | RFC 8785 JCS | `tools/canonical_json.py` Primary + Fallback + `canonical_json_fallback` entry |
| ADR-012 §2.6 Genesis Hash | MVP 정의 | `genesis_hash = sha256("genesis:<scope>:<schema_version>")` |
| ADR-012 §2.7 prev_hash 검증 실패 | BLOCK + manual + violation entry | rc=1 + `chain_violation_detected` 자동 작성 |
| ADR-012 §2.9 round-trip 3 entry 형식 | `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` | `jsonl_roundtrip.py` 3 형식 자동 작성 |
| G4 §4.2 11 필드 | `event` 11번째 신규 | schema validation 의무 |
| Provider Liquidity (헌법 5조 비협상) | feedback_provider_liquidity.md | `rfc8785` + `pyjcs` 모두 provider-neutral PyPI + `jq` POSIX 표준 |

---

## 8. 금지 사항 (사용자 명시 답습)

| # | 금지 항목 | 출처 |
|---|----------|------|
| 1 | G4 전체 Implementation/Runtime PASS 선언 | 사용자 명시 |
| 2 | G2/G3/G4 전체 Implementation/Runtime PASS 선언 | 사용자 명시 |
| 3 | Hermes PMO 격상 선언 | 사용자 명시 |
| 4 | 실 migration script (`hermes_to_claude.py` 등) 본 구현 | 사용자 명시 |
| 5 | ADR 본문 자동 갱신 | 사용자 명시 |
| 6 | 신규 정책 발명 (roadmap / ADR-012 / G4 외) | 답습 시제 |
| 7 | Hermes 의존 도입 (Evidence Ledger Hermes 의존 0 — ADR-008 차단조건 #2) | 헌법 권위 |

본 PoC = **G4 *부분 충족 시제* 한정** — G4 전체 PASS 권한 0건.

---

## 9. 합의 형식 (Q4 결정 답습)

| Sub | 형식 | 답습 |
|-----|------|------|
| Q1 (JCS 라이브러리 선정) | **풀 3+1 합의** | Group A 2차 T-1~T-4 패턴 답습. RA-9 사전 검증 evidence 흡수. fallback 도구 충돌 시 Q2/Q3 까지 일괄 격상 trigger 등록 |
| Q2 (corpus 24개) | Reviewer-only 단축 | Group B 답습 |
| Q3 (PoC 6 영역) | Reviewer-only 단축 | Group B 답습 |
| 본 PoC 자체 | Reviewer-only 단축 (구현 후) | Group A/B 답습 |

### 9.1 escalation trigger (Q1 풀 3+1 후 등록)

| # | trigger | 격상 |
|---|---------|------|
| TR-C-1 | RA-9 사전 검증 결과 `rfc8785` + `pyjcs` 모두 install 불가 | Q1 재합의 (stdlib + jq 단독 검토) |
| TR-C-2 | corpus 24개 중 1+ Primary ↔ Fallback 동등성 실패 | Q2/Q3 풀 3+1 격상 |
| TR-C-3 | `event` 17 enum 중 본 PoC MVP 4종 외 추가 발화 | 별도 합의 + ADR-012 §2.2 cross-reference |
| TR-C-4 | round-trip T2 strict 실패율 > 0% (24개 corpus 적용 시) | 풀 3+1 + ADR-012 §2.5 fallback 정식화 검토 (`Fallback 사용 빈도 > 10%` 답습) |
| TR-C-5 | Hermes 의존 발견 (subprocess Hermes 호출 등) | 즉시 BLOCK + ADR-008 차단조건 #2 위반 escalation |

---

## 10. Evidence 5 형식 (R-7 SOP 답습)

| # | Evidence | 위치 |
|---|----------|------|
| 1 | 본 사양 문서 (PoC 사양 + 답습 매핑) | 본 파일 |
| 2 | RA-9 사전 검증 evidence | 본 파일 §B (RA-9 결과 흡수) |
| 3 | Q1 풀 3+1 합의 보고서 | `docs/review/3plus1-consensus-2026-05-XX-g4-jcs-library-selection.md` |
| 4 | Q2/Q3 Reviewer-only 단축 합의 보고서 | `docs/review/3plus1-consensus-2026-05-XX-g4-corpus-poc-scope-short.md` |
| 5 | CI actual run + corpus 24/24 + chain 4/4 + round-trip T2 evidence | `.github/workflows/g4-hash-chain.yml` actual run URL + summary |

---

## 11. 알려진 한계 (자기 명시 — Group B P-1~P-5 답습)

| # | 한계 | 별도 합의 영역 |
|---|------|---------------|
| L-1 | Layer 2~5 (history / signed commit / branch protection / Full Rewrite 5 Layer) 미적용 | ADR-012 §2.3 + §2.8 답습 — 별도 PoC |
| L-2 | round-trip = JSONL → JSONL 동일 형식 한정 (cross-format 미적용) | Group H (Migration script implementation) — ADR-014 발행 trigger |
| L-3 | `event` 17 enum 중 MVP 4종 한정 검증 (`canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) | ADR-012 §2.2 답습 — 17 enum 전체 검증은 별도 합의 |
| L-4 | timestamp monotonicity 검증은 entry-level 한정 (clock drift / timezone normalization 미적용) | ADR-012 §3.4 답습 — 별도 합의 |
| L-5 | content-level 의미 정확성 보장 0건 (ADR-012 §11 한계 답습) | 헌법 1조 + 합의 인프라 + Reviewer 종합 + Human override layer |

---

## 부록 A — 의존 매트릭스

| 의존 | 출처 | 본 PoC 사용 |
|------|------|------------|
| `rfc8785` 0.1.4 (PyPI, Apache-2.0) | Trail of Bits | Primary 1 — corpus 24개 byte/sha256 동등성 cross-check (Q1 결정 갱신 답습) |
| `jcs` 0.2.1 (PyPI, Apache-2.0) | titusz (`tp@py7.de`, GitHub `titusz/jcs`) | Primary 2 — corpus 24개 byte/sha256 동등성 cross-check (RA-9 §B.3 발견 — `pyjcs` PyPI 미존재 발견 후 사용자 결정 갱신 흡수) |
| `jq` (POSIX) | stedolan/jq | Fallback (`-S -c`) — ADR-012 §2.5 명시 답습 |
| ~~`pyjcs`~~ | ~~Anders Rundgren (RFC 저자)~~ | ❌ **PyPI 미존재 — 채택 불가** (RA-9 §B.1 결과) |
| Python stdlib `hashlib.sha256` | CPython | hash 계산 |
| Python stdlib `json` | CPython | parse / fallback |
| Python stdlib `subprocess` | CPython | jq fallback 호출 |
| Python stdlib `uuid` | CPython | id 형식 검증 |
| Python stdlib `datetime` | CPython | ISO 8601 monotonicity |

**Hermes 의존 0** (ADR-008 차단조건 #2 답습) — 본 PoC 모든 도구 = POSIX 표준 + Python stdlib + provider-neutral PyPI 한정.

---

## 부록 B — RA-9 사전 검증 Evidence (2026-05-10 완료)

> **상태**: ✅ 완료 (격리 venv `.poc-prep/jcs-ra9-venv/` Python 3.12, install + license + 의존 + sanity check 6 항목 검증)
> **답습**: Group A 2차 RA-9 (외부 모듈 사전 검증 의무) — `g2-gp5-poc2-import-linter-implementation.md` 답습 시제

### B.1 검증 항목 결과 매트릭스

| # | 항목 | `rfc8785` | `pyjcs` (사용자 명시 원본 후보) | `jcs` (대안 후보 — 본 RA-9 발견) |
|---|------|----------|------|------|
| 1 | PyPI install 가능성 | ✅ 0.1.4 install OK | ❌ **PyPI 미존재** (`No matching distribution found for pyjcs`) | ✅ 0.2.1 install OK |
| 2 | License | Apache-2.0 (LICENSE 파일 존재) | (n/a) | Apache-2.0 (메타데이터 명시) |
| 3 | Author / 책임 주체 | Trail of Bits (`opensource@trailofbits.com`) | (n/a) | titusz (`tp@py7.de`, GitHub `titusz/jcs`) |
| 4 | 의존성 트리 (Hermes / provider SDK) | Requires: 없음 (의존 0) | (n/a) | Requires: 없음 (의존 0) |
| 5 | API surface | `dump`, `dumps`, `CanonicalizationError`, `FloatDomainError`, `IntegerDomainError` | (n/a) | `canonicalize`, `ntoj` |
| 6 | NaN/Infinity 거부 (RFC 8785 §3.2.2.2 답습) | ✅ `FloatDomainError: nan is not representable in JCS` | (n/a) | ✅ `ValueError: Invalid JSON number: nan` |

### B.2 동등성 sanity check (`rfc8785` vs `jcs`, 11 vector)

| # | case | rfc8785 sha256[:16] | jcs sha256[:16] | hash 일치 | 출력 일치 |
|---|------|---------------------|-----------------|----------|----------|
| 1 | simple `{b:2,a:1}` | `43258cff783fe703` | `43258cff783fe703` | ✅ | ✅ |
| 2 | unicode_korean `{k:"한글"}` | `9aa3f9b311e3f026` | `9aa3f9b311e3f026` | ✅ | ✅ |
| 3 | emoji_surrogate `{e:U+1F600}` | `47a47202d021be06` | `47a47202d021be06` | ✅ | ✅ |
| 4 | number_int `{n:1}` | `2bfd14f43d17fc7c` | `2bfd14f43d17fc7c` | ✅ | ✅ |
| 5 | number_float_one `{n:1.0}` | `2bfd14f43d17fc7c` | `2bfd14f43d17fc7c` | ✅ (#4 와 동일 — RFC 8785 §3.2.2 IEEE 754 동등) | ✅ |
| 6 | number_neg_zero `{n:-0.0}` | `f3013f933b9fb80a` | `f3013f933b9fb80a` | ✅ | ✅ |
| 7 | nested (depth 3) | `4bc2ec0b524651b2` | `4bc2ec0b524651b2` | ✅ | ✅ |
| 8 | escape_control_u01 `{c:U+0001}` | `e4755b00d504ea60` | `e4755b00d504ea60` | ✅ | ✅ |
| 9 | escape_quote_backslash `{s:"\"\\/"}` | `c41176394d3b2dfd` | `c41176394d3b2dfd` | ✅ | ✅ |
| 10 | unicode_2028 `{u:U+2028}` | `08de9591e5b52fc0` | `08de9591e5b52fc0` | ✅ | ✅ |
| 11 | rfc8785_a1_numbers (RFC §A.1 reference) | `7c892d3452ad85ad` | `7c892d3452ad85ad` | ✅ | ✅ |

**Total: 11/11 EQUAL** (hash 동일 + 출력 byte 동일).

### B.3 핵심 발견 + Q1 결정 갱신 영역

| 발견 | 영향 | 격상 |
|------|------|------|
| **`pyjcs` PyPI 미존재** (사용자 명시 Q1 후보 1건) | Q1 결정 ("rfc8785 + pyjcs 병렬") *부분 무효화* | **사용자 명시 결정 갱신 의무** (TR-C-1 부분 발화) |
| **`jcs` 0.2.1 (titusz)** PyPI 신규 발굴 | 동등성 11/11 PASS — 대안 후보 적격 | Q1 후보 옵션 A (권고): `rfc8785` + `jcs` 병렬 |
| `rfc8785` 단독 신뢰 가능 | Trail of Bits + Apache-2.0 + RFC 명시 구현 + NaN/Inf reject | Q1 후보 옵션 B: `rfc8785` 단독 |
| `canonicaljson` 2.0.0 (Matrix.org) PyPI 존재 | Matrix 자체 정의 — RFC 8785 동등성 미확정 | Q1 후보 옵션 C: 비권고 (별도 동등성 corpus 검증 필요) |

### B.4 Hermes 의존 0 + Provider Liquidity 보존 검증

- `rfc8785` Requires = 없음 + `jcs` Requires = 없음 → ADR-008 차단조건 #2 (Evidence Ledger Hermes 의존 0) **충족** 양 라이브러리
- 두 라이브러리 모두 provider-neutral PyPI (Anthropic / OpenAI / Google SDK 의존 0) → 헌법 5조 (Provider Liquidity) **보존** HIGH
- `jq` fallback (POSIX 표준) → 외부 의존 최소화 + ADR-012 §2.5 명시 답습

### B.5 escalation trigger 발화 매트릭스

| trigger | 발화 여부 | 비고 |
|---------|---------|------|
| TR-C-1 (RA-9 결과 두 후보 모두 install 불가) | **부분 발화** (`pyjcs` 1건 미존재) | 사용자 결정 갱신으로 대안 `jcs` 흡수 가능 |
| TR-C-2 (corpus 24개 동등성 실패) | 미발화 (sanity 11/11 PASS) | corpus 24개 본 PoC 구현 시 재검증 |
| TR-C-3 (`event` enum 추가 발화) | 미발화 | 본 PoC MVP 4종 한정 |
| TR-C-4 (round-trip T2 strict 실패) | 미발화 | 본 PoC 구현 시 검증 |
| TR-C-5 (Hermes 의존 발견) | 미발화 | 두 라이브러리 모두 의존 0 |

### B.6 evidence 산출 위치

- venv: `.poc-prep/jcs-ra9-venv/` (Python 3.12, gitignore 권고)
- script: `.poc-prep/sanity_equivalence.py` (11 vector 동등성)
- raw output: 본 §B.2 표 + 본 PoC 구현 시 corpus 24개 회귀로 격상

---

## 부록 C — 본 PoC 범위 vs roadmap §4.1 매트릭스

| roadmap §4.1 G4 영역 | 본 PoC 포함 |
|---------------------|------------|
| JSONL hash chain verification PoC (Order 3 tie) | ✅ §2 + §4.2 + §5 + §6 |
| RFC 8785 JCS canonicalization (Order 3 tie) | ✅ §3 + §4.1 + §6 |
| Round-trip validation PoC (Order 3 tie) | ✅ §4.3 + §5 + §6 (JSONL → JSONL 한정) |
| Memory/Skill schema validation (Order 6 tie) | ❌ Group E 영역 |
| Memory boundary hook (Order 9 tie) | ❌ Group G 영역 |
| Migration script implementation (Order 10) | ❌ Group H 영역 (사용자 명시 금지) |
| `provider_bindings` lint (G2 GP-5 통합) | ❌ Group A 답습 |

**본 PoC = Group C (Order 3 tie 3건 통합) 한정**. roadmap §4.1 7 영역 중 3 영역 ✅ + 4 영역 ❌ (별도 그룹 영역).
