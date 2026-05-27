import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def ecosia_search(query):
    print(f"Searching Ecosia for: {query}")
    url = "https://www.ecosia.org/search?" + urllib.parse.urlencode({'q': query})
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
            # Ecosia search results are in div tags with class "result" or similar
            for card in soup.find_all('div', class_='result'):
                title_el = card.find('a', class_='result-title')
                snippet_el = card.find('p', class_='result-snippet') or card.find('div', class_='result-snippet')
                
                title = title_el.get_text().strip() if title_el else ""
                link = title_el.get('href') if title_el else ""
                snippet = snippet_el.get_text().strip() if snippet_el else ""
                
                if title and link:
                    results.append({
                        'title': title,
                        'link': link,
                        'snippet': snippet
                    })
            
            # If nothing, print first 500 chars of HTML
            if not results:
                print("No results parsed. HTML Title:", soup.title.string if soup.title else "No Title")
                print(html[:1000])
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

results = ecosia_search("Opera by the Glass Toronto")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
