from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/opera5_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("OPERA 5 SEASON STRUCTURE:")
# Let's traverse the document and find sections, h1/h2/h3, and images in order.
for el in soup.find_all(['h1', 'h2', 'h3', 'h4', 'img']):
    if el.name == 'img':
        src = el.get('src') or el.get('data-src')
        if src and 'squarespace-cdn' in src and not any(x in src for x in ['Favicon', 'logo']):
            print(f"  IMAGE: {src}")
    else:
        text = el.get_text().strip()
        if text and len(text) > 5:
            # clean text
            text_clean = re.sub(r'\s+', ' ', text)
            print(f"TEXT: {text_clean}")
