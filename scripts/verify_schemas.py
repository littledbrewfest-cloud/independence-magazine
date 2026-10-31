# -*- coding: utf-8 -*-
import re

for slug in ["nicolo-robert-tucci", "yasmin-abdallah", "jillian-beth-gumbel"]:
    path = f"{slug}/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    print(f"=== {slug} ===")
    print(f"Total JSON-LD schemas: {len(scripts)}")
    for i, s in enumerate(scripts, 1):
        types = re.findall(r'"@type":\s*"([^"]+)"', s)
        print(f"  Schema {i}: types = {types}")

print("\nVerification complete!")
