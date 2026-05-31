# 디딤돌1h — requires_execution 실 실행 격리 갭 + did_act 우회 silent semantic 설계 brief

> **상태**: **v1.1** — 3+1 합의(A/B/C + Reviewer, REVISE) 흡수 + 사용자 결정. **TDD 구현 진입**.
> **합의 보고서**: `docs/review/3plus1-consensus-2026-05-31-jarvis-stone1h-execution-isolation.md`
> **작성**: 2026-05-31 세션 (디딤돌1g did_act dogfooding 후속, 다단계 협업 dogfooding 발견)
> **선행**: 디딤돌1f(silent semantic failure) · 1g(did_act 행동 관측) · ADR-014(레벨2 가짜홈 격리) · [[reference_claude_landlock_isolation]]
> **방법론**: SDD (코드 전 설계) + 단계별 합의 (brief → 승인 → 3+1 합의 → 구현)
> **성격**: ⚠️ 헌법 8조(보안) 직결 — 격리 완화 방향이라 means/ends 분리(ADR-011) + 다관점 검증 필수

---

## 합의 흡수 (v1.1 — 3+1 REVISE → 옵션 A 채택 + 통합 BLOCKING 6 + 사용자 결정)

> A/B/C 만장일치 옵션 A 채택 + B/C/D 거부(C 가 대안 전부 실측 불가 확정). brief v1 의 BL-1(기술 가능성)은 F5 로 해소. 합의가 **누락 BLOCKING 6**(특히 CL-1 치명) + over-claim 정정 + 근거 보강을 도출.

| # | 통합 BLOCKING | 구현 요구 |
|---|---------------|-----------|
| **CL-1** ⭐치명 | `isolation.py:99` `os.path.isdir(p)` → `os.path.exists(p)`. `/dev/null`(char device)이 현재 조용히 드롭됨 → **없으면 옵션 A 무효** | wrap 필터 완화 |
| **CL-2** | 별도 `CLAUDE_RW_DEVICES: tuple = ("/dev/null",)` 상수 + `LandlockIsolation(rw_files=…)` 인자. stat 자동판정 단독 금지(RO목록 파일=자동RW silent 권한상승 차단) | 명시 means 레버 |
| **CL-3** | 시작 allowlist = **`/dev/null` 단일 리터럴**. `/dev/tty`(터미널 주입)·`zero`·`urandom` 분리(노드별 판정+dogfooding). 디렉터리/glob/prefix 금지 | 최소 노출 |
| **CL-4** | allowlist 항목: `islink` 거부 + `realpath` `/dev/` prefix 검증 + `stat` **`S_ISCHR` 만 허용**(`S_ISBLK`=sda 거부). **음성 테스트**(`/dev/sda`·`/dev/mem`·`/dev/stdin` 명시 요청 거부 실증, F5 미실증분) | 노드 검증 |
| **CL-5** | ADR-014 §2.3 "전체 /dev 미노출" + `worker_setup.py:36-37` 주석(F5 가 반증) 정정. `reference_claude_landlock_isolation` 메모리 교차 갱신 | 문서 정합 |
| **CL-6** | CI 에 `make -C src/jarvis/sandbox` 빌드 스텝 추가(C 회귀 자동 포착) | 센서 (**사용자: 이번 1h 포함**) |

**발견 #2 (did_act 우회 silent semantic)** — 만장일치 DEFER(옵션 E 신호원 부재) 이되, **사용자 결정 = E-3 산출 계약 동시 도입**:
- **E-3 (stdout 산출 계약)**: `requires_execution=True` 작업의 prompt 에 **sentinel 산출 지시**(feedforward) — 실행 결과를 `===EXEC_RESULT===` 류 마커로 stdout 에 찍게. controller 가 sentinel **부재 시 = 실행 미수행 신호**(센서, harness 직접 결정적 관측 — provider 누출 0, 헌법 5조). 추론 폴백("12입니다" 자연어)은 sentinel 없음 → 결정적 포착. did_act(num_turns) 약점("도구 썼지만 무산출") 보완.
- E-2(fs-delta)·옵션 E(exit≠0)는 후속(E-3 우선, 사용자 미선택).
- 차단 아님 — 경고-only(1f/1g 동형, BL-4 정신).

**over-claim 정정**: F5 "위험 디바이스 차단"은 *미노출-자동차단*까지만 실증(명시-요청-거부는 CL-4 음성 테스트로). "양립"=목표≠결과. "`/dev/null` 무해"의 암묵 일반화 차단(노드별 분리). §7 1줄 추가.
**근거 보강**: `2>/dev/null` 쓰기 = claude **shell-snapshot source**(`unalias -a 2>/dev/null` 등)의 구조적 산물 — 회피 불가(C 실측, §7 "추정"→"실측").

### 사용자 결정 (Q-A~Q-D)
- Q-A: 발견 #2 완화재 = **E-3 산출 계약 동시 도입**
- Q-B: 시작 allowlist = `/dev/null` 단일 (합의 권고대로)
- Q-C: 별도 `CLAUDE_RW_DEVICES` 명시 상수 (합의 권고대로)
- Q-D: CL-6 CI 빌드 = **이번 1h 포함**

---

## 1. 문제 (실 dogfooding 발견 — 2건, 인과 연결)

### 시나리오
ollama 사장(qwen3-30b) plan → 실 claude code 워커 다단계 의존 협업:
- subtask 0 (file→ollama): `mathutil.py` 에 `gcd(a,b)` 작성
- subtask 1 (code→claude, depends_on=[0], **requires_execution=True**): `mathutil.py` import 하여 `gcd(48,36)` **실행해 출력**

### 발견 #1 — requires_execution 실 실행이 격리에 막힘 (HIGH)
claude(subtask 1) 가짜홈 세션 로그(`9d0ad4cb`) 실측:
```
Bash: ls mathutil.py              → Exit 1, "/dev/null: 허가 거부"
Write: mathutil.py                → 성공
Bash: python3 -c "...gcd(48,36)"  → Exit 1, "/dev/null: 허가 거부"  (×4 재시도 전부)
text: "셸에서 /dev/null 접근 권한 문제가 발생하고 있지만, 논리적으로 결과를 알려드리겠습니다. 12입니다"
```
- **claude 의 모든 Bash 도구 호출이 `/dev/null: 허가 거부`로 실패** → 실제 코드 실행 불가.
- 근본 원인은 §3 PoC 에서 정밀 규명(claude Bash 래핑의 `2>/dev/null` 쓰기 vs 격리 RO 세트의 `/dev` 부재).

### 발견 #2 — did_act 우회 silent semantic failure (HIGH, 116 false negative 현실화)
- claude 가 `Write`(mathutil.py) 했으므로 `num_turns>1` → **`did_act=True`** → **noop 경고 미발화**.
- 그러나 실제 실행은 4회 모두 실패 → **LLM 추론으로 "12입니다" 폴백**(우연히 정답).
- 결과: `exit=0` · `status=COMPLETED` · 경고 0. → **사용자가 원한 실제 실행 출력이 아닌 추론값인데 "완료" 표시.**
- 116(1g) 정직단서가 예측한 false negative("도구를 썼지만(did_act=True) 무산출")가 **실 작업에서 현실화**. 117 dogfooding 이 "9회 0건"이라 한 건 그 prompt 들이 *도구 미사용*에 수렴했기 때문 — 실행 필요 작업에선 발생.

### 인과 사슬
```
발견 #1 (/dev/null 차단) → Bash 실행 4회 실패 → claude 추론 폴백
  → Write 로 did_act=True → 발견 #2 (경고 미발화, silent semantic)
```

---

## 2. 회귀 검증 (기존 갭 vs 회귀 — 기존 갭 확정)

| 항목 | 증거 | 결론 |
|------|------|------|
| `/dev` 제외 시점 | `CLAUDE_RO_PATHS` 가 레벨2 도입 커밋 `827bb98`(2026-05-30)부터 `/dev` 미포함. 그 후 변경 0 | 발견 #1 = **회귀 아님, 레벨2 도입 이래 기존 갭** |
| 108 "성공" 진위 | 108 dogfooding 세션 로그(`d44fdd68`, 2026-05-30 17:51): claude **Bash 0회**, 텍스트 `print(add(2,3)) 출력: 5`만 (추론) | 108 "add→5 성공" = **과대기록**(추론 폴백, did_act 도입 전이라 미검출) |
| 함의 | — | ⚠️ **레벨2 격리 이래 `requires_execution` 실 실행이 진짜로 작동한 적 없을 가능성** — 늘 추론 폴백, did_act(116)가 부분적으로만 포착 |

---

## 3. PoC 실측 (근본 원인 규명 — 2026-05-31, ll_sandbox 직접 호출)

`ll_sandbox <rw_dir> [ro_dir...] -- <cmd>` 로 격리 RO 세트(`/usr /lib /bin /sbin /etc /run/systemd/resolve`, **/dev 없음**)를 그대로 재현:

| # | 케이스 | 결과 | 의미 |
|---|--------|------|------|
| **F1** | `/dev` 없이 `python3 -c "print(2+3)"` | **`5` 정상** | python/subprocess 실행 자체는 /dev 불요 |
| **F2** | `bash -c 'echo HI 2>/dev/null'` | stdout 빈 + stderr **`bash: 줄 1: /dev/null: 허가 거부`** | ⭐ **근본 원인** — claude Bash 래핑의 `2>/dev/null` *쓰기*가 차단. 실 로그와 정확히 일치 |
| **F3** | `/dev/null` 단일 파일을 RO 인자로 추가 | **`add_rule(/dev/null): Invalid argument`** (EINVAL, cmd 미실행) | 현재 ll_sandbox.c 로 **단일 파일 노출 불가** — RO access mask 에 디렉터리 전용 권한 포함 → 파일 fd 에 EINVAL |
| **F4** | `/dev` 디렉터리 전체 RO 노출 | python 실행(`5`)되나 `echo >/dev/null` *쓰기* 실패(`WROTE_NULL` 없음) | /dev RO 로도 `/dev/null` **쓰기 불가** — write 하려면 RW 필요(ll_sandbox 는 RW 1개=가짜홈만) |
| **F5** ⭐ | PoC 바이너리(`/tmp/poc_devnull.c`): `allow_path` 에 stat 기반 파일/디렉터리 분기 — 파일이면 `ACCESS_FS_FILE_RW`(디렉터리 bit 제거 + WRITE_FILE) 로 좁힘. `/dev/null` 단일 파일 RW 노출 | `echo HI 2>/dev/null`→**HI + WRITE_NULL_OK**, `python3 print(40+2)`→**42** (실행 복구). `/dev/null` 만 줬을 때 `/dev/zero`→**ZERO_BLOCKED** | ⭐ **옵션 A 기술 가능 확정** — F3 EINVAL 원인 = ②(RO 규칙의 `READ_DIR` 디렉터리 bit). 파일용 mask 로 좁히면 **단일 파일 RW 노출 가능**(ABI 7), allowlist 선별 정확(위험 디바이스 차단) |

**핵심**: claude Bash 도구는 명령에 `2>/dev/null` 류 **쓰기 리다이렉션**을 붙인다(claude 내부, 불투명·제어 불가). `/dev/null` 은 **RW 노출**이 필요한데, 현재 ll_sandbox.c 는 RO 규칙에 디렉터리 전용 bit(`READ_DIR`)를 포함해 파일에 EINVAL(F3). **해소 = `allow_path` 에 파일/디렉터리 mask 분기**(F5 PoC 실증) → `/dev/null` 등 무해 디바이스 단일 파일 RW allowlist 노출. ① Landlock 자체 불가 아님(원인 ② 확정).

---

## 4. 설계 공간 (옵션 + 트레이드오프)

> 제약: `/dev/null`(+ 셸이 흔히 쓰는 `/dev/zero`·`/dev/urandom`·`/dev/tty`)은 **RW 노출**이 필요. 위험 디바이스(`/dev/sda`·`/dev/mem`·`/dev/kmem`·`/dev/port`)는 **노출 금지**. 보안 = "무해 디바이스만 선별 RW".

| 옵션 | 내용 | 장점 | 단점/리스크 |
|------|------|------|-------------|
| **A** (권고 후보) | ll_sandbox.c 수정 — 파일용 access mask 분리(REG 파일 전용 RW 규칙) → `/dev/null` 등 **무해 디바이스 단일 파일 RW** 노출 | 최소·정밀 노출(우회 채널 0), 위험 디바이스 미노출 | C 코드 변경 + **Landlock 파일 RW path_beneath 가능 여부 PoC 필요**(F3 는 RO 에서 EINVAL — mask 좁히면 될지 미실측) |
| **B** | ll_sandbox 다중 RW 디렉터리 지원 + `/dev` RW 노출 | C 변경 작음 | ⛔ `/dev/sda` 등 위험 디바이스 RW 동시 노출 — 보안 후퇴, **거부 권고** |
| **C** | 가짜홈 안에 `/dev/null` mknod/bind | claude 가 절대경로 `/dev/null` 참조 → 가짜홈 내부로 안 보임. mknod=권한 필요, bind=root 필요 | ⛔ 비현실적(권한), **거부 권고** |
| **D** | requires_execution 작업만 격리 완화(passthrough) | 즉시 실행 복구 | ⛔ 헌법 8조 보안 후퇴 — code 워커 = 가장 격리 필요. **거부 권고** |
| **E** | (발견 #2 별도) did_act 를 "도구 사용"→"실행 *성공*"으로 강화 — 실패한 Bash exit≠0 을 신호로 | silent semantic 추가 포착 | claude 엔벨로프가 개별 tool exit 미노출(1g PoC) — 신호원 불명확, #1 해결 후 재평가 |

### 보안 트레이드오프 (헌법 8조 + ADR-011 means/ends)
- `/dev/null` RW 노출은 **격리 완화**다 — 하지만 `/dev/null` 자체는 쓰면 버려지고 읽으면 EOF, **exfil/우회 채널 아님**. 위험은 *어떤 디바이스를 노출하느냐*(means)이지 노출 행위(ends) 자체가 아님.
- 옵션 A 의 "무해 디바이스 allowlist"는 §1 안전 결과(실 실행 복구) + 격리 본질(위험 디바이스 차단) 양립. allowlist 가 means 레버(harness 소유, 워커/boss 가 못 정함).

---

## 5. 미해결 질문 (Q — 사용자/합의 결정 포인트)

- **Q1** (방향): 옵션 A(파일 RW allowlist) 채택? B/C/D 거부 권고 동의?
- **Q2** (PoC 선행): ✅ **해소(F5)** — 파일용 mask 분기로 단일 파일 RW 노출 가능 확정. EINVAL = access mask 원인(파일 자체 불가 아님). 잔여: claude Bash 가 `/dev/null` *외* 다른 /dev 노드(`/dev/tty` 등)도 쓰는지는 통합 dogfooding 확인.
- **Q3** (디바이스 allowlist 범위): `/dev/null` 만? `+/dev/zero /dev/urandom /dev/tty`? 최소 시작 후 dogfooding 확장?
- **Q4** (발견 #2 우선순위): #1 해결(실행 복구)로 추론 폴백이 사라지므로 #2(센서 강화 옵션 E)는 **#1 후 재평가**로 DEFER? 아니면 동시?
- **Q5** (108 기록 정정): 108 entry "성공" 과대기록을 세션 로그/CONTEXT 에 정직 정정 표기?
- **Q6** (회귀 테스트): 격리 안에서 실제 코드 실행 성공을 검증하는 트랙 A 테스트(주입 runner) 추가 — 향후 회귀 방지?

---

## 6. BLOCKING 후보 (3+1 합의 입력)

| # | 잠정 BLOCKING | 근거 |
|---|---------------|------|
| BL-1 | 옵션 A 의 Landlock 파일 RW 기술 가능성 미실측 (Q2) | F3 EINVAL — 가능 여부가 A 성립을 가름 |
| BL-2 | 디바이스 allowlist 의 "무해" 판정 근거 (Q3) | 어떤 /dev 노드가 진짜 무해한지 = 보안 판단, over-claim 위험 |
| BL-3 | 발견 #2 의 잔여 — #1 해결해도 *다른* 실행 실패 시 추론 폴백은 여전 (Q4) | did_act 우회는 /dev/null 특정이 아닌 일반 패턴 |
| BL-4 | 격리 완화가 ADR-014/[[reference_claude_landlock_isolation]] 의 레벨2 불변식과 충돌 안 하는지 | RW 노출이 BL-1(env)·BL-2(RO 최소화) 정신과 정합한지 교차 검증 |

---

## 7. 정직 단서
- PoC F1~F4 는 ll_sandbox **직접 호출** 실측 — claude Bash 도구의 *정확한* 래핑 명령은 claude 내부라 불투명. `2>/dev/null` 은 실 로그(`/dev/null: 허가 거부`)와 F2 재현으로 강하게 추정되나 claude 내부 코드 미확인.
- "레벨2 이래 실 실행 0회"는 108·1h 두 케이스 + 코드 이력 기반 **강한 정황**이지 전수 증명 아님. 다른 dogfooding 에서 우연히 작동한 케이스 존재 가능성 배제 못 함.
- 발견 #2 의 "추론 폴백"은 claude 가 *정직하게* "실행 안 되지만 논리적으로"라 밝힘 — 완전 은폐 아님. 단 jarvis controller 가 그 텍스트를 COMPLETED 로 처리 = 하네스 레벨 silent.
- 옵션 A 가 "보안 무손실"이라 단정 금지 — allowlist 추가는 공격면 증가(작더라도). "무해 디바이스 한정 최소 증가"가 정확한 표현.
