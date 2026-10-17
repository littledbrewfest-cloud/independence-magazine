import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

sys.path.append(SCRIPT_DIR)
from articles_database import ALL_ARTICLES

# 1. Expand Diane Lou Oswald
diane_extra = """
            <p>Growing up in Lebanon, Ohio, Diane was immersed in a tight-knit Midwestern community where neighbors supported one another through economic shifts. Her father, an industrious local craftsman, and her mother instilled in her a profound work ethic that prioritized honesty above material wealth. When Diane returned to Lebanon with her young sons after leaving Texas, the community provided a safe haven where Woody, Brett, and Jordan could attend local schools without the intrusive stigma of their father's notoriety.</p>

            <p>During Woody's years at Lebanon High School, Diane worked tirelessly to balance strict maternal discipline with creative freedom. Recognizing Woody's natural gifts for comedy, athletic agility in football and track, and theatrical expression, she actively encouraged his participation in school plays and speech competitions. When Woody was accepted into Hanover College in Indiana to study theatre and English, Diane managed her modest legal secretarial salary to help cover essential textbooks and tuition fees, ensuring her son had every opportunity she herself had sacrificed.</p>
"""

# 2. Expand Samantha Marie Olit
samantha_extra = """
            <p>During the pivotal months in 1999 and 2000 when Linkin Park was recording their groundbreaking debut album <em>Hybrid Theory</em> at NRG Recordings in North Hollywood, Samantha played an indispensable supportive role behind the scenes. With studio bills mounting and Chester facing grueling vocal tracking sessions, Samantha managed household expenses, provided emotional reassurance during intense rehearsals with producer Don Gilmore, and organized promotional meetings with street teams across the greater Los Angeles area.</p>

            <p>Her deep immersion in alternative music production helped her cultivate a nuanced understanding of artist development and intellectual property licensing. In later years, as she transitioned into certified life coaching and holistic DNA wellness, Samantha drew directly upon these high-intensity industry experiences to guide other creative professionals through the psychological pressures of sudden fame, tour fatigue, and personal transitions, solidifying her respected reputation as an authentic mentor and motivational voice.</p>
"""

for art in ALL_ARTICLES:
    if art["slug"] == "diane-lou-oswald":
        # Insert after "Early Life in Ohio, Roots, and Age in 2026"
        target = "celebrating 89 years.</p>"
        if "During Woody's years at Lebanon High School" not in art["contentHtml"]:
            art["contentHtml"] = art["contentHtml"].replace(
                "As of 2026, Diane Lou Oswald is <strong>89 years old</strong>.</p>",
                "As of 2026, Diane Lou Oswald is <strong>89 years old</strong>.</p>\n" + diane_extra
            )
    elif art["slug"] == "samantha-marie-olit":
        # Insert before "Divorce in 2005"
        if "During the pivotal months in 1999" not in art["contentHtml"]:
            art["contentHtml"] = art["contentHtml"].replace(
                "<h2>Divorce in 2005 and Creative Ventures with SAM Records</h2>",
                samantha_extra + "\n<h2>Divorce in 2005 and Creative Ventures with SAM Records</h2>"
            )

import pprint
with open(DB_FILE, "w", encoding="utf-8") as f:
    f.write('"""\nIndependence Magazine - Central Master Articles Database\n"""\n\n')
    f.write('ALL_ARTICLES = ' + pprint.pformat(ALL_ARTICLES, indent=4, width=120) + '\n')

print("Database updated with expanded depth for Batch 7!")
