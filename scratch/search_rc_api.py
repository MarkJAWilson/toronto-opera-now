import re

with open("scratch/rc_calendar.html", "r", encoding="utf-8") as f:
    html = f.read()

print("Searching RCM Calendar for API URLs:")
urls = re.findall(r'https?://[^\s"\'\\<>]+', html)
api_urls = [u for u in urls if 'api' in u.lower() or 'graphql' in u.lower() or 'query' in u.lower() or 'search' in u.lower() or 'concerts' in u.lower()]
print(f"Found {len(api_urls)} API-like URLs:")
for u in list(set(api_urls))[:20]:
    print("  ", u)
