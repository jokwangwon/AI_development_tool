# C-14 Cross-vendor Blind 검토 의뢰 — P2 v3 정식 채택 진입 전 사전 검토

> **이 문서를 통째로 ChatGPT (GPT-5.x), Gemini, 또는 다른 *비-Claude* vendor 강력한 LLM 에 붙여넣고 평가를 요청하십시오.** 첨부 자료 없이 본 문서만으로 평가 가능하도록 작성되었습니다.
>
> **본 의뢰의 *blind 강도* 는 가장 높습니다. 본 자료에는 다음이 *의도적으로 포함되지 않습니다*:**
> - ❌ 본 프로젝트의 내부 Agent A / B / C 분석 결과
> - ❌ 본 프로젝트의 Reviewer 종합 결론
> - ❌ 의뢰자 (사용자) 가 원하는 결론 / 방향 / 선호
> - ❌ APPROVE 유도 표현 / 답안 제시 / 결론 시사
>
> 본 의뢰는 vendor 다양성 (cross-vendor) 을 통해 진정한 *제3자* 의 독립 판단을 확보하기 위함입니다. 응답은 본 세션 또는 `docs/external-review/2026-05-XX-c14-cross-vendor-p2v3-pre-adoption-response.md` 에 저장될 예정입니다.

---

## 0. 검토 의뢰자의 입장 + 본 검토의 단일 질문

### 0.1 검토 의뢰자

저는 1인 개발자로 "**아이디어를 던지면 AI 에이전트 (주로 Claude Code) 가 SDD + TDD 로 자동 개발하도록 설계된 메타-템플릿**" 을 만들고 있습니다. 본 프로젝트 자체는 그 템플릿이며, 새 아이디어가 생길 때마다 본 템플릿을 복사해 시작합니다.

본 프로젝트의 메인 작업 컨텍스트는 Claude (Anthropic) 입니다. 따라서 본 cross-vendor 의뢰는 *비-Claude vendor* 의 의견을 확보하는 것이 핵심 목적입니다.

### 0.2 본 검토의 단일 질문

> **현재 DRAFT 상태인 P2 v3 (Hermes Adoption Design v3) 를 정식 채택 합의로 진입해도 안전한가?**

본 질문은 다음을 *묻지 않습니다*:
- ❌ 의뢰자가 무슨 답을 원하는지 (의뢰자는 답을 미리 제시하지 않음)
- ❌ 다른 LLM 이 어떤 답을 했는지 (본 자료는 다른 LLM 응답을 *포함하지 않음*)
- ❌ 내부 Agent 가 어떤 결론에 도달했는지 (본 자료에 *포함되지 않음*)

다음 4 판정 옵션 중 *어느 것이라도* 정당한 근거와 함께 제시 가능합니다:

1. **APPROVE** — P2 v3 정식 채택 합의로 진입해도 안전.
2. **APPROVE WITH CONDITIONS** — 일부 조건 충족 후 진입 가능. (조건 명시 필수)
3. **PARTIAL** — 일부 영역만 진입 가능, 나머지 추가 작업 필요. (부분 영역 명시)
4. **BLOCK** — 정식 채택 합의 진입 불가. (결함 명시 + 후속 조치 권고)

**본 의뢰자는 어느 판정도 사전에 선호하지 않습니다.** APPROVE 가 안전한 답이 아닙니다. BLOCK 도 안전한 답이 아닙니다. *근거에 의해 도출된 판정*이 안전한 답입니다.

### 0.3 본 검토의 *메타* 목적

자기참조 편향 통제. 본 프로젝트의 모든 합의 산출 (4 게이트 DRAFT 검토 + G2/G3/G4 정식 PASS 합의 + PR-1 + PR-2) 은 모두 Claude 패밀리 컨텍스트에서 작성되었습니다 (1 cross-vendor 의뢰 + 1 Claude 인접 컨텍스트 의뢰는 PR-2 에 포함). P2 v3 정식 채택 = *영구 권위 발행* 시점이므로, vendor 다양성 확보가 합의 적격성에 결정적입니다.

본 의뢰는 그 vendor 다양성을 확보하기 위한 의도적 *blind* 의뢰입니다.

---

## 1. 시스템 목적 (요약)

### 1.1 프로젝트 정체성

- **이름**: AI Development Tool Template
- **사용자**: 1인 개발자 (동일 호스트, SPOF 의도적 수용)
- **저장소**: 코드 0줄, 약 65개 마크다운 (헌법 + 12 ADR + 11 설계 문서 + 합의 보고서 + 가이드)
- **사용 방식**: 새 프로젝트 → 템플릿 복사 → Phase 0 (질문지) → Phase 1 (스택/에셋 합의) → Phase 2-3 (SDD → TDD)
- **메타-슬로건**: "에이전트에게 하라고 말하지 말고, 잘못하는 것이 *불가능*하게 만들어라."

### 1.2 핵심 방법론 (4축)

- **SDD** (Specification-Driven Development): 코드 변경 전 설계 문서 우선
- **TDD** (RED → GREEN → REFACTOR, 70% 커버리지 목표)
- **하네스 엔지니어링**: 8-Layer 피드백 루프 (CLAUDE.md / 검토 질문지 / PostToolUse / PreCommit / git pre-commit / CI / 3+1 합의 / Human review)
- **3+1 멀티에이전트 합의**: Agent A (구현) + Agent B (안전성) + Agent C (대안) → Reviewer 종합

### 1.3 권위 위계 (영구)

```
Constitution > ADR > SDD > Harness Gates > Hermes > Worker Agents
```

본 위계는 **ADR-011 §2.3** 에 영구 권위로 명시. **Hermes 는 시스템의 root of trust 가 아니라 검증 대상**.

---

## 2. 현재 G1b / G2 / G3 / G4 상태 요약 (2026-05-09 시점)

### 2.1 4 게이트 진행 상태

| 게이트 | 정의 | 현 상태 (2026-05-09) |
|-------|------|---------------------|
| ~~G1a~~ | Hermes native redaction → DB | ❌ FAIL 확정 (폐기, ADR-011 §2.2 권위) — Phase 0 R-1 evidence (`agent/redact.py` docstring "for logs and tool output", redact import 25개 모두 비-DB, `hermes_state.py` redact import 0건) |
| **G1b** | DB-level fallback (SQLCipher BEFORE INSERT trigger + REGEXP UDF + Tier-1 42 catalog) | ✅ **PASS** (2026-05-07, R-2~R-7 6단계 완료 + R-6 actual run `25482284523` 24초 PASS, 42/42 catalog, leak 0). **Implementation/Runtime PASS** |
| **G2** | 6 거버넌스 사전조건 (P1~P8 위반 경로 매핑 + GP-1~GP-6 강제 메커니즘) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)**. GP-1 = G1b PASS evidence 흡수 (Tier-1 한정). **GP-2 ~ GP-6 = DESIGN PASS / IMPLEMENTATION PENDING** |
| **G3** | "Hermes ≠ root of trust" 운영 구현 (22 권한 / 자기참조 차단 / Evidence 결정 5 운영 규칙) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)**. **운영 구현 = DESIGN PASS / IMPLEMENTATION PENDING** (실 hook / wrapper / CI step 미작성) |
| **G4** | Provider-agnostic Memory/Skill 형식 (Memory scope 4 / Skill schema 17 필드 / JSONL hash chain) | ✅ **Design/Governance Gate PASS (Bundled, 2026-05-09)**. **§4 라운드트립 + migration script = DESIGN PASS / IMPLEMENTATION PENDING**. PR-2 (2026-05-09 후속 3) 로 **§4.2 schema 11 필드 + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차 보강 완료** |

### 2.2 합산

```
4 게이트 Design/Governance Gate PASS = 4/4 (G1b PASS + G2/G3/G4 Design/Governance PASS Bundled)
4 게이트 Implementation/Runtime PASS = 1/4 (G1b 만 — GP-2~GP-6 / G3 운영 / G4 라운드트립 모두 IMPLEMENTATION PENDING)
Hermes PMO 격상 선언 = 미선언 (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 사람 리뷰 + 사용자 명시 결정 후 별도)
```

### 2.3 합의 인프라 적용 이력

| 합의 | 형태 | 외부 LLM |
|----|----|--------|
| G1b PASS 승격 (2026-05-07) | 단축 합의 (Reviewer-only) | 0 (R-7 SOP §7.3 답습) |
| G2/G3/G4 정식 PASS (2026-05-09) | 풀 3+1 + 외부 LLM 2 | cross-vendor (1) + Claude 인접 (1) |
| PR-1 본문 흡수 6건 (2026-05-09 후속 2) | 단축 합의 (Reviewer-only) | 0 (G2/G3/G4 합의 권위 *내부* 작업) |
| PR-2 ADR-012 + G4 §4 보강 (2026-05-09 후속 3) | 풀 3+1 + 외부 LLM 2 | cross-vendor (1) + Claude 인접 (1) |

**현 cross-vendor 의뢰 누적 = 2건** (G2/G3/G4 + PR-2). 본 의뢰 (C-14) = **3번째 cross-vendor 의뢰**, 단 P2 v3 정식 채택 진입 *전* 시점 한정 의무.

---

## 3. P2 v3 DRAFT 요약

`docs/architecture/hermes-adoption-design-v3.md` (12 섹션, 652 줄, **DRAFT**, 작성일 2026-05-07, 정식 채택 미발생).

### 3.1 본 v3 의 발생 사유

P2 v2 (`hermes-adoption-design.md`) §2.1.3 가정 ("외부 `pre_record` hook 공식 지원") 이 Phase 0 Day 1 사실 확인 (Hermes v0.12.0 `add_pre_record_hook` API grep 0건) 에서 폐기됨. R-2 ~ R-7 6단계 evidence + R-6 GitHub Actions actual run `25482284523` PASS + G1b PASS 권위 흡수 + Hermes PMO 구조 사전 정의 + G2/G3/G4 잔여 게이트 entry/exit 명세.

### 3.2 본 v3 의 *하는* 것 (7 항목)

1. P2 v2 §2.1.3 가정 코드 미존재 사실 명시 흡수
2. R-2 ~ R-7 + R-6 actual run PASS evidence 흡수
3. G1b PASS (2026-05-07) 권위를 P2 본문 권위로 반영
4. Hermes PMO 구조 명세 (활성화 후보 대상의 *사전 정의*, 활성화 자체는 별도)
5. G2 / G3 / G4 잔여 게이트 정의 + entry/exit 기준 + 산출 후보
6. 동시 갱신 ADR 매트릭스 (ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 cross-reference)
7. `system-identity-prequel.md` 흡수 후 archived 처리 경로 명시

### 3.3 본 v3 의 *하지 않는* 것

- ❌ **Hermes PMO 격상 선언** — 4 게이트(G1b ✅ + G2 ⏳ + G3 🟡 + G4 ⏳) 모두 통과 + 사용자 명시 결정 후 별도 발행 (DRAFT 시점 기준)
- ❌ G2 / G3 / G4 PASS 선언 (본 v3 는 *정의*까지만)
- ❌ ADR-008 본문 / ADR-009 / ADR-010 / ADR-011 본문 자동 갱신
- ❌ `system-identity-prequel.md` 자동 폐기 (정식 채택 시점)
- ❌ P2 v2 자동 폐기
- ❌ 자동 정책 변경 (T3)
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ Phase 진입 결정

### 3.4 본 v3 의 §3 4 게이트 *DRAFT 시점* 진행 상태 (2026-05-07 기준)

본 v3 §3 본문 안에는 다음 표가 있음:

| 게이트 | 정의 | DRAFT 시점 (2026-05-07) |
|-------|------|---------------------|
| G1a | Hermes native redaction → DB | ❌ FAIL 확정 (폐기) |
| G1b | DB-level fallback | ✅ PASS (2026-05-07 승격) |
| G2 | 6 거버넌스 사전조건 | ⏳ **미작성** (DRAFT 시점) |
| G3 | "Hermes ≠ root of trust" 운영 구현 | 🟡 **ADR-011 §2.3 권위 확정 / 운영 구현 미작성** |
| G4 | Provider-agnostic Memory/Skill | ⏳ **미작성** |

**중요**: 본 v3 가 DRAFT 로 작성된 시점 (2026-05-07) 이후, **G2 / G3 / G4 DRAFT 작성 + 검토 APPROVE + 정식 PASS (Design/Governance Gate Bundled, 2026-05-09)** 가 *별도로* 진행되어 §2.1 의 현 시점 상태가 갱신되었습니다. 즉 본 v3 §3 본문은 *DRAFT 시점* 진행 상태이며, **현 시점 (2026-05-09 후속 3) 진행 상태는 §2.1 표 답습** 입니다.

본 v3 본문 갱신 (DRAFT → 정식) 자체가 본 의뢰 평가 대상.

### 3.5 본 v3 §2 Hermes PMO 구조 (활성화 후보 대상의 사전 정의)

본 v3 §2 는 Hermes PMO 격상 *선언* 이 아니라, 4 게이트 통과 후 *활성화 가능* 한 PMO 의 *구조 사전 정의*. §2.1.1 10 책임 후보 (작업 분배 / Phase 0 질문지 생성 / Skill 추출 / Memory 관리 등) + §2.1.2 6 *하지 않는* 것 (Constitution / ADR 자동 작성 금지 등) + §2.6 격상 절차 7 단계.

### 3.6 본 v3 §4 / §5 / §6 = G2 / G3 / G4 본 v3 시점 *정의*

본 v3 §4 (G2) / §5 (G3) / §6 (G4) 본문은 *DRAFT 시점* 의 정의. **현 시점 G2 / G3 / G4 Design/Governance Gate PASS (Bundled, 2026-05-09) 이후, 각 게이트 자체 본문 (`governance-preconditions.md` / `hermes-not-root-of-trust-runtime.md` / `provider-agnostic-memory-skill-design.md`) 이 정식 산출**. 본 v3 §4 / §5 / §6 = 게이트 본문 *cross-reference* 까지.

### 3.7 본 v3 §7 동시 갱신 ADR 매트릭스

- ADR-008 본문: 차단조건 #1 충족 메커니즘 갱신 + R-2~R-7 cross-reference (별도 PR)
- ADR-009: 자체 Adapter v2.0 진입조건 (별도 PR — C-N)
- ADR-010: SQLCipher Vault HSM 키 관리 (별도 PR)
- ADR-011: 모법 (cross-reference 추가, 별도 PR)
- ADR-012: **Evidence Ledger Protection** (PR-2 에서 신규 발행, 2026-05-09 후속 3)

### 3.8 본 v3 §10 영구 핵심 제약 (5 제약, 변동 없음)

1. Provider Liquidity (헌법 5조 관용)
2. Hermes ≠ root of trust (ADR-011 §2.3)
3. 메타포 강제 금지 (system-identity-prequel §7)
4. 자동 정책 변경 금지 T3 (ADR-011 §2.4)
5. 수단/목적 분리 (ADR-011 §2.1 (a)~(d) + (e))

### 3.9 본 v3 §11 변경 절차

DRAFT 상태 해제 → 정식 채택 = **단축 합의 또는 풀 3+1 합의 APPROVE** + 외부 LLM 의견 권장 (G3 §4.4.2 답습) + ADR-008 부록 B Amendment cross-reference + P2 v2 archived + system-identity-prequel archived.

### 3.10 본 v3 §12 메타 편향 자기진단

본 v3 자체가 *자기 작성 산출* (P2 v2 → P2 v3 동일 컨텍스트). 자기 검증 한계 인지 + 외부 LLM 1+ 권장 명시.

---

## 4. ADR-012 와 G4 Hash Chain 보강 요약 (2026-05-09 후속 3 PR-2 산출)

### 4.1 ADR-012: Evidence Ledger Protection (신규 발행)

`docs/decisions/ADR-012-evidence-ledger-protection.md` (~700 줄). 풀 3+1 + 외부 LLM 2 합의 (5/5 입력 APPROVE WITH CONDITIONS).

**12 보호 원칙 + 4 매트릭스 + 5 추가 의무**:

- **원칙**: Evidence Ledger 는 PASS *성립 조건* (보조 기록 아님). Hermes 가 승인 / 수정 불가. 변조 가능성 = G3 root-of-trust 직접 훼손. *형식적 무결성* 까지만 (의미적 정확성 별도).
- **11 필드 schema** (10 G4 §4.2 + `event` 신규): `type` / `scope` / `id` / `schema_version` / `ts` / `agent` / **`event`** / `content` / `evidence_refs` / `prev_hash` / `hash`
- **17 enum 후보** (MVP 12 의무): `memory_write` / `skill_proposed` / `skill_approved` / `skill_promoted` / `skill_revoked` / `gate_pass` / `gate_fail` / `external_llm_received` / `evidence_forgery_detected` / `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` 외 5
- **Layer 1~5 다층 강제**: Hash chain MANDATORY + Git append-only MANDATORY + Signed RECOMMENDED MVP / MANDATORY multi-host + CI 회귀 + External anchor RECOMMENDED
- **Canonical JSON**: RFC 8785 JCS Primary + `jq -S -c` Fallback + test corpus 의무
- **Genesis hash**: `sha256("genesis:<scope>:<schema_version>")` MVP + 0.2 진입 시 재정의 (canonical_json with 4 fields)
- **prev_hash 검증 실패**: BLOCK + manual review + 새 `event: chain_violation_detected` entry append (자동 revert 금지 — T3 위반)
- **Full Rewrite 5 Layer 방어**: hash chain + denyNonFastForwards + pre-commit hook + CI line deletion 감지 + external anchor (RECOMMENDED)
- **Round-trip Tier-based**: T2 (로컬 promotion) hash 일치 STRICT / T3 (cross-vendor migration) 의미 보존 + 사용자 명시 review + 정책/권한/증거 손실은 BLOCK
- **Migration 검증 실패**: BLOCK + 원본 보존 + 새 `event: migration_failed` entry + manual
- **Hermes 변조 차단 매트릭스 4항목**: Hermes-originated entry / 파일 변조 / git commit / external LLM response 위조
- **Provider Liquidity 4-way → 5-way Multi-layer Defense** (Evidence 형식 layer 추가)
- **External LLM response**: `agent="user"` 강제 + `event: external_llm_received` entry 의무
- **C-14 cross-vendor 의무**: P2 v3 정식 채택 진입 *전* GPT-5.x or Gemini blind 의뢰 1+ 의무 (영구) — **본 의뢰가 그 의무의 실현**

### 4.2 G4 §4.2 / §4.4 / §4.6 보강 (ADR-012 동일 PR commit)

- **§4.2**: schema 10 → 11 필드 (`event` 신규), 17 enum 후보, provider-neutral 강제, timestamp monotonicity (외부 LLM 2 C-15)
- **§4.4**: Layer 1~5 다층 강제 본문 + RFC 8785 JCS Primary + jq fallback + 라이브러리 후보 (Python `pyjcs` / Node `canonicalize` / Go `cyberphone/json-canonicalization`) + Test corpus 의무 + Genesis Hash MVP+0.2 전이 + prev_hash 검증 실패 BLOCK + Full Rewrite 5 Layer
- **§4.6**: Tier-based 검증 + 3 ledger entry 형식 (`roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`) + 자동화 vs 사용자 review 분리 + JSONL Export/Import 무결성 + Migration 검증 실패 rollback (BLOCK + manual + `migration_failed`)

---

## 5. P2 v3 정식 채택 전 검토 질문 (필수 — 9 차원)

다음 9 차원으로 평가해 주십시오. 각 차원에 *명확한 판정* + *근거* + *식별된 위험 / 결함 / 개선 권고* 를 제시해 주십시오.

### 5.1 차원 1 — P2 v3 DRAFT 의 *DRAFT 시점* vs *현 시점* 정합성

본 v3 §3 본문 = DRAFT 시점 (2026-05-07) 4 게이트 진행 상태. 현 시점 (2026-05-09) 4 게이트 진행 상태는 §2.1 (본 의뢰 §2) 답습. **본 v3 가 정식 채택 시 §3 본문 갱신 의무가 있는가, 또는 *DRAFT 시점 사실 보존* 으로 유지하는 것이 정당한가?**

### 5.2 차원 2 — Hermes PMO 구조 §2 사전 정의의 적정성

본 v3 §2 는 *격상 선언이 아닌* 활성화 후보의 *구조 사전 정의*. §2.1.1 10 책임 후보 + §2.1.2 6 *하지 않는* 것 + §2.6 7 단계 격상 절차. **사전 정의 자체가 활성화 *시사* 효과를 발생시키는가? 정의 vs 시사 분리가 충분한가?**

### 5.3 차원 3 — ADR-012 + G4 §4 보강 흡수의 cross-reference 정합성

본 v3 §7 동시 갱신 ADR 매트릭스에 ADR-012 추가 (PR-2 에서 신규 발행). G4 §4.2 / §4.4 / §4.6 보강도 PR-2 에서 완료. **본 v3 정식 채택 시점에 §7 갱신 + §6 (G4 정의) cross-reference 갱신은 본 v3 정식 채택 합의 *내부* 작업으로 충분한가, 또는 *별도 PR 묶음* 으로 분리해야 하는가?**

### 5.4 차원 4 — DESIGN PASS / IMPLEMENTATION PENDING 상태에서의 정식 채택 적정성

현 4 게이트 = Design/Governance Gate PASS (Bundled) **만**. Implementation/Runtime PASS = 1/4 (G1b 만). 즉 GP-2 ~ GP-6 / G3 운영 구현 / G4 라운드트립 + migration script = *설계 승인까지만*, 실 구현 미수행. **이 상태에서 P2 v3 (Hermes Adoption Design) 정식 채택이 정당한가, 또는 Implementation/Runtime PASS 1+ 추가 후로 미뤄야 하는가?**

### 5.5 차원 5 — 자기참조 위험 통제 충분성

본 프로젝트의 모든 합의 (4 게이트 DRAFT 검토 + G2/G3/G4 정식 PASS + PR-1 + PR-2) 가 Claude 패밀리 컨텍스트 작성. 본 cross-vendor 의뢰 (C-14) 가 3번째 cross-vendor 의뢰. **본 의뢰 1건만으로 P2 v3 정식 채택 진입의 자기참조 위험이 충분히 통제되는가? 또는 추가 cross-vendor 의뢰 (Gemini + GPT 동시 등) + 사람 리뷰가 의무인가?**

### 5.6 차원 6 — 영구 핵심 제약 5건 보호 (P2 v3 정식 채택 후 보존성)

본 v3 §10 영구 핵심 제약 5건 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리). **본 v3 정식 채택 + P2 v2 archived + system-identity-prequel archived 시점에 5 제약 보존 매커니즘이 충분한가, 또는 추가 보호 (예: ADR Amendment 의무 강화) 필요한가?**

### 5.7 차원 7 — Hermes PMO 격상 vs P2 v3 정식 채택 분리

본 v3 §2 는 *격상 선언이 아닌* 사전 정의. 정식 채택 = *문서 채택* 까지, 격상 = *Hermes 활성화* 영역. **본 분리가 명료한가, 또는 정식 채택이 격상의 *사실상 도화선* 이 될 위험이 있는가?** 정식 채택 후 격상 사이의 시간/조건 분리가 충분한가?

### 5.8 차원 8 — Cross-vendor 의뢰의 *blind 강도* 적정성

본 의뢰는 *blind 강도가 가장 높음* — 내부 Agent / Reviewer / 사용자 의도 / APPROVE 유도 모두 미포함. **이 강도가 적정한가, 과도한가, 부족한가?** 외부 LLM 이 본 자료만으로 합리적 평가 가능한 *충분한 정보* 를 제공받았는가?

### 5.9 차원 9 — 본 의뢰 후속 (P2 v3 정식 채택 합의) 의 합의 형태 권고

본 v3 §11 변경 절차 = 단축 합의 또는 풀 3+1 합의. **본 v3 정식 채택 합의는 단축 합의 충분한가, 또는 풀 3+1 + 본 cross-vendor 의뢰 응답 + 추가 외부 LLM (사람 리뷰 또는 다른 vendor) 의무인가?**

### 5.10 최종 판정

다음 중 하나를 *명시* 해 주십시오:
- **APPROVE**
- **APPROVE WITH CONDITIONS** (조건 enumeration)
- **PARTIAL** (어느 부분 진입 가능, 어느 부분 보류)
- **BLOCK** (결함 enumeration + 후속 조치 권고)

판정 근거는 §5.1 ~ §5.9 9 차원 모두 반영해 주십시오. 본 외부 LLM 의견은 본 프로젝트의 합의 인프라 (3+1 + Reviewer + 추가 외부 LLM) 의 *한 입력* 으로 사용됩니다.

---

## 6. 금지 사항 (사용자 명시 답습 — 본 의뢰 결과와 무관 영구 유지)

본 의뢰가 *어떤 판정* 을 받든, 다음은 *발생하지 않습니다*:

- ❌ **Hermes PMO 격상 선언** — 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도
- ❌ **P2 v3 정식 채택 자동 선언** — 본 의뢰 후 별도 합의 (단축 또는 풀 3+1) 필요
- ❌ **ADR-008 / 009 / 010 / 011 본문 자동 갱신** — cross-reference 만 가능, 본문 변경은 별도 PR
- ❌ **P2 v2 / system-identity-prequel.md archive 자동 처리** — 정식 채택 시점에
- ❌ **실 runtime code / migration script / hook 구현** — Implementation/Runtime PASS 별도
- ❌ **Tier-2 / Tier-3 catalog 자동 확장** — 별도 합의

---

## 7. 판정 형식 (요청 사항)

다음 구조로 응답해 주십시오 (분량 자유, 단 최소 §7.1 + §7.10 필수):

```
§7.1 사전 점검 — 본 의뢰자의 메타 편향 통제 강도 평가 (강하다/적정/약하다 중)
§7.2 차원 1 (DRAFT vs 현 시점 정합성) 평가 + 판정
§7.3 차원 2 (Hermes PMO 사전 정의 적정성) 평가 + 판정
§7.4 차원 3 (ADR-012 + G4 §4 cross-reference 정합성) 평가 + 판정
§7.5 차원 4 (DESIGN PASS / IMPLEMENTATION PENDING 상태에서 정식 채택 적정성) 평가 + 판정
§7.6 차원 5 (자기참조 위험 통제 충분성) 평가 + 판정
§7.7 차원 6 (영구 핵심 제약 5건 보호 보존성) 평가 + 판정
§7.8 차원 7 (Hermes PMO 격상 vs P2 v3 정식 채택 분리) 평가 + 판정
§7.9 차원 8 (Cross-vendor blind 강도 적정성) + 차원 9 (정식 채택 합의 형태 권고) 평가
§7.10 최종 판정 (APPROVE / APPROVE WITH CONDITIONS / PARTIAL / BLOCK) + 핵심 조건 enumeration (조건부 시) 또는 결함 enumeration (BLOCK 시)
§7.11 (선택) 본 검토자 자기 노출 — 사각지대 / 한계 / 추가 검토 권고 사항
```

각 차원 평가는 *근거 명시* 가 핵심. *결론 자체* 보다 *결론에 도달한 추론 경로* 가 본 합의 인프라에 가치 있습니다.

---

## 8. 메타 — 본 의뢰의 *blind 강도* 명시

본 의뢰는 다음 측면에서 *의도적으로 정보를 제한* 합니다:

| 항목 | 본 의뢰 |
|----|----|
| 내부 Agent A / B / C 분석 결과 | ❌ 미포함 (의도된 배제) |
| 내부 Reviewer 종합 결론 | ❌ 미포함 (의도된 배제) |
| 사용자 (의뢰자) 의 선호 / 의도 / 원하는 결론 | ❌ 미포함 (의도된 배제) |
| APPROVE 유도 표현 / 답안 시사 | ❌ 미포함 (의도된 배제) |
| 다른 외부 LLM 응답 (G2/G3/G4 합의 + PR-2 합의 응답 4건) | ❌ 미포함 (의도된 배제) |

**제공된 정보**:

| 항목 | 본 의뢰 |
|----|----|
| 시스템 목적 (1인 개발자 메타-템플릿) | ✅ 포함 |
| 4 게이트 현 진행 상태 | ✅ 포함 |
| P2 v3 DRAFT 핵심 12 섹션 요약 | ✅ 포함 |
| ADR-012 + G4 §4 보강 PR-2 산출 요약 | ✅ 포함 |
| 9 평가 차원 + 4 판정 옵션 | ✅ 포함 |
| 영구 금지 사항 6건 | ✅ 포함 |

본 *blind 강도* 자체에 대한 평가도 §7.1 의 일부입니다.

---

**검토 의뢰 작성일**: 2026-05-09 (PR-2 머지 + push 후속)
**의뢰 자료 버전**: v1
**자기충족성**: 본 문서만으로 평가 가능 (첨부 자료 없음)
**의뢰 채널**: 사용자가 직접 비-Claude vendor (GPT-5.x / Gemini / 다른 강력한 LLM) 에 paste
**응답 저장 예정**: `docs/external-review/2026-05-XX-c14-cross-vendor-p2v3-pre-adoption-response.md` 또는 본 세션 직접 paste
**선행 의뢰 자료** (참조 *불필요*, 본 의뢰 평가에 영향 *없음*):
- `docs/external-review/2026-05-09-g2g3g4-promotion-request.md` (G2/G3/G4 정식 PASS 합의)
- `docs/external-review/2026-05-XX-pr2-evidence-ledger-request.md` (PR-2 ADR-012 + G4 hash chain)
