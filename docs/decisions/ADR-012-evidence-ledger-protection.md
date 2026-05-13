# ADR-012: Evidence Ledger Protection (Evidence Ledger 보호 강화)

**상태**: 승인 (풀 3+1 + 외부 LLM 2건 — 2026-05-09)
**날짜**: 2026-05-09
**의사결정자**: 사용자 + Reviewer 종합 합의 — `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`
**상위 권위**: 헌법 제8조 (보안), 헌법 제5조 (Provider Liquidity, 관용), ADR-011 §2.1 (수단/목적 분리), §2.3 (Hermes ≠ root of trust), §2.4 (T1/T2/T3)
**모법 ADR**: ADR-011 (Means-vs-Ends Redaction Principle)
**갱신 대상**: G4 §4.2 schema (10 → 11 필드), G4 §4.4 hash chain 사양 보강, G4 §4.6 round-trip 검증 절차 보강 (동일 PR — `provider-agnostic-memory-skill-design.md`)
**P10 트리거**: 본 ADR-012 발행 시점 = G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거* (정식 row 추가는 별도 G2 update PR — 본 ADR 범위 외)
**합의 권위**: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (5/5 입력 APPROVE WITH CONDITIONS — Agent A/B/C + cross-vendor 외부 LLM + Claude 인접 컨텍스트)

---

## 1. 맥락 (Context)

### 1.1 본 ADR 발행 트리거 (prequel §6.4 재해석)

`docs/architecture/system-identity-prequel.md` §6.4 는 "Phase 1 종료 시점에 Evidence Ledger schema 의 ADR 권위화" 를 명시했다. **본 ADR-012 는 그 트리거를 *4 게이트 Design/Governance PASS + PR-1/PR-2 묶음 안정화 시점* 으로 재해석하여 발행** (합의 보고서 §5.2 Agent C C-1 답습).

재해석 사유:
- Phase 1 acceptance PASS = 2026-05-07 (G1b PASS, R-7 SOP §7.3 단축 합의)
- G2 / G3 / G4 Design/Governance Gate PASS (Bundled) = 2026-05-09
- PR-1 6건 본문 흡수 완료 = 2026-05-09 후속 2 (`commit 750faaf`)
- 본 PR-2 = G2/G3/G4 정식 PASS 합의 §11.2 P1 조건 흡수 (C-C + C-G) — **권위 내부 작업**

### 1.2 G3 "Evidence decides" 운영 규칙의 근거 강화 필요성

`docs/architecture/hermes-not-root-of-trust-runtime.md` §5 Evidence 결정 5 운영 규칙:

```
Agent proposes.       (제안)
Hermes orchestrates.  (조율 — 격상 후)
Tools verify.         (검증 — 계산적 우선)
Evidence decides.     (결정 — 기록 없으면 PASS 미성립)
Human overrides.      (사람이 최종 방향)
```

**PASS 성립 4 요건** (G3 §5.3):
- (i) Tools 검증
- (ii) **Evidence Ledger entry** ← 본 ADR-012 보호 강화 대상
- (iii) (T2/T3) 사용자 명시 승인
- (iv) (해당 시) 합의 보고서 commit

Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호.

### 1.3 G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 트리거 명시

PR-1 §1.4 (C-I 흡수, `commit 750faaf`) 에서 G2 §1.2.5 P9~P12 deferred candidates 4건 등록:
- P9 (Prompt Injection)
- **P10 (Evidence Forgery)** ← **본 ADR-012 발행 시점 = 정식 등록 트리거** (G2 §1.2.5.2 명시)
- P11 (Supply-chain)
- P12 (Memory Poisoning Side-channel)

본 ADR-012 발행은 P10 의 *정식 위반 경로 등록 트리거*. 단 **G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외, 합의 §4.2 답습).

### 1.4 Cross-reference (헌법 + ADR + G + 5 영구 핵심 제약)

| 연결 대상 | 연결 사유 |
|--------|--------|
| **헌법 제8조 (보안)** | Evidence Ledger entry 자체에 평문 secret 포함 가능 (P1 변종) — GP-1 SQLCipher trigger 보호 범위에 ledger DB 명시 포함 의무 (외부 LLM 2 C-1) |
| **헌법 제5조 관용 (Provider Liquidity)** | Ledger 형식 = Hermes 의존 0 (ADR-008 차단조건 #2 답습) + provider-neutral 강제 (Provider Liquidity 4-way Multi-layer Defense → **5-way** Evidence 형식 layer 추가) |
| **ADR-011 §2.1 (수단/목적 분리)** | 본 ADR 자체가 Evidence 무결성 = 목적, hash chain + signed/append commit + JCS = 수단. (a)~(d) + (e) 5조건 답습 (§4) |
| **ADR-011 §2.3 (Hermes ≠ root of trust)** | Hermes 는 ledger entry 생성 가능 (T1 자동 학습), 단 promotion / approval 은 사용자 명시 (T2). Hash chain + signed/append commit = Hermes 변조 차단 운영 매커니즘. **본 ADR-012 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 직접 답습 — 외부 LLM 2 C-15 / Agent B Gap-18) |
| **ADR-011 §2.4 (T1/T2/T3)** | prev_hash 검증 실패 자동 revert = T3 위반 위험 → BLOCK + manual review 채택 (외부 LLM 2 C-3 / Agent B C-3) |
| **ADR-008 차단조건 #2** | JSONL export 표준 — 본 ADR §2.10 흡수 |
| **ADR-010 (SQLCipher Vault)** | secret 처리 cross-reference — Evidence Ledger DB 가 secret 포함 가능 시 GP-1 보호 범위 명시 의무 |
| **G3 §1.3 + §5.3** | Evidence 결정 5 운영 규칙 + PASS 성립 4 요건 |
| **G4 §4.4 + §4.6** | Hash chain + canonical JSON + round-trip 검증 (본 ADR §2.3 + §2.5 + §2.7 + §2.8 + §2.9 와 동시 보강) |
| **system-identity-prequel §6.3** | Evidence Ledger schema 후보 권위 근거 — 본 ADR §2.2 답습 |

### 1.5 메타포 회피 명시 (외부 LLM 2 §1)

본 ADR-012 는 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지만 보호. *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 ADR 방어 범위 외 (§11 한계 명시 답습). "Ledger 를 *불변의 진리* 로 비유" 같은 메타포 회피 — `system-identity-prequel §7` 답습.

---

## 2. 결정 (Decision)

본 ADR-012 는 다음 12 보호 원칙 + 4 매트릭스 항목 + 5 추가 의무 을 권위로 선언한다.

### 2.1 Evidence Ledger 보호 원칙 (12)

**원칙 1**: Evidence Ledger 는 PASS 의 *보조 기록* 이 아니라 **PASS 성립 조건** 이다.

**원칙 2**: Evidence 가 없으면 PASS 는 *존재하지 않는다*.

**원칙 3**: Evidence Ledger 는 Hermes 가 *승인하거나 수정* 할 수 없다 (T3 영역).

**원칙 4**: Evidence Ledger 의 변조 가능성은 G3 root-of-trust 구조를 직접 훼손한다.

**원칙 5**: Evidence Ledger 는 *Hermes 의존 0* — 모든 entry 가 표준 도구 (`jq` + `sha256sum` + 표준 라이브러리) 만으로 검증 가능 (ADR-008 차단조건 #2 답습).

**원칙 6**: Evidence Ledger entry 작성 주체는 `agent` 필드로 *provider-neutral* 식별 — `user` / `<worker_name>` / `hermes` 등.

**원칙 7**: External LLM response 적재 시 entry `agent = "user"` (수동 paste 주체) 강제 (외부 LLM 2 C-9). Hermes 가 외부 LLM response 를 자기 제안으로 위조 차단 (Gap-17 #4).

**원칙 8**: Evidence Ledger 는 *append-only* — entry 수정 / 삭제 / 재작성 금지 (T3 영역, ADR-011 §2.4).

**원칙 9**: Hash chain 검증 실패 = 즉시 BLOCK. 자동 복구 / 자동 revert 금지 (T3 위반 위험 답습).

**원칙 10**: Round-trip 검증은 tier-based — T2 (로컬 promotion) strict / T3 (cross-vendor migration) 의미 보존 + 사용자 명시 review (§2.9 답습).

**원칙 11**: Evidence Ledger 보호 범위 = *형식적 무결성* — *의미적 정확성* (content-level forgery) 은 본 ADR 방어 범위 외 (§11 답습).

**원칙 12**: 1인 동일 호스트 SPOF 한계 인지 (G3 §5.5 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖. multi-host 전환 시 Layer 3 / Layer 5 의무 발동 트리거.

### 2.2 11 필드 구조 (G4 §4.2 schema 갱신, 10 → 11 필드)

```jsonl
{
  "type": "memory|skill|meta",
  "scope": "global|project|session|team",
  "id": "<uuid-v4-or-slug>",
  "schema_version": "0.2",
  "ts": "2026-05-09T10:00:00Z",
  "agent": "user|<worker_name>|hermes",
  "event": "<event-enum>",
  "content": {...},
  "evidence_refs": ["docs/evidence/<path>.md"],
  "prev_hash": "<sha256>",
  "hash": "<sha256>"
}
```

**11번째 필드 = `event`** (4/5 합의, Agent A enumeration 결과적 일치 — 합의 §3.1).

**`event` enum 후보 (25건, MVP 의무 12건 + 후속 확장 5건 + MVP-1 신규 8건 — schema_version 0.2)**:

| # | enum | 정체성 | T 분류 |
|---|------|------|------|
| 1 | `memory_write` | Memory entry 작성 | T1 (Hermes) / T2 (사용자 promotion) |
| 2 | `skill_proposed` | Skill 후보 추출 | T1 (Hermes 자동) |
| 3 | `skill_approved` | Skill `proposed` → `approved` | T2 (사용자 명시) |
| 4 | `skill_promoted` | Skill `approved` → `promoted` | T2 + Evidence |
| 5 | `skill_revoked` | Skill `promoted` → `revoked` | T3 자동 안전 (rollback_trigger) |
| 6 | `gate_pass` | Gate (G1b/G2/G3/G4 등) PASS 선언 | T2 사용자 명시 |
| 7 | `gate_fail` | Gate FAIL 선언 | T2 사용자 명시 |
| 8 | `external_llm_received` | External LLM response 적재 | **T2 + agent="user" 강제** (원칙 7) |
| 9 | `evidence_forgery_detected` | P10 위반 검출 | T3 BLOCK |
| 10 | `roundtrip_pass` | Round-trip hash 일치 | T1 자동 |
| 11 | `roundtrip_lossy` | Round-trip 의미 보존 (lossy) | T3 사용자 review |
| 12 | `roundtrip_fail` | Round-trip 정책/권한/증거 손실 | T3 BLOCK |
| 13 | `migration_failed` | Migration 검증 실패 (Agent A 권고) | T3 BLOCK + manual |
| 14 | `chain_violation_detected` | prev_hash mismatch 또는 hash 재계산 검출 (외부 LLM 2 C-3) | T3 BLOCK + manual |
| 15 | `hash_chain_broken` | Hash chain 자체 단절 (외부 LLM 1) | T3 BLOCK |
| 16 | `policy_change_attempted` | Hermes 가 정책 변경 시도 (T3 위반) | T3 BLOCK + audit |
| 17 | `canonical_json_fallback` | Canonical JSON `jq -S -c` fallback 사용 | T1 audit |
| 18 | `secret_scan_layer1_implementation` | Secret scan Layer 1 구현 ledger (MVP-1 Stage 1, GP-3 S-1) | T1 audit |
| 19 | `docker_secret_isolation_layer1_implementation` | Docker secret 격리 Layer 1 구현 ledger (MVP-1 Stage 2, GP-3 ST-3) | T1 audit |
| 20 | `provider_adapter_enforcement_layer1_static` | Provider adapter Layer 1 static 검출 ledger (MVP-1 Stage 3, GP-5 T-6) | T1 audit |
| 21 | `pc3_ar1_integration_implementation` | pre-commit + auto-revert 통합 구현 ledger (MVP-1 Stage 4) | T1 audit |
| 22 | `g3_7_workflow_hygiene_implementation` | Workflow hygiene 4 항목 구현 ledger (MVP-1 Stage 5, G3-7) | T1 audit |
| 23 | `provider_key_adapter_bypass_risk_detected` | Provider lock-in 위반 detect (MVP-1 IR-1) | T2 사용자 review |
| 24 | `direct_sdk_with_secret_leakage_detected` | Direct SDK + secret 검출 (MVP-1 IR-2) | T3 BLOCK + manual |
| 25 | `secret_handling_environment_mismatch_detected` | 환경 secret mismatch detect (MVP-1 IR-3) | T2 사용자 review |

**MVP 의무 12 enum** (1~12, schema_version 0.1 도입). **후속 확장 5 enum** (13~17, schema_version 0.2 진입). **MVP-1 신규 8 enum** (18~25, schema_version 0.2 정식 등록 — Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위, MVP-1 PASS §C-2 충족).

**Provider-neutral 강제** (Agent B C-16): 11 필드 모두 provider-specific 식별자 미허용.

### 2.3 Append-only 원칙 + Hash Chain (다층 강제)

**Layer 1 — Hash Chain (MANDATORY 모든 환경)**:
- `prev_hash` = 직전 entry 의 `hash` (chain 형성)
- `hash` = 본 entry 의 canonical JSON sha256
- 첫 entry 의 `prev_hash` = `genesis_hash` (§2.6)
- SHA-256 hardcode (schema_version 0.1) — `hash_algo` 필드 후속 격상 영역 (§3.2 답습)

**Layer 2 — Git append-only branch (MANDATORY)**:
- `git config receive.denyNonFastForwards true` (force-push 차단)
- branch protection rule
- pre-commit hook: `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject
- CI 회귀 검증: base branch 대비 JSONL line deletion / rewrite 감지

**Layer 3 — Signed commit (RECOMMENDED MVP, MANDATORY multi-host)**:
- GPG / SSH key signed commit
- 1인 동일 호스트 = SHOULD (SPOF 면책)
- Multi-host 전환 / 외부 공유 / 팀 사용 / Hermes PMO 격상 시점 = MUST 승격 (G3 §5.5.3 트리거 답습)

**Layer 4 — External anchor (RECOMMENDED MVP, MANDATORY P2 v3 정식 채택 시점)**:
- 월 1회 external snapshot (별도 외부 git remote / cloud storage push)
- GitHub Actions run ID + signed tag (Agent B C-4 권고)
- 1인 SPOF 완화 + 침해 후 발견 가능

### 2.4 Signed commit OR Git append commit (사용자 명시 답습)

**사용자 명시 결정 답습**: "signed commit 또는 git append commit (둘 중 하나) 의무".

**5/5 입력 권고**: Layer 1 + Layer 2 동시 의무 (Hash chain + Git append-only) + Layer 3 RECOMMENDED.

**옵션** (사용자 결정 영역 — D-1):

| 옵션 | 정체성 | 적용 |
|-----|------|---|
| **D-1A** (사용자 명시 답습) | "둘 중 하나 의무" 그대로 — 최소 = git append-only, signed = 권장 | 사용자 결정 |
| **D-1B** (5 입력 권고) | "Hash chain + Git append-only MANDATORY + Signed RECOMMENDED" 다층 | 사용자 결정 |
| **D-1C** (절충, Reviewer 권고) | MVP = "둘 중 하나 의무" + Implementation 시점 다층 격상 | 사용자 결정 |

**본 ADR 의 권위 결정**: D-1A / D-1B / D-1C 모두 본 ADR §2.3 Layer 1 + Layer 2 동시 의무 *호환*. 단 사용자 명시 결정 영역 — 본 ADR 갱신은 단축 합의 가능.

### 2.5 RFC 8785 JCS Canonicalization (채택 + Fallback)

**Primary**: RFC 8785 JCS (https://www.rfc-editor.org/rfc/rfc8785) — *informational track*, IETF 권위.

**Fallback**: `jq -S -c` (lex sort + compact + UTF-8 + RFC 8259 escape) 또는 자체 구현 동등성 의무 + test corpus 검증.

**구현 라이브러리 후보** (Agent C C-3 권고):
- Python: `pyjcs` / `rfc8785` / 또는 stdlib `json.dumps(sort_keys=True, separators=(",",":"))` 동등 보장
- Node: `canonicalize` npm
- Go: `cyberphone/json-canonicalization` / `gowebpki/jcs`

**Test corpus 의무** (외부 LLM 2 C-6):
- `tests/canonical/` 디렉토리에 RFC 8785 reference 출력 ≥ 20개 포함
- CI 회귀 검증: 입력 → 자체 canonical → JCS reference output 비교
- 불일치 시 BLOCK

**Fallback 사용 시 의무**:
- `event: canonical_json_fallback` ledger entry 작성 의무
- Reviewer 알림 + 사용자 review 권장

### 2.6 Genesis Hash 정의

**MVP (schema_version 0.1) — 현 G4 §4.4 정의 유지**:

```
genesis_hash = sha256("genesis:<scope>:<schema_version>")
```

**0.2 진입 또는 multi-chain 도입 시 (외부 LLM 2 C-7)**:

```python
genesis_hash = sha256("genesis:" + canonical_json({
  "scope": <scope>,
  "schema_version": <version>,
  "created_at": <ISO 8601>,
  "agent": "user"
}))
```

**전이 절차**: 0.1 chain 의 첫 entry 는 MVP 정의로 유지. 0.2 진입 시 새 chain (별도 `chain_id` 또는 schema_version) 생성, 기존 0.1 chain 은 read-only.

### 2.7 prev_hash 검증 실패 처리 (BLOCK + Manual Review)

**처리 절차** (4/5 합의 답습 — 합의 §2.2 #8):

1. **즉시 BLOCK** — import / export / migration 중단
2. **기존 원본 JSONL 보존** — 자동 revert 금지 (T3 위반 위험)
3. **새 violation entry append** — `event: chain_violation_detected` ledger entry 작성:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"chain_violation_detected","content":{"violation_type":"prev_hash_mismatch|hash_recalculation|history_rewrite","detected_at":"<ts>","affected_entry":"<id>","prev_hash_expected":"<sha256>","prev_hash_actual":"<sha256>"},...}
   ```
4. **사용자 명시 review 의무** — 자동 PASS 금지
5. **자동 revert 금지** (T3 위반 — ADR-011 §2.4)
6. **Dual write 금지** (silent failure 위험)

**검출 layer**:
- Layer 1: pre-commit hook (입력 entry 의 `prev_hash` 검증)
- Layer 2: pre-push hook (chain 전체 재검증)
- Layer 3: CI nightly 회귀 검증 (R-6 답습 확장)
- Layer 4: import script (`scripts/hermes-migration/import.py` — 향후 Implementation 시점)

### 2.8 Full Rewrite 방어 (다층)

**5 Layer 강제** (합의 §3.5 답습):

- **Layer 1**: Hash chain (middle entry tampering 차단)
- **Layer 2**: Git append-only branch + denyNonFastForwards (history 재작성 차단)
- **Layer 3**: pre-commit hook — `git rebase` / `git filter-branch` / `git reset --hard` 감지 시 reject (T3 자동 *방어* 권한, T3 자동 *변경* 금지의 비대칭 활용 — 외부 LLM 2 §3.3)
- **Layer 4**: CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지
- **Layer 5 (RECOMMENDED MVP, MANDATORY multi-host)**: External anchor — GitHub Actions run ID + signed tag (Agent B C-4) 또는 월 1회 external snapshot (외부 LLM 2 C-4)

**1인 동일 호스트 SPOF 한계 명시** (외부 LLM 1 권고 5 직접 인용):

> 동일 호스트 전체 침해 상황은 본 ADR-012 의 완전 방어 범위 밖이다. 본 ADR 은 Hermes container compromise, middle-entry tampering, accidental rewrite, migration 손실, evidence forgery 시도에 대한 탐지와 차단을 목표로 한다.

### 2.9 Round-trip Lossy 검출 (Tier-based)

**검증 PASS 조건** (4/5 합의 답습 — 합의 §3.3):

| Tier | 정체성 | PASS 조건 |
|-----|------|------|
| **Genesis (신규 chain)** | 첫 entry 작성 | (round-trip 무관) |
| **T2 (Skill/Memory promoted, 로컬)** | 로컬 promotion 절차 | **hash 일치 STRICT** — 손실 0건. 위반 시 BLOCK + `event: roundtrip_fail` |
| **T3 (Cross-vendor migration)** | 외부 형식 변환 + 재import | 의미 보존 허용 — (i) 손실 영역 자동 enumeration / (ii) `event: roundtrip_lossy` 의무 / (iii) 사용자 명시 review + ADR-011 §2.4 사용자 승인 / (iv) 정책/권한/증거 손실 BLOCK |

**Ledger entry 3 형식**:

```jsonl
{"type":"meta","scope":"<scope>","event":"roundtrip_pass","content":{"source_chain":"<id>","target_provider":"openai","hash_match":true},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_lossy","content":{"source_chain":"<id>","target_provider":"openai","lost_fields":["evidence_refs.confidence_score"],"semantic_diff":"<user-review-summary>"},...}
{"type":"meta","scope":"<scope>","event":"roundtrip_fail","content":{"source_chain":"<id>","target_provider":"openai","failure_reason":"chain_violation_detected|policy_loss|permission_loss|evidence_loss"},...}
```

**자동화 vs 사용자 review 분리**:
- `lost_fields` enumeration = 자동 (canonical JSON diff)
- `semantic_diff` 판단 = 사용자 명시 review (ADR-011 §2.4 T2/T3 사용자 승인)
- **의미 보존 review 자동화 절대 금지** (Agent A R-4)

### 2.10 JSONL Export / Import 무결성

**Export** (Hermes 의존 0 — ADR-008 차단조건 #2 답습):
- `scripts/hermes-migration/` 변환 스크립트 = `import hermes_agent` 0건 (depcruise 검증, G2 GP-5 답습)
- 표준 도구 (`jq` + `sha256sum`) 만으로 검증 가능
- 외부 오케스트레이터 (claude / openai / gemini / local) 최소 2+ 재해석 가능

**Import 의무 검증** (외부 LLM 2 C-11):
1. `schema_version` 필드 존재 확인 (없으면 BLOCK)
2. 호환성 매트릭스 조회 — 현 MVP 0.1 only, 외부 형식 매핑은 별도 (Implementation 영역)
3. 미일치 시 BLOCK + 사용자 명시 manual approval 요구
4. Hash chain 검증 (§2.7 답습)

**Migration 검증 실패 = `event: migration_failed`** (Agent A 권고 + 합의 §4.3):
1. BLOCK
2. 원본 보존
3. 새 `event: migration_failed` entry append:
   ```jsonl
   {"type":"meta","scope":"<scope>","event":"migration_failed","content":{"source_provider":"hermes","target_provider":"openai","failure_step":"export|conversion|import|reverify","error_summary":"..."},...}
   ```
4. 사용자 명시 manual review 의무
5. 자동 revert 금지

### 2.11 Evidence Forgery 방지 (P10 정식 등록 트리거)

**P10 정식 등록 트리거** = 본 ADR-012 발행 시점 (G2 §1.2.5.2 답습).

**G2 §1.2 본문 P10 row 추가는 별도 G2 update PR** (본 ADR 범위 외 — 합의 §4.2):
- 사용자 명시 결정 답습 — PR-2 = ADR-012 + G4 §4.4/§4.6 한정
- G2 본문 변경 = T3 변경 + 별도 합의 (단축 가능)
- 본 ADR §1.3 cross-reference 명시는 의무

**Evidence Forgery 공격 모델 5종** (외부 LLM 2 §6 답습):

| # | 공격 | 본 ADR 방어 유효성 | 보강 |
|---|------|--------------|----|
| (a) | 1인 호스트 침해 | **약** — host 전체 침해 시 모든 layer 우회 | Layer 5 external snapshot (월 1회) |
| (b) | Hermes container compromise | **강** — Hermes 는 ledger write 권한 0 (G3 §2 T3) | (그대로) |
| (c) | Git history rewrite | **중** — Layer 2~4 차단, 그러나 host 권한 상승 시 force push 가능 | (a) 동일 + Layer 5 |
| (d) | JSONL middle tampering | **강** — Layer 1 (hash chain) 정확히 이 케이스 차단 | (그대로) |
| (e) | External LLM response 위조 | **약** — vendor API key / signed response 부재 시 검증 부족 | 원칙 7 (`agent="user"` 강제) + Layer 3 권장 |

### 2.12 Hermes 변조 차단 매트릭스 4항목 (Agent B Gap-17 HIGH)

본 §2.12 = Agent B Gap-17 HIGH 흡수 — Hermes ≠ root of trust 운영 매커니즘:

| # | 변조 영역 | 차단 매커니즘 | G3 cross-reference |
|---|--------|---------|----|
| 1 | **Hermes-originated ledger entry** (Hermes 자기 entry 작성 시도 — T1 자동 학습 vs T2 사용자 승인 분기) | Hermes container `~/.claude/global/` write 권한 0 + Hermes-originated commit auto-reject | G3 §2.5 #11 + G3 §2.2 #20 |
| 2 | **파일 변조 (filesystem 직접 변경)** | `evidence/<scope>.jsonl` filesystem read-only + audit log + 컨테이너 정지 | G3 §4.5 |
| 3 | **Git commit (Hermes 가 ledger commit 시도)** | Hermes-originated commit auto-reject (commit author = Hermes 검출 시 차단) | G3 §2.2 #20 |
| 4 | **외부 LLM 응답 위조 (Hermes 가 외부 LLM response 를 자기 제안으로 위조)** | External LLM response ledger entry `agent = "user"` 강제 (수동 paste 시) + signed commit 권장 (multi-host 시 의무) | G3 §2.5 #9 + 본 §2.1 원칙 7 |

**4 항목 모두 본 ADR 권위로 차단**. ADR-011 §2.3 (Hermes ≠ root of trust) 운영 매커니즘 흡수.

---

## 3. 추가 의무 (5)

### 3.1 External LLM Response Ledger Entry (N-1)

External LLM response 적재 시 의무 entry 형식:

```jsonl
{
  "type":"meta",
  "scope":"<scope>",
  "id":"<uuid>",
  "schema_version":"0.1",
  "ts":"<ISO 8601>",
  "agent":"user",
  "event":"external_llm_received",
  "content":{
    "source_vendor":"gpt-5.x|gemini|claude-adjacent|other",
    "request_file":"docs/external-review/<request-file>.md",
    "response_file":"docs/external-review/<response-file>.md",
    "canonical_hash":"<sha256(canonical(response_body))>",
    "verdict":"APPROVE|APPROVE_WITH_CONDITIONS|PARTIAL|BLOCK"
  },
  "evidence_refs":["docs/external-review/<response-file>.md"],
  "prev_hash":"<sha256>",
  "hash":"<sha256>"
}
```

**의무**:
- `agent = "user"` 강제 (수동 paste 주체, 본 §2.12 #4 답습)
- `canonical_hash` = response 본문의 canonical JSON sha256
- Multi-host 전환 시 signed commit MUST (Layer 3)

### 3.2 Schema 진화 정책 (Semver MAJOR/MINOR — N-2)

본 §3.2 는 G4 §11.4.1 (PR-1 흡수) 답습 + ADR 권위 강화:

| 변경 유형 | 절차 | semver |
|---------|---|---|
| 필드 *추가* | 단축 합의 + import backward compatibility 보장 | MINOR (0.1 → 0.2) |
| 필드 *제거* | **풀 3+1 합의 + ADR Amendment** + migration script 의무 | MAJOR (0.x → 1.0) |
| 필드 *이름 변경* | **풀 3+1 합의 + ADR Amendment** + alias 1 release 유지 | MAJOR |
| 필드 *타입 변경* | **풀 3+1 합의 + ADR Amendment** + migration script 의무 | MAJOR |
| `event` enum 추가 (12 → 17) | 단축 합의 + 호환성 보장 | MINOR |
| `event` enum 추가 (17 → 25, MVP-1 신규 8건) | 단축 합의 + 호환성 보장 + schema_version 0.1 → 0.2 격상 (Backlog #5 합의 `docs/review/3plus1-consensus-2026-05-13-adr-012-event-enum-registration.md` 권위) | MINOR |
| `event` enum 제거 | **풀 3+1 합의** | MAJOR |
| Hash 알고리즘 변경 (sha256 → blake3 등) | **풀 3+1 합의 + ADR Amendment** + `hash_algo` 필드 도입 + 마이그레이션 trigger 정의 | MAJOR (외부 LLM 2 C-5 답습) |

### 3.3 Content-level Forgery 한계 명시 (N-3 + 외부 LLM 2 C-16)

본 ADR 의 *방어 범위 밖* 명시 (§11 본문 답습):

> 본 ADR-012 는 ledger entry 의 *형식적 무결성* (hash chain / canonical / append-only / signed) 까지만 보호. content 자체의 *의미적 정확성* (예: 사용자가 위조된 사실을 본인이 작성한 것처럼 ledger 에 기록) 은 본 ADR 방어 범위 외. 헌법 1조 (정직성) + 합의 인프라 (3+1 + 외부 LLM) + Reviewer 종합 + Human override 가 content-level 보장 layer.

ADR-011 §7.3 답습 패턴 ("본 ADR-011 은 Hermes 안전성을 선언하지 않는다 — Hermes 는 검증 대상이며, 본 ADR-011 은 검증 외부화의 권위 근거이다").

### 3.4 Timestamp Monotonicity (외부 LLM 2 C-15)

각 entry 의무:
- `ts` 는 ISO 8601
- 본 entry `ts` ≥ `prev_hash` 의 entry `ts` (timestamp monotonicity)
- 위반 시 `event: chain_violation_detected` (§2.7 답습)
- NTP 동기화 가정 — 1인 호스트 silent clock drift 위험 인지 (G3 §5.5 SPOF 답습)

### 3.5 운영 부담 Monitoring Trigger (외부 LLM 2 C-17)

운영 부담이 사용자 우회 (reality risk) 를 유발하지 않도록 monitoring trigger 명시:

| 지표 | 트리거 | 처리 |
|----|----|----|
| Ledger entry 작성 평균 시간 > 30초 | 단순화 합의 트리거 | 별도 합의 — 17 enum 축소 / 자동화 보강 / hook 비용 감소 |
| 일 ledger 수 > 50건 | 단순화 합의 트리거 | 별도 합의 — `meta` type 빈도 분석 + 통합 가능성 검토 |
| Fallback 사용 빈도 > 10% | JCS Primary 검토 합의 | 별도 합의 — JCS 라이브러리 안정화 또는 fallback 정식화 |

본 트리거 자체는 *지표 모니터링* 까지, 단순화 결정은 별도 합의 (T3 변경 = ADR-012 본문 갱신).

---

## 4. ADR-011 §2.1 (a)~(d) + (e) 5조건 답습 (Means-vs-Ends Pattern)

본 ADR-012 는 ADR-011 §2.1 5조건 패턴 답습 (수단/목적 분리):

### (a) 동등 이상의 보안 결과 (Agent B Gap-21)

**현 G4 §4.4 (보강 전) vs 본 ADR-012 강화 chain 비교표**:

| 보안 차원 | 현 G4 §4.4 | 본 ADR-012 |
|--------|---------|----------|
| Middle entry tampering 차단 | ✅ Hash chain | ✅ Hash chain (Layer 1) |
| History 재작성 차단 | ⚠️ git append commit *권고* | ✅ Layer 2 MANDATORY (git append-only + denyNonFastForwards) |
| Force-push 차단 | ❌ 미명시 | ✅ Layer 2 (denyNonFastForwards) |
| pre-commit hook 거절 | ❌ 미명시 | ✅ Layer 3 (rebase/filter-branch/reset reject) |
| CI 회귀 검증 | ❌ 미명시 | ✅ Layer 4 (line deletion/rewrite 감지) |
| External anchor | ❌ 미명시 | ✅ Layer 5 RECOMMENDED |
| prev_hash 실패 처리 | ❌ 미명시 | ✅ §2.7 BLOCK + manual + violation entry |
| Round-trip lossy 검출 | ⚠️ "hash 일치 OR 의미 보존" 단순 OR | ✅ §2.9 Tier-based + 3 ledger entry 형식 |
| Canonical JSON 표준 | ⚠️ 자체 정의 (lex sort + RFC 8259) | ✅ §2.5 RFC 8785 JCS Primary + fallback |
| Hermes 변조 차단 매트릭스 | ❌ 미명시 | ✅ §2.12 4 항목 |
| External LLM response 위조 차단 | ❌ 미명시 | ✅ 원칙 7 + §3.1 |
| Provider Liquidity 4-way → 5-way | ⚠️ 4-way (GP-5 + G3 §6.4 + G4 §3.5 + G4 §4.3) | ✅ 5-way (Evidence 형식 layer 추가) |

**결론**: 본 ADR-012 강화 chain 은 현 G4 §4.4 대비 *동등 이상의 보안 결과* — 12 보안 차원 중 11/12 ↑, 1/12 동등 (Hash chain Layer 1).

### (b) 격리 환경 PoC 실증

**Implementation/Runtime PASS 영역 — 본 ADR 범위 외**. PoC 실증은 별도 합의 (R-2 답습 — Docker network_mode: none + read_only + cap_drop ALL).

### (c) ADR 권위 명시

본 ADR-012 자체로 충족. ADR-011 §2.3 + §2.4 cross-reference 명시 (§1.4).

### (d) 자동 회귀 검증 경로 (Agent B Gap-22)

**R-6 workflow (`.github/workflows/r2-canary.yml`) 답습 확장**:
- 본 ADR-012 발행 후 별도 PR 로 R-6 workflow 에 ledger 검증 step 추가
- canonical JSON 위반 검출
- prev_hash 검증 실패 검출
- timestamp monotonicity 검증
- Implementation/Runtime PASS 영역

### (e) 합의 APPROVE

본 PR-2 풀 3+1 + 외부 LLM 2건 합의 (5/5 입력 APPROVE WITH CONDITIONS) — `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`.

---

## 5. 선택지 (Options Considered)

### 5.1 옵션 A (채택): ADR-012 별도 발행 + G4 §4.4/§4.6 보강 (본 PR-2)

- **장점**: 권위 분리 명료, P10 정식 등록 트리거 명확, Hermes ≠ root of trust 운영 매커니즘 ADR 권위화
- **단점**: ADR 갯수 증가, 1인 개발자 부담 (외부 LLM 1 권고 1 답습 — *가장 안전한 판정*)
- **5/5 입력 합의**: 채택

### 5.2 옵션 B (비채택): ADR-008 부록 C 추가

- 장점: 단일 ADR, 차단조건 #2 자연 확장
- 단점: ADR-008 비대화, Hermes 도입 결정과 evidence 무결성 혼재 (G3 §6.5 답습 어려움)

### 5.3 옵션 C (비채택): G3 §1.3 + §5.3 본문 보강 단독 (ADR 신규 0건)

- 장점: 새 권위 0건, ADR-011 §2.4 답습
- 단점: Evidence 무결성의 ADR 권위 부재 (T3 변경 시 권위 약함), P10 정식 등록 트리거 부재

### 5.4 옵션 D (비채택): G4 §4.4/§4.6 본문 보강 단독 (ADR 신규 0건)

- 장점: 사양만 명시, 권위 발행 0건
- 단점: 11 필드 / signed commit / forgery 방지 등의 ADR 권위 부재

---

## 6. 근거 (Rationale)

### 6.1 Evidence Ledger = G3 "Evidence decides" 의 Root Prerequisite

G3 §1.3 + §5.3 의 PASS 성립 4 요건 중 (ii) Evidence Ledger entry 가 부재하면 PASS 자체가 성립 불가. Evidence Ledger 변조 가능성 = G3 root-of-trust 직접 훼손 → 본 ADR 권위로 보호 의무.

### 6.2 Provider Liquidity 4-way → 5-way Multi-layer Defense

기존 4-way (G2 GP-5 + G3 §6.4 + G4 §3.5 + G4 §4.3) 에 본 ADR-012 가 layer 5 추가:
- Layer 5: Evidence 형식 차원 — ledger entry 11 필드 모두 provider-neutral 강제 (원칙 6)

### 6.3 풀 3+1 + 외부 LLM 2 채택 사유 (T3 변경 = ADR 신규)

ADR 신규 발행 = T3 변경 (ADR-011 §2.4) → 풀 3+1 + 외부 LLM 1+ 의무 (G3 §4.4.2). 본 PR-2 = 외부 LLM 2건 (cross-vendor + Claude 인접 컨텍스트) 충족. C-14 cross-vendor (P2 v3 정식 채택 진입 전) 추가 의무 (외부 LLM 2 C-14 답습).

### 6.4 메타-순환 청산 (G3 §4.7 답습)

본 ADR-012 = 동일 Claude 패밀리 자기 작성 산출 — G3 §4.7 메타-순환 청산 4 매커니즘 답습:
1. 사후 외부 LLM 충족 (외부 LLM 2건)
2. 격상 전 면제 (Hermes PMO 격상 전)
3. 합의 권위 내부 변경 (G2/G3/G4 정식 PASS §11.2 P1 흡수)
4. 자기 작성 한계 명시 (§11)

---

## 7. 합의 결과 (단축 합의 — 풀 3+1 + 외부 LLM 2건)

세부: `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md`

| 입력 | 판정 | 핵심 |
|----|----|----|
| Agent A (구현/운영) | APPROVE WITH CONDITIONS (8 조건) | HIGH 위험 3건 (R-6 Tier-1 catalog, R-7 branch protection, R-11 외부 LLM binary) |
| Agent B (보안/거버넌스) | APPROVE WITH CONDITIONS (4 + 14 NOTES, **Gap-17 HIGH**) | Hermes 변조 차단 매트릭스 4항목 (본 ADR §2.12) |
| Agent C (대안/단순화) | APPROVE WITH CONDITIONS (4 핵심 + 6 보조) | 트리거 재해석 + JCS 옵션 1 + 외부 LLM 권장→필수 격상 |
| 외부 LLM (cross-vendor) | APPROVE WITH CONDITIONS (5 권고 + 16 차원) | 11 필드 = `event` + JCS primary + jq fallback |
| 외부 LLM (Claude 인접) | APPROVE WITH CONDITIONS (17 조건 C-1~C-17) | 다층 동시 의무 + 다층 강제 + cross-vendor C-14 의무 |
| **Reviewer 종합** | **APPROVE WITH CONDITIONS — Design/Governance Gate 권위 격상 적격** | 5/5 입력 일치 + Gap-17 흡수 + 영구 핵심 제약 5/5 HIGH |

---

## 8. 결과 (Consequences)

### 8.1 긍정적

- Evidence Ledger 의 *형식적 무결성* ADR 권위화 → G3 "Evidence decides" 운영 규칙의 root prerequisite 강화
- Provider Liquidity 4-way → 5-way Multi-layer Defense (Evidence 형식 layer 추가)
- Hermes ≠ root of trust 운영 매커니즘의 영구 권위화 (Gap-17 4항목 매트릭스)
- P10 (Evidence Forgery) 정식 등록 트리거 명시
- ADR-011 §2.1 (a)~(d) + (e) 5조건 패턴 답습 — 미래 다른 비협상 조항 해석에도 적용 가능
- 1인 개발자 메타-템플릿 운영 부담 7~10일 (사양 2.5일 + Implementation 5~7일) — 적정 범위

### 8.2 부정적

- ADR 갯수 증가 (11 → 12) — 1인 개발자 부담 (단 Reviewer 종합 + 외부 LLM 2 권고 답습)
- 본 ADR-012 의 (a)~(e) 5조건 검증 부담 — 의도된 안전 비용
- C-14 cross-vendor (P2 v3 정식 채택 진입 전) 추가 의뢰 비용
- Layer 5 (External anchor) MVP RECOMMENDED → multi-host MANDATORY 전환 시점 의무 발동 — 별도 합의

### 8.3 주의사항 (한계 명시)

- **본 ADR 은 *형식적 무결성* 까지** — *의미적 정확성* (content-level forgery) 은 방어 범위 외 (§3.3 답습)
- **1인 동일 호스트 SPOF** — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖 (§2.8 답습)
- **본 ADR 은 Hermes 안전성을 선언하지 않는다** — Hermes 는 검증 대상이며, 본 ADR 은 검증 외부화의 권위 근거이다 (ADR-011 §7.3 직접 답습)
- **Cryptography 영역 심층 검토는 본 합의 검토자 한계** — RFC 8785 JCS 동등 구현 검증은 crypto specialist + cross-vendor (GPT-5.x or Gemini) 추가 의견 권고 (외부 LLM 2 §15)
- **D-1 사용자 명시 결정 영역** — signed commit OR git append commit "둘 중 하나 의무" vs 다층 동시 의무 vs 절충 (§2.4 답습)

---

## 9. 영구 핵심 제약 보호 (5 제약)

| 제약 | 권위 근거 | 본 ADR-012 보호 위치 | 강도 |
|----|------|---------|----|
| Provider Liquidity | 헌법 5조 (관용) + ADR-008 차단조건 #2 | §2.5 (JCS = vendor-neutral) + §2.10 (JSONL Hermes 의존 0) + 원칙 6 (provider-neutral 강제) + 4-way → 5-way Multi-layer Defense | **HIGH** |
| Hermes ≠ root of trust | ADR-011 §2.3 영구 권위 | §2.12 (Hermes 변조 차단 매트릭스 4항목) + 원칙 3 + 원칙 7 + Hermes-originated commit auto-reject + ADR-011 §7.3 답습 | **HIGH** |
| 메타포 강제 금지 | system-identity-prequel §7 | §1.5 메타포 회피 + §3.3 (형식적 무결성 한계) + Evidence Ledger = 기존 prequel §6.3 + G4 §4 ADR 권위화, 메타포 인플레이션 0 | **HIGH** |
| 자동 정책 변경 금지 (T3) | ADR-011 §2.4 | §2.7 (BLOCK + manual review, 자동 revert 금지) + 원칙 7 (External LLM agent="user" 강제) + §2.12 (Hermes 변조 차단) + Hermes T1 자동 학습 vs T2 사용자 승인 분리 | **HIGH** |
| 수단/목적 분리 | ADR-011 §2.1 (a)~(d) + (e) | §4 (a)~(e) 5조건 답습 — (a) 비교표 / (b) Implementation 영역 / (c) ADR-012 자체 / (d) R-6 답습 확장 / (e) 본 합의 APPROVE | **HIGH** ((b) 별도) |

**5 영구 핵심 제약 = 5/5 HIGH 보호** (단 (b) 격리 환경 PoC 는 Implementation/Runtime PASS 영역).

---

## 10. 본 ADR 의 발생 / 미발생

### 10.1 발생 사항 (즉시 유효)

- ✅ Evidence Ledger 보호 원칙 12 + 4 매트릭스 + 5 추가 의무 권위화
- ✅ G4 §4.2 schema 11 필드 갱신 (10 → 10 + `event`) — 동일 PR commit
- ✅ G4 §4.4 hash chain 사양 보강 — 동일 PR commit
- ✅ G4 §4.6 round-trip 검증 절차 보강 (tier-based + 3 ledger entry 형식) — 동일 PR commit
- ✅ Provider Liquidity 4-way → **5-way** Multi-layer Defense (Evidence 형식 layer 추가)
- ✅ G2 §1.2.5 P10 (Evidence Forgery) 정식 등록 *트리거* (별도 G2 update PR 필요)
- ✅ Hermes 변조 차단 매트릭스 4항목 (Gap-17) 영구 권위
- ✅ External LLM response ledger entry 의무 (원칙 7 + §3.1)
- ✅ Schema 진화 정책 (semver MAJOR/MINOR — §3.2)
- ✅ Content-level forgery 한계 명시 (§3.3)
- ✅ Timestamp monotonicity (§3.4)
- ✅ 운영 부담 monitoring trigger (§3.5)
- ✅ C-14 cross-vendor (P2 v3 정식 채택 진입 *전*) blind 의뢰 1+ 의무

### 10.2 미발생 사항 (별도 합의)

- ❌ Hermes PMO 격상 선언
- ❌ P2 v3 정식 채택 자동 선언
- ❌ ADR-008 / 009 / 010 / 011 본문 자동 갱신 (cross-reference 만 가능)
- ❌ G2 §1.2 P10 정식 row 자동 추가 (별도 G2 update PR)
- ❌ ADR-013 / 014 후보 자동 발행
- ❌ P2 v2 / system-identity-prequel archive 자동 처리
- ❌ 실 runtime code / migration script / hook 구현 (Implementation/Runtime PASS 별도)
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ ADR-009 / P1 facade MVP 진입조건 갱신 (C-N 별도 PR)
- ❌ provider_bindings lint 룰 강제 구현 (C-H 별도 합의)
- ❌ signed commit OR git append commit "둘 중 하나 의무" 변경 (D-1 사용자 명시 결정 영역)
- ❌ R-6 workflow ledger 검증 step 추가 (별도 PR — Implementation 영역)

---

## 11. 메타 한계

### 11.1 동일 모델 패밀리 자기 작성 산출

본 ADR-012 = Claude Opus 4.7 메인 컨텍스트 + Agent A/B/C (모두 Claude 패밀리) + 외부 LLM 2 (Claude 인접 컨텍스트) + 외부 LLM 1 (cross-vendor — 1/5 입력) 합의. **5/5 입력 중 4/5 가 Claude 패밀리** — 자기 작성 산출 자기 검토 한계 인지.

청산 매커니즘 (G3 §4.7 답습 + §6.4):
1. 사후 외부 LLM 충족 (cross-vendor + Claude 인접 = 2건)
2. 격상 전 면제 (Hermes PMO 격상 전)
3. 합의 권위 내부 변경 (G2/G3/G4 정식 PASS §11.2 P1 흡수)
4. 자기 작성 한계 명시 (본 §11)

### 11.2 C-14 Cross-vendor 의무 (P2 v3 진입 전)

본 ADR-012 머지 후 P2 v3 정식 채택 진입 *전* **cross-vendor (GPT-5.x or Gemini) blind 의뢰 1+ 의무** (외부 LLM 2 C-14 직접 답습 + 사용자 명시 결정 3 답습). 본 의무는 본 ADR 결과와 무관 영구 유지.

### 11.3 Cryptography 심층 검토 한계 (외부 LLM 2 §15)

- RFC 8785 JCS 동등 구현 검증은 본 합의 검토자 한계
- crypto specialist 추가 검토 권고 (별도 합의)
- 본 ADR §2.5 의 fallback `jq -S -c` 가 JCS 와 *모든 케이스 동등* 보장 부재 — test corpus 검증 의무 (별도 PR — Implementation 영역)

### 11.4 본 ADR 가 *지금 강제하는* 것 (DRAFT 상태에서도)

본 ADR-012 자체가 *영구 권위 ADR* 이지만, 다음을 *즉시 강제*:

1. G4 §4.2 schema 11 필드 갱신 의무 (동일 PR commit)
2. G4 §4.4 hash chain 사양 보강 의무 (동일 PR commit)
3. G4 §4.6 round-trip 검증 절차 보강 의무 (동일 PR commit)
4. ADR-011 §2.1 + §2.3 + §2.4 cross-reference 답습
5. Hermes 변조 차단 매트릭스 4항목 권위 (§2.12)
6. C-14 cross-vendor 의무 (P2 v3 진입 전)

본 6 즉시 강제는 **Hermes 가 4 게이트 통과 전 ADR-008 합의 자동화 + R-6 CI 회귀 검증 + 본 PR-2 풀 3+1 합의** 책임 한정으로 작동하는 현 상태에 적용.

---

## 12. 관련 문서

### 12.1 상위 권위

- `docs/constitution/PROJECT_CONSTITUTION.md` 제8조 (보안), 제5조 관용 (Provider Liquidity)
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 / §2.3 / §2.4 / §7.3 (모법)
- `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #2 (JSONL export)
- `docs/decisions/ADR-010-sqlcipher-vault-key-management.md` (secret 처리 cross-reference)

### 12.2 갱신 대상 (동일 PR commit)

- `docs/architecture/provider-agnostic-memory-skill-design.md` §4.2 schema (10 → 11 필드) + §4.4 hash chain 사양 + §4.6 round-trip 검증 절차

### 12.3 합의 보고서

- `docs/review/3plus1-consensus-2026-05-09-pr2-evidence-ledger.md` (본 ADR 합의 — 5/5 입력)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-a-implementation.md` (481 줄)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-b-security.md` (597 줄)
- `docs/review/agents-2026-05-09-pr2-evidence-ledger/agent-c-alternatives.md` (424 줄)
- `docs/external-review/2026-05-XX-pr2-evidence-ledger-request.md` (외부 LLM 의뢰 자료, 내부 Agent 분석 미포함)
- `docs/external-review/2026-05-09-pr2-evidence-ledger-response.md` (cross-vendor 외부 LLM 응답)
- `docs/external-review/2026-05-09-pr2-evidence-ledger-response-claude.md` (Claude 인접 컨텍스트 응답)

### 12.4 후속 작업 (별도 PR)

- G2 §1.2 P10 (Evidence Forgery) 정식 row 추가 (단축 합의)
- C-14 cross-vendor (GPT-5.x or Gemini) blind 의뢰 — P2 v3 정식 채택 진입 전
- R-6 workflow ledger 검증 step 추가 (Implementation 영역)
- ADR-009 / P1 facade MVP 진입조건 갱신 (C-N 별도 PR)
- provider_bindings lint 룰 강제 구현 합의 (C-H 별도)

---

**작성일**: 2026-05-09
**판정**: ✅ **APPROVE — Design/Governance Gate 권위 격상** (5/5 입력 풀 3+1 + 외부 LLM 2건)
**다음 진입점**: G2 §1.2 P10 정식 row 추가 (별도 G2 update 단축 합의) → C-14 cross-vendor blind 의뢰 → P2 v3 정식 채택 합의
