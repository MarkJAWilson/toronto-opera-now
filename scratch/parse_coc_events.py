from bs4 import BeautifulSoup
import json

with open("scratch/coc_season.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

events = []
for item in soup.find_all(class_='event-item'):
    link_el = item.find('a', class_='event-item__link')
    if not link_el:
        continue
    
    href = link_el.get('href')
    link = "https://www.coc.ca" + href if href.startswith('/') else href
    
    # Image
    img_el = item.find('img', class_='event-item__image')
    image_url = ""
    if img_el:
        image_url = img_el.get('src')
    
    # Title
    title_el = item.find('h3', class_='event-item__title')
    title = title_el.get_text().strip() if title_el else ""
    
    # Composer
    suffix_el = item.find('span', class_='event-item__suffix')
    composer = suffix_el.get_text().strip() if suffix_el else ""
    
    # Date & Venue
    date_el = item.find('span', class_='event-item__date')
    date = date_el.get_text().strip() if date_el else ""
    
    venue_el = item.find('span', class_='event-item__venue')
    venue = venue_el.get_text().strip() if venue_el else ""
    
    events.append({
        'company': 'Canadian Opera Company',
        'title': title,
        'composer': composer,
        'date': date,
        'venue': venue,
        'link': link,
        'image': image_url
    })

print(json.dumps(events, indent=2))
with open("scratch/coc_events.json", "w", encoding="utf-8") as f:
    json.dump(events, f, indent=2)
