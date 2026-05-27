import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://tapa.ca/membership/member-directory/"
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
        print("TAPA Members containing Glass or Opera:")
        found = False
        for a in soup.find_all('a'):
            text = a.get_text().strip()
            if text and ('glass' in text.lower() or 'opera' in text.lower()):
                print(f"  - {text} -> {a.get('href')}")
                found = True
        if not found:
            print("No members found with these keywords.")
            # Search for any text containing glass in the entire body
            text_matches = re.findall(r'.{0,50}glass.{0,50}', html, re.IGNORECASE)
            print("Raw text matches for 'glass':")
            for m in text_matches[:10]:
                print("  ", m.strip())
except Exception as e:
    print("Error:", e)
