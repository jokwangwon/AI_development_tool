# Jarvis 오케스트레이터 MVP 설계 brief — 로컬 사장 + tmux 워커 (DRAFT v1)

> **본 brief = 자비스 오케스트레이터 MVP 설계 한정.** 본 brief 의 어떤 §도 그 자체로 **코드 작성·CAO 설치·로컬 모델 다운로드·추론 런타임 설치·tmux 세션 생성·provider adapter 구현·git hook/CI 구성** 을 발생시키지 않는다. 본 brief = **비전 정식화 + 확정 제약 기록 + 아키텍처 후보 + 3+1 합의용 결정 항목 정리** — 실 변경 0건. staged: brief → 승인 → **3+1 합의(아키텍처 큰 결정 = 필수)** → (합의 후) TDD 구현.

---

**작성일**: 2026-05-22
**Status**: **DRAFT v1 — 3+1 합의 진입 대기**
**진입 단위**: 자비스 본연 기능 — 오케스트레이터 MVP (보안 거버넌스 트랙과 독립, [[feedback_proportionate_security_personal_tool]] 로 거버넌스 DEFER)
**근거 메모리**: [[project_jarvis_local_boss_direction]] (방향 확정) · [[feedback_provider_liquidity]] (헌법 5조) · [[feedback_proportionate_security_personal_tool]] (비례성) · [[project_minimize_user_intervention]] (개입 최소화) · [[feedback_staged_consensus_workflow]] (단계 분리)

---

## 0. 비전 (사용자 확정, 2026-05-22 대화)

> **인터넷/구독에 묶이지 않는 나만의 자비스(Jarvis).** Provider-agnostic — Claude 비종속. 토큰 소진·구독 불가 시 GLM 등 fallback 워커로 계속 작업. 넓은 개인 비서를 지향하되, 개발자이므로 **개발 작업이 MVP 중심**.

### 0.1 조직 모델 (사용자 제시 은유 — 기능에 봉사하는 선에서만, "메타포 강제 금지" 준수)

| 역할 | 정체 | 권한 |
|------|------|------|
| **대표** | 사용자 본인 | **최종 결정** (승인 게이트) |
| **사장** | 로컬 LLM (항상 ON) | 작업 수령·계획·분배·결과 검토 |
| **워커** | claude / gpt / GLM … CLI 에이전트 | 작업 수행 + **자기 의견 표현 가능**, **언제든 교체** |

- 사장↔워커 **의논 → 점진 강화** = 자가진화 루프 (기존 3+1 합의 프로토콜의 자동화 형태와 매핑)
- 워커 교체 = [[feedback_provider_liquidity]] 구현 형태 (헌법 5조 비협상)

## 1. 확정된 선행 결정 (본 세션 대화에서 사용자 명시)

| # | 결정 | 근거 |
|---|------|------|
| D-1 | **코어 두뇌 = 로컬 LLM(사장)이 직접 추론·지휘** (안 (a)) | 사용자 명시. GB10/121GB 로 현실적 |
| D-2 | **워커 = CLI 에이전트, tmux 로 구동·교체** | provider liquidity 가 CLI-via-tmux 를 사실상 강제 (§3) |
| D-3 | **개발 작업 MVP 중심**, 비서 기능은 후속 확장 | 검증 용이(테스트/lint/git), 자가진화 부착 용이 |
| D-4 | **자가진화 = 깊게 지향, 무리면 중간 타협**. self-change 는 git+테스트+사람승인 게이트 통과해야 반영 | 비례성 — 하드웨어 서명 같은 과잉 인프라 불요 |
| D-5 | **구현 형태 = 제3안(하이브리드)**: 우리 얇은 오케스트레이터 직접 구축 + CAO(Apache-2.0)를 참조 구현으로 검증된 배관 패턴 차용 | 본 세션 비교표 (§4), 사용자 명시 |

## 2. 환경 실측 (2026-05-22 확인, read-only)

| 항목 | 값 | 함의 |
|------|----|----|
| SoC | **NVIDIA GB10** (Grace Blackwell, DGX Spark급) | 로컬 사장 LLM 구동 충분 |
| 메모리 | **121GB 통합** (104GB 여유) | 대형 모델(70B급 양자화 등) 가능 |
| 디스크 | 1.9TB (332GB 여유) | 모델 가중치 다수 보관 OK |
| 아키텍처 | ARM64 (Grace) + Blackwell(sm_12x) | ⚠️ 추론 런타임 ARM64+CUDA 빌드 필요 |
| 보유 | tmux 3.4 ✅ · claude CLI ✅ · python 3.12 ✅ | 워커 구동 토대 확보 |
| 미보유 | ollama / llama.cpp / vllm | 로컬 추론 런타임 설치 필요 (별도 검증) |

## 3. 왜 CLI-via-tmux 인가 (Provider Liquidity 정합)

오케스트레이션 방식 두 갈래:

- **(A) CLI-via-tmux**: 워커 = 별도 프로세스/바이너리(claude·codex·glm CLI). tmux 가 프로세스 경계 추상화 → **provider 교체 = "다른 바이너리 띄우기"로 공짜**. GLM fallback = "GLM CLI 추가".
- **(B) API 프레임워크**(LangGraph/CrewAI): provider SDK 코드 결합 → **헌법 5조 Provider Liquidity 와 정면충돌**. CLI 워커 교체 모델과 불일치.

→ **결론: 비협상 제약(Provider Liquidity) 때문에 (A) CLI-via-tmux 가 사실상 강제.** D-2 의 근거.

## 4. 제3안 근거 — CAO 비교표 (§ 본 세션 조사)

CAO(awslabs/cli-agent-orchestrator) 실측: Python 92% / Python 3.10+ / **tmux 3.3+** / **Apache-2.0** / 계층(CLI·MCP server·FastAPI:9889·service·SQLite·**provider 추상 `base.py`**) / provider 추가 = `glm.py`+`provider_manager.py` 등록 / handoff·assign·send_message + agent profile(.md).

| 관점 | (가) CAO 기반 | (나) 직접 구축 | **제3안(채택)** |
|------|--------------|--------------|----------------|
| 배관 확보 | ⭐ 80% 완성 | 0% | CAO 패턴 **차용** |
| send-keys 함정 | 이미 해결 | 재발견 위험 | 차용 |
| provider liquidity | ⭐ 추상 내장 | 직접 설계 | 차용 + 우리 정책 |
| 철학 정렬(SDD/TDD/한국어) | △ 강제 어려움 | ⭐ | ⭐ 우리 코드 |
| 자가진화 깊이 | △ fork 발산 | ⭐ 1급 설계 | ⭐ |
| 비례성(의존성 최소) | △ FastAPI·웹UI 무거움 | ⭐ 얇게 | ⭐ |

**차용 대상 패턴**: ① send-keys 타이밍 처리(텍스트→sleep→`C-m` 분리) ② handoff(동기)/assign(비동기)/send_message 프리미티브 ③ provider 추상(`base.py` 인터페이스) ④ `.done` 파일 또는 SQLite 기반 완료신호/상태(rohanverma 식 메시지버스).

## 5. MVP 척추 (가장 얇은 end-to-end)

```
사용자(대표) 작업 입력
   │
   ▼
[로컬 사장 LLM] 계획 수립 → 워커 선택(가용성·비용 정책)
   │  tmux: 텍스트 send → sleep → C-m  (워커 CLI 구동)
   ▼
[워커 CLI] (우선 claude, fallback 가능) 작업 수행
   │  .done / SQLite 로 완료 신호 + 출력 회수
   ▼
[사장] 결과 검토
   │
   ▼
[대표] 보고 받고 승인/반려  ← 사람 결정 게이트
```

증명 항목 4: ① 로컬 사장 추론 ② tmux 워커 분배 ③ provider 교체 ④ 사람 결정 게이트.
**MVP 범위 밖(후속 층)**: 사장↔워커 다중턴 의논 / 다중 워커 병렬 / 자가진화 루프 발효 / 넓은 비서 기능.

## 6. 3+1 합의용 결정 항목 (본 brief 가 *결정하지 않음* — 합의/사용자 몫)

| # | 결정 항목 | 후보 | 비고 |
|---|----------|------|------|
| Q-1 | **로컬 사장 모델** | Qwen2.5-Coder / Llama / GLM-local / 기타 | GB10 VRAM·코딩 성능·라이선스 형량. **하드코딩 금지**(config 교체, 헌법 5조) |
| Q-2 | **추론 런타임** | Ollama / llama.cpp / vLLM | ARM64+Blackwell 호환성 = **별도 PoC 검증 필요** |
| Q-3 | **사장↔워커 통신** | tmux send-keys + `.done` 파일 / SQLite inbox / MCP | MVP 는 최소(파일/SQLite), MCP 는 후속 |
| Q-4 | **워커 provider 추상 형태** | `Worker` 인터페이스(spawn/send/capture/done) | CAO `base.py` 차용, provider liquidity 1급 |
| Q-5 | **provider 라우팅 정책** | claude 우선 → 토큰/구독 끊기면 GLM fallback | 가용성·비용 신호 감지 방법(MVP=수동/설정, 후속=자동) |
| Q-6 | **대표 결정 게이트 위치** | 작업 착수 전 / 결과 반영 전 / 양쪽 | 개입 최소화([[project_minimize_user_intervention]])와 형량 |
| Q-7 | **자가진화 첫 적용 지점** | 워커 프롬프트/profile 갱신(중간) → 코어 자기수정(깊음) | git+테스트+승인 게이트 필수(D-4) |
| Q-8 | **언어/패키징** | Python(CAO 정합·uv) vs 기타 | Python 권고(CAO 패턴 차용·python3.12 보유) |

## 7. 별도 선결 검증 (아키텍처 결정과 직교)

- **V-1 ⚠️ GB10(ARM64+Blackwell)에서 로컬 추론 런타임 실동작** — (가)/(나) 무관하게 풀어야 함. Ollama/llama.cpp/vLLM 중 sm_12x CUDA 빌드 가용성 PoC. 사장 모델 구동 = MVP 전제.
- **V-2** CAO 가 ARM64 에서 설치/동작(순수 Python 이라 거의 확실, 단 참조용으로만 쓰면 무관).

## 8. 자가진화 안전 모델 (D-4 구체화)

- self-change(워커 프롬프트·skill·코어 코드 수정) = **항상 git commit 형태** → 기존 피드백 루프(Layer 1 lint / Layer 2 테스트 / Layer 6 사람 리뷰) 통과해야 반영.
- **대표 승인 게이트** = 자가진화 반영의 최종 차단. 자동 재배포 0건(MVP).
- 비례성: 하드웨어 서명·touch-per-commit 등 과잉 인프라 불요([[feedback_proportionate_security_personal_tool]]). git+테스트+리뷰로 충분.

## 9. 다음 단계 (사용자 결정 — 자동 진입 0건)

| 옵션 | 내용 |
|------|------|
| (A) | 본 brief **3+1 합의 진입** (아키텍처 큰 결정 = 필수, Q-1~Q-8 다관점 검증 — **권장**) |
| (B) | V-1 추론 런타임 PoC 먼저 (로컬 사장 구동 가능성 = MVP 전제 확인) |
| (C) | brief 보강 (특정 § 더 깊이) |
| (D) | commit 체크포인트 |

- ⚠️ **TDD 코드 구현 = 3+1 합의 후**. 본 brief 승인 ≠ 구현 착수.

---

## 부록 — 답습 출처 + 금지

**출처**: 본 세션 대화(D-1~D-5 사용자 명시) / 웹 조사(CAO·rohanverma tmux swarm·orchestrator-worker 패턴) / 환경 실측(GB10/121GB) / 헌법 5조 Provider Liquidity / [[project_jarvis_local_boss_direction]].

**금지 (영구 답습, 본 brief 0건)**: 코드 작성(orchestrator·provider·라우팅) / CAO 설치·fork / 로컬 모델 다운로드 / 추론 런타임(ollama/llama.cpp/vllm) 설치 / tmux 세션 생성·send-keys 실행 / git hook·CI·skill 실 구성 / 사장 모델 결정 고정(Q-1) / 런타임 결정 고정(Q-2) / 자가진화 자동 발효 / 워커 자동 설치 / commit / push / 5 영구 핵심 제약·Provider Liquidity 약화 / 보안 거버넌스(credential/4축/BI-*) 자동 재개([[feedback_proportionate_security_personal_tool]]).
