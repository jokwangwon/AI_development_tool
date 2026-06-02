# jarvis_hud/plugins — 플러그인 디렉터리

> 설계: `docs/phase0/jarvis-plugin-architecture-design-brief.md` (v2)
> 합의: `docs/review/3plus1-consensus-2026-06-01-jarvis-plugin-architecture.md`

각 플러그인 = `<name>/` 폴더 + `plugin.json`(manifest 데이터) + `panel.js`(프론트 패널)
\+ 선택적 `routes.py`(백엔드 라우트, `make_routes(ports)` 노출).

## ⭐ 탐색 ≠ 활성화 (BLOCKING C-4 — self-mod 우회 차단)

폴더에 plugin 을 **drop-in 한다고 자동 활성화되지 않는다.** 활성화는 이 디렉터리의
`enabled.json` 에 name 을 **명시 등록**해야 한다(사람 게이트). 등록되지 않은 플러그인은
탐색은 되지만 라우트/패널이 로드되지 않는다.

```json
// enabled.json
{ "enabled": ["tts_compare"] }
```

## manifest (plugin.json) 형식

```json
{
  "name": "tts_compare",            // 폴더명과 일치 필수 (스푸핑 차단)
  "title": "TTS 비교",
  "panel_js": "panel.js",           // 폴더 안 단일 파일명 (traversal 차단)
  "icon": "🔊",
  "routes_module": "jarvis_hud.plugins.tts_compare.routes",  // 선택 (백엔드 없으면 생략)
  "permissions": ["measurement:write", "conversation:read"]  // 화이트리스트만 (최소권한)
}
```

허용 권한: `conversation:read`, `measurement:read`, `measurement:write`
(`src/jarvis/plugin_registry.py:ALLOWED_PERMISSIONS`). 선언한 권한의 capability 포트만
주입된다(미선언=미접근).

## 등록 절차 (B 복사 게이트 — 단계3에서 코드 강제 예정)

격리 work 에서 claude 워커가 플러그인 3요소를 구축 → 사람이 diff 검토 → 이 디렉터리로
복사 → `enabled.json` 에 등록 → 자비스 **재시작** 시 활성.
