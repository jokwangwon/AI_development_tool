# pass/normal_operation — 정상 운영 시나리오

> **Backlog #1 ST-2 Cycle 2 fixture #1** — init grace period 이후 runtime 변경 0건. sidecar 가 정상 운영 상태 유지 시연.

## 시나리오

1. sidecar startup → init grace period 10초 (사용자 #8 결정 답습) 동안 inotify event 무시
2. init grace 종료 후 inotify watch 본격 시작
3. 본 fixture 의 `run-secrets/` 파일은 **변경 0건** (mtime / mode / content / 존재 모두 정적 유지)

## 기대 결과 (Cycle 6 시점 시연)

| 검증 항목 | 기대 |
|---------|------|
| sidecar status file (`/var/run/sidecar-status`) | empty (or absent) |
| hermes-mock healthcheck | `healthy` |
| inotify event 발화 | 0건 |
| docker-compose `gp3_st2_sidecar_integration` step | PASS |

## fixture 구성

```
run-secrets/
├── mock_api_key         # FAKE_CANARY_DO_NOT_USE_* (R-4.1 답습)
├── mock_provider_key
└── mock_db_password
```

simulate.sh 미보유 (runtime 변경 0건).

## Cycle 영역

- Cycle 2 = 본 fixture 작성 한정
- Cycle 3 ~ Cycle 6 = 본 fixture 미사용 (sidecar 본문 + CI step + actual run 후속)
