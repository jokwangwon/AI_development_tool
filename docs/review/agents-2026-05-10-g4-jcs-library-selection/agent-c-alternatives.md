# Agent C — 대안/단순화 분석 (G4 Q1: Canonical JSON 라이브러리 선정)

**작성일**: 2026-05-10
**Agent 역할**: 대안/단순화 탐색 (Alternatives & Simplification)
**검토 의제**: G4 JSONL hash chain + RFC 8785 JCS PoC 의 **Canonical JSON 라이브러리 선정 (Q1)** — 사용자 명시 결정 갱신 결과 `rfc8785` (Trail of Bits) + `jcs` (titusz) **병렬 corpus 24개 cross-check** 채택. 본 합의는 풀 3+1 형식 (Q4 결정 답습).
**관점**: "더 나은 방법이 있는가? — `rfc8785` 단독으로 충분한가? cross-check 비용은 정당한가? `jq` fallback 외 더 단순한 fallback 은? corpus 24개는 적정인가? 본 PoC 범위에서 분리 가능한 영역은?"
**검토 영역 10건**: (1) 단순화 대안 / (2) 라이브러리 enumerate / (3) fallback 대안 / (4) cross-check overhead / (5) canonicaljson 비채택 사유 / (6) PoC 범위 단순화 / (7) corpus 24 vs 20 / (8) round-trip T2/T3 / (9) `event` 17 vs 4 / (10) 표준 도구 단독 가능성
**금지 사항 답습** (사용자 명시): G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 / Hermes PMO 격상 선언 / 실 migration script 본 구현 / ADR 본문 자동 갱신 / 신규 정책 발명 / Hermes 의존 도입 — 모두 본 분석 범위 외
**메타 명시**: 본 Agent C 도 메인 컨텍스트와 *동일 Claude 패밀리* 자기 작성 산출 — G3 §4 자기참조 차단 적용 대상. 외부 LLM 1+ 의견 격상 가능성 평가는 §5 권고 조건 영역.

---

## 0. 요약

본 Agent C 는 G4 PoC Q1 (Canonical JSON 라이브러리 선정) 의 *대안 합의 형태* 와 *단순화 가능성* 을 평가했다. 사용자 명시 갱신 결정 = `rfc8785` + `jcs` 병렬 cross-check (RA-9 §B.3 결과 흡수). 핵심 발견:

1. **사용자 명시 갱신 결정 (Alt-1, 병렬 cross-check) 은 *조건부 정당*** — RA-9 §B.2 sanity 11/11 동등성 PASS + ADR-008 차단조건 #2 (Hermes 의존 0) 양 라이브러리 충족 + Provider Liquidity HIGH. 단, *cross-check overhead (corpus 24 + runtime entry 마다 2× canonicalize)* 의 정당성은 본 PoC 범위에서 *조건부*. 본 Agent C 는 **단순화 대안 3건 enumerate** + Alt-1 채택 시 *조건부 적격* 평가.
2. **`rfc8785` 단독 (Alt-2) 도 정당** — Trail of Bits + Apache-2.0 + RFC 명시 구현 + NaN/Inf reject + 의존 0 → ADR-008 차단조건 #2 + Provider Liquidity 모두 충족. cross-check 비용 0. 단, *cryptography 영역 검토자 한계* (ADR-012 §11.3) → corpus 24개 reference output 이 *유일 검증 layer* 가 됨. 단일 implementation bug 위험 있음.
3. **`jq -S -c` fallback 은 *적정* 한계 보유** — POSIX 표준 + 외부 의존 최소 + ADR-012 §2.5 명시 답습 정당. 단, subprocess overhead + jq 가 RFC 8785 *완전* 동등 보장 부재 (ADR-012 §11.3 답습). stdlib `json.dumps(sort_keys=True, ...)` 은 *추가* fallback 이 아니라 *비-fallback* — RFC 8785 number normalization (IEEE 754) 미구현. 본 PoC 범위 외.
4. **corpus 24개 (8 카테고리 × 3) = 적정 균형** — ADR-012 §2.5 ≥20개 답습 + 1인 개발자 비용 관리. 단순화 대안 (8 카테고리 × 2 = 16개) 은 lossy round-trip 영역 case 부족 위험. **24개 유지 권고**.
5. **PoC 범위 6 영역 = 적정 통합** — schema / canonical / prev_hash / chain violation / round-trip / failure event 6 영역은 사용자 Q3 결정 답습. 분리 가능 영역 후보: round-trip T3 lossy 영역 *분리* (별도 후속 PoC) — 단순화 권고 안 #2.
6. **`event` 17 enum 중 MVP 4종 한정 검증 = 적정** — ADR-012 §2.2 답습 + L-3 한계 명시 답습. 본 Agent C 는 4종 → 3종 추가 단순화 *비권고* (`canonical_json_fallback` 은 fallback layer 자체와 직결 의무).
7. **표준 도구 (`jq` + `sha256sum` + Python stdlib) 단독 = *비채택 권고*** — ADR-008 차단조건 #2 (Hermes 의존 0) 는 *Hermes* 의존 0 의미이지, *PyPI provider-neutral 라이브러리* 의존 0 의미 아님. RFC 8785 의 number normalization (IEEE 754) + escape 처리는 stdlib `json.dumps` 만으로 *완전* 등가 구현 부담 = 1인 개발자 비용 격증 (Reviewer 한계 영역 — ADR-012 §11.3 답습). 본 Agent C 는 *별도 라이브러리 의존 정당화* 평가.

**판정** (Agent C 단독, Reviewer 종합 대상):

```
APPROVE WITH CONDITIONS
```

본 Q1 (사용자 명시 갱신 결정 = Alt-1 병렬 cross-check) 진행 적격이나, 다음 5 조건 권고 (§5 enumerate):
- C-C1 (cross-check overhead 의 *정량 measurement* 본 PoC 구현 시 의무 — TR-C-2 발화 시 Alt-2 단독 격상 trigger)
- C-C2 (Alt-2 `rfc8785` 단독 backup plan 본 PoC 사양 §B.5 escalation 매트릭스 cross-reference 명시)
- C-C3 (`canonicaljson` Matrix.org 비채택 사유 본 PoC 사양 부록 A 또는 §3.2 명시 보강)
- C-C4 (`jq` fallback 의 RFC 8785 *완전 동등성 부재* 한계 명시 — ADR-012 §11.3 답습)
- C-C5 (cryptography 영역 검토자 한계 명시 — 외부 LLM 1+ blind 의뢰 영역 *권고* 격상 — ADR-012 §11.3 + C-14 답습)

---

## 1. 검토 evidence 목록 (직접 읽은 파일)

| # | 파일 | 검토 영역 |
|---|------|--------|
| 1 | `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` | 본 의제 본문 (§3 Canonical JSON Primary + Fallback) + §B RA-9 evidence (B.1~B.6) + 부록 A 의존 매트릭스 |
| 2 | `docs/decisions/ADR-012-evidence-ledger-protection.md` | §2.5 (RFC 8785 JCS Primary + jq fallback) + §11.3 (cryptography 영역 검토자 한계) + 원칙 5 (Hermes 의존 0) + §3.5 운영 부담 monitoring trigger (Fallback 사용 빈도 > 10%) |
| 3 | `docs/architecture/provider-agnostic-memory-skill-design.md` | §4.4.2 (Canonical JSON RFC 8785 JCS Primary + Fallback) + §4.4 (hash chain 다층 강제) + §11.4 (P-1 RFC 8785 JCS 자기 명시 한계) |
| 4 | `docs/architecture/implementation-runtime-roadmap.md` | §4.1 (G4 7 영역 — Order 3 tie 3건: hash chain / JCS / round-trip) + §4.2 (G4 우선순위 합산) |
| 5 | `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-c-alternatives.md` | 답습 형식 reference (424 줄, 2026-05-09 Agent C 보고서) |

본 Agent C 분석은 위 5건 + ADR-008 차단조건 #2 + ADR-011 §2.1 (a)~(e) + ADR-011 §2.4 (T1/T2/T3) cross-reference 한정. 다른 Agent (A, B) 출력 본 분석 시점 *부재* (병렬 독립 분석 패턴 답습 — CLAUDE.md §3 Phase 2).

---

## 2. 영역별 분석 (10 영역)

### 2.1 영역 1 — 단순화 대안 (`rfc8785` 단독 vs 병렬 cross-check)

**사실 인용**:
- PoC 사양 §3.1: "Q1 사용자 명시 결정 갱신 답습 (2026-05-10, RA-9 §B.3 발견 후) — `rfc8785` 0.1.4 (Trail of Bits, Apache-2.0) + `jcs` 0.2.1 (titusz, Apache-2.0) **병렬 corpus 24개 cross-check** 채택"
- PoC 사양 §B.2: 11/11 EQUAL (hash 동일 + 출력 byte 동일) — sanity check PASS
- PoC 사양 §B.4: 양 라이브러리 모두 의존 0 + ADR-008 차단조건 #2 충족 + Provider Liquidity HIGH

**단순화 평가**:
- Alt-1 (병렬 cross-check, 사용자 명시 갱신): cross-check 비용 = corpus 24 + runtime entry 마다 2× canonicalize. *implementation bug detection* layer 추가 → 단일 라이브러리 bug 위험 ↓
- Alt-2 (`rfc8785` 단독): cross-check 비용 0. corpus 24개 reference output 이 *유일* 검증 layer. ADR-012 §11.3 (cryptography 검토자 한계) 답습 시 단일 implementation 의 *완전* 검증 부담 ↑

**트레이드오프 매트릭스**:

| 차원 | Alt-1 (병렬 cross-check) | Alt-2 (`rfc8785` 단독) |
|----|-----|-----|
| Implementation bug detection layer | 2 (양 lib 동등성 + corpus reference) | 1 (corpus reference only) |
| Runtime cost | 2× canonicalize / entry | 1× canonicalize / entry |
| CI cost | corpus 24 × 2 lib + 동등성 24 = 72 검증 | corpus 24 × 1 lib = 24 검증 |
| 의존성 추가 | 2 PyPI lib (rfc8785 + jcs) | 1 PyPI lib (rfc8785) |
| 단일 lib bug → forgery risk | LOW (cross-check detection) | MEDIUM (corpus reference 외 detection 부재) |
| Provider Liquidity 보존 | HIGH (양 lib provider-neutral) | HIGH (1 lib provider-neutral) |
| Hermes 의존 0 | ✅ (양 lib Requires=없음) | ✅ (rfc8785 Requires=없음) |

**Agent C 평가**: Alt-1 (사용자 명시 갱신 결정) = *cryptography 검토자 한계 답습 시 정당*. 단, runtime cost 2× 부담 + CI 시간 ≥3× 증가는 **§3 단순화 권고 안 #1 (cross-check = corpus 검증 시점 한정, runtime 1×)** 영역 합리화 필요.

### 2.2 영역 2 — 대안 라이브러리 enumerate (Python 외 후보)

**사실 인용**:
- ADR-012 §2.5 명시 후보:
  - Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
  - Node: `canonicalize` npm
  - Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`
- PoC 사양 §B.1: `pyjcs` PyPI 미존재 (`No matching distribution found for pyjcs`) — RA-9 §B.3 결과
- PoC 사양 §B.1: `jcs` 0.2.1 (titusz) PyPI 발굴 — Apache-2.0, Requires=없음, 11/11 sanity PASS

**단순화 평가**:
- 본 PoC 는 **Python 환경** 한정 (CI workflow `.github/workflows/g4-hash-chain.yml` Python 3.11 + jq install — PoC 사양 §6 step setup)
- Node `canonicalize` 또는 Go `cyberphone/json-canonicalization` 채택 시 → CI Node/Go runtime 추가 + cross-language 검증 layer 추가 → PoC 범위 격증
- Python 외 후보는 본 PoC *범위 외* 평가

**트레이드오프 매트릭스**:

| 후보 | 환경 | 본 PoC 적용 |
|----|----|----|
| `rfc8785` (Python, Trail of Bits) | Python | ✅ Primary 1 |
| `jcs` (Python, titusz) | Python | ✅ Primary 2 (RA-9 §B.3 발견) |
| ~~`pyjcs`~~ | (PyPI 미존재) | ❌ 비채택 (RA-9 §B.1) |
| `canonicaljson` (Python, Matrix.org) 2.0.0 | Python | ⚠️ RFC 8785 동등성 미확정 (§2.5 영역 5) |
| `canonicalize` (Node) | Node | ❌ 본 PoC 범위 외 (Python only) |
| `cyberphone/json-canonicalization` (Go) | Go | ❌ 본 PoC 범위 외 |
| `gowebpki/jcs` (Go) | Go | ❌ 본 PoC 범위 외 |

**Agent C 평가**: ADR-012 §2.5 명시 후보 중 본 PoC (Python) 적용 가능 = `rfc8785` + `jcs` 양호 + `canonicaljson` (Matrix.org) 비권고. Node/Go 후보는 *cross-language 검증 layer* 향후 격상 영역 (별도 PoC, 본 범위 외).

### 2.3 영역 3 — fallback 대안 (stdlib `json.dumps` 가능성)

**사실 인용**:
- ADR-012 §2.5: "Fallback: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증"
- ADR-012 §2.5: 구현 라이브러리 후보 명시 — "Python: ... 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장"
- PoC 사양 §3.2: `jq -S -c` fallback + `event: canonical_json_fallback` ledger entry 자동 작성 의무
- PoC 사양 §11 L-1 (cryptography 한계): "본 ADR §2.5 의 fallback `jq -S -c` 가 JCS 와 *모든 케이스 동등* 보장 부재" (ADR-012 §11.3 답습)

**단순화 평가**:
- stdlib `json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)` 는 RFC 8785 의 *escape* 와 *key ordering* 일부 등가 — *number normalization* (IEEE 754) 미구현
- 자체 number normalization 구현 부담 = 1인 개발자 + cryptography 검토자 한계 영역 위험 (ADR-012 §11.3 답습)
- stdlib 단독 fallback 은 RFC 8785 *완전* 동등 보장 *부재* → corpus 24개 회귀 검증 시 *number normalization* 카테고리 case (1.0 vs 1 / 1e10 vs 10000000000 / -0 vs 0) 실패 위험

**트레이드오프 매트릭스**:

| Fallback 후보 | RFC 8785 동등성 | 외부 의존 | 운영 부담 | 본 PoC 적용 |
|----|----|----|----|----|
| `jq -S -c` (POSIX) | 부분 (escape + key order) — number normalization 부분 | jq POSIX | subprocess overhead | ✅ ADR-012 §2.5 명시 답습 |
| stdlib `json.dumps(sort_keys=True, separators=(",",":"), ensure_ascii=False)` | 부분 (escape + key order) — number normalization *미구현* | 0 (Python stdlib) | self-implementation 부담 | ⚠️ *비-fallback* — number normalization 부재 |
| 자체 RFC 8785 등가 구현 | (자체 검증 의무) | 0 | cryptography 검토자 한계 영역 위험 (ADR-012 §11.3) | ❌ 본 PoC 범위 외 (Reviewer 한계) |

**Agent C 평가**: `jq -S -c` fallback = ADR-012 §2.5 답습 정당 + POSIX 표준 + 외부 의존 최소 + 운영 부담 적정. stdlib `json.dumps` 추가 fallback = number normalization 부재로 *진정한 fallback* 아님. **본 PoC fallback = `jq -S -c` 단독 유지 권고** + L-1 한계 (jq 와 JCS *완전* 동등성 부재) 명시 보강 권고 → §5 C-C4 조건.

### 2.4 영역 4 — cross-check overhead 정당성

**사실 인용**:
- PoC 사양 §3.1: "본 PoC 는 *두 라이브러리 모두 사용* — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제. 양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2 trigger)"
- PoC 사양 §6 CI workflow: "fallback 동등성 — `rfc8785` vs `jq -S -c` 24개 동등 — 실패 시 rc=1 (Q1 합의 trigger fallback 충돌)"
- PoC 사양 §B.5: TR-C-2 (corpus 24개 동등성 실패) 미발화 (sanity 11/11 PASS) — corpus 24개 본 PoC 구현 시 재검증
- ADR-012 §3.5 운영 부담 monitoring trigger: "Fallback 사용 빈도 > 10% → JCS Primary 검토 합의"

**단순화 평가**:
- corpus 24개 단계 cross-check (CI build time 한정) = *적정 비용*. 한 번 비용 + reproducibility 검증
- runtime entry 마다 cross-check = entry 1건 마다 2× canonicalize → ledger 작성 빈도 ↑ 시 운영 부담 ↑ (ADR-012 §3.5 monitoring trigger 발화 위험)
- *Cross-check 의 진정한 가치* = 단일 lib implementation bug detection — 이는 *corpus 검증 시점* 만으로 충분 (양 lib 출력 동등성 = lib 자체 검증). runtime 마다 재검증은 *redundant* (corpus 검증 PASS 상태에서 lib 출력은 deterministic)

**트레이드오프 매트릭스**:

| 모드 | corpus cross-check (24× 2) | runtime cross-check (entry × 2) | 단일 lib bug detection | 운영 부담 | Agent C 권고 |
|----|----|----|----|----|----|
| Mode 1 (corpus + runtime cross-check) | ✅ | ✅ | HIGH (corpus + runtime 다중 layer) | HIGH (entry 마다 2×) | 비권고 (overhead 격증) |
| Mode 2 (corpus cross-check only, runtime 1×) | ✅ | ❌ (Primary 1개 사용) | MEDIUM (corpus only — lib 자체 검증) | LOW (entry 마다 1×) | **권고 (단순화 권고 안 #1)** |
| Mode 3 (runtime cross-check only, corpus 단순) | ❌ | ✅ | LOW (runtime 마다 — corpus 부재 시 reference 부재) | HIGH | 비권고 |
| Mode 4 (cross-check 0, 단일 lib + corpus) | ❌ | ❌ (Alt-2 = rfc8785 단독) | LOW (corpus reference only) | LOW | Alt-2 (단순화 권고 안 #3) |

**Agent C 평가**: 본 PoC 사양 §3.1 의 "양 라이브러리 의견 불일치 시 BLOCK" 는 *corpus 24개* 시점 한정 합리. runtime entry 마다 cross-check 의무화 = redundant + 운영 부담 격증. **§3 단순화 권고 안 #1 (Mode 2 — corpus cross-check only)** 권고.

### 2.5 영역 5 — `canonicaljson` (Matrix.org) 비채택 사유 재확인

**사실 인용**:
- PoC 사양 §B.3: "`canonicaljson` 2.0.0 (Matrix.org) PyPI 존재 — Matrix 자체 정의 — RFC 8785 동등성 미확정 — Q1 후보 옵션 C: 비권고 (별도 동등성 corpus 검증 필요)"
- ADR-012 §2.5 후보 enumerate 시 `canonicaljson` (Matrix.org) 명시 *부재* — `pyjcs` / `rfc8785` / stdlib 만 명시

**단순화 평가**:
- Matrix.org `canonicaljson` 은 Matrix protocol *자체* canonical JSON 정의 — RFC 8785 동등성 *미확정*
- 별도 동등성 corpus 검증 부담 = 본 PoC 범위 외 (cryptography 검토자 한계 영역)
- 채택 시 *RFC 8785 동등성 검증 PoC 추가* 의무 = scope 격증

**Agent C 평가**: `canonicaljson` (Matrix.org) 비채택 사유 = (1) RFC 8785 동등성 미확정 + (2) Matrix protocol 자체 정의 (vendor-specific 위험) + (3) ADR-012 §2.5 후보 enumerate 부재. 본 PoC 사양 §3.2 또는 부록 A 에 *비채택 사유 명시 보강* 권고 → §5 C-C3 조건.

### 2.6 영역 6 — PoC 범위 단순화 기회 (6 영역 중 분리 가능)

**사실 인용**:
- PoC 사양 §1.1: 6 영역 = (1) Canonical JSON 모듈 / (2) JSONL hash chain 검증기 / (3) Round-trip 검증기 / (4) Test corpus / (5) PASS/FAIL fixture / (6) CI workflow
- PoC 사양 §9: Q3 결정 답습 = "PoC 6 영역" Reviewer-only 단축
- roadmap §4.1: G4 Order 3 tie 3건 = JSONL hash chain / RFC 8785 JCS / Round-trip — 본 PoC 통합 답습

**단순화 평가**:
- 6 영역 중 *분리 가능* 후보:
  - **Round-trip 검증기 (영역 3)** = ADR-012 §2.9 Tier-based + 3 ledger entry 형식 + L-2 한계 (JSONL → JSONL 동일 형식 한정, cross-format 미적용 — Group H 영역) → 본 PoC *분리 가능* 후보
  - **PASS/FAIL fixture (영역 5)** = 본 PoC 검증 evidence — 분리 시 검증 layer 부재 → 분리 *불가*
- Q3 사용자 결정 = 6 영역 통합 답습 — 본 Agent C 는 사용자 결정 *반박* 가능하나 *부정* 금지 (사용자 명시 갱신 결정 권위 보존)

**트레이드오프 매트릭스**:

| 분리 후보 | 통합 시 (6 영역) | 분리 시 (5 영역 + round-trip 후속) |
|----|----|----|
| 본 PoC 산출 | 6 module + 24 corpus + 6 fixture + CI workflow | 5 module + 24 corpus + 4 fixture + CI workflow |
| 합의 비용 | 1 합의 (Q3 단축) | 2 합의 (5 영역 + round-trip 별도) |
| Order 3 tie 3건 통합성 | ✅ 답습 | ⚠️ round-trip 분리 시 tie 통합 약화 |
| Group C 정체성 | "Order 3 tie 3건 통합" 그대로 | "Order 3 tie 2건 통합" 변경 |
| 1인 개발자 비용 | 본 PoC 1회 7 영역 작업 | 본 PoC + 후속 PoC (round-trip 별도) |

**Agent C 평가**: 사용자 Q3 결정 = 6 영역 통합 답습 정당 — Group C 정체성 (Order 3 tie 3건) 보존 + 합의 비용 1회. 단, **단순화 권고 안 #2 (round-trip T3 lossy 분리)** 영역에서 일부 분리 후보 평가 (T3 lossy = ADR-012 §2.9 사용자 명시 review 의무 영역, 자동화 한계).

### 2.7 영역 7 — Test corpus 24 vs 20 단순화 가능성

**사실 인용**:
- PoC 사양 §1.1: "Test corpus (24개) — 8 카테고리 × 3 = 24 reference output. ADR-012 §2.5 ≥20개 답습"
- PoC 사양 §3.4: 8 카테고리 = unicode / number / key_ordering / escape / nested / array / hash_stability / lossy
- ADR-012 §2.5: "test corpus ≥ 20개"

**단순화 평가**:
- 24개 (8 × 3) vs 20개 (8 × 2.5) — 단순화 시 8 카테고리 × 2 = 16개 (≥20 미충족) 또는 8 카테고리 × 2 + 4 추가 = 20개 (균형 부족)
- ADR-012 §2.5 ≥20개 답습 → 24개 = 20개 *충분 이상* + 1인 개발자 비용 4 case 추가 한정
- lossy round-trip 카테고리 (`tests/canonical/lossy/`) = float precision loss / unicode normalization / number→string 3 case → 2 case 축소 시 lossy 영역 cover 부족

**트레이드오프 매트릭스**:

| corpus 수 | 카테고리 cover | ADR-012 §2.5 답습 | 1인 개발자 비용 | 회귀 detection 강도 |
|----|----|----|----|----|
| 24개 (8×3) | 8 카테고리 균형 (3 each) | ✅ ≥20개 충분 | MEDIUM (24 reference output 작성) | HIGH |
| 20개 (8×2.5) | 8 카테고리 비균형 (4 카테고리 3 + 4 카테고리 2) | ✅ ≥20개 충족 | LOW-MEDIUM | MEDIUM |
| 16개 (8×2) | 8 카테고리 (2 each) | ❌ ≥20개 미충족 | LOW | LOW (lossy / hash_stability case 부족) |

**Agent C 평가**: 24개 = 적정 균형점 — ADR-012 §2.5 답습 + 8 카테고리 균등 + 1인 개발자 비용 적정. **24개 유지 권고**. Q2 사용자 결정 답습 정당.

### 2.8 영역 8 — Round-trip T2 strict + T3 lossy 양 모드 강제 vs T2 단독 단순화

**사실 인용**:
- PoC 사양 §4.3: "T2 strict (hash 일치 100%) → `roundtrip_pass` ledger entry 작성 / 의미 보존 (lossy 영역 명시) → `roundtrip_lossy` ledger entry 작성 (lost_fields enumeration 자동) / parse 실패 / 의미 보존 실패 → `roundtrip_fail` ledger entry 작성"
- PoC 사양 §1.1: PASS fixture × 2 = `pass/{minimal_chain, roundtrip_t2_strict}.jsonl` — *T2 strict 만* fixture
- PoC 사양 §1.1: FAIL fixture × 4 — `fail/roundtrip_lossy_no_entry.jsonl` (lossy 영역) 1건
- ADR-012 §2.9: T3 (Cross-vendor migration) = "외부 형식 변환 + 재import" — 본 PoC L-2 한계 (cross-format 미적용, Group H 영역)

**단순화 평가**:
- 본 PoC = JSONL → JSONL 동일 형식 한정 (L-2) → T3 cross-vendor migration *본 PoC 외*
- 본 PoC T3 lossy 검증 영역 = JSONL → JSONL 동일 형식 *내* lossy 발생 (예: float precision loss within JSONL re-parse)
- T2 단독 검증 = JSONL → JSONL hash 일치 100% 한정 → L-2 한계 답습 시 *충분*
- T3 lossy 영역 = `roundtrip_lossy` ledger entry 자동 작성 의무 + lost_fields enumeration 자동 — *자동 가능 영역* (의미 보존 review = 사용자 명시, ADR-012 §2.9)

**트레이드오프 매트릭스**:

| 모드 | 본 PoC 검증 layer | L-2 한계 답습 | 1인 개발자 비용 | Agent C 권고 |
|----|----|----|----|----|
| T2 + T3 양 모드 (사용자 Q3 결정) | T2 hash 일치 + T3 lossy ledger entry | ✅ JSONL → JSONL 한정 (cross-format L-2 답습) | MEDIUM | 사용자 명시 답습 |
| T2 단독 (단순화 후보) | T2 hash 일치 only | ✅ L-2 한정 + T3 분리 | LOW | **단순화 권고 안 #2** (T3 lossy 별도 후속 PoC) |

**Agent C 평가**: T2 + T3 양 모드 = ADR-012 §2.9 답습 정당. 단, T3 lossy = 사용자 명시 review 영역 (자동화 한계 — ADR-012 §2.9) → 본 PoC 자동화 layer = *3 ledger entry 형식 자동 작성* 한정. **단순화 권고 안 #2 (T3 lossy 영역 분리 후속 PoC)** 평가 — Q3 사용자 결정 답습 시 정당.

### 2.9 영역 9 — `event` 17 enum vs MVP 4종 한정 단순화

**사실 인용**:
- PoC 사양 §2 #7: "`event` enum 17 후보 중 1 (ADR-012 §2.2 답습 — 본 PoC MVP 4종 한정 검증: `canonical_json_fallback` / `chain_violation_detected` / `roundtrip_lossy` / `roundtrip_fail`)"
- PoC 사양 §11 L-3: "`event` 17 enum 중 MVP 4종 한정 검증 — ADR-012 §2.2 답습 — 17 enum 전체 검증은 별도 합의"
- ADR-012 §2.2: 17 enum 후보 + MVP 의무 12 enum + 후속 확장 5 enum

**단순화 평가**:
- 본 PoC MVP 4종 = (1) `canonical_json_fallback` (영역 1 fallback layer 직결) / (2) `chain_violation_detected` (영역 2 chain 검증 직결) / (3) `roundtrip_lossy` (영역 3 round-trip 직결) / (4) `roundtrip_fail` (영역 3 round-trip 직결)
- 4종 = 본 PoC 6 영역 cover 의무 최소 set
- 추가 단순화 (3종 / 2종) → fallback / chain / round-trip 중 1+ 영역 검증 layer 부재 위험

**Agent C 평가**: MVP 4종 = 본 PoC 영역 cover 최소 set + ADR-012 §2.2 답습 + L-3 한계 명시 답습. **4종 → 3종 추가 단순화 비권고** — 4종 모두 본 PoC 6 영역과 직결.

### 2.10 영역 10 — Hermes-free 보장 단순화 (표준 도구 단독 가능성)

**사실 인용**:
- ADR-008 차단조건 #2: "Evidence Ledger = Hermes 의존 0"
- ADR-012 원칙 5: "Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능"
- PoC 사양 §부록 A: "Hermes 의존 0 (ADR-008 차단조건 #2 답습) — 본 PoC 모든 도구 = POSIX 표준 + Python stdlib + provider-neutral PyPI 한정"
- PoC 사양 §B.4: 양 라이브러리 (rfc8785 + jcs) 모두 Requires=없음 + ADR-008 차단조건 #2 충족 + Provider Liquidity HIGH

**단순화 평가**:
- ADR-008 차단조건 #2 = *Hermes* 의존 0 의무 — *PyPI provider-neutral 라이브러리* 의존 0 의무 *아님*
- ADR-012 원칙 5 의 "표준 도구" = `jq` + `sha256sum` + Python stdlib *예시* — RFC 8785 JCS 의 number normalization 등은 stdlib 만으로 *완전* 등가 구현 부담 = 1인 개발자 + cryptography 검토자 한계 영역 위험 (ADR-012 §11.3 답습)
- 표준 도구 단독 (rfc8785 / jcs 미사용) → number normalization 자체 구현 의무 → 검증 layer = corpus 24개 reference output (자체 구현 자기 검증) → cryptography 검토자 한계 영역
- PyPI provider-neutral 라이브러리 (rfc8785 / jcs) 의존 추가 = Provider Liquidity 보존 + Hermes 의존 0 + cryptography 검토자 한계 회피 = 정당화 가능

**트레이드오프 매트릭스**:

| 모드 | RFC 8785 등가 구현 책임 | Hermes 의존 0 | Provider Liquidity | cryptography 검토자 한계 회피 |
|----|----|----|----|----|
| 표준 도구 단독 (`jq` + `sha256sum` + Python stdlib only) | 자체 구현 의무 (number normalization 등) | ✅ | ✅ | ❌ (자체 구현 검증 부담) |
| PyPI 라이브러리 의존 (`rfc8785` 또는 `rfc8785` + `jcs`) | 라이브러리 위임 + corpus 24 회귀 검증 | ✅ (Requires=없음) | ✅ (provider-neutral) | ✅ (라이브러리 maintainer + Trail of Bits / titusz 책임) |

**Agent C 평가**: 표준 도구 단독 = ADR-008 차단조건 #2 의 *해석 단순화* 일 뿐 *완전 단순화 아님* — RFC 8785 자체 구현 부담 = 1인 개발자 + cryptography 검토자 한계 영역. **PyPI provider-neutral 라이브러리 의존 추가는 정당** + ADR-008 차단조건 #2 (Hermes 의존 0) 충족 + Provider Liquidity HIGH. **표준 도구 단독 비권고**.

---

## 3. 단순화 대안 권고 안 (3건 enumerate)

### 3.1 권고 안 #1 — Cross-check 시점 한정 (Mode 2)

**정의**: corpus 24개 시점 cross-check (양 lib 동등성 검증) + runtime entry canonicalize 1× (Primary lib 1개 사용 — `rfc8785` 권고).

**트레이드오프**:
- (+) 단일 lib bug detection layer 보존 (corpus 시점)
- (+) runtime overhead 50% 감소 (entry 마다 1×)
- (+) ADR-012 §3.5 monitoring trigger (Fallback 사용 빈도 > 10%) 발화 위험 ↓
- (-) runtime 마다 cross-check 부재 → corpus 검증 PASS 후 lib 자체 변경 (silent update) detection 부재 → CI matrix install + version lock 보강 의무

**채택 사유**: cross-check 의 *진정한 가치* = lib implementation bug detection. 이는 corpus 24개 reference output 시점 검증으로 충분 (양 lib 출력 deterministic). runtime 마다 재검증은 redundant + 운영 부담 격증.

**비채택 사유** (사용자 명시 갱신 결정 = Alt-1 그대로 유지 시): 양 lib 의 *모든 entry 마다 동등성 검증* 이 cryptography 검토자 한계 영역 (ADR-012 §11.3) 보강 layer 로서 의미 → 본 Agent C 권고는 *cryptography specialist 검토 후 결정* 영역.

### 3.2 권고 안 #2 — Round-trip T3 lossy 영역 분리 (후속 PoC)

**정의**: 본 PoC = T2 strict 단독 검증 + T3 lossy = 별도 후속 PoC (`g4-roundtrip-lossy-poc-spec.md` 신규).

**트레이드오프**:
- (+) 본 PoC 6 영역 → 5 영역 단순화
- (+) T3 lossy = ADR-012 §2.9 사용자 명시 review 영역 (자동화 한계) → 분리 시 자동 영역 (T2) 한정 본 PoC = 검증 layer 명료
- (+) 1인 개발자 비용 본 PoC 한정 ↓
- (-) Group C 정체성 (Order 3 tie 3건 통합) 변경 — Q3 사용자 결정 답습 위반
- (-) 합의 비용 2× (본 PoC 단축 + 후속 T3 lossy 별도)

**채택 사유**: T2 strict (자동 hash 일치) ↔ T3 lossy (사용자 명시 review) 의 *자동화 layer 분리* — Group C 의 자동 검증 layer 본 PoC 한정 합리.

**비채택 사유** (사용자 Q3 결정 답습 시): 6 영역 통합 = ADR-012 §2.9 + roadmap §4.1 Order 3 tie 3건 통합 답습. Group C 정체성 보존 + 합의 비용 1회. T3 lossy 자동화 한계 (자동 영역 = 3 ledger entry 작성 + lost_fields enumeration) 는 본 PoC 자동 가능 영역 → 분리 정당성 약함.

### 3.3 권고 안 #3 — `rfc8785` 단독 채택 (Alt-2 — backup plan)

**정의**: cross-check 0 + `rfc8785` (Trail of Bits) 단독 채택 + corpus 24개 reference output 유일 검증 layer + `jq -S -c` fallback 유지.

**트레이드오프**:
- (+) 의존성 1 PyPI lib (rfc8785 only) — runtime overhead 50% 감소
- (+) Trail of Bits maintainer 책임 + RFC 8785 명시 구현 + Apache-2.0 + NaN/Inf reject (RA-9 §B.1 답습)
- (+) ADR-008 차단조건 #2 + Provider Liquidity HIGH 충족
- (-) cryptography 검토자 한계 영역 — corpus 24 reference output 이 *유일* 검증 layer (단일 lib bug 위험)
- (-) 사용자 명시 갱신 결정 (Alt-1 병렬 cross-check) *부정* 위험

**채택 사유**: cross-check overhead 0 + 단순성 최대 + Trail of Bits maintainer 책임 위임 + 의존성 최소화 (1 lib).

**비채택 사유** (사용자 명시 갱신 결정 = Alt-1 답습 시): 사용자 명시 갱신 결정 권위 보존 (사용자 명시 결정 *부정* 금지 — 본 Agent C 제약 답습) + cryptography 검토자 한계 영역 보강 layer (양 lib cross-check) 추가 가치.

**보조 활용**: Alt-2 = TR-C-2 (corpus 24개 동등성 실패) 발화 시 *backup plan* 으로 활용 — §5 C-C2 조건 권고.

---

## 4. Risk Assessment

### 4.1 Over-engineering 위험

| 위험 | 사실 인용 | 강도 | 회피 매커니즘 |
|----|----|----|----|
| Cross-check overhead 격증 (entry 마다 2×) | PoC §3.1 양 lib 모두 사용 | MEDIUM | §3 권고 안 #1 (corpus 시점 한정) |
| 6 영역 통합 의무 (Q3) — round-trip T3 lossy 자동화 한계 영역 포함 | PoC §1.1 + ADR-012 §2.9 사용자 명시 review | LOW (Q3 사용자 결정 답습) | §3 권고 안 #2 (T3 lossy 분리) — 사용자 결정 시 |
| corpus 24개 (Q2) — ≥20개 답습 충분 이상 4 case 추가 | PoC §3.4 + ADR-012 §2.5 | LOW | 24개 유지 (§2.7 평가) |
| `event` 17 enum 중 MVP 4종 → 추가 enum 발화 시 합의 trigger | PoC §11 L-3 + TR-C-3 | LOW | TR-C-3 (`event` enum 추가 발화 시 별도 합의) |

### 4.2 Lock-in 위험

| 위험 | 사실 인용 | 강도 | 회피 매커니즘 |
|----|----|----|----|
| `rfc8785` lib lock-in (Trail of Bits) | PoC §3.1 + 부록 A | LOW (Apache-2.0 + Requires=없음) | Provider-neutral PyPI + 양 lib cross-check (Alt-1) 또는 corpus 24 reference output (Alt-2) |
| `jcs` lib lock-in (titusz) | PoC §B.3 | LOW (Apache-2.0 + Requires=없음 + sanity 11/11) | 동일 |
| `jq` POSIX 의존 (fallback) | PoC §3.2 + ADR-012 §2.5 | LOW (POSIX 표준 + 외부 의존 최소) | POSIX 표준 답습 — replace 가능 |
| Python 3.11 환경 lock-in (CI workflow) | PoC §6 setup | LOW (Python 3.11 = LTS) | venv 격리 (PoC §B.6) |

### 4.3 복잡도 inflation

| 영역 | 단순화 가능성 | 본 Agent C 평가 |
|----|----|----|
| Cross-check (corpus + runtime 양쪽) | corpus 시점 한정 가능 | §3 권고 안 #1 |
| 6 영역 통합 → round-trip T3 lossy 분리 | T3 lossy 후속 PoC 분리 가능 | §3 권고 안 #2 (사용자 결정 시) |
| 24 corpus | 적정 균형 (단순화 비권고) | §2.7 |
| 4 MVP `event` enum | 4종 = 영역 cover 최소 set | §2.9 (단순화 비권고) |
| 표준 도구 단독 (PyPI 의존 0) | RFC 8785 자체 구현 부담 = cryptography 검토자 한계 영역 위험 | §2.10 (단순화 비권고) |

**총 복잡도 inflation 평가**: MEDIUM. cross-check overhead 단순화 (권고 안 #1) 가 가장 큰 단순화 기회 + T3 lossy 분리 (권고 안 #2) 가 부수적 기회. 24 corpus + 4 MVP enum + PyPI 의존은 단순화 *비권고* 영역 (각 영역 정당화 사유 존재).

---

## 5. 추가 권고 조건 (C-C1 ~ C-C5)

### 5.1 본 PoC 진입 *전* 의무 조건

| # | 조건 | 사유 | 책임 |
|----|----|----|----|
| **C-C1** | Cross-check overhead 의 *정량 measurement* 본 PoC 구현 시 의무 (corpus 24 + runtime entry × 100 회 benchmark) | TR-C-2 (corpus 24개 동등성 실패) 발화 시 Alt-2 (rfc8785 단독) 격상 trigger 결정 근거 | 본 PoC 구현자 (Group C) |
| **C-C2** | Alt-2 (`rfc8785` 단독) backup plan 본 PoC 사양 §B.5 escalation 매트릭스 cross-reference 명시 보강 | TR-C-1 (양 후보 install 불가) / TR-C-2 (corpus 동등성 실패) 발화 시 즉시 격상 가능 layer | PoC 사양 §B 갱신 |
| **C-C3** | `canonicaljson` (Matrix.org) 비채택 사유 본 PoC 사양 §3.2 또는 부록 A 명시 보강 | RA-9 §B.3 발견 답습 + ADR-012 §2.5 후보 부재 사유 명시 | PoC 사양 §3 갱신 |
| **C-C5** | cryptography 영역 검토자 한계 명시 — 외부 LLM 1+ blind 의뢰 영역 권고 격상 (ADR-012 §11.3 + C-14 답습) | 본 Q1 = cryptography 영역 직접 결정 → cross-vendor (GPT-5.x or Gemini) 의견 *권고* (사용자 명시 결정 영역) | Reviewer 종합 + 사용자 결정 영역 |

### 5.2 본 PoC 구현 시 의무 조건

| # | 조건 | 사유 | 책임 |
|----|----|----|----|
| **C-C4** | `jq` fallback 의 RFC 8785 *완전 동등성 부재* 한계 명시 보강 (ADR-012 §11.3 답습) | PoC 사양 §3.2 의 fallback 운영 시 *비-RFC 8785 동등 case* 발생 가능 → ledger entry `event: canonical_json_fallback` 자동 작성 의무 (현 사양 답습) + Reviewer 알림 + 사용자 review 권장 (ADR-012 §2.5 답습) | PoC 구현 + ledger writer |

**C-C1 ~ C-C5 모두 본 PoC 진행 적격 *조건* — BLOCK 사유 *아님***. Reviewer 종합 + 사용자 결정 영역.

---

## 6. 반박 영역 (본 Agent C 권고 안의 *비채택* 사유 자기 명시)

본 §6 = PR-2 Agent C 답습 형식 — Agent C 자기 권고가 *비채택* 될 수 있는 사유 자기 명시 (편향 회피).

### 6.1 권고 안 #1 (Cross-check 시점 한정) 비채택 사유

- 사용자 명시 갱신 결정 (Alt-1) = "양 라이브러리 모두 사용 — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제. 양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2 trigger)" — 본 결정의 *runtime cross-check* 부분이 *명시적*인지 *암묵적*인지 *해석 영역*. 사용자 명시 결정이 *runtime cross-check 의무* 포함이라면 본 권고는 *사용자 결정 부정* 위험.
- cryptography 검토자 한계 영역 (ADR-012 §11.3) 보강 layer 로서 양 lib cross-check 의 *runtime* 가치 = lib 의 silent update / version drift 시 detection layer → corpus 시점 한정으로는 detection 부재.
- ADR-012 §3.5 monitoring trigger 발화 위험 (Fallback 사용 빈도 > 10%) 은 *fallback* 영역 — *Primary cross-check* 영역 monitoring trigger 부재 → 운영 부담 진정한 격증 여부 미확정.

### 6.2 권고 안 #2 (T3 lossy 분리) 비채택 사유

- Q3 사용자 결정 = 6 영역 통합 답습 — 본 권고는 *사용자 명시 결정 부정* 위험 (사용자 명시 결정 권위 부정 금지 — 본 Agent C 제약 답습).
- Group C 정체성 = "Order 3 tie 3건 통합 (hash chain + JCS + round-trip)" — round-trip T3 lossy 분리 시 Group C 정체성 변경.
- T3 lossy 자동화 layer (3 ledger entry 자동 작성 + lost_fields enumeration) 는 본 PoC 가능 영역 → 분리 정당성 약함.
- 합의 비용 2× (본 PoC 단축 + 후속 T3 lossy 별도).

### 6.3 권고 안 #3 (`rfc8785` 단독 — Alt-2) 비채택 사유

- 사용자 명시 갱신 결정 = Alt-1 (병렬 cross-check) — 본 권고 (Alt-2) 는 *사용자 명시 결정 부정* 위험.
- cryptography 검토자 한계 영역 (ADR-012 §11.3) 보강 layer 부재 → corpus 24 reference output 이 *유일* 검증 layer (단일 lib bug 위험).
- 본 권고 = backup plan 한정 (TR-C-2 발화 시) — 본 채택 권고 아님 (§3.3 보조 활용 명시).

### 6.4 본 Agent C 분석 자체의 메타 한계

- 본 Agent C 분석 = *Claude Opus 4.7 (1M context) 단독* — 외부 LLM 의견 부재. *대안 탐색* 의 범위가 본 모델 시야 한정.
- 본 분석 = 사양 본문 + RA-9 evidence 기반 — 실 cross-check overhead 정량 measurement 미수행 → 권고 안 #1 의 *50% overhead 감소* 추정은 정량 evidence 부재 (C-C1 조건 답습).
- 본 분석 = *Reviewer 종합 대상* — Agent A (구현 가능성) / Agent B (품질·안전성) 의견과 교차 비교 후 Reviewer 가 합의 보고서 작성.
- 본 분석 = cryptography 영역 직접 검토 한계 (ADR-012 §11.3 답습) — RFC 8785 JCS 동등 구현 검증은 crypto specialist + cross-vendor 추가 의견 권고 영역 (C-C5 조건 답습).

---

## 7. Verdict

### 7.1 판정

```
APPROVE WITH CONDITIONS
```

### 7.2 조건 (5건)

본 Q1 (사용자 명시 갱신 결정 = Alt-1 병렬 cross-check) 진행 적격 — 다음 5 조건 권고:

1. **C-C1** (cross-check overhead 정량 measurement 본 PoC 구현 시 의무 — TR-C-2 발화 시 Alt-2 격상 trigger 결정 근거)
2. **C-C2** (Alt-2 `rfc8785` 단독 backup plan 본 PoC 사양 §B.5 escalation 매트릭스 cross-reference 명시 보강)
3. **C-C3** (`canonicaljson` Matrix.org 비채택 사유 본 PoC 사양 §3.2 또는 부록 A 명시 보강)
4. **C-C4** (`jq` fallback 의 RFC 8785 *완전 동등성 부재* 한계 명시 보강 — ADR-012 §11.3 답습)
5. **C-C5** (cryptography 영역 검토자 한계 명시 — 외부 LLM 1+ blind 의뢰 영역 권고 격상 — ADR-012 §11.3 + C-14 답습)

### 7.3 판정 사유

- 사용자 명시 갱신 결정 (Alt-1) = RA-9 §B.2 sanity 11/11 PASS + ADR-008 차단조건 #2 (Hermes 의존 0) 양 lib 충족 + Provider Liquidity HIGH → *합리적 결정*.
- 5 영구 핵심 제약 모두 답습 충분 (Provider Liquidity HIGH / Hermes ≠ root of trust 영향 0 / 메타포 회피 명시 / 자동 정책 변경 금지 답습 / 수단/목적 분리 = JCS = 수단, Evidence 무결성 = 목적).
- 단순화 권고 안 3건 enumerate (§3) 모두 *사용자 명시 결정 부정 위험* 또는 *cryptography 검토자 한계 영역* 으로 *조건부* 권고 한정 — Reviewer 종합 + 사용자 결정 영역.

### 7.4 BLOCK 사유 부재

다음 사유로 BLOCK 권고 *하지 않음*:
- 사용자 명시 갱신 결정 (Alt-1) = RA-9 evidence 기반 합리적 결정
- 양 lib 모두 ADR-008 차단조건 #2 + Provider Liquidity HIGH 충족
- corpus 24 = ADR-012 §2.5 ≥20개 답습 충분
- `event` MVP 4종 = 본 PoC 6 영역 cover 최소 set
- L-1 ~ L-5 한계 자기 명시 답습 (PoC §11)
- Cryptography 검토자 한계 = C-C5 조건 (외부 LLM 권고 격상) 으로 회피 가능

---

## 8. 본 Agent C 분석의 메타 편향 자기진단

본 Agent C 분석은 다음 5 통제 답습 (PR-2 Agent C §8 답습):

1. **사용자 명시 절차 답습**: G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 / Hermes PMO 격상 / 실 migration script 본 구현 / ADR 본문 자동 갱신 / 신규 정책 발명 / Hermes 의존 도입 모두 본 분석 *범위 외* 명시.
2. **다른 Agent (A/B) 출력 미참조**: 본 분석은 PoC 사양 + ADR-012 + G4 §4.4 + roadmap §4.1 + PR-2 Agent C 답습 형식만 참조. Agent A/B 출력 본 분석 시점 *부재* (병렬 독립 분석 패턴 답습 — CLAUDE.md §3 Phase 2).
3. **자기참조 한계 명시**: 본 분석 자체가 동일 Claude 패밀리 컨텍스트 — Reviewer 종합 + 외부 LLM 1+ *권고* 격상 (§5 C-C5) 으로 통제.
4. **APPROVE WITH CONDITIONS 판정의 *조건* 명시**: 5 조건 (C-C1 ~ C-C5) 모두 *Reviewer 종합 또는 사용자 결정* 영역.
5. **반박 영역 자기 명시 (§6)**: 권고 안 3건 모두 비채택 가능 사유 자기 명시 + 본 Agent C 분석 자체의 메타 한계 4건 명시.

본 5 통제는 PR-2 Agent C 보고서 + Group A/B Agent C 보고서 답습 — Group A/B/C 동일 패턴 유지.

### 8.1 본 분석의 한계 (재명시)

- 본 Agent C 분석 = *Claude Opus 4.7 (1M context) 단독* — 외부 LLM 의견 없음. *대안 탐색* 의 범위가 본 모델의 시야 한정.
- 본 분석 = *PoC 사양 본문 + RA-9 evidence 기반* — 실 cross-check overhead 정량 measurement 미수행 → §3 권고 안 #1 의 정량 effect (50% overhead 감소) 추정은 evidence 부재 (C-C1 조건 답습).
- 본 분석 = *Reviewer 종합 대상* — Agent A (구현 가능성) / Agent B (품질·안전성) 의견과 교차 비교 후 Reviewer 가 합의 보고서 작성.
- 본 분석 = *cryptography 영역 직접 검토 한계* (ADR-012 §11.3 답습) — RFC 8785 JCS 동등 구현 검증은 crypto specialist + cross-vendor (GPT-5.x or Gemini) 추가 의견 권고 영역 (C-C5).
- 본 분석 = `pyjcs` PyPI 미존재 발견 (RA-9 §B.3) 시점 후 작성 — 사용자 명시 갱신 결정 *권위 보존* (반박 가능, 부정 금지 — 본 Agent C 제약 답습).

### 8.2 본 분석이 *PASS 판정 트리거하지 않는 것*

- ❌ Q1 합의 보고서 자동 작성 (본 분석 = Agent C 단독 입력)
- ❌ G4 PoC 진행 자동 결정 (Reviewer 종합 + 사용자 결정 영역)
- ❌ Alt-1 / Alt-2 자동 결정 (사용자 명시 결정 영역)
- ❌ Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신
- ❌ Reviewer 종합 *대체*
- ❌ 다른 Agent (A, B) 출력 참조 (본 분석 시점)
- ❌ 외부 LLM 1+ 의견 자동 호출 (사용자 명시 결정 영역)
- ❌ TR-C-1 ~ TR-C-5 자동 발화 결정 (PoC 구현 시점 영역)

본 Agent C 판정 (APPROVE WITH CONDITIONS) 은 *오직* "사용자 명시 갱신 결정 (Alt-1) 진행 적격 + 5 조건 권고" 의미. 다른 Agent / Reviewer / 사용자 결정 *우선*.

---

**작성일**: 2026-05-10
**Agent**: C (대안/단순화 탐색)
**판정**: APPROVE WITH CONDITIONS
**조건 수**: 5건 (C-C1 ~ C-C5)
**핵심 단순화 권고 안 (3건 enumerate)**:
1. Cross-check 시점 한정 (corpus 24 시점만, runtime 1×) — Mode 2
2. Round-trip T3 lossy 분리 (후속 PoC) — Q3 사용자 결정 답습 시 정당성 약화
3. `rfc8785` 단독 (Alt-2) — backup plan 한정 (TR-C-2 발화 시)
**Reviewer 종합 대상**: Agent A (구현 가능성) + Agent B (품질·안전성) + 본 Agent C
**금지 사항 답습 (변동 없음)**:
- ❌ G4 / G2 / G3 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 migration script 본 구현
- ❌ ADR 본문 자동 갱신
- ❌ 신규 정책 발명
- ❌ Hermes 의존 도입
- ❌ 다른 Agent (A, B) 출력 참조 (본 분석 시점)
- ❌ Reviewer 합의 예측
- ❌ 사용자 명시 갱신 결정 권위 부정 (반박 가능, 부정 금지)
