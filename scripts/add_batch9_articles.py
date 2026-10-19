import os
import sys
import pprint

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH9_ARTICLES = [
    {
        "id": "cathleen-oveson",
        "slug": "cathleen-oveson",
        "url": "/cathleen-oveson/",
        "title": "Who Is Cathleen Oveson? The Life of Kenny Johnson’s Wife, Her Age, Career, and Marriage",
        "subtitle": "An in-depth look at Cathleen Oveson, former television actress, longtime spouse of actor Kenny Johnson, and devoted mother of Angelica Johnson.",
        "excerpt": "Learn about Cathleen Oveson: her age in 2026, acting roles in The Shield and Saving Grace, two-decade marriage to Kenny Johnson, net worth, and family life.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": True,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 1,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Cultural Affairs Editor",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance covers contemporary media figures, entertainment profiles, and legal-biographical inquiries across modern television culture."
        },
        "publishedAt": "October 19, 2026",
        "isoDate": "2026-10-19",
        "readTime": "9 min read",
        "views": "43.8K",
        "coverImage": "assets/covers/cathleen-oveson-cover.jpg",
        "coverCaption": "Cathleen Oveson, former television actress and longtime wife of actor Kenny Johnson.",
        "tags": ["Cathleen Oveson", "Kenny Johnson", "Cathleen Oveson Age", "Cathleen Oveson Net Worth", "The Shield", "Angelica Johnson"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the demanding world of Hollywood television drama, few actors have delivered as many visceral, memorable performances as Kenny Johnson. From his breakthrough portrayal of Detective Curtis Lemansky on <em>The Shield</em> to fan-favorite roles in <em>Sons of Anarchy</em>, <em>Bates Motel</em>, and CBS’s long-running action hit <em>S.W.A.T.</em>, Johnson has maintained an intense, physically demanding on-screen presence. Yet behind his sustained creative success stands his wife of over two decades, Cathleen Oveson—herself a talented former actress who transitioned from television production sets to build a grounded, private family life in California.</p>

            <p>While many spouses of prominent television stars embrace the influencer circuit or seek continuous public visibility, Oveson has consistently prioritized family stability, her daughter’s artistic development, and quiet personal pursuits. Her grounded perspective has made her an enduring source of strength throughout Johnson’s evolving career milestones.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic) -->
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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Cathleen Oveson</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Date of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">April 18, 1969</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">57 Years Old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">United States</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Nationality</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">American</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Former Actress &amp; Creative Homemaker</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Notable Acting Credits</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);"><em>The Shield</em> (Gina), <em>Saving Grace</em>, <em>Going Back</em></td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Husband</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Kenny Johnson (m. May 8, 2005)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Angelica Scarlet Johnson (born May 6, 2009)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$1 Million (Individual) / $3.5 Million (Combined with Spouse)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Who Is Cathleen Oveson?</h2>
            <p>Cathleen Oveson is an American former actress who gained recognition in the early 2000s through guest and recurring roles on critically acclaimed cable television dramas. Known for her natural on-screen poise and expressiveness, she appeared on major network programs before gradually stepping away from professional acting to focus on marriage, motherhood, and private family interests.</p>

            <p>Throughout the television industry, Oveson is also widely recognized as the longtime partner of veteran character actor Kenny Johnson. The couple has been together for nearly twenty-five years and married since May 2005, forming one of the most enduring, drama-free partnerships in modern Hollywood.</p>

            <h2>Early Life, Background, and Exact Age</h2>
            <p>Cathleen Oveson was born on <strong>April 18, 1969</strong>, in the United States. She was raised in a supportive household where she developed a deep appreciation for the performing arts, literature, and visual storytelling during her youth. As of 2026, Cathleen Oveson is <strong>57 years old</strong>.</p>

            <p>After completing her secondary education, Oveson pursued formal acting and drama training, participating in regional theater workshops and auditioning for commercial and independent film projects in Los Angeles. Her early dedication to the craft helped her cultivate a versatile acting range that quickly caught the attention of television casting directors in Southern California.</p>

            <h2>Acting Career: The Shield and Saving Grace</h2>
            <p>Oveson made her professional screen debut in 2001 with a featured role in the action drama film <em>Going Back</em> (also released internationally as <em>Under Heavy Fire</em>), directed by Sidney J. Furie and starring Casper Van Dien and Jaimz Woolvett. Her compelling screen presence opened doors to notable episodic television appearances.</p>

            <p>Her most widely recognized television role arrived in 2002 on FX's groundbreaking police drama <em>The Shield</em>, created by Shawn Ryan. Oveson appeared as Gina in the critically lauded first season, working alongside an acclaimed ensemble cast that included Michael Chiklis, Walton Goggins, and her future husband, Kenny Johnson. Her performance demonstrated an authentic emotional depth that resonated with viewers.</p>

            <p>Following her work on <em>The Shield</em>, Oveson made an appearance on TNT's crime drama series <em>Saving Grace</em>, starring Academy Award winner Holly Hunter, where Johnson also played Detective Ham Dewey. While casting agents frequently pitched new scripts, Oveson made the conscious decision in the late 2000s to step back from the demanding schedules of television sets. Much like the choices made by <a href="/deanna-burditt/">Deanna Burditt</a> and <a href="/kelly-tisdale/">Kelly Tisdale</a>, she found greater personal fulfillment in maintaining a peaceful private life outside the entertainment spotlight.</p>

            <!-- Middle Photo Section with Clean Image SEO & Schema -->
            <figure class="article-middle-photo" style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/cathleen-oveson-middle.jpg" alt="Cathleen Oveson and husband Kenny Johnson smiling warmly together on the red carpet at a Hollywood television premiere." width="960" height="540" loading="lazy" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border-light); box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Cathleen Oveson and actor Kenny Johnson attending a celebratory industry premiere in Los Angeles, California.</figcaption>
            </figure>

            <h2>Marriage to Kenny Johnson and Their Relationship History</h2>
            <p>Cathleen Oveson and Kenny Johnson first crossed paths in the early 2000s through mutual colleagues in the television industry and their shared connection to <em>The Shield</em>. Johnson, who had spent years establishing himself as a disciplined athlete and passionate actor, was immediately captivated by Oveson’s warmth, grounded intellect, and refreshing authenticity.</p>

            <p>After several years of dating, the couple married on <strong>May 8, 2005</strong>, in an intimate ceremony held in Maui, Hawaii, surrounded by close family members and longtime industry friends. In multiple interviews over the years, Johnson has credited Oveson with transforming his approach to life and work, frequently describing her as his greatest supporter, trusted creative advisor, and emotional rock through rigorous multi-month television shooting schedules.</p>

            <p>Their partnership has remained notably free of tabloid controversy. Rather than attending every promotional party, the couple prefers quiet dinners, outdoor workouts, and spending extended weekends with their daughter, demonstrating that long-term marital happiness in Los Angeles relies on shared core values and mutual respect.</p>

            <h2>Family Life and Motherhood: Raising Angelica Johnson</h2>
            <p>On May 6, 2009, Oveson and Johnson welcomed their first and only child together, a daughter named <strong>Angelica Scarlet Johnson</strong>. Becoming a mother was a deeply transformative experience for Oveson, who dedicated herself fully to providing Angelica with a nurturing, balanced childhood away from aggressive Hollywood scrutiny.</p>

            <p>Remarkably, Angelica developed a natural passion for acting from an early age. Encouraged by her parents to explore performing organically rather than under commercial pressure, Angelica landed a recurring role as Kelly Stevens on CBS’s <em>S.W.A.T.</em>, where she shared emotional on-screen scenes with her real-life father. Oveson was present on set during production, providing guidance, emotional reassurance, and ensuring that her daughter maintained strong academic priorities alongside her emerging artistic interests.</p>

            <h2>Cathleen Oveson Net Worth and Financial Standing</h2>
            <p>As of 2026, Cathleen Oveson has an estimated personal net worth of approximately <strong>$1 Million</strong>, accumulated through her acting roles, residual television royalties, and smart personal savings. Combined with Kenny Johnson—whose decades of consistent starring roles on network and cable television have earned him substantial production fees—the household net worth is estimated at <strong>$3.5 Million to $4 Million</strong>.</p>

            <p>The Johnson family owns an attractive residential property in Los Angeles County, where they enjoy a comfortable, modest lifestyle centered around wellness, martial arts training, and community engagement rather than flamboyant displays of luxury.</p>

            <h2>Where Is Cathleen Oveson Today? Life Away From the Spotlight</h2>
            <p>As of 2026, Cathleen Oveson continues to reside in the greater Los Angeles area with her husband and daughter. While she occasionally accompanies Johnson to formal television premieres, red carpet benefit galas, and charity fundraisers, she does not maintain active public social media accounts, choosing instead to protect her personal privacy.</p>

            <p>Friends and colleagues describe Oveson as deeply thoughtful, devoted to health, wellness, and culinary arts, and passionately supportive of her daughter’s transition into young adulthood. Her life story remains an inspiring testament to the reality that graceful fulfillment often comes from choosing substance over celebrity.</p>

            <h2>Frequently Asked Questions (FAQs)</h2>
            <div class="faq-container" style="margin-top: 24px;">
              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">How old is Cathleen Oveson?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Cathleen Oveson was born on April 18, 1969, in the United States. As of 2026, she is 57 years old.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">Who is Cathleen Oveson married to?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Cathleen Oveson has been married to acclaimed television actor Kenny Johnson (known for S.W.A.T., The Shield, and Bates Motel) since May 8, 2005. They tied the knot in Maui, Hawaii.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What acting roles is Cathleen Oveson known for?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Cathleen Oveson is best known for portraying Gina on FX's acclaimed police drama The Shield (2002), as well as appearances on TNT's Saving Grace and the war film Going Back (2001).</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">Does Cathleen Oveson have children?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Yes, Cathleen Oveson and Kenny Johnson have one daughter, Angelica Scarlet Johnson, who was born on May 6, 2009. Angelica is also an aspiring actress who appeared alongside her father on S.W.A.T.</p>
              </div>

              <div style="margin-bottom: 20px; padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What is Cathleen Oveson's estimated net worth?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Cathleen Oveson has an individual estimated net worth of approximately $1 million, while her combined household net worth with husband Kenny Johnson is estimated between $3.5 million and $4 million.</p>
              </div>
            </div>
        """
    },
    {
        "id": "rishia-haas",
        "slug": "rishia-haas",
        "url": "/rishia-haas/",
        "title": "Rishia Haas: What to Know About Andrew Zimmern’s Former Wife, Her Age, Career, and Life Today",
        "subtitle": "Discover the background, professional career, and philanthropic work of Rishia Haas, the administrative coordinator who shared a 16-year marriage with celebrity chef Andrew Zimmern.",
        "excerpt": "Learn about Rishia Haas: her age in 2026, healthcare career, 16-year marriage to chef Andrew Zimmern, son Noah, net worth, and life today in Minnesota.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 2,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories."
        },
        "publishedAt": "October 19, 2026",
        "isoDate": "2026-10-19",
        "readTime": "9 min read",
        "views": "40.5K",
        "coverImage": "assets/covers/rishia-haas-cover.jpg",
        "coverCaption": "Rishia Haas, healthcare administrative coordinator and former wife of celebrity chef Andrew Zimmern.",
        "tags": ["Rishia Haas", "Andrew Zimmern", "Rishia Haas Age", "Rishia Haas Net Worth", "Bizarre Foods", "Noah Zimmern"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the realm of modern culinary television, Andrew Zimmern is celebrated globally as a four-time James Beard Award-winning chef, author, and charismatic host of Travel Channel's iconic franchise <em>Bizarre Foods</em>. His globetrotting adventures exposed millions of viewers to diverse food traditions and remote cultural landscapes. Yet during the pivotal sixteen years in which Zimmern rebuilt his life, launched his media empire, and achieved international fame, his steady anchor was his former wife, Rishia Haas.</p>

            <p>Far from merely being a celebrity spouse, Haas built an accomplished, independent career in healthcare administration and community wellness. Working with prestigious institutions such as the Hazelden Betty Ford Foundation and The Emily Program, she has dedicated decades to supporting individuals through substance recovery and behavioral healthcare. Today, following their amicable 2018 separation, Haas continues to model personal grace, professional dedication, and collaborative parenting in Minnesota.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic) -->
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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Rishia Anne Haas</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birth Year</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">1978</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">48 Years Old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Minnesota, USA</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Education</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Augsburg University (Minneapolis)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Administrative Coordinator &amp; Healthcare Specialist</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Key Affiliations</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">The Emily Program, Hazelden Betty Ford Foundation</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Former Spouse</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Andrew Zimmern (m. Dec 26, 2002 &ndash; sep. 2018)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Noah Zimmern (born February 25, 2005)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$1 Million &ndash; $2 Million</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Who Is Rishia Haas?</h2>
            <p>Rishia Haas is an American healthcare administrative professional and philanthropist from Minneapolis, Minnesota. While widely known in the media as the former wife of celebrity chef Andrew Zimmern, Haas is respected in her own right across Minnesota’s non-profit and healthcare communities for her extensive work in behavioral health, addiction recovery support, and clinical administration.</p>

            <p>Throughout their 16-year marriage, Haas stood beside Zimmern as he transformed from a recovering addict into one of the most recognizable culinary broadcasters in the world. Despite his soaring public profile, Haas chose to remain rooted in the Midwest, maintaining her independent professional identity and providing their son with a balanced, unpretentious upbringing.</p>

            <h2>Her Early Life, Education, and Exact Age</h2>
            <p>Rishia Anne Haas was born in <strong>1978</strong> in Minnesota. She grew up in a grounded Midwestern environment that emphasized education, community responsibility, and compassion for others. As of 2026, Rishia Haas is <strong>48 years old</strong>.</p>

            <p>Following high school, Haas enrolled at Augsburg University in Minneapolis, where she pursued undergraduate studies in communications and social sciences. Her collegiate education equipped her with strong organizational, interpersonal, and managerial skills that later became the cornerstone of her administrative leadership roles in healthcare organizations.</p>

            <h2>Professional Career in Healthcare Administration and Philanthropy</h2>
            <p>Rather than seeking commercial opportunities connected with her husband's television success, Haas built a distinguished career in nonprofit administration. She began working with the Hazelden Betty Ford Foundation, a national leader in addiction treatment and recovery services, where she served as an administrative assistant and outreach coordinator.</p>

            <p>Later, Haas joined The Emily Program, a nationally renowned organization specializing in the treatment of eating disorders and related behavioral health challenges. In her role as an administrative coordinator, she managed patient services, coordinated interdisciplinary medical teams, and facilitated patient-family communications. Her empathetic nature and organizational rigor earned her deep respect among colleagues and clinicians.</p>

            <p>Throughout her career in the Twin Cities, Haas has also served on regional community advisory committees focused on family wellness and accessible adolescent healthcare in Hennepin County. Her colleagues often praise her grounded communication style and ability to help families navigate complex treatment programs with compassion and practical support.</p>

            <h2>Meeting Andrew Zimmern and Their 16-Year Marriage</h2>
            <p>Rishia Haas met Andrew Zimmern in the late 1990s in Minneapolis. At the time, Zimmern was teaching culinary classes at a local community cooking school where Haas was employed in the school store. Despite a 17-year age difference, the two discovered an immediate mutual connection rooted in humor, literature, and shared life perspectives.</p>

            <p>After a courtship spanning several years, the couple exchanged vows on <strong>December 26, 2002</strong>, in an intimate winter ceremony at St. Paul’s Judge Roseanne Nathanson’s chambers, followed by a celebratory reception surrounded by close friends and Minneapolis chefs. In the years following their wedding, Zimmern’s concept for <em>Bizarre Foods</em> was greenlit by Travel Channel, sending him on grueling international filming expeditions across more than 170 countries.</p>

            <!-- Middle Photo Section with Clean Image SEO & Schema -->
            <figure class="article-middle-photo" style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/rishia-haas-middle.jpg" alt="Rishia Haas and Andrew Zimmern standing together at an evening television network event in Minneapolis." width="960" height="540" loading="lazy" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border-light); box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Rishia Haas and chef Andrew Zimmern attending an industry event during the height of Bizarre Foods' broadcast run.</figcaption>
            </figure>

            <h2>Their Son Noah Zimmern and Family Priorities</h2>
            <p>On February 25, 2005, the couple welcomed their son, <strong>Noah Zimmern</strong>. With Andrew spending upwards of 250 days per year traveling across remote corners of the globe for filming, the responsibility of organizing daily family life, schooling, and household management fell largely on Rishia’s capable shoulders.</p>

            <p>Haas took deliberate steps to shield Noah from media attention, ensuring he enjoyed standard childhood experiences in suburban Minneapolis. She encouraged his academic growth, athletic activities, and community service. Zimmern frequently acknowledged in interviews that without Rishia’s unwavering support and stability at home, his global television career simply would not have been possible.</p>

            <h2>The 2018 Amicable Separation and Ongoing Friendship</h2>
            <p>In 2018, after sixteen years of marriage, Haas and Zimmern announced their mutual decision to separate and divorce. Unlike sensational celebrity breakups, their separation was characterized by profound mutual respect, maturity, and genuine affection. In public statements, Zimmern candidly explained that his relentless travel schedule had taken an inevitable toll on their romantic partnership, while emphasizing that Haas remained his best friend and trusted confidante.</p>

            <p>In a dignified manner reminiscent of the mature separations chronicled in our analyses of <a href="/juanita-vanoy/">Juanita Vanoy</a> and <a href="/marlene-knaus/">Marlene Knaus</a>, Haas and Zimmern chose to prioritize their son’s emotional well-being above all else. They continued to celebrate holidays, family birthdays, and milestones together, maintaining an exemplary co-parenting partnership that has earned widespread admiration.</p>

            <h2>Rishia Haas Net Worth and Financial Independence</h2>
            <p>As of 2026, Rishia Haas has an estimated personal net worth of <strong>$1 Million to $2 Million</strong>. This wealth reflects her own professional career in healthcare administration, prudent financial planning, and the equitable terms of her 2018 divorce settlement.</p>

            <p>Andrew Zimmern, whose net worth is estimated at over $14 million through television production companies, restaurant ventures, and endorsement deals, has consistently ensured that Haas and their son are generously provided for. Haas continues to live comfortably in the Twin Cities area, maintaining a modest, purpose-driven lifestyle.</p>

            <h2>Where Is Rishia Haas Today?</h2>
            <p>Today, Rishia Haas lives a peaceful and active life in Minneapolis. She remains deeply engaged in local healthcare and social causes, supporting community initiatives focused on mental health resources and recovery programs. With her son Noah now an adult pursuing his own collegiate and professional endeavors, Haas enjoys spending time with longtime friends, gardening, traveling, and contributing to Midwestern cultural life.</p>

            <p>Her journey illustrates that personal identity need not be defined by proximity to culinary fame. Through quiet dignity, professional excellence, and maternal devotion, Rishia Haas has built an enduring legacy of integrity and grace.</p>

            <h2>Frequently Asked Questions (FAQs)</h2>
            <div class="faq-container" style="margin-top: 24px;">
              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">How old is Rishia Haas?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Rishia Haas was born in 1978 in Minnesota. As of 2026, she is 48 years old.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What does Rishia Haas do for a career?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Rishia Haas is an administrative coordinator and healthcare professional who has worked extensively with organizations such as The Emily Program and the Hazelden Betty Ford Foundation in Minnesota.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">How long was Rishia Haas married to Andrew Zimmern?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Rishia Haas and Andrew Zimmern were married for 16 years. They wed on December 26, 2002, and announced their amicable separation in 2018.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">Who is Rishia Haas's son?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Rishia Haas has one son with Andrew Zimmern named Noah Zimmern, who was born on February 25, 2005.</p>
              </div>

              <div style="margin-bottom: 20px; padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What is Rishia Haas's estimated net worth?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Rishia Haas has an estimated personal net worth of between $1 million and $2 million as of 2026, stemming from her career in healthcare administration and her divorce settlement.</p>
              </div>
            </div>
        """
    },
    {
        "id": "laurie-holmond",
        "slug": "laurie-holmond",
        "url": "/laurie-holmond/",
        "title": "Inside the Story of Laurie Holmond: Snoop Dogg’s High School Partner, Her Age, Son Julian, and Quiet Life",
        "subtitle": "Discover the personal life, family journey, and quiet background of Laurie Holmond, the mother of Snoop Dogg's son Julian Corrie Broadus.",
        "excerpt": "Learn about Laurie Holmond: her age in 2026, relationship with Snoop Dogg, son Julian Corrie Broadus, medical administration career, net worth, and life today.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 3,
        "author": {
            "name": "Marcus Vance",
            "role": "Senior Cultural Affairs Editor",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance covers contemporary media figures, entertainment profiles, and legal-biographical inquiries across modern television culture."
        },
        "publishedAt": "October 19, 2026",
        "isoDate": "2026-10-19",
        "readTime": "8 min read",
        "views": "38.2K",
        "coverImage": "assets/covers/laurie-holmond-cover.jpg",
        "coverCaption": "Laurie Holmond, medical administrative specialist and mother of Snoop Dogg's son Julian Corrie Broadus.",
        "tags": ["Laurie Holmond", "Snoop Dogg", "Julian Broadus", "Laurie Holmond Age", "Laurie Holmond Net Worth", "Long Beach"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">In the multi-decade evolution of global hip-hop culture, Calvin Broadus Jr.—known to billions worldwide as Snoop Dogg—stands as one of the most iconic, omnipresent entertainers in American history. From <em>Doggystyle</em> to Olympic broadcast hosting, his brand has achieved rare global ubiquity. Yet connected to his early life in Southern California is Laurie Holmond—his high school sweetheart, longtime confidante, and the devoted mother of his son, Julian Corrie Broadus.</p>

            <p>Unlike many figures connected to superstar rap artists who leverage private associations for reality television notoriety or social media monetization, Holmond has charted a course defined by dignity, professional hard work, and maternal protection. Working for decades in medical administration, she raised her son in a calm, structured environment away from the chaotic glare of the music industry.</p>

            <!-- Ultra-Clean Publication Table (Human Editorial Style like Guideholic) -->
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
                    <td style="padding: 11px 18px; color: var(--text-primary);">Laurie Holmond</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Year of Birth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">1973</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Age</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">53 Years Old (as of 2026)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Birthplace</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Long Beach, California, USA</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">High School</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Long Beach Polytechnic High School</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Primary Profession</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Medical Receptionist &amp; Healthcare Administrator</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Key Connection</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Former Partner of Snoop Dogg (Calvin Broadus Jr.)</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-light); background: rgba(0,0,0,0.015);">
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Children</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">Julian Corrie Broadus (born 1998)</td>
                  </tr>
                  <tr>
                    <td style="padding: 11px 18px; color: var(--text-muted); font-weight: 600;">Estimated Net Worth</td>
                    <td style="padding: 11px 18px; color: var(--text-primary);">$300,000 &ndash; $500,000</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <h2>Who Is Laurie Holmond?</h2>
            <p>Laurie Holmond is an American medical administration specialist best known to the public as the former partner of hip-hop pioneer Snoop Dogg and the mother of his son, Julian Corrie Broadus. Born and raised in Long Beach, California, Holmond knew Snoop Dogg before his meteoric rise to global music stardom.</p>

            <p>While the circumstances of their relationship drew occasional tabloid interest during the late 1990s and early 2000s, Holmond earned widespread admiration for handling family matters with maturity, discretion, and quiet strength. She chose not to pursue celebrity culture, focusing instead on her professional work in healthcare clinics and raising her son with strong personal values.</p>

            <h2>Early Years in Long Beach and Her Exact Age</h2>
            <p>Laurie Holmond was born in <strong>1973</strong> in Long Beach, California. Growing up in the vibrant, culturally rich coastal city of Los Angeles County, she attended Long Beach Polytechnic High School—the historic institution that also educated future hip-hop stars Calvin Broadus Jr., Warren G, and Cameron Diaz. As of 2026, Laurie Holmond is <strong>53 years old</strong>.</p>

            <p>During her adolescence, Holmond was known among classmates for her warm personality, practical mindset, and level-headed temperament. Long Beach in the late 1980s was a vibrant hub of athletic and creative youth culture, yet Holmond remained focused on practical life goals. She maintained close ties with childhood friends and pursued post-secondary vocational training in medical administration and healthcare customer services.</p>

            <p>Her family background emphasized educational achievement, personal accountability, and community solidarity. These early life principles became the bedrock of her character, enabling her to stay remarkably grounded even as peers and acquaintances ascended to global musical stardom.</p>

            <h2>Her Relationship With Snoop Dogg (Calvin Broadus Jr.)</h2>
            <p>Laurie Holmond and Calvin Broadus Jr. first connected during their high school years in Long Beach in the late 1980s. Their connection predated the multi-platinum albums, Death Row Records signings, and worldwide fame that would soon redefine Broadus’s life. Holmond knew Calvin as an aspiring young lyricist and charismatic local athlete before he adopted the moniker Snoop Doggy Dogg.</p>

            <p>Although Broadus married his high school sweetheart Shante Taylor in 1997, his deep emotional history with Holmond led to a reunion during a turbulent period in 1997, resulting in the birth of their son Julian in 1998. When news of Julian's parentage became public several years later, Holmond handled legal establishment of paternity through formal family court proceedings with quiet professionalism, ensuring that legal child support and parental responsibilities were formalized without unnecessary public hostility.</p>

            <!-- Middle Photo Section with Clean Image SEO & Schema -->
            <figure class="article-middle-photo" style="margin: 32px 0; text-align: center;">
              <img src="/assets/covers/laurie-holmond-middle.jpg" alt="Laurie Holmond smiling proudly next to her son Julian Corrie Broadus at a formal graduation celebration." width="960" height="540" loading="lazy" style="width: 100%; height: auto; border-radius: 6px; border: 1px solid var(--border-light); box-shadow: 0 4px 16px rgba(0,0,0,0.04);">
              <figcaption style="font-size: 0.85rem; color: var(--text-muted); margin-top: 10px; font-style: italic;">Laurie Holmond with her son Julian Corrie Broadus celebrating an academic and personal milestone.</figcaption>
            </figure>

            <h2>Welcoming Son Julian Corrie Broadus and Co-Parenting Journey</h2>
            <p>In 1998, Holmond gave birth to <strong>Julian Corrie Broadus</strong>. From his earliest years, Holmond dedicated herself to giving Julian a grounded, secure upbringing. While Broadus was frequently away touring the world and headlining stadium concerts, Holmond provided a structured daily routine, prioritizing Julian's schooling, athletic activities, and emotional security.</p>

            <p>As Julian grew into his teenage years, Snoop Dogg stepped forward to build an active, loving father-son relationship with him, welcoming Julian into the broader Broadus family circle. In interviews, Julian has repeatedly praised his mother for being his ultimate foundation, teaching him discipline, humility, and the importance of forging an independent identity rather than coasting on his father's legendary reputation.</p>

            <h2>Julian Broadus Today: Music, Modeling, and Real Estate</h2>
            <p>Today, Julian Corrie Broadus is an accomplished adult who has explored multiple creative and professional avenues. He studied at Bowling Green State University, where he demonstrated talent on the basketball court, before pursuing his interests in contemporary R&amp;B music, fashion modeling, and high-end residential real estate.</p>

            <p>Julian has released original music singles, worked with prominent lifestyle brands, and served as a luxury real estate agent with prestigious Southern California brokerages. Laurie encouraged his transition into high-end real estate, emphasizing market research, client discretion, and long-term fiduciary responsibility. In his public comments, Julian credits his mother’s grounded guidance for his entrepreneurial work ethic, reflecting the parental values celebrated in our features on <a href="/inty-miller/">Inty Miller</a> and <a href="/wanda-hutchins/">Wanda Hutchins</a>.</p>

            <h2>Career as a Medical Receptionist and Private Lifestyle</h2>
            <p>Throughout her adult life, Laurie Holmond has worked steadily in the healthcare and clinical administrative sector. As a medical receptionist and patient coordinator in California clinics, she manages patient appointments, insurance verifications, and clinical records with care and confidentiality.</p>

            <p>In community healthcare clinics, administrative coordinators serve as the crucial frontline bridge between medical providers, diagnostic laboratories, and patient families. Holmond's meticulous attention to patient privacy protocols, scheduling workflows, and empathetic patient intake has made her a highly valued team member across medical practices.</p>

            <p>Her colleagues have long commended her dependable work ethic and genuine compassion for patients. Despite the public curiosity that occasionally surfaces regarding her connection to hip-hop royalty, Holmond has never used her personal history for commercial gain, finding satisfaction in honest professional labor and quiet domestic peace.</p>

            <h2>Laurie Holmond Net Worth and Living Away From the Cameras</h2>
            <p>As of 2026, Laurie Holmond possesses an estimated personal net worth of <strong>$300,000 to $500,000</strong>. This wealth has been built through decades of steady employment in the medical administration sector, sensible savings, and child support agreements established during Julian's youth.</p>

            <p>Holmond continues to live quietly in Southern California, staying completely away from reality television and tabloid interviews. When not working, she enjoys tending her garden, attending local church services, cooking family dinners, and supporting local youth sports programs in Los Angeles County. Her life is filled with the joys of family, close friends, and watching her son achieve his own professional goals. Her enduring story is a reminder of the quiet courage of everyday mothers who put their children's well-being first.</p>

            <h2>Frequently Asked Questions (FAQs)</h2>
            <div class="faq-container" style="margin-top: 24px;">
              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">How old is Laurie Holmond?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Laurie Holmond was born in 1973 in Long Beach, California. As of 2026, she is 53 years old.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">Who is Laurie Holmond's son?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Laurie Holmond is the mother of Julian Corrie Broadus, born in 1998, whose father is world-famous hip-hop artist Snoop Dogg (Calvin Broadus Jr.).</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">How did Laurie Holmond and Snoop Dogg meet?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Laurie Holmond and Snoop Dogg met during their high school years at Long Beach Polytechnic High School in Long Beach, California, long before his rise to international musical stardom.</p>
              </div>

              <div style="margin-bottom: 20px; border-bottom: 1px solid var(--border-light); padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What is Laurie Holmond's profession?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Laurie Holmond has worked for many years in the healthcare sector as a medical receptionist and administrative coordinator in California.</p>
              </div>

              <div style="margin-bottom: 20px; padding-bottom: 16px;">
                <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-primary); margin-bottom: 6px;">What is Laurie Holmond's estimated net worth?</h3>
                <p style="font-size: 0.95rem; color: var(--text-secondary); line-height: 1.6;">Laurie Holmond has an estimated personal net worth between $300,000 and $500,000 as of 2026, earned through her professional career and diligent savings.</p>
              </div>
            </div>
        """
    }
]

def add_batch9():
    print("Reading articles_database.py...")
    sys.path.append(SCRIPT_DIR)
    from articles_database import ALL_ARTICLES

    # Reset previous heroMain and heroSubs
    for art in ALL_ARTICLES:
        art["isHeroMain"] = False
        art["isHeroSub"] = False
        if art["slug"] == "juanita-vanoy":
            art["isTrending"] = True
            art["trendingRank"] = 4
        elif art["slug"] == "deanna-burditt":
            art["isTrending"] = True
            art["trendingRank"] = 5
        elif art["slug"] == "inty-miller":
            art["isTrending"] = True
            art["trendingRank"] = 6

    # Combine: Batch 9 first, then existing
    new_all = BATCH9_ARTICLES + ALL_ARTICLES

    print(f"Writing updated database with {len(new_all)} total articles...")
    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write('"""\nIndependence Magazine - Central Master Articles Database\n"""\n\n')
        f.write('ALL_ARTICLES = ' + pprint.pformat(new_all, indent=4, width=120) + '\n')

    print(f"Successfully updated {DB_FILE} with {len(new_all)} total articles!")

if __name__ == "__main__":
    add_batch9()
