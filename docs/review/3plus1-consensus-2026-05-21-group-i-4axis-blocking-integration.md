# 3+1 합의 보고서 — Group I 4축 BLOCKING 통합 정리 brief (DRAFT v1)

**일자**: 2026-05-21 (후속 77)
**대상**: `docs/phase0/group-i-4axis-blocking-integration-brief.md` (DRAFT v1)
**진입 단위**: Group I 구현 entry 합의(`f29c772`) 후속 #5 — 4축(credential·allow-list·anchor·audit) 단독 심화 완주 후 통합 정리 + 구현 entry 발효 readiness 검토
**합의 형태**: **풀 3+1** (Agent A 구현 / B 품질·안전성 / C 대안 + Reviewer 교차)
**판정**: **APPROVE WITH CONDITIONS** (BLOCKING 4 = IB-1~4 + 권고 6 = IR-1~6)
**합의 권위**: 추론적 검증(권고) 한정 — 수단 결정·구현 entry 발효·실 hook/CI/ruleset/credential/audit sink·sigstore·Rekor 도입·Operational Readiness PASS·brief 본문 수정·commit·push = 모두 사용자 명시 + 별도 단계. 본 보고서는 어떤 코드/설정도 변경하지 않음.

---

## 1. Reviewer 직접 재검증 결과

| 항목 | 결과 |
|----|----|
| **citation SHA 11건 실재** | `git cat-file -t`/`git log` 직접 확인 — `ead5754`/`bb661f0`/`9492193`/`f77e488`/`ae4c091`/`4c5f5f4`/`c7a103b`/`f29c772` + 답습 SHA 전부 실재. **stale 0 확정** (A "3연속 단절 유지" 채택, B CR-3 우려 *통과로 해소*) |
| **누적 39 산술** | `entry 34 → 71~72 +2 → 73 +1 → 75 +1 → 76 +1 = 39` 정확 |
| **B CR-3 "MEMORY 36 vs 34 기준점"** | **기각** — MEMORY "36"은 71~72 *이후* 누적, brief "34"는 71~72 *이전* base. 동일 시점 아님, 사슬 정합 |
| **AR-1 (BI4C-3)** | `bb661f0` BI4C-3 = 독립 BLOCKING(direct-push gate, G-BI4-6) 실재 → §7 P-2 일반 흡수 = silent 누락 표면. 권고 격상 정당 |
| **CB-1~4 / C 대안1** | brief §7/§8/§9 본문에서 전수 사실 확인 |

---

## 2. 교차 비교

| # | 항목 | A | B | C | 분류 |
|---|------|---|---|---|------|
| 1 | 판정 (발효 0건 통합 적격) | 적격 | APPROVE w/C | APPROVE w/C | **일치** |
| 2 | citation stale 0 / SHA 11건 | stale 0 | CR-3 grep 요구 | — | 부분→통과 |
| 3 | 누적 39 산술 | 정확 | 기준점 우려 | — | 부분→기각 |
| 4 | 교차 패턴 9건 가치 | 정확 | 호평 | 호평 | **일치** |
| 5 | 거짓 안전감 (§9 CP-9) | — | **CB-1 통합 고유 미차단** | 대안3 위협중심 | 부분 |
| 6 | owner self-bypass DEFER 비용 | — | **CB-2** | **대안1** | **일치(수렴)** |
| 7 | BI4C-3 direct-push gate | **AR-1** | — | — | 누락(A) |
| 8 | P-5 binary 구체화 | — | **CB-3** | — | 누락(B) |
| 9 | BI-8/BI-10 안전 구멍 + BI-9 백업키 | BI-8 분류 정확 | **CB-4** | 대안4 묶음 | 부분 |
| 10 | Sigstore 위상 (후보1 vs 구조적 대안) | CP-7 정확 | (CB-2) | **대안1** | 부분 |
| 11 | 발효 2-track (enforce 순차/observe 동시) | — | — | **대안2** | 누락(C) |
| 12 | Provider Liquidity 긴장 (Sigstore OIDC) | — | — | **PL** | 누락(C) |
| 13 | AR-2/AR-3 (anchor 행·P-2 2분) | AR-2/3 | — | — | 누락(A) |

**집계: 일치 3 / 부분 5 / 불일치 0 / 누락 5**

---

## 3. ⭐ 핵심 수렴 판정 — CB-2 ≡ C 대안1 (동일 쟁점 → 통합 BLOCKING IB-2)

세 경로가 한 지점으로 수렴:
1. **BI-5 원 합의(`f77e488`) BI5C-2(d)가 이미 명문**: "Rekor(제3자) = audit self-bypass 닫는 *유일* 구조적 후보, MVP-6 DEFER = audit self-bypass 잔여 수용 결정". 그 합의 자체가 "B(명문 누락)·C(Rekor=유일 해소·DEFER=수용 결정) 수렴" 기록.
2. **본 검토에서 B CB-2(§7 미전파·인과 격상)와 C 대안1(통합 책무·수단 융합 vs 누적)이 다시 같은 입구로 수렴** — B = 거짓 안전감/§7 readiness 각도, C = 통합 trade-off 책무 각도, 실질 동일: **"Rekor/Sigstore MVP-6 DEFER 의 비용 = owner self-bypass 의 *4축 영구 수용 결정*이 통합 readiness 에서 과소평가/미전파."**
3. CP-1(§4)·§9가 owner self-bypass 를 "MVP-6 전까지 수용"으로만 적고 *DEFER=결정 동치* 인과·비용(4축 영구 잔존)을 readiness 의사결정 위치(§7.4)·다음 단계(§10)로 끌어올리지 않음.

→ **동일 쟁점 확정, 통합 BLOCKING IB-2 격상.** BI-5 단일 축 BLOCKING 이 통합 차원 4축 전체 owner SPOF 영구 수용으로 확대.

---

## 4. 최종 판정 — APPROVE WITH CONDITIONS

### BLOCKING 4건 (IB-1~4)

| # | 조건 |
|---|----|
| **IB-1** ⭐ | §9 CP-9에 **통합/readiness *고유* 거짓 안전감 차단** — "통합·readiness 검토 자체가 발효 정당성·안전 부여 안 함, 통합 = 뷰 환원이지 SPOF 해소 아님" = entry "진입 적격≠안전 확정"의 통합 축 대칭. (§9 단순 답습 처리 불가, B CR-4) |
| **IB-2** ⭐ | (CB-2 ≡ C 대안1 *수렴* — 통합 격상) §7.4 readiness 판정 + §6 Rekor 행 + §9에 **(i) owner 경로 self-bypass 가 P-1~P-5 충족 후에도 4축 잔존**(CP-1) + **(ii) "Rekor/Sigstore MVP-6 DEFER = owner self-bypass 4축 영구 수용 *결정* 동치"**(BI5C-2 d 통합 확대) 인과를 *각주 아닌 readiness 의사결정 위치* 명문 + **CP-7을 "MVP-6 후보 1개"→"4단 누적의 *구조적 대안 경로* 1개"로 위상 격상** + "4단 누적 총비용 vs Sigstore 1회 융합" 통합 trade-off 1문단 (채택은 MVP-6+별도 entry 보류) |
| **IB-3** | §7.2 P-3 / §8에 **BI-8(silent scope expansion·observe 라벨 간극) + BI-10(`.git/` commit layer 사각 = 두 축이 범위 밖으로 밀어낸 합집합 무방비)** 안전 구멍 *발효 선결* 명문 + **BI-9 백업키 역설(기밀성 저하·공격표면 N배)**을 §6 credential 행/P-1 trade-off 병기 |
| **IB-4** | §7.2 P-5 binary PoC를 **각 축 binary 종료조건 매핑**(BI1C-1 미서명 reject=ruleset+CI 결합 / BI-5 §10 / BI4C-2 anchor binary) — "PoC 실시"가 무엇 입증하는지 명시 = CP-2 라벨화 재발 차단 |

### 권고 6건 (IR-1~6)

| # | 권고 |
|---|----|
| **IR-1** (AR-1) | §7 P-list에 BI4C-3 direct-push gate(restrict-direct-push/PR-required + G-BI4-6) anchor 발효 독립 선결 격상 |
| **IR-2** (AR-2) | §6 anchor 행에 restrict-direct-push 전제 병기 |
| **IR-3** (AR-3) | §7.2 P-2를 "brief 본문 반영분 / 미반영분(CD-4/CD-9/BI5C-3 등)" 2분 |
| **IR-4** (C 대안2) | §7 발효 경로 = **enforce 순차 + observe 4축 동시 조기 발효 2-track** 분리 (BI-7 면책 라벨 동반 필수, 부분 격리 그라데이션 거짓안전감 위험 명문; audit-first enforce 비권고=CT-4 재귀 credential 의존) |
| **IR-5** (C PL) | §6에 Sigstore(CP-7)↔CP-6 2층 중립 Provider Liquidity 긴장("투명성 로그 필요 ≠ Rekor여야 함", OIDC=새 단일 벤더 신뢰 축) + 다중 vendor 미러(BI5C-4) PL-안전 대안 1급 병치 |
| **IR-6** (CR-1/CR-2) | §6 anchor 층1 "(서명 존재+fingerprint)"에서 fingerprint=allow-list 몫 분리(CP-5 정합) + BI1C-2/3(observe FN·Rollback owner 미전파) §4 표/§8 교훈 승격(line 104 각주 매몰) |

### 거짓 안전감 차단 (핵심 평가)
**IB-1이 핵심** — 통합 brief 고유 위험 = *완결감*("4축·교차 9건·readiness 다 봤으니 발효 OK"). §9 CP-9의 *수단 차원* 명문만으로 *통합/검토 행위 차원* 미끄럼 못 막음. **B/C의 owner self-bypass DEFER 비용 수렴(IB-2)이 거짓 안전감의 가장 구조적 발현** — "owner 경로는 4축 어디서도 안 닫히고 MVP-6까지 영구 수용"이 readiness 의사결정 위치에 없으면 "수용된 SPOF 위 최선"을 각주로 강등.

---

## 5. 종합 결론

본 통합 brief는 발효 0건 정리 문서로서 구조 견고하고 citation 11건 실재·누적 39 산술·§2~§5 정합·교차 패턴 9건 추출이 직접 재검증을 통과한 양질의 통합 산출이며(Agent B의 CR-3 SHA grep 우려와 "36 vs 34 기준점" 우려는 재검증 결과 각각 *통과*·*기각*), APPROVE WITH CONDITIONS가 타당하다. 가장 무게 있는 조건 둘: 첫째 이 문서의 *고유* 위험 = 4축을 한 뷰로 모은 데서 오는 *완결감(통합 차원 거짓 안전감)* 이므로 "통합·readiness 검토 자체가 발효 정당성을 부여하지 않는다"는 entry 원칙의 통합 축 대칭을 §9에 명문(IB-1); 둘째 **Agent B(CB-2, §7 미전파/거짓 안전감)와 Agent C(대안1, 통합 책무/수단 융합 vs 누적)가 동일 쟁점에 수렴 — "Rekor/Sigstore MVP-6 DEFER 의 비용 = owner self-bypass 의 4축 영구 수용 결정"이 통합 readiness 의사결정 위치에서 과소평가/미전파됨을 지적하며, BI-5 단일 축 BLOCKING(BI5C-2 d)이 통합 차원 4축 전체로 확대된 것이므로 통합 BLOCKING(IB-2)으로 격상하고 CP-7 위상을 "구조적 대안 경로"로 끌어올려야 한다.** BI-8/BI-10 안전 구멍·BI-9 백업키 trade-off 발효 선결(IB-3)과 P-5 binary 축별 매핑(IB-4)을 더해 BLOCKING 4건·권고 6건. 본 합의는 추론적 검증(권고) 한정이며 수단 결정·구현 entry 발효·실 구현·sigstore·Rekor 도입·commit·push는 모두 사용자 명시 + 별도 단계(풀 3+1, R-I-IMPL-BOUNDARY)의 권한이다.

---

## 부록 — Agent 관점 요약

| Agent | 관점 | 핵심 |
|------|------|------|
| **A** (구현) | "동작하는가?" | citation SHA 11건 전수 grep = stale 0(3연속 단절 유지). 누적 39·§2~5 정합. BLOCKING 0, 권고 AR-1(BI4C-3 P-list 격상)·AR-2·AR-3 |
| **B** (안전성) | "견고한가?" | **CB-1 통합 고유 거짓 안전감 / CB-2 owner self-bypass §7 미전파+Rekor DEFER=영구 수용 인과 / CB-3 P-5 binary 희석 / CB-4 BI-8·BI-10 안전 구멍** |
| **C** (대안) | "더 나은 방법?" | **대안1 CP-7 위상(수단 융합 vs 누적 trade-off 미수행) / 대안2 2-track / 대안3 위협중심 재구성 / Sigstore↔PL 긴장** |
| **Reviewer** | "최선 합의?" | 직접 grep 재검증(SHA 11건·산술 39·B 우려 기각·CB-2≡C대안1 수렴 확정) → APPROVE WITH CONDITIONS, BLOCKING 4 + 권고 6 |
