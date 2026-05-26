# Phase 0 — Day 2 R-1 검증 보고서: Hermes 자체 redaction 적용 위치

> **작성일**: 2026-05-05
> **브랜치**: `feature/hermes-phase0`
> **상태**: R-1 검증 완료, **FAIL 확정** (코드 분석 only, PoC 미시행)
> **다음 단계**: R-2 (DB-level fallback PoC, 1~2일 timebox)

---

## 1. 결론 요약

| 항목 | 결과 |
|------|------|
| Hermes 자체 redaction 적용 위치 | **로그·도구 출력·Gateway 통신 전용** (DB INSERT 경로 미적용) |
| R-1 판정 | **FAIL** (LLM 송신/도구 출력 전용) |
| 검증 방법 | 코드 분석 (docstring + grep + 시그니처) — PoC 미시행으로 충분 |
| G1 (Hermes 자체 redaction이 DB INSERT 경로 적용) | **미충족** |
| 즉시 Hermes 보류 전환 | **아직 하지 않음** (사용자 결정) |
| R-2 진입 | **DB-level fallback PoC, 1~2일 timebox** |
| R-2 결과에 따른 분기 | PASS → G1b 재판정 / FAIL → 옵션 (a) 자동 전환 |

---

## 2. 검증 배경

단축 합의 R-1 (`docs/review/3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md` §R-1):

> "Hermes v0.12.0에서 `security.redact_secrets: true` 활성화 후 *DB INSERT 경로*에 redaction이 실제 적용되는지 직접 검증. PASS 기준: 0건 반환 (DB 평문 부재). FAIL 기준: 1건 이상 반환 → 정정안 즉시 폐기 → 옵션 A로 회귀 → §3.4 폴백 트리거."

풀 합의 G1 (`docs/review/3plus1-consensus-2026-05-05-system-identity-redefinition.md` §4.2):

> "Phase 0 R-1 (canary 검증) 완료 — Hermes 자체 redaction이 DB INSERT 경로에 실제 적용되는지 격리 환경 검증"

---

## 3. 검증 방법

### 3.1 1차: 코드 분석 (실 PoC 미시행으로 충분)

격리 환경 PoC 진행 전 코드 분석만으로 결정적 결과 도출 가능 여부 점검. 다음 3종 grep:

1. `agent/redact.py` 모듈 docstring + 핵심 함수 위치
2. `agent.redact` 모듈을 import 하는 모든 파일
3. `hermes_state.py` (SessionDB) 에서 `agent.redact` import 여부

결과적으로 1차 코드 분석만으로 **결정적 FAIL 증거** 확보. PoC 미시행 결정.

### 3.2 PoC 미시행 정당성

다음 3건 모두 충족 → PoC가 동일 결론을 강화하기만 할 뿐 변경하지 않음:
1. `agent/redact.py` 첫 줄 docstring이 적용 범위 명시
2. `hermes_state.py` 2050+ 줄 코드에 redact import 0건 (단순 grep 검증 가능)
3. `SessionDB.append_message` 시그니처에 redaction 인자 또는 콜백 없음

PoC는 동일 결과 확인이며 시간·환경 비용 대비 추가 정보 가치 0.

---

## 4. 결정적 사실 3건

### 4.1 사실 1 — `agent/redact.py:1-8` 모듈 docstring (적용 범위 명시)

```python
"""Regex-based secret redaction for logs and tool output.

Applies pattern matching to mask API keys, tokens, and credentials
before they reach log files, verbose output, or gateway logs.

Short tokens (< 18 chars) are fully masked. Longer tokens preserve
the first 6 and last 4 characters for debuggability.
"""
```

**해석**: Hermes 자체 redaction은 처음부터 **로그·verbose 출력·gateway 로그** 적용으로 설계됨. DB INSERT 경로는 적용 범위에 포함되지 않음.

### 4.2 사실 2 — redaction import 위치 25개, 모두 비-DB 경로

| 카테고리 | 파일 | 적용 위치 |
|---------|------|---------|
| 로깅 | `hermes_logging.py:211, 267` | RedactingFormatter (로그 파일 기록 직전) |
| 로깅 | `gateway/run.py:14993` | gateway 로깅 |
| 통신 | `agent/context_compressor.py:34` | context 압축 |
| 통신 | `agent/copilot_acp_client.py:25` | ACP 클라이언트 |
| 도구 출력 | `tools/code_execution_tool.py:895, 1240` | 코드 실행 결과 |
| 도구 출력 | `tools/browser_camofox.py:534, 574` | 브라우저 출력 |
| 도구 출력 | `tools/browser_tool.py:1660, 1732, 2531` | 브라우저 출력 |
| 도구 출력 | `tools/send_message_tool.py:18` | 메시지 전송 |
| 도구 출력 | `tools/file_tools.py:19` | 파일 작업 |
| 도구 출력 | `tools/terminal_tool.py:2084` | 터미널 출력 |
| 도구 출력 | `tools/web_tools.py:1241` | 웹 도구 |
| CLI | `hermes_cli/status.py:38`, `dump.py:42`, `debug.py:399`, `config.py:4407` | CLI 명령 출력 |
| Cron | `cron/scheduler.py:650` | cron job 텍스트 |
| Phone | `gateway/platforms/sms.py:37`, `signal.py:41` | 전화번호 redaction (별도 모듈) |

→ **25개 import 모두 출력·로깅·통신 경로**. DB write 경로 0개.

### 4.3 사실 3 — `hermes_state.py` (SessionDB) redaction import 0건

```bash
$ grep "agent.redact\|from agent import redact" /tmp/hermes-phase0/hermes-agent/hermes_state.py
0건
```

`SessionDB` 클래스 (`hermes_state.py`, ~2050줄)에서 `agent.redact` 모듈 import 또는 사용 흔적 **0건**.

`SessionDB.append_message` 시그니처 (line 1222, 이전 보고서 §13.2 인용):
```python
def append_message(self, session_id, role, content=None, ..., codex_message_items=None) -> int:
    # JSON 직렬화 → INSERT INTO messages (...) VALUES (...)
    # redaction 호출 없음, 콜백 등록 인자 없음
```

→ **DB INSERT 경로에 Hermes 자체 redaction 미적용 확정**.

---

## 5. R-1 판정

**FAIL** (LLM 송신/도구 출력 전용)

### 5.1 판정 근거

- 사실 1: docstring이 적용 범위 명시 (DB 미포함)
- 사실 2: 25개 import 위치 모두 비-DB 경로
- 사실 3: SessionDB에 redact import 0건

3건 모두 충족 → **R-1 PASS 기준 (DB INSERT 경로 적용 확인) 미충족**.

### 5.2 G1 재판정

풀 합의 §4.2 G1 정의 ("Hermes 자체 redaction이 DB INSERT 경로 적용 확인") 기준으로:

- **G1a (현 정의 — 형태 기준)**: **미충족**. Hermes 자체 redaction은 DB INSERT 경로 미적용.
- **G1b (재정의 후보 — 본질 기준)**: "DB 평문 저장 차단 (보완 메커니즘 포함)" — R-2 결과에 따라 재판정.

---

## 6. 사용자 결정 (확정)

```
R-1 = FAIL 확정
즉시 Hermes 보류 전환은 아직 하지 않음
R-2 DB-level fallback PoC를 1~2일 timebox로 수행
R-2 PASS 시 G1b로 재판정
R-2 FAIL 시 옵션 (a) 자동 전환
R-1 결과는 단독 커밋
```

본 보고서가 위 결정의 R-1 결과 단독 커밋에 해당.

---

## 7. R-2 PoC 작업 정의 (다음 단계)

### 7.1 목표

**SQLite trigger (BEFORE INSERT on messages) + REGEXP user-defined function 으로 DB 평문 저장 차단이 가능한가?**

### 7.2 timebox

**1~2일** (사용자 명시)

### 7.3 검증 항목

1. **SQLCipher가 BEFORE INSERT trigger를 지원하는가** — SQLCipher는 SQLite 위에 암호화 layer만 추가하므로 trigger 지원 추정. 실측 필요.
2. **REGEXP UDF 등록이 SQLCipher에서 동작하는가** — `pysqlcipher3` connection에 `create_function("REGEXP", 2, regex_match)` 호출 후 trigger에서 사용 가능한지.
3. **canary 검증**:
   - 격리 환경에서 인위 비밀 (`sk-ant-CANARY-XXXXX`) 주입
   - LLM 호출 또는 직접 `SessionDB.append_message` 호출
   - trigger 적용 후 `SELECT content FROM messages WHERE content LIKE '%sk-ant-CANARY%'` 결과 0건 확인
4. **redact 패턴 동등성**: trigger의 REGEXP UDF가 P1_REDACTOR와 동등 패턴 커버하는지 (단축 합의 R-4)

### 7.4 PASS / FAIL 기준

- **PASS**: 위 4건 모두 동작 → G1b 재판정 (DB 평문 저장 차단 본질 충족) → 풀 합의 옵션 (1) 유지
- **FAIL**: 1건 이상 미동작 → **자동 옵션 (a) 전환** (Hermes PMO 격상 6~12개월 완전 보류, LiteLLM facade + Claude Code 메모리 + 정량 트리거 ADR)

### 7.5 PoC 산출

- `docs/phase0/day3-r2-sqlite-trigger-poc.md` — PoC 보고서
- 격리 환경 docker-compose 또는 직접 pysqlcipher3 PoC 스크립트
- canary 검증 결과 (SQLite SELECT 결과)

---

## 8. R-1 결과의 의미

### 8.1 P2 v2 §2.1.3 가정 무효화 추가 확인

이전 단축 합의 (`3plus1-consensus-2026-05-05-p2-n1-redaction-reinterpretation.md`)에서 이미 P2 v2 §2.1.3 (`add_pre_record_hook`) 가정 코드의 공식 API 미존재 확정. 본 R-1은 추가로 **Hermes 자체 redaction을 우회 경로로 활용하는 가설도 부분 폐기** — Hermes는 DB INSERT 경로에 redaction을 적용할 의도조차 가지지 않음.

### 8.2 풀 합의 옵션 (1) 채택의 안전성 재확인

R-1 FAIL은 단순히 "Hermes 자체 redaction 신뢰 불가" 신호이며, 풀 합의가 G1을 4 게이트로 분리해 둔 덕분에 **헌법 8조 위반으로 직결되지 않음**. 풀 합의가 즉시 Hermes PMO 격상을 거부하고 4 게이트 후 활성화로 보존한 것이 본 결과로 정당화됨.

### 8.3 시스템 정체성 prequel과의 정합

`docs/architecture/system-identity-prequel.md` §4.2의 G1 정의는 "Hermes 자체 redaction" 형태로 명시되어 있으나, §3.2 "Hermes ≠ root of trust" + 단축 합의 R-3 "수단/목적 분리"와 결합하면 **G1을 본질 기준 (DB 평문 저장 차단 + 보완 메커니즘 포함)** 으로 재정의 가능. R-2 PASS 시 prequel §4.2를 minor revision으로 갱신.

---

## 9. 산출 파일 (본 단계)

- `docs/phase0/day2-r1-redaction-location-verification.md` (본 보고서)

## 10. 다음 작업 진입

R-1 단독 커밋 → R-2 timebox PoC 진입.

---

**Day 2 R-1 종료 시각**: 2026-05-05
**다음 진입점**: R-2 PoC (1~2일 timebox) — `day3-r2-sqlite-trigger-poc.md` 작성
