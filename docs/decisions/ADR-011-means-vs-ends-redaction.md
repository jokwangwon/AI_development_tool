# ADR-011: Means-vs-Ends Redaction Principle (수단/목적 분리 원칙)

**상태**: 승인 (단축 합의 — Reviewer-only, 2026-05-06)
**날짜**: 2026-05-06
**의사결정자**: 사용자 + Reviewer 합의 — `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), `docs/architecture/system-identity-prequel.md` §3
**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)
**모법 역할**: R-4 / R-5 / R-6 / R-7 작업의 권위 근거

---

## 1. 맥락 (Context)

### 1.1 P2 v2 가정의 붕괴

ADR-008 부록 A는 R1 (학습루프 평문 누적)을 비협상 CRITICAL 위험으로 명시했다. P2 v2 §2.1.3은 R1 차단 메커니즘으로 "외부 pre-record hook" 형태를 가정 채택했다.

Phase 0 Day 1 사실 확인(`docs/phase0/day1-environment-and-fact-check.md`)에서 Hermes v0.12.0 main HEAD에 `pre_record` / `add_pre_record_hook` / `before_record` API가 존재하지 않음이 grep 0건으로 확정되었다 (15종 `VALID_HOOKS` 중 DB 기록 직전 가로채기 hook 0개).

### 1.2 Phase 0 R-1 / R-2 evidence

- **R-1 검증**(`docs/phase0/day2-r1-redaction-location-verification.md`): Hermes 자체 redaction(`agent/redact.py`)이 LLM 송신/도구 출력/로깅 전용이고 DB INSERT 경로 미적용 확정 → **G1a FAIL**.
  - `agent/redact.py:1-8` docstring 명시: "Regex-based secret redaction for logs and tool output"
  - redact 모듈 import 25개 모두 비-DB 경로
  - `hermes_state.py` (SessionDB) redact import 0건

- **R-2 PoC**(`docs/phase0/day3-r2-sqlite-trigger-poc.md`): SQLCipher BEFORE INSERT trigger + REGEXP UDF 조합이 Docker 격리 환경(network_mode: none + read_only + cap_drop ALL)에서 6항목 모두 PASS → **G1b PASS by R-2 PoC**.

### 1.3 ADR 권위 해석 요청 사항

위 결과는 다음 질문에 대한 ADR 권위 해석을 요구한다:

> **R1의 "비협상" 본질은 무엇인가 — 특정 구현 수단인가, 보안 결과인가?**

본 ADR은 이 질문에 답하고, 동시에 다음 3개 인접 안건을 ADR 권위로 정착한다:
- G1a/G1b 게이트 분리 공식화
- "Hermes ≠ root of trust" 권위 위계 영구화 (prequel §3 → ADR 승격)
- 자동 학습 vs 자동 정책 변경 분리

---

## 2. 결정 (Decision)

본 ADR은 다음 4가지를 권위로 선언한다.

### 2.1 수단/목적 분리 원칙 (Means-vs-Ends Separation)

**비협상 조건의 본질은 특정 구현 수단이 아니라, 달성해야 하는 안전 결과(safety outcome)이다.**

- 헌법 제8조 (보안)의 본질은 **DB 평문 저장 차단이라는 결과**이다.
- 외부 hook, redaction 호출, trigger, 암호화 등은 **수단**이다.
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:

  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |

**원칙 위반**: "수단이 비협상이다"는 텍스트 해석으로 본질 회귀를 차단하는 것은 본 ADR로 무효화된다. 동시에 (a)~(d) 4조건 미충족 시 수단 대체도 금지된다 — 본 ADR은 *수단 자유*가 아니라 *목적 달성 검증 의무*를 강제한다.

### 2.2 G1a / G1b 게이트 분리 공식화

P2 v2의 단일 G1 게이트는 본 ADR로 다음 두 게이트로 분해된다.

```
G1a: Hermes native redaction applies before DB INSERT
   Result: FAIL (R-1 확정)
   Evidence: agent/redact.py docstring "for logs and tool output",
             redact import 25개 모두 비-DB,
             hermes_state.py redact import 0건
   Status: 폐기 (이 경로로 헌법 8조 충족 시도 금지)

G1b: DB-level fallback prevents plaintext secret persistence
   Result: PASS by R-2 PoC
   Evidence: Docker 격리 환경 (network_mode: none + read_only + cap_drop ALL)
             + SQLCipher BEFORE INSERT trigger + REGEXP UDF
             + 6항목 자동 검증 (C1~C6 모두 PASS)
   Status: PoC PASS, 정식 충족은 R-3~R-5 완료 후
```

#### G1b 정식 충족 조건 (Phase 1 차단조건 #1 exit 기준)

| # | 조건 | 산출 |
|---|------|------|
| R-3 | 본 ADR-011 발행 + ADR-008 Amendment | `ADR-011`, `ADR-008` 부록 B |
| R-4 | Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 검증, gap 발견 시 trigger UDF 보충 | `docs/architecture/redaction-pattern-equivalence.md` |
| R-5 | canary 재검증 트리거 설계 (T13 강화 — config + 주기적 inject) | `docs/architecture/canary-recheck-design.md` |
| R-6 | CI/nightly 회귀 검증 (Hermes 업그레이드 자동 R-2 재실행) | `.github/workflows/r2-canary.yml` |
| R-7 | Phase 1 합격 SOP (canary 패턴/주입/검증/PASS·FAIL 기준) | `docs/phase0/redaction-verification-sop.md` |

R-3~R-7 모두 완료 시 G1b는 PoC 단계를 벗어나 Phase 1 차단조건 #1 정식 exit 기준이 된다.

### 2.3 Hermes ≠ Root of Trust

**Hermes는 시스템의 최종 신뢰 근거가 아니라 검증 대상이다.**

#### 권위 위계 (Authority Hierarchy)

```
Constitution
  > ADR
  > SDD
  > Harness Gates
  > Hermes
  > Worker Agents
```

#### 운영 함의 (Operational Implications)

1. **Hermes 출력은 Tools로 검증된다**: 린터/타입체커/테스트/trigger/canary가 Hermes 출력 위에 위치한다.
2. **Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음.
3. **DB INSERT 경로는 Hermes 외부에서 별도 보호**: SQLCipher trigger 기반 fallback (G1b).
4. **Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증**: 신뢰 경계 외부 변경의 자동 검출 (R-6).
5. **Hermes 학습 결과의 자동 정책 반영 금지**: §2.4와 결합.

#### prequel과의 관계

본 §2.3은 `docs/architecture/system-identity-prequel.md` §3 ("Hermes ≠ root of trust") 의 prequel(임시) 선언을 ADR 영구 권위로 승격한다. prequel은 R-7 완료 후 P2 v3로 흡수되며 폐기되지만, 본 ADR-011 §2.3은 영구 유지된다.

### 2.4 자동 학습과 자동 정책 변경 분리

- **자동 학습은 허용**: Worker Agent가 도구 사용/패턴/실패 사례를 누적 학습하는 것은 시스템 가치의 핵심.
- **자동 정책 변경은 금지**: Constitution / ADR / Harness Gates / Hermes 설정의 변경은 사용자 승인 경로(3+1 합의 또는 단축 합의)를 거쳐야 한다.

#### 3-tier 분류 (T1 / T2 / T3)

| Tier | 정의 | 예시 | 승인 경로 |
|------|------|------|---------|
| **T1** | 자동 허용 | Worker Agent 패턴 학습, 도구 사용 빈도 누적, 실패 회피 휴리스틱 | 자동 |
| **T2** | 사용자 승인 필수 | Skill/Memory promotion, 새 도구 등록, 합의 형태 결정 | 사용자 명시 결정 |
| **T3** | 자동 금지 (절대) | Constitution / ADR / Harness Gates 정의 자체의 변경 | 단축 또는 풀 3+1 합의 |

본 분리는 prequel §6의 3-tier 선언을 ADR 권위로 승격한 것이며, R-5 (canary 재검증) / R-6 (CI 회귀)의 권위 근거이기도 하다 — Hermes 내부 학습 또는 upstream 변경으로 redaction 동작이 silent 깨짐 발생 가능성을 자동 검증으로 차단.

---

## 3. R-4 ~ R-7 모법 역할 (Governing Precedent)

본 ADR은 다음 후속 작업의 권위 근거로 기능한다.

| 작업 | 산출 | 본 ADR §과의 관계 |
|------|------|----------------|
| **R-4** | `docs/architecture/redaction-pattern-equivalence.md` | §2.1 (a) — 대체 수단(R-2 trigger)이 기존 수단(Hermes redaction) 대비 패턴 커버리지 동등 이상임을 명시적 비교표로 실증 |
| **R-5** | `docs/architecture/canary-recheck-design.md` | §2.4 — Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현 |
| **R-6** | `.github/workflows/r2-canary.yml` | §2.1 (d) + §2.3 — Hermes 의존성 업그레이드의 자동 회귀 검증 |
| **R-7** | `docs/phase0/redaction-verification-sop.md` | §2.2 G1b 정식 충족 절차의 SOP화 |

후속 작업은 본 ADR §2를 명시 인용하고, 본 ADR 위반(예: "수단이 비협상이다" 텍스트 회귀, T3 자동 변경 시도) 시 단축 합의 + ADR Amendment 절차로만 갱신 가능하다.

---

## 4. 선택지 (Options Considered)

### 옵션 A: ADR-011 단독 (Amendment 없음)

- 장점: 일반 원칙 ADR 단일 산출 — 작성 부담 최소
- 단점: ADR-008 부록 A R1 표면 텍스트("외부 pre-record hook 공식 지원")가 갱신되지 않아 ADR-008 본문과 ADR-011 사이 표면 모순. 이력 추적 시 혼란.

### 옵션 B: ADR-008 Amendment 단독 (ADR-011 없음)

- 장점: ADR-008 한 문서로 일관
- 단점:
  - "수단/목적 분리"는 R1을 넘어선 일반 원칙 — Amendment에 일반 원칙을 담는 것은 Amendment 형식 위반
  - "Hermes ≠ root of trust" 운영 ADR화는 ADR-008 (Hermes 도입 결정) 범위 초과
  - R-4~R-7이 Amendment를 권위 근거로 인용하는 것은 비표준 (Amendment는 specific 갱신 한정)

### 옵션 C: ADR-011 신규 + ADR-008 Amendment ⭐ **채택**

- 장점:
  - 일반 원칙(수단/목적 분리, G1a/G1b 분리, Hermes ≠ root of trust, 학습/정책 분리)은 ADR-011로 권위화
  - ADR-008 부록 A R1 specific 갱신은 Amendment로 짧게 처리 + ADR-011 cross-reference
  - R-4~R-7이 ADR-011을 명확한 모법으로 인용
  - ADR-008 본문 read 시 즉시 R-1 FAIL 후 갱신 사항 파악 가능
- 단점: 작성 분량 2배 (수용)

---

## 5. 근거 (Rationale)

### 5.1 헌법 제8조 본질 재해석의 정당성

헌법 제8조의 비협상 본질은 "특정 hook이 존재해야 함"이 아니라 "비밀이 평문 영구 저장되지 않음"이다. R-2 PoC는 SQLCipher trigger 기반 fallback이 이 본질을 충족함을 실증했다.

수단을 비협상으로 굳히면, 수단이 부재한 시점(현 Hermes v0.12.0)에 헌법 제8조 자체를 충족할 수 없는 모순이 발생한다. 본 ADR은 이 모순을 수단/목적 분리로 해소하되, 동시에 (a)~(d) 4조건으로 자의적 수단 대체를 차단한다.

### 5.2 "Hermes ≠ root of trust" ADR 권위화 필요성

system-identity-prequel은 임시 선언(Pre-Declaration)으로, R-7 완료 후 P2 v3 흡수와 함께 폐기된다. 그러나 "Hermes ≠ root of trust"는 폐기되어서는 안 되는 영구 권위 원칙이다. 본 ADR-011 §2.3으로 권위 승격하여 prequel 폐기 후에도 보존한다.

### 5.3 G1a/G1b 분리의 영구화 필요성

R-1 FAIL과 R-2 PASS는 Phase 0 evidence 보고서에 기록되어 있으나, 이는 보고서이지 ADR 권위가 아니다. G1a/G1b 분리를 ADR로 권위화하지 않으면 미래 합의에서 "G1 단일 게이트로 회귀 가능" 해석 위험이 발생한다. 본 ADR §2.2가 이를 차단한다.

### 5.4 단축 합의(Reviewer-only)의 정당성

본 R-3은 새 설계 안건이 아니라 R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`) + 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`) 의 ADR 형식화 작업이다. 새 합의 검증이 아니므로 풀 3+1은 과잉. 직전 R-1 단축 합의 패턴 답습.

---

## 6. 합의 결과 (단축 합의 — Reviewer-only)

세부: `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md`

| 차원 | 판정 | 핵심 근거 |
|------|------|---------|
| 헌법 제8조 본질 충족 권위화 | **PASS** | §2.1 수단/목적 분리 + (a)~(d) 4조건 명시로 자의적 회귀·자의적 수단 대체 양방향 차단 |
| G1a/G1b 분리 공식화 | **PASS** | R-1 FAIL evidence + R-2 PASS evidence 모두 인용, 정식 충족 조건 명시 |
| Hermes ≠ root of trust 권위 승격 | **PASS** | prequel §3 → ADR §2.3 영구화, 운영 함의 5항목 명문화 |
| 자동 학습 vs 정책 변경 분리 | **PASS** | T1/T2/T3 3-tier 분류 본문 흡수, R-5/R-6 권위 근거화 |
| Provider Liquidity 영향 | **무관** | 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 |
| 메타 편향 통제 | **명시** | 본 ADR은 자체 코드 우호 결론(R-2 PASS)을 반영하나, (a)~(d) 4조건과 R-4~R-7 모법으로 회귀 견제 — 합의 보고서 §메타 편향 자기진단 참조 |

---

## 7. 결과 (Consequences)

### 7.1 긍정적

- 헌법 제8조 본질 충족이 specific 수단에 종속되지 않음 → 미래 Hermes API 변경 / upstream 변경 시에도 본질 보존 경로 확보
- G1a/G1b 분리로 R-2 PASS evidence가 P2 v3에 직접 흡수 가능
- "Hermes ≠ root of trust" ADR 권위화 → prequel 폐기 후에도 운영 원칙 영구 보존
- R-4~R-7이 권위 근거 명확화 → 후속 작업 의사결정 비용 감소
- 자동 학습/자동 정책 분리(T1/T2/T3)의 ADR 권위화 → silent 깨짐 자동 차단의 권위 근거

### 7.2 부정적

- ADR-008 부록 A R1의 표면 텍스트와 본 ADR §2.1 사이 텍스트 차이 존재 (Amendment로 동시 갱신하여 완화)
- "수단/목적 분리"가 일반화되어 미래 다른 비협상 조항 해석에도 적용 시 합의 비용 발생 가능 (대체 수단 검증 부담 — 의도된 비용)
- (a)~(d) 4조건 검증 부담은 본 ADR이 의도하는 안전 비용 — 회피 시도는 본 ADR 위반

### 7.3 주의사항

- 본 ADR의 (a)~(d) 4조건 미충족 시 수단 대체 불가 — "동등 이상의 보장" 검증을 PoC로 실증하지 않은 채 텍스트 해석만으로 수단 변경 금지
- §2.4 자동 정책 변경 금지(T3) 위반 감지 시 Layer 1~2 hook(설정 파일 변경 감지)에서 차단 — CI/nightly 강제 (R-6 범위)
- **본 ADR은 Hermes 안전성을 선언하지 않는다** — Hermes는 검증 대상이며, 본 ADR은 검증 외부화의 권위 근거이다.
- ADR-009 (자체 Adapter v2.0 entry) / ADR-010 (SQLCipher Vault) 도 미래 본 ADR §2.1 (a)~(d) 4조건 적용 대상이 될 수 있음 — 적용 시점은 별도 합의로 결정

---

## 8. 관련 문서 (2026-05-09 후속 9 cross-reference 갱신, 결정 내용 변경 0건 — 단축 합의 APPROVE Reviewer-only)

### 8.1 상위 권위
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
- `docs/architecture/system-identity-prequel.md` §3 (권위 위계 prequel — 본 ADR §2.3으로 영구 권위 승격, prequel §6의 3-tier 선언 → 본 ADR §2.4 영구 권위 승격) — **Archived 2026-05-09 후속 8**, 본 ADR §2.3 / §2.4 영구 권위 승격 직접 명시 답습으로 archive 후에도 권위 보존. archive 합의: `docs/review/3plus1-consensus-2026-05-09-system-identity-prequel-archive-decision.md`

### 8.2 갱신 대상 / 후속 권위
- `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (R-3 동시 발행, 2026-05-06)
- `docs/architecture/hermes-adoption-design.md` (P2 v2, **Archived 2026-05-09 후속 7** — 옵션 A 최소 침습)
- **`docs/architecture/hermes-adoption-design-v3.md`** (P2 v3, **Adopted — Design Adoption only, 2026-05-09 후속 6, 후속 권위**) — 본 ADR §2.1 (수단/목적 분리) / §2.2 (G1a/G1b 분리) / §2.3 (Hermes ≠ root of trust) / §2.4 (T1/T2/T3) 모두 답습 권위 발행. P2 v3 §10.1 Normative Constraints + §10.2 Archive Migration Note + §3 dual-structure + §6 G4 + §7 ADR 매트릭스 + §11 변경 절차 + §11.1 Hermes PMO 격상 전 인간 전문 리뷰 의무화

### 8.3 Phase 0 evidence
- `docs/phase0/day1-environment-and-fact-check.md` (Hermes v0.12.0 사실 확인)
- `docs/phase0/day2-r1-redaction-location-verification.md` (R-1 FAIL)
- `docs/phase0/day3-r2-sqlite-trigger-poc.md` (R-2 PASS)
- `docker/r2-poc/` (R-2 PoC Docker 격리 환경 + 6항목 자동 검증 스크립트)

### 8.4 합의 보고서
- `docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` (단축 합의 §R-3 권고)
- `docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` (풀 합의 권위 위계)
- `docs/review/3plus1-consensus-2026-05-06-adr-011-means-vs-ends.md` (본 ADR 단축 합의)

### 8.5 후속 작업 (R-4 ~ R-7 + 4 게이트 PASS + ADR 발행 + Archive 후속)

#### 8.5.1 R-4 ~ R-7 (모법 역할 — §3 답습)

- R-4: ✅ **완료** — `docs/architecture/redaction-pattern-equivalence.md` (Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 + gap 식별 + 보충 권고, ADR-011 §2.1 (a) 충족, 2026-05-06)
- R-4.1: ✅ **완료** — `docs/phase0/r4-1-trigger-extension-evidence.md` + `docker/r4-1-poc/` (Tier-1 42종 trigger UDF 확장 + Docker 격리 환경 PoC PASS, ADR-011 §2.1 (b) 충족, 2026-05-06)
- R-5: ✅ **완료** — `docs/architecture/canary-recheck-design.md` (canary 재검증 트리거 설계, T13 강화 + R-4.1 catalog 재사용 + 6 trigger 시점 + 4 verdict + 4 안전장치 + Markdown+JSONL evidence + T1/T2/T3 정책 매트릭스, 2026-05-06)
- R-6: ✅ **완료** — `.github/workflows/r2-canary.yml` (CI/nightly canary regression workflow, ADR-011 §2.1 (d) 자동 회귀 검증 경로, 2026-05-06) + R-6 GitHub Actions actual run `25482284523` PASS (24초, verdict=PASS, 42/42 BLOCK, leak 0, 2026-05-07)
- R-7: ✅ **완료** — `docs/phase0/redaction-verification-sop.md` (Phase 1 acceptance SOP, 13 항목 checklist + 4 verdict + 9 ROLLBACK + 7 Evidence + push 전/후 작업 분리, 2026-05-06) + R-7 SOP §7.3 단축 합의 APPROVE Reviewer-only (`docs/review/3plus1-consensus-2026-05-07-g1b-phase1-acceptance.md`, 2026-05-07) → **G1b CONDITIONALLY PASS → PASS 승격 + Phase 1 acceptance PARTIAL → PASS 선언**

#### 8.5.2 G1b PASS 이후 후속 작업 (2026-05-09 후속 1 ~ 후속 8 누적)

- ✅ **G2 / G3 / G4 정식 산출 + Design/Governance Gate PASS (Bundled, 2026-05-09 후속 1)** — 옵션 3 통합 풀 3+1 합의 + 외부 LLM 2건 (GPT cross-vendor + Claude 인접) APPROVE WITH CONDITIONS:
  - G2: `docs/architecture/governance-preconditions.md` (6 GP, P1~P8 + §1.2.6 P10) — GP-1 = G1b PASS evidence 흡수 (Implementation/Runtime PASS), GP-2~GP-6 = Design PASS / Implementation Pending
  - G3: `docs/architecture/hermes-not-root-of-trust-runtime.md` (Hermes 권한 22 항목, T1 8 / T2 2 / T3 12, Hermes 변조 차단 매트릭스 4항목) — 운영 구현 = Design PASS / Implementation Pending
  - G4: `docs/architecture/provider-agnostic-memory-skill-design.md` (Memory scope 4 + Skill schema 17 + JSONL 11 필드 + hash chain Layer 1~5 + Tier-based round-trip) — 라운드트립 + migration script = Design PASS / Implementation Pending
- ✅ **PR-1 본문 흡수 6건 (2026-05-09 후속 2)** — C-D / C-E / C-F / C-I / C-K / C-L 단축 합의 APPROVE Reviewer-only
- ✅ **PR-2 (ADR-012 + G4 §4 보강) 풀 3+1 + 외부 LLM 2건 APPROVE WITH CONDITIONS (2026-05-09 후속 3)** — `docs/decisions/ADR-012-evidence-ledger-protection.md` (Evidence Ledger Protection 신규 발행 — 12 보호 원칙 + 4 매트릭스 + 5 추가 의무 + 본 ADR §2.1 (a)~(d) + (e) 5조건 패턴 답습 + §2.3 Hermes ≠ root of trust 답습 (ADR-012 §2.12 변조 차단 매트릭스 4항목) + §2.4 T3 답습 (ADR-012 §원칙 9))
- ✅ **C-14 cross-vendor blind 의뢰 1+ 의무 충족 (2026-05-09 후속 4)** — cross-vendor 응답 2건 (vendor 미명시 + Gemini 사고모델) APPROVE WITH CONDITIONS
- ✅ **C-N ADR-009 갱신 단축 합의 APPROVE (2026-05-09 후속 4)** — `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` (P1 facade MVP 진입조건 + **Hermes PMO ↔ provider 분리 영구 권위 (§2.3)** + **Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1 (§5)** + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference)
- ✅ **G2 §1.2.6 P10 Evidence Forgery 정식 등록 단축 합의 APPROVE (2026-05-09 후속 5)** — Evidence Forgery 정식 위반 경로 등록 + ADR-012 §1.4 cross-reference + Hermes 변조 차단 매트릭스 4항목 + Layer 1~5 enforcement
- ✅ **P2 v3 정식 채택 풀 3+1 + 외부 LLM 2건 (cross-vendor — Gemini + vendor 미명시) APPROVE WITH CONDITIONS — Design Adoption only (2026-05-09 후속 6)** — DRAFT → Adopted, 8 본문 영역 갱신 (§0/§2/§3/§6/§7/§9/§10/§11). 본 ADR §2.1 / §2.2 / §2.3 / §2.4 모두 P2 v3 §10.1 Normative Constraints 답습 권위 발행
- ✅ **P2 v2 Archive 적격성 검토 + Archive 전환 단축 합의 APPROVE (2026-05-09 후속 7)** — 옵션 A 최소 침습. 본 ADR §1.1 (P2 v2 §2.1.3 가정 붕괴) cross-reference 영구 보존
- ✅ **system-identity-prequel.md Archive 적격성 검토 + Archive 전환 단축 합의 APPROVE (2026-05-09 후속 8)** — 옵션 A 최소 침습. 본 ADR §2.3 / §2.4 영구 권위 승격 직접 명시 답습 + AI Dev Company OS 정체성 직접 권위 출처 영구 보존
- ✅ **본 ADR-008 / 010 / 011 갱신 PR 묶음 *범위 결정* 단축 합의 APPROVE (2026-05-09 후속 9)** — 6 항목 분류 + 6/6 풀 3+1 승격 트리거 0건 발화 + 옵션 1 (3 ADR 단일 PR 묶음) 권고 + 25 cross-reference 갱신 항목 (A1~A25)

본 §8.5 의 모든 후속 작업은 본 ADR §2.1 (a)~(d) + 합의 APPROVE (e) 5조건 패턴 답습 (G2/G3/G4 정식 PASS + ADR-012 발행 + ADR-009 C-N + G2 §1.2.6 P10 + P2 v3 정식 채택 + Archive 모두) — 본 ADR 의 모법 역할 영구 보존.
