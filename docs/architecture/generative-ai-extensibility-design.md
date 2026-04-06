# 생성 AI 확장성 설계 (Generative AI Extensibility Design)

> **모델 교체/학습/확장이 용이한 Guide-First 구조 — 외부 SDK 활용 + config 기반 전환 + 학습 안내 가이드**

**최종 수정**: 2026-04-06
**상태**: 설계 확정 (3+1 합의 검증 완료)
**상위 문서**: `generative-ai-asset-pipeline-design.md` (ADR-003)
**관련 ADR**: ADR-004 (생성 AI 확장성)

---

## 1. 핵심 원칙 (3+1 합의 결과)

| 원칙 | 설명 | 근거 |
|------|------|------|
| **자체 어댑터 불필요** | Replicate/HuggingFace SDK가 이미 모델 추상화를 제공. 자체 코드 계층 없음 | Agent C + Reviewer — Guide-First 원칙 정합 |
| **Config-Driven** | 모델 교체 = config 파일 1줄 변경. 코드 변경 없음 | Agent A/C 합의 |
| **학습은 안내** | 파인튜닝이 필요할 때 방법/서비스를 안내. 자체 인프라 없음 | Guide-First 일관 적용 |
| **MVP = Level 0** | API 호출 안내만. Level 1(LoRA) 이상은 필요 입증 후 추가 | 최소 범위 원칙 |
| **데이터 거버넌스** | 학습 데이터의 출처/라이선스/동의 체크리스트 필수 | Agent B — 안전성 |

---

## 2. 모델 교체: Config 기반 전환

### 2.1 단일 설정 파일

모든 생성 AI 모델 정보를 **1개 파일**에서 관리한다.

```yaml
# generative-models.yaml (단일 진실 원천)

defaults:
  image: stable-diffusion-xl
  audio: suno-v4
  video: runway-gen3
  threed: meshy-v2

models:
  stable-diffusion-xl:
    provider: replicate              # 어디서 실행하는가
    model_id: stability-ai/sdxl      # provider 내 모델 식별자
    api_key_env: REPLICATE_API_TOKEN # API 키 환경변수명
    license: open-rail              # 라이선스
    cost: ~$0.01/image              # 대략적 비용
    status: active                  # active | deprecated | removed

  suno-v4:
    provider: suno
    model_id: suno/v4
    api_key_env: SUNO_API_KEY
    license: commercial-pro
    cost: $10/month subscription
    status: active

  # 새 모델 추가 = 여기에 항목 1개 추가. 끝.
```

### 2.2 모델 교체 절차

```
새 모델 "AuraFlow" 출시 시:

Step 1: generative-models.yaml에 항목 추가
  auraflow:
    provider: replicate
    model_id: auraflow/v1
    api_key_env: REPLICATE_API_TOKEN
    ...

Step 2: defaults.image를 auraflow로 변경 (선택)

Step 3: 끝. 코드 변경 없음.

LLM이 안내할 때 이 config을 참조하여 최적 모델을 추천한다.
```

### 2.3 폴백 체인

```yaml
# generative-models.yaml에 추가
fallback:
  image: [stable-diffusion-xl, dall-e-3, flux-schnell]
  audio: [suno-v4, audiocraft, elevenlabs]
```

기본 모델이 불가용(API 중단 등)이면 다음 모델을 자동으로 안내한다.

### 2.4 Deprecation

```yaml
  old-model:
    ...
    status: deprecated    # 사용 시 경고 표시
    successor: new-model  # 대체 모델 안내
```

---

## 3. AI 학습: 레벨별 안내 가이드

### 3.1 학습 레벨 의사결정 트리

```
에셋 생성 시도 (기존 모델 + 프롬프트)
    │
    ├── 만족 → 완료 (Level 0)
    │
    └── 2회 반복 후에도 불만족
        │
        ▼
    "프롬프트 한계인가, 모델 한계인가?"
        │
        ├── 프롬프트 한계
        │   → 프롬프트 최적화 안내 (여전히 Level 0)
        │
        └── 모델 한계
            │
            ▼
        "어떤 종류의 커스터마이징이 필요한가?"
            │
            ├── 스타일/캐릭터 일관성
            │   → Level 1: LoRA 파인튜닝 안내
            │
            ├── 도메인 특화 (의료, 법률 등)
            │   → Level 2: 본격 파인튜닝 안내
            │
            └── 완전히 새로운 능력
                → Level 3: 커스텀 학습 안내 (외부 전문가 권장)
```

### 3.2 레벨별 안내 내용

| Level | 방법 | LLM이 안내하는 것 | 실행 주체 |
|-------|------|------------------|----------|
| **0** | 프롬프트 최적화 | 프롬프트 개선 기법, 파라미터 조정 | LLM + 사용자 |
| **1** | LoRA/경량 파인튜닝 | 클라우드 서비스 사용법 (Replicate Training, HF AutoTrain), 필요 데이터, 예상 비용/시간 | 사용자 (클라우드) |
| **2** | 본격 파인튜닝 | 학습 플랫폼 안내 (Colab, Modal, RunPod), 학습 코드/노트북 생성, 하이퍼파라미터 | 사용자 (GPU 필요) |
| **3** | 커스텀 학습 | 외부 전문가/팀 연결 권장, 논문/리소스 안내 | 외부 전문가 |

### 3.3 Level 1 안내 예시 (Guide-First)

```
사용자: "모든 아이콘이 동일한 브랜드 스타일이어야 해"

LLM 안내:
  "브랜드 스타일 일관성을 위해 LoRA 파인튜닝을 추천합니다.

  [방법] Replicate Training API 사용
  1. 브랜드 스타일 참조 이미지 10~30장 준비
  2. Replicate에서 SDXL LoRA 학습 실행:
     replicate.trainings.create(
       model="stability-ai/sdxl",
       input={"input_images": "your_images.zip", ...}
     )
  3. 학습 완료 (약 15분, ~$1)
  4. 학습된 LoRA로 생성:
     replicate.run("your-username/your-lora", input={...})

  [비용] ~$1 (1회 학습)
  [시간] ~15분
  [필요] Replicate 계정 + 참조 이미지 10장+

  ⚠️ 데이터 거버넌스 체크:
  □ 참조 이미지의 저작권이 본인에게 있습니까?
  □ 타인의 작품을 사용하는 경우 허가를 받았습니까?"
```

---

## 4. 데이터 거버넌스 체크리스트

학습 데이터를 사용할 때 **반드시 확인**해야 하는 항목.

### 4.1 학습 데이터 체크리스트

```
⚠️ AI 학습 데이터 거버넌스 체크리스트

[필수]
□ 데이터 출처가 명확한가?
□ 데이터의 저작권/라이선스가 학습을 허용하는가?
□ 타인의 저작물인 경우 사용 동의를 받았는가?
□ 개인 정보(얼굴, 음성 등)가 포함된 경우 동의가 있는가?

[권장]
□ 데이터 출처를 기록했는가? (재현성)
□ 학습 데이터에 부적절/유해 콘텐츠가 없는가?
□ 학습 결과물의 상업적 사용이 가능한가?
```

### 4.2 학습 모델 안전성 체크

```
⚠️ 파인튜닝 모델 안전성 체크

[필수]
□ 학습 후 모델이 부적절 콘텐츠를 생성하지 않는가? (샘플 테스트)
□ 기반 모델의 안전장치가 유지되는가?
□ 학습 모델의 출력에 저작권 문제가 없는가?

[권장]
□ 기반 모델 버전을 기록했는가? (호환성 추적)
□ 학습 설정(하이퍼파라미터)을 기록했는가? (재현성)
```

---

## 5. 대용량 파일 관리

### 5.1 Git LFS 설정

학습 모델/데이터셋은 대용량이므로 Git LFS를 사용한다.

```bash
# .gitattributes
*.safetensors filter=lfs diff=lfs merge=lfs -text
*.ckpt filter=lfs diff=lfs merge=lfs -text
*.pt filter=lfs diff=lfs merge=lfs -text
*.bin filter=lfs diff=lfs merge=lfs -text
training/datasets/** filter=lfs diff=lfs merge=lfs -text
```

### 5.2 대안: 외부 스토리지

대용량 파일을 Git에 넣지 않고 외부에 관리하는 방법:

| 방법 | 적합 | 안내 |
|------|------|------|
| HuggingFace Hub | 모델 공유/버전 관리 | `huggingface-cli upload` |
| 클라우드 스토리지 (S3 등) | 대규모 데이터셋 | 경로만 config에 기록 |
| DVC (Data Version Control) | 데이터+모델 버전 관리 | Git과 병행 사용 |

---

## 6. 생태계 변화 대응

### 6.1 변화 감지

```
수동 (현재):
  사용자: "최신 이미지 생성 모델 확인해줘"
  → 탐색 에이전트가 웹 검색 → generative-models.yaml 업데이트 제안

자동 (Phase 2+):
  주기적 탐색 에이전트 → 모델 변경 감지 → 사용자 알림
```

### 6.2 마이그레이션

```
모델 A → 모델 B 전환:
  ① generative-models.yaml에 B 추가
  ② defaults를 B로 변경
  ③ A를 deprecated 처리
  ④ 기존 LoRA가 있으면 호환성 확인 (비호환 시 재학습 안내)
  → 코드 변경 없음
```

---

## 7. Phase 로드맵

| Phase | 내용 | 상태 |
|-------|------|------|
| **MVP** | Level 0 (API 호출 안내) + generative-models.yaml + Git LFS | 구현 대상 |
| **v1.1** | Level 1 (LoRA 안내) + 데이터 거버넌스 체크리스트 | 필요 입증 후 |
| **v1.2** | Level 2 (파인튜닝 안내) + 자동 모델 탐색 | 필요 입증 후 |
| **v2.0** | 자체 어댑터 계층 (현재 제거된 설계) | 외부 SDK 부족 입증 후에만 |

> Level 1 진입 조건: Level 0에서 "모델 한계" 판정이 3회 이상 반복될 때

---

## 8. 3+1 합의 검증 결과 요약

### 핵심 설계 변경

| 변경 항목 | 초안 | 최종 | 근거 |
|-----------|------|------|------|
| 어댑터 계층 | 자체 Python 인터페이스 + 어댑터 파일 | **제거** — 외부 SDK(Replicate/HF) 활용 | Guide-First 원칙 위반 |
| 설정 파일 | registry.yaml + project-config.yaml (2중) | **generative-models.yaml 단일** | 설정 단일화 |
| 학습 인프라 | training/ 디렉토리 + registry.json | **제거** — 클라우드 서비스 안내 | 자체 인프라 불필요 |
| MVP 범위 | Level 0~3 전체 | **Level 0만** | 최소 범위 원칙 |
| 데이터 거버넌스 | 없음 | **체크리스트 추가** | Agent B 안전성 |
| 문서 규모 | ~800줄 | **~250줄** (70% 감축) | Agent C 간결화 |

---

**이 문서는 3+1 에이전트 합의를 거쳐 설계가 확정되었습니다.**
