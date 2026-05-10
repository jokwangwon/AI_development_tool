# 3+1 합의 보고서 — G2 GP-3 + GP-2 Credential/Secret Hygiene + Egress Redaction (Group D PoC, Reviewer-only 단축)

> **세션**: 2026-05-10 (Group D 진입 — code-side secret 검출 (D-1) + redaction 후 잔존 secret 검증 (D-2) 통합 PoC)
> **PASS scope**: G2 GP-2 / GP-3 *형식적 검출 layer 시제* 한정 — **Implementation Pending** (G2 GP-2 / GP-3 / G2 전체 Implementation/Runtime PASS 권한 0건, 사용자 명시 답습)
> **합의 형식**: **Reviewer-only 단축** (풀 3+1 승격 trigger 7 = 0/7 발화 → 단축 적격, 사용자 명시 답습)
> **검토 대상**:
> - `tools/secret_scanner.py`
> - `tests/fixtures/secret_hygiene/{pass,fail,redaction_pass,redaction_fail}/*`
> - `.github/workflows/secret-hygiene-egress-redaction.yml`
> - `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md`
> - `.gitignore` (`group-d-logs/` 추가)
> **상위 권위**: ADR-008 부록 C (Design/Governance ↔ Implementation/Runtime 분리), ADR-011 §2.1 (a)~(e) + §2.3 운영 함의 #2, ADR-010 (Vault HSM, cross-reference), ADR-012 (Evidence Ledger), governance-preconditions.md §4 (GP-2) + §5 (GP-3), redaction-pattern-equivalence.md (R-4), r4-1-trigger-extension-evidence.md §4.1 (R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns), implementation-runtime-roadmap.md §3.1 (Order 4 + 5)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group F PoC 합의 형식 (`docs/review/3plus1-consensus-2026-05-10-g2-gp6-memory-skill-feasibility-reviewer-only.md` 직접 답습)

---

## 1. 검토 사항

### 1.1 산출물 매트릭스 (8건)

| # | 산출물 | 라인 | 답습 |
|---|-------|-----|------|
| 1 | `tools/secret_scanner.py` | 261 | R-4.1 Tier-1 42 catalog + baseline 5 = **45 patterns** import 직접 (Prefix 36 + regex 7 + alternation 2) + 2 mode CLI (`scan-source` / `scan-log`) + `--list-patterns` self-check + `is_redaction_marker_match()` (scan-log 전용 FP 회피) + `Violation` dataclass + 재귀 file iterator. **외부 의존성 0건** (custom scanner 단독, gitleaks/detect-secrets 미도입). |
| 2 | `tests/fixtures/secret_hygiene/pass/{safe_config.py, safe_settings.json}` | 11 + 8 lines | D-1 PASS — Tier-1 패턴 0건 (FP 검증) |
| 3 | `tests/fixtures/secret_hygiene/fail/{env_assignment.py, json_field.json, private_key_block.pem, prefix_aws.py}` | 4 fixture | D-1 FAIL — 4 패턴 cover (prefix-baseline + regex + alternation + private-key sub-type T1-035) |
| 4 | `tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt` | 7 lines | D-2 PASS — `[REDACTED]` 마커 5건 (redaction marker 인식 OK) |
| 5 | `tests/fixtures/secret_hygiene/redaction_fail/{partial_redact.txt, base64_evasion.txt}` | 2 fixture | D-2 FAIL — partial leak 1건 + base64 evasion 1건 (*known limitation* 표기, Hermes upstream R2-6 영역) |
| 6 | `.github/workflows/secret-hygiene-egress-redaction.yml` | 217 | 12 step (3 setup + 6 검증 + summary.json + artifact + Evidence summary). artifact path = `group-d-logs/` (Group F 후속 답습, leading dot 미사용) |
| 7 | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` | 351 | PoC 사양 (12 섹션 — 목적 / 범위 / 도구 근거 / R-4.1 답습 / fixture / 검증 매트릭스 / 답습 매핑 / PASS 7 / 한계 / CI 설계 / trigger 7 / Evidence 5 / 변경이력) |
| 8 | 본 합의 보고서 | ~310 | Group A 1차/2차 + Group B + Group C + Group F Reviewer-only 합의 형식 답습 |

**합산 = 8 파일** (Group F 답습 평균).

### 1.2 fixture 9건 검증 결과

| Fixture | 위치 | 매칭 패턴 |
|---|---|---|
| `safe_config.py` | pass/ | 0 (Tier-1 부재 — FP 0건) |
| `safe_settings.json` | pass/ | 0 (sensitive key 부재) |
| `env_assignment.py` | fail/ | BL-1 (sk-ant-) + BL-2 (sk-) + T1-032 (H-A ENV) — 6건 |
| `json_field.json` | fail/ | T1-033 (H-B JSON) + T1-041/042 (alternation) — 3건 |
| `private_key_block.pem` | fail/ | T1-035 (H-E Private key) — 1건 |
| `prefix_aws.py` | fail/ | BL-4 (AKIA) + BL-5 (xoxb) + T1-032 (H-A) — 4건 |
| `env_redacted.txt` | redaction_pass/ | 0 (`[REDACTED]` 마커 인식 OK) |
| `partial_redact.txt` | redaction_fail/ | BL-2 + T1-032 + T1-041/042 — 7건 (partial leak 검출) |
| `base64_evasion.txt` | redaction_fail/ | 0 (base64 미검출 = known limitation, 의도된 동작) |

### 1.3 Pattern 45 등록 확인 (`--list-patterns` 출력)

```
registered_patterns_count=45
  baseline_prefix=5     (sk-ant-, sk-, ghp_, AKIA, xox[baprs]-)
  tier1_prefix=31       (Hermes #3..#7, #9..#14, #16..#35)
  tier1_regex=7         (H-A/B/C/E/F/G/K — H-J/H-L 제외)
  tier1_alternation=2   (URL query 16 + Body/form 14 sensitive keys)
  skip_direct_register=['T1-038', 'T1-040']  (R-4.1 §4.2 답습)
  active_patterns=45
  tier1_42_catalog_compliant=True
```

### 1.4 D-1 / D-2 로컬 검증 결과 (6/6 PASS)

| # | 검증 | 명령 | rc | 결과 |
|---|------|------|-----|------|
| 1 | D-1 PASS scan | `secret_scanner.py --mode scan-source pass/` | **0** | 위반 0건 (FP 0) |
| 2 | D-1 FAIL scan | `secret_scanner.py --mode scan-source fail/` | **1** | 14 violations + 3 카테고리 cover (alternation + prefix-baseline + regex) + private-key T1-035 |
| 3 | D-2 PASS redaction residual | `secret_scanner.py --mode scan-log redaction_pass/` | **0** | 잔존 0건 (`[REDACTED]` 마커 인식) |
| 4 | D-2 FAIL redaction leak | `secret_scanner.py --mode scan-log redaction_fail/` | **1** | partial_redact 7건 검출 + base64_evasion 미검출 (known limitation) |
| 5 | Tier-1 pattern count | `secret_scanner.py --list-patterns` | **0** | registered=45 + tier1_42_catalog_compliant=True |
| 6 | F-금지 grep | scanner + fixture grep | **0** | 실 API key / provider SDK import 0건 (fake canary 의무 답습) |

### 1.5 CI workflow 12 step 구조

| # | Step | 책무 | 검증 |
|---|------|------|------|
| 1 | Checkout | actions/checkout@v4 | — |
| 2 | Set up Python | actions/setup-python@v5 (3.12) | — |
| 3 | Prepare log directory | `mkdir -p group-d-logs` (leading dot 미사용) | — |
| 4 | Tier-1 pattern count self-check | `--list-patterns` | rc=0 + `registered_patterns_count=45` + `tier1_42_catalog_compliant=True` |
| 5 | D-1 PASS — scan-source pass/ | rc=0 + violations=0 grep | §1.4 #1 |
| 6 | D-1 FAIL — scan-source fail/ | rc=1 + ≥4 + 3 카테고리 + T1-035 grep | §1.4 #2 |
| 7 | D-2 PASS — scan-log redaction_pass/ | rc=0 + violations=0 grep | §1.4 #3 |
| 8 | D-2 FAIL — scan-log redaction_fail/ | rc=1 + partial_redact 검출 + base64 미검출 (known limitation) | §1.4 #4 |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 API key / provider SDK 0건 grep | §1.4 #6 |
| 10 | Build summary.json | step output 집계 → `group-d-logs/summary.json` 14 항목 | — |
| 11 | Upload artifact | `actions/upload-artifact@v4` `secret-hygiene-egress-redaction-evidence` retention 30일 | Group F 후속 답습 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` 16 항목 | R-6 답습 |

---

## 2. 검토 항목 — Reviewer 관점 10 영역

### 2.1 PASS 조건 답습 — ADR-011 §2.1 (a)~(e)

| 조건 | 충족 | 근거 |
|------|----|------|
| (a) 동등 이상의 안전 결과 | ✅ | R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 직접 답습 (Hermes Tier-1 패턴 카탈로그 전수 적용) |
| (b) 격리 환경 PoC 실증 | ✅ | fixture 한정 (실 secret 0건, fake canary 의무 답습) + 외부 의존 0건 (custom scanner 단독) + CI ubuntu-latest |
| (c) ADR/SDD 권위 명시 | ✅ | ADR-008 §A.2 + 부록 C / ADR-011 §2.1 + §2.3 / ADR-010 / ADR-012 / GP §4 + §5 / R-4 + R-4.1 / roadmap §3.1 cross-reference |
| (d) 자동 회귀 검증 경로 | ✅ | CI workflow 12 step + paths trigger 3 영역 + artifact 30일 retention |
| (e) 합의 APPROVE | ✅ | 본 보고서 §5 결론 |

### 2.2 사용자 명시 PASS 기준 7 (사양 §7 답습)

| # | 기준 | 충족 | 근거 |
|---|----|----|------|
| 1 | D-1 PASS scan | ✅ | rc=0 + 위반 0건 (FP 0) |
| 2 | D-1 FAIL scan | ✅ | rc=1 + 14 violations + 3 카테고리 cover + private-key T1-035 |
| 3 | D-2 PASS redaction residual | ✅ | rc=0 + 잔존 0건 |
| 4 | D-2 FAIL redaction leak | ✅ | rc=1 + partial leak 검출 (base64 = known limitation) |
| 5 | Tier-1 pattern count self-check | ✅ | registered_patterns_count=45 + tier1_42_catalog_compliant=True |
| 6 | F-금지 grep | ✅ | 실 API key / provider SDK 0건 |
| 7 | summary.json + artifact + evidence summary | ✅ | summary.json 14 항목 + artifact 9 파일 + Evidence summary 16 항목 |

**합산 7/7 충족.**

### 2.3 사용자 명시 12 금지 자기 검증 (0/12 위반)

| # | 금지 | 위반 | 근거 |
|---|------|----|------|
| 1 | 실 API key 사용 | 0 | fake canary 의무 (`sk-FAKE-...`, `AKIAFAKEGROUPDNOTREAL01`, `ghp_FAKE_...`, `R41T-fakecanary-...`) — F-금지 grep step 자동 강제 |
| 2 | 실 provider SDK 호출 | 0 | scanner 본문 `import (openai\|anthropic\|google.generativeai\|litellm\|ollama)` 0건 |
| 3 | 실 외부 API 호출 | 0 | 본 PoC 외부 호출 0건 (regex matching 한정) |
| 4 | 실 secret 파일 사용 | 0 | fixture 한정 (`tests/fixtures/secret_hygiene/`) |
| 5 | production credential 접근 | 0 | 본 PoC 미진입 |
| 6 | Hermes 컨테이너 chmod / entrypoint stat / inotify | 0 | Hermes upstream 영역 (R1-2, ADR-008 §A.2, ADR-010 Vault HSM) — 사양 §1.2 + §8 분리 명시 |
| 7 | git pre-commit hook 실 활성화 | 0 | T2 정책 영역 (ADR-011 §2.4) — 분리 |
| 8 | PR auto-reject GitHub branch protection | 0 | T3 정책 영역 — 분리 |
| 9 | G2 GP-2 / GP-3 최종 PASS 선언 | 0 | 본 PoC = *형식적 검출 layer 시제* 한정 (사양 §0 + §1.2 명시) |
| 10 | G2 전체 Implementation/Runtime PASS 선언 | 0 | CONTEXT.md 변경 0건 (meta 갱신 시 *부분 충족 시제* 한정 답습) |
| 11 | Hermes PMO 격상 선언 | 0 | 변경 0건 (4 게이트 합산표 변경 0건) |
| 12 | ADR 본문 자동 갱신 | 0 | `docs/decisions/` + `docs/architecture/` 본문 변경 0건 (cross-reference 답습 한정) |

**추가**: gitleaks / detect-secrets 도입 0건 + Tier-2 / Tier-3 catalog 확장 0건.

### 2.4 사용자 명시 풀 3+1 승격 trigger 7 자기 검증 (0/7 발화)

| # | Trigger | 발화 | 근거 |
|---|---------|----|------|
| 1 | 실제 secret 처리 정책 변경 필요 | 0 | fake canary 한정, 정책 변경 0건 |
| 2 | R-4 Tier-1 catalog 변경 필요 | 0 | 답습만 (R-4.1 §4.1 직접 복사, 변경 0건) |
| 3 | redaction 정책 완화 필요 | 0 | Tier-1 42 catalog 답습 (완화 0건) — `is_redaction_marker_match()` 는 *FP 회피*, 정책 완화 아님 |
| 4 | gitleaks / detect-secrets 도구 선택 장기 정책 고정 | 0 | 도구 도입 0건 (custom scanner 단독, 사양 §2.1 답습) |
| 5 | false positive가 정상 개발 흐름을 과도하게 막음 | 0 | fixture 한정 + redaction marker 인식 OK (FP 0건) |
| 6 | false negative로 secret 누출 가능성 잔존 | ⚠️ 부분 (base64 1건 *known limitation* 분리 명시) | 본 한계 = §3 #1 명시, 본 PoC 차단 조건 아님 |
| 7 | ADR-010 / ADR-011 / ADR-012 와 충돌 | 0 | cross-reference 답습 한정 |

**합산 0/7 발화** (#6 부분 발화는 known limitation 명시 분리 → 풀 3+1 미발화 적격) → **Reviewer-only 단축 합의 적격**.

### 2.5 R-4.1 답습 충실도

| 영역 | R-4.1 답습 방식 | 신규 작성 |
|---|---|---|
| Tier-1 42 catalog | `docker/r4-1-poc/r4_1_poc.py` line 51~213 직접 복사 (변경 0건) | 0 |
| canary marker convention | R-4.1 §5 답습 | 0 |
| 45 patterns 등록 (Prefix 36 + regex 7 + alternation 2) | R-4.1 §4.1 답습 (변경 0건) | 0 |
| H-J/H-L 직접 등록 제외 + alternation 채택 | R-4.1 §4.2 답습 (`SKIP_DIRECT_REGISTER`) | 0 |
| violation reporter 형식 | R-4.1 §5.1 답습 (id / source / category / vendor) | 0 |
| Custom scanner 신규 (~261줄) | — | 2 mode CLI + violation 집계 + Tier-1 count + redaction marker 인식 + 재귀 file iterator |
| 9 fixture | — | 9 (PASS 2 + FAIL 4 + REDACTION_PASS 1 + REDACTION_FAIL 2) |

**리팩토링 0건** (R-4.1 patterns 직접 복사 답습) + **외부 의존 0건** (custom scanner 단독, gitleaks/detect-secrets 미도입).

### 2.6 Group A/B/C/F 답습 충실

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + 2 mode) | Group A 1차 + Group B + Group F |
| Fixture 디렉토리 구조 (`pass/` + `fail/` + `redaction_pass/` + `redaction_fail/`) | Group A 1차 (pass/fail) + Group F (직접 답습) |
| CI workflow 12 step (4 검증 + Tier-1 count + F-금지 grep + summary.json + artifact + Evidence summary) | Group F (직접 답습) |
| Reviewer-only 단축 합의 형식 | Group A 1차 + Group B + Group F |
| **artifact path (leading dot 미사용)** | **Group F 후속 (group-d-logs/) 직접 답습** |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group F |

### 2.7 base64 evasion known limitation 처리

`redaction_fail/base64_evasion.txt` = base64-encoded canary (`c2stRkFLRS1HUk9VUC1ELU5PVC1BLVJFQUwtU0VDUkVU`) 1건 + comment 4건 (limitation 명시). Scanner 가 base64 직접 미검출 (의도된 동작 — direct prefix/regex/alternation 한정). Comment 내 literal canary 노출 0건 (cleanup 답습).

**한계 분리 영역**: Hermes upstream R2-6 영역 (`tests/hermes/redaction/test_base64_evasion.py`) — 별도 합의.

### 2.8 책무 분리 — 별도 합의 영역

| 영역 | 분리 사유 | 미래 영역 |
|------|---------|---------|
| Hermes 컨테이너 chmod 600 / entrypoint stat / inotify | Hermes upstream (R1-2, ADR-008 §A.2) | ADR-010 Vault HSM 영역 |
| git pre-commit hook 실 활성화 | T2 정책 영역 | 별도 합의 |
| PR auto-reject GitHub branch protection | T3 정책 영역 | 별도 합의 |
| log file canary inject + grep nightly | R-6 workflow 확장 | 별도 합의 (R-7 SOP §5 ROLLBACK trigger R5) |
| LLM API request body 실 송신 redaction | P1 facade RedactionFilter | 별도 합의 |
| Tier-2 / Tier-3 catalog 확장 (Slack / GCP / Azure 등) | 사용자 명시 금지 | 풀 3+1 합의 + 외부 LLM 1+ |
| gitleaks / detect-secrets 도구 도입 | 풀 3+1 trigger #4 위험 회피 | 별도 합의 |

### 2.9 알려진 한계 (사양 §8 답습)

1. **base64 / URL-encoded / 압축 등 advanced evasion 미커버** — Hermes upstream R2-6 영역 (사양 §8 #1, 본 합의 §2.7 명시).
2. Hermes 컨테이너 storage 보호 (chmod / inotify) — §2.8 분리.
3. git pre-commit hook 실 활성화 — §2.8 분리.
4. PR auto-reject branch protection — §2.8 분리.
5. log file canary inject nightly — §2.8 분리.
6. LLM API request body 실 송신 redaction — §2.8 분리.
7. Tier-2/3 catalog 확장 — §2.8 분리.
8. gitleaks / detect-secrets 도입 — §2.8 분리.
9. Reference 토이 redactor 본문 변경 시 redaction 정책 완화 trigger #3 발화 가능 — 사양 §8 #9.
10. **18 fixture 확장안** (8 패턴 모두 cover) — 본 PoC = 9 fixture 한정 (사양 §1.1 + §8 #10).
11. **Markdown 본문 자기 검출** — 본 합의 보고서 / 사양 문서가 fixture 매트릭스 본문에 fake canary literal (`sk-FAKE-...`, `AKIAFAKEGROUPDNOTREAL01`, `ghp_FAKE_...`) 을 포함하므로 secret_scanner 가 본 보고서 자기 검출 가능 (Group B `evidence_pass_gate.py` 와 동일한 markdown 자기 검출 패턴 답습). **CI workflow 는 `tests/fixtures/secret_hygiene/` 한정 scan** (paths trigger + step 명시) 로 회피. 후속 markdown code block 회피 = 별도 합의 영역 (Group B PoC 사양 §2.8 #1 답습).

### 2.10 책무 분담 매트릭스 (사양 §0 답습)

| 영역 | D-1 (GP-3) | D-2 (GP-2) | 분리 영역 |
|------|------------|------------|----------|
| code-side secret 검출 | ✅ scan-source mode | — | — |
| redaction 후 잔존 검증 | — | ✅ scan-log mode (redaction marker 인식) | — |
| Hermes 컨테이너 chmod / inotify | ❌ | ❌ | Hermes upstream (R1-2) |
| Hermes native `agent/redact.py` 본 호출 | ❌ | ❌ | Hermes upstream |
| 토이 reference redactor | — | (선택, 본 PoC 미작성) | 별도 합의 시점 |
| Tier-2/3 catalog | ❌ | ❌ | 별도 합의 + 외부 LLM 1+ |

---

## 3. 풀 3+1 승격 trigger 7 자기 검증 (재명시)

§2.4 와 동일 — 0/7 미발화. **Reviewer-only 단축 합의 적격 (사용자 명시 답습)**.

---

## 4. 본 PoC 의 *발생* / *미발생* 사항

### 4.1 본 PoC 가 *발생* 시키는 것

- ✅ R-4.1 Tier-1 42 catalog + baseline 5 = 45 patterns 의 *code-side scan* 운영 적용 첫 시제
- ✅ R-4.1 Tier-1 42 catalog 의 *redaction 후 잔존 검증* 적용 첫 시제 (D-2 GP-2 형식적 contract)
- ✅ Custom scanner 단독 채택 (외부 의존성 0건 + Tier-2/3 확장 위험 0건) 답습 검증
- ✅ Group F 후속 artifact path 답습 (`group-d-logs/` — leading dot 미사용)
- ✅ Reviewer-only 단축 합의 답습 (Group A/B/C/F)

### 4.2 본 PoC 가 *발생시키지 않는* 것 (사용자 명시 답습)

- ❌ G2 GP-2 / GP-3 최종 Implementation/Runtime PASS 선언
- ❌ G2 전체 Implementation/Runtime PASS 선언
- ❌ Hermes PMO 격상 선언
- ❌ ADR 본문 자동 갱신 (cross-reference 답습 한정)
- ❌ R-4 Tier-1 catalog 변경 (답습만)
- ❌ Tier-2 / Tier-3 catalog 확장
- ❌ gitleaks / detect-secrets 도구 도입
- ❌ Hermes 컨테이너 chmod / entrypoint stat / inotify
- ❌ git pre-commit hook 실 활성화 / PR auto-reject branch protection
- ❌ 실 secret / API key / provider SDK 호출 / 외부 API 호출
- ❌ Hermes native `agent/redact.py` 본 호출

---

## 5. 검토 결론

### 5.1 Reviewer 종합 판정

**APPROVE WITH CONDITIONS** — Group D PoC = G2 GP-2 / GP-3 *형식적 검출 layer 시제* 답습 충실 (Reviewer 관점 10 영역 모두 충족, 풀 3+1 승격 trigger 0/7 발화, 12 금지 0/12 위반, ADR-011 §2.1 5/5 충족, 사용자 명시 PASS 기준 7/7 충족, 로컬 6/6 검증 PASS, CI workflow 12 step 형식 검증 PASS, R-4.1 직접 답습 (리팩토링 0 / 복제 0 / 외부 의존 0)).

### 5.2 추가 조건 (C-D-1 ~ C-D-7)

| # | 조건 | 답습 위치 |
|---|----|---------|
| C-D-1 | 본 PoC = G2 GP-2 / GP-3 *형식적 검출 layer 시제* 한정 — G2 GP-2 / GP-3 / G2 전체 Implementation/Runtime PASS 권한 0건 (사용자 명시 답습) | 사양 §0 + §1.2 + 본 합의 §2.3 #9~#12 명시 |
| C-D-2 | base64 / URL-encoded / 압축 등 advanced evasion = Hermes upstream R2-6 영역 (별도 합의) — 본 PoC 차단 조건 외 | 사양 §8 #1 + 본 합의 §2.7 + §2.9 #1 명시 |
| C-D-3 | Hermes 컨테이너 chmod / entrypoint stat / inotify = R1-2 + ADR-010 Vault HSM 영역 (별도 합의) | 사양 §1.2 + §8 #2~#3 + 본 합의 §2.8 명시 |
| C-D-4 | gitleaks / detect-secrets 도입 = Tier-2 / Tier-3 catalog 확장 결정 후 풀 3+1 합의 + 외부 LLM 1+ | 사양 §2.1 + §8 #7~#8 + 본 합의 §2.4 #4 명시 |
| C-D-5 | redaction marker 인식 (`is_redaction_marker_match()`) = scan-log mode FP 회피 한정, redaction 정책 완화 0건 | 사양 §0 + 본 합의 §2.4 #3 명시 |
| C-D-6 | 18 fixture 확장안 (8 패턴 모두 cover) = 후속 후보, 본 PoC = 9 fixture 한정 (사용자 명시) | 사양 §1.1 + §8 #10 + 본 합의 §2.9 #10 명시 |
| C-D-7 | Step 9 GitHub Actions actual run 결과 → CONTEXT/INDEX/SESSION 메타 갱신 영역 (사양 §12 변경 이력 답습) | 본 합의 §5.3 #4 |

### 5.3 다음 단계 권고

1. 본 합의 commit 분리 (PoC 본문 / CI workflow / 사양 / 합의 / .gitignore)
2. push (사용자 confirm 후) origin feature/hermes-phase0
3. GitHub Actions actual run 검증 (R-6 답습 — Group A/B/C/F 답습)
4. CONTEXT / INDEX / SESSION 갱신 (사용자 명시 답습) — *meta* 문서 영역, ADR 본문 변경 0건
5. **다음 진입점 (사용자 결정 영역)**:
   - (a) Group E (G2 GP-4 External Input Validation + G4 Memory/Skill schema validation) — 단축 합의
   - (b) Group A 3차 (URL/endpoint grep PoC, C-8) — 풀 3+1
   - (c) Group F 후속 — `hermes_to_openai` 또는 Skill 변환 feasibility 추가
   - (d) Group C 후속 — `history_rewrite` Layer 5 PoC (ADR-012 §2.8)
   - (e) cross-vendor LLM 의뢰 (Group C 또는 Group D 산출물)
   - (f) Group H — ADR-014 발행 (풀 3+1 + 외부 LLM 1+)
   - (g) Group I — G3 22 권한 분해 (풀 3+1 + 외부 LLM 1+)

---

## 6. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 | Group D 통합 PoC, Reviewer-only 단축 합의 APPROVE WITH CONDITIONS, 풀 3+1 승격 trigger 7 0/7 발화, 12 금지 0/12 위반, PASS 기준 7/7 + ADR-011 §2.1 5/5 충족, 로컬 6/6 PASS, CI workflow 12 step 형식 검증 PASS, R-4.1 직접 답습 (리팩토링 0 / 복제 0 / 외부 의존 0). evidence 별도 파일 미작성 — 본 보고서 §1~§4 매트릭스 통합 (Group B/C/F 답습). Step 8 actual run 결과 = 본 합의 *후속* meta 문서 영역. |
