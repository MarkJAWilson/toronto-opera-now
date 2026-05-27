from bs4 import BeautifulSoup
import re

with open("scratch/opera5_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

def show_context(img_url_part):
    img = soup.find('img', src=re.compile(img_url_part))
    if img:
        print(f"\n=== Context for {img_url_part} ===")
        # Walk up to find parent section or row
        parent = img.parent
        for _ in range(5):
            if parent:
                parent = parent.parent
        if parent:
            print(re.sub(r'\s+', ' ', parent.get_text())[:400])
    else:
        print(f"\nImage {img_url_part} not found")

show_context("3.png")
show_context("SeasonAnnouncement")
show_context("4.png")
show_context("5.png")
show_context("6.png")
