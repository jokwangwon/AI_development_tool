# Jarvis 품질 axis prompt 정밀화 brief — few-shot 예시 갱신

> **scope**: (n) Layer 1 axis 자료화에서 발견된 신호 — Qwen3 가 품질 axis 에 emoji 미사용 (`unknown=3/3`). few-shot 예시의 4 도메인 모두 품질 line 을 `✅` 시작으로 갱신해 mode collapse 차단.
> **DONE 기준**: Layer 0 demo 재실행 → 품질 axis = `ok` (or `warn`/`fail`), `unknown=0`.
> **답습**: 후속 (o) [[v00-sprint-pending]] + [[ceremony-inflation]] 1-agent + (h)+(m) 답습 보존 (mirror 차단 + 4 axis + R2 권위 invariant).

---

## 1. (n) 발견 진단

`_DOMAIN_TEMPLATES` (`src/jarvis/boss.py`) 의 few-shot 예시 4 도메인 모두:

| Axis | code | shell | file | general |
|------|------|-------|------|---------|
| 의도 부합 | ✅ ... | ✅ ... | ✅ ... | ✅ ... |
| Axis 2 | ✅ ... | ✅ ... | ✅ ... | ✅ ... |
| 위험 신호 | 없음 | 없음 (sudo·rm 흔적 0) | 없음 | 없음 |
| **품질** | **단순/명료, 검사 순서 명확** | **명령 chain 명료, 실행 ~2초** | **UTF-8 평문, 줄바꿈 일관** | **단락 구조 명료** |

품질 axis 예시 4 종 모두 emoji 없이 시작 → Qwen3 가 모방 → 응답 시 품질 line 도 emoji 없이 작성 → parse_advice_axes 가 `unknown` 분류.

실 evidence (n cycle 측정, 3 entry):
```
품질    ok=0 warn=0 fail=0 none=0 unknown=3
```

위험 신호 axis 의 "없음" → `none` 매핑은 정상 (parser 의도). 품질은 평가 결과 항목 → emoji 사용 의도 → 예시 정정 필요.

## 2. 갱신 — 품질 axis 예시 4 도메인

각 도메인 품질 line 을 `✅ <서술>` 형식으로 갱신:

| Domain | Before | After |
|--------|--------|-------|
| code | "단순/명료, 검사 순서 명확" | **"✅ 단순/명료, 검사 순서 명확"** |
| shell | "명령 chain 명료, 실행 ~2초" | **"✅ 명령 chain 명료, 실행 ~2초"** |
| file | "UTF-8 평문, 줄바꿈 일관" | **"✅ UTF-8 평문, 줄바꿈 일관"** |
| general | "단락 구조 명료" | **"✅ 단락 구조 명료"** |

다른 axis 답습 보존. 위험 신호 axis 의 "없음" 도 그대로 (parse 의 `none` 매핑은 정상 = 위험 없음 = 정상 상태).

## 3. TDD

| # | test |
|---|------|
| 1 | 4 도메인 모두 품질 axis few-shot 이 ✅ 시작 (직접 substring 검증) |
| 2 | (h)+(m) 답습 — 4 도메인 mirror 차단 + R2 권위 invariant 보존 (기존 test 회귀 0) |
| 3 | parser test — parse_advice_axes 가 갱신된 prompt 가 만든 응답 패턴을 ok 로 분류 (모의 응답으로 검증) |

회귀: 143/143 test 보존 + 4 신규 (또는 갱신).

## 4. 의미 evidence

Layer 0 demo 재실행 (3 task multi-dispatch) → Layer 1 mine → axis_stats 확인:
- 합격 조건: 품질 axis `unknown` < 3 (이상적 = ok=3 또는 ok≥1)
- 다른 axis 회귀 0 (의도 부합/정확성/위험 신호 = 이전 동일)

## 5. 위험 + 완화

| 위험 | 완화 |
|------|------|
| 갱신 후에도 LLM 이 품질에 emoji 미사용 (mode collapse 잔존) | Layer 0 demo 재실행 실측으로 검증. 실패 시 prompt 추가 명시 ("각 line ✅/⚠️/❌ 로 시작") |
| (m) 분기 8 도메인 test 회귀 | 기존 `test_all_domains_preserve_mirror_block_and_authority` 답습 — 4 도메인 본질 보존 자동 회귀 가드 |
| 다른 axis 영향 | 갱신은 *품질 line 한 줄* 만 → 다른 axis 동작 0 변화 |

## 6. 비-scope (DEFER 영구)

- LLM 응답 schema 강제 (JSON 출력) — Layer 2+ 영역
- 응답 검증 post-processing (parse 실패 시 LLM 재호출) — 별도 cycle
- axis 라벨 normalization — 별도 cycle
- 다국어 prompt — 한국어 한정

DONE 후 단일 commit + push + memory.
