import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.torontocityopera.com/vivavoce2026"
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
        print("VIVA VOCE PAGE:")
        found = set()
        for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4']):
            text = tag.get_text().strip()
            if len(text) > 10:
                txt_clean = re.sub(r'\s+', ' ', text)
                if txt_clean not in found:
                    found.add(txt_clean)
                    print("  -", txt_clean)
except Exception as e:
    print("Error:", e)
