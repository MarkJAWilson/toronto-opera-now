from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/canuck_cantatas.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== CANUCK CANTATAS DETAILS ===")
for tag in soup.find_all(["span", "p", "div", "h1", "h2", "h3", "h4"]):
    txt = tag.get_text().strip()
    if len(txt) > 20 and any(w in txt for w in ["April", "Redwood", "2026", "2027", "2025"]):
        print("  -", re.sub(r"\s+", " ", txt)[:200])
