# ADR-015: VTuber 에셋 패러다임 = char_factory VRoid 조립 VRM

**상태**: 승인 (3+1 합의 → PoC 게이트 PASS → 사용자 명시 확정 — 2026-06-24)
**날짜**: 2026-06-24
**의사결정자**: 사용자 + 3+1 합의 — `docs/review/3plus1-consensus-2026-06-24-vtuber-asset-paradigm.md`
**상위 권위**: 헌법 제5조-2 (Provider Liquidity — 도구/모델 교체) · CLAUDE.md §2 (계산적 검증 우선 — PoC 게이트로 미검증을 실증) · `feedback_proportionate_security_personal_tool` (비례 노력)
**Supersedes**: `docs/review/3plus1-consensus-2026-06-10-vtuber-body-motion-backend.md` (hybrid_phased) 의 "조건부 3D 전신(Phase 2~3)" — 본 ADR이 확정으로 승격·구체화
**관련 설계**: `talking-head-motion-design.md` · 메모리 `project_motion_lab`, `reference_stdgen_gb10_unblocked`

---

## 1. 맥락 (Context)

아벨린(큰 붉은 뿔 + 박쥐 날개를 가진 오리지널 애니 캐릭터)을 버튜버로 발전시키려는데, 현재 경로(단일 평면 일러 + THA3 워핑)는 **토킹헤드 프로토타입**이지 버튜버 리그가 아니다. THA3(인간 얼굴로 학습된 단일 이미지 워핑)는 loop3(단순 캐릭터)에서는 고품질이나 **아벨린 뿔/날개에서 깨진다**(2026-06-24 실증) — 비인간 돌출 요소에 매핑이 없는 구조적 한계.

사용자 통찰: "버튜버용 그림체가 맞나, 그저 토킹헤드 이미지가 아닌?" → 화풍(적합)과 **에셋 포맷**(토킹헤드 ≠ 리깅된 버튜버 에셋)을 분리해야 한다.

세 패러다임(THA3 토킹헤드 / Live2D 부위분리 / VRM·3D)을 로컬 자산 정찰 + deep-research(20 claim confirmed)로 비교한 결과:
- **Live2D**: 2D 품질 천장 최고이나 Cubism Core가 **aarch64 데스크톱 Linux 공식 바이너리 없음**(GB10 불리), 리깅은 AI 자동화 불가(사람 몫), 우리 자산 0.
- **AI생성 3D**(StdGEN/TRELLIS 이미지→3D): 사용자가 이미 품질 폐기(`reference_stdgen_gb10_unblocked`), GLB=정적 메시(리그·표정 모프 자동 생성 안 됨).
- **char_factory VRoid 절차조립**: VRoid CC0 베이스가 production-grade 표준 본 + 표정 blendshape를 **상속**, MIT·aarch64 친화, 우리 자산 최다.

## 2. 결정 (Decision) — char_factory VRoid 조립 VRM 채택

VTuber 에셋의 메인 패러다임을 **char_factory(VRoid CC0 베이스 절차조립) → VRM** 으로 확정한다.

### 2.1 "VRM"의 정의 — AI생성 3D와 분리 (합의 핵심)
- 채택: **char_factory VRoid 절차조립 VRM**. VRoid 베이스의 표준 본 + 표정 모프(a/i/u/e/o·blink·감정)를 상속하므로 "AI 자동리그 품질 미달(medial-axis 근사)" 비판에서 **면제**된다.
- **제외(메인에서)**: AI생성 3D(StdGEN/TRELLIS 이미지→3D) — 정적 메시·모프 0·사용자 품질 폐기. R&D 트랙으로만 보존.

### 2.2 폴백 다층 보존 (영구 삭제 0)
- **THA3 토킹헤드**: 단순 캐릭터·정면 말하는 클립 용도로 유지(loop3 실증). 폐기 아님.
- **Live2D**: 비채택이나 보존(aarch64 런타임 갭·리깅 수작업이 해소되면 재평가 가능).
- **2.5D 자체제작**(`puppet.py` + See-Through 레이어 분리): 정면 한정 폴백.

### 2.3 hybrid_phased(2026-06-10) supersede
- 06-10 합의는 "THA3 2D 얼굴 + 3D 바디 분업(VRM blendshape 갭 우회), 조건부 Phase 2~3"였다.
- PoC 게이트 PASS로 **char_factory VRM이 표정 모프를 자체 상속**(VRoid)함이 확인되어 "VRM blendshape 갭"이 소멸 → THA3 얼굴 합성 분업 불필요. "조건부 3D"를 **char_factory VRoid 조립 VRM 전신으로 확정 승격**한다.

## 3. 근거 — PoC 게이트 PASS (계산적 검증, CLAUDE.md §2)

확정 전 합의가 지목한 미검증을 실증(`3plus1-consensus-2026-06-24-vtuber-asset-paradigm.md` 부록):
- **VRM export 경로**: VRM-Addon v4.3.0(Blender 5.1 지원) + `export_scene.vrm` 작동. VRoid 라운드트립 본·표정 모프 보존, char_factory .blend→.vrm humanoid 본 정상.
- **뿔/날개("최대 미검증")**: 뿔=head 본 강체 회전 추종, 날개=독립 본 flap 2 DOF, VRM export 후 커스텀 본 보존(83→85). **THA3가 깨졌던 비인간 요소가 3D 본 리깅으로 풀림.**

## 4. 결과 (Consequences)

### 4.1 라이선스 게이트 (선결, 합의 거버넌스)
상업 출력 AND-clamp에 다음을 명시 등록·검증:
- **StdGEN checkpoint = research-only** → 상업 출력 사용 시 게이트 차단(메인 제외라 영향 작으나 R&D 트랙 사용 시 필수).
- **TRELLIS rembg 기본값**(briaai/RMBG = non-commercial) → BiRefNet 패치 보존 검증.
- **VRM 메타 라이선스**(avatarPermission 등) ↔ char_factory catalog 등급 동기화(재export 시).
- char_factory VRoid 베이스 = CC0(상업 안전).

### 4.2 구현 로드맵 (별도 TDD, 본 ADR은 방향 확정)
1. 표정 wiring: char_factory Face shapekey `Fcl_*` rename + poc_vrm_drive `target_NN` → 인덱스/이름 기반.
2. 아벨린 화풍 이식: VRoid 베이스 텍스처/색에 아벨린 디자인 반영 + 뿔/날개 절차 메시 튜닝(solidify·위치).
3. 날개 부드러운 flap: segment 본 체인 + weight 그라데이션(현재는 강체 통판).
4. 말하는 아벨린 VRM e2e: voice_lab 음성 → poc_vrm_drive 구동 → 립싱크+표정+뿔/날개 모션.

### 4.3 비용/한계 (정직)
- VRM/3D는 THA3 대비 "한 단계" 무겁다(에셋 신설 3~4 작업). 보상 = 풀바디 자유·각도 회전·뿔/날개 리깅·three-vrm 웹 실시간.
- 현 PoC는 절차 메시 + VRoid 교복 베이스 = **아벨린 화풍 미완**(기술 검증만 PASS).
- char_factory는 날개급 대형 부속물의 부드러운 물리(segment 본)는 아직 미구현.
