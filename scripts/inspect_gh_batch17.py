import urllib.request
import re
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

slugs = ['yasmin-abdallah', 'nicolo-robert-tucci', 'jillian-beth-gumbel', 'olivia-rose-cameron', 'toni-dalto']

for s in slugs:
    url = f"https://guideholic.com/{s}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        title_m = re.search(r'<title>([^<]+)</title>', html)
        title = title_m.group(1) if title_m else 'No title'
        
        img_m = re.search(r'https://guideholic\.com/wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|webp)', html)
        img_url = img_m.group(0) if img_m else None
        
        h2s = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        
        print(f"=== {s} ===")
        print("Title:", title)
        print("Image:", img_url)
        print("H2s:", h2s[:6])
        
        if img_url:
            fn = f"gh_{s}.jpg"
            fp = os.path.join(ART_DIR, fn)
            r = urllib.request.Request(img_url, headers=headers)
            data = urllib.request.urlopen(r, timeout=10).read()
            with open(fp, 'wb') as f:
                f.write(data)
            with Image.open(fp) as im:
                print(f"Saved {fn}: {im.size}")
        print()
    except Exception as e:
        print(f"Error {s}: {e}")
