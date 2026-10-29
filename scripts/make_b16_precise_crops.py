import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Dalia Asafi: gh_dalia.jpg (1600x900)
# Cover: Dalia in blue hijab (left side: x 30 to 450, y 100 to 720)
# Or Dalia in green hijab (right side: x 980 to 1550, y 80 to 750)
im_dalia = Image.open(os.path.join(ART_DIR, "gh_dalia.jpg"))
crop_dalia_blue = im_dalia.crop((40, 100, 440, 680))
crop_dalia_blue.save(os.path.join(ART_DIR, "crop_dalia_blue.jpg"))

crop_dalia_green = im_dalia.crop((980, 80, 1550, 750))
crop_dalia_green.save(os.path.join(ART_DIR, "crop_dalia_green.jpg"))

# 2. Cody Herpin: gh_cody.jpg (1600x900)
im_cody = Image.open(os.path.join(ART_DIR, "gh_cody.jpg"))
# Cody face on left: x: 100 to 580, y: 80 to 720
crop_cody_solo = im_cody.crop((110, 80, 560, 720))
crop_cody_solo.save(os.path.join(ART_DIR, "crop_cody_solo.jpg"))

# Cody with Jodie Sweetin & baby Zoie on right: x 820 to 1580, y 30 to 750
crop_cody_family = im_cody.crop((820, 30, 1580, 750))
crop_cody_family.save(os.path.join(ART_DIR, "crop_cody_family.jpg"))

# 3. Peta Gibb: gh_peta.jpg (1600x900)
im_peta = Image.open(os.path.join(ART_DIR, "gh_peta.jpg"))
# Peta face on left: x 0 to 450, y 0 to 700
crop_peta_solo = im_peta.crop((0, 0, 450, 700))
crop_peta_solo.save(os.path.join(ART_DIR, "crop_peta_solo.jpg"))

# Andy Gibb on right: x 850 to 1550, y 40 to 780
crop_andy_solo = im_peta.crop((850, 40, 1550, 780))
crop_andy_solo.save(os.path.join(ART_DIR, "crop_andy_solo.jpg"))

print("Precise crops saved successfully!")
