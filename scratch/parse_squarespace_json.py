from bs4 import BeautifulSoup
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/opera5_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

print("Squarespace JSON context extraction:")
# Find script tags containing SQUARESPACE_CONTEXT
scripts = soup.find_all('script')
for s in scripts:
    content = s.string if s.string else ""
    if "SQUARESPACE_CONTEXT" in content:
        print("Found SQUARESPACE_CONTEXT in script!")
        # Let's extract the JSON block
        # SQUARESPACE_CONTEXT = { ... };
        match = re.search(r'SQUARESPACE_CONTEXT\s*=\s*(\{.*?\});', content, re.DOTALL)
        if match:
            try:
                ctx = json.loads(match.group(1))
                print("Context parsed successfully!")
                # Let's dump the keys
                print("Keys:", list(ctx.keys()))
                # Look for items
                if 'website' in ctx:
                    print("Website info:", ctx['website'].get('siteTitle'))
            except Exception as e:
                print("Failed to parse JSON:", e)

# Also let's inspect the block elements. Fluid engine uses data-block-type="image"
print("\nFluid Engine Blocks:")
for block in soup.find_all('div', class_='sqs-block-image'):
    block_id = block.get('id')
    # Find text nearby or inside the block
    img = block.find('img')
    src = img.get('src') or img.get('data-src') if img else ""
    alt = img.get('alt') if img else ""
    # Find the nearest text block (e.g. preceding sibling or adjacent)
    # Wix/Squarespace often has layouts where the text and image are inside the same section
    section = block.find_parent('section')
    section_text = section.get_text().strip()[:200] if section else ""
    print(f"Block: {block_id} | Img: {src[:80]} | Alt: {alt} | SectionText: {re.sub(r'\s+', ' ', section_text)}")
