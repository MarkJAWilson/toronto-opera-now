from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/parse_instagram_obtg.py", "r", encoding="utf-8") as f:
    pass # we'll write this script and run it

import urllib.request
import ssl

url = "https://www.instagram.com/operabytheglass/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

with urllib.request.urlopen(urllib.request.Request(url, headers=headers), context=ctx) as r:
    html = r.read().decode('utf-8', errors='ignore')

soup = BeautifulSoup(html, 'html.parser')
print("All Meta Tags:")
for meta in soup.find_all('meta'):
    print(meta.attrs)

print("\nAll script content containing biography:")
for script in soup.find_all('script'):
    content = script.string if script.string else ""
    if "biography" in content:
        # Try to find biography value using regex
        match = re.search(r'"biography"\s*:\s*"([^"]+)"', content)
        if match:
            print("Biography:", match.group(1))
        # Look for website link
        link_match = re.search(r'"external_url"\s*:\s*"([^"]+)"', content)
        if link_match:
            print("External URL:", link_match.group(1))
        # Look for full name
        name_match = re.search(r'"full_name"\s*:\s*"([^"]+)"', content)
        if name_match:
            print("Full Name:", name_match.group(1))
