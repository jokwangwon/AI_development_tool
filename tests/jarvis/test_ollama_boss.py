"""OllamaBoss — Ollama HTTP `/api/chat` 직결 BossLLM 구현 (TDD).

답습: docs/phase0/jarvis-v00-working-sprint-brief.md §2
  - BossLLM Protocol 충족(`name`, `advise(AdviceRequest) -> BossAdvice`)
  - stdlib `urllib.request` 단독(신규 dep 0, `ollama` SDK import 0 — `.importlinter` 답습)
  - endpoint = `http://localhost:11434/api/chat` 하드코딩(SSRF 회피)
  - HTTP 실패 → RuntimeError (R3 호출측 누락→경고 변환 답습)
  - 응답 → BossAdvice(summary=text, extra_flags=[], advisory_failed=False)

본 test 는 실 HTTP 호출 0건 — urllib.request.urlopen monkeypatch 한정.
"""
from __future__ import annotations

import io
import json
from typing import Any
from unittest.mock import patch

import pytest

from src.jarvis.boss import AdviceRequest, BossAdvice, BossLLM, OllamaBoss


def _fake_response(payload: dict[str, Any]) -> io.BytesIO:
    """urlopen 응답 객체 모사 — read() 가 JSON bytes 반환."""
    buf = io.BytesIO(json.dumps(payload).encode("utf-8"))
    return buf


def test_ollama_boss_implements_protocol() -> None:
    boss = OllamaBoss(model="qwen3-30b-a3b-instruct-2507-bartowski:latest")
    assert isinstance(boss, BossLLM)
    assert boss.name == "qwen3-30b-a3b-instruct-2507-bartowski:latest"


# ── T-RED-1 (70 entry, (나)): 송신 전 RedactionFilter 적용 — untrusted worker
#    output 의 secret 이 Ollama POST body 에 평문 노출 0 (GP-2 prevention 송신 한정).
def test_ollama_boss_redacts_secret_in_request_before_post() -> None:
    from src.adapters.llm.redaction_patterns import REDACTION_MARK

    boss = OllamaBoss(model="m1")
    captured: dict[str, Any] = {}
    secret = "sk-ant-LEAKSECRET1234567890"

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response({"message": {"content": "검토 요약"}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        boss.advise(AdviceRequest(prompt="작업 X", worker_alias="w",
                                  output=f"my api key {secret} leaked", deterministic_flags=[]))

    blob = json.dumps(captured["data"]["messages"], ensure_ascii=False)
    assert secret not in blob           # 원본 secret 부재
    assert REDACTION_MARK in blob        # REDACTION_MARK 존재 (양방향)
    assert "작업 X" in blob              # benign 내용 보존 (무손상)


def test_ollama_boss_advise_returns_text_only_advice() -> None:
    boss = OllamaBoss(model="m1")
    payload = {"message": {"role": "assistant", "content": "검토 요약 — 위험 없음."}, "done": True}
    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
        out = boss.advise(AdviceRequest(prompt="p", worker_alias="claude",
                                        output="hello", deterministic_flags=[]))
    assert isinstance(out, BossAdvice)
    assert out.summary == "검토 요약 — 위험 없음."
    assert out.extra_flags == []        # R2 텍스트 전용 답습 — 자동 flag 추출 0건
    assert out.advisory_failed is False


def test_ollama_boss_advise_posts_chat_endpoint_with_model() -> None:
    """endpoint·모델·prompt 가 정확히 HTTP body 에 실리는가."""
    boss = OllamaBoss(model="m1")
    captured: dict[str, Any] = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["url"] = req.full_url
        captured["data"] = json.loads(req.data.decode("utf-8"))
        captured["timeout"] = timeout
        return _fake_response({"message": {"content": "ok"}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        boss.advise(AdviceRequest(prompt="작업 X", worker_alias="claude",
                                  output="결과 Y", deterministic_flags=["risk"]))

    assert captured["url"] == "http://localhost:11434/api/chat"
    assert captured["data"]["model"] == "m1"
    assert captured["data"]["stream"] is False
    msgs = captured["data"]["messages"]
    assert msgs[0]["role"] == "system"
    # system prompt 가 검토 책무 + 재출력 금지 + 체크리스트 어휘를 명시
    sp = msgs[0]["content"]
    assert "재출력" in sp or "옮겨 쓰" in sp     # mirror 차단 어휘
    assert "advisory" in sp.lower() or "검토" in sp
    # 사용자 prompt / worker 출력 / deterministic flags 가 user 메시지에 포함
    user_blob = msgs[-1]["content"]
    assert "작업 X" in user_blob
    assert "결과 Y" in user_blob
    assert "risk" in user_blob
    assert captured["timeout"] is not None and captured["timeout"] > 0


def test_ollama_boss_advise_raises_on_http_failure() -> None:
    """HTTP 예외 → RuntimeError (R3 호출측 처리 답습)."""
    import urllib.error
    boss = OllamaBoss(model="m1")
    err = urllib.error.URLError("connection refused")
    with patch("urllib.request.urlopen", side_effect=err):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_advise_raises_on_malformed_json() -> None:
    """응답이 JSON 아니면 RuntimeError — 부재≠안전 답습(silent empty advice 금지)."""
    boss = OllamaBoss(model="m1")
    bad = io.BytesIO(b"not-json")
    with patch("urllib.request.urlopen", return_value=bad):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_advise_raises_on_missing_content() -> None:
    """응답 schema 누락 → RuntimeError (silent empty 차단)."""
    boss = OllamaBoss(model="m1")
    payload = {"done": True}  # message.content 없음
    with patch("urllib.request.urlopen", return_value=_fake_response(payload)):
        with pytest.raises(RuntimeError):
            boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                      output="o", deterministic_flags=[]))


def test_ollama_boss_endpoint_is_localhost_only() -> None:
    """endpoint = localhost:11434 하드코딩 (SSRF 회피 답습)."""
    boss = OllamaBoss(model="m1")
    # endpoint 인자로 외부 host 주입 불가 — 생성자 시그니처에 url 인자 없음
    import inspect
    sig = inspect.signature(OllamaBoss.__init__)
    assert "url" not in sig.parameters
    assert "host" not in sig.parameters
    assert "endpoint" not in sig.parameters


# --- prompt 정밀화 (h) 답습: mirror 차단 + 4 항목 체크리스트 ---

def test_system_prompt_forbids_mirroring_worker_output() -> None:
    """신규 _SYSTEM_PROMPT 가 코드/명령 재출력 명시 금지 어휘 포함."""
    from src.jarvis.boss import _SYSTEM_PROMPT
    # mirror 차단 = "재출력" / "옮겨 쓰지 마십시오" / "그대로" 중 1+ 어휘
    assert "재출력" in _SYSTEM_PROMPT
    assert "옮겨 쓰" in _SYSTEM_PROMPT or "그대로" in _SYSTEM_PROMPT


def test_system_prompt_includes_four_evaluation_axes() -> None:
    """4 항목 체크리스트 어휘 (의도 부합 / 정확성 / 위험 / 품질) 모두 포함."""
    from src.jarvis.boss import _SYSTEM_PROMPT
    assert "의도" in _SYSTEM_PROMPT
    assert "정확성" in _SYSTEM_PROMPT
    assert "위험" in _SYSTEM_PROMPT
    assert "품질" in _SYSTEM_PROMPT


def test_system_prompt_long_enough_for_guidance() -> None:
    """sufficient guidance 길이 — few-shot + 체크리스트 (도메인별 어휘 차이 허용)."""
    from src.jarvis.boss import _SYSTEM_PROMPT
    assert len(_SYSTEM_PROMPT) >= 380


def test_system_prompt_preserves_authority_invariants() -> None:
    """기존 R2 답습 어휘 — 사람 게이트 단독 권위 + 결정적 flag 대체 금지 보존."""
    from src.jarvis.boss import _SYSTEM_PROMPT
    assert "사람 게이트" in _SYSTEM_PROMPT
    assert "대체" in _SYSTEM_PROMPT     # 결정적 flag 대체 금지 답습


# --- (m) 워커별 prompt 분기: boss_prompt_for + 4 도메인 + override ---

def test_boss_prompt_for_code_equals_default_system_prompt() -> None:
    """boss_prompt_for('code') = 기존 _SYSTEM_PROMPT (회귀 0, (h) 정밀화 보존)."""
    from src.jarvis.boss import _SYSTEM_PROMPT, boss_prompt_for
    assert boss_prompt_for("code") == _SYSTEM_PROMPT


def test_boss_prompt_for_shell_includes_command_vocabulary() -> None:
    from src.jarvis.boss import boss_prompt_for
    p = boss_prompt_for("shell")
    assert "명령" in p
    assert "로그" in p or "결과" in p


def test_boss_prompt_for_file_includes_file_vocabulary() -> None:
    from src.jarvis.boss import boss_prompt_for
    p = boss_prompt_for("file")
    assert "파일" in p
    assert "내용" in p


def test_boss_prompt_for_general_includes_request_vocabulary() -> None:
    from src.jarvis.boss import boss_prompt_for
    p = boss_prompt_for("general")
    assert "요구" in p or "요청" in p
    assert "사실" in p or "명료" in p


def test_boss_prompt_for_unknown_kind_falls_back_to_general() -> None:
    from src.jarvis.boss import boss_prompt_for
    assert boss_prompt_for("nonexistent_kind") == boss_prompt_for("general")


def test_all_domains_preserve_mirror_block_and_authority() -> None:
    """4 도메인 모두 (h) 정밀화 답습 — mirror 차단 + R2 권위."""
    from src.jarvis.boss import boss_prompt_for
    for kind in ("code", "shell", "file", "general"):
        p = boss_prompt_for(kind)
        assert "재출력" in p, f"{kind}: mirror 차단 어휘 누락"
        assert "사람 게이트" in p, f"{kind}: R2 권위 어휘 누락"
        assert "대체" in p, f"{kind}: 결정적 flag 대체 금지 어휘 누락"
        assert len(p) >= 380, f"{kind}: sufficient guidance 길이 미달 ({len(p)})"


def test_ollama_boss_defaults_to_code_domain_prompt() -> None:
    """OllamaBoss(system_prompt=None) → boss_prompt_for('code') 사용."""
    from src.jarvis.boss import OllamaBoss, boss_prompt_for
    boss = OllamaBoss(model="m")
    captured: dict = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response({"message": {"content": "ok"}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                  output="o", deterministic_flags=[]))
    assert captured["data"]["messages"][0]["content"] == boss_prompt_for("code")


def test_all_domains_quality_axis_few_shot_starts_with_check_emoji() -> None:
    """(o) 답습 — 4 도메인 모두 few-shot 의 품질 line 이 ✅ 시작.

    (n) Layer 1 evidence 에서 발견된 unknown=3/3 mode collapse 차단.
    Qwen3 가 응답에서 품질도 ✅ 로 시작하도록 mode 유도.
    """
    from src.jarvis.boss import boss_prompt_for
    for kind in ("code", "shell", "file", "general"):
        p = boss_prompt_for(kind)
        # few-shot 영역 (예시: 이후) 의 "- 품질: ✅" 패턴 검증
        # 단일 매칭 — 4 도메인 모두 1 회 등장
        assert "품질: ✅" in p, f"{kind}: 품질 axis few-shot 이 ✅ 시작 아님"


def test_ollama_boss_system_prompt_override_applied() -> None:
    """caller 가 명시한 system_prompt 가 HTTP body 에 그대로 전달."""
    from src.jarvis.boss import OllamaBoss
    custom = "CUSTOM-DOMAIN-PROMPT-XYZ"
    boss = OllamaBoss(model="m", system_prompt=custom)
    captured: dict = {}

    def fake_urlopen(req, timeout=None):  # type: ignore[no-untyped-def]
        captured["data"] = json.loads(req.data.decode("utf-8"))
        return _fake_response({"message": {"content": "ok"}, "done": True})

    with patch("urllib.request.urlopen", side_effect=fake_urlopen):
        boss.advise(AdviceRequest(prompt="p", worker_alias="w",
                                  output="o", deterministic_flags=[]))
    assert captured["data"]["messages"][0]["content"] == custom
