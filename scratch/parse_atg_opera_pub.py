from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/atg_opera_pub.html", "r", encoding="utf-8") as f:
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
            if any(w in txt_clean for w in ["Opera Pub", "Toronto", "June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "2026", "2027", "venue", "tickets", "free", "date", "time"]):
                found.add(txt_clean)
                print("  -", txt_clean[:200])
                
print("\nLinks:")
for a in soup.find_all('a'):
    href = a.get('href')
    text = a.get_text().strip()
    if href and ('ticket' in href.lower() or 'opera' in href.lower() or 'event' in href.lower() or len(text) > 5):
        print(f"  {text} -> {href}")
        
print("\nImages:")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    if src and not any(x in src for x in ["facebook", "twitter", "instagram", "youtube"]):
        print(f"  {src} | Alt: {alt}")
