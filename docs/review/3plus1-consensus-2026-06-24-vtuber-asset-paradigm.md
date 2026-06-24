# 3+1 합의 — 아벨린 버튜버 에셋 패러다임 결정

> 일자: 2026-06-24 (5부 후속) · 프로토콜: CLAUDE.md §3 (아키텍처 결정=3+1 필수)
> Agent A(구현)·B(품질/안전)·C(대안) 병렬 독립 분석 → Reviewer(메인) 교차 비교·합의.
> 입력: 로컬 자산 정찰 + deep-research(VTuber 3패러다임, 20 claim confirmed).

---

## 결정 질문
아벨린(큰 뿔·박쥐날개 오리지널 애니 캐릭터)을 버튜버로 만드는 에셋 패러다임을 **VRM/3D로 확정**할 것인가? (THA3=프로토타입 유지, Live2D=배제)

## 배경
- 현재 = 단일 평면 일러 + THA3 워핑(토킹헤드). loop3(단순 캐릭터)는 고품질이나 **아벨린 뿔/날개에서 깨짐**(5부 실증).
- 사용자 통찰: "버튜버용 그림체가 맞나, 그저 토킹헤드 이미지가 아닌?" → 그림체(화풍)는 적합하나 **에셋 포맷이 토킹헤드 수준**이라는 진단.
- 두 정찰(로컬 자산 + 외부 기술)이 표면상 VRM/3D로 수렴.

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus, 3/3 만장)
1. **"지금 VRM 확정"은 시기상조.** A(경로 B 구현 낮음)·B(확정 불가, 선결 2건)·C(확정 보류, PoC 먼저) 전원이 *무조건 확정*에 반대.
2. **StdGEN/TRELLIS 이미지→3D = 정적 메시, 리그·표정 모프 자동 생성 안 됨.** A("모프 0"), B("AI3D medial-axis·사용자 이미 품질 폐기"), C("GLB=정적 메시, 리그 자체가 자동으로 안 생김").
3. **뿔/날개 VRM 미검증.** 3/3 명시. 특히 **날개(독립 본 + 물리 스프링)는 우리 PoC 0건**.
4. **첫 단계 = 작은 PoC로 뿔/날개 + 리그/모프 실증 먼저** (계산적 검증 우선, CLAUDE.md §2).

### ② 부분 일치 (Partial, 2/3)
5. **"VRM"의 두 경로를 분리해야 한다 — char_factory(VRoid 절차조립) vs StdGEN/TRELLIS(AI생성 3D).** B가 최강(프레이밍 결함 지목), A가 경로 A/B 구분으로 정합. 결론: **VRoid 베이스 조립이 유효 경로, AI생성 3D는 버튜버 바디 메인에서 제외**(사용자가 이미 품질 폐기·2D pivot).
6. **Live2D 폴백 보존.** B(영구배제 성급→"1순위 비채택 + 폴백 보존"), C(2.5D 자체제작 fallback). A 미언급.

### ③ 불일치 (Divergence)
7. **fallback 후보가 다름**: C=2.5D 자체제작(puppet+See-Through, 정면 한정) / B=Live2D 폴백 + hybrid_phased(THA3 2D얼굴+3D바디) / A=경로 A 자체가 메인이라 fallback 약함. (약한 불일치 — 폴백 다층 보존으로 흡수 가능)

### ④ 누락 (Gap, 단독 — 중요)
- **B 단독 ⭐**: 순수 3D는 이미 `3plus1-consensus-2026-06-10-vtuber-body-motion-backend.md`에서 **A·B·C 만장 1순위 거부**, 만장일치 결론=`hybrid_phased`. "VRM 확정"은 그 합의를 뒤집는 **재결정** → supersede SDD/ADR 의무.
- **A 단독 ⭐**: 표정·립싱크 모프 출처 = **VRoid 통과가 사실상 강제**. poc_vrm_drive 립싱크(`VIS={"aaa":"target_37"...}`)는 AvatarSample_B.vrm에 *이미 있던* VRoid 표준 모프를 이름으로 쓴 것. 자동리깅 PoC엔 shape_key 0.
- **B 단독**: 라이선스 함정 3점 — StdGEN checkpoint **research-only**(상업 출력 구멍) / TRELLIS rembg 기본값(non-commercial, monkeypatch 의존) / VRM 메타 재export 동기화 미검증.
- **C 단독**: 머리 yaw 회전 = 2.5D 구조적 불가(Live2D 상용가치 핵심) · 브라우저 런타임(three-vrm/Live2D WASM)은 *런타임* 갭만 우회, *제작* 갭은 그대로.
- **A 단독**: VRM Blender Add-on = MIT·aarch64 순수 Python, 설치+`export_scene.vrm` 한 줄(블로커 낮음).

---

## Phase 4 — 합의 도출

### 핵심 판정
**방향(VRM 우선·Live2D 비채택)은 합리적이나, "지금 확정"은 시기상조다.** 세 Agent가 독립적으로 같은 결론에 도달했고, 두 가지를 먼저 풀어야 한다: (a) "어느 VRM인가"의 프레이밍, (b) 아벨린 뿔/날개의 실증.

### 합의 권고 (5)
1. **VRM/3D를 *지금 확정하지 않는다*** (3/3). 방향으로는 1순위 후보.
2. **"VRM"을 char_factory VRoid 절차조립 경로로 좁힌다.** AI생성 3D(StdGEN/TRELLIS 이미지→3D)는 **버튜버 바디 메인에서 제외**(사용자 품질 폐기 + 모프 0 + 정적 메시). StdGEN은 R&D 트랙으로만.
   - 근거: VRoid 베이스가 **production-grade 표준 본 + 표정 blendshape(a/i/u/e/o·blink·감정)를 상속** → A의 "모프 공짜", B의 "AI리그 비판 면제"가 동시 성립.
3. **선결 PoC 게이트 (단일 변수 실증, ~1~2일).** 아벨린 뿔/날개를 char_factory VRoid 베이스에 조립 → VRM export → `poc_vrm_drive` 구동. 체크포인트:
   - ⓐ **뿔** (head 본 부착) — 헤어 부착 선례로 가능성 높음
   - ⓑ **날개** (독립 본 + 물리 스프링) — **최대 미검증, 헤어 스프링보다 어려움**
   - ⓒ **표정·립싱크 모프** — VRoid 상속으로 즉시 동작 기대
   - 통과 → VRM 확정 / 실패(특히 날개) → fallback 강등
4. **폴백 다층 보존** (영구 삭제 0): Live2D(비채택이나 보존) · 2.5D 자체제작(puppet+See-Through, 정면 한정) · hybrid_phased(2026-06-10 합의).
5. **거버넌스 선결**:
   - `hybrid_phased` 합의(2026-06-10)를 명시 supersede하는 **VTuber 에셋 패러다임 SDD** 작성(확정 시).
   - 라이선스 함정 3점을 gen_gate/motion 게이트에 **명시 등록·검증**(StdGEN research-only / TRELLIS rembg / VRM 메타 동기화).

### 사용자 질문에 대한 답
> "버튜버용 그림체가 맞나, 그저 토킹헤드 이미지가 아닌?"

**맞다 — 현 단일일러+THA3는 토킹헤드 프로토타입이다.** 진짜 버튜버로는 **char_factory VRoid 조립 VRM**이 이 하드웨어(GB10 aarch64)에서 가장 현실적 경로다. 단 *지금 확정하지 말고*, 아벨린 뿔/날개가 그 경로에서 실제 되는지 작은 PoC로 검증한 뒤 확정한다. 화풍(animagine 일러)은 2D 텍스처/참조로 계속 쓰되, 리깅 가능한 에셋은 VRoid 베이스 위에 만든다.

---

## 다음 단계 (사용자 결정 영역)
- **옵션 1 (권고)**: 선결 PoC 게이트 진행 — 아벨린 뿔/날개 char_factory VRM PoC(~1~2일). 통과 시 확정 + SDD.
- **옵션 2**: char_factory 본류 강화(VRM export 마무리)부터, 아벨린 적용은 후속.
- **옵션 3**: 방향만 합의로 기록하고 다른 작업으로(버튜버는 백로그).

> ⚠️ 이 합의는 **방향 권고**다. 패러다임 *확정*과 구현은 PoC 게이트 통과 + 사용자 명시 후 별도 SDD·TDD.
