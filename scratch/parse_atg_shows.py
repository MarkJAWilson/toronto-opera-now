from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_show(filename, label):
    print(f"\n================= {label} ({filename}) =================")
    with open(f"scratch/{filename}", "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    print("Headings:")
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = tag.get_text().strip()
        if text:
            print("  -", re.sub(r'\s+', ' ', text))
            
    print("\nInteresting Text Blocks:")
    found = set()
    for tag in soup.find_all(['span', 'p', 'div', 'td', 'a']):
        text = tag.get_text().strip()
        if len(text) > 15:
            txt_clean = re.sub(r'\s+', ' ', text)
            if txt_clean not in found:
                if re.search(r'2025|2026|2027|October|November|December|January|February|March|April|May|June|July|August|September|opera|production|ticket|perform|season|show|stage', txt_clean, re.IGNORECASE):
                    found.add(txt_clean)
                    print("  -", txt_clean[:200])
                    
    print("\nLinks:")
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.get_text().strip()
        if href and ('ticket' in href.lower() or 'opera' in href.lower() or 'season' in href.lower() or 'show' in href.lower() or len(text) > 5):
            print(f"  {text} -> {href}")
            
    print("\nImages:")
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        alt = img.get('alt')
        print(f"  {src} | Alt: {alt}")

parse_show("stories_dont_die.html", "Stories Dont Die")
parse_show("canuck_cantatas.html", "Canuck Cantatas")
