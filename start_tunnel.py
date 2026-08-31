import subprocess
import re
import time
import os

working_dir = r"C:\Users\sanja\.gemini\antigravity\scratch\myntra_wishlist_conversion"
os.makedirs(working_dir, exist_ok=True)
url_file = os.path.join(working_dir, "pinggy_url.txt")

# pinggy command to tunnel port 8352
cmd = ["ssh", "-o", "StrictHostKeyChecking=no", "-p", "443", "-R0:127.0.0.1:8352", "free.pinggy.io"]

print("Starting SSH Pinggy Tunnel...")
process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1)

url_found = None
start_time = time.time()

# Read stdout line by line to extract the generated public link
while time.time() - start_time < 20:
    # Check if process is still running
    ret = process.poll()
    if ret is not None:
        print(f"Process exited with code {ret}")
        break

    # Read line
    line = process.stdout.readline()
    if not line:
        time.sleep(0.1)
        continue

    print(f"OUT: {line.strip()}")
    
    # Pinggy generates URLs ending in .pinggy.link or .pinggy.io
    match = re.search(r'https?://[a-zA-Z0-9.-]+\.pinggy\.(?:link|io|online)', line)
    if match:
        url_found = match.group(0)
        print(f"\n🎉 SUCCESS: Public URL generated: {url_found}\n")
        
        # Write url to a file
        with open(url_file, "w") as f:
            f.write(url_found)
        break

# Keep the script running to maintain the tunnel process
if url_found:
    print("Tunnel is active. Keeping process alive...")
    try:
        while True:
            # Print any incoming traffic info if printed by pinggy
            line = process.stdout.readline()
            if line:
                print(f"OUT: {line.strip()}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping tunnel...")
        process.terminate()
else:
    # Print errors if any
    err = process.stderr.read()
    if err:
        print(f"ERR: {err}")
    print("Failed to find public URL.")
