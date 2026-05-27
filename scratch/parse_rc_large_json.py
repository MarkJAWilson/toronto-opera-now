import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's search for script tags containing JSON data.
# Often there's a big JSON string in the script tag, let's search for script tags that contain event data.
# Let's search for "Katya" or "Lucia" or "Orpheus" or "Traviata" or "Medium" or "Glenn Gould" inside all script tags
import html as html_lib

print("Searching scripts for event details...")
# Look for scripts that have "Glenn Gould School Operas" or similar
# Let's look for any script containing "Lucia" or "Katya" or "Glenn Gould"
for i, m in enumerate(re.finditer(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)):
    content = m.group(1)
    if "The Glenn Gould School" in content and len(content) > 10000:
        print(f"\nFound script {i} of length {len(content)}")
        
        # Let's look for standard JSON structures. The script might be JS defining a variable, or it might be raw JSON.
        # Let's find any substring starting with '{' or '[' and see if we can parse it.
        # Often it starts with window.state = { ... } or similar.
        # Let's search for any JSON-like text
        # Let's search for event titles using regex
        # Look for "title" or "name" fields
        titles = re.findall(r'"title"\s*:\s*"([^"]+)"', content)
        print("Titles in script:", len(titles))
        for t in list(set(titles))[:30]:
            print("  - Title:", t)
            
        # Let's search for "The Glenn Gould School Opera" or "GGS Opera" or "Opera"
        print("\nOpera-like titles:")
        for t in list(set(titles)):
            if 'opera' in t.lower() or 'glenn' in t.lower() or 'gould' in t.lower() or 'conservatory' in t.lower() or 'orchestra' in t.lower():
                print("  -", t)
