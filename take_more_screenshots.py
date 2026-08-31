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
        
        # 5. Segmentation & Feedback Feed Detail
        feed_elem = page.locator("#feedbackFeed")
        if await feed_elem.count() > 0:
            await feed_elem.scroll_into_view_if_needed()
            await page.wait_for_timeout(500)
            await page.locator(".panel").nth(1).screenshot(path=os.path.join(artifact_dir, "screenshot_segmentation_feed.png"))
            print("Captured screenshot_segmentation_feed.png")
            
        # 6. Opportunity & Solution Q10 Accordion
        headers = page.locator(".accordion-header")
        count = await headers.count()
        if count >= 10:
            await headers.nth(9).click() # Q10
            await page.wait_for_timeout(500)
            await page.locator(".qa-container").screenshot(path=os.path.join(artifact_dir, "screenshot_opportunity_prioritization.png"))
            print("Captured screenshot_opportunity_prioritization.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(capture())
