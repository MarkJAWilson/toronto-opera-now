from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/tco_pagliacci.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("PAGLIACCI PAGE TEXTS:")
found = set()
for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4']):
    text = tag.get_text().strip()
    if len(text) > 10:
        txt_clean = re.sub(r'\s+', ' ', text)
        if txt_clean not in found:
            found.add(txt_clean)
            print("  -", txt_clean)
