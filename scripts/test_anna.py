# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

im1 = Image.open(os.path.join(ART_DIR, "gh_anna-kate-denver.jpg"))
# Let's crop Anna Kate face nicely
c1 = im1.crop((260, 160, 750, 750))
c1.save(os.path.join(ART_DIR, "clean_anna_crop3.jpg"))
print("Saved anna 3")
