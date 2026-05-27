import re

with open("scratch/coc_season.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's find occurrences of "La Traviata" and show surrounding HTML
for match in re.finditer(r'La Traviata', html):
    start = max(0, match.start() - 500)
    end = min(len(html), match.end() + 1000)
    print(f"=== MATCH AT {match.start()} ===")
    print(html[start:end])
    print("=" * 40)
