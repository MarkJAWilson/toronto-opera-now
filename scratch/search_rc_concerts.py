from bs4 import BeautifulSoup
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Searching for Glenn Gould School Opera events...")
# We know they have "The Glenn Gould School Operas(2)".
# Let's search for "opera" and print surrounding text in the HTML (ignoring navigation links).
matches = []
for tag in soup.find_all(['div', 'span', 'p', 'h2', 'h3', 'h4', 'a']):
    txt = tag.get_text().strip()
    if "opera" in txt.lower() and "glenn gould" in txt.lower():
        # Clean text
        clean = re.sub(r'\s+', ' ', txt)
        if len(clean) > 15 and len(clean) < 400:
            if clean not in matches:
                matches.append(clean)

for m in matches[:15]:
    print("  -", m)

# Let's write a python script to search for the specific JSON blocks in the HTML
# Next.js or React often stores the data in a window.__PRELOADED_STATE__ or similar script.
print("\nSearching script tags for JSON arrays of events...")
for s in soup.find_all('script'):
    content = s.string if s.string else ""
    if "events" in content or "concerts" in content:
        # Check if it has a large JSON block
        if len(content) > 10000:
            print("Found large script tag, length:", len(content))
            # Let's see if we can extract strings like "Opera" or "Gould"
            operas = re.findall(r'"title"\s*:\s*"([^"]*opera[^"]*)"', content, re.IGNORECASE)
            print("Titles containing 'opera' in this script:")
            for o in set(operas):
                print("  ", o)
                
            dates = re.findall(r'"startDate"\s*:\s*"([^"]*)"', content)
            print("Found dates count:", len(dates))
