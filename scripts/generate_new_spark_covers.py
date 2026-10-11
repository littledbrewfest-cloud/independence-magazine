import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "covers")

NEW_PROFILES = [
    {
        "id": "marlene-knaus",
        "source_path": os.path.join(ASSETS_DIR, "cand_marlene_111.jpg"),
        "crop_box": (630, 0, 1108, 616),  # Clean real iconic vintage portrait of Marlene Knaus (no blue divider)
        "name": "Marlene Knaus",
        "category": "Biography",
        "subtitle": "Fashion Icon & Niki Lauda's First Wife",
        "cover_filename": "marlene-knaus-cover.jpg",
        "middle_source": os.path.join(ASSETS_DIR, "cand_marlene_112.jpg"),
        "middle_filename": "marlene-knaus-middle.jpg",
        "middle_caption": "Marlene Knaus with Niki Lauda in the Formula One Paddock"
    },
    {
        "id": "cindy-deangelis-grossman",
        "source_path": os.path.join(ASSETS_DIR, "cand_cindy_8.jpg"),
        "crop_box": (700, 50, 1130, 630),  # Real photo of Cindy DeAngelis Grossman
        "name": "Cindy DeAngelis Grossman",
        "category": "Celebrity",
        "subtitle": "Businesswoman & Herschel Walker's Former Wife",
        "cover_filename": "cindy-deangelis-grossman-cover.jpg",
        "middle_source": None,
        "middle_filename": None,
        "middle_caption": None
    }
]

def make_spark_cover(item):
    width, height = 1200, 675
    raw_full = Image.open(item["source_path"]).convert('RGB')
    cropped_subject = raw_full.crop(item["crop_box"])

    # 1. Background: Blurred & Darkened version of the subject photo
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

    # 3. Editorial Typography
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

    # Top brand badge: Independence. MAGAZINE (with proper spacing)
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
    draw.text((70, curr_y + 54), "Early Life, Career, Family & Latest Updates", fill=(148, 163, 184), font=font_sub2)

    out_p = os.path.join(ASSETS_DIR, item["cover_filename"])
    bg.save(out_p, "JPEG", quality=92)
    print(f"Generated Spark cover: {out_p}")

def make_middle_image(item):
    if not item.get("middle_source"):
        return
    width, height = 960, 540
    raw = Image.open(item["middle_source"]).convert('RGB')
    w, h = raw.size

    target_ratio = width / height
    cur_ratio = w / h
    if cur_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        p_crop = raw.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 3
        p_crop = raw.crop((0, max(0, top), w, min(h, top + new_h)))

    img = p_crop.resize((width, height), Image.Resampling.LANCZOS)
    draw = ImageDraw.Draw(img, 'RGBA')

    # Bottom caption bar
    draw.rectangle([0, height - 52, width, height], fill=(15, 23, 42, 215))
    draw.rectangle([0, height - 4, width, height], fill=(217, 4, 41, 255))

    try:
        font_caption = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 14)
    except Exception:
        font_caption = ImageFont.load_default()

    draw.text((24, height - 36), item["middle_caption"], fill=(241, 245, 249), font=font_caption)

    out_p = os.path.join(ASSETS_DIR, item["middle_filename"])
    img.save(out_p, "JPEG", quality=90)
    print(f"Generated Middle image: {out_p}")

if __name__ == "__main__":
    for p in NEW_PROFILES:
        make_spark_cover(p)
        make_middle_image(p)
    print("NEW profiles generated successfully!")
