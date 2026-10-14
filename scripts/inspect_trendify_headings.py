import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for slug in ['rouba-saadeh', 'jennifer-lynton', 'armstead-edwards']:
    url = f'https://trendifymagazine.com/{slug}/'
    try:
        html = urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=10).read().decode('utf-8', errors='ignore')
        headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', html)
        print(f"=== Headings for {slug} ===")
        for h in headings:
            clean_h = re.sub(r'<[^>]+>', '', h).strip()
            if clean_h and not clean_h.startswith('Related') and not clean_h.startswith('Leave a'):
                print("  -", clean_h)
    except Exception as e:
        print(f"Error {slug}:", e)
