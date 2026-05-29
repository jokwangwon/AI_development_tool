"""LedgerLog — 디딤돌0 영속 레저 (append-only event-sourcing JSONL).

답습: docs/phase0/jarvis-collaborative-orchestration-design-brief.md (v2) §5
  - B6: `MemoryLog`(memory.py) 직접 재사용 불가 — 카드 상태(running→awaiting→
    applied)는 *가변*이라 read-only 관찰 누적기로는 표현 못 함. **별도 LedgerLog**
    (append-only event-sourcing, 같은 fail-soft JSONL *패턴* 답습, 모듈은 별개).
    상태 = 이벤트 fold 결과.
  - 재시작 고아: "마지막 상태=running/awaiting 인 task = interrupted" fold.
    자동 복구 없음(정직·단순).
  - B5 scrub 모순 해소: 본 모듈은 *덤 persister* 다 — scrub / exfil 검사 / raw
    미영속 판단은 모두 호출측(JarvisTaskBoard) 책무. 레저는 주어진 필드를 그대로
    적재(영속 *수단*만). 이로써 "어디서 scrub 하는가"의 권위가 board 로 단일화.
  - fold() = 공유 맥락 read API (디딤돌0). 협업(디딤돌1)은 후속 cycle.

append-only 불변식: record / read / fold 만 노출. modify / delete / clear 등
*변경 API 부재* — 상태 변화는 *새 이벤트* 로만 표현(event-sourcing). [[memory]] 의
read-only 패턴과 형제(둘 다 외부 SDK import 0, stdlib 만).
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator

# fold 시 "완결" 로 간주하는 상태 — 이 외(running/awaiting 등)는 재시작 고아.
_TERMINAL = frozenset({"applied", "denied", "failed", "cancelled", "interrupted"})

# 재시작 고아 마킹 상태(자동 복구 없음 — 정직·단순, brief §5).
_INTERRUPTED = "interrupted"

# event/메타 외 fold 카드에 병합하지 않는 예약 키.
_RESERVED = frozenset({"task_id", "event", "ts"})

# UI 제거 — fold 결과에서 task 완전 제외(레저 원본엔 append-only 로 기록 보존).
_DISMISSED = "dismissed"


def _now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


class LedgerLog:
    """append-only event-sourcing JSONL 레저 — 카드 상태 영속 + fold 재구성.

    `record(task_id, event, **fields)` = 1 이벤트 적재 (fail-soft, 예외 흡수).
    `read()` = 적재 순서 보존 iter (파일 미존재 시 빈 iter).
    `fold()` = task_id → 재구성 카드 dict. 마지막 상태가 비완결(running/awaiting)이면
               interrupted 로 마킹(재시작 고아). 첫 등장 순서 보존.
    modify / delete / clear 등 *변경 API 부재* = append-only 답습.
    """

    def __init__(self, path: str | Path) -> None:
        self._path = Path(path)

    @property
    def path(self) -> Path:
        return self._path

    def record(self, task_id: str, event: str, **fields: Any) -> None:
        """1 이벤트 적재. 디스크/직렬화 실패 = silent (fail-soft 답습).

        레저 부재(쓰기 실패)가 board dispatch 를 차단하면 디딤돌0 의 "위험 최소"
        성질이 깨진다. 호출측(JarvisTaskBoard) 도 본 호출을 try/except 로 감싸
        두 겹 fail-soft 가 책무 분리(brief §5).

        fields 는 *이미 scrub / exfil 검사 통과한* 카드 메타만 — raw 워커 출력은
        호출측이 영속시키지 않는다(CB-1 보존). 본 모듈은 검증하지 않는다(덤 persister).
        """
        try:
            entry: dict[str, Any] = {"ts": _now_iso(), "task_id": task_id, "event": event}
            entry.update(fields)
            self._path.parent.mkdir(parents=True, exist_ok=True)
            line = json.dumps(entry, ensure_ascii=False)
            with open(self._path, "a", encoding="utf-8") as fh:
                fh.write(line + "\n")
        except Exception:
            # silent — 레저 부재가 dispatch 차단 사유 0건 (fail-soft).
            return

    def read(self) -> Iterator[dict[str, Any]]:
        """JSONL 을 적재 순서 보존 iter 로 반환. 파일 미존재 = 빈 iter."""
        if not self._path.exists():
            return iter(())
        return self._iter_lines()

    def _iter_lines(self) -> Iterator[dict[str, Any]]:
        with open(self._path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    yield json.loads(line)
                except (json.JSONDecodeError, TypeError):
                    # 손상 라인 = skip (정상 라인만 권위).
                    continue

    def fold(self) -> dict[str, dict[str, Any]]:
        """이벤트 → task_id 별 재구성 카드. 공유 맥락 read API (디딤돌0).

        각 이벤트의 (event/ts/task_id 제외) 필드를 카드에 순서대로 병합 →
        마지막 값 승리. `dismissed` 이벤트가 있으면 그 task 는 결과에서 완전 제외
        (UI 제거 — 레저 원본엔 기록 보존). 모든 이벤트 fold 후 status 가 비완결이면
        interrupted 로 마킹(재시작 고아, 자동 복구 없음). 첫 등장 순서 보존.
        """
        cards: dict[str, dict[str, Any]] = {}
        dismissed: set[str] = set()
        for ev in self.read():
            task_id = ev.get("task_id")
            if not isinstance(task_id, str):
                continue
            if ev.get("event") == _DISMISSED:
                dismissed.add(task_id)
                continue
            card = cards.get(task_id)
            if card is None:
                card = {"id": task_id}
                cards[task_id] = card
            for key, value in ev.items():
                if key in _RESERVED:
                    continue
                card[key] = value
        # UI 제거된 task 제외.
        for task_id in dismissed:
            cards.pop(task_id, None)
        # 재시작 고아 마킹 — 비완결 상태 = interrupted.
        for card in cards.values():
            if card.get("status") not in _TERMINAL:
                card["status"] = _INTERRUPTED
        return cards
