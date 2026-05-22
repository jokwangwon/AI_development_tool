# 3+1 합의 보고서 — Jarvis 오케스트레이터 MVP brief (DRAFT v1)

**작성일**: 2026-05-22
**대상**: `docs/phase0/jarvis-orchestrator-mvp-design-brief.md` (DRAFT v1)
**프로토콜**: 3+1 멀티 에이전트 합의 (CLAUDE.md §3) — Agent A/B/C 독립 병렬 분석 → Reviewer 교차 비교
**판정 분포**: A=APPROVE WITH CONDITIONS · B=REVISE · C=APPROVE WITH CONDITIONS
**최종 판정**: **REVISE**

---

## Phase 2 — 독립 분석 요약

### Agent A (구현 분석가) — "실제로 동작하는가?" → APPROVE WITH CONDITIONS
- **A-1**(관찰→권고): V-1 이미 상당 de-risk. 머신에 CUDA 13 toolkit(nvcc) 설치·sm_121·aarch64. 2026 현황: llama.cpp sm_121+ARM64+CUDA13 동작, Ollama NVIDIA 파트너십 GB10 out-of-box. brief §2가 V-1 과대평가.
- **A-2**(BLOCKING): vLLM은 GB10 sm_121 aarch64 미동작(vllm #36821). Q-2에서 제외 → Ollama vs llama.cpp.
- **A-3**(BLOCKING): GB10 bandwidth-bound(~273GB/s LPDDR5X). dense 70B = 한자릿수 tok/s. Q-1을 MoE/30B이하+양자화로 재조준 + "tok/s 실측" 기준.
- **A-4**(권고): 완료감지가 최난점. CAO 실제는 ".done"이 아니라 provider별 startup marker + idle-pattern watchdog + inline-mode 강제. §4④/Q-3 재기술. CAO 차용 전제라 BLOCKING→권고.
- **A-5**(관찰): provider 추상 쉬움. Q-5 자동감지는 표준신호 없어 fragile → "MVP=수동/설정" 분리가 정확.
- **A-6**(관찰): 자가진화 게이트 구현가능, MVP 밖 적절.
- **A-7**(권고): §5 누락 — (1) 사장 호출 추상(사장도 liquidity 대상), (2) 워커 작업디렉터리/git 격리.
- **A-8**(관찰): CAO Apache-2.0/py3.10+/tmux3.3 정합.

### Agent B (품질/안전성 검증가) — "안전하고 견고한가?" → REVISE
- **B-1**(BLOCKING): 자가진화 게이트 "테스트/게이트 자체 조작" 구멍. self-change 범위에 tests/·hooks·CI config·§8문서 포함 여부 미정의 = green washing = 거짓 안전감. immutable zone 명시 필요.
- **B-2**(BLOCKING): 워커 신뢰 경계 부재. 워커=사용자 권한 실행(전체 FS/네트워크). blast radius·출력검증·권한경계 0건. 사장의 무비판 수용 → prompt injection 체인. 적용 위협(에이전트 실수+공급망) 주공격면을 비움.
- **B-3**(권고): provider fallback silent 품질저하 + egress 미정의(claude→GLM 동일 프롬프트가 타 클라우드로) + 로컬 fallback 워커 부재(토큰 소진=정지, §0 "인터넷 비종속" 비전 충돌).
- **B-4**(관찰): 비례성 과잉배제측 양호, 부족측 — 적용위협 최소방어조차 비움. §8 "게이트로 충분" 미입증.
- **B-5**(권고/관찰): D-3↔§0 긴장. 메타포 "사장↔워커 의논=3+1 자동화" 위험(단일 사장=독립성 없음=단일실패점). Q-8 D-5에서 이미 결정. Provider Liquidity always-on 로컬 워커 경로 MVP 부재.
- **B-6**(BLOCKING): §5 thin=unsafe. 워커 출력검증·권한제한이 "범위 밖"으로도 명시 안됨(누락). MVP 자체가 워커에 실행권한 부여 → 워커 실행경계는 첫 실행 전제. 최소 결정적 가드면 충분.

### Agent C (대안 탐색가) — "더 나은 방법은?" → APPROVE WITH CONDITIONS
- **C-1**(검토필요): D-1 "사장=로컬LLM 직접지휘" 재검토. 오케스트레이션 대부분=결정적 배관. 순수(a)는 hop마다 LLM 지연+비결정성(TDD 곤란). **하이브리드(결정적 배관+판단지점만 LLM)** = CLAUDE.md "계산적 우선"과 동형.
- **C-2**(채택권고): tmux send-keys 대신 **headless `claude -p --output-format json`/`codex exec`** → 함정 회피 + json이 완료신호+출력+`total_cost_usd` 반환(Q-3·Q-5 공짜) + exit code=결정적 완료. tmux=관전용 래퍼. §3 "tmux 강제" 과장 — subprocess도 Provider Liquidity 충족.
- **C-3**(검토필요): CAO 단독비교=조사편향. multi-agent-shogun(file-queue, zero coordination cost) 더 가벼움. 차용원 CAO+shogun cherry-pick(단 feudal 메타포 주의).
- **C-4**(채택권고): V-1을 Ollama 단독으로 좁힘(vLLM 미지원). Ollama OpenAI-호환 endpoint로 사장·워커 통일. Q-4 Worker 인터페이스=CLI+endpoint 백엔드 수용.
- **C-5**(채택권고): Q-7에 "Layer 0: 메모리누적(read-only 학습)"을 프롬프트갱신 앞에. 코드변경0·게이트불요·최안전. ADR-011 T1/T2/T3 정합. 3단(메모리→프롬프트→코어), MVP=Layer0만.
- **C-6**(검토필요): 2단계 MVP — MVP-0(claude 사장+headless배관+게이트) → MVP-1(사장만 로컬LLM 교체, V-1통과후). V-1 블로킹 분리. SQLite 과설계(MVP제외).

---

## Phase 3 — 교차 비교

### ① 일치 (Consensus)
- **CON-1**: vLLM 제외(A-2+C-4, #36821) → Ollama/llama.cpp 2파전. **확정 채택.**
- **CON-2**: Q-5 자동감지 MVP 제외, 수동/설정 정확(A-5+C+B-3 무반대). **brief 유지.**
- **CON-3**: 자가진화 루프 발효 MVP 밖(A-6+B+C-5). **유지** (단 B-1 게이트 *정의* 명문화).
- **CON-4**: Python/CAO provider 추상 차용 정합(A-8+C-4). **Q-8 → "확정(Python)" 강등**(B-5).

### ② 부분 일치 (Partial)
- **PAR-1**: 워커 신뢰경계/디렉터리 격리 — B-2/B-6(BLOCKING)+A-7(권고) **수렴**, C 무관(반대근거 없음). → **BLOCKING 인정.** 비례성 위반 아님(신규 인프라 불요, 격리 작업디렉터리+무비판수용 금지 = 계산적 가드).
- **PAR-2**: D-1 단일사장 비결정성/단일실패점 — C-1(하이브리드)+B-5(메타포 정정) **수렴**. → **둘 다 채택.** D-1 하이브리드 재정식화 + §0.1 "3+1 자동화" 매핑 삭제.

### ③ 불일치 (Divergence)
- **DIV-1 ★최대 분기**: 완료감지/통신 — A-4(CAO 차용으로 해결) vs C-2(headless subprocess로 회피). → **C-2 우선 채택, A-4 fallback 보조.** 근거: (1) exit code+json=결정적 = CLAUDE.md "계산적 우선" 부합(A-4 idle watchdog=추론적, 후순위). (2) A-4 실패모드(ANSI/alt-screen/idle오탐/출력잘림)는 전부 화면 스크래핑 발생 → headless가 공격면 제거. (3) json `total_cost_usd`=Q-5 비용신호 공짜. **단** headless 미지원 provider는 A-4 watchdog fallback, tmux=관전 래퍼. §3 "tmux 강제" 정정.
- **DIV-2**: 차용원 CAO 단독 vs CAO+shogun(C-3). → **보류**(검토 항목). DIV-1로 통신이 headless면 file-queue/SQLite 자체 MVP 필요성 약화. MVP=CAO provider 추상만, shogun=후속 메모.

### ④ 누락 (Gap)
- **GAP-B1**(B-1, BLOCKING): immutable zone(tests/·게이트·hooks·CI·§8문서 = self-change 제외). → §8 명문화. 신규 인프라 0.
- **GAP-A1**(A-7): 사장 호출 추상(Ollama OpenAI-호환). C-4 수렴. → §5/Q 추가.
- **GAP-B3**(B-3): 로컬 fallback 워커 부재 + egress 미정의. → §0 명시적 한계 기록.
- **GAP-C5**(C-5): Layer 0 메모리 학습. → Q-7 추가.
- **GAP-C6**(C-6, A-1 수렴): 2단계 MVP, V-1 비블로킹. → §5 단계 분리.
- **GAP-A3**(A-3, BLOCKING): GB10 bandwidth-bound. → §2/Q-1 정정(물리 사실, 이견 불가).

### ④-G Reviewer 직접 검증
- nvcc 13.0 설치·sm_121·aarch64 확인 → A-1 사실. §2 CUDA toolkit 보유 누락 정정 필요.

---

## 최종 판정: REVISE

**한 줄 요약**: 비전·제약·차용 전략 골격은 건전하고 구현 진입 가치 충분하나, 2개 BLOCKING(워커 신뢰경계 PAR-1, immutable zone GAP-B1) + 물리 정정 1개(대역폭 GAP-A3) + 통신 재정식화(DIV-1)가 v1 미반영. **모두 신규 인프라 없이 텍스트 수정으로 해소 가능** → REJECT 아닌 REVISE.

**판정 논리**: A·C의 APPROVE W/COND = "조건 충족 시 진입", B의 REVISE = "적용 위협 최소방어 부재로 §8 미입증". B의 BLOCKING 2건이 A-7과 수렴·반박 없음 → **B의 REVISE가 가장 보수적·정확**. 모든 BLOCKING이 수정으로 해소 가능 → REVISE.

---

## brief v2 修正 권고 (12개, 🔴=BLOCKING 게이트)

1. 🔴 **§2**: CUDA 13 toolkit(nvcc)+sm_121+aarch64 추가. "70B 양자화 가능"→대역폭(~273GB/s) 기준 재기술(dense 70B=한자릿수 tok/s 경고). (GAP-A3, ④-G)
2. 🔴 **§7·Q-2**: vLLM 제외(#36821), Ollama/llama.cpp 2파전. V-1 "toolkit 보유로 부분 de-risk, 잔여=런타임 PoC". (CON-1, A-2, C-4)
3. 🔴 **Q-1**: 대역폭 적합형(MoE: Qwen3-A3B/A10B급, 또는 30B이하+양자화) 재조준 + "tok/s 실측" 기준. (GAP-A3)
4. **Q-3·§3·§5**: headless subprocess(`claude -p --output-format json`, exit code=결정적 완료신호 + json 출력/비용) 1급 격상. tmux=관전 래퍼 강등, watchdog=headless 미지원 fallback. §3 "tmux 강제"→"subprocess도 Provider Liquidity 충족" 정정. (DIV-1, C-2, A-4)
5. 🔴 **§5·신규 Q-9**: 워커 격리 작업디렉터리(+git worktree) + 사장의 워커 출력 무비판 수용 금지(최소 결정적 가드)를 MVP 첫 실행 전제로 명문화. (PAR-1, B-2/B-6, A-7)
6. 🔴 **§8**: immutable zone(tests/·게이트·hooks·CI config·§8문서 = self-change 제외) 추가. (GAP-B1, B-1)
7. **D-1·§0.1**: 하이브리드(결정적 배관+판단지점만 LLM) 재정식화 + §0.1 "3+1 자동화" 매핑 삭제. (PAR-2, C-1, B-5)
8. **§5·Q-4**: 사장도 provider 추상 대상(Ollama OpenAI-호환). Worker=CLI+endpoint 백엔드 수용(역할 차이 주석). (GAP-A1, A-7, C-4)
9. **§5**: MVP-0(claude 사장+headless+게이트+워커격리)/MVP-1(로컬 사장 교체) 단계 분리. 비전 시연=MVP-1. SQLite=MVP-0 밖. (GAP-C6, A-1, C-6)
10. **Q-7**: "Layer 0: 메모리 누적(read-only 학습)" 프롬프트갱신 앞에. ADR-011 T1 정합. (GAP-C5, C-5)
11. **§0**: MVP 워커 전부 클라우드 = "인터넷 비종속" 비전 간극을 명시적 한계로 기록. egress 인지. (GAP-B3, B-3)
12. **Q-8·§4**: Q-8 "확정(Python)" 강등. §4에 shogun file-queue=후속 다중워커 검토 메모. (CON-4, DIV-2, B-5, C-3)

**구현 진입 게이트**: BLOCKING 항목(1·2·3·5·6) 반영 = 필수. 나머지(4·7·8·9·10·11·12) = 강력 권고. v2 작성 후 사용자 승인 → 재합의 또는 TDD 구현.

**범위 한정**: 본 합의 = "구현 진입 가능 여부 + 수정 사항" 판단. 코드/모델 결정(Q-1)/런타임 설치(V-1)는 별도 승인 단계.
