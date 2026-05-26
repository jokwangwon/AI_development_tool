# G4 Rewrite Defense — Layer 2/3/4 통합 PoC — Group C 후속 후속 사양

> **PASS scope**: G4 *Layer 2/3/4 정적 검출 시제* 한정 — **Implementation Pending** (G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **상태**: DRAFT (2026-05-10, Group C 후속 후속 진입 — ADR-012 §2.8 *Full Rewrite 5 Layer* 中 Layer 2 + Layer 3 + Layer 4 영역 정적 검출 PoC)
> **답습 출처**:
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.8 (Full Rewrite 방어 5 Layer — Layer 2 git append-only / Layer 3 pre-commit hook / Layer 4 CI 회귀 검증) / §2.12 (Hermes 변조 차단 매트릭스)
> - `docs/architecture/provider-agnostic-memory-skill-design.md` §4.4.5 (Full Rewrite 방어 5 Layer — ADR-012 §2.8 답습)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e)
> - **Group C 산출물**: `tools/jsonl_hash_chain.py` (`parse_jsonl` import 직접 — L4 base/head ledger 파싱)
> - **Group C 후속 산출물**: `tools/history_anchor_verifier.py` (Layer 1 + Layer 5 답습 완결 cross-reference)
> - **Group A~G/A3/CF PoC 형식**: Group D + Group E + Group G + Group A 3차 + Group C 후속 사양 형식 직접 답습
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 5 풀 3+1 승격 trigger / 10 검증 / 9 금지 / 외부 의존 0건
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), ADR-012 §2.8 1인 동일 호스트 SPOF 한계 명시
> **답습 시제**: Group A 1차/2차/3차 + Group B + Group C + Group D + Group E + Group F + Group G + Group C 후속 PoC 사양 형식 직접 답습 (`g4-history-rewrite-layer5-anchor-poc.md` 답습)

---

## 0. 목적

본 PoC 는 ADR-012 §2.8 *Full Rewrite 방어 5 Layer* 中 **Layer 2 (Git append-only branch) + Layer 3 (pre-commit hook) + Layer 4 (CI 회귀 검증)** 의 *형식적 검출 layer* 첫 시제 — Layer 1 (Group C `validate_chain` 답습 완료) + Layer 5 (Group C 후속 anchor verifier 답습 완료) + 본 PoC = **ADR-012 §2.8 5 Layer 답습 5/5 완결**.

**범위 한정 핵심 결정** (사용자 명시 답습):

- **Layer 2 (Git append-only branch + denyNonFastForwards)** = 실 git config 변경 0건. *fixture 기반* commit history 비교 정적 검출 (force-push / reorder).
- **Layer 3 (pre-commit hook — git rebase/filter-branch/reset 감지)** = 실 hook 활성화 0건. *fixture 기반* git command log 정적 패턴 검출.
- **Layer 4 (CI 회귀 검증 — base branch 대비 JSONL line deletion / rewrite 감지)** = 실 CI base branch fetch 0건. *fixture 기반* base.jsonl ↔ head.jsonl 정적 line-by-line 비교.

본 PoC 는 **Layer 2/3/4 정적 검출 layer 한정** — runtime 강제 / 실 GitHub branch protection / 실 git hook 활성화 / 실 CI base branch fetch = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `ADR-012 §2.8` + `G4 §4.4.5` + Group C `parse_jsonl` 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g4-rewrite-defense-layer234-poc.md` | PoC 사양 + 답습 매핑 + 사용자 명시 10 검증 / 5 trigger / 9 금지 / 17 files (8 logical fixtures) / Layer 2/3/4 책임 매트릭스 |
| Validator | `tools/rewrite_defense_check.py` | 단일 도구 + 3 mode (append-only / rewrite-command / line-regression) + Group C `jsonl_hash_chain.parse_jsonl` import 직접 + commit history diff (L2) + dangerous command catalog 4 (L3) + line regression detector (L4) + violation reporter + `--list-defenses` self-check |
| L2 fixture × 6 files (3 logical) | `tests/fixtures/rewrite_defense/append_only/{pass, fail/force_push, fail/reorder}/{commit_history_before.txt, commit_history_after.txt}` | append-only PASS + force-push FAIL + reorder FAIL |
| L3 fixture × 5 files | `tests/fixtures/rewrite_defense/rewrite_command/{pass/git_command_log_safe.txt, fail/git_command_log_{rebase, filter_branch, reset_hard, push_force}.txt}` | safe PASS + 4 dangerous patterns FAIL |
| L4 fixture × 6 files (3 logical) | `tests/fixtures/rewrite_defense/line_regression/{pass, fail/line_deletion, fail/line_rewrite}/{base.jsonl, head.jsonl}` | append-only PASS + line deletion FAIL + in-place rewrite FAIL |
| CI workflow | `.github/workflows/rewrite-defense.yml` | 14 step (3 setup + rfc8785+jcs install + `--list-defenses` + 7 검증 + summary.json + artifact + Evidence summary). artifact path = `group-cff-logs/` (Group F 후속 답습) |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-reviewer-only.md` | PoC 검토 + 5 trigger 0/5 자기 검증 + evidence 매트릭스 통합 (Group D/E/G/A3/CF 답습) |

**합산 = 8 파일 + 17 fixture files** (Group D/E/G/A3/CF 답습 평균).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 9 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** — 본 PoC = *Layer 2/3/4 정적 검출 시제* 한정 |
| G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | **사용자 명시** |
| Hermes PMO 격상 선언 | **사용자 명시** |
| 실 branch protection 변경 | **사용자 명시** — Layer 2 운영 적용은 별도 합의 |
| 실 `denyNonFastForwards` 설정 변경 | **사용자 명시** — git config 변경 0건 |
| 실 signed commit 강제 | **사용자 명시** — Layer 5 multi-host MANDATORY 영역 |
| 실 git hook 활성화 (`.git/hooks/pre-commit`) | **사용자 명시** — Layer 3 운영 적용은 별도 합의 |
| 실 git command 실행 / 실 repo history rewrite 수행 | **사용자 명시** — fixture 한정, `subprocess.run(['git', ...])` 호출 0건 |
| 실 GitHub API 호출 / 실 CI base branch fetch | **사용자 명시** — `httpx` / `requests` / `gh api` 호출 0건 |
| ADR 본문 자동 갱신 | **사용자 명시** — cross-reference 답습 한정 |
| Layer 1 (hash chain) 통합 | Group C 영역 답습 완료 — 본 PoC 미중복 |
| Layer 5 (External anchor) 통합 | Group C 후속 영역 답습 완료 — 본 PoC 미중복 |
| Reflog 통합 | runtime 영역 — 별도 합의 |
| commit signature verification (GPG / Sigstore / cosign) | Layer 5 multi-host MANDATORY 영역 — 별도 합의 |

---

## 2. ADR-012 §2.8 5 Layer 책무 분담 매트릭스 (5/5 완결 시연)

| Layer | 차단 영역 | 답습 시점 | 도구 | 본 PoC |
|---|---|---|---|---|
| **Layer 1** | Single entry tampering / partial chain break (PREV_HASH_MISMATCH / HASH_RECALCULATION / HISTORY_REWRITE / GENESIS_MISMATCH) | Group C (commits `1e82346 → 5fd69af`) | `tools/jsonl_hash_chain.py` (`validate_chain`) | ❌ 미중복 (cross-reference 답습만) |
| **Layer 2** | History 재작성 (force-push / commit reorder / non-fast-forward) | **본 PoC** | **`tools/rewrite_defense_check.py` `--mode append-only`** | ✅ |
| **Layer 3** | Dangerous git command 사용 (rebase / filter-branch / reset --hard / push --force / commit --amend) | **본 PoC** | **`tools/rewrite_defense_check.py` `--mode rewrite-command`** | ✅ |
| **Layer 4** | Line deletion / in-place rewrite (CI 회귀 검증) | **본 PoC** | **`tools/rewrite_defense_check.py` `--mode line-regression`** | ✅ |
| **Layer 5** | External anchor mismatch (full rewrite / tail truncation / middle deletion / substitution) | Group C 후속 (commits `fd25cbe → cfc48ae`) | `tools/history_anchor_verifier.py` | ❌ 미중복 (cross-reference 답습만) |

**본 PoC 종료 후 = ADR-012 §2.8 5 Layer 답습 5/5 완결** (모든 layer 의 책무 정적 검출 시제 답습 완료).

### 2.1 Layer 보완 관계 (Group C / Group C 후속 답습)

| 시나리오 | L1 | L2 | L3 | L4 | L5 | 비고 |
|---|---|---|---|---|---|---|
| 단일 entry hash 변조 | ✅ | — | — | — | ✅ | L1 직접 검출 |
| Force-push (history 재작성) | ❌ | **✅** | (간접: rebase 등) | (간접: line diff) | ✅ | **L2 1차 검출 (본 PoC)** |
| `git rebase` / `filter-branch` / `reset --hard` | (사후) | (사후) | **✅** | (사후) | ✅ | **L3 1차 검출 (본 PoC) — 사전 차단** |
| Line deletion (entry 제거) | ❌ (chain 일관 시) | (간접) | (사용 명령 별) | **✅** | ✅ | **L4 1차 검출 (본 PoC)** |
| In-place rewrite (entry content 변조) | ✅ (hash 변조 시) | (간접) | (사용 명령 별) | **✅** | ✅ | L1 + L4 보완 |
| Substitution (다른 valid chain) | ❌ | ❌ | ❌ | (간접) | ✅ | L5 직접 검출 |
| Full rewrite (모든 entry 재작성) | ❌ | (force-push 흔적) | (`reset --hard` 흔적) | ✅ (line diff) | ✅ | **L4 + L5 보완** |

**Layer 2/3/4 의 *사전 차단* 책무 vs Layer 1/5 의 *사후 검출* 책무 분리** — ADR-012 §2.8 다층 방어 의도 직접 시연.

---

## 3. fixture 형식 (literal text, 실 git 환경 0건)

### 3.1 L2 fixture (commit history pair)

`commit_history_before.txt` / `commit_history_after.txt` 형식 — 각 line = `<short-sha> <message>` (literal text):

```
abc1234 feat: initial commit
def5678 feat: add jsonl_hash_chain
9876543 feat: add history_anchor_verifier
```

**시뮬레이션 한정** — 실 `git log --oneline` 호출 0건. 본 PoC 는 fixture text 비교만.

### 3.2 L3 fixture (git command log)

`git_command_log_*.txt` 형식 — 각 line = git 명령 (literal text):

```
git status
git add tools/example.py
git commit -m "feat: example"
git push origin main
```

**시뮬레이션 한정** — 실 shell 실행 0건. 본 PoC 는 fixture text 의 line-by-line 패턴 grep.

### 3.3 L4 fixture (base/head ledger pair)

`base.jsonl` / `head.jsonl` — Group C JSONL 11-field schema 답습 (Group C 후속 fixture 형식 답습):

```jsonl
{"type":"memory","scope":"project","id":"...","schema_version":"0.1","ts":"...","agent":"user","event":"memory_write","content":{...},"evidence_refs":[],"prev_hash":"...","hash":"..."}
```

**fake canary entry 한정** — 실 ledger 0건, fake content (`fake-key-N` / `fake value N`).

---

## 4. 도구 선택 근거 (stdlib 단독)

### 4.1 채택 (Group D/E/G/A3/CF 답습)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom validator (stdlib `re` + `dataclasses` 단독 + Group C import)** | **✅ 채택** | Group D/E/G/A3/CF 답습 (외부 의존 0건) + Group C `parse_jsonl` import 직접 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) `subprocess.run(['git', ...])` 호출 | ❌ 제외 | 사용자 명시 — 실 git command 호출 금지 (fixture 한정) |
| (C) `gitpython` / `pygit2` 라이브러리 | ❌ 제외 | runtime hook 영역 — 별도 합의 |
| (D) `httpx` / `requests` (GitHub API 호출) | ❌ 제외 | 사용자 명시 — 실 GitHub API 호출 금지 |

**채택 = (A) 단독**.

### 4.2 본 PoC 의 stdlib 답습 영역

| stdlib 모듈 | 책무 |
|------|------|
| `re` | dangerous command pattern catalog (rebase / filter-branch / reset --hard / push --force / amend) |
| `json` | JSONL parse (Group C `parse_jsonl` 답습) |
| `dataclasses` | `Violation` reporter (Group D/E/G/A3/CF 답습) |
| `argparse` | 3 mode CLI + `--list-defenses` self-check |
| `pathlib` | fixture file 경로 처리 |

**외부 의존 0건** (`requirements-dev.txt` 변경 0건).

---

## 5. Group C / Group C 후속 도구 재사용 매트릭스

### 5.1 import 직접 (리팩토링 0건)

```python
from jsonl_hash_chain import (  # Group C 답습 직접
    SUPPORTED_SCHEMA_VERSION,
    parse_jsonl,                # JSONL parser — L4 base/head ledger 파싱
)
```

### 5.2 답습 분포

| 영역 | Group C / Group C 후속 답습 | 신규 작성 |
|---|---|---|
| JSONL line-by-line parse | Group C `parse_jsonl` import 직접 | 0 |
| L2 commit history diff (literal text) | — (본 PoC 신규) | ~50줄 |
| L3 dangerous command catalog (4 patterns) | — (본 PoC 신규) | ~30줄 |
| L4 line regression detector (entry-level diff) | — (본 PoC 신규) | ~50줄 |
| 3 mode CLI dispatch | Group D/E/G/A3/CF 답습 | ~60줄 |
| violation reporter | Group A 1차 + Group D 답습 | ~25줄 |
| `--list-defenses` self-check | Group D `--list-patterns` + Group G `--list-boundaries` + CF `--list-attack-models` 답습 | ~30줄 |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건**. 신규 작성 ~245줄.

### 5.3 Group C 후속 cross-reference 답습 (book-keeping)

| 영역 | Group C 후속 답습 |
|---|---|
| Layer 5 anchor verifier 영역 | 본 PoC 미중복 (Layer 5 = Group C 후속 영역) |
| Layer 1 inadequacy demo | 본 PoC = Layer 2/3/4 inadequacy 보완 시연 (Group C / Group C 후속 영역에서 미커버) |
| 1인 동일 호스트 SPOF 한계 | 본 PoC 도 동일 한계 답습 (사양 §9 명시) |

---

## 6. Layer 2 (append-only) 검증 기준

### 6.1 검증 logic

`commit_history_before.txt` 의 모든 line 이 `commit_history_after.txt` 의 *strict prefix* 인지 검증.

| 시나리오 | before | after | 검출 |
|---|---|---|---|
| **PASS — append-only** | 5 commits | 5 + 2 commits (prefix 동일) | violations=0 |
| **FAIL — force-push** | 5 commits | 5 commits (commit 3 hash 변조) | non_fast_forward_detected — shared prefix hash mismatch |
| **FAIL — reorder** | `[A, B, C, D, E]` | `[A, C, B, D, E]` (B/C swap) | history_reorder_detected — line position 변경 |

### 6.2 violation type 2종

- `non_fast_forward_detected`: shared prefix line 의 commit hash 가 다름
- `history_reorder_detected`: shared prefix line 의 순서 변경

---

## 7. Layer 3 (rewrite-command) 검증 기준

### 7.1 dangerous command catalog (4 패턴)

| # | 패턴 | regex | 답습 출처 |
|---|---|---|---|
| 1 | `git rebase` | `\bgit\s+rebase\b` | ADR-012 §2.8 Layer 3 |
| 2 | `git filter-branch` | `\bgit\s+filter[- ]branch\b` | ADR-012 §2.8 Layer 3 |
| 3 | `git reset --hard` | `\bgit\s+reset\s+--hard\b` | ADR-012 §2.8 Layer 3 |
| 4 | `git push --force` / `git push -f` / `git commit --amend` | `\bgit\s+push\s+(?:--force\|-f)\b\|\bgit\s+commit\s+--amend\b` | ADR-012 §2.8 Layer 3 (확장) |

추가 영역 (별도 합의):
- `git filter-repo` (modern alternative — Tier-2 영역)
- `git reset --soft` / `--mixed` (덜 위험, 별도 합의)

### 7.2 검증 logic

`git_command_log_*.txt` 의 각 line 에 대해 4 패턴 grep — 1+ 매치 시 violation.

---

## 8. Layer 4 (line-regression) 검증 기준

### 8.1 검증 logic

`base.jsonl` 과 `head.jsonl` 을 entry-level 로 비교:

1. Group C `parse_jsonl` 로 base/head 모두 parse
2. `head[0:len(base)]` 의 entry 가 `base` 와 entry-by-entry 동일한지 확인
3. `head` 는 `base` 보다 길거나 같아야 (truncation 차단)
4. 동일 index 의 entry 의 모든 필드가 동일해야 (in-place rewrite 차단)

### 8.2 violation type 2종

- `line_deletion_detected`: head length < base length 또는 head[0:len(base)] entry 누락
- `line_rewrite_detected`: head[i] != base[i] (any field — id / hash / content / etc.)

| 시나리오 | base | head | 검출 |
|---|---|---|---|
| **PASS — append-only** | 5 entries | 5 + 2 entries (prefix 동일) | violations=0 |
| **FAIL — line deletion** | 5 entries | 4 entries (entry[2] 제거 후 chain 재계산) | line_deletion_detected (length mismatch) |
| **FAIL — in-place rewrite** | 5 entries | 5 entries (entry[2] content 변조) | line_rewrite_detected (entry[2] field 변경) |

---

## 9. fixture 17 files / 8 logical 사양

### 9.1 L2 (append_only) — 6 files / 3 logical

```
append_only/pass/{commit_history_before.txt, commit_history_after.txt}
append_only/fail/force_push/{commit_history_before.txt, commit_history_after.txt}
append_only/fail/reorder/{commit_history_before.txt, commit_history_after.txt}
```

### 9.2 L3 (rewrite_command) — 5 files

```
rewrite_command/pass/git_command_log_safe.txt
rewrite_command/fail/git_command_log_rebase.txt
rewrite_command/fail/git_command_log_filter_branch.txt
rewrite_command/fail/git_command_log_reset_hard.txt
rewrite_command/fail/git_command_log_push_force.txt
```

### 9.3 L4 (line_regression) — 6 files / 3 logical

```
line_regression/pass/{base.jsonl, head.jsonl}
line_regression/fail/line_deletion/{base.jsonl, head.jsonl}
line_regression/fail/line_rewrite/{base.jsonl, head.jsonl}
```

**합산 = 17 files / 8 logical fixtures** (Group D/E/G/A3/CF 답습 평균 — 9-10 logical fixture 와 비교 시 +/- 1).

### 9.4 fake canary 의무

- L2/L3 fixture: literal text, 실 git command/repo 0건
- L4 fixture: Group C 후속 답습 형식 (fake canary entry — `fake-key-N` / `fake value N`)
- 실 GitHub API 호출 0건 + 실 production data 0건

---

## 10. 검증 매트릭스 (사용자 명시 10 검증 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 결과 |
|---|------|------|------|---------|------|
| 1 | L2 PASS — append-only commit history | `append_only/pass/` | `--mode append-only append_only/pass/` | 0 | violations=0 (strict prefix extension) |
| 2 | L2 FAIL — force-push | `append_only/fail/force_push/` | `--mode append-only append_only/fail/force_push/` | 1 | non_fast_forward_detected |
| 3 | L2 FAIL — reorder | `append_only/fail/reorder/` | `--mode append-only append_only/fail/reorder/` | 1 | history_reorder_detected |
| 4 | L3 PASS — safe commands | `rewrite_command/pass/` | `--mode rewrite-command rewrite_command/pass/` | 0 | violations=0 |
| 5 | L3 FAIL — dangerous commands | `rewrite_command/fail/` | `--mode rewrite-command rewrite_command/fail/` | 1 | ≥4 violations + 4 patterns cover (rebase + filter-branch + reset-hard + push-force/amend) |
| 6 | L4 PASS — head extends base | `line_regression/pass/` | `--mode line-regression line_regression/pass/` | 0 | violations=0 |
| 7 | L4 FAIL — line deletion | `line_regression/fail/line_deletion/` | `--mode line-regression line_regression/fail/line_deletion/` | 1 | line_deletion_detected |
| 8 | L4 FAIL — in-place rewrite | `line_regression/fail/line_rewrite/` | `--mode line-regression line_regression/fail/line_rewrite/` | 1 | line_rewrite_detected |
| 9 | `--list-defenses` self-check | — | `--list-defenses` | 0 | 3 layers + 4 dangerous commands + 3 line regression types + 5 layer 완결 flag |
| 10 | F-금지 grep | scanner + fixture grep | grep | 0 | 실 git command 호출 / 실 repo 변조 / 실 GitHub API 호출 / production data 0건 |

**합산 10 검증** (3 layers × PASS+FAIL + list-defenses + F-금지 grep).

---

## 11. PASS 기준 자기 검증 매트릭스

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | L2 PASS — append-only | rc=0 + violations=0 |
| 2~3 | L2 FAIL × 2 (force-push + reorder) | rc=1 + 각 violation type 검출 |
| 4 | L3 PASS — safe commands | rc=0 + violations=0 |
| 5 | L3 FAIL — dangerous commands | rc=1 + ≥4 + 4 patterns cover |
| 6 | L4 PASS — head extends base | rc=0 + violations=0 |
| 7~8 | L4 FAIL × 2 (line deletion + in-place rewrite) | rc=1 + 각 violation type 검출 |
| 9 | `--list-defenses` | 3 layers + 4 commands + 3 regression types + 5_layer_compliant=True |
| 10 | F-금지 grep | 0건 (실 git command / 실 GitHub API / production data 부재) |

**합산 10/10 충족 적격**.

---

## 12. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | 실 `git config receive.denyNonFastForwards true` / branch protection rule 미진입 | Layer 2 운영 적용 = 별도 합의 (사용자 명시 #4~#5) | 별도 합의 |
| 2 | 실 `.git/hooks/pre-commit` 활성화 미진입 | Layer 3 운영 적용 = 별도 합의 (사용자 명시 #7) | 별도 합의 |
| 3 | 실 GitHub Actions base branch fetch / CI 통합 미진입 | Layer 4 운영 적용 = 별도 합의 | 별도 합의 |
| 4 | 실 git command 실행 / 실 repo history rewrite 수행 미진입 | 사용자 명시 #6 — fixture 한정 | 별도 합의 |
| 5 | 실 GitHub API 호출 미진입 | 사용자 명시 #8 — `httpx` / `requests` / `gh api` 0건 | 별도 합의 |
| 6 | `git filter-repo` (modern alternative) catalog 미진입 | Tier-2 영역 — 별도 합의 | 별도 합의 |
| 7 | `git reset --soft` / `--mixed` (덜 위험) 미진입 | Tier-2 영역 — 별도 합의 | 별도 합의 |
| 8 | Reflog 통합 미진입 | runtime 영역 | 별도 합의 |
| 9 | Commit signature verification (GPG / Sigstore / cosign) 미진입 | Layer 5 multi-host MANDATORY 영역 | Group C 후속 분리 |
| 10 | **1인 동일 호스트 SPOF 한계** (ADR-012 §2.8 답습) — 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖 | multi-host 전환 시 Layer 2/3/4 + 5 모두 MANDATORY 발동 | 별도 합의 |
| 11 | Markdown 본문 자기 검출 (Group D/E/G/A3/CF 답습 패턴) | CI 는 `tests/fixtures/rewrite_defense/` 한정 scan 으로 회피 | Group B PoC 사양 §2.8 #1 답습 |

---

## 13. CI workflow 설계

### 13.1 14 step 구조 (Group D/E/G/A3/CF 답습)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Install Group C deps (rfc8785 + jcs) | Group C `parse_jsonl` 의존성 (canonical_json) |
| 4 | Prepare log directory | `mkdir -p group-cff-logs` (Group F 후속 답습 — leading dot 미사용) |
| 5 | `--list-defenses` self-check | rc=0 + 3 layers + 4 commands + 3 regression types + 5_layer_compliant=True grep |
| 6 | L2 PASS — append-only commit history | rc=0 + violations=0 grep |
| 7 | L2 FAIL — force-push + reorder | rc=1 + non_fast_forward_detected + history_reorder_detected grep |
| 8 | L3 PASS — safe commands | rc=0 + violations=0 grep |
| 9 | L3 FAIL — dangerous commands | rc=1 + 4 patterns cover (rebase + filter-branch + reset-hard + push-force/amend) grep |
| 10 | L4 PASS — head extends base | rc=0 + violations=0 grep |
| 11 | L4 FAIL — line deletion + in-place rewrite | rc=1 + line_deletion_detected + line_rewrite_detected grep |
| 12 | F-금지 자기 검증 (Layer 1 grep) | 실 git command 호출 / 실 repo 변조 / 실 GitHub API 호출 / production data 0건 grep |
| 13 | Build summary.json + Upload artifact | `actions/upload-artifact@v4` `rewrite-defense-evidence` retention 30일 |
| 14 | Evidence summary | `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-cff-logs/`** (Group F 후속 답습 — leading dot 미사용).

### 13.2 paths trigger

```yaml
paths:
  - tools/rewrite_defense_check.py
  - tools/jsonl_hash_chain.py        # Group C 모듈 변경 시 trigger
  - tests/fixtures/rewrite_defense/**
  - .github/workflows/rewrite-defense.yml
```

---

## 14. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 5 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | 실제 branch protection 정책 변경 필요 | ❌ 미발화 | fixture 한정, 실 git config 변경 0건 |
| 2 | signed commit 정책 실 도입 필요 | ❌ 미발화 | Layer 5 영역 (Group C 후속) |
| 3 | external anchor mandatory 격상 필요 | ❌ 미발화 | Group C 후속 영역 |
| 4 | ADR-012 hash chain 구조 변경 필요 | ❌ 미발화 | Group C 11-field schema 답습만 |
| 5 | 기존 Group C / Layer 5 결과와 충돌 | ❌ 미발화 | cross-reference 답습 한정 |

**합산 0/5 발화** → **Reviewer-only 단축 합의 적격**.

---

## 15. Evidence 형식 (5종 — Group A/B/C/D/E/F/G/A3/CF 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g4-rewrite-defense-...`) | 본 문서 |
| JSONL ledger entry | summary.json (단순화 — Group D/E/G/A3/CF 답습) | summary.json 16 항목 |
| 격리 검증 | fixture 한정 + 외부 의존 0건 + 실 git command 호출 0건 | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `rewrite-defense.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g4-rewrite-defense-layer234-...`) | 본 PoC 산출물 #8 |

---

## 16. 본 PoC 의 *evidence 가치* (5 Layer 완결)

본 PoC 가 답하는 핵심 (사용자 명시 §0 답습):

> "Layer 2/3/4 가 full rewrite 방어에 어떤 역할을 하는지 fixture와 CI 기반으로 검증한다." + "Layer 1/5와의 보완 관계 명시."

### 16.1 본 PoC 가 *발생* 시키는 것

- ✅ ADR-012 §2.8 *Layer 2 + Layer 3 + Layer 4* 영역의 *형식적 검출 layer* 운영 적용 첫 시제
- ✅ **ADR-012 §2.8 5 Layer 답습 5/5 완결** — Layer 1 (Group C) + Layer 2/3/4 (본 PoC) + Layer 5 (Group C 후속)
- ✅ Layer 2/3/4 의 *사전 차단* 책무 vs Layer 1/5 의 *사후 검출* 책무 분리 시연
- ✅ Custom validator 단독 채택 (외부 의존 0건 + 실 git command 호출 0건 + 실 GitHub API 호출 0건) 답습 검증
- ✅ Group C 산출물 (`jsonl_hash_chain.parse_jsonl`) import 직접 답습
- ✅ Group F 후속 artifact path 답습 (`group-cff-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A~G/A3/CF 답습)

### 16.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ 실 branch protection 변경 / 실 denyNonFastForwards 설정 변경
- ❌ 실 signed commit 강제
- ❌ 실 git hook 활성화
- ❌ 실 git command 실행 / 실 repo history rewrite 수행
- ❌ 실 GitHub API 호출
- ❌ Layer 1 (Group C 영역) / Layer 5 (Group C 후속 영역) 중복 통합

---

## 17. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group C 후속 후속 진입 사양 — ADR-012 §2.8 *Layer 2 + Layer 3 + Layer 4* 영역 정적 검출 PoC. 사용자 명시 10 검증 / 5 trigger / 9 금지 / 17 fixture files / 8 logical / 3 mode / stdlib 단독 채택. Group A 1차/2차/3차 + Group B + Group C + Group D + Group E + Group F + Group G + Group C 후속 사양 형식 직접 답습. ADR-012 §2.8 + §2.12 + G4 §4.4.5 + Group C `parse_jsonl` 답습 (변경 0건). Reviewer-only 단축 합의 적격 (풀 3+1 trigger 0/5 발화). artifact path `group-cff-logs/` (Group F 후속 답습, leading dot 미사용). **본 PoC 종료 후 = ADR-012 §2.8 5 Layer 답습 5/5 완결** (Layer 1 Group C + Layer 2/3/4 본 PoC + Layer 5 Group C 후속). |
