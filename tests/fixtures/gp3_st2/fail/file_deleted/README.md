# fail/file_deleted — runtime secret 파일 삭제 시나리오

> **Backlog #1 ST-2 Cycle 2 fixture #5** — init grace 종료 후 runtime 시점에 mock secret 파일이 *삭제* 되었을 때 sidecar 가 `IN_DELETE_SELF` (또는 `IN_MOVE_SELF`) 감지 후 fail-closed 처리 시연.

## 시나리오

1. sidecar startup → init grace 10초 → 정상 watch 시작
2. **runtime 시점** 에 `simulate.sh` 실행
3. `simulate.sh` 가 `/run/secrets/mock_api_key` 를 `rm` 으로 삭제
4. sidecar inotifywait 가 `IN_DELETE_SELF` event 발화 (또는 환경에 따라 `IN_MOVE_SELF`)
5. status file 에 `UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <timestamp>` 기록
6. hermes-mock healthcheck (interval 5초) 가 `unhealthy` 처리

## 기대 결과 (Cycle 6 시점 시연)

| 검증 항목 | 기대 |
|---------|------|
| inotify event | `IN_DELETE_SELF` 또는 `IN_MOVE_SELF` 발화 |
| sidecar status file | `UNHEALTHY: IN_DELETE_SELF /run/secrets/mock_api_key <ISO8601>` |
| hermes-mock healthcheck | `unhealthy` 처리 |
| `inotify_event_response_time` | < 5초 |

## inotify event 변동성

`IN_DELETE_SELF` vs `IN_MOVE_SELF` event 는 file system + 삭제 방식에 따라 다를 수 있음:

| 삭제 방식 | inotify event |
|---------|-------------|
| `rm <file>` (unlink syscall) | `IN_DELETE_SELF` |
| `mv <file> /tmp/` (rename syscall) | `IN_MOVE_SELF` |
| `truncate -s 0 <file>` | `IN_MODIFY` (본 fixture 영역 외 — `content_modified` 답습) |

본 fixture = `rm` 사용 → `IN_DELETE_SELF` 우선. Cycle 3 sidecar 본문 (`watch-secrets.sh`) 는 양쪽 event 모두 처리.

## fixture 구성

```
run-secrets/
├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_*
├── mock_provider_key
└── mock_db_password
simulate.sh              # runtime 파일 삭제 시뮬레이션
```

## 안전 원칙

- `simulate.sh` 가 sidecar PoC container 내부 한정 — production 영역 영향 0건
- 삭제 후 *복원* 0건 (docker-compose down 으로 cleanup)
- 실 secret 0건 (fake canary 의무 답습)

## Cycle 영역

- Cycle 2 = 본 fixture 작성 한정
- Cycle 4 = `simulate.sh` 호출 step
- Cycle 6 = actual run 시연
