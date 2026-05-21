# 3+1 합의 보고서 — G3 본문 교정 "본문 반영 한정 합의" (4 결정 항목)

> **본 합의 = 추론적 검증(권고) 한정.** frame 4축(positive allow-list / credential boundary / external enforcement / audit sink integrity)은 `f6c6d5a`+`141bbc9` 만장일치 확정 — 재논쟁 없음. 본 합의는 4 결정 항목(① 최종 문구 ② 범위 종료 ③ author 어휘 ④ 채널명)의 *후보·조건* 만 평가한다. **G3 본문 실 수정 / 어떤 줄(443/445/568/328 포함)의 편집 / 채널명 결정 / literal 갱신 / 수단 고정 / git hook·ruleset·CI 구현 / commit / push = 모두 0건.** 실 결정/구현 = 사용자 명시 + 별도 단계 (R-I-CONFIG-CHANGE = T3, Reviewer-only 부적격).

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — "본문 반영 한정 합의" (frame 재논쟁 제거, 4 결정 항목 scope)
**합의 입력**: `docs/phase0/g3-body-correction-stage-entry-brief.md` (진입 brief DRAFT v1) + `docs/phase0/g3-metadata-detection-correction-patch-brief.md` (patch brief v2, `e8e47de`)
**1차 권위 답습**: `92cc9f3` (PC-1~PC-7) + `141bbc9` (CN-1~CN-10) + `f6c6d5a` (B-1~B-6) + ADR-011 §2.1 means/ends
**판정**: **APPROVE WITH CONDITIONS** (4 결정 항목 中 ①③ 결정·④ 어휘 권고·② 미충족 → grep 전수 완주 선결. BLOCKING 5 + 권고 4)
**Reviewer 직접 G3 전수 grep 재실행 완료**: "provenance"=0 / 443·445·1118·1121·328 verbatim 확인 / 12줄 1차 + 정합 群 + 범위밖 群 완전 분류

---

## 0. 합의 대상

`92cc9f3` 합의(APPROVE WITH CONDITIONS, PC-1~PC-7)가 검증한 patch brief v2(`e8e47de`) + 진입 brief 에 대해, 본문 교정 단계가 *결정*할 4 항목과 PC-1~PC-4 충족 판정을 다룬다. **핵심 = 통합 grep 확정으로 PC-1 동적 종료 조건의 "잔여 미분류 0" 도달 가능성 판정.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 일치 항목 |
|----|----|
| K1 | "provenance" = 0 hits → 채널명 cascade 대상 = "detection" literal 한정 (A·C 직접 확인, Reviewer 재확인) |
| K2 | 채널명 ④ 결정은 cascade(enumeration) *완결 후* 본문 교정 단계 (재명명 시 dangling 위험) |
| K3 | author 어휘 ③ = "판정 입력 아님·audit 사후 대조 전용" 유지 (line 465 별도 audit JSONL 본문 근거) — 변경 불요 |
| K4 | C 群 "auto-reject" 행위명 = "Hermes commit *이* reject 대상" 독해로 CN-3 양립, 전면 reframe 불요 (silent scope expansion 위반 회피) |
| K5 | **진입 brief §4.2 enumeration 이 또 불완전** — A·C 가 §4.2 *밖* 추가 hit 를 독립 발견 (PC-1 정적 닫힌 목록 = 위반) |

### 1.2 부분 일치 (Partial — 2 동의)

| # | 항목 | 동의 | Reviewer |
|----|----|----|----|
| PA1 | 1118/1121 (§11.4.1 #3/#6) = 정합 확인 群 편입 | A 명시 / B(C群 전수 정합) | C 미언급 — 채택. 360↔1122·354↔1116 과 동형 RESOLVED 평행행 |
| PA2 | 889(§6.4) = 457 동형 약한 CN-3 긴장 | A 명시 / B(차단지점) | C 미언급 — 정합 확인 群 편입 (행위명 유지 시 영향 0) |

### 1.3 불일치 (Divergence)

| # | 쟁점 | 입장 | Reviewer 판정 |
|----|----|----|----|
| **DV1** | ② 범위 = 본문 편집 즉시 가능 vs grep 전수 선결 | A=발효 grep 전수 비협상 의무(②미충족) / B=발효 전 BLOCKING(재grep 잔여0) / C=PC-1 패턴에 섹션/컬럼 헤더 추가 | **A·B·C 동형 = grep 전수 완주가 선결.** 본 합의(추론적)에서 확정 enumeration 산출 가능하나 "잔여 0" *최종 확인* = 발효 단계 재grep 의무. **본문 실 편집 즉시 불가** (§5) |
| **DV2** | ④ 채널명 최종안 | A=cascade 완결 후 / B=APPROVE(v2 문구) / C=제3안 "provenance check" | **C 제3안 우월(어휘 채택 권고), 단 *결정* 보류** — A 의 "cascade 미완 중 결정 위험" 정당 (C 의 443/445 헤더 누락 = cascade 또 불완전 실증) |

### 1.4 누락 (Gap — 단독 발견, Reviewer 본문 직접 확인)

| # | 단독 발견 | 발견 | Reviewer 판정 (grep 확인) |
|----|----|----|----|
| **G-a** | ⭐ **443 섹션 헤더 "(Detection)" + 445 컬럼 헤더 "감지 channel"** = 채널명 본체 헤더, §4.2 미포착 | C | ✅ **채택 (BLOCKING 보강, PC-1).** 확인: 443 "#### 3.1.2 감지 방법 (Detection)" / 445 "\| 감지 channel \| 메커니즘 \| 시점 \|". **재명명 시 헤더-본체 dangling 확정.** 단 485/528(§3.2.2/§3.3.2 "(Detection)") = *다른 채널* → (iii) 범위 밖 |
| **G-b** | **1118/1121** = RESOLVED 매트릭스 평행행, §4.2 C群 미열거 | A | ✅ **채택 (정합 확인, PC-5 확장).** 1118/1121 = 354/356/359 의 RESOLVED 미러. auto-reject 어휘 유지 시 영향 0 |
| **G-c** | **328 "§3.2" stale ref** | A·patch brief §3.10 | ✅ **재확인.** §3.2(479)="Upstream Silent Breakage", detection 채널=§3.1.2(443) → "§3.2"→"§3.1.2" 정정 정확 |
| **G-d** | 112/178/206/355/356/359 = auto-reject/override 행위명 群 | A | ✅ **(ii) 정합 확인.** 모두 "수정 자동 reject"/"verdict reject" — detection literal 아님, frame 모순 0 |
| **G-e** | 203 "drift detection" / 91 "모순 detection" / 385 "detected" = (iii) 범위 밖 | A·C | ✅ **채택.** commit 식별과 무관 (학습 drift / ADR 모순 / gate bypass event) |

---

## 2. ⭐ 통합 grep 확정 enumeration (Reviewer 직접 전수)

**grep 패턴**: `detection`/`감지`/`provenance` + `auto-reject`/`자동 reject`/`수정 자동` + `author`/`committer`/`단일 author`. **"provenance" = 0 hits 확정.**

### 2.1 (i) 1차 교정 群 — frame 으로 교정 (channel literal + 차단 frame)

| Line | §위치 | 분류 근거 |
|----|----|----|
| **448** | §3.1.2 | "detection" 채널 본체 + "author/committer" 판정 입력 |
| **568** | §3.4 매트릭스 | "Hermes-originated detection" + "git pre-commit" CN-3 frame |
| **328** | §2.6.3(b) | "detection" 2번째 literal + "§3.2"→"§3.1.2" stale ref |
| **457** | §3.1.3 | "pre-commit hook 자동 reject" 차단권 frame |
| **648** | §4.5 | "auto-reject" + "git pre-commit hook + audit log" |
| **784** | §5.5.1 | "단일 author 비교" (SPOF 기준) |
| **360** | §2.6.4 #7 | "author = user 강제" 가정 잔존 (P1) |
| **1122** | §11.4.1 #7 | 360 RESOLVED 미러 (P1 dangling 방지) |
| ⭐ **443** | §3.1.2 헤더 | 섹션 헤더 "(Detection)" — 재명명 시 cascade (G-a) |
| ⭐ **445** | §3.1.2 컬럼 | 컬럼 헤더 "감지 channel" — 재명명 시 cascade (G-a) |

> **10줄 → 12줄** (443/445 헤더 추가). 채널명 재명명(N2'/제3안) 선택 시 448/568/328 + **443/445 헤더** 동기 갱신 필수.

### 2.2 (ii) 정합 확인 群 — auto-reject 행위명 유지 시 영향 0 (frame 모순 검증)

`9 / 112 / 178(#20) / 198 / 203(보조) / 206 / 216 / 221 / 228 / 229 / 230 / 269 / 283 / 310 / 319 / 327 / 341 / 354 / 355 / 356 / 359 / 459 / 726 / 734 / 740 / 751 / 757 / 769 / 783 / 805 / 889 / 1116 / 1118 / 1121` — 모두 "수정 자동 reject"/"verdict reject"/"gate entry reject"/positive author 선례. **detection channel literal 아님.** 발효 단계 (ii) 일관성 재확인 대상. (특히 889 = 457 동형 약한 CN-3 긴장, 354/1116/1118/1121 = 평행 frame)

### 2.3 (iii) 범위 밖 群 — commit 식별과 무관 (오탐)

| Line | 의미 |
|----|----|
| 91 | ADR/SDD 모순 detection |
| 203 | 학습 drift detection (보조) |
| 385 | gate_enforcement_bypass JSONL "detected" |
| 479/569 | Upstream Silent Breakage (§3.2) |
| 485/528 | §3.2.2/§3.3.2 "(Detection)" = **다른 채널** 헤더 |
| 1166 | "자동 검출 hook" = Implementation 영역 (Backlog #6) |

### 2.4 ⭐ enumeration 종료 판정

본 Reviewer grep 으로 **현 시점 잔여 미분류 = 0** 도달 (12 + 정합 群 + 범위 밖 群 전수 분류). **그러나** §4.2 가 *두 번째로* 불완전(443/445 헤더 또 누락)으로 드러난 사실 자체가 정적 열거의 구조적 위험을 *재실증* — 따라서 **확정 enumeration 산출 ≠ 발효 면제.** PC-1 동적 종료 조건 = "발효 단계 재grep 후 잔여 0 *재확인*" 의무는 유지된다 (harness feedforward).

---

## 3. 4 결정 항목 종합

| 항목 | 종합 판정 | 조건 |
|----|----|----|
| **① 최종 문구** | 조건부 (방향 정확) | PC-2 전파(448·648·360·1122·568) + PC-3 ends 1구 + 457 에 ends 1구 부가(경미) |
| **② 범위 종료** | **미충족 → 발효 grep 전수 선결** | PC-1: 443/445 헤더 추가 + 발효 재grep 잔여 0. **본문 즉시 편집 불가** |
| **③ author 어휘** | 채택 (변경 불요) | PC-4: 360/1122 negative 배제 명제 *동시* 갱신 |
| **④ 채널명** | 제3안 "provenance check" *어휘* 권고, **결정 보류** | cascade(448/568/328/443/445) 완결 후 본문 교정 단계 (사용자 명시) |

---

## 4. 판정: APPROVE WITH CONDITIONS

진입 brief 의 진입 적격성(E-1~E-7)·결정 scope·PC 충족 의무 정비는 견고하나, **§4.2 enumeration 이 443/445 섹션·컬럼 헤더를 또 silent 누락**(457→568/328 누락의 *세 번째 구조적 반복*)한 것이 가장 무거운 보강 사항이다.

| 구분 | 조건 | 출처 |
|----|----|----|
| **BLOCKING** | **PC-1** ⭐ 443/445 헤더 enumeration 추가 + 발효 단계 grep 전수 재실행 → 잔여 미분류 0 재확인 (정적 닫힌 목록 금지) | C(G-a) + A(§4.2 불완전) + Reviewer grep |
| **BLOCKING** | **PC-2** CN-4/CN-7/CN-8 의 448·648·360·1122 **+568** 전파 비대칭 해소 | B + A + C |
| **BLOCKING** | **PC-3** enforcement 보장 속성(ends) 1구 명문 (means §6 분리) | A·B + DV2 |
| **BLOCKING** | **PC-4** 360/1122 author 판정 *배제* negative 명제 **동시** 갱신 | B + C |
| **BLOCKING** | observe mode 도입처 정의 (§5.5 미정의 — 신규면 정의 1줄 동반) | B |
| 권고 | PC-5 354/1116/**1118/1121**/221 enumeration 정합 확인 (G-b 평행행 추가) | A·C |
| 권고 | PC-6 line 448 거대 셀 → 요약 + 하단 주석 분리 | C |
| 권고 | PC-7 §5.5.2 수용사유 정합 / §6 환경종속 4행 일관 | B·C |
| 권고 | 889(§6.4) 정합 확인 群 명시 (457 동형 약한 CN-3 긴장) | A |

---

## 5. 경계 — ② enumeration 또 불완전의 함의

**판정: 본문 교정 실 편집 즉시 불가, grep 전수 완주가 선결.** 근거 — (1) 본 Reviewer 가 추론적으로 잔여 0 enumeration 을 산출했으나, §4.2 가 *세 번째*(457, 568/328, 443/445)로 누락을 드러낸 패턴은 "또 다른 미발견 hit 가능성"을 배제 못함; (2) PC-1 은 정적 목록이 아닌 *발효 단계 재grep* 을 종료 조건으로 못박음 (harness feedforward); (3) 채널명 ④ 결정도 cascade(443/445 추가로 또 변동) 완결 의존. 따라서 **본문 반영 한정 합의 → 발효 단계 grep 전수 재실행(잔여 0) → 실 G3 본문 수정 + commit** 순서가 강제되며, 본 합의는 그 어느 것도 발생시키지 않는다.

본 합의 = 추론적 검증(권고) 한정. **G3 본문 실 수정 / 443/445 포함 어떤 줄의 편집 / 채널명 결정(N1/N2'/제3안) / literal 갱신 / 수단 고정 / git hook·ruleset·CI 구현 / ADR·합의 본문 갱신 / commit / push = 모두 0건.** 실 결정/구현 = 사용자 명시 + 별도 단계 (R-I-CONFIG-CHANGE = T3 본문 교정 + Backlog #6 Runtime).

---

## 6. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 발견 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | §4.2 불완전(112/178/206/355/356/359/**1118/1121**) + 328 "§3.2"→"§3.1.2" stale ref + 889 457 동형 + "provenance"=0 + 발효 grep 전수=비협상 의무 |
| **Agent B** (보안 PC충족) | "안전하고 견고한가?" | APPROVE — v2 문구 = PC-1~PC-4 약화 없이 충족 + BLOCKING 4(재grep0/360·1122 동시/C群 전수정합/observe mode 정의) + self-reference CN-3 양립 |
| **Agent C** (채널명/어휘) | "더 나은 방법?" | ⭐ **443 섹션 헤더 + 445 컬럼 헤더 cascade 미포착(4번째 누락)** + 채널명 제3안 "provenance check" + 459/203 enumeration 누락 + author 어휘 유지(465 본문 근거) |
| **Reviewer** | "최선의 합의는?" | 교차(일치 5 / 부분 2 / 불일치 2 / 누락 5) + **G3 전수 grep 직접 재실행**("provenance"=0 / 443·445·1118·1121·328 verbatim / 12줄 1차 + 정합 群 + 범위밖 群 완전 분류) + APPROVE WITH CONDITIONS + BLOCKING 5·권고 4 + ② 본문 즉시 편집 불가(grep 전수 선결) 판정 |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의 보고서의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805/568/328/443/445 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경) / **4 결정 항목 발효** (최종 문구 / 범위 종료 / author 어휘 / 채널명 N1·N2'·제3안 선택 / literal 갱신) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run / workflow_dispatch / paths 필터) / **Hermes runtime·upstream 변경** / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 / threshold 고정 / MVP-1 exit / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·#6 자동 진입 / tmux 멀티 에이전트 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / commit·push 외 자동 다음 단계 진입 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
