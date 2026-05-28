# MVP-2 진입 합의 entry brief — Agent B 응답 (품질/안전성 검증가)

> **본 응답은 풀 3+1 합의 (52 entry) 의 *병렬 독립* Agent B 응답이며 — 단독으로 (i) 본 brief v1 발효, (ii) MVP-2 진입 권한 발효, (iii) sub-수단 결정 cycle (β) 진입 자격 발효, (iv) 분리 영역 결정 cycle (γ) 진입 자격 발효, (v) Rollback Trigger / Evidence 본문 채택, (vi) ADR / 헌법 / roadmap / governance-preconditions / provider-agnostic-memory-skill-design / ADR-012 본문 갱신, (vii) GP-2 sub-수단 결정 (R-1~R-5), (viii) G4 §4.4 Layer 4 sub-수단 결정 (L-1~L-5), (ix) threshold 고정, (x) Tier-2/3 catalog 자동 확장, (xi) Hermes PMO 격상, (xii) MVP-1 PASS 재선언, (xiii) `adapters/llm/facade.py` placeholder → real, (xiv) 외부 library (`pyjcs` / `rfc8785`) 도입 결정, (xv) MVP-2 자동 진입 — 어떤 행위도 자동 발생시키지 않는다. 본 응답 = Reviewer 통합 입력 자료 한정.**

---

**작성일**: 2026-05-28
**검토자**: Agent B (품질/안전성 검증가) — Claude Opus 4.7 (1M context, 본 cycle)
**합의 형태**: 풀 3+1 + 외부 LLM 1+ (52 entry, Agent B 병렬 독립 응답)
**검토 대상**: `docs/phase0/mvp2-entry-brief.md` (v1, 480줄, §0~§10, 2026-05-28)
**판정**: ⚠️ **REVISE** (BLOCKING 2건 + 권고 4건 + NOTE 3건) — 본 brief v1 → v1.1 1pass 흡수 보강 후 Reviewer 통합 단계 진입 권고. 권위 chain 의 **CONFIRMED divergence** (P-4 잠재 risk → 확정 risk 격상) + ADR-011 §2.1 모법 framing 부정확성 2건 BLOCKING, sub-수단 결정 cycle 분리 / 헌법 답습 / 51 entry audit cross-check 정합성 등 망라성 영역 정확.

---

## §0 총평

| 항목 | 평가 |
|---|---|
| 판정 | **REVISE** |
| BLOCKING | **2건** (R-B-1 ADR-012 §2.3 Layer 4 vs G4 §4.4 Layer 4 **CONFIRMED divergence**, R-B-2 ADR-011 §2.1 (a)~(e) "5조건 모법" framing 부정확성) |
| 권고 | **4건** (N-B-1 ~ N-B-4) |
| NOTE | **3건** (NT-B-1 ~ NT-B-3) |
| 6 검토 의무 항목별 평가 | §4 참조 (1 ✅ 정확 + 2 ⚠️ 확정 risk 발견 + 3 ✅ 정확 + 4 ✅ 정확 + 5 ⛔ 격상 의무 + 6 ✅ 충분) |

**핵심 발견 (Agent B 관점)**:
- ⛔ **R-B-1 (BLOCKING)**: brief §10 P-4 가 "잠재 risk" 로 분류한 ADR-012 §2.3 line 182 vs G4 §4.4.1 line 649 의 "Layer 4" 정의 충돌은 verbatim 직접 read 결과 **CONFIRMED divergence** 이다. ADR-012 §2.3 line 182 = "**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**" / G4 §4.4.1 line 649 = "**Layer 4 — CI 회귀 검증 (MANDATORY)**" — 두 권위 source 의 Layer 4 가 **완전히 다른 영역** (G4 의 "Layer 4 = CI 회귀 검증" 은 ADR-012 §2.3 의 "Layer 4 = External anchor" 와 동일 이름 / 다른 정의 — ADR-012 §2.3 의 Layer 매트릭스는 4 layer 체계 (Layer 1~4), G4 §4.4.1 의 Layer 매트릭스는 5 layer 체계 (Layer 1~5)). 이는 brief 가 "잠재 risk + Reviewer 단독 verify 자격" 영역으로 처리할 *수준이 아니라*, brief §1.3 본문 표현 + §3 매트릭스 + §1.1 권위 인용 모두 **권위 chain 다중 source 손상 risk = 7 trigger 중 (4) 발화 영역 격상 의무** 발생.
- ⛔ **R-B-2 (BLOCKING)**: brief §1.1 line 94 + §3 헤더 "ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스" 표현 중 **§1.1 line 94 = "ADR-011 §2.1 (a)~(e) 5조건 모법"** 으로 단축 표현 (line 94 verbatim: "5조건 모법 — (a) 동등 보안 결과 / (b) 격리 PoC / (c) ADR/SDD 권위 / (d) 자동 회귀 검증 / (e) 합의 APPROVE"). 그러나 ADR-011 §2.1 원문 (line 53) verbatim = "다음 **4조건** 을 모두 충족할 때 기존 수단을 대체할 수 있다 — (a)~(d)". **(e) 합의 APPROVE 는 ADR-011 §2.1 의 모법이 아니라 governance-preconditions §4.5 Exit 표 line 455 의 운영조건** 으로 추가된 영역. brief §3 헤더 (line 219) 는 정확하게 "(a)~(d) + 합의 APPROVE 운영조건 (e)" 로 표현 — §1.1 line 94 표현이 §3 헤더와 *내적 모순*. 권위 source 정확성 차원 BLOCKING.
- ⚠️ **R-S1 격상 결과**: 24 entry R-S1 답습 패턴 (잠재 risk → Reviewer 단독 verify) 의 본 cycle 적용 자격은 24 entry 와 본 cycle 의 *위험 수준 차등* 명시 의무 — 본 cycle R-S1 = **확정 divergence** (verbatim 검증 완료) → §9.5 "별도 cycle" deferred 영역 한정 처리 부족, brief v1.1 흡수 영역 BLOCKING.

---

## §1 BLOCKING 2건

### R-B-1 — ADR-012 §2.3 Layer 4 vs G4 §4.4.1 Layer 4 **CONFIRMED divergence** (P-4 잠재 risk 격상 의무)

**위치**: brief §1.3 line 110 + §4.3 trigger (4) "부분 발화" + §10 P-4 "잠재 risk"

**brief 현재 표현** (line 110):
> "**⚠️ 권위 미세 충돌 흡수 — ADR-012 §2.3 line 182 = "Layer 4 RECOMMENDED MVP" vs G4 §4.4.1 line 649 = "Layer 4 MANDATORY"**. 본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY). ADR-012 §2.3 line 182 = Layer 4 *External anchor* (Layer 5 영역) 와 혼동 위험 (line 182 verbatim 재확인 의무, R-S1 유형 잠재 risk → 본 brief §10 P-? 자기진단 영역). 본 (α) 합의 발효 시 cross-reference 정정 cycle 후속 영역."

**Agent B verbatim 직접 read 결과** (Read tool, ADR-012 line 165~185):
```
[ADR-012 §2.3] - 4 layer 체계
Layer 1 — Hash Chain (MANDATORY 모든 환경)
Layer 2 — Git append-only branch (MANDATORY)
Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)
Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)
```

**Agent B verbatim 직접 read 결과** (Read tool, provider-agnostic-memory-skill-design line 631~660):
```
[G4 §4.4.1] - 5 layer 체계
Layer 1 — Hash Chain (MANDATORY 모든 환경)
Layer 2 — Git Append-only Branch (MANDATORY)
Layer 3 — Signed Commit (RECOMMENDED MVP, MANDATORY multi-host)
Layer 4 — CI 회귀 검증 (MANDATORY)
Layer 5 — External Anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)
```

**Agent B 확정 판단**:
- ADR-012 §2.3 은 **4 layer 체계** — Layer 4 = External anchor
- G4 §4.4.1 은 **5 layer 체계** — Layer 4 = CI 회귀 검증, Layer 5 = External anchor
- 두 source 의 **"Layer 4" 라는 이름이 가리키는 영역이 서로 다르다**
- 이는 brief 가 "Layer 4 vs Layer 5 혼동" 으로 framing 한 것 수준의 *명명 충돌* 이 아니라, **권위 source 자체의 Layer 매트릭스 체계 (4 vs 5) 가 다른 영역 — confirmed structural divergence**

**왜 BLOCKING 인가**:
1. brief §1.1 line 101 = "ADR-012 §2.3 (다층 강제)" 인용 — **본 brief 의 권위 chain 핵심 source 1개의 Layer 정의 자체가 본문에서 G4 §4.4.1 와 충돌** → 권위 chain 다중 source 손상 risk = 7 풀 3+1 승격 trigger (4) **발화** 영역 (brief §4.3 의 "부분 발화" 분류 부족)
2. brief §1.3 line 110 = "본 cycle = G4 §4.4.1 line 649 답습 (Layer 4 = MANDATORY)" → **선차 변경 매트릭스에서 G4 §4.4.1 답습 측 결정만 명시하고, ADR-012 §2.3 측 영향 평가 0 + 정정 영역 = §9.5 별도 cycle deferred 한정** → 풀 3+1 합의 의 *현재 cycle 內* 처리 의무 (R-S1 = "Reviewer 단독 verify 자격" 으로 처리 가능한 범위 초과, R-S1 답습 패턴 자체 미흡 → 별도 정정 cycle 의무로 격상)
3. brief §10 P-4 = "ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험" 표현 → **verbatim 재확인이 *이미* 본 응답 (Agent B) 에서 수행 완료** → P-4 는 더 이상 "잠재 risk" 가 아니라 **확정 divergence** 로 격상 의무. brief 작성자 (Claude Opus 4.7) 가 self-reading 시점 verbatim 재확인 안 한 자격 미숙성 자체가 자기진단 P-4 답습 부족

**요구 수정** (brief v1.1):
- (a) §1.3 line 110 의 "ADR-012 §2.3 line 182 = Layer 4 RECOMMENDED MVP" 표현을 **"ADR-012 §2.3 의 4 layer 체계에서 Layer 4 = External anchor (RECOMMENDED MVP) — G4 §4.4.1 의 5 layer 체계에서 Layer 4 = CI 회귀 검증 (MANDATORY), Layer 5 = External anchor (RECOMMENDED MVP)"** 로 verbatim 확장
- (b) §4.3 trigger (4) = "부분 발화" → **"발화"** 로 격상 + 근거 명시
- (c) §10 P-4 = "잠재 risk" → **"확정 divergence"** 로 격상 + 본 cycle 內 정정 영역 vs 별도 cycle deferred 영역 분류 의무
- (d) §9.5 "R-S1 정정 영역 — 별도 cycle" → **"ADR-012 §2.3 Layer 매트릭스 권위 source 정합 cycle (4 layer vs 5 layer 체계 통일)"** 로 본 cycle 발효 후 *즉시* 사용자 명시 진입 권고 영역으로 격상 (별도 cycle deferred 한정 부족)
- (e) **본 cycle (α) 합의 = "MVP-2 영역 진입 권한 발효" 자격은 R-B-1 정정 cycle 후속 의무 영역인가, 동시 진행 영역인가** 사용자 명시 결정 영역 brief 본문 추가 (Agent B 판단 = 동시 진행 가능 — 본 R-B-1 정정 = brief v1.1 1pass 흡수 + 별도 정정 cycle 영역, MVP-2 진입 발효 의 *block* 영역 아님 — 단 brief v1.1 흡수 부족 시 합의 발효 자격 부족)

---

### R-B-2 — ADR-011 §2.1 (a)~(e) "5조건 모법" framing 부정확성 (권위 source 정확성)

**위치**: brief §1.1 line 94 + §3 line 219 + §0.1 line 32

**brief 현재 표현 1** (line 94, ⭐ 정확하지 않은 framing):
> "ADR-011 §2.1 (a)~(e) | 2026-05-06 | 5조건 모법 — (a) 동등 보안 결과 / (b) 격리 PoC / (c) ADR/SDD 권위 / (d) 자동 회귀 검증 / (e) 합의 APPROVE | 본 cycle = MVP-2 영역 진입 자격 = 5조건 *경로* 권고"

**brief 현재 표현 2** (line 219, ⭐ 정확한 framing):
> "## §3 ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) — 5조건 매트릭스 (두 영역별)"

**brief 현재 표현 3** (line 32, ⭐ 정확한 framing):
> "두 영역 *진입 자격* 분석 — ADR-011 §2.1 (a)~(d) + 합의 APPROVE 운영조건 (e) 5조건 매트릭스 (§3)"

**Agent B verbatim 직접 read 결과** (Read tool, ADR-011 line 52~60):
```
- 대체 수단은 다음 4조건을 **모두** 충족할 때 기존 수단을 대체할 수 있다:
  | # | 조건 | 검증 방식 |
  |---|------|---------|
  | (a) | 동등 이상의 보안 결과 | 명시적 비교표 (수단 A 보장 ↔ 수단 B 보장) |
  | (b) | 격리 환경 PoC로 실증 | Docker isolation + 자동 검증 항목 |
  | (c) | ADR 권위로 명시 | 본 ADR 또는 후속 ADR |
  | (d) | 자동 회귀 검증 경로 확보 | CI/nightly 재실행 (R-6) |
```

**Agent B 확정 판단**:
- ADR-011 §2.1 원문 모법 = **(a)~(d) 4조건만**
- "(e) 합의 APPROVE" = **governance-preconditions §4.5 Exit 표 (line 455) 의 *운영조건*** 으로 별도 layer 에서 추가된 영역
- brief §3 헤더 (line 219) + §0.1 line 32 = 정확하게 "(a)~(d) + 운영조건 (e)" 로 표현
- brief §1.1 line 94 = "5조건 모법 — (a) ... (e)" 로 **모법 자격을 (e) 까지 확장 표현 — 내적 모순**

**왜 BLOCKING 인가**:
1. 권위 source 정확성 = 합의 brief 의 *기본 요건* (24 entry 답습 패턴 자체가 "선행 권위 verbatim 답습" 의무)
2. brief §3 매트릭스 본문에서는 5/5 trigger 0건 + 정확한 framing 사용 → §1.1 line 94 단축 표현이 정확 framing 과 *직접 충돌* → 본 brief 자체 *내적 정합성* 결함
3. 외부 LLM 응답 자격 검증 §7.3 #3 = "ADR-011 §2.1 (a)~(e) 5조건 답습 정확성" 표현 — **외부 LLM 이 본 brief framing 에 맞춰 (e) 까지 ADR-011 §2.1 모법으로 검증 시 codex / GPT 의 추론 input 자체가 권위 source 오인 risk** → cross-vendor 답습 의무 충돌

**요구 수정** (brief v1.1):
- (a) §1.1 line 94 "5조건 모법" → **"4조건 모법 (a)~(d) + 합의 APPROVE 운영조건 (e, governance-preconditions §4.5 Exit 표 추가)"** 로 verbatim 확장
- (b) §3 line 219 + §0.1 line 32 표현 유지 (정확)
- (c) §7.3 #3 = "ADR-011 §2.1 (a)~(d) 4조건 모법 + 운영조건 (e) 답습 정확성" 으로 framing 정합

---

## §2 권고 4건

### N-B-1 — 권위 chain 다중 source 손상 위험 trigger (4) 발화 처리 본문 추가

**위치**: brief §4.3 line 270

**현재 표현**:
> "(4) 권위 chain 다중 source 손상 위험 | ⚠️ **부분 발화 (R-S1 유형 잠재)** | §1.3 G4 §4.4 Layer 4 항목 = ADR-012 §2.3 line 182 verbatim 재확인 의무 (Layer 4 vs Layer 5 혼동 risk). 본 brief §10 P-? 자기진단 영역 명시. Reviewer 단독 verify 자격 (24 entry R-S1 답습 패턴)"

**권고**: R-B-1 격상 결과 (Agent B 검증 완료, **확정 divergence**) trigger (4) = **"발화"** 격상. brief §4.3 line 275 = "3/7 발화 + 1 부분 발화" → **"4/7 발화"** 격상 + trigger (4) row = "**발화 — ADR-012 §2.3 (4 layer) vs G4 §4.4.1 (5 layer) Layer 매트릭스 체계 divergence verbatim 확정 (Agent B 응답 §1 R-B-1)**" 추가.

### N-B-2 — sub-수단 결정 cycle (β) "동시 진행" 위험 자격 brief 본문 명시

**위치**: brief §1.3 line 112 (sub-수단 결정 vs 진입 합의 분리)

**현재 표현**:
> "본 (α) cycle = MVP-2 영역 *진입* 합의만, sub-수단 결정 = (β) 별도"

**위험**: 24 entry 답습 패턴은 "MVP-1 1.5차 보강 entry brief = 4 sub-수단 진입 + 채택 결정 통합" 형식 — 본 (α) cycle 가 *영역 진입* 한정으로 분리한 사유 = "25 조합 복잡도 + 부담 회피 + 단계별 cycle 답습 충실". 이는 **본 brief 의 의도적 분리 자체가 24 entry 와 *형태 변경* 영역** — 24 entry 답습 답습 동형 패턴 부족 risk.

**권고**: brief §1.3 line 112 + §11 등 (별도 행 또는 §10 P-? 추가) 에 "본 (α) = 영역 진입 한정 + (β) sub-수단 결정 분리 = 24 entry 答습 *형태 변경* 영역 → 본 변경 자격 발효 = 풀 3+1 합의 + 사용자 명시 의무 (현 cycle 의 사용자 명시 = '4번으로 진행' 직접 답습)" 본문 추가.

### N-B-3 — 헌법 8조 본질 충족 영역 분리 명시 보강

**위치**: brief 전체 (헌법 8조 직접 인용 부족)

**현재 표현**: brief §9.1 line 420~424 = "헌법 제8조 (보안)" cross-reference 한정. **본 brief 본문 (§1~§7) 에서 헌법 8조 본질 = "DB 평문 저장 차단" 답습 0**.

**위험**: governance-preconditions §4 line 424 = "GP-2 는 ADR-011 §2.3 운영 함의 #2 의 *보조* 역할. **DB INSERT 차단은 GP-1 의 책임이며, GP-2 는 송신/로그 경로만 다룸**. GP-2 단독으로 헌법 8조 본질 충족 시도 금지." → **본 brief 가 GP-2 = MVP-2 영역 진입 합의를 다루면서 헌법 8조 본질 (DB 평문 차단 = GP-1 책임) 분리 답습 본문 0** → 차후 (β) sub-수단 결정 cycle 가 GP-2 단독 헌법 8조 본질 충족 시도 위험.

**권고**: brief §2.1.1 또는 §0.4 (권위 한계) 에 "GP-2 = ADR-011 §2.3 운영 함의 #2 *보조* 역할 — 본 cycle 합의 = GP-2 단독 헌법 8조 본질 충족 영역 아님 (DB INSERT 차단 = GP-1 책임, 별도 영역). 본 brief 발효 후 후속 (β) sub-수단 결정 cycle 시점 헌법 8조 본질 *보조* 자격 한계 답습 의무" 본문 추가.

### N-B-4 — Provider Liquidity (헌법 5조-2) 답습 brief 본문 명시 보강

**위치**: brief §7.1 line 360 (외부 LLM 1+ cross-vendor 의무)

**현재 표현**: brief §7.1 #4 = "헌법 5조-2 Provider Liquidity (비협상) — cross-vendor 검증 의무 (OpenAI ≠ Anthropic)" cross-reference 한정.

**위험**: 본 brief = "MVP-2 영역 진입 합의" 영역, 사용자 메모리 7행 "Provider Liquidity 하드 요구" + "모델/구독/오케스트레이터 교체가 코드 변경 없이 가능해야 함" 헌법 5조-2 line 78 직접 인용 "LLM provider 선택은 코드가 아닌 설정 파일(YAML 등)에서만". **본 brief 의 sub-수단 후보 (R-1~R-5 / L-1~L-5) 가 Provider Liquidity 자격 평가 0** → 차후 (β) sub-수단 결정 cycle 시점 Provider Liquidity 위반 sub-수단 자동 채택 위험.

**권고**: brief §2.1.3 + §2.2.3 (sub-수단 후보 영역) 또는 §2.3.3 W-A 통합 영역에 "(β) sub-수단 결정 cycle 시점 = R-1~R-5 / L-1~L-5 각 sub-수단의 Provider Liquidity 자격 (헌법 5조-2 line 78 답습) 평가 의무 — 본 (α) cycle 영역 외 (후보 식별 한정), (β) cycle 입력 자료 명시 영역" 본문 추가.

---

## §3 NOTE 3건

### NT-B-1 — base64 / URL-encoded / 압축 evasion (R-5 영역) 분리 명시 정확

**위치**: brief §0.3 #8 + §2.1.4 + §2.3.2 + §5.1 RT-3

**평가**: brief 전반에서 R-5 (base64/URL/압축 evasion) = MVP-2/3 분리 영역 (G3-4 답습) 명시 정확. §0.3 #8 "외부 library 도입 trigger = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger" 와 cross-reference 정합.

**평가**: ✅ 정확. 추가 수정 의무 0.

### NT-B-2 — Layer 4 단독 진입 의미 부재 (P-5 답습) 정확

**위치**: brief §2.2.4 + §0.3 #25 + 51 brief §11 P-5

**평가**: G4 §4.4 Layer 4 = Layer 1+2 의존 영역. brief §2.2.4 "(γ) 분리 영역 결정 cycle (Layer 1+2 의존 영역 우선 vs Layer 4 동시 결정)" + §0.3 #25 "G4 §4.4 Layer 1/2/3/5 영역 진입 자동 결정 = 0건" 명시 정확. 51 brief §11 P-5 답습 충실.

**평가**: ✅ 정확. 추가 수정 의무 0.

### NT-B-3 — Reviewer 통합 단계 R-B-1 verify 의무

**위치**: brief §10 P-4 + 본 응답 §1 R-B-1

**평가**: Agent B 본 응답에서 **R-B-1 verbatim 직접 read 완료** (ADR-012 line 165~185 + provider-agnostic-memory-skill-design line 631~660). Reviewer 통합 단계 = Agent B 의 R-B-1 verify cross-confirm 의무 + Agent A / C 의 동일 영역 응답과 cross-check (Agent A / C 가 동일 verbatim read 수행 시 3/3 verify → BLOCKING 격상 확정). 24 entry R-S1 답습 패턴 = "Reviewer 단독 verify 자격" 영역, 본 cycle = 3 agent 병렬 verbatim verify 가능 + 본 Agent B 응답 자체 verbatim 직접 read 완료 → Reviewer 의 R-B-1 처리 = "verbatim 재확인 한정 (Agent A/B/C 3개 응답 답습 cross-check)" 한정 (별도 verbatim 재read 의무 없음).

**평가**: ✅ Reviewer 통합 단계 R-B-1 처리 부담 ≤ 일반 cross-check 수준.

---

## §4 6 검토 의무 항목별 평가

### §4.1 보안 영역 분리 정확성 — ✅ 정확 (수정 의무 0)

**평가 영역**: brief §0.3 27 금지 사항 + §6.2 10 금지 사항 망라성.

**Agent B 평가**:
- §0.3 27 항목 = 실 코드 / 본문 변경 / Implementation Evidence PASS / Operational Readiness / Hermes PMO 격상 / 외부 library 도입 / threshold 고정 / sub-수단 결정 / 분리 영역 결정 / MVP-1 PASS 재선언 / facade.py real / 다른 Layer 진입 / 다른 GP 영역 / branch protection / ADR 본문 / 헌법 본문 / roadmap 본문 / governance-preconditions 본문 / provider-agnostic-memory-skill-design 본문 / Tier-2/3 catalog / 외부 LLM 자동 호출 / 본 brief 영구화 = **27/27 망라**
- §6.2 10 항목 = (β) (γ) 실 구현 자동 진입 차단 + MVP-2 Implementation Evidence PASS 자동 선언 차단 + 외부 library 자동 도입 차단 + 다른 Layer / GP 영역 자동 진입 차단 + branch protection 자동 추가 차단 + ADR cross-reference 자동 변경 차단 + Tier-2/3 자동 확장 차단 = **10/10 망라**

**평가**: ✅ 망라성 충분 + 27/10 분리 정확. 추가 항목 의무 0.

### §4.2 엣지케이스 — ⚠️ 확정 risk 발견 (R-B-1 BLOCKING)

**평가 영역**: §2.1.4 GP-2 deferred + §2.2.4 G4 §4.4 Layer 4 deferred + L-5 trigger + Layer 1+2 의존 영역.

**Agent B 평가**:
- §2.1.4 R-5 (base64/URL/압축 evasion) 영역 분리 = ✅ 정확 (NT-B-1 답습)
- §2.2.4 외부 library (L-5) = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger 정확
- Layer 1+2 의존 영역 미진입 시 Layer 4 단독 진의미 부재 = ✅ 정확 (NT-B-2 답습)
- ⛔ **ADR-012 §2.3 Layer 4 vs G4 §4.4.1 Layer 4 = CONFIRMED divergence (R-B-1)** — Layer 매트릭스 체계 (4 vs 5 layer) 자체가 다른 영역. 이는 엣지케이스 영역에서 *권위 chain divergence* 로 분류 의무.

**평가**: ⚠️ 망라성은 대부분 충분하나 R-B-1 격상 의무 발견 → brief v1.1 흡수 의무.

### §4.3 문서 정합성 검증 — ⚠️ 2건 확정 (R-B-1 + R-B-2 BLOCKING)

**평가 영역**: brief §1.3 선차 변경 매트릭스 + §3 ADR-011 5조건 매트릭스 + G4 §4.4 Layer 4 정의 답습 + ADR-012 §2.3 vs §2.8 + governance-preconditions §4.4/§4.5.

**Agent B 평가**:
- ADR-011 §2.1 (a)~(d) 4조건 답습 *원문 검증* = ⛔ **R-B-2 BLOCKING (브리프 §1.1 line 94 표현 부정확)**
- G4 §4.4 Layer 4 정의 답습 = ✅ verbatim 일치 (G4 §4.4.1 line 649~653 = "Layer 4 — CI 회귀 검증 (MANDATORY)")
- ADR-012 §2.3 line 165~182 vs §2.8 line 266~272 Layer numbering 비교 = ⛔ **R-B-1 CONFIRMED divergence (ADR-012 §2.3 4 layer 체계 vs §2.8 5 layer 강제 — §2.8 line 268~272 verbatim = "Layer 1: Hash chain / Layer 2: Git append-only / Layer 3: pre-commit hook / Layer 4: CI 회귀 검증 / Layer 5: External anchor" — §2.8 자체는 5 layer 체계 + Layer 4 = CI 회귀 검증)** — **ADR-012 §2.3 (4 layer) vs ADR-012 §2.8 (5 layer) 내부 충돌 발견** + ADR-012 §2.3 (4 layer) vs G4 §4.4.1 (5 layer) 충돌 = 권위 chain 다중 source 손상 R-B-1 격상 의무 *더 강화* (ADR-012 자체 내 §2.3 vs §2.8 충돌 + G4 §4.4.1 vs ADR-012 §2.3 충돌 = 2중 divergence)
- governance-preconditions §4.4 Entry / §4.5 Exit 답습 = ✅ 정확 (Entry 2/3 + Exit 2.5/5 답습 정합)

**평가**: ⚠️ R-B-1 + R-B-2 BLOCKING 격상 의무 + ADR-012 §2.3 (4 layer) vs §2.8 (5 layer) 내부 충돌 추가 발견 → 정정 cycle 영역 = ADR-012 §2.3 vs §2.8 통일 (Agent B 권고 = ADR-012 §2.3 를 5 layer 체계로 정합 — §2.8 + G4 §4.4.1 답습).

### §4.4 헌법 답습 — ⚠️ 본문 답습 부족 (N-B-3 + N-B-4 권고)

**평가 영역**: GP-2 송신 redaction = 헌법 8조 본질 (DB 평문 차단) 보조 역할 / 외부 LLM 1+ cross-vendor = Provider Liquidity 답습.

**Agent B 평가**:
- GP-2 = 헌법 8조 본질 보조 영역 (DB INSERT 차단 = GP-1 책임) = brief 본문 답습 부족 → **N-B-3 권고**
- 외부 LLM 1+ cross-vendor = Provider Liquidity (헌법 5조-2) = brief §7.1 #4 cross-reference 한정, sub-수단 후보 Provider Liquidity 자격 평가 0 → **N-B-4 권고**
- sub-수단 결정 분리 = 큰 결정 분리 답습 = ✅ 정확 (§1.3 + §2.1.3 + §2.2.3 다층 답습)

**평가**: 본문 답습 보강 의무 (N-B-3 + N-B-4) — BLOCKING 아님, 권고 영역.

### §4.5 R-S1 잠재 risk 처리 정확성 — ⛔ 격상 의무 (R-B-1)

**평가 영역**: brief §10 P-4 (ADR-012 §2.3 line 182 verbatim 재확인 + Layer 4 vs Layer 5 혼동 + R-S1 답습 패턴 + 권위 chain 다중 source 손상).

**Agent B 평가**:
- ADR-012 §2.3 line 182 verbatim 재확인 = Agent B 본 응답에서 *완료* → "잠재 risk" → **확정 divergence**
- G4 §4.4.1 line 649 verbatim 재확인 = Agent B 본 응답에서 *완료* → ADR-012 §2.3 와 충돌 확인
- 두 source "Layer 4" 정의 충돌 = ADR-012 §2.3 (4 layer 체계, Layer 4 = External anchor) vs G4 §4.4.1 (5 layer 체계, Layer 4 = CI 회귀 검증) = **체계 divergence** (단순 이름 충돌 아님)
- brief "잠재 risk" 표현 vs **CONFIRMED divergence** 격상 자격 = ⛔ **격상 의무 (R-B-1)**
- 권위 chain 다중 source 손상 위험 자격 = ⛔ **trigger (4) 발화 격상 의무 (N-B-1)**

**평가**: ⛔ 격상 의무 — brief v1.1 흡수 의무 (R-B-1 + N-B-1).

### §4.6 메타 편향 회피 — ✅ 망라성 충분 (7 항목, 1 추가 권고)

**평가 영역**: brief §10 자기진단 7 항목 (P-1 ~ P-7) 망라성.

**Agent B 평가**:
- P-1 (MVP-2 진입 편향) = ✅ §0.3 + §0.4 + §6.2 다층 답습
- P-2 (sub-수단 (β) 무단 침입) = ✅ §0.3 #11 #12 + §1.3 + §2.1.3 + §2.2.3 다층 답습
- P-3 (51 entry audit cascade) = ✅ 51 brief 자체 Reviewer-only 단축 합의 5/5 trigger 0건 + 14/14 verbatim 답습
- P-4 (R-S1 잠재 risk) = ⛔ **격상 의무 (R-B-1, 잠재 → 확정)**
- P-5 (24 entry 답습 동형 패턴 vs 본 cycle 특수성) = ⚠️ N-B-2 권고 추가 (sub-수단 결정 분리 = 형태 변경 자격 명시 의무)
- P-6 (W-A 통합 권고 사용자 영역 침입) = ✅ §2.3.2 단점 명시 + 51 brief §4.2 답습 + §6.2 #1 다층 답습
- P-7 (두 영역 통합 = 각 영역 특성 무시) = ✅ §2.1 + §2.2 별도 분석 + §3 별도 컬럼 + §4.2 발효 시점 합의 형태 별도 명시

**추가 자기진단 항목 권고** (Agent B):
- **P-8 후보**: 본 brief 작성자 (Claude Opus 4.7) 가 self-reading 시점 verbatim 재확인 미흡 자격 자체가 P-4 자기진단 답습 부족 → brief v1.1 흡수 시 P-4 처리 본문 = "Agent B 응답 §1 R-B-1 직접 답습 + 확정 divergence 격상 + 정정 cycle 영역 명시" 추가 + P-8 자기진단 추가 "Claude self-reading verbatim 재확인 의무 강제화 (3+1 합의 cycle 의무 의 *최저선* )"

**평가**: ✅ 7 항목 망라성 충분. P-4 격상 + P-8 추가 권고 영역.

---

## §5 자기 편향 자기진단 (Agent B)

| # | 잠재 편향 | Agent B 처리 |
|---|--------|----------|
| **B-1** | Agent B 가 brief 작성자 (Claude Opus 4.7, 본 cycle) 와 동일 LLM 인 경우 자기 우호 결론 위험 | 본 응답 §1 R-B-1 + R-B-2 = **BLOCKING 격상 결과** → 자기 우호 결론 회피 evidence. brief §10 P-4 = "잠재 risk" 분류를 Agent B 가 **확정 divergence** 로 격상 + brief §1.1 line 94 framing 정확성을 R-B-2 BLOCKING 로 격상 = 자기 비판 충실 |
| **B-2** | 24 entry R-S1 답습 동형 패턴 적용 시 본 cycle 특수성 무시 위험 | 24 entry R-S1 = "Reviewer 단독 verify 자격" 영역 / 본 cycle = 3 agent 병렬 verify 가능 + brief 자체 P-4 자기진단 명시 영역 → R-B-1 격상 자격 = 24 entry R-S1 답습 *수준 이상* (verbatim 직접 read 완료 + 확정 divergence + 7 trigger (4) 발화 격상) |
| **B-3** | Agent B 가 BLOCKING 격상 위해 R-B-1 / R-B-2 *과대 평가* 위험 | R-B-1 = verbatim 직접 read 결과 (ADR-012 line 165~185 + provider-agnostic-memory-skill-design line 631~660) — Reviewer 통합 시점 cross-confirm 의무 영역. R-B-2 = ADR-011 line 52~60 verbatim 직접 read 결과 — 권위 source 정확성 차원. *과대 평가* 위험 = Reviewer cross-check 영역 |
| **B-4** | Agent B 가 brief v1 → v1.1 REVISE 판정으로 본 cycle 합의 발효 *지연* 위험 | v1.1 1pass 흡수 = brief 본문 수정 한정 (BLOCKING 2 + 권고 4 흡수) + Agent A / C 응답 통합 + Reviewer 합의 → 본 cycle 발효 timeline 영향 최소 (1 entry 추가 cycle). MVP-2 영역 진입 권한 발효 자체는 brief v1.1 후 발효 가능. R-B-1 별도 정정 cycle = 본 cycle 발효 후 사용자 명시 진입 영역 (block 영역 아님) |
| **B-5** | Agent B 가 권위 chain 답습 정확성을 본 cycle 핵심 검토 영역으로 집중하여 다른 검토 의무 (사용자 영역 / Provider Liquidity / 헌법 8조) 답습 부족 위험 | §4.4 헌법 답습 = N-B-3 + N-B-4 권고 별도 명시 + §4.1 보안 영역 분리 + §4.2 엣지케이스 + §4.6 메타 편향 = 망라 검토 완료. 권위 chain 검토 집중 ≠ 다른 검토 부족 |

---

## §6 발효 자격 권고

본 Agent B 응답 = 풀 3+1 합의 (52 entry) Reviewer 통합 입력 자료 한정.

**판정**: ⚠️ **REVISE** (BLOCKING 2 + 권고 4 + NOTE 3).

**brief v1.1 흡수 의무 영역**:
- R-B-1 흡수 (§1.3 + §4.3 + §10 P-4 + §9.5 본문 수정)
- R-B-2 흡수 (§1.1 line 94 framing 정정)
- N-B-1 ~ N-B-4 흡수 (권고 영역, 본문 보강)

**brief v1.1 흡수 후 Reviewer 통합 단계 진입 적격**. Reviewer 통합 시:
- Agent A / C 응답과 cross-check + R-B-1 verbatim verify (Agent B 본 응답 §1 R-B-1 read 자료 답습)
- 합의 형태 = 풀 3+1 + 외부 LLM 1+ 외부 LLM (codex) 응답 입력 + 사용자 명시 결정 3 조건 모두 충족 시점 발효
- 발효 효과 = MVP-2 영역 진입 권한 발효 + (β) (γ) sub-cycle 진입 자격 발효 + Rollback Trigger / Evidence 본문 채택 + ADR-012 §2.3 vs §2.8 vs G4 §4.4.1 Layer 매트릭스 통일 정정 cycle 사용자 명시 진입 영역 (별도 cycle, 본 합의 발효 의 block 영역 아님)

---

**Agent B 응답 v1 끝.**

**다음 단계**: Reviewer 통합 단계 → Agent A / C 응답 + 외부 LLM (codex) 응답 + 본 Agent B 응답 cross-check → 합의 보고서 작성 → brief v1.1 1pass 흡수 → 사용자 명시 결정 → 본 cycle 합의 발효 → SESSION + INDEX commit + push.
