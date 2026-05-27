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
        print(f"Title: {display_name}")
        print("All Keys and Values:")
        for k, v in attrs.items():
            if v is not None and v != "" and k not in ['relationTitle', 'createdAt', 'updatedAt', 'publishedAt']:
                # If the value is a dict or list, dump it clean
                if isinstance(v, (dict, list)):
                    print(f"  {k}: {json.dumps(v)[:300]}")
                else:
                    print(f"  {k}: {v}")
