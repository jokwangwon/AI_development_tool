# 3+1 합의 보고서 — 디딤돌1h requires_execution 실행 격리 갭

> **대상 brief**: `docs/phase0/jarvis-stone1h-execution-isolation-gap-design-brief.md` (v1, PoC F5 반영)
> **합의일**: 2026-05-31 세션
> **구성**: Agent A(구현 분석) · Agent B(품질/안전) · Agent C(대안 탐색) 독립 병렬 + Reviewer(오케스트레이터) 교차 비교
> **판정**: **REVISE → 옵션 A 채택 (조건부, 통합 BLOCKING 6 + 발견#2 DEFER)**
> **성격**: 헌법 8조(보안) 직결 — 격리 완화 방향이라 다관점 필수

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus, 3 source 동의)

| 사항 | A | B | C |
|------|---|---|---|
| **옵션 A 채택** (`/dev/null` 등 무해 디바이스 단일 파일 RW allowlist) | 구현 가능(F5) | 조건부 안전 | 최선(대안 전부 불가) |
| **옵션 B/C/D 거부** | — | D=헌법8조 위배, B=심링크/위험노드 동시노출 | A-3 bwrap·A-4 overlay·A-5 우회 **실측 전부 불가** |
| **발견 #2 (did_act 우회) DEFER** | — | DEFER 안전(옵션E 신호원 부재) | #1 먼저, #2 후속 |
| **발견 #2 잔여 위험은 `/dev/null` 비특정 일반 패턴** | — | BL-3 정확 | BL-3 일반 해법 필요 |

### ② 부분 일치 (Partial, 2 동의 1 보강)

| 사항 | 합치 | 차이/보강 |
|------|------|-----------|
| **RW 디바이스 인터페이스** | A·B 모두 "명시 분리 필요" | A: 별도 `CLAUDE_RW_DEVICES` 상수+`rw_files` 인자(stat 자동판정 단독 = "RO목록 파일이 자동 RW" silent 권한상승 함정). B: B-2 심링크/CHR 검증 요구 → **"명시 + 검증"으로 수렴** |
| **발견 #2 완화재** | B·C 모두 "DEFER하되 보완재 도입" | B: 추론폴백 휴리스틱 detection 동시. C: **E-3(stdout 산출계약)+E-2(fs-delta) 결합이 옵션E보다 우월**(harness 직접 결정적 관측) |

### ③ 발산 (Divergence)

| 사항 | 입장 | Reviewer 판정 |
|------|------|---------------|
| **발견 #2 완화재 *동시* 도입 여부** | B/C = 동시 권고 / 사용자 사전선택 = "#1 후 재평가 DEFER" | **사용자 결정 포인트로 승격**(§ 결정 Q-A) — 순수 DEFER vs 저비용 detection 동시 |

### ④ 누락 (Gap, 특정 에이전트만 포착)

| 출처 | 누락 포착 | 중요도 |
|------|-----------|--------|
| **A** | `isolation.py:99` `os.path.isdir` 필터가 `/dev/null`(char device)을 **조용히 드롭** → 옵션 A 자체 무효화 | ⭐ **치명** — 이 한 줄 없으면 전부 무효 |
| **A** | CI 에 `make -C src/jarvis/sandbox` 빌드 스텝 부재 → C 변경 회귀를 `_sandbox_built` skip 으로 자동 포착 못 함 | 중 |
| **B** | `/dev/tty` = 터미널 주입(TIOCSTI) 클래스 — `/dev/null`·`zero` 와 위협 클래스 다름. 무해 묶음서 분리 | ⭐ 높음 |
| **B** | `/dev/stdin|stdout|fd` = `/proc/self/fd` **심링크** → allowlist 오판 포함 시 `/proc` 우회(BL-2 붕괴). O_PATH 가 심링크 follow | ⭐ 높음 |
| **B** | F5 는 *미노출-자동차단*만 실증, **명시-요청-거부**(`/dev/sda` 줬을 때 BLK 거부) 미실증 | 높음 |
| **B** | 문서 정합 — ADR-014 §2.3 "전체 /dev 미노출" + `worker_setup.py:36-37` 주석("단일파일도 EINVAL→디렉터리만")을 F5 가 **반증** → 정정 필요 | 중 |
| **C** | `/dev/null` 쓰기 = claude **shell-snapshot source**(`unalias -a 2>/dev/null` 등 10건)의 구조적 산물 — **회피 불가** 실측. brief §7 "추정"→"실측" 격상 | 중(근거 강화) |
| **C** | 스냅샷이 `/dev/null` **단일 노드만** 참조 → 최소 allowlist=`/dev/null`만으로 발견#1 해소 충분(Q3 답) | 중 |
| **C** | 옵션 A는 ll_sandbox 레벨 수정 = **provider-중립**(codex 등 전 워커 혜택, 헌법 5조) | 중(장점) |

---

## Phase 4 — 합의 도출 (통합 BLOCKING)

> brief 의 BL-1(기술 가능성)은 F5 PoC 로 **이미 해소**. 아래는 합의가 도출한 *구현/안전* BLOCKING 재집합.

| # | BLOCKING | 내용 | 출처 |
|---|----------|------|------|
| **CL-1** (치명·필수) | wrap 필터 | `isolation.py:99` `os.path.isdir(p)` → `os.path.exists(p)`. **없으면 `/dev/null` 드롭 → 옵션 A 무효.** | A 누락 |
| **CL-2** (필수) | 명시 means 레버 | 별도 `CLAUDE_RW_DEVICES: tuple[str,...] = ("/dev/null",)` 상수 + `LandlockIsolation(rw_files=…)` 인자. stat 자동판정 *단독* 금지(RO목록 파일=자동RW silent 권한상승 차단). RW 디바이스 = 이름 있는 감사가능 레버 | A·B 수렴 |
| **CL-3** (보안·필수) | 최소 시작 allowlist | 시작 = **`/dev/null` 단일 리터럴**. `/dev/tty`(터미널 주입)·`zero`·`urandom` 은 무해 묶음서 분리 — 노드별 개별 판정 + dogfooding 신호 시에만 추가. **디렉터리/glob/prefix 금지** | B-1·C |
| **CL-4** (보안·필수) | 노드 검증 + 음성 테스트 | allowlist 항목: ① `os.path.islink` 거부(심링크 우회 차단) ② `realpath` 후 `/dev/` prefix 검증 ③ `stat` **`S_ISCHR` 만 허용, `S_ISBLK`(sda)·기타 거부**. **음성 테스트**: `/dev/sda`·`/dev/mem`·`/dev/stdin` 명시 요청 시 거부 실증(F5 미실증분) | B-2 |
| **CL-5** (문서 정합) | ADR/주석 정정 | 채택 시 ADR-014 §2.3 "전체 /dev 미노출" + `worker_setup.py:36-37` 주석(F5 가 반증) 정정. `reference_claude_landlock_isolation` 메모리 교차 갱신(CLAUDE.md §7) | B-3 |
| **CL-6** (센서) | CI 빌드 스텝 | CI 에 `make -C src/jarvis/sandbox` 추가 — C 디바이스 분기 회귀를 `_sandbox_built` skip 너머로 자동 포착 | A |

### 발견 #2 (did_act 우회 silent semantic) — DEFER 합의
- **만장일치 DEFER**: 옵션 E(개별 tool exit 신호)는 claude 엔벨로프에 신호원 부재(1g PoC) → 즉시 구현 불가.
- **단 잔여 위험은 DEFER 기간 활성** + `/dev/null` 비특정 일반 패턴(BL-3). #1 고쳐도 *다른* 실행 실패(컴파일 에러·import 실패·타임아웃 등) 시 추론 폴백 + did_act=True 우회 여전.
- **B·C 가 더 나은 후속 센서 제시**(옵션 E 대체): **C 의 E-3(stdout 산출 계약 — sentinel 부재=실행 미수행) + E-2(fs-delta — 가짜홈 `work/` 전후 스냅샷)** 결합. 둘 다 **harness 직접 결정적 관측**(provider 누출 0, 헌법 5조). 단 controller 통합 PoC 미수행(설계 권고 수준).

### over-claim 정정 (B)
- F5 "위험 디바이스 차단/선별 정확" = *미노출-자동차단*까지만 실증. *명시-요청-거부*는 CL-4 음성 테스트로 실증 전 미검증.
- "격리 본질 양립" = 목표≠결과("양립 *가능*"이 정확).
- "`/dev/null` 무해"의 암묵 일반화 차단(노드별 분리 표기). brief §7 에 1줄 추가.

### 근거 보강 (C)
- brief §7 "`2>/dev/null` 추정" → **"claude shell-snapshot source 의 구조적 산물(실측, 회피 불가)"** 격상.

---

## Phase 5 — 사용자 결정 포인트

- **Q-A** (발산 해소): 발견 #2 완화재를 **#1과 동시 도입**할까(B·C 권고: E-3 stdout 산출계약 저비용 센서) 아니면 **순수 DEFER**(사용자 사전선택)할까?
- **Q-B** (CL-3 범위): 시작 allowlist = `/dev/null` 단일로 확정? (합의 권고 = 예, 스냅샷 실측상 충분)
- **Q-C** (CL-2): 별도 `CLAUDE_RW_DEVICES` 명시 상수 방식 채택? (합의 권고 = 예)
- **Q-D** (CL-6): CI 빌드 스텝 추가 범위 — 이번 1h 에 포함 vs 별건?

**합의 종합 권고**: 옵션 A 채택 + CL-1~CL-6 충족 + 발견#2 DEFER(단 Q-A 로 E-3 동시 도입 여부 결정). brief v1.1 로 흡수 후 TDD.
