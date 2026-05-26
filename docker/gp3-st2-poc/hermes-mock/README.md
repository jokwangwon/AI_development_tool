# hermes-mock — ST-2 PoC mock target (Cycle 3 test/scaffold)

> **Backlog #1 ST-2 inotify sidecar PoC mock target** — Cycle 3 test/scaffold commit 영역.
>
> 본 container 는 실 Hermes 영향 0건 — Hermes upstream Dockerfile 변경 0건 보존 (`0e99a56` + 사용자 #1 결정 답습).

---

## 1. 목적

F-B 우선 답습 시연용 mock target:

- `inotify-sidecar` (Cycle 3 feat commit 영역) 가 status file 에 UNHEALTHY 기록 시
- 본 container 의 docker-compose healthcheck 가 exit 1
- retries 2 초과 시 hermes-mock = unhealthy 처리
- docker-compose 가 정지 시뮬레이션 발생

## 2. 권위 출처

- ST-2 실 구현 brief = `docs/phase0/backlog1-st2-implementation-brief.md` §2 + §3
- ST-2 실 구현 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-implementation-entry.md` (`6c616a8`)
- ST-2 진입 적격성 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-inotify-sidecar-entry.md` (`0e99a56`)
- ADR-008 §A.2 R1-2 + §2.6.2 R2-1

## 3. 구성 요소

| 파일 | 영역 |
|------|------|
| `Dockerfile` | alpine + healthcheck.sh + `sleep infinity` entrypoint |
| `healthcheck.sh` | sidecar status file read + exit 0/1 결정 |
| `README.md` | 본 파일 |

## 4. 사용자 명시 9 결정 답습 (본 container 관련)

| # | 결정 | 본 container 적용 |
|---|------|------|
| 1 | fail-closed = F-B 우선 / F-A 비채택 | healthcheck.sh = status file 읽기 한정 (docker socket / Hermes upstream 접근 0건) |
| 9 | healthcheck interval 5초 | docker-compose level (Cycle 3 feat commit 답습) |

## 5. 영구 강제 안전 원칙

- 본 container 가 secret 본문 자체 접근 0건 (status file 만 read — 단, simulate.sh 실행 시 fixture run-secrets/ 에 read-write 접근 — runtime 변경 시뮬레이션 용도 한정)
- 본 container 가 docker socket / privileged / host network 접근 0건
- status content logging / hashing / export 0건 (R-4.1 답습)
- 실 Hermes Dockerfile 변경 0건 (Hermes upstream 영역 분리)
- cap_drop ALL (docker-compose level)

## 6. Cycle 영역

- **Cycle 3 test/scaffold (본 commit)** = 본 container (mock target) 구현 한정
- Cycle 3 feat = sidecar Dockerfile + watch-secrets.sh + docker-compose 구현 (별도 commit)
- Cycle 4 ~ Cycle 6 = 본 container 변경 0건 (CI step / actual run 외부 호출 한정)

## 7. 동작 흐름 (Cycle 3 feat commit + Cycle 6 actual run 시점)

```
1. fixture-init container (Cycle 3 feat) → fixture run-secrets/ 를 named volume 으로 복사
2. inotify-sidecar 시작 → init grace 10초 → inotifywait 시작
3. hermes-mock 시작 (sidecar service_healthy 이후, F-C 보조 답습)
4. (fail/* 시나리오) hermes-mock 내부에서 /fixtures/<fixture>/simulate.sh 실행
5. simulate.sh 가 /run/secrets/mock_api_key 변경 (chmod / modify / rm)
6. inotify-sidecar 가 event 감지 → status file 에 "UNHEALTHY: <event> <path> <ts>" 기록
7. hermes-mock healthcheck (interval 5초) → status file 읽고 exit 1
8. retries 2 초과 → hermes-mock = unhealthy 상태
```

## 8. 본 container 가 *하지 않는* 것

- ❌ docker socket 접근 (F-A 비채택 답습)
- ❌ Hermes upstream Dockerfile 변경
- ❌ privileged / host network / capability 추가
- ❌ status content 본문 logging / hashing / export
- ❌ secret 본문 자체 logging / export (simulate.sh 는 변경만 — 본문 읽기 0건)
- ❌ production docker-compose 변경
- ❌ CI workflow 자동 진입 (Cycle 4 영역)
- ❌ actual run 자동 진입 (Cycle 6 영역)
