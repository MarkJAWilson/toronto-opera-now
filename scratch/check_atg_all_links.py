from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/atg_upcoming.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

print("=== ATG UPCOMING ALL LINKS ===")
for a in soup.find_all("a"):
    href = a.get("href")
    text = a.get_text().strip()
    if href:
        print(f"  {text} -> {href}")
