import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.rcmusic.com/concerts"
print(f"Fetching {url}...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
        with open("scratch/rc_concerts.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved scratch/rc_concerts.html, length:", len(html))
        
        soup = BeautifulSoup(html, 'html.parser')
        print("Headings:")
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            print("  ", h.get_text().strip())
            
        print("\nLinks:")
        for a in soup.find_all('a'):
            href = a.get('href')
            text = a.get_text().strip()
            if href and ('opera' in href.lower() or 'glenn-gould' in href.lower()):
                print(f"  {text} -> {href}")
except Exception as e:
    print("Error:", e)
