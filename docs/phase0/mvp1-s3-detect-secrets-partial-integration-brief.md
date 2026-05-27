# MVP-1 S-3 detect-secrets 부분 통합 실 구현 sub-cycle brief

> **scope**: MVP-1 1.5차 보강 entry 합의 (24번째 entry, commit `9638521`) 의 **S-3 detect-secrets 부분 통합 실 구현 sub-cycle**. 본 sub-cycle = entry 합의 결정 *집행* (S-3 채택 결정 + plugin catalog 본문 채택 자체는 entry cycle 에서 완료).
>
> **본 brief 자체에서 실 코드 / CI workflow / hook 본문 변경 0건 의무** — brief 합의 발효 *후* 별도 실 구현 단계에서 file 생성/수정.

---

## §0 답습 출처 (인용 source)

| Source | 위치 | 답습 내용 |
|---|---|---|
| **24번째 entry brief v1.1** | `docs/phase0/mvp1-1.5th-reinforcement-entry-brief.md` (commit `9638521`) | §2.1 S-3 정의 (line 121~149) + §3 ADR-011 (a)~(e) 매트릭스 (S-3 cell) + §4 합의 형태 권고 (line 290 "단축 합의 + 사용자 명시") + §5.1 Rollback Trigger R-MVP1-1.5-S3-{1,2,3} (line 323~325) + §6 Evidence 행 (line 341~345) |
| **24번째 entry 합의 보고서** | `docs/review/3plus1-consensus-2026-05-27-mvp1-1.5th-reinforcement-entry.md` | R-4 BLOCKING (S-3 plugin identifier 정확 mapping + `--baseline` 미사용 CI assertion) + S-3 = APPROVE w/ COND 격상 |
| **roadmap-mvp1** | §3.6.3 line 289 | "MVP-1 1.5차 (S-3 detect-secrets 부분 통합) \| **풀 3+1 합의 + 외부 LLM 1+** \| Tier-2/3 catalog 확장 영역" |
| **Group D PoC** | §2.1 (D) sub-수단 #5 | "detect-secrets baseline silenceable risk 명시" → R-MVP1-1.5-S3-2 본 sub-cycle 영구 금지 명문 발효 |
| **ADR-011** | `docs/decisions/ADR-011-means-vs-ends-redaction.md` | §2.1 (a)~(d) + (e) 5조건 + §2.4 T2/T3 영역 |
| **secret_scanner.py (S-1)** | `tools/secret_scanner.py` (368줄, Tier-1 45 patterns) | S-3 = *추가* layer (S-1 답습 유지, 미대체, Defense in depth) |
| **PC-1-T3 sub-cycle 답습** | `docs/phase0/mvp1-pc1-t3-mandatory-enforcement-brief.md` + 합의 (`3a63a5b`) | 단축 합의 패턴 + 단계별 6단계 cycle + 변경 0건 의무 매트릭스 답습 |

---

## §1 scope (S-3 sub-cycle 한정)

### 1.1 본 sub-cycle 의 본질

| 항목 | 내용 |
|---|---|
| **scope** | S-3 detect-secrets 부분 통합 실 구현 (entry 합의 결정 *집행*) |
| **영역** | GP-3 Tier-1 답습 plugin 한정 (Tier-2/3 catalog 확장 영역 아님) |
| **합의 형태 권고** | **단축 합의 + 사용자 명시** (entry brief line 290 답습) — PC-1-T3 패턴 답습 |
| **변경 0건 의무** | `tools/secret_scanner.py` 본문 변경 0건 (S-1 답습 유지) / `.pre-commit-config.yaml` 본문 변경 0건 / src/ 0건 / ADR 0건 / 헌법 0건 / roadmap 본문 0건 / Tier-2/3 catalog 0건 (Tier-1 답습 plugin 한정) / baseline file 영구 금지 |
| **변경 허용 영역** | `requirements-dev.txt` (`detect-secrets` 추가) + `.github/workflows/secret-hygiene-egress-redaction.yml` (step 추가 + `on.push.paths` 추가) + `tests/fixtures/secret_hygiene/mvp1_s3/` 신규 (testfile evidence) + (선택) `tools/detect_secrets_run.sh` wrapper (D-3 결정) |

### 1.2 본 sub-cycle 이 *하지 않는* 것 (변경 0건 의무)

| # | 항목 | 변경 자격 |
|---|---|---|
| 1 | `tools/secret_scanner.py` 본문 변경 (S-1 답습 유지) | 0건 (R-MVP1-1.5-S3-3 영구 금지 답습 — Defense in depth) |
| 2 | `.pre-commit-config.yaml` 본문 변경 (S-3 = CI 영역 한정, pre-commit hook 영역 0건) | 0건 |
| 3 | `.githooks/pre-commit` 본문 변경 | 0건 |
| 4 | src/ 본문 변경 | 0건 |
| 5 | tools/ 기존 21 도구 본문 변경 | 0건 (`detect_secrets_run.sh` 신규 = D-3 결정 영역, 신규 추가 ≠ 본문 변경) |
| 6 | Tier-2 / Tier-3 catalog 본문 확장 (S-3 plugin Slack/GCP/Azure/등 추가) | 0건 (R-MVP1-1.5-S3-1 풀 3+1 trigger 답습 — 본 sub-cycle = Tier-1 답습 plugin 한정) |
| 7 | baseline file 도입 (`--baseline <baseline>.json`) | 0건 (R-MVP1-1.5-S3-2 영구 금지 답습 — silenceable risk) |
| 8 | S-1 step 제거 / 대체 | 0건 (R-MVP1-1.5-S3-3 영구 금지 답습 — Defense in depth) |
| 9 | branch protection rule 변경 (AR-3 sub-cycle 영역) | 0건 |
| 10 | ADR / 헌법 / roadmap 본문 변경 | 0건 |
| 11 | MVP-1 Implementation Evidence PASS 발효 | 0건 ((c) carry-over 영역) |
| 12 | `adapters/llm/facade.py` placeholder → real | 0건 ((d) carry-over 영역) |

---

## §2 24번째 entry BLOCKING + 권고 흡수 매트릭스

| ID | 항목 | 본 brief 흡수 위치 |
|---|---|---|
| **R-4** BLOCKING | S-3 plugin allowlist = detect-secrets CLI 실 plugin identifier 정확 mapping (`AWSKeyDetector` / `KeywordDetector` / `Base64HighEntropyString` / `HexHighEntropyString` / `PrivateKeyDetector`) + `--baseline` 미사용 CI assertion 명시 (CI step 본문 `--baseline` 검출 시 fail) | §4.2 plugin allowlist 명문 + §4.3 `--baseline` 미사용 assertion 명문 |
| **권고** | S-3 APPROVE w/ COND 격상 (entry 합의 §1 line 36 답습) — 본 sub-cycle = COND 해소 (R-4 BLOCKING 흡수 시점 + 본 sub-cycle 발효 시점) | 본 brief 전체 |

### 1.3 plugin allowlist hardcoded list (R-4 BLOCKING 본문 채택)

**Tier-1 답습 plugin 정확 mapping** (detect-secrets CLI 실 인식 plugin name):

| # | Plugin name (CLI) | 검출 대상 | Tier-1 답습 source |
|---|---|---|---|
| 1 | `AWSKeyDetector` | AWS access key (AKIA / ASIA prefix) | Tier-1 catalog `aws_access_key` 답습 |
| 2 | `KeywordDetector` | API key / token / password keyword | Tier-1 catalog `keyword_assignment` 답습 |
| 3 | `Base64HighEntropyString` | Base64 encoded high entropy string | Tier-1 catalog `base64_high_entropy` 답습 |
| 4 | `HexHighEntropyString` | Hex encoded high entropy string | Tier-1 catalog `hex_high_entropy` 답습 |
| 5 | `PrivateKeyDetector` | RSA/SSH private key (`-----BEGIN` marker) | Tier-1 catalog `private_key_pem` 답습 |

**제외** (Tier-2/3 확장 영역, R-MVP1-1.5-S3-1 풀 3+1 trigger):
- `SlackDetector` / `GoogleDetector` / `AzureDetector` / `StripeDetector` / `IbmDetector` / `MailchimpDetector` / `JwtDetector` / etc.

---

## §3 현 상태 audit

### 3.1 이미 발효 (답습 영역)

| 자료 | 상태 | source |
|---|---|---|
| `tools/secret_scanner.py` (S-1, 368줄, Tier-1 45 patterns) | ✅ 발효 (Group D PoC) | R-MVP1-1.5-S3-3 답습 유지 의무 (Defense in depth) |
| `.github/workflows/secret-hygiene-egress-redaction.yml` (694줄, `scan` job) | ✅ 발효 | S-1 step 11+ 다수 발효 |
| `tests/fixtures/secret_hygiene/{pass,fail,mvp1_entry,redaction_pass,redaction_fail}/` | ✅ 발효 | D-1/D-2 fixture 다수 |
| `requirements-dev.txt` (5 패키지) | ✅ 발효 | import-linter / rfc8785 / jcs / pytest / pytest-cov / pre-commit==4.0.1 (PC-1 sub-cycle 신규) |

### 3.2 미충족 (본 sub-cycle 발효 대상)

| # | 항목 | 현 상태 | 본 sub-cycle 발효 |
|---|---|---|---|
| 1 | `detect-secrets` 패키지 설치 | 부재 | `requirements-dev.txt` 추가 (D-4 결정 — 버전 pin) |
| 2 | workflow step (detect-secrets scan) | 부재 (detect-secrets 언급 line 692 = 0건 명시 한정) | secret-hygiene-egress-redaction.yml 신규 step 추가 (D-2 결정 — 위치) |
| 3 | plugin allowlist hardcoded (R-4 BLOCKING) | 부재 | step 본문 5 plugin 명시 (§1.3 본문 채택 답습) |
| 4 | `--baseline` 미사용 CI assertion (R-4 BLOCKING) | 부재 | step 본문 `grep --baseline` 검출 시 fail assertion |
| 5 | Tier-1 catalog testfile evidence | 부재 | `tests/fixtures/secret_hygiene/mvp1_s3/` 신규 (D-5 결정 — 디렉토리명) |
| 6 | `on.push.paths` 필터 (메모리 "Actual run trigger paths 필터" 답습) | 14 entry | detect-secrets 관련 file 추가 (workflow 자체 / fixture / wrapper) |

### 3.3 S-3 vs S-1 관계 (Defense in depth, R-MVP1-1.5-S3-3 답습)

| 항목 | S-1 (`tools/secret_scanner.py`) | S-3 (`detect-secrets`) |
|---|---|---|
| 영역 | Tier-1 45 custom patterns | Tier-1 답습 plugin 5종 (§1.3 본문 채택) |
| 운영 | 답습 유지 (`R-MVP1-1.5-S3-3` 영구 금지 = 제거/대체) | *추가* layer (S-1 미대체) |
| baseline | 0건 (custom 답습) | **0건 영구 금지** (R-MVP1-1.5-S3-2 = silenceable risk) |
| workflow step | 11+ step 발효 | 1 step 신규 추가 (본 sub-cycle) |

→ **Defense in depth 답습**: S-3 발효 = S-1 위 추가 layer, 양 도구 모두 PASS 의무 (rc=0 + violations=0)

---

## §4 실 구현 5 항목

### 4.1 `requirements-dev.txt` `detect-secrets` 추가

```python
# S-3 detect-secrets 부분 통합 (MVP-1 1.5차 보강 sub-cycle)
# 답습 출처:
#   - docs/phase0/mvp1-s3-detect-secrets-partial-integration-brief.md
#   - docs/review/3plus1-consensus-2026-05-27-mvp1-s3-detect-secrets-partial-integration.md
# Tier-1 답습 plugin 5종 한정 (Tier-2/3 확장 = R-MVP1-1.5-S3-1 풀 3+1 trigger)
# --baseline 미사용 영구 금지 (R-MVP1-1.5-S3-2)
detect-secrets==<버전>  # D-4 결정
```

### 4.2 workflow step (plugin allowlist hardcoded, R-4 BLOCKING 흡수)

위치: `.github/workflows/secret-hygiene-egress-redaction.yml` `jobs.scan.steps[]` (D-2 결정 — 후보)

```yaml
- name: S-3 detect-secrets scan — Tier-1 답습 plugin 5종 (R-4 BLOCKING 본문 채택)
  id: s3_detect_secrets
  run: |
    set +e
    # plugin allowlist hardcoded (§1.3 본문 채택, Tier-1 답습 한정)
    detect-secrets scan \
      --disable-plugin ArtifactoryDetector \
      --disable-plugin AzureStorageKeyDetector \
      --disable-plugin BasicAuthDetector \
      --disable-plugin CloudantDetector \
      --disable-plugin DiscordBotTokenDetector \
      --disable-plugin GitHubTokenDetector \
      --disable-plugin IbmCloudIamDetector \
      --disable-plugin IbmCosHmacDetector \
      --disable-plugin JwtTokenDetector \
      --disable-plugin MailchimpDetector \
      --disable-plugin NpmDetector \
      --disable-plugin OpenAIDetector \
      --disable-plugin PypiTokenDetector \
      --disable-plugin SendGridDetector \
      --disable-plugin SlackDetector \
      --disable-plugin SoftlayerDetector \
      --disable-plugin SquareOAuthDetector \
      --disable-plugin StripeDetector \
      --disable-plugin TelegramBotTokenDetector \
      --disable-plugin TwilioKeyDetector \
      tests/fixtures/secret_hygiene/mvp1_s3/ \
      > group-d-logs/s3-detect-secrets.json 2> group-d-logs/s3-detect-secrets.stderr
    rc=$?
    set -e
    # ... evidence verify
```

**또는** (D-3 결정 시 wrapper 채택): `bash tools/detect_secrets_run.sh tests/fixtures/secret_hygiene/mvp1_s3/`

### 4.3 `--baseline` 미사용 CI assertion (R-4 BLOCKING 흡수)

```yaml
- name: S-3 --baseline 미사용 assertion (R-MVP1-1.5-S3-2 영구 금지 답습)
  run: |
    set -e
    # workflow 본문에 --baseline 사용 시 fail (silenceable risk 차단)
    if grep -n -E '\-\-baseline\b' .github/workflows/secret-hygiene-egress-redaction.yml; then
      echo "::error::R-MVP1-1.5-S3-2 위반 — --baseline 사용 검출 (영구 금지, silenceable risk)"
      exit 1
    fi
    echo "[OK] --baseline 미사용 assertion PASS (R-MVP1-1.5-S3-2 답습)"
```

### 4.4 `tests/fixtures/secret_hygiene/mvp1_s3/` 신규 testfile

| 파일 | 내용 | 목적 |
|---|---|---|
| `pass/clean.py` | 평범 코드 (secret 0건) | S-3 PASS evidence (false positive 0) |
| `fail/aws_key.py` | `AKIAFAKES3NOTREAL01` (fake canary) | `AWSKeyDetector` 검출 evidence |
| `fail/keyword.py` | `API_KEY = "sk-FAKES3NOTAREALSECRET"` | `KeywordDetector` 검출 evidence |
| `fail/base64_entropy.py` | high entropy Base64 string | `Base64HighEntropyString` 검출 evidence |
| `fail/hex_entropy.py` | high entropy Hex string | `HexHighEntropyString` 검출 evidence |
| `fail/private_key.py` | `-----BEGIN RSA PRIVATE KEY-----` (fake) | `PrivateKeyDetector` 검출 evidence |

**fake canary 의무** — 모든 fail fixture = "NOTAREAL" / "FAKE" / "CANARY" marker 포함 (Group D PoC 답습)

### 4.5 (선택) `tools/detect_secrets_run.sh` wrapper (D-3 결정 시)

```bash
#!/bin/bash
# S-3 detect-secrets wrapper — plugin allowlist hardcoded + --baseline 미사용 의무
# 답습: brief §1.3 본문 채택 (Tier-1 답습 plugin 5종 한정)
set -e

TARGET="${1:-tests/fixtures/secret_hygiene/mvp1_s3/}"

# Tier-1 답습 plugin 한정 (다른 plugin 모두 --disable-plugin)
detect-secrets scan \
  --disable-plugin ArtifactoryDetector \
  --disable-plugin AzureStorageKeyDetector \
  ... (§4.2 동일 list)
  "$TARGET"
```

---

## §5 ADR-011 §2.1 (a)~(e) 5/5 매트릭스 (S-3 본 sub-cycle 한정)

| 조건 | 본 sub-cycle 충족 |
|---|---|
| **(a)** 사용자 명시 결정 | ⏳ 본 brief 사용자 승인 + D-1~D-5 결정 시 충족 |
| **(b)** 격리 환경 PoC 실증 | ⏳ 본 sub-cycle 발효 시 `tests/fixtures/secret_hygiene/mvp1_s3/` PoC + workflow step actual run id evidence |
| **(c)** 도구/리소스 stateless · network-free | ✅ detect-secrets = stateless scanner (network 0), Provider Liquidity 답습 |
| **(d)** 자동 회귀 검증 경로 | ⏳ 본 sub-cycle 발효 시 `secret-hygiene-egress-redaction.yml` step 통합 + nightly run + `--baseline` 미사용 assertion (R-4 흡수) |
| **(e)** 합의 APPROVE 운영조건 | ⏳ 본 brief 합의 (단축 합의 + 사용자 명시 권고) APPROVE 시 발효 |

→ **현 시점 충족 = (c) 만** → 본 sub-cycle 합의 발효 + 실 구현 단계 완료 = (a)~(e) 5/5 충족 (S-3 영역 한정)

---

## §6 Rollback Trigger (본 sub-cycle 적용 형태)

| ID | trigger | 본 sub-cycle 발효 형태 |
|---|---|---|
| **R-MVP1-1.5-S3-1** | detect-secrets plugin 활성화 추가 (Tier-2/3 vendor — Slack/GCP/Azure 등) | **풀 3+1 합의 + 외부 LLM 1+ + 사용자 명시** (Tier-2/3 catalog 확장 영역 답습) |
| **R-MVP1-1.5-S3-2** | baseline file 도입 시도 (`--baseline <baseline>.json`) | **영구 금지** (본 sub-cycle 본문 채택 — 합의 변경 = 풀 3+1) → §4.3 CI assertion 발효 |
| **R-MVP1-1.5-S3-3** | S-1 (`tools/secret_scanner.py`) 답습 step 제거 / 대체 시도 | **영구 금지** (Defense in depth 답습) |

---

## §7 Evidence

| Evidence | 형식 | 본 sub-cycle 발효 |
|---|---|---|
| **(a) Markdown report** | `docs/phase0/g2-gp3-mvp1-evidence.md` 보강 (S-3 영역 추가) | 별도 sub-cycle 또는 본 sub-cycle 확장 결정 |
| **(b) PoC 실증** | `tests/fixtures/secret_hygiene/mvp1_s3/` + local `detect-secrets scan` 격리 결과 + plugin 5종 검출 evidence | 본 sub-cycle 실 구현 단계 발효 |
| **(c) Docker isolation log** | detect-secrets scanner stateless · network-free (도구 본질) | (c) 답습 발효 자격 |
| **(d) GitHub Actions run** | `secret-hygiene-egress-redaction.yml` S-3 step actual run id + nightly run id (`gh run list` 답습) | 본 sub-cycle 실 구현 단계 발효 |
| **(e) 합의 보고서** | 본 sub-cycle 합의 보고서 (단축 합의 권고) | 본 brief 합의 발효 |

---

## §8 사용자 결정 항목 (brief 합의 진입 전 의무)

| # | 항목 | 후보 | 권고 |
|---|---|---|---|
| **D-1** | 합의 형태 | (i) 단축 합의 (Reviewer-only) / (ii) 풀 3+1 / (iii) 풀 3+1 + 외부 LLM 1+ | **(i) 단축 합의 (Reviewer-only)** — entry brief line 290 답습 + entry cycle 에서 S-3 채택 결정 + plugin catalog 본문 채택 완료, 본 sub-cycle = 결정 *집행*, PC-1-T3 sub-cycle 패턴 답습 (`3a63a5b`) |
| **D-2** | workflow step 위치 | (i) `Tier-1 pattern count` step 직후 (line 97) / (ii) 마지막 `MVP-1 entry secret_scanner coverage check` step 직후 (line 287) / (iii) 신규 별도 job | **(ii) MVP-1 entry step 직후** — S-1 답습 step 들 모두 통과 후 S-3 추가 layer (Defense in depth 답습 순서) |
| **D-3** | wrapper 스크립트 도입 | (A) `tools/detect_secrets_run.sh` wrapper 신규 (재사용성 ↑) / (B) workflow 직접 호출 (단순, wrapper 0) | **(B) workflow 직접 호출** — Ceremony 최소화 + tools/ 신규 0건 (Tier-1 plugin allowlist = workflow step 본문에 hardcoded, 단일 source-of-truth) |
| **D-4** | `detect-secrets` 버전 | (i) `==1.5.0` (최신 stable) / (ii) `==1.4.0` (보수적) / (iii) `>=1.4,<2` (범위) | **(i) `==1.5.0` 정확 pin** — pre-commit==4.0.1 답습 패턴 (정확 version pin, requirements-dev.txt 답습) |
| **D-5** | testfile 디렉토리명 | (i) `tests/fixtures/secret_hygiene/mvp1_s3/` / (ii) `tests/fixtures/secret_hygiene/s3_detect_secrets/` / (iii) `tests/fixtures/secret_hygiene/mvp1_1_5_s3/` | **(i) `mvp1_s3/`** — 기존 `mvp1_entry/` 패턴 답습 (간결, MVP-1 그룹 답습) |

---

## §9 합의 형태 권고 + 다음 단계

### 9.1 합의 형태 권고

**단축 합의 (Reviewer-only)** 권고 — 근거 (PC-1-T3 sub-cycle 패턴 답습):

| 근거 | 내용 |
|---|---|
| **entry brief line 290** | "단축 합의 + 사용자 명시 (사용자 명시 결정 1회). 본 cycle 합의 = 수단 결정 + plugin catalog 본문 채택 발효. 실 구현 sub-cycle = workflow step 추가 + plugin 활성화 hardcoded list = 본 cycle 결정 *집행*" |
| **entry cycle 완료** | S-3 채택 결정 + APPROVE w/ COND (R-4 BLOCKING 흡수) 자체는 24번째 entry cycle (`9638521`) 에서 완료. 본 sub-cycle = 결정 *집행* + COND 해소 |
| **변경 0건 의무** | `tools/secret_scanner.py` (S-1) / `.pre-commit-config.yaml` / src / 기존 tools 21 도구 본문 모두 0건. 변경 = `requirements-dev.txt` + workflow step + testfile + (선택) wrapper 한정 |
| **풀 3+1 승격 trigger** | 5/5 모두 발화 0건 (① 새 권위 결정 0 [S-3 채택 = entry cycle] / ② Tier-2/3 catalog 자동 확장 0 [Tier-1 답습 plugin 한정] / ③ Implementation Evidence PASS 자동 선언 0 / ④ 후속 합의 본문 변경 0 / ⑤ ADR-011 §2.1 5조건 자동 충족 선언 0) |
| **PC-1-T3 답습** | PC-1 sub-cycle (`3a63a5b`) Reviewer-only 단축 합의 패턴 답습 |
| **메모리 답습** | "Ceremony 인플레이션 차단" — Reviewer-only 단축 합의 영역 |

### 9.2 다음 단계 (단계별 합의 cycle 6단계 답습)

1. ✅ **brief 작성** (본 단계, 본 commit)
2. ⏳ **사용자 승인** — §8 D-1~D-5 사용자 결정 의무
3. ⏳ **단축 합의** — Reviewer-only 합의 보고서 작성 (5/5 풀 3+1 승격 trigger 발화 검증)
4. ⏳ **실 구현** — §4 5 항목 file 생성/수정
5. ⏳ **commit** — 본 sub-cycle 정리 commit (SESSION + INDEX + 본 commit)
6. ⏳ **push** — 사용자 명시 의무 답습

---

## §10 본 brief 자기진단 (8/8 통과 의무)

| # | 항목 | 통과 |
|---|---|---|
| 1 | 본 brief 자체 실 코드 / CI workflow / hook 본문 변경 0건 | ✅ brief 작성 한정 |
| 2 | `tools/secret_scanner.py` (S-1) 답습 유지 명문 (R-MVP1-1.5-S3-3 영구 금지) | ✅ §1.2 #1 + §3.3 |
| 3 | baseline file 영구 금지 명문 (R-MVP1-1.5-S3-2) | ✅ §1.2 #7 + §4.3 + §6 |
| 4 | plugin allowlist Tier-1 답습 한정 명문 (R-MVP1-1.5-S3-1 풀 3+1 trigger) | ✅ §1.2 #6 + §1.3 + §6 |
| 5 | R-4 BLOCKING 흡수 (plugin identifier 정확 mapping + `--baseline` 미사용 assertion) | ✅ §2 + §4.2 + §4.3 |
| 6 | Defense in depth 명문 (S-1 + S-3 양 layer) | ✅ §3.3 |
| 7 | ADR-011 (a)~(e) 매트릭스 발효 자격 명시 | ✅ §5 |
| 8 | 사용자 결정 항목 명시 (D-1~D-5) + 합의 형태 권고 명시 | ✅ §8 + §9.1 |

---

> **본 brief 발효 시점** = 사용자 승인 (§8 D-1~D-5 결정) + Reviewer-only 단축 합의 APPROVE (§9.1 권고 답습) + 본 brief commit. 본 brief 자체 = **실 구현 단계 진입 권한 발효 자격** 한정 (실 file 생성/수정 = 별도 단계).
