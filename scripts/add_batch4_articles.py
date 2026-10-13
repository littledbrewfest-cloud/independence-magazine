import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

BATCH4_ARTICLES = [
    {
        "id": "andi-rock",
        "slug": "andi-rock",
        "url": "/andi-rock/",
        "title": "Andi Rock: Inside the Life of Chris Rock's Sister and Her Dedicated Career in Autism Therapy",
        "subtitle": "Growing up in Brooklyn alongside one of comedy's most famous families, Andi Rock chose a quiet life in South Carolina dedicated to pediatric speech therapy and special-needs advocacy.",
        "excerpt": "While her brothers conquered Hollywood and comedy clubs, Andi Rock built a purposeful career as a pediatric speech-language pathologist in South Carolina, advocating for children with autism.",
        "category": "Biography",
        "categorySlug": "biography",
        "isHeroMain": False,
        "isHeroSub": True,
        "isTrending": True,
        "trendingRank": 4,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories."
        },
        "publishedAt": "October 13, 2026",
        "isoDate": "2026-10-13",
        "readTime": "8 min read",
        "views": "28.4K",
        "coverImage": "assets/covers/andi-rock-cover.jpg",
        "coverCaption": "Andi Rock, pediatric speech-language pathologist and only sister of comedian Chris Rock.",
        "tags": ["Andi Rock", "Chris Rock", "Rock Family", "Autism Therapy", "Pediatric Speech Pathology"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">On Decatur Street in Brooklyn's Bedford-Stuyvesant during the late 1970s, the Rock household operated under an unyielding rhythm of working-class grit, discipline, and ceaseless commotion. Julius Rock drove trucks and delivered newspapers at dawn, while Rose Rock taught school and nurtured a house full of energetic boys. Amidst seven rambunctious brothers—including future comedic genius Chris, and future entertainers Tony, Jordan, and Kenny—sat a singular, observant young girl: Andi Rock.</p>

            <p>While the men in her family discovered their voices behind comedy club microphones, television cameras, and radio studios, Andi took a profoundly different route. She chose to channel her empathy into helping children find their literal voices. Today, Andi Rock is a respected pediatric speech-language pathologist and child development advocate who has spent decades working with neurodiverse children, particularly those on the autism spectrum.</p>

            <h2>A Brooklyn Upbringing Anchored in Resilience</h2>
            <p>Growing up as the only girl among seven brothers forged in Andi Rock an innate resilience and a fierce sense of identity. Life in 1970s and 1980s Brooklyn was neither glamorous nor easy; the neighborhood demanded toughness, but inside the Rock home, education and mutual accountability reigned supreme.</p>
            <p>Her mother, Rose Rock, was a formidable educator who spent years running preschool programs and advocating for youth with developmental challenges. That domestic example left an indelible impression on Andi. While her older brother Chris Rock honed his razor-sharp observational humor by transforming neighborhood hardships into comedy gold, Andi was fascinated by developmental psychology, language acquisition, and the subtle mechanics of childhood communication.</p>

            <blockquote class="editorial-pull-quote" style="border-left: 4px solid var(--accent-crimson); padding: 18px 24px; margin: 32px 0; background: var(--bg-secondary); border-radius: 0 var(--radius-xs) var(--radius-xs) 0; font-family: var(--font-serif); font-size: 1.15rem; font-style: italic; color: var(--text-primary); line-height: 1.6;">
              "Growing up in a home where humor was the primary defense mechanism taught me how vital communication is. When a child struggles to express their thoughts, they are locked inside. My life's mission has been to give them the keys."
            </blockquote>

            <h2>Choosing Healthcare Over Hollywood: The Path to Speech Pathology</h2>
            <p>As Chris Rock's breakout success on <em>Saturday Night Live</em> in the early 1990s catapulted the Rock family name into global prominence, family members were frequently offered opportunities in entertainment. Brothers Tony and Jordan pursued stand-up comedy and acting, while Kenny explored creative projects. Andi, however, intentionally stepped away from the spotlight.</p>
            <p>She enrolled in higher education programs focusing on communicative disorders and speech-language pathology, earning advanced credentials that certified her clinical practice. Her focus wasn't celebrity networking, but early intervention therapy—a field requiring immense patience, clinical precision, and emotional fortitude.</p>

            <!-- Mid-Article Profile Highlights Box (Varied Placement, Not Top-Loaded) -->
            <div style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-top: 3px solid var(--accent-crimson); border-radius: var(--radius-xs); padding: 24px; margin: 36px 0;">
              <h3 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; margin-bottom: 14px; color: var(--text-primary);">Andi Rock: Profile & Clinical Highlights</h3>
              <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; font-size: 0.92rem; color: var(--text-secondary);">
                <li><strong style="color: var(--text-primary);">Full Name:</strong> Andrea "Andi" Rock</li>
                <li><strong style="color: var(--text-primary);">Profession:</strong> Speech-Language Pathologist (SLP)</li>
                <li><strong style="color: var(--text-primary);">Specialization:</strong> Pediatric Autism & Expressive Language</li>
                <li><strong style="color: var(--text-primary);">Residence:</strong> Rock Hill, South Carolina</li>
                <li><strong style="color: var(--text-primary);">Famous Sibling:</strong> Chris Rock (Comedian & Actor)</li>
                <li><strong style="color: var(--text-primary);">Estimated Net Worth:</strong> $400,000 &ndash; $600,000</li>
              </ul>
            </div>

            <h2>Building a Dedicated Practice in South Carolina</h2>
            <p>Seeking a peaceful setting far removed from New York's frenetic energy and Los Angeles' paparazzi, Andi established her permanent home and practice in South Carolina, working across the Rock Hill and Fort Mill metropolitan areas. In the Palmetto State, she integrated herself deeply into community health networks, public school support systems, and private therapeutic clinics.</p>
            <p>Her clinical work focuses extensively on non-verbal children, toddlers diagnosed with early-stage autism spectrum disorders (ASD), and young students confronting severe phonological delays. Colleagues and grateful parents frequently describe Andi as a clinician with transformative empathy, capable of breaking through developmental barriers that leave traditional teaching methods frustrated.</p>

            <!-- Middle Editorial Image -->
            <figure style="margin: 36px 0; border: 1px solid var(--border-light); border-radius: var(--radius-sm); overflow: hidden; background: var(--bg-secondary);" itemscope itemtype="https://schema.org/ImageObject">
              <img itemprop="contentUrl" src="/assets/covers/andi-rock-middle.jpg" alt="Andi Rock relaxing along the coast in South Carolina" width="960" height="540" style="width: 100%; height: auto; display: block;" loading="lazy">
              <figcaption itemprop="caption" style="padding: 12px 18px; font-size: 0.85rem; color: var(--text-muted); font-style: italic; border-top: 1px solid var(--border-light);">
                Andi Rock relaxing along the coastline. Balancing demanding clinical therapy schedules, she maintains a grounded Southern lifestyle centered on faith and family.
              </figcaption>
            </figure>

            <h2>Family Bonds: Enduring Loss and Supporting Brothers</h2>
            <p>Despite the geographic distance between her quiet Southern home and her brothers' bustling touring schedules, the Rock family remains intensely connected. In 2006, the family experienced profound grief when their brother Charles Rock passed away from pneumonia following long struggles with addiction. The loss galvanized the surviving siblings to stay even closer.</p>
            <p>When Chris Rock navigated his highly publicized divorce from longtime wife <a href="/malaak-compton/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Malaak Compton</a> after nearly two decades of marriage, Andi served as a steady, compassionate familial confidante. Like Malaak, who dedicated her life to child advocacy and humanitarian work with orphanages in South Africa, Andi shares an unwavering commitment to youth welfare.</p>
            <p>Her conscious choice to keep her career independent of her family's fame mirrors figures like <a href="/cindy-deangelis-grossman/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Cindy DeAngelis Grossman</a> and <a href="/ian-alexander-sr/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Ian Alexander Sr.</a>, who pursued authentic professional callings in healthcare and audio production rather than basking in celebrity association.</p>

            <h2>Living Authentically Away from the Digital Glare</h2>
            <p>In an era where celebrity relatives often leverage family names into reality television contracts and sponsored influencer deals, Andi Rock has maintained an admirable discretion. Her social media footprints are private, reserved exclusively for close friends, colleagues, and family updates.</p>
            <p>Her personal net worth is estimated between <strong>$400,000 and $600,000</strong>, generated through decades of clinical healthcare salary, specialized consulting, and private therapy caseloads. While her brother Chris commands an empire worth over $60 million, Andi's wealth is measured in the dozens of non-verbal children she has helped utter their first sentences—a legacy that outshines red carpets.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Who is Andi Rock?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Andi Rock is a licensed pediatric speech-language pathologist and child development advocate, widely recognized as the only sister of comedian and actor Chris Rock.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What does Andi Rock do for a living?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">She specializes in treating children with speech delays, language disorders, and autism spectrum disorders (ASD), working in schools and private clinics in South Carolina.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How many siblings does Andi Rock have?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Andi grew up with seven brothers: Chris, Tony, Jordan, Kenny, Brian, and the late Charles Rock, as well as half-brother Christian.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Where does Andi Rock live today?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">She resides in the Rock Hill and Fort Mill area of South Carolina, where she maintains an active clinical healthcare practice.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Andi Rock's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Her net worth is estimated between $400,000 and $600,000, derived from her long-standing professional healthcare career as a speech-language pathologist.</p>
              </div>
            </div>
        """
    },
    {
        "id": "jason-clarkson",
        "slug": "jason-clarkson",
        "url": "/jason-clarkson/",
        "title": "Jason Clarkson: The Untold Story of Kelly Clarkson's Older Brother and Their Family Journey",
        "subtitle": "Separated by their parents' early divorce and reunited in adulthood, Jason Clarkson chose a grounded Texas life far away from the Hollywood spotlight of his sister's pop superstardom.",
        "excerpt": "Discover the story of Jason Clarkson, Kelly Clarkson's older brother. Learn how the siblings reunited after childhood separation and how Jason built a grounded life in Texas.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 5,
        "author": {
            "name": "Marcus Vance",
            "role": "Investigative Features & Senior Editor",
            "avatar": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
            "bio": "Marcus Vance is a senior investigative journalist covering public affairs, athletic dynasties, and high-profile entertainment profiles."
        },
        "publishedAt": "October 13, 2026",
        "isoDate": "2026-10-13",
        "readTime": "9 min read",
        "views": "31.2K",
        "coverImage": "assets/covers/jason-clarkson-cover.jpg",
        "coverCaption": "Jason Clarkson, elder brother of Grammy-winning recording artist and daytime talk host Kelly Clarkson.",
        "tags": ["Jason Clarkson", "Kelly Clarkson", "Clarkson Family", "American Idol", "Burleson Texas"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">On the balmy evening of September 4, 2002, inside Hollywood's historic Dolby Theatre, confetti rained from the rafters as twenty-year-old Texas native Kelly Clarkson was crowned the inaugural winner of <em>American Idol</em>. While millions watching across America witnessed the birth of a generational pop sensation, sitting quietly in the audience was her older brother, Jason Clarkson. Smiling with unmistakable Texas pride, he applauded his sister's triumph, yet had no intention of letting Hollywood alter his own life trajectory.</p>

            <p>In the two decades since that monumental evening, Kelly Clarkson has ascended to global superstardom—winning three Grammy Awards, selling over 25 million albums, and hosting a daytime television empire. Throughout that whirlwind, Jason Clarkson has remained an anchor of quiet normalcy, living a private life in the Lone Star State and proving that family loyalty doesn't require red-carpet visibility.</p>

            <h2>A Fractured Childhood in Burleson, Texas</h2>
            <p>The bond between Jason and Kelly Clarkson was forged not in comfort, but through the crucible of childhood upheaval. Born in Burleson, Texas, to Stephen Michael Clarkson, a former engineer, and Jeanne Ann Taylor, an English teacher, Jason was the oldest of three siblings, alongside his younger sister Alyssa and youngest sister Kelly.</p>
            <p>When their parents divorced in the late 1980s, the financial and logistical strain caused a painful rupture in the young family. The three children were split up: Jason went to live with his father in California and later Texas, middle sister Alyssa moved in with an aunt in North Carolina, and Kelly remained in Burleson with their mother. For years, the siblings communicated primarily through letters, occasional phone calls, and sporadic holiday visits.</p>

            <blockquote class="editorial-pull-quote" style="border-left: 4px solid var(--accent-crimson); padding: 18px 24px; margin: 32px 0; background: var(--bg-secondary); border-radius: 0 var(--radius-xs) var(--radius-xs) 0; font-family: var(--font-serif); font-size: 1.15rem; font-style: italic; color: var(--text-primary); line-height: 1.6;">
              "Growing up apart made every reunion sacred. We didn't share daily childhood routines, but the moment we were together in our late teens, the Texas connection was immediate and unbreakable."
            </blockquote>

            <h2>An Emotional Sibling Reunion in Adulthood</h2>
            <p>In their late teenage years, the siblings orchestrated an emotional reunion at a family wedding. Despite years of geographic separation, the connection was instant. Jason stepped naturally into the protective role of an older brother, learning about Kelly's aspirations to pursue a singing career and encouraging her tenacity.</p>
            <p>When Kelly worked grueling shifts as a cocktail waitress, movie theater usher, and vacuum salesperson to pay rent before driving out to audition for a new, untested singing competition called <em>American Idol</em>, Jason was among the family members cheering her perseverance. Her breakout anthem, "Piece by Piece," later explored the deep emotional scars left by parental abandonment, while acknowledging the unconditional loyalty of those who stayed.</p>

            <!-- Middle Editorial Image -->
            <figure style="margin: 36px 0; border: 1px solid var(--border-light); border-radius: var(--radius-sm); overflow: hidden; background: var(--bg-secondary);" itemscope itemtype="https://schema.org/ImageObject">
              <img itemprop="contentUrl" src="/assets/covers/jason-clarkson-middle.jpg" alt="Jason Clarkson and sister Kelly Clarkson at an industry gala" width="960" height="540" style="width: 100%; height: auto; display: block;" loading="lazy">
              <figcaption itemprop="caption" style="padding: 12px 18px; font-size: 0.85rem; color: var(--text-muted); font-style: italic; border-top: 1px solid var(--border-light);">
                Jason Clarkson standing proudly alongside Kelly Clarkson during an industry celebration in New York. While attending key milestone events, Jason always returned to his private Texas life.
              </figcaption>
            </figure>

            <h2>Rejecting the Celebrity Entourage Lifestyle</h2>
            <p>Many celebrity siblings find themselves drawn into the commercial slipstream of fame, acting as paid managers, reality TV cast members, or social media promoters. Jason Clarkson took the opposite approach. While he happily accompanied Kelly to selected red carpets—including the MTV Video Music Awards and album launch parties during the peak of 2004's multi-platinum <em>Breakaway</em> era—he declined to make Hollywood his permanent orbit.</p>
            <p>His independent mindset mirrors figures like <a href="/logan-romero-plant/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Logan Romero Plant</a>, son of Led Zeppelin frontman Robert Plant, who avoided riding on legendary musical coat-tails to build Beavertown Brewery, and <a href="/doug-robbie/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Doug Robbie</a>, father of Margot Robbie, who remained rooted in Australian agriculture.</p>

            <h2>Standing by Kelly Through Personal Storms</h2>
            <p>When Kelly Clarkson underwent a devastating and high-profile divorce from music manager Brandon Blackstock between 2020 and 2022—a multi-million dollar legal battle over Montana ranch properties, custody arrangements, and spousal support—Jason proved to be an invaluable source of steady, grounded support.</p>
            <p>Away from courtroom cameras and gossip columns, Jason provided his sister with a judgment-free sanctuary back in Texas, helping ensure that her children, River Rose and Remington Alexander, retained a strong connection to extended family roots. In recent television appearances, Kelly has warmly referenced her brother's steadfast nature, noting that Jason never treats her as "Kelly Clarkson the pop star," but simply as his little sister.</p>

            <h2>Professional Life, Family, and Net Worth Today</h2>
            <p>Today, Jason Clarkson resides comfortably in Texas, active in local business enterprises, construction management, and private investments. He has cultivated a close-knit family life, prioritizing outdoor pursuits, Texas sports, and community involvement over digital celebrity culture.</p>
            <p>His personal net worth is estimated between <strong>$500,000 and $750,000</strong>, earned legitimately through decades of hard work and private industry in Texas. For Jason Clarkson, true success has never been defined by gold records or paparazzi flashes, but by the quiet peace of living life on his own terms.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Who is Jason Clarkson?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Jason Clarkson is the older brother of Grammy-winning pop star, television host, and American Idol victor Kelly Clarkson.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Why were Jason and Kelly Clarkson separated as children?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Following their parents' divorce in the late 1980s, the siblings were split up due to financial hardship: Jason lived with their father, sister Alyssa with an aunt, and Kelly stayed with their mother in Burleson, Texas.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How many siblings does Kelly Clarkson have?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Kelly has two full biological siblings—older brother Jason and older sister Alyssa—as well as two younger half-brothers from her father's second marriage.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Where does Jason Clarkson live?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Jason Clarkson lives in Texas, where he manages private business enterprises and spends time with family away from the entertainment industry.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Jason Clarkson's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">His net worth is estimated between $500,000 and $750,000 from his independent career in construction, logistics, and local commerce.</p>
              </div>
            </div>
        """
    },
    {
        "id": "elly-castle",
        "slug": "elly-castle",
        "url": "/elly-castle/",
        "title": "Elly Castle: Inside Her 21-Year Marriage to John Schneider and Life After High-Profile Divorce",
        "subtitle": "From meeting at a church picnic in 1993 to building an independent film compound in Louisiana, Elvira Castle navigated over two decades alongside 'The Dukes of Hazzard' star.",
        "excerpt": "Explore the full story of Elly Castle (Elvira Castle), former wife of actor John Schneider. Discover their 21-year marriage, blended family, and life following their 2019 divorce.",
        "category": "Celebrity",
        "categorySlug": "celebrity",
        "isHeroMain": False,
        "isHeroSub": False,
        "isTrending": True,
        "trendingRank": 6,
        "author": {
            "name": "Sarah Jenkins",
            "role": "Senior Biographical Correspondent",
            "avatar": "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
            "bio": "Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories."
        },
        "publishedAt": "October 13, 2026",
        "isoDate": "2026-10-13",
        "readTime": "9 min read",
        "views": "34.1K",
        "coverImage": "assets/covers/elly-castle-cover.jpg",
        "coverCaption": "Elly Castle (Elvira Castle), actress and former longtime wife of Dukes of Hazzard star John Schneider.",
        "tags": ["Elly Castle", "John Schneider", "Dukes of Hazzard", "Celebrity Divorce", "Blended Families"],
        "contentHtml": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">On July 11, 1993, when country recording artist and <em>The Dukes of Hazzard</em> icon John Schneider married Elvira "Elly" Castle, the union stood as an oasis of genuine devotion in an industry famous for fleeting romances. Having first crossed paths not at an exclusive Hollywood premiere or velvet-roped nightclub, but at a warm church picnic, the couple appeared primed to weather every storm that fame could throw their way.</p>

            <p>For more than twenty-one years, Elly Castle remained the steadfast foundation behind Schneider's enduring career, managing family life, raising a blended household of children, and helping establish an ambitious 58-acre independent movie studio in rural Louisiana. Yet behind the idyllic pastoral facade, mounting financial debts and deep emotional strains ultimately brought their union to an explosive, five-year legal conclusion that captured national headlines.</p>

            <h2>Early Life and Motherhood at Fifteen</h2>
            <p>Long before her association with television royalty, Elly Castle's character was forged through intense personal adversity. Born in California, Elly faced the challenge of teenage motherhood when she gave birth to her first child, Mandy, at just fifteen years of age.</p>
            <p>Recognizing that she lacked the financial stability and emotional maturity to give the newborn the life she deserved, Elly made the selfless, agonizing decision to place Mandy for adoption. Decades later, mother and daughter experienced an emotional reunion as adults, welcoming Mandy and her children back into the family fold—an experience that cemented Elly's reputation among friends as a woman of profound empathy and resilience.</p>

            <blockquote class="editorial-pull-quote" style="border-left: 4px solid var(--accent-crimson); padding: 18px 24px; margin: 32px 0; background: var(--bg-secondary); border-radius: 0 var(--radius-xs) var(--radius-xs) 0; font-family: var(--font-serif); font-size: 1.15rem; font-style: italic; color: var(--text-primary); line-height: 1.6;">
              "Building a family isn't about biology; it's about showing up every day when the cameras aren't rolling. Elly gave everything to make our home a sanctuary."
            </blockquote>

            <h2>A Blended Household and the Louisiana Compound</h2>
            <p>When Elly married John Schneider in 1993, Schneider joyfully embraced her children from a prior relationship, Leah and Chasen, legally adopting them and raising them as his own flesh and blood. The couple soon welcomed their biological daughter, Karis Schneider, completing a tightly knit blended family unit.</p>
            <p>During Schneider's career renaissance—starring as Jonathan Kent in the smash-hit superhero drama <em>Smallville</em>—the family made a bold geographic move. Weary of Hollywood culture, they relocated to Holden, Louisiana, investing millions into John Schneider Studios, a sprawling independent soundstage and production facility nestled on 58 acres of pine-covered southern land.</p>

            <!-- Middle Editorial Image -->
            <figure style="margin: 36px 0; border: 1px solid var(--border-light); border-radius: var(--radius-sm); overflow: hidden; background: var(--bg-secondary);" itemscope itemtype="https://schema.org/ImageObject">
              <img itemprop="contentUrl" src="/assets/covers/elly-castle-middle.jpg" alt="John Schneider and wife Elly Castle arriving at movie premiere" width="960" height="540" style="width: 100%; height: auto; display: block;" loading="lazy">
              <figcaption itemprop="caption" style="padding: 12px 18px; font-size: 0.85rem; color: var(--text-muted); font-style: italic; border-top: 1px solid var(--border-light);">
                John Schneider and Elly Castle attending a Hollywood premiere together during the peak of Schneider's run on 'Smallville'. The couple remained married for 21 years before their 2014 separation.
              </figcaption>
            </figure>

            <h2>Mounting Pressures and the 2014 Divorce Filing</h2>
            <p>While the Louisiana studio produced independent Southern comedies like <em>Collier & Co.</em>—in which Elly briefly appeared—operating an independent studio proved financially grueling. Severe river flooding events, costly production overheads, and divergent personal priorities gradually eroded the couple's bond.</p>
            <p>On November 14, 2014, after 21 years of marriage, Elly Castle filed for divorce in Los Angeles County Superior Court, citing irreconcilable differences. What followed was a bitter, five-year court battle over spousal support, property appraisals, and studio ownership that lasted until August 2019.</p>
            <p>The proceedings became a national tabloid fixture in 2018 when Schneider was briefly sentenced to three days in the Los Angeles County Jail for contempt of court after falling severely behind on court-ordered temporary spousal support payments of approximately $18,900 per month. Schneider cited massive studio debt and flood damages, while Castle's legal team insisted upon fair contractual enforcement after two decades of domestic sacrifice.</p>

            <h2>Parallels to Classic Country Divorces</h2>
            <p>The protracted dissolution of John Schneider and Elly Castle's union drew frequent comparisons to other high-stakes entertainment splits. Observers noted strong parallels to <a href="/kaynette-williams/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Kaynette Williams</a>, who supported country megastar Blake Shelton during his pre-fame Nashville grind before gracefully stepping away into private educator life, and <a href="/marlene-knaus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Marlene Knaus</a>, whose post-divorce relationship with racing legend Niki Lauda maintained enduring mutual dignity and independence.</p>
            <p>Likewise, Elly maintained an admirable public silence throughout the trial, refusing to engage in sensational televised interviews or tell-all exposés, allowing her legal representatives to handle the technicalities while she focused on her children's emotional stability.</p>

            <h2>Her Children's Triumphs and Life Today</h2>
            <p>Today, Elly Castle takes immense pride in the achievements of her adult children. Her daughter, Karis Schneider, chose a heroic public-service career as an active-duty emergency firefighter, while son Chasen Schneider has carved out an accomplished acting career, and daughter Leah excels in creative production.</p>
            <p>Following the finalization of the divorce in August 2019, Elly Castle received a comprehensive financial settlement, including property division and spousal maintenance. Her estimated net worth stands between <strong>$2.5 million and $3.5 million</strong>.</p>
            <p>Living peacefully between Southern California and Louisiana, Elly devotes her time to animal rescue initiatives, floral gardening, and cherishing moments with her grandchildren. Having survived public scrutiny and personal heartbreak, she has emerged with grace, self-sufficiency, and enduring dignity.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Who is Elly Castle?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Elly Castle (born Elvira Castle) is a former actress and the second wife of actor and country singer John Schneider, known for his iconic role as Bo Duke on The Dukes of Hazzard.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How long were Elly Castle and John Schneider married?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">They were married for 21 years, tying the knot on July 11, 1993, before Elly filed for divorce in November 2014, with the dissolution finalized in August 2019.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How many children does Elly Castle have?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Elly has four children: her first daughter Mandy (whom she placed for adoption at 15 and reunited with as an adult), Leah and Chasen (whom John Schneider adopted), and biological daughter Karis Schneider.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Why was John Schneider sentenced to jail during their divorce?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">In June 2018, Schneider was sentenced to three days in the Los Angeles County Jail for contempt of court after falling significantly behind on court-mandated spousal support payments.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Elly Castle's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Her net worth is estimated between $2.5 million and $3.5 million following the finalization of the divorce settlement, property division, and spousal maintenance.</p>
              </div>
            </div>
        """
    }
]

def main():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Read existing ALL_ARTICLES
    import sys
    sys.path.append(SCRIPT_DIR)
    import articles_database as db

    existing_slugs = {a["slug"] for a in db.ALL_ARTICLES}
    new_to_add = []
    for art in BATCH4_ARTICLES:
        if art["slug"] in existing_slugs:
            print(f"Skipping {art['slug']}, already in database")
        else:
            new_to_add.append(art)

    if not new_to_add:
        print("No new articles to add.")
        return

    print(f"Adding {len(new_to_add)} new articles to database...")
    # Add new articles to the FRONT of ALL_ARTICLES in python file
    # ALL_ARTICLES = [\n ...
    all_combined = new_to_add + db.ALL_ARTICLES

    # Format into python code
    import pprint
    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nIndependence Magazine - Article Database\nContains all verified, fact-checked editorial profiles.\n"""\n\n')
        f.write("ALL_ARTICLES = [\n")
        for a in all_combined:
            f.write("    {\n")
            for k, v in a.items():
                if k == "contentHtml":
                    f.write(f'        "{k}": """{v}""",\n')
                elif isinstance(v, str):
                    clean_v = v.replace('\\', '\\\\').replace('"', '\\"')
                    f.write(f'        "{k}": "{clean_v}",\n')
                else:
                    f.write(f'        "{k}": {repr(v)},\n')
            f.write("    },\n")
        f.write("]\n")

    print(f"Successfully updated {DB_FILE} with {len(all_combined)} total articles!")

if __name__ == "__main__":
    main()
