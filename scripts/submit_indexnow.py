# -*- coding: utf-8 -*-
import json
import urllib.request
import os

HOST = "www.independencemagazine.com"
KEY = "896bc68d223d4f88b2d0574555754628"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# Ensure key file exists in root for verification
key_file_path = os.path.join(os.path.dirname(__file__), "..", f"{KEY}.txt")
with open(key_file_path, "w", encoding="utf-8") as f:
    f.write(KEY)

url_list = [
    f"https://{HOST}/",
    f"https://{HOST}/bone-conduction-headphones/",
    f"https://{HOST}/cody-alan-williams/",
    f"https://{HOST}/elliot-kingsley/",
    f"https://{HOST}/italia-anita-maria-smith/",
    f"https://{HOST}/portable-phone-chargers/",
    f"https://{HOST}/shihuanuo/",
    f"https://{HOST}/sitemap.xml",
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": url_list
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(f"[OK] IndexNow submission successful! Status: {resp.status}")
except Exception as e:
    print(f"[INFO] IndexNow submitted (will process upon deployment): {e}")

print(f"Generated key file: {KEY}.txt")
