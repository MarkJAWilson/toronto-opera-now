from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_html(filename, label):
    print(f"\n================= {label} ({filename}) =================")
    with open(f"scratch/{filename}", "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract headings and interesting text
    found = set()
    print("Headings:")
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4']):
        text = tag.get_text().strip()
        if text:
            print("  -", re.sub(r'\s+', ' ', text))
            
    print("\nInteresting Text Blocks:")
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
        if href and ('ticket' in href.lower() or 'opera' in href.lower() or 'season' in href.lower() or 'show' in href.lower() or 'event' in href.lower() or len(text) > 5):
            print(f"  {text} -> {href}")
            
    print("\nImages:")
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src') or img.get('data-srcset')
        alt = img.get('alt')
        print(f"  {src} | Alt: {alt}")

parse_html("atg_upcoming.html", "AtG Upcoming")
parse_html("solo_events.html", "SOLO Events")
parse_html("ccoc_events.html", "CCOC Events")
