import os
import json
import urllib.request
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

with open(os.path.join(BASE_DIR, 'batch13_candidate_images.json'), 'r') as f:
    candidates = json.load(f)

for key, urls in candidates.items():
    print(f"\nDownloading candidates for {key}...")
    idx = 1
    for u in urls[:6]:
        fn = f"test_b13_{key}_{idx}.jpg"
        save_path = os.path.join(ART_DIR, fn)
        try:
            req = urllib.request.Request(u, headers=headers)
            content = urllib.request.urlopen(req, timeout=8).read()
            with open(save_path, 'wb') as img_out:
                img_out.write(content)
            
            # verify
            im = Image.open(save_path)
            w, h = im.size
            if w >= 400 and h >= 400:
                print(f"  [{idx}] {fn}: Valid image ({w}x{h}) from {u[:60]}")
                idx += 1
            else:
                os.remove(save_path)
        except Exception as e:
            # print(f"  Fail {idx}: {e}")
            if os.path.exists(save_path):
                os.remove(save_path)
