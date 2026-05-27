import urllib.request
import ssl

urls = [
    "https://operabytheglass.com/",
    "https://www.operabytheglass.com/",
    "https://operabytheglass.ca/",
    "https://www.operabytheglass.ca/"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for url in urls:
    print(f"Trying {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=5) as response:
            print(f"SUCCESS! {url} returned status {response.status}")
            html = response.read().decode('utf-8', errors='ignore')
            with open("scratch/obtg_home.html", "w", encoding="utf-8") as f:
                f.write(html)
            print("Saved to scratch/obtg_home.html")
            break
    except Exception as e:
        print(f"Failed {url}: {e}")
