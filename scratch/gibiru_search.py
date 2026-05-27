import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def gibiru_search(query):
    print(f"Searching Gibiru for: {query}")
    url = "https://gibiru.com/results.html?q=" + urllib.parse.quote_plus(query)
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
            results = []
            # Print title
            print("HTML Title:", soup.title.string if soup.title else "No Title")
            # Search for results (in Gibiru they are usually in divs with class "results" or "g")
            for a in soup.find_all('a'):
                href = a.get('href')
                text = a.get_text().strip()
                if href and ('http' in href) and len(text) > 10:
                    print(f"Link: {text} -> {href}")
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

gibiru_search("Opera by the Glass Toronto")
