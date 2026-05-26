# 3+1 합의 보고서 — Agent 권한 상승(sudo/root) 처리 정책 brief

> **본 합의 = 추론적 검증(권고) 한정.** 본 합의는 **agent 권한 처리 정책 brief(`agent-privilege-escalation-policy-brief.md`)의 정합·안전·대안 검증 + 발효 전 BLOCKING 통합** 만 다룬다. **정책 *채택·고정* / sudoers·broker·sidecar 실 구현 / `settings.json` 변경 / credential 수단 재결정 / S-0+S-2 발효 / sigstore·gitsign·Rekor 도입 / Operational Readiness PASS / Hermes PMO 격상 / commit·push = 모두 0건.** 실 채택/구현 = 사용자 명시 + 별도 단계.

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — **의무** (harness 아키텍처 + 보안 정책 + 핵심 제약 #1[agent≠root] 직결)
**합의 입력**: `docs/phase0/agent-privilege-escalation-policy-brief.md` (DRAFT v1)
**1차 권위 답습**: ADR-011 §2.1 means/ends + Hermes ≠ root / `harness-engineering-design.md` (가이드 vs 센서, Layer 0~6) / `ead5754` BI-3 (CD-3·CD-5·CD-8) / credential 수단 발효 합의 (H-1·H-2·CMA-2·CMA-3·CMA-5·CMA-6·CMA-7) / R-I-CONFIG-CHANGE T3 / [[project_minimize_user_intervention]] / [[feedback_provider_liquidity]]
**판정**: **APPROVE WITH CONDITIONS** — brief = *설계 정리* 단계로서 범위(권고 한정·실 변경 0건) 준수, R/P/T 분류 + (2) 형량 골격 유효, citation stale 0. 단 **정책 *채택* 전 BLOCKING 6(AP-1~6) 해소 필요**. ⭐ **핵심 = 정적 R/P/T 분류로는 부족 — (a) T-경계를 default-T 구조로 (b) broker 강제 메커니즘 명세 (c) *시간 차원*(capability lease) + drift 단방향 ratchet 추가.** **BLOCKING 6(AP-1~6) + 권고 9.**

---

## 0. 종합 판정 (한 문단)

세 Agent 는 모두 **APPROVE WITH CONDITIONS** 로 수렴했고, (1) brief 의 범위 규율(실 변경 0건·정책 고정 0건)과 핵심 긴장(G⊥S) 명문화가 견고, (2) **R/P/T 작업 분류 + (2) 형량 골격은 유효하나 *정적 분류*가 공통 약점**, (3) **citation stale 0**(CP-10 메타 답습 효과 지속 — BI-3 N-2→BI-4→BI-5 3연속 stale 단절이 본 brief 에서도 유지), (4) **거짓 안전감 차단이 "binary" 를 *언급*하나 강제 메커니즘 부족** 에 일치했다. 가장 무게 있는 발견은 **Agent B·C 가 서로 다른 입구로 "정적 분류의 한계"에 수렴**한 점이다 — Agent B 는 "(2) 형량이 *drift 엔진*: 운영 중 편의를 위해 T→R 미끄러짐 = H-1 재현 → 분류 *단방향 ratchet* 필요", Agent C 는 "형량의 빠진 차원 = *시간(TTL/lease)*: 1회 authorization → 짧은 TTL capability → 윈도우 내 자동 = §4(4) '마찰은 횟수에, 존재엔 미적용' 원칙의 *유일한 실현 메커니즘*". 둘을 결합하면 **정적 분류 위에 (시간 차원 lease + 단방향 ratchet + drift Rollback Trigger)** 가 형량을 안전하게 동적화한다. 두 번째 무게 발견은 **Agent A·B 가 "broker/게이트 강제 메커니즘 미명세"에 수렴**(A = argv 정확매칭·`SO_PEERCRED` IPC 인증·canonical path·TOCTOU / B = broker 위협 4항목[IPC 인증·요청 위조·TOCTOU·상시 특권 표면]) — "결정적 게이트"가 *원칙 선언*에 그쳐 CD-5 binary(라벨 ≠ 입증)와 충돌. 세 번째는 **Agent A·B 수렴 "T-경계 목록의 *정적 enumeration* 이 위협 모델과 모순"** — brief §2 자신이 "목록 완전성이 안전을 좌우, 누락=silent 권한 상승"이라 경고하면서 패키지/공급망·`.git/`·CI yaml·env/secret·egress 를 빠뜨림 → **"닫힌 enumeration"→"default-T(미분류=보수적 T)" 구조 전환**. Agent C 단독으로 **harness 4축 일반 원칙화**(R/P/T+lease 가 allow-list·anchor·audit 전체 재사용)와 **PL = broker 인터페이스/구현 분리**(축 간 교훈 비전파 = `ead5754` CD-8 의 broker 축 미적용 = CP-10 재발)를 격상했다. 본 합의 = **추론적 검증(권고) 한정 — 정책 채택·구현·credential 재결정 = 사용자 명시 + 별도 단계.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|----------|---|---|---|
| C1 | **판정 = APPROVE WITH CONDITIONS** (설계 정리 적격, 채택 전 조건) | ✅ | ✅ | ✅ |
| C2 | **R/P/T 분류 + (2) 형량 골격 유효** — 단 *정적 분류*가 공통 약점 | ✅ (A-2) | ✅ (B-5) | ✅ (C-1) |
| C3 | **citation stale 0** (ADR-011·harness-design·CD-3/5·CMA-* 전수 실재, CP-10 답습 효과) | ✅ (전수) | ✅ (전수) | ✅ (정합) |
| C4 | **거짓 안전감 차단이 binary *언급*뿐 — 강제 메커니즘 부족** | ✅ (A-1) | ✅ (B-4) | ✅ (C-3 추론적 판정) |
| C5 | **agent 일반 sudo 미부여 = 불변**(H-1 hole 금지), broker 는 좁고 결정적 | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial — 2 동의, 1 강조/추가)

| # | 항목 | 분류 |
|---|------|------|
| P1 ⭐ | **정적 분류 → 동적 차원** = drift 단방향 ratchet(B) + 시간 lease(C) | **B 강하게(B-5 drift 엔진) + C 강하게(C-1 시간 차원)** 독립 수렴 / A(A-2 모호 경계로 정합) |
| P2 ⭐ | **broker/게이트 강제 메커니즘** = argv·IPC 인증·TOCTOU(A) + broker 위협 4(B) | **A 강하게(A-1) + B 강하게(B-3)** 수렴(서로 다른 입구, 동일 IPC 인증·TOCTOU) |
| P3 ⭐ | **T-경계 목록 → default-T 구조** + 누락 5건 | **B 강하게(B-1) + A(A-2 모호 경계)** 수렴 |
| P4 | **credential fork §5 단정 약화** = 비서명 공백(B) + 대안 확장(C) | B(B-6 보안 공백) + C(C-3 batch/cached presence 대안) — 방향 보완 |

### 1.3 불일치 (Divergence)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 | **§5 서명 빈도 축소의 위상** | (미언급) | "비서명 commit 빈도 축소 = *S 일부 양보*"(보수, B-6) | "batch/cached presence 로 G+S 양립 *가능*"(적극, C-3) | **진정 충돌 아닌 *보완* — 둘 다 "빈도 축소 = G+S 양립" *단정* 을 빼라는 데 동의**. B = 비서명 구간 보안 공백(BI-1 판정 부재·merge≠provenance·CMA-2 건당 의도 희석) *명시*, C = CMA-2(자동서명 차단) *유지하며* 마찰↓ 대안(batch·짧은 TTL cached presence·계산적 자동) *병치*. → **AP-6 = "단정 약화(B 위험 명시) + 대안 확장(C 병치)" 통합**. cached presence TTL = 형량 변수(C), 비서명 구간 = BI-1 판정 공백(B) 둘 다 반영 |

### 1.4 누락 (Gap — 단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-C1 ⭐ | **capability 토큰 lease = 시간 차원** (1회 authorization→짧은 TTL→윈도우 내 자동, 사람 존재 유지·횟수↓) — §4(4) 원칙의 *유일 실현 메커니즘*. C-1(형량)·C-2 H(패턴)·C-3(credential cached presence) 관통 단일 축 | C | **높음** | **AP-3** (B-5 와 통합) |
| N-B1 ⭐ | **allow-list 항목 *escape-equivalence*** — `apt install`(공급망)·`tee`·`systemctl`·`cp/install`(SUID) = 정확 매칭이어도 root-동치 확장. 항목 *semantics* 도 T3 검토 | B | **높음** | **AP-4** |
| N-C2 ⭐ | **harness 4축 일반 원칙화** — R/P/T+lease 가 allow-list·anchor·audit 전체 재사용. P-PRIV 가 credential 한정인지 4축 일반인지 = 합의 결정 항목 | C | **높음** | 권고 AR-5 (§7 격상) |
| N-C3 | **설계 공간 확장** = 실행 격리 패턴 E(rootless+userns)/F(gVisor·Kata)/G(ephemeral VM per task)/H(lease) — §3 A/B/C/D 가 sudoers/broker 축에 갇힘 | C | 중-높음 | 권고 AR-1 |
| N-C4 | **PL = broker 인터페이스/구현 분리** (sudoers/systemd vs 클라우드 IAM lock-in). CD-8/R-4 의 broker 축 *미적용* = CP-10 재발 | C | 중-높음 | 권고 AR-6 |
| N-A1 | **패턴 B = 기존 r2-poc/gp3-st3 PoC 일반화** (cap_drop ALL·user 1000:1000·socket 미마운트·network none = 이미 검증) — 신규 설계 아님 | A | 중-높음 | 권고 AR-2 |
| N-A2 | **systemd unit + Polkit = sudoers 보다 좁은 표면 대안** (argv 미노출, shell-escape 우회) | A | 중 | 권고 AR-3 |
| N-A3 | **재귀 종료 닻** = allow-list 파일 root:root, agent 쓰기 미보유 = 회귀 1단계 멈춤 *구현 속성*으로 명문 | A | 중-높음 | 권고 AR-4 |
| N-B2 | broker = sudoers 대비 *순이득*인지 = broker 표면 < allow-list 표면일 때만 (형량 산식 반영) | B | 중 | AP-2 통합 |
| N-B3 | P-provision artifact = 사람 *검토 후* 실행, 에이전트 생성 artifact 무비판 실행 금지 | B | 중 | 권고 AR-9 |

---

## 2. 합의 도출 — 발효 전 BLOCKING 통합 (AP-1~6)

> 세 Agent BLOCKING(A 2 + B 6 + C 3 = 11) 중복 제거 + Reviewer 격상 = **6건**. **우선순위: AP-1(default-T 구조) > AP-3(동적 차원=lease+ratchet) > AP-2(broker 강제) > AP-5(거짓 안전감 §) > AP-4(escape-equivalence) > AP-6(credential fork).**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **AP-1** ⭐ | **T-경계 목록 = "닫힌 enumeration" → "default-T(미분류=보수적 T, default-deny)" *구조*로 전환** + 명시 누락 5건 추가(**패키지/공급망·`.git/` 변조·CI workflow yaml·env/secret·네트워크 egress**) + R/P/T 매핑 예시(서명=T·push=R 분해 / docker run = H-1 미해소 시 T-등가 / 패키지 system=P·프로젝트 의존성=R). brief §2 자기경고("누락=silent 권한 상승")의 *자기충족* | P3 (B-1 + A-2 수렴) | **1** |
| **AP-2** ⭐ | **broker/게이트 강제 메커니즘 명세** — 결정적 게이트 4속성: (a) **고정 argv 정확 매칭**(wildcard·shell metachar 금지) (b) **IPC = `SO_PEERCRED` uid 인증 + 호출자 화이트리스트** (c) **canonical path + 정적 enum** (d) **TOCTOU 방지(fd 기반)** + broker 위협 4(IPC 인증·요청 위조·TOCTOU·상시 특권 표면). "broker 순이득 = broker 표면 < allow-list 표면일 때만". CD-5 binary(적대적 시연으로만 입증) 연결 | P2 (A-1 + B-3 수렴, N-B2) | **1** |
| **AP-3** ⭐ | **정적 분류 → 동적 차원 추가** = (a) **분류 단방향 ratchet**(R→T 승격 자유 / T→R 강등 = T3 사람 + 적대적 재시연) + drift 능동 감지(Rollback Trigger) (b) **2축 grid(폭발반경×빈도) + capability 토큰 lease**(1회 authorization→짧은 TTL→윈도우 내 동종 자동 = 사람 *존재* 유지·*횟수* ↓ = §4(4) 원칙의 실현 메커니즘). ⚠️ TTL = 형량 변수(host 침해 기회 윈도우) | P1 (B-5 + N-C1 통합) | **1** |
| **AP-4** | **allow-list 항목 escape-equivalence 분석 의무** — 명령이 임의 파일 쓰기·임의 패키지(공급망)·SUID·셸 우회로 root-동치 확장되는가. 항목 *추가*뿐 아니라 *semantics* 도 T3 사람 검토 | N-B1 (B 단독) | 2 |
| **AP-5** | **거짓 안전감 차단 = 별도 §** — 적대적 시연 종료조건: ① 에이전트가 broker/sudoers 우회해 임의 root 실행 *실패* ② allow-list 항목 escape *실패* ③ 미분류 sudo 요구 = 자동 거부. + **CMA-7 동형 부분 적용 면책 라벨**(정책 일부만 깔린 중간 상태 = "보장 0") + owner 경로(같은 사람 정책 변경) 잔존 | B-4 (B 단독) | 2 |
| **AP-6** | **credential fork §5 = 단정 약화 + 대안 확장** — "비서명 commit 빈도 축소 = G+S 양립" 단정 → (i) 보안 공백 명시(비서명 commit = 에이전트 자유 생성·**BI-1 fingerprint 판정 입력 부재**·merge 가 각 commit provenance 미보증·**CMA-2 "건당 의도 확인" 희석**) (ii) CMA-2(자동서명 차단) *유지하며* 마찰↓ 대안 병치(**batch 서명**[N commit 1 터치]·**FIDO2 cached presence**[짧은 TTL=형량 변수]·**정책 기반 자동**[계산적 판정만, 화이트리스트=T 재귀보호]) (iii) keyless 이중 부담(gitsign 도 OIDC 토큰 격리 필요 → CP-4 안 닫음, "Sigstore=credential 해결" 거짓 안전감 차단) | P4/D1 (B-6 + C-3 통합) | 3 |

---

## 3. 권고 항목 (비차단)

| # | 권고 | 출처 |
|---|------|------|
| **AR-1** | 설계 공간 §3 확장 — 실행 격리 패턴 **E(rootless+userns-remap)·F(gVisor/Kata)·G(ephemeral VM per task)·H(capability lease)**, 각 R/P/T 적용 매핑 + ARM64/PL trade-off | C-2 |
| **AR-2** | 패턴 B = **기존 r2-poc/gp3-st3 PoC 일반화** cross-ref (신규 설계 아님, 채택 비용 인식 정확화) | A AR-1 |
| **AR-3** | 패턴 A 에 **systemd unit + Polkit** = sudoers 보다 좁은 표면 대안 1줄 | A AR-2 |
| **AR-4** | **재귀 종료 닻** = allow-list/정책 파일 root:root, agent 쓰기 미보유 = 회귀 1단계 멈춤 *구현 속성* 명문 | A AR-3 |
| **AR-5** ⭐ | **harness 4축 일반 원칙화 = §7 합의 결정 항목 격상** — P-PRIV 가 credential 한정인지 4축(allow-list·anchor·audit) 일반인지. 일반화 시 T 경계 목록 = 4축 합집합 | C-R3 |
| **AR-6** | **PL = broker 인터페이스/구현 분리** (CD-8/R-4 답습) — broker 정책=선언적 데이터, 집행 매체(sudoers/systemd/IAM) 교체 가능. 클라우드 IAM lock-in 차단 | C-R1 |
| **AR-7** | 패턴 B fallback 순서 — B 불가(동적 권한 필수) 시 → 폭발반경 최소 broker(C) + 단명 capability(H) | C-R2 |
| **AR-8** | "모호하면 T" over-classification 마비 방지 = 정기 분류 재검토(어떤 T 가 lease 로 G 회복 가능한가) — 정적 1회 ≠ 형량 | C-R4 |
| **AR-9** | Signer/Verifier 분리 cross-ref(§5) + P-provision artifact = 사람 검토 후 실행(무비판 금지) | A AR-4 + B R-4 |

---

## 4. 거짓 안전감 차단 (Reviewer 격상)

본 합의의 가장 위험한 실패 양식 3가지: (i) **"broker/정책 깔았으니 안전"** — AP-2(강제 메커니즘)·AP-5(별도 §·적대적 시연 binary)로 차단. "결정적 게이트" 라벨 ≠ 입증(CD-5). (ii) **"T-목록 다 적었으니 안전"** — AP-1: 목록은 본질적으로 불완전 → *구조*(default-T)로만 닫힘. brief 자기경고가 자기충족 안 됨. (iii) **"(2) 형량 = 마찰 줄이기"** — AP-3: 형량은 마찰을 *줄이는* 게 아니라 *어디로 옮기는지*(CMA-6 표면 이동 동형) + 정적 분류가 *drift 엔진*(편의로 T→R). ⭐ **메타(CP-10 재발)**: Agent C 핵심2 = "`ead5754` CD-8/PL 교훈(인터페이스/구현 분리)이 broker 축에 *미적용*" = 축 간 교훈 비전파의 권한 정책 축 재발 → 거짓 안전감 차단·PL 정합은 *매 축 재명문* 필요(자동 전파 안 됨). agent 일반 sudo 미부여 = 불변(자기검증 금지, Hermes ≠ root).

---

## 5. 미해소 쟁점 / 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | brief 를 AP-1~6 + 권고 AR-1~9 반영 **v2 수정** (본문 반영, 채택·발효 0건) | brief 수정 |
| (B) | **AR-5 결정** — P-PRIV 일반화 범위(credential 한정 vs 4축 일반)를 먼저 정함 | 결정 |
| (C) | 형량 결과(특히 AP-3 lease·AP-6 서명 빈도) 반영해 **credential 발효 (다) 재개** | 발효 (보류) |
| (D) | 합의 보고서 + brief commit | 메타 |
| (E) | 세션 종료 | 메타 |

- ⭐ **권고 순서**: (A) brief v2(AP-1~6) → (B) AR-5 범위 결정 → (C) credential 발효 (다) 재개. AP-3(lease)·AP-6(서명 빈도)이 credential 수단 결정의 직접 입력.
- **정책 *채택*·broker 구현·credential 재결정 = 본 합의가 내리지 않음** — 사용자 명시 + 별도 단계.

---

## 6. 합의 한 문단 요약

**Agent 권한 상승(sudo) 처리 정책 brief = APPROVE WITH CONDITIONS** 이다. 세 Agent 는 (1) 범위 규율·핵심 긴장(G⊥S) 명문화 견고, (2) R/P/T 분류 + (2) 형량 골격 유효하나 *정적 분류*가 공통 약점, (3) citation stale 0(CP-10 답습 효과), (4) 거짓 안전감 차단이 binary *언급*뿐 강제 부족 에 일치했다. 가장 무게 있는 발견은 **B·C 가 "정적 분류의 한계"에 독립 수렴**(B = (2) 형량이 *drift 엔진* → 단방향 ratchet / C = 빠진 차원 = *시간 lease* → §4(4) 원칙 실현 메커니즘) → 결합해 **AP-3(lease + ratchet + drift Rollback Trigger)**. 이어 **A·B 수렴 "broker 강제 메커니즘 미명세"**(argv·`SO_PEERCRED`·TOCTOU + broker 위협 4 → AP-2), **A·B 수렴 "T-목록 정적 enumeration 이 위협모델과 모순"**(누락 5건[패키지/공급망·`.git/`·CI yaml·env/secret·egress] → default-T 구조 AP-1)이다. Agent C 단독으로 **harness 4축 일반 원칙화**(AR-5)·**PL broker 인터페이스/구현 분리**(CP-10 재발, AR-6)·**실행 격리 패턴 E~H**(AR-1)를, Agent B 단독으로 **allow-list 항목 escape-equivalence**(AP-4)를, Agent A 단독으로 **패턴 B = 기존 PoC 일반화**(AR-2)·**재귀 종료 닻**(AR-4)을 격상했다. 채택 전 **BLOCKING 6**(AP-1 default-T 구조 / AP-2 broker 강제 메커니즘 / AP-3 동적 차원=lease+ratchet / AP-4 escape-equivalence / AP-5 거짓 안전감 § / AP-6 credential fork 단정 약화+대안 확장) + 권고 9이며, 거짓 안전감 차단(라벨 ≠ 입증·목록은 구조로만 닫힘·형량=표면 이동·축 간 교훈 비전파)을 Reviewer 격상했다. 교차 = 일치 5 / 부분 4 / 불일치 1(D1, 보완으로 해소) / 누락 10. 본 합의는 추론적 검증(권고) 한정 — 정책 *채택*·sudoers/broker 구현·credential 재결정·commit·push 는 사용자 명시 + 별도 단계이며, **본 보고서 외 어떤 파일도 편집/생성하지 않고 commit/push 0건**이다.

---

## 7. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | APPROVE w/ COND. citation stale 0. BLOCKING 2: **A-1 결정적 게이트 강제 메커니즘 미명세**(argv·`SO_PEERCRED`·canonical·TOCTOU) / **A-2 R/P/T 모호 경계**(git push·docker·패키지). 핵심 = 패턴 B는 기존 PoC 일반화 / 게이트가 원칙 선언에 그침 |
| **Agent B** (보안) | "안전하고 견고한가?" | APPROVE w/ COND. BLOCKING 6: **B-1 T-목록 불완전→default-T** / B-2 allow-list escape-equivalence / B-3 broker 공격 표면 / B-4 거짓 안전감 binary 미전파 / **B-5 (2)형량=drift 엔진→단방향 ratchet** / B-6 credential 비서명 공백. 핵심 = 정적 enumeration이 위협모델과 모순 / 형량이 drift 엔진 |
| **Agent C** (대안) | "더 나은 방법?" | APPROVE w/ COND. BLOCKING 3: **C-1 정적 분류→2축 grid+lease(시간 차원)** / **C-2 설계 공간 확장(E~H 격리 패턴)** / **C-3 credential fork 대안(batch·cached presence)**. 핵심 = 빠진 차원=시간(lease) / PL=인터페이스 분리(축 간 교훈 비전파=CP-10 재발) / 4축 일반화 |
| **Reviewer** | "최선의 합의는?" | 교차(일치 5 / 부분 4 / 불일치 1 / 누락 10) + B·C 수렴(정적→동적) + A·B 수렴(broker 강제·default-T) = **BLOCKING 6(AP-1~6) 통합 + 거짓 안전감 차단 격상(CP-10 재발) + AR-5 4축 일반화 §7 격상**. **APPROVE WITH CONDITIONS** |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**정책 *채택·고정* / sudoers·`/etc/sudoers.d/` 변경 / broker·sidecar·systemd unit·Polkit 실 구현 / `settings.json` 권한·hook 변경 / capability lease·TTL 실 구성 / credential 수단 *재결정*(BI-3 `ead5754` 본문 변경) / S-0+S-2 발효 / tpm2-pkcs11 설치·group·tss 변경 / rootless·gVisor·Kata·ephemeral VM 전환 / sigstore·gitsign·Rekor 도입 / Hermes runtime·upstream 변경 / Vault HSM ST-4 / threshold 고정 / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit / Phase α defer-lockdown 변경 / git history rewrite / ADR·harness-engineering-design·합의 본문 자동 갱신 / 원 합의 본문(`ead5754`/credential 발효 합의) 자동 정정 / 다른 BLOCKING 자동 진입 / 합의 보고서 외 파일 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.**
