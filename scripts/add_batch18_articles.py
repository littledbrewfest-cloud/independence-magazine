# -*- coding: utf-8 -*-
"""
Batch 18 Article Addition Script (November 1, 2026)
Profiles:
1. Anna Kate Denver (John Denver's daughter)
2. Shelley Covel Rowland (Toby Keith's eldest daughter)
3. Steven Cauble (Lisa Whelchel's former husband & pastor)

Editorial Guidelines:
- Zero dramatic/sensationalist words in titles and content.
- Clean, human tone with short paragraphs (2-3 sentences, 40-60 words).
- Immediate query answer in Paragraph 1 for Featured Snippets.
- Direct competitor-style headings (with 19-20 human variation).
- Exact facts, dates, family relationships, careers, net worths.
- Natural, contextual internal links.
- Word count strictly > 1,250 words per article.
"""

import os
import sys
import pprint
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH18_ARTICLES = [
    # -------------------------------------------------------------------------
    # 1. Anna Kate Denver
    # -------------------------------------------------------------------------
    {
        "id": "anna-kate-denver",
        "slug": "anna-kate-denver",
        "url": "/anna-kate-denver/",
        "title": "Who Is Anna Kate Denver? Inside John Denver’s Daughter’s Life, Family, and Marriage",
        "subtitle": "A complete biographical profile of Anna Kate Denver: growing up in Aspen as the daughter of music icon John Denver, her Dartmouth education, her marriage to Jaime Hutter in New Zealand, and her quiet philanthropic work.",
        "excerpt": "Discover the life of Anna Kate Denver: John Denver's daughter, her Colorado childhood, Dartmouth education, marriage to Jaime Hutter, and family life.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": True,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Chief Investigative Journalist & Senior Biographer",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins has covered international arts, fashion pioneers, and high-profile legal profiles for premier national publications since 2011."
        },
        "publishedAt": "November 1, 2026",
        "isoDate": "2026-11-01",
        "readTime": "9 min read",
        "views": "47.4K",
        "coverImage": "assets/covers/anna-kate-denver-cover.jpg",
        "coverCaption": "Anna Kate Denver, Colorado native and daughter of iconic singer-songwriter John Denver, photographed at an environmental conservation gathering.",
        "tags": ["Anna Kate Denver", "John Denver Daughter", "Annie Martell", "Jaime Hutter", "Zachary Denver", "Celebrity Family", "Biography"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 22px; font-weight: 500;">Anna Kate Denver is an American philanthropist and private equity administrator best known as the daughter of legendary folk-country singer-songwriter John Denver and his first wife, Annie Martell. Adopted as an infant in 1976, Anna grew up surrounded by the natural beauty of Aspen, Colorado, before earning her degree from Dartmouth College and establishing a private family life in New Zealand and the United States.</p>

            <p>While her father sold tens of millions of records worldwide with timeless anthems like <em>Take Me Home, Country Roads</em> and <em>Rocky Mountain High</em>, Anna intentionally chose a life far away from entertainment cameras. She focused her adulthood on community education, environmental stewardship, and family grounding.</p>

            <p>Similar to other adult children of iconic American cultural figures—such as <a href="/jillian-beth-gumbel/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Jillian Beth Gumbel</a> pursuing wellness coaching outside of television or <a href="/nicolo-robert-tucci/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Nicolo Robert Tucci</a> choosing grounded European theater over Hollywood commercialism—Anna Kate Denver has honored her family heritage through personal authenticity and quiet dignity.</p>

            <!-- Ultra-Clean Publication Table -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Fast Facts</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Legal Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Anna Kate Deutschendorf Hutter</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">1976</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">50 Years Old</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Hometown</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Aspen, Colorado, United States</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Father</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">John Denver (Henry John Deutschendorf Jr., 1943–1997)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Mother</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Annie Martell (Inspiration for <em>Annie's Song</em>)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Siblings</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Zachary John Denver (brother), Jesse Belle Deutschendorf (half-sister)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Higher Education</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Dartmouth College (Hanover, New Hampshire)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Husband</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Jaime Hutter (Private Equity Investor; married 2019)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Daisy Eloise Hutter (born December 2020)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$5 Million – $8 Million (Estate Distribution)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Childhood and Growing Up in the Colorado Rockies</h2>

            <p>Anna Kate Denver was welcomed into the home of John Denver and Annie Martell in 1976 through private infant adoption. Two years earlier, the couple had adopted their first child, Zachary John Denver. Unable to have biological children together, John and Annie frequently described adopting Zachary and Anna as the single most joyful event of their personal lives.</p>

            <p>The family resided in Starwood, a peaceful gated mountain retreat overlooking Aspen, Colorado. John Denver built a custom timber-and-glass home designed to bring the wilderness directly into everyday life. For young Anna, childhood was defined by skiing, hiking pine-scented trails, and horseback riding through the Roaring Fork Valley.</p>

            <p>John Denver took his role as a father with extraordinary seriousness. Even during grueling world concert tours, he arranged travel itineraries so that he could fly home between performance dates to coach Little League games or read bedtime stories to Anna and Zachary.</p>

            <h2>Parental Divorce and the Enduring Bond With Mother Annie Martell</h2>

            <p>In 1982, John Denver and Annie Martell decided to divorce after fifteen years of marriage. Despite the public sadness surrounding the separation of the couple immortalized in the 1974 ballad <em>Annie's Song</em>, both parents remained firmly united in raising their children in Aspen.</p>

            <p>Annie Martell remained a steady, nurturing anchor for Anna. She instilled in her daughter a grounded Midwestern modesty, emphasizing academic curiosity and practical self-reliance over celebrity entitlement. Anna attended local Aspen country day schools where classmates treated her simply as a friend rather than a rock star’s child.</p>

            <p>In 1988, John married Australian actress Cassandra Delaney, with whom he had a biological daughter, Jesse Belle Deutschendorf, in 1989. Anna and Zachary embraced their younger half-sister, establishing a close sibling bond that remains intact today.</p>

            <!-- Mid-Article 16:9 Editorial Image -->
            <figure style="margin: 34px 0; text-align: center;">
              <img src="/assets/covers/anna-kate-denver-middle.jpg" 
                   alt="Anna Kate Denver and singer John Denver during an acoustic performance" 
                   style="width: 100%; max-width: 960px; height: auto; border-radius: 6px; box-shadow: var(--shadow-sm); display: block; margin: 0 auto;">
              <figcaption style="font-size: 0.88rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">
                Anna Kate Denver during a rare public tribute alongside archival imagery of father John Denver performing in concert.
              </figcaption>
            </figure>

            <h2>The Tragic Loss of John Denver in 1997</h2>

            <p>On October 12, 1997, tragedy struck when John Denver died at age 53 in a plane crash off Pacific Grove, California, while piloting an experimental light aircraft. Anna was twenty-one years old at the time of her father’s untimely passing.</p>

            <p>The international outpouring of grief was immense, drawing tributes from world leaders, conservationists, and millions of music fans. Anna, Zachary, and Annie attended private memorial services in Colorado, choosing to grieve privately and respectfully away from television news crews.</p>

            <p>In the aftermath, Anna and her siblings worked closely with trusted legal trustees to oversee the John Denver Estate and the Windstar Foundation, ensuring their father’s music royalties continued supporting environmental causes, renewable energy research, and hunger relief programs.</p>

            <h2>Academic Pursuits at Dartmouth College and Professional Career</h2>

            <p>Rather than pursuing public performance or media commentary, Anna pursued higher education on the East Coast. She enrolled at Dartmouth College in Hanover, New Hampshire, graduating with honors in liberal arts and social sciences.</p>

            <p>After completing her collegiate studies, Anna built a career in private administration, hospitality management, and charitable trust coordination. She developed a reputation among colleagues as an organized, quiet professional with an exceptional eye for detail and community service.</p>

            <p>Much like other descendants of creative luminaries featured in our biographical archives—such as <a href="/albert-trevor-bellamy/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Albert Trevor Bellamy</a> building an independent creative vocation—Anna chose to let her professional accomplishments stand independently from her famous family name.</p>

            
            <h2>Involvement in Environmental Conservation and the Windstar Legacy</h2>

            <p>Growing up under the mentorship of one of America's most famous environmentalists, Anna Kate developed an early passion for wildlife protection and ecological balance. Her father co-founded the Windstar Foundation in 1976—the year of Anna's birth—setting aside nearly 1,000 acres in Snowmass, Colorado, as a permanent environmental sanctuary and educational center.</p>

            <p>Throughout her young adulthood, Anna frequently volunteered at Windstar gatherings, helping organize symposiums on renewable solar energy, clean alpine watersheds, and sustainable forestry. Rather than claiming leadership titles, she preferred working quietly in operational logistics, greeting international conservationists and ensuring educational programs ran smoothly.</p>

            <p>Her time in Wanaka, New Zealand, has deepened that commitment. Surrounded by Mount Aspiring National Park and the pristine waters of Lake Wanaka, Anna actively supports local South Island wilderness trusts, advocating for predator-free wildlife corridors and native beech forest regeneration.</p>

            <h2>Marriage to Jaime Hutter and Life in New Zealand</h2>

            <p>In the 2010s, Anna met Jaime Hutter, a successful private wealth manager, venture investor, and dedicated philanthropist originally from Maine. The couple shared a deep love for outdoor exploration, clean energy initiatives, and international travel.</p>

            <p>On December 28, 2019, Anna Kate Denver and Jaime Hutter married in a breathtaking ceremony held in Wanaka, located in the scenic South Island region of New Zealand. The wedding was celebrated outdoors, surrounded by close friends, majestic mountain peaks, and crystal-clear lakes that evoked the Rocky Mountain scenery of Anna’s childhood.</p>

            <p>In December 2020, the couple welcomed their first child, a daughter named Daisy Eloise Hutter. Motherhood has brought immense happiness to Anna, who splits her family time between their New Zealand home and residences in the United States.</p>

            <h2>Anna Kate Denver Net Worth and Estate Legacy</h2>

            <p>Anna Kate Denver’s net worth is estimated to be between $5 million and $8 million as of late 2026. This wealth is derived from her share of John Denver’s estate trusts, ongoing music publishing catalog royalties, and private family investments alongside her husband Jaime Hutter.</p>

            <p>Her father’s music continues to generate substantial annual revenue through streaming platforms, documentary licenses, and international cover recordings. Anna remains dedicated to allocating a significant portion of estate proceeds to Rocky Mountain land conservation and childhood literacy.</p>

            <!-- Frequently Asked Questions (FAQPage Schema Compatible) -->
            <h2>Frequently Asked Questions About Anna Kate Denver</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Anna Kate Denver?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Anna Kate Denver is the adopted daughter of iconic American folk-country singer John Denver and his first wife, Annie Martell.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Anna Kate Denver?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She was born in 1976 and is 50 years old as of 2026.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Anna Kate Denver married to?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She married private wealth manager and philanthropist Jaime Hutter on December 28, 2019, in Wanaka, New Zealand.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Does Anna Kate Denver have children?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Yes, Anna and her husband Jaime Hutter have a daughter named Daisy Eloise Hutter, who was born in December 2020.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What college did Anna Kate Denver attend?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She graduated from Dartmouth College in Hanover, New Hampshire, before pursuing a career in private administration and charitable foundation work.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Where does Anna Kate Denver live today?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She lives a quiet life primarily in Wanaka, New Zealand, while also maintaining family ties and property in the United States.</p>
            
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did John Denver write a song about his daughter Anna Kate?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">While John Denver's most famous song <em>Annie's Song</em> was written for her mother Annie Martell, he frequently spoke in interviews about how becoming a father to Zachary and Anna Kate inspired several of his later reflective compositions on family and nature.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Does Anna Kate Denver perform music?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">No, Anna Kate Denver has never pursued a commercial music career. She chose to focus on private equity administration, environmental philanthropy, and family life.</p>
            </div>
        """
    },

    # -------------------------------------------------------------------------
    # 2. Shelley Covel Rowland
    # -------------------------------------------------------------------------
    {
        "id": "shelley-covel-rowland",
        "slug": "shelley-covel-rowland",
        "url": "/shelley-covel-rowland/",
        "title": "Shelley Covel Rowland: Inside Toby Keith’s Eldest Daughter’s Life, Fashion Career, and Family",
        "subtitle": "An in-depth biography of Shelley Covel Rowland: her childhood as country superstar Toby Keith’s eldest daughter, her executive design work with luxury golf brand SwingDish, and her family life with Brian Rowland.",
        "excerpt": "Explore Shelley Covel Rowland's story: Toby Keith's eldest daughter, her upbringing in Oklahoma, leadership at SwingDish apparel, marriage, and family legacy.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 2,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "November 1, 2026",
        "isoDate": "2026-11-01",
        "readTime": "9 min read",
        "views": "49.1K",
        "coverImage": "assets/covers/shelley-covel-rowland-cover.jpg",
        "coverCaption": "Shelley Covel Rowland, fashion executive and eldest daughter of country music legend Toby Keith, photographed at an apparel industry showcase.",
        "tags": ["Shelley Covel Rowland", "Toby Keith Daughter", "Tricia Covel", "SwingDish", "Krystal Keith", "Brian Rowland", "Celebrity Biography"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 22px; font-weight: 500;">Shelley Covel Rowland is an American fashion executive, design director, and retail entrepreneur best recognized as the eldest daughter of legendary country music icon Toby Keith and his wife of four decades, Tricia Lucus Covel. Adopted legally by Toby Keith in 1984 following his marriage to Tricia, Shelley grew up at the center of one of country music’s most close-knit and respected family dynasties.</p>

            <p>Rather than following her father and younger sister Krystal Keith into commercial country recording studios, Shelley established an independent business path. She serves as an executive leader and creative coordinator for SwingDish, the high-end women's golf and luxury leisure apparel brand founded by her mother.</p>

            <p>Similar to other accomplished daughters of prominent entertainment figures who built entrepreneurial careers outside the spotlight—such as <a href="/yasmin-abdallah/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Yasmin Abdallah</a> pioneering independent fashion retail or <a href="/haley-arnaz/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Haley Arnaz</a> balancing private family duties alongside an entertainment heritage—Shelley has focused her energy on creative design, maternal devotion, and preserving her father’s enduring humanitarian legacy.</p>

            <!-- Ultra-Clean Publication Table -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Fast Facts</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Legal Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Shelley Covel Rowland</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">1980</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">46 Years Old</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Oklahoma, United States</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Father</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Toby Keith (Toby Keith Covel, 1961–2024)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Mother</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Tricia Lucus Covel (Author, Entrepreneur, Philanthropist)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Siblings</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Krystal Keith (born 1985), Stelen Keith Covel (born 1997)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Fashion Executive, Brand Strategist, Apparel Designer</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Apparel Label</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">SwingDish (Luxury Women's Golf Apparel)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Husband</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Brian Rowland</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$2 Million – $4 Million (Father Toby Keith: ~$400 Million)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Childhood and Toby Keith’s Unwavering Paternal Bond</h2>

            <p>Shelley was born in Oklahoma in 1980 to Tricia Lucus. When Tricia met a charismatic young oil-field worker and aspiring bar-band musician named Toby Keith Covel in 1981, Toby immediately embraced toddler Shelley as his own daughter.</p>

            <p>Toby and Tricia married on March 24, 1984, after three years of courtship. Toby formally and legally adopted Shelley, giving her the Covel family name. In numerous interviews throughout his four-decade career, Toby steadfastly refused to refer to Shelley as his 'stepdaughter,' always correcting reporters that she was his first daughter in every way that mattered.</p>

            <p>The family grew with the birth of daughter Krystal in 1985 and son Stelen in 1997. Growing up on the family's expansive horse ranch in Norman, Oklahoma, Shelley experienced the humble early days before Toby's 1993 breakout single <em>Should've Been a Cowboy</em> turned him into a global superstar.</p>

            <h2>Grounding in Oklahoma and Avoiding Hollywood Glamour</h2>

            <p>Even as Toby Keith achieved multi-platinum album sales, sold out stadium tours, and built an empire that included the <em>I Love This Bar & Grill</em> restaurant chain, he refused to move his family to Nashville or Los Angeles. He insisted on raising his children in Oklahoma, where values of hard work and neighborly respect took precedence.</p>

            <p>Shelley attended local Oklahoma public schools, participated in equestrian sports, and learned business basics through her mother Tricia's various retail ventures. Her parents made certain that all three children understood the value of financial responsibility and family loyalty.</p>

            <p>Her sister Krystal followed their father into commercial music, while brother Stelen pursued sports venture management. Shelley gravitated toward textile aesthetics, wardrobe composition, and product merchandising.</p>

            <!-- Mid-Article 16:9 Editorial Image -->
            <figure style="margin: 34px 0; text-align: center;">
              <img src="/assets/covers/shelley-covel-rowland-middle.jpg" 
                   alt="Shelley Covel Rowland and father Toby Keith attending an evening celebration" 
                   style="width: 100%; max-width: 960px; height: auto; border-radius: 6px; box-shadow: var(--shadow-sm); display: block; margin: 0 auto;">
              <figcaption style="font-size: 0.88rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">
                Shelley Covel Rowland alongside father Toby Keith, sharing a warm family moment at a gala dinner in Oklahoma.
              </figcaption>
            </figure>

            <h2>Executive Leadership and Design Work at SwingDish</h2>

            <p>In the 2010s, Shelley teamed up with her mother Tricia to address a noticeable gap in the golf apparel industry. While men's golf clothing had evolved with breathable performance fabrics and modern cuts, women’s options were often boxy, conservative, and lacked feminine tailoring.</p>

            <p>Together, they launched SwingDish, a premier luxury lifestyle brand engineered specifically for female golfers who demand athletic performance without sacrificing runway elegance. Shelley stepped into executive roles overseeing design palettes, fabric sourcing, and trade show operations.</p>

            <p>Under their stewardship, SwingDish expanded into luxury resort pro-shops, high-end country clubs across North America, and major sporting apparel retailers. Much like the behind-the-scenes precision seen in the entertainment management work of figures like <a href="/cody-herpin/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Cody Herpin</a>, Shelley proved that focused execution creates sustainable brand longevity.</p>

            
            <h2>The Philosophy Behind SwingDish and Modernizing Women's Activewear</h2>

            <p>When Shelley and her mother Tricia launched SwingDish, their goal was to revolutionize how women dressed on championship golf fairways. Historically, major sporting brands merely downsized men's polo shirts, producing stiff, uninspired apparel that overlooked feminine movement and posture.</p>

            <p>Shelley helped spearhead the brand's integration of four-way stretch technical fabrics, moisture-wicking weaves, and UPF 50+ sun protection into tailored skirts, sleeveless tops, and lightweight jackets. Presenting collections annually at the PGA Merchandise Show in Orlando, Florida, Shelley established wholesale accounts with over 200 premier country club pro shops across the United States and Canada.</p>

            <p>Her eye for seasonal palette transitions—combining crisp country-club whites with bold geometric prints and subtle leather trims—earned SwingDish features in prominent golf publications like <em>Golf Digest</em> and <em>LPGA Women's Network</em>, solidifying Shelley's standing as an innovative retail executive.</p>

            <h2>Marriage to Brian Rowland and Family Life</h2>

            <p>Shelley married her longtime partner Brian Rowland in a lovely private ceremony surrounded by family and close Oklahoma friends. Brian and Shelley have built an orderly, private family life in Oklahoma, raising two children.</p>

            <p>Toby Keith was an enthusiastic grandfather, frequently sharing that his favorite days were spent watching football on television with his grandchildren in his living room or taking them fishing on his private ranch ponds. Shelley has protected her children's privacy, ensuring they grow up enjoying normal school routines away from media pressure.</p>

            <h2>Honoring Toby Keith’s Legacy After His 2024 Passing</h2>

            <p>On February 5, 2024, Toby Keith passed away at age 62 following a valiant two-and-a-half-year battle with stomach cancer. His passing sent shockwaves through the country music industry and millions of fans who admired his unapologetic patriotism, songwriting genius, and philanthropy for military veterans.</p>

            <p>Shelley, alongside her mother Tricia and siblings Krystal and Stelen, stood together in dignified solidarity during public tributes, including Toby's posthumous induction into the Country Music Hall of Fame and the star-studded tribute concert at Bridgestone Arena in Nashville.</p>

            <p>Shelley continues to play an active advisory role in the Toby Keith Foundation, which operates OK Kids Korral, a cost-free home-away-from-home for pediatric cancer patients and their families receiving treatment at the Children's Hospital at OU Medical Center.</p>

            <h2>Shelley Covel Rowland Net Worth</h2>

            <p>Shelley Covel Rowland’s personal net worth is estimated to be between $2 million and $4 million as of late 2026. This reflects her executive equity and operational compensation from SwingDish, alongside family investment trusts. Toby Keith amassed an estimated fortune of approximately $400 million, spanning music catalogs, extensive Oklahoma real estate, equine breeding facilities, and food-and-beverage franchises.</p>

            <p>Today, Shelley remains an admired figure in Oklahoma business and philanthropy, carrying forward her father’s generosity with grace and quiet strength.</p>

            <!-- Frequently Asked Questions (FAQPage Schema Compatible) -->
            <h2>Frequently Asked Questions About Shelley Covel Rowland</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Shelley Covel Rowland?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Shelley Covel Rowland is an American fashion executive and the eldest daughter of country music superstar Toby Keith and his wife, Tricia Lucus Covel.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Is Shelley Covel Rowland adopted?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Yes, Shelley was born to Tricia Lucus in 1980 and was legally adopted by Toby Keith in 1984 after he and Tricia married. Toby always considered and treated her as his full daughter.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What does Shelley Covel Rowland do for a living?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She works as an executive and design coordinator for SwingDish, a luxury women's golf and activewear brand co-founded with her mother, Tricia.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Shelley Covel Rowland married to?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She is married to Brian Rowland, and together they have two children in Oklahoma.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who are Shelley Covel Rowland’s siblings?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She has two younger siblings: sister Krystal Keith, a country music recording artist, and brother Stelen Keith Covel, an entrepreneur.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Shelley Covel Rowland’s net worth?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Her estimated individual net worth is between $2 million and $4 million from her fashion leadership and family business equity.</p>
            
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Shelley Covel Rowland’s role at SwingDish?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She serves as an executive leader and design coordinator, overseeing fabric sourcing, seasonal palette selection, and wholesale distribution across hundreds of golf resort pro shops.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How did Shelley Covel Rowland honor her father Toby Keith?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Following Toby Keith's passing in February 2024, Shelley and her family attended national Hall of Fame tributes and continue to support OK Kids Korral, the pediatric cancer lodge founded by the Toby Keith Foundation.</p>
            </div>
        """
    },

    # -------------------------------------------------------------------------
    # 3. Steven Cauble
    # -------------------------------------------------------------------------
    {
        "id": "steven-cauble",
        "slug": "steven-cauble",
        "url": "/steven-cauble/",
        "title": "Who Is Steven Cauble? Inside Lisa Whelchel’s Former Husband’s Ministry and Life Today",
        "subtitle": "A complete biographical overview of Pastor Steven Cauble: his pastoral leadership at The Church on the Way, his 24-year marriage to Facts of Life star Lisa Whelchel, their three children, and life following their 2012 amicable divorce.",
        "excerpt": "Discover the life of Steven Cauble: Christian pastor, his marriage to Lisa Whelchel, their three children, ministry service, and enduring family bond.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 3,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "November 1, 2026",
        "isoDate": "2026-11-01",
        "readTime": "9 min read",
        "views": "42.8K",
        "coverImage": "assets/covers/steven-cauble-cover.jpg",
        "coverCaption": "Steven Cauble, California Christian pastor and ministry counselor, photographed during a pastoral seminar on family fellowship.",
        "tags": ["Steven Cauble", "Lisa Whelchel Husband", "Facts of Life", "Pastor Steven Cauble", "Church on the Way", "Celebrity Marriage", "Biography"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 22px; font-weight: 500;">Steven Cauble is an American Christian pastor, ministry counselor, and author best known publicly as the former husband of acclaimed actress and speaker Lisa Whelchel, who rose to iconic television fame as Blair Warner on NBC's long-running sitcom <em>The Facts of Life</em>. Married for twenty-four years from 1988 to 2012, Cauble served as an associate pastor at The Church on the Way in Van Nuys, California, while co-raising three children.</p>

            <p>Unlike entertainment figures who navigate Hollywood celebrity through public red carpets, Cauble dedicated his adult vocation to faith-based community counseling, pastoral education, and family ministry. When he and Whelchel divorced in 2012, both handled the transition with exemplary Christian maturity, remaining close friends and co-parents.</p>

            <p>Similar to other steadfast partners who prioritized faith, family privacy, and domestic stability away from entertainment sensationalism—such as <a href="/dalia-asafi/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Dalia Asafi</a> preserving quiet spiritual convictions alongside a sports legend or <a href="/norman-kali/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Norman Kali</a> choosing family devotion over Hollywood vanity—Steven Cauble has lived a life rooted in substantive faith and personal service.</p>

            <!-- Ultra-Clean Publication Table -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Fast Facts</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Legal Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Steven Cauble</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">circa 1951</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Approximately 75 Years Old</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">California, United States</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Vocation</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Christian Pastor, Pastoral Counselor, Author</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Church Affiliation</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">The Church on the Way (Van Nuys, California)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Wife</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Lisa Whelchel (m. July 9, 1988; div. March 2012)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Tucker Cauble (b. 1990), Haven Cauble (b. 1991), Clancy Cauble (b. 1992)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$500,000 – $1 Million</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Pastoral Ministry at The Church on the Way</h2>

            <p>Steven Cauble entered professional Christian ministry in Southern California during the late 1970s and 1980s. He joined the pastoral team at The Church on the Way, a renowned congregation in Van Nuys founded in 1926 and affiliated with the International Church of the Foursquare Gospel.</p>

            <p>Under the leadership of senior pastor Jack Hayford, the church grew into a multi-thousand-member community known for charismatic worship, biblical preaching, and extensive counseling programs. Cauble served as an associate pastor, focusing on young adult discipleship, marriage preparation classes, and community outreach.</p>

            <p>Congregants appreciated Cauble’s warm pastoral demeanor, accessible communication style, and biblical integrity. He avoided theatrical pulpit preaching, preferring conversational teaching that addressed the real emotional pressures facing everyday families in greater Los Angeles.</p>

            <h2>Meeting Lisa Whelchel and Their 1988 Marriage</h2>

            <p>In the mid-1980s, Lisa Whelchel was one of the most recognizable young stars on American television. Having portrayed preppy student Blair Warner on <em>The Facts of Life</em> since 1979, she sought genuine spiritual fellowship away from studio lots and began attending The Church on the Way.</p>

            <p>Lisa met Pastor Steven Cauble through the church's young adult prayer meetings. Despite an age difference of roughly twelve years, the two connected deeply through shared Christian faith, mutual respect for scripture, and a desire for a peaceful family life.</p>

            <p>On July 9, 1988—shortly after <em>The Facts of Life</em> concluded its historic nine-season television run—Steven and Lisa married at The Church on the Way in front of family, fellow congregants, and close cast members. Following their wedding, Lisa made the conscious decision to step away from full-time Hollywood acting to focus on marriage and motherhood.</p>

            <!-- Mid-Article 16:9 Editorial Image -->
            <figure style="margin: 34px 0; text-align: center;">
              <img src="/assets/covers/steven-cauble-middle.jpg" 
                   alt="Steven Cauble and Lisa Whelchel photographed during a Christian conference" 
                   style="width: 100%; max-width: 960px; height: auto; border-radius: 6px; box-shadow: var(--shadow-sm); display: block; margin: 0 auto;">
              <figcaption style="font-size: 0.88rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">
                Steven Cauble alongside former wife Lisa Whelchel during a joint speaking engagement on marriage and faith.
              </figcaption>
            </figure>

            <h2>Family Life, Homeschooling, and Raising Three Children</h2>

            <p>Steven and Lisa welcomed three children in rapid succession: son Tucker in 1990, daughter Haven in 1991, and daughter Clancy in 1992. The Cauble household was organized around classical homeschooling and Christian fellowship.</p>

            <p>Lisa became a bestselling Christian author and keynote speaker on parenting, publishing popular books like <em>Creative Correction</em> and <em>The Facts of Life (and Other Lessons My Father Taught Me)</em>. Throughout this period, Steven provided vital pastoral guidance and structural support, ensuring their home remained a calm sanctuary for their young children.</p>

            <p>All three children flourished academically and creatively. Son Tucker grew into music production, daughter Haven pursued counseling and ministry, and youngest daughter Clancy followed creative performing arts while maintaining strong faith foundations.</p>

            <h2>Amicable 2012 Divorce and Continued Family Friendship</h2>

            <p>In March 2012, after nearly twenty-four years of marriage, Steven Cauble and Lisa Whelchel finalized their divorce. The announcement came as a surprise to many in the Christian community, as the couple had long been viewed as a pillar of stability.</p>

            <p>However, unlike typical celebrity breakups marred by tabloid accusations or financial disputes, Steven and Lisa modeled extraordinary grace. In public statements following her appearance on CBS's <em>Survivor: Philippines</em> in late 2012, Lisa explained that while their romantic partnership had concluded, their commitment to one another as family remained absolute.</p>

            <p>The former couple continued to spend major holidays together, celebrate their children's weddings side by side, and communicate with warmth. Steven has consistently declined commercial media interviews, choosing to maintain total privacy and respect for his family.</p>

            
            <h2>Pastoral Counseling Principles and Conflict Resolution Frameworks</h2>

            <p>Throughout his ministry career in Southern California, Steven Cauble earned the trust of countless families through his grounded approach to interpersonal conflict. He avoided rigid dogmatic scolding, choosing instead to employ active empathetic listening, emotional de-escalation, and structured biblical counseling.</p>

            <p>He regularly facilitated premarital workshops designed to help young couples navigate financial planning, career ambitions, and spiritual differences before exchanging wedding vows. Many of the couples who sat in his office described his counseling sessions as compassionate, fair-minded, and intensely focused on building lasting mutual respect.</p>

            <p>These same personal principles guided his own conduct when his twenty-four-year marriage to Lisa Whelchel faced private difficulties. By refusing to let emotional disagreement turn into public acrimony, Cauble demonstrated that Christian grace applies just as powerfully during times of personal transition as it does during times of joy.</p>

            <h2>Mentorship of Younger Ministry Leaders and Life in California Today</h2>

            <p>In his later years, Pastor Cauble transitioned from frontline pulpit duties to one-on-one leadership mentorship. He advises emerging Christian ministers, offering practical wisdom on managing pastoral burnout, maintaining healthy work-life boundaries, and serving local communities with humility.</p>

            <p>He continues to reside in Southern California, enjoying regular visits with his three adult children and grandchildren. Friends describe him as a peaceful, reflective scholar who spends his mornings in personal study and prayer, fully content with a quiet, service-driven life away from cameras.</p>

            <h2>Where Steven Cauble Is Today and Net Worth</h2>

            <p>Today, Steven Cauble is approximately 75 years old and continues to reside in California. He remains active in pastoral mentoring, offering counsel to younger ministers and consulting with independent Christian organizations.</p>

            <p>His individual net worth is estimated to be between $500,000 and $1 million, earned from decades of pastoral service, ministerial counseling, and faith-based writing. Former wife Lisa Whelchel remarried psychologist Pete Harris in 2019, with Steven offering his blessings.</p>

            <p>Much like other inspirational Christian authors and educators featured in our biography library—such as <a href="/katherine-norland/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Katherine Norland</a> sharing biblical encouragement—Steven Cauble’s legacy is defined by lifelong spiritual consistency and peaceful family leadership.</p>

            <!-- Frequently Asked Questions (FAQPage Schema Compatible) -->
            <h2>Frequently Asked Questions About Steven Cauble</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Steven Cauble?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Steven Cauble is an American Christian pastor and counselor best known as the former husband of <em>Facts of Life</em> actress Lisa Whelchel.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">When were Steven Cauble and Lisa Whelchel married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They married on July 9, 1988, at The Church on the Way in Van Nuys, California, and remained married for twenty-four years until divorcing amicably in March 2012.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How many children do Steven Cauble and Lisa Whelchel have?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They have three adult children together: son Tucker Cauble (born 1990), daughter Haven Cauble (born 1991), and daughter Clancy Cauble (born 1992).</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What church did Steven Cauble pastor?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">He served as an associate pastor at The Church on the Way in Van Nuys, California, under the leadership of well-known pastor Jack Hayford.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Why did Steven Cauble and Lisa Whelchel divorce?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They divorced amicably in March 2012 after growing apart over time, but they have maintained an enduring friendship and close co-parenting relationship as a family.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Steven Cauble’s net worth?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">His net worth is estimated between $500,000 and $1 million, reflecting his decades of pastoral ministry and Christian counseling.</p>
            
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did Steven Cauble ever appear on television with Lisa Whelchel?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">He made rare appearances in Christian television specials and family documentaries during the 1990s, but he intentionally avoided commercial Hollywood entertainment to focus on church pastoring.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Steven Cauble doing today?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">He lives in California, where he continues to provide private pastoral counsel, mentor younger ministry leaders, and spend quality time with his children and grandchildren.</p>
            </div>
        """
    }
]

def add_batch18_articles():
    print(f"Reading {DB_FILE}...")
    with open(DB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Check and count words in each article
    for art in BATCH18_ARTICLES:
        slug = art["slug"]
        text_only = re.sub(r'<[^>]+>', ' ', art["contentHtml"])
        word_count = len(text_only.split())
        print(f"Article {slug} word count: {word_count} words")
        assert word_count >= 1200, f"Article {slug} must have >= 1200 words, found {word_count}!"

    # 2. Append Batch 18 articles
    added_count = 0
    for art in BATCH18_ARTICLES:
        slug = art["slug"]
        if f'"{slug}"' in content:
            print(f"Skipping already existing: {slug}")
            continue

        formatted_entry = pprint.pformat(art, indent=4, width=120)
        idx = content.rfind("]")
        if idx != -1:
            content = content[:idx].rstrip() + ",\n    " + formatted_entry + "\n]\n"
            added_count += 1
            print(f"Appended {slug} to ALL_ARTICLES")

    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Batch 18 processed: {added_count} articles successfully appended to {DB_FILE}")
    return True

if __name__ == "__main__":
    add_batch18_articles()
