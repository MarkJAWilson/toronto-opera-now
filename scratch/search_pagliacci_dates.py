import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

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
        # Use a short timeout and handle exception
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            results = []
            for result in soup.find_all('a', class_='result__snippet'):
                title_el = result.find_previous('a', class_='result__url')
                title = title_el.get_text().strip() if title_el else ""
                link = title_el.get('href') if title_el else ""
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
        print(f"Error: {e}")
        return []

# Search for TCO Pagliacci
results = ddg_search("site:torontocityopera.com Pagliacci")
for r in results[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)

results2 = ddg_search("\"Toronto City Opera\" Pagliacci 2025 OR 2026")
for r in results2[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
