from bs4 import BeautifulSoup

with open("scratch/solt_performances.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
print("All images on SOLT Performances Page:")
for img in soup.find_all('img'):
    src = img.get('src') or img.get('data-src')
    alt = img.get('alt')
    print(f"  {src} | Alt: {alt}")
