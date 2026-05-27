import json
from bs4 import BeautifulSoup
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open("scratch/rc_calendar.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
script = soup.find('script', id='__NEXT_DATA__')

if script:
    print("Found __NEXT_DATA__!")
    try:
        data = json.loads(script.string)
        # Save to file to analyze
        with open("scratch/rc_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Saved raw data to scratch/rc_data.json")
        
        # Let's search for events
        # Next.js props are usually in props.pageProps.events or props.pageProps.fallback or props.pageProps.dehydratedState
        # Let's search recursively for keys that look like event listings
        events = []
        def find_events(obj):
            if isinstance(obj, dict):
                if 'title' in obj and 'startDate' in obj and ('opera' in str(obj).lower() or 'glenn gould' in str(obj).lower()):
                    events.append(obj)
                for k, v in obj.items():
                    find_events(v)
            elif isinstance(obj, list):
                for item in obj:
                    find_events(item)
                    
        find_events(data)
        print(f"Found {len(events)} potential events in JSON data.")
        
        # Print unique events
        seen = set()
        for e in events:
            title = e.get('title')
            date = e.get('startDate') or e.get('date')
            if title and title not in seen:
                seen.add(title)
                print(f"\nTitle: {title}")
                print(f"Date: {date}")
                print(f"Url: {e.get('url') or e.get('eventUrl')}")
                print(f"Venue: {e.get('venue') or e.get('locationName')}")
                # Print keys
                # print("Keys:", e.keys())
    except Exception as e:
        print("Error parsing __NEXT_DATA__:", e)
else:
    print("No __NEXT_DATA__ script found.")
