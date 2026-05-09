# 외부 LLM 검토 응답 — PR-2 Evidence Ledger 보호 강화 (cross-vendor)

> **회수 일자**: 2026-05-09
> **의뢰 자료**: `docs/external-review/2026-05-XX-pr2-evidence-ledger-request.md`
> **의뢰자**: 사용자 (1인 개발자, 메인 컨텍스트 = Claude Opus 4.7 메타-템플릿)
> **검토자**: 외부 LLM (cross-vendor — 사용자가 직접 외부 vendor 에 제출 후 응답 회수, 본 응답은 vendor 자기 명시 부재 시 cross-vendor 후보 — GPT-5.x / Gemini / 또는 다른 비-Claude vendor)
> **판정**: **APPROVE WITH CONDITIONS**
> **본 응답은 사용자가 본 세션에 직접 paste 한 원문을 보존** (구조 변경 0건, 일부 형식 인코딩 변형 허용 — `9.10 JSONL expoal` 등 수신 시점 표기는 원문 그대로). 본 프로젝트의 Reviewer 가 Agent A / B / C + 본 응답 + Claude 인접 컨텍스트 응답 (`2026-05-09-pr2-evidence-ledger-response-claude.md`) 와 종합.

---

## 최종 판정: APPROVE WITH CONDITIONS

PR-2의 방향은 적절합니다. ADR-012를 별도 발행하고, G4 §4.4 / §4.6의 hash chain·canonical JSON·round-trip 검증 사양을 보강하는 설계는 안전성, 추적성, Provider Liquidity 측면에서 타당합니다. 특히 Evidence Ledger가 G3의 "Evidence decides" 원칙을 떠받치는 핵심 근거라면, 이를 별도 ADR 권위로 보호하는 것은 충분히 정당합니다.

다만 본 PR-2는 설계/거버넌스 보강 PR이어야 하며, 아직 runtime hook, migration script, CI enforcement, 실제 JSONL writer 구현 완료를 의미하면 안 됩니다.

## 1. 핵심 결론

| 항목 | 판정 |
|------|------|
| ADR-012 별도 발행 | 승인 |
| G4 §4.4 hash chain 보강 | 승인 |
| G4 §4.6 round-trip 검증 보강 | 승인 |
| P10 Evidence Forgery 정식 등록 | 조건부 승인 |
| RFC 8785 JCS 채택 | 권고 |
| signed commit OR git append commit | 조건부 유지 가능 |
| PR-2 통합 묶음 | 승인 |
| P2 v3 정식 채택 자동 진입 | 아직 아님 |
| Runtime / Implementation PASS | 아직 아님 |

## 2. 주요 권고안 요약

### 권고 1 — 11번째 필드는 `event`를 추천

현 G4 JSONL schema는 10필드입니다. PR-2에서 11필드 구조를 요구한다면, 추가 필드는 `event` 가 가장 적절합니다.

```json
"event": "memory_write"
```

권장 enum 예시는 다음과 같습니다.

- `memory_write`
- `skill_proposed`
- `skill_approved`
- `skill_promoted`
- `skill_revoked`
- `gate_pass`
- `gate_fail`
- `external_llm_received`
- `roundtrip_lossy`
- `migration_failed`
- `evidence_forgery_detected`
- `hash_chain_broken`

`event`가 가장 좋은 이유는 단순합니다.

| 후보 | 평가 |
|-----|------|
| `event` | 가장 추천. Ledger의 의미를 명확히 하고, lossy 검출·forgery 검출·gate pass 기록을 모두 표현 가능 |
| `signature` | commit layer에서 처리하는 편이 낫다. entry 필드에 넣으면 키 관리 부담 증가 |
| `chain_id` | 유용하지만 MVP에서는 `scope` + `type` + `event`로 상당 부분 대체 가능 |
| `parent_event_id` | 추적성은 좋지만 1인 개발자 MVP에는 다소 무겁다 |
| 추가 없음 | 사용자 명시 11필드 요구와 충돌 |

최종 권고는 다음입니다.

> G4 JSONL 11번째 필드는 `event`로 한다. `chain_id`와 `parent_event_id`는 MVP 이후 확장 필드로 둔다.

### 권고 2 — RFC 8785 JCS를 채택하되 fallback 허용

Canonical JSON은 자체 정의보다 RFC 8785 JCS를 인용하는 편이 낫습니다.

| 기준 | 평가 |
|------|------|
| 표준성 | RFC 8785는 외부 설명력이 높음 |
| Provider Liquidity | Claude/OpenAI/Gemini/local tool 어디서든 재현 가능한 기준이 됨 |
| CI 검증 | canonicalization 위반을 자동 테스트하기 쉬움 |
| 1인 개발자 부담 | 약간 증가하지만, 장기적으로 자체 정의보다 위험이 낮음 |

다만 Python/Node 구현 차이가 생길 수 있으므로 다음 문구를 권장합니다.

> Canonical JSON은 RFC 8785 JCS를 기본 표준으로 한다. 단, 구현 환경에서 JCS 라이브러리 사용이 어려운 경우 `jq -S -c` 기반 fallback을 허용하되, fallback 사용 시 `canonicalization_mode` 또는 evidence entry에 기록한다.

단, 여기서 `canonicalization_mode`를 11번째 필드로 넣기보다는 `content` 또는 evidence metadata에 넣는 편이 낫습니다. 11번째 필드는 `event`가 더 범용적입니다.

### 권고 3 — signed commit OR git append commit은 유지 가능하나, 우선순위를 정해야 함

사용자 명시가 "signed commit OR git append commit 둘 중 하나 의무"라면 그대로 유지해도 됩니다. 하지만 보안 수준이 다르므로 ADR-012에 우선순위를 명시하는 것이 좋습니다.

권장안:

| 환경 | 권고 |
|------|------|
| MVP / 1인 개발자 / 동일 호스트 | git append-only branch + branch protection + force-push 금지 |
| 외부 공유 / 다중 호스트 / 팀 사용 | signed commit 권장 |
| 고보안 프로젝트 | hash chain + signed commit + protected branch |

최종 문구는 다음이 적절합니다.

> MVP에서는 hash chain + git append-only branch를 최소 요구로 한다. signed commit은 권장 보강책이며, 팀/다중 호스트/외부 배포 시 SHOULD에서 MUST로 승격한다.

즉, **둘 다 의무**는 1인 개발자 템플릿에는 과합니다. **둘 중 하나 의무**는 허용하되, 최소 기준은 append-only branch로 두는 편이 현실적입니다.

### 권고 4 — `prev_hash` 실패는 BLOCK + manual review

`prev_hash` 검증 실패 시에는 자동 복구보다 BLOCK + manual review가 맞습니다.

권장 처리:

1. import/export/migration 즉시 BLOCK
2. 기존 원본 JSONL 보존
3. 실패 evidence entry 생성 시도
4. 실패 entry도 기존 chain을 오염시키지 않도록 별도 incident log에 기록
5. 사용자 수동 확인 전 gate pass 금지

자동 revert는 위험합니다. 자동 revert가 잘못 동작하면 오히려 evidence 삭제나 silent rewrite가 될 수 있습니다. 특히 ADR-011의 T3 자동 정책 변경 금지 원칙과 충돌할 수 있습니다.

### 권고 5 — full rewrite 방어는 git layer가 핵심

Hash chain은 중간 entry 변조를 잘 잡지만, 공격자가 전체 JSONL을 처음부터 다시 계산해 rewrite하면 hash chain만으로는 부족합니다.

따라서 full rewrite 방어는 다음 조합이 필요합니다.

- hash chain
- + append-only branch
- + force-push 금지
- + CI에서 base branch 대비 JSONL line deletion/rewrite 감지
- + 선택적으로 signed tag 또는 signed commit

1인 개발자 동일 호스트 환경에서는 완벽한 방어가 불가능합니다. 이 한계는 ADR-012에 명시해야 합니다.

권장 문구:

> 동일 호스트 전체 침해 상황은 본 ADR-012의 완전 방어 범위 밖이다. 본 ADR은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.

## 3. 16개 평가 차원별 판정

### 9.1 Evidence Ledger 보호 원칙

판정: APPROVE WITH CONDITIONS

ADR-012는 다음 원칙을 명시해야 합니다.

- Evidence Ledger는 PASS의 보조 기록이 아니라 PASS 성립 조건이다.
- Evidence가 없으면 PASS는 존재하지 않는다.
- Evidence Ledger는 Hermes가 승인하거나 수정할 수 없다.
- Evidence Ledger의 변조 가능성은 G3의 root-of-trust 구조를 직접 훼손한다.

Cross-reference는 최소 다음을 포함해야 합니다.

| 연결 대상 | 이유 |
|----------|------|
| ADR-011 §2.1 | 수단/목적 분리 원칙 |
| ADR-011 §2.3 | Hermes ≠ root of trust |
| ADR-011 §2.4 | T1/T2/T3 권한 분리 |
| G3 §5 | Evidence decides |
| G4 §4.4 | hash chain |
| G4 §4.6 | round-trip 검증 |
| ADR-008 | JSONL export 표준 |
| ADR-010 | secret이 evidence에 섞이지 않도록 처리 |

### 9.2 11 필드 구조

판정: `event` 권고

추천 11필드:

```json
{
  "type": "memory",
  "scope": "project",
  "id": "...",
  "schema_version": "0.1",
  "ts": "2026-05-09T10:00:00Z",
  "agent": "user",
  "event": "gate_pass",
  "content": {},
  "evidence_refs": [],
  "prev_hash": "...",
  "hash": "..."
}
```

`event`는 round-trip lossy, migration failure, forgery detection, external LLM receipt, gate pass/fail을 모두 표현할 수 있어 가장 범용적입니다.

### 9.3 Append-only + hash chain

판정: APPROVE WITH CONDITIONS

SHA-256은 충분합니다. BLAKE3나 SHA-3로 바꿀 필요는 없습니다.

권장 계층:

1. JSONL append-only 원칙
2. hash chain
3. pre-commit에서 기존 line 수정/삭제 차단
4. CI에서 prev_hash/hash 전체 검증
5. branch protection 또는 signed commit

### 9.4 signed commit OR git append commit

판정: APPROVE WITH CONDITIONS

둘 중 하나 의무는 허용 가능합니다. 다만 ADR-012에 최소/권장 수준을 분리해야 합니다.

- MUST: hash chain
- MUST: git append-only commit or signed commit
- SHOULD: protected branch
- SHOULD: signed commit for multi-host/team usage

### 9.5 RFC 8785 JCS

판정: 채택 권고

자체 canonicalization 정의는 장기적으로 위험합니다. JCS를 기본으로 두고 fallback을 문서화하십시오.

- Primary: RFC 8785 JCS
- Fallback: `jq -S -c` + UTF-8 + no insignificant whitespace
- Fallback 사용 시 evidence에 기록

### 9.6 Genesis hash

판정: 조건부 승인

현 정의:

```
sha256("genesis:<scope>:<schema_version>")
```

MVP에서는 충분합니다. 다만 `event`를 도입하면 향후 다중 chain이 필요할 수 있으므로 다음 확장형을 권장합니다.

```
sha256("genesis:<type>:<scope>:<schema_version>")
```

만약 `chain_id`를 후속 도입한다면:

```
sha256("genesis:<chain_id>:<schema_version>")
```

### 9.7 prev_hash 검증 실패 처리

판정: BLOCK + manual review 권고

권장 정책:

- prev_hash mismatch = BLOCK
- 자동 import/export/migration 중단
- 자동 PASS 금지
- 원본 파일 보존
- 사용자 수동 검토 전 복구 금지

자동 revert는 금지하는 편이 안전합니다.

### 9.8 Full rewrite 방어

판정: 조건부 승인

완결성은 git layer 없이는 부족합니다.

필수 조합:

- hash chain
- + protected branch 또는 append-only branch
- + force-push 금지
- + CI에서 line deletion/rewrite 감지

선택 보강:

- signed commit
- signed tag
- external snapshot

외부 snapshot은 1인 개발자 MVP에서는 과할 수 있으므로 SHOULD로 두면 됩니다.

### 9.9 Round-trip lossy 검출

판정: tiered 방식 권고

현 OR 조건은 너무 느슨할 수 있습니다. 권장안은 다음입니다.

- 기본 PASS: hash 일치
- hash 불일치 시: `roundtrip_lossy` event 생성
- `roundtrip_lossy`는 자동 PASS 불가
- 사용자 review + 손실 영역 명시 후 조건부 허용
- T3/정책/권한 관련 손실은 허용 불가

즉, "hash 일치 OR 의미 보존"이 아니라 다음이 더 안전합니다.

- hash 일치 = PASS
- hash 불일치 + 의미 보존 + 사용자 승인 = CONDITIONAL PASS
- 정책/권한/증거 손실 = BLOCK

### 9.10 JSONL export Verdict: APPROVE WITH CONDITIONS

> *(원문 인코딩 그대로 보존 — `9.10 JSONL expoal Verdict` 표기 수신, 본 절 이후 영문 요약으로 수신됨)*

PR-2 is directionally sound and appropriate as a pre-P2-v3 design/governance hardening step. ADR-012 should be issued as a separate authority document because Evidence Ledger integrity is a root prerequisite for G3's "Evidence decides" rule. G4 §4.4 and §4.6 should be strengthened in the same PR because JSONL hash chain, canonicalization, round-trip verification, and evidence forgery prevention are tightly coupled.

However, PR-2 must clarify that this is not Implementation/Runtime PASS. The 11th JSONL field should be `event`; RFC 8785 JCS should be the primary canonicalization standard with a documented fallback; `prev_hash` failures must BLOCK and require manual review; full rewrite defense must rely on git append-only/protected branch controls; round-trip lossy cases must be conditional, not normal PASS; and P10 Evidence Forgery registration must be triggered by ADR-012 but recorded through a separate G2 update/evidence commit.

따라서 BLOCK은 아닙니다. PARTIAL도 아닙니다.

PR-2는 통합으로 진행해도 되지만, 위 조건을 반영한 APPROVE WITH CONDITIONS가 가장 안전한 판정입니다.

---

**원문 보존 종료** — Reviewer 가 본 응답 + Claude 인접 컨텍스트 응답 + Agent A/B/C 와 종합.
