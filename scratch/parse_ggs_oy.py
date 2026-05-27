from bs4 import BeautifulSoup
import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def parse_file(filename):
    path = f"scratch/{filename}"
    if not os.path.exists(path):
        print(f"\nFile {path} does not exist!")
        return
    print(f"\n================= {filename} =================")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Print headings and interesting text
    found = set()
    for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4', 'div', 'td', 'a']):
        text = tag.get_text().strip()
        if len(text) > 15:
            txt_clean = re.sub(r'\s+', ' ', text)
            if txt_clean not in found:
                found.add(txt_clean)
                # Look for dates or season keywords
                if re.search(r'2025|2026|2027|October|November|December|January|February|March|April|May|June|July|August|September|opera|production|ticket', txt_clean, re.IGNORECASE):
                    print("  -", txt_clean[:150])
                    
    # Print links
    print("\nLinks:")
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.get_text().strip()
        if href and ('ticket' in href.lower() or 'opera' in href.lower() or 'season' in href.lower() or 'show' in href.lower() or len(text) > 5):
            print(f"  {text} -> {href}")
            
    # Print images
    print("\nImages:")
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        alt = img.get('alt')
        print(f"  {src} | Alt: {alt}")

parse_file("www_operayork_com_home.html")
parse_file("glenn-gould-school-opera_home.html")
parse_file("events_home.html")
