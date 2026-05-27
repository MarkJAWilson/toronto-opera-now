from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/ccoc_events.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== CCOC PHANTOM DETAILS ===")
# Find the section containing "Phantom of the Music Room"
for tag in soup.find_all(text=re.compile(r"Phantom of the Music Room", re.IGNORECASE)):
    parent = tag.parent
    while parent and parent.name not in ["div", "section"] and len(parent.get_text()) < 500:
        parent = parent.parent
    if parent:
        print(re.sub(r"\s+", " ", parent.get_text()).strip()[:600])
        print("-" * 50)
        # Look for images and links in this block
        for a in parent.find_all("a"):
            print(f"Link: {a.get_text().strip()} -> {a.get('href')}")
        for img in parent.find_all("img"):
            print(f"Image: {img.get('src') or img.get('data-src')} | Alt: {img.get('alt')}")
