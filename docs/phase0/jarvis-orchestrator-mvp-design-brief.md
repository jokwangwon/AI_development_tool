# Jarvis 오케스트레이터 MVP 설계 brief — 로컬 사장 + headless CLI 워커 (DRAFT v4)

> **본 brief = 자비스 오케스트레이터 MVP 설계 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임 설치·로컬 모델 다운로드·워커 격리 구현·sandbox 생성·git hook/CI 구성** 을 발생시키지 않는다. 본 brief = **3+1 합의(REVISE) 12 修正 + OpenShell PoC + v3 직접 검토 + v4 V-2 Landlock 실증 발견 반영한 설계 갱신** — 실 변경 0건(PoC=`/tmp` 격리, repo 코드 0). staged: brief v4 → 승인 → (재합의 or TDD 구현). 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-22
**Status**: **DRAFT v4 — V-2 Landlock 격리 실증(트랙 B de-risk) 반영, 재합의 또는 구현 진입 대기**
**진입 단위**: 자비스 본연 기능 — 오케스트레이터 MVP (보안 거버넌스 트랙과 독립)
**근거**: [[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]] (REVISE, 12 修正) · [[jarvis-safety-layer-poc-findings]] (OpenShell→경량 격리) · `project_jarvis_local_boss_direction` · `feedback_provider_liquidity` (헌법 5조) · `feedback_proportionate_security_personal_tool` (비례성) · `project_minimize_user_intervention`

## v2 변경 이력 (3+1 12 修正 반영)

| # | v1 → v2 | 출처 |
|---|---------|------|
| 🔴1 | §2 CUDA13 toolkit 보유 추가 + "70B 가능"→대역폭(273GB/s) 재기술 | GAP-A3 |
| 🔴2 | Q-2 vLLM 제외(#36821) → Ollama/llama.cpp | A-2,C-4 |
| 🔴3 | Q-1 MoE/30B이하 재조준 + tok/s 실측 기준 | A-3 |
| 4 | Q-3·§3·§5 **headless subprocess 1급**, tmux=관전용, "tmux 강제" 정정 | DIV-1,C-2 |
| 🔴5 | §6 워커 격리(작업디렉터리+무비판수용 금지) MVP 전제 + 신규 Q-9 | B-2/B-6,A-7 |
| 🔴6 | §8 immutable zone | B-1 |
| 7 | D-1 하이브리드 재정식화 + §0.1 "3+1 자동화" 매핑 삭제 | C-1,B-5 |
| 8 | §5·Q-4 사장도 provider 추상 / Worker=CLI+endpoint | A-7,C-4 |
| 9 | §5 MVP-0/MVP-1 단계 분리 | C-6,A-1 |
| 10 | Q-7 Layer 0 메모리 누적 학습 | C-5 |
| 11 | §0 egress·로컬 워커 부재 명시적 한계 | B-3 |
| 12 | Q-8 "확정(Python)" 강등 / §4 shogun 후속 메모 | CON-4,DIV-2 |
| + | §6 OpenShell=참조only + Landlock/bubblewrap 경량 격리 채택 | PoC findings |

### v3 변경 이력 (v2 직접 검토 반영)

| # | v2 → v3 | 출처 |
|---|---------|------|
| 🔴v3-1 | §5·§7 **MVP-0↔V-2 의존 순서 명시** — 워커 격리(증명 ⑤)는 V-2 통과에 의존하므로 "직교"가 아님. **2-트랙 시퀀싱**(트랙 A: 격리-제외 배관/headless 골격 TDD 선행 / 트랙 B: V-2 격리 실증 → 통합) 명문화 | v3 검토 지점 1 |
| v3-2 | Q-6 **게이트 위치 잠정 결정 = "반영 전"** (착수 전 아님) — §8 self-change 게이트와 동형, 개입 최소화 정합. §5 다이어그램 주석 | v3 검토 지점 2 + `project_minimize_user_intervention` |
| v3-3 | §6 워커 이중격리 효용 = V-2 측정 대상 명시(워커 자체 bwrap/Landlock 위 순이득 경계) | v3 검토 지점 3 |

### v4 변경 이력 (V-2 Landlock 실증 반영)

| # | v3 → v4 | 출처 |
|---|---------|------|
| v4-1 | §6·Q-9 **Landlock 단독 충분(무권한 환경) 확정** — 직접 Landlock C(ABI 7) 작업디렉터리 격리 실증(소스/SSH키 차단·밖 쓰기 차단). landrun/go 불요 | V-2: V2-3/V2-4 |
| v4-2 | §6 **bubblewrap = 조건부(권한 작업 전제)로 강등** — 24.04 `apparmor_restrict_unprivileged_userns=1`로 무권한 bwrap 불가(uid map denied) | V-2: V2-5, V-F3 |
| v4-3 | §6 **이중격리 순이득 확정(v3-3 측정 완료)** — claude.exe=`apt install bubblewrap` 의존 → 워커 자체 sandbox도 이 머신에서 막힘 → 외부 Landlock이 유일 실효 격리·커널 강제(워커 침해 무관). 강등 불요 | V-2: V2-6, V-F2 |
| v4-4 | §5 트랙 B **de-risk 완료** — 격리 backend = 검증된 `ll_sandbox` path_beneath 패턴 재사용 | V-2 종합 |

---

## 0. 비전

> **인터넷/구독에 묶이지 않는 나만의 자비스(Jarvis).** Provider-agnostic — Claude 비종속. 토큰 소진·구독 불가 시 다른 워커(GLM 등)로 계속 작업. 넓은 개인 비서 지향, **개발 작업이 MVP 중심**.

**⚠️ 비전 vs MVP 간극 (명시적 한계, B-3)**: MVP 워커는 대부분 클라우드 CLI(claude/codex…) → 이 단계에선 "인터넷 비종속"이 *부분적*으로만 성립(사장만 로컬). **완전 로컬 워커 + egress 통제는 §6 Privacy 정책 + MVP-1 이후**. fallback 시 동일 프롬프트(코드)가 다른 provider 클라우드로 전송됨을 인지 — egress 정책 대상(§6).

### 0.1 조직 모델 (사용자 은유 — 기능에 봉사하는 선에서만, "메타포 강제 금지")

| 역할 | 정체 | 권한 |
|------|------|------|
| **대표** | 사용자 | **최종 결정** (승인 게이트) |
| **사장** | 로컬 LLM + 결정적 오케스트레이터 | 작업 수령·계획·분배·결과 검토 |
| **워커** | claude/codex/opencode … CLI 에이전트 | 작업 수행, **격리 환경에서**, 언제든 교체 |

- ~~사장↔워커 의논 = 3+1 합의 자동화~~ **(삭제, B-5)**: 단일 사장은 독립성이 없어 3+1 교차검증과 동형이 아니며 단일 실패점. 사장↔워커는 "위임+검토"이지 "독립 합의"가 아니다. 자가진화 학습은 §8 별도 메커니즘.
- 워커 교체 = `feedback_provider_liquidity` 구현 (헌법 5조 비협상).

## 1. 확정 결정 (D-1~D-5)

| # | 결정 | 비고 |
|---|------|------|
| **D-1** | **사장 = 결정적 오케스트레이터(배관·라우팅·완료감지) + 판단 지점(작업 분해·워커 선택·결과 품질 평가)에서만 로컬 LLM 호출** | **하이브리드 재정식화(C-1)**. CLAUDE.md "계산적 검증 우선·추론적 보조" 동형. 순수 LLM-매-hop 폐기(지연·비결정·TDD 곤란) |
| **D-2** | 워커 = CLI 에이전트, **headless subprocess 우선** 구동·교체 (§3) | tmux=선택적 관전 |
| **D-3** | 개발 작업 MVP 중심, 비서 기능 후속 | 검증 용이 |
| **D-4** | 자가진화 = 깊게 지향, 무리면 중간. self-change = git+테스트+사람승인 게이트 + **immutable zone**(§8) | 비례성 |
| **D-5** | 제3안: 우리 얇은 오케스트레이터 직접 구축 + CAO 패턴 차용 + **OpenShell=안전 참조**(§6) | PoC 반영 |

## 2. 환경 실측 (2026-05-22, read-only)

| 항목 | 값 | 함의 |
|------|----|----|
| SoC | NVIDIA GB10 (Grace Blackwell, DGX Spark급) | 로컬 사장 구동 |
| 메모리 | 121GB 통합 (104GB 여유) | 용량은 충분 |
| **대역폭** ⚠️ | **~273GB/s LPDDR5X** | **decode는 memory-bound — dense 70B = 한자릿수 tok/s. MoE/적정크기 필수(§Q-1)** |
| 아키텍처 | aarch64 + Blackwell sm_121 | — |
| **CUDA** | **CUDA 13.0 toolkit(nvcc) 설치됨** | 빌드 환경 확보 → V-1 부분 de-risk |
| 보유 | tmux 3.4 · claude CLI · python3.12 · **bwrap** · **Landlock 활성 LSM(커널6.17)** · uv · openshell-CLI(venv) | 워커 구동 + 경량 격리 토대 |
| 미보유 | ollama / llama.cpp / vllm / landrun | 추론 런타임 설치 필요(§7) |

## 3. 통신 = headless subprocess 우선 (tmux=관전용)

- **1급 = headless subprocess**: `claude -p --output-format json` / `codex exec` 등. **exit code = 결정적 완료신호**, json = 출력 + `total_cost_usd`(비용신호 공짜). send-keys 타이밍·ANSI/alt-screen·idle 오탐·출력잘림 함정을 통째 회피. CLAUDE.md "계산적 검증 우선" 부합.
- **tmux = 선택적 관전 래퍼**: 사용자가 작업 화면을 보고 싶을 때(human attach)만. 완료감지를 tmux에 의존하지 않음.
- **fallback**: headless json 미지원 provider는 idle-pattern watchdog(CAO 차용) 보조.
- **§3 정정(C-2)**: "provider liquidity가 tmux를 강제"는 **과장**. provider 교체 = "다른 바이너리를 headless 호출"로 동일 충족 — tmux 불필수.

## 4. 제3안 — 차용 전략

CAO(awslabs/cli-agent-orchestrator, Apache-2.0, Python): **provider 추상(`base.py`)** 차용. handoff/assign 프리미티브 참고.
- **MVP 차용원 = CAO provider 추상**으로 한정.
- **후속 메모(DIV-2)**: multi-agent-shogun의 file-queue(zero coordination cost)는 *후속 다중워커 층* 검토 대상(feudal 메타포 주의). DIV-1로 통신이 headless면 SQLite/file-queue의 MVP 필요성 약함.

## 5. MVP 척추 (2단계 분리, C-6)

### MVP-0 (척추 증명 — 로컬 모델 없이)
```
대표 작업 입력
   │
[사장: 결정적 배관 + 판단지점 LLM(MVP-0은 claude로 대체 가능)] 계획·워커 선택
   │  headless subprocess (claude -p --output-format json)
   ▼
[워커 CLI] ← §6 격리 작업디렉터리에서 실행
   │  exit code + json = 완료/출력/비용
   ▼
[사장] 결과 검토 (무비판 수용 금지 — §6)
   ▼
[대표] 보고·승인/반려  ← 사람 결정 게이트 = "반영 전"(Q-6 잠정 결정 v3-2)
```
- 증명: ① 결정적 배관 ② headless 워커 분배 ③ provider 교체(인터페이스, 실 fallback은 후속) ④ 사람 게이트 ⑤ **워커 격리(§6)**.
- **게이트 위치 = "반영 전"(Q-6 잠정 v3-2)**: 워커는 격리 작업디렉터리에서 *자유롭게* 작업(착수마다 승인 불요 = 개입 최소화) → 사장 검토 → **결과를 워크스페이스/메인에 *반영*(merge·commit·apply)하기 직전 1회 대표 승인**. §8 self-change 게이트("commit→테스트→사람승인 반영")와 동형. 착수-전 게이트는 매 작업 승인 = 개입 과다로 *기각*. (확정 = 재합의/구현 단계)
- **사장 호출도 추상(A-7/C-4)**: 사장 LLM 호출 = provider 추상 대상(Ollama OpenAI-호환 endpoint). 사장도 교체 가능해야 헌법 5조 일관. MVP-0은 claude로 대체 → MVP-1에서 로컬로 교체.
- **⚠️ MVP-0 내부 의존 순서 (v3-1, 검토 지점 1)**: 증명 ⑤(워커 격리)는 **V-2(§7) 통과에 의존** — V-2 미실증 상태로 MVP-0 전체를 짜면 격리 부분만 미검증 stub. 따라서 MVP-0 = **2-트랙 시퀀싱**:
  - **트랙 A (격리-직교 골격)**: 결정적 배관 + headless subprocess 분배(증명 ①②③) + 사람 게이트(④) + 무비판수용 금지 가드(결정적 패턴 검토). **V-2 없이 TDD 선행 가능** — 워커는 잠정적으로 비격리 작업디렉터리(`git worktree` 분리)에서만 실행.
  - **트랙 B (격리 발효) — ✅ V-2 de-risk 완료(v4-4)**: V-2 통과(Landlock 단독 충분 실증) → 트랙 A의 작업디렉터리 실행을 격리 실행으로 *교체*(증명 ⑤ 완성). 트랙 A 인터페이스가 격리 backend를 주입받도록 설계(격리 = 교체 가능 의존성). 격리 backend = 검증된 `ll_sandbox` path_beneath 패턴.
  - 두 트랙 순서는 자유(A 먼저/B 먼저/병렬)이나 **MVP-0 *완료* 선언 = 트랙 B 통합까지** — "골격만 = MVP-0 부분 완료".
- **범위 밖**: 로컬 사장 모델 / 실 fallback / SQLite(과설계) / 다중턴 의논 / 다중워커 병렬 / 자가진화 발효 / 넓은 비서.

### MVP-1 (비전 시연 — 로컬 사장 교체)
- 사장 LLM을 **로컬(Ollama+MoE 모델)**으로 교체 (V-1 통과 후). "인터넷 비종속" 핵심 비전 시연.

## 6. 안전 모델 — 워커 격리 (🔴 BLOCKING 해소, B-2/B-6/A-7)

> **워커 실행경계는 "후속 층"이 아니라 MVP 첫 실행 전제.** MVP 자체가 워커에 실행 권한을 부여하므로(증명 ②), 격리 없는 MVP = thin=unsafe 함정.

- **격리 수단 = Landlock 단독 충분(무권한 환경) + bubblewrap 조건부** (OpenShell=참조only, k3s 회피 — PoC findings, 비례성). 워커 본인 제작사도 경량 격리: Claude Code=bubblewrap, Codex=Landlock+seccomp. **✅ V-2 실증 완료(v4)**.
  - **Landlock**(커널6.17 ABI 7, userns·root 불요): 워커당 **작업디렉터리만 read/write**, 그 외 fs 차단. **V-2 실증**: 직접 Landlock C(`ll_sandbox`, path_beneath)로 workspace RW / 프로젝트 소스·`~/.ssh` 읽기 차단 / 밖 쓰기 차단 = deny-by-default 동작 확인. **추가 권한 0**(24.04 AppArmor userns 제한과 무관). landrun/go 불요. (net 포트 제한 ABI4는 후속)
  - **bubblewrap = 조건부(v4-2)**: 이 머신 24.04 `apparmor_restrict_unprivileged_userns=1` + bwrap 비-setuid → **무권한 동작 불가**(V-2: `uid map: Permission denied`). mount/pid ns가 *꼭* 필요하고 권한 작업(sudo/AppArmor 프로파일)이 허용될 때만 보완. **무권한 환경 기본 = Landlock 단독.**
  - **✅ 이중격리 순이득 확정(v4-3, v3-3 측정 완료)**: claude.exe strings = `apt install bubblewrap` → **워커(claude) 자체 sandbox도 bwrap 의존 → 이 머신에서 동일하게 막힘**. 따라서 우리 외부 Landlock = 사실상 **유일한 실효 워커 격리** + 커널 강제(워커 침해·prompt injection으로 워커가 자기 sandbox를 꺼도 유효). **중복 아님 → 강등 불요, Landlock 채택 확정.** 비용 ~110줄 C wrapper = 비례 적합.
- **무비판 수용 금지**: 사장은 워커 출력을 결정적 가드로 검토(파괴적 명령 패턴·diff 검토) 후 대표에 보고. prompt injection 체인 차단.
- **OpenShell 참조 개념**: deny-by-default 정책 모델 / Privacy Router(로컬 vs 프론티어 라우팅) / skill 검증 + 정책변경=승인. 통째 채택(k3s)은 비례 초과로 미채택.

## 7. 별도 선결 검증 (V-1=MVP-1 직교 / V-2=MVP-0 트랙 B 선결, v3-1 정정)

> **v3 정정**: V-1·V-2가 *동등하게* "직교"는 아니다. **V-1 = MVP-1(로컬 사장) 블로커**(MVP-0는 claude 사장이라 불요). **V-2 = MVP-0 트랙 B(격리 발효) 선결**(증명 ⑤ 의존, §5). MVP-0 트랙 A(골격)는 둘 다 없이 진입 가능.

- **V-1 (MVP-1 선결, MVP-0 직교)**: 로컬 추론 런타임 PoC. **vLLM 제외**(GB10 sm_121 aarch64 미동작, vllm #36821). 후보 = **Ollama**(NVIDIA 파트너십, out-of-box) / llama.cpp(sm_121 빌드). **CUDA13 toolkit 보유로 부분 de-risk** — 잔여 = 런타임 구동 + 모델 tok/s 실측.
- **V-2 (MVP-0 트랙 B 선결) — ✅ 완료(v4)**: Landlock 워커 격리 **실증 완료**(직접 Landlock C, ABI 7 — 작업디렉터리 격리·deny-by-default 동작) + bubblewrap unprivileged = **무권한 불가 확인**(24.04 제한) + **이중격리 순이득 확정**(claude 자체 sandbox=bwrap 의존→막힘→외부 Landlock 유일 실효). **트랙 B 격리 backend 설계 위험 해소** → MVP-0 트랙 B 통합 시 `ll_sandbox` path_beneath 패턴 재사용. 상세 = [[jarvis-safety-layer-poc-findings]] §6.

## 8. 자가진화 안전 모델 (🔴 immutable zone, B-1)

- 3단 점진(C-5): **Layer 0 메모리 누적(read-only 학습 — 코드/프롬프트 변경 0, 게이트 불요, 최안전, ADR-011 T1 정합) → Layer 1 워커 프롬프트/skill 갱신(중간) → Layer 2 코어 자기수정(깊음)**. MVP = Layer 0만.
- self-change(Layer 1/2) = **git commit → Layer1 lint / Layer2 테스트 / Layer6 사람리뷰 → 대표 승인** 통과해야 반영.
- **🔴 immutable zone**: `tests/ · 게이트 로직 · git hooks · CI config · 본 §8 안전모델 문서`는 self-change 범위 **제외**. 피검증자가 검증자를 수정하면 green washing(거짓 안전감) → 차단. MVP에서 루프 미발효라도 게이트 *정의*는 명문화.
- 비례성: 하드웨어 서명 등 과잉 인프라 불요(`feedback_proportionate_security_personal_tool`).

## 9. 결정 항목 (3+1/사용자 몫 — 본 brief 결정 안 함)

| # | 항목 | 후보 | 비고 |
|---|------|------|------|
| Q-1 | **로컬 사장 모델** | **Qwen3.x-A3B/A10B(MoE)** 또는 30B이하+양자화. 조사: Qwen3.6-35B-A3B(SWE-bench 73.4%) | **대역폭 적합형 + tok/s 실측 기준**(A-3). 하드코딩 금지(config 교체) |
| Q-2 | **추론 런타임** | **Ollama**(유력) / llama.cpp | vLLM 제외 |
| Q-3 | **통신** | **headless subprocess(1급)** / watchdog(fallback) / tmux(관전) | §3 |
| Q-4 | **Worker 추상** | `Worker`(spawn/send/capture/done) — **CLI 백엔드 + OpenAI-endpoint 백엔드 둘 다 수용** | CLI=실행에이전트, endpoint=순수추론(역할 차이) |
| Q-5 | **provider 라우팅** | claude 우선 → fallback. **MVP=수동/설정**, 자동감지=후속 | 표준 신호 없어 fragile |
| Q-6 | **대표 게이트 위치** | **잠정 결정 = "반영 전"**(v3-2). 착수-전 = 매 작업 승인=개입 과다 *기각* / 양쪽 = 후속 옵션 | §8 동형·개입 최소화. 확정은 재합의/구현 단계 |
| Q-7 | **자가진화 첫 지점** | **Layer 0 메모리 누적** → 프롬프트 → 코어 | §8 |
| Q-8 | ~~언어/패키징~~ | **확정 = Python** (D-5 CAO 차용으로 사실상 결정) | 강등(CON-4) |
| **Q-9** | **워커 격리 구현** | **✅ V-2 실증 = 직접 Landlock C(landrun 불요), 작업디렉터리 격리 동작**. bwrap=조건부. net 정책=후속(ABI4) | 신규(§6 BLOCKING) / V-2 완료 |

## 10. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 |
|------|------|
| (A) | 본 v4 **재합의**(BLOCKING 5 + v3 의존순서/게이트 + v4 V-2 결과 확인 — 단축 Reviewer-only 가능) 또는 **구현 진입 승인** |
| (B) | **MVP-0 트랙 A 구현 진입**(격리-직교 배관/headless 골격 TDD) — 즉시 가능(§5 v3-1) |
| (C) | ~~V-2 PoC~~ **✅ 완료(v4)** — Landlock 단독 충분·이중격리 순이득 확정 |
| (D) | commit / push / 세션 정리 |

- ⚠️ TDD 코드 구현 = 본 v4 승인 + (재합의 통과) 후. BLOCKING 5(§2·Q-2·Q-1·§6·§8) 반영 완료 = 구현 진입 게이트 충족. **v3·v4 추가**: MVP-0 = 트랙 A(즉시 진입 가능)+트랙 B(**V-2 de-risk 완료**). Q-6 게이트 = "반영 전" 잠정 확정. **트랙 B 격리 backend = 검증된 `ll_sandbox` 패턴.**

---

## 부록 — 답습 + 금지

**출처**: [[3plus1-consensus-2026-05-22-jarvis-orchestrator-mvp]] (12 修正) / [[jarvis-safety-layer-poc-findings]] / 웹 조사(Devin·Codex·Claude Code·OpenShell·경량 sandbox) / 환경 실측 / 헌법 5조.

**금지 (영구 답습, 본 brief 0건)**: 코드 작성(orchestrator·provider·라우팅·격리) / 런타임(ollama/llama.cpp) 설치 / 로컬 모델 다운로드 / Landlock·bubblewrap 워커 격리 실 구현 / OpenShell k3s 게이트웨이 배포 / git hook·CI·skill 실 구성 / 사장 모델 결정 고정(Q-1) / 런타임 결정 고정(Q-2) / 자가진화 자동 발효 / commit·push / 5 영구 핵심 제약·Provider Liquidity 약화 / 보안 거버넌스(credential/4축/BI-*) 자동 재개.
