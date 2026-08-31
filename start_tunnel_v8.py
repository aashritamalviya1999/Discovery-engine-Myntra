import subprocess
import time
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
log_path = os.path.join(working_dir, "tunnel_v8.log")
url_path = os.path.join(working_dir, "latest_url.txt")

cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-R", "80:127.0.0.1:8352", "nokey@localhost.run"]

print("Starting resilient tunnel manager v8...")

while True:
    print("Launching SSH tunnel process...")
    with open(log_path, "w", encoding="utf-8") as log_file:
        process = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
    print(f"Tunnel process started with PID {process.pid}")
    
    start_time = time.time()
    url_found = None
    
    while time.time() - start_time < 15:
        time.sleep(1)
        if process.poll() is not None:
            break
            
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                content = f.read()
                match = re.search(r'https?://(?!admin\.)[a-zA-Z0-9.-]+\.(?:localhost\.run|lhr\.life|lhr\.pro|lhr\.rocks)', content)
                if match:
                    url_found = match.group(0)
                    print(f"🎉 ACTIVE URL: {url_found}")
                    with open(url_path, "w", encoding="utf-8") as uf:
                        uf.write(url_found)
                    break
                    
    if url_found:
        print("Tunnel active. Keeping process alive...")
        while process.poll() is None:
            time.sleep(2)
        print("Process exited. Reconnecting in 3 seconds...")
        time.sleep(3)
    else:
        print("Failed to capture URL. Retrying in 3 seconds...")
        time.sleep(3)
