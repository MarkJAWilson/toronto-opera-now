from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/tco_pagliacci.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("PAGLIACCI PAGE ANALYSIS")
keywords = ['date', 'november', 'december', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', '918 bathurst', 'bathurst', 'p.m.', 'pm', 'staged']
found = set()
for tag in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4']):
    text = tag.get_text().strip()
    if len(text) > 10:
        if any(kw in text.lower() for kw in keywords):
            txt_clean = re.sub(r'\s+', ' ', text)
            if txt_clean not in found:
                found.add(txt_clean)
                print("  -", txt_clean)

print("\nIMAGES:")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    if src and 'wixstatic' in src and not any(x in src for x in ['instagram', 'facebook', 'youtube', 'twitter', 'headshot', 'Icon']):
        print(f"  {src} (Alt: {alt})")
