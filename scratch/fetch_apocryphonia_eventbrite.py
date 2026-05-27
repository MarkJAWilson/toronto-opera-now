import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.eventbrite.ca/e/of-whales-and-willpower-the-jamaican-jonah-pt-1-tickets-1501714882639?aff=websiteApoc"
print(f"Fetching Eventbrite {url}...")
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
        with open("scratch/apocryphonia_eventbrite.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Saved Eventbrite HTML.")
        soup = BeautifulSoup(html, 'html.parser')
        
        # Look for dates and text content
        # Eventbrite puts dates in custom components or structures
        print("Text Blocks:")
        found = set()
        for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div']):
            txt = tag.get_text().strip()
            if len(txt) > 10:
                txt_clean = re.sub(r'\s+', ' ', txt)
                if txt_clean not in found and any(x in txt_clean for x in ['Date', 'date', 'Time', 'time', 'pm', 'PM', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', '2026', '2027']):
                    found.add(txt_clean)
                    print("  -", txt_clean[:150])
except Exception as e:
    print("Error:", e)
