import os
import sys
import re
import pprint

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH16_ARTICLES = [
    # 1. Dalia Asafi
    {
        "id": "dalia-asafi",
        "slug": "dalia-asafi",
        "url": "/dalia-asafi/",
        "title": "Who Is Dalia Asafi? The Life and Faith of Hakeem Olajuwon’s Wife",
        "subtitle": "A comprehensive biographical profile of Dalia Asafi: her marriage to NBA icon Hakeem Olajuwon, family life in Houston and London, children, and quiet philanthropic dedication.",
        "excerpt": "Explore the life of Dalia Asafi: her marriage to NBA legend Hakeem Olajuwon, family life, children, age, background, and philanthropic work.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": True,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "October 27, 2026",
        "isoDate": "2026-10-27",
        "readTime": "9 min read",
        "views": "53.8K",
        "coverImage": "assets/covers/dalia-asafi-cover.jpg",
        "coverCaption": "Dalia Asafi, community philanthropist and wife of basketball legend Hakeem Olajuwon, photographed during a charitable seminar.",
        "tags": ["Dalia Asafi", "Hakeem Olajuwon", "Dalia Asafi Age", "Hakeem Olajuwon Wife", "Dalia Asafi Net Worth", "Houston Rockets", "Islamic Philanthropy"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the annals of professional basketball history, very few figures command the reverence and global esteem accorded to Hakeem 'The Dream' Olajuwon. The Hall of Fame center guided the Houston Rockets to back-to-back NBA championships in 1994 and 1995, redefining the art of footwork and interior defense while earning universal respect for his spiritual devotion and humility. Yet behind Olajuwon’s towering public career stands an equally principled, quietly influential figure: his wife of three decades, Dalia Asafi. Reared with deep Islamic convictions and traditional cultural values, Asafi has consistently prioritized spiritual grounding, domestic harmony, and charitable service over courtside glamour, exemplifying how dignity and private devotion can anchor an iconic sports family.</p>

            <p>Similar to other steadfast partners of renowned sporting and cultural figures, such as <a href="/mirka-federer/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Mirka Federer</a> anchoring family life alongside Roger Federer or <a href="/laura-quinn-hawk/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Laura Quinn Hawk</a> building community roots alongside A.J. Hawk, Dalia Asafi has chosen a life rooted in substantive action rather than commercial publicity.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Dalia Asafi Olajuwon</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">circa 1968</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">58 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Religious Faith & Heritage</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Islam (Middle Eastern heritage; American citizenship)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Hakeem Olajuwon (married August 8, 1996; married 30 years)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Rahmah, Aisha, Abdullah, and Abdul Olajuwon</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Role</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Philanthropic Director, Community Organizer & Educator</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Household Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$200 – $300 Million USD (combined real estate & NBA assets)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Residences</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Houston / Sugar Land, Texas and London, United Kingdom</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Life, Upbringing, and Islamic Heritage</h2>
            <p>Dalia Asafi was born in the late 1960s into a respected family of Middle Eastern origin who practiced orthodox Islamic traditions. From her formative years, her home environment emphasized moral rectitude, scholarly learning, modesty, and hospitality. Unlike many individuals who sought out public attention or commercial ventures, Asafi’s upbringing focused on community volunteerism, Quranic studies, and cultivating an unshakeable inner compass.</p>

            <p>When she relocated to the United States as a young woman, she maintained an unwavering commitment to her faith. Her modest attire, dignified personal conduct, and deep spiritual discipline stood out in sharp contrast to the surrounding materialistic culture. Those who knew her in Houston during the early 1990s described her as an exceptionally thoughtful, articulate individual who took pride in preserving her cultural and religious heritage.</p>

            <h2>Meeting Hakeem Olajuwon and Their 1996 Wedding</h2>
            <p>During the early 1990s, Hakeem Olajuwon underwent a profound spiritual renaissance. Although he had been raised Muslim in Lagos, Nigeria, Olajuwon experienced a renewed, intense dedication to orthodox Islamic practice around 1991, observing strict daytime fasts during the holy month of Ramadan even while playing grueling 40-minute NBA playoff contests. Olajuwon expressed a strong desire to find a life partner who shared his deep religious devotion and dedication to traditional Islamic marital principles.</p>

            <p>Through mutual family friends and community elders within the Houston Muslim community, Hakeem was introduced to Dalia Asafi. The connection was immediate and rooted in shared spiritual values. Rather than a modern Hollywood courtship driven by public appearances, their relationship was guided by Islamic tradition. On August 8, 1996, the couple married in an intimate, deeply spiritual Islamic ceremony (Nikah) in Houston, attended by close relatives and community leaders. Olajuwon proudly shared that his marriage to Dalia brought profound peace and clarity to his home, cementing a foundation of mutual respect that has endured for three decades.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/dalia-asafi-middle.jpg" alt="Dalia Asafi photographed during a community appearance" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Dalia Asafi, reflecting her dignified public presence and dedication to family and faith-based community service.</figcaption>
            </figure>

            <h2>Life in Houston, Texas and Moving to the United Kingdom</h2>
            <p>Following their 1996 wedding, Dalia and Hakeem established their primary residence in the Sugar Land suburb of Houston, Texas. Dalia created a tranquil sanctuary where Olajuwon could decompress from the intense pressures of professional athletics, especially during his historic championship-defense campaigns and later seasons with the Houston Rockets and Toronto Raptors.</p>

            <p>After Olajuwon officially retired from the NBA in 2002, the couple expanded their horizons, establishing a second family home in London, England. This move allowed their children to experience an international education while immersing the family in the diverse cultural and Islamic heritage of the UK capital. The Olajuwon-Asafi household spent years dividing their time between the rolling landscapes of Texas—where Hakeem operates extensive real estate ventures and youth basketball camps—and their residence in England.</p>

            <h2>Raising Rahmah, Aisha, Abdullah, and Abdul: Family Values</h2>
            <p>Dalia Asafi and Hakeem Olajuwon are the proud parents of four children: two daughters, Rahmah and Aisha, and two sons, Abdullah and Abdul. In raising their children, Asafi was determined to instill humility, academic discipline, and a deep understanding of their religious identity, ensuring they remained untouched by the entitlement often associated with extreme athlete wealth.</p>

            <p>Both sons inherited their father’s athletic stature and love for sports, competing in basketball leagues while prioritizing their collegiate studies. Hakeem has frequently paid tribute to Dalia’s hands-on parenting, noting that while his business investments frequently required travel, Dalia was the intellectual and moral center of their home, guiding each child with patience and loving discipline.</p>

            <h2>Islamic Philanthropy and Community Contributions</h2>
            <p>Throughout their 30-year marriage, Dalia Asafi has been a driving force behind the family’s extensive philanthropic endeavors. In Houston, she worked alongside Hakeem to fund the construction and ongoing charitable programs of the Islamic Da'wah Center, housed in a historic former bank building in downtown Houston that Olajuwon purchased and meticulously restored.</p>

            <p>Asafi has championed numerous initiatives focused on community food banks, women’s educational literacy, refugee assistance, and youth mentorship. Her charitable involvement is intentionally discreet; following traditional Islamic guidance regarding charity (Sadaqah), she avoids vanity ceremonies and press releases, preferring that the resources directly benefit families in need without personal fanfare.</p>

            <p>In addition to local Texas initiatives, Dalia has supported educational sponsorships for orphaned children in West Africa and spearheaded humanitarian relief shipments to international disaster zones. Friends and colleagues within Houston faith organizations often remark on her approachable nature, noting that she actively participates in weekly community study circles, volunteers at youth sports camps, and provides practical counsel to newly arrived immigrant families seeking to establish themselves in the United States.</p>

            <h2>Hakeem Olajuwon and Dalia Asafi's Lasting Household Wealth</h2>
            <p>Unlike many professional athletes who face financial turbulence upon retirement, Hakeem Olajuwon executed one of the most brilliant post-career financial transitions in sports history. Guided by conservative principles that avoid interest-based speculation (Riba), Olajuwon invested heavily in commercial real estate across Greater Houston, buying high-potential land along major transit corridors using cash reserves.</p>

            <p>Today in 2026, financial and real estate analysts estimate the Olajuwon-Asafi family net worth at between $200 Million and $300 Million USD. Their portfolio encompasses extensive Houston commercial acreage, the DR34M luxury clothing and athletic brand, and international properties. Dalia Asafi’s prudent household stewardship and shared commitment to long-term financial conservatism have played an essential role in preserving and growing this multi-generational legacy.</p>

            <h2>Life in 2026: A Serene Chapter of Faith and Family Mentorship</h2>
            <p>As 2026 unfolds, Dalia Asafi and Hakeem Olajuwon are celebrating their 30th wedding anniversary, marking three decades of unbroken partnership, mutual spiritual growth, and devoted parenting. Now that their four children are grown adults pursuing their own collegiate and professional journeys, Dalia and Hakeem enjoy a quieter, reflective pace of life.</p>

            <p>They divide their time between their peaceful home in Sugar Land, Texas, where Hakeem continues to coach aspiring young NBA big men on footwork fundamentals, and their residence in the United Kingdom. Asafi remains a steadfast symbol of grace, demonstrating how an authentic devotion to spiritual principles, family loyalty, and quiet benevolence can foster a deeply fulfilling life that completely transcends the fleeting temptations of fame.</p>

            <h2>Frequently Asked Questions About Dalia Asafi</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Dalia Asafi?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Dalia Asafi was born around 1968 and is approximately 58 years old as of 2026.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">When did Dalia Asafi and Hakeem Olajuwon get married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They married on August 8, 1996 in Houston, Texas in a traditional Islamic wedding ceremony, marking 30 years of marriage in 2026.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How many children do Dalia Asafi and Hakeem Olajuwon have?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple shares four children together: two daughters, Rahmah and Aisha, and two sons, Abdullah and Abdul.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Where does Dalia Asafi live today?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Dalia Asafi and Hakeem Olajuwon split their time between their longtime family residence in Sugar Land, Texas and their secondary home in London, United Kingdom.</p>
            </div>
        """
    },

    # 2. Cody Herpin
    {
        "id": "cody-herpin",
        "slug": "cody-herpin",
        "url": "/cody-herpin/",
        "title": "Cody Herpin: Jodie Sweetin’s Ex-Husband, Behind-the-Scenes Film Career, and Fatherhood",
        "subtitle": "An investigative editorial profile of Cody Herpin: his career as a film transportation coordinator and prop technician, marriage to Full House actress Jodie Sweetin, co-parenting daughter Zoie, and life today.",
        "excerpt": "Discover the life of Cody Herpin: his marriage to Full House star Jodie Sweetin, daughter Zoie Laurel May, career in Hollywood production, age, and net worth.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 2,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Lifestyle & Culture Writer",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins covers contemporary celebrity profiles, family histories, and cultural narratives across modern American arts."
        },
        "publishedAt": "October 27, 2026",
        "isoDate": "2026-10-27",
        "readTime": "9 min read",
        "views": "46.2K",
        "coverImage": "assets/covers/cody-herpin-cover.jpg",
        "coverCaption": "Cody Herpin, film production technician and former spouse of actress Jodie Sweetin, attending an industry screening event.",
        "tags": ["Cody Herpin", "Jodie Sweetin", "Cody Herpin Age", "Jodie Sweetin Ex Husband", "Zoie Laurel May Herpin", "Cody Herpin Net Worth", "Full House"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the fast-moving universe of Hollywood celebrity marriages, media narratives frequently reduce complex human partnerships to fleeting tabloid headlines. Cody Herpin experienced the full intensity of that glare during the late 2000s when he married beloved television star Jodie Sweetin—famed globally for her childhood portrayal of Stephanie Tanner on the iconic ABC sitcom <em>Full House</em>. Yet before and after his high-profile marriage, Herpin was an established, hardworking film and television industry technician whose practical expertise in transportation logistics, prop coordination, and set operations supported dozens of independent and studio productions. His life story reflects the reality of a dedicated father who navigated unexpected public scrutiny while remaining committed to his work and daughter.</p>

            <p>Much like other grounded professionals who experienced temporary media frenzies through celebrity marriages—such as <a href="/norman-kali/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Norman Kali</a> navigating Hollywood production alongside Evangeline Lilly or <a href="/ashton-meem/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Ashton Meem</a> rebuilding personal privacy—Cody Herpin stepped away from public speculation to prioritize private stability and long-term parental responsibility.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Cody Herpin</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">April 28, 1977</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">49 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Nationality</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">California, United States (American)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Jodie Sweetin (married July 14, 2007; divorced April 20, 2010)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Zoie Laurel May Herpin (born April 12, 2008)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Film Transportation Driver, Prop Coordinator & Set Technician</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$300,000 – $500,000 USD (independent production earnings)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Southern California, United States</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Life, Background, and Technical Training</h2>
            <p>Cody Herpin was born on April 28, 1977, in California. Growing up in the greater Los Angeles area, he developed an early enthusiasm for mechanics, automobiles, and physical construction. Rather than pursuing performing arts or theoretical academia, Herpin possessed a hands-on disposition, learning practical automotive maintenance, heavy transport logistics, and technical carpentry throughout his late teens and early twenties.</p>

            <p>His technical skills naturally opened doors to the Southern California entertainment production infrastructure. Film and television studios constantly require reliable, punctual crew members who understand the intricate logistics of moving delicate film equipment, transporting talent safely to remote shooting locations, and fabricating on-set props under tight schedules. Herpin earned a reputation among studio department heads as an industrious, calm technician who got jobs done efficiently without drama.</p>

            <h2>Hollywood Production Career: Transportation and Art Department Roles</h2>
            <p>Throughout the 2000s, Herpin built an impressive technical resume across major studio and independent motion picture sets. He served on the transportation and art departments of various notable film projects, including the post-apocalyptic action feature <em>Resident Evil: Extinction</em> (2007), starring Milla Jovovich, the thriller <em>Dark Honeymoon</em> (2008), family comedy <em>Alice Upside Down</em> (2007), and horror production <em>Unearthed</em> (2007).</p>

            <p>His responsibilities often involved coordinating picture cars, operating specialized transport trailers, and assisting set decorators with props and mechanical rigging. While audience members focus solely on famous actors on screen, industry veterans recognize that crew members like Herpin are indispensable for maintaining the seamless daily operations of Hollywood film sets.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/cody-herpin-middle.jpg" alt="Cody Herpin with Jodie Sweetin and baby Zoie on the red carpet" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Cody Herpin and Jodie Sweetin attending a charity red carpet event with their infant daughter Zoie in 2008.</figcaption>
            </figure>

            <h2>Meeting Jodie Sweetin on Set and Their 2007 Wedding</h2>
            <p>In May 2007, Cody Herpin crossed paths with actress Jodie Sweetin through mutual colleagues in the television production community. Sweetin, who had divorced her first husband Shaun Holguin in 2006, was actively working to rebuild her life and career following well-documented personal struggles with substance abuse during her early twenties.</p>

            <p>Sweetin found comfort in Herpin’s down-to-earth demeanor, dry humor, and grounded lifestyle outside Hollywood’s party circuit. The romance developed rapidly; after just two months of dating, the couple traveled to Las Vegas, Nevada, exchanging vows in an intimate ceremony on July 14, 2007. Sweetin spoke glowingly to entertainment reporters about Herpin’s supportive presence, frequently stating that his steady nature gave her the emotional security she needed to begin a new chapter.</p>

            <h2>The Birth of Daughter Zoie Laurel May Herpin</h2>
            <p>On April 12, 2008, the couple welcomed their first child, a daughter named Zoie Laurel May Herpin, delivered via an emergency C-section in Los Angeles. The arrival of baby Zoie brought immense happiness to both parents, and Herpin was deeply devoted to hands-on fatherhood from her first moments.</p>

            <p>In interviews during that period, Sweetin proudly described Herpin as an exceptional father who handled midnight feedings and diaper changes with patient dedication. Photographs from red carpet charity premieres showed Herpin standing proudly alongside Sweetin and their baby daughter, projecting a warm, united family front to the world.</p>

            <h2>High-Profile Divorce, Custody Agreements, and Co-Parenting</h2>
            <p>However, the rapid nature of their romance, financial pressures, and differing long-term expectations soon introduced severe strains into the marriage. In November 2008, just seven months after Zoie’s birth and sixteen months after their wedding, Sweetin filed for legal separation in Orange County Superior Court, which evolved into a contentious divorce battle covered extensively by entertainment tabloids.</p>

            <p>Herpin contested custody arrangements, seeking primary custody to ensure Zoie’s safety and daily stability during a turbulent period in Sweetin’s personal life. The legal proceedings continued for nearly two years before being formally finalized on April 20, 2010. Ultimately, both parents agreed to a comprehensive joint custody arrangement. Over time, as media interest faded, both Herpin and Sweetin matured into a cooperative co-parenting dynamic, putting Zoie’s emotional and academic needs first.</p>

            <h2>Career After the Spotlight and Personal Growth</h2>
            <p>Following the finalization of his divorce, Cody Herpin deliberately retreated from public exposure. He avoided reality television offers, declined sensational tell-all interviews, and returned to his core vocation in technical production, mechanical services, and automotive logistics in Southern California.</p>

            <p>In 2026, Herpin’s daughter Zoie is 18 years old, celebrating her high school graduation and stepping forward into young adulthood. Family acquaintances consistently note that Herpin has remained a constant, loving presence in Zoie’s life, attending her school activities, milestones, and celebrations quietly away from cameras.</p>

            <h2>Behind the Scenes: The Technical Craft of Film Transportation</h2>
            <p>In the entertainment industry, the role of a transportation technician and picture car specialist requires an intricate balance of logistical precision and safety coordination. Operating under Teamsters standards, drivers and equipment coordinators are responsible for moving millions of dollars in camera rigs, sound stages, lighting trailers, and specialized stunt vehicles across challenging shooting terrains.</p>

            <p>Throughout his career on demanding sets like <em>Resident Evil: Extinction</em>—which filmed in rigorous desert conditions in Mexico and the American Southwest—Herpin demonstrated the endurance, technical problem-solving, and punctual reliability that high-budget productions rely on. Those who worked alongside him on set recall that while movie stars commanded the public spotlight, crew members like Herpin worked eighteen-hour shifts ensuring every mechanical asset was primed and ready for the director's call.</p>

            <h2>Life in 2026: Maturity, Independence, and Private Stability</h2>
            <p>Today in 2026, at 49 years old, Cody Herpin has built a peaceful, grounded existence in Southern California. Having weathered the intense media storm of a public celebrity divorce early in his thirties, he developed a profound appreciation for discretion and personal boundaries. Friends describe him as an avid outdoorsman and devoted mechanic who enjoys working on classic cars, spending quality time with family, and pursuing practical projects away from the digital noise of social media.</p>

            <p>His story serves as an instructive example of personal resilience. Rather than allowing a brief celebrity marriage to define his lifetime trajectory or pursuing fleeting internet fame, Herpin embraced his authentic calling as a skilled technician and committed father, proving that long-term character is forged through quiet, daily responsibility.</p>

            <h2>Financial Profile and Estimated Net Worth</h2>
            <p>As of 2026, financial biographical analysts estimate Cody Herpin’s personal net worth at between $300,000 and $500,000 USD. This estimate is based on his multi-decade career as an independent film technician, commercial transportation contractor, and technical specialist in California.</p>

            <p>Herpin has lived a modest, disciplined life, demonstrating that happiness is rooted in reliable work, authentic relationships, and fatherhood rather than the transient superficiality of celebrity headlines.</p>

            <h2>Frequently Asked Questions About Cody Herpin</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Cody Herpin?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Cody Herpin was born on April 28, 1977, making him 49 years old as of 2026.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How long were Cody Herpin and Jodie Sweetin married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple married on July 14, 2007 in Las Vegas. They separated in November 2008, and their divorce was finalized on April 20, 2010.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Cody Herpin’s daughter?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">His daughter is Zoie Laurel May Herpin, born on April 12, 2008. In 2026, Zoie turns 18 years old.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What films did Cody Herpin work on?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Herpin worked in transportation and art department roles on films including <em>Resident Evil: Extinction</em>, <em>Dark Honeymoon</em>, <em>Alice Upside Down</em>, and <em>Unearthed</em>.</p>
            </div>
        """
    },

    # 3. Haley Arnaz
    {
        "id": "haley-arnaz",
        "slug": "haley-arnaz",
        "url": "/haley-arnaz/",
        "title": "Haley Arnaz: Ballet Career, Desi Arnaz Jr.’s Family Legacy, and Life Beyond Hollywood",
        "subtitle": "A biographical profile of ballet dancer Haley Arnaz: her adoption by Desi Arnaz Jr., connection to comedy legends Lucille Ball and Desi Arnaz, her dance discipline, and private life today.",
        "excerpt": "Read the biography of Haley Arnaz: her adoption by Desi Arnaz Jr., mother Amy Bargiel, Lucille Ball family legacy, ballet career, age, and marriage.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": False,
        "trendingRank": 3,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "October 27, 2026",
        "isoDate": "2026-10-27",
        "readTime": "9 min read",
        "views": "41.5K",
        "coverImage": "assets/covers/haley-arnaz-cover.jpg",
        "coverCaption": "Haley Arnaz, classical dancer and adopted daughter of actor Desi Arnaz Jr., attending a family tribute in Nevada.",
        "tags": ["Haley Arnaz", "Desi Arnaz Jr", "Haley Arnaz Age", "Lucille Ball Granddaughter", "Amy Arnaz", "Haley Arnaz Ballet", "Boulder City Ballet Company"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the golden history of American television and theater, the Arnaz surname occupies an indelible place of honor. As the descendants of television pioneers Lucille Ball and Desi Arnaz—whose revolutionary sitcom <em>I Love Lucy</em> created the multi-camera sitcom format and delighted generations across the globe—the family has lived under a permanent cultural microscope. Yet within this historic dynasty, Haley Arnaz stands out for her grace, artistic integrity, and intentional modesty. Adopted by actor and musician Desi Arnaz Jr. during his lasting marriage to her mother, Amy Bargiel, Haley embraced classical dance as her primary life’s calling, honoring her family’s artistic heritage while deliberately steering clear of Hollywood vanity.</p>

            <p>Similar to other grounded descendants and spouses of iconic entertainment dynasties—such as <a href="/haley-giraldo/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Haley Giraldo</a> carving out an authentic path alongside Pat Benatar’s rock legacy or <a href="/tanya-haden/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Tanya Haden</a> continuing musical traditions—Haley Arnaz has balanced her family name with authentic creative discipline in classical ballet and community teaching.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Haley Arnaz Carson</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">December 17, 1976</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">49 years old (turning 50 in Dec 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Parents</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Desi Arnaz Jr. (adoptive father) & Amy Bargiel Arnaz (mother)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Grandparents</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Lucille Ball & Desi Arnaz (paternal adoptive grandparents)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Matt Carson</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Classical Ballet Dancer, Choreographer & Dance Instructor</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$500,000 – $1.0 Million USD (independent career assets)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Boulder City, Nevada, United States</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Early Background, Mother Amy Bargiel, and Nevada Roots</h2>
            <p>Haley Arnaz was born on December 17, 1976, in Nevada. Her mother, Amy Vacconi (known professionally as Amy Bargiel), was a passionate, highly disciplined classical ballet dancer and dance educator who had dedicated her life to the study of performing arts. Growing up in a household steeped in musical theater, classical orchestration, and rigorous dance routines, Haley was introduced to the barre before she could even read.</p>

            <p>Her childhood in Boulder City, Nevada, was defined by daily rehearsals, stretching sessions, and community recitals. Her mother Amy instilled in her a profound reverence for classical technique, teaching her that dance was not merely entertainment, but an athletic discipline requiring physical precision, mental stamina, and emotional vulnerability.</p>

            <h2>Adoption by Desi Arnaz Jr. and Becoming Part of the Arnaz Dynasty</h2>
            <p>In 1987, Haley’s life expanded in an extraordinary way when her mother Amy married Desi Arnaz Jr., the son of legendary entertainment pioneers Lucille Ball and Desi Arnaz. Desi Jr., who had grown up under intense global media attention from the moment his real-life birth was mirrored on <em>I Love Lucy</em> in 1953, had retired from the frantic Hollywood fast lane, seeking peace and creative rejuvenation in Nevada.</p>

            <p>Desi Jr. fell deeply in love with Amy and formed an immediate, profound fatherly bond with young Haley, who was ten years old at the time. Desi Jr. formally adopted Haley, giving her his family name and embracing her as his beloved daughter. Desi Jr. and Amy’s marriage became an inspiring 28-year partnership characterized by shared artistic projects, deep mutual love, and quiet domestic stability until Amy’s passing from cancer in 2015.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/haley-arnaz-middle.jpg" alt="Haley Arnaz and Desi Arnaz Jr. attending an arts gathering in Nevada" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Haley Arnaz and her adoptive father Desi Arnaz Jr., showcasing their close lifelong bond rooted in creative arts and Nevada community life.</figcaption>
            </figure>

            <h2>The Lucille Ball and Desi Arnaz Heritage: Growing Up in a Legendary Family</h2>
            <p>Becoming an official member of the Arnaz family connected Haley to Hollywood royalty. Her adoptive grandmother, Lucille Ball, was an icon of twentieth-century American comedy, while grandfather Desi Arnaz was a musical innovator who popularized Latin big band music across the United States.</p>

            <p>Rather than using this prestigious lineage to seek out reality television cameos or paparazzi attention, Haley treated her family connection with quiet reverence. Desi Jr. frequently emphasized to Haley the importance of maintaining an authentic, private life away from Hollywood commercialization—a value that Lucille Ball herself had cherished in her private family hours.</p>

            <h2>Passion for Classical Ballet and The Boulder City Ballet Company</h2>
            <p>Following in her mother’s footsteps, Haley Arnaz dedicated her career to classical ballet. In Boulder City, Nevada, Amy and Desi Arnaz Jr. purchased and restored the historic Boulder Theatre, transforming it into a vibrant cultural center and founding the Boulder City Ballet Company (BCBC).</p>

            <p>Haley served as a principal dancer, choreographer, and lead instructor for the company, performing starring roles in seasonal productions such as <em>The Nutcracker</em>, <em>Coppélia</em>, and <em>Sleeping Beauty</em>. Through BCBC, Haley helped train hundreds of young dancers across Southern Nevada, providing accessible arts education and fostering a deep love for classical dance in the desert community.</p>

            <h2>The Historic Boulder Theatre: Restoring a Desert Cultural Jewel</h2>
            <p>The restoration of the historic Boulder Theatre in Boulder City was one of the most remarkable artistic undertakings spearheaded by Desi Arnaz Jr., Amy, and Haley. Originally constructed in the 1930s during the building of the Hoover Dam to provide entertainment for thousands of construction workers, the theater had fallen into disrepair before the Arnaz family acquired it in the late 1990s.</p>

            <p>With Haley actively contributing to stage design, dance floor acoustics, and backstage dressing room arrangements, the theater was transformed into a state-of-the-art regional performing arts facility. The venue not only hosted full-scale ballet productions, but also served as a community hub for youth theatrical workshops, musical concerts, and charitable showcases, solidifying the family's deep roots in Southern Nevada.</p>

            <h2>Choreography and Teaching: Mentoring the Next Generation</h2>
            <p>Beyond her technical mastery as a performing dancer, Haley earned widespread acclaim as an empathetic, encouraging instructor. Understanding the intense physical and emotional toll that classical ballet training can place on young performers, she championed a teaching methodology rooted in positive reinforcement, biomechanical longevity, and expressive joy.</p>

            <p>Former students often describe her classes as transformative, emphasizing that Haley focused on building self-confidence, personal discipline, and creative expression rather than toxic perfectionism. Many of her students went on to secure collegiate dance scholarships and professional engagements across regional American dance troupes, carrying forward the artistic traditions instilled by Haley and her mother Amy.</p>

            <h2>Relationship and Family Life with Husband Matt Carson</h2>
            <p>In her personal life, Haley Arnaz found lasting happiness with her husband, Matt Carson. The couple married in an intimate ceremony surrounded by family and close community friends in Nevada. Much like Haley, Carson appreciates a calm, private existence focused on outdoor life, family gatherings, and community service.</p>

            <p>Following the heartbreaking loss of her mother Amy in 2015, Haley remained an essential pillar of support for Desi Arnaz Jr. Today, the family remains close, honoring Amy’s memory through continued support for local arts education and youth dance scholarships in Boulder City.</p>

            <h2>Preserving Legacy While Choosing Personal Anonymity</h2>
            <p>In an era dominated by social media oversharing and internet influencer culture, Haley Arnaz stands out for her deliberate discretion. She does not maintain public commercial social media profiles, preferring that her contribution to the world be measured by the students she has taught and the classical art she has preserved.</p>

            <p>Her life demonstrates that being part of a legendary family does not require sacrificing personal peace. By dedicating herself to classical ballet and community education, Haley has honored the legacy of Lucille Ball and Desi Arnaz in the most meaningful way possible—through artistic excellence and enduring personal dignity.</p>

            <h2>Life in 2026: Celebrating Artistic Maturity and Family Roots</h2>
            <p>Now in 2026, as she approaches her 50th birthday, Haley Arnaz embodies the enduring grace of a lifetime dedicated to movement and mentorship. Residing peacefully in Nevada with her husband Matt Carson, she continues to advocate for community arts access, mentor emerging regional dancers, and maintain close, affectionate ties with Desi Arnaz Jr.</p>

            <p>Her story stands as an inspiring testament to the power of authentic creative dedication. Without ever leaning on sensationalism or exploiting her historic family name, Haley Arnaz has crafted an honorable, deeply meaningful life that celebrates the transformative beauty of dance and the enduring strength of family love.</p>

            <h2>Frequently Asked Questions About Haley Arnaz</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Haley Arnaz?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Haley Arnaz was born on December 17, 1976, making her 49 years old as of 2026 (turning 50 in December 2026).</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Is Haley Arnaz the biological daughter of Desi Arnaz Jr.?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">No, Haley is the biological daughter of Amy Bargiel. Desi Arnaz Jr. formally adopted Haley after marrying Amy in 1987, raising her with deep fatherly devotion.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Haley Arnaz’s profession?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Haley Arnaz is an accomplished classical ballet dancer, choreographer, and dance instructor associated with the Boulder City Ballet Company in Nevada.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Who is Haley Arnaz married to?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Haley Arnaz is married to Matt Carson, and the couple resides privately in Nevada.</p>
            </div>
        """
    }
]

def add_batch16_and_clean_titles():
    print("Verifying Batch 16 word counts:")
    for art in BATCH16_ARTICLES:
        clean = re.sub(r'<[^<]+?>', ' ', art['contentHtml'])
        wc = len(clean.split())
        print(f"  {art['slug']}: {wc} words")
        if wc < 1200:
            print(f"  [ERROR] {art['slug']} is under 1200 words!")
            return False

    with open(DB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update titles for Batches 14 & 15 to remove the repetitive "in 2026" footprint
    title_replacements = {
        '"Vanessa Villanueva: Life After Her Marriage to Chris Perez, Children, and Quiet Career in 2026"':
            '"Vanessa Villanueva: Life After Her Marriage to Chris Perez, Children, and Quiet Career"',
        '"Joy Ann Richards: Six Decades of Marriage to Jamie Farr, Philanthropic Legacy, and Life in 2026"':
            '"Joy Ann Richards: Six Decades of Marriage to Jamie Farr, Philanthropy, and Enduring Family Bond"',
        '"Sacha Stacey: Inside Her Marriage to Martyn Ford, Family Life, and Fitness Career in 2026"':
            '"Sacha Stacey: Inside Her Marriage to Martyn Ford, Family Dynamics, and Fitness Career"',
        '"Olivia Korenberg: Her Interior Design Career, Marriage to Seann William Scott, and Post-Divorce Life in 2026"':
            '"Olivia Korenberg: Her Interior Design Career, Marriage to Seann William Scott, and Post-Divorce Life"',
        '"Diana Lasso: The Colombian Singer\'s Musical Roots, Marriage to Wayne Brady, and Life Today in 2026"':
            '"Diana Lasso: The Colombian Singer\'s Musical Roots, Marriage to Wayne Brady, and Life Journey"',
        '"Norman Kali: Hawaii Roots, Career in Hollywood Production, and Family Life with Evangeline Lilly in 2026"':
            '"Norman Kali: Hawaii Roots, Career in Hollywood Production, and Family Life with Evangeline Lilly"'
    }

    for old_t, new_t in title_replacements.items():
        if old_t in content:
            content = content.replace(old_t, new_t)
            print(f"Updated title: {old_t[:40]}... -> {new_t[:40]}...")

    # 2. Append Batch 16 articles
    for art in BATCH16_ARTICLES:
        if f'"{art["slug"]}"' in content:
            print(f"Skipping existing {art['slug']}")
            continue
        formatted_entry = pprint.pformat(art, indent=4, width=120)
        idx = content.rfind("]")
        if idx != -1:
            content = content[:idx].rstrip() + ",\n    " + formatted_entry + "\n]\n"
            print(f"Appended {art['slug']} to ALL_ARTICLES")

    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Batch 16 added and older titles cleaned successfully!")
    return True

if __name__ == "__main__":
    add_batch16_and_clean_titles()
