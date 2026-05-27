import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_upcoming.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for item in data.get('data', []):
    attrs = item.get('attributes', {})
    display_name = attrs.get('DisplayName')
    if display_name and "Glenn Gould School Spring Opera" in display_name:
        print(f"\nID: {item.get('id')}")
        desc_list = attrs.get('Description', [])
        for block in desc_list:
            if 'text' in block:
                print("DESCRIPTION TEXT:")
                print(block['text'])
        # Also print image URL
        img_data = attrs.get('EventImage', {}).get('data', {})
        if img_data:
            img_attrs = img_data.get('attributes', {})
            print("IMAGE URL:", img_attrs.get('url'))
