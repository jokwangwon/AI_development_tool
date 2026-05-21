# BI-4 GitHub plan·ruleset 가용성 brief — external anchor 실재성 심화 (DRAFT v3)

> **본 brief = Group I 구현 entry 합의(`f29c772`, R-I-IMPL-BOUNDARY)의 우선순위 2 BLOCKING BI-4("external anchor 실재성")를 *단독 심화* 하는 brief 한정.** 본 brief 의 어떤 §도 그 자체로 GitHub ruleset·branch protection 변경 / required status check 설정 / bypass list 변경 / CI workflow(provenance step) 변경 / GHES 도입 / plan 업그레이드 / 실 hook 구현 / Operational Readiness PASS / Hermes PMO 격상 / 수단 결정 고정 / threshold 고정 을 발생시키지 않는다. 본 brief = **anchor 정의·plan 가용성 사실 정비·self-bypass 역설·CI↔ruleset 보완·token 호스트 외 분리(CT-2 cross-ref)·GHES 대안·origin replace 위험·single-host 한계·진입 gate·합의 형태 정비** — 실 변경 0건. staged cycle: **brief → 승인 → 합의(풀 3+1) → commit → push** (각 단계 사용자 명시 분리).

---

**작성일**: 2026-05-21
**Status**: **DRAFT v3** (v2 + BI-4 brief 검증 풀 3+1 합의 `bb661f0` BLOCKING BI4C-1~5 + 권고 BI4R-1~6 반영 — 본문 반영, 결정 0건). v2 = G-BI4-1 사실 확인(repo `jokwangwon/AI_development_tool` = **`public` 확정**, 2026-05-21 비인증 API, plan 종속 worst-case 해소, 쟁점 = self-bypass/token 이동).
**진입 단위**: Group I 구현 entry 합의 후속 #2 (`f29c772` 합의 §2.2 BI-4 = 우선순위 **2** · BI-3 credential 다음)
**선행 발효 답습**: `ead5754` BI-3 credential 수단 결정 합의 (CD-1~10) + `bf42d0e`/`cc5b517` BI-3 credential 격리 brief·검증 합의 (BI3-1~8, §7.4 CT-2 격리 선결 = BI-4) + `8e57f7b`/`f29c772` Group I 구현 entry 합의 (BI-1~BI-10 + CBI-1~CBI-4 + N-1/N-3) + `596f866` Group I 구현 경계 brief + `708bc0e` G3 provenance check 4축 DESIGN + `4880e88` Group α 합의 (AR-3/C-4) + ADR-011 §2.1 means/ends + hermes-not-root-of-trust-runtime §2.2 #20 (R-I-CONFIG-CHANGE T3)
**답습 입력 (1차 권위)**: **`f29c772` 합의 BI-4 정의 4요소(i~iv) + N-3 self-bypass 역설 + GA-2 plan 종속 + CBI-2 명목 anchor + §86 우선순위** + BI-3 brief `bf42d0e` §7.4(CBI3-3) + Group α `4880e88` C-4(GitHub plan 종속, AR-3 8 결정 영역 中) + R-I-CONFIG-CHANGE T3
**합의 권위 한계**: 본 brief = BI-4 *심화* DRAFT — anchor 수단 *결정 고정*·plan *업그레이드 결정*·ruleset/branch protection/CI required check/bypass list *실 변경*·GHES *도입 결정* 은 별도 구현 entry 발효(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다.

---

## v2 변경 이력 (G-BI4-1 사실 확인 반영)

| 항목 | v1 → v2 반영 위치 |
|----|----|
| **G-BI4-1 사실 확인** (현 repo public/private) | 2026-05-21 비인증 GitHub API: `jokwangwon/AI_development_tool` = **`visibility: public` / `private: false` 확정** (account = personal, org 아님) |
| **§3.2 함의 1** (private+Free worst-case) | **해소** — public repo 는 모든 plan(Free 포함)에서 ruleset 가용 → anchor 후보 (A) 존재 가능. plan 업그레이드/GHES 는 anchor 의 *전제* 아님 (§3.2/§3.3) |
| **쟁점 이동** | plan 종속(C-4/GA-2) 무게 **경감** → BI-4 의 *진짜* 쟁점 = **self-bypass(§4) + token 분리(§6)** 로 좁힘 (§3.3) |
| **§3.3 신설** | 현 repo 맥락 확정 — public 확정 + personal account = bypass list org-only = owner 전권 = §4 self-bypass 최강 적용 |
| **부수 관찰** | repo public = `docs/` 전체 세계 공개 → 개인 데이터 repo 밖 유지 권고(Obsidian 논의)와 정합 (§3.3 note) |
| **§11.1 G-BI4-1** | gate 상태 = **부분 충족**(public 확정으로 ruleset 가용 ✅ / push ruleset·org-level = Team plan 종속은 잔존, entry 재확인) |

## v3 변경 이력 (`bb661f0` 합의 BLOCKING BI4C-1~5 + 권고 BI4R-1~6 반영)

| 항목 | v2 → v3 반영 위치 |
|----|----|
| **BI4C-1** (§11.3 citation stale) | §11.3 — "G3 §5.5"(SPOF Accepted Risk, 문구 0건) → **`f29c772` line 118 + BI-7** 정정 (후속 72 N-2 동형) |
| **BI4C-2** ⭐ (CD-5 binary 입증 미적용) | §11.3 + §2 — **anchor 실효 = 적대적 우회 시연(binary) 종료 조건** 명문 (enforcement status 라벨 ≠ 충족, ADR-011 §2.1(b) 동형) |
| **BI4C-3** (CI required direct-push 우회) | §3.1 (A)/(C) + §5 — required check = *merge* 게이트, 직접 push 차단 = 별도 ruleset 종속 명문 + §11.1 **gate G-BI4-6** 추가 |
| **BI4C-4** ⚠️ (개인 이메일 public 노출) | §3.3 + §13 — `tgdata200` 3파일 plaintext 현존 노출 = entry 발효 **선결 점검 격상**(redaction 별도) |
| **BI4C-5** (Rekor 후보표 비대칭) | §3.1 표 **(E) Sigstore Rekor 행 병치** (채택 아님) + CBI-4 BI-3·BI-4 cross-ref |
| BI4R-2 | §5/§6 — anchor 집행(vendor) ⊕ 신뢰 기준(allowed_signers 중립) 분리 (BI-3 cross-ref 답습) |
| BI4R-3 | §7 — anchor "신뢰 기준 × 집행 매체" 2층 추상화 모델 + §6 GitHub App installation token 후보 |
| BI4R-4 | §4.4 self-bypass 재귀 닫힘 + §8 origin replace↔CBI-2 + §11.2 Rollback Trigger 추가 + §4.3 workflow yaml 우회 |
| BI4R-5 | §8 — 외부 미러 cross-check 후보(동일 owner 침해 경계 한계 명시) |
| BI4R-1 / BI4R-6 | §3.2 entry 재확인 유지 / 제목 v1→v3 정합 |

---

## 0. 본 brief 의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-21)

> "BI-4 GitHub plan·ruleset 가용성 brief로 진행해줘"

본 brief = 위 명령 답습 — **BI-4(external anchor 실재성) 단독 심화** = (i) anchor *정의* 재확인(4요소 i~iv) + (ii) GitHub.com **plan별 ruleset 가용성 사실 정비**(C-4/GA-2, 현 repo 맥락 포함 — entry 발효 시 재확인) + (iii) ⭐ SaaS **self-bypass 역설**(1인 = repo owner = ruleset off, N-3) + (iv) ruleset ↔ CI provenance step = *보완*(서명 존재 vs fingerprint 대조) + (v) anchor token **Hermes 호스트 외 분리**(CT-2 격리 ↔ BI-3 cross-ref) + R-I-CONFIG-CHANGE T3 + (vi) GHES pre-receive 대안(off-host anchor 상승)·Provider Liquidity 긴장 + (vii) origin replace 위험(BI-5 audit cross-ref) + (viii) single-host = 동일 admin 경계 + 진입 gate + 합의 형태 — **실 변경 0건**.

### 0.2 본 brief 가 *하는* 것

1. 진입 맥락 — 구현 entry 합의(후속 69)에서 BI-4 = 우선순위 2 (BI-3 다음) (§1)
2. BI-4 정의 재확인 — external anchor 실재성 4요소(i plan / ii token 분리 / iii self-bypass 차단 / iv origin replace) (§2)
3. anchor 대상 + GitHub.com **plan별 ruleset 가용성 사실** (C-4/GA-2 — 후보, entry 재확인) (§3)
4. ⭐ SaaS **self-bypass 역설**(N-3) — 1인 admin = ruleset 비활성화·bypass 가능 = 명목 anchor 현실 경로 (§4)
5. ⭐ ruleset(서명 *존재*) ↔ CI provenance step(fingerprint allow-list *대조*) = *보완* (둘 다 필요, BI-1 인터페이스) (§5)
6. anchor token **Hermes 호스트 외 분리** = CT-2 격리 선결(BI-3 cross-ref) + ruleset 변경 = R-I-CONFIG-CHANGE T3 (§6)
7. GHES pre-receive 대안(off-host anchor 상승) + Provider Liquidity(vendor lock-in 긴장) (§7)
8. origin replace / remote 교체 위험 + append-only audit cross-ref(BI-5) (§8)
9. single-host 한계 = 동일 admin 경계 = "수용된 SPOF 위 최선" (§9)
10. 영구 핵심 제약 + means/ends(anchor 보장=ends, 수단=means) (§10)
11. 진입 gate + Rollback Trigger + anchor observe binary 성격 (§11)
12. 합의 형태 (풀 3+1 의무) (§12)
13. 다음 단계 (§13)

### 0.3 본 brief 가 *하지 않는* 것 (사용자 명시 영구 답습)

본 brief 의 어떤 §도 그 자체로 다음을 발생시키지 않는다:

- ❌ **GitHub ruleset / branch protection 변경** (rule 생성·수정·삭제 / 대상 branch / 적용 enforcement status — active/evaluate/disabled)
- ❌ **required status check 설정** / **bypass list 변경**(actor 추가·제거·비움) / **CI required 게이트 설정**
- ❌ **CI workflow 변경**(provenance step / actual run / workflow_dispatch / `on.push.paths` 필터 — [[feedback_actual_run_trigger_paths_filter]] 답습 의무)
- ❌ **plan 업그레이드 결정**(Free→Pro/Team) / **org 전환 결정**(personal→organization) / **GHES 도입 결정**
- ❌ **실 hook 구현** (pre-commit / pre-receive / server-side / CI provenance step 본문)
- ❌ **credential / anchor token 실 분리 구성** (token Hermes 미주입 / scope 최소화 / 호스트 외 보관 — BI-3 영역, 결정 = entry 발효)
- ❌ Hermes runtime / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR)
- ❌ **audit sink 실 구성** / append-only git remote 설정 (BI-5 영역)
- ❌ **수단 *결정 고정*** (anchor 매체 = ruleset / CI / GHES pre-receive — CN-6/means-ends, 결정 = entry 발효)
- ❌ threshold 고정 (observe mode 기간 등)
- ❌ **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)**
- ❌ Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경
- ❌ G3 본문 변경 / GP-3 본문 변경 / ADR·합의 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경
- ❌ 다른 BLOCKING(BI-1/2/3/5~10) 자동 진입 / Group α C-4 *결정* 발효(plan 결정 = AR-3 영역) / 합의 보고서 작성 / commit / push (별도 단계)
- ❌ 5 영구 핵심 제약 · Provider Liquidity 5-way 약화

### 0.4 권위 한계

본 brief 는 결론을 *선취하지 않는다*. anchor 정의·plan 가용성 사실·self-bypass 역설·CI 보완·token 분리·GHES 대안·origin replace 위험·gate 는 *심화/정비/권고* 이며, anchor 수단 *결정*·plan/org/GHES *도입 결정*·ruleset/CI/bypass *실 변경*·token 분리 *발효* 는 구현 entry 합의(풀 3+1, R-I-IMPL-BOUNDARY) + 사용자 명시 의 권한이다. 본 §3 의 GitHub.com plan 가용성 사실은 **2026-05 시점 web 확인 후보**이며 — Group I 합의(`f29c772` line 147)가 "plan 확인 = entry 발효 시"로 명시한 바 — **entry 발효 시 현 repo plan 으로 재확인**해야 하는 비권위 입력이다.

---

## 1. 진입 맥락 — BI-4 = 우선순위 2 · external anchor

```
후속 69 (f29c772) ─ Group I 구현 entry 합의 (BI-1~BI-10)
        │  우선순위: BI-3(credential) > BI-4(anchor) > BI-1/BI-2 > BI-5 > …
        ▼
후속 71~72 (bf42d0e/ead5754) ─ BI-3 credential 격리 brief + 수단 결정 합의 (우선순위 1 완주)
        ▼
후속 73 (본 brief) ─ BI-4 external anchor 실재성 단독 심화 (우선순위 2)
```

- **BI-4 우선순위 = 2** (`f29c772` §2.2: `credential(BI-3) > anchor(BI-4) > …`). 순서(만장일치): credential 격리 → allow-list 정의 → **external anchor** → audit.
- **선결 관계**: BI-3 §7.4(CBI3-3) — **CT-2(host token) 격리 실효성은 "token 이 ruleset 을 끌 수 있는가"에 종속 → BI-4(plan·ruleset 가용성)가 BI-3 CT-2 격리의 선결.** 즉 BI-3 ↔ BI-4 는 양방향 인터페이스(credential 격리가 anchor 를 지키고, anchor 가용성이 credential 격리 대상을 정의).
- **Group α C-4 (GA-2)**: `4880e88` Group α 합의의 AR-3 8 결정 영역 中 "GitHub plan 종속"이 **미해소** — BI-4 가 이를 anchor 실재성 관점에서 흡수.

---

## 2. BI-4 정의 재확인 — external anchor 실재성 4요소

`f29c772` §2.2 BI-4 (우선순위 2):

> **external anchor 실재성** — (i) plan 확인(C-4, GA-2) + (ii) anchor token Hermes 호스트 외 분리 + (iii) **SaaS self-bypass 차단**(bypass list 비움 + CI required check 실 게이트 + ruleset 변경 = R-I-CONFIG-CHANGE T3) + (iv) origin replace 위험 명시. **명목 anchor 금지.**

| 요소 | 내용 | 본 brief § | 인터페이스 |
|----|----|----|----|
| (i) plan 확인 | ruleset/branch protection 가용 plan (C-4/GA-2) | §3 | Group α AR-3 |
| (ii) token 호스트 외 분리 | anchor 설정/변경 token 이 Hermes 호스트 밖 | §6 | BI-3 CT-2 |
| (iii) self-bypass 차단 | bypass list 비움 + CI required 실 게이트 + ruleset 변경 = T3 | §4·§5·§6 | N-3 / R-I-CONFIG-CHANGE |
| (iv) origin replace 위험 | remote 교체·history rewrite 로 anchor 우회 | §8 | BI-5 audit / G4 |

**핵심 명제 (CBI-2)**: "SaaS ruleset = external anchor"는 **self-bypass 차단(BI-4 (iii))이 충족될 때만** 성립. 미충족 시 = **명목 anchor**(존재하나 동일 주체가 끌 수 있음 = 보호 0 + 거짓 안전감). → BI-4 = "anchor 가 *실재* 하는가"를 묻는 BLOCKING.

---

## 3. anchor 대상 + GitHub.com plan별 ruleset 가용성 (C-4/GA-2)

### 3.1 anchor 후보 대상 (means 후보 — 결정 0건, CN-6)

| 후보 | 메커니즘 | 차단 보장 시점(ends) | off-host 여부 |
|----|----|----|----|
| **(A) SaaS Repository ruleset** | 서명 require / required status check / **restrict direct push(PR 강제)** / restrict deletion·force-push | push/merge 거부 (서버 측) — **직접 push 차단은 restrict direct push rule 필수**(BI4C-3) | ✅ GitHub 서버 (단 동일 owner 가 설정 변경 가능 = §4) |
| **(B) SaaS branch protection (legacy)** | required review / required status check | merge 거부 | ✅ (ruleset 의 구형, 점진 대체) |
| **(C) CI required status check** | provenance step 통과를 merge 필수 게이트로 (BI-1 fingerprint 대조) | **merge 거부 한정** — ⚠️ 직접 `git push`(PR 미경유) 시 우회됨, (A) restrict direct push 결합 전제(BI4C-3) | ✅ (단 required 지정 자체가 ruleset/protection 종속) |
| **(D) GHES pre-receive hook** | 서버 측 hook 으로 push 거부 | push 거부 (서버 측, owner 우회 난이도↑) | ✅✅ (Enterprise Server, §7) |
| **(E) Sigstore Rekor transparency log** (CN-C1/BI4C-5, **후보 보존·채택 아님**) | gitsign keyless 서명 → Rekor append-only 공개 로그 기록 | 사후 입증(transparency) — 차단보다 *부인 불가* 증거 | ✅✅✅ **제3자(Sigstore 공개 인스턴스)** — owner 가 공개 로그 *삭제 불가* → self-bypass(§4)·origin replace(§8)에 구조적 강함. trade-off = OIDC IdP 새 의존 축 + 메타데이터 공개(public repo 라 완화). CBI-4 = BI-3 §4 M5 ↔ BI-4 양쪽 cross-ref. MVP-6 audit 시너지 |

> **BI4R-2 (집행 ⊕ 기준 분리)**: anchor 는 **집행 매체**(위 (A)~(E) = vendor 종속도 상이)와 **신뢰 기준**(누구 서명을 신뢰 = SSH/GPG `allowed_signers` / fingerprint allow-list = **vendor 중립**)의 직교 2층(§7 BI4R-3). 신뢰 기준의 중립 매체(`allowed_signers`)는 BI-3 가 이미 1순위 권고 → 본 brief 는 **재결정이 아니라 cross-ref 답습**.

### 3.2 GitHub.com plan별 가용성 (2026-05 web 확인 후보 — entry 재확인 의무)

| plan | public repo ruleset | **private repo ruleset** | bypass list | org-level ruleset |
|----|----|----|----|----|
| **Free (personal)** | ✅ | **❌ 불가** | — (org 만 가능) | — |
| **Free for org** | ✅ | ❌ | actor 추가 가능(org) | — |
| **Pro (personal)** | ✅ | **✅** | — (org 만 가능) | — |
| **Team** | ✅ | ✅ | ✅ (org) | ✅ (2025-06 추가) |
| **Enterprise Cloud** | ✅ | ✅ | ✅ | ✅ |
| **Enterprise Server(GHES)** | ✅ | ✅ | ✅ | ✅ + pre-receive |

**⭐ 현 repo 맥락 (2026-05-21 비인증 API 확인)**: origin = `github.com/jokwangwon/AI_development_tool` = **GitHub.com SaaS · personal account(org 아님) · `visibility: public` 확정**.
- **함의 1 (plan 종속 — 해소)**: repo 가 **public 확정** → §3.2 표 기준 **모든 plan(Free 포함)에서 ruleset 가용** → anchor 후보 (A) ruleset *존재 가능* ✅. "private+Free → ruleset 부재" worst-case 는 **적용 안 됨**. plan 업그레이드(Pro+)/public 전환/GHES 는 anchor 실재의 *전제 아님*. (단 push ruleset·org-level ruleset = Team plan 종속은 잔존 → entry 재확인.)
- **함의 2 (bypass list 부재 — 잔존)**: personal account = **bypass list 는 org 소속 repo 에서만** → personal repo 는 owner 본인이 곧 전권. → §4 self-bypass 역설이 *가장 강하게* 적용 (plan 변수 제거 후 BI-4 의 *진짜* 쟁점).
- **함의 3 (org 전환 trade-off)**: org 전환 시 bypass list·org-level ruleset 가용하나 = 운영 복잡도 + Provider Liquidity(vendor 구조 종속) 긴장 — 결정 = AR-3 영역, 본 brief 0건.

### 3.3 G-BI4-1 확인 결과 = 쟁점 이동 (v2)

- **확인된 사실**(2026-05-21 비인증 API): repo = **public** → ruleset plan 종속(C-4/GA-2)의 가장 무거운 변수(private+Free)가 **소거**.
- **쟁점 이동**: BI-4 의 무게 중심이 **"anchor 후보가 *존재* 하는가"(plan, 통과)** 에서 **"anchor 가 *실효* 하는가"(self-bypass §4 + token 분리 §6)** 로 이동. → 합의 Agent 분배 시 §4/§6 가 핵심, §3 plan 은 *통과 확인* 으로 격하.
- **잔존 plan 종속**(entry 재확인): push ruleset / org-level ruleset = Team plan 종속(§3.2). 기본 anchor(require signed commits + required status check + restrict force-push/deletion)는 public 으로 가용.
- **⭐ public 노출 = 현존 위험 (BI4C-4, 합의 BLOCKING 격상)**: repo = public → `docs/` 전체(CONTEXT·합의 보고서·brief)가 **세계 공개**. 합의 Reviewer grep 재검증 결과 — 개인 이메일 `tgdata200@gmail.com` 이 **`docs/review/3plus1-consensus-2026-05-13-{mvp1-pass-c1-k2, adr-012-event-enum, k2-permissions}.md` 3개 파일에 plaintext 로 *이미 commit·공개*** 됨 = 가설 아닌 **현존 노출**. → **entry 발효 *선결* 점검 항목으로 격상**(redaction 실 변경 = git history rewrite 얽힘, 별도 단계). 직전 "개인 데이터 = repo 밖 vault" 권고와 정합(공개 repo 에 개인 데이터 유입 = 노출). (`ghp_` 매치 = redaction 패턴 정의 *예시* = false positive.) 본 brief redaction 0건.

---

## 4. ⭐ SaaS self-bypass 역설 (N-3) — anchor 명목화의 현실 경로

### 4.1 역설 정의

`f29c772` N-3 (Agent C 발견, 높음): **single-host 1인 환경에서 그 1인 = repo owner/admin** → ruleset 을 **(a) 비활성화(disabled)** 하거나 **(b) bypass 권한 대상에 자신을 추가**하거나 **(c) enforcement status 를 `evaluate`(비차단)로 강등** 할 수 있음. 즉 anchor 가 "host 밖"에 있어도 **host 안의 동일 주체가 SaaS 콘솔에서 끌 수 있으면 anchor 는 명목**.

> web 확인(2026-05): ruleset bypass 대상 = **Repository admins · organization owners · enterprise owners** + maintain/write 역할 등. → repo admin(=1인 owner)은 *구조적으로* bypass 가능 주체에 포함됨.

### 4.2 왜 BI-3(credential 격리)만으로 안 막히는가

- BI-3 는 **Hermes(에이전트) 환경에 사람/admin credential 미주입** = 에이전트가 anchor 를 못 끄게 함. ✅
- 그러나 **사람 사용자 본인**은 여전히 GitHub 웹 콘솔 로그인으로 ruleset 을 끌 수 있음 — 이건 credential *격리* 로 막는 대상이 아니라 *권한 분리(SoD)* 문제.
- → single-host 1인은 SoD 가 **구조적으로 불가**(승인자 = 작성자 = admin). 이것이 §9 "수용된 SPOF".

### 4.3 차단 후보 (means 후보 — 결정 0건)

| 후보 | 효과 | 한계 |
|----|----|----|
| bypass list 비움 + active enforcement | 에이전트·CI 경로 우회 차단 | owner 본인 콘솔 변경 불가 차단 ❌ |
| **ruleset 변경 = R-I-CONFIG-CHANGE T3** | anchor 설정 변경을 *추적/합의* 대상으로 (Hermes token 미보유 = 에이전트는 변경 불가) | 사람 본인 변경은 *audit 사후 탐지*로 격하 (§8) |
| **CI required check 별 경로** | ruleset off 해도 CI 게이트 잔존(이중화) | CI 설정도 owner 가 끌 수 있음(동일 역설 재귀) — ⚠️ **CI workflow yaml(`.github/workflows/`)이 repo 內 = commit 으로 변경 가능** → 에이전트가 workflow 를 수정해 게이트 무력화 가능. **BI-1 "workflow read-only"(§2.5 #2/N-4) 의존** (BI4R-4) |
| org 전환 + 별도 admin 분리 | 진정한 SoD | 1인 환경에서 비현실(추가 인원 필요) |

**⭐ 거짓 안전감 차단 (CBI-2 / P2 답습)**: self-bypass 가 구조적으로 잔존하는 한 — **"ruleset 존재 = 안전 확정"이 아니라 "수용된 SPOF 위 최선"**. anchor 의 실효는 *에이전트(Hermes) 경로 차단*에 있고, *사람 owner 우회*는 audit 사후 탐지로 격하됨을 명문해야 명목 anchor 오독을 차단.

### 4.4 self-bypass 재귀 닫힘 명제 (BI4R-4)

self-bypass 는 **ruleset · CI · token · origin 4 표면 전부에서 재귀**한다(§4.3 표 각 행의 한계가 동일 owner 권한으로 수렴). → **닫힌 명제**: *어느 단일 anchor 도 1인 owner 우회를 막지 못한다.* anchor 의 안전 주장은 **"(a) 에이전트(Hermes) 경로 차단(credential 격리 BI-3 + R-I-CONFIG-CHANGE T3) ⊕ (b) 사람 owner 경로 audit 사후 격하(BI-5)"의 *결합* 으로만** 성립하며, 단일 anchor 라벨로는 성립하지 않는다(§9 "수용된 SPOF 위 최선"의 §4 측 명문).

---

## 5. ⭐ ruleset ↔ CI provenance step = 보완 (둘 다 필요)

`f29c772` (만장일치): ruleset 과 CI provenance step 은 **경쟁이 아니라 보완**.

| 축 | SaaS ruleset | CI provenance step (BI-1) |
|----|----|----|
| 검증 대상 | 서명 *존재* (require signed commits) | fingerprint **allow-list 대조** (누가 서명했나) |
| 한계 | 서명이 *있기만* 하면 통과 — Hermes 키 서명도 통과 | 서명 주체가 allow-list 인지 판별 → Hermes-originated reject(G1/Group I) |
| 단독 시 gap | Hermes 자기 서명 commit 을 못 거름 | CI 미연결 시 merge 강제 안 됨 |
| 보완 결합 | ruleset = 서명 require + **CI required check 지정** | CI = fingerprint 대조 결과를 required status 로 |

→ **결론**: anchor 실재 = ruleset(서명 존재) **AND** CI required(fingerprint 대조) 둘 다. CI step 실 코드 = **BI-1 영역**(본 brief 0건, cross-ref). CI required 지정 = ruleset/branch protection 기능 → §3 plan 종속.

### 5.1 ⚠️ enforcement model gap — required check = merge 게이트 (BI4C-3)

**required status check 는 *merge* 게이트이지 *push* 게이트가 아니다.** single-host 1인이 보호 branch 에 **직접 `git push`(PR 미경유)** 하면 — merge 가 없으므로 **required check 가 발생하지 않고 우회**된다(§4 self-bypass 와 *별개* 의 구조적 우회 경로).
- → CI required check 가 *실 게이트* 가 되려면 **(A) ruleset 의 "restrict direct push / PR-required" rule 결합이 전제** (직접 push 차단 → PR 강제 → PR 에서 required check 발효).
- → 진입 gate **G-BI4-6**(§11.1) = "direct-push 차단 ruleset 결합 확인". 이 전제 없는 "CI = 실 게이트" 는 명목.

---

## 6. anchor token Hermes 호스트 외 분리 (CT-2 cross-ref) + R-I-CONFIG-CHANGE T3

### 6.1 token 분리 (BI-4 (ii) ↔ BI-3 CT-2)

- anchor 설정/변경 권한 token(GitHub PAT / fine-grained token / GitHub App)이 **Hermes 호스트에 있으면** → 에이전트가 ruleset 을 변경/비활성화 가능 = anchor 자기 무력화.
- → BI-3 **CT-2(host token) 격리**가 BI-4 anchor 실재의 선결 (BI-3 brief §7.4 CBI3-3 양방향).
- 후보(means, 결정 0건): (a) anchor 변경 token 미주입(Hermes 는 read-only 또는 push-only token 만) / (b) fine-grained token scope 최소화(repo admin·`administration:write` 권한 배제) / (c) token 호스트 외 보관(BI-3 credential 격리 메커니즘 재사용) / **(d) GitHub App installation token**(scope·만료·repo 한정이 PAT 보다 우월 — BI4R-3, 후보 추가).

### 6.2 ruleset 변경 = R-I-CONFIG-CHANGE = T3

- hermes-not-root-of-trust-runtime §2.2 #20: **provenance check 기준·차단 설정 변경 = R-I-CONFIG-CHANGE = T3 (Hermes token 미보유).**
- → anchor(ruleset) 변경은 *에이전트가 자율 수행 불가* = 사람 명시 + (해당 시) 합의 대상. 이것이 self-bypass(§4)의 *에이전트 경로* 차단. (사람 owner 경로는 §4.3·§8 audit.)

---

## 7. GHES pre-receive 대안 (off-host anchor 상승) + Provider Liquidity 긴장

| 차원 | SaaS(GitHub.com) ruleset + CI | GHES pre-receive hook |
|----|----|----|
| anchor 위치 | GitHub 서버 (off-host) — 단 owner 콘솔 변경 가능(§4) | Enterprise Server 서버 측 hook — owner 우회 난이도↑(서버 admin 분리 가능) |
| self-bypass | repo owner = 끌 수 있음 | 서버 운영자 ≠ repo owner 분리 가능 → SoD 상승 |
| 비용/운영 | 0 (SaaS) | 서버 운영·라이선스 비용↑ |
| **Provider Liquidity** | GitHub.com 종속 | GHES 종속 (자가 호스팅 = vendor 종속↓ but 운영 종속↑) |
| MVP 적합 | ✅ single-host MVP | **MVP-6 후보** (multi-host/Enterprise) |

**⭐ Provider Liquidity 긴장 ([[feedback_provider_liquidity]])**: anchor 를 특정 vendor(GitHub) 기능에 못박으면 — "모델/구독 교체가 코드 변경 없이"라는 하드 요구와 긴장. 단 anchor = *git remote 정책*이지 *모델/LLM provider*가 아니므로 직접 충돌은 아님. 그러나 **간접 lock-in 은 실재**(git host 교체 시 anchor 재구축 = "코드 변경 없이 교체" 정신 위배) → "직접 충돌 아님"은 맞되 *불충분*.

### 7.1 anchor 2층 직교 추상화 모델 (BI4R-3 — 설계 언어, 결정 고정 아님)

Provider Liquidity 긴장을 *구조적으로* 해소하는 설계 언어 = anchor 를 **2층 직교**로 분해:

| 층 | 내용 | vendor 종속 | 중립화 |
|----|----|----|----|
| **층1 — 신뢰 기준** | 누구 서명을 신뢰하나 = SSH/GPG `allowed_signers` / fingerprint allow-list | **중립** (어느 host/CI/로컬 hook 에서도 동일) | ✅ 가능 (BI-3 1순위 권고 답습) |
| **층2 — 집행 매체** | 무엇으로 차단하나 = ruleset / branch protection / CI required / GHES pre-receive / Rekor | 매체별 상이 | △ 후보 다수 열거(하드코딩 금지) |

→ **권고(결정 아님)**: **신뢰 기준 = vendor 중립 유지(`allowed_signers`/fingerprint), 집행 매체 = 후보 다수 열거 — 어느 단일 vendor 매체로도 하드코딩 금지** (BI-3 §10 "토큰 벤더·IdP 하드코딩 금지, 후보 열거 유지"와 동형). 결정 = entry.

---

## 8. origin replace / remote 교체 위험 (BI-4 (iv)) + BI-5 audit cross-ref

- **위험**: anchor(ruleset)가 origin 에 걸려 있어도 — (a) `git remote set-url` 로 다른 remote 로 교체 / (b) 새 repo 생성 후 force-push / (c) history rewrite(rebase·filter-branch)로 서명 commit 우회 — 시 anchor 가 *적용 범위 밖*으로 이탈.
- **차단 인터페이스 (cross-ref, 본 brief 0건)**:
  - **BI-5 audit**: append-only git remote audit sink — remote 교체/rewrite 를 *사후 탐지*. (audit write credential 재귀 = BI-3 CT-4.)
  - **G4(history rewrite Layer)**: `g4-history-rewrite-layer5-anchor-poc` / `g4-rewrite-defense-layer234-poc` 선행 PoC — rewrite 방어 4 layer.
- **명문 요구 (BI-4 (iv))**: anchor 실재성 보고 시 "origin replace/rewrite 로 우회 가능, 이는 anchor 자체가 아니라 audit(BI-5)·rewrite 방어(G4)가 담당" 경계를 명시 → anchor 의 보호 범위 오독 차단.
- **⭐ CBI-2 명목 anchor 와 직접 연결 (BI4R-4)**: "ruleset 을 켰으니 anchor 실재"는 **origin 자체를 바꾸면 무의미** — 즉 origin replace 는 anchor *약화*가 아니라 anchor 보호 *범위 이탈*. §2 CBI-2(명목 anchor 금지) 옆에 "anchor 보호 *범위*의 거짓 안전감(범위 밖 우회)" 으로 명문해야 anchor 과신 차단.
- **외부 미러 cross-check (CN-C3/BI4R-5 — 후보 보존)**: 別 remote(예: GitLab/Codeberg/self-hosted bare)에 push-only 미러 + 주기 해시 cross-check → origin ruleset off 해도 *미러↔origin history 불일치* 즉시 탐지. **한계**: 미러도 동일 owner credential = 동일 침해 경계 회귀(§9 동형) — 단 **2 vendor 동시 침해** 필요로 silent 비용↑(Provider Liquidity remote 다변화 정합).

---

## 9. single-host 한계 = 동일 admin 경계 = "수용된 SPOF 위 최선"

- BI-3(§6)과 동형: single-host 1인 = anchor 설정 주체 = commit 작성 주체 = admin → **SoD 구조적 불가**.
- anchor 의 실효 경계: **에이전트(Hermes) 경로 = 차단** (credential 격리 + R-I-CONFIG-CHANGE T3) / **사람 owner 경로 = audit 사후 탐지로 격하**.
- → `f29c772` P2 답습: **"single-host anchor 충족 = 안전 확정 아님, 수용된 SPOF 위 최선."** BI-4 보고서·합의는 이 거짓 안전감 차단을 명문해야 함 (CBI-2 명목 anchor 금지와 한 묶음).
- **MVP-6 상승 경로**: GHES pre-receive(§7) / org 전환 + admin 분리 / multi-host = 진정한 SoD → DEFER.

---

## 10. 영구 핵심 제약 + means/ends

- **means/ends 분리 (ADR-011 §2.1)**: anchor 의 *보장 속성*(ends) = "push/merge 전 host 밖 실 anchor 가 서명·provenance 미충족을 차단" / *수단*(means) = ruleset / CI required / GHES pre-receive (후보, CN-6, 결정 0건). 본 brief = ends 명문 + means 후보 열거, 결정 0건.
- **Hermes ≠ root of trust**: anchor 는 *Hermes 밖* 최소 1개 *실* anchor (명목 금지). Hermes 는 anchor 변경 token 미보유(§6.2).
- **Provider Liquidity ([[feedback_provider_liquidity]])**: §7 — anchor vendor 종속 축 명시, 모델/구독 교체 무관성 유지.
- **5 영구 핵심 제약 5/5 / Provider Liquidity 5-way 약화 0건.**

---

## 11. 진입 gate + Rollback Trigger + anchor observe binary

### 11.1 진입 gate (entry 발효 선결)

| Gate | 조건 | 출처 |
|----|----|----|
| G-BI4-1 | 현 repo public/private 여부 + plan 확인 | **부분 충족** (2026-05-21: `public` 확정 → ruleset 가용 ✅ / push·org-level ruleset = Team plan 종속 잔존, entry 재확인) — §3.3 / C-4 |
| G-BI4-2 | BI-3 CT-2 token 격리 선결 (anchor 변경 token Hermes 외) | §6 / BI-3 |
| G-BI4-3 | self-bypass 차단 범위 명문 (에이전트 경로 차단 / owner 경로 = audit 격하) | §4 / CBI-2 |
| G-BI4-4 | CI required(BI-1) 보완 결합 확인 (서명 존재 + fingerprint 대조 둘 다) | §5 / BI-1 |
| G-BI4-5 | origin replace/rewrite = BI-5/G4 소속 명문 (anchor 보호 범위 경계) | §8 |
| **G-BI4-6** (BI4C-3) | **direct-push 차단 ruleset 결합 확인** (required check = merge 게이트 → restrict direct push/PR-required 전제, §5.1) | §5.1 |
| **G-BI4-7** (BI4C-4) | **public 노출 선결 점검** — 개인 식별정보(이메일 등) plaintext commit redaction (현존: `tgdata200` 3파일) | §3.3 |

### 11.2 Rollback Trigger (anchor 명목화 감지)

- ruleset enforcement status 가 `evaluate`/`disabled` 로 강등 → 명목 anchor 회귀 (audit alert).
- bypass list 에 actor 추가 → self-bypass 통로 재개방.
- anchor 변경 token 이 Hermes 호스트 재유입 → §6 위반.
- **(BI4R-4)** origin url 변경 / force-push / history rewrite 감지 → anchor 보호 범위 이탈 (BI-5 audit cross-ref, §8).
- **(BI4R-4)** CI workflow yaml(`.github/workflows/`) 변경 → 게이트 무력화 시도 (BI-1 read-only 의존).

### 11.3 anchor observe = binary + 실효 종료 조건 (BI4C-1 / BI4C-2)

- observe mode 에서 anchor 는 *enforce* (**`f29c772` line 118**: "observe = runtime 항구 observe(sensor) — enforcement는 anchor만" + **BI-7**) — anchor 는 면책 대상 아님. observe = provenance *판정*의 면책이지 anchor *차단*의 면책 아님. *(BI4C-1: 직전 "G3 §5.5" citation = SPOF Accepted Risk 섹션 오지목·문구 0건 → `f29c772` line 118 + BI-7 로 정정. 후속 72 N-2 동형.)*
- **⭐ anchor 실효 = 적대적 우회 시연 binary (BI4C-2 — 거짓 안전감 차단 핵심)**: BI-3 수단 결정 합의 **CD-5("수단 라벨 ≠ 입증, 계산적 PoC + 적대적 침투 시연 binary")를 anchor 에 대칭 적용.** anchor 실효 충족 = enforcement status 라벨("ruleset 켜짐")이 아니라 **다음 적대적 우회 시연이 *전부 실패* 함이 입증될 때(binary)**:
  - 에이전트가 host token 으로 ruleset off 시도 → **실패**(R-I-CONFIG-CHANGE T3, token 미보유)
  - `--no-verify` push / 직접 push → **server-side reject**(restrict direct push 결합, §5.1)
  - origin replace / force-push → **audit alert**(BI-5)
  - → "ruleset 가용 ✅"(§11.1 G-BI4-1) 는 *후보 조건*이지 *충족*이 아니다. ADR-011 §2.1(b) "격리 환경 PoC 실증" 의무와 한 묶음.

---

## 12. 합의 형태 (풀 3+1 의무)

- BI-4 = 보안 BLOCKING(우선순위 2) + R-I-CONFIG-CHANGE T3 연계 → **풀 3+1 의무** (Reviewer-only 부적격).
- Agent A(구현/정합): plan 가용성 사실 정확성 + CI required 결합 + token 분리 기술. Agent B(보안): self-bypass 역설 + 명목 anchor + audit 격하 경계. Agent C(대안): GHES/org 전환/anchor 추상화 + Provider Liquidity.
- 합의 = **추론적 검증(권고) 한정** — anchor 수단 결정·plan/org/GHES 도입·ruleset/CI/bypass 실 변경·token 분리 발효 = 사용자 명시 + 별도 단계.

---

## 13. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 내용 | 형태 |
|----|----|----|
| (A) | 본 brief(v2) 승인 → BI-4 검증 풀 3+1 합의 | 합의(권고) |
| (B) | ~~현 repo public/private + plan 사실 확인~~ → **완료** (2026-05-21: public 확정, §3.3) | ✅ 완료 |
| (C') ⚠️ | **public 노출 redaction = entry 선결 점검 (BI4C-4 격상)** — 개인 이메일 `tgdata200` 3파일 plaintext 현존 노출 (git history rewrite 얽힘, 별도 단계) | entry 선결 |
| (C) | 다른 BLOCKING 심화 (BI-1 CI fingerprint / BI-5 audit) | 별도 brief |
| (D) | credential 수단 *발효* (BI-3 후속, host OS 확인 후) | 구현 entry |
| (E) | 5 commit push (현 미push) | push |
| (F) | 세션 종료 | 메타 |

---

## 부록 A — 답습 출처

| 출처 | 본 brief 반영 |
|----|----|
| `f29c772` Group I 구현 entry 합의 BI-4 (4요소) | §2 정의 |
| `f29c772` N-3 self-bypass 역설 (Agent C) | §4 |
| `f29c772` GA-2 / Group α C-4 (plan 종속) | §3 |
| `f29c772` CBI-2 (SaaS ruleset = anchor, self-bypass 차단 시) | §2·§4 |
| `bf42d0e` BI-3 brief §7.4 (CBI3-3, CT-2 격리 선결) | §6 |
| `ead5754` BI-3 credential 수단 결정 합의 | §6 cross-ref |
| hermes-not-root-of-trust-runtime §2.2 #20 (R-I-CONFIG-CHANGE T3) | §6.2 |
| ADR-011 §2.1 means/ends | §10 |
| GitHub Docs (rulesets/plan 가용성, 2026-05 web — entry 재확인) | §3.2 |
| `g4-history-rewrite-layer5-anchor-poc` / `g4-rewrite-defense-layer234-poc` | §8 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

GitHub ruleset·branch protection 변경 (rule 생성·수정·삭제 / 대상 branch / enforcement status) / required status check 설정 / bypass list 변경 / CI required 게이트 설정 / **CI workflow 변경** (provenance step / actual run / workflow_dispatch / `on.push.paths` 필터) / **plan 업그레이드 결정** (Free→Pro/Team) / **org 전환 결정** / **GHES 도입 결정** / **실 hook 구현** (pre-commit / pre-receive / server-side / CI provenance step) / **anchor/credential token 실 분리 구성** (token 미주입 / scope 최소화 / 호스트 외 보관 — BI-3 영역) / **audit sink 실 구성** (append-only git remote — BI-5) / Hermes runtime·upstream 변경 / 수단 결정 고정 (anchor 매체 = ruleset / CI / GHES — CN-6) / threshold 고정 / **Operational Readiness PASS (Layer E)** / **Hermes PMO 격상 (Layer F)** / Implementation Evidence PASS 재발효 / MVP-1 exit / Phase α defer-lockdown 변경 / G3 본문 변경 / GP-3 본문 변경 / ADR 본문 자동 갱신 / **원 합의 본문(`f29c772`) 자동 정정** / Group I·α·β·γ 합의 본문 변경 / GP entry 합의 본문 변경 / **Group α C-4 *결정* 발효** (plan 결정 = AR-3 영역) / 다른 BLOCKING(BI-1/2/3/5~10) 자동 진입 / G1 신규 단위 자동 진입 / Backlog #4 자동 진입 / tmux·Obsidian 도입 결정·구현 / 외부 LLM 응답 강제 채택·추가 자동 호출 / 합의 보고서 작성 / commit / push / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
