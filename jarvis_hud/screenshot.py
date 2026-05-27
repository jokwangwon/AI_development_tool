#!/usr/bin/env python3
"""JARVIS HUD 자동 screenshot 도구.

Playwright headless Chromium 으로 localhost:8765 접속 → Three.js render 대기 →
PNG 저장 → 분석용. 자비스 dogfooding 의 자연 확장 = 자비스가 자기 화면을 본다.

사용:
    python jarvis_hud/screenshot.py [out_path] [wait_ms]
"""
from __future__ import annotations

import asyncio
import os
import sys
from playwright.async_api import async_playwright

URL = "http://localhost:8765"
DEFAULT_OUT = "/tmp/jarvis_hud_screenshot.png"
DEFAULT_WAIT_MS = 4000


async def capture(out_path: str, wait_ms: int, viewport_w: int = 1600, viewport_h: int = 900) -> None:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": viewport_w, "height": viewport_h})
        page = await context.new_page()

        # console + error 캡처
        page_errors = []
        page.on("pageerror", lambda exc: page_errors.append(f"JS error: {exc}"))
        page.on("requestfailed", lambda req: page_errors.append(
            f"Request failed: {req.url} {req.failure}"))

        print(f"[1/4] {URL} 접속 ...")
        try:
            await page.goto(URL, wait_until="domcontentloaded", timeout=15000)
        except Exception as exc:
            print(f"[error] page.goto 실패: {exc}")
            await browser.close()
            sys.exit(1)

        print(f"[2/4] Three.js render + 데이터 로드 대기 ({wait_ms}ms) ...")
        await page.wait_for_timeout(wait_ms)

        print(f"[3/4] PNG 저장 → {out_path}")
        await page.screenshot(path=out_path, full_page=False)

        if page_errors:
            print(f"[!] page errors {len(page_errors)} 건:")
            for e in page_errors[:5]:
                print(f"    {e}")

        print(f"[4/4] viewport={viewport_w}x{viewport_h}, 크기 {os.path.getsize(out_path)} bytes")
        await browser.close()


def main() -> int:
    out = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT
    wait_ms = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_WAIT_MS
    asyncio.run(capture(out, wait_ms))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
