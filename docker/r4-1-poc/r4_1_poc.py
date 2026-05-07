"""R-4.1 PoC: Tier-1 42종 trigger UDF 확장 + R-2 격리 환경 재실행.

목표: ADR-011 §2.1 (b) 격리 환경 PoC 실증을 직접 충족.
       R-4 §6/§7 권고 카탈로그 (Hermes 측 Tier-1 41~42종) 를 trigger UDF에 반영하고,
       각 패턴별 C1 canary inject 결과를 evidence로 기록.

R-4 §7.2 enumerate 정정:
  R-4 §7.2 헤딩 "41종 (Prefix 30 + regex 9 + frozenset 2)" 표현은 prefix
  카운트 산술 오류로 추정. R-4 §6.2.1 카탈로그를 직접 enumerate하면
  prefix 31종 (Hermes 35 - baseline 4) + regex 9종 + alternation 2종 = 42종.
  본 R-4.1은 사용자 결정 "Tier-1 41종"의 본질 (Hermes 측 Tier-1 카탈로그
  전수 반영) 을 충족하기 위해 enumerate 42종으로 진행.

검증 항목 (R-4.1 PASS 기준):
  C1. BEFORE INSERT trigger 등록 성공
  C2. REGEXP UDF 등록·동작
  C3. Tier-1 42종 canary INSERT 모두 차단
  C4. 정상 safe message INSERT 모두 성공
  C5. DB 평문 부재 (memory/session DB 모두 검사)
  C6. 에러 메시지에 canary 평문 미노출

전체 PASS → R-4.1 PASS → ADR-011 §2.1 (b) 직접 충족 evidence 생성.
하나라도 FAIL → R-4.1 PARTIAL/FAIL.
"""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
from pathlib import Path

from pysqlcipher3 import dbapi2 as sqlcipher

DB_KEY = "test-key-r4-1-poc-not-for-prod"

# ============================================================================
# Tier-1 패턴 카탈로그 (42종) — R-4 §6.2 enumerate
#
# 형식: (id, source, category, vendor, regex, canary)
#   - id: T1-001 ~ T1-042
#   - source: Hermes 측 출처 식별자 (#NN = _PREFIX_PATTERNS index, H-X = 추가 regex)
#   - category: prefix / regex / alternation
#   - vendor: 사람이 읽을 수 있는 vendor/유형 라벨
#   - regex: trigger UDF 등록용 정규식 문자열
#   - canary: C1 inject 시 사용할 입력 메시지 (NOT-A-REAL-SECRET 명시)
# ============================================================================

# Prefix patterns (31종, Hermes #3~#7,#9~#14,#16~#35)
PREFIX_PATTERNS = [
    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
     r"github_pat_[A-Za-z0-9_]{10,}",
     "config token=github_pat_CANARYR41T001NOTAREAL"),
    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
     r"gho_[A-Za-z0-9]{10,}",
     "user gho_CANARYR41T002NOTAREAL value"),
    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
     r"ghu_[A-Za-z0-9]{10,}",
     "ghu_CANARYR41T003NOTAREAL hint"),
    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
     r"ghs_[A-Za-z0-9]{10,}",
     "tok ghs_CANARYR41T004NOTAREAL string"),
    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
     r"ghr_[A-Za-z0-9]{10,}",
     "refresh ghr_CANARYR41T005NOTAREAL boom"),
    ("T1-006", "Hermes #9", "prefix", "Google API keys",
     r"AIza[A-Za-z0-9_-]{30,}",
     "key AIzaCANARYR41T006NOTAREALSECRETTOKEN001 ok"),
    ("T1-007", "Hermes #10", "prefix", "Perplexity",
     r"pplx-[A-Za-z0-9]{10,}",
     "pplx-CANARYR41T007NOTAREAL test"),
    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
     r"fal_[A-Za-z0-9_-]{10,}",
     "fal_CANARYR41T008NOTAREAL key"),
    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
     r"fc-[A-Za-z0-9]{10,}",
     "fc-CANARYR41T009NOTAREAL crawl"),
    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
     r"bb_live_[A-Za-z0-9_-]{10,}",
     "bb_live_CANARYR41T010NOTAREAL session"),
    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
     r"gAAAA[A-Za-z0-9_=-]{20,}",
     "tok gAAAACANARYR41T011NOTAREAL_=AAAAA codex"),
    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
     r"sk_live_[A-Za-z0-9]{10,}",
     "stripe sk_live_CANARYR41T012NOTAREAL ok"),
    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
     r"sk_test_[A-Za-z0-9]{10,}",
     "stripe sk_test_CANARYR41T013NOTAREAL test"),
    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
     r"rk_live_[A-Za-z0-9]{10,}",
     "stripe rk_live_CANARYR41T014NOTAREAL ok"),
    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
     r"SG\.[A-Za-z0-9_-]{10,}",
     "send SG.CANARYR41T015NOTAREAL email"),
    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
     r"hf_[A-Za-z0-9]{10,}",
     "hf_CANARYR41T016NOTAREAL model"),
    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
     r"r8_[A-Za-z0-9]{10,}",
     "tok r8_CANARYR41T017NOTAREAL replicate"),
    ("T1-018", "Hermes #22", "prefix", "npm access token",
     r"npm_[A-Za-z0-9]{10,}",
     "npm_CANARYR41T018NOTAREAL install"),
    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
     r"pypi-[A-Za-z0-9_-]{10,}",
     "pypi-CANARYR41T019NOTAREAL upload"),
    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
     r"dop_v1_[A-Za-z0-9]{10,}",
     "dop_v1_CANARYR41T020NOTAREAL droplet"),
    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
     r"doo_v1_[A-Za-z0-9]{10,}",
     "doo_v1_CANARYR41T021NOTAREAL oauth"),
    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
     r"am_[A-Za-z0-9_-]{10,}",
     "am_CANARYR41T022NOTAREAL agentmail"),
    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
     r"sk_[A-Za-z0-9_]{10,}",
     "elevenlabs sk_CANARYR41T023NOTAREAL_speak"),
    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
     r"tvly-[A-Za-z0-9]{10,}",
     "tvly-CANARYR41T024NOTAREAL search"),
    ("T1-025", "Hermes #29", "prefix", "Exa search API",
     r"exa_[A-Za-z0-9]{10,}",
     "exa_CANARYR41T025NOTAREAL search"),
    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
     r"gsk_[A-Za-z0-9]{10,}",
     "gsk_CANARYR41T026NOTAREAL llama"),
    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
     r"syt_[A-Za-z0-9]{10,}",
     "syt_CANARYR41T027NOTAREAL matrix"),
    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
     r"retaindb_[A-Za-z0-9]{10,}",
     "retaindb_CANARYR41T028NOTAREAL data"),
    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
     r"hsk-[A-Za-z0-9]{10,}",
     "hsk-CANARYR41T029NOTAREAL hindsight"),
    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
     r"mem0_[A-Za-z0-9]{10,}",
     "mem0_CANARYR41T030NOTAREAL memory"),
    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
     r"brv_[A-Za-z0-9]{10,}",
     "brv_CANARYR41T031NOTAREAL bytre"),
]

# Additional regex patterns (9종, Hermes H-A,B,C,E,F,G,J,K,L)
REGEX_PATTERNS = [
    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2",
     "export OPENAI_API_KEY=fakecanaryR41T032NOTAREAL"),
    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"',
     'config {"api_key": "fakecanaryR41T033NOTAREAL"} loaded'),
    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
     r"(?i)(Authorization:\s*Bearer\s+)(\S+)",
     "headers Authorization: Bearer fakecanaryR41T034NOTAREAL ok"),
    ("T1-035", "Hermes H-E", "regex", "Private key block",
     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----",
     "key -----BEGIN PRIVATE KEY-----\nfakecanaryR41T035NOTAREAL\n-----END PRIVATE KEY----- end"),
    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)",
     "db postgres://user:fakecanaryR41T036NOTAREAL@host:5432/db loaded"),
    ("T1-037", "Hermes H-G", "regex", "JWT token",
     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}",
     "tok eyJfakecanaryR41T037NOTAREAL.eyJpayloadFAKEr41t037.signfakeR41T037 ok"),
    ("T1-038", "Hermes H-J", "regex", "URL query secrets",
     r"(https?|wss?|ftp)://([^\s/?#]+)([^\s?#]*)\?([^\s#]+)(#\S*)?",
     "redirect https://example.com/cb?access_token=fakecanaryR41T038NOTAREAL&state=x"),
    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@",
     "url https://user:fakecanaryR41T039NOTAREAL@api.example.com/v1"),
    ("T1-040", "Hermes H-L", "regex", "Form-urlencoded body",
     r"^[A-Za-z_][A-Za-z0-9_.-]*=[^&\s]*(?:&[A-Za-z_][A-Za-z0-9_.-]*=[^&\s]*)+$",
     "access_token=fakecanaryR41T040NOTAREAL&user=alice"),
]

# Frozenset alternation patterns (2종, Hermes URL/body sensitive keys)
ALTERNATION_PATTERNS = [
    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+",
     "redirect https://x.com/cb?api_key=fakecanaryR41T041NOTAREAL&q=hi"),
    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
     r"(?i)(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+",
     "form payload password=fakecanaryR41T042NOTAREAL&user=alice"),
]

TIER1_PATTERNS = PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS

# Baseline 4 prefix (R-2 PoC 그대로 보존, trigger 등록 유지)
BASELINE_PREFIX = [
    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
     r"sk-ant-[A-Za-z0-9_-]{10,}", None),
    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
     r"sk-[A-Za-z0-9_-]{10,}", None),
    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
     r"ghp_[A-Za-z0-9]{10,}", None),
    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
     r"AKIA[A-Z0-9]{16}", None),
    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
     r"xox[baprs]-[A-Za-z0-9-]{10,}", None),
]

# H-J `_URL_WITH_QUERY_RE` 와 H-L `_FORM_BODY_RE` 는 trigger 직접 등록에서 제외:
#   - 1차 실행에서 false-positive 발견 (모든 URL+query / form-shaped body 차단)
#   - R-4 §7.2.3 alternation 변환 (T1-041, T1-042) 이 sensitive key 기반 매칭 담당
#   - H-J/H-L canary (T1-038, T1-040) 는 alternation T1-041/T1-042 에 의해 매칭 차단 보장
SKIP_TRIGGER_REGISTER = {"T1-038", "T1-040"}
ALL_TRIGGER_REGEXES = (
    [p[4] for p in BASELINE_PREFIX]
    + [p[4] for p in TIER1_PATTERNS if p[0] not in SKIP_TRIGGER_REGISTER]
)

# Safe samples (정상 INSERT 성공해야 함, false-positive 회피 검증)
SAFE_SAMPLES = [
    ("plain-text", "hello world, this is a normal user message"),
    ("code-snippet", "def foo(): return 42"),
    ("near-but-not-secret", "session_id_count is 5 and token_count is 100"),
    ("safe-json", '{"username": "alice", "user_id": 12345, "page": 2}'),
    ("safe-url", "https://example.com/api/users"),
    ("safe-url-with-query", "https://example.com/api?q=hello&page=2&lang=en"),
    ("safe-form-no-secret", "theme=dark&lang=en&page=3"),
    ("ascii-art", "+--+--+ | x | y | +--+--+"),
    ("markdown-link", "see [docs](https://example.com/docs) for details"),
]

# C5/C6 leak detection: literal markers, not Hermes regex.
# Hermes 정규식 (특히 H-J URL_WITH_QUERY_RE 와 H-L FORM_BODY_RE) 은 형식 매칭이라
# safe sample (`https://...?q=hello`, `theme=dark&lang=en`) 도 매칭 → false-leak 위험.
# 모든 R-4.1 canary 는 공통 marker `R41T` 를 포함하므로 literal substring 검사가 정확.
CANARY_LITERAL_MARKERS = [b"R41T"]


def regexp(pattern: str, value: object) -> bool:
    """SQLite REGEXP UDF — pattern is 1st arg (RHS), value is 2nd arg (LHS).

    Inline flags `(?i)` 등은 Python re.search 가 자체 인식.
    """
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
    """Return error class + safe message — strip any potential canary echo.

    For C6: ensure error output does not echo any R-4.1 canary marker.
    The ABORT message is a fixed string ('secret-pattern-detected: ...').
    """
    msg = str(err).encode(errors="ignore")
    for marker in CANARY_LITERAL_MARKERS:
        if marker in msg:
            return f"{type(err).__name__}: <error contained canary — REDACTED>"
    return f"{type(err).__name__}: {str(err)}"


def main() -> int:
    summary: dict[str, object] = {
        "tier1_count": len(TIER1_PATTERNS),
        "baseline_count": len(BASELINE_PREFIX),
        "trigger_pattern_total": len(ALL_TRIGGER_REGEXES),
        "results": {},
        "tier1_canary_results": [],
        "leak_observations": [],
        "safe_results": [],
    }
    results: dict[str, bool] = {}
    leak_observations: list[str] = []

    workdir = Path(tempfile.mkdtemp(prefix="r4-1-poc-"))
    db_path = workdir / "state.db"
    print(f"[setup] workdir={workdir}", flush=True)
    print(f"[setup] db_path={db_path}", flush=True)
    print(f"[setup] tier1_count={len(TIER1_PATTERNS)}", flush=True)
    print(f"[setup] baseline_count={len(BASELINE_PREFIX)}", flush=True)
    print(f"[setup] trigger_pattern_total={len(ALL_TRIGGER_REGEXES)}", flush=True)

    # --- C2: SQLCipher + REGEXP UDF -----------------------------------------
    header("C2: SQLCipher 환경에서 REGEXP UDF 등록·동작")
    conn = sqlcipher.connect(str(db_path))
    conn.execute(f"PRAGMA key = '{DB_KEY}'")
    conn.execute("PRAGMA cipher_page_size = 4096")
    try:
        conn.create_function("REGEXP", 2, regexp)
        cur = conn.execute(
            "SELECT 'sk-ant-CANARYR41check12345' REGEXP 'sk-ant-[A-Za-z0-9_-]{10,}'"
        )
        (val,) = cur.fetchone()
        results["C2"] = check("REGEXP UDF returns 1 for matching pattern", val == 1)
    except Exception as exc:
        results["C2"] = check(
            "REGEXP UDF registration", False, detail=safe_repr_error(exc)
        )
        return finish(results, summary, leak_observations)

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

    # --- C1: trigger 등록 ----------------------------------------------------
    header("C1: BEFORE INSERT trigger 등록 (Tier-1 42종 + baseline 5)")
    pattern_clauses = " OR ".join(
        f"NEW.content REGEXP {sql_quote(p)}" for p in ALL_TRIGGER_REGEXES
    )
    trigger_sql = f"""
    CREATE TRIGGER block_secrets_messages
    BEFORE INSERT ON messages
    FOR EACH ROW
    WHEN NEW.content IS NOT NULL AND ({pattern_clauses})
    BEGIN
        SELECT RAISE(ABORT, 'secret-pattern-detected: INSERT blocked by R-4.1 trigger');
    END;
    """
    try:
        conn.executescript(trigger_sql)
        results["C1"] = check(
            f"CREATE TRIGGER 성공 ({len(ALL_TRIGGER_REGEXES)} regex registered)", True
        )
    except Exception as exc:
        results["C1"] = check(
            "CREATE TRIGGER", False, detail=safe_repr_error(exc)
        )
        return finish(results, summary, leak_observations)

    # --- C4: 정상 메시지 INSERT 성공 ---------------------------------------
    header("C4: 정상 safe message INSERT 성공 (false-positive 회피)")
    safe_ok = True
    for label, content in SAFE_SAMPLES:
        try:
            conn.execute(
                "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
                ("s1", "user", content),
            )
            check(f"safe INSERT [{label}]", True)
            summary["safe_results"].append(
                {"label": label, "result": "PASS"}
            )
        except Exception as exc:
            safe_ok = False
            check(
                f"safe INSERT [{label}]",
                False,
                detail=safe_repr_error(exc),
            )
            summary["safe_results"].append(
                {"label": label, "result": "FAIL", "error": safe_repr_error(exc)}
            )
    conn.commit()
    results["C4"] = safe_ok

    # --- C3: Tier-1 42종 canary INSERT 차단 -----------------------------------
    header("C3: Tier-1 42종 canary INSERT 차단")
    blocked_ok = True
    for tid, source, category, vendor, _regex, canary in TIER1_PATTERNS:
        actual = "ALLOW"  # default
        result = "FAIL"
        err_brief = ""
        try:
            conn.execute(
                "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
                ("s1", "user", canary),
            )
            blocked_ok = False
            actual = "ALLOW"
            result = "FAIL"
            check(
                f"{tid} [{category}/{vendor}] blocked", False,
                "INSERT was NOT blocked",
            )
        except sqlcipher.Error as exc:
            err_msg = str(exc)
            if "secret-pattern-detected" in err_msg:
                actual = "BLOCK"
                result = "PASS"
                check(f"{tid} [{category}/{vendor}] blocked", True)
            else:
                blocked_ok = False
                actual = f"ERROR: {type(exc).__name__}"
                result = "FAIL"
                err_brief = safe_repr_error(exc)
                check(
                    f"{tid} [{category}/{vendor}] blocked",
                    False,
                    detail=f"unexpected error: {err_brief}",
                )
        except Exception as exc:
            blocked_ok = False
            actual = f"ERROR: {type(exc).__name__}"
            result = "FAIL"
            err_brief = safe_repr_error(exc)
            check(
                f"{tid} [{category}/{vendor}] blocked",
                False,
                detail=err_brief,
            )

        summary["tier1_canary_results"].append({
            "id": tid,
            "source": source,
            "category": category,
            "vendor": vendor,
            "expected": "BLOCK",
            "actual": actual,
            "result": result,
        })
    conn.commit()
    results["C3"] = blocked_ok

    # --- C5: DB 평문 부재 ---------------------------------------------------
    # Literal marker `R41T` 검사 — 모든 R-4.1 canary 가 이 substring 포함.
    # canary 차단이 정상 작동했다면 INSERT 자체가 거부되어 row 에 marker 잔존 불가.
    header("C5: DB 평문 부재 — committed rows + raw bytes (literal marker R41T)")
    leak_in_db = False
    cur = conn.execute("SELECT id, role, content FROM messages")
    rows = cur.fetchall()
    print(f"  rows committed: {len(rows)}", flush=True)
    for rid, role, content in rows:
        if content is None:
            continue
        content_b = content.encode(errors="ignore")
        for marker in CANARY_LITERAL_MARKERS:
            if marker in content_b:
                leak_in_db = True
                leak_observations.append(
                    f"row id={rid} role={role} contains marker={marker.decode()}"
                )
    results["C5"] = check(
        "no canary marker in messages.content",
        not leak_in_db,
        detail=f"{len(rows)} rows scanned, markers={[m.decode() for m in CANARY_LITERAL_MARKERS]}",
    )

    # Raw byte check (SQLCipher encryption)
    file_bytes = db_path.read_bytes()
    file_leak = False
    for marker in CANARY_LITERAL_MARKERS:
        if marker in file_bytes:
            file_leak = True
            leak_observations.append(f"disk byte match: marker={marker.decode()}")
    check(
        "no canary marker in raw db file bytes (SQLCipher encrypted)",
        not file_leak,
        detail=f"file size={len(file_bytes)} bytes",
    )

    # --- C6: 에러 메시지에 canary 평문 미노출 ------------------------------
    header("C6: 에러 메시지에 canary 평문 미노출")
    test_canary = "sk-ant-CANARYR41C6LEAKCHECK99999"
    captured_err = ""
    try:
        conn.execute(
            "INSERT INTO messages (session_id, role, content) VALUES (?, ?, ?)",
            ("s1", "user", f"sneaky {test_canary} value"),
        )
    except Exception as exc:
        captured_err = str(exc)
    leak_in_err = bool(re.search(r"sk-ant-CANARYR41C6LEAKCHECK", captured_err))
    results["C6"] = check(
        "ABORT error message does not echo canary",
        not leak_in_err,
        detail=f"captured_err='{captured_err[:80]}'",
    )

    conn.close()
    summary["leak_observations"] = leak_observations
    return finish(results, summary, leak_observations)


def sql_quote(s: str) -> str:
    """Quote string for SQL trigger body — escape single quotes."""
    return "'" + s.replace("'", "''") + "'"


def finish(results: dict[str, bool], summary: dict, leaks: list[str]) -> int:
    header("R-4.1 PoC 종합 결과")
    order = ["C1", "C2", "C3", "C4", "C5", "C6"]
    titles = {
        "C1": "BEFORE INSERT trigger 등록",
        "C2": "REGEXP UDF 동작",
        "C3": "Tier-1 42종 canary INSERT 차단",
        "C4": "정상 safe message INSERT 성공",
        "C5": "DB 평문 부재",
        "C6": "에러 출력 평문 미노출",
    }
    all_pass = True
    for k in order:
        ok = results.get(k, False)
        all_pass = all_pass and ok
        print(f"  {k} {titles[k]}: {'PASS' if ok else 'FAIL'}", flush=True)
    summary["results"] = {k: ("PASS" if results.get(k, False) else "FAIL") for k in order}
    if leaks:
        print("\n  leak observations:", flush=True)
        for obs in leaks:
            print(f"    - {obs}", flush=True)

    # Tier-1 PASS 집계
    tier1_pass = sum(1 for r in summary["tier1_canary_results"] if r["result"] == "PASS")
    tier1_total = len(summary["tier1_canary_results"])
    print(f"\n  Tier-1 canary PASS rate: {tier1_pass}/{tier1_total}", flush=True)

    # PASS / PARTIAL / FAIL 판정
    if all_pass and tier1_pass == tier1_total:
        verdict = "PASS"
    elif tier1_pass >= 1 or any(results.get(k, False) for k in order):
        verdict = "PARTIAL"
    else:
        verdict = "FAIL"
    print(f"\n[verdict] R-4.1 = {verdict}", flush=True)
    summary["verdict"] = verdict
    summary["tier1_pass_rate"] = f"{tier1_pass}/{tier1_total}"

    # JSON dump for evidence document
    print("\n=== JSON_EVIDENCE_BEGIN ===", flush=True)
    print(json.dumps(summary, indent=2, ensure_ascii=False), flush=True)
    print("=== JSON_EVIDENCE_END ===", flush=True)

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
