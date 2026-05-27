from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read Twitter HTML from the previous fetch or fetch it again and save it
import urllib.request
import ssl

url = "https://twitter.com/operabytheglass"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), context=ctx) as r:
        html = r.read().decode('utf-8', errors='ignore')
    
    soup = BeautifulSoup(html, 'html.parser')
    print("Parsed Twitter page. Length:", len(html))
    
    # Print links in page
    print("\nLinks in profile:")
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.get_text().strip()
        if href and not any(x in href for x in ['twitter.com', 'x.com', 'help', 'privacy', 'tos']):
            print(f"  {text} -> {href}")
            
    # Print description or text blocks
    print("\nTexts in profile:")
    for tag in soup.find_all(['span', 'p', 'div']):
        text = tag.get_text().strip()
        if len(text) > 15:
            # check if contains interesting text
            print("  -", re.sub(r'\s+', ' ', text)[:150])
            break # just print first few
            
except Exception as e:
    print("Error:", e)
