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

# Let's fetch COC 2627 season page
coc_season_html = fetch_url("https://www.coc.ca/tickets/2627-season")
if coc_season_html:
    print("Length:", len(coc_season_html))
    # Write to a temp file so we can analyze it, or scan for patterns
    with open("scratch/coc_season.html", "w", encoding="utf-8") as f:
        f.write(coc_season_html)
    # Let's extract headers and descriptions if possible
    # COC site uses components. Let's scan for heading tags or text
    titles = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', coc_season_html)
    print("Titles found:")
    for t in titles:
        print("  ", t.strip())

    # Let's find images
    images = re.findall(r'<img[^>]+src="([^"]+)"', coc_season_html)
    print("\nImages found:")
    for img in set(images)[:20]:
        print("  ", img)
