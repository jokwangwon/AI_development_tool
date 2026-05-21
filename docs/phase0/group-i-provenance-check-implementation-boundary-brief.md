# Group I (provenance check) Implementation Boundary brief (DRAFT v1)

> **본 brief = Group I "Hermes-originated commit provenance check" *구현 경계 정의* 한정 (R-I-IMPL-BOUNDARY).** 본 brief 의 어떤 §도 그 자체로 실 hook(pre-commit / pre-receive) / GitHub ruleset·branch protection / CI provenance step / filesystem ACL·`read_only` mount·`cap_drop` / credential isolation / audit sink 구현 / CI workflow 변경 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 을 발생시키지 않는다. 본 brief = **구현 경계·guardrail·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **boundary brief → 승인 → 구현 entry 합의(풀 3+1) → 실 구현 + Evidence → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v1** (구현 경계 정의 — 실 구현 미진입)
**진입 단위**: G3 결함 교정 후속 #4 (`1bbbcb9` G3 DESIGN 발효 → IMPLEMENTATION 경계 정비) + Group I 합의 `f6c6d5a` §5 "구현 = Backlog #6 + 별도 풀 3+1 (R-I-IMPL-BOUNDARY)"
**선행 발효 답습**: `708bc0e` G3 본문 교정 발효 (provenance check 4축 DESIGN) + `f6c6d5a` Group I 풀 3+1 합의 (B-1~B-6) + Backlog #6 Layer A(`f1e0b23` entry 기준)·Layer B(`f40423f`+`55c5b4b` 9 sub-수단)·Layer C(`eb01bc4` Implementation Evidence PASS) + Group α `4880e88` (AR-3) + γ-1 `9b1f8cd`(ST-1)·γ-2 `2e9d46b`(ST-4 DEFER) + ADR-011 §2.1 means/ends
**답습 입력 (1차 권위)**: **`f6c6d5a` B-1~B-6 + §5 경계 + Group I brief §8 (R-I-IMPL-BOUNDARY / R-I-CONFIG-CHANGE 정의)** + G3 교정 본문(provenance check §3.1.2/§3.1.3/§4.5/§5.5) + patch brief v2 §6 수단 후보
**합의 권위 한계**: 본 brief = 경계 *정비* DRAFT — 구현 *진입 결정*·수단 *고정*·실 hook/ruleset/CI/credential/sink 구현은 별도 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "Group I implementation boundary brief 작성해줘"

본 brief = 위 명령 답습 — **provenance check 구현의 경계(R-I-IMPL-BOUNDARY) 정의 + 4축 → 구현 컴포넌트 매핑 + Backlog #6 vs MVP-6 경계 + Defense-in-depth 정합 + 영구 제약 보존 + 진입 gate + 합의 형태** + **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — G3 DESIGN 발효(후속 68) → IMPLEMENTATION 경계 (§1)
2. R-I-IMPL-BOUNDARY 정의 (구현 진입 boundary + rollback trigger) (§2)
3. 4축(positive allow-list / credential boundary / external enforcement / audit sink) → 구현 컴포넌트 매핑 + 각 경계 guardrail (§3)
4. ⭐ Backlog #6 (single-host MVP 적격) vs MVP-6 / Operational Readiness 경계 (§4)
5. Defense-in-depth 3-layer 정합 (provenance check / AR-3 ruleset / filesystem ACL) (§5)
6. 영구 핵심 제약 보존 (Hermes ≠ root / Provider Liquidity / means/ends) (§6)
7. 진입 적격성 + 선행 gate (§7)
8. 합의 형태 (풀 3+1 의무) + R-I-IMPL-BOUNDARY rollback (§8)
9. 다음 단계 (§9)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **실 hook 구현** (pre-commit / pre-receive / git server-side hook / CI provenance step 본문)
- ❌ **GitHub ruleset / branch protection 변경** (required-signature / required status check / bypass 정책)
- ❌ **CI workflow 변경** (provenance step 추가 / actual run / workflow_dispatch / paths 필터 — [[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **filesystem ACL / `read_only` mount / `cap_drop` / credential isolation (사람 키 미주입) 실 구성**
- ❌ **audit sink 실 구성** (외부 read-only sink / append-only)
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ **수단 *결정 고정*** (positive allow-list 키 종류·서명 방식·차단 지점·sink 매체 — CN-6/means-ends, 결정 = 구현 entry 합의)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)**
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ Vault HSM ST-4 진입 (γ-2 BLOCK/DEFER MVP-6 답습)
- ❌ G3 본문 재변경 / ADR·합의 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경
- ❌ G1 (PR·approval auto-reject) 신규 단위 자동 진입 (Group α C-2 별도 단위)
- ❌ 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. 경계·guardrail·gate·형태는 *정비/권고* 이며, 구현 *진입 결정*·수단 *고정*·실 구현 *발효* 는 구현 entry 합의(풀 3+1) + 사용자 명시 의 권한이다.

---

## 1. 진입 맥락 — DESIGN 발효 → IMPLEMENTATION 경계

```
후속 68 (708bc0e) ─ G3 본문 교정 발효 = provenance check DESIGN (4축 = 목적/원칙 수준)
        │  (DESIGN PASS — 문구 발효 완료)
        ▼
⭐ 본 brief ─ R-I-IMPL-BOUNDARY 정의 (DESIGN → IMPLEMENTATION 경계 정비, 실 변경 0건)
        ▼ (승인)
구현 entry 합의 (풀 3+1) ─ 수단 *결정* + 4축 구현 컴포넌트 진입 적격성 (Backlog #6)
        ▼ (승인)
실 구현 + Evidence ─ hook/ruleset/CI/credential/sink (Implementation Evidence PASS 영역)
```

- **현 상태**: provenance check = **DESIGN 발효 완료** (후속 68). 실 enforcement = 미구현.
- **R-I-CONFIG-CHANGE (B-5) = 이미 발효** — G3 본문 교정(설정/판정 기준 변경)이 T3 풀 3+1로 처리됨 (후속 65~68). 본 brief = 그 *다음* 경계 = **R-I-IMPL-BOUNDARY** (실 hook/ruleset/credential/sink 구현).

---

## 2. R-I-IMPL-BOUNDARY 정의 (Group I brief §8 답습)

| 항목 | 내용 |
|----|----|
| **trigger 대상** | Group I provenance check 의 *실 강제* 구현 진입 (hook / ruleset / CI provenance step / filesystem ACL / credential isolation / audit sink) |
| **boundary 조건** | Implementation/Runtime PASS 영역 + Backlog #6 연결 + **별도 풀 3+1** (Group I brief §8 line 278) |
| **R-I-CONFIG-CHANGE 와 구분** | R-I-CONFIG-CHANGE(B-5) = enforcement *설정/판정 기준* 변경 (G3 본문·ruleset 정책·audit 보존 정책 = T3, Hermes token 미보유) — 후속 65~68 발효. **R-I-IMPL-BOUNDARY = 그 설정을 *실 코드/구성*으로 구현** (별개 경계) |
| **rollback 발화** | 구현 중 (i) Hermes ≠ root of trust 위반(Hermes 가 ruleset/CI/audit token 획득) / (ii) Provider lock-in(특정 CLI·모델·SDK 하드코딩) / (iii) means 본문 고정(CN-6 위반) / (iv) credential 미격리로 allow-list 무력(FN>FP) / (v) audit sink Hermes 쓰기 가능 발견 시 → 구현 rollback + 사용자 alert |

---

## 3. 4축 → 구현 컴포넌트 매핑 + 경계 guardrail

> 본 §3 = *매핑 정비* (권고). 구현 컴포넌트의 *수단 결정·실 구현* = 구현 entry 합의 (CN-6 — 수단 = 후보, 결정 = Backlog #6). 수단 후보 = patch brief v2 §6 답습.

| 축 (G3 DESIGN) | 구현 컴포넌트 (Backlog #6 영역) | 수단 후보 (결정 = entry 합의) | ⭐ 경계 guardrail (R-I-IMPL-BOUNDARY) |
|----|----|----|----|
| **positive allow-list 검증** | 사람 권위 신호 서명 검증 + 사람 키 fingerprint allow-list 대조 (default-deny) | [ GPG/SSH signed commit / hardware-backed key / GitHub ruleset required-signature / CI provenance step 의 fingerprint 대조 ] 中 | allow-list = *사람* 키만 (Hermes 키 미포함) / 특정 서명 방식 본문 고정 금지 (Provider Liquidity·means/ends) / G4 §3.4.2 Skill 권한과 분리 |
| **credential boundary 격리** | Hermes 컨테이너에 사람 signing key·token·agent **미주입** | [ Hermes 컨테이너 사람 키 미주입(single-host canonical = ST-3 docker secret + ST-1 file perm γ-1) / secrets vault / KMS-backed ] 中 | **미격리 시 allow-list 무력(FN>FP) = 발효 전 BLOCKING (B-3 선결 전제)** / Vault HSM ST-4 = MVP-6 (§4) / chmod 능동강제 비권고(γ-1) |
| **external enforcement anchor** | runtime = provenance sensor *신호만*, 최종 reject = **Hermes 밖 anchor** (host 밖 최소 1개 *실* anchor) | [ GitHub branch protection·ruleset required-signature(off-host) / container filesystem ACL / hardware key 보유 분리 ] 中 | **Hermes 는 ruleset/CI token 미보유 (R-I-CONFIG-CHANGE B-5)** / pre-commit hook = sensor 신호(차단권 아님) / 명목 anchor 금지(B-4) / 차단 보장 = push/merge 전 |
| **audit sink integrity** | provenance·차단 시도 audit = **외부 read-only sink (Hermes 쓰기 불가)** | [ 외부 append-only sink / read-only mount 분리 매체 / 분산 sync ] 中 | audit 보존 정책 변경 = R-I-CONFIG-CHANGE(T3) / Hermes audit 위조 불가 (B-5 + G2) / credential 격리와 *별개 축* (G2) |

---

## 4. ⭐ Backlog #6 (single-host MVP 적격) vs MVP-6 / Operational Readiness 경계

> 핵심: provenance check 구현은 *전부* Backlog #6 가 아니다. single-host MVP 적격 부분과 MVP-6(multi-host/Operational Readiness) 부분의 경계를 명시 (silent scope expansion 차단).

| 구현 요소 | Backlog #6 (single-host MVP 적격) | MVP-6 / Operational Readiness (DEFER) |
|----|----|----|
| positive allow-list 검증 | CI provenance step + commit signature 검증 (single-host) | multi-stakeholder 승인 키 |
| credential 격리 | **Hermes 컨테이너 사람 키 미주입 (docker secret ST-3 + file perm ST-1, γ-1)** | **Vault HSM ST-4 (γ-2 BLOCK/DEFER — single-host 무력·안전 순이득 음수) / KMS** |
| external anchor | GitHub ruleset required-signature (SaaS/GHES off-host = single-host 의 현실적 실 anchor) | multi-host mutual TLS + distributed read-only + branch protection multi-author |
| audit sink | append-only git remote / 외부 read-only log (single-host) | 분산 audit sync (multi-host) |
| FP/observe | **observe mode (FN 통과, enforcement 미발효) 우선** (CN-9) | hard-block threshold 고정 (Implementation Evidence PASS 후) |

> ⚠️ γ-2 답습: Vault HSM ST-4 = single-host 에서 무력(external root/auto-unseal 동일 침해 경계) → **MVP-6 multi-host 전환 trigger 시 진입**. single-host canonical = ST-3 docker secret + ST-1 file perm. 본 brief 는 이 경계를 *재확인* 만 (γ-2 결정 변경 0건).

---

## 5. Defense-in-depth 3-layer 정합 (`f6c6d5a` 답습)

```
Layer 1 ─ commit provenance check (Hermes runtime = sensor 신호 + CI provenance step)  ← Group I 본 단위
Layer 2 ─ branch protection / ruleset required-signature (GitHub, off-host)            ← AR-3 (Group α) + external enforcement anchor (B-2/B-4)
Layer 3 ─ filesystem read-only ACL on Hermes container (G3 §2.5, `.git/` 우회 차단)     ← B-6 (commit layer 사각 보완)
        = 책무 분리 → 단일 source-of-truth 보존 (5 영구 핵심 제약 #4)
```

- Layer 2 (ruleset) = host 밖 실 anchor → Layer 1 (runtime sensor) 의 self-reference 차단 (Hermes 가 자기 차단책 무력화 불가).
- Layer 3 (`.git/` ACL) = commit provenance check 범위 *밖* 사각 보완 (G3 §3.1.3 note, 후속 68 발효).
- **G1 (PR·approval auto-reject) = 별도 단위** (Group α C-2, AR-2) — 본 brief 범위 *밖* (commit 아닌 approval 차원).

---

## 6. 영구 핵심 제약 보존 (구현 entry 합의 BLOCKING 후보)

| 제약 | 구현 guardrail |
|----|----|
| **Hermes ≠ root of trust** (핵심 제약 #1) | Hermes 는 ruleset/CI/audit 수정 token 미보유 (R-I-CONFIG-CHANGE) + 최종 reject = Hermes 밖 + 사람 키 Hermes 미주입. 구현이 Hermes 에 enforcement 권한을 주면 BLOCKING |
| **Provider Liquidity** (5-way) | provenance check 구현이 특정 git host(GitHub.com vs GHES)·CLI·서명 도구를 *하드코딩* 금지 — 환경 종속 후보 열거(GHES≠GitHub.com) 유지. [[feedback_provider_liquidity]] |
| **means/ends (ADR-011 §2.1)** | 구현 컴포넌트 = 목적(positive 검증/external reject/credential 격리/audit 무결) 충족, 수단(키·도구·anchor)은 entry 합의에서 *결정* (본문 고정은 G3 DESIGN 에서 금지됨) |
| **단일 source-of-truth** (#4) | Defense-in-depth 3-layer 책무 분리 (§5) |

---

## 7. 진입 적격성 + 선행 gate

| # | 진입 gate | 충족 | 비고 |
|----|----|----|----|
| G-1 | provenance check DESIGN 발효 | ✅ | 후속 68 (`708bc0e`) |
| G-2 | Group I 풀 3+1 합의 (B-1~B-6) | ✅ | `f6c6d5a` |
| G-3 | Backlog #6 Layer A(entry 기준)·Layer B(9 sub-수단)·Layer C(Implementation Evidence PASS) | ✅ | `f1e0b23`/`f40423f`·`55c5b4b`/`eb01bc4` — provenance check = 그 영역 내 *신규 컴포넌트* |
| G-4 | credential 격리 선결 전제 (B-3) 구현 가능성 | ⏳ | single-host = 사람 키 Hermes 미주입(ST-3/ST-1) 적격 / Vault = MVP-6 |
| G-5 | external anchor host 밖 실 anchor 가용 (B-4) | ⏳ | GitHub ruleset(SaaS/GHES) — 환경 확인 = entry 합의 |
| G-6 | Operational Readiness (multi-host/Vault) | ❌ DEFER | MVP-6 (§4) — single-host 부분만 진입 적격 |

> **진입 적격성 결론 (권고)**: single-host MVP 영역(§4 좌열)은 **구현 entry 합의 진입 적격** (G-1~G-3 충족, G-4/G-5 = entry 합의 확인). MVP-6 영역(Vault/multi-host)은 DEFER. 진입 *결정* = 사용자 명시.

---

## 8. 합의 형태 + R-I-IMPL-BOUNDARY rollback

- **합의 형태 = 풀 3+1 (Agent A/B/C + Reviewer) *의무*, Reviewer-only 부적격** — Group I = T3 보안 enforcement (`f6c6d5a` 만장일치, trigger #2 T3 + #5 핵심 제약 #1/#4 + §4 self-reference). 구현 entry 도 동일 (R-I-IMPL-BOUNDARY = 별도 풀 3+1, Group I brief §8).
- **2차 vendor 입력**: trigger #7 = Group I 외부 GPT-5.5 1건 기 충족. 구현 단계 추가 vendor = 사용자 결정(의무 아님).
- **R-I-IMPL-BOUNDARY rollback** (§2): 구현 중 Hermes≠root 위반 / Provider lock-in / means 본문 고정 / credential 미격리 / audit Hermes 쓰기 가능 발견 시 rollback + alert.

---

## 9. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 |
|----|----|----|
| **(A)** | 본 brief 승인 → **provenance check 구현 entry 합의 진입** (풀 3+1 — single-host MVP 영역 수단 결정 + 진입 적격성) | 합의 보고서 작성 |
| (B) | 본 brief 일부 수정 → v2 | v2 작성 |
| (C) | 본 brief 승인 → commit *까지만* | 1 commit |
| (D) | 보류 → 다른 backlog (tmux 도입 / G1 PR·approval auto-reject 신규 단위 / 2차 vendor / GP-5 C-2 facade real P1 v2 Backlog #4) | 별도 brief |
| (E) | 세션 종료 | — |

> 본 brief = **boundary brief 단계 한정**. 구현 entry 합의 / 수단 결정 / 실 hook·ruleset·CI·credential·sink 구현 / commit / push = 사용자 명시 승인 후 별도 단계. 구현 = **R-I-IMPL-BOUNDARY → Backlog #6 + 별도 풀 3+1**.

---

## 10. 한 단락 요약

`708bc0e` G3 본문 교정 발효(provenance check 4축 DESIGN 완료)를 받아, 그 *실 강제 구현*의 경계(**R-I-IMPL-BOUNDARY**)를 정의하는 brief — DESIGN(후속 68) → IMPLEMENTATION 경계를 (§2) R-I-IMPL-BOUNDARY 정의(실 hook/ruleset/CI/filesystem ACL/credential/sink 구현 = Implementation/Runtime PASS + Backlog #6 + 별도 풀 3+1, R-I-CONFIG-CHANGE[설정 변경, 후속 65~68 발효]와 구분), (§3) 4축 → 구현 컴포넌트 매핑 + 경계 guardrail(allow-list=사람 키만/credential 미격리=BLOCKING 선결/Hermes ruleset token 미보유/audit Hermes 쓰기 불가), (§4) ⭐ Backlog #6(single-host MVP 적격 = CI provenance step + 사람 키 Hermes 미주입[ST-3/ST-1] + GitHub ruleset off-host + append-only audit + observe mode) vs MVP-6/Operational Readiness(Vault HSM ST-4[γ-2 DEFER]·multi-host·KMS·hard-block threshold) 경계, (§5) Defense-in-depth 3-layer(commit provenance check / ruleset AR-3 / filesystem ACL) 정합, (§6) Hermes≠root·Provider Liquidity·means/ends 보존 guardrail, (§7) 진입 gate(DESIGN 발효·Group I 합의·Backlog #6 Layer A/B/C 충족 → single-host 영역 진입 적격, MVP-6 DEFER), (§8) 풀 3+1 의무 형태로 정비. 본 brief 는 결론을 *선취하지 않으며* — 구현 진입 결정·수단 고정·실 구현(hook/ruleset/CI/credential/sink)은 모두 사용자 명시 + 별도 단계(구현 entry 합의 + Backlog #6) — **실 hook 구현 / GitHub ruleset 변경 / CI workflow 변경 / filesystem ACL·credential isolation·audit sink 구현 / Operational Readiness PASS / Hermes PMO 격상 / Vault HSM ST-4 진입 / 수단 결정 고정 / threshold 고정 / G1 신규 단위 자동 진입 / commit / push = 모두 0건** 이다.

---

## 부록 A — 답습 출처

| 출처 | 답습 |
|----|----|
| `3plus1-consensus-2026-05-20-group-i-...-autoreject.md` (`f6c6d5a`) B-1~B-6 + §5 | 경계·guardrail·형태 (§2·§3·§6·§8) |
| `group-i-...-full-3plus1-brief.md` §8 (R-I-IMPL-BOUNDARY / R-I-CONFIG-CHANGE) | R-I-IMPL-BOUNDARY 정의 (§2) |
| `hermes-not-root-of-trust-runtime.md` (`708bc0e`) provenance check 4축 | DESIGN 입력 (§1·§3·§5) |
| `g3-metadata-detection-correction-patch-brief.md` v2 §6 | 수단 후보 (§3) |
| Backlog #6 `f1e0b23`/`f40423f`·`55c5b4b`/`eb01bc4` (Layer A/B/C) | 진입 gate G-3 (§7) |
| γ-1 `9b1f8cd`(ST-1) / γ-2 `2e9d46b`(ST-4 DEFER) / Group α `4880e88`(AR-3) | §4 경계 + §5 Layer 2 |
| ADR-011 §2.1 (means/ends) | §6 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
**실 hook 구현** (pre-commit / pre-receive / git server-side / CI provenance step) / **GitHub ruleset·branch protection 변경** / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / paths 필터) / **filesystem ACL·`read_only` mount·`cap_drop`·credential isolation(사람 키 미주입) 실 구성** / **audit sink 실 구성** / **Hermes runtime·upstream 변경** / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / **Vault HSM ST-4 진입** (γ-2 DEFER MVP-6) / 수단 결정 고정 (키 종류·서명 방식·차단 지점·sink 매체) / threshold 고정 (observe mode 기간) / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 재변경 / ADR 본문 자동 갱신 / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / **G1 (PR·approval auto-reject) 신규 단위 자동 진입** (Group α C-2 별도 단위) / Backlog #4 자동 진입 / tmux 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
