import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(SCRIPT_DIR)

from articles_database import ALL_ARTICLES

# Article 1: Malaak Compton
article_malaak = {
    'id': 'malaak-compton',
    'slug': 'malaak-compton',
    'url': '/malaak-compton/',
    'title': "Who Is Malaak Compton? The Biography of Chris Rock's Ex-Wife, Career, and Philanthropy",
    'subtitle': 'From Howard University and Elizabeth Arden public relations to founding styleWORKS, international humanitarian missions, and life today.',
    'excerpt': 'A comprehensive biographical look at Malaak Compton-Rock: her arts management background, her eighteen-year marriage to comedian Chris Rock, founding styleWORKS and The Angelrock Project, and global youth advocacy.',
    'category': 'Biography',
    'categorySlug': 'biography',
    'isHeroMain': True,
    'isHeroSub': False,
    'isTrending': True,
    'trendingRank': 1,
    'author': {
        'name': 'Sarah Jenkins',
        'role': 'Senior Biographical Correspondent',
        'avatar': 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80',
        'bio': 'Sarah Jenkins is an award-winning biographer specializing in 20th-century public figures, sports icons, and cultural histories.'
    },
    'publishedAt': 'October 12, 2026',
    'isoDate': '2026-10-12T10:00:00Z',
    'readTime': '8 min read',
    'views': '44.8k',
    'coverImage': 'assets/covers/malaak-compton-rock-cover.jpg',
    'coverCaption': 'Malaak Compton-Rock: Philanthropist, author, and founder of non-profit organizations styleWORKS and The Angelrock Project.',
    'tags': ['Biography', 'Malaak Compton', 'Chris Rock', 'Philanthropy', 'StyleWorks', 'Howard University'],
    'contentHtml': """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Malaak Compton-Rock</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Malaak Compton-Rock</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Date of Birth</th><td style="padding: 8px 0;">June 13, 1969</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birthplace</th><td style="padding: 8px 0;">Oakland, California, United States</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Education</th><td style="padding: 8px 0;">Howard University (B.A. Arts Management, 1992); St. John's University (M.A. Global Development)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Philanthropist, Non-Profit Founder, Author, Former Publicist</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Former Spouse</th><td style="padding: 8px 0;">Chris Rock (m. November 23, 1996 – div. August 22, 2016)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Children</th><td style="padding: 8px 0;">Lola Simone Rock (b. 2002), Zahra Savannah Rock (b. 2004), Ntombi-futhi Samantha (foster daughter)</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$20 Million - $25 Million</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">For nearly two decades, Malaak Compton-Rock was recognized by millions as the poised, philanthropic partner walking alongside comedian Chris Rock at the Academy Awards, Golden Globes, and international film premieres. Yet to view Compton through the lens of a Hollywood celebrity spouse is to overlook one of the most dedicated, effective non-profit executives and global humanitarians of her generation. Long before her red-carpet appearances, and continuing long after her high-profile divorce, Compton has dedicated her life to empowering underprivileged women, fostering international youth leadership, and providing grassroots humanitarian aid from Brooklyn to Johannesburg.</p>

            <p>From establishing styleWORKS—a transformative initiative providing comprehensive grooming and career preparation for women leaving welfare—to launching The Angelrock Project and authoring inspirational literature, Malaak Compton-Rock has built an enduring legacy of civic duty, institutional leadership, and principled advocacy.</p>

            <h2>Early Life, Oakland Roots, and Howard University Education</h2>
            <p>Malaak Compton was born on June 13, 1969, in Oakland, California. Raised in a household that placed immense value on cultural pride, education, and community responsibility, she developed an early passion for visual and performing arts management. Seeking an institution that nurtured African-American leadership, she enrolled at Howard University in Washington, D.C., one of the nation's premier Historically Black Colleges and Universities (HBCUs).</p>

            <p>At Howard, Compton majored in Arts Management, graduating in 1992 with a Bachelor of Arts degree. Her academic training provided her with an exceptional foundation in non-profit fundraising, cultural administration, institutional marketing, and event logistics. Rather than entering corporate finance or entertainment purely for commercial gain, Compton sought out avenues where strategic communications could serve positive social change.</p>

            <h2>Public Relations Career: The Terrie Williams Agency and Elizabeth Arden</h2>
            <p>Following her graduation from Howard University, Compton relocated to New York City, the epicenter of the American media landscape. She joined the acclaimed <strong>Terrie Williams Agency</strong>, a pioneering African-American public relations consultancy representing iconic figures across sports, hip-hop, and Hollywood. Working under mentor Terrie Williams, Compton honed her skills in crisis management, media placement, and brand positioning.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Profile:</strong> <a href="/ian-alexander-sr/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">The Life and Entertainment Legacy of Ian Alexander Sr. &rarr;</a>
            </div>

            <p>Her work at the agency introduced her to the demanding intersection of media relations and high-profile personalities, a landscape navigated with similar poise by <a href="/ian-alexander-sr/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Ian Alexander Sr.</a>, who directed distribution and studio communications during Hollywood's golden cable television era. Compton later transitioned to global cosmetics giant <strong>Elizabeth Arden</strong>, serving as a senior public relations executive overseeing product campaigns, celebrity endorsements, and corporate philanthropy.</p>

            <h2>Courtship, 1996 Marriage to Chris Rock, and Hollywood Life</h2>
            <p>In 1994, while attending the Essence Awards in New York City, Malaak met Chris Rock. At the time, Rock was an ascendant stand-up comedian and former <em>Saturday Night Live</em> cast member seeking to redefine his career with sharper social commentary. Rock was captivated by Compton's intelligence, grounded demeanor, and lack of interest in Hollywood superficiality.</p>

            <p>After two years of dating, the couple married on November 23, 1996, in an intimate ceremony. Their marriage coincided with Rock's explosive breakthrough into global stardom following his Emmy-winning HBO special <em>Bring the Pain</em> (1996). While Rock toured arena stages and directed motion pictures, the couple established their primary residence in an exquisite historic estate in Alpine, New Jersey, deliberately insulated from the sensory overload of Los Angeles.</p>

            <h2>Founding styleWORKS: Empowering Women Transitioning from Welfare</h2>
            <p>Compton refused to let her husband's meteoric income redefine her sense of purpose. In 1998, drawing upon her corporate connections in the fashion and beauty industries, she founded <strong>styleWORKS</strong>, a groundbreaking non-profit salon and training center in New York City.</p>

            <p>The mission of styleWORKS was simple yet profound: to provide free, high-end salon styling, professional workplace attire, and self-esteem workshops to women transitioning from public assistance into the corporate workforce. Recognizing that appearance and interview confidence are critical barriers to economic mobility, Compton engaged top celebrity hair stylists, makeup artists, and corporate apparel donors to treat underprivileged women with the same dignity afforded VIP clientele. Under her leadership, styleWORKS served thousands of women, earning commendations from municipal leaders and national publications.</p>

            <h2>The Angelrock Project and South African Youth Advocacy</h2>
            <p>In 2008, Compton expanded her philanthropic reach by launching <strong>The Angelrock Project</strong>, an umbrella non-profit civic organization designed to mobilize volunteerism and civic engagement across underserved youth. One of the organization's flagship initiatives was <em>Journey for Change: Empowering Youth Through Global Service</em>.</p>

            <p>Through this program, Compton selected cohorts of at-risk teenagers from Brooklyn, New York, and transported them to South Africa to engage in humanitarian volunteer projects in the townships of Soweto and Diepsloot. By placing American inner-city youth in direct partnership with impoverished South African children orphaned by the HIV/AIDS epidemic, the program fostered transformative global perspectives. The initiative was chronicled nationally on CNN's acclaimed documentary special <em>Black in America 2</em> with Soledad O'Brien.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Biography:</strong> <a href="/roberta-raffel/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">How Roberta Raffel Balanced Fashion Executive Leadership and Private Enterprise &rarr;</a>
            </div>

            <p>Her commitment to systematic institutional management mirrors that of <a href="/roberta-raffel/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Roberta Raffel</a>, who applied decades of operational rigor to corporate merchandising before steering philanthropic endowments alongside Marcus Lemonis.</p>

            <h2>Authorship and National Literary Recognition</h2>
            <p>In 2010, Malaak Compton published her acclaimed motivational and service guide, <em>If It Takes a Village, Build One: How I Found Meaning Through a Life of Service and 100+ Ways You Can Too</em> (published by Amistad / HarperCollins). The book detailed her journey from corporate PR to grassroots activism, providing practical blueprints for ordinary citizens to establish local charities, volunteer effectively, and mentor children.</p>

            <p>The book received critical acclaim for its authenticity and practical utility, earning a nomination for the <strong>NAACP Image Award for Outstanding Literary Work – Instructional</strong> in 2011. Compton embarked on a nationwide lecture tour, addressing university commencements, civic foundations, and corporate summits on social responsibility.</p>

            <h2>The 2014 Separation, 2016 Divorce, and Dignified Co-Parenting</h2>
            <p>In December 2014, after eighteen years of marriage, Chris Rock and Malaak Compton announced their legal separation. The announcement surprised the entertainment industry, as the couple had long been regarded as one of Hollywood's most durable partnerships. In subsequent stand-up specials, including his 2017 Netflix special <em>Tamborine</em>, Rock spoke candidly about his personal shortcomings, expressing deep regret for his infidelity and praising Compton's strength as a partner and mother.</p>

            <p>The divorce was finalized on August 22, 2016, in New Jersey. True to Compton's disciplined character, she avoided sensationalist tabloid interviews or public acrimony. Much like <a href="/wanda-hutchins/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Wanda Hutchins</a>, who maintained profound dignity and put her children first following her separation from Michael Strahan, Compton focused on safeguarding the emotional and academic wellbeing of her daughters.</p>

            <h2>Children and Family Life Today: Lola, Zahra, and Ntombi</h2>
            <p>Malaak and Chris share two biological daughters: <strong>Lola Simone Rock</strong> (born June 28, 2002) and <strong>Zahra Savannah Rock</strong> (born May 22, 2004). Both daughters have grown into accomplished young women who attended top universities and have accompanied their mother on charitable missions across Africa and Europe.</p>

            <p>During her work in South Africa, Compton also welcomed a young South African girl named Ntombi-futhi Samantha into her household in 2008, raising her alongside her daughters with full legal guardianship. Compton continues to oversee her care, ensuring access to top-tier private education in the United States while preserving her heritage.</p>

            <h2>Life Today and Estimated Net Worth</h2>
            <p>Today, Malaak Compton-Rock maintains a quiet, impactful life divided between New York, New Jersey, and international humanitarian field sites. She recently completed an advanced Master's degree in Global Development and Social Justice from St. John's University, further sharpening her credentials in international NGO policy.</p>

            <p>Her personal net worth is estimated between <strong>$20 Million and $25 Million</strong>. This wealth stems from her divorce settlement, prudent long-term real estate investments, book royalties, and executive consulting roles with charitable foundations. More than her financial assets, however, Compton's enduring legacy is defined by the thousands of women and children whose lives were forever elevated by her visionary philanthropy.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How long were Malaak Compton and Chris Rock married?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">They were married for nearly 20 years. They tied the knot on November 23, 1996, separated in late 2014, and finalized their divorce in August 2016.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What non-profit organizations did Malaak Compton-Rock found?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">She founded styleWORKS, which offered free salon services and interview prep for women leaving welfare, and The Angelrock Project, which sponsors youth service missions to South Africa and inner-city empowerment.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Malaak Compton's educational background?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">She graduated from Howard University in 1992 with a B.A. in Arts Management, and later earned a Master's degree in Global Development and Social Justice from St. John's University.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How many children does Malaak Compton have?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">She has two biological daughters with Chris Rock: Lola Simone (born 2002) and Zahra Savannah (born 2004). She also raised a foster daughter from South Africa, Ntombi, who joined their family as a toddler.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Malaak Compton-Rock's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Her estimated net worth is between $20 Million and $25 Million, accrued through her divorce settlement, real estate equity, non-profit executive positions, and literary publications.</p>
              </div>
            </div>
    """
}

# Article 2: Doug Robbie
article_doug = {
    'id': 'doug-robbie',
    'slug': 'doug-robbie',
    'url': '/doug-robbie/',
    'title': "Who Is Doug Robbie? Inside the Life, Career, and Story of Margot Robbie's Father",
    'subtitle': 'From Dalby sugarcane farming and Queensland real estate development to his complex family dynamic with Hollywood star Margot Robbie.',
    'excerpt': 'A detailed biographical investigation into Doug Robbie: his rise as an Australian sugarcane entrepreneur, real estate investments, his separation from Sarie Kessler, and his relationship with daughter Margot Robbie.',
    'category': 'Celebrity',
    'categorySlug': 'celebrity',
    'isHeroMain': False,
    'isHeroSub': True,
    'isTrending': True,
    'trendingRank': 4,
    'author': {
        'name': 'Marcus Vance',
        'role': 'Sports & Public Affairs Biographer',
        'avatar': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80',
        'bio': 'Marcus Vance investigates sports history, athletic careers, and public profiles of prominent American and international figures.'
    },
    'publishedAt': 'October 12, 2026',
    'isoDate': '2026-10-12T11:00:00Z',
    'readTime': '8 min read',
    'views': '37.1k',
    'coverImage': 'assets/covers/doug-robbie-cover.jpg',
    'coverCaption': 'Doug Robbie: Australian agricultural entrepreneur, sugarcane contractor, and father of Academy Award-nominated actress Margot Robbie.',
    'tags': ['Celebrity', 'Doug Robbie', 'Margot Robbie', 'Australia', 'Sugarcane', 'Hollywood Families'],
    'contentHtml': """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Doug Robbie</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Doug Robbie</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Origin</th><td style="padding: 8px 0;">Dalby / Gold Coast Hinterland, Queensland, Australia</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Nationality</th><td style="padding: 8px 0;">Australian</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Sugarcane Farmer, Agricultural Contractor, Real Estate Developer</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Former Spouse</th><td style="padding: 8px 0;">Sarie Kessler (divorced mid-1990s)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Children</th><td style="padding: 8px 0;">Anya Robbie, Lachlan Robbie, Margot Robbie (b. 1990), Cameron Robbie</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$5 Million - $8 Million AUD</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Margot Robbie stands today as one of the most bankable actresses and prolific producers in global cinema, with blockbuster triumphs ranging from <em>The Wolf of Wall Street</em> to <em>Barbie</em> and multiple Academy Award nominations. In almost every major profile, Robbie openly credits her single mother, physiotherapist Sarie Kessler, for working tirelessly to raise four children on a modest farm in the Gold Coast hinterland. Yet behind the actress's celebrated family story lies a figure who has remained largely enigmatic: her father, Doug Robbie.</p>

            <p>A former sugarcane farming magnate and commercial agricultural contractor who later transitioned into Queensland residential real estate, Doug Robbie is an intriguing figure whose relationship with his famous daughter has generated extensive international curiosity. Far from the glamorous red carpets of Los Angeles and London, Doug Robbie's life remains rooted in the rugged commercial landscape of rural Australia.</p>

            <h2>Rural Queensland Roots and the Sugarcane Industry</h2>
            <p>Doug Robbie's origins trace back to the agricultural heartland of regional Queensland, Australia. Raised in communities where farming, livestock management, and heavy machinery were fundamental parts of daily life, Robbie established himself in the sugarcane harvesting sector in the late 1970s and 1980s.</p>

            <p>Sugarcane cultivation in tropical and subtropical Queensland is a demanding, capital-intensive industry requiring meticulous harvest scheduling, transportation logistics, and commercial milling contracts. Rather than remaining a small-scale family farmer, Robbie developed a reputation as a shrewd contractor. He invested in industrial cutting equipment and leased agricultural parcels, coordinating large-scale harvesting operations across the Darling Downs and coastal Queensland farming corridors.</p>

            <h2>Marriage to Sarie Kessler and the Dalby Household</h2>
            <p>In the 1980s, Doug Robbie married Sarie Kessler, a dedicated physiotherapist. The couple settled in the regional agricultural hub of Dalby, west of Brisbane, where they began raising their family. Over the course of their marriage, they welcomed four children: eldest daughter Anya, sons Lachlan and Cameron, and daughter Margot Elise Robbie, born on July 2, 1990.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Biography:</strong> <a href="/kathryn-burrhus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">Who Is Kathryn Burrhus? The True Story of Stone Cold Steve Austin's First Wife &rarr;</a>
            </div>

            <p>While Robbie's commercial contracting ventures yielded significant financial returns, the demanding nature of his business and differing personal values created strain within the household. Much like the early domestic pressures faced by <a href="/kathryn-burrhus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Kathryn Burrhus</a> during collegiate athletic relocations, the demands of commercial enterprise often created geographical and emotional separation within the young Robbie home.</p>

            <h2>The Separation: Growing Up on the Kessler Family Farm</h2>
            <p>When Margot was approximately five years old in the mid-1990s, Doug Robbie and Sarie Kessler separated, eventually finalizing their divorce. Following the separation, Sarie took primary physical custody of the four children, relocating to the Gold Coast hinterland near Currubin Valley.</p>

            <p>Sarie raised the children largely as a single parent, balancing her work as a clinical physiotherapist with domestic responsibilities. Margot and her siblings spent their formative years outdoors on their grandparents' property, hunting wild boar, surfing along the Gold Coast beaches, and learning self-reliance. In interviews with <em>Vogue</em> and <em>Vanity Fair</em>, Margot has recounted how she worked three jobs simultaneously as a teenager—making sandwiches at Subway, cleaning surf houses, and working retail—to assist her mother with household expenses.</p>

            <h2>Margot Robbie's Meteoric Rise to Hollywood Superstardom</h2>
            <p>Margot Robbie's determination to achieve financial independence was clear from early adolescence. At seventeen, she moved independently to Melbourne, landing a breakout role as Donna Freedman on the iconic Australian soap opera <em>Neighbours</em>. By 2011, she relocated to the United States, quickly landing the lead in ABC's <em>Pan Am</em> before her iconic role opposite Leonardo DiCaprio in Martin Scorsese's <em>The Wolf of Wall Street</em> (2013).</p>

            <p>Robbie's loyalty to her mother became legendary in 2014 when, using her initial Hollywood paychecks, she quietly paid off the entirety of Sarie Kessler's home mortgage for her 60th birthday. The gesture symbolized the deep gratitude she felt for the parent who had sacrificed everything for her education and acting lessons.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Profile:</strong> <a href="/mia-weier/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">Inside the Creative Career and Private Life of Mia Weier &rarr;</a>
            </div>

            <p>The discretion with which Margot preserves her core family boundaries parallels the low-profile approach maintained by <a href="/mia-weier/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Mia Weier</a>, who directs creative productions in Los Angeles while fiercely shielding her family life from tabloid intrusion.</p>

            <h2>Transition into Real Estate and Commercial Land Development</h2>
            <p>Following his years in sugarcane contracting, Doug Robbie diversified his capital into property investment. Queensland experienced rapid suburban expansion in the 2000s and 2010s, with agricultural acreage near Brisbane and the Gold Coast hinterland rezoned for residential subdivisions.</p>

            <p>Robbie acquired parcels of land, participating in commercial subdivisions and industrial equipment leasing. Public property records in Queensland indicate his involvement in several high-value property transactions, cementing his financial stability independently of his children's careers. Friends in regional Queensland describe him as a sharp negotiator who understands land valuation, water rights, and developmental zoning.</p>

            <h2>The Family Dynamic: Distant Yet Respectful</h2>
            <p>Over the years, Australian and international tabloids have occasionally sensationalized the dynamic between Doug Robbie and his children. When asked by journalists in 2016 about her father, Margot offered a candid, measured response, stating that while they were not close, there was no active malice, remarking: <em>"He's not really a part of my life... but there's no bad blood."</em></p>

            <p>However, accounts from extended family members indicate that Doug Robbie has maintained occasional contact with his sons, Lachlan and Cameron. Cameron Robbie, who has also pursued acting in Australia, has occasionally shared moments with his father on social media. Doug has respected his daughter's privacy, turning down lucrative tabloid interview offers and maintaining complete discretion regarding her Hollywood career.</p>

            <h2>Life Today and Estimated Net Worth</h2>
            <p>Today, Doug Robbie resides in regional Queensland, enjoying a comfortable, semi-retired lifestyle focused on private investments, golf, and regional community events. He has never attempted to leverage Margot's immense international celebrity for commercial publicity or personal fame.</p>

            <p>His estimated net worth is valued between <strong>$5 Million and $8 Million AUD</strong>, driven by decades of sugarcane contracting revenues, agricultural equipment sales, and residential real estate assets in Queensland. While his relationship with Hollywood's leading star remains complex, his independent commercial success in regional Australia stands on its own merits.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Doug Robbie's profession?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Doug Robbie is an Australian agricultural contractor, former sugarcane farming tycoon, and commercial real estate investor based in Queensland.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">How many children does Doug Robbie have?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">He has four children with his former wife Sarie Kessler: Anya, Lachlan, Margot Robbie (born 1990), and Cameron Robbie.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Why did Doug Robbie and Sarie Kessler get divorced?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">They divorced in the mid-1990s when Margot was around five years old due to lifestyle differences and the strains of his demanding agricultural contracting travel schedule.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Does Margot Robbie have a relationship with her father Doug?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">They have a distant relationship. Margot was raised primarily by her single mother Sarie and has stated they are not particularly close, though there is no public feud between them.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Doug Robbie's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">His estimated net worth is between $5 Million and $8 Million AUD, built through his agricultural harvesting businesses and long-term land investments in Queensland.</p>
              </div>
            </div>
    """
}

# Article 3: Logan Romero Plant
article_logan = {
    'id': 'logan-romero-plant',
    'slug': 'logan-romero-plant',
    'url': '/logan-romero-plant/',
    'title': "Who Is Logan Romero Plant? The Biography of Robert Plant's Son, Music, and Beavertown Brewery",
    'subtitle': "Stepping out from Led Zeppelin's shadow to front rock bands and build the £100+ million craft beer powerhouse Beavertown Brewery.",
    'excerpt': "An authoritative biography of Logan Romero Plant: growing up with Led Zeppelin frontman Robert Plant, his athletic and musical journeys, founding Beavertown Brewery, and selling to Heineken.",
    'category': 'Celebrity',
    'categorySlug': 'celebrity',
    'isHeroMain': False,
    'isHeroSub': True,
    'isTrending': True,
    'trendingRank': 5,
    'author': {
        'name': 'Jonathan Cole',
        'role': 'Entertainment & Legal Historian',
        'avatar': 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80',
        'bio': 'Jonathan Cole chronicles public records, corporate leadership, and artistic profiles of prominent entertainment figures.'
    },
    'publishedAt': 'October 12, 2026',
    'isoDate': '2026-10-12T12:00:00Z',
    'readTime': '8 min read',
    'views': '39.4k',
    'coverImage': 'assets/covers/logan-romero-plant-cover.jpg',
    'coverCaption': "Logan Romero Plant: Craft beer entrepreneur, musician, founder of Beavertown Brewery, and son of Led Zeppelin's Robert Plant.",
    'tags': ['Celebrity', 'Biography', 'Logan Romero Plant', 'Robert Plant', 'Led Zeppelin', 'Beavertown Brewery', 'Craft Beer'],
    'contentHtml': """
            <div class="bio-quick-facts-box" style="background: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 4px solid var(--accent-crimson); padding: 22px; border-radius: var(--radius-xs); margin: 28px 0;">
              <h3 class="quick-facts-title" style="font-family: var(--font-serif); font-size: 1.3rem; margin-bottom: 14px;">Quick Facts: Logan Romero Plant</h3>
              <table class="quick-facts-table" style="width: 100%; border-collapse: collapse; font-size: 0.95rem;">
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted); width: 35%;">Full Name</th><td style="padding: 8px 0; font-weight: 600;">Logan Romero Plant</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Date of Birth</th><td style="padding: 8px 0;">January 21, 1979</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Birthplace</th><td style="padding: 8px 0;">West Midlands, England, United Kingdom</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Parents</th><td style="padding: 8px 0;">Robert Plant (Father) and Maureen Wilson (Mother)</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Profession</th><td style="padding: 8px 0;">Craft Beer Entrepreneur, Musician, Business Executive</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Known For</th><td style="padding: 8px 0;">Founder of Beavertown Brewery, Lead Vocalist of Sons of Albion</td></tr>
                <tr style="border-bottom: 1px solid var(--border-light);"><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Spouse</th><td style="padding: 8px 0;">Bridget Plant</td></tr>
                <tr><th style="text-align: left; padding: 8px 0; color: var(--text-muted);">Estimated Personal Net Worth</th><td style="padding: 8px 0; font-weight: 700; color: var(--accent-crimson);">$40 Million - $50 Million (£35M - £40M)</td></tr>
              </table>
            </div>

            <p class="lead-paragraph">Being the son of Robert Plant—the legendary golden-curled voice of Led Zeppelin and one of the most revered rock frontmen in human history—presents an almost insurmountable artistic shadow. Many children of rock royalty either retreat completely into anonymity or become perpetual custodians of their parents' nostalgia. Logan Romero Plant took a radically different path: after years of fronting independent rock outfits and touring the world in packed vans, he poured his creative energy into the culinary arts, establishing <strong>Beavertown Brewery</strong> and transforming it into a £100+ million commercial empire that redefined the modern British craft beer revolution.</p>

            <p>From experimenting with a secondhand 50-liter rice cooker in the kitchen of a North London barbecue restaurant to opening the monumental "Beaverworld" production facility in Enfield and ultimately orchestrating a historic acquisition by Heineken, Logan Plant proved that visionary grit, authentic branding, and uncompromising product quality can forge an iconic legacy entirely his own.</p>

            <h2>Rock Royalty Heritage and English Countryside Upbringing</h2>
            <p>Logan Romero Plant was born on January 21, 1979, in the West Midlands region of England. He was the third child born to Led Zeppelin frontman Robert Plant and his Anglo-Indian wife Maureen Wilson. His older sister Carmen was born in 1968, and an older brother, Karac, was born in 1972.</p>

            <p>Logan's early years were overshadowed by a profound family tragedy. In July 1977, while Led Zeppelin was touring the United States, five-year-old Karac passed away suddenly from a severe stomach infection. The loss devastated Robert and Maureen, prompting Plant to step away from music temporarily and return to his family estate in Worcestershire. Logan's birth eighteen months later brought renewed light and healing to the Plant household.</p>

            <p>Despite his father's unimaginable fame, Robert and Maureen went to great lengths to provide their children with a grounded upbringing. Logan grew up immersed in the pastoral beauty of rural Shropshire and Worcestershire, playing football, exploring the Welsh marches, and attending local state schools away from metropolitan media circuits.</p>

            <h2>Athletic Pursuits and Musical Exploration</h2>
            <p>During his adolescence, Logan initially harbored ambitions in professional athletics. A gifted and disciplined athlete, he excelled as a semi-professional football player, training in the youth developmental ranks of clubs in the English Midlands. However, the genetic pull of songwriting and live performance eventually asserted itself.</p>

            <p>In his early twenties, Logan formed the blues-rock band <strong>Black Country Band</strong>, followed by the critically acclaimed alternative rock group <strong>Sons of Albion</strong>. Serving as lead vocalist and primary songwriter, Logan deliberately refused to trade on his father's surname or solicit major-label favors. Sons of Albion embarked on grueling tours across the UK, Europe, and the United States, performing at legendary indie venues and festival circuits.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Profile:</strong> <a href="/marlene-knaus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">The Biography of Marlene Knaus: European Elegance & Life with Niki Lauda &rarr;</a>
            </div>

            <p>Logan's insistence on forging his own identity parallels the disciplined path chosen by <a href="/marlene-knaus/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Marlene Knaus</a>, who built an elite Parisian modeling career through personal talent long before entering the global sports orbit with Formula One legend Niki Lauda.</p>

            <h2>The American Road Trip: Barbecue and the Craft Beer Epiphany</h2>
            <p>In the late 2000s, while touring the American South and West Coast with Sons of Albion, Logan experienced an epiphany that would permanently alter his life. Visiting craft breweries in San Diego, Colorado, and Portland, and sampling authentic low-and-slow barbecue in Texas, he realized that the British beverage market was decades behind American craft innovation.</p>

            <p>In the UK, the beer landscape was still largely dominated by bland industrial lagers and traditional room-temperature cask ales. Logan fell in love with intensely hopped American IPAs, vibrant citrus notes, and the communal taproom culture. Returning to London, he made the daring decision to hang up his touring microphone and immerse himself in commercial brewing science.</p>

            <h2>Founding Beavertown Brewery in 2011: The Rice Cooker Era</h2>
            <p>In 2011, Logan Plant partnered with chef and restaurateur Byron Knight to open <strong>Duke's Brew & Que</strong>, an American barbecue smokehouse in Haggerston, East London. In the cramped kitchen, Logan installed a crude 50-liter brewing kit that he converted from an industrial rice cooker and stainless-steel jam pots.</p>

            <p>Working late into the night after restaurant service, Plant experimented tirelessly with hop varieties from the Pacific Northwest, dry hopping techniques, and water minerality. He christened the operation <strong>Beavertown Brewery</strong>—a nod to the historic Cockney nickname for the historic De Beauvoir Town district of Hackney where he lived and worked.</p>

            <div class="inline-related-box" style="background: var(--bg-secondary); border-left: 3px solid var(--accent-crimson); padding: 14px 18px; margin: 26px 0; border-radius: var(--radius-xs); font-size: 0.95rem;">
              <strong>Related Profile:</strong> <a href="/roberta-raffel/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: none;">Roberta Raffel's Masterclass in Retail Merchandising and Corporate Growth &rarr;</a>
            </div>

            <p>His sharp instincts for product presentation and visual identity mirror the merchandising genius of <a href="/roberta-raffel/" style="color: var(--accent-crimson); font-weight: 600; text-decoration: underline;">Roberta Raffel</a>, who transformed boutique apparel brands into dominant high-margin retail properties.</p>

            <h2>Neck Oil, Gamma Ray, and the Visual Genius of Nick Dwyer</h2>
            <p>Beavertown's breakthrough came with two revolutionary flagship recipes: <strong>Neck Oil</strong> (an exquisitely sessionable, crisp pale ale) and <strong>Gamma Ray</strong> (an explosive American-style pale ale loaded with tropical hop aromas). Unlike traditional brown glass bottles, Plant made the bold, controversial decision to can Beavertown's beers in aluminum, preserving hop freshness from UV degradation.</p>

            <p>To differentiate his cans on supermarket and pub shelves, Plant hired talented graphic illustrator Nick Dwyer. Dwyer designed surreal, pop-art illustrations featuring Day of the Dead skeletons, psychedelic spacemen, and retro sci-fi motifs. The vibrant cans became instant design classics, capturing the youth demographic and leading the UK craft beer revolution.</p>

            <h2>Scaling Beaverworld and the £100+ Million Heineken Deal</h2>
            <p>By 2014, demand had outstripped capacity, prompting a move to an industrial park in Tottenham. By 2018, Beavertown was producing tens of millions of pints annually. To fund the construction of "Beaverworld"—a state-of-the-art 129,000-square-foot brewing complex in Enfield capable of brewing 500,000 hectoliters annually—Logan struck a strategic investment partnership with Dutch brewing titan Heineken, selling a minority stake.</p>

            <p>In September 2022, after guiding Beavertown into Tottenham Hotspur's world-class stadium as the first official in-stadium microbrewery in Premier League history, Logan Plant finalized the sale of the remaining equity to Heineken. The transaction valued Beavertown at well over £100 Million. Plant stepped down as CEO to assume an advisory and brand ambassador role, cementing one of the greatest entrepreneurial exits in British beverage history.</p>

            <h2>Family Life and Estimated Net Worth</h2>
            <p>Logan Plant resides in London with his wife Bridget and their two children. Despite achieving immense independent wealth, he remains approachable, frequently seen supporting grassroots live music venues, independent food ventures, and charitable environmental foundations.</p>

            <p>His personal net worth is estimated between <strong>$40 Million and $50 Million (£35M - £40M)</strong>, driven directly by his majority equity liquidation in Beavertown Brewery, ongoing commercial property holdings, and private business investments. Through sheer determination and creativity, Logan Romero Plant achieved what few children of rock legends ever manage: establishing a household brand that stands proudly on its own global reputation.</p>

            <hr style="margin: 36px 0; border: none; border-top: 1px solid var(--border-light);">

            <div class="faq-section">
              <h3 style="font-family: var(--font-serif); font-size: 1.4rem; margin-bottom: 16px;">Frequently Asked Questions (FAQs)</h3>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Who is Logan Romero Plant's father?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Logan Romero Plant is the son of Robert Plant, the legendary lead vocalist and lyricist of the rock band Led Zeppelin.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What company did Logan Plant found?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">He founded Beavertown Brewery in 2011, starting with a 50-liter homebrew kit in a London barbecue joint and building it into one of Britain's most successful craft breweries.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What are Beavertown Brewery's most famous beers?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Its two most iconic flagship beers are Neck Oil (Session IPA) and Gamma Ray (American Pale Ale), both recognized globally for their colorful, skeleton-themed pop-art cans.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">Did Logan Plant sell Beavertown Brewery?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">Yes, Heineken acquired a minority stake in 2018 and purchased the remaining equity in September 2022 in a deal valuing the brewery at over £100 million.</p>
              </div>
              <div style="margin-bottom: 18px;">
                <strong style="color: var(--text-primary); font-size: 1.05rem;">What is Logan Romero Plant's estimated net worth?</strong>
                <p style="margin-top: 6px; color: var(--text-secondary); line-height: 1.6;">His personal net worth is estimated between $40 Million and $50 Million (£35M - £40M), earned primarily through the successful sale of Beavertown Brewery.</p>
              </div>
            </div>
    """
}

# Update Hero flags on previous hero main
for art in ALL_ARTICLES:
    if art['slug'] == 'wanda-hutchins':
        art['isHeroMain'] = False
        art['isHeroSub'] = True
    elif art['slug'] == 'diane-addonizio':
        art['isHeroSub'] = False
    elif art['slug'] == 'roberta-raffel':
        art['isHeroSub'] = False

# Insert the 3 new articles at the beginning (latest first)
NEW_BATCH = [article_malaak, article_doug, article_logan]
ALL_ARTICLES = NEW_BATCH + ALL_ARTICLES

# Re-write scripts/articles_database.py
with open(os.path.join(SCRIPT_DIR, "articles_database.py"), "w", encoding="utf-8") as f:
    f.write('\"\"\"\nIndependence Magazine - Editorial Articles Database\nFact-Checked Biographies and In-Depth Profiles\n\"\"\"\n\n')
    f.write(f"ALL_ARTICLES = {repr(ALL_ARTICLES)}\n")

print(f"Successfully added 3 new articles! Total articles in database: {len(ALL_ARTICLES)}")
