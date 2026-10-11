import os
import urllib.request
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ASSETS_DIR = os.path.join(BASE_DIR, "assets", "covers")
os.makedirs(ASSETS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

def fetch_image(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as response:
        return Image.open(io.BytesIO(response.read())).convert('RGB')

def create_spark_style_cover(person_img_url, name, category, subtitle, output_path):
    width, height = 1200, 675
    raw_img = fetch_image(person_img_url)

    # 1. Background: Stretched, Blurred & Darkened
    bg = raw_img.resize((width, height), Image.Resampling.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=38))
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.38)  # Darken

    # 2. Foreground Portrait (Sharp, right-aligned)
    pw, ph = 470, 570
    w, h = raw_img.size
    ratio = pw / ph
    cur_ratio = w / h
    if cur_ratio > ratio:
        new_w = int(h * ratio)
        left = (w - new_w) // 2
        p_cropped = raw_img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / ratio)
        top = (h - new_h) // 4
        p_cropped = raw_img.crop((0, top, w, top + new_h))
    
    portrait = p_cropped.resize((pw, ph), Image.Resampling.LANCZOS)

    # Mask with rounded corners
    mask = Image.new('L', (pw, ph), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, pw, ph], radius=16, fill=255)

    px, py = width - pw - 60, (height - ph) // 2
    
    # Soft drop shadow
    shadow = Image.new('RGBA', (pw + 40, ph + 40), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([15, 15, pw + 25, ph + 25], radius=22, fill=(0, 0, 0, 180))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=16))
    bg.paste(shadow, (px - 20, py - 15), shadow)

    # Paste portrait
    bg.paste(portrait, (px, py), mask)

    # 3. Typography on Left Side
    draw = ImageDraw.Draw(bg, 'RGBA')

    try:
        font_brand = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 22)
        font_tag = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 13)
        font_name = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 52)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 17)
        font_sub2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 14)
    except Exception:
        font_brand = ImageFont.load_default()
        font_tag = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_sub2 = ImageFont.load_default()

    # Brand badge at top left
    draw.text((70, 60), "Independence.", fill=(255, 255, 255), font=font_brand)
    draw.text((225, 62), "MAGAZINE", fill=(148, 163, 184), font=font_tag)

    # Category Pill
    tag_y = 205
    tag_text = f"  {category.upper()} PROFILE  "
    draw.rounded_rectangle([70, tag_y, 230, tag_y + 32], radius=4, fill=(217, 4, 41, 230))
    draw.text((82, tag_y + 8), tag_text.strip(), fill=(255, 255, 255), font=font_tag)

    # Person Name
    name_lines = name.split(" ")
    if len(name_lines) <= 2:
        draw.text((70, 265), name, fill=(255, 255, 255), font=font_name)
        curr_y = 340
    else:
        line1 = " ".join(name_lines[:2])
        line2 = " ".join(name_lines[2:])
        draw.text((70, 255), line1, fill=(255, 255, 255), font=font_name)
        draw.text((70, 320), line2, fill=(255, 255, 255), font=font_name)
        curr_y = 398

    # Crimson underline accent
    draw.rectangle([70, curr_y, 160, curr_y + 4], fill=(217, 4, 41, 255))

    # Subtitle
    draw.text((70, curr_y + 24), subtitle, fill=(226, 232, 240), font=font_sub)
    draw.text((70, curr_y + 54), "Early Life, Career, Family & Latest Updates", fill=(148, 163, 184), font=font_sub2)

    bg.save(output_path, "JPEG", quality=92)
    print(f"Created Spark-style cover: {output_path}")

ARTICLES_DATA_LIST = [
    {
        "url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=800&q=80",
        "name": "Kaynette Williams",
        "category": "Celebrity",
        "subtitle": "The Untold Story of Blake Shelton's First Wife",
        "filename": "kaynette-williams-cover.jpg"
    },
    {
        "url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80",
        "name": "Ian Alexander Sr.",
        "category": "Biography",
        "subtitle": "Music Executive & Regina King's Ex-Husband",
        "filename": "ian-alexander-sr-cover.jpg"
    },
    {
        "url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
        "name": "Kathryn Burrhus",
        "category": "Celebrity",
        "subtitle": "Stone Cold Steve Austin's First Wife",
        "filename": "kathryn-burrhus-cover.jpg"
    },
    {
        "url": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=800&q=80",
        "name": "Mia Weier",
        "category": "Biography",
        "subtitle": "Inside Her Life With Partner Clea DuVall",
        "filename": "mia-weier-cover.jpg"
    }
]

if __name__ == "__main__":
    for item in ARTICLES_DATA_LIST:
        out_p = os.path.join(ASSETS_DIR, item["filename"])
        create_spark_style_cover(item["url"], item["name"], item["category"], item["subtitle"], out_p)
    print("All 4 Spark-style covers created successfully!")
