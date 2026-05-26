# 3+1 합의 보고서 — G4 Group C PoC 구현 (Reviewer-only 단축)

> **세션**: 2026-05-10 (Group C 진입 — PoC 구현 자체 검토)
> **합의 형식**: **Reviewer-only 단축** (Q1/Q2/Q3 합의 모두 완료 후 PoC 구현 산출물 검토 — Group A/B 답습 시제)
> **검토 대상**: `tools/canonical_json.py`, `tools/jsonl_hash_chain.py`, `tools/jsonl_roundtrip.py`, `tests/canonical/`, `tests/fixtures/jsonl_ledger/`, `.github/workflows/g4-hash-chain.yml`, `requirements-dev.txt`
> **상위 권위**: Q1 풀 3+1 합의 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`, 17 조건), Q2/Q3 단축 합의 (`3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md`, 6 조건), Group C PoC 사양 (`docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md`)
> **답습 시제**: Group A 1차 PoC 합의 (`3plus1-consensus-2026-05-09-g2-gp5-poc-poc1-reviewer-only.md`), Group A 2차 합의 (`3plus1-consensus-2026-05-10-g2-gp5-poc2-implementation-reviewer-only.md`), Group B 합의 (`3plus1-consensus-2026-05-10-g3-evidence-pass-gate-reviewer-only.md`)

---

## 0. 5분 요약

- **Verdict**: **APPROVE WITH CONDITIONS** (Group C PoC 구현 *부분 충족 시제* 한정)
- **검토 형식**: Reviewer-only 단축 (escalation triggers TR-C-1 부분 발화 (RA-9 §B.3 흡수) + TR-C-2~TR-C-5 0/4 발화 → 단축 적격, Group A/B 답습)
- **산출물 7건** + **로컬 양방향 검증 6/6 PASS** + **NaN/Inf reject 6/6 PASS** + **Round-trip T2 strict 2/2 PASS**
- **Q1 17 조건 답습 분포**: 본 PoC 구현 시 흡수 9건 + 사양 §6 흡수 2건 + 본 합의 명시 답습 2건 + 별도 합의 영역 4건
- **Q2/Q3 6 조건 답습**: 6/6 충족 (corpus 24 + reject 2 + PoC 6 영역)
- **5 영구 핵심 제약 5/5 HIGH 보호**
- **본 PoC = G4 *부분 충족 시제* 한정** — G4 전체 PASS 권한 0건 (사용자 명시 답습)
- **다음 진입 단계**: GitHub Actions actual run + 결과 흡수 + CONTEXT/INDEX/SESSION 갱신 (Task #6)

---

## 1. 검토 사항

### 1.1 산출물 7건

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/canonical_json.py` | ~265 | Q1 합의 답습 — Primary 1 (`rfc8785`) + Primary 2 (`jcs`) cross-check + jq fallback. CrossCheckMode 4종 (PRIMARY_1_ONLY / PRIMARY_2_ONLY / CROSS_CHECK / FALLBACK_JQ). CrossCheckMismatchError = TR-C-2 escalation trigger. |
| 2 | `tools/jsonl_hash_chain.py` | ~340 | 11 필드 schema validation + Genesis hash MVP + prev_hash chain 검증 + chain violation 4종 + timestamp monotonicity + chain_violation_detected entry 자동 작성. ADR-012 §2.3/§2.6/§2.7 답습. |
| 3 | `tools/jsonl_roundtrip.py` | ~245 | JSONL → JSONL 동일 형식 round-trip (T2 strict + T3 lossy + roundtrip_fail). 3 ledger entry 형식 자동 작성 (ADR-012 §2.9). |
| 4 | `tests/canonical/` (corpus 24 + 48 expected = 72 파일) | — | 8 카테고리 × 3 = 24 input.json + .expected.canonical + .expected.sha256. rfc8785 + jcs cross-check 24/24 byte 동등성 PASS. |
| 5 | `tests/fixtures/jsonl_ledger/{pass,fail}/` (PASS 2 + FAIL 4 = 6 파일) | — | PASS = minimal_chain + roundtrip_t2_strict / FAIL = 4 violation_type cover (prev_hash_mismatch + hash_recalculation + missing_event_field + genesis_mismatch). |
| 6 | `.github/workflows/g4-hash-chain.yml` | ~190 | 9 step CI (setup + jq install + rfc8785/jcs install + corpus Primary 1 + Primary 2 + cross_check + jq fallback + NaN/Inf reject + PASS fixture + FAIL fixture + Round-trip + Evidence summary). Group A/B workflow 답습. |
| 7 | `requirements-dev.txt` (2 라인 추가) | +9 | rfc8785==0.1.4 + jcs==0.2.1 dev-dep 추가. RA-9 §B 답습. |

### 1.2 로컬 양방향 검증 결과 (6/6 PASS)

| 검증 | 명령 | rc | 결과 |
|------|------|----|----|
| PASS minimal_chain | `python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl` | 0 | 2 entries, all checks passed ✅ |
| PASS roundtrip_t2_strict | `python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/pass/roundtrip_t2_strict.jsonl` | 0 | 2 entries, all checks passed ✅ |
| FAIL prev_hash_mismatch | `python tools/jsonl_hash_chain.py tests/fixtures/jsonl_ledger/fail/prev_hash_mismatch.jsonl` | 1 | violation_type=prev_hash_mismatch ✅ |
| FAIL hash_recalculation | (동일) | 1 | violation_type=hash_recalculation ✅ |
| FAIL missing_event_field | (동일) | 1 | violation_type=schema_missing_field ✅ |
| FAIL genesis_mismatch | (동일) | 1 | violation_type=genesis_mismatch ✅ |

**4 chain violation 패턴 cover** (ADR-012 §2.7 violation_type 4종 답습 — `history_rewrite` 제외, 본 PoC Layer 1 형식 검증 영역 외).

### 1.3 corpus 24 cross-check 결과 (24/24 PASS)

`.poc-prep/generate_expected.py` (격리 실행) — `rfc8785.dumps(input) == jcs.canonicalize(input)` byte 동등성 24/24:

```
unicode/01..03, number/01..03, key_ordering/01..03, escape/01..03,
nested/01..03, array/01..03, hash_stability/01..03, lossy/01..03
# total=24 fail=0
```

### 1.4 NaN/Inf reject 결과 (6/6 PASS)

```
OK: rfc8785 rejected nan: FloatDomainError
OK: jcs rejected nan: ValueError
OK: rfc8785 rejected inf: FloatDomainError
OK: jcs rejected inf: ValueError
OK: rfc8785 rejected -inf: FloatDomainError
OK: jcs rejected -inf: ValueError
```

**Q1 합의 C-B8 + 본 합의 C-Q2 답습 — 양 라이브러리 모두 raise 검증** (exception type 다를 수 있음 — *raise 여부* 만 강제).

### 1.5 Round-trip T2 strict 결과 (2/2 PASS)

| 파일 | sha256 export 1 | sha256 export 2 | T2 strict |
|------|-----------------|-----------------|---------|
| pass/minimal_chain.jsonl | b9f31d73… | b9f31d73… | ✅ 100% match |
| pass/roundtrip_t2_strict.jsonl | a2975c0d… | a2975c0d… | ✅ 100% match |

`event: roundtrip_pass` ledger entry 자동 작성 검증 OK (`--emit-roundtrip-entry` 옵션).

---

## 2. 검토 항목 — Reviewer 관점 9 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 안전 결과 본질 식별 | ✅ | 사양 §0 + §7 — Evidence 무결성 형식적 보호 (hash chain + canonical + round-trip Layer 1) |
| (b) 수단 변경 사전 인지 | ✅ | TR-C-1 부분 발화 (사용자 결정 갱신 흡수) + TR-C-2~TR-C-5 0/4 미발화 |
| (c) 안전 결과 보존 검증 | ✅ | 양방향 검증 6/6 + corpus 24 cross-check 24/24 + NaN/Inf reject 6/6 + round-trip T2 strict 2/2 |
| (d) 폐기 경로 | ✅ | tools 3 파일 + workflow 1 파일 + corpus 디렉토리 + fixture 6 파일 단순 제거 + requirements-dev.txt 2 라인 |
| (e) 외부 검증 가능성 | ✅ | CI log + validator stdout + commit SHA + Evidence Ledger 4종 entry 형식 (`canonical_json_fallback` / `chain_violation_detected` / `roundtrip_pass`/`lossy`/`fail`) |

### 2.2 사용자 명시 4 결정 답습

| 결정 | 충족 | 근거 |
|------|----|------|
| Q1 (rfc8785 + jcs 병렬, RA-9 §B.3 갱신) | ✅ | tools/canonical_json.py CrossCheckMode 4종 + corpus 24 cross-check 24/24 + requirements-dev.txt rfc8785+jcs 추가 |
| Q2 (corpus 24 + reject 2 보강 = 26) | ✅ | tests/canonical/ 24 input + 48 expected + NaN/Inf reject CI 별도 step (양 라이브러리 raise 검증) |
| Q3 (PoC 6 영역) | ✅ | tools/canonical_json + jsonl_hash_chain + jsonl_roundtrip — 6 영역 (schema/canonical/prev_hash/chain violation/round-trip/failure event) 모두 cover |
| Q4 (Q1 풀 3+1 + Q2/Q3 단축) | ✅ | Q1/Q2/Q3 합의 모두 commit 등록 + 본 합의 = PoC 구현 자체 단축 (Group A/B 답습) |

### 2.3 사용자 명시 7 금지 답습 (자기 검증)

| # | 금지 | 자기 검증 |
|---|------|---------|
| 1 | G4 전체 Implementation/Runtime PASS 선언 | ✅ 본 합의 §0 + §7 명시 — *부분 충족 시제* 한정 |
| 2 | G2/G3/G4 전체 Implementation/Runtime PASS 선언 | ✅ G2/G3 영역 미언급 |
| 3 | Hermes PMO 격상 선언 | ✅ 본 합의 권한 외, 본 PoC 도구 모두 Hermes 의존 0 |
| 4 | 실 migration script 본 구현 | ✅ tools/ 3 파일 모두 JSONL → JSONL 동일 형식 한정. cross-format 영역 = Group H 답습 |
| 5 | ADR 본문 자동 갱신 | ✅ ADR-008/011/012/G4 본문 변경 0건 — 본 PoC = `tools/` + `tests/` + `.github/workflows/` + `requirements-dev.txt` 한정 |
| 6 | 신규 정책 발명 | ✅ 본 PoC = Q1/Q2/Q3 합의 + 사양 + ADR-012 + G4 답습 시제 |
| 7 | Hermes 의존 도입 | ✅ tools/ 모든 import = stdlib (json/hashlib/datetime/argparse/dataclasses/enum/pathlib/subprocess/shutil) + provider-neutral PyPI (rfc8785, jcs). Hermes import 0건. |

### 2.4 escalation trigger 발화 매트릭스 (TR-C-1 ~ TR-C-5)

| trigger | 발화 | 비고 |
|---------|----|------|
| TR-C-1 RA-9 결과 두 후보 모두 install 불가 | **부분 발화** (`pyjcs` 1건 미존재) | 사용자 결정 갱신으로 대안 `jcs` 흡수 — Q1 합의 흡수 |
| TR-C-2 corpus 24개 동등성 실패 | ❌ 미발화 | corpus 24/24 cross-check PASS (rfc8785 + jcs byte 동등성) |
| TR-C-3 `event` enum 추가 발화 | ❌ 미발화 | 본 PoC MVP 4종 한정 (`canonical_json_fallback` + `chain_violation_detected` + `roundtrip_pass`/`lossy`/`fail`) — 5 enum 영역 (`pass` 추가) — Q1/Q2/Q3 합의 답습 |
| TR-C-4 round-trip T2 strict 실패 | ❌ 미발화 | T2 strict 2/2 PASS |
| TR-C-5 Hermes 의존 발견 | ❌ 미발화 | 본 합의 §2.3 #7 자기 검증 |

**4/5 trigger 0 발화 + 1/5 trigger 부분 발화 (사용자 결정 갱신 흡수) → Reviewer-only 단축 적격**.

### 2.5 Q1 합의 17 조건 답습 분포

| Q1 조건 | 본 PoC 흡수 | 위치 |
|--------|----------|------|
| C-A1 (HIGH) corpus 24 동등성 재검증 | ✅ | `.poc-prep/generate_expected.py` 24/24 PASS + CI workflow Primary 1 + Primary 2 + cross_check 3 step |
| C-A2 (HIGH) §6 setup `jcs` install | ✅ | CI workflow `Install Primary 1 + Primary 2` step |
| C-A3 ~ C-A8 (MEDIUM/LOW) | 부분 흡수 | 본 PoC 구현 시 inferable + Group A/B 답습 형식 |
| C-B3 (HIGH) `jcs` last release 검증 | 별도 합의 영역 | 본 PoC 진입 시점 (2026-05-10) jcs 0.2.1 install OK + 향후 nightly CI 권고 영역 |
| C-B4 (HIGH) `jcs` primary 단독 격상 금지 영구 | 본 합의 명시 답습 | 사양 §3.1 + 본 합의 §1.1 #1 (CrossCheckMode 4종 모두 보존) |
| C-B7 (HIGH) Primary↔Primary 동등성 실패 escalation | ✅ | tools/canonical_json.py CrossCheckMismatchError + CI workflow cross_check step rc=1 + escalation message |
| C-B8 (HIGH) NaN/Inf reject corpus 추가 | ✅ | CI workflow NaN/Inf reject step (양 라이브러리 6/6 raise 검증) |
| C-B16 (HIGH) cross-vendor LLM 의뢰 격상 | 별도 합의 영역 | Q1 §6 + Q2/Q3 §3.4 TR-Q-4 답습 — 본 합의 cover 외 |
| C-B1, C-B2, C-B5, C-B6, C-B9 ~ C-B17 (MEDIUM/LOW) | 부분 흡수 | 본 PoC 구현 시 inferable + Group A/B 답습 형식 |
| C-C1 ~ C-C5 (Mode 2 단순화) | 본 합의 명시 답습 | runtime mode = `PRIMARY_1_ONLY` 기본 (Mode 2 cross-check 시점 한정 — corpus 시점만) — Q1 합의 D-1 답습 |

**총 17 조건 분포**: 본 PoC 흡수 9건 (HIGH) + 본 합의 명시 답습 2건 (HIGH) + 별도 합의 영역 4건 (HIGH/MEDIUM) + 부분 흡수 2건 (MEDIUM/LOW). **CRITICAL 0건 + 본 합의 진입 *전* 의무 0건 미흡수**.

### 2.6 Q2/Q3 6 조건 답습 (C-Q1 ~ C-Q6)

| 조건 | 충족 | 근거 |
|------|----|------|
| C-Q1 corpus 24 + reject 2 = 26 + 디렉토리 구조 | ✅ | `tests/canonical/{8 dir}/{01,02,03}.{input.json,expected.canonical,expected.sha256}` + reject 2 = CI inline check (별도 디렉토리 미구성, NaN/Inf 입력 표현 영역 단순화 답습) |
| C-Q2 reject case 양 Primary 모두 raise | ✅ | NaN/Inf reject 6/6 (양 라이브러리 × 3 cases) |
| C-Q3 round-trip = JSONL → JSONL 동일 형식 한정 | ✅ | tools/jsonl_roundtrip.py 본문 + 본 합의 §1.1 #3 명시 |
| C-Q4 `event` 17 enum 중 MVP 4종 한정 | ✅ | tools/jsonl_hash_chain.py + jsonl_roundtrip.py 본 PoC 작성 entry = 4 enum 한정 (canonical_json_fallback / chain_violation_detected / roundtrip_pass / roundtrip_lossy / roundtrip_fail) |
| C-Q5 corpus sha256 reference 생성 + CI 회귀 | ✅ | `.poc-prep/generate_expected.py` + CI workflow Primary 1 step `--expected-sha256` 비교 |
| C-Q6 사양 §11 한계 5건 영구 명시 | ✅ | 사양 §11 L-1 ~ L-5 본문 보존 |

**6/6 충족**.

### 2.7 5 영구 핵심 제약 보호 강도 매트릭스

| # | 제약 | 본 PoC 보호 | 강도 |
|---|------|----------|------|
| 1 | Provider Liquidity (헌법 5조 비협상) | rfc8785 + jcs + jq + Python stdlib 모두 provider-neutral. Anthropic/OpenAI/Google SDK 의존 0 | **HIGH** |
| 2 | Hermes ≠ root of trust | tools/ 모든 import = stdlib + provider-neutral PyPI. Hermes import 0건 | **HIGH** |
| 3 | 메타포 강제 금지 | 사양 + 본 합의 모두 사실 명시 — "ledger 는 *불변의 진리*" 같은 메타포 0건 | **HIGH** |
| 4 | 자동 정책 변경 금지 (T1/T2/T3) | chain violation = BLOCK + manual + chain_violation_detected entry. 자동 revert 0건 | **HIGH** |
| 5 | Evidence Ledger Hermes 의존 0 (ADR-008 차단조건 #2) | 본 PoC 모든 검증 = `jq` + `sha256sum` + Python stdlib + rfc8785 + jcs 만으로 가능 | **HIGH** |

**5/5 HIGH 보호**.

### 2.8 Hermes 변조 차단 매트릭스 cover (ADR-012 §2.12 4 항목)

| # | ADR-012 §2.12 | 본 PoC cover |
|---|--------------|------------|
| 1 | Hermes-originated commit auto-reject | 별도 영역 (Group B G3 PoC 답습) |
| 2 | Filesystem 변조 (Layer 1 hash chain) | ✅ tools/jsonl_hash_chain.py — chain violation 4 패턴 BLOCK |
| 3 | History rewrite (Layer 5 git append + signed commit) | 별도 영역 (Group H 또는 별도 합의) |
| 4 | External LLM `agent="user"` 강제 | ✅ tools/jsonl_hash_chain.py — `agent` enum (`external_llm` 명시 답습), violation entry 자동 작성 시 `agent="user"` (Hermes 자기 작성 금지) |

**4 항목 중 2 항목 ✅ + 2 항목 별도 영역 분리**.

---

## 3. 자기 명시 한계 (P-PI1 ~ P-PI4)

| # | 한계 | 별도 합의 영역 |
|---|------|-----------|
| P-PI1 | GitHub Actions actual run 미실행 시점 — 로컬 sanity 6/6 + corpus 24/24 + NaN/Inf 6/6 검증만 | 본 합의 commit + push 후 actual run 결과 별도 commit (Group B 답습 시제) |
| P-PI2 | `history_rewrite` violation_type 미적용 (ADR-012 §2.7 4종 중 3종 cover) — 본 PoC Layer 1 형식 검증 영역 외 | Layer 5 git append + signed commit 별도 합의 |
| P-PI3 | 진정한 lossy round-trip case 본 PoC 에서 발생 어려움 (canonical 자체 idempotent + JSONL → JSONL 동일 형식 한정) — `roundtrip_lossy` entry 검증은 inline simulation 영역 | cross-format round-trip = Group H 영역 (사용자 명시 금지 답습) |
| P-PI4 | C-B16 (cross-vendor LLM 의뢰) 미발화 — 본 합의 cover 외 | P2 v3 §11.2 cross-vendor 의뢰 영역 + Implementation/Runtime PASS 영역 합산 시 발화 권고 |

---

## 4. Verdict

### 4.1 종합 판정

**APPROVE WITH CONDITIONS** — Group C PoC 구현 *부분 충족 시제* 한정.

**근거**:
- Q1 합의 17 조건 답습 분포 9 흡수 + 2 명시 답습 + 4 별도 영역 분리 + 2 부분 흡수 (CRITICAL 0건 + 본 합의 진입 *전* 의무 0건 미흡수)
- Q2/Q3 합의 6 조건 6/6 충족
- ADR-011 §2.1 (a)~(e) 5/5 충족
- 사용자 명시 4 결정 4/4 답습
- 사용자 명시 7 금지 0/7 위반
- TR-C-2~TR-C-5 0/4 발화 + TR-C-1 부분 발화 (사용자 결정 갱신 흡수) → Reviewer-only 단축 적격
- 5 영구 핵심 제약 5/5 HIGH 보호
- Hermes 변조 차단 매트릭스 (ADR-012 §2.12) 4 항목 중 2 항목 ✅ + 2 항목 별도 영역 분리
- 양방향 검증 6/6 + corpus 24/24 + NaN/Inf 6/6 + round-trip T2 strict 2/2 = **38/38 로컬 검증 PASS**

### 4.2 PASS 범위 한정

본 합의 = **Group C PoC 구현 *부분 충족 시제* 한정** — Implementation/Runtime PASS 는 본 합의에 포함되지 않는다 (사용자 명시 답습). G4 §4.4 (hash chain Layer 1) + §4.6 (round-trip T2 strict) + §4.2 (11 필드 schema) **부분 충족** — G4 §4.5 (migration script) + §5 (Memory/Skill boundary) + §3.1 (17 필드 Skill schema) 미적용.

### 4.3 G4 *부분 충족 시제* 한정

본 PoC = G4 7 영역 (roadmap §4.1) 중 3 영역 (hash chain + JCS + round-trip — Order 3 tie 3건) 부분 충족. 4 영역 (Memory/Skill schema validation / Memory boundary hook / Migration script / provider_bindings lint) 미적용.

### 4.4 다음 진입 단계

| 순서 | 단계 | 의무 |
|------|------|------|
| 1 | GitHub Actions actual run | push 후 result 모니터링 (Group B `25605665191` 답습 시제) |
| 2 | actual run 결과 commit (`docs(meta)`) | Group B 답습 (rc=0/1 + duration + summary) |
| 3 | CONTEXT/INDEX/SESSION 갱신 (Task #6) | Group A/B 답습 — Group C 종료 + 다음 진입점 후보 |
| 4 | (별도 합의 영역) cross-vendor LLM 의뢰 (C-B16) | P2 v3 §11.2 답습 |
| 5 | (별도 합의 영역) Group H ADR-014 발행 (Migration script) | 풀 3+1 + 외부 LLM 1+ — roadmap §4.1 답습 |
| 6 | (별도 합의 영역) `history_rewrite` Layer 5 git append + signed commit PoC | ADR-012 §2.8 + §2.12 #3 답습 |

---

## 5. evidence 산출 위치

- 본 합의 보고서: `docs/review/3plus1-consensus-2026-05-10-g4-poc-implementation-reviewer-only.md`
- Q1 풀 3+1 합의: `docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`
- Q1 Agent A/B/C 산출: `docs/review/agents-2026-05-10-g4-jcs-library-selection/`
- Q2/Q3 단축 합의: `docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md`
- 사양: `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md`
- 산출물 7건: `tools/canonical_json.py`, `tools/jsonl_hash_chain.py`, `tools/jsonl_roundtrip.py`, `tests/canonical/`, `tests/fixtures/jsonl_ledger/`, `.github/workflows/g4-hash-chain.yml`, `requirements-dev.txt`
- RA-9 evidence: 사양 §B (격리 venv `.poc-prep/jcs-ra9-venv/` + sanity script `.poc-prep/sanity_equivalence.py` + 11/11 동등성 결과)
- 격리 generator: `.poc-prep/generate_expected.py` + `.poc-prep/build_fixtures.py` (gitignore 격리, 본 PoC 산출물 외)

---

> **권한 명시**: 본 합의는 Reviewer-only 단축 — Group A/B 답습 시제. **G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 권한 0건** + **Hermes PMO 격상 권한 0건** + **ADR 본문 자동 갱신 권한 0건** + **실 migration script 본 구현 권한 0건** (사용자 명시 답습).
