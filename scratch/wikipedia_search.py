import urllib.request
import urllib.parse
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

def wikipedia_search(query):
    print(f"Searching Wikipedia for: {query}")
    url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=" + urllib.parse.quote_plus(query) + "&format=json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = []
            if 'query' in data and 'search' in data['query']:
                for item in data['query']['search']:
                    results.append({
                        'title': item['title'],
                        'snippet': item['snippet'],
                        'pageid': item['pageid']
                    })
            return results
    except Exception as e:
        print("Error:", e)
        return []

results = wikipedia_search("Opera by the Glass")
for r in results[:10]:
    print("\nTitle:", r['title'])
    print("Snippet:", r['snippet'])
    print("-" * 30)
