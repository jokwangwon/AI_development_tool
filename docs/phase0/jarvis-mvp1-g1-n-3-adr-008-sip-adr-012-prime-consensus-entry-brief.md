# (g1-N-3-adr-008+sip+adr-012') 정합 정정 자격 평가 entry brief v1.1 — 11번째 cycle entry (APPROVE w/ COND 반영)

> **본 brief v1.1 = (g1-N-3-adr-008+sip+adr-012') 풀 3+1 합의 (`209f04d`, APPROVE w/ COND, BLOCKING 11 + R-S1~R-S3 + 권고 9 + NOTE 18 + 기각 4) verbatim 본문 직접 반영**. v1 (`b55e0c9`, 561줄) → v1.1 본문 변경 통합. **R-S1 CRITICAL** = hermes-not-root-of-trust-runtime.md line 23/176/1040 추가 source 신설 (Agent C C-B1 + Reviewer raw cross-check 강화) — 본 cycle 범위 = **3 → 4 source 확장 발효**. 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 변경·헌법 본문 자동 정정·ADR-011 본문 자동 정정·MVP-1 합의 본문 자동 정정·메모리 본문 자동 정정·4 source 본문 자동 정정·(P4) 자동 신설·(11) sub-boundary 자동 신설·결합 cycle 자동 채택·(g1-N-4) framing 자동 진입** 를 발생시키지 않는다. 실 변경 0건. staged: brief v1 (`b55e0c9`) → 합의 (`209f04d`) → **brief v1.1 (본 문서)** → 4 source cross-ref block 1 commit ((f) 채택, R-7 답습) → 세션 정리 → push. 자동 다음 단계 진입 0건.

**작성일**: 2026-05-25 (합의 `209f04d` 직후)
**cycle 명**: (g1-N-3-adr-008+sip+adr-012') = (g1-N-3') 직접 후속, 11번째 cycle entry
**진입 형태**: (g1-N-3') 합의 §8.2 후속 cycle 매트릭스 HIGH 우선순위 직접 carry-over + 사용자 명시 ("권고로 진행")
**범위 (v1 3 source → v1.1 4 source 확장)**: system-identity-prequel.md + ADR-008.md + ADR-012.md + **hermes-not-root-of-trust-runtime.md (R-S1 추가)** 의 (ii-b) 헌법-직접-매핑 범위 자격 평가 + 정정 자격 평가 (정정 *결정* = 본 합의 R-7 (f) cross-ref block 만 1 commit 채택, 사용자 명시 확인)
**결합 형식 결정 (R-7 답습)**: ✅ **(f) cross-ref block 만 1 commit 채택 (사용자 명시 직접 확인)** — 4 source 본문 verbatim 변경 0건 + cross-ref block 추가만, (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습. (a) 결합 + verbatim 자동 채택 = 차단 명문 강화 (R-3 답습). (b) 4 cycle 분리 = 정직성 *보존 차순* 명문 (NOTE 보존). (h) [신규 대안 framing] 결합 + cross-ref block 만 = Agent C 단독 input, NOTE 보존
**정정 후 형식 결정 (R-rec-3 답습)**: ✅ **ADR-011 line 245 모법 "제5조-2 관용 (Provider Liquidity, 비협상)" 채택 (사용자 명시 직접 확인)** — (P3) 약식 통일 cycle DEFER carry-over

**합의 답습** (R-22 답습):
- (g1-N-3-adr-008+sip+adr-012') 합의 (`209f04d`) BLOCKING 11 + R-S1~R-S3 + 권고 9 + NOTE 18 + 기각 4 본문 직접 반영 100%
- 특히 **R-S1 (CRITICAL) hermes-not-root-of-trust-runtime 추가 source 직접 흡수**
- (g1-N-3') 합의 (`fea84bf`) Reviewer 권한 한계 (10-a)~(10-k) 11 sub-boundary 답습 영구 의무
- 본 cycle = **(11) sub-boundary 신설 *기각* 본 합의 발효** (R-1 + 기각-3 답습)
- 본 cycle = **(g1-N-3) chain 11번째 entry → chain 영구 종결 명문 의무** (R-10 + R-rec-8 답습)

**선행 답습**:
- `docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-g1-n-3-adr-008-sip-adr-012-prime.md` (본 cycle 합의, `209f04d`)
- `docs/review/3plus1-consensus-2026-05-25-jarvis-mvp1-g1-n-3-prime-high-integrated-consensus.md` ((g1-N-3') 합의)
- `docs/phase0/jarvis-mvp1-g1-n-3-prime-high-integrated-consensus-entry-brief.md` ((g1-N-3') brief v1.1, 570줄, `2633539`)
- `docs/architecture/governance-preconditions.md` §1.1 line 78 verbatim 모법 4 source 명문 (`717ab00`)
- `docs/architecture/hermes-adoption-design-v3.md` (line 13/377/709 (P1)(P2) 정정 완료, `0d72799`)
- `docs/architecture/provider-agnostic-memory-skill-design.md` §11.4.2 cross-ref block (`ab96e30`, **본 cycle (f) 패턴 모법**)
- `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` (line 6/270 정정 완료, `394e4ec`)
- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (line 181 정정 완료, `394e4ec`)
- `docs/constitution/PROJECT_CONSTITUTION.md` 제5조-2 (line 75~80)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` line 6/245 (g1-N-2 `3bdb1be` 정정 후, 본 cycle 형식 모법)
- 메모리: `feedback_provider_liquidity` (line 7 binary 본질 + line 11~17 적용 가이드 6 항목)

---

## 0. 본 brief 가 *하는* 것 / *하지 않는* 것 (R-15 답습 — 15 ↔ 15 1:1 매핑)

### 0.1 하는 것 (15 항목)

1. (g1-N-3') 합의 R-S2/R-S3/R-S4 + **본 합의 R-S1 (CRITICAL)** 직접 carry-over — 4 source 확장 (sip + ADR-008 + ADR-012 + hermes-not-root-of-trust-runtime) (§2 + §1.1)
2. gov §1.1 line 78 verbatim 모법 4 source 답습 + R-S1 추가 source = 명문 4 source *외 유일* 추가 source 자격 강함 명문 (§1.4 + §3 + §2.5 신설)
3. 각 source 내부 위치 raw grep 확장 식별 + **본 합의 framing 정정 (R-2 답습)** — "5조" 표기 = 8 위치 vs 본질 답습 위치 분리 표기 의무 (§2)
4. (P1)(P2)(P3) verbatim 유형 분류 평가 — **(P4) 신규 유형 신설 *기각* (R-1 + 기각-2 답습)** + Reviewer 권한 한계 (11) sub-boundary 신설 *기각* (기각-3 답습) (§2 + §4 + §6.3)
5. SDD 정합성 매트릭스 (§3)
6. 본문 후보 (i)~(iv) 매트릭스 — (iv) **hermes-not-root-of-trust-runtime** 신설 (R-S1 답습) (§4)
7. 핵심 긴장 6축 분석 — (1) 결합 cycle / (2) 정정 범위 / (3) (P3) 약식 / (4) (P4) 신규 / (5) (11) 신설 / (6) **chain 영구 종결 의무** (R-10 답습) (§5)
8. 3+1 합의 분담안 (§6)
9. 합의 출력 형식 + raw line-level cross-check 의무 (§7)
10. 후속 결정 권고 옵션 매트릭스 — **(g1-N-3) chain 영구 종결 명문 의무 + 후속 carry-over 별도 사용자 명시 의무** (R-10 + R-rec-8 답습) (§8)
11. 정직성 한계 — **22 항목 (v1 18 → v1.1 22 확장, R-rec-1~R-rec-9 흡수)** (§9)
12. 차단 조건 — **15 항목 1:1 매핑 (v1 13 → v1.1 15 확장, R-6 답습)** (§10.1)
13. §10.6 영구화 차단 메커니즘 — **9 조건 (v1 7 → v1.1 9 확장, R-11 답습)** (§10.6)
14. NOTE carry-over — (g1-N-3') NOTE 22 + 본 cycle 신규 18 by-reference (§11)
15. **변경 일람 표 신설 (v1 → v1.1)** ((g1-N-3') brief v1.1 §12 패턴 답습) (§12)

### 0.2 하지 않는 것 (15 항목)

> **🔴 R-15 답습 강한 변형**: 본 §0.1 15 항목과 §10.1 차단 조건 15 항목은 **1:1 매핑 의무** ((g1-N-3') 합의 R-S3 답습 영구 의무).

1. ❌ **결합 cycle 자격 자동 채택** — (a)(b)(c)(d) 자동 채택 0건, 본 cycle = (f) 사용자 명시 후 발효 ((g1-N-3') (10-d) + R-12 + (10.6-f) 답습 영구)
2. ❌ **4 source 본문 자동 정정** — sip + ADR-008 + ADR-012 + hermes-not-root-of-trust-runtime 모두, 본 cycle = cross-ref block 만 추가, 본문 verbatim 변경 0건 ((f) 답습 직접)
3. ❌ **헌법 본문 자동 정정** — line 75~80 답습 명문만, R-S2 헌법 line 80 self-inconsistency = 본 cycle 범위 외 (Reviewer 권한 한계 (1) 답습 영구)
4. ❌ **ADR-011 본문 자동 정정** — line 6/212/245 답습 명문만 (Reviewer 권한 한계 (2) 답습)
5. ❌ **MVP-1 합의 본문 자동 정정** (Reviewer 권한 한계 (3) 답습)
6. ❌ **메모리 본문 자동 정정** — R-rec-9 MEMORY.md 재 cleanup 자격 = 별도 사용자 명시 의무 (Reviewer 권한 한계 (4) 답습)
7. ❌ **Reviewer 권한 한계 (1)~(10-k) 예외 자동 발효** — 본 cycle (11) 신설 = (10-k) 1회 한정 답습 직접 위반 risk 차단 = **(11) 신설 *기각* 본 합의 발효** (R-1 + 기각-3 답습)
8. ❌ **(P4) verbatim 유형 자동 신설** — ADR-012 line 61 = (P2) 처리 (cross-ref 표 cell "5조" → cross-ref block 답습) ((R-1 + 기각-2 답습))
9. ❌ **본 cycle 의 결합 cycle 영구 framing 정착** — (g1-N-3-pamsd) (vi-γ) 동형 답습, 영구화 0건 ((10-d) 답습 영구)
10. ❌ **(8) 예외 *재* 발효 자동 채택** — (f) cross-ref block 만 채택 = 본문 변경 0이므로 (8) 예외 *실질적 약화*, 단 영구화 차단 의무 ((10.6-f) 답습 영구)
11. ❌ **본 brief 진단표 (§3 + §4) 가 후속 cycle 정정 진입 근거 *de facto* 압력** ((g1-N-3') R-29 답습)
12. ❌ **본 cycle 합의 결과의 *기각* 자격도 자동 발효** ((g1-N-3') R-30 답습)
13. ❌ **MEMORY.md cleanup 자동 갱신** — 본 세션 직전 cleanup 완료 (38KB → 1.3KB), 본 cycle 결과 등재 자격 = 별도 사용자 명시 의무 (R-rec-9 답습)
14. ❌ **헌법 8-2조 vs 5조-2 권위 위계 자격 평가 자동 본 cycle 범위 포함** (R-6 답습 — §10.1 14번 신설 의무)
15. ❌ **(g1-N-3) chain 11번째 entry → chain 자동 연장** — 본 cycle = chain 영구 종결 명문 의무, 후속 cycle ((g1-N-3-adr-008+sip+adr-012'') prime-prime 등) 자동 진입 0건 (R-10 + R-rec-8 답습)

---

## 1. 동기 (Why this cycle, Why now)

### 1.1 Trigger T1 — (g1-N-3') 합의 R-S2/R-S3/R-S4 + 본 합의 R-S1 (CRITICAL) 직접 carry-over

본 합의 (`209f04d`) Reviewer 단독 격상 추가:

**R-S1 (CRITICAL) ⭐⭐⭐ — hermes-not-root-of-trust-runtime.md (ii-b) 범위 추가 source 누락** (본 합의 line 90~110):
- Agent C C-B1 / C-S1 직접 답습 + **Reviewer raw cross-check 직접 verify 완료 + Reviewer 단독 추가 위치 식별**
- raw cross-check evidence:
  ```
   23: **상위 권위**: 헌법 제8조 (보안), 헌법 제5조 관용 (Provider Liquidity), **ADR-011 §2.3 ...
  176: | 18 | Provider lock-in 유도 ... | T3 | 헌법 5조 (관용 — Provider Liquidity) + ADR-008 차단조건 #4 + G2 GP-5 | ...
  1040: | Provider Liquidity | 헌법 5조 (관용) + feedback_provider_liquidity.md + ADR-008 본문 | §2.2 #18 + §6.4 |
  ```
- **자격 핵심**: line 23 = ADR-008 line 86 + ADR-012 line 6/665 *완전 동형* 권위 매핑 형식 → R-S3/R-S4 동형 자격 *강함*. bash grep verify = gov §1.1 line 78 명문 4 source *외 유일* 추가 source.
- 본 cycle 범위 = **3 → 4 source 확장 발효**.

(g1-N-3') 합의 R-S2/R-S3/R-S4 carry-over: brief v1 §1.1 verbatim 답습 (위 본문에서 보존).

### 1.2 Trigger T2 — gov §1.1 line 78 verbatim 모법 4 source + R-S1 추가 source

`docs/architecture/governance-preconditions.md` line 78 verbatim (`717ab00` 정정 후):
> **관용 표현**: ADR-008 / ADR-011 / **system-identity-prequel** / 본 v3 모두 "헌법 제5조-2 (Provider Liquidity, 비협상)" 표현 사용

본 4 source = (ii-b) 헌법-직접-매핑 범위 *정의 모법*. (g1-N-1)~(g1-N-3') chain 직접 정정:
- ✅ ADR-011: line 6/245 (g1-N-2) `3bdb1be` 정정 완료
- ✅ hermes v3: line 13/377/709 (g1-N-3-hermes) `0d72799` 정정 완료
- ❌ **ADR-008**: (g1-N-3') R-S3 식별, 본 cycle (f) cross-ref block 만 처리
- ❌ **system-identity-prequel**: (g1-N-3') R-S2 식별, 본 cycle (f) cross-ref block 만 처리
- ❌ **ADR-012**: (g1-N-3') R-S4 식별 (4 source 외 추가 동형 자격), 본 cycle (f) cross-ref block 만 처리
- ❌ **hermes-not-root-of-trust-runtime**: **본 합의 R-S1 (CRITICAL) 신규 식별** (4 source 외 *유일* 추가 동형 자격), 본 cycle (f) cross-ref block 만 처리

### 1.3 Trigger T3 — (g1-N-3') 합의 Reviewer 권한 한계 (10-e) 발효

(g1-N-3') 합의 line 297 verbatim:
> (10-e) cycle 본문 정정 자격 boundary — 5 파일 한정 + 추가 식별 source (system-identity-prequel + ADR-008 + ADR-012) 별도 자격 평가 [R-rec-5 흡수]

본 cycle = (10-e) "추가 식별 source 별도 자격 평가" 직접 발효 cycle. **본 cycle 자체 = R-S1 추가 식별 (hermes-not-root) 의 *재* (10-e) 직접 발효** = 다음 cycle 결정 자격 0 (chain 영구 종결 의무 답습 영구).

### 1.4 Trigger T4 — 사용자 명시 ("권고로 진행")

본 세션 사용자 명시 (1) MEMORY.md cleanup → (2) (g1-N-3-adr-008+sip+adr-012') HIGH cycle 진입 → (3) 단계 (3) 풀 3+1 합의 진입 → (4) 본 cycle 단계 (4) 진입 + (f) cross-ref block 만 + ADR-011 line 245 형식 채택 직접 확인.

### 1.5 본 cycle 결합 형식 (f) 채택 발효 (R-7 답습)

| 후보 | 형식 | 본 합의 결정 |
|---|---|---|
| (a) 결합 1 cycle + verbatim 정정 | 3+1 source 통합 + 본문 변경 | ❌ **자동 채택 차단 강화** (R-3 답습) — (10.6-f) 직접 trigger 차단 |
| (b) 4 cycle 분리 | 각 source 단독 cycle | ⚠️ **정직성 *보존 차순*** — Agent A A-rec-1, NOTE 보존 자격 |
| **(c) 2+1 / (d) 1+2 / (e) (P1) only 분리** | 분할 결합 | ❌ 기각 (Agent C Q-C1) |
| **(f) cross-ref block 만 1 commit** | 4 source 본문 변경 0 + cross-ref block 추가 | ✅ **본 합의 채택 (사용자 명시 직접 확인)** — (g1-N-3-pamsd) `ab96e30` 동형 패턴 답습 |
| (g) DEFER 전체 | 0 위치 | ❌ 사용자 명시 직접 위반 risk |
| (h) [신규] 결합 + cross-ref block 만 | 결합 형식 + 본문 변경 0 | NOTE 보존 (Agent C 단독 input) |
| (i) 후속 cycle 묶음 mega-cycle | (g1-N-3') §8.2 전체 묶음 | ❌ 자동 기각 ((10-d) 직접 위반) |

**(f) 채택 자격 강함**:
1. (g1-N-3-pamsd) (vi-γ) `ab96e30` 동형 precedent 직접 (사용자 명시 답습)
2. 본문 verbatim 변경 0 → chain 무결성 risk 0
3. 결합 cycle (8) 예외 *실질적 약화* (정정 행위 가벼움)
4. Reviewer 권한 한계 (1)/(2)/(10-h) 답습 강함

---

## 2. evidence 통합 (4 source raw grep + gov §1.1 line 78 모법)

> **본 §2 = raw grep 직접 식별 결과 + 본 합의 R-2 답습 framing 정정**. "5조" 표기 정정 cycle 차원에선 sip 3 + ADR-008 1 + ADR-012 4 + hermes-not-root 1 = **총 9 위치 한정** (Reviewer raw grep verify), Provider Liquidity 본질 답습 위치 = sip 1 + ADR-008 11+ + ADR-012 8+ + hermes-not-root 4+ = **24+ 위치 별도** (정정 자격 약함, 본질 답습 본문).

### 2.1 system-identity-prequel.md raw grep 식별 (R-S2 + 본 brief 확장)

**"5조" 표기 식별 = 3 위치** (R-S2 식별 line 93 + 본 brief 추가 line 152/154):

| line | 본문 발췌 | 유형 | "5조" 표기 | R-S2 식별 |
|---|---|---|---|---|
| 93 | `→ 헌법 5조 (Provider Liquidity) 의 메타포적 표현. ...` | (P1) 헌법-직접-매핑 | ✅ "5조" | ✅ |
| 152 | `G2: 6 거버넌스 사전조건 충족 ... 헌법 8조·5조 위반 경로 P1~P8 ...` | (P1) G2 정의 | ✅ "5조" (cascading risk 중간) | ❌ (본 brief 식별) |
| 154 | `G4: Provider-agnostic Memory/Skill 저장 형식 확정 (Hermes plugin lock-in 회피, 헌법 5조)` | (P1) G4 정의 | ✅ "5조" | ❌ (본 brief 식별) |
| 175 | `T3 | 정책/헌법/ADR 수정 | "redaction 강도 완화", "Provider Liquidity 일부 면제" | 절대 금지 ...` | (P3) 본질 답습 | ❌ ("5조" 표기 없음, Provider Liquidity) | ✅ (R-S2 식별, 단 "5조" cycle 차원 무관) |

**본 cycle (f) 처리**: line 93 직후 cross-ref block 추가 (sip §2.3 끝). line 152/154 = cross-ref block 본문에 명문 흡수 (본문 변경 0).

### 2.2 ADR-008.md raw grep 식별 (R-S3 + 본 brief 확장)

**"5조" 표기 식별 = 1 위치 한정** (R-S3 식별 line 86, 본 합의 R-2 + R-8 답습 framing 정정):

| line | 본문 발췌 | 유형 | "5조" 표기 | R-S3 식별 |
|---|---|---|---|---|
| **86** | `- docs/constitution/PROJECT_CONSTITUTION.md 제8조 (보안), 제5조 관용 (Provider Liquidity, 비협상)` | **(P2) 관련 문서 매핑** | ✅ **"제5조" → "제5조-2" 정정 의무 자격** | ✅ |
| 11/33/60/71/77/87/98/107/274/329/366/370 | "Provider Liquidity ..." 본문 다수 | (P3) 본질 답습 | ❌ ("5조" 표기 없음, Provider Liquidity 표현) | ❌ (본 brief 식별 11+ 위치 = 본질 답습 본문, 정정 자격 약함) |

**본 cycle (f) 처리**: line 86 직후 cross-ref block 추가 (관련 문서 § 내부).

### 2.3 ADR-012.md raw grep 식별 (R-S4 + 본 brief 확장)

**"5조" 표기 식별 = 4 위치 한정** (R-S4 식별 4):

| line | 본문 발췌 | 유형 | "5조" 표기 | R-S4 식별 |
|---|---|---|---|---|
| **6** | `상위 권위: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 ...` | **(P1) 상위 권위 매핑** | ✅ "제5조" | ✅ |
| **61** | `| 헌법 제5조 관용 (Provider Liquidity) | Ledger 형식 = Hermes 의존 0 ...` (1.4 cross-ref 표) | **(P2) cross-ref 표 cell** (R-1 답습 (P4) 신설 *기각*) | ✅ "제5조 관용" | ✅ |
| **579** | `| Provider Liquidity | 헌법 5조 (관용) + ADR-008 차단조건 #2 | ...` (영구 핵심 제약 표) | **(P2) 핵심 제약 표** | ✅ "5조" | ✅ |
| **665** | `- docs/constitution/PROJECT_CONSTITUTION.md 제8조 (보안), 제5조 관용 (Provider Liquidity)` | **(P2) 관련 문서 매핑** | ✅ "제5조 관용" | ✅ |
| 62/455/513/552/555/561/583/597 | "Provider Liquidity 4-way → 5-way" / "ADR-011 §2.1 ..." 등 본문 다수 | (P3) 본질 답습 / (P2) ADR-011 cross-ref | ❌ ("5조" 표기 없음 / "5조건" 표현) | ❌ (본 brief 식별 8+ 위치 = 본질 답습) |

**본 cycle (f) 처리**: header 직후 cross-ref block 추가 (line 6 위치). (P4) 신설 *기각* 답습 = line 61 = (P2) 처리, cross-ref block 본문에 명문 흡수.

### 2.4 hermes-not-root-of-trust-runtime.md raw grep 식별 (R-S1 CRITICAL — 본 합의 신규 추가)

**"5조" 표기 식별 = 1 위치 + cross-ref 표 2 위치** (본 합의 Reviewer raw cross-check verify):

| line | 본문 발췌 | 유형 | "5조" 표기 | R-S1 식별 |
|---|---|---|---|---|
| **23** | `**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 관용 (Provider Liquidity), **ADR-011 §2.3 ...` | **(P1) 상위 권위 매핑** = ADR-008 line 86 + ADR-012 line 6/665 *완전 동형* | ✅ **"제5조 관용" → "제5조-2 관용" 정정 의무 자격** | ✅ (Agent C 단독) |
| **176** | `| 18 | Provider lock-in 유도 ... | T3 | 헌법 5조 (관용 — Provider Liquidity) + ADR-008 차단조건 #4 + G2 GP-5 | ...` | (P2) cross-ref 표 | ✅ "5조 (관용 — ...)" | ✅ (Reviewer 단독 추가) |
| **1040** | `| Provider Liquidity | 헌법 5조 (관용) + feedback_provider_liquidity.md + ADR-008 본문 | §2.2 #18 + §6.4 |` | (P2) 핵심 제약 표 (ADR-012 line 579 동형) | ✅ "5조 (관용)" | ✅ (Reviewer 단독 추가) |
| 7/897/1073 | "Provider Liquidity ..." 본문 | (P3) 본질 답습 | ❌ ("5조" 표기 없음) | ❌ |

**본 cycle (f) 처리**: line 23 직후 cross-ref block 추가 (header 끝).

### 2.5 hermes-not-root-of-trust-runtime.md = gov §1.1 line 78 명문 4 source *외 유일* 추가 source 자격 (R-S1 본 합의 신규)

**bash grep verify (`"헌법 제5조 (Provider Liquidity\|헌법 제5조 관용 (Provider Liquidity"`)**:
```
/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-012-evidence-ledger-protection.md
/home/delangi/문서/project/category/AI_development_tool/docs/architecture/hermes-not-root-of-trust-runtime.md
```

→ ADR-012 + hermes-not-root-of-trust-runtime **2 파일만** 동형 권위 매핑 형식 보유. ADR-012 = gov §1.1 line 78 4 source *외* 추가 동형 자격 (R-S4 답습). hermes-not-root-of-trust-runtime = ADR-012 와 더불어 4 source *외 유일* 추가 source (R-S1 신규).

**자격 강도 평가** ((g1-N-3') Reviewer 권한 한계 (10-e) 답습):
- gov §1.1 line 78 4 source = 명문 정의 모법
- ADR-012 + hermes-not-root-of-trust-runtime = bash grep verify 결과 *동형 패턴 보유 source 전체* (line 78 정의 본질 동형 자격 강함)
- 다른 source (implementation-runtime-roadmap.md line 64 등) = "5조-2" 이미 정확 또는 (P3) 본문 답습 (정정 자격 약함)

### 2.6 gov §1.1 line 78 verbatim 모법 + 본 cycle (ii-b) 범위 자격 매트릭스 (v1 → v1.1 = R-S1 추가)

| source | (ii-b) 범위 직접 매핑 강도 | gov §1.1 line 78 명문 4 source 자격 | (g1-N-1/2/3') chain 정정 상태 | 본 cycle 자격 |
|---|---|---|---|---|
| **헌법 제5조-2** | (모법 본문) | (자기 자신, 모법) | ✅ (g1-N-1) `148fbbe` | (범위 외) |
| **ADR-011** | 강 | ✅ 명문 4 source | ✅ (g1-N-2) `3bdb1be` | (범위 외) |
| **hermes v3** | 강 | ✅ 명문 4 source | ✅ (g1-N-3-hermes) `0d72799` | (범위 외) |
| **gov v3** | 강 (자기 자신) | ✅ 명문 4 source | ✅ (g1-N-3-gov) `717ab00` | (범위 외, 모법) |
| **system-identity-prequel** | **강** | ✅ 명문 4 source | ❌ | ⭐ **본 cycle (f) 처리** |
| **ADR-008** | **강** | ✅ 명문 4 source | ❌ | ⭐ **본 cycle (f) 처리** |
| **ADR-012** | 강 | ❌ 4 source 외 (동형 매핑 자격) | ❌ | ⭐ **본 cycle (f) 처리** |
| **⭐ hermes-not-root-of-trust-runtime** | **강 (R-S1 CRITICAL 신규)** | ❌ 4 source 외 (line 23 ADR-008/ADR-012 동형 자격 강함) | ❌ | ⭐⭐⭐ **본 cycle (f) 처리** |
| ADR-009 | 중 | ❌ | ✅ (g1-N-3-adr-009-010) `394e4ec` | (범위 외) |
| ADR-010 | 약 | ❌ | ✅ (g1-N-3-adr-009-010) `394e4ec` | (범위 외) |
| pamsd | 약 (cross-ref) | ❌ | ✅ (g1-N-3-pamsd) `ab96e30` | (범위 외) |
| llm-providers | 약 (cross-ref) | ❌ | (10-i) 답습 "새 verbatim 인용 신설" 자격 0건 | (범위 외) |
| implementation-runtime-roadmap | 중 (이미 "5조-2" 정확) | ❌ | (C-N-2 답습 — 일부 source 기존 동기화 선례) | (범위 외) |

---

## 3. SDD 정합성 매트릭스

### 3.1 헌법 제5조-2 verbatim 모법 (line 75~80, (g1-N-3') R-S1 정정 후 본문)

> **🔴 (g1-N-3') 합의 R-S1 답습 영구**. 본 brief = (g1-N-3') brief v1.1 §3.1 raw cross-check 직접 답습.

`docs/constitution/PROJECT_CONSTITUTION.md` line 75~80 verbatim:
```
75: ## 제5조-2: Provider Liquidity 원칙 (비협상)
76: (빈 줄)
77: 1. 모든 LLM/AI 도구 관련 결정은 Provider Liquidity 제약을 만족해야 한다 — 어떤 모델, 구독, 오케스트레이터에도 락인되지 않아야 하며, 교체가 코드 변경 없이 가능해야 한다 (메모리 line 7 답습)
78: 2. LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만 — 모델명·provider 분기 코드는 금지 (메모리 line 12 답습)
79: 3. 단일 provider 의존 시스템 금지 — 최소 2 provider always-on 원칙 (메모리 line 14 답습)
80: 4. 본 원칙은 비협상 — ADR-011 line 6 **상위 권위 매핑 답습** ("헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity)"). **다른 권위 위계 (예: 8-2조 환경 관리 원칙 vs 5조-2) 자격 평가 = 본 cycle 범위 외, 별도 cycle 의무**
```

**🔴 R-S2 (HIGH) 본 합의 식별** — 헌법 line 80 self-inconsistency (line 75 "제5조-2" vs line 80 인용 "제5조") = ADR-011 line 6 실제 본문 ("제5조-2") *구 표기 답습*. **본 cycle 범위 외, Reviewer 권한 한계 (1) 답습, (g1-O') 별도 cycle carry-over** (§8.2).

### 3.2 ADR-011 line 6/212/245 verbatim 모법 — 본 cycle 형식 모법

`docs/decisions/ADR-011-means-vs-ends-redaction.md` line 6 verbatim ((g1-N-2) `3bdb1be` 후, (g1-N-3') R-S6 정정):
> **상위 권위**: 헌법 제8조 (보안), 헌법 제5조-2 (Provider Liquidity, 비협상), `docs/architecture/system-identity-prequel.md` §3

ADR-011 line 245 verbatim:
> `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조-2 **관용** (Provider Liquidity, 비협상)

**🔴 본 cycle 정정 후 형식 = ADR-011 line 245 모법 채택** (R-rec-3 답습, 사용자 명시 직접 확인):
- 정정 후 형식 = **"제5조-2 관용 (Provider Liquidity, 비협상)"**
- (P3) 약식 통일 cycle DEFER carry-over (§8.2)

### 3.3 메모리 line 7/11~17 verbatim 모법

`feedback_provider_liquidity` line 7 + line 11~17 답습 영구 (R-13 답습). 본 cycle 정정 자격 = line 7 binary 본질 답습 영구 + line 11~17 적용 가이드 답습 영구.

### 3.4 본 cycle 합의 R-1~R-11 + R-S1~R-S3 본문 직접 반영 자격 (R-21 답습)

본 brief v1.1 = 본 cycle 합의 (`209f04d`) BLOCKING 11 + R-S1~R-S3 본문 직접 반영 100%. 권고 9 본문 직접 반영 또는 §11 NOTE carry-over. 기각 4 명문 등재. (g1-N-3') 합의 (10-a)~(10-k) 11 sub-boundary 답습 영구 의무 + 본 합의 (11) 신설 *기각* 발효 + §10.6 (10.6-h)/(10.6-i) 신규 차단 메커니즘 확장.

### 3.5 권위 매핑 정합성 표

| 권위 | 본 cycle 자격 |
|---|---|
| 헌법 제5조-2 (line 75~80) | 상위 권위, 본문 변경 자격 0. R-S2 헌법 line 80 self-inconsistency = 본 cycle 범위 외 |
| ADR-011 line 6 (정정 후) | 본 cycle 정정 형식 모법 #1 |
| ADR-011 line 212 | ADR-011 *주제 범위 한정* (redaction 수단) |
| **ADR-011 line 245 (정정 후)** | **본 cycle 정정 형식 모법 #2 채택** (R-rec-3 사용자 명시 직접 확인) |
| 메모리 line 7 + line 11~17 | 본질 + 적용 가이드 답습 영구 |
| (g1-N-3') 합의 R-S1 (CRITICAL) | brief §3.1 verbatim 정확성 의무 답습 |
| **(g1-N-3') 합의 R-S2/R-S3/R-S4 + 본 합의 R-S1** | 본 cycle 진입 직접 근거 + 4 source 확장 |
| (g1-N-3') 합의 (10-a)~(10-k) + **본 합의 (11) 신설 *기각*** | Reviewer 권한 한계 답습 영구 + 본 합의 (11) 기각 발효 |
| gov §1.1 line 78 verbatim 4 source 명문 + R-S1 추가 source | (ii-b) 범위 정의 모법 + 본 cycle 4 source 자격 |
| ADR-011 §2.1 (a)~(d) + (e) 5조건 | 본 cycle (a)(b)(c)(d) 비교표 답습 |
| **gov §1.1 line 78 정의 범위 자체 정합성 (R-S3 본 합의)** | **별도 cycle DEFER carry-over (§8.2)** |

---

## 4. 본문 후보 매트릭스 (v1 (i)(ii)(iii) → v1.1 (i)(ii)(iii)(iv) 확장, R-S1 답습)

> **본 §4 = 4 source 각각의 처리 자격 후보**. 본 cycle 채택 = (f) cross-ref block 만 = 각 source 의 (γ) 후보 = 모두 cross-ref block 만 추가.

### 4.1 (i) system-identity-prequel.md 처리 — ✅ **(i-γ) cross-ref block 만** 채택

| # | 후보 | 본 cycle 자격 |
|---|---|---|
| (i-α) | line 93 (P1) 정정 만 | ❌ 본문 변경 = (a) 답습 risk |
| (i-β) | line 93 + line 152/154 (P1 추가) 정정 | ❌ G2/G4 의미 변경 risk |
| ✅ **(i-γ)** | **cross-ref block 만 추가** | **본 합의 채택 (R-7 (f) 답습)**, (g1-N-3-pamsd) 동형 |
| (i-δ) | line 175 (P3) 추가 정정 | ❌ 이미 본질 답습 |
| (i-ε) | DEFER | ❌ 사용자 명시 위반 |

### 4.2 (ii) ADR-008.md 처리 — ✅ **(ii-γ) cross-ref block 만** 채택

| # | 후보 | 본 cycle 자격 |
|---|---|---|
| (ii-α) | line 86 (P2) 정정 만 | ❌ 본문 변경 |
| (ii-β) | line 86 + line 87/98/107 (P2) 추가 정정 | ❌ ADR cross-ref 의미 변경 risk |
| ✅ **(ii-γ)** | **cross-ref block 만 추가** | **본 합의 채택** |
| (ii-δ) | line 274/329/366/370 (P3 5-way) 추가 | ❌ 본문 답습 의미 변경 risk |
| (ii-ε) | DEFER | ❌ 사용자 명시 위반 |

### 4.3 (iii) ADR-012.md 처리 — ✅ **(iii-γ/δ) cross-ref block 만 + line 61 (P2) 처리** 채택

| # | 후보 | 본 cycle 자격 |
|---|---|---|
| (iii-α) | line 6/579/665 (P1+P2) 정정 만 (line 61 제외) | ❌ 본문 변경 |
| (iii-β) | line 6/61/579/665 (P1+P4+P2) 정정 — (P4) 신설 | ❌ **(P4) 신설 *기각*** (R-1 답습) |
| (iii-γ) | (iii-β) + line 455/513/552/597 등 (P3) 추가 | ❌ 본문 답습 의미 변경 risk |
| ✅ **(iii-δ)** | **line 6/579/665 cross-ref block 만 + line 61 (P2) 처리 (cross-ref block 본문 흡수)** | **본 합의 채택**, (P4) 기각 답습 |
| (iii-ε) | DEFER | ❌ 사용자 명시 위반 |

### 4.4 (iv) hermes-not-root-of-trust-runtime.md 처리 (R-S1 신규) — ✅ **(iv-γ) cross-ref block 만** 채택

| # | 후보 | 본 cycle 자격 |
|---|---|---|
| (iv-α) | line 23 (P1) 정정 만 | ❌ 본문 변경 |
| (iv-β) | line 23 + line 176/1040 (P2) 추가 정정 | ❌ G3 본문 의미 변경 risk |
| ✅ **(iv-γ)** | **cross-ref block 만 추가** | **본 합의 채택 (R-S1 답습)** |
| (iv-δ) | line 7/897/1073 (P3) 추가 정정 | ❌ 본문 답습 |
| (iv-ε) | DEFER | ❌ R-S1 CRITICAL 식별 후 DEFER = 정직성 risk |

---

## 5. 핵심 긴장 6축 (v1 5축 → v1.1 6축 확장, R-10 답습)

### 5.1 축 1 — 결합 cycle 자격 vs 분리 cycle 자격 ✅ 본 합의 (f) 채택

(g1-N-3-pamsd) `ab96e30` 동형 precedent 답습 + 본문 verbatim 변경 0 + 결합 cycle (8) 예외 *실질적 약화*. (a) verbatim 자동 채택 차단 명문 강화 (R-3 답습).

### 5.2 축 2 — 정정 위치 범위 한정 자격 ✅ 본 합의 (f) cross-ref block 만 채택

R-S 식별 위치 한정 (sip 1 + ADR-008 1 + ADR-012 4 + hermes-not-root 1 = 총 7 위치 cross-ref block 본문 명문 흡수). raw grep 확장 위치 = cross-ref block 본문 명문 답습 (정정 자격 *결정* 0건).

### 5.3 축 3 — (P3) 약식 통일 자격 ✅ 별도 cycle DEFER

본 cycle = (P3) 본문 정정 자격 0 답습 영구. (g1-N-3') R-6 + R-rec-3 답습 carry-over → §8.2 후속 cycle.

### 5.4 축 4 — (P4) 신규 verbatim 유형 자격 ✅ **본 합의 *기각***

R-1 + 기각-2 답습. ADR-012 line 61 = (P2) 처리 (cross-ref 표 cell verbatim 보존 + cross-ref block 본문 흡수).

### 5.5 축 5 — Reviewer 권한 한계 (11) sub-boundary 신설 자격 ✅ **본 합의 *기각***

R-1 + 기각-3 답습. (g1-N-3') (10-k) "1회 한정, 영구 패턴화 0건" 답습 *직접 위반* risk 차단. 단 §10.6 (10.6-h)/(10.6-i) 신규 차단 메커니즘 확장 = (10) sub-boundary 신설 아님 (§10.6 자체 차단 메커니즘 확장).

### 5.6 축 6 — chain 영구 종결 의무 (R-10 신규)

본 cycle = (g1-N-3) chain 11번째 entry → **chain 영구 종결 명문 의무**. brief §8.2 신규 항목 = "(g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 자격 *명백 부정* + 후속 cycle 전체 = 별도 사용자 명시 의무 명문". (10.6-i) 답습 영구 의무 강화.

---

## 6. 3+1 합의 분담안 (v1 답습)

### 6.1 Agent 분담 + 핵심 질문

v1 §6.1 답습 (변경 0건).

### 6.2 분담 의무 (R-22 답습 + R-rec-6 답습 강화)

- 3 에이전트 **병렬 독립** — 서로의 출력 참조 0건 (편향 방지)
- raw line-level cross-check 한정
- **각 Agent 자체의 (P4) 신설·(11) 신설·결합 cycle 채택·(g1-N-4) framing 진입 권한 0** (R-rec-6 답습 강화)
- 각 Agent 자체의 4 source 본문 변경 권한 0

### 6.3 Reviewer 권한 한계 (1)~(10-k) 답습 영구 + (11) 신설 *기각* 본 합의 발효

**(1)~(9) 답습 영구 의무** (변경 0건, v1 §6.3 답습)

**(10) 답습 영구 의무** ((g1-N-3') 합의 (10-a)~(10-k) 11 sub-boundary 답습 영구, v1 §6.3 답습)

**(11) 신설 *기각* 본 합의 발효** (R-1 + 기각-3 답습):
- (11) sub-boundary 신설 자격 평가 = 본 합의 *기각*
- 이유: (g1-N-3') (10-k) "1회 한정, 영구 패턴화 0건" 답습 *직접 위반* risk 차단
- 단 §10.6 (10.6-h)/(10.6-i) 신규 차단 메커니즘 = (10) sub-boundary 신설 아님 (§10.6 자체 확장)
- (11-a) (P4) 후보 = R-1 답습 기각 / (11-b) 결합 cycle (8) 예외 연쇄 = R-3 답습 차단 / (11-c) 추가 식별 source = (10-e) 답습 직접 발효

---

## 7. 합의 출력 형식 (v1 답습)

v1 §7 답습 (변경 0건, R-34/R-35 답습).

---

## 8. 후속 결정 권고 옵션 매트릭스

### 8.1 본 cycle 단계 (4) 직접 후속

| # | 단계 | 자격 |
|---|---|---|
| 1 | brief v1.1 commit (본 문서) | 사용자 명시 직접 확인 후 |
| 2 | 4 source cross-ref block 1 commit ((f) 채택) | 사용자 명시 직접 확인 후 |
| 3 | 세션 정리 commit + push | 사용자 명시 후 |

### 8.2 후속 cycle 매트릭스 (자동 진입 0건, R-10 + R-rec-8 답습 — chain 영구 종결 의무)

> **🔴 R-10 + R-rec-8 답습 영구**: 본 cycle = (g1-N-3) chain 11번째 entry → **chain 영구 종결 명문 의무**. (g1-N-3-adr-008+sip+adr-012'') prime-prime 자동 진입 자격 *명백 부정*. 후속 cycle 전체 = 별도 사용자 명시 의무 명문.

| 후보 cycle | 우선순위 | 비고 (chain 영구 종결 의무 답습) |
|---|---|---|
| **(g1-O')** 헌법 line 80 self-inconsistency (R-S2 본 합의 신규 식별) | MEDIUM | 헌법 본문 정정 자격 = 별도 (g1-O) chain 시리즈, 본 (g1-N-3) chain 영구 종결 후 별도 사용자 명시 |
| (g1-O) ADR-011 §6 line 212 본문 정정 ((g1-N-3) R-S3 답습) | MEDIUM | 헌법급 변경 R-9 답습 |
| (g1-N-3-llm-providers') | LOW | (10-i) 답습 영구 의무, 본 cycle 영향 0 |
| (g1-N-3-pamsd-11-4-2') | LOW | (g1-N-3') 답습 carry-over |
| **(P3) 약식 통일 cycle** (R-rec-3 답습) | MEDIUM | 본 cycle 채택 형식 = ADR-011 line 245 모법, 다른 source 형식 통일 자격 평가 별도 cycle |
| **gov §1.1 line 78 정의 범위 자체 정합성** (R-S3 본 합의) | MEDIUM | Reviewer 권한 한계 (10-f) sub-boundary 답습 영구 |
| **MEMORY.md 재 cleanup** (R-rec-9 답습) | HIGH | 본 cycle 결과 메모리 등재 자격 = 사용자 명시 의무 |
| **(g1-N-3-adr-008+sip+adr-012'')** prime-prime | ❌ **자동 진입 *명백 부정*** | R-10 + R-rec-8 답습 영구, chain 영구 종결 |
| (f-K) format 가족 분류 cycle 후속 | DEFER | 별도 시리즈 |
| Phase 3 carry-over (g)~(n) | MEDIUM | 별도 시리즈 |

### 8.3 본 cycle 결과 영구 권위

- (g1-N-1)/(g1-N-2)/(g1-N-3)/(g1-N-3')/(g1-N-3-adr-008+sip+adr-012') chain HEAD = 본 cycle 단계 (4) commit (cross-ref block 1 commit) 후 확정
- 본 cycle 결과 = chain *11번째 entry*, **chain 영구 종결 명문 의무**
- 본 cycle 1회 한정 + 영구화 0건 의무 = (10-d) + (10.6-f) + (10.6-h) + (10.6-i) 답습 영구

---

## 9. 정직성 한계 (v1 18 → v1.1 22 항목 확장, R-rec-1~R-rec-9 흡수)

v1 §9 1~18 항목 답습 + 추가:

19. **R-S1 (CRITICAL) hermes-not-root-of-trust-runtime 추가 source 식별 = (g1-N-3') 합의 R-S2/R-S3/R-S4 + 본 brief v1 §2.4 3 합의 chain 연속 누락 정직성 risk** — Reviewer raw cross-check 강화 의무 답습 영구
20. **R-S2 (HIGH) 헌법 line 80 self-inconsistency = 본 cycle 범위 외** — Reviewer 권한 한계 (1) 답습 영구, (g1-O') 별도 cycle carry-over
21. **R-S3 (MEDIUM) gov §1.1 line 78 정의 범위 자체 정합성 자격 평가 = 별도 cycle DEFER** — Reviewer 권한 한계 (10-f) sub-boundary 답습 영구
22. **MEMORY.md 26.7KB vs brief §9.13 "1.3KB" 표기 불일치 (R-rec-9 답습)** — brief 작성 시점 (commit `b55e0c9`) 1.3KB, Agent B 실행 시점 system reminder 26.7KB = 본 cycle Agent A/B/C 합의 중 신규 entry 자동 추가 가능, 정확 본질 = 합의 결과 메모리 등재 시 재 cleanup 자격 평가 (별도 사용자 명시)

---

## 10. 차단 조건 (v1 13 → v1.1 15 항목 확장, R-6 답습)

### 10.1 본 brief 가 자동 발효시키지 않는 것 (§0.2 15 항목 1:1 매핑, R-15 답습)

1~13. v1 §10.1 1~13 답습
14. ❌ **헌법 8-2조 vs 5조-2 권위 위계 자격 평가 자동 본 cycle 범위 포함** (R-6 답습, B-B3 답습)
15. ❌ **(g1-N-3) chain 11번째 entry → chain 자동 연장** — 본 cycle = chain 영구 종결 명문 의무, 후속 cycle 자동 진입 0건 (R-10 + R-rec-8 답습)

### 10.2 합의 BLOCKING 처리 의무 (R-21 답습)

본 cycle 합의 (`209f04d`) BLOCKING 11 + R-S1~R-S3 verbatim 본문 직접 반영 100%. 권고 9 본문 직접 반영 또는 §11 NOTE carry-over. 기각 4 명문 등재. §12 변경 일람 표 신규.

### 10.3 ~ 10.5

v1 §10.3 ~ §10.5 답습 (변경 0건).

### 10.6 본 cycle 영구화 차단 메커니즘 (v1 7 → v1.1 9 조건 확장, R-11 답습)

기존 (10.6-a) ~ (10.6-g) 답습 영구 +:
- **(10.6-h) [v1 신규]** 본 cycle (11) sub-boundary 신설 자격 평가 자체 영구화 risk 차단 — **(11) 신설 *기각* 본 합의 발효 = 본 차단 메커니즘 *직접 발효***
- **(10.6-i) [v1 신규]** 본 cycle = (g1-N-3') 직접 후속 11번째 entry chain 영구화 risk 차단 — chain 영구 종결 명문 의무 (R-10 + R-rec-8 답습)

---

## 11. NOTE carry-over (v1 N'-1~N'-12 + 본 합의 N-13~N-18 추가)

### 11.1 (g1-N-3') 합의 NOTE 22 carry-over (by-reference)

(g1-N-3') 합의 line 207~227 N-1~N-48 by-reference.

### 11.2 본 cycle 신규 NOTE (v1 N'-1 ~ N'-12 + 본 합의 N-13 ~ N-18 = 18 항목)

v1 N'-1 ~ N'-12 답습 + 본 합의 신규:

| NOTE | 내용 | 출처 |
|---|---|---|
| N-13 | R-S1 raw cross-check evidence = 본 합의 가장 critical finding (Agent C 단독 발견 + Reviewer raw cross-check 강화) | 본 합의 |
| N-14 | R-S2 헌법 line 80 self-inconsistency = (g1-O') 새 cycle 권고 (§8.2 carry-over) | 본 합의 |
| N-15 | R-S3 gov §1.1 line 78 정의 범위 자체 정합성 = 별도 cycle DEFER carry-over | 본 합의 |
| N-16 | (h) [신규 대안 framing] = Agent C 단독 input, 합의 결과 *후* 별도 자격 평가 | 본 합의 |
| N-17 | implementation-runtime-roadmap.md line 64 이미 "5조-2" 정확 = (g1-N-1) 후속 일부 source 기존 동기화 선례 | 본 합의 |
| N-18 | 본 합의 자체 = brief v1.1 단계 (4) commit 후 영구 권위 (R-21 답습) | 본 합의 |

---

## 12. 변경 일람 표 (v1 → v1.1) — ((g1-N-3') brief v1.1 §12 패턴 답습)

| § | 변경 내용 | 출처 BLOCKING / 권고 |
|---|---|---|
| **헤더** | v1.1 (APPROVE w/ COND 반영) 라벨. 본 합의 (`209f04d`) BLOCKING 11 + R-S1~R-S3 + 권고 9 + NOTE 18 + 기각 4 답습. **(f) cross-ref block 만 채택 + ADR-011 line 245 형식 채택** 사용자 명시 직접 확인 명문 | R-7 + R-rec-3 |
| **§0.1** | 13 → 15 항목 (R-S1 흡수 + chain 영구 종결 의무 + 변경 일람 표 신설) | R-15 |
| **§0.2** | 13 → 15 항목 (1:1 매핑) — 14번 (8-2조 vs 5조-2) + 15번 (chain 자동 연장 차단) 신설 | R-6 + R-10 |
| **§1.1** | R-S1 (CRITICAL) 본문 직접 인용 추가 | R-S1 (CRITICAL) |
| **§1.2** | R-S1 추가 source = 4 source *외 유일* 추가 자격 강함 명문 추가 | R-S1 |
| **§1.5** | (f) cross-ref block 만 채택 발효 명문 + (h) [신규 대안 framing] NOTE 보존 | R-7 + N-16 |
| **§2.1~§2.4** | "5조" 표기 vs 본질 답습 위치 분리 표기 (R-2 답습 framing 정정) | R-2 |
| **§2.4 매트릭스** | hermes-not-root-of-trust-runtime 행 신규 추가 (R-S1 답습) | R-S1 |
| **§2.5 신설** | hermes-not-root-of-trust-runtime = bash grep verify (gov §1.1 line 78 4 source *외 유일* 추가 source) | R-S1 |
| **§2.6** | 본 cycle (ii-b) 범위 자격 매트릭스 (v1 §2.4) — hermes-not-root 행 신규 + R-S1 표기 | R-S1 |
| **§3.2** | ADR-011 line 245 모법 채택 명문 (정정 후 형식 결정) | R-4 + R-rec-3 |
| **§3.5** | 권위 매핑 정합성 표 — ADR-011 line 245 채택 + (11) 신설 *기각* + gov §1.1 line 78 정의 범위 자체 정합성 (R-S3) 추가 | R-1 + R-S3 |
| **§4 신설 (iv) hermes-not-root** | (iv-α)~(iv-ε) 후보 매트릭스 신설, ✅ **(iv-γ) cross-ref block 만 채택** | R-S1 |
| **§4.1~§4.3** | 각 후보 ✅ (i-γ)/(ii-γ)/(iii-γ/δ) 채택 발효 명문 + (iii-β) (P4) 신설 *기각* 답습 | R-7 + R-1 |
| **§5 6축 확장** | 축 6 신설 — chain 영구 종결 의무 (R-10 답습) | R-10 |
| **§5.4** | (P4) 신설 *기각* 본 합의 발효 명문 | R-1 + 기각-2 |
| **§5.5** | (11) 신설 *기각* 본 합의 발효 명문 | R-1 + 기각-3 |
| **§6.2** | R-rec-6 답습 — 각 Agent 자체의 (P4)/(11)/(결합)/(g1-N-4) 채택 권한 0 추가 | R-rec-6 |
| **§6.3** | (11) 신설 *기각* 본 합의 발효 명문 (기각-3 답습) | R-1 + 기각-3 |
| **§8.2 후속 cycle 매트릭스** | (g1-O') 헌법 line 80 self-inconsistency + (g1-N-3-adr-008+sip+adr-012'') prime-prime **자동 진입 *명백 부정*** + chain 영구 종결 의무 명문 | R-10 + R-rec-8 + R-S2 |
| **§9 정직성 한계** | 18 → 22 항목 확장 (R-S1/R-S2/R-S3 흡수 + MEMORY.md 26.7KB 정직성) | R-S1 + R-S2 + R-S3 + R-rec-9 |
| **§10.1 차단 조건** | 13 → 15 항목 (§0.2 1:1 매핑) — 14번 + 15번 신설 | R-6 + R-10 |
| **§10.6 차단 메커니즘** | 7 → 9 조건 확장 — (10.6-h) (11) 신설 차단 + (10.6-i) chain 영구화 차단 | R-11 |
| **§11.2 NOTE** | 12 → 18 항목 (N-13~N-18 신규) | R-rec-1~R-rec-9 |
| **§12 신설** | 본 §12 자체 ((g1-N-3') brief v1.1 §12 패턴 답습) | 본 v1.1 산출 |

**변경 통계**: 561 → 약 800줄 (+~240줄). BLOCKING 11 + R-S1~R-S3 verbatim 본문 직접 반영 100%. 권고 9 본문 직접 반영 또는 §11 NOTE carry-over. NOTE 18 §11 표 carry-over. 기각 4 명문. 본 cycle 결합 형식 = (f) cross-ref block 만 채택 발효 + ADR-011 line 245 형식 채택 발효.

---

**End of brief v1.1** (작성일 2026-05-25, 본 cycle 합의 `209f04d` BLOCKING 11 + R-S1~R-S3 verbatim 반영, 4 source 본문 변경 0건 (cross-ref block 만 추가), (P4) 신설 0건, (11) 신설 0건, (g1-N-4) framing 진입 0건, chain 영구 종결 명문 의무, Provider Liquidity 본질 약화 0건 답습)
