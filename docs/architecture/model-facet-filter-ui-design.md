# 모델 패싯 필터 UI 설계 (Model Facet Filter UI)

> prompt_lab 웹 페이지(text→image, 포트 8780)의 베이스 모델 선택 편의성 개선.
> 작성: 2026-06-20 · 상태: DESIGN (사용자 mockup 컨펌 완료 → TDD 구현)

---

## 1. 문제 (Problem)

현재 `prompt_lab/static/index.html` 의 베이스 모델 선택은 **평면 `<select>` 하나**에
모든 이미지 모델을 나열하고, 비상업 모델은 `(비상업)` 접미사만 붙는다. 별도로
`☐ 상업화 등급 요구` 체크박스가 있다. 모델이 늘면서(animagine·illustrious·realvisxl·
noobai·novelai·qwen·nano-banana …) **용도(애니 일러스트 vs 실사)·라이선스(상업 vs 개인)로
좁히는 수단이 없어** 사용자가 매번 전체 목록을 훑어야 한다.

## 2. 목표 (Goal)

모델 select 위에 **패싯 칩 한 줄**을 두어, 토글로 목록을 좁힌다. 사용자 표현
"상업/비상업/실사/이미지" 를 그대로 수용한다.

- **용도**: `🎨 일러스트` / `📷 실사` (registry `category` = `anime` / `realistic`)
- **라이선스**: `💼 상업용` / `🔒 개인용` (registry `commercial` = true / false)

## 3. 핵심 설계 결정 (Decisions)

| # | 결정 | 근거 |
|---|------|------|
| D-1 | 안 맞는 모델은 **숨김**(목록에서 제거), 회색 비활성 아님 | 사용자 mockup 컨펌. 목록이 짧고 깔끔 |
| D-2 | **체크박스 → `💼 상업용` 패싯으로 통합**. 별도 체크박스 제거 | `☐ 상업화 등급 요구`는 단순 필터가 아니라 백엔드 게이트(`commercial_mode` → LicenseError). 패싯이 (a)상업 모델만 표시 + (b)`commercial_mode=true` 전송을 동시에 표현 → 의미 일관·혼란 제거 |
| D-3 | **3D 모달리티는 패싯에서 제외**. 이미지 모델(`modality==="image"`)만 | 결과 카드 `renderResult()` 가 `<img>` 만 렌더 → glb 는 깨진 경로. 3D는 별도 페이지가 맞음 |
| D-4 | 백엔드(gen_gate·webapp.py) **변경 0** | `/api/models` 가 이미 `{key, modality, category, commercial, license}` 전부 노출 → 필터는 순수 클라이언트 |
| D-5 | 용도 칩 = **독립 토글**(애니+실사 동시 가능, 둘 다/0개 = 전체). 라이선스 칩 = **상호 배타**(상업 켜면 개인 꺼짐) | 라이선스는 상업·개인 동시 요구가 모순. 용도는 둘 다 보고 싶을 수 있음 |
| D-6 | **LoRA(캐릭터) 잠금 우선**: 캐릭터 선택으로 model 이 disabled 면 패싯이 선택을 바꾸지 않음 | 기존 베이스 잠금(`loraBase`) 규약 보존 |

## 4. 필터 로직 (순수 함수)

```
filterModels(allImageModels, facets) =
  allImageModels.filter(m =>
       (facets.usage.size === 0 || facets.usage.has(m.category))
    && (facets.license === null || m.commercial === (facets.license === "commercial"))
  )
```

- `facets.usage` : Set ⊆ {"anime","realistic"}
- `facets.license` : "commercial" | "personal" | null
- `commercialMode()` (생성 페이로드) = `facets.license === "commercial"`

## 5. UI 변경 (index.html 단독)

1. 모델 `row` 위에 **패싯 row** 추가 (`.facet-chip` — 기존 `.gal-tab` 토글 스타일 재사용).
2. `fillSelect("/api/models", …)` 의 하드코딩 `if (m.modality !== "image") return;` 제거 →
   `allModels` 캐시 + `renderModels()` 로 분리. 패싯 토글 시 재렌더.
3. `renderModels()`: 현재 선택이 필터 통과하면 유지, 아니면 첫 유효 항목(없으면 안내)로 폴백.
   model 이 disabled(LoRA 잠금)면 재필터 스킵.
4. `☐ 상업화 등급 요구` 체크박스 제거 → `$("commercial").checked` 사용처(생성·보관함 저장)를
   `commercialMode()` 로 치환.

## 6. 검증 (Verification)

- **계산적**: `filterModels` 를 순수 함수로 분리. (현재 페이지에 JS 테스트 러너 없음 → JS 단위
  테스트는 미도입. 백엔드 무변경이므로 기존 pytest 그린 유지로 회귀 방지.)
- **추론적/시각적**: 비주얼 반복 규율 — 한 패싯씩 토글하며 전/후로 목록 변화 확인
  (전체 → 실사만 → 상업+실사 → LoRA 잠금 시 패싯 무효).

## 7. 비범위 / 후속 (Out of scope)

- 3D 모델 선택(별도 페이지 필요). 모델별 LoRA 자동 매칭.
- 데이터 정정(후속): `anima-base-v1` 이 `commercial:true` 인데 license=`circlestone-non-commercial`
  → 불일치. 이번 범위 밖, 별도 정정 제안.
