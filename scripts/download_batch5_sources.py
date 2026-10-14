import os
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

urls = [
    ('raw_rouba1.jpg', 'https://www.leggo.it/photos/HIGH/19/55/2241955_michele_morrone_con_la_moglie_rouba_saadeh.jpg'),
    ('raw_rouba2.jpg', 'https://cdn.amomama.com/ba95ef014b173b545ac4f7efd2a26f54.jpg'),
    ('raw_jennifer1.jpg', 'https://cdn.amomama.com/15f60920eb9a0fab0de625397708d9ac.jpg'),
    ('raw_jennifer2.jpg', 'https://c8.alamy.com/comp/PABEK9/los-angeles-ca-march-30-actor-anthony-hopkins-r-with-wife-jennifer-lynton-and-his-best-actor-oscar-for-silence-of-the-lambs-attend-the-64th-annual-academy-awards-on-march-30-1992-at-the-dorothy-chandler-pavilion-in-los-angeles-california-photo-by-barry-kingalamy-stock-photo-PABEK9.jpg'),
    ('raw_diana1.jpg', 'https://cdn.amomama.com/4e5d68fc30f55705c6d4b4f6433f4dd113e450d283f87fc7765de14a53af7d73.jpg'),
    ('raw_diana2.jpg', 'https://cdn.briefly.co.za/images/1120/25d052e614a35366.jpeg?v=1')
]

for fname, url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
            with open(fname, 'wb') as f:
                f.write(data)
            print(f"Downloaded {fname} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed to download {fname}: {e}")
