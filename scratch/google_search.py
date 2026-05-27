import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def google_search(query):
    print(f"Searching Google for: {query}")
    url = "https://www.google.com/search?q=" + urllib.parse.quote_plus(query) + "&gbv=1"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9'
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
            # Google basic search results are inside divs.
            # Let's inspect class or structure. Typically they are inside div elements with specific styles.
            # Let's look for standard a tags that don't go to google.com/url but are result links
            # Actually, let's look for all h3 elements, since Google result titles are always h3!
            for h3 in soup.find_all('h3'):
                parent_a = h3.find_parent('a')
                if parent_a:
                    link = parent_a.get('href')
                    # Google redirects result links to /url?q=...
                    if link.startswith('/url?q='):
                        link = urllib.parse.unquote(link.split('/url?q=')[1].split('&')[0])
                    
                    # Find snippet (usually sibling div or text nearby)
                    snippet = ""
                    # Let's climb up to find the result container
                    container = h3.parent
                    while container and container.name != 'div':
                        container = container.parent
                    if container:
                        # Find the snippet text
                        sibling = container.find_next_sibling('div')
                        if sibling:
                            snippet = sibling.get_text().strip()
                    
                    results.append({
                        'title': h3.get_text().strip(),
                        'link': link,
                        'snippet': snippet
                    })
            return results
    except Exception as e:
        print(f"Error: {e}")
        return []

results = google_search("Opera by the Glass Toronto")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Link:", r['link'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
