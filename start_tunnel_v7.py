import subprocess
import time
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
log_path = os.path.join(working_dir, "tunnel_v7.log")

cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:127.0.0.1:8352", "nokey@localhost.run"]

print("Starting fresh localhost.run tunnel process v7...")
with open(log_path, "w", encoding="utf-8") as log_file:
    process = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True, bufsize=1)

print(f"Tunnel process started with PID {process.pid}")

start_time = time.time()
url_found = None

while time.time() - start_time < 15:
    time.sleep(1)
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'https?://(?!admin\.)[a-zA-Z0-9.-]+\.(?:localhost\.run|lhr\.life|lhr\.pro|lhr\.rocks)', content)
            if match:
                url_found = match.group(0)
                print(f"🎉 NEW FRESH PUBLIC URL: {url_found}")
                break

if url_found:
    print("Tunnel is active.")
    while True:
        time.sleep(5)
else:
    print("Failed to capture URL.")
