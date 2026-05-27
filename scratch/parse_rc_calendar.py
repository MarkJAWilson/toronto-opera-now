from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_calendar.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
print("RCM Calendar Length:", len(html))

print("\nSearching for Glenn Gould School or Opera:")
found = set()
for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div', 'a', 'td']):
    text = tag.get_text().strip()
    if len(text) > 10:
        txt_clean = re.sub(r'\s+', ' ', text)
        if txt_clean not in found:
            if re.search(r'glenn gould|ggs|opera|school|orchestra|recital', txt_clean, re.IGNORECASE):
                found.add(txt_clean)
                print("  -", txt_clean[:150])

print("\nImages on RCM Calendar page:")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    print(f"  {src} | Alt: {alt}")
