from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_links(filename):
    print(f"\nLinks in {filename}:")
    with open(f"scratch/{filename}", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.find_all('a'):
        href = a.get('href')
        text = a.get_text().strip()
        if href and (re.search(r'pagliacci|orpheus|underworld|macina|vivavoce|season|ticket', href, re.IGNORECASE) or len(text) > 5):
            print(f"  {text} -> {href}")

extract_links("tco_season.html")
extract_links("tco_home.html")
