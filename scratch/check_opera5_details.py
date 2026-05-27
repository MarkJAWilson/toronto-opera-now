from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/opera5_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== OPERA 5 DETAILS ===")
found = set()
for tag in soup.find_all(["span", "p", "div", "h1", "h2", "h3", "h4", "td"]):
    text = tag.get_text().strip()
    if len(text) > 20:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(w in txt_clean for w in ["Angelica", "Schicchi", "Parelios", "June", "2026", "Festival", "performing", "venue", "tickets"]):
            found.add(txt_clean)
            print(" -", txt_clean[:200])
