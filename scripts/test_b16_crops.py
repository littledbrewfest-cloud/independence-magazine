import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Dalia Asafi: gh_dalia.jpg (1600x900)
# Right side: Dalia in green hijab (x: 520 to 1050, y: 70 to 780)
im_dalia = Image.open(os.path.join(ART_DIR, "gh_dalia.jpg"))
crop_dalia_cov = im_dalia.crop((530, 80, 1050, 760))
crop_dalia_cov.save(os.path.join(ART_DIR, "test_b16_dalia_cov.jpg"))

crop_dalia_mid = im_dalia.crop((0, 90, 490, 750))
crop_dalia_mid.save(os.path.join(ART_DIR, "test_b16_dalia_mid.jpg"))

# 2. Cody Herpin: gh_cody.jpg (1600x900)
# Left side: Cody closeup portrait (x: 20 to 480, y: 60 to 700)
im_cody = Image.open(os.path.join(ART_DIR, "gh_cody.jpg"))
crop_cody_cov = im_cody.crop((20, 60, 480, 700))
crop_cody_cov.save(os.path.join(ART_DIR, "test_b16_cody_cov.jpg"))

crop_cody_mid = im_cody.crop((540, 30, 1580, 750))
crop_cody_mid.save(os.path.join(ART_DIR, "test_b16_cody_mid.jpg"))

# 3. Peta Gibb: gh_peta.jpg (1600x900)
# Left side: Peta in studio (x: 0 to 480, y: 0 to 740)
im_peta = Image.open(os.path.join(ART_DIR, "gh_peta.jpg"))
crop_peta_cov = im_peta.crop((0, 0, 480, 740))
crop_peta_cov.save(os.path.join(ART_DIR, "test_b16_peta_cov.jpg"))

crop_peta_mid = im_peta.crop((0, 0, 1600, 750))
crop_peta_mid.save(os.path.join(ART_DIR, "test_b16_peta_mid.jpg"))

print("Test crops for Batch 16 generated!")
