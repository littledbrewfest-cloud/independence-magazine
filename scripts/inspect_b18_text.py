# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def inspect(slug):
    url = f"https://guideholic.com/{slug}/"
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text)
    print(f"=== {slug} ===")
    print(text[:1200])
    print()

inspect("shelley-covel-rowland")
inspect("anna-kate-denver")
