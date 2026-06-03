# TTS 랩 — 외부 관제형 음성 생성 프로젝트 설계 brief (v1)

> 2026-06-02. 외부 관제형 **첫 실사례**(세션 #127 taxonomy). 버추얼 캐릭터 **오리지널 음성
> 생성**(복제 아님). 결정 0건 — 후보 비교 + 권고 + 3+1 회부 항목 정리(SDD 검토 *전* 단계).
>
> 답습: `docs/phase0/tts-lab-voice-generation-research-synthesis.md`(연구+GB10 실측+경로1 PoC) ·
> `docs/phase0/jarvis-plugin-taxonomy-external-view-design-brief.md` v2.1(외부 관제형 §1.5/§3.5/§4) ·
> `docs/review/3plus1-consensus-2026-06-02-jarvis-plugin-external-taxonomy.md`(읽기측 승인) ·
> 사용자 아이디어 문서(버추얼 캐릭터 오리지널 음성 생성 리서치 핸드오프).

---

## 0. 요약 (한 문단)

자비스가 워커로 구축을 돕는 **외부 관제형 첫 실사례** = "음성 생성 랩". 실존 인물 복제가 아닌
**speaker generation**(화자 잠재공간 prior 샘플링)으로 한국어 캐릭터 보이스를 만든다. **별도
프로젝트**(자체 repo/venv/서버/URL)로 살고, 자비스 HUD 엔 **읽기측 링크 카드**(provenance=jarvis,
#128 외부 허브)로만 등록한다(제어측 DEFER). **U-1 = 상업 이용 목표 확정**(사용자: "음성은 상업으로 다른
프로젝트에서 재사용") → **XTTS v2 탈락(비상업 라이선스)**. 백본 = **CosyVoice(Apache-2.0) 등
상업 가능** 으로 확정, GB10 실측 검증 진행. PoC(XTTS)는 메커니즘 증명용일 뿐 산출 백본 아님.
음색 prior = 한국어 화자 임베딩 뱅크에서 샘플링 — **데이터도 상업 안전 출처 필요**(AIHub 542
상업 약관 확인 / 미허용 시 **Zeroth-Korean CC BY 4.0** 대체).

## 1. 배경 — 실측으로 확정된 사실 (research-synthesis 답습)

- ✅ **GB10 호환성 해소**: aarch64+CUDA13(sm_121)+torch 2.12.0+cu130 네이티브 동작. F5-TTS-ko·
  XTTS v2 둘 다 GB10 실합성(발화당 1~2.4초). 연구의 CUDA12 비관은 outdated.
- ✅ **경로1(임베딩 보간) 동작하나 한계**: 2명 보간 = "평균 혼합"(독립 신원 약함, 동질). 권리도
  약함(2 실존 파생).
- ✅ **경로1+(prior 샘플링) 개선**: 58명 분포 PCA-Gaussian 독립 샘플 → 다양성 0.81→0.60, 복사
  아님(최근접 실존 0.40~0.56 ≈ 실존 기준선 0.399). VoxGenesis 경량판. 권리 개선(인구 통계 추출).
- 🔴 **잔여 한계**: prior 가 **영어 화자 분포**(XTTS 내장 58명) → 한국어 네이티브 음색 아님.
  → **한국어 화자 뱅크(AIHub 다화자) 필요.**
- 🔴 **진짜 생성(경로3 VoxGenesis/TacoSpawn)**: 코드·체크포인트 없음 + 영어 전용 → 한국어는
  처음부터 재학습 R&D. **DEFER**(ROI 재평가 후).

## 1.5. 적용 범위 / 비협상 제약

- **외부 관제형 첫 실사례**(taxonomy §1.5): 자비스가 도와 만든 프로젝트 한정. 이 랩은 자비스
  워커가 구축 → provenance=jarvis 정당. **읽기측만**(링크 카드). 제어측(자격증명·제어채널·등급)
  은 #127 BLOCKING X-1~3 미해소 → **범위 밖 DEFER**.
- **Provider Liquidity(헌법 5조-2 비협상)**: 백본(XTTS/CosyVoice/F5)·모델은 **교체 가능한
  수단**이어야 함. 코드가 특정 백본에 하드결합 금지 — seam(추상 인터페이스) 필수.
  [[feedback_provider_liquidity]]
- **개인 툴 비례성**: 자비스 = 개인 자비스([[project_jarvis_local_boss_direction]]). 상업 배포가
  아니면 **비상업 라이선스(XTTS)도 허용 가능** — 상업 자유는 *목표라면* 제약, 아니면 완화.
  → **U-1 사용자 결정 필요.** [[feedback_proportionate_security_personal_tool]]

## 2. 아키텍처 — 외부 관제형 별도 프로젝트

```
┌─ 자비스 HUD (이 repo, jarvis_hud) ──────────────┐
│  external/registry.json  ← 링크 카드(읽기측)     │
│    { name:"voice_lab", title:"🎙️ 음성 생성 랩",  │
│      url:"http://localhost:8770", origin:"jarvis"}│
└───────────────┬─────────────────────────────────┘
                │ 링크(입구만 제공, 읽기 전용)
                ▼
┌─ 음성 생성 랩 (별도 프로젝트, 별도 venv/서버) ────┐
│  voice_lab/  (자체 git repo 권장)                 │
│   ├─ .venv/         ← coqui-tts/torch (트랙A 격리) │
│   ├─ server.py      ← FastAPI, port 8770          │
│   ├─ engine/        ← 백본 seam(XTTS/CosyVoice…)  │
│   ├─ prior/         ← 한국어 화자 뱅크(임베딩 .pt)│
│   └─ web/           ← 음성 생성·캐릭터 UI         │
└──────────────────────────────────────────────────┘
```

**왜 별도 프로젝트인가**:
1. **외부 관제형 정의**(별도 시스템·자체 URL) 충족 — 첫 실사례 진짜 외부형(TTS 가 사실 외부형이란
   #127 진단 해소).
2. **트랙 A 순수성 보존**(#128): coqui-tts·torch·XTTS 의존을 자비스 repo `.venv` 에서 격리. 현재
   PoC 의 일시 설치를 **별도 venv 로 정식 분리**(메인 `.venv` 정리).
3. **Provider Liquidity**: 백본 교체가 자비스 본체와 무관(랩 내부 seam 만 교체).

**위치 후보**(U-2 결정): (a) `~/문서/project/category/voice_lab/`(사이드) (b) 메인 repo 하위
`external_projects/voice_lab/` + .gitignore (c) 완전 별도 repo. **권고 = (c) 별도 repo**(외부형
정의에 가장 충실, dogfooding=자비스 워커가 구축).

## 3. 백본 결정 (수단 후보 비교 — Provider Liquidity seam)

| 백본 | GB10 | 한국어 | prior 샘플링 | 라이선스 | 비고 |
|------|------|--------|-------------|----------|------|
| **XTTS v2** | ✅ 실증 | ✅ ko | ✅ 실증(58명 뱅크) | ❌ **비상업**(Coqui Public Model License) | PoC 검증 완료. 개인용이면 OK |
| **CosyVoice** | ⚠️ 미실측 | ✅ | ⚠️ 임베딩 구조 확인 필요 | ✅ Apache-2.0 | 상업 자유. GB10 실측 필요 |
| **GPT-SoVITS** | ⚠️ 미실측 | ✅ | ⚠️ 클로닝 중심 | ✅ MIT | 복제 함정 주의 |
| **F5-TTS-ko**(현 자산) | ✅ 실증 | ✅ | ❌ ref 클로닝(샘플 불가) | 코드 MIT/ckpt 별도 | 생성 부적합(흉내 전용) |

- ✅ **백본 확정 = GPT-SoVITS v2 (MIT, 상업)** — 2026-06-03 GB10 실측 검증 완료. **작동 레시피 =
  충실 복제(나이 보존, XTTS 평균화 성인편향 회피) + aux_ref 톤 융합(새 목소리 생성) + 정확한 전사
  (또렷함).** 사용자 청취 확인: 젊은+또렷+새목소리 PASS. `~/gpt_sovits` 별도 venv(torch 2.12+cu130).
  CosyVoice2 는 미사용(GPT-SoVITS 로 충분). XTTS = 검증용 throwaway(비상업, 평균화 성인편향).
  ⭐ **실패 교훈**: 참조-전사 정확 매칭 필수(AIHub 아동 발성캐릭터 클립은 전사 "고맙다"≠4.5초 오디오
  불일치 → 발음 깨짐. 깨끗한 문장 참조 필요).
- **BLOCKING B-1**(해소중): 상업 라이선스 = CosyVoice 등으로 확정. 잔여 = **CosyVoice GB10 실측 +
  화자 임베딩 prior 샘플링 가능성**(XTTS 의 58명 뱅크식 구조가 CosyVoice 에 있는지). **B-2**: 백본
  seam 인터페이스(`synthesize(text, lang, speaker_latent)` + `extract_embedding(audio)` +
  `sample_prior(n)`)를 최소 계약으로 고정해 Provider Liquidity 보장(백본 교체 가능).

## 4. 음성 생성 파이프라인 (prior 샘플링 — 한국어 뱅크)

1. **한국어 화자 뱅크 구축**(학습 0): AIHub 다화자(542) 화자별 클립 → XTTS `get_conditioning_latents`
   로 (speaker_embedding 512, gpt_cond_latent 32×1024) 추출 → `prior/ko_bank.pt`(수십~수백 명).
   원본 음성 재배포 0(임베딩만 보관 — 약관 안전).
2. **prior 추정**: speaker_embedding PCA-Gaussian(상관 보존). gpt_cond_latent = Dirichlet 혼합
   (in-distribution 안정). (PoC 2.7 방식 답습, 단 한국어 뱅크로 교체.)
3. **새 화자 샘플링**: seed 별 독립 화자 → 캐릭터별 보이스 N종. **다양성/복사 거리 메트릭**
   자동 산출(상호 코사인 + 최근접 실존)으로 품질 게이트.
4. **합성**: 캐릭터 대사 → wav. 메트릭(시간/RMS) 기록.

**BLOCKING P-1**: prior 가 영어→한국어 전환으로 음색 개선되는지 **실측 검증**(뱅크 구축 후 동일
메트릭 비교 — 한국어 화자 최근접 거리·다양성). **P-2**: 동질성(0.597 잔여) 추가 완화 필요 여부.

## 5. 캐릭터 제어 (Phase 2 — DEFER, 데이터 의존)

- 화자 뱅크(=정체성 "누구") **위에** 감정/말투/애니체("어떻게") 제어를 얹음 — 별개 축, 호환.
- ⚠️ **정직**: XTTS 캐릭터 제어는 제한적(참조 스타일+temperature/speed, 명시 감정 라벨 0).
  진짜 감정·애니체 제어엔 **AIHub 감성·발화스타일(71349)** + 스타일 조건화/파인튜닝 필요.
- **권고**: Phase 1(화자 뱅크 생성) 완성 후 진입. VoiceMe식 human-in-the-loop 속성 슬라이더
  탐색이 캐릭터↔보이스 매칭 UX 참고 모델([[research]] F8).

## 6. MVP 범위 / 단계

| 단계 | 내용 | 상태 |
|------|------|------|
| **0** | GB10 호환성 + 경로1/1+ PoC | ✅ 완료 |
| **1a** | 한국어 화자 뱅크(AIHub 542 임베딩 추출) | 🔴 데이터 대기 |
| **1b** | 별도 프로젝트 골격(venv/서버/seam) + 새 화자 샘플링 + 캐릭터 보이스 N종 wav | 다음 |
| **1c** | 웹 UI(생성·재생·캐릭터 관리) + 자비스 registry 링크 카드 등록(첫 외부 실사례) | 다음 |
| **2** | 캐릭터 감정·말투 제어(AIHub 감성 71349) | DEFER |
| **3** | 진짜 생성 prior 학습(VoxGenesis식 한국어 재학습) | DEFER(R&D) |

## 7. 권리 / 라이선스 (정직 — 법적 미확정)

- prior 샘플링(인구 통계) > 클로닝 = 권리 위치 강함(연구 F3). 단 **법적 결론 미검증**.
- **3중 라이선스 확인 필요**: ① 백본(XTTS 비상업 / CosyVoice Apache) ② AIHub 데이터(약관·상업
  가부) ③ 출력 음성 권리(학습 코퍼스 영향). **상업 목표 시 전부 통과 조합 필요**(CosyVoice +
  Zeroth-Korean). **개인 비상업이면 XTTS+AIHub(약관 내) 허용 가능** → U-1.

## 8. 기존 탑재형 tts_compare 처리

- 현 `jarvis_hud/plugins/tts_compare`(흉내·in-process) = #127 "외부형 오분류". 외부 랩 1c 완성 후
  **은퇴/이관 판단**(즉시 제거 아님 — 회귀 방지, 별도 결정). enabled.json 에서 제외 시점도 U-3.

## 9. 자비스 통합 (읽기측 링크 카드 = 첫 외부 실사례)

- #128 외부 허브(`external/registry.json`)에 entry 추가: `{name, title, url:localhost:8770,
  origin:"jarvis"}`. **rule-of-three 진전**(TTS 가 1번째 진짜 외부 실사례 — 핸드오프 1순위 충족).
- 읽기 전용(입구만). 제어측(자비스가 랩을 직접 제어)은 #127 BLOCKING 미해소 → DEFER.

## 10. BLOCKING / 미해결 (3+1 회부)

- **B-1**(라이선스): XTTS 비상업 vs 목표 — U-1 의존.
- **B-2**(seam): 백본 추상 인터페이스 계약 고정(Provider Liquidity).
- **P-1**(한국어 prior 실측): 영어→한국어 음색 개선 정량 검증.
- **P-2**(동질성): 잔여 0.597 완화 필요 여부.
- **A-1**(위치): 별도 repo vs 사이드 dir(U-2).
- **A-2**(트랙 A): coqui-tts 계열 메인 `.venv` 일시 설치(coqui-tts·torchcodec·unidic-lite·
  coqpit·num2words·pysbd·anyascii) 정리 + 별도 venv 분리.
- **A-3**(시스템 선결): 반복 블로커 = **python3.12-dev(Python.h) 부재** → C확장(pynini[CosyVoice]·
  monotonic-alignment-search[coqui]) 빌드 실패. **`sudo apt install python3.12-dev build-essential`
  1회**가 상업 백본(CosyVoice) 정식 설치 선결. (PoC 는 stub 으로 우회했으나 산출 빌드엔 필요.)

## 2.8. CosyVoice(상업 백본) de-risk 중간 결과 (2026-06-02, 다운로드 대기 중 probe)

- ✅ **GB10 적합 근거**: CosyVoice = torch 기반 → torch 2.12+cu130 GB10 동작 확인됨(§2.5)이므로
  구동 가능성 높음. 화자 임베딩(CAMPPlus spk_emb)을 가져 **prior 샘플링 전이 가능**(아키텍처 기대,
  빌드 후 실측 확정).
- 🔴 **설치는 phase 1b 빌드 작업**: pip `cosyvoice` 0.0.8 = **stub**(실 모델 코드 아님). 진짜는
  git(FunAudioLLM/CosyVoice) + Matcha-TTS 서브모듈 + **pynini(→python3.12-dev 필요)** +
  modelscope 모델 다운로드. 별도 프로젝트 venv 에서 수행이 적절(트랙 A 격리).
- 💡 **대안(C빌드 회피)**: **Supertonic**(ONNX, MIT/OpenRAIL 상업) = pynini·torch C확장 불요,
  aarch64 실증. onnxruntime GPU provider 는 부재이나 CPU(강한 ARM)로 소형 모델 구동 가능.
  단 화자 임베딩 샘플링 가능성은 CosyVoice 보다 불확실(프리셋+voice builder). **백본 후보 2순위.**

## 11. 사용자 결정 회부 (U)

- ~~**U-1**~~ ✅ **결정됨 = 상업 이용 목표**(음성을 다른 프로젝트에서 상업 재사용). → 백본
  CosyVoice(Apache) 등 상업 가능만, XTTS 제외. 데이터도 상업 안전 출처(AIHub 542 약관 확인 /
  Zeroth-Korean 대체). **신규 U-5: AIHub 542 상업 약관 가부 확인 결과 → 미허용 시 Zeroth-Korean.**
- **U-2**: 프로젝트 위치(별도 repo 권고 / 사이드 dir / 메인 하위 gitignore).
- **U-3**: 기존 탑재형 tts_compare 은퇴 시점.
- **U-4**: 캐릭터 제어(Phase 2) 우선순위 — 화자 뱅크 직후 vs 더 뒤.

## 12. 합의 형태 권고

- 아키텍처 결정(외부 별도 프로젝트·백본 seam·라이선스) = **3+1 합의 권고**(CLAUDE.md §3
  아키텍처 의사결정 필수). 단 읽기측 링크 등록 자체는 #128 합의로 이미 승인(풀3+1 불요).
- **순서**: 이 brief 사용자 검토 → U-1~4 결정 → 3+1 합의(B/P/A 항목) → 1b TDD 구현.
