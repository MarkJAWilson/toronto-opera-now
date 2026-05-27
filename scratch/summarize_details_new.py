import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/parse_details_new_output.txt", "r", encoding="utf-16") as f:
    content = f.read()

sections = content.split("=================")
for sec in sections:
    if not sec.strip():
        continue
    lines = sec.split("\n")
    title = lines[0].strip()
    print(f"\n================= {title} =================")
    
    headings = []
    text_blocks = []
    links = []
    images = []
    
    mode = None
    for line in lines[1:]:
        if line.startswith("Headings:"):
            mode = "headings"
        elif line.startswith("Interesting Text Blocks:"):
            mode = "text"
        elif line.startswith("Links:"):
            mode = "links"
        elif line.startswith("Images:"):
            mode = "images"
        elif line.strip():
            if mode == "headings":
                headings.append(line.strip())
            elif mode == "text":
                text_blocks.append(line.strip())
            elif mode == "links":
                links.append(line.strip())
            elif mode == "images":
                images.append(line.strip())
                
    print("Headings:")
    for h in headings[:25]:
        print(f"  {h}")
        
    print("\nText Blocks with dates/seasons (first 25):")
    count = 0
    for t in text_blocks:
        if any(yr in t for yr in ["2025", "2026", "2027"]) or any(m in t for m in ["June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May"]):
            print(f"  {t[:200]}")
            count += 1
            if count >= 25:
                break
                
    print("\nLinks:")
    for l in links[:20]:
        print(f"  {l}")
        
    print("\nImages:")
    for img in images[:20]:
        print(f"  {img}")
