import re

def extract():
    path = 'C:/Users/mark/.gemini/antigravity/brain/415b7b97-d415-43ae-b834-8baa3ee87328/.system_generated/steps/1303/content.md'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Search for all strings matching squarespace CDN or similar image hostings
    cdn_links = re.findall(r'//[^\s"\'>]+?squarespace[^\s"\'>]+', content)
    print("Found CDN strings:")
    for link in set(cdn_links):
        print("  -", link)

if __name__ == '__main__':
    extract()
