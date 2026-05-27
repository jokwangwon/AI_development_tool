#!/usr/bin/env python3
"""설정 popover 열기 + 캡처 — 인터랙션 시뮬 evidence."""
import asyncio
import sys
from playwright.async_api import async_playwright

URL = "http://localhost:8765"

async def main(out_path: str):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1600, "height": 900})
        await page.goto(URL, wait_until="domcontentloaded", timeout=15000)
        await page.wait_for_timeout(3500)
        await page.click("#gear-btn")
        await page.wait_for_timeout(500)
        await page.screenshot(path=out_path, full_page=False)
        await browser.close()
        print(f"saved {out_path}")

asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "/tmp/jarvis_settings_open.png"))
