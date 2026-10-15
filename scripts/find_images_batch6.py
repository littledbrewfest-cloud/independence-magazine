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
        # Bing embeds image URLs in m="{...&quot;murl&quot;:&quot;URL&quot;...}"
        murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
        print(f"[{query}] found {len(murls)} image candidate URLs")
        return murls[:10]
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

candidates = {
    'kelly_tisdale': 'Kelly Tisdale Mike Myers',
    'alex_cowper_smith': 'Alex Cowper-Smith Alice Eve',
    'amanda_moye_brown': 'Amanda Moye Brown Wes Brown'
}

results = {}
for key, q in candidates.items():
    results[key] = search_bing_images(q)

with open('batch6_candidate_images.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Saved candidate URLs to batch6_candidate_images.json")
