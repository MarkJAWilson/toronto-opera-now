import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://tapa.ca/?s=Opera+by+the+Glass"
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
        print("TAPA Search Results:")
        
        # Look for search results or listings
        for item in soup.find_all(['h2', 'h3', 'h4', 'a']):
            text = item.get_text().strip()
            href = item.get('href') if item.name == 'a' else None
            # If the item has class entry-title or similar
            if href and ('opera' in href or 'glass' in href or len(text) > 10):
                print(f"Text: {text} -> Link: {href}")
                
        # Print headings
        print("\nAll Headings:")
        for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
            print("  ", h.get_text().strip())
except Exception as e:
    print("Error:", e)
