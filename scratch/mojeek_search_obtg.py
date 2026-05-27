import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def mojeek_search(query):
    print(f"Searching Mojeek for: {query}")
    url = "https://www.mojeek.com/search?" + urllib.parse.urlencode({'q': query})
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
            for li in soup.find_all('li'):
                a = li.find('a', class_='t')
                s = li.find('p', class_='s') or li.find('p')
                if a:
                    title = a.get_text().strip()
                    link = a.get('href')
                    snippet = s.get_text().strip() if s else ""
                    if title and link:
                        results.append({
                            'title': title,
                            'link': link,
                            'snippet': snippet
                        })
            return results
    except Exception as e:
        print(f"Error searching Mojeek: {e}")
        return []

results = mojeek_search("Opera by the Glass")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
