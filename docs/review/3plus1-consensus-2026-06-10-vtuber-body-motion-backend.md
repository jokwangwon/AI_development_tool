# 3+1 합의 보고서 — VTuber 바디 모션 백엔드 결정

> **일자**: 2026-06-10 · **프로토콜**: CLAUDE.md §3 (아키텍처 결정 = 3+1 필수)
> **사안**: anime VTuber 캐릭터에 바디 모션을 추가하는 애니메이션 백엔드 결정
> **후보**: (1) 3D VRM 전신 · (2) 파츠 컷아웃 2.5D · (3) 하이브리드/단계적
> **근거**: 딥리서치 2건(3D VRM·파츠 컷아웃, 각 ~105 agents·23 소스·3-vote 적대 검증)
> **관련**: `talking-head-motion-design.md`, `reference_talking_head_lipsync_landscape`(메모리)

---

## 결과: 만장일치 `hybrid_phased` (단계적 하이브리드)

A(구현)·B(품질/안전)·C(대안) **3개 모두** 순수 단일 경로(3D 또는 2.5D) 즉시 채택을 거부하고
THA3(이미 작동·GPU 실증) 유지 + 단계 진입을 권고. Reviewer 채택.

## ① 일치 (Consensus)
- 둘 다 turnkey 아님 + 각각 미해결 자동화 링크 1개(3D=얼굴 blendshape 헤드리스 패키징 / 2.5D=자동 파츠 스켈레탈 리깅).
- GB10 aarch64 실측 검증된 컴포넌트는 **Blender 렌더 단 하나**. 나머지(UniRig·EMAGE·See-Through·Inochi2D)는 전부 포팅/검증 리스크.
- 지배 리스크를 PoC로 먼저 죽인 뒤에만 다음 단계 승격 — THA3 'sm_121+viseme 먼저' 패턴 답습(§2·하네스 규칙).
- 지금 단일 백엔드 '고정'은 over-claim — PoC로 지배 리스크 제거 전 '단계적 채택' 이상 선언 금지.
- 재사용 자산: THA3 렌더러(얼굴/입/blink 보존)·viseme 브리지(Allosaurus)·gen_gate 게이트+AND-clamp+attribution·renderer.py Provider Liquidity 계약·idle 결정적 프레임-함수(`_hash01`) 패턴 — 복제 0.
- 음성→제스처 SOTA(EMAGE·ZeroEGGS·DiffuseStyleGesture)는 전부 x86 stale(py3.7·sm_75)+영어 학습+neural(비결정) → aarch64 포팅·한국어·결정성 삼중 리스크.

## ④ 핵심 누락 발견 (Gap) — C 단독, HIGH, 코드 검증 완료
⭐ **THA3가 `body_y`/`body_z`(BODY_ROTATION)+`neck_z`를 이미 노출하나 motion_lab이 전혀 미구동**
(standard_float.py:282-284 정의 존재, renderer.py IDLE_PARAMS 미등장). idle(blink/breathing) 때 쓴
`compose_pose` disjoint 가산 패턴으로 **0 신규 의존성·0 HW 리스크·0 라이선스 변경**으로 상체 sway/lean/
weight-shift 추가 가능. → 만장일치 '상체 강화' 권고를 가장 싸게 실현하는 무료 레버.

기타 누락: [B] 음성→제스처 weight 라이선스 gen_gate 게이트 미등록(AND-clamp fail-closed 위험) ·
[B] single-image→3D 측면/후면 환각 천장 · [A] bpy aarch64 휠 부재→`blender --background` 서브프로세스 IPC 전제.

## ② 부분 일치 / ③ 불일치 (요약)
- **2.5D 위상**: B·C는 hybrid 1단계 대비 우위 없음으로 격하(영구 수동 리깅 부채·측면/회전 구조적 천장). A는 '3D no-go 시 폴백'으로 보존. → 다수 채택: 1순위 제외, 문서상 폴백만.
- **B의 갭 우회 통찰**: 3D 가도 얼굴=THA3 2D / 바디=3D 분업이면 VRM 얼굴 blendshape 패키징 *불필요*. 채택하되 2D얼굴↔3D머리 시점 정합을 PoC 검증 대상으로.
- **첫 PoC 선정 불일치**: A(Blender 렌더+EMAGE 부팅 병렬) vs B(Blender+UniRig+고정BVH 풀체인) vs C(THA3 body 축 0-의존성). → C 채택: 비용 비대칭 압도(0 의존성·1~2일)이고 '3D가 정말 필요한가'라는 상위 분기를 *먼저* 결정. 순서 = C → (불충족 시) B → (3D go 시) A.

## 최종 권고 — 단계적 로드맵
- **Phase 0** (1~2일, 분기 결정): THA3 body_y/body_z/neck_z 단독 구동 PoC → 상체 회전 각도 한계 시각 측정. **[완료 2026-06-10: 전 구간 -1→+1 붕괴 0 실증]**
- **Phase 1** (즉시 출하): `compose_pose`에 상체 sway/lean/weight-shift를 idle 동일 결정적 프레임-함수+disjoint 가산으로 추가(신규 의존성 0). 발화 amount 연동 weight-shift. capabilities='살아있는 상체 토킹헤드'(over-claim 가드). **[완료 2026-06-10: 110 tests + 실 e2e mp4]**
- **Phase 1.5** (선택): 절차적 음성→상체 제스처 사전·강세 매핑 정교화(neural 미사용, 결정성 보존).
- **Phase 2** (3D go 시에만): 신규 contract 경계 설계 → Blender 헤드리스 UniRig.glb+고정BVH(Mixamo)→OptiX→mp4 PoC + 환각/시점정합 검증. `blender --background` 서브프로세스 IPC 전제.
- **Phase 3** (Blender 생존 후): EMAGE/ZeroEGGS aarch64 부팅+한국어 검증+BVH→VRM 리타게팅. neural 비결정은 seed 고정+BVH 캐싱. weight를 gen_gate 게이트 등록.
- **폴백**(3D no-go): 2.5D는 1순위 아님. THA3 상체(Phase 1)+절차적 정면 제스처(Phase 1.5)로 안착.

## 사용자 잔여 결정 (BLOCKING)
1. **'전신 움직임' 정의** — 표현력 상체(Phase 1로 끝) vs 진짜 걷기·360 회전(3D 불가피, 6~12주+).
   → **[결정 2026-06-10: 단계적 — 상체 먼저 출하 후 재평가]**
2. 유지보수 부채 성격(2.5D 반복 수동 vs 3D 일회 고위험) — 현 권고 둘 다 1순위 배제.
3. 결정성 vs 표현력(3D 바디를 절차적/결정적 vs neural) — §2 충돌점, Phase 3 시 결정.
4. Phase 2 시 얼굴=2D/바디=3D 분업 채택 + 시점 정합 PoC 포함 여부.
5. capabilities 라벨 = '진짜 전신' 아닌 '살아있는 상체 토킹헤드' over-claim 가드 동의 — **[동의됨]**
