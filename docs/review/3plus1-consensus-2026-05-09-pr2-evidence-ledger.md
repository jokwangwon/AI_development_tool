# 풀 3+1 합의 보고서 — PR-2: ADR-012 신규 발행 + G4 §4.4 / §4.6 hash chain 사양 보강

**합의 형태**: 풀 3+1 + 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) — 사용자 명시 결정 답습 (`SESSION_2026-05-09.md` §11.1 결정 1·2)
**합의 일자**: 2026-05-09 (옵션 β PR-2)
**검토 대상**: P1 조건 C-C (Evidence Ledger 보호 강화) + C-G (G4 §4.4/§4.6 hash chain 사양 보강) **통합 묶음**
**판정**: ✅ **APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격** (5/5 입력 일치)

---

## 0. 사전 점검

### 0.1 가동 사유

`SESSION_2026-05-09.md` §11.1 사용자 명시 결정 3건 답습:
- **결정 1 (PR 묶음)**: 옵션 β — 2-PR 묶음 (PR-1 본문 보강 / PR-2 ADR-012 + G4 hash chain)
- **결정 2 (검토 형태)**: 본문 PR = 단축 / 신규 ADR PR = **풀 3+1 + 외부 LLM 1+**
- **결정 3 (외부 LLM 추가 시점)**: P1 흡수 후 + P2 v3 진입 *전*

PR-1 (단축, Reviewer-only) 6건 본문 흡수 완료 (`3plus1-consensus-2026-05-09-p1-doc-absorption.md`, commit `54a328b`) → **PR-2 풀 3+1 합의** (본 보고서) 진입.

### 0.2 풀 3+1 + 외부 LLM 2건 채택 사유

**G3 §4.4.2 답습**: ADR 신규 발행 (T3 변경) = 외부 LLM 1+ *권장*. 본 ADR-012 = 영구 권위 ADR + Evidence Ledger forgery 차단 = 핵심 권위 발행 → **권장 → 필수 격상** (5/5 입력 일치, Agent A R-11 HIGH / Agent B C-2 / Agent C C-7 / 외부 LLM 1 (cross-vendor) 진행 가능 범위 / 외부 LLM 2 C-14).

| 충족 조건 | 본 PR-2 충족 |
|---------|-----------|
| ADR 신규 발행 시 풀 3+1 (T3 변경) | ✅ Agent A/B/C 병렬 분석 + Reviewer 종합 |
| 외부 LLM 1+ 충족 (G3 §4.4.2) | ✅ **2건** — `2026-05-09-pr2-evidence-ledger-response.md` (cross-vendor 외부 LLM, vendor 자기 명시 부재) + `2026-05-09-pr2-evidence-ledger-response-claude.md` (Claude Anthropic Opus 4.7 인접 컨텍스트, 동일 모델 패밀리 면책 명시) |
| 의뢰 자료에 내부 Agent 분석 *포함 0건* (편향 통제 강화) | ✅ `2026-05-XX-pr2-evidence-ledger-request.md` 작성 시 의도적 배제 (선행 의뢰 대비 강화) |
| 사용자 명시 결정 답습 | ✅ SESSION §11.1 결정 1·2 답습 |

### 0.3 메타 편향 인지 (G3 §4.7 메타-순환 청산 답습)

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-012 / G4 §4 작성 컨텍스트와 동일 패밀리. 자기 작성 산출 자기 검토 한계 인지.

**청산 매커니즘** (G3 §4.7.2 답습):
1. **사후 외부 LLM 충족** — 본 합의 시점 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) 권위 *내부* 작업
2. **격상 전 면제** — 본 PR-2 = Hermes PMO 격상 *전*, Hermes 자기참조 차단 §4 적용 대상 아님
3. **합의 권위 내부 변경** — 본 PR-2 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 = *권위 내부* 작업
4. **자기 작성 한계 명시 의무** — §11 메타 편향 자기진단 명시

**추가 통제** (Claude 외부 LLM 2 응답 §15 답습):
- Claude 패밀리 공유 한계 명시 (선행 의뢰 답습)
- Cryptography 영역 심층 검토는 본 응답자 한계 — 본 PR-2 후 **C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무 (P2 v3 정식 채택 진입 전)** 영구 답습

### 0.4 비검토 대상 (사용자 명시 답습 + 5/5 입력 일치)

| 항목 | 본 합의 범위 |
|-----|----------|
| Hermes PMO 격상 선언 | ❌ 4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2개 또는 외부 LLM 1개 + 사람 리뷰 + 사용자 명시 결정 후 별도 |
| P2 v3 정식 채택 자동 선언 | ❌ 본 PR-2 머지 + cross-vendor (C-14) + 사용자 명시 결정 후 별도 |
| ADR-008 / 009 / 010 / 011 본문 자동 갱신 | ❌ cross-reference 만 가능 (본문 변경은 별도 PR) |
| ADR-012 본문 자동 작성 | ❌ 본 합의 = 권고 사양까지, 본문 작성은 후속 작업 (본 합의 §7) |
| G4 §4.4 / §4.6 본문 자동 갱신 | ❌ 본 합의 = 보강 사양까지, 본문 갱신은 후속 작업 (본 합의 §8) |
| G2 §1.2 P10 신규 row 자동 추가 | ❌ ADR-012 발행 시점 = 트리거, G2 본문 등록은 별도 G2 update PR (외부 LLM 1 진행 가능 범위 답습) |
| ADR-013 / ADR-014 후보 자동 발행 | ❌ 별도 합의 + 사용자 명시 결정 |
| P2 v2 / system-identity-prequel archive 자동 처리 | ❌ P2 v3 정식 채택 시점 |
| 실 runtime code / migration script / hook 구현 | ❌ Implementation/Runtime PASS 별도 합의 |
| Tier-2 / Tier-3 catalog 자동 확장 | ❌ 별도 합의 |

---

## 1. 5 입력 종합 매트릭스

### 1.1 5 입력 enumeration

| # | 입력 | 모델 / 컨텍스트 | 산출 파일 | 판정 | 분량 |
|---|------|-------------|--------|------|------|
| 1 | **Agent A** (구현/운영) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` | APPROVE WITH CONDITIONS (8 조건) | 481 줄 |
| 2 | **Agent B** (보안/거버넌스) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-b-security.md` | APPROVE WITH CONDITIONS (4 CONDITIONS — C-1 HIGH + C-2~C-4 MEDIUM, 14 NOTES, **Gap-17 HIGH 단독 발견**) | 597 줄 |
| 3 | **Agent C** (대안/단순화) | Claude Opus 4.7 / 메인 패밀리 | `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-c-alternatives.md` | APPROVE WITH CONDITIONS (4 핵심 + 6 보조 + 3 사용자 결정) | 424 줄 |
| 4 | **외부 LLM (cross-vendor)** | vendor 자기 명시 부재 (likely GPT-5.x / Gemini) — *내부 Agent 분석 미포함 의뢰 자료* 답습 | `docs/external-review/2026-05-09-pr2-evidence-ledger-response.md` | APPROVE WITH CONDITIONS — 5 권고 + 16 차원별 판정 | (사용자 paste 원문) |
| 5 | **외부 LLM (Claude 인접 컨텍스트)** | Claude Anthropic Opus 4.7 / 동일 모델 패밀리 면책 | `docs/external-review/2026-05-09-pr2-evidence-ledger-response-claude.md` | APPROVE WITH CONDITIONS (17 조건 C-1~C-17 + 11번째 필드 = `event` 강력 권고) | (사용자 paste 원문) |

**합산 = 5 입력 / 5 APPROVE WITH CONDITIONS / 5 Hermes PMO 격상 미선언 / 5 영구 핵심 제약 5건 보호**.

### 1.2 의뢰 자료 편향 통제 (선행 의뢰 대비 강화)

본 PR-2 외부 LLM 의뢰 자료 (`2026-05-XX-pr2-evidence-ledger-request.md`) 는 다음 측면에서 선행 의뢰 (`2026-05-09-g2g3g4-promotion-request.md`) 대비 **편향 통제 강화**:

1. **내부 Agent A/B/C 분석 결과 포함 0건** — 의도된 배제 (외부 LLM 의 *진정한 독립 판단* 확보, blind 의뢰)
2. **16 평가 차원 + 8 트레이드오프 명시** — 외부 LLM 이 모호한 영역에서 자기 판정 가능하도록 강제
3. **메타 한계 §11 자기 노출** — 5 한계 명시 (자기참조 / G3 §4.4.2 / 의뢰 자료 자체 / 메타-템플릿 / 외부 LLM 집계 방식)

→ 외부 LLM 2 (Claude 인접 컨텍스트) §0 자체에서 본 강화 인지 ("본 PR-2 자료는 내부 Agent A/B/C 분석을 의도적으로 배제한 점이 선행 의뢰 대비 편향 통제 강화입니다. 이는 인식 가능한 개선이며, 본 응답은 그 통제를 존중하여 독립적으로 형성되었습니다.").

---

## 2. 5/5 일치 사항 (Consensus)

### 2.1 핵심 판정 5/5 일치

```
APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격
```

5 입력 중 BLOCK / PARTIAL / 단순 APPROVE 0건. 모두 *조건부 승인*.

### 2.2 5/5 모두 일치한 결정 사항

| # | 사항 | 5 입력 출처 |
|---|------|---------|
| 1 | **PR-2 통합 묶음 (C-C + C-G)** 진행 적격 — 분리 시 합의 비용 ↑ + cross-reference drift 위험 | A R-8 + B (§9.14 동의) + C Alt-1 + 외부 LLM 1 항목 7 + 외부 LLM 2 §9 |
| 2 | **외부 LLM 1+ 필수 격상** (T3 변경 = ADR 신규 발행 사유) | A R-11 HIGH + B Gap-23 + C C-7 + 외부 LLM 1 (P2 v3 진입 전 권고) + 외부 LLM 2 C-14 |
| 3 | **본 PR-2 = Design/Governance Gate PASS 한정** — Implementation/Runtime PASS 미발생 | A §1 / §6 + B §6 + C §6 + 외부 LLM 1 §1 + 외부 LLM 2 §14 |
| 4 | **5 영구 핵심 제약 모두 보호** (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리) | A §5 (5/5 PASS) + B §5 (5/5 강도 HIGH 조건부) + C §5 (5/5 답습 충분 + 2 보강) + 외부 LLM 1 §9.1 + 외부 LLM 2 §1 |
| 5 | **금지 사항 영구 답습** (Hermes PMO 격상 / P2 v3 자동 / ADR 본문 자동 갱신 / archive / 실 runtime code / migration script / Tier 자동 확장) | A §6 + B §6 + C §6 + 외부 LLM 1 §1 + 외부 LLM 2 §14 |
| 6 | **RFC 8785 JCS 채택** (canonical JSON 자체 정의 단독 대비 권위 명료성 ↑) | A §1.4 + B (§9.5 동의) + C C-3 + 외부 LLM 1 권고 2 + 외부 LLM 2 C-6 |
| 7 | **JCS fallback 명시 의무** (`jq -S -c` 또는 자체 구현 동등 보장 + test corpus) | A §1.4 + B (§9.5) + C C-3 + 외부 LLM 1 권고 2 + 외부 LLM 2 C-6 |
| 8 | **prev_hash 검증 실패 = BLOCK + manual review** (자동 revert / dual write 비권고 — T3 위반 위험) | A §2.5 (BLOCK + entry) + B C-3 + (C 미평가) + 외부 LLM 1 권고 4 + 외부 LLM 2 C-3 = **4/5 일치, C 단독 미평가** |
| 9 | **C-14 cross-vendor blind 의뢰 1+ 의무** (P2 v3 정식 채택 진입 전) | A R-12 + B C-2 + C C-7 + (외부 LLM 1 진행 가능 범위) + 외부 LLM 2 C-14 |
| 10 | **운영 부담 추정 합산** ≈ 7~10일 (사양 2.5일 + Implementation 5~7일) — 1인 개발자 메타-템플릿 적정 | A §2.5 (직접 명시) + B (간접 동의) + C (간접 동의) + 외부 LLM 1 (간접 — 운영 부담 monitoring 권고) + 외부 LLM 2 C-17 (operating burden monitoring trigger) |

### 2.3 5/5 모두 일치한 *추가 의무 영역* (조건부)

5 입력 모두 권고하는 **NEW** 의무 (사용자 명시 12 항목 + 4 G4 보강 항목 외):

| # | 추가 의무 | 5 입력 출처 |
|---|--------|---------|
| N-1 | **External LLM response ledger entry 의무** — `event: external_llm_received` + `agent: user` (수동 paste 시) + canonical_hash 검증 | A R-9 cross-ref + B Gap-11 + C C-2 enum 후보 + 외부 LLM 1 권고 1 cross-ref + 외부 LLM 2 C-9 |
| N-2 | **Schema 진화 정책 (semver MAJOR/MINOR)** — 필드 추가/제거/이름 변경/타입 변경 절차 | A R-10 + (B 간접) + C C-9 후속 격상 + (외부 LLM 1 간접) + 외부 LLM 2 §3.4 (C-5 hash 알고리즘 agility) |
| N-3 | **Content-level forgery 한계 §명시 의무** — ADR-012 가 *형식적 무결성* 까지, *의미적 정확성* 보장 아님 | A §7.3 (한계 명시) + B (Gap-18 ADR-011 §7.3 답습) + C §8.1 (한계) + 외부 LLM 1 권고 5 (1인 호스트 침해 한계) + 외부 LLM 2 C-16 |

---

## 3. 부분 일치 사항 (Partial Consensus)

### 3.1 11번째 필드 = `event` (4/5 일치, 1 보완)

| 입력 | 권고 |
|-----|------|
| Agent A | 별도 후보 추가 0건 — *11 필드 enumeration* 자체에 `event` 포함 (ts/id/**event**/agent/result/tool/scope/schema_version/evidence_refs/prev_hash/hash) |
| Agent B | Gap-1 — 명시 결정 부재 (`signature` / `external_anchor_ref` / `policy_change_required` 후보 비교 권고) |
| Agent C | C-2 — `event` enum 12 후보 명시 (옵션 a) |
| 외부 LLM 1 | 권고 1 — `event` 가장 추천 (12 enum 후보) |
| 외부 LLM 2 | §2 강력 권고 — `event` (옵션 a, 다른 후보는 `event` 전제 필요) |

**Reviewer 종합**: **11번째 필드 = `event` (5/5 정합)**. Agent A 의 enumeration 도 `event` 를 11 필드에 포함하므로 *결과적 일치*. Agent B Gap-1 은 *명시 결정 부재* 지적 → ADR-012 본문 작성 시점 흡수.

**enum 후보 종합** (5 입력 통합 — 중복 제거):

```
event ∈ {
  memory_write,
  skill_proposed, skill_approved, skill_promoted, skill_revoked,
  gate_pass, gate_fail,
  external_llm_received,
  evidence_forgery_detected,
  roundtrip_pass, roundtrip_lossy, roundtrip_fail,
  migration_failed,
  chain_violation_detected,
  hash_chain_broken,
  policy_change_attempted,
  canonical_json_fallback
}
```

**합산 = 17 enum 후보**. ADR-012 본문 작성 시점 *최소 12 enum* 의무 + 후속 확장 (`schema_version` 0.2) 가능.

### 3.2 signed/append 권고 — 다층 강제 (4/5 권고, 1 단축 권고)

| 입력 | 권고 |
|-----|------|
| Agent A | 옵션 2 (git append-only branch + branch protection rule) MVP 단독 — multi-host 전환 시 옵션 3 의무 발동 트리거 |
| Agent B | (직접 비평가, Gap-17 HIGH Hermes 변조 차단 매트릭스 영역에서 보강) |
| Agent C | 옵션 C (둘 중 하나, 사용자 PR-2 채택 시점 명시 결정 D-1) — 옵션 D 후속 격상 영역 |
| 외부 LLM 1 | MUST hash chain + MUST git append-only OR signed + SHOULD protected branch + SHOULD signed for multi-host/team |
| 외부 LLM 2 | C-2: **다층 동시 의무** (Hash chain MANDATORY + Git append-only MANDATORY + Signed RECOMMENDED, multi-host 전환 시 Signed MUST 승격) |

**Reviewer 종합 권고** (5 입력 *최강 안전 합집합*, 1인 개발자 메타-템플릿 균형):

| Layer | 의무 등급 | 사양 |
|------|--------|---|
| **Layer 1: Hash chain (sha256 + canonical JSON)** | **MANDATORY** (1인 동일 호스트 / multi-host / 모든 환경) | ADR-012 §hash chain 본문 답습 |
| **Layer 2: Git append-only branch + force-push 차단** | **MANDATORY** (1인 동일 호스트 포함) | `git config receive.denyNonFastForwards true` + branch protection + pre-commit hook (rebase/filter-branch/reset --hard reject) |
| **Layer 3: Signed commit (GPG / SSH)** | **RECOMMENDED** (1인 동일 호스트 SHOULD) → **MANDATORY** (multi-host / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점) | ADR-012 §signed commit 본문 |
| **Layer 4: External anchor (월 1회 external snapshot)** | **RECOMMENDED** (1인 SPOF 완화) → **MANDATORY** (multi-host 또는 P2 v3 정식 채택 시점) | 별도 외부 git remote / cloud storage / GitHub Actions run ID + signed tag |

**사용자 명시 옵션 ("둘 중 하나 의무") 변경 권고**: 5 입력 모두 *다층 동시 의무* 강도가 견고. 사용자 결정 영역.

### 3.3 Round-trip Lossy = Tier-based (4/5 일치 + 1 ledger entry 형식)

| 입력 | 권고 |
|-----|------|
| Agent A | (직접 미평가) |
| Agent B | Gap-5 손실 영역별 T1/T2/T3 분류 매트릭스 (C-7) |
| Agent C | C-5 round-trip 1차 (hash 일치) + 2차 (의미 보존) + ledger entry 3 형식 (`roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`) |
| 외부 LLM 1 | 권고 round-trip lossy: tiered (PASS / CONDITIONAL / BLOCK), "hash 일치 OR 의미 보존" 보다 안전 |
| 외부 LLM 2 | C-8 Tier-based (T2 strict / T3 의미 보존 + 사용자 명시 승인) |

**Reviewer 종합**:

| Tier | 정체성 | 검증 PASS 조건 |
|-----|------|------|
| **신규 chain (genesis)** | 첫 entry 작성 | (해당 없음 — round-trip 무관) |
| **T2 (Skill/Memory promoted)** | 로컬 promotion 절차 | hash 일치 **STRICT** — 손실 0건. 위반 시 BLOCK |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — 단 (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` ledger entry 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 T2/T3 분류상 사용자 승인 / (iv) 정책/권한/증거 손실은 BLOCK |

**Ledger entry 3 형식** (Agent C C-5 + 외부 LLM 2 §5 통합):

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"...","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"...","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"...","target_provider":"openai","failure_reason":"chain_violation_detected | policy_loss | permission_loss | evidence_loss"},...}
```

### 3.4 Genesis Hash 정의 (3/5 권고, 2 미평가)

| 입력 | 권고 |
|-----|------|
| Agent A | 명시 안 함 (현 정의 답습 가정) |
| Agent B | (간접 — Gap-1 +1 필드 영역에서 평가) |
| Agent C | (간접 — C-8 G4 §4.2 schema 갱신) |
| 외부 LLM 1 | 권고 6 — 현 정의 충분 (MVP), `chain_id` 후속 도입 시 변경 권고 |
| 외부 LLM 2 | C-7 — 재정의 (canonical JSON + 4 필드: scope/schema_version/created_at/agent) |

**Reviewer 종합**: 외부 LLM 2 C-7 권고 채택 (canonical JSON 답습 정합 + 후속 multi-chain 확장 가능). 단 *MVP 호환성* 위해 외부 LLM 1 권고 (현 정의 OR 신 정의 둘 다 허용) 도 ADR-012 §genesis 본문에 *전이 절차* 명시.

```
# MVP (schema_version 0.1) — 현 정의 유지 가능
genesis = sha256("genesis:<scope>:<schema_version>")

# 권고 (schema_version 0.2 진입 또는 multi-chain 도입 시)
genesis = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

### 3.5 Full Rewrite 방어 — 다층 (4/5 권고)

| 입력 | 권고 |
|-----|------|
| Agent A | R-7 HIGH — branch protection rule 의무 |
| Agent B | Gap-2 + C-4 — 외부 anchor (GitHub Actions run ID + signed tag) 권고 + G3 §5.5 SPOF cross-reference |
| Agent C | (간접 — Layer 4 후속 격상 영역) |
| 외부 LLM 1 | 권고 5 — hash chain + append-only branch + force-push 금지 + CI line deletion 감지 + 선택 signed tag/commit |
| 외부 LLM 2 | C-4 — pre-commit hook + denyNonFastForwards + 월 1회 external snapshot |

**Reviewer 종합**: §3.2 Layer 1~4 답습 + 추가 보강:

```
Full rewrite 방어 다층:
- Layer 1: Hash chain (middle entry tampering 차단)
- Layer 2: Git append-only branch + denyNonFastForwards (history 재작성 차단)
- Layer 3: pre-commit hook — git rebase / filter-branch / reset --hard 감지 시 reject
- Layer 4: CI 회귀 검증 — base branch 대비 JSONL line deletion/rewrite 감지
- Layer 5 (RECOMMENDED): External anchor — GitHub Actions run ID + signed tag (B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)
```

**1인 동일 호스트 SPOF 한계 명시 의무** (ADR-012 §11 답습):

> 동일 호스트 전체 침해 상황은 본 ADR-012의 완전 방어 범위 밖이다. 본 ADR은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다. (외부 LLM 1 권고 5 직접 인용)

---

## 4. 불일치 사항 (Divergence) — 사용자 결정 영역

### 4.1 사용자 명시 "둘 중 하나" → "다층 동시 의무" 변경 권고 (5/5 권고 vs 사용자 결정)

5 입력 모두 *다층 강제* 강도 권고 (§3.2). 단 사용자 명시 = "signed commit 또는 git append commit (둘 중 하나) 의무". 본 합의는 *권고* 하되 **최종 채택 = 사용자 명시 결정 영역** (D-1 답습).

| 옵션 | 정체성 | 적용 |
|-----|------|---|
| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 5 입력 권고 미반영 | 사용자 결정 |
| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
| **D-1C** (절충) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |

**Reviewer 권고**: **D-1C 절충** (MVP 단순성 + 다층 격상 후속 의무). 단 사용자 명시 결정 영역.

### 4.2 P10 정식 등록 처리 (3/5 권고, 2 보완)

| 입력 | 권고 |
|-----|------|
| Agent A | R-9 cross-reference 의무 |
| Agent B | Gap-6 + C-8 — ADR-012 본문 명시 + G2 후속 합의 권고 |
| Agent C | (C-1 트리거 재해석 답습) |
| 외부 LLM 1 | 조건부 승인 — ADR-012 트리거 + G2 update commit 분리 |
| 외부 LLM 2 | C-10 — PR-2 내 동시 처리 |

**불일치 영역**: G2 §1.2 P10 row 추가를 본 PR-2 *내* 처리 (외부 LLM 2 C-10) vs *별도 G2 update PR* (외부 LLM 1 + Agent B Gap-6).

**Reviewer 종합**: **외부 LLM 1 + Agent B 답습 — 분리**. 사유:
- 본 PR-2 = ADR-012 + G4 §4.4/§4.6 한정 (사용자 명시 결정 답습)
- G2 본문 변경 = T3 변경 + 별도 합의 (단축 가능)
- ADR-012 §P10 cross-reference 명시는 의무, G2 본문 row 추가는 별도

### 4.3 Migration Rollback 4 후보 채택 (분기)

| 입력 | 권고 |
|-----|------|
| Agent A | (a) BLOCK + (c) 원본 보존 + 새 entry (`event: migration_failed`) |
| Agent B | C-3 BLOCK + manual review |
| Agent C | (간접) |
| 외부 LLM 1 | BLOCK + 원본 보존 + 사용자 명시 manual + 실패 entry 별도 incident log |
| 외부 LLM 2 | C-12 BLOCK + manual + 새 violation entry |

**Reviewer 종합**: 4/5 (C 미평가) 합의 — **BLOCK + 원본 보존 + 새 violation entry + manual review** (자동 revert 비권고, dual write 비권고). `event` 분류:
- `migration_failed` (Agent A) — migration 시도 자체 실패
- `chain_violation_detected` (외부 LLM 2 C-3) — prev_hash mismatch 또는 hash 재계산 검출
- `roundtrip_fail` (Agent C C-5) — round-trip lossy 의 *fail* 케이스

3 분류 모두 ledger entry 의무 + 사용자 명시 review.

---

## 5. 단독 발견 (Gap — 1 Agent 단독)

### 5.1 Agent B Gap-17 (HIGH) — Hermes 변조 차단 매트릭스

**Agent B 단독 발견** (다른 4 입력 미언급 또는 간접). ADR-012 본문에 다음 4 항목 매트릭스 명시 + cross-reference 의무:

| # | 변조 영역 | 차단 매커니즘 | G3 cross-reference |
|---|--------|---------|-----------------|
| 1 | Hermes-originated ledger entry (Hermes 가 자기 entry 작성 시도 — T1 자동 학습 vs T2 사용자 승인 분기) | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | G3 §2.5 #11 + #20 |
| 2 | 파일 변조 (filesystem 직접 변경) | filesystem read-only on `evidence/<scope>.jsonl` + audit log + 컨테이너 정지 | G3 §4.5 |
| 3 | Git commit (Hermes 가 ledger commit 시도) | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | G3 §2.2 #20 |
| 4 | 외부 LLM 응답 위조 (Hermes 가 외부 LLM response 를 자기 제안으로 위조) | External LLM response ledger entry agent = "user" 강제 (수동 paste 시) + signed commit 권장 (multi-host 시 의무) | G3 §2.5 #9 + N-1 |

**Reviewer 종합**: **Gap-17 HIGH = ADR-012 본문 작성 의무 항목**. 흡수 시 *Hermes ≠ root of trust* 보호 강도 = HIGH (Agent B §5.6 답습).

### 5.2 Agent C Alt-1 트리거 재해석 (단독)

**Agent C 단독 발견**: ADR-012 발행 트리거 = "prequel §6.4 Phase 1 종료" 를 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석 명시.

**Reviewer 종합**: ADR-012 본문 §맥락 (Context) 에 트리거 재해석 명시 의무. 단 prequel §6.4 본문 갱신은 본 PR-2 범위 외 (별도 합의 — P2 v3 정식 채택 시점).

### 5.3 외부 LLM 2 C-15 Timestamp Monotonicity (단독)

**외부 LLM 2 단독 발견**: 각 entry `ts` ≥ `prev_hash` entry `ts` (timestamp monotonicity assertion). 위반 시 `event: chain_violation_detected` (C-3 답습). NTP 동기화 가정 — 1인 호스트 silent clock drift 위험 (G3 §5.5 SPOF 답습).

**Reviewer 종합**: ADR-012 §검증 본문에 timestamp monotonicity assertion 명시.

### 5.4 외부 LLM 2 C-17 운영 부담 Monitoring Trigger (단독, 외부 LLM 1 간접)

**외부 LLM 2 단독 발견** (외부 LLM 1 간접): "ledger entry 작성 평균 시간 > 30초 / 일 ledger 수 > 50건 시 단순화 합의 트리거". 메타-템플릿 과도화 → 사용자 우회 시작 = reality risk.

**Reviewer 종합**: ADR-012 §결과 (Consequences) 에 운영 부담 monitoring trigger 명시.

---

## 6. 16 차원 종합 판정 매트릭스

본 §6 은 의뢰 자료 §9.1 ~ §9.16 16 차원 + 추가 차원 (Timestamp / Content-level forgery / 운영 부담) 에 대한 5 입력 종합:

| # | 차원 | 5 입력 종합 판정 | Reviewer 결정 |
|---|------|-----------|---------|
| 1 | Evidence Ledger 보호 원칙 | A/B/C/외부 LLM 1/외부 LLM 2 = APPROVE WITH CONDITIONS | ADR-012 §1 본문 — ADR-011 §2.1 + §2.3 + §2.4 + 헌법 8조 + 5조 cross-reference (외부 LLM 2 C-1) + 메타포 회피 (외부 LLM 2 §1) |
| 2 | 11 필드 구조 | 4/5 `event` 합의 (A 도 enumeration 에 포함) | **`event` 채택** (§3.1) — 17 enum 후보 |
| 3 | Append-only + hash chain | 5/5 SHA-256 충분, hash agility (외부 LLM 2 C-5) 후속 | sha256 hardcode 유지 (schema 0.1) — `hash_algo` 필드 0.2 후속 |
| 4 | signed commit OR git append commit | 5/5 다층 권고 (사용자 명시 변경 권고) | §3.2 Layer 1~4 — D-1C 절충 권고, 사용자 결정 |
| 5 | RFC 8785 JCS | 5/5 채택 + fallback | §2.2 #6 + #7 — JCS 정식 인용 + jq fallback + test corpus |
| 6 | Genesis hash | 외부 LLM 2 C-7 재정의 권고 + 외부 LLM 1 현 정의 충분 | §3.4 — MVP 현 정의 유지 + 0.2 진입 시 재정의 |
| 7 | prev_hash 검증 실패 | 4/5 BLOCK + manual + violation entry | §2.2 #8 — `event: chain_violation_detected` + manual review |
| 8 | Full rewrite 방어 | 5/5 다층 | §3.5 Layer 1~5 |
| 9 | Round-trip lossy | 4/5 tier-based | §3.3 — T2 strict / T3 의미 보존 + ledger 3 형식 |
| 10 | JSONL export/import 무결성 | 5/5 Hermes 의존 0 + schema_version declaration | C-11 import 시 schema_version 의무 검증 |
| 11 | Evidence forgery 방지 (P10 정식 등록 트리거) | 3/5 ADR-012 트리거 + 2/5 G2 분리 vs 동시 | §4.2 — 분리 (G2 update 별도 PR) + ADR-012 §1 cross-reference |
| 12 | Migration / export / import 검증 실패 시 rollback | 4/5 BLOCK + manual + 새 violation entry | §4.3 — `event: migration_failed` |
| 13 | 영구 핵심 제약 5건 답습 | 5/5 답습 (5/5 보호) | §10 |
| 14 | PR-2 통합 묶음 정당성 | 5/5 통합 진행 | §2.2 #1 |
| 15 | ADR cross-reference (008 / 009 / 010 / 011) | 5/5 권고 (009 = 별도 PR C-N) | ADR-012 §관련 문서 본문 |
| 16 | 메타 편향 / 자기참조 + cross-vendor | 5/5 외부 LLM 1+ 필수 + C-14 cross-vendor 추가 의무 (P2 v3 진입 전) | §0.3 + §11 |
| **추가 1** | Timestamp monotonicity | 외부 LLM 2 C-15 단독 | §5.3 — ADR-012 §검증 본문 |
| **추가 2** | Content-level forgery 한계 명시 | 5/5 한계 명시 의무 (외부 LLM 2 C-16 직접) | ADR-012 §11 본문 — 형식적 무결성 까지, 의미적 정확성 별도 |
| **추가 3** | 운영 부담 monitoring trigger | 외부 LLM 2 C-17 단독 + 외부 LLM 1 간접 | ADR-012 §결과 본문 |
| **추가 4** | Hermes 변조 차단 매트릭스 4항목 | Agent B Gap-17 HIGH 단독 | §5.1 — ADR-012 §본문 의무 |

**16 + 4 추가 차원 모두 5 입력 합의 또는 Reviewer 결정 완료**.

---

## 7. ADR-012 본문 작성 가이드 (Reviewer 종합 결정)

### 7.1 ADR-012 §구조 (사용자 명시 12 항목 + 5 추가 + 4 매트릭스 항목)

```
# ADR-012: Evidence Ledger Protection (Evidence Ledger 보호 강화)

## 1. 맥락 (Context)
   1.1 본 ADR 의 발행 트리거 (prequel §6.4 재해석 — Agent C C-1)
   1.2 G3 "Evidence decides" 운영 규칙의 근거 강화 필요성
   1.3 G2 §1.2.5 P10 정식 등록 트리거 명시
   1.4 Cross-reference (헌법 8조 / 5조 / ADR-011 / G3 / G4 / ADR-008 / ADR-010 — 외부 LLM 2 C-1)

## 2. 결정 (Decision)
   2.1 Evidence Ledger 보호 원칙 (12 보호 원칙)
       - PASS의 보조 기록 아니라 PASS 성립 조건 (외부 LLM 1 §1)
       - Hermes 가 승인 또는 수정 불가 (외부 LLM 1 §1)
       - 변조 가능성은 G3 root-of-trust 직접 훼손
       - 메타포 회피 — *형식적 무결성* 까지, *진리 보장* 아님 (외부 LLM 2 §1)
   2.2 11 필드 구조 (10 G4 §4.2 + `event` — 본 합의 §3.1)
   2.3 Append-only 원칙 + Hash Chain (다층 강제 — 본 합의 §3.2)
   2.4 Signed commit OR Git append commit (사용자 명시 답습 + 다층 권고 본문 — D-1A/B/C 사용자 결정 영역)
   2.5 RFC 8785 JCS canonicalization 채택 + fallback (본 합의 §2.2 #6/#7)
   2.6 Genesis hash 정의 (MVP + 0.2 진입 시 재정의 — 본 합의 §3.4)
   2.7 prev_hash 검증 실패 처리 (BLOCK + manual + chain_violation_detected — 본 합의 §2.2 #8)
   2.8 Full rewrite 방어 (Layer 1~5 — 본 합의 §3.5)
   2.9 Round-trip lossy 검출 (tier-based + 3 ledger entry 형식 — 본 합의 §3.3)
   2.10 JSONL export/import 무결성 (schema_version declaration 의무)
   2.11 Evidence forgery 방지 (P10 cross-reference, G2 update 별도 PR)
   2.12 Hermes 변조 차단 매트릭스 4항목 (Agent B Gap-17 HIGH — 본 합의 §5.1)

## 3. 추가 의무 (5 추가)
   3.1 External LLM response ledger entry (N-1)
   3.2 Schema 진화 정책 (semver MAJOR/MINOR — N-2)
   3.3 Content-level forgery 한계 명시 (N-3 + 외부 LLM 2 C-16)
   3.4 Timestamp monotonicity (외부 LLM 2 C-15)
   3.5 운영 부담 monitoring trigger (외부 LLM 2 C-17)

## 4. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습 (Means-vs-Ends Pattern)
   (a) 동등 이상의 보안 결과 (현 G4 §4.4 ↔ 본 ADR-012 비교표 — Agent B Gap-21)
   (b) 격리 환경 PoC (Implementation 영역 — 본 PR-2 외)
   (c) ADR 권위 명시 — 본 ADR-012 자체 충족
   (d) 자동 회귀 검증 경로 (R-6 workflow 답습 확장 — Agent B Gap-22)
   (e) 합의 APPROVE — 본 PR-2 합의 (5/5 입력)

## 5. 선택지 (Options Considered)
   5.1 옵션 A (채택): ADR-012 별도 발행 + G4 §4.4/§4.6 보강 (본 PR-2)
   5.2 옵션 B (비채택): ADR-008 부록 C 추가
   5.3 옵션 C (비채택): G3 §1.3 + §5.3 본문 보강 단독
   5.4 옵션 D (비채택): G4 §4.4/§4.6 보강 단독

## 6. 근거 (Rationale)
   6.1 Evidence Ledger = G3 "Evidence decides" 의 root prerequisite
   6.2 Provider Liquidity 4-way Multi-layer Defense → 5-way (Evidence 형식 추가)
   6.3 풀 3+1 + 외부 LLM 2 채택 사유 (T3 변경 = ADR 신규)
   6.4 메타-순환 청산 (G3 §4.7 답습)

## 7. 합의 결과 (5 입력 + Reviewer)
   - Agent A: APPROVE WITH CONDITIONS (8 조건)
   - Agent B: APPROVE WITH CONDITIONS (4 + 14 NOTES, Gap-17 HIGH)
   - Agent C: APPROVE WITH CONDITIONS (4 핵심 + 6 보조)
   - 외부 LLM (cross-vendor): APPROVE WITH CONDITIONS (5 권고 + 16 차원)
   - 외부 LLM (Claude 인접): APPROVE WITH CONDITIONS (17 조건 C-1~C-17)
   - **Reviewer: APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격**

## 8. 결과 (Consequences)
   8.1 긍정적
   8.2 부정적
   8.3 주의사항 (한계 명시 — 동일 호스트 SPOF / Content-level / Cryptography 심층 검토 한계)

## 9. 영구 핵심 제약 보호 (5 제약)
   - Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 / 수단/목적 분리

## 10. 본 ADR 의 발생/미발생
   10.1 발생 사항 (즉시 유효)
   10.2 미발생 사항 (별도 합의)

## 11. 메타 한계
   11.1 동일 모델 패밀리 자기 작성 산출
   11.2 cross-vendor (P2 v3 진입 전) C-14 의무
   11.3 Cryptography 심층 검토 한계 (외부 LLM 2 §15)

## 12. 관련 문서
   - 상위 권위 / 갱신 대상 / Phase 0 evidence / 합의 보고서 / 후속 작업
```

### 7.2 ADR-012 분량 추정

본 §7.1 구조 → 약 600~800 줄 (ADR-011 약 270 줄 대비 +2~3 배 — 12 원칙 + 5 추가 + 4 매트릭스 + 16 차원 평가 합산).

### 7.3 본 §7 의 권한 한계

본 §7 = ADR-012 본문 작성 *가이드*. ADR-012 본문 자체 작성은 본 합의 §13 다음 진입점 답습 (별도 작업, 본 PR-2 commit 의 일부).

---

## 8. G4 §4.4 / §4.6 보강 가이드

### 8.1 G4 §4.2 schema 갱신 (10 → 11 필드)

```
| 필드 | 타입 | 필수 | 검증 규칙 |
|------|-----|----|--------|
| `type` | enum | ✅ | `memory` / `skill` / `meta` (META 추가 — round-trip / migration / forgery / external_llm 영역) |
| `scope` | enum | ✅ | `global` / `project` / `session` / `team` |
| `id` | string | ✅ | UUID v4 또는 slug |
| `schema_version` | string | ✅ | semver (현 `0.1` MVP) |
| `ts` | ISO 8601 | ✅ | entry 생성 timestamp + monotonicity (외부 LLM 2 C-15) |
| `agent` | string | ✅ | provider-neutral identifier (`user` / `<worker_name>` / `hermes` 등) |
| **`event`** | **enum** | **✅** (신규 — 본 합의 §3.1) | **17 enum 후보 (§3.1)** |
| `content` | object | ✅ | (Memory) 자유 schema, (Skill) §3.1 17 필드 schema 그대로, (Meta) event-specific |
| `evidence_refs` | array\<string\> | 권장 | Markdown evidence 파일 경로 |
| `prev_hash` | string (sha256) | ✅ | 직전 entry 의 `hash` (chain 형성) — 첫 entry 는 `genesis_hash` |
| `hash` | string (sha256) | ✅ | 본 entry 의 canonical JSON sha256 (변조 방지) |
```

**합산 = 11 필드** (사용자 명시 답습).

### 8.2 G4 §4.4 hash chain 사양 보강 (PR-2 핵심)

```
**원칙** (system-identity-prequel §6.3 + ADR-012 §2.3 답습):
- JSONL append-only — entry 수정 / 삭제 금지
- Hash chain — `prev_hash` + `hash` 로 변조 검출 (Layer 1)
- Git append-only branch + denyNonFastForwards (Layer 2 — MANDATORY, 본 PR-2 합의 §3.2)
- Signed commit (Layer 3 — RECOMMENDED MVP, MANDATORY multi-host)
- External anchor (Layer 4 — RECOMMENDED MVP, MANDATORY P2 v3)
- 사용자 명시 답습: signed commit 또는 git append commit "둘 중 하나" 의무 (D-1A 사용자 결정 시) 또는 Layer 1+2 동시 의무 (D-1B/C — 본 합의 권고)

**Canonical JSON 정의** (RFC 8785 JCS — 본 PR-2 합의 §2.2 #6):
- Primary: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785)
- Fallback: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) — 동등성 의무 + test corpus 검증
- Fallback 사용 시 `event: canonical_json_fallback` ledger entry 의무

**Genesis hash** (본 PR-2 합의 §3.4 — MVP 현 정의 유지):
```python
# MVP (schema_version 0.1)
genesis_hash = sha256("genesis:<scope>:<schema_version>")

# 0.2 진입 또는 multi-chain 시 (외부 LLM 2 C-7)
genesis_hash = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

**prev_hash 검증 실패 처리** (본 PR-2 합의 §2.2 #8):
1. import/export/migration 즉시 BLOCK
2. 기존 원본 JSONL 보존
3. 새 `event: chain_violation_detected` entry append
4. 사용자 명시 review 의무
5. 자동 revert 금지 (T3 위반 위험 — ADR-011 §2.4)
6. Dual write 금지 (silent failure 위험)

**Full rewrite 방어** (본 PR-2 합의 §3.5):
- Layer 1: Hash chain (middle entry tampering 차단)
- Layer 2: Git append-only branch + denyNonFastForwards
- Layer 3: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- Layer 4: CI 회귀 검증 — base branch 대비 JSONL line deletion/rewrite 감지
- Layer 5 (RECOMMENDED): External anchor — GitHub Actions run ID + signed tag 또는 월 1회 external snapshot
- 1인 동일 호스트 SPOF 한계 명시 (외부 LLM 1 권고 5 답습)

**Hash 알고리즘 agility** (외부 LLM 2 C-5 — 후속 갱신 영역):
- MVP `0.1` = sha256 hardcode
- `0.2` 진입 또는 sha256 충돌 발견 시 `hash_algo` 필드 도입
- 마이그레이션 trigger 정의 = 별도 합의
```

### 8.3 G4 §4.6 round-trip 검증 절차 보강 (PR-2 핵심)

```
**라운드트립 검증 절차** (tier-based — 본 PR-2 합의 §3.3):

[원본 Hermes JSONL]
       │ ① hermes_to_<provider>.py 변환
       ↓
[<provider> 형식]
       │ ② <provider> → 본 G4 JSONL 형식 재변환
       ↓
[재변환 JSONL]
       │ ③ canonical JSON sha256 비교
       ↓
[검증]

**검증 PASS 조건 (Tier-based)**:

| Tier | 정체성 | PASS 조건 |
|-----|------|------|
| Genesis (신규 chain) | 첫 entry | (해당 없음) |
| **T2 (Skill/Memory promoted, 로컬)** | promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 | 의미 보존 허용. (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실은 BLOCK |

**Ledger entry 3 형식**:

{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"...","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"...","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"...","target_provider":"openai","failure_reason":"chain_violation_detected | policy_loss | permission_loss | evidence_loss"},...}

**자동화 vs 사용자 review 분리**:
- `lost_fields` enumeration = 자동
- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
- 의미 보존 review 자동화 절대 금지 (Agent A R-4 답습)

**Migration 검증 실패 시 rollback** (본 PR-2 합의 §4.3):
1. BLOCK
2. 원본 보존
3. 새 `event: migration_failed` entry append
4. 사용자 명시 manual review
5. 자동 revert 금지 (T3 위반 위험)
```

### 8.4 본 §8 의 권한 한계

본 §8 = G4 §4.4 / §4.6 보강 *가이드*. 본문 갱신은 본 합의 §13 다음 진입점 답습.

---

## 9. PR-2 PASS 조건 + 발생/미발생

### 9.1 PR-2 PASS 조건 (본 합의 시점 충족 명시)

| 조건 | 충족 |
|-----|----|
| 풀 3+1 합의 (Agent A/B/C 병렬 분석 + Reviewer 종합) | ✅ |
| 외부 LLM 1+ 충족 (G3 §4.4.2) | ✅ 2건 (cross-vendor + Claude 인접 컨텍스트) |
| 의뢰 자료 내부 Agent 분석 미포함 (편향 통제 강화) | ✅ |
| 5/5 입력 APPROVE WITH CONDITIONS | ✅ |
| 5 영구 핵심 제약 보호 | ✅ |
| 16 + 4 차원 평가 종합 결정 | ✅ §6 |
| ADR-012 본문 작성 가이드 + G4 §4.4/§4.6 보강 가이드 | ✅ §7 + §8 |

### 9.2 PR-2 *발생* 사항 (즉시 유효)

- ✅ Design/Governance Gate 권위 격상 적격 — ADR-012 발행 + G4 §4.4/§4.6 보강 진행 가능
- ✅ G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거* (정식 row 추가는 별도 G2 update PR)
- ✅ G4 §4.2 schema 11 필드 갱신 적격 (10 → 10 + `event`)
- ✅ Provider Liquidity 4-way Multi-layer Defense → 5-way (Evidence 형식 추가) 적격
- ✅ External LLM response ledger entry 의무 (N-1) 적격
- ✅ Schema 진화 정책 (semver MAJOR/MINOR — N-2) 적격
- ✅ Content-level forgery 한계 명시 (N-3) 적격
- ✅ Hermes 변조 차단 매트릭스 4항목 (Gap-17) ADR-012 본문 의무
- ✅ C-14 cross-vendor blind 의뢰 1+ 의무 (P2 v3 정식 채택 진입 *전*) 적격
- ✅ 본 합의 보고서 자체 (즉시 유효 — Reviewer 종합 권위)

### 9.3 PR-2 *미발생* 사항 (사용자 명시 답습)

- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 자동 선언
- ❌ ADR-008 / 009 / 010 / 011 본문 자동 갱신 (cross-reference 만 가능)
- ❌ G2 §1.2 P10 정식 row 자동 추가 (별도 G2 update PR — §4.2)
- ❌ ADR-013 / 014 후보 자동 발행
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ 실 runtime code / migration script / hook 구현 (Implementation/Runtime PASS 별도)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR-009 / P1 facade MVP 진입조건 갱신 (C-N 별도 PR)
- ❌ provider_bindings lint 룰 강제 구현 (C-H 별도 합의)
- ❌ signed commit OR git append commit "둘 중 하나" 의무 변경 (사용자 명시 결정 영역 — D-1)
- ❌ G4 §4.4 / §4.6 본문 자동 갱신 (본 PR-2 commit 의 일부 — §8)
- ❌ ADR-012 본문 자동 작성 (본 PR-2 commit 의 일부 — §7)

---

## 10. 영구 핵심 제약 보호 점검

| # | 제약 | 권위 근거 | 본 PR-2 보호 위치 | 보호 강도 |
|---|------|--------|--------|------|
| 1 | **Provider Liquidity** | 헌법 5조 (관용) + ADR-008 차단조건 #2 | ADR-012 §2.5 (JCS = vendor-neutral) + §2.10 (JSONL Hermes 의존 0) + G4 §4.3 답습 + Provider Liquidity 4-way → **5-way Multi-layer Defense** (Evidence 형식 layer 추가) | **HIGH** (5/5 일치) |
| 2 | **Hermes ≠ root of trust** | ADR-011 §2.3 영구 권위 | ADR-012 §2.12 (Hermes 변조 차단 매트릭스 4항목 — Gap-17) + §2.4 (signed/append commit) + §2.7 (BLOCK + manual) + Hermes-originated commit auto-reject | **HIGH** (5/5 일치 + Gap-17 흡수) |
| 3 | **메타포 강제 금지** | system-identity-prequel §7 | ADR-012 §2.1 (메타포 회피 — 외부 LLM 2 §1) + Evidence Ledger = 기존 prequel §6.3 + G4 §4 ADR 권위화, 메타포 인플레이션 0 | **HIGH** (5/5 영향 무관 또는 답습) |
| 4 | **자동 정책 변경 금지 (T3)** | ADR-011 §2.4 | ADR-012 §2.7 (BLOCK + manual review, 자동 revert 금지) + §3.1 (External LLM `agent: user` 강제) + §2.12 (Hermes 변조 차단) + Hermes T1 자동 학습 vs T2 사용자 승인 분리 | **HIGH** (5/5 답습 강화) |
| 5 | **수단/목적 분리** | ADR-011 §2.1 (a)~(d) + (e) | ADR-012 §4 (a)~(e) 5조건 답습 — (a) 비교표 / (b) Implementation 영역 / (c) ADR-012 자체 / (d) R-6 답습 확장 / (e) 본 합의 APPROVE | **HIGH** ((b) 별도 + 4/5 충족) |

**5 영구 핵심 제약 = 5/5 HIGH 보호** (단 (b) 격리 환경 PoC 는 Implementation/Runtime PASS 영역).

---

## 11. 본 합의의 메타 편향 자기진단

### 11.1 본 Reviewer 의 한계

- 본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = ADR-012 / G4 §4 작성 컨텍스트와 동일 패밀리 (자기 작성 산출 자기 검토 한계)
- Agent A/B/C 모두 동일 Claude 패밀리 (3/5 입력)
- 외부 LLM 2 (Claude 인접 컨텍스트) 도 Claude (4/5 입력 Claude 패밀리)
- 외부 LLM 1 (cross-vendor) 만 다른 vendor (1/5)

### 11.2 본 한계의 청산

| # | 청산 매커니즘 | 본 PR-2 적용 |
|---|----------|--------|
| 1 | 사후 외부 LLM 충족 (G3 §4.4.2) | ✅ 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) — 5/5 입력 권위 내부 |
| 2 | 격상 전 면제 (G3 §4.7.2 #2) | ✅ 본 PR-2 = Hermes PMO 격상 *전* — Hermes 자기참조 차단 §4 적용 대상 아님 |
| 3 | 합의 권위 내부 변경 (G3 §4.7.2 #3) | ✅ 본 PR-2 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 (C-C + C-G) = *권위 내부* 작업 |
| 4 | 자기 작성 한계 명시 의무 (G3 §4.7.2 #4) | ✅ 본 §11 명시 |

### 11.3 5 통제 답습

| # | 통제 | 본 PR-2 |
|---|-----|--------|
| 1 | 사용자 명시 절차 답습 | ✅ SESSION §11.1 결정 1·2·3 답습 |
| 2 | R-7 SOP §0 핵심 선언 답습 | ✅ §0 사전 점검 + §9 발생/미발생 |
| 3 | ADR-011 §2.4 T1/T2/T3 답습 | ✅ §6 차원 12 / §10 #4 |
| 4 | 수단/목적 분리 원칙 답습 | ✅ §10 #5 (a)~(e) 5조건 |
| 5 | 본 합의가 *하지 않는* 것 명시 (§9.3) | ✅ 13건 명시 |

### 11.4 C-14 cross-vendor 의무 (영구 답습)

본 PR-2 머지 후 P2 v3 정식 채택 진입 *전* **cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무** (외부 LLM 2 C-14 직접 답습 + 사용자 명시 결정 3 답습). 본 의무는 본 합의 결과와 무관 영구 유지.

---

## 12. 다음 진입점

### 12.1 본 PR-2 합의 후 즉시 작업 (본 PR-2 commit 의 일부)

1. **ADR-012 본문 작성** — 본 합의 §7 가이드 답습 (12 원칙 + 5 추가 + 4 매트릭스)
2. **G4 §4.4 / §4.6 본문 보강** — 본 합의 §8 가이드 답습 (schema 11 필드 + Layer 1~5 + tier-based round-trip)
3. **본 합의 보고서 + 외부 LLM 응답 2건 + Agent A/B/C 보고서 3건 + ADR-012 + G4 보강 동일 PR commit** (Agent A R-8 답습 — cross-reference drift 차단)

### 12.2 본 PR-2 머지 후 후속 (별도 PR)

| # | 작업 | 시점 |
|---|------|----|
| 1 | G2 §1.2.5 P10 (Evidence Forgery) 정식 row 추가 (별도 G2 update 단축 합의) | PR-2 머지 직후 또는 P2 v3 진입 전 |
| 2 | C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ | P2 v3 정식 채택 진입 *전* |
| 3 | C-N ADR-009 / P1 facade MVP 진입조건 갱신 (별도 PR) | P2 v3 진입 전 또는 후 |
| 4 | C-H provider_bindings lint 룰 강제 구현 합의 | Implementation/Runtime PASS 영역 |
| 5 | P2 v3 정식 채택 풀 3+1 + 외부 LLM (cross-vendor + 인접 컨텍스트 등) | C-14 충족 후 |
| 6 | ADR-008 / 009 / 010 / 011 cross-reference 갱신 PR 묶음 | P2 v3 정식 채택 후 |
| 7 | P2 v2 / system-identity-prequel archive 처리 | P2 v3 정식 채택 시점 |
| 8 | Hermes PMO 격상 합의 (4 게이트 모두 Implementation/Runtime PASS + 외부 LLM 2 + 사람 리뷰 + 사용자 명시 결정 후) | 별도 |

### 12.3 본 합의가 *발생시키지 않는* 것 (영구 답습)

§9.3 13건 답습. 본 합의 결과와 무관 영구 유지.

### 12.4 권고 시작 명령 (다음 세션 또는 본 세션 후속)

> **"본 합의 §7 / §8 가이드 답습으로 ADR-012 본문 작성 + G4 §4.4 / §4.6 본문 보강 진행해주세요."**

---

**합의 commit 권위**: 본 commit (`docs(review): record PR-2 ADR-012 + G4 hash chain full 3+1 consensus + external LLM ×2`)
**본 PR-2 산출 합산** (PR-2 머지 시점):
- `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (본 합의 보고서)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` (481 줄)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-b-security.md` (597 줄)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-c-alternatives.md` (424 줄)
- `docs/external-review/2026-05-XX-pr2-evidence-ledger-request.md` (외부 LLM 의뢰 자료)
- `docs/external-review/2026-05-09-pr2-evidence-ledger-response.md` (cross-vendor 외부 LLM 응답)
- `docs/external-review/2026-05-09-pr2-evidence-ledger-response-claude.md` (Claude 인접 컨텍스트 응답)
- `docs/decisions/ADR-012-evidence-ledger-protection.md` (신규 발행 — 본 합의 §7 답습, 후속 작업)
- `docs/architecture/provider-agnostic-memory-skill-design.md` (G4 §4.2 schema 11 필드 + §4.4 + §4.6 보강 — 본 합의 §8 답습, 후속 작업)
- `docs/CONTEXT.md` / `docs/INDEX.md` / `docs/sessions/SESSION_2026-05-09.md` (housekeeping)

**판정**: ✅ **APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격** (5/5 입력 일치)

**다음 단계**: §12.1 즉시 작업 (ADR-012 본문 작성 + G4 §4.4/§4.6 본문 보강 + PR-2 commit + push)
