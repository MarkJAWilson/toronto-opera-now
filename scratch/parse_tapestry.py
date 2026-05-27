from bs4 import BeautifulSoup
import re

with open("scratch/tapestry_home.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Tapestry Opera Web Page Analysis")
print("=" * 40)

# Print all text that has "Madhouse" or "2026" or "2027"
for parent in soup.find_all(text=re.compile(r'Madhouse|2026|2027|Season|Show|June|September|October|November|December|January|February|March|April|May', re.IGNORECASE)):
    text = parent.strip()
    if text and len(text) > 10:
        print("Text:", text)

# Let's find all links and print their text and href
print("\nLinks:")
for a in soup.find_all('a'):
    href = a.get('href')
    text = a.get_text().strip()
    if href and ('show' in href.lower() or 'production' in href.lower() or 'event' in href.lower() or 'ticket' in href.lower() or 'box-office' in href.lower() or len(text) > 5):
        print(f"  {text} -> {href}")
