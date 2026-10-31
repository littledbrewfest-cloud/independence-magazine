with open(r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\scripts\rebuild_clean_site.py", encoding="utf-8") as f:
    text = f.read()

import re
schemas = re.findall(r'<script\s+type="application/ld\+json">.*?</script>', text, re.DOTALL)
print("Schemas found in rebuild_clean_site.py template:", len(schemas))
for s in schemas:
    print(s[:300])
    print("...")
