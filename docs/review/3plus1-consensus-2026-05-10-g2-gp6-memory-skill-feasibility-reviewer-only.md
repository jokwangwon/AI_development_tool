# 3+1 합의 보고서 — G2 GP-6 Memory/Skill Migration Feasibility (Group F PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group F 진입 — Memory/Skill provider-agnostic JSONL round-trip *feasibility* 통합 PoC)
> **PASS scope**: G2 GP-6 *feasibility 시제* 한정 — **Implementation Pending** (G2 GP-6 / G2 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 6 = 0/6 발화 → 단축 적격, 사용자 명시 답습)
> **검토 대상**:
> - `tools/memory_skill_roundtrip.py`
> - `tests/fixtures/memory_skill_migration/{pass,lossy,fail}/*.jsonl`
> - `.github/workflows/memory-skill-migration-feasibility.yml`
> - `docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md`
> - `.gitignore` (`.venv-group-f/` + `.group-f-logs/` 추가)
> **상위 권위**: ADR-008 부록 C (Design/Governance ↔ Implementation/Runtime 분리), ADR-011 §2.1 (a)~(e), ADR-012 §2.9 / §2.10, G4 §4.2 / §4.6, governance-preconditions.md §8 (GP-6), implementation-runtime-roadmap.md §3.1 / §5.3 / §5.4
> **답습 시제**: Group A 1차/2차 + Group B + Group C PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g4-poc-implementation-reviewer-only.md` 직접 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/memory_skill_roundtrip.py` | 245 | Group C 3 모듈 (`canonical_json` + `jsonl_hash_chain` + `jsonl_roundtrip`) **import 직접** + 토이 매핑 3 함수 + `--feasibility-mode hermes-to-claude` CLI + `build_feasibility_lossy_entry` ledger entry 자동 작성 |
| 2 | `tests/fixtures/memory_skill_migration/pass/memory_global.jsonl` | 3 entries | T2 strict Memory chain (event=`memory_write`, scope=`global`) — Group C `minimal_chain.jsonl` 형식 답습 |
| 3 | `tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` | 3 entries | T2 strict Skill chain (event=`skill_proposed` → `skill_approved` → `skill_promoted`, scope=`project`, content=17 필드 sample) |
| 4 | `tests/fixtures/memory_skill_migration/lossy/hermes_to_claude_memory.jsonl` | 2 entries | Hermes vendor-specific 필드 (`_hermes_internal_id`) 포함, hash chain 정합 (12 필드 hash) |
| 5 | `tests/fixtures/memory_skill_migration/fail/chain_violation_memory.jsonl` | 2 entries | entry 2 의 `prev_hash` 의도적 0×64 (PREV_HASH_MISMATCH 한정) — Group C `prev_hash_mismatch.jsonl` 형식 답습 |
| 6 | `.github/workflows/memory-skill-migration-feasibility.yml` | 187 | Group C `g4-hash-chain.yml` 형식 답습 + 4 검증 step + F-금지 grep step + summary.json + artifact upload + Evidence summary |
| 7 | `docs/phase0/g2-gp6-memory-skill-migration-feasibility-poc.md` | 315 | Group C `g4-jsonl-hash-chain-jcs-poc-spec.md` 형식 직접 답습 (11 섹션 — 목적 / 범위 / 토이 매핑 / fixture / 검증 매트릭스 / 답습 매핑 / PASS 9 / F-금지 9 / trigger 6 / Evidence 5 / 한계 9) |
| 8 | 본 합의 보고서 | ~280 | Group A 1·2차 + Group B + Group C Reviewer-only 합의 형식 답습 |

**합산 = 8 파일** (사용자 명시 사양 §1.1 일치).

### 1.2 로컬 양방향 검증 결과 (4/4 PASS)

| # | 검증 | 명령 | rc | verdict / lost_fields / ledger entry |
|---|------|------|-----|--------------------------------------|
| 1 | Memory PASS | `python tools/memory_skill_roundtrip.py tests/fixtures/memory_skill_migration/pass/memory_global.jsonl --emit-ledger-entry` | **0** | `verdict=roundtrip_pass`, `sha256_1=sha256_2=87418e0f...`, lost_fields=0, `event=roundtrip_pass` ledger entry 자동 |
| 2 | Skill PASS | `python tools/memory_skill_roundtrip.py tests/fixtures/memory_skill_migration/pass/skill_project.jsonl` | **0** | `verdict=roundtrip_pass`, `sha256_1=sha256_2=bdd857de...`, lost_fields=0 |
| 3 | Hermes→Claude LOSSY | `python tools/memory_skill_roundtrip.py --feasibility-mode hermes-to-claude --emit-ledger-entry tests/fixtures/memory_skill_migration/lossy/hermes_to_claude_memory.jsonl` | **1** | `verdict=roundtrip_lossy`, lost_fields=2 (`entry[0]._hermes_internal_id`, `entry[1]._hermes_internal_id`), `event=roundtrip_lossy` ledger entry 자동 (lost_fields_sample 명시) |
| 4 | Chain violation FAIL | `python tools/memory_skill_roundtrip.py --emit-ledger-entry tests/fixtures/memory_skill_migration/fail/chain_violation_memory.jsonl` | **2** | `CHAIN_VIOLATION: 1 violation(s)`, `prev_hash_mismatch`, `event=chain_violation_detected` ledger entry 자동 |

**보조 검증**: LOSSY fixture 의 *default mode* 동작 = rc=0 + `roundtrip_pass` (chain 정합 + T2 strict on as-is) — feasibility 시제 진입 전제 확보 (사양 §3.3 답습).

### 1.3 CI workflow 12 step 검증

YAML syntax 검증 통과 (1 job `feasibility`, 12 step). 로컬 step 재현 4/4 PASS:

| # | Step | 본 합의 검증 | 검증 layer |
|---|------|------------|-----------|
| 1 | Checkout | actions/checkout@v4 | — |
| 2 | Set up Python | actions/setup-python@v5 (3.12) | — |
| 3 | Install Group C deps | `rfc8785==0.1.4` + `jcs==0.2.1` | Group C 답습 |
| 4 | Prepare log directory | `.group-f-logs/` 준비 | artifact 답습 |
| 5 | Memory PASS | rc=0 + `verdict=roundtrip_pass` 명시 grep | §1.2 #1 |
| 6 | Skill PASS | rc=0 + `verdict=roundtrip_pass` 명시 grep | §1.2 #2 |
| 7 | Hermes→Claude LOSSY | rc=1 + `verdict=roundtrip_lossy` + `lost_fields ≥ 1` 강제 + `"event": "roundtrip_lossy"` ledger entry stdout 검증 | §1.2 #3 |
| 8 | Chain violation FAIL | rc=2 + `CHAIN_VIOLATION` + `prev_hash_mismatch` + `"event": "chain_violation_detected"` ledger entry stdout 검증 | §1.2 #4 |
| 9 | F-금지 자기 검증 (Layer 1 grep) | provider SDK import 0건 + 실 migration script 작성 0건 | §2.4 자동화 |
| 10 | Build summary.json | step output 집계 → JSON | §2.8 |
| 11 | Upload feasibility logs | `actions/upload-artifact@v4` `memory-skill-migration-feasibility-evidence` retention 30일 | §2.8 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` 13 항목 | R-6 답습 |

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | PoC 사양 §0 — 본 PoC 가 발생시키는 안전 결과 = "Memory/Skill JSONL ledger 가 hash chain 정합 + canonical 층 round-trip + lossy 감지 가능"의 *형식적* feasibility 1차 시제 |
| (b) 격리 환경 PoC 실증 | ✅ | `.venv-group-f/` 격리 venv (rfc8785+jcs 한정), fixture 한정 (실 Hermes 디스크 0건), CI 환경 ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | 사양 + 본 합의 헤더 = ADR-008 부록 C / ADR-011 §2.1 / ADR-012 §2.9 / G4 §4.2 / §4.6 / GP §8 / roadmap §3.1 cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 4 검증 step + paths trigger 7 영역 (Group C 모듈 변경 시도 trigger) + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 9 (사양 §6 답습)

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | Memory fixture round-trip PASS | ✅ | §1.2 #1 → rc=0 + `roundtrip_pass` |
| 2 | Skill fixture round-trip PASS | ✅ | §1.2 #2 → rc=0 + `roundtrip_pass` |
| 3 | T2 strict case hash 재현 | ✅ | §1.2 #1+#2 → `sha256_1 == sha256_2` |
| 4 | T3 lossy case 감지 | ✅ | §1.2 #3 → rc=1 + `roundtrip_lossy` + lost_fields=2 |
| 5 | failure event 기록 | ✅ | §1.2 #3+#4 → 자동 ledger entry (`roundtrip_lossy` + `chain_violation_detected`) |
| 6 | Group C round-trip 패턴 재사용 또는 제한적 복제 근거 명시 | ✅ | §2.6 답습 분포 — import 직접 / 리팩토링 0 / 복제 0 / 신규 ~80 줄 |
| 7 | CI 또는 로컬 명령으로 재현 가능 | ✅ | CI workflow 12 step + 로컬 명령 §1.2 |
| 8 | evidence 문서 작성 | ✅ | 사양 + 본 합의 (별도 evidence 파일 미작성, Group B/C 답습) |
| 9 | Reviewer-only 단축 합의 APPROVE 또는 APPROVE WITH CONDITIONS | ✅ | 본 보고서 §5.1 = APPROVE WITH CONDITIONS |

**합산 = 9/9 충족.**

### 2.3 사용자 명시 F-범위 10 답습 (사양 §1.5 답습)

| F-범위 # | 사용자 명시 | 본 PoC 충족 |
|---|---|---|
| 1 | Group C jsonl_roundtrip.py 패턴 답습 | ✅ import 직접 (사양 §5.1) |
| 2 | Memory fixture 1종 이상 | ✅ `pass/memory_global.jsonl` (3 entries) |
| 3 | Skill fixture 1종 이상 | ✅ `pass/skill_project.jsonl` (3 entries, 17 필드) |
| 4 | hermes_to_claude/openai 변환 feasibility 1+ | ✅ 토이 매핑 (Memory hermes→claude, 2 entries) |
| 5 | export → import → re-export → hash 비교 | ✅ `round_trip()` 답습 (canonical 층 T2 strict) |
| 6 | T2 strict case 1+ | ✅ Memory + Skill PASS 2건 |
| 7 | T3 lossy case 1+ | ✅ Hermes→Claude LOSSY 1건 |
| 8 | failure event 기록 | ✅ `roundtrip_lossy` + `chain_violation_detected` ledger entry 자동 |
| 9 | CI step 또는 로컬 검증 명령 | ✅ 양쪽 모두 (CI 12 step + 로컬 명령) |
| 10 | Reviewer-only 단축 합의 | ✅ 본 보고서 |

**합산 = 10/10 충족.**

### 2.4 사용자 명시 F-금지 9 자기 검증 (0/9 위반)

| # | F-금지 | 위반 | 근거 |
|---|--------|----|------|
| 1 | 실 Hermes 디스크 데이터 사용 | 0 | fixture 한정 (`tests/fixtures/memory_skill_migration/`), `~/.claude` / `hermes_state.py` / 실 disk read 0건 (docstring 1건 = Group H 분리 명시) |
| 2 | 실 provider SDK 호출 | 0 | grep `^(import\|from)\s+(openai\|anthropic\|google\.generativeai\|litellm\|ollama)` 결과 0건 (CI step 9 자동 강제) |
| 3 | 실 migration script 본 구현 | 0 | `tools/hermes_to_*.py` / `tools/migration_*.py` 0 파일 (CI step 9 자동 강제) |
| 4 | provider 간 cross-format migration 자동 진입 | 0 | `--feasibility-mode hermes-to-claude` 명시 플래그 한정, 자동 진입 0건 (사양 §2.1 명시) |
| 5 | Tier-2/3 catalog 확장 | 0 | `redaction-pattern-equivalence.md` / G4 design 변경 0건 (vendor catalog `_hermes_*` 1건 한정 — PoC 한정 토이) |
| 6 | G2 GP-6 최종 Implementation/Runtime PASS 선언 | 0 | 사양 §0 + §1.2 + 본 합의 §2.8 명시 — *feasibility 시제* 한정 |
| 7 | G2 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 |
| 8 | Hermes PMO 격상 선언 | 0 | 변경 0건 (4 게이트 합산표 변경 0건) |
| 9 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/provider-agnostic-memory-skill-design.md` + 다른 architecture 본문 변경 0건 (cross-reference 답습 한정) |

**합산 = 0/9 위반.**

### 2.5 사용자 명시 풀 3+1 승격 trigger 6 자기 검증 (0/6 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 실제 migration script 구현 필요 | 0 | 토이 매핑 1건 (Memory hermes→claude), 실 migration script 0 파일 |
| 2 | provider 간 cross-format migration 필요 | 0 | `--feasibility-mode` 명시 플래그 한정, 자동 진입 0건 |
| 3 | Memory/Skill schema 자체 변경 | 0 | G4 §4.2 11 필드 답습만, schema 변경 0건 |
| 4 | ADR-014 발행 trigger 발생 | 0 | Group H 영역 미진입, `docs/decisions/ADR-014-*.md` 작성 0건 |
| 5 | G4 / ADR-012 / ADR-011 원칙 충돌 | 0 | 답습만 (사양 §0 + §5 cross-reference) |
| 6 | Implementation PASS 기준 완화 위험 | 0 | *feasibility 시제* 한정, PASS 기준 완화 0건 (사양 §0 + §1.2 명시) |

**합산 = 0/6 발화 → Reviewer-only 단축 합의 적격.**

### 2.6 Group C 답습 충실도 (F-사전 결정 1순위)

| 영역 | Group C 답습 방식 | 신규 작성 |
|---|---|---|
| 11 필드 schema 검증 | `jsonl_hash_chain.parse_jsonl` + `validate_schema` import 직접 | 0 |
| Hash chain (Genesis + prev_hash + recompute + monotonicity) | `compute_genesis_hash` + `compute_entry_hash` + `validate_chain` import 직접 | 0 |
| Canonical JSON (RFC 8785 JCS Primary 1) | `canonical_json.to_canonical(mode=PRIMARY_1_ONLY)` import 직접 | 0 |
| Round-trip (T2 strict / T3 lossy / FAIL) | `jsonl_roundtrip.round_trip` + `RoundtripVerdict` + `diff_lost_fields` import 직접 | 0 |
| Ledger entry 자동 작성 (chain_violation_detected) | `build_violation_entry` import 직접 | 0 |
| Ledger entry 자동 작성 (roundtrip_pass/lossy/fail) | `build_roundtrip_entry` import 직접 | 0 |
| 토이 매핑 3 함수 (`hermes_to_canonical` / `canonical_to_claude` / `claude_to_canonical`) | — | ~25 줄 |
| Feasibility verdict 함수 (`feasibility_hermes_to_claude`) | — | ~30 줄 |
| Feasibility lossy ledger entry builder (`build_feasibility_lossy_entry`) | — | ~25 줄 |
| CLI 단일 dispatch (default mode + feasibility mode) | — | ~80 줄 (parse + 검증 분기) |

**리팩토링 0건 / 복제 0건 / 공유 모듈 import 직접** = F-사전 결정 1순위 충족 (사용자 명시 답습 — "Group C jsonl_roundtrip.py를 우선 공유 모듈로 재사용 가능한지 검토 → 리팩토링 범위가 커지면 복제 방식으로 최소 PoC 먼저 수행" 중 *재사용* 채택).

### 2.7 PASS / LOSSY / FAIL 기대값 일치 매트릭스

| 사양 §4 예상 | 실측 (§1.2) | 일치 |
|---|---|---|
| 검증 1: rc=0 + `roundtrip_pass` | rc=0 + `roundtrip_pass` | ✅ |
| 검증 2: rc=0 + `roundtrip_pass` | rc=0 + `roundtrip_pass` | ✅ |
| 검증 3: rc=1 + `roundtrip_lossy` + lost_fields ≥ 1 | rc=1 + `roundtrip_lossy` + lost_fields=2 | ✅ |
| 검증 4: rc=2 + `chain_violation_detected` (+ `roundtrip_fail` 영역) | rc=2 + `chain_violation_detected` + ledger entry 자동 (chain violation 우선 차단 → round-trip 미진입) | ✅ |

**합산 4/4 사양 일치** (CI workflow step 도 동일 logic 답습).

### 2.8 Artifact / summary.json 구성

CI workflow `Build summary.json` step (id 10) 산출:

```json
{
  "memory_pass": "PASS",
  "skill_pass": "PASS",
  "hermes_to_claude_lossy": "PASS",
  "chain_violation_fail": "PASS",
  "f_forbidden_violations": "0/9",
  "escalation_triggers": "0/6",
  "commit": "<sha>",
  "ref": "<ref>",
  "run_id": "<run_id>",
  "feasibility_scope": "G2 GP-6 *feasibility 시제* 한정 — G2 GP-6 / G2 / G4 전체 PASS 권한 0건"
}
```

Artifact `memory-skill-migration-feasibility-evidence` (retention 30일) 포함:
- `memory-pass.stdout` + `memory-pass.stderr`
- `skill-pass.stdout` + `skill-pass.stderr`
- `hermes-to-claude-lossy.stdout` + `hermes-to-claude-lossy.stderr`
- `chain-violation.stdout` + `chain-violation.stderr`
- `summary.json`

`$GITHUB_STEP_SUMMARY` 13 항목 (commit / ref / run / event / agent / ledger_layer / 4 step 결과 / 0/9 / 0/6 / shared_module_import / refactoring=0 / duplication=0 / PASS scope 한정).

### 2.9 책무 분리 — 별도 합의 영역 명시

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| 실 Hermes SQLite / Claude `~/.claude/memory.jsonl` / OpenAI export 형식 연동 | 사용자 명시 F-금지 #1~#2 | Group H (ADR-014 발행 후) |
| `hermes_to_openai` 변환 | F-범위 #4 = 1개 이상 (Memory hermes→claude 한정) | Group H 후속 |
| Skill 변환 feasibility | F-범위 #4 = Memory 한정 | Group H 후속 |
| Vendor-specific 필드 catalog 확장 (`_hermes_*` 1건 → Tier-1/2/3 catalog) | Tier-2/3 catalog 확장 금지 답습 | 별도 합의 |
| Round-trip nightly cron 설정 | feasibility 한정 — Group F 종료 후 별도 합의 | G2 GP-6 후속 PASS PoC |
| Migration BLOCK + manual + `migration_failed` event 검증 | ADR-012 §2.10 = 실 migration 영역 | Group H |
| Full Rewrite 5 Layer 방어 (history_rewrite) | Group C 후속 별도 영역 (사용자 명시 후보 7) | 별도 PoC |
| Memory boundary 4 금지 hook | Group G 영역 | 별도 합의 |
| Skill `forbidden_actions` runtime 강제 | Group G 영역 | 별도 합의 |

### 2.10 알려진 한계 (사양 §10 답습)

1. **토이 Claude format = identity** — 실 `~/.claude/memory.jsonl` 형식 미반영. 실 형식은 Group H 영역.
2. **`hermes_to_openai` 미구현** — F-범위 #4 = 1개 이상 충족 (Memory hermes→claude 한정).
3. **Skill 변환 feasibility 미구현** — F-범위 #4 = Memory 한정.
4. **Vendor-specific 필드 catalog 1건 (`_hermes_internal_id`)** — Tier-2/3 확장 금지 답습.
5. **Round-trip nightly cron 미설정** — feasibility 한정, 별도 합의 영역.
6. **chain violation fixture = `prev_hash_mismatch` 1건 한정** — Group C 의 4 패턴 (`hash_recalculation` / `genesis_mismatch` / `history_rewrite`) 은 Group C g4-hash-chain.yml 가 cover (본 PoC 는 Memory/Skill 시제 답습 한정).
7. **CI workflow `actions/upload-artifact@v4` 외부 의존** — Group A/B/C 답습 (별도 합의 미발화).

---

## 3. 풀 3+1 승격 trigger 6 자기 검증 (다시 명시)

§2.5 와 동일 — 6/6 미발화. **Reviewer-only 단축 합의 적격 (사용자 명시 답습)**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ Memory/Skill JSONL ledger 의 hash chain 정합 + canonical 층 round-trip + vendor-specific 필드 lossy 감지 *형식적* feasibility 1차 시제
- ✅ Group C 산출물 (`canonical_json` + `jsonl_hash_chain` + `jsonl_roundtrip`) 의 **재사용 가능성 실증** (리팩토링 0건 / 복제 0건)
- ✅ G4 §4.2 11 필드 schema 가 `type=memory` + `type=skill` 양쪽에 적용 가능 실증
- ✅ ADR-012 §2.9 3 ledger entry 형식 (`roundtrip_pass` / `roundtrip_lossy` / `roundtrip_fail`) 자동 작성 동작 실증
- ✅ Reviewer-only 단축 합의 답습 (Group A/B/C 답습)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G2 GP-6 최종 Implementation/Runtime PASS 선언
- ❌ G2 전체 Implementation/Runtime PASS 선언
- ❌ G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ 실 migration script 본 구현 (`hermes_to_claude.py` / `hermes_to_openai.py` 0 파일)
- ❌ 실 provider SDK 호출 (anthropic / openai / google.generativeai 0건)
- ❌ 실 Hermes 디스크 데이터 사용 (fixture 한정)
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ Memory/Skill schema 변경
- ❌ Tier-2/3 catalog 확장
- ❌ ADR-014 신규 발행 (Group H 영역)

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group F PoC = G2 GP-6 *feasibility 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/6 발화, F-금지 0/9 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 9/9 충족, F-범위 10/10 충족, 로컬 4/4 PASS, CI workflow 12 step 형식 검증 PASS).

### 5.2 추가 조건 (C-F-1 ~ C-F-6)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-F-1 | 본 PoC = G2 GP-6 *feasibility 시제* 한정 — G2 GP-6 / G2 / G4 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.4 #6~#7 명시 |
| C-F-2 | 토이 매핑 한정 — 실 migration script (`hermes_to_claude.py` / `hermes_to_openai.py`) 본 구현 = Group H 영역 (ADR-014 발행 trigger 후 별도 풀 3+1 합의) | 사양 §1.2 + §2.3 + 본 합의 §2.4 #3~#4 명시 |
| C-F-3 | Vendor-specific 필드 catalog `_hermes_internal_id` 1건 한정 — Tier-2/3 catalog 확장은 별도 합의 영역 (R-4 catalog 답습 분리) | 사양 §2.3 + §10 #4 + 본 합의 §2.10 #4 명시 |
| C-F-4 | Round-trip nightly cron 미설정 — feasibility 한정, 후속 G2 GP-6 PASS PoC 영역 | 사양 §10 #5 + 본 합의 §2.10 #5 명시 |
| C-F-5 | LOSSY fixture chain violation 1 패턴 (`prev_hash_mismatch`) 한정 — Group C g4-hash-chain.yml 가 4 패턴 cover (본 PoC 는 Memory/Skill 시제 답습 한정) | 본 합의 §2.10 #6 명시 |
| C-F-6 | Step 9 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §11 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (validator+CI / fixture / 사양·합의·gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습 — Group A/B/C 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group D (G2 GP-3 + GP-2 secret/redaction) — 단축 합의, R-4 catalog 답습
   - (b) Group A 3차 (URL/endpoint grep PoC, C-8 답습) — 풀 3+1
   - (c) Group F 후속 — Memory `hermes_to_openai` 변환 feasibility 추가 / Skill 변환 feasibility 추가 (별도 합의)
   - (d) Group C 후속 — `history_rewrite` Layer 5 PoC (ADR-012 §2.8)
   - (e) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+, Implementation/Runtime PASS PoC 완료 후 영역)
   - (f) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)
   - (g) cross-vendor LLM 의뢰 — Q1 C-B16 + P2 v3 §11.2 답습

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group F 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 0/6 발화, F-금지 0/9 위반, F-범위 10/10 + PASS 기준 9/9 + ADR-011 §2.1 5/5 충족, 로컬 4/4 PASS, CI workflow 12 step 형식 검증 PASS, Group C 산출물 import 직접 (리팩토링 0 / 복제 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C 답습). Step 9 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
