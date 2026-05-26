# ADR-013 / ADR-014 후보 발행 결정 검토 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ("우선 Reviewer-only 단축 검토로 후보 발행 필요성을 정리")
**합의 일자**: 2026-05-09 (후속 12 — ADR-013 / 014 후보 발행 결정 검토)
**검토 대상**: ADR-013 후보 (Hermes PMO Activation / Human Review / Runtime Governance) + ADR-014 후보 (Memory/Skill Runtime Implementation 또는 Provider-agnostic Migration / Round-trip 검증) — **후보 발행 필요성 검토** (실 ADR 본문 작성은 본 검토 후속, 사용자 명시 답습)
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — ADR-013 / 014 후보 모두 *현 시점 발행 보류*. 후속 시점 / 조건부 발행 권고**

---

## 0. 사전 점검

### 0.1 가동 사유

P2 v3 §9.2 별도 PR 우선순위 #5 답습 ("ADR-013 / 014 후보 발행 결정 — 별도 합의, Hermes PMO 격상 *전*"). 사용자 명시 작업명 = "ADR-013 / ADR-014 후보 발행 결정 검토".

**사용자 명시 결정 답습** (2026-05-09 후속 11 후속):
- 작업명 = "ADR-013 / ADR-014 후보 발행 결정 검토"
- 목적 = "Hermes PMO 격상 전 별도 ADR로 분리해야 할 주제가 남아 있는지 판단"
- 작업 단계 = **후보 발행 필요성 검토만, 본문 작성 X**
- 검토 형태 = Reviewer-only 단축 검토 우선 — 5 풀 3+1 승격 트리거 1+ 발화 시 풀 3+1 승격
- 7 항목 분류 사용자 명시: 필요 이유 / 기존 ADR 커버 / Implementation 처리 / Hermes PMO 격상 전후 / 합의 형태

### 0.2 단축 채택 사유

본 검토는 다음 단축 합의 충분 조건 모두 충족:

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (ADR 본문 작성 X, 발행 필요성 검토만) | ✅ 사용자 명시 답습 |
| 직전 합의 (G2/G3/G4 헤더 cross-reference 갱신, 후속 11) 패턴 답습 가능 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **5 풀 3+1 승격 트리거 발화 0건** | ✅ §3 답습 (5/5 트리거 0 발화) |

### 0.3 메타 편향 인지 (G3 §4.7 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 ~ 012 + P2 v3 + G2/G3/G4 작성자와 동일 패밀리. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘**:
1. 사후 외부 LLM 충족 — P2 v3 정식 채택 cross-vendor 외부 LLM 2건 + ADR-012 발행 외부 LLM 2건 권위 *내부* 작업
2. 격상 전 면제 — Hermes PMO 격상 *전*
3. 합의 권위 내부 변경 — 본 검토 = P2 v3 §9.2 #5 답습
4. 자기 작성 한계 명시 — 본 §0.3 + §4 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ |
| Implementation/Runtime PASS 선언 | ❌ |
| **ADR-013 / 014 본문 자동 작성** | ❌ 사용자 명시 금지 (본 검토 = 후보 발행 필요성 검토만) |
| ADR-008 ~ 012 결정 내용 변경 | ❌ |
| 실 runtime code / migration script / hook 구현 | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |

---

## 1. 사용자 명시 7 항목 분류

### 1.1 ADR-013 후보가 필요한 이유

**ADR-013 후보 영역** (사용자 명시): "Hermes PMO Activation / Human Review / Runtime Governance 관련 결정"

#### 1.1.1 발행 필요성 평가

| 영역 | 현 권위 출처 | ADR-013 신규 발행 필요성 |
|------|---------|----|
| **Hermes PMO Activation 절차** | P2 v3 §2.6 (격상 절차 7 단계) + §2.6.1 (PMO 격상 체크리스트 12 조건) + ADR-008 §단계 마이그레이션 | **선택적** — P2 v3 = SDD 권위 (ADR 보다 하위), ADR Amendment / 신규 발행으로 *영구 ADR 권위 정착* 가능. 단 *현 시점 필수 X* — 격상 *시점* 에 ADR-008 본문 갱신 또는 ADR-013 신규 발행 결정 |
| **Human Review (Human-in-the-loop) 의무화** | P2 v3 §11.1 + §2.6 단계 5.5 (인간 전문 리뷰) + Gemini 사고모델 §7.10 #3 cross-vendor 권고 답습 | **선택적** — P2 v3 §11.1 권위 충족. ADR 권위 정착 차원에서 ADR-013 또는 ADR-008 부록 추가 가능 |
| **Runtime Governance** | G3 §1 ~ §7 (권위 위계 운영 + 22 권한 + 자기참조 차단 + Evidence 결정 5 운영 규칙 + Hermes 변조 차단 매트릭스 4항목) | **불필요** — G3 = 정식 산출 (Design/Governance Gate PASS Bundled). Runtime 영역은 G3 *Implementation 단축 합의* 영역, 별도 ADR 불필요 |
| **권위 위계 영구화** | ADR-011 §2.3 (Hermes ≠ root of trust) + ADR-009 C-N §2.3 (Hermes PMO ↔ provider 분리) + ADR-012 §2.12 (Hermes 변조 차단 매트릭스) | **불필요** — 3 ADR 영구 권위 충족 |

#### 1.1.2 ADR-013 발행 *필요* 시점 (조건부)

다음 조건 중 *하나라도* 발생 시 ADR-013 발행 *필수* 검토:

1. **Hermes PMO Activation 절차의 영구 ADR 권위 정착 결정** — P2 v3 §2.6 권위만으로 *부족* 판정 시 (예: 사용자 또는 외부 검토에서 SDD 권위 vs ADR 권위 차이 명시 권고)
2. **Human Review 의무 수준 변경** — P2 v3 §11.1 의 "Human-in-the-loop 1회 이상" 의무 *강화* 또는 *조정* 시 (예: 다중 인간 리뷰어 / 외부 감사 / 정량 트리거 추가)
3. **Runtime Governance 새 권위 결정** — G3 §1 ~ §7 본문 *변경* 또는 새 22 권한 추가 시
4. **ADR-008 본문 갱신 PR 묶음 (Hermes PMO 격상 절차 추가) 시점** — ADR-008 본문 갱신 vs ADR-013 신규 발행 *분리 결정* 영역. 단축 합의로 ADR-008 부록 추가 채택 시 ADR-013 *불필요*

#### 1.1.3 ADR-013 발행 *현 시점 보류* 권고

**현 시점 (2026-05-09 후속 12)** Hermes PMO 격상 절차 = P2 v3 §2.6 + §11.1 + §2.6.1 + ADR-008 부록 B + ADR-011 §2.3/§2.4 + ADR-009 C-N §2.3 + ADR-012 §2.12 = **7 권위 layer 중첩 답습**. 추가 ADR 필요성 *낮음*.

**발행 권고 시점** (선택 1):
- 시점 (a): ADR-008 본문 갱신 PR (P2 v3 §9.2 #3 답습) 시점에 *부록 추가* 또는 *ADR-013 신규 발행* 사용자 결정 (추후)
- 시점 (b): Hermes PMO 격상 적격성 검토 시점 (4 게이트 모두 Implementation/Runtime PASS 후) 에 *영구 권위 정착* 검토
- 시점 (c): 외부 LLM cross-vendor 추가 검토 시점에 ADR-013 권위 정착 권고 발생 시

### 1.2 ADR-014 후보가 필요한 이유

**ADR-014 후보 영역** (사용자 명시): "Memory/Skill Runtime Implementation 또는 Provider-agnostic Migration / Round-trip 검증 관련 결정"

#### 1.2.1 발행 필요성 평가

| 영역 | 현 권위 출처 | ADR-014 신규 발행 필요성 |
|------|---------|----|
| **Memory/Skill Runtime Implementation 형식** | G4 §2 (Memory scope) + §3 (Skill schema 17 필드) + §4.2 (JSONL 11 필드) + §5 (boundary 4 금지) | **불필요** (현 시점) — G4 = 정식 산출 (Design PASS). Runtime Implementation 시점에 ADR-014 발행 검토 가능 |
| **Provider-agnostic Migration script** | G4 §4.5 (변환 스크립트 사양) + ADR-012 §2.10 (Migration BLOCK + manual + migration_failed entry) | **불필요** (현 시점) — Design PASS 까지 권위 충족. Implementation/Runtime PASS 시점 (migration script PoC 완료 후) 발행 검토 가능 |
| **Round-trip 검증** | G4 §4.6 (Tier-based round-trip 검증 절차 — T2 strict / T3 의미 보존) + ADR-012 §2.9 (Tier-based + 3 ledger entry 형식) | **불필요** (현 시점) — Design PASS 까지 권위 충족 |
| **provider_bindings lint 룰 강제** | G4 §3.5 (`provider_bindings` schema *required*/*exclusive* 금지) + G2 GP-5 (depcruise 룰) + ADR-009 C-N §5 Layer 1 모법 | **불필요** (현 시점) — Implementation 단축 합의 영역 (C-H 후속, P2 v3 §9.2 답습) |

#### 1.2.2 ADR-014 발행 *필요* 시점 (조건부)

1. **Migration script Implementation/Runtime PASS PoC 완료 시점** — 라운드트립 검증 + canonical JSON sha256 일치 + Hermes 의존 0 + 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능 evidence 누적 후 ADR-014 신규 발행 검토
2. **G4 §4.2 schema 진화 정책 변경 시점** — semver MAJOR (필드 제거 / 이름 변경 / 타입 변경) 변경 시 ADR Amendment 또는 ADR-014 신규 발행 (ADR-012 §3.2 답습)
3. **Provider Liquidity 5-way Multi-layer Defense 새 Layer 추가 시점** — 현 5 Layer (ADR-009 C-N §5 Layer 1 + G2 GP-5 + G3 §6.4 + G4 §3.5/§4.3 + ADR-012 §원칙 6) 외 새 Layer 발생 시
4. **Tier-2 / Tier-3 catalog 확장 합의 시점** — G2 GP-1 의 Tier-1 42 catalog 확장 (Tier-2 / Tier-3) 합의에 ADR-014 권위 정착 검토

#### 1.2.3 ADR-014 발행 *현 시점 보류* 권고

**현 시점** G4 = Design PASS / Implementation Pending. ADR-014 = *Implementation/Runtime PASS 시점 발행 검토 영역*. 현 시점 발행 = *PoC 전 권위 정착* → ADR-011 §2.1 (b) 격리 환경 PoC 실증 *전* 의 ADR 발행은 *기존 ADR 패턴 위반*. 

**발행 권고 시점** (선택 1):
- 시점 (a): G4 Implementation/Runtime PASS PoC 완료 후 ADR-014 신규 발행
- 시점 (b): G4 §4.2 schema 진화 (필드 제거/이름 변경/타입 변경 등 MAJOR 변경) 시점에 ADR Amendment 또는 ADR-014 신규
- 시점 (c): Tier-2 / Tier-3 catalog 확장 합의에 ADR-014 권위 정착

### 1.3 기존 ADR-008 / 009 / 010 / 011 / 012 로 충분히 커버되는 항목

다음 영역은 **기존 5 ADR + P2 v3 + G2/G3/G4 답습 충족** — ADR-013/014 신규 발행 *불필요*:

| 영역 | 권위 출처 |
|------|----|
| Hermes 도입 결정 (Option B) + 6 차단조건 | ADR-008 본문 + 부록 B |
| 자체 Adapter v2.0 진입 트리거 (T1~T4) + P1 facade MVP + Hermes PMO ↔ provider 분리 | ADR-009 C-N |
| SQLCipher Vault HSM 키 관리 | ADR-010 |
| 수단/목적 분리 + G1a/G1b + Hermes ≠ root of trust + T1/T2/T3 | ADR-011 |
| Evidence Ledger Protection (12 보호 원칙 + 4 매트릭스 + 5 추가 의무 + Hermes 변조 차단 매트릭스 4항목 + Provider Liquidity 5-way Layer 5) | ADR-012 |
| Hermes PMO 격상 절차 7 단계 + 12 조건 체크리스트 + 인간 전문 리뷰 의무화 | P2 v3 §2.6 + §11.1 + §2.6.1 |
| 4 게이트 정의 + Design/Governance Gate PASS (Bundled) | G2 / G3 / G4 정식 산출 |
| Provider Liquidity 5-way Multi-layer Defense (Layer 1 ADR-009 §5 + Layer 2 G3 §6.4 + Layer 3 G4 §3.5 + Layer 4 G4 §4.3 + Layer 5 ADR-012 §원칙 6) | ADR-009 C-N §5 + ADR-012 §원칙 5/6 + G3 §6.4 + G4 §3.5/§4.3 |
| 합의 인프라 (3+1 + 외부 LLM + 인간 리뷰) | ADR-011 §2.4 + P2 v3 §11 + Gemini §7.10 #3 답습 |

→ **현 시점 ADR-013/014 신규 발행 *불필요* 영역 = 9건**.

### 1.4 새 ADR이 아니라 G2/G3/G4 Implementation 작업으로 넘겨야 할 항목

| 영역 | 처리 방식 |
|------|----|
| G2 GP-2 ~ GP-6 PoC 실증 + CI 강제 + runtime hook | G2 Implementation/Runtime PASS 별도 합의 (단축 또는 풀 3+1) |
| G3 운영 구현 (22 권한 hook / wrapper / sidecar / CI step / depcruise 룰 코드) | G3 Implementation/Runtime PASS 별도 합의 |
| G4 migration script (`hermes_to_claude.py` / `hermes_to_openai.py` 등) + 라운드트립 PoC | G4 Implementation/Runtime PASS 별도 합의 |
| ADR-012 CI enforcement (R-6 workflow ledger 검증 step + canonical JSON 검증 + prev_hash 검증 + timestamp monotonicity) | ADR-012 §10.2 답습, 별도 PR (Implementation 영역) |
| ADR-009 T1~T4 trigger detection task (분기별 측정) | ADR-009 §3.1~§3.4 답습, 분기별 별도 합의 |
| Provider Liquidity Layer 1~5 runtime 활성 (depcruise + AST 스캐너 + pre-commit hook + CI step) | C-H 별도 합의 (P2 v3 §9.2 답습) |
| Hermes-originated commit auto-reject runtime 구현 | G3 Implementation 영역 |
| Tier-2 / Tier-3 catalog 확장 | 별도 합의 (Implementation 영역 + 정량 트리거 충족 후) |

→ **8 영역 = G2/G3/G4 Implementation 작업 영역, 별도 ADR 불필요**.

### 1.5 Hermes PMO 격상 전 반드시 ADR화해야 하는 항목

P2 v3 §2.6.1 12 조건 PMO 격상 체크리스트 답습 — *현 시점 모두 충족 또는 별도 합의 영역* :

| PMO 격상 조건 | 현 권위 |
|------|----|
| G1b Implementation/Runtime PASS | ✅ ADR-008 부록 B + R-7 SOP §7.3 (이미 권위) |
| GP-1 (G1b 흡수) Implementation/Runtime PASS | ✅ G2 §3 (정식 산출, 이미 권위) |
| GP-2 ~ GP-6 Implementation/Runtime PASS | Implementation 영역, ADR-013 *불필요* (G2 정식 산출 + 별도 합의 권위 충분) |
| G3 runtime hooks/wrappers + Hermes 변조 차단 매트릭스 runtime | Implementation 영역, ADR-013 *불필요* (G3 + ADR-012 §2.12 권위 충분) |
| G4 migration round-trip PASS + JSONL writer + 11 필드 schema 활성 | Implementation 영역, ADR-014 *발행 시점 후보* — 단 *Implementation PASS 시점* |
| ADR-012 evidence protection CI | ADR-012 §10.2 별도 PR (Implementation 영역) |
| ADR-009 T1~T4 trigger detection task | 분기별 별도 합의 |
| Provider Liquidity 5-way Layer 1~5 runtime 활성 | C-H 별도 합의 |
| 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 | 합의 *시점* 별도 진행 |
| **인간 전문 리뷰 (Human-in-the-loop)** | ✅ P2 v3 §11.1 + §2.6 단계 5.5 (이미 권위) |
| 사용자 명시 격상 결정 | 합의 *시점* 별도 |
| **ADR-008 본문 Hermes PMO 격상 절차 추가 PR** | **ADR-008 본문 갱신 PR (P2 v3 §9.2 #3 답습) — ADR-013 *대체 가능*** |

→ **Hermes PMO 격상 전 반드시 ADR화해야 하는 항목 = 1건** (ADR-008 본문 갱신 PR — 부록 추가 또는 ADR-013 신규 발행 *분리 결정* 영역). **현 시점 ADR-013 / 014 *모두 불필요*** (대체 가능).

### 1.6 Hermes PMO 격상 후에 다뤄도 되는 항목

| 영역 | 사유 |
|------|----|
| ADR-014 (Memory/Skill Runtime Implementation 또는 Migration script 영구 권위) | Implementation/Runtime PASS PoC 완료 후 발행 검토 |
| Tier-2 / Tier-3 catalog 확장 ADR | Tier-2/3 catalog 정량 트리거 충족 후 별도 합의 |
| 새로운 Hermes plugin / extension 권위 ADR | Hermes upstream 변경 또는 새 plugin 발생 시점 |
| 자체 Adapter v2.0 implementation ADR | ADR-009 T1~T4 트리거 1+ 충족 후 별도 ADR |
| 새로운 Phase 4+ (Phase 1/2/3 후속) 작업 ADR | Phase 진입 결정 시점 별도 합의 |
| Memory/Skill scope 확장 (Session / Team-Agent) ADR | 정량 트리거 (파생 프로젝트 ≥ 3건 / 실 코드 ≥ 1000 줄) 충족 후 별도 |

→ **6 영역 = 격상 후 다뤄도 되는 항목** (현 시점 ADR 불필요).

### 1.7 풀 3+1이 필요한 항목과 단축 합의로 충분한 항목

| 영역 | 합의 형태 | 사유 |
|------|----|----|
| ADR-013 (Hermes PMO Activation 영구 권위 정착) — *발행 결정 시점* | **풀 3+1 + 외부 LLM 1+** | Hermes PMO 격상 = T3 변경 + 영구 권위 발행 = ADR Amendment 절차 답습 |
| ADR-014 (Memory/Skill Runtime Implementation 영구 권위) — *발행 결정 시점* | **풀 3+1 + 외부 LLM 1+ (PoC evidence 후)** | Migration script Implementation = T3 영역 + 영구 권위 |
| ADR-008 본문 갱신 (Hermes PMO 격상 절차 추가) — *부록 추가 시점* | 단축 합의 또는 풀 3+1 (사용자 결정) | 부록 추가 = cross-reference + 절차 명시 한정 시 단축 합의, 격상 절차 *변경* 시 풀 3+1 |
| G2 GP-2~GP-6 Implementation PASS | 단축 합의 또는 풀 3+1 (각 GP 별 PoC + 검증) | (a)~(e) 5조건 답습 |
| G3 runtime enforcement Implementation PASS | 단축 합의 또는 풀 3+1 | (a)~(e) 5조건 답습 |
| G4 migration script + round-trip PoC | 단축 합의 (R2-5 답습) | PoC evidence 검증 후 |
| ADR-012 CI enforcement | 단축 합의 (별도 PR — Implementation 영역) | 사양 답습 한정 |

→ **ADR-013 / 014 신규 발행 = 풀 3+1 + 외부 LLM 1+ 의무 (각 발행 시점)**. **현 시점 본 검토 = 단축 합의 적격** (후보 결정만, 본문 작성 X).

---

## 2. 4 새 ADR 필요 기준 + 4 불필요 기준 평가

### 2.1 새 ADR 필요 기준 평가

| # | 기준 | ADR-013 후보 | ADR-014 후보 |
|---|----|----|----|
| 1 | 기존 ADR 결정 범위를 넘어서는 새 정책/권한/운영 결정 | ❌ 0 (P2 v3 §2.6 + ADR-008/011/012 답습 충족) | ❌ 0 (G4 + ADR-012 답습 충족) |
| 2 | Hermes PMO 격상 전 root-of-trust 또는 human review 체계 영향 결정 | ⚠️ 부분 — Human Review 영역 (P2 v3 §11.1 권위 충족) | ❌ 0 |
| 3 | Implementation/Runtime 단계 영구 기준 결정 | ⚠️ 부분 — Hermes PMO 격상 절차 영구 권위 정착 가능 | ✅ 현 시점 X, **PoC 완료 후 필요** |
| 4 | Provider Liquidity / Evidence Integrity 장기 영향 결정 | ❌ 0 (ADR-009 C-N + ADR-012 답습 충족) | ❌ 0 (G4 §3.5 + §4.3 + ADR-012 §원칙 5/6 답습 충족) |

→ **현 시점 4 기준 모두 *부분/불충족*** (ADR-013 = 2/4 부분, ADR-014 = 1/4 부분 — Implementation 후 시점). **현 시점 발행 *불필요*** 권고.

### 2.2 새 ADR 불필요 기준 평가

| # | 기준 | ADR-013 후보 | ADR-014 후보 |
|---|----|----|----|
| 1 | 단순 cross-reference 갱신 | ✅ 부분 (ADR-008 부록 추가 가능) | ✅ |
| 2 | 이미 ADR-008~012에서 결정된 내용의 반복 | ✅ 다수 (P2 v3 §2.6 + ADR-008 부록 B + ADR-011 + ADR-012 답습) | ✅ 다수 (G4 §4 + ADR-012 §2.10 답습) |
| 3 | G2/G3/G4 Implementation 세부 작업 처리 가능 | ✅ Runtime Governance 영역 = G3 Implementation | ✅ 모두 (Memory/Skill Runtime / Migration / Round-trip) |
| 4 | 아직 실험/PoC 전이라 결정하기 이른 항목 | ⚠️ 부분 (Hermes PMO 격상 시점에 결정 가능) | ✅ 강 (PoC 전 발행 = 기존 ADR 패턴 위반) |

→ **현 시점 4 기준 모두 *충족 또는 부분 충족*** → **현 시점 발행 *불필요* 권고**.

---

## 3. 5 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | Hermes PMO 격상 절차 자체 변경 | P2 v3 §2.6 + §2.6.1 권위 답습, 변경 0건 — 본 검토 = *후보 발행 필요성 검토만*, 절차 변경 0건 | ❌ 0 |
| 2 | Human Review 의무 수준 변경 | P2 v3 §11.1 + §2.6 단계 5.5 권위 답습, 변경 0건 — *Human-in-the-loop 1회 이상* 의무 수준 그대로 | ❌ 0 |
| 3 | Provider Liquidity / Evidence Integrity 원칙 변경 | ADR-009 C-N + ADR-012 + G4 §3.5/§4.3 권위 답습, 5-way Multi-layer Defense 변경 0건 + Evidence Ledger Protection 12 보호 원칙 변경 0건 | ❌ 0 |
| 4 | 새 영구 제약 발생 | 5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) 변경 0건. 본 검토 = 후보 결정 한정, 새 제약 발생 0건 | ❌ 0 |
| 5 | 기존 ADR-008~012 충돌 가능성 | 기존 5 ADR cross-reference 검증 통과, 충돌 0건. ADR-013 (선택적 발행) 가능성 평가 = ADR-008 부록 추가 또는 신규 ADR 분리 결정 영역 — 충돌 *아님* | ❌ 0 |

→ **5/5 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 4. 메타 편향 자기진단

### 4.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-008 ~ 012 + P2 v3 + G2/G3/G4 작성자와 동일 컨텍스트 패밀리. 자기 작성 산출 자기 검토 한계 인지.

### 4.2 본 한계의 청산 (G3 §4.7 답습)

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업. 본 검토 = 후보 결정 한정 — 별도 외부 LLM 회수 *불필요*. 단 **ADR-013 / 014 *발행 결정 시점* 에 cross-vendor 외부 LLM 1+ 권장** (Gemini §7.10 #3 답습) |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* |
| 3 | 합의 권위 내부 변경 | 본 검토 = P2 v3 §9.2 #5 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §4 명시 |

### 4.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 목적 + 작업 단계 + 7 항목 분류 + 4+4 새 ADR 기준 + 5 트리거 모두 본 §0 + §1 + §2 + §3 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 7 항목 분류 + §3 5 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.7 (ADR-013/014 발행 시점 = T3 변경, 풀 3+1 + 외부 LLM 1+ 의무) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1 (수단 = ADR 발행 / 목적 = 권위 정착 + 영구 보존) |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §5.2) | ✅ 명시 |

### 4.4 본 단축 합의가 *하지 않는* 것

§5.2 답습.

---

## 5. 결론

```
✅ APPROVE (단축 합의, Reviewer-only) — ADR-013 / 014 후보 모두 *현 시점 발행 보류*
```

본 결론은 **ADR-013 / ADR-014 후보 발행 결정** 의 *현 시점 발행 불필요 + 후속 시점 / 조건부 발행 권고* 한정.

### 5.1 본 합의가 *발생시키는* 것

- ✅ ADR-013 후보 (Hermes PMO Activation / Human Review / Runtime Governance) **현 시점 발행 보류** + 발행 시점 후보 명시 (선택 a/b/c)
- ✅ ADR-014 후보 (Memory/Skill Runtime Implementation / Migration / Round-trip) **현 시점 발행 보류** + 발행 시점 후보 명시 (선택 a/b/c)
- ✅ 현 시점 발행 *불필요* 영역 9건 enumerated (§1.3)
- ✅ Implementation 작업 영역 8건 enumerated (§1.4)
- ✅ Hermes PMO 격상 전 반드시 ADR화 영역 = 1건 (ADR-008 본문 갱신 PR — 부록 추가 또는 ADR-013 신규 분리 결정)
- ✅ 격상 후 다뤄도 되는 영역 6건 enumerated (§1.6)
- ✅ ADR-013 / 014 발행 시점 = 풀 3+1 + 외부 LLM 1+ 의무 명시 (§1.7)

### 5.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 자동 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ **ADR-013 / 014 본문 자동 작성** (사용자 명시 금지)
- ❌ ADR-008 ~ 012 결정 내용 변경
- ❌ 실 runtime code / migration script / hook 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장

### 5.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE → 다음 작업 (사용자 결정 영역):

1. **Hermes PMO 격상 적격성 검토** (다음 진입점, 별도 합의) — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 인간 전문 리뷰 + 사용자 명시 결정 후
2. **ADR-008 본문 갱신 PR** (Hermes PMO 격상 절차 추가) — 단축 합의 또는 풀 3+1 (사용자 결정)
3. **G2 GP-2~GP-6 / G3 / G4 Implementation/Runtime PASS 합의** — 각 별도 합의 (Implementation 영역)
4. **ADR-013 발행** — 격상 시점 또는 영구 권위 정착 결정 시점 (조건부)
5. **ADR-014 발행** — Migration script Implementation/Runtime PASS PoC 완료 후 (조건부)

**권고 시작 명령**:
- "Hermes PMO 격상 적격성 검토 진행해주세요 (4 게이트 Implementation/Runtime PASS 필요 — 별도 합의 + 외부 LLM 2 + 인간 전문 리뷰)" — 격상 진입 *전* 작업
- 또는 "G2 GP-2 ~ GP-6 / G3 / G4 Implementation 작업 시작해주세요" — Implementation 영역 진입

---

**합의 commit 권위**: 본 commit (`docs(review): record ADR-013/014 candidate decision short consensus APPROVE`)
**본 commit + housekeeping commits = 본 세션 후속 12 (ADR-013/014 후보 결정 검토) 완료**
**다음 세션 진입점**: Hermes PMO 격상 적격성 검토 (4 게이트 Implementation/Runtime PASS 후 별도) → 또는 ADR-008 본문 갱신 PR (Hermes PMO 격상 절차 추가) → 또는 G2/G3/G4 Implementation/Runtime PASS 영역 진입
