import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def analyze(url):
    print(f"\n==================== {url} ====================")
    try:
        req = urllib.request.Request(url, headers=headers)
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        
        # Title
        t = re.findall(r'<title>(.*?)</title>', html, re.DOTALL)
        print("Title:", t[0].strip() if t else 'None')
        
        # Meta description
        d = re.findall(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.I)
        print("Meta Description:", d[0].strip() if d else 'None')
        
        # H1, H2s
        h1 = re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
        print("H1:", [re.sub(r'<[^>]+>', '', x).strip() for x in h1])
        h2 = re.findall(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
        print("H2s (first 6):", [re.sub(r'<[^>]+>', '', x).strip() for x in h2[:6]])
        
        # Schemas
        ld_json = re.findall(r'<script\s+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.DOTALL)
        print(f"JSON-LD count: {len(ld_json)}")
        for i, s in enumerate(ld_json):
            print(f"  Schema {i+1}: {s.strip()[:160]}...")
            
        # Tables
        tables = re.findall(r'<table[^>]*>.*?</table>', html, re.DOTALL)
        print(f"Tables count: {len(tables)}")
        
        # Clean text word count
        clean_text = re.sub(r'<[^>]+>', ' ', html)
        words = len(clean_text.split())
        print(f"Estimated total text words on page: {words}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")

analyze('https://guideholic.com/dalia-asafi/')
analyze('https://guideholic.com/cody-herpin/')
