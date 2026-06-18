# 3+1 합의 — 콘텐츠 등급(선정성) 분류 게이트 (gen_gate)

> 날짜: 2026-06-19 · 유형: 아키텍처/보안 결정 · 결과: **권고 도출, 구현 착수 전부 DEFER (사용자 결정)**
> 적용 대상: `~/gen_gate` (로컬 GB10 생성 AI 중앙 게이트, 현재 상업화 등급 1축만 강제)
> ⚠️ 이 합의는 **권고**다. 수단 결정·threshold 고정·구현 착수는 **사용자 영역**.

## 결정 질문
gen_gate 에 **콘텐츠 등급(선정성/NSFW) 분류 게이트**를 도입할 것인가? 도입한다면 어떤 구조·시점으로? solo 개인 툴, provider-liquidity 비협상, 한국 거주, GPU 추가 추론 회피.

## 핵심 프레임 — 두 직교 축으로 분해
- **축 X — 절대 금지선**(가상/애니풍 포함 미성년 성적 표현) = 형사 리스크 실재. 비례성 예외.
- **축 Y — 일반 수위 등급**(safe ~ explicit) = 개인 소지는 형법 음란물 *반포 목적* 요건 미충족이라 리스크 낮음.

## ① 만장일치 합의 (3/3)
1. **현재 `rating` 필드는 "게이트"가 아니다** — 차단 기능 0. 실체는 `diffusers_sdxl._compose_prompt`(:90)에서 프롬프트에 booru 태그를 주입하는 **조향 태그**(사용자 프롬프트로 덮임). "콘텐츠 게이트가 이미 있다"는 전제는 거짓.
2. **gen_gate 본체엔 콘텐츠 AND-clamp 없음** — clamp 는 `motion_lab/gate.py assert_composite_allowed` 에 **commercial 축 전용**으로만 존재.
3. **출력 분류기(feedback)는 도입 금지(DEFER)** — GB10 OOM + aarch64/sm_121 분류기 가용성 미검증 + 애니 도메인 정확도 낮음(실사 학습) + provider-liquidity 충돌(분류기=숨은 정책 모델) + "생성 후 차단" 비결정성.

## ② 한국 법 — Agent B 추가 차원
- **아청법 11조**: 가상/애니풍 포함 미성년 성적 표현물 = **제작·소지·시청 자체 처벌**("인식될 수 있는 표현물", 실사 불요). → solo 로컬 생성·저장만으로 리스크. **유일하게 형사 리스크가 실재하는 지점.**
- 형법 음란물(243·244조)은 *반포·판매 목적* 요건 → 순수 개인 소지 리스크 낮음.
- ⚠️ 가상 미성년의 *판단 경계*는 **변호사 확인 필요(미확인)**. 절대선 존재는 확실, 경계는 미확정.

## ③ 시점 — 3구간 권고
| 구간 | 항목 | 형태 |
|------|------|------|
| 🟢 지금 | 축 X — 절대 금지선 hard-block | `available:false` 동급, 항상-ON·우회불가·모드/선언 무관. 경량 prompt deny-list(미성년 지칭어 ∩ 성적 표현어) + 차단 로그. 무거운 분류기·GPU 불필요 |
| 🟡 스키마만 지금 | 축 Y 데이터 모델 | 신규 필드(예 `content_ceiling`) enum(`safe/sensitive/questionable/explicit`) + 전 모델 채움 + 노출. 집행·clamp 부착 0. 기존 `rating`(조향 태그)은 이름 충돌 회피 위해 분리 보존 |
| 🔴 DEFER | 축 Y 집행 / 출력 분류기 / input_image 콘텐츠 검사 | 무검열 trigger 도래 시 집행만 얹음. 분류기는 만장일치 영구 DEFER |

## ④ 누락(Gap) 채택
- (B) input_image 경로(3D, 프롬프트 없음) = deny-list 사각지대 → 정직 표기.
- (C) 업계 관행(Civitai 출력에만 등급·모델엔 nsfw boolean / HF `not-for-all-audiences`=경고 메타 / SD safety checker=출력 분류·로컬 기본 off) = 모두 *모델 선언 ⊥ 출력 집행* 계층 분리. 누구도 commercial 식 단일 boolean 으로 content 집행 안 함.
- (A) `rating` 이름 충돌(조향 vs 게이트) → 새 필드는 별도 이름.
- (B) 영토 축: 한국 거주 = 절대선 항상-ON 고정.

## 정직한 한계 (over-claim 차단)
- deny-list = **부분 prevention**. 은어·다국어·암시·input_image 우회 잔존. detection ≠ prevention.
- feedforward 선언 ≠ 실제 출력(범주 오류 가드: "천장 선언"이지 "실제 수위 보장" 아님).
- 이 합의는 어떤 threshold 도 고정 안 함, 어떤 수단도 결정 안 함(메모리 "수단 결정/threshold 고정 0건" 원칙 준수).

## 사용자 결정 (2026-06-19 수령)
- **퀄리티 우선 연구 활동 → 콘텐츠 게이트 구현 전부 DEFER**(축 X hard-block 포함, 지금 착수 안 함). 실제 해당 방향 출력 생성 시 재논의.
- 즉 현재 gen_gate 는 상업화 1축만 유지, 콘텐츠 수위는 **모델 선택(noobai/illustrious 등)에 의존**.

## 열린 질문 (재진입 시)
1. 축 X 구현 착수 / deny-list 어휘·언어 범위 / 미선언 모델 기본 천장(explicit 보수 vs safe 낙관) / 신규 필드 이름 / 변호사 확인.
