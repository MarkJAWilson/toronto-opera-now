import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def webcrawler_search(query):
    print(f"Searching WebCrawler for: {query}")
    url = "https://www.webcrawler.com/serp?" + urllib.parse.urlencode({'q': query})
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
            # In WebCrawler, search results are usually in divs with class "web-bing" or class "serp-result"
            # Let's print some text if we don't find classes
            for a in soup.find_all('a', class_='title'):
                title = a.get_text().strip()
                link = a.get('href')
                # find description nearby
                p = a.find_next('p') or a.find_parent('div').find('div', class_='description')
                snippet = p.get_text().strip() if p else ""
                results.append({
                    'title': title,
                    'link': link,
                    'snippet': snippet
                })
            
            # If no results found, let's look for standard result structures
            if not results:
                for card in soup.find_all('div', class_='result'):
                    title_el = card.find('a')
                    snippet_el = card.find('div', class_='description') or card.find('p')
                    if title_el:
                        title = title_el.get_text().strip()
                        link = title_el.get('href')
                        snippet = snippet_el.get_text().strip() if snippet_el else ""
                        results.append({
                            'title': title,
                            'link': link,
                            'snippet': snippet
                        })
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

results = webcrawler_search("Opera by the Glass Toronto")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
