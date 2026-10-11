import os
import urllib.request
import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

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
    bg = bg.filter(ImageFilter.GaussianBlur(radius=35))
    enhancer = ImageEnhance.Brightness(bg)
    bg = enhancer.enhance(0.40)  # Darken by 60%

    # 2. Foreground Portrait (Sharp, right-aligned)
    # Target height 580px, width ~ 480px with subtle rounded corners
    pw, ph = 460, 560
    # Center crop raw image to pw, ph
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

    # Add rounded mask to portrait
    mask = Image.new('L', (pw, ph), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, pw, ph], radius=16, fill=255)

    # Paste portrait on right side: x = 680, y = 57
    px, py = width - pw - 60, (height - ph) // 2
    
    # Shadow behind portrait
    shadow = Image.new('RGBA', (pw + 30, ph + 30), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow)
    s_draw.rounded_rectangle([10, 10, pw + 20, ph + 20], radius=20, fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=12))
    bg.paste(shadow, (px - 15, py - 10), shadow)

    # Border around portrait
    p_with_border = Image.new('RGB', (pw + 4, ph + 4), (255, 255, 255))
    p_border_mask = Image.new('L', (pw + 4, ph + 4), 0)
    ImageDraw.Draw(p_border_mask).rounded_rectangle([0, 0, pw + 4, ph + 4], radius=18, fill=255)
    
    # Paste
    bg.paste(portrait, (px, py), mask)

    # 3. Typography on Left Side
    draw = ImageDraw.Draw(bg, 'RGBA')

    try:
        font_brand = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 22)
        font_tag = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 13)
        font_name = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 52)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 17)
    except Exception:
        font_brand = ImageFont.load_default()
        font_tag = ImageFont.load_default()
        font_name = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Brand badge at top left
    draw.text((70, 60), "Independence.", fill=(255, 255, 255), font=font_brand)
    # Red dot accent
    draw.text((225, 60), "MAGAZINE", fill=(148, 163, 184), font=ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 11) if os.path.exists(r"C:\Windows\Fonts\arialbd.ttf") else font_tag)

    # Category Pill
    tag_y = 210
    tag_text = f"  {category.upper()} PROFILE  "
    draw.rounded_rectangle([70, tag_y, 230, tag_y + 32], radius=4, fill=(217, 4, 41, 230))
    draw.text((82, tag_y + 8), tag_text.strip(), fill=(255, 255, 255), font=font_tag)

    # Person Name (Large Serif Bold)
    name_lines = name.split(" ")
    if len(name_lines) <= 2:
        draw.text((70, 270), name, fill=(255, 255, 255), font=font_name)
        curr_y = 345
    else:
        # Multi-line
        line1 = " ".join(name_lines[:2])
        line2 = " ".join(name_lines[2:])
        draw.text((70, 260), line1, fill=(255, 255, 255), font=font_name)
        draw.text((70, 325), line2, fill=(255, 255, 255), font=font_name)
        curr_y = 405

    # Crimson underline accent
    draw.rectangle([70, curr_y, 160, curr_y + 4], fill=(217, 4, 41, 255))

    # Subtitle
    draw.text((70, curr_y + 24), subtitle, fill=(226, 232, 240), font=font_sub)
    draw.text((70, curr_y + 54), "Early Life, Career, Family & Latest Updates", fill=(148, 163, 184), font=font_sub)

    bg.save(output_path, "JPEG", quality=92)
    print(f"Created Spark-style cover: {output_path}")

if __name__ == "__main__":
    test_out = r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\assets\covers\test-spark-style.jpg"
    create_spark_style_cover(
        "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=800&q=80",
        "Kaynette Williams",
        "Celebrity",
        "The Untold Life & Journey of Blake Shelton's First Wife",
        test_out
    )
