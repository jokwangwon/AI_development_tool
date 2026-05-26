# Backlog #3 Group β (T-5 β + Tier-2/3 catalog 일반) 단독 풀 3+1 합의 보고서

> **본 합의 = Backlog #3 (T3 영역) 中 Group β (T-5 (β) provider URL/model Tier-2/3 vendor 확장 [GP-5 subset] + Tier-2/3 catalog 자동 확장 일반 정책 [GP-3+GP-5 superset]) *수단 결정 적격성 권위 권고* 발행 한정** — Agent A (구현 분석가) + Agent B (품질/안전성 검증가) + Agent C (대안 탐색가) Phase 2 (Independent Analysis, 병렬 독립 분석) + Reviewer (검토 에이전트) Phase 3-4 (교차 비교 + 합의 도출) 통합. **3/3 만장일치 = APPROVE WITH CONDITIONS**.
>
> 본 합의의 어떤 §도 그 자체로 (i) **실 Tier-2/3 catalog 본문 확장** (URL Tier-1 10 / Model Tier-1 19 / R-4.1 Tier-1 42 보존), (ii) **threshold *고정*** (FP/FN rate / Tier 분류 기준 / vendor 수 수치 결정), (iii) **수단 *최종 결정*** (옵션 *적격성 권고* 한정 — 실 채택 = Implementation Evidence PASS + 별도 합의 + 사용자 명시), (iv) **도구 본문 (`tools/*.py`) / `.importlinter` / catalog manifest 신설·변경**, (v) **LiteLLM 등 외부 의존성 (`requirements*.txt`) 추가**, (vi) **CI workflow 변경 / actual run / workflow_dispatch / paths 필터 변경**, (vii) **Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언**, (viii) **MVP-1 exit 발효 / MVP-2 자동 진입**, (ix) **GP-3 진입 condition C-3 / GP-5 진입 condition C-2 *해소 선언*** (해소 = condition row 갱신 합의 + 사용자 명시 별도 단계), (x) Group γ-1 / γ-2 자동 진입, (xi) Backlog #1 / #2 / #4 / #6 / #7 자동 진입, (xii) follow-up brief (`backlog3-t3-zone-followup-brief.md`) / Group α 합의 / prep brief 계보 (`ad9a02d` / `2a9d02d` / `db0e3ac`) 본문 변경, (xiii) 외부 LLM 응답 (Gemini + GPT) *결론 강제 채택* (응답 = 입력 한정 + 본 합의 평가 대상), (xiv) 외부 LLM *추가 자동 호출* / cross-vendor blind 의뢰 자동 재발송, (xv) 실 API key / provider SDK / 외부 API 호출, (xvi) ADR 본문 자동 갱신 (ADR-008 ~ ADR-012), (xvii) **Phase α defer-lockdown 변경**, (xviii) 5 영구 핵심 제약 / Provider Liquidity 5-way 약화 를 발생시키지 않는다.

**작성일**: 2026-05-20 (Group β 풀 3+1 합의 진입 — follow-up brief 옵션 (A) 답습)
**상태**: APPROVED WITH CONDITIONS — Phase 5 (Report) 완료 + 사용자 명시 승인 *전*, commit 0건
**합의 판정**: **APPROVE WITH CONDITIONS** (Agent A + Agent B + Agent C **3/3 만장일치**)
**합의 영역**: Group β (T-5 β + Tier-2/3 catalog 일반) **수단 결정 적격성 권위 권고 한정** — 실 catalog 확장 / threshold 고정 / 수단 최종 결정 0건
**상위 권위**:
- 진입 brief (본 합의 직접 source) = `docs/phase0/backlog3-t3-zone-followup-brief.md` (DRAFT, §3.1 / §4 / §5 / §6 + 옵션 (A))
- Group α 합의 = `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (657줄, 3/3 만장일치 APPROVE WITH CONDITIONS — §8 옵션 (F) Group β 진입)
- 외부 LLM 응답 = `docs/external-review/2026-05-13-backlog3-t3-zone-review-response-gemini.md` (§7.2 Q7~Q12) + `...-gpt.md` (Q7~Q12) — 양 vendor 종합 (C) PARTIAL 수렴
- GP-3 진입 C-3 / GP-5 진입 C-2 = `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` / `...-gp5-mvp1-entry.md` ("T3 영역 별도 풀 3+1")
- prep brief 계보 = v1 `ad9a02d` / v2 `2a9d02d` / Group α brief `db0e3ac`
- ADR-011 §2.1 (a)~(e) + §2.3 권위 위계 + §2.4 T3 영역 / ADR-008 부록 B + 부록 C / ADR-012 §원칙 9 (Hermes ≠ root of trust) / governance-preconditions §1.2.7 P11 (Supply-chain Compromise)
- 5 영구 핵심 제약 + Provider Liquidity 5-way

---

## 0. 본 합의의 범위

### 0.1 사용자 진입 명령 답습 (2026-05-20)

> "옵션 (A)로 진행 — Group β 풀 3+1 합의 진입"

선행 사용자 명령 답습: "옵션 (A)로 진행 — Group β 풀 3+1 합의 진입" (follow-up brief §8 옵션 (A) = Group β 풀 3+1 합의 진입, Agent A/B/C + Reviewer, 외부 LLM 응답 입력 답습). T3 영역 = 보안 enforcement → CLAUDE.md §3 풀 3+1 의무 영역 (Reviewer-only 단축 부적격, brief §5 답습).

### 0.2 본 합의가 *하는* 것

1. Phase 1 (Distribution) — follow-up brief + 3 Agent 관점 분배 답습 (§1)
2. Phase 2 (Independent Analysis) — Agent A / B / C 병렬 독립 분석 결과 요약 (§2)
3. Phase 3 (Cross-Comparison) — 일치 / 부분 일치 / 불일치 / 누락 분류 (§3)
4. Phase 4 (Consensus Resolution) — 최종 판단 + 12 합의 조건 (§4)
5. Phase 5 (Report) — 11 결정 영역 *최종 합의 권고* (§5)
6. GP-3 C-3 / GP-5 C-2 해소 정합 + cross-reference (§6)
7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수) (§7)
8. 다음 단계 (사용자 결정 영역, 자동 진입 0건) (§8)
9. 메타 검증 (§9) / 합의 요약 한 단락 (§10) / 부록 A·B

### 0.3 본 합의가 *하지 않는* 것 (사용자 명시 영구 답습)

| # | 금지 | 본 합의 위반 |
|---|------|------------|
| 1 | **실 Tier-2/3 catalog 본문 확장** (URL 10 / Model 19 / R-4.1 42 보존) | 0건 (수단 적격성 권고 한정) |
| 2 | **threshold *고정*** (FP/FN rate / Tier 분류 기준 / vendor 수) | 0건 (실측 baseline 부재 — §2.1 Agent A 실측 답습) |
| 3 | **수단 *최종 결정*** | 0건 (옵션 *적격성* 권고 — 실 채택 = Evidence PASS + 별도 합의 + 사용자 명시) |
| 4 | **도구 본문 (`tools/*.py`) / `.importlinter` / catalog manifest 신설·변경** | 0건 |
| 5 | **외부 의존성 (LiteLLM / `requirements*.txt`) 추가** | 0건 (stdlib 단독 보존) |
| 6 | **CI workflow 변경 / actual run / workflow_dispatch / paths 필터 변경** | 0건 |
| 7 | **Operational Readiness PASS (Layer E) / Hermes PMO 격상 (Layer F) 선언** | 0건 |
| 8 | **MVP-1 exit 발효 / MVP-2 자동 진입** | 0건 |
| 9 | **GP-3 C-3 / GP-5 C-2 *해소 선언*** | 0건 (해소 = condition row 갱신 합의 + 사용자 명시 별도 단계) |
| 10 | **Phase α defer-lockdown 변경** | 0건 (별개 트랙 — 충돌 0건) |
| 11 | Group γ-1 / γ-2 / Backlog #1/#2/#4/#6/#7 자동 진입 | 0건 |
| 12 | follow-up brief / Group α 합의 / prep brief 계보 본문 변경 | 0건 |
| 13 | 외부 LLM 응답 *결론 강제 채택* / 추가 자동 호출 | 0건 (입력 한정 — 본 합의 평가 대상) |
| 14 | ADR 본문 자동 갱신 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화 | 0건 |

### 0.4 본 합의의 권위 한계

- 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** (Group α 합의 패턴 답습 — "옵션 채택 권위 권고" 형식).
- 본 합의 발효 ≠ 실 catalog 확장 / threshold 고정 / hard-block 도입. hard-block 승격 = **Implementation Evidence PASS 절대 선행** (실 src/ measurement baseline — §2.1 Agent A 실측 확증) + 별도 풀 3+1 + 사용자 명시.
- 외부 LLM 응답 (Gemini + GPT) = *입력* 한정 (본 합의 시 평가 대상) — 결론 강제 채택 0건.
- Group β 외 영역 (Group γ-1 / γ-2) = 별도 합의 영역.

---

## 1. Phase 1 (Distribution) — follow-up brief + 3 Agent 관점 분배

### 1.1 본 합의 진입 source

| 영역 | 답습 |
|------|------|
| 진입 brief | `backlog3-t3-zone-followup-brief.md` (§3.1 Group β 정비 + §4 외부 LLM synthesis + §5 풀 3+1 의무 + §6.1 1순위 β) |
| 합의 단위 | **Group β 단독** (T-5 β subset + Tier-2/3 일반 superset) — Group γ-1 / γ-2 분리 |
| 합의 형태 | **풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시** (T3 영역 의무) |
| 11 결정 영역 | Tier 정의 / 확장 프로세스 / catalog 형식 / 자동 동기화 / FP/FN mitigation / Evidence 의존 / T-5 β vendor 범위 / GP-3↔GP-5 통합·분리 / lock-in 역효과 / 진입 부적합 / FP 비상 탈출구 |

### 1.2 3 Agent 관점 분배 + 외부 LLM 응답 (입력 한정)

| Agent | 관점 | 분석 영역 |
|-------|------|----|
| **Agent A** | 구현 분석가 ("실제로 동작하는가?") | 현 PoC 기반 기술 구현 가능성 + 실측 benchmark + manifest self-match + regex 충돌 + 성능 + Evidence baseline 측정 가능성 |
| **Agent B** | 품질/안전성 검증가 ("안전하고 견고한가?") | 5 영구 핵심 제약 영향 + 위험 10 영역 + 엣지케이스 (FP 비상 탈출구) + ADR-011 §2.1 정합 + GP-3 C-3 / GP-5 C-2 정합 |
| **Agent C** | 대안 탐색가 ("더 나은 방법이 있는가?") | 11 영역 대안 비교 + 그룹화 frame-first + lock-in 완화 3-계층 + 신규 5 영역 (NC-1~5) + 후속 검토 4 (FU-1~4) |
| Reviewer | 검토 에이전트 | 3 출력 교차 비교 + 일치/부분/불일치/누락 + 최종 판단 |

| Vendor | 종합 판정 (입력) |
|------|----|
| Gemini 3 Flash | (C) PARTIAL — α+β 진입 (β = Implementation Evidence PASS 조건부) + Tier-2 즉시 확장 (Mistral/AI21/HF) + Tier-3 보류 + Sandboxed Tier 완화 |
| GPT-5.5 Thinking | (C) PARTIAL — β = 정책/schema/audit-only 진입 / Tier-2/3 hard-block = Evidence PASS 후 + auto-sync BLOCK + frame 통합/namespace 분리 |
| **양 vendor 수렴** | (C) PARTIAL + 정책 진입 가능 + hard-block = Evidence 후 + auto-sync BLOCK + lock-in 역효과 HIGH + 비상 탈출구 의무 + Tier-3 보류 |
| **차이 영역 (1건)** | Q8 Tier-2 vendor 범위 — Gemini 즉시 hard-block 확장 vs GPT audit-only 우선 |

---

## 2. Phase 2 (Independent Analysis) 결과 요약

### 2.1 Agent A (구현 분석가) — APPROVE WITH CONDITIONS

| 영역 | Agent A 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 정책/schema/audit-first frame = 현 PoC (`provider_url_scanner.py` / `secret_scanner.py`) 기반 소규모 코드 변경으로 구현 가능 / **hard-block 승격 = Implementation Evidence PASS 의존** (절대 차단 요인) |
| **실측 benchmark (read-only)** | `src/` url/model/secret scan = **violations 0건 (PASS)** — 단 "안전 검증 0건"이 아니라 **"measurement 표본 부재 0건"** (src/ = facade stub 1개 / 29 non-blank line). 전체 repo = URL 10건 / secret 801건 (catalog 리터럴 self-match, 실 secret 0). runtime = URL 1.52s / secret 3.77s @ 1278 files, RSS ~22MB → Tier-2/3 확장 추정 4~10s **< 30초 threshold 안전** |
| 기술 차단 요인 | HIGH = hard-block FP/FN baseline measurement 불가 (분모 부재) + LiteLLM auto-sync = supply chain + 외부 의존성 0건 위반 / MEDIUM = manifest self-match + Tier별 severity 분기 도구 변경 / LOW = runtime 선형 증가 |
| 알려진 기술 한계 | (1) comment-line 회피 = line-by-line `#`/`//` 한정 (docstring/multiline 미커버) / (2) regex prefix 충돌 (`sk_` ElevenLabs vs `sk-`) / (3) extension allowlist 회피 / (4) vendor rename stale / (5) **provider scanner = AST 아닌 line-regex** (AST는 1차 import scanner 책무 — Tier-2/3 URL/model 확장 = regex append) |
| 진입 조건 | C-A1~C-A6 (정책 권고 한정 / Evidence 선행 / manifest self-allowlist / advisory 한정 / GP-3·GP-5 물리 분리 / 비상 탈출구 선행) |

### 2.2 Agent B (품질/안전성 검증가) — APPROVE WITH CONDITIONS

| 영역 | Agent B 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 정책 frame + schema + Tier-2 audit/warn-only = 안전 차원 적격 / **Tier-2/3 hard-block threshold 선언 = Implementation Evidence PASS 미발효 시 ADR-011 §2.1 (a)(b) 위반** (동등 보안결과 비교표 + 격리 PoC measurement baseline 부재) → hard-block 분리 차단 |
| 5 영구 핵심 제약 | ② 수단-목적 분리 HIGH (harm model 차이 — GP-3 유출방지 vs GP-5 lock-in방지) + ④ 단일 source-of-truth HIGH (형식 분리·자동 동기화 시 분산, 단 1파일1source = 분산 아님) + ⑤ Provider Liquidity 5-way HIGH (역효과 + 비상 탈출구 = blocking precondition) / ① Hermes≠root + ③ 메타포 = 영향 없음 |
| 위험 10 영역 | HIGH 5 (R-β1 FP폭증 / R-β2 LiteLLM supply chain / R-β3 lock-in 역효과 / R-β4 Tier-1 보존 정책변경 / R-β8 Evidence 의존) — **전부 완화 가능, 완화 불가 HIGH = 0** |
| 엣지케이스 | E-β1 FP 비상 탈출구 (blocking) / E-β2 vendor rename / E-β3 LiteLLM supply chain (P11 cross-ref) / E-β4 정상코드 FP / E-β5 over-block / **E-β6 AI agent catalog 우회 entry → Hermes-originated catalog diff auto-reject** |
| ADR 정합 | ADR-011 §2.1 = 정책/audit-only 5/5 충족 가능 / hard-block = (a)(b) Evidence 전 미충족 → 분리 차단. **정합성 발견**: §2.1 본문 = (a)~(d) 4조건, "5조건" = +e APPROVE 패턴 |
| 진입 조건 | C-B-1~C-B-6 |

### 2.3 Agent C (대안 탐색가) — APPROVE WITH CONDITIONS

| 영역 | Agent C 분석 |
|------|----|
| 종합 판정 | **APPROVE WITH CONDITIONS** |
| 사유 | 정책/schema/audit-first 진입 적격 / hard-block·threshold·Tier-3·LiteLLM auto-sync = BLOCK / **그룹화 = 통합 진입 (II) + frame-first 결정 순서** ((6) 정책 frame 先 → (2) vendor 범위 後 namespace 내) |
| 대안 우월 4건 | AU-1 PR-제안 자동 + 수동 merge gate / AU-2 manifest 단일 source + 코드 loader 강제 / AU-3 lock-in 완화 3-계층 통합 (allowlist 상시 + Sandboxed 한시 + expiry 만료) / AU-4 audit-only + adapter-likelihood 승격 trigger |
| Agent C 신규 5건 | NC-1 expiry 자동 만료 trigger (`R-MVP1-G5-CATALOG-EXPIRY`) / NC-2 Tier 승격 정량 trigger (audit→hard-block) / NC-3 catalog provenance 거버넌스 + Evidence Ledger 연계 / NC-4 adapter stub generator 책무 위치 / NC-5 catalog fixture FP/FN regression |
| 후속 검토 4건 | FU-1 현 scanner FP 표면 (docstring/multiline) / FU-2 `schema_validator.py` 재사용 / FU-3 advisory provider liquidity / FU-4 expiry fail-open vs close |
| 진입 조건 | C-β1~C-β10 |

### 2.4 3 Agent 일치 영역 (사전 식별)

| 영역 | A | B | C | 일치 |
|------|----|----|----|----|
| 종합 판정 = APPROVE WITH CONDITIONS | ✅ | ✅ | ✅ | **3/3 만장일치** |
| 정책 frame + schema + Tier-2 audit/warn-only 진입 적격 | ✅ | ✅ | ✅ | 3/3 |
| Tier-2/3 hard-block threshold = Implementation Evidence PASS 후 분리 (BLOCKING) | ✅ | ✅ | ✅ | 3/3 |
| LiteLLM auto-sync BLOCK / advisory snapshot 한정 | ✅ | ✅ | ✅ | 3/3 |
| 외부 의존성 0건 (stdlib 단독 보존) | ✅ | ✅ | ✅ | 3/3 |
| GP-3 ↔ GP-5 정책 frame 통합 / namespace+threshold 분리 (harm model 차이) | ✅ | ✅ | ✅ | 3/3 |
| provider lock-in 역효과 실재 HIGH + 완화책 의무 | ✅ | ✅ | ✅ | 3/3 |
| FP 비상 탈출구 / 복구 정책 의무 (양 vendor 결함 #1) | ✅ | ✅ | ✅ | 3/3 |
| Tier-3 도입 보류 | ✅ | ✅ | ✅ | 3/3 |
| T-5 β vendor = audit-only 등록 (Gemini 즉시 확장 < GPT audit-only 우월) | ✅ | ✅ | ✅ | 3/3 |
| catalog manifest 적격 + 단일 source 강제 (1파일1source) | ✅ | ✅ | ✅ | 3/3 |
| Group β = GP-3 C-3 / GP-5 C-2 핵심 잔여 매듭 (단 ≠ 해소 선언) | ✅ | ✅ | ✅ | 3/3 |
| 5 영구 핵심 제약 ②④⑤ HIGH (보존 가능) / ①③ 영향 없음 | ✅ | ✅ | ✅ | 3/3 |
| Provider Liquidity 5-way 보존 | ✅ | ✅ | ✅ | 3/3 |
| 외부 LLM 응답 = 입력 한정 (강제 채택 0건) + 양 vendor (C) PARTIAL 수렴 | ✅ | ✅ | ✅ | 3/3 |
| 수단 적격성 권고 한정 (실 catalog 확장 / threshold 고정 / 도구 변경 0건) | ✅ | ✅ | ✅ | 3/3 |
| 풀 3+1 의무 (Reviewer-only 단축 부적격) | ✅ | ✅ | ✅ | 3/3 |
| Q8 차이 영역 = GPT audit-first 우월 | ✅ | ✅ | ✅ | 3/3 |

---

## 3. Phase 3 (Cross-Comparison) — 일치 / 부분 / 불일치 / 누락

### 3.1 일치 (Consensus, 3개 모두 동의) — 18 영역

§2.4 답습 — **18/18 일치 영역**. 본 합의의 핵심 권위 source.

### 3.2 부분 일치 (Partial, 2개 동의 / 1개 이견) — 3 영역

| # | 영역 | A | B | C | 분석 |
|---|------|----|----|----|----|
| P-1 | 확장 프로세스 | 수동 trigger / 자동 BLOCK | 수동 curated | **PR-제안 자동 발견 + 수동 merge gate** (AU-1) | **부분 — C = 발견 자동/결정 수동 분리 신규 / A+B = 수동** |
| P-2 | lock-in 완화 형태 | GPT allowlist/expiry 우세 (Sandboxed 구현 부담) | allowlist/expiry + Sandboxed (단 Sandboxed T1화 시 ② 약화 정합성 재검토) | **3-계층 통합** (allowlist 상시 + Sandboxed 한시 + expiry 만료, AU-3) | **부분 — C = 통합 / A = allowlist 우선 / B = Sandboxed T1화 ② 약화 경고** |
| P-3 | catalog 형식 단일성 강제 강도 | manifest self-allowlist 필수 (실측 self-match 회피) | 형식 분리 ≠ source 분산 (1파일1source) | manifest 단일 source + 코드 loader 강제 (AU-2) | **부분 — 셋 다 manifest 적격 + 단일성 강제, 강조점만 상이 (실측/개념/구조)** |

#### 3.2.1 P-1 분석 (확장 프로세스)
**Reviewer 평가**: Agent C 의 "발견 자동 (PR-제안) + 결정 수동 (merge gate)" 은 Agent A/B 의 "수동 curated" 와 충돌하지 않는 *상위 호환* — 결정 게이트가 수동인 점에서 단일 source-of-truth (④) 보존. **합의 도출 → 수동 결정 게이트 보존 + PR-제안 자동 발견은 선택적 후속 (Evidence 후, NC-2 trigger 와 결합)**.

#### 3.2.2 P-2 분석 (lock-in 완화)
**Reviewer 평가**: Agent B 의 핵심 경고 = **Sandboxed Tier 를 T1 (자동 학습) 영역으로 두면 catalog 우회를 자동 허용 → ⑤ (5-way) 보존하나 ② (수단-목적: lock-in 방지 목적) 약화 → ADR-011 §2.4 정합성 재검토 필요**. Agent C 의 3-계층 통합은 allowlist (상시, T2) + Sandboxed (한시, expiry 강제) + expiry 자동 만료 (NC-1) → B 의 경고를 expiry/owner/audit 로 흡수. **합의 도출 → 3-계층 통합 *권고* + Sandboxed Tier 의 T1/T2 영역 귀속은 풀 3+1 평가 대상 (B 경고 흡수 — 무제한 자동 허용 금지, expiry+audit 강제)**.

#### 3.2.3 P-3 분석 (manifest 단일성)
**Reviewer 평가**: 3 Agent 모두 manifest 적격 + 단일성 강제에 동의 — Agent A (실측 self-match 회피 = self-allowlist) + Agent B (1파일1source = 분산 아님) + Agent C (manifest=유일 source + 코드=loader). 세 강조점이 *상호 보완* (구현 안전 + 개념 + 구조). **합의 도출 → manifest = 유일 source + 코드 loader + self-allowlist (3 강조점 통합)**.

### 3.3 불일치 (Divergence, 3개 모두 다른 의견) — 0 영역

3 Agent 모두 동일하거나 부분 일치 (3/3 만장일치 + 3 부분 일치). **불일치 0건**. (양 vendor 가 갈린 Q8 Tier-2 범위에서도 3 Agent 는 모두 audit-first/GPT 우월로 수렴.)

### 3.4 누락 (Gap, 특정 에이전트만 언급) — 8 영역

| # | 영역 | 출처 | 처리 |
|---|------|----|----|
| G-1 | 실측 benchmark (src/ = measurement 표본 부재 / runtime < 30s) | A | 흡수 — §2.1 + Evidence 의존 데이터 확증 (C-5) |
| G-2 | provider scanner = AST 아닌 line-regex (Tier-2/3 = regex append) | A | 흡수 — §5 #2 구현 단순성 근거 |
| G-3 | regex prefix 충돌 (`sk_` vs `sk-`) + manifest self-match | A | 흡수 — C-3 (self-allowlist) + C-10 (fixture regression) |
| G-4 | ADR-011 §2.1 본문 = (a)~(d) 4조건, "5조건" = +e 패턴 (정합성 발견) | B | 흡수 — §6.1 명시 |
| G-5 | P11 (Supply-chain Compromise) cross-reference + Hermes-originated catalog diff auto-reject | B | 흡수 — C-9 + §6.2 |
| G-6 | Agent C 신규 5건 (NC-1 expiry 만료 trigger / NC-2 승격 정량 trigger / NC-3 provenance 거버넌스 / NC-4 adapter stub 책무 / NC-5 fixture regression) | C | 흡수 — §7 Rollback Trigger + C-8 / C-9 / C-10 |
| G-7 | frame-first 결정 순서 그룹화 ((6) 先 → (2) 後) + β//γ-1 병렬 진입 가능 | C | 흡수 — §5 + §8 |
| G-8 | 후속 검토 4건 (FU-1 scanner FP 표면 / FU-2 schema_validator 재사용 / FU-3 advisory liquidity / FU-4 expiry fail-open/close) | C | 흡수 — C-10 + §6.2 |

**누락 흡수 결론**: 8 누락 영역 모두 흡수 — 충돌 0건. Agent 별 분석 다양성 (A 실측 / B 안전 정합 / C 신규 발굴) = 합의 풍부도 증대.

### 3.5 Phase 3 매트릭스 합산

| 분류 | 영역 수 | 처리 |
|----|----|----|
| 일치 (Consensus) | 18 | 그대로 채택 |
| 부분 일치 (Partial) | 3 | 통합 (§3.2.1~§3.2.3) |
| 불일치 (Divergence) | 0 | — |
| 누락 (Gap) | 8 | 흡수 (§3.4) |

**합산**: 29 영역 모두 합의 도달. **3/3 만장일치 = APPROVE WITH CONDITIONS** 권위 강화.

---

## 4. Phase 4 (Consensus Resolution) — 최종 판단

### 4.1 최종 판정 = **APPROVE WITH CONDITIONS** (3/3 만장일치)

| 영역 | 판정 |
|------|------|
| 종합 판정 | **APPROVE WITH CONDITIONS** (Agent A + B + C 3/3) |
| 합의 단위 | Group β 단독 (T-5 β + Tier-2/3 일반) — Group γ-1 / γ-2 분리 |
| 합의 형태 | 풀 3+1 + 외부 LLM 응답 답습 (입력 한정) + 사용자 명시 |
| 진입 적격 범위 | 정책 frame + catalog schema + Tier 정의 + Tier-2 audit/warn-only + vendor 후보 *적격성 권고* |
| **분리 차단 범위** | **Tier-2/3 hard-block threshold 선언 + FP/FN rate 고정 = Implementation Evidence PASS 후 별도 합의** (ADR-011 §2.1 (a)(b) 위반 회피 — 3/3 BLOCKING) |
| 외부 LLM 결론 강제 채택 | ❌ 0건 (입력 한정 — 평가 결과 = 양 vendor 차이 1/1 (Q8) GPT audit-first 우월 일관) |

### 4.2 본 합의 조건 (Conditions, 통합 12건) — C-Gβ-1 ~ C-Gβ-12

| # | 조건 | 출처 |
|---|------|----|
| **C-Gβ-1** | **진입 = 정책 frame + catalog schema + Tier 정의 + Tier-2 audit/warn-only 한정. hard-block threshold + FP/FN rate *고정* = Implementation Evidence PASS 후 별도 합의** (ADR-011 §2.1 (a)(b) 위반 회피) | A C-A2 + B C-B-1 + C C-β1 (3/3 BLOCKING) |
| **C-Gβ-2** | **FP 비상 탈출구 / 복구 정책 동시 설계 의무** — allowlist 경로 (`src/providers/**` / 공식 adapter) + time-boxed exception (owner+rationale+expiry) + adapter stub + audit downgrade. 비상 탈출구 없는 hard-block 부적합 | A C-A6 + B C-B-2 + C C-β7 (3/3, 양 vendor 결함 #1) |
| **C-Gβ-3** | **catalog manifest = 유일 source + 코드 loader + self-allowlist** (형식 분리 ≠ source 분산, ④ 보존) + 필수 필드 (provenance / rationale / fixture / allowlist / expiry / changelog) | A C-A3 + B C-B-3 + C C-β2 (3/3, P-3 통합) |
| **C-Gβ-4** | **LiteLLM auto-sync BLOCK / advisory snapshot 한정** (snapshot fixture 고정 + checksum/provenance 검증 후 수동 흡수). 외부 의존성 (`requirements*.txt`) 추가 0건 (stdlib 단독 보존) | A C-A4 + B R-β2 + C C-β3 (3/3) |
| **C-Gβ-5** | **GP-3 R-4.1 ↔ GP-5 URL/Model = 정책 frame 통합 / catalog namespace + threshold *분리*** (harm model 차이: 유출방지 vs lock-in방지). 물리적 통합 시 회귀 위험 (`iter_files`/allowlist 정책 상이) | A C-A5 + B C-B-4 + C C-β5 (3/3) |
| **C-Gβ-6** | **provider lock-in 역효과 완화 = allowlist (상시) + Sandboxed Tier (한시) + expiry (자동 만료) 계층 결합.** Sandboxed Tier 의 T1/T2 영역 귀속 = 풀 3+1 평가 대상 (무제한 자동 허용 금지, expiry+owner+audit 강제 — B 경고 흡수) | A(lock-in) + B R-β3/⑤ + C C-β4/AU-3 (3/3, P-2 통합) |
| **C-Gβ-7** | **T-5 β vendor = audit-only 등록 + adapter-likelihood 승격 trigger.** 실 catalog 확장 + vendor 수 *고정* 0건. Tier-3 도입 보류. 후보 기준 = adapter 지원 가능성 + direct-use 우회 위험 + low-FP prefix + allowlist 경로 명확 | B C-B-5 + C C-β6 (양 vendor 차이 → audit-first 통합) |
| **C-Gβ-8** | **hard-block 승격 정량 trigger 구조 명시** (audit→hard-block: warn-cycle N회 + FP_rate < threshold + adapter 미존재 확인 — 구조만, 수치 *고정* 0건) | C NC-2 + A C-A2 + B R-β8 |
| **C-Gβ-9** | **catalog provenance/changelog 거버넌스 + Evidence Ledger 연계 + Hermes-originated catalog diff auto-reject** (P11 Supply-chain cross-reference) | C NC-3 + B E-β6/G-5 |
| **C-Gβ-10** | **현 scanner FP 표면 측정/보강 후속 검토** (docstring/multiline 미회피 line-regex 한계 + regex prefix 충돌 + fixture FP/FN regression) = Evidence baseline 정확도 전제 | A 한계1/2/5 + C FU-1/NC-5/C-β9 |
| **C-Gβ-11** | **외부 LLM 응답 = 입력 한정 보존** (결론 강제 채택 0건) | A + B + C 일치 |
| **C-Gβ-12** | **본 합의 = 수단 결정 적격성 권위 권고 + DRAFT 한정.** 실 catalog 확장 / threshold 고정 / 수단 최종 결정 / 도구 변경 / CI workflow / actual run / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit / GP-3 C-3·GP-5 C-2 *해소 선언* / Phase α defer-lockdown 변경 모두 0건 | A + B + C 일치 + brief §0.2/0.3 |

**합의 조건 합산**: **12 조건 충족 시 = 본 합의 진입 적합** + 본 합의 = "옵션 채택 권위 권고" 한정.

---

## 5. Final Consensus 11 결정 영역 — 최종 합의 권고

| # | 결정 | **최종 합의 옵션** | 사유 (3/3 만장일치 + 부분 흡수) |
|---|------|----|----|
| 1 | Tier 정의 기준 | **enforcement-mode 기준** (Tier-1 = hard-block 보존 / Tier-2 = audit-warn / Tier-3 = observe-doc) + adapter-likelihood = 승격 조건 결합 | confidence = 입력 / tier = 행동 1:1 (Agent C AU 우월) — 정의 합의 적격, 분류 *고정* 별도 |
| 2 | 확장 프로세스 | **수동 결정 게이트 보존** + PR-제안 자동 발견은 선택적 후속 (Evidence 후, NC-2 결합) | P-1 통합 (④ 단일 source-of-truth) |
| 3 | catalog 본문 형식 | **별도 yaml/json manifest = 유일 source + 코드 loader + self-allowlist** (실측 self-match 회피) | P-3 통합 (3 Agent 강조점 통합) — 실 manifest 신설 = 별도 |
| 4 | 자동 동기화 (LiteLLM) | **자체 catalog = 단일 source-of-truth / LiteLLM = advisory snapshot 한정 (fixture 고정)** — auto-sync / auto-merge / auto-hard-block BLOCK | 3/3 일치 + supply chain (R-β2) + ① 변형 root-of-trust 위임 회피 |
| 5 | FP/FN mitigation | **allowlist 경로 + audit-first warn cycle 1회 선행 + Evidence baseline 측정** | 현 scanner multiline/docstring 미회피 = 기존 결함 (C-10) → baseline 측정 전제 |
| 6 | Implementation Evidence PASS 의존 | **정책/schema = MVP-1.5 진입 적격 / hard-block = Evidence PASS (MVP-2 이후) 절대 선행** ⭐ | 실측 (Agent A): src/ measurement 표본 부재 → FP rate 분모 0 = threshold 고정 불가 (3/3 BLOCKING) |
| 7 | T-5 β vendor 범위 | **Tier-2 audit-only 등록 + adapter-likelihood 승격 trigger** (Mistral/AI21/HuggingFace = audit-only 후보 / Stability = image 범위 분리 / Tier-3 보류) ⭐ | 양 vendor 차이 1/1 = GPT audit-first 우월 (Gemini 유동성 의도를 audit-only 등록이 포함) — 3/3 |
| 8 | GP-3 ↔ GP-5 통합 vs 분리 | **정책 frame 통합 (tier 정의·provenance·evidence·fixture·allowlist·expiry) / catalog namespace + threshold 분리** | harm model 차이 (3/3) + 물리 통합 시 회귀 위험 (Agent A) |
| 9 | provider lock-in 역효과 완화 | **allowlist (상시) + Sandboxed Tier (한시, expiry+owner+audit 강제) + expiry 자동 만료 trigger 계층 결합** | P-2 통합 (AU-3) + Sandboxed T1/T2 귀속 = 풀 3+1 평가 (B 경고 흡수) |
| 10 | 진입 부적합 시점 | **정책 = MVP-1.5 적격 / hard-block = MVP-2 Evidence 기반 / 전면 보류 = 부적합** (GP-3 C-3·GP-5 C-2 미해소 지속) | 단계 분리 (Agent C) — 3/3 |
| 11 | FP 복구 / 비상 탈출구 | **time-boxed exception (owner+rationale+expiry) + audit downgrade (hard→warn 한시)** + expiry 자동 만료 trigger (NC-1) | 양 vendor 결함 #1 (3/3 blocking, C-Gβ-2) |

**합산**: 11 결정 영역 모두 합의 도달 — **3/3 만장일치 + P-1/P-2/P-3 부분 통합 + G-1~G-8 누락 흡수**. 모든 권고 = *적격성 권고* 한정 (실 채택 = Evidence PASS + 별도 합의 + 사용자 명시).

---

## 6. GP-3 C-3 / GP-5 C-2 해소 정합 + cross-reference

### 6.1 GP-3 C-3 / GP-5 C-2 해소 정합 (Agent B §5.2 답습)

| condition | 원문 (확인) | Group β 정합 |
|---|---|---|
| **GP-3 C-3** | "T3 영역 별도 풀 3+1 — AR-2 / Vault HSM / **Tier-2/3 catalog 확장**" | ✅ Group β = Tier-2/3 catalog 확장 항목 **직접 대응 = 핵심 잔여 매듭** (AR-2 = Group α 발효 / Vault HSM = Group γ-2) |
| **GP-5 C-2** | "T3 영역 별도 풀 3+1 — AR-2 / facade real 본문 P1 v2 / **Tier-2/3 vendor 확장**" | ✅ Group β = Tier-2/3 vendor 확장 항목 **직접 대응** (facade real 본문 P1 v2 = Backlog #4 별도 영역) |

→ **두 condition *완전* 해소** = Group α (AR-2, 발효) + **Group β (Tier-2/3 catalog/vendor 확장 정책)** 풀 3+1 발효. **단 본 합의 ≠ 해소 선언** (C-Gβ-12) — 해소 = condition row 갱신 합의 + 사용자 명시 별도 단계. 본 합의 = 해소 *vehicle 적격성* 권고 + 정책 frame 진입 적격 권고 한정. ⚠️ 정합성 메모 (Agent B G-4): ADR-011 §2.1 본문 = (a)~(d) 4조건, "5조건" = +e 합의 APPROVE 패턴 — 본 합의는 5조건 패턴 기준 평가.

### 6.2 기타 cross-reference

| 영역 | 답습 |
|------|----|
| **Implementation Evidence PASS** | hard-block 승격 절대 선행 — 실 src/ measurement baseline (Agent A 실측: 현 stub 단독 = 표본 부재) |
| **P11 (Supply-chain Compromise)** (governance-preconditions §1.2.7) | LiteLLM auto-sync BLOCK + advisory checksum/provenance 검증 = P11 enforcement layer 정합 (Agent B E-β3) |
| **Group D §2.1 (D)** (gitleaks default ruleset Tier-2/3 자동 확장 회피) | 자체 curated catalog 우선 = 답습 (R-β9) |
| **MVP-3 G4 §4.6** (의미적 lock-in 라운드트립) | FN cover 잔존 (R-β5) = MVP-3 분리 영역 |
| **Backlog #6** (Runtime + CI-hook) | 실 CI step `pre-commit run` / catalog scan workflow 도입 = Backlog #6 영역 (Group α C-1 답습) |
| **Group E `schema_validator.py`** (PoC 시제) | catalog manifest schema 검증 재사용 후속 검토 (Agent C FU-2) — 신규 도구 신설 회피 |
| **Group C Evidence Ledger** (`jsonl_hash_chain.py`) | catalog changelog ↔ Evidence Ledger 연계 (Agent C NC-3 / C-Gβ-9) |
| **Group γ-1 / γ-2** | 책무 영역 다름 (catalog source vs Hermes upstream / secret source) — 별도 합의 영역 (β//γ-1 병렬 진입 가능, Agent C §6.2) |

---

## 7. Rollback Trigger 통합 매트릭스 (Agent C 신규 trigger 흡수)

### 7.1 Group β 진입 Rollback Trigger (답습)

| Trigger | 발화 조건 | 발화 시 행동 |
|--------|---------|----------|
| **ADR-011 §2.4** | T3 영역 (Tier-2/3 catalog 정책) 진입 결정 | 풀 3+1 + 외부 LLM 1+ (회수 完, 입력 답습) + 사용자 명시 |
| **GP-3 §3.5 (Tier-2 확장 필요)** | Tier-2/3 catalog 확장 결정 | 풀 3+1 합의 |
| **GP-5 §4.6 (URL Tier-2/3)** | Tier-2/3 vendor 확장 결정 | 풀 3+1 합의 |

### 7.2 신규 Rollback Trigger (Agent C NC-1/NC-2 흡수 — 구조 한정, 수치 고정 0건)

| Trigger | 단계 | 발화 조건 | 후속 합의 |
|--------|----|----|----|
| **R-MVP1-G5-CATALOG-EXPIRY** (NC-1) | exception / Sandboxed Tier 만료 | expiry date 도달 | 자동 재검토 발화 (fail-open vs fail-close 정책 = FU-4 후속) |
| **R-MVP1-G5-TIER-PROMOTE** (NC-2) | audit-only → hard-block 승격 | warn-cycle N회 + FP_rate < threshold + adapter 미존재 (구조 — 수치 별도 합의) | 별도 풀 3+1 (Implementation Evidence PASS 의존) |
| **R-MVP1-G5-CATALOG-DIFF** (NC-3/E-β6) | Hermes-originated catalog diff 시도 | catalog 본문 변경 commit 식별 | auto-reject + 풀 3+1 + 사용자 명시 |

### 7.3 후속 단계 Rollback Trigger (본 합의 영역 외)

| 영역 | 후속 Rollback Trigger | 분리 사유 |
|------|----|----|
| 실 Tier-2/3 catalog 본문 확장 | Implementation Evidence PASS + 별도 풀 3+1 + 사용자 명시 | Evidence 영역 |
| catalog manifest 신설 / 도구 본문 변경 | Backlog #6 Runtime + CI-hook 연결 | Backlog #6 영역 |
| LiteLLM advisory snapshot 도입 | 별도 합의 (auto-sync BLOCK 결정 변경 시) | T3 영역 |
| Sandboxed Tier T1/T2 영역 귀속 결정 | 별도 풀 3+1 (ADR-011 §2.4 정합성) | T3 영역 |
| GP-3 C-3 / GP-5 C-2 해소 선언 | condition row 갱신 합의 + 사용자 명시 | GP entry 합의 영역 |

---

## 8. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 옵션 | 영역 | 후속 단계 |
|-----|------|--------|
| **(A)** | 본 합의 그대로 승인 → 파일화 + commit + push (`docs/review/3plus1-consensus-2026-05-20-backlog3-groupbeta-catalog-policy.md`) | 본 합의 commit + push (1 commit) |
| (B) | 본 합의 일부 수정 요청 → 수정 후 승인 | v2 작성 |
| (C) | 본 합의 그대로 승인 → 파일화 + commit *까지만* (push 보류) | 1 commit |
| (D) | 본 합의 승인 + push → **Group γ-1 (C-5b ST-1 Hermes upstream chmod) 풀 3+1 합의 진입 brief** (follow-up brief §6.1 2순위) | downstream preflight |
| (E) | 본 합의 승인 + push → **Group γ-2 (Vault HSM ST-4 MVP-6 보류 확정) 풀 3+1 합의 진입 brief** (3순위) | 양 vendor BLOCK/DEFER 답습 |
| (F) | 본 합의 승인 + push → **GP-3 C-3 / GP-5 C-2 condition row 갱신 합의** (해소 선언 — α+β 발효 답습) | GP entry 갱신 |
| (G) | 본 합의 보류 → 세션 종료 | — |

### 8.1 권고 시작 명령 (사용자 명시 결정 영역)

- (A) 후보: "옵션 (A)로 진행 — 본 합의 그대로 승인하고 commit + push."
- (D) 후보: "옵션 (D)로 진행 — 본 합의 답습 + Group γ-1 (C-5b ST-1) 풀 3+1 합의 진입 brief 작성."

---

## 9. 메타 검증

| 검증 영역 | 결과 |
|--------|----|
| Phase 1~5 완수 | ✅ Distribution + Independent Analysis (A/B/C 병렬 독립) + Cross-Comparison + Consensus Resolution + Report |
| 풀 3+1 의무 영역 (T3 보안 enforcement) | ✅ Agent A/B/C + Reviewer 4 역할 가동 (Reviewer-only 단축 부적격 답습) |
| Agent 독립성 (편향 방지) | ✅ A/B/C 상호 비참조 (각 출력에 "다른 Agent 미참조" 명시) |
| 외부 LLM 응답 = 입력 한정 | ✅ 강제 채택 0건 (Q8 차이 = 독립 평가로 GPT audit-first 우월 도출) |
| 3/3 만장일치 | ✅ APPROVE WITH CONDITIONS (불일치 0건) |
| 12 합의 조건 (C-Gβ-1~12) | ✅ 등록 |
| 사용자 명시 금지 14건 (§0.3) | ✅ 모두 0건 (Phase α defer-lockdown 변경 0건 / actual run 0건 / CI workflow 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건 / MVP-1 exit 0건 / 수단 결정 0건 / threshold 고정 0건) |
| 합산 합의 조건 | 695 → 707 (26 합의 — 본 합의 C-Gβ-1~C-Gβ-12 신규 12 등록) — *commit 시 발효* |
| 실 변경 0건 | ✅ catalog / 도구 본문 / `.importlinter` / CI workflow / `requirements*.txt` 변경 0건 (Agent A 실측 = read-only 실행) |

---

## 10. 합의 요약 (한 단락)

Backlog #3 T3 영역 中 Group β (T-5 (β) provider URL/model Tier-2/3 vendor 확장 [GP-5 subset] + Tier-2/3 catalog 자동 확장 일반 정책 [GP-3+GP-5 superset]) 단독 풀 3+1 합의 (Agent A 구현 분석가 + Agent B 품질/안전성 검증가 + Agent C 대안 탐색가 병렬 독립 분석 + Reviewer 교차 비교·합의 도출) 결과 = **APPROVE WITH CONDITIONS (3/3 만장일치)**. 진입 적격 범위 = **정책 frame + catalog schema + Tier 정의 (enforcement-mode 기준) + Tier-2 audit/warn-only + vendor 후보 적격성 권고** (MVP-1.5 진입 적격). 분리 차단 범위 = **Tier-2/3 hard-block threshold 선언 + FP/FN rate 고정 = Implementation Evidence PASS 후 별도 합의** (3/3 BLOCKING — Agent A 실측으로 현 src/ = measurement 표본 부재 = threshold 고정 기술적 불가 확증, ADR-011 §2.1 (a)(b) 위반 회피). 12 합의 조건 (C-Gβ-1~C-Gβ-12) = hard-block 분리 / FP 비상 탈출구 동시 설계 / manifest 단일 source+loader+self-allowlist / LiteLLM auto-sync BLOCK·advisory 한정 / GP-3↔GP-5 frame 통합·namespace+threshold 분리 (harm model 차이) / lock-in 완화 3-계층 (allowlist 상시+Sandboxed 한시+expiry 만료) / T-5 β audit-only 등록+승격 trigger / 승격 정량 trigger 구조 / provenance 거버넌스+Evidence Ledger 연계+Hermes catalog diff auto-reject / 현 scanner FP 표면 후속 검토 / 외부 LLM 입력 한정 / 수단 적격성 권고+DRAFT 한정. Group β = GP-3 진입 condition C-3 / GP-5 진입 condition C-2 ("T3 영역 별도 풀 3+1") 의 *Tier-2/3 catalog·vendor 확장 항목 직접 대응 = 핵심 잔여 매듭* (Group α AR-2 발효 + Group β 발효 시 두 condition 완전 해소 vehicle) — 단 본 합의 ≠ 해소 선언 (해소 = condition row 갱신 합의 + 사용자 명시 별도 단계). 5 영구 핵심 제약 ②(수단-목적)·④(단일 source)·⑤(Provider Liquidity 5-way) = HIGH 3건 모두 condition 으로 보존 가능 (①③ 영향 없음). 외부 LLM 양 vendor (Gemini + GPT) (C) PARTIAL 수렴 = 입력 한정 (강제 채택 0건), 차이 1건 (Q8 Tier-2 범위) = 3 Agent 독립 평가로 GPT audit-first 우월 도출. 본 합의 = 수단 결정 적격성 권위 권고 발행 한정 — 실 Tier-2/3 catalog 본문 확장 / threshold 고정 / 수단 최종 결정 / 도구 본문 변경 / `.importlinter`·catalog manifest 신설 / LiteLLM 외부 의존성 추가 / CI workflow 변경 / actual run / Operational Readiness PASS / Hermes PMO 격상 / MVP-1 exit 발효 / GP-3 C-3·GP-5 C-2 해소 선언 / Phase α defer-lockdown 변경 / 외부 LLM 강제 채택 모두 0건이며, 모든 *결정* 은 별도 풀 3+1 합의 (Implementation Evidence PASS + 사용자 명시 후). 합산 합의 조건 695 → 707 (26 합의 — commit 시 발효).

---

## 부록 A — 다음 단계 옵션 (사용자 결정 영역)

§8 답습. 본 합의 = Phase 5 (Report) 완료 + 사용자 명시 승인 *전* 상태 (commit 0건). staged cycle (brief → 승인 → 합의 → commit → push) 답습 — commit / push = 사용자 명시 승인 후 별도 단계.

## 부록 B — 금지 사항 (사용자 명시 영구 답습)

본 합의의 어떤 §도 그 자체로 다음을 발생시키지 않는다:
실 Tier-2/3 catalog 본문 확장 (URL 10 / Model 19 / R-4.1 42 보존) / threshold 고정 (FP/FN rate / Tier 분류 / vendor 수) / 수단 최종 결정 / 도구 본문 (`tools/*.py`) 변경 / `.importlinter` 변경 / catalog manifest 신설 / LiteLLM 등 외부 의존성 (`requirements*.txt`) 추가 / CI workflow 변경 / actual run 재실행 / workflow_dispatch 추가 / paths 필터 변경 / Operational Readiness PASS (Layer E) 선언 / Hermes PMO 격상 (Layer F) 선언 / MVP-1 exit 발효 / MVP-2 자동 진입 / GP-3 C-3·GP-5 C-2 해소 선언 / Group γ-1·γ-2 자동 진입 / Backlog #1/#2/#4/#6/#7 자동 진입 / follow-up brief·Group α 합의·prep brief 계보 본문 변경 / 외부 LLM 응답 결론 강제 채택 / 외부 LLM 추가 자동 호출 / ADR 본문 자동 갱신 (ADR-008~012) / Phase α defer-lockdown 변경 / 5 영구 핵심 제약·Provider Liquidity 5-way 약화.
