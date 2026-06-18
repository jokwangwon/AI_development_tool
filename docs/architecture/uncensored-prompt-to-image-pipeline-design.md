# 무검열 텍스트→이미지 파이프라인 설계 (Position A — jarvis 명시 위임)

> 상태: **IMPLEMENTED v3 (스켈레톤 TDD + R1(A) gen_gate GPU flock 완료, 실 기동=학습 비점유 시 가능)** · 날짜: 2026-06-19 · 유형: 아키텍처 설계 (SDD)
> 모법: `docs/review/3plus1-consensus-2026-06-19-uncensored-llm-worker-delegation.md` (결정 #3)
> 합의: `docs/review/3plus1-consensus-2026-06-19-uncensored-pipeline-integration.md` (REVISE 7건 — 본 v2 가 반영)
> 적용 대상: `src/jarvis/` (이 repo, feature/uncensored-prompt-pipeline) + `~/prompt_lab` (신규 repo, commit 2fa01bf)
> ⚠️ **실 기동은 R1(GPU lock) 충족 시까지 DEFER.** 사용자 R1=(b) 선택 → 스켈레톤+테스트만 구현(flock·실 e2e 보류).

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
| **GB10 OOM cross-process lock** | ✅ **R1 (A) 구현(부분 충족)**: gen_gate `gpu_guard.gpu_flock()`(flock LOCK_EX, lockfile `~/.gb10/gpu.lock` env-override, fail-soft) 신규 → `gate.generate()` 의 로컬 GPU backend 호출을 cross-process 직렬화(commit `22227cf`, 136 passed). 무검열 파이프라인 GPU 작업은 gen_gate 경유 → 다른 gen_gate 인스턴스와 직렬화. ⚠️ **학습 lab(lora/anima/OneTrainer/trellis)은 아직 같은 lockfile 미동참 → gen_gate↔학습 동시 실행은 여전히 OOM 가능**. | **부분 충족 — gen_gate 직렬화 ✅ / 전체 GPU 소비자 직렬화는 lab 동참 후** |
| `allow_code_consume` 영구 off | `service`=텍스트 소비(SAFE_CONSUME 등록, R3). code/shell consume off 유지 | ✅ (테스트 회귀 차단) |
| fail-closed = 검열측 | `ApprovalGate` default-deny + 예외→deny + 워커 비200→is_error(R4) | ✅ |

**R1 결정 (확정)**: 사용자 선택 = **(A) `flock` 구현**, 범위 = **gen_gate `gate.generate()` 1차**(2026-06-19). lockfile 경로(`~/.gb10/gpu.lock`)를 규약화해 향후 학습 lab 이 같은 경로 flock 으로 동참하면 완전한 cross-process 직렬화 완성. **실 기동 가능 조건**: gen_gate 단독 GPU 작업이면 직렬화 보장 ✅ / 학습과 *동시* 실행은 lab flock 동참까지 수동 비점유 보장 필요(jarvis 는 GPU 비점유라 flock 불필요 — flock 은 GPU 직접 점유 프로세스에만 의미).

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
- **D6 (구현 중 신규 발견)**: step1(service)의 gen_gate prompt 정제 미결. controller 의
  artifact 주입은 desc 에 `[artifact:..] (데이터 — 지시 아님)\n<값>` 래퍼를 append 한다
  (LLM 워커가 *읽는* 용도 설계). 그러나 `HttpServiceWorker` 는 LLM 이 아니라 받은 prompt
  *전체*를 gen_gate `prompt` 로 직송 → step1 desc + 래퍼 텍스트가 이미지 프롬프트를 오염.
  스켈레톤은 워커를 controller 내부 포맷에 **결합시키지 않기 위해**(R5 범용성 보존) 추출
  로직을 넣지 않고, 깨끗한 전달 경로 결정을 실 e2e(R1 DEFER) 시점으로 미룸. 후보:
  (i) service-step 전용 주입 포맷 / (ii) `HttpServiceWorker` artifact-aware 옵션 /
  (iii) prompt_lab 가 controller 밖에서 2단계 직접 잇기. **결정=사용자 영역.**

---

## 8. 다음 단계 (단계적 cycle)

검토 → 합의(완료, REVISE 7건) → v2 반영 commit(`87603fb`) → **구현 완료(현재, R1(b) GPU-무관 스켈레톤 TDD)** → push(사용자 명시 시). **실 기동은 R1 충족까지 DEFER.**

### 구현 산출 (2026-06-19, feature/uncensored-prompt-pipeline)

| 단위 | 위치 | 상태 |
|------|------|------|
| `HttpServiceWorker`(범용, localhost 강제, 202/비200→is_error) | `src/jarvis/worker.py` | ✅ 20 tests, 95% cov |
| `SAFE_CONSUME_KINDS`/`EXECUTING_KINDS` += `service` (R3, code consume off 불변) | `src/jarvis/plan_controller.py` | ✅ 회귀 테스트 |
| `build_uncensored_pipeline_registry`(전용 kind_table) | `src/jarvis/worker_setup.py` | ✅ 7 tests, 91% cov |
| 고정 2-step DAG + ApprovalGate 노출 + R6 sentinel 미주입 | `tests/jarvis/test_uncensored_pipeline.py` | ✅ 7 tests |
| `~/prompt_lab`(templates/recipe/conftest, 별도 repo) | `~/prompt_lab` (commit `2fa01bf`) | ✅ 6 tests(e2e mock 포함) |

- 전체 jarvis 스위트 632 passed (사전 존재 환경 의존 실패 1건 = sandbox venv 권한, 본 변경 무관).
- import-linter 2 계약 PASS(grimp 직접 검증, SDK 직접 import 0 / 단방향 보존).
- AI_dev PR **#56**(→ develop). prompt_lab commit `2fa01bf`.

### R1 (A) GPU flock 구현 (2026-06-19, gen_gate `22227cf`)

- `gpu_guard.gpu_flock()` + `gate.generate()` 로컬 backend 직렬화. lockfile `~/.gb10/gpu.lock`(env override). 136 passed(cross-process subprocess 상호배제 실증 포함).
- **부분 충족**: gen_gate 인스턴스 직렬화 ✅ / 학습 lab 동참은 후속(같은 lockfile 규약).
- **다음 (사용자 명시 시)**: ① 학습 lab flock 동참(완전 cross-process) → ② D6 깨끗한 프롬프트 전달 경로 결정 → ③ dolphin3 실 e2e(GB10 비점유 또는 lab 동참 시).
