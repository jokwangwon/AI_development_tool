# Jarvis MVP-1 (g1-N-3) CLAUDE.md / roadmap.md 정합 정정 자격 평가 cycle entry brief (v1)

> **본 brief = (g1-N-2) ADR-011 line 6/245 매핑 정정 cycle (`3bdb1be`, BLOCKING 10 + 권고 10 + NOTE 11 + Reviewer 단독 격상 3 R-S1~R-S3) 후속 carry-over cycle entry brief.** (g1-A) 합의 §7.1 (g1-N-3) 옵션 + (g1-N-2) 합의 §12.2 다음 단계 #5 (g1-N-3) carry-over 직접 발효. 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·CLAUDE.md 본문 자동 정정·roadmap.md 본문 자동 정정·헌법 본문 자동 정정·ADR-011 본문 자동 정정·MVP-1 합의 본문 자동 정정·메모리 자동 정정·Provider Liquidity 본질 약화·결합 cycle 자동 진입·자동 채택·자동 기각·부분 정정** 을 발생시키지 않는다. 실 변경 0건. **단 본 cycle 합의 채택 + 사용자 명시 *후* 단일 atomic commit 시점에 CLAUDE.md / roadmap.md 본문 변경 발효 (Reviewer 권한 한계 (9) 신규 예외 자격 발효 — R-13 (4-c) 동형 패턴 답습)**. staged: (g1-N-2) commit `3bdb1be` (ADR-011 line 6/245 매핑 정정) → 세션 7-8차 통합 정리 `3f84c26` → 새 세션 시작 → **본 (g1-N-3) brief v1 (현재)** → commit → 풀 3+1 합의 → brief v1.1 + CLAUDE.md/roadmap.md 정정 단일 atomic commit → 세션 정리. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-24 (8 cycle entry 통합 정리 `3f84c26` 후속, 새 세션 시작)
**카테고리**: 합의 cycle entry brief v1 ((g1-N-3) CLAUDE.md / roadmap.md 정합 정정, **9번째 cycle entry**)
**범위 (사용자 명시)**:
- **(β) CLAUDE.md + roadmap.md** ((g1-A) 합의 §7.1 (g1-N-3) 옵션 본문 표기 직역) — 좁은 범위, 16 영향 문서 별도 cycle 분리
- **정공법** (단계 (1)~(6) 풀 답습)
- **(g1-N-3') 본 cycle 내 통합 *평가*** (식별 only, *해결* 자격은 별도 cycle — R-9 헌법급 변경 답습 영구 의무)

**합의 답습** (R-22 의무):
- (g1-N-2) 합의 BLOCKING 10 + Reviewer 단독 격상 3 (R-S1 line 245 entire verbatim / R-S2 헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off / R-S3 "비협상" 명문 추가 boundary)
- (g1-N-1) 합의 BLOCKING 14 + Reviewer 단독 격상 4 (R-S1 line offset 산술 모순 / R-S2 chain 차수 / R-S3 ADR-008 부록 B framing / R-S4 본문 (i) 항목 4 영구화 anchor risk)
- (g1-N) 합의 BLOCKING 22 + Reviewer 단독 격상 5 (R-S1 line 97~98 자기-구속 / R-S2 "관용" + "비협상" 의미 충돌 / R-S3 ADR-008 부록 B framing + 8-2조 패턴 선례 / R-S4 MEMORY.md 9.4% over / R-S5 §0 ↔ §10.1 비대칭)
- (g1-A) 합의 BLOCKING 16 + Reviewer 단독 격상 3 (R-S1 메모리 line offset 정정 / R-S2 ADR-011 매핑 4 차원 분리 / R-S3 NOTE 합산 비중복 35)
- format 합의 BLOCKING 16 + Reviewer 단독 격상 3
- Provider Liquidity 합의 BLOCKING 13 + 권고 17 + NOTE 12
- R-9 헌법급 변경 답습 영구 의무 7 항목 본 cycle 적용 자격 평가
- Reviewer 권한 한계 8 항목 + **(9) 신규 CLAUDE.md / roadmap.md 본문 정정 자격 boundary**

**선행 답습**:
- `docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md` v1.1 (`3bdb1be`, 519줄, **R-S1~R-S3 답습 영구**)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md` (`07cd3f4`, BLOCKING 10 + 권고 10 + NOTE 11)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` **현재 line 6 + line 245** (본 cycle 변경 0건 영역, R-S1 verbatim 답습)
- `docs/constitution/PROJECT_CONSTITUTION.md` 현재 line 75~80 (5조-2 신설 본문) + **line 80 임시 stale (R-S2 carry-over 영구)** + line 82+ (9조 +7 이동) + line 104~105 (종결 명문 +7 이동)
- `docs/phase0/jarvis-mvp1-g1-n-1-constitution-article-5-2-body-change-commit-consensus-entry-brief.md` v1.1 (`148fbbe`, R-S1~R-S4 답습)
- `docs/phase0/jarvis-mvp1-constitution-article-5-2-provider-liquidity-new-clause-consensus-entry-brief.md` v1.1 (`58e06d5`, 780줄, R-S1~R-S5 답습)
- `CLAUDE.md` 현재 본문 (본 cycle 정정 대상 1 — §1 + §7 + §8 모두 변경 자격 평가)
- `docs/architecture/implementation-runtime-roadmap.md` 현재 본문 (본 cycle 정정 대상 2 — line 61~65 GP-2~6 + line 111/114/137/142/146/147 등 "Provider Liquidity" 인용 광범위)
- 메모리: `feedback_provider_liquidity` line 7 + line 12~17 / `project_jarvis_local_boss_direction` / `feedback_staged_consensus_workflow` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention`

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것 (12 항목, §10.1 와 1:1 매핑 의무 — R-15 = R-S3 + R-S5 답습)

1. (g1-A) 합의 §7.1 (g1-N-3) 옵션 + (g1-N-2) 합의 §12.2 다음 단계 #5 (g1-N-3) carry-over 답습 — CLAUDE.md / roadmap.md 정합 정정 자격 평가 (§1)
2. **CLAUDE.md 본문 현재 헌법 5조-2 신설 사실 미반영 식별** (§2.3) — §1 SDD / §7 의존 표 / §8 참조 표 3 영역 + line 244 ADR-011 entry "헌법 8조 본질" 만 인용
3. **roadmap.md 본문 현재 "Provider Liquidity" 인용 광범위 stale 식별** (§2.4) — line 61~65 GP-2~6 + line 111/114/137/142/146/147 등 10+ 위치
4. **R-9 헌법급 변경 답습 영구 의무 7 항목** 본 cycle *하위 layer 정합 정정* 차원 적용 자격 평가 (§1.4)
5. **Reviewer 권한 한계 8 항목 영구 답습 + (9) 신규 — CLAUDE.md / roadmap.md 본문 정정 자격 boundary** (§6.3, R-7 답습 8 → 9 격상)
6. SDD 정합성 매트릭스 — 헌법/ADR-011/CLAUDE.md/roadmap.md/MVP-1/메모리 본문 변경 자격 (§3)
7. CLAUDE.md / roadmap.md 정정 *본문 후보* 매트릭스 (§4) — (i)~(iv) 변경 강도 4 후보, **채택 자격 0** (R-15 답습 — 본 brief v1 = 진단·자격 평가 only, 실 변경은 단계 (4))
8. 핵심 긴장 **4축** 분석 (§5) — (1) "하위 layer 정합 정정" boundary + (2) (g1-N-3') 통합 *평가* vs *해결* 분리 + (3) 16 영향 문서 carry-over self-citation anchor 차단 + (4) Reviewer 권한 한계 (9) 신규 boundary
9. 3+1 합의 분담안 — Agent A/B/C 관점·핵심 질문·출력 형식 (§6)
10. 합의 출력 형식 + raw line-level cross-check 의무 (§7)
11. 후속 결정 권고 옵션 매트릭스 (§8) — **권고 자격 only, 결정 *고정* 0** (R-12 답습)
12. 정직성 한계 (§9) 18+ 항목 + 차단 조건 (§10) 12 항목 1:1 매핑 (R-15 = R-S3 + R-S5 답습 영구) + NOTE carry-over (§11) 80 by-reference + 본 cycle 신규 + §12 변경 일람 표 (v1.1 보강 시 신규)

### 하지 않는 것 (12 항목, §10.1 와 1:1 매핑 의무 — R-15 = R-S3 + R-S5 답습 영구)

1. ❌ **CLAUDE.md 본문 자동 정정** — 본 brief v1 = 진단·자격 평가 only. 본문 변경은 합의 *후* 사용자 명시 *후* 단일 atomic commit (Reviewer 권한 한계 (9) 신규 예외 자격 발효)
2. ❌ **roadmap.md 본문 자동 정정** — 동일 답습
3. ❌ **헌법 본문 자동 정정** — (g1-N-1) commit `148fbbe` 결과 유지, **헌법 line 80 임시 stale 정정 = (g1-N-3') 별도 cycle 의무** (R-S2 carry-over 영구). 본 cycle 통합 *평가* 자격만, *해결* 자격 0 (R-9 답습)
4. ❌ **ADR-011 본문 자동 정정** — (g1-N-2) commit `3bdb1be` 결과 유지, **ADR-011 line 212 본문 정정 = (g1-O) 별도 cycle 의무** carry-over (R-S2 답습 — Provider Liquidity 합의 R-13 + 본 cycle 합의 carry-over)
5. ❌ **MVP-1 합의 본문 자동 정정** — by-reference carry-over only (R-6 + R-20 답습)
6. ❌ **메모리 본문 자동 정정** — line 7 + line 12~17 by-reference 답습. **MEMORY.md 9.4% over R-S4 carry-over depth 3 cycle 누적** (R-7 cleanup cycle 우선순위 평가 carry-over 강화)
7. ❌ **ADR-008 본문 자동 정정** — 부록 B by-reference only (R-18 답습 영구)
8. ❌ **16 영향 문서 자동 정정** — `governance-preconditions.md` / `hermes-adoption-design.md` / `hermes-adoption-design-v3.md` / `system-identity-prequel.md` / `llm-providers-design.md` / `mvp-1-to-6-entry-conditions-brief.md` / `provider-agnostic-memory-skill-design.md` / `hermes-not-root-of-trust-runtime.md` / ADR-008 / ADR-009 / ADR-010 / ADR-012 = 본 cycle 범위 외, 별도 cycle 의무 (사용자 명시 (β) 범위 boundary)
9. ❌ **Provider Liquidity 본질 약화** — binary 본질 유지 (메모리 line 7 답습). 본 cycle 정정 = 헌법 5조-2 매핑 reference 정정 + "비협상" boundary 영구 답습 강화
10. ❌ **본 brief framing 영구 정착** (R-12 답습) — 4 후보 (i)~(iv) + 4 긴장 framing 본 cycle 임시 framing 명문, *영구화* risk 차단
11. ❌ **본 brief 진단표 → 후속 cycle 정정 진입 근거화 *de facto* 압력** (R-29 답습 + R-S5 답습 — §3·§4·§5 모두)
12. ❌ **본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 자격** 모두 0건 (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — 사용자 명시 "(g1-N-3)" + 범위 (β) + 정공법 + (g1-N-3') 통합 평가

- (g1-A) 합의 §7.1 (g1-N-3) 옵션 직접 발효 carry-over
- (g1-N-2) 합의 §12.2 다음 단계 #5 "(g1-N-3) CLAUDE.md §1 + §7 + §8 + roadmap.md 답습 추가 (R-15)" carry-over
- 사용자 명시 (2026-05-24, 새 세션 시작): "(g1-N-3)" + 범위 (β) + 정공법 + (g1-N-3') 본 cycle 내 통합 *평가*
- R-19 답습 trigger 정확한 form 4 단계 직접 적용 — 본 cycle 은 *하위 layer 정합 정정* cycle 차원 (R-9 헌법급 변경 *직접 적용 아님*, 단 답습 의무)

### 1.2 본 cycle 의 핵심 결과 (R-19 답습 단계 (4) 직접 적용 예정)

| 변경 대상 | 본 cycle 결과 |
|---|---|
| **CLAUDE.md** | 본문 변경 (§1.4 본 cycle 합의 채택 후 단일 atomic commit 시점, 변경 후보 (i)~(iv) 매트릭스) |
| **roadmap.md** | 본문 변경 (§1.4 본 cycle 합의 채택 후 단일 atomic commit 시점, 변경 후보 (i)~(iv) 매트릭스) |
| 헌법 본문 | 변경 0건 ((g1-N-1) 결과 유지, line 80 임시 stale = (g1-N-3') 별도 cycle 의무) |
| ADR-011 본문 | 변경 0건 ((g1-N-2) 결과 유지, line 212 = (g1-O) 별도 cycle 의무) |
| 16 영향 문서 | 변경 0건 (사용자 명시 (β) 범위 boundary, 별도 cycle 의무) |
| 본 brief | v1 (현재) → 풀 3+1 합의 → v1.1 (BLOCKING verbatim + 권고 본문 반영, 단계 (4) 직접 적용) |

### 1.3 R-19 답습 trigger 정확한 form 4 단계 chain ((g1-N-3) cycle)

| 단계 | 산출 | commit |
|---|---|---|
| (1) 사용자 명시 + 범위 선택 | "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 통합 평가 | (사용자 메시지) |
| (2) entry brief v1 (현재) | 본 문서 | (본 commit) |
| (3) 풀 3+1 합의 | Agent A/B/C 병렬 → Reviewer 통합 | (별도 commit) |
| **(4) brief v1.1 보강 + CLAUDE.md/roadmap.md 정정 단일 atomic commit** | brief v1.1 + CLAUDE.md + roadmap.md 본문 변경 | (별도 commit) |

### 1.4 R-9 답습 영구 의무 7 항목 본 cycle 직접 적용 자격 평가 (하위 layer 정합 정정 차원)

| 항목 | 본 cycle 적용 자격 |
|---|---|
| **(1) 사용자 명시** | "(g1-N-3)" + (β) + 정공법 + (g1-N-3') 통합 평가 ✅ |
| **(2) 풀 3+1 합의** | 본 cycle 합의 진행 *예정* (단계 (3)). **본 cycle = *하위 layer 정합 정정* 차원, R-9 (2) 헌법급 변경 합의 의무의 *간접 확장 답습*** (R-9 (2) 직접 모법 = 헌법 본문 변경, 본 cycle = 헌법 본문 변경 결과 *반영* 의 하위 의존 정합) |
| **(3) Reviewer 권한 한계 8 → 9 항목 영구 답습** | §6.3 + **(9) 신규 — CLAUDE.md / roadmap.md 본문 정정 자격** (R-7 답습 8 → 9 격상, R-13 (4-c) 동형 패턴 답습) |
| **(4) ADR-011 §2.1 (a)~(e) 답습 자격 평가** | (e) 후속 패턴 *제안* — 본 cycle 합의 BLOCKING verbatim 본문 직접 반영 의무 답습. (a)~(d) 적용 자격 = CLAUDE.md / roadmap.md 정정 자체가 헌법급 변경 *결과 반영* 이므로 *간접 적용* (R-9 (4) 직접 모법 = 헌법 본문 변경 시) |
| **(5) ADR-008 부록 B Amendment 패턴 (R-S3 답습 영구 — 형식 유사성)** | **본 cycle = (g1-N-1)/(g1-N-2) 의 하위 의존 정합 정정**, ADR-008 부록 B Amendment 동시 발행 형식 모법 *간접 적용* (ADR-011 line 7 "동시 발행" = 최초 발행 시점 한정, R-18 답습) |
| **(6) 자동 amendment 발의 0건** | 본 cycle 합의 채택 + 사용자 명시 후 brief v1.1 + CLAUDE.md + roadmap.md 단일 atomic commit (자동 발효 0건) ✅ |
| **(7) 본 cycle = *하위 의존 정합 정정 cycle*** | **R-9 답습 *간접 확장*, 헌법급 변경 *직접 적용 아님*** — (g1-N-1) `148fbbe` + (g1-N-2) `3bdb1be` 결과 *반영* cycle |

**§1.4 R-9 7 항목 ↔ §6.3 Reviewer 권한 한계 9 항목 통합 매핑** (R-31 + R-9 답습 어휘 보강): R-9 (3) Reviewer 권한 한계 1 항목 = §6.3 9 항목의 *상세 분해* 형식 통합 매핑. 수치 비대칭 (7 ≠ 9) = *분해 매핑* 형식 답습.

---

## 2. evidence 통합

### 2.1 (g1-N-2) 합의 (`07cd3f4`) + (g1-N-1) 합의 (`77f36cf`) + (g1-N) 합의 (`1ec9c5e`) carry-over (R-22 답습)

| cycle | 산출 | 본 (g1-N-3) 답습 의무 |
|---|---|---|
| (g1-N) | BLOCKING 22 + 권고 17 + NOTE 25 + Reviewer 단독 격상 5 | by-reference carry-over only (R-26 답습) |
| (g1-N-1) | BLOCKING 14 + 권고 12 + NOTE 14 + Reviewer 단독 격상 4 + **헌법 본문 변경 commit `148fbbe`** | 본 cycle 변경 결과 *반영* 의 직접 trigger |
| (g1-N-2) | BLOCKING 10 + 권고 10 + NOTE 11 + Reviewer 단독 격상 3 + **ADR-011 본문 변경 commit `3bdb1be`** | 본 cycle §12.2 #5 (g1-N-3) carry-over 직접 trigger |

### 2.2 헌법 5조-2 신설 line 75~80 verbatim (R-1 + R-S1 답습 영구)

```
line 75   ## 제5조-2: Provider Liquidity 원칙 (비협상)
line 76   
line 77   1. 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다 — 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 코드 변경 없이 가능해야 한다 (메모리 line 7 답습)
line 78   2. LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만 — 모델명·provider 분기 코드는 금지 (메모리 line 12 답습)
line 79   3. 단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙 (메모리 line 14 답습)
line 80   4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**
```

**🔴 line 80 임시 stale 신규 발효 (R-S2 carry-over 영구)** — line 80 verbatim 인용 "헌법 제5조 (Provider Liquidity)" ≠ ADR-011 line 6 현재 본문 verbatim "헌법 제5조-2 (Provider Liquidity, 비협상)". **본 (g1-N-3) cycle 정정 자격 0** (R-9 헌법 본문 변경 답습 영구 의무, (g1-N-3') 별도 cycle 의무).

### 2.3 CLAUDE.md 본문 현재 헌법 5조-2 신설 사실 미반영 식별 (R-1 답습)

**현재 line-level cross-check** (8 cycle 통합 정리 `3f84c26` 시점):

| CLAUDE.md 위치 | 현재 본문 | 본 cycle 정정 후보 자격 |
|---|---|---|
| §1 SDD 답습 의무 | 변경 0건 (5조-2 명시 부재) | (i) 명시 추가 후보 |
| §7 문서 의존 관계 표 (line 219~228 부근) | 헌법 5조-2 신설 → 의존 항목 추가 미반영 | (i) 의존 항목 추가 후보 (예: "헌법 5조-2 수정 시 → ADR-011 §6 line 6/245 + 본 §8 참조 표 + roadmap.md GP-2~6 entry 교차 확인") |
| §8 참조 문서 표 line 233 | 헌법 본문 line 참조 미포함 (조 번호 인용만) | (i) 5조-2 강조 entry 추가 후보 |
| §8 참조 문서 표 line 244 ADR-011 entry | "**수단/목적 분리 원칙** \| `docs/decisions/ADR-011-means-vs-ends-redaction.md` \| **헌법 8조 본질 = 안전 결과. R-4~R-7 모법, ...**" | (i) "헌법 8조 본질" → "헌법 8조 본질 + 5조-2 (Provider Liquidity, 비협상) 상위 권위 매핑" 보강 후보 |
| 기타 본문 | 5조-2 reference 부재 | (iv) 광범위 정정 후보 |

### 2.4 roadmap.md 본문 현재 "Provider Liquidity" 인용 광범위 stale 식별 (R-1 답습)

**현재 grep 결과 (297줄 전체 검색, "Provider Liquidity" 인용 위치 10+ 곳)**:

| roadmap.md 위치 | 현재 본문 발췌 | 본 cycle 정정 후보 자격 |
|---|---|---|
| **line 61** | "**G2** \| **GP-2 Egress Redaction** ... (P2 헌법 8조 위반 경로)" | 8조 only — 5조-2 reference 추가 *불필요* (Provider Liquidity 직접 무관) |
| **line 62** | "**GP-3 Credential / Secret Hygiene** ... (P3 + P4 헌법 8조 위반 경로)" | 8조 only — 5조-2 직접 무관 |
| **line 63** | "**GP-4 External Input Validation** ... (P5 헌법 8조 #3)" | 8조 only |
| **line 64** | "**GP-5 Provider Adapter Enforcement** (코드 lock-in 차단) ... \| **HIGH** (**Provider Liquidity 5-way Layer 1 모법**)" | "Provider Liquidity" → "**헌법 5조-2 Provider Liquidity** 5-way Layer 1 모법" reference 추가 후보 (i) |
| **line 65** | "**GP-6 Memory / Skill Migration Feasibility** ... \| **MEDIUM** (P8 + **Provider Liquidity Layer 4 — Provider 교체 자유**)" | 동일 reference 추가 후보 (i) |
| **line 111** | "**G4 Round-trip validation PoC** ... (**Provider Liquidity Layer 4** — JSONL Hermes 의존 0)" | 동일 reference 추가 후보 (i) |
| **line 114** | "**G4 Memory/Skill schema validation** ... (**Provider Liquidity Layer 3**)" | 동일 reference 추가 후보 (i) |
| **line 137** | "**1** \| **G2 GP-5 Provider Adapter Enforcement** ... HIGH 보안 (**Provider Liquidity 5-way Layer 1 모법**)" | 동일 reference 추가 후보 (i) |
| **line 142** | "**3 (tie)** \| **G4 Round-trip validation PoC** ... HIGH (**Provider Liquidity Layer 4**)" | 동일 reference 추가 후보 (i) |
| **line 146** | "**6 (tie)** \| **G4 Memory/Skill schema validation** ... MEDIUM (**Provider Liquidity Layer 3**)" | 동일 reference 추가 후보 (i) |
| **line 147** | "**7** \| **G2 GP-6 Memory/Skill Migration Feasibility** ... MEDIUM (**Provider Liquidity Layer 4**)" | 동일 reference 추가 후보 (i) |

**🔴 정정 *불필요* 위치 명문** (R-1 답습 — 분류 기준 명시):
- line 61~63 GP-2~4 = **헌법 8조 직접 모법, Provider Liquidity 직접 무관** → 정정 0건 자격
- line 64~65 + line 111/114/137/142/146/147 = **Provider Liquidity 직접 인용**, 5조-2 reference 추가 자격 (i)~(iv) 후보

### 2.5 ADR-011 line 6 + line 245 현재 verbatim (R-S1 답습 영구 — (g1-N-2) `3bdb1be` 결과 유지)

```
line 6     **상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
line 245   - `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)
```

**본 cycle 변경 0건** (ADR-011 = (g1-N-2) 결과 유지, **ADR-011 line 212 본문 정정 = (g1-O) 별도 cycle 의무** carry-over).

### 2.6 ADR-011 + 헌법 + (g1-N-1)/(g1-N-2) + 본 cycle Reviewer 권한 한계 (9) 신규 boundary 명문 (R-7 + R-11 + R-13 답습)

**Reviewer 권한 한계 영구 답습 chain**:
- (1) ADR-011 §6 본문 정정 자격 = (g1-N-2) cycle 예외 자격 발효 직접 적용 완료
- (4) 헌법 본문 정정 자격 = (g1-N-1) cycle 예외 자격 발효 직접 적용 완료, **헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무**
- **(9) 신규 — CLAUDE.md / roadmap.md 본문 정정 자격 = 본 (g1-N-3) cycle 합의 채택 + 단일 atomic commit 시점 *예외 자격* 발효 (R-13 (4-c) 동형 패턴 답습 + (1) (4) chain 답습)**

### 2.7 16 영향 문서 carry-over by-reference only (R-15 답습 신규 강화)

- `governance-preconditions.md` — 광범위 "헌법 5조 (Provider Liquidity)" 관용 표현 (§1.1 자체가 명명 정정 본문, line 26~96/108/803 등)
- `implementation-runtime-roadmap.md` (본 cycle 정정 대상 2) ✓
- `hermes-adoption-design.md` / `hermes-adoption-design-v3.md`
- `system-identity-prequel.md`
- `llm-providers-design.md`
- `mvp-1-to-6-entry-conditions-brief.md`
- `provider-agnostic-memory-skill-design.md`
- `hermes-not-root-of-trust-runtime.md`
- ADR-008 / ADR-009 / ADR-010 / ADR-012
- **본 cycle 범위 외, 별도 cycle 의무** (사용자 명시 (β) 범위 boundary)
- 후보 별도 cycle 명: (g1-N-3-gov) / (g1-N-3-hermes) / (g1-N-3-adr-series) 등 — **본 cycle 합의 결과 carry-over** 자격

---

## 3. SDD 정합성 매트릭스

### 3.1 CLAUDE.md / roadmap.md 본문 변경 정합성 (본 cycle 변경 결과 예정)

| 위치 | 본 cycle 변경 자격 |
|---|---|
| **CLAUDE.md §1 SDD** | 5조-2 명시 추가 후보 (i)~(iv) |
| **CLAUDE.md §7 의존 표** | 헌법 5조-2 의존 entry 추가 후보 (i)~(iv) |
| **CLAUDE.md §8 참조 표 line 233** | 5조-2 강조 후보 (i)~(iv) |
| **CLAUDE.md §8 line 244 ADR-011 entry** | "헌법 8조 본질" → "헌법 8조 + 5조-2 본질" 보강 후보 (i)~(iv) |
| **roadmap.md line 64/65/111/114/137/142/146/147** | "Provider Liquidity" → "헌법 5조-2 Provider Liquidity" reference 추가 후보 (i)~(iv) |
| roadmap.md line 61~63 (GP-2~4 헌법 8조 only) | 변경 0건 자격 (R-1 답습 분류 기준 명시) |

### 3.2 헌법 본문 변경 자격 0 + 헌법 line 80 임시 stale carry-over (R-S2 영구)

- 헌법 line 40~46 (5조 "코드 품질 원칙") — 변경 0건
- 헌법 line 75~80 (5조-2 신규, (g1-N-1) commit 결과 유지) — 변경 0건
- **헌법 line 80 임시 stale** — 본 cycle 변경 0건, **(g1-N-3') 별도 cycle 의무** carry-over (R-S2 격상 영구)
- 헌법 line 104~105 (종결 명문, R-S1 답습 영구) — 변경 0건

### 3.3 ADR-011 본문 변경 자격 0 + ADR-011 line 212 carry-over

- ADR-011 line 6 + line 245 — (g1-N-2) 결과 유지, 변경 0건
- ADR-011 line 212 ("Provider Liquidity 영향 \| 무관") — 변경 0건, **(g1-O) 별도 cycle 의무** carry-over

### 3.4 MVP-1 + 메모리 + ADR-008 본문 변경 자격 0

- MVP-1 R4 by-reference carry-over only (R-6 + R-20 답습)
- 메모리 line 7 + line 12~17 by-reference 답습, **MEMORY.md 9.4% over R-S4 carry-over depth 3 cycle 누적** (R-7 cleanup cycle 우선순위 carry-over 강화)
- ADR-008 부록 B B.1~B.6 by-reference only (R-S3 답습 영구)

### 3.5 16 영향 문서 변경 자격 0 (사용자 명시 (β) 범위 boundary)

본 cycle 범위 = CLAUDE.md + roadmap.md only. 16 영향 문서 = **본 cycle 합의 결과 carry-over** 자격, 본 cycle 본문 변경 0건.

---

## 4. CLAUDE.md / roadmap.md 정정 본문 후보 매트릭스 (채택 자격 0, 합의 *후* 사용자 명시 의무)

### 4.1 본문 후보 (i)~(iv) 변경 강도 매트릭스

| 후보 | CLAUDE.md 변경 | roadmap.md 변경 | 강도 | 채택 자격 |
|---|---|---|---|---|
| **(i) 최소 정정** | §8 line 244 ADR-011 entry "헌법 8조 본질" → "헌법 8조 + 5조-2 본질" 만 | line 64/65 GP-5/6 "Provider Liquidity" → "헌법 5조-2 Provider Liquidity" 만 | 약 | 본 cycle 합의 채택 자격 평가 *입력 only* |
| **(ii) 중간 정정** | §7 의존 표 5조-2 entry 추가 + §8 line 244 보강 | line 64/65/111/114/137/142/146/147 모두 "헌법 5조-2 Provider Liquidity" reference 추가 | 중 | 동일 |
| **(iii) 최대 정정** | §1 SDD + §7 의존 표 + §8 참조 표 line 233 강조 + line 244 보강 모두 | (ii) 동일 + 본문 다른 "Provider Liquidity" 인용 모두 정정 | 강 | 동일 |
| **(iv) 광범위 정정** | (iii) 동일 | (iii) 동일 + 16 영향 문서 일부 포함 | 매우 강 | **사용자 명시 (β) 범위 boundary 위반 risk** (R-15 답습), 채택 자격 0 |

**🔴 (iv) 채택 자격 boundary 명문** (R-15 답습): 사용자 명시 (β) = CLAUDE.md + roadmap.md only. (iv) 광범위 = boundary 위반, 본 cycle 채택 자격 0. 별도 cycle 분리 의무.

### 4.2 본문 후보의 본 cycle 채택 자격 boundary (R-15 답습 신규)

- (i)~(iii) = 본 cycle 합의 채택 자격 *평가* 대상 (사용자 명시 (β) 범위 내)
- (iv) = boundary 위반, 본 cycle 채택 자격 0 (별도 cycle 의무)
- **합의 후 사용자 명시** 후 단일 atomic commit 시점에 (i)~(iii) 중 1 후보 채택

### 4.3 본 cycle 범위 boundary 명문 (사용자 명시 단독 발효, R-15 답습 신규)

- CLAUDE.md = §1 SDD + §7 의존 표 + §8 참조 표 (line 233 + line 244) 만 명시
- roadmap.md = line 64/65/111/114/137/142/146/147 만 명시 (line 61~63 GP-2~4 = 헌법 8조 only, Provider Liquidity 직접 무관 → 변경 0건 자격)
- **16 영향 문서 = 본 cycle 범위 외, 별도 cycle 의무**
- **부분 정정 자격 0** (R-10 + R-7 *대칭* 답습) — (i)~(iii) 중 1 후보 채택 시 *부분* 적용 자격 0, 전체 atomic 적용 의무

---

## 5. 핵심 긴장 분석 (4 긴장)

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

### 5.4 긴장 4 — Reviewer 권한 한계 (9) 신규 boundary (R-7 + R-11 + R-13 답습)

- **(9) 신규**: CLAUDE.md / roadmap.md 본문 정정 자격 = 본 cycle 합의 채택 + 단일 atomic commit 시점 *예외 자격* 발효 (R-13 (4-c) 동형 패턴)
- (1) (4) chain 답습 = (g1-N-2) (1) ADR-011 §6 예외 발효 + (g1-N-1) (4) 헌법 본문 예외 발효 + 본 cycle (9) CLAUDE.md/roadmap.md 예외 발효
- **(9-a)** Reviewer 가 (i)~(iv) 후보 채택 자격 BLOCKING 발의 = 본 cycle *제안* 범위 내 (자격 충족)
- **(9-b)** Reviewer 가 *현 CLAUDE.md / roadmap.md 다른 부분* 정정 권고 = 자격 0 (별도 cycle 의무)
- **(9-c)** Reviewer 가 *합의 후 단계 본문 정정 시점* 의 verbatim 본문 권고 = 본 cycle 합의 채택 자격 + 사용자 명시 *후* 자격 발생
- **(9-d)** "사용자 명시 *전* 단계 (Reviewer 합의 산출 후 + 사용자 명시 *전*)" sub-boundary — (g1-N-2) (1-d) 답습 (R-11 답습)

---

## 6. 3+1 합의 분담안

### 6.1 Agent + Reviewer 분담 + 핵심 질문

| 에이전트 | 관점 | 핵심 질문 |
|---|---|---|
| **Agent A (구현 분석가)** | "정합 정정이 실제로 동작하는가?" | Q-A1: CLAUDE.md / roadmap.md 정정 후보 (i)~(iv) 중 어느 강도가 헌법 5조-2 신설 사실 *정합 회복*에 충분한가? / Q-A2: roadmap.md line 61~63 (GP-2~4) 정정 0건 자격이 R-1 답습 분류 기준에 부합하는가? / Q-A3: line 244 ADR-011 entry 보강 표현이 (g1-N-2) 결과와 정합한가? |
| **Agent B (품질·안전성 검증가)** | "정합 정정이 안전하고 견고한가?" | Q-B1: 본 brief §0 12 ↔ §10.1 12 1:1 매핑 self-consistency? / Q-B2: Reviewer 권한 한계 (9) 신규 boundary 가 (1)(4) chain 과 정합한가? / Q-B3: 16 영향 문서 carry-over self-citation anchor 차단 충족? / Q-B4: (g1-N-3') 통합 *평가* vs *해결* 분리 boundary 명문 충족? / Q-B5: 헌법 line 80 임시 stale R-S2 carry-over 답습 충족? |
| **Agent C (대안 탐색가)** | "더 나은 정합 정정 방법이 있는가?" | Q-C1: 본 후보 (i)~(iv) 외 다른 정정 후보 식별? (예: 본문 변경 0건 + comment block 추가 / CLAUDE.md 만 / roadmap.md 만) / Q-C2: 16 영향 문서 carry-over 우선순위 권고? / Q-C3: 본 cycle 자격 자체 대안 framing (예: (g1-N-3α) only / (g1-N-3β) only / 통합) / Q-C4: Reviewer 권한 한계 (9) 신규 boundary 의 (1)(4) chain 답습 외 다른 모법 식별? / Q-C5: anchor depth limit cycle 진입 trigger 명문 자격 carry-over |
| **Reviewer (검토 에이전트)** | "최선의 합의는?" | Q-R1: 3 에이전트 출력 교차 비교 + 일치/부분 일치/불일치/누락 분류 / Q-R2: BLOCKING / 권고 / NOTE 분류 (R-26 답습) / Q-R3: Reviewer 단독 격상 자격 평가 (R-S1+ 답습) / Q-R4: raw line-level direct cross-check (R-1 + R-S1 답습 영구) |

### 6.2 분담 의무 (R-22 답습)

- 3 Agent 병렬 독립 (편향 방지 — 헌법 4조 #3)
- 본 brief v1 본문 + 선행 답습 chain 8 cycle + 메모리 본문 + 현재 CLAUDE.md / roadmap.md / 헌법 / ADR-011 본문 cross-check
- Reviewer = 3 에이전트 출력 + raw line-level cross-check (R-1 + R-S1 답습 영구)
- 본 cycle 합의 결과 BLOCKING / 권고 / NOTE / Reviewer 단독 격상 분류 명문 (R-26 답습)

### 6.3 Reviewer 권한 + 한계 (R-14 + R-7 답습 — 9 항목 영구 명문 + (9) 신규 예외 자격 발효 발의 자격)

> **Reviewer 권한 한계 9 항목 출처 chain** (R-7 답습): Provider Liquidity → format → (g1-A) → (g1-N) → (g1-N-1) → (g1-N-2) → 본 (g1-N-3) brief §6.3 (**7 cycle carry-over chain**).

> Reviewer 권한 = brief v1 진술 BLOCKING 정정 권한 + **본 cycle 합의 채택 시 CLAUDE.md / roadmap.md 본문 정정 자격 (9) 신규 예외 발효 발의 자격 — 단일 atomic commit 시점 적용**.

**9 권한 한계 영구 답습 + (9) 신규 예외 자격 발의 자격 + (9-a)~(9-d) sub-boundary**:

1. **ADR-011 §6 본문 정정 자격 = (g1-N-2) cycle 예외 자격 발효 직접 적용 완료** ((1-a)~(1-d) 답습)
2. Provider Liquidity 본질 약화 자격 0
3. MVP-1 합의 본문 정정 자격 0
4. **헌법 본문 정정 자격 = (g1-N-1) cycle 예외 자격 발효 직접 적용 완료**, 헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무
5. 메모리 본문 정정 자격 0
6. 4 가족 분류 + 6축 framing 영구 정착 자격 0
7. 자동 다음 단계 진입 자격 0
8. 결합 cycle 진입 자격 평가 자격 0
9. **신규 — CLAUDE.md / roadmap.md 본문 정정 자격 = 본 (g1-N-3) cycle 합의 채택 + 사용자 명시 *후* 단일 atomic commit 시점 *예외 자격* 발효 (R-13 (4-c) 동형 패턴 답습)**.
   - **(9-a)** Reviewer 가 (i)~(iv) 후보 채택 자격 BLOCKING 발의 = 본 cycle *제안* 범위 내 (자격 충족) ✅
   - **(9-b)** Reviewer 가 *현 CLAUDE.md / roadmap.md 다른 부분* 정정 권고 = 자격 0 (별도 cycle 의무 (g1-N-3-gov)/(g1-N-3-hermes)/(g1-N-3-adr-series)) ✅
   - **(9-c)** Reviewer 가 *합의 후 단계 본문 정정 시점* 의 verbatim 본문 권고 = 본 cycle 합의 채택 자격 + 사용자 명시 *후* 자격 발생 ✅
   - **(9-d)** "사용자 명시 *전* 단계 (Reviewer 합의 산출 후 + 사용자 명시 *전*)" sub-boundary — (g1-N-2) (1-d) 답습 (R-11 답습) ✅

---

## 7. 합의 출력 형식

### 7.1 합의 보고서 형식 (carry-over)

- 합의 보고서 = `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-3-claude-md-roadmap-md-correction.md` (예정)
- BLOCKING / 권고 / NOTE / Reviewer 단독 격상 분류
- 3 에이전트 일치 / 부분 일치 / 불일치 / 누락 표
- (g1-N-2) 합의 패턴 답습

### 7.2 raw line-level cross-check 의무 (R-1 + R-S1 답습 영구)

- **본 (g1-N-3) brief v1** (본 문서)
- 본 cycle 합의 보고서 (예정)
- **`CLAUDE.md` 현재 본문** — 본 cycle 변경 대상 1
- **`docs/architecture/implementation-runtime-roadmap.md` 현재 본문** — 본 cycle 변경 대상 2
- `docs/constitution/PROJECT_CONSTITUTION.md` line 75~80 (5조-2 신설 본문) + **line 80 (R-S2 임시 stale carry-over)** + line 104~105
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` line 6 + line 245 (R-S1 답습 영구) + line 212 ((g1-O) carry-over)
- ADR-008 부록 B B.1~B.6 by-reference (R-S3 답습)
- 메모리 `feedback_provider_liquidity` line 7 + line 12~17 verbatim
- (g1-N-2) brief v1.1 + 합의 보고서 (`3bdb1be` + `07cd3f4`)
- (g1-N-1) brief v1.1 + 합의 보고서 (`148fbbe` + `77f36cf`)
- (g1-N) brief v1.1 + 합의 보고서 (`58e06d5` + `1ec9c5e`)

---

## 8. 후속 결정 권고 옵션 매트릭스 (권고 자격 only, 결정 *고정* 0)

### 8.1 본 (g1-N-3) 적용 후 별도 단계

| 단계 | 내용 | 자격 |
|---|---|---|
| (1) 본 brief v1 + commit | 본 commit (현재) | ✅ |
| (2) 풀 3+1 합의 | 별도 commit | 사용자 명시 "(A)" 후 |
| (3) brief v1.1 + CLAUDE.md/roadmap.md 정정 atomic commit | 별도 commit (Reviewer 권한 한계 (9) 신규 예외 자격 발효) | 사용자 명시 후 |
| (4) 세션 정리 | SESSION + CONTEXT + INDEX | 사용자 명시 후 |

### 8.2 (g1-N-3) carry-over

| 후속 cycle | 우선순위 | 자격 |
|---|---|---|
| **(g1-N-3')** ⭐⭐ 헌법 line 80 임시 stale 정정 cycle (R-S2 carry-over 영구) | **HIGH** | R-9 헌법 본문 변경 답습 영구 의무, 사용자 명시 의무 |
| **(g1-N-3-gov)** governance-preconditions.md §1.1 + line 26~96/108/803 정합 정정 | MEDIUM | 광범위 정정 cycle, 별도 합의 의무 |
| **(g1-N-3-hermes)** hermes-adoption-design.md + v3 + system-identity-prequel.md + hermes-not-root-of-trust-runtime.md 정합 정정 | MEDIUM | hermes 시리즈 통합 cycle |
| **(g1-N-3-adr-series)** ADR-008/009/010/012 정합 정정 | MEDIUM | ADR 시리즈 통합 cycle |
| **(g1-N-3-llm-providers)** llm-providers-design.md + provider-agnostic-memory-skill-design.md + mvp-1-to-6-entry-conditions-brief.md 정합 정정 | LOW | 별도 cycle |
| **(g1-O)** ADR-011 line 212 본문 미세 보강 | MEDIUM | (g1-N-2) carry-over |
| **MEMORY.md cleanup cycle** (R-S4 정량 9.4% over depth 3 cycle 누적) | HIGH | R-7 답습 |
| anchor depth limit cycle 진입 trigger 명문 | LOW | R-22 답습 carry-over |

### 8.3 DEFER / 기각 옵션 (R-30 + R-24 *대칭* 답습) — 본 cycle 적용 완료 후 carry-over only

- (gN-3-D1) DEFER 자격 — 본 cycle 부분 채택 / 부분 DEFER 시 R-9 답습 영구 의무 미충족 risk (carry-over only, 채택 자격 0)
- (gN-3-D2) 기각 자격 — 본 cycle 후보 (i)~(iii) 모두 기각 시 (g1-N-1)/(g1-N-2) 결과 정합 회복 미충족 risk (carry-over only, 채택 자격 0)
- 변형 — (i) 최소 정정 채택 후 (ii)/(iii) carry-over (R-30 답습 대안 input only)

---

## 9. 정직성 한계 (18 항목)

1. 본 brief v1 = 진단·자격 평가 only, 실 변경 0건 (R-15 답습)
2. (i)~(iv) 4 후보 = 본 cycle 채택 자격 0, 합의 *후* 사용자 명시 의무
3. R-9 답습 = 본 cycle *간접* 적용 (헌법 본문 변경 직접 적용 아님, 하위 의존 정합 정정 차원)
4. Reviewer 권한 한계 (9) 신규 boundary = 본 cycle 합의 채택 + 단일 atomic commit 시점만 예외 자격 발효
5. (g1-N-3') 별도 cycle 의무 carry-over = 본 cycle 통합 *평가* 자격만, *해결* 자격 0 (사용자 명시 단독 발효)
6. 16 영향 문서 = 본 cycle 범위 외, 별도 cycle 의무 (사용자 명시 (β) 범위 boundary)
7. R-S2 헌법 line 80 임시 stale carry-over 영구 답습
8. R-S3 "비협상" 명문 추가 boundary 답습 (헌법 line 75 + ADR-011 line 6 verbatim 직접 답습)
9. R-S1 line 245 entire verbatim 답습 (R-1 답습 영구)
10. R-S4 MEMORY.md 9.4% over depth 3 cycle 누적 — cleanup cycle 우선순위 강화 carry-over
11. R-S5 §0 ↔ §10.1 1:1 매핑 self-consistency 답습 (12 ↔ 12)
12. (9-d) 신규 sub-boundary "사용자 명시 *전* 단계" boundary (R-11 답습)
13. 본 brief framing 임시 framing 명문, 영구 정착 자격 0 (R-12 답습)
14. ADR-011 line 212 ((g1-O) carry-over) 본 cycle 변경 0건
15. 본 cycle = 9번째 cycle entry, brief progression chain anchor depth limit cycle 진입 trigger 명문 부재 carry-over (R-22)
16. 본 cycle 합의 채택 자격 평가 0건, 합의 *후* Reviewer 권한 한계 (9) 신규 예외 자격 발효 시점에만 적용
17. CLAUDE.md / roadmap.md 정정 = 헌법급 변경 *결과 반영* 의 하위 의존 정합 정정 (R-9 직접 적용 아님)
18. 본 brief v1 488줄 → brief v1.1 ~570줄 (예상, BLOCKING + 권고 + NOTE + R-S 격상 verbatim 본문 직접 반영)

---

## 10. 차단 조건 (§0 12 항목 1:1 매핑 — R-15 = R-S3 + R-S5 답습 영구)

### 10.1 본 brief 가 자동 발효시키지 않는 것

1. ❌ **CLAUDE.md 본문 자동 정정** — 본 brief v1 = 진단·자격 평가 only
2. ❌ **roadmap.md 본문 자동 정정** — 동일 답습
3. ❌ **헌법 본문 자동 정정** — (g1-N-1) 결과 유지, line 80 = (g1-N-3') 별도 cycle 의무
4. ❌ **ADR-011 본문 자동 정정** — (g1-N-2) 결과 유지, line 212 = (g1-O) 별도 cycle 의무
5. ❌ **MVP-1 합의 본문 자동 정정**
6. ❌ **메모리 본문 자동 정정** — line 7 + line 12~17 by-reference only, MEMORY.md cleanup carry-over
7. ❌ **ADR-008 본문 자동 정정** — 부록 B by-reference only
8. ❌ **16 영향 문서 자동 정정** — 사용자 명시 (β) 범위 boundary, 별도 cycle 의무
9. ❌ **Provider Liquidity 본질 약화** — binary 본질 유지
10. ❌ **본 brief framing 영구 정착** (R-12 답습)
11. ❌ **본 brief 진단표 → 후속 cycle 정정 진입 근거화 *de facto* 압력** (R-29 답습 + R-S5 답습)
12. ❌ **본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 자격** 모두 0건 (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

### 10.2 합의 BLOCKING 처리 의무 (R-21 답습)

본 cycle 합의 결과 BLOCKING verbatim 본문 직접 반영 100% 의무 (brief v1.1 보강 시).

### 10.3 본 brief 진단표 → 후속 cycle 정정 진입 근거화 차단 (R-29 답습)

§2.3 + §2.4 + §3.1 + §4.1 진단표 = 본 cycle 합의 *입력* 자격만, 후속 cycle 의 *de facto* 정정 진입 근거화 자격 0.

### 10.4 본 cycle 합의 결과의 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 자격 0 (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

### 10.5 본 brief 의 4 긴장 framing self-citation anchor 차단 (R-2 + R-12 + R-29 + R-15 통합 답습)

### 10.6 본 brief 의 §3·§4·§5·§8 진단표 후속 cycle 인용 자격 (R-6 + R-S5 답습)

---

## 11. NOTE carry-over (80+ 항목, by-reference only — 80 carry-over + 본 cycle 신규)

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
| **9 (본 cycle)** | **(g1-N-3) CLAUDE.md / roadmap.md 정합 정정** | **(본 brief v1 commit)** / (합의 예정) / (brief v1.1 + CLAUDE.md/roadmap.md atomic commit 예정) |

### 11.2 본 cycle 신규 NOTE (예상, 합의 후 v1.1 보강 시 N-81~ 추가)

| NOTE | 내용 | 출처 |
|---|---|---|
| **N-81** | CLAUDE.md / roadmap.md = 하위 layer 정합 정정 cycle, R-9 헌법급 변경 *간접* 적용 carry-over | R-9 + R-S2 |
| **N-82** | Reviewer 권한 한계 (9) 신규 — CLAUDE.md / roadmap.md 본문 정정 예외 자격 발효 boundary (R-13 (4-c) 답습) | R-7 + R-11 + R-13 |
| **N-83** | (g1-N-3') 통합 *평가* vs *해결* 분리 boundary (사용자 명시) | R-S2 + R-9 |
| **N-84** | 16 영향 문서 carry-over self-citation anchor 차단 (R-12 + R-29) | R-12 + R-29 + R-15 |
| **N-85** | roadmap.md line 61~63 (GP-2~4) 정정 0건 자격 = 헌법 8조 only Provider Liquidity 직접 무관 (R-1 답습 분류 기준) | R-1 |
| **N-86** | 16 영향 문서 별도 cycle 후보 명 (g1-N-3-gov/hermes/adr-series/llm-providers) carry-over | R-30 |
| **N-87** | anchor depth limit cycle 진입 trigger 명문 부재 carry-over 9번째 cycle entry 도달 | R-22 + N-50 + N-80 |
| **N-88** | MEMORY.md 9.4% over R-S4 carry-over depth **3 cycle 누적** — cleanup cycle 우선순위 강화 | R-7 + R-S4 |
| **N-89** | brief v1.1 보강 시 (9-a)~(9-d) sub-boundary 직접 적용 결과 명문 carry-over | R-11 + (g1-N-2) (1-d) 답습 |
| **N-90** | Reviewer 단독 격상 자격 평가 R-S1+ 답습 (raw line-level direct cross-check) | R-S1 답습 영구 |

### 11.3 NOTE carry-over 정정 의무 (R-S1~R-S4 답습 영구)

- **R-S1 정정 chain carry-over**: raw line-level direct cross-check 답습 영구
- **R-S2 정정 답습**: 헌법 line 80 임시 stale carry-over 영구 의무 ((g1-N-3') 별도 cycle)
- **R-S3 정정 답습**: "비협상" 명문 추가 boundary 영구 답습
- **R-S4 정정 답습**: MEMORY.md cleanup cycle 우선순위 carry-over 영구 (depth 3 cycle 누적)
- **R-S5 정정 답습**: §0 ↔ §10.1 1:1 매핑 self-consistency 답습 영구

---

## 12. 변경 일람 표 + 다음 단계

### 12.1 변경 일람 표 (v1 → v1.1, 본 brief v1 작성 시점 placeholder)

본 brief v1 = 합의 *전* 상태. brief v1.1 보강 시 (단계 (4)) BLOCKING verbatim 본문 직접 반영 100% + 권고 본문 직접 반영 또는 §11 NOTE carry-over + 신규 NOTE 추가 + §12.1 변경 일람 표 신설 + Reviewer 단독 격상 verbatim 답습 영구.

### 12.2 다음 단계 (자동 진입 0건)

1. **본 brief v1 commit·push (현재)** — `docs(phase0): (g1-N-3) entry brief v1`
2. **사용자 검토 + "(A)" 명시 대기** — 본 commit 결과 확인 + 풀 3+1 합의 진입 자격 명시
3. 사용자 명시 → **풀 3+1 합의** — Agent A/B/C 병렬 독립 → Reviewer 통합 → APPROVE w/ COND / REVISE / 기각 분류
4. 사용자 명시 → **brief v1.1 + CLAUDE.md/roadmap.md 정정 단일 atomic commit** (Reviewer 권한 한계 (9) 신규 예외 자격 발효 직접 적용) — `docs(claude/roadmap): CLAUDE.md / roadmap.md 5조-2 정합 정정 (g1-N-3)` 또는 유사 commit message
5. 사용자 명시 → **세션 정리** — SESSION_2026-05-24.md + CONTEXT.md + INDEX.md 갱신
6. 후속 단계 = 사용자 명시:
   - **(g1-N-3')** ⭐⭐ 헌법 line 80 임시 stale 정정 cycle (R-S2 carry-over 영구)
   - **(g1-N-3-gov)** governance-preconditions.md 정합 정정 (광범위 cycle)
   - **(g1-N-3-hermes)** hermes 시리즈 정합 정정
   - **(g1-N-3-adr-series)** ADR-008/009/010/012 정합 정정
   - **(g1-N-3-llm-providers)** llm-providers 시리즈 정합 정정
   - **(g1-O)** ADR-011 line 212 본문 미세 보강
   - **MEMORY.md cleanup cycle** (R-S4 depth 3 cycle 누적 강화)
   - (g1-A) carry-over / (f-) / Phase 3 / 새 주제 / anchor depth limit cycle 진입 trigger 명문

**자동 다음 단계 진입 0건** (R-29 + R-30 + R-24 + R-7 *대칭* 답습).

---

**End of brief v1** (작성일 2026-05-24, (g1-N-3) cycle = brief progression chain **9번째 cycle entry**, R-19 답습 trigger 정확한 form 단계 (2) 직접 적용 = entry brief v1 작성 완료, R-9 답습 영구 의무 7 항목 본 cycle *간접* 적용 자격 평가, Reviewer 권한 한계 9 항목 영구 답습 + **(9) 신규 — CLAUDE.md / roadmap.md 본문 정정 자격 boundary** + (9-a)~(9-d) sub-boundary 신규, MVP-1·메모리·헌법·ADR-008·ADR-011 본문 변경 0건, **헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off carry-over (R-S2 격상 영구)** + (g1-N-3') 통합 *평가* 자격만 (사용자 명시 단독 발효), Provider Liquidity 본질 약화 자격 0 (5조-2 reference 추가 + "비협상" boundary 영구 답습 강화), 16 영향 문서 별도 cycle 의무 carry-over, 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 4 양방향 자격 0건)
