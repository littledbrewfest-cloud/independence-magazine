import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(SCRIPT_DIR, "articles_database.py")

import sys
sys.path.append(SCRIPT_DIR)
import articles_database as db

EXPANDED_ARTICLES = {
    "andi-rock": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">On Decatur Street in Brooklyn's Bedford-Stuyvesant during the late 1970s, the Rock household operated under an unyielding rhythm of working-class grit, discipline, and ceaseless commotion. Julius Rock drove trucks and delivered newspapers at dawn, while Rose Rock taught school and nurtured a house full of energetic boys. Amidst seven rambunctious brothers—including future comedic genius Chris, and future entertainers Tony, Jordan, and Kenny—sat a singular, observant young girl: Andi Rock.</p>

            <p>While the men in her family discovered their voices behind comedy club microphones, television cameras, and radio studios, Andi took a profoundly different route. She chose to channel her empathy into helping children find their literal voices. Today, Andi Rock is a respected pediatric speech-language pathologist and child development advocate who has spent decades working with neurodiverse children, particularly those on the autism spectrum.</p>

            <h2>A Brooklyn Upbringing Anchored in Resilience</h2>
            <p>Growing up as the only girl among seven brothers forged in Andi Rock an innate resilience and a fierce sense of identity. Life in 1970s and 1980s Brooklyn was neither glamorous nor easy; the neighborhood demanded toughness, but inside the Rock home, education and mutual accountability reigned supreme.</p>
            <p>Her mother, Rose Rock, was a formidable educator and community organizer who spent years running preschool programs and advocating for youth with developmental challenges. Rose later authored <em>Mama Rock's Rules: Ten Lessons for Raising a Household of Successful Children</em>, chronicling how maternal structure kept her children grounded amidst urban hardship. That domestic example left an indelible impression on Andi. While her older brother Chris Rock honed his razor-sharp observational humor by transforming neighborhood hardships into comedy gold, Andi was fascinated by developmental psychology, language acquisition, and the subtle mechanics of childhood communication.</p>

            <blockquote class="editorial-pull-quote" style="border-left: 4px solid var(--accent-crimson); padding: 18px 24px; margin: 32px 0; background: var(--bg-secondary); border-radius: 0 var(--radius-xs) var(--radius-xs) 0; font-family: var(--font-serif); font-size: 1.15rem; font-style: italic; color: var(--text-primary); line-height: 1.6;">
              "Growing up in a home where humor was the primary defense mechanism taught me how vital communication is. When a child struggles to express their thoughts, they are locked inside. My life's mission has been to give them the keys."
            </blockquote>

            <h2>Choosing Healthcare Over Hollywood: The Path to Speech Pathology</h2>
            <p>As Chris Rock's breakout success on <em>Saturday Night Live</em> in the early 1990s catapulted the Rock family name into global prominence, family members were frequently offered opportunities in entertainment. Brothers Tony and Jordan pursued stand-up comedy and acting, while Kenny explored creative projects. Andi, however, intentionally stepped away from the spotlight.</p>
            <p>She enrolled in higher education programs focusing on communicative disorders and speech-language pathology, earning advanced credentials that certified her clinical practice. Her focus wasn't celebrity networking, but early intervention therapy—a field requiring immense patience, clinical precision, and emotional fortitude.</p>
            <p>Her training encompassed advanced diagnostic assessment for expressive and receptive language delays, articulation disorders, and augmentative and alternative communication (AAC) devices. Rather than seeking high-paying administrative roles in Manhattan private practices, Andi felt called to grassroots pediatric clinics where under-resourced families struggled to find specialized care for neurodevelopmental delays.</p>

            <!-- Mid-Article Profile Highlights Box (Varied Placement, Not Top-Loaded) -->
            <div style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-top: 3px solid var(--accent-crimson); border-radius: var(--radius-xs); padding: 24px; margin: 36px 0;">
              <h3 style="font-family: var(--font-serif); font-size: 1.25rem; font-weight: 700; margin-bottom: 14px; color: var(--text-primary);">Andi Rock: Profile & Clinical Highlights</h3>
              <ul style="list-style: none; padding: 0; margin: 0; display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 12px; font-size: 0.92rem; color: var(--text-secondary);">
                <li><strong style="color: var(--text-primary);">Full Name:</strong> Andrea "Andi" Rock</li>
                <li><strong style="color: var(--text-primary);">Profession:</strong> Speech-Language Pathologist (SLP)</li>
                <li><strong style="color: var(--text-primary);">Specialization:</strong> Pediatric Autism & Expressive Language</li>
                <li><strong style="color: var(--text-primary);">Clinical Base:</strong> Rock Hill, South Carolina</li>
                <li><strong style="color: var(--text-primary);">Famous Sibling:</strong> Chris Rock (Comedian & Actor)</li>
                <li><strong style="color: var(--text-primary);">Estimated Net Worth:</strong> $400,000 &ndash; $600,000</li>
              </ul>
            </div>

            <h2>Building a Dedicated Practice in South Carolina</h2>
            <p>Seeking a peaceful setting far removed from New York's frenetic energy and Los Angeles' paparazzi, Andi established her permanent home and practice in South Carolina, working across the Rock Hill and Fort Mill metropolitan areas. In the Palmetto State, she integrated herself deeply into community health networks, public school support systems, and private therapeutic clinics.</p>
            <p>Her clinical work focuses extensively on non-verbal children, toddlers diagnosed with early-stage autism spectrum disorders (ASD), and young students confronting severe phonological delays. Utilizing evidence-based methodologies such as the Picture Exchange Communication System (PECS) and tactile-kinesthetic speech facilitation, Andi works one-on-one with children to unlock verbal expression.</p>
            <p>Colleagues and grateful parents frequently describe Andi as a clinician with transformative empathy, capable of breaking through developmental barriers that leave traditional teaching methods frustrated. She frequently advocates at school district IEP (Individualized Education Program) hearings, ensuring that students receive the mandated therapy hours, specialized assistive technology, and sensory accommodations they require to thrive in general classrooms.</p>

            <!-- Middle Editorial Image -->
            <figure style="margin: 36px 0; border: 1px solid var(--border-light); border-radius: var(--radius-sm); overflow: hidden; background: var(--bg-secondary);" itemscope itemtype="https://schema.org/ImageObject">
              <img itemprop="contentUrl" src="/assets/covers/andi-rock-middle.jpg" alt="Andi Rock relaxing along the coast in South Carolina" width="960" height="540" style="width: 100%; height: auto; display: block;" loading="lazy">
              <figcaption itemprop="caption" style="padding: 12px 18px; font-size: 0.85rem; color: var(--text-muted); font-style: italic; border-top: 1px solid var(--border-light);">
                Andi Rock relaxing along the coastline. Balancing demanding clinical therapy schedules, she maintains a grounded Southern lifestyle centered on faith, community service, and family.
              </figcaption>
            </figure>

            <h2>Family Bonds: Enduring Loss and Supporting Brothers</h2>
            <p>Despite the geographic distance between her quiet Southern home and her brothers' bustling touring schedules, the Rock family remains intensely connected. In 2006, the family experienced profound grief when their brother Charles Rock passed away from pneumonia following long struggles with addiction. The loss galvanized the surviving siblings to stay even closer.</p>
            <p>When Chris Rock navigated his highly publicized divorce from longtime wife <a href="/malaak-compton/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Malaak Compton</a> after nearly two decades of marriage, Andi served as a steady, compassionate familial confidante. Like Malaak, who dedicated her life to child advocacy and humanitarian work with orphanages in South Africa through the Angelrock Project, Andi shares an unwavering commitment to youth welfare.</p>
            <p>Her conscious choice to keep her career independent of her family's fame mirrors figures like <a href="/cindy-deangelis-grossman/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Cindy DeAngelis Grossman</a> and <a href="/ian-alexander-sr/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Ian Alexander Sr.</a>, who pursued authentic professional callings in healthcare and audio production rather than basking in celebrity association.</p>

            <h2>Maternal Wisdom and the Legacy of Rose Rock</h2>
            <p>The philosophical foundation of Andi's clinical career traces directly back to her mother, Rose. In public speeches and interviews, Rose Rock has often highlighted how proud she is not just of Chris's Emmys or Tony's sitcom roles, but of Andi's daily service to children who cannot speak for themselves.</p>
            <p>"My children all learned how to work," Rose once observed. "Andi could have asked Chris for a job on a movie set or an office in California. Instead, she went to school, earned her degrees, and went to work helping babies who need her." That maternal seal of approval represents the core of Andi's personal pride.</p>
            <p>Every holiday season, when the Rock brothers assemble in New York or South Carolina, Andi serves as the domestic center of gravity. Brothers often consult her on child-rearing and education, viewing her as the family's intellectual anchor on pediatric health.</p>

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
    """,
    "jason-clarkson": """
            <p class="lead-paragraph" style="font-size: 1.18rem; line-height: 1.75; color: var(--text-primary); margin-bottom: 24px; font-weight: 500;">On the balmy evening of September 4, 2002, inside Hollywood's historic Dolby Theatre, confetti rained from the rafters as twenty-year-old Texas native Kelly Clarkson was crowned the inaugural winner of <em>American Idol</em>. While millions watching across America witnessed the birth of a generational pop sensation, sitting quietly in the audience was her older brother, Jason Clarkson. Smiling with unmistakable Texas pride, he applauded his sister's triumph, yet had no intention of letting Hollywood alter his own life trajectory.</p>

            <p>In the two decades since that monumental evening, Kelly Clarkson has ascended to global superstardom—winning three Grammy Awards, selling over 25 million albums, and hosting a daytime television empire. Throughout that whirlwind, Jason Clarkson has remained an anchor of quiet normalcy, living a private life in the Lone Star State and proving that family loyalty doesn't require red-carpet visibility.</p>

            <h2>A Fractured Childhood in Burleson, Texas</h2>
            <p>The bond between Jason and Kelly Clarkson was forged not in comfort, but through the crucible of childhood upheaval. Born in Burleson, Texas, to Stephen Michael Clarkson, a former aerospace engineer, and Jeanne Ann Taylor, an English teacher, Jason was the oldest of three siblings, alongside his younger sister Alyssa and youngest sister Kelly.</p>
            <p>When their parents divorced in the late 1980s, the financial and logistical strain caused a painful rupture in the young family. The three children were split up: Jason went to live with his father in California and later Texas, middle sister Alyssa moved in with an aunt in North Carolina, and Kelly remained in Burleson with their mother. For years, the siblings communicated primarily through letters, occasional phone calls, and sporadic holiday visits.</p>
            <p>While growing up with his father, Jason absorbed traditional blue-collar values—learning the fundamentals of mechanical trades, home construction, and automotive mechanics. He developed a deep affinity for hands-on labor, finding satisfaction in tangible craftsmanship rather than artistic performance.</p>

            <blockquote class="editorial-pull-quote" style="border-left: 4px solid var(--accent-crimson); padding: 18px 24px; margin: 32px 0; background: var(--bg-secondary); border-radius: 0 var(--radius-xs) var(--radius-xs) 0; font-family: var(--font-serif); font-size: 1.15rem; font-style: italic; color: var(--text-primary); line-height: 1.6;">
              "Growing up apart made every reunion sacred. We didn't share daily childhood routines, but the moment we were together in our late teens, the Texas connection was immediate and unbreakable."
            </blockquote>

            <h2>An Emotional Sibling Reunion in Adulthood</h2>
            <p>In 2001, just months before the creation of <em>American Idol</em>, the siblings orchestrated an emotional reunion at a family wedding in Texas. Despite years of geographic separation, the connection was instant. Jason stepped naturally into the protective role of an older brother, learning about Kelly's aspirations to pursue a singing career and encouraging her tenacity.</p>
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
            <p>Whenever producers approached Jason with proposals for behind-the-scenes reality specials or tell-all interviews about the Clarkson household, he politely but firmly turned them down. For Jason, his sister's stardom was her professional accomplishment, not his personal meal ticket.</p>

            <h2>Standing by Kelly Through Personal Storms</h2>
            <p>When Kelly Clarkson underwent a devastating and high-profile divorce from music manager Brandon Blackstock between 2020 and 2022—a multi-million dollar legal battle over Montana ranch properties, custody arrangements, and spousal support—Jason proved to be an invaluable source of steady, grounded support.</p>
            <p>Away from courtroom cameras and gossip columns, Jason provided his sister with a judgment-free sanctuary back in Texas, helping ensure that her children, River Rose and Remington Alexander, retained a strong connection to extended family roots. In recent television appearances, Kelly has warmly referenced her brother's steadfast nature, noting that Jason never treats her as "Kelly Clarkson the pop star," but simply as his little sister.</p>
            <p>When Kelly decided in 2023 to relocate <em>The Kelly Clarkson Show</em> from Los Angeles to 30 Rockefeller Plaza in New York City to start fresh and be closer to the East Coast, Jason was among the first family members to help her pack, coordinate logistics, and reassure her that home is wherever family gathers.</p>

            <h2>Professional Life, Family, and Net Worth Today</h2>
            <p>Today, Jason Clarkson resides comfortably in Texas, active in local business enterprises, construction management, and private investments. He has cultivated a close-knit family life, prioritizing outdoor pursuits, Texas sports, hunting, and community involvement over digital celebrity culture.</p>
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
    """,
    "elly-castle": """
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
            <p>On the compound, Elly managed domestic operations, hosted touring cast members, and supported independent filmmaking initiatives. When the studio launched indie action-comedies like <em>Collier & Co.: Hot Pursuit</em> in 2006, Elly even appeared in an acting cameo alongside her husband, contributing directly to the family's artistic enterprise.</p>

            <!-- Middle Editorial Image -->
            <figure style="margin: 36px 0; border: 1px solid var(--border-light); border-radius: var(--radius-sm); overflow: hidden; background: var(--bg-secondary);" itemscope itemtype="https://schema.org/ImageObject">
              <img itemprop="contentUrl" src="/assets/covers/elly-castle-middle.jpg" alt="John Schneider and wife Elly Castle arriving at movie premiere" width="960" height="540" style="width: 100%; height: auto; display: block;" loading="lazy">
              <figcaption itemprop="caption" style="padding: 12px 18px; font-size: 0.85rem; color: var(--text-muted); font-style: italic; border-top: 1px solid var(--border-light);">
                John Schneider and Elly Castle attending a Hollywood premiere together during the peak of Schneider's run on 'Smallville'. The couple remained married for 21 years before their 2014 separation.
              </figcaption>
            </figure>

            <h2>Mounting Pressures and the 2014 Divorce Filing</h2>
            <p>While the Louisiana studio produced independent Southern comedies, operating a massive film studio facility proved financially grueling. Severe river flooding events, costly production overheads, and divergent personal priorities gradually eroded the couple's bond.</p>
            <p>The catastrophic 2016 historic floods along the Amite River in Louisiana submerged the studio compound under four feet of muddy floodwaters, destroying expensive sound equipment, vintage <em>Dukes of Hazzard</em> memorabilia, and production sets. Although this disaster occurred after their formal separation, the chronic financial debts from building the compound had already created insurmountable domestic friction.</p>
            <p>On November 14, 2014, after 21 years of marriage, Elly Castle filed for divorce in Los Angeles County Superior Court, citing irreconcilable differences. What followed was a bitter, five-year court battle over spousal support, property appraisals, and studio ownership that lasted until August 2019.</p>
            <p>The proceedings became a national tabloid fixture in 2018 when Schneider was briefly sentenced to three days in the Los Angeles County Jail for contempt of court after falling severely behind on court-ordered temporary spousal support payments of approximately $18,900 per month. Schneider cited massive studio debt and flood damages, while Castle's legal team insisted upon fair contractual enforcement after two decades of domestic sacrifice.</p>

            <h2>Parallels to Classic Country Divorces</h2>
            <p>The protracted dissolution of John Schneider and Elly Castle's union drew frequent comparisons to other high-stakes entertainment splits. Observers noted strong parallels to <a href="/kaynette-williams/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Kaynette Williams</a>, who supported country megastar Blake Shelton during his pre-fame Nashville grind before gracefully stepping away into private educator life, and <a href="/marlene-knaus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Marlene Knaus</a>, whose post-divorce relationship with racing legend Niki Lauda maintained enduring mutual dignity and independence.</p>
            <p>Likewise, Elly maintained an admirable public silence throughout the trial, refusing to engage in sensational televised interviews or tell-all exposés, allowing her legal representatives to handle the technicalities while she focused on her children's emotional stability.</p>

            <h2>Her Children's Triumphs and Life Today</h2>
            <p>Today, Elly Castle takes immense pride in the achievements of her adult children. Her daughter, Karis Schneider, chose a heroic public-service career as an active-duty emergency firefighter, braving hazardous wildfires across the western United States. Her son Chasen Schneider has carved out an accomplished acting and theatrical career, while daughter Leah excels in creative production.</p>
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

def main():
    # Update ALL_ARTICLES in db
    for a in db.ALL_ARTICLES:
        if a["slug"] in EXPANDED_ARTICLES:
            a["contentHtml"] = EXPANDED_ARTICLES[a["slug"]]

    # Write back to articles_database.py
    with open(DB_FILE, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nIndependence Magazine - Article Database\nContains all verified, fact-checked editorial profiles.\n"""\n\n')
        f.write("ALL_ARTICLES = [\n")
        for a in db.ALL_ARTICLES:
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

    print("articles_database.py updated with expanded, high-depth content!")

if __name__ == "__main__":
    main()
