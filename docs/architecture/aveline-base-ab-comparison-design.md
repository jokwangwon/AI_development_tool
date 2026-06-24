# 아벨린 베이스 모델 A/B 비교 준비 — 설계 (SDD)

> **상태**: 설계 → 검토 → TDD 구현
> **근거 합의**: `docs/review/3plus1-consensus-2026-06-24-aveline-multimedia-base-ab.md`
> **범위**: "현 animagine vs 새 베이스" 두 케이스를 **비교 가능하게 준비**(실 재학습/모델 채택은 사용자 영역). 멀티미디어화 3트랙 e2e는 1순위에서 PASS 완료.

---

## 1. 목표 / 비범위

- **목표**: 사용자가 동일 시드·프롬프트로 베이스 모델을 A/B 비교할 수 있는 **재현 가능한 비교 하네스**를 준비. 비교 축 둘 다(사용자 확정).
- **비범위**: 신규 베이스로 아벨린 LoRA 재학습("준비만" 위배), 모델 실 채택(사용자 결정), Z-Image/Anima(합의에서 제외 — 코드 0건·라이선스 미확인·비상업).

## 2. 두 비교 축 (정직 명명)

| 축 | 질문 | 메커니즘 | 아벨린 정체성 |
|----|------|---------|--------------|
| **축1 — raw 화풍/품질** | "어느 베이스 그림체가 좋은가" | `gate.generate(model, prompt)` **LoRA 없이**, 동일 시드·프롬프트, 모델별 native 설정 | 없음(캐릭터 무관) |
| **축2 — 아벨린 정체성 재현** | "아벨린을 만들면 베이스별로 다른가" | 케이스 A=`generate(animagine, lora=aveline)` 단독 vs 케이스 B/C=`generate_chain(structure=새 베이스, style=animagine, lora=aveline)` 체인 | LoRA가 보장(체인 2단계 animagine 고정) |

> **정직**: 축2는 "정체성 A/B"가 아니라 **"베이스별 구조/해부학 기여 비교"**다. 최종 화풍은 항상 animagine(2단계 고정), 새 베이스는 1단계 구조에만 기여. 순수 화풍 비교는 축1로만 가능.

## 3. 베이스 후보 (합의 확정)

- **축1**: `animagine-xl-4.0`(baseline) · `illustrious-xl-2.0`(SDXL·상업) · `qwen-image`(DiT·실사·Apache).
- **축2 체인 1단계(structure)**: `qwen-image`(해부학 강점, 검증됨) · `illustrious-xl-2.0`(애니 SDXL). 2단계(style)=`animagine-xl-4.0` 고정(LoRA 호환 강제).

## 4. 구현

### 4-1. `gen_gate/compare_aveline_basemodel.py` (신규)

- **기존 `compare_basemodels.py`는 SDXL-only**(`from backends import diffusers_sdxl` 직접) → qwen DiT 미지원. 따라서 **`gate.generate`/`gate.generate_chain` 경유 신규 스크립트**(코어 무변경, 기존 스크립트 불변).
- 두 축을 모드 인자로(`--axis style|identity|both`). 산출 = `outputs/aveline_ab/{axis}_{label}_{seed}.png` + montage 시트.
- **OOM 회피**: 모델당 순차 — 각 케이스 생성 후 `diffusers_sdxl._PIPE_CACHE.clear()` + (qwen 캐시 해당 시) 해제 + `torch.cuda.empty_cache()`. `gate.generate`가 내부 `gpu_flock` 직렬화하므로 추가 lock 불요.
- **cross-arch 공정성 통제(명시 기록)**:
  - 동일: seed, prompt(내용), 해상도, hires.
  - 모델별 native: quality_tags/negative/CFG/rescale/clip_skip = 레지스트리 자동(백엔드 책임). style preset 미적용(룩 텍스트가 base 비교 오염).
  - **함정 주석 필수**: ① 토큰 한계 비대칭(CLIP 77 vs LLM TE 무제한) → **짧은 프롬프트** 권고. ② 태그 dialect(Danbooru vs 자연어) → qwen에 불리할 수 있음, 결과 해석 시 명시.
  - 축2 체인: **strength 고정·기록**(기본 0.5, 공정성 — 높으면 1단계 구조가 animagine 화풍에 먹힘).

### 4-2. `comic_lab/make_comic.py` — `--lora` CLI 노출

- 현재 `render_panels`까지 `**opts`로 `lora=`가 흐르나 CLI에 미노출(라이브러리 호출만 가능). argparse `--lora` 추가 + `make_comic(...)` 시그니처에 `lora` 전달(`**img_kwargs` 배관 기존).
- e2e(1순위)에서 `lora="aveline"` 게이트 통과 실증 완료 — 이건 그 경로의 CLI 표면화.

## 5. 테스트 (TDD)

- **comic_lab**: `make_comic.py main`이 `--lora aveline` 파싱 → `make_comic`/`render_panels`에 전달되는지(gate_fn mock으로 opts에 `lora` 포함 검증). RED→GREEN. 기존 61 tests 회귀 0.
- **compare 스크립트**: 케이스 조합 로직 단위 테스트(gate_fn/chain_fn mock — 축1=lora 없음, 축2-A=animagine+lora 단독, 축2-B/C=chain structure 교체). GPU 실행은 수동 e2e(사용자 비교 실행 영역).

## 6. 산출물 / 정합성

- gen_gate `compare_aveline_basemodel.py` + 테스트. comic_lab `make_comic.py --lora` + 테스트.
- CLAUDE.md §8 참조 테이블 + INDEX.md 등록. 코어(jarvis) 무변경.
- **미해결 기록**: R1(anima-base-v1 게이트 false-positive)은 이 작업 후보에서 Anima 배제로 회피 — 별도 fail-closed 정정 권고(사용자 1차 라이선스 확인 영역). 이 설계는 R1을 건드리지 않음.
