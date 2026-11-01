# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

im1 = Image.open(os.path.join(ART_DIR, "gh_anna-kate-denver.jpg"))
c1 = im1.crop((220, 100, 750, 680))
c1.save(os.path.join(ART_DIR, "clean_anna_crop4.jpg"))
print("Saved anna 4")
