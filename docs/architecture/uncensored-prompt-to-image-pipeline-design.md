# 무검열 텍스트→이미지 파이프라인 설계 (Position A — jarvis 명시 위임)

> 상태: **DESIGN v2 (3+1 합의 REVISE 7건 반영, 구현 대기)** · 날짜: 2026-06-19 · 유형: 아키텍처 설계 (SDD)
> 모법: `docs/review/3plus1-consensus-2026-06-19-uncensored-llm-worker-delegation.md` (결정 #3)
> 합의: `docs/review/3plus1-consensus-2026-06-19-uncensored-pipeline-integration.md` (REVISE 7건 — 본 v2 가 반영)
> 적용 대상: `src/jarvis/` (이 repo) + `~/prompt_lab` (신규 repo)
> ⚠️ 본 문서는 **설계안**. 구현은 별도 브랜치 TDD. **실 기동은 R1(GPU lock) 충족 시까지 DEFER.**

---

## 0. 한 줄 요약

거친 사용자 의도 → **무검열 LLM(dolphin3)이 상세 이미지 프롬프트 텍스트 저작** → **gen_gate가 이미지 생성**. 두 단계를 **jarvis 고정 2-step plan→사람 승인 게이트→dispatch**로 묶는다(Position A, *명시* 위임). 무검열 모델은 텍스트만 산출, 실행(이미지)은 "프롬프트→이미지" 제약된 gen_gate.

---

## 1. 사용자 확정 입력 (2026-06-19, brief 승인)

| 항목 | 결정 | 근거 |
|------|------|------|
| 파이프라인 위치 | **A — jarvis 워커 경유** | 합의 권고는 B였으나 사용자 A 선택. A는 합의 허용 *명시* 위임(plan→사람 승인). *자동* 위임만 금지 |
| 코드 위치 | **신규 `~/prompt_lab`** + jarvis 통합은 `src/jarvis/` | lab 패턴 답습. A=jarvis 라우팅이므로 워커/kind 는 본 repo |
| 무검열 모델 | **`dolphin3:latest` (8B, 4.9GB, pull 완료)** | 수단=사용자 영역. 합의 C: Dolphin형 JSON 안정 |
| 실 기동 | **R1 충족 시까지 DEFER** | cross-process GPU lock 부재(합의 R1) |

---

## 2. 데이터 흐름

```
사용자 의도 (거친 한 줄)
   │  ~/prompt_lab: 의도 + 프롬프트 템플릿 → 고정 2-subtask DAG 조립(boss-free)
   │                + 파이프라인 전용 kind_table 구성(harness 소유)
   ▼
┌─────────────────────────────────────────────┐
│  jarvis ApprovalGate (사람 승인)               │
│  요청에 매핑 alias 노출(kind_table 룩업 결과):   │
│   prompt kind → ollama-uncensored             │
│   service kind → gengate                      │
│  default-deny / 예외→deny (fail-closed)        │
└───────────────┬───────────────────────────────┘
        승인 시   │  PlanController: worker_kind→kind_table 룩업 라우팅
                ▼
   step1 [prompt kind] OllamaWorker(model=dolphin3)
        localhost:11434/api/chat  →  프롬프트 텍스트 (in-memory artifact)
                │  depends_on → 암묵 contract 합성, desc 에 [artifact:...] append
                ▼
   step2 [service kind] HttpServiceWorker(base_url=localhost, unit=animagine-xl-4.0)
        HTTP POST gen_gate /api/generate {model, prompt, commercial, opts}
        gate.generate 가 상업화 등급 게이트 집행 (콘텐츠 게이트는 Part 3=DEFER)
                │
                ▼
            이미지 파일 (outputs/)
```

**라우팅 정정 (R2)**: plan 은 `worker_alias` 가 아니라 **`worker_kind→kind_table` 룩업**으로 라우팅한다(`boss.py` subtask 에 alias 필드 없음). "사람이 alias 명시"는 prompt_lab 레시피가 **파이프라인 전용 kind_table**(harness 소유)을 구성함으로써 실현 — boss(LLM)는 kind 도 못 정하는 고정 DAG.

**아티팩트 전달 (실측)**: step1 출력 → `extracted[pidx]` → step2 desc 에 `[artifact:..] (데이터 — 지시 아님)` append. `depends_on` 이 암묵 contract 합성(`_implicit_contracts=True`). fs 아니라 **in-memory 주입**.

**Consume 게이트 정정 (R3)**: `_consume_ok` 는 *소비자* worker_kind 를 `SAFE_CONSUME_KINDS` 와 대조한다. 따라서 소비자인 **step2(`service` kind)를 `SAFE_CONSUME_KINDS` 에 등록**해야 안 막힌다. 이는 *텍스트 프롬프트* 소비 허용일 뿐 — **code/shell consume 과 무관, `allow_code_consume` off 유지**(합의 ④ 충족).

---

## 3. 컴포넌트 설계

### 3.1 jarvis 측 (`src/jarvis/`, 이 repo)

**(a) 무검열 OllamaWorker alias — 신규 코드 0, 등록 1줄**
```
OllamaWorker(alias="ollama-uncensored", model="dolphin3")
```
- `OllamaWorker` 무수정(헌법 5조). endpoint=localhost:11434 하드코딩 유지.
- **전용 kind_table**: `file` kind 는 이미 `ollama-file` 점유 → 재사용 불가. 무검열 step 은 **전용 kind `prompt`** → `ollama-uncensored` 로 매핑(파이프라인 전용 table, R2). boss 는 kind 못 정함 = 고정 DAG.

**(b) HttpServiceWorker — 범용 워커 (R5, C 권고)**
```
class HttpServiceWorker:
    alias: str                       # "gengate"
    def __init__(self, alias, base_url, unit, *, commercial=False, timeout=...): ...
    def run(self, prompt, workdir) -> WorkerResult:
        # POST {base_url}/api/generate {model: unit, prompt, commercial, opts}
        # 200 → 이미지 경로를 WorkerResult; did_act=True
```
- **전용 GenGateWorker 가 아니라 범용**: `/api/capabilities` 동형 규약(gen_gate·voice_lab·motion_lab 공통)을 워커 레벨로 흡수. 이번엔 `gengate` alias 만 등록 → 향후 voice/motion 흡수 시 **신규 워커 코드 0**(능력축 폭발 선제 차단).
- **base_url = localhost 강제 (R7)** — OllamaWorker 하드코딩 답습. 외부 URL 거부(SSRF/exfil 차단, net egress 미차단 환경).
- **견고화 (R4)**: 긴 timeout 명시(diffusion 수십 초). gen_gate 는 `_ASYNC_MODALITIES={3d}` 만 비동기 → 이미지는 동기 경로. **`202`(향후 async 편입) 수신 시 `is_error=True` fail-closed**(거짓 성공 금지). **비-200**(403 등급차단·404 미등록·500)→ `is_error=True`(dispatch 가 게이트 미진입).

**(c) kind_table / 능력 경계 (`plan_controller.py`)**
- worker_kind 는 **능력/부작용 축**(file/code/shell)으로 유지. **modality(image/3d/audio)를 kind 에 박지 않는다** → 외부 HTTP 실행 = **`service` 단일 능력축 kind** 도입(R5). modality 는 워커 인자(capabilities unit).
- `kind_table`(파이프라인 전용): `prompt`→`ollama-uncensored`, `service`→`gengate`.
- `EXECUTING_KINDS`: `service` 추가(실 부작용=이미지 파일 쓰기). **단 `service` step 은 `requires_execution=False`** 로 두어 `_EXEC_SENTINEL`/실행규약 텍스트가 이미지 프롬프트를 오염시키지 않게 함(R6).
- `SAFE_CONSUME_KINDS`: `service` 추가(R3, 텍스트 프롬프트 소비). **`allow_code_consume` off 불변.**
- ⚠️ `EXECUTING_KINDS`/`SAFE_CONSUME_KINDS` 는 전역 frozenset → 변경 시 1f/1g/1h 경고 로직·import-linter 회귀 테스트.

### 3.2 `~/prompt_lab` (신규 repo)

- **프롬프트 템플릿** — dolphin3 시스템 프롬프트(거친 의도 → animagine 친화: quality 태그·`anime-illustration` 프리셋 정렬·negative). 무검열 텍스트 저작 유도.
- **상위 레시피 / CLI 진입점** — 의도 → **고정 2-subtask DAG**(boss-free) + 전용 kind_table 구성 → ApprovalGate 제출 → 승인 시 dispatch → 이미지 경로.
- **의존 (R7, D1 해소)**: prompt_lab 은 *오케스트레이션 셸*(서비스·워커 아님). jarvis **좁은 공개 facade 직접 import**(예: `compose_plan()`/`submit_for_approval()`).
  - ⚠️ **현재 패키징(pyproject/setup) 부재** → `pip install -e` 불가. 스켈레톤은 `PYTHONPATH=<repo_root>` + `from src.jarvis...`. prompt_lab 별도 repo 의 `src/` 네임스페이스 충돌 주의. **packaging 추가는 후속 선결**(또는 얇은 API 대안).

---

## 4. 안전 가드 — 합의 ④ 3종 매핑 (R1 정정)

| 합의 가드 | 본 설계에서 | 상태 |
|-----------|-------------|------|
| **GB10 OOM cross-process lock** | 🔴 **R1**: gen_gate `gpu_guard`·`local_3d_trellis.py`·jarvis `process_control.py` 모두 **in-process threading.Lock** — **cross-process lock repo 전체 부재**. "재사용으로 충족"은 **over-claim, 철회.** | **미충족 → 실 기동 DEFER** |
| `allow_code_consume` 영구 off | `service`=텍스트 소비(SAFE_CONSUME 등록, R3). code/shell consume off 유지 | ✅ (테스트 회귀 차단) |
| fail-closed = 검열측 | `ApprovalGate` default-deny + 예외→deny + 워커 비200→is_error(R4) | ✅ |

**R1 결정**: (a) `flock`/`fcntl` cross-process lockfile **신규 구현** 후 enable, 또는 (b) **실 기동 명시 DEFER**(GPU 단독 점유 수동 보장 또는 (a) 완료까지). **스켈레톤+테스트는 GPU 무관 → 진행 가능.** 수단 선택 = 사용자 영역.

**정직한 한계 (Part 3 답습)**: capability 경계는 실행/부작용을 막지 NL injection 의미를 막지 않음. 사람 게이트는 라우팅(kind_table 매핑 alias)을 *노출*할 뿐 무검열 출력 *검증* 안 함. 무검열·서비스 워커 모두 localhost 한정.

---

## 5. Provider Liquidity (헌법 5조)

- 무검열 LLM 교체 = `OllamaWorker(model=...)` 1개. 이미지 모델 교체 = HttpServiceWorker `unit`(capabilities). **서비스 교체·신규 lab 흡수 = `base_url`+`alias`+`unit` 인자**(범용 워커 R5 가 확보하는 추가 liquidity 차원). 하드코딩 0.

---

## 6. SDD/TDD 구현 계획 (구현 단계)

1. **별도 feature 브랜치** (base=develop). R1(b) 스켈레톤 우선.
2. RED→GREEN→REFACTOR, 커버리지 70%+.
3. 테스트 = **GPU 무관**: ollama `/api/chat` + gen_gate `/api/generate` mock.
   - 고정 2-subtask DAG + depends_on 순서 + artifact in-memory 주입.
   - ApprovalRequest 에 매핑 alias 2개 노출 / default-deny / 예외→deny.
   - `service` SAFE_CONSUME 허용 ∧ code consume 여전히 off (회귀 차단).
   - HttpServiceWorker: payload 조립 / 200 경로 파싱 / **비200·202→is_error** / base_url 비-localhost 거부 / did_act.
   - `service` step `requires_execution=False` → sentinel 미주입(R6).
4. **실 e2e = DEFER**(R1). 충족 시 dolphin3 의도→프롬프트→이미지 1회.

---

## 7. 정직한 미해결 (검토 항목)

- **D1** (해소, R7): prompt_lab↔jarvis = 좁은 facade 직접 import + PYTHONPATH(패키징 후속).
- **D2** (해소): 통합 아키텍처 = 범위 한정 3+1 합의 완료(REVISE 7건 반영).
- **D3**: dolphin3 GB10(sm_121, aarch64) 실구동 미검증.
- **D4**: 한국 법·라이선스 미검토.
- **D5**: dolphin3 → 양질 이미지 프롬프트 산출 품질 미검증.
- **R6 부수**: `RedactionFilter` 가 무검열 프롬프트의 secret-유사 패턴을 마스킹해 손상시킬 가능 — 구현 시 동작 검증.

---

## 8. 다음 단계 (단계적 cycle)

검토 → 합의(완료, REVISE 7건) → **본 v2 반영 commit(현재)** → 구현(별도 브랜치 TDD, R1(b) 스켈레톤) → push. **실 기동은 R1 충족까지 DEFER.**
