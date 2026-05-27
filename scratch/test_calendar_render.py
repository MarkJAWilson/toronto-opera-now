import json

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

calendarMonths = [
    { "name": "May 2026", "key": "2026-05" },
    { "name": "June 2026", "key": "2026-06" },
    { "name": "July 2026", "key": "2026-07" },
    { "name": "August 2026", "key": "2026-08" },
    { "name": "September 2026", "key": "2026-09" },
    { "name": "October 2026", "key": "2026-10" },
    { "name": "November 2026", "key": "2026-11" },
    { "name": "December 2026", "key": "2026-12" },
    { "name": "January 2027", "key": "2027-01" },
    { "name": "February 2027", "key": "2027-02" },
    { "name": "March 2027", "key": "2027-03" },
    { "name": "April 2027", "key": "2027-04" },
    { "name": "May 2027", "key": "2027-05" }
]

def isProductionInMonth(prod, monthKey):
    isoStart = prod.get("isoStart")
    if not isoStart:
        return False
    startMonth = isoStart[:7]
    isoEnd = prod.get("isoEnd")
    endMonth = isoEnd[:7] if isoEnd else startMonth
    return (monthKey >= startMonth and monthKey <= endMonth)

# Simulate unfiltered productions list (like activeMonthFilter is null)
productions = []
for company in data["companies"]:
    for prod in company["productions"]:
        productions.append({
            **prod,
            "companyName": company["name"]
        })

print("=== Grouping Calendar Events ===")
for m in calendarMonths:
    month_events = [p for p in productions if isProductionInMonth(p, m["key"])]
    print(f"{m['name']} ({m['key']}): {len(month_events)} show(s)")
    for p in month_events:
        print(f"  - {p['companyName']}: {p['title']} ({p['date']})")
