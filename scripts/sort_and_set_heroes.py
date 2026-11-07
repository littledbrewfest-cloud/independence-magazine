import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")
sys.path.append(SCRIPT_DIR)
import articles_database as db

articles = db.ALL_ARTICLES

# Sort by isoDate descending, then by views/id
articles.sort(key=lambda a: (a.get('isoDate', '2026-01-01'), a.get('views', '0')), reverse=True)

# Define heroes and trending for November 3, 2026
HERO_MAIN_SLUG = 'shihuanuo'
HERO_SUB_SLUGS = [
    'lavelda-fann',
    'olivia-rose-cameron',
    'michael-levonchuck',
    'anya-robbie',
    'ann-belsky'
]

TRENDING_MAP = {
    'shihuanuo': 1,
    'lavelda-fann': 2,
    'olivia-rose-cameron': 3,
    'michael-levonchuck': 4,
    'anya-robbie': 5,
    'ann-belsky': 6
}

for a in articles:
    slug = a['slug']
    if slug == HERO_MAIN_SLUG:
        a['isHeroMain'] = True
        a['isHeroSub'] = False
    elif slug in HERO_SUB_SLUGS:
        a['isHeroMain'] = False
        a['isHeroSub'] = True
    else:
        a['isHeroMain'] = False
        a['isHeroSub'] = False

    if slug in TRENDING_MAP:
        a['isTrending'] = True
        a['trendingRank'] = TRENDING_MAP[slug]
    else:
        a['isTrending'] = False
        a.pop('trendingRank', None)

# Save back to DB_FILE cleanly
with open(DB_FILE, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nIndependence Magazine - Article Database\nContains all verified, fact-checked editorial profiles.\n"""\n\n')
    f.write("ALL_ARTICLES = [\n")
    for a in articles:
        f.write("    {\n")
        for k, v in a.items():
            if k == "contentHtml":
                f.write(f'        "{k}": """{v}""",\n')
            elif isinstance(v, str):
                clean_v = v.replace('\\', '\\\\').replace('"', '\\"')
                f.write(f'        "{k}": "{clean_v}",\n')
            else:
                f.write(f'        "{k}": {repr(v)},\n')
        f.write("    },\n")
    f.write("]\n")

print(f"Successfully sorted {len(articles)} articles by date descending and configured heroes & trending for Nov 3, 2026!")
