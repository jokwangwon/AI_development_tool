# 단축 3+1 합의 보고서 (Reviewer-only): ADR-011 수단/목적 분리 원칙 + ADR-008 Amendment

**날짜**: 2026-05-06
**검증 대상**:
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` (신규)
- `docs/decisions/ADR-008-hermes-adoption-decision.md` 부록 B Amendment (추가)
**상위 결정**:
- 단축 합의 §R-3 권고 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`)
- 풀 합의 §3 권위 위계 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md`)
**관련 evidence**:
- R-1 FAIL: `docs/phase0/day2-r1-redaction-location-verification.md`
- R-2 PASS: `docs/phase0/day3-r2-sqlite-trigger-poc.md`
**합의 형태**: 단축 (Reviewer-only) — 직전 R-1 단축 합의 패턴 답습
**사용자 명시 결정**: 옵션 C (ADR-011 신규 + ADR-008 Amendment), 단축 합의

---

## 1. 사전 점검 — 합의 가동 정당성

### 1.1 가동 사유

본 R-3은 새 설계 안건이 아니라, R-1 FAIL + R-2 PASS + 단축 합의 §R-3 (2026-05-05) + 풀 합의 §3 (2026-05-05) 의 ADR 형식화 작업이다. 다음 4가지 결론을 ADR 권위로 정착하는 것이 본 R-3의 본질:

1. 수단/목적 분리 원칙 (헌법 8조 본질 = "DB 평문 저장 차단" 결과)
2. G1a/G1b 게이트 분리 공식화
3. "Hermes ≠ root of trust" prequel 선언의 ADR 권위 승격
4. 자동 학습 vs 자동 정책 변경 분리 (T1/T2/T3)

### 1.2 단축 합의 채택 사유

- 본 안건은 사실 검증된 evidence(R-1/R-2) + 이미 완료된 합의(2026-05-05 단축/풀 합의) 의 ADR 형식화이며 새 설계 검증이 아님 → 풀 3+1 (병렬 3 에이전트) 과잉
- 직전 R-1 단축 합의 패턴 답습 (Reviewer 1인 + 메타 편향 자기진단)
- 사용자 명시 결정으로 단축 합의 형태 채택

### 1.3 Liquidity 영향

본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관 — Provider Liquidity 영향 **무관**. 반려 사유 없음.

### 1.4 ADR-009 / ADR-010 연동 영향

- ADR-009 (자체 Adapter v2.0 entry): 본 ADR §2.1 (a)~(d) 4조건 미래 적용 가능성 명시 (ADR-011 §7.3 주의사항). 즉시 영향 없음.
- ADR-010 (SQLCipher Vault HSM): R-2 PoC trigger와 통합 명시 권고 (CONTEXT.md 갱신 시 반영). 즉시 영향 없음.

---

## 2. Reviewer 평가 — 결론 및 차원별

### 2.1 결론

**APPROVE** — ADR-011 본문 + ADR-008 Amendment 모두 합의 가동 사유 4건을 ADR 권위로 정착하며, R-1/R-2 evidence 인용 정합. 메타 편향 통제 명시 + (a)~(d) 4조건과 R-4~R-7 모법 역할로 자체 코드 우호 결론 회귀 견제 — Reviewer 단독 누락 위험 0건.

### 2.2 차원별 평가

| # | 차원 | 판정 | 핵심 근거 |
|---|------|------|---------|
| 1 | **헌법 8조 본질 충족 권위화** | **PASS** | ADR-011 §2.1 — 본질을 "DB 평문 저장 차단 결과"로 명시, 수단 대체에 (a)~(d) 4조건 강제. 자의적 수단 회귀 차단 + 자의적 수단 대체 차단 양방향 견제. |
| 2 | **G1a/G1b 분리 공식화** | **PASS** | ADR-011 §2.2 — R-1 FAIL evidence(`agent/redact.py` docstring + import 25개 grep + `hermes_state.py` 0건) 인용, R-2 PASS evidence(Docker 격리 + 6항목 자동 검증) 인용, G1b 정식 충족 조건 5단계 명시. |
| 3 | **Hermes ≠ root of trust 권위 승격** | **PASS** | ADR-011 §2.3 — prequel §3 임시 선언을 ADR 영구 권위화, 운영 함의 5항목 명문화 (Tools 검증 / redaction 신뢰 범위 / DB 외부 보호 / 자동 R-2 회귀 / 학습 결과 자동 정책 반영 금지). |
| 4 | **자동 학습 vs 정책 변경 분리** | **PASS** | ADR-011 §2.4 — T1/T2/T3 3-tier 분류 본문 흡수. R-5 (canary 재검증) / R-6 (CI 회귀) 권위 근거화. silent 깨짐 자동 차단 정당화. |
| 5 | **R-4~R-7 모법 역할** | **PASS** | ADR-011 §3 — 4 작업 모두 ADR §2 항목 매핑 명시. 후속 작업이 본 ADR을 권위 근거로 인용 가능. |
| 6 | **ADR-008 Amendment 정합성** | **PASS** | 부록 B B.1~B.6 — R1 specific 갱신 + ADR-011 cross-ref + 오해 방지 (Hermes 안전 선언 아님) + 6 차단조건 #1 충족 메커니즘 갱신 표 + 정식 충족 5단계. ADR-011 §2와 일관, 일반 원칙 중복 없음. |
| 7 | **Provider Liquidity 영향** | **무관** | redaction 수단 해석. 모델/구독 교체 자유와 무관. 헌법 5조 위반 없음. |
| 8 | **누락 위험** | **0건** | 본 §3 |

---

## 3. 누락 위험 점검 (Reviewer 단독 발견)

### 3.1 점검 항목

| 항목 | 결과 |
|------|------|
| ADR-011이 미래 다른 비협상 조항(예: ADR-009 트리거 조건, ADR-010 키 관리)에 무리하게 일반화될 위험 | **차단됨** — §7.3 주의사항에 "별도 합의로 결정" 명시 |
| ADR-008 본문 §6 차단조건 #1 외 다른 차단조건(#2~#6) 표면 텍스트와 모순 위험 | **차단됨** — Amendment B.5 "차단조건 #2~#6은 변경 없음" 명시 |
| prequel §6 자동 학습 3-tier가 ADR-011 §2.4와 표현 차이 위험 | **검증 PASS** — prequel은 R-7 후 폐기되며 ADR-011 §2.4가 영구 권위. 표현 차이는 ADR 우선 |
| ADR-009 / ADR-010 갱신 PR 묶음(P2 v3 작성 시) 누락 위험 | **추적 항목** — CONTEXT.md "다음 세션 TODO" 7번 (P2 v3 + ADR-008/009/010 갱신 PR 묶음) 에 본 ADR-011도 포함되도록 갱신 권고 |
| R-4 패턴 동등성 검증 시 gap 발견되면 trigger UDF 보충 — UDF 보충이 §2.1 (a)~(d) 4조건 검증 필요 | **명시됨** — ADR-011 §2.2 G1b 정식 충족 조건 R-4 항목 + §3 R-4 매핑 §2.1 (a) |
| 본 단축 합의의 메타 편향 통제 부재 위험 | **차단됨** — 본 §4 메타 편향 자기진단 명시 |

### 3.2 결론

**Reviewer 단독 누락 위험 0건**. 다만 §3.1 4번 (ADR-009/010 갱신 PR 묶음)은 CONTEXT.md 갱신 시 ADR-011 포함을 명시 권고.

---

## 4. 메타 편향 자기진단 (자체 코드 우호 결론 견제)

### 4.1 본 평가의 자체 코드 우호 잠재 위험

본 ADR-011은 다음 의미에서 *자체 코드 친화* 결론을 권위화한다:

- R-2 PoC가 PASS 했다는 사실을 ADR §2.1 수단/목적 분리의 근거로 활용
- G1a FAIL을 폐기, G1b PASS를 채택 → 시스템 진행 경로 보존
- "Hermes ≠ root of trust" 선언이 미래 Hermes 신뢰 범위 확대 시도를 차단하지만, 동시에 *현재 시스템 구조 보존* 효과도 가짐 (자기 보존 편향 가능)

### 4.2 통제 수단

본 ADR이 자체 코드 우호 회귀로 흐르지 않도록 다음 4가지를 의식적으로 본문에 명시했다:

1. **(a)~(d) 4조건의 양방향 견제** — 자의적 수단 회귀("외부 hook 비협상") 차단 + 자의적 수단 대체("trigger 있으니 OK") 차단. R-2 PASS 자체로는 §2.1 충족이 아니라 (a) 동등 이상 보장이 별도 검증되어야 함을 §3 R-4 매핑으로 강제.
2. **§7.3 주의사항 — "본 ADR은 Hermes 안전성을 선언하지 않는다"** — Hermes 신뢰 범위 확대 시도를 본문에서 직접 차단.
3. **Hermes ≠ root of trust 운영 함의 5항목** — 단순 선언이 아니라 Tools 검증 / DB 외부 보호 / 자동 R-2 회귀 / 학습 결과 자동 정책 반영 금지 등 *외부 검증 의무*를 명시.
4. **자동 학습/자동 정책 변경 분리(T1/T2/T3)** — 본 ADR을 미래 자동 갱신/회귀할 수 없도록 T3로 분류. ADR 갱신은 단축 또는 풀 합의 거쳐야 함.

### 4.3 자체 진단 결과

- 자체 코드 우호 회귀 위험: **차단됨** (4가지 통제 수단 모두 본문에 명시)
- 자기 보존 편향: **잔여** — 현재 시스템 구조(Hermes 도입 + SQLCipher trigger fallback)를 보존하는 결론이지만, 이는 R-2 PASS evidence + 풀 합의 §3 권위 위계의 직접 결과이며 임의 해석이 아님. 잔여 편향은 R-4 (패턴 동등성) / R-6 (CI 회귀) 의 자동 검증으로 외부화.
- 본 ADR 자체의 자기 비판: **PASS** — 자체 코드 우호 결론을 권위화하면서도 동일 본문에 회귀 견제 4종을 강제한 형태로, 메타 편향 통제 정합.

---

## 5. 최종 합의

### 5.1 Reviewer 권고

**APPROVE — ADR-011 + ADR-008 Amendment 즉시 발행**.

### 5.2 메인 컨텍스트 권고 (단축 합의 메타 평가)

- Reviewer 평가 정합성: **HIGH** (메타 편향 통제 명시 + 차원별 8건 PASS + 누락 위험 점검 7항목 모두 차단/검증)
- 사용자 결정 입력: 본 합의 보고서 채택 → 즉시 다음 단계로 진입 가능

### 5.3 다음 단계 (사용자 명시 순서)

| # | 작업 | 산출 | 권위 근거 |
|---|------|------|---------|
| 1 | R-4 — Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교 | `docs/architecture/redaction-pattern-equivalence.md` | ADR-011 §2.1 (a) + §3 R-4 |
| 2 | R-5 — canary 재검증 트리거 설계 | `docs/architecture/canary-recheck-design.md` | ADR-011 §2.4 + §3 R-5 |
| 3 | R-6 — CI/nightly 회귀 검증 설계 | `.github/workflows/r2-canary.yml` | ADR-011 §2.1 (d) + §2.3 + §3 R-6 |
| 4 | R-7 — Phase 1 합격 SOP | `docs/phase0/redaction-verification-sop.md` | ADR-011 §2.2 + §3 R-7 |
| 5 | P2 v3 신규 작성 | `docs/architecture/hermes-adoption-design-v3.md` | R-3 ~ R-7 모두 완료 후 |
| 6 | ADR-008 / 009 / 010 갱신 PR 묶음 (P2 v3 와 동시) | 각 ADR 갱신 | P2 v3 작성 결과 반영 |

### 5.4 본 합의 보고서 발행 후 즉시 처리

- INDEX.md 업데이트 이력 추가
- CLAUDE.md §8 참조 테이블에 ADR-011 추가
- CONTEXT.md "다음 세션 TODO" 갱신 (R-3 → 완료, R-4 → 다음)

---

**합의 보고서 작성 시각**: 2026-05-06
**다음 진입점**: R-4 (Hermes redact pattern ↔ P1_REDACTOR 패턴 동등성 비교) — 사용자 결정 시 즉시 진입
