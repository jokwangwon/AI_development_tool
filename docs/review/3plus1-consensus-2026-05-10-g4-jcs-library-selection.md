# 풀 3+1 합의 보고서 — G4 Q1: Canonical JSON 라이브러리 선정 (`rfc8785` + `jcs` 병렬 cross-check)

**합의 형태**: 풀 3+1 (Q4 결정 답습 — Q1 = 풀 3+1, Q2/Q3 = Reviewer-only 단축, 본 PoC = Reviewer-only 단축 — 사양 §9)
**합의 일자**: 2026-05-10
**검토 대상**: G4 JSONL Hash Chain + RFC 8785 JCS PoC 의 **Canonical JSON 라이브러리 선정 (Q1)** — 사용자 명시 결정 갱신 결과 `rfc8785` 0.1.4 (Trail of Bits) + `jcs` 0.2.1 (titusz) **병렬 cross-check** 채택
**사용자 명시 결정 갱신 권위 trace**: SESSION_2026-05-10 (RA-9 §B.3 발견 후 — `pyjcs` PyPI 미존재 → `jcs` (titusz) 대안 흡수) → PoC 사양 §3.1 + 부록 A + 부록 B.3 답습
**판정**: ✅ **APPROVE WITH CONDITIONS** — Q1 본 PoC 진입 적격 (3/3 Agent 일치)
**금지 사항 답습 (영구)**: ❌ G4 / G2 / G3 전체 Implementation/Runtime PASS 선언 / ❌ Hermes PMO 격상 선언 / ❌ ADR 본문 자동 갱신 / ❌ 신규 정책 발명 / ❌ 실 migration script 본 구현 / ❌ Q2/Q3 본 합의 흡수 (별도 단축 합의 영역)

---

## 0. 5분 요약

### 0.1 핵심 판정

```
APPROVE WITH CONDITIONS — G4 Q1 (rfc8785 + jcs 병렬 cross-check) 본 PoC 진입 적격
```

3/3 Agent 모두 APPROVE WITH CONDITIONS. BLOCK / 단순 APPROVE / PARTIAL 0건.

### 0.2 Agent 별 판정 + 핵심 위험

| Agent | 판정 | 조건 수 | HIGH 위험 / Gap | 분량 |
|-------|------|--------|--------------|------|
| Agent A (구현/운영) | APPROVE WITH CONDITIONS | 8 (C-A1 ~ C-A8) | R-A1 corpus 24개 동등성 재검증 HIGH + R-A2 §6 setup `jcs` install 누락 HIGH | 378 줄 |
| Agent B (보안/거버넌스) | APPROVE WITH CONDITIONS | 17 (C-B1 ~ C-B17) + Gap-N HIGH 4건 + MEDIUM-HIGH 1건 | Gap-N #1 `external_llm_received` 미적용 + Gap-N #4 `jcs` 개인 maintainer supply chain HIGH | 684 줄 |
| Agent C (대안/단순화) | APPROVE WITH CONDITIONS | 5 (C-C1 ~ C-C5) | 핵심 단순화 안 = Mode 2 cross-check 시점 한정 (corpus 시점만, runtime 1×) — 50% overhead 감소 | 507 줄 |

### 0.3 Reviewer 종합 verdict

- **통합 조건 수**: **17건** (HIGH 7건 / MEDIUM 7건 / LOW 3건) — 중복 제거 후 (§5)
- **Gap-N HIGH 흡수**: 4건 본 PoC 구현 시 §11 한계 자기 명시 흡수 + 별도 합의 영역 명시 의무 (§9)
- **5 영구 핵심 제약 보호 강도**: **5/5 HIGH** (§7)
- **Hermes 변조 차단 매트릭스 cover (ADR-012 §2.12 4 항목)**: #2 HIGH cover + #1/#3 부분 cover + #4 0 cover (Gap-N #1) (§8)

### 0.4 갈등 영역 종결 — Reviewer 판단

핵심 갈등 = **cross-check overhead vs 보안 layer 강도** (Agent C Mode 2 권고 vs Agent A/B 사용자 명시 답습):

- Agent C 권고: corpus 시점 cross-check + runtime 1× (`rfc8785` Primary 단독)
- Agent A 권고: corpus 회귀 한정 cross-check + runtime entry Primary 단독 (사실상 Agent C Mode 2 와 일치)
- Agent B 입장: cross-check 강제 = 단일 supply chain 침해 + bug-class 회피 layer 보존 의무 (HIGH)

**Reviewer 결정**: 사용자 명시 갱신 결정 (Alt-1 = 병렬 cross-check) 의 *명시 영역* = corpus 24개 (§3.1 직접 명시) — *runtime cross-check 의무* 는 *해석 영역*. 본 합의는 **corpus 24개 시점 cross-check 의무 (강제, BLOCK trigger TR-C-2 발화 정합) + runtime entry cross-check = 본 PoC 구현 시 정량 measurement 후 결정 (C-A3 + C-C1 결합)** 으로 채택. 사용자 명시 결정 권위 부정 0건.

### 0.5 다음 진입 단계

본 합의 머지 후 → **Q2/Q3 Reviewer-only 단축 합의** (corpus 24개 + PoC 6 영역) → **Group C PoC 구현** → **Reviewer-only 단축 합의 (구현 후)** (Q4 결정 답습).

---

## 1. 합의 의제

### 1.1 Q1 본 의제 정의

**G4 JSONL Hash Chain + RFC 8785 JCS PoC** 의 **Canonical JSON 라이브러리 선정** — `tools/canonical_json.py` 의 Primary 라이브러리.

원본 사용자 명시 결정 (`docs/architecture/implementation-runtime-roadmap.md` §4.1 답습 시점) = "Q1: `rfc8785` + `pyjcs` 병렬 검증". RA-9 §B.3 발견 후 **사용자 명시 결정 갱신** = `pyjcs` PyPI 미존재 → `jcs` (titusz) 대안 흡수.

### 1.2 갱신 후 채택 결정 (사양 §3.1 + 부록 A 답습)

- **Primary 1**: `rfc8785` 0.1.4 (Trail of Bits, Apache-2.0)
- **Primary 2**: `jcs` 0.2.1 (titusz, Apache-2.0)
- **Cross-check**: corpus 24개 출력 byte 동등성 + sha256 동등성 100% 강제 (의견 불일치 시 BLOCK + escalation TR-C-2)
- **Fallback**: `jq -S -c` (POSIX 표준) + `event: canonical_json_fallback` ledger entry 자동 작성 (ADR-012 §2.5 답습)

### 1.3 RA-9 §B.3 발견 흡수 권위 trace

| 단계 | 내용 | 답습 |
|------|------|------|
| 1. Phase 0 사용자 명시 결정 (원본) | `rfc8785` + `pyjcs` 병렬 | roadmap §4.1 |
| 2. RA-9 §B.1 검증 결과 | `pyjcs` PyPI 미존재 (`No matching distribution found for pyjcs`) | PoC 사양 §B.1 |
| 3. RA-9 §B.3 대안 발굴 | `jcs` 0.2.1 (titusz) PyPI 발굴 + 11/11 sanity vector 동등성 PASS | PoC 사양 §B.3 |
| 4. 사용자 명시 결정 갱신 (TR-C-1 부분 발화 후 흡수) | `rfc8785` + `jcs` 병렬 cross-check 채택 | PoC 사양 §3.1 + 부록 A |
| 5. 본 Q1 합의 (본 보고서) | 갱신 결정 적격성 검증 + 8 + 17 + 5 = 30 조건 → 통합 17 조건 (§5) | 본 보고서 |

---

## 2. Phase 1 (분배) + Phase 2 (3 Agent 독립 분석)

### 2.1 Phase 1 — 분배

메인 컨텍스트 (Reviewer) 가 본 Q1 의제를 다음 3 관점으로 분배:

- **Agent A** (구현/운영) → 핵심 질문: "실제로 동작하는가?" (8 검토 영역)
- **Agent B** (보안/거버넌스) → 핵심 질문: "안전하고 견고한가?" (12 검토 영역)
- **Agent C** (대안/단순화) → 핵심 질문: "더 나은 방법이 있는가?" (10 검토 영역)

### 2.2 Phase 2 — 3 Agent 독립 분석 요약

#### 2.2.1 Agent A (구현/운영) 핵심 결론

- **판정**: APPROVE WITH CONDITIONS (8 조건, P0 2건 + P1 5건 + P2 1건)
- **핵심 사실**:
  - 양 라이브러리 모두 PyPI install OK + Apache-2.0 + Hermes 의존 0 + Requires=없음 (RA-9 §B.1)
  - sanity 11/11 동등성 PASS — 출력 byte + sha256 모두 일치 (RA-9 §B.2)
  - CI workflow 실행 시간 ≈ 1분 (Group A 2차 + Group B 답습 범위 *내*)
- **핵심 위험**:
  - **R-A1 (HIGH)**: corpus 24개 본 PoC 구현 시 양 라이브러리 동등성 *재검증 의무* — sanity 11 vector 만으로 24개 100% 동등 보장 미성립
  - **R-A2 (HIGH)**: §6 setup step `jcs` install 누락 — §1.1 cross-check 와 cross-reference drift
  - MEDIUM 4건 / LOW 4건
- **핵심 권고**: corpus 회귀 한정 cross-check + runtime entry Primary 단독 (C-A3) — Agent C Mode 2 와 사실상 일치

#### 2.2.2 Agent B (보안/거버넌스) 핵심 결론

- **판정**: APPROVE WITH CONDITIONS (17 조건 + Gap-N HIGH 4건 + MEDIUM-HIGH 1건)
- **핵심 사실**:
  - Provider Liquidity 보존 강도 HIGH (양 라이브러리 + jq fallback 모두 provider-neutral)
  - Hermes 의존 0 충족 HIGH (ADR-008 차단조건 #2 자동 충족)
  - ADR-012 §2.12 #2 (filesystem 변조) HIGH cover (hash chain Layer 1 + sha256 결정적 검출)
  - 단일 라이브러리 bug-class 회피 layer 강화 (서로 다른 maintainer + PyPI account + API surface)
- **핵심 위험 (HIGH)**:
  - **C-B3 (HIGH)**: `jcs` last release / commit frequency 검증 의무
  - **C-B4 (HIGH)**: `jcs` *primary 단독 격상 금지* 영구 명시
  - **C-B7 (HIGH)**: Primary 1 ↔ Primary 2 동등성 실패 escalation 명시 (TR-C-2 본문 보강)
  - **C-B8 (HIGH)**: corpus `number` 카테고리에 NaN/Infinity reject case 추가 의무
  - **C-B16 (HIGH)**: Q1 풀 3+1 합의 + cross-vendor LLM 1+ 의뢰 결합 권고
- **핵심 Gap-N HIGH 4건**:
  - **Gap-N #1 (HIGH)**: External LLM Response 위조 차단 layer 0 cover (`external_llm_received` #8 미적용 → ADR-012 §2.12 #4 cover 0)
  - **Gap-N #2 (HIGH)**: Evidence Forgery 검출 layer 부분 cover (`evidence_forgery_detected` #9 미적용)
  - **Gap-N #3 (HIGH)**: Policy Change Attempted 검출 layer 0 cover (`policy_change_attempted` #16 미적용)
  - **Gap-N #4 (HIGH)**: `jcs` (titusz) 개인 maintainer supply chain HIGH 잔여 위험

#### 2.2.3 Agent C (대안/단순화) 핵심 결론

- **판정**: APPROVE WITH CONDITIONS (5 조건 — C-C1 ~ C-C5)
- **핵심 사실**:
  - 사용자 명시 갱신 결정 (Alt-1 = 병렬 cross-check) = *조건부 정당* (RA-9 §B 답습)
  - `rfc8785` 단독 (Alt-2) 도 정당 (Trail of Bits + Apache-2.0 + RFC 명시 구현)
  - corpus 24개 = ADR-012 §2.5 ≥20개 답습 적정 균형 (단순화 비권고)
  - `event` MVP 4종 = 본 PoC 6 영역 cover 최소 set (단순화 비권고)
  - 표준 도구 단독 = RFC 8785 자체 구현 부담 = cryptography 검토자 한계 영역 위험 (비권고)
- **핵심 단순화 권고 안**:
  - **Mode 2 (corpus cross-check only, runtime 1×)** — Cross-check 시점 한정 (50% overhead 감소)
  - Round-trip T3 lossy 영역 분리 (사용자 Q3 결정 답습 시 정당성 약화)
  - `rfc8785` 단독 (Alt-2) — backup plan 한정 (TR-C-2 발화 시)
- **핵심 조건**:
  - **C-C1**: cross-check overhead 정량 measurement 본 PoC 구현 시 의무
  - **C-C2**: Alt-2 backup plan 본 PoC 사양 §B.5 escalation 매트릭스 cross-reference 명시
  - **C-C3**: `canonicaljson` (Matrix.org) 비채택 사유 명시
  - **C-C4**: `jq` fallback 의 RFC 8785 *완전 동등성 부재* 한계 명시 (ADR-012 §11.3 답습)
  - **C-C5**: cryptography 영역 검토자 한계 명시 — 외부 LLM 1+ blind 의뢰 영역 권고 격상

---

## 3. Phase 3 — 교차 비교 (4 분류 매트릭스)

### 3.1 ① 일치 (Consensus) — 3/3 Agent 동의

| # | 사항 | A 출처 | B 출처 | C 출처 |
|---|------|--------|--------|--------|
| K-1 | 사용자 명시 갱신 결정 (Alt-1 병렬 cross-check) **진행 적격** | §0.1 #1 + §7 | §0.1 + §8.2 #1 | §0 #1 + §7.4 |
| K-2 | 양 라이브러리 모두 **PyPI install OK + Apache-2.0 + Hermes 의존 0** (RA-9 §B 답습) | §2.1 + 2.2 | §2.1 + 2.2 + 2.4 | §2.1 (Alt-1 트레이드오프) |
| K-3 | **sanity 11/11 동등성 PASS** = 본 PoC 진입 적격 evidence | §2.1 | §2.5 | §0 #1 + §2.1 |
| K-4 | **corpus 24개 본 PoC 구현 시 동등성 재검증 의무** (sanity 11 vector 만으로 24개 보장 미성립) | R-A1 (HIGH) | C-B7 (HIGH) | C-C1 (정량 measurement) |
| K-5 | **fallback `jq -S -c` 답습 정당** (POSIX 표준 + ADR-012 §2.5 명시) | §2.3 | §2.7 | §2.3 |
| K-6 | **fallback 의 RFC 8785 *완전* 동등성 부재 한계** (ADR-012 §11.3 답습) | R-A9 | §2.7 + 영역 7 | §2.3 + C-C4 |
| K-7 | **Provider Liquidity 보존 강도 HIGH** (헌법 5조 비협상 충족) | §5 | §4 + 영역 3 | §4 + §7.3 |
| K-8 | **Hermes 의존 0 충족 HIGH** (ADR-008 차단조건 #2) | §5 | §4 + 영역 4 | §2.10 |
| K-9 | **5 영구 핵심 제약 5/5 HIGH 보호 적격** | §5 (5/5 HIGH) | §4 (5/5 HIGH) | §7.3 (5/5 답습) |
| K-10 | **`event` 17 enum 중 MVP 4종 한정 = 본 PoC 범위 적절** + 별도 합의 영역 명시 의무 | §2.7 + L-3 | 영역 11 + Gap-N 흡수 | §2.9 |
| K-11 | **prev_hash 검증 실패 → BLOCK + manual + violation entry** = T3 답습 (ADR-011 §2.4) | §2.5 | 영역 9 + §4 | (간접) |
| K-12 | **cryptography 영역 검토자 한계** (ADR-012 §11.3 답습) — 자기 작성 자기 검토 위험 | §0.2 + §7.3 한계 | §0.3 + 영역 12 + Gap-N #5 | §0.1 #2 + 메타 §6.4 + §8 |
| K-13 | **Hermes PMO 격상 / G4 / G2 / G3 전체 PASS / ADR 본문 자동 갱신 금지** 답습 | §6 | §0.2 | §0 + 8.2 |

**총 13 일치 사항** — 본 합의 채택 (Phase 4 §4.1).

### 3.2 ② 부분 일치 (Partial) — 2/3 Agent 동의

| # | 사항 | 동의 (2) | 이견 (1) |
|---|------|---------|---------|
| P-1 | **runtime entry 마다 cross-check 권고하지 않음** (corpus 회귀 한정) | A C-A3 + C 권고 안 #1 (Mode 2) | B 영역 5 (cross-check 강제 보안 layer 강화 — runtime 영역 명시 부재이나 강조) |
| P-2 | **`jcs` 개인 maintainer supply chain 위험 HIGH** | B Gap-N #4 + C §2.1 (cross-check 보강 layer 사용 사유) | A §2.1 (warning 미적용 — 운영 가능성 한정) |
| P-3 | **`canonicaljson` (Matrix.org) 비채택 사유 명시 보강** | C C-C3 + B 영역 2 (간접 — `canonicaljson` 미평가) | A 미평가 |
| P-4 | **CI workflow `jq` 특정 버전 pin 의무** | B C-B11 + A §2.8 (jq install 명시) | C 미평가 |
| P-5 | **violation_type 4종 vs FAIL fixture 4종 교집합 2건 한정 — fixture 추가 또는 cross-reference 명확화** | A R-A4 + B 영역 9 (간접 — 4 violation_type 직접 cover 2/4 한정) | C 미평가 |
| P-6 | **T3 lossy fixture 정의 또는 cross-reference 명시** | A R-A5 + C 권고 안 #2 (T3 lossy 분리) | B 미평가 |
| P-7 | **cross-vendor LLM 1+ 의뢰 권고 격상** | B C-B16 + C C-C5 | A §7.3 한계 자기 명시 (간접) |

**총 7 부분 일치** — 모두 본 합의 채택 사유 평가 후 흡수 (Phase 4 §4.2).

### 3.3 ③ 불일치 (Divergence) — 3/3 다른 의견

| # | 사항 | A | B | C |
|---|------|---|---|---|
| D-1 | **cross-check 의 시점 (corpus only vs runtime+corpus)** | corpus 회귀 한정 + runtime 단독 (Primary `rfc8785`) — C-A3 | runtime 시 cross-check 강조 (영역 5 #1 단일 라이브러리 bug-class 회피 HIGH + #2 supply chain compromise BLOCK 자동 발화) — runtime 명시는 사양 §3.1 답습 한정 | Mode 2 (corpus cross-check only, runtime 1×) — 50% overhead 감소 권고 |

**총 1 불일치** — 핵심 갈등 영역 (Phase 4 §4.3).

### 3.4 ④ 누락 (Gap) — 특정 Agent 만 언급

| # | 사항 | 단독 언급 |
|---|------|---------|
| G-1 | **`event: external_llm_received` (#8) 미적용 → ADR-012 §2.12 #4 cover 0** | B Gap-N #1 (HIGH) |
| G-2 | **`evidence_forgery_detected` (#9) 미적용 → P10 정식 등록 trigger 부분 발화** | B Gap-N #2 (HIGH) |
| G-3 | **`policy_change_attempted` (#16) 미적용 → Hermes 정책 변경 시도 검출 layer 부재** | B Gap-N #3 (HIGH) |
| G-4 | **PyPI signature (sigstore / GPG) 검증 부재** | B C-B1 + Gap-N #5 (MEDIUM-HIGH) |
| G-5 | **`rfc8785` 0.x → 0.2 격상 시 RA-9 재실행 의무** | B C-B2 (MEDIUM) |
| G-6 | **CI workflow Reviewer notification step 권고** (`canonical_json_fallback` entry 발화 시) | B C-B13 (MEDIUM) |
| G-7 | **fallback 빈도 > 10% 시 T2 escalation 절차 명시** (ADR-012 §3.5 답습) | B C-B14 (MEDIUM) |
| G-8 | **`event` enum #14 ↔ #15 의미 중첩 정리 권고** | B C-B15 (LOW) |
| G-9 | **air-gap 환경 시 `jq` binary 별도 보관 권고** | B C-B12 (LOW-MEDIUM) |
| G-10 | **본 PoC Docker 격리 환경 권고** (현 venv 격리만) | B C-B17 (MEDIUM) |
| G-11 | **PyPI release frequency monitoring 권고** (월 1회 자동 확인) | B C-B6 (MEDIUM) |
| G-12 | **`jcs` maintainer abandonment 시 fallback 정책 명시** (TR-C-7 권고) | B C-B5 (HIGH) |
| G-13 | **CI workflow setup step `jcs` install 누락** (사양 §6 명시 미흡) | A R-A2 (HIGH) |
| G-14 | **`tools/canonical_json.py` API normalization wrapper 의무** (str/bytes 분기) | A C-A4 (LOW) |
| G-15 | **nightly round-trip schedule 분리 명시 (`on: schedule` cron 정의)** | A C-A8 (LOW) |
| G-16 | **24 vs 20 corpus 단순화 비권고** (8 카테고리 균형) | C §2.7 (단순화 비권고 명시) |
| G-17 | **Round-trip T3 lossy 분리 (후속 PoC) 단순화 안** | C 권고 안 #2 (사용자 Q3 답습 시 비권고) |
| G-18 | **`rfc8785` 단독 backup plan (Alt-2) 사양 §B.5 cross-reference** | C C-C2 (HIGH) |
| G-19 | **non-BMP surrogate pair corpus case 추가 권고** | B C-B9 (MEDIUM) |

**총 19 누락 사항** — 중요도 평가 후 채택/제외 (Phase 4 §4.4).

---

## 4. Phase 4 — 합의 도출 (핵심 갈등 + 채택/제외 사유)

### 4.1 일치 사항 (13건) — 모두 그대로 채택

K-1 ~ K-13 모두 3/3 Agent 동의 + 5 영구 핵심 제약 보호 + 사용자 명시 갱신 결정 권위 답습 → **모두 본 합의 채택** + §5 통합 조건에 흡수.

### 4.2 부분 일치 (7건) — 소수 의견 평가 후 결정

| # | 결정 | 사유 |
|---|------|------|
| P-1 | **채택** (corpus 회귀 한정 cross-check + runtime 단독 권고 — 본 PoC 구현 시 정량 measurement 후 결정) | A + C 일치 + B 의 runtime cross-check 보안 layer 강화 사유는 *명시 영역 부재* (사양 §3.1 의 "두 라이브러리 모두 사용" 해석 영역). 사용자 명시 결정 권위 부정 0건 회피 — 본 PoC 구현 시 정량 측정 후 결정 (C-A3 + C-C1 결합) |
| P-2 | **채택** (`jcs` 개인 maintainer 위험 HIGH 명시) | B + C 일치 (HIGH 평가) + A 의 운영 가능성 관점 한정 (보안 미평가) — Reviewer 종합 시 보안 평가 우선 |
| P-3 | **채택** (`canonicaljson` 비채택 사유 명시 보강) | C 명시 + B 간접 동의 + ADR-012 §2.5 후보 부재 사유 정합 |
| P-4 | **채택** (`jq` 특정 버전 pin 의무) | B 명시 + A 간접 동의 (jq install 명시) — version drift 위험 회피 (C-B11) |
| P-5 | **채택** (violation_type 4종 vs FAIL fixture 4종 cross-reference 명확화) | A + B 일치 (교집합 2건 한정) + 본 PoC 검증 cover 완전성 보장 (C-A5 답습) |
| P-6 | **채택** (T3 lossy fixture 정의 또는 cross-reference 명시) | A + C 일치 + Round-trip T3 lossy 자동 영역 (3 ledger entry 형식 자동 작성) 본 PoC 검증 evidence 보강 (C-A6 답습) |
| P-7 | **채택** (cross-vendor LLM 1+ 의뢰 권고 격상) | B + C 일치 (HIGH) + A 한계 자기 명시 (간접) + ADR-012 §11.2 C-14 + §11.3 답습 |

### 4.3 불일치 (1건) — 핵심 갈등 영역 + Reviewer 판단

#### D-1 — Cross-check 시점: corpus only vs runtime+corpus

**Agent 별 입장 정확 인용**:

- **Agent A (§2.2 영역 2 + C-A3)**: "본 권고는 PoC 사양 §1.1 / §3.1 의 '두 라이브러리 모두 사용' *해석 영역* — Reviewer 영역. 본 Agent A 권고: corpus 회귀 step 한정 cross-check + runtime entry 는 Primary 단독 (조건 §4 C-A4 답습)" — **Mode 2 와 사실상 일치**
- **Agent B (§2.5 영역 5)**: 영역 5 차원 평가에서 cross-check 자체의 *보안 이점* 강조. 단 *runtime 영역 명시* 부재 — 사양 §3.1 답습 한정 + C-B7 ("Primary 1 ↔ Primary 2 동등성 실패 escalation 명시") 강조. Runtime 영역 명시적 권고 부재
- **Agent C (§2.4 영역 4 + 권고 안 #1)**: "**Mode 2 (corpus cross-check only, runtime 1×)** 권고 — 단일 lib bug detection layer 보존 (corpus 시점) + runtime overhead 50% 감소 + ADR-012 §3.5 monitoring trigger 발화 위험 ↓"

**Reviewer 판단 — 사용자 명시 갱신 결정 권위 cross-reference**:

사양 §3.1 직접 인용: *"본 PoC 는 두 라이브러리 모두 사용 — 출력 byte 동등성 + sha256 동등성 100% 검증을 corpus 24개 모든 case 에 강제. 양 라이브러리 의견 불일치 시 BLOCK + escalation (TR-C-2 trigger)."*

→ **사용자 명시 영역 = corpus 24개 시점**. *runtime cross-check 의무* 는 *해석 영역* (명시 부재).

**채택 결정**: **corpus 24개 시점 cross-check 의무 (강제, BLOCK + TR-C-2 발화) + runtime entry cross-check = 본 PoC 구현 시 정량 measurement 후 결정 (C-A3 + C-C1 결합)**.

**채택 사유** (4건):
1. 사용자 명시 갱신 결정 *명시 영역* 보존 (corpus 24개 강제)
2. 사용자 명시 결정 *해석 영역* (runtime cross-check) 은 *정량 evidence 후 결정* — 권위 부정 0건 + 단순화 비권고 0건
3. Agent C 의 *implementation bug detection layer* 의 진정한 가치 = corpus 시점 (lib 자체 검증) — Agent A 와 일치
4. Agent B 의 runtime 영역 명시적 권고 부재 = corpus 시점 한정 cross-check 도 *충족 가능 layer*

**비채택 사유** (Mode 1 — runtime 마다 cross-check 강제):
- 운영 부담 격증 (entry 마다 2× canonicalize) + ADR-012 §3.5 monitoring trigger 발화 위험 ↑
- Agent A R-A3 (MEDIUM) 답습 — 운영 risk

**비채택 사유** (Mode 4 — Alt-2 `rfc8785` 단독, cross-check 0):
- 사용자 명시 갱신 결정 (Alt-1) *부정* 위험 — Agent C §6.3 자기 명시 답습
- cryptography 검토자 한계 영역 (ADR-012 §11.3) 보강 layer 부재

→ **본 합의 = corpus 시점 cross-check 의무 (사용자 명시 영역 답습) + runtime cross-check = 본 PoC 구현 시 정량 measurement 후 결정** 채택. 통합 조건 §5 C-1 + C-3 흡수.

### 4.4 누락 사항 (19건) — 중요도 평가 후 결정

#### 4.4.1 본 합의 채택 (HIGH 영역 11건)

| # | 결정 | 사유 |
|---|------|------|
| G-1 (Gap-N #1) | **§9 별도 합의 영역 명시 + §11 한계 흡수** | HIGH — 본 PoC §11 L-3 한계 자기 명시 적격 + Q1 외 영역 (외부 LLM response ledger entry 형식 PoC 별도) |
| G-2 (Gap-N #2) | **§9 별도 합의 영역 명시 + §11 한계 흡수** | HIGH — 본 PoC §11 L-5 답습 + ADR-012 §3.3 한계 답습 (content-level forgery 방어 범위 외) |
| G-3 (Gap-N #3) | **§9 별도 합의 영역 명시 + §11 한계 흡수** | HIGH — Hermes 정책 변경 시도 검출 = G3 §2.5 #11 + Group G 영역 (별도) |
| G-12 (C-B5 → TR-C-7) | **본 PoC §9.1 escalation trigger TR-C-7 등록** | HIGH — `jcs` maintainer abandonment 시 fallback 정책 명시 의무 |
| G-13 (R-A2) | **본 PoC §6 setup step `jcs` install 추가 의무** | HIGH — 사양 §6 갱신 (P0) |
| G-18 (C-C2) | **본 PoC §B.5 escalation 매트릭스 cross-reference 명시 보강** | HIGH — Alt-2 backup plan TR-C-2 발화 시 즉시 격상 가능 layer |
| G-19 (C-B9) | **본 PoC §3.4 corpus `unicode` 카테고리 추가 권고** | MEDIUM — non-BMP surrogate pair case 보강 |
| G-4 (C-B1) | **별도 합의 영역 (RA-9 후속 항목)** | MEDIUM — PyPI signature 검증 별도 의무 |
| G-5 (C-B2 → TR-C-6) | **본 PoC §9.1 escalation trigger TR-C-6 등록** | MEDIUM — `rfc8785` 0.x → 0.2 격상 시 RA-9 재실행 의무 |
| G-6 (C-B13) | **본 PoC §6 + 별도 합의** | MEDIUM — CI workflow Reviewer notification step 권고 |
| G-7 (C-B14) | **본 PoC §9.1 TR-C-4 본문 보강** | MEDIUM — fallback 빈도 > 10% 시 T2 escalation 절차 명시 |

#### 4.4.2 본 합의 채택 (LOW/MEDIUM 영역 5건)

| # | 결정 | 사유 |
|---|------|------|
| G-8 (C-B15) | **별도 합의 영역 (ADR-012 §2.2 본문 갱신 영역)** | LOW — `event` enum #14 ↔ #15 의미 중첩 정리 |
| G-9 (C-B12) | **본 PoC §6 setup step 주석 보강** | LOW-MEDIUM — air-gap 환경 시 `jq` binary 별도 보관 |
| G-10 (C-B17) | **본 PoC §7 답습 강제 조건 보강** | MEDIUM — Docker 격리 환경 권고 (ADR-011 §2.1 (b) 답습) |
| G-14 (C-A4) | **본 PoC `tools/canonical_json.py` API normalization wrapper 의무** | LOW — str/bytes 분기 처리 (`.poc-prep/sanity_equivalence.py:26-27` 답습) |
| G-15 (C-A8) | **본 PoC `.github/workflows/g4-hash-chain.yml` `on: schedule` cron 정의 의무** | LOW — nightly round-trip schedule 분리 명시 |

#### 4.4.3 본 합의 비채택 (3건)

| # | 결정 | 사유 |
|---|------|------|
| G-11 (C-B6) | **별도 합의 영역 (Q1 외)** | PyPI release frequency monitoring 권고 = Q1 영역 외 별도 운영 합의 |
| G-16 (C 단순화 비권고) | **24 corpus 유지 채택** | C 자기 단순화 비권고 명시 — Q2 단축 합의 영역 |
| G-17 (C 권고 안 #2) | **본 합의 비채택** (사용자 Q3 결정 답습) | Round-trip T3 lossy 분리 = 사용자 Q3 결정 (6 영역 통합) 답습 시 정당성 약화 + 합의 비용 2× |

---

## 5. Phase 5 — 최종 verdict + 통합 조건 매트릭스

### 5.1 최종 verdict

```
APPROVE WITH CONDITIONS — G4 Q1 (rfc8785 + jcs 병렬 cross-check) 본 PoC 진입 적격
```

3/3 Agent 일치 (§2.2) + 5 영구 핵심 제약 5/5 HIGH 보호 (§7) + Hermes 변조 차단 매트릭스 §2.12 #2 HIGH cover (§8).

### 5.2 통합 조건 매트릭스 (17건)

본 합의는 Agent A 8 조건 + Agent B 17 조건 + Agent C 5 조건 = **30 조건 → 중복 제거 + Reviewer 추가 → 17 통합 조건** 으로 정리. Agent 별 조건 ID 보존 (C-A1 / C-B3 / C-C2 등).

#### 5.2.1 본 PoC 진입 *전* P0 의무 (HIGH 4건)

| # | 통합 조건 ID | 출처 | 조건 | 처리 |
|---|------|------|------|------|
| C-1 | **CR-P0-1** (C-A1) | A R-A1 + B C-B7 + C C-1 | corpus 24개 양 라이브러리 동등성 재검증 의무 — 본 PoC 구현 첫 step. 1+ case 불일치 시 TR-C-2 escalation 발화 | 본 PoC 구현자 책임 (Group C) |
| C-2 | **CR-P0-2** (C-A2 + R-A2) | A R-A2 | 본 PoC 사양 §6 setup step `jcs` install 추가 의무 | 사양 §6 갱신 (본 합의 머지 직후) |
| C-3 | **CR-P0-3** (C-B7 보강) | B C-B7 | 사양 §9.1 TR-C-2 본문 명시 보강 — "Primary ↔ Fallback" → "Primary 1 ↔ Primary 2 또는 Primary ↔ Fallback" | 사양 §9.1 갱신 (본 합의 머지 직후) |
| C-4 | **CR-P0-4** (C-B16 + C-C5) | B C-B16 + C C-C5 | Q1 풀 3+1 합의 + cross-vendor LLM 1+ 의뢰 결합 권고 (P2 v3 정식 채택 진입 *전* 의무 답습 — ADR-012 §11.2 C-14 + §11.3) | Reviewer 결정 영역 — `external_review/` 디렉토리 사용 + `event: external_llm_received` 패턴 답습 (별도) |

#### 5.2.2 본 PoC 구현 시 P1 의무 (HIGH 3건 + MEDIUM 5건)

| # | 통합 조건 ID | 출처 | 조건 | 처리 |
|---|------|------|------|------|
| C-5 | **CR-P1-1** (C-B3) | B C-B3 | `jcs` last release date / commit frequency 검증 의무 (RA-9 §B 보강) | 본 PoC 머지 *전* 의무 |
| C-6 | **CR-P1-2** (C-B4) | B C-B4 | `jcs` *primary 단독 격상 금지* 영구 명시 — 사양 §3.1 + ADR-012 §2.5 cross-reference 보강 | 사양 §3.1 갱신 |
| C-7 | **CR-P1-3** (C-B8) | B C-B8 | corpus `number` 카테고리에 NaN/Infinity reject case 추가 의무 (24+N 권고) | 사양 §3.4 + 본 PoC 구현 시 |
| C-8 | **CR-P1-4** (C-A3 + C-C1) | A C-A3 + C C-C1 | `tools/canonical_json.py` API: corpus 회귀 step 한정 cross-check + runtime entry Primary (`rfc8785`) 단독 권고 + cross-check overhead 정량 measurement 본 PoC 구현 시 의무 | 본 PoC 구현자 책임 |
| C-9 | **CR-P1-5** (C-A4) | A C-A4 | `tools/canonical_json.py` API normalization wrapper 의무 (str/bytes 분기 처리) | 본 PoC 구현 시 |
| C-10 | **CR-P1-6** (C-A5) | A C-A5 | violation_type 4종 cover 의무 — FAIL fixture 추가 (`history_rewrite` / `genesis_mismatch`) 또는 cross-reference 명확화 | 본 PoC 구현 시 |
| C-11 | **CR-P1-7** (C-A6) | A C-A6 | T3 lossy fixture 정의 또는 corpus `lossy` 카테고리 cross-reference 명시 | 본 PoC 구현 시 |
| C-12 | **CR-P1-8** (C-A7) | A C-A7 | `event` MVP 4종 한정 검증 = *validator 자동 작성 enum* 한정 + fixture 의 다양한 enum 포함 OK 명확화 | 사양 + 본 PoC 구현 시 |

#### 5.2.3 본 PoC 사양 보강 P2 의무 (MEDIUM 5건)

| # | 통합 조건 ID | 출처 | 조건 | 처리 |
|---|------|------|------|------|
| C-13 | **CR-P2-1** (C-C3) | C C-C3 | `canonicaljson` (Matrix.org) 비채택 사유 본 PoC 사양 §3.2 또는 부록 A 명시 보강 | 사양 §3.2 갱신 |
| C-14 | **CR-P2-2** (C-C4) | C C-C4 | `jq` fallback 의 RFC 8785 *완전 동등성 부재* 한계 명시 보강 (ADR-012 §11.3 답습) | 사양 §3.2 + §11 갱신 |
| C-15 | **CR-P2-3** (C-C2) | C C-C2 | Alt-2 (`rfc8785` 단독) backup plan 본 PoC 사양 §B.5 escalation 매트릭스 cross-reference 명시 보강 | 사양 §B.5 갱신 |
| C-16 | **CR-P2-4** (C-B11) | B C-B11 | `jq` 특정 버전 pin 의무 (예: `jq>=1.6,<1.8`) 본 PoC `.github/workflows/g4-hash-chain.yml` setup step 명시 보강 | 사양 §6 갱신 |
| C-17 | **CR-P2-5** (C-B14) | B C-B14 | fallback 빈도 > 10% 시 T2 escalation 절차 명시 — 사양 §9.1 TR-C-4 본문 보강 ("round-trip T2 strict 실패율" → "+ fallback 빈도 > 10%") | 사양 §9.1 갱신 |

#### 5.2.4 본 합의 외 별도 합의 영역 (참조)

| # | 출처 | 조건 | 별도 합의 영역 |
|---|------|------|---------------|
| (Sep-1) | B C-B1 | `rfc8785` PyPI signature (sigstore / GPG) 검증 의무 | 별도 RA-9 후속 항목 |
| (Sep-2) | B C-B6 | PyPI release frequency monitoring 권고 (월 1회 자동 확인) | 별도 운영 합의 |
| (Sep-3) | B C-B10 | crypto specialist 추가 검토 권고 (ADR-012 §11.3 답습) | 본 PoC 머지 후 별도 의뢰 (cross-vendor LLM 으로 부분 대체 가능 — C-4 결합) |
| (Sep-4) | B C-B12 | air-gap 환경 시 `jq` binary 별도 보관 권고 | 본 PoC §6 setup step 주석 보강 (LOW-MEDIUM) |
| (Sep-5) | B C-B13 | CI workflow Reviewer notification step 권고 | 별도 합의 (notification 매커니즘) |
| (Sep-6) | B C-B15 | `event` enum #14 ↔ #15 의미 중첩 정리 권고 | 별도 합의 (ADR-012 §2.2 본문 갱신 영역) |
| (Sep-7) | B C-B17 | 본 PoC Docker 격리 환경 권고 | 본 PoC §7 답습 강제 조건 보강 (MEDIUM) |
| (Sep-8) | A C-A8 | nightly round-trip schedule 분리 명시 | 본 PoC `.github/workflows/g4-hash-chain.yml` `on: schedule` cron 정의 (LOW) |

#### 5.2.5 통합 조건 통계

- **본 PoC 진입 *전* P0 의무**: HIGH 4건 (C-1 ~ C-4)
- **본 PoC 구현 시 P1 의무**: HIGH 3건 (C-5, C-6, C-7) + MEDIUM 5건 (C-8 ~ C-12)
- **본 PoC 사양 보강 P2 의무**: MEDIUM 5건 (C-13 ~ C-17)
- **별도 합의 영역**: 8건 (Sep-1 ~ Sep-8)
- **합산**: 17 통합 조건 (HIGH 7건 / MEDIUM 7건 / LOW 3건) + 별도 합의 영역 8건

---

## 6. Escalation Trigger (TR-C-1 ~ TR-C-7)

본 합의 결과로 등록할 escalation trigger:

| # | trigger | 격상 | 본 합의 출처 |
|---|---------|------|------------|
| TR-C-1 | RA-9 사전 검증 결과 양 후보 모두 install 불가 | Q1 재합의 (stdlib + jq 단독 검토) | 사양 §9.1 답습 (`pyjcs` 1건 부분 발화 → 갱신 결정 흡수) |
| TR-C-2 | corpus 24개 중 1+ Primary ↔ Fallback **또는 Primary 1 ↔ Primary 2** 동등성 실패 | Q2/Q3 풀 3+1 격상 | 사양 §9.1 + **C-3 (CR-P0-3) 보강** |
| TR-C-3 | `event` 17 enum 중 본 PoC MVP 4종 외 추가 발화 | 별도 합의 + ADR-012 §2.2 cross-reference | 사양 §9.1 답습 |
| TR-C-4 | round-trip T2 strict 실패율 > 0% **+ fallback 사용 빈도 > 10%** | 풀 3+1 + ADR-012 §2.5 fallback 정식화 검토 | 사양 §9.1 + **C-17 (CR-P2-5) 보강** |
| TR-C-5 | Hermes 의존 발견 (subprocess Hermes 호출 등) | 즉시 BLOCK + ADR-008 차단조건 #2 위반 escalation | 사양 §9.1 답습 |
| TR-C-6 | **`rfc8785` 0.x → 0.2 격상 (semver minor)** | RA-9 재실행 + Q1 재검증 | **본 합의 신규 (C-B2 → CR-P2 영역)** |
| TR-C-7 | **`jcs` (titusz) maintainer abandonment 검출 (last release > 12개월 또는 PyPI 패키지 삭제)** | 풀 3+1 + fallback 정책 결정 (`rfc8785` + jq 단독 또는 다른 라이브러리 cross-check) | **본 합의 신규 (C-B5 → CR-P1 영역)** |

---

## 7. Provider Liquidity 보존 강도 매트릭스 (5 영구 핵심 제약)

본 합의 결과 5 영구 핵심 제약 보호 강도 (Agent B §4 답습 + Reviewer 종합):

| 제약 | 권위 근거 | 본 Q1 보호 위치 | 강도 |
|------|---------|---------------|------|
| **Provider Liquidity** (헌법 5조 비협상) | `feedback_provider_liquidity.md` + ADR-008 차단조건 #2 + ADR-012 5-way Multi-layer Defense | `rfc8785` + `jcs` 모두 Apache-2.0 + provider-neutral PyPI + 의존 0 + RFC 8785 IETF 표준 (vendor-neutral) + `jq` POSIX 표준 + 라이브러리 교체 비용 LOW (RFC 동등성 byte-level) | **HIGH** |
| **Hermes ≠ root of trust** (ADR-011 §2.3 영구 권위) | ADR-011 §2.3 + ADR-012 §2.12 4 항목 | 본 PoC 도구 = `import hermes_agent` 0건 + `agent` 필드 enum 검증 + chain 검증으로 Hermes-originated entry *사후 검출 layer* 제공 (단 §2.12 #1/#3/#4 미cover 영역 = §9 Gap-N #1, #3 흡수) | **HIGH** (단 Gap-N 4건 §11 한계 흡수 의무) |
| **메타포 강제 금지** (system-identity-prequel §7) | ADR-012 §1.5 답습 | 본 PoC = *형식적 무결성 한정 자기 명시* (사양 §0 + §11 L-5 답습) — *불변의 진리* 메타포 회피. 두 라이브러리 = *cross-check reference*, root of trust 메타포 부여 0건 | **HIGH** |
| **자동 정책 변경 금지 (T3)** (ADR-011 §2.4) | ADR-011 §2.4 + ADR-012 §2.7 | chain violation 검출 시 자동 revert 0건 + manual review 강제 + `chain_violation_detected` entry 자동 작성 (T1 audit) ↔ chain 수정 (T3 BLOCK) 분리 정합. fallback 사용 = T1 audit | **HIGH** |
| **수단/목적 분리** (ADR-011 §2.1 (a)~(e)) | ADR-011 §2.1 5조건 | (a) 동등 이상 보안 결과 — 단일 라이브러리 대비 cross-check 강화 / (b) 격리 환경 PoC 실증 — venv `.poc-prep/jcs-ra9-venv/` 본 RA-9 (Docker 격리는 Sep-7 별도 권고) / (c) ADR 권위 명시 — ADR-012 §2.5 답습 / (d) 자동 회귀 검증 — `.github/workflows/g4-hash-chain.yml` / (e) 합의 APPROVE — 본 Q1 풀 3+1 합의 채택 | **HIGH** |

**5/5 HIGH 보호 적격** (단 (b) Docker 격리 별도 권고 — Sep-7 + Hermes 변조 차단 §2.12 4 항목 cover 보강 의무 — §9 Gap-N).

---

## 8. Hermes 변조 차단 매트릭스 cover 분석 (ADR-012 §2.12 4 항목 ↔ 본 PoC)

Agent B §5 답습:

| # | 변조 영역 | 차단 매커니즘 (ADR-012 §2.12 답습) | 본 PoC cover | 강도 | Gap |
|---|--------|-----------|----|----|-----|
| 1 | Hermes-originated ledger entry | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | **부분 cover** (`agent` 필드 enum 검증 + chain 검증 사후 검출. 단 *작성 차단* 매커니즘 = G3 §2.5 #11 영역 외) | MEDIUM | 작성 차단 매커니즘 = G3 §2.5 #11 + G3 §2.2 #20 영역 (별도) |
| 2 | 파일 변조 (filesystem 직접 변경) | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 | **HIGH cover** — 본 PoC 핵심 영역. hash chain 검증 (Layer 1) + canonical JSON 일관성 + sha256 = filesystem 직접 변조 *결정적 검출* | **HIGH** | 0 |
| 3 | Git commit (Hermes 가 ledger commit 시도) | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | **부분 cover** (chain 검증 결과를 git pre-commit hook 에서 호출 가능 — 본 PoC 가 *호출 대상 도구* 제공. commit author 검증 자체는 본 PoC 영역 외) | MEDIUM | git pre-commit hook commit author 검증 = G3 §2.2 #20 영역 (별도) |
| 4 | 외부 LLM 응답 위조 | External LLM response ledger entry `agent = "user"` 강제 + signed commit 권장 | **0 cover** — `event: external_llm_received` (#8) MVP 4종 한정 외 (영역 11 답습) | 0 (HIGH Gap) | **Gap-N #1 (§9 enumerate)** — 별도 합의 영역 명시 의무 |

**종합 판정**:
- **#2 HIGH cover** (본 PoC 핵심 영역 적중)
- **#1 / #3 부분 cover** (도구 제공 — 별도 차단 매커니즘 영역 명시)
- **#4 0 cover** (Gap-N #1 §9 흡수)

본 PoC = ADR-012 §2.12 4 항목 중 **1/4 HIGH cover + 2/4 부분 cover + 1/4 0 cover**. **최소 1/4 HIGH cover 충족** → §2.12 답습 *부분 적격* + 1/4 0 cover 영역 (#4) 은 §9 Gap-N #1 흡수 의무.

---

## 9. Gap-N HIGH 흡수 결정 (본 PoC 흡수 vs 별도 합의 영역 분리)

본 §9 = Agent B §7 Gap-N 답습 형식 — Reviewer 종합 결정.

### 9.1 Gap-N #1 (HIGH) — External LLM Response 위조 차단 layer 0 cover

- **흡수 결정**: **본 PoC §11 한계 자기 명시 흡수 (L-3 답습) + 별도 합의 영역 명시 의무**
- **별도 합의 영역**: *외부 LLM response ledger entry 형식 PoC* (ADR-012 §3.1 답습) — Q1 외 영역
- **부분 완화**: C-4 (CR-P0-4) Q1 cross-vendor LLM 의뢰 결합 시 *Q1 합의 자체* 가 외부 LLM 의뢰 evidence 산출 → 부분 완화

### 9.2 Gap-N #2 (HIGH) — Evidence Forgery 검출 layer 부분 cover

- **흡수 결정**: **본 PoC §0 + §11 L-5 한계 자기 명시 흡수**
- **별도 합의 영역**: ADR-012 §3.3 답습 — content-level forgery = 헌법 1조 + 합의 인프라 + Reviewer 종합 + Human override layer (별도)
- **본 PoC 영역 외 = 적격**

### 9.3 Gap-N #3 (HIGH) — Policy Change Attempted 검출 layer 0 cover

- **흡수 결정**: **본 PoC §11 한계 자기 명시 흡수 (L-3 답습) + 별도 합의 영역 명시 의무**
- **별도 합의 영역**: *Hermes 정책 변경 시도 검출 hook* — Group G 영역 (Hermes container write 권한 0 = G3 §2.5 #11)

### 9.4 Gap-N #4 (HIGH) — `jcs` (titusz) 개인 maintainer supply chain HIGH 잔여 위험

- **흡수 결정**: **C-5 (CR-P1-1) + C-6 (CR-P1-2) + TR-C-7 등록 결합 적용**
- **본 PoC §3.1 명시 ("`jcs` *primary 단독 격상 금지* 영구") 권고 (C-6 답습)**
- **escalation trigger TR-C-7 등록 권고 (CR-P0-3 결합)**

### 9.5 Gap-N #5 (MEDIUM-HIGH) — RA-9 §B 미검증 영역 (signature / last release / abandonment)

- **흡수 결정**: **C-5 (CR-P1-1) + (Sep-1) 별도 합의 영역 분리**
- **본 PoC 머지 *전* C-5 의무 적용**
- **PyPI signature (sigstore / GPG) 검증** = 별도 RA-9 후속 항목 (Sep-1)

**Gap-N 종합**: HIGH 4건 + MEDIUM-HIGH 1건. 모두 *본 PoC §11 한계 자기 명시 흡수 + 별도 합의 영역 명시 의무 + C-* 통합 조건 적용* 으로 완화. CRITICAL Gap 0건 → **APPROVE WITH CONDITIONS** 적격.

---

## 10. 사용자 명시 결정 권위 정합 검증

본 §10 = 사용자 명시 갱신 결정 권위 trace 의 본 합의 정합 검증.

### 10.1 사용자 명시 갱신 결정 (Alt-1) 적격성

| 차원 | 사용자 명시 결정 (사양 §3.1) | 본 합의 결과 정합 |
|------|--------------------------|----------------|
| 라이브러리 채택 | `rfc8785` + `jcs` 병렬 cross-check | ✅ 채택 (3/3 Agent 일치 K-1) |
| Cross-check 시점 (corpus) | corpus 24개 모든 case 강제 | ✅ 채택 (사용자 명시 영역 — §4.3 D-1 결정) |
| Cross-check 시점 (runtime) | (사양 §3.1 명시 부재 — 해석 영역) | ⚠️ 본 PoC 구현 시 정량 measurement 후 결정 (C-8 답습) — 사용자 명시 결정 *부정 0건* |
| 의견 불일치 시 BLOCK + escalation (TR-C-2) | 강제 명시 | ✅ 채택 (CR-P0-3 보강 — Primary 1 ↔ Primary 2 명시 추가) |
| Fallback (`jq -S -c` + `canonical_json_fallback` entry) | ADR-012 §2.5 답습 | ✅ 채택 (3/3 Agent 일치 K-5) |

### 10.2 갱신 권위 trace (RA-9 §B.3 발견 → 갱신 결정 흡수)

| # | 단계 | 답습 |
|---|------|------|
| 1 | 원본 사용자 명시 결정 (`rfc8785` + `pyjcs` 병렬) | roadmap §4.1 |
| 2 | RA-9 §B.1 결과 (`pyjcs` PyPI 미존재) | 사양 §B.1 |
| 3 | RA-9 §B.3 발견 (`jcs` 0.2.1 PyPI 발굴 + sanity 11/11 PASS) | 사양 §B.3 |
| 4 | 사용자 명시 결정 갱신 (`rfc8785` + `jcs` 병렬 흡수) | 사양 §3.1 + 부록 A |
| 5 | 본 Q1 합의 (사용자 명시 갱신 결정 적격성 검증) | 본 보고서 |

→ **사용자 명시 결정 권위 부정 0건**. 갱신 권위 trace = TR-C-1 부분 발화 후 갱신 결정으로 흡수 (RA-9 §B.5 답습).

---

## 11. 본 합의 진입 *전* / 구현 *시* / 구현 *후* 의무 분리 매트릭스

| 시점 | 의무 | 통합 조건 ID |
|------|------|------------|
| **본 합의 진입 *전*** (이미 충족) | RA-9 §B 6 항목 검증 + sanity 11/11 PASS + 사용자 명시 갱신 결정 권위 흡수 | (이미 충족) |
| **본 합의 머지 *직후*** | 사양 §3.1 + §3.2 + §3.4 + §6 + §9.1 + §11 + §B.5 갱신 (C-2, C-3, C-6, C-7, C-13 ~ C-17) | C-2 / C-3 / C-6 / C-7 / C-13 / C-14 / C-15 / C-16 / C-17 |
| **본 PoC 구현 *전*** (P0) | (1) corpus 24개 동등성 재검증 (C-1) / (2) `jcs` last release 검증 (C-5) / (3) cross-vendor LLM 1+ 의뢰 결정 (C-4) | C-1 / C-4 / C-5 |
| **본 PoC 구현 *시*** (P1) | (1) cross-check overhead 정량 measurement (C-8) / (2) API normalization wrapper (C-9) / (3) violation_type 4종 cover (C-10) / (4) T3 lossy fixture (C-11) / (5) `event` MVP 4종 한정 명확화 (C-12) | C-8 / C-9 / C-10 / C-11 / C-12 |
| **본 PoC 구현 *후*** (Reviewer-only 단축) | 본 PoC 자체 합의 (Reviewer-only — Q4 결정 답습) | 별도 합의 |
| **본 합의 외 별도 합의 영역** | Sep-1 ~ Sep-8 + Gap-N #1 / #2 / #3 별도 합의 영역 | 별도 |

---

## 12. 자기 명시 한계 (P-1 ~ P-7)

본 §12 = Agent A §0.2 + Agent B §0.3 + Agent C §6 + §8 답습 — 본 합의가 cover 하지 못하는 영역 자기 명시.

| # | 한계 | 회피 매커니즘 / 별도 합의 영역 |
|---|------|---------------------|
| **P-1** | Reviewer = Claude Opus 4.7 메인 컨텍스트 = G4 PoC 사양 작성 컨텍스트와 동일 패밀리. 자기 작성 산출 자기 검토 위험 잔존 | C-4 (cross-vendor LLM 1+ 의뢰) 결합 + ADR-012 §11.2 C-14 + §11.3 답습 |
| **P-2** | Agent A/B/C 모두 동일 Claude 패밀리 — 외부 LLM 의견 부재 | 본 합의 권위 = Reviewer 종합 *내부 작업* + cross-vendor 의뢰 권고 격상 (C-4) |
| **P-3** | RFC 8785 동등성 자체의 *cryptography* 심층 검증은 본 합의 검토자 한계 (ADR-012 §11.3 답습) — corpus 24개 reference output 검증으로 *부분 완화* | crypto specialist 추가 검토 별도 합의 (Sep-3) + cross-vendor LLM 의뢰 (C-4) 부분 대체 |
| **P-4** | 본 합의 = Q1 *한정* — Q2 (corpus 24개 + 8 카테고리) / Q3 (PoC 6 영역) 본문 평가 미수행 | Q4 결정 답습 — Q2/Q3 Reviewer-only 단축 합의 별도 |
| **P-5** | 본 합의 = *Implementation/Runtime PASS 영역 외* — Group C PoC 구현 후 별도 Reviewer-only 단축 합의 의무 | Q4 결정 답습 |
| **P-6** | Cross-check overhead 정량 evidence 부재 (Agent C 권고 안 #1 의 50% overhead 감소 추정 = C-A3 / C-C1 후 본 PoC 구현 시 정량 measurement 후 결정) | C-8 (CR-P1-4) 본 PoC 구현 시 정량 measurement 의무 |
| **P-7** | Hermes 변조 차단 매트릭스 §2.12 4 항목 중 #4 (외부 LLM 응답 위조) 0 cover | Gap-N #1 (§9.1) 본 PoC §11 한계 자기 명시 흡수 + 별도 합의 영역 |

---

## 13. 답습 매트릭스

본 §13 = 본 합의 권위 답습 정합 검증.

### 13.1 CLAUDE.md §3 (3+1 멀티 에이전트 합의 5 Phase) 답습

| Phase | 답습 위치 | 비고 |
|-------|---------|------|
| Phase 1 (분배) | §2.1 | 메인 Reviewer 가 3 관점 분배 |
| Phase 2 (독립 분석) | §2.2 (3 Agent 산출물 직접 인용) | 3 Agent 모두 다른 Agent 출력 참조 0건 (편향 회피) |
| Phase 3 (교차 비교) | §3 (4 분류 매트릭스 — 일치 13건 / 부분 일치 7건 / 불일치 1건 / 누락 19건) | 답습 정합 |
| Phase 4 (합의 도출) | §4 (일치 그대로 채택 + 부분 일치 평가 후 결정 + 불일치 핵심 갈등 §4.3 + 누락 중요도 평가 §4.4) | 답습 정합 |
| Phase 5 (보고) | §5 + §0.3 (Reviewer 종합 verdict + 통합 조건 17건) | 답습 정합 |

### 13.2 ADR-011 §2.1 (a)~(e) 5조건 답습

| 조건 | 답습 위치 |
|------|---------|
| (a) 동등 이상의 보안 결과 | §7 (Provider Liquidity 5/5 HIGH) + §2.5 영역 5 답습 (단일 라이브러리 대비 cross-check 강화) |
| (b) 격리 환경 PoC 실증 | §7 (venv `.poc-prep/jcs-ra9-venv/` 본 RA-9 + Docker 격리 Sep-7 별도) |
| (c) ADR 권위 명시 | ADR-012 §2.5 + ADR-008 차단조건 #2 + ADR-011 §2.4 답습 |
| (d) 자동 회귀 검증 경로 | `.github/workflows/g4-hash-chain.yml` (사양 §6 답습) |
| (e) 합의 APPROVE | 본 Q1 풀 3+1 합의 채택 (본 보고서) |

### 13.3 사용자 명시 4 결정 답습

| 결정 | 본 합의 답습 |
|------|------------|
| Q1 (`rfc8785` + `pyjcs` → `jcs` 갱신 흡수) 풀 3+1 합의 | ✅ 본 보고서 (Q1 한정 풀 3+1) |
| Q2 (corpus 24개) Reviewer-only 단축 | ⏳ 별도 합의 영역 (본 합의 외) — §14 다음 진입 단계 |
| Q3 (PoC 6 영역) Reviewer-only 단축 | ⏳ 별도 합의 영역 (본 합의 외) — §14 다음 진입 단계 |
| Q4 (Q1 풀 3+1 + Q2/Q3 단축) | ✅ 본 합의 형식 답습 |

### 13.4 사용자 명시 7 금지 답습

| 금지 | 본 합의 답습 |
|------|------------|
| ❌ ADR 본문 자동 갱신 | ✅ 본 합의 = `docs/review/` + 사양 §B 흡수 한정 (별도 PR 묶음) |
| ❌ "Implementation/Runtime PASS" / "Hermes PMO 격상" 선언 | ✅ §0.2 + §10 명시 (격상 권한 0건) |
| ❌ G4 / G2 / G3 전체 PASS 선언 | ✅ §0.2 명시 |
| ❌ 신규 정책 발명 | ✅ 본 합의 = 3 Agent 분석 + ADR-012 + G4 + 사용자 명시 4 결정 답습 시제 |
| ❌ Q1 한정 — Q2/Q3 합의 흡수 금지 | ✅ §0 + §1 + §13.3 명시 |
| ❌ 실 migration script 본 구현 | ✅ §0 + §11 명시 |
| ❌ Hermes 의존 도입 | ✅ 양 라이브러리 Requires=없음 (RA-9 §B 답습) + ADR-008 차단조건 #2 자동 충족 |

---

## 14. 다음 진입 단계

본 합의 머지 후 다음 4 단계 진입:

| # | 단계 | 형식 | 출처 답습 |
|---|------|------|---------|
| 1 | **본 합의 머지** + 사양 §3.1 + §3.2 + §3.4 + §6 + §9.1 + §11 + §B.5 갱신 (C-2, C-3, C-6, C-7, C-13 ~ C-17 흡수) | (commit) | 본 합의 §11 |
| 2 | **Q2/Q3 Reviewer-only 단축 합의** (corpus 24개 + PoC 6 영역) | Reviewer-only 단축 (사용자 Q4 결정 답습) | 사양 §9 |
| 3 | **Group C PoC 구현** — `tools/canonical_json.py` + `tools/jsonl_hash_chain.py` + `tools/jsonl_roundtrip.py` + corpus 24개 + PASS/FAIL fixture 6건 + CI workflow + Evidence 산출 | TDD + C-1 / C-5 / C-8 / C-9 / C-10 / C-11 / C-12 흡수 의무 | 사양 §1.1 + §6 |
| 4 | **본 PoC Reviewer-only 단축 합의** (구현 후) | Reviewer-only 단축 (사용자 Q4 결정 답습) | 사양 §9 |

cross-vendor LLM 1+ 의뢰 (C-4) 시점 결정 = 사용자 결정 영역 (Reviewer 결정 영역 — 본 합의 머지 후 또는 본 PoC 머지 후).

---

## 15. Evidence 산출 위치

본 합의 evidence 5 형식 (R-7 SOP + 사양 §10 답습):

| # | Evidence | 위치 |
|---|----------|------|
| 1 | 본 합의 보고서 | `docs/review/3plus1-consensus-2026-05-10-g4-jcs-library-selection.md` (본 파일) |
| 2 | Agent A 입력 (구현/운영) | `docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-a-implementation.md` (378 줄) |
| 3 | Agent B 입력 (보안/거버넌스) | `docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-b-security.md` (684 줄) |
| 4 | Agent C 입력 (대안/단순화) | `docs/review/agents-2026-05-10-g4-jcs-library-selection/agent-c-alternatives.md` (507 줄) |
| 5 | RA-9 사전 검증 evidence | `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` §B (sanity 11 vector + venv `.poc-prep/jcs-ra9-venv/` + script `.poc-prep/sanity_equivalence.py`) |

---

**작성 완료**: 2026-05-10
**Reviewer**: Claude Opus 4.7 (1M context) — 메인 컨텍스트
**판정**: ✅ **APPROVE WITH CONDITIONS** (3/3 Agent 일치)
**통합 조건 수**: 17건 (HIGH 7건 / MEDIUM 7건 / LOW 3건) + 별도 합의 영역 8건
**Gap-N HIGH**: 4건 (모두 §11 한계 자기 명시 흡수 + 별도 합의 영역 명시)
**5 영구 핵심 제약 보호 강도**: 5/5 HIGH
**Hermes 변조 차단 매트릭스 cover**: 1/4 HIGH + 2/4 부분 + 1/4 0 (Gap-N #1 흡수)
**다음 진입 단계**: Q2/Q3 Reviewer-only 단축 합의 → Group C PoC 구현 → 본 PoC Reviewer-only 단축 합의
**격상 권한 0건**: ❌ ADR 본문 자동 갱신 / ❌ Implementation/Runtime PASS / ❌ Hermes PMO 격상 / ❌ G4 / G2 / G3 전체 PASS / ❌ Q2/Q3 본 합의 흡수
