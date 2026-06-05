# 3+1 합의 보고서 — 제어측 C-3 자율완화

> **일자**: 2026-06-05 · **브랜치**: `feature/control-c3-autorelax`
> **대상 brief**: `docs/phase0/jarvis-control-c3-relaxation-brief.md`
> **판정**: **REVISE (조건부)** — rate 축 깨끗이 수렴(APPROVE), 누적 축은 적대적 검증으로 후보 좁힘 + BLOCKING 5개
> **프로토콜**: CLAUDE.md §3 (보안 관련 변경 = 3+1 필수). Agent A(구현)·B(품질/안전)·C(대안) 병렬 독립 → Reviewer 교차 비교.

---

## 판정: REVISE (조건부)

C-3 = 보안 게이트 → 보수 우선. **rate 축**은 3개 수렴해 그대로 채택. **누적 축**은 적대적 검증에서 드러난 결함(2-B가 CB-2 깸) + 누락(windowed 우회 표면 3개) 때문에 무조건 채택 불가 → 후보 2개로 좁히고 값은 사용자 회부.

---

## ① 일치 (Consensus)

- **rate 후보 = R-b(5/60s)** — A·B·C 3개 수렴. R-a(현 유지)·R-c(10/60s) 기각.
- **R-a 기각 근거** = F-1 실측(M2: 단일 3-op `start→restart→restart`이 op#3에서 referred) → 정상 작업 봉쇄 입증.
- **L-5 2축 비협상 보존** — 3개 모두 rate 단독(C-c) 기각, 누적 축 유지.
- **경계 로직 불변** — 임계 *값/형태* 한정, 소유/회부 경계(M4·M5 실증) 코드 0줄. over-claim 없음(M1 정직단서 모범).

## ② 부분일치 (Partial)

- **rate 윈도가 잡는 것** = "*executed* 빈도"이지 crash-loop 자체 아님(`_rate_record`는 executed 시에만, `process_control.py:393`). A·B 명시, C는 이를 근거로 2-B 주장. **사실 인식 3개 일치, 처방 갈림.**
- **누적 미봉책 인식** — A(C-a)도 "lifetime 의미론 → 언젠가 봉쇄, 미봉책"임을 자인하되 "100 cap 헤드룸 충분 → 실 trigger 미도달"로 정당화. B·C는 더 무겁게 봄.

## ③ 불일치 (Divergence) — 누적 축 3-way

| | Agent A | Agent B | Agent C |
|--|---------|---------|---------|
| 처방 | C-a (10→100) | C-b windowed (+안전조건) | **2-B 재정의**(반복실패 탐지) |
| F-2 해소 | 헤드룸 회피(미도달) | 시간창 | 구조적 소멸 |
| 비용 | 1줄, 테스트 0 | seam+2테스트+O(n)+시계방어 | 의미론 재설계 |
| 리스크 | 미봉책 잔존 | 새 우회표면 3개 | **CB-2 깨짐(적대적 검증)** |

## ④ 누락 (Gap)

- **(B만) C-b 새 우회 표면 3개**: (가) 시계 후퇴 시 누적 리셋 — brief §5(b)가 재시작만 잡고 **시계 후퇴 누락(실 GAP)**, (나) fixed-window 경계 burst(슬라이딩 강제 필요), (다) ts 무결성.
- **(C만) §4 1-클릭 override**: referred를 값 변경 없이 1클릭 승인 흡수 = 보안표면 0(평가 가치, 단 게이트 의미 약화 우려).
- **(C만) 거버넌스**: 적응형/per-target/모드별 = ADR-011 T1/T2/T3(자동학습≠자동정책변경) 위반 → DEFER.
- **(A만) C-b 구현비용 정량화**: tz-aware 비교 TypeError·now 주입 seam이 기존 테스트 영향.

---

## ⭐ 적대적 검증 — 2-B(crash-loop 재정의)가 CB-2를 깨는가: **그렇다. 대체로는 BLOCKING 결함.**

**CB-2 불변(코드+slice-1b 합의 line 63 확정)**: rate는 in-memory(`_rate`, `process_control.py:316`)라 controller 재시작 시 리셋. 합의는 이를 *허용*했고 그 **유일 근거** = "누적 축이 ledger 파생으로 *성공한 executed op의 총량*을 계속 세므로, 재시작으로 rate를 리셋해도 무제한 성공 spawn은 불가". **rate의 in-memory 약점을 누적의 ledger-executed-카운트가 backstop**하는 구조.

**2-B 적용 시**: 누적 축이 "성공 op count" → "반복 *실패* spawn 탐지"로 바뀌면 **executed(성공)는 누적 축 관심 밖**. 공격자/폭주 boss가 controller 재시작 → `_rate={}` 리셋 → rate_limit만큼 *성공* op 실행 → 재시작 → 반복. **막는 축 없음**: rate=재시작마다 리셋, 누적(2-B)=성공 op 안 셈, CB-9 동시1=*순차* 재기동 연타(stop→start 반복) 못 막음.

**결론**: 2-B는 "재시작으로 rate 우회 → 무제한 성공 lifecycle" 경로를 **재개방**. CB-2가 닫으려던 바로 그 구멍. C의 "2축 보존"은 *축 개수*만 보존하고 **각 축이 막는 위협을 바꿔** 둘 다 restart-bypass를 안 막는다. C 스스로 "2-A(rate ledger 영속화)가 재시작우회를 흡수하나 L-5로 기각"이라 한 것은 **재시작우회 방어가 원래 누적 축 역할임을 자인**.

**단, 2-B의 통찰은 유효** — rate가 crash-loop를 *직접* 못 잡는다는 지적은 정확. → 2-B는 **누적 축 *대체* = REJECT**, **추가 센서(후속 백로그) = 유효**.

---

## 합의 BLOCKING (CC-1 ~ CC-5)

- **CC-1 (CB-2 기능 보존 — 최상위)**: 어떤 누적 축 형태든 "controller 재시작으로 rate 리셋해도 무제한 *성공* lifecycle 불가"를 보존. 누적 축 = **ledger 파생 + executed(성공) op 카운트 포함**. → **2-B를 누적 축 *대체*로 채택 금지.**
- **CC-2 (L-5 2축 검사 불변)**: 완화 후에도 rate **또는** 누적 어느 한 축 초과 = referred. 단독 판정 금지.
- **CC-3 (경계 로직 불변 + 회귀테스트)**: 소유/회부 경계(L-2/CB-1/CB-9, M4·M5)는 값 변경이 안 건드림을 회귀테스트로 고정.
- **CC-4 (windowed 채택 *시에만* 발효)**: C-b 택할 경우 (가) 시계 후퇴 방어, (나) 슬라이딩(fixed-window 금지), (다) ts 무결성 — B 발견 GAP 3개 모두 BLOCKING. Rollback Trigger에 "시계 후퇴 후 누적 리셋 재현 = 중단" 추가.
- **CC-5 (rate 의미론 명시)**: rate = *executed* 빈도이며 propose 폭주 1차 방어 = 1-클릭 게이트(C-2)임을 코드 주석/문서에 명시. rate가 crash-loop를 직접 안 잡음을 정직 단서로 기록.

---

## 축별 합의

**rate 축**: ✅ **R-b(5/60s) 후보 수렴, APPROVE.** R-c 기각(보수 마진↓·폭주 둔감). Rollback (a)가 안전망. **값(5) 확정 = 사용자.**

**누적 축**: ⚠️ **2-B 대체 REJECT, 후보 2개로 좁힘 — C-a 권고 / C-b 후속.**
- 남은 후보: **C-a(값↑ lifetime executed) vs C-b(windowed executed +CC-4)**. 둘 다 CC-1 충족.
- **Reviewer 권고 = C-a 먼저(비례성)**: 개인 로컬 툴 비례성. F-2는 현재 *잠재적 미봉책*이지 실 봉쇄 아님(A 실측: 100 cap ≫ voice_lab 1일 ~10 restart). windowed 선제 재설계 = trigger 없는 과설계 경향 + 우회 표면 3개를 *지금* 떠안음.
- **C-a 한계 정직 단서**(B·C 정당): lifetime 의미론은 언젠가 봉쇄 → "값↑는 미봉책, windowed는 실 봉쇄 재현(Rollback 신규 trigger) 시 진입할 설계된 후속". **값(100) 확정 = 사용자.**

**1-클릭 override(C §4)**: **별도 슬라이스로 분리.** 본 완화(임계 값/형태)와 범위 다름(referred 처리 UX) + "referred를 1클릭 통과"가 2축 게이트 의미를 약화시킬 수 있어 독립 검토 필요. 후속 brief 권장.

---

## 사용자 회부 사항

1. **rate 값 확정** — R-b 후보(5/60s). Reviewer는 R-b로 좁힘, 숫자는 사용자.
2. **누적 형태 선택** — C-a(권고, 값↑ lifetime executed) vs C-b(windowed, CC-4 비용). Reviewer 권고 = C-a 먼저.
3. **누적 값 확정** — C-a 채택 시 cap(예: 100).
4. **1-클릭 override 분리 승인** — 별도 슬라이스 후속 진행 여부.
5. **2-B(crash-loop 탐지) 추가 센서 백로그 등록** — 대체 REJECT지만 탐지 아이디어 유효.

---

## 다음 단계 (TDD — 값 확정 후, 자동 진입 0)

1. **RED**: (a) 완화 rate 경계(R-b N+1 referred), (b) 폭주 차단 유지, (c) 누적 경계(cap+1 referred) + **CC-1 회귀(재시작 시뮬 `_rate={}` 리셋 후에도 ledger executed 누적 차단 유지** = 적대적 검증의 코드화), (d) 경계 불변 회귀(CC-3: M4 동시1·M5 미소유 stop 여전히 referred), (e) C-b 채택 시에만 시계후퇴/슬라이딩/ts(CC-4).
2. **GREEN**: `ProcessController` 생성자 기본값 조정(명시 인자 전달로 기존 43 tests 무파손). server.py 배선 값 동기화(명시 인자화).
3. **REFACTOR**: CC-5 주석.
4. 범위 = **임계 값/형태 한정, 경계 로직 0줄.** 1-클릭 override 제외(별도).
