from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/against_the_grain_theatre.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

print("=== ATG HOME HEADINGS ===")
for tag in soup.find_all(["h1", "h2", "h3", "h4"]):
    print("  -", tag.get_text().strip())

print("\n=== ATG HOME TEXT BLOCKS ===")
found = set()
for tag in soup.find_all(["span", "p", "div", "a"]):
    text = tag.get_text().strip()
    if len(text) > 15:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(w in txt_clean for w in ["2025", "2026", "2027", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "opera", "pub"]):
            found.add(txt_clean)
            print("  -", txt_clean[:120])
