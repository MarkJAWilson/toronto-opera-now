import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_api_sample.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Scanned concerts from API:")
for item in data.get('data', []):
    attrs = item.get('attributes', {})
    display_name = attrs.get('DisplayName')
    sub_heading = attrs.get('SubHeading')
    venue = attrs.get('Venue')
    date = attrs.get('Date')
    time = attrs.get('Time')
    school = attrs.get('School')
    slug = attrs.get('slug')
    
    # Check if this concert is an opera or belongs to GGS
    if school == "GGS" or (display_name and "opera" in display_name.lower()) or (sub_heading and "opera" in sub_heading.lower()):
        print(f"\nID: {item.get('id')}")
        print(f"Title: {display_name}")
        print(f"Subheading: {sub_heading}")
        print(f"Date: {date}")
        print(f"Time: {time}")
        print(f"School: {school}")
        print(f"Venue: {venue}")
        print(f"Slug: {slug}")
