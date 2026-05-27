from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/ccoc_events.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== CCOC EVENTS DETAILS ===")
found = set()
for tag in soup.find_all(["span", "p", "div", "h1", "h2", "h3", "h4"]):
    txt = tag.get_text().strip()
    if len(txt) > 20 and any(w in txt for w in ["upcoming", "2026", "2027"]):
        txt_clean = re.sub(r"\s+", " ", txt)
        if txt_clean not in found:
            found.add(txt_clean)
            print("  -", txt_clean[:200])
