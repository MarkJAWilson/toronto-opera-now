import re
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def scan_js(filepath):
    print(f"\nScanning {filepath}:")
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Look for cms.rcmusic.com
    for m in re.finditer(r'cms\.rcmusic\.com', content):
        print("  - Occur:", content[max(0, m.start()-100):min(len(content), m.end()+200)].strip())
        print("-" * 40)
        
    # Search for all strings matching "/api/..." or similar endpoints
    endpoints = re.findall(r'\"(/[^\"]*api/[^\"]*)\"', content)
    endpoints += re.findall(r'\'(/[^\']*api/[^\']*)\'', content)
    if endpoints:
        print("  API endpoints found:")
        for ep in list(set(endpoints))[:10]:
            print("    ", ep)
            
    # Search for any string starting with "http" and containing "rcmusic"
    urls = re.findall(r'https?://[^\s"\'\\<>]+', content)
    rc_urls = [u for u in urls if 'rcmusic' in u]
    if rc_urls:
        print("  RCM URLs found:")
        for ru in list(set(rc_urls))[:10]:
            print("    ", ru)

# Scan script_11.js and script_12.js which we know have matches
scan_js("scratch/js/script_11.js")
scan_js("scratch/js/script_12.js")
