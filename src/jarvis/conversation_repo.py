"""ConversationRepo — 통합 데이터 레이어 §10-3 (0.5단계).

답습: docs/phase0/jarvis-unified-data-layer-design-brief.md
  - §10-3: server.py 인라인 conversation 핸들러 6곳 → sync ConversationRepo
    추출(동작 불변 refactor). 다중대화 SQLite swap 시 호출부 1곳만 교체되도록.
  - §5: repo별 얇은 port — JSONL 직접(Backing 추상화 없이, Rule of Three).
  - Q7 해소: 대화 raw 저장(저장 redaction 없음). 영속 위치 권한은 paths(§10-2).

본 repo 는 server.py 의 기존 동작을 *그대로* 옮긴 것(동작 불변):
  - append = fail-soft JSONL append (부모 디렉터리 부재 시 조용히 실패).
  - read_all = parse, 깨진 줄 skip, 파일 부재 시 [].
  - delete_entry = id 매칭 제거 후 tmp+replace rewrite, 깨진 줄은 raw 보존.
  - export 의 "파일 부재" 특수 분기를 위해 exists() 분리.

stdlib only. backing 교체(SQLite, §10-4)는 이 클래스 내부만 바뀐다.
"""
from __future__ import annotations

import json
import os
from pathlib import Path


class ConversationRepo:
    def __init__(self, path: str | Path) -> None:
        self._path = str(path)

    @property
    def path(self) -> str:
        return self._path

    def exists(self) -> bool:
        return os.path.exists(self._path)

    def append(self, entry: dict) -> None:
        """JSONL append (fail-soft) — 기존 _save_conversation_entry 동작."""
        try:
            with open(self._path, "a", encoding="utf-8") as fh:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
        except Exception:
            pass

    def read_all(self) -> list[dict]:
        """전체 entry 파싱. 깨진 줄 skip, 파일 부재 시 []."""
        if not os.path.exists(self._path):
            return []
        out: list[dict] = []
        with open(self._path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    out.append(json.loads(line))
                except Exception:
                    continue
        return out

    def delete_entry(self, entry_id: str) -> int:
        """id 매칭 entry 제거 후 rewrite. 깨진 줄은 raw 보존. removed count 반환."""
        if not os.path.exists(self._path):
            return 0
        kept: list[str] = []
        removed = 0
        with open(self._path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    e = json.loads(line)
                except Exception:
                    kept.append(line)
                    continue
                if e.get("id") == entry_id:
                    removed += 1
                else:
                    kept.append(json.dumps(e, ensure_ascii=False))
        tmp_path = self._path + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as fh:
            for line in kept:
                fh.write(line + "\n")
        os.replace(tmp_path, self._path)
        return removed

    def archive_to(self, archive_path: str) -> bool:
        """파일이 있으면 archive_path 로 이동(rename). 없으면 no-op. 이동 여부 반환."""
        if not os.path.exists(self._path):
            return False
        os.rename(self._path, archive_path)
        return True
