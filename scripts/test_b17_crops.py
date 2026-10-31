import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Yasmin Abdallah
# gh_yasmin-abdallah.jpg (1600x900)
# Left half: Yasmin sunglasses (x: 20 to 450, y: 30 to 730)
im_yas = Image.open(os.path.join(ART_DIR, "gh_yasmin-abdallah.jpg"))
crop_yas_cov = im_yas.crop((30, 40, 450, 720))
crop_yas_cov.save(os.path.join(ART_DIR, "crop_yasmin_cover.jpg"))

# Middle: Right side of gh_yasmin-abdallah.jpg (Yasmin in black dress: x 800 to 1580, y 40 to 760)
crop_yas_mid = im_yas.crop((800, 30, 1580, 760))
crop_yas_mid.save(os.path.join(ART_DIR, "crop_yasmin_middle.jpg"))

# 2. Nicolo Robert Tucci
# gh_nicolo-robert-tucci.jpg (1600x900)
# Right half: Nicolo (x: 820 to 1550, y: 70 to 800)
im_nic = Image.open(os.path.join(ART_DIR, "gh_nicolo-robert-tucci.jpg"))
crop_nic_cov = im_nic.crop((880, 70, 1480, 780))
crop_nic_cov.save(os.path.join(ART_DIR, "crop_nicolo_cover.jpg"))

# Middle: Stanley and Nicolo side by side (x: 50 to 1550, y: 50 to 780)
crop_nic_mid = im_nic.crop((50, 50, 1550, 780))
crop_nic_mid.save(os.path.join(ART_DIR, "crop_nicolo_middle.jpg"))

# 3. Jillian Beth Gumbel
# gh_jillian-beth-gumbel.jpg (1600x900)
# Left half: Jillian solo close up (x: 20 to 480, y: 30 to 720)
im_jil = Image.open(os.path.join(ART_DIR, "gh_jillian-beth-gumbel.jpg"))
crop_jil_cov = im_jil.crop((20, 30, 460, 720))
crop_jil_cov.save(os.path.join(ART_DIR, "crop_jillian_cover.jpg"))

# Middle: Jillian and husband on right (x: 820 to 1580, y: 30 to 780)
crop_jil_mid = im_jil.crop((820, 30, 1580, 780))
crop_jil_mid.save(os.path.join(ART_DIR, "crop_jillian_middle.jpg"))

print("Batch 17 test crops created successfully!")
