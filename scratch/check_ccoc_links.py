from bs4 import BeautifulSoup
import re

with open("scratch/ccoc_events.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== CCOC ALL LINKS ===")
for a in soup.find_all("a"):
    href = a.get("href")
    text = a.get_text().strip()
    if href and any(word in href.lower() or word in text.lower() for word in ["phantom", "music", "room", "alice", "spider"]):
        print(f"  {text} -> {href}")
