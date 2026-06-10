# 3+1 합의 보고서 — 토킹헤드 모션 설계 (2026-06-10)

> **대상**: `docs/architecture/talking-head-motion-design.md` (D-1~D-4)
> **프로토콜**: CLAUDE.md §3 (3+1 멀티에이전트 합의)
> **종합 판정**: **REVISE** (방향 만장일치 승인 · 계약/라이선스/성능 세부 보완)
> **에이전트**: A(구현분석가) · B(품질안전검증가) · C(대안탐색가) + Reviewer

---

## 종합 판정: REVISE

세 에이전트 모두 **REVISE** 일치. 아키텍처 골격(THA3 렌더러 + audio→viseme 브리지 + 독립
capabilities 서비스)은 PoC 2건으로 실증됐고 Local-First·Provider Liquidity·계산적 우선·비례
보안 등 비협상 제약과 정합. 방향 승인하되 라이선스 진술·합성물 게이트·동기 계약·성능 표기 4영역 보완.

---

## 결정 항목별 합의 권고 (결정 고정 = 사용자 영역)

### D-1 — 배치: 독립 motion_lab 서비스 [만장일치, high]
- 독립 서비스로 시작. capabilities envelope = gen_gate/voice_lab 동형.
- ⚠️ **근거 교체**: 설계의 '입력 2모달리티가 gen_gate 단일에셋 가정과 충돌'은 부분적으로만 옳음.
  코드 확인: `gen_gate/server.py:91-96` HTTP 계층은 prompt 강제(None시 400)지만,
  `backends/local_3d_hunyuan.py`는 prompt 미사용+input_image 필수로 **image-only 생성을 이미 처리**
  (C 실측 반박). 결론(독립)은 유지하되 차단 근거를 **운영 라이프사이클 분리**(THA3 GPU 상주
  1.8GB·30fps 렌더 루프·ffmpeg mux 운영이 gen_gate stateless 단발 생성과 다름)로 교체.
- 게이트 로직(load_registry/select/assert_allowed)은 **복제 금지 → gen_gate 공유 모듈 재사용**.

### D-2 — 브리지 프론트엔드: 계약 격리 + 기본 포먼트 [만장일치]
- `bridge.analyze(wav,fps)->List[{vowel,amount}]` 계약 먼저 고정.
- **1단계(교체 전 분류기 수정)**: `poc_bridge.py`의 `mouth_uuu(350,800)`/`mouth_ooo(480,900)`
  포먼트 중심값 근접 중첩 → ooo 미선출, line 83 무성 폴백이 무조건 `mouth_aaa` → 편향(iii 과다·ooo 0)
  증폭. 중심값 재캘리브레이션 + 폴백 '직전 viseme 유지' + 스무딩으로 결정적 경로 내 개선(§2 계산적 우선).
- **2단계(교체)**: Allosaurus 1순위(다국어·텍스트 불필요·경량), MFA 2순위, **Rhubarb 후보 제거**(영어 전용).
- ⚠️ **ROI 전제**: THA3 노출 viseme=5모음뿐(자음·양순폐쇄 없음). 모든 프론트엔드 정밀도 이득이
  5모음으로 양자화 소실. 입 자연스러움은 프론트엔드 교체보다 45-dim 내 jaw/입꼬리 활용이 더 큰 레버.

### D-3 — THA3 라이선스 등급 게이트 [다수+소수이견, BLOCKING]
- Reviewer 직접 확인: 코드=**MIT**(Pramook Khungurn 2022), weight=**CC BY 4.0**(README line 128-129
  "상업 사용 가능, 배포시 저작자 표시 의무"). Crypko/lambda는 weight 학습데이터가 아니라
  `data/images` **데모 입력 샘플**의 라이선스(프로덕션은 gen_gate 일러스트 입력 → 무관).
- → 설계의 'commercial:false 보수 표기'는 **과소차단(부정확)**. `license:'cc-by-4.0' +
  commercial:true + attribution_required:true`로 정정. (C는 보수 표기 유지 의견이었으나 실측과 어긋남.)
- **핵심 보강(B·C 합의, BLOCKING)**: 모션 출력=합성물 → 상업화 = 입력 image ∧ 입력 audio ∧
  THA3 weight **3자 AND clamp**(가장 보수적 등급). `voice_lab/server.py:69-73`의 fail-closed
  (commercial=true시 primary+aux 중 비-CC0 1개라도 차단) 선례 답습.

### D-4 — repo화 시점: DEFER 후 트리거 승격 [만장일치]
- 즉시 repo화 아님(비례성). 트리거: (1) bridge.analyze 계약+포먼트 1단계 수정 test GREEN,
  (2) 공유 게이트 모듈 추출 완료. 충족 시 feature 브랜치(베이스=develop) 승격.
- THA3 vendor 코드+weight(797MB)는 .gitignore/submodule 미추적, 다운로드 스크립트+attribution NOTICE 재현.

---

## 사용자 BLOCKING 항목 (구현 진입 전 해소)
1. **D-3 라이선스 정정** — commercial:false → cc-by-4.0/commercial:true (실측 근거)
2. **D-3 attribution 집행 지점** — 출력 메타데이터/NOTICE 어디서 충족
3. **D-3 합성물 AND clamp** — 3자 중 가장 보수적 등급 fail-closed (voice_lab 선례)
4. **D-1 generate 계약** — 긴 클립 대비 max_duration 게이트 vs async job(POST→job_id) 선택
5. **D-2 우선순위** — 포먼트 분류기 자체 수정을 교체보다 먼저 할지

## 추가 보완 (non-blocking)
- 성능 표기: §4.1 raw 30fps(GPU 추론 한정) vs 실 throughput ~18fps(알파합성 CPU 루프) 분리 명시.
- 브리지/렌더러 경계: viseme→45dim 매핑이 렌더러 책임임을 §4 명시(THA4 교체 시 브리지 무변경).
- 무음/한국어 음소 엣지: `poc_bridge.py:79` 이중정규화 무음 임계를 결정적 계약으로. 한국어 ㅓ/ㅡ
  미커버 한계가 capabilities label에 over-claim 안 되게.

## 교차비교 분류 요약
- **일치(만장일치)**: D-1 결론·D-2 계약격리·D-4 DEFER·성능 표기 분리
- **불일치**: D-1 근거(gen_gate 편입 불가 사유) — C가 실측 반박, 운영 분리 근거로 교체
- **부분일치**: D-3 라이선스 사실(A·B 정확/C 보수)·합성물 clamp(B·C)·attribution(A·B)
- **누락(1만 제기, 채택)**: D-2 포먼트 자체수정 1단계(C)·5모음 천장(C)·async job(A)·viseme→45dim 경계(A)

## 비협상 제약 점검
Provider Liquidity·Local-First·계산적 우선·비례 보안 위반 **없음**. 단 게이트 복제(D-1)·라이선스
오기입(D-3) 방치 시 깨질 수 있어 보완 전제.
