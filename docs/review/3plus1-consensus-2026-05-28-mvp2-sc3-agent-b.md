# 3+1 합의 — Agent B (품질/안전성 검증가) — MVP-2 SC-3 GP-2 full PASS 발효 brief

> **작성**: 2026-05-28 (67번째 entry cycle — 세션 #3, SC-3)
> **역할**: Agent B (품질/안전성 검증가) — 관점 "over-claim 없는가, 정직한가?"
> **검토 대상**: `docs/phase0/mvp2-sc3-full-gp2-pass-activation-brief.md` (v1, §0~§11)
> **독립 분석**: Agent A/C / 외부 LLM 응답 미참조

---

## 1. 판정

**APPROVE WITH CONDITIONS**

근거 요지: evidence 실증은 견고하고 over-claim 차단 장치(복합 자격, 조건부 R-1, deferred 명문, 자기진단 P-1~P-7)는 62/66 패턴을 충실히 답습한다. 단 **본 brief 의 *제목 명칭* 에 "GP-2 **full** PASS"** 라는 단어가 그대로 들어가 있어, 60 detection-layer 강등 cascade 의 핵심 교훈("full" 단어 자체가 over-claim trigger)과 정면으로 긴장한다. 이는 **차단(BLOCKING)이 아니라 조건부 정정** 으로 처리 — brief 본문이 무수식 "full" 을 *항상 복합 자격과 동반* 시키는지 + 발효 시 명칭이 절대 단독 "full PASS" 로 축약되지 않는지가 발효 자격의 hard 조건이다. 아래 BLOCKING 1건은 명칭 운용 규칙의 명문화 누락(잠재 축약 위험)에 대한 것이다.

---

## 2. BLOCKING (정정 필수)

### B-1 ⭐ — "full" 단어의 명칭 축약 방지 규칙 명문 부재 (60 강등 cascade 핵심 교훈 미완 답습)

**근거**:
- 본 brief **title (line 1)** = "GP-2 full PASS (detection + prevention R-2 in-repo + R-1 조건부 위임, 실 canary/R-6 Hermes trigger deferred)" — *괄호 복합 자격은 부착됨* (62 패턴 답습 ✅).
- 그러나 **§5 line 113** "권고 = GP-2 full PASS 발효 APPROVE WITH CONDITIONS", **§6.2 line 137** "GP-2 full PASS milestone", **§7 line 151** "GP-2 detection-tier → full PASS", **§9 RT-1 line 165** "GP-2 완전 PASS" 등 본문 다수 위치에서 **"GP-2 full PASS" 가 괄호 자격 없이 단독 등장**한다.
- 60 brief 의 강등 교훈(line 5, line 236 B-1)은 정확히 **"GP-2 (full) 송신 redaction PASS" 라는 *명칭 자체*가 over-claim → "detection-layer PASS" 강등**이었다. 즉 cascade 의 trigger 는 "괄호 자격 누락"이 아니라 **"full" 이라는 단어가 prevention 능동 보증 *완료* 를 함의**한다는 점이었다.
- 본 brief 의 prevention R-1 은 (a) 활성화 전제(HERMES_REDACT_SECRETS=true 미검증), (b) R-6 Tier-1 한정(Hermes dependency lock trigger 미구현), (c) 실 격리 canary 미실행 — **3중 조건부**(§4 line 100, §11 P-7 line 193). 이 상태에서 "full" 단어는 **R-1 prong 의 조건부성을 단어 차원에서 은폐**한다.

**정정 요구**: 둘 중 하나.
- (대안 1, 권장) 명칭을 **"GP-2 full-scope PASS (detection + prevention 양 prong; R-1 조건부)"** 또는 **"GP-2 PASS (full scope — detection operative + prevention R-2 in-repo + R-1 조건부)"** 로 *항상* 복합 자격과 불가분 결합. 무수식 "full PASS" / "완전 PASS" 의 본문/SESSION/INDEX/roadmap 등재 시 **단독 축약 절대 금지 규칙을 §4 또는 (C-1) 에 명문**.
- (대안 2) "full" 단어를 유지하되 **명칭 운용 규칙** 을 (C-1) 에 추가: "발효 후 roadmap/governance/SESSION 등재 시 'GP-2 full PASS' 는 반드시 'prevention R-1 조건부' 수식 동반, 단독 'GP-2 PASS' / 'GP-2 완전 PASS' 축약 = RT-1 발화".

현 brief 는 RT-1(line 165) 이 "완전 PASS over-claim 발생 시" *사후* 대응만 명시하고, **"full" 단어 자체의 *사전* 축약 방지 규칙**(feedforward)이 없다. 본 프로젝트 규약상 사후 센서보다 사전 가이드 우선(CLAUDE.md Layer 0/feedforward) — 명칭 규칙은 발효 *전* 명문이어야 한다.

> ※ 이 항목은 evidence 위조나 권위 모순이 아니라 *명칭 운용 규칙 누락* 이므로, 1pass 흡수(1문장 규칙 추가)로 해소 가능 — 그래서 판정은 REVISE 가 아닌 APPROVE WITH CONDITIONS.

---

## 3. 권고 (정정 권장, 비차단)

### R-1 — Exit (a) 판정의 "충족" 단어가 R-1 조건부성보다 강하게 읽힘

- §2 line 75 "(a)~(d) prevention 검증 충족", §2 매트릭스 (a) 통합 판정 line 69 "R-1 ∧ R-2 prevention 검증 충족", §5 line 115 "Exit (a)~(e) 충족 (R-1 조건부)".
- governance §4.5 (a) verbatim(line 451) = **"Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증"** — 이는 **R-1 AND R-2 의 AND 조건**이다. R-1 prong 이 *조건부/문서 기반* 이면, AND 의 결과인 (a) 도 **"조건부 충족"** 이지 무수식 "충족" 이 아니다.
- 본 brief 는 (a) 통합 판정 셀(line 69)에 "R-2 강 + R-1 조건부" 를 병기하여 *부분적으로* 완화했으나, §5 line 115·123 의 결론 문장은 "충족"으로 단순화된다. **권고**: (a) 의 표기를 일관되게 **"(a) 조건부 충족 (R-2 강 / R-1 조건부)"** 로 통일 — 66 SC-2 가 자기 prong 을 "조건부/문서 기반 충족"(SC-2 §5 line 141)으로 명문한 것과 정합. 이렇게 해야 "(a) 도 조건부여야 하지 않나?"(검토 지시 #2) 에 대한 답이 brief 전체에 일관 반영된다.

### R-2 — §2 (a) 셀의 detection(60) 항목 "R-4 설계 동등성" 의 prevention 무관성 명시 보강

- §2 매트릭스 (a) 행 detection(60) 셀(line 69) = "R-4 설계 동등성 (Tier-1 42)". 60 brief 는 R-4(redaction-pattern-equivalence)를 **"설계 동등성 문서, prevention 입증 아님 / Hermes safety 선언 *금지*"**(60 §2 line 96)로 강하게 한정했다. 본 SC-3 (a) 셀에서 R-4 가 prevention 충족의 *근거* 처럼 한 줄에 병기되면 설계 동등성 → prevention 격상 오인 risk. **권고**: 해당 셀에 "(설계 동등성, prevention 입증 아님 — 60 §2 답습)" 1구 추가.

### R-3 — §2 (d) 행 "pytest 167" 의 prevention 회귀 scope 명확화

- §2 (d) 행 R-2(65) 셀(line 72) = "redaction test (pytest 167)". 이는 **facade RedactionFilter 단위 회귀**(in-repo)이지 Hermes egress 자동 회귀가 아니다. 66 SC-2 의 B-1(SC-2 §2.3, line 91)이 정확히 "R-6 = Tier-1 catalog canary / Hermes dependency lock trigger 미구현"을 정정했다. 본 SC-3 (d) R-1(66) 셀은 이를 "⚠️ R-6 Tier-1 canary (Hermes lock trigger 미구현)"으로 올바르게 반영(line 72)했으므로 모순은 없다. **권고**: (d) 통합 판정(line 72) "in-repo 회귀 / R-1 Hermes trigger deferred" 표현 유지 — 이 부분은 정직하다(NOTE 로도 기록).

### R-4 — §3 "in-repo prevention cover 1" 의 cover 비대칭 잔존 명문 보강

- §3 line 87 "65 SC-1 → in-repo prevention cover 1 (R-2 facade) + Hermes 위임 (R-1) = 이중 cover (비대칭 부분 해소)". 60 §3.2 B-2(60 line 125)는 cover 구조 **비대칭**(GP-2 prevention in-repo layer 0, Hermes 단독 위임)을 "완전 동형 회피" 로 명문했다. 본 SC-3 는 "비대칭 *부분* 해소"로 적절히 완화했으나, **R-1 prong 은 여전히 in-repo cover 0(Hermes 위임)** 임이 명확히 읽혀야 한다. **권고**: "R-2 = in-repo cover 1 확보 / R-1 = 여전히 upstream 위임 (in-repo cover 0, 60 B-2 비대칭 R-1 측 잔존)" 으로 1구 보강.

---

## 4. NOTE (관찰)

- **N-1 (positive)**: §0.2 금지 매트릭스(10건) + §8 + §9 RT-1~RT-5 + §11 P-1~P-7 = over-claim 차단 장치가 60/62/66 답습으로 *구조적으로* 충실. 특히 **P-3(Hermes 안전성 선언 격상 금지, ADR-011 §7.3 답습)** + **P-4(MVP-2 PASS 62 재선언 0)** + **P-7(R-1 조건부 3중 명문)** 은 검토 지시 #4·#5·#2 를 정면 대응. ADR-011 §7.3 verbatim(line 237) "본 ADR은 Hermes 안전성을 선언하지 않는다" 와 brief §0.2 #2 / P-3 일치 — **Hermes 안전성 선언 격상 risk = 차단됨**.
- **N-2 (positive)**: **MVP-2 PASS(62) 재선언 0** 검증 통과. §0.2 #3, (C-4)(line 120), P-4(line 190) 모두 "본 cycle = GP-2 prevention-tier 격상 한정, MVP-2 PASS 명칭 갱신 = 발효 후 별도 chore" 명문. 62 brief 의 scope(G4 ledger 완전 + GP-2 detection-tier)를 흔들지 않음 → over-claim 아님.
- **N-3 (positive)**: 66 SC-2 의 R-1 조건부성(활성화 전제 + R-6 Tier-1 한정 + 실 canary deferred)이 SC-3 §4 line 100 / §11 P-7 line 193 에 3중으로 정확히 전이됨. SC-2 §5(line 141) "조건부/문서 기반 충족" → SC-3 이 이를 격상 없이 보존 — **R-1 정직성 검증 통과**(검토 지시 #2 핵심).
- **N-4 (관찰, 비차단)**: §2 (b) R-1(66) 셀(line 70) "실 격리 canary deferred (day2-r1 코드 분석)" 의 day2-r1 evidence 가 **2026-05-05 시점성**(SC-2 B-4, SC-2 §2.1 line 77)임은 SC-3 본문에 직접 노출되지 않음. SC-2 흡수 매트릭스 B-4 답습이 SC-3 §4·§7 에 암시되나, (b) 셀에 "(2026-05-05 시점, artifact 재확인 = C-3 SOP)" 1구 있으면 시점성 정직 강화. 비차단.
- **N-5 (관찰)**: §6.2 승격 트리거 4/4 발화(큰 결정 + 보안 + cross-vendor + 명칭 over-claim risk) → 풀 3+1 + 외부 LLM 1+ 정당. PASS 발효 milestone 답습(60/62/32)과 정합.
- **N-6 (절차 관찰)**: 본 brief 작성자 = 60/62/65/66 작성자(Claude). §11 P-6(line 192) 이 cross-vendor codex + 풀 3+1 독립 검증으로 cascade 완화 명문 — 본 세션 over-claim 5회 포착(메모리 feedback_pass_scope_overclaim)이 process 가치 입증. 본 Agent B 독립 검증이 그 layer 의 일부.

---

## 5. 권위 인용 cross-verify 매트릭스 (brief 인용 vs 실제 문서)

| # | brief 인용 | 위치 | 실제 문서 verbatim | 판정 |
|---|-----------|------|-----------------|------|
| 1 | governance §4.5 (a) = "Hermes native(R-1) + facade(R-2) 검증" (AND) | §0.3 line 46, §2 | governance line 451 "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" | ✅ **일치** (AND 구조 정확) |
| 2 | governance §4.5 Exit (a)~(e) 5조건 | §0.3, §2 매트릭스 | governance §4.5 line 447~455 (a)~(e) 5행 존재 | ✅ **일치** |
| 3 | ADR-011 §2.3 #2 = "Hermes 자체 redaction 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0" | §2 (c), §4, §0.3 | ADR-011 line 113 운영 함의 #2 "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰: 저장 경로(DB/파일) 차단 책임 없음" | ✅ **일치** (위임 권위) |
| 4 | ADR-011 §7.3 = 안전성 선언 금지 | §0.2 #2, §11 P-3 | ADR-011 line 237 "본 ADR은 Hermes 안전성을 선언하지 않는다 — Hermes는 검증 대상이며..." | ✅ **일치** |
| 5 | ADR-011 §2.1 (a)~(d) 4조건 모법 | §0.3 line 51 | ADR-011 line 55~61 (a)~(d) 표 + "*수단 자유*가 아니라 *목적 달성 검증 의무*" | ✅ **일치** |
| 6 | 60 = "GP-2 (full) PASS → detection-layer PASS 강등" | §1 line 57, §3 | 60 brief line 5 "GP-2 (full) 송신 redaction PASS → detection-layer PASS 강등" + line 236 B-1 | ✅ **일치** (강등 사실 정확) |
| 7 | 62 = MVP-2 PASS = GP-2 detection-tier (full = 후속 trajectory) | §1 line 58, §0.2 #3 | 62 brief title + line 7 "full GP-2 PASS (prevention) 아님" + line 13 후속 trajectory | ✅ **일치** |
| 8 | 65 SC-1 = R-2 facade RedactionFilter in-repo operative (15 test, 커버리지 92%) | §0.3 line 48, §2, §10 E-2 | 65 SC-1 brief line 1 "facade redaction layer real (R-2 GP-2 prevention)" + 발효 효과 "in-repo operative" + B-2 group-aware 치환 | ✅ **일치** (단 "15 test/92%" 수치는 본 매트릭스에서 65 brief head 만 확인 — 정합 추정, full 본문 미대조) |
| 9 | 66 SC-2 = R-1 조건부/문서 기반 위임 검증 (활성화 전제 + R-6 Tier-1 한정) | §0.3 line 49, §2, §4 | 66 SC-2 brief line 5/13 + §5 line 141 "조건부/문서 기반 충족" + B-1 R-6 Tier-1 한정 + B-2 활성화 전제 | ✅ **일치** (조건부성 정확 전이) |
| 10 | governance §4.5 (a) = R-1/R-2 **prevention** 검증 (60 B-1 해석) | §2 (a), §4 | 60 brief §2 line 96 "governance §4 (a) = prevention (R-1/R-2) 검증" | ✅ **일치** (60 해석 답습) |

**cross-verify 결론**: 권위 인용 10/10 일치, **모순 0**. 인용 정직성은 견고하다. (8 의 "15 test/92%" 수치만 65 본문 full 미대조 — 65/66 합의가 이미 검증한 값이므로 신뢰, 단 발효 brief 의 수치는 발효 시 1회 재확인 권장.)

---

## 6. 종합

| 검토 지시 항목 | 결과 |
|---|---|
| #1 명칭 over-claim 차단 ("full" 단어) | ⚠️ **B-1** — 괄호 복합 자격은 부착, 단 본문 다수 무수식 "full PASS" + 단어 자체 축약 방지 규칙 부재 |
| #2 Exit (a) R-1 ∧ R-2 충족 정직성 | ⚠️ **R-1 권고** — (a) "충족" → "조건부 충족" 일관화 필요. SC-2 가 R-1 조건부 명문한 것은 정확히 전이됨 |
| #3 권위 인용 정합성 (verbatim) | ✅ 10/10 일치, 모순 0 |
| #4 Hermes 안전성 선언 격상 risk | ✅ 차단 (§0.2 #2 + P-3, ADR-011 §7.3 verbatim 일치) |
| #5 MVP-2 PASS(62) 재선언 0 | ✅ 통과 (§0.2 #3 + C-4 + P-4) |
| #6 prevention 조건부 scope 정직 | ✅ 충분 (§4 deferred 3건 명문: 실 canary / R-6 Hermes trigger / R-5 base64) |

**최종 판정: APPROVE WITH CONDITIONS**

**발효 hard 조건**:
- (C-B1) **명칭 축약 방지 규칙 명문** — 무수식 "GP-2 full PASS" / "완전 PASS" 단독 등재 금지, 항상 "prevention R-1 조건부" 수식 동반 (대안 1 권장: "full-scope" 재명명). RT-1 사후 대응 + 사전 feedforward 규칙 병행.
- (C-R1) Exit (a) 표기 "충족" → "조건부 충족 (R-2 강 / R-1 조건부)" 일관화.

권고 R-2/R-3/R-4 + NOTE N-4 는 1pass 흡수 시 함께 처리 권장(비차단).

---

**Agent B 독립 분석 끝.**
