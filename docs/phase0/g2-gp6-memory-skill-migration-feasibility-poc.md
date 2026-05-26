# G2 GP-6 Memory/Skill Migration Feasibility — Group F PoC 사양

> **상태**: DRAFT (2026-05-10, Group F 진입 — Memory/Skill provider-agnostic JSONL round-trip *feasibility* 통합 PoC)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §3.1 (G2 GP-6 매트릭스 — Order 7, 그룹 F = "Group C round-trip 답습 + R2-5") / §5.3 (그룹 F 의존성 = 그룹 C 완료 후) / §5.4 (단축 합의 + PoC evidence)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §4.2 (11 필드 schema) / §4.6 (Tier-based round-trip — T2 strict / T3 lossy / Migration rollback)
> - `docs/architecture/governance-preconditions.md` §8 (GP-6 Memory/Skill Migration)
> - `docs/decisions/ADR-008-hermes-adoption-decision.md` 차단조건 #2 (JSONL export — Hermes 의존 0)
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.9 (3 ledger entry 형식 — `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`) / §2.10 (Migration BLOCK + manual + `migration_failed`)
> - `docs/phase0/g4-jsonl-hash-chain-jcs-poc-spec.md` §2 (11 필드 schema 답습) — Group C 산출물 직접 import
> **PASS 조건 답습**: `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e), 사용자 명시 F-범위 10 / F-금지 9 / 풀 3+1 승격 trigger 6 / PASS 기준 9
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance PASS ↔ Implementation/Runtime PASS 분리), P2 v3 §3.1.4 (Implementation Pending), Provider Liquidity Layer 4 (모델/구독 교체 코드 변경 0건)
> **답습 시제**: Group A 1차 + 2차 + Group B + Group C PoC 사양 형식 (`g4-jsonl-hash-chain-jcs-poc-spec.md` 직접 답습)

---

## 0. 목적

본 PoC 는 G2 GP-6 *Memory/Skill Migration Feasibility* 의 첫 시제 — Group C 산출물 (`tools/canonical_json.py` + `tools/jsonl_hash_chain.py` + `tools/jsonl_roundtrip.py`) 을 Memory/Skill 영역에 *재사용 가능한지* 의 형식적 검증.

핵심 질문 4건 (사용자 명시 — Group F 진입 directive):

1. G4 JSONL schema (11 필드) 가 Memory/Skill migration 후보 데이터에도 적용 가능한가?
2. Round-trip 검증이 Memory/Skill 구조에서도 동작하는가?
3. lossy case (vendor-specific field drop) 를 감지할 수 있는가?
4. `roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail` / `chain_violation_detected` event 기록이 Memory/Skill 에서도 동작하는가?

본 PoC = **feasibility 한정** — 실 migration script (`hermes_to_claude.py` / `hermes_to_openai.py` 본 구현) 은 Group H 영역 (사용자 명시 금지). 토이 dict 변환 함수만 작성 (provider SDK 호출 0건, 디스크 Hermes 데이터 0건, fixture 한정).

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §3.1 + G4 §4 + ADR-012 §2.9 + §2.10 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md` | PoC 사양 + 답습 매핑 + F-범위/금지/trigger 매트릭스 |
| Validator | `tools/memory_skill_roundtrip.py` | Memory/Skill 전용 wrapper. Group C 3 모듈 import (리팩토링 0건). hermes ↔ canonical ↔ claude toy transformation + lost_fields enum + 4 verdict |
| PASS fixture × 2 | `tests/fixtures/memory_skill_migration/pass/{memory_global,skill_project}.jsonl` | T2 strict — Memory (`memory_write`, `global`) + Skill (`skill_promoted`, `project`, content=17 필드 sample) |
| LOSSY fixture × 1 | `tests/fixtures/memory_skill_migration/lossy/hermes_to_claude_memory.jsonl` | T3 lossy — Hermes vendor-specific 필드 (`_hermes_internal_id`) 포함, claude 변환 시 drop → `lost_fields` enum |
| FAIL fixture × 1 | `tests/fixtures/memory_skill_migration/fail/chain_violation_memory.jsonl` | FAIL — `prev_hash_mismatch` (jsonl_hash_chain 답습) + `roundtrip_fail` |
| CI workflow | `.github/workflows/memory-skill-migration-feasibility.yml` | PASS/LOSSY/FAIL 양방향 + Evidence summary (Group A/B/C 형식 답습) |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md` | PoC 검토 + 풀 3+1 trigger 6 자기 검증 0/6 |

**합산 = 8 파일** (사양 1 + 코드 1 + fixture 4 + CI 1 + 합의 1).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 F-금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| 실 Hermes 디스크 데이터 사용 | **사용자 명시 F-금지 #1** — fixture 한정 |
| 실 provider SDK 호출 (anthropic / openai / google.generativeai) | **사용자 명시 F-금지 #2** — 토이 dict 변환만 |
| 실 migration script 본 구현 (`hermes_to_claude.py` / `hermes_to_openai.py`) | **사용자 명시 F-금지 #3** — Group H 영역 (ADR-014 발행 trigger 후 별도 풀 3+1) |
| Provider 간 cross-format migration 자동 진입 | **사용자 명시 F-금지 #4** — 토이 매핑 1건 (Memory hermes→claude) 한정 |
| Tier-2 / Tier-3 catalog 확장 | **사용자 명시 F-금지 #5** |
| G2 GP-6 최종 Implementation/Runtime PASS 선언 | **사용자 명시 F-금지 #6** — *feasibility 시제 한정* |
| G2 / G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시 F-금지 #7~8** |
| Hermes PMO 격상 선언 | **사용자 명시 F-금지 #9** — 4 게이트 모두 PASS + 외부 LLM + 사용자 명시 결정 후 별도 |
| 실 migration script 구현 | **사용자 명시 F-금지** — Group H 영역 |
| ADR 본문 자동 갱신 | **사용자 명시 F-금지** — cross-reference 답습 한정 |
| Memory/Skill schema 변경 | **풀 3+1 승격 trigger #3** — 본 PoC = G4 §4.2 11 필드 답습만 |
| Skill `forbidden_actions` 강제 | Group G 영역 (roadmap §3 답습) |
| Memory boundary 4 금지 hook | Group G 영역 (roadmap §4.1 답습) |

---

## 2. 변환 feasibility 토이 매핑 정의

### 2.1 토이 매핑 함수 3종 (`tools/memory_skill_roundtrip.py`)

본 PoC 는 *Hermes-format ↔ canonical JSONL ↔ Claude-format* 의 *형식 차이* 를 **dict 키 추가/삭제** 한정으로 시뮬레이션. 실 Hermes / Claude SDK 구조는 미사용.

```
def hermes_to_canonical(entry: dict) -> tuple[dict, list[str]]:
    """Hermes vendor-specific 필드 (`_hermes_*`) 제거 → canonical 11 필드 한정.
    반환: (canonical_entry, dropped_field_names)
    """

def canonical_to_claude(entry: dict) -> dict:
    """Canonical 11 필드 → Claude toy format (필드 추가 0건, 본 PoC 토이 = identity).
    실 Claude format 은 Group H 영역 — 본 함수는 *형식 보존* 강제 (lossy 0).
    """

def claude_to_canonical(entry: dict) -> tuple[dict, list[str]]:
    """Claude toy format → canonical 11 필드 (역방향).
    본 PoC 토이 = identity → lost_fields = []. 실 Claude → canonical lossy 는 Group H 영역.
    """
```

### 2.2 검증 흐름 (lossy 감지 6 단계)

```
Step 1: Hermes-format input 로드 (fixture)
        예: { "type": "memory", "_hermes_internal_id": "h-xxx", ...11 필드 }
Step 2: hermes_to_canonical(entry) → canonical (11 필드만) + dropped = ["_hermes_internal_id"]
Step 3: round_trip(canonical_list) → T2 strict (canonical 층은 byte 일치)
Step 4: canonical_to_claude(entry) → claude_format (본 PoC 토이 = identity)
Step 5: claude_to_canonical(entry) → canonical_2 + dropped_2 = []
Step 6: diff = diff_lost_fields(original_hermes, canonical_2) → lost_fields = dropped (Step 2)
        → roundtrip_lossy ledger entry 자동 작성 (lost_fields_count ≥ 1)
```

**핵심 강제**: canonical 층은 항상 T2 strict (byte 일치). lossy 는 *Hermes ↔ canonical 경계* 에서만 발생 (vendor-specific 필드 drop).

### 2.3 토이 매핑 한계 (의도된 분리)

| 한계 | 분리 이유 |
|------|----------|
| Claude format 은 toy identity (실 Claude API 형식 미반영) | 실 형식 = Group H 영역 (ADR-014 발행 후) |
| `_hermes_internal_id` 외 vendor-specific 필드 미카탈로그화 | catalog 확장 = 별도 합의 (Tier-2/3 catalog 확장 금지 답습) |
| `hermes_to_openai` 변환 미구현 | F-범위 #4 = "1개 이상" 충족 (Memory hermes→claude 단독) |
| Skill 변환 미구현 | F-범위 #4 = Memory 한정 (Skill PASS 는 canonical 층 round-trip 만) |

---

## 3. Fixture 사양

### 3.1 PASS fixture 1 — `pass/memory_global.jsonl` (Memory T2 strict)

3 entries chain:
- entry 1: `event=memory_write`, `scope=global`, content={`key`:`user_role`, `value`:`software_engineer`}
- entry 2: `event=memory_write`, `scope=global`, content={`key`:`preferred_lang`, `value`:`python`}
- entry 3: `event=memory_write`, `scope=global`, content={`key`:`tdd`, `value`:true}

**예상**: round_trip rc=0, verdict=`roundtrip_pass`, hash chain valid.

### 3.2 PASS fixture 2 — `pass/skill_project.jsonl` (Skill T2 strict)

3 entries chain:
- entry 1: `event=skill_proposed`, `scope=project`, content={Skill 17 필드 sample — `id`, `name`, `version`, `scope`, `owner`, `description`, `inputs`, `outputs`, `allowed_actions`, ..., `promotion_status=proposed`}
- entry 2: `event=skill_approved`, `scope=project`, content={동일 skill, `promotion_status=approved`}
- entry 3: `event=skill_promoted`, `scope=project`, content={동일 skill, `promotion_status=promoted`, `last_verified_at`}

**예상**: round_trip rc=0, verdict=`roundtrip_pass`, hash chain valid.

### 3.3 LOSSY fixture — `lossy/hermes_to_claude_memory.jsonl` (T3 lossy 감지)

2 entries chain (Hermes-format input — 12 필드):
- entry 1: 11 canonical 필드 + `_hermes_internal_id="h-aaa"` (vendor-specific)
- entry 2: 11 canonical 필드 + `_hermes_internal_id="h-bbb"`

**예상**: 본 PoC validator `--feasibility-mode hermes-to-claude` 실행 시:
- canonical 층 round_trip rc=0 (T2 strict on canonical projection)
- 토이 매핑 검증 → lost_fields = [`_hermes_internal_id` × 2]
- 자동 ledger entry 작성: `event=roundtrip_lossy`, `lost_fields_count=2`
- 종료 코드: rc=1 (LOSSY)

### 3.4 FAIL fixture — `fail/chain_violation_memory.jsonl` (chain violation)

2 entries chain:
- entry 1: 정상 Memory entry (hash 정합)
- entry 2: `prev_hash` 가 entry 1 의 `hash` 와 *불일치* (intentional `prev_hash_mismatch`)

**예상**:
- jsonl_hash_chain 검증 실패 (1 violation: `prev_hash_mismatch`)
- 자동 ledger entry 작성: `event=chain_violation_detected`
- round_trip 미진입 (parse 단계는 OK, hash chain 단계 실패) — `event=roundtrip_fail` 또는 chain_violation 우선
- 종료 코드: rc=2 (FAIL)

---

## 4. 검증 매트릭스 (PoC 종료 시점 자기 검증 의무)

| # | 검증 | 입력 | 명령 | 예상 rc | 예상 verdict |
|---|------|------|------|---------|-------------|
| 1 | Memory PASS | `pass/memory_global.jsonl` | `python tools/memory_skill_roundtrip.py pass/memory_global.jsonl` | 0 | `roundtrip_pass` |
| 2 | Skill PASS | `pass/skill_project.jsonl` | `python tools/memory_skill_roundtrip.py pass/skill_project.jsonl` | 0 | `roundtrip_pass` |
| 3 | Hermes→Claude LOSSY | `lossy/hermes_to_claude_memory.jsonl` | `python tools/memory_skill_roundtrip.py --feasibility-mode hermes-to-claude lossy/hermes_to_claude_memory.jsonl` | 1 | `roundtrip_lossy` (lost_fields ≥ 1) |
| 4 | Chain violation FAIL | `fail/chain_violation_memory.jsonl` | `python tools/memory_skill_roundtrip.py fail/chain_violation_memory.jsonl` | 2 | `chain_violation_detected` (Group C answer) + `roundtrip_fail` |

**합산 = 4 검증 (PASS 2 + LOSSY 1 + FAIL 1)**.

---

## 5. 답습 매핑 (Group C 모듈 → Group F)

### 5.1 import 직접 (리팩토링 0건)

```python
# tools/memory_skill_roundtrip.py
from canonical_json import to_canonical, CrossCheckMode, CanonicalizationError
from jsonl_hash_chain import (
    parse_jsonl,
    compute_entry_hash,
    compute_genesis_hash,
    ALLOWED_TYPES,        # ("memory", "skill", "meta") — 이미 Memory/Skill 지원
    ALLOWED_SCOPES,
    ALLOWED_AGENTS,
    SUPPORTED_SCHEMA_VERSION,  # "0.1"
    ViolationType,
)
from jsonl_roundtrip import (
    round_trip,
    build_roundtrip_entry,
    RoundtripVerdict,
    RoundtripResult,
    diff_lost_fields,
)
```

### 5.2 답습 분포

| Group F 영역 | Group C 답습 | 신규 작성 |
|---|---|---|
| 11 필드 schema 검증 | `jsonl_hash_chain.parse_jsonl` 직접 사용 | 0 |
| Hash chain (prev_hash + Genesis) | `compute_genesis_hash` + `compute_entry_hash` 직접 사용 | 0 |
| Canonical JSON (RFC 8785 JCS) | `canonical_json.to_canonical` 직접 사용 | 0 |
| Round-trip (T2 strict) | `jsonl_roundtrip.round_trip` 직접 사용 | 0 |
| `lost_fields` enum | `diff_lost_fields` 직접 사용 | 0 |
| Ledger entry 자동 작성 | `build_roundtrip_entry` 직접 사용 | 0 |
| 토이 매핑 3 함수 (`hermes_to_canonical` 등) | — | ~30 줄 (본 PoC 신규) |
| `--feasibility-mode hermes-to-claude` CLI | — | ~50 줄 (본 PoC 신규) |
| 4 fixture 작성 | — | ~10 entries (본 PoC 신규) |

**리팩토링 0건 / 복제 0건 / 공유 모듈 import 직접 = F-사전 결정 1순위 충족**.

### 5.3 G4 §4.2 11 필드 답습 (변경 0건)

본 PoC 는 G4 §4.2 schema 를 **변경 없이** 답습:

| # | 필드 | 답습 출처 | 본 PoC 검증 |
|---|------|----------|------------|
| 1~11 | `type` / `scope` / `id` / `schema_version` / `ts` / `agent` / `event` / `content` / `evidence_refs` / `prev_hash` / `hash` | G4 §4.2 + ADR-012 §2.2 | `parse_jsonl` 답습 (Group C 검증 답습) |

**Schema 변경 0건** = 풀 3+1 승격 trigger #3 미발화 (사용자 명시 답습).

---

## 6. PASS 기준 9 자기 검증 매트릭스 (사용자 명시)

| # | PASS 기준 | 본 PoC 충족 | Evidence |
|---|----------|------------|----------|
| 1 | Memory fixture round-trip PASS | §4 검증 #1 → rc=0 + `roundtrip_pass` | 양방향 검증 결과 |
| 2 | Skill fixture round-trip PASS | §4 검증 #2 → rc=0 + `roundtrip_pass` | 양방향 검증 결과 |
| 3 | T2 strict case hash 재현 | §4 검증 #1+#2 → sha256_1 == sha256_2 | round_trip detail |
| 4 | T3 lossy case 감지 | §4 검증 #3 → rc=1 + `roundtrip_lossy` + `lost_fields ≥ 1` | lost_fields enum |
| 5 | failure event 기록 | §4 검증 #3+#4 → 자동 ledger entry (`roundtrip_lossy` / `chain_violation_detected` / `roundtrip_fail`) | `build_roundtrip_entry` 출력 |
| 6 | Group C round-trip 패턴 재사용 또는 제한적 복제 근거 명시 | §5.1 import 직접 + §5.2 분포 (리팩토링 0 / 복제 0 / 신규 ~80 줄) | 본 사양 §5 |
| 7 | CI 또는 로컬 명령으로 재현 가능 | §1.1 산출물 #6 (`memory-skill-migration-feasibility.yml`) + §4 검증 명령 | GitHub Actions actual run |
| 8 | evidence 문서 작성 | 본 사양 + 합의 보고서 + GitHub Actions run id | `docs/phase0/` + `docs/review/` |
| 9 | Reviewer-only 단축 합의 APPROVE 또는 APPROVE WITH CONDITIONS | §1.1 산출물 #8 (Reviewer-only) | `docs/review/3plus1-consensus-2026-05-10-g2-gp6-...` |

**합산 9/9 충족 적격** (PoC 종료 시점 자기 검증 의무).

---

## 7. F-금지 9 자기 검증 매트릭스 (사용자 명시)

| # | F-금지 | 본 PoC 차단 메커니즘 | 자기 검증 |
|---|--------|---------------------|----------|
| 1 | 실 Hermes 디스크 데이터 사용 | fixture 한정 (`tests/fixtures/memory_skill_migration/`) | grep 0건 — `~/.claude` / `hermes_state.py` / 실 디스크 경로 미참조 |
| 2 | 실 provider SDK 호출 | 토이 dict 변환만, `import openai` / `import anthropic` / `google.generativeai` 0건 | provider_import_scanner.py 답습 검증 |
| 3 | 실 migration script 본 구현 | `tools/memory_skill_roundtrip.py` = feasibility 한정 (~80 줄 신규), 실 migration script 미작성 | 산출물 1 파일 한정 (Group H 분리) |
| 4 | provider 간 cross-format migration 자동 진입 | 토이 매핑 1건 (Memory hermes→claude), `--feasibility-mode` 명시 플래그 한정, 자동 진입 0건 | `--feasibility-mode` 미지정 시 일반 round-trip 만 |
| 5 | Tier-2 / Tier-3 catalog 확장 | catalog 변경 0건 (Tier-1 42 catalog 답습 영역 미진입) | `redaction-pattern-equivalence.md` 미수정 |
| 6 | G2 GP-6 최종 Implementation/Runtime PASS 선언 | 본 PoC = *feasibility 시제* 한정, 최종 PASS 선언 0건 | 사양 §0 + §6 명시 |
| 7 | G2 전체 Implementation/Runtime PASS 선언 | 본 PoC = G2 6 GP 중 GP-6 부분 충족만, 전체 PASS 선언 0건 | CONTEXT.md 갱신 영역 0건 |
| 8 | Hermes PMO 격상 선언 | 본 PoC 진입 후 4 게이트 합산 변경 0건 | CONTEXT.md "Hermes PMO 격상 = 미선언" 유지 |
| 9 | ADR 본문 자동 갱신 | ADR-008 / ADR-011 / ADR-012 / G4 cross-reference 답습 한정, 본문 변경 0건 | `git diff docs/decisions/` 0건 + `git diff docs/architecture/provider-agnostic-memory-skill-design.md` 0건 |

**합산 0/9 위반 적격** (PoC 종료 시점 자기 검증 의무).

---

## 8. 풀 3+1 승격 trigger 6 자기 검증 (사용자 명시)

| # | Trigger | 본 PoC 발화 여부 | 자기 검증 |
|---|---------|-----------------|----------|
| 1 | 실제 migration script 구현 필요 | ❌ 미발화 — 토이 매핑 1건 (산출물 1 파일) | `tools/memory_skill_roundtrip.py` 신규 ~80 줄, 실 migration script 0 파일 |
| 2 | provider 간 cross-format migration 필요 | ❌ 미발화 — 토이 1건 (Memory hermes→claude), 자동 진입 0건 | `--feasibility-mode` 명시 플래그 한정 |
| 3 | Memory/Skill schema 자체 변경 | ❌ 미발화 — G4 §4.2 11 필드 답습만 | provider-agnostic-memory-skill-design.md 변경 0건 |
| 4 | ADR-014 발행 trigger 발생 | ❌ 미발화 — Group H 영역 미진입 | `docs/decisions/ADR-014-*.md` 작성 0건 |
| 5 | G4 / ADR-012 / ADR-011 원칙 충돌 | ❌ 미발화 — 답습만 | 본 사양 §0 + §5 cross-reference 영역 한정 |
| 6 | Implementation PASS 기준 완화 위험 | ❌ 미발화 — *feasibility 시제* 한정, PASS 기준 완화 0건 | 사양 §0 + §1.2 명시 분리 |

**합산 0/6 발화 → Reviewer-only 단축 합의 적격** (사용자 명시 답습).

---

## 9. Evidence 형식 (5종 — Group A/B/C 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g2-gp6-...`) | 본 문서 |
| JSONL ledger entry | fixture 내부 entries + validator 자동 작성 entry | `build_roundtrip_entry` 출력 |
| 토이 매핑 격리 검증 | fixture 한정 (provider SDK / 실 Hermes 디스크 0건) | provider_import_scanner.py 회귀 답습 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `memory-skill-migration-feasibility.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g2-gp6-...`) | 본 PoC 산출물 #8 |

---

## 10. 한계 (의도된 분리 — 본 PoC 미커버)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | 실 Hermes SQLite / 실 Claude `~/.claude/memory.jsonl` / 실 OpenAI export 형식 미연동 | 사용자 명시 F-금지 #1~#2 | Group H (ADR-014 발행 후) |
| 2 | `hermes_to_openai` 변환 미구현 | F-범위 #4 = 1개 이상 (Memory hermes→claude 한정) | Group H 후속 영역 |
| 3 | Skill 변환 feasibility 미구현 | F-범위 #4 = Memory 한정 | Group H 후속 |
| 4 | Vendor-specific 필드 catalog 미카탈로그화 (`_hermes_*` 1건 한정) | Tier-2/3 catalog 확장 금지 답습 | 별도 합의 |
| 5 | Round-trip nightly cron 미설정 | feasibility 한정 — Group F 종료 시 별도 합의 | G2 GP-6 후속 PASS PoC |
| 6 | Migration BLOCK + manual + `migration_failed` event 검증 미커버 | ADR-012 §2.10 = 실 migration 영역 | Group H |
| 7 | Full Rewrite 5 Layer 방어 (history_rewrite) 미커버 | Group C 후속 별도 영역 (사용자 명시 후보 7) | 별도 PoC |
| 8 | Memory boundary 4 금지 hook 미커버 | Group G 영역 | 별도 합의 |
| 9 | Skill `forbidden_actions` runtime 강제 미커버 | Group G 영역 | 별도 합의 |

---

## 11. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group F 진입 사양 — 사용자 명시 F-범위 10 / F-금지 9 / 풀 3+1 trigger 6 / PASS 기준 9 답습. Group A 1차/2차 + Group B + Group C 사양 형식 직접 답습. Group C 산출물 (`canonical_json.py` + `jsonl_hash_chain.py` + `jsonl_roundtrip.py`) import 직접 (리팩토링 0건 / 복제 0건). |
