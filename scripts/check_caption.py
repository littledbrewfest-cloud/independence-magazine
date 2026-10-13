import urllib.request
import re

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.dailymail.co.uk/tvshowbiz/article-2872656/Dukes-Hazzard-star-John-Schneider-s-wife-files-divorce-21-years-marriage.html'
try:
    req = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    for line in html.splitlines():
        if '2403373800000578' in line:
            print("DM line:", line[:200])
except Exception as e:
    print("DM error:", e)
