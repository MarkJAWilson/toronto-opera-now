import urllib.request
import urllib.error
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

# Let's fetch COC
coc_html = fetch_url("https://www.coc.ca/")
if coc_html:
    print("COC homepage length:", len(coc_html))
    links = re.findall(r'href="([^"]+)"', coc_html)
    season_links = [l for l in links if 'season' in l.lower() or 'production' in l.lower() or '2026' in l or '2027' in l or 'what-we-do' in l.lower()]
    print("Potential season links:")
    for l in list(set(season_links))[:20]:
        print("  ", l)

# Let's check Opera Atelier
oa_html = fetch_url("https://www.operaatelier.com/")
if oa_html:
    print("Opera Atelier homepage length:", len(oa_html))
    links = re.findall(r'href="([^"]+)"', oa_html)
    oa_season_links = [l for l in links if 'season' in l.lower() or 'production' in l.lower() or '2026' in l or '2027' in l or 'show' in l.lower()]
    print("Potential OA season links:")
    for l in list(set(oa_season_links))[:20]:
        print("  ", l)

# Let's check Tapestry Opera
tapestry_html = fetch_url("https://tapestryopera.com/")
if tapestry_html:
    print("Tapestry Opera homepage length:", len(tapestry_html))
    links = re.findall(r'href="([^"]+)"', tapestry_html)
    tapestry_season_links = [l for l in links if 'season' in l.lower() or 'production' in l.lower() or '2026' in l or '2027' in l or 'show' in l.lower()]
    print("Potential Tapestry season links:")
    for l in list(set(tapestry_season_links))[:20]:
        print("  ", l)

# Let's check Toronto City Opera
tco_html = fetch_url("https://www.torontocityopera.com/")
if tco_html:
    print("TCO homepage length:", len(tco_html))
    links = re.findall(r'href="([^"]+)"', tco_html)
    tco_season_links = [l for l in links if 'season' in l.lower() or 'production' in l.lower() or '2026' in l or '2027' in l or 'show' in l.lower()]
    print("Potential TCO season links:")
    for l in list(set(tco_season_links))[:20]:
        print("  ", l)
