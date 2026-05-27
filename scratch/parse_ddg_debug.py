from bs4 import BeautifulSoup

with open("scratch/debug_ddg_html.txt", "w", encoding="utf-8") as f:
    pass # we will write the next fetch

import urllib.request
import urllib.parse
import ssl

url = "https://html.duckduckgo.com/html/?" + urllib.parse.urlencode({'q': 'Toronto City Opera'})
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
    html = response.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
print("Title of page:", soup.title.string if soup.title else "No Title")
# Print all text
print("Text content:")
print(soup.get_text()[:2000])
