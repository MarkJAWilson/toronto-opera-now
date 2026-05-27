import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Checking matching logic for '2026-05' (May 2026):")
found_any = False
for company in data["companies"]:
    for prod in company["productions"]:
        iso_start = prod.get("isoStart", "")
        iso_end = prod.get("isoEnd", "")
        
        start_month = iso_start[:7]
        end_month = iso_end[:7] if iso_end else start_month
        
        month_key = "2026-05"
        matches = (month_key >= start_month and month_key <= end_month)
        
        if matches:
            found_any = True
            print(f"  Matches: {company['name']} - {prod['title']} (Start: {start_month}, End: {end_month})")

if not found_any:
    print("  No productions matched May 2026!")
