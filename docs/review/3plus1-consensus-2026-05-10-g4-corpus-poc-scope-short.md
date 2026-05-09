# 3+1 합의 보고서 — G4 Corpus 24 + PoC 6 영역 사양 (Group C, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group C 진입 — Q2/Q3 사양 단축 합의)
> **합의 형식**: **Reviewer-only 단축** (Q4 사용자 명시 결정 답습 — Q1 풀 3+1 + Q2/Q3 단축 분리)
> **검토 대상**: `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` §1.1 산출물 표 / §3.4 corpus 24 / §4 validator 명세 / §5 fixture 명세 / §6 CI workflow + Q1 합의 결과 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`) 흡수 검증
> **상위 권위**: ADR-008 차단조건 #2 (Evidence Ledger Hermes 의존 0), ADR-011 §2.1 (a)~(e), ADR-012 §2.3/§2.5/§2.6/§2.7/§2.9, G4 §4.2/§4.4/§4.6, P2 v3 §6 (G4 답습 권위), `implementation-runtime-roadmap.md` §4.1 (G4 7 영역 — Order 3 tie 3건)
> **답습 시제**: Group A 1차 PoC 합의 (`3plus1-consensus-2026-05-09-g2-gp5-poc-poc1-reviewer-only.md`), Group B 합의 (`3plus1-consensus-2026-05-10-g3-evidence-pass-gate-reviewer-only.md`), Q1 풀 3+1 합의 (`3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`)

---

## 0. 5분 요약

- **Verdict**: **APPROVE WITH CONDITIONS** (Q2 + Q3 사양 *설계 승인* 한정)
- **검토 형식**: Reviewer-only 단축 (Q4 사용자 명시 결정 답습 + 풀 3+1 격상 trigger TR-Q-1~TR-Q-4 0/4 발화)
- **Q2 (corpus 24개 + reject 2건 보강)**: 권고 채택 (8 카테고리 × 3 = 24 + NaN/Inf reject 2건 = 26 total)
- **Q3 (PoC 6 영역)**: 권고 채택 (schema / canonical / prev_hash / chain violation / round-trip / failure event)
- **Q1 합의 흡수 정합**: 사양 §1.1 (Canonical JSON 모듈 갱신) + §3.1 (Primary 채택 설명 갱신) + §3.4 (corpus reject 보강) + §6 (CI setup `jcs` install + corpus cross-check step 추가) + 부록 A (의존 매트릭스 갱신) + 부록 B (RA-9 evidence 흡수) — **5 영역 갱신 정합 검증**
- **추가 조건 6건** (C-Q1 ~ C-Q6) — 모두 본 PoC 구현 시 의무 (별도 합의 영역 0건 추가)
- **5 영구 핵심 제약 5/5 HIGH 보호** (Q1 합의 §7 답습)
- **본 합의 = G4 *부분 충족 시제* 한정** — G4 전체 PASS 권한 0건 (사용자 명시 답습)
- **다음 진입 단계**: Group C PoC 구현 (Task #5) → Reviewer-only 단축 합의 (PoC 자체)

---

## 1. 합의 의제

### 1.1 Q2 — Test corpus 24개 (8 카테고리 × 3) 사양

| 카테고리 | case 3개 | 총 |
|----------|---------|----|
| unicode | 한글 NFC / 일본어 카타카나 / Emoji surrogate pair (U+1F600 등 BMP 외부) | 3 |
| number normalization | `1.0` vs `1` / `1e10` vs `10000000000` / `-0` vs `0`. **+ NaN/Inf reject 2건 보강** (`nan_reject.json` + `inf_reject.json` — Q1 합의 C-B8 답습) | 3 + 2 |
| object key ordering | flat key 다수 / 비-ASCII key (UTF-16 codepoint 순) / 숫자 형 key (ASCII 순) | 3 |
| escape handling | U+0001~U+001F control / U+2028 line separator / `"`, `\\`, `/` | 3 |
| nested object | depth 3 / depth 10 / mixed dict+list 교차 | 3 |
| array | empty `[]` / homogeneous `[1,2,3]` / heterogeneous mixed type | 3 |
| hash stability | 동일 입력 100회 → 동일 hash / key 입력 순서 무관 / whitespace 무관 | 3 |
| lossy round-trip | float precision loss / unicode normalization (NFC vs NFD) / number→string | 3 |
| **합계** | | **26** (24 + reject 2) |

**ADR-012 §2.5 ≥20개 답습 — 26개로 130% cover**.

### 1.2 Q3 — PoC 6 영역

| # | 영역 | 본 PoC 사양 출처 |
|---|------|---------------|
| 1 | JSONL ledger entry schema (11 필드) | 사양 §2 (G4 §4.2 답습) |
| 2 | Canonical JSON (rfc8785 + jcs 병렬 cross-check + jq fallback) | 사양 §3 (Q1 합의 답습) |
| 3 | prev_hash / hash 검증 (sha256 + canonical, Genesis hash MVP) | 사양 §4.2 (ADR-012 §2.3 + §2.6 답습) |
| 4 | Chain violation detection (mismatch → BLOCK + violation entry 자동 작성) | 사양 §4.2 (ADR-012 §2.7 답습) |
| 5 | Round-trip validation (T2 strict + T3 lossy, 동일 형식 내) | 사양 §4.3 (G4 §4.6 + ADR-012 §2.9 답습) |
| 6 | Failure event ledger entry (4종 — `canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) | 사양 §2.1 + §3.2 + §4.2 + §4.3 (ADR-012 §2.2 enum 17 후보 중 MVP 4종 한정) |

---

## 2. Q1 합의 결과 흡수 정합 검증 (5 영역)

| # | 사양 영역 | Q1 합의 흡수 | 정합 |
|---|---------|-----------|----|
| 1 | §1.1 산출물 표 — Canonical JSON 모듈 책무 표현 | "rfc8785 단독" → "rfc8785 + jcs 병렬 cross-check" + RA-9 §B.3 cross-reference | ✅ 정합 |
| 2 | §3.1 Primary 채택 설명 | `pyjcs` PyPI 미존재 발견 + `jcs` (titusz) 대안 발굴 사용자 결정 갱신 + 11/11 sanity 동등성 + cross-check 강제 | ✅ 정합 |
| 3 | §3.4 corpus 24 number 카테고리 | NaN/Inf reject 2건 보강 (Q1 C-B8 답습 — 양 라이브러리 모두 reject 검증) | ✅ 정합 |
| 4 | §6 CI workflow setup step | `jcs==0.2.1` install 추가 (Q1 R-A2 답습) + corpus 회귀 Primary 2 cross-check step 신규 (Q1 D-1 답습 — corpus 시점 cross-check 강제) | ✅ 정합 |
| 5 | 부록 A 의존 매트릭스 + 부록 B RA-9 evidence | `jcs` (titusz, Apache-2.0) Primary 2 추가 + `pyjcs` 채택 불가 명시 + 11/11 sanity vector 표 흡수 | ✅ 정합 |

**5/5 정합 — 흡수 drift 0건**.

---

## 3. 검토 항목 — Reviewer 관점 7 영역

### 3.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 안전 결과 본질 식별 | ✅ | 사양 §0 + §7 — Evidence 무결성 형식적 보호 (hash chain + canonical + round-trip Layer 1) |
| (b) 수단 변경 사전 인지 | ✅ | TR-C-1~TR-C-5 5 trigger 등록 (사양 §9.1) + Q1 합의 escalation matrix |
| (c) 안전 결과 보존 검증 | ✅ | corpus 26 + chain 4 violation cover + round-trip T2/T3 양 모드 + fallback 동등성 + RA-9 §B.2 11/11 sanity 답습 (PoC 구현 시 26 회귀 의무) |
| (d) 폐기 경로 | ✅ | tools 3 파일 + workflow 1 파일 + corpus 디렉토리 + fixture 6건 단순 제거 |
| (e) 외부 검증 가능성 | ✅ | CI log + validator stdout + commit SHA + Evidence Ledger entry 4종 형식 |

### 3.2 사용자 명시 4 결정 답습

| 결정 | 충족 | 근거 |
|------|----|------|
| Q1 (rfc8785 + jcs 병렬, RA-9 §B.3 갱신) | ✅ | Q1 풀 3+1 합의 보고서 APPROVE WITH CONDITIONS (3/3 일치) + 본 사양 §1.1 + §3.1 + §6 + 부록 A 흡수 |
| Q2 (corpus 24개 + reject 2 보강) | ✅ | 본 합의 §1.1 + 사양 §3.4 + Q1 합의 C-B8 답습 |
| Q3 (PoC 6 영역) | ✅ | 본 합의 §1.2 + 사양 §1.1 + §1.2 (제외 매트릭스 9건) |
| Q4 (Q1 풀 3+1 + Q2/Q3 단축) | ✅ | Q1 = `3plus1-consensus-2026-05-10-g4-jcs-library-selection.md` 풀 3+1 + 본 = Reviewer-only 단축 |

### 3.3 사용자 명시 7 금지 답습 (자기 검증)

| # | 금지 | 자기 검증 |
|---|------|---------|
| 1 | G4 전체 Implementation/Runtime PASS 선언 | ✅ 본 합의 = Q2/Q3 사양 *설계 승인* 한정 (§0 명시) |
| 2 | G2/G3/G4 전체 Implementation/Runtime PASS 선언 | ✅ 본 합의 = G4 *부분 충족 시제* — 다른 게이트 영역 미언급 |
| 3 | Hermes PMO 격상 선언 | ✅ 본 합의 권한 외 — 본 PoC 도 Hermes 의존 0 (ADR-008 차단조건 #2 답습) |
| 4 | 실 migration script 본 구현 | ✅ 본 PoC §1.2 제외 매트릭스 명시 (Group H 영역) |
| 5 | ADR 본문 자동 갱신 | ✅ ADR-008/011/012/G4 본문 변경 0건 — 본 합의 = `docs/review/` + 사양 §B 흡수 한정 |
| 6 | 신규 정책 발명 | ✅ 본 합의 = roadmap §4.1 + ADR-012 §2 + G4 §4 + Q1 합의 + 사용자 명시 4 결정 답습 시제 |
| 7 | Hermes 의존 도입 | ✅ 본 PoC 모든 도구 = POSIX + Python stdlib + provider-neutral PyPI (rfc8785 + jcs + jq) — 의존 트리 0 |

### 3.4 풀 3+1 격상 trigger 발화 매트릭스 (TR-Q-1 ~ TR-Q-4)

| trigger | 발화 | 격상 |
|---------|----|------|
| TR-Q-1 corpus 26 reference output 자체 정의 모호 (8 카테고리 cover 불충분) | ❌ 미발화 | 8 카테고리 cover + Q1 C-B8 reject case 보강 명시 |
| TR-Q-2 PoC 6 영역 중 1+ 영역의 ADR-012 / G4 답습 drift | ❌ 미발화 | §1.2 6/6 영역 모두 권위 cross-reference 명시 |
| TR-Q-3 Q1 합의 결과 흡수 drift (5 영역 중 1+ 미정합) | ❌ 미발화 | §2 5/5 정합 검증 |
| TR-Q-4 Q1 합의 17 조건 중 본 합의 진입 *전* 의무 (P0 4건) 흡수 drift | ❌ 미발화 (P0 4건 분포: corpus 동등성 재검증 = 본 PoC 구현 시 / `jcs` install setup = 사양 §6 갱신 ✅ / TR-C-2 보강 = 사양 §6 + §9.1 ✅ / cross-vendor LLM 의뢰 = 별도 합의 영역) | 별도 합의 영역 분리 (cross-vendor LLM 의뢰) |

**0/4 발화 → Reviewer-only 단축 적격 (사용자 명시 답습)**.

### 3.5 Q1 합의 17 조건 매핑 (본 합의 흡수 분포)

| Q1 조건 ID | 제목 | 본 합의 흡수 | 비고 |
|-----------|------|---------|------|
| C-A1 (HIGH) | corpus 24 동등성 재검증 의무 | 본 PoC 구현 시 (Task #5) | §6 corpus 회귀 Primary 2 cross-check step ✅ |
| C-A2 (HIGH) | §6 setup `jcs` install 누락 | 사양 §6 setup 갱신 ✅ | 본 합의 §2 #4 정합 |
| C-B3 (HIGH) | `jcs` last release 검증 | 본 PoC 구현 시 (RA-9 §B 답습 + nightly CI 권고) | 별도 합의 영역 (supply chain 모니터) |
| C-B4 (HIGH) | `jcs` primary 단독 격상 금지 영구 | 본 PoC 구현 후 영구 답습 (사양 §3.1 + 부록 A 명시 적격) | 본 합의 명시 답습 |
| C-B7 (HIGH) | Primary↔Primary 동등성 실패 escalation | 사양 §6 corpus 회귀 Primary 2 cross-check rc=1 + escalation ✅ | 본 합의 §1.1 + Q1 §6 답습 |
| C-B8 (HIGH) | NaN/Inf reject corpus 추가 | 사양 §3.4 number 카테고리 reject 2건 보강 ✅ | 본 합의 §1.1 정합 |
| C-B16 (HIGH) | cross-vendor LLM 의뢰 권고 격상 | **별도 합의 영역** (본 합의 cover 외 — Q1 §6 답습) | 본 합의 §3.4 TR-Q-4 명시 |
| C-A3~C-A8, C-B1~C-B17 (MEDIUM/LOW), C-C1~C-C5 | 기타 14건 | 본 PoC 구현 시 (Task #5) 또는 별도 합의 영역 | Q1 §5 매트릭스 답습 |

---

## 4. 본 합의 추가 조건 (C-Q1 ~ C-Q6 — Q2/Q3 사양 한정)

| # | 조건 | 시제 | 우선 |
|---|------|----|------|
| C-Q1 | corpus 24 + reject 2 = 26 total. corpus 디렉토리 구조 = `tests/canonical/{8 카테고리}/{01,02,03}.{json,canonical,sha256}` + `tests/canonical/number/{nan_reject,inf_reject}.json` (reject case 는 `.canonical` 미생성, ValueError 강제 검증). | 본 PoC 구현 시 | HIGH |
| C-Q2 | reject case 2건 = 양 Primary (`rfc8785.dumps()` + `jcs.canonicalize()`) 모두 exception raise 검증 의무 (NaN → `FloatDomainError` / `ValueError` / Infinity 동일). exception type 다를 수 있음 — *raise 여부* 만 강제. | 본 PoC 구현 시 | HIGH |
| C-Q3 | PoC 6 영역 중 round-trip = JSONL → JSONL **동일 형식** 한정 (사양 §4.3 명시 답습). cross-format (Hermes / Claude / OpenAI ↔ JSONL) round-trip 은 **Group H 영역** (사용자 명시 금지 답습). | 본 PoC 구현 시 + 합의 시 명시 | HIGH |
| C-Q4 | `event` 17 enum 중 본 PoC MVP 4종 (`canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) 한정 검증. 추가 발화 시 TR-C-3 trigger → 별도 합의 + ADR-012 §2.2 cross-reference. | 본 PoC 구현 시 | MEDIUM |
| C-Q5 | corpus 26 의 sha256 reference output 생성 절차 = `rfc8785.dumps(input) → sha256 hex → expected.sha256 파일`. CI 회귀 = `sha256(rfc8785.dumps(input)) == expected.sha256` 100% + `sha256(jcs.canonicalize(input)) == expected.sha256` 100% (양 라이브러리 모두). | 본 PoC 구현 시 | HIGH |
| C-Q6 | 사양 §11 한계 5건 (L-1 ~ L-5) 답습 — 본 합의 흡수 후에도 알려진 한계 영구 명시 (Layer 2~5 / cross-format / 17 enum 중 13종 / clock drift / content-level 의미 정확성). 본 PoC 합의 후속 권한 외 영역. | 본 PoC 합의 시 명시 + 영구 보존 | MEDIUM |

---

## 5. 답습 매트릭스

| 출처 | 답습 영역 | 본 합의 정합 |
|------|---------|-----------|
| ADR-008 차단조건 #2 | Evidence Ledger Hermes 의존 0 | ✅ 본 합의 §3.3 #7 + 사양 부록 A |
| ADR-011 §2.1 (a)~(e) | 수단/목적 분리 5조건 | ✅ 본 합의 §3.1 5/5 충족 |
| ADR-011 §2.4 (T1/T2/T3) | T3 자동 정책 변경 금지 | ✅ chain violation = BLOCK + manual + violation entry (자동 revert 0건) — 사양 §4.2 검사 3 답습 |
| ADR-012 §2.2 (event 11번째 필드 17 enum) | MVP 4종 한정 | ✅ C-Q4 답습 |
| ADR-012 §2.3 (Append-only + Hash Chain Layer 1) | Layer 1 한정 (L-1 답습) | ✅ 사양 §11 L-1 명시 |
| ADR-012 §2.5 (RFC 8785 JCS Primary + jq fallback + corpus 검증 ≥20개) | corpus 26 (130% cover) + Primary 2 cross-check + jq fallback | ✅ 본 합의 §1.1 + Q1 §6 답습 |
| ADR-012 §2.6 (Genesis Hash MVP `sha256("genesis:<scope>:<schema_version>")`) | MVP 정의 | ✅ 사양 §3.3 + Q3 #3 |
| ADR-012 §2.7 (prev_hash 검증 실패 BLOCK + manual + violation entry) | violation_type 4종 | ✅ Q3 #4 + 사양 §4.2 검사 3 |
| ADR-012 §2.9 (round-trip 3 ledger entry 형식) | T2 + T3 양 모드 (T2 strict + T3 lossy) + roundtrip_fail | ✅ Q3 #5 + #6 + 사양 §4.3 |
| G4 §4.2 (11 필드 — `event` 11번째 신규) | schema validation 의무 | ✅ Q3 #1 + 사양 §2.1 |
| G4 §4.4 (hash chain 보강) | 사양 §4 답습 | ✅ Q3 #2~#4 |
| G4 §4.6 (round-trip Tier-based) | T2 + T3 + roundtrip_fail | ✅ Q3 #5 |
| roadmap §4.1 (G4 7 영역 — Order 3 tie 3건) | hash chain + JCS + round-trip 통합 | ✅ 사양 부록 C 매트릭스 |
| 헌법 5조 (Provider Liquidity 비협상) | rfc8785 + jcs + jq 모두 provider-neutral | ✅ Q1 합의 §7 답습 |
| Q1 풀 3+1 합의 17 조건 | 본 합의 §3.5 매핑 매트릭스 | ✅ 흡수 7건 + 별도 영역 1건 + 본 PoC 구현 시 9건 |
| 사용자 명시 4 결정 | Q1 (rfc8785 + jcs) + Q2 (corpus 24+2) + Q3 (PoC 6) + Q4 (Q1 풀 3+1 + Q2/Q3 단축) | ✅ 본 합의 §3.2 4/4 충족 |
| 사용자 명시 7 금지 | 본 합의 §3.3 7/7 자기 검증 | ✅ 0/7 위반 |

---

## 6. 자기 명시 한계 (P-Q1 ~ P-Q3)

| # | 한계 | 별도 합의 영역 |
|---|------|------------|
| P-Q1 | 본 합의 = *사양 검토 한정* — 코드 / fixture / CI workflow 산출물 *미구현* 시점. 양방향 검증은 본 PoC 구현 후 별도 합의 (Task #5 영역) | Group C PoC 구현 합의 |
| P-Q2 | corpus 26 의 reference `expected.canonical` + `expected.sha256` 파일 *생성 절차* 자동화 미명시 (수동 생성 시 drift 위험) — 본 PoC 구현 시 generator 스크립트 권고 (별도 합의 outside) | 본 PoC 구현 시 generator 권고 |
| P-Q3 | Q1 합의 C-B16 (cross-vendor LLM 의뢰) 흡수 미발생 — 본 합의 cover 외 (별도 합의 영역, P2 v3 §11.2 cross-vendor 의뢰 영역) | 별도 합의 영역 (Implementation/Runtime PASS 영역 합산 시 발화 권고) |

---

## 7. Verdict

### 7.1 종합 판정

**APPROVE WITH CONDITIONS** — Q2 (corpus 24 + reject 2 보강 = 26) + Q3 (PoC 6 영역) 사양 *설계 승인* 한정.

**근거**:
- Q1 합의 17 조건 흡수 정합 5/5 (본 합의 §2)
- ADR-011 §2.1 (a)~(e) 5/5 충족 (본 합의 §3.1)
- 사용자 명시 4 결정 4/4 답습 (본 합의 §3.2)
- 사용자 명시 7 금지 0/7 위반 (본 합의 §3.3)
- 풀 3+1 격상 trigger TR-Q-1~TR-Q-4 0/4 발화 (본 합의 §3.4) → Reviewer-only 단축 적격
- 5 영구 핵심 제약 5/5 HIGH 보호 (Q1 §7 답습)
- 본 합의 추가 조건 6건 (C-Q1 ~ C-Q6) — 모두 본 PoC 구현 시 의무, 별도 합의 영역 0건 신설

### 7.2 PASS 범위 한정

본 합의 = **Q2/Q3 사양 *설계 승인* 한정** — Implementation/Runtime PASS 는 본 합의에 포함되지 않는다 (사용자 명시 답습). 양방향 검증 + actual run + corpus 26 회귀 PASS + chain 4 violation cover + round-trip T2 strict + Primary↔Primary cross-check 100% + fallback 동등성은 **본 PoC 구현 후 별도 합의 영역** (Task #5 영역).

### 7.3 G4 *부분 충족 시제* 한정

본 PoC = G4 §4.4 (hash chain) + §4.6 (round-trip) + §4.2 (11 필드) **부분 충족 시제** 한정. G4 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습 — Memory boundary hook / Skill wrapper / Migration script / `provider_bindings` lint / Memory schema validation 등 4 영역 미적용).

---

## 8. evidence 산출 위치

- 본 합의 보고서: `docs/review/3plus1-consensus-2026-05-10-g4-corpus-poc-scope-short.md`
- Q1 풀 3+1 합의: `docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md`
- Q1 Agent A/B/C 산출: `docs/review/agents-2026-05-10-g4-jcs-library-selection/{agent-a-implementation, agent-b-security, agent-c-alternatives}.md`
- Group C PoC 사양: `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` (§1.1 + §3.1 + §3.4 + §6 + 부록 A + 부록 B 갱신)
- RA-9 evidence: 사양 §B (격리 venv `.poc-prep/jcs-ra9-venv/` + sanity script `.poc-prep/sanity_equivalence.py` + 11/11 동등성 결과)

---

## 9. 다음 진입 단계

| 순서 | 단계 | 형식 | 답습 |
|------|------|------|------|
| 1 | Group C PoC 구현 (Task #5) | 코드 + corpus 26 + fixture 6건 + CI workflow + actual run | Q1 + 본 합의 17 + 6 = 23 조건 답습 의무 |
| 2 | PoC Reviewer-only 단축 합의 (PoC 자체) | Reviewer-only 단축 (Group A/B 답습) | 양방향 검증 + corpus 26 회귀 + chain 4 cover + round-trip T2 + cross-check 100% |
| 3 | CONTEXT/INDEX/SESSION 갱신 (Task #6) | Group A/B 답습 | Group C 종료 + 다음 진입점 후보 등재 |
| 4 | (별도 합의 영역) cross-vendor LLM 의뢰 | 외부 LLM 의뢰 | C-B16 답습, P2 v3 §11.2 cover |
| 5 | (별도 합의 영역) Group H ADR-014 발행 (Migration script) | 풀 3+1 + 외부 LLM 1+ | roadmap §4.1 답습 |

**본 합의 종료 후 즉시 진입 적격 단계 = 1 (Group C PoC 구현)**.

---

> **권한 명시**: 본 합의는 Reviewer-only 단축 — Q4 사용자 명시 결정 답습. Q1 풀 3+1 합의 결과 흡수 + Q2/Q3 사양 *설계 승인* 한정. **G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 권한 0건** + **Hermes PMO 격상 권한 0건** + **ADR 본문 자동 갱신 권한 0건** (사용자 명시 답습).
