from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/tco_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("=== Wix text block extraction from Season page ===")
# Find paragraphs or spans with Pagliacci or Orpheus
for p in soup.find_all(string=re.compile(r'Pagliacci|Orpheus|Underworld|Bathurst|June|November|March|April|May|July|August|September|October|December|January|February', re.IGNORECASE)):
    parent = p.parent
    while parent and parent.name not in ['div', 'section'] and len(parent.get_text()) < 150:
        parent = parent.parent
    if parent:
        print("\nBLOCK TEXT:")
        print(re.sub(r'\s+', ' ', parent.get_text()).strip()[:400])
        print("-" * 50)

# Find images on the season page
print("\n=== Wix image tags ===")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    # If the src contains wixstatic or similar, print it
    if src and ('static.wixstatic.com' in src or 'wix' in src):
        print(f"Image: {src} | Alt: {alt}")
