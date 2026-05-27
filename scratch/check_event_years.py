import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Let's write a script to download and parse the year for each of the 5 eventbrite links
links = {
    'Jonah': 'https://www.eventbrite.ca/e/of-whales-and-willpower-the-jamaican-jonah-pt-1-tickets-1501714882639?aff=odcleoeventsincollection',
    'Cabinet': 'https://www.eventbrite.ca/e/a-cabinet-of-curiosities-3-classical-variety-show-odds-arts-auction-tickets-1501693428469?aff=odcleoeventsincollection',
    'CoolCats': 'https://www.eventbrite.ca/e/the-collective-of-cool-cats-jazz-classical-from-beyond-the-iron-curtain-tickets-1501675685399?aff=odcleoeventsincollection',
    'Bohemian': 'https://www.eventbrite.ca/e/bohemian-holiday-a-festive-night-of-czech-classical-music-tickets-1501662225139?aff=odcleoeventsincollection',
    'Baroque': 'https://www.eventbrite.ca/e/apocryphonia-enchanted-baroque-bloor-west-tickets-1514051933089?aff=odcleoeventsincollection'
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for name, url in links.items():
    print(f"\nFetching {name} event info...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            # Look for schema markup or microdata which has the exact date with year
            # Search for ld+json
            json_ld = soup.find_all('script', type='application/ld+json')
            date_found = False
            for j in json_ld:
                if j.string and 'startDate' in j.string:
                    print("  JSON-LD startDate:", re.search(r'"startDate"\s*:\s*"([^"]+)"', j.string).group(1))
                    print("  JSON-LD endDate  :", re.search(r'"endDate"\s*:\s*"([^"]+)"', j.string).group(1))
                    date_found = True
                    break
            if not date_found:
                # Search for any text containing year
                print("  No JSON-LD, looking for date text:")
                for tag in soup.find_all(['span', 'p', 'div']):
                    txt = tag.get_text().strip()
                    if len(txt) > 10 and re.search(r'2025|2026|2027', txt):
                        print("    -", txt[:100])
                        break
    except Exception as e:
        print(f"Error {name}: {e}")
