# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Anna Kate Denver (avoid watermark on right):
im1 = Image.open(os.path.join(ART_DIR, "gh_anna-kate-denver.jpg"))
c1 = im1.crop((70, 150, 560, 750))
c1.save(os.path.join(ART_DIR, "clean_anna_crop.jpg"))

# 2. Shelley Covel Rowland (avoid watermark at bottom left):
im2 = Image.open(os.path.join(ART_DIR, "gh_shelley-covel-rowland.jpg"))
c2 = im2.crop((830, 20, 1340, 660))
c2.save(os.path.join(ART_DIR, "clean_shelley_crop.jpg"))

# 3. Steven Cauble (avoid watermark at bottom left):
im3 = Image.open(os.path.join(ART_DIR, "gh_steven-cauble.jpg"))
c3 = im3.crop((960, 40, 1560, 750))
c3.save(os.path.join(ART_DIR, "clean_steven_crop.jpg"))

print("Clean crops saved!")
