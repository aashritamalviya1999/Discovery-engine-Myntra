import os
import shutil
import subprocess

src_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra-discovery-engine"
target_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"

files_to_copy = [
    "fitcheck.html",
    "app.js",
    "dataset.js",
    "feedbackData.json",
    "styles.css"
]

for filename in files_to_copy:
    src_file = os.path.join(src_dir, filename)
    target_file = os.path.join(target_dir, filename)
    if os.path.exists(src_file):
        shutil.copy(src_file, target_file)
        print(f"Copied {filename} to {target_dir}")

print("Syncing git repo...")
subprocess.run(["git", "add", "."], cwd=target_dir)
subprocess.run(["git", "commit", "-m", "Sync FitCheck MVP prototype and all supporting scripts"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master:main", "-f"], cwd=target_dir)
print("Git sync complete!")
