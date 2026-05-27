from bs4 import BeautifulSoup
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read Instagram HTML that we saved or fetch it again
import urllib.request
import ssl

url = "https://www.instagram.com/operabytheglass/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
    
    soup = BeautifulSoup(html, 'html.parser')
    print("Parsed Instagram page. Length:", len(html))
    
    # Instagram profile page usually has JSON in one of the script tags:
    # <script type="text/javascript">window._sharedData = ...</script> or script containing "biography"
    for s in soup.find_all('script'):
        content = s.string if s.string else ""
        if "biography" in content or "external_url" in content or "graphql" in content:
            print("Found script containing biography or external_url!")
            # Let's print some parts of it
            print(content[:1000])
            print("...")
            # Search for any URL in the script
            urls = re.findall(r'https?://[^\s"\'\\<>]+', content)
            print("URLs found in script:")
            for u in set(urls):
                print("  ", u)
                
    # Also let's print any meta description tag, which often has the biography!
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    if meta_desc:
        print("\nMeta Description:")
        print(meta_desc.get('content'))
        
    meta_og = soup.find('meta', attrs={'property': 'og:description'})
    if meta_og:
        print("\nOG Description:")
        print(meta_og.get('content'))
        
except Exception as e:
    print("Error:", e)
