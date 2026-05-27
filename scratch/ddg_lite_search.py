import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def ddg_lite_search(query):
    print(f"Searching DDG Lite for: {query}")
    url = "https://lite.duckduckgo.com/lite/"
    data = urllib.parse.urlencode({'q': query}).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    req = urllib.request.Request(url, data=data, headers=headers)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
            soup = BeautifulSoup(html, 'html.parser')
            results = []
            # In DDG Lite, results are tables or rows. Let's find tr elements or links
            for link in soup.find_all('a', class_='result-link'):
                title = link.get_text().strip()
                href = link.get('href')
                # The next tr or sibling usually contains the snippet
                # Let's find the description snippet
                snippet = ""
                tr = link.find_parent('tr')
                if tr:
                    next_tr = tr.find_next_sibling('tr')
                    if next_tr:
                        snippet_td = next_tr.find('td', class_='result-snippet')
                        if snippet_td:
                            snippet = snippet_td.get_text().strip()
                results.append({
                    'title': title,
                    'link': href,
                    'snippet': snippet
                })
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

results = ddg_lite_search("Opera Atelier \"The Descent of Orpheus\" image")
for r in results[:5]:
    print("Title:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
