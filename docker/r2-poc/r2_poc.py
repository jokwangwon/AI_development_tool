"""R-2 PoC: SQLCipher BEFORE INSERT trigger + REGEXP UDF로 DB 평문 secret 차단.

목표 (사용자 요구): "DB-level fallback으로 AI memory/session DB에 plaintext
secret persistence를 차단할 수 있는가?"

차단 방향: secret 포함 INSERT를 RAISE(ABORT)로 확실히 거부 (마스킹 미시도).

검증 6항목:
  C1. SQLCipher 환경에서 BEFORE INSERT trigger 동작
  C2. SQLCipher 환경에서 REGEXP UDF 동작
  C3. canary secret 포함 INSERT 차단
  C4. 정상 메시지 INSERT 성공
  C5. DB 내부에 canary 평문 미존재
  C6. 로그/에러 출력에 canary 평문 미노출

전부 PASS → R-2 PASS → G1b 재판정.
하나라도 FAIL → R-2 FAIL → 옵션 (a) 자동 전환.
"""

from __future__ import annotations

import os
import re
import sys
import tempfile
from pathlib import Path

from pysqlcipher3 import dbapi2 as sqlcipher

DB_KEY = "test-key-r2-poc-not-for-prod"

CANARY_PATTERNS = [
    r"sk-ant-[A-Za-z0-9_-]{10,}",
    r"sk-[A-Za-z0-9_-]{10,}",
    r"ghp_[A-Za-z0-9]{10,}",
    r"AKIA[A-Z0-9]{16}",
    r"xox[baprs]-[A-Za-z0-9-]{10,}",
]

CANARY_SAMPLES = [
    ("anthropic-style", "user query: API key is sk-ant-CANARYDEADBEEF12345 please use it"),
    ("openai-style", "config: sk-CANARYDEADBEEF1234567890 was the key"),
    ("github-pat", "git config http.token=ghp_CANARYDEADBEEF1234"),
    ("aws-akid", "aws access key id AKIACANARY1234567XYZ"),
    ("slack-token", "slack webhook xoxb-CANARY-1234567-XYZ"),
]

SAFE_SAMPLES = [
    ("plain-text", "hello world, this is a normal user message"),
    ("code-snippet", "def foo(): return 42"),
    ("near-but-not-secret", "session_id_count is 5 and token_count is 100"),
]


def regexp(pattern: str, value: object) -> bool:
    """SQLite REGEXP UDF — pattern is 1st arg (RHS), value is 2nd arg (LHS)."""
    if value is None:
        return False
    try:
        return re.search(pattern, str(value)) is not None
    except re.error:
        return False


def header(title: str) -> None:
    print(f"\n=== {title} ===", flush=True)


def check(name: str, ok: bool, detail: str = "") -> bool:
    mark = "PASS" if ok else "FAIL"
    extra = f" — {detail}" if detail else ""
    print(f"  [{mark}] {name}{extra}", flush=True)
    return ok


def safe_repr_error(err: BaseException) -> str:
    """Return error class + safe message — strip any potential secret echo.

    For C6: ensure error output does not echo the original canary plaintext.
    The ABORT message in our trigger is a fixed string that does not include
    NEW.content, so this just confirms the error chain is safe.
    """
    msg = str(err)
    for pat in CANARY_PATTERNS:
        if re.search(pat, msg):
            return f"{type(err).__name__}: <error message contained secret — REDACTED>"
    return f"{type(err).__name__}: {msg}"


def main() -> int:
    results: dict[str, bool] = {}
    leak_observations: list[str] = []

    workdir = Path(tempfile.mkdtemp(prefix="r2-poc-"))
    db_path = workdir / "state.db"
    print(f"[setup] workdir={workdir}", flush=True)
    print(f"[setup] db_path={db_path}", flush=True)

    # --- C2 setup: open SQLCipher + register REGEXP UDF -----------------
    header("C2: SQLCipher 환경에서 REGEXP UDF 등록·동작")
    conn = sqlcipher.connect(str(db_path))
    conn.execute(f"PRAGMA key = '{DB_KEY}'")
    conn.execute("PRAGMA cipher_page_size = 4096")
    try:
        conn.create_function("REGEXP", 2, regexp)
        # Functional check: SELECT 'sk-ant-X' REGEXP 'sk-ant-...'
        cur = conn.execute(
            "SELECT 'sk-ant-CANARYDEADBEEF12345' REGEXP 'sk-ant-[A-Za-z0-9_-]{10,}'"
        )
        (val,) = cur.fetchone()
        results["C2"] = check("REGEXP UDF returns 1 for matching pattern", val == 1)
    except Exception as exc:
        results["C2"] = check(
            "REGEXP UDF registration",
            False,
            detail=safe_repr_error(exc),
        )
        return finish(results, leak_observations)

    # --- Schema -------------------------------------------------------------
    conn.execute(
        """
        CREATE TABLE messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT
        )
        """
    )

    # --- C1 setup: BEFORE INSERT trigger using REGEXP UDF -------------------
    header("C1: BEFORE INSERT trigger 등록·동작")
    pattern_clauses = " OR ".join(
        f"NEW.content REGEXP '{p}'" for p in CANARY_PATTERNS
    )
    trigger_sql = f"""
    CREATE TRIGGER block_secrets_messages
    BEFORE INSERT ON messages
    FOR EACH ROW
    WHEN NEW.content IS NOT NULL AND ({pattern_clauses})
    BEGIN
        SELECT RAISE(ABORT, 'secret-pattern-detected: INSERT blocked by R-2 trigger');
    END;
    """
    try:
        conn.executescript(trigger_sql)
        results["C1"] = check("CREATE TRIGGER 성공", True)
    except Exception as exc:
        results["C1"] = check(
            "CREATE TRIGGER",
            False,
            detail=safe_repr_error(exc),
        )
        return finish(results, leak_observations)

    # --- C4: 정상 메시지 INSERT 성공 ---------------------------------------
    header("C4: 정상 메시지 INSERT 성공")
    safe_ok = True
    for label, content in SAFE_SAMPLES:
        try:
            conn.execute(
                "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
                ("s1", "user", content),
            )
            check(f"safe INSERT [{label}]", True)
        except Exception as exc:
            safe_ok = False
            check(
                f"safe INSERT [{label}]",
                False,
                detail=safe_repr_error(exc),
            )
    conn.commit()
    results["C4"] = safe_ok

    # --- C3: canary INSERT 차단 ---------------------------------------------
    header("C3: canary secret INSERT 차단")
    blocked_ok = True
    for label, content in CANARY_SAMPLES:
        try:
            conn.execute(
                "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
                ("s1", "user", content),
            )
            # If we reach here, the trigger did NOT fire — FAIL
            blocked_ok = False
            check(f"canary INSERT [{label}] blocked", False, "INSERT was NOT blocked")
        except sqlcipher.Error as exc:
            # Expected — trigger raised ABORT (IntegrityError or OperationalError
            # depending on SQLite/sqlcipher version; both are sqlcipher.Error).
            err_msg = safe_repr_error(exc)
            if "secret-pattern-detected" in str(exc):
                check(f"canary INSERT [{label}] blocked", True)
            else:
                check(
                    f"canary INSERT [{label}] blocked",
                    False,
                    detail=f"unexpected error: {err_msg}",
                )
                blocked_ok = False
        except Exception as exc:
            blocked_ok = False
            check(
                f"canary INSERT [{label}] blocked",
                False,
                detail=safe_repr_error(exc),
            )
    conn.commit()
    results["C3"] = blocked_ok

    # --- C5: DB 내부에 canary 평문 미존재 -----------------------------------
    header("C5: DB 내부 canary 평문 부재")
    leak_in_db = False
    cur = conn.execute("SELECT id, role, content FROM messages")
    rows = cur.fetchall()
    print(f"  rows committed: {len(rows)}", flush=True)
    for rid, role, content in rows:
        for pat in CANARY_PATTERNS:
            if content and re.search(pat, content):
                leak_in_db = True
                leak_observations.append(
                    f"row id={rid} role={role} matched pattern={pat[:20]}"
                )
    results["C5"] = check(
        "no canary plaintext in messages.content",
        not leak_in_db,
        detail=f"{len(rows)} rows scanned",
    )

    # Also scan the raw DB file: SQLCipher should keep file encrypted, so
    # plaintext canary should not appear in the file bytes either.
    header("C5-extra: 디스크 파일 byte 수준 검사 (SQLCipher 암호화 확인)")
    file_bytes = db_path.read_bytes()
    file_leak = False
    for pat in CANARY_PATTERNS:
        if re.search(pat.encode(), file_bytes):
            file_leak = True
            leak_observations.append(f"disk byte match: pattern={pat[:20]}")
    check(
        "no canary plaintext in raw db file bytes (SQLCipher encrypted)",
        not file_leak,
        detail=f"file size={len(file_bytes)} bytes",
    )
    # Note: file-level check is informational; C5 (committed rows) is the
    # primary R-2 criterion.

    # --- C6: 로그/에러에 canary 평문 미노출 --------------------------------
    # Throughout this script, every error path uses safe_repr_error() which
    # strips canary patterns. The trigger's ABORT message is a fixed string
    # ('secret-pattern-detected: ...') and does NOT echo NEW.content.
    # We synthesise a final adversarial check: try one more INSERT and
    # capture the resulting error message; verify it contains no canary.
    header("C6: 에러 메시지에 canary 평문 노출 여부")
    test_secret = "sk-ant-CANARYLEAKCHECK99999"
    captured_err = ""
    try:
        conn.execute(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            ("s1", "user", f"sneaky {test_secret} value"),
        )
    except Exception as exc:
        captured_err = str(exc)
    leak_in_err = bool(re.search(r"sk-ant-CANARYLEAKCHECK", captured_err))
    results["C6"] = check(
        "ABORT error message does not echo secret",
        not leak_in_err,
        detail=f"captured_err='{captured_err[:80]}'",
    )

    conn.close()

    return finish(results, leak_observations)


def finish(results: dict[str, bool], leaks: list[str]) -> int:
    header("R-2 PoC 종합 결과")
    order = ["C1", "C2", "C3", "C4", "C5", "C6"]
    titles = {
        "C1": "BEFORE INSERT trigger 동작",
        "C2": "REGEXP UDF 동작",
        "C3": "canary INSERT 차단",
        "C4": "정상 메시지 INSERT 성공",
        "C5": "DB 평문 부재",
        "C6": "에러 출력 평문 미노출",
    }
    all_pass = True
    for k in order:
        ok = results.get(k, False)
        all_pass = all_pass and ok
        print(f"  {k} {titles[k]}: {'PASS' if ok else 'FAIL'}", flush=True)
    if leaks:
        print("\n  leak observations:", flush=True)
        for obs in leaks:
            print(f"    - {obs}", flush=True)
    verdict = "PASS" if all_pass else "FAIL"
    print(f"\n[verdict] R-2 = {verdict}", flush=True)
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
