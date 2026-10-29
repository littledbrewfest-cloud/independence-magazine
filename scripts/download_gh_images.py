import urllib.request
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

urls = {
    'gh_dalia.jpg': 'https://guideholic.com/wp-content/uploads/2026/10/Untitled-design-10.jpg',
    'gh_cody.jpg': 'https://guideholic.com/wp-content/uploads/2026/10/Untitled-design-28-1.jpg',
    'gh_peta.jpg': 'https://guideholic.com/wp-content/uploads/2026/10/Untitled-design-17.jpg',
    'gh_haley.jpg': 'https://guideholic.com/wp-content/uploads/2026/10/Untitled-design-10-1.jpg'
}

for fn, u in urls.items():
    fp = os.path.join(ART_DIR, fn)
    try:
        req = urllib.request.Request(u, headers=headers)
        data = urllib.request.urlopen(req, timeout=10).read()
        with open(fp, 'wb') as f:
            f.write(data)
        with Image.open(fp) as im:
            print(f"Downloaded {fn}: {im.size}")
    except Exception as e:
        print(f"Error {fn}: {e}")
