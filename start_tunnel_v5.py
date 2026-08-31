import subprocess
import time
import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
log_path = os.path.join(working_dir, "tunnel_v5.log")
url_path = os.path.join(working_dir, "pinggy_url.txt")

# localhost.run command. nokey@localhost.run exposes the port. -n prevents stdin read.
cmd = ["ssh", "-n", "-o", "StrictHostKeyChecking=no", "-R", "80:127.0.0.1:8352", "nokey@localhost.run"]

print("Starting resilient localhost.run tunnel manager...")

while True:
    print("Launching tunnel process...")
    # Clear old log file
    with open(log_path, "w", encoding="utf-8") as log_file:
        process = subprocess.Popen(cmd, stdout=log_file, stderr=subprocess.STDOUT, text=True, bufsize=1)
        
    print(f"Tunnel process started with PID {process.pid}")
    
    # Wait and inspect log_path for the URL
    start_time = time.time()
    url_found = None
    
    while time.time() - start_time < 15:
        time.sleep(1)
        # Check if process is still alive
        ret = process.poll()
        if ret is not None:
            print(f"Process exited early with code {ret}")
            break
            
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Match any http/https link containing localhost.run or lhr.life or lhr.pro
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
                ret = process.poll()
                if ret is not None:
                    print(f"Process exited with code {ret}. Reconnecting...")
                    break
                time.sleep(2)
        except KeyboardInterrupt:
            print("Stopping tunnel...")
            process.terminate()
            break
    else:
        print("Could not find URL. Retrying connection in 5 seconds...")
        process.terminate()
        time.sleep(5)
