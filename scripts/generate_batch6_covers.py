import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
COVERS_DIR = os.path.join(BASE_DIR, "assets", "covers")
os.makedirs(COVERS_DIR, exist_ok=True)

PROFILES = [
    {
        "id": "kelly-tisdale",
        "src_image": os.path.join(BASE_DIR, "test_kelly3.jpg"),
        # Kelly Tisdale portrait crop (test_kelly3 is 3000x2003)
        "crop_box": (1550, 150, 2550, 1550),
        "name": "Kelly Tisdale",
        "category": "Celebrity",
        "subtitle": "Scenic Artist, Entrepreneur & Mike Myers' Wife",
        "cover_filename": "kelly-tisdale-cover.jpg",
        "middle_src": os.path.join(BASE_DIR, "test_kelly1.jpg"),
        "middle_crop": (40, 20, 980, 750),
        "middle_filename": "kelly-tisdale-middle.jpg"
    },
    {
        "id": "alex-cowper-smith",
        "src_image": os.path.join(BASE_DIR, "test_alex2.jpg"),
        # Alex Cowper-Smith portrait crop (test_alex2 is 2400x1200)
        "crop_box": (700, 70, 1380, 1150),
        "name": "Alex Cowper-Smith",
        "category": "Biography",
        "subtitle": "Financier, Ex-Goldman Sachs & Alice Eve's Ex-Husband",
        "cover_filename": "alex-cowper-smith-cover.jpg",
        "middle_src": os.path.join(BASE_DIR, "test_alex2.jpg"),
        "middle_crop": (650, 60, 2150, 1150),
        "middle_filename": "alex-cowper-smith-middle.jpg"
    },
    {
        "id": "amanda-moye-brown",
        "src_image": os.path.join(BASE_DIR, "test_amanda1.jpg"),
        # Amanda Moye Brown portrait crop (test_amanda1 is 1600x900)
        "crop_box": (780, 330, 1450, 900),
        "name": "Amanda Moye Brown",
        "category": "Celebrity",
        "subtitle": "Disney Executive Assistant & Wes Brown's Wife",
        "cover_filename": "amanda-moye-brown-cover.jpg",
        "middle_src": os.path.join(BASE_DIR, "test_amanda2.jpg"),
        "middle_crop": (400, 60, 2200, 1180),
        "middle_filename": "amanda-moye-brown-middle.jpg"
    }
]

def generate_cover(item):
    width, height = 1200, 675
    raw_img = Image.open(item["src_image"]).convert("RGB")
    cropped_subject = raw_img.crop(item["crop_box"])

    # 1. Background: Blurred & Darkened version of subject photo
    bg = cropped_subject.resize((width, height), Image.Resampling.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=42))
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.35)

    # 2. Foreground Portrait Box (480 x 570)
    pw, ph = 480, 570
    sw, sh = cropped_subject.size
    target_ratio = pw / ph
    cur_ratio = sw / sh

    if cur_ratio > target_ratio:
        new_w = int(sh * target_ratio)
        left = (sw - new_w) // 2
        p_crop = cropped_subject.crop((left, 0, left + new_w, sh))
    else:
        new_h = int(sw / target_ratio)
        top = (sh - new_h) // 4
        p_crop = cropped_subject.crop((0, max(0, top), sw, min(sh, top + new_h)))

    portrait = p_crop.resize((pw, ph), Image.Resampling.LANCZOS)

    # Rounded corners mask
    mask = Image.new('L', (pw, ph), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, pw, ph], radius=16, fill=255)

    px, py = width - pw - 60, (height - ph) // 2

    # Drop shadow
    shadow = Image.new('RGBA', (pw + 44, ph + 44), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([18, 18, pw + 26, ph + 26], radius=24, fill=(0, 0, 0, 195))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=18))
    bg.paste(shadow, (px - 22, py - 18), shadow)

    # Paste sharp portrait
    bg.paste(portrait, (px, py), mask)

    # 3. Editorial Typography (Left side)
    draw = ImageDraw.Draw(bg, 'RGBA')
    try:
        font_brand = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 22)
        font_tag = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 12)
        font_name = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 52)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 17)
        font_sub2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 14)
    except Exception:
        font_brand = ImageFont.load_default()
        font_tag = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_sub2 = ImageFont.load_default()

    # Top brand badge: Independence. MAGAZINE
    draw.text((70, 58), "Independence.", fill=(255, 255, 255), font=font_brand)
    draw.text((245, 64), "MAGAZINE", fill=(148, 163, 184), font=font_tag)

    # Category Pill
    tag_y = 205
    tag_text = f"{item['category'].upper()} PROFILE"
    draw.rounded_rectangle([70, tag_y, 230, tag_y + 30], radius=4, fill=(217, 4, 41, 235))
    draw.text((82, tag_y + 7), tag_text, fill=(255, 255, 255), font=font_tag)

    # Person Name
    name_lines = item["name"].split(" ")
    if len(name_lines) <= 2:
        draw.text((70, 260), item["name"], fill=(255, 255, 255), font=font_name)
        curr_y = 338
    else:
        line1 = " ".join(name_lines[:2])
        line2 = " ".join(name_lines[2:])
        draw.text((70, 250), line1, fill=(255, 255, 255), font=font_name)
        draw.text((70, 315), line2, fill=(255, 255, 255), font=font_name)
        curr_y = 395

    # Crimson underline accent
    draw.rectangle([70, curr_y, 160, curr_y + 4], fill=(217, 4, 41, 255))

    # Subtitles
    draw.text((70, curr_y + 24), item["subtitle"], fill=(226, 232, 240), font=font_sub)
    draw.text((70, curr_y + 54), "Age, Net Worth, Career, Family & Latest Updates", fill=(148, 163, 184), font=font_sub2)

    cover_path = os.path.join(COVERS_DIR, item["cover_filename"])
    bg.save(cover_path, "JPEG", quality=92)
    print(f"Generated Spark cover: {cover_path}")

    # Generate Middle Editorial Image
    middle_src = item.get("middle_src", item["src_image"])
    raw_middle = Image.open(middle_src).convert("RGB")
    mid_crop = raw_middle.crop(item["middle_crop"])
    
    # Ensure exact 16:9 aspect ratio to eliminate any stretching/distortion
    mw, mh = mid_crop.size
    target_mid_ratio = 16.0 / 9.0
    cur_mid_ratio = mw / mh
    if cur_mid_ratio > target_mid_ratio:
        new_mw = int(mh * target_mid_ratio)
        offset_x = (mw - new_mw) // 2
        mid_crop = mid_crop.crop((offset_x, 0, offset_x + new_mw, mh))
    elif cur_mid_ratio < target_mid_ratio:
        new_mh = int(mw / target_mid_ratio)
        offset_y = (mh - new_mh) // 3
        mid_crop = mid_crop.crop((0, max(0, offset_y), mw, min(mh, offset_y + new_mh)))

    mid_resized = mid_crop.resize((960, 540), Image.Resampling.LANCZOS)
    middle_path = os.path.join(COVERS_DIR, item["middle_filename"])
    mid_resized.save(middle_path, "JPEG", quality=92)
    print(f"Generated Middle image: {middle_path}")

if __name__ == "__main__":
    for p in PROFILES:
        generate_cover(p)
    print("Batch 6 covers and middle photos generated successfully!")
