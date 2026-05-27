from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/solo_events.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("=== SOLO EVENTS HEADINGS ===")
for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
    print("  -", tag.get_text().strip())

print("\n=== SOLO EVENTS TEXT BLOCKS ===")
found = set()
for tag in soup.find_all(["span", "p", "div", "a"]):
    text = tag.get_text().strip()
    if len(text) > 15:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(w in txt_clean for w in ["2025", "2026", "2027", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "opera", "performance", "concert", "soprano", "baritone"]):
            found.add(txt_clean)
            print("  -", txt_clean[:150])

print("\n=== SOLO EVENTS IMAGES ===")
for img in soup.find_all("img"):
    src = img.get("src") or img.get("data-src")
    alt = img.get("alt")
    print(f"  {src} | Alt: {alt}")
