import os
from PIL import Image, ImageFilter, ImageOps

ASSETS_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\assets\covers"
os.makedirs(ASSETS_DIR, exist_ok=True)

TARGET_W, TARGET_H = 1200, 675

def make_editorial_cover(source_path, crop_box, output_path, bg_color=(24, 24, 27)):
    im = Image.open(source_path)
    cropped = im.crop(crop_box)
    
    # Create 1200x675 canvas
    canvas = Image.new("RGB", (TARGET_W, TARGET_H), bg_color)
    
    # Scale cropped portrait to fit height nicely (e.g. height 675)
    scale = TARGET_H / cropped.height
    new_w = int(cropped.width * scale)
    new_h = TARGET_H
    resized = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    # If portrait is narrower than 1200, we create a subtle blurred background from the portrait itself
    # or center it on an elegant dark editorial backdrop
    blurred_bg = cropped.resize((TARGET_W, TARGET_H), Image.Resampling.LANCZOS)
    blurred_bg = blurred_bg.filter(ImageFilter.GaussianBlur(radius=30))
    # Dim the blurred background slightly for sleek contrast
    dark_overlay = Image.new("RGB", (TARGET_W, TARGET_H), (15, 15, 20))
    blurred_bg = Image.blend(blurred_bg, dark_overlay, alpha=0.45)
    
    # Paste blurred background
    canvas.paste(blurred_bg, (0, 0))
    
    # Center the crisp subject portrait
    offset_x = (TARGET_W - new_w) // 2
    canvas.paste(resized, (offset_x, 0))
    
    canvas.save(output_path, "JPEG", quality=92)
    print(f"Generated clean HD cover: {output_path} (Size: {canvas.size})")

# 1. Malaak Compton-Rock: crop from test_malaak.jpg
# (test_malaak is 1000x600, Malaak portrait is on left, watermark is at bottom left)
make_editorial_cover(
    "test_malaak.jpg",
    (50, 15, 465, 465),
    os.path.join(ASSETS_DIR, "malaak-compton-rock-cover.jpg")
)

# 2. Doug Robbie: crop from test_doug.jpg
# (test_doug is 1671x1007, Doug Robbie is on right: x=980 to 1660, y=20 to 990)
make_editorial_cover(
    "test_doug.jpg",
    (980, 20, 1660, 990),
    os.path.join(ASSETS_DIR, "doug-robbie-cover.jpg")
)

# 3. Logan Romero Plant: crop from test_logan.jpg
# (test_logan is 1006x608, Logan is on left: crop avoiding top right blue line: x=10 to 445, y=10 to 470)
make_editorial_cover(
    "test_logan.jpg",
    (10, 10, 445, 470),
    os.path.join(ASSETS_DIR, "logan-romero-plant-cover.jpg")
)
