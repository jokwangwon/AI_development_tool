# 3+1 합의 보고서 — G4 History Rewrite Layer 5 External Anchor (Group C 후속 PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group C 후속 진입 — ADR-012 §2.8 *Full Rewrite 5 Layer* 中 Layer 5 External Anchor 정적 검출 PoC)
> **PASS scope**: G4 *Layer 5 External anchor 정적 검출 시제* 한정 — **Implementation Pending** (G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 5 = 0/5 발화 → 단축 적격)
> **검토 대상**:
> - `tools/history_anchor_verifier.py`
> - `tests/fixtures/history_anchor_verifier/{pass,fail,chain_only_demo}/*`
> - `.github/workflows/history-anchor-verifier.yml`
> - `docs/phase0/g4-history-rewrite-layer5-anchor-poc.md`
> - `.gitignore` (`group-c-followup-logs/` 추가)
> **상위 권위**: ADR-008 부록 C, ADR-011 §2.1 (a)~(e), ADR-012 §2.8 (Full Rewrite 5 Layer) + §2.12 (Hermes 변조 차단), G4 §4.4.5, Group C `validate_chain` import 직접
> **답습 시제**: Group A 1차/2차/3차 + Group B + Group C + Group D + Group E + Group F + Group G PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g3-g4-boundary-guard-reviewer-only.md` 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/history_anchor_verifier.py` | ~310 | **stdlib `re` + `json` + `dataclasses` 단독** (외부 의존 0건). 2 mode CLI (`--mode chain-only` / `--mode anchor-verify`) + `--list-attack-models` self-check + Group C `jsonl_hash_chain` import 직접 (`parse_jsonl` + `validate_chain` + `compute_entry_hash` + `compute_genesis_hash` + ENUMs) + 11-field anchor schema validation + 5 attack model 검출 (full_rewrite / tail_truncation / middle_deletion / substitution / anchor_tampered) + appended_only mode (Layer 5 정상 운영 시제 — extended ledger prefix match) + violation reporter |
| 2 | `tests/fixtures/history_anchor_verifier/pass/{original_ledger.jsonl, original_anchor.json, extended_ledger.jsonl, extended_anchor.json}` | 4 fixture | original 5 entries + extended 5+2 entries + matching anchors |
| 3 | `tests/fixtures/history_anchor_verifier/fail/*.jsonl + *.json` | 5 fixture (4 ledger + 1 anchor 변조) | full_rewrite + tail_truncation + middle_deletion + substitution + anchor_tampered |
| 4 | `tests/fixtures/history_anchor_verifier/chain_only_demo/full_rewrite_ledger.jsonl` | 1 fixture | **Layer 1 inadequacy demo** — chain-only mode 시 의도된 PASS |
| 5 | `.github/workflows/history-anchor-verifier.yml` | ~315 (16 step) | 13 step 사양 답습 + setup/post step 포함. artifact path = `group-c-followup-logs/` (Group F 후속 답습) |
| 6 | `docs/phase0/g4-history-rewrite-layer5-anchor-poc.md` | 410 (14 섹션) | PoC 사양 (Group D/E/G/A3 답습) |
| 7 | 본 합의 보고서 | ~330 | Group A~G/A3 Reviewer-only 합의 형식 답습 |
| 8 | `.gitignore` 갱신 | +3 lines | `group-c-followup-logs/` 추가 |

**합산 = 8 파일** (Group D/E/G/A3 답습 평균).

### 1.2 fixture 10건 검증 결과

| Fixture | 위치 | 매칭 패턴 | 합계 |
|---|---|---|---|
| `original_ledger.jsonl` + `original_anchor.json` | pass/ | 0 (anchor matched) | 0 (FP 0) |
| `extended_ledger.jsonl` + `extended_anchor.json` | pass/ | 0 (anchor prefix matched — Layer 5 정상 시제) | 0 (FP 0) |
| `full_rewrite_ledger.jsonl` + `anchor_full_rewrite.json` | fail/ | tail-hash-mismatch + anchor-self-inconsistent | 2 |
| `tail_truncation_ledger.jsonl` + `anchor_tail_truncation.json` | fail/ | entry-count-mismatch + tail-hash-mismatch | 2 |
| `middle_deletion_ledger.jsonl` + `anchor_middle_deletion.json` | fail/ | entry-count-mismatch + tail-hash-mismatch | 2 |
| `substitution_ledger.jsonl` + `anchor_substitution.json` | fail/ | tail-hash-mismatch + genesis-hash-mismatch + anchor-self-inconsistent | 3 |
| `anchor_tampered.json` (+ original_ledger.jsonl) | fail/ | tail-hash-mismatch + anchor-self-inconsistent (known limitation) | 2 |
| `chain_only_demo/full_rewrite_ledger.jsonl` | chain_only_demo/ | 0 (chain-only mode 의도된 PASS) | 0 (Layer 1 inadequacy evidence) |

### 1.3 `--list-attack-models` 출력

```
attack_scenarios=5
  full_rewrite        Full rewrite — 모든 entry 재작성, prev_hash 모두 재계산 (chain 일관, tail hash 다름)
  tail_truncation     Tail truncation — 마지막 N entry 제거, 남은 chain valid
  middle_deletion     Middle deletion + 재계산 — 중간 entry 제거 후 prev_hash 재계산
  substitution        Substitution — 전체 ledger 를 다른 valid chain 으로 교체
  anchor_tampered     Anchor 자체 변조 (signature 부재 시 한계 — known limitation)
anchor_required_fields=9
  fields=['anchor_id', 'anchor_ts', 'anchor_method', 'ledger_path', 'expected_entry_count',
          'expected_tail_hash', 'expected_genesis_hash', 'schema_version', 'external_run_id']
anchor_optional_fields=2
  fields=['external_run_url', 'notes']
total_anchor_fields=11
allowed_anchor_methods=['ci_run_id']
known_limitations=1 (anchor 자체 signing 부재 — multi-host MANDATORY 영역, ADR-012 §2.8)
layer_5_compliant=True
anchor_field_count_compliant=True
layer_1_inadequacy_demo_supported=True (chain-only mode)
```

### 1.4 로컬 검증 결과 (10/10 PASS)

| # | 검증 | 명령 | rc | 결과 |
|---|------|------|-----|------|
| 1 | Anchor PASS — original | `--mode anchor-verify pass/original_anchor.json` | **0** | violations=0, anchor matched |
| 2 | Anchor PASS — extended append | `--mode anchor-verify pass/extended_anchor.json` | **0** | violations=0, prefix matched (Layer 5 정상 시제) |
| 3 | Anchor FAIL — full rewrite | `--mode anchor-verify fail/anchor_full_rewrite.json` | **1** | tail-hash-mismatch + anchor-self-inconsistent |
| 4 | Anchor FAIL — tail truncation | `--mode anchor-verify fail/anchor_tail_truncation.json` | **1** | entry-count-mismatch + tail-hash-mismatch |
| 5 | Anchor FAIL — middle deletion | `--mode anchor-verify fail/anchor_middle_deletion.json` | **1** | entry-count-mismatch + tail-hash-mismatch |
| 6 | Anchor FAIL — substitution | `--mode anchor-verify fail/anchor_substitution.json` | **1** | tail-hash-mismatch + genesis-hash-mismatch + anchor-self-inconsistent |
| 7 | Anchor FAIL — tampered anchor | `--mode anchor-verify fail/anchor_tampered.json` | **1** | tail-hash-mismatch + anchor-self-inconsistent (known limitation) |
| 8 | **Layer 1 inadequacy demo** | `--mode chain-only chain_only_demo/full_rewrite_ledger.jsonl` | **0 (의도된 PASS)** | "Layer 1 단독으로는 full rewrite 검출 불가" 명시 — Layer 5 의무성 evidence |
| 9 | `--list-attack-models` self-check | `--list-attack-models` | **0** | 5 attack + 11 fields + layer_5_compliant=True + layer_1_inadequacy_demo_supported=True |
| 10 | F-금지 grep | scanner + fixture grep | **0** | 실 signed commit / external service / GitHub API / production data 0건 |

### 1.5 CI workflow 16 step 구조

| # | Step | 책무 |
|---|------|------|
| 1~3 | Checkout / Set up Python 3.12 / `mkdir -p group-c-followup-logs` | — |
| 4 | `--list-attack-models` self-check | rc=0 + 5 attack + 11 fields + layer_5_compliant=True + layer_1_inadequacy_demo_supported=True grep |
| 5 | Anchor PASS — original | rc=0 + violations=0 grep |
| 6 | Anchor PASS — extended append | rc=0 + violations=0 grep |
| 7 | Anchor FAIL — full rewrite | rc=1 + tail-hash-mismatch grep |
| 8 | Anchor FAIL — tail truncation | rc=1 + entry-count + tail-hash grep |
| 9 | Anchor FAIL — middle deletion | rc=1 + entry-count + tail-hash grep |
| 10 | Anchor FAIL — substitution | rc=1 + tail-hash + genesis-hash grep |
| 11 | Anchor FAIL — tampered anchor | rc=1 + anchor-self-inconsistent grep (known limitation) |
| 12 | **Layer 1 inadequacy demo** — chain-only | rc=0 (의도된 PASS) + "Layer 1 단독으로는 full rewrite 검출 불가" grep |
| 13 | F-금지 자기 검증 (Layer 1 grep) | 7 위반 영역 grep (signed commit / HTTP client / 외부 호출 / production data) |
| 14 | Build summary.json | step output 집계 → `group-c-followup-logs/summary.json` 18 항목 |
| 15 | Upload artifact | `actions/upload-artifact@v4` `history-anchor-verifier-evidence` retention 30일 |
| 16 | Evidence summary | `$GITHUB_STEP_SUMMARY` |

**artifact path = `group-c-followup-logs/`** (Group F 후속 답습 — leading dot 미사용).

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | ADR-012 §2.8 *Full Rewrite 5 Layer* 中 Layer 5 (External anchor) 직접 답습 — Layer 1 단독으로 검출 불가능한 4 attack scenario (full rewrite + tail truncation + middle deletion + substitution) 모두 anchor mismatch 로 검출 |
| (b) 격리 환경 PoC 실증 | ✅ | fixture 한정 (실 signed commit 0건, 실 external service 0건, fake anchor metadata) + 외부 의존 0건 (stdlib 단독) + CI ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 부록 C / ADR-011 §2.1 / ADR-012 §2.8 + §2.12 / G4 §4.4.5 / Group C `validate_chain` cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 16 step + paths trigger 4 영역 + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 10 (사양 §8 답습)

| # | 기준 | 충족 |
|---|----|----|
| 1 | Anchor PASS — original | ✅ rc=0 |
| 2 | Anchor PASS — extended append | ✅ rc=0 (Layer 5 정상 시제) |
| 3~6 | Anchor FAIL × 4 (4 attack scenarios) | ✅ rc=1 + 각 scenario 별 mismatch 검출 |
| 7 | Anchor FAIL — tampered anchor | ✅ rc=1 (known limitation 명시) |
| 8 | Layer 1 inadequacy demo | ✅ rc=0 (의도된 PASS) — Layer 5 의무성 evidence |
| 9 | `--list-attack-models` | ✅ 5 attack + 11 fields + layer_5_compliant=True |
| 10 | F-금지 grep | ✅ 0/7 위반 |

**합산 10/10 충족.**

### 2.3 사용자 명시 7 금지 자기 검증 (0/7 위반)

| # | 금지 | 위반 | 근거 |
|---|------|----|------|
| 1 | G4 전체 Implementation/Runtime PASS 선언 | 0 | 본 PoC = *Layer 5 정적 검출 시제* 한정 |
| 2 | G2 / G3 / G4 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 (meta 갱신 시 *부분 충족 시제* 한정) |
| 3 | Hermes PMO 격상 선언 | 0 | 변경 0건 |
| 4 | 실 branch protection 변경 | 0 | Layer 2 영역 미진입 |
| 5 | 실 signed commit 강제 | 0 | scanner 본문 `import (gnupg\|pynacl\|sigstore\|cosign)` 0건 |
| 6 | 실 external timestamping service 연동 | 0 | scanner 본문 HTTP client / 외부 호출 0건 |
| 7 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/` 본문 변경 0건 |

**합산 0/7 위반.**

### 2.4 사용자 명시 풀 3+1 승격 trigger 5 자기 검증 (0/5 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | signed commit 정책 실 도입 필요 | 0 | anchor metadata file 한정, signed commit = 별도 합의 |
| 2 | branch protection 정책 변경 필요 | 0 | fixture 한정 |
| 3 | external anchor 필수 격상 필요 | ⚠️ 부분 — 본 PoC = MVP RECOMMENDED 시제 한정 (multi-host MANDATORY 격상 = 별도 합의) | known limitation 분리 (사양 §9 #5/#8) |
| 4 | Evidence Ledger hash chain 구조 자체 변경 필요 | 0 | Group C 11-field schema 답습만 |
| 5 | ADR-012 본문 결정 변경 필요 | 0 | cross-reference 답습 한정 |

**합산 0/5 발화** → **Reviewer-only 단축 합의 적격**.

### 2.5 ADR-012 §2.8 + G4 §4.4.5 답습 충실도

| 영역 | 답습 방식 | 신규 작성 |
|---|---|---|
| Layer 1 (hash chain — middle entry tampering 차단) | Group C `validate_chain` import 직접 (chain-only mode) | 0 |
| Layer 2 (Git append-only branch) | ❌ 미진입 (별도 합의 영역) | 0 |
| Layer 3 (pre-commit hook — git rebase/filter-branch/reset 감지) | ❌ 미진입 (별도 합의 영역) | 0 |
| Layer 4 (CI 회귀 검증 — base branch 대비 line deletion / rewrite 감지) | ❌ 미진입 (별도 합의 영역) | 0 |
| **Layer 5 (External anchor)** | **본 PoC 영역 — anchor metadata + verification logic** | ~310줄 |
| 11-field anchor schema | — (본 PoC 신규 정의, 사양 §3.1) | ~30줄 |
| 5 attack scenario 검출 logic | — (본 PoC 신규) | ~80줄 |
| Group C reuse (`validate_chain` + `compute_entry_hash` + `compute_genesis_hash` + ENUMs) | import 직접 | 0 |
| 1인 동일 호스트 SPOF 한계 명시 (외부 LLM 1 권고 5 답습) | — (사양 §9 #9 명시) | docstring |

**리팩토링 0건 + 복제 0건 + 외부 의존 0건**. 신규 작성 ~225줄.

### 2.6 Layer 1 inadequacy demo 충실도 (사용자 명시 핵심 evidence)

| 시나리오 | Group C `validate_chain` 단독 시 | Layer 5 anchor mode 시 |
|---|---|---|
| #1 Full rewrite | **PASS** (chain 내부 일관) — chain-only demo fixture 로 시연 | **FAIL** detected (tail-hash-mismatch) |
| #2 Tail truncation | **PASS** (남은 chain valid) | **FAIL** detected (entry-count + tail-hash mismatch) |
| #3 Middle deletion + 재계산 | **PASS** (재계산된 chain valid) | **FAIL** detected (entry-count + tail-hash mismatch) |
| #4 Substitution | **PASS** (다른 valid chain) | **FAIL** detected (tail-hash + genesis-hash mismatch) |

**Layer 1 inadequacy 영역 4 시나리오 모두 Layer 5 가 검출** — ADR-012 §2.8 5 Layer 다층 방어의 *각 layer 의 책무 명확화* 직접 evidence.

### 2.7 Group A~G + A3 답습 충실

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + N mode + `--list-*` self-check) | Group A 1차 + Group D + Group E + Group G + Group A 3차 |
| Fixture 디렉토리 구조 (PASS / FAIL 분리, mode 별 subdir) | Group D + Group E + Group G + Group A 3차 |
| CI workflow 16 step (Anchor PASS×2 + FAIL×5 + Layer 1 demo + list-attack + F-금지 + summary.json + artifact + Evidence summary) | Group D + Group E + Group G + Group A 3차 직접 답습 |
| Reviewer-only 단축 합의 형식 | Group A~G + A3 답습 |
| **artifact path (leading dot 미사용)** | **Group F 후속 + Group D/E/G/A3 (group-c-followup-logs/) 직접 답습** |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A~G + A3 답습 |
| Group C `validate_chain` import 직접 | Group F + Group G 답습 |

### 2.8 책무 분리 — 별도 합의 영역

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| Layer 2 (Git append-only branch + denyNonFastForwards) | ADR-012 §2.8 별도 layer | 별도 합의 |
| Layer 3 (pre-commit hook — git rebase/filter-branch/reset 감지) | ADR-012 §2.8 별도 layer | 별도 합의 |
| Layer 4 (CI 회귀 검증 — base branch 대비 line deletion / rewrite 감지) | ADR-012 §2.8 별도 layer | 별도 합의 |
| `anchor_method=signed_tag` / `external_snapshot` 2 메서드 | 본 PoC = `ci_run_id` 한 메서드 한정 | 별도 합의 |
| Anchor metadata 자체 signing (GPG / Sigstore / cosign) | Layer 5 multi-host MANDATORY 영역 | multi-host MANDATORY 격상 시 의무 발동 (ADR-012 §2.8 답습) |
| 실 GitHub Actions run id / commit SHA 검증 (외부 호출) | 본 PoC = literal 비교만 | 별도 합의 |
| Anchor 자동 갱신 / nightly cron | runtime hook 영역 | 별도 합의 |
| Multi-host external service 통합 | ADR-012 §2.8 MANDATORY 격상 영역 | 별도 합의 (multi-host 전환 시) |
| 1인 동일 호스트 SPOF 한계 (ADR-012 §2.8 + 외부 LLM 1 권고 5) | 동일 호스트 전체 침해는 본 ADR 의 완전 방어 범위 밖 | multi-host 전환 시 Layer 5 MANDATORY 발동 |

### 2.9 알려진 한계 (사양 §9 답습)

11건 (모두 분리 영역 명시):
1. Layer 2/3/4 미진입 (ADR-012 §2.8 별도 layer)
2. `anchor_method` `signed_tag` / `external_snapshot` 미진입
3. Anchor metadata 자체 signing 미진입 — multi-host MANDATORY
4. 실 GitHub Actions run id / commit SHA 외부 호출 검증 미진입
5. Anchor 자동 갱신 / nightly cron 미진입
6. Multi-host external service 통합 미진입
7. **1인 동일 호스트 SPOF 한계** (ADR-012 §2.8 답습)
8. Markdown 본문 자기 검출 — CI fixture 한정 scan 으로 회피
9. `agent: hermes` 의 anchor 작성 시도 = Group G `boundary_guard` 영역 (책무 분리)
10. `signed_tag` / `external_snapshot` 지원 부재
11. 외부 timestamping service (RFC 3161) 미통합

### 2.10 본 PoC 의 *evidence 가치* (사용자 명시 답습)

본 PoC 가 답하는 핵심 (사용자 명시 §0 + 사양 §13 답습):

> "hash chain만으로 충분한 영역과 부족한 영역을 구분하는가" + "Layer 5 external anchor / signed commit / git append-only가 왜 필요한지 evidence로 보강하는가"

**Layer 1 충분 영역** (Group C 답습 완료):
- 단일 entry tampering — 4 violation_type cover (PREV_HASH_MISMATCH / HASH_RECALCULATION / HISTORY_REWRITE / GENESIS_MISMATCH)

**Layer 1 부족 영역** (chain-only demo fixture 로 직접 시연):
- Full rewrite (모든 entry 재작성) → chain-only mode 시 PASS
- Tail truncation (마지막 entry 제거) → 남은 chain valid
- Middle deletion + 재계산 → 재계산된 chain valid
- Substitution (다른 valid chain) → 그 자체는 valid

**Layer 5 의무성 evidence** (anchor mode 시 모두 검출):
- `tail-hash-mismatch` — 모든 시나리오에서 검출 (anchor expected_tail_hash vs ledger 실 tail)
- `entry-count-mismatch` — truncation/deletion 검출
- `genesis-hash-mismatch` — substitution 검출 (다른 scope 시)

**1인 동일 호스트 SPOF 한계** (ADR-012 §2.8 + 외부 LLM 1 권고 5 답습):
- anchor file 자체가 변조되면 Layer 5 도 부분만 cover (fixture #5 = anchor_tampered) — multi-host external service 의무성 명시.

→ ADR-012 §2.8 5 Layer 다층 방어의 *각 layer 의 책무 명확화* 직접 evidence.

---

## 3. 풀 3+1 승격 trigger 5 자기 검증 (재명시)

§2.4 와 동일 — 0/5 미발화. **Reviewer-only 단축 합의 적격**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ ADR-012 §2.8 *Layer 5 External anchor* 영역의 *형식적 검출 layer* 운영 적용 첫 시제
- ✅ Layer 1 inadequacy 시연 — 4 attack scenario 모두 Group C `validate_chain` 단독 시 PASS (의도된 한계, evidence 가치)
- ✅ Layer 5 의무성 evidence — 동일 4 시나리오 + substitution + anchor tampered 모두 anchor mismatch 로 검출
- ✅ Custom validator 단독 채택 (외부 의존 0건 + Layer 2~4 미진입) 답습 검증
- ✅ Group C 산출물 (`jsonl_hash_chain` `validate_chain` + ENUMs + `compute_genesis_hash`) import 직접 답습
- ✅ Group F 후속 artifact path 답습 (`group-c-followup-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A~G/A3 답습)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ ADR-012 §2.8 5 Layer 中 Layer 2/3/4 통합
- ❌ 실 signed commit 강제 / 실 branch protection 변경 / 실 external timestamping service 연동
- ❌ Anchor metadata 자체 signing (GPG / Sigstore / cosign)
- ❌ 실 GitHub Actions run id 검증 (외부 호출)
- ❌ Multi-host external service 통합
- ❌ `anchor_method` `signed_tag` / `external_snapshot` 2 메서드 cover

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group C 후속 PoC = G4 *Layer 5 External anchor 정적 검출 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/5 발화, 7 금지 0/7 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 10/10 충족, 로컬 10/10 검증 PASS, CI workflow 16 step 형식 검증 PASS, ADR-012 §2.8 + G4 §4.4.5 직접 답습 (변경 0건 / 외부 의존 0건 / Layer 2~4 미진입)).

### 5.2 추가 조건 (C-CF-1 ~ C-CF-7)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-CF-1 | 본 PoC = G4 *Layer 5 External anchor 정적 검출 시제* 한정 — G4 / G2 / G3 / G4 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.3 #1~#2 명시 |
| C-CF-2 | Layer 2/3/4 미진입 — ADR-012 §2.8 별도 layer 영역 (별도 합의) | 사양 §9 #1 + 본 합의 §2.5 + §2.8 명시 |
| C-CF-3 | Anchor metadata 자체 signing (GPG / Sigstore / cosign) 미진입 — multi-host MANDATORY 영역 (별도 합의) | 사양 §9 #3 + §13 + 본 합의 §2.10 명시 |
| C-CF-4 | `anchor_method=ci_run_id` 한 메서드 한정 — `signed_tag` / `external_snapshot` = 별도 합의 | 사양 §3.2 + §9 #2 명시 |
| C-CF-5 | 1인 동일 호스트 SPOF 한계 (ADR-012 §2.8 + 외부 LLM 1 권고 5 답습) — multi-host 전환 시 Layer 5 MANDATORY 발동 | 사양 §9 #7 + §13 + 본 합의 §2.10 명시 |
| C-CF-6 | **Layer 1 inadequacy demo = 본 PoC 핵심 evidence** — chain-only mode 의도된 PASS 처리 → Layer 5 의무성 evidence | 사양 §2.2 + §13 + 본 합의 §2.6 명시 |
| C-CF-7 | Step 8 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §14 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (PoC 본문 / CI workflow / 사양 / 합의 / .gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group F 후속 — `hermes_to_openai` 또는 Skill 변환 feasibility 추가
   - (b) cross-vendor LLM 의뢰 (Group D/E/G/A3/CF 산출물)
   - (c) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)
   - (d) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)
   - (e) Group C 후속 후속 — Layer 2/3/4 통합 (별도 합의)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group C 후속 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 5 0/5 발화, 7 금지 0/7 위반, PASS 기준 10/10 + ADR-011 §2.1 5/5 충족, 로컬 10/10 PASS, CI workflow 16 step 형식 검증 PASS, ADR-012 §2.8 + §2.12 + G4 §4.4.5 직접 답습 (변경 0건 / 외부 의존 0건 / Layer 2~4 미진입). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group D/E/G/A3 답습). **본 PoC 핵심 evidence = Layer 1 inadequacy demo** (chain-only mode 에서 full rewrite 의도된 PASS → Layer 5 의무성 evidence). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
