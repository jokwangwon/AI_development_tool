# Jarvis MVP-1 (g1-N-3) CLAUDE.md / roadmap.md 정합 정정 자격 평가 cycle entry brief (v1.1, APPROVE w/ COND + (i) 최소 정정 채택 적용 완료)

> **본 brief v1.1 = (g1-N-3) cycle 풀 3+1 합의 (`386c552`, APPROVE w/ COND, BLOCKING 12 + Reviewer 단독 격상 4 R-S1~R-S4 + 권고 16 + NOTE 10 신규, 기각 0) verbatim 본문 직접 반영 + (i) 최소 정정 채택 (Reviewer R-rec-15 권고) 적용 완료.** v1 = `19b0f76` (522줄). v1.1 = 본 commit (BLOCKING 12 verbatim + R-S1~R-S4 verbatim + framing 통일 + (i) 최소 정정 적용 + 단일 atomic commit). 본 brief 의 어떤 §도 **헌법 본문 자동 정정·ADR-011 본문 자동 정정·MVP-1 합의 본문 자동 정정·메모리 자동 정정·Provider Liquidity 본질 약화·결합 cycle 자동 진입·자동 채택·자동 기각·부분 정정 (4 양방향)** 을 발생시키지 않는다. **단 본 commit 시점에 CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 발효 직접 적용 완료 (Reviewer 권한 한계 (9) 신규 예외 자격 발효 — R-13 (4-c) 동형 패턴 답습)**. staged: (g1-N-2) commit `3bdb1be` → 세션 7-8차 통합 정리 `3f84c26` → 본 (g1-N-3) brief v1 `19b0f76` → 합의 `386c552` → **본 v1.1 + CLAUDE.md/roadmap.md (i) 최소 정정 단일 atomic commit (현재)** → 세션 정리.

**작성일**: 2026-05-24 (8 cycle entry 통합 정리 `3f84c26` 후속, 9번째 cycle entry)
**카테고리**: 합의 cycle entry brief v1.1 ((g1-N-3) CLAUDE.md / roadmap.md 정합 정정, **9번째 cycle entry**, R-19 답습 단계 (4) 직접 적용 = brief v1.1 + CLAUDE.md/roadmap.md 본문 변경 단일 atomic commit)
**범위 (사용자 명시 — entry 시점 답습)**:
- **(β) CLAUDE.md + roadmap.md** ((g1-A) 합의 §7.1 (g1-N-3) 옵션 본문 표기 직역) — 좁은 범위, 16 영향 문서 별도 cycle 분리
- **정공법** (단계 (1)~(6) 풀 답습)
- **(g1-N-3') 본 cycle 내 통합 *평가*** (식별 only, *해결* 자격은 별도 cycle — R-9 헌법급 변경 답습 영구 의무)
- **(i) 최소 정정** (단계 (4) 채택 명시) — Reviewer R-rec-15 권고 답습

**합의 답습** (R-22 의무):
- **본 (g1-N-3) cycle 합의** (`386c552`) BLOCKING 12 + Reviewer 단독 격상 4 (R-S1 §2.3 ↔ §4.1 내부 모순 / R-S2 CLAUDE.md grep 0 matches 정량 / R-S3 3-way trade-off carry-over / R-S4 pamsd 19 위치 헌법-동급 권위) + 권고 16 + NOTE 10 신규
- (g1-N-2) 합의 BLOCKING 10 + Reviewer 단독 격상 3 (R-S1 line 245 entire verbatim / R-S2 헌법 line 80 ↔ ADR-011 line 6 임시 stale / R-S3 "비협상" boundary)
- (g1-N-1) 합의 BLOCKING 14 + Reviewer 단독 격상 4
- (g1-N) 합의 BLOCKING 22 + Reviewer 단독 격상 5
- (g1-A) 합의 BLOCKING 16 + Reviewer 단독 격상 3
- format 합의 BLOCKING 16 + Reviewer 단독 격상 3
- Provider Liquidity 합의 BLOCKING 13
- R-9 헌법급 변경 답습 영구 의무 7 항목 본 cycle *간접* 적용
- **Reviewer 권한 한계 9 항목 영구 답습 + (9) 신규 CLAUDE.md / roadmap.md 본문 정정 자격 boundary + (9-a)~(9-d) sub-boundary 답습 충족**

**선행 답습**:
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction.md` (`386c552`, 423줄, **R-S1~R-S4 답습 영구 + (i) 최소 정정 R-rec-15 권고**)
- `docs/phase0/jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction-consensus-entry-brief.md` v1 (`19b0f76`, 522줄)
- `docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md` v1.1 (`3bdb1be`, 519줄, **R-S1~R-S3 답습 영구**)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` **현재 line 6 + line 245** (본 cycle 변경 0건 영역, R-S1 verbatim 답습)
- `docs/constitution/PROJECT_CONSTITUTION.md` 현재 line 75~80 (5조-2 신설 본문) + **line 80 임시 stale (R-S2 + R-S3 carry-over 영구)** + line 104~105
- `CLAUDE.md` 본 commit 후 line 244 ADR-011 entry (i) 최소 정정 적용
- `docs/architecture/implementation-runtime-roadmap.md` 본 commit 후 line 64 + line 65 (i) 최소 정정 적용
- 메모리: `feedback_provider_liquidity` line 7 + line 12~17 / `feedback_staged_consensus_workflow` / `project_jarvis_local_boss_direction`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것 (12 항목, §10.1 와 1:1 매핑 — R-15 = R-S3 + R-S5 답습 영구)

> **🔴 §0 ↔ §10.1 1:1 매핑 *의미적 한계* 인정** (R-12 = R-S5 답습 명문 한계): §0 = *행위 명세* / §10.1 = *차단 명세* 비대칭 매핑 형식. *수치* 동일 (12 = 12) self-consistency 만 의무, *의미적 1:1 매핑* 의무 0 — 동일 영역의 *행위 차원* + *차단 차원* 짝.

1. (g1-A) §7.1 (g1-N-3) + (g1-N-2) §12.2 #5 carry-over 답습 (§1)
2. **CLAUDE.md 본문 현재 헌법 5조-2 신설 사실 미반영 + grep 0 matches 정량 evidence 식별** (§2.3, R-S2 격상 답습 영구)
3. **roadmap.md 본문 현재 "Provider Liquidity" 인용 광범위 stale 식별** (§2.4) — line 64/65/111/114/137/142/146/147 (8 위치, line 61~63 GP-2~4 정정 0건 자격)
4. **R-9 헌법급 변경 답습 영구 의무 7 항목** 본 cycle *하위 layer 정합 정정* 차원 *간접* 적용 (§1.4 + 분해 매핑 표 신설 — R-1 BLOCKING 답습)
5. **Reviewer 권한 한계 8 → 9 항목 격상 영구 답습 + (9) 신규** CLAUDE.md / roadmap.md 본문 정정 자격 boundary + (9-a)~(9-d) sub-boundary (§6.3, R-7 답습) + (9-d) 차단 메커니즘 본문 명문 (R-9 BLOCKING 답습)
6. SDD 정합성 매트릭스 — 본 commit 후 CLAUDE.md line 244 + roadmap.md line 64/65 정정 결과 명문 (§3)
7. CLAUDE.md / roadmap.md 정정 *본문 후보* 매트릭스 (§4) — **(i) 최소 정정 채택 결과 명문** (Reviewer R-rec-15 권고 답습) + (ii)~(iii) carry-over by-reference only
8. 핵심 긴장 **4축** 분석 (§5) — (1) 하위 layer 정합 boundary / (2) (g1-N-3') 통합 *평가* vs *해결* 분리 / (3) 16 영향 문서 self-citation anchor 차단 / (4) Reviewer 권한 한계 (9) 신규 boundary
9. 3+1 합의 분담안 + Reviewer 권한 한계 9 항목 영구 답습 + (9) 신규 발효 + (9-a)~(9-d) sub-boundary 명문 (§6)
10. 합의 출력 형식 + raw line-level cross-check 의무 (§7) — 본 cycle 합의 보고서 `386c552` carry-over
11. 후속 결정 권고 옵션 매트릭스 (§8) — **(g1-N-3-pamsd) 신규 분리 HIGH + (g1-N-3-hermes) HIGH 격상** (R-7 + R-8 BLOCKING 답습) + (g1-N-3') HIGH + MEMORY.md cleanup HIGH (depth 4 cycle 누적)
12. 정직성 한계 (§9) 22 항목 + 차단 조건 (§10) 12 항목 1:1 매핑 + NOTE carry-over (§11) **90 by-reference** (80 carry-over + 본 cycle 신규 N-91~N-100) + §12 변경 일람 표 본문 신설 (R-S5 답습)

### 하지 않는 것 (12 항목, §10.1 와 1:1 매핑 — R-15 = R-S3 + R-S5 답습 영구)

1. ❌ **CLAUDE.md *다른 부분* 자동 정정** — 본 commit (i) 최소 정정 = line 244 entry 만, §1 SDD / §7 의존 표 / §8 line 233 변경 0건 (Reviewer 권한 한계 (9-b) 답습)
2. ❌ **roadmap.md *다른 위치* 자동 정정** — 본 commit (i) 최소 정정 = line 64/65 만, line 111/114/137/142/146/147 변경 0건 (별도 cycle 의무, (9-b) 답습)
3. ❌ **헌법 본문 자동 정정** — (g1-N-1) `148fbbe` 결과 유지, **헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무** (R-S2 + R-S3 carry-over 영구)
4. ❌ **ADR-011 본문 자동 정정** — (g1-N-2) `3bdb1be` 결과 유지, **ADR-011 line 212 = (g1-O) 별도 cycle 의무** carry-over
5. ❌ **MVP-1 합의 본문 자동 정정** — by-reference carry-over only
6. ❌ **메모리 본문 자동 정정** — line 7 + line 12~17 by-reference 답습. **MEMORY.md 9.4% over R-S4 carry-over depth 4 cycle 누적** (R-7 cleanup 우선순위 HIGH 격상 carry-over)
7. ❌ **ADR-008 본문 자동 정정** — 부록 B by-reference only
8. ❌ **16 영향 문서 자동 정정** — (β) 범위 boundary 영구. **provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 = (g1-N-3-pamsd) 신규 분리 HIGH carry-over** (R-S4 격상)
9. ❌ **Provider Liquidity 본질 약화** — binary 본질 유지. 본 commit (i) 최소 정정 = 5조-2 reference 추가 + 비협상 boundary 영구 답습 *강화*
10. ❌ **본 brief framing 영구 정착** (R-12 답습) — (i)~(iv) 후보 + 4 긴장 framing 본 cycle 임시 framing 명문, *영구화* risk 차단
11. ❌ **본 brief 진단표 → 후속 cycle 정정 진입 근거화 *de facto* 압력** (R-29 답습 + R-S5 답습 — §3·§4·§5·§8 모두) + **anchor depth limit cycle 9-cycle entry 도달 *비추론* 차단** (R-10 BLOCKING 답습)
12. ❌ **본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 4 양방향 자격** 모두 0건 (R-30 + R-24 + R-7 + R-10 *대칭* 답습) + **framing "8 → 9 격상" vs "9 항목 영구 답습" 통일 의무** (R-11 BLOCKING 답습)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — 사용자 명시 "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 통합 평가 + "(i) 최소 정정" 채택 + R-19 단계 (4) 직접 진입

- (g1-A) 합의 §7.1 (g1-N-3) 옵션 + (g1-N-2) 합의 §12.2 #5 carry-over 직접 발효
- 사용자 명시 (2026-05-24, 새 세션 시작): "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 본 cycle 내 통합 *평가*
- 사용자 명시 (단계 (3) 합의 후): **"(i) 최소 정정 (Reviewer R-rec-15 권고)"** 채택 + 단계 (4) 진입
- R-19 답습 trigger 정확한 form 4 단계 직접 적용 — 본 cycle 은 *하위 layer 정합 정정* cycle 차원 (R-9 헌법급 변경 *간접* 적용)

### 1.2 본 cycle 의 핵심 결과 (R-19 답습 단계 (4) 직접 적용 완료)

| 변경 대상 | 본 cycle 결과 |
|---|---|
| **CLAUDE.md line 244** | "헌법 8조 본질" → "**헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질**" (i) 최소 정정 **변경 완료** ✅ |
| **roadmap.md line 64** (GP-5) | "Provider Liquidity 5-way Layer 1 모법" → "**헌법 5조-2 Provider Liquidity 5-way Layer 1 모법**" (i) 최소 정정 **변경 완료** ✅ |
| **roadmap.md line 65** (GP-6) | "Provider Liquidity Layer 4 — Provider 교체 자유" → "**헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유**" (i) 최소 정정 **변경 완료** ✅ |
| CLAUDE.md *다른 부분* (§1/§7/§8 line 233) | 변경 0건 ((i) 최소 정정 채택 결과, (ii)/(iii) = carry-over by-reference only) |
| roadmap.md *다른 위치* (line 111/114/137/142/146/147) | 변경 0건 ((i) 최소 정정 채택 결과, 별도 cycle 의무 carry-over) |
| 헌법 본문 | 변경 0건 ((g1-N-1) 유지, line 80 임시 stale = (g1-N-3') 별도 cycle) |
| ADR-011 본문 | 변경 0건 ((g1-N-2) 유지, line 212 = (g1-O) 별도 cycle) |
| 16 영향 문서 | 변경 0건 ((β) 범위 boundary, 별도 cycle 의무) |
| 본 brief | v1 (`19b0f76`, 522줄) → 합의 (`386c552`, 423줄) → **본 v1.1 (현재, ~700줄, BLOCKING 12 verbatim + R-S1~R-S4 verbatim + (i) 채택 + framing 통일)** |

### 1.3 R-19 답습 trigger 정확한 form 4 단계 완료 chain ((g1-N-3) cycle)

| 단계 | 산출 | commit |
|---|---|---|
| (1) 사용자 명시 + 범위 선택 | "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 통합 평가 | (사용자 메시지) ✅ |
| (2) entry brief v1 | brief v1 522줄 | `19b0f76` ✅ |
| (3) 풀 3+1 합의 | 합의 보고서 423줄, APPROVE w/ COND, BLOCKING 12 + R-S1~R-S4 + 권고 16 + NOTE 10 | `386c552` ✅ |
| **(4) brief v1.1 + CLAUDE.md/roadmap.md (i) 최소 정정 단일 atomic commit** | **본 v1.1 (현재) + CLAUDE.md line 244 + roadmap.md line 64/65 본문 변경 (현재 완료)** | **본 commit (현재)** |

### 1.4 R-9 답습 영구 의무 7 항목 본 cycle 직접 적용 완료 + R-S1~R-S4 본 cycle 신규 격상

| 항목 | 본 cycle 적용 결과 |
|---|---|
| **(1) 사용자 명시** | "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 통합 평가 + (i) 최소 정정 채택 ✅ |
| **(2) 풀 3+1 합의** | 본 cycle 합의 `386c552` APPROVE w/ COND, BLOCKING 12 + R-S1~R-S4. **본 cycle = *하위 layer 정합 정정* 차원, R-9 (2) 헌법급 변경 합의 의무의 *간접 확장 답습*** (R-9 (2) 직접 모법 = 헌법 본문 변경, 본 cycle = 헌법 본문 변경 결과 *반영* 의 하위 의존 정합) ✅ |
| **(3) Reviewer 권한 한계 9 항목 영구 답습** | §6.3 + **(9) 신규 — CLAUDE.md / roadmap.md 본문 정정 자격 직접 적용 완료** (R-7 + R-13 (4-c) 동형 패턴 답습) + (9-a)~(9-d) sub-boundary 명문 ✅ |
| **(4) ADR-011 §2.1 (a)~(e) 답습 자격 평가** | (e) 후속 패턴 *직접 충족* — 본 commit BLOCKING 12 verbatim 본문 직접 반영 100% (R-21 답습). (a)~(d) 적용 자격 = *간접 적용* (R-9 (4) 직접 모법 = 헌법 본문 변경 시) |
| **(5) ADR-008 부록 B Amendment 패턴 (R-S3 답습 영구 — 형식 유사성)** | **본 cycle = (g1-N-1)/(g1-N-2) 의 하위 의존 정합 정정**, ADR-008 부록 B Amendment 동시 발행 형식 모법 *간접 적용* (ADR-011 line 7 "동시 발행" = 최초 발행 시점 한정, R-18 답습) ✅ |
| **(6) 자동 amendment 발의 0건** | 본 cycle 합의 채택 + 사용자 명시 후 brief v1.1 + CLAUDE.md + roadmap.md 단일 atomic commit (자동 발효 0건) ✅ |
| **(7) 본 cycle = *하위 의존 정합 정정 cycle*** | **R-19 답습 trigger 정확한 form 단계 (4) 직접 적용 완료** ✅ — (g1-N-1) `148fbbe` + (g1-N-2) `3bdb1be` 결과 *반영* cycle |

### 1.4.1 §1.4 R-9 7 항목 ↔ §6.3 Reviewer 권한 한계 9 항목 *분해 매핑 표 본문* (R-1 BLOCKING 답습 — 4-way 일치 격상)

> **🔴 R-1 4-way 일치 (A-B1 + B-B3 + B-S2 + C-B3)** — *분해 매핑 표* 본문 신설 의무.

| §1.4 R-9 항목 | §6.3 Reviewer 권한 한계 (9 항목) | 분해 매핑 |
|---|---|---|
| (1) 사용자 명시 | — | trigger 직접 적용 (외부 입력) |
| (2) 풀 3+1 합의 | (7) 자동 다음 단계 진입 자격 0 + (8) 결합 cycle 진입 자격 평가 자격 0 | 합의 절차 boundary 분해 2 항목 |
| (3) Reviewer 권한 한계 8 → 9 영구 답습 | (1)~(9) 9 항목 전체 | 1 → 9 분해 매핑 (수치 비대칭 정상) |
| (4) ADR-011 §2.1 (a)~(e) 답습 | (1) ADR-011 §6 본문 정정 (g1-N-2) 발효 완료 | 모법 ADR 권위 1 항목 |
| (5) ADR-008 부록 B Amendment 패턴 | — | 형식 모법 *간접 적용* (본 cycle 형식 모법 발효 0) |
| (6) 자동 amendment 발의 0건 | (7) 자동 다음 단계 진입 자격 0 | 동의어 답습 |
| (7) 하위 의존 정합 정정 cycle | (9) CLAUDE.md/roadmap.md 본문 정정 (R-13 (4-c) 답습) | 본 cycle 차원 명문 |
| — | (2)~(6) 본질·MVP-1·헌법·메모리·framing 정착 자격 0 | 본 cycle *간접 적용* 외 영역 boundary |

**§1.4 ↔ §6.3 통합 매핑 어휘 + 표 본문** (R-1 BLOCKING 답습): R-9 (3) Reviewer 권한 한계 1 항목 = §6.3 9 항목의 *상세 분해* 형식 통합 매핑. 수치 비대칭 (7 ≠ 9) = *분해 매핑* 형식 답습 영구.

### 1.5 framing 통일 명문 (R-11 BLOCKING 답습 — R-12 framing 영구 정착 자격 0)

> **🔴 R-11 답습**: "**8 → 9 격상**" = 본 (g1-N-3) cycle *임시* framing (entry 시점 표현). 본 cycle 합의 채택 후 = **"9 항목 영구 답습 (본 cycle 직전 까지 8 항목, 본 cycle 발효 후 9 항목)"**. (9) 신규 = 본 cycle 한정 신규, 후속 cycle 에서는 *영구 9 항목* 으로 흡수. framing 자체 *영구 정착* 자격 0 — 후속 cycle ((g1-N-3') 등) 에서 추가 (10) 격상 자격 = 사용자 명시 + 별도 합의 단독 발효 (R-7 + R-13 답습).

---

## 2. evidence 통합

### 2.1 본 cycle 합의 (`386c552`) 결과 (R-22 답습)

| 산출 | 본 v1.1 답습 |
|---|---|
| BLOCKING 12 (R-1~R-12) | brief v1.1 verbatim 본문 직접 반영 100% (본 문서) — R-21 답습 |
| Reviewer 단독 격상 4 (R-S1·R-S2·R-S3·R-S4) | brief v1.1 verbatim 본문 직접 반영 100% (본 문서) — R-S1 답습 영구 |
| 권고 16 (R-rec-1~R-rec-16) | brief v1.1 본문 직접 반영 또는 §11 NOTE carry-over |
| NOTE 10 신규 (N-91~N-100) + 80 carry-over = **90 by-reference only** | brief v1.1 §11 신설 (R-26 답습) |
| 기각 0 | 4 양방향 자동 발효 0건 |
| 3 Agent 정렬 — 정면 충돌 0건 + 4-way 일치 BLOCKING 1 (R-1) + 2+ 일치 (R-10·R-11) | 분담 결과 자연 수렴 evidence (헌법 4조 #3 정상 작동) |

### 2.2 헌법 5조-2 신설 line 75~80 verbatim (R-1 + R-S1 답습 영구)

```
line 75   ## 제5조-2: Provider Liquidity 원칙 (비협상)
line 76   
line 77   1. 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다 — 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 코드 변경 없이 가능해야 한다 (메모리 line 7 답습)
line 78   2. LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만 — 모델명·provider 분기 코드는 금지 (메모리 line 12 답습)
line 79   3. 단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙 (메모리 line 14 답습)
line 80   4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**
```

**🔴 line 80 임시 stale 신규 발효 (R-S3 carry-over 영구 — 3-way trade-off 답습)** — line 80 verbatim 인용 "헌법 제5조 (Provider Liquidity)" ≠ ADR-011 line 6 현재 본문 verbatim "헌법 제5조-2 (Provider Liquidity, 비협상)". **본 (g1-N-3) cycle 정정 자격 0** (R-9 헌법 본문 변경 답습 영구 의무, (g1-N-3') 별도 cycle 의무).

### 2.3 CLAUDE.md 본문 현재 stale 식별 + (i) 최소 정정 적용 결과 (R-3 + R-5 + R-S1 + R-S2 답습 영구)

> **🔴 R-S1 격상 답습 영구 (A-S2 → R-S1)**: brief v1 §2.3 line 143~146 라벨 ↔ §4.1 line 246~249 (i)~(iv) 매트릭스 정의 *내부 모순*. (i) 최소 정정 = §4.1 정의 = §8 line 244 ADR-011 entry **만**. §2.3 line 143~145 모두 "(i) 명시 추가/의존 항목/강조 entry" 라벨 = §4.1 정의 위반. R-1 답습 영구 의무 — 본 라벨 정정 후 후속 cycle 자동 답습 시 모순 전파 차단.

> **🔴 R-S2 격상 답습 영구 (A-S1 → R-S2)**: CLAUDE.md 본문 전체 (251줄) `grep -nE "(Provider Liquidity|5조-2|제5조-2|헌법 제5조|헌법 5조)" CLAUDE.md` 결과 = **0 matches** 정량 evidence. (g1-N-1) commit `148fbbe` 헌법 5조-2 신설 사실의 CLAUDE.md 본문 *전무 반영* 정량 직격. **본 commit (i) 최소 정정 후** = line 244 entry 1 위치에 reference 추가, 나머지 250줄 *미반영 유지* ((9-b) 답습 — 별도 cycle 의무).

**현재 line-level cross-check + (i) 최소 정정 적용 결과** (본 commit 시점):

| CLAUDE.md 위치 | 본 commit 전 본문 (stale) | (i) 최소 정정 후 본문 | 본 cycle 변경 자격 |
|---|---|---|---|
| §1 SDD 답습 의무 | 변경 0건 (5조-2 명시 부재) | 변경 0건 ((i) 최소 정정 범위 외) | **(iii) 최대 정정 명시 추가 후보** (R-3 R-S1 격상 라벨 정정 답습) — 별도 cycle |
| §7 문서 의존 관계 표 (line 219~228 부근) | 헌법 5조-2 신설 → 의존 항목 추가 미반영 | 변경 0건 ((i) 최소 정정 범위 외) | **(ii) 중간 정정 의존 항목 추가 후보** (R-3 R-S1 격상 라벨 정정 답습) — 별도 cycle |
| §8 참조 문서 표 line 233 | 헌법 본문 line 참조 미포함 (조 번호 인용만) | 변경 0건 ((i) 최소 정정 범위 외) | **(iii) 최대 정정 강조 entry 추가 후보** (R-3 R-S1 격상 라벨 정정 답습) — 별도 cycle |
| **§8 참조 문서 표 line 244 ADR-011 entry** | "**수단/목적 분리 원칙** \| `docs/decisions/ADR-011-means-vs-ends-redaction.md` \| **헌법 8조 본질 = 안전 결과. R-4~R-7 모법, Hermes ≠ root of trust, 자동 학습 vs 자동 정책 변경 분리(T1/T2/T3)**" | **"**수단/목적 분리 원칙** \| `docs/decisions/ADR-011-means-vs-ends-redaction.md` \| **헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질 = 안전 결과 + Provider Liquidity. R-4~R-7 모법, Hermes ≠ root of trust, 자동 학습 vs 자동 정책 변경 분리(T1/T2/T3). 상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)**"** ✅ | **(i) 최소 정정 적용 완료** (line 244 보강) |
| 기타 본문 | 5조-2 reference 부재 | 변경 0건 ((i)/(iv) 범위 외) | **(iv) 광범위 정정 후보 (사용자 명시 (β) 범위 boundary 위반 risk)** — 별도 cycle 의무 |

### 2.4 roadmap.md 본문 현재 stale 식별 + (i) 최소 정정 적용 결과 (R-1 + R-rec-1 답습)

**현재 본 commit 시점 cross-check** (라벨 정정 + (i) 적용 결과):

| roadmap.md 위치 | 본 commit 전 본문 (stale) | (i) 최소 정정 후 본문 | 본 cycle 변경 자격 |
|---|---|---|---|
| **line 61** | "**G2** \| **GP-2 Egress Redaction** ... (P2 헌법 8조 위반 경로)" | 변경 0건 | 8조 only — **5조-2 reference 추가 *불필요* (Provider Liquidity 직접 무관, R-1 답습 분류 기준 정정 0건 자격)** |
| **line 62** | "**GP-3 Credential / Secret Hygiene** ... (P3 + P4 헌법 8조 위반 경로)" | 변경 0건 | 8조 only — 5조-2 직접 무관 (정정 0건 자격 R-1) |
| **line 63** | "**GP-4 External Input Validation** ... (P5 헌법 8조 #3)" | 변경 0건 | 8조 only (정정 0건 자격 R-1) |
| **line 64** | "**GP-5 Provider Adapter Enforcement** ... \| **HIGH** (**Provider Liquidity 5-way Layer 1 모법**)" | "**HIGH** (**헌법 5조-2 Provider Liquidity 5-way Layer 1 모법**)" ✅ | **(i) 최소 정정 적용 완료** |
| **line 65** | "**GP-6 Memory / Skill Migration Feasibility** ... \| **MEDIUM** (P8 + **Provider Liquidity Layer 4 — Provider 교체 자유**)" | "**MEDIUM** (P8 + **헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유**)" ✅ | **(i) 최소 정정 적용 완료** |
| **line 111** | "**G4 Round-trip validation PoC** ... (**Provider Liquidity Layer 4** — JSONL Hermes 의존 0)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |
| **line 114** | "**G4 Memory/Skill schema validation** ... (**Provider Liquidity Layer 3**)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |
| **line 137** | "**1** \| **G2 GP-5 Provider Adapter Enforcement** ... HIGH 보안 (**Provider Liquidity 5-way Layer 1 모법**)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |
| **line 142** | "**3 (tie)** \| **G4 Round-trip validation PoC** ... HIGH (**Provider Liquidity Layer 4**)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |
| **line 146** | "**6 (tie)** \| **G4 Memory/Skill schema validation** ... MEDIUM (**Provider Liquidity Layer 3**)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |
| **line 147** | "**7** \| **G2 GP-6 Memory/Skill Migration Feasibility** ... MEDIUM (**Provider Liquidity Layer 4**)" | 변경 0건 ((i) 범위 외) | **(ii) 중간 정정 후보** — 별도 cycle 의무 |

**🔴 R-rec-1 권고 답습 영구**: line 61~63 GP-2~4 정정 0건 자격 = R-1 답습 분류 기준 *명문* — 보안 결과 차단 = 헌법 8조 직접 모법 = Provider Liquidity 본질 (모델/구독 교체 자유) 와 *직접 무관* = 정정 0건 자격. ADR-011 line 212 "Provider Liquidity 영향 \| 무관" 답습 정합.

### 2.5 ADR-011 line 6 + line 245 현재 verbatim (R-S1 답습 영구 — (g1-N-2) `3bdb1be` 결과 유지)

```
line 6     **상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
line 245   - `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)
```

**본 cycle 변경 0건** (ADR-011 = (g1-N-2) 결과 유지, **ADR-011 line 212 본문 정정 = (g1-O) 별도 cycle 의무** carry-over).

### 2.6 ADR-011 + 헌법 + (g1-N-1)/(g1-N-2) + 본 cycle Reviewer 권한 한계 (9) 신규 boundary 명문 (R-7 + R-11 + R-13 답습)

**Reviewer 권한 한계 영구 답습 chain** (framing 통일 — R-11 답습 영구):
- (1) ADR-011 §6 본문 정정 자격 = (g1-N-2) cycle 예외 자격 발효 직접 적용 완료
- (4) 헌법 본문 정정 자격 = (g1-N-1) cycle 예외 자격 발효 직접 적용 완료, **헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무**
- **(9) 신규 (본 cycle 발효 후 = 9 항목 영구 답습)** — CLAUDE.md / roadmap.md 본문 정정 자격 = 본 (g1-N-3) cycle 합의 채택 + 단일 atomic commit 시점 *예외 자격* 발효 **직접 적용 완료** (R-13 (4-c) 동형 패턴 답습 + (1) (4) chain 답습)

### 2.7 16 영향 문서 carry-over by-reference only + (g1-N-3-pamsd) + (g1-N-3-hermes) HIGH 격상 (R-S4 + R-7 + R-8 BLOCKING 답습)

> **🔴 R-S4 격상 답습 영구 (C-S1 → R-S4)**: provider-agnostic-memory-skill-design.md 본문 전체 `grep -c "Provider Liquidity"` = **19 위치** 정량 (raw line-level direct cross-check 충족). 특히 line 27 "**상위 권위**: 헌법 제5조 관용 (Provider Liquidity), 헌법 제8조 (보안)" + line 1143 "**Provider Liquidity** \| 헌법 5조 (관용) + `feedback_provider_liquidity.md` + ADR-008 차단조건 #2 \| §3.5 + §4.3 + §6.4 (3-way 보호)" + line 1292 "**정정 명명**: **Provider Liquidity 4-way Multi-layer Defense**" = **§11.4.2 4-way Multi-layer Defense 본문 자체 헌법-동급 권위**. brief v1 §8.2 LOW 분류 = 과소평가, 본 v1.1 §8.2 신규 분리 **HIGH** 격상.

| 후보 별도 cycle | 우선순위 | 출처 BLOCKING / 격상 |
|---|---|---|
| **(g1-N-3-pamsd)** ⭐⭐⭐ provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 단독 분리 cycle | **HIGH** | R-7 BLOCKING + R-S4 격상 답습 영구 |
| **(g1-N-3-hermes)** ⭐⭐ hermes-adoption-design-v3.md line 13 상위 권위 *직접 stale* (R-S3 carry-over 영구) | **HIGH** (MEDIUM → HIGH 격상) | R-8 BLOCKING 답습 |
| (g1-N-3-gov) governance-preconditions.md §1.1 + line 26~96/108/803 정합 정정 | MEDIUM | by-reference carry-over |
| (g1-N-3-adr-series) ADR-008/009/010/012 정합 정정 | MEDIUM | by-reference carry-over (ADR-008 line 86 = "비협상" 이미 충족 evidence, R-rec-12 + C-S3 답습) |
| (g1-N-3-llm-providers) llm-providers-design.md + mvp-1-to-6-entry-conditions-brief.md 정합 정정 | MEDIUM (pamsd 분리 후) | by-reference carry-over |
| 기타 hermes 시리즈 (hermes-adoption-design.md / hermes-not-root-of-trust-runtime.md / system-identity-prequel.md) | MEDIUM | by-reference carry-over |

**본 cycle 범위 외, 별도 cycle 의무** (사용자 명시 (β) 범위 boundary 답습 영구).

### 2.8 3-way trade-off carry-over 영구 (R-S3 격상 답습 — 헌법 line 80 + ADR-011 line 212 + hermes-adoption-design-v3.md line 13)

> **🔴 R-S3 격상 답습 영구**: 3 stale 위치 동시 존재 + 본 (g1-N-3) cycle 변경 0건 자격 명문. (g1-N-3') / (g1-O) / (g1-N-3-hermes) 3 후속 cycle 의무 carry-over.

- **헌법 line 80**: "ADR-011 line 6 상위 권위 매핑 답습 ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)")" ↔ ADR-011 line 6 현재 "헌법 제5조-2 (Provider Liquidity, 비협상)" → **임시 stale** (R-S2 → R-S3 carry-over 영구, (g1-N-3') 별도 cycle 의무)
- **ADR-011 line 212**: "Provider Liquidity 영향 \| 무관 \| 본 ADR은 redaction 수단 해석이며 모델/구독 교체 자유와 무관" → 5조-2 신설 후 "무관" 표현 정합성 평가 필요, (g1-O) carry-over
- **hermes-adoption-design-v3.md line 13**: "상위 권위: 헌법 제5조 (Provider Liquidity)..." → (g1-N-3-hermes) 별도 cycle 의무 HIGH 격상

---

## 3. SDD 정합성 매트릭스

### 3.1 CLAUDE.md / roadmap.md 본문 변경 정합성 (본 commit 결과)

| 위치 | 본 cycle 변경 결과 |
|---|---|
| **CLAUDE.md line 244** | "헌법 8조 본질" → "**헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질 ... 상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)**" **변경 완료** ✅ ((i) 최소 정정 R-rec-15 답습) |
| **roadmap.md line 64** | "HIGH (Provider Liquidity 5-way Layer 1 모법)" → "HIGH (**헌법 5조-2 Provider Liquidity 5-way Layer 1 모법**)" **변경 완료** ✅ ((i) 최소 정정) |
| **roadmap.md line 65** | "MEDIUM (P8 + Provider Liquidity Layer 4 — Provider 교체 자유)" → "MEDIUM (P8 + **헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유**)" **변경 완료** ✅ ((i) 최소 정정) |
| CLAUDE.md §1 SDD / §7 의존 표 / §8 line 233 | 변경 0건 ((i) 최소 정정 범위 외, (ii)/(iii) carry-over by-reference only — Reviewer 권한 한계 (9-b) 답습) |
| roadmap.md line 61~63 (GP-2~4) | 변경 0건 자격 (R-1 답습 분류 기준 — 헌법 8조 only Provider Liquidity 직접 무관) |
| roadmap.md line 111/114/137/142/146/147 | 변경 0건 ((i) 최소 정정 범위 외, (ii) 중간 정정 carry-over by-reference only — 별도 cycle 의무) |

### 3.2 헌법 본문 변경 자격 0 + 헌법 line 80 임시 stale carry-over (R-S3 영구)

- 헌법 line 40~46 (5조 "코드 품질 원칙") — 변경 0건
- 헌법 line 75~80 (5조-2 신규, (g1-N-1) commit 결과 유지) — 변경 0건
- **헌법 line 80 임시 stale** — 본 cycle 변경 0건, **(g1-N-3') 별도 cycle 의무** carry-over (R-S2 → R-S3 carry-over 영구, **§2.2 verbatim cross-check 참조** — "line 80 인용 \"헌법 제5조 (Provider Liquidity)\" ≠ ADR-011 line 6 현재 \"헌법 제5조-2 (Provider Liquidity, 비협상)\"") (R-rec-7 답습)
- 헌법 line 104~105 (종결 명문, R-S1 답습 영구) — 변경 0건

### 3.3 ADR-011 본문 변경 자격 0 + ADR-011 line 212 carry-over

- ADR-011 line 6 + line 245 — (g1-N-2) 결과 유지, 변경 0건
- ADR-011 line 212 ("Provider Liquidity 영향 \| 무관") — 변경 0건, **(g1-O) 별도 cycle 의무** carry-over (R-S3 3-way trade-off 답습 영구)

### 3.4 MVP-1 + 메모리 + ADR-008 본문 변경 자격 0

- MVP-1 R4 by-reference carry-over only (R-6 + R-20 답습)
- 메모리 line 7 + line 12~17 by-reference 답습, **MEMORY.md 9.4% over R-S4 carry-over depth 4 cycle 누적** (R-7 cleanup cycle 우선순위 HIGH 격상 carry-over)
- ADR-008 부록 B B.1~B.6 by-reference only (R-S3 답습 영구) — **ADR-008 line 86 "비협상" 이미 충족 evidence** (R-rec-12 + C-S3 답습) carry-over

### 3.5 16 영향 문서 변경 자격 0 (사용자 명시 (β) 범위 boundary) + (g1-N-3-pamsd) 신규 분리 carry-over

본 cycle 범위 = CLAUDE.md + roadmap.md only. 16 영향 문서 = **본 cycle 합의 결과 carry-over** 자격, 본 cycle 본문 변경 0건. **(g1-N-3-pamsd) 신규 분리 HIGH carry-over** (R-S4 격상) + **(g1-N-3-hermes) HIGH 격상** (R-S3 carry-over).

---

## 4. CLAUDE.md / roadmap.md 정정 본문 후보 매트릭스 + (i) 최소 정정 채택 결과 (R-3 + R-S1 격상 라벨 정정 답습 영구)

### 4.1 본문 후보 (i)~(iv) 매트릭스 (라벨 정정 적용 — R-S1 격상 답습 영구)

> **🔴 R-S1 격상 답습 영구**: brief v1 §2.3 ↔ §4.1 내부 모순 정정 — §2.3 라벨 정합 정정 후 (i)~(iv) 매트릭스 정의 유지.

| 후보 | CLAUDE.md 변경 | roadmap.md 변경 | 강도 | 본 cycle 채택 자격 |
|---|---|---|---|---|
| **(i) 최소 정정** ✅ **채택 완료** | §8 line 244 ADR-011 entry "헌법 8조 본질" → "헌법 8조 + 5조-2 본질" **만** | line 64/65 GP-5/6 "Provider Liquidity" → "헌법 5조-2 Provider Liquidity" **만** | 약 | **본 commit 채택 적용 완료** (Reviewer R-rec-15 답습) |
| **(ii) 중간 정정** | §7 의존 표 5조-2 entry 추가 + §8 line 244 보강 | line 64/65/111/114/137/142/146/147 모두 "헌법 5조-2 Provider Liquidity" reference 추가 | 중 | carry-over by-reference only (별도 cycle 의무) |
| **(iii) 최대 정정** | §1 SDD + §7 의존 표 + §8 참조 표 line 233 강조 + line 244 보강 모두 | (ii) 동일 + 본문 다른 "Provider Liquidity" 인용 모두 정정 | 강 | carry-over by-reference only |
| **(iv) 광범위 정정** | (iii) 동일 | (iii) 동일 + 16 영향 문서 일부 포함 | 매우 강 | **사용자 명시 (β) 범위 boundary 위반 risk** (R-15 답습), 채택 자격 0 영구 |

### 4.2 본 cycle (i) 최소 정정 채택 결과 boundary 명문 (R-6 + R-rec-15 답습)

> **🔴 R-6 BLOCKING 답습 — "*입력 only*" boundary 명문 영구**: 본 cycle 합의 시 (i)~(iii) 후보 = Agent A/B/C 분석 *입력*, Reviewer (9-a) 발의 *입력*, 사용자 명시 단독 채택 *입력*. 본 합의 *자체* 가 (i)~(iii) 중 1 후보 *고정* 자격 0. **합의 채택 = APPROVE w/ COND + Reviewer 발의 권고 + 사용자 명시 후 단일 atomic commit 시점 *최종* 채택**. 본 commit 시점 = 사용자 명시 "(i) 최소 정정" 채택 → 단일 atomic commit 발효 완료 ✅.

- **(i) 최소 정정 채택 결과** (본 commit 시점):
  - CLAUDE.md line 244 ADR-011 entry 보강 완료 ✅
  - roadmap.md line 64 GP-5 reference 추가 완료 ✅
  - roadmap.md line 65 GP-6 reference 추가 완료 ✅
  - 나머지 위치 = 변경 0건 (별도 cycle 의무 carry-over)
- (ii) 중간 정정 + (iii) 최대 정정 = **carry-over by-reference only** (별도 cycle 의무, R-15 + (9-b) 답습)
- (iv) 광범위 정정 = boundary 위반, 본 cycle 채택 자격 0 영구

### 4.3 본 cycle 범위 boundary 명문 (R-rec-6 + R-rec-2 답습 — 부분 정정 자격 0 영구)

> **🔴 R-rec-6 답습**: (i)~(iii) 중 1 후보 *전체* 채택 의무 (예: (i) 채택 시 (i) 의 모든 변경 동시 atomic 적용, (i) 의 일부만 적용 자격 0). 본 commit = (i) *전체* 적용 = CLAUDE.md line 244 + roadmap.md line 64 + line 65 = 3 위치 동시 atomic commit 발효 ✅.

- CLAUDE.md = §8 line 244 만 변경 ((i) 최소 정정 정의 정합)
- roadmap.md = line 64 + line 65 만 변경 ((i) 최소 정정 정의 정합, R-rec-3 일관성 권고 — 본 cycle (i) 한정 = line 64/65 2 위치 일관성 충족)
- roadmap.md line 61~63 (GP-2~4) = 변경 0건 자격 (R-1 답습 분류 기준 — A-R1 권고 답습)
- **16 영향 문서 = 본 cycle 범위 외, 별도 cycle 의무**
- **부분 정정 자격 0 영구** (R-10 + R-7 *대칭* 답습) — (i) 채택 시 *부분* 적용 자격 0, 전체 atomic 적용 의무 ✅ 충족

---

## 5. 핵심 긴장 분석 (4 긴장 — 본 cycle 임시 framing 명문, R-12 + R-29 답습 영구 정착 자격 0)

### 5.1 긴장 1 — "하위 layer 정합 정정" boundary vs *영구 framing 정착* risk (R-6 + R-12 답습)

- 본 (g1-N-3) cycle = (g1-N-1) 헌법 본문 변경 + (g1-N-2) ADR-011 본문 변경 결과의 *하위 의존 정합 정정* 차원
- *영구 framing 정착* risk = 본 brief 의 "하위 layer 정합 정정" framing 자체가 후속 cycle 의 정정 진입 근거화 자격 0 (R-12 답습)
- boundary 명문 = 본 cycle 합의 후 단일 atomic commit 으로 종료, 영구 framing 정착 자격 0

### 5.2 긴장 2 — (g1-N-3') 본 cycle 내 통합 *평가* vs *해결* 분리 (R-9 답습 + 사용자 명시)

- 사용자 명시 = (g1-N-3') 본 cycle 내 **통합 *평가*** (식별 only)
- **해결 자격 = 별도 cycle** (R-9 헌법 본문 변경 답습 영구 의무)
- 본 cycle = 헌법 line 80 임시 stale **식별** + (g1-N-3') 별도 cycle 의무 carry-over **명문** (해결 0건)

### 5.3 긴장 3 — 16 영향 문서 carry-over self-citation anchor 차단 (R-12 + R-29 + R-15 통합 답습)

- 본 cycle 범위 = (β) CLAUDE.md + roadmap.md only
- 16 영향 문서 carry-over = 본 cycle 합의 결과 *입력* 자격, 별도 cycle 의무
- self-citation anchor risk = 본 brief §2.7 + §3.5 가 후속 cycle 의 정정 진입 근거화 *de facto* 압력 0 (R-29 답습)
- **anchor depth limit cycle 9-cycle entry 도달 *비추론* 차단** (R-10 BLOCKING 답습)

### 5.4 긴장 4 — Reviewer 권한 한계 (9) 신규 boundary (R-7 + R-11 + R-13 답습 — framing 통일 영구)

- **(9) 신규** (본 cycle 발효 후 = 9 항목 영구 답습): CLAUDE.md / roadmap.md 본문 정정 자격 = 본 cycle 합의 채택 + 단일 atomic commit 시점 *예외 자격* 발효 **직접 적용 완료** (R-13 (4-c) 동형 패턴)
- (1) (4) chain 답습 = (g1-N-2) (1) ADR-011 §6 예외 발효 + (g1-N-1) (4) 헌법 본문 예외 발효 + 본 cycle (9) CLAUDE.md/roadmap.md 예외 발효 **완료** ✅
- **(9-a)~(9-d) sub-boundary 답습 충족** (§6.3 본문 명문)

---

## 6. 3+1 합의 분담안 (carry-over)

### 6.1 Agent + Reviewer 분담 + 핵심 질문

본 cycle 합의 (`386c552`) §6.1 carry-over. Q-A1~A3 / Q-B1~B5 / Q-C1~C5 / Q-R1~R4 carry-over.

### 6.2 분담 의무 (R-22 답습)

본 cycle 합의 분담 의무 carry-over. Reviewer 단독 격상 4 (R-S1·R-S2·R-S3·R-S4) 완료. 3 Agent 정면 충돌 0건 = 강한 정합성 evidence + 4-way 일치 BLOCKING 1 (R-1).

### 6.3 Reviewer 권한 + 한계 (R-14 + R-7 답습 — 9 항목 영구 명문 + (9) 신규 예외 자격 발효 직접 적용 완료 + R-11 framing 통일 답습 영구)

> **Reviewer 권한 한계 9 항목 출처 chain** (R-7 답습): Provider Liquidity → format → (g1-A) → (g1-N) → (g1-N-1) → (g1-N-2) → 본 (g1-N-3) brief §6.3 (**7 cycle carry-over chain**).

> Reviewer 권한 = brief v1 진술 BLOCKING 정정 권한 + **본 cycle 합의 채택 시 CLAUDE.md / roadmap.md 본문 정정 자격 (9) 신규 예외 발효 — 단일 atomic commit 시점 적용 직접 완료** (R-13 (4-c) 동형 패턴).

**9 권한 한계 영구 답습 + (9) 예외 자격 발효 직접 적용 완료 + (9-a)~(9-d) sub-boundary**:

> **🔴 R-11 framing 통일 답습 영구**: "8 → 9 격상" = entry 시점 *임시* framing. **본 commit 발효 후 = "9 항목 영구 답습" (본 cycle 직전 까지 8 항목, 본 cycle 발효 후 9 항목)**.

1. **ADR-011 §6 본문 정정 자격 = (g1-N-2) cycle 예외 자격 발효 직접 적용 완료** ((1-a)~(1-d) 답습)
2. Provider Liquidity 본질 약화 자격 0
3. MVP-1 합의 본문 정정 자격 0
4. **헌법 본문 정정 자격 = (g1-N-1) cycle 예외 자격 발효 직접 적용 완료**, 헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무
5. 메모리 본문 정정 자격 0
6. 4 가족 분류 + 6축 framing 영구 정착 자격 0
7. 자동 다음 단계 진입 자격 0
8. 결합 cycle 진입 자격 평가 자격 0
9. **CLAUDE.md / roadmap.md 본문 정정 자격 = 본 (g1-N-3) cycle 합의 채택 + 사용자 명시 *후* 단일 atomic commit 시점 *예외 자격* 발효 직접 적용 완료** (R-13 (4-c) 동형 패턴 답습 + (1)(4) chain 답습)
   - **(9-a)** Reviewer 가 (i)~(iii) 후보 채택 자격 BLOCKING 발의 = 본 합의 BLOCKING R-1~R-12 + R-S1~R-S4 발의 완료 ✅
   - **(9-b)** Reviewer 가 *현 CLAUDE.md / roadmap.md 다른 부분* 정정 권고 = 자격 0 (별도 cycle 의무 (g1-N-3-pamsd)/(g1-N-3-hermes)/(g1-N-3-gov)/(g1-N-3-adr-series)/(g1-N-3-llm-providers)) ✅
   - **(9-c)** Reviewer 가 *합의 후 단계 본문 정정 시점* verbatim 본문 권고 = R-rec-15 "(i) 최소 정정 권고" 발의 완료, 사용자 명시 단독 발효 후 본 commit 발효 ✅
   - **(9-d)** "사용자 명시 *전* 단계 (Reviewer 합의 산출 후 + 사용자 명시 *전*)" sub-boundary — (g1-N-2) (1-d) 답습 (R-11 답습). **차단 메커니즘** (R-9 BLOCKING 답습): Reviewer 합의 산출 (본 합의 보고서 commit `386c552`) 후 사용자 "(i) 최소 정정" 또는 동등 명시 *전* 까지 CLAUDE.md/roadmap.md 본문 변경 자격 0. brief v1.1 보강 commit + 본문 정정 atomic commit *둘 다* 사용자 명시 단독 발효 (자동 진입 0건, R-30 + R-24 *대칭* 답습). ✅

---

## 7. 합의 출력 형식 (carry-over)

본 cycle 합의 (`386c552`) §형식 carry-over.

### 7.2 raw line-level cross-check 의무 (R-1 + R-S1 답습 영구)

- **본 (g1-N-3) brief v1.1** (본 문서)
- `docs/phase0/jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction-consensus-entry-brief.md` v1 (`19b0f76`, 522줄)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction.md` (`386c552`, 423줄, BLOCKING 12 + R-S1~R-S4)
- **`CLAUDE.md` 본 commit 후 line 244** — 본 cycle 변경 결과 verbatim ((i) 최소 정정)
- **`docs/architecture/implementation-runtime-roadmap.md` 본 commit 후 line 64 + line 65** — 본 cycle 변경 결과 verbatim ((i) 최소 정정)
- `docs/constitution/PROJECT_CONSTITUTION.md` line 75~80 + **line 80 (R-S3 임시 stale carry-over)** + line 104~105
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` line 6 + line 245 (R-S1 답습 영구) + line 212 ((g1-O) carry-over)
- ADR-008 부록 B B.1~B.6 by-reference (R-S3 답습) + **line 86 "비협상" 이미 충족** (R-rec-12 + C-S3 답습)
- 메모리 `feedback_provider_liquidity` line 7 + line 12~17 verbatim

---

## 8. 후속 결정 권고 옵션 매트릭스

### 8.1 본 (g1-N-3) 적용 후 별도 단계

| 단계 | 내용 | 자격 |
|---|---|---|
| (1) brief v1 commit | `19b0f76` ✅ 완료 | 사용자 명시 |
| (2) 풀 3+1 합의 commit | `386c552` ✅ 완료 | 사용자 명시 "(A)" |
| **(3) brief v1.1 + CLAUDE.md/roadmap.md (i) 최소 정정 atomic commit** | **본 commit (현재)** | 사용자 명시 "(i) 최소 정정" + R-rec-15 답습 |
| (4) 세션 정리 | SESSION + CONTEXT + INDEX | 사용자 명시 |

### 8.2 (g1-N-3) carry-over — 우선순위 격상 (R-7 + R-8 BLOCKING 답습)

| 후속 cycle | 우선순위 | 출처 BLOCKING / 격상 |
|---|---|---|
| **(g1-N-3')** ⭐⭐⭐ 헌법 line 80 임시 stale 정정 cycle | **HIGH** | R-S3 carry-over 영구 |
| **(g1-N-3-pamsd)** ⭐⭐⭐ provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 정합 정정 (**신규 분리**) | **HIGH** | R-7 BLOCKING + R-S4 격상 |
| **(g1-N-3-hermes)** ⭐⭐ hermes-adoption-design-v3.md line 13 상위 권위 *직접 stale* 정정 (MEDIUM → **HIGH** 격상) | **HIGH** | R-8 BLOCKING + R-S3 |
| **MEMORY.md cleanup cycle** ⭐⭐ depth 4 cycle 누적 | **HIGH** | R-7 + R-S4 carry-over 강화 |
| **(ii) 중간 정정 carry-over** roadmap.md line 111/114/137/142/146/147 정합 정정 + CLAUDE.md §7 의존 표 보강 | MEDIUM | by-reference carry-over |
| **(iii) 최대 정정 carry-over** CLAUDE.md §1 SDD + §8 line 233 강조 | MEDIUM | by-reference carry-over |
| (g1-N-3-gov) governance-preconditions.md §1.1 광범위 정정 | MEDIUM | by-reference carry-over |
| (g1-N-3-adr-series) ADR-008/009/010/012 정합 정정 (ADR-008 line 86 = "비협상" 이미 충족) | MEDIUM | by-reference carry-over (R-rec-12 답습) |
| (g1-N-3-llm-providers) llm-providers-design.md + mvp-1-to-6-entry-conditions-brief.md 정합 정정 | MEDIUM (pamsd 분리 후) | by-reference carry-over |
| (g1-O) ADR-011 line 212 본문 미세 보강 | MEDIUM | (g1-N-2) carry-over + R-S3 영구 |
| anchor depth limit cycle 진입 trigger 명문 | LOW | R-10 BLOCKING 답습 — 9-cycle 도달 *비추론* |
| (g1-N-3γ) 대안 (v)~(ix) 통합 framing 자격 평가 | LOW | R-rec-9 + R-rec-13 carry-over |

### 8.3 DEFER / 기각 옵션 (R-30 + R-24 *대칭* 답습) — 본 cycle 적용 완료 후 carry-over only

- (gN-3-D1) DEFER 자격 — 본 cycle 부분 채택 / 부분 DEFER 시 R-9 답습 영구 의무 미충족 risk (carry-over only, 채택 자격 0)
- (gN-3-D2) 기각 자격 — 본 cycle 후보 (i)~(iii) 모두 기각 시 (g1-N-1)/(g1-N-2) 결과 정합 회복 미충족 risk (carry-over only, 채택 자격 0)
- (v)~(ix) 대안 후보 carry-over by-reference only (R-rec-9 답습) — (g1-N-3γ) 통합 framing 자격 평가 별도 cycle 의무

---

## 9. 정직성 한계 (22 항목)

1. 본 brief v1.1 = (i) 최소 정정 채택 적용 완료, 본 commit 변경 결과 명문
2. (ii) 중간 정정 + (iii) 최대 정정 = carry-over by-reference only, 별도 cycle 의무
3. R-9 답습 = 본 cycle *간접* 적용 (헌법 본문 변경 직접 적용 아님, 하위 의존 정합 정정 차원)
4. Reviewer 권한 한계 (9) 신규 boundary = 본 commit 시점 예외 자격 발효 직접 적용 완료
5. (g1-N-3') 별도 cycle 의무 carry-over = 본 cycle 통합 *평가* 자격만, *해결* 자격 0 (사용자 명시 단독 발효)
6. 16 영향 문서 = 본 cycle 범위 외, 별도 cycle 의무 (사용자 명시 (β) 범위 boundary)
7. R-S3 헌법 line 80 + ADR-011 line 212 + hermes v3 line 13 3-way trade-off carry-over 영구
8. R-S2 "비협상" 명문 추가 boundary 답습 (헌법 line 75 + ADR-011 line 6 verbatim 직접 답습)
9. R-S1 §2.3 ↔ §4.1 내부 모순 정정 답습 영구 + line 245 entire verbatim 답습 (R-1 답습 영구)
10. R-S4 provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 carry-over + MEMORY.md 9.4% over depth 4 cycle 누적
11. R-S5 §0 ↔ §10.1 1:1 매핑 self-consistency 답습 영구 + 의미적 한계 인정 명문 (R-12 답습)
12. (9-d) 신규 sub-boundary "사용자 명시 *전* 단계" 차단 메커니즘 본문 명문 (R-9 BLOCKING 답습)
13. 본 brief framing 임시 framing 명문, 영구 정착 자격 0 (R-12 답습) + framing 통일 "8 → 9 격상" vs "9 항목 영구 답습" (R-11 답습)
14. ADR-011 line 212 ((g1-O) carry-over) 본 cycle 변경 0건
15. 본 cycle = 9번째 cycle entry, brief progression chain anchor depth limit cycle 진입 trigger 명문 부재 carry-over (R-22) + *비추론* 차단 (R-10 BLOCKING)
16. 본 cycle 합의 채택 자격 평가 + 사용자 명시 "(i) 최소 정정" 채택 + Reviewer 권한 한계 (9) 예외 자격 발효 시점 적용 완료
17. CLAUDE.md / roadmap.md 정정 = 헌법급 변경 *결과 반영* 의 하위 의존 정합 정정 (R-9 직접 적용 아님)
18. 본 brief v1 522줄 → brief v1.1 ~700줄 (BLOCKING 12 verbatim + R-S1~R-S4 verbatim + (i) 채택 + framing 통일 + 분해 매핑 표 + §10.5/§10.6 본문 + 의미적 한계 인정)
19. §1.4 ↔ §6.3 분해 매핑 표 본문 신설 (R-1 4-way 일치 BLOCKING 답습)
20. §10.5 + §10.6 본문 신설 (R-2 BLOCKING 답습 — R-S5 self-consistency 강화)
21. (i) 최소 정정 채택 결과 = CLAUDE.md line 244 + roadmap.md line 64 + line 65 3 위치 동시 atomic commit 발효 ((9-c) 답습)
22. **MEMORY.md cleanup carry-over depth 4 cycle 누적** (Provider Liquidity → format → (g1-N) → (g1-N-1) → (g1-N-2) → 본 (g1-N-3) — R-7 cleanup 시급도 HIGH 격상 carry-over)

---

## 10. 차단 조건 (§0 12 항목 1:1 매핑 — R-15 = R-S3 + R-S5 답습 영구)

### 10.1 본 brief 가 자동 발효시키지 않는 것 (R-S5 의미적 한계 인정 명문)

> **🔴 §0 ↔ §10.1 1:1 매핑 *의미적 한계* 인정** (R-12 = R-S5 답습 영구 명문): §0 12 항목 = *하는 것 행위 명세*, §10.1 12 항목 = *하지 않는 것 차단 명세*. 1:1 매핑 = *수치* 동일 (12 = 12) self-consistency 만 의무, *의미적 1:1 매핑* 의무 0. 각 항목 = 동일 영역의 *행위 차원* + *차단 차원* 짝 (예: §0-1 = §10.1-1 모두 동일 영역). 의미적 비대칭은 R-S5 self-consistency 위반 아님 명문.

1. ❌ **CLAUDE.md *다른 부분* 자동 정정** — 본 commit (i) 최소 정정 = line 244 만 ((9-b) 답습)
2. ❌ **roadmap.md *다른 위치* 자동 정정** — 본 commit (i) 최소 정정 = line 64/65 만 ((9-b) 답습)
3. ❌ **헌법 본문 자동 정정** — (g1-N-1) 결과 유지, line 80 = (g1-N-3') 별도 cycle 의무
4. ❌ **ADR-011 본문 자동 정정** — (g1-N-2) 결과 유지, line 212 = (g1-O) 별도 cycle 의무
5. ❌ **MVP-1 합의 본문 자동 정정**
6. ❌ **메모리 본문 자동 정정** — line 7 + line 12~17 by-reference only, MEMORY.md cleanup depth 4 cycle 누적 carry-over
7. ❌ **ADR-008 본문 자동 정정** — 부록 B by-reference only (line 86 "비협상" 이미 충족 carry-over)
8. ❌ **16 영향 문서 자동 정정** — (β) 범위 boundary, (g1-N-3-pamsd) 신규 분리 HIGH + (g1-N-3-hermes) HIGH 격상 carry-over
9. ❌ **Provider Liquidity 본질 약화** — binary 본질 유지, (i) 최소 정정 = 5조-2 reference 추가 + "비협상" boundary 영구 답습 강화
10. ❌ **본 brief framing 영구 정착** (R-12 답습) + framing 통일 (R-11 답습)
11. ❌ **본 brief 진단표 → 후속 cycle 정정 진입 근거화 *de facto* 압력** (R-29 + R-S5 답습) + anchor depth limit cycle 9-cycle entry 도달 *비추론* 차단 (R-10 답습)
12. ❌ **본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 자격** 모두 0건 (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

### 10.2 합의 BLOCKING 처리 의무 (R-21 답습) — **본 v1.1 commit 시점 완료**

본 cycle 합의 결과 BLOCKING R-1 ~ R-12 verbatim 본문 직접 반영 100% (브리프 v1.1 본 §1.4.1 + §1.5 + §2.3 + §4.1 + §4.2 + §4.3 + §6.3 + §10.1 + §10.5 + §10.6 + §11.2 신설 본문) + Reviewer 단독 격상 R-S1~R-S4 verbatim 답습 영구 충족 ✅.

### 10.3 본 brief 진단표 → 후속 cycle 정정 진입 근거화 차단 (R-29 답습) + anchor depth limit 9-cycle 도달 *비추론* 차단 (R-10 BLOCKING 답습)

§2.3 + §2.4 + §3.1 + §4.1 + §11.1 진단표 = 본 cycle 합의 *입력* 자격만, 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0. **9-cycle entry 도달 *자체* 가 anchor depth limit cycle 진입 *근거화* 자격 0** — trigger 명문 = 사용자 명시 단독 발효, brief 자체 *de facto* 압력 자격 0.

### 10.4 본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 자격 0 영구 (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

### 10.5 본 brief 의 4 긴장 framing self-citation anchor 차단 (R-2 BLOCKING + R-12 + R-29 + R-15 통합 답습)

§5 4 긴장 framing ((1) 하위 layer 정합 정정 / (2) 통합 평가 vs 해결 / (3) 16 영향 문서 carry-over / (4) Reviewer 권한 한계 (9)) = 본 (g1-N-3) cycle *임시 framing* 명문. 후속 cycle 의 *영구 framing 정착* 자격 0. self-citation anchor 차단 — §5 자체가 후속 cycle 의 정정 진입 근거화 *de facto* 압력 0.

### 10.6 본 brief 의 §3·§4·§5·§8 진단표 후속 cycle 인용 자격 (R-2 BLOCKING + R-6 + R-S5 답습)

§3 SDD 정합성 매트릭스 + §4 (i)~(iv) 후보 매트릭스 + §5 4 긴장 분석 + §8 후속 cycle 우선순위 표 = 본 cycle 합의 *입력* 자격 only. 후속 cycle ((g1-N-3') / (g1-N-3-pamsd) / (g1-N-3-hermes) 등) 인용 시 **by-reference carry-over only** (R-6 답습) + **본 brief 합의 *입력* 자격 명문** (후속 cycle 의 *자동 채택* 자격 0). §0 12 ↔ §10.1 12 1:1 매핑 self-consistency 답습 (R-S5 의미적 한계 인정 명문 영구).

---

## 11. NOTE carry-over (90 항목, by-reference only — 80 carry-over + 본 cycle 신규 10)

### 11.1 brief progression chain trace 표 (R-S2 답습 carry-over 통일, **9번째 cycle entry**)

| cycle 차수 | cycle | brief / 합의 commit |
|---|---|---|
| 1 | Phase 3 entry / 합의 / 실 빌드 | `cc145fd` / `25eb008` / `e76acc8` / `7209743` |
| 2 | Provider Liquidity deep-dive | `9ed376a` / `a9e1e88` / `8ae1ab6` |
| 3 | format 가족별 분류 (f-K) | `f305174` / `d75dceb` / `eca4cf5` |
| 4 | (g1-A) 채택 | `fc6731e` / `d0f516d` / `bdcc3a6` |
| 5 | (g1-N) 헌법 5조-2 신설 자격 평가 | `6f64491` / `1ec9c5e` / `58e06d5` |
| 6 | (g1-N-1) 헌법 5조-2 본문 변경 commit | `5b0c0ab` / `77f36cf` / `148fbbe` |
| 7 | (g1-N-2) ADR-011 line 6/245 매핑 정정 | `8207f55` / `07cd3f4` / `3bdb1be` |
| 8 | 세션 7-8차 통합 정리 | `3f84c26` (세션 정리 only, brief X) |
| **9 (본 cycle)** | **(g1-N-3) CLAUDE.md / roadmap.md 정합 정정** | `19b0f76` (brief v1) / `386c552` (합의) / **`(본 v1.1 + CLAUDE.md/roadmap.md (i) 최소 정정 동시 commit)`** |

### 11.2 본 cycle 신규 NOTE 10 (N-91 ~ N-100)

| NOTE | 내용 | 출처 |
|---|---|---|
| **N-91** | R-1 4-way 일치 BLOCKING 격상 chain — A-B1 + B-B3 + B-S2 + C-B3 (단일 출처가 아닌 *분담 결과의 자연 수렴*, 편향 방지 헌법 4조 #3 정상 작동 evidence) | R-22 + 헌법 4조 #3 |
| **N-92** | (g1-N-3-pamsd) 신규 carry-over 분리 cycle = provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 단독 자격 | R-S4 |
| **N-93** | hermes-adoption-design-v3.md line 13 상위 권위 직접 stale = (g1-N-3-hermes) 시급도 MEDIUM → HIGH 격상 | R-S3 |
| **N-94** | Reviewer 단독 발견 0 = 3 Agent 분담 결과의 *전 영역 커버* (편향 방지 정상 작동) | 헌법 4조 #3 |
| **N-95** | R-S4 MEMORY.md cleanup carry-over depth 4 cycle 누적 (Provider Liquidity → format → (g1-N) → (g1-N-1) → (g1-N-2) → 본 (g1-N-3) — R-7 cleanup 시급도 HIGH 격상) | R-S4 carry-over |
| **N-96** | "8 → 9 격상" vs "9 항목 영구 답습" framing 통일 의무 = R-12 framing 영구 정착 자격 0 답습 + 본 commit 발효 후 = 9 항목 영구 답습 | R-12 + R-11 BLOCKING |
| **N-97** | §10.5 / §10.6 본문 부재 보강 의무 = R-S5 self-consistency 답습 영구 강화 | R-S5 + R-2 BLOCKING |
| **N-98** | (v)~(ix) 대안 후보 carry-over by-reference only — (g1-N-3γ) 통합 framing 자격 평가 별도 cycle 의무 | R-rec-9 + R-rec-13 |
| **N-99** | brief v1.1 보강 결과 = brief v1 522줄 → brief v1.1 ~700줄 (BLOCKING 12 verbatim + R-S1~R-S4 verbatim + (i) 채택 + framing 통일 + §1.4.1 분해 매핑 표 + §10.5/§10.6 본문 + §10.1 의미적 한계 인정) | R-21 + R-1 + R-2 BLOCKING |
| **N-100** | 본 합의 보고서 + brief v1.1 = (g1-N-3) cycle 9번째 brief progression chain entry — *고정* 자격 0, 사용자 명시 단독 발효 chain ((1) brief commit → (2) 합의 commit → (3) brief v1.1 + CLAUDE.md/roadmap.md atomic commit → (4) 세션 정리) | R-9 답습 |

### 11.3 NOTE carry-over 정정 의무 (R-S1~R-S4 답습 영구)

- **R-S1 정정 chain carry-over**: §2.3 line 143~145 라벨 정정 적용 완료 + raw line-level direct cross-check 답습 영구
- **R-S2 정정 답습**: CLAUDE.md grep 0 matches 정량 evidence + 헌법 line 80 임시 stale carry-over 영구 의무 ((g1-N-3') 별도 cycle)
- **R-S3 정정 답습**: "비협상" 명문 추가 boundary 영구 답습 + 3-way trade-off carry-over (헌법 line 80 + ADR-011 line 212 + hermes v3 line 13)
- **R-S4 정정 답습**: MEMORY.md cleanup cycle 우선순위 carry-over 영구 (depth 4 cycle 누적) + provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 (g1-N-3-pamsd) 신규 분리 HIGH carry-over

---

## 12. 변경 일람 표 + 다음 단계

### 12.1 변경 일람 표 (v1 → v1.1)

| § | 변경 내용 | 출처 BLOCKING / 권고 |
|---|---|---|
| **헤더 + §0 머리** | v1.1 (APPROVE w/ COND + (i) 최소 정정 채택 반영) 라벨. 합의 답습 R-S1~R-S4 + R-1~R-12 + 권고 16 + NOTE 10 명시 + **CLAUDE.md line 244 + roadmap.md line 64/65 단일 atomic commit 라벨** | R-21 + R-22 |
| **§0 *하는 것* 12** | (i) 채택 적용 결과 명문 + R-S5 의미적 한계 인정 명문 + 분해 매핑 표 신설 명시 + (g1-N-3-pamsd) 신규 분리 + framing 통일 | R-S1~R-S4 + R-1 + R-2 + R-11 + R-12 |
| **§0 *하지 않는 것* 12** | 1:1 매핑 R-S5 답습 정합화 + (9-b) CLAUDE.md/roadmap.md *다른 부분* 정정 자격 0 명문 + (i) 채택 외 부분 자격 0 (R-10) + anchor depth limit *비추론* 차단 (R-10) + framing 통일 (R-11) | R-15 + R-10 + R-11 + R-S5 |
| **§1.1 trigger** | 사용자 명시 "(i) 최소 정정" 채택 + R-19 답습 단계 (4) 직접 적용 명문 | R-19 |
| **§1.2 본 cycle 핵심 결과 표** | (i) 최소 정정 적용 결과 verbatim 명문 (CLAUDE.md line 244 + roadmap.md line 64 + line 65) + (ii)/(iii) carry-over by-reference only + "(i)~(iv) 매트릭스" → "(i)~(iv) 매트릭스 + (i) 채택" 정정 | R-4 + R-S1 |
| **§1.3 R-19 4 단계 완료 chain** | (1)~(4) 단계 모두 완료 + commit chain trace `19b0f76` / `386c552` / 본 commit | R-19 |
| **§1.4 R-9 7 항목 본 cycle 직접 적용 완료** | (1)~(7) 모두 적용 결과 ✅ | R-9 |
| **§1.4.1 §1.4 ↔ §6.3 분해 매핑 표 본문 신설** | 4-way 일치 BLOCKING — R-9 7 항목 ↔ §6.3 9 항목 1:1 분해 매핑 표 본문 | R-1 BLOCKING |
| **§1.5 framing 통일 명문 (신설)** | "8 → 9 격상" entry 시점 vs "9 항목 영구 답습" 발효 후 명문 | R-11 BLOCKING |
| **§2.3 CLAUDE.md 현재 stale + (i) 최소 정정 적용 결과 표** | §2.3 line 143~145 라벨 정정 ((i) → (iii)/(ii)/(iii)) + (i) 적용 결과 verbatim + R-S1 정량 evidence 명문 추가 | R-3 + R-5 + R-S1 + R-S2 |
| **§2.4 roadmap.md 현재 stale + (i) 최소 정정 적용 결과 표** | line 64/65 (i) 적용 verbatim + 나머지 변경 0건 명문 + line 61~63 정정 0건 자격 R-1 답습 강화 | R-rec-1 |
| **§2.7 16 영향 문서 + (g1-N-3-pamsd)/(g1-N-3-hermes) HIGH 격상 (신설)** | provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 + hermes v3 line 13 직접 stale | R-7 + R-8 BLOCKING + R-S4 |
| **§2.8 3-way trade-off carry-over (신설)** | 헌법 line 80 + ADR-011 line 212 + hermes v3 line 13 3-way trade-off | R-S3 |
| **§3.1 CLAUDE.md / roadmap.md 변경 결과 표** | (i) 적용 결과 verbatim (line 244 + line 64 + line 65) + 나머지 변경 0건 명문 | R-rec-3 + R-rec-4 |
| **§3.2 헌법 line 80 stale by-reference 강화** | §2.2 verbatim cross-check 참조 명문 강화 | R-rec-7 |
| **§3.4 MEMORY.md depth 4 cycle 누적 + ADR-008 line 86 carry-over** | depth 3 → depth 4 누적 정정 + ADR-008 line 86 "비협상" 이미 충족 carry-over | R-S4 + R-rec-12 |
| **§3.5 (g1-N-3-pamsd) + (g1-N-3-hermes) HIGH carry-over** | 시급도 격상 carry-over | R-7 + R-8 BLOCKING |
| **§4.1 (i) 최소 정정 채택 결과 표** | 라벨 정정 후 (i)~(iv) 매트릭스 + (i) 채택 완료 마킹 + (ii)/(iii) carry-over only | R-S1 + R-rec-15 |
| **§4.2 "*입력 only*" boundary 본문 (신설)** | 합의 후 사용자 명시 단독 발효 명문 | R-6 BLOCKING |
| **§4.3 부분 정정 자격 0 영구 명확화** | (i) 채택 시 *전체* atomic 적용 의무 명문 강화 | R-rec-6 |
| **§5 4 긴장 분석** | 4 긴장 *임시 framing* 명문 + anchor depth limit 9-cycle *비추론* 차단 추가 | R-10 + R-12 + R-S5 |
| **§6.3 (9-d) 차단 메커니즘 본문 신설** | (9-d) "사용자 명시 *전* 단계" 차단 메커니즘 verbatim 본문 | R-9 BLOCKING |
| **§6.3 framing 통일 영구** | "8 → 9 격상" vs "9 항목 영구 답습" 통일 명문 | R-11 BLOCKING |
| **§7.2 raw cross-check** | **본 v1.1 자체 + CLAUDE.md 본 commit 후 line 244 + roadmap.md 본 commit 후 line 64/65 + 헌법 line 80 (R-S3) + ADR-011 line 212 carry-over** | R-1 + R-S1 + R-S3 |
| **§8.1 후속 단계 (i) 채택 완료** | 단계 (3) (i) 채택 commit 완료 표 | R-19 |
| **§8.2 후속 cycle 우선순위 격상** | **(g1-N-3-pamsd) 신규 분리 HIGH + (g1-N-3-hermes) MEDIUM → HIGH 격상 + MEMORY.md cleanup depth 4 HIGH + (ii)/(iii) carry-over** | R-7 + R-8 BLOCKING + R-S3 + R-S4 |
| **§9 정직성** | 18 → **22 항목** — 항목 16/18 (i) 채택 + framing 통일 / 항목 19 분해 매핑 / 항목 20 §10.5/§10.6 / 항목 21 (i) 채택 verbatim 결과 / 항목 22 MEMORY.md depth 4 | R-1~R-12 + R-S1~R-S4 |
| **§10.1 §0↔§10.1 의미적 한계 인정 (신설)** | R-S5 답습 영구 명문 한계 인정 본문 | R-12 BLOCKING |
| **§10.5 + §10.6 본문 신설** | header only → 본문 신설 (R-S5 self-consistency 강화) | R-2 BLOCKING |
| **§11.2 신규 NOTE 10 (N-91~N-100)** | R-1~R-12 + R-S1~R-S4 + R-rec-1~R-rec-16 통합 | R-26 + 모든 R-# |
| **§11.3 carry-over 정정 의무** | R-S1 §2.3 정정 적용 완료 + R-S4 depth 4 누적 + R-S3 3-way trade-off | R-S1~R-S4 답습 영구 |
| **§12.1 변경 일람 표 (신규)** | v1 → v1.1 변경 일람 (본 §) | R-10 |
| **CLAUDE.md line 244 (외부 파일, 본 commit 동시)** | "헌법 8조 본질" → "**헌법 8조 (보안) + 5조-2 (Provider Liquidity, 비협상) 본질 ... 상위 권위 매핑 답습 (ADR-011 line 6/245 + 헌법 line 75~80)**" | R-19 단계 (4) + R-rec-15 |
| **roadmap.md line 64 (외부 파일, 본 commit 동시)** | "HIGH (Provider Liquidity 5-way Layer 1 모법)" → "HIGH (**헌법 5조-2 Provider Liquidity 5-way Layer 1 모법**)" | R-19 단계 (4) + R-rec-15 |
| **roadmap.md line 65 (외부 파일, 본 commit 동시)** | "MEDIUM (P8 + Provider Liquidity Layer 4 — Provider 교체 자유)" → "MEDIUM (P8 + **헌법 5조-2 Provider Liquidity Layer 4 — Provider 교체 자유**)" | R-19 단계 (4) + R-rec-15 |

**변경 통계**: brief v1 522줄 → brief v1.1 약 700줄 (+~178줄). BLOCKING 12 verbatim 본문 직접 반영 100%. 권고 16 본문 직접 반영 또는 §11 NOTE carry-over. NOTE 10 신규 + 80 carry-over = 90 by-reference only. 기각 0건. **Reviewer 단독 격상 4 (R-S1·R-S2·R-S3·R-S4) verbatim 본문 직접 반영 100%**. **CLAUDE.md line 244 + roadmap.md line 64 + line 65 (i) 최소 정정 단일 atomic commit 완료**.

### 12.2 다음 단계 (자동 진입 0건)

1. **본 v1.1 + CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 단일 atomic commit·push (현재)** — `docs(claude/roadmap): (g1-N-3) CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 — 헌법 5조-2 reference 추가`
2. **사용자 검토 + 명시 대기** — 본 commit 결과 확인 + 세션 정리 진입 자격 명시
3. 사용자 명시 → 세션 정리 — SESSION_2026-05-24.md + CONTEXT.md + INDEX.md 갱신 (본 commit 답습 명문 + brief progression chain 9번째 cycle entry 통합)
4. 세션 정리 commit·push
5. 후속 단계 = 사용자 명시:
   - **(g1-N-3')** ⭐⭐⭐ 헌법 line 80 임시 stale 정정 cycle (R-S3 carry-over) — 헌법 본문 변경 cycle, R-9 헌법 본문 변경 답습 영구 의무
   - **(g1-N-3-pamsd)** ⭐⭐⭐ provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위 정합 정정 (**신규 분리 HIGH**) — R-S4 격상 답습
   - **(g1-N-3-hermes)** ⭐⭐ hermes-adoption-design-v3.md line 13 상위 권위 *직접 stale* 정정 (MEDIUM → **HIGH 격상**) — R-S3 답습
   - **MEMORY.md cleanup cycle** ⭐⭐ depth 4 cycle 누적 (R-7 + R-S4 강화)
   - **(ii) 중간 정정 carry-over** roadmap.md line 111/114/137/142/146/147 + CLAUDE.md §7 의존 표
   - **(iii) 최대 정정 carry-over** CLAUDE.md §1 SDD + §8 line 233 강조
   - (g1-N-3-gov) governance-preconditions.md 광범위 정정
   - (g1-N-3-adr-series) ADR-008/009/010/012 정합 정정
   - (g1-N-3-llm-providers) llm-providers 시리즈 정합 정정
   - (g1-O) ADR-011 line 212 본문 미세 보강
   - anchor depth limit cycle 진입 trigger 명문 / 새 주제

**자동 다음 단계 진입 0건** (R-29 + R-30 + R-24 + R-7 *대칭* 답습).

---

**End of brief v1.1** (작성일 2026-05-24, (g1-N-3) cycle = brief progression chain **9번째 cycle entry**, R-19 답습 trigger 정확한 form 단계 (4) 직접 적용 완료 = **본 commit + CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 단일 atomic commit** (`docs(claude/roadmap): (g1-N-3) CLAUDE.md line 244 + roadmap.md line 64/65 (i) 최소 정정 — 헌법 5조-2 reference 추가`), 본 cycle 합의 `386c552` BLOCKING 12 + 권고 16 + NOTE 10 신규 + Reviewer 단독 격상 4 (R-S1·R-S2·R-S3·R-S4) verbatim 본문 직접 반영 100%, R-9 헌법급 변경 답습 영구 의무 7 항목 본 cycle *간접* 적용 완료, Reviewer 권한 한계 9 항목 영구 답습 (framing 통일 R-11 답습 영구) + (9) 예외 자격 발효 직접 적용 완료 + (9-a)~(9-d) sub-boundary 명문, MVP-1·메모리·헌법·ADR-008·ADR-011 본문 변경 0건, **헌법 line 80 + ADR-011 line 212 + hermes v3 line 13 3-way trade-off carry-over (R-S3 격상 영구)** + (g1-N-3') / (g1-O) / (g1-N-3-hermes) 3 후속 cycle 의무, Provider Liquidity 본질 약화 자격 0 ((i) 최소 정정 = 5조-2 reference 추가 + "비협상" boundary 영구 답습 강화), **(g1-N-3-pamsd) 신규 분리 HIGH carry-over (R-S4 격상 — provider-agnostic-memory-skill-design.md 19 위치 + §11.4.2 헌법-동급 권위)**, **MEMORY.md cleanup carry-over depth 4 cycle 누적** (R-7 cleanup 시급도 HIGH 격상), anchor depth limit cycle 9-cycle entry 도달 *비추론* 차단 (R-10 BLOCKING 답습), 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 4 양방향 자격 0건)
