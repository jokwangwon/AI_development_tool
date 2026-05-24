# Jarvis MVP-1 (g1-N-2) cycle — ADR-011 line 6/245 매핑 정정 commit 자격 평가 합의 entry brief (v1.1, APPROVE w/ COND 반영 + ADR-011 본문 변경 동시 commit)

> **본 brief = (g1-N-2) 합의 cycle entry brief v1.1**. v1.1 = 풀 3+1 합의 (`07cd3f4`, APPROVE w/ COND, BLOCKING 10 + 권고 10 + NOTE 11, 기각 0, Reviewer 단독 격상 3 R-S1~R-S3) verbatim 본문 직접 반영 100% + **ADR-011 line 6/245 매핑 정정 *동시* 단일 atomic commit** (R-19 답습 단계 (4) 직접 적용, (g1-N-1) `148fbbe` 답습 패턴). 본 commit = **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit** (Reviewer 권한 한계 (1) 예외 자격 발효 시점). 사용자 명시 — "(g1-N-2)" + 정공법 + 단독 범위 + "brief v1.1 보강 + ADR-011 line 6/245 단일 atomic commit 진입". staged: brief v1 (`8207f55`, 488줄) → 풀 3+1 합의 (`07cd3f4`, 303줄) → **brief v1.1 + ADR-011 line 6/245 매핑 정정 단일 atomic commit (본 commit)** → 세션 정리. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-24 ((g1-N-1) commit `148fbbe` 직후, (g1-N-2) cycle = brief progression chain **7번째 cycle entry**, R-19 답습 단계 (4) 직접 적용, ADR-011 본문 변경 동시 commit)
**카테고리**: 합의 cycle entry brief v1.1 ((g1-N-2) ADR-011 line 6/245 매핑 정정 commit, **R-19 답습 trigger 정확한 form 단계 (4) 직접 적용 + Reviewer 권한 한계 (1) 예외 자격 발효 시점**)

**합의 답습 (R-21 + R-22 + R-9 영구 의무)**:
- 본 cycle 합의 (`07cd3f4`) BLOCKING 10 본문 직접 반영 100% (R-21 답습)
- 본 cycle 합의 권고 10 본문 직접 반영 또는 §11 NOTE carry-over
- 본 cycle 합의 NOTE 11 (N-70~N-80) §11.2 신설 (R-26 답습)
- **Reviewer 단독 격상 3 (R-S1~R-S3) verbatim 본문 직접 반영 영구 의무**:
  - **R-S1** (line 245 verbatim entire 부분 추출 정정) — §2.2/§2.3/§4.2 entire verbatim 명시 + §2.4 양방향 trade-off
  - **R-S2** (헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off 신규 발효) — §2.4 양방향 + §9 신규 항목 (g1-N-3') carry-over
  - **R-S3** ("비협상" 명문 추가 boundary) — §4.1 evidence 보강

**선행 답습**:
- `docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md` v1 (`8207f55`, 488줄)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md` (본 cycle 합의, `07cd3f4`, 303줄)
- `docs/phase0/jarvis-mvp1-g1-n-1-constitution-article-5-2-body-change-commit-consensus-entry-brief.md` v1.1 (`148fbbe`) — (g1-N-1) cycle 모법
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-1-constitution-article-5-2-body-change-commit.md` ((g1-N-1) 합의, `77f36cf`)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` **(본 commit 으로 변경 — line 6 "헌법 제5조-2 (Provider Liquidity, 비협상)" + line 245 "제5조-2 관용 (Provider Liquidity, 비협상)")**
- `docs/constitution/PROJECT_CONSTITUTION.md` line 75~81 (5조-2 신규) + **line 80 (R-S2 임시 stale carry-over 영구)** + line 104~105 (종결 명문, R-S1 답습 영구)
- 메모리 `feedback_provider_liquidity` line 7 + line 12~17 verbatim (MEMORY.md 9.4% over carry-over)

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것

### 하는 것 (12 항목, §10.1 와 1:1 매핑 의무 — R-15 = R-S3 + R-S5 답습)

1. **ADR-011 line 6 매핑 정정 적용**: "헌법 제5조 (Provider Liquidity)" → "**헌법 제5조-2 (Provider Liquidity, 비협상)**" (§2.3 + §4.1)
2. **ADR-011 line 245 매핑 정정 적용**: 변경 *전* "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)`" → 변경 *후* "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), **제5조-2 관용 (Provider Liquidity, 비협상)**`" (R-S1 격상 — entire verbatim 정정, §2.3 + §4.2)
3. **헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off 신규 발효 명문** (R-S2 격상 carry-over) — (g1-N-3') 또는 별도 cycle 의무 영구 carry-over (§2.4 + §9 항목 17)
4. **"비협상" 명문 추가 boundary** (R-S3 격상) — (i) reference 정정 + (ii) 헌법 line 75 verbatim 직접 답습 한정. 변형 A (brief default) 채택 정합 (§4.1 evidence 보강)
5. **본 cycle = R-19 답습 trigger 정확한 form 단계 (4) 직접 적용** — brief v1.1 + ADR-011 단일 atomic commit (본 commit) (§1.3 + §5)
6. **임시 stale 정합 회복 완료** ((g1-N-1) commit `148fbbe` 이래 ADR-011 line 6/245 *임시 stale* → 본 cycle commit 으로 정합 회복, N-61 carry-over 답습 완료) (§1.2 + §2.4)
7. **R-9 답습 영구 의무 7 항목 본 cycle 직접 적용 완료 + R-S1~R-S4 영구 답습 carry-over + R-S1~R-S3 본 cycle 신규 격상** (§1.4)
8. **Reviewer 권한 한계 (1) "ADR-011 §6 본문 정정 자격 0" 예외 자격 발효 직접 적용 완료** (R-13 (4-c) 동형 패턴) — (1-a)/(1-b)/(1-c) sub-boundary 명문 + (1-d) 사용자 명시 전 단계 (R-11 답습 신규) (§6.3)
9. SDD 정합성 매트릭스 + 본 cycle 변경 0건 항목 명문 (ADR-011 line 1~5 메타데이터 + line 240~244 + line 246~290, R-5 답습) (§3)
10. (g1-N-2) 적용 후 carry-over 옵션 매트릭스 (§8) — **(g1-N-3') 헌법 line 80 정정 cycle ⭐ 신규** + (g1-N-3) CLAUDE.md/roadmap + (g1-O) line 212 + MEMORY.md cleanup
11. 정직성 한계 (§9) — 18 항목, brief v1.1 보강
12. 차단 조건 (§10) — 12 항목 1:1 매핑 + **#10' 부분 정정 자격 0 추가** (R-10) + NOTE 80 carry-over (§11) + §12.1 변경 일람 + §12.2 다음 단계

### 하지 않는 것 (12 항목, §10.1 와 1:1 매핑 의무)

1. ❌ **ADR-011 line 212 본문 자동 정정** — (g1-O) 별도 cycle 의무
2. ❌ **CLAUDE.md §1 SDD + §7 의존 표 + §8 참조 표 + roadmap.md 자동 정정** — (g1-N-3) 별도 cycle 의무 (R-15 답습)
3. ❌ **헌법 본문 자동 정정** — (g1-N-1) commit 결과 유지. **헌법 line 80 임시 stale 정정 = (g1-N-3') 또는 별도 cycle 의무** (R-S2 carry-over 영구)
4. ❌ **ADR-008 부록 B 본문 자동 정정** (R-S3 답습) — by-reference only
5. ❌ **MVP-1 합의 본문 자동 정정** (R-6 + R-21 답습)
6. ❌ **메모리 본문 자동 정정 + 메모리 신규 entry 자동 등재** (R-13 + R-27 + R-S4 답습) — MEMORY.md 9.4% over carry-over depth 2 cycle 누적
7. ❌ **M3·M4 결정 *고정* + 코드 작성 + 새 측정·새 빌드·새 다운로드·sudo**
8. ❌ **Provider Liquidity 본질 약화** — 본 cycle = 매핑 정정 + "비협상" 명문 추가 (binary 본질 *강화* 방향), 약화 risk 0건 (R-4 답습)
9. ❌ **(g1-N-2) 자체의 영구화 정착** — cycle-specific, 후속 cycle (g1-N-3)/(g1-N-3')/(g1-O) 자유
10. ❌ **자동 채택 자격 0** (R-30 *대칭* 답습) + **결합 cycle 자동 진입 자격 0** (R-7 답습)
11. ❌ **본 brief 의 진단표 (§3·§4·§5) 가 후속 cycle 의 정정 *진입 근거* 가 되는 *de facto* 압력 발생** (R-29 + R-S5 답습)
12. ❌ **본 cycle 합의 결과의 *기각* + *자동 채택* + *결합 cycle 자동 진입* 3 양방향 자격도 자동 발효 0건** (R-30 + R-24 + R-7 *대칭* 답습) + **#10' line 6 만 또는 line 245 만 부분 정정 자격 0** (R-10 신규, 동시 정정 의무)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 trigger — 사용자 명시 "brief v1.1 + ADR-011 단일 atomic commit 진입" → R-19 답습 단계 (4) 직접 진입

본 cycle = (g1-N-1) commit `148fbbe` 후속 carry-over cycle. 사용자 명시 (본 brief v1.1 보강 시점, 본 cycle 합의 `07cd3f4` 채택 후) — "brief v1.1 보강 + ADR-011 line 6/245 단일 atomic commit 진입" → **R-19 답습 trigger 정확한 form 단계 (4) 직접 진입**:
- **단계 (4)**: brief v1.1 보강 + ADR-011 line 6/245 매핑 정정 **단일 atomic commit** (본 commit)
- **commit message** (Conventional Commits, R-8 답습): `docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)`
- **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit** (Reviewer 권한 한계 (1) 예외 자격 발효 시점)

### 1.2 본 cycle 의 핵심 결과 (R-19 답습 단계 (4) 직접 적용 완료)

| 변경 대상 | 변경 내용 | 결과 |
|---|---|---|
| **`ADR-011 line 6`** | "헌법 제5조 (Provider Liquidity)" → "**헌법 제5조-2 (Provider Liquidity, 비협상)**" | 매핑 정정 적용 ✅ |
| **`ADR-011 line 245` (entire verbatim, R-S1 격상)** | "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)`" → "`- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), **제5조-2 관용 (Provider Liquidity, 비협상)**`" | 매핑 정정 적용 ✅ |
| 임시 stale 자격 종료 (N-61 carry-over 완료) | ADR-011 line 6/245 정합 회복 | ✅ |
| **헌법 line 80 임시 stale 신규 발효** (R-S2 격상 carry-over) | 헌법 line 80 = ADR-011 line 6 변경 *전* verbatim 인용 → 변경 *후* line 6 ↔ 헌법 line 80 인용 verbatim 미정합 | **(g1-N-3') 별도 cycle 의무** |
| **본 brief v1.1** (본 문서) | v1 (488줄) → v1.1 (~700줄 예상) BLOCKING 10 verbatim 100% + 권고 10 + NOTE 11 신규 | 본 atomic commit 동시 |

### 1.3 R-19 답습 trigger 정확한 form 4 단계 완료 chain ((g1-N-2) cycle)

| 단계 | 내용 | 시점 | commit |
|---|---|---|---|
| (1) (g1-N-1) commit + 사용자 명시 "(g1-N-2)" | (g1-N-1) `148fbbe` + 사용자 명시 | 완료 | `148fbbe` (선행) |
| (2) (g1-N-2) entry brief v1 별도 작성 | brief v1 (`8207f55`, 488줄) | 완료 | `8207f55` |
| (3) 사용자 (A) 명시 + 풀 3+1 합의 | Agent A/B/C → Reviewer 통합 (`07cd3f4`, 303줄) | 완료 | `07cd3f4` |
| **(4) brief v1.1 보강 + ADR-011 line 6/245 매핑 정정 단일 atomic commit** | **본 v1.1 (현재) + ADR-011 본문 변경 (현재 완료)** | **본 commit (현재)** | **본 commit** |

### 1.4 R-9 답습 영구 의무 7 항목 본 cycle 직접 적용 완료 + R-S1~R-S3 본 cycle 신규 격상

| 항목 | 본 cycle 적용 결과 |
|---|---|
| **(1) 사용자 명시** | "(g1-N-2)" + 정공법 + 단독 범위 + "동시 atomic commit 진입" ✅ |
| **(2) 풀 3+1 합의 + R-S1 답습 영구 보강** | 본 cycle 풀 3+1 합의 `07cd3f4` APPROVE w/ COND. 헌법 line 105 verbatim "헌법 수정은 반드시 3+1 에이전트 합의" *재* 답습 — **본 cycle = ADR-011 본문 변경 차원, 헌법 line 105 = 헌법 본문 차원 직접 모법의 *일반 확장 답습*** (R-13 답습 어휘 boundary 명문 — line 110 통합 매핑) ✅ |
| **(3) Reviewer 권한 한계 8 항목 영구 답습** | §6.3 + (1) **"ADR-011 §6 본문 정정 자격 0" 예외 자격 발효 직접 적용 완료** (R-13 (4-c) 동형 패턴 + 본 cycle (1-d) 신규 — R-11 답습) ✅ |
| **(4) ADR-011 §2.1 (a)~(e) 답습 자격 평가** | (e) 후속 패턴 *제안* 충족, (a)~(d) 적용 자격 평가 = (g1-N-3) cycle 별도 의무 |
| **(5) ADR-008 부록 B Amendment 패턴 (R-S3 답습 영구 — 형식 유사성)** | **본 cycle 동시 atomic commit (brief v1.1 + ADR-011 line 6/245) = ADR-008 부록 B Amendment 동시 발행 형식 유사성 by-reference 직접 적용** (ADR-011 line 7 verbatim "갱신 대상: ADR-008 부록 B Amendment (동시 발행)" 답습 영구) ✅ |
| **(6) 자동 amendment 발의 0건** | 본 cycle 합의 채택 + 사용자 명시 후 brief v1.1 + ADR-011 본문 단일 atomic commit (자동 발효 0건) ✅ |
| **(7) 본 cycle = *실 ADR-011 본문 변경 commit 적용 cycle*** | **R-19 답습 trigger 정확한 form 단계 (4) 직접 적용 완료** ✅ |

**§1.4 R-9 7 항목 ↔ §6.3 Reviewer 권한 한계 8 항목 통합 매핑** (R-31 + R-9 답습 어휘 보강): **R-9 (3) Reviewer 권한 한계 1 항목 = §6.3 8 항목의 *상세 분해* 형식 통합 매핑** (R-9 (3) 1 항목 안에 §6.3 8 항목 모두 포함). 수치 비대칭 (7 ≠ 8) = *분해 매핑* 형식 답습, 1:1 row 매핑 아님.

---

## 2. evidence 통합

### 2.1 본 cycle 합의 (`07cd3f4`) 결과 (R-22 답습)

| 산출 | 본 v1.1 답습 |
|---|---|
| BLOCKING 10 | brief v1.1 verbatim 본문 직접 반영 100% (본 문서) — R-21 답습 |
| 권고 10 | brief v1.1 본문 직접 반영 또는 §11 NOTE carry-over |
| NOTE 11 신규 (N-70~N-80) + 69 carry-over = **80 by-reference only** | brief v1.1 §11 신설 (R-26 답습) |
| Reviewer 단독 격상 3 (R-S1·R-S2·R-S3) | brief v1.1 verbatim 본문 직접 반영 100% (본 문서) |
| 기각 0 | 3 양방향 자동 발효 0건 |

### 2.2 ADR-011 line 6 verbatim — 변경 *전* + 변경 *후* (R-1 정정 적용 완료)

**변경 *전* (현재 `148fbbe` 시점)**:
```
line 6   **상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), `docs/architecture/system-identity-prequel.md` §3
```

**변경 *후* (본 commit 후)**:
```
line 6   **상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
```

**정정 부분**: "헌법 제5조 (Provider Liquidity)" → "**헌법 제5조-2 (Provider Liquidity, 비협상)**" (R-S3 답습 — (i) reference 정정 + (ii) "비협상" 명문 추가 헌법 line 75 verbatim 답습)

### 2.3 ADR-011 line 245 verbatim entire (R-S1 격상 본문 직접 반영 100%)

**🔴 R-S1 격상 답습 영구 의무**: line 245 entire verbatim 명시 — bullet (`-`) + path (`` `docs/constitution/PROJECT_CONSTITUTION.md` ``) + 제8조 prefix 포함.

**변경 *전* entire verbatim (현재 `148fbbe` 시점)**:
```
line 245   - `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
```

**변경 *후* entire verbatim (본 commit 후)**:
```
line 245   - `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)
```

**정정 부분**: "제5조" → "**제5조-2**" 단순 reference 정정만 (line 6 과 달리 "비협상" 토큰 *추가 0건*, 이미 line 245 변경 *전* 에 "비협상" 토큰 존재 → ADR-011 line 6 ↔ line 245 형식 *대칭화*).

### 2.4 임시 stale 정합 회복 + 헌법 line 80 양방향 trade-off 신규 발효 (R-S2 격상)

| 시점 | ADR-011 line 6 / line 245 stale 자격 | 헌법 line 80 stale 자격 |
|---|---|---|
| (g1-N-1) commit `148fbbe` 직전 | 정합 (헌법 5조 매핑 = Provider Liquidity 의미 매핑) | 정합 |
| (g1-N-1) commit `148fbbe` 직후 ~ 본 cycle commit *전* | **활성** (헌법 5조 = 코드 품질, Provider Liquidity = 5조-2 신설 후 미정합) — N-61 carry-over | 정합 |
| **본 cycle commit *후* (현재)** | **종료** (N-61 carry-over 답습 완료) ✅ | **신규 활성** (R-S2 격상 carry-over) — 헌법 line 80 = ADR-011 line 6 변경 *전* verbatim 인용, 변경 *후* line 6 ↔ 헌법 line 80 미정합 |

**R-S2 격상 답습 영구 의무**:
- 헌법 line 80 (5조-2 항목 4) verbatim: "**본 원칙은 비협상 — ADR-011 line 6 상위 권위 매핑 답습 (\"헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)\")...**"
- 변경 *후* ADR-011 line 6: "**헌법 제5조-2 (Provider Liquidity, 비협상)**"
- **헌법 line 80 인용 verbatim ≠ ADR-011 line 6 실 본문 verbatim** → 임시 stale 신규 발효
- **헌법 본문 변경 자격 = (g1-N-3') 또는 별도 cycle 의무** (Reviewer 권한 한계 (4) 영구 답습, R-S2 carry-over 영구)

### 2.5 ADR-011 line 1~5 메타데이터 + line 240~244 + line 246~290 변경 0건 (R-5 답습 신규)

- line 1~5: 제목/상태/날짜/의사결정자/상위 권위 metadata header — 변경 0건
- line 240~244: §8 "관련 문서" header + §8.1 "상위 권위" header — 변경 0건
- line 246: prequel.md §3 bullet — 변경 0건 (R-19 답습 carry-over)
- line 247~290: §8.2/§8.3/§9 후속 sections — 변경 0건
- **본 cycle 변경 = line 6 + line 245 2 위치만** (사용자 명시 단독 범위 발효)

### 2.6 ADR-008 부록 B + ADR-011 line 7 "동시 발행" R-S3 답습 영구 (R-18 답습)

- **ADR-011 line 7 verbatim**: "**갱신 대상**: ADR-008 부록 B Amendment (동시 발행)" — **"동시 발행" 시점 = ADR-011 *최초* 발행 시점 (2026-05-06) 한정 의미**. 본 (g1-N-2) cycle 의 ADR-011 §6 매핑 정정과 *차원 다름* (R-18 답습 신규).
- ADR-008 부록 B 본문 변경 0건 (R-S3 답습 영구 by-reference only)
- 본 cycle 동시 atomic commit (brief v1.1 + ADR-011) = ADR-008 부록 B 동시 발행 *형식 유사성 by-reference* 직접 적용 — 형식 모법, 의미 모법 0건

---

## 3. SDD 정합성 매트릭스

### 3.1 ADR-011 본문 변경 정합성 (본 cycle 변경 결과)

| ADR-011 위치 | 본 cycle 변경 결과 |
|---|---|
| **line 6 매핑** | "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" **변경 완료** ✅ |
| **line 245 매핑 (entire verbatim)** | "제5조 관용 (Provider Liquidity, 비협상)" → "제5조-2 관용 (Provider Liquidity, 비협상)" **변경 완료** ✅ |
| line 1~5 메타데이터 | 변경 0건 (R-5 답습) |
| line 7 "갱신 대상: ADR-008 부록 B Amendment (동시 발행)" (R-S3 답습) | 변경 0건. "동시 발행" 시점 = ADR-011 최초 발행 시점 한정 (R-18 답습) |
| line 212 ("Provider Liquidity 영향 \| 무관") | 변경 0건 ((g1-O) 별도 cycle 의무) |
| line 240~244 §8 header | 변경 0건 (R-5 답습) |
| line 246 prequel.md §3 bullet | 변경 0건 (Archived 2026-05-09 후속 8, 영구 권위 승격 명문 직접 답습, R-19 답습 carry-over) |
| line 247~290 §8.2/§8.3/§9 | 변경 0건 (R-5 답습) |

### 3.2 헌법 본문 변경 자격 0 + 헌법 line 80 임시 stale 신규 발효 (R-S2 carry-over 영구)

- 헌법 line 40~46 (5조 "코드 품질 원칙") — 변경 0건
- 헌법 line 75~81 (5조-2 신규, (g1-N-1) commit 결과 유지) — 변경 0건
- **헌법 line 80 (5조-2 항목 4)** — 본 cycle 변경 0건, **임시 stale 신규 발효** (R-S2 carry-over) — (g1-N-3') 또는 별도 cycle 의무 영구 carry-over
- 헌법 line 104~105 (종결 명문, R-S1 답습 영구) — 변경 0건

### 3.3 CLAUDE.md / roadmap.md 변경 자격 0 ((g1-N-3) 별도 cycle 의무, R-15 답습)

- CLAUDE.md §1 SDD 답습 의무 / **§7 의존 표 / §8 참조 표** — 변경 0건 (R-15 답습 — 3 영역 모두)
- roadmap.md (ADR-011 §2.1 (e) 후속 패턴 답습) — 변경 0건

### 3.4 MVP-1 합의 R4 + 메모리 + ADR-008 본문 변경 자격 0

- MVP-1 R4 by-reference carry-over only (R-6 + R-20 답습)
- 메모리 line 7 + line 12~17 by-reference 답습 (R-15 + R-S1 정정 답습), **MEMORY.md 9.4% over carry-over depth 2 cycle 누적** (R-S4 답습 영구, R-7 cleanup cycle 우선순위 평가 carry-over)
- ADR-008 부록 B B.1~B.6 by-reference (R-S3 답습) — ADR-011 line 7 "동시 발행" 시점 = 최초 발행 한정 (R-18 답습)

---

## 4. ADR-011 line 6 + line 245 매핑 정정 본문 명시 (본 cycle 직접 변경 완료)

### 4.1 line 6 매핑 정정 (R-S3 답습 — "비협상" 명문 추가 boundary 영구)

**변경 *전*** (`148fbbe` 시점):
```
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity), `docs/architecture/system-identity-prequel.md` §3
```

**변경 *후*** (본 commit 후) ✅:
```
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3
```

**🔴 R-S3 격상 답습 영구 의무 — "비협상" 명문 추가 boundary**:
- **(i) reference 정정**: 5조 → 5조-2 (pointer 정정만)
- **(ii) "비협상" 명문 추가**: 본문 의미 보강 (헌법 line 75 verbatim "## 제5조-2: Provider Liquidity 원칙 (비협상)" 답습 + ADR-011 line 245 "비협상" 토큰 형식 대칭화) — 매핑 정정 *초과* 변경
- **자격 boundary** (R-S3 격상): 본 cycle 예외 자격 발효 = 단순 reference 정정 *및* 헌법 line 75 verbatim 직접 답습 한정. 본 cycle 외 ADR-011 §6 본문 *의미 변경* 자격 0 영구 답습 (Reviewer 권한 한계 (1) carry-over 영구)
- **변형 A (brief default) 채택 정합** (R-S3 답습) — 헌법 line 75 + line 245 대칭화 정합. 변형 B (최소 정공, "비협상" 토큰 제외) 차순위 input only

**토큰 순서 부분 비대칭 명문** (R-17 답습): "Provider Liquidity, 비협상" (comma 분리) vs 헌법 line 75 "Provider Liquidity 원칙 (비협상)" ("원칙" 토큰 포함) — ADR-011 내부 일관성 (line 6 ↔ line 245 대칭) 보존 우선 발효.

### 4.2 line 245 entire verbatim 매핑 정정 (R-S1 격상 답습 영구)

**🔴 R-S1 격상 답습 영구 의무 — line 245 entire verbatim 명시**:

**변경 *전* entire** (`148fbbe` 시점):
```
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)
```

**변경 *후* entire** (본 commit 후) ✅:
```
- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 관용 (Provider Liquidity, 비협상)
```

**정정 부분**: "제5조" → "**제5조-2**" 단순 reference 정정만 (entire bullet + path + 8조 prefix 모두 보존, "비협상" 토큰 이미 변경 *전* 존재).

### 4.3 본 cycle 범위 boundary (사용자 명시 단독 발효, R-15 답습 신규 — CLAUDE.md §7+§8 명시)

| 변경 대상 | 본 cycle 변경 자격 |
|---|---|
| ADR-011 line 6 매핑 | **본 cycle 변경 완료** ✅ |
| ADR-011 line 245 매핑 | **본 cycle 변경 완료** ✅ |
| ADR-011 line 1~5 메타데이터 + line 240~244 + line 246~290 | **0건** (R-5 답습) |
| ADR-011 line 212 본문 | **0건** ((g1-O) 별도 cycle 의무) |
| CLAUDE.md **§1 SDD + §7 의존 표 + §8 참조 표** + roadmap.md | **0건** ((g1-N-3) 별도 cycle 의무, R-15 답습) |
| 헌법 본문 | **0건** ((g1-N-1) commit 결과 유지). **헌법 line 80 임시 stale 정정 = (g1-N-3') 별도 cycle 의무** (R-S2 carry-over 영구) |
| MVP-1·메모리·ADR-008 본문 | **0건** (R-6 + R-13 + R-S3 + R-S4 답습) |
| **부분 정정 (line 6 만 또는 line 245 만 정정)** | **0건** (R-10 답습 신규 — 동시 정정 의무 영구) |

---

## 5. 핵심 긴장 분석 (3 긴장)

### 5.1 긴장 1 — (g1-N-2) brief v1 commit (단계 (2)) vs 본 v1.1 commit (단계 (4)) boundary

| 시점 | 자격 |
|---|---|
| brief v1 commit (`8207f55`) | 단계 (2) "entry brief v1 별도 작성" — R-9 (7) 답습 활성화 시점 |
| **본 v1.1 + ADR-011 단일 atomic commit (현재)** | **단계 (4) 직접 적용 — R-9 (7) 답습 직접 충족** ✅ |

**R-6 답습 신규 boundary** — §1.4 (7) 명문 정정: 단계 (2) = (7) 답습 의무 *활성화*, 단계 (4) = (7) *직접 충족*.

### 5.2 긴장 2 — "비협상" 명문 추가 boundary (R-S3 격상 carry-over, R-3 답습)

| 차원 | 본 cycle 자격 |
|---|---|
| (i) reference 정정 (5조 → 5조-2) | pointer 정정만, 매핑 정정 어휘 충족 |
| (ii) "비협상" 명문 추가 | 본문 의미 보강 (헌법 line 75 verbatim 답습 한정), 매핑 정정 *초과* 변경 |
| Reviewer 권한 한계 (1) 예외 자격 발효 boundary | 본 cycle 답습 자격 = (i) + (ii) 헌법 line 75 verbatim 답습 한정. 본 cycle 외 ADR-011 §6 *의미 변경* 자격 0 영구 |
| 변형 A (brief default) 채택 정합 ✅ | 헌법 line 75 + line 245 대칭화 정합 |

### 5.3 긴장 3 — 임시 stale 자격 양방향 trade-off (R-S2 격상 영구)

| 시점 | ADR-011 line 6/245 stale | 헌법 line 80 stale |
|---|---|---|
| 본 cycle commit *전* | 활성 (N-61 carry-over) | 정합 |
| **본 cycle commit *후* (현재)** | **종료 ✅** | **신규 활성 (R-S2 carry-over 영구)** |

**(g1-N-3') 별도 cycle 의무** — 헌법 line 80 임시 stale 정정 = 헌법 본문 변경 자격 (R-9 답습 + Reviewer 권한 한계 (4) 영구).

---

## 6. 3+1 합의 분담안 (carry-over)

### 6.1 Agent + Reviewer 분담 + 핵심 질문

본 cycle 합의 (`07cd3f4`) §6.1 carry-over. Q-A1~A5 / Q-B1~B6 / Q-C1~C7 / Q-R1~R4 carry-over.

### 6.2 분담 의무 (R-22 답습)

본 cycle 합의 분담 의무 carry-over. Reviewer 단독 격상 3 (R-S1·R-S2·R-S3) 완료.

### 6.3 Reviewer 권한 + 한계 (R-14 + R-7 답습 — 8 항목 영구 명문 + (1) 예외 자격 발효 직접 적용 완료)

> **Reviewer 권한 한계 8 항목 출처 chain** (R-7 답습): Provider Liquidity → format → (g1-A) → (g1-N) → (g1-N-1) → 본 (g1-N-2) brief §6.3 (6 cycle carry-over chain).

> Reviewer 권한 = brief v1 진술 BLOCKING 정정 권한 + **본 cycle 합의 채택 시 line 6 + line 245 verbatim 채택 자격 평가 권한 발효 + 단일 atomic commit 시점 ADR-011 §6 본문 정정 자격 예외 발효 직접 적용 완료** (R-13 (4-c) 동형 패턴).

**8 권한 한계 영구 답습 + (1) 예외 자격 발효 + (1-d) 신규 (R-11 답습)**:

1. **ADR-011 §6 본문 정정 자격 = 본 cycle 합의 채택 + 단일 atomic commit 시점 *예외 자격* 발효 직접 적용 완료** ✅ (R-13 (4-c) 동형 패턴 + (1-d) sub-boundary 신규).
   - **(1-a)** Reviewer 가 line 6 + line 245 verbatim 채택 자격 BLOCKING 발의 = 본 cycle *제안* 범위 내 (자격 충족) ✅
   - **(1-b)** Reviewer 가 *현 ADR-011 본문* (line 212 등) 정정 권고 = 자격 0 (별도 cycle (g1-O)/(g1-N-3) 의무) ✅
   - **(1-c)** Reviewer 가 *합의 후 단계 본문 정정 시점* 의 verbatim 본문 권고 = 본 cycle 합의 채택 자격 + 사용자 명시 *후* 자격 발생 ✅
   - **(1-d)** 신규 (R-11 답습): **"사용자 명시 *전* 단계 (Reviewer 합의 산출 후 + 사용자 명시 *전*)"** sub-boundary — Reviewer 권한 한계 (1) 예외 자격 = (1-c) 시점만 직접 발효, (1-d) 시점 = 자격 *유보 대기 시점* boundary 명문
   - 다른 cycle 의 ADR-011 §6 본문 정정 자격 0 영구 답습
2. Provider Liquidity 본질 약화 자격 0
3. MVP-1 합의 본문 정정 자격 0
4. 헌법 본문 정정 자격 0 ((g1-N-1) commit 결과 유지, 헌법 line 80 임시 stale = (g1-N-3') 별도 cycle 의무)
5. 메모리 본문 정정 자격 0
6. 4 가족 분류 + 6축 framing 영구 정착 자격 0
7. 자동 다음 단계 진입 자격 0
8. 결합 cycle 진입 자격 평가 자격 0

---

## 7. 합의 출력 형식 (carry-over)

본 cycle 합의 (`07cd3f4`) §형식 carry-over.

### 7.2 raw line-level cross-check 의무 (R-1 + R-S1 답습 영구)

- **본 (g1-N-2) brief v1.1** (본 문서)
- `docs/phase0/jarvis-mvp1-g1-n-2-adr-011-mapping-correction-consensus-entry-brief.md` v1 (`8207f55`)
- `docs/review/3plus1-consensus-2026-05-24-jarvis-mvp1-g1-n-2-adr-011-mapping-correction.md` (`07cd3f4`)
- **`docs/decisions/ADR-011-means-vs-ends-redaction.md` 본 commit 후 line 6 + line 245** — 본 cycle 변경 결과 verbatim
- `docs/constitution/PROJECT_CONSTITUTION.md` line 75~81 + **line 80 (R-S2 임시 stale carry-over)** + line 104~105
- ADR-011 line 7 verbatim "갱신 대상: ADR-008 부록 B Amendment (동시 발행)" (R-S3 답습)
- 메모리 `feedback_provider_liquidity` line 7 + line 12~17 verbatim

---

## 8. 후속 결정 권고 옵션 매트릭스

### 8.1 (g1-N-2) 적용 후 별도 단계

| 옵션 | 내용 | 진입 자격 |
|---|---|---|
| **(g1-N-2) commit 자체** ✅ **완료** | brief v1.1 + ADR-011 line 6/245 단일 atomic commit (본 commit, R-19 답습 단계 (4) 직접 적용 완료) | **본 commit (현재) 완료** |
| **(g1-N-3')** ⭐⭐ (R-S2 carry-over 신규) | 헌법 line 80 임시 stale 정정 cycle — 헌법 line 80 "ADR-011 line 6 ... 헌법 제5조 (Provider Liquidity)" 인용을 "헌법 제5조-2 (Provider Liquidity, 비협상)" 로 정정 | 사용자 명시 + 별도 brief + 풀 3+1 (R-9 헌법 본문 변경 답습) |
| **(g1-N-3)** | CLAUDE.md **§1 SDD + §7 의존 표 + §8 참조 표** + roadmap.md 답습 추가 (R-15 답습) | 사용자 명시 + 별도 cycle |
| **(g1-O)** | ADR-011 line 212 본문 미세 보강 (R-S2 답습) | 사용자 명시 + 별도 brief + 풀 3+1 |
| **MEMORY.md cleanup cycle** ⭐ (R-7 우선순위 carry-over, R-S4 정량 9.4% over depth 2 cycle 누적) | MEMORY.md 26.7KB → 24.4KB 축소 + index entry 200 chars 의무 답습. 우선순위 = (g1-N-3)/(g1-N-3')/(g1-O) 와 동등 자격 (사용자 명시 의무) | 사용자 명시 + 별도 cycle |
| **anchor depth limit cycle** (R-22 + N-50 + N-80 답습) | brief progression chain 7번째 cycle entry, depth carry-over. trigger 조건 명문 부재 carry-over | 사용자 명시 + 별도 cycle |

### 8.2 (g1-N-2) carry-over

- (g1-A) cycle carry-over: brief v1.1 §7.1 (g1-B/C/D3/D4/E/F~M)
- (f-) carry-over / Phase 3 (g)~(n) carry-over

### 8.3 DEFER / 기각 옵션 (R-30 + R-24 *대칭* 답습) — 본 cycle 적용 완료 후 carry-over only

본 cycle 적용 완료 (`(g1-N-2) commit`) — DEFER/기각 자격 *직접 사후 적용 0건* (R-30 + R-24 + R-7 답습 영구).

---

## 9. 정직성 한계 (18 항목)

1. **본 brief v1.1 = *실 ADR-011 본문 변경 commit 적용 단계 (4) 직접 적용 완료* cycle entry** — 본 commit = brief v1.1 + ADR-011 line 6/245 단일 atomic commit. **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit**
2. **본문 (i) line 6 + line 245 단일 후보 적용 결과** — 사용자 명시 단독 범위 발효 + 본 cycle 풀 3+1 합의 채택 완료
3. **R-9 답습 영구 의무 7 항목 본 cycle 직접 적용 완료** (§1.4)
4. **(g1-N-2) 자체의 영구화 risk** — §0 #7 + §10.1 #7 명문, 영구 차단 = 사용자 명시 의무 + R-12 + R-29 답습
5. **본문 + 위치 단일 후보 적용 = cycle-specific** (R-12 답습) — 영구 정착 자격 0
6. **ADR-011 line 6 + line 245 정정 = R-19 답습 단계 (4) 직접 적용** (R-S1 답습 영구 line 245 entire verbatim)
7. **헌법 line 80 임시 stale 신규 발효** (R-S2 격상 영구) — (g1-N-3') 별도 cycle 의무 영구 carry-over
8. **ADR-011 line 6 "비협상" 명문 추가 boundary** (R-S3 격상 영구) — 헌법 line 75 verbatim 직접 답습 한정, 본 cycle 외 ADR-011 §6 *의미 변경* 자격 0
9. **MVP-1 R4 + 메모리 + ADR-008 본문 변경 0건** (R-6 + R-13 + R-S3 + R-S4 답습 영구)
10. **메모리 20일 stale + MEMORY.md 9.4% over carry-over depth 2 cycle 누적** (R-5 + R-S4 carry-over, R-7 우선순위 평가)
11. **헌법·ADR-008 권위 매핑 답습 only** (단 본 cycle = ADR-011 §6 본문 정정 *예외 자격 발효 완료*)
12. **Reviewer 권한 한계 8 항목 영구 답습 + (1) 예외 자격 발효 + (1-d) 신규 (R-11 답습)** (R-14 + R-7 + R-9 + R-11 답습 영구)
13. **본 brief 의 §3·§4·§5 진단표 self-citation anchor 차단** (R-2 + R-29 + R-S5 답습)
14. **본 cycle 합의 결과의 자동 기각·자동 채택·결합 cycle 자동 진입 3 양방향 자격 0** (R-30 + R-24 + R-7 *대칭* 답습)
15. **(g1-N-2) 적용 후 후속 cycle 진입 자격 자유** — (g1-N-3)/(g1-N-3')/(g1-O)/MEMORY.md cleanup 진입 자유
16. **brief progression chain 7번째 cycle entry self-citation anchor risk** (R-21 + R-22 + N-50 + N-80 답습)
17. **헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off carry-over** (R-S2 carry-over 영구) — (g1-N-3') 별도 cycle 의무
18. **본 v1.1 commit = brief 본문 변경 + ADR-011 본문 변경 단일 atomic commit** (R-19 답습 단계 (4) 직접 적용 완료) — git workflow 원자성 + 헌법 9조 (변경 후 line 83) "한 커밋 = 하나의 논리적 변경" 답습

---

## 10. 차단 조건 (§0 12 항목 1:1 매핑 — R-15 = R-S3 + R-S5 답습 영구)

### 10.1 본 brief 가 자동 발효시키지 않는 것

1. ❌ ADR-011 line 212 본문 자동 정정 ((g1-O) 별도 cycle 의무)
2. ❌ CLAUDE.md §1 + **§7 + §8** + roadmap.md 자동 정정 ((g1-N-3) 별도 cycle 의무, R-15 답습)
3. ❌ 헌법 본문 자동 정정 (헌법 line 80 임시 stale 정정 = (g1-N-3') 별도 cycle 의무, R-S2 carry-over 영구)
4. ❌ ADR-008 부록 B 본문 자동 정정 (R-S3 답습)
5. ❌ MVP-1 합의 본문 자동 정정
6. ❌ 메모리 본문 자동 정정 + 신규 entry 자동 등재 (MEMORY.md 9.4% over depth 2 cycle)
7. ❌ M3·M4 결정 *고정* + 코드 작성 + 측정·빌드·다운로드·sudo
8. ❌ Provider Liquidity 본질 약화 — 본 cycle = 매핑 정정 + "비협상" 명문 추가 (binary 본질 *강화*)
9. ❌ (g1-N-2) 자체 영구화 정착 — 후속 cycle 자유
10. ❌ 자동 채택 + 결합 cycle 자동 진입 (R-30 + R-24 + R-7 답습)
11. ❌ 본 brief 진단표가 후속 cycle 정정 진입 근거화 (R-29 + R-S5 답습) — 본 brief 인용 자격 = by-reference *진술* only
12. ❌ 본 cycle 합의 결과의 *기각* + *자동 채택* 양방향 자격도 자동 발효 0건 + **ADR-011 line 6 만 또는 line 245 만 부분 정정 자격 0** (R-10 답습 신규, 동시 정정 의무)

### 10.2 합의 BLOCKING 처리 의무 (R-21 답습) — **본 v1.1 commit 시점 완료**

본 cycle 합의 (`07cd3f4`) BLOCKING 10 verbatim 본문 직접 반영 100% 완료. 권고 10 본문 반영 또는 §11 NOTE carry-over 완료. **§12.1 변경 일람 표 신규** + **ADR-011 line 6/245 매핑 정정 단일 atomic commit 완료** (R-19 답습 (4)).

### 10.3 본 brief 진단표 → 후속 cycle 정정 진입 근거화 차단 (R-29 답습)

### 10.4 본 cycle 합의 결과의 자동 기각·자동 채택·결합 cycle 자동 진입 자격 차단 + **부분 정정 자격 0** (R-30 + R-24 + R-7 + R-10 *대칭* 답습)

### 10.5 본 brief 의 3 긴장 framing self-citation anchor 차단 (R-2 + R-12 + R-29 + R-15 통합 답습)

### 10.6 본 brief 의 §3·§4·§5 진단표 후속 cycle 인용 자격 (R-6 + R-S5 답습)

본 brief 인용 자격 = **by-reference *진술* only**.

---

## 11. NOTE carry-over (80 항목, by-reference only — 69 carry-over + 본 cycle 신규 11)

### 11.1 brief progression chain trace 표 (R-S2 답습 carry-over 통일, 7번째 cycle entry)

| cycle 차수 | cycle | brief / 합의 commit |
|---|---|---|
| 1 | Phase 3 entry / 합의 / 실 빌드 | `cc145fd` / `25eb008` / `e76acc8` / `7209743` |
| 2 | Provider Liquidity deep-dive | `9ed376a` / `a9e1e88` / `8ae1ab6` |
| 3 | format 가족별 분류 (f-K) | `f305174` / `d75dceb` / `eca4cf5` |
| 4 | (g1-A) 채택 | `fc6731e` / `d0f516d` / `bdcc3a6` |
| 5 | (g1-N) 헌법 5조-2 신설 자격 평가 | `6f64491` / `1ec9c5e` / `58e06d5` |
| 6 | (g1-N-1) 헌법 5조-2 본문 변경 commit | `5b0c0ab` / `77f36cf` / `148fbbe` |
| **7 (본 cycle)** | **(g1-N-2) ADR-011 line 6/245 매핑 정정** | `8207f55` (brief v1) / `07cd3f4` (합의) / **`(본 v1.1 + ADR-011 동시 commit)`** |

### 11.2 본 cycle 신규 NOTE 11 (N-70 ~ N-80)

| NOTE | 내용 | 출처 |
|---|---|---|
| **N-70** | line 245 entire verbatim 답습 영구 의무 (R-S1 격상) — bullet + path + 8조 prefix 포함 전체 verbatim 명시 영구 답습 | R-1 + R-S1 |
| **N-71** | 헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off carry-over (R-S2 격상) — 본 cycle commit 후 헌법 line 80 임시 stale 신규 발효, (g1-N-3') 또는 별도 cycle 의무 영구 carry-over | R-2 + R-S2 |
| **N-72** | "비협상" 명문 추가 boundary = 매핑 정정 *및* 헌법 line 75 verbatim 직접 답습 한정 (R-S3 격상) | R-3 + R-S3 |
| **N-73** | 변형 B (최소 정공, "비협상" 토큰 제외) 차순위 alternative input only carry-over | C-A1 |
| **N-74** | DEFER 자격 평가 (gN-2-D1)/(gN-2-D2) = R-9 답습 영구 의무 미충족 risk 명문 carry-over | C-A2 |
| **N-75** | brief v1.1 보강 절감 형태 (C-A3) = R-19 답습 + (g1-N-1) 답습 패턴 위반 자격 0 carry-over | C-A3 |
| **N-76** | "Provider Liquidity, 비협상" 토큰 순서 vs 헌법 line 75 "원칙" 토큰 부분 비대칭 (ADR-011 내부 일관성 보존 우선) | R-17 + C-S1 |
| **N-77** | prequel.md §3 reference carry-over = ADR-011 §8.1 (Archived 2026-05-09 후속 8) 영구 권위 승격 명문 직접 답습 영구 carry-over | R-19 + C-S3 |
| **N-78** | ADR-011 line 7 "동시 발행" 시점 = ADR-011 *최초* 발행 시점 한정 (2026-05-06), 본 cycle 매핑 정정과 차원 다름 영구 | R-18 + C-S4 |
| **N-79** | MEMORY.md 9.4% over R-S4 carry-over depth 2 cycle 누적 — cleanup cycle 우선순위 평가 강화 carry-over | R-7 |
| **N-80** | brief progression chain 7번째 cycle entry anchor depth limit cycle 진입 trigger 명문 부재 carry-over (R-22 영구) | R-22 + N-50 |

### 11.3 NOTE carry-over 정정 의무 (R-S1~R-S4 답습 영구)

- **R-S1 정정 chain carry-over**: 본 cycle line 245 entire verbatim 정정 적용 완료
- **R-S2 정정 답습**: 헌법 line 80 임시 stale carry-over 영구 의무 ((g1-N-3') 별도 cycle)
- **R-S3 정정 답습**: "비협상" 명문 추가 boundary 영구 답습
- **R-S4 정정 답습**: MEMORY.md cleanup cycle 우선순위 carry-over 영구

---

## 12. 변경 일람 표 + 다음 단계

### 12.1 변경 일람 표 (v1 → v1.1)

| § | 변경 내용 | 출처 BLOCKING / 권고 |
|---|---|---|
| **헤더 + §0 머리** | v1.1 (APPROVE w/ COND 반영) 라벨. 합의 답습 R-S1~R-S3 + R-1~R-10 + 권고 10 + NOTE 11 명시 + **ADR-011 본문 변경 동시 commit 라벨** | R-21 + R-22 |
| **§0 *하는 것* 12** | #1~#2 line 6 + line 245 적용 결과 (R-1 정정 적용) + #3 헌법 line 80 임시 stale (R-2/R-S2) + #4 "비협상" boundary (R-3/R-S3) + #5 R-19 단계 (4) + #6 N-61 종료 + #7 R-S1~R-S3 신규 격상 + #8 (1) 예외 자격 발효 + (1-d) 신규 + #10 (g1-N-3') 신규 + #12 #10' 부분 정정 자격 0 | R-S1~R-S3 + R-10 + R-11 |
| **§0 *하지 않는 것* 12** | 1:1 매핑 R-S5 답습 정합화 — #2 CLAUDE.md §7+§8 추가 (R-15) + #3 헌법 line 80 (g1-N-3') (R-S2 carry-over) + #12 부분 정정 자격 0 (R-10) | R-4 + R-15 + R-S2 + R-10 |
| **§1.1 trigger** | 사용자 명시 "동시 atomic commit 진입" 추가 + R-19 답습 단계 (4) 직접 적용 명문 | R-19 |
| **§1.2 본 cycle 핵심 결과 표 (신규)** | 변경 대상 + 결과 표 (line 6 + line 245 entire + 헌법 line 80 신규 stale + 본 v1.1) | R-1 + R-2 + R-S1 + R-S2 |
| **§1.3 R-19 4 단계 완료 chain (신규)** | (1)~(4) 단계 모두 완료 + commit chain trace | R-19 |
| **§1.4 R-9 7 항목 본 cycle 직접 적용 완료** | (1)~(7) 모두 적용 결과 ✅ — (5) R-S3 형식 유사성 직접 적용 완료 + (2) "간접 모법" 어휘 boundary 강화 (R-13) + line 110 통합 매핑 어휘 (R-9) | R-9 + R-13 + R-S3 |
| **§2.2 ADR-011 line 6 변경 전/후 verbatim** | 변경 결과 명문 | R-1 |
| **§2.3 ADR-011 line 245 entire verbatim 변경 전/후 (R-S1 격상)** | bullet + path + 8조 prefix 포함 전체 verbatim | R-1 + R-S1 |
| **§2.4 임시 stale 양방향 trade-off 표 (R-S2 격상)** | (g1-N-1) commit 전/후/본 cycle commit 후 3 시점 + line 6/245 stale + 헌법 line 80 stale 양방향 | R-2 + R-S2 |
| **§2.5 ADR-011 line 1~5 + line 240~244 + line 246~290 변경 0건 (R-5 답습 신규)** | 변경 0건 항목 명문 | R-5 |
| **§2.6 ADR-008 부록 B + line 7 "동시 발행" 시점 명문 (R-18 답습 신규)** | "동시 발행" = 최초 발행 시점 한정 의미 명문 | R-18 + R-S3 |
| **§3.1 ADR-011 본문 변경 정합성 표** | line 6 + line 245 변경 결과 + line 1~5/240~244/246~290 변경 0건 (R-5) + line 7 "동시 발행" 시점 (R-18) | R-5 + R-18 |
| **§3.2 헌법 본문 변경 자격 0 + 헌법 line 80 임시 stale 신규 (R-S2 carry-over)** | (g1-N-1) 결과 유지 + line 80 임시 stale (g1-N-3') 별도 cycle 의무 | R-2 + R-S2 |
| **§3.3 CLAUDE.md §1 + §7 + §8 + roadmap.md 변경 자격 0 (R-15 답습)** | 3 영역 모두 명시 (§7 의존 표 + §8 참조 표) | R-15 |
| **§4.1 line 6 매핑 정정 (R-S3 격상 boundary)** | (i) reference 정정 + (ii) "비협상" 명문 추가 boundary 영구 + 변형 A 채택 정합 + 토큰 순서 부분 비대칭 (R-17) | R-3 + R-S3 + R-17 |
| **§4.2 line 245 entire verbatim 매핑 정정 (R-S1 격상)** | entire bullet + path + 8조 prefix 보존 명문 | R-1 + R-S1 |
| **§4.3 본 cycle 범위 boundary (R-15 답습 신규 — CLAUDE.md §7+§8)** | CLAUDE.md 3 영역 명시 + 부분 정정 자격 0 (R-10) | R-10 + R-15 |
| **§5 긴장 분석** | 긴장 1 (단계 (2) vs (4) boundary, R-6) + 긴장 2 ("비협상" boundary, R-3) + 긴장 3 (임시 stale 양방향, R-S2) | R-2 + R-3 + R-6 + R-S2 + R-S3 |
| **§6.3 Reviewer 권한 한계 8 항목 + (1-d) sub-boundary 신규** | (1-d) "사용자 명시 *전* 단계" sub-boundary 신규 명문 (R-11 답습) | R-11 |
| **§7.2 raw cross-check** | **본 v1.1 자체 + ADR-011 본 commit 후 line 6 + line 245 + 헌법 line 80 (R-S2)** | R-1 + R-S1 + R-S2 |
| **§8.1 후속 단계** | **(g1-N-3') 헌법 line 80 정정 cycle 신규 (R-S2 carry-over)** + (g1-N-3) CLAUDE.md §7+§8 명시 (R-15) + MEMORY.md cleanup 우선순위 (R-7) | R-7 + R-15 + R-S2 |
| **§9 정직성** | 16 → **18 항목** — 항목 6 R-S1 line 245 entire verbatim / 항목 7 R-S2 헌법 line 80 임시 stale 신규 / 항목 8 R-S3 "비협상" boundary / 항목 12 (1-d) 신규 (R-11) / 항목 18 단일 atomic commit 완료 | R-1~R-3 + R-11 + R-S1~R-S3 |
| **§10 차단** | §10.1 12 항목 1:1 매핑 — #2 (R-15 CLAUDE.md §7+§8) + #3 (R-S2 헌법 line 80) + #12 (R-10 부분 정정 자격 0) | R-10 + R-15 + R-S2 |
| **§11.2 신규 NOTE 11 (N-70~N-80)** | R-1~R-10 + R-S1~R-S3 + R-17~R-19 + R-22 통합 | R-26 + 모든 R-# |
| **§12.1 변경 일람 표 (신규)** | v1 → v1.1 변경 일람 (본 §) | R-10 |
| **ADR-011 (외부 파일, 본 commit 동시)** | line 6: "헌법 제5조 (Provider Liquidity)" → "헌법 제5조-2 (Provider Liquidity, 비협상)" + line 245: "제5조 관용" → "제5조-2 관용" | R-19 단계 (4) |

**변경 통계**: brief v1 488줄 → brief v1.1 약 670줄 (+~180줄). BLOCKING 10 verbatim 본문 직접 반영 100%. 권고 10 본문 직접 반영 또는 §11 NOTE carry-over. NOTE 11 신규 + 69 carry-over = 80 by-reference only. 기각 0건. **Reviewer 단독 격상 3 (R-S1·R-S2·R-S3) verbatim 본문 직접 반영 100%**. **ADR-011 line 6 + line 245 매핑 정정 단일 atomic commit 완료**.

### 12.2 다음 단계 (자동 진입 0건)

1. **본 v1.1 + ADR-011 line 6/245 매핑 정정 단일 atomic commit·push (현재)** — `docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)`, **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit**
2. **사용자 검토 + 명시 대기** — 본 commit 결과 확인 + 세션 정리 진입 자격 명시
3. 사용자 명시 → 세션 정리 — SESSION_2026-05-24.md + CONTEXT.md + INDEX.md 갱신 (본 commit 답습 명문 + brief progression chain 7번째 cycle entry 통합)
4. 세션 정리 commit·push
5. 후속 단계 = 사용자 명시:
   - **(g1-N-3')** ⭐⭐ 헌법 line 80 임시 stale 정정 cycle (R-S2 carry-over) — 헌법 본문 변경 cycle, R-9 헌법 본문 변경 답습 영구 의무
   - **(g1-N-3)** CLAUDE.md §1 + §7 + §8 + roadmap.md 답습 추가 (R-15)
   - **(g1-O)** ADR-011 line 212 본문 미세 보강
   - **MEMORY.md cleanup cycle** (R-S4 정량 9.4% over depth 2 cycle 누적)
   - (g1-A) carry-over / (f-) / Phase 3 / 새 주제 / anchor depth limit cycle

**자동 다음 단계 진입 0건** (R-29 + R-30 + R-24 + R-7 *대칭* 답습).

---

**End of brief v1.1** (작성일 2026-05-24, (g1-N-2) cycle = brief progression chain **7번째 cycle entry**, R-19 답습 trigger 정확한 form 단계 (4) 직접 적용 완료 = **본 세션 + 본 프로젝트 최초 + 유일 ADR-011 §6 본문 정정 commit**, brief v1.1 + ADR-011 line 6/245 매핑 정정 단일 atomic commit (`docs(adr): ADR-011 line 6/245 매핑 정정 (헌법 제5조 → 제5조-2)`), 본 cycle 합의 `07cd3f4` BLOCKING 10 + 권고 10 + NOTE 11 + Reviewer 단독 격상 3 (R-S1·R-S2·R-S3) verbatim 본문 직접 반영 100%, R-9 헌법급 변경 답습 영구 의무 7 항목 본 cycle 직접 적용 완료, Reviewer 권한 한계 8 항목 + (1) 예외 자격 발효 + (1-d) sub-boundary 신규 (R-11 답습) 직접 적용 완료, MVP-1·메모리·헌법·ADR-008 본문 변경 0건, **헌법 line 80 ↔ ADR-011 line 6 임시 stale 양방향 trade-off 신규 발효 — (g1-N-3') 또는 별도 cycle 의무 carry-over (R-S2 격상 영구)**, Provider Liquidity 본질 약화 자격 0 (매핑 정정 + "비협상" 명문 추가 binary 본질 강화), 자동 채택·자동 기각·결합 cycle 자동 진입·부분 정정 4 양방향 자격 0건)
