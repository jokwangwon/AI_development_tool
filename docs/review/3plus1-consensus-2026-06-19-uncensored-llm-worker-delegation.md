# 3+1 합의 — 무검열 로컬 LLM 워커 + 정책 민감 작업 위임 (jarvis)

> 날짜: 2026-06-19 · 유형: 아키텍처/보안 결정(신뢰경계) · 결과: **명시 위임 = 지금 가능(가드 3종) / 자동 위임 = trust-boundary gated DEFER**
> 적용 대상: `src/jarvis/` (provider-agnostic 개인 명령 실행 에이전트, plan-then-execute + 사람 승인 게이트)
> ⚠️ 이 합의는 **권고**. 수단(모델) 결정·구현 착수는 **사용자 영역**.

## 결정 질문
자비스에 **무검열 로컬 LLM을 워커로 붙이고, 정책 민감 작업을 위임**하는 구조를 도입할 것인가? 어떤 구조·시점으로? solo 개인 툴, provider-liquidity 비협상, GB10 OOM 위험.

## 핵심 결론 — 두 결정을 분리하라
- **(1) 무검열 모델 "붙이기"** = 거의 공짜. 지금 가능.
- **(2) 정책 민감 작업 "자동 위임"** = 신뢰경계 모순. DEFER.

## ① 만장일치 합의 (3/3)
1. **무검열 워커 = `OllamaWorker(alias="ollama-uncensored", model="<무검열모델>")` 등록 1줄.** OllamaWorker 무수정(헌법5조 provider 교체 정의=model 인자 교체). HTTP localhost:11434, **LLM 텍스트만 수신·실행 경로 구조적 부재**.
2. **자동 위임(정책 분류→자동 라우팅)은 지금 금지** — A(불필요), B(BI-3 근본 모순), C(DEFER한 분류의 거울상).
3. **사람 승인 게이트가 이미 핵심 안전장치** — `PlanApprovalRequest.mapped_aliases` 가 "이 작업은 ollama-uncensored 로 간다"를 dispatch 전 사람에게 노출.
4. **boss 는 means/정책 못 정함**(PLAN-INV/BL-1) — worker_kind enum 만 untrusted 제안, alias/argv/isolation 은 harness 소유.

## ② 핵심 통찰 — 자동 위임의 근본 모순 (Agent B, BI-3 재현)
> "자동 위임으로 개입 최소화"는 사람 승인 게이트와 **원리적으로 양립 불가**.
> - 게이트 *우회* 자동 위임 = 불변식①(plan→사람 승인) 위반
> - 게이트 *유지* 자동 위임 = 개입을 안 줄여 동기와 모순

→ 단순 연기가 아니라 **신뢰경계 변경(별도 풀 3+1)이 선행돼야 진입 가능한 trust-boundary gated DEFER**. ([[project_minimize_user_intervention]] ↔ BI-3 충돌의 가장 날카로운 형태)

## ③ 불일치 해소
- **위임 단위 (alias vs 새 kind)**: A는 "결정적 자동 라우팅하려면 새 kind 필요"라 했으나, 자동 위임을 안 하기로 한 순간 그 조건 소멸 → **alias 명시 채택**(`dispatch(worker_alias=)` 이미 1급 인자, 새 코드 0). 새 kind 는 *능력축*(file/code/shell)에 *정책축* 오염(C) → 거부.
- **자동 위임 시점**: 명시만 지금 + 자동 DEFER(B 근거로 구조적 보류 격상).

## ④ 안전 가드 3종 (지금 붙인다면 동시 필수)
- **GB10 OOM cross-process 상호배제** — 시스템 lockfile/flock(`process_control.py` lock+probe 패턴 재사용). in-process threading.Lock 은 diffusion/학습이 별 프로세스라 무효. **이것 없이 enable 금지.**
- **`allow_code_consume` 영구 off** — 무검열 produce → code/shell consume 이 가장 위험(NL injection 페이로드 품질↑).
- **fail-closed 방향 = 검열 워커 쪽** — 모호하면 무검열로 안 흐름.

## 정직한 한계 (over-claim 차단)
- capability 경계(`SAFE_CONSUME_KINDS={file}`)는 **실행/부작용**을 막지 **NL injection 의미**를 막지 않음(`_extract_artifact` 라벨=위조방어이지 의미격리 아님). 사람 게이트는 라우팅을 *노출*할 뿐 무검열 출력 내용을 *검증*하지 않음.
- net egress 미차단 → 무검열은 **localhost OllamaWorker 로 한정**(CliWorker형 무검열은 exfil 잔여, 별도 검토).
- **미확인**: 무검열 모델의 GB10(sm_121, aarch64) 실구동 / 한국 영토 법·라이선스.

## 사용자 결정 (2026-06-19 수령)
- **결정 = 3번**: 무검열 LLM = **프롬프트 작성(텍스트 생성)** 단계, **gen_gate = 이미지 생성(실행)** 단계. (사용자 결정 #2 "텍스트 vs 실행" 해소)
  - 무검열 워커 = `file` kind 텍스트 산출(OllamaWorker 적합). 프롬프트 artifact → gen_gate 가 이미지 생성.
  - gen_gate 는 "프롬프트→이미지"로 제약된 실행이지 code/shell consumer 아님 → `allow_code_consume` off 유지해도 이 파이프라인 안 막힘.
- **파이프라인 위치(권고 B = 독립 파이프라인)**: 지금은 무검열 ollama 직접 호출 → gen_gate 직접 호출(jarvis 풀 오케스트레이션 밖). 자동화·통제 필요 시 A(jarvis plan→승인→gen_gate 워커)로 승격. *사용자 최종 확인 대기.*
- **실 기동은 GPU 가드(OOM lockfile) 때문에 다른 GPU 작업 비점유 시에만.** 설계/스켈레톤은 무관.

## 열린 질문 (사용자 영역)
1. 무검열 모델 선택(C 관찰: Dolphin류 fine-tune 이 abliteration 보다 출력 안정적, JSON 엄격 파싱 워커엔 유리). 라이선스·한국 법 별도.
2. 파이프라인 위치 A vs B(추천 B).
3. 구현 착수 시점.
