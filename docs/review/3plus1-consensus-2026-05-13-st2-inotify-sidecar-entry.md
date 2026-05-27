# Backlog #1 ST-2 inotify sidecar 단독 우선 진입 합의 보고서 (Reviewer-only 단축 합의)

**합의 형태**: **단축 합의 (Reviewer-only)** — 사용자 명시 결정 답습 (옵션 (A) brief 그대로 승인 + 4 결정 명시: F-B 우선 / F-C 보조 / F-A 비채택 / Multi-host 미요구 / `/run/secrets/*` / secret rotation 별도 합의)
**합의 일자**: 2026-05-13 후속 25
**검토 대상**: **Backlog #1 ST-2 (inotify sidecar) *단독 우선* 진입 적격성** — fail-closed = F-B 우선 채택 + Multi-host parity 미요구 + `/run/secrets/*` 감시 경로 + runtime secret 변경 fail-closed + secret rotation 별도 합의 분리 + T3 자동 진입 0건 적절성
**보조 참조**:
- 본 합의 대상 brief = `docs/phase0/backlog1-st2-inotify-sidecar-brief.md` (commit `d9ae98b`, DRAFT 12 섹션)
- Backlog #1 진입 *직전* 사전 정비 합의 = `docs/review/3plus1-consensus-2026-05-13-backlog1-gp3-1.5-deepening.md` (commit `43b898c`, APPROVE AS BRIEF — ST-2 = T2 + 단독 우선 진입 후보 권위 확정)
- Backlog #1 brief = `docs/phase0/backlog1-gp3-1.5-deepening-brief.md` (commit `6b15070`)
- MVP-1 PASS (Layer D) 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` (commit `210c98f`, APPROVE WITH CONDITIONS, §C-5 GP-3 1.5차 보강 Backlog #1 Deferred)
- §C-1 충족 갱신 합의 = `docs/review/3plus1-consensus-2026-05-13-mvp1-pass-c1-k2-satisfaction.md` (commit `1dd1036`)
- MVP-1 deepening roadmap = `docs/architecture/implementation-runtime-roadmap-mvp1.md` §3.3 (ST-1~ST-5) + §3.4.2 + §3.5 + §3.6.3
- Governance preconditions = `docs/architecture/governance-preconditions.md` §5.3 + §5.4
- ADR-008 차단조건 #1 (SQLCipher) + #6 (Docker 격리) + 부록 B + ADR-010 + ADR-011 (저장 경로 secret 보호 + docker secret 권위, 37번째 entry R-S1 정정 답습)
- ADR-011 §2.4 (T1/T2/T3 분류)

**검토 목적**: Backlog #1 ST-2 *단독 우선* 진입 적격성 + 4 결정 답습 적절성 확정. **본 합의 = ST-2 진입 적격성 권위 확정 한정 ≠ ST-2 실 구현 / docker-compose 변경 / CI workflow / hook 추가 / 다른 backlog 자동 진입 / MVP-1 PASS 재선언 / Operational Readiness PASS / Hermes PMO 격상 / §C-5 Satisfied 자동 갱신**.

**판정**: ✅ **APPROVE — Backlog #1 ST-2 (inotify sidecar) 단독 우선 진입 적격성 권위 확정 (Reviewer-only 단축 합의, 사용자 명시 4 결정 답습)**

⚠️ **본 합의 = ST-2 진입 *적격성* 확정 한정** — ST-2 실 구현 0건 + sidecar Dockerfile / inotify 스크립트 / docker-compose 변경 0건 + CI workflow / hook 추가 0건 + 다른 backlog 자동 진입 0건.

⚠️ **본 합의 ≠ MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 / §C-5 *Satisfied* 자동 갱신** — 모두 그대로 유지.

---

## 0. 사전 점검

### 0.1 가동 사유

사용자 명시 진입 명령 답습 (2026-05-13 후속 25):

> "옵션 (A)로 진행해주세요. 본 텍스트 brief를 그대로 승인하고, 파일화한 뒤 Reviewer-only 단축 합의 보고서 작성 단계로 진입하겠습니다."

> "1. fail-closed 메커니즘: F-B 우선 채택 / 2. F-C: 보조 후보로 유지 / 3. F-A: 비채택 / 4. Multi-host parity: 이번 ST-2 단독 진입 범위에서는 미요구"

**사용자 명시 4 결정 답습**:
1. fail-closed = **F-B 우선** (status file → Hermes healthcheck unhealthy) / F-C 보조 / **F-A 비채택** (docker socket 권한 영역 회피)
2. Multi-host parity = **미요구** (MVP-1 단일 host 한정)
3. inotify 감시 경로 = **`/run/secrets/*`** (ADR-008 차단조건 #6 + 부록 B (37번째 entry R-S1 정정 답습) docker secret 답습)
4. secret rotation 정책 = **별도 합의 영역 분리** (runtime 변경 = fail-closed)

### 0.2 단축 채택 사유

| 조건 | 충족 |
|-----|------|
| 새 *권위 결정* 0건 (본 합의 = brief §2~§10 답습 한정 — 새 권위 도입 0건 + Layer D 본문 변경 0건 + §5.5 9 sub-수단 본문 채택 변경 0건 + C-1~C-8 상태 변경 0건 + ADR 본문 갱신 0건) | ✅ |
| 직전 합의 chain (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 모두 Reviewer-only) 패턴 답습 | ✅ |
| brief §10.3 본문 명시 답습 — "**합의 형태 = Reviewer-only 단축 합의 적격 확정** (사용자 명시 4 결정 답습 후)" | ✅ |
| ADR-011 §2.4 T2 분류 (사용자 승인 기반 — 새 도구 등록 영역, T1 deterministic 0 + T3 영역 침범 0) | ✅ |
| 사용자 명시 결정으로 단축 합의 형태 채택 (옵션 (A) + 4 결정 명시) | ✅ §0.1 답습 |
| **7/7 풀 3+1 승격 트리거 0건 발화** | ✅ §2 답습 |
| Backlog #1 진입 직전 정비 합의 (`43b898c`) 답습 — ST-2 = T2 + 단독 우선 진입 후보 권위 확정 | ✅ |
| 사용자 명시 4 결정 brief 반영 (§7 F-B / §3 Multi-host 미요구 / §5 `/run/secrets/*` / §6.2 secret rotation 분리) | ✅ |

### 0.3 메타 편향 인지

본 Reviewer = Claude Opus 4.7 메인 컨텍스트 = Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / ST-2 brief 작성자. 자기 작성 권위 누적 자기 검토 한계 인지.

**청산 매커니즘**:
1. **사후 외부 LLM 충족 보존** — 누적 cross-vendor blind 의뢰 5건 답습 (Stage 5 entry / Layer C / Layer D / Backlog #5 / K-2 fix 권위 chain) — 모두 권위 *내부* 작업으로 통합
2. **격상 전 면제 보존** — Hermes PMO 격상 *전 단계*. 본 검토 = ST-2 진입 *적격성* 확정 한정 — Layer E / Layer F 미진입
3. **합의 권위 내부 변경 한정** — 본 검토 = brief §2~§10 + 사용자 명시 4 결정 답습 한정 — 새 권위 결정 0건 (Layer D / Backlog #5 / K-2 fix / Backlog #1 진입 직전 정비 답습)
4. **자기 작성 한계 명시** — 본 §0.3 + §4 명시
5. **ST-2 자체 구현 ≠ 본 합의 범위** (사용자 명시 답습) — sidecar Dockerfile / inotify 스크립트 / docker-compose 변경 0건 + 진입 발효 시점 별도 commit + 사용자 명시 결정 의무
6. **T3 자동 진입 0건 보존** — brief §2.3 + §10.1 답습 — Hermes upstream / Vault HSM / Tier-2-3 catalog / branch protection / docker socket 접근 모두 자동 진입 0건
7. **외부 LLM cross-vendor blind 의뢰 미진입** — 7/7 단축 합의 적격 트리거 0건 발화 + 직전 합의 chain 일관성

### 0.4 비검토 대상 (사용자 명시 답습)

| 항목 | 본 검토 범위 |
|-----|----------|
| **ST-2 *실 구현*** | ❌ (사용자 명시 답습 — 본 합의 = 진입 *적격성* 확정 한정) |
| **sidecar Dockerfile / inotify 스크립트 / docker-compose 변경** | ❌ (구현 발효 시점 별도 commit + 사용자 명시 결정 의무) |
| **CI workflow / hook 변경** | ❌ (구현 발효 시점 별도 commit) |
| **ST-1 *자동 진입*** | ❌ (T3 영역 — Backlog #3 별도 풀 3+1 합의 + 외부 LLM 1+ 의무) |
| **PC-4 *자동 진입*** | ❌ (T2 sub + T3 sub 모두 — Backlog #1 + #2 1.5차 분리) |
| **ST-4 (Vault HSM) *자동 진입*** | ❌ (Operational Readiness 영역 — Backlog #7) |
| **Multi-host parity *자동 진입*** | ❌ (사용자 #2 결정 답습 — 본 ST-2 단독 진입 범위 외) |
| **T3 영역 *자동 진입*** | ❌ (사용자 명시 답습 + ADR-011 §2.4) |
| **MVP-1 PASS *재선언*** | ❌ (Layer D `210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| Operational Readiness PASS *선언* (Layer E) | ❌ (MVP-6 영역 — Backlog #7) |
| Hermes PMO 격상 *선언* (Layer F) | ❌ (MVP-6 영역 — 외부 LLM + 사람 리뷰 의무) |
| §C-5 *Satisfied 자동 갱신* | ❌ (본 합의 발효 후에도 §C-5 = Deferred 유지) |
| C-2~C-4, C-6~C-8 *자동 변경* | ❌ (다른 7 Conditions 그대로 유지) |
| §5.5 9 sub-수단 본문 채택 *변경* | ❌ (`f40423f` + `55c5b4b` 답습) |
| ADR 본문 *자동 갱신* | ❌ (cross-reference 답습 한정) |
| 다른 backlog (#2/#3/#4/#7) *자동 진입* | ❌ |
| 사용자 명시 4 결정 *재변경* | ❌ (본 합의 = 4 결정 답습 한정) |
| Tier-2/3 catalog 자동 확장 | ❌ |
| Hermes upstream 변경 / 외부 LLM 자동 호출 | ❌ |
| 실 API key / provider SDK / 외부 API 호출 | ❌ |

---

## 1. 검토 기준 충족 분석 (9/9 적절)

### 1.0 사용자 명시 9 검토 기준 답습

사용자 명시 검토 기준 (2026-05-13 후속 25):

1. ST-2가 T2 영역인지
2. Hermes upstream 변경이 0건인지
3. F-B 우선 채택이 적절한지
4. F-A 비채택이 적절한지
5. Multi-host parity 미요구가 적절한지
6. `/run/secrets/*` 감시 경로가 적절한지
7. runtime secret 변경 fail-closed 처리가 적절한지
8. secret rotation 정책을 별도 합의로 분리했는지
9. T3 자동 진입이 발생하지 않았는지

### 1.1 검토 기준 #1 — ST-2가 T2 영역인지

**brief §2 답습**:

| 영역 | 검증 |
|------|------|
| ADR-011 §2.4 T2 정의 답습 | "사용자 승인 필수 — Skill/Memory promotion, 새 도구 등록, 합의 형태 결정" → sidecar 추가 = 새 도구 등록 |
| mvp1.md §3.3.1 본문 직접 답습 | "Hermes upstream 변경 = ❌ (sidecar 분리 가능)" + "sidecar 가능성 = ✅" |
| T3 침범 6/6 0건 (brief §2.3) | Hermes upstream Dockerfile / Constitution·ADR·Harness Gates 정의 / Branch protection / Tier-2-3 catalog / Vault HSM (ST-4) / docker socket 접근 모두 0건 |
| mvp1.md §3.3.2 MVP-1 1.5차 보강 권고 답습 | "ST-3 + **ST-2 inotify sidecar** (Hermes upstream 변경 회피 유지)" |
| Backlog #1 진입 직전 정비 합의 (`43b898c`) §1.2 + §1.5 권위 답습 | ST-2 = T2 + 단독 우선 진입 후보 권위 확정 |

**판정**: ✅ **적절** — ST-2 = T2 영역 (ADR-011 §2.4 + mvp1.md §3.3 + Backlog #1 진입 직전 정비 합의 답습 일관성). brief §2 분류 권위 근거 충실.

### 1.2 검토 기준 #2 — Hermes upstream 변경이 0건인지

**brief §3 답습**:

| 변경 후보 | 본 sidecar | F-B 채택 시 영향 |
|---------|----------|---------------|
| Hermes Dockerfile entrypoint script 본문 | ❌ 0건 | ❌ 0건 |
| Hermes Dockerfile base image | ❌ 0건 | ❌ 0건 |
| Hermes Dockerfile CMD / ENTRYPOINT 본문 | ❌ 0건 | ❌ 0건 |
| Hermes 환경 변수 / volume mount | ❌ 0건 (sidecar = 별도 mount) | ❌ 0건 |
| Hermes 권한 (capability / user / privileged) | ❌ 0건 | ❌ 0건 |
| Hermes upstream PR 제출 | ❌ 0건 | ❌ 0건 |
| Hermes healthcheck *정의* (docker-compose level) | ⚠️ 추가 가능 | ✅ docker-compose level (repo-local 영역, **Hermes upstream Dockerfile 본문 0건 보존**) |

**검증**:

- F-B 메커니즘 = sidecar status file write + Hermes healthcheck (docker-compose level) read → Hermes upstream Dockerfile *본문* 변경 0건
- docker-compose level healthcheck = repo-local 영역 (T2 보존)
- mvp1.md §3.3.2 "Hermes upstream 변경 회피 유지" 답습 충실

**판정**: ✅ **적절** — Hermes upstream Dockerfile / image / PR / config 영역 변경 0건. docker-compose level healthcheck 추가 = repo-local 영역 (T2 보존). brief §3 검증 권위 근거 충실.

### 1.3 검토 기준 #3 — F-B 우선 채택이 적절한지

**brief §7 + 사용자 #1 결정 답습**:

**F-B 메커니즘**: sidecar → status file 기록 (`/var/run/sidecar-status`) → Hermes healthcheck (docker-compose level) 가 해당 파일 read → unhealthy 처리.

| F-B 채택 사유 | 검증 |
|------------|------|
| docker socket 접근 0건 | ✅ (sidecar = volume write 한정) |
| 권한 부담 低 | ✅ (sidecar = non-root + cap drop ALL 권고) |
| T2 영역 유지 | ✅ (T3 영역 침범 0건) |
| Hermes upstream Dockerfile 변경 0건 | ✅ (§3 답습 — docker-compose level healthcheck) |
| T3 자동 진입 위험 0건 | ✅ (6 escalation trigger #5 발화 0건, brief §10.1 답습) |
| 운영 정책 변경 영역 침범 0건 | ✅ (사용자 명시 답습 — F-A 비채택 함의) |

**판정**: ✅ **적절** — F-B = 권한 부담 低 + T2 영역 유지 + Hermes upstream 0건 + T3 자동 진입 위험 0건 (brief §7.2 답습). 사용자 명시 #1 결정 답습 충실.

### 1.4 검토 기준 #4 — F-A 비채택이 적절한지

**brief §7.3 + 사용자 #1 결정 답습**:

**F-A 메커니즘**: sidecar → `docker stop <hermes-container>` via docker socket mount.

| F-A 비채택 사유 | 검증 |
|------------|------|
| docker socket 접근 = root-equivalent | ✅ (docker socket = host docker daemon 직접 통제 권한) |
| 권한 영역 확대 | ✅ (sidecar 가 다른 container 정지 가능 = cross-container 통제) |
| T3 가능성 高 | ✅ (ADR-011 §2.4 T3 = Constitution / ADR / Harness Gates 정의 자체 변경 영역 — docker socket 접근 = repo policy 변경 영역 부분 중첩) |
| 풀 3+1 + 외부 LLM 1+ 의무 추가 | ✅ (6 escalation trigger #5 발화 → 합의 형태 의무 변경) |
| ST-2 단독 진입의 T2 유지 의도 와 충돌 | ✅ (사용자 명시 답습 — ST-2 = T2 단독 진입) |

**판정**: ✅ **적절** — F-A 비채택 = 권한 영역 확대 회피 + T3 가능성 회피 + 풀 3+1 의무 회피 + T2 유지 (brief §7.3 답습). 사용자 명시 #1 결정 답습 충실.

### 1.5 검토 기준 #5 — Multi-host parity 미요구가 적절한지

**brief §3.3 + §10.1 #6 + 사용자 #2 결정 답습**:

| 영역 | 검증 |
|------|------|
| MVP-1 영역 정의 | 단일 host (single-host / isolated PoC 기준) — Backlog #7 Operational Readiness 영역 분리 답습 |
| Multi-host parity = Backlog #7 영역 | ✅ (`docs/review/3plus1-consensus-2026-05-13-mvp1-pass.md` §3.4 C-3 답습 — "Operational Readiness parity (Multi-environment + Vault HSM ST-4)") |
| ST-2 단독 진입 = MVP-1 단일 host 한정 | ✅ (사용자 명시 답습) |
| 6 escalation trigger #6 발화 회피 | ✅ (brief §10.1 답습) |
| ADR-010 (Vault HSM Multi-host) 자동 진입 회피 | ✅ (사용자 명시 답습) |

**판정**: ✅ **적절** — Multi-host parity 미요구 = MVP-1 단일 host 영역 한정 + Backlog #7 영역 분리 보존 + 6 trigger #6 발화 회피. 사용자 명시 #2 결정 답습 충실.

### 1.6 검토 기준 #6 — `/run/secrets/*` 감시 경로가 적절한지

**brief §5 + 사용자 #3 결정 답습**:

| 경로 사유 | 검증 |
|---------|------|
| docker secret 표준 mount 경로 | ✅ (Docker secret 공식 mount 경로 `/run/secrets/<name>` 표준) |
| ST-3 docker secret 흐름과 정합 | ✅ (mvp1.md §5.5.1 ST-3 본문 채택 답습 — docker secret 메커니즘) |
| Hermes upstream 변경 없이 sidecar 에서 감시 가능 | ✅ (sidecar = 별도 mount, Hermes container 자체 변경 0건) |
| ADR-008 차단조건 #6 + 부록 B (37번째 entry R-S1 정정 답습) 답습 | ✅ (docker secret 권위 출처) |
| 사용자 정의 mount 경로 = 구현 시점 후보로 보류 | ✅ (brief §5.4 답습 — 본 합의 = `/run/secrets/*` 기본) |

**판정**: ✅ **적절** — `/run/secrets/*` = docker secret 표준 + ST-3 정합 + ADR-008 차단조건 #6 + 부록 B (37번째 entry R-S1 정정 답습) 답습 + Hermes upstream 변경 회피. 사용자 명시 #3 결정 답습 충실.

### 1.7 검토 기준 #7 — runtime secret 변경 fail-closed 처리가 적절한지

**brief §6.2 + 사용자 #4 결정 답습**:

```
runtime secret 변경 = 기본적으로 fail-closed
```

| fail-closed 처리 시나리오 | sidecar 행동 |
|---------------------|---------|
| init 단계 (container 시작 시 secret 주입) | grace period 후 감시 시작 (정상 init 무시) |
| runtime mtime / perm / content 변경 (정상 rotation 포함) | **모든 runtime 변경 = fail-closed** (사용자 #4 결정 답습) |
| 외부 attack vector (chmod 644 등) | fail-closed (F-B status file write → Hermes unhealthy) |

**검증**:

- 보안 우선 원칙 — runtime 변경 = 잠재적 attack vector 가능성 (false negative > false positive 회피)
- ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (37번째 entry R-S1 정정 답습) 답습 — 저장 경로 secret 보호 강화
- GP-3 §5.3 답습 — "inotify 런타임 감시 (mtime/perm 변경 → 컨테이너 정지)"
- secret rotation 정책 분리로 정상 rotation 시나리오 = 별도 합의 (사용자 #4 결정 답습)

**판정**: ✅ **적절** — runtime 변경 fail-closed = 보안 우선 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (37번째 entry R-S1 정정 답습) 답습 + GP-3 §5.3 답습 + secret rotation 정책 별도 합의 분리 정합. 사용자 명시 #4 결정 답습 충실.

### 1.8 검토 기준 #8 — secret rotation 정책을 별도 합의로 분리했는지

**brief §6.2 + 사용자 #4 결정 답습**:

| 영역 | 본 합의 처리 |
|------|-----------|
| 본 합의 범위 = runtime 변경 fail-closed | ✅ |
| secret rotation 정책 영역 분리 | ✅ "secret rotation 정책 = 별도 합의 영역" |
| 연결 가능 후속 합의 영역 enumeration | ✅ Operational Readiness (Backlog #7) / Vault HSM (ST-4, ADR-010) / secret rotation 자체 정책 (별도 P 발행 가능) |
| 본 brief 의 R-ST2-3 (정상 rotation 오탐) trigger 명시 | ✅ brief §9.2 R-ST2-3 답습 — "secret rotation 정책 별도 합의 진입" |

**검증**:

- 사용자 명시 #4 결정 답습 — runtime fail-closed + rotation 별도 합의
- Multi-host parity 미요구 (사용자 #2 결정) 와 일관성 — 둘 다 Operational Readiness 영역 부분 흡수 가능 영역
- Vault HSM (ST-4) 자동 진입 회피 답습 (사용자 명시)

**판정**: ✅ **적절** — secret rotation 정책 분리 명시 + 연결 가능 후속 합의 영역 enumeration + R-ST2-3 trigger 권위 확정 (brief §6.2 + §9.2 답습). 사용자 명시 #4 결정 답습 충실.

### 1.9 검토 기준 #9 — T3 자동 진입이 발생하지 않았는지

**brief §2.3 + §10.1 + 사용자 명시 4 결정 답습 결과**:

| T3 침범 후보 | 본 합의 발화 |
|------------|----------|
| Hermes upstream Dockerfile 변경 | ❌ 0건 (사용자 #1 + §3 답습) |
| Constitution / ADR / Harness Gates 정의 변경 | ❌ 0건 (sidecar = 운영 layer) |
| Branch protection rule 변경 | ❌ 0건 (저장 경로 영역 한정) |
| Tier-2/3 catalog 확장 | ❌ 0건 (catalog 영역 외) |
| Vault HSM (ST-4) 진입 | ❌ 0건 (사용자 명시 답습) |
| docker socket 접근 (F-A 비채택) | ❌ 0건 (사용자 #1 결정 답습 — F-A 비채택) |
| Multi-host parity 자동 진입 | ❌ 0건 (사용자 #2 결정 답습) |
| ST-1 자동 진입 | ❌ 0건 (Backlog #3 분리 답습) |
| PC-4 자동 진입 | ❌ 0건 (Backlog #1 + #2 분리 답습) |
| dev 환경 강제 (PC-4 T3 sub) | ❌ 0건 |

**판정**: ✅ **적절** — T3 자동 진입 10/10 0건 발화. 사용자 명시 4 결정 답습 결과 + brief §2.3 + §10.1 권위 근거 충실.

### 1.10 9/9 검토 기준 충족 합산

| 검토 기준 # | 항목 | 판정 |
|----------|------|------|
| 1 | ST-2 T2 영역 분류 적절성 | ✅ 적절 (ADR-011 §2.4 + mvp1.md §3.3 + Backlog #1 진입 직전 정비 합의 답습) |
| 2 | Hermes upstream 변경 0건 적절성 | ✅ 적절 (§3 답습 — 7/7 변경 후보 0건) |
| 3 | F-B 우선 채택 적절성 | ✅ 적절 (사용자 #1 결정 답습 + brief §7.2 6/6 사유 충족) |
| 4 | F-A 비채택 적절성 | ✅ 적절 (사용자 #1 결정 답습 + brief §7.3 5/5 사유 충족) |
| 5 | Multi-host parity 미요구 적절성 | ✅ 적절 (사용자 #2 결정 답습 + Backlog #7 영역 분리 보존) |
| 6 | `/run/secrets/*` 감시 경로 적절성 | ✅ 적절 (사용자 #3 결정 답습 + ADR-008 차단조건 #6 + 부록 B (37번째 entry R-S1 정정 답습) + ST-3 정합) |
| 7 | runtime secret 변경 fail-closed 처리 적절성 | ✅ 적절 (사용자 #4 결정 답습 + ADR-008 차단조건 #1 + #6 + 부록 B + ADR-010 + ADR-011 (37번째 entry R-S1 정정 답습) + GP-3 §5.3 답습) |
| 8 | secret rotation 정책 별도 합의 분리 적절성 | ✅ 적절 (사용자 #4 결정 답습 + 연결 가능 후속 합의 영역 enumeration) |
| 9 | T3 자동 진입 0건 적절성 | ✅ 적절 (10/10 T3 침범 후보 0건 — 사용자 명시 4 결정 답습 결과) |

**합산 = 9/9 적절** — 본 brief 의 ST-2 단독 진입 적격성 + 사용자 명시 4 결정 답습 + T3 자동 진입 0건 모두 권위 근거 충실 (Layer D / Backlog #1 진입 직전 정비 / mvp1.md §3 / §5.5 / ADR-008 / ADR-011 답습).

---

## 2. 풀 3+1 승격 트리거 검증 (7/7 0건 발화)

### 2.0 7 트리거 답습 (직전 Reviewer-only 단축 합의 chain 답습)

| # | 트리거 | 본 합의 검토 결과 |
|---|----|------------|
| 1 | 본 합의가 9 sub-수단 *외* 수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — 본 합의 = ST-2 단독 진입 적격성 한정 (Layer B §5.5 본문 채택 4 sub-수단 GP-3 + 3 sub-수단 GP-5 + 2 공유 모두 변경 0건) |
| 2 | 본 합의가 T3 영역 *자동 진입* 을 권고하는 경우 | ❌ 0건 발화 — 본 합의 = T3 자동 진입 10/10 0건 (검토 기준 #9 답습, §1.9) |
| 3 | 본 합의가 9 sub-수단 *재결정* 을 권고하는 경우 | ❌ 0건 발화 — §5.5 본문 채택 변경 0건 |
| 4 | 본 합의가 Provider Liquidity 5-way 약화 가능성을 포함하는 경우 | ❌ 0건 발화 — 본 합의 = GP-3 저장 경로 isolation 영역, Provider Liquidity 영향 0건 |
| 5 | 본 합의가 5 영구 핵심 제약 (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리) 中 1+ 의 약화를 포함하는 경우 | ❌ 0건 발화 — Hermes ≠ root of trust 보존 (F-A 비채택 답습) + T3 분리 보존 (자동 진입 0건) + 수단/목적 분리 보존 |
| 6 | 본 합의가 MVP-1 PASS *재선언* / Layer E / Layer F 격상을 포함하는 경우 | ❌ 0건 발화 — 사용자 명시 답습 (§0.4 비검토 대상) |
| 7 | 본 합의가 외부 LLM cross-vendor blind 의뢰 *없이* T3 영역 결정을 권고하는 경우 | ❌ 0건 발화 — 본 합의 = T3 자동 진입 0건 (검토 기준 #9 답습) |

**합산 = 7/7 0건 발화** → Reviewer-only 단축 합의 적격 확정.

### 2.1 본 §2 의 *범위 한계*

본 §2 = *풀 3+1 승격 트리거 0/7 발화 검증 한정*. 본 합의 *발효 후* 구현 단계에서 트리거 발화 시 별도 풀 3+1 합의 의무 답습 (트리거별 형태 = brief §9 R-ST2-1~R-ST2-8 답습).

---

## 3. 본 합의 발효 범위 (사용자 명시 답습)

### 3.1 본 합의가 *발생시키는* 것

| # | 영역 |
|---|------|
| 1 | Backlog #1 ST-2 (inotify sidecar) *단독 우선 진입 적격성* 권위 확정 |
| 2 | 사용자 명시 4 결정 답습 *권위 확정* (F-B 우선 / F-C 보조 / F-A 비채택 / Multi-host 미요구 / `/run/secrets/*` / secret rotation 별도 합의) |
| 3 | ST-2 = T2 영역 권위 확정 (T3 침범 10/10 0건) |
| 4 | Hermes upstream Dockerfile 변경 0건 권위 확정 (docker-compose level healthcheck 영역 한정) |
| 5 | sidecar 분리 구조 (brief §4) + inotify 감시 대상 (brief §5) + mtime/perm 감지 기준 (brief §6) + fail-closed 동작 매트릭스 (brief §7) + evidence 기준 (brief §8) + Rollback Trigger 8 후보 (brief §9) 권위 권고 |
| 6 | 합의 형태 = Reviewer-only 단축 합의 chain 답습 (Layer C / Layer D / Backlog #5 / K-2 fix / §C-1 갱신 / Backlog #1 진입 직전 정비 / 본 합의) |
| 7 | 다음 단계 = ST-2 *실 구현* 진입 *직전* 의사결정 입력 정비 완료 — 사용자 명시 결정 의무 보존 |

### 3.2 본 합의가 *발생시키지 않는* 것 (사용자 명시 답습)

| # | 영역 | 본 합의 발효 시점 위반 |
|---|------|------------------|
| 1 | ST-2 *실 구현* (sidecar Dockerfile / inotify 스크립트 / docker-compose 변경 / Hermes healthcheck 본문) | 0건 |
| 2 | CI workflow 변경 (`.github/workflows/*.yml` 본문 변경 / 신규 step / 신규 workflow) | 0건 |
| 3 | hook 변경 | 0건 |
| 4 | ST-1 *자동 진입* (T3 영역, Backlog #3) | 0건 |
| 5 | PC-4 *자동 진입* (T2 sub + T3 sub 모두, Backlog #1 + #2 분리) | 0건 |
| 6 | ST-4 (Vault HSM) *자동 진입* (Operational Readiness, Backlog #7) | 0건 |
| 7 | Multi-host parity *자동 진입* (사용자 #2 결정 답습) | 0건 |
| 8 | T3 영역 *자동 진입* (Hermes upstream / docker socket / Tier-2-3 catalog / branch protection / dev 환경 강제) | 0건 |
| 9 | MVP-1 PASS *재선언* (Layer D 본문 변경) | 0건 (`210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| 10 | Operational Readiness PASS (Layer E) 선언 | 0건 (MVP-6 영역, Backlog #7) |
| 11 | Hermes PMO 격상 (Layer F) | 0건 (MVP-6 영역, 외부 LLM + 사람 리뷰 의무) |
| 12 | §C-5 *Satisfied 자동 갱신* | 0건 (본 합의 = 진입 적격성 확정 한정, §C-5 Deferred 그대로 유지) |
| 13 | C-2~C-4 / C-6~C-8 상태 *자동 변경* | 0건 (§C-5 진입 적격성 한정) |
| 14 | §5.5 9 sub-수단 본문 채택 *변경* | 0건 (`f40423f` + `55c5b4b` 답습) |
| 15 | ADR 본문 *자동 갱신* | 0건 (cross-reference 답습 한정) |
| 16 | 다른 backlog (#2/#3/#4/#7) *자동 진입* | 0건 |
| 17 | Tier-2 / Tier-3 catalog 자동 확장 | 0건 |
| 18 | 사용자 명시 4 결정 *재변경* | 0건 (본 합의 = 4 결정 답습 한정) |
| 19 | 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출 | 0건 |
| 20 | 신규 ADR / 신규 P / 신규 GP 발행 | 0건 |
| 21 | 17 항목 우선순위 자동 *재고정* | 0건 |
| 22 | Provider Liquidity 5-way / 5 영구 핵심 제약 약화 | 0건 |
| 23 | CONTEXT / INDEX / SESSION 메타 갱신 (별도 commit 분리 답습) | 0건 |

### 3.3 본 합의 발효 후 다음 단계 (사용자 결정 영역 — 자동 진입 0건)

| 후보 | 영역 | 합의 형태 권고 |
|------|------|----------|
| **(1)** | **ST-2 실 구현 진입** (sidecar Dockerfile + inotify 스크립트 + docker-compose service / healthcheck / volume + CI step + actual run + evidence) | 사용자 명시 결정 후 진입 — Layer C 시점 evidence 합의 (brief §8 답습) |
| (2) | CONTEXT / INDEX / SESSION 메타 갱신 (별도 commit 분리 답습) | 사용자 명시 결정 영역 |
| (3) | PC-4 T2 sub 단독 진입 (Backlog #1 + #2 공유 — config 정의 한정) | 단축 합의 + 사용자 명시 결정 |
| (4) | Backlog #2 brief 작성 (GP-5 1.5차) | 본 brief 패턴 답습 |
| (5) | Backlog #3 brief 작성 (T3 영역 — ST-1 병합 검토) | 풀 3+1 + 외부 LLM 1+ 권고 |
| (6) | MVP-2 진입 합의 (G2 GP-2 + G4 §4.4 Layer 4) | 별도 합의 |
| (7) | 본 합의 commit 한정 → 세션 종료 | 다음 세션에서 사용자 명시 결정 |

⚠️ **본 합의 APPROVE 직후 자동 다음 단계 진입 금지** — 사용자 명시 결정 의무.

⚠️ **사용자 명시 다음 단계 = ST-2 실 구현 진입은 *아직 아님*** — 본 합의 = 진입 *적격성* 확정 한정. 구현 진입 시점 = 별도 합의 + 사용자 명시 결정 (사용자 명시 답습 — "구현은 아직 하지 않음").

---

## 4. 발효 영향 매트릭스

### 4.1 Layer + Backlog 분리 매트릭스 (본 합의 발효 시점)

```
Layer A : Backlog #6 entry 기준 정의                       — APPROVE (f1e0b23)
Layer B : 9 sub-수단 본문 채택 + 시작 권한                 — APPROVE (f40423f + 55c5b4b)
Layer B 행사: Stage 1+3 / 2 / 4 / 5                        — 발효 (5 runs PASS)
Layer C : MVP-1 Implementation Evidence PASS              — APPROVE (6973935)
Layer D : MVP-1 PASS                                      — APPROVE WITH CONDITIONS (210c98f, 본문 변경 0건)
Backlog #5 ADR-012 event enum 정식 등록                   — APPROVE (4221646 + 2ece90a + b705370) — §C-2 Satisfied
K-2 baseline fix 1단계 + actual run + §C-1 갱신          — APPROVE (6b9fedf + 6d95cad + 155f1a9 + 10830cb + 1dd1036 + 56da31f) — §C-1 Satisfied
Backlog #1 진입 *직전* 사전 정비 (브리프 분류)            — APPROVE AS BRIEF (43b898c + 6b15070 + 45de393)
■ Backlog #1 ST-2 단독 우선 진입 적격성 (브리프 + 합의)   — APPROVE (본 합의 + brief d9ae98b + 메타 commit 후속) ← 본 단계
■ Backlog #1 ST-2 *실 구현*                                — 아직 아님 (사용자 명시 답습 — 본 합의 ≠ 구현 진입)
Layer E : Operational Readiness PASS 선언                 — 아직 아님 (C-3, MVP-6, Backlog #7)
Layer F : Hermes PMO 격상                                 — 아직 아님 (C-4, MVP-6, 외부 LLM + 사람 리뷰 의무)
```

### 4.2 C-1~C-8 상태 (본 합의 발효 후)

| Condition | 상태 | 본 합의 영향 |
|----------|------|----------|
| C-1 (K-2 baseline 후속 fix) | ✅ Satisfied (`1dd1036`) | 변경 0건 |
| C-2 (event enum 정식 등록) | ✅ Satisfied (Backlog #5 `b705370`) | 변경 0건 |
| C-3 (Operational Readiness parity) | ⏳ Deferred (MVP-6, Backlog #7) | 변경 0건 |
| C-4 (Hermes PMO 격상) | ⏳ Deferred (MVP-6, 외부 LLM + 사람 리뷰 의무) | 변경 0건 |
| **C-5 (GP-3 1.5차 보강 — Backlog #1)** | ⏳ **Deferred** (본 합의 = ST-2 진입 *적격성* 확정 한정 — **상태 변경 0건**) | **ST-2 진입 적격성 권위 확정 한정 — Condition 상태 변경 0건** |
| C-6 (GP-5 1.5차 보강 — Backlog #2) | ⏳ Deferred (Backlog #2) | 변경 0건 |
| C-7 (T3 영역 — Backlog #3) | ⏳ Requires separate full 3+1 (Backlog #3) | 변경 0건 |
| C-8 (P1 v2 facade MVP — Backlog #4) | ⏳ Deferred (Backlog #4, MVP-3 권고) | 변경 0건 |

**핵심**: 본 합의 = §C-5 *ST-2 진입 적격성* 권위 확정 한정 — §C-5 *상태 변경 0건* (Deferred 그대로 유지, 실 구현 + evidence + §C-5 갱신 합의 후속 의무 영역).

### 4.3 본 합의 행사 의무 (사용자 명시 답습)

| 항목 | 의무 |
|------|------|
| commit 분리 (2 commit) | ✅ Commit 1 (brief `d9ae98b`) + Commit 2 (합의 보고서 — 본 commit) |
| CONTEXT / INDEX / SESSION 메타 갱신 분리 | ✅ 별도 commit (사용자 명시 답습 — "이후 별도 commit으로 분리합니다") |
| ST-2 실 구현 진입 자동 금지 | ✅ 사용자 명시 결정 의무 (사용자 명시 답습 — "구현은 아직 하지 않음") |
| 사용자 명시 4 결정 보존 | ✅ §1.3~§1.8 검토 기준 #3~#8 답습 |

---

## 5. 메타 검증

| 메타 검증 | 본 합의 |
|---------|--------|
| 사용자 명시 진입 명령 답습 (옵션 (A) + 4 결정 + Reviewer-only 단축 합의) | ✅ (§0.1 답습) |
| 사용자 명시 13 금지 답습 | ✅ (§0.4 + §3.2 답습) |
| 9 검토 기준 충족 | ✅ (9/9 — §1.1~§1.9 답습) |
| 7 풀 3+1 승격 트리거 0건 발화 | ✅ (§2 답습) |
| §5.5 9 sub-수단 본문 채택 답습 | ✅ (변경 0건) |
| C-1~C-8 상태 답습 | ✅ (C-1+C-2 Satisfied / C-3~C-8 Deferred/Requires separate — 변경 0건) |
| MVP-1 PASS Layer D 본문 답습 | ✅ (`210c98f` APPROVE WITH CONDITIONS 그대로 유지) |
| Backlog #1 진입 직전 정비 합의 (`43b898c`) 답습 | ✅ |
| ADR-011 §2.4 T1/T2/T3 분류 답습 | ✅ (ST-2 = T2 + T3 침범 10/10 0건) |
| ADR-008 차단조건 #1 + #6 + 부록 B 답습 | ✅ (cross-reference 답습 한정 — 본문 변경 0건, 37번째 entry R-S1 정정 답습) |
| 5 영구 핵심 제약 보존 | ✅ (Provider Liquidity / Hermes ≠ root of trust / 메타포 강제 금지 / T3 분리 / 수단/목적 분리 모두 답습) |
| 7 backlog 분리 매트릭스 답습 | ✅ (Backlog #2/#3/#4/#5/#7 자동 진입 0건) |
| 자동 진입 0건 (ST-2 실 구현 / 다른 backlog / T3 영역 / Multi-host parity) | ✅ |
| commit 분리 답습 (brief + 합의 보고서) | ✅ (사용자 명시 답습) |
| ST-2 실 구현 ≠ 본 합의 범위 | ✅ (사용자 명시 답습 — "구현은 아직 하지 않음") |
| 사용자 명시 4 결정 보존 답습 | ✅ (재변경 0건, 검토 기준 #3~#8 답습) |

---

## 6. 본 합의 요약 (한 단락)

본 합의 는 **Backlog #1 ST-2 (inotify sidecar) *단독 우선 진입* 적격성 권위 확정 + 사용자 명시 4 결정 답습 적절성 확정 (Reviewer-only 단축 합의)** 이다. 사용자 명시 9 검토 기준 (ST-2 T2 영역 / Hermes upstream 변경 0건 / F-B 우선 채택 / F-A 비채택 / Multi-host parity 미요구 / `/run/secrets/*` 감시 경로 / runtime secret 변경 fail-closed / secret rotation 정책 별도 합의 분리 / T3 자동 진입 0건) 모두 9/9 적절 확정 + 7 풀 3+1 승격 트리거 0/7 발화 확인 + §5.5 9 sub-수단 본문 채택 변경 0건 + C-1~C-8 상태 변경 0건 (§C-5 Deferred 그대로 유지). 사용자 명시 4 결정 — (1) fail-closed = **F-B 우선** (status file → Hermes healthcheck unhealthy, docker-compose level) / F-C 보조 / **F-A 비채택** (docker socket 권한 영역 회피) / (2) **Multi-host parity 미요구** (MVP-1 단일 host 한정) / (3) inotify 감시 경로 = **`/run/secrets/*`** (ADR-008 차단조건 #6 + 부록 B (37번째 entry R-S1 정정 답습) docker secret 답습) / (4) **runtime secret 변경 = fail-closed + secret rotation 정책 = 별도 합의 영역 분리** — 모두 권위 확정. **본 합의 ≠ ST-2 실 구현 / docker-compose 변경 / CI workflow / hook / Hermes Dockerfile 변경 / 다른 backlog 자동 진입 / T3 영역 자동 진입 / Multi-host parity 자동 진입 / MVP-1 PASS *재선언* / Operational Readiness PASS / Hermes PMO 격상 / §C-5 *Satisfied* 자동 갱신** (사용자 명시 답습 — "구현은 아직 하지 않음"). 다음 단계 사용자 결정 영역 = ST-2 *실 구현* 진입 (별도 합의 + 사용자 명시) 또는 CONTEXT / INDEX / SESSION 메타 갱신 (별도 commit 분리 답습) 또는 다른 backlog 진입.

---

**합의 일자**: 2026-05-13 후속 25
**판정**: ✅ **APPROVE — Backlog #1 ST-2 (inotify sidecar) 단독 우선 진입 적격성 권위 확정 (Reviewer-only 단축 합의, 사용자 명시 4 결정 답습)**
**다음 단계**: 사용자 결정 영역 (자동 진입 0건)
- (1) ST-2 실 구현 진입 (별도 합의 + 사용자 명시 — 사용자 명시 답습: "구현은 아직 하지 않음")
- (2) CONTEXT / INDEX / SESSION 메타 갱신 (별도 commit 분리 답습)
- 후보 (3)~(7) = §3.3 답습

**금지 (사용자 명시 답습 — 본 합의 영역 + 본 합의 발효 후 단계 양쪽)**:
- ❌ ST-2 *실 구현* (sidecar Dockerfile / inotify 스크립트 / docker-compose 변경 / Hermes healthcheck 본문 / CI workflow / hook 모두 0건)
- ❌ ST-1 자동 진입 (T3 영역, Backlog #3)
- ❌ PC-4 자동 진입 (T2 sub + T3 sub 모두, Backlog #1 + #2 분리)
- ❌ ST-4 / Vault HSM 자동 진입 (Operational Readiness 영역, Backlog #7)
- ❌ Multi-host parity 자동 진입 (사용자 #2 결정 답습)
- ❌ T3 영역 *자동 진입* (Hermes upstream / docker socket / Tier-2-3 catalog / branch protection / dev 환경 강제)
- ❌ MVP-1 PASS *재선언*
- ❌ Operational Readiness PASS (Layer E) 선언
- ❌ Hermes PMO 격상 (Layer F)
- ❌ §C-5 *Satisfied 자동 갱신* (본 합의 발효 후에도 Deferred 유지)
- ❌ C-2~C-4 / C-6~C-8 상태 *자동 변경*
- ❌ §5.5 9 sub-수단 본문 채택 *변경*
- ❌ ADR 본문 *자동 갱신*
- ❌ 다른 backlog (#2/#3/#4/#7) *자동 진입*
- ❌ 사용자 명시 4 결정 *재변경*
- ❌ Tier-2 / Tier-3 catalog 자동 확장
- ❌ 외부 LLM 자동 호출 / 실 API key / provider SDK / 외부 API 호출
- ❌ 신규 ADR / 신규 P / 신규 GP 발행
- ❌ Provider Liquidity 5-way / 5 영구 핵심 제약 약화
- ❌ CONTEXT / INDEX / SESSION 메타 갱신 (본 commit ≠ 메타 갱신 — 별도 commit 분리 답습)
