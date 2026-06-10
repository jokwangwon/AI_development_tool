# 토킹헤드 모션 설계 (Talking-Head Motion Design)

> **정적 anime 일러스트 + 음성(WAV)을 "말하는 캐릭터 클립"으로 만드는 모션 계층 설계 — 비전의 마지막 미싱 피스(이미지 + 음성 + **모션**)**

**최종 수정**: 2026-06-10 (BLOCKING 5건 결정 → motion_lab 독립 repo 구현 → 3-서비스 라이브 dogfood → **D-2 2단계 Allosaurus 교체** → **blink/head idle 모션**)
**상태**: **구현 완료 3차 (blink/head idle 모션 — 결정적 함수·해시 지터 blink·mouth disjoint 가산 합성·81 tests green + 실 e2e mp4 blink 시각 확인). 후속 = 실 3-연쇄 생성·motion_lab remote)**
**구현 repo**: `~/motion_lab` (독립 git repo, main: `c479c5a` 승격 + `8bf127e` 렌더러/서버 + D-2 2단계 커밋)
**상위 문서**: `PROJECT_CONSTITUTION.md` 제3조(에셋), 제5조-2(Provider Liquidity)
**관련 문서**: `generative-ai-asset-pipeline-design.md`, `generative-ai-extensibility-design.md`, `ai-backend-stack-convention.md`
**합의 보고서**: `docs/review/3plus1-consensus-2026-06-10-talking-head-motion.md`
**외부 repo**: `~/gen_gate`(이미지/3D), `~/voice_lab`(음성), `~/comic_lab`(만화), `~/motion_lab`(본 설계 PoC 스크래치)
**근거 메모리**: `reference_talking_head_lipsync_landscape`

---

## 1. 개요

### 1.1 문제

`gen_gate`(이미지)·`voice_lab`(음성)은 동일 `/api/capabilities` 규약으로 발견·조립되어
**이미지 + 음성** 토대가 확립됐다(2026-06-09). 비전의 "애니메이션 한 컷 = 말하는 캐릭터"를
완성하려면 마지막 조각인 **모션**(음성에 맞춰 움직이는 입·표정)이 필요하다.

### 1.2 조사 결론 (딥리서치 2라운드 + PoC 2건, 2026-06-10)

| 발견 | 근거 |
|------|------|
| **실사 토킹헤드 전부 anime 부적합** | SadTalker·MuseTalk·AniPortrait·Sonic·EchoMimic·Hallo 모두 실사 얼굴(3DMM·landmark·insightface) 전용. SadTalker 공식 "only works on REAL people" |
| **THA3(talking-head-anime-3)가 anime 유일 적합** | 512² 알파 일러스트 1캐릭터, 45-dim 포즈 벡터. but **pose 구동(오디오 아님)** → audio→viseme 브리지 필요 |
| ⭐ **THA3 GB10 sm_121 구동 실증** | 헤드리스 로드 1.4s · **~33ms/frame ≈ 30fps(raw GPU 추론 한정)** · 알파합성 CPU 루프 포함 실 throughput **~18fps** · GPU 1.8GB · 기존 torch 2.12.0+cu130 재사용(insightface/onnxruntime/3DMM 의존 0) |
| ⭐ **viseme 직접 노출** | `mouth_aaa(26)/iii(27)/uuu(28)/eee(29)/ooo(30)` — 모음 음소가 파라미터로 직결 → phoneme→viseme = 단순 lookup |
| ⭐ **전체 루프 닫힘** | 실 WAV(voice_lab 한국어 6.5s) → RMS+LPC 포먼트 → viseme 트랙(195프레임) → THA3 렌더 → ffmpeg mp4. **전부 로컬·frontier 0** |
| Live2D/Inochi 우위 무의미화 | Live2D의 유일 장점(CPU·HW안전)은 THA3가 GB10에서 도는 이상 불필요. THA3는 리깅 노동 0(일러스트 1장 즉시)이라 자동화 가치 보존 |
| ⚠️ **THA3 5모음 viseme 천장** | 노출 viseme = `aaa/iii/uuu/eee/ooo` 5모음뿐(자음·양순폐쇄 m/b/p 없음). **모든 audio→viseme 프론트엔드(포먼트/MFA/Allosaurus)의 정밀도 이득이 5모음으로 양자화 소실** → D-2 교체 ROI의 핵심 전제. 입 자연스러움은 프론트엔드 교체보다 45-dim 내 jaw/입꼬리 활용이 더 큰 레버일 수 있음(3+1 합의 C 지적) |

### 1.3 설계 원칙

| 원칙 | 설명 | 근거 |
|------|------|------|
| **Local-First** | 렌더러·브리지 전부 로컬(GB10). frontier 0 | `comic_lab`/`gen_gate` 기조 답습 |
| **Composable Service** | 모션은 이미지·음성을 *소비*해 영상을 *생산*하는 독립 서비스. `/api/capabilities` 규약 공유 | voice_lab 분리 패턴 답습 |
| **Renderer/Bridge 분리** | (a) THA3 렌더러(image+pose track→frames) (b) audio→viseme 브리지(audio→pose track). 둘은 독립 교체 가능 | Provider Liquidity(제5조-2) |
| **등급 게이트 일관** | gen_gate 라이선스 게이트와 동일 — 모델 weight 라이선스 + 출력 상업화 가능 여부 추적 | `registry.py` 답습 |
| **결정성 우선(브리지)** | audio→viseme 프론트엔드는 결정적 계산 우선(포먼트/음소정렬), neural은 품질 부족 시 보조 | CLAUDE.md §2 계산적 우선 |

---

## 2. 아키텍처

### 2.1 컴포넌트 분해

```
                    ┌─────────────────────────────────────────────┐
                    │  오케스트레이터 (애니메이션 앱 / comic_lab)    │
                    │  "말하는 컷 하나 만들어줘"                     │
                    └───┬──────────────┬──────────────┬───────────┘
                        │ image        │ audio(WAV)   │ motion
                        ▼              ▼              ▼
                  ┌──────────┐   ┌──────────┐   ┌────────────────────────┐
                  │ gen_gate │   │voice_lab │   │   motion_lab (신규)      │
                  │ 일러스트  │   │  음성     │   │  ┌──────────────────┐  │
                  └──────────┘   └──────────┘   │  │ ① audio→viseme   │  │
                       │ 512²RGBA      │ WAV    │  │    브리지         │  │
                       └───────────────┴───────►│  │  (audio→pose)    │  │
                                                 │  └────────┬─────────┘  │
                                                 │           ▼ pose track │
                                                 │  ┌──────────────────┐  │
                                                 │  │ ② THA3 렌더러     │  │
                                                 │  │  (image+pose→     │  │
                                                 │  │   frames@30fps)  │  │
                                                 │  └────────┬─────────┘  │
                                                 │           ▼ frames+wav │
                                                 │  ┌──────────────────┐  │
                                                 │  │ ③ mux (ffmpeg)   │  │
                                                 │  └────────┬─────────┘  │
                                                 └───────────┼────────────┘
                                                             ▼ talking clip (mp4)
```

### 2.2 motion_lab 서비스 인터페이스 (capabilities 규약 답습)

gen_gate/voice_lab와 동형 envelope:

```
GET /api/capabilities
→ {service:"motion_lab", unit_param:"renderer", modalities:["video"],
   units:[{id:"tha3-standard-float", modality:"video", commercial:true,
           license:"cc-by-4.0", attribution_required:true,
           label:"THA3 anime talking-head"}]}

POST /api/generate {renderer:"tha3-standard-float", image:<png|ref>, audio:<wav|ref>,
                    image_commercial:<bool>, audio_commercial:<bool>,
                    bridge:"formant", fps:30, ...opts}
→ {job_id}                    # async (사용자 결정 확정, 아래 ✅)
GET /api/jobs/<job_id>        → {status, file?, url?, ms?, attribution?}
→ 최종 {id, file:"<id>.mp4", url:"/outputs/<id>.mp4", ms, modality:"video",
        attribution:"THA3 talking-head-anime-3 © Pramook Khungurn (CC BY 4.0)"}
```

- **unit_param = `renderer`**: 오케스트레이터가 서비스 내부 모르고 단위 선택(provider liquidity 서비스판).
- ✅ **async job 확정 (3+1 합의 A 권고 = 사용자 결정 2026-06-10, D-1)**: PoC 실측상 6.5s 클립=195프레임,
  알파합성 포함 ~18fps → 약 11s+mux. 클립 길이·동시요청에 비례해 동기 HTTP 가 타임아웃/블로킹되므로
  **async job 패턴 채택**: `POST→{job_id}` 즉시 반환 + `GET /api/jobs/<id>` 상태 폴링. (max_duration 게이트는 미채택.)
- ✅ **attribution 출력 응답 포함 (사용자 결정 2026-06-10, D-3)**: registry 의 `attribution_required:true`
  단위는 generate 최종 응답에 `attribution` 필드를 실어 오케스트레이터가 표시 책임을 인지. repo NOTICE 와 이중 보장(§4.4).
- ⚠️ **합성물 등급 AND-clamp (3+1 합의 B·C, BLOCKING D-3)**: 출력 상업화 = `image_commercial ∧
  audio_commercial ∧ renderer.commercial` (3자 중 가장 보수적). `voice_lab/server.py:69-73`
  fail-closed 선례 답습 — 1개라도 비상업이면 commercial 모드 요청 차단(§4.3).

### 2.3 핵심 차별점 — 모션은 *합성*이고 *운영 라이프사이클*이 다르다

> 3+1 합의 C 정정: gen_gate 가 입력 이미지를 못 받는 게 아니다(`backends/local_3d_hunyuan.py`가
> 이미 prompt 없이 image-only 로 mesh 생성). 따라서 "2모달리티 충돌"은 진짜 차단 사유가 아니다.

독립 서비스를 권하는 **진짜 근거 = 운영 라이프사이클 분리**:
- THA3 는 **GPU 상주 모델**(1.8GB warm)이고 **30fps 프레임 루프 + ffmpeg mux + 프레임 시퀀스 I/O**
  를 운영한다 — gen_gate 의 stateless 단발 생성과 라이프사이클이 다르다. 모션을 gen_gate 에 넣으면
  gen_gate 책임이 비대해진다(비디오 파이프라인·job 큐).
- 단 **게이트 로직(load_registry/select/assert_allowed)은 복제 금지** → gen_gate 공유 모듈로
  재사용(§5). 복제 시 라이선스 규칙이 두 곳에서 갈라져 Provider Liquidity·단일출처 위반.

---

## 3. 미결정 사항 (사용자 결정 고정 영역 — 3+1 합의 권고)

> CLAUDE.md §3: 아키텍처 의사결정 = 3+1 합의 필수. 아래는 합의 입력이자 사용자 최종 결정 항목.

> **3+1 합의 결과(만장일치 REVISE)**: 방향 전부 승인, 근거·라이선스·계약 보완. 합의 권고를 아래
> 반영했고, **사용자 BLOCKING 5건은 2026-06-10 결정 완료**(✅ 표시). 결정은 전부 합의 권고와 일치.

### D-1. 배치: 독립 `motion_lab` 서비스 [합의 만장일치, high]

**독립 motion_lab 서비스 채택.** 단 근거는 §2.3 정정대로 **운영 라이프사이클 분리**(GPU 상주·30fps
루프·ffmpeg/job 운영). capabilities envelope = gen_gate/voice_lab 동형. 게이트 로직은 복제 금지,
gen_gate 공유 모듈 재사용(§5).
- ✅ **generate 계약 형태 = async job (사용자 결정 2026-06-10)**: `POST→{job_id}` + `GET /api/jobs/<id>`
  상태 폴링. max_duration 게이트는 미채택. 긴 클립·동시요청 확장 대비(§2.2).

### D-2. audio→viseme 브리지 프론트엔드 [합의 만장일치]

**브리지 계약 `bridge.analyze(wav,fps)->List[{vowel,amount}]` 먼저 고정.** 단계적 접근:

| 단계 | 내용 | 근거 |
|------|------|------|
| **1단계 (교체 전, 권고)** | **포먼트 분류기 자체 수정** — `ooo(480,900)`/`uuu(350,800)` 중심값 재캘리브레이션 + 무성 폴백을 `mouth_aaa` 강제 → **'직전 viseme 유지'**로 변경 + 시간 스무딩 | 편향(iii 과다·ooo 0) 원인은 분류기 결함. 검증된 결정적 경로 유지(§2 계산적 우선·비례성) |
| **2단계 (교체, ✅ 구현 완료 2026-06-10)** | `bridge.analyze` 계약 뒤 **Allosaurus** phone-level 프론트엔드(다국어·텍스트 불필요·경량) — IPA phone(timestamp) → 추상 5모음 매핑. **MFA 2순위(미착수)** | provider liquidity — 코드 변경 0 교체 |

- ~~Rhubarb~~ **후보 제거**(영어 전용 → 한국어 비전 모순, 딥리서치·합의 일치).
- ⚠️ 모든 프론트엔드 이득이 **THA3 5모음 viseme 천장**(§1.2)으로 양자화됨을 ROI 전제로 인지.
- ✅ **우선순위 = 포먼트 자체수정(1단계) 먼저 (사용자 결정 2026-06-10)**: 5모음 천장으로 교체 ROI 가
  제한적이고 편향 원인이 분류기 결함이므로, 검증된 결정적 경로(포먼트 재캘리브레이션 + 폴백 '직전 viseme
  유지' + 스무딩)를 먼저 적용. Allosaurus 교체(2단계)는 1단계 후 dogfooding 으로 ROI 재평가.
- ✅ **2단계 구현 결정 (사용자 결정 2026-06-10)**:
  - **프론트엔드 선택 = env `MOTION_BRIDGE_FRONTEND`**(기본 `allosaurus`, `formant` 옵션). `analyze(wav, fps)`
    시그니처 **불변** — 교체가 계약/호출부를 오염시키지 않음(Provider Liquidity, voice_lab/gen_gate 모델 교체 패턴 동형).
  - **기본값 = allosaurus** — ROI 실측이 명확(아래). LPC(formant)는 폴백/경량 옵션으로 보존.
  - **IPA→5모음 매핑 외부화**(`IPA_TO_VOWEL`, §4.2) — 한국어 단모음 + 변이음(ʌ→aaa·ɯ→uuu·ɪ→iii·ɔ→ooo)·장음(iː/eː/oː)·æ 커버.
  - **공유 후처리(프론트엔드 무관)**: 절대 dBFS 무음→닫힘 · 무성/공백=직전 viseme 유지 · 단발 spike 스무딩 ·
    amount = 프레임 RMS. → 1단계·2단계가 silence/edge/amount 로직을 공유(중복 0).
- ⭐ **ROI 실측 (speech.wav 한국어 6.5s, poc_allosaurus.py 비교 진단)**: LPC 1단계가 **구조적으로 못 낸 ooo
  복구**(0 → 11~37 frames), iii 쏠림 해소, **5모음 전부 등장**(LPC=4모음). 추론 ~0.8s. 1단계 docstring 의
  "실 모음 품질은 2단계가 실측으로 정당화" 예측이 **실측으로 입증**. (test_bridge_allosaurus.py 실 e2e 회귀 가드)
- ⚠️ **정직한 한계**: 이득은 여전히 5모음 천장으로 양자화. uuu 는 이 클립에서 6frames(낮음)이나 LPC 의
  ooo=0 같은 *구조적* 누락은 아님(클립 내용 반영). capabilities label 모음 정확도 over-claim 금지 유지.

### D-3. 라이선스 등급 — THA3 weight + 출력 상업화 [합의 다수, ✅ 결정 완료]

> **합의가 잡은 사실 오류**: 기존 'commercial:false 보수 표기'는 **과소차단(부정확)**.

- ✅ **실측 라이선스 정정 채택 (사용자 결정 2026-06-10)**: THA3 코드 = **MIT**(Pramook Khungurn 2022),
  모델 weight = **CC BY 4.0**(`data/LICENSE.txt`, README line 128-129 "상업 사용 가능, 배포 시 저작자
  표시 의무"). → registry 기입 = `license:'cc-by-4.0' + commercial:true + attribution_required:true`.
- **Crypko/lambda 는 weight 학습데이터가 아님** — `data/images` **데모 입력 샘플** 라이선스
  (crypko=Crypko Guideline, lambda=CC BY-NC). 프로덕션 입력은 gen_gate(Animagine 등) 출력 → 무관.
- ✅ **attribution 집행 지점 = registry + 출력 응답 + NOTICE 3중 (사용자 결정 2026-06-10)**:
  ① registry/capabilities 단위에 `attribution_required:true`(+author) 노출 →
  ② generate 최종 응답에 `attribution` 필드 동봉(오케스트레이터가 표시 책임 인지, §2.2) →
  ③ repo 루트 NOTICE 파일에 THA3 MIT 고지 + CC BY 4.0 저작자 표시(§4.4). 단일출처는 registry.
- ✅ **합성물 AND-clamp 채택 (사용자 결정 2026-06-10)**: 출력 상업화 = image ∧ audio ∧ weight 3자
  보수 등급 fail-closed(§2.2·§4.3, `voice_lab/server.py:69-73` 선례). 1개라도 비상업이면 commercial 모드 차단.

### D-4. repo 화 시점 [합의 만장일치, DEFER]

현재 `~/motion_lab`은 PoC 스크래치(`poc_headless.py`/`poc_bridge.py`/`talking_clip.mp4`). **즉시
repo화 아님(비례성).** 승격 **트리거 2조건**:
1. `bridge.analyze` 계약 + 포먼트 1단계 수정이 `test_bridge.py`로 GREEN
2. 공유 게이트 모듈 추출(gen_gate 게이트 복제 금지) 완료

충족 시 feature 브랜치(베이스=develop) 승격. THA3 vendor 코드 + weight(797MB Dropbox 출처)는
`.gitignore`/submodule 로 git 미추적 — 다운로드 스크립트 + attribution NOTICE 로 재현.

---

## 4. 컴포넌트 상세 (구현 시)

### 4.1 THA3 렌더러 (②)

- 입력: 512² RGBA 일러스트 + pose track(`List[pose_vector(45)]`).
- 모델: `standard_float`(PoC 검증). 속도 요구 시 `separable_half` 옵션.
- 출력: 프레임열 → ffmpeg mux. GB10 실측 **~30fps(raw GPU 추론) / ~18fps(알파합성 CPU 루프 포함
  실 throughput)**. capabilities `fps` 광고는 실 출력 fps와 일치시켜 over-claim 방지.
- **viseme→45dim 매핑은 렌더러 책임**(브리지는 추상 viseme `{vowel,amount}`만, THA3 인덱스
  `mouth_aaa=26..ooo=30`은 렌더러가 안다) → THA4/후속 교체 시 브리지 무변경 보장(§5).
- 최적화 여지(non-blocking): source 이미지 인코딩 캐싱(동일 입력 반복)·배치 추론으로 throughput 개선.
- **THA3 코드는 vendor 디렉토리로 격리**(우리 코드가 import만, 수정 0) — 업스트림 추적성·MIT 고지 준수.
- ✅ **blink/head idle 모션 구현 완료(2026-06-10)** — '말하는 캐릭터' 살아있음(입만 움직이는 죽은 느낌 방지):
  - **결정적 함수**(§2 결정성 우선·재현/테스트 가능, RNG 0): `idle_pose(frame_index, fps)`.
    - blink = `eye_wink_left/right`(12/13) **해시 지터 스케줄**(평균 3.2s 주기 ± 결정적 지터 → 로봇틱 회피, sin 펄스 0→1→0).
    - head sway = `head_x`(39)·`head_y`(40) 저진폭 sine(±0.05~0.06, 5.0s/7.3s **다른 주기** → 비주기적 흔들림).
    - breathing = `breathing`(44) 느린 sine(0~0.4, 4.0s).
  - **mouth viseme(26-36)과 disjoint** → `compose_pose = build_pose(mouth) + idle_pose` **가산 합성**(덮어쓰기 0).
    무음(입 닫힘)에도 idle 은 살아있음. `render_track(..., idle=True)` 토글(False=mouth-only 결정 경로).
  - 설정 외부화(`DEFAULT_IDLE` — 진폭/주기 단일출처). 실 e2e: 6.5s 클립 blink 3회(간격 2.0s·3.9s 비균일) 시각 확인.

### 4.2 audio→viseme 브리지 (①)

- 입력: WAV. 출력: 추상 viseme track(프레임별 `{vowel, amount}` + 무음 시 닫힘). **45dim 매핑 안 함**(§4.1).
- 인터페이스 고정: `bridge.analyze(wav, fps) -> List[{vowel, amount}]`. 프론트엔드(포먼트/Allosaurus/…)는
  이 계약 뒤로 교체 가능(D-2).
- **무음/엣지 결정적 계약**: PoC `poc_bridge.py:79` 이중정규화 무음 임계는 모호 → 절대 dBFS 임계
  또는 명시 적응형으로 못박기. 테스트: 전구간 무음·0.1s 초단음성·클리핑 입력.
- 무성 폴백 = **'직전 viseme 유지'**(mouth_aaa 강제 금지, 편향 방지). 모음→viseme 매핑 테이블 외부화.
- 한계 명기: 한국어 ㅓ/ㅡ 등 5모음 외 미커버 → capabilities label 에 품질 over-claim 금지.
- **프론트엔드 2개(env `MOTION_BRIDGE_FRONTEND`로 선택, 계약 뒤 교체)**:
  - `formant`(1단계): LPC 포먼트 → `classify_vowel`. 결정적 CPU·경량, but 실측상 F2 order 민감(신뢰 모음 분포 미달).
  - `allosaurus`(2단계, **기본**): `_RECOGNIZER.recognize(wav, timestamp=True)` → `parse_phones` → `map_ipa`(IPA→5모음,
    `IPA_TO_VOWEL` 외부 테이블) → `phones_to_frame_vowels`(timestamp→프레임, 자음/공백=None→직전유지). lazy 모델 캐시.
  - 공유 후처리(`analyze`): `_frame_energy`(RMS) → 절대 dBFS 무음→닫힘 → 직전유지 폴백 → `smooth` → `_amount_from_rms`.
    프론트엔드는 raw 모음만, silence/amount/스무딩은 공유 → 프론트엔드 추가 시 후처리 재구현 0.
  - 미지의 frontend = `ValueError`(조용한 폴백 금지 — 명시적 실패).

### 4.3 오케스트레이션 (③)

- gen_gate(이미지) + voice_lab(음성) → motion_lab(영상) 균일 `discover→generate` 흐름.
- 한 컷 매니페스트: {image_id, audio_id, clip_id} 추적.

### 4.4 Attribution 집행 (CC BY 4.0, D-3 결정)

상업 배포 시 저작자(Pramook Khungurn) 표시 의무를 **3중 지점**에서 충족(단일출처 = registry):

| 지점 | 내용 | 책임 |
|------|------|------|
| ① registry/capabilities | `attribution_required:true` + author 필드 노출 (단일출처) | 게이트(공유 모듈) |
| ② generate 출력 응답 | 최종 `{...}`에 `attribution:"THA3 ... © Pramook Khungurn (CC BY 4.0)"` 동봉 | server |
| ③ repo NOTICE | 루트 NOTICE 파일에 THA3 MIT 코드 고지 + CC BY 4.0 weight 저작자 표시 | repo(D-4 승격 시) |

- 테스트: `attribution_required:true` 단위의 generate 응답에 `attribution` 필드 누락 시 실패(`test_server.py`).
- over-claim 금지: attribution 은 **상업 배포 시 표시 의무 충족 수단**이지 그 자체가 상업화 허가를 주는 게 아님(AND-clamp 우선).

---

## 5. Provider Liquidity / 확장성 (제5조-2 비협상)

| 교체 축 | 코드 변경 0 보장 방법 |
|---------|----------------------|
| 렌더러(THA3 → THA4/후속) | capabilities `units` 추가 + 렌더러 핸들러(계약 `render(image, viseme_track)`). viseme→45dim 매핑이 렌더러 내부라 브리지 무변경 |
| 브리지 프론트엔드(포먼트 → Allosaurus) | `bridge.analyze(wav,fps)->List[{vowel,amount}]` 계약 뒤 교체 |
| 이미지/음성 공급원 | 이미 capabilities discovery로 분리됨 |
| **등급 게이트(공유)** | gen_gate `registry.py`(load_registry/select/assert_allowed)를 **공유 모듈로 재사용**(복제 금지). 라이선스 규칙 단일출처 → motion_lab 도 동일 게이트 답습 |

---

## 6. TDD 계획 (구현 시, 커버리지 ≥70%)

| 테스트 | 대상 | GPU |
|--------|------|-----|
| `test_bridge.py` | 무음→닫힘 · 모음 분류 · 트랙 길이=fps×dur · 계약 형태 · **엣지(전구간 무음·0.1s 초단·클리핑)** · **무성 폴백=직전 viseme 유지** | 0 |
| `test_renderer.py` | viseme track→frame 수 · 45-dim 검증 · **viseme→인덱스 매핑이 렌더러측** (THA3 모킹) | 0 |
| `test_server.py` | `/api/capabilities` envelope(license/attribution 노출) · async `{job_id}`→status · **합성물 AND-clamp**(image∧audio∧weight 중 1개 비상업→차단) · max_duration 게이트 | 0 |
| 실 e2e(수동/마킹) | WAV→mp4 풀루프 1건 라이브 | 1 |

---

## 7. 의존 관계 / 등록

- 본 문서 신규 → `docs/INDEX.md` 등록 · `CLAUDE.md §8 참조 문서` 표 추가 후보.
- `generative-ai-asset-pipeline-design.md`(VIDEO 카테고리) 와 정합 — 모션이 그 VIDEO의 anime 특화 구현.
- 확정(3+1 + 사용자) 후 상태를 "설계 확정"으로 갱신.

---

## 8. 다음 단계

1. ✅ 3+1 합의(REVISE) 반영 완료(`docs/review/3plus1-consensus-2026-06-10-talking-head-motion.md`).
2. ✅ **사용자 BLOCKING 5건 결정 완료(2026-06-10, 전부 합의 권고와 일치)**:
   ① D-3 라이선스 정정 = cc-by-4.0/commercial:true/attribution_required:true ✅
   ② attribution 집행 지점 = registry + 출력 응답 + NOTICE 3중(§4.4) ✅
   ③ 합성물 AND-clamp = image∧audio∧weight fail-closed ✅
   ④ D-1 generate 계약 = async job(POST→job_id) ✅
   ⑤ D-2 우선순위 = 포먼트 자체수정(1단계) 먼저 ✅
3. ✅ **D-4 승격 + TDD 구현 완료(2026-06-10)** — `~/motion_lab` 독립 repo(sibling 패턴):
   - `bridge.py`(analyze 계약 + 포먼트 1단계) 18 · `gate.py`(gen_gate 공유 재사용 + AND-clamp + attribution) 11
   - `renderer.py`(viseme→45dim, 렌더러 책임) 8 · `server.py`(동형 capabilities + async job + AND-clamp 403 + attribution) 10
   - 총 **47 tests green** + 실 GPU e2e(lambda_00 + speech.wav 6.5s → mp4 13.6s 렌더).
4. ✅ **3-서비스 라이브 조합 dogfood(2026-06-10)** — gen_gate+voice_lab+motion_lab 동형 발견 →
   모달리티 라우팅(하드코딩 0) → unit_param 자동 조립 → AND-clamp 라이브 집행(403/job_id) 검증.
5. ✅ **D-2 2단계 Allosaurus 교체 완료(2026-06-10)** — `bridge.analyze` 계약 뒤 phone-level 프론트엔드:
   - 지배 리스크(aarch64 설치) 사망 → IPA→5모음 매핑 → env `MOTION_BRIDGE_FRONTEND`(기본 allosaurus) 선택.
   - ROI 실측: LPC 가 못 낸 **ooo 복구**·5모음 전부·iii 쏠림 해소. **66 tests green**(+19) + 실 e2e mp4.
   - `test_bridge_allosaurus.py` 실 speech.wav e2e = ooo 복구 회귀 가드. `poc_allosaurus.py` 비교 진단(repo 외부).
6. ✅ **blink/head idle 모션 완료(2026-06-10)** — 렌더러 §4.1 확장축:
   - 결정적 `idle_pose(frame_index, fps)`: blink(해시 지터 스케줄)·head sway(다른 주기 sine)·breathing.
   - mouth viseme 과 disjoint → `compose_pose` 가산 합성(`render_track(idle=True)` 토글). **81 tests green**(+15).
   - 실 e2e: blink 3회/6.5s 시각 확인(frame 17 눈감음 vs 30 눈뜸). motion_lab 커밋.
7. **후속(자동 진입 0)**: 실 3-연쇄 생성(이미지→음성→모션 풀 파이프라인) · motion_lab remote ·
   D-2 MFA(2순위, 미착수) · comic_lab ② 말풍선 · VTuber VRM.
