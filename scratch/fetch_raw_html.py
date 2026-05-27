import urllib.request
import ssl

def fetch_and_save(url, filename):
    print(f"Fetching {url}...")
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
            with open(f"scratch/{filename}", "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Saved to scratch/{filename}, length: {len(html)}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# Fetch Tapestry
fetch_and_save("https://tapestryopera.com/", "tapestry_home.html")
# Fetch TCO home and season
fetch_and_save("https://www.torontocityopera.com/", "tco_home.html")
fetch_and_save("https://www.torontocityopera.com/copy-of-2024-25-season", "tco_season.html")
# Fetch Voicebox
fetch_and_save("https://www.operainconcert.com/", "voicebox_home.html")
