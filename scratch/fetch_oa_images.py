import urllib.request
import urllib.error
import ssl
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.operaatelier.com/"
print(f"Fetching from {url}...")
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        html = response.read().decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html, 'html.parser')
        print("=== IMAGES FOUND ===")
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-srcset')
            alt = img.get('alt')
            print(f"  Src: {src} | Alt: {alt}")
except Exception as e:
    print("Error:", e)
