# G3 본문 교정 patch brief — line 448/784/457/648/360/1122/230/805 (+568/328) 문구 교정안 (DRAFT v2)

> **본 brief = `92d74be` 합의(APPROVE WITH CONDITIONS, CN-1~CN-10)에서 *방향·조건·범위* 가 확정된 G3 본문 결함 교정을, touch-point별 *문구 교정안 후보* 로 정비하는 brief 한정.** 본 brief 의 어떤 §도 G3 본문 실제 수정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 을 발생시키지 않는다. 문구 교정안 = **후보·권고** — *발효(본문 반영)* 는 별도 단계 (staged cycle: brief → 승인 → 합의 → commit → push). 본 brief = **brief 단계 한정**.

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (patch brief 검증 합의 `92cc9f3` BLOCKING PC-1~PC-4 반영 — 본문 미반영, 본문 교정 단계 미진입)
**진입 단위**: G3 metadata detection 결함 교정 합의 후속 #1 (`92d74be` 합의 §7 #1 "G3 본문 교정 *문구* 확정 + 실 수정")
**선행 발효 답습**: `92cc9f3` patch brief 검증 풀 3+1 합의 (APPROVE WITH CONDITIONS, PC-1~PC-7) + `92d74be` 결함 교정 풀 3+1 합의 (CN-1~CN-10) + `afb92de` 교정 *검토* brief + Group I `f6c6d5a` (B-1~B-6) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **`92cc9f3` 합의 PC-1~PC-7 + `92d74be` 합의 §2.1 교정 방향 + §2.2 CN-1~CN-9 + §2.3 CN-10 + §3 교정 범위 표 + §5 경계** + G3 line 448/784/457/648/360/1122/230/805/568/328 원문
**합의 권위 한계**: 본 brief = 문구 교정안 *후보* DRAFT — 본문 반영 *발효* 아님. 어느 touch-point 를 어떤 *최종 문구* 로 고칠지, 채널명 재명명 여부(CN-10, 삼안), 수단 후보 표기 형식(CN-6/D2) 의 *결정* 은 본문 교정 단계(R-I-CONFIG-CHANGE = T3, 사용자 명시) 의 권한이다.

---

## v2 변경 이력 (`92cc9f3` 합의 BLOCKING 반영)

| BLOCKING | v1 → v2 반영 위치 |
|----|----|
| **PC-1** (누락 touch-point 추가 + 동적 종료 조건) | §1.3 범위 표에 **line 568·328 추가** + 항목② 범위를 "8 touch-point 정적 열거" → **"grep 전수 잔여 'detection'/'auto-reject' 인용 0 검증" 동적 종료 조건**으로 전환 (§1.4) / §3.9(568)·§3.10(328) 신설 / §4 cascade 정정(#20 오지목 제거 + line 328 추가) |
| **PC-2** (전파 비대칭 해소) | CN-4 "실 anchor" → §3.1(448)·§3.4(648) 부가 / CN-7 audit sink 별개성 → §3.4(648) 부가 / CN-8 author 배제 → §3.5(360)·§3.6(1122) 부가 |
| **PC-3** (enforcement 보장 속성 = ends 명문) | §3.1(448)·§3.2(457)·§3.4(648)에 "차단 보장 속성(ends)" 1구 — means(§6 후보)와 분리 |
| **PC-4** (author 판정 배제 negative 명제) | §3.5(360)·§3.6(1122)에 "author/committer = 판정 입력 아님·audit 사후 대조 전용" 명시 |
| 권고 PC-5 | §5 enumeration 에 line 354/1116/221 추가 |
| 권고 PC-6 | §3.1(448) 거대 셀 → 본문 요약 + 하단 주석 분리 옵션 명시 |
| 권고 PC-7 | §6 환경종속 4행 일관화 + Backlog #6 cross-ref / §5 에 §5.5.2 정합·observe mode 도입처 확인 추가 |

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "G3 본문 교정 patch brief 를 작성해주세요. 범위는 line 448 / 784 / 457 / 648 / 360 / 1122 / 230 / 805 touch-point 를 대상으로, metadata 기반 detection frame 을 positive allow-list + credential boundary + external enforcement + audit sink integrity 중심으로 교정하는 문구안을 정리하는 것입니다. 아직 G3 본문 실제 수정, git hook 구현, GitHub ruleset 변경, CI workflow 변경, Operational Readiness PASS, Hermes PMO 격상은 하지 마세요."

본 brief = 위 명령 답습 — **touch-point별 문구 교정안 후보 정비** + **CN-1~CN-10 정합 매핑** + **채널명 재명명 옵션 정비(CN-10)** + **의존 연쇄 갱신 대상 enumeration** + **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. `92d74be` 합의 확정 사항(교정 방향 4축 + CN-1~CN-10 + 교정 범위)을 문구 교정안의 *입력 제약* 으로 정착 (§1)
2. 교정 4축(positive allow-list / credential boundary / external enforcement / audit sink integrity)을 *문구 수준 원칙* 으로 환원 (§2)
3. **10 touch-point(8 + PC-1 추가 568/328) 각각의 현 본문(verbatim) → 문구 교정안 후보 + CN/PC 매핑** (§3) — 본 brief 의 핵심
4. 채널명 재명명 옵션(CN-10) — N1(유지) vs N2'(재명명) 양안 정비 + cross-reference 의존 연쇄 (§4)
5. 교정 시 의존 문서·cross-reference 갱신 대상 enumeration (§5)
6. ADR-011 means/ends 정합(CN-6) — 수단 후보 열거 형식 정비 (§6)
7. 교정 *형태/권위* (R-I-CONFIG-CHANGE = T3, 본문 반영 한정 합의 4 결정 항목) (§7)
8. 미해소 + 다음 단계 (사용자 결정 영역 — 자동 진입 0건) (§8)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경 — **문구안 = 후보 한정, 실 편집 0건**)
- ❌ **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문)
- ❌ **GitHub ruleset / branch protection 변경** (signed commit required / required status check / bypass 정책)
- ❌ **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경)
- ❌ **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**
- ❌ Hermes runtime 변경 / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ 수단 *결정 고정* (positive allow-list 키 종류·서명 방식·차단 지점 최종 고정 — CN-6 위반)
- ❌ threshold 고정 (observe mode 기간 등 — CN-9 구체 수치)
- ❌ **채널명 재명명 *결정*** (CN-10/PC-④ = 삼안 *개방* 이지 결정 아님 — N1/N2'/제3안 최종 선택 = 본문 교정 단계)
- ❌ 문구 교정안 *최종 확정* (본 brief = 후보 한정 — 최종 문구 = 본문 교정 합의 권한)
- ❌ MVP-1 exit 발효 / Phase α defer-lockdown 변경
- ❌ ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012) / Group I·α·β·γ 합의 본문 변경
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 본 brief 의 권위 한계

본 brief 는 결론을 *선취하지 않는다*. §3 의 문구 교정안은 **후보** 이며, 본문 반영 *발효* 는 본문 교정 단계(R-I-CONFIG-CHANGE = T3)의 권한이다. `92d74be` 합의가 이미 (i) 교정 방향(4축), (ii) CN-1~CN-10 조건, (iii) 교정 범위(touch-point), (iv) 형태("본문 반영 한정 합의 + 4 결정 항목 scope 명문")를 **권고로 확정**했으므로, 본 brief 는 그 권고를 *touch-point별 실 문구로 환원* 하는 정비에 해당하며 — 합의가 남긴 4 결정 잔여(문구·범위·author 어휘·채널명)를 *후보 형태로* 제시할 뿐 *결정* 하지 않는다.

---

## 1. 합의 확정 사항 = 본 문구안의 입력 제약 (`92d74be` 답습)

본 brief 의 모든 문구 교정안은 다음 합의 확정 사항을 *위배하지 않는다*:

### 1.1 교정 방향 4축 (합의 §2.1 — 만장일치)

```
positive allow-list   ─ "무엇을 허용하는가" (default-deny + 사람 권위 신호 positive 검증, metadata spoof 무관)
        ⊕
credential boundary   ─ "allow-list 가 작동하기 위한 *선결 전제*" (사람 키·token·SSH/GPG agent 의 Hermes 환경 격리)
        ⊕
external enforcement  ─ "누가 최종 차단하는가" (runtime=sensor / 최종 reject=Hermes 밖 anchor 최소 1개 실 anchor)
        ⊕
audit sink integrity  ─ "audit log cross-reference 의 매체 격리" (외부 read-only sink, Hermes 쓰기 불가)
        =
metadata-기반 single-author detection 결함의 구조적 교정
```

### 1.2 CN-1~CN-10 조건 (합의 §2.2 + §2.3) → 문구안 적용 키

| 조건 | 문구안에서의 의미 |
|----|----|
| **CN-1** | line 448/784/360 의 "author 비교 / author = user 강제" → "default-deny + 사람 권위 신호 positive 검증" 문구로 *대체* |
| **CN-2** | line 784 SPOF 문구에 "credential boundary = allow-list 의 *선결 조건*, 미격리 시 metadata 와 동일 FN 붕괴 + 거짓 안전감 추가" *명문 1구* 삽입 |
| **CN-3** | line 448/457/648 의 "every commit detection / pre-commit hook + audit log" → "runtime = sensor·audit producer, 최종 reject = Hermes 밖" 으로 책무 재배치 문구 |
| **CN-4** | line 457 에 "host 밖 anchor 최소 1개 = 실 anchor 의무" + "detection 기준·차단 설정 변경 = R-I-CONFIG-CHANGE = T3" 문구 |
| **CN-5** | §3.1.3 차단표에 "`.git/` 직접 변조 = filesystem ACL(§2.5 #1) 책무, commit detection 범위 *밖*" *필수 1줄* 추가 |
| **CN-6** | 모든 문구안은 **목적/원칙 수준** — 키 종류·서명 방식·차단 지점은 *수단 후보 비표준 열거(결정 = Backlog #6)* 형식만 허용, 본문 고정 금지 |
| **CN-7** | line 448 "audit log cross-reference" → "외부 read-only sink (Hermes 쓰기 불가) 매체 격리" 를 credential boundary 와 *별개 요소* 로 명시 |
| **CN-8** | line 448 author/committer 메타 = "**판정 경로 제외 · audit 보조 전용**" 비대칭 (모호어 "참고 신호" 금지) |
| **CN-9** | "observe mode = enforcement 발효 아님 (observe 기간 FN 통과)" + "FN 우선 > FP (의심 시 quarantine)" 를 *방향성* 으로 본문 명시 (구체 기간 = threshold, 별도) |
| **CN-10** | 채널명 "detection" → "provenance sensor" 재명명 = **옵션 개방** (역할 어휘 = means 고정 아님). 본 brief = N1/N2' 양안 제시, *결정 보류* |

### 1.3 교정 범위 (합의 §3 + `92cc9f3` PC-1 보강)

| 구분 | Line | §위치 |
|----|----|----|
| **1차 교정** | 448 / 784 / 457 / 648 | §3.1.2 / §5.5.1 / §3.1.3 / §4.5 |
| **1차 교정 (PC-1 추가)** | **568** | §3.4 통합 매트릭스 — "detection" 직접 인용 + "git pre-commit" CN-3 위반 차단 frame |
| **1차 교정 (PC-1 추가)** | **328** | §2.6.x — "detection" 2번째 literal 인용 + "§3.2" stale cross-ref (실제는 §3.1.2) |
| **가정 잔존 교정 (P1)** | 360 / 1122 | §2.6.4 #7 / §11.4.1 #7 |
| **정합 참조만 (G5)** | 230 / 805 | §2.5 #11 / §5.5.3 (1) |

### 1.4 ⭐ 범위 종료 조건 = 동적 검증 (PC-1 — 정적 열거 폐기)

> `92cc9f3` 합의 PC-1: 교정 범위를 "8(→10) touch-point **정적 열거**" 로 못박지 *않는다*. line 457 누락→line 568·328 또 누락의 *구조적 반복* 을 막기 위해, 범위 종료 조건을 **동적 검증** 으로 정의한다.

**범위 종료 조건 (본문 교정 *발효* 단계 의무):**

```
G3 전체에서 grep:
  - "detection" (channel/메커니즘 의미, line 91 "모순 detection" 등 무관 의미 제외)
  - "auto-reject" / "자동 reject"
  - "author = user 강제" / "단일 author" / "author/committer 비교"
→ 잔여 hit 가 (i) 1차 교정 frame 으로 일관 정합되었거나
  (ii) 명시적 "정합 참조만"(230/805) / "범위 밖"(line 91) 으로 분류될 때까지
  = 종료 조건 미충족 시 본문 교정 미완료
```

- 본 brief 가 식별한 10 touch-point + §5 정합 enumeration(354/1116/221) = **현 시점 검증 결과** 이지 *닫힌 목록* 이 아니다.
- 본문 교정 단계에서 **재 grep 전수** 로 잔여 인용 0 을 *재확인* 해야 발효 적격 (harness feedforward — 가이드를 종료 조건에 못박음).
- Reviewer 가 직접 grep 으로 line 328 의 "§3.2" stale ref 까지 발견한 사실(합의 §1.5)이 정적 열거의 위험을 실증.

---

## 2. 교정 4축 → 문구 수준 원칙 환원

| 축 | 문구 수준 원칙 (본문에 들어갈 *목적* 표현) | 들어가지 *말아야* 할 것 (CN-6) |
|----|----|----|
| positive allow-list | "사람 권위 신호가 positive 하게 검증되는 commit *만* T3 영역 통과 — 그 외 default-deny" | "GPG 서명 강제" 같은 *단일 수단* 못박기 |
| credential boundary | "위 allow-list 는 사람 키·token·agent 가 Hermes 환경에서 격리됨을 *선결 전제* 로 한다 (미격리 시 붕괴)" | 격리 *방식*(미주입 vs vault vs KMS) 본문 고정 |
| external enforcement | "runtime 은 provenance *신호 생성* 만, 최종 reject 권한 = Hermes 밖 anchor (host 밖 최소 1개 실 anchor)" | "GitHub ruleset" 단일 anchor 못박기 |
| audit sink integrity | "audit log cross-reference 는 Hermes 가 쓸 수 없는 외부 read-only sink 에 보존됨을 전제로 한다" | sink *제품*(S3/append-only log 등) 본문 고정 |

> 모든 축은 *목적/원칙* 으로 문구화하고, 구체 수단은 §6 "수단 후보 열거" 블록으로 분리 (CN-6 + ADR-011 means/ends).

---

## 3. ⭐ touch-point별 문구 교정안 후보 (본 brief 핵심 — 실 편집 0건)

> 각 항목 = **현 본문 (verbatim)** → **교정안 후보** + **CN 매핑**. 교정안 = *후보* 이며 최종 문구·채택 여부 = 본문 교정 단계 결정 (§7). 표 셀 내 `[…]` = 수단 후보 열거(결정 = Backlog #6, CN-6).

### 3.1 line 448 — §3.1.2 감지 channel (1차 교정)

**현 본문 (verbatim):**
```
| **Hermes-originated commit detection** | git commit author / committer + Hermes audit log cross-reference | every commit |
```

**교정안 후보 (PC-6 권고 = 본문 셀 짧게 + 하단 주석 분리):**

*메커니즘 셀 (요약):*
```
| **Hermes-originated commit provenance**¹ | 사람 권위 신호 positive 검증 (default-deny) — author/committer 메타 = **판정 입력 아님·audit 사후 대조 전용**(CN-8) | sensor 평가 = every commit² |
```
*§3.1.2 표 하단 주석 (세부 — PC-6 분리):*
> 본 채널: runtime = **provenance sensor 신호 생성만**, 최종 reject = **Hermes 밖 anchor (host 밖 최소 1개 *실* anchor, 명목 anchor 금지)**(CN-3/CN-4). **차단 보장 속성(ends): 차단이 push/merge 전에 보장됨**(PC-3 — 보장 *속성* 은 ends, *무엇으로* 차단은 means → §6 후보). audit log cross-reference 는 **외부 read-only sink (Hermes 쓰기 불가)** 매체 격리 전제(CN-7, credential boundary 와 *별개 축*). 수단 후보 → §6 (결정 = Backlog #6, CN-6). `.git/` 직접 변조는 본 채널 범위 *밖* = filesystem ACL(§2.5) 책무(CN-5).

> ¹ 채널명 = N1/N2'/제3안 — §4 (CN-10, *결정 보류*). ² enforcement *시점* = "외부 anchor 가 push/merge 전 보장"(ends), means(§6)와 분리.

| 적용 CN/PC | 반영 |
|----|----|
| CN-1 | "author/committer 비교" → "사람 권위 신호 positive 검증 + default-deny" |
| CN-3 | "every commit" detection → sensor 신호 / 최종 reject = Hermes 밖 |
| **CN-4 (PC-2)** | "Hermes 밖 anchor" → **"host 밖 최소 1개 *실* anchor (명목 anchor 금지)"** (v1 = 457 에만 → 448 전파) |
| **PC-3** | **enforcement 보장 속성(ends) = "push/merge 전 차단 보장" 1구 명문** (means 후보 §6 과 분리 — DV2) |
| CN-7 | "audit log cross-reference" → 외부 read-only sink 매체 격리 (credential 과 별개 축) |
| CN-8 | author/committer 메타 = "판정 입력 아님·audit 사후 대조 전용" (C 권고 = "참고 신호"·"보조" 모호어 회피) |
| **PC-6** | 거대 셀 → 메커니즘 요약 + 하단 주석 분리 (457 패턴 동형) |
| CN-10 | 채널명 삼안 (§4) |

### 3.2 line 457 — §3.1.3 차단 방법 (Git layer) (1차 교정, G1 보완)

**현 본문 (verbatim):**
```
| Git | pre-commit hook on 정책 파일 — Hermes-originated commit 자동 reject | §2.2 #20 + system-identity-prequel §3.3 #2 |
```

**교정안 후보:**
```
| Git (sensor) | runtime = **provenance sensor 신호 생성**(pre-commit hook 등 = 수단 후보, §6 — *차단권 아님*). 최종 reject = **Hermes 밖 anchor 최소 1개 실 anchor**(CN-4). detection 기준·차단 설정 변경 = **R-I-CONFIG-CHANGE = T3**(Hermes token 미보유, 자기 차단책 무력화 불가) | §2.2 #20 + system-identity-prequel §3.3 #2 |
```

**+ §3.1.3 표 하단 *필수 1줄* 추가 (CN-5):**
```
> ⚠️ `.git/` 디렉터리 직접 변조는 **commit detection/provenance 범위 *밖*** 이며 filesystem ACL(§2.5 #1)의 책무다. commit layer sensor 는 `.git/` 우회를 책임지지 않는다.
```

| 적용 CN | 반영 |
|----|----|
| CN-3 | pre-commit hook = 차단권 → sensor 신호 (수단 후보로 격하) |
| CN-4 | host 밖 anchor 최소 1개 실 anchor 의무 + 설정 변경 = R-I-CONFIG-CHANGE T3 |
| CN-5 | `.git/` = filesystem ACL 책무, commit detection 범위 밖 (필수 1줄) |

### 3.3 line 784 — §5.5.1 SPOF Accepted Risk (1차 교정)

**현 본문 (verbatim):**
```
| 합의 보고서 commit author | 동일 사용자 | Hermes-originated commit auto-reject (§2.2 #20) 의 *기준* 자체가 단일 author 비교 |
```

**교정안 후보:**
```
| 합의 보고서 commit author | 동일 사용자 | auto-reject(§2.2 #20)의 *기준* = **사람 권위 신호 positive allow-list**(default-deny, author 비교 아님 — CN-1). SPOF 핵심 위험(사용자=Hermes 동일 credential 공유)은 **credential boundary 실분리가 *선결 전제***(CN-2) — 미격리 시 allow-list 도 metadata detection 과 동일 FN 으로 붕괴하며 *거짓 안전감* 을 추가 생성. observe mode = **enforcement 발효 아님**(observe 기간 FN 통과), 방향성 = **FN 우선 > FP**(의심 시 quarantine, CN-9) |
```

| 적용 CN | 반영 |
|----|----|
| CN-1 | "단일 author 비교" → "사람 권위 신호 positive allow-list" |
| CN-2 | credential boundary = allow-list 선결 조건 + 미격리 시 붕괴·거짓 안전감 명문 |
| CN-9 | observe ≠ 발효 + FN 우선 방향성 (구체 기간 = threshold, 별도) |

### 3.4 line 648 — §4.5 합의 결과 commit author (1차 교정)

**현 본문 (verbatim):**
```
| 합의 결과 commit author | ❌ Hermes-originated commit auto-reject (Hermes 관련 결정 한정) | git pre-commit hook + audit log |
```

**교정안 후보:**
```
| 합의 결과 commit author | ❌ Hermes-originated = positive allow-list 미통과 → default-deny (Hermes 관련 결정 한정) | runtime = **provenance sensor 신호**(pre-commit hook 등 = 수단 후보, §6), 최종 reject = **Hermes 밖 anchor (host 밖 최소 1개 *실* anchor, 명목 anchor 금지)**(CN-3/CN-4). **차단 보장 속성(ends): push/merge 전 보장**(PC-3). audit log = **외부 read-only sink (Hermes 쓰기 불가) — credential boundary 와 *별개 축***(CN-7) |
```

| 적용 CN/PC | 반영 |
|----|----|
| CN-1 | "auto-reject" = positive allow-list 미통과 default-deny 로 frame 정합 |
| CN-3 | "git pre-commit hook" = sensor 신호, 최종 reject = Hermes 밖 |
| **CN-4 (PC-2)** | **"host 밖 최소 1개 *실* anchor (명목 anchor 금지)"** (v1 = 457 에만 → 648 전파) |
| **PC-3** | **enforcement 보장 속성(ends) = "push/merge 전 보장" 1구 명문** |
| **CN-7 (PC-2)** | "audit log" → 외부 read-only sink + **"credential boundary 와 별개 축" 명시**(v1 = 648 에서 약함 → 별개성 강화) |

### 3.5 line 360 — §2.6.4 #7 강제 메커니즘 (가정 잔존 교정, P1)

**현 본문 (verbatim):**
```
| 7 | Hermes-originated gate approval 금지 | T3 | Hermes-originated commit auto-reject (gate 관련 본문) + 합의 보고서 author = user 강제 | 본 §2.2 #13, #20 + §4.5 + §5.5 SPOF accepted risk |
```

**교정안 후보 (강제 메커니즘 셀):**
```
Hermes-originated commit = positive allow-list 미통과 → default-deny (gate 관련 본문) + 합의 보고서 = **사람 권위 신호 positive 검증**(단일 "author = user 강제" 비교 표현 제거 — line 448/784 교정과 동기, CN-1). **author/committer = 판정 입력 아님·audit 사후 대조 전용**(CN-8/PC-4 — 표현 제거에 그치지 않고 author 판정 *배제* negative 명제 명시)
```

| 적용 CN/PC | 반영 |
|----|----|
| CN-1 / P1 | "author = user 강제" = single-author 가정 잔존 → positive allow-list frame 으로 동기 (미교정 시 본문 내부 불일치) |
| **CN-8 / PC-4** | **"author 판정 입력 아님" negative 명제 부가** — v1 은 표현 *제거* 만 → author 가 판정 보조로 재유입될 회귀 통로 잔존(합의 B-B2). negative 배제 명문으로 차단 |

### 3.6 line 1122 — §11.4.1 #7 RESOLVED 흡수 매트릭스 (가정 잔존 교정, P1 — 360 동기)

**현 본문 (verbatim):**
```
| 7 | Hermes-originated gate approval 금지 | §2.6.4 #7 | Hermes-originated commit auto-reject (gate 관련 본문) + 합의 보고서 author = user 강제 + §4.5 + §5.5 SPOF accepted risk 답습 | ✅ **RESOLVED** (2026-05-12) |
```

**교정안 후보 (흡수 방법 셀):**
```
Hermes-originated commit = positive allow-list 미통과 default-deny (gate 관련 본문) + 합의 보고서 = 사람 권위 신호 positive 검증 (§2.6.4 #7 동기 — "author = user 강제" 표현 제거 + **author/committer = 판정 입력 아님·audit 사후 대조 전용** CN-8/PC-4, CN-1) + §4.5 + §5.5 SPOF accepted risk 답습
```

| 적용 CN/PC | 반영 |
|----|----|
| P1 | 360 과 동일 표현 동기 갱신 — **dangling reference 방지** (360 만 고치고 1122 미갱신 시 RESOLVED 매트릭스가 옛 frame 참조) |
| **CN-8 / PC-4** | 360 과 동기로 author 판정 *배제* negative 명제 부가 (회귀 통로 차단) |

### 3.7 line 230 — §2.5 #11 Evidence Ledger (정합 참조만, G5)

**현 본문 (verbatim):**
```
| 11 | Evidence Ledger (...) | T3 (append-only) | hash chain 또는 git append commit + Hermes-originated 수정 자동 reject + signed commit (PR-2 ADR-012 후보) | system-identity-prequel §6.3 + 본 §5.2.4 |
```

**판정: 교정 *불요* (정합 확인만).** 이미 "signed commit (PR-2 ADR-012 후보)" = positive 서명 방향 명시 → line 448/784 교정 방향과 *충돌 없는 내부 선례* (G5).

**선택적 어휘 정합 옵션 (의무 아님):** "signed commit (PR-2 ADR-012 후보)" → "사람 서명 키 allow-list (signed commit, PR-2 ADR-012 후보)" — 1차 교정과 *어휘* 통일 강화. 단 G5 = "정합 참조만" 이므로 **기본 = 무변경**, 어휘 통일은 본문 교정 단계 선택지.

### 3.8 line 805 — §5.5.3 multi-host trigger (1) (정합 참조만, G5)

**현 본문 (verbatim):**
```
| (1) | 두 번째 사용자 (다른 git author) 가 본 저장소에 commit 시도 | 사용자별 GPG signed commit 강제 + branch protection multi-author 룰 + ADR Amendment 절차 | 즉시 |
```

**판정: 교정 *불요* (정합 확인만).** multi-host 전환 시 이미 "GPG signed commit 강제" = positive 서명 방향 선례 (G5). **결함의 정체** = "G3 가 multi-host/Evidence Ledger 에선 positive 서명을 알면서 single-host commit detection(448/784)에서만 metadata 비교에 머문 *비대칭*" — 1차 교정이 이 비대칭을 해소하면 805 와 *정합*.

**CN-6 정합 메모:** 805 가 "GPG"라는 수단을 명시한 것은 *multi-host trigger 발동 = 환경 확정 시점* 맥락이므로 means 명시 허용 범위(선례). **single-host 1차 교정 본문은 means 비고정 유지** (§6) — 805 의 GPG 명시를 single-host 본문으로 복사하지 *않는다*.

### 3.9 line 568 — §3.4 본 §3 통합 매트릭스 (1차 교정 — PC-1 추가)

**현 본문 (verbatim):**
```
| 3.1 Learning silent drift | CI nightly diff + Hermes-originated detection + R-5 canary + R-6 actual run | filesystem read-only + git pre-commit + CI FAIL + 컨테이너 정지 | ... |
```

**교정안 후보 (감지 칸 + 차단 칸):**
```
감지: CI nightly diff + Hermes-originated commit provenance¹ (sensor 신호 — author 메타 = 판정 입력 아님·audit 사후 대조 전용, CN-8) + R-5 canary + R-6 actual run
차단: filesystem read-only + (provenance sensor 신호: pre-commit 등 = 수단 후보 §6 — 차단권 아님) → 최종 reject = Hermes 밖 anchor (host 밖 최소 1개 실 anchor, CN-4) + CI FAIL + 컨테이너 정지. **차단 보장 속성(ends): merge/push 전 차단 보장**(CN-3/PC-3)
```
> ¹ 채널명 = N1/N2'/제3안 (§4). N2'/제3안 채택 시 본 매트릭스 셀의 "detection" 동기 갱신 (cascade).

| 적용 | 반영 |
|----|----|
| PC-1 | line 568 = brief v1 누락 → 1차 교정 범위 편입 (§3.1.2/§3.1.3 교정 시 §3.4 요약 매트릭스 동기 — 미동기 시 본문 내부 불일치 + N2' dangling) |
| CN-3/PC-3 | "git pre-commit" 차단권 → sensor 신호 + Hermes 밖 reject + 차단 보장 속성(ends) |
| CN-4 | "host 밖 최소 1개 실 anchor" (명목 anchor 금지) |
| CN-8 | author 메타 = 판정 입력 아님·audit 사후 대조 전용 |

### 3.10 line 328 — §2.6.3 (b) Hook/CI workflow 비활성화 차단 (1차 교정 — PC-1 추가)

**현 본문 (verbatim):**
```
- `git commit --no-verify` / `git push --no-verify` 시도 = §3.2 Hermes-originated commit detection + pre-commit hook 답습 (Group C 후속 후속 PoC 답습 — `tools/rewrite_defense_check.py` Layer 2/3/4 dangerous command catalog)
```

**교정안 후보:**
```
- `git commit --no-verify` / `git push --no-verify` 시도 = §3.1.2² Hermes-originated commit provenance¹ + (sensor 우회 시도) 답습. **pre-commit hook 이 우회(`--no-verify`)되어도 최종 reject = Hermes 밖 anchor(host 밖 실 anchor, CN-3/CN-4)가 차단을 보장** — runtime sensor 단독 의존 금지 (Group C 후속 후속 PoC 답습 — `tools/rewrite_defense_check.py` Layer 2/3/4 dangerous command catalog)
```
> ¹ 채널명 N1/N2'/제3안 (§4). ² **"§3.2" → "§3.1.2" stale cross-ref 정정** (현 본문의 "§3.2" 는 Upstream Silent Breakage, detection 채널은 §3.1.2 — 합의 §1.5 Reviewer 발견).

| 적용 | 반영 |
|----|----|
| PC-1 | line 328 = brief v1 누락 (A·C 독립 수렴) → 1차 교정 편입 + **"§3.2" stale ref 정정** |
| CN-3/CN-4 | `--no-verify` 우회 = sensor 단독 의존 위험의 *정확한 사례* → "최종 차단 = Hermes 밖 anchor 가 보장" 명문 (self-reference 비유입) |

---

## 4. 채널명 재명명 옵션 (CN-10 — *결정 보류*, 삼안 정비 — `92cc9f3` PC-④)

> 본 brief = N1/N2'/제3안 *삼안 제시* 한정 (`92cc9f3` PC-④ — v1 양안에서 확장). 최종 선택 = 본문 교정 단계 (사용자 명시).

| 옵션 | 채널명 | 근거 | 비용 (cross-reference 갱신) |
|----|----|----|----|
| **N1 (유지)** | "Hermes-originated commit detection" | Group I N1 답습 (현 상태), cross-reference 갱신 0건 | 0줄 |
| **N2' (재명명)** | "Hermes-originated commit **provenance** (sensor)" | "signal/sensor" = *역할* 어휘(means 고정 아님, ADR-011 저촉 X) | "detection" 인용 의존 연쇄 갱신 (§5) |
| **제3안 (재명명, `92cc9f3` PC-④ 채택 권고)** | "Hermes-originated commit **provenance check**" | C 권고 — **"sensor"는 runtime 역할로 고정되어 external enforcement 축을 채널명에서 *배제*하는 부작용**. "provenance check"는 **4축(allow-list/credential/external/audit) 포괄 상위 역할어휘**, means 저촉 0 ("attestation" 은 서명 암시로 배제) | N2' 와 동일 갱신 범위 |

**N2'/제3안 채택 시 cross-reference 의존 연쇄 (`92cc9f3` 합의로 *정정* — v1 의 #20 오지목 제거):**

| 인용처 | 어휘 | N2'/제3안 갱신 필요? |
|----|----|----|
| §3.1.2 (line 448) | "Hermes-originated commit **detection**" (채널명 본체) | ✅ 필수 |
| **§2.6.3 (b) (line 328)** | "§3.2 Hermes-originated commit **detection**" (+ stale ref) | ✅ **필수 (v1 누락 — PC-1)** |
| **§3.4 (line 568)** | "Hermes-originated **detection**" (매트릭스 감지칸) | ✅ **필수 (v1 누락 — PC-1)** |
| ~~§2.2 #20 (line 178)~~ | 실어휘 = "Hermes-originated **수정 자동 reject**" (≠"detection") | ❌ **오지목 정정 — "detection" literal 아님, N2' 영향 밖** |
| §2.6.4 #1~#7 / §11.4.1 / line 221/354/1116 | "Hermes-originated commit **auto-reject**" | △ "auto-reject" 어휘 유지 시 영향 0 (§5 정합 확인) |
| system-identity-prequel §3.3 #2 | cross-doc 참조 | △ 의존 문서 연쇄 (§5) |

> ⚠️ **갱신 비용 = "detection" literal 분포(448/328/568) 한정** — v1 이 비용을 §2.2 #20 으로 오지목했으나(실어휘=auto-reject) 실제는 3 곳. 채널명 *최종 결정* = §1.4 grep 전수 재검증 (잔여 "detection" 인용 0 확인) 완결 후 본문 교정 단계 (A 권고 — cascade 측정 전 결정 위험).

---

## 5. 의존 문서·cross-reference 갱신 대상 enumeration (교정 *발효* 단계 확인 의무 — 본 brief = enumeration 만)

CLAUDE.md §7 의존 관계 + 합의 §3 + `92cc9f3` PC-5/PC-7 답습. **본 §5 = 갱신 *대상 식별* 한정, 실 편집 0건.** 단 식별은 §1.4 동적 종료 조건(grep 전수 잔여 인용 0) 의 *현 시점 결과* 이며 닫힌 목록 아님.

| 갱신 대상 | 사유 |
|----|----|
| **line 354/1116 (§2.6.4 #1 / §11.4.1 #1)** | **(PC-5)** "git pre-commit hook + Hermes-originated commit auto-reject" — 360/1122 와 *평행 frame*. 1차 교정 범위 *밖* 이나 frame 통일 시 정합 확인 (auto-reject 어휘 유지 시 영향 0, N2'/제3안 채택 시 재검토) |
| **line 221 (§2.5 #2)** | **(PC-5)** "Hermes-originated 수정 자동 reject" auto-reject literal — 정합 확인 |
| 동 §2.6.4 #2/#3/#6 (#1·#7 외) | "auto-reject" 표현 잔여 — frame 통일 시 정합 확인 (본 교정 범위 = #7, 나머지 정합 확인) |
| ~~§2.2 #20~~ | **(정정)** v1 이 "detection 메커니즘 인용"으로 분류했으나 #20 실어휘 = "수정 자동 reject"(≠detection) → "detection" cascade 영향 *밖*, auto-reject 정합 확인만 |
| 동 §2.5 #6 (G3 정의 문서 자기 보호) | 본 교정 = G3 본문 변경 → §2.5 #6 (T3 self-protection) 절차 답습 대상 |
| **§5.5.2 SPOF 의도적 수용 사유 단락** | **(PC-7)** line 784 교정 시 "credential 미격리"가 "수용된 SPOF"로 오독되지 않도록 §5.5.2 와 정합 확인 |
| **observe mode 도입처** | **(PC-7)** §3.3(784) "observe mode" 가 G3 기존 개념인지 신규 도입인지 확인 (현 §5.5 미정의 — 신규면 정의 1줄 동반) |
| `system-identity-prequel.md` §3.3 #1/#2/#4 | filesystem read-only + git pre-commit + 권위 등급 reject = line 457/648 차단 책무 출처 |
| `ADR-012` §2.12 (변조 차단 매트릭스) + §원칙 12 (single-host SPOF) + 원칙 7 (`agent=user`) | line 230/360 signed commit·`agent=user` 정합 |
| Group I `f6c6d5a` (B-1~B-6) + `92d74be` (CN-1~CN-10) + `92cc9f3` (PC-1~PC-7) | 교정 방향·조건 출처 (본문 변경 *금지* — 답습만) |

> ⚠️ 본 §5 = touch-point *외* 의 정합 확인 대상 식별. 1차 교정 범위(448/784/457/648/568/328/360/1122)를 *넘어선* 본문 변경은 별도 판단 (silent expansion 차단 — §2.5 enumeration 원칙). 단 §1.4 동적 종료 조건상 본문 교정 *발효* 단계에서 재 grep 으로 잔여 인용 0 재확인 의무.

---

## 6. ADR-011 means/ends 정합 (CN-6) — 수단 후보 열거 형식

§3 의 모든 문구안은 **목적/원칙 수준**(metadata≠root signal / positive 검증 / external enforcement / credential 격리 전제 / audit sink 변조 저항)으로 기술하고, **구체 수단은 본문 고정하지 않는다.** 추적성 위해 *수단 후보* 는 아래 비표준 열거로 분리(결정 = Backlog #6, line 805 선례·MVP-1 패턴 동형):

| 축 | 수단 *후보* (열거 — 결정 0건) | 환경 종속 (PC-7) | 결정 (Backlog #6) |
|----|----|----|----|
| positive allow-list 검증 | [ GPG signed commit / SSH signed commit / hardware-backed key 서명 / GitHub ruleset required-signature / CI provenance step 의 키 fingerprint 대조 ] 中 | ✅ GHES vs SaaS 종속 | Backlog #6 (allow-list 검증 layer) |
| external enforcement anchor | [ GitHub branch protection·ruleset / container filesystem ACL / hardware key 보유 분리 ] 中 host 밖 최소 1개 | ✅ GHES vs SaaS 종속 | Backlog #6 (anchor 구성) |
| credential boundary 격리 | [ Hermes 컨테이너 사람 키 미주입 / secrets vault / KMS-backed ] 中 | ✅ 환경(local/CI/Docker) 종속 | Backlog #6 (격리 구현) |
| audit sink integrity | [ 외부 append-only sink / read-only mount 분리 매체 / 분산 sync ] 中 — Hermes 쓰기 불가 | ✅ 환경 종속 | Backlog #6 (sink 구성) |

> PC-7 (환경종속 4행 일관화): v1 은 일부 행만 "환경 종속" 표기 → 4행 모두 일관 표기 (G4 발견 = "키 fingerprint 대조 = CI provenance step 구현 필요, 0-구현 아님"이 환경 종속과 직결). Backlog #6 cross-ref 추가로 means 결정 단계 추적성 확보.

> **정합 결론**: 본문 = 목적/원칙, 수단 = 후보 열거(결정 보류). 이는 ADR-011 §2.1 means/ends + Group I framing N1(수단 명칭 고정 보류) + Provider Liquidity 정합. **수단 *결정 고정* = 본 brief §0.3 금지 + Backlog #6.**

---

## 7. 교정 *형태* / 권위 (합의 §5 답습)

| 계층 | 본 brief 산출 | 발효 권한 |
|----|----|----|
| **brief (본 문서)** | touch-point별 문구 교정안 *후보* (PC-1~PC-7 반영) + CN/PC 매핑 + 채널명 삼안 + 동적 종료 조건 + 의존 연쇄 enumeration | 본 brief = 후보 정비 — **발효 아님** |
| **본문 교정 결정 (DESIGN)** | line 448/784/457/648/568/328/360/1122 *최종 문구* / 채널명(N1·N2'·제3안) / 수단 후보 표기 *결정* + §1.4 grep 전수 잔여 인용 0 재확인 | **사용자 명시 + 본문 교정 단계** (R-I-CONFIG-CHANGE = T3) |
| **구현 (IMPLEMENTATION)** | 실 hook / ruleset / CI provenance / filesystem ACL / credential 격리 / audit sink 본문 | **Backlog #6 + 별도 풀 3+1 (R-I-IMPL-BOUNDARY)** |

- 현 상태: **G3 DESIGN PASS (방향·조건·범위) / 문구 PENDING / IMPLEMENTATION PENDING**.
- **교정 형태 (합의 §5 권고)**: "단순 텍스트 정정"이 아닌 §2.2 #20 auto-reject 의 *판정 기준 변경* = **T3 (R-I-CONFIG-CHANGE) → Reviewer-only 부적격.** 단 식별 frame 은 Group I `f6c6d5a` + `92d74be` 에서 *이미* 만장일치 확정 → 본문 교정 단계 = **brief §5.3 "본문 반영 한정 합의 + 4 결정 항목(① 문구 ② 범위 ③ author 메타 어휘[CN-8] ④ 채널명[CN-10]) scope 명문 고정"** 권고 (풀 3+1 frame 재투표 중복 제거, B-5 T3 다관점 유지). 풀 3+1 전면 재실행 vs 축소 형태 *최종 결정* = 사용자 명시.
- **Rollback Trigger**: R-I-CONFIG-CHANGE(T3, 본문 교정 자체) + R-I-IMPL-BOUNDARY(실 hook/ruleset/credential/sink 구현 = Backlog #6).

---

## 8. 미해소 + 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

### 8.1 미해소 쟁점

| # | 쟁점 | 분리 사유 |
|----|----|----|
| 1 | 각 touch-point 최종 *문구* 확정 + §1.4 grep 전수 잔여 인용 0 재확인 | 본 brief = 후보 한정. 확정 = 본문 교정 단계 |
| 2 | 채널명 N1(유지) / N2'(provenance sensor) / 제3안(provenance check) 결정 | CN-10/PC-④ = 삼안 개방, 결정 = §1.4 cascade 재검증 후 본문 교정 단계 |
| 3 | line 230/805 어휘 정합 옵션 채택 여부 | G5 = 정합 참조만, 기본 무변경 |
| 4 | 수단 후보 → 결정 고정 | Backlog #6 + CN-6 (means/ends) |
| 5 | observe mode 기간 / threshold | CN-9 구체 수치 = threshold 고정 영역 (별도) |
| 6 | credential boundary / external anchor / audit sink 실 구성 | Implementation/Runtime PASS (Backlog #6) |
| 7 | §5.5.2 수용사유 정합 / observe mode 도입처 (PC-7) | 본문 교정 단계 정합 확인 |

### 8.2 다음 단계 옵션 (v2 = `92cc9f3` BLOCKING PC-1~PC-4 반영 완료)

| 옵션 | 영역 | 후속 |
|----|----|----|
| **(A)** | 본 brief v2 승인 → **본문 교정 단계 진입** (§7 권고 = "본문 반영 한정 합의 + 4 결정 항목 scope" — 단 PC-1~PC-7 이미 합의 발효, 본문 교정 단계는 *최종 문구 결정* + §1.4 재 grep) | 본문 교정 진입 |
| (B) | 본 brief v2 일부 수정 요청 | v3 작성 |
| (C) | 본 brief v2 보류 → 다른 backlog (G1 PR/approval auto-reject / 2차 vendor / GP-5 C-2 facade real P1 v2 Backlog #4) | 별도 brief |
| (D) | 본 brief v2 보류 → 세션 종료 | — |

> 본 brief v2 = **brief 단계 한정** (staged cycle: brief → 승인 → 합의 → commit → push). 본문 교정 단계 / 채널명 결정 / 수단 고정 = 사용자 명시 승인 후 별도 단계. 본문 교정 = **T3 → R-I-CONFIG-CHANGE → Reviewer-only 부적격** (합의 §5 답습).

---

## 9. 한 단락 요약

**(v2 = `92cc9f3` patch brief 검증 풀 3+1 합의 BLOCKING PC-1~PC-4 반영판.)** `92d74be` 가 *방향(4축)·조건(CN-1~CN-10)·범위* 를 확정한 G3 `hermes-not-root-of-trust-runtime.md` 결함 교정을 touch-point별 문구 교정안 *후보* 로 환원한 patch brief 를, `92cc9f3` 합의가 APPROVE WITH CONDITIONS 로 검증하며 낸 BLOCKING 4건을 반영한 v2. **v1 → v2 핵심 변경**: (PC-1) brief v1 의 8 touch-point 정적 열거가 **line 568(§3.4 통합 매트릭스 — "detection" 직접 인용 + "git pre-commit" CN-3 위반 차단 frame)·line 328(§2.6.3(b) — "detection" 2번째 literal + "§3.2" stale cross-ref, 실제는 §3.1.2)을 silent 누락**한 것을 보강 — **10 touch-point 로 확대 + 범위 종료 조건을 "정적 열거" → "grep 전수 잔여 'detection'/'auto-reject' 인용 0 검증" 동적 조건(§1.4)으로 전환**(line 457 누락→568·328 또 누락의 구조적 반복을 harness feedforward 로 차단); (PC-2) **CN-4 "실 anchor(명목 anchor 금지)"·CN-7 audit sink 별개성·CN-8 author 배제의 전파 비대칭 해소**(v1 = 한 touch-point 에만 → 448·648·360·1122 전파); (PC-3) **enforcement 보장 속성(ends) = "push/merge 전 차단 보장" 1구 명문**(means 후보 §6 과 분리 — "언제·어떤 속성으로 차단"은 ends·"무엇으로"는 means); (PC-4) **line 360/1122 에 "author=user 강제" 표현 제거에 그치지 않고 "author 판정 입력 아님·audit 사후 대조 전용" negative 배제 명제 부가**(회귀 통로 차단). 1차 교정 = line 448/784/457/648 **+568/328**, 가정 잔존 = 360/1122(P1 dangling 방지), 정합 참조만 = 230/805(single-host 비대칭 해소 시 정합). 채널명(CN-10/PC-④) = N1(유지) / N2'(provenance sensor) / **제3안 "provenance check"(4축 포괄 상위 역할어휘, "sensor"의 external enforcement 축 배제 부작용 회피, means 저촉 0) 삼안 확장** — 단 결정은 §1.4 cascade 재검증 후 본문 교정 단계(채널명 cascade = "detection" literal 448/328/568 한정, v1 의 #20 오지목 정정). 모든 문구안 = **목적/원칙 수준**, 수단은 **후보 열거(환경종속 4행 일관 + Backlog #6 cross-ref, CN-6/PC-7)** — ADR-011 means/ends 정합. 교정 형태 = **R-I-CONFIG-CHANGE=T3·Reviewer-only 부적격, "본문 반영 한정 합의 + 4 결정 항목 scope"** 권고. 권고 PC-5(line 354/1116/221 enumeration)·PC-6(448 거대 셀 분해)·PC-7(§5.5.2 정합·observe mode 도입처)도 반영. 본 brief v2 는 결론을 *선취하지 않으며* — 문구 *최종 확정*·채널명 *결정*·수단 *고정*·실 구현(hook/ruleset/CI/credential/sink)은 모두 사용자 명시 + 별도 단계 — **G3 본문 실제 수정 / git hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 / 채널명 결정 / ADR·합의 본문 자동 갱신 / commit / push = 모두 0건** 이다.

---

## 부록 A — 본 brief 답습 출처

| 출처 | 답습 영역 |
|----|----|
| **`3plus1-consensus-2026-05-21-g3-patch-brief.md` (`92cc9f3`) PC-1~PC-7** | **v2 BLOCKING 반영 (v2 변경 이력 + §1.3/§1.4 + §3.9/§3.10 + §4 삼안 + §5 + §6)** |
| `3plus1-consensus-2026-05-20-g3-metadata-detection-defect-correction.md` §2.1 (교정 방향 4축) | 문구안 입력 제약 (§1.1) |
| 동 §2.2 (CN-1~CN-9) + §2.3 (CN-10) | touch-point별 CN 매핑 (§3) + 채널명 (§4) |
| 동 §3 (교정 범위 표) | 1차 4 / 가정 잔존 2 / 정합 참조 2 (§1.3, §3) |
| 동 §5 (결정/설계/구현 경계) | 교정 형태·권위 (§7) |
| 동 §1.3 G1 (line 457 누락) / G2 (audit sink) / G5 (230·805 선례) | §3.2 / §2 audit 축 / §3.7~3.8 |
| `g3-line448-784-...-correction-brief.md` (`afb92de`) | 결함 정의·3축 검토 선행 |
| `hermes-not-root-of-trust-runtime.md` line 448/784/457/648/360/1122/230/805/**568/328** 원문 | 현 본문 verbatim (§3) |
| ADR-011 §2.1 (means/ends) | 수단 후보 열거 형식 (§6) |
| Group I `f6c6d5a` (B-1~B-6) + brief §8 (R-I-CONFIG-CHANGE / R-I-IMPL-BOUNDARY) | Rollback Trigger (§7) |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경 — 문구안 = 후보 한정) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경) / **Hermes runtime 변경** / **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 (positive allow-list 키 종류·서명 방식·차단 지점·sink 매체) / threshold 고정 (observe mode 기간) / **채널명 재명명 *결정*** (CN-10/PC-④ = 삼안 개방, N1/N2'/제3안 최종 선택 = 본문 교정 단계) / 문구 교정안 *최종 확정* (후보 한정) / credential boundary 실분리 구현 / external enforcement anchor 실 구성 / audit sink 실 구성 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / 교정 형태·범위·framing *결정 발효* (권고 한정) / Backlog #4·#6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
