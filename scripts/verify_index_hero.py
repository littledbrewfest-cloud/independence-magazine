# -*- coding: utf-8 -*-
import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r'<article class="hero-main-card"[^>]*>(.*?)</article>', text, re.DOTALL)
if m:
    title_m = re.search(r'<h2[^>]*>(.*?)</h2>', m.group(1))
    print("Hero Title:", title_m.group(1) if title_m else "No title")
    print("Has November 1, 2026?", "November 1, 2026" in m.group(1))
