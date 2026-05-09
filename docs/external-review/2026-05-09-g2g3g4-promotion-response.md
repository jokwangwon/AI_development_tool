# 외부 LLM 검토 응답 — G2 + G3 + G4 정식 PASS 승격 (2026-05-09)

> **외부 LLM 응답** — `docs/external-review/2026-05-09-g2g3g4-promotion-request.md` 의뢰 자료에 대한 외부 LLM 평가 결과. 본 문서는 사용자가 외부 LLM 으로부터 회수하여 paste 한 응답을 *원문 그대로* 보존합니다 (Reviewer 종합의 권위 근거).
>
> **권위 규칙**: 본 문서는 사용자 paste 또는 human-signed commit 만 권위 인정. Hermes-originated 변경 자동 reject 대상 (G3 §2.2 #20 답습 + 외부 LLM 조건 4 답습).

**응답 회수일**: 2026-05-09
**검토 대상 의뢰 자료**: `docs/external-review/2026-05-09-g2g3g4-promotion-request.md` (v1)
**최종 판정**: **APPROVE WITH CONDITIONS** (PASS 범위를 Design/Governance Gate PASS 로 한정)

---

## 외부 LLM 검토 결과

### 결론

G2 / G3 / G4를 동시에 정식 PASS로 승격하는 방향은 가능합니다. 다만 이 PASS는 반드시 **"설계·거버넌스 게이트 PASS"** 로 한정해야 합니다. 아직 GP-2~GP-6의 PoC, CI 검증, Evidence Ledger, 합의 evidence가 완전히 충족된 상태는 아니므로, 이를 **"운영 구현 완료 PASS"** 로 선언하면 안 됩니다. 문서 자체도 GP-2~GP-6은 아직 PoC와 합의가 필요하다고 명시하고 있습니다.

따라서 제 판정은 다음과 같습니다.

| 항목 | 판정 |
|------|------|
| G2 | 조건부 PASS |
| G3 | 조건부 PASS |
| G4 | 조건부 PASS |
| P2 v3 정식 채택 합의 단계 진입 | 조건 충족 후 가능 |
| P2 v3 정식 채택 자체 | 아직 아님 |
| Hermes PMO 격상 | 아직 아님 |
| runtime code / migration script 구현 완료 주장 | 불가 |

---

### 1. 운영 가능성 평가

**판정**: 조건부 승인

G2의 6개 GP, G3의 22개 권한, G4의 17개 Skill schema 필드는 구현 인계가 가능할 정도로 구체적입니다. 특히 G2는 P1~P8 위반 경로를 GP-1~GP-6으로 매핑하고 있고, G3는 Hermes가 할 수 있는 일과 할 수 없는 일을 T1/T2/T3로 나누며, G4는 Memory scope와 Skill schema, JSONL hash chain을 구체화하고 있습니다.

다만 1인 개발자 기준으로는 운영 부담이 큽니다. 특히 G3의 22개 권한과 G4의 17개 필드는 "문서 설계"로는 좋지만, 실제 운영에서는 체크리스트·CI·pre-commit·Evidence Ledger 템플릿으로 자동화하지 않으면 사람이 계속 기억해야 하는 체계가 됩니다.

**조건**: G2/G3/G4 PASS 전, 문서에 다음 문구를 명시하는 것을 권장합니다.

> 본 PASS는 "Design / Governance Gate PASS"이며, GP-2~GP-6 및 migration script / runtime hook / CI 검증의 "Implementation PASS"를 의미하지 않는다.

이 문구가 없으면 나중에 "문서 게이트 통과"와 "운영 구현 완료"가 섞일 위험이 큽니다.

---

### 2. 보안 / 거버넌스 견고성 평가

**판정**: 강한 구조이나, 일부 우회 경로 보강 필요

가장 강한 부분은 **Hermes ≠ root of trust 원칙**입니다. 문서는 권위 위계를 Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents로 두고, Hermes를 승인 주체가 아니라 검증 대상 및 조율자로 제한합니다. 또한 PASS 성립 조건으로 Tools 검증, Evidence Ledger, 사용자 승인, 합의 보고서 commit을 요구합니다. 이 방향은 매우 적절합니다.

하지만 현재 설계에서 단일 실패점이 될 수 있는 부분이 있습니다.

**Evidence Ledger 자체의 변조 방지**
"Evidence decides"는 좋은 원칙이지만, Evidence Ledger가 조작되면 전체 판정이 오염됩니다. Evidence Ledger도 hash chain, signed commit, CI 검증 대상에 포함해야 합니다.

**.git 및 CI 설정 보호**
문서는 governance 문서 read-only, Hermes-originated commit auto-reject를 언급하지만, .git, GitHub Actions/CI config, pre-commit 설정, evidence 파일 자체가 수정되면 우회될 수 있습니다. 보호 대상에 .git, .github/, CI workflow, hook 설정, evidence ledger를 명시해야 합니다.

**외부 LLM 검토 결과 저장 경로**
외부 LLM 검토 결과가 docs/external-review/...에 저장될 예정이라면, 이 파일도 Hermes가 임의 생성·수정할 수 없어야 합니다. "외부 검토 파일은 사용자 paste 또는 human-signed commit만 권위 인정" 같은 규칙이 필요합니다.

**누락된 위반 경로**
P1~P8은 핵심을 잘 잡았지만, 다음 위험은 별도 명시하는 편이 안전합니다.
- prompt injection / tool-output injection
- evidence forgery
- CI secret exfiltration
- dependency / supply-chain attack
- generated document poisoning
- migration import/export path traversal
- Memory poisoning

이들은 일부 P5에 포함될 수 있지만, 메타-템플릿의 특성상 명시적으로 분리하는 것이 좋습니다.

---

### 3. 단순화 / 대안 평가

**판정**: 동시 PASS가 단계별 PASS보다 적절

G2/G3/G4는 서로 강하게 의존합니다. 문서도 G2의 GP-6은 G4의 JSONL/Skill 형식과 연결되고, G2 §9의 메타 안전장치는 G3 운영 구현 없이는 약하며, G4의 Skill promotion 통제도 G3 권한 체계 없이는 완성되지 않는다고 설명합니다.

따라서 G2만 먼저 PASS, G4만 먼저 PASS처럼 나누는 것보다, 세 게이트를 하나의 묶음으로 통과시키는 것이 정합성 측면에서 더 낫습니다.

다만 단순화는 필요합니다.

**단순화 권고**

| 영역 | 권고 |
|------|------|
| G2 6 GP | 줄이지 말고 유지. 다만 GP-2~GP-6은 "Implementation Pending" 상태 표기 |
| G3 22 권한 | 삭제하지 말고 T1 allowed / T2 approval / T3 forbidden 3그룹으로 운영 체크리스트화 |
| G4 17 필드 | 유지. 대신 MVP 필수 필드와 후속 필드를 구분 |
| G4 provider_bindings | optional only, required/exclusive 금지, 최소 2 provider 재해석 가능을 schema lint 규칙으로 강제 |

G4의 17개 필드는 다소 많지만, Skill이 권한·입출력·증거·승격 상태까지 포함해야 한다면 과도하다고 보기는 어렵습니다. 줄이기보다는 MVP required / recommended / future로 나누는 것이 낫습니다.

---

### 4. 메타 편향 / 자기참조 위험 평가

**판정**: 한계 노출은 충분하나, 통제는 조건부로 충분

문서는 자기참조 위험을 숨기지 않고 명시적으로 드러냅니다. 특히 G2/G3/G4 DRAFT가 같은 컨텍스트에서 만들어졌고, Reviewer-only 검토였으며, 외부 LLM 검토가 메타 편향 통제 목적이라는 점을 명시한 것은 좋은 설계입니다.

다만 **외부 LLM 1개만으로 "최종 안전성"을 보장한다고 보기는 어렵습니다.**

제 판단은 다음과 같습니다.

| 단계 | 외부 검토 요구 수준 |
|------|---------------|
| G2/G3/G4 설계 PASS | 외부 LLM 1개로 충분 |
| P2 v3 정식 채택 | 외부 LLM 1개 + 내부 3+1 종합이면 가능 |
| Hermes PMO 격상 | 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 권장 |
| runtime code / migration script 구현 | 실제 테스트 evidence 필수 |

즉, 이번 검토는 P2 v3 합의 단계 진입 근거로는 충분하지만, Hermes PMO 격상이나 운영 구현 완료의 근거로는 부족합니다.

---

## 필수 조건 목록

다음 조건을 반영하면 G2/G3/G4 동시 PASS 승격 및 P2 v3 정식 채택 합의 단계 진입을 승인할 수 있습니다.

### 조건 1. PASS 범위 명확화

정식 PASS를 다음처럼 분리해야 합니다.

- **Design/Governance PASS**: 문서 구조, 권위 위계, gate 설계 승인
- **Implementation PASS**: PoC, CI, runtime hook, migration script, Evidence Ledger 검증 완료

이번 G2/G3/G4 승격은 전자에 한정해야 합니다.

### 조건 2. GP-2~GP-6 상태 표기

G2에서 GP-1은 G1b evidence를 흡수해 PASS로 볼 수 있지만, GP-2~GP-6은 아직 PoC와 합의가 필요합니다. 따라서 다음 상태 표기를 권장합니다.

| GP | 상태 |
|----|----|
| GP-1 | PASS |
| GP-2 | DESIGN PASS / IMPLEMENTATION PENDING |
| GP-3 | DESIGN PASS / IMPLEMENTATION PENDING |
| GP-4 | DESIGN PASS / IMPLEMENTATION PENDING |
| GP-5 | DESIGN PASS / IMPLEMENTATION PENDING |
| GP-6 | DESIGN PASS / IMPLEMENTATION PENDING |

### 조건 3. Evidence Ledger 보호 강화

Evidence Ledger에 다음 필드를 요구하십시오.

- evidence_id
- gate_id
- tool / command
- expected result
- actual result
- artifact path
- hash
- reviewer
- timestamp
- pass/fail status
- rollback trigger

그리고 Evidence Ledger 자체를 hash chain 또는 signed commit 대상으로 넣어야 합니다.

### 조건 4. Git / CI / 외부 검토 파일 보호 명시

G3의 보호 대상에 다음을 추가해야 합니다.

- `.git/`
- `.github/workflows/`
- pre-commit config
- CI config
- evidence ledger
- external-review 문서
- ADR / SDD / gate 정의 문서

Hermes-originated commit auto-reject뿐 아니라, Hermes-originated external review file 생성/수정도 권위 없음을 명시해야 합니다.

### 조건 5. P1 facade / ADR-009 Adapter 의존성 명시

P2 v3 정식 채택 전 다음 의존성을 명시해야 합니다.

- GP-2는 LLM facade redaction filter에 의존
- GP-5는 Provider Adapter / P1 facade 단일 진입점에 의존
- G4 migration은 provider-neutral import/export interface에 의존

따라서 P2 v3 채택 전 P1 facade MVP와 ADR-009 Adapter v2.0의 최소 진입 조건을 별도 표로 두는 것이 좋습니다.

### 조건 6. G4 hash chain 사양 보강

G4 JSONL hash chain은 좋은 방향이지만, 다음을 명시해야 합니다.

- canonical JSON 규칙
- newline / encoding 규칙
- field ordering 규칙
- genesis hash 생성 규칙
- prev_hash 검증 실패 시 처리
- 전체 파일 rewrite 공격 방지를 위한 git history 또는 signed commit 사용
- migration round-trip 실패 시 "의미 보존 ledger" 작성 기준

### 조건 7. 누락 위험 P9~P12 추가 고려

P1~P8에 다음을 추가하거나 별도 보조 위험으로 둬야 합니다.

| 후보 | 위험 |
|------|------|
| P9 | prompt injection / tool-output injection |
| P10 | evidence forgery / audit log tampering |
| P11 | dependency / CI / supply-chain secret exfiltration |
| P12 | memory poisoning / generated docs poisoning |

---

## 게이트별 세부 판정

| 게이트 | 판정 | 이유 |
|--------|------|------|
| G2 | APPROVE WITH CONDITIONS | P1~P8 → GP-1~GP-6 매핑은 적절하나, GP-2~GP-6은 implementation evidence 미충족 |
| G3 | APPROVE WITH CONDITIONS | Hermes ≠ root of trust 체계는 강하지만, Evidence Ledger / .git / CI 보호 보강 필요 |
| G4 | APPROVE WITH CONDITIONS | Provider-agnostic schema와 JSONL 방향은 적절하나, hash chain canonicalization과 provider binding lint 필요 |

---

## 최종 문구 제안

최종 합의 보고서에는 아래처럼 쓰는 것이 가장 안전합니다.

> **External Review Verdict**: APPROVE WITH CONDITIONS.
> G2/G3/G4 may be promoted from DRAFT to **Design/Governance PASS** as a bundled gate set, because their interfaces are mutually dependent and the current architecture contains no blocking contradiction. However, **this does not constitute implementation/runtime PASS** for GP-2~GP-6, migration scripts, CI enforcement, or Hermes PMO elevation. Before P2 v3 formal adoption, the project must clarify PASS scope, protect Evidence Ledger / Git / CI / external-review paths, define P1 facade and ADR-009 Adapter dependencies, and strengthen G4 hash-chain canonicalization and provider binding lint rules.

요약하면:
- **BLOCK은 아닙니다.**
- **PARTIAL도 아닙니다.**
- **다만 무조건 APPROVE도 아니고, "설계 PASS로 한정한 조건부 승인" 이 가장 정확합니다.**

---

**응답 원문 보존**: 본 문서는 외부 LLM 응답을 사용자가 paste 한 원문 그대로 보존합니다.
**다음 단계**: Reviewer (`docs/review/3plus1-consensus-2026-05-09-g2g3g4-formal-promotion.md`) 가 본 응답 + Agent A/B/C 3 내부 분석을 종합하여 최종 합의 판정 작성.
