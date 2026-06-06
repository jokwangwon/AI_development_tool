# Jarvis 워커 산출물 반영 루프 brief — 갭 1 정면 공략

> **일자**: 2026-06-06 · **브랜치**: `feature/jarvis-output-application-loop`
> **상태**: brief 작성 완료 → 사용자 검토 완료 → **3+1 합의 완료(REVISE, 2026-06-06)** → **사용자 BLOCKING 확인 대기** → (UI mockup 컨펌) → TDD. **자동 진입 0**.
> **합의 보고서**: `docs/review/3plus1-consensus-2026-06-06-output-application-loop.md`
> **합의 핵심**: 확정 방향 지지 + **BLOCKING 7건**. ★ CB-1 = `patch_validator.py` 신규(git apply는 문법만 검증→patch 의미 검증 필수: `.git/`·symlink·traversal·민감파일 거부). CB-2 화이트리스트(쓰기 0)·CB-3 fail-closed(3-way 금지)·CB-4 repo clean 검증·CB-5 preview scrub·CB-6 자동반영 금지·CB-7 apply≠commit. Q-b=fail-closed / Q-d=workdir 전체 diff(명시목록 V-1 DEFER).
>
> **사용자 검토 결과(2026-06-06) — 방향 고정**:
> - **D-5 첫 슬라이스 = slice-app-1 권고안 채택** (외부 repo에 워커 diff를 preview→1-클릭 승인→`git apply --check` 통과 시만 적용).
> - **D-2 반영 대상 = A (등록된 외부 프로젝트 repo만)**.
> - **Q-c commit 정책 = apply만** (작업트리 변경까지, git commit/push는 사람).
> - 파생 고정: **D-1 = A(diff/patch)** · **D-3 = A(git apply --check)** · **D-4 = plugin preview 재사용**.
> - → 합의 안건은 §4로 축소(D 값은 고정, invariant 답습) — 적대적 검증은 **D-2 안전성 + Q-b 충돌정책 + Q-d 산출물 식별**에 집중.
> **선행**: `docs/phase0/jarvis-completion-gap-analysis-2026-06-06.md` (본 brief의 evidence — 갭 1 식별).

> **답습 (비협상 — 재론 금지)**:
> - `src/jarvis/plugin_install.py` (현존 유일 "반영 게이트" — C-1/C-3/C-4 패턴 모법)
> - `[[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]]` (BLOCKING C-1·C-3·C-4 비협상)
> - `jarvis_tasks.py:15` (승인 게이트 = 반영 전, 워커는 dispatch 시 이미 실행)
> - 메모리: `[[project_jarvis_output_application_gap]]` · `[[project_jarvis_plugin_architecture]]` · `[[feedback_staged_consensus_workflow]]` · `[[feedback_proportionate_security_personal_tool]]` · `[[feedback_pass_scope_overclaim]]` · `[[feedback_ui_design_confirm_first]]`

> **북극성**: `[[project_jarvis_general_executor_northstar]]` — "내가 Claude에게 하듯 명령 수행".
> 그 후반부(**실행 결과를 실제 환경에 반영**)가 현재 plugin 경로 외에는 없다(갭 1). 이 brief는
> 그 **일반 반영 루프**의 설계 후보를 제시한다. **이 brief는 evidence + 후보만** — 반영 대상 범위·
> 단위·메커니즘 *결정*은 사용자 + 3+1 합의 영역(보안 관련 = 합의 필수).

---

## 0. 왜 지금 — 진입 조건

분석(2026-06-06)이 갭 1을 최대 갭으로 식별:
> 워커가 코드를 짜도 그 결과가 실제 repo에 적용되지 않는다. 유일한 반영 게이트는 plugin install뿐.

→ 북극성 "명령 수행"의 후반부가 막혀 있음. **사용자가 4번(분석)→1번(반영 루프) 진입을 명시(2026-06-06).**

---

## 1. 문제 정의 — 무엇이 끊겨 있나

```
[현재]
명령 → 계획 → 사람승인 → 워커 실행(격리 workdir/가짜홈) → 산출물(파일/코드/diff)
                                                              └──╳ 원본 대상으로 반영 경로 없음
                                                              └──✓ plugins_dir 복사만 가능(plugin 한정)

[목표]
                                            산출물 → preview → 사람승인 → 일반 대상에 반영(git apply/복사)
```

- 워커 산출물은 현재 `WorkerResult.output`(텍스트) + (OllamaWorker 한정) workdir 내 파일 1개.
- TmuxWorker(셸)는 가짜 홈 `work/`에서 임의 파일 생성 가능하나, 그게 **원본으로 나오는 경로 0**.
- plugin install은 `work_root → plugins_dir/<name>` **단일 화이트리스트**만 — 일반 대상 불가.

---

## 2. 비협상 invariant (plugin_install.py 답습 — 일반화의 골격)

반영 루프는 plugin 복사 게이트의 **일반화**다. 다음은 재론 없이 그대로 승계한다:

| ID | invariant | plugin_install 근거 |
|----|-----------|---------------------|
| **I1** | **자동 반영 금지** — 명시 사람 트리거 엔드포인트에서만 호출(auto-dispatch 경로 호출 0) | C-1 (`plugin_install.py:7-8`) |
| **I2** | source = `work_root` 하위 realpath (격리 경계, symlink escape 차단) | C-3 (`:105-113`) |
| **I3** | target = realpath 화이트리스트 (traversal·밖 경로 거부) | C-1 (`:115-122`) |
| **I4** | 반영 전 트리 전수 검사 — symlink 거부 + 민감 파일명 fail-closed | C-3 (`_audit_tree :73-87`) |
| **I5** | **preview 필수** — 반영 전 diff 표시(RedactionFilter scrub) | plugin preview(`plugin_routes.py:110-135`) |
| **I6** | fail-closed + 부분 반영물 정리(잔존 0) | `:139-144` |
| **I7** | 반영 ≠ 배포/활성화 (해당 시 분리 단계) | C-4 (`:149-176`) |

> 이 7개는 합의 *대상이 아니다*(이미 합의·구현 검증됨). 합의는 아래 §3 결정 포인트만.

---

## 3. 결정 포인트 — 사용자 + 3+1 합의 영역 (후보 제시, 결정 0)

### D-1. 반영 **단위** — 무엇을 반영하나?
| 후보 | 설명 | 적합 | 트레이드오프 |
|------|------|------|-------------|
| **A. diff/patch** | 워커 변경분을 `git diff`로 추출 → `git apply` | 기존 파일 *수정* | 대상이 git repo여야. 충돌 처리 필요 |
| **B. 파일 전체 복사** | plugin install 동형(트리 복사) | *신규* 파일/디렉토리 | 기존 파일 덮어쓰기 위험(I3 덮어쓰기 금지와 충돌) |
| **C. 둘 다(산출물 종류로 분기)** | diff면 apply, 신규면 복사 | 일반 | 복잡도↑, 첫 슬라이스엔 과함 |

### D-2. 반영 **대상 범위** — 어디에 쓸 수 있나? ★ 최대 위험
| 후보 | 설명 | 안전성 |
|------|------|--------|
| **A. 등록된 외부 프로젝트 repo만** | `external_registry`에 등재된 localhost 프로젝트 경로 화이트리스트 | 높음(provenance 연계, 기존 등록부 재사용) |
| **B. 명시 화이트리스트 디렉토리** | 설정에 반영 가능 루트 N개 명시 | 중간 |
| **C. install 시 대상 지정 + realpath 검증** | 사용자가 매번 대상 지정, 화이트리스트 교집합 | 중간(UX↑, 실수 여지) |

### D-3. 반영 **메커니즘**
| 후보 | 설명 | 전제 |
|------|------|------|
| **A. git apply** | 대상이 git repo, patch 적용 | git 의존, 충돌=fail-closed 거부 |
| **B. shutil 복사** | plugin install 그대로 | 신규만, 덮어쓰기 금지 |
| **C. 파일별 write(allowlist 경로)** | 경로별 검증 후 기록 | 가장 일반적이나 검증 표면 큼 |

### D-4. **승인/preview 모델**
- plugin install의 `preview(diff scrub) → 사람 승인 → install` 게이트를 **그대로 재사용**할지,
  diff 기반(git diff)으로 신규 preview를 만들지.
- I5 비협상이므로 "preview 있음"은 확정, *형태*만 결정.

### D-5. **첫 슬라이스 (MVP) 범위** — 가장 작고 안전한 조각
권고 후보(검토용, 결정 아님):
> **slice-app-1** = "등록된 외부 프로젝트 repo(D-2 A) 1개에, 워커가 만든 **diff/patch**(D-1 A)를,
> preview(git diff) → 1-클릭 사람 승인 → `git apply --check` 통과 시에만 적용(D-3 A).
> 충돌·검증 실패 = fail-closed referred. 적용 후 자동 commit/push 0(I7)."
- 이유: external_registry provenance + git apply --check(드라이런)가 가장 안전한 first cut.
  덮어쓰기 위험(B)·임의 경로(C-write)를 첫 슬라이스에서 회피.

---

## 4. 합의 형태 권고

- **유형**: 아키텍처 + **보안** 변경 → CLAUDE.md §3 매트릭스 **3+1 풀 합의 필수**.
- **합의 안건(D 값 고정 후 잔여)**:
  1. **D-2 안전성 적대적 검증** — "등록 외부 repo만 + git apply"가 자비스 권한 확장의 안전 경계로 충분한가? (Agent C: 우회 표면 — registry 변조·repo 경로 symlink·apply가 repo 밖 파일 건드리는 patch / Agent B: 엣지케이스)
  2. **Q-b git apply 충돌 정책** — 거부만(fail-closed) vs 3-way merge 시도?
  3. **Q-d 산출물 식별** — workdir 전체 diff vs 워커 명시 파일 목록? (격리 workdir → diff 추출 메커니즘)
- **invariant I1~I7은 합의 안건 아님**(답습 확정). **D-1·D-2·D-3·D-4·D-5 값도 고정**(사용자 검토 완료).
- 합의 후 → TDD(RED→GREEN→REFACTOR) → 실 e2e dogfood → PR(develop 베이스).

## 5. UI 컨펌 (선행 의무 — `[[feedback_ui_design_confirm_first]]`)
반영 승인 UI(preview 패널·diff 표시·1-클릭 게이트)는 구현 *전* mockup 사용자 컨펌 필수.

## 6. 미해결 질문 (검토 시 사용자 입력 요청)
- Q-a. 첫 대상 = 어느 외부 프로젝트? (voice_lab repo가 dogfood 후보?)
- Q-b. git apply 충돌 시 정책 = 거부만(fail-closed) vs 3-way merge 시도?
- Q-c. 반영 후 git commit까지 자비스가? 아니면 apply만(작업트리 변경)하고 commit은 사람?
- Q-d. 워커 산출물에서 "무엇이 반영 후보인가"를 어떻게 식별? (workdir 전체 diff vs 명시 파일 목록)
