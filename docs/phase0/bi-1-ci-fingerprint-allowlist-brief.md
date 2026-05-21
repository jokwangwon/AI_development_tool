# BI-1 CI fingerprint allow-list brief — positive allow-list 차단 기준 심화 (DRAFT v2)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 우선순위 2 BLOCKING BI-1("CI provenance step = fingerprint allow-list 실 대조 코드")를 *단독 심화* 하는 brief 한정** (G3 4축 中 *positive allow-list* 축 = 차단 *기준*, 4축 심화의 마지막). 본 brief 의 어떤 §도 그 자체로 CI provenance step 실 코드 / `.github/workflows/` 변경 / SSH `allowed_signers` 파일 구성 / GitHub ruleset·required-signature 변경 / 실 hook / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 을 발생시키지 않는다. 본 brief = **allow-list 정의·매체 후보·CI 대조 실 코드 경계·BI-2 페어·workflow read-only 재귀·credential 선결·owner self-bypass·binary 입증·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v2** (v1 + BI-1 brief 검증 풀 3+1 합의 `4c5f5f4` BLOCKING BI1C-1~5 + 권고 BI1R-1~6 반영 — 본문 반영, 결정 0건)

## v2 변경 이력 (`4c5f5f4` 합의 BLOCKING BI1C-1~5 + 권고 BI1R-1~6 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **BI1C-1** (§10 미서명 reject = ruleset 결합) | §10 시연 #2 — 미서명 reject = SSH `allowed_signers` *단독* 아님, **ruleset required-signature + CI default-deny 결합** (§5 cross-ref 배선) |
| **BI1C-2** ⭐ (§13.2 Rollback owner/능동감지) | §13.2 — **owner 경로 bullet + 능동 감지(fingerprint→author 회귀테스트 FAIL)** 추가 (BI-5 §12.2 대칭, BI5C-2 부분 재발 차단) |
| **BI1C-3** (observe FN 미전파) | §10 + §11 + §13.2 — observe mode = enforcement 미발효·신호만 → "binary 통과 ≠ 차단 입증" 다층 명문 |
| **BI1C-4** (§9 (d)(e) 누락) | §9 — (d) 신뢰 키 개인 키 Hermes 재주입(§8 역경로) + (e) 백업 키(BI-9) 노출 추가 |
| **BI1C-5** (gitsign §4 누락) | §4 — **sigstore/gitsign keyless 행 병치**(채택 아님·MVP-6) + N-1/CBI-4 cross-ref + 3축 1회 도입 시너지 |
| BI1R-1 | §7 — N-4 재귀 닫힘 = BI-2 server-side anchor 결합까지 명문 |
| BI1R-2 | 부록 A — 정합 노이즈 주석(합의 doc 360/784 vs brief 360/448) + citation stale 0 positive |
| BI1R-3 | §3 — 서명 scope(commit 객체 전체·author 변경 시 무효·replay 방어) |
| BI1R-4 | §11 — coverage 경계(merge/squash/force-push) |
| BI1R-5 | §10 — CI reject ↔ required status check 배선 시연 |
| BI1R-6 | §4 — SSH CA·GHES pre-receive·in-toto 후보 보존 + GPG 폐기/만료 trade-off |
**진입 단위**: Group I 구현 entry 합의 후속 #4 (`f29c772` 합의 §2.2 BI-1 = 우선순위 **2**·positive allow-list 축, BI-2 페어) — **4축 심화의 마지막** (BI-3 credential 후속 71~72 / BI-4 anchor 후속 73 / BI-5 audit 후속 75 완주)
**선행 발효 답습**: `27c188f`/`ae4c091`/`f77e488` BI-5 audit sink (BI5C-2 owner self-bypass·binary 입증 답습) + `9492193`/`bb661f0` BI-4 anchor (§5 ruleset↔CI 보완·BI4C-2 binary) + `ead5754`/`bf42d0e` BI-3 credential (4축 공통 선결 전제) + `8e57f7b`/`f29c772` Group I 구현 entry 합의 (BI-1/BI-2 + C3 + N-4) + `708bc0e` G3 provenance check 4축 DESIGN (positive allow-list·author 판정 입력 아님 = 후속 68 발효 본문 line 360/448/789/1127) + hermes-not-root-of-trust-runtime §2.5 #2(`.github/workflows/` 보호)·§2.2 #20·line 460(BI-2 anchor) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **`f29c772` BI-1 정의(fingerprint allow-list 실 대조 코드 + Hermes 밖 신뢰 경계 + §2.5 #2 workflow read-only 의존) + BI-2(reject = server-side, `--no-verify` 우회 불가) + C3(allow-list ≠ ruleset 단독) + N-4(workflow read-only 의존 미명시, 높음) + CN-6 수단(SSH `allowed_signers` 1순위 / GPG 후순위 / ruleset+CI)** + G3 본문 line 360/448/789 + §2.5 #2(line 221)
**합의 권위 한계**: 본 brief = BI-1 *심화* DRAFT — allow-list 매체 *결정 고정*·SSH `allowed_signers` *채택*·CI provenance step 실 코드·`.github/workflows/` 변경·ruleset required-signature 설정 은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "BI-1 CI fingerprint brief로 진행해줘"

본 brief = 위 명령 답습 — **BI-1(positive allow-list / CI fingerprint 대조) 단독 심화** = (i) allow-list *정의* 재확인(positive allow-list = 차단 기준, default-deny, NOT single-author detection — G3 후속 68 교정) + (ii) ⭐ 판정 입력 = **signature fingerprint** (author/committer = 판정 입력 아님·audit 사후 대조 전용) + (iii) allow-list *매체 후보*(SSH `allowed_signers` / GPG / ruleset+CI — means/ends, 결정 0건) + (iv) ⭐ ruleset ↔ CI 보완(C3, ruleset=서명 존재만→fingerprint 대조 별도) + (v) ⭐ **BI-1 ↔ BI-2 페어**(판정 vs 집행, reject=server-side) + (vi) ⭐ **workflow read-only 재귀**(N-4, §2.5 #2 선결) + (vii) credential 격리(BI-3) 선결 + (viii) ⭐ **owner self-bypass**(BI5C-2 답습) + (ix) ⭐ **allow-list 실효 = binary 입증** + 완전성 FN 경계 + single-host 한계 + 진입 gate + 합의 형태 — **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — BI-1 = positive allow-list 축(차단 *기준*), 4축 심화의 마지막 (§1)
2. BI-1 정의 재확인 — CI fingerprint allow-list 실 대조(0-구현 아님) + Hermes 밖 실행 + workflow read-only 의존 (§2)
3. ⭐ positive allow-list = 차단 기준(default-deny) + 판정 입력 = fingerprint(author ≠ 판정 입력, G3 후속 68 교정) (§3)
4. allow-list *매체 후보* 비교 (SSH `allowed_signers` / GPG / ruleset+CI — 결정 0건, CN-6) (§4)
5. ⭐ ruleset ↔ CI 보완 (C3, BI-4 §5 cross-ref) (§5)
6. ⭐ BI-1 ↔ BI-2 페어 (판정 vs 집행, reject=server-side, `--no-verify` 우회 불가) (§6)
7. ⭐ workflow read-only 재귀 (N-4, §2.5 #2 선결 — anchor/audit 재귀와 동형) (§7)
8. ⭐ credential 격리(BI-3) 선결 (미격리 시 allow-list = metadata detection 동일 FN 붕괴, line 789) (§8)
9. ⭐ owner self-bypass (allow-list 에 임의 키 추가·workflow 수정 — BI5C-2 답습) (§9)
10. ⭐ allow-list 실효 = binary 입증 (에이전트 + owner 경로 분리, BI4C-2/CD-5/BI5C-2 선제 답습) (§10)
11. 완전성 FN 경계(BI-7) + `.git/` 직접 변조 = 범위 밖(BI-10/filesystem ACL) (§11)
12. single-host 한계 + 영구 핵심 제약 + means/ends + Provider Liquidity 2층 (§12)
13. 진입 gate + Rollback Trigger (§13)
14. 합의 형태 (풀 3+1 의무) + ⭐ 4축 심화 완주 (§14)
15. 다음 단계 (§15)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **CI provenance step 실 코드** (fingerprint 추출·`allowed_signers` 대조·pass/reject 로직 본문)
- ❌ **`.github/workflows/` 변경** (provenance step / actual run / workflow_dispatch / `on.push.paths` 필터 — [[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **SSH `allowed_signers` 파일 구성** / GPG keyring / 서명 키 등록 (수단 결정 = entry)
- ❌ **GitHub ruleset / required-signature / branch protection 변경** (BI-4 영역)
- ❌ **실 hook 구현** (pre-commit / pre-receive / server-side) / **filesystem ACL** (`.github/workflows/` read-only — §2.5 #2, BI-10 영역)
- ❌ **credential / 서명 키 실 분리 구성** (CT-1~CT-5 — BI-3 영역, allow-list 선결 전제이나 본 brief 0건)
- ❌ Hermes runtime / Hermes upstream 변경
- ❌ **수단 *결정 고정*** (allow-list 매체 = SSH/GPG/ruleset — CN-6/means-ends, 결정 = entry 발효)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / **Vault HSM ST-4** (γ-2 DEFER)
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ G3 본문 변경 (line 360/448/789/1127 4축) / ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경
- ❌ **git history rewrite** (후속 74 답습 — public + SHA 상호참조 수백 곳 = 금지)
- ❌ 다른 BLOCKING(BI-2~BI-10) 자동 진입 / G1(PR·approval auto-reject) 신규 단위 / 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. allow-list 정의·매체 후보·CI 대조 경계·페어·재귀·선결·gate 는 *심화/정비/권고* 이며, allow-list 매체 *결정*·`allowed_signers` *채택*·CI 실 코드·workflow·ruleset 실 변경 *발효* 는 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. G3 본문(후속 68 발효)이 이미 positive allow-list DESIGN(line 360/448/789)을 담고 있으므로, 본 brief 는 그 DESIGN 을 *BI-1 결정 공간으로 환원* 하는 심화일 뿐 *결정* 하지 않는다.

---

## 1. 진입 맥락 — BI-1 = positive allow-list 축 (차단 기준) · 4축 심화 마지막

```
후속 69 (f29c772) ─ Group I 구현 entry 합의 (BI-1~BI-10, 4축)
        │  순서(만장일치): credential(BI-3) → allow-list(BI-1) → external anchor(BI-4) → audit(BI-5)
        ▼
후속 71~72 BI-3 credential ✅ / 후속 73 BI-4 anchor ✅ / 후속 75 BI-5 audit ✅
        ▼
후속 76 (본 brief) ─ BI-1 positive allow-list 단독 심화 (4축 심화 *마지막*)
```

- **BI-1 = allow-list 축 = 차단 *기준*** (`f29c772` line 120: "allow-list 정의(차단 *기준*)"). credential(누가 키를 가지나) 위에서 **누구를 신뢰하나(차단 기준)** 를 정의. anchor(어디서 차단)·audit(무엇을 기록)의 *판정 근거*.
- **BI-1 ↔ BI-2 페어** (`f29c772` 둘 다 우선순위 2): BI-1 = *판정*(fingerprint allow-list 대조) / BI-2 = *집행*(reject server-side). §6.
- **4축 심화 완주**: 본 brief 로 BI-3(credential)·BI-4(anchor)·BI-5(audit)·**BI-1(allow-list)** 4축 단독 심화 완료 → 다음 = 4축 통합 정리·구현 entry 발효 검토 (§14/§15).

---

## 2. BI-1 정의 재확인 — CI fingerprint allow-list 실 대조

`f29c772` §2.2 BI-1 (우선순위 2):

> **CI provenance step** = fingerprint allow-list 실 대조 코드(**0-구현 아님**) + Hermes 밖 신뢰 경계 실행 + **§2.5 #2 workflow read-only 의존 명시**.

| 요소 | 내용 | 본 brief § | 인터페이스 |
|----|----|----|----|
| (a) fingerprint allow-list 실 대조 | commit 서명 fingerprint ↔ allow-list 비교 = **실 코드**(0-구현 아님) | §2·§4 | C1/C3 |
| (b) Hermes 밖 신뢰 경계 실행 | CI step = GitHub Actions runner(Hermes 밖) — 에이전트 변조 불가 | §6 | BI-2 |
| (c) §2.5 #2 workflow read-only 의존 | CI workflow yaml 이 보호 안 되면 무력화 → §2.5 #2(`.github/workflows/`) 선결 | §7 | N-4 |

**핵심 명제 (C1)**: "single-host 구현 *가능* 하나 0-구현 아님" — ruleset 만으로는 안 되고 **fingerprint 대조 실 코드**가 필요(§5). BI-1 = 그 실 코드의 *판정 기준·실행 경계·재귀 보호* 정비.

---

## 3. ⭐ positive allow-list = 차단 기준 (default-deny) + 판정 입력 = fingerprint

### 3.1 positive allow-list (G3 후속 68 교정 발효)

- G3 본문 line 360/448 (후속 68 발효): **"Hermes-originated commit = positive allow-list 미통과 → default-deny"** + **"author/committer 메타 = 판정 입력 *아님*·audit 사후 대조 전용 (단일 author 비교 아님)"**.
- ⭐ **이것이 G3 결함 교정(후속 64~68)의 핵심**: 구 설계 = "single-author detection"(author 필드로 판정 — 위조 가능) → 교정 = **positive allow-list of *signature fingerprint*** (default-deny, 신뢰 키 목록에 없으면 거부).
- **판정 입력 = 암호학적 서명 fingerprint** (author/committer 필드 ≠ 판정 입력, 위조 가능하므로). author 는 *audit 사후 대조* 전용(BI-5 AE-1).

### 3.2 default-deny 의 함의

- allow-list 에 *있는* fingerprint = 통과 / *없으면* = 거부(미서명·Hermes 키 서명·미등록 키 전부 default-deny).
- → **Hermes-originated commit 거부** = Hermes 키가 allow-list 에 *없으므로*(또는 미서명) 자동 default-deny. "Hermes 인지 탐지"가 아니라 "신뢰 목록 외 전부 거부".
- 방향성: **FN 우선 > FP** (의심 시 quarantine — line 789, observe mode 답습).
- **서명 covered scope + replay 방어 (BI1R-3)**: SSH/GPG 서명은 **commit 객체 전체(tree + parent + author + committer + message)를 덮음** → author/committer 만 변경(cherry-pick·rebase 위조)하면 **서명 무효화 → reject**. 단 *동일 서명 commit 재배치(replay)*는 commit SHA(parent 포함) 유일성에 의존하므로 — fingerprint 대조 단독이 replay 를 완전 차단하진 않음(parent 가 다르면 SHA 다름 → 사실상 다른 commit). replay 방어 = commit SHA 체인(BI-5 hash chain/audit cross-ref).

---

## 4. allow-list 매체 후보 (means 후보 — 결정 0건, CN-6)

| 후보 | 메커니즘 | fingerprint 대조 | 비고 |
|----|----|----|----|
| **SSH signed commit + `allowed_signers`** (1순위, 만장일치) | git SSH 서명 + `allowed_signers` 파일 = allow-list 매체 | CI 가 `git verify-commit` / `ssh-keygen -Y verify` 로 signer fingerprint ↔ `allowed_signers` 대조 | **vendor 중립**(어느 host/CI 에서도 동일, BI-4 §7.1 층1) |
| **GPG signed commit** (후순위) | GPG 서명 + keyring | CI 가 GPG fingerprint 대조 | 키 관리 복잡·후순위(만장일치). ⚠️ trade-off(BI1R-6): GPG = `allowed_signers` 대비 *성숙한 폐기/만료 인프라*(웹오브트러스트·revocation) 보유 — 후순위는 *운영 복잡도* 사유이지 보안 열위 아님 |
| **ruleset required-signature + CI** | ruleset = 서명 *존재* require + CI = fingerprint 대조 | ruleset 단독 = 서명 존재만(§5) → CI 보완 필수 | BI-4 anchor 와 결합 |
| **⭐ sigstore/gitsign keyless** (BI1C-5, **후보 보존·채택 아님·MVP-6**) | OIDC 신원(GitHub 계정) 기반 keyless 서명 + Fulcio 단명 인증서 + Rekor 기록 | allow-list 기준 = *정적 키 fingerprint* → **OIDC 신원**(예: `user@github`)으로 이동 | ⭐ (a) 정적 키 목록 관리 부담 0 → §9 "`allowed_signers` 임의 키 추가" 표면이 "OIDC 신원 위조"로 *대체*(난이도↑) (b) GitHub 계정 재사용 (c) **Rekor 투명성 로그로 allow-list 판정 자체 audit** → **anchor(BI-4 §3.1 (E)) + audit(BI-5 §4) + allow-list(BI-1) 3축 1회 도입 시너지**. trade-off: OIDC IdP 새 의존 축(Provider Liquidity §12)·인증서 단명성(오프라인 commit 마찰)·public 메타(public repo 라 완화). N-1/CBI-4 cross-ref |
| **SSH CA 서명** (BI1R-6, 후보 보존) | `allowed_signers` `cert-authority` = 개별 키 대신 CA 키 1개 등록 | CA 서명 단명 인증서 신뢰 | 정적 목록 rotation 부담↓. ⚠️ CA 개인 키 = *새 SPOF*(BI-3 격리 대상 회귀) |
| **GHES pre-receive 서버측 판정** (BI1R-6, MVP-6) | fingerprint 대조 *판정*을 server-side hook 에서 수행 | CI 밖 → §7 workflow 재귀 *구조적 회피* | SaaS GitHub 불가 = GHES 전제, MVP-6 경로 |
| **in-toto / SLSA attestation** (BI1R-6, MVP-6) | commit 단위 → 빌드/단계 provenance 체인 | commit-layer(§11) 범위 밖 = 행위 체인 | 후보 공간 완전성 보존 |

- **fingerprint 대조 = 실 코드(0-구현 아님)**: allow-list 매체가 무엇이든 — CI step 이 commit 서명에서 signer fingerprint 를 추출하고 allow-list 와 대조하는 **실제 코드**가 필요(C1). 이 코드 = BI-1 의 핵심 실 구현 (entry 발효 영역).
- **means/ends 분리 (ADR-011 §2.1)**: allow-list 보장 속성(ends) = "신뢰 fingerprint 외 commit 은 차단됨" / 수단(means) = SSH `allowed_signers` / GPG / ruleset+CI (CN-6, 결정 0건). **신뢰 기준 = vendor 중립**(BI-4 §7.1 층1, allowed_signers).

---

## 5. ⭐ ruleset ↔ CI 보완 (C3 — ruleset 단독 ≠ allow-list)

`f29c772` C3 (만장일치): **positive allow-list ≠ ruleset 단독.**

| 축 | ruleset (required-signature) | CI provenance step (BI-1) |
|----|----|----|
| 검증 대상 | 서명 *존재* (require signed commits) | signer fingerprint **allow-list 대조** (누가 서명했나) |
| 한계 | ⚠️ **Hermes 자기 키 서명도 통과** (서명만 있으면 OK) | fingerprint 가 allow-list 인지 판별 → Hermes 키(미등록) reject |
| 단독 gap | Hermes 키 서명 commit 못 거름 | CI 미연결 시 merge 강제 안 됨(BI-2) |
| 보완 결합 | ruleset = 서명 require + **CI required check 지정** | CI = fingerprint 대조 결과를 required status |

→ **결론 (C3)**: allow-list 실효 = ruleset(서명 존재) **AND** CI(fingerprint 대조) 둘 다. BI-4 §5 와 동일 명제(anchor 측에서도 동일). ruleset 단독 = Hermes 자기 키 서명 통과 = 명목 allow-list.

---

## 6. ⭐ BI-1 ↔ BI-2 페어 (판정 vs 집행)

| | BI-1 (판정) | BI-2 (집행) |
|---|----|----|
| 역할 | fingerprint allow-list 대조 → pass/reject *신호* | reject 를 push/merge 전 *차단 보장* |
| 위치 | CI provenance step (Hermes 밖 runner) | server-side (ruleset required check / GHES pre-receive) |
| 핵심 | "누구를 신뢰하나" 판정 | **`--no-verify` 우회 불가** (Hermes 밖 anchor, line 460) |
| 단독 gap | 판정해도 집행 안 되면 무의미 | 집행해도 판정 기준 없으면 무의미 |

- **G3 line 460 답습**: "runtime = provenance sensor 신호 생성(pre-commit hook 등 = 수단 후보 — *차단권 아님*); 최종 reject = Hermes 밖 anchor; 차단 보장 = push/merge 전." → **runtime sensor 단독 의존 금지**(line 328: `--no-verify` 우회되어도 최종 reject = Hermes 밖 anchor).
- BI-1(판정) 은 sensor 신호, BI-2(집행) 가 anchor 차단 = BI-4 anchor 와 결합. → BI-1·BI-2·BI-4 는 한 차단 경로(판정→집행→anchor 위치).

---

## 7. ⭐ workflow read-only 재귀 (N-4, §2.5 #2 선결)

- ⚠️ **N-4 (높음)**: CI provenance step 은 `.github/workflows/*.yml` 에 정의됨 → **Hermes 가 workflow yaml 을 수정하는 commit 으로 allow-list 대조 자체를 무력화** 가능(검사를 끄거나 항상 pass 로 변조).
- → **§2.5 #2 (`.github/workflows/` 보호) 선결** (hermes-not-root-of-trust-runtime line 221: §2.5 #2 = `.github/workflows/*.yml` T3 + git pre-commit hook + Hermes-originated commit auto-reject). workflow = allow-list 검사의 *메타 보호 대상*.
- **재귀 구조 (anchor/audit 동형)**: BI-4 §6.2(ruleset 변경 token 격리)·BI-5 §5(audit write credential 재귀)와 동형 — **검사를 정의하는 설정(workflow)도 보호 대상**. 무한 후퇴 닫힘 = workflow 변경 = R-I-CONFIG-CHANGE T3(Hermes token 미보유) + §2.5 #2 filesystem 보호.
- TM-6 답습(line 273): "Hermes 가 `.github/workflows/` 본문 변경 또는 `--no-verify` flag PR 자동 머지" = §2.6.3(b) + §2.5 #2 다중 보호.
- ⚠️ **재귀 닫힘 = BI-2 server-side anchor 결합 필수 (BI1R-1)**: §2.5 #2 의 강제 메커니즘(line 221)은 "git pre-commit hook + Hermes-originated commit auto-reject" — pre-commit hook 은 §6 논리(`--no-verify` 우회 가능 = 차단권 아님)에 따라 *sensor 신호일 뿐*이다. 따라서 workflow 보호의 진짜 닫힘 = **§2.5 #2(filesystem 신호) + BI-2 server-side anchor(workflow 변경 commit 자체를 push/merge 전 reject)** 결합. pre-commit 단독 = 명목. (대안: GHES pre-receive 서버측 판정 = workflow 재귀 *구조적 회피*, §4 BI1R-6.)

---

## 8. ⭐ credential 격리(BI-3) 선결 — 미격리 시 allow-list 붕괴

- **line 789 답습**: "auto-reject 의 *기준* = positive allow-list (default-deny, author 비교 아님). SPOF 핵심 위험(사용자=Hermes 동일 credential 공유)은 credential boundary 실분리가 *선결 전제* — **미격리 시 allow-list 도 metadata detection 과 동일 FN 으로 붕괴 + *거짓 안전감* 추가**."
- → **BI-1 allow-list 는 BI-3 credential 격리 위에 얹힘** (4축 공통 선결 전제, Group I 합의 핵심). Hermes 가 사람 서명 키를 보유하면 — allow-list 에 *있는* 키로 서명 가능 → allow-list 가 명목화(Hermes commit 이 통과).
- 즉 allow-list 의 실효 = "신뢰 fingerprint 의 *개인 키* 가 Hermes 에 없음"(BI-3 CT-1/CT-3)에 의존. **미격리 allow-list = metadata detection 과 동일 FN + 거짓 안전감**(순이득 0, C2/P2).

---

## 9. ⭐ owner self-bypass (BI5C-2 답습)

**BI-4 self-bypass 역설·BI-5 audit self-bypass 의 allow-list 대칭** ("1인 = repo admin = allow-list 에 임의 키 추가 / workflow 수정 / required check 해제"):

- single-host 1인 owner = allow-list 관리 admin → owner self-bypass 경로(allow-list 명목화):
  - (a) allow-list 에 Hermes 키 추가
  - (b) workflow 에서 대조 step 제거
  - (c) CI required check 해제
  - **(d) 신뢰 키 *개인 키* 를 Hermes 환경에 (재)주입 (BI1C-4 — §8 credential 선결의 *역경로*)** = allow-list 에 *있는* 키로 Hermes 가 서명 가능 → 가장 직접적 명목화(BI-3 CT-1/CT-3 owner 측 우회)
  - **(e) hardware key 백업 키(BI-9) 노출 (BI1C-4)** = 백업 키 중 하나가 Hermes 접근 가능 환경에 있으면 (d)와 동형 명목화 (백업 키 역설 = 가용성↑ ⊕ 공격 표면 N배, BI-3 CBI3-2 답습)
- **실효 경계**: allow-list 의 차단력은 **에이전트(Hermes) 경로** 한정(Hermes 키 미등록 + workflow read-only). **사람 owner 경로((a)~(e)) = "수용된 SPOF 위 최선"** (BI-4·BI-5 §9 동형).
- → owner self-bypass = allow-list 명목화의 현실 경로 (BI5C-2 답습 — §10 binary 에서 명문, §13.2 Rollback 에서 감지 경계).

---

## 10. ⭐ allow-list 실효 = binary 입증 (BI4C-2/CD-5/BI5C-2 선제 답습)

**직전 3 합의(BI-3 CD-5·BI-4 BI4C-2·BI-5 BI5C-2)의 거짓 안전감 차단 원리를 allow-list 에 *선제 대칭 적용*.**

- **allow-list "있음"(`allowed_signers` 파일 존재·ruleset 켜짐) ≠ 충족.** allow-list 실효 충족 = **다음 적대적 시연이 *전부* binary 통과** (enforcement 발효 상태 전제):
  - Hermes 키로 서명한 commit → **reject** (allow-list 미등록, default-deny)
  - 미서명 commit → **reject** — ⚠️ **SSH `allowed_signers` *단독* 으로는 보장 안 됨(BI1C-1)**: `git verify-commit`/`ssh-keygen -Y verify` 은 *서명 존재 시* signer 검증만 → 미서명 reject = **ruleset required-signature(서명 존재 강제) + CI default-deny(서명 부재=reject) 결합**(§5 C3)으로만 성립
  - `--no-verify` push / 직접 push → **server-side reject** (BI-2, Hermes 밖 anchor)
  - workflow yaml 수정으로 대조 무력화 시도 → **§2.5 #2 + BI-2 server-side anchor reject** (§7, pre-commit 단독 = 명목)
  - **CI reject 신호 ↔ required status check 배선 검증 (BI1R-5)**: CI 가 reject 신호를 내도 required check 미지정 시 merge 통과(C3) → "판정 신호가 실제 차단으로 *배선*됨"도 binary 항목
- → "`allowed_signers` 구성함 ✅" / "CI step 추가함 ✅" 는 *후보 조건*이지 *충족*이 아니다. **계산적 PoC(fingerprint 대조 코드 단위테스트) + 적대적 우회 시연** binary 통과해야 충족. CD-5·BI4C-2·BI5C-2·ADR-011 §2.1(b) "격리 환경 PoC 실증" 한 묶음.
- ⚠️ **⭐ binary = *에이전트(Hermes) 경로* 한정 (BI5C-2 답습)**: 위 시연은 에이전트 주어. **owner(사람) 경로 self-bypass(§9 (a)~(e))는 binary 범위 밖 = §9 수용된 SPOF**. "에이전트 경로 시연 통과 = allow-list 안전 확정"으로 미끄러지지 말 것.
- ⚠️ **⭐ observe mode = enforcement 미발효 (BI1C-3)**: 위 binary 시연은 **enforcement 발효 상태 전제**. observe mode 중에는 reject *신호*만 생성·차단 0(BI-7 면책) → **"binary 시연 통과 ≠ 차단 입증"**(observe 중 = "신호 정확"이지 "차단됨" 아님). "binary 통과 = 안전 확정" + "observe라 차단 0" 두 거짓 안전감 충돌 방지 (BI-5 §6 완전성 FN 다층 명문 답습).

---

## 11. 완전성 FN 경계 (BI-7) + `.git/` 직접 변조 범위 밖 (BI-10)

- **완전성 FN (BI-7)**: observe mode 통과(enforcement 미발효 관찰 기간, FN 통과 — line 789)는 *판정*의 면책. allow-list *무결성*(판정 기준 정확) ≠ *coverage 완전*(모든 commit 이 검사됨). 기록 누락 = BI-7/BI-5(§6 동형).
- **`.git/` 직접 변조 = 범위 밖 (BI-10, line 464)**: "`.git/` 디렉터리 직접 변조는 commit provenance check 범위 *밖* 이며 filesystem ACL(§2.5)의 책무. commit layer sensor 는 `.git/` 우회를 책임지지 않는다." → BI-1 allow-list 는 commit layer 한정, `.git/` 직접 조작 = BI-10(N-8, Layer 3 `.git/` ACL 선행).
- **coverage 미검사 경로 (BI1R-4)**: allow-list 무결성 ≠ coverage 완전 — **merge commit(부모 다수, merge 자체는 미서명일 수 있음) / squash(원 서명 commit 의 fingerprint 소실) / force-push 후 history(검사 우회)** = fingerprint 대조 적용 범위 경계 명시 필요(entry). observe FN 외에도 이 commit 유형들이 검사 사각.

---

## 12. single-host 한계 + 영구 핵심 제약 + means/ends + Provider Liquidity

- **single-host 한계**: 1인 = allow-list 관리 admin = commit 작성자 → BI-3/4/5 와 동형 SoD 구조적 불가(§9). "single-host allow-list 충족 = 안전 확정 아님, 수용된 SPOF 위 최선"(P2). multi-author(line 810: 두 번째 사용자 = 사용자별 signed commit + branch protection) = MVP-6.
- **means/ends**: allow-list 보장 속성(ends) = "신뢰 fingerprint 외 commit 차단" / 수단(means) = SSH `allowed_signers`/GPG/ruleset+CI (CN-6, 결정 0건).
- **Hermes ≠ root of trust**: CI step = Hermes 밖 실행(§6), workflow 변경 = R-I-CONFIG-CHANGE T3(§7) — Hermes 가 자기 판정 기준 무력화 불가.
- **Provider Liquidity 2층 ([[feedback_provider_liquidity]], BI-4 §7.1/BI-5 BI5R-1 동형)**: 층1 신뢰 기준 = SSH `allowed_signers` fingerprint = **vendor 중립**(어느 host/CI 에서도 동일) ⊕ 층2 집행 매체 = CI/ruleset/pre-receive 후보 다수. 중립 기준 유지로 lock-in 경감.
- **5 영구 핵심 제약 5/5 / Provider Liquidity 5-way 약화 0건.**

---

## 13. 진입 gate + Rollback Trigger

### 13.1 진입 gate (entry 발효 선결)

| Gate | 조건 | 출처 |
|----|----|----|
| G-BI1-1 | BI-3 credential 격리 선결 (신뢰 키 개인 키 Hermes 외 — 미격리 시 allow-list 붕괴) | §8 / BI-3 |
| G-BI1-2 | allow-list = **positive(default-deny)** + 판정 입력 = fingerprint(author ≠ 판정 입력) | §3 |
| G-BI1-3 | ruleset(서명 존재) + CI(fingerprint 대조) 보완 결합 (ruleset 단독 = 명목) | §5 / C3 |
| G-BI1-4 | BI-2 집행 결합 (reject = server-side, `--no-verify` 우회 불가) | §6 / BI-2 |
| G-BI1-5 | **§2.5 #2 workflow read-only 선결** (CI 대조 메타 보호, 재귀) | §7 / N-4 |
| G-BI1-6 | **allow-list 실효 = binary 입증** (에이전트 경로 우회 시연 실패 + fingerprint 대조 PoC, 라벨 ≠ 충족) | §10 |
| G-BI1-7 | owner self-bypass 처리 ((a)~(e) binary 범위 밖 = §9 수용 SPOF 명시) | §9 |
| **G-BI1-8** (BI1C-1) | **미서명 reject = ruleset required-signature + CI default-deny 결합** 확인 (SSH `allowed_signers` 단독 ≠ 미서명 reject) | §10/§5 |
| **G-BI1-9** (BI1C-3) | **observe ↔ enforce 전환 결정** (observe 중 binary 통과 ≠ 차단 입증 명시) | §10/§11 |

### 13.2 Rollback Trigger (allow-list 명목화 감지)

- ruleset required-signature / CI required check 해제 → 판정·집행 무력화.
- allow-list(`allowed_signers`)에 미검증 키 추가 → default-deny 우회.
- `.github/workflows/` 대조 step 변경 → §7 위반.
- 판정 입력이 author 필드로 회귀(fingerprint → author) → G3 결함 재발(후속 64 회귀).

⚠️ **감지 경계 + 능동 감지 (BI1C-2, BI-5 §12.2 대칭)**: 위 trigger 는 *결과 상태* 관찰형 → **감지 메커니즘·경로를 명시**해야 명목 trigger 회피.
- **에이전트 경로 = 능동 감지 가능**: author 회귀(fingerprint→author) = **PoC 회귀테스트**(판정 입력을 author 로 바꾸면 단위테스트 FAIL)로 능동 차단 / workflow step 변경 = §7 + BI-2 server-side reject.
- **⭐ owner 경로 = trigger 무력 = §9 수용된 SPOF**: owner 가 (a)~(e)(§9)로 self-bypass 시 — Rollback Trigger 는 *감지하지 못한다*(owner 가 곧 trigger 관리 admin). 즉 "Rollback Trigger 켰으니 회귀 차단됨"은 **에이전트 경로 한정 보장**이며 owner 경로는 binary 범위 밖(§10). "trigger 있음 = 안전"으로 미끄러지지 말 것.
- ⚠️ **observe mode 중**: 위 trigger 감지가 *신호*는 내나 enforcement 미발효 시 자동 차단 0 (BI1C-3, §10 답습).

---

## 14. 합의 형태 (풀 3+1 의무) + ⭐ 4축 심화 완주

- BI-1 = 보안 BLOCKING(우선순위 2) + G3 본문(positive allow-list) 정합 → **풀 3+1 의무** (Reviewer-only 부적격).
- Agent A(구현/정합): fingerprint 대조 실 코드·SSH `allowed_signers` 기술·workflow read-only. Agent B(보안): default-deny·owner self-bypass·binary 입증·credential 선결·FN. Agent C(대안): allow-list 매체(SSH/GPG/sigstore)·Provider Liquidity 2층.
- ⭐ **4축 심화 완주**: 본 brief = BI-3(credential)·BI-4(anchor)·BI-5(audit)·**BI-1(allow-list)** 4축 단독 심화의 *마지막*. 합의 후 → **4축 BLOCKING 통합 정리 + 구현 entry 발효 검토** 가능 (§15).
- 합의 = **추론적 검증(권고) 한정** — allow-list 매체 결정·CI 실 코드·workflow·ruleset 실 변경 = 사용자 명시 + 별도 단계.

---

## 15. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | 본 brief 승인 → BI-1 검증 풀 3+1 합의 | 합의(권고) |
| (B) | ⭐ **4축 BLOCKING 통합 정리** (BI-1/3/4/5 완주 → 우선순위·의존·gate 통합 + 구현 entry 발효 검토) | 통합 brief |
| (C) | credential 수단 *발효* (BI-3 후속, host OS 확인 후 — 구현 entry 첫 발효) | 구현 entry |
| (D) | 다른 BLOCKING (BI-6 Provider Liquidity / BI-7 observe / BI-8 / BI-9 백업키 / BI-10 `.git/` ACL) | 별도 brief |
| (E) | 세션 종료 | 메타 |

---

## 부록 A — 답습 출처

| 출처 | 본 brief 반영 |
|----|----|
| `f29c772` BI-1 (fingerprint allow-list 실 대조 + Hermes 밖 + workflow read-only) | §2 정의 |
| `f29c772` BI-2 (reject server-side, `--no-verify` 우회 불가) | §6 페어 |
| `f29c772` C3 (allow-list ≠ ruleset 단독) | §5 |
| `f29c772` N-4 (workflow read-only 의존, 높음) | §7 |
| `f29c772` CN-6 수단 (SSH `allowed_signers` 1순위 / GPG 후순위 / ruleset+CI) | §4 |
| G3 본문 line 360/448 (positive allow-list·author 판정 입력 아님, 후속 68 발효) — ⚠️ BI1R-2: 본 brief 인용(360/448)은 현 본문과 일치 확인. 합의 doc `f29c772`(§2.5)는 동일 내용을 360/**784**로 인용 = 정합 노이즈(brief 가 현 본문 기준 정확) | §3 |
| **citation stale 0 확정 (BI1R-2 positive)** — 본 brief 인용 10 line(221/273/328/360/448/460/464/789/810/1127) 전수 직접 대조 = stale 0. **BI-3 N-2→BI-4 §11.3→BI-5 차단조건#2 3연속 stale 패턴 단절** (직접 grep 의무 답습 효과) | 전체 |
| G3 본문 line 789 (credential 미격리 시 allow-list 붕괴 + 거짓 안전감) | §8 |
| G3 본문 line 460/328 (BI-2 anchor·runtime sensor 단독 금지) | §6 |
| G3 본문 line 464 (`.git/` 직접 변조 = 범위 밖, BI-10) | §11 |
| hermes-not-root-of-trust-runtime §2.5 #2 line 221 (`.github/workflows/` 보호) + line 273 TM-6 | §7 |
| BI-3 brief(credential 선결) / BI-4 §5(ruleset↔CI)·§7.1(2층) / BI-5 BI5C-2(owner self-bypass·binary) | §5·§8·§9·§10·§12 |
| ADR-011 §2.1 means/ends + §2.1(b) PoC 실증 | §4·§10·§12 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

CI provenance step 실 코드 (fingerprint 추출·`allowed_signers` 대조·pass/reject 로직) / **`.github/workflows/` 변경** (provenance step / actual run / workflow_dispatch / `on.push.paths` 필터) / **SSH `allowed_signers` 파일 구성·GPG keyring·서명 키 등록** / **GitHub ruleset·required-signature·branch protection 변경** (BI-4 영역) / **실 hook 구현** (pre-commit / pre-receive / server-side) / **filesystem ACL** (`.github/workflows/` read-only — §2.5 #2, BI-10) / **credential·서명 키 실 분리** (CT-1~CT-5 — BI-3 영역) / Hermes runtime·upstream 변경 / 수단 결정 고정 (allow-list 매체 — CN-6) / threshold 고정 / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / **Vault HSM ST-4** (γ-2 DEFER) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 변경 (line 360/448/789/1127) / ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / **git history rewrite** (후속 74 답습 — SHA 붕괴) / 다른 BLOCKING(BI-2~BI-10) 자동 진입 / G1(PR·approval auto-reject) 신규 단위 자동 진입 / Backlog #4 자동 진입 / tmux·Obsidian docs-scope 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
