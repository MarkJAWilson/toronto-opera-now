from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/solt_performances.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== SOLT PERFORMACE PAGE TEXT BLOCKS ===")
found = set()
for tag in soup.find_all(["span", "p", "div", "h1", "h2", "h3", "h4"]):
    text = tag.get_text().strip()
    if len(text) > 20:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(w in txt_clean for w in ["Medium", "Earnest", "Katya", "Kabanova", "July", "August", "Alumnae"]):
            found.add(txt_clean)
            print(" -", txt_clean[:150])

print("\n=== SOLT IMAGES ===")
for img in soup.find_all("img"):
    src = img.get("src") or img.get("data-src")
    alt = img.get("alt")
    if src and "wixstatic.com" in src and not any(x in src for x in ["instagram", "facebook", "twitter", "X", "SOLTicon"]):
        print(f"Image: {src} | Alt: {alt}")
