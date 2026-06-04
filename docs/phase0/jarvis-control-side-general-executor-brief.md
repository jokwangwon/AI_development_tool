# Jarvis 제어측 brief v2 — 일반 명령 실행 에이전트 (slice-1: 프로세스 제어)

> **v2 (2026-06-04)**: 풀 3+1 합의 **REVISE(조건부 승인)** 반영. 합의 보고서 = `docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md`. 주요 변경 = slice-1 분할(1a probe / 1b lifecycle) · `/health` 의존 제거(실측) · seam 코드 강제 · provenance 상속 · 빈도+누적 2축 · capability 등급 분리 · C-1 launcher 추상. §0.5·§5·§7·§9 갱신.

> **답습**:
> - `docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md` §3.5 (관제=보기+제어, 리스크 비례 게이트)
> - `docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md` §3 (통합 BLOCKING X-1·X-2·X-3) + §6 U-1~U-4
> - 메모리: `[[project_jarvis_general_executor_northstar]]` · `[[project_jarvis_local_boss_direction]]` · `[[project_jarvis_collaborative_orchestration]]` · `[[project_jarvis_controlled_child_then_friday]]` · `[[project_minimize_user_intervention]]` · `[[feedback_provider_liquidity]]`
>
> **북극성 (사용자 명시, 2026-06-04)**: *"내가 지금 Claude에게 아이디어·조건·명령을 주면 수행되듯 — Jarvis도 내 명령을 받아 어떤 프로젝트든 만들고·고치고·관리·실행해주는 것."* voice_lab = **하나의 예시/모티브**(scoping anchor 아님), Claude가 일하는 방식 = 레퍼런스 모델.
>
> **핵심 명제**: "Claude처럼 수행"의 핵심 갭 = **③ 실행 도구**(프로세스 제어·코드 편집·쉘·파일) = **제어측**. 합의가 일부러 DEFER했던 영역이며, 진입 조건 = **U-4 trigger(사용자가 당김 ✅) + 별도 풀 3+1 + X-1·X-2·X-3 해소**. 본 brief가 그 해소안을 구체화한다.
>
> **다음 단계**: ✅ brief 검토 ✅ 풀 3+1 합의(REVISE) → **BLOCKING B-1~B-6 반영(본 v2)** → **slice-1a TDD**(포트 LISTEN probe, 자율). slice-1b(lifecycle)·slice-2+ 는 설계만, 구현 DEFER.
>
> **자동 진입 0** — slice-1a TDD·1b 진입 등 각 단계는 사용자 명시 후에만.

---

## 0. 이 brief가 생긴 이유

읽기측 링크 허브(패턴1)는 #128에서 구현 완료됐다(voice_lab = 첫 카드). 그러나 그건 **"입구"만** 제공한다(클릭 → 외부 열림, 제어·자격증명·게이트 0). 사용자가 3회에 걸쳐 보충한 목표는 그보다 크다:

1. *"voice_lab을 만들고·관리하고·수정하고·상호작용"* — 읽기 넘어 **제어**.
2. *"voice_lab 뿐 아니라 내가 Claude에게 하듯 명령을 수행"* — **일반 실행 에이전트**.
3. *"voice_lab은 하나의 예시 — Claude로 만든 것/일하는 방식을 모티브·레퍼런스로 방향 보충"*.

합의(2026-06-02) §6 U-4: *"제어측 진입 trigger = 명시 trigger 전 DEFER가 기본값. 사용자가 지금 trigger를 당기면 별도 풀 3+1 즉시 가동."* → **사용자가 지금 당겼다.** 본 brief는 그 풀 3+1의 입력이다.

---

## 0.5 합의 반영 (v2, 풀 3+1 REVISE)

판정 = **REVISE(조건부 승인)**. 방향 건전 + 기존 코드 선례 실재(ApprovalGate·PlanController seam 패턴·select_ports allowlist·external_registry provenance). 단 아래 **BLOCKING 충족 후** slice-1a 진입.

**BLOCKING (TDD 진입 전 필수)**:
- **B-1 seam 코드 강제** — controller 공개표면 = propose-only, 실제 집행(`_execute`)은 등급·빈도·승인 통과 시 *내부에서만* 호출. "boss 직접 집행 차단"을 **우회불가 단위테스트**로 고정(문서 약속 불충분). `ApprovalGate`(default-deny+fail-closed, `approval.py:41-47`) 패턴 답습.
- **B-2 provenance 상속** — 제어 대상도 `origin=="jarvis"` fail-closed(`external_registry.py:83`). 제어측 > 읽기측 위험 → 약화 = §1.5 비협상 회귀.
- **B-3 빈도+누적 2축 + 동시 1인스턴스** — rate 단독 금지(슬라이딩 윈도 리셋 우회 + 단발 비가역 GPU OOM/디스크).
- **B-4 `/health` 의존 제거** — voice_lab에 `/health` 실존 안 함(코드 전수 확인). probe = **포트 LISTEN 확인 + HTTP 선택적(주입형, 부재 시 LISTEN-only degrade)**.
- **B-5 등급 = 원시 연산/capability 바인딩** — 동작 *이름 문자열* 아닌 실제 연산(spawn/signal/probe)에 등급 부착(위장 차단).
- **B-6 controller 자격증명 0 단위테스트** — controller env에 토큰류 부재 assert + `_SENSITIVE_NAMES` 등재(slice-4 자격 미끄럼 방지 센서).

**합의 결정 (갈림길)**: C-1 = (a)본체모듈+launcher 추상(독립데몬 기각) · C-2 = **초기 1-클릭→자율 완화(사용자 확정)** · slice 분할 = 1a(probe)→1b(lifecycle) · C-4 = external_registry 확장+제어필드 분리+provenance 상속(별도 신설 기각) · 등급 = capability 한겹 분리.

**비BLOCKING(개선)**: controller 크래시 fail-closed(다운=모든 dispatch 거부) · 동시 race per-target lock · 부분 실패 자동 롤백 금지(통제 보존) · boss 페이로드 strict 검증+argv(쉘 미경유) · LedgerLog append-only 감사(Rollback Trigger 검출).

---

## 1. 레퍼런스 모티브 — Claude Code가 명령을 수행하는 방식 (능력 역설계)

"Claude처럼"을 막연한 비유로 두지 않고, Claude Code가 한 턴에 하는 일을 능력으로 역설계한다. (voice_lab을 *그 예시*로: 이번 세션에서 Claude가 사용자의 "사람다움 루프 강화" 명령을 어떻게 수행했는가.)

| Claude의 동작 | 이번 voice_lab 세션의 실제 예 |
|---|---|
| ① 자연어 명령 수신 | "1번(사람다움 루프)으로 진행" |
| ② 컨텍스트 파악 + 계획 | 코드 읽기 → 설계 질문(AskUserQuestion) → 결정 |
| ③ **실행 도구**: 파일 편집·쉘 실행·**프로세스 제어** | Edit(server.py/index.html) · Bash(문법검증) · **8777 서버 kill+재기동** |
| ④ 검증 | py_compile · node --check · 실 API 호출 검산 |
| ⑤ 리스크 판단 + 사람 확인 | 서버 재시작 전 사용자 확인, 커밋/push 전 확인 |
| ⑥ 보고 | 변경 요약 + 검증 결과 + 다음 후보 |

**관찰**: ②④⑥은 자비스에 部分 존재(사장 plan-then-execute, contract/did_act, HUD 보고). **③ 실행 도구가 0건** — 특히 이번 예시에서 Claude가 한 "서버 kill+재기동"은 자비스엔 대응 능력이 없다. **slice-1이 정확히 이 ③의 첫 조각(프로세스 제어)을 채운다.**

---

## 2. 능력 맵 — "Claude처럼 수행"의 현 상태 / 갭

| # | 능력 | 현 상태 | 갭 |
|---|---|---|---|
| ① 명령 수신 | 대화 라우팅(`conversation-task-routing`), HUD 입력 | 명령→작업 변환 정련 필요 |
| ② 계획 | ✅ 사장(ollama) plan-then-execute (stone1a), untrusted proposal + 사람승인 | — |
| ③ **실행 도구** | ❌ **제어 채널 0건** | ★ **핵심 갭 — 본 brief 대상** |
| ④ 검증 | 部分 — artifact contract, did_act, fs-delta | 도구 실행 후 관찰 루프 |
| ⑤ 리스크 게이트 | §3.5 設計됨, 미구현 | 결정적 등급 테이블 + dispatch seam |
| ⑥ 보고 | 部分 — HUD | 실행 결과 피드백 |

**결론**: ③+⑤가 같이 가야 한다(실행 도구엔 반드시 게이트가 붙는다). slice-1 = ③의 첫 도구(프로세스 제어) + ⑤의 결정적 등급 테이블 동시 구축.

---

## 3. 제어측 = 보기 + 제어, 리스크 비례 게이트 (§3.5 답습)

```
            자비스 전권 통제 (넓은 범위)
                      │
        ┌─────────────┴─────────────┐
    가역·저위험                 비가역·고위험
 (health·재실행·리터치)      (배포·삭제·자격증명·과금)
        │                           │
    ▶ 자율 집행                 ▶ 사람 승인 게이트
 (개입 최소화 목표)            (통제된 자식 보존)
```

- 등급 분류 = **결정적 정책 테이블**(LLM 판단 아님 — 동작 종류 → 등급 매핑). 계산적 검증 우선(CLAUDE.md §2). 미등재 동작 = **보수적 고위험 + 사람 회부(fail-closed)**.
- 게이트는 §3.5 그대로 답습. 본 brief는 이를 *집행 가능한 seam*으로 구체화한다(합의 X-2: "문서상 정책에 그치지 않게").

---

## 4. 통합 BLOCKING 답습 — X-1 / X-2 / X-3 (합의가 결정한 해결 방향)

합의 §3이 이미 해결 *방향*을 못박았다. 본 brief는 이를 구현안으로 구체화하되 **재론하지 않는다**(비협상).

| # | BLOCKING (비협상) | 합의 해결 방향 | slice-1 적용 |
|---|---|---|---|
| **X-1** | 자비스 본체 자격증명 보유 금지 | **C-β**: 외부가 자기 자격 보유, 자비스↔외부 = 로컬 토큰 1개. 부득이 보유 시 본체 메모리 밖 + `_SENSITIVE_NAMES` 등재 | slice-1 대상 = **localhost 로컬 프로세스(자격증명 없음)** → X-1 부담 최소. 단 설계는 자격 보유를 코어에 굽지 않음(일반화 대비) |
| **X-2** | 제어 채널↔격리 충돌 + 게이트 집행 seam 부재 | 제어측 = **HTTP API로 좁힘**(격리 정합). **단일 결정적 controller**가 외부 dispatch 게이트 신설(**boss 직접 호출 차단**). 빈도/누적 게이트 코어 고정 | §5 controller 아키텍처가 이를 집행. boss 는 controller에 *제안*만, controller가 등급·빈도 검증 후 집행 |
| **X-3** | 등급 매핑 = 코어 고정만, G6(b) self-선언 기각 | **G6(a)만**: 코어 고정 allowlist(`select_ports` 패턴 답습 — 미등재=고위험 fail-closed) | §5 등급 테이블이 코어 소유. 외부형 manifest 자기 등급선언 ❌ |

> ⚠️ **slice-1의 X-2 정면 충돌(설계 핵심 난점)**: "정지된 서버 start"는 본질상 프로세스/CLI 동작이라 HTTP로 부를 수 없다(서버가 죽어 있으니). → §5의 **로컬 controller(프로세스 lifecycle 소유, 자비스엔 HTTP 노출)**가 이 충돌의 해소책. controller는 격리 boss 밖에서 동작하는 결정적 집행자다.

---

## 5. slice-1 구현 범위 — 프로세스 제어 도구 (1a → 1b 분할)

합의 DI-2: slice-1을 **1a(읽기성 probe, 자율)** → **1b(lifecycle, 게이트)** 로 분할. 1a를 먼저 박아 골격·seam을 가장 안전한 동작으로 검증하고, **1b 게이트 임계(C-3)를 1a dogfood 실측으로 확정**. 1b는 1a 관찰 후 사용자 명시 진입(자동 진입 0).

### 5.1 아키텍처 (X-2 해소)

```
 사용자 명령
    │
    ▼
┌────────────────┐  제안(untrusted, argv·enum)  ┌──────────────────────────────┐
│ 자비스 본체/사장 │ ───────────────────────────▶ │ ProcessController (결정적)       │
│ (boss LLM, 격리)│                              │ 공개표면 = propose() only (B-1) │
│  ※ _execute 접근X│ ◀─────────────────────────── │ - Action→capability→등급(코어)  │
└────────────────┘   결과/상태                   │ - rate+누적 2축 + 동시1인스턴스  │
                                                 │ - provenance(origin==jarvis)   │
                                                 │ - 고위험/미등재 → 사람 승인     │
                                                 │ - append-only 감사(LedgerLog)  │
                                                 │ - _execute(): launcher 통해서만 │
                                                 └────────┬─────────────────────┘
                                          HTTP/포트 LISTEN │ Launcher (subprocess | systemd-run 주입)
                                          (probe, 읽기)    ▼   per-target lock
                                                  대상 시스템 (예: voice_lab :8777/:8778)
```

- **B-1 seam 코드 강제**: boss는 controller `propose()`만 호출 가능. 실제 집행 `_execute()`는 **private/별도 모듈**이라 boss가 직접 못 부른다 — 등급·provenance·빈도·승인 통과 시 controller 내부에서만 호출. `ApprovalGate`(default-deny+fail-closed, `approval.py:41-47`) 동형. **우회불가능성을 단위테스트로 고정**(문서 약속 ✗).
- **boss 페이로드 = untrusted**: 대상 이름 allowlist + 인자는 enum/구조화만, **쉘 문자열 금지(argv 리스트)** — controller 단계가 새 injection 표면(GP-6).
- **C-1 = (a) 본체 내 모듈 + Launcher 추상**: lifecycle 집행을 `Launcher` 인터페이스(기본 `subprocess`, `systemd-run` 주입형)로 두어 (a)→systemd 전환을 코드 변경 0. GB10 systemd 미확인을 비차단화. **독립 데몬 기각**(과설계). detach(`setsid`)로 본체 종료 시 고아화 방지.
- **controller 크래시 = fail-closed**: controller 다운 시 모든 dispatch 거부(open-fail 금지, GP-3).
- **자비스↔controller = 로컬 토큰 1개**(X-1 정합). controller는 **자격증명 0**(B-6 단위테스트로 고정).

### 5.2 동작 → capability → 등급 (코어 고정, X-3 + B-5)

등급을 동작 *이름 문자열*이 아닌 **실제 원시 연산(capability)**에 바인딩(위장 차단). `Action(name, capabilities=frozenset)` → 코어가 capability 조합 → 등급 매핑(`select_ports` permission→port 패턴 답습). 대상 추가 시 코어 테이블 수정 0 → Provider Liquidity 보존, slice-2+ capability 모델 무손실 확장(G6(a) 위반 0).

| slice | 동작 | capability | 등급 | 게이트 |
|---|---|---|---|---|
| **1a** | `health` / 상태 | `probe`(읽기) | 저 (가역) | 자율 |
| **1b** | `restart` | `signal`+`spawn` | 중 | **초기 1-클릭 → dogfood 후 자율 완화**(C-2 사용자 확정) |
| **1b** | `start` / `stop` | `spawn` / `signal` | 중 | 〃 |
| — | 미등재 동작 | (unknown) | **고 (fail-closed)** | **사람 승인 필수** |
| (slice-2+) | 코드수정·쉘·배포·삭제 | mutate/egress/irreversible | 고 | 사람 승인 (§6 설계만) |

- **B-4 probe**: voice_lab에 `/health` 실존 안 함 → probe = **포트 LISTEN 확인**(stdlib socket) **+ HTTP GET 선택적**(엔드포인트 registry 주입, 부재 시 LISTEN-only degrade). health probe host = **localhost 한정 코어 고정**(SSRF 차단).
- **B-3 빈도+누적 2축**: rate(슬라이딩 윈도) **+ 절대 누적 총량** + **동시 1인스턴스 강제**(start 시 기존 PID 있으면 거부/회부). rate 단독 = 리셋 우회 + 단발 비가역(GPU OOM/디스크) 못 막음.
- **per-target lock**(GP-4): 동시 lifecycle 변경 직렬화. **부분 실패 자동 롤백 금지**(GP-5) — 사람 회부.

### 5.3 첫 적용 대상 = voice_lab (예시)

voice_lab :8777(GPT-SoVITS)·:8778(Qwen3). 이번 세션에서 Claude가 수동으로 한 "PID 정확 종료 → 포트 해제 대기 → 재기동"(pkill 금지·bind 충돌 교훈)을 1b controller의 결정적 절차로 박는다(레퍼런스 모티브 ③의 자동화).

- **B-2 provenance 상속**: 제어 대상은 `external_registry` 의 `origin=="jarvis"` fail-closed를 **상속**(`external_registry.py:83`). origin 불명 = 제어 대상 아님.
- **PID 소유권(GP-2)**: controller가 **소유한 PID에만** signal. 미소유 기존 프로세스(예: 현재 도는 502419)는 **사람 회부**(또는 포트→PID 역추적 후 명시 인수 게이트). controller 미기동 프로세스 관제 = fail-closed.
- **코드 하드코딩 0**: 대상 = registry 엔트리(launch cmd/cwd/port/pid 파일/probe 경로). 등급은 capability에 묶여 대상별 코어 수정 불요.

---

## 6. slice-2+ — 설계만, 구현 DEFER

| slice | 능력 | 엔진 | 게이트 | 상태 |
|---|---|---|---|---|
| 2 | **코드 수정** | 사장 계획 → claude 워커가 대상 repo 편집 → contract + diff | 코드편집=가역(저~중), **push/배포=고(사람 승인)** | 설계만. stone 디딤돌(artifact-contract) 재사용 |
| 3 | 쉘/파일 실행 | controller 결정적 dispatch | allowlist + 격리 | 설계만 |
| 4 | 배포/삭제/자격증명 | — | **항상 고위험·사람 승인** | 설계만. X-1 재설계 필요(C-β 한계) |

→ slice-2+ 는 slice-1 dogfooding 관찰 후 각각 별도 trigger + (필요 시) 추가 합의.

---

## 7. 갈림길 — 결정됨 (합의 + 사용자)

| # | 갈림길 | **결정** | 주체 |
|---|---|---|---|
| G5 | 제어 채널 형태 | HTTP(probe, 읽기) + controller Launcher(lifecycle). Launcher가 subprocess/systemd-run 흡수 | 합의 재확인(불변) |
| G6 | 등급 매핑 소유권 | **코어 고정(G6(a))** + capability 한겹 분리 | 합의 |
| **C-1** | controller 프로세스 형태 | **(a) 본체 내 모듈 + Launcher 추상**(기본 subprocess, systemd-run 주입). (b) 독립 데몬 기각 | 합의 |
| **C-2** | restart/start 기본 게이트 | **초기 1-클릭 → dogfood 후 자율 완화** | **사용자 확정** |
| **C-3** | 빈도/누적 임계 | **2축 구조 + 동시 1인스턴스 고정.** 임계 *수치*는 1a dogfood 실측 후 | 구조=합의 / 수치=사용자(1a 후) |
| **C-4** | 대상 등록 | **external_registry 확장 + 제어 필드 분리 dataclass + provenance 상속.** 별도 신설 기각 | 합의 |
| slice | 범위 | **1a(probe, 자율) → 1b(lifecycle, 게이트)** 분할 | 합의 / 1b 진입 사용자 명시 |

**U-1~U-4 현 상태**:
- **U-1**(전권 강도): 발화로 "제어 능력 희망" 확인 — 점진(slice 분리)로 수용.
- **U-2**(본인 작품?): voice_lab = **사용자/자비스 작품 ✅** → C-β 성립(외부 자격 자체 보유 가정 유효). 제3자 SaaS 아님.
- **U-3**(registry 형태): (b) 단일+source 권고. C-4에서 확정.
- **U-4**(제어측 trigger): **당겨짐 ✅** → 본 brief + 풀 3+1 가동.

---

## 8. Provider Liquidity 준수 + 검증 / Rollback Trigger

- **Provider Liquidity(헌법 5조-2, 비협상)**: controller·등급 테이블·제어 채널은 **사장 LLM·워커 CLI·모델 교체와 무관**해야 한다. boss는 controller에 *제안*만 → boss 구현체(ollama→다른 모델) 교체 시 controller·게이트 코드 변경 0. 대상 시스템도 registry 엔트리로 주입(코드 하드코딩 0). [[feedback_provider_liquidity]]
- **검증(센서, BLOCKING 대응)**: capability→등급 = 결정적 단위테스트(미등재→고위험 fail-closed, B-5). **B-1 seam 우회불가 테스트**(boss가 `_execute` 직접 호출 불가). **B-2 provenance fail-closed 테스트**(origin≠jarvis 거부). **B-3 2축+동시1인스턴스 폭주 차단 테스트**. **B-6 controller 자격증명 0 assert**. controller 크래시→dispatch 거부 테스트. 실 e2e(1a) = voice_lab 포트 LISTEN probe → 1b(후) health→restart→stop→start + 고위험 회부 경로.
- **Rollback Trigger (검출 센서 = LedgerLog append-only 감사, GP-7)**: (a) controller가 등급 우회로 고위험 자율 집행 1건 = 즉시 중단·재설계. (b) boss 제안이 게이트 없이 집행된 seam = X-2 회귀, 중단. (c) 빈도/누적 게이트 무력화로 외부 영향 = 중단. (d) controller가 자격증명 보유 = X-1 회귀, 중단. 감사 로그 없는 트리거는 문서상 약속 → 모든 dispatch 결정 append-only 기록.

---

## 9. 합의 결과 + 진행

- ✅ **풀 3+1 합의 완료 — REVISE(조건부 승인)**. 보고서 = `docs/review/3plus1-consensus-2026-06-04-jarvis-control-side-slice1.md`. (A 구현·B 안전·C 대안 + Reviewer 코드 검증.)
- 본 v2 = BLOCKING B-1~B-6 + 갈림길 결정 반영.
- **다음 = slice-1a TDD**(포트 LISTEN probe + controller 골격 + capability 등급 + B-1 seam 테스트). 진입은 **사용자 명시 후**(자동 진입 0). 1a dogfood 실측 → C-3 임계 확정 → 1b(lifecycle) 별도 진입.
- **이 brief는 개념·설계 정리. 코드 변경 0.**
