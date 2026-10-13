import urllib.request
import urllib.parse
import re

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

def search_bing(query):
    url = f"https://www.bing.com/images/search?q={urllib.parse.quote(query)}&form=HDRSC2&first=1"
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    # murl pattern: murl&quot;:&quot;(http[^&]+)&quot;
    murls = re.findall(r'murl&quot;:&quot;(https?://[^&]+)&quot;', html)
    print(f"Bing found {len(murls)} images for {query}")
    for u in murls[:5]:
        print("  ", u)
    return murls

if __name__ == '__main__':
    search_bing("Elly Castle John Schneider")
