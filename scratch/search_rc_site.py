import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.rcmusic.com/search?q=opera"
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
        with open("scratch/rc_search_opera.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved scratch/rc_search_opera.html, length:", len(html))
        
        soup = BeautifulSoup(html, 'html.parser')
        print("Texts on Search Page:")
        found = set()
        for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div', 'a']):
            text = tag.get_text().strip()
            if len(text) > 15:
                txt_clean = re.sub(r'\s+', ' ', text)
                if txt_clean not in found:
                    found.add(txt_clean)
                    if re.search(r'2026|2027|Glenn Gould|GGS|Koerner|November|March|June', txt_clean, re.IGNORECASE):
                        print("  -", txt_clean[:150])
except Exception as e:
    print("Error:", e)
