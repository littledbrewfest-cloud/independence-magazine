import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)
import articles_database as db

DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

for a in db.ALL_ARTICLES:
    if a['slug'] == 'andi-rock':
        a['isHeroMain'] = True
        a['isHeroSub'] = False
        a['isTrending'] = True
        a['trendingRank'] = 1
    elif a['slug'] == 'jason-clarkson':
        a['isHeroMain'] = False
        a['isHeroSub'] = True
        a['isTrending'] = True
        a['trendingRank'] = 2
    elif a['slug'] == 'elly-castle':
        a['isHeroMain'] = False
        a['isHeroSub'] = True
        a['isTrending'] = True
        a['trendingRank'] = 3
    elif a['slug'] == 'malaak-compton':
        a['isHeroMain'] = False
        a['isHeroSub'] = True
        a['isTrending'] = True
        a['trendingRank'] = 4
    elif a['slug'] == 'doug-robbie':
        a['isHeroMain'] = False
        a['isHeroSub'] = False
        a['isTrending'] = True
        a['trendingRank'] = 5
    elif a['slug'] == 'logan-romero-plant':
        a['isHeroMain'] = False
        a['isHeroSub'] = False
        a['isTrending'] = True
        a['trendingRank'] = 6
    else:
        a['isHeroMain'] = False
        a['isHeroSub'] = False
        a['isTrending'] = False

with open(DB_FILE, "w", encoding="utf-8") as f:
    f.write("# -*- coding: utf-8 -*-\n")
    f.write('"""\nIndependence Magazine - Article Database\nContains all verified, fact-checked editorial profiles.\n"""\n\n')
    f.write("ALL_ARTICLES = [\n")
    for a in db.ALL_ARTICLES:
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

print("Flags successfully updated in articles_database.py!")
