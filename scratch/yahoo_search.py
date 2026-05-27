import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def yahoo_search(query):
    print(f"\nSearching Yahoo for: {query}")
    url = "https://search.yahoo.com/search?" + urllib.parse.urlencode({'p': query})
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
            # In Yahoo search, results are typically inside div class "algo" or "compTitle"
            results = []
            for item in soup.find_all('div', class_='algo'):
                title_el = item.find('h3')
                link_el = item.find('a')
                snippet_el = item.find('div', class_='compText') or item.find('p')
                
                title = title_el.get_text().strip() if title_el else ""
                link = link_el.get('href') if link_el else ""
                snippet = snippet_el.get_text().strip() if snippet_el else ""
                
                if title and link:
                    results.append({
                        'title': title,
                        'link': link,
                        'snippet': snippet
                    })
            return results
    except Exception as e:
        print(f"Error searching Yahoo: {e}")
        return []

# Search Tapestry Opera
results = yahoo_search("Tapestry Opera 2026 2027 season")
for r in results[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)

# Search Toronto City Opera
results = yahoo_search("Toronto City Opera 2026 2027 season")
for r in results[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
