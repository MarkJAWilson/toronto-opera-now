import urllib.request
import urllib.parse
import ssl
from bs4 import BeautifulSoup

url = "https://www.bing.com/search?q=Opera+by+the+Glass+Toronto"
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
        print("Length:", len(html))
        soup = BeautifulSoup(html, 'html.parser')
        print("Title:", soup.title.string if soup.title else "No Title")
        print("Text preview:")
        print(soup.get_text()[:1000])
except Exception as e:
    print("Error:", e)
