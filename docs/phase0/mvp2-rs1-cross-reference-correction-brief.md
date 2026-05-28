# R-S1 cross-reference 정정 entry brief (v1)

> **작성**: 2026-05-28 (61번째 entry 진입 cycle — 신규 세션 #2)
>
> **scope**: ADR-012 *자체 내부* §2.3 (4-layer) vs §2.8 (5-layer) layer numbering divergence (R-S1) 정정 — MVP-2 Implementation Evidence PASS *전* hard gate
>
> **본 cycle = 권위 chain 정정 cycle** (ADR-012 본문 cross-reference note 추가 — 전면 재번호 0)
>
> **본 cycle 발효 효과** = R-S1 해소 → MVP-2 Implementation Evidence PASS 발효 hard gate 1건 해소
>
> **선행 답습**: 52/53 entry R-S1 5 source verify CONFIRMED + 55/59 RT-γ-6 (MVP-2 PASS 전 hard gate, 3 옵션) + 60 GP-2 detection-layer PASS

---

## §0 본 brief 의 범위

### §0.1 본 brief 가 *하는* 것

1. **R-S1 divergence 정확 정의** (§2.3 4-layer vs §2.8 5-layer, 두 분해 비교) (§1)
2. **3 옵션 비교 + 권고** (§2.3 재번호 / §2.8 강화 / 권위 선언) (§2)
3. **권고 = 옵션 3 (권위 선언) — cross-reference note 추가 (전면 재번호 0)** + 정확한 제안 편집 (§3)
4. 합의 형태 + 금지 + 다음 단계 + 자기진단 (§4~§7)

### §0.2 본 brief 가 *하지 않는* 것

| # | 영역 | 위반 |
|---|------|----|
| 1 | R-S1 정정 *발효* 자체 (본 brief = 합의 입력, 정정 = 합의 + 사용자 명시 후) | 0 |
| 2 | §2.3 / §2.8 layer 정의 *내용* 변경 (cross-reference note 추가 한정) | 0 |
| 3 | §2.3 전면 재번호 (4→5 layer 재작성) | 0 (옵션 1 비채택) |
| 4 | G4 §4.4.1 (provider-agnostic-memory-skill-design) 본문 변경 | 0 (PRIMARY 답습) |
| 5 | MVP-2 Implementation Evidence PASS 발효 | 0 (별도 cycle, R-S1 해소 후) |
| 6 | Layer 통합 PASS / GP-2 PASS 재선언 | 0 (59/60 답습) |
| 7 | 다른 ADR / 헌법 / roadmap 본문 변경 | 0 |
| 8 | 자동 후속 (MVP-2 PASS) 진입 | 0 (사용자 명시) |

### §0.3 권위 답습 source

- **ADR-012 §2.3 (line 163~185, Append-only 원칙 + Hash Chain 다층 강제, 4-layer) + §2.8 (line 264~272, Full Rewrite 방어, 5-layer)** — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- **provider-agnostic-memory-skill-design.md §4.4.1** (Layer 1~5 PRIMARY, 5-layer) — `docs/architecture/`
- **52/53 entry R-S1 5 source verify** — `docs/review/3plus1-consensus-2026-05-28-mvp2-entry.md` + `-mvp2-gamma.md`
- **55/59 RT-γ-6** (MVP-2 PASS 전 hard gate, 3 옵션) — `docs/phase0/mvp2-layer-124-pass-{entry,activation}-brief.md`

---

## §1 R-S1 divergence 정확 정의

### §1.1 두 분해 비교 (직접 read)

| | §2.3 "Append-only 원칙 + Hash Chain (다층 강제)" | §2.8 "Full Rewrite 방어 (다층)" | G4 §4.4.1 (PRIMARY) |
|---|---|---|---|
| Layer 1 | Hash Chain | Hash chain | Hash chain |
| Layer 2 | Git append-only branch (**denyNonFastForwards + branch protection + pre-commit hook + CI 회귀 검증** = 하위 항목) | Git append-only + denyNonFastForwards | Git append-only |
| Layer 3 | **Signed commit** | **pre-commit hook** | (5-layer 동형) |
| Layer 4 | **External anchor** | **CI 회귀 검증** | **CI 회귀 검증** |
| Layer 5 | (없음 — 4-layer) | **External anchor** | **External anchor** |

### §1.2 모순의 본질

- §2.3 = **4-layer 분해** (pre-commit hook + CI 회귀 검증 = Layer 2 *하위 항목*, Signed commit = Layer 3, External anchor = Layer 4)
- §2.8 = **5-layer 분해** (pre-commit hook = Layer 3, CI 회귀 검증 = Layer 4 별도 승격, External anchor = Layer 5)
- ⚠️ **"Layer 4" 의미 충돌**: §2.3 Layer 4 = External anchor / §2.8 Layer 4 = CI 회귀 검증
- **MVP-2 작업 전체 = 5-layer 기준** ("Layer 1+2+4" = hash + append-only + **CI 회귀 검증**, 59 Layer 통합 PASS). §2.3 4-layer 로 읽으면 "Layer 4 = External anchor" → MVP-2 가 External anchor PASS 한 것으로 오독 risk.

### §1.3 두 섹션 모두 *내용* 은 valid

- §2.3 = "원칙 + grouping view" (CI/pre-commit 을 Git append-only 의 enforcement 수단으로 묶음). 내용 정확.
- §2.8 = "per-layer 분해 view" (각 방어를 독립 layer 로). 내용 정확.
- → **충돌 = numbering 만, 내용 0**. 어느 쪽도 틀리지 않음 → 전면 재번호 불필요.

---

## §2 3 옵션 비교 + 권고

| 옵션 | 내용 | 장점 | 단점 | 권고 |
|------|----|----|----|----|
| **옵션 1** §2.3 전면 재번호 (4→5 layer) | §2.3 을 §2.8 동형으로 재작성 | 단일 numbering | §2.3 "원칙 grouping view" + Signed commit (L3) 손실 / ADR 본문 대규모 변경 (T3) | ❌ 비권고 (내용 손실 + 과잉) |
| **옵션 2** §2.8 강화 | §2.8 에 "canonical numbering" 명시 | 가벼움 | §2.3 측 오독 risk 잔존 (§2.3 에 단서 0) | ⚠️ 부분 |
| **옵션 3** 권위 선언 (cross-reference note) | §2.3 + §2.8 양쪽에 "§2.8 / G4 §4.4.1 5-layer = canonical per-layer numbering, §2.3 = 원칙 grouping view" cross-reference note 추가 | 모순 해소 + 내용 보존 + 비례 (note 한정) | (없음) | **✅ 본 brief 권고** |

→ **권고 = 옵션 3** (cross-reference note 추가, 전면 재번호 0, 내용 변경 0). 두 섹션 모두 valid 함을 명시 + cross-document "Layer N" 참조 = §2.8/G4 §4.4.1 5-layer canonical 선언.

---

## §3 정확한 제안 편집 (옵션 3)

### §3.1 §2.3 에 추가할 cross-reference note (Layer 정의 직후)

> **Layer numbering 주의 (R-S1, cross-reference)**: 본 §2.3 = *원칙 + grouping view* (pre-commit hook + CI 회귀 검증 = Layer 2 Git append-only enforcement 하위 수단). **cross-document "Layer N" 참조의 canonical per-layer numbering = §2.8 / `provider-agnostic-memory-skill-design.md §4.4.1` 5-layer** (pre-commit = Layer 3, CI 회귀 검증 = Layer 4, External anchor = Layer 5). 본 §2.3 의 "Layer 4 = External anchor" 는 4-layer grouping view 내부 한정 — MVP-2 "Layer 1+2+4" 등 cross-document 참조는 5-layer (Layer 4 = CI 회귀 검증) 기준.

### §3.2 §2.8 에 추가할 cross-reference note (5 Layer 강제 직후)

> **canonical numbering (R-S1, cross-reference)**: 본 §2.8 5-layer = `provider-agnostic-memory-skill-design.md §4.4.1` (PRIMARY) 동형 — cross-document "Layer N" 참조 canonical. §2.3 4-layer = 원칙 grouping view (CI/pre-commit = Layer 2 하위), numbering 충돌 아닌 분해 관점 차이.

### §3.3 편집 영역

- `docs/decisions/ADR-012-evidence-ledger-protection.md` §2.3 + §2.8 = cross-reference note 2개 추가 (layer 정의 내용 변경 0)
- G4 §4.4.1 (provider-agnostic-memory-skill-design) = 변경 0 (PRIMARY 답습)
- 단일 atomic commit

---

## §4 합의 형태

### §4.1 권고 = 풀 3+1 (또는 Reviewer-only 단축)

- R-S1 = 52/53 entry 5 source verify CONFIRMED + 55/59 hard gate (4+ entry 답습) → 권위 영역
- 단 본 정정 = cross-reference note 추가 (내용 변경 0, 전면 재번호 0) → 작은 영역
- **본 brief 권고**: 풀 3+1 (ADR 본문 cross-reference + 권위 chain 영역) — 단 사용자가 Reviewer-only 단축 선택 가능 (note 한정, 내용 0)
- 외부 LLM = 사용자 영역 (R-S1 5 source 이미 CONFIRMED, 추가 cross-vendor 선택)

### §4.2 7 승격 트리거

| # | trigger | 발화 |
|---|---------|----|
| 1 | 큰 결정 (수단 결정 / threshold) | ❌ (numbering 정정) |
| 2 | 아키텍처/SDD 본문 변경 | ⚠️ 부분 (cross-reference note, 내용 0) |
| 3 | **ADR 본문 변경** | ✅ **발화** (§2.3 + §2.8 note 추가) |
| 4 | 권위 chain 다중 source 손상 | ✅ **발화** (R-S1 자체) |
| 5 | 외부 LLM 통합 필요 | ❌ (5 source 이미 CONFIRMED) |
| 6 | Tier-2/3 확장 | ❌ |
| 7 | Hermes PMO 격상 | ❌ |

→ **2 발화 + 1 부분 → 풀 3+1 적격** (ADR 본문 + 권위 chain). 단 정정 규모 작음 → Reviewer-only 단축도 정당 (사용자 영역).

---

## §5 금지 사항

§0.2 답습 (8). 추가: §2.3/§2.8 layer 정의 *내용* 변경 0 / 전면 재번호 0 / G4 §4.4.1 변경 0 / MVP-2 PASS 자동 발효 0 / 자동 후속 0.

---

## §6 다음 단계 (사용자 명시 의무)

1. 본 brief 승인 → 합의 (풀 3+1 또는 Reviewer-only, 사용자 선택) → R-S1 정정 commit (§2.3 + §2.8 cross-reference note) + push → **R-S1 해소**
2. **MVP-2 Implementation Evidence PASS 발효 합의** (Layer 통합 PASS ✅ + GP-2 detection-layer PASS ✅ + R-S1 ✅ → MVP-2 최종 milestone, full GP-2 prevention scope 결정)

---

## §7 cross-reference + 자기진단

### §7.1 cross-reference

- ADR-012 §2.3 + §2.8 — `docs/decisions/ADR-012-evidence-ledger-protection.md`
- provider-agnostic-memory-skill-design.md §4.4.1 (PRIMARY)
- 52/53 R-S1 5 source verify + 55/59 RT-γ-6

### §7.2 자기진단

| # | 위험 | 처리 |
|---|------|----|
| P-1 | 옵션 3 (note) 가 모순을 *덮기* 만 하고 해소 안 함 | §1.3 = 두 섹션 내용 valid (충돌 = numbering 만) → note 로 canonical 선언 = 정당 해소 (전면 재번호 = 내용 손실 risk) |
| P-2 | "canonical = 5-layer" 결정이 §2.3 권위 폄하 | §3.1 note = §2.3 "원칙 grouping view" 정당성 보존 + cross-document 참조만 5-layer |
| P-3 | ADR 본문 변경 (T3) 과잉 | cross-reference note 한정 (내용 0), 전면 재번호 0 — 비례 |
| P-4 | 본 brief 작성자 = MVP-2 chain 작성자 (Claude) cascade | R-S1 = 52/53 5 source 이미 CONFIRMED (독립 verify), 본 정정 = 그 결론 답습 |

---

**본 brief v1 끝.**

**다음 단계**: 사용자 승인 (+ 합의 형태 선택) → 합의 → R-S1 정정 commit + push → R-S1 해소 → MVP-2 PASS 발효 합의.
