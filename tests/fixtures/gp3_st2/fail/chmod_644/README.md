# fail/chmod_644 — runtime chmod 644 시뮬레이션 시나리오

> **Backlog #1 ST-2 Cycle 2 fixture #3** — init grace 종료 후 runtime 시점에 mock secret 파일 권한이 644 로 변경되었을 때 sidecar 가 `IN_ATTRIB` 감지 후 fail-closed 처리 시연.

## 시나리오

1. sidecar startup → init grace 10초 → 정상 watch 시작
2. **runtime 시점** 에 `simulate.sh` 실행 (Cycle 4 CI step 호출)
3. `simulate.sh` 가 `/run/secrets/mock_api_key` 의 권한을 644 로 변경 (`chmod 644`)
4. sidecar inotifywait 가 `IN_ATTRIB` event 발화
5. status file 에 `UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <timestamp>` 기록
6. hermes-mock healthcheck (interval 5초, 사용자 #9 결정 답습) 가 status file read → `unhealthy` 처리

## 기대 결과 (Cycle 6 시점 시연)

| 검증 항목 | 기대 |
|---------|------|
| inotify event | `IN_ATTRIB` 발화 |
| sidecar status file | `UNHEALTHY: IN_ATTRIB /run/secrets/mock_api_key <ISO8601>` |
| hermes-mock healthcheck (5초 interval) | `unhealthy` 처리 (retries 2 초과 후 정지) |
| `inotify_event_response_time` | < 5초 (interval 답습) |

## fail-closed 메커니즘 답습 (F-B 우선, 사용자 #1 결정)

- sidecar = status file write 한정 (`docker socket` 0건 — F-A 비채택 답습)
- hermes-mock 정지 = docker-compose level healthcheck 통한 시뮬레이션 (Hermes upstream Dockerfile 변경 0건)

## fixture 구성

```
run-secrets/
├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습) — 초기 권한 0600 (정상 docker secret 기본값 시뮬레이션)
├── mock_provider_key
└── mock_db_password
simulate.sh              # runtime chmod 644 시뮬레이션 (Cycle 4 CI step 호출)
```

## 안전 원칙

- `simulate.sh` 가 host system 영향 0건 (PoC container 內부 한정)
- 실제 권한 변경은 docker-compose 격리 환경의 sidecar mount 경로에서만 발생 (production 영역 영향 0건)
- 실 secret 본문 0건 (fake canary 의무 답습)

## Cycle 영역

- Cycle 2 = 본 fixture 작성 한정 (`simulate.sh` 본문 포함)
- Cycle 4 = `simulate.sh` 호출 step 추가
- Cycle 6 = actual run 시연
