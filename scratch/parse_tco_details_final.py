from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_show(filename):
    print(f"\n================= {filename} =================")
    with open(f"scratch/{filename}", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Let's extract all text tags and print clean lines
    lines = []
    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'span', 'p']):
        txt = tag.get_text().strip()
        if len(txt) > 20:
            txt_clean = re.sub(r'\s+', ' ', txt)
            if txt_clean not in lines:
                lines.append(txt_clean)
                
    print("TEXT BLOCKS:")
    for l in lines[:30]:
        print("  -", l)
        
    print("\nIMAGES:")
    for img in soup.find_all('img'):
        src = img.get('src') or img.get('data-src')
        alt = img.get('alt')
        if src and 'wixstatic' in src and not any(x in src for x in ['instagram', 'facebook', 'youtube', 'twitter']):
            print(f"  {src} (Alt: {alt})")

parse_show("tco_pagliacci.html")
parse_show("tco_orpheus.html")
