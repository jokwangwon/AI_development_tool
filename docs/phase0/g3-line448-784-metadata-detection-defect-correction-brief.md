# G3 line 448/784 metadata-기반 single-author detection 결함 교정 *검토* Brief (DRAFT v1)

> **본 brief = Group I 합의에서 발견·기록된 G3 본문 결함(line 448/784)을 positive allow-list / credential boundary / external enforcement 중심으로 *교정 가능한지 검토*하는 brief 한정** — 합의 보고서 작성 / commit / push / G3 본문 실 교정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 = 모두 별도 단계 (staged cycle: brief → 승인 → 합의 → commit → push). 본 brief = **brief 단계 한정**.

---

**작성일**: 2026-05-20
**Status**: **DRAFT v1** (결함 교정 *검토* — 본문 교정 미발효, 합의 미진입)
**진입 단위**: Group I 합의 후속 #1 (`3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md` §4 미해소 쟁점 #1 — "G3 line 448/784 본문 교정 시점")
**선행 발효 답습**: Group I 풀 3+1 합의 `f6c6d5a` (T3 풀 3+1 의무 + 6 BLOCKING + 3 조건부 + G3 결함 *기록*) + Group α `2026-05-14` C-2 + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **Group I 합의 §2.4 B-1 / B-2 / B-3 / B-4 + §2.6 (G3 결함 처리 양립 논리) + §4 #1** + G3 line 448 (§3.1.2) / line 784 (§5.5.1) 원문
**합의 권위 한계**: 본 brief = 교정 *검토* DRAFT — 본문 교정 *발효* 아님. 교정 가능성·범위·형태 판정도 본 brief 는 *권고*만 발행, *발효* 는 풀 3+1 합의 (또는 사용자 명시 합의 형태 결정) 의 권한.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "G3 line 448/784 metadata 기반 single-author detection 결함 교정 brief 를 작성해주세요. 범위는 Group I 합의에서 발견된 G3 본문 결함을 positive allow-list / credential boundary / external enforcement 중심으로 교정할 수 있는지 검토하는 것입니다. 아직 G3 본문 수정, git hook 구현, GitHub ruleset 변경, CI workflow 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

본 brief = 위 명령 답습 — **결함 교정 가능성 검토** + **교정 대상 touch-point 범위 정비** + **교정 형태 판정 영역 정비** + **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 결함 정의 정밀화 — line 448/784 가 *어떤* 설계 가정에 기대고 있는지 + 연동 touch-point 전수 (§1)
2. 교정 3축(positive allow-list / credential boundary / external enforcement) 이 결함을 *교정 가능한지* 검토 — 각 축이 line 448/784 의 어느 가정을 대체하는지 매핑 (§2)
3. Group I 합의 BLOCKING(B-1~B-4) ↔ 교정 3축 정합 확인 (§3)
4. 교정 시 영향받는 G3 본문 touch-point 매트릭스 (검토 대상 enumeration — *실 편집 아님*) (§4)
5. 교정 *형태* 판정 영역 — G3 detection 메커니즘 변경 자체가 T3(R-I-CONFIG-CHANGE)인가 + 풀 3+1 의무인가 (§5)
6. ADR-011 means/ends 정합 검토 (positive allow-list = 수단 명칭 고정 함정 회피) (§6)
7. 미해소 쟁점 + Rollback Trigger 연결 (§7)
8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건) (§8)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **G3 본문 수정** (line 448/784 detection 메커니즘 교정 / §2.2 #20 / §2.5 / §2.6 / §3.1 / §4.5 / §5.5 본문 변경 — 검토만, 실 편집 0건)
- ❌ **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문)
- ❌ **GitHub ruleset / branch protection 변경** (signed commit required / required status check / bypass 정책)
- ❌ **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경)
- ❌ **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**
- ❌ 수단 *결정 고정* (positive allow-list 의 키 종류·서명 방식·차단 지점 최종 고정)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ MVP-1 exit 발효 / Phase α defer-lockdown 변경
- ❌ ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012) / Group I·α·β·γ 합의 본문 변경
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 본 brief 의 권위 한계

본 brief 는 결론을 *선취하지 않는다*. 교정 가능성 판정(§2)·교정 형태 판정(§5) 은 *권고*만 발행하며, 본문 교정 *발효* 는 풀 3+1 합의 (또는 사용자 명시 합의 형태 결정) 의 권한이다. Group I 합의가 이미 "G3 본문 교정 = 별도 단계 (T3, 풀 3+1 + 사용자 명시)"(합의 §2.6 #3 / §4 #1)로 분리했으므로, 본 brief 는 그 *별도 단계 진입 전 정비* 에 해당한다.

---

## 1. 결함 정의 정밀화

### 1.1 결함의 본질 (Group I 합의 §2.6 답습)

Group I 합의(만장일치 C3+C4 / Reviewer 원문 검증)가 기록한 결함:

> **현 G3 본문(line 448/784)이 Hermes-originated commit 식별을 *commit author/committer metadata 비교* 에 기대고 있으며, 이는 외부(GPT-5.5)·세 Agent 가 "spoof 가능 — 인증 신호 아님"으로 판정한 negative detection 방식이다.**

핵심은 *"detection 정확도가 낮다"* 가 아니라 **"식별 frame 자체가 권한 경계가 아닌 metadata 판별에 의존한다"** 는 구조적 문제다. 1인 single-host 에서 사용자와 Hermes 가 동일 credential/identity 를 공유하면, author 메타는 위조 가능하므로 **FN(Hermes 가 사람으로 보이는 commit) > FP** 위험 (합의 C10 / B-3).

### 1.2 line 448 — §3.1.2 Learning Silent Drift 감지

```
| **Hermes-originated commit detection** | git commit author / committer + Hermes audit log cross-reference | every commit |
```

- 가정: "author/committer 메타 + audit log 대조" 로 Hermes-originated 를 *식별*할 수 있다.
- 결함: author/committer = 낮은 신뢰 신호 (합의 §2.4 신뢰 등급 표). audit log cross-reference 도 Hermes 가 audit log 에 접근·위조 가능하면 무력 (→ B-5 audit tamper-resistance 와 연동).

### 1.3 line 784 — §5.5.1 SPOF Accepted Risk

```
| 합의 보고서 commit author | 동일 사용자 | Hermes-originated commit auto-reject (§2.2 #20) 의 *기준* 자체가 단일 author 비교 |
```

- 가정: auto-reject 의 *판정 기준* = "단일 author 비교" (사용자 author 와 같으면 통과, 다르면 reject).
- 결함: 단일 author 비교 = 사용자/Hermes 가 동일 author 로 commit 하면 구분 불가. **이 줄은 결함을 *명시적으로 자인* 하고 있음** ("기준 자체가 단일 author 비교") — 즉 결함 교정 = 이 자인된 기준을 positive allow-list 로 *대체*하는 것.

### 1.4 연동 touch-point 전수 (교정 시 연쇄 확인 대상 — 검토만)

| Line | §위치 | 현 본문 (metadata/author 의존 부분) | 교정 연동 여부 |
|----|----|----|----|
| **448** | §3.1.2 감지 channel | "git commit author/committer + audit log cross-reference" | ⭐ **1차 교정 대상** |
| **784** | §5.5.1 SPOF | "기준 자체가 단일 author 비교" | ⭐ **1차 교정 대상** |
| 230 | §5.2.4 #11 Evidence Ledger | "auto-reject + signed commit (PR-2 ADR-012 후보)" | △ 이미 signed commit 언급 — positive allow-list 와 정합 방향 (교정 시 강화 확인) |
| 360 | §2.6.4 #7 | "auto-reject + 합의 보고서 author = user 강제" | △ "author = user 강제" = single-author 가정 잔존 — 교정 연동 확인 |
| 648 | §4.5 합의 결과 commit author | "❌ auto-reject — git pre-commit hook + audit log" | △ 차단 지점(pre-commit hook)·식별 근거 연동 — B-2(runtime=sensor) 와 정합 확인 |
| 805 | §5.5.3 multi-host trigger (1) | "사용자별 GPG signed commit 강제" | ○ multi-host 전환 시 이미 signed commit 강제 — positive allow-list 의 multi-host 판 (교정 방향 선례) |
| 1122 | §2.6 RESOLVED 표 #7 | "author = user 강제" | △ 360 과 동일 가정 잔존 — 연동 확인 |

> ⚠️ 위 표 = *교정 시 연쇄 확인 대상 enumeration* (검토 대상 정비) — *실 편집 0건* (§0.3). 어느 줄을 *어떻게* 고칠지 *결정* = 별도 단계 (풀 3+1 + 사용자 명시).

---

## 2. 교정 3축이 결함을 *교정 가능한지* 검토

> 사용자 명시 검토 영역. 본 §2 = 교정 *가능성 권고* — *발효* 아님 (§0.4).

### 2.1 축 A — positive allow-list (Group I 합의 B-1)

| 항목 | 내용 |
|----|----|
| 결함 대체 가정 | line 448 "author/committer 식별" + line 784 "단일 author 비교" → **"사람 전용 hardware-backed key 서명을 가진 commit *만* T3 영역 통과 허용"** (negative 식별 → positive 허용 목록) |
| 교정 논리 | "Hermes 인가?" 를 *판별* 하지 않고, "사람의 신뢰 키 서명이 *있는가?*" 만 검사 → metadata spoof 무관 (없으면 미통과, default-deny) |
| line 448 교정 방향 | "author/committer 비교" → "허용 키 allow-list 검증 (author 메타 = 참고 신호 한정)" |
| line 784 교정 방향 | "기준 자체가 단일 author 비교" → "기준 = 사람 전용 서명 키 allow-list (author 비교 아님)" + SPOF 자인은 *credential 격리 전제* 로 재기술 |
| **교정 가능 여부** | ✅ **교정 가능 (권고)** — allow-list 는 metadata 의존을 *제거*하고 default-deny 로 frame 전환. 단 §2.2/§2.4 전제 충족 시 |

### 2.2 축 B — credential boundary 실분리 (Group I 합의 B-3)

| 항목 | 내용 |
|----|----|
| 결함 대체 가정 | positive allow-list 가 성립하려면 **사람 signing key·token·SSH/GPG agent 가 Hermes 환경에서 실제로 격리** 되어야 함 (동일 credential 공유 시 allow-list 도 무력 — Hermes 가 사람 키로 서명 가능) |
| 교정 논리 | line 784 SPOF 의 핵심 위험("사용자 = Hermes container 양쪽 제어")을 *credential 격리* 로 완화 — Hermes 컨테이너에 사람 키 미주입 |
| line 784 교정 방향 | "단일 author 비교 = SPOF" → "credential boundary 실분리가 *전제* — 미분리 시 FN 위험으로 allow-list 불성립 (B-3)" 으로 재기술 |
| **교정 가능 여부** | ✅ **교정 가능 (권고) — 단 B-3 의 *전제* 성격** : credential boundary 는 line 448/784 의 *대체 기준*이라기보다 allow-list 가 작동하기 위한 *선결 조건*. 교정 본문은 이 의존 관계를 명시해야 함 |

### 2.3 축 C — external enforcement (Group I 합의 B-2 / B-4)

| 항목 | 내용 |
|----|----|
| 결함 대체 가정 | line 448/648 의 차단 지점("pre-commit hook + audit log" = Hermes runtime 내부)이 *유일 enforcement* 면 self-reference — Hermes 가 자기 차단책을 우회/무력화 가능 |
| 교정 논리 | **runtime = provenance sensor/audit producer 한정, 최종 reject 권한 = Hermes 밖** (GitHub ruleset / container ACL / hardware key 中 1+, B-2) + **host 밖 layer 최소 1개 실 anchor 의무** (B-4) |
| line 448/648 교정 방향 | "Hermes-originated commit detection (every commit)" + "git pre-commit hook" → "runtime sensor 가 *신호 생성*, 최종 차단 = host 밖 (ruleset/ACL/key)" 로 책무 재배치 |
| **교정 가능 여부** | ✅ **교정 가능 (권고)** — external enforcement 는 line 448 의 "every commit detection" 을 *sensor 신호*로 격하하고 enforcement 를 Hermes 밖으로 이전 → 핵심 제약 #1(Hermes ≠ root of trust) *강화* 방향 |

### 2.4 종합 — 교정 가능성 권고

**세 축은 line 448/784 결함을 *교정 가능* 하며, 셋이 결합해야 완성된다 (single layer 불충분):**

```
positive allow-list (B-1)  ─ "무엇을 허용하는가" (default-deny + 사람 키 서명)
        ⊕
credential boundary (B-3)  ─ "allow-list 가 작동하기 위한 전제" (Hermes 환경 키 격리)
        ⊕
external enforcement (B-2/B-4) ─ "누가 최종 차단하는가" (Hermes 밖 anchor)
        =
metadata-기반 single-author detection 결함의 구조적 교정
```

- positive allow-list 단독 = credential 미격리 시 무력 (B-3 전제 필요)
- credential boundary 단독 = 차단 주체가 Hermes 면 self-reference 잔존 (B-2/B-4 필요)
- external enforcement 단독 = 무엇을 허용할지 기준 부재 (B-1 필요)

> **교정 가능성 결론 (권고)**: line 448/784 결함은 **3축 결합으로 교정 가능** 하다는 것이 본 brief 의 검토 권고다. 단 (i) 교정 *본문 문구* 결정, (ii) 키 종류/차단 지점 *수단 고정*, (iii) 실 구현은 모두 별도 단계 (§5 형태 + §8 다음 단계). 본 §2 = 가능성 *권고* — *발효* 아님 (§0.4).

---

## 3. Group I 합의 BLOCKING ↔ 교정 3축 정합 확인

| Group I BLOCKING | 본 교정 brief 축 | 정합 |
|----|----|----|
| **B-1** positive allow-list + 신뢰 등급 분리 | 축 A | ✅ line 448/784 의 author 비교를 allow-list 로 대체 = B-1 직접 구현 방향 |
| **B-2** runtime=sensor·최종 reject=Hermes 밖 | 축 C | ✅ line 448 "every commit detection" → sensor / line 648 pre-commit hook → 신호 |
| **B-3** credential boundary 실분리 = 전제 | 축 B | ✅ allow-list 의 선결 조건으로 명시 |
| **B-4** host 밖 anchor 최소 1개 의무 | 축 C | ✅ external enforcement anchor |
| **B-5** R-I-CONFIG-CHANGE = T3 (audit 보존 포함) | §5 + §7 | ✅ G3 detection 메커니즘 변경 *자체* = T3 → 본문 교정 단계 권위 결정 |
| **B-6** `.git/` 직접 변조 = filesystem ACL 책무 | (범위 외) | ○ line 448/784 교정 범위 아님 — `.git/` 변조는 commit layer 사각, §2.5 #1 ACL 책무 (교정 시 *commit detection 이 책임지지 않음* 명시 확인) |

> 정합 결론: 본 brief 의 교정 3축 = Group I 합의 B-1/B-2/B-3/B-4 의 *G3 본문 반영* 에 해당. 합의가 "권고로 기록"한 것을 "본문 교정 단계 진입 전 정비"로 잇는 구조 (합의 §2.6 #3 의 "본문 반영 = 사용자 명시 별도 단계" 답습).

---

## 4. 교정 시 영향받는 G3 본문 touch-point 매트릭스 (검토 대상 — 실 편집 0건)

| # | Line | 교정 성격 | 의존 연쇄 (CLAUDE.md §7 답습) |
|----|----|----|----|
| 1 | 448 (§3.1.2) | detection channel 본문 = author 비교 → allow-list 검증 + sensor 신호 | §2.2 #20 강제 메커니즘 / §3.1.3 차단 layer 표 |
| 2 | 784 (§5.5.1) | SPOF 기준 본문 = 단일 author 비교 → 사람 키 allow-list + credential 격리 전제 | §5.5.3 multi-host trigger / ADR-012 §원칙 12 |
| 3 | 360 / 1122 (§2.6.4 #7) | "author = user 강제" → "사람 서명 키 allow-list" 정합 | §2.6 RESOLVED 정합 |
| 4 | 648 (§4.5) | 차단 지점 "pre-commit hook" → runtime sensor + Hermes 밖 reject | §4 self-reference / B-2 |
| 5 | 230 (§5.2.4 #11) | signed commit 후보 → allow-list 와 통합 강화 | ADR-012 (PR-2) |

**의존 문서 연쇄 (교정 *발효* 단계에서 확인 의무 — 본 brief 는 enumeration 만):**
- G3 `hermes-not-root-of-trust-runtime.md` §2.2 #20 / §2.5 / §2.6 / §3.1 / §4.5 / §5.5 상호 정합
- `system-identity-prequel.md` §3.3 #1/#2/#4 (filesystem read-only + git pre-commit + 권위 등급 reject)
- ADR-012 §2.12 (변조 차단 매트릭스 4항목) + §원칙 12 (single-host SPOF)
- Group I 합의 `f6c6d5a` (B-1~B-6 출처) + Group α `2026-05-14` C-2

> ⚠️ 본 §4 = touch-point *식별* (실 편집 0건, §0.3). *어느 줄을 어떤 문구로* 교정할지 = 별도 단계.

---

## 5. ⭐ 교정 *형태* 판정 영역 — G3 detection 메커니즘 변경 = T3 / 풀 3+1 의무?

> 본 §5 = 형태 판정 *근거 정비 + 권고* — *발효* 는 합의/사용자 결정 (§0.4).

### 5.1 판정 기준 (Group I 합의 B-5 + γ-2 trigger 매트릭스 답습)

| 트리거 | 발화 | 근거 |
|----|----|----|
| #2 T3 영역 변경 | ✅ **HIGH (BLOCKING)** | G3 §2.2 #20 = T3 절대 금지. detection 메커니즘 = #20 의 *판정 기준* → 변경 = T3 enforcement 설정 변경 (**B-5 R-I-CONFIG-CHANGE 직결**) |
| #5 5 핵심 제약 약화 | ✅ **HIGH** | 교정이 핵심 제약 #1(Hermes ≠ root of trust) 강화 방향이나, *변경 자체* 가 enforcement 기준 변경 → 다관점 검증 필수 |
| #7 외부 LLM cross-vendor | ⚠️ MEDIUM | Group I 합의에서 GPT-5.5 1건 이미 회수(이 결함 직접 평가). 교정 본문 단계 추가 vendor = 사용자 결정 (의무 아님 — 기 충족) |
| self-reference | ✅ HIGH | Hermes 자기 차단책의 *판정 기준* 변경 = Hermes 가 끄지 못해야 함 (B-5) → 풀 3+1 + 사용자 명시 |

### 5.2 형태 권고 (발효 아님)

**G3 line 448/784 detection 메커니즘 본문 교정 = T3 보안 enforcement 설정 변경 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 단축 *부적격*.**

근거:
1. **B-5 R-I-CONFIG-CHANGE = T3**: Group I 합의가 "Group I enforcement *설정 자체* 변경 = T3, Hermes 단독 변경 불가, 사용자 명시 + 풀 3+1" 로 이미 분류. detection 메커니즘 = 그 설정의 핵심 → 동일 분류 (합의 §2.6 #3 명시).
2. **새 권위 결정 발생**: metadata 비교 → positive allow-list 는 *새 식별·차단 기준 결정* (단순 evidence 흡수 아님) → Reviewer-only 부적격 (Group I 본 합의 §5.2 답습).
3. **단, Group I 본 합의가 이미 5 보강점 + B-1~B-6 을 도출** 했으므로, 교정 본문 합의는 *그 권고를 본문에 반영하는 결정* 에 집중 (식별 방법 frame 은 합의 완료, 본문 문구·범위 결정이 잔여).

### 5.3 미니 합의 vs 풀 3+1 경계 (검토 영역)

본 brief 가 검토 영역으로 정비하는 미해결 질문: **Group I 합의가 이미 교정 *방향*(B-1/B-2/B-3/B-4)을 만장일치로 확정했는데, 본문 교정 단계가 *풀 3+1 전체* 인가, 아니면 "확정된 방향의 본문 반영 + 정합 검증"에 한정한 *축소 합의* 인가?**

| 후보 | 적격 조건 | 평가 (권고 — 발효 아님) |
|----|----|----|
| 풀 3+1 (재실행) | 새 권위 결정 + T3 + self-reference | ⚠️ B-5 형식상 적격이나, 식별 frame 은 Group I 합의에서 *이미* 만장일치 확정 → 전면 재실행은 중복 소지 |
| 본문 반영 한정 합의 (방향 고정 + 문구·정합 검토) | Group I 합의 권고를 본문에 *반영*, 새 식별 frame 결정 0건 | ✅ **권고 후보** — B-1~B-4 = 기 확정 / 본 단계 = 본문 문구 + touch-point 정합 + 수단 고정 여부 |
| Reviewer-only | 새 권위 결정 0건 + evidence 흡수 한정 | ❌ 부적격 — 본문 문구 = 새 결정 요소 잔존 (단일 author → allow-list 는 §2.2 #20 판정 기준 변경) |

> **§5 형태 권고**: 교정 본문 단계 = **최소 "본문 반영 한정 합의" (Group I B-1~B-4 방향 고정 + 본문 문구·touch-point 정합 + 수단 고정 여부 판정)** 권고. 풀 3+1 전면 재실행 vs 축소 형태의 *최종 결정* = 사용자 명시 (§0.4). 어느 쪽이든 Reviewer-only 단독은 부적격 (B-5 T3).

---

## 6. ADR-011 means/ends 정합 검토

Group I 합의 framing N1(§2.3)은 외부 제안 명칭 "Human-authorized T3 change enforcement with Hermes credential isolation" 이 *수단(credential isolation)을 명칭에 고정* → ADR-011 §2.1 means/ends 위반 소지로 전면 재정의를 보류했다. **본 교정 brief 도 동일 함정을 피해야 한다:**

| 함정 | 회피 방향 |
|----|----|
| "positive allow-list = hardware-backed GPG key" 처럼 *수단을 본문에 못박기* | 교정 본문 = **목적(ends)** 명시 한정 — "식별 = metadata 판별 아닌 *사람 권위 신호 positive 검증*" + "최종 차단 = Hermes 밖". 키 종류·서명 방식 = *수단* → 본문 고정 보류, 별도 구현 단계 |
| line 448 의 구체 채널을 다른 구체 수단으로 *교체* | "author 비교" 를 "GPG 서명 강제" 로 바꾸면 또 다른 수단 고정 — 대신 "신뢰 등급 분리 + allow-list 기준 (수단은 구현 단계)" 로 *원칙* 기술 |

> **정합 결론 (권고)**: 교정 본문은 **목적/원칙 수준** (metadata≠root signal / positive 검증 / external enforcement / credential 격리 전제) 으로 기술하고, **구체 수단(키 종류·차단 지점)은 본문 고정하지 않는다** = ADR-011 means/ends + brief §0.3 "수단 결정 고정 0건" 정합. 이는 Group I 합의 N1 처리와 동일 구조.

---

## 7. 미해소 쟁점 + Rollback Trigger 연결

| # | 미해소 쟁점 | 분리 사유 |
|----|----|----|
| 1 | 교정 본문 *문구* 확정 | 본 brief = 가능성·범위·형태 검토만. 실 문구 = 교정 합의 단계 |
| 2 | positive allow-list 수단 고정 (키 종류·서명 방식) | 수단 결정 = 구현 단계 (Backlog #6) + ADR-011 means/ends (§6) |
| 3 | credential boundary 실분리 구현 (Hermes 환경 키 격리) | B-3 전제 = Implementation/Runtime PASS 영역 |
| 4 | external enforcement anchor 실 구성 (ruleset/ACL/key) | B-2/B-4 = git hook/ruleset 구현 단계 (본 brief 금지) |
| 5 | line 360/1122 "author = user 강제" 정합 교정 여부 | 교정 합의 단계 touch-point 결정 |
| 6 | observe mode 기간 / threshold | threshold 고정 영역 (별도 단계) |

**Rollback Trigger 연결 (Group I 합의 §8 답습):**
- **R-I-CONFIG-CHANGE (B-5)**: G3 detection 메커니즘 본문 교정 = enforcement 설정 변경 = T3 → Hermes 단독 변경 불가, 사용자 명시 + 풀 3+1(또는 §5.3 축소 합의). **본 결함 교정 자체가 이 trigger 의 적용 사례.**
- **R-I-IMPL-BOUNDARY**: 교정 본문의 실 hook/ruleset/credential 격리 구현 = Implementation PASS + Backlog #6 + 별도 풀 3+1.

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|----|----|----|
| **(A)** | 본 brief 그대로 승인 → **G3 line 448/784 교정 합의 진입** (§5.3 권고 = 본문 반영 한정 합의 또는 풀 3+1, 사용자 형태 결정) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 brief 승인 → commit (`docs/phase0/g3-line448-784-metadata-detection-defect-correction-brief.md`) *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → Group I 후속 다른 단위 (G1 Hermes PR/approval auto-reject 신규 단위 / 2차 vendor 입력) 우선 | 별도 brief |
| (E) | 본 brief 보류 → GP-5 C-2 완전 해소 (facade real P1 v2, Backlog #4) 우선 | Backlog #4 |
| (F) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 교정 합의 / commit / push = 사용자 명시 승인 후 별도 단계. 교정 본문 = **T3 → R-I-CONFIG-CHANGE → 풀 3+1 의무(또는 §5.3 축소 합의), Reviewer-only 부적격** (§5 권고 — 발효는 합의/사용자 결정).

---

## 9. 한 단락 요약

Group I 풀 3+1 합의(`f6c6d5a`)가 **만장일치로 기록**한 G3 본문 결함 — `hermes-not-root-of-trust-runtime.md` **line 448**(§3.1.2 "Hermes-originated commit detection = git commit author/committer + audit log cross-reference") + **line 784**(§5.5.1 "auto-reject §2.2 #20 의 *기준* 자체가 단일 author 비교") 가 commit author/committer **metadata-기반 single-author detection** 에 기대고 있으며, 이는 외부(GPT-5.5)·세 Agent 가 "spoof 가능 — 인증 신호 아님" 으로 판정한 negative detection 방식 — 을 **positive allow-list / credential boundary / external enforcement 3축으로 교정 *가능한지* 검토** 하는 brief. 검토 권고: 결함은 **3축 결합으로 교정 가능** — (A) positive allow-list(B-1, "사람 권위 신호 positive 검증 + default-deny", author 메타 = 참고 신호 한정)가 line 448/784 의 author 비교를 *대체*, (B) credential boundary 실분리(B-3)가 allow-list 의 *선결 전제* (미격리 시 FN > FP 로 불성립), (C) external enforcement(B-2/B-4, "runtime = sensor / 최종 reject = Hermes 밖 anchor 최소 1개")가 line 448 의 "every commit detection" 을 sensor 신호로 격하하고 차단을 Hermes 밖으로 이전(핵심 제약 #1 Hermes ≠ root of trust *강화*) — single layer 단독은 모두 불충분. 교정 시 연동 touch-point = line 230/360/648/805/1122(검토만, 실 편집 0건). 교정 *형태* 권고: G3 detection 메커니즘 본문 변경 = **B-5 R-I-CONFIG-CHANGE = T3 enforcement 설정 변경 → 풀 3+1 의무(또는 §5.3 "본문 반영 한정 합의"), Reviewer-only 단축 부적격** — 단 식별 frame 은 Group I 합의에서 이미 만장일치 확정됐으므로 본 단계는 본문 문구·touch-point 정합·수단 고정 여부에 집중. ADR-011 means/ends 정합: 교정 본문은 **목적/원칙 수준**(metadata≠root signal / positive 검증 / external enforcement / credential 격리 전제)으로 기술하고 **구체 수단(키 종류·차단 지점)은 본문 고정하지 않음** (Group I framing N1 과 동일 구조). 본 brief 는 결론을 *선취하지 않으며* — 교정 가능성·범위·형태 *결정* 과 본문 문구·수단 고정·실 구현(hook/ruleset/CI/credential 격리)은 모두 사용자 명시 + 별도 단계(교정 합의 + Backlog #6) — **G3 본문 수정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 / ADR·합의 본문 자동 갱신 / commit / push = 모두 0건** 이다.

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| `3plus1-consensus-2026-05-20-group-i-hermes-originated-commit-autoreject.md` §2.4 (B-1~B-6) | 교정 3축 권위 근거 |
| 동 §2.6 (G3 결함 처리 양립 논리) | 결함 기록 vs 본문 교정 분리 + 본문 교정 = 별도 단계 (T3) |
| 동 §4 #1 ("G3 line 448/784 본문 교정 시점") | 본 brief = 그 별도 단계 진입 전 정비 |
| 동 §2.4 신뢰 등급 표 + C3/C4/C10 | metadata = 낮은 신뢰 / positive allow-list / credential 전제 |
| `hermes-not-root-of-trust-runtime.md` line 448 / 784 / 230 / 360 / 648 / 805 / 1122 | 결함 1차 + 연동 touch-point |
| ADR-011 §2.1 (means/ends 분리) | §6 정합 — 수단 명칭 고정 함정 회피 |
| Group I brief `group-i-...-full-3plus1-brief.md` §8 (R-I-CONFIG-CHANGE / R-I-IMPL-BOUNDARY) | Rollback Trigger 연결 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 수정** (line 448/784 detection 메커니즘 교정 / §2.2 #20·§2.5·§2.6·§3.1·§4.5·§5.5 본문 변경) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 (positive allow-list 키 종류·서명 방식·차단 지점 최종 결정) / threshold 고정 (observe mode 기간) / credential boundary 실분리 구현 / external enforcement anchor 실 구성 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / 교정 형태·범위 *판정 발효* (권고 한정 — 발효는 합의/사용자 결정) / Backlog #4·#6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
