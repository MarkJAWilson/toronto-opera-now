from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/apocryphonia_collection.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("EVENT CARDS IN COLLECTION:")
# Eventbrite collections usually store details in list items or divs with event JSON or visible text.
# Let's search for text containing event titles and dates.
for card in soup.find_all(['div', 'li']):
    text = card.get_text().strip()
    if "Of Whales and Willpower" in text or "Cabinet of Curiosities" in text or "Collective of Cool Cats" in text or "Bohemian Holiday" in text or "Enchanted Baroque" in text:
        # Check if this div is a container by seeing if it has dates
        # clean and print if it has a date pattern or a link
        cleaned = re.sub(r'\s+', ' ', text)
        if len(cleaned) < 500:
            a = card.find('a')
            href = a.get('href') if a else "No link"
            print(f"\nCard Text: {cleaned[:300]}")
            print(f"Link: {href}")
            print("-" * 50)
