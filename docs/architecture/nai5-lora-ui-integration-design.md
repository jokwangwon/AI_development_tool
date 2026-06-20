# NAI5 LoRA UI 통합 설계 (SDD)

> 학습한 `@NAI5` 그림체 LoRA(AnimaYume/Cosmos DiT)를 gen_gate/prompt_lab UI에서 생성 가능하게 통합.
> 경로 A(lab 추론 브리지) + 상주 inference_server 확정(사용자 승인 2026-06-20).
> 상태: **APPROVED — 3+1 합의 통과(2026-06-20), TDD 구현 진행**. 합의 fix는 §9 반영.
> 합의 판정: A(구현)=GO-with-fixes · B(안전)=SAFE-with-fixes · C(대안)=채택안 GO(변경0). 방향 만장일치.

---

## 1. 배경 / 문제

- NAI5 LoRA(`~/anima_lora_lab/anima_lora/output/ckpt/nai5_v05.safetensors`, 92MB, rank32, @NAI5 트리거)는 GB10 aarch64에서 본 학습 완료·그림체 눈 컨펌. 그러나 **gen_gate/prompt_lab UI에서 사용 불가**.
- gen_gate `diffusers-anima` 백엔드는 diffusers 모듈러 파이프라인(`AnimaAutoBlocks().init_pipeline`)으로 DiT를 HF repo에서 로딩 → **LoRA 로딩 코드 0**.
- LoRA 출력 포맷 = `net.` 프리픽스 공식/ComfyUI 포맷(lab `save_anima_model`, sd-scripts 컨벤션) ≠ diffusers 키 → **포맷 불일치**가 직접 로딩의 벽.

## 2. 핵심 발견 (정찰)

| 자산 | 사실 | 함의 |
|------|------|------|
| lab `scripts/inference_server.py` | **완성된 상주 HTTP 추론 서버**. `POST /generate`에 `lora_weight`/`lora_multiplier` 파라미터 내장. pidfile discovery(`~/.anima/inference.json`), `/health`·`/unload`·`/stop`, idle TTL, 협조적 eviction | **NAI5 LoRA 로딩이 서버측에 이미 구현됨**. lab 코드 변경 0 |
| lab 추론 경로 | NAI5 그림체 컨펌이 **lab 단독 경로**(`cmd_test`/서버)로 됨 | 그림체 출력 자체는 실증됨 — 키 변환 불요. ⚠️ **gen_gate→서버 통합 경로는 미실증**(§7 e2e에서 검증) |
| gen_gate `gpu_guard.gpu_flock()` | `gate.py`가 local 백엔드를 `with gpu_flock(): free_ollama_memory(); backend(...)`로 감쌈 | 신규 local 백엔드는 **자동으로 GPU 직렬화 편입**(`~/.gb10/gpu_lock`) |
| gen_gate `local_3d_trellis.py` | subprocess→별도 venv 백엔드 패턴 확립(env override, 하드코딩 0) | 신규 백엔드의 템플릿 |

⭐ **merge_to_dit 불필요화**: 직전 세션의 계획은 "merge_to_dit → 공식포맷 single-file → 백엔드가 변환·로딩". 그러나 상주 서버가 `lora_weight`를 **로드 시 직접 적용** → merge·키변환 경로 전체가 critical path에서 제거. (merge_to_dit는 lab 독립 도구로 잔존, UI 통합엔 미사용.)

## 3. 아키텍처

```
prompt_lab (UI, 8780)
   │  사용자: 모델=anima-nai5 선택 → 프롬프트 → 생성
   ▼
gen_gate HTTP (server.py, 8770)  ─ /api/generate
   ▼
gate.generate(model_key="anima-nai5", ...)
   │  등급 게이트(commercial=false → 개인 전용) → with gpu_flock():
   ▼
backends/anima_lab.generate(spec, prompt, out_path, ...)
   │  ① discover_base_url(~/.anima/inference.json)
   │  ② 없으면 lab venv python 으로 `inference_server serve` 기동(detached) + /health 폴링
   │  ③ POST /generate {prompt(@NAI5 주입), negative, width/height, steps, cfg,
   │                     seed, lora_weight=[nai5_v05.safetensors], save_path=out_path}
   ▼
lab inference_server (8766, ~/anima_lora_lab/.venv)  ← 코드 변경 0
   │  warm DiT(AnimaYume v05)+TE+VAE, LoRA 적용, 생성 → save_path 에 저장
   ▼
out_path 반환 → gen_gate → prompt_lab 렌더
```

GPU 동시 점유 방어: gen_gate가 `gpu_flock()`을 **동기 HTTP 호출 전체 구간** 보유 → 서버의 실제 GPU 작업이 flock 보유 중 일어남. 서버 자체는 flock 미동참(불요). ⚠️ 카운터: lab 서버를 gen_gate 우회 직접 호출 시 flock 없음(TRELLIS와 동일 한계, 문서화).

## 4. 변경 범위

### 4.1 lab (`~/anima_lora_lab`) — **변경 0**
서버가 이미 `lora_weight` 지원. (선택: warm 기동 편의 스크립트만 추가 가능, 비필수.)

### 4.2 gen_gate (`~/gen_gate`) — 주 작업
1. **신규 백엔드 `backends/lab_inference.py`** (파일명 일반화 — C 권고1, spec에서 url/lora/trigger 주입):
   - `_discover_server()`: lab pidfile(`~/.anima/inference.json`) → base_url, env `ANIMA_INFERENCE_URL` override.
   - `_ensure_server()`: down이면 `_venv_python()`(env `ANIMA_LAB_VENV`, 기본 `~/anima_lora_lab/anima_lora/.venv/bin/python`)로 `scripts/inference_server.py serve --warm` 기동 + `/health` 폴링. **module-level Lock으로 spawn 직렬화(이중 기동→OOM 차단, R1)** · `start_new_session=True` + stdin/out/err 리다이렉트(고아화 방지, R2) · `shell=False` 리스트 인자(인젝션 차단).
   - `generate(spec, prompt, out_path, *, seed=None, steps=None, size=None, negative=None, cfg=None, **opts)`: ① **트리거 멱등 주입**(`@NAI5` 중복 방지) ② **size→`{width,height}` 명시 매핑**(F1) ③ `lora_weight`는 **spec에서만**(opts의 SDXL `lora_*` 무시, F1/BLOCKING-3) ④ POST `/generate`(save_path=out_path) ⑤ `resp["ok"]` 검사→비-200/`ok:false`면 RuntimeError. **HTTP 타임아웃=분 단위(기본 ~600s, 3600s 아님, F2)**.
2. **`gate.py` BACKENDS 에 `"lab-inference": lab_inference.generate` 등록.**
3. **`model_registry.json` 신규 엔트리 `anima-nai5`** (noobai 동형 정렬):
   - `modality: image`, `category: anime`, `backend: lab-inference`
   - `lora_weight: <nai5_v05 **절대경로**>`(R3, env override·expanduser), `trigger: "@NAI5"`
   - `license: circlestone-non-commercial (derivative)`, **`commercial: false`** + **`personal_use_only: true`** + **`tier: "personal"`**(BLOCKING-1, noobai 동형)
   - **`attribution`**: base 상속 — "Derivative of Anima(CircleStone NC) / Cosmos-Predict2(NVIDIA Open Model License)"(BLOCKING-1)
   - **`rating: "safe"`** (표시용, 차단 아님 — 2축 분리; nsfw_capable은 base와 동일 미부여)
   - `negative`: 직전 세션 보강(`2girls, multiple views, reference sheet` 포함)
   - `quality_tags`: 비움(Anima native 긴 프롬프트), `defaults: {steps, cfg, size}`
   - `notes`: 개인 전용·NAI5 데이터 출처·lab 서버 경유 + **"4축상 베이스=anima/캐릭터=NAI5 합성 모델"**(C 권고4)

### 4.3 prompt_lab — **변경 0 (자동 노출)**
`anima-nai5`가 `/api/models`에 뜨면 기존 패싯 필터(용도=일러스트, 라이선스=개인)로 자동 노출. UI 코드 변경 불요(2차 세션 패싯 인프라 재사용).

## 5. 설계 결정 (3+1 합의로 확정 — 전부 채택)

| # | 결정 | 확정 | 합의 근거 |
|---|------|------|------------|
| D1 | NAI5를 **모델**(`anima-nai5`)로 등록 | ✅ 모델 | A·C 독립 확인: gen_gate LoRA 레지스트리는 in-process diffusers LoRA(`gate.py:90-105`, SDXL `load_lora_weights`) 전용. lab 서버 자체 적용과 구조 다름. 공유 backend + JSON 한 줄이라 폭발 없음. 멘탈모델 정합은 notes로 보존(C 권고4), D3 통합 후 자연 해소 |
| D2 | 서버 라이프사이클: **auto-spawn-if-down** | ✅ auto-spawn(discover-first) | 사용자 개입 최소화. spawn 직렬화+생존 강화는 §9. systemd 1급 운영모드는 **문서 권고만**(C 권고3, GB10 단일·개인 툴이라 설치 스텝 비례성상 fallback이 기본) |
| D3 | base "anima"는 **diffusers-anima 유지**, 공존 | ✅ 공존 | C 정량: 즉시 통합은 검증된 경로(2026-06-18, 125 tests + 만화/VTuber 의존) 폐기 + 범위 폭증. 공존은 올바른 시퀀싱. **조건부 후속 트리거는 §8** |
| D4 | merge_to_dit **미사용** | ✅ 미사용 | 서버가 lora_weight 직접 적용. 경로 B(diffusers 변환)는 venv 양립 불가(C 실증) + 미검증 변환기 |

## 6. 라이선스 / 안전 (B-검증가 관점)

- NAI5 LoRA = **Anima(CircleStone NC) 베이스의 Derivative** + NAI5 그림체 데이터(ilxl/Civitai 627장) 학습 → **이중 비상업 소스 → 개인 전용**. noobai 동형으로 `commercial:false` + `personal_use_only:true` + `tier:"personal"` 강제 → 상업 모드에서 `assert_allowed`가 `LicenseError`로 차단(`registry.py:67`), 상업 패싯에서 숨김(개인 패싯에서만 노출). **B 검증: `noobai`만 두 플래그를 갖고 NAI5만 `commercial:false`면 패싯 분류 비대칭 → 세 필드 모두 정렬 필수(BLOCKING-1).**
- **attribution 상속(BLOCKING-1)**: base anima의 `attribution`(Cosmos-Predict2/NVIDIA Open Model License)을 NAI5도 상속 명기. NAI5 = Anima 파생 = Cosmos-Predict2 2차 파생.
- ⚠️ 별개 기존 버그: `anima-base-v1` 엔트리 `commercial: true` ↔ `license non-commercial`. base는 "가중치 NC but 출력 상업 OK" 2축 논리. NAI5는 학습 데이터 출처 때문에 **출력도 개인 전용**으로 보수 적용(base와 다름). 이 차이를 notes에 명기. (base 엔트리 정정은 **별도 권고 유지** — 이번 범위 밖, NAI5는 답습 안 함.)
- **콘텐츠 축**: `rating:"safe"` 명시(base 동형). **표시용이지 차단 게이트 아님**(무검열 설계 2축 분리 원칙). nsfw_capable은 base와 동일 미부여.
- 콘텐츠/법 판단 = 사용자 감독(무검열 설계 원칙 유지).

## 7. 검증 계획 (TDD + 시각)

- **계산적(TDD)**: `test_lab_inference.py` — discover(pidfile 유/무), ensure_server(mock subprocess+health·spawn 직렬화), generate(size→width/height 매핑·lora_weight spec-only/opts 무시·트리거 멱등 주입·negative 전달·`ok:false`→RuntimeError). `test_gate.py`·`test_registry.py` — anima-nai5 dispatch·commercial=false 게이트(상업 모드 차단). `test_server.py` — `/api/models`에 anima-nai5 노출.
- **시각(실 이미지)**: lab 서버 기동 → gen_gate 경유 @NAI5 e2e 1장(은발 성숙 일러스트 확인) + commercial 게이트 실차단 확인. ⚠️ **통합 경로 실증은 이 단계에서 처음**(§2 down-scope).
- **회귀**: 기존 gen_gate 245 passed 유지. diffusers-anima(base) 무영향.

## 8. 잔여 / 후속

- **[조건부 ADR 트리거]** lab-server-anima로 base anima 통합(D3) → diffusers-anima deprecate 재평가는 **"anima-lab e2e 안정 + LoRA 2개 이상 등록" 시점**에 발동(C 권고2 — 공존이 영구 부채로 굳는 것 방지).
- NAI5를 정식 LoRA 축으로 이전(D1) — 통합 런타임 후.
- **[운영 권고]** lab inference_server를 systemd user service로 두면 책임 경계가 깨끗(C 권고3). 현재는 auto-spawn fallback 기본.
- NAI5 그림체 미세조정(풀바디 구도·캐릭터 편향, 직전 세션 후보 ②).
- merge_to_dit 별도 TDD(ComfyUI 배포용, UI 무관).

## 9. 구현 제약 (3+1 합의 반영 — 구현 시 필수)

**BLOCKING (전부 §4.2/§6에 반영됨):**
1. `lora_weight`·`negative`는 **spec에서만** 도출, 호출자 `opts`의 SDXL `lora_*` 키 무시 (A F1 + B BLOCKING-3) — 임의 safetensors 경로 로딩 차단.
2. `size` 단일값 → 서버 `{width, height}` **명시 매핑** (A F1) — 누락 시 사용자 size 무시 silent bug.
3. registry `lora_weight` = **절대경로**(`expanduser`) (A R3) — detached 서버 cwd 불확실.
4. auto-spawn: **module-level Lock으로 spawn 직렬화**(A R1, 이중 기동→OOM) + `start_new_session=True` + I/O 리다이렉트(A R2, 고아화) + `shell=False` 리스트 인자(B 권고).
5. 백엔드 HTTP **타임아웃 분 단위**(~600s, 3600s 아님) (A F2 + B) — cold-start는 `--warm`해도 첫 `/generate`에서 DiT 로드됨 인지(폴링 여유).
6. 라이선스 메타데이터 noobai 동형 + attribution 상속 (B BLOCKING-1).

**SHOULD:**
7. `out_path`를 gen_gate `OUT` 하위로 제약(traversal 거부) (B BLOCKING-2) — gen_gate가 이미 `os.path.join(OUT, fn)`로 생성하므로 방어심층(LOW).
8. backend 파일명 `lab_inference.py` + spec 주입(C 권고1) — 추후 임의 HTTP 추론서버 일반화 비용↓ (지금 일반화는 YAGNI).

**정찰 정정:** LoRA 실제 **88MB**(설계 초안 "92MB" 오기).
