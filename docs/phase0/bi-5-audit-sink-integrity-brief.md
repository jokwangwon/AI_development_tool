# BI-5 Audit sink integrity brief — audit 위조·삭제 불가 + 재귀 격리 심화 (DRAFT v2)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 우선순위 마지막(audit) BLOCKING BI-5("audit sink integrity")를 *단독 심화* 하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 audit sink 실 구성(append-only remote / 외부 read-only mount / hash chain 본문) / Evidence Ledger 실 변경 / sigstore·Rekor 도입 / credential·audit token 실 분리 / 실 hook·CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 을 발생시키지 않는다. 본 brief = **audit 정의·기록 대상·무결성 수단 후보·CT-4 재귀 격리·완전성 FN 경계·Evidence Ledger 정합·single-host 한계·binary 입증·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + BI-5 brief 검증 풀 3+1 합의 `f77e488` BLOCKING BI5C-1~4 + 권고 BI5R-1~5 반영 — 본문 반영, 결정 0건)

## v2 변경 이력 (`f77e488` 합의 BLOCKING BI5C-1~4 + 권고 BI5R-1~5 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **BI5C-1** (citation stale) | §7 + §12.1 G-BI5-5 + 부록 A — "ADR-012 차단조건 #2" → **"ADR-012 원칙 5(Hermes 의존 0) + 원칙 3(승인/수정 불가) — ADR-008 차단조건 #2 답습"** 정정 (BI-4 §11.3·BI-3 N-2 동형) |
| **BI5C-2** ⭐ (owner self-bypass 미전파) | §9 + §10 + §12.2 — **owner self-bypass = audit 명목화 현실 경로**(BI-4 역설 audit 대칭) 명문 / §10 binary = 에이전트 경로 한정·owner 경로 = §9 수용 SPOF / §12.2 Rollback owner off 추가 / §9 Rekor=유일 구조적 해소·DEFER=수용 결정 인과 |
| **BI5C-3** (AE write 주체 미명세) | §3 — AE-4(observe 통과)·AE-6(origin replace) **audit write 주체·포착 메커니즘** 명세 + §5 CT-4 재귀 정합 |
| **BI5C-4** (수단표 보강) | §4 — **"owner 경로 방어" 컬럼** 추가(Rekor✅ / remote·mount❌) + **다중 vendor 미러 cross-check §8→§4 1급 후보 격상** |
| BI5R-1 | §11 — audit 매체 2층 추상화(BI-4 §7.1 동형, audit lock-in > anchor) |
| BI5R-2 | §4 — RFC 3161/Roughtime TSA(backdating 차단, MVP-6) |
| BI5R-3 | §4 — Merkle / per-entry signing / WORM 후보 보존 |
| BI5R-4 | §3 — AE-5 격리위반 기록 = §5 CT-4 재귀 의존 명문 |
| BI5R-5 | §7 — Evidence Ledger 통합 = enum #9/#16 중첩 + schema 진화 + blast radius trade-off |
| (기각) | AE-3 "BI-4 §6.2" = 재검증 실재 → 무변경 |
**진입 단위**: Group I 구현 entry 합의 후속 #3 (`f29c772` 합의 §2.2 BI-5 = 구현 순서 **3**·4축 중 audit sink integrity)
**선행 발효 답습**: `e7e4bc1` BI4C-4 redaction + `bb661f0`/`9492193` BI-4 brief·검증 합의 (BI4C-1~5, §8 origin replace → BI-5) + `ead5754`/`bf42d0e`/`cc5b517` BI-3 credential 격리·수단 결정 (CT-4 = BI-3 ∩ BI-5, BI3-8 완전성 FN) + `8e57f7b`/`f29c772` Group I 구현 entry 합의 (BI-1~BI-10 + CBI-1~4 + N-1/N-5) + `708bc0e` G3 provenance check 4축 DESIGN (audit sink integrity = 4축) + ADR-012 Evidence Ledger Protection + G4 JSONL hash chain JCS PoC spec + ADR-011 §2.1 means/ends + hermes-not-root-of-trust-runtime §2.2 (R-I-CONFIG-CHANGE T3 / Hermes audit token 미보유 = C9)
**답습 입력 (1차 권위)**: **`f29c772` 합의 BI-5 정의(write 불가 + tamper-evident hash chain + CT-4 재귀 격리 N-5) + C8(append-only git remote + hash chain single-host ✅·완전 immutable MVP-6) + C9(Hermes audit token 미보유) + CBI-4(Rekor MVP-6 시너지)** + BI-3 brief `bf42d0e` §9 (CT-4 재귀·완전성 FN BI3-8) + BI-4 brief §8 (origin replace 사후 탐지) + ADR-012 §2.3/§2.5/§2.6/§2.7 + G4 PoC spec
**합의 권위 한계**: 본 brief = BI-5 *심화* DRAFT — audit sink 매체 *결정 고정*·hash chain 알고리즘 *고정*·Evidence Ledger 실 변경·sigstore/Rekor *도입 결정*·append-only remote/외부 mount *실 구성* 은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "BI-5 audit sink brief로 진행해줘"

본 brief = 위 명령 답습 — **BI-5(audit sink integrity) 단독 심화** = (i) audit *정의* 재확인(3 무결성 속성) + (ii) audit *기록 대상* 이벤트 enumeration + (iii) 무결성 *수단 후보* 비교(append-only remote / 외부 read-only / 분산 sync / Rekor + hash chain — means/ends, 결정 0건) + (iv) ⭐ **CT-4 audit write credential 재귀 격리**(N-5, BI-3 ∩ BI-5, 무한 후퇴 경계) + (v) ⭐ **완전성 FN 경계**(audit = 위조/삭제 방어 ≠ 기록 누락 = BI-7 소속, BI3-8) + (vi) Evidence Ledger / G4 hash chain / ADR-012 정합(이미 DESIGN) + (vii) origin replace 사후 탐지(BI-4 §8) + (viii) single-host 한계 + (ix) ⭐ **audit 무결성 = binary 입증**(BI4C-2/CD-5 답습) + 진입 gate + 합의 형태 — **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — 구현 순서 마지막(audit), 4축 중 audit sink integrity (§1)
2. BI-5 정의 재확인 — 3 무결성 속성(a Hermes write 불가 / b tamper-evident hash chain / c CT-4 재귀 격리) (§2)
3. audit *기록 대상* 이벤트 enumeration (무엇을 audit 하는가) (§3)
4. ⭐ 무결성 *수단 후보* 비교 (append-only remote / 외부 read-only / 분산 sync MVP-6 / Rekor + hash chain — 결정 0건, CN-6) (§4)
5. ⭐ CT-4 audit write credential 재귀 격리 (N-5, BI-3 ∩ BI-5, 무한 후퇴 경계) (§5)
6. ⭐ 완전성 FN 경계 (audit = 위조/삭제 방어 ≠ 기록 누락[BI-7 소속], BI3-8) (§6)
7. Evidence Ledger / G4 hash chain / ADR-012 정합 (이미 DESIGN → 실 구현 경계) (§7)
8. origin replace/rewrite 사후 탐지 (BI-4 §8 cross-ref) + G4 rewrite defense (§8)
9. single-host 한계 = append-only+hash chain ✅ / 완전 immutable·분산 = MVP-6 DEFER (§9)
10. ⭐ audit 무결성 = binary 입증 (audit "있음" ≠ 충족, 적대적 위조/삭제 시연 실패해야 충족 — BI4C-2/CD-5 답습) (§10)
11. 영구 핵심 제약 + means/ends + Rekor 시너지(CBI-4) (§11)
12. 진입 gate + Rollback Trigger (§12)
13. 합의 형태 (풀 3+1 의무) (§13)
14. 다음 단계 (§14)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **audit sink 실 구성** (append-only git remote 설정 / 외부 read-only mount / 분산 sync / hash chain 본문 / genesis hash / prev_hash 검증 로직)
- ❌ **Evidence Ledger 실 변경** (ADR-012 본문 / JSONL ledger entry 형식 / G4 PoC 코드)
- ❌ **sigstore·Rekor 실 도입** (CBI-4 = 후보 보존, MVP-6 DEFER)
- ❌ **credential / audit write token 실 분리 구성** (CT-4 Hermes 미주입 — BI-3 영역, 결정 = entry 발효)
- ❌ **실 hook 구현** (pre-commit / pre-receive / CI provenance step 본문) / **CI workflow 변경** ([[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **GitHub ruleset / branch protection 변경** / bypass list 변경 (BI-4 영역)
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ **수단 *결정 고정*** (sink 매체 = remote/mount/Rekor / hash chain 알고리즘 — CN-6/means-ends, 결정 = entry 발효)
- ❌ threshold 고정 (observe mode 기간 / audit retention 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6)
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ G3 본문 변경 / ADR-012·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경
- ❌ **git history rewrite** (후속 74 답습 — public + SHA 상호참조 수백 곳 = 금지)
- ❌ 다른 BLOCKING(BI-1/2/3/4/6~10) 자동 진입 / 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. audit 정의·기록 대상·수단 후보·재귀 격리·FN 경계·gate 는 *심화/정비/권고* 이며, audit sink 매체 *결정*·hash chain *고정*·Evidence Ledger 실 변경·Rekor *도입*·실 구성 *발효* 는 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. ADR-012 + G4 PoC spec 이 이미 Evidence Ledger hash chain DESIGN 을 담고 있으므로, 본 brief 는 그 DESIGN 을 *provenance audit sink 의 BI-5 결정 공간으로 환원* 하는 심화일 뿐 *결정* 하지 않는다.

---

## 1. 진입 맥락 — BI-5 = 구현 순서 마지막 · audit sink integrity

```
후속 69 (f29c772) ─ Group I 구현 entry 합의 (BI-1~BI-10, 4축)
        │  순서(만장일치): credential(BI-3) → allow-list(BI-1) → external anchor(BI-4) → audit(BI-5)
        ▼
후속 71~72 (BI-3) ─ credential 격리 brief + 수단 결정 (우선순위 1)
        ▼
후속 73~74 (BI-4) ─ external anchor 실재성 brief + redaction (우선순위 2)
        ▼
후속 75 (본 brief) ─ BI-5 audit sink integrity 단독 심화 (4축 마지막)
```

- **BI-5 = 구현 순서 마지막** (`f29c772` line 86·120: `credential → allow-list → anchor → audit`). audit = 앞 3축의 *행위를 기록·검증* 하는 축 → 앞 3축 위에 얹힘.
- **4축 중 audit sink integrity** (G3 provenance check 4축 = positive allow-list ⊕ credential boundary ⊕ external enforcement ⊕ **audit sink integrity**). audit = "무엇이 일어났는지 위조·삭제 불가하게 기록" 축.
- **인터페이스 (BI-5 가 닿는 곳)**: BI-3(CT-4 audit write credential 재귀, §5) / BI-7(완전성 FN = 기록 누락, §6) / BI-4(origin replace 사후 탐지, §8) / G4·ADR-012(hash chain DESIGN, §7) / CBI-4(Rekor MVP-6 시너지, §11).

---

## 2. BI-5 정의 재확인 — 3 무결성 속성

`f29c772` §2.2 BI-5 (구현 순서 3):

> **audit sink** = Hermes write 불가 + host 침해 tamper-evident(hash chain) + **audit write 자격증명 재귀 격리**(N-5). credential과 별개 축.

| 속성 | 내용 | 본 brief § | 인터페이스 |
|----|----|----|----|
| **(a) Hermes write 불가** | 에이전트(Hermes)가 audit 를 위조/삭제 불가 (CT-4 audit write credential 미보유, C9) | §5 | BI-3 CT-4 |
| **(b) tamper-evident** | host 침해 시에도 변조가 *탐지* 됨 = hash chain (append-only + prev_hash 검증) | §4·§7 | G4 / ADR-012 |
| **(c) CT-4 재귀 격리** | audit write 자격증명도 격리 대상 (N-5, 무한 후퇴 경계) | §5 | BI-3 ∩ BI-5 |

**핵심 명제**: audit sink integrity = "사건을 *위조·삭제 불가* 하게 기록"이 ends. (a)는 *내부자(Hermes)* 위조 차단, (b)는 *host 침해* 변조 탐지, (c)는 (a)를 지키는 credential 자체의 재귀 격리. **단 셋 다 *기록된* 사건 한정 — *기록되지 않은* 사건(observe FN)은 BI-7 소속(§6).**

---

## 3. audit 기록 대상 이벤트 enumeration (무엇을 audit 하는가)

provenance check 시스템(G3 4축)의 audit sink 가 *기록* 해야 하는 사건 (결정 0건 — 후보 enumeration):

| # | 이벤트 | 출처 축 | 비고 |
|---|----|----|----|
| AE-1 | provenance 판정 결과 (pass/reject) + 판정 입력(서명 주체 fingerprint·allow-list 대조) | allow-list(BI-1) | observe/enforce 라벨 포함(BI-8) |
| AE-2 | reject 이벤트 (server-side, --no-verify 우회 시도 포함) | anchor(BI-2/BI-4) | reject = Hermes 밖(BI-2) |
| AE-3 | **R-I-CONFIG-CHANGE** (ruleset/차단 설정 변경) | anchor(BI-4 §6.2) | T3, 사람 명시 |
| AE-4 | observe-mode 통과 사건 (면책 but 기록) | observe(BI-7) | ⚠️ 기록 *누락* = FN(§6) |
| AE-5 | credential/anchor token 관련 사건 (격리 위반 시도 탐지 시) | credential(BI-3) | CT-1~CT-5 |
| AE-6 | origin replace / force-push / history rewrite 감지 | anchor(BI-4 §8) | §8, G4 |

### 3.1 ⭐ audit write 주체·포착 메커니즘 (BI5C-3)

⚠️ **AE write 경로가 CT-4(audit write credential)를 요구하면 §5 재귀와 충돌** → write 주체를 명세해야 한다 (결정 0건, 후보):

| 이벤트 | write 주체 후보 | 포착 메커니즘 | §5 정합 |
|----|----|----|----|
| AE-4 (observe 통과) | **observe sensor**(runtime 항구 sensor, `f29c772` line 152) 또는 CI step | provenance 판정 시점 emit | sensor 는 *판정 입력 미보유*(서명 없음) → CT-4 분리 가능 |
| AE-6 (origin replace) | **외부 watcher / CI step**(별도 fetch + 해시 cross-check) 또는 G4 rewrite defense PoC | 주기 fetch 후 audit↔origin 불일치 비교 | Hermes 밖 → CT-4 무관 |

- **핵심**: audit *write 주체* ≠ Hermes(에이전트). write 주체가 CT-4 를 요구하지 않거나(observe sensor = 판정 입력 미보유), Hermes 밖(CI/watcher)이어야 §5 "Hermes write 불가"와 양립. write 주체 *결정* = entry 발효.

- **기록 형식**: ADR-012 JSONL ledger entry (event 필드 = G4 §4.2 11번째 신규 필드) + hash chain. 형식 = 이미 DESIGN(§7).
- **AE-5 재귀 의존 (BI5R-4)**: AE-5(격리 위반 *탐지* 기록)의 무결성은 §5 CT-4 격리에 **재귀 의존** — host 침해로 CT-4 재유입 시 위반을 audit 에 쓰려 해도 그 audit 가 이미 오염일 수 있음(BI-3 §8.3 부분 격리 그라데이션 동형, §6 완전성 FN 과 별개 = 관측은 했으나 sink 오염). sink 자기참조 명문.
- **범위 경계**: 본 §3 = audit *대상* 후보 enumeration. 어떤 이벤트를 실제 sink 에 쓸지 + write 주체 *결정* = entry 발효 (silent scope expansion 차단).

---

## 4. 무결성 수단 후보 (means 후보 — 결정 0건, CN-6)

**⭐ "owner 경로 방어" 컬럼 (BI5C-4)**: single-host 1인 = audit sink 관리 admin → owner 가 정책을 끌 수 있는가를 *수단별로* 구분(에이전트 경로는 모든 후보가 차단, owner 경로는 후보별 비대칭):

| 후보 | 메커니즘 | 보장 속성(ends) | single-host | **owner 경로 방어** | 비고 |
|----|----|----|----|----|----|
| **append-only git remote** (C 1순위) | 별 remote 에 append-only push (force-push·삭제 거부) | 위조/삭제 불가(remote 측) | ✅ | ❌ (owner 가 remote 정책 변경 가능) | 가장 저비용·기존 git 인프라 재사용 |
| **외부 read-only mount** | sink 를 Hermes 에서 read-only mount (write 불가) | Hermes write 불가 | ✅ | ❌ (owner 가 mount 권한 보유) | (a) 직접 충족, but 외부 writer 필요 |
| **hash chain** (ADR-012/G4, 보강 축) | prev_hash ↔ hash sha256 + RFC 8785 JCS canonical + genesis hash | tamper-evident(변조 탐지) | ✅ (G4 PoC 형식 무결성 ✅) | △ (owner genesis 재생성 가능 — TSA 필요, BI5R-2) | append-only/mount 와 *직교 보강*(둘 다) |
| **⭐ 다중 vendor remote 미러 cross-check** (C N-C4, **1급 후보**) | 別 vendor remote(GitLab/Codeberg 등) push-only 미러 + 주기 해시 cross-check | 미러↔origin 불일치 탐지 | ✅ (무료 plan 2개·즉시) | **△→부분 ✅** (N-vendor *동시* 침해 강제) | owner 1차 remote off 해도 미러 불일치 탐지 — Rekor OIDC 없이 owner 경로 *부분* 완화 |
| **Sigstore Rekor transparency log** (CBI-4) | 제3자 append-only 공개 로그 | 위조/삭제 불가(제3자) | △ (OIDC = GitHub 재사용 가능) | **✅ (제3자 = owner 구조적 삭제 불가)** | BI-4 §3.1 (E) 동일 후보 — **audit self-bypass 를 닫는 유일 구조적 후보**(§9), anchor(E)와 1회 도입 2축 충족. MVP-6 |
| **WORM Object Lock** (C N-C5, COMPLIANCE) | S3-호환 Object Lock retention | root 조차 삭제 불가 | △ (클라우드 소액) | ✅ (retention 기간 root 불가) | SPOF 매체 레벨 닫힘. MVP-6 후보 |
| **분산 sync / distributed audit** | 다중 노드 복제 + 합의 | 완전 immutable | ❌ MVP-6 | ✅ | C8: multi-host = MVP-6 DEFER |
| **RFC 3161 / Roughtime TSA** (C N-C1, 보강) | chain head 주기 외부 타임스탬프 서명 | backdating 차단 | ✅ (무료 공개 TSA) | △ (genesis 재생성 시점 고정) | hash chain *순서*는 보장하나 *backdating* 못 막음 → TSA 보강 (BI5R-2) |
| **Merkle tree** (C N-C2) | hash chain → Merkle root + inclusion proof | O(log n) 부분 증명 | — MVP-6 | — | linear chain O(n) 검증 한계 보완 (BI5R-3) |
| **per-entry signing** (C N-C3) | 각 entry 작성 시점 서명 | entry 작성자 부인 불가 | — | — | ⚠️ Hermes 서명 시 **CT-4 회귀** → *외부 writer* 서명만 의미 (BI5R-3) |

- **means/ends 분리 (ADR-011 §2.1)**: audit *보장 속성*(ends) = "provenance 사건의 위조·삭제 불가 기록 + 사후 검증 가능" / *수단*(means) = 위 후보 (CN-6, 결정 0건). hash chain 은 append-only/mount 와 *경쟁이 아니라 직교 보강*(매체 = 삭제 방어 / hash chain = 변조 탐지).
- **순서 답습**: audit = 4축 마지막 — credential(BI-3)·anchor(BI-4) 위에 얹힘 (CT-4 격리·remote anchor 가 audit 무결성의 전제).

---

## 5. ⭐ CT-4 audit write credential 재귀 격리 (N-5, BI-3 ∩ BI-5)

### 5.1 재귀 구조

- audit "Hermes write 불가"(BI-5 (a))이려면 → **CT-4(audit write credential)가 Hermes 에 없어야** 한다(BI-3 재귀). 즉 CT-4 = **BI-3 ∩ BI-5 교집합** (BI-3 brief §9 답습).
- ⚠️ **무한 후퇴(N-5)**: audit 를 지키는 credential(CT-4)을 격리하면 — 그 격리를 *기록* 하는 audit 가 또 필요하고, 그 audit 의 credential 을 또 격리해야… → 무한 후퇴. **닫힘**: append-only/제3자(Rekor) 매체는 **credential *없이도* 삭제 불가**(remote 정책·제3자 로그) → 재귀를 *매체 속성*으로 끊는다(credential 격리에만 의존하지 않음).
- → **권고(결정 0건)**: audit sink 는 "CT-4 격리"(에이전트 위조 차단) **AND** "매체 자체 append-only/tamper-evident"(credential 무관 삭제 방어) **둘 다** — credential 격리 단독은 무한 후퇴.

### 5.2 BI-3 와의 경계

- CT-4 의 *credential 측면*(Hermes 미주입) = BI-3 영역. CT-4 의 *sink 매체*(append-only/hash chain) = BI-5 고유. 본 brief = BI-5 측 (BI-3 brief §9 silent scope expansion 차단 명문 답습).

---

## 6. ⭐ 완전성 FN 경계 (BI3-8) — audit ≠ 완전

- ⚠️ **CT-4 격리·tamper-evident = audit *위조/삭제* 불가 *한정*.** audit 가 *기록하지 않는* 사건(observe-mode 통과 FN, AE-4)은 사후 대조 시 "정상"으로 보임.
- **이 기록 누락 FN = BI-7(observe 면책) / 부분 BI-5(sink 가 받은 것만 보장) 소속** 이지 audit 무결성으로 닫히지 *않는다*. → **"audit 무결성 = audit 완전" 오용 차단** (BI3-8 답습).
- 즉 audit 는 "기록된 것은 위조 불가"를 보장하지 "모든 사건이 기록됨"을 보장하지 않는다. 완전성(무엇이 기록되어야 하는가)은 sensor(provenance check)의 coverage 문제(BI-7).
- → BI-5 보고서·합의는 이 경계를 명문해야 거짓 안전감("audit 있으니 다 잡힌다") 차단.

---

## 7. Evidence Ledger / G4 hash chain / ADR-012 정합 (이미 DESIGN)

- **ADR-012 (Evidence Ledger Protection)** 이 이미 audit 무결성 DESIGN 보유: §2.3 Append-only + Hash Chain 다층 / §2.5 RFC 8785 JCS canonical(provider-neutral) / §2.6 Genesis Hash / §2.7 prev_hash 검증 실패 = BLOCK + manual + violation entry.
- **G4 JSONL hash chain JCS PoC spec** = Evidence Ledger 무결성 layer 첫 시제 (hash chain + JCS + round-trip). **형식 무결성 한정** (의미적 정확성 = 방어 범위 외 — ADR-012 §11).
- → **BI-5 = 그 DESIGN 의 *provenance audit sink 특화 실 구현 경계*** (재논쟁 0건). 단 ⚠️ **ADR-012 원칙 5("Evidence Ledger = Hermes 의존 0") + 원칙 3("Hermes 가 승인/수정 불가") — 모두 ADR-008 차단조건 #2(JSONL export) 답습** → BI-5 (a)/(c)와 직접 정합(Hermes write 불가·CT-4 재귀). *(BI5C-1: 직전 "ADR-012 차단조건 #2"는 ADR-012 자체 항목 부재 = ADR-008 소속 → 원칙 5/3 으로 정정. BI-4 §11.3·BI-3 N-2 동형.)*
- **경계 + 통합 trade-off (BI5R-5)**: Evidence Ledger(memory/skill 형식 무결성)와 provenance audit sink(commit/provenance 사건 기록)는 *동일 hash chain 인프라 시너지* 이나 *기록 대상*이 다름 — 통합 vs 분리 = entry 결정(본 brief 0건). **통합 시 entry gate 의무 검토**: (i) ADR-012 §2.2 event enum 중첩(#9 `evidence_forgery_detected`·#16 `policy_change_attempted` ↔ AE 사건) → §3.2 schema 진화 절차(MINOR 단축 합의) / (ii) **단일 sink = blast radius 확대**(한쪽 침해 = 양쪽 오염) / 분리 시 = 두 chain 동기화 비용.

---

## 8. origin replace / rewrite 사후 탐지 (BI-4 §8 cross-ref)

- BI-4 §8: anchor(ruleset)가 origin replace(`git remote set-url`)·force-push·history rewrite 로 *범위 밖* 우회됨 → 이를 **BI-5 audit 가 사후 탐지**.
- **수단 cross-ref**: append-only git remote audit sink = remote 교체/rewrite 시 audit↔origin 불일치 탐지 / **G4 rewrite defense**(`g4-history-rewrite-layer5-anchor-poc` / `g4-rewrite-defense-layer234-poc` 선행 PoC = rewrite 방어 4 layer).
- **후속 74 답습**: 이 repo 는 **git history rewrite 금지**(public + SHA 상호참조 수백 곳 붕괴) → audit 는 rewrite 를 *탐지* 하되 BI-5 자신이 rewrite 를 *수행* 하지 않는다(방어 ≠ 실행).

---

## 9. single-host 한계 = append-only+hash chain ✅ / 완전 immutable = MVP-6 DEFER

- **C8 답습**: append-only git remote + hash chain(tamper-evident)까지 = **single-host ✅**. **완전 immutable(분산 audit·다중 노드 합의)= MVP-6**.
- single-host 1인 = audit write 주체 = sink 관리 주체 = admin → BI-3·BI-4 와 동형 SoD 구조적 불가. audit 무결성의 실효 경계: **에이전트(Hermes) 경로 = 차단**(CT-4 격리 + tamper-evident) / **사람 owner 경로 = "수용된 SPOF 위 최선"**(append-only remote 도 owner 가 remote 정책 변경 가능).
- → `f29c772` P2 답습: **"single-host audit 충족 = 안전 확정 아님, 수용된 SPOF 위 최선."**

### 9.1 ⭐ audit self-bypass = audit 명목화의 현실 경로 (BI5C-2, BI-4 역설 audit 대칭)

**BI-4 self-bypass 역설("1인 = repo admin = ruleset off")의 audit 대칭 = "1인 = audit sink 관리 admin = append-only 정책·hash chain 검증 off".** anchor self-bypass(enforcement 시점)는 R-I-CONFIG-CHANGE T3 로 *사람 경로 격하* 가능하나 — **audit self-bypass(owner 가 *과거 기록* 삭제·위조)는 §9 가 "수용된 SPOF"로 포기한 바로 그 지점**이다. → audit 명목화의 가장 현실적 경로.

- **⭐ Rekor = audit self-bypass 를 audit 축에서 닫는 유일 구조적 후보 (BI5C-2 d)**: 제3자(Sigstore) append-only 공개 로그 = **owner 가 구조적으로 삭제 불가**. append-only git remote 는 owner 가 remote 정책을 끌 수 있어 §9 를 닫지 *못한다*(스스로 인정). → **Rekor 를 MVP-6 로 DEFER 하는 것 = "audit self-bypass 를 잔여 수용된 SPOF 로 둔다"는 결정과 *동치***. 이 인과를 명문해야 거짓 안전감 차단(audit 판).
- **audit = 4축 중 self-bypass 를 *부분 완화 가능한* 유일 축 (C)**: anchor·credential 은 owner 권한으로 완전 우회, audit 는 외부 사본으로 *탐지·복원* 가능. 완화 사다리(비용-효과): **다중 vendor 미러(즉시·무료, §4) → Rekor(제3자 구조적) → WORM(root 불가) → TSA(backdating)**. → audit 의 SPOF 를 anchor·credential 과 *동형으로 평탄하게 포기하지 말 것*.

---

## 10. ⭐ audit 무결성 = binary 입증 (BI4C-2 / CD-5 답습)

**직전 BI-4 합의(BI4C-2)와 BI-3 수단 결정(CD-5)의 거짓 안전감 차단 원리를 audit 에도 *대칭 적용*.**

- **audit "있음"(sink 구성됨·hash chain 켜짐) ≠ 충족.** audit 무결성 충족 = **다음 적대적 시연이 *전부 실패* 함이 입증될 때(binary)**:
  - 에이전트가 audit entry *위조* 시도(과거 기록 변조) → **hash chain 검증 실패로 탐지**
  - 에이전트가 audit entry *삭제* 시도 → **append-only/CT-4 미보유로 불가**
  - 에이전트가 audit token 으로 sink 설정 변경 시도 → **CT-4 격리로 실패**
  - host 침해 후 ledger 변조 → **prev_hash 불일치 탐지**(tamper-evident)
- → "append-only remote 설정함 ✅" / "hash chain 켬 ✅" 는 *후보 조건*이지 *충족*이 아니다. **계산적 PoC(G4 hash chain round-trip) + 적대적 위조/삭제 시연** binary 통과해야 충족. CD-5·BI4C-2·ADR-011 §2.1(b) "격리 환경 PoC 실증" 한 묶음.
- ⚠️ **단 §6 경계 유지**: binary 입증은 *위조/삭제 방어* 의 입증 — *기록 누락(완전성 FN)* 은 별개(BI-7). audit binary = "기록된 것의 무결성" binary 이지 "완전성" binary 아님.
- ⚠️ **⭐ binary 입증 = *에이전트(Hermes) 경로* 한정 (BI5C-2 a)**: 위 4 시연은 전부 *에이전트* 주어. **owner(사람) 경로 self-bypass(append-only 정책 off·hash chain 검증 off·과거 기록 삭제)는 binary 입증 *범위 밖* = §9.1 "수용된 SPOF"** (Rekor 제3자 채택 시에만 owner 경로 구조적 차단). → "에이전트 경로 적대적 시연 통과 = audit 무결성 *확정*"으로 미끄러지지 말 것 (BI-4 self-bypass 역설 audit 대칭). audit binary = 에이전트 경로 입증이지 owner 경로 입증 아님.

---

## 11. 영구 핵심 제약 + means/ends + Rekor 시너지

- **means/ends 분리**: audit 보장 속성(ends) = "provenance 사건의 위조·삭제 불가 기록 + 사후 검증 가능" / 수단(means) = append-only remote / 외부 mount / hash chain / Rekor (후보, CN-6, 결정 0건).
- **Hermes ≠ root of trust**: Hermes 는 audit token 미보유(C9·R-I-CONFIG-CHANGE) — 자기 차단책(audit) 무력화 불가.
- **Provider Liquidity 2층 추상화 ([[feedback_provider_liquidity]], BI5R-1)**: BI-4 §7.1 의 2층 직교를 audit 매체에 명시 적용 — **층1 신뢰 기준 = vendor 중립**(JSONL + RFC 8785 JCS + sha256 = ADR-012 §2.5 에서 이미 확보, 어느 매체로 옮겨도 검증 동일) ⊕ **층2 집행 매체 = 후보 다수 열거**(append-only remote / WORM / Rekor / 다중 미러 — *단일 vendor 매체 하드코딩 금지*). ⚠️ **audit 매체 lock-in 이 anchor 보다 무거움**: anchor(ruleset)는 host 교체 시 재설정이나 audit sink 는 *과거 기록 전체* + hash chain genesis + SHA 상호참조가 묶임(후속 74 "git history rewrite 금지"와 충돌) → 층1 중립 유지가 더 중요.
- **Rekor 시너지 (CBI-4)**: Sigstore Rekor 투명성 로그 = append-only 제3자 = BI-4 anchor (E) 후보 ∩ BI-5 audit sink **동일 인프라** — MVP-6 채택 시 anchor+audit 동시 충족 시너지. MVP 비채택·후보 보존.
- **5 영구 핵심 제약 5/5 / Provider Liquidity 5-way 약화 0건.**

---

## 12. 진입 gate + Rollback Trigger

### 12.1 진입 gate (entry 발효 선결)

| Gate | 조건 | 출처 |
|----|----|----|
| G-BI5-1 | BI-3 CT-4 격리 선결 (audit write credential Hermes 외) | §5 / BI-3 |
| G-BI5-2 | sink 매체 = append-only/tamper-evident 둘 다 (credential 격리 단독 = 무한 후퇴) | §4·§5 |
| G-BI5-3 | audit 기록 *대상* 이벤트 확정 (AE-1~6 中 — silent scope expansion 차단) | §3 |
| G-BI5-4 | 완전성 FN = BI-7 소속 명문 ("audit 무결성 ≠ 완전" 거짓 안전감 차단) | §6 |
| G-BI5-5 | Evidence Ledger 정합 (**ADR-012 원칙 5 Hermes 의존 0 + 원칙 3**, ADR-008 차단조건 #2 답습) + 통합/분리 결정(blast radius·schema 진화) | §7 |
| G-BI5-6 | **audit 무결성 = binary 입증** (에이전트 경로 위조/삭제 시연 실패 + G4 hash chain PoC, 라벨 ≠ 충족) | §10 |
| **G-BI5-7** (BI5C-2) | **owner self-bypass 처리 결정** — Rekor(제3자) 채택 시 구조적 차단 / 미채택 시 "audit self-bypass = 잔여 수용 SPOF" 명시 수용 | §9.1 |

### 12.2 Rollback Trigger (audit 명목화 감지)

- append-only remote 가 force-push 허용으로 변경 → 삭제 방어 무력화 (audit alert 재귀).
- hash chain 검증 비활성화 / genesis hash 변경 → tamper-evident 상실.
- CT-4(audit write credential)가 Hermes 호스트 재유입 → §5 위반.
- audit 기록 대상에서 이벤트 누락(coverage 축소) → §6 FN 확대.
- **⭐ owner self-bypass (BI5C-2 b)**: owner 가 append-only remote 정책 off / hash chain 검증 비활성화 / 다중 미러 cross-check 중단 → **audit self-bypass(§9.1) 재개방** = audit 명목화. (단 owner 경로는 §10 binary 범위 밖 = 수용된 SPOF — Rekor 채택 시에만 구조적 차단.)

---

## 13. 합의 형태 (풀 3+1 의무)

- BI-5 = 보안 BLOCKING(4축 마지막) + Evidence Ledger(ADR-012) 정합 → **풀 3+1 의무** (Reviewer-only 부적격).
- Agent A(구현/정합): hash chain·append-only remote 기술 실현성 + Evidence Ledger 정합 + AE 이벤트 coverage. Agent B(보안): CT-4 재귀·완전성 FN·binary 입증·거짓 안전감. Agent C(대안): Rekor/분산 audit/외부 mount + Provider Liquidity.
- 합의 = **추론적 검증(권고) 한정** — sink 매체 결정·hash chain 고정·Evidence Ledger 변경·Rekor 도입·실 구성 = 사용자 명시 + 별도 단계.

---

## 14. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | 본 brief 승인 → BI-5 검증 풀 3+1 합의 | 합의(권고) |
| (B) | 다른 BLOCKING 심화 (BI-1 CI fingerprint) | 별도 brief |
| (C) | credential 수단 *발효* (BI-3 후속, host OS 확인 후) | 구현 entry |
| (D) | 4축 BLOCKING 통합 정리 (BI-3/4/5 완주 후 구현 entry 발효 검토) | 통합 |
| (E) | 세션 종료 | 메타 |

---

## 부록 A — 답습 출처

| 출처 | 본 brief 반영 |
|----|----|
| `f29c772` Group I 구현 entry 합의 BI-5 (3 속성) + C8/C9 | §2 정의 / §9 single-host |
| `f29c772` N-5 (audit write credential 재귀, Agent C) | §5 |
| `f29c772` CBI-4 (Rekor MVP-6 시너지) | §4·§11 |
| `bf42d0e` BI-3 brief §9 (CT-4 = BI-3 ∩ BI-5, 완전성 FN BI3-8) | §5·§6 |
| `9492193` BI-4 brief §8 (origin replace → BI-5) + BI4C-2 (binary 입증) | §8 / §10 |
| ADR-012 Evidence Ledger Protection §2.3/§2.5/§2.6/§2.7 + 원칙 5·3 (ADR-008 차단조건 #2 답습) | §7 |
| `g4-jsonl-hash-chain-jcs-poc-spec` + G4 rewrite defense PoC | §7 / §8 |
| ADR-011 §2.1 means/ends + §2.1(b) PoC 실증 | §4·§10·§11 |
| hermes-not-root-of-trust-runtime (Hermes audit token 미보유 C9) | §2·§11 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

audit sink 실 구성 (append-only git remote 설정 / 외부 read-only mount / 분산 sync / hash chain 본문 / genesis hash / prev_hash 검증 로직) / **Evidence Ledger 실 변경** (ADR-012 본문 / JSONL ledger entry / G4 PoC 코드) / **sigstore·Rekor 실 도입** (CBI-4 DEFER) / **credential·audit write token 실 분리** (CT-4 — BI-3 영역) / **실 hook 구현** (pre-commit / pre-receive / CI provenance step) / **CI workflow 변경** / **GitHub ruleset·bypass 변경** (BI-4 영역) / Hermes runtime·upstream 변경 / 수단 결정 고정 (sink 매체·hash chain 알고리즘 — CN-6) / threshold 고정 (observe 기간·retention) / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 변경 / ADR-012·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / **git history rewrite** (후속 74 답습 — SHA 붕괴) / 다른 BLOCKING(BI-1/2/3/4/6~10) 자동 진입 / Backlog #4 자동 진입 / tmux·Obsidian docs-scope 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
