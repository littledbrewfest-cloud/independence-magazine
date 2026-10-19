import urllib.request
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_downloads = [
    # Deanna Burditt
    ('test_deanna1.jpg', 'https://cdn.amomama.com/9fb0452f8348b8ddca25ec8457188c11404197ef2df6f790ffe577d65ab25fe0.jpg'),
    ('test_deanna2.jpg', 'https://cdn.amomama.com/d573b0139fab06d49da2a3eb1dc450625f43fab8a49866784926fa3c0db0e5a1.jpg'),
    ('test_deanna3.jpg', 'https://i.dailymail.co.uk/i/pix/2013/07/22/article-2373115-1AEE7E2D000005DC-326_634x819.jpg'),

    # Sib Hashian
    ('test_sib1.jpg', 'https://cdn.vox-cdn.com/thumbor/uDiTg1uYhlnM3Kwe8biYA5JgTdg=/0x0:500x334/1200x800/filters:focal(210x127:290x207)/cdn.vox-cdn.com/uploads/chorus_image/image/63466041/hashian_facebook.0.jpg'),
    ('test_sib2.jpg', 'https://i.dailymail.co.uk/i/pix/2017/03/23/16/3E8F910600000578-4342982-image-m-26_1490285120640.jpg'),
    ('test_sib3.jpg', 'https://i.dailymail.co.uk/i/pix/2017/03/23/15/3E8F35E600000578-0-image-a-15_1490284287181.jpg'),

    # Inty Miller
    ('test_inty1.jpg', 'https://cdn.amomama.com/8f3ef525ea2fc0b172f93912d7ce531e.jpg'),
    ('test_inty2.jpg', 'https://cdn.amomama.com/756718dacce20ce592981e907717b0a9.jpg'),
    ('test_inty3.jpg', 'https://networthpost.com/wp-content/uploads/2024/03/IntyMiller_Instagram_theonlyprincessinty.jpg')
]

for fname, url in test_downloads:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(fname, 'wb') as f:
                f.write(data)
            img = Image.open(fname)
            print(f"[OK] {fname}: {img.size[0]}x{img.size[1]} ({len(data)} bytes)")
    except Exception as e:
        print(f"[FAIL] {fname}: {e}")
