# 설계 brief — jarvis 플러그인 아키텍처 + 산출물 반영 통합 (#UI-1~4 통합)

> **상태**: v2 (3+1 합의 REVISE 반영, 사용자 검토 대기) · **출처**: 119 세션 dogfooding #UI-1~4 + 확장 지속가능성
> **합의**: `docs/review/3plus1-consensus-2026-06-01-jarvis-plugin-architecture.md` (REVISE — BLOCKING 4 + 정식 인터페이스 확정)
> **상위**: `jarvis-conversation-task-routing-design-brief.md`(#UI-1 라우팅, 구현됨) 흡수
> **핵심 명제**: **플러그인 아키텍처 = #UI-4 산출물 반영의 안전한 답 + 자비스 확장 지속가능성**
> **첫 사례**: TTS 음성 비교 분석 페이지. **다음 단계**: v2 검토 → TDD (자동 진입 0)

---

## 0. v1 → v2 변경 (3+1 합의 반영)

| 항목 | v1 | v2 (REVISE) | 출처 |
|---|---|---|---|
| 추상 수준 | 정식 인터페이스(메타 3요소) | **정식 인터페이스 확정** — 사용자 로드맵 "여러 개 확장 확정" | §D 사용자 결정 |
| 메타 형식(갈림길3) | 미정 | **데이터 manifest(폴더 스캔) + 명시 사람 등록 분리** | C-4 BLOCKING |
| B복사 게이트 | 게이트 존재처럼 서술(over-claim) | **미구현 → 본 설계가 신규 정의** 명시 | R3 §7 |
| "등록 1줄" | 코어 1줄 주장 | **데이터 레지스트리 전제** 정정(현재 server.py 2곳 편집) | R3 §7 |
| 경로 표기 | `hud/plugins/` | **`jarvis_hud/plugins/`** 정정 | A 경로보정 |
| 탭 패턴 | "canvas-tab 답습" | **2-뷰 하드코딩(추상 부재) → 신규 마운트** 정정 | A 실측 |
| TTS 첫 사례 | 다중 음성/모델 | **다중 음성/모델 유지(원안)** + GPU 리스크 선결 검증 | §F 사용자 결정 |
| BLOCKING | 없음 | **C-1~C-4 (C-1·C-3 비협상)** | §C 통합 |

## 1. 배경 (119 dogfooding이 도달한 지점)

사용자 UI 실 테스트로 #UI-1~4 발견 → "대화로 시킨 작업이 실제로 반영되는지"의 진짜 병목은
**산출물을 자비스에 통합하는 메커니즘 부재**(#UI-4)였다. 동시에 사용자는 자비스를 계속 확장
하려 한다(계산기·TTS 비교·버추얼 캐릭터…). 두 문제의 **공통 답 = 플러그인 아키텍처**.

- `[[project_jarvis_output_application_gap]]` (워커는 격리 work 작업, 실 반영 0 — 의도된 안전 경계)
- `[[project_jarvis_controlled_child_then_friday]]` (사람 시킨 단발 작업 = jarvis 영역, 자율진화 friday 아님)

## 2. 현 구조 진단 (실측 — 합의 코드 재확인)

| 영역 | 상태 | 한계 |
|---|---|---|
| 백엔드 `server.py` | `make_jarvis_routes(board)`(`jarvis_tasks.py:400`)·`make_jarvis_plan_routes`(`jarvis_plan.py:307`) **빌더 패턴 2개** → `server.py:600·606` `routes += make_*()` 2회 = **사실상 수동 레지스트리** | 신규 플러그인마다 server.py 2곳(import + `routes +=`) 편집 = 코어 수정 |
| 프론트 `jarvis_hud/index.html` | **2179줄 모놀리식**. 단일 inline style(11-868)+script(1122-2177), `type=module`/import 전무, **StaticFiles 0**, FileResponse 단일 서빙(`server.py:558`). 탭 전환=`jarvisView`/`canvasList` **2-뷰 하드코딩** `style.display` 토글(2160-2163) | ★ 가장 약한 고리. N-패널 마운트 추상화 **부재**(답습 대상 아님 = 신규 구축) |
| TTS | F5-TTS-ko `/api/tts`(`server.py:401-477`), `_synthesize_wav_sync` **단일 ref 하드코딩**(`HANA_REF_AUDIO`) | 비교/측정 UI 부재 + **다중 음성/모델 합성 경로 미존재** |
| #UI-4 반영 | `OutcomeStatus.APPLIED`(`orchestrator.py:24-27,152`) = **라벨만**. 복사/repo 반영 코드 **0건**(grep `copytree·register_plugin·PLUGINS` 0 hit) | 산출물이 격리 work에 머묾, 실 반영 메커니즘 0 |
| 캐릭터 | `setCharState` 상태 개념 + 에셋 파이프라인(ADR-003) | 버추얼 캐릭터 에셋 미구축(별건) |

**결론**: 백엔드는 플러그인 *씨앗*(빌더 2개) 있으나 **메타·레지스트리·동적 로드는 0**, 프론트는 모놀리식이 병목. **사용자 확장 로드맵이 다수 확정 → 정식 인터페이스 선투자 정당화**(아래 §3).

## 3. 핵심 명제 — 플러그인 아키텍처가 두 문제를 동시에 푼다

```
[#UI-4 산출물 반영]                    [확장 지속가능성]
자비스가 만든 결과물을        ═══►      계산기·TTS비교·캐릭터를
어떻게 자비스에 붙이나?                  어떻게 깔끔히 추가하나?
                    └──── 같은 답 ────┘
              표준 플러그인 인터페이스 + 등록
```

- 플러그인 = 자비스 코어와 **분리된 기능 단위**(백엔드 라우트 + 프론트 패널 + 메타).
- 자비스 코어는 플러그인을 **등록**만 한다 → **self-modification(자기 코드 직접 수정) 회피**.
- claude 워커(#UI-3)가 별도 폴더(#UI-4)에 플러그인을 구축 → 사람 승인 후 플러그인으로 **등록(B 복사)** = "반영".

**▶ 추상 수준 결정 (합의 §D + 사용자)**: 합의 Reviewer는 "TTS 1사례엔 rule-of-three 위반 선투자"로 *경량 규약*을 권고했으나, **명시한 사용자 영역 변수("2~3개 이상 확장 확정 = 정식 인터페이스 정당")** 에서 사용자가 **"여러 개 확정"** 을 선택 → **정식 인터페이스(메타 + 레지스트리) 채택**. 단 BLOCKING C-4(데이터 레지스트리 + 명시 등록 분리)는 정식에서도 비협상.

## 4. 목표 / 비목표

**목표**
- 플러그인 인터페이스 정의(백엔드 라우트 빌더 + 프론트 패널 + **데이터 메타/manifest**) + 등록 메커니즘.
- 프론트 모놀리식(`jarvis_hud/index.html`) → 플러그인 패널 분해 *경로* 확립(전면 재작성 아님, 점진. StaticFiles 마운트 선결).
- #UI-1~4를 이 아키텍처로 수용: 대화 라우팅 → claude 워커 → 별도폴더 구축 → **B 복사 게이트(신규 정의)** → 플러그인 등록.
- 첫 사례(TTS 비교 페이지)로 설계를 *구체 검증*.

**비목표 (이번 범위 밖)**
- `index.html` 전면 재작성(점진 분해만).
- 버추얼 캐릭터 에셋 *생성* 자체(에셋 파이프라인 ADR-003 별건, "에셋 플러그인" 유형으로 자리만).
- friday 자가진화 (사람 시킨 단발 확장만).
- 제3자 플러그인 보안 모델 / 샌드박싱 / 서명 / 핫리로드 (개인 툴, 자기·자비스 생성만 — 비례. DEFER).
- BL-3 redaction 비대칭 즉시 구현 (합의 등록만, 발효는 실 trigger까지 DEFER).

## 5. 설계 — 플러그인 아키텍처

### 5-1. 플러그인 구성 (3요소)
| 요소 | 내용 | 기존 자산 |
|---|---|---|
| 백엔드 | `make_<plugin>_routes(<주입 포트>) -> list[Route]` 빌더 | `make_jarvis_routes` 패턴 답습 |
| 프론트 | 패널 JS 조각(`jarvis_hud/plugins/<name>.js`) — StaticFiles 로드 + 마운트 지점 div | **신규 마운트**(현 2-뷰 하드코딩은 추상 아님) |
| 메타 | **데이터 manifest**(`{name, title, icon, routes_module, panel_js, 격리요건, 권한}`) | 신규 |

### 5-2. 등록 메커니즘 (C-4 반영 — 데이터 레지스트리 + 명시 등록 분리)
- **탐색**: `jarvis_hud/plugins/` 폴더 스캔 → manifest 발견(데이터, 코어 코드 불변).
- **활성화**: 탐색 ≠ 활성화. drop-in 자동 로드 **금지**(self-mod 우회 차단). 활성화는 **명시 사람 등록 파일**(예: `plugins/enabled.json` 또는 명시 등록 리스트)에 등재된 것만.
- 백엔드: `for p in discover_enabled_plugins(): routes += p.make_routes(ports)`. `server.py` 핵심 라우트와 분리.
- 프론트: StaticFiles 마운트(C-2 선결) → manifest의 `panel_js` 를 `<script src>` 로 동적 로드, index.html 은 마운트 지점만.
- **등록 시점**: **재시작**(갈림길2 합의 — 핫리로드 미도입, 상태오염·코어 핫스왑 표면 회피).
- ★ **점진 경로**: 기존 라우트/UI 즉시 이전 X. 신규(TTS 비교)부터 플러그인으로, 기존은 여유 시 흡수. 첫 TTS 패널은 인라인先 가능, 분리는 2번째부터(C-2).

### 5-3. #UI-1~4 수용 흐름 (통합)
```
대화 "TTS 비교 페이지 만들어줘" → [#UI-1 라우팅 + #UI-2 백엔드 통합 판정] 작업 감지
  → 제안 버튼 → plan
  → [#UI-3 claude 워커]가 [별도 폴더]에 플러그인 3요소 구축 (격리 work)
  → 사람 승인(plan 모달 + 산출 diff 검토 — scrub 적용)
  → [#UI-4 B 복사 게이트(신규)] work/ 하위 산출물 → jarvis_hud/plugins/<name> 복사
       (realpath 화이트리스트 + symlink 방어 + 자동복사 금지 코드강제) + enabled 등록
  → 자비스 재시작 시 플러그인 활성
```

## 6. 첫 사례 — TTS 음성 비교 분석 페이지 (다중 음성/모델 — 원안 유지)

- **기능**: 입력 텍스트 → **여러 음성/모델로 생성** + 나란히 **비교**(파형/재생/메모) + 측정 기록.
- **백엔드**: 기존 `/api/tts`(F5-TTS-ko) + `make_tts_compare_routes`(생성 N개·측정 저장). 데이터 레이어 `[[project_jarvis_data_layer]]` §10-5 측정 repo 정합.
- **프론트**: 플러그인 패널(비교 그리드 + 재생 + 메모). 첫 분리 패널 사례.
- **▶ GPU/메모리 리스크 선결 검증 (합의 §F — R4 기각 대신 명시)**: `_synthesize_wav_sync` 는 현재 `HANA_REF_AUDIO` **단일 ref 하드코딩** + `_f5_tts` 단일 전역 캐시. "다중 음성/모델"은 **신규 합성 경로**(ref voice 파라미터화 또는 다중 모델 로드)가 필요하며, 다중 모델 동시 보유 = **GPU/메모리 리스크**. → **구현 선결 조건**: ① 다중 모델 동시 로드 메모리 실측 ② ref voice 파라미터화 PoC ③ 모델당 로드 시간/캐시 전략. 실측 후 동시 비교 개수 상한 결정.
- **UX 컨펌**(`[[feedback_ui_design_confirm_first]]`): 비교 페이지 레이아웃 mockup 컨펌 후 구현.

## 7. 보안 / 신뢰 경계 (over-claim 정정 — R3)

- **self-mod 회피**: 플러그인은 `jarvis_hud/plugins/<name>` 격리 디렉터리에 등록 → 자비스 코어 코드 미수정. **정정(R3)**: 현재 `server.py:600·606` 2곳 편집 필요 = "1줄"은 거짓. **진짜 코어 불변화는 §5-2 데이터 레지스트리(폴더 스캔) 도입이 전제** — 코어는 `discover_enabled_plugins()` 1회 호출만, 플러그인 추가는 데이터(폴더+enabled 등록)로.
- **B 복사 게이트**: **정정(R3)**: 현재 **미구현**(복사 로직 0건). 본 설계가 게이트를 *신규 정의*함 — 기존 plan 게이트(`plan_controller`)와 별개. 격리 work 산출 → 사람 **diff 검토**(scrub 적용) 후 plugins/ 로 복사. **자동 복사 금지 = 코드 강제**(승인 핸들러가 명시 사람 액션 없이 복사 함수 호출 불가).
- **복사 범위 (C-3 비협상)**: 복사 소스 = `home/work` 하위로 **엄격 제한**. `work/` 는 단일 RW루트이자 `.credentials.json`(0600) 잠재 위치 → 상위 통째 복사 시 credential 유출. symlink/realpath 방어 + secret scrub 필수.
- **복사 소스 결정 (C-1 비협상)**: claude 는 항상 `~/.jarvis/claude-home/work/` 에 씀(`worker_setup.py:159` cwd 고정), dispatch workdir(`/tmp`)과 불일치(`orchestrator.py:124`). B복사 구현 전 **복사 소스를 `home/work` 하위로 명시 고정**해야 소스 경로 결정됨.
- **플러그인 권한 (갈림길5 합의)**: 플러그인은 board 전체 핸들 금지. **최소권한 주입 — 대화 repo = read-only / 측정 repo = write** 두 함수(포트)만 주입. 별도 권한 프레임워크는 과잉(비례).
- **잔여 BL-3 (DEFER)**: 대화 입력 → claude argv redaction 미적용(`worker.py:130`, OllamaWorker `:339`와 비대칭). 플러그인 고유 신규 표면 아님(기존 라우팅과 동일 경로). **합의록 명시 등록**, 발효는 실 trigger(secret 유출 dogfooding 신호)까지 DEFER.

## 8. 핵심 갈림길 — 합의 확정 상태

| # | 갈림길 | 합의 결정 | 분류 |
|---|---|---|---|
| 1 | 프론트 분해 방식 | **(a) 분리 JS / 무빌드** (빌드스텝 3자 기각) | Consensus |
| 2 | 등록 시점 | **재시작** (핫리로드 미도입) | Consensus |
| 3 | 등록 메타 형식 | **데이터 manifest(폴더 스캔) + 명시 사람 등록 분리** | C 규약 + B 명시등록 흡수 |
| 4 | B 복사 대상 | **내부 `jarvis_hud/plugins/` 1차 + 외부앱(데이터 비공유 위젯) 후속 DEFER** | Consensus |
| 5 | 플러그인↔코어 권한 | **최소권한 주입: 대화 read-only / 측정 write** | Partial→합의 |

**잔여 사용자 결정**: 갈림길4 외부앱(버추얼 캐릭터 등 데이터 비공유 위젯) 유형 분기를 *언제* 도입할지 / BL-3 발효 시점 — v2 검토 시 확인.

## 9. 구현 BLOCKING (TDD 진입 전 설계 해소 — 합의 §C)

1. **C-1 ⭐비협상**: B복사 소스 결정(workdir 불일치 해소 + 게이트 코드강제 + realpath 화이트리스트).
2. **C-2**: StaticFiles 마운트 신규(분리 JS 선결).
3. **C-3 ⭐비협상**: 복사 범위 work/ 하위 엄격 제한 + symlink 방어 + scrub.
4. **C-4**: 데이터 레지스트리(폴더 스캔) + 탐색≠활성화(명시 사람 등록 분리).

## 10. 다음 단계

CLAUDE.md 단계별 합의 cycle: brief v2 **검토 → (필요시 미세 합의) → TDD → commit → push** (자동 진입 0).
- v2 검토에서 §8 잔여 사용자 결정 2건 확인.
- TDD 진입 시 GPU 리스크 선결 검증(§6) → 플러그인 인프라(레지스트리+manifest+StaticFiles) → B복사 게이트 → TTS 첫 사례 순.
- UX mockup 컨펌(§6)은 TTS 프론트 구현 직전.
