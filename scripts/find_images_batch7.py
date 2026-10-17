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
        return murls[:10]
    except Exception as e:
        print(f"Error searching {query}: {e}")
        return []

candidates = {
    'marisela_vallejos_felix': 'Marisela Vallejos Felix Chalino Sanchez',
    'jeremy_yaffe': 'Jeremy Yaffe Alan Arkin',
    'joy_ann_richards': 'Joy Ann Richards Jamie Farr',
    'sacha_stacey': 'Sacha Stacey Martyn Ford',
    'diane_lou_oswald': 'Diane Lou Oswald Woody Harrelson'
}

results = {}
for key, q in candidates.items():
    results[key] = search_bing_images(q)

with open('batch7_candidate_images.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Saved candidate URLs to batch7_candidate_images.json")
