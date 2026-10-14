import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for cat in ['biography', 'celebrity']:
    url = f'https://trendifymagazine.com/category/{cat}/'
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        matches = re.findall(r'<a[^>]+href="https://trendifymagazine\.com/([^"/]+)/"[^>]*>([^<]+)</a>', html)
        print(f"=== Trendify {cat} ===")
        seen = set()
        for slug, title in matches:
            slug = slug.strip()
            title = title.strip()
            if slug and title and slug not in seen and len(title) > 15:
                seen.add(slug)
                print(f"  {slug} -> {title}")
    except Exception as e:
        print(f"Error for {cat}:", e)
