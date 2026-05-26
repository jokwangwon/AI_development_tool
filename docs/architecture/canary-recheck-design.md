# Canary Recheck Design (R-5)

> **Hermes / redaction / trigger UDF 의 silent 깨짐 발생 가능성을 자동 검증으로 차단하는 canary 재검증 트리거 설계 — R-4.1 evidence 의 Tier-1 42종 catalog 를 baseline 으로 활용**

**상태**: 작성 (R-5 설계 단계 — 코드 구현 미포함)
**날짜**: 2026-05-06
**상위 권위**: ADR-011 §2.4 (자동 학습 vs 자동 정책 변경 분리), ADR-011 §3 R-5 매핑
**입력 자료**: `docs/phase0/r4-1-trigger-extension-evidence.md` §10.3 R-5 입력
**범위**: 설계 문서 작성. 실제 자동화 구현은 R-6, Phase 1 합격 SOP 는 R-7.

---

## 1. 작업 정의

### 1.1 본 R-5 의 본질

R-5 는 **canary 재검증 트리거의 설계**이다. canary catalog 자체는 R-4.1 evidence §5 (Tier-1 42 catalog) 를 그대로 재사용하며, 본 R-5 는 다음 4가지를 정의한다:

1. **언제** canary 를 재실행할지 (실행 시점, §4)
2. **어떤 판정 기준** 으로 PASS/PARTIAL/FAIL/ROLLBACK 을 결정할지 (§5)
3. **어떤 안전장치** 로 canary 자체가 누출 위험원이 되지 않을지 (§6)
4. **어떻게 evidence 를 기록** 하고 변조 방지할지 (§7)

### 1.2 사용자 명시 R-5 필수 7 카테고리

| # | 카테고리 | 본 문서 § |
|---|---------|------|
| 1 | T13 강화 (config 체크 / 주기적 inject / drift 감지) | §2 |
| 2 | Canary catalog (R-4.1 재사용 + fake 강제) | §3 |
| 3 | 실행 시점 (6 trigger) | §4 |
| 4 | 판정 기준 (PASS/PARTIAL/FAIL/ROLLBACK) | §5 |
| 5 | 안전장치 (평문 노출 금지 / 격상 차단) | §6 |
| 6 | Evidence 기록 (Markdown + JSONL append-only) | §7 |
| 7 | 자동 정책 변경 금지 (T1/T2/T3 운영 적용) | §8 |

### 1.3 본 문서가 *하지 않는* 것 (사용자 명시 금지 사항)

- ❌ 실제 CI/nightly 구현 — R-6 영역
- ❌ P2 v3 작성 — R-7 완료 후 별도 작업
- ❌ Hermes PMO 격상 판정 — 4 게이트 통과 후 별도 결정
- ❌ Tier-2 (Telegram bot) / Tier-3 (Discord, E.164 phone) canary 확장 — 별도 합의 또는 R-7
- ❌ R-6 작업과 섞기 — 본 R-5 는 *trigger 정의* 까지

---

## 2. T13 강화 정의

P2 v2 §T13 (canary recheck) 의 강화. P2 v2 의 T13 은 canary 패턴 단순 매칭만 정의했으나, 본 R-5 는 다음 3 항목을 추가한다.

### 2.1 Config 체크

다음 config 활성 상태를 startup + 주기적 검증:

| 항목 | 위치 | 검증 시점 |
|------|------|---------|
| `HERMES_REDACT_SECRETS` 환경변수 | Hermes process env | startup, 매 trigger 시 |
| `security.redact_secrets: true` | `~/.hermes/config.yaml` | startup 시 |
| SQLCipher PRAGMA key 설정 | DB connection 시점 | 매 connection 시 |
| trigger UDF 등록 상태 | DB connection 시점 | 매 connection 시 |
| trigger SQL 등록 상태 | DB schema | startup 시 + 매 trigger 시 |

**중요 — ADR-011 §2.3 운영 함의 #2 답습**: Hermes redaction (config 체크 #1, #2) 은 *로그/송신* 방어 수단. **DB INSERT 차단 책임은 trigger UDF (R-4.1)** 이다. 따라서 redaction config 체크는 *보조*, *primary* 는 trigger 등록 상태 (#4, #5) 검증.

### 2.2 주기적 Canary Inject

R-4.1 Tier-1 42 catalog 를 주기적으로 inject 하여 trigger 차단 동작이 살아있음을 검증:

| 환경 | 기본 주기 | 사용자 조정 가능 여부 |
|------|---------|------|
| 운영 (Hermes runtime) | 매 60분 | T2 (사용자 승인 필요) |
| CI / nightly | 1회 / 24h | T2 (사용자 승인 필요) |
| Pre-commit (`agent/redact.py` 변경 시) | 1회 / commit | T1 (자동 허용) |

주기 변경은 ADR-011 §2.4 T2 (사용자 승인) — 자동 변경 금지.

### 2.3 Drift 감지

다음 4 차원의 drift 자동 검출:

| Drift 차원 | 비교 대상 | 검출 시 처리 |
|---------|---------|---------|
| **Hermes drift** | `agent/redact.py` 의 `_PREFIX_PATTERNS` / regex 변경 | R-4 §5 비교표 갱신 PR trigger (R-6 영역) |
| **Pattern catalog drift** | `redaction-pattern-equivalence.md` (R-4) 카탈로그 ↔ 실제 trigger UDF 등록 패턴 | catalog version mismatch 시 단축 합의 (T2) |
| **Trigger UDF drift** | `r4_1_poc.py` 또는 운영 환경 trigger SQL 의 패턴 catalog | R-4.1 evidence 갱신 PR + ADR-011 §2.4 T3 절차 |
| **Config drift** | startup 시점 config 값 ↔ runtime 시점 config 값 | runtime 변경 감지 시 즉시 차단 + 알림 |

---

## 3. Canary Catalog (R-4.1 재사용)

### 3.1 Catalog 정의 — `R4.1-tier1-v1`

본 R-5 는 **별도 catalog 신설 없이** R-4.1 evidence §5 (Tier-1 42 catalog) 를 그대로 재사용한다. 정합성 보장 + 의사결정 비용 0.

| 속성 | 값 |
|------|-----|
| Catalog name | `R4.1-tier1-v1` |
| Catalog source | `docs/phase0/r4-1-trigger-extension-evidence.md` §5 (commit `e1fb4be`) |
| Catalog hash baseline | SHA-256 of canonical catalog dump (구현 시 산정 — R-6 자동화) |
| Pattern count | 42 (prefix 31 + regex 9 + alternation 2) |
| Source 추적 | `T1-001` ~ `T1-042` ID 체계 |

**Catalog 갱신 정책**: ADR-011 §2.4 T3 — Tier-1 catalog 변경은 단축/풀 합의 필수. 본 R-5 는 *catalog 재사용*만 정의, *catalog 변경 정책*은 ADR-011 §2.4 권위 답습.

### 3.2 Fake Canary 강제 (실제 secret 누출 방지)

**모든 canary 입력은 명백히 가짜임이 표시되어야 한다**. 다음 marker 중 최소 1개 포함 필수:

- 공통 ID marker `R41T` (R-4.1 evidence §1.3 marker 정의 답습)
- prefix `CANARY` 또는 `fakecanary`
- suffix `NOTAREAL` 또는 `NOT-A-REAL-SECRET`
- vendor 형식 충실하되 의도된 가짜 표시 (예: `sk-ant-CANARY-R4-1-001-NOT-A-REAL-SECRET`)

**Catalog 등록 시 검증**:
- canary 입력에 위 marker 중 최소 1개 미포함 시 → **canary 등록 거부** (정책 위반, T2 트리거)
- canary catalog 무결성 검사: SHA-256 hash 비교 (§3.1 baseline 과 매칭)

**실 secret 우연 매칭 방지**: vendor 정규식과 매칭하지만 marker 표시로 운영자가 *명백히 가짜* 임을 즉시 식별 가능.

### 3.3 본 R-5 범위 외 (Tier-2 / Tier-3)

| Tier | 항목 | 처리 |
|------|------|------|
| Tier-2 | Telegram bot token | R-7 SOP 작성 시 Tier-1 승격 검토. 본 R-5 미포함 |
| Tier-3 | Discord mention, E.164 phone (privacy) | 헌법 8조 외 영역. 별도 ADR. 본 R-5 미포함 |

---

## 4. 실행 시점 (Trigger Conditions)

R-5 canary recheck 는 다음 6 시점에 자동 발화 (실제 자동화는 R-6).

| # | Trigger | 발화 빈도 | 발화 조건 | 자동화 책임 |
|---|---------|---------|---------|---------|
| 1 | **Hermes startup** | 1회 / startup | Hermes process 시작 직후 | Hermes runtime 통합 (R-6 + Hermes wrapper) |
| 2 | **CI / nightly** | 1회 / 24h | GitHub Actions cron `0 0 * * *` | R-6 GitHub Actions YAML |
| 3 | **Hermes upstream version 변경** | 의존성 변경 시 | `requirements.txt` / `pyproject.toml` 의 `hermes-agent` 버전 변경 PR | Renovate / Dependabot + GitHub Actions `workflow_run` |
| 4 | **Redaction pattern 변경** | `agent/redact.py` diff 시 | upstream Hermes `agent/redact.py` 의 `_PREFIX_PATTERNS` / regex 변경 | pre-commit hook + GitHub Actions push trigger |
| 5 | **Trigger UDF 변경** | `r4_1_poc.py` / 운영 trigger SQL diff 시 | Tier-1 catalog 또는 alternation regex 변경 PR | pre-commit hook + ADR-011 §2.4 T3 절차 강제 |
| 6 | **Phase 1 acceptance 직전** | 1회 (Phase 1 진입 직전) | 운영자 manual 발화 + R-7 SOP 의무 | R-7 SOP + 운영자 절차 |

### 4.1 Trigger 시점별 PASS 의무

| Trigger | PASS 미충족 시 결과 |
|---------|------|
| #1 startup | Hermes process **abort** (시작 차단) |
| #2 CI/nightly | PR merge 차단 (운영 영향 없음, 알림만) |
| #3 upstream version | PR merge 차단 + 단축 합의 trigger |
| #4 redaction pattern | PR merge 차단 + 단축 합의 + R-4 비교표 갱신 의무 |
| #5 trigger UDF | PR merge 차단 + ADR-011 §2.4 T3 절차 강제 |
| #6 acceptance | Phase 1 진입 차단 (R-7 SOP) |

본 R-5 는 trigger *정의*만. 실제 차단 메커니즘 (Actions YAML / pre-commit / Hermes wrapper) 은 R-6 작업.

---

## 5. 판정 기준 (PASS / PARTIAL / FAIL / ROLLBACK)

### 5.1 5 가지 평가 차원

매 trigger 실행 시 5개 차원 평가:

| 차원 | 정의 | 측정 |
|------|------|------|
| **P1** | Tier-1 42 canary 차단 | trigger ABORT 발화 = PASS, INSERT 성공 = FAIL |
| **P2** | Safe sample 9 INSERT 성공 | INSERT 성공 = PASS, ABORT = FAIL (false-positive) |
| **P3** | DB 평문 부재 | committed rows + raw bytes 에 marker `R41T` 검출 = FAIL |
| **P4** | 에러 메시지 평문 미노출 | ABORT 메시지 = 고정 문자열 only |
| **P5** | Drift 감지 0건 | §2.3 4 차원 모두 정합 |

### 5.2 PASS

**조건**: P1~P5 모두 충족.

**처리**:
- 운영 계속, 다음 trigger 시점까지 무조치
- evidence 기록 (§7)
- alert 발화 안 함

### 5.3 PARTIAL

**조건**: P1~P5 중 1~2건 실패, 단 (P3) 와 (P4) 는 모두 충족.

**처리**:
- 운영 계속하되 운영자 알림
- 단축 합의 trigger (ADR-011 §2.4 T2)
- Hermes PMO 격상 *후보* 상태인 경우 → 격상 차단 (§6.4)
- evidence 기록 + drift 상세 첨부

### 5.4 FAIL

**조건** (다음 중 하나):
- (P3) 또는 (P4) 실패 — 본질적 보안 위반
- P1~P5 중 3건 이상 실패

**처리**:
- 운영 즉시 차단 — Hermes process 정지 권고
- 단축/풀 합의 trigger (ADR-011 §2.4 T3 적용 — Hermes 자체 정책 변경 금지)
- 격상 절대 차단
- 운영자 즉시 alert (PagerDuty / Slack equivalent)

### 5.5 ROLLBACK Trigger

ROLLBACK 은 FAIL 의 일부 + 추가 자동 회수 발화 조건:

| 조건 | ROLLBACK 종류 | 자동/수동 |
|------|---------|------|
| (P3) DB 평문 leak 검출 — 헌법 8조 본질 위반 | trigger UDF 갱신 PR revert + 이전 commit 복원 | **automatic** |
| (P2) 신규 trigger UDF 가 false-positive 폭증 (정상 safe sample 차단율 > 10%) | trigger UDF PR revert | **automatic** |
| Hermes upstream version 변경 후 canary recheck FAIL | hermes-agent 버전 핀 복원 + 단축 합의 | **manual** + 단축 합의 |
| Pattern catalog drift > 10% (§2.3) | catalog version 이전 commit 복원 | **manual** + 단축 합의 |

ROLLBACK 후에는 ADR-011 §2.4 T3 절차로 trigger UDF / hermes 버전 / config 변경 재검토 (단축 또는 풀 합의 의무).

---

## 6. 안전장치 (Safety Constraints)

### 6.1 Canary 평문 로그 노출 금지

| 누출 경로 | 차단 메커니즘 |
|---------|---------|
| trigger ABORT 메시지 | **고정 문자열** (`secret-pattern-detected: ...`) — `NEW.content` echo 안 함 (R-4.1 §4.3 답습) |
| Recheck 결과 보고 | catalog ID (`T1-001`) 만 출력, canary 입력 자체 미출력 |
| Exception trace | `safe_repr_error()` 패턴 (R-4.1 §3) 으로 자동 redact — marker `R41T` 검출 시 메시지 redact |
| Evidence 문서 | catalog ID + verdict 만 — canary 입력은 catalog source (`R4.1-tier1-v1`) 인용으로 대체 |

### 6.2 DB 평문 저장 금지

- 모든 canary INSERT 는 trigger 에 의해 차단 (R-4.1 evidence §7 C5 baseline)
- recheck 자체가 *검증* 작업 — canary inject 결과가 운영 DB 에 영구 저장되지 않아야 함
- **격리 DB 사용 권고**: recheck 전용 ephemeral DB (e.g. `tmpfs` 마운트 또는 임시 SQLCipher 파일) — R-4.1 PoC 의 `/tmp/r4-1-poc-*` 패턴 답습
- recheck 종료 시 임시 DB 파일 즉시 삭제 (운영 환경) 또는 컨테이너 ephemeral storage 활용 (CI 환경)

### 6.3 실패 에러 = 고정 문자열만

| 항목 | 정책 |
|------|------|
| trigger ABORT 메시지 | 고정 문자열 (`secret-pattern-detected: INSERT blocked by R-4.1 trigger`) |
| Application 레벨 에러 | `safe_repr_error()` 통과 — marker 검출 시 자동 redact |
| Stack trace | redacted — canary 입력 또는 실 secret 형식 검출 시 redact |
| 외부 통보 (alert) | catalog ID + verdict + drift summary — canary 입력 미포함 |

### 6.4 실패 시 Hermes PMO 격상 차단

ADR-011 §2.3 + system-identity-prequel §3 — Hermes PMO 격상은 4 게이트 통과 필수.

| Recheck verdict | Hermes PMO 격상 | 격상 재시도 조건 |
|----------------|---------------|--------------|
| PASS | 격상 가능 (4 게이트 모두 통과 시) | — |
| PARTIAL | **격상 차단** | drift 정정 + 단축 합의 + recheck PASS |
| FAIL / ROLLBACK | **격상 절대 차단** | 단축/풀 합의 + recheck PASS + 격상 결정 별도 합의 |

본 §6.4 는 R-5 trigger 의 *방어선* 역할. 격상 결정 자체는 ADR-011 §2.4 T3 (자동 정책 변경 금지) 적용 — 자동 격상 금지.

---

## 7. Evidence 기록 방식

### 7.1 이중 형식 (Markdown + JSONL)

매 trigger 실행 시 다음 두 evidence 동시 기록 (system-identity-prequel §6.5 Evidence Ledger 답습).

#### 7.1.1 Markdown summary

**경로**: `docs/operations/canary-recheck/{YYYY-MM-DD}-{trigger-id}.md`

**내용 구조**:
- 헤더: Trigger ID + 발화 시점 + 발화 사유 (§4 #1~#6 매핑)
- §1 Catalog version (e.g. `R4.1-tier1-v1`) + hash
- §2 Tier-1 42 canary 결과 표 (R-4.1 evidence §5 답습 형식)
- §3 Safe sample 결과 표
- §4 자동 검증 결과 (P1~P5)
- §5 Drift observations
- §6 Verdict (PASS/PARTIAL/FAIL) + ROLLBACK 발화 여부
- §7 실행 명령어 + git commit reference

#### 7.1.2 JSONL append-only event

**경로**: `docs/operations/canary-recheck/events.jsonl` (단일 파일, append-only)

**Schema** (각 line = 1 trigger 실행):

```json
{
  "schema_version": 1,
  "timestamp": "2026-05-06T14:30:00Z",
  "trigger_id": "<UUID>",
  "trigger_reason": "hermes-startup | ci-nightly | upstream-version | pattern-change | udf-change | acceptance",
  "catalog_version": "R4.1-tier1-v1",
  "catalog_hash": "sha256:<hex>",
  "git_commit": "<HEAD commit hash>",
  "verdict": "PASS | PARTIAL | FAIL",
  "p1_tier1_pass_rate": "42/42",
  "p2_safe_pass_rate": "9/9",
  "p3_db_clean": true,
  "p4_error_clean": true,
  "p5_drift_count": 0,
  "drift_observations": [],
  "rollback_triggered": false,
  "evidence_doc": "docs/operations/canary-recheck/2026-05-06-startup-001.md",
  "prev_event_hash": "sha256:<hex>"
}
```

### 7.2 변조 방지 (append-only + hash chain)

| 메커니즘 | 적용 |
|---------|------|
| Append-only | 기존 line 수정 금지 — 운영 도구가 sed/awk/edit in-place 차단 |
| Hash chain | 매 line 의 `prev_event_hash` 가 이전 line 전체의 SHA-256 — 임의 변조 시 chain 깨짐 검출 |
| Git append commit | events.jsonl 변경은 *새 line 추가* PR 만 허용. 다른 변경 PR 차단 (pre-commit hook) |
| Git notes (선택) | events 무결성 보강 위해 별도 `git notes` 사용 가능 — R-7 SOP 시점 결정 |

본 §7.2 schema 의 자세 구현 (hash chain 알고리즘, git pre-commit 메커니즘) 은 R-7 SOP 또는 별도 ADR 로 확정.

### 7.3 실행 명령어 보존

각 evidence 에 다음 메타 필수 포함:

| 메타 | Markdown | JSONL |
|------|---------|-------|
| docker compose 명령 또는 GH Actions workflow ID | §7 본문 | `workflow_run_id` 필드 (CI) 또는 `command` 필드 |
| Catalog version 인용 | §1 | `catalog_version` |
| Git HEAD commit reference | §7 | `git_commit` |
| 결과 hash | §6 | `catalog_hash`, `prev_event_hash` |

---

## 8. 자동 정책 변경 금지 (ADR-011 §2.4 운영 적용)

### 8.1 Tier 분류 운영 매핑

| Tier | 항목 | 본 R-5 적용 | 승인 절차 |
|------|------|---------|---------|
| **T1** (자동 허용) | catalog ID 추가 — 신규 vendor 패턴 (e.g. `T1-043`) | 자동 catalog version 갱신 + recheck 재실행 | 자동 |
| **T2** (사용자 승인) | catalog version major 갱신 (Tier-1 42 → 43+), 주기 변경 | 사용자 명시 결정 + 단축 합의 trigger | 단축 합의 (Reviewer-only) |
| **T3** (절대 금지) | canary 실패 시 정책 완화 (Tier-1 42 → 30), redaction 비활성, trigger 제거 | **즉시 차단 + alert** — Hermes 자체 변경 시도 거부 | 단축/풀 합의 + ADR amendment 의무 |

### 8.2 Hermes 자체 정책 완화 차단 메커니즘

canary recheck 가 FAIL/PARTIAL 시 Hermes 가 *자기 자신* 의 redaction 정책을 자동 완화 시도하면 즉시 차단:

| 차단 레이어 | 메커니즘 |
|---------|---------|
| Code level | `r4_1_poc.py` (또는 운영 trigger SQL) 의 변경은 git commit + 단축/풀 합의 거쳐야만 적용 (ADR-011 §2.4 T3) |
| Process level | Hermes process 가 trigger UDF 자체를 disable 시도 시 — startup 시 trigger 등록 검증 (§2.1) FAIL → process abort |
| Config level | `HERMES_REDACT_SECRETS=false` 자동 설정 시도 감지 → ADR-011 §2.4 T3 위반 alert + 단축/풀 합의 의무 |
| Audit level | events.jsonl chain (§7.2) 으로 변조 시도 자동 검출 |

### 8.3 정책 변경 절차 매트릭스

| 변경 유형 | 승인 절차 | 후속 작업 |
|---------|---------|---------|
| Tier-1 catalog 신규 vendor 추가 | 단축 합의 (Reviewer-only) | recheck 재실행 + catalog version 갱신 |
| Tier-1 catalog 기존 vendor 제거 | **풀 3+1 합의** (보안 약화 가능성) | recheck 재실행 + ADR-011 amendment |
| Tier-2 → Tier-1 승격 | 단축 합의 + R-7 SOP 갱신 | catalog version 갱신 |
| Tier-3 별도 카탈로그 신설 | **별도 ADR** (헌법 8조 외 영역) | privacy 정책 별도 합의 |
| trigger UDF 정규식 변경 | 단축 합의 + R-4.1 PoC 재실행 | catalog version 갱신 |
| Hermes 의존성 버전 핀 변경 | 단축 합의 + canary recheck 재실행 | drift 검사 |
| Hermes redaction config 변경 | **ADR-011 §2.4 T3 절대 금지** — 단축/풀 합의 필수 | ADR-011 amendment |

---

## 9. ADR-011 §2.4 / §3 R-5 매핑 결과

### 9.1 §2.4 T1/T2/T3 적용

본 R-5 의 모든 정책 변경은 §2.4 3-tier 분류 적용:
- canary recheck *자체 실행* = T1 (자동 허용 — 학습 루프 일부)
- 결과에 따른 정책 변경 = T2 (드리프트 정정) 또는 T3 (보안 약화 시도 차단)

### 9.2 §3 R-5 매핑 — silent 깨짐 자동 차단

> ADR-011 §3 R-5 매핑: "Hermes 학습 또는 upstream 변경으로 redaction silent 깨짐 발생 가능성 자동 검증 + §2.3 운영 함의 #4 구현"

| ADR-011 §3 R-5 의무 | 본 R-5 § |
|---|---|
| Silent 깨짐 자동 검증 | §2.3 (drift 감지 4 차원) + §4 (#4-5 trigger) |
| §2.3 운영 함의 #4 (Hermes 의존성 업그레이드 자동 R-2 회귀) | §4 #3 (upstream version 변경 trigger) |
| 자동 정책 반영 금지 | §8 (T1/T2/T3 운영 적용) + §6.4 (격상 차단) |

---

## 10. R-6 / R-7 직접 입력

### 10.1 R-6 (CI/nightly 회귀 검증) 직접 입력

R-6 (`.github/workflows/r2-canary.yml` 작성 예정) 은 본 R-5 §4 trigger 시점 #2~#5 의 *실제 자동화 구현*:

| R-5 trigger 시점 | R-6 구현 책임 |
|---|---|
| #2 CI / nightly | GitHub Actions schedule cron `0 0 * * *` |
| #3 Upstream version 변경 | Renovate / Dependabot PR + Actions `workflow_run` trigger on dependency PR |
| #4 Pattern 변경 | pre-commit hook + Actions push trigger on `agent/redact.py` change |
| #5 UDF 변경 | pre-commit + Actions push trigger on `r4_1_poc.py` change + ADR-011 §2.4 T3 강제 |

R-6 은 본 §10.1 trigger 매트릭스를 GitHub Actions YAML 로 구현 + 결과를 §7 evidence 형식으로 기록.

### 10.2 R-7 (Phase 1 합격 SOP) 직접 입력

R-7 (`docs/phase0/redaction-verification-sop.md` 작성 예정) 은 본 R-5 §4 #6 (Phase 1 acceptance) trigger 의 *판정 SOP* 화:

| R-5 항목 | R-7 SOP 항목 |
|---|---|
| §3.1 catalog version `R4.1-tier1-v1` | SOP PASS 기준 catalog 명시 |
| §5 PASS/PARTIAL/FAIL/ROLLBACK 4 verdict | SOP 판정 조건 |
| §6 안전장치 4 항목 | SOP 운영자 절차 |
| §7 evidence Markdown + JSONL schema | SOP evidence 제출 양식 |
| §8 정책 변경 매트릭스 | SOP 거버넌스 절차 |

### 10.3 R-5 가 R-6 / R-7 에 *위임* 하는 사항

| 항목 | 위임 대상 | 사유 |
|------|---------|------|
| GitHub Actions YAML 작성 | R-6 | §1.3 금지 사항 (실제 CI/nightly 구현 미포함) |
| pre-commit hook 작성 | R-6 | 동상 |
| Hermes runtime wrapper (startup trigger) | R-6 | 외부 hook 미지원 (Day 1 사실 확인) — 별도 wrapper 설계 |
| events.jsonl hash chain 알고리즘 세부 | R-7 | SOP 시점 schema 확정 |
| Phase 1 acceptance 판정 절차 | R-7 | SOP 자체가 R-7 산출 |

---

## 11. 결과 (Consequences)

### 11.1 긍정적

- ADR-011 §2.4 자동 학습 vs 자동 정책 변경 분리의 *운영 메커니즘* 설계 완료
- R-4.1 catalog 재사용으로 의사결정 비용 0 — Tier-1 42 catalog 의 운영 보호 절차 명시
- §4 6 trigger 시점으로 silent 깨짐 위험 차원 매트릭스화 (Hermes runtime / CI / 의존성 / pattern / UDF / acceptance)
- §5 4 verdict + ROLLBACK trigger 명시로 운영 자동 회수 경로 확보
- §6 4 안전장치로 canary 자체가 누출 위험원이 되지 않음 보장
- §7 이중 evidence (Markdown + JSONL append-only + hash chain) 로 변조 방지
- §8 정책 변경 매트릭스로 ADR-011 §2.4 T1/T2/T3 운영 적용 절차 정의
- R-6 / R-7 직접 입력 (§10) 명시 — 후속 작업 의사결정 비용 0

### 11.2 부정적

- 본 R-5 는 *설계 문서* — 실제 자동화 구현은 R-6 으로 위임. 운영 활성화까지 추가 작업 필요
- §7 evidence JSONL hash chain 메커니즘 미세부 — R-7 SOP 작성 시 또는 별도 ADR 로 schema 확정 필요
- §6.4 Hermes PMO 격상 차단 메커니즘은 *논리적* 정의 — 실제 구현 (격상 시점 검증 hook) 은 R-7 / G3 작업
- §4 #1 Hermes startup trigger 는 Hermes runtime 통합 의무. Hermes 가 외부 hook 미지원 (Day 1 사실 확인) 이므로 *외부 wrapper* 또는 *plugin* 형태로 구현 필요 — R-6 별도 설계 의무

### 11.3 주의사항

- 본 R-5 는 *trigger 정의*까지. 자동화 *실제 구현*은 R-6, *Phase 1 acceptance SOP*는 R-7
- §3.1 catalog `R4.1-tier1-v1` 은 commit `e1fb4be` 시점 정합. 미래 R-4.1 catalog 갱신 시 본 문서 §3.1 version 갱신 PR 의무
- §8 정책 변경 매트릭스는 ADR-011 §2.4 답습 — 본 R-5 가 정책 변경의 *분류 기준* 변경하지 않음. 분류 자체 변경은 ADR-011 amendment
- Tier-2 / Tier-3 catalog 본 R-5 미포함 — R-7 또는 별도 ADR
- **본 R-5 는 Hermes 안전성을 선언하지 않는다** (ADR-011 §7.3 답습) — Hermes 는 검증 대상이며 본 R-5 는 검증 외부화의 trigger 메커니즘 정의

---

## 12. 관련 문서

### 12.1 상위 권위
- `docs/decisions/ADR-011-means-vs-ends-redaction.md` §2.4 (자동 학습 vs 자동 정책 변경 분리), §3 R-5 매핑

### 12.2 입력 자료
- `docs/phase0/r4-1-trigger-extension-evidence.md` (R-4.1) §5 Tier-1 42 catalog, §10.3 R-5 입력
- `docs/architecture/redaction-pattern-equivalence.md` (R-4) §6 Tier-1 분류, §7.4 patterns 일관성 메커니즘
- `docs/architecture/system-identity-prequel.md` §6.5 Evidence Ledger (JSONL append-only 정신), §3 권위 위계
- `docs/architecture/hermes-adoption-design.md` (P2 v2) §T13 (canary recheck) — 본 R-5 가 강화 대상

### 12.3 본 R-5 산출
- `docs/architecture/canary-recheck-design.md` (본 문서)

### 12.4 후속 작업 입력 (§10 매핑)
- R-6 `.github/workflows/r2-canary.yml` (작성 예정) — 본 §4 trigger 매트릭스 + §7 evidence 형식 직접 인용
- R-7 `docs/phase0/redaction-verification-sop.md` (작성 예정) — 본 §5 판정 + §6 안전장치 + §7 evidence + §8 정책 매트릭스 직접 인용

---

**본 문서 발행 시점**: 2026-05-06
**다음 진입점**: R-6 (CI/nightly 회귀 검증 설계) — 본 §4 trigger 매트릭스 + §7 evidence 형식의 GitHub Actions YAML 구현 설계. 또는 R-5 사용자 검토 후 결정.
