# 3+1 합의 보고서 — 원본 창작 AI 시스템 SDD

> 대상: `docs/architecture/original-creative-ai-system-design.md`
> 일자: 2026-06-29 · 프로토콜: CLAUDE.md §3 (Agent A 구현 / B 품질안전 / C 대안 → Reviewer)
> **종합 판정: 조건부 통과 / REVISE** (A=CONDITIONAL, B=CONDITIONAL PASS, C=REVISE — 기각 아님, 수정 후 PoC 진행 가능)

## ① 일치 (3개 모두) — 채택
1. **3계층 맵 타당** — 유지(repo 매핑·격리·순차 메모리).
2. **① Style Forge = 최저 리스크·진짜 핵심 → 먼저**(부품 in-repo, 배선만 신규).
3. **"RLHF-lite/RL/원본" 프레이밍 over-claim** — 실제=선호 큐레이션 **best-of-N SFT + prior 위 수렴**. 정직화 필수.
4. **"수렴"이 정성적(soft) → 정량 센서 필요**(계산적 검증 우선).
5. **③ 영상 = 최고 리스크 → 핵심 가치 걸지 말 것**(정체성 drift·오디오 미검증).
6. **② "다중 LoRA 동시=기존 지원/신규 코드 최소" 부정확**(A 실측: gen_gate 단일 슬롯 `gate.py`·`diffusers_sdxl.py:_apply_lora` unload-then-load; B: SDXL-LoRA↔영상모델 불일치; SDD 스스로 ZipLoRA 인용).

## ② 부분 일치 (2 동의) — 채택
7. **자동 클러스터링 강등**(B+C): CLIP는 *내용*으로 군집(화풍 아님)·콜드스타트 노이즈 → **MVP=명시 트랙**, 클러스터링 후속(스타일 임베딩 검증 후).
8. **순서 반전**(C 강력·A·B 동의): SDD 모순(P1 핵심인데 P0 먼저) → **P1→P2 우선, P0 병렬·비게이팅**.

## ③ 불일치 — 결정 보류
9. **영상 베이스**: A=CogVideoX(sm_121 SDPA 최선) vs C=Wan2.x(anime 생태계+오디오+Apache). 상충 아님(HW vs anime 능력 기준) → **0-A/0-B 스파이크에서 둘 다 평가**.

## ④ 누락 (단일 포착, 중요도 평가 후 포함)
- **B**: noobai 라이선스 전파(개인전용→상업, 헌법 비협상)·뿔/날개 비인간 drift 누락·재학습 vs 이어학습 모호(aveline loop-2 회귀 전례)·제3자 작가 시그니처 근접 정직성.
- **A**: 오디오 조건화 = 연구급(2D 리그 모션→I2V latent 다리 발명 필요, cheap PoC 불가) → P3 무음 I2V만, 발화는 motion_lab 2D 흡수.
- **C**: dislike(거부) 신호 회수(DPO 절반 신호)·무학습 콜드스타트(IP-Adapter)·본인 그림 학습(a) 선택 트랙(유일한 진짜 원본)·Hunyuan 영토 라이선스 선검증(0-C)·⭐**③ 대안(viseme/2.5D/THA3) 모두 Live2D 천장 재생산 → ③은 "Live2D 못하는 멀티포즈/head-turn 돌파"에만 조준, talking-head는 motion_lab 유지**.

## Phase 4 — 합의 결정 (SDD REVISE 사항)
1. 프레이밍 정직화(원본→고유 스타일 수렴, RL→선호 best-of-N SFT, 제3자 작가 근접 한계 명기).
2. ② 정정(다중 LoRA=신규 multi-adapter 코드+간섭 튜닝 필요, 미구현; 영상 보존=스타일 입력 이미지 조건화, LoRA 재적재 불가).
3. ③ 범위 축소("Live2D 천장 돌파"로 한정·오디오 P4+ 분리·병렬 스파이크 강등·Wan2.x 후보·0-C 영토 라이선스 게이트).
4. 순서 P1→P2 우선, P0 병렬.
5. 다중 스타일 MVP=명시 트랙, 클러스터링 후속.
6. ① 보강(dislike 회수·무학습 콜드스타트·정량 수렴 센서·base 재학습 고정·본인 그림(a) 선택 트랙).
7. 라이선스(상업 트랙서 개인전용 베이스 제외/등급 전파 규칙).
8. 게이트 정량화 + 뿔/날개 drift 0-B 명시.

## Phase 5 — 권고
**REVISE 반영 후 P1(Style Forge MVP — 명시 단일 트랙·best-of-N SFT·정량 수렴 센서)부터 진입**, P0 영상은 병렬 timebox 스파이크. "원본 창작 달성" milestone 선언은 갭 미해결 시 차단.
