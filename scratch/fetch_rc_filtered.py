import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Try to fetch pre-filtered 2026-2027 season events from RCM
url = "https://www.rcmusic.com/concerts?fq=eventseason%7C%7C2026-2027%20Season&tps_activeFacetTab=_showall_"
print(f"Fetching pre-filtered page: {url}")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx, timeout=12) as response:
        html = response.read().decode('utf-8', errors='ignore')
        with open("scratch/rc_filtered.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved scratch/rc_filtered.html, length:", len(html))
        
        soup = BeautifulSoup(html, 'html.parser')
        # Let's search for titles of events in the pre-rendered HTML
        # In rcmusic.com, event items are usually inside cards with heading tags or specific classes
        # Let's print out all event links or text block summaries
        print("\nAll event titles and links found in filtered HTML:")
        count = 0
        for card in soup.find_all(['div', 'li', 'a']):
            text = card.get_text().strip()
            href = card.get('href') if card.name == 'a' else None
            # Event title is usually in a link with a class like "event-title" or inside a list of search results
            if href and ('/performance/event/' in href or '/events/' in href or '/concerts/' in href) and len(text) > 5:
                # clean text
                text_clean = re.sub(r'\s+', ' ', text)
                print(f"  - {text_clean} -> {href}")
                count += 1
                
        if count == 0:
            print("No matching event links found. Let's dump all headings:")
            for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
                print("  ", h.get_text().strip())
                
except Exception as e:
    print("Error:", e)
