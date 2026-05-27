import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

# Set standard output to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

def ddg_search(query):
    print(f"\nSearching DuckDuckGo for: {query}")
    url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({'q': query})
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
            for result in soup.find_all('a', class_='result__snippet'):
                title_el = result.find_previous('a', class_='result__url')
                title = title_el.get_text().strip() if title_el else "No Title"
                link = title_el.get('href') if title_el else "#"
                if link.startswith('//duckduckgo.com/l/?uddg='):
                    link = urllib.parse.unquote(link.split('uddg=')[1].split('&')[0])
                snippet = result.get_text().strip()
                results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })
            return results
    except Exception as e:
        print(f"Error searching DuckDuckGo: {e}")
        return []

# Search Tapestry Opera
tapestry_results = ddg_search("Tapestry Opera 2026 2027 season")
for r in tapestry_results[:10]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)

# Search Toronto City Opera 2025 2026 or 2026 2027
tco_results = ddg_search("Toronto City Opera 2026 season")
for r in tco_results[:10]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
