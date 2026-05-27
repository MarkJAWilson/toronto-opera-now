import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.broadwayworld.com/bwwopera/article/Opera-Atelier-Unveils-202627-Season-A-SEASON-OF-HEROES-20260210"
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
        soup = BeautifulSoup(html, 'html.parser')
        print("BroadwayWorld Page:")
        # Look for images
        print("Images:")
        for img in soup.find_all('img'):
            src = img.get('src')
            alt = img.get('alt')
            if src and ('broadwayworld.com' in src or 'upload' in src or 'news' in src or 'article' in src):
                print(f"  {src} | Alt: {alt}")
except Exception as e:
    print("Error:", e)
