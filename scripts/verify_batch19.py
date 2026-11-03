# -*- coding: utf-8 -*-
import os
import re
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Verify index.html Lead Hero
index_path = os.path.join(BASE_DIR, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_html = f.read()

hero_match = re.search(r'<article class="hero-main-card"[^>]*>.*?<h2[^>]*>(.*?)</h2>.*?By (.*?)</div>.*?<span>(.*?)</span>', index_html, re.DOTALL)
if hero_match:
    print("=== HERO VERIFICATION ===")
    print("Title:", re.sub(r'<[^>]+>', '', hero_match.group(1)).strip())
    print("Author:", hero_match.group(2).strip())
    print("Date:", hero_match.group(3).strip())
else:
    print("ERROR: Hero card not matched in index.html")

# 2. Verify Schemas for Batch 19 articles
batch19_slugs = ["anya-robbie", "ann-belsky", "michael-cannata-jr"]

print("\n=== BATCH 19 SCHEMA & STATIC HTML VERIFICATION ===")
for slug in batch19_slugs:
    file_path = os.path.join(BASE_DIR, slug, "index.html")
    if not os.path.exists(file_path):
        print(f"ERROR: {file_path} does not exist!")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        html = f.read()
    
    # Check Schemas
    schemas = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    schema_types = []
    for s in schemas:
        try:
            parsed = json.loads(s.strip())
            st = parsed.get("@type", "Unknown")
            schema_types.append(st)
        except Exception as e:
            schema_types.append(f"Invalid JSON: {e}")
    
    # Check word count from reader-prose
    article_body = re.search(r'<div class="reader-prose">(.*?)</div>\s*<!-- Internal Linking', html, re.DOTALL)
    body_text = re.sub(r'<[^>]+>', ' ', article_body.group(1)) if article_body else ''
    words = len(body_text.split())
    
    # Check middle image
    mid_img = f"assets/covers/{slug}-middle.jpg"
    has_mid = mid_img in html and os.path.exists(os.path.join(BASE_DIR, mid_img))
    
    print(f"[{slug}]")
    print(f"  - Word Count: {words}")
    print(f"  - Schemas found ({len(schemas)}): {schema_types}")
    print(f"  - 16:9 Middle Image Present: {has_mid}")

# 3. Check Sitemap
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap = f.read()

print("\n=== SITEMAP VERIFICATION ===")
print("Contains anya-robbie:", "anya-robbie" in sitemap)
print("Contains ann-belsky:", "ann-belsky" in sitemap)
print("Contains michael-cannata-jr:", "michael-cannata-jr" in sitemap)
print("Homepage lastmod:", re.search(r'<loc>https://www\.independencemagazine\.com/</loc>\s*<lastmod>([^<]+)</lastmod>', sitemap).group(1))

print("\nBatch 19 Verification Complete!")
