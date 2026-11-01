# -*- coding: utf-8 -*-
import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Anna Kate centered:
im1 = Image.open(os.path.join(ART_DIR, "gh_anna-kate-denver.jpg"))
c1 = im1.crop((160, 160, 620, 740))
c1.save(os.path.join(ART_DIR, "clean_anna_crop2.jpg"))

# 2. Steven Cauble shifted:
im3 = Image.open(os.path.join(ART_DIR, "gh_steven-cauble.jpg"))
c3 = im3.crop((1020, 40, 1580, 750))
c3.save(os.path.join(ART_DIR, "clean_steven_crop2.jpg"))

print("Saved test crops 2")
