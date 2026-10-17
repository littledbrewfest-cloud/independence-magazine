import urllib.request
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_downloads = [
    # Marisela Vallejos Felix
    ('test_marisela1.jpg', 'https://cdn.amomama.com/293b98cee957a44aab8318d815b625efb48fe693a8e944a98dbc20782061a7a9.jpg'),
    ('test_marisela2.jpg', 'https://heraldodemexico.com.mx/u/fotografias/m/2022/5/16/f1280x720-514123_645798_5050.jpg'),
    ('test_marisela3.jpg', 'https://cdn.tuko.co.ke/images/1120/ac95d35e11dd41c5.jpeg?v=1'),
    
    # Joy Ann Richards
    ('test_joy1.jpg', 'https://cdn.amomama.com/82e8fded714823c66248da9200855d58426cfa5b3ae0ffb57ed72e5a0e4b1b43.jpeg'),
    ('test_joy2.jpg', 'https://heightline.com/wp-content/uploads/Jamie-Farr-and-wife-Joy-Ann-Richards.jpg'),
    ('test_joy3.jpg', 'https://cdn.amomama.com/bfaf26a7fa13f658a9247654635a5a96.jpg'),
    
    # Diane Lou Oswald
    ('test_diane1.jpg', 'https://cdn.amomama.fr/79797cb0919c36b692071584a77a13695265f2d2765f6434a4a073be4d877e57.jpg'),
    ('test_diane2.jpg', 'https://cdn.amomama.es/64e5d2619a8625e2af6f594de8770181b1c284e871c53316f31179003749b419.jpg'),
    
    # Sacha Stacey
    ('test_sacha1.jpg', 'https://cdn.amomama.com/50c81bf48ed5b6187f07f3fe372961721558832113f82302febf04610d4bbb48.jpg'),
    ('test_sacha2.jpg', 'https://creeto.com/wp-content/uploads/Martyn-Ford-Wife-Sacha-Stacy-768x916.jpg')
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
