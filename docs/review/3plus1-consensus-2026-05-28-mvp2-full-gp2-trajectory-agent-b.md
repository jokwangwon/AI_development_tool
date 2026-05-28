# 3+1 합의 — Agent B (품질/안전성 검증가) 응답

> **대상**: `docs/phase0/mvp2-full-gp2-pass-trajectory-entry-brief.md` (v1, §0~§13)
> **관점**: "안전하고 견고한가?" (보안, 엣지케이스, 문서 정합성)
> **날짜**: 2026-05-28 (64번째 entry cycle — 세션 #3)
> **독립성**: Agent A/C 및 외부 LLM(codex) 응답 미참조 (편향 방지). 모든 인용 = 실제 문서 직접 read 교차검증.

---

## 1. 판정

**APPROVE WITH CONDITIONS**

본 brief 는 trajectory **진입 자격 audit + 경로 분석 + 합의 형태 권고** 한정 scope 를 정직하게 유지하며, 본 세션 #2 의 over-claim cascade 4회 교훈 ([[feedback_pass_scope_overclaim]]) 을 §13 P-4 / (C-5) 에 명문 답습한다. detection ≠ prevention 구분이 §1.2 3축 + §2.1 + §13 P-4 에 일관 명시되어 over-claim 0 이다. 권위 인용 verbatim cross-verify 결과 핵심 인용(governance §4.5 (a) line 451, ADR-011 §2.3 #2/#4, §2.4 T3, ADR-009 §2/§2.3, R-4 = 설계 동등성, ADR-011 §7.3)은 전원 **일치**. 단, **citation 정밀도 결함 1건 (BLOCKING B-1)** + 경계/엣지 보강 권고 4건. evidence 차단급 over-claim 0 이므로 1pass 흡수 후 APPROVE 가능.

---

## 2. BLOCKING (발효 전 정정 필수)

### B-1 — §1.1 line 70 citation 오귀속 (`(β) §0.2 #23` → `#10`)

brief §1.1 line 70:

> "**R-1 import = 별도 cycle ((β) §0.2 #9) / R-2 facade real = 별도 trajectory ((β) §0.2 #23)**"

**실제 57 (β) brief 직접 read 결과**:
- (β) §0.2 #9 (line 43) = "Hermes upstream `agent/redact.py` 본 repo 內 import 결정 (R-1 구현 경로)" → R-1 인용 **일치 ✅**
- (β) §0.2 **#10** (line 44) = "`adapters/llm/facade.py` placeholder → real (R-2 구현 경로, TR-1)" → **이것이 R-2 facade real 의 정확한 source**
- (β) §0.2 **#23** (line 57) = "자동 후속 실 구현 sub-cycle 진입" → **R-2 와 무관한 항목**

→ brief 의 "R-2 facade real = (β) §0.2 #23" 은 **#10 의 오귀속**. 권위 인용의 핵심 = source line 정확성인데, #23 인용 시 독자가 57 brief #23 ("자동 후속") 을 R-2 근거로 오인할 수 있음.

**근거**: 본 프로젝트 §7 문서 의존 관계 + [[feedback_pass_scope_overclaim]] (citation 정정 = 본 세션 #2 B-3 동형). 61 entry R-S1 정정도 동일 성격 (ADR-012 §2.3 vs §2.8 citation 오류) — citation 정밀도는 본 프로젝트가 반복적으로 BLOCKING 처리해 온 항목.

**정정 권고**: `(β) §0.2 #23` → `(β) §0.2 #10`. (§5.2 / §13 P-3 등 동일 인용 연쇄 확인 — brief 본문 다른 위치에는 #23 재발 없음, line 70 단독.)

---

## 3. 권고 (조건부 흡수)

### R-B-1 — RT-1 (RedactionFilter 미부착 window) 보안 엣지케이스 보강 — **핵심 안전성**

§8 RT-1 = "facade real 후 RedactionFilter 미부착 window → (R-2-a) 동시 구현 (분리 금지)" 로 trigger 식별은 되어 있으나, **window 동안의 실 위험 = LLM API request body 평문 secret 송신 (헌법 8조 본질)**. 이는 단순 "분리 금지" 권고를 넘어, **(R-2-a) 동시 구현이 sub-cycle SC-1 의 BLOCKING 조건**임을 명문화 권고. 현 §4.4 (R-2-b) "facade real 먼저 / filter 후속" 후보가 §8 RT-1 과 **직접 충돌** — (R-2-b) 채택 = RT-1 window 발생을 구조적으로 허용. brief 는 §4.4 ⭐ 권고로 (R-2-a) 를 선호하나, (R-2-b) 를 후보로 *남겨두는* 것 자체가 SC-1 sub-cycle 에서 안전성 약화 옵션을 제공. 권고: §4.4 (R-2-b) 옆에 "RT-1 위반 = SC-1 미충족" 명문 추가 (결정은 sub-cycle 이나, *안전 제약*은 trajectory 진입 시점 고정 가능).

### R-B-2 — RT-2 (Hermes upstream silent 깨짐) 의 detection 공백 명시 보강

§8 RT-2 = "Hermes upstream redaction silent 깨짐 → R-6 자동 재실행 + R-5 canary 재검증" 으로 대응이 매핑되나, **본 repo 는 R-1 import 0 (R-1-a 위임 검증 권고) 상태** = Hermes runtime redaction 이 실제로 본 repo runtime 에 *적용되지 않음*. 즉 R-6/R-5 가 검증하는 것은 **upstream `agent/redact.py` 패턴 동등성/회귀**이지, *본 repo 가 Hermes redaction 을 통과시킨다는 보증이 아님*. 이 비대칭 (60 brief §3.2 B-2 "cover 구조 비대칭, in-repo 능동 redaction 보증 0" 답습)을 RT-2 대응란에 명시 권고 — 그렇지 않으면 "R-6 + R-5 = prevention 보증" 으로 읽힐 over-claim risk (P-4 cascade 인접). evidence 실증 차원에서 R-6 actual run (`25482284523` PASS, ADR-011 §8.5.1 R-6) 은 *upstream 패턴 회귀* 검증이지 *본 repo prevention* 이 아님을 SC-2 evidence (E-4) 후보 설명에 부착.

### R-B-3 — R-5 base64/URL evasion known limitation 의 영구성 vs full GP-2 PASS 자격 관계 명시

§0.2 #7 + §8 RT-4 + §10 = R-5 evasion 영역 영구 분리 (G3-4) 로 일관 처리되나, **full GP-2 PASS 명칭이 "Tier-1 42 평문 redaction 한정" 자격을 *명시적으로* 부착하는지** 가 §7 권고에 누락. 60 brief §4.1 + (C-2) 는 "GP-2 PASS = Tier-1 42 catalog 평문 한정 (base64 evasion 제외 명문)" 을 명시했는데, 본 trajectory entry brief §7 (C-1~C-5) 에는 동등 명문이 약화됨 ((C-5) 에 over-claim 주의는 있으나 base64 자격 부착은 §8 RT-4 로만). 권고: §7 조건에 "(C-6) full GP-2 PASS = Tier-1 42 평문 redaction prevention 한정, base64/URL/압축 evasion 제외 명문 ([[feedback_pass_scope_overclaim]] detection≠prevention + 자격 부착 답습)" 추가 — full GP-2 PASS 가 SC-3 에서 무수식 "GP-2 PASS" 로 격상되는 cascade (62 B-1 동형) 사전 차단.

### R-B-4 — §6.2 trigger 4 "권위 chain 다중 source 손상 ❌" 판정의 정밀성

§6.2 trigger 4 = "권위 chain 다중 source 손상 ❌ — 권위 인용 답습 (governance §4.5 + ADR-011 §2.3)". 그러나 본 B-1 (citation 오귀속) 은 *경미한* 권위 인용 손상에 해당. trigger 4 = ❌ 유지는 정당 (다중 source 손상 아님, 단일 line citation 정밀도 결함)하나, B-1 정정 후에도 ❌ 유지가 적절함을 합의 보고서가 확인 권고. (이 항목은 NOTE 급이나 trigger 판정 정합성 차원에서 권고 분류.)

---

## 4. NOTE (관찰)

- **N-B-1 (scope 경계 안전성 — §0.2 13개 준수 확인)**: §0.2 "하지 않는 것" 13개 전수 대조 결과 **본문 침입 0**. 특히 #2 (R-1 import 결정 0), #3 (R-2 facade real 구현 0), #9 (ADR/헌법/governance 본문 갱신 0), #10 (`facade.py` placeholder 보존) 은 §3.3/§4.4 가 모두 "(결정 = sub-cycle, 본 cycle = 권고만)" 으로 명문 종결 — 경계 침입 없음. `facade.py` 직접 read 결과 placeholder 보존 확인 (`raise NotImplementedError`, `health() → {}`). 실제 코드 변경 0.

- **N-B-2 (Hermes ≠ root of trust 안전성 — R-1-a/R-1-b)**: §3.2 line 118 "Hermes ≠ root of trust (line 95~108): Hermes 출력은 Tools 로 검증 → R-1 검증 = canary/test 가 Hermes 위에 위치" 는 ADR-011 §2.3 권위 위계 (line 95~108 Constitution > ADR > SDD > Harness Gates > Hermes) 와 **정합 ✅**. R-1-b (import 통합) 가 권위 위계 위반 가능성을 §3.3 ⭐ 권고 + §8 RT-5 가 선제 식별 — "(R-1-b)이 Hermes ≠ root of trust 위반 → 위임 검증 (R-1-a) 환원 또는 Hermes PMO 경계 합의". 안전한 처리. R-1-a (위임 검증 우선) 권고는 ADR-011 §2.3 #2 위임 권위 + 본 repo = DESIGN repo 정체성에 부합 — **import 가 권위 위계를 깨지 않음** (import 해도 Hermes 출력은 여전히 Tools 로 검증, 단 ADR-009 §2.3 Hermes PMO ≠ provider 경계 평가 필요). §3.3 가 이를 정확히 ADR-009 §2.3 으로 매핑.

- **N-B-3 (prevention over-claim risk — 핵심 검증 결과)**: brief 가 R-4 (설계 동등성)를 prevention 입증으로 오인하지 **않음 ✅**. §1.2 축 2 line 75 "R-4 = Tier-1 42 catalog *패턴 동등성 문서*. prevention 입증 아님 (Hermes 안전성 선언 금지)", §2.1 (a) line 88 "⚠️ partial (설계 동등성)", §13 P-4 "R-4 = 설계 동등성, prevention 입증 아님" — 3중 명문. R-4 문서 직접 read 결과 §1.3 line 39 "Hermes 안전성 선언 금지 — ADR-011 §7.3" + §10.3 line 481 "본 문서는 trigger UDF 동등성을 선언하지 않는다" 와 정합. "full GP-2 PASS" 명칭은 brief 전체에서 **trajectory 진입 자격** 한정으로 사용되며 (§0.2 #1, §13 P-1), *발효는 SC-3 별도* 로 일관 — 명칭 자격 정직.

- **N-B-4 (governance §4.5 (a) verbatim 정합)**: brief §0.3 line 49 + §2.2 line 96 인용 "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" = governance line 451 **verbatim 완전 일치 ✅**. 2-pronged (R-1 검증 ∧ R-2 검증) 해석 정확 (§5.1 line 161 AND 명시).

- **N-B-5 (문서 의존 관계 — CLAUDE.md §7)**: ADR-011/governance §4 본문 변경 0 (§0.2 #9 + #10 보존). brief = phase0 신규 1 문서, 권위 chain 등재 0 (§0.2 #13). §7 의존 관계 (governance §4.5 / ADR-011 §2.1 5조건 / ADR-008 부록 B) 답습 — 본 brief 자체가 권위 문서가 아니라 합의 입력이므로 연쇄 갱신 trigger 0. ✅

- **N-B-6 (RT-3 Provider Liquidity 위반 — 5조-2 비협상)**: §8 RT-3 = "LiteLLM 도입이 Provider Liquidity 위반 (provider lock-in) → ADR-009 §2.3 facade 단일 진입점 강제 + 5-way Defense". ADR-009 §2.3 직접 read 결과 (line 89) "Provider 추가/제거/교체 = config 변경 + 사용자 명시 승인 (T2)" + facade 단일 진입점 (line 75 #6) 과 정합 ✅. (C-4) "LiteLLM 도입 = Q1 합의 보존 (신규 0)" 은 §0.2 #11 과 일관 — 본 cycle Provider Liquidity 본문 변경 0. 단 R-2 facade real = "Provider Liquidity Layer 1 실 구현" (§4.3 line 144) 격상은 SC-1 sub-cycle 의 실 구현 영역이며 trigger 6 발화 정당.

- **N-B-7 (작성자 cascade self-진단)**: §13 P-7 "작성자 = 60/62 작성자 (Claude) cascade → cross-vendor codex + 풀 3+1 독립 검증". 본 세션 #2 over-claim 4회 포착 입증 답습 — meta-편향 회피 정직. 본 Agent B 독립 검증도 이 frame 에 부합 (citation B-1 포착).

---

## 5. 권위 인용 cross-verify 매트릭스 (brief 인용 vs 실제 문서 직접 read)

| # | brief 인용 위치 | brief 주장 | 실제 문서 | 판정 |
|---|---------------|----------|----------|------|
| 1 | §0.3 / §2.2 (line 49, 96) | governance §4.5 (a) line 451 = "Hermes native redaction Tier-1 42 catalog 적용 검증 + P1 facade redaction filter 검증" | governance line 451 verbatim 동일 | **일치 ✅** |
| 2 | §0.3 / §3.2 (line 50, 116) | ADR-011 §2.3 #2 line 113 = "Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰, 저장 경로 책임 0" | ADR-011 line 113 = "**Hermes 자체 redaction은 로그/LLM 송신 방어로만 신뢰**: 저장 경로(DB/파일) 차단 책임 없음" | **일치 ✅** (의미 동일, "0" = "없음") |
| 3 | §3.2 (line 118) | Hermes ≠ root of trust 권위 위계 line 95~108 | ADR-011 §2.3 line 95(제목)~108(위계 코드블록 + 운영함의 시작) | **일치 ✅** |
| 4 | §0.3 / §12 (line 51) | ADR-011 §2.4 T3 line 133 = ADR/헌법/Harness Gates 정의 변경 = 풀 3+1 | ADR-011 line 133 = "**T3** 자동 금지(절대) Constitution/ADR/Harness Gates 정의 자체의 변경 단축 또는 풀 3+1 합의" | **일치 ✅** |
| 5 | §0.3 (line 52) | ADR-009 §2 line 49~62 = P1 facade MVP 진입조건 2026-05-04 충족 | ADR-009 line 49~62 = §2.1 MVP 진입 4조건 전원 2026-05-04 충족, "별도 트리거 없음" | **일치 ✅** |
| 6 | §4.3 / §12 (line 143) | ADR-009 §2.3 = Hermes PMO ≠ provider, facade 단일 진입점 | ADR-009 §2.3 (line 77~99) = "Hermes PMO가 provider를 직접 소유하지 않는다", facade 단일 진입점 (line 75) | **일치 ✅** |
| 7 | §0.3 / §13 P-4 (line 53) | R-4 (`redaction-pattern-equivalence.md`) = 설계 동등성, "Hermes 안전성 선언 금지 (ADR-011 §7.3)", prevention 입증 아님 | R-4 §1.3 line 39 = "Hermes 안전성 선언 금지 — ADR-011 §7.3 '본 ADR은 Hermes 안전성을 선언하지 않는다'" + 상태 line 5 "코드 수정 미포함" | **일치 ✅** (ADR-011 §7.3 line 237 = "본 ADR은 Hermes 안전성을 선언하지 않는다" 도 일치) |
| 8 | §4.2 (line 138) | governance §4.3 line 435 = "P1 v2 LLM facade RedactionFilter" 계산적 강제 (P1 facade layer) | governance line 435 = "계산적 \| P1 v2 LLM facade RedactionFilter \| P1 facade layer" | **일치 ✅** |
| 9 | §2.1 (d) / §8 RT-2 (line 91, 224) | ADR-011 §2.3 #4 = Hermes 의존성 업그레이드 자동 R-6 재실행 | ADR-011 line 115 = "Hermes 의존성 업그레이드는 자동 R-2 재실행으로 회귀 검증 (R-6)" | **일치 ✅** |
| 10 | §1.1 (line 70) | R-1 import = 별도 cycle ((β) §0.2 **#9**) | 57 (β) line 43 = #9 "Hermes upstream `agent/redact.py` import 결정 (R-1 구현 경로)" | **일치 ✅** |
| 11 | §1.1 (line 70) | R-2 facade real = 별도 trajectory ((β) §0.2 **#23**) | 57 (β) line 57 = #23 "자동 후속 실 구현 sub-cycle 진입" (R-2 무관). 정확한 source = **#10** (line 44 facade placeholder→real) | **모순 ❌ (B-1)** |
| 12 | §0.3 / §1.1 (line 57, 68) | 52 entry R-A-1 = `agent/redact.py` 본 repo 부재 = upstream v0.12.0 401 LOC | R-4 §2 line 46 = "`/tmp/hermes-phase0/.../agent/redact.py` (v0.12.0 main HEAD, 401 LOC)" + 본 repo 직접 확인 부재 | **일치 ✅** (upstream clone /tmp 현재 미존재이나 부재 답습 = 본 repo scope 외, 정합) |
| 13 | §4.1 (line 132) | `facade.py` = placeholder, `complete()` = NotImplementedError, `health()` = `{}` | `src/adapters/llm/facade.py` 직접 read = `raise NotImplementedError(...)` + `async def health(): return {}` | **일치 ✅** (단 brief "42 LOC" vs 실제 42줄 — `wc` 미확인이나 파일 1390 byte, 본문 42줄 대략 일치) |
| 14 | §1.2 / §2.1 (b)(d) | detection-tier evidence = secret-hygiene D-2 + secret_scanner.py + actual run `26517803107` (60 brief 답습) | `.github/workflows/secret-hygiene-egress-redaction.yml` + `tools/secret_scanner.py` 존재 확인. run id = 60 brief 인용 (본 cycle 직접 미재확인, 60 답습) | **일치 ✅** (60 brief 답습, 본 cycle scope = 재선언 0) |

**매트릭스 요약**: 14건 中 **13 일치 / 1 모순 (B-1, citation 오귀속 #23→#10)**. 핵심 권위 인용 (governance §4.5 (a), ADR-011 §2.3/§2.4, ADR-009 §2/§2.3, R-4 설계 동등성, ADR-011 §7.3) 전원 verbatim 일치. 모순 1건은 source line 정밀도 결함 (의미 손상 아님), B-1 정정 후 전원 일치.

---

## 6. 종합 (Agent B 안전성 결론)

1. **prevention over-claim risk = 통제됨 (핵심 검증 PASS)**: detection ≠ prevention 구분 3중 명문 (§1.2 + §2.1 + §13 P-4), R-4 = 설계 동등성 (prevention 입증 아님) 명확, "full GP-2 PASS" = trajectory 진입 자격 한정 (발효 = SC-3 별도). 본 세션 #2 4회 cascade 교훈 답습 정직 (N-B-3).
2. **scope 경계 안전 = 침입 0**: §0.2 13개 전수 준수, `facade.py` placeholder 보존 직접 확인, ADR/governance 본문 변경 0 (N-B-1, N-B-5).
3. **Hermes ≠ root of trust 안전 = 정합**: R-1-a 위임 검증 권고 + RT-5 (R-1-b 위반 환원) 선제 식별, 권위 위계 보존 (N-B-2).
4. **보안 엣지케이스 = 식별 양호, 보강 권고 3건**: RT-1 window 안전 제약 명문 (R-B-1), RT-2 cover 비대칭 명시 (R-B-2), R-5 base64 자격 부착 (R-B-3).
5. **citation 정밀도 = BLOCKING 1건 (B-1)**: #23 → #10 오귀속. 본 프로젝트 반복 BLOCKING 항목 (R-S1 동형), 정정 필수.

→ **B-1 1pass 흡수 + R-B-1~R-B-3 v1.1 반영 권고 → APPROVE WITH CONDITIONS**. trajectory 진입 자격 자체는 정직하게 충족 (detection-layer PASS ✅ + MVP-2 PASS prevention 잔여 명문 ✅ + 격차 = (a) prevention 검증 정확 정의). 실 sub-수단 결정/구현/발효 0 경계 준수.

---

**Agent B 응답 끝.**
