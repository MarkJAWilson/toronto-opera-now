import urllib.request
import urllib.error
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

urls = {
    "Cells of Wind": "https://www.fawnchambercreative.com/cells-of-wind-1/",
    "Lhomme et le ciel": "https://www.fawnchambercreative.com/upcomingevents/upcoming/",
    "Devised Horror Project": "https://www.fawnchambercreative.com/2064-2/"
}

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

for name, url in urls.items():
    print(f"\nFetching {name} from {url}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            content = response.read().decode('utf-8', errors='ignore')
            print(f"  Success! Length: {len(content)}")
            filename = f"scratch/{name.lower().replace(' ', '_')}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Saved to {filename}")
    except urllib.error.HTTPError as e:
        print(f"  HTTP Error {e.code} for {url}")
    except Exception as e:
        print(f"  Error for {url}: {e}")
