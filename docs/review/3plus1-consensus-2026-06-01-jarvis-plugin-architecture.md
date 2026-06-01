# 3+1 합의 보고서 — jarvis 플러그인 아키텍처 brief v1 (#UI-1~4 통합)

> **일자**: 2026-06-01 · **대상**: `docs/phase0/jarvis-plugin-architecture-design-brief.md` (v1)
> **프로토콜**: CLAUDE.md §3 (아키텍처 의사결정 + 보안 경계 → 3+1 필수)
> **판정**: **REVISE (조건부 승인)** → brief v2 작성으로 진입
> **참여**: Agent A(구현) · Agent B(안전/신뢰경계) · Agent C(대안) · Reviewer(교차비교)

---

## 1. 교차 검증 — 실측 주장 (Reviewer가 코드 재확인, 전부 사실)

| # | 주장 | 분류 | 확인 |
|---|---|---|---|
| 1 | `hud/`·`plugins/` 미존재, 프론트 루트는 `jarvis_hud/` | Consensus | ✅ 셋 다 미존재(신규 생성 대상) |
| 2 | 백엔드 빌더 패턴 2개 = 레지스트리 씨앗 | Consensus | ✅ `server.py:600·606` `routes += make_*()` |
| 3 | 프론트 `index.html` 2179줄 모놀리식 = 진짜 병목 | Consensus | ✅ StaticFiles 0, FileResponse 단일 서빙 |
| 4 | B복사(plugins/ 복사) 코드 0건 | Consensus | ✅ `copytree·hud/plugins·register_plugin·PLUGINS` grep 0 hit |
| 5 | APPLIED = 라벨만, 실 복사·반영 0 | Consensus | ✅ `orchestrator.py:152` status 마킹뿐 |
| 6 | 라우팅 = 순수분류·proposal만 (BL-1 견고) | Consensus | ✅ `server.py:259-266` proposal 페이로드만 |
| 7 | **BL-3 비대칭**: CliWorker raw argv vs OllamaWorker redaction | Gap (B 단독) | ✅ `worker.py:130` 무방비 / `:339` redact_messages |
| 8 | **B복사 소스 vs dispatch workdir 불일치** | Gap (A 단독) | ✅ `worker_setup.py:159` cwd=work 강제 → dispatch /tmp 무시 |
| 9 | 메타3요소+레지스트리클래스 = rule-of-three 위반 선투자? | **Divergence** | C 단독 이의, A·B는 brief 틀 내부 |
| 10 | "등록 1줄" = 실측 거짓 | Partial (B강, A약) | ✅ `server.py:600·606` 2곳 코어편집 |
| 11 | F5-TTS 다중음성/모델 미검증 | Gap (A 단독) | ✅ `_synthesize_wav_sync` 단일 ref 하드코딩 |

## 2. 갈림길 5건 3자 입장 + 합의

| 갈림길 | A | B | C | 합의 |
|---|---|---|---|---|
| 1 프론트 분해 | (a) 분리JS, 첫TTS 인라인先 | (a) 로컬 화이트리스트 | (a) `<script src>`, (b)빌드 기각 | **분리JS / 무빌드** (Consensus) |
| 2 등록 시점 | 재시작 | 재시작 | 재시작 | **재시작** (Consensus) |
| 3 메타 형식 | Python 선언 | JSON manifest+명시등록 | 메타 생략·규약 | **Divergence** → §4 + 사용자결정으로 정식화 |
| 4 B복사 대상 | 내부(조건부) | 내부1차+좁은포트 | 내부(정적한정)+외부위젯 후속 | **내부 1차 + 외부앱 후속DEFER** (Consensus) |
| 5 권한 경계 | 주입식 | 명시 capability 포트(대화ro/측정w) | 최소권한 주입 ro기본 | **최소권한 주입: 대화 read-only / 측정 write 분리** |

## 3. 통합 BLOCKING 4건 (A 기술3 + B 보안3 중복제거)

| # | BLOCKING | 왜 막아야 하나 | 해결 방향 |
|---|---|---|---|
| **C-1** ⭐비협상 | B복사 소스 미정의 (workdir 불일치 + 게이트 코드 0) | claude는 항상 `~/.jarvis/claude-home/work/`에 쓰는데 dispatch는 `/tmp` 넘김 → 복사 소스 미결. 복사 로직 0건인데 brief는 게이트 존재처럼 서술 | ① 복사 소스 = `home/work` 하위 명시 고정 ② plugins/<name> 화이트리스트 realpath 검증 ③ 자동복사 경로 구조적 부재(코드강제) ④ 복사 전 scrub diff |
| **C-2** | StaticFiles 마운트 부재 | FileResponse 단일 서빙 + import 전무. "canvas-tab 답습"으론 분리 JS 못 올림 = 신규 마운트 지점 선결 | StaticFiles 마운트 신규. 첫 TTS 인라인先, 분리는 2번째 |
| **C-3** ⭐비협상 | work = 단일 RW루트 = `.credentials.json`(0600) 시드 위치 | 복사 범위 미제한 시 credential 유출 표면 | 복사 범위 work/ 하위 엄격 제한 + symlink/realpath 방어 + secret scrub |
| **C-4** | "등록 1줄" framing이 self-mod 회피 실효 over-claim | `server.py:600·606` 2곳 코어편집 = 진짜 self-mod 회피 아님. drop-in 자동탐색 단독은 우회 | 레지스트리를 데이터(폴더 스캔)로 + 탐색 자동 ≠ 활성화(명시 사람 등록 분리) |

**DEFER (합의 등록만, 발효는 실 trigger까지)**: BL-3 redaction 비대칭 즉시구현 / 제3자 샌드박싱·서명·manifest 서명 / 핫리로드. (개인 솔로 툴 비례성)

## 4. 중심 쟁점 판정 — 정식 인터페이스 vs 경량 규약

**Reviewer 권고**: 부분 채택 — C의 경량 규약 골격(메타클래스·레지스트리클래스·manifest파서·핫리로드 미도입). 근거: 백엔드 빌더가 *이미 2개* 메타 없이 운영 = "메타 레이어 불필요" 실증, TTS 1사례엔 rule-of-three 위반 선투자.

**단, Reviewer가 명시한 사용자 영역 변수**: "2~3개 이상 확장 확정 = 정식 인터페이스 선투자 정당".

**▶ 사용자 결정 (2026-06-01)**: **"여러 개 확정 (정식 인터페이스)"** 선택 → 확장 로드맵 확신도가 정식 인터페이스 선투자를 정당화. **§D 판정이 정식 인터페이스 쪽으로 확정**(합의 권고를 사용자 로드맵 정보가 뒤집음 — 합의가 예고한 변수). 단 BLOCKING C-4(데이터 레지스트리 + 명시 등록 분리)는 정식 인터페이스에서도 비협상.

## 5. brief over-claim 정정 권고 (R3, [[feedback_pass_scope_overclaim]])

1. §7 "B복사 게이트" → 복사 로직 0건인데 기존 게이트처럼 framing. **정정**: "미구현, 본 설계가 신규 정의" 명시.
2. §7 "등록 1줄" → server.py 2곳 편집 필요 실측 불일치. **정정**: 데이터 레지스트리(폴더 스캔) 전제 명시.
3. §2·§5-1 경로/패턴 표기 → `hud/plugins/`→`jarvis_hud/plugins/`, "canvas-tab 답습"→2-뷰 하드코딩(추상 부재, 신규 마운트).
4. §6 "위험 낮음" → F5-TTS 다중음성 미검증과 충돌. 정직 단서 추가.

## 6. 첫 사례 TTS 적합성

**Reviewer 권고**: 조건부 적합 — "단일 모델 다중 입력 비교"로 1차 축소(R4). `_synthesize_wav_sync`가 단일 ref 하드코딩이라 다중 모델 = GPU/메모리 리스크.

**▶ 사용자 결정 (2026-06-01)**: **"다중 음성/모델 비교 (원안)" 유지** → R4 기각. 대신 GPU/메모리 리스크를 **선결 검증 항목**으로 brief v2에 명시(silent drop 금지): 다중 모델 동시 로드 메모리 실측 + ref voice 파라미터화 신규 합성 경로가 구현 선결 조건.

## 7. 최종 판정: REVISE → brief v2

- **R1 (BLOCKING)**: C-1~C-4 해소 설계. C-1·C-3 비협상.
- **R2 (틀)**: 정식 인터페이스 채택(사용자 로드맵 확정) — 단 C-4 데이터 레지스트리/명시 등록은 정식에서도 유지.
- **R3 (over-claim)**: §5 1~4 정정.
- **R4**: 기각(사용자 원안 유지) → GPU 리스크 선결 검증으로 대체.
- **갈림길 확정**: 1=분리JS무빌드 / 2=재시작 / 3=데이터 manifest+명시등록 / 4=내부1차+외부DEFER / 5=최소권한 주입(대화ro/측정w).

**잔여 사용자 결정**: 갈림길4 외부앱(데이터 비공유 위젯) 재고 여부 / BL-3 발효 시점 — brief v2 검토 시 확인.
