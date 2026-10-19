import os
from PIL import Image

art_dir = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Cathleen Oveson
# test_cathleen2.jpg is 1603x1020
# Cathleen is on the left: x from 250 to 950, y from 300 to 1020
img_c = Image.open("test_cathleen2.jpg")
crop_c = img_c.crop((320, 320, 850, 980))
crop_c.thumbnail((500, 500))
crop_c.save(os.path.join(art_dir, "test_crop_cathleen.jpg"), "JPEG")

# 2. Rishia Haas
# test_rishia1.jpg is 1120x888
# Rishia is on the right: x from 500 to 950, y from 80 to 750
img_r = Image.open("test_rishia1.jpg")
crop_r = img_r.crop((510, 90, 890, 600))
crop_r.thumbnail((500, 500))
crop_r.save(os.path.join(art_dir, "test_crop_rishia.jpg"), "JPEG")

# 3. Laurie Holmond
# test_laurie1.jpg is 2400x1200
# Laurie is at right: x from 1750 to 2350, y from 180 to 900
img_l = Image.open("test_laurie1.jpg")
crop_l = img_l.crop((1780, 200, 2300, 850))
crop_l.thumbnail((500, 500))
crop_l.save(os.path.join(art_dir, "test_crop_laurie.jpg"), "JPEG")

# 4. Haley Arnaz
# test_haley1.jpg is 2085x1645
# Haley is on the left: x from 50 to 650, y from 180 to 1050
img_h = Image.open("test_haley1.jpg")
crop_h = img_h.crop((60, 180, 600, 950))
crop_h.thumbnail((500, 500))
crop_h.save(os.path.join(art_dir, "test_crop_haley.jpg"), "JPEG")

print("All 4 test crops saved!")
