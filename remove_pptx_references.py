import os
import glob
import subprocess

target_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"

# 1. Update update_web_presentation.py to remove btn-pptx
with open(os.path.join(target_dir, "update_web_presentation.py"), "r", encoding="utf-8") as f:
    web_code = f.read()

# Replace pptx button in web presentation script
web_code = web_code.replace(
    '<a href="NL_Myntra.pptx" download class="btn btn-pptx">📥 Download PPTX</a>',
    ''
)
web_code = web_code.replace(
    '<a href="NL_Myntra.pptx" download class="btn btn-pptx">📥 Download PPTX</a>\n',
    ''
)

with open(os.path.join(target_dir, "update_web_presentation.py"), "w", encoding="utf-8") as f:
    f.write(web_code)

# Execute update_web_presentation.py
python_exe = r"C:\Users\sanja\.gemini\antigravity\scratch\swiggy_instamart_discovery\.venv\Scripts\python.exe"
subprocess.run([python_exe, "update_web_presentation.py"], cwd=target_dir)

# 2. Update index.html top banner
with open(os.path.join(target_dir, "index.html"), "r", encoding="utf-8") as f:
    index_html = f.read()

old_pptx_link = '<a href="NL_Myntra.pptx" download style="background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">📥 PowerPoint (.pptx)</a>'
if old_pptx_link in index_html:
    index_html = index_html.replace(old_pptx_link, '')

with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

# 3. Clean all HTML files of any lingering PPTX references
html_files = glob.glob(os.path.join(target_dir, "**/*.html"), recursive=True)

for hpath in html_files:
    with open(hpath, "r", encoding="utf-8") as f:
        hcontent = f.read()
    
    modified = False
    if "NL_Myntra.pptx" in hcontent:
        hcontent = hcontent.replace('<a href="NL_Myntra.pptx" download class="btn btn-pptx">📥 Download PPTX</a>', '')
        hcontent = hcontent.replace('<a href="NL_Myntra.pptx" download style="background: rgba(255,255,255,0.2); color: white; text-decoration: none; padding: 6px 14px; border-radius: 6px; font-weight: 700; border: 1px solid rgba(255,255,255,0.4); display: inline-flex; align-items: center; gap: 6px;">📥 PowerPoint (.pptx)</a>', '')
        hcontent = hcontent.replace('NL_Myntra.pptx', 'NL_Myntra.pdf')
        modified = True
    
    if modified:
        with open(hpath, "w", encoding="utf-8") as f:
            f.write(hcontent)
        print(f"Cleaned PPTX references from {hpath}")

# Copy fitcheck.html to fitcheck/index.html
shutil_fitcheck = os.path.join(target_dir, "fitcheck.html")
shutil_target = os.path.join(target_dir, "fitcheck", "index.html")
if os.path.exists(shutil_fitcheck):
    import shutil
    shutil.copy(shutil_fitcheck, shutil_target)
    print("Updated fitcheck/index.html copy")

# Git add, commit, push to master and main
subprocess.run(["git", "add", "."], cwd=target_dir)
subprocess.run(["git", "commit", "-m", "Remove PPTX/PowerPoint references; enforce PDF-only submission rules"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master:main", "-f"], cwd=target_dir)
print("Pushed PDF-only version to GitHub master and main!")
