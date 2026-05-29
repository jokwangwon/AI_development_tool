# 3+1 합의 — Agent C (대안 탐색가) — jarvis 협업 오케스트레이션 brief

**일자**: 2026-05-29 · **관점**: "더 나은 방법이 있는가?" (대안·트레이드오프·업계 패턴)
**대상**: `docs/phase0/jarvis-collaborative-orchestration-design-brief.md` (DRAFT v1)

---

## Agent C 분석 (대안)

**전제**: 현 dispatch = 사실상 workflow 식 1-step. boss(_advise)는 제어흐름에 안 들어감(제어권 0). brief D-1 은 이 0을 깨고 boss 를 제어루프에 끌어들이는 방향 전환. 평가 축 = "이 전환이 필요한가, R2 정신을 협업까지 연장하는 길이 있는가".

### 대안 1 — Workflow 식 결정적 오케스트레이션 (boss=분해만)
boss 가 DAG 1회 생성, 이후 실행/순서/환류는 결정적 코드. **장점**: D-3(제어루프 injection) 숙제 제거(루프 없음), dispatch 결정성 N-노드 확장, 약한 boss 호출 횟수↓. **단점**: 동적 적응 약(단 L4 = brief 범위 밖). **부분 차용(강하게)** — production 표준 실체(LangGraph)가 이 형태.

### 대안 2 — Blackboard (워커 공유 레저, boss 최소)
**기각** — 격리(§6①) 충돌 심화, 비결정적 polling, injection 횡전파, 비례성 위반. boss 빼면 "흐름 이해" 주체 소멸.

### 대안 3 — Plan-then-Execute (boss 1회 계획 → 사람 승인 → 결정적 실행)
boss 전체 계획(DAG+노드 prompt) 1회 → 사람이 계획 *전체* 1회 승인 → 결정적 executor 중간 boss 호출 0. **장점**: 대안1 injection 면역 + 게이트 피로(§6③) 구조적 해소(게이트=계획1회), ApprovalGate 위치 이동만, 사람 승인 계획=명시 작업그래프=공유맥락. **단점**: 실행중 실패 재계획에 사람 1회(단 "인간 통제 하 협력자" 정합). **채택(최우선)** — brief 가 버린 3권분립의 합리적 버전.

### 대안 4 — injection 루프 회피
brief §3 (a)(b)(c)는 "루프 존재" 전제 완화책. 대안1/3 은 루프를 안 만들어 불필요화. CLAUDE.md §2("불가능하게 만들어라") 부합. **채택**.

### 대안 5 — 공유 맥락 표현
JSONL(brief) 적정 / SQLite 과함(기각) / 파일공유디렉터리 격리충돌. **권고: JSONL 영속 + frozen 작업그래프 dataclass(런타임)** — 워커가 읽는 건 raw JSONL 아닌 결정적 구성 plan 객체(injection·이해도 양립).

### 대안 6 — L3 협상 → 계약 고정 (contract-first)
boss 가 인터페이스 계약(API schema)을 명시 산출물로 **먼저 고정** → 백엔드/프론트 워커 *양쪽 입력*으로 결정적 주입. 워커간 통신 0. **채택(강하게)** — "협상"→"계약 고정"이면 L3 위험(워커간통신, 쟁점②) 대부분 증발. OpenAPI 우선설계 = 인간팀 표준.

### 대안 7 — 업계 참고
LangGraph(graph=결정적 제어흐름, 노드만 LLM) 차용 / AutoGen 자유대화 기각 / CrewAI sequential 차용·hierarchical manager 위임 제외 / Swarm handoff 대상집합 결정적 제한만. **공통 골격 = "제어흐름은 코드, LLM은 노드, 상태/계약은 명시 객체"**. brief 가 D-1 지지로 인용한 도구들이 실제론 대안1/3 지지.

### 대안 8 — 단계화
brief L1(레저+통제)은 협업과 독립. **더 작은 첫 디딤돌**: 디딤돌0(JarvisTaskBoard 영속화+interrupted, 협업0, 즉시가치) → 디딤돌1(plan-then-execute+contract-first, L2·L3 압축). **L1 을 둘로 쪼갤 것**.

## 가장 강력한 대안
**Plan-then-Execute + Contract-First DAG** (대안3+1+6): boss 가 작업그래프+계약 schema 1회 → 사람 1회 승인 → 결정적 executor(중간 boss 0, 워커간 통신 0). boss 워커출력 관여 = 사람용 advisory 만.
- brief 최대 숙제 D-3 *발생 안 함*(루프 없음). 쟁점③ 닫음. 쟁점② 축소. R2 글자그대로 연장. 현 코드 재사용↑. 업계패턴 일치.
- trade-off: 자율 재계획 포기 — 단 "인간 통제 하 협력자" 정합, L4=프라이데이로 이미 밀림.

## 권고
1. D-1 → plan-then-execute(boss=계획1회) 수정. 인용 도구가 실제로 이 모델.
2. D-3 → 루프를 안 만들어 불필요화. R2 글자그대로 연장.
3. L3 → contract-first 계약 고정. 워커간 통신 금지 불변식.
4. 단계화 → 통제·히스토리 먼저 독립 출하.
5. 공유맥락 → JSONL + frozen 작업그래프. SQLite/blackboard/파일공유 기각.
6. 유지: §4(means/ends)·§5(JSONL)·§6①·§7 비례성 — 대안과 충돌 없고 오히려 강화.

핵심: 같은 사용자 요구(분담·흐름이해·인터페이스 조율)를 "제어를 결정적 코드에, boss 는 계획·계약만 1회"로 충족하면 brief 최대 숙제가 *문제로 존재하지 않음*.
