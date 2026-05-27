from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/oa_curl.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")
print("=== OA CURL TEXT SEARCH ===")
# Search for image links inside HTML, stylesheets, or text
found = set()
for tag in soup.find_all(['span', 'p', 'div', 'a', 'script', 'style']):
    text = str(tag)
    # Search for patterns like .jpg, .png, .gif, .webp
    urls = re.findall(r'https?://[^\s"\'>]+\.(?:jpg|png|gif|webp|jpeg|svg)', text, re.IGNORECASE)
    for u in urls:
        if u not in found:
            found.add(u)
            print("  Image URL:", u)

print("\n=== STYLESHEET OR LINK IMAGES ===")
for link in soup.find_all('link'):
    href = link.get('href')
    if href and any(ext in href.lower() for ext in ['.jpg', '.png', '.svg', '.webp']):
        print("  Link image:", href)
