import urllib.request
import json
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8')

endpoints = [
    "https://cms.rcmusic.com/api/concerts?pagination[pageSize]=100",
    "https://cms.rcmusic.com/api/events?pagination[pageSize]=100",
    "https://cms.rcmusic.com/api/performances?pagination[pageSize]=100",
    "https://cms.rcmusic.com/api/shows?pagination[pageSize]=100",
    "https://cms.rcmusic.com/api/concerts?populate=*&pagination[pageSize]=20",
    "https://cms.rcmusic.com/api/events?populate=*&pagination[pageSize]=20"
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for url in endpoints:
    print(f"\nTesting endpoint: {url}")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=8) as response:
            print("Status:", response.status)
            res_data = response.read().decode('utf-8', errors='ignore')
            data = json.loads(res_data)
            print("Successfully parsed JSON!")
            if 'data' in data:
                print("Data length:", len(data['data']))
                if data['data']:
                    # Print first item keys and title
                    first = data['data'][0]
                    print("First item ID:", first.get('id'))
                    print("First item Attributes:", list(first.get('attributes', {}).keys()))
                    attr = first.get('attributes', {})
                    print("First item Title:", attr.get('title') or attr.get('name'))
                    # Let's save a sample of the successful endpoint to a file
                    with open("scratch/rc_api_sample.json", "w", encoding="utf-8") as f_out:
                        json.dump(data, f_out, indent=2)
                    print("Saved sample to scratch/rc_api_sample.json")
                    break
            else:
                print("No 'data' key in response JSON. Keys:", list(data.keys()))
    except Exception as e:
        print("Failed:", e)
