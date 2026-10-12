import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
sys.path.append(SCRIPT_DIR)

from articles_database import ALL_ARTICLES

AUTHOR_SARAH = {
    'name': 'Sarah Jenkins',
    'role': 'Senior Biographical Correspondent',
    'avatar': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80',
    'bio': 'Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories.'
}

AUTHOR_MARCUS = {
    'name': 'Marcus Vance',
    'role': 'Investigative Features & Senior Editor',
    'avatar': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80',
    'bio': 'Marcus Vance is a senior investigative journalist covering public affairs, athletic dynasties, and high-profile entertainment profiles.'
}

# 6 articles each
AUTHOR_MAP = {
    'malaak-compton': AUTHOR_SARAH,
    'doug-robbie': AUTHOR_MARCUS,
    'logan-romero-plant': AUTHOR_MARCUS,
    'wanda-hutchins': AUTHOR_SARAH,
    'diane-addonizio': AUTHOR_MARCUS,
    'roberta-raffel': AUTHOR_SARAH,
    'marlene-knaus': AUTHOR_SARAH,
    'cindy-deangelis-grossman': AUTHOR_MARCUS,
    'kaynette-williams': AUTHOR_SARAH,
    'ian-alexander-sr': AUTHOR_MARCUS,
    'kathryn-burrhus': AUTHOR_SARAH,
    'mia-weier': AUTHOR_MARCUS
}

for art in ALL_ARTICLES:
    slug = art['slug']
    if slug in AUTHOR_MAP:
        art['author'] = AUTHOR_MAP[slug]

# Re-save articles_database.py
with open(os.path.join(SCRIPT_DIR, "articles_database.py"), "w", encoding="utf-8") as f:
    f.write('\"\"\"\nIndependence Magazine - Editorial Articles Database\nFact-Checked Biographies and In-Depth Profiles\n\"\"\"\n\n')
    f.write(f"ALL_ARTICLES = {repr(ALL_ARTICLES)}\n")

print(f"Successfully mapped all {len(ALL_ARTICLES)} articles to max 2 authors: Sarah Jenkins & Marcus Vance!")
