# 3+1 합의 보고서 — BI-1 CI fingerprint allow-list brief (DRAFT v1)

**일자**: 2026-05-21 (후속 76 — G3 4축 심화의 마지막)
**대상**: `docs/phase0/bi-1-ci-fingerprint-allowlist-brief.md` (DRAFT v1)
**진입 단위**: Group I 구현 entry 합의(`f29c772`) 후속 #4 — BI-1(positive allow-list, 우선순위 2, BI-2 페어) 단독 심화 검증
**합의 형태**: **풀 3+1** (Agent A 구현 / B 품질·안전성 / C 대안 + Reviewer 교차) — 보안 BLOCKING + G3 본문(positive allow-list) 정합 → Reviewer-only 부적격
**판정**: **APPROVE WITH CONDITIONS** (BLOCKING 5 = BI1C-1~5 + 권고 6 = BI1R-1~6)
**합의 권위**: 추론적 검증(권고) 한정 — allow-list 매체 결정·SSH `allowed_signers` 채택·CI 실 코드·`.github/workflows/`·ruleset 실 변경·commit·push = 모두 사용자 명시 + 별도 단계. 본 보고서는 어떤 코드/설정도 변경하지 않음.

---

## 0. 검토 대상 및 권위

- 대상 = BI-1 brief v1 (positive allow-list = G3 4축 中 차단 *기준* 축, **4축 심화의 마지막**). 합의 = 권고 한정. CI provenance step 실 코드·workflow·ruleset·`allowed_signers` 구성·commit/push = 0건.

---

## 1. 핵심 재검증 결과 (Reviewer 직접 grep/read 확정)

### citation stale 0 — A·B 독립 수렴 → **positive 확정**
- 표본 직접 grep: **line 360**(positive allow-list·author 판정 입력 아님·default-deny ✓) / **line 448**(provenance check 채널·author audit 사후 대조 전용 ✓) / **line 789**(credential 미격리 시 allow-list 붕괴 + 거짓 안전감, *verbatim* ✓) / line 221(§2.5 #2 `.github/workflows/` T3 ✓) / line 460·328·464·273·810·1127 全 정합.
- → **citation stale 0 확정. BI-3 N-2 → BI-4 §11.3 → BI-5 차단조건 #2 3연속 stale 패턴 *단절*** (직접 grep 대조 의무 답습 효과). 답습 정합성 회복 = positive 신호.

### A-BI1-1 — §10 미서명 reject = ruleset 결합 의존 → **기술 재검증 타당 (BLOCKING)**
- §10 line 192 시연 #2 "미서명 commit → reject (default-deny)" = 인접 시연(#3 BI-2 / #4 §7)은 cross-ref 보유하나 **미서명 case 만 §5 미연결**.
- 기술 확정: `git verify-commit`/`ssh-keygen -Y verify` 은 *서명 존재 시* signer 검증만 → 미서명 자동 reject = **CI default-deny 로직(서명 부재=reject) + ruleset required-signature(서명 존재 강제) 결합**으로만 성립. §3.2 line 111 이 "미서명=default-deny" 명제는 담으나 §10 시연이 §5(C3)와 미배선 → SSH 단독 미서명 reject 오독 위험.

### BB-1 — §13.2 Rollback owner 경로/능동 감지 부재 → **BI5C-2 부분 재발 확정 (BLOCKING)**
- §13.2 (line 233-236) 4 trigger 全 결과상태 관찰형, **owner 경로 bullet 부재**. 대조: BI-5 §12.2 (line 269)는 "⭐ owner self-bypass (BI5C-2 b)" bullet 을 binary 범위 밖 caveat 포함 명시 → **BI-1 §13.2 가 BI-5 §12.2 와 비대칭**. 능동 감지 메커니즘(회귀테스트 fingerprint→author FAIL) 부재도 사실.

### BB-3 — §9 owner self-bypass (d)(e) 누락 → **확정 (BLOCKING)**
- §9 (line 180-182) = (a) allow-list Hermes 키 추가 / (b) workflow step 제거 / (c) CI required check 해제 **3종 한정**. (d) 신뢰 개인 키 Hermes 재주입(§8 line 171 역경로의 owner 능동 경로)·(e) 백업 키(BI-9) **둘 다 부재**.

### C gitsign — §4 매체 표 통째 누락 → **BI-5 비대칭 확정 (BLOCKING, 병치 권고)**
- BI-1 §4 표(line 119-123) = SSH/GPG/ruleset+CI **3행, sigstore/gitsign 행 없음**. "sigstore" 1회 = §14 line 243 역할배정 note 뿐. 대조: BI-5 §4 표 "Sigstore Rekor transparency log (CBI-4)" 1급 행. → 비대칭 확인. 채택 아님 — 후보 병치·MVP-6.

---

## 2. 교차 비교

| # | 항목 | A | B | C | 분류 |
|---|------|---|---|---|------|
| 1 | 판정 = APPROVE WITH CONDITIONS (구조 견고) | ✅ | ✅ | ✅ | **일치** |
| 2 | citation stale 0 (3연속 패턴 끊김) | ✅ | ✅ | — | **일치(A·B)** |
| 3 | positive allow-list / default-deny / author≠판정입력 (line 360/448/1127) | ✅ | ✅ | ✅ | **일치** |
| 4 | C3 ruleset 단독=명목, CI fingerprint 대조 보완 | ✅ | ✅ | ✅ | **일치** |
| 5 | credential(BI-3) 선결, 미격리 시 붕괴(line 789) | ✅ | ✅ | ✅ | **일치** |
| 6 | owner self-bypass = §9 가 binary 범위 밖 *선제* 분리 | — | ✅ | ✅ | **일치(B·C)** |
| 7 | Provider Liquidity 2층 / allowed_signers vendor 중립 | ✅ | — | ✅ | **일치(A·C)** |
| 8 | A-BI1-1 §10 미서명 reject = ruleset 결합, §10↔§5 미연결 | ✅ | △ | — | **부분(A 심화)** |
| 9 | BB-1 §13.2 Rollback owner/능동감지 부재 = BI5C-2 재발 | — | ✅ | — | **누락(B 단독)** |
| 10 | BB-2 observe FN 거짓안전감 §10/§13.2 미전파 | — | ✅ | — | **누락(B 단독)** |
| 11 | BB-3 §9 (d)재주입 (e)백업키 누락 | — | ✅ | — | **누락(B 단독)** |
| 12 | C gitsign §4 표 통째 누락 (BI-5 비대칭) | — | — | ✅ | **누락(C 단독, 최중대)** |
| 13 | C 누락 2~4 (SSH CA / GHES pre-receive / in-toto) | — | — | ✅ | **누락(C 단독, 보존)** |
| 14 | GPG 폐기/만료 인프라 trade-off | ✅ | — | ✅ | 부분 |

**집계: 일치 7 / 부분 3 / 불일치 0 / 누락 7**

---

## 3. 핵심 수렴 판정 — BI5C-2 패턴 BI-1 *부분* 재발

**판정: 부분 재발 — §9/§10 선제 해소, §13.2·observe 두 곳 잔여.**

brief 는 BI-5 BI5C-2("owner self-bypass 거짓안전감 미전파")를 학습해 **§9(owner self-bypass = 명목화 현실 경로)·§10(binary = 에이전트 경로 한정, owner = §9 수용 SPOF, line 196)에 선제 반영** = 호평할 진보. 그러나 동일 패턴이 **(잔여 1) §13.2 Rollback Trigger(owner bullet·능동 감지 부재, BB-1) + (잔여 2) observe mode(§10 binary 가 enforcement 미발효=신호만 통과를 미구분, BB-2)** 두 곳에 남음. → 거짓 안전감 차단 완결을 위해 §13.2·observe 잔여를 BLOCKING 으로 닫는다.

---

## 4. 최종 판정 — APPROVE WITH CONDITIONS

### BLOCKING 5건 (BI1C-1~5)

| # | 조건 |
|---|----|
| **BI1C-1** | §10 시연 #2 "미서명 commit → reject"에 §5 cross-ref 명문 — 미서명 reject = SSH `allowed_signers` *단독* 아님, **ruleset required-signature(서명 존재 강제) + CI default-deny(서명 부재=reject) 결합**으로만 성립. `git verify-commit`/`ssh-keygen -Y verify` = 서명 존재 시 signer 검증만. §10↔§5 배선 |
| **BI1C-2** ⭐ | §13.2 Rollback Trigger 에 **owner 경로 bullet + 능동 감지 메커니즘** 추가 — BI-5 §12.2 대칭(owner self-bypass = §9 수용 SPOF, binary 범위 밖 caveat). "author 회귀" = 결과상태만 → 능동 감지(fingerprint→author 변경 시 회귀테스트 FAIL) 명문. BI5C-2 패턴 BI-1 부분 재발 차단 |
| **BI1C-3** | observe mode FN 거짓안전감을 §10 binary·§13.2 에 전파 — §10 "Hermes 키 서명→reject" 시연이 observe 중엔 "신호만·enforcement 미발효=통과"임을 구분. "binary 통과=안전 확정"+"observe라 차단 0" 두 거짓안전감 다층 명문(BI-5 §6 대비) |
| **BI1C-4** | §9 owner self-bypass 목록에 **(d) 신뢰 키 개인 키 Hermes 재주입(§8 역경로) + (e) 백업 키(BI-9) 노출** 추가 (현 (a)(b)(c) 불완전) |
| **BI1C-5** | §4 매체 후보 표에 **sigstore/gitsign keyless 행 병치** + N-1/CBI-4 cross-ref — BI-5 §4 Rekor 1급 병치 비대칭. gitsign = 정적 키 목록 부담 0(신뢰=OIDC 신원)·GitHub 계정 재사용·Rekor 로그로 allow-list 판정 자체 audit → anchor(BI-4 E)+audit(BI-5)+allow-list(BI-1) **3축 1회 도입 시너지**. trade-off(OIDC 새 의존축·인증서 단명성·public 메타) 명시. **채택 아님 — 후보 병치·MVP-6 DEFER** |

### 권고 6건 (BI1R-1~6)

| # | 권고 |
|---|----|
| **BI1R-1** | §7 N-4 재귀 닫힘 = §2.5 #2 강제가 pre-commit hook(차단권 아님)이므로 BI-2 server-side anchor 결합까지 명문 (A R-1) |
| **BI1R-2** | §부록A 정합 노이즈 주석 — brief 360/448 정확하나 합의 doc `f29c772` 는 360/784 인용. + citation stale 0 positive 평가 명문 (A R-2 + B BR-4) |
| **BI1R-3** | §3 서명 scope = commit 객체 전체·author 변경 시 무효·replay 방어 명문 (B BR-2) |
| **BI1R-4** | §11 coverage 경계 = merge/squash/force-push commit fingerprint 대조 적용 범위 (B BR-3) |
| **BI1R-5** | §10 CI reject ↔ required status check 배선 검증 시연 (B BR-1) |
| **BI1R-6** | 후보 보존(채택 0) — SSH CA 서명(CA키=새 SPOF) / GHES pre-receive 서버측 판정(§7 재귀 구조 회피, SaaS 불가=MVP-6) / in-toto·SLSA attestation(commit-layer 범위 밖) + GPG 폐기/만료 인프라 성숙도 trade-off (C 누락2~4 + A R-3) |

### 거짓 안전감 차단 (핵심 평가)
brief 가 BI-5 BI5C-2 를 §9/§10 에 **선제 흡수**한 것은 진보로 호평하나, **동일 패턴이 §13.2 Rollback(owner bullet·능동 감지 부재)·observe FN(§10/§11) 두 곳에 잔여**(BI1C-2/3) = BI5C-2 의 BI-1 부분 재발. "owner self-bypass = binary 범위 밖" 명제가 §9/§10 에는 박혔으나 *감지·관찰기간* 으로 전파되지 못해 "에이전트 시연 통과 + Rollback 켬 = allow-list 안전" 두 번째 미끄럼 잔존. 한편 **citation stale 0 확정 = 3연속 stale 패턴 단절**(line 360/448/789 verbatim 재확인) = 답습 정합성 회복 positive.

---

## 5. 종합 결론

BI-1 brief v1 = **APPROVE WITH CONDITIONS** (BLOCKING 5 BI1C-1~5 + 권고 6 BI1R-1~6). 교차 = 일치 7 / 부분 3 / 불일치 0 / 누락 7. 핵심: (i) **citation stale 0 확정 = BI-3 N-2→BI-4 §11.3→BI-5 차단조건#2 3연속 stale 패턴 단절**(직접 grep 의무 답습 효과, positive). (ii) **A-BI1-1** = §10 미서명 reject 가 SSH `allowed_signers` 단독 아닌 ruleset required-signature 결합 의존 → §10↔§5 배선(BI1C-1). (iii) **BI5C-2 부분 재발** = §9/§10 선제 해소했으나 §13.2 Rollback(owner·능동감지)·observe FN 두 곳 잔여(BI1C-2/3). (iv) **§9 owner 목록 (d)신뢰키 재주입·(e)백업키 누락**(BI1C-4). (v) **gitsign/sigstore §4 매체 표 통째 누락** = BI-5 §4 Rekor 1급 병치 비대칭, 3축 1회 도입 시너지로 병치 권고(BI1C-5, 채택 아님·MVP-6). 본 합의는 추론적 검증(권고) 한정이며 allow-list 매체 결정·CI 실 코드·workflow·ruleset 실 변경·commit·push 0건이다. **4축(BI-3/4/5/1) 단독 심화 완주** → 다음 = 4축 BLOCKING 통합 정리(옵션 B) 또는 credential 수단 발효(옵션 C) = 사용자 결정 영역.

---

## 부록 — Agent 관점 요약

| Agent | 관점 | 핵심 |
|------|------|------|
| **A** (구현) | "동작하는가?" | citation 10 line 전수 대조 = stale 0(3연속 패턴 끊김). SSH allowed_signers·ruleset 보완·페어·재귀 정확. **A-BI1-1** §10 미서명 reject = ruleset 결합 의존(§10↔§5 미연결) |
| **B** (안전성) | "견고한가?" | §3 default-deny·§8 credential·§9/§10 owner self-bypass 선제 해소 우수. **BB-1** §13.2 Rollback owner/능동감지 부재(BI5C-2 재발) / **BB-2** observe FN 미전파 / **BB-3** §9 (d)(e) 누락 |
| **C** (대안) | "더 나은 방법?" | means/ends·C3·2층 충실. **gitsign §4 표 통째 누락**(BI-5 Rekor 병치 비대칭, 3축 1회 시너지) / SSH CA·GHES pre-receive·in-toto 후보 보존 |
| **Reviewer** | "최선 합의?" | 직접 grep 재검증(A-BI1-1 기술 확정·BB-1/3 확정·gitsign 비대칭 확정·citation stale 0 표본 verbatim) → APPROVE WITH CONDITIONS, BLOCKING 5 + 권고 6. BI5C-2 부분 재발 판정 |
