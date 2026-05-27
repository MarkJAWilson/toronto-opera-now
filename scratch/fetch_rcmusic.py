import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def fetch_and_save(url, filename):
    print(f"Fetching {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
            html = response.read().decode('utf-8', errors='ignore')
            with open(f"scratch/{filename}", "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Saved to scratch/{filename}, length: {len(html)}")
            return html
    except Exception as e:
        print(f"Failed {url}: {e}")
        return None

# Fetch Opera York "Whats On" page
fetch_and_save("https://operayork.com/whats-on/", "operayork_whatson.html")

# Let's fetch RCM home page to inspect links
rc_html = fetch_and_save("https://www.rcmusic.com/", "rc_home.html")
if rc_html:
    soup = BeautifulSoup(rc_html, 'html.parser')
    print("\nLinks in Royal Conservatory homepage:")
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.get_text().strip()
        if href and ('opera' in href.lower() or 'glenn-gould' in href.lower() or 'event' in href.lower() or 'performance' in href.lower()):
            print(f"  {text} -> {href}")
