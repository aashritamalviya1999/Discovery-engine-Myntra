import subprocess
import time
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
log_path = os.path.join(working_dir, "tunnel_v4.log")
url_path = os.path.join(working_dir, "pinggy_url.txt")

# localhost.run command. nokey@localhost.run exposes the port. -n prevents stdin read.
cmd = ["ssh", "-n", "-o", "StrictHostKeyChecking=no", "-R", "80:127.0.0.1:8352", "nokey@localhost.run"]

print("Starting localhost.run tunnel process...")
with open(log_path, "w", encoding="utf-8") as log_file:
    process = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True, bufsize=1)

print(f"Tunnel process started with PID {process.pid}")

# Wait and inspect log_path for the URL
start_time = time.time()
url_found = None

# Localhost.run usually provides a URL in standard format like xxxx.localhost.run or xxxx.lhr.life
while time.time() - start_time < 15:
    time.sleep(1)
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'https?://(?!admin\.)[a-zA-Z0-9.-]+\.(?:localhost\.run|lhr\.life|lhr\.pro|lhr\.rocks)', content)
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

if url_found:
    print("Tunnel is active. Keeping process alive...")
    try:
        while True:
            # Check if child process is still running
            ret = process.poll()
            if ret is not None:
                print(f"Child process exited with code {ret}")
                break
            time.sleep(2)
    except KeyboardInterrupt:
        print("Stopping tunnel...")
        process.terminate()

if not url_found:
    print("Could not find URL in localhost.run logs after 15 seconds.")
    if os.path.exists(log_path):
        with open(log_path, "r", encoding="utf-8") as f:
            print("Log content so far:\n", f.read())
