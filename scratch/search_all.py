import os
import re

terms = ["atelier", "tapestry", "madhouse", "orpheus", "vivavoce", "opera5", "apocryphonia", "solt", "gould", "york"]

for term in terms:
    print(f"\nSearching for '{term}':")
    found_count = 0
    for root, dirs, files in os.walk("scratch"):
        for file in files:
            if file.endswith((".py", ".html", ".json", ".txt")):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    matches = list(re.finditer(re.escape(term), content, re.IGNORECASE))
                    if matches:
                        print(f"  {file}: {len(matches)} matches")
                        found_count += 1
                        # For JSON or txt, print snippet if useful
                        if file.endswith(".json") or (file.startswith("parse_") and file.endswith(".py")):
                            for m in matches[:2]:
                                start = max(0, m.start() - 60)
                                end = min(len(content), m.end() + 100)
                                snippet = content[start:end].replace('\n', ' ')
                                print(f"    Snippet: ... {snippet} ...")
                except Exception as e:
                    pass
    if found_count == 0:
        print("  No matches found.")
