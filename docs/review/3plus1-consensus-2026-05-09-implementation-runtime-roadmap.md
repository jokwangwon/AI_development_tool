# Implementation / Runtime PASS Roadmap 단축 합의 보고서 (Reviewer-only)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 ("이번 작업은 구현 착수 전 roadmap 작성이므로 Reviewer-only 단축 검토로 충분")
**합의 일자**: 2026-05-09 (후속 15 — Implementation/Runtime PASS roadmap)
**검토 대상**: `docs/architecture/implementation-runtime-roadmap.md` (DRAFT) — Implementation/Runtime PASS 작업 분해 + 우선순위 결정
**판정**: ✅ **APPROVE (단축 합의 — Reviewer-only) — roadmap 권위 권고 발행 적격, 5/5 풀 3+1 승격 트리거 0건 발화**

---

## 0. 사전 점검

### 0.1 가동 사유

ADR-010/011 후속 보강 검토 (2026-05-09 후속 14) 분기 A 채택 → Implementation/Runtime PASS 작업 진입 적격 → 사용자 명시 결정 답습 ("Implementation/Runtime PASS 작업 분해 및 우선순위 결정").

**사용자 명시 결정 답습**:
- 작업명 = "Implementation/Runtime PASS 작업 분해 및 우선순위 결정"
- 목적 = "G2 GP-2~GP-6 / G3 / G4 작업 한 번에 착수 X, 먼저 작업 쪼개기"
- 산출 = `docs/architecture/implementation-runtime-roadmap.md` (사용자 첫 권고 경로 답습)
- 검토 형태 = Reviewer-only 단축 검토 우선 — 5 풀 3+1 승격 트리거 1+ 발화 시 풀 3+1 승격
- 사용자 명시 표 컬럼: Area / Item / Type / Dependency / Evidence Required / PASS Criteria / Risk / Suggested Order
- 사용자 명시 5 우선순위 판단 기준 (보안 위험 / 기존 PoC 재사용 / 선행 조건 / CI 자동화 / PMO 격상 연결)
- 사용자 예상 8 우선순위 명시 + Claude 재평가 권고

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (roadmap = 권고 한정, 각 항목 PASS 별도 합의) | ✅ 사용자 명시 답습 |
| 직전 합의 (ADR-010/011 후속 보강 검토, 후속 14) 패턴 답습 | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 | ✅ §0.1 답습 |
| **5 풀 3+1 승격 트리거 발화 0건** | ✅ §2 답습 |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = roadmap 작성자. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘**:
1. 사후 외부 LLM 충족 — P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업
2. 격상 전 면제 — Hermes PMO 격상 *전*
3. 합의 권위 내부 변경 — 본 검토 = 후속 14 분기 A 답습
4. 자기 작성 한계 명시 — 본 §0.3 + §3 명시

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ |
| Implementation/Runtime PASS 자동 선언 | ❌ |
| 실 runtime code / migration script / hook 구현 | ❌ |
| ADR 본문 자동 갱신 | ❌ |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ |
| **roadmap 우선순위 자동 *고정*** | ❌ (사용자 명시 결정 + 각 그룹 별 합의 영역) |

---

## 1. roadmap 평가 (사용자 명시 항목 답습)

### 1.1 사용자 명시 표 컬럼 충족

| 컬럼 | 충족 |
|----|----|
| Area | ✅ G2 / G3 / G4 |
| Item | ✅ G2 GP-2~GP-6 (5) + G3 5 영역 + G4 7 영역 = 17 항목 |
| Type | ✅ PoC / CI / hook / wrapper / sandbox / library 등 |
| Dependency | ✅ 각 항목 ADR / SDD / R-* / G* cross-reference |
| Evidence Required | ✅ ADR-011 §2.1 (a)~(e) 5조건 답습 + Evidence 5 형식 |
| PASS Criteria | ✅ 정량 기준 (예: 100% BLOCK, 100% PASS, 라운드트립 hash 일치) |
| Risk | ✅ HIGH / MEDIUM-HIGH / MEDIUM 등급 |
| Suggested Order | ✅ Order 1 ~ 11 (그룹 A ~ I 분류) |

→ **8/8 컬럼 모두 충족**.

### 1.2 사용자 명시 5 우선순위 판단 기준 답습

| # | 기준 | 본 roadmap 답습 |
|---|------|---|
| 1 | 보안 위험이 큰 것 | ✅ §1 5 기준 가중치 — HIGH (3) |
| 2 | 기존 PoC 패턴 재사용 가능 | ✅ R-2 / R-4.1 / R-2-5 / R-6 / R-7 답습 명시 |
| 3 | 다른 작업의 선행 조건 | ✅ 그룹 A (Order 1) = 모든 작업의 root 의존성 명시 |
| 4 | CI 자동화 쉬움 | ✅ 각 항목 (d) 자동 회귀 검증 경로 명시 |
| 5 | Hermes PMO 격상 조건 직접 연결 | ✅ P2 v3 §2.6.1 12 조건 답습 |

→ **5/5 기준 모두 답습**.

### 1.3 사용자 예상 8 우선순위 vs Claude 재평가

| 사용자 예상 | 본 roadmap | 평가 |
|----|----|----|
| 1. G2 GP-5 Provider Adapter Enforcement | 1. (동일) | ✅ |
| 2. G3 Evidence 없는 PASS 차단 / commit auto-reject | 2. (동일, tie) | ✅ |
| 3. G4 JSONL hash chain / round-trip PoC | 3. (동일, tie + JCS canonical 동시) | ✅ + 보강 |
| 4. G2 GP-3 Credential / Secret Hygiene | 4. (동일) | ✅ |
| 5. G2 GP-2 Egress Redaction | 5. (동일) | ✅ |
| 6. G2 GP-4 External Input Validation | 6. (동일, tie + G4 schema validation) | ✅ + 보강 |
| 7. G2 GP-6 Memory/Skill Migration | 7. (동일) | ✅ |
| 8. G3 Skill escalation / runtime wrapper | 8. (동일) | ✅ |
| (사용자 미명시) | 9 G3 합의 자기참조 차단 + G4 Memory boundary hook | 본 roadmap 신규 추가 |
| (사용자 미명시) | 10 G4 Migration script (ADR-014 발행 trigger) | 본 roadmap 신규 추가 |
| (사용자 미명시) | 11 G3 22 권한 분해 — 별도 분해 후속 합의 | 본 roadmap 신규 추가 |

→ **사용자 예상 8 우선순위 = 모두 유지** + 본 roadmap 추가 3 항목 (Order 9 ~ 11) = 신규 영역. **사용자 의도 답습 + 보강**.

### 1.4 그룹 A ~ I 동시 진행 가능 분류

본 roadmap 권고 9 그룹 분류 — 의존성 0건 + 격리 PoC 패턴 답습 영역 병렬 작업 효율 ↑:

- **그룹 A (Order 1)**: G2 GP-5 (root 의존성)
- **그룹 B (Order 2 tie)**: G3 commit auto-reject + Evidence 없는 PASS 차단
- **그룹 C (Order 3 tie)**: G4 JSONL hash chain + JCS canonical + Round-trip PoC
- **그룹 D (Order 4 + 5)**: G2 GP-3 + GP-2
- **그룹 E (Order 6 tie)**: G2 GP-4 + G4 schema validation
- **그룹 F (Order 7)**: G2 GP-6
- **그룹 G (Order 8 + 9 tie)**: G3 Skill escalation + G3 자기참조 차단 + G4 Memory boundary hook
- **그룹 H (Order 10)**: G4 Migration script (ADR-014 발행 합의 + Implementation PASS PoC 완료 후)
- **그룹 I (Order 11)**: G3 22 권한 분해 (별도 분해 후속 합의)

→ **9 그룹 분류 = 17 항목 효율 분배**.

### 1.5 합의 형태 권고 (그룹 별)

| 그룹 | 합의 형태 |
|----|----|
| 그룹 A ~ G | 단축 합의 (Reviewer-only) + PoC evidence |
| **그룹 H** | **풀 3+1 + 외부 LLM 1+** (ADR-014 신규 발행) |
| **그룹 I** | **풀 3+1 + 외부 LLM 1+** (G3 22 권한 분해) |

→ **단축 7 그룹 + 풀 3+1 2 그룹** 적정 분배.

### 1.6 PASS 기준 통합 매트릭스

본 roadmap §6 답습:
- ADR-011 §2.1 (a)~(e) 5조건 답습 (모든 항목 의무) — (a) 동등 이상 보안 결과 + (b) 격리 PoC + (c) ADR/SDD 권위 + (d) 자동 회귀 + (e) 합의 APPROVE
- Rollback Trigger 9 항목 (R-1 ~ R-9) 명시
- Evidence Required 5 형식 (Markdown / JSONL ledger / Docker isolation log / GitHub Actions run / 합의 보고서)

→ **PASS 기준 통합 매트릭스 = 권위 위계 + ADR-011 모법 답습 충실**.

---

## 2. 5 풀 3+1 승격 트리거 검증 (사용자 명시 답습)

| # | 트리거 | 본 검토 | 발화 |
|---|----|----|----|
| 1 | **Hermes PMO 격상 조건 자체 변경** | 본 roadmap = P2 v3 §2.6.1 12 조건 직접 답습, 변경 0건 | ❌ 0 |
| 2 | **G2 / G3 / G4 Design PASS 의미 변경** | 본 roadmap = Implementation/Runtime PASS 분해 한정, Design PASS 의미 변경 0건 | ❌ 0 |
| 3 | **Implementation PASS 기준 완화** | ADR-011 §2.1 (a)~(e) 5조건 답습 의무 + R-2/R-4.1 PoC 패턴 답습 + Evidence 5 형식 의무 — 기준 강화 (완화 0건) | ❌ 0 |
| 4 | **5 영구 핵심 제약 약화 가능성** | roadmap = 권고 한정, 5 제약 직접 답습 (Provider Liquidity 5-way / Hermes ≠ root of trust 5 layer / 메타포 강제 금지 / T3 / 수단/목적 분리). 약화 0건 | ❌ 0 |
| 5 | **ADR-011 §2.1 (a)~(e) 조건 충돌** | 본 roadmap §6.1 = ADR-011 §2.1 (a)~(d) + (e) 5조건 직접 답습 표 명시. 충돌 0건 | ❌ 0 |

→ **5/5 트리거 0건 발화** → **단축 합의 (Reviewer-only) 적격** 확정.

---

## 3. 메타 편향 자기진단

### 3.1 본 검토자의 컨텍스트 한계

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = roadmap 작성자와 동일 컨텍스트. 자기 작성 산출 자기 검토 한계 인지.

### 3.2 본 한계의 청산

| # | 청산 원칙 | 본 검토 적용 |
|---|-------|--------|
| 1 | 사후 외부 LLM 충족 | P2 v3 정식 채택 + ADR-012 발행 cross-vendor 외부 LLM 합산 4건 권위 *내부* 작업 |
| 2 | 격상 전 면제 | Hermes PMO 격상 *전* — 본 roadmap 자체가 *Implementation/Runtime PASS 진입 전 우선순위 결정* |
| 3 | 합의 권위 내부 변경 | 본 검토 = 후속 14 분기 A 답습 = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 | 본 §0.3 + §3 명시 |

### 3.3 5 통제 답습

| # | 통제 | 본 검토 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ 사용자 명시 작업명 + 목적 + 표 컬럼 8 + 5 우선순위 판단 기준 + 8 예상 우선순위 + 검토 형태 + 5 트리거 모두 §0 + §1 + §2 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0.4 비검토 대상 + §1 평가 + §2 5 트리거 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §1.5 (그룹 H + 그룹 I = 풀 3+1 = T3 변경 영역) |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §1.6 (PASS 기준 통합 매트릭스 — ADR-011 §2.1 (a)~(e) 5조건 직접 답습) |
| 5 | 본 검토가 *하지 않는* 것 명시 (§0.4 + §4.2) | ✅ 명시 |

### 3.4 본 단축 합의가 *하지 않는* 것

§4.2 답습.

---

## 4. 결론

```
✅ APPROVE (단축 합의, Reviewer-only) — roadmap 권위 권고 발행 적격
```

본 결론은 **Implementation/Runtime PASS roadmap 작성 + 우선순위 권고** 의 *권고 권위 발행 적격* 한정. **본 roadmap 의 우선순위 자동 *고정* 0건** — 사용자 명시 결정 + 각 그룹 별 합의 (단축 또는 풀 3+1) + PoC evidence 후 발생.

### 4.1 본 합의가 *발생시키는* 것

- ✅ Implementation/Runtime PASS roadmap (`docs/architecture/implementation-runtime-roadmap.md`) 권위 권고 발행
- ✅ 17 항목 분해 + 9 그룹 (A ~ I) 동시 진행 가능 분류
- ✅ 사용자 예상 8 우선순위 = 모두 유지 + Claude 재평가 추가 3 항목 (Order 9 ~ 11)
- ✅ ADR-011 §2.1 (a)~(e) 5조건 답습 매트릭스 + Rollback Trigger 9 항목 + Evidence Required 5 형식
- ✅ 그룹 H (ADR-014 신규 발행) + 그룹 I (G3 22 권한 분해) = 풀 3+1 + 외부 LLM 1+ 의무 명시
- ✅ 그룹 A ~ G = 단축 합의 + PoC evidence 적격

### 4.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ Hermes PMO 격상 선언
- ❌ Implementation/Runtime PASS 자동 선언
- ❌ 실 runtime code / migration script / hook 구현
- ❌ ADR 본문 자동 갱신
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 본 roadmap 의 우선순위 자동 *고정* (사용자 명시 결정 + 각 그룹 별 합의 영역)
- ❌ ADR-014 신규 발행 자동 (그룹 H = 별도 풀 3+1 + 외부 LLM 1+ 합의)

### 4.3 다음 진입점 (사용자 결정 영역)

본 검토 APPROVE → roadmap 권위 권고 발행 → 다음 작업 (사용자 결정 영역):

1. **그룹 A (Order 1) — G2 GP-5 Provider Adapter Enforcement 첫 PoC 착수** (다음 진입점, 단축 합의 + PoC evidence)
2. 그룹 B / C / D 동시 진행 (그룹 A 완료 후) — 의존성 0건 영역 병렬 작업
3. 그룹 H (ADR-014 신규 발행) — 그룹 C 완료 후 별도 풀 3+1
4. 그룹 I (G3 22 권한 분해) — 별도 분해 후속 합의

**권고 시작 명령**: "G2 GP-5 Provider Adapter Enforcement 첫 PoC 착수해주세요 (depcruise rule + AST scanner + pre-commit hook + CI step + Docker 격리 PoC)" — 그룹 A 진입.

---

**합의 commit 권위**: 본 commit (`docs(review): record implementation/runtime roadmap short consensus APPROVE (Reviewer-only)`)
**본 commit + roadmap 문서 commit + housekeeping commits = 본 세션 후속 15 (roadmap 작성) 완료**
**다음 세션 진입점**: 그룹 A (G2 GP-5 Provider Adapter Enforcement) 첫 PoC 착수 (단축 합의 + PoC evidence)
