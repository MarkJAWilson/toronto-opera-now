import urllib.request
import ssl
from bs4 import BeautifulSoup
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
scripts = soup.find_all('script')

print(f"Found {len(scripts)} script tags. Downloading external scripts to scan...")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create a directory for JS files
os.makedirs("scratch/js", exist_ok=True)

js_files = []
for i, s in enumerate(scripts):
    src = s.get('src')
    if src:
        # Resolve absolute URL
        if src.startswith('/'):
            js_url = "https://www.rcmusic.com" + src
        else:
            js_url = src
        
        # Don't download common third party scripts like google, facebook
        if any(x in js_url for x in ['google', 'facebook', 'twitter', 'recaptcha', 'doubleclick', 'hotjar', 'omnisend']):
            continue
            
        print(f"Downloading {js_url}...")
        try:
            req = urllib.request.Request(js_url, headers=headers)
            with urllib.request.urlopen(req, context=ctx, timeout=5) as response:
                js_content = response.read().decode('utf-8', errors='ignore')
                filename = f"scratch/js/script_{i}.js"
                with open(filename, "w", encoding="utf-8") as f_out:
                    f_out.write(js_content)
                js_files.append(filename)
        except Exception as e:
            print(f"  Failed: {e}")

print(f"\nScanning {len(js_files)} JS files for API paths and endpoints...")
for f in js_files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    # Search for api paths
    paths = re.findall(r'\"(/[^\"]*api/[^\"]*)\"', content)
    paths += re.findall(r'\'(/[^\']*api/[^\']*)\'', content)
    # Search for graphql
    gql = re.findall(r'graphql', content, re.IGNORECASE)
    # Search for strapi
    strapi = re.findall(r'strapi', content, re.IGNORECASE)
    
    if paths or gql or strapi:
        print(f"\nIn file {f}:")
        if paths:
            print("  Paths found:", list(set(paths))[:10])
        if gql:
            print(f"  GraphQL occurrences: {len(gql)}")
        if strapi:
            print(f"  Strapi occurrences: {len(strapi)}")
        
        # Search for any endpoint pattern (e.g. host or backend api)
        endpoints = re.findall(r'https?://[^\s"\'\\<>]+', content)
        backend = [e for e in endpoints if 'rcmusic' in e or 'strapi' in e or 'aws' in e]
        if backend:
            print("  Backend URLs found:", list(set(backend))[:5])
