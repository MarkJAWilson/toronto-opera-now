import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def ask_search(query):
    print(f"Searching Ask.com for: {query}")
    url = "https://www.ask.com/web?" + urllib.parse.urlencode({'q': query})
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
            # In Ask.com, search results are usually in divs with class "PartialSearchResults-item" or similar
            for item in soup.find_all('div', class_='PartialSearchResults-item'):
                title_el = item.find('a', class_='PartialSearchResults-item-title-link')
                snippet_el = item.find('p', class_='PartialSearchResults-item-abstract')
                
                title = title_el.get_text().strip() if title_el else ""
                link = title_el.get('href') if title_el else ""
                snippet = snippet_el.get_text().strip() if snippet_el else ""
                
                if title and link:
                    results.append({
                        'title': title,
                        'link': link,
                        'snippet': snippet
                    })
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

results = ask_search("U of T Opera 2026 2027 season")
for r in results[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
