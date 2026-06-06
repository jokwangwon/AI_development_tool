# 3+1 합의 보고서 — 워커 산출물 반영 루프 (slice-app-1)

> **일자**: 2026-06-06 · **브랜치**: `feature/jarvis-output-application-loop`
> **안건 기준**: `docs/phase0/jarvis-output-application-loop-brief.md` §4 (D 값 고정 후 잔여 3안건)
> **합의 결과**: **REVISE** — 확정 방향 지지 + **BLOCKING 7건 흡수**(특히 CB-1 patch_validator 신규).
> **프로토콜**: CLAUDE.md §3 (보안 변경 = 3+1 풀 합의 필수). Phase 2 독립 분석 → Phase 3 교차 → Phase 4 합의.

> **답습**: `src/jarvis/plugin_install.py`(C-1/C-3/C-4) · `[[3plus1-consensus-2026-06-01-jarvis-plugin-architecture]]` · brief §2 invariant I1~I7 · `[[feedback_proportionate_security_personal_tool]]` · `[[feedback_pass_scope_overclaim]]`

---

## 0. 안건

| ID | 안건 | 사용자 고정값(brief) |
|----|------|---------------------|
| D-2 | "등록 외부 repo만 + git apply" 안전 경계 충분성 | 대상 = 등록 외부 repo만 |
| Q-b | git apply 충돌 정책 | 미정(합의 대상) |
| Q-d | 워커 산출물 식별 | 미정(합의 대상) |

invariant I1~I7, D-1/D-3/D-4/D-5 = 답습/고정(합의 대상 아님).

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus) — 3개 독립 수렴
| 항목 | A(구현) | B(안전) | C(대안) |
|------|---------|---------|---------|
| **Q-b = fail-closed 거부** (3-way merge 금지) | ✓ 단순·견고 | ✓ 부분적용 회피·안전 | ✓ I1/I5 답습·최적 |
| **D-2 메커니즘 = git apply** (worktree/3-way는 후속) | ✓ 의존성 최소 | ✓ 안전 가능 | ✓ 더 나은 대안 없음 |
| **plugin_install 패턴 재사용** (realpath 화이트리스트·_within·fail-closed) | ✓ | ✓ | ✓ |
| **external_registry 쓰기 차단** (워커 자기대상 등록 불가) | ✓ 리스크 지적 | ✓ BLOCKING | (암묵) |

### ② 불일치 (Divergence) — Q-d 산출물 식별 (2 vs 1)
| 입장 | 주장 | 근거 |
|------|------|------|
| **A·C: workdir 전체 diff** | `git init→git add -f→git diff` 추출, `_audit_tree` 재사용 | 워커 구현 단순, plugin_install 답습, 새 코드 최소 |
| **B: 명시 파일 목록** | `WorkerResult.output_files` 추가, 그것만 diff | workdir 전체는 의도 외/민감 파일 포함 위험(HIGH) |

### ③ 갭 (Gap) — 특정 에이전트 단독
| 출처 | 발견 | 중요도 |
|------|------|--------|
| **B 단독** ★ | `git apply --check`는 **문법만 검증, 의미 검증 안 함** → patch 내용 화이트리스트 검증(신규 모듈) 필수. plugin_install C-3 그대로 재사용 **불가** | **CRITICAL** |
| **B 단독** | patch가 `.git/` 수정·symlink(mode 120000) 생성·민감파일 수정·traversal(`a/../../`) 가능 | CRITICAL |
| **A 단독** | apply 전 대상 repo 상태 검증(`git status --porcelain` clean) 필요 | 견고성 |
| **A 단독** | Landlock 격리 시 git binary 접근(`ro_paths += /usr/bin/git`) | 구현 디테일 |
| **C 단독(실측)** | registry.json에 voice_lab 등록(origin jarvis), 실 repo `/home/delangi/voice_lab`=git repo. **단 repo 경로 필드 없음** → 별도 화이트리스트 필요 | scope |

---

## Phase 4 — 합의 도출

### 결정 1 — Q-b = **fail-closed 거부** (만장일치 채택)
- `git apply --check` 실패 = 거부(referred). **3-way merge 금지**. apply 실패 시 작업트리 부분 변경 정리(I6).
- 근거: A·B·C 독립 수렴. plugin_install fail-closed(`:139-144`) 답습.

### 결정 2 — Q-d = **workdir 전체 diff 채택** (불일치 해소: 2:1, B 우려는 BLOCKING 흡수)
- **채택**: workdir 전체 diff(A·C) — 워커 구현 변경 0, 첫 슬라이스 단순성.
- **B의 우려(의도 외/민감 파일)는 거부하지 않고 BLOCKING으로 흡수**: ① `_audit_tree` 전수검사(symlink/민감파일 fail-closed) ② patch_validator 민감파일 거부 ③ preview(I5) 육안. → **3중 방어로 B의 HIGH 위험을 LOW로 강등**.
- **명시 파일 목록(B안)은 V-1 opt-in DEFER** — "워커가 명시할 때만 그것만 반영" 모드로 후속 추가 가능(A·C도 동의).

### 결정 3 — D-2 = git apply 채택, **단 patch_validator 신규 필수** (B의 CRITICAL 갭 정면 흡수)
- "등록 외부 repo만"은 안전 경계로 **필요하나 불충분**. git apply는 patch 의미를 검증하지 않으므로 patch 내용 검증이 **반드시** 추가돼야 한다.

### BLOCKING 조건 (구현 전 필수 — TDD RED에서 검증)
| ID | 조건 | 출처 |
|----|------|------|
| **CB-1** ★ | **`patch_validator.py` 신규** — git apply 전 patch 텍스트 검증: (a) 각 대상 경로 normalize 후 **repo realpath 하위**(traversal 차단) (b) **`.git/` 거부** (c) **symlink(`mode 120000`) 거부** (d) **민감파일명 거부**(`_SENSITIVE_NAMES`/`_SENSITIVE_SUFFIXES` 재사용). 위반=fail-closed reject | B |
| **CB-2** | **반영 대상 화이트리스트** — repo 경로를 realpath+화이트리스트 검증(`_within` 재사용). **쓰기 경로 0**(워커/코드가 화이트리스트에 등록 불가, 사람 수동 편집만) | A·B·C |
| **CB-3** | **fail-closed** — apply --check 실패=거부, 3-way 금지, 실패 시 작업트리 정리 | 만장일치 |
| **CB-4** | **apply 전 대상 repo clean 검증** — `git status --porcelain` 비어있지 않으면 referred(미완 merge/dirty 위 적용 금지) | A |
| **CB-5** | **preview = RedactionFilter scrub** (I5) + diff 육안. plugin preview(`plugin_routes.py:131`) 재사용 | 만장일치 |
| **CB-6** | **I1 자동 반영 금지** — 명시 사람 트리거 엔드포인트만(same-origin), auto-dispatch 호출 0 | 만장일치 |
| **CB-7** | **I7 apply ≠ commit** — 자비스는 작업트리 변경까지, git commit/push는 사람. 코드 주석 명기 | 확정 |

### 권고 (합의, 비-BLOCKING)
- **첫 대상 = voice_lab**(`/home/delangi/voice_lab`, C 실측). Q-a 해소 후보 — 사용자 최종 확정 필요.
- **diff 추출 = 자비스가 workdir을 git 초기화** 후 `git add -f . → git diff --cached`(A). `_audit_tree`로 전수검사 선행.
- Landlock 경로면 git binary RO 노출(A).
- **UI preview mockup 컨펌 선행**(brief §5, `[[feedback_ui_design_confirm_first]]`).

### DEFER (후속 슬라이스)
- 명시 파일 목록(Q-d B안) = V-1 opt-in · reject 브랜치(Q-b C 대안②) = V-1 · git worktree 격리(Q-d C 대안③) = V-2 보안 재검증 후 · 3-way merge = MVP 이후.

---

## 합의 결론

**REVISE** — 확정 방향(등록 외부 repo + git apply + fail-closed + workdir diff)을 **지지**하되,
brief에 누락된 **CB-1 patch_validator(B의 CRITICAL 발견)를 비협상 BLOCKING으로 추가**한다.
git apply의 "문법만 검증" 한계가 핵심 위험이며, plugin_install C-3는 출발점(workdir) 검증만 하므로
**도착점(patch가 repo에 무엇을 하는가)을 검증하는 신규 게이트가 반드시 필요**하다.
BLOCKING CB-1~CB-7 충족 시 안전 경계는 plugin_install 수준 이상. 다음 단계 = 사용자 BLOCKING 확인 → (UI mockup 컨펌) → TDD.
