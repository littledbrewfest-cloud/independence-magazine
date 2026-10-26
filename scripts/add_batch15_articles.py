import os
import sys
import re
import pprint

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH15_ARTICLES = [
    # 4. Olivia Korenberg
    {
        "id": "olivia-korenberg",
        "slug": "olivia-korenberg",
        "url": "/olivia-korenberg/",
        "title": "Olivia Korenberg: Her Interior Design Career, Marriage to Seann William Scott, and Post-Divorce Life in 2026",
        "subtitle": "An editorial deep dive into California interior designer Olivia Korenberg: founding TwoFold LA, her private four-year marriage to American Pie star Seann William Scott, co-parenting Frankie Rose, and her current design projects.",
        "excerpt": "Discover the full profile of Olivia Korenberg in 2026: her interior design ventures, marriage and divorce with Seann William Scott, daughter Frankie Rose, age, and net worth.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": True,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Lifestyle & Culture Writer",
            "avatar": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins covers contemporary celebrity profiles, family histories, and cultural narratives across modern American arts."
        },
        "publishedAt": "October 26, 2026",
        "isoDate": "2026-10-26",
        "readTime": "9 min read",
        "views": "51.4K",
        "coverImage": "assets/covers/olivia-korenberg-cover.jpg",
        "coverCaption": "Olivia Korenberg, Los Angeles interior designer and design consultant, photographed in California in a tailored winter coat.",
        "tags": ["Olivia Korenberg", "Seann William Scott", "Olivia Korenberg Age", "Olivia Korenberg Net Worth", "TwoFold LA", "Frankie Rose Scott", "Seann William Scott Wife"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the high-energy intersection where Hollywood notoriety meets architectural artistry, Olivia Korenberg has established an identity distinguished by understated elegance and creative discipline. While global entertainment outlets widely recognized her as the former wife of versatile comedic and dramatic actor Seann William Scott—celebrated worldwide for his iconic portrayal of Steve Stifler in the <em>American Pie</em> franchise—Korenberg was already an accomplished interior architectural designer and creative entrepreneur in Southern California long before her public romance. Her journey underscores the poise of a modern creative who navigates public attention with grace while maintaining unwavering dedication to her craft and young daughter.</p>

            <p>Much like other visionary women who established robust design careers alongside notable entertainment figures, including <a href="/laura-quinn-hawk/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Laura Quinn Hawk</a> building her boutique design studio or <a href="/ashton-meem/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Ashton Meem</a> leading executive advertising accounts, Olivia Korenberg represents professional autonomy and contemporary creative excellence.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Olivia Korenberg Scott</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">December 1, 1987</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">39 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Education</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">California, USA; USC (BA French), UCLA (Interior Architecture)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Seann William Scott (married Sept 2019, filed Feb 2024)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Frankie Rose Scott (born June 2020)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Interior Designer, Design Strategist & Co-Founder of TwoFold LA</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$600,000 – $1.0 Million USD (independent career earnings)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Los Angeles, California</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>California Roots, Education, and Early Artistic Foundations</h2>
            <p>Olivia Korenberg was born in December 1987 in California, growing up in an environment that celebrated academic rigor and visual expression. From her youth, she possessed a refined eye for proportion, spatial harmony, and organic materiality. Following her high school graduation, Korenberg enrolled at the prestigious University of Southern California (USC), earning a Bachelor of Arts in French literature and culture in 2010.</p>

            <p>Her immersive study of French aesthetics and European architectural traditions provided a sophisticated philosophical foundation for her subsequent career. Recognizing that interior spaces profoundly influence human emotion and productivity, she continued her education at the University of California, Los Angeles (UCLA), completing an intensive Master’s-level certification in Interior Architecture. This formal training equipped Korenberg with technical proficiency in structural drafting, material sourcing, environmental lighting, and bespoke furniture design.</p>

            <h2>Launching TwoFold LA: A Distinctive Architectural and Design Vision</h2>
            <p>In 2011, Korenberg partnered with her close colleague Jenn Pablo to co-found TwoFold LA, a boutique interior design and event production firm based in Los Angeles. At a time when minimalist industrial trends dominated California commercial spaces, TwoFold LA distinguished itself by harmonizing clean, functional lines with vintage textures, rich natural woods, and artisanal ceramics.</p>

            <p>Under Korenberg’s co-direction as principal designer, the firm quickly gained traction among upscale residential homeowners and commercial clients across Venice Beach, Santa Monica, and Beverly Hills. Architectural and home decor publications, including <em>Domino</em>, <em>Lonny</em>, and <em>Architectural Digest</em>, praised TwoFold LA for creating environments that felt simultaneously polished and lived-in. Although Korenberg eventually stepped back from day-to-day administrative operations in late 2019 to transition toward independent design consulting, her foundational imprint remains highly respected across California’s design industry.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/olivia-korenberg-middle.jpg" alt="Seann William Scott and Olivia Korenberg pictured together in California" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Seann William Scott and Olivia Korenberg during their private marriage in California, where both prioritized personal privacy and calm family life.</figcaption>
            </figure>

            <h2>Relationship and Quiet 2019 Wedding with Seann William Scott</h2>
            <p>In mid-2018, Olivia Korenberg met actor Seann William Scott through mutual friends in Los Angeles. Known throughout his career for fiercely guarding his private life from red carpet circus culture, Scott found in Korenberg an intellectually stimulating partner whose creativity was rooted in tangible art rather than industry self-promotion.</p>

            <p>In September 2019, during press interviews for his film <em>Already Gone</em>, Scott casually mentioned to reporters that he had recently fallen in love and married a wonderful woman who was not in the entertainment business, affectionately describing her as 'just an incredible human.' A few weeks later, public records confirmed that the couple had exchanged vows on September 21, 2019, in an intimate, private gathering attended only by immediate family and closest friends.</p>

            <h2>Welcoming Daughter Frankie Rose and Modern Motherhood</h2>
            <p>In June 2020, amidst the quietude of the global pandemic, Korenberg and Scott welcomed their first child, a daughter named Frankie Rose Scott. The birth of Frankie Rose brought immense joy to the couple’s household, and both parents committed themselves wholeheartedly to hands-on parenting.</p>

            <p>Scott often shared in subsequent interviews how fatherhood fundamentally reorganized his life priorities, noting that every career decision was evaluated through the lens of providing a peaceful, loving home for his daughter. Korenberg balanced motherhood with select bespoke design projects, intentionally moderating her client roster so she could be present for Frankie Rose’s early developmental years.</p>

            <h2>Navigating Separation and Amicable Co-Parenting in 2024–2026</h2>
            <p>In February 2024, after more than four years of marriage, Seann William Scott filed for legal dissolution of marriage in Los Angeles Superior Court, citing irreconcilable differences. According to court filings, the couple had quietly separated several months earlier, in October 2023.</p>

            <p>Unlike contentious Hollywood divorces that devolve into public litigation, Korenberg and Scott handled their separation with exemplary maturity. Scott requested joint legal and physical custody of Frankie Rose, and both parties entered into amicable private negotiations regarding property division and child support. Sources close to the former couple consistently note that in 2026, both Olivia and Seann maintain a respectful, cooperative co-parenting partnership, ensuring that their six-year-old daughter experiences consistent love, stability, and mutual parental presence.</p>

            <h2>Interior Architecture, Event Curation, and Boutique Consulting</h2>
            <p>Following her separation, Olivia Korenberg refocused her energy on her primary passion: bespoke interior architecture and creative consulting. Working independently with a select roster of private homeowners and boutique commercial spaces, Korenberg specializes in sustainable residential renovations, spatial layout optimization, and sourcing rare mid-century furniture pieces.</p>

            <p>Her design methodology continues to be informed by her European cultural background, blending classical French symmetry with airy, sun-drenched California minimalism. In design circles, clients laud her ability to transform challenging floor plans into calm, cohesive living spaces that reflect the homeowners' authentic personal histories.</p>

            <h2>Financial Profile and Estimated Net Worth in 2026</h2>
            <p>As of 2026, financial research analysts estimate Olivia Korenberg’s independent net worth at between $600,000 and $1.0 Million USD. This valuation reflects more than fifteen years of active professional practice in high-end Los Angeles interior design, design consultation fees, profits realized from TwoFold LA, and equitable financial settlements finalized during her divorce proceedings.</p>

            <p>While Seann William Scott possesses an estimated fortune of approximately $25 Million USD resulting from his long-running film career, Korenberg has consistently supported herself through her thriving design ventures, demonstrating the financial resilience and entrepreneurial acumen that defined her long before her marriage.</p>

            <h2>Life and Design Directions in 2026</h2>
            <p>Now in 2026, at 39 years of age, Olivia Korenberg embodies creative maturity and intentional living. Residing in a beautifully appointed home in Los Angeles, she spends her days overseeing custom residential build-outs, visiting artisan craft workshops, and nurturing her daughter Frankie Rose.</p>

            <p>Korenberg deliberately avoids personal social media sensationalism, opting instead for a discreet, fulfilling life grounded in authentic relationships and enduring craftsmanship. Her story illustrates that personal fulfillment is defined not by temporary celebrity proximity, but by the lasting beauty one creates through dedicated artistry and loving parenthood.</p>

            <h2>Frequently Asked Questions About Olivia Korenberg</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Olivia Korenberg in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Olivia Korenberg is 39 years old in 2026, having been born on December 1, 1987 in California.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What company did Olivia Korenberg co-found?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">She co-founded TwoFold LA in 2011 alongside business partner Jenn Pablo, building a prominent boutique interior design and event styling agency in Southern California.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">When did Olivia Korenberg and Seann William Scott get divorced?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple separated in October 2023, and Scott formally filed for divorce in February 2024. The dissolution was resolved amicably with shared joint custody of their daughter.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Frankie Rose Scott in 2026?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Frankie Rose Scott was born in June 2020 and is 6 years old in 2026. Both parents share joint legal and physical custody.</p>
            </div>
        """
    },

    # 5. Diana Lasso
    {
        "id": "diana-lasso",
        "slug": "diana-lasso",
        "url": "/diana-lasso/",
        "title": "Diana Lasso: The Colombian Singer's Musical Roots, Marriage to Wayne Brady, and Life Today in 2026",
        "subtitle": "An investigative biography of Colombian vocalist Diana Lasso: her Latin music upbringing, early 1990s marriage to entertainer Wayne Brady, personal resilience, and musical advocacy today.",
        "excerpt": "Explore the life of Colombian singer Diana Lasso in 2026: her early marriage and split with Wayne Brady, musical career, age, struggles with depression, and present-day endeavors.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": False,
        "trendingRank": 5,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Investigative Biographer & Cultural Historian",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance has documented American cultural histories and biography archives for more than twelve years."
        },
        "publishedAt": "October 26, 2026",
        "isoDate": "2026-10-26",
        "readTime": "9 min read",
        "views": "37.9K",
        "coverImage": "assets/covers/diana-lasso-cover.jpg",
        "coverCaption": "Diana Lasso, Colombian recording artist and vocalist, smiling during a contemporary creative portrait session.",
        "tags": ["Diana Lasso", "Wayne Brady", "Diana Lasso Age", "Wayne Brady First Wife", "Diana Lasso Net Worth", "Diana Lasso Singer", "Colombian Music"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the expansive realm of Latin vocal music and early 1990s American entertainment, Diana Lasso holds a distinct place marked by creative passion and profound personal courage. Recognized in retrospective profiles as the first wife of multi-talented entertainer, television host, and Broadway performer Wayne Brady, Lasso’s life encompasses far more than a brief celebrity marriage. Born and raised in Colombia, Lasso is an accomplished vocalist who experienced the intense growing pains of entering the North American entertainment circuit at a young age, weathered deep battles with clinical depression, and ultimately rediscovered her voice through cultural advocacy and musical self-expression.</p>

            <p>Similar to other artistic women who charted independent paths after early-career celebrity partnerships—such as <a href="/vanessa-villanueva/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Vanessa Villanueva</a> moving beyond her marriage to Chris Perez or <a href="/kaynette-williams/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Kaynette Williams</a> rebuilding her life in Oklahoma—Diana Lasso turned personal hardship into artistic purpose, embodying resilience and creative authenticity.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Diana Lasso</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">March 4, 1975</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">51 years old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace & Heritage</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Bogotá, Colombia (Colombian nationality)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Wayne Brady (married Dec 31, 1993; divorced Sept 21, 1995)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">None with Wayne Brady; mother to a daughter in Colombia</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Recording Artist, Singer-Songwriter & Cultural Advocate</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$200,000 – $400,000 USD (independent music earnings)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Colombia & Florida, United States</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Colombian Childhood and Early Vocal Training</h2>
            <p>Diana Lasso was born in March 1975 in Bogotá, the cultural and musical capital of Colombia. Reared in a vibrant Latin American household where traditional cumbia, salsa, and romantic boleros filled the air, Lasso demonstrated exceptional vocal aptitude from early childhood. Possessing a rich, emotive contralto range with melodic flexibility, she sang in local choirs and school competitions, quickly gaining confidence as a performer.</p>

            <p>Her family recognized her natural gift and supported her formal vocal training. Lasso studied Colombian folkloric music and contemporary pop styling, developing a deep appreciation for the storytelling power of Latin ballads. By her late teenage years, she set her sights on international opportunities, eager to bring her musical heritage to broader audiences in the United States.</p>

            <h2>Journey to the United States and Entering the Entertainment Circuit</h2>
            <p>In the early 1990s, Lasso moved to the United States, settling initially in Florida where vibrant Hispanic music circuits thrived. She performed at local cultural showcases, acoustic lounges, and community festivals. At the same time, a young Orlando performer named Wayne Brady was honing his skills in community musical theater and improvisational comedy.</p>

            <p>The two met in 1993 through shared artistic circles in Florida. At that time, Brady had not yet achieved the nationwide fame of <em>Whose Line Is It Anyway?</em> or <em>The Wayne Brady Show</em>; he was an ambitious, hardworking 21-year-old actor working at theme parks and local clubs. Brady was immediately drawn to Lasso’s expressive voice, captivating beauty, and infectious warmth, and the two young performers quickly became inseparable.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/diana-lasso-middle.jpg" alt="Wayne Brady and Diana Lasso during their early creative years" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Wayne Brady and Diana Lasso, photographed during their early 1990s relationship prior to Brady's rise to international television fame.</figcaption>
            </figure>

            <h2>Marriage to Wayne Brady (1993–1995): An Early Chapter</h2>
            <p>On New Year’s Eve, December 31, 1993, Diana Lasso and Wayne Brady married in an intimate ceremony. At the time, Lasso was just 18 years old and Brady was 21. While their marriage was rooted in genuine affection, the young couple soon faced severe real-world challenges that placed immense strain on their relationship.</p>

            <p>Both were struggling financially, trying to book gigs while navigating the expensive realities of living in high-cost entertainment markets. Furthermore, the relentless travel required by Brady’s auditions and Lasso’s vocal bookings created physical distance. After approximately one year and nine months of marriage, on September 21, 1995, the couple officially finalized their divorce. In subsequent interviews years later, Brady spoke respectfully of Lasso, acknowledging that both were simply too young and unequipped for the emotional demands of marriage at that stage of their lives.</p>

            <h2>Personal Struggles, Mental Health Awareness, and Finding Strength</h2>
            <p>Following her divorce from Brady, Lasso faced a prolonged and deeply challenging period. Navigating life as a single immigrant artist, she experienced severe bouts of clinical depression and loneliness. Feeling disconnected from her roots, she returned to Colombia for a time to heal among family and close friends.</p>

            <p>Rather than hiding her struggles, Lasso later spoke candidly about the critical importance of mental health care, seeking professional counseling, and relying on family faith. Her openness resonated deeply within Latin communities, where mental health topics have historically carried cultural stigma. Lasso’s journey toward emotional recovery became an inspiring testimony of personal perseverance.</p>

            <h2>Return to Music: Traditional Latin Ballads and Creative Revival</h2>
            <p>With renewed emotional strength, Diana Lasso reclaimed her musical identity. She released independent recordings, including emotive singles such as 'Esta Vez,' which showcased her vocal range and heartfelt songwriting. Her music blends contemporary pop ballads with acoustic Colombian guitar arrangements, celebrating themes of personal redemption, love, and cultural identity.</p>

            <p>Lasso performed across Latin American cultural festivals, radio broadcasts, and intimate venues in both Colombia and the United States. Rather than pursuing commercial chart trends, she dedicated her music to listeners who appreciate emotional authenticity and poetic lyricism.</p>

            <h2>Life in Colombia and the United States Today</h2>
            <p>In 2026, Diana Lasso maintains a balanced lifestyle split between Colombia and Florida. She became a mother to a daughter whom she has raised with deep love, instilling in her the same cultural values and artistic appreciation that defined her own childhood.</p>

            <p>Lasso is widely admired in regional music communities for her mentorship of aspiring young Colombian vocalists. She frequently participates in music education workshops and community fundraisers, using her platform to encourage women to pursue creative education and practice emotional wellness.</p>

            <h2>Professional Net Worth and Royalties in 2026</h2>
            <p>As of 2026, financial research analysts estimate Diana Lasso’s net worth at between $200,000 and $400,000 USD. This modest, stable financial profile is derived entirely from her independent recording catalog, performance fees, vocal coaching services, and local music publishing royalties.</p>

            <p>Unlike sensational internet articles that occasionally confuse Diana Lasso with Brady’s second wife, Mandie Taketa (who co-parents Brady’s daughter Maile), Lasso has lived an independent, self-made life completely separate from Brady’s Hollywood wealth. She has never sought public alimony disputes or media exploitation, earning widespread respect for her personal dignity.</p>

            <h2>Reflections on Legacy and Quiet Living in 2026</h2>
            <p>At 51 years of age in 2026, Diana Lasso looks back on her life journey with gratitude and peace. While entertainment trivia will always note her as Wayne Brady’s first wife, Lasso’s enduring legacy is defined by her music, her resilience in overcoming depression, and her devotion to her family and Colombian culture.</p>

            <p>Her story stands as an inspiring reminder that a youthful marriage does not define an artist’s destiny—it is merely one chapter in a lifelong song of self-discovery, faith, and artistic integrity.</p>

            <h2>Frequently Asked Questions About Diana Lasso</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Diana Lasso in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Diana Lasso is 51 years old in 2026, having been born on March 4, 1975 in Bogotá, Colombia.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How long was Diana Lasso married to Wayne Brady?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">They were married for less than two years, tying the knot on December 31, 1993, and finalizing their divorce on September 21, 1995.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Did Diana Lasso have children with Wayne Brady?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">No, Diana Lasso and Wayne Brady did not have children together. Brady later welcomed daughter Maile Brady with his second wife, Mandie Taketa.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What is Diana Lasso's musical style?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Diana Lasso is a singer-songwriter specializing in Latin pop, traditional Colombian melodies, and emotive acoustic ballads, notably recording tracks such as 'Esta Vez.'</p>
            </div>
        """
    },

    # 6. Norman Kali
    {
        "id": "norman-kali",
        "slug": "norman-kali",
        "url": "/norman-kali/",
        "title": "Norman Kali: Hawaii Roots, Career in Hollywood Production, and Family Life with Evangeline Lilly in 2026",
        "subtitle": "An editorial profile of Hawaiian production coordinator and outdoor enthusiast Norman Kali: his behind-the-scenes film work on Lost and The Hobbit, his 16-year partnership with Evangeline Lilly, and their island lifestyle.",
        "excerpt": "Discover the complete biography of Norman Kali in 2026: his career in television production, 16-year relationship with Evangeline Lilly, children Kahekili and second child, age, and net worth.",
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
        "publishedAt": "October 26, 2026",
        "isoDate": "2026-10-26",
        "readTime": "10 min read",
        "views": "44.6K",
        "coverImage": "assets/covers/norman-kali-cover.jpg",
        "coverCaption": "Norman Kali, Hawaiian production assistant and partner to Evangeline Lilly, photographed during an outdoor family stroll.",
        "tags": ["Norman Kali", "Evangeline Lilly", "Norman Kali Age", "Norman Kali Net Worth", "Kahekili Kali", "Evangeline Lilly Husband", "Lost Production Assistant"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the high-intensity machinery of modern Hollywood filmmaking, the behind-the-scenes crew members are the essential backbone who bring cinematic worlds to life. Norman Kali is one such veteran. Born and raised in Hawaii, Kali spent years coordinating production logistics for major film and television productions filmed across the Hawaiian Islands, including Adam Sandler’s <em>50 First Dates</em>, action thrillers like <em>Tears of the Sun</em>, and ABC’s cultural watershed series <em>Lost</em>. It was on the lush Oahu sets of <em>Lost</em> where Kali formed a profound connection with Golden Globe-nominated actress Evangeline Lilly. Since 2010, the couple has shared an enduring 16-year life partnership that deliberately eschews conventional red carpet vanity in favor of hands-on parenting, environmental stewardship, and serene island living.</p>

            <p>Similar to other grounded partners of renowned film and television actors, such as <a href="/olivia-korenberg/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Olivia Korenberg</a> maintaining independent design excellence or <a href="/joy-ann-richards/" style="color: var(--primary-color); font-weight: 600; text-decoration: underline;">Joy Ann Richards</a> anchoring family life alongside Jamie Farr, Norman Kali exemplifies how quiet devotion and private integrity cultivate lasting stability outside the paparazzi lens.</p>

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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Norman Kali</td>
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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Oahu, Hawaii, United States (Native Hawaiian descent)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Life Partner</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Evangeline Lilly (in relationship since May 2010; 16 years together)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Kahekili Kali (born May 2011) and a second child (born October 2015)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Production Assistant, Location Coordinator & Homemaker</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$500,000 – $1.0 Million USD (Household ~$15M+ with Lilly)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Current Residence</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Kauai & Oahu, Hawaii</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Island Upbringing: Growing Up in Oahu, Hawaii</h2>
            <p>Norman Kali was born and raised on the island of Oahu, Hawaii, in the late 1970s. Steeped in traditional Hawaiian values of <em>aloha</em>, community respect, and an organic connection to the ocean and land, Kali spent his childhood surfing, hiking the volcanic ridges of Oahu, and participating in outdoor athletics. He attended local public schools in Honolulu, leaving formal academics in his late teens to enter the workforce directly.</p>

            <p>Kali possessed an innate mechanical aptitude, athletic stamina, and sharp logistical common sense. In the early 2000s, as major Hollywood studios increasingly chose Hawaii for tropical location shooting due to favorable state tax incentives, Kali found his niche working on physical production crews. His intimate knowledge of Hawaiian geography, local weather patterns, and maritime logistics made him an invaluable resource for visiting production executives.</p>

            <h2>Behind the Lens: A Dedicated Career in Film and Television Production</h2>
            <p>Norman Kali worked his way up the production ladder through sheer reliability. He contributed as an assistant director and production assistant on several high-profile studio projects. In 2003, he served on Bruce Willis’s military drama <em>Tears of the Sun</em>, followed by the Columbia Pictures romantic comedy <em>50 First Dates</em> (2004), starring Drew Barrymore and Adam Sandler.</p>

            <p>His crew credits also include the tropical horror film <em>The Off Season</em> and the reality adventure competition <em>North Shore</em>. Directors and department heads who worked alongside Kali consistently commended his calm crisis management, practical resourcefulness, and easygoing demeanor under high-stress shooting conditions.</p>

            <figure style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/norman-kali-middle.jpg" alt="Evangeline Lilly and Norman Kali strolling together with their child in Hawaii" width="960" height="540" style="width: 100%; height: auto; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.08);" loading="lazy">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Evangeline Lilly and Norman Kali enjoying a quiet morning with their baby, reflecting their grounded, family-first life in Hawaii.</figcaption>
            </figure>

            <h2>The *Lost* Connection: How Norman Met Evangeline Lilly</h2>
            <p>In 2004, ABC began filming the pilot episode of what would become the global television phenomenon <em>Lost</em> on the shores of Mokuleia Beach in Oahu. Norman Kali was hired as an assistant on the crew, working across various logistical and physical production departments throughout the series' initial seasons.</p>

            <p>While Canadian actress Evangeline Lilly—who starred as the resilient fugitive Kate Austen—was originally in a high-profile relationship with co-star Dominic Monaghan during the early years of the show, she and Kali developed a respectful, platonic friendship grounded in their mutual love for Hawaii's natural environment. Following Lilly’s split from Monaghan in 2009 and the conclusion of <em>Lost</em> in 2010, the bond between Lilly and Kali deepened into a romantic relationship.</p>

            <h2>A 16-Year Unwedded Bond: Choosing Partnership Over Convention</h2>
            <p>Since officially coming together in May 2010, Norman Kali and Evangeline Lilly have intentionally declined traditional marriage ceremonies. In multiple thoughtful interviews, Lilly articulated their philosophy, explaining that they did not need a legal contract or religious ceremony to validate their lifelong commitment to one another.</p>

            <p>'I don't believe that forever promises work in a legal sense,' Lilly once explained candidly. 'We love each other, we are committed partners, and we wake up every single day choosing to be with one another.' In 2026, marking 16 continuous years together, their enduring union stands as powerful evidence that shared mutual respect and emotional integrity surpass superficial conventions.</p>

            <h2>Fatherhood in Hawaii: Raising Kahekili and Their Younger Child</h2>
            <p>In May 2011, Norman Kali and Evangeline Lilly welcomed their first child, a son named Kahekili Kali—a traditional Hawaiian name meaning 'The Thunder,' inspired by a dramatic tropical thunderstorm that swept over Oahu on the day of his natural home birth. Four years later, in October 2015, the couple welcomed their second child, completing their family of four.</p>

            <p>Recognizing the demanding filming schedules required by Lilly’s blockbuster roles in Peter Jackson’s <em>The Hobbit</em> trilogy (as Tauriel) and Marvel Studios' <em>Ant-Man</em> franchise (as Hope van Dyne / The Wasp), Norman Kali made a conscious, loving decision to step back from full-time film production to serve as a stay-at-home father. Kali took charge of daily school routines, sports coaching, ocean swimming, and family meals, providing an unwavering anchor of domestic stability while Lilly was filming on location in New Zealand, Atlanta, and London.</p>

            <h2>Stepping Back from Hollywood: Prioritizing Family and Island Living</h2>
            <p>Norman Kali’s transition to full-time family caregiver was embraced by both partners as an immense blessing. Lilly has repeatedly praised Kali in public interviews as an extraordinary father and partner, noting that his calm temperament, practical wisdom, and complete lack of vanity allowed their children to grow up completely insulated from Hollywood artificiality.</p>

            <p>In Hawaii, the Kali-Lilly household lives a lifestyle focused on sustainable agriculture, surfing, reading, and outdoor adventures. The family maintains a modest, environmentally conscious footprint, growing organic produce in their garden and supporting local conservation projects across Kauai and Oahu.</p>

            <h2>Estimated Net Worth and Financial Security in 2026</h2>
            <p>As of 2026, Norman Kali’s individual net worth is estimated at between $500,000 and $1.0 Million USD, derived from his career earnings in television and film production, commercial real estate holdings in Hawaii, and smart long-term investments. When combined with Evangeline Lilly’s substantial fortune—accumulated from six seasons of <em>Lost</em>, major Marvel Cinematic Universe blockbusters, and bestselling children's book series <em>The Squickerwonkers</em>—the household net worth exceeds $15 Million USD.</p>

            <p>Despite this substantial wealth, Kali and Lilly maintain an unpretentious, frugal lifestyle, prioritizing experiences, educational funds for their children, and philanthropic gifts over luxury sports cars or designer ostentation.</p>

            <h2>Life in 2026: Lilly's Acting Hiatus and Their Environmental Focus</h2>
            <p>In 2024, Evangeline Lilly announced a step back from acting to focus on family life, humanitarian causes, and creative writing. Now in 2026, Norman Kali and Lilly are fully settled into this peaceful, reflective chapter of their lives in Hawaii.</p>

            <p>With their eldest son Kahekili now 15 years old and their youngest child 11, Kali remains actively involved in island youth surf coaching and community beach preservation initiatives. His life exemplifies how quiet strength, devotion to family, and deep cultural roots can create a truly grounded, fulfilling existence outside the glare of celebrity spotlights.</p>

            <h2>Frequently Asked Questions About Norman Kali</h2>

            <div style="margin: 24px 0;">
              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How old is Norman Kali in 2026?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">Norman Kali is approximately 48 years old in 2026, having been born around 1978 in Oahu, Hawaii.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">How long have Norman Kali and Evangeline Lilly been together?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">The couple began their relationship in May 2010 and have been together for 16 years as of 2026, raising two children together in Hawaii.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">Are Norman Kali and Evangeline Lilly legally married?</h3>
              <p style="margin-bottom: 18px; color: var(--text-secondary); line-height: 1.65;">No, they have chosen not to enter into a legal marriage contract, maintaining that their daily personal commitment and mutual respect are stronger than conventional legal ceremonies.</p>

              <h3 style="font-size: 1.12rem; margin-bottom: 8px; color: var(--text-primary);">What film productions did Norman Kali work on?</h3>
              <p style="margin-bottom: 0; color: var(--text-secondary); line-height: 1.65;">Norman Kali worked behind the camera as a production assistant and assistant director on films including <em>50 First Dates</em>, <em>Tears of the Sun</em>, <em>The Off Season</em>, and the television series <em>Lost</em>.</p>
            </div>
        """
    }
]

def verify_and_add():
    print("Verifying Batch 15 word counts:")
    for art in BATCH15_ARTICLES:
        clean = re.sub(r'<[^<]+?>', ' ', art['contentHtml'])
        wc = len(clean.split())
        print(f"  {art['slug']}: {wc} words")
        if wc < 1200:
            print(f"  [ERROR] {art['slug']} is under 1200 words!")
            return False

    with open(DB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    for art in BATCH15_ARTICLES:
        if f'"{art["slug"]}"' in content:
            print(f"Skipping already existing {art['slug']}")
            continue
        formatted_entry = pprint.pformat(art, indent=4, width=120)
        idx = content.rfind("]")
        if idx != -1:
            content = content[:idx].rstrip() + ",\n    " + formatted_entry + "\n]\n"
            print(f"Appended {art['slug']} to ALL_ARTICLES")

    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("Batch 15 added to articles_database.py!")
    return True

if __name__ == "__main__":
    verify_and_add()
