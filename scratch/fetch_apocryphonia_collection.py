import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.eventbrite.com/cc/the-fourth-cycle-of-musical-revelations-4510263?utm-campaign=social&utm-content=creatorshare&utm-medium=discovery&utm-term=odclsxcollection&utm-source=cp&aff=escb"
print(f"Fetching Eventbrite collection {url}...")
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
        with open("scratch/apocryphonia_collection.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved Eventbrite collection HTML.")
        soup = BeautifulSoup(html, 'html.parser')
        
        # Print text blocks containing Event or ticket details
        print("Event links and titles in collection:")
        for a in soup.find_all('a'):
            href = a.get('href')
            text = a.get_text().strip()
            if href and 'tickets' in href and len(text) > 5:
                print(f"  {text} -> {href}")
                
        # Let's print some other headers to see what events are listed
        print("Headers:")
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'span']):
            txt = h.get_text().strip()
            if len(txt) > 15 and ('Jonah' in txt or 'Whales' in txt or 'Cycle' in txt or 'West' in txt or 'Classical' in txt or 'Concert' in txt or 'June' in txt or 'July' in txt or 'Apocryphonia' in txt):
                print("  -", txt[:120])
except Exception as e:
    print("Error:", e)
