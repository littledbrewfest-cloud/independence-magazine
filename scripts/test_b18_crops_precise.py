# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Anna Kate Denver
im1 = Image.open(os.path.join(ART_DIR, "gh_anna-kate-denver.jpg"))
crop_anna_cov = im1.crop((70, 160, 680, 880))
crop_anna_cov.save(os.path.join(ART_DIR, "crop_anna_cover.jpg"))

# 2. Shelley Covel Rowland
# In gh_shelley-covel-rowland.jpg, let's crop Shelley's portrait
im2 = Image.open(os.path.join(ART_DIR, "gh_shelley-covel-rowland.jpg"))
crop_shelley_cov = im2.crop((840, 120, 1300, 780))
crop_shelley_cov.save(os.path.join(ART_DIR, "crop_shelley_cover.jpg"))

# 3. Steven Cauble
im3 = Image.open(os.path.join(ART_DIR, "gh_steven-cauble.jpg"))
crop_steven_cov = im3.crop((880, 40, 1540, 860))
crop_steven_cov.save(os.path.join(ART_DIR, "crop_steven_cover.jpg"))

print("Precise crops created!")
