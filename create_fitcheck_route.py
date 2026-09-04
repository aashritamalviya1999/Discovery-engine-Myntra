import os
import shutil
import subprocess

target_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
fitcheck_dir = os.path.join(target_dir, "fitcheck")

os.makedirs(fitcheck_dir, exist_ok=True)

# Copy fitcheck.html to fitcheck/index.html
shutil.copy(os.path.join(target_dir, "fitcheck.html"), os.path.join(fitcheck_dir, "index.html"))
print("Created fitcheck/index.html")

# Git add and push
subprocess.run(["git", "add", "."], cwd=target_dir)
subprocess.run(["git", "commit", "-m", "Add fitcheck/index.html for root directory URL validation"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master:main", "-f"], cwd=target_dir)
print("Pushed fitcheck/index.html to GitHub!")
