# TTS 랩 — 오리지널 캐릭터 음성 "생성" 기술 검증 리서치 종합

> 2026-06-02. 외부 관제형 첫 실사례(TTS 랩) 설계 *직전* feedforward.
> 출처: deep-research 워크플로우(GB10·3갈래·경로1·VoxGenesis·라이선스, 25 claim 중 21 confirmed)
> + 한국어 특화 병렬 조사. 설계 brief 의 근거 자료(결정 0건 — 검증된 사실 + 미해결 항목 정리).

## 0. 한 줄 결론

**복제 아닌 speaker generation 은 학술적으로 정립된 타당한 접근(확증).** 단 ① 진짜 화자
생성(VoxGenesis/TacoSpawn)은 **공개 코드·체크포인트 부재 + 영어 전용**이라 한국어는 처음부터
재학습 R&D, ② 가장 빠른 경로 1(임베딩 샘플/보간)은 **작동하나 "독립 신원"이 아님**(두 실존
화자 혼합·동질성 한계), ③ **최우선 리스크였던 GB10 호환성은 웹 리서치로 미해결** — 실 하드웨어
실측이 유일한 답. 한국어 조사에서 **Supertonic(ONNX·aarch64 실증)** 이 GB10 우회 유력 후보로 부상.

## 1. 확증된 사실 (high confidence, 3-0 검증)

| # | 사실 | 함의 |
|---|------|------|
| F1 | speaker generation(잠재공간 새 좌표 샘플링)은 "세상에 없는 인간형 음성" 합성의 정립된 과제 (TacoSpawn/VoxGenesis/VoiceMe) | 경로 C 방향 자체는 옳음 |
| F2 | TacoSpawn = 화자 임베딩 공간 위 **GMM** 학습→샘플링. 평균/보간 collapse 아님, transfer learning 불요. **단 영어(1468 화자) 전용** | 한국어 재학습 필요 |
| F3 | VoxGenesis = **비지도** Gaussian manifold. 학습 화자 유사도가 TacoSpawn보다 낮음 = **복제 의존 적음(권리 안전성↑)** | 가장 "생성"다움. 단 ↓ |
| F4 | VoxGenesis = **공개 GitHub 코드·체크포인트 없음**(데모 페이지만) + **영어 LibriTTS-R 16kHz 전용** | 로컬 즉시 재현 불가. 한국어 = 처음부터 재구현+재학습 |
| F5 | 경로 1(multi-speaker 임베딩 random/보간)은 **원리적으로 새 인공 음성 생성 가능**(NVIDIA Casanova + Jia 2018) | 가장 빠른 실증 OK |
| F6 | **그러나** 보간 화자 = 두 실존 화자 "balanced blend"(α=0.5), recognition 임베딩 특성상 합성 화자 발화 간 유사도 비정상 높음 = **동질적(homogeneous), 진짜 독립 신원 아님** | 경로 1 = MVP 체감용, 품질·독립성 한계 명확 |
| F7 | 경로 B(YourTTS 등 <1분 파인튜닝) = 타깃 실존 화자 복제 SOTA = **복제 함정. 회피 대상** | B 비채택 근거 |
| F8 | VoiceMe = human-in-the-loop(Gibbs Sampling with People)로 잠재 화자공간 탐색, 타깃 미지(복제 아님) | **캐릭터 보이스 선택 UX 참고 모델** |

medium(2-1): PCA로 임베딩 속성(gender) 분리 후 경계 샘플링 = 단순 보간보다 구별되는 음성(경로 1 개선 변형).

## 2. 한국어 특화 발견 (병렬 조사)

- ⭐ **한국어 전용 speaker generation 연구·repo = 부재(갭)**. 핵심 기법 전부 영어. → 한국어는
  "다화자 한국어 백본 + 임베딩 공간 샘플/보간" 직접 구성이 현실적.
- ⭐ **Supertonic** (supertone-inc, 코드 MIT/모델 OpenRAIL-M 상업가능): **ONNX + aarch64/RPi/Jetson
  실증**. GB10 호환성 미해결 문제의 **유력 우회로**(ONNX runtime = PyTorch CUDA 휠 문제 회피).
  flow-matching(F5 친화). ko 포함 31언어.
- **CosyVoice**(Apache-2.0)·**GPT-SoVITS**(MIT) = 한국어 다화자 임베딩 토대.
- **F5-TTS Korean (DavidVita, jamo 변형)** = 사용자 기존 F5-TTS-ko 자산과 가장 근접 공개물.
- **g2pK**(Apache-2.0) = 한국어 G2P 전처리 1순위. **Vo-Ve**(SNU, 코드 공개) = 화자 속성("cute"
  등) 해석·제어 = 캐릭터성 제어 한국발 토대.
- **데이터(캐릭터성)**: AIHub 감성·발화스타일(애니체, dataSetSn=71349) + 다화자(542). 단
  **상업 이용은 AIHub 약관 개별 확인 필수**. 상업 자유 필요 시 **Zeroth-Korean(CC BY 4.0)** 한정.

## 2.5. ✅ GB10 실측 결과 (2026-06-02, 실 하드웨어 probe) — 최우선 리스크 해소

> 연구가 못 푼 GB10 호환성을 **실 GB10에서 직접 실측** — PyTorch 경로 호환성 **확정 해소**.

- ✅ **환경**: aarch64 · CUDA 13.0 driver(580.159.03) + nvcc 13.0 · Python 3.12 ·
  **compute capability = sm_121**(연구가 0-3 기각한 "sm_121" 주장이 실은 정확 — 검증자 오판).
- ✅ **PyTorch CUDA 네이티브 동작**: `.venv` 에 **torch 2.12.0+cu130 · torchaudio 2.11.0+cu130**
  이미 설치, `cuda.is_available()=True`, **2048² matmul 실연산 성공**(GPU). 연구의 비관
  (CUDA12 휠 실패·휠 부재)은 **outdated** — cu130 aarch64 휠 존재·동작.
- ✅ **기존 한국어 자산 F5-TTS-ko 합성 실동작**: model load 2.3s + **8.58초 오디오를 2.4s 합성**
  (RTF~0.28), 24kHz 정상. 의존(numpy/soundfile/f5_tts/librosa/transformers/vocos) 전부 OK.
  → **우리 한국어 TTS 자산이 GB10에서 바로 돈다**(0단계 선결 충족).
- ⚠️ **ONNX runtime GPU provider 부재**(CPU/Azure만, CUDAExecutionProvider 없음). Supertonic
  ONNX-GPU 는 별도 빌드 필요. **단 PyTorch CUDA 가 네이티브로 도니 ONNX 우회 불필요해짐** —
  Supertonic 의 "GB10 우회로" 가치 하락(여전히 후보지만 우선순위↓).

**잔여 미지(repo별)**: F5-TTS 는 이색 커스텀 CUDA 커널 없어 무탈. **VITS 계열(monotonic_align
cython/cuda)·flash-attn 의존 모델은 sm_121 재컴파일 이슈 가능** — 미실측, 채택 시 repo별 확인.

## 2.6. ✅ 경로 1 PoC 실측 (2026-06-02, GB10 실 합성) — 메커니즘 확증 + 연구 한계 재현

> 사용자 요청: "경로 1이 GB10에서 새 목소리 내는지 먼저 PoC". XTTS v2(다국어, **한국어 ko
> 지원**, espeak 불요)로 **기존 hana×kss 한국어 참조의 화자 임베딩을 보간/랜덤 샘플** → 새
> 목소리 생성 → 생성 음성에서 화자 임베딩 재추출 → 신원 거리 정량.

- ✅ **GB10 동작**: XTTS v2 cuda 로드 + 한국어 합성 **발화당 ~1.3초**(실시간). coqui-tts 0.27.5
  설치 우회 성공(`monotonic_alignment_search` = 추론 미사용이라 stub, MAS C빌드/python3-dev 불요;
  fugashi→unidic-lite, torchcodec 추가). **VCTK VITS 는 espeak-ng(sudo) 필요해 회피, XTTS 채택.**
- ✅ **새 목소리 생성됨(복사 아님)**: 보간(MID)·랜덤(RAND) 화자가 두 실존 화자 어느 쪽과도
  코사인 ≠1.0. MID↔A=0.733 / MID↔B=0.710(거의 등거리) / RAND↔A=0.736 / RAND↔B=0.672.
- ⚠️ **연구 한계 F6 그대로 재현(중요)**: 실존 A↔B=**0.495**인데 MID 는 A·B 각각에 **0.71~0.73**
  = 두 실존 화자보다 *더 가까운* 중앙 혼합("balanced blend"). 합성끼리 MID↔RAND=**0.814** =
  동질적 클러스터(독립·다양성 낮음). 즉 **"세상에 없는 대담한 새 신원"이 아니라 두 참조의
  평균 지대 목소리** — 경로 1 의 알려진 한계(§1 F6) 실측 확인.
- 🔴 **권리 정직 단서**: 이 PoC 는 **두 실존 화자(hana·kss) 참조에서 파생된 보간** — "학습된
  prior 순수 샘플링"(TacoSpawn/VoxGenesis, §1 F3)이 아님. 따라서 "실존 인물과 무관한 권리
  자유"는 이 경로로는 약함(두 실존 화자 혼합). 강한 권리 안전성엔 prior 샘플링(경로 3) 필요.
- 정직: 음성 *자연성·한국어 발음·체감 구별성*은 **사용자 육안(육이) 청취 미확인**(파일만 생성).
  XTTS 라이선스 = **Coqui Public Model License(비상업)** — 상업 목표 시 백본 교체 필요.
- 산출(되돌림 대상): `/tmp/poc_{A_hana,B_kss,MID_interp,RAND_sample}.wav`. `.venv` 에 coqui-tts
  계열 일시 설치(트랙 A 순수성 — PoC 후 정리 판단). evidence 스크립트 인라인.

## 2.7. ✅ 경로 1+ PoC (prior 샘플링, 2026-06-02) — 동질성 한계 완화 실증

> 사용자 "더 넓은/독립 샘플링 시도". 2명 보간 대신 **XTTS v2 내장 58명 화자 임베딩으로
> 화자 분포(prior) 추정 → PCA-Gaussian 독립 샘플링** = VoxGenesis식 prior 샘플링 경량판.

- ✅ **다양성 개선**: 새 화자 4명 평균 상호 코사인 **0.597** (2명 보간 MID↔RAND **0.814** 대비
  크게↓). 동질 클러스터 탈출.
- ✅ **복사 아님(새 신원)**: 각 새 화자의 최근접 실존(58명) 코사인 0.40~0.56, **실존 58명 상호
  평균 기준선 0.399** 와 유사 위치 = 인구 분포에서 추출한 진짜 새 신원(어떤 실존도 복사 안 함).
- ✅ **권리 개선**: 특정 1인(hana/kss) 파생이 아니라 **화자 *인구 통계*에서 샘플링** → §2.6
  보다 권리 위치 강함.
- 🔴 **핵심 한계(사용자 질문 답)**: prior 가 **XTTS 의 58명 *영어* 화자 분포**임. 한국어 음색
  분포 아님 → 영어 화자 통계로 한국어 합성. **한국어 네이티브 음색엔 한국어 다화자 임베딩 뱅크
  (AIHub 다화자 dataSetSn=542 등) 필요.** 잔여 동질성(0.597 > 실존 0.399)도 남음.
- 정직: 자연성·한국어 발음·체감 구별성 육안 청취 미확인. XTTS 비상업 라이선스 유지.
- 산출(되돌림): `/tmp/poc2_voice0..3.wav`.

### AIHub 데이터 필요 시점 (사용자 질문 — **현재까지 미사용**)
지금까지 전부 로컬 기존 자산(hana/kss·F5-TTS-ko) + XTTS(내장 영어 58명)만. AIHub 미다운로드.
필요해지는 시점: (1) **한국어 네이티브 화자 분포**(다화자 542 → 한국어 임베딩 뱅크), (2) **캐릭터
감정·말투/애니체 제어**(감성·발화스타일 71349), (3) **경로 3 한국어 생성 prior 학습 코퍼스**.
모두 약관 동의 + 상업 이용 별도 확인 필요.

## 2.9. ✅ 한국어 화자 뱅크 검증 (2026-06-03, AIHub 015 + XTTS) — P-1 부분 답

> AIHub 015 다운로드 완료(220GB, 5 zip). 라벨 manifest(50명·7감정·5스타일·3캐릭터) +
> **XTTS 검증 패스**(비상업, 메커니즘·데이터 검증용 — 생산은 CosyVoice). 50명 × 5발화 평균
> centroid → PCA-Gaussian 독립 샘플.

- ✅ **GB10 추출 초고속**: 50명 화자 centroid 추출 **7초**(다중참조 평균). 뱅크 `/tmp/ko_bank_xtts.pt`.
- ✅ **한국어 새 화자 생성**: 4명 샘플, 최근접 실존 0.58~0.66(복사 아님, 기준선 0.451 초과).
- ⚠️ **다양성 영어보다 약간 낮음**: 한국어 샘플 상호 0.662 vs 영어 0.597. 원인 = **AIHub 50명이
  인구학적으로 좁음**(대부분 30~40대·동일 스튜디오 → 실존 상호 0.451 > 영어 0.399 = 더 동질).
  prior 가 tight → 샘플 다양성 제한. 완화책 = 더 넓은 화자 소스·연령 가중·perturbation↑.
- 🎧 **P-1 핵심(한국어 네이티브 음색)은 청취 미확정**: 코사인은 화자 구별성이지 "한국어다움"
  아님. 임베딩이 한국어 화자 유래라 영어 파생보다 네이티브일 것이나 **육이 청취 필요**(미수행).
- 정직: XTTS(비상업) 검증 — 생산 뱅크는 CosyVoice 재구축(임베딩 차원 다름, python3.12-dev 선결).
  화자 centroid = 감정 평균(순수 중립 아님 — 감정색 상쇄 가정). 산출 `/tmp/ko_voice0..3.wav`.

## 3. ⚠️ 미해결 / 약한 근거 (정직 단서)

- 🟢 ~~GB10 호환성~~ → **§2.5 실측으로 PyTorch 경로 해소**. 잔여 = VITS/flash-attn 계열 repo별
  커널 재컴파일 미실측 + ONNX-GPU provider 부재(필요 시 빌드).
- GPT-SoVITS 자체 생존 claim 0건 + F5-TTS claim 0건 — 경로 B/현 자산은 직접 검증 안 됨.
- **권리/라이선스 = 기술 정황만, 법적 결론 미검증.** "생성 음성이 초상권/저작권 자유"는 정황
  (VoxGenesis 낮은 memorization·보간=혼합)일 뿐 법적 확정 아님. 학습 코퍼스 라이선스가 출력
  상업 이용에 미치는 영향 별도 확인 필요.
- 상용 API 경로 A(ElevenLabs/Fish) = "로컬 아님" 전제로 분석 제외(내부적으론 C의 제품화).

## 4. 미해결 핵심 질문 (설계/실측 대상)

1. **GB10에서 PyTorch CUDA 실동작 최신 경로?** NGC ARM64 컨테이너 + 커널 재컴파일로 VITS/
   YourTTS/F5-TTS 추론·파인튜닝 가능한가. ONNX(Supertonic) 우회가 더 빠른가.
2. **한국어 자산을 multi-speaker 로 확장 가능한가?** 현 F5-TTS-ko 가 화자 조건화 구조를 갖는지,
   아니면 prior 학습을 한국어 코퍼스로 처음부터 해야 하는지.
3. **권리 안전성 법적 확정 가능?** "보간" vs "prior 순수 샘플링"의 권리 차이, 코퍼스 라이선스 영향.
4. **경로 1 동질성 한계를 GST/prosody·sub-center 로 실용 수준 완화 가능한가, 아니면 prior 학습
   투자가 더 빠른가?**

## 5. 권장 단계 경로 (난이도순, 함정 포함)

> ✅ 0단계는 §2.5 실측으로 **완료** — PyTorch+CUDA+F5-TTS-ko 가 GB10에서 돈다. 경로 선택 가능.

- ~~**0단계 (선결·실측)**~~ ✅ **완료(§2.5)**: torch 2.12.0+cu130 동작 + F5-TTS-ko 실합성 PASS.
  ONNX-GPU 는 미설치이나 PyTorch 네이티브 동작으로 불필요. → **PyTorch 기반 경로로 진행 가능.**
- **1단계 (빠른 체감)**: 도는 한국어 다화자 백본(우선순위 Supertonic→CosyVoice→GPT-SoVITS)에서
  **화자 임베딩 샘플/보간 → 캐릭터 보이스 N종 wav 출력** 최소 예제. **함정**: 동질성·비독립
  신원(F6) — "체감용"으로 한정, 품질 기대치 관리.
- **2단계 (캐릭터성 제어)**: g2pK 전처리 통일 + 속성 슬라이더(VoiceMe/Vo-Ve식 human-in-the-loop)로
  캐릭터↔보이스 매칭. **함정**: 속성 분리 품질, 한국어 Vo-Ve 재학습 부담.
- **3단계 (진짜 생성, R&D)**: VoxGenesis식 Gaussian manifold 를 한국어 다화자 코퍼스로 재학습.
  **함정**: 코드 부재 = 재구현, 데이터·학습 인프라, 가장 큼. ROI 재평가 후 진입.

## 6. 라이선스 안전 조합 (상업 자유 필요 시)

코드: Supertonic(MIT/OpenRAIL-M) · CosyVoice(Apache-2.0) · GPT-SoVITS(MIT) · g2pK(Apache-2.0).
데이터: **Zeroth-Korean(CC BY 4.0)**. ⛔ 회피(상업 불가): KSS(CC BY-NC-SA) · MMS-TTS-kor(CC-BY-NC) ·
AIHub(약관 개별 확인). 단 **법적 확정은 별도**(§3).
