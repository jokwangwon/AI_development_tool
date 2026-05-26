# 외부 LLM 응답 — G2 + G3 + G4 통합 게이트 PASS 승격 가능성 평가 (2026-05-07)

**의뢰서**: `docs/external-review/2026-05-07-g2-g3-g4-integrated-gate-review-request.md`
**응답 수령일**: 2026-05-07
**vendor / model**: OpenAI ChatGPT / GPT-5.5 Thinking
**외부 참고 자료 사용 여부**: 없음. 본 의뢰서에 포함된 정보만 기준으로 평가
**판정 기준**: "문서 설계 게이트로서 PASS 가능한가" 와 "실제 runtime / PoC / migration 구현까지 완료되었는가" 를 분리하여 판단

---

## 0. 응답자 정체

- vendor / model: OpenAI ChatGPT / GPT-5.5 Thinking
- 외부 참고 자료 사용 여부: 없음. 본 의뢰서에 포함된 정보만 기준으로 평가했습니다.
- 판정 기준: "문서 설계 게이트로서 PASS 가능한가" 와 "실제 runtime / PoC / migration 구현까지 완료되었는가" 를 분리해 판단했습니다.

---

## 1. Q1 — 4 게이트 충분성 평가

**판정**: 대체로 충분하나, PMO 격상 전 보조 게이트 또는 보강 항목이 필요합니다.

G1b / G2 / G3 / G4 구성은 Hermes PMO 격상 전의 핵심 위험을 꽤 잘 덮고 있습니다.

- **G1b**: secret persistence 방어
- **G2**: 거버넌스 사전조건
- **G3**: Hermes ≠ root of trust 운영 원칙
- **G4**: provider-agnostic Memory / Skill 형식

다만 현재 4 게이트만으로는 다음 영역이 별도 명시되거나 보조 게이트로 추가되는 것이 좋습니다.

### 1.1 Human approval provenance

- "사용자 승인" 이 중요한 권위로 반복 등장하지만, 그 승인의 식별 방식이 약합니다.
- 누가, 언제, 어떤 commit / artifact / evidence 에 대해 승인했는지 추적해야 합니다.

### 1.2 Audit / Evidence Ledger 무결성

- Evidence 없는 PASS 금지는 좋지만, Evidence Ledger 자체의 변조 / 삭제 / 재작성 방어가 별도 T3 로 명확히 묶여야 합니다.

### 1.3 Network egress / external communication policy

- GP-2 가 로그 / LLM 송신 redaction 을 다루지만, 어떤 외부 endpoint 로 나갈 수 있는지, network allowlist / denylist 정책은 더 명확해야 합니다.

### 1.4 Recovery / rollback / incident response

- 자동 비활성화와 컨테이너 정지는 언급되어 있으나, 사고 후 복구 절차, 증거 보존, 재승격 조건이 더 필요합니다.

### 1.5 Supply chain / dependency integrity

- provider lock-in 은 다루지만, dependency pinning, checksum, CI 환경 신뢰, external tool 업데이트 위험은 별도 항목으로 다루는 것이 좋습니다.

**결론**: 4 게이트 구조는 핵심 축으로 충분하지만, PMO 격상 전에는 *"승인 출처 / 증거 무결성 / 네트워크 egress / 복구 절차 / supply chain"* 보강이 필요합니다.

---

## 2. Q2 — 통합 PASS 적합성 평가

**판정**: 조건부로 적합합니다. 단, "통합 PASS" 가 각 게이트의 개별 결함을 가리면 안 됩니다.

G2 / G3 / G4 는 서로 강하게 맞물려 있으므로 통합 검토 자체는 타당합니다.

- G2 의 GP-5 / GP-6 은 G4 없이는 provider / memory lock-in 방어가 불완전합니다.
- G2 §9 는 G3 없이는 Hermes 자기참조 차단이 약합니다.
- G4 의 Memory / Skill schema 는 G3 권한 모델 없이는 자동 승격 / skill escalation 위험을 막기 어렵습니다.

따라서 동시 검토는 단계별 검토보다 인터페이스 정합성을 확인하기 좋습니다.

다만 동시 PASS 선언에는 주의가 필요합니다. 특히 G2 에서 GP-2~GP-6 의 exit 기준이 아직 충족되지 않았다고 명시되어 있습니다. 그러므로 무조건적인 PASS 는 부적절합니다.

권장 방식은 다음과 같습니다.

| 구분 | 권장 상태 |
|---|---|
| G2/G3/G4 문서 설계의 상호 정합성 | PASS 가능 |
| 실제 runtime / PoC / migration 구현 완료 여부 | PASS 불가 |
| PMO 격상 가능성 | 아직 불가 |
| P2 v3 채택 합의 진입 | 조건부 가능 |

**결론**: *"Design Gate PASS"* 로는 통합 PASS 가능하지만, *"Operational Readiness PASS"* 로 해석하면 아직 이릅니다.

---

## 3. Q3 — PARTIAL 유지 필요 게이트 여부

**판정**: 엄격한 의미의 PASS 라면 **G2 는 PARTIAL, G3/G4 는 조건부 PASS** 에 가깝습니다.

### 3.1 G2

G2 는 가장 신중해야 합니다.

문서 자체는 잘 구성되어 있지만, GP-2~GP-6 의 (a)~(e) 조건이 아직 충족되지 않았다고 명시되어 있습니다. 따라서 G2 를 "실제 사전조건 충족 완료" 로 PASS 처리하면 안 됩니다.

권장 상태:
- **G2 Design Definition PASS**
- **G2 Implementation Evidence PARTIAL**

즉, G2 는 *"거버넌스 사전조건의 정의"* 로는 PASS 가능하지만, *"사전조건이 실제로 충족되었다"* 는 의미의 PASS 는 아직 불가합니다.

### 3.2 G3

G3 는 구조적으로 가장 강합니다.

Hermes 를 root of trust 로 두지 않기 위한 권한 분류, T1/T2/T3, 자기참조 차단, evidence rule 은 설계상 타당합니다.

다만 다음 보강이 필요합니다.

- Evidence Ledger 변조 방지 명시
- 사용자 승인 provenance 강화
- signed commit SHOULD → T2/T3 결정에는 사실상 MUST 에 가깝게 상향 검토

권장 상태:
- **G3 Design PASS with Conditions**

### 3.3 G4

G4 도 설계상 타당합니다.

Memory scope, Skill schema, provider_bindings, JSONL export, hash chain 방향은 좋습니다. 다만 canonical JSON, schema evolution, import declaration 은 PASS 전 또는 P2 v3 채택 전 흡수하는 것이 안전합니다.

권장 상태:
- **G4 Design PASS with Conditions**

---

## 4. Q4 — Provider / Memory lock-in / Skill escalation 위험 평가

### 4.1 Provider lock-in

**판정**: 방향은 충분하지만, 검증 레이어가 조금 더 필요합니다.

G2 GP-5 + G3 §6.4 + G4 §3.5 + G4 §4.3 조합은 설계상 강합니다.

다만 depcruise 는 주로 JavaScript / TypeScript 생태계에 맞는 도구입니다. 본 템플릿이 여러 언어 프로젝트에 복사될 가능성이 있다면, provider lock-in 검증은 언어별로 확장되어야 합니다.

보강 권장:
- Python: import graph / AST 기반 provider SDK direct import 탐지
- Java/Kotlin: dependency / package import 탐지
- Docker / YAML / env: provider-specific endpoint / model 명 탐지
- Skill 본문 내 model name / endpoint / SDK 문자열 탐지

### 4.2 Memory lock-in

**판정**: 충분한 방향이나, G4 P-1 은 PASS 전 또는 P2 v3 전 흡수 권장입니다.

JSONL + hash chain + migration script + roundtrip PoC 는 provider-agnostic memory 전략으로 적절합니다.

다만 canonical JSON 정의가 약하면 hash 재현성이 흔들릴 수 있습니다. RFC 8785 JCS 를 직접 채택하거나, 프로젝트 자체 canonicalization 규칙을 명확히 적어야 합니다.

권장:
- canonical JSON 규칙 명시
- field ordering / whitespace / Unicode normalization / number representation 규칙 명시
- hash 계산 대상에서 hash 필드 제외 여부 명시
- schema_version 별 hash compatibility 정책 명시

### 4.3 Skill escalation

**판정**: 기본 구조는 충분하지만, `allowed_actions` 를 더 세분화해야 합니다.

현재 `read`, `write`, `shell`, `network`, `db`, `git`, `docker` 는 너무 넓은 권한입니다.

예를 들어 `shell: true` 는 사실상 모든 것을 할 수 있습니다. `docker` 도 매우 강한 권한입니다.

보강 권장:
- `shell` 은 기본 금지
- 허용 command allowlist 필요
- `network` 는 domain / method / port 단위 제한
- `db` 는 read/write/migrate/admin 분리
- `git` 은 read/status/diff/commit/tag/push 분리
- `docker` 는 build/run/volume/socket 접근 분리
- timeout / memory / CPU / filesystem mount 제한 명시

---

## 5. Q5 — Hermes ≠ root of trust 운영 구현 평가

**판정**: 원칙 구현은 강하지만, approval / evidence / audit 쪽 보강이 필요합니다.

G3 의 T1/T2/T3 분류는 좋은 구조입니다. 특히 다음은 강점입니다.

- Hermes 가 PASS 를 자동 선언하지 못함
- Hermes 가 ADR / Constitution 을 자동 수정하지 못함
- Hermes 가 Skill 을 자기 승인하지 못함
- Evidence 없는 PASS 금지
- Reviewer / Human / Tools / Evidence 우선 구조

하지만 우회 경로가 남아 있습니다.

### 가능한 우회 경로

#### 5.1 Evidence Ledger 자체 수정

- Hermes 가 정책은 못 바꾸더라도 evidence 기록을 조작하면 PASS 판단을 왜곡할 수 있습니다.
- Evidence Ledger 수정 / 삭제 / 재작성은 T3 로 명확히 지정해야 합니다.

#### 5.2 사용자 승인 위조 또는 모호한 승인

- "사용자 승인" 이 채팅 문맥인지, commit 인지, signed artifact 인지 모호합니다.
- T2/T3 승인에는 최소한 commit hash, timestamp, 승인 문구, 승인 대상 artifact 가 남아야 합니다.

#### 5.3 CI / hook 설정 변경

- Hermes 가 gate 본문은 못 바꾸더라도 CI 설정, pre-commit, wrapper 설정을 바꾸면 우회가 가능합니다.
- CI / hook / wrapper / branch protection 변경도 T3 로 묶어야 합니다.

#### 5.4 Skill wrapper 자체 변경

- Skill permission escalation 을 wrapper 가 막는 구조라면, wrapper 변경은 고위험 정책 변경입니다.
- wrapper / sandbox / permission evaluator 변경은 T3 또는 T2+full consensus 가 필요합니다.

### signed commit 관련

G3 §5.5 에서 1인 동일 호스트 SPOF 에 대해 signed commit 을 SHOULD 로 둔 것은 현실적이지만, **PASS / ADR / Gate / T2/T3 승인에는 MUST 에 가깝게 상향** 하는 것이 좋습니다.

**결론**: Hermes ≠ root of trust 원칙은 설계상 충분히 구현되어 있으나, evidence ledger 와 approval provenance 가 약하면 실제 운영에서 다시 Hermes 또는 동일 세션 문맥이 사실상 root of trust 가 될 수 있습니다.

---

## 6. Q6 — 1인 개발자 거버넌스 오버헤드 평가

**판정**: 현재 구조는 강하지만, 1인 개발자 기준으로는 과합니다. **단계적 MVP 축소가 필요** 합니다.

현재 구조는 보안 / 거버넌스 관점에서는 훌륭하지만, "코드 0줄 + 50개 마크다운 + 1인 개발자" 상태에서는 구현 부담이 큽니다.

특히 다음 조합은 과부하 위험이 있습니다.

- G2 6 GP × 5조건
- G3 22 권한
- G4 17 schema 필드
- Memory scope 4 단계
- JSONL hash chain
- migration scripts
- PoC / evidence / consensus / approval pipeline

권장 축소 방식은 *"삭제"* 가 아니라 *"단계화"* 입니다.

### 권장 MVP 단계

| 단계 | 최소 구현 |
|---|---|
| MVP-0 | G2/G3/G4 문서 PASS, 범위 명확화 |
| MVP-1 | G1b, GP-2 redaction, GP-3 secret scan, GP-5 provider facade |
| MVP-2 | G4 JSONL schema + canonical hash + migration stub |
| MVP-3 | Skill wrapper + allowed_actions enforcement |
| MVP-4 | full evidence ledger + signed approval + multi-provider roundtrip |
| MVP-5 | PMO 격상 검토 |

### 축소 후보

- G2 GP-2 와 GP-3 는 *"Secret / Egress Hygiene"* 상위 그룹으로 묶을 수 있습니다.
- G3 22 권한은 유지하되, 문서상으로는 5~7개 권한군으로 재분류하면 운영 부담이 줄어듭니다.
- G4 17 필드는 모두 유지해도 되지만, *required core* 와 *optional governance metadata* 로 나누는 것이 좋습니다.

권장 예시:

| Skill 필드 구분 | 필드 |
|---|---|
| Core required | `id`, `name`, `version`, `scope`, `description`, `inputs`, `outputs`, `allowed_actions`, `promotion_status` |
| Governance required for promotion | `owner`, `required_evidence`, `required_tests`, `rollback_triggers`, `created_from`, `last_verified_at` |
| Optional / constrained | `forbidden_actions`, `provider_bindings` |

---

## 7. Q7 — P2 v3 정식 채택 전 보강 항목

**판정**: P2 v3 정식 채택 전 반드시 흡수할 항목이 있습니다.

### 반드시 보강

#### 7.1 PASS 의미 분리

- Design Gate PASS
- Implementation Evidence PASS
- Operational Readiness PASS

이 셋을 명확히 분리해야 합니다.

#### 7.2 G2 GP-2~GP-6 evidence 상태 명시

- 현재는 "형식 정의 완료, PoC 미완료" 에 가깝습니다.
- 이를 PASS 선언문에 반드시 반영해야 합니다.

#### 7.3 Evidence Ledger schema

- evidence id
- artifact path
- command / tool result
- timestamp
- actor
- commit hash
- previous evidence hash
- approval reference

#### 7.4 Approval provenance

- T2/T3 승인에 대해 사용자 승인 문구와 대상 commit / 문서 / gate 를 연결해야 합니다.

#### 7.5 Canonical JSON / hash 규칙

- G4 P-1 은 P2 v3 전 흡수 권장입니다.

#### 7.6 Schema evolution policy

- G4 P-2 는 P2 v3 전 흡수 권장입니다.
- 필드 추가뿐 아니라 제거 / rename / type change / deprecation / migration rule 이 필요합니다.

#### 7.7 External import schema_version declaration

- G4 P-3 도 P2 v3 전 흡수 권장입니다.

#### 7.8 Skill permission granularity

- shell, network, db, git, docker 권한을 세분화해야 합니다.

#### 7.9 Audit / CI / wrapper 변경 보호

- gate 본문뿐 아니라 gate 를 강제하는 도구 자체도 보호 대상이어야 합니다.

---

## 8. G4 자기 발견 5 위험 처리 시점 권고

| 항목 | 위험도 | 권고 |
|---|---|---|
| **P-1** canonical JSON RFC 8785 직접 인용 부재 | LOW 지만 중요 | P2 v3 정식 채택 전 흡수 권장 |
| **P-2** schema evolution 에서 제거 / rename / type change 정책 부재 | LOW 지만 중요 | P2 v3 정식 채택 전 흡수 권장 |
| **P-3** 외부 import 시 schema_version declaration 절차 약함 | LOW | P2 v3 정식 채택 전 흡수 권장 |
| **P-4** "3-way 인터페이스" 명명 문제 | VERY LOW | G2/G3/G4 PASS 전 문구 정정하면 좋음. BLOCK 사유 아님 |
| **P-5** `~/.claude/global/` 경로 충돌 가능성 | VERY LOW | P2 v3 전 경로 namespace 정리 권장. 예: `~/.ai-dev-template/global/` 또는 명시적 env override |

---

## 9. 최종 판정

### **APPROVE WITH CONDITIONS**

G2 / G3 / G4 는 문서 설계 게이트로서 통합 PASS 승격 가능합니다. 다만 다음 조건을 반영해야 합니다.

### 필수 조건

#### 9.1 PASS 범위 명시

- 이번 PASS 는 **Design Gate PASS** 로 한정해야 합니다.
- runtime 구현 완료, PoC 완료, PMO 격상, P2 v3 정식 채택으로 해석하면 안 됩니다.

#### 9.2 G2 상태 정정

- GP-1 은 G1b evidence 로 흡수 가능.
- GP-2~GP-6 은 *"조건 정의 완료 / 구현 evidence 미완료"* 로 명확히 표시해야 합니다.
- 따라서 G2 는 *"governance precondition definition PASS"* 이지 *"all GP evidence PASS"* 가 아닙니다.

#### 9.3 G4 P-1 / P-2 / P-3 흡수

- canonical JSON
- schema evolution
- external import schema_version

이 3개는 P2 v3 정식 채택 전 반드시 반영해야 합니다.

#### 9.4 Evidence Ledger 와 approval provenance 보강

- Evidence Ledger 자체의 변조 방지
- 사용자 승인 대상 / 시점 / commit 연결
- T2/T3 승인 기록 방식 명시

#### 9.5 Skill permission 세분화

- shell, network, db, git, docker 는 현재 너무 넓습니다.
- 최소한 allowlist / denylist / timeout / sandbox / scope 제한을 문서화해야 합니다.

#### 9.6 Gate enforcement layer 보호

- Constitution / ADR / Gate 문서뿐 아니라 CI, hook, wrapper, branch protection, evidence writer 변경도 보호 대상으로 명시해야 합니다.

#### 9.7 1인 개발자용 단계적 MVP 계획 추가

- 전체 구조를 한 번에 구현하려 하면 과합니다.
- P2 v3 채택 전 *"최소 구현 순서"* 를 명시하는 것이 좋습니다.

---

## 10. 메타 노트

### 10.1 결론 유도 여부

약한 수준의 결론 유도는 있습니다.

특히 *"통합 PASS 가 유리하다는 견해가 있음"* 과 *"내부 평가에서는 BLOCK 사유 아님"* 이라는 표현은 외부 검토자에게 방향성을 줄 수 있습니다. 다만 메타 한계를 정직하게 노출했고, 범위 밖 항목을 명확히 분리했기 때문에 *심각한 결론 유도는 아닙니다.*

### 10.2 누락된 정보

다음 정보가 있으면 더 정확한 판단이 가능합니다.

- PASS 용어의 정확한 상태 체계
- Evidence Ledger 실제 schema
- CI / hook / wrapper 가 어느 언어와 도구로 구현될 예정인지
- Hermes 실제 권한 모델과 filesystem 접근 모델
- 사용자 승인 기록 방식
- PMO 격상 후 Hermes 가 실제로 수행할 작업 범위
- target project 의 주 언어 / 배포 환경 / 위협 모델

### 10.3 문서 길이

문서는 깁니다. 하지만 검토 대상이 meta-governance / root-of-trust / provider liquidity 이므로 길이 자체는 과도하지 않습니다.

다만 실제 운영 문서로는 다음 분리가 좋습니다.

- Executive summary
- Gate decision matrix
- Risk register
- Required conditions
- Full technical appendix

---

## 요약 판정

**APPROVE WITH CONDITIONS** 입니다.

G2/G3/G4 는 통합 설계 게이트로 PASS 승격해도 됩니다. 하지만 그 PASS 는 반드시 **"설계 정합성 PASS"** 로 한정해야 하며, **"구현 evidence 완료"**, **"P2 v3 정식 채택"**, **"Hermes PMO 격상"** 으로 확대 해석하면 안 됩니다.

---

**응답 수령일**: 2026-05-07
**vendor / model**: OpenAI ChatGPT / GPT-5.5 Thinking
**최종 판정**: APPROVE WITH CONDITIONS (Design Gate PASS 한정, 7 필수 조건 반영 의무)
**흡수 처리**: 다음 단계 G2 + G3 + G4 통합 풀 3+1 합의 (`docs/review/3plus1-consensus-2026-05-07-g2-g3-g4-gate-adoption.md`) 에서 Reviewer 가 Agent A/B/C 내부 분석과 종합
