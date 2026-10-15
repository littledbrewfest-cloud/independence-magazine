import os
import urllib.request
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_downloads = [
    # Kelly Tisdale
    ('test_kelly1.jpg', 'https://www.hollywoodreporter.com/wp-content/uploads/2014/04/mike_myers_wife_kelly.jpg?w=1024'),
    ('test_kelly2.jpg', 'https://m.media-amazon.com/images/M/MV5BMTkwMTU0MzA5M15BMl5BanBnXkFtZTgwMjE0NDgyNzM@._V1_.jpg'),
    ('test_kelly3.jpg', 'https://cdn.amomama.com/a1c885f0495a6a18ffe5ac0b69a0b37a.jpg'),
    
    # Alex Cowper-Smith
    ('test_alex1.jpg', 'https://cdn.amomama.com/7d59f853e72be859c53daaa6a1f5283c327647cef6afe358bc5261ad9ac3377f.jpeg'),
    ('test_alex2.jpg', 'https://cdn.amomama.com/de817a3528c7c8b0b2deb3b0ab393a5c67f122a08f96e5d0adf12145aff28fe8.jpg'),
    ('test_alex3.jpg', 'https://i.dailymail.co.uk/i/pix/2015/05/15/12/28B4D8BC00000578-3083167-image-a-99_1431688959968.jpg'),
    
    # Amanda Moye Brown
    ('test_amanda1.jpg', 'https://www.thelist.com/img/gallery/inside-hallmark-hunk-wes-browns-relationship-with-wife-amanda/l-intro-1728325659.jpg'),
    ('test_amanda2.jpg', 'https://cdn.amomama.com/6b473d908cf4a4bc398d13719e68dc34.jpg'),
    ('test_amanda3.jpg', 'https://profvalue.com/wp-content/uploads/2020/09/Amanda-Moye-Brown.jpg')
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
