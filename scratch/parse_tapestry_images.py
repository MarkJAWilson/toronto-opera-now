from bs4 import BeautifulSoup

with open("scratch/tapestry_whats_on.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img'):
    print("SRC:", img.get('src'))
    print("ALT:", img.get('alt'))
    print("-" * 30)
