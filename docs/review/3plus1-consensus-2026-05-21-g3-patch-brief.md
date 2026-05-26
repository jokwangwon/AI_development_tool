# 3+1 합의 보고서 (후속) — G3 본문 교정 patch brief "본문 반영 한정 합의"

> **본 합의는 추론적 검증(권고) 한정이며, `92d74be` 합의의 *후속(patch brief 검증)* 이다.** 본 합의의 어떤 §도 그 자체로 (i) **G3 (`hermes-not-root-of-trust-runtime.md`) 본문 실제 수정** (line 448/784/457/648/360/1122/230/805 및 line 568/328/354/1116/221 포함 어떤 줄도), (ii) git hook 구현 (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step), (iii) GitHub ruleset·branch protection 변경, (iv) CI workflow 변경 (actual run 재실행 / workflow_dispatch / paths 필터), (v) Hermes runtime·upstream 변경, (vi) **채널명 재명명 *결정*** (N1/N2'/제3안 최종 선택), (vii) 수단 결정 고정, (viii) threshold 고정, (ix) Operational Readiness PASS / Hermes PMO 격상, (x) ADR·Group 합의 본문 자동 갱신, (xi) 외부 LLM 응답 강제 채택·추가 호출, (xii) commit / push, (xiii) 5 영구 핵심 제약·Provider Liquidity 5-way 약화 를 발생시키지 않는다. **frame 4축(positive allow-list / credential boundary / external enforcement / audit sink integrity)은 `f6c6d5a` + `92d74be` 만장일치 확정 — 본 합의는 재논쟁하지 않으며 4 결정 항목(① 문구 ② 범위 ③ author 어휘 ④ 채널명)만 다룬다.**

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — "본문 반영 한정 합의" (frame 재논쟁 제거, 4 결정 항목 scope)
**합의 입력**: `docs/phase0/g3-metadata-detection-correction-patch-brief.md` (DRAFT v1 — 본 합의 시점 untracked → BLOCKING PC-1~PC-4 반영 v2 = 별도 단계)
**1차 권위 답습**: `92d74be` (CN-1~CN-10) + `f6c6d5a` (B-1~B-6) + ADR-011 §2.1 means/ends
**판정**: **APPROVE WITH CONDITIONS** (문구 교정안 *방향* 승인 + 신규 조건 PC-1~PC-7. brief 의 핵심 결함 = 8 touch-point 정적 열거가 line 568/328 등 동형 touch-point 를 silent 누락)
**Reviewer 직접 G3 본문 재검증 완료**: line 568 / 328 / 178(#20) / 354 / 1116 / 221 / 91 verbatim 확인 (§1.5)

---

## 0. 합의 대상 + 선행 맥락

`92d74be` 합의가 G3 결함 교정의 *방향(4축)·조건(CN-1~CN-10)·범위(8 touch-point)·형태(본문 반영 한정 합의 + 4 결정 항목)* 를 권고로 확정한 뒤, 그 권고를 **touch-point별 실 문구 교정안 후보** 로 환원한 patch brief(DRAFT v1)를 검증한다. frame 4축은 `f6c6d5a`+`92d74be` 만장일치 확정 사항이므로 **본 합의는 재논쟁하지 않는다**. scope = 4 결정 항목(① 문구 ② 범위 ③ author 어휘 ④ 채널명) 한정.

---

## 1. 교차 비교 (일치 / 부분 / 불일치 / 누락)

### 1.1 일치 (Consensus — 3 Agent 모두 동의)

| # | 일치 항목 | A | B | C |
|----|----|----|----|----|
| K1 | 8 touch-point verbatim 인용 정확 (행번호·셀 오차 0) | ✅ | ✅ | ✅ |
| K2 | author 어휘(③) 방향 = "판정 경로 제외·audit 보조 전용" 정확하나 360/1122 에 **negative 배제 명제 미부가** 잔존 | ✅(Q4) | ✅(B2) | ✅(Q2) |
| K3 | line 360↔1122 동기쌍 = dangling 방지 정합 (P1) | ✅ | ✅(암묵) | ✅ |
| K4 | 채널명(④) N1 단순 유지는 결함 어휘 잔재 위험, 그대로 두지 말 것 | ⚠️(보정 후 재평가) | (양안 승인) | ✅(제3안) |
| K5 | 230/805 = 정합 참조만, single-host 비대칭 해소가 핵심 (CN-6 805 GPG 복사 금지 유지) | ✅ | ✅(Q7) | (동의) |
| K6 | 모든 문구안 = 목적/원칙 수준, 수단 = 후보 열거 (CN-6 정합) | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial — 2 동의)

| # | 항목 | 동의 | 이견/보강 |
|----|----|----|----|
| PA1 | **enforcement *보장 시점/속성* 이 ends 로서 미명시 → CN-4 명목화가 문구 수준 재현** | A(Q5) 명시 / B(B1 "실 anchor" 누락)이 동일 결함을 다른 각도로 포착 | C 미언급 — Reviewer: A·B 동형 지적, 채택 (PC-3) |
| PA2 | **CN-4/CN-7/CN-8 의 touch-point 간 전파 비대칭** (한 곳만 강하게, 나머지 약) | B(Q1·Q3·Q5) 명문 / A(이중화)·C(568 방치) 가 동일 패턴 다른 사례 | Reviewer: 단일 결함(비대칭 전파)의 3 사례 → 채택 (PC-2) |

### 1.3 불일치 (Divergence — Reviewer 판정 필요)

| # | 쟁점 | 입장 | Reviewer 판정 |
|----|----|----|----|
| **DV1** | **채널명(④) 안의 수** | A=N1 유지(cascade 보정 후 재평가, 갱신비용 brief 표기보다 큼) / B=N1·N2' 양안(N2' 미세 안전 우위) / C=**제3안 "provenance check" (삼안 확장)** | **C 우월 — 삼안 확장 채택(§2.4).** 단 *결정* 아닌 옵션 확장. 근거: N2' "sensor"가 external enforcement 축을 채널명에서 배제하는 부작용(C)은 line 568·648 의 "sensor 신호 / 최종 reject = Hermes 밖" 이중 구조와 대조해 타당. 단 A 의 "갱신비용 측정 전 결정 위험"도 정당 → **결정은 cascade(PC-1) 완결 후 본문 교정 단계** |
| **DV2** | **enforcement 시점 = means 인가 ends 인가** | A=시점은 means 아닌 ends(미명시 시 CN-4 명목화 재현) | **A 인정 — CN-6 과 긴장 없음.** "*언제* 차단이 보장되는가"(보장 속성)는 ends, "*무엇으로* 차단하는가"(ruleset vs ACL vs hardware key)는 means. brief §3.2 가 means(pre-commit hook 등 = §6 후보)는 분리했으나 enforcement *보장 속성* 을 ends 로 명문화하지 않아 CN-4 가 약화 가능. 채택 (PC-3) |

### 1.4 누락 (Gap — 특정 Agent 단독, Reviewer 중요도 평가 + 직접 본문 검증)

| # | 단독 발견 | 발견 | Reviewer 판정 (본문 직접 확인) |
|----|----|----|----|
| **G-a** | **⭐ line 568 (§3.4 통합 매트릭스) 누락** — 채널명 "detection" 직접 인용 + 차단칸 "git pre-commit"(CN-3 위반 frame) | C | ✅ **채택 (BLOCKING, PC-1).** 본문 확인: line 568 = "... Hermes-originated **detection** ... \| ... git pre-commit ...". brief §3(8 touch-point)·§5(enumeration) 어디에도 없음. 1차 4줄 + 360/1122 만 고치면 **본문 내부 불일치 + (N2' 시) line 1122 와 동형 dangling**. C 의 P1급 판정 정확 |
| **G-b** | **line 328 = "Hermes-originated commit detection" 2번째 literal 인용 누락 + brief §4 가 #20 을 detection 인용처로 오지목** | A·C **독립 수렴** | ✅ **채택 (BLOCKING, PC-1).** 본문 확인: line 328 = "... §3.2 Hermes-originated commit **detection** + pre-commit hook ...". 추가 발견: **line 328 의 "§3.2" cross-ref 가 stale** — "detection" 채널은 §3.1.2(448)에 있고 §3.2(479)는 "Upstream Silent Breakage". 그리고 line 178 #20 실어휘 = "Hermes-originated **수정 자동 reject**"(≠detection) → **A 의 #20 오지목 지적 정확**. brief §4 N2' cascade 목록이 line 328 직접 인용·§3.2 stale ref 미포착 |
| **G-c** | **line 354/1116/221 = "auto-reject" + "git pre-commit hook" framing, 360/1122 와 평행이나 §5 미열거** | A(이중화) / C(327/354/1116/221 auto-reject 반복) | ✅ **부분 채택 (권고, PC-5).** 본문 확인: line 354·1116 = Gate definition tampering 방지, "filesystem read-only + git pre-commit hook + Hermes-originated commit auto-reject". 1차 교정 4줄 범위 *밖* 이나 frame 통일 시 검토 대상 → enumeration 보강 권고 |
| **G-d** | **line 91 "모순 detection log" = 범위 밖 (오탐 방지)** | C | ✅ **채택 (정보성).** 본문 확인: line 91 = ADR/SDD 모순 detection (commit 식별과 무관). 교정 대상 아님 — C 의 오탐 차단 정확 |
| **G-e** | **line 448 거대 셀 → 본문 한 구 요약 + 하단 주석 분리** (457 패턴 동형) | C | ✅ **채택 (권고, PC-6).** brief §3.1 후보가 단일 표 셀에 6 요소(CN-1/3/7/8/10) 압축 → 가독성·재편집 범위 우려 타당. 형식 선택 = 본문 교정 단계 |
| **G-f** | **§5.5.2 수용사유 단락과 line 784 교정 정합 / "observe mode" G3 신규개념 여부 / §6 환경종속 4행 일관화** | B(R3·R4) / C(Q6) | ✅ **채택 (권고, PC-7).** brief 가 784 교정 시 §5.5.2 정합·observe mode 도입처 미명시 |

### 1.5 Reviewer 직접 본문 재검증 (G3 verbatim — 교차 검증 근거)

| Line | 확인된 본문 (핵심) | 판정 |
|----|----|----|
| 568 | "Hermes-originated **detection** ... \| ... git pre-commit ..." | C 정확 — 누락 BLOCKING |
| 328 | "§3.2 Hermes-originated commit **detection** + pre-commit hook" | A·C 정확 — 누락 + §3.2 stale ref 추가 발견 |
| 178 (#20) | "합의 보고서 git commit 보존 + Hermes-originated **수정 자동 reject**" | A 정확 — #20 ≠ "detection" literal, brief §4 오지목 |
| 354/1116 | "git pre-commit hook + Hermes-originated commit auto-reject" | G-c — 범위 밖이나 frame 평행 |
| 221 | "git append-only ... Hermes-originated 수정 자동 reject" | G-c — auto-reject literal, §2.5 행 |
| 91 | "ADR/SDD 모순 **detection** log" | C 정확 — 무관, 범위 밖 |

---

## 2. 4 결정 항목 합의 도출

### 2.1 항목 ① 문구 — 조건부 승인

3 Agent 공히 "방향 정확, 보강 필요". 합의 = 다음 BLOCKING 조건부로 문구 *후보* 승인:
- **PC-2 (전파 비대칭 해소, BLOCKING)**: CN-4 "실 anchor" 수식을 line 448·648 에도 부가(현재 §3.2/457 에만) / CN-8 author 배제를 360/1122 에도 / CN-7 audit sink 별개성을 648 에도. (B-B1·B-B2 + A 이중화 + C 568 = 동일 비대칭의 4 사례)
- **PC-3 (enforcement 보장 속성 = ends 명문, BLOCKING)**: "*무엇으로* 차단(means, §6 후보)" 과 별개로 "*언제·어떤 속성으로* 차단이 보장(ends)" 1구 명문 — CN-4 명목 anchor 오독 통로 차단 (DV2 + PA1).

### 2.2 항목 ② 범위 — 조건부 승인 (BLOCKING)

- **PC-1 (누락 touch-point 추가 + 동적 종료 조건, BLOCKING)**: **line 568·328 을 교정 범위에 추가**(둘 다 "detection" 채널명 직접 인용 + 568 은 CN-3 위반 차단 frame). 그리고 항목②를 "8 touch-point **정적 열거**" 에서 **"grep 전수 잔여 'detection'/'auto-reject' 인용 0 검증" 동적 종료 조건**으로 전환 — 457 누락→568·328 또 누락의 *구조적 반복* 을 harness feedforward 로 차단. Reviewer 직접 grep 으로 line 328 §3.2 stale ref 까지 발견된 점이 정적 열거의 위험을 실증.
- **PC-5 (line 354/1116/221 enumeration 보강, 권고)**: 1차 교정 범위 밖이나 frame 평행 → §5 정합 확인 대상에 명시.

### 2.3 항목 ③ author 어휘 — 조건부 승인 (BLOCKING)

- 방향(448 "판정 경로 제외·audit 보조 전용") 만장일치 정확. 단 **PC-4 (BLOCKING)**: line 360/1122 가 "author=user 강제" 표현 *제거* 만 하고 **author 판정 *배제* negative 명제를 부가하지 않으면** author 가 판정 보조로 재유입되는 회귀 통로 잔존(B-B2). C 의 "판정 입력 아님·audit 사후 대조 전용"(모호어 "보조" 회피)을 더 좁은 표현으로 권고.

### 2.4 항목 ④ 채널명 — 삼안 확장 (결정 보류)

- brief 의 N1/N2' 양안을 **N1(유지) / N2'("provenance sensor") / 제3안("provenance check") 삼안으로 확장**(C). 근거: N2' "sensor"는 external enforcement 축을 채널명에서 배제하는 부작용, 제3안 "provenance check"가 4축 포괄 상위 역할어휘로 means 저촉 0. 단 **DV1: 최종 결정은 PC-1 cascade 완결(전수 인용 식별) 후 본문 교정 단계** — A 의 "갱신비용 측정 전 결정 위험" 정당. line 568·328 누락 상태에서 채널명 결정 시 cascade 불완전.

---

## 3. 판정 + 조건 목록

### 판정: APPROVE WITH CONDITIONS

brief 의 4축 문구 환원·CN 매핑·means/ends 정합은 견고하나, **8 touch-point 정적 열거가 line 568·328(둘 다 "detection" 직접 인용, 568 은 CN-3 위반 frame)을 silent 누락** 한 것이 가장 무거운 결함이며, 이는 line 457 누락이 이미 한 차례 드러낸 *구조적 반복* 이다.

| 구분 | 조건 | 출처 |
|----|----|----|
| **BLOCKING** | **PC-1** line 568·328 범위 추가 + 항목② "grep 전수 잔여 인용 0" 동적 종료 조건 전환 | C(G-a) + A·C(G-b) + Reviewer 본문 검증 |
| **BLOCKING** | **PC-2** CN-4/CN-7/CN-8 의 448·648·360·1122 전파 비대칭 해소 | B-B1·B-B2 + A + PA2 |
| **BLOCKING** | **PC-3** enforcement 보장 속성 = ends 1구 명문(means 후보와 분리) | A(Q5)·B(B1) + DV2 |
| **BLOCKING** | **PC-4** line 360/1122 author 판정 *배제* negative 명제 부가 | B-B2 + C(Q2) |
| 권고 | **PC-5** line 354/1116/221 enumeration 정합 확인 추가 | A·C(G-c) |
| 권고 | **PC-6** line 448 거대 셀 → 요약 + 하단 주석 분리(457 패턴) | C(G-e) |
| 권고 | **PC-7** §5.5.2 수용사유 정합 / observe mode 도입처 / §6 환경종속 4행 일관화 | B(R3·R4)·C(Q6) |

> PC-1~PC-4 = BLOCKING (본문 교정 *발효* 단계에서 충족 의무, brief 단계에서는 v2 반영 권고). PC-5~PC-7 = 권고.

---

## 4. 경계 명시 (권고 한정)

본 합의 = **추론적 검증 = 권고 한정.** 본 합의는 frame 4축을 재논쟁하지 않으며(선행 만장일치 확정), 4 결정 항목(문구·범위·author 어휘·채널명)의 *후보·조건* 만 평가한다. **G3 본문 실 수정 / line 568·328 포함 어떤 줄의 편집 / 채널명 결정(N1/N2'/제3안) / 수단 고정 / git hook·ruleset·CI 구현 / commit / push** = 모두 사용자 명시 + 별도 단계 (**R-I-CONFIG-CHANGE = T3**, Reviewer-only 부적격 — §2.2 #20 판정 기준 변경이므로). 본 합의는 brief 의 자동 다음 단계 진입을 발생시키지 않는다.

---

## 5. 합의 한 단락 요약

`92d74be` 가 방향·조건·범위를 확정한 G3 결함 교정을 8 touch-point별 문구 *후보* 로 환원한 patch brief 에 대해, Agent A(구현/정합)·B(보안)·C(대안) + Reviewer 가 **APPROVE WITH CONDITIONS** 로 합의한다 — 4축 frame 문구 환원·CN 매핑·means/ends 정합은 견고하나 (i) **brief 가 line 568(§3.4 매트릭스, "detection" 직접 인용 + "git pre-commit" CN-3 위반 차단 frame) 과 line 328("detection" 2번째 literal + §3.2 stale cross-ref)을 silent 누락**(C 단독 G-a + A·C 독립 수렴 G-b, Reviewer 가 G3 본문 직접 grep 으로 재검증·확정 + line 328 의 "§3.2" 참조가 실제로는 §3.1.2 를 가리켜야 할 stale ref 임을 추가 발견 + brief §4 가 #20 을 "detection 인용처"로 오지목했으나 #20 실어휘는 "수정 자동 reject"임을 확인), (ii) CN-4/CN-7/CN-8 이 한 touch-point 에만 강하게 반영된 **전파 비대칭**(B-B1·B-B2 + A 이중화 + C 568 = 동일 결함 4 사례), (iii) **enforcement 보장 속성이 ends 로 미명문**되어 CN-4 명목 anchor 오독 통로 잔존(A·B 동형, DV2 = "언제·어떤 속성으로 차단 보장"은 ends·"무엇으로 차단"은 means 로 CN-6 과 긴장 없음), (iv) line 360/1122 가 "author=user 강제" 제거만 하고 **author 판정 배제 negative 명제 미부가**로 회귀 통로 잔존(B-B2 + C)이 BLOCKING 4건(PC-1~PC-4)이다. 따라서 항목② 범위는 "8 touch-point 정적 열거" 에서 **"grep 전수 잔여 'detection'/'auto-reject' 인용 0 검증" 동적 종료 조건**으로 전환할 것을 권고(457→568·328 누락의 구조적 반복을 harness feedforward 로 차단), 항목④ 채널명은 N1/N2' 양안을 **제3안 "provenance check"(4축 포괄 상위 역할어휘, means 저촉 0) 삼안으로 확장**하되 *결정* 은 PC-1 cascade 완결 후 본문 교정 단계로 보류(갱신비용 측정 전 결정 위험, A). PC-5~PC-7(line 354/1116/221 enumeration·448 거대 셀 분해·§5.5.2 정합 등)은 권고. 본 합의는 추론적 검증(권고) 한정 — **G3 본문 실 수정 / line 568·328 포함 어떤 줄의 편집 / 채널명 결정 / 수단 고정 / git hook·ruleset·CI 구현 / ADR·합의 본문 갱신 / commit / push = 모두 0건**이며, 실 *결정/구현* 은 사용자 명시 + 별도 단계(R-I-CONFIG-CHANGE = T3 본문 교정 + Backlog #6 Runtime)이다.

---

## 6. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 발견 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | 8 touch-point verbatim 100% 정확(오차 0) + **line 328 = detection 2번째 literal 누락 + brief §4 가 #20 을 detection 인용처로 오지목(#20 실어휘=auto-reject)** + enforcement 보장 *시점*=ends 미명시→CN-4 문구 명목화 재현 + 채널명 갱신비용 brief 표기보다 큼(N1 보정 후 재평가) |
| **Agent B** (보안) | "안전하고 견고한가?" | CN-1~CN-10 전부 반영되나 **CN-4/CN-7/CN-8 전파 비대칭** + B1(448/648 "실 anchor" 수식 누락→명목 anchor 오독) + B2(360/1122 author 배제 negative 명제 미부가→회귀 통로) BLOCKING 2건 + §5.5.2 정합·observe mode 도입처·`.git/` CN-5·means/ends CN-6 확인 |
| **Agent C** (대안) | "더 나은 방법이 있는가?" | **⭐ line 568(§3.4 매트릭스) 누락 = P1급**(detection 직접 인용 + git pre-commit CN-3 위반 frame, N2' 시 dangling) + **항목② 동적 종료 조건(grep 전수 인용 0)** + 채널명 **제3안 "provenance check" 삼안** + author "판정 입력 아님·audit 사후 대조 전용" + 448 거대 셀 분해 + line 91 범위 밖(오탐 차단) |
| **Reviewer** | "최선의 합의는?" | 교차(일치 6 / 부분 2 / 불일치 2 / 누락 6) + **G3 본문 직접 재검증**(568·328·178·354·1116·221·91 verbatim, line 328 §3.2 stale ref 추가 발견) + APPROVE WITH CONDITIONS + BLOCKING 4(PC-1~PC-4)·권고 3(PC-5~PC-7) + 채널명 삼안 확장(결정 보류) + 권고 한정 경계 |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의 보고서의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328/354/1116/221 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run 재실행 / workflow_dispatch / paths 필터) / **Hermes runtime·upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 / threshold 고정 / **채널명 재명명 결정** (N1/N2'/제3안 최종 선택 = 본문 교정 단계) / 문구 교정안 최종 확정 / credential boundary 실분리·external enforcement anchor·audit sink 실 구성 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·#6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / commit·push 외 자동 다음 단계 진입 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
