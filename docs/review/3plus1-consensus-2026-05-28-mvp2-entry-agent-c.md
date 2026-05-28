# MVP-2 진입 합의 entry brief — 풀 3+1 합의 Agent C (대안 탐색가) 응답

> **본 응답은 추론적 검증(권고) 한정이며 — 본 응답의 어떤 §도 그 자체로 (i) 실 runtime code / CI workflow / hook 구현 / 변경, (ii) MVP-2 진입 발효, (iii) Implementation Evidence PASS / Operational Readiness PASS 발효, (iv) ADR 본문 갱신, (v) 헌법 본문 갱신, (vi) roadmap-mvp1 본문 갱신, (vii) governance-preconditions / provider-agnostic-memory-skill-design / ADR-012 본문 갱신, (viii) GP-2 / G4 §4.4 sub-수단 *결정* (R-1~R-5 / L-1~L-5), (ix) threshold *고정*, (x) Tier-2/3 catalog 자동 확장, (xi) Hermes PMO 격상, (xii) MVP-1 PASS 재선언, (xiii) `adapters/llm/facade.py` placeholder → real, (xiv) 외부 library (`pyjcs` / `rfc8785`) 도입 결정, (xv) MVP-2 진입 자동 진입 — 어떤 행위도 자동 발생시키지 않는다. 본 응답 = Agent C (대안 탐색가) 병렬 독립 평가 한정, 풀 3+1 합의 Reviewer 통합 입력 자료.**

---

**작성일**: 2026-05-28
**검토자**: Agent C — 대안 탐색가 (병렬 독립 평가)
**검토 대상**: `docs/phase0/mvp2-entry-brief.md` (v1, 480줄, 52 entry MVP-2 진입 합의 entry brief)
**관점**: "더 나은 방법이 있는가?" — 대안 기술, 트레이드오프, 영역 분리/통합 대안 탐색

---

## 0. 직접 read 자료 path 목록

본 응답 작성 시점 *직접 read* 완료한 자료 (병렬 독립 평가 evidence):

1. `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-entry-brief.md` (480 line — primary 검토 대상)
2. `/home/delangi/문서/project/category/AI_development_tool/docs/phase0/mvp2-entry-eligibility-audit-brief.md` (372 line — 51 entry audit brief, 본 brief 의 직접 입력 자료)
3. `/home/delangi/문서/project/category/AI_development_tool/docs/review/3plus1-consensus-2026-05-28-mvp2-entry-eligibility-audit.md` (184 line — 51 entry 합의)
4. `/home/delangi/문서/project/category/AI_development_tool/docs/architecture/governance-preconditions.md` §4 (line 425~466 — GP-2 정의 + Entry §4.4 + Exit §4.5 + 산출 §4.6 + 의존 ADR §4.7)
5. `/home/delangi/문서/project/category/AI_development_tool/docs/architecture/provider-agnostic-memory-skill-design.md` §4.4 (line 615~700 — Layer 1~5 정의)
6. `/home/delangi/문서/project/category/AI_development_tool/docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (event enum 18~25) + §2.3 (Layer 1~4 다층 강제, line 163~185) + §2.5 (RFC 8785 JCS)
7. `/home/delangi/문서/project/category/AI_development_tool/docs/architecture/implementation-runtime-roadmap.md` §4 (G4 7 영역) + §5 (종합 우선순위 매트릭스) + §5.3 (그룹 A~I) + §5.4 (그룹별 합의 형태 권고)
8. `/home/delangi/문서/project/category/AI_development_tool/docs/architecture/implementation-runtime-roadmap-mvp1.md` §1.2 (3-layer PASS) + §1.3 (GP-2 = MVP-2 분리 사유)

⚠️ codex 응답 + Agent A/B 응답 = *참조 0건* (병렬 독립 평가 의무 답습, 편향 방지). Reviewer 통합 시 cross-check.

---

## §0 총평

**판정**: **APPROVE WITH CONDITIONS** — 본 brief v1 = 대안 탐색 관점에서 *진입 자격* 권고는 충분히 정당 (R-S1 식별 + 영역 통합 W-A 권고 + sub-수단 후보 식별 합리적). 단, **2 BLOCKING + 6 권고 흡수 후 v1.1 진입 자격 발효 권고**.

- **BLOCKING**: 2건 (R-C-1, R-C-2 — 대안 영역 부족 / 정당화 부족)
- **권고**: 6건 (N-C-1 ~ N-C-6 — 대안 매트릭스 보강)
- **NOTE**: 3건 (N-O-1 ~ N-O-3 — 후속 cycle 사용자 영역)

Agent C 한 줄 결론: **두 영역 통합 W-A 권고 정당 / sub-수단 분리 (β) 정당 — 그러나 brief 가 "대안을 *비교* 후 W-A 채택" 형식이 아닌 "W-A 답습 후 대안 명시 부족" 형식 → BLOCKING. 본 v1 흡수 후 v1.1 = 풀 3+1 합의 발효 자격 충분.**

---

## §1 BLOCKING (R-C-x)

### R-C-1 [BLOCKING — 대안 매트릭스 부족]: 두 영역 통합 R-6 workflow 확장 (W-A) 권고가 W-B 단 1개 대안만 비교 (W-C / W-D 추가 대안 미커버)

**위치**: brief §2.3 (line 196~216) + §1.3 line 111

**문제**:
- brief §2.3.1~§2.3.3 = "W-A 단일 R-6 확장" 채택 정당화 답습
- 51 entry audit brief §4.2 = W-A (통합) vs W-B (분리 2 workflow) 2 대안 비교
- brief §1.3 line 111 = "51 entry audit brief §4 W-A 권고 직접 답습" 그대로 — **W-A vs W-B 외 추가 대안 0건**

**누락된 대안** (Agent C 식별):
- **W-C: 단계 분리 (GP-2 우선 진입 → G4 §4.4 Layer 4 후속 진입)** — 시간 분리. GP-2 Exit (a)/(c) 이미 충족 (2.5/5) vs G4 §4.4 Layer 4 (c) 만 충족 (1/5) — GP-2 진입 부담 << G4 §4.4 Layer 4 진입 부담. 우선 GP-2 진입 후 G4 §4.4 Layer 4 별도 cycle 대안.
- **W-D: 그룹 D + 그룹 C 별도 progression** (roadmap.md §5.3 답습) — roadmap.md §5.3 line 181~182 = "그룹 D (Order 4+5) = G2 GP-3 + G2 GP-2 / 그룹 C (Order 3 tie) = G4 hash chain + JCS + Round-trip PoC" 별도 그룹 명시. 본 brief = 그룹 D 잔존 (GP-2) + 그룹 C 부분 (G4 §4.4 Layer 4) 통합 진행 → **roadmap.md §5.3 9 그룹 구조와의 일치성 검증 부족**.
- **W-E: pre-commit hook 활용** — R-6 workflow 외 pre-commit hook 영역 = GP-2 log canary inject 일부 + G4 hash chain verify 일부 = pre-commit 단계 검증 대안 (Layer 1 ≈ 500ms 답습, CLAUDE.md §2 표). 51 audit brief 미커버 영역.

**요청**: brief §2.3 에 W-C / W-D / W-E 3 대안 추가 비교 매트릭스 (장점/단점/ceremony-inflation/실패 영역 식별/branch protection contexts 부담/운영 복잡도) 명시 + W-A 채택 *비교 결과 정당화* (단순 51 audit brief 답습이 아닌 본 cycle 독립 평가).

**근거 권위**: CLAUDE.md §3 "Agent C (대안 탐색가) 핵심 질문: 더 나은 방법이 있는가? 대안 기술, 트레이드오프" + roadmap.md §5.3 9 그룹 구조 답습 의무.

---

### R-C-2 [BLOCKING — 합의 형태 격상 정당화 부족]: roadmap.md §5.4 그룹 C/D = "단축 합의 + PoC evidence" 권고 vs 본 cycle = "풀 3+1 + 외부 LLM 1+" 격상 차이가 §1.3 선차 변경 매트릭스 missing

**위치**: brief §1.3 선차 변경 매트릭스 (line 107~114) + §4.1 (line 243~252)

**문제**:
- roadmap.md §5.4 line 192~200 = 그룹 C (G4 §4.4 Layer 4 영역 포함) = "단축 합의 + PoC evidence" / 그룹 D (GP-2 포함) = "단축 합의 + PoC evidence" — **단축 합의 권고 명시**
- 본 brief = 두 영역 모두 "풀 3+1 + 외부 LLM 1+" 권고 (§4.1 + §4.2) — **격상**
- brief §1.3 선차 변경 매트릭스 (line 107~114) = GP-2 시점 분리 + G4 Layer 4 진입 자격 + W-A 통합 + sub-수단 분리 4 항목 다룸 — **roadmap.md §5.4 격상 차이는 0건 명시**
- brief §4.1 정당화 5건 = 51 audit brief / roadmap-mvp1 §1.3 / 32 entry / 24 entry / ADR-011 §2.1 (e) — **roadmap.md §5.4 단축 합의 권고와의 직접 대비 정당화 부재**

**위험**: 격상 사유가 본 brief 내에서 명시 정당화되지 않으면 후속 cycle 에서 "왜 그룹 C/D = 단축 합의에서 격상?" 질문 발생 시 답습 권위 부재.

**요청**: brief §1.3 선차 변경 매트릭스에 항목 5 추가 — "선행 권위 = roadmap.md §5.4 그룹 C/D 단축 합의 / 본 cycle 결정 = 풀 3+1 + 외부 LLM 1+ 격상 / 권위 정당성 = MVP-2 = MVP-1 동격 Layer 2 Implementation Evidence PASS *영역 진입* 결정 (32 entry 답습) + Implementation Evidence PASS *발효* (각 그룹 별 PoC 후) ≠ *영역 진입* 결정 (큰 영역, 풀 3+1 + 외부 LLM 1+ 자격) 분리". 또는 본 cycle = 단축 합의 권위 활용 (대안 — roadmap.md §5.4 단축 합의 권고 답습 정확 형식).

**근거 권위**: roadmap.md §5.4 line 192~200 + ADR-011 §2.1 (e) "합의 APPROVE" 단축 vs 풀 3+1 명시.

---

## §2 권고 (N-C-x)

### N-C-1 [권고 — sub-수단 (β) 분리 정당화 보강]: 24 entry "sub-수단 채택 결정 통합" vs 본 (α) "sub-수단 결정 (β) 분리" 차이의 정당화 충분성 — 부분 통합 대안 1+ 명시 필요

**위치**: brief §1.3 line 112 + §10 P-5 (line 472)

**문제**:
- 24 entry MVP-1 1.5차 보강 entry brief = "sub-수단 진입 자격 + sub-수단 채택 결정 통합" (한 entry brief 내 4 sub-수단 결정)
- 본 (α) = "영역 진입 자격만, sub-수단 결정 = (β) 별도"
- brief §1.3 line 112 정당화: "25 조합 (R-1~R-5 × L-1~L-5) 가 24 entry 4 sub-수단 보다 복잡 + 단계별 cycle 답습"
- **그러나 25 조합 = 5 (R) × 5 (L) = 독립 차원** — 실제 매트릭스 조합이 아닌 *각 영역별 5 후보 中 1 선택*. GP-2 = 5 선택지 / G4 §4.4 Layer 4 = 5 선택지 = 총 10 선택 (조합 ≠ 매트릭스)

**대안 — Agent C 식별**:
- **부분 통합 대안 (P-1)**: 본 (α) cycle 에서 sub-수단 *기본 권고* (GP-2 = R-4, G4 §4.4 Layer 4 = L-4) 만 *확정* (51 brief §2.3 + §3.4 권고 답습), 세부 catalog 결정 = (β) 별도
- **단계 분리 대안 (P-2)**: GP-2 sub-수단 결정 = 본 (α) cycle 흡수 (5 선택지 = 단순), G4 §4.4 Layer 4 sub-수단 결정 = (β) 별도 cycle (외부 library 트리거 ADR-012 §2.1 답습 영역 분리)

**요청**: brief §1.3 line 112 또는 §10 P-5 에 위 2 대안 (P-1 / P-2) 명시 + 본 brief 채택 (sub-수단 결정 전면 분리) 의 비교 정당화 보강.

**근거 권위**: 24 entry entry brief 답습 동형 패턴 (brief §10 P-5 자기진단 영역 답습) + 5/5 입력 권고 답습 (51 audit brief §2.3 + §3.4 답습).

---

### N-C-2 [권고 — γ 분리 영역 결정 대안 매트릭스 미커버]: brief §1.3 / §2.2 / §4.2 = (γ) "Layer 1+2 의존 영역 우선 vs Layer 4 동시" 2 대안만 명시, 4 대안 비교 매트릭스 부재

**위치**: brief §2.2.3 (line 184) + §2.2.4 (line 191~192) + §8.1 (line 405~408)

**문제**:
- brief 전체에서 (γ) 분리 영역 결정 = "Layer 1+2 의존 영역 우선 진입 vs Layer 4 동시 진입" 2 대안만 명시
- ADR-012 §2.3 + G4 §4.4.1 답습 = Layer 1 (Hash Chain MANDATORY) + Layer 2 (Git append-only MANDATORY) + Layer 4 (CI 회귀 검증 MANDATORY) = 3 MANDATORY layer

**Agent C 식별 4 대안**:
- **(γ-a)** Layer 1+2 의존 영역 우선 진입 → Layer 4 추가 (단계적, 안전) — brief 명시 영역
- **(γ-b)** Layer 4 단독 진입 (Layer 1+2 = 의존 영역 자동 동시 진입) — Layer 4 검증 대상 = Layer 1+2 이므로 자동 의존
- **(γ-c)** Layer 1+2+4 동시 진입 (defense-in-depth 답습) — 51 audit brief §3.1 답습 "Layer 1+2+4 MANDATORY 통합" 시점
- **(γ-d)** Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle 분리 (현 brief framing) — brief 명시 영역

**평가**:
- (γ-a) = 안전, 단계적, 의존 명확. 단점 = 시점 분리로 운영 부담 ↑
- (γ-b) = 효율, 단점 = Layer 1+2 = "의존 영역 자동 진입" 형식 명시 부재 시 권위 chain 위험
- (γ-c) = 가장 견고. 단점 = 본 cycle 범위 격상 (3 영역 동시), 51 audit brief Entry 자격 매트릭스 3/8 답습 부담
- (γ-d) = 본 brief 답습. 장점 = scope 분리 명확, 단점 = 후속 사용자 명시 cycle 부담 ↑

**요청**: brief §2.2.3 또는 §2.2.4 에 (γ-a/b/c/d) 4 대안 매트릭스 + ADR-012 §2.3 다층 강제 답습 정합성 평가 추가. 본 (α) 합의 발효 시점 = "(γ) 별도 cycle" 분리 정당화 *(별도 cycle 진입 시 4 대안 비교 의무)*.

**근거 권위**: ADR-012 §2.3 (line 163~185) + provider-agnostic-memory-skill-design §4.4.1 (line 629~660) Layer 1~5 정의 다층 강제.

---

### N-C-3 [권고 — L-2/L-5 vs L-1/L-4 외부 library 도입 trade-off 매트릭스]: brief §2.2.4 + §6.2 #5 외부 library 도입 = (β) 별도 cycle 명시만, *trade-off 평가* 0건

**위치**: brief §2.2.4 (line 193) + §6.2 #5 (line 344)

**문제**:
- brief §2.2.4 + §6.2 #5 = "L-5 외부 library 도입 = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger, 별도 cycle" 명시만
- L-1 (stdlib `json.dumps(sort_keys=True, separators=(",",":"))`) vs L-2 (`pyjcs` / `rfc8785`) **동등성** trade-off 평가 0건
- ADR-012 §2.5 (line 213~218) + G4 §4.4.2 (line 662~677) = "test corpus 의무: `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함 + 입력 → 자체 canonical → JCS reference output 비교 + 불일치 시 BLOCK"

**Agent C 평가**:
- **L-1 stdlib 단독 + test corpus** = MVP 권고 (brief 답습 정확). 단점 = 자체 RFC 8785 reference test corpus 검증 충분성 검증 부담 → test corpus 정합성 자체가 별도 검증 영역. 장점 = 의존성 0건 (Provider Liquidity Layer 4 답습)
- **L-2 외부 library 정식** = 정식 채택 시점 권고. 단점 = ADR-012 §2.1 R-2 / R-4.1 PoC 자동 재실행 trigger + 의존성 추가 (Provider Liquidity Layer 4 위반 risk) + Python `pyjcs` vs `rfc8785` 라이브러리 선택 자체가 또 다른 sub-결정. 장점 = RFC 8785 정확성 보장 + maintenance 부담 ↓

**Agent C 식별 대안 — L-1.5**: stdlib + 자체 RFC 8785 reference test corpus + 매년 1회 외부 library 동등성 cross-check (운영 부담 ↓) — MVP-2 ~ MVP-3 단계 사용 후 정식 L-2 전환 정당성 evidence 누적.

**요청**: brief §2.2.4 또는 별도 §2.2.5 신설 → L-1 / L-2 / L-1.5 trade-off 매트릭스 (의존성 / RFC 8785 정확성 / 운영 부담 / Provider Liquidity 정합성) + 본 (α) 합의 발효 시 *(β) cycle 진입 시 L-1 권고* 정당화 명시.

**근거 권위**: ADR-012 §2.5 (RFC 8785 JCS Primary + Fallback 동등성) + provider-agnostic-memory-skill-design §4.4.2 + 헌법 5조-2 Provider Liquidity.

---

### N-C-4 [권고 — 외부 LLM cross-vendor 1+ vs 2+ 격상 권고 검증 부족]: brief §4.1 + §7.1 = "외부 LLM 1+ (cross-vendor)" 권고만, 2+ 격상 검증 부재

**위치**: brief §4.1 (line 245~252) + §7.1 (line 357~362)

**문제**:
- brief 전체 "외부 LLM 1+ (cross-vendor 의무)" 권고 5건 명시 (§4.1 / §4.2 / §4.3 / §6.2 #10 / §7.1)
- 32 entry MVP-1 Implementation Evidence PASS 발효 합의 = 외부 LLM 1+ (codex via tmux) 답습 — brief 정확
- **그러나** ADR-012 §2.3 P-2 (보강) = "외부 LLM 2건" 답습 (G4 §4.4 line 623 "PR-2 풀 3+1 + 외부 LLM 2건 APPROVE WITH CONDITIONS") 답습 — **G4 영역 특화 권위에서는 2+ 답습 패턴 존재**

**대안**:
- **본 (α) cycle = 외부 LLM 1+ (cross-vendor)** = 본 brief 답습 (정합)
- **격상 대안 — 외부 LLM 2+ (cross-vendor 2-way)**: G4 §4.4 Layer 4 영역이 ADR-012 §2.3 답습 (외부 LLM 2건) 이고 본 cycle = 두 영역 통합 (GP-2 + G4) 이므로 G4 영역 답습 우선 시 2+ 권고. 예: codex (OpenAI) + Gemini (Google) cross-vendor 2-way → 더 견고
- **trade-off**: 1+ = ceremony-inflation 회피 + 사용자 부담 ↓ (24 entry 답습) / 2+ = G4 답습 충실성 + Provider Liquidity 답습 cross-vendor 2-way 권위 강화

**요청**: brief §4.1 또는 §7.1 에 "외부 LLM 1+ vs 2+ trade-off + 본 cycle 1+ 채택 정당화 (24 entry / 32 entry 답습 우선)" 명시. 또는 *(별도 권고)* 2+ 격상 사용자 영역 carry-over.

**근거 권위**: G4 §4.4 line 623 + 헌법 5조-2 Provider Liquidity (cross-vendor 검증 의무) + 24/32 entry 답습 패턴.

---

### N-C-5 [권고 — Implementation Evidence PASS 발효 시점 합의 형태 강화 권고]: 32 entry "풀 3+1 + 외부 LLM 1+" 답습 vs 본 cycle 두 영역 통합 = "풀 3+1 + 외부 LLM 2+" 격상 검토

**위치**: brief §4.2 (line 256~259)

**문제**:
- brief §4.2 = GP-2 / G4 §4.4 Layer 4 발효 시점 합의 형태 = "풀 3+1 + 외부 LLM 1+ + 사용자 명시" (32 entry 답습)
- 32 entry MVP-1 PASS 발효 = GP-3 + GP-5 통합 (2 영역) = 외부 LLM 1+ — brief 답습 정확
- **본 cycle = GP-2 + G4 §4.4 Layer 4 통합 (2 영역) + R-S1 잠재 risk** — 32 entry 동격

**Agent C 평가**:
- 32 entry 답습 시 = 외부 LLM 1+ (정합)
- R-S1 잠재 risk (ADR-012 §2.3 Layer 4 vs Layer 5 혼동, brief §1.3 P-4) 가 발효 시점에 미해소 시 → 외부 LLM 2+ 격상 필요 가능성
- **대안 — 발효 시점 *조건부* 격상**: R-S1 정정 (cross-reference 정정 cycle 별도) 미완료 시 발효 합의 = 외부 LLM 2+ 격상 / R-S1 정정 완료 시 = 외부 LLM 1+ 답습

**요청**: brief §4.2 또는 §5.2 E-9 에 "Implementation Evidence PASS 발효 시점 = 외부 LLM 1+ 답습 (32 entry) + R-S1 정정 cycle 완료 사전조건 명시 (미완료 시 외부 LLM 2+ 격상 권고)" 추가.

**근거 권위**: 32 entry MVP-1 PASS 발효 합의 + brief §1.3 P-4 R-S1 잠재 risk 명시 + ADR-012 §2.3 답습.

---

### N-C-6 [권고 — JSONL event enum 후보 (§5.3) trade-off 대안 명시]: brief §5.3 = 3 신규 enum 후보 명시, 명명 규칙 / scope 대안 평가 0건

**위치**: brief §5.3 (line 314~324)

**문제**:
- brief §5.3 = 3 신규 enum 후보 (`gp2_redaction_layer1_implementation` / `g4_ledger_chain_verify_layer4_implementation` / `r6_workflow_extension_mvp2`)
- ADR-012 §2.2 답습 (line 150~156) = MVP-1 신규 enum 패턴 (`secret_scan_layer1_implementation` / `docker_secret_isolation_layer1_implementation` / `provider_adapter_enforcement_layer1_static` / `pc3_ar1_integration_implementation` / `g3_7_workflow_hygiene_implementation`) — **"layer1_implementation" / "implementation" suffix 답습 패턴 일치**
- 그러나 본 §5.3 = `g4_ledger_chain_verify_layer4_implementation` — "layer4" 명시 = R-S1 잠재 risk (ADR-012 §2.3 Layer 4 = External anchor vs G4 §4.4.1 Layer 4 = CI 회귀 검증 혼동 가능성 — enum 명명에 내재화 시 cross-reference 위험)

**대안**:
- **명명 대안 (E-1)**: `g4_ledger_chain_verify_layer4_implementation` → `g4_ledger_chain_ci_regression_implementation` (Layer 번호 직접 사용 회피, semantic 명명) — R-S1 회피
- **명명 대안 (E-2)**: `g4_ledger_chain_verify_layer4_g4_implementation` (Layer 번호 + 권위 source 명시 G4) — R-S1 명시 회피
- **scope 대안 (S-1)**: 본 cycle 합의 발효 시 enum 후보 = 사용자 영역 carry-over (ADR-012 §2.2 cross-reference 갱신 별도 commit 영역, brief §5.3 답습) — *결정 0* 영구 분리

**요청**: brief §5.3 에 enum 명명 대안 (E-1 / E-2) + scope 대안 (S-1) 명시 + 본 cycle = 결정 0 영구 분리 (사용자 영역 carry-over) 답습 강화. R-S1 회피 명명 대안 (E-1) 권고.

**근거 권위**: ADR-012 §2.2 enum 명명 패턴 + brief §1.3 P-4 R-S1 잠재 risk + brief §0.3 #19 "ADR 본문 갱신 0건" 답습.

---

## §3 NOTE (N-O-x)

### N-O-1 [NOTE]: brief §10 P-4 R-S1 잠재 risk 처리가 "Reviewer 단독 verify 자격" 으로 명시되어 있으나, 실제 정정 cycle 진입 trigger 검증 필요

**위치**: brief §10 P-4 (line 471)

**관찰**:
- brief §10 P-4 = "ADR-012 §2.3 line 182 verbatim 재확인 부족 — Layer 4 vs Layer 5 혼동 위험"
- Agent C 직접 verbatim 확인 (본 응답 §0 #6 read evidence): ADR-012 §2.3 line 182 = "Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)" / G4 §4.4.1 line 649 = "Layer 4 — CI 회귀 검증 (MANDATORY)" — **권위 chain 다중 source 손상 확정** (서로 다른 정의 같은 Layer 번호)
- ADR-012 §2.3 = 4 Layer (1: Hash Chain / 2: Git append-only / 3: Signed commit / 4: External anchor)
- G4 §4.4.1 = 5 Layer (1: Hash Chain / 2: Git append-only / 3: Signed commit / **4: CI 회귀 검증** [신규] / 5: External anchor)
- → G4 §4.4.1 = ADR-012 §2.3 의 Layer 4 (External anchor) 를 Layer 5 로 밀고, Layer 4 슬롯에 신규 "CI 회귀 검증" 삽입 구조

**평가**: brief §1.3 P-4 + §10 P-4 자기진단 정확 — Reviewer 단독 verify 자격 확정 + §9.5 별도 cycle (R-S1 정정 영역) 영역 carry-over 정확.

**권고**: 본 (α) 합의 발효 후 R-S1 정정 cycle = 사용자 명시 시 진입 의무 (brief §9.5 답습). 정정 영역 = ADR-012 §2.3 Layer 4 → Layer 5 재명명 + 신규 Layer 4 = "CI 회귀 검증" 추가 (G4 §4.4.1 답습 정합) **또는** G4 §4.4.1 Layer 4 → Layer 5 재명명 + Layer 5 = Layer 6 재명명 (ADR-012 §2.3 답습 정합).

→ 본 NOTE = 본 cycle 영역 외 (사용자 명시 후속 R-S1 정정 cycle 진입 시 영역).

---

### N-O-2 [NOTE]: brief §9.5 "별도 commit 영역" 4건 (cross-reference 갱신) 의 순서 / 우선순위 명시 부재

**위치**: brief §9.5 (line 455~458)

**관찰**:
- 4건 명시: (1) ADR-008 차단조건 #1 보조 cross-reference 추가 / (2) ADR-012 §2.2 event enum 신규 등록 / (3) ADR-011 §8.5 후속 작업 등록 / (4) R-S1 정정 영역
- 4건 모두 "별도 commit" 명시만, *순서 / 우선순위 / 의존 관계* 0건

**권고**: 사용자 영역 carry-over (본 cycle = 별도 commit 영역 *결정 0건* 답습) — 본 NOTE = 후속 cycle 사용자 명시 영역.

→ 본 NOTE = 본 cycle 영역 외.

---

### N-O-3 [NOTE]: brief §2.2.2 Entry 자격 매트릭스 = G4 §4.4 Layer 4 Entry 3/8 충족 (line 169~177) — Layer 4 *단독* 진입 의존 영역 4 gap 답습이 (γ) 분리 영역 결정 cycle 후속

**위치**: brief §2.2.2 (line 168~179)

**관찰**:
- Entry 자격 8 조건 中 충족 3건 (Design/Governance Gate / ADR-012 §2.3 권위 / G4 §4.4 P-1 흡수) + gap 4건 (Layer 1 실 구현 / canonical JSON test corpus / Layer 4 CI step / ledger 첫 genesis) + 사용자 영역 1건
- gap 4건 中 3건 = Layer 1 의존 영역 (Layer 1 실 구현 / genesis hash / test corpus는 Layer 1 검증 의존)
- brief 답습 정확 = "(γ) 별도 cycle" 분리

**권고**: (γ) 분리 영역 결정 cycle 진입 시 N-C-2 4 대안 (γ-a/b/c/d) 매트릭스 답습 의무. 본 NOTE = 본 cycle 영역 외 후속 cycle 사용자 영역.

---

## §4 검토 의무 6 항목별 대안 분석

### §4.1 두 영역 통합 R-6 workflow 확장 (§2.3 W-A) vs 대안 (검토 의무 1)

| 대안 | 장점 | 단점 | ceremony-inflation | 실패 영역 식별 | branch protection contexts 부담 | 운영 복잡도 | 본 (α) 권고 |
|----|----|----|----|----|----|----|----|
| **W-A 단일 R-6 확장 (brief)** | CI 자원 효율 + evidence 통합 + R-6 답습 한 PR | step 수 증가 + 실패 영역 식별 ↑ (step name 분리 완화) | 차단 ✅ | 복잡도 ↑ (완화 가능) | 0 추가 (8 contexts 답습) | MEDIUM | ✅ 답습 |
| **W-B 별도 2 workflow** (`secret-egress-redaction.yml` + `ledger-chain-verify.yml`) | 영역 분리 명확 + 실패 영역 즉시 식별 | ceremony-inflation 위험 + R-6 답습 미답습 + branch protection contexts 추가 부담 | 위험 ❌ | 명확 ✅ | 2+ 추가 | HIGH | ❌ 비권고 (51 brief §4.2 답습) |
| **W-C 단계 분리 (GP-2 우선 → G4 후속)** | GP-2 진입 부담 적음 (2.5/5) + 단계 안전 | GP-2 / G4 2 cycle 부담 + 외부 LLM 응답 2회 | 중간 | 명확 ✅ | 단계 분리 | HIGH | ⚠️ 부분 권고 (사용자 명시 시) |
| **W-D 그룹 D + 그룹 C 별도 progression** (roadmap.md §5.3 답습) | roadmap.md §5.3 9 그룹 구조 답습 정확 + 영역 분리 명확 | 그룹 D / C 2 cycle 부담 + 통합 효율 0 | 중간 | 명확 ✅ | 그룹 별 분리 | HIGH | ⚠️ 부분 권고 |
| **W-E pre-commit hook 활용** | Layer 1 ≈ 500ms 답습 (CLAUDE.md §2) + 빠른 피드백 | log file canary inject 부적합 (pre-commit 시점 log 미생성) + hash chain 부분 검증만 가능 | 차단 | 영역 한정 | 0 | LOW | ❌ 비권고 (영역 부적합) |

**Agent C 결론**: W-A 권고 정합 (51 brief §4.2 답습 정확) + W-C / W-D 부분 권고 사용자 명시 영역 + W-E 비권고 명시 추가.

### §4.2 sub-수단 결정 (β) 분리 vs (α) 흡수 대안 (검토 의무 2)

| 대안 | 본 (α) cycle 범위 | (β) cycle 부담 | 합의 형태 | 사용자 부담 |
|----|----|----|----|----|
| **본 brief 답습 (전면 (β) 분리)** | 영역 진입만 | R-1~R-5 + L-1~L-5 全 결정 (별도 cycle) | (α) 풀 3+1 + 외부 LLM 1+ / (β) 풀 3+1 | 2 cycle |
| **(α) 흡수 (24 entry 답습)** | 영역 진입 + R-4 + L-4 결정 | 0 (모두 (α) 흡수) | 1 cycle 풀 3+1 + 외부 LLM 1+ | 1 cycle (효율) |
| **부분 통합 (P-1, Agent C 식별)** | 영역 진입 + 기본 권고 (R-4 + L-4) 확정 / 세부 catalog (Tier-2/3 / threshold 등) (β) | sub-수단 *적용 세부* (catalog / threshold) | 1.5 cycle | 중간 |
| **단계 분리 (P-2, Agent C 식별)** | 영역 진입 + GP-2 sub-수단 (R-4) 흡수 / G4 sub-수단 = (β) | L-1~L-5 + 외부 library trigger (별도 cycle 외부 library 위험) | 1 cycle (GP-2) + 1 cycle (L) | 중간 |

**Agent C 결론**: 본 brief 답습 (전면 (β) 분리) = 안전, 사용자 명시 강화. 단점 = 2 cycle 부담. (P-1) 부분 통합 = MVP 권고 R-4 + L-4 답습 시 합리적 대안 (51 audit brief §2.3 + §3.4 답습 권고). 본 cycle 진입 합의 발효 시 = 사용자 명시 영역 선택.

### §4.3 G4 §4.4 Layer 분리 영역 결정 (γ) 대안 (검토 의무 3)

위 §2 N-C-2 답습 — (γ-a/b/c/d) 4 대안 매트릭스.

| 대안 | ADR-012 §2.3 다층 강제 답습 | Entry 자격 충족 (51 brief §3.2 답습) | scope |
|----|----|----|----|
| **(γ-a) Layer 1+2 의존 영역 우선 → Layer 4 추가** | ✅ 단계적 (Layer 1 MANDATORY → Layer 2 MANDATORY → Layer 4 MANDATORY) | 단계별 충족 진행 | 안전 우선 |
| **(γ-b) Layer 4 단독 (Layer 1+2 자동 의존)** | ⚠️ Layer 1+2 = 의존 영역 자동 진입 형식 명시 부재 시 권위 chain 위험 | Layer 4 검증 대상 = Layer 1+2 이므로 자동 의존 | 효율 우선 |
| **(γ-c) Layer 1+2+4 동시 (defense-in-depth)** | ✅ 가장 견고 | 3 영역 동시 부담 | 견고성 우선 |
| **(γ-d) Layer 4 단독 + Layer 1+2 = (γ) 별도 cycle (brief 답습)** | ⚠️ Layer 4 단독 진입 의미 부재 risk (51 brief §11 P-5 답습) | 의존 영역 4 gap 답습 | scope 분리 우선 |

**Agent C 결론**: (γ-a) 또는 (γ-c) 권고. 본 brief = (γ-d) 답습 = scope 분리 우선 (정합) — 단, (γ) 별도 cycle 진입 시 4 대안 매트릭스 답습 의무 강조 (N-C-2).

### §4.4 외부 library 도입 대안 (L-2 / L-5 vs L-1 / L-4) (검토 의무 4)

위 §2 N-C-3 답습 — L-1 / L-2 / L-1.5 trade-off + 자체 RFC 8785 reference test corpus vs 외부 library 검증 충분성 trade-off.

**Agent C 결론**: 본 brief 답습 (L-4 = L-1 + L-3 stdlib 단독 MVP) = MVP 권고 정합. **L-1.5 (stdlib + 자체 reference test corpus + 매년 cross-check)** = Agent C 추가 식별 alternative (별도 cycle 진입 시 검토 영역).

### §4.5 추가 대안 영역 식별 (검토 의무 5)

- **51 brief §4 W-A 통합 외 W-C / W-D / W-E**: §4.1 답습 — W-C / W-D 사용자 명시 영역, W-E 비권고
- **두 영역 외 MVP-2 영역 추가** (GP-1 / GP-4 / GP-6 / G3 / G4 Layer 4 외): brief §0.3 #26 = "MVP-3 ~ MVP-5 영역" 답습 정확. 본 cycle 분리 정당 (영역 확장 시 부담 ↑ + roadmap-mvp1 §1.3 답습 정확)
- **외부 LLM 1+ vs 2+ 격상**: §2 N-C-4 답습 — G4 영역 답습 시 2+ 권고 가능성, 본 cycle = 1+ 답습 정합 (24 entry 답습 우선)
- **Implementation Evidence PASS 발효 시점 강화**: §2 N-C-5 답습 — R-S1 정정 미완료 시 외부 LLM 2+ 격상 권고

### §4.6 24 entry 답습 동형 패턴 대안 — 본 cycle 특수성 무시 위험 (검토 의무 6)

| 항목 | 24 entry (MVP-1 1.5차 보강) | 본 (α) cycle (MVP-2 진입) | 동형 패턴 적합성 |
|----|----|----|----|
| Scope | 4 sub-수단 채택 결정 통합 (작은 영역) | MVP-2 영역 진입 + 25 조합 (큰 영역) | ⚠️ 부분 (영역 규모 차이) |
| sub-수단 처리 | 채택 결정 통합 | (β) 분리 | ❌ 차이 명시 (brief §1.3 line 112 + §10 P-5) |
| 합의 형태 | 풀 3+1 + 외부 LLM 1+ | 풀 3+1 + 외부 LLM 1+ | ✅ 일치 |
| 권위 발효 | sub-수단 채택 + 진입 자격 | 영역 진입 자격만 | ❌ 차이 명시 |
| 합의 형태 (PASS 발효) | 32 entry MVP-1 PASS 답습 (1+ 외부 LLM) | brief §4.2 답습 (1+) | ✅ 일치 (R-S1 미해소 시 격상 가능 — N-C-5) |

**대안**: **32 entry MVP-1 PASS 발효 합의 답습 패턴** = 본 cycle 보다 적합한 답습 source 가능성:
- 32 entry = "MVP-1 PASS *발효*" + Implementation Evidence 6 BLOCKING + 5 권고 1pass 흡수
- 본 (α) = "MVP-2 영역 *진입*" + (β) / (γ) cycle 진입 자격 발효
- 두 cycle 모두 "큰 결정 + 외부 LLM 1+ + 사용자 명시" 패턴 일치
- 32 entry = **PASS 발효** / 본 (α) = **진입 발효** — 동격 큰 결정

**Agent C 평가**: 24 entry 답습 정합 + 32 entry 답습 *추가* 적용 권고 — brief §9.2 답습 source 4건 명시 (24 entry / 32 entry 모두 포함) 정확. **본 cycle = "entry brief 구조 (24 entry)" + "큰 결정 합의 형태 (32 entry)" 2 답습 source 동시 적용** = 본 brief 답습 정합.

---

## §5 자기 편향 자기진단

Agent C (대안 탐색가) 본 응답 작성자의 자기 발견 잠재 위험:

| # | 위험 | 본 응답 처리 |
|---|------|--------------|
| **C-P-1** | Agent C 가 "더 나은 방법" 강박으로 *불필요한 대안* 식별 위험 | R-C-1 (W-C / W-D / W-E 3 대안) 식별 시 본 (α) 권고 = W-A 답습 정합 명시 + 비교 매트릭스 추가 의무 한정 (대안 채택 강요 0건). N-C-2 (γ) 4 대안 명시 시 본 brief (γ-d) 답습 정합 명시 |
| **C-P-2** | Agent C 가 본 brief §10 P-4 R-S1 위험을 *확대 해석* 위험 | N-O-1 = brief §10 P-4 자기진단 정확 + Agent C verbatim 확인 (ADR-012 §2.3 line 182 + G4 §4.4.1 line 649 직접 read evidence) — 사실 기반, 확대 해석 0건 |
| **C-P-3** | Agent C 가 외부 LLM 2+ 격상 권고 (N-C-4) 가 *ceremony-inflation* 권유 위험 | N-C-4 = "1+ vs 2+ trade-off 명시 + 본 cycle 1+ 채택 정당화 보강" 한정 — 2+ 격상 *결정 0건* (사용자 영역) |
| **C-P-4** | Agent C 가 sub-수단 (β) 흡수 권고 (N-C-1) 가 사용자 영역 침입 위험 | N-C-1 = "부분 통합 (P-1) / 단계 분리 (P-2) 대안 명시 + 본 brief 채택 (전면 분리) 정당화 보강" 한정 — 흡수 강요 0건 |
| **C-P-5** | Agent C 가 codex 응답 + Agent A/B 응답 *참조* 위험 (병렬 독립 평가 위반) | 본 응답 §0 read 자료 목록 = primary 검토 대상 + 답습 source 8건 한정, codex / Agent A/B 응답 *참조 0건* 명시 evidence (Reviewer 통합 시 cross-check) |
| **C-P-6** | Agent C 가 6 검토 의무 답습 의무 회피하고 대안 식별만 집중 위험 | 본 응답 §4 = 6 검토 의무 각 항목별 대안 분석 매트릭스 명시 (1: W-A 대안 / 2: (β) 분리 대안 / 3: (γ) 분리 대안 / 4: L 대안 / 5: 추가 영역 / 6: 24 entry vs 32 entry 답습) |
| **C-P-7** | Agent C 가 BLOCKING 2건 + 권고 6건 식별이 *과잉 식별* 위험 | BLOCKING 2건 = R-C-1 (W-A 대안 매트릭스 부족, 답습 source 51 brief §4.2 단 1 대안 답습 한정 — 본 (α) 독립 평가 부족) + R-C-2 (roadmap.md §5.4 단축 합의 권고 vs 본 cycle 격상 정당화 부족, missing 영역 명시) — 둘 다 **선차 변경 매트릭스 누락 / 대안 비교 부족** 객관적 결함. 권고 6건 = 모두 흡수 시 v1.1 자격 충분 (REVISE / REJECT 아님) |

---

## §6 본 응답 결론 요약

**판정**: **APPROVE WITH CONDITIONS**

- **BLOCKING 2건** 흡수 후 brief v1.1 진입 자격 발효 권고:
  - R-C-1 (W-C / W-D / W-E 3 대안 추가 매트릭스 + W-A 채택 비교 정당화)
  - R-C-2 (선차 변경 매트릭스 항목 5 추가 — roadmap.md §5.4 단축 합의 권고 vs 본 cycle 풀 3+1 + 외부 LLM 1+ 격상 정당화)

- **권고 6건** 흡수 = 대안 매트릭스 보강:
  - N-C-1 (sub-수단 (β) 분리 vs 부분 통합 / 단계 분리 대안 명시)
  - N-C-2 (γ 4 대안 매트릭스 — (γ-a/b/c/d))
  - N-C-3 (L-2/L-5 vs L-1/L-4 외부 library trade-off + L-1.5 alternative)
  - N-C-4 (외부 LLM 1+ vs 2+ trade-off + 1+ 채택 정당화)
  - N-C-5 (Implementation Evidence PASS 발효 시점 R-S1 정정 사전조건 명시)
  - N-C-6 (event enum 명명 대안 E-1 / E-2 + scope 대안 S-1)

- **NOTE 3건** (사용자 영역 후속 cycle):
  - N-O-1 (R-S1 정정 cycle 영역, brief §9.5 답습)
  - N-O-2 (별도 commit 4건 순서 / 우선순위 사용자 영역)
  - N-O-3 (γ 분리 영역 결정 cycle 후속)

**대안 탐색가 한 줄 결론**: 본 brief v1 = 51 entry audit brief 답습 충실 + 자기진단 P-1~P-7 정확 — **그러나 "대안 탐색 차원" 부족** (W-A 단 1 대안 답습 / γ 2 대안 명시 / sub-수단 분리 단일 권고). 본 응답 BLOCKING 2 + 권고 6 흡수 후 v1.1 = 풀 3+1 합의 발효 자격 충분. R-S1 잠재 risk = brief §10 P-4 자기진단 정확 (Agent C verbatim cross-check 일치) — Reviewer 단독 verify 자격 + §9.5 정정 cycle 사용자 명시 영역 carry-over 정합.

---

**Agent C 응답 v1 끝.**

**다음 단계**: Reviewer 통합 (Agent A/B/C + 외부 LLM codex 응답 cross-check) → brief v1.1 흡수 보강 권고 → Reviewer 최종 판정.
