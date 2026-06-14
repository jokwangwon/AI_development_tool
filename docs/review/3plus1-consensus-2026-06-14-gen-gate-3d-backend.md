# 3+1 합의 보고서 — gen_gate에 self-host AI 3D 생성 backend 통합

- **일시**: 2026-06-14
- **주제**: 검증된 로컬 AI 3D 생성 파이프라인(이미지→3D 캐릭터/사물)을 gen_gate에 정식 backend로 통합
- **프로토콜**: CLAUDE.md §3 (3+1: 구현 분석가 A / 품질·안전 검증가 B / 대안 탐색가 C → Reviewer 종합)
- **상태**: 합의 완료. 구현은 다음 세션. **⚠️ 중요 — 합의는 Hunyuan3D 2.1을 대상으로 수행됐으나, 합의 결과(B1 라이선스 BLOCKING)로 모델이 TRELLIS.2-4B로 교체됨. 아키텍처 결론(subprocess 격리·범위·추적성 등)은 모델 무관하게 TRELLIS.2에 그대로 적용된다.** (관련: SESSION_2026-06-14.md, 메모리 `project_ai_3d_selfhost_gb10`)

---

## 0. 배경 / 검토 대상 설계

GB10(aarch64, sm_121 Blackwell, 121GB 통합메모리)에서 image→3D(shape+PBR) 생성을 실증. 이를 gen_gate(provider-agnostic composable 생성 게이트)에 끼우는 설계:
- **D1 서브프로세스 격리**: gen_gate(diffusers 0.38)와 3D 스택(별도 venv, diffusers 0.30 등) 충돌 회피 위해, backend가 별도 venv python으로 러너를 subprocess 호출, `RESULT_PATH` 파싱.
- **D3 shape+paint 기본 on** (texture=false면 shape-only).
- gen_gate backend 계약: `generate(spec, prompt, out_path, input_image=None, **opts) -> str` (duck typing).

gen_gate 구조(Explore 매핑): `model_registry.json`(메타) + `gate.py` BACKENDS dict(핸들러) + `server.py`(HTTP `/api/generate`·`/api/capabilities`·`/api/models`·`/outputs`) + `registry.py` `assert_allowed`(commercial 플래그 등급 게이트). 기존 `local-3d-hunyuan` backend(구버전 2.0, in-process, shape-only)가 이미 존재.

---

## 1. ① 일치 (3 에이전트 모두 동의)

1. **subprocess 격리(D1)는 옳고 거의 유일한 현실해** — diffusers 0.30(3D)/0.38(gen_gate)/0.27.2(구 backend) 3중 충돌 실측. 한 프로세스 공존 불가.
2. **신규 backend로 추가** (기존 2.0 backend 덮어쓰기 금지 — 회귀 방지).
3. **범위를 image→textured GLB까지로 좁혀라** — 리깅/리토폴로지는 이 통합에서 분리. (motion_lab에 dense-mesh decimate+rig PoC 이미 존재.)

## 2. ② 반드시 해결 (BLOCKING)

| # | 이슈 | 출처 | 근거/내용 |
|---|------|------|-----------|
| **B1** | ⚠️ **라이선스 영토 제외** | B | **Hunyuan3D 2.1 Community License가 EU·UK·South Korea를 영토에서 명시 제외**(LICENSE §1.l, §5.c: 영토 밖 Output 사용은 unlicensed). 사용자=한국 거주 → `commercial:true`는 게이트 통과시키나 실제 미허가(false-negative). **→ 이 BLOCKING이 모델 교체(Hunyuan 폐기 → TRELLIS.2)를 강제함.** |
| **B2** | ⚠️ **"PBR" over-claim** | A | Hunyuan paint의 bpy 우회(trimesh fallback)가 `map_Pm/Pr/Bump`(metallic/roughness/normal) 미파싱 → glb엔 baseColor+상수 roughness만. **→ TRELLIS.2 채택으로 해소**(o_voxel.to_glb가 baseColor+metallicRoughness 4096² 진짜 PBR 임베드). |
| **B3** | VCS 추적 0 — 재현 불가 | B,C | `~/3d_lab`에 git 없음, 패치들이 dirty working-tree·`.so` 빌드물 gitignore. **→ 다음 세션 선결: 안정 위치 + git 추적 + patch 파일/빌드 절차 문서화.** |
| **B4** | 동기 194s → 타임아웃 | A | gen_gate `/api/generate` 동기. 3D 생성은 분 단위(TRELLIS.2 ~8분) → 504/좀비. `subprocess.TimeoutExpired`를 server except에 잡히게 변환. 비동기 잡 vs 타임아웃 상향 결정 필요. |
| **B5** | HF 공급망 — pickle ACE | A,B | `from_pretrained` revision 핀 없음 + `use_safetensors=False` 경향 → HEAD pickle 로드. 커밋 핀 + safetensors 우선 권고. |
| **B6** | subprocess 견고화 | A,B | `shell=False`+리스트 인자(인젝션 차단), `RESULT_PATH` **마지막 줄** 파싱(stdout 로그 오염 대비), exit≠0→stderr 동봉 RuntimeError, out_path 실존 검증, **GPU 직렬화 Lock**(동시 호출 OOM/좀비 방지), input_image PIL→임시파일. |

## 3. ③ 부분 일치 / 대안 (트레이드오프)

- **콜드스타트**(A,C): subprocess는 매 호출 모델 재로드(수십초~분). MVP는 subprocess로 가되 러너에 **상주 serve() 훅**을 남겨 후속에 로컬 프록시(C안 (c))로 승격 → 콜드스타트 해결. Provider Liquidity 정합(registry `local:true`).
- **타임아웃 처리**(A): 비동기 잡 vs 타임아웃 상향 vs modality 분기. 비동기는 voice_lab 정렬 envelope를 깸(트레이드오프).
- **dense 메시**(C): 기본 보존(품질 우선) + 선택적 decimate 옵션(`fast-simplification`, open3d 불필요). (TRELLIS.2는 `o_voxel.to_glb`에 decimation_target 내장 — 이미 ~1M로 감소.)

## 4. ④ 누락 → 추가 발견 (Gap)

- **모델 의존성 라이선스**(B): DINOv2/RealESRGAN 등 출력 기여 컴포넌트 라이선스를 HF 카드로 직접 확인. **→ TRELLIS.2에서 실제 발현**: DINOv3(commercial·worldwide·"Built with DINOv3" 표기)·BiRefNet(기본 `briaai/RMBG-2.0`=게이트+non-commercial 함정 → `ZhengPeng7/BiRefNet` MIT로 교체). **gen_gate 라이선스 플래그/notes에 "Built with DINOv3" attribution 의무 반영 필요.**
- **StdGEN 투트랙 씨앗**(C): registry에 `available:false` 등재 + xformers→SDPA 교체 실험(분해형은 캐릭터/VTuber에 구조적 우위, 현재 Blackwell 막힘).

## 5. Reviewer 최종 판단

기술적으로 **subprocess 신규 backend + 범위 축소(image→GLB) + 추적성 정리(git+patch)** 로 가면 견고. B3~B6은 구현 단계 처리 항목. **B1(라이선스 영토)·B2(PBR)는 사용자 결정 → 결과: Hunyuan3D 2.1 폐기, TRELLIS.2-4B 채택**(MIT + DINOv3 worldwide/한국OK + 진짜 풀 PBR).

### 다음 세션 구현 체크리스트 (TRELLIS.2 기준)
1. (선결, B3) 러너 패치 영속(`~/3d_lab/hy3d21_runner.py` 패턴으로 TRELLIS 러너 일반화: 입력 이미지/출력 GLB/texture 인자, BiRefNet→ZhengPeng7 + DINOv3 layer 경로 패치 내장, `RESULT_PATH` 규약) + `~/3d_lab` git 추적 + 빌드 절차(flash-attn ARCH=12.0, 커널5종, **MAX_JOBS=2+워치독**) 문서화.
2. gen_gate 신규 backend `local-3d-trellis`: `.venv_trellis` subprocess 격리, B6 견고화 전부 적용, image→GLB.
3. `model_registry.json` 등재: modality=3d, license/commercial 플래그 + **DINOv3 "Built with DINOv3" attribution notes**, `local:true`.
4. (B4) 동기/타임아웃 정책 결정.
5. (분리 아크) 리토폴/리깅 → motion_lab.

---

*부록: 3 에이전트 원시 분석은 세션 d1dcc462 트랜스크립트에 보존(Agent A 구현 50.7k tok / B 품질·안전 56.5k / C 대안 56.2k). 본 문서는 Reviewer 종합 + 모델 전환 반영본.*
