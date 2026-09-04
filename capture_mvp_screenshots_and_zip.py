import asyncio
import os
import zipfile
from playwright.async_api import async_playwright

work_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
artifact_dir = r"C:\Users\sanja\.gemini\antigravity\brain\6f804c75-bb20-4335-9a56-bdd0fd8557af"
desktop_dir = r"C:\Users\sanja\Desktop"
downloads_dir = r"C:\Users\sanja\Downloads"

async def capture_screenshots():
    fitcheck_path = "file:///" + os.path.abspath(os.path.join(work_dir, "fitcheck.html")).replace("\\", "/")
    print(f"Opening {fitcheck_path}...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(viewport={"width": 1400, "height": 900})
        page = await context.new_page()
        
        await page.goto(fitcheck_path)
        await page.wait_for_timeout(1000)

        # Step 1: Initial View / Fit Anchor Setup
        img1 = os.path.join(work_dir, "mvp_step1_fit_anchor.png")
        await page.screenshot(path=img1, full_page=True)
        print("Captured Step 1: Fit Anchor")

        # Step 2: Set Waiting on Fit / Select Fit option if available
        # Click on 'Waiting on Fit' toggle button or interact with UI
        try:
            fit_btn = page.locator("button:has-text('Waiting on Fit'), .waiting-opt-btn:has-text('Fit')").first
            if await fit_btn.is_visible():
                await fit_btn.click()
                await page.wait_for_timeout(500)
        except Exception as e:
            print("Interaction step 2 info:", e)

        img2 = os.path.join(work_dir, "mvp_step2_waiting_on_fit.png")
        await page.screenshot(path=img2, full_page=True)
        print("Captured Step 2: Waiting on Fit")

        # Step 3: Run FitCheck trigger
        try:
            run_btn = page.locator("button:has-text('Run FitCheck'), button:has-text('FitCheck'), #runFitCheckBtn").first
            if await run_btn.is_visible():
                await run_btn.click()
                await page.wait_for_timeout(1000)
        except Exception as e:
            print("Interaction step 3 info:", e)

        img3 = os.path.join(work_dir, "mvp_step3_fitcheck_result.png")
        await page.screenshot(path=img3, full_page=True)
        print("Captured Step 3: FitCheck Result")

        # Step 4: Ready to Buy State
        img4 = os.path.join(work_dir, "mvp_step4_ready_to_buy.png")
        await page.screenshot(path=img4, full_page=True)
        print("Captured Step 4: Ready to Buy")

        # Step 5: Move to Bag
        try:
            bag_btn = page.locator("button:has-text('Move to Bag'), button:has-text('Add to Bag')").first
            if await bag_btn.is_visible():
                await bag_btn.click()
                await page.wait_for_timeout(500)
        except Exception as e:
            print("Interaction step 5 info:", e)

        img5 = os.path.join(work_dir, "mvp_step5_move_to_bag.png")
        await page.screenshot(path=img5, full_page=True)
        print("Captured Step 5: Move to Bag")

        await browser.close()

def create_submission_zip():
    zip_path = os.path.join(work_dir, "myntra_growth_pm_submission.zip")
    files_to_zip = [
        "fitcheck.html",
        "index.html",
        "slides.html",
        "NL_Myntra.pdf",
        "NL_Myntra.pptx",
        "mvp_step1_fit_anchor.png",
        "mvp_step2_waiting_on_fit.png",
        "mvp_step3_fitcheck_result.png",
        "mvp_step4_ready_to_buy.png",
        "mvp_step5_move_to_bag.png"
    ]

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for fname in files_to_zip:
            fpath = os.path.join(work_dir, fname)
            if os.path.exists(fpath):
                zipf.write(fpath, arcname=fname)
                print(f"Zipped {fname}")

    print(f"Created submission ZIP at {zip_path}")

    # Copy to Desktop, Downloads, and Artifacts
    for folder in [desktop_dir, downloads_dir, artifact_dir]:
        shutil.copy(zip_path, os.path.join(folder, "myntra_growth_pm_submission.zip"))
        for fname in files_to_zip:
            src = os.path.join(work_dir, fname)
            if os.path.exists(src):
                shutil.copy(src, os.path.join(folder, fname))

if __name__ == "__main__":
    import shutil
    asyncio.run(capture_screenshots())
    create_submission_zip()
