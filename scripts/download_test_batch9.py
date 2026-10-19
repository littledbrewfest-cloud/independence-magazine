import urllib.request
import os
from PIL import Image

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

test_urls = {
    # Cathleen Oveson
    'cathleen1': 'https://cdn.amomama.com/676b8283e689912f9acd7c98fedc6da2ee1629cbd50baff7368385d35be09736.jpg',
    'cathleen2': 'https://i.pinimg.com/originals/67/4f/50/674f508f31b5be7fe3ba9915f4824cac.jpg',
    'cathleen3': 'https://img5.bdbphotos.com/images/orig/4/s/4shc85qbtl5o5lq.jpg?skj2io4l',
    'cathleen4': 'https://marriedwiki.com/uploads/2023/08/15/cathleen-oveson-with-her-husband-kenny-johnson--1692097445.jpg',
    
    # Rishia Haas
    'rishia1': 'https://cdn.briefly.co.za/images/1120/021d98e866776dab.jpeg?v=1',
    'rishia2': 'https://biographytribune.com/wp-content/uploads/2018/07/TopDogNYHotDogCompetitionHostedAndrewmeJsj1ccvrqx.jpg',
    'rishia3': 'https://marriedwiki.com/uploads/article/american-chef-andrew-zimmern-and-her-wife-rishia-haas-married-life.jpg',
    
    # Laurie Holmond
    'laurie1': 'https://cdn.amomama.com/b306247a369891fb5347a6189e55f4fdc4a6130bcb1e3937ee0e8dbaa1dd88a6.jpg',
    'laurie2': 'https://cdn.briefly.co.za/images/1120/4952438823df9d10.jpeg?v=1',
    
    # Diana Lasso
    'diana1': 'https://cdn.amomama.com/50a3cf62d06e1c5486cf28da7c670acd.jpg',
    'diana2': 'https://cdn.amomama.com/4e5d68fc30f55705c6d4b4f6433f4dd113e450d283f87fc7765de14a53af7d73.jpg',
    
    # Haley Arnaz
    'haley1': 'https://cdn.amomama.com/b710f04af16762bd5f5e43447f8e01c7.jpg',
    'haley2': 'https://i.ebayimg.com/images/g/n3YAAOSw7V5msZw9/s-l1200.jpg',
    'haley3': 'https://i.pinimg.com/originals/37/c1/4c/37c14c16af3080919ce5b415cbd30aef.jpg'
}

for name, url in test_urls.items():
    filename = f"test_{name}.jpg"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(filename, 'wb') as out_file:
            out_file.write(resp.read())
        im = Image.open(filename)
        print(f"Downloaded {filename}: size {im.size}, format {im.format}")
    except Exception as e:
        print(f"Failed {name} ({url[:60]}...): {e}")
