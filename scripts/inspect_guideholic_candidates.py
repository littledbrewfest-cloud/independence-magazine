import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

slugs = ['dalia-asafi', 'cody-herpin', 'peta-gibb', 'haley-arnaz']

for slug in slugs:
    url = f"https://guideholic.com/{slug}/"
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Get title
        title_m = re.search(r'<title>([^<]+)</title>', html)
        title = title_m.group(1) if title_m else 'No title'
        
        # Get featured image
        img_m = re.search(r'wp-content/uploads/[^"\']+\.(?:jpg|jpeg|png|webp)', html)
        img = img_m.group(0) if img_m else 'No img'
        
        # Get headings (h2)
        h2s = re.findall(r'<h2[^>]*>([^<]+)</h2>', html)
        
        print(f"=== {slug} ===")
        print("Title:", title)
        print("Image:", "https://guideholic.com/" + img if img != 'No img' else 'None')
        print("H2s:", h2s[:5])
        print()
    except Exception as e:
        print(f"Error {slug}: {e}")
