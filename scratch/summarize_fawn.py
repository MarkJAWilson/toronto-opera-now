import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/parse_fawn_output.txt", "r", encoding="utf-16") as f:
    content = f.read()

lines = content.split("\n")

headings = []
text_blocks = []
links = []
images = []

mode = None
for line in lines:
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
for h in headings[:15]:
    print(f"  {h}")
    
print("\nText Blocks with dates/venues (first 30):")
count = 0
for t in text_blocks:
    if any(yr in t for yr in ["2025", "2026", "2027"]) or any(m in t for m in ["June", "July", "August", "September", "October", "November", "December", "January", "February", "March", "April", "May", "Toronto", "venue", "show", "performance"]):
        print(f"  {t[:200]}")
        count += 1
        if count >= 30:
            break
            
print("\nLinks (first 15):")
for l in links[:15]:
    print(f"  {l}")
    
print("\nImages (first 15):")
for img in images[:15]:
    print(f"  {img}")
