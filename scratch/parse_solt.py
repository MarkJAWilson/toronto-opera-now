from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/solt_home.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("SOLT HOME PAGE:")
found = set()
for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div', 'a', 'td']):
    text = tag.get_text().strip()
    if len(text) > 15:
        txt_clean = re.sub(r'\s+', ' ', text)
        if txt_clean not in found:
            found.add(txt_clean)
            print("  -", txt_clean[:150])

print("\nLinks:")
for a in soup.find_all('a'):
    href = a.get('href')
    text = a.get_text().strip()
    if href:
        print(f"  {text} -> {href}")

print("\nImages:")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    print(f"  {src} | Alt: {alt}")
