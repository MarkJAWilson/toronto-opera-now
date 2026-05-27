import subprocess
from bs4 import BeautifulSoup
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.operaatelier.com/"
print(f"Fetching from {url} via curl...")

try:
    # Run curl command with standard browser headers
    result = subprocess.run([
        'curl', 
        '-s',
        '-H', 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        '-H', 'Accept-Language: en-US,en;q=0.9',
        url
    ], capture_output=True, text=True, errors='ignore')
    
    html = result.stdout
    print(f"Response size: {len(html)}")
    
    # Save the output for inspection
    with open("scratch/oa_curl.html", "w", encoding="utf-8") as f:
        f.write(html)
        
    soup = BeautifulSoup(html, 'html.parser')
    print("=== IMAGES FOUND VIA CURL ===")
    count = 0
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src') or img.get('data-srcset')
        alt = img.get('alt')
        print(f"  Src: {src} | Alt: {alt}")
        count += 1
    print(f"Total images found: {count}")
    
except Exception as e:
    print("Error:", e)
