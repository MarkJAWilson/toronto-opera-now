import re

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Searching for 'Glenn Gould School Opera' occurrences in raw text:")
for m in re.finditer(r'Glenn Gould School Opera', html, re.IGNORECASE):
    print(f"\nMatch at {m.start()}:")
    print(html[max(0, m.start()-200):min(len(html), m.end()+300)])
    print("-" * 50)
    
print("\nSearching for 'Koerner Hall' and 'Opera' occurrences in raw text:")
count = 0
for m in re.finditer(r'Koerner Hall', html, re.IGNORECASE):
    context = html[max(0, m.start()-100):min(len(html), m.end()+150)]
    if 'opera' in context.lower() or 'school' in context.lower() or 'orchestra' in context.lower():
        print(f"\nMatch at {m.start()}:")
        print(context)
        print("-" * 50)
        count += 1
        if count > 10:
            break
