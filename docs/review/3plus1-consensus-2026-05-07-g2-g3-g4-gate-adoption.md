# 풀 3+1 합의 보고서: G2 + G3 + G4 통합 게이트 PASS 승격 (2026-05-07)

**날짜**: 2026-05-07
**합의 형태**: 풀 3+1 (Agent A + Agent B + Agent C + Reviewer) + 외부 LLM 1건 (GPT-5.5 Thinking)
**합의 범위**: G2 + G3 + G4 *Design/Governance Gate PASS* 승격 합의 한정
**합의 권위**: 사용자 명시 결정 + G4 §8.3 옵션 3 (G2+G3+G4 통합 풀 3+1 + 외부 LLM 1+) + G3 §4.4.2 (격상 통합 합의 시 외부 LLM 1+ 권장 — 본 합의 실현)
**상위 권위**: 헌법 5조 (관용 — Provider Liquidity), 헌법 8조 (보안), ADR-008 (Hermes 도입 Option B), ADR-009 C-N (Provider Liquidity 5-way Multi-layer Defense 모법 ADR Layer 1), ADR-011 §2.1 (수단/목적 분리 원칙), ADR-011 §2.3 (권위 위계 영구 권위), ADR-011 §2.4 (T1/T2/T3 자동 학습 vs 정책 변경 분리), system-identity-prequel §3 / §6.3 / §8.4 (Memory 2단계 + Skill 자동 추출 T1 한정)

**관련 evidence**:
- G2 DRAFT (`docs/architecture/governance-preconditions.md`) + DRAFT 검토 APPROVE AS DRAFT (`docs/review/3plus1-consensus-2026-05-07-g2-governance-preconditions-draft.md`)
- G3 DRAFT (`docs/architecture/hermes-not-root-of-trust-runtime.md`) + DRAFT 검토 APPROVE AS DRAFT (`docs/review/3plus1-consensus-2026-05-07-g3-root-of-trust-runtime-draft.md`)
- G4 DRAFT (`docs/architecture/provider-agnostic-memory-skill-design.md`) + DRAFT 검토 APPROVE AS DRAFT (`docs/review/3plus1-consensus-2026-05-07-g4-memory-skill-draft.md`, 13/13 기준 PASS + 9/9 금지 0 위반)
- P2 v3 DRAFT (`docs/architecture/hermes-adoption-design-v3.md`) + DRAFT 검토 APPROVE AS DRAFT (`docs/review/3plus1-consensus-2026-05-07-p2-v3-draft.md`)
- G1b PASS evidence (R-7 SOP §7.3 단축 합의, 2026-05-07)
- 외부 검토 의뢰서 (`docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md`, 2026-05-07 작성)
- 외부 LLM 응답 (`docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-response.md`, GPT-5.5 Thinking, APPROVE WITH CONDITIONS)

**사용자 명시 결정**:
- 옵션 3 (G2+G3+G4 통합 풀 3+1 + 외부 LLM 1+) 채택
- 본 합의 = *G2/G3/G4 게이트 승격 합의* — Hermes PMO 격상 / P2 v3 정식 채택 자동 트리거 금지
- Hermes PMO 격상 / P2 v3 정식 채택 / ADR-008/009/010/011 본문 갱신 / P2 v2 archive / system-identity-prequel archive / 실 runtime 코드 / 실 migration script 구현 모두 본 합의 범위 밖

---

## 0. 사전 점검 — 본 합의의 위치 + 범위 + 비대상

### 0.1 본 합의의 *목적* (사용자 명시 답습)

> **G2 + G3 + G4 세 게이트를 정식 PASS 로 승격할 수 있는지 판단한다 — 자기참조 편향을 외부 LLM 1+ 의견으로 통제하면서.**

**본 합의 결과로 *발생 가능* 한 것 (사용자 명시 결정 후)**:
- G2 / G3 / G4 헤더 *Design/Governance Gate PASS* 명시 (별도 commit)
- P2 v3 DRAFT 의 G2/G3/G4 상태 갱신 (별도 commit)
- INDEX / CONTEXT 갱신 (별도 commit)
- SESSION 로그 갱신

**본 합의 결과로 *발생하지 않는* 것 (사용자 명시 금지 답습)**:
- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 선언
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
- ❌ P2 v2 (`hermes-adoption-design.md`) archive 처리
- ❌ `system-identity-prequel.md` archive 처리
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
- ❌ Tier-2 / Tier-3 catalog 확장

### 0.2 본 합의 채택 사유 — 옵션 3 (통합 풀 3+1 + 외부 LLM 1+)

| 옵션 | 평가 |
|-----|------|
| 옵션 1 (각 게이트 별도 단축) | 책임 분리 매트릭스 시점차 일관성 손실 + 합의 보고서 ≥ 6건 |
| 옵션 2 (각 게이트 단독 풀 3+1) | 1인 부담 ~3배 + 동일 컨텍스트 반복 메타 편향 절감 미미 |
| **옵션 3 (G2+G3+G4 통합 풀 3+1 + 외부 LLM 1+)** | **PR 묶음 자연 + 책임 분리 매트릭스 동시 발효 + Provider Liquidity 4-way 완결성 즉시 + Hermes PMO 격상 합의 패턴 답습** |

### 0.3 본 합의가 *판정하지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 적격성
- ❌ P2 v3 정식 채택 적격성
- ❌ Implementation/Runtime PASS 적격성 (별도 합의)
- ❌ ADR 본문 갱신 적격성
- ❌ archive 처리 적격성

본 합의 PASS 의 *유일한 의미*: **G2 + G3 + G4 Design/Governance Gate 승격 + P2 v3 정식 채택 합의 *진입 단계* 적격**.

---

## 1. Phase 1 — 분배 (Distribution)

### 1.1 본 합의 입력

| # | 입력 | 관점 | 시야 |
|---|----|----|----|
| 1 | Agent A | 구현/운영 분석가 | 실제로 동작하는가? 구현 인계 가능한가? |
| 2 | Agent B | 품질/안전성 검증가 | 안전하고 견고한가? 우회 경로는? |
| 3 | Agent C | 대안 탐색가 / 단순화 옹호자 | 더 나은 방법? 단순화? 1인 부담? |
| 4 | 외부 LLM (GPT-5.5 Thinking) | 자기참조 편향 통제 — cross-vendor 시야 | "문서 설계 게이트 PASS" vs "Operational Readiness PASS" 분리 |

### 1.2 분배 원칙

- 본 합의 *Phase 2 독립 분석* 단계: Agent A/B/C 가 서로의 출력 및 외부 LLM 응답을 *참조하지 않음* (편향 방지 강제)
- 외부 LLM 응답은 *별도 commit* (`93b4d41`) 으로 회수 후 Reviewer 종합 단계에서 합산
- 본 Reviewer 종합 (Phase 3 + Phase 4) 은 4 입력 모두 *읽고* 교차 비교 + 합의 도출

---

## 2. Phase 2 — 독립 분석 요약 (Independent Analysis)

### 2.1 Agent A 결과 (구현/운영 분석가)

**판정**: ✅ APPROVE WITH CONDITIONS (6 조건)

**핵심 관찰**:
- G4 구체성 = VERY HIGH (17 + 11 + Layer 1~5 schema enumeration)
- G3 구체성 = HIGH (22 권한 + 15 보호 대상 + 3 위험 5 측면)
- G2 구체성 = HIGH (6 GP × 7 요소 구조)
- 계산적 우선 충족 (G2 6/6, G3 22/22, G4 거의 전부 계산적; 추론적 보조는 *의도적 사용자 review* 한정)
- 4 핵심 인터페이스 + 추가 2 (P10 + SPOF) 모두 모순 0건

**식별 위험 매트릭스**:
- HIGH 1건: W-3 SPOF 1인 동일 호스트 (의도적 수용)
- MEDIUM 4건: W-1 GP-2~GP-6 PoC 0건 / W-4 Layer 4+5 미구현 / W-5 Migration script 미구현 / W-8 `.git/` author SPOF (W-3 부분)
- LOW 4건: W-2 산술 오류 / W-6 의미 보존 기준 부재 / W-7 GP-4 Layer 5 의존 / W-9 ADR cross-reference 별도 PR

**6 조건**:
- C-1: Design/Governance Gate 한정
- C-2: W-3 SPOF 명시 수용 + 트리거 5건 의무 발동
- C-3: W-1/W-4/W-5 Implementation Pending 명시
- C-4: W-2 산술 오류 후속 정정
- C-5: W-6 의미 보존 기준 정밀화 권고
- C-6: PMO 격상 / P2v3 / ADR / archive / runtime / migration 본 합의 범위 외

### 2.2 Agent B 결과 (품질/안전성 검증가)

**판정**: ✅ APPROVE WITH CONDITIONS (8 조건 + 4 추가 권고)

**핵심 관찰**:
- §2.5 보호 대상 15건 enumeration 차단력 = 견고
- 22 권한 분류 + 충돌 매트릭스 12 행 = 결정적 처리 견고
- §4 자기참조 차단 13 행 + §4.5 처리 권한 표 = 자기 격상 차단 견고
- 30+ 명시 부정 layer (헤더 / §0.2 / §11.2 / 종료 줄) = 해석 위험 차단 충분

**식별 위험 매트릭스**:
- HIGH 3건: H-1 단일 호스트 SPOF / H-2 Implementation/Runtime PASS 분리 해석 위험 / H-3 메타-순환 자기참조 청산
- MEDIUM 8건: M-1 Worker proxy 우회 / M-2 ADR 본문 Memory 복제 / M-3 ADR Amendment 오인 유도 / M-4 §10 단축 합의 T3 잠식 / M-5 commit auto-reject 판정 알고리즘 / M-6 합의 보고서 사후 변조 / M-7 단축 표현 silent loss / M-8 P15/P16/P17 누락 후보
- LOW 5건: L-1 산술 오류 / L-2 P13/P14 흡수 적격 / L-3 dependency lock silent merge / L-4 schema enum 외 차단 / L-5 catalog 자동 확장

**8 조건 + 4 추가 권고**:
- C-1: Implementation/Runtime PASS 분리 명시 *재확인*
- C-2: 트리거 자동 검출 hook (G3 §5.5.3) Implementation 합의에 포함
- C-3: §4 자기참조 차단 판정 알고리즘 (Hermes-originated commit 기준) Implementation 합의에 포함
- C-4: P9 / P11 / P12 deferred candidates 정식 등록 시점 명시 + P11 supply-chain (Hermes PMO 격상 *전* 권장)
- C-5: P15 / P16 / P17 신규 후보 (Agent B 자기 발견) 후속 합의 등록
- C-6: G3 §2.4 자동 롤백 합산 정정 (14/22 → 15/22)
- C-7: External LLM 응답 cross-vendor distinct 정도 사후 검증
- C-8: 본 PASS *범위 외* (PMO 격상 / P2 v3 / ADR / archive / runtime / script) 반복 명시

**4 추가 권고 (BLOCK 사유 아님)**:
- PR-2 ADR-012 §2.12 Layer 4 CI 회귀 검증 step 추가 의무화 (Implementation 시점)
- Skill `description` markdown prompt injection 패턴 grep
- Memory `content` 복제 검출 diff hook
- External anchor (Layer 5) RECOMMENDED → MANDATORY 격상 트리거 명시

### 2.3 Agent C 결과 (대안 탐색가 / 단순화 옹호자)

**판정**: ✅ APPROVE WITH CONDITIONS — 옵션 3 (G2+G3+G4 통합 풀 3+1 + 외부 LLM 1~2) 적격, 7 조건

**핵심 관찰**:
- 거버넌스 산출이 코드 0줄 + 50 마크다운 대비 *큼* — 단, *지속 가능* (자기-방어 표현 ≥ 50회 합리적 통제)
- 세 게이트 PASS 범위 *완전 동일* (Design/Governance Gate PASS) — 새 권위 결정 0건, 옵션 3 단순화 정당화 강력
- 자기참조 + 메타-순환 청산 *반복* 패턴화 — *지속 가능성* 의문

**단순화 평가**:
- G2 6 GP → 4 GP 통합: **반대** (P1~P8 경로 매핑 1:1 가독성 손실)
- G3 22 권한 → 19 권한 (#5↔#6 / #9↔#10↔#11 통합): **현 22 유지** (enumeration 명시 가치 큼)
- G4 17 필드 → 15 필드: **현 17 유지** + §3.6 MVP 분리 강화 (이미 12 필수 / 1 MVP-필수 / 4 MVP-권장)
- G4 옵션 B (통합 단일 문서): **유지** (단, ~1500 줄 증가 시 옵션 A 분리 재검토)

**식별 위험 매트릭스**:
- HIGH 3건: H-1 Implementation 한꺼번에 시도 위험 / H-2 메타-순환 청산 지속 가능성 / H-3 enumeration 동기화 부담
- MEDIUM 4건: M-1 Provider Liquidity Layer 1 Python 적용 부담 (depcruise = JS/TS 도구) / M-2 Skill 예시 부재 / M-3 환경변수 실 사용처 부재 / M-4 옵션 3 동시 발효 위험
- LOW 4건

**7 조건**:
- C-1: Implementation/Runtime PASS 분리 명시 재확인
- C-2: MVP-0 ~ MVP-5 단계화 권고 등록
- C-3: 메타-순환 청산 템플릿화 권고 등록
- C-4: 공유 enumeration 추출 권고 (DRY)
- C-5: 부분 BLOCK 가능성 명시 (옵션 3 채택 시 1 게이트만 PARTIAL 가능)
- C-6: PoC Skill 1건 + Memory entry 1건 작성 권고
- C-7: 22 / 17 / 6 enumeration *유지* 권고 (단순화 효과 < 명시 가치)

### 2.4 외부 LLM 결과 (GPT-5.5 Thinking)

**판정**: ✅ APPROVE WITH CONDITIONS — Design Gate PASS 한정, 7 필수 조건

**핵심 관찰**:
- "Design Gate PASS" vs "Implementation Evidence PASS" vs "Operational Readiness PASS" 3-layer 분리 권고
- G2 = "거버넌스 사전조건 정의 PASS" 이지 "사전조건 충족 PASS" 아님 — GP-2~GP-6 Implementation Pending 명시 의무
- G3 = "Design PASS with Conditions" (Evidence Ledger 변조 방지 + approval provenance + signed commit MUST 상향)
- G4 = "Design PASS with Conditions" (canonical JSON / schema evolution / import declaration P2 v3 전 흡수)
- Skill `allowed_actions` (shell / network / db / git / docker) 너무 넓음 — 세분화 권고
- Gate enforcement layer (CI / hook / wrapper / branch protection) 도 보호 대상으로 확장 권고
- 1인 개발자용 MVP-0 ~ MVP-5 단계화 권고

**Gap-N (외부 LLM 단독 발견 — 내부 Agent 미언급)**:
- N-1: Human approval provenance 보강 (commit hash / timestamp / 승인 문구 / 승인 대상 artifact)
- N-2: Audit / Evidence Ledger 변조 방지 별도 T3 명시
- N-3: Network egress / external communication allowlist/denylist 정책
- N-4: Recovery / rollback / incident response 절차 보강
- N-5: Supply chain / dependency integrity 보호
- N-6: Skill permission granularity (shell allowlist / network domain·port / db read·write·migrate·admin / git read·status·diff·commit·tag·push / docker build·run·volume·socket)
- N-7: Gate enforcement layer 보호 확장 (CI/hook/wrapper/branch protection 변경도 T3)
- N-8: `~/.claude/global/` → `~/.ai-dev-template/global/` namespace 정리 권고

**7 필수 조건**:
- N-9.1: PASS 범위 명시 (Design Gate 한정)
- N-9.2: G2 상태 정정 (GP-1 흡수 / GP-2~GP-6 Implementation Pending)
- N-9.3: G4 P-1 / P-2 / P-3 흡수 (canonical JSON / schema evolution / import schema_version) — P2 v3 정식 채택 *전* 반드시
- N-9.4: Evidence Ledger + approval provenance 보강
- N-9.5: Skill permission 세분화
- N-9.6: Gate enforcement layer 보호
- N-9.7: 1인 개발자용 단계적 MVP 계획 추가

**메타 노트**:
- 약한 결론 유도 발견 ("통합 PASS 가 유리하다는 견해" / "내부 평가에서는 BLOCK 사유 아님") — 단 *심각한 결론 유도는 아님*
- 누락 정보 7건 enumeration (PASS 용어 체계 / Evidence Ledger 실 schema / CI 도구 / Hermes 실 권한 모델 / 사용자 승인 기록 방식 / PMO 격상 후 작업 범위 / target project 위협 모델)

---

## 3. Phase 3 — 교차 비교 (Cross-Comparison)

### 3.1 일치 (Consensus, 4/4 입력 동의)

| # | 일치 항목 | 입력 |
|---|---------|----|
| **CO-1** | **판정: APPROVE WITH CONDITIONS** (4/4 입력 만장일치) | A/B/C/GPT |
| **CO-2** | **Design/Governance Gate PASS 한정 + Implementation/Runtime PASS 분리** 의무 명시 | A C-1 / B C-1 / C C-1 / GPT N-9.1 |
| **CO-3** | **Hermes PMO 격상 / P2 v3 정식 채택 / ADR 본문 갱신 / archive / 실 runtime / 실 migration script 본 합의 범위 외** 반복 명시 | A C-6 / B C-8 / C 본문 / GPT 명시 |
| **CO-4** | **G2 = GP-1 PASS (G1b 흡수) / GP-2~GP-6 = Design PASS + Implementation Pending** 비대칭 명시 | A 본문 / B 본문 / C 본문 / GPT N-9.2 |
| **CO-5** | **1인 개발자 MVP-0 ~ MVP-5 단계화 권고** (한꺼번에 Implementation 진입 차단) | A W-1 추정 / B 본문 / C C-2 / GPT N-9.7 |
| **CO-6** | **단일 호스트 SPOF 의도적 수용 명시 + Multi-host 트리거 5건 명시** 적격 | A W-3 / B H-1 / C 본문 / GPT 5.5 |
| **CO-7** | **자기 작성 산출 자기 검토 한계 명시** + *사후 외부 LLM 충족* 패턴 답습 | A §5.1 / B §5.1 / C §5.1 / GPT 10.1 (내부 결론 유도 약 인지) |

### 3.2 부분 일치 (Partial, 3/4 또는 2/4 입력 동의)

| # | 부분 일치 항목 | 입력 |
|---|---------|----|
| **PA-1** | **G4 P-1 (RFC 8785 JCS) / P-2 (schema evolution) / P-3 (import schema_version) 흡수 — P2 v3 정식 채택 *전* 의무 또는 권고** | B C-?/ GPT N-9.3 (강조) / C M-1 인접 (Provider Liquidity Layer 1 Python 적용) — A 미명시 |
| **PA-2** | **Evidence Ledger + approval provenance 보강 (commit hash / timestamp / 승인 문구 / 승인 대상)** | B §2.7 / GPT N-9.4 (강조) — A/C 미명시 |
| **PA-3** | **Skill permission 세분화 (shell allowlist / network domain·port / db read·write·migrate / git / docker)** | GPT N-9.5 (강조 단독) — A/B/C 미언급 |
| **PA-4** | **Gate enforcement layer 보호 확장 (CI / hook / wrapper / branch protection 변경도 T3)** | GPT N-9.6 / B T3-2 (합의 보고서 사후 변조) 인접 — A/C 미명시 |
| **PA-5** | **22 / 17 / 6 enumeration 유지 vs 단순화** | C C-7 (유지 권고 명시) — GPT 단순화 권고 (Skill 필드 분리: Core required 9 + Governance 6 + Optional 2) — A/B 분류 / 통합 가능 후보 명시 정도 |
| **PA-6** | **메타-순환 청산 템플릿화 / 공유 enumeration 추출 (DRY)** | C C-3 / C-4 단독 — A/B/GPT 미언급 |
| **PA-7** | **부분 BLOCK 가능성 명시 (옵션 3 채택 시 1 게이트만 PARTIAL 가능)** | C C-5 단독 — A/B/GPT 미명시 |
| **PA-8** | **G3 §2.4 산술 오류 정정 (14/22 → 15/22)** | A C-4 / B C-6 — C/GPT 미언급 |

### 3.3 불일치 (Divergence, 입력 간 의견 차이)

| # | 불일치 항목 | 입력 + 의견 |
|---|---------|---------|
| **DI-1** | **enumeration 유지 vs 축소** | C 권고 *유지* (22 권한 / 17 필드 / 6 GP) — *명시 가치 > 절감 효과*. GPT 권고 *Skill 필드 분리* (Core required 9 + Governance 6 + Optional 2). **둘 다 enumeration 자체 *유지*** — GPT 권고는 *분류 강화* 까지로 일치 가능. 실질 불일치 0. |
| **DI-2** | **Provider Liquidity Layer 1 (depcruise vs Python 도구)** | C M-1 명시: depcruise = JS/TS 도구, Python 본 프로젝트에 `import-linter` + `ruff` 대안 권고. GPT 본문 명시 (Python AST 기반 provider SDK direct import 탐지 / Java/Kotlin / Docker/YAML/env / Skill 본문 문자열 탐지). **실질 일치** — 둘 다 Python AST 대안 권고. |

→ **실질 불일치 항목: 0건**. DI-1 / DI-2 모두 표면적 차이로 *실질 일치*.

### 3.4 누락 (Gap, 특정 입력만 언급)

#### 3.4.1 Agent A 단독 발견

- W-4 G4 §4.4 Layer 4 + Layer 5 미구현 — *MANDATORY* 등급이지만 PENDING 명시 (G4 본문 헤더 P0 조건 C-B 답습으로 명시되어 있으나 A 가 *구체 위치* 명시)
- W-8 G3 §2.5 #1 `.git/` author SPOF — W-3 의 *구체적 실현 경로* enumeration

#### 3.4.2 Agent B 단독 발견 (P15 / P16 / P17 후보)

- **P15 후보**: External-review 자료 위조 — GPT/Gemini 응답 본문이 Hermes 또는 Worker 가 위조 생성 — ADR-012 §2.1 원칙 7 (`agent="user"` 강제) 답습으로 차단되나 *현 hook 미구현*
- **P16 후보**: Skill `description` 본문 (markdown) 내 prompt injection 페이로드 — `inputs`/`outputs` 는 JSON Schema 검증되지만 `description` 자유 텍스트
- **P17 후보**: Memory `content` (자유 schema) 내 오염된 사실 (잘못된 ADR 인용 / 합의 결과 cross-reference)

#### 3.4.3 Agent C 단독 발견

- 메타-순환 청산 패턴 *템플릿화* — `docs/architecture/meta-cycle-clearance-template.md` 분리 권고
- 공유 enumeration 추출 — `docs/architecture/shared-enumerations.md` (DRY 원칙)
- 옵션 3 채택 시 *부분 BLOCK 가능성* 명시 — 1 게이트만 PARTIAL 처리 가능

#### 3.4.4 외부 LLM (GPT) 단독 발견 (Gap-N — 가장 가치 큼)

- **N-3 Network egress allowlist/denylist 정책** — GP-2 가 송신 redaction 까지만, *어떤 외부 endpoint 로 나갈 수 있는지* 정책 부재
- **N-4 Recovery / rollback / incident response 절차** — 자동 비활성화 + 컨테이너 정지 명시되어 있으나 *사고 후 복구 / 증거 보존 / 재승격 조건* 보강 필요
- **N-5 Supply chain / dependency integrity** — provider lock-in 차단되어 있으나 dependency pinning / checksum / CI 환경 신뢰 / external tool 업데이트 위험 별도 항목 부재
- **N-6 Skill permission granularity 세분화** — shell allowlist / network domain·port / db read·write·migrate·admin / git read·status·diff·commit·tag·push / docker build·run·volume·socket
- **N-7 Gate enforcement layer 보호 확장** — ADR / Gate 문서뿐 아니라 CI / hook / wrapper / branch protection 도 T3 보호
- **N-8 `~/.claude/global/` namespace 정리** — Claude Code 표준 디렉토리 충돌 (G4 P-5 자기 발견 답습) 보강

### 3.5 교차 비교 요약 매트릭스

| 분류 | 항목 수 | 입력 분포 |
|----|------|------|
| 일치 (Consensus, 4/4) | 7 | A/B/C/GPT 모두 |
| 부분 일치 (Partial, 2/4 또는 3/4) | 8 | 다양 |
| 불일치 (Divergence) | 0 (실질) | DI-1/DI-2 표면적 차이만 |
| 누락 — A 단독 | 2 | A 위치 enumeration |
| 누락 — B 단독 | 3 | P15/P16/P17 후보 |
| 누락 — C 단독 | 3 | 템플릿화 / DRY / 부분 BLOCK |
| 누락 — GPT 단독 (Gap-N) | 6 | N-3~N-8 (가장 가치 큼) |

**Phase 3 결론**: 4 입력 *판정 만장일치 (APPROVE WITH CONDITIONS)*. *조건 통합* 단계에서 일치 7 + 부분 일치 8 + 누락 (특히 Gap-N 6건) 흡수.

---

## 4. Phase 4 — 합의 도출 (Consensus Resolution)

### 4.1 최종 판정

```
✅ APPROVE WITH CONDITIONS
G2 + G3 + G4 Design/Governance Gate PASS 승격 적격 — 12 통합 조건 충족 의무
```

**4/4 입력 만장일치** + **실질 불일치 0건** + **모든 누락이 *조건* 으로 흡수 가능** + **BLOCK 사유 0건**.

### 4.2 12 통합 조건 (Consensus Conditions)

본 PASS 발효 후 *반드시 충족 또는 후속 합의 진입* 할 조건 12건:

#### C-1 (CO-2 답습) — PASS 범위 = Design/Governance Gate PASS 한정

본 PASS 는 *문서 정의 + 권위 위계 + 6 GP 정의 + 22 권한 분류 + 17 schema 정의 + JSONL 형식 + hash chain 다층 강제 사양* 의 *설계 승인* 한정. **Implementation/Runtime PASS / Operational Readiness PASS 는 본 PASS 에 포함되지 않는다** — 별도 합의 강제.

3-layer 분리 명시 (GPT 권고 답습):
- **Design Gate PASS** (본 합의 — 발효 ✅)
- **Implementation Evidence PASS** (별도 합의 — Pending)
- **Operational Readiness PASS** (별도 합의 — Pending)

#### C-2 (CO-4 + GPT N-9.2 답습) — G2 상태 비대칭 명시

| GP | 상태 |
|----|----|
| **GP-1** | ✅ **PASS** (G1b PASS evidence 흡수, (a)~(e) 5/5 충족) |
| **GP-2 ~ GP-6** | 🟡 **DESIGN PASS / IMPLEMENTATION PENDING** (조건 정의 완료 / 구현 evidence 미완료) |

본 비대칭은 G2 헤더 / §1.2.6.3 P10 enforcement Implementation Pending 명시 답습 + GPT N-9.2 강조. *향후 단축 표현 시 "G2 = PASS" 로 단축 silent loss 차단*.

#### C-3 (PA-1 + CO-5 답습) — G4 P-1 / P-2 / P-3 흡수 시점 명시

본 G4 DRAFT 검토 자기 발견 5 위험 중 P-1 (RFC 8785 JCS 직접 인용) + P-2 (schema 진화 정책 필드 제거/이름변경/타입변경) + P-3 (외부 import schema_version declaration) 흡수 시점:

- **P-1 흡수**: G4 정식 채택 시점 또는 P2 v3 정식 채택 *전*. ADR-012 §2.5 Primary + Fallback 답습 가능.
- **P-2 흡수**: G4 §10 변경 절차 보강 — 본 합의 후 단축 합의 또는 G4 정식 채택 시점.
- **P-3 흡수**: G4 §4.5 import 절차 보강 — Implementation/Runtime PASS 합의 영역 또는 별도 합의.

본 3건은 *BLOCK 사유 아님* — 본 합의 PASS 효력에는 영향 없음. 단 *P2 v3 정식 채택 전 흡수 의무* 권고.

#### C-4 (PA-2 + GPT N-9.4 답습) — Evidence Ledger + approval provenance 보강

본 통합 합의 발효 후 Implementation/Runtime PASS 합의 시점에 의무 흡수:

**Evidence Ledger schema 보강** (GPT 7.3 답습):
- evidence id / artifact path / command·tool result / timestamp / actor / commit hash / previous evidence hash / approval reference

**Approval provenance 보강**:
- T2/T3 사용자 승인 = commit hash + timestamp + 승인 문구 + 승인 대상 artifact 4-tuple 명시
- 사용자 host 침해 시 위변조 위험 (G3 §5.5.1 (ii)) 의도적 수용 + Multi-host 전환 시 signed commit MUST 승격

#### C-5 (PA-3 + PA-4 + GPT N-9.5/N-9.6 답습) — Skill permission 세분화 + Gate enforcement layer 보호 확장

**Skill permission 세분화 (G4 정식 채택 또는 Implementation 시점)**:
- `shell` → 기본 금지 + 허용 command allowlist
- `network` → domain / method / port 단위 제한
- `db` → read / write / migrate / admin 분리
- `git` → read / status / diff / commit / tag / push 분리
- `docker` → build / run / volume / socket 접근 분리
- timeout / memory / CPU / filesystem mount 제한 명시

**Gate enforcement layer 보호 확장 (G3 §2.5 보호 대상 확장)**:
- 현 15건 (ADR / Gate 문서 / docs/decisions / docs/architecture / docs/constitution / Evidence Ledger / 등) 외
- 추가: CI workflow / pre-commit hook / wrapper / sandbox / permission evaluator / branch protection 설정 모두 T3 보호
- 변경 시 사용자 명시 + ADR Amendment 절차

#### C-6 (PA-5 + C-7 답습) — Enumeration 유지 + MVP 분리 강화

본 합의는 **22 권한 / 17 schema / 6 GP enumeration *유지*** 권고:
- 22 권한 enumeration *명시 가치* > 단순화 절감 효과
- 17 필드 §3.6 MVP 분리 (12 필수 / 1 MVP-필수 / 4 MVP-권장) 이미 충분
- 6 GP P1~P8 경로 매핑 1:1 가독성 유지

단, **MVP 분리 강화** (Agent C #1 답습):
- 22 권한 → "MVP 필수 차단 (T3 6건 핵심)" + "MVP 권장 차단 (T2/T3 8건)" 분리
- 17 필드 → 이미 §3.6 분류 / GPT 권고 (Core 9 / Governance 6 / Optional·constrained 2) 추가 layer 가능
- 본 분리는 *Implementation 진입 우선순위* 결정 보조

#### C-7 (CO-5 + Agent C C-2 + GPT N-9.7 답습) — MVP-0 ~ MVP-5 단계화 권고 등록

본 합의 PASS 후 Implementation 진입 결정 시점에 *한꺼번에 시도 차단* + *순서 명시*:

| 단계 | 최소 구현 | 시점 |
|----|--------|----|
| **MVP-0** | 본 통합 PASS 시점 (Design/Governance Gate PASS 발효) | ✅ 본 합의 |
| **MVP-1** | G2 GP-3 + GP-5 (gitleaks + detect-secrets + depcruise/import-linter 실 구현) | Implementation 1차 합의 |
| **MVP-2** | G2 GP-2 + G4 §4.4 Layer 4 (log canary + canonical JSON + R-6 workflow ledger 검증) | Implementation 2차 합의 |
| **MVP-3** | G2 GP-6 + G4 §4.5 PoC (migration script 1건 라운드트립) | Implementation 3차 합의 |
| **MVP-4** | G3 운영 hook (filesystem read-only + Hermes-originated commit auto-reject pre-commit) | Implementation 4차 합의 |
| **MVP-5** | G4 §4.4 Layer 3 + Layer 5 (Signed commit + External anchor) | Multi-host 전환 시점 |
| **MVP-6 (PMO 격상)** | 4 게이트 모두 Implementation PASS + 외부 LLM 1+ + 인간 전문 리뷰 + 사용자 명시 | 별도 합의 |

본 단계화는 *권고 등록 한정* — 본 합의 범위 외 강제 효력 없음.

#### C-8 (Agent B H-1 + Agent C C-5 답습) — 부분 BLOCK 가능성 명시

옵션 3 (G2+G3+G4 통합 PASS) 채택 시, *향후 1 게이트만 결함 발견 시 PARTIAL 처리 가능* 명시:
- G2 / G3 / G4 중 일부 본문 갱신 (단순 오타 + 단축 합의 영역) 은 *나머지 게이트 PASS 효력 유지*
- T3 영역 변경 (§2.2 권한 표 / §4.3 합의 매트릭스 / §5 Evidence 결정) 은 *3 게이트 동시 재합의* 의무

#### C-9 (Agent B C-2/C-3 답습) — 트리거 자동 검출 + Hermes-originated 판정 알고리즘 Implementation 합의 진입

**G3 §5.5.3 / G2 §9.5.2 트리거 5건 자동 검출 hook 미구현** + **Hermes-originated commit auto-reject 판정 알고리즘 미명시** 모두 Implementation/Runtime PASS 합의에 포함 의무:
- 5 트리거 자동 검출 = git hook + audit log + alerting
- Hermes-originated 판정 = git author / committer + Hermes audit log cross-reference 알고리즘

#### C-10 (Agent B C-4/C-5 답습) — P9 / P11 / P12 deferred + P15 / P16 / P17 신규 후보 등록

**현 P 정식 등록 상태** (2026-05-07):
- P1~P8 정식 (G2 §1.2)
- P10 Evidence Forgery 정식 등록 (G2 §1.2.6, ADR-012 권위)

**Deferred candidates 처리 시점 명시**:
- **P9 Prompt Injection**: GP-4 PoC 진입 시점에 정식 등록 검토
- **P11 Supply-chain Compromise**: Hermes PMO 격상 *전* 권장 (Agent B 답습)
- **P12 Memory Poisoning Side-channel**: G4 Implementation/Runtime PASS 합의 시점

**신규 후보 등록 (Agent B 자기 발견)**:
- **P15 후보**: External-review 자료 위조 — ADR-012 §2.1 원칙 7 답습으로 흡수
- **P16 후보**: Skill `description` markdown prompt injection — Skill 등록 사용자 review 단계 보강
- **P17 후보**: Memory `content` 오염 — diff hook + 사용자 명시 commit 강제

본 후보 6건 처리는 각 정식 등록 시점 별도 합의.

#### C-11 (PA-8 + L-1 답습) — G3 §2.4 산술 오류 후속 정정

G3 §2.4 마지막 줄 "자동 롤백 14/22 (T1 #1~#7 외 전부)" → **15/22** (실제 = #8 + #9~#22 = 15). 본문 의미 ("T1 #1~#7 외 전부" = 22-7=15) 정확하므로 *해석 위험 0*. G3 §10 "단순 오타: 사용자 단독 결정 가능" 답습으로 본 합의 후 단순 commit 가능.

#### C-12 (CO-7 + Agent B C-7 + Agent C C-3/C-4 + GPT 10.1/10.2 답습) — 메타-한계 명시 + 후속 외부 LLM 검증

**메타-한계 명시**:
- 본 합의 4 입력 중 3건 (Agent A/B/C) 동일 컨텍스트 — 자기참조 + 메타 편향 위험 잔존
- 외부 LLM 1건 (GPT-5.5 Thinking) 충족 — G3 §4.4.2 *통합 합의 시 외부 LLM 1+ 권장* 답습
- *Hermes PMO 격상* 합의 시점에는 **외부 LLM 1+ *필수*** + **인간 전문 리뷰** 의무 (P2 v3 §11.1 답습)

**후속 검증 권고**:
- C-12-a: cross-vendor 응답의 *distinct 정도* 사후 검증 (Agent B C-7 답습) — Hermes PMO 격상 합의 시점에 vendor 다양성 확인
- C-12-b: 메타-순환 청산 패턴 *템플릿화* (Agent C C-3) + 공유 enumeration 추출 (Agent C C-4) — 별도 합의 영역 권고 등록
- C-12-c: 약한 결론 유도 (GPT 10.1 명시 — "통합 PASS 가 유리하다는 견해" / "내부 평가에서는 BLOCK 사유 아님") *심각하지 않음* 판정 답습. 향후 외부 검토 의뢰서에서 *결론 유도 약화* 검토

### 4.3 Gap-N 흡수 처리 (외부 LLM 단독 발견 6건)

| Gap | 흡수 위치 | 처리 시점 |
|----|--------|------|
| **N-3** Network egress allowlist/denylist | GP-2 정식 채택 시점에 §4.7 추가 또는 별도 GP 신설 검토 | Implementation/Runtime PASS 시 |
| **N-4** Recovery / rollback / incident response 절차 | G2 §1.2.6 P10 enforcement 보강 + G3 §3 위험 차단 §X.5 (Rollback) 답습 확장 | Implementation/Runtime PASS 시 |
| **N-5** Supply chain / dependency integrity | P11 deferred candidate 정식 등록 시점 (C-10 답습) — Hermes PMO 격상 *전* 권장 | P11 정식 등록 합의 |
| **N-6** Skill permission granularity 세분화 | G4 §3.1 #9 `allowed_actions` 본문 정밀화 — C-5 답습 | G4 정식 채택 또는 Implementation 시 |
| **N-7** Gate enforcement layer 보호 확장 | G3 §2.5 보호 대상 enumeration 추가 — C-5 답습 | G3 정식 채택 또는 Implementation 시 |
| **N-8** `~/.claude/global/` namespace 정리 | G4 P-5 자기 발견 답습 — Implementation/Runtime PASS 영역 | Implementation 시 |

본 6건 모두 BLOCK 사유 아님 — *후속 합의 영역* 으로 분류. 본 합의 결과에 *흡수 시점* 명시 기록.

### 4.4 본 합의 PASS *발효* 시 변경 사항

본 합의 PASS APPROVE WITH CONDITIONS 결과로 *발효* 되는 변경:

| # | 변경 | 처리 |
|---|----|----|
| 1 | G2 / G3 / G4 헤더 *Design/Governance Gate PASS* (Bundled, 2026-05-07) 명시 | 별도 commit (사용자 명시 결정 후) |
| 2 | G2 / G3 / G4 본문에 본 합의 보고서 cross-reference 추가 | 별도 commit |
| 3 | G2 §1.2.6.3 P10 enforcement / G3 §0.1 / G4 §0.1 헤더 "Design/Governance Gate PASS 한정 — Implementation/Runtime PASS 미포함" 명시 | 본 합의 cross-reference로 명시 충분 |
| 4 | P2 v3 DRAFT §3 4-게이트 상태표 갱신 (G2/G3/G4 = Design Gate PASS) | 별도 commit |
| 5 | INDEX / CONTEXT.md 갱신 | 별도 commit |
| 6 | SESSION 로그 갱신 | 별도 commit |
| 7 | G3 §2.4 산술 오류 정정 (14/22 → 15/22, C-11 답습) | 별도 commit |

본 합의 PASS *발효* 시 *발생하지 않는* 변경 (사용자 명시 금지 답습):
- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 선언
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신
- ❌ P2 v2 archive 처리
- ❌ system-identity-prequel.md archive 처리
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
- ❌ Tier-2 / Tier-3 catalog 확장

---

## 5. 메타 편향 자기진단

### 5.1 본 합의의 메타 편향 위험

본 합의는 G3 §4.4.2 + G4 §11.1 / §0.3 #4 답습의 *실현*:
- "통합 합의 시 외부 LLM 1+ 권장" — GPT-5.5 Thinking 응답 회수로 충족
- "자기 작성 산출 자기 검토 한계 명시" — Agent A §5 / B §5 / C §5 모두 명시
- 메타-순환 청산 (Agent C C-3 답습) — 본 합의 자체가 §4 자기참조 차단의 *적용 대상*

### 5.2 5 통제 답습

| # | 통제 수단 | 본 합의 적용 |
|---|---|----|
| 1 | 사용자 명시 절차 답습 | ✅ 옵션 3 채택 + 7 절차 + 금지 사항 6건 |
| 2 | 직전 단축 합의 패턴 답습 | ✅ P2 v3 / G2 / G3 / G4 DRAFT 검토 4건 답습 |
| 3 | 13 항목 답습 (G4 검토) + 7 질문 답습 (외부 의뢰서) + 4 입력 교차 비교 | ✅ §3.1~§3.5 매트릭스 |
| 4 | 자기 발견 잠재 위험 명시 (각 Agent §3 P-N 형식 + GPT 10.2 누락 정보 7건) | ✅ 누락 enumeration §3.4 |
| 5 | 본 합의가 *하지 않는* 것 명시 (§0.3 + §4.4 발생하지 않는 변경) | ✅ 8 항목 + 6 항목 |

### 5.3 본 합의의 한계

- **자기 작성 산출 자기 검토 한계 잔존**: Agent A/B/C 가 본 프로젝트 동일 컨텍스트 — *4 입력 중 1 입력만* 외부 LLM (GPT-5.5 Thinking)
- **외부 LLM 1건 한정**: Gemini / Claude 인접 컨텍스트 등 추가 cross-vendor 시점 *부재* — Hermes PMO 격상 합의 시점에 추가 vendor 필수
- **§3 자기 발견 + Gap-N 의 *완전성* 한계**: 본 Reviewer 시야 한정 — 외부 검토자 / 인간 전문 리뷰가 추가 발견 가능
- **C-7 MVP-0 ~ MVP-5 단계화 권고의 *권위 한계***: 본 합의 *범위 외* (Implementation/Runtime PASS 합의 영역). 권고 등록 한정.
- **약한 결론 유도 위험 (GPT 10.1 명시)**: 본 합의 본문에 *옵션 3 권고 결론* / *통합 PASS 가 유리* / *BLOCK 사유 아님* 표현 잔존 — 의도적이나 향후 외부 검토 의뢰서에서 *결론 유도 약화* 검토 의무.

### 5.4 본 합의 PASS 판정이 *트리거하지 않는* 것

본 §6 결론 PASS 판정은 다음을 *트리거하지 않는다*:

- ❌ G2 / G3 / G4 Implementation/Runtime PASS
- ❌ Operational Readiness PASS
- ❌ Hermes PMO 격상
- ❌ P2 v3 정식 채택
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신
- ❌ P2 v2 / system-identity-prequel archive
- ❌ Phase 진입 결정 (Phase 1 acceptance 이후 Phase 2 진입은 별도)
- ❌ 실 runtime 코드 구현
- ❌ 실 migration script 구현
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ Provider Liquidity 4-way Multi-layer Defense Layer 1~4 실 구현 (depcruise / import-linter 등)
- ❌ Hash chain Layer 4 CI 회귀 검증 step 추가
- ❌ Hash chain Layer 5 External anchor 운영

본 합의 PASS 판정은 *오직* "G2 + G3 + G4 Design/Governance Gate PASS 승격 + P2 v3 정식 채택 합의 *진입 단계* 적격" 의미.

---

## 6. 최종 판정

### 6.1 판정

```
✅ APPROVE WITH CONDITIONS
G2 + G3 + G4 Design/Governance Gate PASS 승격 (Bundled, 2026-05-07)
4/4 입력 만장일치 — 12 통합 조건 충족 의무
```

### 6.2 입력 분포

| # | 입력 | 판정 | 조건 수 |
|---|----|----|----|
| 1 | Agent A (구현/운영) | APPROVE WITH CONDITIONS | 6 |
| 2 | Agent B (안전/거버넌스) | APPROVE WITH CONDITIONS | 8 + 4 권고 |
| 3 | Agent C (대안/단순화) | APPROVE WITH CONDITIONS | 7 |
| 4 | 외부 LLM (GPT-5.5 Thinking) | APPROVE WITH CONDITIONS | 7 필수 + 5 누락 정보 |

**합산**: 4/4 APPROVE WITH CONDITIONS + 0/4 BLOCK + 0/4 PARTIAL + 0/4 APPROVE 무조건. **만장일치 + 실질 불일치 0건**.

### 6.3 12 통합 조건 요약

| # | 조건 | 처리 시점 |
|---|----|------|
| **C-1** | PASS 범위 = Design/Governance Gate PASS 한정 (3-layer 분리) | 본 PASS 발효 |
| **C-2** | G2 상태 비대칭 명시 (GP-1 PASS / GP-2~GP-6 Implementation Pending) | 본 PASS 발효 |
| **C-3** | G4 P-1 (RFC 8785 JCS) / P-2 (schema evolution) / P-3 (import schema_version) 흡수 시점 명시 | P2 v3 정식 채택 *전* |
| **C-4** | Evidence Ledger schema + approval provenance 보강 | Implementation/Runtime PASS 합의 |
| **C-5** | Skill permission 세분화 + Gate enforcement layer 보호 확장 | G4 정식 채택 또는 Implementation 시 |
| **C-6** | Enumeration 유지 (22 / 17 / 6) + MVP 분리 강화 | 본 PASS 발효 + Implementation 진입 시 |
| **C-7** | MVP-0 ~ MVP-5 단계화 권고 등록 | Implementation 진입 결정 시 |
| **C-8** | 부분 BLOCK 가능성 명시 (옵션 3 단축 합의 영역 한정) | 본 PASS 발효 |
| **C-9** | 트리거 자동 검출 + Hermes-originated 판정 알고리즘 Implementation 합의 진입 | Implementation/Runtime PASS 합의 |
| **C-10** | P9 / P11 / P12 deferred + P15 / P16 / P17 신규 후보 처리 시점 명시 | 각 정식 등록 시점 |
| **C-11** | G3 §2.4 산술 오류 후속 정정 (14/22 → 15/22) | 본 PASS 발효 후 단축 commit |
| **C-12** | 메타-한계 명시 + 후속 외부 LLM 검증 (Hermes PMO 격상 시 추가 vendor + 인간 전문 리뷰 필수) | Hermes PMO 격상 합의 시 |

### 6.4 Gap-N 흡수 처리 6건 (외부 LLM 단독 발견)

| Gap | 흡수 시점 |
|----|------|
| N-3 Network egress allowlist/denylist | Implementation/Runtime PASS 시 |
| N-4 Recovery / rollback / incident response | Implementation/Runtime PASS 시 |
| N-5 Supply chain / dependency integrity | P11 정식 등록 시 (PMO 격상 *전* 권장) |
| N-6 Skill permission granularity | G4 정식 채택 또는 Implementation 시 |
| N-7 Gate enforcement layer 보호 확장 | G3 정식 채택 또는 Implementation 시 |
| N-8 `~/.claude/global/` namespace 정리 | Implementation 시 |

---

## 7. 후속 작업 (본 합의 *이후*)

본 합의 APPROVE WITH CONDITIONS 결과 + 사용자 명시 결정 후 다음 단계 진입 적격:

### 7.1 단기 (본 합의 발효 직후 — 사용자 명시 결정 후 별도 commit)

| # | 작업 | 산출 |
|---|----|----|
| 1 | 본 합의 보고서 별도 commit | `docs(review): record G2 G3 G4 integrated gate adoption full 3+1 consensus` |
| 2 | G2 / G3 / G4 헤더 *Design/Governance Gate PASS* (Bundled, 2026-05-07) 명시 | 별도 commit |
| 3 | G2 / G3 / G4 본문 본 합의 cross-reference 추가 | 별도 commit |
| 4 | P2 v3 DRAFT §3 4-게이트 상태표 갱신 | 별도 commit |
| 5 | G3 §2.4 산술 오류 정정 (14/22 → 15/22, C-11 답습) | 별도 commit |
| 6 | INDEX / CONTEXT.md 갱신 | 별도 commit |
| 7 | SESSION 로그 갱신 | 별도 commit |

### 7.2 중기 (P2 v3 정식 채택 합의 *진입 단계*)

| # | 작업 | 시점 |
|---|----|----|
| 8 | G4 P-1 / P-2 / P-3 흡수 (C-3 답습) | P2 v3 정식 채택 *전* |
| 9 | P2 v3 정식 채택 합의 형태 결정 (Reviewer-only 단축 / 풀 3+1 / 외부 LLM 추가 vendor 등) | 사용자 명시 결정 |
| 10 | P2 v3 정식 채택 합의 + ADR-008 / ADR-009 / ADR-010 / ADR-011 cross-reference 갱신 검토 | 별도 합의 |
| 11 | P2 v2 / system-identity-prequel.md archive 처리 검토 | P2 v3 정식 채택 후 별도 결정 |

### 7.3 장기 (Implementation/Runtime PASS 합의 — MVP-1 ~ MVP-5)

| # | 작업 | 시점 |
|---|----|----|
| 12 | MVP-1 (G2 GP-3 + GP-5 실 구현) | 별도 합의 + 사용자 명시 결정 |
| 13 | MVP-2 (G2 GP-2 + G4 §4.4 Layer 4) | 별도 합의 |
| 14 | MVP-3 (G2 GP-6 + G4 §4.5 PoC) | 별도 합의 |
| 15 | MVP-4 (G3 운영 hook) | 별도 합의 |
| 16 | MVP-5 (G4 §4.4 Layer 3 + Layer 5) | Multi-host 전환 시점 |
| 17 | P9 / P11 / P12 deferred candidates 정식 등록 (특히 P11 PMO 격상 *전*) | 각 정식 등록 합의 |
| 18 | P15 / P16 / P17 신규 후보 처리 검토 | 후속 합의 |
| 19 | 메타-순환 청산 템플릿화 (Agent C C-3) + 공유 enumeration 추출 (Agent C C-4) | 별도 합의 권고 등록 |
| 20 | Network egress / Recovery / Supply chain / Skill permission granularity / Gate enforcement 보강 (Gap-N 6건) | Implementation 시점 분산 |

### 7.4 Hermes PMO 격상 (MVP-6 — 최종, 별도 합의 의무)

| # | 의무 조건 (P2 v3 §2.6.1 12 조건 + 본 합의 C-12 답습) |
|---|---|
| 21 | 4 게이트 모두 Implementation/Runtime PASS 충족 |
| 22 | 외부 LLM 1+ (현 1건 충족) + 추가 vendor 1+ 필수 (Gemini / Claude family 외) |
| 23 | 인간 전문 리뷰 (Human-in-the-loop) — P2 v3 §11.1 답습 |
| 24 | 사용자 명시 결정 (T2 + ADR Amendment) |
| 25 | SPOF Multi-host 전환 트리거 (5) 의무 발동 — G3 §5.5.3 답습 |

본 합의 PASS *자체* 가 *MVP-6 (PMO 격상) 합의 진입 trigger 아님*. 본 합의는 *MVP-0 = Design/Governance Gate PASS* 완료까지.

---

## 8. 본 합의 보고서 commit 절차

본 결론 APPROVE WITH CONDITIONS에 따라 다음 단일 파일을 별도 commit으로 처리:

```
docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md
```

commit 메시지:
```
docs(review): record G2 G3 G4 integrated gate adoption full 3+1 consensus
```

본 commit에 포함하지 *않는* 항목 (사용자 명시 답습):
- G2 / G3 / G4 본문 갱신 (별도 후속 commit)
- P2 v3 DRAFT 본문 갱신 (별도 후속 commit)
- ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 갱신
- P2 v2 / system-identity-prequel archive 처리
- INDEX / CONTEXT 갱신 (별도 후속 commit)
- SESSION 로그 갱신 (별도 후속 commit)
- Hermes PMO 격상 선언
- 실 runtime 코드 / 실 migration script 구현

---

## 9. 본 합의의 변경 절차

본 합의 보고서는 *합의 완료 후* 다음 절차로 변경:

| 변경 유형 | 절차 |
|--------|----|
| 단순 오타 / 문구 정리 | 사용자 단독 결정 가능 |
| 12 조건 본문 명세 갱신 | 단축 합의 (Reviewer-only) — 단, 조건 *추가/삭제* 는 풀 3+1 |
| §3 교차 비교 매트릭스 갱신 | 단축 합의 — 단, 입력 *추가* (예: 추가 vendor 응답 회수) 는 풀 3+1 또는 본 합의 §X 부록 추가 |
| §4 합의 도출 본문 갱신 | **풀 3+1 합의 + ADR Amendment 절차** (T3 변경 — 합의 결과 자체 변경) |
| §6 최종 판정 변경 (예: APPROVE WITH CONDITIONS → PARTIAL → BLOCK) | **풀 3+1 + 외부 LLM 1+ 필수 + ADR Amendment 절차** (격상 통합 합의 답습) |

---

**합의일**: 2026-05-07
**합의 형태**: 풀 3+1 (Agent A + B + C + Reviewer) + 외부 LLM 1건 (GPT-5.5 Thinking)
**판정**: ✅ APPROVE WITH CONDITIONS (4/4 입력 만장일치 + 12 통합 조건 + Gap-N 6건 흡수 처리 명시)
**합의 권위**: 본 통합 합의 = G3 §4.4.2 통합 합의 시 외부 LLM 1+ 권장의 *실현* + Hermes PMO 격상 합의 패턴의 *축약 시연*
**다음 단계**: 본 합의 보고서 별도 commit → G2/G3/G4 헤더 갱신 + P2 v3 DRAFT 상태 갱신 + G3 §2.4 산술 오류 정정 등 후속 commit (사용자 명시 결정 후)

**금지 사항** (사용자 명시 답습, 본 합의 *발효* 시에도 변동 없음):
- ❌ Hermes PMO 격상 선언 자동
- ❌ P2 v3 정식 채택 선언 자동
- ❌ ADR-008 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ 실 runtime 코드 자동 구현
- ❌ 실 migration script 자동 구현
- ❌ Tier-2 / Tier-3 catalog 자동 확장
