import urllib.request
import urllib.parse
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def searx_search(query):
    print(f"Searching Searx for: {query}")
    # Try a few public Searx instances
    instances = [
        "https://searx.be/search",
        "https://searx.space/search",
        "https://search.disclosure.gmbh/search"
    ]
    for inst in instances:
        url = inst + "?" + urllib.parse.urlencode({'q': query, 'format': 'json'})
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        req = urllib.request.Request(url, headers=headers)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        try:
            with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
                res_data = response.read().decode('utf-8', errors='ignore')
                data = json.loads(res_data)
                if 'results' in data and data['results']:
                    return data['results']
        except Exception as e:
            print(f"Failed instance {inst}: {e}")
    return []

results = searx_search("Opera by the Glass Toronto")
for r in results[:10]:
    print("\nTitle:", r.get('title'))
    print("Link:", r.get('url'))
    print("Snippet:", r.get('content'))
    print("-" * 30)
