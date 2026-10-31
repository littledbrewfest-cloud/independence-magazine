import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = 'https://guideholic.com/dalia-asafi/'
req = urllib.request.Request(url, headers=headers)
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')

# Extract main entry content
content_m = re.search(r'<div class="entry-content[^"]*"[^>]*>(.*?)</div>\s*<footer', html, re.DOTALL)
if not content_m:
    content_m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)

if content_m:
    article_body = content_m.group(1)
    # clean tags
    p_tags = re.findall(r'<p[^>]*>(.*?)</p>', article_body, re.DOTALL)
    print("Found paragraphs:", len(p_tags))
    for i, p in enumerate(p_tags[:8]):
        text = re.sub(r'<[^>]+>', '', p).strip()
        print(f"P{i+1}: {text[:150]}...")
else:
    print("Could not isolate article body")
