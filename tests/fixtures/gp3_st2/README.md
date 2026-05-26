# GP-3 ST-2 inotify sidecar fixtures (Cycle 2)

> **Backlog #1 ST-2 inotify sidecar PoC fixture 세트** — Cycle 2 한정 진입.
>
> 본 디렉토리는 **Cycle 6 actual run 시연용 fixture 데이터** — sidecar 본문 구현 (Cycle 3) + CI step (Cycle 4) 후 검증에 사용.

---

## 1. 본 fixture 의 목적

`docker/gp3-st2-poc/` PoC 격리 환경에서 sidecar (Cycle 3 구현 예정) 의 fail-closed 동작 검증을 위한 **5 시나리오 fixture** 세트.

### 1.1 권위 출처

- 상위 brief = `docs/phase0/backlog1-st2-implementation-brief.md` (`997ca18`, 16 섹션 §8 + §9.1 답습)
- 상위 합의 = `docs/review/3plus1-consensus-2026-05-13-st2-implementation-entry.md` (`6c616a8`)
- Cycle 1 README = `docker/gp3-st2-poc/README.md` (`c558216`)
- R-4.1 Tier-1 catalog (fake canary 의무) + ADR-008 §A.2 R1-2 + GP-3 §5.3

---

## 2. fixture 5개 목록

| Fixture | 시나리오 | 기대 결과 (Cycle 6 시점 시연) |
|---------|--------|--------------|
| `pass/normal_operation/` | init grace 후 runtime 변경 0건 | sidecar status empty / hermes-mock healthy |
| `pass/init_phase/` | init grace period 내 정상 secret 주입 | event 무시 (grace) / hermes-mock healthy |
| `fail/chmod_644/` | runtime `chmod 644 /run/secrets/mock_api_key` 시뮬레이션 | `IN_ATTRIB` 감지 / status `UNHEALTHY: IN_ATTRIB ...` / hermes-mock unhealthy |
| `fail/content_modified/` | runtime mock secret 본문 변경 시뮬레이션 | `IN_MODIFY` 감지 / status `UNHEALTHY: IN_MODIFY ...` / hermes-mock unhealthy |
| `fail/file_deleted/` | runtime mock secret 파일 삭제 시뮬레이션 | `IN_DELETE_SELF` 감지 / status `UNHEALTHY: IN_DELETE_SELF ...` / hermes-mock unhealthy |

---

## 3. fixture 구조

각 fixture 하위 구조:

```
<fixture>/
├── README.md            # 시나리오 설명 + 기대 결과 + Cycle 3 sidecar 동작 명시
├── run-secrets/         # mock secret 파일 (Cycle 3 docker-compose 가 /run/secrets/ 로 mount)
│   ├── mock_api_key     # fake canary (R-4.1 답습)
│   ├── mock_provider_key
│   └── mock_db_password
└── simulate.sh          # (fail/* 전용) runtime 시뮬레이션 스크립트
```

`pass/*` fixture 는 `simulate.sh` 미보유 (runtime 변경 0건).

---

## 4. 영구 강제 안전 원칙

| # | 영역 |
|---|------|
| 1 | **실 secret 본문 commit 0건** (영구 금지 — R-4.1 답습) — 모든 mock secret = `FAKE_CANARY_DO_NOT_USE_*` prefix |
| 2 | fixture mount 권한 = read-only (docker-compose 정의 시) |
| 3 | sidecar 가 mock secret 본문을 logging / hashing / export 하지 않음 (Cycle 3 sidecar 본문 구현 시점 강제) |
| 4 | simulate.sh 가 production 영역 또는 sibling fixture 에 영향 주지 않음 (격리) |

---

## 5. Cycle 2 영역 한계

본 Cycle 2 = **fixture 작성 한정**:

- ❌ sidecar Dockerfile 작성 0건 (Cycle 3 영역)
- ❌ inotify script 작성 0건 (Cycle 3 영역)
- ❌ docker-compose 작성 0건 (Cycle 3 영역)
- ❌ CI workflow 변경 0건 (Cycle 4 영역)
- ❌ actual run 실행 0건 (Cycle 6 영역)
- ❌ §C-5 / C-5a Satisfied 자동 갱신 0건 (Cycle 6 후속 별도 합의)

본 fixture 는 **Cycle 3 sidecar 구현 후 Cycle 4 CI step 에서 호출** — 본 Cycle 2 시점은 데이터 준비 한정.

---

## 6. 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

Cycle 2 commit 완료 후 사용자 결정 영역:

| 후보 | 영역 |
|------|------|
| (1) | Cycle 3 진입 (sidecar Dockerfile + watch script + docker-compose + hermes-mock) — **test + feat 2 commit 분리 (사용자 #6 결정 답습)** |
| (2) | 보류 → 다른 backlog 우선 |
| (3) | 세션 종료 |

⚠️ **Cycle 3 자동 진입 금지** — 사용자 명시 결정 영역.

---

**작성일**: 2026-05-13 후속 27 (Cycle 2)
**상태**: fixture 작성 한정 — sidecar 본문 구현 / docker-compose / CI step / actual run 모두 미진입
