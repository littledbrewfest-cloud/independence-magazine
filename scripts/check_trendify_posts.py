import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

slugs = ['rouba-saadeh', 'jennifer-lynton', 'terrence-duckett', 'armstead-edwards', 'alex-cowper-smith', 'mary-beougher', 'jennifer-youngblood']
for s in slugs:
    url = f'https://trendifymagazine.com/{s}/'
    try:
        html = urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=8).read().decode('utf-8', errors='ignore')
        imgs = re.findall(r'<meta property="og:image" content="([^"]+)"', html)
        titles = re.findall(r'<title>([^<]+)</title>', html)
        h1s = re.findall(r'<h1[^>]*>([^<]+)</h1>', html)
        t = h1s[0] if h1s else (titles[0] if titles else "")
        img = imgs[0] if imgs else "None"
        print(f"[{s}]")
        print(f"  Title: {t}")
        print(f"  Image: {img}")
    except Exception as e:
        print(f"[{s}] Error: {e}")
