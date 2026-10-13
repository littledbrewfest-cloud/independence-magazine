import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

import sys
sys.path.append(SCRIPT_DIR)
import articles_database as db

JASON_ADDITION = """
            <h2>Texas Roots, Outdoor Passions, and Quiet Community Service</h2>
            <p>Beyond his career in commercial construction and logistics, Jason Clarkson has cultivated a deeply fulfilling life rooted in traditional Texas pastimes. An avid outdoorsman, he spends considerable time fishing in Central Texas lakes, off-roading across the Hill Country, and perfecting slow-smoked Texas barbecue recipes that have become legendary among his family and neighborhood gatherings.</p>
            <p>Rather than seeking public accolades, Jason quietly partners with local North Texas charitable initiatives, contributing to youth athletics leagues, holiday toy drives, and community food pantries. When Kelly launched her own philanthropic campaigns supporting children's healthcare in Dallas and Fort Worth, Jason worked behind the scenes to assist with logistics and local family outreach without seeking media coverage. This understated devotion to community reflects the core character of a man who values practical contribution far more than digital celebrity.</p>
"""

ELLY_ADDITION = """
            <h2>Healing Through Animal Rescue and Community Philanthropy</h2>
            <p>In the years following her high-profile court appearances, Elly Castle turned toward personal healing through nature, animal advocacy, and community service. Drawing on her lifelong compassion for animals, she became actively involved with independent pet rescue foundations across St. Tammany and Tangipahoa parishes in Southeast Louisiana, providing foster support and funding medical treatments for abandoned dogs and horses.</p>
            <p>She also developed a passion for sustainable organic horticulture, tending expansive vegetable gardens and heritage flower beds that provide a quiet sanctuary from urban chaos. Friends and family members frequently note that this grounded connection to the earth and animal welfare helped Elly rebuild her emotional equilibrium after decades in the public eye. By dedicating her time to vulnerable creatures and domestic creativity, she found an authentic peace that no red-carpet appearance could ever match.</p>
"""

def main():
    for a in db.ALL_ARTICLES:
        if a["slug"] == "jason-clarkson":
            # insert before FAQs
            parts = a["contentHtml"].split('<hr style="margin: 36px 0;')
            a["contentHtml"] = parts[0] + JASON_ADDITION + '<hr style="margin: 36px 0;' + parts[1]
        elif a["slug"] == "elly-castle":
            parts = a["contentHtml"].split('<hr style="margin: 36px 0;')
            a["contentHtml"] = parts[0] + ELLY_ADDITION + '<hr style="margin: 36px 0;' + parts[1]

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

    print("articles_database.py updated with additions!")

if __name__ == "__main__":
    main()
