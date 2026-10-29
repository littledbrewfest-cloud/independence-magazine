import urllib.request
import urllib.parse
import re
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def download_images(query, prefix):
    url = 'https://www.bing.com/images/search?q=' + urllib.parse.quote(query) + '&form=HDRSC2&first=1'
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        print(f"[{query}] found {len(murls)} images")
        saved = 0
        for u in murls:
            if saved >= 4:
                break
            try:
                fn = f"{prefix}_{saved+1}.jpg"
                fp = os.path.join(ART_DIR, fn)
                r = urllib.request.Request(u, headers=headers)
                data = urllib.request.urlopen(r, timeout=8).read()
                with open(fp, 'wb') as f:
                    f.write(data)
                with Image.open(fp) as im:
                    w, h = im.size
                    if w >= 400 and h >= 300:
                        print(f"  [{saved+1}] {fn}: {w}x{h} from {u[:65]}")
                        saved += 1
                    else:
                        im.close()
                        os.remove(fp)
            except Exception:
                if os.path.exists(fp):
                    try:
                        os.remove(fp)
                    except Exception:
                        pass
    except Exception as e:
        print(f"Error {query}: {e}")

download_images("Dalia Asafi Hakeem Olajuwon", "b16_dalia")
download_images("Cody Herpin Jodie Sweetin", "b16_cody")
download_images("Peta Gibb Andy Gibb daughter", "b16_peta")
