import os
from PIL import Image

art_dir = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Juanita Vanoy
# test_juanita3.jpg is 1848x2922 (Michael and Juanita at gala)
# Juanita is on the right: x from 950 to 1800, y from 500 to 1800
img_j3 = Image.open("test_juanita3.jpg")
crop_j = img_j3.crop((1000, 550, 1800, 1600))
crop_j.thumbnail((500, 500))
crop_j.save(os.path.join(art_dir, "crop_juanita_portrait.jpg"), "JPEG")

# Middle image: test_juanita4.jpg is 3000x1688 (walking together)
img_j4 = Image.open("test_juanita4.jpg")
crop_j_mid = img_j4.crop((100, 100, 2900, 1650))
crop_j_mid.thumbnail((600, 400))
crop_j_mid.save(os.path.join(art_dir, "crop_juanita_middle.jpg"), "JPEG")

# 2. Deanna Burditt
# test_deanna1.jpg is 2400x1200 (Rick and Deanna)
# Deanna is on the right: x from 1200 to 2200, y from 150 to 1180
img_d1 = Image.open("test_deanna1.jpg")
crop_d = img_d1.crop((1200, 150, 2150, 1180))
crop_d.thumbnail((500, 500))
crop_d.save(os.path.join(art_dir, "crop_deanna_portrait.jpg"), "JPEG")

# Middle image: test_deanna2.jpg is 1925x3000
img_d2 = Image.open("test_deanna2.jpg")
crop_d_mid = img_d2.crop((100, 100, 1850, 1650))
crop_d_mid.thumbnail((600, 400))
crop_d_mid.save(os.path.join(art_dir, "crop_deanna_middle.jpg"), "JPEG")

# 3. Inty Miller
# test_inty3.jpg is 1920x960 (portrait)
img_i3 = Image.open("test_inty3.jpg")
crop_i = img_i3.crop((750, 10, 1550, 950))
crop_i.thumbnail((500, 500))
crop_i.save(os.path.join(art_dir, "crop_inty_portrait.jpg"), "JPEG")

# Middle image: test_inty1.jpg is 4499x3000
img_i1 = Image.open("test_inty1.jpg")
crop_i_mid = img_i1.crop((200, 200, 4300, 2600))
crop_i_mid.thumbnail((600, 400))
crop_i_mid.save(os.path.join(art_dir, "crop_inty_middle.jpg"), "JPEG")

print("Batch 8 crop previews saved successfully!")
