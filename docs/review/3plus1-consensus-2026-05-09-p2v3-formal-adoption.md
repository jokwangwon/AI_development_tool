# 풀 3+1 합의 보고서 — P2 v3 (Hermes Adoption Design v3) DRAFT → 정식 채택

**합의 형태**: 풀 3+1 + 외부 LLM 2건 (cross-vendor — Gemini 사고모델 + vendor 자기 명시 부재) — 사용자 명시 결정 답습 (`SESSION_2026-05-09.md` §13.7 + §14.7)
**합의 일자**: 2026-05-09 (후속 6 — P2 v3 정식 채택)
**검토 대상**: P2 v3 (`docs/architecture/hermes-adoption-design-v3.md`, 12 섹션, 652 줄, **DRAFT 시점 2026-05-07**) → 정식 채택 (Adopted) 가능 여부
**판정**: ✅ **APPROVE WITH CONDITIONS — Design Adoption only 정식 채택 적격** (5/5 입력 일치)

---

## 0. 사전 점검

### 0.1 가동 사유

`SESSION_2026-05-09.md` §14.7 사용자 명시 결정 답습:

> "P2 v3 정식 채택 풀 3+1 합의를 진행해주세요 (C-14 응답 evidence 포함, C-14 11 조건 흡수 + ADR-012 + ADR-009 C-N + G2 P10 모두 반영)."

본 합의는 **P2 v3 DRAFT → 정식 채택 가능 여부** 단일 질문 답습. **Hermes PMO Activation / Runtime Implementation PASS / G2/G3/G4 Implementation PASS 결정 영역 외**.

### 0.2 풀 3+1 + 외부 LLM 2건 채택 사유

C-14 cross-vendor blind 의뢰 응답 2건 (vendor 미명시 §7.9 + Gemini §7.9) **모두 풀 3+1 합의 권고** + 본 합의 = *영구 권위 발행* (T3 변경 = ADR-011 §2.4 + ADR-012 §3.2 schema 진화 정책 답습 — 풀 3+1 + ADR Amendment 절차 의무).

| 충족 조건 | 본 P2 v3 충족 |
|---------|-----------|
| 풀 3+1 (T3 변경, 영구 권위 발행) | ✅ Agent A/B/C 병렬 분석 + Reviewer 종합 |
| 외부 LLM 1+ 충족 (G3 §4.4.2 답습) | ✅ **2건** — `2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response.md` (vendor 미명시) + `2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response-gemini.md` (Gemini 사고모델) |
| C-14 cross-vendor blind 의뢰 의무 (ADR-012 §11.2 + 외부 LLM 2 C-14) | ✅ 본 합의 시점 충족 (cross-vendor = Gemini + 1 추가 vendor) |
| 9 입력 모두 반영 (사용자 명시 답습) | ✅ §1.1 enumeration |
| 사용자 명시 결정 답습 | ✅ SESSION §14.7 + §13.7 |

### 0.3 메타 편향 인지 (G3 §4.7 + ADR-012 §11.1 메타-순환 청산 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = P2 v3 DRAFT 작성자 (2026-05-07 Part 2) + Agent A/B/C 작성자 + ADR-012 작성자 + ADR-009 C-N 작성자 + G2 §1.2.6 P10 작성자와 동일 패밀리. **5/5 입력 중 4/5 가 Claude 패밀리** (Agent A/B/C + Reviewer + Claude 인접 컨텍스트 응답 — 단 본 P2 v3 합의에서는 Claude 인접 컨텍스트 응답은 PR-2 의 입력이고 본 P2 v3 의 외부 LLM 2건은 *둘 다 cross-vendor* — Gemini + vendor 미명시 1건).

**청산 매커니즘** (G3 §4.7.2 답습):
1. **사후 외부 LLM 충족** — 본 합의 외부 LLM 2건 = cross-vendor blind 의뢰 (Gemini + vendor 미명시) — *진정한 비-Claude vendor* 1건 명시 (Gemini), 1건 추정 cross-vendor — Claude 패밀리 자기참조 통제 강도 ↑↑
2. **격상 전 면제** — 본 P2 v3 정식 채택 = Hermes PMO 격상 *전*. Hermes 자기참조 차단 §4 적용 대상 아님 (Hermes 가 본 합의 결정 주체 아님)
3. **합의 권위 내부 변경** — 본 합의 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 + ADR-012 발행 권위 + ADR-009 C-N 갱신 권위 + G2 §1.2.6 P10 정식 등록 권위 *내부* 작업
4. **자기 작성 한계 명시 의무** — 본 §0.3 + §10 메타 편향 자기진단

### 0.4 비검토 대상 (사용자 명시 답습 + 5/5 입력 일치)

| 항목 | 본 합의 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도 |
| Runtime Implementation PASS 선언 | ❌ Implementation/Runtime 영역 별도 합의 |
| G2 / G3 / G4 Implementation PASS 선언 | ❌ Implementation/Runtime 영역 별도 합의 (G1b 만 1/4 충족) |
| ADR-008 / 009 / 010 / 011 본문 자동 갱신 | ❌ cross-reference 만 가능 (본문 변경은 별도 PR) |
| ADR-013 / 014 후보 자동 발행 | ❌ 별도 합의 |
| **P2 v2 / system-identity-prequel.md archive 자동 처리** | ❌ **본 합의 *후* 별도 PR** (Agent C C-8 + 외부 LLM 1 §7.4 권고 답습) |
| 실 runtime code / migration script / hook 구현 | ❌ Implementation/Runtime PASS 별도 합의 |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ 별도 합의 |
| INDEX / CONTEXT 일괄 갱신 (본문 갱신 외) | ❌ 본 합의 commit 내 *해당 변경 영역만*, 일괄 갱신은 별도 PR |
| Hermes PMO 격상 적격성 검토 | ❌ 본 합의 범위 외 (별도 합의) |

---

## 1. 5 입력 종합 매트릭스

### 1.1 5 입력 enumeration

| # | 입력 | 모델 / 컨텍스트 | 산출 파일 | 판정 | 분량 |
|---|------|-------------|--------|------|------|
| 1 | **Agent A** (구현/운영) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md` | APPROVE WITH CONDITIONS (15 조건 = C-14 7 + C-14 4 + 운영 4 / **P0 4 HIGH binary**) | 580 줄 |
| 2 | **Agent B** (보안/거버넌스) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md` | APPROVE WITH CONDITIONS (12 CONDITIONS + 14 Gap, **HIGH 8건**, Gap-13 종합) | 861 줄 |
| 3 | **Agent C** (대안/단순화) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md` | APPROVE WITH CONDITIONS (8 조건, Alt-1 = 즉시 채택 + 본문 최소 갱신 + 후속 PR 분리) | 515 줄 |
| 4 | **외부 LLM (cross-vendor, vendor 미명시)** | 비-Claude vendor (likely GPT-5.x / 다른 cross-vendor) | `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response.md` | APPROVE WITH CONDITIONS (7 핵심 조건, 풀 3+1 권고) | (사용자 paste 원문) |
| 5 | **외부 LLM (Gemini 사고모델)** | Gemini (cross-vendor, vendor 자기 명시) | `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response-gemini.md` | APPROVE WITH CONDITIONS (4 핵심 조건, 풀 3+1 권고) | (사용자 paste 원문) |

**합산 = 5 입력 / 5 APPROVE WITH CONDITIONS / 5 Hermes PMO 격상 미선언 / 5 영구 핵심 제약 5건 보호 / 5 풀 3+1 합의 형태 권고**.

### 1.2 본 합의에 반영한 9 입력 (사용자 명시 답습)

1. **C-14 cross-vendor blind 응답 2건** — 입력 #4 + #5
2. **C-14 11 핵심 조건 체크리스트** — `docs/CONTEXT.md` "C-14 cross-vendor 응답 7+4 핵심 조건" §
3. **ADR-012 Evidence Ledger Protection** — `docs/decisions/ADR-012-evidence-ledger-protection.md` (PR-2 후속 3 발행)
4. **G4 §4.2 / §4.4 / §4.6 hash chain 보강** — PR-2 후속 3 보강
5. **ADR-009 C-N 갱신** — `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` (후속 4 갱신)
6. **G2 §1.2.6 P10 Evidence Forgery 정식 등록** — `docs/architecture/governance-preconditions.md` (후속 5)
7. **G1b PASS** — 2026-05-07 R-7 SOP §7.3 단축 합의
8. **G2 / G3 / G4 Design/Governance Gate PASS (Bundled)** — 2026-05-09 후속 1
9. **PR-1 / PR-2 / C-N / P10 흡수 완료 상태** — `docs/CONTEXT.md`

---

## 2. 5/5 일치 사항 (Consensus)

### 2.1 핵심 판정 5/5 일치

```
APPROVE WITH CONDITIONS — Design Adoption only 정식 채택 적격
```

5 입력 중 BLOCK / PARTIAL / 단순 APPROVE 0건. 모두 *조건부 승인*. **현 시점 (2026-05-09 후속 6) P2 v3 정식 채택 합의 진입 적격** 5/5 일치.

### 2.2 5/5 모두 일치한 결정 사항

| # | 사항 | 5 입력 출처 |
|---|------|---------|
| 1 | **P2 v3 정식 채택 = "Design Adoption only" 의미 제한** — Hermes PMO Activation / Runtime Implementation PASS / G2/G3/G4 Implementation PASS 모두 *별도 합의* | A 조건 2 + B C-1 + C C-2 + 외부 LLM 1 §7.10 조건 2 + Gemini §7.5 (Design Adoption ≠ Implementation Pending) |
| 2 | **풀 3+1 합의 형태 권고** (단축 합의 비권고) | A 조건 7 ✅ 충족 + B C-10 + C C-7 + 외부 LLM 1 §7.9 + Gemini §7.9 |
| 3 | **§3 4-게이트 진행 상태표 = 2026-05-09 동기화 의무** (DRAFT 시점 2026-05-07 vs 현 시점 차이 명시) | A R-1 HIGH + B Gap-4 HIGH + C C-1 + 외부 LLM 1 §7.2 + Gemini §7.2 |
| 4 | **§3 dual-structure 권고** (DRAFT Snapshot + Adoption-time Status + Delta + Implementation Pending 표) | A 조건 1 (P0 binary) + B C-3 HIGH + C C-1 + 외부 LLM 1 §7.5 + Gemini §7.10 #1 |
| 5 | **§7 ADR 매트릭스에 ADR-012 + ADR-009 C-N 추가 의무** | A 조건 4 (P0 binary) + B C-9 HIGH + C C-4 + 외부 LLM 1 §7.4 + Gemini §7.10 #2 |
| 6 | **§6 (G4) ADR-012 mandatory reference + G4 §4.2/§4.4/§4.6 보강 cross-reference 의무** | A R-3 HIGH + B C-7 HIGH + C C-4 + 외부 LLM 1 §7.4 + Gemini §7.10 #2 |
| 7 | **§2 Hermes PMO non-activation clause 강화 의무** (정식 채택 = PMO 활성화 신호 아님 명시) | A 조건 3 (P0 binary) + B C-1 HIGH + C C-3 + 외부 LLM 1 §7.3 + Gemini §7.8 (CLEAR) |
| 8 | **§10 영구 핵심 제약 archive 후 약화 방지 문구 강화 의무** | A 조건 5 (R-5) + B C-11 HIGH ENHANCEMENT REQUIRED + C C-5 + 외부 LLM 1 §7.7 + Gemini §7.10 #4 |
| 9 | **5 영구 핵심 제약 모두 보호** (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) | A §5 5/5 PASS + B §5 5/5 강도 HIGH 조건부 + C §5 5/5 충분 + 외부 LLM 1 §7.7 + Gemini §7.7 |
| 10 | **금지 사항 영구 답습** (Hermes PMO 격상 / Runtime PASS / archive 자동 / runtime code / Tier 자동) | A §6 + B §6 + C §6 + 외부 LLM 1 §1 + Gemini §10 |
| 11 | **Hermes ≠ root of trust 원칙 유지** (5 layer 보호 — ADR-011 §2.3 + ADR-012 §2.12 + ADR-009 C-N §2.3 + G3 §1.3/§5 + G3 §2.5 #11) | A §5 #2 + B §5.2 5/5 + C §5 #2 + 외부 LLM 1 §1.3 + Gemini §7.8 |
| 12 | **Provider Liquidity 5-way Multi-layer Defense 보존** (5 Layer 모두 ADR-009 C-N + ADR-012 영구 권위 layer) | A §5 #1 + B §5.1 5/5 + C §5 #1 + 외부 LLM 1 §1.5 + Gemini §1.4 |
| 13 | **자동 정책 변경 (T3) 유발 위험 0건** (본 P2 v3 정식 채택은 T3 변경이지만 *권위 내부 작업* + 사용자 명시 결정 답습) | A §5 #4 + B §5.4 5/5 + C §5 #4 + 외부 LLM 1 §7.10 + Gemini §7.10 |

### 2.3 5/5 모두 일치한 *추가 의무 영역* (조건부)

| # | 추가 의무 | 5 입력 출처 |
|---|--------|---------|
| N-1 | **Implementation Pending 표 명시 의무** (§3.4 신설 또는 §6 통합) | A 조건 6 + B C-3 + C C-1 + 외부 LLM 1 §7.5 + Gemini §7.5 |
| N-2 | **§11 또는 §2.6 격상 전 인간 리뷰 (Human-in-the-loop) 의무화 명문화** | A 조건 10 + B C-12 HIGH (Gemini 단독 강조) + C C-6 + 외부 LLM 1 §7.5 보완 + **Gemini §7.10 #3** (단독 강조) |
| N-3 | **본 합의 *후* archive (P2 v2 / system-identity-prequel) + ADR PR 묶음 + INDEX 일괄 갱신 = *별도 PR 분리*** | A R-7 + B (간접) + C C-8 + 외부 LLM 1 §7.4 + Gemini §1 |
| N-4 | **Adoption decision commit + Evidence Ledger entry (`event: external_llm_received` + `agent="user"` 강제)** | A R-11 ✅ + B C-10 + C C-7 + 외부 LLM 1 §7.9 + Gemini §7.9 |

---

## 3. 부분 일치 / 분기 사항 (Divergence — Reviewer 종합 결정 영역)

### 3.1 본 합의 *내부* 본문 갱신 분량 (Agent A/B vs Agent C 분기)

| 입력 | 권고 |
|-----|------|
| Agent A | 본 합의 *내부* P2 v3 본문 갱신 의무 — HIGH 위험 4건 (R-1 §3 dual-structure / R-2 §7 ADR-012 row / R-3 §6 ADR-012 mandatory reference / R-4 §2 non-activation clause) = **P0 binary 차단 조건**. 6.5일 본문 + 1일 부가 = 7.5일 |
| Agent B | 본 합의 *commit 전* 단일 PR 흡수 의무 — Gap-13 종합 = 6 영역 cross-reference 0건 (ADR-012 / G4 11 필드 / G4 hash chain / G4 round-trip / G2 P10 / ADR-009 C-N) MUST UPDATE. 12 CONDITIONS (HIGH 8건) |
| Agent C | 본 합의 *내부* = cross-ref + 상태 동기화 *최소 갱신* (Alt-5 단순화). archive / ADR 본문 / INDEX = *후속 별도 PR* |
| 외부 LLM 1 | "P2 v3 정식 채택 합의 내부에서 cross-reference 반영과 상태 갱신 정도로 제한" + "기존 ADR 본문 변경은 분리" |
| Gemini | "정식 채택 합의 내에서 갱신 가능" + ADR-008/009/010/011 본문 수정 = 별도 PR |

**Reviewer 종합**: **Agent A + Agent C + 외부 LLM 1 + Gemini 통합** — 본 합의 내부 = **P2 v3 본문 *7~8 영역* cross-ref + 상태 동기화 + non-activation clause + Archive Migration Note + 인간 리뷰 의무화 갱신**. archive (P2 v2 / system-identity-prequel) + ADR-008/010/011 본문 갱신 + INDEX 일괄 갱신 = **본 합의 *후* 별도 PR 분리** (사용자 결정 영역). 

→ Agent C 의 "Alt-5 단순화" 는 *본문 권위 명시 약화* 단점 인지하지만, Agent A/B 의 *dual-structure + cross-ref + non-activation clause* 영역은 *cross-ref + 상태 동기화* 와 동일 영역 (응답 1 §7.4 답습). **본 합의 내부 작업 = 7~8 영역 본문 갱신 (cross-ref + 상태 동기화 + 권위 강화)** 으로 결정.

### 3.2 §11 / §2.6 인간 리뷰 의무화 명문화 위치 (분기)

| 입력 | 권고 |
|-----|------|
| Agent A | §11 1 row 추가 + §2.6 단계 5.5 추가 (양쪽) |
| Agent B | §11 또는 §2.6 (택일) |
| Agent C | §11 row 추가 (단일) |
| 외부 LLM 1 | (간접 — §7.5 보완) |
| Gemini | "§11 변경 절차 또는 격상 절차(§2.6) 에 명문화" (택일 OR 양쪽) |

**Reviewer 종합**: Agent A 권고 답습 — **§11 1 row 추가 (변경 유형: "Hermes PMO 격상" → 절차: "풀 3+1 + 외부 LLM 2 또는 외부 LLM 1+사람 리뷰 + 인간 전문 리뷰 (Human-in-the-loop) 의무 + 사용자 명시 + Adoption decision commit") + §2.6 단계 5.5 추가 (인간 전문 리뷰 단계)**. 양쪽 답습 = 변경 절차 + 격상 절차 양 권위 모두 보호.

### 3.3 §10 형식 결정 (α 본문 유지 vs β Normative Constraints 격상)

| 입력 | 권고 |
|-----|------|
| Agent A | (직접 미평가, R-5 §10.1 Archive Migration Note 신설 권고) |
| Agent B | C-11 ENHANCEMENT REQUIRED — Normative Constraints 명시 격상 + 5-way 답습 + archive 후 보존 강화 문구 |
| Agent C | D-4 사용자 결정 영역 (α vs β) |
| 외부 LLM 1 | "P2 v3 §10에 \"Normative Constraints\"로 명시" + cross-reference + migration note 추가 |
| Gemini | "5대 제약을 §10에 단순 요약으로만 두면 약합니다" + 권장 문구 (영문) |

**Reviewer 종합**: **β 채택 (Normative Constraints 격상)** — 외부 LLM 1 + Gemini + Agent B 일치 권고 답습. 본 §10 본문 형식 = (i) Normative Constraints 명시 격상 + (ii) Provider Liquidity 5-way 답습 + (iii) archive 후 보존 강화 문구 + (iv) ADR-012 §9 5/5 HIGH 보호 매트릭스 cross-reference.

---

## 4. 단독 발견 (Gap — 1 Agent 단독)

### 4.1 Gemini §7.10 #3 — Hermes PMO 격상 전 인간 전문 리뷰 의무화 (단독 강조)

**Gemini 단독 강조** (다른 4 입력 간접 또는 미언급). 본 합의는 *Reviewer 종합* 시점에 **§11 + §2.6 양쪽 명문화 의무** 채택 (§3.2 답습) — Agent A 권고와 통합 흡수.

### 4.2 Agent A R-15 — §0.3 정식화 절차 시점 갱신 (단독)

**Agent A 단독 발견**: §0.3 정식화 절차 단계 4 시점 (2026-05-07 → 2026-05-09 후속 6) 갱신. 본 합의 commit 시점 갱신 — 본문 갱신 영역 흡수.

### 4.3 Agent A R-13 / R-14 — §1.4 R-2~R-7 표 + §9.2 옵션 갱신 (단독 LOW)

**Agent A 단독 발견** (LOW): §1.4 R-8~R-11 row 추가 + §9.2 옵션 갱신 (단축 합의 → 풀 3+1). 본 합의 commit 시점 동시 흡수.

### 4.4 Agent C Alt-5 — 본문 *최소* 갱신 (단순화 권고)

**Agent C 단독 권고**: 본 합의 내부 작업 = cross-ref + 상태 동기화 *한정*. Reviewer 종합 시 **부분 답습** — 본문 갱신 영역은 Agent A/B 권고 답습 (cross-ref + 상태 동기화 + non-activation clause + Archive Migration Note + 인간 리뷰), archive / ADR / INDEX 일괄 갱신은 후속 PR 분리 (Alt-5 답습).

---

## 5. 종합 판정 + P2 v3 본문 갱신 영역 결정

### 5.1 본 합의 판정

```
✅ APPROVE WITH CONDITIONS — Design Adoption only 정식 채택 적격
```

본 결론은 **P2 v3 (Hermes Adoption Design v3) DRAFT → 정식 채택 가능 여부** 의 *Design Adoption only* 한정 + *11 핵심 조건 (C-14 7+4) + Agent 보강 4 운영 조건 = 15 조건 흡수 후 정식 채택 적격*.

### 5.2 본 합의 *내부* 작업 영역 (P2 v3 본문 갱신 7~8 영역, 동일 PR commit)

5/5 입력 종합 결정 — 본 합의 commit 내부 P2 v3 본문 갱신 영역:

| # | 영역 | 갱신 내용 |
|---|----|----|
| **A1** | **§3 dual-structure** (P0 binary) | DRAFT Snapshot (2026-05-07) + Adoption-time Status (2026-05-09 이후) + Delta + Implementation Pending 표 |
| **A2** | **§7 ADR 매트릭스** (P0 binary) | ADR-012 + ADR-009 C-N 2 row 추가 |
| **A3** | **§6 (G4) ADR-012 mandatory reference** (P0 binary) | §6.2.3 / §6.2.4 / §6.4.2 / §6.6 / §6.7 cross-reference 추가 |
| **A4** | **§2 Hermes PMO non-activation clause 강화** (P0 binary) | §2 첫 문단 한국어 명시 + §2.6.1 PMO 격상 체크리스트 신설 + §2.5 ADR-009 C-N §2.3 cross-reference |
| **A5** | **§10 Normative Constraints 격상 + Archive Migration Note** | (i) Normative Constraints 명시 + (ii) Provider Liquidity 5-way 답습 + (iii) archive 약화 방지 문구 + (iv) ADR-012 §9 5/5 HIGH cross-reference |
| **A6** | **§11 + §2.6 인간 리뷰 의무화 명문화** | §11 1 row 추가 (Hermes PMO 격상 변경 절차) + §2.6 단계 5.5 추가 (인간 전문 리뷰) |
| **A7** | **§0.1 / §0.2 / §0.3 헤더 갱신** | "Design Adoption only" 의미 명시 + §0.3 정식화 절차 단계 4 시점 (2026-05-07 → 2026-05-09 후속 6) 갱신 + §0.2 *하지 않는* 것 답습 강화 |
| **A8** | **§1.4 / §9.2 / §1.3 보완 갱신** | §1.4 R-8~R-11 row 추가 (DRAFT 후속 evidence 반영) + §9.2 풀 3+1 권고 (옵션 갱신) + §1.3 차단조건 #1 충족 메커니즘 갱신 (현 G1b PASS evidence 답습) |

**합산 = 7~8 본문 갱신 영역**. 분량 추정 = ~350~400 줄 추가 (Agent A 6.5일 + 1일 운영 부담 추정 답습).

### 5.3 본 합의 *후* 별도 PR 분리 영역 (Agent C C-8 + 외부 LLM 1 §7.4 + Gemini 답습)

본 합의 commit 외 *후속 PR* 처리:

| # | 영역 | 처리 시점 / 합의 형태 |
|---|----|----|
| **B1** | **P2 v2 (`hermes-adoption-design.md`) archive 결정** | 별도 archive commit (사용자 명시 결정 영역, D-2 답습) |
| **B2** | **system-identity-prequel.md archive 결정** | 별도 archive commit (사용자 명시 결정 영역, D-2 답습) |
| **B3** | **ADR-008 본문 갱신** (cross-reference + Hermes PMO 격상 절차 추가) | 별도 PR (단축 또는 풀 3+1) |
| **B4** | **ADR-010 본문 갱신** (Evidence Ledger DB secret 처리 cross-reference) | 별도 PR (단축) |
| **B5** | **ADR-011 본문 갱신** (cross-reference 추가, §8.5 후속 작업 answer) | 별도 PR (단축) |
| **B6** | **G2 / G3 / G4 헤더 cross-reference 갱신** (P2 v3 정식 채택 → 본 v3 권위 발행 cross-reference) | 별도 PR (단축) 또는 본 합의 commit 내 |
| **B7** | **INDEX / CONTEXT 일괄 갱신** | 본 합의 commit 내 (해당 변경 영역만, B1~B6 영역은 *후속 PR* 시점) |

### 5.4 본 합의 *commit 묶음* 권고 (Agent A R-8 + 외부 LLM 1 §7.9 + Gemini 답습)

본 합의는 다음 commit 묶음으로 진행 권고:

```
[본 합의 commits — 권고]
1. docs(review): record P2 v3 formal adoption full 3+1 consensus + external LLM ×2 (cross-vendor + Gemini)
   - 합의 보고서 + Agent A/B/C 보고서 묶음
2. docs(p2v3): adopt P2 v3 — DRAFT → Adopted (8 본문 영역 갱신, Design Adoption only)
   - P2 v3 본문 갱신 (§0/§2/§3/§6/§7/§10/§11 + §1.4/§9.2/§1.3 보완)
3. docs(session): close 2026-05-09 후속 6 — P2 v3 formal adoption merged
4. docs(context+index): track P2 v3 formal adoption + 다음 진입점 (별도 PR)
```

### 5.5 본 합의 *후 별도 PR 우선순위* (사용자 결정 영역)

본 합의 머지 후 후속 PR 우선순위:

1. **P2 v2 / system-identity-prequel archive 결정** (사용자 명시 결정) — B1 + B2
2. **ADR-008 / 010 / 011 본문 갱신** (cross-reference + B3 ~ B5)
3. **G2 / G3 / G4 헤더 cross-reference 갱신** (B6, 단축 합의)
4. **ADR-013 / 014 후보 발행 결정** (별도 합의, Hermes PMO 격상 *전*)
5. **Hermes PMO 격상 적격성 검토** (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 사람 리뷰 + 사용자 명시 결정 후 별도)

---

## 6. PASS 조건 (본 합의 시점 충족 명시)

| 조건 | 충족 |
|-----|----|
| 풀 3+1 합의 (Agent A/B/C 병렬 분석 + Reviewer 종합) | ✅ |
| 외부 LLM 1+ 충족 (G3 §4.4.2) | ✅ 2건 (cross-vendor + Gemini 사고모델, 둘 다 비-Claude) |
| C-14 cross-vendor blind 의뢰 의무 (ADR-012 §11.2) | ✅ |
| 5/5 입력 APPROVE WITH CONDITIONS | ✅ |
| 5 영구 핵심 제약 보호 | ✅ |
| C-14 11 핵심 조건 흡수 매트릭스 | ✅ §5.2 답습 (A1~A8 본문 갱신 영역) |
| ADR-012 + ADR-009 C-N + G2 P10 + G4 §4 보강 모두 반영 | ✅ §5.2 답습 |
| 합의 보고서 commit | ✅ 본 commit |
| Adoption decision commit + Evidence Ledger entry (`event: external_llm_received` × 2) | ⏳ 본 합의 머지 시점 (Implementation 영역, 본 합의 commit 외) |

---

## 7. 영구 핵심 제약 5건 보호 점검

| # | 제약 | 권위 근거 | 본 P2 v3 정식 채택 보호 위치 | 강도 |
|---|------|--------|----------|------|
| 1 | **Provider Liquidity** | 헌법 5조 + ADR-008 차단조건 #2 + ADR-009 §5 (5-way Multi-layer Defense Layer 1 모법 ADR) + ADR-012 §원칙 5/6 | §10 (Normative Constraints) + §1.6 (P1 과의 관계, ADR-009 §5 답습) + §6 (G4 5-way) | **HIGH** (5/5) |
| 2 | **Hermes ≠ root of trust** | ADR-011 §2.3 영구 권위 + ADR-012 §2.12 (변조 차단 매트릭스 4항목) + ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) + G3 §1.3/§5 + G3 §2.5 #11 | §2.2 권위 위계 + §2.3 운영 함의 5항목 + §2.4 비활성 책임 + §10 + §5.2/§5.3 ADR-012 cross-reference | **HIGH** (5 layer) |
| 3 | **메타포 강제 금지** | system-identity-prequel §7 + 본 v3 §10 + §2.5 | §10 (Normative Constraints + archive 약화 방지) + §2.5 메타포 정합성 위해 구조 늘림 금지 | **HIGH** (조건부 — A5 흡수 후) |
| 4 | **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 + 본 v3 §0.2 #6 + §11 + ADR-012 §원칙 9 | §2.1.2 Hermes 가 *하지 않는* 것 6항목 + §10 + §11 변경 절차 (T3 = 풀 3+1 + ADR Amendment) + §2.6 격상 절차 7 단계 + §2.6.1 격상 체크리스트 | **HIGH** (5/5) |
| 5 | **수단/목적 분리** | ADR-011 §2.1 (a)~(d) + ADR-012 §4 (a)~(e) | §3.3 G1b / §4.3 G2 / §5.4 G3 / §6.4 G4 Exit 기준 (a)~(e) 5조건 답습 + §10 | **HIGH** (5/5) |

**5 영구 핵심 제약 = 5/5 HIGH 보호** (단 #3 메타포 강제 금지 = A5 §10 Archive Migration Note 흡수 후 HIGH).

---

## 8. 본 합의의 메타 편향 자기진단

### 8.1 본 Reviewer 의 한계

- 본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = P2 v3 DRAFT (2026-05-07) + Agent A/B/C 작성자 + ADR-012 + ADR-009 C-N + G2 §1.2.6 P10 작성자와 동일 패밀리
- Agent A/B/C 모두 Claude 패밀리 (3/5 입력)
- 외부 LLM 2건 (입력 #4 + #5) = 둘 다 cross-vendor (Gemini 명시 + vendor 미명시 1건, 추정 비-Claude vendor)
- **Claude 패밀리 = 3/5 / 비-Claude vendor = 2/5** — PR-2 합의 (Claude 패밀리 4/5 / 비-Claude 1/5) 대비 cross-vendor 비중 ↑↑

### 8.2 본 한계의 청산

| # | 청산 매커니즘 | 본 합의 적용 |
|---|----------|--------|
| 1 | 사후 외부 LLM 충족 (G3 §4.4.2) | ✅ 외부 LLM 2건 = 둘 다 cross-vendor (Gemini + vendor 미명시) — *진정한 비-Claude* 의견 PR-2 보다 강 |
| 2 | 격상 전 면제 (G3 §4.7.2 #2) | ✅ 본 P2 v3 정식 채택 = Hermes PMO 격상 *전* (Hermes 자기참조 차단 §4 적용 대상 아님) |
| 3 | 합의 권위 내부 변경 (G3 §4.7.2 #3) | ✅ 본 합의 = G2/G3/G4 정식 PASS §11.2 + ADR-012 + ADR-009 C-N + G2 P10 권위 *내부* 작업 |
| 4 | 자기 작성 한계 명시 (G3 §4.7.2 #4) | ✅ 본 §8 명시 |

### 8.3 5 통제 답습

| # | 통제 | 본 합의 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ SESSION §14.7 + 9 입력 + 4 검토 관점 + 7 금지 사항 + 7 후속 사항 모두 본 §0 + §5 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §6 PASS 조건 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §7 #4 (T3 영역) + §5.2 A4 (non-activation clause 영구) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §7 #5 ((a)~(e) 5조건) |
| 5 | 본 합의가 *하지 않는* 것 명시 (§0.4 + §5.2 *하지 않는* 영역) | ✅ 명시 |

### 8.4 Cross-vendor 추가 의무 (영구 답습)

본 P2 v3 정식 채택 = *Hermes PMO 격상 전 마지막 거버넌스 작업*. **Hermes PMO 격상 합의 시점**에 추가 cross-vendor (다른 비-Claude vendor — 예: GPT-5.x 또는 추가 Gemini 모델) 의무 (Gemini §7.10 #3 + 외부 LLM 1 §7.5 보완 권고 답습).

---

## 9. 다음 진입점

### 9.1 본 합의 후 즉시 작업 (본 합의 commit 의 일부)

1. **P2 v3 본문 갱신** — §5.2 A1~A8 8 본문 영역 (Design Adoption only 의미 제한)
2. **본 합의 보고서 + Agent A/B/C 보고서 + 외부 LLM 응답 2건 동일 PR commit** (Agent A R-8 답습 — cross-reference drift 차단)
3. **CONTEXT.md / INDEX.md / SESSION_2026-05-09.md 갱신** (P2 v3 정식 채택 commit 시점 본문 갱신만)

### 9.2 본 합의 *후* 별도 PR (사용자 결정 영역)

| # | 작업 | 합의 형태 |
|---|------|----|
| 1 | P2 v2 (`hermes-adoption-design.md`) archive | 별도 archive commit (D-2) |
| 2 | system-identity-prequel.md archive | 별도 archive commit (D-2) |
| 3 | ADR-008 본문 갱신 (cross-reference + Hermes PMO 격상 절차) | 별도 PR (단축 또는 풀 3+1) |
| 4 | ADR-010 본문 갱신 | 별도 PR (단축) |
| 5 | ADR-011 본문 갱신 (§8.5 후속 작업 answer) | 별도 PR (단축) |
| 6 | G2 / G3 / G4 헤더 P2 v3 정식 채택 cross-reference 갱신 | 별도 PR (단축) |
| 7 | ADR-013 / 014 후보 발행 결정 | 별도 합의 (Hermes PMO 격상 *전*) |
| 8 | Hermes PMO 격상 적격성 검토 (4 게이트 Implementation/Runtime PASS 후) | 별도 합의 (사용자 명시 결정 + 인간 전문 리뷰 + cross-vendor 추가) |

### 9.3 본 합의가 *발생시키지 않는* 것 (영구 답습)

§0.4 9건 답습. 본 합의 결과와 무관 영구 유지.

### 9.4 권고 시작 명령 (본 합의 후속)

> **"본 합의 §5.2 A1~A8 가이드 답습으로 P2 v3 본문 갱신 (DRAFT → Adopted, Design Adoption only) 진행해주세요."**

---

**합의 commit 권위**: 본 commit (`docs(review): record P2 v3 formal adoption full 3+1 consensus + external LLM ×2`)
**본 P2 v3 정식 채택 산출 합산** (commit 시점):
- `docs/review/3plus1-consensus-2026-05-09-p2v3-formal-adoption.md` (본 합의 보고서)
- `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-a-implementation.md` (580 줄)
- `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-b-security.md` (861 줄)
- `docs/review/agents-2026-05-09-p2v3-formal-adoption/agent-c-alternatives.md` (515 줄)
- `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-request.md` (외부 LLM 의뢰 자료)
- `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response.md` (cross-vendor, vendor 미명시)
- `docs/external-review/2026-05-09-c14-cross-vendor-p2v3-pre-adoption-response-gemini.md` (Gemini 사고모델)
- `docs/architecture/hermes-adoption-design-v3.md` (DRAFT → **Adopted**, 8 본문 영역 갱신, 본 합의 §5.2 답습)
- `docs/CONTEXT.md` / `docs/INDEX.md` / `docs/sessions/SESSION_2026-05-09.md` (housekeeping — 본 합의 commit 시점 본문 갱신만)

**판정**: ✅ **APPROVE WITH CONDITIONS — Design Adoption only 정식 채택 적격** (5/5 입력 일치)

**다음 단계**: §9.1 즉시 작업 (P2 v3 본문 갱신 8 영역 + 합의 commit 묶음 + 후속 별도 PR 분리)
