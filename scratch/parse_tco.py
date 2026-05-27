from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def parse_tco_file(filename):
    print(f"\nAnalyzing {filename}:")
    with open(f"scratch/{filename}", "r", encoding="utf-8") as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    for span in soup.find_all(['span', 'p', 'h1', 'h2', 'h3', 'h4']):
        text = span.get_text().strip()
        if len(text) > 15 and re.search(r'2026|2027|Season|June|October|November|December|January|February|March|April|May|production|ticket|opera', text, re.IGNORECASE):
            text_clean = re.sub(r'\s+', ' ', text)
            print("  -", text_clean[:120])

parse_tco_file("tco_season.html")
parse_tco_file("tco_home.html")
