import urllib.request
import urllib.parse
import re
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

def search_bing_images(query):
    encoded = urllib.parse.quote(query)
    url = f"https://www.bing.com/images/search?q={encoded}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        print(f"[{query}] found {len(murls)} image candidate URLs")
        return murls[:12]
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

candidates = {
    'cathleen_oveson': 'Cathleen Oveson Kenny Johnson',
    'rishia_haas': 'Rishia Haas Andrew Zimmern',
    'laurie_holmond': 'Laurie Holmond Snoop Dogg',
    'diana_lasso': 'Diana Lasso Wayne Brady',
    'haley_arnaz': 'Haley Arnaz Desi Arnaz Jr'
}

results = {}
for key, q in candidates.items():
    results[key] = search_bing_images(q)

with open('batch9_candidate_images.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Saved candidate URLs to batch9_candidate_images.json")
