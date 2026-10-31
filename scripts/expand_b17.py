# -*- coding: utf-8 -*-
import os
import re

SCRIPT_PATH = r"C:\Users\Lapzone.pk\.gemini\antigravity\scratch\independence-magazine\scripts\add_batch17_articles.py"

with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
    code = f.read()

# 1. Expand Yasmin Abdallah
yasmin_addition = """
            <h2>Pioneering the Cool Britannia Era and Sustainable Aesthetics</h2>

            <p>During the height of London's 'Cool Britannia' cultural renaissance in the late 1990s and early 2000s, Yasmin Abdallah was at the epicenter of British music and high fashion convergence. She collaborated regularly with iconic photographers, styling leading indie musicians, actresses, and models for influential publications like <em>Dazed & Confused</em>, British <em>Vogue</em>, and <em>The Face</em>.</p>

            <p>Unlike stylists who relied on standard brand sponsorship packages, Abdallah pioneered an eclectic, deconstructed aesthetic that paired antique lace slips with rugged motorcycle boots and bespoke men's tailoring. Her fearless eye helped define the effortless, undone London look that dominated international catwalks for over a decade.</p>

            <p>In her later consulting work, Yasmin became an outspoken champion of sustainable apparel and ethical textile manufacturing. She guided several European fashion houses through the transition toward organic natural fibers—such as certified merino wool and recycled cashmere—proving that luxury fashion can maintain commercial appeal while respecting environmental boundaries.</p>
"""

# Insert before "<h2>Family Life, Marriage to Kyle Falconer, and Motherhood</h2>"
code = code.replace(
    '<h2>Family Life, Marriage to Kyle Falconer, and Motherhood</h2>',
    yasmin_addition + '\n            <h2>Family Life, Marriage to Kyle Falconer, and Motherhood</h2>'
)

# Also add 2 FAQs for Yasmin
yasmin_faqs = """
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Yasmin Abdallah's cultural background?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Yasmin Abdallah was born and raised in Sydney, Australia, and is of Lebanese heritage, bringing a rich multicultural aesthetic to her international styling and design career.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How did Yasmin Abdallah contribute to London fashion?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Through her iconic boutique <em>Yasmin Cho</em> and her editorial styling, she introduced European audiences to groundbreaking international designers including Rick Owens and Miguel Adrover, shaping London's late-1990s retail landscape.</p>
"""

code = code.replace(
    '</div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 3. Jillian Beth Gumbel',
    yasmin_faqs + '            </div>\n        """\n    },\n\n    # -------------------------------------------------------------------------\n    # 3. Jillian Beth Gumbel'
)

# 2. Expand Jillian Beth Gumbel
jillian_addition = """
            <h2>Classical Pilates Methodology and Functional Movement Philosophy</h2>

            <p>Jillian's approach to physical conditioning is rooted firmly in classical Pilates principles established by Joseph Pilates. Rather than adopting fast-moving fitness fads that prioritize exhaustion over biomechanics, her studio sessions emphasize core stability, spinal articulation, and precise breath synchronization.</p>

            <p>Working primarily with classical apparatus—including the universal reformer, Cadillac trapeze table, and wunda chair—Jillian tailors movement sequences to correct postural misalignments caused by prolonged desk work and modern urban lifestyles. Her restorative techniques have made her a trusted specialist for prenatal and postnatal women seeking to rebuild functional abdominal strength safely.</p>

            <p>She has also authored accessible home-conditioning routines for busy professionals, advocating for twenty minutes of deliberate, mindful movement each morning as an antidote to urban stress and postural fatigue.</p>
"""

code = code.replace(
    '<h2>Marriage to Bernard ‘Bernie’ Robins in Palm Beach</h2>',
    jillian_addition + '\n            <h2>Marriage to Bernard ‘Bernie’ Robins in Palm Beach</h2>'
)

# Also add 2 FAQs for Jillian
jillian_faqs = """
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Jillian Beth Gumbel's fitness philosophy?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She advocates for classical Pilates, prioritizing anatomical alignment, breath control, and core stabilization over exhausting workout trends to build sustainable lifelong mobility.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Does Jillian Gumbel offer prenatal and postnatal fitness coaching?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Yes, she is widely recognized in New York wellness circles for specializing in gentle, restorative Pilates sequences that help mothers rebuild core strength safely before and after childbirth.</p>
"""

code = code.replace(
    '</div>\n        """\n    }\n]',
    jillian_faqs + '            </div>\n        """\n    }\n]'
)

with open(SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(code)

print("Expanded add_batch17_articles.py successfully!")
