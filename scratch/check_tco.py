from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/tco_pagliacci.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== PAGLIACCI HEADINGS ===")
for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
    print(tag.get_text().strip())

print("\n=== PAGLIACCI TEXT BLOCKS ===")
found = set()
for tag in soup.find_all(["span", "p", "div"]):
    text = tag.get_text().strip()
    if len(text) > 15:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(word in txt_clean for word in ["June", "May", "April", "tickets", "performing", "staged", "conduct", "direct", "opera"]):
            found.add(txt_clean)
            print(" -", txt_clean[:120])

print("\n=== PAGLIACCI IMAGES ===")
for img in soup.find_all("img"):
    src = img.get("src") or img.get("data-src")
    if src and "wixstatic.com" in src:
        print("Image:", src)
        break
