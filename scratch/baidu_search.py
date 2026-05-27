import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def baidu_search(query):
    print(f"Searching Baidu for: {query}")
    url = "https://www.baidu.com/s?" + urllib.parse.urlencode({'wd': query})
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
            
            # Baidu results are typically inside div elements with class "result" or "c-container"
            for card in soup.find_all('div', class_=['result', 'c-container']):
                title_el = card.find('h3') or card.find('a')
                link_el = card.find('a')
                # abstract
                snippet_el = card.find('span', class_=['c-abstract', 'content-desc']) or card.find('div', class_='c-abstract') or card.find('p')
                
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

results = baidu_search("Glenn Gould School Opera 2026 2027")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
