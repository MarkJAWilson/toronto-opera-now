from bs4 import BeautifulSoup
import re

with open("scratch/coc_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Let's search for the productions
# Typically they are in some grid or card.
# Let's inspect the page content by finding headers like H3 and seeing what is around them.
cards = []
for h3 in soup.find_all(['h2', 'h3', 'h4']):
    text = h3.get_text().strip()
    if text in ["La Traviata", "Cosi fan tutte", "Così fan tutte", "The Turn of the Screw", "Ariadne auf Naxos", "Empire of Wild", "The Elixir of Love", "Come Closer"]:
        print(f"\nFound production: {text}")
        # Look for parent container or adjacent elements
        parent = h3.parent
        # Let's print some info around it to see how the card is structured
        # Find images in parent or siblings
        images = []
        for img in parent.find_all('img'):
            images.append(img.get('src') or img.get('data-src'))
        
        # If no images in parent, look at grandparent
        if not images and parent.parent:
            for img in parent.parent.find_all('img'):
                images.append(img.get('src') or img.get('data-src'))
                
        # Find links
        links = []
        for a in parent.find_all('a'):
            links.append(a.get('href'))
        if not links and parent.parent:
            for a in parent.parent.find_all('a'):
                links.append(a.get('href'))
                
        print("  Images:", list(set(images)))
        print("  Links:", list(set(links)))
