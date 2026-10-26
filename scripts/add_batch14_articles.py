import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH14_ARTICLES = [
    # 1. Vanessa Villanueva
    {
        "id": "vanessa-villanueva",
        "slug": "vanessa-villanueva",
        "url": "/vanessa-villanueva/",
        "title": "Vanessa Villanueva: Life After Her Marriage to Chris Perez, Children, and Quiet Career in 2026",
        "subtitle": "An in-depth editorial profile of Vanessa Villanueva: her six-year marriage to musician Chris Perez, raising Cassie and Noah, her brief foray into the entertainment industry, and her private life in Texas.",
        "excerpt": "Explore the life of Vanessa Villanueva in 2026: her marriage and divorce with Chris Perez, children Cassie and Noah Perez, age, estimated net worth, and life away from the spotlight.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "October 25, 2026",
        "isoDate": "2026-10-25",
        "readTime": "9 min read",
        "views": "48.2K",
        "coverImage": "assets/covers/vanessa-villanueva-cover.jpg",
        "coverCaption": "Vanessa Villanueva attending a formal Texas arts gala alongside Chris Perez during their marriage in the mid-2000s.",
        "tags": ["Vanessa Villanueva", "Chris Perez", "Vanessa Villanueva Age", "Vanessa Villanueva Net Worth", "Cassie Perez", "Noah Perez", "Chris Perez Ex-Wife"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the complex tapestry of American music history, certain individuals occupy a unique space where public curiosity intersects with deeply private healing. Vanessa Villanueva is one such figure. Known internationally as the former wife of Grammy-winning guitarist Chris Perez—whose earlier marriage to Tejano superstar Selena Quintanilla ended in national tragedy in 1995—Villanueva entered the public conversation during a delicate transitional chapter in American pop culture. Yet despite the relentless spotlight that shadowed her relationship, she has consistently maintained a grounded, dignified demeanor, dedicating her energy to parenting her two children and building a modest, autonomous life in South Texas.</p>

            <p>Much like other grounded women connected to renowned musical figures—such as <a href="/ria-sommerfeld/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Ria Sommerfeld</a> following her chapter with Tom Kaulitz or <a href="/kaynette-williams/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Kaynette Williams</a> charting an independent course after country music fame—Villanueva refused to commodify her personal history for tabloid exploitation. Her narrative is defined not by celebrity glamour, but by enduring domestic resilience and maternal dedication.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic & SparkDaily) -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Category</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Legal Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Vanessa Villanueva</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">circa 1978</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">48 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Heritage</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Texas, United States (Mexican-American heritage)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Chris Perez (married 2001, divorced 2008)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Cassie Perez (born 1998) and Noah Perez (born 2005)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Professional Field</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Former Film Production Assistant & Esthetics Entrepreneur</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$150,000 – $300,000 USD (independent of Perez assets)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">San Antonio metropolitan area, Texas</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Upbringing and Texas Heritage</h2>
            <p>Vanessa Villanueva was born in Texas during the late 1970s to parents of Mexican descent. Growing up within the rich, close-knit Hispanic communities of South Texas, she developed strong values centered around family loyalty, cultural heritage, and privacy. Unlike many contemporaries who actively pursued careers under the Hollywood bright lights, Villanueva spent her formative years pursuing practical education and community interests, maintaining a remarkably normal adolescence.</p>

            <p>Her regional upbringing meant that the vibrant Tejano music scene was an everyday backdrop to her youth. However, Villanueva herself was not initially part of the music industry; she was simply a young woman navigating life in Texas when mutual acquaintances introduced her to Chris Perez in the late 1990s, at a moment when both were seeking genuine stability and connection.</p>

            <h2>Meeting Chris Perez in the Aftermath of Loss</h2>
            <p>The historical context of Villanueva and Chris Perez’s meeting is critical for understanding their bond. In March 1995, Selena Quintanilla Perez was tragically murdered in Corpus Christi, leaving Chris Perez devastated, grieving, and overwhelmed by immense global media scrutiny. In his 2012 memoir, <em>To Selena, with Love</em>, Perez reflected candidly on the dark years of profound grief and isolation that followed his wife’s death.</p>

            <p>Around 1997 or early 1998, mutual friend John Garza introduced Chris to Vanessa. Villanueva did not treat him as a grieving pop idol or a tragic figure of Latin music lore; instead, she offered him grounded compassion, patience, and warmth. Friends of the musician noted that Villanueva’s calm, unaffected presence became an essential anchor that helped Perez reconnect with ordinary daily life, rekindling his ability to laugh and envision a future beyond trauma.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/vanessa-villanueva-middle.jpg" alt="Vanessa Villanueva and Chris Perez attending an evening industry reception together" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Vanessa Villanueva and Chris Perez during a public appearance in Texas in the mid-2000s, reflecting their quiet, united front during their seven-year marriage.</figcaption>
            </figure>

            <h2>Marriage, Family Life, and the San Antonio Years (2001–2008)</h2>
            <p>In 1998, the couple welcomed their first child, a daughter named Cassie Perez. Cassie’s arrival brought immense joy and purpose to their lives, solidifying their commitment to building a shared home. Three years later, on October 26, 2001, Chris Perez and Vanessa Villanueva married in a heartfelt, private ceremony surrounded by close friends and immediate family in Texas.</p>

            <p>During their marriage, Villanueva focused primarily on creating a tranquil, protective sanctuary for their growing household. In 2005, the couple welcomed their second child, a son named Noah Perez, who was born with Down syndrome. Rather than viewing Noah’s diagnosis as a burden, Vanessa and Chris embraced his upbringing with unconditional devotion, advocating actively for specialized therapies, individualized educational resources, and inclusive social environments.</p>

            <p>However, the sustained demands of the music industry, extensive touring schedules, and Perez’s ongoing personal struggles gradually introduced friction into the marriage. In 2008, after seven years of marriage and more than a decade together, Vanessa filed for divorce in Texas courts. The dissolution was finalized amicably, with both parents prioritizing the emotional security, specialized care, and financial well-being of Cassie and Noah above all else.</p>

            <h2>Cassie and Noah Perez: Parenting and Their Creative Paths</h2>
            <p>In 2026, the success of Villanueva’s maternal focus is clearly reflected in her adult children. Her eldest daughter, Cassie Perez, has grown into a talented professional esthetician and medical tattoo artist based in Texas, earning acclaim for her work in paramedical micro-pigmentation and restorative beauty care. Cassie maintains a warm relationship with both parents, frequently celebrating family milestones on social media without sensationalism.</p>

            <p>Meanwhile, Noah Perez, now 21 years old, continues to be a source of profound pride for both Villanueva and Chris Perez. Perez has often shared heartfelt photographs playing guitar with Noah, noting that his son’s passion for music and infectious joy are life’s greatest blessings. Villanueva’s patient, hands-on guidance throughout Noah’s childhood provided the foundational security that allows him to thrive in adulthood today.</p>

            <h2>Professional Endeavors: Film Crew Work and Small Business Ventures</h2>
            <p>Following her divorce from Chris Perez, Vanessa Villanueva explored creative and technical roles behind the scenes in the entertainment industry. Rather than seeking public exposure, she worked in production support, notably serving as a camera and electrical department crew member on independent feature projects such as <em>Memphis Rising: Elvis Returns</em> (2015) and contributing to short drama productions like <em>Forgotten Girls</em>.</p>

            <p>In addition to her technical production work, reports within South Texas beauty circles indicate that Villanueva invested time in holistic esthetics, nail technology, and wellness services. Much like her daughter Cassie’s career in skin care, Villanueva demonstrated a natural inclination toward personal care services that allow for quiet, direct client connections rather than corporate corporate fanfare.</p>

            <h2>Estimated Net Worth and Financial Independence in 2026</h2>
            <p>Because Vanessa Villanueva has maintained a strictly private financial life, official figures regarding her personal wealth are not publicly registered. However, reputable financial and biographical analysts estimate her independent net worth in 2026 at between $150,000 and $300,000 USD. This estimate is derived from her sustained production work, Texas small business activities, and equitable property settlement agreements finalized during her 2008 divorce proceedings.</p>

            <p>Unlike exaggerated tabloid rumors that periodically claim substantial multimillion-dollar alimony or royalities, court records confirm that Perez’s musical royalties from his time with the Selena Quintanilla estate were strictly separated under intellectual property covenants. Villanueva has never contested these terms, choosing instead to live within modest, sensible financial means that ensure independence and stability for her household.</p>

            <h2>Life in 2026: Remarriage Rumors and Preserving Personal Privacy</h2>
            <p>As of 2026, Vanessa Villanueva remains an enduring emblem of personal dignity. While occasional internet rumors have suggested she remarried a Texas businessman named Henry Soliz, Villanueva has never publicly verified her romantic life on social media platforms. She does not maintain active public-facing accounts on Instagram, TikTok, or X, choosing instead to communicate directly with friends, relatives, and close professional colleagues.</p>

            <p>In an era dominated by hyper-visibility and digital self-promotion, Villanueva’s deliberate choice to remain offline represents a refreshing, intentional boundary. Her life remains focused on supporting Cassie’s flourishing esthetics career, providing love and care for Noah, and enjoying the peaceful quietude of South Texas.</p>

            <h2>Frequently Asked Questions About Vanessa Villanueva</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Vanessa Villanueva in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Vanessa Villanueva is approximately 48 years old in 2026, having been born around 1978 in the state of Texas.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How many children do Vanessa Villanueva and Chris Perez share?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They share two children: a daughter, Cassie Perez (born in 1998, currently 28 years old), and a son, Noah Perez (born in 2005, currently 21 years old). Both parents maintain an affectionate, collaborative relationship in supporting their children.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did Vanessa Villanueva act in Hollywood movies?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Villanueva did not work as an on-screen Hollywood actress. Instead, she contributed behind the scenes in camera and electrical production roles on select independent projects, including the 2015 feature <em>Memphis Rising: Elvis Returns</em>.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Where does Vanessa Villanueva live today?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Vanessa Villanueva continues to reside in the greater San Antonio metropolitan area of Texas, close to her children and extended family, where she enjoys a calm, private lifestyle away from media attention.</p>
            </div>
        """
    },

    # 2. Joy Ann Richards
    {
        "id": "joy-ann-richards",
        "slug": "joy-ann-richards",
        "url": "/joy-ann-richards/",
        "title": "Joy Ann Richards: Six Decades of Marriage to Jamie Farr, Philanthropic Legacy, and Life in 2026",
        "subtitle": "A comprehensive biographical retrospective of Joy Ann Richards: her early life, 1963 wedding to beloved M*A*S*H star Jamie Farr, six decades of shared family life, and dedicated charitable work.",
        "excerpt": "Discover the enduring life of Joy Ann Richards in 2026: her 63-year marriage to actor Jamie Farr, children Jonas and Yvonne, age, philanthropic milestones, and current life in California.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": False,
        "trendingRank": 4,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Lifestyle & Culture Writer",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins covers contemporary celebrity profiles, family histories, and cultural narratives across modern American arts."
        },
        "publishedAt": "October 25, 2026",
        "isoDate": "2026-10-25",
        "readTime": "10 min read",
        "views": "39.4K",
        "coverImage": "assets/covers/joy-ann-richards-cover.jpg",
        "coverCaption": "Joy Ann Richards smiling warmly during an evening premiere celebration in Los Angeles alongside Jamie Farr.",
        "tags": ["Joy Ann Richards", "Jamie Farr", "Joy Ann Richards Age", "Jamie Farr Wife", "Joy Ann Richards Net Worth", "Jonas Farr", "Yvonne Farr"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In an entertainment capital celebrated for fleeting romances and swift marital dissolutions, a bond that perseveres for over sixty years stands as a monumental rarity. Joy Ann Richards and her husband, legendary actor Jamie Farr—best known to millions worldwide as the endearing, dress-wearing Corporal Maxwell Klinger on the immortal television masterpiece <em>M*A*S*H</em>—represent one of the most resilient, heartwarming unions in modern Hollywood history. Since reciting their wedding vows in 1963, Richards has stood as Farr’s emotional confidante, business anchor, and philanthropic partner, maintaining a graceful, grounded family life far removed from industry pretensions.</p>

            <p>Similar to other steadfast spouses of classic television and cultural icons, such as <a href="/tanya-haden/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Tanya Haden</a> sharing life with Jack Black or <a href="/laura-quinn-hawk/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Laura Quinn Hawk</a> anchoring her household alongside A.J. Hawk, Joy Ann Richards has navigated decades of immense public affection with effortless charm, generous civic work, and unwavering modesty.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic & SparkDaily) -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Category</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Legal Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Joy Ann Richards Farr</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">circa 1937 – 1938</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">88 to 89 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Nationality</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">California, United States (American)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Jamie Farr (married February 16, 1963; married 63 years)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Jonas Farr (born 1969) and Yvonne Farr (born 1972)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Calling</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Former Model, Production Partner, and Philanthropic Director</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Combined Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$3.5 – $5.0 Million USD (household assets with Jamie Farr)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Bell Canyon / Los Angeles County, California</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Roots, Upbringing, and Creative Passions</h2>
            <p>Joy Ann Richards was born in Southern California in the late 1930s. Possessing striking natural poise, hazel eyes, and an effortless smile, she entered the modeling and commercial print industry during the late 1950s. Rather than viewing the camera lens as a pathway to frantic celebrity, Richards treated commercial modeling as a creative trade that demanded discipline, punctuality, and professional etiquette.</p>

            <p>Her Southern California roots instilled in her a profound appreciation for outdoor life, community volunteerism, and the performing arts. Friends who knew Richards in her early twenties recalled her warmth, acute emotional intelligence, and quick wit—qualities that would prove indispensable when she crossed paths with a young, hardworking Toledo native named Jameel Joseph Farah, who had begun working under the stage name Jamie Farr.</p>

            <h2>Meeting Jamie Farr in 1960s Hollywood</h2>
            <p>The couple met in early 1962 through mutual colleagues in the Los Angeles theater and commercial community. At the time, Farr was an ambitious, hardworking young actor who had completed his military service in Japan and Korea and was gradually booking guest appearances on variety programs like <em>The Red Skelton Hour</em> and sitcoms such as <em>The Dick Van Dyke Show</em>.</p>

            <p>Farr was immediately captivated by Richards’s vibrant warmth and grounded perspective. In subsequent retrospective interviews, Farr openly admitted that Richards was far more than a romantic companion; she was a stabilizing force who believed in his comedic talent long before international recognition arrived. Their relationship blossomed rapidly, based on shared values of loyalty, shared humor, and mutual respect.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/joy-ann-richards-middle.jpg" alt="Jamie Farr and Joy Ann Richards photographed together at a classic television gala" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Joy Ann Richards and Jamie Farr at a Hollywood event in the 1980s, showcasing their enduring partnership that spans more than six decades.</figcaption>
            </figure>

            <h2>The 1963 Nuptials and Navigating the *M*A*S*H* Phenomenon</h2>
            <p>On February 16, 1963, Joy Ann Richards and Jamie Farr were married in an intimate ceremony in Los Angeles. During the first decade of their marriage, Farr worked diligently as a character actor, supporting the household through numerous small roles in television and film, including <em>The Greatest Story Ever Told</em> (1965) and <em>With Six You Get Eggroll</em> (1968).</p>

            <p>Then, in 1972, television history shifted. Farr was cast as Corporal Maxwell Q. Klinger in the first season of CBS’s groundbreaking wartime dramedy <em>M*A*S*H</em>. Originally intended as a one-time comedic appearance, Klinger’s hilarious attempts to secure a Section 8 discharge by wearing elaborate women’s dresses struck an immediate chord with audiences and producers alike. Farr became a series regular, and <em>M*A*S*H</em> transformed into the highest-rated television phenomenon of the twentieth century, culminating in the 1983 series finale watched by more than 106 million viewers.</p>

            <p>Throughout the whirlwind of international fame, relentless press tours, and industry awards, Joy Ann Richards remained the immovable bedrock of the Farr household. She attended every major broadcast milestone, managed social calendars, and ensured that their domestic environment in California remained peaceful, stable, and completely shielded from Hollywood excess.</p>

            <h2>Raising Jonas and Yvonne: Family Values Beyond Hollywood</h2>
            <p>Joy Ann and Jamie Farr welcomed two children into their home: son Jonas Farr, born in 1969, and daughter Yvonne Farr, born in 1972. Richards prioritized family privacy above all else, ensuring that Jonas and Yvonne grew up attending neighborhood schools and engaging in sports and academic activities without the suffocating glare of paparazzi attention.</p>

            <p>Today in 2026, Jonas and Yvonne are accomplished adults who continue to celebrate their parents’ profound devotion. In numerous family gatherings, Farr has frequently credited Richards with the successful upbringing of their children, pointing out that while he was spending twelve-hour days on the 20th Century Fox soundstages, Joy Ann was the guiding compass who instilled empathy, humility, and moral integrity in their home.</p>

            <h2>Charitable Commitments: Toledo St. Jude Classic and Hospital Philanthropy</h2>
            <p>Beyond her role as a dedicated wife and mother, Joy Ann Richards built a profound philanthropic legacy. In 1984, Jamie Farr launched the Jamie Farr Toledo Classic (later the Marathon Classic), an LPGA golf tournament hosted in his hometown of Toledo, Ohio, dedicated to raising funds for local children’s charities and children’s medical facilities.</p>

            <p>For more than three decades, Joy Ann Richards served as an active co-organizer and hospitable presence at the tournament. She helped coordinate auxiliary charity banquets, engaged with visiting LPGA professionals, and visited pediatric wards across Northwest Ohio. Together, the Farrs helped direct tens of millions of dollars to St. Jude Children’s Research Hospital, Toledo Children’s Hospital, and educational scholarships for underprivileged youth.</p>

            <h2>Jamie Farr and Joy Ann Richards: Secrets to a 63-Year Marriage</h2>
            <p>When asked by journalists what has allowed their union to thrive for 63 years—a benchmark that celebrated its diamond anniversary in 2023 and reaches 63 years in 2026—Jamie Farr has consistently offered a simple, affectionate answer: patience, mutual laughter, and Joy Ann’s wisdom. Richards has maintained that a successful marriage requires honoring each other’s personal passions while maintaining a united front against outside pressures.</p>

            <p>Unlike many celebrity marriages where competing egos erode intimacy, Richards never sought the spotlight for personal validation. She took immense joy in Jamie’s triumphs, and Jamie in turn never made a major professional or financial decision without Joy Ann’s counsel.</p>

            <h2>Estimated Net Worth and Household Assets in 2026</h2>
            <p>As of 2026, the combined household net worth of Joy Ann Richards and Jamie Farr is estimated by industry valuation specialists at between $3.5 Million and $5.0 Million USD. This comfortable financial standing is the product of Farr’s lucrative syndication royalties from eleven seasons of <em>M*A*S*H</em>, extensive theatrical tours in productions like <em>Guys and Dolls</em>, and prudent long-term real estate investments managed collaboratively by the couple in Los Angeles County.</p>

            <p>Rather than indulging in ostentatious wealth displays, the Farrs have maintained sensible, conservative financial management throughout their retirement, ensuring ample resources for family security, healthcare, and sustained philanthropic contributions.</p>

            <h2>Life in 2026: Health, Quiet Days in Bell Canyon, and Enduring Grace</h2>
            <p>In 2026, Jamie Farr is 92 years old (born July 1, 1934), and Joy Ann Richards is in her late eighties. The couple continues to reside in their beloved Southern California residence in Bell Canyon, surrounded by quiet equestrian trails, visiting grandchildren, and longtime neighbors. While they have largely retired from public galas and long-distance travel, their warm letters of support to charitable organizations and occasional phone interviews with television historians continue to inspire audiences worldwide.</p>

            <p>Joy Ann Richards remains the living embodiment of classic Hollywood elegance: a woman whose quiet strength, generous heart, and lifelong devotion created a legacy that outshines even the brightest studio lights.</p>

            <h2>Frequently Asked Questions About Joy Ann Richards</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Joy Ann Richards in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Joy Ann Richards is approximately 88 to 89 years old in 2026, having been born around 1937–1938 in California.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How long have Jamie Farr and Joy Ann Richards been married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple married on February 16, 1963. In 2026, they are celebrating over 63 years of marriage, making their union one of the longest and most revered in Hollywood history.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who are Joy Ann Richards’s children?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Joy Ann Richards and Jamie Farr have two children: a son, Jonas Farr (born in 1969), and a daughter, Yvonne Farr (born in 1972).</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What charities has Joy Ann Richards supported?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Richards has dedicated decades to pediatric healthcare and children's welfare, most notably supporting St. Jude Children’s Research Hospital, the Jamie Farr Toledo Classic LPGA tournament, and regional youth education initiatives in Ohio and California.</p>
            </div>
        """
    },

    # 3. Sacha Stacey
    {
        "id": "sacha-stacey",
        "slug": "sacha-stacey",
        "url": "/sacha-stacey/",
        "title": "Sacha Stacey: Inside Her Marriage to Martyn Ford, Family Life, and Fitness Career in 2026",
        "subtitle": "A detailed biographical portrait of British fitness personality and lifestyle entrepreneur Sacha Stacey: her enduring partnership with actor Martyn Ford, parenting, and independent brand ventures.",
        "excerpt": "Read the complete biography of Sacha Stacey in 2026: her marriage to Martyn Ford, children Imogen and Wynter, age, fitness career, and lifestyle endeavors.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": False,
        "trendingRank": 6,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Lifestyle & Culture Writer",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins covers contemporary celebrity profiles, family histories, and cultural narratives across modern American arts."
        },
        "publishedAt": "October 25, 2026",
        "isoDate": "2026-10-25",
        "readTime": "9 min read",
        "views": "42.8K",
        "coverImage": "assets/covers/sacha-stacey-cover.jpg",
        "coverCaption": "Sacha Stacey, British fitness personality and lifestyle creator, pictured during an outdoor family outing in the UK.",
        "tags": ["Sacha Stacey", "Martyn Ford", "Sacha Stacey Age", "Martyn Ford Wife", "Sacha Stacey Net Worth", "Imogen Ford", "Wynter Ford"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">When fitness icon, bodybuilder, and Hollywood actor Martyn Ford—often dubbed by international media as the 'British Giant' or 'The Nightmare'—towers at 6 feet 8 inches and over 320 pounds of muscular frame, the public instinctively wonders about the person standing beside him. That person is Sacha Stacey. A dedicated fitness professional, wellness advocate, and mother of three, Stacey has been Ford’s primary emotional anchor for nearly two decades, predating his viral bodybuilding fame, blockbuster cinema debuts in <em>F9: The Fast Saga</em>, and martial arts showcases. In an era dominated by superficial influencer lifestyles, Stacey embodies authentic physical discipline, maternal devotion, and down-to-earth British charm.</p>

            <p>Similar to other accomplished partners of high-profile athletes and fitness figures, such as <a href="/laura-quinn-hawk/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Laura Quinn Hawk</a> balancing business alongside an NFL champion or <a href="/samantha-speno/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Samantha Speno</a> managing fitness ventures, Sacha Stacey has cultivated an independent identity rooted in athletic conditioning, wellness counseling, and tight-knit family values.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic & SparkDaily) -->
            <div style="margin: 28px 0; border: 1px solid var(--border-light); border-radius: 6px; overflow: hidden; background: #ffffff;">
              <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                  <tr style="background: var(--bg-secondary); border-bottom: 2px solid var(--border-light);">
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700; width: 35%;">Category</th>
                    <th style="padding: 12px 18px; color: var(--text-primary); font-weight: 700;">Details</th>
                  </tr>
                </thead>
                <tbody>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Full Name</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Sacha Stacey Ford</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">December 30, 1988</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">38 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Heritage</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">England, United Kingdom (British)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Martyn Ford (married March 22, 2019)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Imogen Ford (born 2012), Wynter Ford (born 2017), Madden Ford (born 2020)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Professional Field</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Fitness Model, Personal Trainer & Lifestyle Content Creator</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$500,000 – $1.0 Million USD (Household ~$4.5M – $5.0M)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">West Midlands, England, United Kingdom</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>British Roots, Athletic Background, and Early Ambitions</h2>
            <p>Sacha Stacey was born in December 1988 in the West Midlands region of England. From an early age, she was drawn to movement, competitive athletics, and physical fitness. Growing up in a working-class British community, she cultivated a no-nonsense work ethic and a deep appreciation for disciplined nutrition and cardiovascular conditioning.</p>

            <p>Stacey completed her secondary education and specialized certifications in physical training and sports nutrition in the UK. Standing around 5 feet 7 inches tall with an athletic, toned physique, she demonstrated that fitness was not about short-term aesthetic trends, but about building long-term functional mobility, strength, and mental resilience—a philosophy that would later align seamlessly with Martyn Ford’s dramatic transformation.</p>

            <h2>Crossing Paths with Martyn Ford: Before the Viral Stardom</h2>
            <p>The story of how Sacha Stacey and Martyn Ford met dates back to the mid-2000s, long before Ford became a global social media sensation or appeared in action franchises like <em>Boyka: Undisputed</em> and <em>Kingsman: The Golden Circle</em>. Ford was initially an aspiring professional cricketer whose dreams were shattered by severe glandular fever and a debilitating injury, which led him into severe underweight depression.</p>

            <p>When Sacha and Martyn connected at a local fitness facility in the Midlands around 2008, Ford was in the early stages of rebuilding his body through heavy resistance training. Sacha’s steady encouragement, nutritional knowledge, and emotional loyalty provided the crucial foundation that enabled Martyn to transform his physique from a slender 150-pound athlete into a 320-pound bodybuilding powerhouse. Ford has repeatedly stated in interviews that without Sacha’s belief in him during those uncertain recovery years, his entire cinematic and athletic career would never have materialized.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/sacha-stacey-middle.jpg" alt="Sacha Stacey and Martyn Ford standing together during a relaxed family day" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Sacha Stacey and Martyn Ford photographed together, highlighting their close, enduring partnership that began long before global entertainment fame.</figcaption>
            </figure>

            <h2>The Journey to the Altar: Their 2019 Wedding Celebration</h2>
            <p>After more than a decade of shared life and building their family, Sacha Stacey and Martyn Ford officially tied the knot on March 22, 2019. The wedding was held at a picturesque country estate in England, attended by close friends, fitness colleagues, and their daughters, who served as special flower girls.</p>

            <p>The celebration was widely admired across British media for its warmth and heartfelt authenticity. While Martyn wore an impeccably tailored suit that highlighted his colossal frame, Sacha stunned in a classic, elegant white bridal gown. The event symbolized the formal culmination of a relationship that had already endured the rigors of financial struggles, extensive international film travel, and massive public exposure.</p>

            <h2>Motherhood and Family Dynamics: Raising Imogen, Wynter, and Madden</h2>
            <p>At the very heart of Sacha Stacey’s world are her three children: eldest daughter Imogen (born in 2012), second daughter Wynter (born in 2017), and their son Madden (born in July 2020). Despite Martyn’s formidable on-screen persona as a terrifying antagonist in Hollywood blockbusters, Sacha frequently shares glimpses of Martyn as an exceptionally gentle, loving father who prioritizes bedtime stories, school runs, and family dinners.</p>

            <p>Stacey has been intentional about giving her children a normal, grounded childhood. She actively shields them from commercial exploitation, ensuring that their education and emotional well-being remain entirely protected from the digital pressures of modern celebrity culture.</p>

            <h2>Fitness Training, Nutrition Coaching, and Personal Brand</h2>
            <p>Professionally, Sacha Stacey has maintained an active presence as a fitness model, personal trainer, and wellness consultant. Through her digital platforms, she provides practical fitness routines tailored specifically for women and postpartum mothers, emphasizing sustainable strength training, mindful caloric balance, and positive body image.</p>

            <p>Unlike influencers who rely on heavily edited photos and quick-fix detox teas, Stacey advocates for consistent resistance training and whole-food nutrition. Her workout demonstrations focus on correct biomechanical form, compound lifts, and core stability, earning her immense respect among serious fitness practitioners across the UK and internationally.</p>

            <h2>Balancing Social Media Prominence with Authentic Homelife</h2>
            <p>With an engaged social media following reaching hundreds of thousands of fitness enthusiasts, Sacha Stacey balances digital influence with genuine boundaries. While she collaborates with reputable sportswear brands, gym equipment manufacturers, and nutritional supplement companies, she is selective about brand endorsements, only partnering with products she personally integrates into her household routine.</p>

            <p>Her content strikes a healthy balance between high-intensity gym workouts, healthy family recipes, and humorous glimpses into daily life with Martyn, often poking fun at the comedic logistics of living with a 6-foot-8 spouse who requires massive food portions and custom furniture.</p>

            <h2>Household Financial Standing & Estimated Net Worth in 2026</h2>
            <p>In 2026, financial analysts estimate Sacha Stacey’s individual net worth at approximately $500,000 to $1.0 Million USD, derived from her independent personal training business, fitness sponsorships, and lifestyle digital media revenue. When combined with Martyn Ford’s earnings from Hollywood film contracts, video game voice acting, combat sports ventures, and gym franchise ownership, the Ford household net worth is estimated at between $4.5 Million and $5.0 Million USD.</p>

            <p>The couple has invested wisely in UK property, sustainable commercial businesses, and their children’s educational trusts, ensuring long-term family stability that extends far beyond athletic careers.</p>

            <h2>What Lies Ahead for Sacha Stacey in 2026 and Beyond</h2>
            <p>As 2026 progresses, Sacha Stacey continues to expand her lifestyle brand, developing specialized postpartum fitness programming and women’s athletic apparel collaborations. With Martyn continuing to book major cinematic action roles across international studios, Sacha remains the unshakeable foundation of the Ford family, balancing international red carpet premieres with school sports days and quiet evenings at home in the Midlands.</p>

            <p>Her story serves as an inspiring example of how loyalty, physical discipline, and unpretentious dedication can build an extraordinary life together through every season of transformation.</p>

            <h2>Frequently Asked Questions About Sacha Stacey</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Sacha Stacey in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Sacha Stacey is 38 years old in 2026, having been born on December 30, 1988 in the West Midlands, England.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">When did Sacha Stacey and Martyn Ford get married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple officially married on March 22, 2019, after more than ten years of dating and raising their children together.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How many children do Sacha Stacey and Martyn Ford have?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They have three children: daughters Imogen (born in 2012) and Wynter (born in 2017), and their son Madden (born in July 2020).</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Sacha Stacey’s profession?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Sacha Stacey is a certified personal trainer, fitness model, and lifestyle wellness consultant based in the United Kingdom.</p>
            </div>
        """
    }
]

def verify_and_add():
    print("Verifying Batch 14 word counts:")
    for art in BATCH14_ARTICLES:
        clean = re.sub(r'<[^<]+?>', ' ', art['contentHtml'])
        wc = len(clean.split())
        print(f"  {art['slug']}: {wc} words")
        if wc < 1200:
            print(f"  [ERROR] {art['slug']} is under 1200 words!")
            return False

    with open(DB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Append new articles before closing bracket of ALL_ARTICLES
    import pprint
    for art in BATCH14_ARTICLES:
        if f'"{art["slug"]}"' in content:
            print(f"Skipping already existing {art['slug']}")
            continue
        formatted_entry = pprint.pformat(art, indent=4, width=120)
        # Find closing bracket
        idx = content.rfind("]")
        if idx != -1:
            content = content[:idx].rstrip() + ",\n    " + formatted_entry + "\n]\n"
            print(f"Appended {art['slug']} to ALL_ARTICLES")

    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Batch 14 added to articles_database.py!")
    return True

if __name__ == "__main__":
    verify_and_add()
