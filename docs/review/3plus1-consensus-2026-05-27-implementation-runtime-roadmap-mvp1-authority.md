# `implementation-runtime-roadmap-mvp1.md` DRAFT → APPROVED 권위 발효 합의 보고서 (Reviewer-only 단축 합의)

> **본 합의는 추론적 검증(권고) 한정이며 — 본 합의의 어떤 §도 그 자체로 (i) 실 runtime code / CI workflow / hook 구현 / 변경, (ii) Implementation Evidence PASS / Operational Readiness PASS 발효, (iii) ADR 본문 갱신, (iv) 수단 *결정*, (v) threshold *고정*, (vi) Tier-2/3 catalog 자동 확장, (vii) DRAFT → APPROVED *외* 다른 권위 변경, (viii) 후속 합의 본문 변경, (ix) ADR-011 §2.1 (a)~(e) 5조건 충족 *자동* 선언, (x) 1.5차 보강 / MVP-2 진입 자동 진입 — 어떤 행위도 자동 발생시키지 않는다. 본 합의 = `implementation-runtime-roadmap-mvp1.md` 권위 표시 격상 한정 (840줄 본문 변경 0건, line 826/827 상태 표시 격상 + 변경 이력 line 추가 한정).**

---

**작성일**: 2026-05-27
**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 + 5/5 풀 3+1 승격 트리거 0건 발화 검증 후 확정 (§1 답습)
**합의 입력**: `docs/architecture/implementation-runtime-roadmap-mvp1.md` (DRAFT 2026-05-12, 840줄) + `docs/phase0/mvp1-gp3-gp5-current-state-audit-brief.md` (2026-05-27)
**1차 권위 답습**: roadmap-mvp1 §3.6.3 / §4.7.3 line 287/477 합의 형태 권고 + audit brief 후속 3 합의 cross-check + ADR-011 §2.1 (a)~(e)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — `implementation-runtime-roadmap-mvp1.md` DRAFT → APPROVED 권위 발효 가능, 5/5 풀 3+1 승격 트리거 0건 발화**

---

## 0. 합의 대상 + 권위 한계

**대상**: `implementation-runtime-roadmap-mvp1.md` (DRAFT 2026-05-12, 840줄, §1~§9) → **APPROVED** 권위 발효 한정.

**본 합의가 *발생시키는 것***:
- 문서 line 826 `**작성일**: 2026-05-12 (DRAFT)` → `2026-05-12 (DRAFT) — 2026-05-27 APPROVED` 갱신
- line 827 `**상태**: DRAFT — Reviewer-only 단축 합의 진행 예정` → `**상태**: APPROVED (2026-05-27 Reviewer-only 단축 합의)` 갱신
- §9 변경 이력 line 1건 추가 (본 합의 답습)

**본 합의가 *발생시키지 않는 것*** (audit brief §6 + roadmap-mvp1 line 829~840 답습):
- ❌ 실 runtime code / CI workflow / hook 구현 / 변경
- ❌ Implementation Evidence PASS / Operational Readiness PASS 발효
- ❌ ADR 본문 갱신
- ❌ 수단 *결정* / threshold *고정* / Tier-2/3 자동 확장
- ❌ DRAFT → APPROVED 외 다른 권위 변경
- ❌ 후속 3 합의 본문 변경
- ❌ 본문 §1~§8 변경 (cross-reference 답습 한정)

---

## 1. 5/5 풀 3+1 승격 트리거 검증 결과

| # | trigger | 발화 | 근거 |
|---|---------|------|------|
| 1 | 새 권위 결정 (수단/threshold/ADR 갱신) | ❌ 미발화 | roadmap-mvp1 line 829~840 명시 금지. 본 합의 = 권위 표시 격상 한정 |
| 2 | Tier-2/3 catalog 자동 확장 | ❌ 미발화 | line 287/477 "Tier-2/3 자동 확장 0건" 명시 + audit brief §3.2 deferred |
| 3 | Implementation Evidence PASS 자동 선언 | ❌ 미발화 | audit brief §4 "현재 PASS 발효 미적격, 1.5차 보강 cycle 필요" + line 292/483 별도 합의 |
| 4 | 후속 합의 본문 변경 | ❌ 미발화 | 후속 3 합의 (gp3/gp5/backlog6) 본문 = 변경 없이 흡수 완료 (line 819~821) |
| 5 | ADR-011 §2.1 (a)~(e) 5조건 충족 *자동* 선언 | ❌ 미발화 | audit brief §4 "(e) conditions 미해소 = 1.5차 보강 cycle 필요" — 자동 충족 선언 0 |

→ **5/5 미발화** = 단축 합의 (Reviewer-only) 적격.

---

## 2. 본 문서 권위 발효 적격성 평가

**(a) 후속 3 합의 흡수 완료**: ✅
- line 821 = gp3 합의 흡수 (§3.1.2 G3-7 row, C-1 흡수)
- line 820 = gp5 합의 흡수 (§5.4 통합 위험 매트릭스, C-4 흡수)
- line 819 = backlog #6 합의 흡수 (§5.5 9 sub-수단 본문 채택, commit `f40423f` push 완료)

**(b) audit brief 정합성**: ✅
- audit brief §2.1 (21 도구) + §2.2 (11 workflow) = roadmap §5.5 본문 채택 영역과 정합
- audit brief §3.1 = DRAFT 잔재 = line 826 만 잔재 (본문 권위 사실상 합의됨)
- audit brief §3.2 deferred 영역 = roadmap §3.6.3 / §4.7.3 권고 매트릭스와 정합

**(c) ADR-011 §2.1 (a)~(e) 답습 정확성**: ✅
- audit brief §4 매트릭스 = 양 GP 5/5 답습 (단 conditions 미해소 = deferred)
- roadmap §3.6.2 + §4.7.2 = ADR-011 5조건 본문 답습 일치

---

## 3. cross-check verbatim

| line | verbatim | 평가 |
|------|---------|------|
| 826 | `**작성일**: 2026-05-12 (DRAFT)` | DRAFT 상태 확인 ✅ (본 합의 대상) |
| 287 | `본 문서 (GP-3 MVP-1 roadmap deepening) 자체 \| **Reviewer-only 단축 합의** \| ... 17 항목 우선순위 답습 + 새 권위 결정 0건` | Reviewer-only 단축 합의 형태 권고 ✅ |
| 477 | `본 문서 (GP-5 MVP-1 roadmap deepening) 자체 \| **Reviewer-only 단축 합의** \| ... 17 항목 우선순위 답습 + 새 권위 결정 0건` | 양 GP 동일 권고 ✅ |
| §5.5 (630~714) | 9 sub-수단 본문 채택 매트릭스 (GP-3 4 + GP-5 3 = 7 unique + 2 일관성) + 18 Rollback Trigger + §5.5.5 범위 한계 | ✅ |
| §8 (795~811) | 6 다음 진입점 + 5 시작 명령 — 본 합의 = (a) "Reviewer-only 단축 합의 보고서 작성" 진입 | ✅ |

→ 5/5 verbatim 확인 완료, 모순 0건.

---

## 4. deferred 영역 명시 (본 합의 *영역 외*)

audit brief §3.2 + roadmap §3.6.3 / §4.7.3 답습:
- ❌ S-3 detect-secrets 부분 통합 (1.5차 보강) — 풀 3+1 + 외부 LLM 1+
- ❌ ST-2 inotify sidecar (1.5차 보강) — 풀 3+1
- ❌ PC-1 pre-commit framework 의무화 (T3) — 풀 3+1 + 사용자 명시
- ❌ AR-3 통합 PR auto-reject (T3) — 풀 3+1 + 외부 LLM 1+
- ❌ ST-1 / ST-2 / ST-5 (Hermes upstream) — 풀 3+1 + Hermes upstream PR
- ❌ ST-4 (Vault HSM) — ADR-010 §X 진입 합의 + 외부 LLM 1+
- ❌ T-1 / T-3 / T-4 / T-5 단독 진입 — 풀 3+1
- ❌ URL / 모델 Tier-2/3 vendor 추가 — 풀 3+1
- ❌ `src/adapters/llm/facade.py` placeholder → real 본문 — TR-1 자동 풀 3+1 trigger (별도 trajectory)
- ❌ Implementation Evidence PASS 발효 — 별도 합의 + ADR-011 5/5 evidence + conditions 해소 + 사용자 명시

---

## 5. 판정

**판정: APPROVE (단축 합의 — Reviewer-only)**

**근거**: 5/5 풀 3+1 승격 trigger 미발화 + 후속 3 합의 본문 흡수 완료 + audit brief §3.1 권위 잔재 정합 + ADR-011 §2.1 (a)~(e) 답습 정확. roadmap-mvp1 line 287/477 명시한 합의 형태 권고 답습.

**발효 효과**: `implementation-runtime-roadmap-mvp1.md` DRAFT → **APPROVED** 권위 발효 (840줄 본문 변경 0건, line 826/827 상태 표시 격상 + §9 변경 이력 1줄 추가 한정).

**발효되지 않는 영역**: 실 runtime code / CI / hook 변경 0건 / Implementation Evidence PASS / Operational Readiness PASS / ADR 본문 갱신 / 수단 결정 / threshold 고정 / Tier-2/3 자동 확장 / DRAFT 외 권위 변경 — 모두 별도 합의 + 사용자 명시 결정 의무 영역.

---

## 6. 다음 단계 (사용자 결정 영역)

audit brief §5 4 진입점 권고 답습:
- (a) ✅ **본 합의로 발효** — DRAFT → APPROVED
- (b) MVP-1 1.5차 보강 합의 — 풀 3+1 + 외부 LLM 1+ (S-3 / ST-2 / PC-1 / AR-3 중 1 이상)
- (c) MVP-1 Implementation Evidence PASS 발효 합의 — (a)+(b) 선행 후
- (d) `facade.py` placeholder → real 본문 — TR-1 자동 풀 3+1 trigger (별도 trajectory)

권고 순서: (a) → (b) → (c). (d) 는 다른 trajectory.
