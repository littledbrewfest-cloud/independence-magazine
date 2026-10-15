import os
from PIL import Image

art_dir = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Kelly Tisdale (test_kelly3.jpg is 3000x2003)
# Let's crop Kelly on right:
img_k3 = Image.open("test_kelly3.jpg")
w, h = img_k3.size
# Kelly is approximately x: 1550 to 2550, y: 150 to 1550
crop_k = img_k3.crop((1550, 150, 2550, 1550))
crop_k.thumbnail((500, 500))
crop_k.save(os.path.join(art_dir, "crop_kelly_portrait.jpg"), "JPEG")

# Kelly middle (test_kelly1.jpg is 1024x1537)
img_k1 = Image.open("test_kelly1.jpg")
crop_k_mid = img_k1.crop((40, 20, 980, 750))
crop_k_mid.thumbnail((600, 400))
crop_k_mid.save(os.path.join(art_dir, "crop_kelly_middle.jpg"), "JPEG")

# 2. Alex Cowper-Smith (test_alex2.jpg is 2400x1200)
img_a2 = Image.open("test_alex2.jpg")
# Alex is on the left
crop_a = img_a2.crop((750, 80, 1450, 1150))
crop_a.thumbnail((500, 500))
crop_a.save(os.path.join(art_dir, "crop_alex_portrait.jpg"), "JPEG")

# Alex middle (test_alex2.jpg or test_alex1.jpg)
crop_a_mid = img_a2.crop((650, 60, 2150, 1150))
crop_a_mid.thumbnail((600, 400))
crop_a_mid.save(os.path.join(art_dir, "crop_alex_middle.jpg"), "JPEG")

# 3. Amanda Moye Brown (test_amanda1.jpg is 1600x900)
img_am1 = Image.open("test_amanda1.jpg")
# Amanda is on the right
crop_am = img_am1.crop((800, 340, 1400, 900))
crop_am.thumbnail((500, 500))
crop_am.save(os.path.join(art_dir, "crop_amanda_portrait.jpg"), "JPEG")

# Amanda middle (test_amanda2.jpg is 2400x1200)
img_am2 = Image.open("test_amanda2.jpg")
crop_am_mid = img_am2.crop((400, 60, 2200, 1180))
crop_am_mid.thumbnail((600, 400))
crop_am_mid.save(os.path.join(art_dir, "crop_amanda_middle.jpg"), "JPEG")

print("Crop previews saved successfully!")
