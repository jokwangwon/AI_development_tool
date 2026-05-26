# Jarvis Layer 1 (n) boss 평가 자료화 brief — advice 4 항목 추출

> **scope**: Layer 0 의 `advice_summary` (boss prompt (h)+(m) 발효 후 4 항목 체크리스트) → 항목별 status (✅/⚠️/❌/없음) 자료화 → Layer 1 신규 신호.
> **DONE 기준**: parse_advice_axes 결정적 파서 + PatternReport.axis_stats + format_report 섹션 + 실 Layer 0 JSONL 처리 evidence.
> **답습**: 후속 (n) [[v00-sprint-pending]] + [[jarvis-layer1-active]] read-only 답습 + [[ceremony-inflation]] 1-agent.

---

## 1. 안전 등급 답습 (Layer 1 와 동일)

| 속성 | 보장 |
|------|------|
| Layer 0 수정 | 0 (parser 입력 = str, raw 보존) |
| 자비스 동작 변경 경로 | 0 (Layer 1 책무 답습) |
| 외부 호출 | 0 (stdlib re 단독) |
| 출력 형태 | frozen PatternReport 확장 (axis_stats: dict frozen via tuple-immutability 아님 = 답습) |

axis_stats 는 dict 이지만 PatternReport frozen 으로 재할당 차단 = Layer 1 의 dict 필드 패턴 답습 (status_counts, flag_frequency 와 동형).

---

## 2. 입력 패턴 — boss prompt (h)+(m) 발효 후

`advice_summary` 형식 (4 도메인 모두 동일 골격):
```
- 의도 부합: ✅ ...
- <axis-2>: ✅ ...
- 위험 신호: 없음
- 품질: ✅ ...
```

도메인별 axis-2 라벨:
- code → "정확성"
- shell → "결과·로그 의미"
- file → "내용 일치"
- general → "사실 정확"

axis-1·3·4 는 4 도메인 모두 공통 ("의도 부합", "위험 신호", "품질").

## 3. parser 설계

```python
def parse_advice_axes(summary: str) -> dict[str, str]:
    """advice_summary → {axis_label: status} dict.

    status 매핑:
      "✅" → "ok"
      "⚠️" → "warn"
      "❌" → "fail"
      "없음" (위험 신호 axis 한정) → "none"
      기타 → "unknown"

    파싱 규칙:
      - "- <axis>: <body>" 패턴 (boss prompt few-shot 형식 답습)
      - body 의 *첫* 이모지/단어 = status
      - 손상 line skip (정상 line 만 채택)
      - 빈 입력 → {}
    """
```

axis 라벨 normalization 0건 = 사용자에게 raw 그대로 노출 (도메인별 axis-2 라벨 4 종 그대로). Layer 1 sum 시 axis 라벨 = key.

## 4. PatternReport 확장

```python
@dataclass(frozen=True)
class PatternReport:
    ...  # 기존 필드 보존
    advice_axis_stats: dict[str, dict[str, int]] = {}
    # axis_label → status → count
    # 예: {"의도 부합": {"ok": 5, "warn": 0, "fail": 1, "unknown": 0}, ...}
```

집계 규칙:
- Layer 0 entry 의 `advice_summary` 가 None / 빈 → axis 0건 추가
- parser 가 dict 반환 → axis 별 status count++
- format_report 신규 섹션: "Advice 4 항목 (axis_label: ok/warn/fail …)"

## 5. TDD

| # | test |
|---|------|
| 1 | parse_advice_axes(빈 입력) → {} |
| 2 | parse 정상 4 axis (code 도메인) → {axis: "ok"} 4건 |
| 3 | parse "없음" → "none" 매핑 (위험 신호 axis 한정) |
| 4 | parse ⚠️ → "warn" / ❌ → "fail" / 기타 → "unknown" |
| 5 | parse 손상 line skip + 정상 line 만 채택 |
| 6 | parse multi-domain (code + shell + file + general 모두) |
| 7 | mine() 가 advice 부재 entry skip (axis_stats 미증가) |
| 8 | mine() 의 axis_stats 가 dict[axis][status]=count 정확 |
| 9 | PatternReport.advice_axis_stats default = {} (회귀 0) |
| 10 | format_report 가 axis_stats 비어있어도 정상 렌더 |
| 11 | format_report 에 axis 라벨 + status 카운트 모두 표시 |

## 6. 의미 evidence

`examples/jarvis_v00_layer1_mine.py` 재실행 = 기존 `/tmp/jarvis-v00-layer0-memory.jsonl` 처리 (Layer 0 demo 의 3 entry, code 도메인 advice).

추가로 GLM/codex/claude worker 실행 후 누적된 다양한 axis 데이터 mining 가능. 단 v0.0 evidence 1 회 = Layer 0 demo entry (3 건) + claude worker entry (1 건) 합집합 정도 충분.

합격 (3/3):
- axis_stats 비어있지 않음 (≥ 1 axis)
- 적어도 1 axis 에 "ok" count ≥ 1
- format_report 출력에 axis 섹션 visible

## 7. 비-scope (DEFER 영구)

- axis 라벨 normalization (도메인별 다른 axis-2 라벨 통합) — 별도 cycle
- LLM 응답 JSON schema 강제 — Layer 2+
- axis trend 시계열 (1주/1월 단위) — Layer 2+ 마이닝 확장
- axis 별 자동 알람 (fail 임계치 도달 시) — Layer 2+ (사람 게이트 신설)
- 자유 텍스트 advice (체크리스트 형식 아님) 강제 분류 — DEFER

DONE 후 단일 commit + push + PR comment + memory.
