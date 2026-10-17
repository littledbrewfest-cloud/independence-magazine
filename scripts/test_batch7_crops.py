import os
from PIL import Image

art_dir = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Marisela Vallejos Felix (test_marisela1.jpg is 2400x1200)
img_m1 = Image.open("test_marisela1.jpg")
crop_m = img_m1.crop((200, 40, 1050, 1100))
crop_m.thumbnail((500, 500))
crop_m.save(os.path.join(art_dir, "crop_marisela_portrait.jpg"), "JPEG")

img_m3 = Image.open("test_marisela3.jpg")
crop_m_mid = img_m3.crop((30, 20, 1090, 610))
crop_m_mid.thumbnail((600, 400))
crop_m_mid.save(os.path.join(art_dir, "crop_marisela_middle.jpg"), "JPEG")

# 2. Diane Lou Oswald (test_diane1.jpg is 2122x3000)
img_d1 = Image.open("test_diane1.jpg")
crop_d = img_d1.crop((1100, 380, 2050, 1750))
crop_d.thumbnail((500, 500))
crop_d.save(os.path.join(art_dir, "crop_diane_portrait.jpg"), "JPEG")

img_d2 = Image.open("test_diane2.jpg")
crop_d_mid = img_d2.crop((50, 100, 2050, 1500))
crop_d_mid.thumbnail((600, 400))
crop_d_mid.save(os.path.join(art_dir, "crop_diane_middle.jpg"), "JPEG")

# 3. Samantha Marie Olit (test_sam2.jpg is 2045x3000)
img_s2 = Image.open("test_sam2.jpg")
crop_s = img_s2.crop((120, 420, 950, 1650))
crop_s.thumbnail((500, 500))
crop_s.save(os.path.join(art_dir, "crop_samantha_portrait.jpg"), "JPEG")

img_s1 = Image.open("test_sam1.jpg")
crop_s_mid = img_s1.crop((30, 40, 960, 750))
crop_s_mid.thumbnail((600, 400))
crop_s_mid.save(os.path.join(art_dir, "crop_samantha_middle.jpg"), "JPEG")

print("Batch 7 crop previews saved successfully!")
