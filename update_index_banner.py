import os

index_path = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

banner_html = """
    <!-- Top Submission Artifact Bar -->
    <div style="background: linear-gradient(90deg, #1b264f 0%, #e11d48 100%); color: white; padding: 12px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px; font-family: 'Outfit', sans-serif; font-size: 14px; font-weight: 600; position: sticky; top: 0; z-index: 9999; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
        <div style="display: flex; align-items: center; gap: 10px;">
            <span style="background: rgba(255,255,255,0.25); padding: 4px 10px; border-radius: 20px; text-transform: uppercase; letter-spacing: 1px; font-size: 11px;">Top Scholar Submission</span>
            <span>Myntra Wishlist Growth PM Case Study Presentation (10 Slides)</span>
        </div>
        <div style="display: flex; gap: 10px; flex-wrap: wrap;">
            <a href="slides.html" target="_blank" style="background: white; color: #0f172a; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">📊 View Slides Online</a>
            <a href="NL_Myntra.pptx" download style="background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">📥 PowerPoint (.pptx)</a>
            <a href="NL_Myntra.pdf" target="_blank" style="background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">📄 Vector PDF (.pdf)</a>
            <a href="fitcheck.html?v=10" target="_blank" style="background: #10b981; color: white; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; display: inline-flex; align-items: center; gap: 6px;">👗 Launch FitCheck MVP</a>
        </div>
    </div>
"""

if "Top Submission Artifact Bar" not in content:
    content = content.replace("<body>", "<body>" + banner_html, 1)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully added banner to index.html")
else:
    print("Banner already present in index.html")
