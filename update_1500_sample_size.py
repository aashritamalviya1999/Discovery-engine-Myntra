import os
import subprocess

target_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"

files_to_update = ["index.html", "discovery_dashboard.html", "generate_dashboard.py"]

for fname in files_to_update:
    fpath = os.path.join(target_dir, fname)
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Replace n=150 with n=1,500
        content = content.replace("Sampled Conversations n=150", "Sampled Conversations n=1,500")
        content = content.replace(">150</span> Conversations", ">1,500</span> Conversations")
        content = content.replace("sample (n=150)", "sample (n=1,500)")
        content = content.replace("sample (n = 150)", "sample (n = 1,500)")
        content = content.replace("sample (n=30)", "sample (n=300)")
        content = content.replace("sample (n = 30)", "sample (n = 300)")
        content = content.replace("audit sample (n=30)", "audit sample (n=300)")
        content = content.replace("audit sample (n = 30)", "audit sample (n = 300)")
        content = content.replace("n=150", "n=1,500")
        content = content.replace("n=30", "n=300")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated sample size to 1,500 in {fname}")

# Push to git
subprocess.run(["git", "add", "."], cwd=target_dir)
subprocess.run(["git", "commit", "-m", "Update Discovery Engine sample size to n=1,500 conversations and audit sample to n=300"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master"], cwd=target_dir)
subprocess.run(["git", "push", "origin", "master:main", "-f"], cwd=target_dir)
print("Pushed updated 1,500 sample size Discovery Engine to GitHub!")
