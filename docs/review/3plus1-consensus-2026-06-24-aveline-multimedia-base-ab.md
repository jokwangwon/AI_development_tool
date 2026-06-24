# 3+1 합의 보고서 — 아벨린 멀티미디어화 + 베이스 모델 A/B 준비

> **일자**: 2026-06-24
> **주제**: 오리지널 상업 캐릭터 **아벨린**(흑익의 악마 공녀)을 만화·영상·버튜버로 발전시키고, "현 animagine vs 새 베이스" 두 케이스를 A/B 비교 가능하게 **준비**(실 재학습/적용이 아닌 비교 구조 셋업)
> **프로토콜**: CLAUDE.md §3 3+1 (Agent A 구현·B 품질/안전·C 대안 → orchestrator Reviewer)
> **상태**: 합의 완료 → 사용자 확정 완료 → 구현 진행

---

## 0. 사용자 확정 사항

- **비교 축 = 둘 다 준비**: 축1(베이스 raw 화풍/품질 시트, LoRA 무관) + 축2(아벨린 결과물 체인 시트)
- **진행 순서 = 합의 권고안대로**: ① 0코드 e2e 3트랙 실증 → ② 베이스 A/B 준비 → ③ ②말풍선 렌더러

---

## 1. 정찰 확정 사실 (3 Agent 코드 1:1 대조)

- **아벨린 LoRA**: `~/lora_lab/out_aveline/pytorch_lora_weights.safetensors`, 트리거 `aveline`, **animagine-xl-4.0 전용**. gen_gate `lora_registry.json` 등록(`gate.generate(..., lora="aveline")`). v1 운용 가능(트리거+디자인 태그 병용), 트리거 단독은 색바인딩 약함. 바이블 `~/lora_lab/CHARACTER_BIBLE_AVELINE.md`. 의상 가변(outfit_adapter+library 358벌) 완성.
- **comic_lab**: 텍스트(줄거리·페르소나·대사·연출)+이미지 파이프 완성. `render_panels`가 `**opts`로 `lora=` 게이트 전달(image_generator.py:207). 61 tests. **갭 = make_comic.py CLI에 `--lora` 미노출 + ②말풍선 렌더러 0줄**. master 브랜치.
- **motion_lab**: 이미지+음성→말하는 mp4 e2e 완성(THA3 + audio→viseme + align.py 자동정렬). 2D 버튜버(idle·립싱크·표정) 완성. 임의 PNG→512² RGBA 자동 정규화(renderer.py:252-279). AND-clamp 게이트(gate.py:35-52). 49 tests. **갭 = 아벨린 e2e 미실행(데이터, ~40s)**.
- **gen_gate**: `generate_chain()` img2img 체인 구현됨(gate.py:203-282). `compare_basemodels.py`(native 격리 비교)·`compare_multiseed.py` 존재. LoRA 적용은 **`diffusers-sdxl` 백엔드에만**(`_apply_lora`, diffusers_sdxl.py:49) — anima/qwen 백엔드 LoRA 0줄.

---

## 2. 교차 비교 (Reviewer)

### ① 일치 (만장일치)

1. **인프라 사실상 완성** — 코드 갭은 comic_lab `--lora` 노출(~5줄) + ②말풍선(별개 갭)뿐. 나머지는 데이터/실행.
2. **베이스 A/B 재현 수단 = img2img 체인(`generate_chain`)** — 이미 구현됨. **재학습은 "준비만"에 정면 위배** → 범위 밖.
3. **최소 구현 = 기존 `compare_*.py` 복제 + registry 엔트리. 코어 무변경.** 전용 하네스 = 오버엔지니어링.

### ② 핵심 통찰 (B·C 독립 수렴)

**비교 축이 작업 전체를 가른다.**

| 축 | 비교 대상 | 셋업 | 아벨린 정체성 |
|----|----------|------|--------------|
| 축1 — 베이스 화풍/품질 | "어느 모델 그림체가 좋은가" | LoRA 없이 동일 프롬프트 raw | 없음(캐릭터 무관) |
| 축2 — 아벨린 결과물 | "아벨린을 만들면 베이스별로 다른가" | 체인(새 베이스 구조→animagine+LoRA) | LoRA 보장. **단 최종 화풍은 항상 animagine, 새 베이스는 구조/해부학만 기여** |

### ③ 불일치 → 해소

- **Z-Image**: C "1순위 비교 대상" ↔ A "코드베이스 0건·신규 백엔드 필요"(실증) ↔ B "Z-Anime 라이선스 미확인". → **이번 준비에서 제외**(평가 메모만). 대신 **Qwen-Image(체인 1단계 검증됨) + illustrious-xl-2.0(SDXL·상업)** 사용.
- **우선순위(말풍선 위치)**: A 후순위(별개 갭) ↔ C 1순위(만화 완성). → **0코드 즉시 e2e 최우선, 말풍선은 그 다음**.

### ④ 누락 (단독 발견 — 중요)

- **A 단독 — 백엔드 LoRA 제약(코드 실증)**: anima/qwen 백엔드 LoRA 0줄. 신규 베이스 단독에 aveline LoRA를 얹으면 dead opt로 조용히 무시되거나 `LoraError` 차단(gate.py:96-99) → **축2는 반드시 체인으로만**.
- **B 단독 — 🔴 R1 (BLOCKING, 코드 실증)**: `anima-base-v1`이 비상업인데 `commercial:true`로 상업 게이트 통과(false-positive, hunyuan3d 선례와 대칭). → **Anima 상업 A/B 후보 제외** + 메모리 🚩 미해결 **게이트 분류 fail-closed 정정 권고**(commercial:false; 1차 라이선스 출처 확인=사용자 영역).
- **B 단독 — cross-arch 비교 함정**: SDXL↔Qwen DiT 토큰 한계 비대칭(CLIP 77 vs LLM TE 무제한)·태그 dialect(Danbooru vs 자연어)·`compare_basemodels.py`는 SDXL-only import. → 비교 시 **명시 기록 + 짧은 프롬프트 통제**.
- **B 단독 — SDD 의무**: 베이스 교체 = provider-liquidity 핵심(헌법 5조-2) → 코드 변경(2순위) 전 설계 문서 + CLAUDE.md §8/INDEX 등록.
- **A 단독 — align 폴백 리스크**: 아벨린 비표준 실루엣(날개·뿔)에서 anime 얼굴 검출 흔들리면 center_top 저품질 폴백 → **정면·전신·단순배경 프롬프트 규약**으로 완화.

---

## 3. 합의 결정

1. **재현 수단**: img2img 체인(`generate_chain`) 확정. 재학습 = 범위 밖(사용자 본 적용 명시 시).
2. **베이스 후보**: Qwen-Image + illustrious-xl-2.0 (둘 다 등록·상업 안전). **Z-Image·Anima 제외**.
3. **비교 = 둘 다 준비**: 축1(raw 화풍 시트, LoRA 없이) + 축2(아벨린 체인 시트). 정직 명명 — 축2는 "정체성 A/B"가 아니라 "베이스별 구조 기여 비교"(화풍은 animagine 고정).
4. **R1 (Anima 게이트)**: 이번 후보에서 Anima 배제로 즉시 블로킹 회피. 별도 fail-closed 정정 권고(사용자 1차 라이선스 확인 영역).
5. **최소 산출물**: compare 스크립트(축1+축2, `compare_*.py` 복제) + comic_lab `--lora` 노출. 코어 무변경. cross-arch 함정 명시 기록.

### 진행 순서 (확정)

1. **[0코드·즉시] 아벨린 e2e 3트랙 실증** — 단일 일러 → 영상 mp4(그 PNG) → 만화 패널. 위험 0, 기반 확정.
2. **[소] 베이스 A/B 준비** — SDD 문서 선행 → compare 스크립트(축1+축2) + comic_lab `--lora` 노출 (TDD).
3. **[중·별개] ②말풍선 렌더러** — 만화 완성.
- 범위 밖: 신규 베이스 LoRA 재학습(사용자 명시 시).

---

## 4. 미검증 / 정직

- 축2 체인의 strength 스위트스팟(~0.45~0.6)은 실 이미지로 튜닝 필요(공정성: strength 고정·명시).
- 신규 베이스 화풍의 **순수** 비교는 체인으로 불가(2단계 animagine 고정) — 축1 raw 시트로만 가능.
- Anima/Z-Image 라이선스 1차 출처(CircleStone/Z-Anime LICENSE 원문) 미확인 — 추론적 가정. 상업 후보는 Apache/OpenRAIL 확정분만.
