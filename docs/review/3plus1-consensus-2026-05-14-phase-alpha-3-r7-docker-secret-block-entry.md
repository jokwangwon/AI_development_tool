# Reviewer-only 단축 합의 보고서 — Phase α-3 R-7 docker secret block 진입 Brief

> **본 문서는 `docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md` (DRAFT, commit `8da3273`) 의 Reviewer-only 단축 합의 보고서.** 사용자 명시 진입 명령 ("옵션 A로 진행해주세요") 답습.
>
> 본 합의 = **수단 결정 적격성 권위 권고 발행 한정** — 실 변경 0건. Phase α-3 실 진입 / R-7 docker secret block 본문 변경 / Production `docker-compose.yml` 신설 / Hermes upstream Dockerfile 변경 / Phase α-1 / α-2 / α-4 자동 진입 / Layer C 발효 / MVP-1 PASS / 7 금지 영역 해소 / ST-1 / ST-2 / ST-4 / ST-5 흡수 / R-MVP1-G3-3 자동 발화 / 실 secret material commit 모두 본 합의 영역 외.

**작성일**: 2026-05-14 후속 13
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**검토 대상**: `docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md` (commit `8da3273`, 748줄)
**상위 권위 (답습 한정)**:
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-2-r5-importlinter-body-entry.md` (Phase α-2 R-5 합의, commit `6a79247` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-phase-alpha-1-r4-tools-body-entry.md` (Phase α-1 R-4 합의, commit `1b3090b` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog6-runtime-ci-hook-priority-entry.md` (Backlog #6 우선 진입 합의, commit `c7ddfdd` APPROVE AS BRIEF, Reviewer-only 단축)
- `docs/review/3plus1-consensus-2026-05-14-backlog3-enforcement-defense.md` (Group α 합의, commit `4880e88` APPROVE WITH CONDITIONS 3/3 만장일치)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-implementation-entry.md` (Layer B APPROVE, commit `f40423f`)
- `docs/review/3plus1-consensus-2026-05-12-backlog6-runtime-ci-hook-entry.md` (Layer A APPROVE, commit `f1e0b23`)
- `docs/review/3plus1-consensus-2026-05-12-gp3-mvp1-entry.md` (GP-3 MVP-1 진입 합의 — ST-3 단독 채택 권위 권고, commit `6dc5bdc`)
- `docs/review/3plus1-consensus-2026-05-12-gp3-stage2-implementation-entry.md` (**GP-3 Stage 2 (ST-3 docker secret) 단독 구현 진입 합의 APPROVE — sub-step 2.1 ~ 2.4 4 cycle**)
- `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.4.2 + §5.3 + §5.5.1 ST-3 본문 채택 (commit `55c5b4b`)
- ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 (file system secret isolation — docker secret 답습)
- ADR-011 §2.1 (a)~(e) 5조건 패턴 + §2.4 T2 영역 (CI step Entry)

---

## 0. 본 합의 범위

### 0.1 사용자 명시 진입 명령 답습

> "옵션 A로 진행해주세요"

(Phase α-1 / α-2 패턴 답습 — brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 R-7 docker secret block 수정은 아직 하지 않음.)

사용자 명시 7 금지 답습 (Phase α-1 / α-2 패턴 답습 — brief §0.2 답습):

1. ❌ 실 R-7 docker secret block 수정 금지 — `docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` + `tests/fixtures/gp3_st3/` 어느 줄도 변경 0건 (현 9 artifacts × 328줄 답습 보존)
2. ❌ CI workflow 변경 금지
3. ❌ branch protection 변경 금지
4. ❌ dev 환경 강제 금지
5. ❌ `pre-commit install` 의무화 금지
6. ❌ Operational Readiness PASS 선언 금지
7. ❌ Hermes PMO 격상 금지

### 0.2 본 합의가 *하는* 것

1. Brief `phase-alpha-3-r7-docker-secret-block-entry-brief.md` (DRAFT, `8da3273`) 의 **수단 결정 적격성 권위 권고** 발행
2. **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-3 영역 답습** 확인
3. **Phase α-3 = R-7 docker secret block 영역 정의** 채택 권고 (9 artifacts × 328줄 + ST-3 단독 답습 + 4 sub-step)
4. **R-7 PoC 답습 변경 0건 확정** 채택 권고
5. **ST-3 단독 답습 채택** (ST-1 / ST-2 / ST-4 / ST-5 분리 명시)
6. **Phase α-3 진입 적격성 5 조건 (C-α3-1 ~ C-α3-5) 5/5 충족** 검증
7. **12/12 풀 3+1 승격 트리거 0건 발화** 검증
8. **R-7 영역 영향 Rollback Trigger 18개 분류** 채택 권고 + ST-1/2/4/5 별도 backlog 4 trigger 분리
9. **실 R-7 docker secret block 수정 진입 아직 아님** 답습 명시

### 0.3 본 합의가 *하지 않는* 것

- ❌ Phase α-3 실 진입 (R-7 본문 변경 0건)
- ❌ R-7 영역 9 artifacts × 328줄 어느 줄도 변경 0건 (`docker/gp3-st3-poc/docker-compose.gp3-st3.yml` / `Dockerfile` / `app.py` / `secrets/api_key.placeholder` / `tools/docker_secret_image_layer_check.sh` / `tools/docker_secret_restart_recovery.sh` / `tests/fixtures/gp3_st3/{pass,fail}/`)
- ❌ `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 변경 0건 (R-1 영역 = Phase α-4)
- ❌ Production `docker-compose.yml` 신설 / 변경 0건 (PoC 격리 디렉토리 한정 답습)
- ❌ Hermes upstream Dockerfile 변경 0건 (ADR-008 차단조건 #6 + 부록 B 답습 보존)
- ❌ R-4 도구 (`secret_scanner.py` / `provider_import_scanner.py` / `provider_url_scanner.py`) 변경 0건
- ❌ R-5 `.importlinter` 본문 변경 0건
- ❌ R-1 CI workflow 신설 / 본문 변경 0건
- ❌ Phase α-1 / α-2 / α-4 자동 진입 0건
- ❌ Phase β / γ 자동 진입 0건
- ❌ 실 hook 구현 (`.pre-commit-config.yaml` / `.git/hooks/*` 본문 변경 0건)
- ❌ Backlog #6 우선 진입 합의 §6.1 1순위 *해소* (의존성 정리 한정)
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *해소* 0건
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) *해소* 0건
- ❌ GP-3 Stage 2 합의 *재결정* 0건
- ❌ GP-3 MVP-1 진입 합의 (`6dc5bdc`) *재결정* 0건
- ❌ 사용자 명시 7 금지 영역 어느 것의 *해소* (분리 매트릭스 한정)
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ MVP-1 PASS (Layer D) 선언
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ Group α 합의 본문 변경 / 14 결정 영역 *재결정*
- ❌ Layer A / Layer B / §5.5.1 ST-3 본문 채택 *재결정*
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ ST-3 = ST-1 / ST-2 / ST-4 / ST-5 흡수 시도 0건 (단독 답습)
- ❌ ST-4 Vault HSM 진입 0건 (Backlog #7 분리)
- ❌ inotify sidecar (`tools/docker_secret_inotify_sidecar_check.sh` 258줄) 본 영역 흡수 0건 (Backlog #1 ST-2 분리)
- ❌ R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) trigger 자동 발화 0건
- ❌ G3-7 row 4 항목 자동 흡수 0건 (Stage 5 별도 영역 분리)
- ❌ 실 secret material commit 0건 (`secrets/api_key.placeholder` = FAKE_TEST_SECRET marker 답습)
- ❌ `secrets/.gitignore` 변경 0건 (placeholder 한정 영구 답습)
- ❌ secret material marker 위반 0건 (실 vendor prefix 사용 금지)
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ GitHub plan / ruleset 가용성 자동 확인
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold *고정* (image layer leak 0 / restart recovery 100% / latency 모두 *후보 한정* 유지)
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출 (Group α C-11 답습 — 응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 인간 리뷰 의무 자동 발화
- ❌ 실 docker build / docker run / docker history 자동 실행
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ event enum 정식 등록 (`event: docker_secret_isolation_layer1_implementation` = Backlog #5 분리)

### 0.4 본 합의 후속 commit chain

| Commit | 영역 | 권위 |
|--------|------|----|
| Commit 1 (`8da3273`) | brief 신설 (`docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md`, 748줄) | brief 본문 채택 |
| **Commit 2** | **본 합의 보고서 신설 (`docs/review/3plus1-consensus-2026-05-14-phase-alpha-3-r7-docker-secret-block-entry.md`)** | **Reviewer-only 단축 합의 — APPROVE AS BRIEF** |
| Commit 3 | 메타 갱신 (CONTEXT.md / INDEX.md / SESSION_2026-05-14.md) | 메타 답습 |

---

## 1. Phase α-3 R-7 docker secret block 영역 정의 채택 (Brief §2 답습)

### 1.1 R-7 = docker secret block 영역 정의 채택 (Backlog #6 우선 진입 합의 §2 + Layer B §5.5.1 + GP-3 Stage 2 합의 답습)

| 영역 | 답습 출처 | 현 상태 (2026-05-15 기준) | 본 합의 채택 |
|------|---------|----------------------|----------|
| 책무 (ST-3 영역) | GP-3 저장 경로 secret 검출 (G3-1) — file system secret isolation | Layer B §5.5.1 ST-3 본문 채택 답습 | ✅ 답습 채택 |
| 도구 | docker-compose secret block + image layer 검증 + container restart recovery | GP-3 Stage 2 합의 4 sub-step 답습 | ✅ 답습 채택 |
| 권위 | ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 | upstream 변경 회피 답습 | ✅ 답습 채택 |
| 책무 분리 (ST-3 단독) | Vault HSM ST-4 미진입 (Backlog #7) / entrypoint stat ST-1 / inotify sidecar ST-2 미진입 (Backlog #1 1.5차 보강) / ST-5 Defense in depth (MVP-2 이후) | GP-3 진입 합의 답습 | ✅ 답습 채택 |

### 1.2 R-7 본문 9 artifacts 답습 채택 (실 본문 변경 0건 — enumerate 한정)

| # | 산출물 | 경로 | 현 라인 수 | sub-step | 본 합의 변경 |
|---|--------|------|---------|---------|---------|
| 1 | docker-compose secret block | `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` | 34 | 2.1 | 0건 |
| 2 | Dockerfile (PoC) | `docker/gp3-st3-poc/Dockerfile` | 12 | 2.1 | 0건 |
| 3 | 응용 (secret read) | `docker/gp3-st3-poc/app.py` | 46 | 2.1 | 0건 |
| 4 | placeholder secret material | `docker/gp3-st3-poc/secrets/api_key.placeholder` | 1 | 2.1 | 0건 (FAKE_TEST_SECRET marker 답습) |
| 5 | image layer 검증 도구 | `tools/docker_secret_image_layer_check.sh` | 99 | 2.2 | 0건 |
| 6 | container restart recovery 도구 | `tools/docker_secret_restart_recovery.sh` | 118 | 2.3 | 0건 |
| 7 | PASS fixture (Dockerfile) | `tests/fixtures/gp3_st3/pass/Dockerfile` | 9 | 2.2 | 0건 |
| 8 | FAIL fixture (Dockerfile) | `tests/fixtures/gp3_st3/fail/Dockerfile` | 8 | 2.2 | 0건 |
| 9 | FAIL fixture (secret material) | `tests/fixtures/gp3_st3/fail/baked_secret.txt` | 1 | 2.2 | 0건 (FAKE_TEST_SECRET marker 답습) |

**합산**: 9 artifacts × **328줄 PoC 본문 답습 변경 0건** *확정 채택*.

### 1.3 R-7 = Layer B §5.5.1 GP-3 4 sub-수단 中 ST-3 답습 채택

| sub-수단 ID | 영역 | 본문 채택 권위 (답습 한정) | R-7 관계 | 본 합의 채택 |
|----------|------|----------------------|----------|----------|
| S-1 | 코드 본문 secret 검출 (R-4.1 Tier-1 45 patterns) | Group D PoC 답습 | R-4 영역 (Phase α-1) — Stage 1 | ✅ 영역 분리 답습 |
| **ST-3** | **docker secret (저장 경로 isolation)** | **ADR-008 차단조건 #6 + 부록 B 답습 + Layer A §1.2 + Layer B §1.1 답습** | **R-7 본문 = ST-3 본문 (Stage 2)** | ✅ **답습 채택** |
| PC-3 | CI-only enforcement (pre-commit) | T2 영역 답습 | Stage 4 영역 (양 GP 공유) | ✅ 영역 분리 답습 |
| AR-1 | CI step fail-closed (PR auto-reject) | T2 영역 답습 | Stage 4 영역 (양 GP 공유) | ✅ 영역 분리 답습 |

**범위 한계**: S-1 (R-4) = Phase α-1 영역 / PC-3 + AR-1 (Stage 4) = 별도 Stage 영역 분리.

### 1.4 R-7 = ST 5 후보 中 ST-3 단독 답습 채택 (mvp1.md §5.3)

| ST 후보 | 영역 | 본 합의 채택 |
|--------|------|----------|
| ST-1 | entrypoint stat (시작 시점) | ✅ 영역 외 답습 (Backlog #1 1.5차 보강) |
| ST-2 | inotify sidecar (런타임 지속) | ✅ 영역 외 답습 (Backlog #1 분리 — `tools/docker_secret_inotify_sidecar_check.sh` 258줄 존재 = 본 합의 영역 외) |
| **ST-3** | **docker secret (저장 경로 isolation)** | ✅ **답습 채택 (MVP-1 1차)** |
| ST-4 | Vault HSM (외부 키 관리) | ✅ 영역 외 답습 (Backlog #7 + MVP-6 이후) |
| ST-5 | ST-1 + ST-2 + ST-3 통합 (Defense in depth) | ✅ 영역 외 답습 (MVP-2 이후) |

본 합의 = **ST-3 단독 답습 한정** (MVP-1 1차 — Hermes upstream 변경 회피 보존).

---

## 2. R-7 PoC 답습 변경 0건 확정 (Brief §3 답습)

### 2.1 R-7 본문 답습 검증 채택

| 영역 | PoC 답습 | 현 상태 | 본 합의 변경 |
|------|--------|----------|---------|
| `docker/gp3-st3-poc/` (93줄, 4 파일) | ADR-008 차단조건 #6 + 부록 B + mvp1.md §3.4.2 + §5.3 답습 | 4 파일 답습 (compose + Dockerfile + app + placeholder) | 0건 |
| `tools/docker_secret_image_layer_check.sh` (99줄) | mvp1.md §3.4.2 `docker_secret_isolation_check` 답습 | 99줄 답습 | 0건 |
| `tools/docker_secret_restart_recovery.sh` (118줄) | mvp1.md §3.4.2 `container_restart_recovery` 답습 | 118줄 답습 | 0건 |
| `tests/fixtures/gp3_st3/{pass,fail}/` (18줄, 3 파일) | Stage 2 합의 §1.3 답습 | 3 파일 답습 (PASS + FAIL Dockerfile + baked_secret.txt) | 0건 |

**합산**: 9 artifacts × **328줄 PoC 답습 100% 보존** + 본 합의 발효 시점 변경 0건 *확정 채택*.

### 2.2 R-7 = Layer B §5.5.1 + GP-3 Stage 2 합의 답습 채택

| 답습 항목 | 본 합의 검증 | 충족 |
|---------|--------|------|
| Layer B `f40423f` APPROVE 발효 + §5.5.1 ST-3 본문 채택 (`55c5b4b`) | ✅ 답습 변경 0건 | ✅ |
| GP-3 MVP-1 진입 합의 (`6dc5bdc`) — ST-3 단독 채택 권위 권고 | ✅ 답습 변경 0건 | ✅ |
| GP-3 Stage 2 합의 (Reviewer-only APPROVE) — sub-step 2.1 ~ 2.4 4 cycle 발효 | ✅ 답습 변경 0건 | ✅ |
| Stage 2 actual run PASS (run_id `25728590939` 후속) | ✅ 선행 evidence 답습 | ✅ |
| ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 답습 | ✅ 답습 변경 0건 (Hermes upstream 변경 회피 보존) | ✅ |

**합산**: 5/5 답습 검증 *확정 채택*.

### 2.3 R-7 × Phase α-3 sub-step 분할 매트릭스 채택 (Brief §3 답습)

| sub-step | 영역 | 답습 출처 | 본 합의 채택 |
|---------|------|---------|----------|
| 2.1 | docker-compose secret block 본문 답습 검증 (34줄) | ADR-008 차단조건 #6 + 부록 B + mvp1.md §3.4.2 답습 | ✅ 답습 enumerate 한정 |
| 2.1.a | Dockerfile + app.py + placeholder 답습 검증 (59줄) | PoC 격리 영역 답습 | ✅ 답습 enumerate 한정 |
| 2.1.b | `secrets/.gitignore` + placeholder 답습 검증 | F-금지 #1 marker 답습 | ✅ 답습 enumerate 한정 |
| 2.2 | image layer 검증 도구 답습 (99줄) | mvp1.md §3.4.2 `docker_secret_isolation_check` 답습 | ✅ 답습 enumerate 한정 |
| 2.2.a | PASS / FAIL fixture (Dockerfile) 답습 검증 | Stage 2 합의 §1.3 답습 | ✅ 답습 enumerate 한정 |
| 2.3 | container restart recovery 도구 답습 (118줄) | mvp1.md §3.4.2 `container_restart_recovery` 답습 | ✅ 답습 enumerate 한정 |
| 2.4 | CI Stage 2 entry step 답습 (R-1 영역 = Phase α-4) | Stage 2 합의 §1.3 답습 | ✅ 답습 검증 한정 (실 변경 = Phase α-4) |
| 2.4.a | ledger entry 형식 답습 — `event: docker_secret_isolation_layer1_implementation` 후보 | mvp1.md §5.2 enum *후보 한정* 답습 | ✅ 정식 등록 0건 (Backlog #5 분리) |
| 2.4.b | Evidence Artifact 형식 답습 | Layer B §1.8 (a) 답습 | ✅ 실 생성 = Layer C 시점 (영역 외) |

**합산**: **9 sub-step 답습 enumerate 한정** *확정 채택* — 실 sub-step 결정 = Phase α-3 실 진입 시점.

---

## 3. ST-3 단독 답습 채택 (Brief §2.4 답습)

### 3.1 ST-3 단독 답습 채택 매트릭스

| ST 후보 | 영역 | 본 합의 분리 | 진입 시점 |
|--------|------|----------|--------|
| ST-1 | entrypoint stat (시작 시점) | ✅ Backlog #1 1.5차 보강 분리 | Hermes upstream Dockerfile 변경 필요 — 풀 3+1 합의 trigger |
| ST-2 | inotify sidecar (런타임 지속) | ✅ Backlog #1 분리 (`tools/docker_secret_inotify_sidecar_check.sh` 258줄 = 영역 외) | Hermes upstream 변경 필요 |
| **ST-3** | **docker secret (저장 경로 isolation)** | ✅ **본 합의 영역 (MVP-1 1차)** | **Hermes upstream 변경 회피** |
| ST-4 | Vault HSM (외부 키 관리) | ✅ Backlog #7 분리 + MVP-6 이후 | MVP-6 이후 별도 합의 |
| ST-5 | ST-1 + ST-2 + ST-3 통합 (Defense in depth) | ✅ MVP-2 이후 분리 | MVP-2 이후 별도 합의 |

**합산**: 5/5 ST 후보 분리 매트릭스 채택 — ST-3 단독 진입 적격 + ST-1 / ST-2 / ST-4 / ST-5 영역 외 답습.

### 3.2 ST-3 단독 답습 채택 근거

1. **MVP-1 1차 답습** — mvp1.md §5.3 (ST-3 = MVP-1 1차 docker secret 단독, Hermes upstream 변경 회피)
2. **GP-3 진입 합의 답습** — ST-3 단독 채택 권위 권고 (`6dc5bdc`)
3. **GP-3 Stage 2 합의 답습** — Stage 2 (ST-3) 단독 구현 진입 APPROVE
4. **Hermes upstream 변경 회피 보존** — ADR-008 차단조건 #6 + 부록 B 답습

---

## 4. 5/5 진입 적격성 5 조건 충족 검증 (Brief §5.1 답습)

### 4.1 적격성 검토 매트릭스 채택

| 조건 # | 조건 | 본 합의 검증 결과 | 판정 |
|------|------|--------------|----|
| **C-α3-1** | **사용자 명시 7 금지 영역 충돌 0** | R-7 docker secret block = file-system 격리 영역 — 7 금지 영역 모두 직교 또는 영역 분리 (충돌 0). 금지 #1 (실 R-7 수정) / #2 (CI workflow 변경) = Phase α-3 *실 진입* 시점 적용 — 본 합의 = 검토 한정 (충돌 0). | ✅ **0/7 충돌** |
| **C-α3-2** | **PoC 답습 변경 0** | R-7 영역 9 artifacts × 328줄 답습 + GP-3 Stage 2 합의 §1.3 4 sub-step 답습 + ADR-008 차단조건 #6 + 부록 B 답습 + ST-3 단독 채택 답습 + Layer B §5.5.1 ST-3 본문 채택 답습 모두 변경 0건 | ✅ **답습 100% 보존** |
| **C-α3-3** | **의존성 0 (Phase α-1 / α-2 / α-3 병렬 진입 적격)** | R-7 ↔ R-4 = 영역 분리 (S-1 코드 본문 vs ST-3 저장 경로 — 의존 0) + R-7 ↔ R-5 = 영역 분리 (provider import vs file-system isolation — 의존 0) + R-7 ↔ R-1 = Phase α-4 영역 + Stage 2 actual run PASS 검증 답습 (run_id `25728590939` 후속) — 의존성 해소됨 | ✅ **의존성 0 (병렬 진입 적격)** |
| **C-α3-4** | **Provider Liquidity 5-way 100% 보존** | R-7 = file-system secret isolation Layer (R2-1) — catalog / provider 영역과 직교 + docker secret = vendor-agnostic 표준 (Docker BuildKit / Docker Compose) + secret material = placeholder 답습 | ✅ **5/5 100% 보존** |
| **C-α3-5** | **5 영구 핵심 제약 보존** | Hermes ≠ root of trust 보존 (R-7 = file-system isolation, Hermes upstream 변경 0건) / 단일 source-of-truth 보존 (PoC 답습 변경 0건) / 수단/목적 분리 보존 (R-7 = 수단, 목적 = 저장 경로 secret isolation) / T1/T2/T3 분리 보존 (R-7 = T2 영역, ST-4 Vault HSM = T3 영역 분리) / SPOF 의도적 수용 보존 | ✅ **5/5 보존** |

**합산**: **5/5 충족** *확정 채택* — Phase α-3 진입 적격성 검증 완료 + 실 진입 결정 = 사용자 명시 결정 영역 (자동 진입 0건).

---

## 5. 12/12 풀 3+1 승격 트리거 0건 발화 검증 (Brief §5.2 답습)

| # | 트리거 | 본 합의 발화 |
|---|----|----------|
| 1 | Group α 합의 C-1 ~ C-12 / Backlog #6 C-α-1 ~ C-α-11 / Phase α-1 C-β-1 ~ C-β-15 / Phase α-2 C-γ-1 ~ C-γ-26 / GP-3 Stage 2 합의 어느 것의 *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 |
| 2 | 사용자 명시 7 금지 영역 中 1+ *해소* 권고 | ❌ 0건 — 본 합의 = 분리 매트릭스 한정 |
| 3 | Layer B §5.5.1 GP-3 4 sub-수단 (S-1 + ST-3 + PC-3 + AR-1) *재결정* 권고 | ❌ 0건 — 본 합의 = 답습 한정 (ST-3 영역 한정) |
| 4 | Provider Liquidity 5-way 약화 가능성 | ❌ 0건 — docker secret = vendor-agnostic 표준 (catalog / provider 영역과 직교) |
| 5 | 5 영구 핵심 제약 中 1+ 약화 | ❌ 0건 — 5/5 보존 답습 |
| 6 | T3 영역 진입 권고 | ❌ 0건 — R-7 = T2 영역 (ST-4 Vault HSM = T3 영역 분리) |
| 7 | ADR-008 부록 C Hermes PMO Activation 12 조건 中 1+ 충족 발생 | ❌ 0건 — Hermes PMO 격상 분리 명시 한정 |
| 8 | secret handling 방식이 기존 정책 변경 권고 (GP-3 Stage 2 §1.8 #1 답습) | ❌ 0건 — ADR-008 차단조건 #6 + 부록 B 답습 변경 0건 + Hermes upstream 변경 0건 |
| 9 | Hermes upstream root of trust 변경 권고 (GP-3 Stage 2 §1.8 #2 답습) | ❌ 0건 — docker secret = upstream 분리 영역 (ADR-011 §2.1 (b) 수단/목적 분리 답습) |
| 10 | Docker secret / local config / CI secret 경계 불명확 (GP-3 Stage 2 §1.8 #3 답습) | ❌ 0건 — ST-3 + S-1 + G3-7 경계 명확 |
| 11 | ST-3 = ST-1/2/4/5 흡수 시도 권고 | ❌ 0건 — ST-3 단독 답습 한정 (mvp1.md §5.3 답습) |
| 12 | 실 secret material commit / `secrets/.gitignore` 변경 권고 | ❌ 0건 — placeholder 한정 영구 답습 (F-금지 #1 marker 답습) |

**검증 결과**: **12/12 트리거 0건 발화** → **Reviewer-only 단축 합의 적격 확정** ✅

---

## 6. R-7 영역 영향 Rollback Trigger 18개 분류 채택 (Brief §6.1 답습)

### 6.1 R-7 본문 영역 *직접* 영향 trigger (2개) — 의존성 enumerate 한정

| Trigger | 발화 조건 | R-7 영향 | 본 합의 채택 |
|--------|---------|-----------|----------|
| R-MVP1-G3-3 | ST-3 Docker secret 도입 실패 | `docker/gp3-st3-poc/` + `tools/docker_secret_*.sh` 본문 영향 | ✅ 답습 한정 (발화 0건 — Stage 2 actual run PASS 답습) |
| R-MVP1-G3-4 | PC-3 CI runtime 폭증 (>2분) | image layer 검증 + restart recovery 실행 시간 *간접* 영향 | ✅ 답습 한정 (발화 0건) |

### 6.2 R-7 영역 *간접* 영향 trigger (1개) — Layer E 영역 의존

| Trigger | 영역 의존 | 본 합의 채택 |
|--------|---------|----------|
| R-MVP1-G3-8 | Operational Readiness parity 필요 (Hermes runtime parity) | ✅ 영역 외 답습 (Layer E, 금지 #6 답습) |

### 6.3 R-7 영역 *영향 0* trigger (15개) — Phase α-1/α-2/T3/MVP-3/MVP-6/Backlog 분리

| Trigger | 분리 사유 | 본 합의 채택 |
|--------|--------|----------|
| R-MVP1-G3-1 | S-1 FP_rate 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G3-2 | S-2 gitleaks (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G3-5 | AR-1 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G3-6 | R-4.1 Tier-1 catalog 변경 (Backlog #3) | ✅ 영역 외 답습 |
| R-MVP1-G3-7 | Tier-2 확장 (Backlog #1 1.5차) | ✅ 영역 외 답습 |
| R-MVP1-G5-1 | T-2 FP_rate 폭증 (R-5 영역 = Phase α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-2 | T-5 단독 FN 폭증 (R-4 영역 = Phase α-1) | ✅ 영역 외 답습 |
| R-MVP1-G5-3 | T-6 병행 충돌 (Phase α-1 + α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-4 | `.importlinter` rule 충돌 (R-5 영역 = Phase α-2) | ✅ 영역 외 답습 |
| R-MVP1-G5-5 | PC-3 hook 우회 (T3 영역) | ✅ 영역 외 답습 |
| R-MVP1-G5-6 | AR-1 fail-closed 폭증 (Stage 4 + R-1 영역) | ✅ 영역 외 답습 |
| R-MVP1-G5-7 | P1 v2 facade real (Backlog #4) | ✅ 영역 외 답습 |
| R-MVP1-G5-8 | branch protection (T3, 금지 #3) | ✅ 영역 외 답습 |
| R-MVP1-G5-9 | 의미적 lock-in (MVP-3) | ✅ 영역 외 답습 |
| R-MVP1-G5-10 | Layer 2 runtime (MVP-3/4) | ✅ 영역 외 답습 |

### 6.4 ST-1 / ST-2 / ST-4 / ST-5 별도 backlog trigger (4개) — 분리 명시

| ST 후보 | 진입 trigger | 본 합의 채택 |
|--------|----------|----------|
| ST-1 | entrypoint stat 검증 필요 — Hermes upstream Dockerfile 변경 의존 | ✅ 영역 외 답습 (Backlog #1 1.5차 보강, 풀 3+1 합의 trigger) |
| ST-2 | inotify sidecar 운영 필요 — `tools/docker_secret_inotify_sidecar_check.sh` 258줄 존재 | ✅ 영역 외 답습 (Backlog #1 분리) |
| ST-4 | Vault HSM 외부 키 관리 필요 | ✅ 영역 외 답습 (Backlog #7 분리, MVP-6 이후) |
| ST-5 | Defense in depth 통합 필요 | ✅ 영역 외 답습 (MVP-2 이후) |

### 6.5 합산 채택

| 분류 | trigger 수 | 본 합의 채택 |
|------|---------|----------|
| R-7 직접 영향 | 2 | ✅ 의존성 enumerate 한정 (발화 0건) |
| R-7 간접 영향 (Layer E 영역) | 1 | ✅ 영역 외 답습 |
| R-7 영향 0 (Phase α-1/α-2/T3/MVP-3/MVP-6/Backlog 분리) | 15 | ✅ 영역 외 답습 |
| **합산 (Layer B 18 trigger)** | **18 trigger** | ✅ **본문 확정 답습 + 발화 0건** |
| **추가: ST-1/2/4/5 별도 backlog trigger** | **4** | ✅ **분리 명시 답습** |

---

## 7. 실 R-7 docker secret block 수정 진입 아직 아님 (답습 명시)

### 7.1 본 합의 발효 후 영역 *내* vs *외*

| 영역 | 본 합의 발효 후 *영역 내* | 본 합의 발효 후 *영역 외* (별도 합의 / 사용자 명시 결정) |
|------|-------------------|-----------------------|
| Brief 본문 채택 권고 | ✅ APPROVE AS BRIEF | — |
| R-7 영역 9 artifacts × 328줄 답습 채택 | ✅ APPROVE AS BRIEF | — |
| ST-3 단독 답습 채택 (ST-1/2/4/5 분리) | ✅ APPROVE AS BRIEF | — |
| 적격성 5/5 충족 검증 | ✅ APPROVE AS BRIEF | — |
| 12/12 풀 3+1 트리거 0건 발화 검증 | ✅ APPROVE AS BRIEF | — |
| 18 + 4 Rollback Trigger 분류 채택 | ✅ APPROVE AS BRIEF | — |
| Phase α-3 실 진입 | ❌ | Backlog #6 실 진입 + 사용자 명시 결정 영역 |
| R-7 영역 9 artifacts 본문 변경 | ❌ | 동상 |
| `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 변경 | ❌ | Phase α-4 영역 (R-1) |
| Production `docker-compose.yml` 신설 / 변경 | ❌ | PoC 격리 디렉토리 한정 답습 (별도 합의) |
| Hermes upstream Dockerfile 변경 | ❌ | Backlog #1 1.5차 보강 영역 (풀 3+1 합의) |
| R-4 도구 본문 변경 | ❌ | Phase α-1 영역 (`1b3090b` 합의 답습) |
| R-5 `.importlinter` 본문 변경 | ❌ | Phase α-2 영역 (`6a79247` 합의 답습) |
| R-1 CI workflow 통합 | ❌ | Phase α-4 영역 |
| R-6 / R-10 / R-2 / branch protection | ❌ | Phase β 영역 (5 금지 #1 #2 #3 해소 의존) |
| commit signing / Vault HSM / Layer E / Layer F | ❌ | Phase γ 영역 (MVP-6) |
| ST-1 / ST-2 / ST-4 / ST-5 진입 | ❌ | Backlog #1 1.5차 보강 / Backlog #7 / MVP-2 이후 영역 |
| 7 금지 영역 해소 | ❌ | 별도 합의 + 사용자 명시 결정 영역 |
| Layer C 발효 합의 | ❌ | ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 |
| Layer D MVP-1 PASS 선언 | ❌ | Layer C 발효 후 별도 합의 |
| Layer E Operational Readiness PASS | ❌ | MVP-6 영역 |
| Layer F Hermes PMO 격상 | ❌ | ADR-008 부록 C 12 조건 + 별도 풀 3+1 + 외부 LLM 2+ + 인간 리뷰 의무 영역 |

### 7.2 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

1. Phase α-4 R-1 CI workflow 통합 brief
2. Phase α 4 단계 (α-1 + α-2 + α-3 + α-4) 통합 진입 brief
3. Phase α-3 실 R-7 docker secret block 운영 단계 분할 brief
4. Phase α-1 ~ α-3 병렬 실제 구현 계획 brief
5. Phase α-1 R-4 실 진입 step 분할 brief
6. Phase α-2 실 `.importlinter` 수정 step 분할 brief
7. Group α 조건 재평가 (C-1 ~ C-12 영역)
8. Group I (Hermes-originated commit auto-reject) 별도 합의 진입 brief
9. token rotation 정책 별도 합의 진입 brief (Group α C-3 답습)
10. GitHub plan / ruleset 가용성 확인 단계 진입 (Group α C-4 답습)
11. 세션 종료

---

## 8. 최종 판정 + Conditions

### 8.1 종합 판정

| 영역 | 판정 |
|------|----|
| **종합 판정** | **APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격) |
| 합의 단위 | brief 본문 채택 — 수단 결정 적격성 권위 권고 |
| 합의 형태 | (가) Reviewer-only 단축 합의 (12/12 풀 3+1 트리거 0건 발화) |
| 외부 LLM 응답 결론 강제 채택 | ❌ 0건 (응답 = 입력 한정 — Group α C-11 답습) |

### 8.2 본 합의 조건 (Conditions, 답습 한정)

| # | 조건 | 출처 |
|---|------|----|
| C-δ-1 | Group α 합의 C-1 ~ C-12 *변경 0건* | 본 합의 §4 답습 |
| C-δ-2 | Backlog #6 우선 진입 합의 11 조건 (C-α-1 ~ C-α-11) *변경 0건* | 본 합의 §4 답습 |
| C-δ-3 | Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) *변경 0건* | 본 합의 §4 답습 |
| C-δ-4 | Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) *변경 0건* | 본 합의 §4 답습 |
| C-δ-5 | GP-3 Stage 2 합의 본문 *변경 0건* | 본 합의 §1 답습 |
| C-δ-6 | GP-3 MVP-1 진입 합의 (`6dc5bdc`) *변경 0건* (ST-3 단독 채택 권위 권고 답습) | 본 합의 §1 답습 |
| C-δ-7 | 사용자 명시 7 금지 영역 (실 R-7 docker secret block 수정 / CI workflow 변경 / branch protection / dev 환경 강제 / `pre-commit install` 의무화 / Operational Readiness PASS / Hermes PMO 격상) *해소 0건* | 본 합의 §0.1 답습 |
| C-δ-8 | Phase α-3 실 진입 = **Backlog #6 + 사용자 명시 결정 영역** (자동 진입 0건) | 본 합의 §7.1 답습 |
| C-δ-9 | R-7 영역 9 artifacts × 328줄 본문 어느 줄도 *변경 0건* | 본 합의 §2.1 답습 |
| C-δ-10 | ST-3 단독 답습 *변경 0건* — ST-1 / ST-2 / ST-4 / ST-5 흡수 0건 | 본 합의 §3 답습 |
| C-δ-11 | ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 답습 — Hermes upstream Dockerfile 변경 *0건* | 본 합의 §1.1 답습 |
| C-δ-12 | Production `docker-compose.yml` 신설 / 변경 *0건* (PoC 격리 디렉토리 한정 답습) | 본 합의 §0.3 답습 |
| C-δ-13 | `secret-hygiene-egress-redaction.yml` Stage 2 entry step 본문 *변경 0건* (R-1 영역 = Phase α-4) | 본 합의 §0.3 답습 |
| C-δ-14 | 실 secret material commit *0건* + `secrets/.gitignore` *변경 0건* + secret marker 위반 *0건* (FAKE_TEST_SECRET marker 답습) | 본 합의 §0.3 답습 |
| C-δ-15 | R-4 도구 본문 / R-5 `.importlinter` 본문 / R-1 CI workflow 어느 영역도 *변경 0건* | 본 합의 §7.1 답습 |
| C-δ-16 | Layer A / Layer B / §5.5.1 GP-3 4 sub-수단 본문 채택 *변경 0건* | 본 합의 §1.3 답습 |
| C-δ-17 | Layer C 발효 = ADR-011 §2.1 (a)~(e) 5/5 evidence + 사용자 명시 결정 영역 | 본 합의 §7 답습 |
| C-δ-18 | Phase α-1 / α-2 / α-4 / β / γ *자동 진입 0건* | 본 합의 §7.1 답습 |
| C-δ-19 | Group I / Group β / γ-1 / γ-2 *자동 진입 0건* | 본 합의 §0.3 답습 |
| C-δ-20 | token rotation 정책 / GitHub plan 가용성 *자동 결정 0건* (Group α C-3 + C-4 답습) | 본 합의 §0.3 답습 |
| C-δ-21 | R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) trigger *자동 발화 0건* | 본 합의 §6.1 답습 |
| C-δ-22 | inotify sidecar (`tools/docker_secret_inotify_sidecar_check.sh` 258줄) 본 영역 흡수 *0건* (Backlog #1 분리) | 본 합의 §3 답습 |
| C-δ-23 | ST-4 Vault HSM 진입 *0건* (Backlog #7 분리, MVP-6 이후) | 본 합의 §3 답습 |
| C-δ-24 | G3-7 row 4 항목 자동 흡수 *0건* (Stage 5 별도 영역 분리) | 본 합의 §0.3 답습 |
| C-δ-25 | 외부 LLM *응답 결론 강제 채택 0건* (응답 = 입력 한정 — Group α C-11 답습) | 본 합의 §8.1 답습 |
| C-δ-26 | 5 영구 핵심 제약 (Hermes ≠ root of trust / 단일 source-of-truth / 수단/목적 분리 / T1/T2/T3 분리 / SPOF 의도적 수용) **5/5 보존** | 본 합의 §4 답습 |
| C-δ-27 | Provider Liquidity 5-way **100% 보존** (R-7 = file-system secret isolation Layer = catalog / provider 영역과 직교) | 본 합의 §4 답습 |
| C-δ-28 | 본 합의 = **수단 결정 적격성 권위 권고 한정** + 실 진입 = 별도 사용자 명시 결정 영역 | 본 합의 §7 답습 |

**합산**: **28 조건 (C-δ-1 ~ C-δ-28) 충족 시 = 본 합의 진입 적합** + 본 합의 = "수단 결정 적격성 권위 권고 발행" 한정 (실 적용 = Backlog #6 + 사용자 명시 결정 영역).

---

## 9. 변경 0건 / 진입 0건 검증

### 9.1 본 합의 발효 시점 변경 0건 영역

| 영역 | 변경 |
|------|----|
| `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` (34줄) | 0건 |
| `docker/gp3-st3-poc/Dockerfile` (12줄) | 0건 |
| `docker/gp3-st3-poc/app.py` (46줄) | 0건 |
| `docker/gp3-st3-poc/secrets/api_key.placeholder` (1줄) | 0건 (FAKE_TEST_SECRET marker 답습) |
| `tools/docker_secret_image_layer_check.sh` (99줄) | 0건 |
| `tools/docker_secret_restart_recovery.sh` (118줄) | 0건 |
| `tools/docker_secret_inotify_sidecar_check.sh` (258줄, Backlog #1 분리 영역) | 0건 |
| `tests/fixtures/gp3_st3/pass/Dockerfile` (9줄) | 0건 |
| `tests/fixtures/gp3_st3/fail/Dockerfile` (8줄) | 0건 |
| `tests/fixtures/gp3_st3/fail/baked_secret.txt` (1줄) | 0건 |
| `secret-hygiene-egress-redaction.yml` Stage 2 entry step | 0건 |
| Production `docker-compose.yml` | 0건 (PoC 격리 디렉토리 한정 답습) |
| Hermes upstream Dockerfile | 0건 (ADR-008 차단조건 #6 + 부록 B 답습) |
| `secrets/.gitignore` (placeholder 한정) | 0건 |
| R-4 도구 (`secret_scanner.py` 368 / `provider_import_scanner.py` 178 / `provider_url_scanner.py` 283) | 0건 |
| `/.importlinter` 본문 (35줄) | 0건 |
| `/.github/workflows/*.yml` | 0건 |
| `requirements*.txt` | 0건 |
| `src/adapters/llm/facade.py` | 0건 |
| Phase α-1 합의 (`1b3090b`) 본문 | 0건 |
| Phase α-2 합의 (`6a79247`) 본문 | 0건 |
| Backlog #6 우선 진입 합의 (`c7ddfdd`) 본문 | 0건 |
| Group α 합의 (`4880e88`) 본문 | 0건 |
| GP-3 MVP-1 진입 합의 (`6dc5bdc`) 본문 | 0건 |
| GP-3 Stage 2 합의 본문 | 0건 |
| Layer A (`f1e0b23`) 본문 | 0건 |
| Layer B (`f40423f`) 본문 | 0건 |
| Layer D (`210c98f`) 본문 | 0건 |
| `implementation-runtime-roadmap-mvp1.md` §5.5.1 ST-3 본문 채택 | 0건 |
| ADR-008 ~ ADR-012 본문 | 0건 (cross-reference 답습 한정) |
| `.pre-commit-config.yaml` 본문 | 0건 |
| GitHub branch protection rule / Actions secrets / permissions | 0건 |

### 9.2 본 합의 발효 시점 진입 0건 영역

| 영역 | 진입 |
|------|----|
| Phase α-3 실 진입 (R-7 docker secret block 본문 변경) | 0건 |
| Phase α-1 / α-2 / α-4 자동 진입 | 0건 |
| Phase β / γ 자동 진입 | 0건 |
| Backlog #6 실 진입 | 0건 |
| ST-1 / ST-2 / ST-4 / ST-5 자동 진입 | 0건 |
| R-MVP1-G3-3 (ST-3 도입 실패) 자동 발화 | 0건 |
| 7 금지 영역 해소 | 0건 |
| Layer C 발효 (Implementation Evidence PASS) | 0건 |
| Layer D 발효 (MVP-1 PASS) | 0건 |
| Layer E 발효 (Operational Readiness PASS) | 0건 |
| Layer F 발효 (Hermes PMO 격상) | 0건 |
| Group I / Group β / γ-1 / γ-2 | 0건 |
| Backlog #1 / #2 / #4 / #5 / #7 | 0건 |
| MVP-2 ~ MVP-6 본문 deepening | 0건 |
| 17 항목 우선순위 자동 *재고정* | 0건 |
| 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| event enum 정식 등록 (`docker_secret_isolation_layer1_implementation` = Backlog #5 분리) | 0건 |
| 외부 LLM 자동 호출 | 0건 |
| 외부 LLM 응답 결론 강제 채택 | 0건 |
| 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 실 secret material commit | 0건 |
| `secrets/.gitignore` 변경 | 0건 |
| 인간 리뷰 의무 자동 발화 | 0건 |
| token rotation 정책 자동 결정 | 0건 |
| GitHub plan / ruleset 가용성 자동 확인 | 0건 |
| commit signing 도입 | 0건 |
| `pull_request_target` workflow 도입 | 0건 |
| Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| threshold *고정* | 0건 (모두 *후보 한정* 유지) |
| MVP-1 PASS 재선언 | 0건 |
| GP-3 / GP-5 PASS 발효 | 0건 |
| ADR 본문 자동 갱신 | 0건 |
| Layer 2 runtime block (G5-5) 진입 | 0건 |
| 실 docker build / docker run / docker history 자동 실행 | 0건 |

---

## 10. 본 합의 요약 (한 단락)

본 합의는 **`docs/phase0/phase-alpha-3-r7-docker-secret-block-entry-brief.md` (DRAFT, commit `8da3273`, 748줄) 의 Reviewer-only 단축 합의 보고서** 다. 사용자 명시 진입 명령 ("옵션 A로 진행해주세요") + Phase α-1 / α-2 패턴 답습 (brief commit → Reviewer-only 단축 합의 보고서 작성 → 메타 갱신 → push. 실 R-7 docker secret block 수정은 아직 하지 않음). **판정 = APPROVE AS BRIEF** (Reviewer-only 단축 합의 적격 — **12/12 풀 3+1 트리거 0건 발화** 확인). 본 합의 = **Backlog #6 우선 진입 합의 §6.1 1순위 (Phase α-1 + α-2 + α-3 병렬) 中 Phase α-3 답습** + **R-7 = docker secret block 본문 정의 채택 권고** (9 artifacts × 328줄 답습 — `docker/gp3-st3-poc/docker-compose.gp3-st3.yml` 34줄 + `Dockerfile` 12줄 + `app.py` 46줄 + `secrets/api_key.placeholder` 1줄 = sub-step 2.1 / `tools/docker_secret_image_layer_check.sh` 99줄 = sub-step 2.2 / `tools/docker_secret_restart_recovery.sh` 118줄 = sub-step 2.3 / `tests/fixtures/gp3_st3/pass/Dockerfile` 9줄 + `fail/Dockerfile` 8줄 + `fail/baked_secret.txt` 1줄 = sub-step 2.2 — 본문 변경 0건) + **ST-3 단독 답습 채택** (ST-1 entrypoint stat / ST-2 inotify sidecar 258줄 = Backlog #1 분리 / ST-4 Vault HSM = Backlog #7 + MVP-6 이후 분리 / ST-5 Defense in depth = MVP-2 이후 분리) + **Layer B §5.5.1 GP-3 4 sub-수단 中 ST-3 답습** (S-1 = R-4 영역 / PC-3 + AR-1 = Stage 4 영역 분리) + **9 sub-step 분할 매트릭스 채택 권고** + **5/5 진입 적격성 5 조건 (C-α3-1 ~ C-α3-5) 충족 검증** + **12/12 풀 3+1 트리거 0건 발화 검증** + **18 + 4 Rollback Trigger 분류 채택** (R-7 직접 영향 2 + 간접 영향 1 + 영향 0 15 + ST-1/2/4/5 별도 backlog 4 trigger 분리) + **28 합의 조건 (C-δ-1 ~ C-δ-28)** 답습. **사용자 명시 7 금지 7/7 답습** (실 R-7 docker secret block 수정 0건 / CI workflow 변경 0건 / branch protection 변경 0건 / dev 환경 강제 0건 / `pre-commit install` 의무화 0건 / Operational Readiness PASS 0건 / Hermes PMO 격상 0건) + **5 영구 핵심 제약 5/5 보존** + **Provider Liquidity 5-way 100% 보존** (R-7 = file-system secret isolation Layer = catalog / provider 영역과 직교, docker secret = vendor-agnostic 표준) + **ADR-008 차단조건 #6 + 부록 B + §A.2 R1-2 답습 — Hermes upstream Dockerfile 변경 0건** + **Group α 합의 본문 변경 0건** + **Backlog #6 우선 진입 합의 본문 변경 0건** + **Phase α-1 합의 본문 변경 0건** + **Phase α-2 합의 본문 변경 0건** + **GP-3 Stage 2 합의 본문 변경 0건** + **GP-3 MVP-1 진입 합의 본문 변경 0건** + **Layer A / Layer B / §5.5.1 ST-3 본문 채택 변경 0건** + **R-7 영역 9 artifacts × 328줄 어느 줄도 변경 0건** (PoC 답습 100% 보존) + **Production `docker-compose.yml` / `secrets/.gitignore` / R-4 도구 / R-5 `.importlinter` / R-1 CI workflow / `.pre-commit-config.yaml` 변경 0건** + **ST-3 = ST-1 / ST-2 / ST-4 / ST-5 흡수 0건** + **inotify sidecar (258줄) 본 영역 흡수 0건** + **실 secret material commit 0건** + **R-MVP1-G3-3 자동 발화 0건** + **G3-7 자동 흡수 0건** + **외부 LLM 자동 호출 0건** + **외부 LLM 응답 결론 강제 채택 0건** + **Phase α-3 실 진입 0건** + **Phase α-1 / α-2 / α-4 / β / γ 자동 진입 0건** + **7 금지 영역 *해소* 0건** + **Layer C / D / E / F 발효 0건** + **Group I / β / γ-1 / γ-2 자동 진입 0건** + **자동 진입 모두 0건**. 다음 단계 = **사용자 결정 영역** (자동 진입 0건): (1) Phase α-4 R-1 CI workflow 통합 brief / (2) Phase α 4 단계 통합 진입 brief / (3) Phase α-3 실 R-7 운영 단계 분할 brief / (4) Phase α-1 ~ α-3 병렬 실제 구현 계획 brief / (5) Phase α-1 R-4 / Phase α-2 R-5 실 진입 step 분할 brief / (6) Group α 조건 재평가 / (7) Group I 별도 합의 / (8) token rotation 정책 별도 합의 / (9) GitHub plan 가용성 확인 / (10) 세션 종료.

---

**작성일**: 2026-05-14 후속 13
**상태**: APPROVE AS BRIEF (Reviewer-only 단축 합의 적격)
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
**금지 (사용자 명시 답습 — 본 합의 영역)**:
- ❌ **실 R-7 docker secret block 수정** (사용자 명시 7 금지 #1)
- ❌ **CI workflow 변경** (사용자 명시 7 금지 #2)
- ❌ **branch protection 변경** (사용자 명시 7 금지 #3)
- ❌ **dev 환경 강제** (사용자 명시 7 금지 #4)
- ❌ **`pre-commit install` 의무화 도입** (사용자 명시 7 금지 #5)
- ❌ **Operational Readiness PASS (Layer E) 선언** (사용자 명시 7 금지 #6)
- ❌ **Hermes PMO 격상 (Layer F)** (사용자 명시 7 금지 #7)
- ❌ R-7 영역 9 artifacts × 328줄 어느 줄도 변경
- ❌ Production `docker-compose.yml` 신설 / 변경 (PoC 격리 디렉토리 한정 답습)
- ❌ Hermes upstream Dockerfile 변경 (ADR-008 차단조건 #6 + 부록 B 답습)
- ❌ 실 secret material commit (FAKE_TEST_SECRET marker 답습)
- ❌ `secrets/.gitignore` 변경 (placeholder 한정 영구 답습)
- ❌ secret material marker 위반 (실 vendor prefix 사용 금지)
- ❌ R-4 도구 본문 변경
- ❌ R-5 `.importlinter` 본문 변경
- ❌ R-1 CI workflow 변경
- ❌ Phase α-3 실 진입 자동 진입 금지
- ❌ Phase α-1 / α-2 / α-4 자동 진입 금지
- ❌ Phase β / γ 자동 진입 금지
- ❌ Implementation Evidence PASS (Layer C) 발효
- ❌ ST-3 = ST-1 / ST-2 / ST-4 / ST-5 흡수 시도 (단독 답습)
- ❌ ST-4 Vault HSM 진입 (Backlog #7 분리)
- ❌ inotify sidecar (`tools/docker_secret_inotify_sidecar_check.sh` 258줄) 본 영역 흡수
- ❌ R-MVP1-G3-3 (ST-3 Docker secret 도입 실패) 자동 발화
- ❌ G3-7 row 4 항목 자동 흡수 (Stage 5 분리)
- ❌ Layer B §5.5.1 GP-3 4 sub-수단 본문 채택 변경
- ❌ GP-3 Stage 2 합의 본문 변경
- ❌ GP-3 MVP-1 진입 합의 본문 변경
- ❌ Group α 합의 C-1 ~ C-12 자동 변경
- ❌ Backlog #6 우선 진입 합의 11 조건 자동 변경
- ❌ Phase α-1 합의 15 조건 (C-β-1 ~ C-β-15) 자동 변경
- ❌ Phase α-2 합의 26 조건 (C-γ-1 ~ C-γ-26) 자동 변경
- ❌ §5.5 9 sub-수단 본문 채택 변경
- ❌ Group I / Group β / γ-1 / γ-2 자동 진입
- ❌ token rotation 정책 자동 결정
- ❌ commit signing 도입
- ❌ `pull_request_target` workflow 도입
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ threshold 자동 고정
- ❌ ADR 본문 자동 갱신
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ 외부 LLM 자동 호출
- ❌ 외부 LLM 응답 결론 강제 채택 (응답 = 입력 한정)
- ❌ 실 API key / provider SDK / 외부 API 호출
- ❌ 실 docker build / docker run / docker history 자동 실행
- ❌ 인간 리뷰 의무 자동 발화
- ❌ Backlog #1 / #2 / #4 / #5 / #7 자동 진입
- ❌ Layer 2 runtime block (G5-5) 진입 (MVP-3/4 분리)
- ❌ 17 항목 우선순위 자동 *재고정*
- ❌ MVP-2 ~ MVP-6 본문 deepening
- ❌ `src/adapters/llm/facade.py` real 본문 작성 (Backlog #4 분리)
- ❌ event enum 정식 등록 (`docker_secret_isolation_layer1_implementation` = Backlog #5 분리)
