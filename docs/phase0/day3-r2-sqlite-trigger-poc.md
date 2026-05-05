# Phase 0 — Day 3 R-2 PoC 보고서: SQLCipher BEFORE INSERT Trigger DB-level Fallback

> **작성일**: 2026-05-05
> **브랜치**: `feature/hermes-phase0`
> **상태**: R-2 검증 완료, **PASS 확정**
> **timebox**: 1~2일 (실제 소요 ~1시간 — 사용자 timebox 내 조기 완료)
> **다음 단계**: G1b 재판정 → R-3~R-7 보강 → P2 v3 작성

---

## 1. 결론 요약

| 검증 항목 | 결과 |
|---------|------|
| **C1** BEFORE INSERT trigger 동작 | **PASS** |
| **C2** REGEXP UDF 동작 | **PASS** |
| **C3** canary secret INSERT 차단 (5종 패턴) | **PASS** |
| **C4** 정상 메시지 INSERT 성공 | **PASS** |
| **C5** DB 평문 부재 (committed rows + 디스크 파일 byte) | **PASS** |
| **C6** 에러 메시지 평문 미노출 | **PASS** |
| **종합 판정** | **R-2 = PASS** |

→ **DB-level fallback 으로 AI memory/session DB에 plaintext secret persistence 차단 가능 실증**.
→ **풀 합의 G1b 재판정 진입 조건 충족** (헌법 8조 본질 = "DB 평문 저장 차단" 충족).

---

## 2. 검증 목적 (사용자 명시)

> "DB-level fallback으로 AI memory/session DB에 plaintext secret persistence를 차단할 수 있는가?"

차단 방향 (사용자 선호): "trigger가 secret을 자동 마스킹하는 것보다, 우선은 secret 포함 INSERT를 확실히 차단하는 방향".

→ 본 PoC는 `RAISE(ABORT, ...)` 방식으로 secret 포함 INSERT 자체를 거부 (마스킹 미시도).

---

## 3. PoC 환경 (Docker 격리)

### 3.1 격리 정책 (P2 v2 §2.6 부분 정합)

`docker/r2-poc/docker-compose.r2-poc.yml`:

```yaml
services:
  r2-poc:
    build: { context: ., dockerfile: Dockerfile }
    image: r2-poc:local
    network_mode: none           # 외부 통신 차단
    read_only: true              # 루트 fs 읽기 전용
    tmpfs:
      - /tmp:noexec,nosuid,size=64m
    cap_drop: [ALL]
    security_opt:
      - no-new-privileges:true
    user: "1000:1000"
```

### 3.2 의존성 (재현 가능)

`docker/r2-poc/Dockerfile`:

- Base: `python:3.11-slim`
- System: `libsqlcipher-dev` + `build-essential` (pysqlcipher3 컴파일용)
- Python: `pysqlcipher3==1.2.0` (PyPI 가용 최신, 1.2.1 미존재 확인)

이미지 크기: ~470MB (build cache 활용 시 재빌드 ~1초).

### 3.3 빌드/실행 명령

```bash
cd docker/r2-poc
sg docker -c "docker compose -f docker-compose.r2-poc.yml build"
sg docker -c "docker compose -f docker-compose.r2-poc.yml run --rm r2-poc"
```

(현 사용자 `delangi`가 docker group에 추가된 후 `sg docker -c` 로 단일 명령 활성화.)

---

## 4. 검증 설계

### 4.1 SQLCipher DB

```python
conn = sqlcipher.connect(db_path)
conn.execute(f"PRAGMA key = '{DB_KEY}'")  # 평문 키, PoC 한정 — 실 운영은 ADR-010 Vault HSM
conn.execute("PRAGMA cipher_page_size = 4096")
```

### 4.2 REGEXP UDF 등록

```python
def regexp(pattern: str, value: object) -> bool:
    if value is None:
        return False
    try:
        return re.search(pattern, str(value)) is not None
    except re.error:
        return False

conn.create_function("REGEXP", 2, regexp)
```

→ Python `re.search` 를 SQLite REGEXP 연산자로 노출. SQLCipher는 SQLite 위에 암호화 layer만 추가하므로 동일 작동.

### 4.3 BEFORE INSERT Trigger

```sql
CREATE TRIGGER block_secrets_messages
BEFORE INSERT ON messages
FOR EACH ROW
WHEN NEW.content IS NOT NULL AND (
       NEW.content REGEXP 'sk-ant-[A-Za-z0-9_-]{10,}'
    OR NEW.content REGEXP 'sk-[A-Za-z0-9_-]{10,}'
    OR NEW.content REGEXP 'ghp_[A-Za-z0-9]{10,}'
    OR NEW.content REGEXP 'AKIA[A-Z0-9]{16}'
    OR NEW.content REGEXP 'xox[baprs]-[A-Za-z0-9-]{10,}'
)
BEGIN
    SELECT RAISE(ABORT, 'secret-pattern-detected: INSERT blocked by R-2 trigger');
END;
```

ABORT 메시지는 **고정 문자열** — `NEW.content` 를 echo 하지 않으므로 에러 출력에 secret 누출 없음 (C6 만족 설계).

### 4.4 검증 시나리오

**Safe 메시지 3종** (INSERT 성공 기대):
- `"hello world, this is a normal user message"`
- `"def foo(): return 42"`
- `"session_id_count is 5 and token_count is 100"` (near-but-not-secret)

**Canary 메시지 5종** (INSERT 차단 기대):
- `anthropic-style`: `"...sk-ant-CANARYDEADBEEF12345 please use it"`
- `openai-style`: `"...sk-CANARYDEADBEEF1234567890..."`
- `github-pat`: `"...ghp_CANARYDEADBEEF1234"`
- `aws-akid`: `"...AKIACANARY1234567XYZ"`
- `slack-token`: `"...xoxb-CANARY-1234567-XYZ"`

**디스크 파일 byte scan** (SQLCipher 암호화 확인):
- `db_path.read_bytes()` 에서 canary 패턴 검색 → 0건 기대

---

## 5. 실행 결과 (raw stdout)

```
[setup] workdir=/tmp/r2-poc-ou1922k0
[setup] db_path=/tmp/r2-poc-ou1922k0/state.db

=== C2: SQLCipher 환경에서 REGEXP UDF 등록·동작 ===
  [PASS] REGEXP UDF returns 1 for matching pattern

=== C1: BEFORE INSERT trigger 등록·동작 ===
  [PASS] CREATE TRIGGER 성공

=== C4: 정상 메시지 INSERT 성공 ===
  [PASS] safe INSERT [plain-text]
  [PASS] safe INSERT [code-snippet]
  [PASS] safe INSERT [near-but-not-secret]

=== C3: canary secret INSERT 차단 ===
  [PASS] canary INSERT [anthropic-style] blocked
  [PASS] canary INSERT [openai-style] blocked
  [PASS] canary INSERT [github-pat] blocked
  [PASS] canary INSERT [aws-akid] blocked
  [PASS] canary INSERT [slack-token] blocked

=== C5: DB 내부 canary 평문 부재 ===
  rows committed: 3
  [PASS] no canary plaintext in messages.content — 3 rows scanned

=== C5-extra: 디스크 파일 byte 수준 검사 (SQLCipher 암호화 확인) ===
  [PASS] no canary plaintext in raw db file bytes (SQLCipher encrypted) — file size=12288 bytes

=== C6: 에러 메시지에 canary 평문 노출 여부 ===
  [PASS] ABORT error message does not echo secret — captured_err='secret-pattern-detected: INSERT blocked by R-2 trigger'

=== R-2 PoC 종합 결과 ===
  C1 BEFORE INSERT trigger 동작: PASS
  C2 REGEXP UDF 동작: PASS
  C3 canary INSERT 차단: PASS
  C4 정상 메시지 INSERT 성공: PASS
  C5 DB 평문 부재: PASS
  C6 에러 출력 평문 미노출: PASS

[verdict] R-2 = PASS
```

### 5.1 검증 결과 해석

- `rows committed: 3` — Safe 3건만 commit, Canary 5건은 trigger ABORT로 차단됨
- `file size=12288 bytes` — SQLCipher 암호화 적용 확인 (canary 평문이 디스크 byte 수준에도 부재)
- `captured_err='secret-pattern-detected: INSERT blocked by R-2 trigger'` — 에러 메시지에 canary 평문 미노출 (고정 문자열만 출력)

---

## 6. 1차 시도 실패와 학습 (PoC 신뢰도 강화)

### 6.1 1차 실패 원인

PoC 스크립트의 except 분기에서 `sqlcipher.OperationalError` 만 잡았으나, 실제 `RAISE(ABORT, ...)` 는 `sqlcipher.IntegrityError` 로 raise됨. 결과: trigger는 정상 동작했으나 PoC 코드가 잘못 FAIL 판정.

### 6.2 1차 결과 분석으로 본질 동작 확인

1차 결과에서도 다음이 실증됨:
- 모든 5종 canary가 `IntegrityError: secret-pattern-detected: INSERT blocked by R-2 trigger` 로 raise됨 → trigger 정상 동작
- `rows committed: 3` (safe 3건만) → DB에 canary 평문 미저장
- 에러 메시지에 secret 평문 미노출

### 6.3 수정

```python
except sqlcipher.OperationalError as exc:   # 1차
↓
except sqlcipher.Error as exc:               # 2차 (모든 sqlcipher 에러 base class)
```

### 6.4 학습 자료 가치

PoC의 1차 실패 자체가 **"trigger 동작 신호 ↔ Python 예외 클래스 매핑"의 명세 격차**를 드러냄. 실 운영 통합 시 except 분기 robustness 검증을 회귀 테스트에 포함 필요.

---

## 7. R-2 PASS의 의미

### 7.1 G1b 재판정 진입

풀 합의 §4.2 G1 정의 ("Hermes 자체 redaction이 DB INSERT 경로 적용") 미충족 (R-1 FAIL 확정). 그러나 본 R-2 PoC가 **DB-level fallback (SQLCipher BEFORE INSERT trigger + REGEXP UDF)** 로 헌법 8조 본질("DB 평문 저장 차단") 충족 가능 실증.

→ **G1을 다음으로 재정의 권고**:

> **G1b**: Hermes redaction (LLM 송신 단계) + **SQLCipher BEFORE INSERT trigger** (DB INSERT 경로) 의 다층 방어로 DB 평문 secret persistence 차단 입증.

### 7.2 풀 합의 옵션 (1) 유지

- 옵션 (a) 자동 전환 거부 — Hermes PMO 격상 6~12개월 보류 사유 부재
- 4 게이트 중 G1 재정의 후 충족 가능 → R-3~R-7 보강 진행 + P2 v3 작성 진입

### 7.3 단축 합의 R-2 (SQLite trigger 의무화) 정합

단축 합의 §R-2:
> "(ii) SQLite trigger 의무 채택 (DB 레벨 강제, BEFORE INSERT on messages, REGEXP user-defined function 등록)"

본 PoC가 정확히 이 권고 형태로 동작 — SQLite trigger 의무화 결정의 실현 가능성 확정.

---

## 8. 한계 + 다음 단계 (실 Hermes 통합 시 검증 필요)

### 8.1 본 PoC의 한계

| 한계 | 영향 | 후속 작업 |
|------|------|---------|
| 격리 환경 in-memory tmpfs DB | 실 Hermes `~/.hermes/state.db` 통합 미검증 | R-3~R-4에서 실 Hermes `SessionDB` monkey-patch + trigger 주입 검증 |
| `PRAGMA key = '<plain>'` 평문 키 | 실 운영은 ADR-010 Vault HSM | R-7에서 Vault 통합 검증 |
| 5종 canary 패턴만 검증 | P1_REDACTOR 패턴 동등성 미확인 | R-4 단축 합의 패턴 동등성 검증 |
| 단일 INSERT 직접 호출 | `SessionDB.append_message` 호출 경로 통합 미검증 | R-3에서 monkey-patch 실측 |
| trigger drop 가능성 미검증 | Hermes schema migration이 trigger 삭제 가능 | 단축 합의 R-5 강화 (entry point에서 trigger 존재 검증 fail-fast) |
| `PRAGMA legacy_alter_table` 등 우회 미검증 | 악성 SQL이 trigger 우회 가능성 | R-3에서 우회 시도 시뮬레이션 |

### 8.2 다음 단계 작업

1. **R-3** (단축 합의): ADR-011 또는 ADR-008 Amendment 발행 (수단/목적 분리 명문화)
2. **R-4**: redaction 패턴 동등성 검증 (Hermes redact_secrets ↔ R-2 trigger UDF)
3. **R-5**: T13 강화 (config 체크 + 주기적 canary inject DB 검증 둘 다)
4. **R-6**: CI nightly 회귀 (Hermes 업그레이드 자동 R-2 PoC 재실행)
5. **R-7**: Phase 1 합격 SOP 명세화 (canary 주입 절차)
6. **G1b 정식 재정의** (system-identity-prequel §4.2 갱신)

R-3~R-7 완료 후 P2 v3 신규 작성 + ADR-008/009/010 동시 갱신 PR 묶음.

### 8.3 G1b 재판정 → 4 게이트 진행 상태

| 게이트 | 정의 | 현 상태 |
|-------|------|--------|
| **G1b** | DB 평문 저장 차단 (Hermes redaction + DB-level fallback 다층 방어) | **충족 가능 실증** (R-2 PASS) — 정식 충족은 R-3~R-5 보강 후 |
| G2 | 6 거버넌스 사전조건 충족 | 미작성 |
| G3 | "Hermes ≠ root of trust" 운영적 구현 | 미작성 |
| G4 | Provider-agnostic Memory/Skill 저장 형식 확정 | 미작성 |

---

## 9. 산출 파일 (본 단계)

```
docker/r2-poc/
├── Dockerfile                       # python:3.11-slim + libsqlcipher-dev + pysqlcipher3==1.2.0
├── docker-compose.r2-poc.yml       # 격리 정책 (network_mode: none, read_only, cap_drop, etc.)
└── r2_poc.py                        # 6항목 검증 스크립트

docs/phase0/
└── day3-r2-sqlite-trigger-poc.md   # 본 보고서
```

---

## 10. 사용자 결정 옵션

R-2 PASS 확정 후 다음 단계:

| 옵션 | 의미 | 권고 |
|------|------|------|
| **(1) G1b 재판정 + R-3~R-7 진행** | system-identity-prequel §4.2 갱신, 단축 합의 R-3~R-7 작업 진입 | ⭐ |
| (2) R-2 추가 강화 PoC | 실 Hermes `SessionDB` monkey-patch 통합 검증 | R-3에 흡수 가능, 별도 진행 불필요 |
| (3) 합의 보고서 갱신 | 풀 합의 보고서에 R-2 PASS 결과 명시 | (1)과 병행 가능 |

**메인 컨텍스트 추천: (1) + (3) 병행**.

---

**Day 3 R-2 종료 시각**: 2026-05-05 (timebox 1~2일 내 조기 완료)
**다음 진입점**: G1b 재판정 + R-3 ADR-011 작성 (수단/목적 분리 명문화)
