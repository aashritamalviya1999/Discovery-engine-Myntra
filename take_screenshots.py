import asyncio
from playwright.async_api import async_playwright
import os

async def capture():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 900})
        
        await page.goto("http://localhost:8352/index.html", wait_until="networkidle")
        await page.wait_for_timeout(1000)
        
        artifact_dir = r"C:\Users\sanja\.gemini\antigravity\brain\84fac263-61a0-44e3-84bc-7f85b3d8656a"
        
        # 1. Landing / Top Metrics Dashboard
        await page.screenshot(path=os.path.join(artifact_dir, "screenshot_landing_dashboard.png"), full_page=False)
        print("Captured screenshot_landing_dashboard.png")
        
        # 2. Scraped Sources & Methodology Section
        elem_sources = page.locator(".methodology-box").first
        if await elem_sources.count() > 0:
            await elem_sources.screenshot(path=os.path.join(artifact_dir, "screenshot_data_ingestion.png"))
            print("Captured screenshot_data_ingestion.png")
            
        # 3. Themes & Visual Chart Analysis
        elem_chart = page.locator(".dashboard-layout")
        if await elem_chart.count() > 0:
            await elem_chart.screenshot(path=os.path.join(artifact_dir, "screenshot_themes_analysis.png"))
            print("Captured screenshot_themes_analysis.png")
            
        # 4. Q&A Accordion Section
        headers = page.locator(".accordion-header")
        count = await headers.count()
        if count > 0:
            await headers.nth(0).click()
            await headers.nth(1).click()
            await page.wait_for_timeout(500)
            
        elem_qa = page.locator(".qa-container")
        if await elem_qa.count() > 0:
            await elem_qa.screenshot(path=os.path.join(artifact_dir, "screenshot_qa_accordion.png"))
            print("Captured screenshot_qa_accordion.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
