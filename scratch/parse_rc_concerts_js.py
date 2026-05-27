import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/js/script_23.js", "r", encoding="utf-8") as f:
    content = f.read()

print("Analyzing concerts/page.js script chunk:")
# Search for any endpoint paths, query parameters, or fetch logic
# Let's search for keywords like "fq", "eventseason", "api", "slug", "venues"
print("Occurrences of 'fq' or 'eventseason':")
for m in re.finditer(r'eventseason|fq|cms\.rcmusic', content, re.IGNORECASE):
    print(f"  - {content[max(0, m.start()-50):min(len(content), m.end()+150)].strip()}")
    print("-" * 30)

# Let's search for any strings like "/api/..." or "/concerts/..."
print("\nPaths found in script:")
paths = re.findall(r'\"(/[^\"]+)\"', content)
paths += re.findall(r'\'(/[^\']+)\'', content)
for p in list(set(paths))[:15]:
    print("  ", p)
