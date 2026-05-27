from bs4 import BeautifulSoup

with open("scratch/coc_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img', class_='event-item__image')[:2]:
    print("SRCSET:", img.get('srcset'))
    print("SRC:", img.get('src'))
