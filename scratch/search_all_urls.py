import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Searching for hidden performance/event links:")
# Find strings like "/performance/event/some-slug" or "performance/event"
links = re.findall(r'\"([^\"]*performance/event[^\"]*)\"', html)
print(f"Found {len(links)} links in JSON strings:")
for l in list(set(links))[:20]:
    print("  ", l)
    
# Let's also look for `/events/` or `/concerts/` slugs
links2 = re.findall(r'\"([^\"]*rcmusic\.com/events/[^\"]*)\"', html)
print(f"Found {len(links2)} external links:")
for l in list(set(links2))[:20]:
    print("  ", l)
    
# Let's search for "Katya" or "flute" or "fledermaus" or "marriage" or "cendrillon" or "boheme" in the entire raw HTML file
print("\nSearching for opera title keywords in raw HTML:")
keywords = ["fledermaus", "flute", "magic", "figaro", "marriage", "cendrillon", "boheme", "alcina", "dido", "rinaldo", "orfeo", "oratorio", "schicchi", "angelica", "kabanova", "medium", "earnest", "lucia", "lammermoor", "cosi", "tutte", "traviata"]
for kw in keywords:
    matches = list(re.finditer(kw, html, re.IGNORECASE))
    if matches:
        print(f"  Keyword '{kw}': found {len(matches)} matches")
        # Print first match context
        m = matches[0]
        print(f"    Context: ... {html[max(0, m.start()-50):min(len(html), m.end()+100)].strip()} ...")
