# Backlog #3 Group I (Hermes-originated commit auto-reject) 단독 풀 3+1 합의 보고서

> **본 합의 = Backlog #3 (T3 영역) 中 Group I (Hermes-originated commit auto-reject) *합의 형태 판정 + 식별·차단 메커니즘 설계 권위 권고* 발행 한정** — Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) Phase 2 (Independent Analysis, 병렬 독립 분석) + Reviewer (검토 에이전트) Phase 3-4 (교차 비교 + 합의 도출) 통합. **판정: T3 풀 3+1 의무 (만장일치) + 외부 5 보강점 5/5 채택 + 6 BLOCKING / 3 조건부 안전 조건 + framing N1**.
>
> 본 합의의 어떤 §도 그 자체로 (i) **Hermes runtime 실 구현** (orchestrator / container / agent runtime 본문), (ii) **Hermes-originated commit 실 차단 hook 구현** (git pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문), (iii) **GitHub ruleset / branch protection 실 변경** (signed commit required / required status check / force push 차단 / bypass 정책), (iv) **Hermes upstream 변경** (Dockerfile / `hermes-version.yaml` / upstream PR), (v) **수단 결정 *고정*** (식별 방법·차단 지점·보호 범위 최종 결정), (vi) **threshold 고정** (observe mode 기간 등), (vii) CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경, (viii) **Operational Readiness PASS (Layer E) 선언** / **Hermes PMO 격상 (Layer F) 선언**, (ix) **MVP-1 exit 발효** (GP-3 5/5 + GP-5 5/5 별도), (x) **Phase α defer-lockdown 변경**, (xi) **G3 (`hermes-not-root-of-trust-runtime.md`) §2.2 #20 / §2.5 / §2.6 / §4 / §5.5 본문 변경** (특히 line 448/784 detection 메커니즘 본문 교정 — 별도 단계), (xii) ADR 본문 자동 갱신 (ADR-008 / ADR-011 / ADR-012), (xiii) Group α / β / γ-1 / γ-2 합의 본문 변경 / GP entry 합의 본문 변경, (xiv) Backlog #4 · Backlog #6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입, (xv) 외부 LLM 응답 *결론 강제 채택* (응답 = 입력 한정 + 본 합의 평가 대상) / 외부 LLM 추가 자동 호출, (xvi) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (Group I 풀 3+1 합의 진입 — brief v2 승인 후)
**상태**: 합의 판정 발행 — Phase 5 (Report) 완료. 식별 방법·차단 지점·framing·G3 본문 교정의 실 *결정/구현* = 사용자 명시 + 별도 단계
**합의 판정**: **T3 풀 3+1 의무 / Reviewer-only 부적격 (만장일치)** + 외부 5 보강점 **5/5 채택** (3 BLOCKING + 1 조건부 + 1 채택) + **6 BLOCKING / 3 조건부** 안전 조건 + framing **N1**
**합의 영역**: Group I (Hermes-originated commit auto-reject) **합의 형태 판정 + 식별·차단 메커니즘 설계 권위 권고 한정** — 실 변경 0건

**상위 권위**:
- Group I brief v2 (본 합의 직접 source) = `docs/phase0/group-i-hermes-originated-commit-autoreject-full-3plus1-brief.md` (DRAFT v2, 외부 응답 1건 회수 반영)
- 외부 LLM 응답 회수 = `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-response-gpt.md` (GPT-5.5 Thinking, Q1~Q8 + 5 보강점 + framing 권고 — **입력 한정, 본 합의 평가 대상**)
- 외부 LLM 의뢰서 = `docs/external-review/2026-05-20-group-i-hermes-originated-commit-autoreject-review-request.md`
- Group α 합의 = `3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (C-2 "AI agent self-approval 차단 = Group I 결합 필수" + §6.1 + §8 옵션 (E))
- G3 = `hermes-not-root-of-trust-runtime.md` §2.2 #20 (T3 절대 금지) + §2.5 (보호 대상 16건) + §4 (합의 인프라 순환 권위) + §4.5 (합의 결과 처리 권한) + §5.5 (SPOF) + **line 448/784 (현 detection 메커니즘 = metadata-기반 single-author 비교)**
- ADR-011 §2.1 means/ends + §2.4 T3 영역 + 외부 LLM 입력 원칙 (응답 = 입력 한정)
- ADR-012 §2.12 변조 차단 4항목 中 (3) git commit + §원칙 12 (single-host SPOF / multi-host Layer 3/5)
- 5 영구 핵심 제약 #1 (Hermes ≠ root of trust) + #4 (단일 source-of-truth) + Provider Liquidity 5-way

---

## 0. 종합 판정 (한 문단)

세 Agent는 **(1) Group I 진입 적격, (2) T3 풀 3+1 의무 / Reviewer-only 부적격, (3) 외부 5 보강점 전부 채택 또는 조건부 채택, (4) framing 권고 N1(명칭 유지 + 중심 명제 명시) 선호, (5) runtime=sensor·최종 reject=Hermes 밖이 핵심 안전 조건**이라는 데 완전 일치한다. 가장 무게 있는 교차 발견은 Agent A·B가 독립적으로 짚고 Reviewer가 G3 원문(line 448 "author/committer + audit log cross-reference", line 784 "기준 자체가 단일 author 비교")으로 검증한 사실 — **현 G3 본문이 정확히 외부가 약하다고 지적한 metadata-기반 negative detection을 명시하고 있다.** 따라서 positive allow-list 권고는 새 제안이 아니라 현 G3 설계의 구조적 결함 교정이며, 이것이 본 합의의 핵심 BLOCKING 사유다. 단 brief 금지사항(G3 본문 변경 0건)과 양립하려면 결함은 "Group I 합의 권고로 식별·기록"하되 G3 본문 교정은 별도 단계로 분리해야 한다. 본 합의는 **추론적 검증(권고) 한정 — 발효·실 채택·G3 본문 변경은 사용자 명시 + 별도 단계.**

---

## 1. 교차 비교 매트릭스

### 1.1 일치 (Consensus) — 3개 모두 동의

| # | 합의 항목 | A | B | C |
|---|---------|---|---|---|
| C1 | **진입 기술/안전/대안 모두 적격** (진입 막을 정도 아님) | ✅ | ✅ | ✅ |
| C2 | **Reviewer-only 부적격, 풀 3+1 의무** (T3 + 새 메커니즘 결정 + self-reference) | ✅ | ✅ | ✅ |
| C3 | **metadata 신호(author/committer/trailer) = root signal 부적격** (spoof 가능) | ✅ | ✅ | ✅ |
| C4 | **positive allow-list (사람 전용 hardware-backed key 서명) 채택** | ✅ | ✅ | ✅ |
| C5 | **runtime reject 단독 = self-reference 역설 → runtime=sensor, 최종 reject=Hermes 밖** | ✅ | ✅ | ✅ |
| C6 | **GHES pre-receive ≠ GitHub.com 기본** — GitHub.com=ruleset+CI provenance | ✅ | ✅ | ✅ |
| C7 | **`.git/` 직접 변조 = commit 검사 사각 → filesystem ACL(§2.5 #1) 책무** | ✅ | ✅ | ✅ |
| C8 | **observe mode / quarantine / patch artifact 채택** (작업 손실 방지) | ✅ | ✅(조건부) | ✅ |
| C9 | **negative-control-only 조항 채택** (PASS = positive evidence 오용 금지) | ✅ | ✅ | ✅ |
| C10 | **credential boundary 실분리 = positive allow-list의 *전제*** (FN > FP 위험) | ✅ | ✅ | ✅ |
| C11 | **R-I-CONFIG-CHANGE 필수** (Hermes는 ruleset/CI token/audit 수정 token 미보유) | ✅ | ✅ | ✅ |
| C12 | **framing = N1 (명칭 유지 + 중심 명제 명시) 선호, 전면 재정의 보류** | ✅ | ✅ | ✅ |
| C13 | **실 구현 = Backlog #6 / Implementation PASS 분리, DESIGN PASS / IMPL PENDING** | ✅ | ✅ | ✅(I-8) |
| C14 | **Group I 단독 차단 불가 — Defense in depth 결합에서만 가치** | ✅ | ✅ | ✅ |

### 1.2 부분 일치 (Partial) — 2개 동의, 1개 이견/추가

| # | 항목 | A | B | C | 분류 |
|---|------|---|---|---|------|
| P1 | **외부 보강점 1(positive allow-list)을 권고가 아닌 BLOCKING으로 *격상***. B는 명시 격상 주장, A는 "필수 조건 6"에 포함(사실상 BLOCKING), C는 frame 전환의 일부로 흡수 | (포함) | ✅ 명시 | (흡수) | B 강조, A·C 실질 동의 |
| P2 | **audit log tamper-resistance / 외부 read-only sink 격리**. A 명시, C 명시(ADR-012 Layer 1/2/5 연계), B는 약하게 언급 | ✅ | (약) | ✅ | A·C 명시 |
| P3 | **observe mode 자체가 FN 통과 구멍** — observe ≠ enforcement 발효 명시 필요. B 강하게 조건화 | (채택) | ✅ 조건 | (채택) | B 단독 강조 |

### 1.3 불일치 (Divergence) — 3개 다른 강조점

| # | 항목 | A | B | C |
|---|------|---|---|---|
| D1 | **문제의 본질 framing** | "auto-reject"가 기술 오독 유도 (line 448 함정) → credential isolation 중심 **명시**로 충분 | metadata→positive 전환을 **BLOCKING 안전 조건**으로 (안전성 관점) | **식별 frame 자체가 잘못** — 식별 정확도 향상이 아니라 **권한 경계 사전 구성(perm-by-construction)으로 식별 불요화** (γ-1 답습) |

> D1은 진정한 충돌이 아니라 **관점차에서 오는 강조 스펙트럼**이다(A=기술 오독 방지 / B=안전 BLOCKING / C=frame 전환). 셋 다 "metadata 중심을 버리고 credential/권한 경계 중심으로" 귀결한다. C의 perm-by-construction이 가장 근본적이며 A·B를 포함한다.

### 1.4 누락 (Gap) — 특정 Agent만 언급

| # | 항목 | 언급자 | 중요도 |
|---|------|-------|-------|
| G1 | **신규 영역: Hermes PR/approval auto-reject** — Group α C-2 직표적은 *approval*이지 commit이 아님. "commit" 고정이 표적을 좁힘 | C 단독 | **높음** (표적 정합) |
| G2 | **신규 sub단위 후보 I-9: credential isolation** | C 단독 | 중간 |
| G3 | **차단 객체 기준 책무 재정렬** (merge/push=Group α, `.git/`=§2.5 ACL, commit 주체화=Group I credential isolation, provenance 판정=Group I sensor 단일 source) | C 단독 | 높음 (#4 단일 source-of-truth 보존) |
| G4 | **single-host 3-layer 명목화 우려** — host 밖 layer 최소 1개를 실 anchor로 의무화해야 #4 실질 | B 단독 | 높음 |
| G5 | **§4.7.2 격상 전 면제 인용 1건 미세 권고** (문서 정합성) | B 단독 | 낮음 |
| G6 | **commit trailer 표준화 (audit 보조 한정)** | C 단독 | 낮음 |

---

## 2. 합의 도출

### 2.1 진입 적격성 + T3/T2 형태 판정

**합의: Group I = T3 보안 enforcement 영역 → 풀 3+1 (Agent A/B/C + Reviewer) *의무*. Reviewer-only 단축 *부적격*.** (C2 만장일치, 이견 0건)

근거 종합:
- **trigger #2 (T3 BLOCKING)**: Group I = G3 §2.2 #20 (T3 절대 금지)의 enforcement.
- **trigger #5 (HIGH)**: 핵심 제약 #1 (Hermes ≠ root of trust) + #4 (단일 source-of-truth) 직결.
- **§5.3 self-reference 구조**: Group I은 합의 인프라 순환 권위 *자체*를 대상으로 하는 결정 — Hermes orchestrated 단축(Reviewer-only) 단독은 메타-편향 통제 부족. G3 §4.2 원칙 2 ("Reviewer-only 또는 외부 LLM이 Hermes 관련 결정에 필수")와 정합.
- **trigger #7**: GPT-5.5 응답 1건 회수로 충족. 추가 vendor는 사용자 결정 영역(의무 아님). 단 Reviewer 권고: Group I은 식별·차단 메커니즘 결정으로 표면적이 넓어 2차 vendor(Gemini 등) 추가 입력이 *바람직*하나 강제 아님.

세 Agent 모두 "신규 식별·차단 메커니즘 결정 발생 = 단순 evidence 흡수 아님"으로 Reviewer-only 부적격에 독립 동의. **C(대안 탐색가)는 신규 결정이 오히려 *늘어난다*(frame 전환 + 신규 영역)고 보아 풀 3+1 필요성을 강화한다.** → 부적격 판정 견고.

### 2.2 외부 5 보강점 최종 합의

| # | 보강점 | 최종 판정 | 근거 |
|---|--------|----------|------|
| **1** | positive allow-list > negative detection | **채택 (BLOCKING)** | 만장일치(C3+C4). G3 line 448/784 원문이 metadata-기반임을 Reviewer 확인 — 현 설계 결함의 직접 교정. B 격상 주장 + A 필수조건 포함 + C frame 흡수 = 사실상 3자 BLOCKING 동의 (P1) |
| **2** | GHES pre-receive ≠ GitHub.com 기본 | **채택** | 만장일치(C6). GitHub.com = ruleset + CI provenance check 중심 |
| **3** | runtime = sensor, 최종 reject = Hermes 밖 | **채택 (BLOCKING)** | 만장일치(C5). self-reference 역설 해소의 핵심. Hermes ≠ root of trust *강화* 방향 |
| **4** | FP 통제 = T3 path 한정 + observe mode + quarantine | **조건부 채택** | C8 채택 합의 + **조건(B, P3): observe mode ≠ enforcement 발효 (observe 기간 FN 통과 명시), FN 우선순위 > FP ("의심스러우면 quarantine"), 사람 commit 기준 = 사람 서명 + 사람 token + ruleset 통과** |
| **5** | `.git/` 변조 gap + negative-control-only | **채택** | 만장일치(C7+C9). `.git/` = filesystem ACL(§2.5 #1) 책무 명시 + Group I = negative control only (PMO positive evidence 오용 금지) |

**5/5 채택** (3건 BLOCKING/채택, 1건 조건부, 1건 채택). 기각 0건. 단 전부 **입력 한정 → 합의 권고**이며, 실 수단 *결정*·G3 본문 반영·threshold 고정은 별도 단계 (§0.4 + brief 금지사항).

### 2.3 framing 권고 판정

**합의: N1 (명칭 유지 + 중심 명제 명시) — 전면 재정의(N2) / 신규 명칭(N3) 보류.** (C12 만장일치)

**Reviewer 종합**: B의 ADR-011 means/ends 논거가 결정적이다. 외부가 제안한 명칭 "Human-authorized T3 change enforcement with Hermes credential isolation"은 *수단(credential isolation)*을 명칭에 박는다 — ADR-011 §2.1 수단/목적 분리 원칙 위반 소지. **목적(ends) = "Hermes가 T3 변경의 권위 주체가 될 수 없음"이며, credential isolation은 그 수단의 하나일 뿐.** 따라서 명칭은 유지하되, **중심 명제 = "credential boundary + external enforcement + audit의 결합 (metadata 판별기 아님)"을 합의 본문에 명시 권고.** brief 금지사항(G3 §2.2 #20 본문 변경 0건)과도 양립.

### 2.4 BLOCKING 안전 조건 최종 목록

**BLOCKING (안전 필수 — 미충족 시 진입/구현 불가):**

| # | BLOCKING 조건 | 출처 종합 |
|---|--------------|----------|
| **B-1** | **식별 = metadata negative detection 아닌 positive allow-list** (사람 전용 hardware-backed key 서명 + 신뢰 등급 분리). author/committer/trailer = 참고 신호 한정 | A필수1 + B BLOCKING + C(A4) — G3 line 448/784 결함 교정 |
| **B-2** | **runtime = sensor/audit producer 한정, 최종 reject = Hermes 밖** (ruleset / container ACL / hardware key 中 1+) | A필수2 + B#1강화 + C frame |
| **B-3** | **credential/process boundary 실분리가 전제** (사람 signing key·token·SSH/GPG agent를 Hermes 환경에서 격리. 동일 credential 공유 시 FN 위험으로 Q6 불성립) | A필수3 + B BLOCKING + C(A6/A7) + C10 |
| **B-4** | **host 밖 layer 최소 1개를 실 anchor로 의무화** (ruleset + tamper-evident audit) — single-host 3-layer 명목화 방지 | B G4 단독 → Reviewer 채택 (#4 단일 source-of-truth 실질) |
| **B-5** | **R-I-CONFIG-CHANGE = T3 분류** — Hermes는 ruleset/CI workflow/audit log 수정 token 미보유. 자기 차단책을 끄지 못함 (audit 보존 정책 + 외부 read-only sink 포함) | C11 만장일치 + P2 audit |
| **B-6** | **`.git/` 직접 변조 = filesystem ACL(§2.5 #1) 책무** (commit layer 사각 — Group I이 책임지지 않음, 맨 아래 layer) | C7 만장일치 |

**조건부 (채택하되 조건 충족 시):**

| # | 조건부 | 조건 |
|---|--------|------|
| **CB-1** | FP 통제 (observe mode / quarantine / T3 path 한정) | observe ≠ enforcement 발효 명시 (observe 기간 FN 통과) + FN 우선 > FP + 사람 commit 기준 명시 (B, P3) |
| **CB-2** | negative-control-only 조항 | PASS를 positive evidence로 오용 금지 — Operational Readiness / PMO 경계와 정합 (C9) |
| **CB-3** | framing N1 | 명칭 유지 + 중심 명제 명시, 수단(credential isolation) 명칭 고정 보류 (§2.3) |

### 2.5 신규 발굴 영역 포함/제외

| # | 신규 영역 | 판정 | 사유 |
|---|----------|------|------|
| **G1** | **Hermes PR/approval auto-reject** | **포함 — 후속 영역 flag** | C의 정확한 지적: Group α C-2 직표적은 *approval*이며 commit이 아님. 단 본 Group I 범위(commit 차원)를 *확장*하면 brief §1.2 변조 차단 매트릭스 (3) git commit 단위 정의와 충돌 → **별도 후속 단위(Group α 결합 또는 신규)로 flag**, 본 합의 범위 외. 사용자 결정 영역 |
| **G2** | **credential isolation sub단위 I-9** | **부분 포함 — BLOCKING B-3에 흡수** | credential isolation은 별도 sub단위라기보다 B-3 BLOCKING 전제로 흡수. 실 구현 시 sub단위화 여부는 Backlog #6 결정 영역 |
| **G3** | **차단 객체 기준 책무 재정렬** | **포함 — 합의 권고** | merge/push=Group α, `.git/`=§2.5, commit 주체화=Group I credential isolation, provenance 판정=Group I sensor *단일 source* — #4 단일 source-of-truth 보존 + 3중 판정 회피에 정합 |
| **G4** | **single-host 3-layer 명목화 → host 밖 anchor 의무** | **포함 — BLOCKING B-4로 격상** | (§2.4 B-4) |
| **audit** | **audit log tamper-resistance / 외부 read-only sink** | **포함 — B-5 보강** | A·C 명시(P2). 외부 응답 결함 #6 + Q7 직접 근거. ADR-012 Layer 1/2/5 연계 |
| **G6** | commit trailer 표준화 (audit 보조) | **포함 — 보조 한정** | 식별 root signal 아님(B-1), audit 보조 신호 한정 |

### 2.6 G3 line 448/784 metadata 결함 처리 (brief 금지사항과 양립)

**핵심 양립 논리:**

1. **사실 확인 (Reviewer 검증)**: G3 line 448 = "Hermes-originated commit detection = git commit author/committer + Hermes audit log cross-reference", line 784 = "auto-reject (§2.2 #20)의 *기준* 자체가 단일 author 비교". **현 G3 본문이 정확히 metadata-기반 negative detection을 명시** — 외부·세 Agent가 약하다고 판정한 방식.
2. **결함 ≠ 본문 변경**: brief §0.3 + 부록 B는 "G3 §2.2 #20·§2.5·§4 본문 변경 0건"을 명시 금지. 본 합의는 **결함을 "Group I 합의 권고로 식별·기록"하되, G3 본문 교정은 별도 단계(사용자 명시 + 별도 풀 3+1 또는 G3 개정 단위)로 분리**하여 양립한다.
3. **처리 방식 (권고)**:
   - 본 합의 보고서는 "G3 line 448/784가 metadata-기반 detection을 명시하고 있으며, 이는 B-1 (positive allow-list)이 교정 대상으로 삼는 현 설계 결함"임을 **기록**한다 (추론적 검증 산출물 — 본문 변경 아님).
   - G3 본문 교정 = **R-I-CONFIG-CHANGE 또는 별도 G3 개정 단위로 trigger** (Group I enforcement 설정 자체가 T3이므로 G3 §2.2 #20 detection 메커니즘 변경도 T3 분류 → Hermes 단독 변경 불가, 사용자 명시 + 풀 3+1).
   - 이는 brief §7.3 framing 처리(flag 한정)와 동일 구조: **결함 식별·flag = 합의 권고 영역 / 본문 반영 = 사용자 명시 별도 단계.**

> **양립 결론**: 본 합의는 G3 본문을 변경하지 *않으며*, "현 G3 detection 본문이 외부·Agent가 지적한 metadata 결함을 그대로 담고 있다"는 사실을 권고로 기록한다. 본문 교정은 별도 단계 — brief 금지사항과 충돌 0건.

---

## 3. 결정 vs 설계 vs 구현 경계

| 계층 | 본 합의 산출 | 발효 권한 |
|------|-------------|----------|
| **합의 권고 (본 보고서)** | T3 풀 3+1 의무 판정 / 5 보강점 채택 / N1 framing / 6 BLOCKING + 3 조건부 / 신규 영역 flag / G3 결함 기록 | Reviewer 종합 (추론적 검증) — **발효 아님** |
| **설계 결정 (DESIGN)** | 식별 방법(positive allow-list) / 차단 지점(ruleset+CI+ACL) / 보호 범위 / framing 명칭 *결정* | **사용자 명시 + 별도 단계** — 본 합의 권고 기반 |
| **구현 (IMPLEMENTATION)** | 실 hook / ruleset / CI provenance / filesystem ACL / credential isolation 본문 | **Backlog #6 Runtime + CI-hook + 별도 풀 3+1 (R-I-IMPL-BOUNDARY)** |

- 현 상태: **G3 DESIGN PASS / IMPLEMENTATION PENDING** (§1~§7 (b) 격리 PoC + (d) 자동 회귀 미충족).
- A 정확 지적: 현 시점 hook 구현은 **연결 대상(Backlog #6 Runtime) 부재로 무의미** — 실 강제는 Backlog #6 의존.
- 본 합의 = brief §8.1 답습: 실 hook 구현 / branch protection 활성화 / PMO 격상 = 각각 별도 trigger + 사용자 명시.

---

## 4. 미해소 쟁점 / 후속 (사용자 결정 영역 — 자동 진입 0건)

1. **G3 line 448/784 본문 교정 시점** — 본 합의는 결함을 기록만 함. 실 교정 = 별도 G3 개정 단위 (T3, 풀 3+1 + 사용자 명시).
2. **Hermes PR/approval auto-reject (G1)** — Group α C-2 직표적이 approval임을 반영한 표적 확장 또는 신규 단위 진입 여부. Group α 결합 vs 신규 단위 = 사용자 결정.
3. **2차 vendor 외부 입력 (Gemini 등)** — trigger #7은 1건으로 충족됐으나 Group I 표면적상 추가 입력 바람직 (의무 아님). 사용자 결정.
4. **credential isolation sub단위화 (I-9)** — B-3로 흡수했으나 Backlog #6에서 독립 sub단위로 분리할지 = 구현 단계 결정.
5. **observe mode 기간 / threshold** — 1~2주 등 구체 수치 = threshold 고정 영역 (brief 금지 — 별도 단계).
6. **framing 명칭 최종 결정** — N1 권고이나 명칭 확정 = 사용자 명시.
7. **§4.7.2 격상 전 면제 인용 1건 (B, G5)** — 문서 정합성 미세 권고, 후속 정비.

---

## 5. 합의 한 문단 요약

**Group I (Hermes-originated commit auto-reject)는 T3 보안 enforcement 영역으로 풀 3+1 (Agent A/B/C + Reviewer) 의무이며 Reviewer-only 단축은 부적격이다** (만장일치 — trigger #2 T3 BLOCKING + #5 핵심 제약 #1/#4 직결 + #7 외부 1건 충족 + §4 self-reference 구조). 세 Agent와 Reviewer의 G3 원문 검증(line 448 "author/committer + audit log cross-reference", line 784 "기준 자체가 단일 author 비교")이 일치시키는 핵심은 **현 G3 본문이 외부가 약하다고 지적한 metadata-기반 negative detection을 그대로 담고 있으며, positive allow-list 권고는 신규 제안이 아니라 이 설계 결함의 교정**이라는 점이다. 외부 5 보강점은 **전부 채택**(positive allow-list·runtime=sensor·`.git`=ACL 책무 = BLOCKING / GHES≠GitHub.com = 채택 / FP통제 = 조건부). BLOCKING 안전 조건은 **6건**(B-1 positive allow-list+신뢰등급 분리 / B-2 runtime=sensor·reject=Hermes 밖 / B-3 credential boundary 실분리 전제 / B-4 host 밖 anchor 최소 1개 의무 / B-5 R-I-CONFIG-CHANGE T3 / B-6 `.git/`=filesystem ACL 책무) + 조건부 3건(observe≠발효·FN우선 / negative-control-only / framing N1). framing은 **N1 (명칭 유지 + 중심 명제 명시)** 권고 — 외부 제안 명칭이 수단(credential isolation)을 명칭에 고정해 ADR-011 means/ends 원칙에 저촉되므로 전면 재정의 보류. C 발굴 신규 영역 중 **PR/approval auto-reject·책무 재정렬·audit tamper-resistance는 포함**(전자는 후속 단위 flag), credential isolation은 B-3으로 흡수. G3 line 448/784 결함은 **합의 권고로 기록하되 본문 교정은 별도 단계로 분리**하여 brief 금지사항(G3 본문 변경 0건)과 양립한다. 본 합의는 추론적 검증(권고) 한정 — 식별 방법·차단 지점·framing·G3 본문 교정의 실 *결정/구현*은 사용자 명시 + 별도 단계(Backlog #6 Runtime + CI-hook 연결)이며, **본 보고서는 코드/문서 본문 변경·commit·push 0건**이다.

---

## 부록 A — Phase 2 독립 분석 요약 (3 Agent)

| Agent | 관점 | 핵심 결론 |
|----|----|----|
| **Agent A** (구현 분석가) | "실제로 동작하는가?" | metadata 신호 전부 spoof 가능 → positive allow-list(GitHub ruleset 기본 기능, 즉시 구현 가능) + 사람 키 실분리 전제. runtime reject 단독 = 자기참조, pre-receive=GHES 한정. audit log tamper-resistance 미설계 지적. **G3 line 448/784가 현 metadata detection 명시** 발견. 필수 조건 6 + 실 구현 Backlog #6 분리 |
| **Agent B** (품질/안전성 검증가) | "안전하고 견고한가?" | FN(silent T3 위반) > FP(가시·복구가능) 비대칭 → "의심스러우면 quarantine". runtime self-reject = self-reference 역설(§4.1). single-host 3-layer 명목화 → host 밖 anchor 의무. ADR-011 means/ends로 framing 명칭 보류. 문서 정합성 검증 (과대선언·약화 없음). BLOCKING 4 + 조건부 3 |
| **Agent C** (대안 탐색가) | "더 나은 방법이 있는가?" | 식별 frame 자체가 잘못 → perm-by-construction(식별 불요화). A4 allow-list ⊕ A6 patch-only ⊕ A7 hardware key. 책무 객체 기준 재정렬(provenance 판정 = sensor 단일 source). 신규 발굴: PR/approval auto-reject, credential isolation I-9, observe=항구 sensor, audit tamper-resistance. framing N1/N2/N3 옵션 제시, N1 권고 |

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
Hermes runtime 실 구현 / Hermes-originated commit 실 차단 hook 구현 (git pre-commit / pre-receive / filesystem ACL / `read_only` mount / `cap_drop` / CI provenance step 본문) / GitHub ruleset·branch protection 실 변경 / Hermes upstream 변경 (Dockerfile / `hermes-version.yaml` / upstream PR) / 수단 결정 *고정* (식별 방법·차단 지점·보호 범위 최종 결정) / threshold 고정 (observe mode 기간 등) / CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경 / Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) / MVP-1 exit 발효 / Phase α defer-lockdown 변경 / **G3 §2.2 #20·§2.5·§2.6·§4·§5.5 본문 변경 (특히 line 448/784 detection 메커니즘 교정)** / ADR 본문 자동 갱신 (ADR-008/011/012) / Group α·β·γ-1·γ-2 합의 본문 변경 / GP entry 합의 본문 변경 / Backlog #4·Backlog #6 자동 진입 / Hermes PR·approval auto-reject 신규 단위 자동 진입 / 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정) / 외부 LLM 추가 자동 호출 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
