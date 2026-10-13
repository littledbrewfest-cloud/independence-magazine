import urllib.request
import urllib.parse
import json
import re

def get_images(query):
    url = 'https://duckduckgo.com/?q=' + urllib.parse.quote(query) + '&iax=images&ia=images'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    res = urllib.request.urlopen(req).read().decode('utf-8')
    lines = [l for l in res.splitlines() if 'vqd' in l]
    print("Found vqd lines:", lines[:3])
    m = re.search(r'vqd=([0-9-]+)', res)
    if not m:
        m = re.search(r'vqd="([^"]+)"', res)
    if not m:
        print("No vqd token found")
        return []
    token = m.group(1)
    print("Found vqd token:", token)
    api_url = f"https://duckduckgo.com/i.js?l=us-en&o=json&q={urllib.parse.quote(query)}&vqd={token}"
    try:
        req2 = urllib.request.Request(api_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'Referer': 'https://duckduckgo.com/'
        })
        content = urllib.request.urlopen(req2).read().decode('utf-8')
        data = json.loads(content)
        print("Got results count:", len(data.get('results', [])))
    except Exception as e:
        print("Error fetching api_url:", e)
        return []
    results = []
    for r in data.get('results', []):
        results.append({
            'title': r.get('title'),
            'image': r.get('image'),
            'width': r.get('width'),
            'height': r.get('height')
        })
    return results

if __name__ == '__main__':
    for item in get_images('Elly Castle John Schneider')[:5]:
        print(item)
