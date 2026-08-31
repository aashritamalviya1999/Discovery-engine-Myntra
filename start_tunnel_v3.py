import subprocess
import time
import os
import re

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
log_path = os.path.join(working_dir, "tunnel_v3.log")
url_path = os.path.join(working_dir, "pinggy_url.txt")

# pinggy command with -n (no stdin)
cmd = ["ssh", "-n", "-p", "443", "-o", "StrictHostKeyChecking=no", "-o", "ServerAliveInterval=30", "-R0:127.0.0.1:8352", "free.pinggy.io"]

print("Starting tunnel process...")
# Redirect stdout and stderr to the log file in UTF-8
with open(log_path, "w", encoding="utf-8") as log_file:
    process = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True, bufsize=1)

print(f"Tunnel process started with PID {process.pid}")

# Wait and inspect log_path for the URL
start_time = time.time()
url_found = None

while time.time() - start_time < 15:
    time.sleep(1)
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Match any http/https pinggy link
            match = re.search(r'https?://[a-zA-Z0-9.-]+\.pinggy\.(?:link|io|online)', content)
            if match:
                url_found = match.group(0)
                print(f"🎉 FOUND URL: {url_found}")
                with open(url_path, "w", encoding="utf-8") as uf:
                    uf.write(url_found)
                # Copy to artifact folder
                try:
                    with open(r"C:\Users\sanja\.gemini\antigravity\brain\84fac263-61a0-44e3-84bc-7f85b3d8656a\pinggy_url.txt", "w", encoding="utf-8") as af:
                        af.write(url_found)
                except Exception as e:
                    print("Artifact copy error:", e)
                break

if not url_found:
    print("Could not find URL in logs after 15 seconds.")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            print("Log content so far:\n", f.read())
