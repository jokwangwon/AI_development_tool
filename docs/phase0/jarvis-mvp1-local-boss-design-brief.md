# Jarvis MVP-1 설계 brief — 로컬 사장(Boss LLM) 교체 + 판단 지점 도입 (DRAFT v2)

> **본 brief = 자비스 MVP-1 설계 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·런타임(Ollama) 설치·로컬 모델 다운로드·tok/s 측정 실행·config 변경** 을 발생시키지 않는다. 실 변경 0건. staged: brief v1 → **3+1 합의(APPROVE w/ COND, R1~R13)** → **brief v2(본 문서, 합의 반영)** → (트랙 A 구현 / V-1 PoC) → 트랙 B 통합. 코드 전 문서 먼저(SDD).

---

**작성일**: 2026-05-22 (세션 3)
**Status**: **DRAFT v2 — 3+1 합의(APPROVE w/ COND) R1~R13 반영, 구현 진입 가능**
**진입 단위**: 자비스 본연 기능 — MVP-1 (MVP-0 오케스트레이터 위 *로컬 사장* 발효)
**전제**: MVP-0 완료(HEAD `ed0df1b`, `tests/jarvis/` 50 green) — 결정적 배관 + headless 워커 + Landlock 격리 + "반영 전" 사람 게이트 동작.
**근거**: [[3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss]] (풀 3+1, APPROVE w/ COND) · [[jarvis-orchestrator-mvp-design-brief]] (v4 §5 MVP-1·D-1·Q-1·Q-2) · [[jarvis-safety-layer-poc-findings]] (V-1 미착수) · `project_jarvis_local_boss_direction` · `feedback_provider_liquidity` (헌법 5조) · `feedback_proportionate_security_personal_tool` (비례성) · `project_minimize_user_intervention`

## v2 변경 이력 (3+1 합의 R1~R13 반영)

| R# | v1 → v2 | 출처(Agent) | 등급 |
|----|---------|------|------|
| R1 | §4·§5 "green washing 구조적 차단" → "*기계적* flag 감산만 차단, *의미적* 우회는 못 막음 + 3중 방어 명시" | B | 🔴 |
| R2 | §4 `BossAdvice` = 텍스트 전용 frozen dataclass 명문화(콜백·경로·명령 필드 금지) | B·A | 🔴 |
| R3 | §5 advisory 실패 거동 = 게이트 진행(비차단) + **"Boss advisory 실패" 명시 경고**(fail-closed 정신) | B | 🔴 |
| R4 | §6·M3 **llama.cpp ↔ Ollama 동급**, **vLLM "제외" → "MVP-2 재검토" 강등**(C-2 충돌) | C | 🔴 |
| R5 | §6 tok/s 기대치(roofline+실측) + prefill·입력 상한 V1-3 측정 항목 | A·C | 권고 |
| R6 | §4 `BossAdvice.confidence` 삭제(LLM 자기보고=거짓 안전감) | C | 권고 |
| R7 | §3 `Orchestrator(boss=None)` 하위호환 + `ApprovalRequest.advice` 필드 | A | 권고 |
| R8 | §4 워커 실패 시 advise 미호출 | A | 권고 |
| R9 | §8 MVP-1 2-트랙(A=추상+advisory TDD / B=런타임) 명시 | C·A | 권고 |
| R10 | §4 사람은 결정적 flag + raw diff 직접 확인(Boss summary 종속 금지) | B | 권고 |
| R11 | §5 egress "*추론 시점* 0, 설치/pull/텔레메트리 별개" 한정 | B | 권고 |
| R12 | §1 advisory 트레이드오프(안전 최저 ↔ 비전 임팩트 최저) 명시 | C | 권고 |
| R13 | §3 LiteLLM 게이트웨이 = MVP-2 진화 경로 메모 | C | 메모 |

---

## 0. 위치 — MVP-0 가 남긴 간극

MVP-0 의 "사장"(`Orchestrator.dispatch`)은 **순수 결정적 배관**이다: 워커 선택(수동 alias)→workdir→headless run→결정적 가드(`ReviewGuard` 정규식)→사람 게이트→보고. **LLM 판단 호출이 0건**이다 — brief v4 D-1 의 "판단 지점에서만 LLM 호출"은 트랙 A 범위 밖으로 미루어졌다.

따라서 "MVP-1 = 로컬 사장 교체"는 한 줄로 보이지만 **세 가지가 묶여 있다**:

1. **판단 지점을 *처음* 도입** — 지금까지 없던 LLM 추론 hop 을 파이프라인에 추가.
2. **그 LLM 을 로컬로** — 클라우드가 아니라 Ollama+MoE 로컬 추론(비전: "인터넷 비종속").
3. **사장도 교체 가능** — Boss LLM = provider 추상(헌법 5조 동형). 로컬↔클라우드↔다른 로컬 모델 = config 교체, 코드 불변.

> **MVP-1 의 시연 목표 (비전)**: 토큰이 끊겨도/구독이 없어도 **사장이 로컬에서 돈다**. MVP-0 은 사장 자리에 클라우드(claude)를 대체로 끼울 수 있었으나, MVP-1 은 그 자리를 *로컬 모델*로 채워 "인터넷 비종속" 핵심 비전을 실증한다.

## 1. MVP-1 범위 정의 (포함 / 제외)

| 포함 (MVP-1) | 제외 (MVP-2+) |
|---|---|
| **Boss LLM provider 추상** (OpenAI-호환 endpoint, 교체 가능) | 다중 워커 병렬·오케스트레이션 |
| **판단 지점 1개 도입** = §4 (결과 검토 advisory) | 작업 분해(multi-step decomposition) |
| **로컬 런타임 연결** (Ollama, V-1 통과 후) | 자동 워커 라우팅(Q-5 자동감지) |
| **V-1 PoC** (런타임 + MoE 모델 + tok/s 실측) | 자가진화 Layer 1/2 발효 |
| advisory 가 결정적 가드·사람 게이트를 **약화 못 함** 보장 | 넓은 비서 기능 |

**범위 결정 원칙 (비례성)**: brief v4 가 나열한 판단 지점 3개(작업 분해·워커 선택·결과 품질 평가) 중 **MVP-1 은 "결과 검토 advisory" 1개만** 도입한다(§4). 이유: (a) 가장 낮은 위험(advisory=사람 게이트 보조, 실행 권한 0) (b) 가장 작은 표면(단일 hop, TDD 용이) (c) "로컬 사장이 돈다"는 비전 시연에 충분. 작업 분해·자동 라우팅은 다중턴/다중워커 표면을 열어 별도 단계.

**⚠️ 트레이드오프 명시 (R12, Agent C)**: advisory 는 **안전 위험이 최저인 동시에 비전 시연 임팩트도 최저**다 — 결정적 가드 위에 자연어 요약을 *덧붙이는* 가장 소극적 형태(사장이 "판단"하기보다 "거든다"). 첫 판단 지점으로는 여전히 옳으나(위험·표면 최소), "사장이 능동 판단"하는 더 강한 시연은 워커 선택·작업 분해(MVP-2)에서 온다는 점을 정직히 기록한다.

## 2. 확정 제약 (답습 — 본 brief 가 새로 정하지 않음)

| # | 제약 | 출처 |
|---|------|------|
| C-1 | **D-1 하이브리드**: 결정적 우선, LLM 은 판단 지점에서만. CLAUDE.md "계산적 검증 우선·추론적 보조" 동형 | brief v4 D-1 |
| C-2 | **Provider Liquidity (헌법 5조 비협상)**: Boss LLM = 교체 가능. 모델/런타임 = config, 하드코딩 금지 | `feedback_provider_liquidity` |
| C-3 | **사람 게이트 = "반영 전"** 유지. LLM 판단이 게이트를 대체/제거하지 않음 | brief v4 Q-6 / `project_minimize_user_intervention` |
| C-4 | **비례성**: 개인 단일 머신 툴. 과설계(분산 추론·다중 모델 앙상블·서명) 금지 | `feedback_proportionate_security_personal_tool` |
| C-5 | **immutable zone 불변**: tests·게이트 로직·가드·hooks·CI = Boss LLM 영향권 밖 | brief v4 §8 |

## 3. 아키텍처 — Boss LLM provider 추상

> **대칭 설계**: MVP-0 `Worker`(외부 *바이너리* 실행) 와 평행하게, `BossLLM`(외부 *추론 endpoint* 호출) 를 둔다. 둘 다 provider 교체 단위(헌법 5조). 차이 = Worker=실행 에이전트(부작용 있음, 격리 필요) / BossLLM=순수 추론(부작용 없음, 텍스트 in→텍스트 out).

```
BossLLM (Protocol)
  ├─ complete(messages) -> BossReply        # 순수 추론, 부작용 0
  └─ name: str                              # 교체 키
        ├─ OllamaBoss(endpoint, model)      # 로컬 (OpenAI-호환 /v1/chat/completions)
        ├─ OpenAiCompatBoss(endpoint, ...)  # 임의 OpenAI-호환(클라우드/타 로컬) — 교체 실증
        └─ (test) StubBoss(scripted)        # 주입, 결정적 테스트
```

- **OpenAI-호환 endpoint 로 통일**: Ollama 는 `/v1/chat/completions` 제공 → 클라우드/타 로컬과 *동일 인터페이스*. provider 교체 = endpoint+model 문자열 교체(C-2 충족). Boss 도 외부 LLM SDK 직접 import 최소화(가능하면 httpx/표준 HTTP — `worker.py` 가 "SDK import 0" 원칙 답습한 것과 동형). 2026 표준: Ollama·llama.cpp `llama-server` 모두 `/v1/` 내장.
- **config 주입**: 모델·endpoint·timeout = config(env/파일). 코드 상수 금지(`environment-and-docker-design` 하드코딩 금지 답습).
- **Orchestrator 통합 (R7)**: `Orchestrator.__init__(boss: BossLLM | None = None)` — 기존 `guard`/`gate`/`workdir_factory` 와 동일 생성자 주입. **`boss=None` 이면 advisory 없이 MVP-0 동작 그대로 보존(하위 호환 무파손)**. 판단 지점(§4)에서만 호출, 배관은 결정적 유지(D-1).
- **R13 메모(진화 경로, Agent C)**: 다중 provider 라우팅·fallback 이 필요해지면 **LiteLLM 게이트웨이**가 자연스러운 진화 경로(MVP-2) — 진짜 provider-agnostic 실현(헌법 5조). MVP-1 에서 도입은 별도 데몬·YAML = 과설계이므로 httpx 직접 채택, 진화 경로만 기록.

## 4. 판단 지점 설계 — 결과 검토 advisory (계산적 우선 / 추론적 보조)

현 파이프라인: `worker.run` → `ReviewGuard.review`(결정적 정규식) → `gate.request`(사람). MVP-1 은 **결정적 가드와 사람 게이트 *사이*에 LLM advisory 를 끼운다**:

```
worker.run → ReviewGuard(결정적, 권위/차단) → BossLLM.advise(advisory, 비차단) → gate(사람, 최종)
```

- **계산적 우선 (CLAUDE.md)**: `ReviewGuard` 정규식 flag 는 **여전히 권위**. LLM 은 그 위에 자연어 위험요약·diff 설명을 더해 *사람의 판단을 돕는다*.
- **🔴 fail-safe 불변식 (핵심 안전 속성)**: **LLM advisory 는 결정적 flag 를 *제거/완화*할 수 없다.** LLM 은 caution 을 *추가*만 가능(flag 0 인데 "위험해 보임" 경고 OK), *감산* 불가(flag 있는데 "괜찮음"으로 통과 불가). 즉 advisory 는 게이트를 **더 보수적으로만** 움직인다.
- **🔴 R1 — green washing 차단 범위 정직성 (Agent B)**: 위 합집합 불변식은 ***기계적* green washing(코드로 flag 를 지우는 경로)만 차단**한다. **막지 *못하는* 것**: 침해된 워커→Boss 가 flag 는 그대로 두되 `summary` 자유 텍스트에 "이 `rm -rf` 는 임시 디렉터리라 안전, 승인하세요"라 써서 **사람을 오도(*의미적* green washing)**. "구조적 차단"이라 단정하면 그 단정 자체가 거짓 안전감(CLAUDE.md). **3중 방어로 한정**: (a) 결정적 flag 를 Boss summary 와 **분리 표시** (b) 사람이 **raw diff 직접 확인**(R10) (c) `ReviewGuard` 정규식 권위 유지. advisory 는 보조이며 완전성을 주장하지 않는다(`review.py` 정직성 기조 동형).
- **R10 — Boss summary 종속 금지 (Agent B)**: 사람 게이트는 **결정적 flag + raw diff(또는 충분한 출력)를 직접** 보고 판단한다. 현 `ApprovalRequest.output_preview[:200]` 절단은 사람을 Boss 해석에 종속시킬 위험 → advisory 표시 시 결정적 flag·diff 를 Boss summary 와 별도로 노출.
- **advisory 는 자동 승인 안 함**: LLM 출력이 게이트를 *통과시키지* 않는다. 사람 게이트(C-3)는 그대로. advisory = 사람에게 보여줄 요약/플래그일 뿐.
- **🔴 R2 — `BossAdvice` = 텍스트 전용 frozen dataclass (Agent B·A)**: `BossAdvice(summary: str, extra_flags: list[str])` — **콜백·경로·명령 필드 금지.** "Boss 출력 실행 권한 0"을 산문이 아니라 데이터 모델 제약으로 강제: `Orchestrator.dispatch`/`ApprovalGate` 가 BossAdvice 로부터 **어떤 제어 흐름 결정도 자동 도출하지 않음**(게이트 통과·workdir·argv 에 영향 0)을 **테스트로 고정**. (R6: `confidence` 필드 삭제 — LLM 자기보고 confidence = injection 표적의 거짓 안전감, 게이트 결정에 무의미.)
- **데이터 흐름 (R7)**: `BossAdvice` → `ApprovalRequest.advice: BossAdvice | None = None`(frozen, default → 기존 호출부 무파손) 에 첨부. `flags = verdict.flags + [f for f in advice.extra_flags if f not in verdict.flags]`(합집합, 감산 불가 = 불변식 1줄 강제). 게이트 통과 결정은 **오직 사람 approver** — advice 는 표시용.
- **🔴 R8 — 워커 실패 시 advise 미호출 (Agent A)**: `result.is_error` 면 advise 를 호출하지 않는다(현 `orchestrator.py:83` early-return 위). 실패 출력에 LLM 비용/지연 낭비 + injection 표면 확대 회피.

## 5. 안전 모델 — Boss LLM 도 신뢰 안 함

- **🔴 Boss LLM = prompt injection 표적**: 입력에 워커 출력(신뢰 불가)이 들어간다 → 침해된 워커가 Boss LLM 을 조종해 "이 diff 안전함"이라 말하게 할 수 있다. 따라서 **Boss 출력도 untrusted**: (a) 실행 권한 0(텍스트만 반환, §4 R2 frozen 으로 강제) (b) §4 fail-safe 불변식으로 게이트 완화 불가 (c) 결정적 가드가 advisory *전에* 권위로 작동. 단 의미적 오도는 §4 R1 3중 방어로 한정(불변식만으로 미차단).
- **로컬 ≠ 안전 가정 금지**: 로컬 모델이라고 출력을 더 신뢰하지 않는다(거짓 안전감의 변종). advisory-only 가 신뢰 경계.
- **🔴 R3 — advisory 실패 거동 (Agent B, fail-closed 정신)**: Boss endpoint timeout/다운/비정상 응답 = **advisory 누락으로 처리**(결정적 flag·사람 게이트는 그대로 진행 — advisory 는 보조이므로 부재가 차단 아님). **단 사람에게 "⚠️ Boss advisory 실패 — 결정적 flag 만으로 판단" 명시 경고**(거짓 안전감 방지: 사람이 advisory 부재를 "안전"으로 오해 금지). 구분: *게이트* 는 항상 fail-closed(default-deny, `approval.py`), *advisory* 는 부재 시 명시 경고.
- **격리 무관**: Boss LLM 은 순수 추론(부작용 0)이라 워커 Landlock 격리(§MVP-0)와 직교. 단 Ollama 데몬은 로컬 포트 노출 → MVP-1 은 **localhost 바인딩 한정**(외부 노출 금지) — **V-1 PoC 에서 실측 확인 대상**(현재 후보 진술).
- **egress (R11 한정)**: 로컬 Boss = **추론 *시점* egress 0**(인터넷 비종속 시연의 핵심). **단 설치/모델 pull/텔레메트리는 별개**(Ollama 가 외부 접속할 여지 — "egress 0"의 범위를 추론 시점으로 한정, 거짓 안전감 예방). 워커가 클라우드 CLI 인 한 워커 egress 잔여(brief v4 B-3, MVP-1 미해소 — net 정책은 별도 후속).

## 6. V-1 선결 검증 (MVP-1 블로커 — 구현 전 PoC)

> brief v4 §7: **V-1 = MVP-1 블로커**(로컬 사장 구동). 현재 **미착수**. MVP-1 코드 구현 전 PoC 로 de-risk 필요.

| 검증 | 내용 | 통과 기준(후보 — 3+1/사용자 확정) |
|------|------|------|
| V1-1 | Ollama 설치·구동 (aarch64/CUDA13/sm_121) | 데몬 기동 + GPU 인식 |
| V1-2 | MoE 모델 pull + 추론 | 모델 로드 + 응답 생성 |
| V1-3 | **decode tok/s 실측** + **prefill(긴 diff 입력) 지연** + **advisory 입력 길이 상한/요약** | **threshold 후보**: advisory 용도엔 ≥ ~15 tok/s 면 실용(짧은 요약). 대화형이면 더 필요. *고정 안 함*. **decode 와 prefill 분리 측정**(긴 워커 출력은 prefill 이 decode 보다 지배 가능 → 입력 truncation/요약 필요) |
| V1-4 | `/v1/chat/completions` OpenAI-호환 확인 (Ollama·llama.cpp 둘 다) | §3 추상이 endpoint 교체로 성립 |
| V1-5 | 메모리/대역폭 실측 (273GB/s 병목 확인) | MoE 가 dense 대비 tok/s 우위 재현 |

**🔴 R4 — 런타임 후보 재조정 (Agent C, 2026 실측):**
- **llama.cpp ↔ Ollama 동급 후보** (v1 의 "Ollama 유력" 정정). 2026 DGX Spark 실측: **llama.cpp Qwen3-Coder-30B-A3B ~31 tok/s(Q8_0)** 확인 / Ollama 는 dense qwen3:32b **9.4 tok/s** 공개되나 MoE 미공개. → **V-1 에서 둘 다 MoE 로 측정** 후 결정(M3).
- **vLLM = "제외" → "MVP-1 비채택, MVP-2 재검토"로 강등**. 근거: 2026 기준 sm_120/121 binary-compat 으로 실동작 보고 + vLLM 0.17 해소 흐름(MXFP4 gpt-oss-120B ~56 tok/s 최고속). **영구 배제는 C-2(런타임도 교체 가능)와 충돌** → 문서에서 영구 못 박지 않음.

**R5 — tok/s 기대치 (de-risk 신호, Agent A roofline + C 실측):**
- roofline(memory-bound): `tok/s ≈ 273GB/s ÷ (활성파라미터 × bytes/param)`. **A3B Q4(~1.5GB/tok) → 상한 ~182, 실효 ~90–120 tok/s**. A3B Q8 → 실효 ~45–60. ~10B 활성 MoE Q4 → 실효 ~25–35. dense 70B Q4 → 한자릿수(brief §2 일치).
- **결론: ~15 tok/s threshold 는 MoE 로 2~8배 여유 충족**(A roofline·C 실측 ~31 독립 일치). MoE 방향(Q-1)이 273GB/s 병목에 정확. 단 **prefill 은 compute-bound 라 별개** — 긴 diff 입력 시 decode 보다 지연 클 수 있어 입력 상한/요약 필요(V1-3).

- **모델 후보(Q-1)**: Qwen3.x-A3B/A10B(MoE, 대역폭 적합) — brief v4 조사 Qwen3.6-35B-A3B SWE-bench 73.4%(35B총/3B활성, 12:1 sparsity). **활성 파라미터 작은 MoE = 273GB/s 병목에 적합**. 하드코딩 금지(config).
- **롤백**: Ollama/llama.cpp 설치 = 사용자 영역(`~`) 한정 + 모델은 디스크. 시스템 변경 최소. PoC 후 `rm`/uninstall 복구.

## 7. 결정 항목 (3+1 / 사용자 몫 — 본 brief 결정 안 함)

| # | 항목 | 후보 | 비고 |
|---|------|------|------|
| M1 | **판단 지점 범위** | **MVP-1=advisory 1개만**(§1) / 워커선택·작업분해 포함 | 비례성 — 본 brief 권고=1개 |
| M2 | **로컬 모델** | Qwen3.x-A3B(MoE) / 30B이하 양자화 | tok/s 실측 기준, config |
| M3 | **추론 런타임** | **llama.cpp ↔ Ollama 동급**(V-1 MoE 실측 후) | **vLLM=MVP-2 재검토(영구배제 아님, R4)** |
| M4 | **tok/s threshold** | advisory용 ~15+ 후보(MoE 2~8배 여유, R5) | *고정 금지* — V-1 실측 후 |
| M5 | **advisory fail-safe 불변식** | flag 감산 불가(합집합만) + R1 의미적 한계 명시 | §4 — 확정 대상 |
| M6 | **Boss endpoint 보안** | localhost 바인딩 한정(V-1 실측 확인) | §5 |
| M7 | **Boss HTTP 클라이언트** | 표준 httpx(SDK import 회피) / provider SDK | worker.py 원칙 동형 |
| ~~M8~~ | ~~`BossAdvice.confidence`~~ | **삭제(R6)** — LLM 자기보고=거짓 안전감 | §4 |

## 8. 구현 2-트랙 (R9, MVP-0 패턴 재사용) + 단계

> **R9 (Agent C·A)**: MVP-1 도 MVP-0 처럼 격리(V-1)-직교 골격을 선행 분리한다. 추상화+advisory 는 V-1 무관하게 TDD 가능, 로컬 런타임 연결만 V-1 블로커.

- **트랙 A (BossLLM 추상 + advisory) — V-1 무관, 즉시 진입 가능**: `BossLLM` Protocol + `BossAdvice`(R2 frozen) + `Orchestrator(boss=None)` 통합(R7) + advisory 합집합 flag(R8 실패경로 포함) + `StubBoss` 주입 TDD. 실 LLM 호출·설치 0(StubBoss 로 결정적 테스트). 합의 후 즉시 가능.
- **트랙 B (로컬 런타임 연결) — V-1 통과 후**: `OllamaBoss`/`llama.cpp` endpoint 구현 + config 주입 + 실 advisory 연결. V-1(런타임·tok/s) de-risk 의존.

### 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 |
|------|------|
| ✅ | ~~본 v1 3+1 합의~~ **완료** — [[3plus1-consensus-2026-05-22-jarvis-mvp1-local-boss]] APPROVE w/ COND, R1~R13 본 v2 반영 |
| (A) | **트랙 A 구현 진입**(BossLLM 추상 + advisory + StubBoss TDD) — V-1 무관, 즉시 가능 |
| (B) | **V-1 PoC** 진입(Ollama·llama.cpp 둘 다 MoE tok/s 실측, R4) — 트랙 B 선결 |
| (C) | **트랙 B 통합**(로컬 런타임 연결) — V-1 통과 후 |
| (D) | commit / push / 세션 정리 |

- ⚠️ 트랙 A 코드 = 본 v2 + 합의 통과로 진입 게이트 충족. 트랙 B = V-1 통과 후. 설치/모델 다운로드는 V-1 단계에서 별도 승인.

---

## 부록 — 답습 + 금지

**출처**: [[jarvis-orchestrator-mvp-design-brief]] (v4 §5 MVP-1·D-1·Q-1·Q-2·§7 V-1) / [[jarvis-safety-layer-poc-findings]] (V-1 미착수) / MVP-0 코드(`src/jarvis/orchestrator.py`·`worker.py`·`review.py`) / 헌법 5조. 답습: `project_jarvis_local_boss_direction` / `feedback_provider_liquidity` / `feedback_proportionate_security_personal_tool` / `project_minimize_user_intervention` / `feedback_staged_consensus_workflow`.

**금지 (영구 답습, 본 brief 0건)**: 코드 작성(BossLLM·advisory·통합) / Ollama·llama.cpp 설치 / 로컬 모델 다운로드 / tok/s 측정 실행 / config 변경 / 모델 결정 고정(M2) / 런타임 결정 고정(M3) / tok/s threshold 고정(M4) / 판단 지점 advisory→자동승인 격상 / 사람 게이트 약화 / 결정적 가드 권위 약화(fail-safe 불변식 위반) / immutable zone 침범 / Provider Liquidity 약화 / commit·push / 보안 거버넌스(credential/4축/BI-*) 자동 재개.
