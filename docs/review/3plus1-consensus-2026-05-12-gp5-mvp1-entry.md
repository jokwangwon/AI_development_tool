# GP-5 (Provider Adapter Enforcement) MVP-1 진입 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 + 5/5 풀 3+1 승격 트리거 0건 발화 검증 후 확정 (§4 답습)
**합의 일자**: 2026-05-12 후속 5 (GP-3 진입 합의 APPROVE WITH CONDITIONS + Condition C-1 흡수 후속, commits `bbc05ca` + `ed1b6d6` push 완료 후속)
**검토 대상**: GP-5 MVP-1 진입 권고 수단 조합 = **T-6 (T-2 import-linter — Group A 2차 채택 + T-5 custom AST scanner — Group A 1차/3차 병행 운영) + PC-3 (CI-only enforcement) + AR-1 (CI step fail-closed 한정)**
**보조 참조**: `docs/architecture/implementation-runtime-roadmap-mvp1.md` §4 + §5 (commit `cddd22f` + `bbc05ca`), `docs/review/3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` §1.6 + §5.1 (commit `95be2e5`), `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (commit `6dc5bdc` — 답습 형식), `docs/phase0/g2-gp5-provider-adapter-enforcement-poc.md` (Group A 1차), `docs/phase0/g2-gp5-poc2-depcruise-rule-scope.md` (Group A 2차 SCOPE), `docs/phase0/g2-gp5-poc2-import-linter-implementation.md` (Group A 2차 구현), `docs/phase0/g2-gp5-poc3-url-endpoint-model-name-scanner.md` (Group A 3차), `docs/architecture/governance-preconditions.md` §7 (GP-5 Entry/Exit), `docs/architecture/llm-providers-design.md` §9 (Liquidity 위반 패턴 차단), `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #4, `docs/decisions/ADR-009-self-adapter-v2-entry-conditions.md` C-N §2.3 + §5, `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.2 (event enum)
**검토 목적**: GP-5 MVP-1 구현 진입에 사용할 수단 조합 (T-6 + PC-3 + AR-1) 의 *진입 적격성* 판단 한정
**판정**: ✅ **APPROVE WITH CONDITIONS (단축 합의 — Reviewer-only) — GP-5 MVP-1 진입 가능, 4 conditions 명시 (C-1 1.5차 보강 영역 분리 / C-2 T3 영역 별도 풀 3+1 / C-3 G5-4 P1 v2 facade real 본문 별도 합의 / C-4 O-2 GP-5 합의 후속 §5.4 신설), 5/5 풀 3+1 승격 트리거 0건 발화**

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-12 다섯 번째 명령):

> "GP-5 MVP-1 진입 합의 진행. 권고 수단 후보 = T-6 + PC-3 + AR-1. ... O-2는 아직 흡수하지 마세요. ... GP-5 합의 완료 후 MVP-1 roadmap §5.4 통합 위험 sub-section 신설."

**사용자 명시 결정 답습**:
- 검토 형태 = Reviewer-only 단축 합의 적격성 우선 판단 + 5 트리거 1+ 발화 시 풀 3+1 승격
- 검토 대상 = T-6 + PC-3 + AR-1 권고 수단 조합 한정
- 검토 목적 = **GP-5 MVP-1 진입 *가능 여부* + 수단 조합 *적격성*** 한정
- 결론 형식 = APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK 中 1
- 본 합의 = **GP-5 Implementation Evidence PASS *선언* / MVP-1 PASS 선언 / GP-3 + GP-5 통합 PASS 선언 / runtime 구현 / CI-hook 구현 / Operational Readiness PASS / Hermes PMO 격상 / Observation O-2 자동 흡수 모두 *불가***

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 검토 = 권고 수단 조합 *진입 적격성* 한정, *Implementation Evidence PASS 선언* 0건 + *수단 본문 채택 commit* 0건) | ✅ |
| 직전 합의 (`3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` Reviewer-only) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 진입 적격성) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **5 풀 3+1 승격 트리거 발화 0건** | ✅ §4 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` §4 GP-5 deepening 작성자 = 본 권고 수단 (T-6 / PC-3 / AR-1) 작성자. 자기 작성 권고 자기 검토 한계 인지.

**청산 매커니즘**:

1. **사후 외부 LLM 충족** — 본 검토 답습 출처 (Group A 1차/2차/3차 PoC + Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄, T-2 import-linter 채택) + ADR-008 + ADR-009 C-N + ADR-011 + ADR-012) 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 + Group A 2차 풀 3+1 합의 (T-1 vs T-2 vs T-3 vs T-4 결정) 자체가 외부 LLM 답습 (`external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 + L51 답습 — depcruise 본질적 한계 3종 명시)
2. **격상 전 면제** — Hermes PMO 격상 *전*. 본 검토 = MVP-1 진입 *적격성* 한정
3. **합의 권위 내부 변경** — 본 검토 = `3plus1-consensus-2026-05-12-implementation-runtime-roadmap-mvp1.md` (DRAFT APPROVE) + `3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (GP-3 진입 APPROVE WITH CONDITIONS) 답습 = *권위 내부* 작업 (GP-3 합의 후속 양 GP 균형 답습)
4. **자기 작성 한계 명시** — 본 §0.3 + §5 명시
5. **수단 조합 *진입 적격성* 한정** — 본 합의 ≠ 수단 *본문 채택* — Implementation Evidence PASS 발효 시점에 ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 별도 합의 의무 답습

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| GP-5 Implementation Evidence PASS 선언 | ❌ (별도 합의 영역 — ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정) |
| MVP-1 PASS 선언 (GP-3 + GP-5 통합) | ❌ (별도 합의 영역) |
| GP-3 + GP-5 통합 PASS 선언 | ❌ (별도 합의 영역) |
| MVP-1 1.5차 보강 (T-1 dependency-cruiser / T-3 grimp / T-4 ruff / T-5 custom AST 단독 / PC-1 framework / PC-4 / AR-3 통합) | ❌ (풀 3+1 합의 영역, 본 검토 §1.5 + §6.3 답습) |
| T3 영역 진입 (AR-2 branch protection / facade real 본문 P1 v2 / Tier-2/3 vendor 확장) | ❌ (별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시) |
| MVP-1 roadmap §5.4 통합 위험 sub-section 신설 (Observation O-2) | ❌ (본 GP-5 합의 후속 영역, Condition C-4) |
| G5-4 P1 v2 facade real 본문 작성 | ❌ (별도 합의 영역 — `g2-gp5-poc2-import-linter-implementation.md` §8 TR-1 답습) |
| G5-5 runtime egress 차단 (Layer 2) | ❌ (MVP-3/4 영역, `g2-gp5-provider-adapter-enforcement-poc.md` §9 답습) |
| G5-6 의미적 lock-in | ❌ (라운드트립 영역, MVP-3 G4 §4.6 답습) |
| G5-7 OAuth 응답 후처리 / 메타 저장 / 파서 차단 (§9.1 #2~#6) | ❌ (MVP-3 영역) |
| 실 runtime code / CI workflow 수정 / hook 구현 | ❌ |
| ADR 본문 자동 갱신 | ❌ (cross-reference 답습 한정) |
| Tier-2 / Tier-3 vendor 자동 확장 | ❌ |
| threshold *고정* | ❌ (FP/FN/latency 모두 *후보 한정*) |
| Operational Readiness PASS 선언 | ❌ |
| Hermes PMO 격상 선언 | ❌ |

---

## 1. 권고 수단 조합 평가

### 1.1 T-6 (T-2 import-linter + T-5 custom AST scanner 병행)

#### 1.1.1 T-2 (import-linter, Group A 2차 채택) 평가

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 2차 PoC `.importlinter` config + `requirements-dev.txt` (import-linter 2.11) + `src/` placeholder (TR-1 미발화 답습) + `transitive_import.py` fixture + CI workflow 양방향 검증 직접 답습 | ✅ |
| 풀 3+1 합의 답습 | Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄, 17 통합 조건 HIGH 7 / MEDIUM 7 / LOW 3, T-2 채택 APPROVE WITH CONDITIONS) 직접 답습 | ✅ |
| Transitive import 강점 | 본 PoC 핵심 추가 가치 — A→B→forbidden cascading 검출 (Group A 2차 §1 답습) | ✅ |
| C-9 RA-9 사전 검증 | `import-linter 2.11 + grimp 3.14` 환경에서 `include_external_packages = True` 정상 동작 확인 (2026-05-10) | ✅ |
| `google.generativeai` 도구 제약 | T-2 forbidden contract 제약 → 1차 AST scanner 단독 책무 분리 (`g2-gp5-poc2-import-linter-implementation.md` 각주 1 답습) | ✅ (책무 분담 명시) |
| 외부 의존성 | dev-dep 1개 (`pip install import-linter`) — Node 환경 도입 회피 (T-1 dependency-cruiser 미채택 사유 답습) | ✅ |
| MVP-1 영역 적격성 | T-2 = MVP-1 1차 영역 적격 (전체 17 항목 우선순위 매트릭스 Order 1 = GP-5 답습) | ✅ |

→ **T-2 = MVP-1 1차 진입 적격** (Group A 2차 풀 3+1 합의 권위 답습 충실).

#### 1.1.2 T-5 (custom AST scanner, Group A 1차/3차) 평가

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 1차 `tools/provider_import_scanner.py` (~165줄, AST 5 패턴 — direct/from/dynamic-importlib/__import__/model-name) + Group A 3차 `tools/provider_url_scanner.py` (~210줄, URL Tier-1 catalog 10 + Model Tier-1 catalog 19) 직접 답습 | ✅ |
| 동적 import 전담 | T-2 미커버 영역 — `importlib.import_module` + `__import__` 패턴 cover (Group A 2차 §1 책무 분담 답습) | ✅ |
| 모델명 분기 전담 | T-2 미커버 영역 — `if model == "claude-opus-..."` / `if "gpt-" in model_name` 패턴 cover (Group A 1차 답습) | ✅ |
| URL endpoint + 모델명 catalog 전담 | T-2 미커버 영역 — Group A 3차 답습 (10 vendor URL Tier-1 + 19 Model Tier-1, comment line 부분 회피, extension allowlist) | ✅ |
| 외부 의존성 | stdlib `re` + `dataclasses` 단독 — 외부 의존 0건 | ✅ |
| Tier-2/3 vendor 자동 확장 위험 | 0건 (Tier-1 catalog 답습 한정 — Group A 3차 §1 답습) | ✅ |
| MVP-1 영역 적격성 | T-5 = MVP-1 1차 영역 적격 (책무 분담 매트릭스로 T-2 와 통합 운영 = T-6) | ✅ |

→ **T-5 = MVP-1 1차 진입 적격** (Group A 1차/3차 PoC 답습 충실).

#### 1.1.3 T-6 = T-2 + T-5 병행 책무 분담 매트릭스 (mvp1.md §4.2.2 답습 + Group A 2차 §1 답습)

| 검증 영역 | T-2 (import-linter) | T-5 (custom AST scanner) | 통합 cover |
|---------|--------------------|-----|---------|
| Direct import (`openai`/`anthropic`/`litellm`/`ollama`) | ✅ (중첩 강화) | ✅ | ✅ (양쪽 cover) |
| Direct (`google.generativeai`) | ❌ (각주 1 답습) | ✅ | ✅ (T-5 단독) |
| From-import | ✅ (중첩 강화) | ✅ | ✅ (양쪽 cover) |
| **Transitive (A→B→forbidden)** | ✅ (T-2 강점) | ❌ | ✅ (T-2 단독) |
| 동적 import (`importlib`, `__import__`) | ❌ | ✅ (T-5 전담) | ✅ (T-5 단독) |
| 모델명 분기 (문자열) | ❌ | ✅ (T-5 전담) | ✅ (T-5 단독) |
| URL/endpoint 하드코딩 | ❌ | ✅ (Group A 3차 cover) | ✅ (T-5 단독) |
| 의미적 lock-in | ❌ | ❌ | ❌ (G5-6 라운드트립 영역, MVP-3) |

→ **T-6 책무 분담 = 7/8 영역 cover + 1/8 분리 영역 (의미적 lock-in = MVP-3 G4 §4.6 라운드트립 영역) 명시**. silent fail 위험 = `g2-gp5-poc2-import-linter-implementation.md` §6 답습 (CI fail-closed + 책무 분담 명시 + PR review 보조).

#### 1.1.4 T-6 종합 평가

| 항목 | 본 검토 | 충족 |
|------|--------|------|
| Group A 1차/2차/3차 PoC 답습 충실성 | ✅ (모든 PoC 산출물 직접 재사용 — 0 신규 구현) | ✅ |
| 책무 분담 매트릭스 명시 | ✅ §1.1.3 답습 + Group A 2차 §1 답습 | ✅ |
| silent fail 위험 회피 | CI fail-closed + 책무 분담 명시 + PR review 보조 (Group A 2차 §6 답습) | ✅ |
| TR-1~TR-5 재합의 trigger 등록 | Group A 2차 §8 답습 (`g2-gp5-poc2-import-linter-implementation.md` 답습) | ✅ |
| MVP-1 영역 적격성 | T-6 = MVP-1 1차 영역 적격 (1.5차 = T-1/T-3/T-4/T-5 단독 진입 = 풀 3+1 영역 분리) | ✅ |

→ **T-6 = MVP-1 1차 진입 적격** (T-2 + T-5 병행 운영, Group A 2차 풀 3+1 합의 권위 답습).

### 1.2 PC-3 (CI-only enforcement, GP-3 동일)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 1차/2차/3차 모두 CI-only enforcement 답습 (pre-commit framework 미도입) | ✅ |
| dev 환경 영향 | 0건 (PC-1 pre-commit framework 미도입, dev 환경 자동 강제 0) | ✅ |
| commit 자체 차단 | ⚠️ 부분 (commit 가능, push 시 CI 차단) — 본 영역 = 1.5차 보강 (PC-1 framework 또는 PC-4 = PC-1 + PC-3 병행) 영역 분리 |
| T2 영역 적격성 | T2 (CI step) — ADR-011 §2.4 답습, T3 미진입 | ✅ |
| GP-3 와의 일관성 | GP-3 진입 합의 (`6dc5bdc`) §1.3 PC-3 적격 답습 — 양 GP 동일 PC-3 채택 시 운영 부담 일관 | ✅ |
| MVP-1 영역 적격성 | PC-3 = MVP-1 1차 영역 적격 | ✅ |

→ **PC-3 = MVP-1 1차 진입 적격** (GP-3 합의 답습 충실).

### 1.3 AR-1 (CI step fail-closed 한정, GP-3 동일)

| 평가 항목 | 본 검토 | 충족 |
|----------|--------|------|
| PoC 답습 충실성 | Group A 1차/2차/3차 모두 CI step fail-closed 답습 | ✅ |
| T3 영역 진입 | 0건 (AR-2 GitHub branch protection rule 변경 = T3 영역, 본 검토 회피) | ✅ |
| 시스템 외부 PR 우회 위험 | ⚠️ 부분 (CI bypass 가능 — T3 영역 미진입의 trade-off) — 본 영역 = 1.5차 보강 (AR-3 = AR-1 + AR-2 통합) = 풀 3+1 영역 분리 |
| Hermes-originated commit auto-reject (G3 §2.2 #20) | 별도 영역 (G3 영역, 본 GP-5 합의 범위 외) — Group A 2차 답습 (G3 합의 후속 영역) |
| GP-3 와의 일관성 | GP-3 진입 합의 §1.4 AR-1 적격 답습 — 양 GP 동일 AR-1 채택 시 운영 부담 일관 | ✅ |
| MVP-1 영역 적격성 | AR-1 = MVP-1 1차 영역 적격 | ✅ |

→ **AR-1 = MVP-1 1차 진입 적격** (GP-3 합의 답습 충실).

### 1.4 4 sub-수단 종합 평가

| # | 수단 | MVP-1 영역 | 1.5차 보강 영역 | T3 진입 |
|---|-----|----------|--------------|-------|
| 1 | T-2 (import-linter, transitive 강점) | ✅ 1차 적격 | T-1 dependency-cruiser 단독 / T-3 grimp 단독 진입 = 풀 3+1 (Group A 2차 §8 TR-3 답습) | — |
| 2 | T-5 (custom AST, dynamic + model-name + URL) | ✅ 1차 적격 | T-4 ruff custom rule 단독 / T-5 단독 진입 = 풀 3+1 | — |
| 3 | T-6 = T-2 + T-5 병행 (PoC 채택 형태) | ✅ 1차 적격 | (해당 없음 — T-6 자체가 권고 수단) | — |
| 4 | PC-3 (CI-only enforcement) | ✅ 1차 적격 | PC-4 (PC-1 + PC-3 병행) = 단축 + 사용자 명시 | — (T3 영역 0) |
| 5 | AR-1 (CI step fail-closed) | ✅ 1차 적격 | AR-3 (AR-1 + AR-2 통합) = 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | AR-2 단독 = T3 영역 |

→ **5/5 sub-수단 모두 MVP-1 1차 진입 적격**. 1.5차 보강 / T3 진입 영역 = 별도 합의 영역 분리 명시 (Conditions §6 답습).

### 1.5 G5-4 P1 v2 facade real 본문 분리 명시 (Condition C-3)

본 합의 = T-6 + PC-3 + AR-1 *진입 적격성* 한정. **G5-4 (P1 v2 facade real 본문 = `src/adapters/llm/facade.py` LiteLLM 실 import) 작성 = 별도 합의 영역**:

- Group A 2차 §8 TR-1 답습 — facade real 본문 작성 시 T-2 룰 ignore_imports 검증 + LiteLLM 정상 동작 재합의 trigger
- 본 합의 = `src/adapters/llm/facade.py` placeholder 한정 (Group A 2차 PoC 답습 — 빈 함수 시제)
- P1 v2 (`llm-providers-design.md`) 작업 영역 분리 — 별도 P1 v2 facade MVP 합의 영역

→ **G5-4 = Condition C-3 별도 합의 영역 명시**.

---

## 2. 사용자 명시 8 검토 기준 매트릭스

| # | 기준 | 평가 | 답습 |
|---|-----|----|----|
| 1 | T-6 이 GP-5 MVP-1 의 1차 provider adapter 강제 수단으로 적절한가 | ✅ 적격 | §1.1 (T-2 + T-5 병행 + 책무 분담 매트릭스 7/8 cover) — Group A 1차/2차/3차 PoC 답습 + Group A 2차 풀 3+1 합의 권위 답습 |
| 2 | PC-3 이 CI-only enforcement 로 적절한가 | ✅ 적격 | §1.2 (Group A PoC 답습 + dev 환경 영향 0 + T2 영역 + GP-3 일관) |
| 3 | AR-1 이 fail-closed enforcement 로 적절한가 | ✅ 적격 | §1.3 (Group A PoC 답습 + T3 영역 진입 0 + GP-3 일관) |
| 4 | direct provider SDK import 차단 경로가 명확한가 | ✅ 명확 | §1.1.3 책무 분담 매트릭스 (T-2 direct + from-import + transitive + T-5 dynamic + model-name + URL endpoint, 5-vendor cover) |
| 5 | P1 facade 경유 강제가 Provider Liquidity 와 충돌하지 않는가 | ✅ 충돌 0건 | T-6 = facade single entry 강제 = Provider Liquidity 5-way Layer 1 모법 답습 (ADR-009 C-N §5 답습). facade 외 차단 → Provider Liquidity 보존. P1 v2 (`llm-providers-design.md` §9) 답습 |
| 6 | false positive / false negative 위험이 관리 가능한가 | ✅ 관리 가능 | FP = Group A PoC 0건 (실 src/ 0건 환경 측정 baseline 부재 — fixture 한정). FN = (i) 의미적 lock-in (G5-6 분리 영역 = MVP-3 G4 §4.6 라운드트립) + (ii) URL Tier-2/3 (Group A 3차 §1 분리 영역) + (iii) silent fail (Group A 2차 §6 = CI fail-closed + 책무 분담 + PR review 답습) — 모두 분리 영역 명시 |
| 7 | GP-3 secret hygiene 과 충돌하지 않는가 | ✅ 충돌 0건 | T-6 = adapter 강제 (provider 우회 차단) ↔ GP-3 = secret 검출. 두 GP 다른 layer (GP-5 = adapter / GP-3 = secret). secret 사용 자체는 facade 내부 (S-1 catalog 답습). 단 *통합 위험* = O-2 영역 (Condition C-4 별도 합의 분리) |
| 8 | Implementation Evidence PASS 와 Operational Readiness PASS 가 분리되어 있는가 | ✅ 분리 | T-6 / PC-3 / AR-1 = MVP-1 Implementation Evidence 영역 / 1.5차 보강 (T-1/T-3/T-4/T-5 단독 / PC-4 / AR-3) = 풀 3+1 / T3 영역 (AR-2 / Tier-2/3 / facade real 본문 P1 v2) = 별도 합의 / Operational Readiness PASS = MVP-6 영역 (PMO 격상 검토). §0.4 비검토 대상 분리 |

→ **8/8 검토 기준 모두 충족** (#3 부분 충족 항목 시스템 외부 PR 우회 위험 = 1.5차 보강 영역 분리 명시).

---

## 3. (MVP-1 roadmap §4 답습 + 본 합의 평가 통합)

본 §은 mvp1.md §4 GP-5 deepening + 본 합의 §1 + §2 평가의 통합 답습 한정. 신규 본문 0건.

| 영역 | 본 합의 통합 매트릭스 |
|------|------------------|
| §4.1 PoC 완료 | Group A 1차/2차/3차 답습 — Layer 1a (AST 5 패턴) + Layer 1b (Transitive) + Layer 1c (URL + Model name) ALL PASS |
| §4.2 수단 후보 비교 | 6 수단 매트릭스 (T-1 ~ T-6) → T-6 채택 권고 (본 합의 §1.1) |
| §4.3 pre-commit 후보 | PC-1 ~ PC-4 → PC-3 채택 권고 (본 합의 §1.2) |
| §4.4 PR auto-reject 후보 | AR-1 ~ AR-3 → AR-1 채택 권고 (본 합의 §1.3) |
| §4.5 측정 metric | direct/transitive/url/model_name/FP/FN/scan_latency (mvp1.md §4.5.1 답습) |
| §4.6 Rollback Trigger 10 | R-5 + R-9 + R-MVP1-G5-1~10 (mvp1.md §4.6 답습) |
| §4.7 Evidence Required 5형식 + 의존성 + 합의 형태 권고 | mvp1.md §4.7 답습 |

본 합의 = mvp1.md §4 본문 변경 0건 (cross-reference 답습 한정).

---

## 4. 5 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **Provider Adapter 강제 방식이 기존 Provider Liquidity 원칙을 약화하는 경우** | 본 합의 = T-6 (T-2 + T-5 병행) = Provider Liquidity 5-way Layer 1 모법 답습 (ADR-009 C-N §5 답습). facade single entry 강제 = Provider Liquidity 보존 강화. 약화 0건 | ❌ 0 |
| 2 | **특정 provider SDK lock-in 가능성이 생기는 경우** | 본 합의 = T-6 = 5-vendor (anthropic / openai / litellm / google.generativeai / ollama) 모두 차단 (Group A 1차 §2.1 답습 + 3차 10 vendor URL + 19 model 답습). specific lock-in 0건 | ❌ 0 |
| 3 | **direct SDK import 차단이 과도한 false positive 를 유발하는 경우** | T-6 = Group A PoC FP 0건 (실 src/ 0건 환경 baseline 부재 — fixture 한정 측정). 본 PoC threshold 답습 (정량 측정 baseline = T-2 contracts 1 kept + T-5 5 패턴 매칭 정확). 신규 risk 0건 | ❌ 0 |
| 4 | **enforcement 가 CI-only 를 넘어 branch protection 또는 T3 영역으로 들어가는 경우** | 본 합의 = AR-1 (T2 CI step) + PC-3 (T2 CI step) 모두 T2 영역. T3 영역 (AR-2 branch protection / facade real 본문 P1 v2 / Tier-2/3 catalog 확장) = 별도 풀 3+1 영역 분리 명시 (§0.4 + §6.3 = Conditions C-2 + C-3) | ❌ 0 |
| 5 | **ADR-011 T3 영역에 닿는 경우** | 본 합의 = T-6 + PC-3 + AR-1 모두 T2 영역 (CI step + 권고 수단 채택 권위). T3 영역 진입 = 별도 합의 영역 분리 명시 (Conditions C-2) | ❌ 0 |

→ **5/5 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 5. 메타 편향 자기진단

### 5.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = `implementation-runtime-roadmap-mvp1.md` §4 GP-5 deepening 작성자 = 본 권고 수단 (T-6 / PC-3 / AR-1) 작성자. 자기 작성 권고 자기 검토 한계 인지.

### 5.2 본 한계의 청산

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | 본 검토 답습 출처 모두 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 + Group A 2차 풀 3+1 합의 (Agent A/B/C 1206줄 + Reviewer 380줄, T-2 채택 권위) 자체가 외부 LLM 답습 (`external-review/2026-05-09-g2g3g4-promotion-response-claude.md` L39 + L51 답습) |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 검토 = MVP-1 진입 *적격성* 한정 |
| 3 | 합의 권위 내부 변경 | 본 검토 = MVP-1 roadmap 단축 합의 + GP-3 진입 합의 답습 = *권위 내부* 작업 (양 GP 균형 답습) |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §5 명시 |
| 5 | 진입 적격성 한정 (수단 본문 채택 ≠ 본 합의) | 본 합의 = *진입 적격성* — Implementation Evidence PASS 발효 시점 별도 합의 의무 답습 |
| 6 | GP-3 합의와의 일관성 | 본 합의 = GP-3 진입 합의 답습 형식 + PC-3 / AR-1 양 GP 동일 채택 — 일관성 보존 |

### 5.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 검토 형태 + 권고 수단 조합 + 8 검토 기준 + 5 트리거 + 결론 형식 + 8 금지 사항 + O-2 보류 모두 §0 + §1 + §2 + §4 + §6 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 4 sub-수단 평가 + §2 8 검토 + §4 5 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.4 5 sub-수단 모두 T2 영역 + T3 진입 영역 분리 + Conditions C-2 |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 + §2 모두 *수단 후보 평가* (목적 = Provider Liquidity 5-way Layer 1 모법 보존) — ADR-011 §2.1 (a)~(e) 5조건 답습 + ADR-009 C-N §5 모법 ADR 답습 |
| 5 | 본 합의가 *하지 않는* 것 명시 (§0.4 + §6.2) | ✅ 명시 |

### 5.4 본 단축 합의가 *하지 않는* 것

§6.2 답습.

---

## 6. 결론

```
✅ APPROVE WITH CONDITIONS (단축 합의, Reviewer-only)
   — GP-5 MVP-1 진입 가능 (T-6 + PC-3 + AR-1 5 sub-수단 조합 1차 적격)
   — 4 Conditions 명시:
     C-1: 1.5차 보강 영역 (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3) = 풀 3+1 또는 단축 합의 영역 분리
     C-2: T3 영역 (AR-2 branch protection / Tier-2/3 vendor 확장) = 별도 풀 3+1 + 외부 LLM 1+ + 사용자 명시
     C-3: G5-4 (P1 v2 facade real 본문 = `src/adapters/llm/facade.py` LiteLLM 실 import) = 별도 합의 영역 분리 (Group A 2차 §8 TR-1 답습)
     C-4: O-2 (GP-3 + GP-5 통합 위험) = 본 GP-5 합의 후 §5.4 신설 영역 분리 (사용자 명시 답습 — 다음 단계)
   — 5/5 풀 3+1 승격 트리거 0건 발화 → 단축 합의 적격 확정
```

본 결론은 **GP-5 MVP-1 *진입 가능 여부* + 5 sub-수단 조합 *적격성*** 한정. **본 합의는 GP-5 Implementation Evidence PASS *선언* / MVP-1 PASS 선언 / GP-3 + GP-5 통합 PASS 선언 / runtime 구현 / CI-hook 구현 / Operational Readiness PASS / Hermes PMO 격상 / Observation O-2 자동 흡수 / 수단 본문 채택 commit 모두 *불가***.

### 6.1 본 합의가 *발생시키는* 것

- ✅ GP-5 MVP-1 진입 *적격성* 권위 권고 발행 (5 sub-수단 조합 = T-6 (T-2 + T-5) + PC-3 + AR-1)
- ✅ T-2 (import-linter, transitive 강점) MVP-1 1차 영역 적격 권위 권고 — Group A 2차 풀 3+1 합의 권위 답습
- ✅ T-5 (custom AST, dynamic + model-name + URL) MVP-1 1차 영역 적격 권위 권고 — Group A 1차/3차 PoC 답습
- ✅ T-6 = T-2 + T-5 병행 책무 분담 매트릭스 (7/8 cover + 1/8 분리 영역 명시) 권위 권고
- ✅ PC-3 (CI-only enforcement, T2 영역, GP-3 일관) MVP-1 1차 영역 적격 권위 권고
- ✅ AR-1 (CI step fail-closed, T3 미진입, GP-3 일관) MVP-1 1차 영역 적격 권위 권고
- ✅ direct provider SDK import 차단 경로 명확화 (5-vendor cover, 10 URL Tier-1 + 19 Model Tier-1)
- ✅ P1 facade 경유 강제 ↔ Provider Liquidity 5-way Layer 1 모법 보존 (충돌 0건) 권위 권고
- ✅ GP-3 secret hygiene 충돌 0건 (다른 layer — adapter vs secret) 권위 권고
- ✅ G5-4 (P1 v2 facade real 본문) 분리 영역 명시 = Condition C-3
- ✅ G5-5 / G5-6 / G5-7 (runtime egress / 의미적 lock-in / OAuth 등) 분리 영역 명시 (MVP-3/4 영역, §0.4 답습)
- ✅ 1.5차 보강 영역 5 후보 (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3) 분리 영역 명시 = Condition C-1
- ✅ T3 영역 3 후보 (AR-2 / Tier-2/3 / facade real 본문) 분리 영역 명시 = Condition C-2 + C-3
- ✅ Observation O-2 (GP-3 + GP-5 통합 위험) 영역 분리 명시 = Condition C-4 (본 GP-5 합의 후 §5.4 신설 영역, 사용자 명시 답습)
- ✅ Evidence Ledger enum 후보 답습 (`event: provider_adapter_enforcement_layer1_static` — `g2-gp5-poc2-import-linter-implementation.md` §4 직접 답습)
- ✅ MVP-1 영역 양 GP 균형 (GP-3 + GP-5 모두 진입 적격성 발효) 권위 권고

### 6.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습 — 2026-05-12 진입 명령 답습)

- ❌ GP-5 Implementation Evidence PASS 선언
- ❌ MVP-1 PASS 선언 (GP-3 + GP-5 통합)
- ❌ GP-3 + GP-5 통합 PASS 선언
- ❌ runtime code 구현 (`src/adapters/llm/facade.py` 본문 변경 / `tools/provider_import_scanner.py` 본문 변경 / `tools/provider_url_scanner.py` 본문 변경 / `.importlinter` config 변경 등 0건)
- ❌ CI workflow 수정 / hook 구현 (`.github/workflows/provider-adapter-enforcement.yml` 본문 변경 / `.pre-commit-config.yaml` 신설 / GitHub branch protection rule 변경 등 0건)
- ❌ Operational Readiness PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ GP-3 + GP-5 통합 위험 자동 흡수 (Observation O-2 = Condition C-4 별도 합의 — 본 GP-5 합의 후속 §5.4 신설 영역 분리)
- ❌ 수단 *본문 채택* commit (T-6 / PC-3 / AR-1 = 진입 *적격성* 권위 권고 한정, 본문 채택 commit = 별도 합의 + ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정 — ADR-008 차단조건 #4 / ADR-009 C-N / ADR-012 본문 변경 0건)
- ❌ Tier-2 / Tier-3 vendor 자동 확장 (Tier-1 catalog 답습 한정 — Group A 3차 §1 답습)
- ❌ threshold *고정* (FP/FN/scan_latency 모두 *후보 한정*)
- ❌ 1.5차 보강 자동 진입 (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3 = Condition C-1 별도 합의 영역 분리)
- ❌ T3 영역 자동 진입 (AR-2 / Tier-2/3 / facade real 본문 P1 v2 = Conditions C-2 + C-3 별도 풀 3+1 영역 분리)
- ❌ G5-4 P1 v2 facade real 본문 작성 (Condition C-3 별도 합의 영역 분리)
- ❌ G5-5 runtime egress 차단 (Layer 2, MVP-3/4 영역)
- ❌ G5-6 의미적 lock-in 검출 (라운드트립 영역, MVP-3 G4 §4.6)
- ❌ G5-7 OAuth 응답 후처리 / 메타 저장 / 파서 차단 (MVP-3 영역)
- ❌ 외부 LLM 자동 호출
- ❌ 실 API key / provider SDK / 외부 API 호출

### 6.3 다음 진입점 (사용자 결정 영역 — 사용자 명시 최종 순서 답습)

본 합의 APPROVE WITH CONDITIONS → GP-5 MVP-1 진입 *적격성* 권위 권고 발효 → 다음 작업 (사용자 결정 영역):

| 후보 | 영역 | 합의 형태 | Conditions 흡수 |
|------|------|---------|----------------|
| (b+c 통합 시점, 사용자 명시 다음 단계) | **MVP-1 roadmap §5.4 통합 위험 sub-section 신설** (Observation O-2 흡수) | 단축 합의 적격 (양 GP Rollback 답습 + ADR-011 §2.1 5/5 답습 영역) | **C-4 흡수** (Observation O-2 — 사용자 명시 처리 시점 답습) |
| (d-1) | **GP-5 1.5차 보강 합의** (T-1 dependency-cruiser 단독 진입) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | C-1 흡수 |
| (d-2) | **GP-5 1.5차 보강 합의** (T-3 grimp 단독) | 풀 3+1 (Group A 2차 §8 TR-3 답습) | C-1 흡수 |
| (d-3) | **GP-5 1.5차 보강 합의** (T-4 ruff custom rule 단독) | 풀 3+1 (도구 변경 영향 분석) | C-1 흡수 |
| (d-4) | **GP-5 1.5차 보강 합의** (T-5 custom AST 단독) | 풀 3+1 (transitive 자체 구현 부담 ↑) | C-1 흡수 |
| (d-5) | **GP-5 1.5차 보강 합의** (PC-1 / PC-4 framework 도입) | 단축 합의 + 사용자 명시 (T2 정책 영역) | C-1 흡수 |
| (d-6) | **GP-5 1.5차 보강 합의** (AR-3 = AR-1 + AR-2 통합) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 (T3 영역) | C-1 + C-2 흡수 |
| (e-1) | **G5-4 P1 v2 facade real 본문 작성** (`src/adapters/llm/facade.py` LiteLLM 실 import) | 별도 P1 v2 facade MVP 합의 영역 (Group A 2차 §8 TR-1 답습) | C-3 흡수 |
| (e-2) | **GP-5 Implementation Evidence PASS 발효 합의** | 별도 합의 + 사용자 명시 + ADR-011 §2.1 (a)~(e) 5/5 evidence | (전체 conditions 충족 후) |
| (e-3) | **MVP-1 PASS 발효** (GP-3 + GP-5 통합) | 별도 합의 + 사용자 명시 + Implementation Evidence PASS 발효 | (전체 conditions 충족 후) |

**권고 시작 명령** (사용자 권한 영역, 사용자 명시 최종 순서 답습):

- **"O-2 §5.4 통합 위험 sub-section 신설"** — Condition C-4 흡수 (사용자 명시 다음 단계 답습)
- **"GP-5 1.5차 보강 합의 진입 (수단 d-1 ~ d-6 中 1)"** — Condition C-1 / C-2 흡수 (풀 3+1 또는 단축)
- **"G5-4 P1 v2 facade real 본문 작성 진입"** — Condition C-3 흡수 (별도 합의)
- **"MVP-1 PASS 발효 합의"** — 전체 conditions 충족 후 (별도 합의 + 사용자 명시)

본 합의 자체 = **GP-5 MVP-1 진입 *적격성* 권위 권고 발행 + Conditions 4 영역 분리 명시**. 진입 결정 = 사용자 명시 결정 영역.

---

## 7. Conditions 매트릭스 (보강/분리 영역)

### 7.1 Condition C-1 — 1.5차 보강 영역 (T-1 / T-3 / T-4 / T-5 단독 / PC-4 / AR-3) 분리

| 후보 | 합의 형태 | 사유 |
|------|--------|------|
| T-1 dependency-cruiser 단독 진입 | 풀 3+1 + 외부 LLM 1+ | Node 환경 도입 비용 高 + Python repo 정합성 저하 (`g2-gp5-poc2-depcruise-rule-scope.md` 답습) |
| T-3 grimp 단독 | 풀 3+1 (Group A 2차 §8 TR-3 답습) | import-linter 보다 lower-level, 본 PoC 답습 충실성 ↓ |
| T-4 ruff custom rule 단독 | 풀 3+1 (도구 변경 영향 분석) | transitive 미지원, T-2 강점 손실 |
| T-5 custom AST 단독 | 풀 3+1 (transitive 자체 구현 부담 ↑) | import-linter 답습 충실성 ↓ |
| PC-4 (PC-1 + PC-3 병행) | 단축 합의 + 사용자 명시 | T2 정책 영역 (ADR-011 §2.4) |
| AR-3 (AR-1 + AR-2 통합) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | T3 영역 (branch protection rule 변경) |

### 7.2 Condition C-2 — T3 영역 진입 분리

| 후보 | T3 영역 | 합의 형태 |
|------|-------|--------|
| AR-2 단독 (branch protection rule 변경) | branch protection rule = T3 (repo policy 수준) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 |
| Tier-2 / Tier-3 vendor 확장 (Anthropic Tier-2 / 신규 vendor 등) | catalog 확장 = T3 (정책 영역) — Group A 3차 §1 답습 | 풀 3+1 + 외부 LLM 1+ |
| Hermes-originated commit auto-reject (G3 §2.2 #20) | G3 영역 — 본 GP-5 합의 범위 외, G3 합의 후속 영역 | G3 영역 별도 합의 |

### 7.3 Condition C-3 — G5-4 P1 v2 facade real 본문 분리

| 항목 | 분리 사유 | 분리 영역 |
|------|---------|---------|
| `src/adapters/llm/facade.py` LiteLLM 실 import 작성 | Group A 2차 §8 TR-1 답습 — facade real 본문 작성 시 T-2 룰 ignore_imports 검증 + LiteLLM 정상 동작 재합의 trigger | P1 v2 facade MVP 합의 영역 (`llm-providers-design.md` 작업 영역) |
| 책무 경계 | 본 GP-5 MVP-1 = T-6 / PC-3 / AR-1 *진입 적격성* 한정 — facade real 본문 = G5-4 영역 (mvp1.md §4.1.2 답습 분리 영역) | 별도 합의 |

### 7.4 Condition C-4 — Observation O-2 (GP-3 + GP-5 통합 위험) 분리

| 항목 | 처리 시점 | 합의 형태 |
|------|---------|--------|
| MVP-1 roadmap §5.4 통합 위험 sub-section 신설 | **본 GP-5 합의 후속 영역** (사용자 명시 답습 — "GP-5 합의 완료 후 MVP-1 roadmap §5.4 통합 위험 sub-section 신설") | 단축 합의 적격 (양 GP Rollback 답습 + ADR-011 §2.1 5/5 답습 영역) |
| 통합 위험 3 row 본문화 | (i) provider key adapter 우회 / (ii) direct SDK + secret leakage 결합 / (iii) local-CI-Docker 일관성 | 본 §5.4 신설 시 통합 |

### 7.5 4 Conditions 합의 형태 권고 종합

| 합의 영역 | 합의 형태 | 사유 |
|---------|---------|------|
| 본 합의 자체 (GP-5 MVP-1 진입 적격성) | Reviewer-only 단축 합의 (본 보고서) | 사용자 명시 진입 명령 답습 + 5 트리거 0/5 발화 |
| C-1 흡수 (1.5차 보강) | 풀 3+1 (T-1 / T-3 / T-4 / T-5 단독 / AR-3) + 단축 (PC-4) | 수단별 trade-off |
| C-2 흡수 (T3 영역 진입) | 풀 3+1 + 외부 LLM 1+ + 사용자 명시 | T3 영역 답습 |
| C-3 흡수 (G5-4 facade real 본문) | 별도 P1 v2 facade MVP 합의 영역 | Group A 2차 §8 TR-1 답습 |
| **C-4 흡수 (O-2 §5.4 신설)** | **단축 합의 (양 GP Rollback 답습)** | **사용자 명시 다음 단계 답습** |

---

**합의 commit 권위**: 본 commit (`docs(review): record GP-5 MVP-1 entry consensus APPROVE WITH CONDITIONS`)
**본 commit + 직전 commits (`cddd22f` MVP-1 roadmap 본문 + `6c91980` references + `95be2e5` MVP-1 roadmap 단축 합의 + `6dc5bdc` GP-3 진입 합의 + `bbc05ca` G3-7 row 추가 + `ed1b6d6` GP-3 condition absorption) = MVP-1 roadmap deepening 작성 + DRAFT 적격성 합의 + GP-3 진입 적격성 합의 + C-1 흡수 + GP-5 진입 적격성 합의 완료**
**다음 세션 진입점** (사용자 명시 최종 순서 답습): **MVP-1 roadmap §5.4 통합 위험 sub-section 신설** (Observation O-2 흡수, Condition C-4)
