# 3+1 합의 — 무검열 텍스트→이미지 파이프라인 **통합 아키텍처** (Position A)

> 날짜: 2026-06-19 · 유형: 아키텍처 설계 검토 (범위 한정) · 결과: **REVISE (원칙 승인, 구현 전 7개 정정 필수)**
> 검토 대상: `docs/architecture/uncensored-prompt-to-image-pipeline-design.md`
> 범위: **통합 아키텍처만**(GenGateWorker + image kind + 2-step plan + prompt_lab 경계). 보안/신뢰경계 정책은 Part 3 합의가 확정 → 재논의 안 함.
> 모법: `3plus1-consensus-2026-06-19-uncensored-llm-worker-delegation.md`

---

## Phase 2 — 독립 분석 요약

| Agent | 관점 | 한 줄 결론 |
|-------|------|-----------|
| **A 구현 분석가** | "동작하는가?" | **조건부 가능** — 인터페이스는 실재하나 설계 §2 라우팅 서술·consume 가정·동기 근거가 코드와 어긋남(정정 필수) |
| **B 품질/안전 검증가** | "안전·견고한가?" | **Gard 1 위반** — cross-process GPU lock repo 전체 부재(설계 over-claim). Gard 2·3은 문구 정정 후 보존 |
| **C 대안 탐색가** | "더 나은가?" | **통합 표면 축소 권고** — 전용 GenGateWorker→범용 HttpServiceWorker, image kind→`service` 단일 능력축(modality는 인자) |

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus, 3/3 정렬)
- **정책=alias로만, 능력=kind** 분리 원칙 자체는 견고 → 유지.
- **Provider Liquidity 유지**: 무검열 모델(model 인자)·이미지 모델(capabilities unit) 둘 다 코드 결합 없음 (A·C 확인).
- **prompt_lab ≠ 서비스, ≠ jarvis 워커**: prompt_lab은 *오케스트레이션 셸/레시피*다. 서비스화·워커화 모두 비권장 (C 명시, A는 import 경로 문제로 보강).

### ② 부분 일치 (2/3)
- **gen_gate 워커 형태** — A는 GenGateWorker를 *견고화*(timeout·202 fail-closed·비200→is_error·did_act)하면 동작 가능. C는 아예 *범용 HttpServiceWorker*로(전용 클래스 양산 차단). → **수렴**: C의 범용 워커 골격 + A의 견고화 디테일.
- **image kind** — A는 "image를 SAFE_CONSUME_KINDS에 넣어야 안 막힘 + EXEC_SENTINEL 오염 주의". C는 "modality를 kind에 박지 말고 `service` 단일 능력축". → **수렴**: `service` 능력축 kind 채택 + 그 kind를 SAFE_CONSUME_KINDS에 등록.

### ③ 불일치 (Divergence)
- **Gard 1 심각도** — B만 깊이 파고들어 **repo 전체 cross-process lock 부재**를 확증(BLOCKING). A·C는 미언급. → B 판정 채택(반증 없음, 코드 실측 근거).

### ④ 누락 (Gap, 1개 에이전트만)
- **B**: GenGateWorker `base_url` 주입형이면 **SSRF 재도입** 위험(OllamaWorker는 localhost 하드코딩으로 차단). → 중요, 채택(localhost 강제).
- **A**: ① `_EXEC_SENTINEL`/실행규약 텍스트가 이미지 프롬프트 *오염*, ② `RedactionFilter`가 무검열 프롬프트의 secret-유사 패턴을 마스킹해 프롬프트 *손상* 가능. → 중요, 채택.
- **C**: **능력축 폭발** — voice_lab·motion_lab이 이미 존재(MEMORY: 다음=모션)하므로 modality당 kind+워커 1쌍은 *예고된* 폭발. → 채택(선제 차단).

---

## Phase 4 — 합의 도출: **REVISE** (구현 전 정정 7건)

설계의 *방향*(Position A 명시 위임, 정책=alias·능력=kind 분리)은 승인. 단 아래 7건을 설계 문서에 반영하고 구현해야 합의 충족.

### 🔴 R1 (BLOCKING) — Gard 1: cross-process GPU lock 부재
- **사실**: gen_gate `gpu_guard.py`/`local_3d_trellis.py:24`·jarvis `process_control.py`(line 317~) 모두 **in-process threading.Lock**. 합의 line 32가 "in-process Lock 무효"라 한 바로 그 한계. cross-process lock은 repo 어디에도 없음.
- **결정**: 설계 §4 "gpu_guard 재사용으로 충족" = **over-claim 철회**. 두 경로 중 하나:
  - (a) 실제 `flock`/`fcntl` 기반 **cross-process lockfile 신규 구현** 후 enable, 또는
  - (b) **실 기동 명시 DEFER** — 스켈레톤+테스트(GPU 무관)만 진행, 실 e2e 기동은 "GPU 단독 점유 수동 보장" 또는 (a) 완료까지 보류.
- 합의 ④ "이것 없이 enable 금지" 답습. **스켈레톤·테스트는 GPU 무관이므로 진행 가능**(설계 §6 유지).

### 🟠 R2 — plan 라우팅 = worker_kind (alias 아님)
- **사실**: `PlanController`는 `worker_kind→kind_table` 룩업으로 라우팅. `boss.py` subtask엔 `worker_alias` 필드 없음. 설계 §2 다이어그램의 `dispatch(worker_alias=)`는 직접 호출 시그니처일 뿐 plan 경로 아님.
- **결정**: prompt_lab 레시피가 **이 파이프라인 전용 kind_table**(harness 소유)을 구성 — 무검열 step은 전용 kind(예: `prompt`)→`ollama-uncensored`. `file` kind는 기존 `ollama-file` 점유라 재사용 불가. "사람(레시피)이 alias 명시"는 *전용 kind_table 구성*으로 실현(boss는 여전히 kind만 제안 못 함 → 고정 DAG).

### 🟠 R3 — consume 게이트는 *소비자* kind 기준
- **사실**: `_consume_ok`는 *소비자* worker_kind를 SAFE_CONSUME_KINDS와 대조. 이미지 step(소비자)이 미포함이면 `allow_code_consume=False`인 한 **reject**. 설계 §3.1(c) "SAFE_CONSUME 불변" 주장은 그대로면 **파이프라인 차단**.
- **결정**: 이미지 step kind(R5의 `service`)를 **SAFE_CONSUME_KINDS에 추가**. 이는 *텍스트 프롬프트 artifact* 소비 허용일 뿐 — **code/shell consume과 무관, `allow_code_consume` off 유지**(합의 ④ 충족). 설계 §2 각주 "file 소비라 안 막힘" → "소비자 kind를 SAFE_CONSUME에 등록(code consume 아님)"으로 정정.

### 🟠 R4 — gen_gate 동기/비동기 + 워커 견고화
- **사실**: gen_gate는 `_ASYNC_MODALITIES={3d}`만 비동기(202+poll). 이미지는 동기. 설계 결론(동기)은 맞으나 근거 틀림 + 향후 이미지가 async 편입 시 silent 오작동.
- **결정**: GenGate(또는 HttpServiceWorker)는 — 긴 timeout 명시 / **202 수신 시 fail-closed**(거짓 성공 금지) / 비-200(403 등급·404·500)→`is_error=True` / 성공 시 `did_act=True`. 설계 §2·§3.1(b) 근거 정정.

### 🟡 R5 — 범용 HttpServiceWorker + `service` 능력축 (C)
- **결정**: 전용 `GenGateWorker` → **범용 `HttpServiceWorker(alias, base_url, unit)`**(`/api/capabilities` 규약 흡수, lab 정석 패턴). 이번엔 `gengate` alias만 등록. worker_kind는 modality(image/3d/audio)별 신설 금지 → **`service`(외부 HTTP 실행) 단일 능력축**, modality는 워커 인자. `EXECUTING_KINDS`에 `service` 추가, `SAFE_CONSUME_KINDS`에 `service` 추가(R3). → voice_lab·motion_lab 무료 흡수, 능력축 폭발 차단.

### 🟡 R6 — 프롬프트 오염 차단 (A)
- **결정**: 이미지 step은 `requires_execution=False`로 두거나 `_EXEC_SENTINEL`/실행규약 주입을 `service` kind에서 제외(이미지 프롬프트 오염 방지). `RedactionFilter`가 무검열 프롬프트를 손상시키는지 구현 시 검증(동작 정합 이슈, 보안 정책 아님).

### 🟡 R7 — base_url SSRF + prompt_lab 의존 (B·A·C)
- **결정**: HttpServiceWorker `base_url`은 **localhost 강제**(OllamaWorker 하드코딩 답습, SSRF/exfil 차단). prompt_lab↔jarvis = **좁은 공개 facade 직접 import**(C). 단 **현재 패키징(pyproject/setup) 부재로 editable install 불가**(A) → 스켈레톤은 `PYTHONPATH=<repo>` + `from src.jarvis...`, 별도 repo `src/` 네임스페이스 충돌 주의. packaging 추가는 후속 선결로 명시.

---

## 정직한 한계 (over-claim 차단)
- 본 합의는 **통합 아키텍처** 검토. 무검열 위임 정책 가부·콘텐츠 게이트 DEFER는 Part 3가 확정(재검토 아님). 콘텐츠 게이트 DEFER와 본 파이프라인은 정합(gate.generate=상업화 1축만, 무검열 프롬프트 통과가 의도된 상태).
- capability 경계는 실행/부작용을 막지 NL injection 의미를 막지 않음(Part 3 답습). 사람 게이트는 라우팅(kind_table 매핑 alias)을 *노출*할 뿐 내용 *검증* 안 함.
- 미검증 유지: dolphin3 GB10 실구동(D3)·한국 법(D4)·프롬프트 품질(D5).

---

## 사용자 결정 대기
- REVISE 7건을 설계 문서(`uncensored-prompt-to-image-pipeline-design.md`)에 반영 → commit. 그 후 구현(별도 브랜치 TDD, R1(b) 스켈레톤 우선).
- **수단/threshold 결정**(R1 a vs b, 실 기동 시점)은 사용자 영역.
