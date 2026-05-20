# 3+1 합의 보고서 — G3 line 448/784 metadata-기반 single-author detection 결함 교정

> **본 합의는 추론적 검증(권고) 한정.** 본 합의의 어떤 §도 그 자체로 (i) **G3 (`hermes-not-root-of-trust-runtime.md`) 본문 실제 수정** (line 448/784 및 연동 touch-point detection 메커니즘 교정 / §2.2 #20·§2.5·§2.6·§3.1·§4.5·§5.5 본문 변경), (ii) **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문), (iii) **GitHub ruleset / branch protection 실 변경**, (iv) **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경), (v) **Hermes runtime 변경** / **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR), (vi) **수단 결정 *고정*** (positive allow-list 키 종류·서명 방식·차단 지점 최종 결정), (vii) **threshold 고정** (observe mode 기간 등), (viii) **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**, (ix) MVP-1 exit 발효 / Phase α defer-lockdown 변경, (x) ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012), (xi) Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경, (xii) 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정) / 외부 LLM 추가 자동 호출, (xiii) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

---

**작성일**: 2026-05-20
**합의 형태**: **풀 3+1 (Agent A 구현 / Agent B 보안 / Agent C 대안 + Reviewer)** — 사용자 명시 결정 (brief §5 권고 + B-5 R-I-CONFIG-CHANGE T3 답습)
**판정**: **APPROVE WITH CONDITIONS** (교정 *방향* 승인 + 9 조건. 단 "단순 텍스트 정정"이 아닌 §2.2 #20 판정 기준 변경 = T3 — §5 참조)
**합의 입력**: `docs/phase0/g3-line448-784-metadata-detection-defect-correction-brief.md` (DRAFT v1, commit `afb92de`)
**1차 권위 답습**: Group I 풀 3+1 합의 `f6c6d5a` (B-1~B-6 + framing N1 + G3 결함 *기록*) + G3 line 448/784 원문 + ADR-011 §2.1 means/ends
**외부 입력**: Group I 외부 GPT-5.5 응답 (`2026-05-20-...-response-gpt.md`) = **입력 한정** (강제 채택 0건, 추가 외부 LLM 자동 호출 0건)

---

## 0. 합의 대상 + 결함 정의

### 0.1 대상

G3 `hermes-not-root-of-trust-runtime.md` 의 Hermes-originated commit 식별 메커니즘이 **commit author/committer metadata 비교(single-author detection)** 에 기대고 있는 본문 결함을, **positive allow-list / credential boundary / external enforcement 3축**으로 교정 *가능한지* + 어떤 조건·형태·범위로 교정해야 하는지 판정.

### 0.2 결함 정의 (3 Agent + Reviewer 원문 검증 일치)

| Line | §위치 | 현 본문 (원문) | 결함 |
|----|----|----|----|
| **448** | §3.1.2 감지 channel | "Hermes-originated commit detection \| git commit author / committer + Hermes audit log cross-reference \| every commit" | 식별 = **위조 가능 metadata** 비교 + audit log cross-reference (audit 변조 시 무력) |
| **784** | §5.5.1 SPOF | "Hermes-originated commit auto-reject (§2.2 #20) 의 *기준* 자체가 단일 author 비교" | auto-reject **판정 기준 자체가 단일 author 비교** — 본문이 결함을 *자인* |

**결함의 본질 (만장일치)**: "탐지 정확도 부족"이 아니라 **식별 frame 자체가 권한 경계가 아닌 위조 가능 신호에 묶여 있음**. 1인 single-host 에서 사용자=Hermes 가 동일 author/credential 공유 시 **FN(Hermes 가 사람으로 위장한 commit 통과) > FP(정상 commit 오차단)** 비대칭의 *위험한 쪽*(silent·정책 변조 직결)을 방치. **Agent B 추가 검증**: line 784 가 SPOF "Accepted Risk"로 약점을 *수용*한 채 §2.2 #20 이 그 약한 기준을 *enforcement 권위*로 승격 → **"수용된 약점이 enforcement 권위로 승격된 모순"** 이 결함의 핵심.

---

## 1. 교차 비교 (일치 / 부분 / 불일치 / 누락)

### 1.1 일치 (Consensus — 3 Agent 모두 동의)

| # | 일치 항목 | A | B | C |
|----|----|----|----|----|
| C1 | 결함 = 구조적 frame 문제 (metadata 의존), 단순 정확도 아님 | ✅ | ✅ | ✅ |
| C2 | **3축(positive allow-list / credential boundary / external enforcement) 결합으로 교정 가능** | ✅ | ✅ | ✅ |
| C3 | **single layer 불충분 — 3축 분리 불가 결합** | ✅ | ✅ | ✅ |
| C4 | runtime = sensor / 최종 reject = Hermes 밖 (external enforcement) 가 §4 self-reference 해소 | ✅ | ✅ | ✅ |
| C5 | credential boundary = allow-list 의 *선결 전제* (대체 기준 아님) | ✅ | ✅ | ✅ |
| C6 | **수단(키 종류·차단 지점) 본문 고정 금지** (ADR-011 means/ends + 환경 종속 GHES/SaaS) | ✅ | ✅ | ✅ |
| C7 | 본문 교정 = SDD상 구현(Backlog #6) *선행* 작업으로 유의미 (틀린 frame 명세 구현 방지) | ✅ | ✅ | ✅ |
| C8 | 형태 = **brief §5.3 "본문 반영 한정 합의" 적정 / Reviewer-only 부적격** | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial — 2 동의)

| # | 항목 | 동의 | 이견/보강 |
|----|----|----|----|
| P1 | **line 360/1122 "author = user 강제" 가정 잔존 → 함께 교정 필요** (미교정 시 본문 내부 불일치 + 1122 RESOLVED 표 dangling reference) | A 명시 / C 동의 | B 암묵 (보안 무관) — Reviewer 채택 |
| P2 | **5 BLOCKING 안전 조건** (B-B1~B-B5) | B 명문 / A·C 실질 동의 | A·C 가 정합 표·§6 에서 동일 내용 포착 — Reviewer 채택 |

### 1.3 누락 (Gap — 특정 Agent 단독, Reviewer 중요도 평가)

| # | 단독 발견 | 발견 | Reviewer 판정 |
|----|----|----|----|
| G1 | **⭐ line 457 (§3.1.3 차단표) touch-point 누락** — "pre-commit hook on 정책 파일 — Hermes-originated commit 자동 reject", line 448 detection 과 직결 | C | ✅ **채택** — brief §1.4 touch-point 표 누락. 교정 범위에 추가 |
| G2 | **audit sink integrity = 사실상 4번째 축** — line 448 "audit log cross-reference" 가 detection 절반인데 brief 가 §1.2 각주로 강등 (과소). credential(서명 키 격리)과 별개 = audit 기록 매체 격리 | C 명시 / B 잔존우회 #4 암시 | ✅ **채택 (조건 CN-7)** — Group I B-5 (audit 보존 + 외부 read-only sink) 답습. 3축 → "3축 + audit sink integrity" 명시 |
| G3 | author/committer 메타 "참고 신호 한정" = 모호어 → "**판정 경로 제외 · audit 보조 전용**" 비대칭으로 좁혀 회귀(regression) 통로 차단 | C | ✅ **채택 (조건 CN-8)** — Group I G6 (audit 보조 한정) 답습 |
| G4 | positive allow-list 골격(서명 강제+required check+default-deny) = ruleset 기본 가능, **but 키 fingerprint allow-list 대조 = CI provenance step 구현 필요** (0-구현 아님) | A | ✅ **채택 (정보성)** — 실 구현 = Backlog #6, 본 합의 범위 외이나 기록 |
| G5 | line 230(`signed commit` ADR-012 후보)·805(`GPG signed commit 강제`)는 **이미 positive 서명 방향 명시 = 교정 방향과 충돌 없는 내부 선례.** 결함의 정체 = "G3 가 multi-host/Evidence Ledger 에선 positive 서명을 알면서 single-host commit detection 에서만 metadata 비교에 머문 *비대칭*" | A | ✅ **채택** — 230/805 = 교정 아닌 *정합 참조*. 교정 정당성 강화 |

### 1.4 불일치 (Divergence — Reviewer 판정 필요)

| # | 쟁점 | 입장 | Reviewer 판정 |
|----|----|----|----|
| **D1** | **framing — G3 채널명 "Hermes-originated commit detection" 유지(N1) vs 재명명 "provenance sensor"(N2')** | brief = Group I N1 답습 (명칭 유지) / **C = N2' 우월** (외부 제안 명칭과 G3 채널명은 별개 문제, "signal/sensor"는 *역할* 어휘로 means 고정 아님, perm-by-construction frame·B-2 와 어휘 일치) | **조건부 인정 — 조건 CN-9 (아래 §3)** |
| D2 | 수단 표기 형식 — A "목적/원칙 추상" vs C "목적 + 수단 후보 비표준 열거(결정 보류 명문)" | A 추상 / C 후보 열거 | **양립 — 둘 다 means 고정 0건. C 형식(후보 열거)이 line 805 선례·MVP-1 패턴과 동형으로 추적성 우월 → 조건 CN-6 에 흡수** |

---

## 2. 합의 도출 — 교정 방향 + 조건

### 2.1 교정 방향 (만장일치 — C2/C3/C4/C5)

```
positive allow-list   ─ "무엇을 허용하는가" (default-deny + 사람 권위 신호 positive 검증, metadata spoof 무관)
        ⊕
credential boundary   ─ "allow-list 가 작동하기 위한 *선결 전제*" (사람 키·token·SSH/GPG agent 의 Hermes 환경 격리)
        ⊕
external enforcement  ─ "누가 최종 차단하는가" (runtime=sensor / 최종 reject=Hermes 밖 anchor 최소 1개 실 anchor)
        ⊕
audit sink integrity  ─ (G2 추가) "audit log cross-reference 의 매체 격리" (외부 read-only sink, Hermes 쓰기 불가)
        =
metadata-기반 single-author detection 결함의 구조적 교정
```

### 2.2 조건 (CONDITIONS — 교정 본문 발효 단계 BLOCKING)

| # | 조건 | 출처 |
|----|----|----|
| **CN-1** | **positive allow-list 중심 교정** — line 448/784 의 author 비교를 default-deny + 사람 권위 신호 positive 검증으로 *대체* | C2/C4 만장일치 (B-1) |
| **CN-2** | **credential boundary 를 allow-list 의 *선결 조건* 으로 본문 명시** — "미격리 시 allow-list 는 metadata detection 과 동일 FN 으로 붕괴 + 거짓 안전감 추가 생성" 명문화 | C5 만장일치 + B-B1 (B-3) |
| **CN-3** | **runtime = sensor / audit producer 한정, 최종 reject = Hermes 밖** (ruleset / container ACL / hardware key 中 1+) — §4 self-reference 비유입 | C4 만장일치 + B-B2 (B-2) |
| **CN-4** | **host 밖 anchor 최소 1개 = 실 anchor 의무** (single-host 3-layer 명목화 방지) + detection 기준·차단 설정 변경 = R-I-CONFIG-CHANGE = T3 (Hermes token 미보유, 자기 차단책 무력화 불가) | B-B2 (B-4/B-5) |
| **CN-5** | **`.git/` 직접 변조 = filesystem ACL(§2.5 #1) 책무, commit detection 범위 *밖*** 임을 본문 *필수 1줄*로 명시 (commit layer 만능 오독 방지) | B-B3 + C(C7) (B-6) |
| **CN-6** | **수단(키 종류·서명 방식·차단 지점) 본문 고정 금지** — 목적/원칙 수준 기술. 단 추적성 위해 "수단 *후보* 비표준 열거(결정 = Backlog #6)" 형식 허용 (line 805 선례·MVP-1 패턴 동형, means 고정 0건) | C6 만장일치 + B-B5 + D2 (ADR-011 §2.1 + framing N1) |
| **CN-7** | **audit sink integrity 를 교정 축에 명시** — line 448 "audit log cross-reference" 교정 시 audit log 변조 저항(외부 read-only sink, Hermes 쓰기 불가)을 credential boundary 와 *별개 요소*로 포함 | G2 (B-5 + P2) |
| **CN-8** | **author/committer 메타 = "판정 경로 제외 · audit 보조 전용"** 비대칭으로 명시 (모호어 "참고 신호" 회피 — 회귀 통로 차단) | G3 (Group I G6) |
| **CN-9** | **observe mode = enforcement 발효 아님** (observe 기간 FN 통과 명시) + **FN 우선 > FP** ("의심스러우면 quarantine") 를 *방향성*으로 본문 명시 (구체 기간 = threshold, 별도 단계) | B-B4 (CB-1/P3) |

### 2.3 framing 판정 (D1 — 조건 CN-10)

| # | 조건 | 판정 |
|----|----|----|
| **CN-10** | **framing** — brief 의 Group I N1 무비판 답습은 *over-constraint*. 외부 제안 명칭("Human-authorized T3 change enforcement with credential isolation", 수단=credential isolation 을 명칭 고정 → ADR-011 저촉)과 **G3 채널명 "detection" 은 별개 문제**다. **G3 채널명 재명명 옵션(N2' "provenance sensor" 등 역할 기반)을 *닫지 않는다*** — "signal/sensor"는 *역할* 어휘로 수단(키/차단 지점) 고정이 아니므로 ADR-011 means/ends 저촉 아님 + perm-by-construction frame·CN-3(sensor) 와 어휘 일치. **단 재명명 시 §2.2 #20 등 cross-reference "detection" 인용의 의존 연쇄 갱신을 touch-point 에 포함.** 명칭 *최종 결정* = 본문 교정 단계 (사용자 명시) | C(D1) 인정 / brief N1 *수정* |

> **Reviewer 종합 (D1)**: brief §6 이 Group I framing N1 을 그대로 답습한 것은 *외부 제안 명칭*에 대한 N1 권고를 *G3 내부 채널명* 에까지 무비판 확장한 것이다. C 의 지적이 정확하다 — 외부 명칭은 *수단(credential isolation)을 명칭에 박는* ADR-011 위반이라 보류됐으나, "detection → provenance sensor" 는 *역할 어휘 재명명* 으로 means 고정이 아니며 오히려 CN-3(runtime=sensor) 와 어휘 일치한다. 따라서 채널명 재명명은 **금지가 아니라 본문 교정 단계의 열린 옵션**으로 둔다. 단 ADR-011 정합 핵심(수단 명칭 고정 금지)은 CN-6 으로 유지.

---

## 3. 교정 범위 (touch-point) — 검토만, 실 본문 수정 0건

**Agent A·C 종합 권고 범위 (brief §1.4 + G1 line 457 보완):**

| 구분 | Line | §위치 | 성격 |
|----|----|----|----|
| **1차 교정** | **448** | §3.1.2 감지 channel | detection = author 비교 → positive 검증 + sensor 신호 |
| **1차 교정** | **784** | §5.5.1 SPOF | "단일 author 비교" → 사람 키 allow-list + credential 격리 *전제* |
| **1차 교정 (G1 보완)** | **457** | §3.1.3 차단표 | "pre-commit hook — 자동 reject" → sensor + Hermes 밖 reject |
| **1차 교정** | **648** | §4.5 합의 결과 commit author | "pre-commit hook + audit log" → sensor + 외부 anchor |
| **가정 잔존 교정 (P1)** | **360** | §2.6.4 #7 | "author = user 강제" → 사람 서명 키 allow-list |
| **가정 잔존 교정 (P1)** | **1122** | §11.4 RESOLVED 표 #7 | 360 동기 갱신 (dangling reference 방지) |
| **정합 참조만 (G5)** | **230** | §5.2.4 #11 | 이미 "signed commit (ADR-012 후보)" — 교정 아닌 정합 확인 |
| **정합 참조만 (G5)** | **805** | §5.5.3 multi-host trigger | 이미 "GPG signed commit 강제" — positive 방향 선례, 정합 확인 |

> ⚠️ 본 §3 = 교정 범위 *검토* (실 본문 수정 0건). 어느 줄을 어떤 문구로 교정할지 *결정* = 본문 교정 단계 (사용자 명시 + R-I-CONFIG-CHANGE T3). **G3 본문 실제 수정은 아직 하지 않는다 (요청 항목 #9).** Hermes runtime / hook / ruleset / CI 구현도 아직 하지 않는다 (요청 항목 #10).

---

## 4. ADR-011 means/ends 정합 (요청 항목 #7)

교정 본문은 **목적(ends)** 수준으로 기술한다: "식별 = metadata 판별이 아닌 사람 권위 신호 positive 검증" / "최종 차단 = Hermes 밖" / "credential 격리 = 전제" / "audit sink = 변조 저항". **구체 수단(키 종류·서명 방식·차단 지점)은 본문 고정하지 않으며**(CN-6), 추적성을 위해 수단 *후보 열거*(결정 = Backlog #6)는 허용한다. 이는 ADR-011 §2.1 수단/목적 분리 + Group I framing N1(수단 명칭 고정 보류) + Provider Liquidity 정합. Agent A·B·C 만장일치(C6).

---

## 5. 결정 vs 설계 vs 구현 경계

| 계층 | 본 합의 산출 | 발효 권한 |
|----|----|----|
| **합의 권고 (본 보고서)** | 교정 방향(3축+audit) 승인 / 9+1 조건(CN-1~CN-10) / 교정 범위(touch-point) / framing 재명명 옵션 개방 | Reviewer 종합 (추론적 검증) — **발효 아님** |
| **본문 교정 결정 (DESIGN)** | line 448/784/457/648/360/1122 *문구* / 채널명 / 수단 후보 표기 *결정* | **사용자 명시 + 본문 교정 단계** (R-I-CONFIG-CHANGE = T3) — 본 합의 권고 기반 |
| **구현 (IMPLEMENTATION)** | 실 hook / ruleset / CI provenance / filesystem ACL / credential 격리 / audit sink 본문 | **Backlog #6 Runtime + CI-hook + 별도 풀 3+1 (R-I-IMPL-BOUNDARY)** |

- 현 상태: **G3 DESIGN PASS / IMPLEMENTATION PENDING**.
- **본 교정 = "단순 텍스트 정정"이 아님** — Agent A·B 일치: §2.2 #20 auto-reject 의 *판정 기준* 변경 (metadata → positive allow-list) = 새 설계 결정 요소 잔존 → **T3, Reviewer-only 부적격**. 따라서 판정을 "APPROVE AS TEXTUAL CORRECTION"이 아닌 **APPROVE WITH CONDITIONS (T3)** 로 한다.
- 단 식별 frame 은 Group I `f6c6d5a` 에서 *이미* 만장일치 확정 → 본문 교정 단계의 *새 결정 잔여* = (i) 본문 문구, (ii) touch-point 범위(§3), (iii) author 메타 어휘(CN-8), (iv) 채널명(CN-10) 4건에 한정. **형태 권고: brief §5.3 "본문 반영 한정 합의" + 위 4 결정 항목에 scope 명문 고정** (Agent C 권고 — 풀 3+1 재실행의 frame 재투표 중복 제거, B-5 T3 다관점 유지).

---

## 6. 외부 응답 처리

Group I 외부 GPT-5.5 응답 = **입력 한정** (강제 채택 0건). 본 합의는 그 5 보강점(positive allow-list / GHES≠GitHub.com / runtime=sensor / FP통제 / `.git` ACL+negative-control)을 *입력*으로 답습했을 뿐, 교정 방향·조건·framing *결정* 은 풀 3+1 Agent A/B/C 독립 평가 + Reviewer 종합 + 사용자 명시 권한이다. **추가 외부 LLM 자동 호출 0건.** 2차 vendor(Gemini 등) 입력 = 사용자 결정 영역 (의무 아님 — trigger #7 기 충족).

---

## 7. 미해소 쟁점 / 후속 (사용자 결정 영역 — 자동 진입 0건)

1. **G3 본문 교정 *문구* 확정 + 실 수정** — 본 합의는 방향·조건·범위 권고만. 실 수정 = 별도 본문 교정 단계 (R-I-CONFIG-CHANGE = T3, 사용자 명시 + §5.3 축소 합의 또는 풀 3+1).
2. **채널명 재명명 (CN-10 D1)** — "detection" 유지 vs "provenance sensor" 재명명. 본문 교정 단계 결정.
3. **audit sink integrity 구현** (CN-7) — 외부 read-only sink 실 구성 = Backlog #6.
4. **positive allow-list 키 fingerprint 대조 CI step** (G4) — 0-구현 아님, Backlog #6 구현.
5. **observe mode 기간 / threshold** (CN-9 구체 수치) — threshold 고정 영역 (별도 단계).
6. **credential boundary / external enforcement anchor 실 구성** — Implementation/Runtime PASS (Backlog #6).

---

## 8. 합의 한 문단 요약

**G3 line 448/784 의 metadata-기반 single-author detection 은 HIGH 심각도의 구조적 결함이며**(1인 single-host 에서 사용자=Hermes 동일 author/credential 공유 시 의도적 사람 위장 commit 을 못 막아 FN > FP 비대칭의 위험한 쪽을 방치 — line 784 가 약점을 *자인*한 채 §2.2 #20 enforcement 권위로 승격된 모순), **positive allow-list / credential boundary / external enforcement 3축 + audit sink integrity 결합으로 교정 가능**하다는 것이 Agent A(구현)·B(보안)·C(대안) 만장일치 + Reviewer 종합이다. 판정 = **APPROVE WITH CONDITIONS** — 단 Agent A·B 가 일치 지적하듯 본 교정은 "단순 텍스트 정정"이 아니라 §2.2 #20 auto-reject 의 *판정 기준 변경* = T3(R-I-CONFIG-CHANGE)이므로 Reviewer-only 부적격이며, 식별 frame 이 Group I `f6c6d5a` 에서 이미 만장일치 확정인 점을 들어 형태는 **brief §5.3 "본문 반영 한정 합의 + 4 결정 항목(문구·범위·author 어휘·채널명) scope 명문 고정"** 을 권고한다(풀 3+1 frame 재투표 중복 제거). 9+1 조건 = CN-1(positive allow-list 중심) / CN-2(credential boundary = allow-list 선결 조건 본문 명시 — 누락 시 metadata 보다 위험한 거짓 안전감) / CN-3(runtime=sensor·audit producer, 최종 reject=Hermes 밖) / CN-4(host 밖 anchor 실 anchor 의무 + detection 설정 변경=R-I-CONFIG-CHANGE T3) / CN-5(`.git/`=filesystem ACL 책무, commit detection 범위 밖 본문 명시) / CN-6(수단 본문 고정 금지 — 후보 열거는 허용) / CN-7(audit sink integrity = line 448 'audit log cross-reference' 교정 시 외부 read-only sink 별개 요소 포함) / CN-8(author 메타 = '판정 경로 제외·audit 보조 전용' 비대칭) / CN-9(observe ≠ 발효·FN 우선 방향성) / CN-10(framing — G3 채널명 재명명 옵션 개방, 'detection→provenance sensor'는 역할 어휘로 means 고정 아님). 교차 발견 중 무게 있는 것은 **Agent C 가 brief touch-point 표에서 누락된 line 457(§3.1.3 차단표)을 발견**하고 **audit sink integrity 를 사실상 4번째 축으로 격상**한 것, 그리고 **Agent A 가 line 230/805 가 이미 positive 서명 방향을 명시한 내부 선례임을 짚어 "G3 가 multi-host 에선 positive 서명을 알면서 single-host commit detection 에서만 metadata 비교에 머문 비대칭"이 결함의 정체임을 규명**한 것이다. 교정 범위 = 1차 4줄(448/784/457/648) + 가정 잔존 교정 2줄(360/1122, 미교정 시 본문 내부 불일치 + 1122 RESOLVED dangling) + 정합 참조만 2줄(230/805). ADR-011 means/ends 정합 = 목적/원칙 수준 기술 + 수단 본문 고정 금지(후보 열거 허용) 유지. 본 합의는 추론적 검증(권고) 한정 — **G3 본문 실제 수정·git hook 구현·GitHub ruleset 변경·CI workflow 변경·Hermes runtime 변경·Hermes upstream 변경·Operational Readiness PASS·Hermes PMO 격상·수단 결정 고정·threshold 고정·commit·push 외 코드/문서 본문 변경 = 모두 0건**이며, 실 *결정/구현* 은 사용자 명시 + 별도 단계(본문 교정 + Backlog #6 Runtime + CI-hook)이다.

---

## 9. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 발견 |
|----|----|----|
| **Agent A** (구현) | "실제로 동작하는가?" | 7 touch-point 정합 가능 + line 230/805 = positive 선례(비대칭이 결함 정체) + **448/784만 고치면 360/1122 가정 잔존 → 본문 내부 불일치** + positive allow-list 골격=ruleset 기본 가능/키 fingerprint 대조=CI 구현 필요 + runtime=sensor 타당(GHES vs SaaS 환경 종속→원칙 추상화) + 본문 교정=SDD 선행으로 유의미. 형태=§5.3/Reviewer-only 부적격 |
| **Agent B** (보안) | "안전하고 견고한가?" | HIGH 구조적 결함(수용된 약점→enforcement 권위 승격 모순) + 3축 분리 불가(한 축 본문 누락 시 metadata 보다 위험한 false sense of security) + **5 BLOCKING(B-B1 credential 본문 명시 / B-B2 self-reference 비유입 / B-B3 `.git/` 경계 / B-B4 FN 우선·observe≠발효 / B-B5 means/ends)** + T3 풀 3+1 의무/Reviewer-only 부적격 |
| **Agent C** (대안) | "더 나은 방법이 있는가?" | 3축=perm-by-construction 충분히 근본적이나 **"3축+audit sink integrity 4요소"가 더 정확**(line 448 audit cross-reference 직결) + **line 457 누락 발견** + 범위=(다) 1차4+가정2+참조2 + **framing N2'(채널명 'provenance sensor' 재명명) 우월**(역할 어휘=means 고정 아님) + 수단 "후보 열거" 형식(line 805 선례) + author 메타 "참고 신호"→"audit 보조 전용" 비대칭 |
| **Reviewer** | "최선의 합의는?" | 교차 비교(일치 8 / 부분 2 / 누락 5 / 불일치 2) + APPROVE WITH CONDITIONS(T3) + 9+1 조건 + 교정 범위 + framing 재명명 옵션 개방(D1 brief N1 무비판 답습 *수정*) + 실 결정/구현 = 사용자 명시 + 별도 단계 분리 |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의 보고서의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**G3 본문 실제 수정** (line 448/784/457/648/360/1122/230/805 및 §2.2 #20·§2.5·§2.6·§3.1·§4.5·§5.5 본문 변경) / **git hook 구현** (pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경) / **Hermes runtime 변경** / **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / 수단 결정 고정 (positive allow-list 키 종류·서명 방식·차단 지점) / threshold 고정 (observe mode 기간) / credential boundary 실분리 구현 / external enforcement anchor 실 구성 / audit sink 실 구성 / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / ADR 본문 자동 갱신 (ADR-008/011/012) / Group I·α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / 교정 범위·형태·framing *결정 발효* (권고 한정 — 발효는 본문 교정 단계 + 사용자 결정) / Backlog #4·#6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
