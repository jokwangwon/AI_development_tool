# G3 본문 교정 *발효 단계* 진입 정비 brief (DRAFT v1)

> **본 brief = G3 본문 교정 *발효 단계(실 G3 편집)* 진입 *직전* 정비 한정.** 본 brief 의 어떤 §도 그 자체로 G3 본문 실제 수정 / 채널명 *결정* / literal 갱신 / git hook / ruleset / CI / commit / push 를 발생시키지 않는다. 본 brief = **확정 enumeration 정착 + 12줄 final 문구 정비 + 채널명 cascade 계획 + grep 전수 재실행 gate + 실 편집 시퀀스 정의** — 실 변경 0건. staged cycle: **정비 brief → 승인 → (채널명 결정) → grep 전수 재실행(잔여 0) → 실 G3 편집 + commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v1** (발효 단계 진입 정비 — 본문 미수정, 실 편집 미진입)
**진입 단위**: G3 결함 교정 후속 #3 (`ede4943` 본문 반영 한정 합의 §5 "본문 실 편집 즉시 불가, grep 전수 완주 선결" → 본 brief = 그 grep 완주 + final 문구 정비)
**선행 발효 답습**: `ede4943` 본문 반영 한정 합의 (APPROVE WITH CONDITIONS, BLOCKING 5 + 권고 4, 확정 enumeration §2) + `e8e47de` patch brief v2 (§3 문구안) + `92cc9f3` (PC-1~PC-7) + `141bbc9` (CN-1~CN-10)
**답습 입력 (1차 권위)**: **`ede4943` 합의 §2 통합 grep 확정 enumeration + §3 4 결정 항목 + §4 BLOCKING 5/권고 4** + patch brief v2 §3 final 문구안 + G3 원문
**합의 권위 한계**: 본 brief = 발효 *직전 정비* DRAFT — 실 G3 편집·채널명 결정·literal 갱신 *발효* 는 사용자 명시(채널명) + grep 전수 재실행(잔여 0) + 실 편집 commit 의 권한이다 (R-I-CONFIG-CHANGE = T3).

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "(가) 먼저 진행하고, 그 다음 (다)로 이어가겠습니다." — (다) = "본문 교정 발효 단계 진입 정비 brief (grep 전수 완주 절차 + 12줄 1차 교정 + 채널명 cascade 확정 — 실 편집 직전 정비)".

본 brief = 위 (다) 답습 — **grep 전수 완주 결과 정착 + 12줄 final 문구 정비 + 채널명 cascade 계획 + 발효 gate/시퀀스 정의** + **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 선행 답습 (`ede4943` 합의 §2 확정 enumeration) (§1)
2. ⭐ grep 전수 완주 결과 정착 (확정 enumeration + 발효 시 재grep gate) (§2)
3. 12줄 1차 교정 final 문구 정비 (line별, PC-1~PC-4 + observe mode + 457 ends 반영) (§3)
4. 채널명 cascade 계획 (제3안 vs N1, ⭐ 443/445 generic 헤더 nuance) (§4)
5. 정합 群 처리 계획 (auto-reject 행위명 유지 + 정합 확인 목록) (§5)
6. 발효 BLOCKING checklist (PC-1~PC-5 + observe mode) (§6)
7. Exit Criteria + 실 편집 시퀀스 (§7)
8. 다음 단계 (§8)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

- ❌ **G3 본문 실제 수정** (line 448/784/457/648/360/1122/568/328/443/445 및 어떤 줄도 — 본 brief = 정비, 실 편집은 승인 후 별도 단계)
- ❌ **채널명 *결정*** (제3안/N1/N2' 선택 = 사용자 명시) / **literal 갱신**
- ❌ git hook / GitHub ruleset / CI workflow / Hermes runtime·upstream 변경
- ❌ Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F)
- ❌ 수단 결정 고정 (CN-6) / threshold 고정 (CN-9)
- ❌ MVP-1 exit / Phase α defer-lockdown 변경 / ADR·합의 본문 자동 갱신
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ tmux 도입 결정·구현 / 외부 LLM 추가 호출
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. §3 final 문구·§4 cascade 계획은 *정비/권고* 이며, 실 편집 *발효* 는 (i) 채널명 사용자 결정, (ii) grep 전수 재실행 잔여 0, (iii) PC-1~PC-5+observe BLOCKING 충족, (iv) 사용자 명시 commit 의 권한이다.

---

## 1. 선행 답습 (`ede4943` 합의 §2/§3/§4/§5)

- **판정**: APPROVE WITH CONDITIONS. 4 결정 항목 中 ①③ 결정·④ 어휘 권고(제3안 "provenance check", 결정 보류)·② 미충족.
- **§5 핵심**: 본문 실 편집 즉시 불가 → **grep 전수 완주(잔여 미분류 0)가 선결**. enumeration 이 *세 번째*(457→568/328→443/445)로 누락 드러남 = PC-1 동적 종료 조건 정당.
- **BLOCKING 5** (PC-1 grep 전수 / PC-2 전파 / PC-3 ends / PC-4 360·1122 동시 / observe mode 정의) + **권고 4** (PC-5/PC-6/PC-7/889).

---

## 2. ⭐ grep 전수 완주 결과 정착 (확정 enumeration + 발효 재grep gate)

> `ede4943` §2 Reviewer 전수 grep 결과 답습 + 본 brief 재확인. **"provenance" = 0 hits.** 본 §2 = *현 시점* 확정 분류이며, **발효 단계(실 편집)는 이 grep 을 *재실행* 하여 잔여 미분류 0 을 재확인해야 한다 (PC-1 — 정적 닫힌 목록 금지).**

### 2.1 (i) 1차 교정 群 (12줄)

| Line | §위치 | 교정 성격 |
|----|----|----|
| 448 | §3.1.2 | detection 채널 본체 + author/committer 판정 입력 |
| 568 | §3.4 매트릭스 | "Hermes-originated detection" + git pre-commit frame |
| 328 | §2.6.3(b) | "detection" 2번째 literal + "§3.2"→"§3.1.2" stale ref |
| 457 | §3.1.3 | pre-commit hook 차단권 frame |
| 648 | §4.5 | auto-reject + git pre-commit hook + audit log |
| 784 | §5.5.1 | "단일 author 비교" SPOF 기준 |
| 360 | §2.6.4 #7 | "author = user 강제" 가정 잔존 |
| 1122 | §11.4.1 #7 | 360 RESOLVED 미러 (동시 갱신) |
| **443** | §3.1.2 헤더 | 섹션 헤더 "(Detection)" — **⭐ §4 nuance 참조** |
| **445** | §3.1.2 컬럼 | 컬럼 헤더 "감지 channel" — **⭐ §4 nuance 참조** |

### 2.2 (ii) 정합 확인 群 (auto-reject 행위명 유지 시 영향 0)

`9 / 112 / 178 / 198 / 206 / 216 / 221 / 228 / 229 / 230 / 269 / 283 / 310 / 319 / 327 / 341 / 354 / 355 / 356 / 359 / 459 / 726 / 734 / 740 / 751 / 757 / 769 / 783 / 805 / 889 / 1116 / 1118 / 1121` — 발효 단계 (ii) 일관성 재확인 (§5).

### 2.3 (iii) 범위 밖 群 (오탐)

`91 (ADR/SDD 모순) / 203 (학습 drift) / 385 (gate bypass JSONL) / 479·569 (§3.2 upstream) / 485·528 (§3.2.2/§3.3.2 = 다른 채널) / 1166 (Implementation hook)`.

### 2.4 발효 재grep gate (PC-1)

```
실 편집 직전:
  grep -n "detection|감지|provenance" + "auto-reject|자동 reject|수정 자동" + "author|committer|단일 author"
  → 각 hit 를 (i)/(ii)/(iii) 분류, 본 §2 와 대조, 신규/변동 hit 0 확인
  → 잔여 미분류 = 0 도달 시에만 편집 발효 (X-2 Exit)
```

---

## 3. 12줄 1차 교정 — final 문구 정비

> final 문구 = patch brief v2 §3 (`e8e47de`) 안 + `ede4943` BLOCKING 반영. **본 §3 = 정비(권고) — 실 편집 0건.** 8 commit-채널 줄(448/784/457/648/568/328/360/1122)은 v2 §3.1~§3.10 안 그대로 + 아래 발효 delta. 443/445 = §4 nuance.

### 3.1 발효 delta (v2 §3 대비 추가 반영 — BLOCKING)

| delta | 내용 | 출처 |
|----|----|----|
| **D-1 (PC-2)** | CN-4 "host 밖 최소 1개 *실* anchor(명목 금지)" 가 448·648·**568** 에 / CN-7 audit sink 별개가 448·648 에 / CN-8 author 배제가 448·360·1122 에 — 전수 확인 | `ede4943` PC-2 |
| **D-2 (PC-3)** | enforcement 보장 속성(ends)="push/merge 전 차단 보장" 1구 = 448·568·648 + **457 에도 부가**(B 권고) | `ede4943` PC-3 + 457 ends |
| **D-3 (PC-4)** | 360·1122 "author 판정 입력 아님·audit 사후 대조 전용" negative 명제 **동시** | `ede4943` PC-4 |
| **D-4 (observe mode)** | 784 의 "observe mode" = G3 신규 개념(§5.5 미정의) → **정의 1줄 동반**("observe mode = enforcement 미발효 관찰 기간, FN 통과") | `ede4943` BLOCKING observe |
| **D-5 (PC-6)** | 448 거대 셀 → 메커니즘 요약 셀 + §3.1.2 표 *직후* 하단 주석 분리 (각주 표 직후 배치) | `ede4943` PC-6 + C 미세조정 |

### 3.2 final 문구 참조

- **448 / 784 / 457 / 648 / 568 / 328 / 360 / 1122**: patch brief v2 §3.1 / §3.3 / §3.2 / §3.4 / §3.9 / §3.10 / §3.5 / §3.6 안 + 위 D-1~D-5. (verbatim 현 본문은 v2 §3 에 보존 — 본 brief 중복 미기재)
- **author 어휘 (③ 확정)**: 전 author touch-point = "author/committer 메타 = **판정 입력 아님·audit 사후 대조 전용**" (line 465 "별도 audit JSONL" 본문 근거).

---

## 4. 채널명 cascade 계획 (④ — 결정 pending + ⭐ 443/445 nuance)

> 채널명 *결정* = 사용자 명시 (제3안 "provenance check" = `ede4943` 권고 / N1 유지 / N2'). 본 §4 = 각 분기 cascade 계획 정비.

### 4.1 ⭐ 443/445 generic 헤더 nuance (발효 단계 검토 핵심)

`ede4943` §2.1 이 443/445 를 "(i) 1차 교정 群 — 재명명 시 cascade"로 분류했으나, **본 brief 가 재검토 권고**: §3.1.2 섹션 헤더 "감지 방법 (Detection)"(443) + 컬럼 헤더 "감지 channel"(445)은 **이 절의 4개 채널(CI nightly diff / Hermes-originated / R-5 canary / R-6 actual run)을 *모두* 덮는 generic 헤더**다. "Hermes-originated commit" *한 채널만* "provenance check"로 재명명하는데 generic 헤더까지 바꾸면 **다른 3 채널(CI diff/canary/R-6)을 provenance 로 오염**한다.

| 권고 (발효 단계 사용자 확인) | 처리 |
|----|----|
| **443/445 = 정합 확인만 (무변경)** | generic 헤더 유지 ("감지 방법"은 채널 일반 명칭). 재명명은 448 *셀 내* 채널명 + 328 + 568 한정 |

> 즉 본 brief 권고: **443/445 = (ii) 정합 확인으로 재분류** (rename cascade 대상 아님). 이 권고 채택 시 rename cascade = **448 cell + 328 + 568 (3곳)** 으로 환원 (= `92cc9f3`/patch v2 §4 원래 3곳). 단 *재분류 확정* = 발효 단계 사용자/합의 확인 (본 brief 는 권고).

### 4.2 분기별 cascade

| 채널명 분기 | cascade 대상 | 비용 |
|----|----|----|
| **N1 (detection 유지)** | 없음 | 0줄 |
| **제3안 "provenance check" (`ede4943` 권고)** | 448 cell + 328 + 568 ("detection" literal 3곳). 443/445 = §4.1 권고상 무변경 | 3줄 |
| N2' (provenance sensor) | 동일 3곳 (단 sensor 부작용 — `ede4943` DV2 열위) | 3줄 |

---

## 5. 정합 群 처리 계획 (§2.2 — auto-reject 행위명)

- **행위명 유지** ("Hermes-originated commit auto-reject" = "Hermes commit *이* reject 대상", CN-3 양립) — 전면 reframe 불요 (`ede4943` K4).
- **발효 단계 (ii) 일관성 재확인 대상** (frame 모순 0 확인): 특히 **354/1116/1118/1121** (360/1122 평행 RESOLVED frame — 미정합 시 본문 내부 frame 불일치) + **889** (§6.4 "git pre-commit hook on Hermes-originated commit" = 457 동형 약한 CN-3 긴장, "sensor 신호" 어휘 정합 확인).
- **1166** = Implementation 영역 (Backlog #6) — 본 단계 밖.

---

## 6. 발효 BLOCKING checklist (PC-1~PC-5 + observe)

| # | 발효 전 충족 확인 (BLOCKING) | 검증 방법 |
|----|----|----|
| B-1 (PC-1) | grep 전수 재실행 → 잔여 미분류 0 (§2.4 gate) | 발효 직전 grep |
| B-2 (PC-2) | CN-4/CN-7/CN-8 전파 448·648·360·1122·568 전수 | final 문구 검토 |
| B-3 (PC-3) | enforcement 보장 속성(ends) 명문 448·457·568·648 (means §6 분리) | final 문구 검토 |
| B-4 (PC-4) | 360·1122 author 배제 negative 명제 *동시* | final 문구 검토 |
| B-5 (observe) | observe mode 정의 1줄 동반 (784) | final 문구 검토 |
| 권고 | PC-5(354/1116/1118/1121/221 정합) / PC-6(448 셀 분해) / PC-7(§5.5.2·환경종속) / 889 정합 | final 문구 검토 |

> B-1~B-5 中 1+ 미충족 = 발효 미가능 (BLOCKING). means 본문 고정(CN-6 위반) 발견 시도 발효 차단.

---

## 7. Exit Criteria + 실 편집 시퀀스

### 7.1 Exit Criteria (발효 단계 완료 조건 — `ede4943` X-1~X-6 답습)

X-1 4 결정 항목 결정(채널명 포함) / X-2 grep 전수 잔여 0 / X-3 PC-1~PC-5+observe 충족 / X-4 채널명 재명명 시 cascade(448/328/568) 완료 / X-5 의존 cross-ref 정합(§2.2 #20 / §2.5 #6 / system-identity-prequel / ADR-012) / X-6 실 G3 수정 = 결정과 일치(T3 self-protection: 사용자 명시 commit).

### 7.2 실 편집 시퀀스 (승인 후 — 본 brief 발생 0건)

```
1. 채널명 결정 (사용자: 제3안/N1/N2')
2. grep 전수 재실행 → 잔여 0 확인 (§2.4)
3. 12줄(또는 채널명 무변경 시 10줄) final 문구 적용 — B-1~B-5 충족
4. 의존 cross-ref 정합 확인 (X-5)
5. 실 G3 본문 수정 commit (T3 self-protection, 사용자 명시)
6. push
```

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 |
|----|----|----|
| **(A)** | 본 brief 승인 + **채널명 결정** → 실 편집 시퀀스(§7.2) 진입 (grep 전수 → 12/10줄 수정 → commit) | 실 G3 편집 |
| (B) | 본 brief 일부 수정 → v2 | v2 작성 |
| (C) | 본 brief 승인 → commit *까지만* (편집 보류) | 1 commit |
| (D) | 보류 → 다른 backlog (tmux 도입 / Group I implementation boundary / Backlog #4) | 별도 brief |
| (E) | 세션 종료 | — |

> 본 brief = **정비 brief 단계 한정**. 채널명 결정 / grep 전수 재실행 / 실 G3 편집 / commit / push = 사용자 명시 승인 후 별도 단계. 본문 교정 = **T3 → R-I-CONFIG-CHANGE → Reviewer-only 부적격**.

---

## 9. 한 단락 요약

`ede4943` 본문 반영 한정 합의(APPROVE WITH CONDITIONS — "본문 실 편집 즉시 불가, grep 전수 완주 선결")를 받아, G3 본문 교정 *발효 단계(실 편집)* 진입 *직전* 을 정비하는 brief — (§2) `ede4943` §2 통합 grep 확정 enumeration 정착(1차 교정 12줄[448/784/457/648/568/328/360/1122 + 443/445 헤더] / 정합 群 / 범위밖 群, "provenance"=0) + **발효 단계 grep 전수 *재실행* gate**(PC-1 — 정적 닫힌 목록 금지), (§3) 12줄 final 문구 정비(patch brief v2 §3 안 + 발효 delta D-1~D-5: PC-2 전파·PC-3 ends[457 포함]·PC-4 360·1122 동시·observe mode 정의·PC-6 셀 분해), (§4) ⭐ **443/445 = §3.1.2 generic 헤더(4 채널 전체 덮음)이므로 "provenance check" 재명명 시 함께 바꾸면 다른 채널 오염 → 정합 확인(무변경)으로 재분류 권고**, rename cascade = 448 cell + 328 + 568 (3곳) 환원, (§5) auto-reject 행위명 유지 + 정합 群(특히 354/1116/1118/1121/889) 재확인, (§6) 발효 BLOCKING B-1~B-5 + 권고 checklist, (§7) Exit X-1~X-6 + 실 편집 시퀀스(채널명 결정 → grep 0 → 수정 → commit). 채널명 = 제3안 "provenance check" 권고(사용자 결정). 본 brief 는 결론을 *선취하지 않으며* — 채널명 결정·grep 전수 재실행·실 G3 편집·commit·push 는 모두 사용자 명시 + 별도 단계 — **G3 본문 실제 수정 / 채널명 결정 / literal 갱신 / git hook / GitHub ruleset / CI workflow / Operational Readiness PASS / Hermes PMO 격상 / 수단 고정 / commit / push = 모두 0건** 이다.

---

## 부록 A — 답습 출처

| 출처 | 답습 |
|----|----|
| `3plus1-consensus-2026-05-21-g3-body-correction-stage.md` (`ede4943`) §2/§3/§4/§5 | 확정 enumeration + BLOCKING + 본문 즉시 편집 불가 (§1·§2·§6) |
| `g3-metadata-detection-correction-patch-brief.md` v2 (`e8e47de`) §3/§4 | final 문구안 + 채널명 (§3·§4) |
| `g3-body-correction-stage-entry-brief.md` (`5d4b0d7`) §4/§6 | grep 절차 + Exit (§2·§7) |
| `hermes-not-root-of-trust-runtime.md` grep 전수 (2026-05-21) | §2 enumeration |
| ADR-011 §2.1 (means/ends) | §6 CN-6 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/568/328/443/445 및 §2.2 #20·§2.5·§2.6·§3.1·§3.4·§4.5·§5.5 본문 변경) / **채널명 결정** (제3안/N1/N2' 선택) / **literal 갱신** / **git hook 구현** / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** / **Hermes runtime·upstream 변경** / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 / threshold 고정 / MVP-1 exit / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·#6 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
