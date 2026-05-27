import os
import re

print("Searching saved HTML files for 'glass':")
for file in os.listdir("scratch"):
    if file.endswith(".html"):
        with open(os.path.join("scratch", file), "r", encoding="utf-8") as f:
            content = f.read()
        matches = list(re.finditer(r'glass', content, re.IGNORECASE))
        if matches:
            print(f"\nIn file {file}: found {len(matches)} matches")
            # Print text context around each match
            for m in matches[:5]:
                start = max(0, m.start() - 100)
                end = min(len(content), m.end() + 100)
                print(f"  Context: ... {content[start:end].strip()} ...")
