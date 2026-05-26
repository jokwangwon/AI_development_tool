## Cross-vendor Blind 검토 응답

* **응답자 vendor**: GPT-5.5 Thinking
* **응답 일자**: 2026-05-14
* **검토 범위**: 업로드된 Backlog #3 T3 영역 6 sub-영역 통합 진입 결정 사전 검토 문서 기준. 본 문서는 3 Group × 6 질문 + 종합 1 질문, 총 19개 질문에 대한 독립 판단을 요청하고 있으며, 응답은 풀 3+1 합의의 입력으로만 사용되는 것으로 정의되어 있습니다. 

---

# 종합 선판정

**최종 판정: C) PARTIAL — Group α 우선 진입, Group β는 정책/감사 모드 한정 진입, Group γ는 ST-1과 ST-4를 분리하여 ST-4는 MVP-6 이후로 보류 권고**

권고 우선순위는 다음입니다.

1. **Group α — AR-3 + PC-4 T3 sub**
   진입 가능. 단, 실제 강제 적용은 Backlog #6 Runtime + CI-hook implementation과 연결해야 합니다.

2. **Group β — T-5 β + Tier-2/3 catalog 일반**
   정책 합의는 진입 가능. 하지만 Tier-2/3 hard-block catalog 확장은 Implementation Evidence PASS 전에는 보류해야 합니다. 우선은 **audit/warn-only**가 적절합니다.

3. **Group γ — C-5b ST-1 + Vault HSM ST-4**
   현재 그룹 묶음은 과도합니다. **ST-1은 제한적/다운스트림 preflight 형태로 검토 가능**, **Vault HSM ST-4는 MVP-6 Operational Readiness 또는 multi-host 전환 시점까지 BLOCK/DEFER**가 적절합니다.

GitHub branch protection은 required status checks, required reviews, signed commits 같은 병합 조건을 강제할 수 있고, required status checks는 보호 브랜치 변경 전 성공/스킵/중립 상태를 요구할 수 있습니다. 따라서 `--no-verify` 우회 대응의 핵심은 로컬 hook이 아니라 원격 branch protection + CI required check입니다. ([GitHub Docs][1])

---

# Group α — AR-3 + PC-4 T3 sub

## Q1. AR-3 옵션 선택

**판정: APPROVE WITH CONDITIONS**
**권고 옵션: 초기에는 (e) CODEOWNERS + required status check, commit signing은 후속 단계**

가장 균형 잡힌 선택은 **(e) CODEOWNERS + required status check**입니다. required status check는 실제 우회 차단의 중심이고, CODEOWNERS는 AI agent 또는 자동화가 변경한 중요 경로에 인간 소유자 확인을 붙이는 장치가 됩니다. GitHub는 CODEOWNERS를 branch protection과 연결해 코드 오너 리뷰를 요구할 수 있습니다. ([GitHub Docs][2])

다만 1인 개발자 환경에서는 CODEOWNERS의 효과가 제한적입니다. “다른 사람의 리뷰”가 아니라 “중요 경로 변경을 명시적으로 다시 보게 만드는 friction”으로 봐야 합니다. 그래서 CODEOWNERS는 전체 repo가 아니라 `docs/decisions/**`, `tools/**`, `.github/workflows/**`, `.pre-commit-config.yaml`, catalog 파일 같은 핵심 경로에만 적용하는 편이 낫습니다.

**조건**

* required status check는 반드시 실제 CI scanner와 연결되어야 합니다.
* direct push / force push / admin bypass 허용 여부를 별도 결정해야 합니다.
* commit signing은 MVP-1.5 필수 조건이 아니라 MVP-6 또는 외부 contributor/PMO 전환 시점으로 미루는 것이 적절합니다.

---

## Q2. PC-4 T3 sub 옵션 조합

**판정: APPROVE WITH CONDITIONS**

권고 조합은 다음입니다.

* `pre-commit install`은 **README 안내 + bootstrap script + doctor check** 형태로 시작
* `default_install_hook_types`는 초기에는 `pre-commit`, `commit-msg` 중심
* `pre-push`는 heavy check가 아니라 빠른 smoke check만 허용
* `fail_fast`는 로컬에서는 `true` 권고, CI에서는 전체 리포트가 보이도록 별도 설계 가능
* `minimum_pre_commit_version`은 명시
* `--no-verify` 차단은 로컬에서 완전 차단하려 하지 말고, branch protection의 required CI로 보완

pre-commit은 각 hook 실행 환경을 관리해주는 도구이며 root 권한 없이도 hook 실행 환경을 구성할 수 있다는 장점이 있습니다. 하지만 로컬 hook은 본질적으로 개발자 우회 가능성이 있으므로, 보안 경계로 삼으면 안 됩니다. ([Pre-Commit][3])

**조건**

* 로컬 hook 실패가 개발 자체를 막지 않도록 “빠른 실패 + 명확한 복구 명령”이 있어야 합니다.
* 실제 차단은 CI required check에서 수행해야 합니다.
* PC-4 T3의 강제 install은 즉시 강제보다 opt-in → doctor warning → required check 순서가 안전합니다.

---

## Q3. AR-3 × PC-4 결합 효과

**판정: APPROVE**

우회 차단 강도는 다음 순서입니다.

1. **pre-commit 단독**: 가장 약함. `--no-verify`로 우회 가능.
2. **branch protection + required CI 단독**: 핵심 방어선. 로컬 우회와 무관하게 merge 차단 가능.
3. **pre-commit + branch protection 결합**: 가장 강함. 로컬에서는 빠른 피드백, 원격에서는 강제 차단.

따라서 PC-4는 developer experience용 1차 피드백이고, AR-3는 실제 enforcement layer입니다. 잔존 우회는 admin bypass, force push 허용, required check 미등록, GitHub token 탈취, workflow 자체 변조입니다.

---

## Q4. fork PR / `pull_request_target` 정책

**판정: BLOCK for `pull_request_target`, APPROVE for default conservative policy**

1인 개발자 환경에서는 `pull_request_target`을 도입하지 않는 것이 적절합니다. GitHub는 `pull_request_target`에서 신뢰할 수 없는 코드를 실행하면 cache poisoning, write 권한 또는 secrets 노출 같은 보안 문제가 생길 수 있다고 경고합니다. ([GitHub Docs][4])

권고는 **default 정책 유지 + fork PR은 secrets 접근 없는 read-only 검증만 수행**입니다. 외부 contributor가 거의 없는 1인 프로젝트에서 `pull_request_target`을 쓸 실익보다 위험이 큽니다.

---

## Q5. commit signing 의무화 시점

**판정: APPROVE WITH CONDITIONS**
**권고 시점: MVP-6 Operational Readiness**

commit signing은 보안적으로 의미가 있지만, MVP-1.5에서 필수로 넣기에는 운영 비용이 큽니다. 1인 개발자에게는 GPG/SSH signing key 관리, 백업, 분실, revocation, CI bot signing 정책까지 부담이 됩니다.

권고는 다음입니다.

* MVP-1.5: 선택적 signing 권장
* MVP-6: required signed commits 검토
* Hermes PMO 격상: required signing 또는 bot signing 정책 필수 검토

GitHub에서도 protected branch에 signed commits 요구를 설정할 수 있으나, 이는 branch protection과 결합되는 운영 정책입니다. ([GitHub Docs][5])

---

## Q6. Group α 진입 부적합/차단 영역

**판정: PARTIAL APPROVE**

Group α는 **정책 합의 진입은 가능**합니다. 다만 실제 강제 적용은 Backlog #6 Runtime + CI-hook implementation 이후가 안전합니다.

**차단/보류해야 할 항목**

* PC-4 T3 hard install 즉시 강제
* pre-push heavy check 강제
* commit signing 즉시 필수화
* fork PR에 `pull_request_target` 도입

**진입 가능한 항목**

* required status check 설계
* 보호 브랜치 정책 설계
* CODEOWNERS 핵심 경로 설계
* hook stage 최소화 정책
* `--no-verify`는 로컬 차단 대상이 아니라 CI에서 보완한다는 원칙

---

# Group β — T-5 β + Tier-2/3 catalog 일반

## Q7. Tier-2/3 catalog 자동 확장 정책 일반

**판정: APPROVE WITH CONDITIONS**
**핵심 권고: 자동 확장 금지, 수동 curated catalog + audit-first**

Tier-2/3 catalog는 자동 확장하면 FP 폭증과 Provider Liquidity 약화가 동시에 발생할 수 있습니다. 따라서 정책은 다음이 적절합니다.

* Tier-1: high-confidence hard-block
* Tier-2: audit/warn-only 시작
* Tier-3: observe-only 또는 문서상 후보군
* catalog 본문: 도구 코드 내장보다 별도 `yaml/json` manifest 권고
* catalog 변경: provenance, rationale, test fixture, allowlist를 함께 요구
* hard-block 승격: Implementation Evidence PASS 이후

---

## Q8. T-5 β vendor catalog 확장 범위

**판정: PARTIAL**

현 시점에서는 **Tier-2 URL/model hard-block 확장 0건**이 적절합니다. 대신 Tier-2 후보를 audit-only로 등록하는 방향이 안전합니다.

후보군은 “유명 vendor라서 추가”가 아니라 다음 기준으로 선정해야 합니다.

* 실제 프로젝트에서 adapter로 지원할 가능성이 있음
* direct SDK/import/URL 사용이 provider adapter 우회로 이어질 수 있음
* false positive가 낮은 endpoint/model prefix를 정의할 수 있음
* allowlist 경로가 명확함

예시 후보로는 Mistral API, AI21, Stability 등은 검토 가능하지만, Stability는 이미지 모델 영역까지 범위를 넓히는 결정이므로 별도 범위 정의가 필요합니다. Inflection, Aleph Alpha 등은 실제 사용 가능성이나 adapter 대상 여부가 낮다면 Tier-3 observe-only가 더 적절합니다.

---

## Q9. LiteLLM vendor list 자동 동기화 vs 자체 catalog

**판정: BLOCK for auto-sync, APPROVE for advisory snapshot**

LiteLLM vendor list를 자동 동기화 source-of-truth로 삼는 것은 권고하지 않습니다. 외부 catalog가 변경될 때 내부 차단 정책이 자동으로 바뀌면 supply chain 위험과 예측 불가능한 FP가 생깁니다.

권고는 다음입니다.

* 내부 catalog가 단일 source-of-truth
* LiteLLM 등 외부 목록은 참고용 advisory input
* 자동 PR 생성은 가능하되 자동 merge/자동 hard-block 금지
* vendor rename/deprecation은 별도 changelog와 fixture 필요

Provider Liquidity 5-way를 보존하려면 “새 vendor를 막는 catalog”가 아니라 “adapter 경유를 강제하되 새 adapter 추가는 쉽게 하는 catalog”여야 합니다.

---

## Q10. provider lock-in 강화 역효과

**판정: APPROVE — 위험 실재, 강도 HIGH**

이 위험은 실재합니다. provider URL/model 차단을 넓힐수록 신규 vendor 실험, migration, emergency fallback이 어려워질 수 있습니다. 즉 “provider lock-in 방지 scanner”가 오히려 “provider 교체 비용 증가 장치”가 될 수 있습니다.

**완화책**

* `src/providers/**` 또는 공식 adapter 경로는 allowlist
* 실험 디렉터리 `experiments/**`는 audit-only
* Tier-2는 최소 1 cycle warn-only 후 hard-block 검토
* 예외는 expiry date와 owner/rationale 필수
* 새 provider 도입 시 adapter stub generator 제공
* direct use 차단 메시지에 “어디에 adapter를 만들면 되는지” 안내

---

## Q11. GP-3 R-4.1 catalog와 GP-5 URL/model catalog 통합 여부

**판정: APPROVE WITH CONDITIONS**

정책 frame은 통합하고, catalog namespace는 분리하는 것이 적절합니다.

* 통합할 것: tier 정의, provenance, evidence, fixture, allowlist, expiry 정책
* 분리할 것: secret pattern catalog와 provider URL/model catalog

이유는 harm model이 다르기 때문입니다. Secret scanner는 유출 방지가 목적이고, provider scanner는 architecture lock-in 방지가 목적입니다. 같은 프로세스는 쓰되 같은 파일/같은 threshold로 묶으면 안 됩니다.

Implementation Evidence PASS 전에는 hard-block 확장을 하지 않는 것이 좋습니다. MVP-1.5에서는 “정책과 schema”만 합의하는 정도가 적절합니다.

---

## Q12. Group β 진입 부적합/차단 영역

**판정: PARTIAL APPROVE**

Group β는 **정책 설계 진입은 가능**하지만, Tier-2/3 hard-block 도입은 차단해야 합니다.

**진입 가능**

* catalog schema
* tier 정의
* provenance/rationale 필드
* audit-only Tier-2 후보군
* allowlist/exception 정책

**보류/차단**

* Tier-2/3 자동 동기화
* Tier-2/3 즉시 hard-block
* LiteLLM vendor list를 source-of-truth로 채택
* Implementation Evidence 없이 FP/FN threshold 선언

---

# Group γ — C-5b ST-1 + Vault HSM ST-4

## Q13. C-5b ST-1 chmod 600 강제

**판정: APPROVE WITH CONDITIONS**

ST-1은 “Hermes upstream Dockerfile 변경”으로 바로 들어가기보다, 먼저 **downstream wrapper / entrypoint preflight / CI container test** 형태로 검증하는 것이 적절합니다.

권고 조합은 다음입니다.

* dev 환경: warning 또는 명확한 복구 안내
* CI/production-like 환경: fail-closed
* 위반 메시지: 어떤 파일이 어떤 permission이어야 하는지 명시
* upstream PR: downstream evidence 확보 후 최소 패치로 제안
* Hermes 자체를 root of trust로 보지 않고, 외부 harness가 Hermes container behavior를 검증

즉 ST-1은 좋은 방어선이지만, “Hermes가 자기 자신을 검증하니 안전하다”가 되면 안 됩니다.

---

## Q14. Vault HSM ST-4

**판정: BLOCK / DEFER**

1인 개발자 single-host 환경에서는 Vault HSM의 실효성이 낮고 운영 비용이 큽니다. 문서에서도 ST-4가 Operational Readiness / MVP-6 영역과 cross-reference 되어 있으므로, 현재 Backlog #3에서 실제 진입시키기에는 이릅니다. 

HashiCorp Vault의 HSM 지원은 외부 root key storage, automatic unseal, seal wrapping 등 운영 인프라 성격이 강하고, 일부 기능은 Vault Enterprise 또는 HCP Vault Dedicated 성격의 요구를 가집니다. 따라서 개인 single-host 템플릿의 MVP-1.5 단계에는 과합니다. ([HashiCorp Developer][6])

권고는 다음입니다.

* 현재: ADR-010 참조 유지, 구현 진입 금지
* MVP-6: Operational Readiness와 함께 재검토
* multi-host 전환 또는 PMO 격상: ST-4 필요성 재평가

---

## Q15. ST-1/ST-2/ST-3/ST-4 통합 정책

**판정: APPROVE WITH CONDITIONS**

Defense in depth와 single source-of-truth는 충돌하지 않게 역할을 나눠야 합니다.

권고 역할 분담은 다음입니다.

* **ST-3 docker secret**: 현재 주 secret injection 방식
* **ST-1 chmod/stat check**: 파일 permission preflight guard
* **ST-2 inotify sidecar**: runtime drift detection
* **ST-4 Vault HSM**: multi-host/production-grade root secret source

즉 ST-4 단독으로 모든 것을 대체하는 것도 부적절하고, ST-1~ST-4를 모두 현 시점에 강제하는 것도 부적절합니다. 환경별 canonical secret source를 명시해야 합니다.

---

## Q16. ST-4 진입 시점

**판정: BLOCK until MVP-6**

권고 시점은 **MVP-6 Operational Readiness 발효 시점 또는 multi-host 전환 시점**입니다. MVP-2 조기 진입은 과설계입니다. Hermes PMO 격상 후로만 미루는 것은 너무 늦을 수 있으므로, “PMO 격상 조건이 보이면 MVP-6에서 선검토”가 적절합니다.

single-host SPOF를 의도적으로 수용한 상태라면 HSM의 핵심 이점이 약화됩니다. 이 경우 중요한 것은 HSM보다 secret 파일 권한, docker secret, audit log, backup/restore, rotation 절차입니다.

---

## Q17. Hermes upstream 변경 경계 vs Hermes PMO 격상 경계

**판정: PARTIAL**

Hermes upstream 변경은 root of trust 침범 위험을 만듭니다. 특히 Hermes가 “자기 자신의 secret 안전성을 판단하는 주체”가 되면 Hermes ≠ root of trust 원칙이 약해집니다.

다만 ST-1 같은 최소 permission preflight는 PMO 격상 전에도 가능할 수 있습니다. 조건은 다음입니다.

* upstream 변경 전 downstream wrapper로 evidence 확보
* 외부 harness가 container behavior 검증
* image build와 runtime check를 분리
* fail-closed 조건과 dev warning 조건을 명확히 분리
* rollback 가능
* Hermes가 판단 주체가 아니라 검증 대상이라는 문구 유지

따라서 **ST-1 downstream 검증은 PMO 전 가능**, **Hermes upstream PR은 evidence 확보 후**, **PMO 격상과 자동 연결 금지**가 적절합니다.

---

## Q18. Operational Readiness PASS 경계

**판정: BLOCK before MVP-6, APPROVE at/after MVP-6**

Vault HSM ST-4는 Operational Readiness PASS 전에는 부적합합니다. Operational Readiness의 의미는 enterprise HA를 흉내 내는 것이 아니라, 1인 개발자 기준으로도 다음을 검증하는 것입니다.

* secret rotation 가능
* backup/restore 가능
* Vault 장애 시 fallback 정책
* audit log 확인 가능
* 비용과 복구 절차를 감당 가능
* single-host SPOF 수용 범위가 문서화됨

현재 single-host SPOF를 의도적으로 수용한다면, ST-4는 “지금 해야 할 보안”이 아니라 “운영 단계 전환 신호”입니다.

---

# Q19. 최종 판정

**최종 판정: C) PARTIAL**

## 그룹별 결론

| Group   | 판정                      | 권고                                                            |
| ------- | ----------------------- | ------------------------------------------------------------- |
| Group α | APPROVE WITH CONDITIONS | 우선 진입. 단, 실제 강제는 Backlog #6 CI/runtime 구현과 연결                 |
| Group β | PARTIAL                 | 정책/schema/audit-only 진입. Tier-2/3 hard-block은 Evidence PASS 후 |
| Group γ | PARTIAL/BLOCK           | ST-1은 제한적 검토 가능. ST-4 Vault HSM은 MVP-6까지 보류                   |

## prep brief 우선순위 평가

제시된 **α → β → γ** 우선순위는 대체로 적절합니다. 다만 Group γ는 하나로 묶기보다 다음처럼 나누는 것이 더 안전합니다.

* **γ-1: ST-1 chmod/stat preflight**
* **γ-2: Vault HSM ST-4**

ST-1은 비교적 작은 file permission guard이지만, ST-4는 인프라/운영/비용/PMO 경계가 모두 걸린 큰 결정입니다. 둘을 같은 합의 단위로 묶으면 ST-1까지 불필요하게 지연되거나, 반대로 ST-4가 너무 빨리 끌려올 위험이 있습니다.

## 본 brief의 주요 결함/누락

1. **branch protection 세부 설정 누락**
   direct push 금지, force push 금지, admin bypass 허용 여부, required PR 여부가 별도 결정 항목으로 필요합니다.

2. **GitHub plan/권한 제약 누락**
   private repo, branch protection, ruleset, CODEOWNERS, required reviewers 기능의 실제 사용 가능성을 확인해야 합니다.

3. **CODEOWNERS의 1인 개발자 한계**
   1인 환경에서는 CODEOWNERS가 “독립 리뷰”가 아니라 “중요 변경 재확인 friction”이라는 점을 명시해야 합니다.

4. **Tier-2/3 catalog의 예외 경로 부족**
   Provider Liquidity를 보존하려면 allowlist, expiry exception, adapter stub 생성 경로가 필수입니다.

5. **Group γ가 과도하게 묶임**
   ST-1과 ST-4는 위험 규모가 다릅니다. 별도 합의 단위가 더 적절합니다.

6. **Operational Readiness의 1인 개발자 정의 필요**
   enterprise HA가 아니라 rotation, backup, restore, audit, fallback을 기준으로 정의해야 합니다.

## 최종 권고 문장

Backlog #3 T3 영역은 **3그룹 동시 진입 APPROVE가 아니라 PARTIAL 진입**이 타당합니다. 우선 Group α를 통해 원격 enforcement의 뼈대를 세우고, Group β는 catalog hard-block이 아닌 audit-first 정책으로 진입시키며, Group γ는 ST-1과 ST-4를 분리해 ST-4 Vault HSM은 MVP-6 Operational Readiness 이후로 보류하는 것이 가장 안전합니다.

[1]: https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches?utm_source=chatgpt.com "About protected branches"
[2]: https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners?utm_source=chatgpt.com "About code owners"
[3]: https://pre-commit.com/?utm_source=chatgpt.com "pre-commit"
[4]: https://docs.github.com/actions/using-workflows/events-that-trigger-workflows?utm_source=chatgpt.com "Events that trigger workflows"
[5]: https://docs.github.com/ko/rest/branches/branch-protection?utm_source=chatgpt.com "보호된 브랜치에 대한 REST API 엔드포인트 - GitHub 문서"
[6]: https://developer.hashicorp.com/vault/docs/enterprise/hsm?utm_source=chatgpt.com "Vault HSM support overview"
