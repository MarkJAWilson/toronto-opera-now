import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_upcoming.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("ALL UPCOMING EVENTS FROM RCM API:")
for i, item in enumerate(data.get('data', [])):
    attrs = item.get('attributes', {})
    name = attrs.get('DisplayName')
    date = attrs.get('Date')
    school = attrs.get('School')
    presenter = attrs.get('Presenter')
    print(f"  {i+1}. {name} | Date: {date} | School: {school} | Presenter: {presenter}")
