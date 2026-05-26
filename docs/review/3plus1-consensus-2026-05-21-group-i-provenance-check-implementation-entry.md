# 3+1 합의 보고서 — Group I (provenance check) 실 강제 구현 entry (Backlog #6, R-I-IMPL-BOUNDARY)

> **본 합의 = 추론적 검증(권고) 한정.** frame 4축(positive allow-list / credential boundary / external enforcement / audit sink integrity)은 `f6c6d5a`+`141bbc9`+후속 68(`708bc0e`) 만장일치 확정 — 재논쟁 없음. 본 합의는 **합의 형태 + single-host MVP 수단 권고 + 진입 적격성 + 구현 발효 전 BLOCKING 통합** 만 다룬다. **실 hook/ruleset/CI/credential/sink 구현 / 수단 결정 *고정* / Operational Readiness PASS / Hermes PMO 격상 / Vault HSM ST-4 진입 / commit·push 외 변경 = 모두 0건.** 실 결정/구현 = 사용자 명시 + 별도 단계.

---

**작성일**: 2026-05-21
**합의 형태**: 풀 3+1 (Agent A 구현/정합 · Agent B 보안 · Agent C 대안 + Reviewer) — **의무** (Group I = T3 보안 enforcement, `f6c6d5a` §8 + boundary brief §8, R-I-IMPL-BOUNDARY 별도 풀 3+1). Reviewer-only 부적격
**합의 입력**: `docs/phase0/group-i-provenance-check-implementation-boundary-brief.md` (boundary brief DRAFT v1)
**1차 권위 답습**: `f6c6d5a` Group I 합의 (B-1~B-6) + `708bc0e` G3 provenance check DESIGN 발효 + Backlog #6 Layer A/B/C(`f1e0b23`/`f40423f`·`55c5b4b`/`eb01bc4`) + Group α `4880e88`(AR-3/C-4) + γ-1 `9b1f8cd`(ST-1)·γ-2 `2e9d46b`(ST-4 DEFER) + ADR-011 §2.1 means/ends
**판정**: **APPROVE WITH CONDITIONS** — single-host MVP 영역 구현 entry 진입 *적격* + MVP-6 DEFER + **10 BLOCKING (BI-1~BI-10) + 4 조건부** + single-host 수단 권고(권고 한정, CN-6)

---

## 0. 종합 판정 (한 문단)

세 Agent는 **(1) single-host 구현이 기술적으로 가능하나 "0-구현"이 아님(CI provenance step의 fingerprint allow-list 대조 = 실 코드 필요), (2) 3축(allow-list·external anchor·audit sink)이 모두 "Hermes 환경에 사람/admin credential 미주입"에 독립 수렴 → credential 격리 = 4축의 *공통 선결 전제*, (3) single-host에서 4축이 *구현되어도* 동일 침해 경계로 수렴할 때 명목화되며 "충족=안전 확정"이 아니라 "수용된 SPOF 위 최선", (4) SaaS self-bypass 역설(1인=repo admin이 ruleset을 끌 수 있음)이 external anchor 명목화의 가장 현실적 경로, (5) CI step과 ruleset은 경쟁이 아니라 보완(ruleset=서명 *존재*, CI=fingerprint allow-list 대조)** 이라는 데 완전 일치한다. 가장 무게 있는 교차 발견은 Agent C가 단독 제시하고 A가 harness 원칙("잘못하는 것이 불가능하게")으로, B가 안전 우선순위로 독립 수렴시킨 사실 — **hardware-backed key(YubiKey/FIDO2)가 credential 격리를 *구조적으로 흡수*한다**(키가 물리 토큰 밖으로 안 나오므로 동일 호스트 keychain/agent socket 공유 gap 자체가 소멸). 단 그 부작용으로 **1인 lock-out 가용성 SPOF → 백업 키 의무**(BI-9). Reviewer가 G3 원문(후속 68 발효, line 360/784/805)으로 검증한 결과 본 entry는 4축 DESIGN의 *실 구현 경계*에 정확히 위치한다(재논쟁 0건). 본 합의 = **추론적 검증(권고) 한정 — 수단 결정·실 구현·commit·push는 사용자 명시 + 별도 단계.**

---

## 1. 교차 비교

### 1.1 일치 (Consensus — 3 Agent 모두)

| # | 합의 항목 | A | B | C |
|---|---------|---|---|---|
| C1 | single-host 구현 *가능*하나 "0-구현 아님" (CI provenance step fingerprint 대조 = 실 코드) | ✅ | ✅ | ✅ |
| C2 | **⭐ credential 격리 = 4축 공통 선결 전제** (3축이 credential 미주입에 독립 수렴) | ✅ | ✅ | ✅ |
| C3 | positive allow-list ≠ ruleset 단독 (ruleset=서명 존재만, Hermes 자기 키도 통과 → fingerprint 대조 별도) | ✅ | ✅ | ✅ |
| C4 | CI step ↔ ruleset = 보완(둘 다 필요) | ✅ | ✅ | ✅ |
| C5 | external anchor = host 밖 ruleset(off-host)이 현실적 실 anchor / pre-commit hook = sensor 신호(차단권 아님) | ✅ | ✅ | ✅ |
| C6 | SaaS plan 종속(Group α C-4 미해소) + SaaS self-bypass = 명목 anchor 현실 경로 | ✅ | ✅ | ✅ |
| C7 | SaaS(ruleset+CI) ≠ GHES(pre-receive) 분리 명문 (GHES anchor 상승) | ✅ | ✅ | ✅ |
| C8 | audit = append-only git remote + hash chain(tamper-evident)까지 single-host ✅, 완전 immutable=MVP-6 | ✅ | ✅ | ✅ |
| C9 | Hermes는 ruleset/CI/audit token 미보유 (R-I-CONFIG-CHANGE B-5) — 자기 차단책 무력화 불가 | ✅ | ✅ | ✅ |
| C10 | observe ≠ enforcement 발효 (FN 통과=차단 보장 0) + 전환=사용자 명시 | ✅ | ✅ | ✅ |
| C11 | Vault HSM ST-4 = MVP-6 DEFER / single-host canonical = ST-3 docker secret + ST-1 file perm | ✅ | ✅ | ✅ |
| C12 | Provider Liquidity — host·CLI·서명 도구 하드코딩 금지(GHES≠GitHub.com 후보 열거 유지) | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial — 2 동의, 1 강조/추가)

| # | 항목 | 분류 |
|---|------|------|
| P1 | **hardware-backed key가 credential 격리를 *구조적으로 흡수*** | C 명시 / A "키 물리 토큰 밖 미이탈=harness 원칙" 수렴 / B "진정 hardware 격리만 BLOCKING 해소" 실질 동의 |
| P2 | **single-host 4축 = "충족=안전 확정 아님, 수용된 SPOF 위 최선"** (거짓 안전감 차단) | B 강하게 명시 / A "3축 credential 수렴"으로 동일 결론 / C self-bypass 역설로 보강 |
| P3 | **observe→enforce 전환 = 증거 기반(시간 기반 아님) + 주체 명시(`agent=user`)** | C 명시(N-6) / B 면책 조건화(B-IMPL-7) / A "Phase α↔β observe 라벨" |

### 1.3 불일치 (Divergence — 관점차 스펙트럼)

| # | 항목 | A | B | C | Reviewer |
|---|------|---|---|---|----------|
| D1 | 단일 우선순위 강조 | 기술 간극 식별(*어디가 0-구현 아닌가*) | credential 격리 BLOCKING이 모든 축 전제(최강) | 수단 선택이 격리 흡수(hardware-backed) | **진정 충돌 아닌 관점차 — 셋 다 "credential 격리=핵심 gate·single-host에서 최약"으로 귀결. C 흡수가 가장 근본적이나 B의 1인 lock-out SPOF(N-7)가 부작용 → 상보(BI-3 + BI-9 통합)** |

### 1.4 누락 (Gap — 단독 발견, Reviewer 중요도)

| # | 항목 | 언급 | 중요도 | 처리 |
|---|------|-----|-------|------|
| N-1 | sigstore/gitsign·Rekor 수단 후보 누락 (keyless·투명성 로그) | C | 중 | CBI-4 후보 보존(MVP 비채택) |
| N-2 | GP-3 §6.2 인터페이스 미인용 (G2 노출 차단 / G3 변경 권한 차단) | C | **높음** | BI-3 권위 |
| N-3 | SaaS self-bypass 역설 (1인 admin=ruleset bypass) | C | **높음** | BI-4 |
| N-4 | CI step의 §2.5 #2(workflow read-only) 의존 미명시 | C | **높음** | BI-1 |
| N-5 | audit write 자격증명 = credential 재귀 | C | 중 | BI-5 |
| N-6 | observe→enforce 전환 주체 미명시 (`agent=user`+증거 기반) | C | 중 | BI-7/P3 |
| N-7 | hardware token SPOF — 1인 lock-out, 백업 키 | C | **높음** | BI-9 |
| N-8 | Layer 3 `.git/` ACL 선행 (commit layer 사각) | C | 중 | BI-10 |
| GA-1 | Phase α(scanner)↔Phase β(anchor) 간극 = 강제 observe 라벨 필수 | A | **높음** | BI-8 |
| GA-2 | Group α C-4 (GitHub.com plan 종속) 미해소 = entry 확인 사항 | A | 높음 | BI-4 |

---

## 2. 합의 도출

### 2.1 합의 형태 + 진입 적격성

**R-I-IMPL-BOUNDARY 구현 entry = 풀 3+1 *의무*, Reviewer-only 부적격** (만장일치, trigger #2 T3 + #5 핵심 제약 #1/#4 + §4 self-reference). 2차 vendor = trigger #7 기 충족(GPT-5.5 1건), 추가 = 사용자 결정.

| 영역 | 판정 | 근거 |
|----|----|----|
| **single-host MVP 영역** (CI provenance step + 사람 키 Hermes 미주입[ST-3/ST-1] + GitHub ruleset off-host + append-only git remote audit + observe mode) | **구현 entry 진입 *적격*** | G-1~G-3 충족. G-4(격리)·G-5(anchor 가용)=entry 확인 — 단 BI-3·BI-4 발효 전 BLOCKING |
| **MVP-6 / Operational Readiness** (Vault HSM ST-4·multi-host mTLS·KMS·distributed audit·hard-block threshold) | **DEFER (진입 부적격)** | G-6 ❌. γ-2 답습. §5.5.3 trigger 시 별도 진입 |

> 진입 적격 ≠ 즉시 발효. **BI-1~BI-10(특히 BI-3) 충족이 실 구현 발효 전 BLOCKING.** 진입 *결정* = 사용자 명시.

### 2.2 구현 발효 전 BLOCKING 통합 (A 3 + B 7 + C 8누락 → 중복 제거 10건)

**우선순위: BI-3(credential) > BI-4(anchor) > BI-1/BI-2 > BI-5 > BI-9 > BI-6/BI-7/BI-8/BI-10.**

| # | BLOCKING | 출처 | 우선 |
|---|----------|------|------|
| **BI-1** | CI provenance step = fingerprint allow-list 실 대조 코드(0-구현 아님) + Hermes 밖 신뢰 경계 실행 + **§2.5 #2 workflow read-only 의존 명시** | A + B-IMPL-1 + C3/N-4 | 2 |
| **BI-2** | runtime = sensor 신호만, 최종 reject = push/merge server-side(`--no-verify` 우회 불가) — Hermes 밖 anchor 차단 보장 | A + B-IMPL-2 | 2 |
| **BI-3** ⭐ | **credential 격리 = 4축 공통 선결 전제** — 사람 signing key·token·SSH/GPG agent Hermes 미주입(env scrub + socket 미마운트 + cap_drop). 미격리 시 4축 명목화 + 순이득 0 + 거짓 안전감. host 침해 한계 명시. **GP-3 §6.2 권위**(N-2) | A 공통 gate + B-IMPL-3(최강) + C2/N-2 | **1** |
| **BI-4** | external anchor 실재성 — (i) plan 확인(C-4, GA-2) + (ii) anchor token Hermes 호스트 외 분리 + (iii) **SaaS self-bypass 차단**(bypass list 비움 + CI required check 실 게이트 + ruleset 변경=R-I-CONFIG-CHANGE T3) + (iv) origin replace 위험 명시. 명목 anchor 금지 | A + B-IMPL-4 + C/N-3 | 2 |
| **BI-5** | audit sink = Hermes write 불가 + host 침해 tamper-evident(hash chain) + **audit write 자격증명 재귀 격리**(N-5). credential과 별개 축 | A + B-IMPL-5 + C/N-5 | 3 |
| **BI-6** | Provider Liquidity — host·CLI·서명 도구 하드코딩 금지(후보 열거 유지) | B-IMPL-6 + C12 | 4 |
| **BI-7** | observe 면책 명시(FN 통과="차단 보장 0") + 전환 = 증거 기반 + 사용자 명시(`agent=user`) + BLOCKING 재확인 | B-IMPL-7 + C/N-6 + P3 | 4 |
| **BI-8** | Phase α(scanner)↔Phase β(anchor) 간극 = 강제 observe 라벨 명시(GA-1, silent scope expansion 차단) | A GA-1 | 4 |
| **BI-9** | hardware token SPOF 완화 — 채택 시 1인 lock-out 방지 = 백업 키(2개+) 등록 의무(N-7) | C N-7 | 3 |
| **BI-10** | Layer 3 `.git/` ACL 선행(N-8, commit layer 사각, B-6 답습) | C N-8 | 4 |

### 2.3 조건부 4

| # | 조건부 | 조건 |
|---|--------|------|
| CBI-1 | hardware-backed key 흡수 채택 | 백업 키 의무(BI-9) + 토큰 = 수단 후보(결정=entry 발효, CN-6) |
| CBI-2 | SaaS ruleset = external anchor | self-bypass 차단(BI-4) — 미충족 시 명목 anchor |
| CBI-3 | observe mode 우선 | observe≠발효 명시(BI-7) + 전환=증거 기반+`agent=user` |
| CBI-4 | sigstore/gitsign·Rekor (N-1) | MVP 비채택 — 후보 보존(투명성 로그=MVP-6 audit 시너지) |

### 2.4 single-host MVP 수단 권고 (권고 한정, 결정 고정 아님 — CN-6)

| 축 | 1순위 권고 | 후보 (결정=entry 발효) | 근거 |
|----|------|------|------|
| credential boundary (선결) | **hardware-backed key(YubiKey/FIDO2)** + ST-3 docker secret + ST-1 file perm | hardware-backed / vault / KMS | C(흡수)+A(구조 성립)+B(진정 hardware만 해소) |
| positive allow-list | **SSH signed commit (`allowed_signers`=allow-list 매체)** + CI fingerprint 대조 | SSH / GPG(후순위) / ruleset+CI | C+A(CI 대조=실 코드)+GPG 후순위 만장일치 |
| external anchor | **SaaS=ruleset+CI required check / GHES=pre-receive** (분리 명문) | ruleset / container ACL / hardware key 분리 | C(SaaS/GHES)+A(현실적)+B(plan+token 분리) |
| audit sink | **append-only git remote** + hash chain | append-only remote / 외부 read-only mount / 분산 sync(MVP-6) | C 1순위+A(hash chain까지 ✅)+Rekor MVP-6 |
| observe | **runtime 항구 observe(sensor) — enforcement는 anchor만** + 증거 기반 전환 | — | C+B+P3 |

**순서(만장일치)**: **credential(hardware 흡수) → allow-list 정의(차단 *기준*) → external anchor → audit.**

### 2.5 G3 DESIGN 정합 (Reviewer 원문 검증, 본문 변경 0건)

후속 68(`708bc0e`) 발효 G3 본문이 이미 4축 DESIGN 보유: line 360/784(positive allow-list·author 판정 입력 아님) / line 784 각주¹·§3.1.3(external anchor·host 밖 실 anchor·push/merge 전 보장) / line 784 각주¹(audit sink 별개 축). **재논쟁 0건.** 본 합의는 G3 본문 미변경, 구현 컴포넌트 매핑(BI-1~BI-10)만 권고.

---

## 3. 결정 vs 설계 vs 구현 경계

| 계층 | 본 합의 산출 | 발효 권한 |
|------|-------------|----------|
| **합의 권고 (본 보고서)** | 풀 3+1 의무 / single-host 진입 적격 / 10 BLOCKING + 4 조건부 / 수단 권고 / MVP-6 DEFER | Reviewer 종합 — **발효 아님** |
| **수단 결정 (DESIGN→IMPL)** | hardware-backed key / SSH `allowed_signers` / SaaS ruleset+CI / append-only git remote *고정* | **사용자 명시 + entry 발효** (CN-6) |
| **구현 (IMPLEMENTATION)** | 실 hook / CI provenance step / ruleset / credential isolation / audit sink 본문 + Implementation Evidence PASS | **Backlog #6 + 별도 발효 + Evidence** |

---

## 4. 거짓 안전감 차단 (B 핵심 — Reviewer 격상)

**"single-host 충족 = 안전 *확정* 아니라 수용된 SPOF 위 *최선*."** single-host 4축은 동일 침해 경계(사용자 호스트=Hermes 호스트)로 수렴 시 명목화 — **credential 미격리(BI-3) 시 4축 전부 명목화 + metadata 대비 순이득 0 + 거짓 안전감만 추가.** G3 §5.5 SPOF는 *의도적 수용*(1인 MVP)이며 본 entry는 그 SPOF *안에서의* 최선. multi-host/Vault(MVP-6)는 §5.5.3 trigger 충족 시에만 진입. 진입 적격 판정이 "single-host=안전 확정"으로 오용되는 것을 명시 금지.

---

## 5. 미해소 쟁점 / 후속 (사용자 결정 영역 — 자동 진입 0건)

1. **수단 최종 결정** = entry 발효 단계(CN-6, 사용자 명시).
2. **Group α C-4 (GitHub.com plan 종속)** = anchor 실재성(BI-4) 전제, plan 확인 = entry 발효 시.
3. **observe→enforce threshold** = threshold 고정 영역(별도 단계).
4. **hardware token 백업 키 정책**(BI-9) = 구현 결정.
5. **2차 vendor**(Gemini 등) = trigger #7 1건 충족, 추가 = 사용자 결정.
6. **G1 (PR·approval auto-reject)** = Group α C-2 별도 단위, 본 entry 범위 밖.
7. **sigstore/gitsign·Rekor**(N-1/CBI-4) = MVP 비채택, MVP-6 audit 강화 시 재검토.

---

## 6. 합의 한 문단 요약

**Group I provenance check 실 강제 구현 entry(R-I-IMPL-BOUNDARY)는 single-host MVP 영역에 대해 구현 entry 진입 *적격*이며 판정 = APPROVE WITH CONDITIONS, MVP-6 영역(Vault HSM ST-4·multi-host·KMS·hard-block threshold)은 DEFER, 합의 형태는 풀 3+1 의무(Reviewer-only 부적격)**이다. 세 Agent가 독립 수렴시킨 핵심은 **credential 격리가 4축(positive allow-list·external anchor·audit sink) 공통 선결 전제**(3축이 "사람/admin credential Hermes 미주입"에 수렴)이며 **미격리 시 4축 전부 명목화 + metadata 대비 순이득 0 + 거짓 안전감만 추가**(C2/P2)라는 점이다. 가장 무게 있는 발견은 **hardware-backed key(YubiKey/FIDO2)가 키를 물리 토큰 밖에 두지 않음으로써 credential 격리를 *구조적으로 흡수*(harness 원칙)하나, 부작용으로 1인 lock-out 가용성 SPOF → 백업 키 의무**(BI-9/N-7)가 생긴다는 점이다. 구현 발효 전 BLOCKING은 **10건**(BI-1 CI fingerprint 대조 실 코드+workflow read-only / BI-2 reject=Hermes 밖 server-side / **BI-3 credential 격리=최강·GP-3 §6.2** / BI-4 anchor 실재성+SaaS self-bypass 차단+plan 확인 / BI-5 audit write 불가+재귀격리 / BI-6 Provider Liquidity / BI-7 observe 면책+증거기반 전환 / BI-8 Phase α↔β observe 라벨 / BI-9 hardware token 백업 키 / BI-10 `.git/` ACL 선행) + 조건부 4건이며 우선순위는 **credential 격리(BI-3) 최강**이다. single-host 수단 권고(권고 한정, CN-6)는 credential=hardware-backed key, allow-list=SSH `allowed_signers`+CI fingerprint 대조, anchor=SaaS ruleset+CI(self-bypass 차단)/GHES pre-receive, audit=append-only git remote, observe=runtime 항구 sensor·anchor만 enforce이며 순서는 credential→allow-list→anchor→audit이다. Reviewer 검증 결과 G3 본문(후속 68 발효)은 이미 4축 DESIGN을 담고 있어 본 entry는 그 실 구현 경계에 정확히 위치(4축 재논쟁 0건). **"single-host 충족=안전 확정 아니라 수용된 SPOF 위 최선"**을 거짓 안전감 차단으로 명시한다. 본 합의는 추론적 검증(권고) 한정 — 수단 *결정*·실 구현·commit·push는 사용자 명시 + 별도 단계이며, **본 보고서는 어떤 파일도 편집/생성/수정하지 않고 commit/push 0건**이다.

---

## 7. 풀 3+1 관점 분배 (실 가동 기록)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현/정합) | "실제로 동작하는가?" | single-host 구현 가능하나 0-구현 아님(GitHub.com 4/6 ✅·2/6 ⚠️ / GHES anchor 상승). ruleset=서명 존재만→CI fingerprint 대조 실 코드(plan 종속 C-4). ⭐ 3축이 credential 미주입에 독립 수렴=공통 선결 전제. 3 BLOCKING(C-4 plan / credential 공통 gate / Phase α↔β observe 라벨) |
| **Agent B** (보안) | "안전하고 견고한가?" | ❌ credential 격리=현 미충족=최강 BLOCKING(동일 호스트 keychain/socket / Vault ST-4 DEFER → 진정 hardware 격리 부재). 미격리 시 4축 명목화+순이득 0+거짓 안전감. 7 BLOCKING(B-IMPL-1~7). "충족=안전 확정 아니라 수용된 SPOF 위 최선" |
| **Agent C** (대안) | "더 나은 방법?" | ⭐ hardware-backed key가 credential 격리 구조적 흡수(SSH `allowed_signers`=allow-list 매체, GPG 후순위). SaaS self-bypass 역설=anchor 명목화 현실 경로(SaaS=ruleset+CI/GHES=pre-receive 분리). CI+ruleset=보완. 순서 credential→allow-list→anchor→audit. 8 누락(N-7 hardware SPOF=백업 키) |
| **Reviewer** | "최선의 합의는?" | 교차(일치 12 / 부분 3 / 불일치 1 / 누락 10) + BLOCKING 통합(10건, credential 최강) + 수단 권고 + 진입 적격성(single-host 적격·MVP-6 DEFER) + G3 DESIGN 원문 검증(재논쟁 0) + 거짓 안전감 차단 명시. **APPROVE WITH CONDITIONS** |

---

## 부록 — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
실 hook 구현(pre-commit / pre-receive / git server-side / CI provenance step) / GitHub ruleset·branch protection·required-signature·required status check·bypass 정책 실 변경 / CI workflow 변경(provenance step / actual run / workflow_dispatch / paths 필터) / filesystem ACL·`read_only` mount·`cap_drop`·credential isolation(사람 키 미주입) 실 구성 / audit sink 실 구성(외부 read-only / append-only) / Hermes runtime·upstream 변경 / 수단 결정 *고정*(키 종류·서명 방식·차단 지점·sink 매체 — CN-6) / threshold 고정(observe mode 기간) / Operational Readiness PASS(Layer E) / Hermes PMO 격상(Layer F) / Vault HSM ST-4 진입(γ-2 DEFER MVP-6) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경(특히 line 360/784/805 4축) / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / G1(PR·approval auto-reject) 신규 단위 자동 진입(Group α C-2 별도 단위) / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 외 파일 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
