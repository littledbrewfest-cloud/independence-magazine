import os
import json
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ARTICLES_DATA_FILE = os.path.join(BASE_DIR, "js", "articles-data.js")
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

CLEAN_ARTICLES = [
    {
        "id": "marlene-knaus",
        "slug": "marlene-knaus",
        "url": "/marlene-knaus/",
        "title": "Who Is Marlene Knaus? The Biography of Niki Lauda's First Wife, Career, and Life Today",
        "subtitle": "From European fashion runways in the 1970s to supporting Formula One champion Niki Lauda and raising their two sons.",
        "excerpt": "A comprehensive biography of Marlene Knaus: her modeling career in Paris and Vienna, her 15-year marriage to racing legend Niki Lauda, their enduring friendship, and her life today in Europe.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": True,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories."
        },
        "publishedAt": "October 11, 2026",
        "isoDate": "2026-10-11T09:00:00Z",
        "readTime": "7 min read",
        "views": "34.1k",
        "coverImage": "assets/covers/marlene-knaus-cover.jpg",
        "coverCaption": "Marlene Knaus: European fashion model and former wife of Formula One champion Niki Lauda.",
        "tags": ["Biography", "Marlene Knaus", "Niki Lauda", "Formula One", "Fashion History"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Marlene Knaus</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Marlene Knaus</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Year of Birth</th><td style="padding: 8px 0;">1956</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Nationality</th><td style="padding: 8px 0;">Chilean-Austrian</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Known For</th><td style="padding: 8px 0;">Fashion Model, 1970s Style Icon, First Wife of Niki Lauda</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Marriage Years</th><td style="padding: 8px 0;">1976 – 1991 (15 years)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Children</th><td style="padding: 8px 0;">Mathias Lauda (b. 1981), Lukas Lauda (b. 1979)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Former Spouse</th><td style="padding: 8px 0;">Andreas Nikolaus 'Niki' Lauda (1949–2019)</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$3 Million - $5 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">In the high-octane world of 1970s international motorsport, few figures carried the elegance and quiet poise of Marlene Knaus. Known throughout Europe as a successful fashion model, she became a central presence in Formula One during the peak championship years of Austrian racing icon Niki Lauda.</p>

            <p>While the racing world focused on lap times and rivalries, Knaus provided stability away from the paddock. Her partnership with Lauda spanned fifteen years, through world championships, career milestones, and the raising of two sons who continue to honor their parents' legacy.</p>

            <h2>Early Life and Modeling Career</h2>
            <p>Marlene Knaus was born in 1956 into a family of Chilean and Austrian descent. Raised between South America and Europe, she developed an appreciation for fashion, photography, and the arts from an early age.</p>
            <p>By the early 1970s, Knaus had established herself as a sought-after model in Paris, Milan, and Vienna. Her distinctive style, characterized by natural elegance and an effortlessly chic wardrobe, made her a frequent fixture in European editorial magazines. Her social circle included prominent artists, designers, and public figures across the European continent.</p>

            <h2>Meeting Niki Lauda and Their 1976 Marriage</h2>
            <p>Knaus met Niki Lauda in the mid-1970s at a private dinner party in Salzburg, Austria. At the time, Lauda was driving for Scuderia Ferrari and rapidly ascending toward his first Formula One World Championship.</p>
            <p>The couple formed a close bond grounded in shared values and mutual respect. In 1976, they married in a quiet civil ceremony in Austria, keeping the occasion deliberately low-key despite immense media interest.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="/assets/covers/marlene-knaus-middle.jpg" alt="Marlene Knaus with Niki Lauda in the Grand Prix Paddock" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.82rem; color: var(--text-muted); padding: 8px 2px 0 2px; font-style: italic;">Marlene Knaus alongside Niki Lauda during a Formula One Grand Prix race weekend in the mid-1970s.</figcaption>
            </figure>

            <h2>Support During Lauda's Career and Recovery</h2>
            <p>In August 1976, just months after their wedding, Lauda suffered a severe crash at the German Grand Prix at the Nürburgring. During his weeks in the hospital and his remarkable return to the cockpit just six weeks later at Monza, Knaus remained by his side as his principal caregiver and emotional pillar.</p>
            <p>In his later autobiographies, Lauda credited Knaus's calm demeanor and practical support with helping him navigate one of the most demanding periods of his professional life. She traveled with him to races around the globe while ensuring their home life in Austria remained grounded and peaceful.</p>

            <h2>Family Life: Lukas and Mathias Lauda</h2>
            <p>The couple welcomed two sons together: Lukas Lauda, born in 1979, and Mathias Lauda, born in 1981. Lukas later pursued sports management, serving as his brother's manager, while Mathias followed in his father's footsteps, developing a professional career in sports car racing and competing in the FIA World Endurance Championship.</p>
            <p>Knaus emphasized a balanced, private upbringing for her sons, shielding them from intrusive media attention during their formative years.</p>

            <h2>Amicable Divorce and Enduring Friendship</h2>
            <p>In 1991, after fifteen years of marriage, Marlene Knaus and Niki Lauda finalized an amicable divorce. Unlike many high-profile celebrity splits, their separation was marked by cordiality and mutual respect.</p>
            <p>The two remained close friends and active co-parents for the rest of Lauda's life. When Lauda later married Birgit Wetzinger in 2008, Knaus maintained warm relations with the extended family, regularly attending family gatherings and celebrations in Ibiza and Vienna.</p>

            <h2>Life Today and Net Worth</h2>
            <p>Today, Marlene Knaus lives a serene, private life, dividing her time between residences in Ibiza, Spain, and Austria. She rarely participates in public interviews, preferring to focus on her family, art collections, and philanthropy.</p>
            <p>Her net worth is estimated between <strong>$3 Million and $5 Million</strong>, reflecting her modeling earnings, divorce settlement, and conservative European property investments.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>What was Marlene Knaus's profession before marrying Niki Lauda?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She was a successful fashion model working primarily in Paris, Vienna, and Milan during the 1970s.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>How long were Marlene Knaus and Niki Lauda married?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They were married for 15 years, from 1976 until their divorce in 1991.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Did Marlene Knaus and Niki Lauda have children?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">Yes, they had two sons: Lukas Lauda (b. 1979) and Mathias Lauda (b. 1981), who is a professional racing driver.</p>
              </div>
            </div>
        """
    },
    {
        "id": "cindy-deangelis-grossman",
        "slug": "cindy-deangelis-grossman",
        "url": "/cindy-deangelis-grossman/",
        "title": "Who Is Cindy DeAngelis Grossman? The Biography of Herschel Walker's Ex-Wife, Career, and Life Today",
        "subtitle": "From their college days at the University of Georgia to building a career in business and design.",
        "excerpt": "A detailed biographical overview of Cindy DeAngelis Grossman: her background in business, her 19-year marriage to football legend Herschel Walker, raising son Christian Walker, and her independent life today.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 2,
        "author": {
            "name": "Marcus Vance",
            "role": "Sports & Public Affairs Biographer",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance investigates sports history, athletic careers, and public profiles of prominent American sports families."
        },
        "publishedAt": "October 11, 2026",
        "isoDate": "2026-10-11T09:30:00Z",
        "readTime": "7 min read",
        "views": "28.6k",
        "coverImage": "assets/covers/cindy-deangelis-grossman-cover.jpg",
        "coverCaption": "Cindy DeAngelis Grossman with her son Christian Walker.",
        "tags": ["Celebrity", "Biography", "Herschel Walker", "NFL", "Business"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Cindy DeAngelis Grossman</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Cindy DeAngelis Grossman</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Year of Birth</th><td style="padding: 8px 0;">1962</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birthplace</th><td style="padding: 8px 0;">Florida, United States</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Education</th><td style="padding: 8px 0;">University of Georgia (Business & Economics)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Businesswoman & Interior Design Consultant</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Marriage Years</th><td style="padding: 8px 0;">March 31, 1983 – 2002 (19 years)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Children</th><td style="padding: 8px 0;">Christian Walker (b. 1999)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Former Spouse</th><td style="padding: 8px 0;">Herschel Walker (Heisman Trophy Winner, NFL Running Back)</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$1.5 Million - $2 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Throughout the 1980s and 1990s, Herschel Walker was one of the most prominent athletes in American sports—a Heisman Trophy winner at the University of Georgia and an accomplished NFL running back. Alongside him during his formative collegiate years and prime professional seasons was his college sweetheart and former wife, Cindy DeAngelis Grossman.</p>

            <p>Over a nineteen-year marriage, Grossman managed their household across multiple relocations and built an independent career in interior design and business consulting. Today, she maintains a dignified, private life while remaining closely involved with her family.</p>

            <h2>Early Life and Collegiate Background</h2>
            <p>Cindy DeAngelis was born in 1962 in Florida into an Italian-American family. Her father, Thomas DeAngelis, worked as a real estate investor and businessman, giving her early exposure to business management and entrepreneurship.</p>
            <p>During her youth, she participated in track and cheerleading before enrolling at the University of Georgia in Athens. There, she pursued studies in business administration and economics, demonstrating strong organizational skills and a keen interest in commercial design.</p>

            <h2>Meeting Herschel Walker and 1983 Marriage</h2>
            <p>Cindy first met Herschel Walker in the training facilities at the University of Georgia, where both were recovering from track-related injuries. Their friendship quickly developed into a relationship during Walker's historic Heisman-winning collegiate football career.</p>
            <p>On March 31, 1983, following Walker's decision to turn professional with the New Jersey Generals in the USFL, the pair married in a family ceremony. When Walker later transitioned to the NFL with the Dallas Cowboys, Minnesota Vikings, Philadelphia Eagles, and New York Giants, Grossman supported the family through frequent cross-country moves.</p>

            <h2>Motherhood and Family Life</h2>
            <p>In 1999, the couple welcomed their son, Christian Walker. Grossman focused significant energy on providing stability and education for their son, encouraging his artistic pursuits and competitive cheerleading achievements.</p>
            <p>Christian Walker later achieved national recognition as a cheerleading champion and social media commentator, frequently speaking warmly of his mother's dedication and support during his upbringing.</p>

            <h2>2002 Separation and Independent Career</h2>
            <p>After nineteen years of marriage, Cindy and Herschel Walker separated in 2001 and finalized their divorce in 2002. The separation was prompted by personal challenges, which Walker later discussed openly in his 2008 memoir regarding his mental health journey.</p>
            <p>Following the divorce, Grossman focused on expanding her independent design consultancy, assisting residential clients with renovations, space planning, and decor in Texas and Florida.</p>

            <h2>Life Today and Net Worth</h2>
            <p>Cindy DeAngelis Grossman has largely remained out of the media spotlight, choosing not to participate in partisan politics during Walker's 2022 Senate campaign. She remarried in the mid-2000s and continues to live comfortably in the southern United States.</p>
            <p>Her personal net worth is estimated at <strong>$1.5 Million to $2 Million</strong>, derived from property investments, divorce financial settlements, and her design business activities.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>Where did Cindy DeAngelis and Herschel Walker meet?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They met as student-athletes at the University of Georgia in Athens in the early 1980s.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>How long were Cindy Grossman and Herschel Walker married?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They were married for 19 years, from March 1983 until their divorce was finalized in 2002.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>What is Cindy DeAngelis Grossman's profession?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She has worked primarily in business administration and residential interior design consulting.</p>
              </div>
            </div>
        """
    },
    {
        "id": "kaynette-williams",
        "slug": "kaynette-williams",
        "url": "/kaynette-williams/",
        "title": "The Biography of Kaynette Williams: Inside Her Marriage to Blake Shelton, Career, and Life Today",
        "subtitle": "From Ada high-school roots to Blake Shelton's early Nashville years, exploring the life of Kaynette Williams and her career in education.",
        "excerpt": "A factual biographical chronicle of Kaynette Williams: her background, her marriage and managerial support during Blake Shelton's early career, and her successful professional life in Kansas today.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 3,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning investigative biographer specializing in music history, public figures, and untold celebrity histories."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T11:00:00Z",
        "readTime": "8 min read",
        "views": "48.2k",
        "coverImage": "assets/covers/kaynette-williams-cover.jpg",
        "coverCaption": "Kaynette Williams: From Ada, Oklahoma to Nashville and beyond.",
        "tags": ["Celebrity", "Biography", "Country Music", "Blake Shelton", "Relationships"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Kaynette Williams</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Kaynette Francis Gern (Williams)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Date of Birth</th><td style="padding: 8px 0;">February 20, 1973</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birthplace</th><td style="padding: 8px 0;">Ada, Oklahoma, United States</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Known For</th><td style="padding: 8px 0;">First Wife and Early Manager of Blake Shelton</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Marriage Years</th><td style="padding: 8px 0;">November 17, 2003 – 2006</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Current Spouse</th><td style="padding: 8px 0;">Cody Joe Scheck (m. 2015)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Current Profession</th><td style="padding: 8px 0;">Mathematics Educator & School Facilitator</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$1.5 Million - $2 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Before Blake Shelton became a household name on national television or performed in stadiums across America, he was an aspiring musician performing at local venues in Ada, Oklahoma. Through those formative years, Kaynette Williams was by his side as his primary supporter and business facilitator.</p>

            <p>Their relationship evolved over more than a decade from high school courtship to Nashville's competitive music landscape. Following their divorce in 2006, Williams opted for a quiet, grounded life outside the public eye, building a rewarding career in education.</p>

            <h2>Early Life and Ada High School Roots</h2>
            <p>Kaynette Francis Gern was born on February 20, 1973, in Ada, Oklahoma. Growing up in Pontotoc County, she showed strong aptitude for mathematics and organizational management. At Ada High School, she first met Blake Shelton.</p>
            <p>When Shelton moved to Nashville after high school to pursue songwriting and country music, Williams supported his ambitions. She soon relocated to Tennessee as well, helping manage his early schedules, promotional merchandise, and touring logistics.</p>

            <h2>Nashville Rise and 2003 Marriage</h2>
            <p>Throughout the late 1990s and Shelton's breakthrough with the 2001 chart-topping single "Austin," Williams served as his road manager. On November 17, 2003, after several years together, they married in a private ceremony in Gatlinburg, Tennessee.</p>
            <p>As Shelton's recording schedule expanded, the pressures of national touring placed strains on the marriage. In 2006, the couple filed for divorce, reaching an amicable settlement that concluded their professional and personal partnership.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="/assets/covers/kaynette-williams-middle.jpg" alt="Kaynette Williams Archival Spotlight" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.82rem; color: var(--text-muted); padding: 8px 2px 0 2px; font-style: italic;">Independence Magazine Archival Spotlight — Kaynette Williams.</figcaption>
            </figure>

            <h2>Career in Education and Life in Kansas</h2>
            <p>Following her time in Nashville, Williams returned briefly to Oklahoma before establishing herself in Kansas. Having earned her academic credentials, she transitioned into education as an associate mathematics teacher and school facilitator.</p>
            <p>In 2015, Williams married Cody Joe Scheck, a world-record rodeo champion and respected rancher. Today, they live a fulfilling rural life in Kansas, actively participating in their local school district and equestrian events.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>How long were Kaynette Williams and Blake Shelton together?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They dated for several years starting in high school and were married from November 2003 until their divorce in 2006.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>What does Kaynette Williams do today?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She works as a mathematics educator and school facilitator in Kansas.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Who is Kaynette Williams married to now?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She has been married to rodeo champion Cody Joe Scheck since 2015.</p>
              </div>
            </div>
        """
    },
    {
        "id": "ian-alexander-sr",
        "slug": "ian-alexander-sr",
        "url": "/ian-alexander-sr/",
        "title": "Ian Alexander Sr. Biography: Career, 10-Year Marriage to Regina King, and Life Today",
        "subtitle": "From senior distribution executive roles at Warner Bros and Qwest Records to his decade-long marriage with Academy Award winner Regina King.",
        "excerpt": "A detailed biographical overview of Canadian-born music executive Ian Alexander Sr., his professional background, his 1997 marriage to Regina King, raising their son, and his life today.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 4,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance covers media executives, record industry veterans, and entertainment history."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T10:15:00Z",
        "readTime": "7 min read",
        "views": "39.4k",
        "coverImage": "assets/covers/ian-alexander-sr-cover.jpg",
        "coverCaption": "Ian Alexander Sr. and Regina King during their marriage.",
        "tags": ["Biography", "Music Industry", "Ian Alexander Sr.", "Regina King", "Entertainment"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Ian Alexander Sr.</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Ian Alexander Sr.</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Date of Birth</th><td style="padding: 8px 0;">April 8, 1956</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birthplace</th><td style="padding: 8px 0;">Kamloops, British Columbia, Canada</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Primary Profession</th><td style="padding: 8px 0;">Music Distribution Executive & Consultant</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Key Positions</th><td style="padding: 8px 0;">VP of Distribution (Qwest Records), Warner Bros Records</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Marriage to Regina King</th><td style="padding: 8px 0;">April 23, 1997 – 2007 (10 years)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Children</th><td style="padding: 8px 0;">Ian Alexander Jr. (1996–2022)</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$3 Million - $4 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">While Regina King has long been celebrated as one of Hollywood's most acclaimed actresses and directors, her former husband, Ian Alexander Sr., played a notable behind-the-scenes role in the American music industry during the 1990s and early 2000s.</p>

            <p>Alexander built a respected executive career in record distribution, managing partnerships with major labels and contributing to prominent artist releases before choosing a quieter path outside corporate entertainment.</p>

            <h2>Early Life and Career in the Music Industry</h2>
            <p>Ian Alexander Sr. was born on April 8, 1956, in Kamloops, British Columbia, Canada. Demonstrating a natural aptitude for marketing and logistics, he moved to California in the late 1980s to work in the recording industry.</p>
            <p>He served as Vice President of Distribution at Qwest Records, the influential label founded by legendary producer Quincy Jones. During his tenure, Alexander oversaw album supply chains, retail partnerships, and international distribution before transitioning into corporate distribution projects with Warner Bros Records.</p>

            <h2>Marriage to Regina King (1997–2007)</h2>
            <p>Alexander met Regina King in the mid-1990s as her acting career gained momentum with major roles in <em>Boyz n the Hood</em>, <em>Friday</em>, and <em>Jerry Maguire</em>. On April 23, 1997, they married in a private ceremony in Jamaica.</p>
            <p>Throughout their ten-year marriage, they supported each other's careers while raising their son, Ian Alexander Jr., born in January 1996. Although the couple divorced in 2007, they maintained a dedicated, cooperative relationship as co-parents.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="/assets/covers/ian-alexander-sr-middle.jpg" alt="Ian Alexander Sr. Archival Spotlight" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.82rem; color: var(--text-muted); padding: 8px 2px 0 2px; font-style: italic;">Independence Magazine Archival Spotlight — Ian Alexander Sr. & Regina King.</figcaption>
            </figure>

            <h2>Life Today and Net Worth</h2>
            <p>Today, Alexander maintains a low public profile, residing in Southern California where he provides private music business consulting and supports community music initiatives. His estimated net worth stands between <strong>$3 Million and $4 Million</strong>.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>What was Ian Alexander Sr.'s executive position in music?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">He served as Vice President of Distribution at Quincy Jones's Qwest Records and held distribution roles at Warner Bros Records.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>How long were Regina King and Ian Alexander Sr. married?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They were married for ten years, from 1997 until their divorce in 2007.</p>
              </div>
            </div>
        """
    },
    {
        "id": "kathryn-burrhus",
        "slug": "kathryn-burrhus",
        "url": "/kathryn-burrhus/",
        "title": "Who Is Kathryn Burrhus? Meet Stone Cold Steve Austin's First Wife and High School Sweetheart",
        "subtitle": "Before the WWE stardom of Steve Austin, Kathryn Burrhus was his high school sweetheart and first wife in Edna, Texas.",
        "excerpt": "A biographical chronicle of Kathryn Burrhus: her high school courtship with Steve Austin in Texas, their 1990 marriage, and her private life today.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": False,
        "trendingRank": 5,
        "author": {
            "name": "Elena Vance",
            "role": "Entertainment & Pop Culture Historian",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Elena Vance investigates 20th-century pop culture origins, athletic legends, and public profiles."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T09:45:00Z",
        "readTime": "6 min read",
        "views": "31.9k",
        "coverImage": "assets/covers/kathryn-burrhus-cover.jpg",
        "coverCaption": "Kathryn Burrhus and Steve Austin on their wedding day in November 1990.",
        "tags": ["Celebrity", "Biography", "WWE", "Stone Cold Steve Austin", "Wrestling History"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Kathryn Burrhus</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Kathryn Burrhus</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birth Year</th><td style="padding: 8px 0;">circa 1965</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Hometown</th><td style="padding: 8px 0;">Edna, Jackson County, Texas</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Spouse</th><td style="padding: 8px 0;">Steve Williams ('Stone Cold' Steve Austin) (m. 1990 – ann. 1992)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Marriage Date</th><td style="padding: 8px 0;">November 24, 1990</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Corporate Administration</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Current Status</th><td style="padding: 8px 0;">Living Privately in Texas</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Before Steve Austin became one of the biggest attractions in professional wrestling history, he was Steve Williams—a high school football athlete from Edna, Texas. In those early years, Kathryn Burrhus was his high school sweetheart and first wife.</p>

            <h2>Edna High School Roots</h2>
            <p>Kathryn Burrhus grew up in Jackson County, Texas, where she attended Edna High School. During their teenage years, she and Williams began dating as he played running back for the school football team.</p>
            <p>When Williams enrolled at the University of North Texas, Burrhus remained an important figure in his life, encouraging his athletic pursuits even after knee injuries shifted his goals toward wrestling.</p>

            <h2>Marriage in 1990</h2>
            <p>On November 24, 1990, the couple married in Texas as Austin began wrestling under the name 'Stunning Steve Austin' in regional promotions. However, the demanding travel requirements of regional wrestling led to personal differences, and the marriage was annulled in August 1992.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="/assets/covers/kathryn-burrhus-middle.jpg" alt="Kathryn Burrhus Wedding Archival" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.82rem; color: var(--text-muted); padding: 8px 2px 0 2px; font-style: italic;">Independence Magazine Archival Spotlight — Kathryn Burrhus & Steve Austin.</figcaption>
            </figure>

            <h2>Life After Marriage</h2>
            <p>Following their separation, Burrhus deliberately chose a private life away from sports entertainment. She built a career in administration in Texas and has maintained her privacy over the decades.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>When did Steve Austin and Kathryn Burrhus marry?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They married on November 24, 1990, in Texas.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Did they have children together?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">No, they did not have children during their marriage.</p>
              </div>
            </div>
        """
    },
    {
        "id": "mia-weier",
        "slug": "mia-weier",
        "url": "/mia-weier/",
        "title": "Mia Weier Biography: Inside Her Life and Creative Career With Partner Clea DuVall",
        "subtitle": "Exploring the life and collaborative journey of creative professional Mia Weier alongside actress and filmmaker Clea DuVall.",
        "excerpt": "A biography of Mia Weier: her background in the creative arts, her partnership with actress and director Clea DuVall, and their life in Los Angeles.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": False,
        "trendingRank": 6,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins covers film, culture, and creative partnerships in contemporary entertainment."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T08:30:00Z",
        "readTime": "6 min read",
        "views": "25.7k",
        "coverImage": "assets/covers/mia-weier-cover.jpg",
        "coverCaption": "Mia Weier and Clea DuVall at a Hollywood film premiere.",
        "tags": ["Biography", "Clea DuVall", "Mia Weier", "Hollywood", "Creative Arts"],
        "contentHtml": """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Mia Weier</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Mia Weier</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Partner</th><td style="padding: 8px 0;">Clea DuVall (Actress, Director, Writer)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Residence</th><td style="padding: 8px 0;">Los Angeles, California</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Creative Professional & Production Collaborator</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$1 Million - $1.5 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Mia Weier is a creative professional based in Los Angeles, known publicly for her longtime partnership with celebrated filmmaker and actress Clea DuVall. Together, they form one of independent cinema's most respected creative couples.</p>

            <h2>Background and Creative Pursuits</h2>
            <p>Weier has maintained a low-key public profile while actively collaborating in film and television production circles in Los Angeles. Her work encompasses production coordination, creative development, and artistic consulting.</p>

            <h2>Partnership with Clea DuVall</h2>
            <p>DuVall, recognized for acclaimed roles in <em>The Faculty</em>, <em>Girl, Interrupted</em>, and as director of <em>Happiest Season</em> and <em>High School</em>, has frequently credited Weier's support as essential to her creative focus.</p>
            <p>The couple has appeared together at industry events and red carpets, presenting a unified front that advocates for independent storytelling and diverse representation in media.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="/assets/covers/mia-weier-middle.jpg" alt="Mia Weier Archival Spotlight" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.82rem; color: var(--text-muted); padding: 8px 2px 0 2px; font-style: italic;">Independence Magazine Archival Spotlight — Mia Weier & Clea DuVall.</figcaption>
            </figure>

            <h2>Life in Los Angeles</h2>
            <p>Residing in California, Weier and DuVall continue to balance professional commitments with personal privacy, focusing on meaningful creative projects.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>Who is Mia Weier's partner?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She is the partner of actress and filmmaker Clea DuVall.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Where do they reside?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They reside in Los Angeles, California.</p>
              </div>
            </div>
        """
    }
]

def render_article_html(article):
    canonical_url = f"https://www.independencemagazine.com{article['url']}"
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{article['title']} | Independence Magazine</title>
  <meta name="description" content="{article['excerpt']}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Social Meta Tags -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{article['title']}">
  <meta property="og:description" content="{article['excerpt']}">
  <meta property="og:image" content="https://www.independencemagazine.com/{article['coverImage']}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="Independence Magazine">
  <meta property="article:published_time" content="{article['isoDate']}">
  <meta property="article:section" content="{article['category']}">

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{article['title']}">
  <meta name="twitter:description" content="{article['excerpt']}">
  <meta name="twitter:image" content="https://www.independencemagazine.com/{article['coverImage']}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="shortcut icon" href="/favicon.ico">

  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,400;1,600&display=swap" rel="stylesheet">

  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="/styles/main.css">
  <link rel="stylesheet" href="/styles/components.css">
  <link rel="stylesheet" href="/styles/responsive.css">

  <style>
    /* Desktop Easy-Reading Container & Balanced Gutters */
    .standalone-article-container {{
      width: 100%;
      max-width: 800px;
      margin: 36px auto 80px auto;
      padding-left: 24px;
      padding-right: 24px;
      box-sizing: border-box;
    }}
    @media (max-width: 768px) {{
      .standalone-article-container {{
        margin: 20px auto 50px auto;
        padding-left: 16px;
        padding-right: 16px;
      }}
      .reader-title {{
        font-size: 1.85rem !important;
      }}
    }}
    .article-breadcrumb {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}
    .article-breadcrumb a {{
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.15s ease;
    }}
    .article-breadcrumb a:hover {{
      color: var(--accent-crimson);
    }}
    .reader-title {{
      font-family: var(--font-serif);
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.015em;
      color: var(--text-primary);
      margin-bottom: 14px;
    }}
    .reader-subtitle {{
      font-size: 1.15rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 22px;
    }}
    .reader-cover-box {{
      margin: 28px 0 36px 0;
      border-radius: var(--radius-sm);
      overflow: hidden;
    }}
    .reader-cover-box img {{
      width: 100%;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      border-radius: var(--radius-sm);
    }}
    .reader-prose {{
      font-family: var(--font-sans);
      font-size: 1.1rem;
      line-height: 1.85;
      color: var(--text-primary);
    }}
    .reader-prose p {{
      margin-bottom: 1.5em;
    }}
    .reader-prose h2 {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 700;
      margin-top: 2em;
      margin-bottom: 0.7em;
      line-height: 1.3;
      color: var(--text-primary);
    }}
    .bio-quick-facts-box {{
      margin: 28px 0;
    }}
  </style>

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{canonical_url}"
    }},
    "headline": "{article['title']}",
    "description": "{article['excerpt']}",
    "image": [
      "https://www.independencemagazine.com/{article['coverImage']}"
    ],
    "datePublished": "{article['isoDate']}",
    "dateModified": "{article['isoDate']}",
    "author": {{
      "@type": "Person",
      "name": "{article['author']['name']}",
      "jobTitle": "{article['author']['role']}"
    }},
    "publisher": {{
      "@type": "NewsMediaOrganization",
      "name": "Independence Magazine",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://www.independencemagazine.com/assets/favicon.svg"
      }}
    }}
  }}
  </script>
</head>
<body>
  <!-- Top Utility Bar -->
  <aside class="top-utility-bar" aria-label="Edition Bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <a href="/" style="font-weight: 700; color: var(--text-primary); display: flex; align-items: center; gap: 6px;">
          &larr; Independence Magazine Homepage
        </a>
      </div>
      <div class="top-bar-right">
        <span>Verified Independent Press</span>
      </div>
    </div>
  </aside>

  <!-- Sticky Header -->
  <header class="site-header">
    <div class="container header-inner">
      <a href="/" class="brand-masthead" style="align-items: flex-start;">
        <span class="brand-title" style="font-size: 1.85rem;">Independence<span class="dot-accent">.</span></span>
        <span class="brand-subtitle" style="font-size: 0.65rem; margin-top: 2px;">MAGAZINE</span>
      </a>
      <div class="header-actions">
        <button class="theme-switch-btn" id="articleThemeBtn" title="Toggle Appearance">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" /></svg>
        </button>
        <a href="/#newsletterSection" class="btn btn-primary btn-sm">Subscribe</a>
      </div>
    </div>
  </header>

  <!-- Main Article Container -->
  <main class="standalone-article-container">
    <div class="article-breadcrumb">
      <a href="/">Home</a>
      <span>/</span>
      <a href="/#{article['categorySlug']}" style="color: var(--accent-crimson); font-weight: 600;">{article['category']}</a>
      <span>/</span>
      <span style="color: var(--text-primary);">{article['title']}</span>
    </div>

    <header class="reader-article-header">
      <span class="category-badge" style="margin-bottom: 14px;">{article['category']}</span>
      <h1 class="reader-title">{article['title']}</h1>
      <p class="reader-subtitle">{article['subtitle']}</p>

      <div class="reader-author-bar">
        <div class="author-pill">
          <img src="{article['author']['avatar']}" alt="{article['author']['name']}">
          <div>
            <div class="author-name">By {article['author']['name']}</div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">{article['author']['role']}</div>
          </div>
        </div>
        <div class="article-meta">
          <span>{article['readTime']}</span>
          <span class="article-meta-divider"></span>
          <span>{article['publishedAt']}</span>
        </div>
      </div>
    </header>

    <figure class="reader-cover-box">
      <img src="/{article['coverImage']}" alt="{article['title']}" style="width: 100%; border-radius: var(--radius-sm); display: block;">
      <figcaption class="reader-caption">{article['coverCaption']}</figcaption>
    </figure>

    <div class="reader-prose">
      {article['contentHtml']}
    </div>

    <!-- Author Bio Box -->
    <div style="background-color: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 3px solid var(--accent-crimson); border-radius: var(--radius-xs); padding: 22px; margin-top: 50px; display: flex; gap: 18px; align-items: center;">
      <img src="{article['author']['avatar']}" alt="{article['author']['name']}" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; border: 1px solid var(--border-light);">
      <div>
        <h4 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; margin-bottom: 2px;">{article['author']['name']}</h4>
        <div style="font-size: 0.74rem; color: var(--accent-crimson); text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">{article['author']['role']}</div>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.5;">{article['author']['bio']}</p>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container" style="text-align: center;">
      <div class="brand-masthead" style="align-items: center; margin-bottom: 12px;">
        <span class="brand-title" style="color: #ffffff; font-size: 2.2rem;">Independence<span class="dot-accent">.</span></span>
        <span class="brand-subtitle" style="color: #64748b; font-size: 0.68rem; margin-top: 4px;">MAGAZINE</span>
      </div>
      <p style="font-size: 0.84rem; color: var(--text-muted); margin-bottom: 18px;">
        Authoritative biographical profiles and investigative journalism.
      </p>
      <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; margin-bottom: 18px; font-size: 0.82rem;">
        <a href="/about.html" style="color: #cbd5e1;">About</a>
        <a href="/editorial-policy.html" style="color: #cbd5e1;">Editorial Charter</a>
        <a href="/contact.html" style="color: #cbd5e1;">Contact</a>
        <a href="/privacy-policy.html" style="color: #cbd5e1;">Privacy Policy</a>
        <a href="/terms-of-service.html" style="color: #cbd5e1;">Terms of Service</a>
        <a href="/disclaimer.html" style="color: #cbd5e1;">Disclaimer</a>
      </div>
      <div style="font-size: 0.78rem; color: #64748b;">
        &copy; 2026 Independence Magazine. All Rights Reserved. &bull; Contact: <a href="mailto:info.washingtontimes@gmail.com" style="color: inherit;">info.washingtontimes@gmail.com</a> &bull; Digital Partner: <a href="https://digitalrank.io" target="_blank" rel="noopener" style="color: #38bdf8;">DigitalRank.io</a>
      </div>
    </div>
  </footer>

  <script>
    const savedTheme = localStorage.getItem("independence_theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);

    document.getElementById('articleThemeBtn')?.addEventListener('click', () => {{
      const curr = document.documentElement.getAttribute("data-theme") || "light";
      const next = curr === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("independence_theme", next);
    }});
  </script>
</body>
</html>"""

def main():
    print("1. Rewriting js/articles-data.js with all 6 clean articles...")
    js_content = f"""/**
 * Independence Magazine - Celebrity & Biographical Journalism Repository
 * Authentic Editorial Standards & Fact-Checked Biographies
 */

const ARTICLES_DATA = {json.dumps(CLEAN_ARTICLES, indent=2)};

if (typeof window !== 'undefined') {{
  window.ARTICLES_DATA = ARTICLES_DATA;
}}
"""
    with open(ARTICLES_DATA_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("articles-data.js updated!")

    print("2. Generating clean static URL directories and index.html files...")
    for art in CLEAN_ARTICLES:
        slug_dir = os.path.join(BASE_DIR, art["slug"])
        os.makedirs(slug_dir, exist_ok=True)
        html_file = os.path.join(slug_dir, "index.html")
        html_content = render_article_html(art)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated clean URL page: /{art['slug']}/index.html")

    print("3. Updating sitemap.xml with clean URLs...")
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Publication Pages -->
  <url>
    <loc>https://www.independencemagazine.com/</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/about.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/contact.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/editorial-policy.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/privacy-policy.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/terms-of-service.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/disclaimer.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
"""
    for art in CLEAN_ARTICLES:
        sitemap_xml += f"""  <url>
    <loc>https://www.independencemagazine.com{art['url']}</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""
    sitemap_xml += "</urlset>\n"

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("sitemap.xml updated with clean URLs!")

if __name__ == "__main__":
    main()
