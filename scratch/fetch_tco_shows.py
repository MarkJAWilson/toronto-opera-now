import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def fetch_and_parse(url, name):
    print(f"\nFetching {url}...")
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
            with open(f"scratch/tco_{name}.html", "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Saved scratch/tco_{name}.html")
            
            soup = BeautifulSoup(html, 'html.parser')
            # Extract text blocks
            print("Texts:")
            for span in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4']):
                txt = span.get_text().strip()
                if len(txt) > 15 and re.search(r'2026|2027|June|November|March|April|May|July|August|September|October|December|January|February|Bathurst|St\.|Avenue|Street|pm|tickets', txt, re.IGNORECASE):
                    print("  -", re.sub(r'\s+', ' ', txt)[:120])
            
            # Extract images
            print("Images:")
            for img in soup.find_all('img'):
                src = img.get('src') or img.get('data-src')
                alt = img.get('alt')
                if src and ('static.wixstatic.com' in src or 'wix' in src):
                    print(f"  {src} | Alt: {alt}")
    except Exception as e:
        print(f"Error: {e}")

fetch_and_parse("https://www.torontocityopera.com/pagliacci", "pagliacci")
fetch_and_parse("https://www.torontocityopera.com/orpheus", "orpheus")
