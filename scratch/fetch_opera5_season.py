import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.opera5.ca/season2026"
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
        with open("scratch/opera5_season.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved scratch/opera5_season.html")
        soup = BeautifulSoup(html, 'html.parser')
        print("Texts in Opera 5 Season:")
        found = set()
        for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div']):
            text = tag.get_text().strip()
            if len(text) > 15:
                txt_clean = re.sub(r'\s+', ' ', text)
                if txt_clean not in found:
                    found.add(txt_clean)
                    print("  -", txt_clean[:150])
                    
        print("\nImages:")
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src')
            alt = img.get('alt')
            print(f"  {src} | Alt: {alt}")
except Exception as e:
    print("Error:", e)
