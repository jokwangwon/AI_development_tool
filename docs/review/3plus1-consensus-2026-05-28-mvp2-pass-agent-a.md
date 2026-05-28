# 3+1 합의 — Agent A (구현 분석가) — MVP-2 Layer 1+2+4 통합 PASS 발효 (e2)

> **검토 대상**: `docs/phase0/mvp2-layer-124-pass-activation-brief.md` (v1)
> **관점**: "실제로 동작하는가? evidence 가 실제인가?" — filesystem + CI 직접 inspection
> **작성**: 2026-05-28 (59번째 entry cycle, 신규 세션 #2)
> **방법**: 모든 evidence 주장을 `.venv/bin/python` 실행 + `gh run view` / `gh api` 직접 verify (다른 Agent/외부 LLM 응답 미참조)

---

## verdict: **APPROVE WITH CONDITIONS**

brief §2 evidence 매트릭스의 **모든 핵심 주장이 filesystem + CI 직접 inspection 으로 실증됨**. (β) cycle 의 "L-1 stdlib 시제 충족" over-claim 전례를 염두에 두고 비판적으로 검증했으나, 본 brief 의 evidence 는 시제 주장과 실측이 일치한다 (특히 가장 위험한 actual run ID 4개 + fixture 실재 + violation_type 단독 emit). over-claim 0건.

조건부인 이유: actual run ID 와 commit 매핑에서 **citation 부정확** 1건 발견 (BLOCKING — evidence 자체는 실재하나 commit 라벨이 틀림). 나머지는 권고/NOTE 수준.

---

## 직접 verify 한 evidence (실측 raw)

### Layer 1 — Hash Chain (E-PASS-1~4) ✅ 전원 실증

5개 fail fixture 를 `.venv/bin/python tools/jsonl_hash_chain.py` 로 직접 실행 (rfc8785+jcs 설치 확인됨):

| fixture | rc | violation_type (실측) | brief 주장 일치 |
|---------|----|--------------------|---------------|
| `genesis_mismatch.jsonl` | 1 | `genesis_mismatch` (1건) | ✅ |
| `hash_recalculation.jsonl` | 1 | `hash_recalculation` (1건) | ✅ |
| `prev_hash_mismatch.jsonl` | 1 | `prev_hash_mismatch` (1건) | ✅ |
| `missing_event_field.jsonl` | 1 | `schema_missing_field` (1건) | ✅ |
| `timestamp_monotonicity.jsonl` | 1 | `monotonicity_violation` (**1건 단독**) | ✅ |

PASS fixture 2개 (`minimal_chain.jsonl` + `roundtrip_t2_strict.jsonl`) = rc=0 실측 확인.

`tools/jsonl_hash_chain.py:67` `ViolationType` enum = 정확히 3 멤버 (`PREV_HASH_MISMATCH` / `HASH_RECALCULATION` / `GENESIS_MISMATCH`). **HISTORY_REWRITE 부재 확인** — 58 entry violation_type 정밀화 (Layer 1 제거) 주장이 코드 실재와 일치. brief §2.1 line 90 의 "3 Layer-1 type + schema" 표현이 정확 (55 entry brief 의 "4 violation_type" 보다 정정된 현행).

### E-PASS-10 (timestamp monotonicity, C-1 보강) ✅ 가장 비판적 — 전원 실증

- `tests/fixtures/jsonl_ledger/fail/timestamp_monotonicity.jsonl` **실재** (mtime 2026-05-28 15:04). 2 entry: entry 0 ts=`10:05:00`, entry 1 ts=`10:00:00` (ts 역행).
- 직접 실행 결과 = **`monotonicity_violation` 단독 emit** (genesis/prev_hash/hash mismatch 0건). brief 의 "valid chain + ts 역행 → monotonicity_violation 단독" 주장 정확.
- `validate_chain` (`jsonl_hash_chain.py:229`) 로직 직접 read: `cur_ts < prev_ts` → monotonicity_violation. chain violation 과 독립. `build_violation_entry:259` 가 monotonicity 를 `chain_violation_detected` 자동 작성에서 제외 — 설계 정합.
- TDD test 실재: `tests/tools/test_jsonl_hash_chain.py:62` `test_validate_chain_monotonicity_violation` — `assert set(chain_vios) == {"monotonicity_violation"}` (단독 emit 강제).
- `g4-hash-chain.yml:201` EXPECTED map 에 `[timestamp_monotonicity.jsonl]=monotonicity_violation` 추가됨 (5 violation_type cover). FAIL step 은 stderr (`2> chain_out.txt`) 를 grep — 직접 확인: violation 출력은 **stderr 로 emit** 되므로 grep 매칭 정상 (workflow 로직 sound).
- **actual run `26557936920` 직접 verify**: `gh run view 26557936920` → `conclusion: success`, `status: completed`, headSha=`4c480996cd...` (= commit `4c48099`), job `enforce` success. commit `4c48099` 의 fail 디렉터리에 `timestamp_monotonicity.jsonl` 포함 + workflow EXPECTED 5종 포함 확인 → **run 이 실제로 신규 fixture 를 실행했음이 입증됨** (단순 green 이 아니라 신규 fixture 경유 green).

### E-PASS-8 (Layer 4 — 3 G4 actual run) ✅ 전원 실증

`gh run view <id> --json conclusion,status,headSha` 직접:

| run ID | workflowName | conclusion | headSha |
|--------|-------------|-----------|---------|
| `26557460199` | G4 Hash Chain + JCS | **success** | `052e5833` |
| `26557460227` | G4 Rewrite Defense (Layer 2/3/4) | **success** | `052e5833` |
| `26557460197` | G4 History Anchor Verifier (Layer 5) | **success** | `052e5833` |

3개 전원 green 실증. 3개 모두 headSha=`052e5833` (= commit `052e583`, "58번째 entry 실 구현 violation_type 정밀화 TDD"). `.github/workflows/rewrite-defense.yml` + `history-anchor-verifier.yml` 실재 확인.

### E-PASS-7 (Layer 2b — branch protection) ✅ 정확 실증

`gh api .../branches/main/protection --jq '.required_status_checks.contexts'`:
```
["guard","verify","feasibility","scan","enforce","defense","validate","bypass-detect"]
```
= **정확히 8 contexts**, brief §2.3 line 108 과 글자 단위 일치. `allow_force_pushes=false` + `allow_deletions=false` 확인.

### E-PASS-5 (Layer 2a — DEFER) ✅ 확인

`git config --get receive.denyNonFastForwards` → rc=1 (미설정). DEFER 상태 정확. 57/58 비례 보안 결정 답습 framing 적절.

### E-PASS-6 (Layer 2 history fixtures) ✅ 실재

- `tests/fixtures/rewrite_defense/` fail = append_only(force_push + reorder) + line_regression(line_deletion + line_rewrite) + rewrite_command fail 4 추가 → brief 명시 4 + 추가.
- `tests/fixtures/history_anchor_verifier/fail/` = anchor full_rewrite + middle_deletion + substitution + tail_truncation (+ tampered) → brief §2.4 명시 4 anchor type 전원 실재.
- brief "FAIL fixtures 8" = append_only 2 + line_regression 2 + anchor 4 = 명시 8건 실재 확인.

### E-PASS-3/9 (canonical corpus) ✅

`find tests/canonical -type f | wc -l` = **72**, 8 카테고리 (array/escape/hash_stability/key_ordering/lossy/nested/number/unicode). brief "72 files / 8 카테고리" 정확.

### 로컬 pytest ✅

`.venv/bin/python -m pytest tests/tools/test_jsonl_hash_chain.py tests/jarvis -q` → **152 passed in 0.07s** (실패 0).

### (e1)/(e2) 혼동 검증 ✅ 혼동 0

55 entry brief (`mvp2-layer-124-pass-entry-brief.md`) = "통합 PASS **격상 진입 권한** 발효" (e1) 로 자기 framing + "PASS 발효 = 별도 sub-cycle" 명시 (line 13/59). 본 brief = (e2) PASS *발효* cycle 로 정확히 위치. §1 (e1)→(e2) 전이표 + §0.2 #1 = 발효 ≠ 기정사실 명시. **혼동 0건**.

### r2-canary 미트리거 — Layer 통합 PASS 영향 분석 ✅

`r2-canary.yml` paths 직접 read: `docker/r4-1-poc/**`, `docker/r2-poc/**`, canary docs, 자기 workflow file. → **ledger/brief 변경으로는 트리거 불가** (path 불일치). 따라서 ledger/brief commit 에서 r2-canary 미트리거는 정상 동작이며 Layer 1+2+4 *ledger* 검증 scope 와 무관. brief §4.3 의 "r2-canary = R-6/R-2 영역, 3 ledger workflow 가 Layer 4 충족" 분석 = **실측 뒷받침됨**. Layer 통합 PASS 에 실제 영향 0.

---

## BLOCKING

### R-A-1: 58 entry "실 구현" commit 라벨 부정확 (`6ebc634` → 실제 `052e583`)

- **근거**: brief §0.3 line 53 + §1.1 line 68 이 "58 실 구현 violation_type 정밀화 (`6ebc634`)" 로 표기. 그러나 `git log --oneline 6ebc634` = `"58번째 entry CI actual run 증거 기록"` (**docs(session) commit**). 실제 violation_type 정밀화 구현 commit 은 `052e583` (`"feat(jsonl_hash_chain): 58번째 entry — 실 구현 sub-cycle (1) violation_type 정밀화: HISTORY_REWRITE Layer 1 제거 (TDD)"`). 3 G4 actual run (`26557460199/227/197`) 의 headSha 도 `052e583` 이지 `6ebc634` 가 아니다.
- evidence 자체(코드/run)는 실재하나, "실 구현 = `6ebc634`" 라벨은 거짓 매핑. (β) cycle 의 시제 over-claim 교훈 답습 — citation 정확성도 evidence 정확성에 포함.
- **정정**: §0.3 line 53 / §1.1 line 68 / §10 line 244 의 "58 실 구현 (`6ebc634`)" → "58 실 구현 (`052e583`, CI 증거 기록 `6ebc634`)" 로 commit 구분 명시. 또는 "58 실 구현 sub-cycle (impl `052e583` + actual run 기록 `6ebc634`)".

---

## 권고

### N-A-1: §2.5 line 122 / §3 (b) line 145 "3 G4 actual run green" 의 headSha 명시 권장
- 3 run 모두 `052e583` 기반임을 evidence 매트릭스에 명시하면 추후 audit 시 commit↔run 추적성 향상 (E-PASS-8 의 "GitHub Actions run ID + verdict PASS" 답습 강화). 현재 run ID 만 있고 headSha 부재.

### N-A-2: E-PASS-8 "✅ 3/4" 표기 — 4번째(r2-canary)는 Layer 4 scope 가 아님 명시 일관화
- §2.5 line 122 가 "✅ 3/4" 로 표기하나, §4.3 분석상 r2-canary 는 R-6/R-2 영역으로 Layer 1+2+4 ledger 검증의 "4번째 항목"이 아니다. "3/4" 는 마치 1개 미달처럼 읽힐 수 있음. "3 ledger workflow green (r2-canary = scope 외)" 로 분모 framing 통일 권장. (실측상 Layer 4 충족엔 영향 0이므로 BLOCKING 아님.)

---

## NOTE

### NT-A-1: g4-hash-chain FAIL step 의 stderr grep 의존성 — 견고하나 fragile
- violation 출력이 stderr 로 가는 것에 workflow 가 의존 (`2> chain_out.txt` 후 grep). 현재 정상 동작 확인했으나, 추후 `jsonl_hash_chain.py` 출력 스트림 변경 시 silent regression 위험. 현 시점 PASS 발효엔 영향 0 (실측 green). 후속 hardening 후보.

### NT-A-2: 작업 트리 clean — 본 cycle 산출물만 untracked
- `git status --short` = brief + codex 응답 + Agent B/C 응답만 untracked. timestamp fixture 는 HEAD 에 tracked 확인 (`4c48099` 흡수 완료). C-1 보강이 "합의 전 미리 보강" 으로 이미 commit 된 상태 — brief §4.2 주장 정확.

### NT-A-3: E-PASS 1~15 enumeration 이 55 entry source 와 충실 일치
- 본 brief §2 + §3 의 E-PASS 라벨이 55 brief §5.2 (line 357~371) 와 매핑 일치. E-PASS-12 (Layer subsection 강제) + E-PASS-15 (R-S1 평가 한정) framing 답습 정확.

---

## 종합 (구현 분석가 판단)

(a)~(d) evidence 4조건은 Layer 1(완전) / Layer 2(2b operative + history actual run, 2a DEFER 문서화) / Layer 4(3 ledger workflow green + canonical BLOCK + timestamp C-1 보강) 전 영역에서 **filesystem + CI 직접 inspection 으로 실증됨**. 가장 위험한 주장(actual run ID 4개, fixture 단독 emit, 8 contexts)이 전부 실측 일치하며 over-claim 0건 — (β) cycle 의 시제 거짓 전례가 본 cycle 에 재발하지 않았다.

유일한 BLOCKING(R-A-1)은 evidence 실재성이 아니라 **commit 라벨 매핑 부정확**이다. evidence(run/code)는 모두 실재하므로 PASS 발효 자체를 막을 사유는 아니나, citation 정확성은 audit 추적성에 직결되므로 v1.1 흡수 전 정정 의무.

→ **APPROVE WITH CONDITIONS** (R-A-1 정정 후 (e2) PASS 발효 자격 충족, (e) = 풀 3+1 + 외부 LLM + 사용자 명시).

---

**Agent A 검토 끝.**
