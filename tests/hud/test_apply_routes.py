"""반영 게이트 HTTP 라우트 테스트 — slice-app-1 (CB-2/CB-5/CB-6).

답습: docs/review/3plus1-consensus-2026-06-06-output-application-loop.md
  - CB-5 preview scrub / CB-6 자동반영 금지(same-origin 명시 트리거) / CB-2 화이트리스트.

git 호출은 git_runner 주입(hermetic). source=work_root 하위 폴더(traversal 차단).
"""
from __future__ import annotations

import json
import os

from starlette.applications import Starlette
from starlette.testclient import TestClient

from jarvis_hud.apply_routes import make_apply_routes

_PATCH = (
    "diff --git a/app.py b/app.py\n--- a/app.py\n+++ b/app.py\n@@ -1 +1 @@\n-old\n+new\n"
)
_BAD_PATCH = (
    "diff --git a/.git/config b/.git/config\n--- a/.git/config\n+++ b/.git/config\n"
    "@@ -1 +1 @@\n+x\n"
)


class FakeGit:
    def __init__(self, diff=_PATCH, responses=None):
        self.diff = diff
        self.responses = responses or {}
        self.calls = []

    def __call__(self, argv, cwd, stdin=None):
        self.calls.append((tuple(argv), cwd, stdin))
        key = tuple(argv)
        for k, v in self.responses.items():
            if key[: len(k)] == k:
                return v
        if key[:3] == ("git", "diff", "--cached"):
            return (0, self.diff, "")
        return (0, "", "")

    def ran(self, *sub):
        return any(c[0][: len(sub)] == sub for c in self.calls)


def _setup(tmp_path, *, git=None, secret_in_diff=False):
    work = tmp_path / "work"
    src = work / "out"
    src.mkdir(parents=True)
    (src / "app.py").write_text("new\n", encoding="utf-8")
    repo = tmp_path / "voice_lab"
    repo.mkdir()
    (repo / ".git").mkdir()
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": [{
        "name": "voice_lab", "title": "T", "url": "http://localhost:8777",
        "origin": "jarvis", "apply": {"repo_path": str(repo)},
    }]}), encoding="utf-8")
    git = git or FakeGit()
    app = Starlette(routes=make_apply_routes(
        work_root=str(work), registry_file=str(reg), git_runner=git))
    return TestClient(app), git


_HDR = {"origin": "http://testserver", "host": "testserver"}


# ── CB-2 targets ─────────────────────────────────────────────────────────
def test_targets_list(tmp_path):
    client, _ = _setup(tmp_path)
    r = client.get("/api/jarvis/apply/targets")
    assert r.status_code == 200
    assert r.json()["targets"] == ["voice_lab"]


# ── sources (work_root 하위 산출물 폴더 목록) ────────────────────────────
def test_sources_lists_workdir_folders(tmp_path):
    client, _ = _setup(tmp_path)
    (tmp_path / "work" / "another").mkdir()
    (tmp_path / "work" / ".hidden").mkdir()
    (tmp_path / "work" / "afile.txt").write_text("x", encoding="utf-8")
    r = client.get("/api/jarvis/apply/sources")
    assert r.status_code == 200
    srcs = r.json()["sources"]
    assert "out" in srcs and "another" in srcs
    assert ".hidden" not in srcs  # 숨김 제외
    assert "afile.txt" not in srcs  # 파일 제외


def test_sources_missing_work_root_empty(tmp_path):
    reg = tmp_path / "registry.json"
    reg.write_text(json.dumps({"entries": []}), encoding="utf-8")
    app = Starlette(routes=make_apply_routes(
        work_root=str(tmp_path / "nope"), registry_file=str(reg), git_runner=FakeGit()))
    r = TestClient(app).get("/api/jarvis/apply/sources")
    assert r.json()["sources"] == []


# ── preview (diff + dry-run) ─────────────────────────────────────────────
def test_preview_returns_diff_ok(tmp_path):
    client, _ = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/preview",
                    json={"source": "out", "target": "voice_lab"}, headers=_HDR)
    assert r.status_code == 200
    body = r.json()
    assert body["outcome"] == "executed"  # dry-run 통과
    assert "app.py" in body["diff"]
    assert body["violations"] == []


def test_preview_violation_patch_rejected_no_apply(tmp_path):
    git = FakeGit(diff=_BAD_PATCH)
    client, git = _setup(tmp_path, git=git)
    r = client.post("/api/jarvis/apply/preview",
                    json={"source": "out", "target": "voice_lab"}, headers=_HDR)
    body = r.json()
    assert body["outcome"] == "rejected"
    assert any(v["kind"] == "dotgit" for v in body["violations"])
    assert not git.ran("git", "apply")  # 위반은 git apply 미접촉


def test_preview_scrubs_secrets(tmp_path):
    # 가짜 키는 런타임 조립(소스에 리터럴 prefix 미잔존 → secret_scanner 오탐 회피)
    fake_key = "sk-ant-" + "api03-" + "S" * 30
    leaky = (
        "diff --git a/app.py b/app.py\n--- a/app.py\n+++ b/app.py\n@@ -1 +1 @@\n"
        f"+token = \"{fake_key}\"\n"
    )
    client, _ = _setup(tmp_path, git=FakeGit(diff=leaky))
    r = client.post("/api/jarvis/apply/preview",
                    json={"source": "out", "target": "voice_lab"}, headers=_HDR)
    assert fake_key not in r.json()["diff"]


# ── CB-6 commit (자동반영 금지: same-origin + confirmed) ──────────────────
def test_commit_applies(tmp_path):
    client, git = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/commit",
                    json={"source": "out", "target": "voice_lab", "confirmed": True},
                    headers=_HDR)
    assert r.status_code == 200
    assert r.json()["outcome"] == "executed"
    assert r.json()["applied"] is True
    assert git.ran("git", "apply")
    assert not git.ran("git", "commit")  # CB-7
    assert not git.ran("git", "push")


def test_commit_requires_confirmed(tmp_path):
    client, git = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/commit",
                    json={"source": "out", "target": "voice_lab"}, headers=_HDR)
    assert r.status_code == 400
    assert not git.ran("git", "apply")


def test_commit_cross_origin_forbidden(tmp_path):
    client, git = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/commit",
                    json={"source": "out", "target": "voice_lab", "confirmed": True},
                    headers={"origin": "http://evil.com", "host": "testserver"})
    assert r.status_code == 403
    assert not git.ran("git", "apply")


def test_commit_unregistered_target_rejected(tmp_path):
    client, git = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/commit",
                    json={"source": "out", "target": "ghost", "confirmed": True},
                    headers=_HDR)
    assert r.status_code == 400
    assert not git.ran("git", "apply")


def test_source_traversal_rejected(tmp_path):
    client, git = _setup(tmp_path)
    r = client.post("/api/jarvis/apply/preview",
                    json={"source": "../../etc", "target": "voice_lab"}, headers=_HDR)
    assert r.status_code == 400
