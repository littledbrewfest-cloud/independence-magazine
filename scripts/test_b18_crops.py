# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

for fn in ["gh_anna-kate-denver.jpg", "gh_shelley-covel-rowland.jpg", "gh_steven-cauble.jpg"]:
    fp = os.path.join(ART_DIR, fn)
    with Image.open(fp) as im:
        print(f"{fn} size: {im.size}")
        # Save a half-size preview for quick inspection
        prev = im.resize((800, 450))
        prev_name = fn.replace(".jpg", "_prev.jpg")
        prev.save(os.path.join(ART_DIR, prev_name))
        print(f"Saved {prev_name}")

print("Previews saved!")
