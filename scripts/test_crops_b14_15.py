import os
from PIL import Image

ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"

# 1. Vanessa Villanueva
# Cover from test_b13_vanessa_villanueva_2.jpg (2400x1200), Vanessa on right
im_van = Image.open(os.path.join(ART_DIR, "test_b13_vanessa_villanueva_2.jpg"))
crop_van = im_van.crop((1250, 100, 2150, 1180))
crop_van.save(os.path.join(ART_DIR, "crop_vanessa_cover.jpg"))

# Vanessa middle from test_b13_vanessa_villanueva_4.jpg (1280x720)
im_van_mid = Image.open(os.path.join(ART_DIR, "test_b13_vanessa_villanueva_4.jpg"))
crop_van_mid = im_van_mid.crop((80, 20, 1200, 680))
crop_van_mid.save(os.path.join(ART_DIR, "crop_vanessa_middle.jpg"))

# 2. Joy Ann Richards
# Cover from preview_test_joy3.jpg (600x530)
im_joy = Image.open(os.path.join(ART_DIR, "preview_test_joy3.jpg"))
crop_joy = im_joy.crop((190, 40, 570, 520))
crop_joy.save(os.path.join(ART_DIR, "crop_joy_cover.jpg"))

# Joy Ann middle from preview_test_joy1.jpg (483x600)
im_joy_mid = Image.open(os.path.join(ART_DIR, "preview_test_joy1.jpg"))
crop_joy_mid = im_joy_mid.crop((30, 20, 460, 420))
crop_joy_mid.save(os.path.join(ART_DIR, "crop_joy_middle.jpg"))

# 3. Sacha Stacey
# From preview_test_sacha1.jpg (600x300)
im_sacha = Image.open(os.path.join(ART_DIR, "preview_test_sacha1.jpg"))
# Right half portrait: Martyn & Sacha in pom pom hat (300 to 600, 0 to 300)
# Sacha is on the right: x from 450 to 595, y from 80 to 290
crop_sacha = im_sacha.crop((440, 80, 595, 290))
crop_sacha.save(os.path.join(ART_DIR, "crop_sacha_cover.jpg"))

# Sacha middle: Left side of preview_test_sacha1.jpg (Martyn and Sacha together)
crop_sacha_mid = im_sacha.crop((0, 10, 290, 295))
crop_sacha_mid.save(os.path.join(ART_DIR, "crop_sacha_middle.jpg"))

# 4. Olivia Korenberg
# From cand_olivia_korenberg_1.jpg (2254x3100)
im_olivia = Image.open(os.path.join(ART_DIR, "cand_olivia_korenberg_1.jpg"))
crop_olivia = im_olivia.crop((20, 320, 1150, 2150))
crop_olivia.save(os.path.join(ART_DIR, "crop_olivia_cover.jpg"))

# Olivia middle from cand_olivia_korenberg_3.jpg (2400x1200)
im_olivia_mid = Image.open(os.path.join(ART_DIR, "cand_olivia_korenberg_3.jpg"))
crop_olivia_mid = im_olivia_mid.crop((200, 100, 2200, 1150))
crop_olivia_mid.save(os.path.join(ART_DIR, "crop_olivia_middle.jpg"))

# 5. Diana Lasso
# Cover from cand_diana_lasso_1.jpg (2400x1200), Diana is on right half: x 1200 to 2400
im_diana = Image.open(os.path.join(ART_DIR, "cand_diana_lasso_1.jpg"))
crop_diana = im_diana.crop((1250, 80, 2350, 1180))
crop_diana.save(os.path.join(ART_DIR, "crop_diana_cover.jpg"))

# Diana middle from cand_diana_lasso_1.jpg (both Wayne Brady and Diana Lasso)
crop_diana_mid = im_diana.crop((50, 50, 2350, 1180))
crop_diana_mid.save(os.path.join(ART_DIR, "crop_diana_middle.jpg"))

# 6. Norman Kali
# From cand_norman_kali_1.jpg (1222x1183)
# Norman is on the right: x from 450 to 1100, y from 20 to 800
im_norman = Image.open(os.path.join(ART_DIR, "cand_norman_kali_1.jpg"))
crop_norman = im_norman.crop((500, 20, 1050, 750))
crop_norman.save(os.path.join(ART_DIR, "crop_norman_cover.jpg"))

# Norman middle: full shot of Evangeline Lilly, Norman Kali & baby
crop_norman_mid = im_norman.crop((50, 20, 1180, 850))
crop_norman_mid.save(os.path.join(ART_DIR, "crop_norman_middle.jpg"))

print("All 6 covers & middles test crops generated successfully!")
