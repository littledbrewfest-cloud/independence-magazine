# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = "https://guideholic.com/steven-cauble/"
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')

ps = re.findall(r'<p>(.*?)</p>', html, re.DOTALL)
print(f"Total paragraphs found: {len(ps)}")
for p in ps[:8]:
    clean = re.sub(r'<[^>]+>', ' ', p).strip()
    if clean:
        print("P:", clean[:180])
        print()
