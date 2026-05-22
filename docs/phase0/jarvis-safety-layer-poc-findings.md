# Jarvis 안전 레이어 PoC 발견 — OpenShell 평가 → 경량 격리 채택

**작성일**: 2026-05-22
**Status**: PoC 완료 — 결정 반영 대상(brief v2 §안전)
**목적**: 3+1 합의가 찾은 BLOCKING(워커 신뢰경계 B-2/B-6, 자가진화 게이트 B-1)을 NVIDIA OpenShell로 해결할지 실증. "OpenShell 통째 채택 vs 참조만" 비례성 판단.
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
**출처**: 본 세션 PoC(2026-05-22) / OpenShell GitHub README(NVIDIA/OpenShell) / DGX Spark 플레이북 README / PyPI openshell 버전 이력 / 웹 검색(경량 sandbox 2026: Claude Code bubblewrap, Codex Landlock+seccomp, firejail Gorgon) / 머신 실측. 답습: [[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]] / `project_jarvis_local_boss_direction` / `feedback_proportionate_security_personal_tool`.
