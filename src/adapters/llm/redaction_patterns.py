"""Tier-1 secret pattern catalog — single source (detection + prevention 공유).

본 모듈은 SC-1 (65 entry) 합의 B-1 (ii) 공유 모듈 추출 산출:
  - `tools/secret_scanner.py` (detection, GP-3 + GP-2 D-2 scan-log)
  - `src/adapters/llm/redaction.py` (prevention, GP-2 R-2 facade RedactionFilter 송신 redaction)
둘 다 본 catalog 를 import → detection ↔ prevention 패턴 drift 0 (single source).

⚠️ 패턴 *내용* (id / source / category / vendor / regex) = R-4.1 §4.1 직접 답습 변경 0건.
secret_scanner 에서 literal 그대로 이동 (equivalence test 강제: len(ALL_PATTERNS)==45 + snapshot 동일).

답습 출처:
  - docs/phase0/r4-1-trigger-extension-evidence.md §4.1 (Tier-1 42 + baseline 5 = 45)
  - docs/architecture/redaction-pattern-equivalence.md (R-4 패턴 동등성)
  - docs/architecture/llm-providers-design.md §8.2 (RedactionFilter 설계)
  - docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md (B-1 (ii) + B-2 group-aware 치환)
"""
from __future__ import annotations

import re

# ============================================================================
# Tier-1 패턴 카탈로그 (45종) — R-4.1 §4.1 직접 답습 (secret_scanner literal 이동, 변경 0)
#
# 형식: (id, source, category, vendor, regex)
# ============================================================================

# Baseline 5 prefix (R-2 PoC 보존 — R-4.1 §4.1)
BASELINE_PREFIX: list[tuple[str, str, str, str, str]] = [
    ("BL-1", "Hermes #1 (sk-ant-)", "prefix-baseline", "Anthropic",
     r"sk-ant-[A-Za-z0-9_-]{10,}"),
    ("BL-2", "Hermes #1 (sk-)", "prefix-baseline", "OpenAI/Anthropic/etc",
     r"sk-[A-Za-z0-9_-]{10,}"),
    ("BL-3", "Hermes #2", "prefix-baseline", "GitHub PAT classic",
     r"ghp_[A-Za-z0-9]{10,}"),
    ("BL-4", "Hermes #15", "prefix-baseline", "AWS Access Key ID",
     r"AKIA[A-Z0-9]{16}"),
    ("BL-5", "Hermes #8", "prefix-baseline", "Slack tokens",
     r"xox[baprs]-[A-Za-z0-9-]{10,}"),
]

# Tier-1 prefix 31 (Hermes #3..#7, #9..#14, #16..#35) — R-4.1 §4.1 직접 답습
PREFIX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-001", "Hermes #3", "prefix", "GitHub PAT (fine-grained)",
     r"github_pat_[A-Za-z0-9_]{10,}"),
    ("T1-002", "Hermes #4", "prefix", "GitHub OAuth access token",
     r"gho_[A-Za-z0-9]{10,}"),
    ("T1-003", "Hermes #5", "prefix", "GitHub user-to-server",
     r"ghu_[A-Za-z0-9]{10,}"),
    ("T1-004", "Hermes #6", "prefix", "GitHub server-to-server",
     r"ghs_[A-Za-z0-9]{10,}"),
    ("T1-005", "Hermes #7", "prefix", "GitHub refresh token",
     r"ghr_[A-Za-z0-9]{10,}"),
    ("T1-006", "Hermes #9", "prefix", "Google API keys",
     r"AIza[A-Za-z0-9_-]{30,}"),
    ("T1-007", "Hermes #10", "prefix", "Perplexity",
     r"pplx-[A-Za-z0-9]{10,}"),
    ("T1-008", "Hermes #11", "prefix", "Fal.ai",
     r"fal_[A-Za-z0-9_-]{10,}"),
    ("T1-009", "Hermes #12", "prefix", "Firecrawl",
     r"fc-[A-Za-z0-9]{10,}"),
    ("T1-010", "Hermes #13", "prefix", "BrowserBase",
     r"bb_live_[A-Za-z0-9_-]{10,}"),
    ("T1-011", "Hermes #14", "prefix", "Codex encrypted tokens",
     r"gAAAA[A-Za-z0-9_=-]{20,}"),
    ("T1-012", "Hermes #16", "prefix", "Stripe secret key (live)",
     r"sk_live_[A-Za-z0-9]{10,}"),
    ("T1-013", "Hermes #17", "prefix", "Stripe secret key (test)",
     r"sk_test_[A-Za-z0-9]{10,}"),
    ("T1-014", "Hermes #18", "prefix", "Stripe restricted key",
     r"rk_live_[A-Za-z0-9]{10,}"),
    ("T1-015", "Hermes #19", "prefix", "SendGrid API key",
     r"SG\.[A-Za-z0-9_-]{10,}"),
    ("T1-016", "Hermes #20", "prefix", "HuggingFace token",
     r"hf_[A-Za-z0-9]{10,}"),
    ("T1-017", "Hermes #21", "prefix", "Replicate API token",
     r"r8_[A-Za-z0-9]{10,}"),
    ("T1-018", "Hermes #22", "prefix", "npm access token",
     r"npm_[A-Za-z0-9]{10,}"),
    ("T1-019", "Hermes #23", "prefix", "PyPI API token",
     r"pypi-[A-Za-z0-9_-]{10,}"),
    ("T1-020", "Hermes #24", "prefix", "DigitalOcean PAT",
     r"dop_v1_[A-Za-z0-9]{10,}"),
    ("T1-021", "Hermes #25", "prefix", "DigitalOcean OAuth",
     r"doo_v1_[A-Za-z0-9]{10,}"),
    ("T1-022", "Hermes #26", "prefix", "AgentMail API key",
     r"am_[A-Za-z0-9_-]{10,}"),
    ("T1-023", "Hermes #27", "prefix", "ElevenLabs TTS key",
     r"sk_[A-Za-z0-9_]{10,}"),
    ("T1-024", "Hermes #28", "prefix", "Tavily search API",
     r"tvly-[A-Za-z0-9]{10,}"),
    ("T1-025", "Hermes #29", "prefix", "Exa search API",
     r"exa_[A-Za-z0-9]{10,}"),
    ("T1-026", "Hermes #30", "prefix", "Groq Cloud API key",
     r"gsk_[A-Za-z0-9]{10,}"),
    ("T1-027", "Hermes #31", "prefix", "Matrix access token",
     r"syt_[A-Za-z0-9]{10,}"),
    ("T1-028", "Hermes #32", "prefix", "RetainDB API key",
     r"retaindb_[A-Za-z0-9]{10,}"),
    ("T1-029", "Hermes #33", "prefix", "Hindsight API key",
     r"hsk-[A-Za-z0-9]{10,}"),
    ("T1-030", "Hermes #34", "prefix", "Mem0 Platform API key",
     r"mem0_[A-Za-z0-9]{10,}"),
    ("T1-031", "Hermes #35", "prefix", "ByteRover API key",
     r"brv_[A-Za-z0-9]{10,}"),
]

# Tier-1 추가 regex 7 (H-A, H-B, H-C, H-E, H-F, H-G, H-K — H-J/H-L 제외, R-4.1 §4.2 답습)
REGEX_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-032", "Hermes H-A", "regex", "ENV assignment",
     r"([A-Z0-9_]{0,50}(?:API_?KEY|TOKEN|SECRET|PASSWORD|PASSWD|CREDENTIAL|AUTH)[A-Z0-9_]{0,50})\s*=\s*(['\"]?)(\S+)\2"),
    ("T1-033", "Hermes H-B", "regex", "JSON field with secret keys",
     r'(?i)("(?:api_?[Kk]ey|token|secret|password|access_token|refresh_token|auth_token|bearer|secret_value|raw_secret|secret_input|key_material)")\s*:\s*"([^"]+)"'),
    ("T1-034", "Hermes H-C", "regex", "Authorization header (Bearer)",
     r"(?i)(Authorization:\s*Bearer\s+)(\S+)"),
    ("T1-035", "Hermes H-E", "regex", "Private key block",
     r"-----BEGIN[A-Z ]*PRIVATE KEY-----[\s\S]*?-----END[A-Z ]*PRIVATE KEY-----"),
    ("T1-036", "Hermes H-F", "regex", "DB connstr password",
     r"(?i)((?:postgres(?:ql)?|mysql|mongodb(?:\+srv)?|redis|amqp)://[^:]+:)([^@]+)(@)"),
    ("T1-037", "Hermes H-G", "regex", "JWT token",
     r"eyJ[A-Za-z0-9_-]{10,}(?:\.[A-Za-z0-9_=-]{4,}){0,2}"),
    ("T1-039", "Hermes H-K", "regex", "URL userinfo (non-DB)",
     r"(https?|wss?|ftp)://([^/\s:@]+):([^/\s@]+)@"),
]

# Tier-1 alternation 2 (H-J / H-L sensitive key 기반 변환, R-4.1 §4.1 답습)
ALTERNATION_PATTERNS: list[tuple[str, str, str, str, str]] = [
    ("T1-041", "Hermes _SENSITIVE_QUERY_PARAMS", "alternation", "URL query sensitive keys (16)",
     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|session|secret|key|code|signature|x-amz-signature)=[^&\s]+"),
    ("T1-042", "Hermes _SENSITIVE_BODY_KEYS", "alternation", "Body/form sensitive keys (14)",
     r"(?i)(?:^|[?&\s'\";#])(?:access_token|refresh_token|id_token|token|api_key|apikey|client_secret|password|auth|jwt|secret|private_key|authorization|key)=[^&\s]+"),
]

ALL_PATTERNS: list[tuple[str, str, str, str, str]] = (
    BASELINE_PREFIX + PREFIX_PATTERNS + REGEX_PATTERNS + ALTERNATION_PATTERNS
)
"""All registered patterns — 5 baseline + 31 prefix + 7 regex + 2 alternation = 45 patterns."""

# Compiled regex objects (모듈 import 시 1회 컴파일)
COMPILED_PATTERNS: list[tuple[str, str, str, str, re.Pattern[str]]] = [
    (pid, src, cat, vendor, re.compile(rgx))
    for (pid, src, cat, vendor, rgx) in ALL_PATTERNS
]

# 본 PoC 직접 등록 제외 (R-4.1 §4.2 답습 — alternation 채택, H-J/H-L 직접 등록 false-positive 회피)
SKIP_DIRECT_REGISTER: frozenset[str] = frozenset({"T1-038", "T1-040"})

# ============================================================================
# Redaction value group 메타 (B-2 group-aware 치환 — prevention 전용, detection 무관)
#
# pattern_id → secret *값* 의 capturing group index.
#   0   = whole match 가 secret 값 (prefix/JWT/private key — key명 없음, 구조 손상 0)
#   N>0 = 해당 capturing group 만 마스킹 (key명/구분자 보존)
#   -1  = alternation (capturing group 없음) → 첫 '=' 뒤만 마스킹 (delimiter+key 보존)
# 미등재 = 0 (whole) default.
#
# 본 매핑 = redaction 처리 메타이며 패턴 *내용* 이 아님 (equivalence test snapshot 무관).
# ============================================================================
REDACTION_VALUE_GROUP: dict[str, int] = {
    "T1-032": 3,   # ENV assignment — group 3 = value
    "T1-033": 2,   # JSON field — group 2 = value
    "T1-034": 2,   # Authorization Bearer — group 2 = token
    "T1-036": 2,   # DB connstr — group 2 = password (group 3 = '@' 보존)
    "T1-039": 3,   # URL userinfo — group 3 = password
    "T1-041": -1,  # alternation — '=' 뒤
    "T1-042": -1,  # alternation — '=' 뒤
    # 그 외 (prefix/baseline, T1-035 private key, T1-037 JWT) = 0 (whole) default
}

# Redaction marker (RedactionFilter 출력 + secret_scanner scan-log FP 회피 정합).
REDACTION_MARK: str = "[REDACTED]"
