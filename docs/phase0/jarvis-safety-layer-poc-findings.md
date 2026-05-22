# Jarvis 안전 레이어 PoC 발견 — OpenShell 평가 → 경량 격리 채택

**작성일**: 2026-05-22 (세션 1: OpenShell 평가 / **세션 3: V-2 Landlock 실증 — §6**)
**Status**: PoC 완료 (OpenShell 평가 + **V-2 Landlock 격리 실증 완료**) — 결정 반영 대상(brief §6 / Q-9 / 트랙 B)
**목적**: 3+1 합의가 찾은 BLOCKING(워커 신뢰경계 B-2/B-6, 자가진화 게이트 B-1)을 NVIDIA OpenShell로 해결할지 실증. "OpenShell 통째 채택 vs 참조만" 비례성 판단. **+ V-2: 채택한 Landlock 경량 격리의 실제 동작·이중격리 순이득 실측(§6).**
**환경**: NVIDIA GB10 / aarch64 / Ubuntu 24.04.4 LTS / 커널 6.17 / Docker 29.2.1 (delangi=docker+sudo)

---

## 1. 실행 결과

| # | 검증 | 결과 |
|---|------|------|
| P-1 | uv 설치 | ✅ 0.11.16 (aarch64) — `~/.local/bin` |
| P-2 | OpenShell CLI 설치 | ✅ **0.0.46** (Rust, aarch64) — `~/openshell-env` venv |
| P-3 | Docker 도달 | ✅ |
| P-4 | 플레이북 `openshell gateway start` | ❌ **명령 없음** — 0.0.46 gateway = add/remove/login/select/info/list만 |
| P-5 | 현 게이트웨이 배포 방식 | ⚠️ **Helm + Kubernetes(k3s)** (`helm install openshell oci://ghcr.io/nvidia/openshell/helm-chart`) |
| P-6 | 커널 Landlock LSM | ✅ **활성** (`/sys/kernel/security/lsm` = lockdown,capability,**landlock**,yama,apparmor,ima,evm) |
| P-7 | bubblewrap | ✅ 설치됨 (`/usr/bin/bwrap`), 호스트에서 격리 동작 확인(BWRAP_OK + /home tmpfs 은닉) |
| P-8 | firejail / landrun / nsjail | 미설치 |
| P-9 | Ubuntu 24.04 unprivileged userns | ⚠️ `apparmor_restrict_unprivileged_userns=1` (제한) / `unprivileged_userns_clone=1` |

## 2. 핵심 발견

### F-1 — NVIDIA DGX Spark OpenShell 플레이북이 stale
플레이북(`NVIDIA/dgx-spark-playbooks/nvidia/openshell`, 2026-03-13자)은 `openshell gateway start`(k3s-in-docker 자동 부트스트랩)를 쓰지만, 이 명령은 **초기 버전(0.0.0a0~0.0.6, 2026-03 중순)에만** 존재. PyPI 37 릴리스(2026-03~05) 거치며 게이트웨이 배포가 **Helm/k8s로 전환**. 현 0.0.46엔 `gateway start` 없음. (검색 NemoClaw issue #835 "install command out of date"와 일치.)

### F-2 — OpenShell 통째 채택 = k3s 상시 구동 = 개인 툴 비례 초과
현 OpenShell을 안전 substrate로 쓰려면 개인 머신에 **Kubernetes(k3s) 클러스터 + Helm 게이트웨이** 상시 구동 필요. solo 단일 개발자 개인 툴엔 과중한 인프라. → `feedback_proportionate_security_personal_tool` 답습.

### F-3 — 워커 제작사가 이미 경량 격리 (k3s 아님)
2026 현황: **Claude Code = Linux에서 bubblewrap**, **OpenAI Codex = Landlock + seccomp(기본 ON, 유일)**. firejail=setuid root+제로데이(Gorgon) 회피. nsjail/systemd-nspawn=과함/root. → 워커 본인들이 쓰는 검증된 경량 수단 = bubblewrap·Landlock.

### F-4 — Landlock은 userns 불요 → Ubuntu 24.04 제한 우회
bubblewrap은 unprivileged userns 의존 → 24.04 AppArmor 제한 영향(에이전트 셸 내 테스트는 uid-map/loopback 실패 = 네임스페이스 중첩 간섭 + 24.04 제한). **Landlock은 현재 프로세스 fs/net 접근을 syscall로 제한, userns·root·컨테이너 불요** → 24.04 제한 우회(Codex 방식). 커널 6.17 = Landlock 풀 ABI(net 포트 제한 ABI4는 6.7+).

## 3. 결정 (사용자 명시 "c로 진행")

**OpenShell = 안전 *참조 설계*로만 채택**, 워커 격리는 k3s 없이 경량 직접 구현.
- 참조할 OpenShell 개념: Landlock 기반 격리 / deny-by-default 정책 / Privacy Router(로컬 vs 프론티어 라우팅) / skill 검증 + 정책변경=승인 게이트.
- **권고 격리 설계 (brief v2 §안전)**: **Landlock 중심**(fs VFS 제한 + net 포트 제한, userns·root 불요 — OpenShell과 동일 primitive를 k3s 없이) **+ bubblewrap 보완**(mount/pid 네임스페이스). 워커당 작업디렉터리만 노출 = 3+1 B-2/B-6 해결. egress 정책 = B-3.
- 후보 도구: `landrun`(Landlock CLI, Go) 또는 직접 Landlock+seccomp(Codex 방식). bubblewrap(이미 설치).

## 4. 머신 상태 / 롤백
- 설치됨(무해): `~/.local/bin/uv*`, `~/openshell-env` venv. → `rm -rf ~/openshell-env ~/.local/bin/uv*`로 완전 복구.
- **0건**: Docker daemon.json 변경 / k3s 설치 / 모델 다운로드 / sudo 시스템 변경 / 서비스 설치.

## 5. 다음
- brief v2에 반영: OpenShell=참조only / Landlock+bubblewrap 경량 격리 / 3+1 12 修正.
- 후속 PoC 후보: landrun 설치 + Landlock fs/net 격리 실증, bubblewrap unprivileged(사용자 셸) 클린 테스트.

---

## 6. V-2 PoC 실행 결과 (2026-05-22 세션 3 — brief v3 트랙 B de-risk)

> **목적**: brief v3 §7 V-2 = Landlock 워커 격리 실증 + bubblewrap 클린 테스트 + **이중격리 순이득 실측(v3-3)**. landrun 미설치·go 미설치 → **직접 Landlock syscall(C ~110줄)**로 실증(머신 오염 최소화).

| # | 검증 | 결과 |
|---|------|------|
| V2-1 | 빌드 도구 | ✅ gcc 13.3.0 / `/usr/include/linux/landlock.h`(풀 매크로) / seccomp.h. go 미설치 → 직접 C 채택 |
| V2-2 | Landlock sandboxer 컴파일 | ✅ `/tmp/jarvis-v2-poc/ll_sandbox.c` (path_beneath 기반, RW/RO 디렉터리 분리) → **런타임 ABI = 7** (커널 6.17) |
| V2-3 | **작업디렉터리 격리 실증** | ✅ workspace **RW** OK / 프로젝트 소스(`CLAUDE.md`) 읽기 **차단(EACCES)** / `~/.ssh` 접근 **차단** / workspace 밖 쓰기 **차단**(`PWNED.txt` 미생성 확인) / `/etc`는 명시 허용 시만 읽힘 = **deny-by-default** |
| V2-4 | root/userns 불요 | ✅ uid 1000 평범 실행 — **24.04 AppArmor userns 제한과 무관하게 동작**(F-4 확정) |
| V2-5 | bubblewrap unprivileged | ❌ `setting up uid map: Permission denied` — `apparmor_restrict_unprivileged_userns=1` + bwrap 비-setuid(`rwxr-xr-x`) → **추가 권한(sudo/AppArmor 프로파일/setuid) 없이는 불가**. 직전 F-4 예측이 *시스템 정책 차원*에서 확정(에이전트 셸 중첩 아님) |
| V2-6 | **claude 워커 자체 격리 의존성** | ⚠️ `claude.exe`(236MB Bun 네이티브) strings에 **`apt install bubblewrap`** → claude 자체 sandbox = **bwrap 의존** → 이 머신에서 동일하게 막힘(V2-5) |

### 핵심 발견 (V-2)

- **V-F1 — Landlock = 이 머신에서 *유일하게* 추가 권한 0으로 작동하는 워커 격리.** bwrap(우리·claude 공통)은 24.04 기본 보안 정책(`apparmor_restrict_unprivileged_userns=1`)에 막힘. Codex가 Landlock+seccomp를 채택한 이유가 머신에서 재현됨.
- **V-F2 — 이중격리 순이득 명백(검토 지점 3 / v3-3 측정 완료).** claude 자체 sandbox가 bwrap 의존(strings 정황) → 이 머신에서 비활성/제한 *가능* → 외부 Landlock이 사실상 유일한 실효 격리일 *수* 있음. **단 이 결론의 결정적 근거는 정황(V2-6 ⚠️)이 아니라**: 우리 외부 Landlock = **커널 강제**라 워커 침해·prompt injection으로 워커가 자기 sandbox를 끄거나 우회해도 유효(워커 신뢰 불요·정황과 독립). **중복 아님 → §6 강등 불요, Landlock 채택 유지 확정.**
- **V-F3 — §6 "bubblewrap 보완"은 이 머신에서 *조건부*(권한 작업 전제)로 정정 권고.** 무권한 환경에서 bwrap은 사실상 제외 → "Landlock 단독으로 워커당 작업디렉터리 격리 충족(이 머신)" + bwrap은 mount/pid ns가 꼭 필요하고 권한 작업이 허용될 때만.
- **V-F4 — 검증된 격리 = fs 한정.** `ll_sandbox`는 net ruleset 미포함(fs-only) → 워커 net egress(클라우드 CLI가 임의 호스트로 코드 전송) 미차단. net 포트 제한(ABI4)은 후속, egress 정책은 MVP-1+. MVP-0 워커가 클라우드 CLI이므로 egress 잔여 위험 존재 — brief §0/B-3가 명시한 인정 범위(BLOCKING 아님).
- **비용 = ~90줄 C wrapper(코드 75줄) + execvp.** 매우 경량 → 비례 적합(`feedback_proportionate_security_personal_tool`). MVP-0 트랙 B 격리 backend = 검증된 `ll_sandbox` path_beneath 패턴 재사용.

### V-2 머신 상태 / 롤백
- 추가물: `/tmp/jarvis-v2-poc/`(C 소스 + 바이너리 + workspace) — **`rm -rf /tmp/jarvis-v2-poc`로 완전 복구**. /tmp라 재부팅 시 자동 소멸.
- **시스템 변경 0건**: sysctl/AppArmor/setuid/패키지 설치/sudo 변경 0. PWNED.txt 미생성(격리 입증). repo 변경 0(본 문서 기록만).

### V-2 결정 영향 (brief 반영 대상)
- **§6**: "Landlock 중심 + bubblewrap 보완" → "**Landlock 단독 충분(무권한 환경)**, bwrap=권한 작업 전제 조건부". v3-3 이중격리 순이득 = **측정 완료, 순이득 확인**.
- **Q-9**: 워커 격리 구현 = **직접 Landlock C(landrun 불요) 실증됨**.
- **V-2 = MVP-0 트랙 B de-risk 완료** → 트랙 B 격리 backend 설계 위험 해소. (V-1=MVP-1 선결은 미착수 — Ollama tok/s 별개)
- **✅ 트랙 B 구현 완료(2026-05-22 세션 4, `ece32bc`)**: 본 §6 검증본 `ll_sandbox.c`를 `src/jarvis/sandbox/`로 그대로 재사용(본문 diff 0) + `LandlockIsolation`(`src/jarvis/isolation.py`, fail-closed=비격리 fallback 금지) 통합. 실제 빌드 바이너리로 workdir 밖 쓰기 차단 통합 테스트 재현(V2-3 동형). 50 tests / 커버리지 100% / import-linter KEPT. 증명 ⑤ 완성.
- **✅ A1 E2E 데모(`ed0df1b`, `examples/jarvis_e2e_demo.py`)**: 실제 claude 워커를 `LandlockIsolation` 격리 안에서 오케스트레이터로 1회 실행 → 증명 ①~⑤ 실 워커 입증(status=applied, exit 0, cost $0.05, hello.txt 생성, workdir 밖 쓰기 차단). **E2E 실측**: claude `-p`는 홈(`~`) 통째 RO 필요(설정·캐시·런타임 의존 — `--version`은 시스템 경로만으로 충분하나 `-p`는 부족 시 hang) + cwd·TMPDIR=workdir 필수. **RO 정밀화(민감 파일 읽기 차단)는 워커별 후속 과제**(claude=넓은 RO / codex 등=좁은 RO, `ro_paths` 워커별 조정). net egress(V-F4)와 함께 후속.

---
**출처**: 본 세션 PoC(2026-05-22 세션 1·3) / OpenShell GitHub README(NVIDIA/OpenShell) / DGX Spark 플레이북 README / PyPI openshell 버전 이력 / 웹 검색(경량 sandbox 2026: Claude Code bubblewrap, Codex Landlock+seccomp, firejail Gorgon) / 머신 실측 + V-2 Landlock 직접 실증. 답습: [[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]] / [[jarvis-orchestrator-mvp-design-brief]](v3) / `project_jarvis_local_boss_direction` / `feedback_proportionate_security_personal_tool`.
