# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

url = "https://guideholic.com/post-sitemap.xml"
try:
    req = urllib.request.Request(url, headers=headers)
    xml = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
    locs = re.findall(r'<loc>(https://guideholic\.com/[^<]+)</loc>', xml)
    print(f"Total URLs in GuideHolic post-sitemap: {len(locs)}")
    for l in locs[-30:]:
        print(" ", l)
except Exception as e:
    print("Error:", e)
