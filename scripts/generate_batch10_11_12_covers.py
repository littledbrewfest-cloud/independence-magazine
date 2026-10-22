import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
COVERS_DIR = os.path.join(BASE_DIR, "assets", "covers")
ART_DIR = r"C:\Users\Lapzone.pk\.gemini\antigravity\brain\896bc68d-223d-4f88-b2d0-574555754628"
os.makedirs(COVERS_DIR, exist_ok=True)

PROFILES = [
    # Batch 10
    {
        "id": "haley-giraldo",
        "src_image": os.path.join(ART_DIR, "test_haley_2.jpg"),
        "crop_box": (10, 120, 280, 440),
        "name": "Haley Giraldo",
        "category": "Celebrity",
        "subtitle": "Musician & Pat Benatar's Eldest Daughter",
        "cover_filename": "haley-giraldo-cover.jpg"
    },
    {
        "id": "jacqueline-ray",
        "src_image": os.path.join(ART_DIR, "test_jacqueline_1.jpg"),
        "crop_box": (60, 240, 520, 780),
        "name": "Jacqueline Ray",
        "category": "Biography",
        "subtitle": "Former Actress & Tom Selleck's Former Wife",
        "cover_filename": "jacqueline-ray-cover.jpg"
    },
    {
        "id": "sunshine-deia-tutt",
        "src_image": os.path.join(ART_DIR, "test_sun_solo.jpg"),
        "crop_box": (30, 10, 600, 680),
        "name": "Sunshine Deia Tutt",
        "category": "Celebrity",
        "subtitle": "Interior Designer & Chris Kattan's Former Wife",
        "cover_filename": "sunshine-deia-tutt-cover.jpg"
    },
    # Batch 11
    {
        "id": "caroline-fentress",
        "src_image": os.path.join(ART_DIR, "test_caroline_cheatsheet2.jpg"),
        "crop_box": (60, 190, 620, 850),
        "name": "Caroline Fentress",
        "category": "Celebrity",
        "subtitle": "Former Educator & Chris O'Donnell's Wife",
        "cover_filename": "caroline-fentress-cover.jpg"
    },
    {
        "id": "emily-kuchar",
        "src_image": os.path.join(ART_DIR, "test_emily_nextbio.jpg"),
        "crop_box": (420, 110, 760, 520),
        "name": "Emily Kuchar",
        "category": "Celebrity",
        "subtitle": "Former Cheerleader & Zack Greinke's Wife",
        "cover_filename": "emily-kuchar-cover.jpg"
    },
    {
        "id": "tanya-hijazi",
        "src_image": os.path.join(ART_DIR, "candidate_tanya_1.jpg"),
        "crop_box": (370, 200, 780, 680),
        "name": "Tanya Hijazi",
        "category": "Biography",
        "subtitle": "Former Performer & Rick James' Former Wife",
        "cover_filename": "tanya-hijazi-cover.jpg"
    },
    # Batch 12
    {
        "id": "mirka-federer",
        "src_image": os.path.join(ART_DIR, "test_b12_mirka_oscars.jpg"),
        "crop_box": (1500, 420, 2900, 1980),
        "name": "Mirka Federer",
        "category": "Celebrity",
        "subtitle": "Former WTA Player & Roger Federer's Wife",
        "cover_filename": "mirka-federer-cover.jpg"
    },
    {
        "id": "dana-blumberg",
        "src_image": os.path.join(ART_DIR, "test_b12_dana_people.jpg"),
        "crop_box": (0, 50, 920, 1150),
        "name": "Dana Blumberg",
        "category": "Biography",
        "subtitle": "Ophthalmologist & Robert Kraft's Wife",
        "cover_filename": "dana-blumberg-cover.jpg"
    },
    {
        "id": "marshall-coben",
        "src_image": os.path.join(ART_DIR, "test_b12_marshall_solo.jpg"),
        "crop_box": (10, 100, 440, 610),
        "name": "Marshall Coben",
        "category": "Celebrity",
        "subtitle": "TV Producer & Jane Leeves' Husband",
        "cover_filename": "marshall-coben-cover.jpg"
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
        font_name = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 50)
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
    draw.rounded_rectangle([70, tag_y, 240, tag_y + 30], radius=4, fill=(217, 4, 41, 235))
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
        draw.text((70, 312), line2, fill=(255, 255, 255), font=font_name)
        curr_y = 390

    # Crimson underline accent
    draw.rectangle([70, curr_y, 160, curr_y + 4], fill=(217, 4, 41, 255))

    # Subtitles
    draw.text((70, curr_y + 24), item["subtitle"], fill=(226, 232, 240), font=font_sub)
    draw.text((70, curr_y + 54), "Age, Net Worth, Legacy, Family & Life Updates", fill=(148, 163, 184), font=font_sub2)

    cover_path = os.path.join(COVERS_DIR, item["cover_filename"])
    bg.save(cover_path, "JPEG", quality=92)
    print(f"Generated Spark cover: {cover_path}")

if __name__ == "__main__":
    for p in PROFILES:
        generate_cover(p)
    print("All Batches 10, 11, and 12 covers generated successfully!")
