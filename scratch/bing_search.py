import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def bing_search(query):
    print(f"Searching Bing for: {query}")
    url = "https://www.bing.com/search?" + urllib.parse.urlencode({'q': query})
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
            # In Bing, search results are in list items of id "b_results"
            for item in soup.find_all('li', class_='b_algo'):
                title_el = item.find('h2')
                link_el = item.find('a')
                snippet_el = item.find('p') or item.find('div', class_='b_caption')
                
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
        print(f"Error: {e}")
        return []

results = bing_search("Opera by the Glass Toronto")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
