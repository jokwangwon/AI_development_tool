# G2 GP-3 + GP-2 Credential/Secret Hygiene + Egress Redaction — Group D PoC 사양

> **상태**: DRAFT (2026-05-10, Group D 진입 — code-side secret 검출 (D-1) + redaction 후 잔존 secret 검증 (D-2) 통합 PoC)
> **답습 출처**:
> - `docs/architecture/implementation-runtime-roadmap.md` §2.1 Order 4 (GP-3) + Order 5 (GP-2) / §3.1 매트릭스 (그룹 D = GP-3 + GP-2 동시 진행) / §5.3 의존성 (Group A 완료 후, R-4 catalog 답습)
> - `docs/architecture/governance-preconditions.md` §4 (GP-2 Egress Redaction) / §5 (GP-3 Credential / Secret Hygiene)
> - `docs/architecture/redaction-pattern-equivalence.md` (R-4 — 패턴 동등성 비교 + Tier-1 catalog enumerate)
> - `docs/phase0/r4-1-trigger-extension-evidence.md` §4.1 (R-4.1 — Tier-1 42 catalog + baseline 5 = 45 patterns trigger 등록 PASS evidence)
> - `docs/decisions/ADR-008-hermes-adoption-decision.md` §A.2 (Credential 처리) + 차단조건 #1 (P2 v3 본질 — DB 평문 저장 차단 결과)
> - `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.1 (a)~(e) (수단/목적 분리 5 조건 의무) + §2.3 운영 함의 #2 (송신 redaction)
> - `docs/decisions/ADR-010-secrets-management.md` (Vault HSM — 본 PoC 미진입 영역, cross-reference)
> - `docs/decisions/ADR-012-evidence-ledger-protection.md` (Evidence Ledger 보호 — secret_scanner 결과 evidence summary 형식)
> **PASS 조건 답습**: ADR-011 §2.1 (a)~(e) 5/5 + 사용자 명시 7 풀 3+1 승격 trigger / 12 금지 항목 / 7 PASS 검증
> **상위 권위**: ADR-008 부록 C §C.5 (Design/Governance ↔ Implementation/Runtime 분리), P2 v3 §3.1.4 (Implementation Pending)
> **답습 시제**: Group A 1차/2차 + Group B + Group C + Group F PoC 사양 형식 (`g2-gp6-memory-skill-migration-feasibility-poc.md` 직접 답습)

---

## 0. 목적

본 PoC 는 G2 GP-3 (Credential / Secret Hygiene) 와 GP-2 (Egress Redaction) 의 *형식적 검출 layer* 첫 시제 — R-4.1 Tier-1 42 catalog (+ baseline 5 = 45 patterns) 를 **code-side scan** (D-1) 과 **redacted output 잔존 검증** (D-2) 양쪽에 적용.

**범위 한정 핵심 결정** (사용자 명시 "최소 PoC 단위로 쪼개" 답습):

- **D-1 (GP-3)** = code-side secret 검출만 (`tools/secret_scanner.py --mode scan-source`). Hermes 컨테이너 *저장 경로* (chmod 600 / entrypoint stat / inotify — R1-2) = **Hermes upstream 영역**, 본 PoC 미진입.
- **D-2 (GP-2)** = redaction 후 *잔존 secret 검증* 만 (`tools/secret_scanner.py --mode scan-log`). Hermes native `agent/redact.py` 본 호출 = **Hermes upstream 영역**. 본 PoC = *contract 검증* (R-4.1 Tier-1 42 catalog 패턴이 redacted output 에 잔존 시 FAIL).

본 PoC 는 **형식적 검출 layer 한정** — 의미적 redaction 정확성 / Hermes 본 redactor 동작 / 실 secret 처리 정책 변경 / Tier-2/3 catalog 확장 = 본 PoC 방어 범위 외 (사용자 명시 답습).

신규 정책 발명 0건 — `implementation-runtime-roadmap.md` §3.1 + GP §4/§5 + R-4 + R-4.1 명세 그대로 답습.

---

## 1. PoC 범위 (사용자 확인 — 2026-05-10)

### 1.1 포함 산출물 8건

| 산출물 | 경로 | 책무 |
|--------|------|------|
| 본 사양 문서 | `docs/phase0/g2-gp3-gp2-secret-hygiene-egress-redaction-poc.md` | PoC 사양 + 답습 매핑 + 사용자 명시 12 금지 / 7 trigger / 7 PASS 매트릭스 |
| Validator | `tools/secret_scanner.py` | 단일 도구 + 2 mode (scan-source / scan-log) + 45 patterns (R-4.1 Tier-1 catalog 직접 답습 — Prefix 36 + regex 7 + alternation 2) + violation reporter |
| PASS fixture × 2 | `tests/fixtures/secret_hygiene/pass/{safe_config.py,safe_settings.json}` | secret 부재 정상 fixture (FP 검증) |
| FAIL fixture × 4 | `tests/fixtures/secret_hygiene/fail/{env_assignment.py,json_field.json,private_key_block.pem,prefix_aws.py}` | 4 패턴 cover (prefix / regex / alternation / private-key) |
| REDACTION_PASS fixture × 1 | `tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt` | 정상 redacted output (잔존 0) |
| REDACTION_FAIL fixture × 2 | `tests/fixtures/secret_hygiene/redaction_fail/{partial_redact.txt,base64_evasion.txt}` | redaction leak 1건 (partial) + base64 evasion 1건 (*known limitation* 표기 — Hermes upstream R2-6 영역) |
| CI workflow | `.github/workflows/secret-hygiene-egress-redaction.yml` | PASS/FAIL 양방향 + Tier-1 count 자기 검증 + F-금지 grep + summary.json + artifact (`group-d-logs/` — Group F 후속 답습, leading dot 미사용) + Evidence summary |
| Reviewer-only 단축 합의 | `docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-secret-hygiene-reviewer-only.md` | PoC 검토 + 7 trigger 0/7 자기 검증 + evidence 매트릭스 통합 (Group F 답습) |

**합산 = 8 파일** (Group F 답습 평균).

### 1.2 제외 (별도 합의 영역 — 사용자 명시 12 금지 답습)

| 항목 | 분리 이유 |
|------|----------|
| 실 API key 사용 | **사용자 명시 #1** — fake canary 의무 (예: `sk-FAKE-GROUP-D-NOT-A-REAL-SECRET`, `AKIAFAKEGROUPDNOTREAL01`, `ghp_FAKE_GROUP_D_NOT_REAL`, `R41T-fakecanary-D-not-real`) |
| 실 provider SDK 호출 | **사용자 명시 #2** |
| 실 외부 API 호출 | **사용자 명시 #3** |
| 실 secret 파일 사용 | **사용자 명시 #4** |
| production credential 접근 | **사용자 명시 #5** |
| Hermes 컨테이너 chmod 600 / entrypoint stat / inotify | **사용자 명시 #6** — Hermes upstream 영역 (R1-2, ADR-008 §A.2, ADR-010 Vault HSM 영역) |
| git pre-commit hook 실 활성화 | **사용자 명시 #7** — T2 정책 영역 (ADR-011 §2.4) |
| PR auto-reject GitHub branch protection 변경 | **사용자 명시 #8** — T3 정책 영역 |
| G2 GP-2 / GP-3 최종 PASS 선언 | **사용자 명시 #9** — 본 PoC = *형식적 검출 layer 시제* 한정 |
| G2 전체 Implementation/Runtime PASS 선언 | **사용자 명시 #10** |
| Hermes PMO 격상 선언 | **사용자 명시 #11** |
| ADR 본문 자동 갱신 | **사용자 명시 #12** — cross-reference 답습 한정 |
| Tier-2 / Tier-3 catalog 확장 | 사용자 명시 (Group F 답습) — `_SENSITIVE_QUERY_PARAMS` / `_SENSITIVE_BODY_KEYS` 외 추가 catalog 0건 |
| gitleaks / detect-secrets 도구 도입 | 사용자 명시 풀 3+1 trigger #4 위험 회피 — custom scanner 단독 채택 |
| log file canary inject + grep nightly | R-6 workflow 확장 영역 — 별도 합의 |
| LLM API request body 실 송신 redaction | P1 facade RedactionFilter — 별도 합의 |

---

## 2. 도구 선택 근거

### 2.1 4 옵션 비교 (사용자 명시 4 후보 답습)

| 옵션 | 채택 | 사유 |
|---|---|---|
| **(A) Custom scanner (R-4.1 Tier-1 42 catalog 직접 재사용)** | **✅ 채택** | R-4.1 답습 충실 + 외부 의존성 0건 + Tier-2/3 확장 위험 0건 + 신규 tool 1 파일 한정 + Reviewer-only 단축 합의 적격 |
| (B) gitleaks | ❌ 제외 | gitleaks default ruleset 에 Tier-2/3 패턴 (Slack token / GCP service account 등) 포함 → 사용자 명시 "Tier-2/3 catalog 자동 확장 금지" 위반 위험 |
| (C) detect-secrets | ❌ 제외 | plugin-based + baseline file 형식이 *silenceable* (false negative 위험) + Tier-2/3 plugin 자동 활성화 위험 |
| (D) gitleaks + detect-secrets 병행 | ❌ 제외 | 도구 2개 = scope 확장 + 정책 고정 risk (사용자 명시 풀 3+1 trigger #4 발화 가능) |

**채택 = (A) 단독**. gitleaks/detect-secrets 도입은 *별도 합의* (Tier-2/3 catalog 확장 결정 후 풀 3+1 영역).

### 2.2 Custom scanner 의 본 PoC 답습 책무

| 책무 | 근거 |
|------|------|
| R-4.1 Tier-1 42 catalog 직접 재사용 | `docker/r4-1-poc/r4_1_poc.py` line 53~228 답습 (변경 0건 — Tier-2/3 확장 금지) |
| Tier-1 marker 답습 (`R41T-` + `NOTAREAL` / `fakecanary`) | R-4.1 §5 canary marker convention 답습 |
| 2 mode CLI dispatch (scan-source / scan-log) | Group A 1차 (`provider_import_scanner.py`) + Group B (`evidence_pass_gate.py`) + Group F (`memory_skill_roundtrip.py`) 답습 |
| violation reporter (line / pattern_id / category / vendor) | R-4.1 §5.1 canary catalog 답습 |
| Tier-1 등록 자기 검증 (`registered_patterns_count`) | R-4.1 §5 PASS rate 자기 검증 답습 |

---

## 3. R-4.1 Tier-1 42 catalog 답습 방식

### 3.1 45 patterns 구성 (사용자 명시 — Prefix 36 + 추가 regex 7 + alternation 2)

본 PoC = R-4.1 §4.1 등록 패턴 (45종) **직접 답습** — 변경 0건.

```
Baseline 5 prefix (R-2 PoC 보존):
  sk-ant-, sk-, ghp_, AKIA, xox[baprs]-

Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35):
  github_pat_, gho_, ghu_, ghs_, ghr_, AIza, pplx-, fal_, fc-, bb_live_,
  gAAAA, sk_live_, sk_test_, rk_live_, SG\., hf_, r8_, npm_, pypi-, dop_v1_,
  doo_v1_, am_, sk_ (ElevenLabs), tvly-, exa_, gsk_, syt_, retaindb_, hsk-,
  mem0_, brv_

Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외):
  ENV assignment, JSON field (12 keys, IGNORECASE),
  Authorization header (Bearer, IGNORECASE), Private key block,
  DB connstr password (postgres/mysql/mongodb/redis/amqp, IGNORECASE),
  JWT (eyJ...), URL userinfo (non-DB schemes)

Tier-1 alternation 2 (H-J/H-L 의 sensitive key 기반 변환):
  URL query sensitive keys alternation (16, IGNORECASE),
  Body/form sensitive keys alternation (14, IGNORECASE)
```

**합산 = 5 + 31 + 7 + 2 = 45 patterns**. **Tier-2 / Tier-3 catalog 확장 0건** (사용자 명시 금지 답습).

### 3.2 H-J / H-L 직접 등록 제외 답습 (R-4.1 §4.2)

R-4.1 의 H-J `_URL_WITH_QUERY_RE` / H-L `_FORM_BODY_RE` 직접 등록 제외 결정 답습 — alternation 변환 (Tier-1 alternation 2) 으로 *sensitive key 기반 정확한 매칭* 만 채택. **본 PoC 변경 0건**.

### 3.3 fake canary 의무 (사용자 명시)

본 PoC fixture 의 모든 secret 은 **fake canary** 의무. 사용자 명시 형식 답습:

```
sk-FAKE-GROUP-D-NOT-A-REAL-SECRET
AKIAFAKEGROUPDNOTREAL01           (16자 한정 — AKIA prefix 4 + canary marker 12)
ghp_FAKE_GROUP_D_NOT_REAL
R41T-fakecanary-D-not-real        (R-4.1 marker 답습)
```

**실 API key 사용 0건 의무** (사용자 명시 #1).

---

## 4. Fixture 사양 (9건 — 사용자 명시 최소 PoC 채택)

### 4.1 PASS fixture × 2 (D-1 — secret 부재 정상)

| 파일 | 내용 |
|------|------|
| `tests/fixtures/secret_hygiene/pass/safe_config.py` | `BASE_URL = "https://example.com"` + `MAX_RETRIES = 3` (ENV assignment 정상, prefix / regex / alternation 패턴 0건) |
| `tests/fixtures/secret_hygiene/pass/safe_settings.json` | `{"name": "alice", "email": "public@example.com", "page": 2}` (sensitive key 0건) |

**예상**: `secret_scanner --mode scan-source pass/` → rc=0 + 위반 0건 (FP 0).

### 4.2 FAIL fixture × 4 (D-1 — 4 패턴 cover 강제)

| 파일 | 패턴 cover | canary |
|------|----------|--------|
| `tests/fixtures/secret_hygiene/fail/env_assignment.py` | **prefix** (sk-) + **regex H-A** (ENV) | `OPENAI_API_KEY = "sk-FAKE-GROUP-D-NOT-A-REAL-SECRET"` |
| `tests/fixtures/secret_hygiene/fail/json_field.json` | **regex H-B** (JSON field 12 keys) | `{"api_key": "ghp_FAKE_GROUP_D_NOT_REAL"}` |
| `tests/fixtures/secret_hygiene/fail/private_key_block.pem` | **regex H-E** (Private key block) | `-----BEGIN RSA PRIVATE KEY-----\nfakekeydataR41T-fakecanary-D\n-----END RSA PRIVATE KEY-----` |
| `tests/fixtures/secret_hygiene/fail/prefix_aws.py` | **prefix** (AKIA, baseline) | `AWS_ACCESS_KEY = "AKIAFAKEGROUPDNOTREAL01"` |

**4 패턴 cover** (사용자 명시) = prefix (env_assignment + prefix_aws) + regex (json_field + private_key_block) + alternation (env_assignment 의 ENV regex 가 alternation 답습 trigger 가능) + private-key (private_key_block 단독).

**예상**: `secret_scanner --mode scan-source fail/` → rc=1 + ≥4 violations + 4 패턴 cover 검증.

### 4.3 REDACTION_PASS fixture × 1 (D-2 — redacted output 잔존 0)

| 파일 | 내용 |
|------|------|
| `tests/fixtures/secret_hygiene/redaction_pass/env_redacted.txt` | `OPENAI_API_KEY=[REDACTED]` + `AUTHORIZATION=[REDACTED]` (Tier-1 prefix / regex / alternation 패턴 0건) |

**예상**: `secret_scanner --mode scan-log redaction_pass/` → rc=0 + 잔존 0건.

### 4.4 REDACTION_FAIL fixture × 2 (D-2 — leak 검출)

| 파일 | leak 형태 |
|------|----------|
| `tests/fixtures/secret_hygiene/redaction_fail/partial_redact.txt` | `OPENAI_API_KEY=sk-FAK[REDACTED]` (앞 5글자 잔존 — partial leak) |
| `tests/fixtures/secret_hygiene/redaction_fail/base64_evasion.txt` | `c2stRkFLRS1HUk9VUC1ELU5PVC1BLVJFQUwtU0VDUkVU` (base64 of `sk-FAKE-GROUP-D-NOT-A-REAL-SECRET`) — **known limitation** 표기 (사양 §8) |

**예상**:
- partial_redact.txt → rc=1 (prefix `sk-FAK` 잔존 검출)
- base64_evasion.txt → 본 PoC validator 는 **검출 불가** (regex 직접 매칭 한정) — 의도된 *known limitation*. 본 fixture 는 *후속 검증 시제* 로 보존, 본 PoC PASS 차단 조건 아님.

→ D-2 FAIL fixture 합산: rc=1 (partial leak 검출) + base64 leak 미검출 (known limitation, 본 PoC 차단 조건 외).

---

## 5. 검증 매트릭스 (CI workflow + 로컬 명령)

### 5.1 7 검증 항목 (사용자 명시 답습)

| # | 검증 | 입력 | 명령 | 예상 rc | 예상 결과 |
|---|------|------|------|---------|----------|
| 1 | D-1 PASS scan | `pass/` | `python tools/secret_scanner.py --mode scan-source tests/fixtures/secret_hygiene/pass/` | 0 | 위반 0건 (FP 0) |
| 2 | D-1 FAIL scan | `fail/` | `python tools/secret_scanner.py --mode scan-source tests/fixtures/secret_hygiene/fail/` | 1 | ≥4 violations + 4 패턴 cover (prefix / regex / alternation / private-key) |
| 3 | D-2 PASS redaction residual scan | `redaction_pass/` | `python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_pass/` | 0 | 잔존 0건 |
| 4 | D-2 FAIL redaction leak scan | `redaction_fail/` | `python tools/secret_scanner.py --mode scan-log tests/fixtures/secret_hygiene/redaction_fail/` | 1 | partial leak 검출 (base64 미검출 = known limitation) |
| 5 | Tier-1 pattern count 자기 검증 | `--list-patterns` | `python tools/secret_scanner.py --list-patterns` | 0 | `registered_patterns_count` ≥ 42 (R-4.1 답습) + Tier-1 prefix 31 + regex 7 + alternation 2 enumerate |
| 6 | F-금지 자기 검증 (CI step grep) | scanner / fixture / workflow | grep `sk-(?!FAKE)` / `AKIA(?!FAKE)` / `ghp_(?!FAKE)` 검출 | 0 | 0 (실 API key 0건) |
| 7 | summary.json + artifact + evidence summary | step output | `Build summary.json` step + `actions/upload-artifact@v4` `group-d-logs/` + `$GITHUB_STEP_SUMMARY` | — | 9 파일 artifact (7 step log + summary.json) + 13 항목 evidence summary |

**합산 7 검증 (D-1 PASS + D-1 FAIL + D-2 PASS + D-2 FAIL + Tier-1 count + F-금지 grep + summary.json/artifact/evidence)**.

---

## 6. 답습 매핑 (R-4.1 + Group A/B/C/F)

### 6.1 R-4.1 답습 영역

| Group D 영역 | R-4.1 답습 | 신규 작성 |
|---|---|---|
| Tier-1 42 catalog | `docker/r4-1-poc/r4_1_poc.py` line 53~228 답습 (변경 0건) | 0 |
| canary marker convention (`R41T-fakecanary-D-not-real`) | R-4.1 §5 canary marker 답습 | 0 |
| 45 patterns 등록 (Prefix 36 + regex 7 + alternation 2) | R-4.1 §4.1 답습 (변경 0건) | 0 |
| H-J/H-L 직접 등록 제외 + alternation 채택 | R-4.1 §4.2 답습 | 0 |
| violation reporter 형식 (id / source / category / vendor / detail) | R-4.1 §5.1 답습 | 0 |
| Custom scanner 본 PoC 신규 (~250줄) — 2 mode CLI + violation 집계 + Tier-1 count 자기 검증 | — | ~250 |
| 9 fixture (PASS 2 + FAIL 4 + REDACTION_PASS 1 + REDACTION_FAIL 2) | — | 9 |
| reference 토이 redactor (D-2 검증 보조) | — | (선택) ~30줄 — fixture 내장 또는 별도 함수 |

**리팩토링 0건** (R-4.1 patterns 직접 복사 답습).

### 6.2 Group A/B/C/F 형식 답습

| 영역 | Group 답습 |
|---|---|
| Validator 구조 (argparse + dataclass + 2 mode) | Group A 1차 + Group B + Group F |
| Fixture 디렉토리 구조 (`pass/` + `fail/`) | Group A 1차 + Group B |
| CI workflow (4 검증 step + summary.json + artifact + Evidence summary) | Group F (12 step) |
| Reviewer-only 단축 합의 형식 | Group A 1차 + Group B + Group F |
| artifact path (leading dot 미사용) | Group F 후속 (`group-d-logs/`) |
| ADR-011 §2.1 (a)~(e) 5/5 충족 매트릭스 | Group A 1차/2차 + Group B + Group C + Group F |

---

## 7. PASS 기준 자기 검증 매트릭스 (사용자 명시 7 검증 답습)

| # | PASS 기준 | 본 PoC 충족 |
|---|----------|------------|
| 1 | D-1 PASS scan | rc=0 + 위반 0건 (FP 0) |
| 2 | D-1 FAIL scan | rc=1 + ≥4 violations + 4 패턴 cover |
| 3 | D-2 PASS redaction residual scan | rc=0 + 잔존 0건 |
| 4 | D-2 FAIL redaction leak scan | rc=1 + partial leak 검출 (base64 = known limitation, PASS 차단 외) |
| 5 | Tier-1 pattern count 자기 검증 | `--list-patterns` 출력 시 `registered_patterns_count ≥ 42` |
| 6 | F-금지 자기 검증 | grep 결과 = 0건 (실 API key 부재) |
| 7 | summary.json + artifact + evidence summary | summary.json 7 항목 + artifact 9 파일 + Evidence summary 13 항목 |

**합산 7/7 충족 적격**.

---

## 8. 알려진 한계 (의도된 분리)

| # | 한계 | 분리 이유 | 미래 영역 |
|---|------|----------|----------|
| 1 | base64 / URL-encoded / 압축 등 advanced evasion 미커버 | 본 PoC = R-4.1 직접 prefix + regex + alternation 매칭 한정 | Hermes upstream R2-6 영역 (`tests/hermes/redaction/test_base64_evasion.py`) — 별도 합의 |
| 2 | Hermes 컨테이너 chmod 600 / entrypoint stat / inotify | 사용자 명시 #6 — Hermes upstream 영역 (R1-2, ADR-008 §A.2) | 별도 합의 (ADR-010 Vault HSM 영역) |
| 3 | git pre-commit hook 실 활성화 | 사용자 명시 #7 — T2 정책 영역 | 별도 합의 |
| 4 | PR auto-reject GitHub branch protection | 사용자 명시 #8 — T3 정책 영역 | 별도 합의 |
| 5 | log file canary inject + grep nightly | R-6 workflow 확장 영역 | 별도 합의 (R-7 SOP §5 ROLLBACK trigger R5 답습) |
| 6 | LLM API request body 실 송신 redaction | P1 facade RedactionFilter | 별도 합의 |
| 7 | Tier-2 / Tier-3 catalog 확장 (Slack / GCP / Azure 등) | 사용자 명시 — 별도 합의 (gitleaks/detect-secrets 도입 시점 결정) | 풀 3+1 합의 + 외부 LLM 1+ |
| 8 | gitleaks / detect-secrets 도구 도입 | 사용자 명시 풀 3+1 trigger #4 위험 회피 | 별도 합의 |
| 9 | Reference 토이 redactor 본문 변경 시 | redactor 변경 = redaction 정책 완화 trigger #3 발화 가능 | 별도 합의 |
| 10 | 18 fixture 확장안 (8 패턴 모두 cover) | 본 PoC = 9 fixture 최소 한정 (사용자 명시) | 후속 후보 (별도 합의) — 사양 §1.1 #3~#5 fixture 확장 |

**18 fixture 확장 후보 (참고만, 본 PoC 미진입)**:

```
PASS:  safe_config.py + safe_settings.json + safe_header.txt + safe_url.txt
FAIL:  env_assignment + json_field + auth_header + private_key + db_connstr +
       url_query + body_form + prefix_aws
REDACTION_PASS:  env_redacted + json_redacted + header_redacted
REDACTION_FAIL:  env_leak + partial_redact + base64_evasion
```

본 PoC = **9 fixture 한정** (사용자 명시 답습).

---

## 9. CI workflow 설계

### 9.1 12 step 구조 (Group F 답습 형식)

| # | Step | 책무 |
|---|------|------|
| 1 | Checkout | actions/checkout@v4 |
| 2 | Set up Python | actions/setup-python@v5 (3.12) |
| 3 | Prepare log directory | `mkdir -p group-d-logs` (Group F 후속 답습 — leading dot 미사용) |
| 4 | D-1 PASS — secret_scanner --mode scan-source pass/ | rc=0 + 위반 0건 grep |
| 5 | D-1 FAIL — secret_scanner --mode scan-source fail/ | rc=1 + ≥4 violations + 4 패턴 cover grep (prefix / regex / alternation / private-key) |
| 6 | D-2 PASS — secret_scanner --mode scan-log redaction_pass/ | rc=0 + 잔존 0건 grep |
| 7 | D-2 FAIL — secret_scanner --mode scan-log redaction_fail/ | rc=1 + partial leak 검출 grep (base64 미검출 = known limitation) |
| 8 | Tier-1 pattern count 자기 검증 — `--list-patterns` | `registered_patterns_count ≥ 42` grep |
| 9 | F-금지 자기 검증 (Layer 1 grep) | 실 API key 부재 grep (`sk-(?!FAKE)` / `AKIA(?!FAKE)` / `ghp_(?!FAKE)` ≥ 1 hit 시 `::error::` + exit 1) |
| 10 | Build summary.json | step output 집계 → `group-d-logs/summary.json` |
| 11 | Upload feasibility logs (artifact) | `actions/upload-artifact@v4` `group-d-logs/` retention 30일 |
| 12 | Evidence summary | `$GITHUB_STEP_SUMMARY` 13 항목 |

**artifact path = `group-d-logs/`** (Group F 후속 답습 — leading dot 미사용, `include-hidden-files: false` default 정책 미의존).

### 9.2 paths trigger

```yaml
paths:
  - tools/secret_scanner.py
  - tests/fixtures/secret_hygiene/**
  - .github/workflows/secret-hygiene-egress-redaction.yml
```

---

## 10. 풀 3+1 승격 trigger 자기 검증 (사용자 명시 7 trigger)

| # | Trigger | 본 PoC 발화 | 자기 검증 |
|---|---------|-----------|----------|
| 1 | 실제 secret 처리 정책 변경 필요 | ❌ 미발화 | fake canary 한정, 정책 변경 0건 |
| 2 | R-4 Tier-1 catalog 변경 필요 | ❌ 미발화 | 답습만 (R-4.1 §4.1 직접 복사, 변경 0건) |
| 3 | redaction 정책 완화 필요 | ❌ 미발화 | Tier-1 42 catalog 답습 (완화 0건) |
| 4 | gitleaks / detect-secrets 도구 선택 장기 정책 고정 | ❌ 미발화 | 도구 도입 0건 (custom scanner 단독, §2.1 답습) |
| 5 | false positive가 정상 개발 흐름을 과도하게 막음 | ❌ 미발화 | fixture 한정, dev flow 영향 0 |
| 6 | false negative로 secret 누출 가능성 잔존 | ⚠️ 부분 — base64 evasion 1건 *known limitation* (Hermes upstream R2-6 영역 명시 분리) | 본 한계 = §8 #1 분리 명시, 본 PoC 차단 조건 아님 |
| 7 | ADR-010 / ADR-011 / ADR-012 와 충돌 | ❌ 미발화 | cross-reference 답습 한정 |

**합산 0/7 발화 (#6 부분 발화는 known limitation 명시 분리 → 풀 3+1 미발화 적격)** → **Reviewer-only 단축 합의 적격**.

---

## 11. Evidence 형식 (5종 — Group A/B/C/F 답습)

| Evidence | 형식 | 본 PoC 산출 |
|---|---|---|
| Markdown report | 본 사양 (`docs/phase0/g2-gp3-gp2-...`) | 본 문서 |
| JSONL ledger entry | secret_scanner 결과 evidence summary (옵션, ADR-012 §2.9 답습 — 본 PoC 미강제) | summary.json (단순화) |
| 격리 검증 | fixture 한정 + 실 secret 0건 + custom scanner 단독 (외부 의존 0건) | F-금지 grep step 자동 강제 |
| GitHub Actions run | actual run id / duration / step PASS 매트릭스 | `secret-hygiene-egress-redaction.yml` 실행 결과 |
| 합의 보고서 | Reviewer-only 단축 (`docs/review/3plus1-consensus-2026-05-10-g2-gp3-gp2-...`) | 본 PoC 산출물 #8 |

---

## 12. 변경 이력

| 일자 | 변경 | 비고 |
|------|------|------|
| 2026-05-10 | 신규 작성 (DRAFT) | Group D 진입 사양 — 사용자 명시 12 금지 / 7 trigger / 7 PASS / 4 도구 옵션 / 9 fixture / 45 patterns / base64 limitation. Group A 1차/2차 + Group B + Group C + Group F 사양 형식 직접 답습. R-4.1 Tier-1 42 catalog (`docker/r4-1-poc/r4_1_poc.py` line 53~228) 직접 답습 (변경 0건). custom scanner 단독 채택 (gitleaks/detect-secrets 0건). artifact path `group-d-logs/` (Group F 후속 답습, leading dot 미사용). |
