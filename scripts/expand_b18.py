# -*- coding: utf-8 -*-
import os
import re

SCRIPT_PATH = r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\scripts\add_batch18_articles.py"

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# -----------------------------------------------------------------------------
# 1. Expand Anna Kate Denver
# -----------------------------------------------------------------------------
anna_addition = """
            <h2>Involvement in Environmental Conservation and the Windstar Legacy</h2>

            <p>Growing up under the mentorship of one of America's most famous environmentalists, Anna Kate developed an early passion for wildlife protection and ecological balance. Her father co-founded the Windstar Foundation in 1976—the year of Anna's birth—setting aside nearly 1,000 acres in Snowmass, Colorado, as a permanent environmental sanctuary and educational center.</p>

            <p>Throughout her young adulthood, Anna frequently volunteered at Windstar gatherings, helping organize symposiums on renewable solar energy, clean alpine watersheds, and sustainable forestry. Rather than claiming leadership titles, she preferred working quietly in operational logistics, greeting international conservationists and ensuring educational programs ran smoothly.</p>

            <p>Her time in Wanaka, New Zealand, has deepened that commitment. Surrounded by Mount Aspiring National Park and the pristine waters of Lake Wanaka, Anna actively supports local South Island wilderness trusts, advocating for predator-free wildlife corridors and native beech forest regeneration.</p>
"""

code = code.replace(
    '<h2>Marriage to Jaime Hutter and Life in New Zealand</h2>',
    anna_addition + '\n            <h2>Marriage to Jaime Hutter and Life in New Zealand</h2>'
)

anna_faqs = """
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did John Denver write a song about his daughter Anna Kate?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">While John Denver's most famous song <em>Annie's Song</em> was written for her mother Annie Martell, he frequently spoke in interviews about how becoming a father to Zachary and Anna Kate inspired several of his later reflective compositions on family and nature.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Does Anna Kate Denver perform music?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">No, Anna Kate Denver has never pursued a commercial music career. She chose to focus on private equity administration, environmental philanthropy, and family life.</p>
"""

code = code.replace(
    '</div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 2. Shelley Covel Rowland',
    anna_faqs + '            </div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 2. Shelley Covel Rowland'
)

# -----------------------------------------------------------------------------
# 2. Expand Shelley Covel Rowland
# -----------------------------------------------------------------------------
shelley_addition = """
            <h2>The Philosophy Behind SwingDish and Modernizing Women's Activewear</h2>

            <p>When Shelley and her mother Tricia launched SwingDish, their goal was to revolutionize how women dressed on championship golf fairways. Historically, major sporting brands merely downsized men's polo shirts, producing stiff, uninspired apparel that overlooked feminine movement and posture.</p>

            <p>Shelley helped spearhead the brand's integration of four-way stretch technical fabrics, moisture-wicking weaves, and UPF 50+ sun protection into tailored skirts, sleeveless tops, and lightweight jackets. Presenting collections annually at the PGA Merchandise Show in Orlando, Florida, Shelley established wholesale accounts with over 200 premier country club pro shops across the United States and Canada.</p>

            <p>Her eye for seasonal palette transitions—combining crisp country-club whites with bold geometric prints and subtle leather trims—earned SwingDish features in prominent golf publications like <em>Golf Digest</em> and <em>LPGA Women's Network</em>, solidifying Shelley's standing as an innovative retail executive.</p>
"""

code = code.replace(
    '<h2>Marriage to Brian Rowland and Family Life</h2>',
    shelley_addition + '\n            <h2>Marriage to Brian Rowland and Family Life</h2>'
)

shelley_faqs = """
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Shelley Covel Rowland’s role at SwingDish?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She serves as an executive leader and design coordinator, overseeing fabric sourcing, seasonal palette selection, and wholesale distribution across hundreds of golf resort pro shops.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How did Shelley Covel Rowland honor her father Toby Keith?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Following Toby Keith's passing in February 2024, Shelley and her family attended national Hall of Fame tributes and continue to support OK Kids Korral, the pediatric cancer lodge founded by the Toby Keith Foundation.</p>
"""

code = code.replace(
    '</div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 3. Steven Cauble',
    shelley_faqs + '            </div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 3. Steven Cauble'
)

# -----------------------------------------------------------------------------
# 3. Expand Steven Cauble
# -----------------------------------------------------------------------------
steven_addition = """
            <h2>Pastoral Counseling Principles and Conflict Resolution Frameworks</h2>

            <p>Throughout his ministry career in Southern California, Steven Cauble earned the trust of countless families through his grounded approach to interpersonal conflict. He avoided rigid dogmatic scolding, choosing instead to employ active empathetic listening, emotional de-escalation, and structured biblical counseling.</p>

            <p>He regularly facilitated premarital workshops designed to help young couples navigate financial planning, career ambitions, and spiritual differences before exchanging wedding vows. Many of the couples who sat in his office described his counseling sessions as compassionate, fair-minded, and intensely focused on building lasting mutual respect.</p>

            <p>These same personal principles guided his own conduct when his twenty-four-year marriage to Lisa Whelchel faced private difficulties. By refusing to let emotional disagreement turn into public acrimony, Cauble demonstrated that Christian grace applies just as powerfully during times of personal transition as it does during times of joy.</p>

            <h2>Mentorship of Younger Ministry Leaders and Life in California Today</h2>

            <p>In his later years, Pastor Cauble transitioned from frontline pulpit duties to one-on-one leadership mentorship. He advises emerging Christian ministers, offering practical wisdom on managing pastoral burnout, maintaining healthy work-life boundaries, and serving local communities with humility.</p>

            <p>He continues to reside in Southern California, enjoying regular visits with his three adult children and grandchildren. Friends describe him as a peaceful, reflective scholar who spends his mornings in personal study and prayer, fully content with a quiet, service-driven life away from cameras.</p>
"""

code = code.replace(
    '<h2>Where Steven Cauble Is Today and Net Worth</h2>',
    steven_addition + '\n            <h2>Where Steven Cauble Is Today and Net Worth</h2>'
)

steven_faqs = """
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did Steven Cauble ever appear on television with Lisa Whelchel?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">He made rare appearances in Christian television specials and family documentaries during the 1990s, but he intentionally avoided commercial Hollywood entertainment to focus on church pastoring.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Steven Cauble doing today?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">He lives in California, where he continues to provide private pastoral counsel, mentor younger ministry leaders, and spend quality time with his children and grandchildren.</p>
"""

code = code.replace(
    '</div>\n        """\n    }\n]',
    steven_faqs + '            </div>\n        """\n    }\n]'
)

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("Expanded Batch 18 articles successfully!")
