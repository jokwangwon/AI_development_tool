# G3 본문 교정 단계 진입 brief (DRAFT v1)

> **본 brief = G3 (`hermes-not-root-of-trust-runtime.md`) 본문 교정 단계 *진입 정비* 한정 (R-I-CONFIG-CHANGE = T3).** 본 brief 의 어떤 §도 그 자체로 G3 본문 실제 수정 / 채널명 *결정* / 수단 *고정* / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 을 발생시키지 않는다. 본 brief = **진입 적격성 + 결정 scope + grep 재검증 절차 + PC 충족 의무 정비** — 실 변경 0건. staged cycle: **진입 brief → 승인 → 본문 반영 한정 합의 → 실 G3 본문 수정 + commit → push** (각 단계 사용자 명시 분리, 자동 다음 단계 진입 금지).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v1** (본문 교정 단계 *진입 정비* — 본문 미수정, 합의 미진입)
**진입 단위**: G3 결함 교정 후속 #2 (`92cc9f3` 합의 §7 #1 "G3 본문 교정 *문구* 확정 + 실 수정" — 본 brief = 그 단계 진입 정비)
**선행 발효 답습**: `e8e47de` patch brief v2 (문구 교정안 후보, PC-1~PC-7 반영) + `92cc9f3` patch brief 검증 풀 3+1 합의 (APPROVE WITH CONDITIONS, PC-1~PC-7) + `141bbc9` G3 결함 교정 합의 (CN-1~CN-10) + Group I `f6c6d5a` (B-1~B-6) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **patch brief v2 §3 (문구 교정안 후보) + §1.4 (동적 종료 조건) + §4 (채널명 삼안) + `92cc9f3` 합의 BLOCKING PC-1~PC-4 + 권고 PC-5~PC-7 + §5 결정/설계/구현 경계** + G3 원문 grep 전수 결과 (§4)
**합의 권위 한계**: 본 brief = 진입 *정비* DRAFT — 진입 적격성·결정 scope·grep 절차·PC 충족 의무를 *정비*할 뿐, 4 결정 항목(문구·범위·author 어휘·채널명)의 *결정* 과 실 G3 본문 수정은 본문 반영 한정 합의(T3, Reviewer-only 부적격) + 사용자 명시 의 권한이다.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "G3 본문 교정 단계 진입 brief 작성해줘"

본 brief = 위 명령 답습 — **본문 교정 단계 진입 적격성 점검 + 4 결정 항목 scope 명문 + §1.4 grep 전수 재검증 절차 정의(+현 시점 enumeration) + PC-1~PC-4 발효 의무 정착 + 합의 형태/Exit 기준 정비** + **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 + 선행 발효 답습 (patch brief v2 + `92cc9f3` 합의) (§1)
2. 진입 적격성 (Entry Criteria) 점검 — prerequisites 충족 여부 (§2)
3. 본문 교정 단계가 *결정*할 4 항목(문구·범위·author 어휘·채널명) scope 명문 (§3)
4. ⭐ §1.4 grep 전수 재검증 절차 정의 + **현 시점 enumeration** (발효 단계 재검증 대상 매트릭스) (§4)
5. PC-1~PC-4 BLOCKING 발효 의무 + PC-5~PC-7 권고 처리 정착 (§5)
6. 합의 형태(본문 반영 한정 합의, T3, Reviewer-only 부적격) + Exit Criteria (§6)
7. means/ends 정합 + Rollback Trigger (§7)
8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건) (§8)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경 — 본 brief = 진입 정비, 실 편집은 합의 후 별도 단계)
- ❌ **4 결정 항목 *결정*** (최종 문구 확정 / 범위 종료 / author 어휘 / 채널명 N1·N2'·제3안 선택 — 본문 반영 한정 합의 권한)
- ❌ **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step)
- ❌ **GitHub ruleset / branch protection 변경** / **CI workflow 변경** (actual run / workflow_dispatch / paths 필터)
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)**
- ❌ 수단 결정 고정 (positive allow-list 키 종류·서명 방식·차단 지점·sink 매체 — CN-6)
- ❌ threshold 고정 (observe mode 기간 등 — CN-9)
- ❌ MVP-1 exit 발효 / Phase α defer-lockdown 변경
- ❌ ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 외부 LLM 응답 강제 채택 / 외부 LLM 추가 자동 호출
- ❌ tmux 멀티 에이전트 도입 결정·구현 (별도 하네스 brief)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 본 brief 의 권위 한계

본 brief 는 결론을 *선취하지 않는다*. 진입 적격성 판정(§2)·결정 scope(§3)·grep 절차(§4)·PC 충족 의무(§5)·합의 형태(§6)는 *정비/권고*만 발행하며, 4 결정 항목의 *결정* 과 실 G3 본문 수정 *발효* 는 본문 반영 한정 합의(R-I-CONFIG-CHANGE = T3, Reviewer-only 부적격) + 사용자 명시 의 권한이다.

---

## 1. 진입 맥락 + 선행 발효 답습

### 1.1 선행 체인

```
Group I 합의 (f6c6d5a) ─ G3 결함 *발견·기록* (line 448/784 = metadata single-author detection) + B-1~B-6
        ↓
G3 결함 교정 합의 (141bbc9) ─ 교정 *방향(4축)·조건(CN-1~CN-10)·범위·형태* 확정 (APPROVE WITH CONDITIONS)
        ↓
patch brief v2 (e8e47de) ─ touch-point별 *문구 교정안 후보* (10 touch-point + 동적 종료 조건 + 채널명 삼안)
        ↓
patch brief 검증 합의 (92cc9f3) ─ 문구안 *방향* 승인 + BLOCKING PC-1~PC-4 + 권고 PC-5~PC-7
        ↓
⭐ 본 brief ─ 본문 교정 단계 *진입 정비* (실 변경 0건)
        ↓ (승인)
본문 반영 한정 합의 ─ 4 결정 항목 *결정* + PC 충족 확인 + §1.4 grep 0 (T3, Reviewer-only 부적격)
        ↓ (승인)
실 G3 본문 수정 + commit ─ R-I-CONFIG-CHANGE *발효*
        ↓
push
```

### 1.2 결함 요지 (재확인 — 재논쟁 아님)

frame 4축은 `f6c6d5a`+`141bbc9` 만장일치 확정. **본 brief 는 frame 을 재논쟁하지 않는다.** 결함 = "식별 frame 이 권한 경계가 아닌 위조 가능 metadata(commit author/committer single-author 비교)에 묶임 → 1인 single-host 에서 FN > FP 비대칭의 위험한 쪽 방치" (`141bbc9` §0.2). 교정 방향:

```
positive allow-list ⊕ credential boundary(선결 전제) ⊕ external enforcement(runtime=sensor·reject=Hermes 밖) ⊕ audit sink integrity
```

---

## 2. 진입 적격성 (Entry Criteria)

| # | 진입 조건 | 충족 | 근거 |
|----|----|----|----|
| E-1 | 교정 *방향(4축)* 만장일치 확정 | ✅ | `f6c6d5a` + `141bbc9` |
| E-2 | 교정 *조건(CN-1~CN-10)* 정의 | ✅ | `141bbc9` §2.2/§2.3 |
| E-3 | touch-point별 *문구 교정안 후보* 정비 | ✅ | patch brief v2 §3 (10 touch-point) |
| E-4 | 문구안 검증 합의 + BLOCKING 식별 | ✅ | `92cc9f3` PC-1~PC-4 (BLOCKING) + PC-5~PC-7 (권고) |
| E-5 | 범위 종료 조건 정의 (정적→동적) | ✅ | patch brief v2 §1.4 (grep 전수 잔여 인용 0) |
| E-6 | 채널명 옵션 정비 (삼안) | ✅ | patch brief v2 §4 (N1/N2'/제3안) |
| E-7 | 합의 형태 권고 (T3 R-I-CONFIG-CHANGE, Reviewer-only 부적격) | ✅ | `141bbc9` §5 + `92cc9f3` §4 |

> **진입 적격성 결론 (권고)**: E-1~E-7 모두 충족 → **본문 교정 단계 진입 = READY (적격)**. 단 진입 *발효* = 사용자 명시. 본 brief = 적격성 *정비* 한정, 진입 *결정* 아님.

---

## 3. 본문 교정 단계가 *결정*할 4 항목 (scope 명문 — `92cc9f3` §5 답습)

> 본 §3 = 결정 *대상 정비* 한정. 각 항목의 *결정* = 본문 반영 한정 합의 권한. frame 4축·CN-1~CN-10·PC-1~PC-7 = 입력 제약 (재논쟁 아님).

| 결정 항목 | 결정 내용 | 입력 (후보/제약) | BLOCKING |
|----|----|----|----|
| **① 최종 문구** | 각 touch-point 의 *최종 본문 문구* 확정 | patch brief v2 §3 교정안 후보 (PC-2/PC-3 반영판) | PC-2 (전파 비대칭) / PC-3 (보장 속성 ends) |
| **② 범위 종료** | §1.4 grep 전수 잔여 'detection'/'auto-reject'/'author 비교' 인용 = 1차 교정 정합 or 명시 분류 (잔여 0) 확인 | §4 현 시점 enumeration (발효 단계 재 grep) | PC-1 (568·328 + 동적 종료 조건) |
| **③ author 어휘** | author/committer 메타 = "판정 입력 아님·audit 사후 대조 전용" 비대칭 최종 어휘 | patch brief v2 §3.1/§3.5/§3.6 (CN-8) | PC-4 (360/1122 negative 명제) |
| **④ 채널명** | N1(detection 유지) / N2'(provenance sensor) / 제3안(provenance check) 中 *선택* + (재명명 시) cascade 갱신 | patch brief v2 §4 삼안 + §4 cascade(328/448/568) | (PC-1 cascade 완결 후 결정) |

> ⚠️ 4 항목 *외* 의 결정(수단 고정 CN-6 / threshold CN-9 / 구현)은 본 단계 scope *밖* (Backlog #6 + 별도 단계). silent scope expansion 차단.

---

## 4. ⭐ §1.4 grep 전수 재검증 절차 + 현 시점 enumeration (발효 단계 재검증 대상)

> `92cc9f3` PC-1 핵심: 범위를 "정적 열거" 아닌 **"grep 전수 잔여 인용 0 검증" 동적 종료 조건**으로. 본 §4 = (a) 절차 정의 + (b) 현 시점 enumeration(2026-05-21, 발효 단계 *재 grep* 대상). **본 enumeration 은 닫힌 목록 아님 — 발효 단계에서 재 grep 후 분류·잔여 0 도달 의무.**

### 4.1 절차 정의

```
본문 교정 발효 단계에서:
  1. G3 전체 grep: "detection"|"provenance" / "auto-reject"|"자동 reject" / "author"|"committer"|"single-author"
  2. 각 hit 를 분류:
     (i) 1차 교정    — frame(positive allow-list / sensor / 외부 reject / author 배제)으로 교정
     (ii) 정합 확인   — "auto-reject" 행위명 유지 시 영향 0 (frame 모순 없음 확인) / positive 선례
     (iii) 범위 밖   — commit 식별과 무관한 다른 의미 (오탐)
  3. 채널명 재명명(N2'/제3안) 선택 시: "detection"|"provenance" channel literal 전부 동기 갱신
  4. 잔여 미분류 hit = 0 도달 시 종료 (미충족 = 본문 교정 미완료)
```

### 4.2 현 시점 enumeration (2026-05-21 grep 결과 — 발효 단계 재검증 대상)

**A. "detection"/"provenance" channel literal (채널명 재명명 시 *필수 갱신*):**

| Line | §위치 | 현 본문 | 분류 |
|----|----|----|----|
| **448** | §3.1.2 | "**Hermes-originated commit detection** \| author/committer + audit cross-reference" | (i) 1차 — 채널명 본체 |
| **568** | §3.4 매트릭스 | "CI nightly diff + **Hermes-originated detection** + ... \| ... git pre-commit ..." | (i) 1차 — PC-1 |
| **328** | §2.6.3 (b) | "= **§3.2 Hermes-originated commit detection** + pre-commit hook" | (i) 1차 — PC-1 + "§3.2"→"§3.1.2" stale ref 정정 |

> ✅ grep 확인: line 91("ADR/SDD 모순 detection")·line 569("upstream silent breakage")는 commit 식별과 무관 = (iii) 범위 밖.

**B. 1차 교정 — Hermes-originated commit 차단 frame (auto-reject 行 中 교정 대상):**

| Line | §위치 | 분류 |
|----|----|----|
| 448 / 784 / 457 / 648 | §3.1.2 / §5.5.1 / §3.1.3 / §4.5 | (i) 1차 (patch brief v2 §3.1~§3.4) |
| 360 / 1122 | §2.6.4 #7 / §11.4.1 #7 | (i) 가정 잔존 (P1, patch brief v2 §3.5/§3.6) |

**C. "auto-reject" 행위명 참조 (발효 단계 (ii) 정합 확인 — "auto-reject 어휘 유지 시 영향 0"이 frame 과 모순 없는지 검증):**

| Line | §위치 | 비고 |
|----|----|----|
| 9 | 변조 차단 매트릭스 4항목 (§2.2 #20 인용) | 정합 |
| 221 / 228 / 229 | §2.5 #2 / #9 / #10 | PC-5 인접 — 정합 |
| 269 / 283 | §2.6 TM-2 / 4 게이트 PASS | 정합 |
| 327 / 341 | §2.6.3 (b) / 합의 보고서 수정 | 정합 (328 인접) |
| 354 / 1116 | §2.6.4 #1 / §11.4.1 #1 | PC-5 — 360/1122 평행 frame |
| 889 | §6.4 "git pre-commit hook on Hermes-originated commit" | 정합 (차단 지점 frame — CN-3 모순 여부 확인) |
| 1166 | §implementation 영역 ("자동 검출 hook") | Implementation 영역 (Backlog #6) |

> ⭐ **발효 단계 검토 항목**: "Hermes-originated commit **auto-reject**" 行위명 = "Hermes commit *이 reject 되는 대상*"(Hermes 가 reject 주체 아님)으로 읽혀 CN-3(reject=Hermes 밖)과 양립. 발효 단계는 이 독해가 C 群 전반에 일관됨을 확인 (전면 reframe vs 행위명 유지 = 합의 결정, `92cc9f3` 권고 = 유지 + 정합 확인).

**D. author/committer 참조 (발효 단계 정합 확인):**

| Line | 현 본문 | 분류 |
|----|----|----|
| 360 / 648 / 784 / 1122 | (B 群과 동일) | (i) 1차/가정 잔존 |
| 751 | "사용자 commit author 또는 명시 결정" | (ii) positive 방향 — 정합 |
| 783 | "단일 사용자 (`jokwangwon` git author)" | (ii) SPOF 표 single-host *사실* 기술 — credential boundary 맥락 정합 (교정 대상 아님) |
| 805 | "사용자별 GPG signed commit 강제" (multi-host) | (ii) 정합 참조만 (G5, patch brief v2 §3.8) |

> 본 §4.2 = **2026-05-21 시점 grep 결과**. 발효 단계는 *재 grep* 으로 (분류 변동·신규 hit) 재확인 후 잔여 0 도달 (PC-1 동적 종료 조건). 본 enumeration 의 (ii)/(iii) 분류도 발효 단계 *재확인* 대상.

---

## 5. PC-1~PC-4 BLOCKING 발효 의무 + PC-5~PC-7 권고 처리

> `92cc9f3` 합의: PC-1~PC-4 = 본문 교정 *발효* 단계 BLOCKING (충족 의무). patch brief v2 가 이미 *문구 후보* 에 반영했으나, 발효 단계는 *최종 문구* 가 PC 를 충족하는지 재확인 의무.

| PC | 발효 단계 충족 확인 항목 | patch brief v2 반영 위치 |
|----|----|----|
| **PC-1** | line 568·328 1차 교정 포함 + §4 grep 전수 잔여 인용 0 도달 | §1.3 / §1.4 / §3.9 / §3.10 |
| **PC-2** | CN-4(실 anchor 명목 금지)·CN-7(audit sink 별개)·CN-8(author 배제) 가 448·648·360·1122 *모두* 에 전파됨 | §3.1 / §3.4 / §3.5 / §3.6 |
| **PC-3** | enforcement 보장 속성(ends)="push/merge 전 차단 보장" 1구 명문 + means(§6 후보)와 분리 | §3.1 / §3.2 / §3.4 / §3.9 |
| **PC-4** | line 360/1122 author 판정 *배제* negative 명제 부가 (표현 제거만 아님) | §3.5 / §3.6 |
| 권고 PC-5 | line 354/1116/221 enumeration 정합 확인 (§4 C 群) | §5 |
| 권고 PC-6 | line 448 거대 셀 → 요약 + 하단 주석 분리 (형식 = 발효 단계 선택) | §3.1 |
| 권고 PC-7 | §5.5.2 수용사유 정합 / observe mode 도입처 / §6 환경종속 4행 일관 | §5 / §6 |

> **PC 충족 = 발효 BLOCKING**: 최종 문구가 PC-1~PC-4 中 1+ 미충족 시 본문 교정 *미발효* (합의 BLOCKING). PC-5~PC-7 = 권고 (미충족 시 사유 명시).

---

## 6. 합의 형태 + Exit Criteria

### 6.1 합의 형태 (재논쟁 아님 — `141bbc9` §5 + `92cc9f3` §4 답습)

- **본문 교정 = "단순 텍스트 정정" 아님** — §2.2 #20 auto-reject *판정 기준 변경* = **T3 (R-I-CONFIG-CHANGE) → Reviewer-only 부적격.**
- **형태 = "본문 반영 한정 합의 + 4 결정 항목(문구·범위·author 어휘·채널명) scope 명문 고정"** (frame 은 `f6c6d5a`+`141bbc9` 만장일치 확정 → 풀 3+1 frame 재투표 중복 제거, B-5 T3 다관점 유지). 풀 3+1 전면 재실행 vs 축소 형태 *최종 결정* = 사용자 명시.
- **§2.5 #6 답습**: 본 교정 = G3 본문(자기 보호 대상) 변경 → T3 self-protection 절차 (사용자 명시 commit + 합의 권위 source).

### 6.2 Exit Criteria (본문 교정 단계 *완료* 조건)

| # | Exit 조건 |
|----|----|
| X-1 | 4 결정 항목 모두 *결정* (최종 문구·범위 종료·author 어휘·채널명) |
| X-2 | §4 grep 전수 재검증 → 잔여 미분류 'detection'/'auto-reject'/'author 비교' 인용 = 0 (PC-1) |
| X-3 | PC-1~PC-4 BLOCKING 모두 충족 (최종 문구 기준) |
| X-4 | 채널명 재명명 선택 시 cascade(328/448/568 + C 群 정합) 갱신 완료 |
| X-5 | 의존 문서 cross-ref 정합 (patch brief v2 §5 enumeration: §2.2 #20 / §2.5 #6 / system-identity-prequel §3.3 / ADR-012) |
| X-6 | 실 G3 본문 수정 = 합의 결정과 일치 (T3 self-protection: 사용자 명시 commit) |

---

## 7. means/ends 정합 + Rollback Trigger

- **means/ends (CN-6, ADR-011 §2.1)**: 본문 교정 = *목적/원칙* 수준 (positive 검증 / external enforcement / credential 격리 전제 / audit sink 변조 저항). 수단(키·차단 지점·격리·sink 매체)은 **후보 열거(결정 = Backlog #6)** — 본문 고정 금지. 발효 단계가 수단을 본문에 못박으면 BLOCKING 위반.
- **Rollback Trigger**:
  - **R-I-CONFIG-CHANGE (T3)**: 본문 교정 = enforcement 판정 기준 변경 = T3 → Hermes 단독 변경 불가, 사용자 명시 + 본문 반영 한정 합의. **본 단계 자체가 이 trigger 의 적용 사례.**
  - **R-I-IMPL-BOUNDARY**: 본문 교정 후 실 hook/ruleset/credential 격리/audit sink 구현 = Implementation PASS + Backlog #6 + 별도 풀 3+1 (본 단계 *밖*).

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 |
|----|----|----|
| **(A)** | 본 brief 승인 → **본문 반영 한정 합의 진입** (4 결정 항목 결정 + PC 충족 + §4 grep 0 검증, 형태 = 사용자 결정[축소 vs 풀 3+1]) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 요청 | v2 작성 |
| (C) | 본 brief 승인 → commit *까지만* (합의 보류) | 1 commit (사용자 명시 시) |
| (D) | 본 brief 보류 → 다른 backlog (tmux 도입 brief / Group I implementation boundary / G1 PR·approval auto-reject / 2차 vendor / GP-5 C-2 Backlog #4) | 별도 brief |
| (E) | 본 brief 보류 → 세션 종료 | — |

> 본 brief = **진입 brief 단계 한정** (staged cycle: 진입 brief → 승인 → 합의 → 본문 수정+commit → push). 합의 / 실 G3 본문 수정 / commit / push = 사용자 명시 승인 후 별도 단계. 본문 교정 = **T3 → R-I-CONFIG-CHANGE → Reviewer-only 부적격**.

---

## 9. 한 단락 요약

`92cc9f3` 합의(APPROVE WITH CONDITIONS)가 검증한 patch brief v2(`e8e47de`, 10 touch-point 문구 교정안 후보 + 동적 종료 조건 + 채널명 삼안)를 기반으로, **G3 본문 교정 단계 *진입* 을 정비**하는 brief — 진입 적격성(E-1~E-7 모두 충족 = READY), 본문 교정 단계가 *결정*할 **4 항목**(① 최종 문구[PC-2/PC-3] / ② 범위 종료[PC-1 grep 전수 잔여 인용 0] / ③ author 어휘[PC-4 negative 배제 명제] / ④ 채널명[N1/N2'/제3안 삼안 + cascade]) scope 명문, **§1.4 grep 전수 재검증 절차 + 2026-05-21 현 시점 enumeration**(A. "detection" channel literal = 328/448/568 [재명명 시 필수 갱신, line 91/569 무관 제외 확인] / B. 1차 교정 448/784/457/648/360/1122 / C. "auto-reject" 행위명 참조 9/221/228/229/269/283/327/341/354/889/1116/1166 = 정합 확인 [행위명 유지 = "Hermes commit 이 reject 되는 대상"으로 CN-3 양립] / D. author/committer 751/783/805 = 정합 참조), **PC-1~PC-4 발효 BLOCKING 충족 의무 + PC-5~PC-7 권고**, 합의 형태(**본문 반영 한정 합의 + 4 결정 항목 scope, T3 R-I-CONFIG-CHANGE, Reviewer-only 부적격**) + Exit Criteria(X-1~X-6) 를 정비. frame 4축은 `f6c6d5a`+`141bbc9` 만장일치 확정 = 재논쟁 아님. 본 brief 는 결론을 *선취하지 않으며* — 4 결정 항목 *결정* 과 실 G3 본문 수정·채널명 선택·수단 고정·구현은 모두 사용자 명시 + 별도 단계(본문 반영 한정 합의 + Backlog #6) — **G3 본문 실제 수정 / 4 결정 항목 결정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 / tmux 도입 / ADR·합의 본문 자동 갱신 / commit / push = 모두 0건** 이다.

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| `g3-metadata-detection-correction-patch-brief.md` v2 (`e8e47de`) §3/§1.4/§4 | 문구 교정안 후보 + 동적 종료 조건 + 채널명 삼안 (§3·§4) |
| `3plus1-consensus-2026-05-21-g3-patch-brief.md` (`92cc9f3`) PC-1~PC-7 + §4·§5 | BLOCKING/권고 발효 의무 (§5) + 합의 형태 (§6) |
| `3plus1-consensus-2026-05-20-g3-metadata-detection-defect-correction.md` (`141bbc9`) CN-1~CN-10 + §5 | 교정 방향·조건 (§1.2) + 형태 (§6) |
| `hermes-not-root-of-trust-runtime.md` grep 전수 (2026-05-21) | §4 현 시점 enumeration |
| ADR-011 §2.1 (means/ends) | §7 수단 후보 (CN-6) |
| Group I `f6c6d5a` (B-5 R-I-CONFIG-CHANGE / B-6) | §7 Rollback Trigger |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경) / **4 결정 항목 결정** (최종 문구 / 범위 종료 / author 어휘 / 채널명 N1·N2'·제3안 선택) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run / workflow_dispatch / paths 필터) / **Hermes runtime·upstream 변경** / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 (키 종류·서명 방식·차단 지점·sink 매체) / threshold 고정 (observe mode 기간) / **채널명 재명명 결정** / 문구 최종 확정 / credential boundary 실분리·external enforcement anchor·audit sink 실 구성 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·#6 자동 진입 / tmux 멀티 에이전트 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
