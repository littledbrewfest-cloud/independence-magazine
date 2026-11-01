# -*- coding: utf-8 -*-
import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_links(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        links = re.findall(r'href=[\'"](https?://[^\'"]+)[\'"]', html)
        return html, links
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return "", []

print("=== Checking GuideHolic Home & Posts ===")
gh_html, gh_links = fetch_links("https://guideholic.com/")
gh_posts = set()
for l in gh_links:
    m = re.match(r'https://guideholic\.com/([a-z0-9\-]+)/?$', l)
    if m:
        slug = m.group(1)
        if slug not in ['about-us', 'contact-us', 'privacy-policy', 'terms-and-conditions', 'disclaimer', 'category', 'author', 'tag']:
            gh_posts.add(slug)

print(f"Found {len(gh_posts)} post slugs on GuideHolic homepage:")
for p in sorted(list(gh_posts))[:25]:
    print(" ", p)

print("\n=== Checking SparkDaily Home & Posts ===")
sd_html, sd_links = fetch_links("https://sparkdaily.co.uk/")
sd_posts = set()
for l in sd_links:
    m = re.match(r'https://sparkdaily\.co\.uk/([a-z0-9\-]+)/?$', l)
    if m:
        slug = m.group(1)
        if slug not in ['about-us', 'contact', 'privacy-policy', 'terms', 'category', 'tag']:
            sd_posts.add(slug)

print(f"Found {len(sd_posts)} post slugs on SparkDaily homepage:")
for p in sorted(list(sd_posts))[:25]:
    print(" ", p)
