import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def brave_search(query):
    print(f"Searching Brave for: {query}")
    url = "https://search.brave.com/search?" + urllib.parse.urlencode({'q': query})
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
            # In Brave search, result blocks are usually divs with class "snippet" or similar
            for card in soup.find_all('div', class_='snippet'):
                title_el = card.find('span', class_='title') or card.find('h2') or card.find('a')
                link_el = card.find('a')
                snippet_el = card.find('p', class_='snippet-description') or card.find('div', class_='snippet-description') or card.find('p')
                
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
        print(f"Error searching Brave: {e}")
        return []

results = brave_search("Apocryphonia Toronto opera")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
