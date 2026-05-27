from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/tco_home.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("=== Wix text block extraction ===")
# Wix sites typically wrap text blocks in divs or spans with certain inline text
# Let's extract all text segments and search for 80th or anniversary
for p in soup.find_all(text=re.compile(r'80th|anniversary|underworld|orpheus', re.IGNORECASE)):
    # get parent
    parent = p.parent
    # Let's climb up a bit to get the full block
    while parent and parent.name not in ['div', 'section'] and len(parent.get_text()) < 100:
        parent = parent.parent
    if parent:
        print("\nBLOCK TEXT:")
        print(re.sub(r'\s+', ' ', parent.get_text()).strip()[:500])
        print("-" * 50)
