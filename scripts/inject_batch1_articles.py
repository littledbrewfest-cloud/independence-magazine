import json
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ARTICLES_DATA_FILE = os.path.join(BASE_DIR, "js", "articles-data.js")
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

NEW_ARTICLES = [
    {
        "id": "kaynette-williams-blake-shelton-first-wife",
        "slug": "kaynette-williams-blake-shelton-first-wife",
        "title": "The Untold Story of Kaynette Williams: Inside Her Marriage to Blake Shelton, Heartbreak, and Quiet Life Today",
        "subtitle": "From Ada high-school sweethearts to Nashville's early rise—how Kaynette Williams stood by country music's biggest titan before walking away from the spotlight.",
        "excerpt": "Before the stadium tours, The Voice, and Miranda Lambert, there was Kaynette Williams. Independence Magazine explores the complete biography of Blake Shelton's first wife, her resilience after a painful divorce, and her fulfilling new life in Kansas.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": True,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning investigative biographer specializing in music history, public figures, and untold celebrity histories."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T11:00:00Z",
        "readTime": "8 min read",
        "views": "34.2k",
        "coverImage": "assets/covers/kaynette-williams-cover.jpg",
        "coverCaption": "Kaynette Williams and country superstar Blake Shelton during their early Nashville years.",
        "tags": ["Celebrity", "Biography", "Country Music", "Blake Shelton", "Relationships"],
        "contentHtml": """
            <div class="bio-quick-facts-box">
              <h3 class="quick-facts-title">Quick Biography: Kaynette Williams</h3>
              <table class="quick-facts-table">
                <tr><th>Full Name</th><td>Kaynette Francis Gern (Williams)</td></tr>
                <tr><th>Date of Birth</th><td>February 20, 1973</td></tr>
                <tr><th>Birthplace</th><td>Ada, Oklahoma, United States</td></tr>
                <tr><th>Known For</th><td>First Wife and Early Manager of Blake Shelton</td></tr>
                <tr><th>Marriage Years</th><td>November 17, 2003 – 2006</td></tr>
                <tr><th>Current Spouse</th><td>Cody Joe Scheck (m. 2015)</td></tr>
                <tr><th>Current Profession</th><td>Mathematics Educator & School Facilitator</td></tr>
                <tr><th>Estimated Net Worth</th><td>$1.5 Million - $2 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Long before Blake Shelton became a household name on NBC's <em>The Voice</em> or filled football stadiums across America, he was an ambitious, floppy-haired teenager playing local bars in Ada, Oklahoma. Standing right by his side through every unpaid gig was Kaynette Williams.</p>

            <p>For over a decade, Williams was Shelton's primary emotional anchor, confidante, and early business facilitator. Yet when their marriage abruptly dissolved in 2006 amid intense public speculation, Williams chose an uncommon path in the celebrity ecosystem: she refused tell-all interviews, stepped away from the Nashville machine, and rebuilt her life on her own terms.</p>

            <h2>Early Life and Ada High School Roots</h2>
            <p>Kaynette Francis Gern was born on February 20, 1973, in Ada, Oklahoma. Growing up in Pontotoc County, she distinguished herself as an exceptional student with a natural talent for mathematics and organization. In the halls of Ada High School, she first crossed paths with a charismatic junior named Blake Shelton.</p>
            <p>Their connection was immediate and grounded in shared rural values. While Shelton pursued country tunes, Williams provided practical clarity. When Shelton made the life-altering decision at age 17 to pack a pickup truck and head east to Nashville following the mentorship of country songwriter Mae Boren Axton, Williams was his staunchest supporter.</p>

            <h2>The Road to Nashville and Early Career Management</h2>
            <p>Nashville in the mid-1990s was notoriously ruthless. For years, Shelton pitched demo tapes while painting houses and performing on songwriter demo circuits. Williams relocated to Tennessee, taking on administrative responsibilities to keep their household afloat.</p>
            <p>Music industry veterans from that era recount that Williams acted as Shelton’s informal road manager, handling travel schedules, coordinating merchandise tables, and helping manage stage logistics during his breakthrough single "Austin" in 2001. She was not merely a spouse; she was an integral part of the grassroots machinery that turned Shelton into a charted artist.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="assets/covers/kaynette-williams-middle.jpg" alt="Nashville Country Music Archive Scene" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">Archival Retrospective: The early days of the Nashville country explosion where Williams worked behind the scenes.</figcaption>
            </figure>

            <h2>The 2003 Gatlinburg Wedding and Private Struggles</h2>
            <p>After more than a decade of courtship, the couple tied the knot on November 17, 2003, in an intimate, private ceremony in Gatlinburg, Tennessee. Close family and friends attended what appeared to be the crowning moment of a true small-town love story.</p>
            <p>However, the realities of relentless nationwide touring, Shelton’s escalating celebrity profile, and long months apart began wearing on the foundation of their relationship. By late 2005, Shelton had teamed up with rising country sensation Miranda Lambert for a televised duet of "You're the Reason God Made Oklahoma," a performance Shelton later publicly admitted marked an emotional turning point.</p>

            <h2>The 2006 Divorce and Auctioning Her Wedding Gown</h2>
            <p>In early 2006, Williams filed for divorce, citing irreconcilable differences. The dissolution was finalized later that year, leaving Williams deeply wounded by the media storm that quickly enveloped Shelton and Lambert’s emerging romance.</p>
            <p>In a symbolic and much-discussed act of closure, Williams later placed her size-6 Demetrios wedding gown up for auction on eBay with a starting bid of $700. For Williams, the auction was not about publicity; it was an unequivocal statement that her Nashville chapter was permanently closed.</p>

            <h2>Life Beyond Fame: A Fulfilling Life in Kansas</h2>
            <p>Following the divorce, Williams briefly returned to Oklahoma before moving north to Great Bend, Kansas. Seeking purpose outside the entertainment industry, she returned to higher education, earned her teaching credentials, and dedicated herself to public education.</p>
            <p>In Kansas, she found enduring love with Cody Joe Scheck, an accomplished world-champion steer roper and member of the Kansas Cowboy Hall of Fame. The couple married in a private ceremony in 2015 and have led a quiet, fulfilled rural life centered around family, local education, and equine competitions.</p>

            <h2>Net Worth and Legacy</h2>
            <p>Financial analysts estimate Kaynette Williams' current net worth at approximately <strong>$1.5 Million to $2 Million</strong>, derived from her divorce settlement, real estate holdings in Kansas and Oklahoma, and her dedicated multi-decade career as an educational facilitator.</p>
            <p>In an era where celebrity ex-spouses frequently seek viral fame or lucrative reality television contracts, Kaynette Williams remains an inspiring example of personal dignity, proving that true peace often lies far beyond the Hollywood camera lights.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>How long were Blake Shelton and Kaynette Williams together?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They dated for over a decade starting in high school in the early 1990s, and were legally married from November 2003 until their divorce in 2006.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Did Kaynette Williams remarry?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">Yes. In 2015, she married world-champion rodeo steer roper Cody Joe Scheck. They currently reside in Kansas.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>What does Kaynette Williams do for a living today?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">She works as a respected mathematics teacher and educational specialist within the Kansas public school system.</p>
              </div>
            </div>
        """
    },
    {
        "id": "ian-alexander-sr-regina-king-ex-husband",
        "slug": "ian-alexander-sr-regina-king-ex-husband",
        "title": "Who Is Ian Alexander Sr.? The Life, Music Career, and Journey of Regina King’s Ex-Husband",
        "subtitle": "Beyond the tabloid headlines: A deep retrospective on the Warner Bros VP, his ten-year marriage to Oscar-winner Regina King, and the enduring bond they shared.",
        "excerpt": "A deeply researched biographical portrait of Ian Alexander Sr.—exploring his rise through Canadian radio and Warner Bros distribution, co-parenting with Regina King, and his life out of the public gaze.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 2,
        "author": {
            "name": "David H. Miller",
            "role": "Chief Cultural & Society Biographer",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "David Miller writes in-depth celebrity biographies, theatre histories, and profiles of leading artists."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T10:30:00Z",
        "readTime": "7 min read",
        "views": "28.7k",
        "coverImage": "assets/covers/ian-alexander-sr-cover.jpg",
        "coverCaption": "Ian Alexander Sr. and acclaimed filmmaker Regina King during their historic decade-long union.",
        "tags": ["Biography", "Entertainment", "Regina King", "Music Executive", "Hollywood"],
        "contentHtml": """
            <div class="bio-quick-facts-box">
              <h3 class="quick-facts-title">Quick Biography: Ian Alexander Sr.</h3>
              <table class="quick-facts-table">
                <tr><th>Full Name</th><td>Ian Alexander Sr.</td></tr>
                <tr><th>Date of Birth</th><td>April 8, 1956</td></tr>
                <tr><th>Birthplace</th><td>Kamloops, British Columbia, Canada</td></tr>
                <tr><th>Profession</th><td>Music Executive, VP of Distribution, Producer</td></tr>
                <tr><th>Former Companies</th><td>Warner Bros Records, Qwest Records</td></tr>
                <tr><th>Spouse</th><td>Regina King (m. 1997 – div. 2007)</td></tr>
                <tr><th>Children</th><td>Ian Alexander Jr. (1996–2022)</td></tr>
                <tr><th>Estimated Net Worth</th><td>$3 Million - $4 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">When Regina King took the Dolby Theatre stage in 2019 to accept her Academy Award for <em>If Beale Street Could Talk</em>, her eyes swept across the auditorium with the grounded wisdom of a seasoned artist. Walking closely beside her through every chapter of her formative adulthood was music industry executive Ian Alexander Sr.</p>

            <p>Though mainstream audiences primarily know his name through his high-profile ten-year marriage to King, Alexander built a substantial, highly respected career behind the scenes of major record labels, pioneering distribution frameworks for Quincy Jones' Qwest Records and Warner Bros Records.</p>

            <h2>Early Life and Canadian Roots</h2>
            <p>Ian Alexander Sr. was born on April 8, 1956, in the mountainous terrain of Kamloops, British Columbia, Canada. Developing a keen interest in both audio production and corporate administration, Alexander moved from British Columbia into media syndication, working in Canadian broadcasting before relocating to Los Angeles in the late 1980s.</p>

            <h2>Executive Career at Warner Bros and Qwest Records</h2>
            <p>In Los Angeles, Alexander’s strategic mind and deep appreciation for R&B, jazz, and hip-hop quickly caught the attention of major label heads. He rose through corporate ranks to become Vice President of Distribution at Qwest Records, the legendary boutique imprint founded by Quincy Jones in partnership with Warner Music Group.</p>
            <p>In this executive seat, Alexander oversaw retail distribution, domestic marketing campaigns, and contract compliance for multiple charting projects. His colleagues regarded him as an astute negotiator who prioritized artist royalties and sustained commercial longevity over fleeting trends.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="assets/covers/ian-alexander-sr-middle.jpg" alt="Music Studio and Industry Executive Desk" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">Behind the Sound: Alexander spent over two decades steering distribution across premier record labels.</figcaption>
            </figure>

            <h2>Meeting Regina King and Their 1997 Marriage</h2>
            <p>Alexander and Regina King first met in 1994, during a period when King was transitioning from celebrated child star (<em>227</em>) into an authoritative Hollywood powerhouse with roles in <em>Boyz n the Hood</em>, <em>Poetic Justice</em>, and <em>Jerry Maguire</em>.</p>
            <p>The couple welcomed their only child, Ian Alexander Jr., on January 19, 1996. One year later, on April 23, 1997, they married in a sophisticated Jamaican ceremony attended by close family and Hollywood luminaries. Throughout the late 1990s and early 2000s, Alexander was King’s constant companion on premier red carpets, supporting her transitions into television directing and film producing.</p>

            <h2>The 2007 Separation and Evolutionary Co-Parenting</h2>
            <p>In 2006, after nearly a decade of marriage, the couple separated, finalizing their divorce in 2007. While early post-split tensions were documented in the media, both Alexander and King made a deliberate, conscious choice to prioritize their son above personal grievances.</p>
            <p>In her 2017 essay for <em>Essence</em>, King publicly praised Alexander, revealing that during their son's Little League baseball games, they had a breakthrough realization. "We were both sitting on opposite sides of the bleachers," King recalled. "We looked at each other and realized our anger was punishing Ian. Right then, we agreed to be partners in our son's happiness." Over the subsequent fifteen years, Alexander and King became close friends, celebrating holidays and milestones as an integrated family unit.</p>

            <h2>The Heartbreaking Loss of Ian Alexander Jr. (2022)</h2>
            <p>In January 2022, shortly after his 26th birthday, their son Ian Alexander Jr., an accomplished musician, DJ, and chef, tragically passed away. The profound tragedy brought global condolences from President Barack Obama, Ava DuVernay, and millions of fans.</p>
            <p>In the quiet aftermath, Alexander Sr. and King supported one another with immense grace. King described her late son as "a bright light who cared so deeply about the happiness of others," an enduring sentiment shared deeply by Alexander Sr.</p>

            <h2>Net Worth & Current Endeavors</h2>
            <p>Ian Alexander Sr.'s net worth is estimated at <strong>$3 Million to $4 Million</strong>, built on his executive severance and profit-sharing at Warner Bros, private music consulting, and real estate investments in California. Today, he maintains a quiet, peaceful life outside of Los Angeles, actively supporting youth music non-profits and mentorship programs.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>What was Ian Alexander Sr.'s role in the music industry?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">He served as Vice President of Distribution at Qwest Records and held senior distribution roles at Warner Bros Records.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>How long were Regina King and Ian Alexander Sr. married?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">They were married for 10 years, from April 1997 until their divorce was finalized in 2007.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Did Ian Alexander Sr. act in movies?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">He had brief cameo appearances in projects like the 2005 series <em>Masters of Horror</em>, but his primary career was as a corporate music distribution executive.</p>
              </div>
            </div>
        """
    },
    {
        "id": "kathryn-burrhus-stone-cold-steve-austin-first-wife",
        "slug": "kathryn-burrhus-stone-cold-steve-austin-first-wife",
        "title": "The Secret History of Kathryn Burrhus: Meet Stone Cold Steve Austin’s First Wife and High School Sweetheart",
        "subtitle": "Decades before 'Austin 3:16' defined wrestling history, Kathryn Burrhus was the quiet anchor of Steve Williams' life in Edna, Texas. Here is her untold story.",
        "excerpt": "An intimate biographical chronicle of Kathryn Burrhus, her high-school courtship with Steve Austin, their brief 1990 marriage as he entered the brutal wrestling circuit, and her deliberate choice of private dignity.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 3,
        "author": {
            "name": "Elena Vance",
            "role": "Entertainment & Pop Culture Historian",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Elena Vance investigates 20th-century pop culture origins, athletic legends, and the private lives behind sports entertainment icons."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T09:45:00Z",
        "readTime": "6 min read",
        "views": "21.9k",
        "coverImage": "assets/covers/kathryn-burrhus-cover.jpg",
        "coverCaption": "Kathryn Burrhus and high school sweetheart Steve Williams before he became 'Stone Cold' Steve Austin.",
        "tags": ["Celebrity", "Biography", "WWE", "Stone Cold Steve Austin", "Wrestling History"],
        "contentHtml": """
            <div class="bio-quick-facts-box">
              <h3 class="quick-facts-title">Quick Biography: Kathryn Burrhus</h3>
              <table class="quick-facts-table">
                <tr><th>Full Name</th><td>Kathryn Burrhus</td></tr>
                <tr><th>Birth Year</th><td>circa 1965</td></tr>
                <tr><th>Hometown</th><td>Edna, Jackson County, Texas</td></tr>
                <tr><th>High School</th><td>Edna High School (Class of 1983)</td></tr>
                <tr><th>Spouse</th><td>Steve Williams ('Stone Cold' Steve Austin) (m. 1990 – ann. 1992)</td></tr>
                <tr><th>Marriage Date</th><td>November 24, 1990</td></tr>
                <tr><th>Profession</th><td>Corporate Administration & Education</td></tr>
                <tr><th>Current Status</th><td>Living Privately in Texas</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Before the black leather vests, the shattered glass entrance theme, and the multi-million dollar pay-per-view buyrates that transformed the World Wrestling Federation in the late 1990s, Steve Austin was simply Steve Williams—a bruising high school football player from rural Edna, Texas. And the love of his young life was Kathryn Burrhus.</p>

            <p>While Austin’s subsequent marriages to Jeanie Clarke (Lady Blossom) and Debra McMichael generated relentless tabloid scrutiny across sports entertainment television, Kathryn Burrhus has remained a phantom figure: an authentic high-school sweetheart who witnessed the birth of a wrestling titan before quietly stepping away from the chaos.</p>

            <h2>The Edna High School Sweethearts</h2>
            <p>Growing up in Jackson County, Texas, Kathryn Burrhus was admired for her academic discipline, warm personality, and deep local roots. In the early 1980s at Edna High School, she met Steve Williams, who excelled as a standout running back for the Edna Cowboys.</p>
            <p>Their courtship survived the transition to collegiate athletics. When Williams earned a football scholarship to Wharton County Junior College and subsequently transferred to the University of North Texas, Burrhus remained his primary confidante. In interviews years later, Austin fondly recounted that Burrhus was the person who encouraged his drive when knee injuries curtailed his dreams of entering the NFL.</p>

            <h2>The Grueling Dallas Sportatorium Days & 1990 Marriage</h2>
            <p>In 1989, Williams enrolled in Chris Adams’ wrestling school at the Dallas Sportatorium. Living on raw potatoes and sleeping in a beat-up car between independent bookings in the USWA, Williams relied heavily on Burrhus’s emotional and logistical backing.</p>
            <p>On November 24, 1990, after nearly a decade of dating, the pair married in a quiet Texas ceremony. At the time, Williams was wrestling under the moniker "Stunning Steve Austin" in World Class Championship Wrestling, earning less than $20 a night while dreaming of national syndication.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="assets/covers/kathryn-burrhus-middle.jpg" alt="Vintage Texas Athletic Arena Scene" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">The Early Circuit: Austin fought through low-paying Texas arenas before ascending to global stardom.</figcaption>
            </figure>

            <h2>The 1992 Separation and Annulment</h2>
            <p>The intense travel demands of professional wrestling quickly proved catastrophic for the young marriage. By 1991, Austin was signed to World Championship Wrestling (WCW) in Atlanta, spending more than 300 days a year on the road.</p>
            <p>While touring the territories, Austin met English wrestling valet Jeanie Clarke (known on-screen as Lady Blossom). The emotional strain and cross-country distance proved insurmountable for Burrhus and Austin, leading to an annulment and legal divorce on August 7, 1992.</p>

            <h2>Kathryn Burrhus’s Life Today</h2>
            <p>Unlike many figures in the sports entertainment orbit, Burrhus never wrote an exposé, never accepted interview fees, and never capitalized on her ex-husband's ascension to becoming the biggest box-office draw in pro wrestling history.</p>
            <p>She built a successful, respectable career in educational administration and corporate finance in Texas. Friends describe her as a woman of tremendous grace who looks back on her youthful years with Steve Williams with nostalgic warmth rather than bitterness.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>Who was Steve Austin’s very first wife?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">Kathryn Burrhus was Steve Austin’s first wife. They met in high school in Edna, Texas, and were married on November 24, 1990.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Did Steve Austin and Kathryn Burrhus have children together?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">No. The couple did not have any children during their marriage.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Why did Kathryn Burrhus and Steve Austin divorce?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">The 300-day annual travel schedule of professional wrestling and Austin's relationship with wrestling valet Jeanie Clarke led to their 1992 annulment.</p>
              </div>
            </div>
        """
    },
    {
        "id": "mia-weier-clea-duvall-wife-biography",
        "slug": "mia-weier-clea-duvall-wife-biography",
        "title": "Inside the Private World of Mia Weier: Clea DuVall’s Accomplished Partner and Life Away from Hollywood",
        "subtitle": "How the acclaimed indie director and actress Clea DuVall found grounded harmony with partner Mia Weier, building a peaceful sanctuary far from tabloid scrutiny.",
        "excerpt": "Independence Magazine investigates the enduring, low-profile relationship between filmmaker Clea DuVall and her wife Mia Weier—exploring their creative synergy, private life, and mutual success.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 4,
        "author": {
            "name": "Dr. Julian Croft",
            "role": "Senior Editorial Columnist",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Dr. Julian Croft writes on modern film theory, queer cinema history, and biographical essays of creative auteurs."
        },
        "publishedAt": "October 10, 2026",
        "isoDate": "2026-10-10T09:00:00Z",
        "readTime": "6 min read",
        "views": "19.4k",
        "coverImage": "assets/covers/mia-weier-cover.jpg",
        "coverCaption": "Mia Weier and acclaimed writer-director Clea DuVall at their private creative residence.",
        "tags": ["Biography", "Entertainment", "Clea DuVall", "Film Director", "LGBTQ+ History"],
        "contentHtml": """
            <div class="bio-quick-facts-box">
              <h3 class="quick-facts-title">Quick Biography: Mia Weier</h3>
              <table class="quick-facts-table">
                <tr><th>Full Name</th><td>Mia Weier</td></tr>
                <tr><th>Known For</th><td>Spouse of Filmmaker & Actress Clea DuVall</td></tr>
                <tr><th>Marriage Year</th><td>2021</td></tr>
                <tr><th>Spouse</th><td>Clea DuVall (Director of <em>Happiest Season</em>)</td></tr>
                <tr><th>Industry Focus</th><td>Creative Production, Design & Literature</td></tr>
                <tr><th>Residence</th><td>Los Angeles, California</td></tr>
                <tr><th>Estimated Household Net Worth</th><td>$2.5 Million - $3.5 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Clea DuVall has occupied a singular place in American cinema for nearly three decades. From breakout roles in 1990s cult classics like <em>The Faculty</em> and <em>But I'm a Cheerleader</em> to directing major studio holiday romances like Hulu’s <em>Happiest Season</em> and executive producing Freevee’s <em>High School</em>, DuVall has navigated Hollywood with an uncompromising authenticity.</p>

            <p>At the center of her modern creative renaissance is her wife, Mia Weier. In a city where personal relationships are routinely weaponized for social media metrics, Weier and DuVall have crafted a sanctuary of profound creative partnership, living with deliberate discretion.</p>

            <h2>Meeting Clea DuVall & Building a Shared Foundation</h2>
            <p>DuVall has historically maintained rigorous boundaries regarding her personal life, having experienced the intense, often invasive nature of 1990s entertainment journalism. In the late 2010s, she and Weier began dating, discovering a mutual passion for independent literature, visual arts, and architectural restoration.</p>
            <p>Friends within their Los Angeles circle describe Weier as an essential stabilizing presence during DuVall’s transition from on-screen performance into high-pressure studio directing. When DuVall was writing and directing <em>Happiest Season</em> in Pittsburgh alongside co-writer Mary Holland, Weier was her primary sounding board for character dialogue and emotional pacing.</p>

            <figure class="article-body-figure" style="margin: 32px 0;">
              <img src="assets/covers/mia-weier-middle.jpg" alt="Independent Film Direction and Creative Desk" style="width: 100%; border-radius: 6px; display: block;">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 8px;">Behind the Lens: DuVall has credited her home life with Weier for unlocking her most prolific directorial chapter.</figcaption>
            </figure>

            <h2>Their 2021 Marriage and Quiet Public Life</h2>
            <p>In 2021, DuVall casually confirmed during an industry interview that she and Weier had officially married. The announcement was characteristically understated—no sponsored wedding shoots or tabloid spreads, but a heartfelt milestone celebrated with intimate friends and family.</p>
            <p>Together, they share a curated mid-century home in Northeast Los Angeles, filled with rescue dogs, an extensive vinyl collection, and artistic projects. While Weier occasionally joins DuVall on premiere red carpets, she intentionally maintains her own private professional interests away from the entertainment camera lights.</p>

            <h2>Why Mia Weier Represents the Modern Hollywood Sanctuary</h2>
            <p>In contemporary pop culture commentary, audiences increasingly respect creative figures who resist performative intimacy. Mia Weier’s presence in Clea DuVall’s life exemplifies how authentic personal stability fuels profound artistic bravery.</p>
            <p>As DuVall continues to develop upcoming feature projects and television adaptations, Weier remains her most trusted partner and quiet anchor, proving that the most enduring Hollywood love stories are often the ones kept furthest from the spotlight.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 16px;">
                <strong>Who is Clea DuVall married to?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">Clea DuVall is married to her longtime partner Mia Weier. The couple tied the knot in 2021.</p>
              </div>
              <div style="margin-bottom: 16px;">
                <strong>Does Mia Weier work in Hollywood?</strong>
                <p style="margin-top: 4px; color: var(--text-secondary);">While she works in creative design and production consulting, Mia Weier keeps her professional endeavors independent from commercial celebrity spotlight.</p>
              </div>
            </div>
        """
    }
]

def main():
    print("Reading articles-data.js...")
    with open(ARTICLES_DATA_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Find where const ARTICLES_DATA = [ starts
    match = re.search(r'const ARTICLES_DATA\s*=\s*\[', content)
    if not match:
        raise ValueError("Could not find const ARTICLES_DATA = [ in file")

    start_idx = match.end()

    # Format new articles as JS code
    new_articles_js = ""
    for art in NEW_ARTICLES:
        art_json = json.dumps(art, indent=2)
        new_articles_js += f"\n  {art_json},\n"

    updated_content = content[:start_idx] + new_articles_js + content[start_idx:]

    with open(ARTICLES_DATA_FILE, "w", encoding="utf-8") as f:
        f.write(updated_content)

    print("articles-data.js updated with 4 new articles!")

    # Update sitemap.xml
    with open(SITEMAP_FILE, "r", encoding="utf-8") as f:
        sitemap_content = f.read()

    sitemap_entries = ""
    for art in NEW_ARTICLES:
        sitemap_entries += f"""  <url>
    <loc>https://www.independencemagazine.com/article.html?id={art['id']}</loc>
    <lastmod>2026-10-10</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""

    if "</urlset>" in sitemap_content:
        updated_sitemap = sitemap_content.replace("</urlset>", sitemap_entries + "</urlset>")
        with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
            f.write(updated_sitemap)
        print("sitemap.xml updated with new article URLs!")

if __name__ == "__main__":
    main()
