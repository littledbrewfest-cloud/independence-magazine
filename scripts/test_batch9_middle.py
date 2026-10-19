import os
from PIL import Image

art_dir = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Cathleen middle: test_cathleen2.jpg (1603x1020)
im_c = Image.open("test_cathleen2.jpg")
# Target 16:9 -> w=1440, h=810
crop_c_mid = im_c.crop((80, 100, 1520, 910))
crop_c_mid.thumbnail((600, 400))
crop_c_mid.save(os.path.join(art_dir, "crop_cathleen_mid.jpg"), "JPEG")

# 2. Rishia middle: test_rishia1.jpg (1120x888)
im_r = Image.open("test_rishia1.jpg")
# Target 16:9 -> w=1000, h=562
crop_r_mid = im_r.crop((60, 100, 1060, 662))
crop_r_mid.thumbnail((600, 400))
crop_r_mid.save(os.path.join(art_dir, "crop_rishia_mid.jpg"), "JPEG")

# 3. Laurie middle: test_laurie1.jpg (2400x1200)
im_l = Image.open("test_laurie1.jpg")
# Target 16:9 -> w=1920, h=1080
crop_l_mid = im_l.crop((100, 60, 2300, 1140))
crop_l_mid.thumbnail((600, 400))
crop_l_mid.save(os.path.join(art_dir, "crop_laurie_mid.jpg"), "JPEG")

print("All 3 middle previews saved!")
