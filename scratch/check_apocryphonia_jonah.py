from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/apocryphonia_eventbrite.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== APOCRYPHONIA JONAH DETAILS ===")

# Try to find text with location or venue
found = set()
for tag in soup.find_all(["span", "p", "div", "h1", "h2", "h3", "h4", "td"]):
    text = tag.get_text().strip()
    if len(text) > 20:
        txt_clean = re.sub(r"\s+", " ", text)
        if txt_clean not in found and any(w in txt_clean for w in ["Jonah", "Jamaica", "June 12", "Event", "About this event", "location", "venue", "Church", "St."]):
            found.add(txt_clean)
            print(" -", txt_clean[:200])

# Look for image
print("\n=== IMAGES ===")
for img in soup.find_all("img"):
    src = img.get("src") or img.get("data-src")
    alt = img.get("alt")
    if src and "eventbrite" in src or (alt and "Jonah" in alt):
        print(f"Image: {src} | Alt: {alt}")
        break
