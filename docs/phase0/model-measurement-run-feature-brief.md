# 모델 측정 실행 기능 brief — 모델 관리에서 직접 벤치마크

> **일자**: 2026-06-05 · **브랜치**: `feature/model-mgmt-refresh`
> **상태**: brief 초안 → 사용자 검토 대기 → TDD (단순~중간 기능, 보안 무관 → 3+1 합의 불요)

## 0. 문제 (진단 완료)

모델 관리(📊) 창이 **5/29에 고정** — "새로 측정해도 갱신 안 됨"의 뿌리는 **측정을 *수행*하는 도구가 repo에 없음**:
- `append_measurement`(DB live writer)·`measurement:write`(플러그인 capability) = 저장 인프라는 존재(§10-5)
- 그러나 이를 호출하는 측정 도구가 0 — 5/29 데이터는 v0.0 작업 때 일회성 생성 legacy
- `migrate_legacy`는 **bootstrap-once**(kind 가드)라 legacy JSON 갱신도 무시
- ⭐ 현재 ollama 모델 = qwen3 30b×2 + qwen3-coder 51.7GB (5/29의 llama3.3/exaone4는 이제 없음 → 랭킹이 실제와 불일치)

→ **빠진 조각 = 측정 수행 + trigger.** 저장은 기존 `append_measurement(kind="multi")` 재사용.

## 1. 설계

### 1.1 측정 수행 (신규 `src/jarvis/model_benchmark.py`, leaf)
```
run_benchmark(model_names, *, prompt, n_runs, generate_fn) -> measurement dict(multi 포맷)
```
- 각 모델: **warmup 1회**(콜드 로드 시간 = warmup_s) + **n_runs회** generate(고정 프롬프트)
- 각 run = ollama `/api/generate`(stream=false) 응답 메트릭 수집:
  `total_duration_ns·load_duration_ns·prompt_eval_count·prompt_eval_duration_ns·eval_count·eval_duration_ns`
  → 계산: `decode_tok_per_s = eval_count / (eval_duration_ns/1e9)` · `prefill_tok_per_s` · `latency_s = total_duration_ns/1e9`
- across runs **stats**(mean/p50/std/min/max) 계산 → `append_session` 입력 포맷과 정확히 일치(`_RUN_FIELDS`·`_STATS_KEYS`)
- 모델 로드 실패/타임아웃 = `skipped`/`error run`(기존 2변종 처리 재사용, fail-soft)
- **`generate_fn` 주입** = hermetic 테스트 seam(실 ollama 없이 메트릭 계산 검증)

### 1.2 라우트 (비동기 — 측정 ~5–10분)
- `POST /api/measurements/run` {models?, n_runs?} → **백그라운드 task 시작**, 즉시 202 + run_id
- `GET /api/measurements/run/status` → {state: idle|running|done|error, progress: "2/3 모델", current_model}
- 완료 시 `append_measurement(kind="multi")` → DB 새 세션. 동시 실행 1개 제한(중복 측정 방지).
- same-origin 가드(기존 답습).

### 1.3 HUD (모델 관리 모달)
- **▶ 측정 실행** 버튼(헤더, 🔄 옆) → POST → 진행 표시(폴링, "측정 중 2/3 qwen3-coder…") → 완료 시 자동 `openMeasurements()` 갱신
- 측정 중 버튼 비활성 + 진행률. 실패 시 사유 표시.
- **🔄 새로고침 버튼**(이미 구현) 함께 포함.

## 2. 결정 필요 (사용자) — §3 후보

| # | 결정 | 후보 |
|---|---|---|
| D-1 | 측정 대상 | (a) ollama 전체 자동 (b) 모달에서 체크박스 선택 (c) 전체 기본 + 선택 옵션 |
| D-2 | n_runs | 3(5/29와 동일·추천) / 5(정밀) / 2(빠름) |
| D-3 | 프롬프트 | 고정 짧은 프롬프트(decode 속도가 지표라 내용 무관). 길이만 고정(예: ~370 tok = 5/29 근사) |
| D-4 | 51.7GB 모델 | 포함(느림 감수) / 기본 제외(옵션) |

## 3. 검증 (TDD)

- `run_benchmark` 단위: generate_fn mock → 메트릭 계산(decode/prefill/latency) + stats(mean/p50/std) 정확 + skipped/error 변종
- `append_measurement` 통합: 측정 dict → DB → `latest_session` 재구성 일치(라운드트립)
- 라우트: POST→running→done 상태 전이, 동시 실행 1개, same-origin
- 실 e2e: 작은 모델 1개(qwen3 30b) 실측 → DB 새 세션 → HUD 랭킹 갱신
- grimp 단방향(model_benchmark leaf) + secret PASS + JS 문법

## 4. 정직 단서

- 측정 시간 = 모델 수·크기 의존(51.7GB 콜드 로드 큼). 진행 표시로 완화하나 수 분 소요.
- 새 측정 프롬프트가 5/29와 다르면 prefill 비교성 제한(decode tok/s는 생성 속도라 무관 — 랭킹 지표).
- **코드 변경 0 (본 brief = 설계).** 사용자 D-1~D-4 결정 후 TDD.
