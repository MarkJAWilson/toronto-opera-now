import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://operacanada.ca/?s=Opera+by+the+Glass"
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
        print("Opera Canada Search Results:")
        
        # WordPress search results usually are in articles or h2 class "entry-title"
        for article in soup.find_all(['article', 'div'], class_=['post', 'entry', 'type-post']):
            title_el = article.find(['h1', 'h2', 'h3', 'a'], class_=['entry-title', 'post-title', 'title'])
            if not title_el:
                title_el = article.find('h2') or article.find('h3')
            link_el = article.find('a')
            
            title = title_el.get_text().strip() if title_el else ""
            link = link_el.get('href') if link_el else ""
            
            # Find excerpt
            excerpt_el = article.find(['div', 'p'], class_=['entry-summary', 'entry-content', 'post-excerpt', 'excerpt'])
            excerpt = excerpt_el.get_text().strip() if excerpt_el else ""
            
            if title and link:
                print(f"\nTitle: {title}")
                print(f"Link: {link}")
                print(f"Excerpt: {excerpt[:200]}")
                print("-" * 50)
                
        # If nothing printed, print all headings
        if not soup.find_all(['article', 'div'], class_=['post', 'entry', 'type-post']):
            print("No structured articles found. Printing all headings:")
            for h in soup.find_all(['h1', 'h2', 'h3', 'h4']):
                print("  ", h.get_text().strip())
except Exception as e:
    print("Error:", e)
