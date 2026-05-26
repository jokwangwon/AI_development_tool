# Agent A — 구현/운영 분석 (G4 Q1: Canonical JSON 라이브러리 선정 — `rfc8785` + `jcs` 병렬 cross-check)

**작성일**: 2026-05-10
**Agent 역할**: 구현/운영 분석가 (Implementation / Operability)
**의제**: G4 JSONL Hash Chain + RFC 8785 JCS PoC 의 Canonical JSON 라이브러리 선정 (Q1) — 사용자 명시 결정 갱신 결과 `rfc8785` 0.1.4 (Trail of Bits) + `jcs` 0.2.1 (titusz) **병렬 cross-check** 채택의 운영 가능성
**관점 기준 질문**: "실제로 동작하는가? — 기술적 구현 가능성, 의존성, 성능, 운영 부담"
**상위 권위**: ADR-011 §2.1 (수단/목적 분리), ADR-011 §2.4 (T1/T2/T3), ADR-012 §2.3 / §2.5 / §2.6 / §2.7 / §2.9, G4 §4.2 / §4.4 / §4.6
**금지 (사용자 명시 답습)**: ❌ ADR-012 / G4 본문 해석 변경 / ❌ Implementation/Runtime PASS 선언 / ❌ Hermes PMO 격상 / ❌ 다른 Agent (B, C) 출력 참조 / ❌ Reviewer 합의 예측 / ❌ 신규 정책 발명

**검토 영역 8건** (사용자 명시 답습):
1. `rfc8785` 0.1.4 + `jcs` 0.2.1 병렬 cross-check 의 *실제 구현 가능성* (Python 3.12 환경, install 의존 0, API surface)
2. 양 라이브러리 출력 byte 동등성 강제 시 *성능 overhead* (corpus 24개 + runtime entry 마다 2회 canonicalize)
3. fallback 전략 (`jq -S -c` subprocess + `event: canonical_json_fallback` ledger entry) 합리성
4. Genesis hash MVP 정의 (`sha256("genesis:<scope>:<schema_version>")`) 의 운영 단순성
5. prev_hash 검증 실패 → BLOCK + manual + violation entry 의 운영 적합성 (T3 위반 자동 revert 금지 답습)
6. Round-trip T2 strict (hash 100% 일치) ↔ T3 lossy (entry 자동 작성) 의 운영 부담
7. `event` 11번째 필드 17 enum 중 본 PoC MVP 4종 (`canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) 한정의 적합성
8. CI workflow (corpus 24개 회귀 + chain 4 violation cover + round-trip nightly) 실행 시간 예측

---

## 0. 요약 (Executive Summary) — 본 입력의 입장 + 메타 한계

### 0.1 입장

본 Agent A 분석은 G4 Q1 (`rfc8785` + `jcs` 병렬 cross-check 채택) 의 **운영 가능성 (Operability)** 만을 본다 — 보안/거버넌스는 Agent B 영역, 대안은 Agent C 영역. 핵심 결론:

1. **양 라이브러리 병렬 cross-check 는 운영 가능 (HIGH)** — RA-9 §B.1 결과 `rfc8785` 0.1.4 + `jcs` 0.2.1 모두 PyPI install OK + Apache-2.0 + Hermes 의존 0 + Requires=없음. RA-9 §B.2 11 vector 동등성 11/11 EQUAL (출력 byte + sha256 모두 일치). RFC §A.1 reference (`rfc8785_a1_numbers`) 도 PASS.
2. **API surface 정합성 LOW friction** — `rfc8785.dumps(obj) -> bytes` 는 직접 bytes, `jcs.canonicalize(obj) -> str | bytes` 는 str/bytes 분기 (`.poc-prep/sanity_equivalence.py:26-27` 답습 — `isinstance(out_jcs, str): out_jcs = out_jcs.encode("utf-8")` adapter 필요). `tools/canonical_json.py` 에 1줄 normalization wrapper 의무.
3. **성능 overhead 는 운영 허용 범위 (LOW)** — corpus 24개 × 2 라이브러리 = 48 canonicalize 회귀 = 추정 ms 단위. runtime entry 마다 2회 canonicalize 는 entry 당 µs 단위 (sha256 계산 자체가 Python 에서 µs 단위 답습). 양 라이브러리 모두 pure Python 또는 C 가속 — `jcs` 는 pure Python 계산 비용이 약간 더 높을 가능성, 단 본 PoC corpus 규모에서 무시 가능.
4. **fallback (`jq -S -c` subprocess + `canonical_json_fallback` entry) 는 합리적** — ADR-012 §2.5 명시 답습 + `canonical_json_fallback` enum 17번째 발화 의무 + Reviewer 알림. 단 운영 risk: subprocess overhead = 양 라이브러리 모두 install 실패 시에만 발화 — 본 RA-9 결과 양 install 모두 OK 이므로 *cold path*.
5. **Genesis hash MVP 정의 (`sha256("genesis:<scope>:<schema_version>")`) 는 운영 단순성 HIGH** — 외부 의존 0 (Python 표준 hashlib + f-string), schema_version 0.2 진입 시 새 chain 정책은 ADR-012 §2.6 답습 명시.
6. **prev_hash 검증 실패 → BLOCK + manual + `chain_violation_detected` entry 자동 작성 = 운영 적합** — T3 위반 자동 revert 금지 (ADR-011 §2.4) 답습. dual write 금지 + 원본 보존 + 사용자 명시 review 의무 = 1인 동일 호스트 환경에서 *수동 결정 부담* 발생, 단 본 PoC 검증 단계에서는 fixture 기반 = 운영 부담 LOW.
7. **round-trip T2 strict ↔ T3 lossy 분리는 본 PoC 범위 한정에서 운영 부담 LOW** — JSONL → JSONL 동일 형식 round-trip 한정 (G4 §4.6.1 답습 = cross-format 미적용 = Group H 영역). 본 PoC 의 T2 strict 는 hash 100% 일치 = canonical JSON 결정성 직접 검증. T3 lossy 는 본 PoC 범위에서 *형식 차원 검증* 만 (의미 보존 review 자동화 금지 — G4 §4.6.4 답습).
8. **`event` 17 enum 중 MVP 4종 한정 (`canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`) 은 본 PoC 범위 적합** — ADR-012 §2.2 17 enum 전체 검증은 별도 합의 (G4 §11.4 P-X 영역). 본 PoC 4종은 모두 *T1 audit / T3 BLOCK* 영역 — Hermes 자동 정책 변경 금지 답습.
9. **CI workflow 실행 시간 예측 ≤ 5분** — setup (Python 3.11 + `rfc8785` + `jcs` install + `jq` install) ≈ 30s, corpus 24개 회귀 (양 라이브러리 cross-check) ≈ 5s, fallback 동등성 ≈ 10s (subprocess 24회), PASS/FAIL fixture 6건 ≈ 5s, round-trip ≈ 5s, Evidence summary ≈ 5s. nightly round-trip 별도 schedule.
10. **판정**: **APPROVE WITH CONDITIONS** — Q1 사용자 명시 결정 갱신 (rfc8785 + jcs 병렬) 은 운영 가능성 적격. 8 조건 충족 시 본 PoC 진입 적격 (§4 참조).

### 0.2 메타 한계

본 Agent A 는 **메인 컨텍스트와 동일 패밀리 (Claude)**. 본 분석의 자기참조 위험은 본 합의 Reviewer 종합 시 외부 LLM 1+ 의견으로 통제 (ADR-012 C-14 답습 — P2 v3 정식 채택 진입 *전* 의무). 본 입력은 *합의 본부* 가 아니라 *Reviewer 가 종합할 한 입력* — APPROVE / BLOCK 판정도 본 입력의 *Agent A 관점* 한정 (단일 권위 아님).

본 Agent A 는 *G4 PoC 사양 작성 컨텍스트와 동일 패밀리* — 자기 작성 산출 자기 검토 위험 잔존. RA-9 §B.6 evidence 산출 (`.poc-prep/sanity_equivalence.py` 11 vector) 은 *동일 컨텍스트 자기 실행 결과* — 본 PoC 구현 시 corpus 24개 회귀로 *재검증 의무* (TR-C-2 trigger 등록 답습).

---

## 1. 검토 evidence 목록 (직접 읽은 파일)

| # | 파일 | 위치 | 본 분석 인용 |
|---|------|------|-----------|
| 1 | `g4-jsonl-hash-chain-jcs-poc-spec.md` | `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` (432 줄) | 본 의제 본문 + §B RA-9 evidence + 부록 A 의존 매트릭스 + §6 CI workflow + §9.1 escalation trigger |
| 2 | `ADR-012-evidence-ledger-protection.md` | `docs/decisions/ADR-012-evidence-ledger-protection.md` | §2.2 (`event` 17 enum) + §2.3 (Layer 1 hash chain) + §2.5 (RFC 8785 JCS Primary + jq fallback) + §2.6 (Genesis Hash) + §2.7 (prev_hash 실패 BLOCK + manual + violation entry) + §2.9 (round-trip 3 ledger entry 형식) + §3.4 (timestamp monotonicity) + §3.5 (운영 부담 monitoring trigger) |
| 3 | `provider-agnostic-memory-skill-design.md` | `docs/architecture/provider-agnostic-memory-skill-design.md` | §4.2 (11 필드 schema, `event` 11번째) + §4.4.1~§4.4.5 (Layer 1~5 + JCS Primary/fallback + Genesis + prev_hash 실패 + Full Rewrite) + §4.6.1~§4.6.7 (round-trip Tier-based) |
| 4 | `sanity_equivalence.py` | `.poc-prep/sanity_equivalence.py` (45 줄) | RA-9 11 vector 동등성 sanity check 스크립트 — 본 PoC corpus 24개 회귀 시 재검증 의무 |
| 5 | (보조) `agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` | (Group A 2차 PR-2 — 직전 Agent A 형식 패턴 답습 참조 한정) | 본 Agent A 작성 형식 답습 (직접 결론 인용 0건 — 별 의제) |

본 분석은 위 4 evidence 의 *내용 답습* 만 — ADR-012 / G4 본문 해석 변경 0건 (사용자 명시 답습).

---

## 2. 영역별 분석 (8 영역)

### 2.1 영역 1 — `rfc8785` 0.1.4 + `jcs` 0.2.1 병렬 cross-check 의 실제 구현 가능성

**사실 인용**:

- RA-9 §B.1 (`docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` Line 358~366) — `rfc8785` 0.1.4 PyPI install OK / Apache-2.0 / Trail of Bits / Requires=없음 / API: `dump`, `dumps`, `CanonicalizationError`, `FloatDomainError`, `IntegerDomainError` / NaN reject = `FloatDomainError: nan is not representable in JCS`.
- RA-9 §B.1 — `jcs` 0.2.1 PyPI install OK / Apache-2.0 / titusz (`tp@py7.de`) / Requires=없음 / API: `canonicalize`, `ntoj` / NaN reject = `ValueError: Invalid JSON number: nan`.
- RA-9 §B.2 (Line 369~384) — 11 vector 모두 출력 byte 동등 + sha256 동등 (`number_int` vs `number_float_one` 동일 hash 발생 = RFC 8785 §3.2.2 IEEE 754 동등 답습).
- `.poc-prep/sanity_equivalence.py:24-31` — `rfc8785.dumps(inp)` → bytes 직접 / `jcs.canonicalize(inp)` → str 또는 bytes (`isinstance(out_jcs, str): out_jcs = out_jcs.encode("utf-8")` adapter 필요).
- 부록 A (Line 338~339) — 양 라이브러리 모두 PyPI Apache-2.0 + Trail of Bits / titusz 책임 주체.

**운영 평가**:

- ✅ **Python 3.12 환경 install 가능성 HIGH** — RA-9 venv (`.poc-prep/jcs-ra9-venv/`) 격리 install 양 모두 OK 검증 완료.
- ✅ **install 의존 0 (Hermes / provider SDK 0건)** — ADR-008 차단조건 #2 (Evidence Ledger Hermes 의존 0) 충족.
- ⚠️ **API surface 차이 (str vs bytes 반환)** — `tools/canonical_json.py` 에 *normalization wrapper* 의무 (본 PoC 구현 시 1줄 처리). `.poc-prep/sanity_equivalence.py:26-27` 가 이미 패턴 답습 — 운영 risk LOW.
- ✅ **NaN/Infinity reject 양 모두 정상** (RFC 8785 §3.2.2.2 답습) — 본 PoC corpus number 카테고리 (Line 140) "NaN/Infinity 입력 = reject" 직접 답습.
- ⚠️ **양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2)** — sanity 11/11 EQUAL 이지만 corpus 24개 (8 카테고리 × 3) 본 PoC 구현 시 재검증 의무. *현 시점 evidence = sanity 11 vector 한정* — corpus 24개 100% 동등성은 *본 PoC 구현 후 입증 영역*.
- ✅ **provider-neutral PyPI** — 헌법 5조 (Provider Liquidity) 보존 HIGH.

**평가 결론**: 운영 가능성 **HIGH** (단 corpus 24개 본 PoC 구현 시 재검증 의무 — RA-9 sanity 11 vector 만으로 24개 보장 미성립).

### 2.2 영역 2 — 양 라이브러리 출력 byte 동등성 강제 시 성능 overhead

**사실 인용**:

- §1.1 (Line 35) — `tools/canonical_json.py` 책무 = "RFC 8785 JCS Primary — `rfc8785` (Trail of Bits) + `jcs` (titusz) 병렬 cross-check".
- §3.1 (Line 111) — "본 PoC 는 *두 라이브러리 모두 사용* — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제".
- §3.4 corpus 24개 = 8 카테고리 × 3 (Line 137~146).
- §6 CI workflow step "corpus 회귀" + "fallback 동등성" 분리 (Line 242~243).
- ADR-012 §3.5 (Line 414~419) — 운영 부담 monitoring trigger: "Ledger entry 작성 평균 시간 > 30초 → 단순화 합의 트리거", "Fallback 사용 빈도 > 10% → JCS Primary 검토 합의".
- RA-9 §B.2 11 vector — 양 라이브러리 cross-check 가 *수동 검증 시점* 에서 즉시 완료 (Python 표준 시간 ms 단위 추정).

**운영 평가**:

- ✅ **corpus 24개 회귀 cross-check overhead = 추정 ms 단위** — sanity 11 vector 가 즉시 완료된 패턴 답습. 24개 × 2 라이브러리 = 48 canonicalize call → 추정 50~200ms (Python 3.11 stdlib hashlib + 양 라이브러리 pure Python or C).
- ⚠️ **runtime entry 마다 2회 canonicalize overhead** — 본 PoC 의 hash 계산 자체는 1회 canonicalize (Primary). 단 cross-check 강제 시 entry 마다 *2회* canonicalize 발생 = entry 당 µs~ms 단위 추가. ADR-012 §3.5 monitoring trigger ("Ledger entry 작성 평균 시간 > 30초") 는 본 PoC overhead 와 무관 — 본 PoC overhead 는 trigger 아래.
- ⚠️ **`jcs` (titusz) pure Python 추정 — `rfc8785` 와 비교 시 약간 더 느릴 가능성** — sanity 11 vector 즉시 완료 패턴에서 차이 미관측, 단 corpus 24개 또는 대규모 entry 시 차이 발생 가능. 본 PoC 범위 (24개 + fixture 6건) 에서는 무시 가능.
- ✅ **`tools/canonical_json.py` API 권고 — Primary = `rfc8785` 단독, cross-check 는 corpus 회귀 step 한정** — runtime entry 마다 2회 canonicalize 강제 시 overhead ↑ + 양 라이브러리 의견 불일치 시 BLOCK 위험 (현재 sanity 11/11 EQUAL 이지만 비-sanity case 의 0% 보장 미성립).
  - 본 권고는 PoC 사양 §1.1 / §3.1 의 "두 라이브러리 모두 사용" *해석 영역* — Reviewer 영역. 본 Agent A 권고: corpus 회귀 step 한정 cross-check + runtime entry 는 Primary 단독 (조건 §4 C-A4 답습).

**평가 결론**: 성능 overhead **LOW** (corpus 회귀 한정 cross-check 시) / **MEDIUM** (runtime entry 마다 cross-check 강제 시 — 운영 부담 + 의견 불일치 BLOCK risk).

### 2.3 영역 3 — fallback 전략 (`jq -S -c` subprocess + `canonical_json_fallback` ledger entry) 합리성

**사실 인용**:

- §3.2 (Line 117~125) — `jq -S -c .` lex sort + compact + UTF-8 (POSIX 표준 답습). "사용 시 `event: canonical_json_fallback` ledger entry 자동 작성 의무 (ADR-012 §2.5 답습)". "subprocess overhead — Primary 사용 권고, Fallback 은 Primary 라이브러리 install 실패 시 한정".
- ADR-012 §2.5 (Line 209~211) — "Fallback 사용 시 의무: `event: canonical_json_fallback` ledger entry 작성 의무 + Reviewer 알림 + 사용자 review 권장".
- ADR-012 §2.2 enum #17 `canonical_json_fallback` (Line 147) — T1 audit.
- §4.1 (Line 162~165) — "Primary 라이브러리 ImportError → Fallback `jq -S -c` subprocess + `canonical_json_fallback` ledger entry 자동 작성".
- ADR-012 §3.5 (Line 419) — "Fallback 사용 빈도 > 10% → JCS Primary 검토 합의".

**운영 평가**:

- ✅ **`jq -S -c` 는 POSIX 표준 + Hermes 의존 0** — ADR-008 차단조건 #2 직접 답습.
- ✅ **fallback trigger = Primary ImportError 한정** — RA-9 §B.1 양 라이브러리 모두 install OK 입증 → 본 PoC 환경 (CI Ubuntu + Python 3.11) 에서 *cold path*. `setup` step 에서 양 라이브러리 install 실패 시 BLOCK (§6 Line 241).
- ⚠️ **subprocess overhead** — Python `subprocess.run(["jq", "-S", "-c"], ...)` 는 entry 당 ~10~50ms (process spawn + JSON serialize/parse). corpus 24개 fallback 동등성 step 시 ≈ 240ms~1.2s 추정. ADR-012 §3.5 monitoring trigger ("Fallback 사용 빈도 > 10%") 위반 시 정식화 검토 (§9.1 TR-C-4 답습).
- ⚠️ **`canonical_json_fallback` ledger entry 자동 작성 의무 = 본 PoC `event` MVP 4종 중 1건** (Line 90, §1.1 Line 35). entry 마다 자동 작성 = T1 audit 영역 (ADR-012 §2.2 #17).
- ✅ **`jq` 와 RFC 8785 JCS 의 동등성 *모든 케이스 보장 미성립*** — ADR-012 §11.3 (Line 633~635) "본 ADR §2.5 의 fallback `jq -S -c` 가 JCS 와 *모든 케이스 동등* 보장 부재 — test corpus 검증 의무" 답습. 본 PoC §6 fallback 동등성 step (Line 243) "실패 시 rc=1 (Q1 합의 trigger fallback 충돌)" — TR-C-2 escalation 답습.

**평가 결론**: fallback 전략 합리성 **HIGH** (운영 단순 + cold path + monitoring trigger 명시). 운영 risk = `jq` 와 JCS 동등성 미보장 = corpus 24개 fallback 동등성 step 의무 답습.

### 2.4 영역 4 — Genesis Hash MVP 정의의 운영 단순성

**사실 인용**:

- §3.3 (Line 128~130) — `genesis_hash = sha256("genesis:<scope>:<schema_version>")`. ADR-012 §2.6 답습.
- ADR-012 §2.6 (Line 215~219) — MVP (schema_version 0.1) 현 정의 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 `schema_version`) 생성.
- G4 §4.4.3 (Line 478~495) — MVP 정의 + 0.2 진입 시 canonical_json 기반 정의 + 전이 절차 (0.1 chain read-only).
- §4.2 (Line 174~188) — `jsonl_hash_chain.py` 검사 2: "첫 entry 의 `prev_hash` == `genesis_hash(scope, schema_version)` 일치".
- 부록 A (Line 342) — Python stdlib `hashlib.sha256` 만 사용.

**운영 평가**:

- ✅ **외부 의존 0** — Python stdlib `hashlib.sha256` + f-string. 1줄 구현 가능: `hashlib.sha256(f"genesis:{scope}:{schema_version}".encode()).hexdigest()`.
- ✅ **결정성 100%** — input 동일 시 output 동일 (sha256 답습).
- ✅ **scope enum 3종 (`global` / `project` / `session`) × schema_version 0.1 한정 = 3 chain MVP** — Line 84.
- ⚠️ **schema_version 0.2 진입 시 전이 정책 = 본 PoC 범위 외** (G4 §4.4.3 답습 = 별도 합의). 본 PoC = 0.1 한정 검증 → 운영 단순성 유지.
- ✅ **`scope` 또는 `schema_version` 누락 시 BLOCK** — schema validation 단계에서 검증 (§4.2 Line 175~177).

**평가 결론**: Genesis Hash MVP 정의 운영 단순성 **HIGH** (외부 의존 0 + 1줄 구현 + 결정성 100%).

### 2.5 영역 5 — prev_hash 검증 실패 → BLOCK + manual + violation entry 의 운영 적합성

**사실 인용**:

- §4.2 검사 3 (Line 182~185) — "각 entry 의 `prev_hash` == 직전 entry 의 `hash`. 불일치 검출 시 → BLOCK + `chain_violation_detected` ledger entry 자동 작성 (ADR-012 §2.7 답습, violation_type 4종: `prev_hash_mismatch` / `hash_recalculation` / `history_rewrite` / `genesis_mismatch`)".
- ADR-012 §2.7 (Line 234~252) — 처리 절차: 즉시 BLOCK / 기존 원본 보존 (자동 revert 금지 = T3 위반 위험) / 새 violation entry append / 사용자 명시 review 의무 / 자동 revert 금지 / Dual write 금지.
- ADR-011 §2.4 답습 — T3 위반 자동 revert 금지.
- §7 답습 매트릭스 (Line 261) — "ADR-011 §2.4 (T1/T2/T3) — T3 위반 자동 revert 금지: chain violation = BLOCK + manual + violation entry (자동 revert 0건)".
- §5.2 FAIL fixture 4종 (Line 228~233) — `prev_hash_mismatch` / `hash_recalculation` / `missing_event_field` (schema BLOCK) / `roundtrip_lossy_no_entry` (round-trip 영역).

**운영 평가**:

- ✅ **T3 위반 자동 revert 금지 = ADR-011 §2.4 직접 답습** — Hermes 자동 정책 변경 금지 영구 핵심 제약 보호.
- ✅ **violation entry 자동 작성 = T1 audit (ADR-012 §2.2 enum #14 `chain_violation_detected`)** — 자동 정책 변경 0건, 자동 audit 만.
- ⚠️ **1인 동일 호스트 환경 사용자 명시 review 부담** — chain violation 발생 시 *수동 결정 의무*. 본 PoC 검증 단계에서는 fixture 기반 = 운영 부담 LOW. 단 본 PoC 이후 실 runtime entry 발생 시 부담 ↑ (별도 합의 영역 — Implementation/Runtime PASS).
- ✅ **dual write 금지 + 원본 보존** = silent failure 위험 차단 (ADR-012 §2.7 #6 답습).
- ⚠️ **violation_type 4종 vs 본 PoC FAIL fixture 4종 매핑 차이** — §4.2 검사 3 violation_type = `prev_hash_mismatch` / `hash_recalculation` / `history_rewrite` / `genesis_mismatch` (4종). §5.2 FAIL fixture 4종 = `prev_hash_mismatch` / `hash_recalculation` / `missing_event_field` (schema BLOCK) / `roundtrip_lossy_no_entry` (round-trip). *교집합 2건 한정* (`prev_hash_mismatch` + `hash_recalculation`). `history_rewrite` + `genesis_mismatch` fixture 미정의 — 본 PoC 검증 cover 미완 risk.

**평가 결론**: 운영 적합성 **HIGH** (T3 답습 + 자동 revert 금지). 단 violation_type 4종 vs FAIL fixture 4종 *교집합 2건 한정* = 본 PoC 구현 시 fixture 추가 권고 (§4 C-A5 답습).

### 2.6 영역 6 — Round-trip T2 strict ↔ T3 lossy 의 운영 부담

**사실 인용**:

- §4.3 (Line 195~213) — `jsonl_roundtrip.py` 절차: parse → canonical re-export → SHA-256 비교 → T2 strict (hash 일치 100%) → `roundtrip_pass` / 의미 보존 → `roundtrip_lossy` / 실패 → `roundtrip_fail`.
- §4.3 (Line 207) — "본 PoC 는 **JSONL → JSONL 동일 형식 round-trip** 한정. 외부 형식 (Hermes / Claude / OpenAI) ↔ JSONL migration 은 **Group H 영역** (사용자 명시 금지 답습)".
- ADR-012 §2.9 (Line 268~289) — Tier-based + 3 ledger entry 형식 + `lost_fields` enumeration 자동 / `semantic_diff` 사용자 review / 의미 보존 review 자동화 절대 금지.
- G4 §4.6.4 (Line 588~592) 답습.
- §5.1 (Line 222~224) — PASS fixture `roundtrip_t2_strict.jsonl` = canonical JSON re-export 시 hash 100% 일치.
- §6 (Line 246) — Round-trip step "pass/roundtrip_t2_strict.jsonl → jsonl_roundtrip.py rc=0".
- §9.1 TR-C-4 (Line 305) — "round-trip T2 strict 실패율 > 0% (24개 corpus 적용 시) → 풀 3+1 + ADR-012 §2.5 fallback 정식화 검토".

**운영 평가**:

- ✅ **JSONL → JSONL 동일 형식 한정 = 본 PoC 운영 부담 LOW** — cross-format (Group H) 미적용. 사용자 명시 금지 답습 (Line 49 + Line 208).
- ✅ **T2 strict (hash 100% 일치) = canonical JSON 결정성 직접 검증** — sanity 11/11 EQUAL 답습 → 본 PoC corpus 24개 시 동등 기대. 단 fixture `roundtrip_t2_strict.jsonl` 1건만 본 PoC 검증 = corpus 24개 + fixture 1건 한정.
- ⚠️ **T3 lossy entry 작성 = 본 PoC 범위 *형식 차원* 한정** — 의미 보존 review 자동화 금지 (G4 §4.6.4 답습). 본 PoC 는 `lost_fields` enumeration 자동 + `roundtrip_lossy` entry 자동 작성 까지. `semantic_diff` 사용자 review 는 본 PoC 범위 외 (Implementation/Runtime PASS 영역).
- ⚠️ **본 PoC FAIL fixture `roundtrip_lossy_no_entry` (Line 233)** = lossy 발생 시 entry 미작성 BLOCK 검증. 단 *lossy 발생 자체* (round-trip lossy fixture) 는 본 PoC §5 명시 0건 — Q3 corpus 카테고리 "lossy round-trip" (`tests/canonical/lossy/` Line 146) 와 fixture 영역 분리 = 운영상 *cross-reference 명확화 필요*.
- ✅ **TR-C-4 escalation (T2 strict 실패율 > 0%)** = 운영 monitoring 명시.

**평가 결론**: 운영 부담 **LOW** (본 PoC 범위 한정 시). 단 T3 lossy fixture 정의 / corpus lossy 카테고리 cross-reference = 본 PoC 구현 시 명확화 의무 (§4 C-A6 답습).

### 2.7 영역 7 — `event` 11번째 필드 17 enum 중 본 PoC MVP 4종 한정의 적합성

**사실 인용**:

- §2.1 (Line 90) — "`event` enum 17 후보 중 1 (ADR-012 §2.2 답습 — 본 PoC MVP 4종 한정 검증: `canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`)".
- ADR-012 §2.2 (Line 127~149) — 17 enum 전체 + MVP 의무 12 enum + 후속 확장 5 enum.
- G4 §4.2 (Line 398) — "17 enum 후보 (MVP 12 의무 + 5 후속 확장)".
- §1.1 (Line 36) — `tools/jsonl_hash_chain.py` 책무 = "11 필드 schema 검증 + ... + `chain_violation_detected` 자동 작성".
- §1.1 (Line 37) — `tools/jsonl_roundtrip.py` 책무 = "`roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` 3 형식 자동 작성".
- §11 L-3 (Line 328) — "한계: `event` 17 enum 중 MVP 4종 한정 검증".
- §9.1 TR-C-3 (Line 304) — "`event` 17 enum 중 본 PoC MVP 4종 외 추가 발화 → 별도 합의 + ADR-012 §2.2 cross-reference".

**운영 평가**:

- ⚠️ **본 PoC MVP 4종 vs ADR-012 MVP 의무 12 enum 차이** — ADR-012 §2.2 (Line 149) "MVP 의무 12 enum (1~12). 후속 확장 5 enum (13~17, schema_version 0.2 또는 별도 합의)". 본 PoC MVP 4종 = `canonical_json_fallback` (#17) / `chain_violation_detected` (#14) / `roundtrip_lossy` (#11) / `roundtrip_fail` (#12). *3건이 ADR-012 후속 확장 5 enum (13~17) 영역* — `canonical_json_fallback` (#17) + `chain_violation_detected` (#14) = 후속 확장. `roundtrip_lossy` (#11) + `roundtrip_fail` (#12) = MVP 의무 12 enum 영역.
- ✅ **본 PoC = G4 *부분 충족 시제* 한정** (§8 Line 285 답습) — 17 enum 전체 검증 = 별도 합의 (§11 L-3 답습). MVP 4종 한정 = 본 PoC 범위 적절.
- ⚠️ **§5.1 PASS fixture `minimal_chain.jsonl` 의 `event: memory_write` (#1, MVP 의무)** — 본 PoC 검증 대상 (4종) 외 enum 사용 = §9.1 TR-C-3 escalation trigger 발화 위험. 단 fixture 가 *4종 외 enum 을 *발화* 하는 게 아니라 *포함* 하는 형태* — fixture 데이터에 다양한 enum 포함 OK + 본 PoC validator 자동 작성 enum 4종 한정 = 운영상 *해석 명확화 필요* (TR-C-3 발화 여부).
- ✅ **MVP 4종 모두 T1 audit / T3 BLOCK 영역** (ADR-012 §2.2 답습) — Hermes 자동 정책 변경 금지 답습. T2 사용자 명시 영역 미포함 = 자동화 안전성 보장.

**평가 결론**: 본 PoC MVP 4종 한정 적합성 **MEDIUM** (본 PoC 범위 적절, 단 fixture 의 `event: memory_write` 등 4종 외 enum 발화 vs 검증 분리 명확화 의무 = §4 C-A7 답습).

### 2.8 영역 8 — CI workflow 실행 시간 예측

**사실 인용**:

- §6 (Line 240~248) CI workflow 8 step:
  - setup (Python 3.11 + `rfc8785` install + `jq` install)
  - corpus 회귀 (24개 → `to_canonical(input) == expected.canonical` 100%)
  - fallback 동등성 (`rfc8785` vs `jq -S -c` 24개 동등)
  - PASS fixture (`pass/*.jsonl` × 2 → rc=0)
  - FAIL fixture (`fail/*.jsonl` × 4 → rc=1 + 4 violation_type cover)
  - Round-trip (`pass/roundtrip_t2_strict.jsonl` → rc=0)
  - Evidence summary (corpus 24/24 + chain 4/4 cover + round-trip T2 + fallback 동등성)
  - probe cleanup (`if: always()` 답습)
- 부록 A (Line 338~339) — `rfc8785` + `jcs` install (양 cross-check 시 `jcs` 도 step 6 setup 추가 의무 — 본 PoC §6 step 6 setup 명시 미흡 — `jcs` install 누락 risk).
- ADR-012 §3.5 (Line 416) — "Ledger entry 작성 평균 시간 > 30초 → 단순화 합의 트리거".
- Group A 2차 + Group B PoC CI 답습 패턴 (대략 2~5분 실행 시간).

**운영 평가**:

- ✅ **setup ≈ 30s** — Python 3.11 + `pip install rfc8785 jcs` (~10s) + `apt install jq` (~10s) + 환경 setup (~10s).
- ✅ **corpus 회귀 24개 ≈ 5s** — RA-9 sanity 11 vector 즉시 완료 답습 → 24개 × 2 라이브러리 = 48 canonicalize call ≈ 100ms.
- ⚠️ **fallback 동등성 24회 ≈ 10s** — subprocess `jq -S -c` × 24 ≈ 240ms~1.2s + I/O.
- ✅ **PASS/FAIL fixture 6건 ≈ 5s** — fixture parse + chain 검증 = 추정 100ms 이하.
- ✅ **Round-trip ≈ 5s** — T2 strict fixture 1건 + canonical re-export = 추정 50ms.
- ✅ **Evidence summary + probe cleanup ≈ 5s**.
- **합산 예측: ≈ 60s (1분)** — Group A 2차 + Group B PoC CI 실행 시간 답습 (2~5분 추정 범위 *내*).
- ⚠️ **`jcs` install 누락 risk** — §6 setup step (Line 241) "Python 3.11 + `rfc8785` install + `jq` install" 명시. *`jcs` install 미명시* = §1.1 (Line 35) 양 라이브러리 cross-check 와 cross-reference drift = 본 PoC 구현 시 step 6 setup 에 `jcs` install 추가 의무 (§4 C-A2 답습).
- ⚠️ **nightly round-trip schedule 별도** — §1.1 (Line 41) "round-trip nightly" 명시. nightly = GitHub Actions `schedule` 별도 workflow 또는 동일 workflow `on: schedule` 분리 = 본 PoC 구현 시 명확화 의무.

**평가 결론**: CI workflow 실행 시간 ≈ 1분 (운영 적정). 단 `jcs` install setup step 누락 risk + nightly schedule 분리 명확화 의무 (§4 C-A2 + C-A8 답습).

---

## 3. Risk Assessment

본 Agent A 가 운영 가능성 관점에서 식별한 risk (R-N 형식):

| # | 위험 / Gap | 등급 | 근거 |
|---|---------|----|----|
| **R-A1** | corpus 24개 본 PoC 구현 시 양 라이브러리 (`rfc8785` + `jcs`) 동등성 *재검증 의무* — sanity 11 vector 만으로 24개 100% 동등 보장 미성립 | **HIGH** | RA-9 §B.2 11/11 EQUAL 은 *sanity* 한정 + TR-C-2 escalation trigger 등록 답습 (§9.1 Line 303) |
| **R-A2** | §6 setup step `jcs` install 누락 — §1.1 cross-check 와 cross-reference drift | **HIGH** | §6 Line 241 "Python 3.11 + `rfc8785` install + `jq` install" 명시 = `jcs` 누락. 본 PoC CI 실행 시 cross-check 불가 |
| **R-A3** | runtime entry 마다 2회 canonicalize 강제 시 overhead ↑ + 양 라이브러리 의견 불일치 시 BLOCK risk | **MEDIUM** | §1.1 (Line 35) "병렬 cross-check" 해석 영역. corpus 회귀 한정 cross-check + runtime entry Primary 단독 권고 |
| **R-A4** | violation_type 4종 (§4.2 Line 185) vs FAIL fixture 4종 (§5.2 Line 228~233) *교집합 2건 한정* — `history_rewrite` + `genesis_mismatch` fixture 미정의 | **MEDIUM** | 본 PoC 검증 cover 미완. fixture 추가 또는 cross-reference 명확화 의무 |
| **R-A5** | T3 lossy fixture 정의 0건 vs corpus `lossy` 카테고리 (Line 146) 분리 | **MEDIUM** | round-trip lossy 검증 evidence 부족 — 본 PoC 구현 시 lossy fixture 추가 또는 corpus cross-reference 명시 |
| **R-A6** | `event` MVP 4종 한정 검증 vs fixture 의 `event: memory_write` 등 4종 외 enum 사용 = TR-C-3 발화 해석 모호 | **MEDIUM** | §5.1 PASS fixture (Line 223) `event: memory_write` (4종 외) 사용. *발화* vs *포함* 분리 명확화 의무 |
| **R-A7** | `jcs` (titusz) pure Python 구현 추정 — 대규모 entry 시 `rfc8785` 와 성능 차이 발생 가능 | **LOW** | sanity 11 vector 즉시 완료 답습. 본 PoC corpus 24개 + fixture 6건 규모에서 무시 가능 |
| **R-A8** | nightly round-trip schedule 분리 명확화 부재 — `on: schedule` cron 정의 미명시 | **LOW** | §1.1 (Line 41) "round-trip nightly" 명시 vs §6 step 단일 workflow = 분리 의무 |
| **R-A9** | `jq` 와 RFC 8785 JCS 동등성 모든 케이스 보장 미성립 — fallback 동등성 step 의무 답습 | **LOW** | ADR-012 §11.3 (Line 633~635) 답습. §6 fallback 동등성 step 명시 = 운영 cover OK |
| **R-A10** | `tools/canonical_json.py` API surface 차이 (str vs bytes) normalization wrapper 의무 | **LOW** | `.poc-prep/sanity_equivalence.py:26-27` 패턴 답습. 1줄 처리 = 운영 부담 LOW |

**HIGH 위험 2건 (R-A1, R-A2)** = 본 PoC PASS 의 binary 조건. **MEDIUM 4건 (R-A3, R-A4, R-A5, R-A6)** = PASS 후 흡수 가능 또는 본 PoC 구현 시 명확화. **LOW 4건 (R-A7, R-A8, R-A9, R-A10)** = 본 PoC 본문 또는 Implementation 시 흡수.

**CRITICAL 위험 0건** — 양 라이브러리 install OK + Hermes 의존 0 + Apache-2.0 + sanity 11/11 EQUAL = ADR-008 차단조건 #2 + 헌법 5조 (Provider Liquidity) + ADR-011 §2.4 (T3 답습) 모두 보호.

---

## 4. 추가 권고 조건 (조건부 APPROVE 시 명시)

본 Agent A 가 **APPROVE WITH CONDITIONS** 판정의 8 조건 enumeration:

### 4.1 본 PoC 진입 *전* 의무 (P0)

**C-A1**. **corpus 24개 동등성 재검증 의무 명시** (R-A1) — 본 PoC 구현 첫 step 으로 `rfc8785` + `jcs` corpus 24개 출력 byte + sha256 동등성 100% 검증 + Evidence 산출. 1+ case 불일치 시 TR-C-2 escalation 발화 (§9.1 답습).

**C-A2**. **§6 setup step 에 `jcs` install 추가 의무** (R-A2) — `pip install rfc8785 jcs` 또는 `requirements.txt` 명시. cross-check 강제 cross-reference 보존.

### 4.2 본 PoC 구현 시 의무 (P1)

**C-A3**. **`tools/canonical_json.py` API 권고: corpus 회귀 step 한정 cross-check + runtime entry Primary (`rfc8785`) 단독** (R-A3) — runtime entry 마다 2회 canonicalize 강제 시 overhead + BLOCK risk. Reviewer 영역 (단일 권위 아님).

**C-A4**. **`canonical_json.py` API normalization wrapper 의무** (R-A10) — `jcs.canonicalize()` str/bytes 분기 처리 (`.poc-prep/sanity_equivalence.py:26-27` 패턴 답습).

**C-A5**. **violation_type 4종 cover 의무 — FAIL fixture 추가 (`history_rewrite` / `genesis_mismatch`) 또는 cross-reference 명확화** (R-A4) — 본 PoC 검증 cover 완전성 보장.

**C-A6**. **T3 lossy fixture 정의 또는 corpus `lossy` 카테고리 cross-reference 명시** (R-A5) — round-trip lossy 검증 evidence 보강.

**C-A7**. **`event` MVP 4종 한정 검증 = *validator 자동 작성 enum* 한정 + fixture 의 다양한 enum 포함 OK 명확화** (R-A6) — TR-C-3 발화 vs 미발화 해석 모호 차단.

### 4.3 본 PoC 구현 시 의무 (P2)

**C-A8**. **nightly round-trip schedule 분리 명시 — `.github/workflows/g4-hash-chain.yml` 의 `on: schedule` cron 정의** (R-A8) — 본 PoC §1.1 "nightly" 명시 vs §6 단일 workflow 분리 의무.

**P0 조건 (필수, 본 PoC 진입 차단)**:
- C-A1 (corpus 24개 동등성 재검증)
- C-A2 (`jcs` install setup 추가)

**P1 조건 (강력 권고, 본 PoC 구현 시 흡수)**:
- C-A3 (cross-check API 권고)
- C-A4 (normalization wrapper)
- C-A5 (violation_type 4종 cover)
- C-A6 (T3 lossy fixture)
- C-A7 (`event` MVP 4종 한정 명확화)

**P2 조건 (본 PoC 구현 시 명확화)**:
- C-A8 (nightly schedule 분리)

---

## 5. 영구 핵심 제약 보호 점검 (5 제약)

본 Q1 결정 (rfc8785 + jcs 병렬 cross-check) 가 *답습해야 하는* 5 영구 핵심 제약 점검:

| 제약 | 권위 근거 | 본 Q1 보호 위치 | 점검 결과 |
|------|--------|-----------|--------|
| **Provider Liquidity** (헌법 5조 관용) | 헌법 5조 + ADR-008 차단조건 #2 + G4 §3.5 + §4.3 + §6.4 (4-way) + ADR-012 5-way | RA-9 §B.4 (Line 396~399) "두 라이브러리 모두 provider-neutral PyPI (Anthropic / OpenAI / Google SDK 의존 0) → 헌법 5조 (Provider Liquidity) 보존 HIGH". `jq` fallback POSIX 표준 | ✅ PASS — 양 라이브러리 + fallback 모두 provider-neutral |
| **Hermes ≠ root of trust** (ADR-011 §2.3) | ADR-011 §2.3 영구 권위 | 본 PoC 의 모든 도구 (canonical JSON / hash chain / round-trip validator) 는 *Tools 검증* 영역 — Hermes 출력 검증 권위. 본 Q1 라이브러리 선정 = Hermes 의존 0 (RA-9 §B.4 답습) | ✅ PASS — Hermes 의존 0 |
| **메타포 강제 금지** (system-identity-prequel §7) | prequel §7 (P2 v3 §10 흡수) | 본 Q1 = *기술 라이브러리 선정* — 메타포 인플레이션 0. RFC 8785 JCS 표준 답습 | ✅ PASS — 메타포 강제 0 |
| **자동 정책 변경 금지 (T3)** (ADR-011 §2.4) | ADR-011 §2.4 | chain violation = BLOCK + manual + violation entry (자동 revert 0건) — §7 답습 매트릭스 (Line 261). MVP 4종 enum 모두 T1 audit / T3 BLOCK 영역 (T2 사용자 명시 영역 미포함) | ✅ PASS — T1/T2/T3 분리 답습 |
| **수단/목적 분리 원칙** (ADR-011 §2.1) | ADR-011 §2.1 (a)~(e) | 본 Q1 = *수단* (canonical JSON 라이브러리), *목적* = Evidence 무결성 결과. (a)~(e) 5조건 답습 (PoC §7 매트릭스 Line 256~260) | ✅ PASS — (a)~(e) 5조건 답습 |

**5 영구 핵심 제약 모두 보호됨** (5/5 HIGH).

---

## 6. 본 입력이 *하지 않는* 것 (사용자 명시 답습)

본 Agent A 입력은 다음 모두 *발생시키지 않는다*:

1. ❌ **ADR-012 / G4 본문 해석 변경** — 답습 시제 한정. 본 분석은 사양 본문 *인용 + 운영 평가* 까지.
2. ❌ **Implementation/Runtime PASS 선언** — 본 PoC = G4 *부분 충족 시제* 한정 (PoC 사양 §8 #1 답습).
3. ❌ **Hermes PMO 격상 선언** — 사용자 명시 금지 (PoC 사양 §1.2 답습).
4. ❌ **다른 Agent (B, C) 출력 참조** — 본 입력은 Agent A 단독 분석. Reviewer 종합 영역.
5. ❌ **Reviewer 합의 예측** — 본 입력의 APPROVE / BLOCK 판정은 *Agent A 관점* 한정. 합의 본부는 Reviewer 종합 영역.
6. ❌ **신규 정책 발명** — roadmap §4.1 + ADR-012 §2 + G4 §4 명세 그대로 답습. 본 분석에서 식별한 risk / 조건은 *기존 권위 cross-reference* 한정.
7. ❌ **다른 라이브러리 후보 평가** — 본 Q1 = `rfc8785` + `jcs` 병렬 채택 결정 검토 한정. `canonicaljson` (Matrix.org) 등 대안 = Agent C 영역.
8. ❌ **메타포 강제** — 본 분석은 *기술 라이브러리 운영 평가* 한정. 메타포 인플레이션 0.

---

## 7. 최종 판정

```
APPROVE WITH CONDITIONS
```

### 7.1 핵심 조건 1줄 요약

**G4 Q1 (rfc8785 + jcs 병렬 cross-check 채택) 의 운영 가능성 적격 — 8 조건 (corpus 24개 동등성 재검증 + `jcs` install setup + cross-check API 권고 + normalization wrapper + violation_type 4종 cover + T3 lossy fixture + `event` MVP 4종 한정 명확화 + nightly schedule 분리) 충족 시 본 PoC 진입 적격.**

### 7.2 판정 근거

운영 가능성 측면에서 본 Q1 결정 (rfc8785 + jcs 병렬 cross-check) 는 다음 사실에서 적격:

1. RA-9 §B.1 양 라이브러리 모두 PyPI install OK + Apache-2.0 + Hermes 의존 0 + Requires=없음 (Provider Liquidity HIGH).
2. RA-9 §B.2 11 vector 동등성 11/11 EQUAL (출력 byte + sha256 모두 일치, RFC §A.1 reference 포함).
3. fallback (`jq -S -c` + `canonical_json_fallback` entry) 운영 단순 (POSIX 표준 + cold path + monitoring trigger 명시).
4. Genesis Hash MVP 정의 운영 단순성 HIGH (Python stdlib hashlib 1줄 구현).
5. prev_hash 검증 실패 BLOCK + manual + violation entry = T3 답습 (ADR-011 §2.4) 직접 보호.
6. Round-trip JSONL → JSONL 동일 형식 한정 (cross-format Group H 영역) = 본 PoC 부담 LOW.
7. CI workflow 실행 시간 ≈ 1분 (Group A 2차 + Group B 답습 범위 *내*).
8. 5 영구 핵심 제약 모두 보호 (5/5 HIGH).

### 7.3 본 판정의 한계

- 본 Agent A 는 *다른 Agent (B, C) 출력 미참조* — 보안 / 거버넌스 / 대안 측면 미평가. Reviewer 종합 시 보강.
- 본 Agent A 는 *RA-9 산출 자기 컨텍스트 검토* — 자기 작성 산출 자기 검토 위험 잔존. 외부 LLM 1+ (cross-vendor) 의견은 본 Agent A 대체 불가 (ADR-012 C-14 답습).
- corpus 24개 동등성 재검증은 *본 PoC 구현 후 입증 영역* — 현 시점 evidence = sanity 11 vector 한정 + corpus 0% 보장 미성립 (R-A1).
- 운영 부담 추정 (CI ≈ 1분, 본 PoC 구현 시간 별도) 은 *합의 + 사양 + 본 PoC 구현 합산* 미포함 — Group A/B 답습 패턴 1.5~2.5일 추정 (별도 영역).
- 본 Agent A 는 *cryptography specialist 미보유* — RFC 8785 JCS 동등 구현 검증의 심층 평가는 본 합의 검토자 한계 (ADR-012 §11.3 답습).

---

**작성일**: 2026-05-10
**작성자**: Agent A (구현/운영 가능성 분석가)
**판정**: ✅ **APPROVE WITH CONDITIONS** (8 조건 — §4)
**핵심 조건 1줄 요약**: G4 Q1 (rfc8785 + jcs 병렬 cross-check) 의 운영 가능성 적격 — corpus 24개 동등성 재검증 + `jcs` install setup + cross-check API 권고 + normalization wrapper + violation_type 4종 cover + T3 lossy fixture + `event` MVP 4종 한정 명확화 + nightly schedule 분리 8 조건 충족 시 본 PoC 진입 적격.
**상위 Reviewer 인계 사항**:
- HIGH 위험 2건 (R-A1 corpus 24개 동등성 재검증, R-A2 `jcs` install setup 누락) 은 본 PoC 진입 *전* binary 조건
- MEDIUM 4건 (R-A3 cross-check API 권고, R-A4 violation_type 4종 cover, R-A5 T3 lossy fixture, R-A6 `event` MVP 4종 한정 명확화) 은 본 PoC 구현 시 흡수
- LOW 4건 (R-A7 `jcs` 성능, R-A8 nightly schedule, R-A9 jq 동등성, R-A10 normalization wrapper) 은 본 PoC 본문 또는 Implementation 시 흡수
- 본 Agent A 는 *운영 가능성* 측면 한정 — 보안 (Agent B) / 대안 (Agent C) / 외부 LLM 검증 종합 의무
