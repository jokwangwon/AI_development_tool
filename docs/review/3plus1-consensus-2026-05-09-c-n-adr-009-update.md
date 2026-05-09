# 단축 합의 보고서 — C-N: ADR-009 갱신 (P1 facade MVP 진입조건 + Hermes PMO ↔ provider 분리)

**합의 형태**: 단축 합의 (Reviewer-only) — *사용자 명시 결정 답습* (P1 결정 1: "C-N은 신규 ADR 발행이 아니라 기존 ADR-009 갱신이므로, 우선 Reviewer-only 단축 합의로 충분")
**합의 일자**: 2026-05-09 (후속 4 — C-N)
**검토 대상**: ADR-009 (`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`) C-N 갱신 5 영역
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only)**

---

## 0. 사전 점검

### 0.1 가동 사유

`SESSION_2026-05-09.md` §11.1 사용자 명시 결정 + PR-2 후속 (C-14 cross-vendor blind 의뢰 충족 후) 사용자 명시 결정 답습:

> "C-N은 신규 ADR 발행이 아니라 기존 ADR-009 갱신이므로, 우선 Reviewer-only 단축 합의로 충분하다고 봅니다. 단, 갱신 과정에서 ADR-009의 핵심 결정이 바뀌거나 자체 Adapter v2.0 조건이 완화되는 경우에는 풀 3+1로 승격해 주세요."

본 합의는 위 명시 결정 답습 → ADR-009 갱신 5 영역의 *핵심 결정 변경 0건* + *v2.0 트리거 (T1~T4) 변경 0건* 검증.

### 0.2 단축 채택 사유 (G3 §4.4.1 답습)

본 C-N 은 다음 G3 §4.4.1 단축 합의 충분 조건 모두 충족:

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (기존 ADR-009 갱신, ADR 신규 발행 0건) | ✅ |
| 직전 합의 (PR-2 풀 3+1 + 외부 LLM 2건) 패턴 답습 가능 | ✅ ADR-012 §원칙 5 (5-way) 답습 + ADR-011 §2.3 답습 |
| ADR-011 §2.4 분류 T2 (사용자 승인 기반) | ✅ 사용자 명시 결정 (단축 합의 채택) |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ 본 §0.1 답습 |
| **자체 Adapter v2.0 트리거 (T1~T4) 변경 0건** | ✅ §1.4 답습 |
| **핵심 결정 (옵션 B 채택) 변경 0건** | ✅ §1.4 답습 |

### 0.3 메타 편향 인지 (G3 §4.7 메타-순환 청산 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-009 C-N 갱신 작성자와 동일 컨텍스트. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘** (G3 §4.7.2 답습):
1. 사후 외부 LLM 충족 — C-N 자체는 외부 LLM *별도 회수 불필요* (C-14 cross-vendor blind 의뢰 2건 권위 *내부* 작업, P2 v3 정식 채택 합의 진입 *전* 작업 — Provider Liquidity 5-way 모법 ADR 권위 강화는 ADR-012 §원칙 5 발행 권위 *내부* 작업)
2. 격상 전 면제 — 본 C-N = Hermes PMO 격상 *전*, Hermes 자기참조 차단 §4 적용 대상 아님
3. 합의 권위 내부 변경 — 본 C-N = ADR-012 §원칙 5 발행 + PR-2 풀 3+1 합의 §11.2 P1 조건 (C-N 별도 PR) 답습 = *권위 내부* 작업
4. 자기 작성 한계 명시 의무 — 본 §0.3 + §3 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 합의 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 사람 리뷰 + 사용자 명시 결정 후 별도 |
| P2 v3 정식 채택 자동 선언 | ❌ 본 C-N 후 별도 합의 (풀 3+1, C-14 응답 답습) |
| ADR-008 / 010 / 011 / 012 본문 자동 갱신 | ❌ cross-reference 만 가능 (본문 변경은 별도 PR) |
| G2 §1.2 P10 정식 row 자동 추가 | ❌ 별도 G2 update PR (PR-2 합의 §4.2 답습) |
| ADR-013 / 014 후보 자동 발행 | ❌ 별도 합의 |
| P2 v2 / system-identity-prequel archive 자동 처리 | ❌ P2 v3 정식 채택 시점 |
| 실 runtime code / migration script / hook 구현 | ❌ Implementation/Runtime PASS 별도 |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ 별도 합의 |
| **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경** | ❌ 사용자 명시 답습 — 변경 시 풀 3+1 승격 의무 |
| **ADR-009 핵심 결정 (옵션 B 채택) 변경** | ❌ 사용자 명시 답습 — 변경 시 풀 3+1 승격 의무 |
| C-14 응답 7+4 조건 자체 흡수 | ❌ 본 C-N 범위 외 (P2 v3 정식 채택 합의 시점) — 추적은 CONTEXT/INDEX/SESSION 갱신으로 |

---

## 1. C-N 갱신 5 영역 점검 (5/5 PASS)

### 1.1 영역 ① — P1 Facade MVP 진입조건 명시 (§2 신설)

| 점검 항목 | 결과 |
|---------|------|
| MVP 진입 4 충족 조건 (a)~(d) 명시 | ✅ PASS — (a) ADR-008 + (b) P1 v2 + (c) LiteLLM Apache 2.0 + (d) Min 2 Active 모두 2026-05-04 이미 충족 답습 |
| MVP 진입 시점 = ADR-008 + P1 v2 합의 APPROVE 시점 (별도 트리거 없음) | ✅ PASS — *별도 트리거 없음* 명시 (자체 Adapter v2.0 트리거와 분리) |
| MVP 진입 의무 6 매커니즘 | ✅ PASS — facade.py 단일 진입점 + provider SDK 직접 import 금지 + 모델명 분기 코드 금지 + Min 2 Active + OAuth 직결 금지 + provider 추가 facade 변경만 |
| `llm-providers-design.md` §4 / §6 / §7 / §9 / §10 cross-reference | ✅ PASS — 5 § 모두 cross-reference 명시 |
| MVP 진입조건 = 별도 트리거 없음 (즉시 의무) 명료화 | ✅ PASS — §2.1 마지막 줄 명시 |

→ **영역 ① PASS** (P2 v3 정식 채택 합의 §1.6 참조 시 모호성 해소).

### 1.2 영역 ② — Hermes PMO ↔ Provider 분리 (§2.3 신설)

| 점검 항목 | 결과 |
|---------|------|
| 7 영역 권한 매트릭스 (LLM 호출 진입점 / Provider 라우팅 / 모델명 분기 / 표준화 / 비용 관측성 Redaction / OAuth refresh / Provider 추가 제거 교체) | ✅ PASS — 모든 영역 Hermes PMO = ❌, P1 Facade = ✅ |
| 4 영구 권위 근거 cross-reference (ADR-011 §2.3 + ADR-008 차단조건 #4 + ADR-012 §원칙 6 + 헌법 5조) | ✅ PASS |
| Hermes PMO 격상 (활성화) 시점 영구 유지 명시 | ✅ PASS — "본 ADR-009 §2.3 분리는 *Hermes PMO 격상 후에도 영구 유지*" 명시 |
| Hermes 가 provider SDK 직접 import 시도 = T3 위반 + Hermes-originated commit auto-reject (G3 §2.2 #20 답습) | ✅ PASS |
| Provider Liquidity (헌법 5조) 비협상 답습 | ✅ PASS |

→ **영역 ② PASS** (Hermes PMO 격상 후에도 provider 소유 시도 차단의 영구 권위).

### 1.3 영역 ③ — Provider Liquidity 5-way Multi-layer Defense 모법 ADR (§5 신설)

| 점검 항목 | 결과 |
|---------|------|
| Layer 1 ~ Layer 5 매트릭스 (책임 영역 / 모법 / 답습) | ✅ PASS — 5 Layer 모두 enumeration |
| Layer 1 모법 ADR = 본 ADR-009 명시 | ✅ PASS — §5 본문 + §5.1 |
| Layer 2 ~ Layer 5 cross-reference (G3 §6.4 / G4 §3.5 / G4 §4.3 / ADR-012 §2.1 원칙 6 + G4 §4.2) | ✅ PASS |
| 5 Layer 모두 충족 시 *완결성*, 1 Layer 만 깨져도 lock-in 위험 잔존 명시 | ✅ PASS |
| 자체 Adapter v2.0 진입 시 5 Layer 보존 의무 (ADR-011 §2.1 (a)~(e) 5조건 답습) | ✅ PASS — §5.1 명시 |

→ **영역 ③ PASS** (ADR-012 §원칙 5 가 발행한 "5-way" 명명의 Layer 1 모법 ADR 권위 확정).

### 1.4 영역 ④ — v2.0 트리거 vs P1 Facade MVP 조건 분리 (§3.0 신설)

| 점검 항목 | 결과 |
|---------|------|
| 분리 매트릭스 (개념 / 위치 / 진입 시점 / 트리거) | ✅ PASS — 두 개념 명료 분리 |
| **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경 0건** | ✅ PASS — §3.1 ~ §3.2 변경 0건 |
| **자동 NO-GO 절 (트리거 미충족 시) 본문 변경 0건** | ✅ PASS — §3.2 변경 0건 |
| **핵심 결정 (옵션 B 채택) 변경 0건** | ✅ PASS — §4 변경 0건 |
| MVP = "현재 운영 중", v2.0 = "백업 옵션, 트리거 충족 시 진입" 명료 | ✅ PASS |

→ **영역 ④ PASS** (단축 합의 적격 — 핵심 결정 변경 0건 + v2.0 트리거 변경 0건).

### 1.5 영역 ⑤ — P2 v3 정식 채택 합의 cross-reference (§9.4 신설)

| 점검 항목 | 결과 |
|---------|------|
| P2 v3 §1.6 (P1 과의 관계) cross-reference | ✅ PASS — 본 ADR §2 + §3.0 |
| P2 v3 §2.3 (Hermes 권위 위계) cross-reference | ✅ PASS — 본 ADR §2.3 |
| P2 v3 §6 (G4 — Provider-agnostic Memory/Skill) cross-reference | ✅ PASS — 본 ADR §5 |
| P2 v3 §10 (영구 핵심 제약 — Provider Liquidity) cross-reference | ✅ PASS — 본 ADR §5 + §8.3 |
| 본 cross-reference = P2 v3 *정식 채택 합의 시점* 인용 가능 (ADR-009 본문 변경 없이) | ✅ PASS |

→ **영역 ⑤ PASS** (P2 v3 정식 채택 합의에서 ADR-009 인용 가능, 모호성 해소).

---

## 2. 잔여 점검

### 2.1 본 갱신 후 자체 Adapter v2.0 진입 트리거 (T1~T4) 진행 상태

| 트리거 | 현 상태 (2026-05-09) | 모니터링 책임 |
|------|------|----|
| T1 (LiteLLM 신규 provider 미지원) | 미충족 (현 운영 중 provider 모두 LiteLLM 지원) | T1 trigger detection task (분기별, ADR-009 §3.1 답습) |
| T2 (LiteLLM 라이센스 변경) | 미충족 (Apache 2.0 유지) | T2 trigger detection task (실시간 모니터링, 라이센스 전환 즉시 알림) |
| T3 (LiteLLM 정상화 불가 결함) | 미충족 (CVE / 차단 버그 / 응답 정규화 결함 0건) | T3 trigger detection task (분기별 + LiteLLM CVE feed 모니터링) |
| T4 (LiteLLM 운영 부담 정량 역전) | 미충족 (분기별 측정 미시작) | T4 trigger detection task (분기별 시간 기록 측정 시작 의무 — Implementation 영역) |

**결론**: T1~T4 모두 미충족 → **자체 Adapter v2.0 진입 자동 NO-GO** (ADR-009 §3.2 답습).

### 2.2 본 갱신 후 P1 facade MVP 의무 활성화 상태

| 의무 (§2.2) | 현 활성화 상태 | 강제 매커니즘 활성 |
|----------|----------|----------|
| 1. LiteLLM 직접 import = `adapters/llm/facade.py` 한 파일 한정 | 활성 (의무) | depcruise 룰 + AST 스캐너 (Implementation 영역, 미작성) |
| 2. Provider SDK 직접 import 금지 | 활성 (의무) | depcruise 룰 + pre-commit hook (Implementation 영역, 미작성) |
| 3. 모델명 분기 코드 금지 | 활성 (의무) | depcruise 룰 + AST 스캐너 (Implementation 영역, 미작성) |
| 4. `Min 2 Active` provider 의무 | 활성 (의무) | 런타임 재검증 (Implementation 영역, 미작성) |
| 5. OAuth 직결 금지 | 활성 (의무) | OAuth refresh single-flight (Implementation 영역, 미작성) |
| 6. Provider 추가 시 facade 단일 진입점 | 활성 (의무) | config 기반 (Implementation 영역, `llm-providers.yaml` 미작성) |

**결론**: 6 의무 모두 *Design 차원 활성*, *Implementation 차원 PENDING* (G2 GP-5 IMPLEMENTATION PENDING 답습).

### 2.3 본 합의 후 다음 진입점

**G2 §1.2 P10 (Evidence Forgery) 정식 row 추가** (단축 합의, ADR-012 발행 트리거 답습) → **P2 v3 정식 채택 풀 3+1 합의** (C-14 응답 답습).

본 C-N 갱신 = P2 v3 정식 채택 합의 *진입 전 모호성 해소* 마지막 단계 → P2 v3 합의 즉시 진입 가능.

---

## 3. 메타 편향 자기진단

### 3.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-009 C-N 갱신 작성자와 동일 컨텍스트. 자기 작성 산출 자기 검토 한계 인지.

### 3.2 본 한계의 청산 (G3 §4.7 답습)

| # | 청산 원칙 | 본 C-N 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | C-14 cross-vendor blind 의뢰 2건 권위 *내부* 작업 (P2 v3 정식 채택 합의 진입 *전* 단계). 본 C-N 자체에 외부 LLM 별도 회수 *불필요* — 본 C-N 은 ADR-012 §원칙 5 발행 권위 + ADR-011 §2.3 권위 *답습* 한정 (새 권위 결정 0건) |
| 2 | 격상 전 면제 | 본 C-N = Hermes PMO 격상 *전* — Hermes 자기참조 차단 §4 적용 대상 아님 |
| 3 | 합의 권위 내부 변경 | 본 C-N = ADR-012 §원칙 5 (5-way) 발행 + PR-2 합의 §4.2 (C-N 별도 PR) 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §3 + §0.3 명시 |

### 3.3 5 통제 답습

| # | 통제 | 본 C-N |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 결정 (단축 합의 채택, 핵심 결정 변경 시 풀 3+1 승격 의무) 본 §0.1 + §0.4 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 5 영역 점검 + §2 잔여 점검 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ 본 ADR-009 §2.3 (Hermes provider 소유 = T3 영역) + §3.0 (자체 Adapter v2.0 진입 = T2 사용자 승인) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ 본 ADR-009 §5.1 (자체 Adapter v2.0 진입 = *수단 변경*, *목적 보존* — Provider Liquidity 비협상 5조건 답습) |
| 5 | 본 검토 *하지 않는* 것 명시 (§0.4) | ✅ 11건 명시 |

### 3.4 본 단축 합의가 *하지 않는* 것

- ❌ Hermes PMO 격상 자동 선언
- ❌ P2 v3 정식 채택 자동 선언
- ❌ ADR-008 / 010 / 011 / 012 본문 자동 갱신 (cross-reference 만 가능)
- ❌ G2 §1.2 P10 정식 row 자동 추가
- ❌ ADR-013 / 014 후보 자동 발행
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ **자체 Adapter v2.0 트리거 (T1~T4) 본문 변경** (사용자 명시 답습, 변경 시 풀 3+1 승격 의무)
- ❌ **ADR-009 핵심 결정 (옵션 B 채택) 변경** (변경 시 풀 3+1 승격 의무)
- ❌ C-14 응답 7+4 조건 자체 흡수 (P2 v3 정식 채택 합의 시점, 추적은 CONTEXT/INDEX/SESSION 갱신)
- ❌ T1~T4 trigger detection task 자동 구현 (Implementation 영역, 별도)
- ❌ depcruise 룰 / pre-commit hook / AST 스캐너 자동 구현 (G2 GP-5 IMPLEMENTATION PENDING 답습)

---

## 4. 결론

```
✅ APPROVE (단축 합의, Reviewer-only)
```

본 결론은 **ADR-009 C-N 갱신 5 영역** (P1 facade MVP 진입조건 명시 + Hermes PMO ↔ provider 분리 + Provider Liquidity 5-way 모법 ADR + v2.0 트리거 vs MVP 조건 분리 + P2 v3 cross-reference) 의 *권위 내부 변경 적격* + *단축 합의 적격* 한정.

### 4.1 본 합의가 *발생시키는* 것

- ✅ ADR-009 본문 갱신 (`docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md`) — 91 → 약 240 줄 (즉시 유효)
- ✅ P1 facade MVP 진입조건 ADR 권위화 (영구)
- ✅ Hermes PMO ↔ provider 분리 영구 권위화 (Hermes PMO 격상 후에도 영구 유지)
- ✅ Provider Liquidity 5-way Multi-layer Defense 모법 ADR (Layer 1) 권위 확정
- ✅ P2 v3 정식 채택 합의에서 ADR-009 인용 가능 (cross-reference 강화)
- ✅ P2 v3 정식 채택 합의 진입 적격 (모호성 해소 완료)

### 4.2 본 합의가 *발생시키지 않는* 것

§3.4 12건 + §0.4 11건 답습.

### 4.3 다음 진입점

> **G2 §1.2 P10 (Evidence Forgery) 정식 row 추가 단축 합의를 진행합니다 (ADR-012 발행 트리거 답습).** → **P2 v3 정식 채택 풀 3+1 합의** (C-14 응답 답습).

권고 시작 명령: 다음 작업 즉시 또는 사용자 명시 결정 시.

---

**합의 commit 권위**: 본 commit (`docs(review): record C-N ADR-009 update short consensus APPROVE`)
**본 commit + ADR-009 갱신 commit + housekeeping commits = 본 세션 후속 4 (C-N) 완료**
**다음 세션 진입점**: G2 §1.2 P10 정식 row 추가 단축 합의 → P2 v3 정식 채택 풀 3+1 합의
