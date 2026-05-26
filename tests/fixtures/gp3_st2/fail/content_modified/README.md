# fail/content_modified — runtime secret 본문 변경 시나리오

> **Backlog #1 ST-2 Cycle 2 fixture #4** — init grace 종료 후 runtime 시점에 mock secret 파일의 *본문* 이 변경되었을 때 sidecar 가 `IN_MODIFY` 감지 후 fail-closed 처리 시연.

## 시나리오

1. sidecar startup → init grace 10초 → 정상 watch 시작
2. **runtime 시점** 에 `simulate.sh` 실행
3. `simulate.sh` 가 `/run/secrets/mock_api_key` 의 본문에 변조 문자열 append (예: ` # tampered`)
4. sidecar inotifywait 가 `IN_MODIFY` event 발화
5. status file 에 `UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <timestamp>` 기록
6. hermes-mock healthcheck (interval 5초) 가 `unhealthy` 처리

## 기대 결과 (Cycle 6 시점 시연)

| 검증 항목 | 기대 |
|---------|------|
| inotify event | `IN_MODIFY` 발화 |
| sidecar status file | `UNHEALTHY: IN_MODIFY /run/secrets/mock_api_key <ISO8601>` |
| hermes-mock healthcheck | `unhealthy` 처리 |
| `inotify_event_response_time` | < 5초 |

## 본문 변조 *권한 한계*

- `simulate.sh` 가 *append* 만 수행 (overwrite 0건 — 변조 흔적 보존 + 분석 용이)
- sidecar 가 변조된 본문을 logging / hashing / export 0건 (영구 금지, R-4.1 답습)
- 본문 변조 후 *복원* 0건 (PoC 격리 환경 종료 시 docker-compose down 으로 cleanup)

## fixture 구성

```
run-secrets/
├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_*
├── mock_provider_key
└── mock_db_password
simulate.sh              # runtime 본문 변조 시뮬레이션
```

## Cycle 영역

- Cycle 2 = 본 fixture 작성 한정
- Cycle 4 = `simulate.sh` 호출 step
- Cycle 6 = actual run 시연
