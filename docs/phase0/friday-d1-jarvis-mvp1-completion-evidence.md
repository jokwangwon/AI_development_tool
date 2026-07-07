# 프라이데이 D-1 — 자비스 MVP-1 완료 evidence 고정 (재베이스라인)

**일자**: 2026-07-07
**유형**: D-1 선행 작업 (경량 evidence 고정 — 진입 brief §15.2 D-1 결정 답습)
**목적**: 프라이데이 진입 stage gate("자비스 MVP-1 단계 완료")의 실증 없는 통과 =
PASS over-claim 패턴 방지. 진입 brief §5.1 체크리스트(2026-05-27 작성)를 현행 실태로
재베이스라인하고 1줄 evidence 로 고정.

---

## 1줄 evidence

> **자비스 MVP-1 완료 = MVP-1 Implementation Evidence PASS 발효(commit `adc7eb3`, 합의 `6973935`)가 이미 성립했고, 이후 MVP-2 Implementation Evidence PASS 발효(`bceb535`, 2026-05-28, 풀 3+1 + codex APPROVE WITH CONDITIONS 흡수)로 supersede 되었으며, 2026-07-07 현행 전체 suite green(789 passed, 2 skipped, 0 failed) 실측으로 회귀 0 확인.**

## §5.1 체크리스트 재베이스라인 (2026-05-27 → 2026-07-07 실태)

| 항목 (원문) | 현행 실태 | 판정 |
|---|---|---|
| (b1-AR3 첫 PR evidence) 첫 PR open + workflow PASS | PR #2 merged (`eb51284`, "MVP-1 1.5차 보강 (b1) 4 sub-cycle + AR-3 branch protection evidence"). 이후 PR #55(반영 루프)·#56~58 등 다수 merged | ✅ |
| (b1-AR3 develop branch protection 적용) | ⚠️ **구조적 불가** — private repo + GitHub free plan 은 branch protection 미지원 (API 403 실측, 2026-07-07). workflow 규율(feature→develop PR)로 대체 운영 중. **미충족이 아니라 플랫폼 제약** — 정직 기록 | ⚠️ N/A (플랫폼 제약) |
| (c) MVP-1 Implementation Evidence PASS 발효 합의 | 발효 완료 (`adc7eb3` CONTEXT 기록 + `6973935` 합의 기록) | ✅ |
| Layer 2 발효 결정 | MVP-2 에서 Layer 1+2+4 통합 PASS (`0f49eb9`) 로 흡수 발효 | ✅ |
| (b2) R-S1 권위 chain 정정 | `bb59342` (MVP-2 발효 brief 가 "61 R-S1 정정" 으로 인용) | ✅ |
| (b3) framing 정정 | `mvp1-r-s1-b2-others-correction-evidence.md` + `mvp1-r4-framing-evidence-entry-brief.md` | ✅ |
| 자비스 test suite green ("144/144" → 재베이스라인) | **789 passed, 2 skipped, 0 failed** (2026-07-07 실측, `pytest tests/`) — "144" 숫자 고정은 진입 brief 에서 이미 폐기 | ✅ |

## 실측 주석 (환경 아티팩트 기록)

- 1차 풀 스위트 실행에서 `test_devnull_rw_restores_execution` 1건 실패 → 조사 결과 **코드 회귀 아님**: VS Code 가 `.venv/bin` 을 PATH 선두에 주입 → Landlock 샌드박스 안 `python3` 가 venv 로 해석 → `pyvenv.cfg` 읽기 거부(Errno 13). clean PATH(`/usr/local/bin:/usr/bin:/bin`) 재실행 시 해당 파일 14/14 + 전체 789/789 green.
- 교훈: **Landlock 관련 테스트의 evidence 실행은 clean PATH 를 기본으로** (venv 활성 셸에서 subprocess `python3` 해석 오염).

## 결론

**D-1 stage gate 충족 — 프라이데이 MVP-0 설계 진입 자격 발효.**
(carry-over 중 develop branch protection 1건 = 플랫폼 제약으로 N/A 처리, 나머지 전부 실증.)
