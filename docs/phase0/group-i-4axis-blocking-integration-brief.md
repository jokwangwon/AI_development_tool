# Group I 4축 BLOCKING 통합 정리 brief — 구현 entry 발효 readiness 검토 (DRAFT v2)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 4축(credential·allow-list·anchor·audit) 단독 심화(BI-3 후속 71~72 / BI-4 73 / BI-5 75 / BI-1 76)가 *완주* 된 시점에서, 4축·10 BLOCKING·교차 패턴을 *통합 정리* 하고 구현 entry 발효 readiness 를 *검토* 하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 수단 *결정 고정*·실 hook/CI/ruleset/credential/audit sink 구현·구현 entry *발효*·Operational Readiness PASS·Hermes PMO 격상 을 발생시키지 않는다. 본 brief = **4축 심화 결과 통합·10 BLOCKING 현황·교차 패턴 추출·의존 그래프·수단 통합·발효 선결 순서·미심화 gap·readiness 검토** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push**.

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + 통합 정리 brief 검증 풀 3+1 합의 `f6a6c57` BLOCKING IB-1~4 + 권고 IR-1~6 반영 — 본문 반영, 결정·발효 0건)

## v2 변경 이력 (`f6a6c57` 합의 BLOCKING IB-1~4 + 권고 IR-1~6 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **IB-1** ⭐ (통합 문서 고유 거짓 안전감) | §9 — "통합·readiness 검토 자체가 발효 정당성·안전 부여 안 함, 통합=뷰 환원이지 SPOF 해소 아님" (entry "진입 적격≠안전 확정" 통합 축 대칭) |
| **IB-2** ⭐ (owner self-bypass DEFER 비용, CB-2≡C대안1) | §7.4 + §6 + §9 — owner 경로 P-1~P-5 충족 후에도 4축 잔존 + "Rekor/Sigstore MVP-6 DEFER = owner self-bypass 4축 영구 수용 *결정* 동치" + §6 CP-7 위상 "구조적 대안 경로" 격상 + "4단 누적 vs Sigstore 1회 융합" trade-off |
| **IB-3** (BI-8/BI-10 안전 구멍 + BI-9 백업키) | §7.2 P-3 + §8 — BI-8 silent scope expansion·BI-10 commit layer 사각(범위 밖 합집합 무방비) 발효 선결 + BI-9 백업키 기밀성·공격표면 N배 trade-off(§6/P-1) |
| **IB-4** (P-5 binary 축별 매핑) | §7.2 P-5 — 각 축 binary 종료조건(BI1C-1 미서명 reject·BI-5 §10·BI4C-2) 매핑 |
| IR-1 (BI4C-3) | §7.2 P-list — direct-push gate(restrict-direct-push + G-BI4-6) anchor 발효 독립 선결 |
| IR-2 | §6 anchor 행 restrict-direct-push 전제 병기 |
| IR-3 | §7.2 P-2 "반영분/미반영분" 2분 |
| IR-4 (2-track) | §7.4 — enforce 순차 + observe 4축 동시 2-track (BI-7 면책 라벨 동반) |
| IR-5 (PL 긴장) | §6 — Sigstore↔CP-6 중립 긴장 + 다중 미러 PL-안전 대안 |
| IR-6 | §6 anchor 층1 정합(fingerprint=allow-list 몫) + §4 BI1C-2/3 교훈 승격 |
**진입 단위**: Group I 구현 entry 합의 후속 #5 — **4축 심화 완주 후 통합 정리** (BI-3/1/4/5 단독 심화 종료)
**선행 발효 답습**: `c896104` 후속 76(BI-1 allow-list) + `27c188f` 후속 75(BI-5 audit) + `9492193` 후속 73(BI-4 anchor) + `ead5754` 후속 72(BI-3 credential 수단) + `bf42d0e` 후속 71(BI-3 격리) + `f29c772`/`8e57f7b` Group I 구현 entry 합의(10 BLOCKING + 4 조건부 + N-1) + `708bc0e` G3 4축 DESIGN
**답습 입력 (1차 권위)**: **`f29c772` BI-1~BI-10 + CBI-1~4 + 우선순위(BI-3>BI-4>BI-1/2>BI-5>BI-9>BI-6/7/8/10) + 순서(credential→allow-list→anchor→audit) + CN-6 수단 권고** + 4축 합의 보고서 4건의 BLOCKING(BI3-*/CD-*/BI4C-*/BI5C-*/BI1C-*) + 교차 패턴
**합의 권위 한계**: 본 brief = *통합 정리·readiness 검토* DRAFT — 수단 *결정*·구현 entry *발효*·실 hook/CI/ruleset/credential/sink 구현 은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. **본 brief 는 "발효해도 되는가/무엇이 선결인가"를 *정리* 할 뿐 발효를 *결정* 하지 않는다.**

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "4축 BLOCKING 통합 정리 ... 우선순위·의존·gate·수단 통합 + 구현 entry 발효 검토"

본 brief = 위 명령 답습 — **4축 심화 완주 후 통합 정리** = (i) 4축 심화 결과 통합(판정·BLOCKING·핵심) + (ii) 10 BLOCKING 현황 매트릭스(심화/부분/미심화) + (iii) ⭐ **교차 패턴 9건**(모든 축 반복 발견) + (iv) 의존 그래프(credential 선결·재귀 보호·ruleset↔CI 보완) + (v) 수단 권고 통합(CN-6 + 2층 추상화 + Rekor 3축 시너지) + (vi) ⭐ **구현 entry 발효 readiness 검토**(선결 순서·미해소 gap·MVP-6 경계) + (vii) 미심화 standalone gap(BI-2/6/7/8/9/10) + 합의 형태 — **실 변경·발효 0건**.

### 0.2 본 brief 가 *하는* 것 / *하지 않는* 것

- **하는 것**: 4축·10 BLOCKING·교차 패턴·의존·수단·readiness 를 *정리/검토/권고*.
- **하지 않는 것 (사용자 명시 영구 답습)**: ❌ 수단 *결정 고정*(credential·allow-list·anchor·audit 매체) / ❌ 구현 entry *발효*(실 hook / CI provenance step / GitHub ruleset·required-signature / `.github/workflows/` / credential·서명 키 분리 / audit sink) / ❌ `allowed_signers`·hardware key·append-only remote 실 구성 / ❌ sigstore·gitsign·Rekor 도입 / ❌ Operational Readiness PASS(Layer E) / Hermes PMO 격상(Layer F) / Vault HSM ST-4(γ-2 DEFER) / ❌ threshold 고정 / MVP-1 exit / Phase α defer-lockdown 변경 / ❌ **git history rewrite**(후속 74, SHA 붕괴) / ❌ G3·ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / ❌ 다른 BLOCKING(BI-2/6/7/8/9/10) standalone 자동 진입 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화.

### 0.3 권위 한계

본 brief 는 결론을 *선취하지 않는다*. readiness 검토·선결 순서·gap 식별은 *정리/권고* 이며, 구현 entry *발효*·수단 *결정* 은 구현 entry 합의(풀 3+1) + 사용자 명시 의 권한이다. 4축 합의 4건이 각 BLOCKING 을 *권고로 확정* 했으므로, 본 brief 는 그 권고들을 *통합 뷰로 환원* 할 뿐 *발효* 하지 않는다.

---

## 1. 진입 맥락 — 4축 심화 완주 → 통합 정리

```
후속 69 (f29c772) ─ Group I 구현 entry 합의: 진입 적격 + 10 BLOCKING(BI-1~10) + 4 조건부
        │  순서(만장일치): credential(BI-3) → allow-list(BI-1) → anchor(BI-4) → audit(BI-5)
        ▼
후속 71~72  BI-3 credential 격리 + 수단 결정 (BI3-1~8 / CD-1~10)
후속 73     BI-4 external anchor (BI4C-1~5)
후속 75     BI-5 audit sink (BI5C-1~4)
후속 76     BI-1 positive allow-list (BI1C-1~5)  ← 4축 심화 *마지막*
        ▼
후속 77 (본 brief) ─ 4축 BLOCKING 통합 정리 + 구현 entry 발효 readiness 검토
```

- 4축 = G3 provenance check DESIGN(후속 68 발효)의 4 기둥: **positive allow-list(BI-1) ⊕ credential boundary(BI-3) ⊕ external enforcement(BI-4) ⊕ audit sink integrity(BI-5)**. 각 단독 심화 완료.
- 본 brief = 4 합의를 한 뷰로 모아 **(a) 무엇이 남았나(미심화 BLOCKING) (b) 발효 선결 순서·gap (c) 반복된 교차 패턴** 을 정리.

---

## 2. 4축 심화 결과 통합

| 축 | 단위 | 후속 | 판정 | BLOCKING | 핵심 발견 |
|----|----|----|----|----|----|
| credential boundary | **BI-3** | 71~72 | APPROVE w/ COND | BI3-1~8 + CD-1~10 | 4축 공통 선결 전제 / host-bound 물리격리(TPM·SE·YubiKey) 1순위 / docker socket 미마운트·CAP_SYS_PTRACE drop 비협상 / 백업키 역설 |
| positive allow-list | **BI-1** | 76 | APPROVE w/ COND | BI1C-1~5 | default-deny + 판정 입력=fingerprint(author≠판정) / ruleset 단독≠allow-list / **citation stale 0 = 3연속 패턴 단절** |
| external enforcement | **BI-4** | 73 | APPROVE w/ COND | BI4C-1~5 | repo public 확정(plan worst-case 소거) / **self-bypass 역설**(1인=admin=ruleset off) / CI=merge 게이트 direct-push 우회 |
| audit sink integrity | **BI-5** | 75 | APPROVE w/ COND | BI5C-1~4 | Hermes write 불가 + tamper-evident hash chain / CT-4 재귀(매체 속성으로 닫음) / 완전성 FN≠무결성 / **Rekor=audit self-bypass 유일 구조적 해소** |

- **4축 전부 APPROVE WITH CONDITIONS** — 진입 적격이나 각 BLOCKING 해소가 발효 선결.
- **신규 합의 누적 = 39** (Group I entry 34 → 71~72 +2 → 73 +1 → 75 +1 → 76 +1).

---

## 3. 10 BLOCKING 현황 매트릭스

| BLOCKING | 내용 | 우선순위 | 심화 상태 |
|----|----|----|----|
| **BI-3** credential 격리 | 사람 키 Hermes 미주입 + 물리격리 + 백업키 | **1 (최강)** | ✅ 심화 완료 (71~72, 수단 권고까지) |
| **BI-4** external anchor | anchor 실재성 + self-bypass 차단 + plan 확인 | 2 | ✅ 심화 완료 (73, public 확정) |
| **BI-1** positive allow-list | CI fingerprint 대조 실 코드 + workflow read-only | 2 | ✅ 심화 완료 (76) |
| **BI-2** server-side reject | reject = push/merge server-side, `--no-verify` 우회 불가 | 2 | ⚠️ **부분** (BI-1 §6 페어로 흡수, standalone 미작성) |
| **BI-5** audit sink | write 불가 + tamper-evident + CT-4 재귀 | 3 | ✅ 심화 완료 (75) |
| **BI-9** hardware token 백업키 | 1인 lock-out 방지 = 백업 키 2개+ 의무 | 3 | ⚠️ **부분** (BI-3 백업키 역설·CBI3-2 + BI-1 §9(e)로 분산, standalone 미작성) |
| **BI-6** Provider Liquidity | host·CLI·서명 도구 하드코딩 금지 | 4 | ⚠️ **부분** (4축 §11/§12 2층 추상화로 분산, standalone 미작성) |
| **BI-7** observe 면책 | FN="차단 보장 0" + 전환=증거 기반·`agent=user` | 4 | ⚠️ **부분** (BI-5 §6 / BI-1 §11 FN 경계로 분산, standalone 미작성) |
| **BI-8** Phase α↔β observe 라벨 | scanner↔anchor 간극 = 강제 observe 라벨(GA-1) | 4 | ❌ **미심화** (standalone) |
| **BI-10** `.git/` ACL 선행 | Layer 3 `.git/` ACL (commit layer 사각, N-8) | 4 | ⚠️ **부분** (BI-1 §11·BI-5 §8 범위 밖 명시, standalone 미작성) |

- **심화 완료 4 (BI-1/3/4/5) / 부분 5 (BI-2/6/7/9/10) / 미심화 1 (BI-8)**.
- 부분 5건 = 4축 brief 안에 *분산 반영* 됐으나 standalone 정리 미작성 → §8 gap.

---

## 4. ⭐ 교차 패턴 9건 (4축 반복 발견 — 통합의 핵심 가치)

4축 심화에서 *반복적으로* 나타난 패턴 = 4축이 동일 구조 문제를 공유함을 입증:

| # | 패턴 | 출현 축 | 통합 명제 |
|---|----|----|----|
| **CP-1** | **self-bypass 역설** | BI-4(ruleset off)·BI-5(audit policy off)·BI-1(allow-list 키 추가·workflow 수정) | single-host 1인=admin → SoD 구조적 불가 → **에이전트 경로 차단 / owner 경로 = 수용된 SPOF**. 제3자(Rekor)만 owner 경로 구조적 차단 |
| **CP-2** | **binary 입증 (CD-5)** | 4축 전부 | 라벨("켰음") ≠ 입증. **적대적 우회 시연 binary 통과** + 계산적 PoC. agent 경로 한정, owner = SPOF |
| **CP-3** | **재귀 보호** | BI-1(workflow read-only)·BI-4(ruleset token)·BI-5(CT-4 audit credential) | "검사를 정의하는 설정/credential 도 보호 대상" → 무한 후퇴 = **R-I-CONFIG-CHANGE T3(Hermes token 미보유) + §2.5 filesystem 보호**(매체 속성)로 닫음 |
| **CP-4** | **credential(BI-3) = 공통 선결 전제** | BI-1·BI-4·BI-5 모두 BI-3 위에 얹힘 | 미격리 시 4축 전부 명목화 + metadata 대비 순이득 0 + 거짓 안전감 (C2/P2) |
| **CP-5** | **ruleset ↔ CI 보완** | BI-1 §5·BI-4 §5 | ruleset = 서명 *존재*(Hermes 자기 키도 통과) / CI = fingerprint *대조*. 둘 다 필요 |
| **CP-6** | **2층 추상화 (Provider Liquidity)** | BI-4 §7.1·BI-5 BI5R-1·BI-1 §12 | 층1 신뢰 기준 중립(`allowed_signers`/JSONL+JCS+sha256) ⊕ 층2 집행 매체 후보 다수(하드코딩 금지) = BI-6 |
| **CP-7** | **Rekor 3축 1회 도입 시너지** | BI-4 (E)·BI-5 §4·BI-1 §4(gitsign) | Sigstore 인프라 1회 도입 = anchor + audit + allow-list 3축 동시 충족. MVP-6(OIDC 의존 trade-off) |
| **CP-8** | **완전성 FN ≠ 무결성** | BI-5 §6·BI-1 §11 | audit/allow-list *무결성*(기록된 것 정확) ≠ *coverage 완전*(모든 사건 포착). 기록 누락 = BI-7(observe) |
| **CP-9** | **거짓 안전감 차단 = 모든 축 의무** | 4축 전부 | "수단 충족 = 안전 확정 아니라 수용된 SPOF 위 최선"(P2) 명문. CP-1·CP-2와 한 묶음 |

| **CP-10** (IR-6 승격) | **교훈 전파의 불완전성** | BI5C-2 → BI1C-2/3 | BI-5 owner self-bypass 교훈이 BI-1 §9/§10 에 *선제 흡수*되나 §13.2 Rollback·observe 에 **부분 재발**(BI1C-2/3) — "교훈이 박혀도 *전파*가 불완전". 통합 IB-2 가 동일 패턴의 *통합 차원* 재발(§7 readiness 미전파) |

- ⭐ **메타 교훈 (프로세스)**: citation stale 3연속(BI-3 N-2 → BI-4 §11.3 → BI-5 차단조건 #2) → BI-1 에서 **단절**(직접 grep 의무 답습). + **CP-10**(교훈 전파 불완전성)이 BI5C-2→BI1C-2/3→IB-2(통합)로 *세 층위 재발* = 거짓 안전감 차단 교훈이 매 단계 *재명문* 필요(자동 전파 안 됨).

---

## 5. 의존 그래프 (발효 순서 근거)

```
         ┌─────────────────────────────────────────┐
         │  BI-3 credential boundary (선결 전제, CP-4) │  ← 미격리 시 아래 3축 전부 명목화
         └───────────────┬─────────────────────────┘
                         │ (신뢰 키 개인 키 Hermes 외)
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   BI-1 allow-list   BI-4 anchor      BI-5 audit
   (차단 기준)        (차단 위치)       (사후 기록)
   판정=fingerprint   reject=server    write 불가+
        │             -side(BI-2)      tamper-evident
        └──── CP-5 ────┘                    │
        ruleset+CI 보완                       │
                         재귀 보호 (CP-3): ───┘
         workflow(BI-1) / ruleset token(BI-4) / CT-4(BI-5)
         = R-I-CONFIG-CHANGE T3 + §2.5 filesystem
```

- **순서(만장일치 답습)**: credential(BI-3) → allow-list(BI-1) → anchor(BI-4) → audit(BI-5). credential 이 최우선(나머지 3축의 전제), audit 가 마지막(앞 3축 행위 기록).
- **재귀 보호(CP-3)**는 BI-1/4/5 위에 공통으로 얹힘 — workflow·ruleset token·audit credential 이 전부 보호 대상.

---

## 6. 수단 권고 통합 (CN-6 + 교차 패턴)

| 축 | 1순위 수단 (CN-6, 권고·결정 0건) | 신뢰 기준(층1 중립) | 집행/매체(층2) | MVP-6 후보 |
|----|----|----|----|----|
| 축 | 1순위 수단 (CN-6, 권고·결정 0건) | 신뢰 기준(층1 중립) | 집행/매체(층2) | MVP-6 후보 |
| credential | host-bound 물리격리(macOS SE / Linux TPM·YubiKey) — ⚠️ 백업키 역설(IB-3): 가용성↑ ⊕ 기밀성↓·공격표면 N배(BI-3 CBI3-2) | — | TPM/SE/M2 (host OS 종속) | Vault HSM ST-4 |
| allow-list | SSH `allowed_signers` + CI fingerprint 대조 | `allowed_signers` fingerprint | CI / ruleset+CI | gitsign keyless |
| anchor | SaaS ruleset + CI(self-bypass 차단) + **restrict-direct-push/PR-required(IR-2, BI4C-3)** | 서명 *존재* (fingerprint 대조 = allow-list 몫, CP-5 — IR-6) | ruleset / GHES pre-receive | Rekor / 외부 미러 |
| audit | append-only git remote + hash chain | JSONL + JCS + sha256 | git remote / 외부 mount | Rekor / WORM / 분산 |

### 6.1 ⭐ CP-7 = 4단 누적의 *구조적 대안 경로* (IB-2 — 위상 격상, 채택 아님)

CP-7(Sigstore 1회 도입)은 단순 "MVP-6 후보 1개"가 아니라 **4단 누적 발효의 *구조적 대안 경로* 1개**다 — 통합 trade-off 비교(통합 brief 의 책무):

| | (A) 4단 누적 수단 | (B) Sigstore 1회 융합 |
|----|----|----|
| 수단 결정 | 4회 (credential·allow-list·anchor·audit 각각) | credential 1회 + Sigstore 1회 |
| binary PoC | 4축 각각 | credential + 융합 검증 |
| owner self-bypass | **4축 *전부* 영구 잔존**(MVP-6 전까지, CP-1/IB-2) | gitsign(allow-list 신원) + Rekor(anchor (E)+audit) = **3축 owner 경로 동시 구조적 해소**(제3자 삭제 불가) |
| 새 의존 | 없음(기존 git 인프라) | **OIDC IdP 1개**(새 단일 벤더 신뢰 축) |
| credential(BI-3) | 선결 | 선결 *여전*(gitsign 도 OIDC 토큰 격리 필요 → CP-4 안 닫힘) |

- **⭐ 통합 명제**: (A)는 owner self-bypass 를 4축 전부에서 *영구 수용*(MVP-6 전까지)하고, (B)는 OIDC 1개 의존으로 *3축 owner 경로를 동시 해소* 한다. **단 (B) 도 credential(CP-4)은 못 닫음.** trade-off = OIDC 새 신뢰 축 + offline commit 마찰(short-lived cert) + public 메타(이미 public, 한계비용↓).
- **결정·도입 = MVP-6 + 별도 entry 보류** (부록 B 금지 유지). 본 §6.1 = *통합 trade-off 명시*까지, 채택 0건.

### 6.2 Provider Liquidity 긴장 (IR-5)
- ⚠️ **CP-7(Sigstore) ↔ CP-6(2층 중립) 긴장**: Sigstore 시너지가 클수록 **OIDC IdP = 새 단일 벤더 신뢰 축** 도입 → BI5R-1 "audit lock-in > anchor"(과거 기록 전체+genesis+SHA, history rewrite 금지와 충돌)가 Rekor 에 적용.
- → **"투명성 로그가 필요하다 ≠ Rekor 여야 한다"**: 신뢰 기준(층1: 서명 신원·투명성 속성) 중립 유지 + 집행 매체(층2: Sigstore vs **다중 vendor remote 미러 cross-check**[BI5C-4, OIDC 없이 owner 경로 부분 완화] vs WORM vs TSA) 복수 후보. 다중 미러 = Sigstore 의 *PL-안전 대안* 1급 병치.
- **수단 결정 = entry 발효 권한** (CN-6, 본 brief 0건). "신뢰 기준 중립" = "어떤 축도 단일 벤더 토큰/IdP 에 hard-bind 안 함".

---

## 7. ⭐ 구현 entry 발효 readiness 검토

### 7.1 발효 *적격* (Group I 합의 답습)
- single-host MVP 영역(CI provenance step + 사람 키 Hermes 미주입 + GitHub ruleset off-host + append-only git remote audit + observe mode) = **구현 entry 진입 적격** (`f29c772`).

### 7.2 발효 *선결* (미해소 gap — 발효 전 필수)

| 선결 | 내용 | 상태 |
|----|----|----|
| **P-1** credential 수단 결정 | 실제 host OS 확인 후 TPM/SE/M2 결정 고정 + 백업키 정책 (BI-3 / CD-*) — ⚠️ **백업키 역설(IB-3)**: 가용성↑ ⊕ 기밀성↓·공격표면 N배(§6 credential 행 trade-off, BI-3 CBI3-2) | ❌ 미실시 (host OS 미확인) — **최우선** |
| **P-2a** brief 본문 *반영분* | BI1C-1~5 / BI4C-1~5(단 P-2b 별도) / BI5C-1·2·4 / BI1C-* citation·binary·self-bypass | ⚠️ brief 반영, *구현* 미반영 |
| **P-2b** brief 본문 *미반영분* (IR-3) | 원 합의 정정 *대상* = CD-4(서명키≠ST-1)·CD-9(공급망 image digest)·BI5C-3(audit write 주체) 등 | ❌ brief 본문도 미반영 |
| **P-2c** anchor direct-push gate (IR-1, BI4C-3) | required check=merge 게이트 → **restrict-direct-push/PR-required ruleset + G-BI4-6** 결합(없으면 ruleset 있어도 direct push 우회) | ❌ anchor 발효 *독립 선결* |
| **P-3** 미심화 standalone (§8) | BI-2/6/7/8/9/10 정리 — ⚠️ **BI-8(silent scope expansion)·BI-10(`.git/` commit layer 사각=무방비) = 안전 구멍 발효 선결(IB-3)** | ⚠️ 부분/미심화 |
| **P-4** 발효 형태 | observe mode 우선(CBI-3) + 증거 기반 전환(`agent=user`, BI-7) + BI-8 강제 observe 라벨 | ❌ 미정의 |
| **P-5** binary 입증 PoC (CP-2) — ⭐ **축별 종료조건 매핑(IB-4)** | allow-list: **BI1C-1 미서명 reject = ruleset required-signature + CI default-deny 결합**(SSH 단독 아님) + Hermes 키 서명→reject / anchor: **BI4C-2 self-bypass 차단 시연** + direct-push→reject / audit: **BI-5 §10 위조·삭제 시연** / credential: 침투시연 PEN-1~8. "PoC 실시"가 *어떤 축의 무엇*을 입증하는지 명시(CP-2 라벨화 재발 차단) | ❌ 미실시 |

### 7.3 MVP-6 DEFER 경계 (발효 *밖*)
- Vault HSM ST-4 / multi-host mTLS / KMS / distributed audit / hard-block threshold / GHES pre-receive / Rekor / sigstore = **DEFER**(γ-2 답습).

### 7.4 readiness 판정 (검토 — 결정 0건)
- **즉시 발효 비권고**: P-1(credential 수단 결정, host OS 확인 선결) 미실시 + P-5(binary PoC) 미실시 → **순서상 credential 수단 발효(P-1)가 첫 구현 entry**.
- ⚠️ **⭐ owner self-bypass 잔존 명문 (IB-2)**: P-1~P-5 를 *전부 충족해도* **owner(사람) 경로 self-bypass 는 4축 *모두*에서 잔존**(CP-1) — allow-list(임의 키 추가·workflow 수정)·anchor(ruleset off)·audit(append-only 정책 off)·credential(신뢰 키 Hermes 재주입). **이는 single-host 1인=admin SPOF 의 필연 귀결이며, MVP-6(Rekor 제3자) 전까지 *수용된 SPOF*다.** ⭐ **"Rekor/Sigstore MVP-6 DEFER = owner self-bypass 4축 영구 수용 *결정* 동치"**(BI5C-2 d 통합 확대) — 발효 의사결정자는 P-1~P-5 충족이 *에이전트 경로* 차단일 뿐 owner 경로 SPOF 를 *수용하기로 결정*하는 것임을 인지해야 한다(§9 IB-1).
- **2-track 발효 경로 (IR-4)**: *enforce* 는 순차(credential→allow-list→anchor→audit, 의존상 정당) / *observe* 는 의존 없음 → **4축 동시 observe 조기 발효 가능**(행위 데이터 조기 축적). ⚠️ 단 observe 4축 동시 = 부분 격리 그라데이션 거짓 안전감 위험 → **BI-7 면책 라벨(`agent=user` 미충족 = "차단 보장 0") 동반 필수**. audit-first *enforce* 는 비권고(CT-4 재귀가 credential 의존).
- 권고 진입 경로: **(1) credential 수단 발효(host OS 확인 → TPM/SE/M2 결정) → (2) allow-list → (3) anchor → (4) audit**, 각 단계 observe mode 우선 + 축별 binary PoC(P-5).

---

## 8. 미심화 standalone gap (BI-2/6/7/8/9/10)

| BLOCKING | 현 분산 위치 | standalone 필요성 |
|----|----|----|
| **BI-2** server-side reject | BI-1 §6 페어 | 낮음 (BI-1 과 한 차단 경로, 페어로 충분할 수 있음) |
| **BI-6** Provider Liquidity | 4축 §11/§12 2층 추상화 | 낮음 (CP-6 으로 통합됨) |
| **BI-7** observe 면책 | BI-5 §6 / BI-1 §11 FN | **중간** (전환 조건 `agent=user`·증거 기반 = 발효 형태 P-4 와 직결, 별도 정리 가치) |
| **BI-8** Phase α↔β observe 라벨 | — | **높음** (유일 미심화, GA-1 silent scope expansion 차단) |
| **BI-9** hardware 백업키 | BI-3 CBI3-2 / BI-1 §9(e) | 중간 (백업키 정책 = credential 수단 발효 P-1 과 함께) |
| **BI-10** `.git/` ACL | BI-1 §11 / BI-5 §8 범위 밖 | 중간 (Layer 3 = commit layer 사각, BI-1 과 별개 layer) |

- ⚠️ **⭐ "범위 밖" 합집합 = 무방비 (IB-3)**: BI-10 은 BI-1·BI-5 가 *각각* "내 범위 밖"으로 밀어낸 항목 → **두 "범위 밖"의 합집합 = `.git/`(config·hooks·objects) 직접 변조를 *아무 축도 안 보는* commit layer 사각**. 발효 시 `.git/config`·`.git/hooks` 변조 경로가 미차단 → **Layer 3 `.git/` ACL(N-8)을 발효 *선결*로 명문** (분산 ≠ 자동 포함).
- ⚠️ **BI-8 silent scope expansion (IB-3)**: BI-8 미정리 발효 시 scanner(α)가 잡는 것과 anchor(β)가 강제하는 것의 *간극*이 라벨 없이 silent 확장 → "observe 켰으니 다 본다" 거짓 안전감. P-4(발효 형태)의 *선결*.
- → **권고**: BI-8(observe 라벨) + BI-7(observe 면책/전환) 을 "observe mode 통합 정리"로 묶고 P-4 선결로 / credential 수단 발효(P-1) 시 BI-9 백업키 동반(역설 trade-off 포함) / **BI-10 은 별개 layer(Layer 3) = credential 발효에 끼우지 말고 standalone 또는 BI-1 페어**(C 대안4).

---

## 9. 영구 핵심 제약 + 거짓 안전감 메타 교훈

- **⭐ 통합 문서 *고유* 거짓 안전감 차단 (IB-1)**: 본 brief 가 4축·10 BLOCKING·교차 패턴 9건·의존 그래프·readiness 를 한 뷰로 모은 *완결감* 자체가 위험 — **"다 정리했으니/검토했으니 발효해도 된다"** 는 미끄럼. **통합·readiness 검토 행위 자체는 발효 정당성·안전을 부여하지 *않는다*. 통합 = 뷰 환원이지 SPOF 해소가 아니다.** entry "진입 적격 ≠ 안전 확정" 원칙의 *통합 축 대칭* — readiness gap 을 다 봤다는 것이 gap 이 닫혔다는 뜻이 아니다.
- **거짓 안전감 차단(CP-9)** = 4축 통합의 결론: "4축 전부 구현 = 안전 확정"이 아니라 **"수용된 SPOF(single-host 1인=admin) 위 최선"**. owner 경로 self-bypass(CP-1)는 4축 모두에서 잔존 → **제3자(Rekor) MVP-6 전까지 수용. ⭐ Rekor/Sigstore MVP-6 DEFER = owner self-bypass 4축 영구 수용 *결정* 동치(IB-2)** — "전까지 수용"은 절차적 미완이 아니라 *수용하기로 한 결정*이며, 발효 의사결정 위치(§7.4)에 가시화돼야 한다.
- **Hermes ≠ root of trust**: 4축 전부 Hermes 밖 신뢰 경계(CI/anchor/audit/credential 격리). 재귀 보호(CP-3)로 Hermes 자기 무력화 차단.
- **Provider Liquidity(CP-6)**: 신뢰 기준 중립 유지 = vendor lock-in 경감. 5-way 약화 0건.
- **means/ends**: 4축 보장 속성(ends) 명문 + 수단(means) 후보 열거(CN-6, 결정 0건).
- **5 영구 핵심 제약 5/5.**

---

## 10. 합의 형태 (풀 3+1 의무) + 다음 단계

- 본 brief = 4축 보안 BLOCKING 통합 + 발효 readiness → **풀 3+1 의무**.
- Agent A(구현/정합): 의존 그래프·발효 순서·readiness gap 기술. Agent B(보안): 교차 패턴 정확성·거짓 안전감 메타·미심화 gap 위험. Agent C(대안): Rekor 3축 시너지·발효 경로 대안.
- 합의 = **추론적 검증(권고) 한정** — 구현 entry 발효·수단 결정 = 사용자 명시 + 별도 단계.

### 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | 본 brief 승인 → 4축 통합 정리 풀 3+1 합의 | 합의(권고) |
| (B) | ⭐ **credential 수단 발효** (P-1, host OS 확인 → TPM/SE/M2 결정 = 구현 entry 첫 발효) | 구현 entry |
| (C) | 미심화 standalone (BI-8 observe 라벨 / BI-7 observe 면책 / BI-9 백업키) | 별도 brief |
| (D) | 세션 종료 | 메타 |

---

## 부록 A — 답습 출처

| 출처 | 반영 |
|----|----|
| `f29c772` BI-1~10 + CBI-1~4 + N-1 + 우선순위·순서·CN-6 | §3·§5·§6 |
| BI-3 합의(`bf42d0e`/`ead5754` — BI3-*/CD-*) | §2·CP-1·CP-4 |
| BI-4 합의(`bb661f0` — BI4C-1~5) | §2·CP-1·CP-5 |
| BI-5 합의(`f77e488` — BI5C-1~4) | §2·CP-1·CP-7·CP-8 |
| BI-1 합의(`4c5f5f4` — BI1C-1~5) | §2·CP-2·CP-3 |
| G3 4축 DESIGN(`708bc0e`) + hermes-not-root §2.5/R-I-CONFIG-CHANGE T3 | §4 CP-3 |
| ADR-011 §2.1 means/ends | §6·§9 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

수단 결정 고정(credential·allow-list·anchor·audit 매체) / **구현 entry 발효** (실 hook / CI provenance step / GitHub ruleset·required-signature / `.github/workflows/` / credential·서명 키 분리 / audit sink) / `allowed_signers`·hardware key·append-only remote 실 구성 / **sigstore·gitsign·Rekor 도입** / Operational Readiness PASS(Layer E) / Hermes PMO 격상(Layer F) / Vault HSM ST-4(γ-2 DEFER) / threshold 고정 / MVP-1 exit / Phase α defer-lockdown 변경 / **git history rewrite**(후속 74, SHA 붕괴) / G3·ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / 미심화 BLOCKING(BI-2/6/7/8/9/10) standalone 자동 진입 / G1 신규 단위 자동 진입 / tmux·Obsidian docs-scope 도입 / 외부 LLM 응답 강제 채택 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
