from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/voicebox_home.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("VOICEBOX OPERA IN CONCERT HOME PAGE:")
found = set()
for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'a']):
    text = tag.get_text().strip()
    if len(text) > 10:
        txt_clean = re.sub(r'\s+', ' ', text)
        if txt_clean not in found:
            found.add(txt_clean)
            print("  -", txt_clean)

# Look for links to show pages or season pages
print("\nLINKS:")
for a in soup.find_all('a'):
    href = a.get('href')
    text = a.get_text().strip()
    if href:
        print(f"  {text} -> {href}")

# Look for images
print("\nIMAGES:")
for img in soup.find_all('img'):
    src = img.get('src')
    alt = img.get('alt')
    print(f"  {src} | Alt: {alt}")
