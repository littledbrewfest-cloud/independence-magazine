import os
import urllib.request
import io
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "assets", "covers"))
os.makedirs(ASSETS_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def fetch_image(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as response:
        img_data = response.read()
        return Image.open(io.BytesIO(img_data)).convert('RGB')

def crop_and_resize(img, target_w, target_h):
    w, h = img.size
    target_ratio = target_w / target_h
    current_ratio = w / h

    if current_ratio > target_ratio:
        # Crop width
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        # Crop height
        new_h = int(w / target_ratio)
        top = (h - new_h) // 4  # Focus slightly higher for portraits
        img = img.crop((0, top, w, top + new_h))

    return img.resize((target_w, target_h), Image.Resampling.LANCZOS)

def create_editorial_split_cover(left_url, right_url, left_name, right_name, output_path):
    width, height = 1200, 675
    half_w = (width - 6) // 2  # 597px each with 6px divider

    print(f"Creating cover: {output_path}...")
    left_img = crop_and_resize(fetch_image(left_url), half_w, height)
    right_img = crop_and_resize(fetch_image(right_url), half_w, height)

    canvas = Image.new('RGB', (width, height), (15, 23, 42))
    canvas.paste(left_img, (0, 0))
    canvas.paste(right_img, (half_w + 6, 0))

    draw = ImageDraw.Draw(canvas, 'RGBA')

    # Crimson accent divider line
    draw.rectangle([half_w, 0, half_w + 6, height], fill=(217, 4, 41, 255))

    # Top Brand Badge Pill
    badge_x, badge_y = 30, 28
    badge_w, badge_h = 240, 42
    draw.rounded_rectangle([badge_x, badge_y, badge_x + badge_w, badge_y + badge_h], radius=6, fill=(15, 23, 42, 230), outline=(217, 4, 41, 200), width=1)
    
    try:
        font_logo = ImageFont.truetype(r"C:\Windows\Fonts\georgiab.ttf", 16)
        font_sub = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 10)
        font_names = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 14)
    except Exception:
        font_logo = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_names = ImageFont.load_default()

    draw.text((badge_x + 16, badge_y + 8), "Independence.", fill=(255, 255, 255), font=font_logo)
    draw.text((badge_x + 130, badge_y + 13), "EXCLUSIVE", fill=(217, 4, 41), font=font_sub)

    # Bottom Gradient Overlays for names
    # Left Name Box
    draw.rectangle([0, height - 70, half_w, height], fill=(15, 23, 42, 210))
    draw.rectangle([0, height - 4, half_w, height], fill=(217, 4, 41, 255))
    draw.text((24, height - 46), left_name.upper(), fill=(255, 255, 255), font=font_names)

    # Right Name Box
    draw.rectangle([half_w + 6, height - 70, width, height], fill=(15, 23, 42, 210))
    draw.rectangle([half_w + 6, height - 4, width, height], fill=(217, 4, 41, 255))
    draw.text((half_w + 30, height - 46), right_name.upper(), fill=(255, 255, 255), font=font_names)

    canvas.save(output_path, "JPEG", quality=90)
    print(f"Saved: {output_path}")

def create_middle_image(url, caption_text, output_path):
    width, height = 900, 520
    print(f"Creating middle image: {output_path}...")
    img = crop_and_resize(fetch_image(url), width, height)
    draw = ImageDraw.Draw(img, 'RGBA')

    # Bottom subtle caption bar
    draw.rectangle([0, height - 50, width, height], fill=(15, 23, 42, 200))
    draw.rectangle([0, height - 3, width, height], fill=(217, 4, 41, 255))
    try:
        font_caption = ImageFont.truetype(r"C:\Windows\Fonts\segoeuib.ttf", 13)
    except Exception:
        font_caption = ImageFont.load_default()

    draw.text((20, height - 35), caption_text, fill=(241, 245, 249), font=font_caption)
    img.save(output_path, "JPEG", quality=88)
    print(f"Saved: {output_path}")

# Batch 1 Config
BATCH_CONFIG = [
    {
        "id": "kaynette-williams",
        "left_url": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=800&q=80",
        "right_url": "https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?auto=format&fit=crop&w=800&q=80",
        "left_name": "Kaynette Williams",
        "right_name": "Blake Shelton",
        "middle_url": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=1200&q=80",
        "middle_caption": "Archival Country Spotlight: From Oklahoma High School Sweethearts to Nashville"
    },
    {
        "id": "ian-alexander-sr",
        "left_url": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=800&q=80",
        "right_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
        "left_name": "Ian Alexander Sr.",
        "right_name": "Regina King",
        "middle_url": "https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?auto=format&fit=crop&w=1200&q=80",
        "middle_caption": "Entertainment Executive & Warner Bros VP: Behind Closed Hollywood Doors"
    },
    {
        "id": "kathryn-burrhus",
        "left_url": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
        "right_url": "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=80",
        "left_name": "Kathryn Burrhus",
        "right_name": "Steve Austin",
        "middle_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=1200&q=80",
        "middle_caption": "Texas Sweethearts: The Untold Story of Steve Austin Before the WWE Stardom"
    },
    {
        "id": "mia-weier",
        "left_url": "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=800&q=80",
        "right_url": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&q=80",
        "left_name": "Mia Weier",
        "right_name": "Clea DuVall",
        "middle_url": "https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&w=1200&q=80",
        "middle_caption": "Hollywood Private Sanctum: The Creative Partnership and Marriage of Clea DuVall & Mia Weier"
    }
]

if __name__ == "__main__":
    for item in BATCH_CONFIG:
        cover_path = os.path.join(ASSETS_DIR, f"{item['id']}-cover.jpg")
        middle_path = os.path.join(ASSETS_DIR, f"{item['id']}-middle.jpg")

        create_editorial_split_cover(
            item["left_url"],
            item["right_url"],
            item["left_name"],
            item["right_name"],
            cover_path
        )

        create_middle_image(
            item["middle_url"],
            item["middle_caption"],
            middle_path
        )

    print("All Batch 1 editorial images created successfully!")
