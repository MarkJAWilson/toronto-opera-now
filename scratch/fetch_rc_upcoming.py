import urllib.request
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://cms.rcmusic.com/api/concerts?filters[Date][$gte]=2026-05-25&pagination[pageSize]=100&populate=*"
print(f"Fetching upcoming concerts from: {url}")
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
        res_data = response.read().decode('utf-8', errors='ignore')
        data = json.loads(res_data)
        print("Successfully fetched upcoming concerts, count:", len(data.get('data', [])))
        
        with open("scratch/rc_upcoming.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        print("\nScanning upcoming concerts:")
        for item in data.get('data', []):
            attrs = item.get('attributes', {})
            display_name = attrs.get('DisplayName')
            sub_heading = attrs.get('SubHeading')
            venue = attrs.get('Venue')
            date = attrs.get('Date')
            time = attrs.get('Time')
            school = attrs.get('School')
            slug = attrs.get('slug')
            presenter = attrs.get('Presenter')
            
            # Check for GGS or Opera
            if (school and 'gould' in school.lower()) or (display_name and "opera" in display_name.lower()) or (sub_heading and "opera" in sub_heading.lower()) or (presenter and "gould" in str(presenter).lower()):
                print(f"\nID: {item.get('id')}")
                print(f"Title: {display_name}")
                print(f"Subheading: {sub_heading}")
                print(f"Date: {date}")
                print(f"Time: {time}")
                print(f"School: {school}")
                print(f"Venue: {venue}")
                print(f"Slug: {slug}")
except Exception as e:
    print("Error:", e)
