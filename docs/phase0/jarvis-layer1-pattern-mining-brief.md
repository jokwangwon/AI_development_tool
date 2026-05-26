# Jarvis 자가진화 Layer 1 brief — 패턴 마이닝 (read-only Layer 0)

> **scope**: Layer 0 누적(JSONL)을 입력으로 받아 운영 패턴을 추출 → 사람 가독 보고서 산출.
> **safety class**: Layer 0 = read-only, 자비스 동작 변경 0, 결과 = 텍스트/dict 산출물 한정. 게이트 *불요*.
> **DONE 기준**: 기존 Layer 0 JSONL evidence 를 mine() 으로 처리 → `PatternReport` 1건 + 사람 가독 출력.
> **답습**: [[jarvis-layer0-active]] 의 Layer 단계 분리표 답습 + [[ceremony-inflation]] 1-agent 직접 진행. 풀 3+1 = Layer 2 진입부터(사람 게이트 신설 = 큰 결정).

---

## 1. Layer 1 안전 등급 정당화

| 속성 | 보장 |
|------|------|
| Layer 0 수정 | **0** — mine() 은 `Iterable[dict]` 받음 (MemoryLog 미참조 = decouple) |
| 자비스 동작 변경 경로 | **0** — 모듈 어디에도 prompt/policy/code 갱신 API 없음 |
| 외부 호출 | **0** — stdlib(`dataclasses`, `collections`) 만, 파일 IO 0 |
| 출력 형태 | `PatternReport` (frozen dataclass) + `format_report()` 텍스트만 |
| 사용 권한 | 보고서 = *읽고 참고만*. 자동 적용 0 (자동 적용 = Layer 2+ 게이트 책무) |

→ "보고서 출력은 안전 행위" 답습 = 게이트 불요 정당화.

---

## 2. 추출 패턴 (v0.0 한정)

| 패턴 | 의미 |
|------|------|
| `total_entries` | 누적 dispatch 총 수 |
| `first_ts` / `last_ts` | 관찰 시간 범위 |
| `status_counts` | applied / denied / worker_failed 분포 |
| `workers[]` | 워커별 `WorkerStats(alias, total, applied, denied, worker_failed, success_rate)` |
| `flag_frequency` | verdict_flags 빈도 히스토그램 (위험 패턴 trending) |
| `advice_total` / `advice_failed` | Boss advisory 발화 수 + 실패 수 (endpoint 건강 신호) |
| `recent_failures[]` | 최근 N 개 실패 entry (worker_failed / denied / advice_failed any) |

비-scope (DEFER 영구): 시계열 추세, anomaly detection, 패턴 *제안* (Layer 2), 자동 정책 적용 (Layer 3).

---

## 3. API 설계

```python
@dataclass(frozen=True)
class WorkerStats:
    alias: str
    total: int
    applied: int
    denied: int
    worker_failed: int

    @property
    def success_rate(self) -> float: ...   # applied / total

@dataclass(frozen=True)
class PatternReport:
    total_entries: int
    first_ts: str | None
    last_ts: str | None
    status_counts: dict[str, int]
    workers: tuple[WorkerStats, ...]
    flag_frequency: dict[str, int]
    advice_total: int
    advice_failed: int
    recent_failures: tuple[dict, ...]

def mine(entries: Iterable[dict], recent_failure_limit: int = 5) -> PatternReport: ...
def format_report(report: PatternReport) -> str: ...
```

- **frozen + tuple**: 결과 *불변* — 호출자가 수정 시도 시 예외 (read-only 답습).
- **mine 인자 = `Iterable[dict]`**: MemoryLog 미참조 = 결합 0. 호출측이 `log.read()` 를 넘김. 테스트는 list/dict literal 직접.
- **malformed entries**: 필수 키 누락 = skip (silent). Layer 0 자체가 JSON parse 실패 line 을 skip 하므로 추가 안전망.

---

## 4. fail-soft + 거짓 안전감 차단

- 빈 입력 → `PatternReport(total_entries=0, ...)` 반환. 예외 없음.
- 손상된 entry (필수 필드 누락) → skip + 다음 entry 계속.
- format_report = 모든 필드 0 일 때도 정상 텍스트 (사용자에게 "데이터 부족" 명시).
- **거짓 안전감 차단**: 패턴 부재(예: failure 0건) ≠ "안전" 라벨. 단순 카운트만 보고 — 의미 부여는 사람.

---

## 5. 합격 조건

- `tests/jarvis/test_layer1.py` 12+ test green (empty / status / per-worker / flag freq / advice / recent failures / frozen / malformed)
- `examples/jarvis_v00_layer1_mine.py` 실 evidence 1회 = 기존 `/tmp/jarvis-v00-layer0-memory.jsonl` (3 entry) 처리 → 사람 가독 보고서 + JSON dump
- 회귀 0 (89 test green 보존)
- import-linter KEPT
- `layer1.py` 의 import 가 MemoryLog 미참조 (decouple) — 구조 검증 test 포함

---

## 6. 비-scope (DEFER 영구)

- Layer 2 (자동 prompt/policy 제안) — 사람 게이트 *필수*, 별도 합의
- Layer 3 (self-modification) — git+테스트+사람 강제, 본격 안전 인프라
- 시계열 anomaly / ML 기반 패턴 / 외부 observability forward — 별도 합의
- 패턴 보고서 *적용* 자동화 — Layer 2+ 영역
