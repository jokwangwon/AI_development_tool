# 3+1 합의 보고서 — BI-4 GitHub plan·ruleset 가용성 brief (DRAFT v2)

**일자**: 2026-05-21
**대상**: `docs/phase0/bi-4-github-plan-ruleset-availability-brief.md` (DRAFT v2)
**진입 단위**: Group I 구현 entry 합의(`f29c772`) 후속 #2 — BI-4(external anchor 실재성, 우선순위 2) 단독 심화 검증
**합의 형태**: **풀 3+1** (Agent A 구현 / B 품질·안전성 / C 대안 + Reviewer 교차) — 보안 BLOCKING + R-I-CONFIG-CHANGE T3 → Reviewer-only 부적격
**판정**: **APPROVE WITH CONDITIONS** (BLOCKING 5 = BI4C-1~5 + 권고 6 = BI4R-1~6)
**합의 권위**: 추론적 검증(권고) 한정 — citation 정정·anchor binary 종료 조건 명문·redaction·plan 표 교정·수단 결정·실 변경·commit·push = 모두 사용자 명시 + 별도 단계. 본 보고서는 어떤 코드/설정도 변경하지 않음.

---

## 0. 검토 대상 및 권위

- 대상 = BI-4 brief v2 (v1 + G-BI4-1 사실 확인 반영 — repo `jokwangwon/AI_development_tool` = **`public` 확정**, 2026-05-21 비인증 API).
- 합의 = 권고 한정. 실 ruleset/branch protection/CI/bypass 변경, plan/org/GHES 도입 결정, 수단 결정 고정, redaction, commit/push = 0건.

---

## 1. 핵심 재검증 결과 (Reviewer 직접 grep/read 확정)

### BI4C-1 — §11.3 citation stale → **사실 확정 (BLOCKING)**
- brief line 268: `observe mode 에서 anchor 는 enforce (G3 §5.5 "observe 라도 anchor 만 enforce")`.
- 직접 확인: `hermes-not-root-of-trust-runtime.md` **§5.5 = "SPOF Accepted Risk" 섹션** — 인용 문구는 G3 본문 **0건** (grep 전수 = brief 자신만 매치).
- 실 출처 = **`f29c772` consensus line 118** (`observe | runtime 항구 observe(sensor) — enforcement는 anchor만`) + **BI-7**.
- → 후속 72 N-2 citation 오류(§ 번호 오지목)와 **동형**. 같은 엄밀성으로 BLOCKING.

### BI4C-4 — 개인 이메일 public 노출 → **사실 확정 (조건부 BLOCKING)**
- `grep -rn "tgdata200" docs/` = **3개 파일 plaintext commit 확정** (`docs/review/3plus1-consensus-2026-05-13-{mvp1-pass-c1-k2, adr-012-event-enum, k2-permissions}` 각 "승인자: 사용자 (`<redacted>`)").
- repo = public 확정 → **현존(현재 진행형) 노출**. brief §13 (C') "옵션" 격하는 위험 과소평가.
- → entry 발효 *선결* 점검 항목 격상. (redaction 실 변경 = 별도 단계. `ghp_` 매치 = redaction 패턴 정의 예시 = false positive.)

### BI4C-3 — CI required check direct-push 우회 → **사실 확정 (BLOCKING)**
- §3.1 (C) CI required status check = "merge 거부", (A) ruleset = "push/merge 거부". required status check 는 *merge* 게이트이고 **직접 `git push`(PR 미경유) 차단은 별도 ruleset(restrict direct push / PR-required)에 종속**. brief 가 이 전제 미명문 (혼동).
- → public repo 결론 무영향이나 anchor 실효 enforcement-model gap = 사실. BLOCKING.

### A-1 — §3.2 plan 표 사실 정확성 → 부분 인정 (권고)
- 표는 line 124("2026-05 web 확인 후보 — entry 재확인 의무") + line 75 권위 한계 + line 254 G-BI4-1 로 **이미 비권위 입력 명시** → 사실 고착 위험 낮음. 표 교정 권고는 유효(권고 등급).

---

## 2. 교차 비교

| # | 항목 | A | B | C | 분류 | 처리 |
|---|------|---|---|---|------|------|
| 1 | self-bypass(§4)·명목 anchor(CBI-2)·거짓안전감(§9) 골격 정확 | ✅ | ✅ | ✅ | **일치** | 채택(통과) |
| 2 | BI-4 = 우선순위 2, BI-3 다음, 양방향 인터페이스 | ✅ | ✅ | ✅ | **일치** | 채택 |
| 3 | §5 ruleset↔CI 보완 명제 정확 | ✅ | ✅ | (전제) | **일치** | 채택 |
| 4 | §6.2 R-I-CONFIG-CHANGE T3 / token 분리 정합 | ✅ | ✅ | — | 부분 | 채택 |
| 5 | §11.3 citation stale (G3 §5.5 오류) | — | ✅ | — | 누락→재검증 확정 | **BLOCKING BI4C-1** |
| 6 | CD-5 binary 입증이 anchor 에 미적용 | — | ✅ | — | 누락→채택 | **BLOCKING BI4C-2** |
| 7 | 개인 이메일 public 노출 현존 | — | ✅ | — | 누락→재검증 확정 | **BLOCKING BI4C-4** |
| 8 | CI required = direct-push 우회 gap | ✅ | — | — | 누락→확정 | **BLOCKING BI4C-3** |
| 9 | §3.2 표 사실 교정 | ✅ | (정합통과) | — | 부분 | 권고 BI4R-1 |
| 10 | Rekor 후보표 §3.1 행 병치(BI-3 M5 비대칭) | — | — | ✅ | 누락→채택 | **BLOCKING BI4C-5** |
| 11 | git 표준 서명 = vendor 중립 anchor 기준 분리 | (token) | — | ✅ | 누락 | 권고 BI4R-2 |
| 12 | anchor 2층(기준×집행) 추상화 / Provider Liquidity | AR-3 | — | ✅ | 부분 | 권고 BI4R-3 |
| 13 | 제목 "DRAFT v1" vs Status "v2" 불일치 | — | ✅ | — | 누락→확정 | 권고 BI4R-6 |
| 14 | 현 순서(BI-3→BI-4) 유지 | (전제) | — | ✅ | 부분 | 채택 |

**집계: 일치 3 / 부분 4 / 불일치 0 / 누락 7** (재검증으로 5건 사실 확정).

---

## 3. 최종 판정 — APPROVE WITH CONDITIONS

### BLOCKING 5건 (BI4C-1~5)

| # | 조건 |
|---|----|
| **BI4C-1** | §11.3 line 268 citation 정정 — "G3 §5.5"(SPOF Accepted Risk, 문구 0건) → **`f29c772` line 118 + BI-7**. 후속 72 N-2 동형. (정정 = 별도 단계, 본 합의는 지목까지) |
| **BI4C-2** ⭐ | **거짓 안전감 핵심** — CD-5("수단 라벨 ≠ 입증, 적대적 침투 시연 binary")를 anchor 에 대칭 적용. §11.3 "anchor observe=binary"에 **종료 조건 명문**: anchor 실효 = 에이전트 경로 실 우회 불가능 시연(token→ruleset off 실패 / `--no-verify` push→server reject / origin replace→audit alert) binary 통과, enforcement status 라벨 ≠ 충족. ADR-011 §2.1(b) 동형 |
| **BI4C-3** | §3.1 (A)/(C) + §5 에 "required status check = merge 게이트, 직접 push 차단 = 별도 ruleset(restrict direct push/PR-required) 종속" 명문 + 진입 gate **G-BI4-6** 추가 |
| **BI4C-4** ⚠️ | 개인 이메일 `<redacted>` 3개 파일 plaintext + repo public = **현존 노출**. §13 (C') 옵션 → **entry 발효 선결 점검 격상** (redaction 실 변경은 별도) |
| **BI4C-5** | Sigstore Rekor transparency log(제3자 append-only = self-bypass 구조적 강함 + origin replace 외부 입증)을 **§3.1 anchor 후보표 (E) 행 병치**(채택 아님) — BI-3 §4 M5 대칭. CBI-4 = BI-3·BI-4 cross-ref |

### 권고 6건 (BI4R-1~6)

| # | 권고 |
|---|----|
| **BI4R-1** | §3.2 plan 표 entry 재확인 시 현행 GitHub Docs 재검증·교정 (비권위 입력 명시는 이미 충족) |
| **BI4R-2** | "anchor 집행 매체(vendor 종속) ⊕ anchor 신뢰 기준(SSH/GPG allowed_signers = 중립)" 분리 명문 (BI-3 1순위 권고 cross-ref 답습, 재결정 아님) |
| **BI4R-3** | anchor "신뢰 기준 × 집행 매체" 2층 직교 추상화 모델 = Provider Liquidity 구조 해소 설계 언어로 §7 격상(결정 고정 아님) + §6 token 후보에 GitHub App installation token 추가 |
| **BI4R-4** | §4 self-bypass 재귀 닫힘 명제(단일 anchor 불가, audit 결합으로만 격하) + §8 origin replace ↔ CBI-2 명목 anchor 직접 연결 + §11.2 Rollback Trigger 에 origin replace/rewrite 추가 + §4.3 CI 재귀에 "workflow yaml = repo 내 commit 변경 가능" 우회 + BI-1 read-only 의존 cross-ref |
| **BI4R-5** | 외부 미러 cross-check = origin replace 저비용 대안 후보 추가(동일 owner credential = 동일 침해 경계 회귀 한계 명시) |
| **BI4R-6** | 제목 line 1 "DRAFT v1" → "DRAFT v2" 정합 정정(경미) |

### 거짓 안전감 차단 (핵심 평가)
**BI4C-2 가 본 brief 거짓 안전감 차단의 핵심.** brief 는 §4·§9·CBI-2 로 "ruleset 존재 ≠ 안전 확정"을 명문하나 **"anchor observe=binary"의 종료 조건 부재**가 BI-3 CD-5 가 막은 함정("수단/라벨을 켰으니 anchor 됐다고 믿는 명목화")을 anchor 축에서 재개방. anchor 실효 = enforcement status 라벨 ≠ 입증, **에이전트 경로 실 우회 불가능의 적대적 시연(binary)** 이어야 함을 §11.3 에 명문 — CD-5·ADR-011 §2.1(b)와 한 묶음.

---

## 4. 종합 결론

BI-4 brief v2 는 public 확정으로 plan 종속 worst-case 를 정당하게 소거하고 쟁점을 self-bypass·token 분리로 정확히 좁혔으며, 다수 citation·정합성(`f29c772` line 118/147, CD-5, R-I-CONFIG-CHANGE §2.2 #20, ADR-011 §2.1)이 직접 재검증을 통과한 견고한 심화 문서로 **APPROVE WITH CONDITIONS** 가 타당하다. 가장 무게 있는 발견 셋: ① §11.3 "G3 §5.5" citation 이 직접 grep 결과 SPOF Accepted Risk 섹션을 오지목하고 인용 문구가 G3 본문에 0건임이 확정(후속 72 N-2 동형, BI4C-1), ② BI-3 수단 결정 합의 CD-5("수단 라벨 ≠ 입증, binary 침투 시연")가 anchor 축에 대칭 적용되지 않아 "anchor observe=binary"의 종료 조건 부재로 명목 anchor 거짓 안전감을 재개방하는 핵심 결함(BI4C-2), ③ 개인 이메일이 public repo 3개 commit 파일에 plaintext 로 현존 노출됨이 grep 으로 확정되어 entry 선결 점검 격상이 필요한 점(BI4C-4)이다. CI required check 의 direct-push 우회 enforcement-model gap(BI4C-3)과 Rekor 후보표 비대칭(BI4C-5)을 더해 BLOCKING 5건, 권고 6건이다. 교차 = 일치 3 / 부분 4 / 불일치 0 / 누락 7(재검증 5건 확정). 본 합의는 추론적 검증(권고) 한정이며 citation 정정·anchor binary 종료 조건 명문·redaction·plan 표 교정·수단 결정·실 변경·commit·push 는 모두 사용자 명시 + 별도 단계의 권한이고, 본 보고서는 어떤 파일도 편집/생성하지 않았다.

---

## 부록 — Agent 관점 요약

| Agent | 관점 | 핵심 |
|------|------|------|
| **A** (구현) | "동작하는가?" | public 확정으로 worst-case 정당 소거. §3.2 표 사실 교정(권고)·CI required direct-push 우회 gap(BI4C-3)·token 분리 fine-grained PAT/GitHub App 실현 가능 |
| **B** (안전성) | "견고한가?" | self-bypass·CBI-2 골격 APPROVE. §11.3 citation stale(BI4C-1)·CD-5 binary 미적용(BI4C-2)·개인 이메일 현존 노출(BI4C-4) |
| **C** (대안) | "더 나은 방법?" | Rekor 후보표 병치(BI4C-5)·allowed_signers 중립 기준 분리·2층 추상화·외부 미러 — Provider Liquidity 구조 해소 |
| **Reviewer** | "최선 합의?" | 직접 grep 재검증으로 누락 5건 사실 확정 → APPROVE WITH CONDITIONS, BLOCKING 5 + 권고 6 |
