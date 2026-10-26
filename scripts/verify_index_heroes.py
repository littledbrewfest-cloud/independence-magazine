import re

with open(r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\index.html", encoding="utf-8") as f:
    text = f.read()

heroes = re.findall(r'<h[23] class="hero-(?:main-headline|sub-title)"><a[^>]*>([^<]+)</a>', text)
print("Current Heroes on index.html:")
for i, h in enumerate(heroes, 1):
    print(f"  {i}. {h}")
