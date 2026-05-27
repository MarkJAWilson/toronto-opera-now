import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.ludwig-van.com/toronto/?s=Opera+by+the+Glass"
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
        print("Ludwig Van Search Results:")
        
        # Ludwig Van is a WordPress site too. Let's look for search results
        for item in soup.find_all(['article', 'div'], class_=['post', 'type-post', 'entry']):
            title_el = item.find(['h1', 'h2', 'h3', 'a'])
            link_el = item.find('a')
            if title_el and link_el:
                title = title_el.get_text().strip()
                link = link_el.get('href')
                print(f"Title: {title}")
                print(f"Link: {link}")
                print("-" * 50)
        
        # If nothing, print headings
        if not soup.find_all(['article', 'div'], class_=['post', 'type-post', 'entry']):
            print("No articles found. All headings:")
            for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
                print("  ", h.get_text().strip())
except Exception as e:
    print("Error:", e)
