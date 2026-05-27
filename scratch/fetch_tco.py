import urllib.request
import re
import ssl

def fetch_url(url):
    print(f"\nFetching {url}...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            return response.read().decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Fetch TCO pages
tco_pages = [
    "https://www.torontocityopera.com/",
    "https://www.torontocityopera.com/copy-of-2024-25-season",
    "https://www.torontocityopera.com/vivavoce2026",
    "https://www.torontocityopera.com/macina2026"
]

for url in tco_pages:
    html = fetch_url(url)
    if html:
        print(f"URL: {url}, Length: {len(html)}")
        # Check for headings or key production names
        titles = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', html)
        print("Headings:")
        for t in list(set([t.strip() for t in titles if t.strip()]))[:15]:
            print("  ", re.sub('<[^<]+?>', '', t))
