import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_concerts.html", "r", encoding="utf-8") as f:
    html = f.read()

# Let's find script 35
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html, re.DOTALL)
for i, content in enumerate(scripts):
    if "The Glenn Gould School" in content and len(content) > 10000:
        print(f"Analyzing Script {i} of length {len(content)}:")
        
        # Let's search for some strings
        # GGS usually does opera. Let's search for "opera" and print 100 chars around it
        print("Occurrences of 'opera':")
        for m in re.finditer(r'opera', content, re.IGNORECASE):
            print(f"  - {content[max(0, m.start()-50):min(len(content), m.end()+150)].strip()}")
            print("-" * 30)
            
        print("\nOccurrences of 'Gould':")
        count = 0
        for m in re.finditer(r'Gould', content, re.IGNORECASE):
            print(f"  - {content[max(0, m.start()-50):min(len(content), m.end()+150)].strip()}")
            print("-" * 30)
            count += 1
            if count > 5:
                break
