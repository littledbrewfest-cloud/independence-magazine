import os
import sys
import pprint

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")
sys.path.append(SCRIPT_DIR)
from articles_database import ALL_ARTICLES

# 1. Expand Ria Sommerfeld
extra_ria = """
            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Navigating the Pressures of Touring and Global Fandom</h2>
            <p>During the peak years of Tokio Hotel's international success, dating one of Europe's most pursued rock musicians required exceptional emotional equilibrium. At live concerts and award shows across Europe, band members were frequently flanked by private security details to manage ecstatic crowds. Sommerfeld handled this demanding environment with notable discretion, rarely giving unauthorized media commentary and consistently prioritizing genuine personal connections over tabloid exposure.</p>

            <p>Rather than adopting the lifestyle of an entourage dependent, Sommerfeld maintained her own independent professional circle. She frequently returned to Germany to visit her parents and childhood friends, ensuring that her identity remained anchored in her own vocational achievements and cultural heritage rather than solely within the orbit of international entertainment touring.</p>

            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Holistic Cosmetology and Aesthetic Philosophy</h2>
            <p>In her professional work today, Sommerfeld champions a philosophy that bridges clinical precision with holistic wellness. Unlike standard commercial salon operations focused solely on rapid turnaround, her aesthetic consultations incorporate scalp health analysis, environmentally responsible product formulations, and customized haircare regimens tailored to individual lifestyle demands. Industry peers often credit her European training for this thorough, client-first approach to sustainable beauty.</p>
"""

# 2. Expand Ashton Meem
extra_ashton = """
            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Corporate Leadership and Campaign Strategy at American Family Insurance</h2>
            <p>During her tenure as an Advertising Operations Manager, Meem was instrumental in overseeing complex digital and broadcast brand campaigns for American Family Insurance across several Midwestern and national markets. Her responsibilities went far beyond administrative logistics; she coordinated directly with external media buying agencies, analyzed impression metrics, and verified brand safety compliance across multi-million-dollar marketing initiatives.</p>

            <p>Those who worked alongside Meem described her as an astute analytical thinker who remained completely unfazed by external distractions. Even as her then-husband's face appeared on national billboards and weekly primetime telecasts, Meem kept her focus centered on deliverables, analytics spreadsheets, and cross-functional team collaboration, earning deep professional respect from agency partners and corporate executives alike.</p>

            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Community Outreach and Seattle Philanthropic Initiatives</h2>
            <p>While living in the Pacific Northwest, Meem dedicated considerable time to charitable endeavors in the greater Seattle community. She was an active participant in hospital visitations at Seattle Children's Hospital, spending quiet hours with pediatric patients away from promotional camera crews. Additionally, she supported regional initiatives focused on early childhood literacy and animal welfare, continuing a lifelong commitment to service instilled during her school days at St. Catherine's in Richmond.</p>
"""

# 3. Expand Laura Quinn Hawk
extra_laura = """
            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Community Philanthropy and Hawk's Locks for Kids</h2>
            <p>Throughout their time in Green Bay and Ohio, Laura and A.J. Hawk placed significant emphasis on civic contribution. Among their most visible charitable endeavors was Hawk's Locks for Kids, a philanthropic foundation established to support children experiencing hair loss due to chemotherapy and other medical conditions. Laura helped coordinate fundraising galas, donor logistics, and community hair donation events, rallying support from both Packers fans and Ohio State alumni.</p>

            <p>The Hawk family has also been long-time supporters of the Columbus-based Buckeye Cruise for Cancer, helping generate millions of dollars for the Urban and Shelley Meyer Fund for Cancer Research. Friends and neighbors in Dublin frequently note that despite their public visibility and athletic acclaim, Laura and A.J. maintain an exceptionally approachable, humble posture within the local school district and civic organizations.</p>

            <h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Architectural Style and the Design Vision of LCH Interiors</h2>
            <p>At LCH Interiors, Laura Quinn Hawk's design methodology focuses on timeless durability rather than fleeting digital trends. Recognizing the functional demands of active families with young children and pets, her residential projects emphasize stain-resistant natural textiles, engineered European oak flooring, custom storage millwork, and balanced architectural lighting. Her work proves that a luxury home can simultaneously look magazine-worthy and comfortably withstand the energetic daily realities of family life.</p>
"""

for art in ALL_ARTICLES:
    if art["slug"] == "ria-sommerfeld":
        idx = art["contentHtml"].find('<h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Ria Sommerfeld Age')
        if idx != -1:
            art["contentHtml"] = art["contentHtml"][:idx] + extra_ria + art["contentHtml"][idx:]
            print("Expanded Ria Sommerfeld content!")
    elif art["slug"] == "ashton-meem":
        idx = art["contentHtml"].find('<h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Ashton Meem Age')
        if idx != -1:
            art["contentHtml"] = art["contentHtml"][:idx] + extra_ashton + art["contentHtml"][idx:]
            print("Expanded Ashton Meem content!")
    elif art["slug"] == "laura-quinn-hawk":
        idx = art["contentHtml"].find('<h2 style="font-family: var(--font-serif); font-size: 1.55rem; color: var(--text-primary); margin: 34px 0 16px;">Laura Quinn Hawk Age')
        if idx != -1:
            art["contentHtml"] = art["contentHtml"][:idx] + extra_laura + art["contentHtml"][idx:]
            print("Expanded Laura Quinn Hawk content!")

with open(DB_FILE, "w", encoding="utf-8") as f:
    f.write('"""\nIndependence Magazine - Central Master Articles Database\n"""\n\n')
    f.write('ALL_ARTICLES = ' + pprint.pformat(ALL_ARTICLES, indent=4, width=120) + '\n')

print("Database rewritten with expanded depth!")
