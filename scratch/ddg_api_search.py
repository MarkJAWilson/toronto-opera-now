import urllib.request
import urllib.parse
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://api.duckduckgo.com/?q=" + urllib.parse.quote_plus("Opera by the Glass") + "&format=json"
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
        print("DuckDuckGo Instant Answer API:")
        print("Abstract:", data.get('Abstract'))
        print("AbstractURL:", data.get('AbstractURL'))
        print("Heading:", data.get('Heading'))
        print("RelatedTopics:")
        for t in data.get('RelatedTopics', [])[:5]:
            print("  -", t.get('Text'))
except Exception as e:
    print("Error:", e)
