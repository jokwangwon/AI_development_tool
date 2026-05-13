# pass/init_phase — init grace period 내 정상 secret 주입 시나리오

> **Backlog #1 ST-2 Cycle 2 fixture #2** — init grace period (10초, 사용자 #8 결정 답습) *내부* 에서 발생하는 secret 주입 event 가 무시되어야 함 시연.

## 시나리오

1. sidecar startup
2. init grace period (T2 = 10초) 시작
3. **init grace 내부** 시점에 mock secret 파일이 *주입* 됨 (docker secret init 시뮬레이션)
4. init grace 종료 후 sidecar 가 정상 watch 시작 — **이전 init 단계 event 는 status 에 기록되지 않음**

## 기대 결과 (Cycle 6 시점 시연)

| 검증 항목 | 기대 |
|---------|------|
| sidecar status file | empty (init grace 내부 event 무시) |
| hermes-mock healthcheck | `healthy` (depends_on: sidecar service_healthy 답습) |
| inotify event 발화 횟수 (logged) | 0건 (grace 내부 event = 미기록) |

## Cycle 3 sidecar 본문 의존성 (구현 영역 외)

Cycle 3 sidecar 본문 (`watch-secrets.sh` 또는 동등) 의 init grace 처리:

```sh
# (Cycle 3 영역 — 본 fixture 시점 미작성)
sleep 10              # init grace period (사용자 #8 결정 답습)
inotifywait -m ...    # 본격 watch 시작 — 이전 event 무시
```

## fixture 구성

```
run-secrets/
├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습)
├── mock_provider_key
└── mock_db_password
```

simulate.sh 미보유 — fixture 자체는 normal_operation 과 동일. 차이는 **Cycle 4 CI step 호출 시점** 에서 *init grace 시뮬레이션* (예: docker-compose 직후 secret 주입 시뮬레이션) 으로 발생.

## Cycle 영역

- Cycle 2 = 본 fixture 작성 한정
- Cycle 4 = init grace 시뮬레이션 호출 영역 (CI step + tool 스크립트)
- Cycle 6 = actual run 시연
