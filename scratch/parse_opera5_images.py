from bs4 import BeautifulSoup
import re

with open("scratch/opera5_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Let's search for Suor Angelica and Parélios sections and find the images in them.
for title in ["Suor Angelica", "Parélios", "Paré", "Threepenny Submarine"]:
    print(f"\nSearching for section: {title}")
    # Find tag containing this title
    element = soup.find(string=re.compile(title, re.IGNORECASE))
    if element:
        # Find the parent div which is a block or section
        parent = element.parent
        while parent and parent.name != 'section' and len(parent.find_all('img')) == 0:
            parent = parent.parent
        
        if parent:
            print("Found section with images:")
            for img in parent.find_all('img'):
                src = img.get('src') or img.get('data-src')
                alt = img.get('alt')
                print(f"  Image: {src} | Alt: {alt}")
        else:
            print("No parent section found with images.")
    else:
        print("Element not found.")
