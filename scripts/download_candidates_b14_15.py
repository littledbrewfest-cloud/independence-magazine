import os
import urllib.request
import urllib.parse
import re
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_bing(q):
    url = f'https://www.bing.com/images/search?q={urllib.parse.quote(q)}&form=HDRSC2&first=1'
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        print(f"[{q}] found {len(murls)} images")
        return murls[:8]
    except Exception as e:
        print(f"[{q}] error: {e}")
        return []

targets = {
    'olivia_korenberg': 'Olivia Korenberg Seann William Scott',
    'diana_lasso': 'Diana Lasso Wayne Brady',
    'yasmin_abdallah': 'Yasmin Abdallah Rufus Sewell',
    'norman_kali': 'Norman Kali Evangeline Lilly'
}

for key, q in targets.items():
    urls = search_bing(q)
    idx = 1
    for u in urls:
        if idx > 3:
            break
        fn = f"cand_{key}_{idx}.jpg"
        save_path = os.path.join(ART_DIR, fn)
        try:
            req = urllib.request.Request(u, headers=headers)
            content = urllib.request.urlopen(req, timeout=8).read()
            with open(save_path, 'wb') as img_out:
                img_out.write(content)
            
            with Image.open(save_path) as im:
                w, h = im.size
                if w >= 400 and h >= 300:
                    print(f"  [{idx}] {fn}: Valid ({w}x{h}) from {u[:55]}")
                    idx += 1
                else:
                    im.close()
                    os.remove(save_path)
        except Exception as e:
            if os.path.exists(save_path):
                try:
                    os.remove(save_path)
                except Exception:
                    pass
