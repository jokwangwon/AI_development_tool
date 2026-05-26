# G4 History Rewrite — Layer 5 External Anchor PoC — Group C 후속 사양

> **PASS scope**: G4 *Layer 5 External anchor 정적 검출 시제* 한정 — **Implementation Pending** (G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **상태**: DRAFT (2026-05-10, Group C 후속 진입 — ADR-012 §2.8 *Full Rewrite 5 Layer* 中 Layer 5 (External Anchor) 영역 정적 검출 PoC)
> **답습 출처**:
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.8 (Full Rewrite 방어 5 Layer — Layer 1 hash chain + Layer 2 git append-only + Layer 3 pre-commit hook + Layer 4 CI 회귀 + Layer 5 External anchor) / §2.12 (Hermes 변조 차단 매트릭스 4 항목)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §4.4.5 (Full Rewrite 방어 5 Layer — ADR-012 §2.8 답습)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e)
> - **Group C 산출물**: `tools/jsonl_hash_chain.py` (`parse_jsonl` + `validate_chain` + `compute_entry_hash` + `compute_genesis_hash` + ENUMs `ALLOWED_TYPES`/`ALLOWED_AGENTS`/`ALLOWED_SCOPES` import 직접) + `tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl` (5 entries chain 답습)
> - **Group A~G PoC 형식**: Group D + Group E + Group G + Group A 3차 사양 형식 직접 답습
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 5 풀 3+1 승격 trigger / 10 검증 / 7 금지 / 외부 의존 0건
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), ADR-012 §2.8 1인 동일 호스트 SPOF 한계 명시 (외부 LLM 1 권고 5)
> **답습 시제**: Group A 1차/2차/3차 + Group B + Group C + Group D + Group E + Group F + Group G PoC 사양 형식 직접 답습 (`g3-g4-boundary-guard-poc.md` 답습)

---

## 0. 목적

본 PoC 는 ADR-012 §2.8 *Full Rewrite 방어 5 Layer* 中 **Layer 5 — External Anchor** 영역의 *형식적 검출 layer* 첫 시제 — Layer 1 (Group C `validate_chain` 답습 완료) 만으로는 *full rewrite / tail truncation / middle deletion / substitution* 4 시나리오를 검출 불가능함을 fixture 로 시연 + Layer 5 anchor metadata 가 검출 가능함을 evidence 로 확보.

**범위 한정 핵심 결정** (사용자 명시 답습):

- **검출 대상** = ADR-012 §2.8 *Layer 5 External anchor* 한 영역만. Layer 2 (git append-only) / Layer 3 (pre-commit hook) / Layer 4 (CI 회귀) = **별도 합의 영역**.
- **Anchor metadata 형식만 정의** + fixture 기반 검출 PoC. 실 signed commit / branch protection / external timestamping service 연동 = **별도 합의** (사용자 명시 7 금지 답습).
- **`anchor_method=ci_run_id` 한 메서드 한정** — `signed_tag` / `external_snapshot` 2 메서드 = 후속 영역.

본 PoC 는 **Layer 5 정적 검출 layer 한정** — runtime 강제 / multi-host MANDATORY 격상 / signed commit 정책 도입 = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `ADR-012 §2.8` + `G4 §4.4.5` + Group C `validate_chain` 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g4-history-rewrite-layer5-anchor-poc.md` | PoC 사양 + 답습 매핑 + 사용자 명시 10 검증 / 5 trigger / 7 금지 / 10 fixture / 5 attack scenario 매트릭스 |
| Validator | `tools/history_anchor_verifier.py` | 단일 도구 + 2 mode (chain-only / anchor-verify) + Group C `jsonl_hash_chain` import 직접 (`parse_jsonl` + `validate_chain` + `compute_entry_hash`) + 11-field anchor schema validation + 5 attack model 검출 (full_rewrite / tail_truncation / middle_deletion / substitution / anchor_tampered) + `--list-attack-models` self-check + violation reporter (Group D/E/G 답습) |
| PASS fixture × 4 | `tests/fixtures/history_anchor_verifier/pass/{original_ledger.jsonl, original_anchor.json, extended_ledger.jsonl, extended_anchor.json}` | original (5 entries) + extended (5+2 entries with previous anchor at 5) — 정상 운영 시제 (Layer 5 anchor matched + anchor_outdated_appended warning) |
| FAIL fixture × 5 | `tests/fixtures/history_anchor_verifier/fail/{full_rewrite_ledger, tail_truncation_ledger, middle_deletion_ledger, substitution_ledger}.jsonl + anchor_tampered.json` | 5 attack model cover (Layer 1 inadequacy 영역 4 + anchor 자체 변조 1) |
| chain_only_demo fixture × 1 | `tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl` | **Layer 1 inadequacy demo** — Group C `validate_chain` 단독 시 *PASS* 처리됨을 시연 (의도된 결과) |
| CI workflow | `.github/workflows/history-anchor-verifier.yml` | 13 step (3 setup + `--list-attack-models` + 8 검증 + summary.json + artifact + Evidence summary). artifact path = `group-c-followup-logs/` (Group F 후속 답습) |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g4-history-rewrite-layer5-reviewer-only.md` | PoC 검토 + 5 trigger 0/5 자기 검증 + evidence 매트릭스 통합 (Group D/E/G/A3 답습) |

**합산 = 8 파일** (Group D/E/G/A3 답습 평균).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 7 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** — 본 PoC = *Layer 5 정적 검출 시제* 한정 |
| G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** |
| Hermes PMO 격상 선언 | **사용자 명시** |
| 실 branch protection 변경 | **사용자 명시** — Layer 2 영역 (별도 합의) |
| 실 signed commit 강제 | **사용자 명시** — Layer 2~3 영역 (별도 합의) |
| 실 external timestamping service 연동 | **사용자 명시** — Layer 5 multi-host MANDATORY 격상 시점 (별도 합의) |
| ADR 본문 자동 갱신 | **사용자 명시** — cross-reference 답습 한정 |
| Layer 2 (Git append-only branch + denyNonFastForwards) 통합 | ADR-012 §2.8 분리 영역 — 별도 합의 |
| Layer 3 (pre-commit hook — git rebase/filter-branch/reset 감지) | ADR-012 §2.8 분리 영역 — 별도 합의 |
| Layer 4 (CI 회귀 검증 — base branch 대비 line deletion / rewrite 감지) | ADR-012 §2.8 분리 영역 — 별도 합의 |
| `anchor_method=signed_tag` / `external_snapshot` 2 메서드 | 본 PoC = `ci_run_id` 한 메서드 한정, 추가 = 별도 합의 |
| Anchor metadata 자체 signing (GPG / Sigstore / cosign) | Layer 5 multi-host MANDATORY 영역 — 별도 합의 |
| 실 GitHub Actions run id / commit SHA 검증 (외부 호출) | 본 PoC = literal 비교만, 실 호출 = 별도 합의 |
| Anchor 자동 갱신 / nightly cron | runtime hook 영역 — 별도 합의 |
| Multi-host external service 통합 | ADR-012 §2.8 MANDATORY 격상 영역 |

---

## 2. history rewrite 공격 모델 (5 시나리오 + Layer 1 inadequacy 시연)

### 2.1 5 attack scenario 매트릭스

| # | 공격 모델 | Group C `validate_chain` 검출 | Layer 5 anchor 검출 | 본 PoC fixture | 답습 |
|---|---|---|---|---|---|
| 0 (baseline) | 단일 entry hash 변조 / prev_hash 끊김 / hash recalculation mismatch | ✅ Group C 답습 완료 (4 violation_type) | ✅ tail hash mismatch 도 검출 | — (Group C 영역) | Group C `tests/fixtures/jsonl_ledger/fail/` |
| 1 | **Full rewrite** — 모든 entry 재작성, prev_hash 모두 재계산 → 내부 chain 일관성 유지 | **❌ 검출 불가** (chain 내부적으로 valid) | ✅ tail hash mismatch | `full_rewrite_ledger.jsonl` | ADR-012 §2.8 Layer 5 |
| 2 | **Tail truncation** — 마지막 N entry 제거, 남은 chain 자체는 valid | **❌ 검출 불가** | ✅ entry count + tail hash mismatch | `tail_truncation_ledger.jsonl` | ADR-012 §2.8 Layer 5 |
| 3 | **Middle deletion + 재계산** — 중간 entry 제거 후 이후 entry 의 prev_hash 재계산 | **❌ 검출 불가** | ✅ entry count + tail hash mismatch | `middle_deletion_ledger.jsonl` | ADR-012 §2.8 Layer 5 |
| 4 | **Substitution** — 전체 ledger 를 *다른* valid chain 으로 교체 | **❌ 검출 불가** | ✅ tail hash mismatch + (가능 시) genesis hash mismatch | `substitution_ledger.jsonl` | ADR-012 §2.8 Layer 5 |
| 5 | **Anchor 자체 변조** — anchor metadata 가 변조됨 | n/a (chain 영역 외) | ⚠️ anchor 형식 검증 (signature 부재 시 한계 — *known limitation*) | `anchor_tampered.json` | ADR-012 §2.8 1인 동일 호스트 SPOF 한계 답습 |

### 2.2 Layer 1 inadequacy demo (사용자 명시 핵심 evidence)

본 PoC 의 *evidence 가치* (사용자 명시 답습):

> "hash chain만으로 충분한 영역과 부족한 영역을 구분하는가" + "Layer 5 external anchor / signed commit / git append-only가 왜 필요한지 evidence로 보강하는가"

**Layer 1 충분 영역**: 단일 entry tampering (Group C 답습 완료) — 4 violation_type cover (PREV_HASH_MISMATCH / HASH_RECALCULATION / HISTORY_REWRITE / GENESIS_MISMATCH).

**Layer 1 부족 영역**: full rewrite + tail truncation + middle deletion + substitution = **4 attack scenario 모두 Group C `validate_chain` 단독 시 PASS 처리됨** (의도된 한계, 사양 §2.1 #1~#4 매트릭스 답습).

**Layer 5 의무성 evidence**: anchor metadata 가 위 4 시나리오 *모두 검출* — fixture #2~#5 + chain-only demo fixture 로 직접 시연.

**1인 동일 호스트 SPOF 한계** (ADR-012 §2.8 + 외부 LLM 1 권고 5 답습): anchor file 자체가 변조되면 Layer 5 도 부분만 cover (fixture #6 = anchor_tampered) — multi-host external service 의무성 명시.

---

## 3. Anchor Metadata 형식 (11 필드)

### 3.1 11 필드 정의 (Group C 11-field schema 답습 표기)

```json
{
  "anchor_id": "anchor-2026-05-10-001",
  "anchor_ts": "2026-05-10T10:00:00Z",
  "anchor_method": "ci_run_id",
  "ledger_path": "tests/fixtures/.../original_ledger.jsonl",
  "expected_entry_count": 5,
  "expected_tail_hash": "abc123...",
  "expected_genesis_hash": "def456...",
  "schema_version": "0.1",
  "external_run_id": "github-actions-run-25618490324",
  "external_run_url": "https://github.com/owner/repo/actions/runs/25618490324",
  "notes": "본 PoC 한정 — 실 signed git tag / external timestamping = 별도 합의"
}
```

| # | 필드 | 타입 | 필수 | 검증 |
|---|------|-----|----|------|
| 1 | `anchor_id` | string | ✅ | UUID v4 또는 slug `[a-z0-9-]{3,64}` |
| 2 | `anchor_ts` | string (ISO 8601) | ✅ | `YYYY-MM-DDTHH:MM:SSZ` 형식 |
| 3 | `anchor_method` | enum | ✅ | `ci_run_id` (본 PoC 한정) / `signed_tag` (별도 합의) / `external_snapshot` (별도 합의) |
| 4 | `ledger_path` | string | ✅ | 상대 경로 (anchor 가 cover 하는 ledger) |
| 5 | `expected_entry_count` | int | ✅ | 양의 정수 (anchor 시점 ledger entry 수) |
| 6 | `expected_tail_hash` | string (sha256 hex) | ✅ | 64자 hex (마지막 entry 의 `hash` 필드) |
| 7 | `expected_genesis_hash` | string (sha256 hex) | ✅ | Group C `compute_genesis_hash` 답습 (`genesis:<scope>:<schema_version>`) |
| 8 | `schema_version` | string (semver) | ✅ | Group C MVP `0.1` 한정 |
| 9 | `external_run_id` | string | ✅ | GitHub Actions run id 또는 외부 commit SHA |
| 10 | `external_run_url` | string | MVP-권장 | URL 형식 (사람 검증 보조, 본 PoC 검증 미강제) |
| 11 | `notes` | string | MVP-권장 | free-form (한계 명시 등) |

**합산 = 11 필드** (필수 9 + MVP-권장 2).

### 3.2 본 PoC 검증 영역 (anchor_method=ci_run_id 한정)

| Field | 본 PoC 검증 | 분리 영역 |
|---|---|---|
| 1 형식 | regex 검증 | — |
| 2 형식 | regex 검증 | — |
| 3 enum | `ci_run_id` 한정 | `signed_tag` / `external_snapshot` = 별도 합의 |
| 4 | path 존재 여부 | — |
| 5 | int + count 일치 검증 | — |
| 6 | sha256 hex + tail hash 일치 검증 | — |
| 7 | sha256 hex + genesis hash 일치 검증 (Group C `compute_genesis_hash` 답습) | — |
| 8 | `0.1` 한정 | 진화 정책 = 별도 합의 |
| 9 | 형식 검증만 (실 호출 0건) | 실 GitHub API 호출 = 별도 합의 |
| 10 | 형식 검증만 (옵셔널) | — |
| 11 | (검증 없음, 사람 보조) | — |

---

## 4. 도구 선택 근거 (stdlib 단독 채택)

### 4.1 채택 (Group D/E/G/A3 답습)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom validator (stdlib `re` + `json` + `dataclasses` 단독 + Group C import)** | **✅ 채택** | Group D/E/G/A3 답습 (외부 의존 0건) + Group C `validate_chain` import 직접 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) GPG / Sigstore / cosign 통합 | ❌ 제외 | Layer 5 multi-host MANDATORY 영역 — 별도 합의 |
| (C) GitHub API 호출 (실 run id 검증) | ❌ 제외 | 외부 호출 = 별도 합의 |
| (D) external timestamping service (RFC 3161) | ❌ 제외 | 별도 합의 |

**채택 = (A) 단독**.

### 4.2 본 PoC 의 stdlib 답습 영역

| stdlib 모듈 | 책무 |
|------|------|
| `re` | anchor field regex 검증 (UUID/slug/ISO 8601/sha256 hex) |
| `json` | anchor metadata JSON parse |
| `dataclasses` | `Violation` reporter (Group D/E/G/A3 답습) |
| `argparse` | 2 mode CLI + `--list-attack-models` self-check |
| `pathlib` | ledger / anchor file 경로 처리 |

**외부 의존 0건** (`requirements-dev.txt` 변경 0건).

---

## 5. Group C 도구 재사용 매트릭스

### 5.1 import 직접 (리팩토링 0건)

```python
from jsonl_hash_chain import (  # Group C 답습 직접
    ALLOWED_AGENTS,
    ALLOWED_SCOPES,
    ALLOWED_TYPES,
    SUPPORTED_SCHEMA_VERSION,
    parse_jsonl,                # JSONL parser
    compute_entry_hash,         # entry hash 재계산
    compute_genesis_hash,       # genesis hash 계산
    validate_chain,             # Layer 1 chain 검증
    validate_schema,            # 11-field schema 검증
)
```

### 5.2 답습 분포

| 영역 | Group C 답습 | 신규 작성 |
|---|---|---|
| 11-field JSONL schema 검증 | `validate_schema` import 직접 | 0 |
| Hash chain Layer 1 검증 | `validate_chain` import 직접 | 0 |
| Genesis hash 계산 | `compute_genesis_hash` import 직접 | 0 |
| Entry hash 재계산 | `compute_entry_hash` import 직접 | 0 |
| ENUMs (`ALLOWED_TYPES` 등) | import 직접 | 0 |
| 11-field anchor metadata schema | — (본 PoC 신규) | ~30줄 |
| 5 attack model 검출 logic | — (본 PoC 신규) | ~80줄 |
| 2 mode CLI dispatch (chain-only / anchor-verify) | Group D/E/G/A3 답습 | ~60줄 |
| violation reporter | Group A 1차 + Group D 답습 | ~25줄 |
| `--list-attack-models` self-check | Group D `--list-patterns` + Group G `--list-boundaries` 답습 | ~30줄 |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건**. 신규 작성 ~225줄.

### 5.3 Group C fixture 답습

| Group C fixture | 본 PoC 답습 |
|---|---|
| `tests/fixtures/jsonl_ledger/pass/minimal_chain.jsonl` (2 entries Memory chain) | `pass/original_ledger.jsonl` (5 entries 확장) base 답습 |

---

## 6. fixture 10건 사양

### 6.1 PASS × 4 (4 파일 = 2 ledger + 2 anchor)

| 파일 | 내용 |
|------|------|
| `pass/original_ledger.jsonl` | 5 entries Memory chain (Group C minimal_chain 답습 확장) — `agent: user`, `scope: project`, `event: memory_write` × 5 |
| `pass/original_anchor.json` | 11 필드 anchor (anchor_method=ci_run_id, expected_entry_count=5, expected_tail_hash=last entry hash, expected_genesis_hash=Group C compute_genesis_hash 결과) — original_ledger 와 matching |
| `pass/extended_ledger.jsonl` | 5+2 = 7 entries Memory chain (original_ledger 에 2 entries append, 모두 valid) |
| `pass/extended_anchor.json` | 5 entries 시점 anchor (extended_ledger 와 비교 시 entries 5~7 = anchor 후 추가, "anchor_outdated_appended" warning PASS — Layer 5 정상 운영 시제) |

### 6.2 FAIL × 5 (4 ledger 변조 + 1 anchor 변조)

| 파일 | attack scenario | violation 검출 |
|------|----------|----------|
| `fail/full_rewrite_ledger.jsonl` (+ original_anchor) | #1 Full rewrite | tail_hash_mismatch — 모든 entry 재작성, 내부 chain 일관, tail hash 다름 |
| `fail/tail_truncation_ledger.jsonl` (+ original_anchor) | #2 Tail truncation | entry_count_mismatch + tail_hash_mismatch — 마지막 1 entry 제거, 4 entries 남음, valid |
| `fail/middle_deletion_ledger.jsonl` (+ original_anchor) | #3 Middle deletion | entry_count_mismatch + tail_hash_mismatch — 중간 entry 제거 + 이후 prev_hash 재계산, valid |
| `fail/substitution_ledger.jsonl` (+ original_anchor) | #4 Substitution | tail_hash_mismatch + (다른 chain 시) genesis_hash_mismatch 도 가능 — 다른 valid 5-entries chain 으로 교체 |
| `fail/anchor_tampered.json` (+ original_ledger) | #5 Anchor 자체 변조 | anchor_self_inconsistent (또는 expected_tail_hash mismatch) — *known limitation 명시* (anchor 자체 signing 부재) |

### 6.3 chain_only_demo × 1 (Layer 1 inadequacy 시연)

| 파일 | 의도 |
|------|------|
| `chain_only_demo/full_rewrite_ledger.jsonl` | FAIL fixture #1 의 *복사본* (또는 동일 형식) — `--mode chain-only` 실행 시 **PASS** (rc=0) 처리됨을 시연. Layer 1 inadequacy evidence. |

**합산 = 10 fixture** (PASS 4 + FAIL 5 + chain_only_demo 1).

### 6.4 fake canary 의무

본 PoC fixture 의 모든 entry 는 **fake**:
- entry id = UUID v4 형식이지만 의도적으로 deterministic (`11111111-1111-4111-8111-...`)
- entry content = `{"key": "fake-key-for-poc", "value": "fake value"}`
- agent = `user` (실 사용자가 본 PoC 동작 위해 작성한 것으로 가정)
- 외부 LLM 응답 0건 + 실 production data 0건

---

## 7. 검증 매트릭스 (사용자 명시 10 검증 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 결과 |
|---|------|------|------|---------|------|
| 1 | Anchor PASS — original | original_ledger + original_anchor | `--mode anchor-verify pass/original_anchor.json` | 0 | violations=0, anchor matched (entry_count + tail_hash + genesis_hash 모두 일치) |
| 2 | Anchor PASS — extended append | extended_ledger + extended_anchor | `--mode anchor-verify pass/extended_anchor.json` | 0 | violations=0 + warning "anchor_outdated_appended" (Layer 5 정상 운영 — anchor 이후 append OK) |
| 3 | Anchor FAIL — full rewrite | full_rewrite_ledger + original_anchor | `--mode anchor-verify fail/anchor_full_rewrite.json` | 1 | tail_hash_mismatch detected |
| 4 | Anchor FAIL — tail truncation | tail_truncation_ledger + original_anchor | `--mode anchor-verify fail/anchor_tail_truncation.json` | 1 | entry_count_mismatch + tail_hash_mismatch |
| 5 | Anchor FAIL — middle deletion | middle_deletion_ledger + original_anchor | `--mode anchor-verify fail/anchor_middle_deletion.json` | 1 | entry_count_mismatch + tail_hash_mismatch |
| 6 | Anchor FAIL — substitution | substitution_ledger + original_anchor | `--mode anchor-verify fail/anchor_substitution.json` | 1 | tail_hash_mismatch + genesis_hash_mismatch (다른 scope 시) |
| 7 | Anchor FAIL — tampered anchor | original_ledger + anchor_tampered | `--mode anchor-verify fail/anchor_tampered.json` | 1 | anchor_self_inconsistent (expected_tail_hash 변조됨, ledger 와 비교 시 mismatch) — *known limitation 명시* |
| 8 | **Layer 1 inadequacy demo** — chain-only mode | chain_only_demo/full_rewrite_ledger.jsonl | `--mode chain-only chain_only_demo/full_rewrite_ledger.jsonl` | **0 (의도된 PASS)** | "Layer 1 단독으로는 full rewrite 검출 불가" 명시 — Layer 5 의무성 evidence |
| 9 | `--list-attack-models` self-check | — | `--list-attack-models` | 0 | 5 attack scenarios + 11 anchor fields + 1 known limitation enumerate |
| 10 | F-금지 grep | scanner + fixture grep | grep | 0 | 실 signed commit / 실 branch protection / 실 external timestamping service / 실 GitHub API 호출 0건 |

**합산 10 검증** (anchor PASS×2 + FAIL×5 + chain-only demo + list-attack-models + F-금지 grep).

---

## 8. PASS 기준 자기 검증 매트릭스

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | Anchor PASS — original | rc=0 + 위반 0건 |
| 2 | Anchor PASS — extended append | rc=0 + warning "anchor_outdated_appended" |
| 3~6 | Anchor FAIL × 4 (4 attack scenarios) | rc=1 + 각 scenario 별 mismatch type 검출 |
| 7 | Anchor FAIL — tampered anchor | rc=1 + anchor_self_inconsistent (known limitation) |
| 8 | Layer 1 inadequacy demo | rc=0 (의도된 PASS) — Layer 5 의무성 evidence |
| 9 | `--list-attack-models` | 5 attack + 11 fields + 1 limitation 모두 enumerate |
| 10 | F-금지 grep | 0건 (실 signed commit / branch protection / external service / GitHub API 0건) |

**합산 10/10 충족 적격**.

---

## 9. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | Layer 2 (Git append-only branch + denyNonFastForwards) 미진입 | ADR-012 §2.8 별도 layer | 별도 합의 |
| 2 | Layer 3 (pre-commit hook — git rebase/filter-branch/reset 감지) 미진입 | ADR-012 §2.8 별도 layer | 별도 합의 |
| 3 | Layer 4 (CI 회귀 검증 — base branch 대비 line deletion / rewrite 감지) 미진입 | ADR-012 §2.8 별도 layer | 별도 합의 |
| 4 | `anchor_method=signed_tag` / `external_snapshot` 2 메서드 미진입 | 본 PoC = `ci_run_id` 한 메서드 한정 | 별도 합의 |
| 5 | **Anchor metadata 자체 signing (GPG / Sigstore / cosign) 미진입** — anchor 자체 변조 시 *부분* 만 cover (fixture #5) | Layer 5 multi-host MANDATORY 영역 | **multi-host MANDATORY 격상 시 의무 발동** (ADR-012 §2.8 답습) |
| 6 | 실 GitHub Actions run id / commit SHA 검증 (외부 호출) | 본 PoC = literal 비교만 | 별도 합의 |
| 7 | Anchor 자동 갱신 / nightly cron 미진입 | runtime hook 영역 | 별도 합의 |
| 8 | **Multi-host external service 통합 미진입** | ADR-012 §2.8 MANDATORY 격상 영역 | 별도 합의 (multi-host 전환 시) |
| 9 | **1인 동일 호스트 SPOF 한계** (ADR-012 §2.8 + 외부 LLM 1 권고 5 답습) | 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖 | multi-host 전환 시 Layer 5 MANDATORY 발동 |
| 10 | Markdown 본문 자기 검출 (Group D/E/G 답습 패턴) | CI 는 `tests/fixtures/history_anchor_verifier/` 한정 scan 으로 회피 | Group B PoC 사양 §2.8 #1 답습 |
| 11 | 사용자 작업 컨테이너 = `agent: user` 만 cover, `agent: hermes` 의 anchor 작성 시도는 G3 §2.2 #16 답습 영역 (Hermes-originated anchor auto-reject) | 본 PoC 미진입 (Group G `boundary_guard` 영역) | 별도 합의 |

---

## 10. CI workflow 설계

### 10.1 13 step 구조 (Group D/E/G/A3 답습)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Prepare log directory | `mkdir -p group-c-followup-logs` (Group F 후속 답습 — leading dot 미사용) |
| 4 | `--list-attack-models` self-check | rc=0 + 5 attack + 11 fields + 1 limitation grep |
| 5 | Anchor PASS — original | rc=0 + violations=0 + "anchor_matched" grep |
| 6 | Anchor PASS — extended append | rc=0 + "anchor_outdated_appended" grep |
| 7 | Anchor FAIL — full rewrite | rc=1 + "tail_hash_mismatch" grep |
| 8 | Anchor FAIL — tail truncation | rc=1 + "entry_count_mismatch" + "tail_hash_mismatch" grep |
| 9 | Anchor FAIL — middle deletion | rc=1 + "entry_count_mismatch" + "tail_hash_mismatch" grep |
| 10 | Anchor FAIL — substitution | rc=1 + "tail_hash_mismatch" grep |
| 11 | Anchor FAIL — tampered anchor | rc=1 + "anchor_self_inconsistent" grep + known limitation 명시 |
| 12 | **Layer 1 inadequacy demo** — chain-only mode | rc=0 (의도된 PASS) + "Layer 1 단독으로는 full rewrite 검출 불가" 명시 |
| 13 | F-금지 grep + summary.json + Upload artifact + Evidence summary | 실 signed commit / branch protection / external service / GitHub API 0건 + `actions/upload-artifact@v4` `history-anchor-verifier-evidence` retention 30일 + `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-c-followup-logs/`** (Group F 후속 답습 — leading dot 미사용).

### 10.2 paths trigger

```yaml
paths:
  - tools/history_anchor_verifier.py
  - tools/jsonl_hash_chain.py        # Group C 모듈 변경 시 trigger
  - tests/fixtures/history_anchor_verifier/**
  - .github/workflows/history-anchor-verifier.yml
```

---

## 11. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 5 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | signed commit 정책 실 도입 필요 | ❌ 미발화 | anchor metadata file 한정, signed commit = 별도 합의 |
| 2 | branch protection 정책 변경 필요 | ❌ 미발화 | fixture 한정 |
| 3 | external anchor 필수 격상 필요 | ⚠️ 부분 | 본 PoC = MVP RECOMMENDED 시제 한정 (multi-host MANDATORY 격상 = 별도 합의) — known limitation 분리 |
| 4 | Evidence Ledger hash chain 구조 자체 변경 필요 | ❌ 미발화 | Group C 11-field schema 답습만 |
| 5 | ADR-012 본문 결정 변경 필요 | ❌ 미발화 | cross-reference 답습 한정 |

**합산 0/5 발화 (#3 부분은 known limitation 분리)** → **Reviewer-only 단축 합의 적격**.

---

## 12. Evidence 형식 (5종 — Group A/B/C/D/E/F/G/A3 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g4-history-rewrite-...`) | 본 문서 |
| JSONL ledger entry | summary.json (단순화 — Group D/E/G/A3 답습) | summary.json 14 항목 |
| 격리 검증 | fixture 한정 + 외부 의존 0건 + 실 GitHub API 호출 0건 | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `history-anchor-verifier.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g4-history-rewrite-layer5-...`) | 본 PoC 산출물 #8 |

---

## 13. 본 PoC 의 *evidence 가치* (사용자 명시 답습)

본 PoC 가 답하는 핵심 (사용자 명시 §0 답습):

> "Layer 1 hash chain만으로는 full rewrite / truncation / middle deletion / substitution을 잡지 못할 수 있다. Layer 5 external anchor metadata가 있으면 tail hash, entry count, genesis hash mismatch로 이를 검출할 수 있다."

### 13.1 본 PoC 가 *발생* 시키는 것

- ✅ ADR-012 §2.8 *Layer 5 External anchor* 의 *형식적 검출 layer* 운영 적용 첫 시제
- ✅ Layer 1 inadequacy 시연 — 4 attack scenario 모두 Group C `validate_chain` 단독 시 PASS 처리됨 (의도된 한계)
- ✅ Layer 5 의무성 evidence — 동일 4 시나리오 + substitution + anchor tampered 모두 anchor mismatch 로 검출
- ✅ Custom validator 단독 채택 (외부 의존 0건 + Layer 2~4 미진입) 답습 검증
- ✅ Group C 산출물 (`jsonl_hash_chain` `validate_chain` + ENUMs + `compute_genesis_hash`) import 직접 답습
- ✅ Group F 후속 artifact path 답습 (`group-c-followup-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A~G 답습)

### 13.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G4 전체 Implementation/Runtime PASS 선언
- ❌ G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ ADR-012 §2.8 5 Layer 中 Layer 2/3/4 통합
- ❌ 실 signed commit 강제 / 실 branch protection 변경 / 실 external timestamping service 연동
- ❌ Anchor metadata 자체 signing (GPG / Sigstore / cosign)
- ❌ 실 GitHub Actions run id 검증 (외부 호출)
- ❌ Multi-host external service 통합

---

## 14. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group C 후속 진입 사양 — ADR-012 §2.8 *Layer 5 External anchor* 영역 정적 검출 PoC. 사용자 명시 10 검증 / 5 trigger / 7 금지 / 10 fixture / 5 attack scenario / 11-field anchor schema / stdlib 단독 채택. Group A 1차/2차/3차 + Group B + Group C + Group D + Group E + Group F + Group G 사양 형식 직접 답습. ADR-012 §2.8 + §2.12 + G4 §4.4.5 + Group C `validate_chain` 답습 (변경 0건). Reviewer-only 단축 합의 적격 (풀 3+1 trigger 0/5 발화). artifact path `group-c-followup-logs/` (Group F 후속 답습, leading dot 미사용). **본 PoC 핵심 evidence = Layer 1 inadequacy demo** (chain-only mode 에서 full rewrite *의도된 PASS* 처리 → Layer 5 의무성 evidence). |
