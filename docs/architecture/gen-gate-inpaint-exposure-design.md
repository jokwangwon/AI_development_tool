# gen_gate 인페인트 노출 설계 (SDD)

> 작성: 2026-06-24. 상태: **검토 완료 → 구현 진행**(2026-06-24 설계 검토: 코드 근거 전부 검증, 결함 2 + 보완 3 반영, 1-agent 승인). CLAUDE.md SDD: 별도 브랜치 `feature/gen-gate-inpaint` TDD 구현.
> 대상 repo: `~/gen_gate` (flat 구조 + 모듈별 `test_*.py` TDD 관례).
> 동기: 손·비대칭 결함 보정 레시피 ①(가장 ROI 높은 레버). 배경 = `~/lora_lab/OUTFIT_TEST_PLAN.md` 후속 + 아벨린 LoRA 품질.

---

## 1. 배경 / 문제

아벨린(상업 캐릭터 LoRA) 생성에서 **손·비대칭 다리**가 SDXL의 구조적 약점으로 반복 결함.
정찰 결과: gen_gate에 **완전한 SDXL 인페인트 백엔드가 이미 구현돼 있으나**(`backends/diffusers_sdxl.py:200-239` `inpaint()`), **gate/CLI/HTTP 어느 계층에도 노출돼 있지 않음** → 호출 불가.

인페인트 노출 시 **하나의 작은 변경으로 두 문제를 동시에 공략**:
- **비대칭**: 양쪽 검정 안정 생성 → 한쪽 다리 마스크 → "흰 스타킹" 인페인트로 비대칭 복구.
- **손**: 망가진 손 영역만 재생성 → 큐레이션 부담 ↓.

---

## 2. 목표 / 비목표 (scope 경계)

### 목표
- `gate.inpaint()` (lib) + `POST /api/inpaint` (HTTP) + `--inpaint` (CLI) 노출.
- **기존 `gate.generate()`와 동일한 등급 게이트·LoRA·flock 규약**을 인페인트에도 적용.
- **핵심 갭 수정**: 백엔드 `inpaint()`가 LoRA를 적용하도록(아래 §4-2) — 재생성 영역이 아벨린 정체성을 유지.

### 비목표 (이번 범위 ❌ — 별도 레버)
- **ControlNet-guided inpaint**(손 스캐폴드 = 레시피 ⑥): 파이프라인 교체 필요, 별도 설계.
- **마스크 에디터 UI**: 마스크는 외부(GIMP/PIL 스크립트)에서 생성 — 본 설계는 마스크를 *입력*으로 받음.
- **자동 손 탐지 인페인트**: ADetailer가 이미 담당(face_detail.py), 손 구조는 못 고침(막다른 길, [[reference_anime_hand_fix_dead_end]]).
- prompt_lab UI 연결: UI 작업은 [[feedback_ui_design_confirm_first]]대로 mockup 컨펌 후 별도.

---

## 3. 현황 (코드 근거)

| 계층 | 현재 | 파일:줄 |
|------|------|---------|
| 백엔드 inpaint | ✅ 구현 (`StableDiffusionXLInpaintPipeline`, lpw=base `.inpaint` 메서드 재사용) | `backends/diffusers_sdxl.py:180-239` |
| gate(lib) | ❌ `inpaint` 미노출 (generate/generate_chain만) | `gate.py:37-203` |
| HTTP | ❌ `/api/generate`만 (inpaint 라우트 0) | `server.py:309-369` |
| CLI | ❌ `--inpaint` 0 | `cli.py:16-44` |

### ⭐ 핵심 갭 (반드시 수정)
백엔드 `inpaint()`(200-239)는 `generate()`/`img2img()`와 달리:
1. **`_apply_lora` 미호출** + **`cross_attention_kwargs=cak` 미전달** → **LoRA가 안 먹음**. 재생성 영역이 아벨린 정체성(트리거 색·형태)을 잃음. (비교: `img2img:268`, `generate:326`은 둘 다 적용)
2. `_compose_prompt` 대신 단순 `quality_tags` join(`:223`) → 모델별 quality 위치 규약 불일치(경미).

> 인페인트의 *목적 자체*가 "캐릭터를 유지한 채 영역만 수정"이므로 (1)은 노출과 함께 **필수 동반 수정**.

---

## 4. 설계

### 4-1. `gate.inpaint()` — lib 계층 (신규)
`gate.generate()`(37-122)의 게이트·래핑 파이프라인을 **그대로 재사용**하되 backend 호출만 inpaint로:

```python
def inpaint(
    model_key: str,
    prompt: str,
    out_path: str,
    init_image,                 # 경로(str) 또는 PIL
    mask_image,                 # 경로(str) 또는 PIL. 흰색=재생성 영역
    commercial_mode: bool = False,
    registry: dict | None = None,
    style: str | None = None,
    lora: str | None = None,
    keywords: list | None = None,
    strength: float = 0.85,
    **opts,
) -> str:
```

처리 순서(= generate와 동일 헬퍼 재사용, 편차 최소):
1. `reg.get_spec` → `reg.assert_allowed(spec, commercial_mode)` — **강한 등급 게이트**.
2. **backend 제약**: `spec.backend != "diffusers-sdxl"` → `NotImplementedError`("inpaint 는 diffusers-sdxl 만 지원"). (generate_chain의 2단계 제약 `gate.py:156-160`과 동형 패턴)
3. keyword/style/lora 래핑 — generate(59-107)와 **동일 헬퍼**:
   - `lora` 주어지면: base_model 불일치 → `LoraError`; 트리거 주입 + `lora_path`/`lora_scale` opts setdefault.
   - style/keywords: 명시 시에만 합성(인페인트는 보통 minimal prompt — 호출자 선택).
   - ⚠️ **style_levers 주의**(검토 보완): `style`을 주면 `style_levers`(hires_strength·hires_scale·freeu 등)가 opts에 setdefault되는데, 백엔드 `inpaint()`는 이 키들을 `**opts`로 받기만 하고 pipe 호출에 전달하지 않아 **조용히 버려진다**(무해하나 dead). → 인페인트 경로는 style negative/prompt 만 적용하고 **levers 주입은 생략**(설계 결정). docstring 명시.
4. `gpu_flock` + `free_ollama_memory` 안에서 `diffusers_sdxl.inpaint(spec, prompt, out_path, init_image, mask_image, strength=strength, **opts)` 호출.

> 설계 결정: **`generate`에 mode 인자를 추가하지 않고 별도 `inpaint()` 함수**로 분리(단일 책임, 시그니처 명확 — init/mask는 inpaint 전용 필수 인자).

### 4-2. 백엔드 `inpaint()` LoRA 수정 (핵심 갭 §3)
`backends/diffusers_sdxl.py:200-239`를 `img2img`(242-287) 패턴에 맞춤:
- 시그니처에 `lora_path/lora_weight_name/lora_scale` 추가.
- `cak = _apply_lora(_get_pipe(spec), lora_path, lora_weight_name, lora_scale)` 호출.
- `pipe(...)` 호출에 `cross_attention_kwargs=cak` 전달.
- **권고(검토 격상)**: `full_prompt = _compose_prompt(spec, prompt)`로 통일. (기존 단순 `quality_tags` join = §3-(2)) — LoRA 정체성은 프롬프트 합성 일관성(rating·quality 위치)에 의존하므로 generate와 **동일 합성**을 쓰는 게 정체성 유지에 유리. 비용 ~0. "(선택)" → **권고**로 격상.

### 4-3. HTTP — `POST /api/inpaint` (신규)
`server.py`의 `/api/generate`(309-369) 패턴 복제:
- 요청: `{model, prompt, init_image, mask_image, strength?, commercial?, lora?, seed?, steps?, ...}`.
- `init_image`/`mask_image` = **로컬 경로**(단일 사용자 로컬 툴). § 5 보안 검증 후 gate.inpaint 호출.
- 예약 키 외 opts 통과(generate와 동일 `:318`).
- 응답: 기존과 **동형** `{id, file, url, ms, model, commercial, modality}`.
- 예외 매핑 동일: LicenseError→403, LoraError/StyleError/KeywordError→400, NotImplementedError→501, 그 외→500. 추가: 마스크/이미지 경로 무효→400.

### 4-4. CLI — `--inpaint` (신규)
`cli.py`에 추가:
- `--inpaint` (flag) + `--init <path>` + `--mask <path>` + `--strength <float>` + `--lora <key>`.
- `--inpaint` 시 `gate.inpaint(model, prompt, out, init_image=init, mask_image=mask, ...)` 호출.

### 4-5. 마스크 의미 규약 (문서화)
- **흰색(255) = 재생성 영역 / 검정(0) = 보존** (SDXL inpaint 표준). README/docstring 명시.
- 마스크 생성은 외부: GIMP 수동 또는 PIL(`ImageDraw.rectangle/polygon`, fill=255). 예시 스니펫 README 추가.

---

## 5. 보안 (HTTP 노출 시)
- `init_image`/`mask_image`가 **로컬 경로**라 HTTP 노출 시 **path traversal/임의 파일 읽기** 위험. (127.0.0.1 단일 사용자라 위협면은 낮으나 — DNS rebinding/로컬 악성 페이지 CSRF — 방어심층은 저비용이므로 적용.)
- 방어: 입력 경로를 **allowlist 디렉터리**로 제한 + `os.path.realpath` 정규화 후 prefix 검사(심볼릭 링크 탈출도 realpath로 차단). 경로가 allowlist 밖 → 400.
- ⭐ **allowlist 기본값에 `server.OUT`(생성 출력 디렉터리) 반드시 포함**(검토 결함): 가장 자연스러운 인페인트 흐름 = "방금 생성한 이미지(`OUT/outputs`에 떨어짐)의 손/다리만 재생성". OUT을 빼면 generate→inpaint 루프가 HTTP에서 400으로 막힌다.
- **allowlist 소스 = 신규 헬퍼**(검토 정정): gen_gate에는 기존 traversal 거부 헬퍼가 **없다**(`keywords.py:34`는 키 이름 regex일 뿐, `outfit_library.py`는 `_DIR`만). 그 SSRF/traversal 패턴은 **prompt_lab `library.py`**(다른 repo)에 있는 것 — gen_gate에선 **신규 작성**한다. "순수 재사용" 아님(개념만 차용). 디렉터리 목록은 env(`GEN_GATE_INPUT_DIRS`, 콜론 구분) override + 기본 `[server.OUT, ~/gen_gate/inputs]`.
- CLI는 로컬 신뢰 경계(사용자 본인) → 경로 제한 불필요(생성물 out_path와 동일 신뢰).

---

## 6. TDD 테스트 계획 (RED 먼저 — `test_gate.py`/`test_server.py`/`test_cli.py`/`test_diffusers_sdxl.py`)

### 계산적(센서) — GPU 불요(모킹)
1. **게이트**: `gate.inpaint`가 비상업 모델 + commercial_mode → `LicenseError`(generate와 동일).
2. **backend 제약**: diffusers-sdxl 아닌 모델(qwen/anima) → `NotImplementedError`.
3. **⭐ LoRA 적용**(핵심 갭 회귀 방지): `lora` 주어지면 트리거 프롬프트 주입 + 백엔드 inpaint가 `_apply_lora` 호출(cak non-None) — 모킹으로 cak 전달 검증.
4. **LoRA base 불일치**: → `LoraError`.
5. **백엔드 inpaint 단위**: `cross_attention_kwargs=cak`가 pipe 호출에 전달됨(현재 누락 = RED).
6. **HTTP**: `/api/inpaint` 정상 200 + 응답 스키마 / 무효 모델 404 / 비상업+commercial 403.
7. **보안**: `/api/inpaint` init/mask가 allowlist 밖 경로 → 400(traversal 거부). **+ OUT 하위 경로는 허용**(generate→inpaint 루프 회귀 방지, 검토 결함).
8. **CLI**: `--inpaint --init --mask` → gate.inpaint 호출(인자 매핑).
8b. **치수 가드**(검토 보완): mask 크기 ≠ init 크기 → 명확한 `ValueError`(HTTP 400). 암묵 리사이즈/파이프 에러 방지.

### 추론적/e2e — GPU 필요(다른 세션 GPU 비점유 시)
9. **실 e2e**: 아벨린 이미지 + 한쪽 다리 마스크 → "white thigh-high stocking" 인페인트 → 정체성 유지 + 해당 다리만 변경(육안 + md5 변화). LoRA on 시 트리거 색 일관.

> ✅ **e2e PASS (2026-06-24, GB10)**: init=`combo3_d_s999.png`(1536², 흰+검 비대칭 스타킹), 뷰어-좌측 흰 다리 마스크 → "black thigh-high stockings" 인페인트(animagine 상업 + LoRA aveline). **풀 경로 작동**(gate→flock→backend inpaint→LoRA, 에러 0). **영역 한정 정확**: 마스크 안 diff 71.16 / 밖 2.50(~28×, 얼굴·드레스·날개·반대쪽 다리·배경 전부 보존). **strength=1.0에서 흰→검 완전 전환**(비대칭→대칭 복구, 육안 컨펌). ⭐ **발견: strength = 색 전환 레버** — 0.85는 원본 흰색이 강하게 보존(LoRA on/off 무관, 둘 다 흰색 유지)되고 1.0에서 완전 재생성. 초기 가설 "LoRA가 흰색 정체성 재주장"은 **오답으로 정정**(원인=strength, LoRA 아님). LoRA의 inpaint 내 *구별되는* 효과는 이 A/B로 분리 못 함(matched strength에서 둘 다 흰색); 핵심 갭 CODE는 단위테스트(cak 전달)+e2e 무에러로 검증. 산출=`~/lora_lab/inpaint_e2e/`.

> 커버리지 70%+ (CLAUDE.md). 1~8은 GPU 없이 즉시 가능, 9는 GPU 슬롯 대기.

---

## 7. 의존성 / 영향
- **변경 파일**: `gate.py`(+inpaint), `backends/diffusers_sdxl.py`(inpaint LoRA 수정), `server.py`(+route), `cli.py`(+flags), 각 `test_*.py`, `README.md`.
- **기존 동작 영향 0**: generate/generate_chain/img2img 무변경. 백엔드 inpaint LoRA 추가는 **순수 가산**(기존 호출자 0 — 미노출이었으므로 회귀 위험 없음).
- **provider liquidity**: backend 제약은 diffusers-sdxl 한정이나, 향후 다른 backend inpaint는 BACKENDS 등록 패턴으로 확장 가능.
- 수락 시 AI_dev CLAUDE.md §8 참조 테이블에 본 문서 등록(후속).

---

## 8. 복잡도 평가 (합의 프로토콜 적용 여부)
- **1-agent 직접 구현** (사용자 승인, 2026-06-24 설계 검토). 근거: 기존 함수의 **노출**(신규 아키텍처 아님) + 등급 게이트·LoRA·flock 규약 재사용 + 영향 가산적. CLAUDE.md §3 매트릭스 "중간 규모 기능 = 1~2" 하단. [[feedback_ceremony_inflation]] 답습(과한 ceremony 차단).
- ⚠️ **CLAUDE.md §3 "보안 변경 = 3+1 필수"에서 의도적 하향**: 이 결정은 ① 127.0.0.1 단일 사용자 로컬 툴([[feedback_proportionate_security_personal_tool]] 비례 보안), ② traversal = 잘 알려진 패턴이라 테스트 7번으로 충분 강제, ③ 신규 아키텍처 아닌 노출 — 세 근거로 사용자가 명시 승인. 향후 인증/네트워크 노출 확대 시 재평가.
- 보안(§5 path traversal)은 테스트 7번(+ OUT 허용)으로 강제 검증.

---

## 9. 미래 확장 (본 설계가 여는 길)
- 인페인트 노출 → **비대칭 데이터 생성** 가능 → loop-3 LoRA가 비대칭 흡수(프롬프트로 안 싸움). `OUTFIT_TEST_PLAN.md` 비대칭 사다리 ③.
- ControlNet-guided inpaint(레시피 ⑥)는 이 인페인트 경로 위에 `conditioning_image`만 추가하는 구조 → 본 설계가 선행 기반.

---

## 부록: 호출 예시 (수락 후)
```python
# lib
import gate
gate.inpaint("animagine-xl-4.0", "white thigh-high stocking",
             "out.png", init_image="aveline.png", mask_image="left_leg_mask.png",
             commercial_mode=True, lora="aveline", strength=0.85)
```
```bash
# CLI
python cli.py --model animagine-xl-4.0 --inpaint \
  --init aveline.png --mask left_leg_mask.png \
  --prompt "white thigh-high stocking" --lora aveline --commercial -o fixed.png
```
```python
# 마스크 생성(외부, PIL)
from PIL import Image, ImageDraw
m = Image.new("L", Image.open("aveline.png").size, 0)   # 0=보존
ImageDraw.Draw(m).rectangle([x1, y1, x2, y2], fill=255) # 255=재생성(왼다리)
m.save("left_leg_mask.png")
```
