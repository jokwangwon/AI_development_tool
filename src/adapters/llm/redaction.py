"""RedactionFilter — GP-2 R-2 prevention (LLM 송신 request body secret strip).

SC-1 (65 entry) 합의 산출 (`docs/review/3plus1-consensus-2026-05-28-mvp2-sc1.md`):
  - 권위: governance §4.1 ("LLM API request body 에 secret 노출 차단") + 64 trajectory §3
          (§8.2 RedactionFilter = egress scrub 보조)
  - B-1 (ii): Tier-1 45 catalog single source = redaction_patterns (detection 과 공유)
  - B-2: group-aware 치환 — secret *값* 만 마스킹, key명/JSON 구조 보존 (whole-match 금지)
  - R-3: scrub() KEY_BLACKLIST (dict key 기반 redaction, §8.2 답습)

GP-2 prevention 핵심 = 송신 (redact_messages). 응답/로그 redaction = 보조 (scrub).
순수 함수 / 원본 불변 (R-1) — frozen 의도.
"""
from __future__ import annotations

import re
from typing import Any

from src.adapters.llm.redaction_patterns import (
    COMPILED_PATTERNS,
    REDACTION_MARK,
    REDACTION_VALUE_GROUP,
    SKIP_DIRECT_REGISTER,
)

# §8.2 KEY_BLACKLIST — dict key 기반 redaction (값 통째 마스킹)
KEY_BLACKLIST: frozenset[str] = frozenset(
    {"api_key", "apikey", "token", "secret", "auth", "credential", "authorization", "password"}
)


def _redact_match(m: re.Match[str], value_group: int) -> str:
    """단일 매칭 → group-aware 치환 (B-2). 값만 [REDACTED], key명/구분자 보존."""
    if value_group == 0:
        # whole match 가 secret 값 (prefix/JWT/private key — key명 없음)
        return REDACTION_MARK
    full = m.group(0)
    if value_group == -1:
        # alternation (capturing group 없음) → 첫 '=' 뒤만 (delimiter+key 보존)
        eq = full.find("=")
        return full[: eq + 1] + REDACTION_MARK if eq != -1 else REDACTION_MARK
    # value_group > 0 → 해당 capturing group span 만 마스킹
    if m.lastindex and value_group <= m.lastindex and m.group(value_group) is not None:
        off = m.start()
        start, end = m.span(value_group)
        return full[: start - off] + REDACTION_MARK + full[end - off :]
    return REDACTION_MARK


class RedactionFilter:
    """모든 LLM 송신/응답/로그에서 비밀값 자동 strip (GP-2 prevention)."""

    def redact_text(self, text: str) -> str:
        """str 에서 Tier-1 45 catalog 매칭 secret 값 group-aware 마스킹."""
        result = text
        for pid, _src, _cat, _vendor, pattern in COMPILED_PATTERNS:
            if pid in SKIP_DIRECT_REGISTER:
                continue
            value_group = REDACTION_VALUE_GROUP.get(pid, 0)
            result = pattern.sub(lambda m, vg=value_group: _redact_match(m, vg), result)
        return result

    def redact_messages(self, messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """송신 request body redaction (GP-2 prevention 핵심). 원본 불변 (R-1)."""
        out: list[dict[str, Any]] = []
        for msg in messages:
            new_msg = dict(msg)  # shallow copy (원본 dict 불변)
            content = new_msg.get("content")
            if isinstance(content, str):
                new_msg["content"] = self.redact_text(content)
            elif isinstance(content, (list, dict)):
                # multimodal/tool structured content → 재귀 (R-5)
                new_msg["content"] = self.scrub(content)
            out.append(new_msg)
        return out

    def scrub(self, obj: Any) -> Any:
        """dict/list/str 재귀 redaction (응답/메트릭/로그, §8.2) + KEY_BLACKLIST (R-3). 원본 불변."""
        if isinstance(obj, dict):
            result: dict[Any, Any] = {}
            for key, value in obj.items():
                if isinstance(key, str) and key.lower() in KEY_BLACKLIST:
                    # blacklist key → 값 통째 마스킹 (str) 또는 재귀
                    result[key] = REDACTION_MARK if isinstance(value, str) else self.scrub(value)
                else:
                    result[key] = self.scrub(value)
            return result
        if isinstance(obj, list):
            return [self.scrub(item) for item in obj]
        if isinstance(obj, str):
            return self.redact_text(obj)
        return obj  # int / float / bool / None — 비밀 아님
