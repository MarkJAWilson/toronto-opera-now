import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def fetch_and_parse_vb(page_name):
    url = f"https://www.operainconcert.com/{page_name}"
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
            with open(f"scratch/vb_{page_name}", "w", encoding="utf-8") as f:
                f.write(html)
            soup = BeautifulSoup(html, 'html.parser')
            
            # Print text blocks
            print("Texts:")
            found = set()
            for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'td', 'div']):
                txt = tag.get_text().strip()
                if len(txt) > 15:
                    txt_clean = re.sub(r'\s+', ' ', txt)
                    if txt_clean not in found and not any(x in txt_clean for x in ['board of directors', 'general director', 'a brief history']):
                        found.add(txt_clean)
                        # Look for dates
                        if re.search(r'2025|2026|2027|October|November|December|January|February|March|April|May|June', txt_clean, re.IGNORECASE):
                            print("  -", txt_clean[:150])
            
            # Print images
            print("Images:")
            for img in soup.find_all('img'):
                src = img.get('src')
                alt = img.get('alt')
                if src and 'spacer' not in src:
                    print(f"  https://www.operainconcert.com/{src} | Alt: {alt}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

fetch_and_parse_vb("Richard.html")
fetch_and_parse_vb("LaSonnambula.html")
fetch_and_parse_vb("LostStars.html")
