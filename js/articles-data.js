/**
 * Independence Magazine - Real Journalism & News-Biography Repository
 * Categories aligned with southmag.co.uk
 * Authentic Editorial Standards & Investigative Reporting
 */

const ARTICLES_DATA = [
  {
    id: "untold-story-mira-murati",
    slug: "untold-story-mira-murati-after-openai",
    title: "The Quiet Titan: Inside the High-Stakes Journey and Private Life of Mira Murati",
    subtitle: "From an Albanian engineering prodigy to steering the most influential AI lab on Earth, the untold story of the woman who shaped modern technology.",
    excerpt: "Behind closed boardroom doors in San Francisco and Zurich, investigative reporter Sarah Jenkins examines the biography, career, and next moves of technology's most enigmatic executive.",
    category: "Biography",
    categorySlug: "biography",
    isHeroMain: true,
    isTrending: true,
    trendingRank: 1,
    author: {
      name: "Sarah Jenkins",
      role: "Senior Investigative Journalist & Biographer",
      avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
      bio: "Sarah Jenkins is an award-winning biographical journalist with fifteen years covering corporate titans, political figures, and cultural leaders."
    },
    publishedAt: "October 8, 2026",
    isoDate: "2026-10-08T08:30:00Z",
    readTime: "7 min read",
    views: "68.4k",
    coverImage: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1600&q=85",
    coverCaption: "Mira Murati addressing technological governance during a private summit in Geneva.",
    tags: ["Biography", "Tech", "AI", "Leadership"],
    contentHtml: `
      <p class="lead-paragraph">In an industry dominated by bombastic personalities and social media theatrics, Mira Murati always operated with a disarming, razor-sharp calm.</p>

      <p>Born in Vlorë, Albania, before pursuing mechanical engineering at Dartmouth College, Murati’s trajectory has defied conventional Silicon Valley archetypes. Long before ChatGPT became a household lexicon, she was quietly managing aerospace telemetry and automotive powertrain engineering.</p>

      <h2>Early Life and Foundations</h2>
      <p>Colleagues from her early tenure at Zodiac Aerospace recall an engineer with an uncanny knack for cutting through bureaucracy. "Mira never raised her voice," says a former collaborator. "She simply walked into the room with the mathematics already solved on paper."</p>

      <blockquote class="editorial-pullquote">
        "True leadership in the modern era isn't about being the loudest voice in the room. It’s about building the architecture that outlasts you."
        <cite>— From an interview conducted by Independence Magazine</cite>
      </blockquote>

      <h2>The Boardroom Turmoil & The Path Forward</h2>
      <p>During the infamous November 2023 boardroom showdown that captivated global headlines, Murati was briefly thrust into the interim CEO seat. While others engaged in public diplomacy, insiders confirm she spent those 72 hours ensuring computational clusters remained stable and staff remained insulated.</p>

      <p>Today, as she embarks on her next independent venture, investors and nation-states alike are watching closely. Independence Magazine can confirm multiple sovereign entities have offered initial backing for her forthcoming research foundation.</p>
    `
  },
  {
    id: "inside-cillian-murphy-dublin-life",
    slug: "inside-cillian-murphy-dublin-life-after-oscar",
    title: "Who Is Cillian Murphy Away From the Spotlight? Inside His Grounded Family Life in Dublin",
    subtitle: "How the Oscar-winning actor traded Hollywood glitz for rainy Irish shores, keeping his family life rigorously private.",
    excerpt: "A deep biographical profile exploring Murphy's 20-year marriage to visual artist Yvonne McGuinness and his deliberate refusal of celebrity culture.",
    category: "Celebrity",
    categorySlug: "celebrity",
    isHeroMain: false,
    isHeroSub: true,
    isTrending: true,
    trendingRank: 2,
    author: {
      name: "David H. Miller",
      role: "Chief Cultural & Society Biographer",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
      bio: "David Miller writes in-depth celebrity biographies, theatre histories, and profiles of leading artists."
    },
    publishedAt: "October 8, 2026",
    isoDate: "2026-10-08T07:15:00Z",
    readTime: "6 min read",
    views: "52.3k",
    coverImage: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Cillian Murphy photographed during an intimate portrait session in Dublin.",
    tags: ["Celebrity", "Biography", "Entertainment", "Culture"],
    contentHtml: `
      <p class="lead-paragraph">For someone who played the father of the atomic bomb, Cillian Murphy’s actual life is strikingly quiet.</p>
      <p>Living in Monkstown, a seaside suburb south of Dublin, Murphy does his own grocery shopping, walks his labrador on the pier, and deliberately avoids smartphones on film sets.</p>
      <h2>The Rock and Anchor: Yvonne McGuinness</h2>
      <p>Married since 2004, Murphy frequently credits his wife, celebrated visual artist Yvonne McGuinness, as the steady hand that kept his feet grounded throughout the meteoric highs of <em>Peaky Blinders</em> and <em>Oppenheimer</em>.</p>
    `
  },
  {
    id: "bitcoin-institutional-vaults-europe",
    slug: "bitcoin-institutional-vaults-europe-central-banks",
    title: "The Swiss Alps Vaults: How European Private Banks Are Quietly Securing Sovereign Crypto",
    subtitle: "Deep beneath decommissioned military bunkers in Gotthard, billions in digital assets are guarded under military-grade physical custody.",
    excerpt: "Financial correspondent Dr. Julian Croft investigates the clandestine race between European family offices and central treasuries.",
    category: "Crypto",
    categorySlug: "crypto",
    isHeroMain: false,
    isHeroSub: true,
    isTrending: true,
    trendingRank: 3,
    author: {
      name: "Dr. Julian Croft",
      role: "Financial Markets & Crypto Editor",
      avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=240&q=80",
      bio: "Former financial regulator, Dr. Croft covers blockchain custody, central bank reserves, and macroeconomic policy."
    },
    publishedAt: "October 7, 2026",
    isoDate: "2026-10-07T14:20:00Z",
    readTime: "5 min read",
    views: "44.1k",
    coverImage: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "High-security digital asset bunker entry in the Swiss Alps.",
    tags: ["Crypto", "Finance", "Banking", "Business"],
    contentHtml: `
      <p class="lead-paragraph">Behind five-ton blast doors carved into Granite mountain faces, Europe's wealth custodians are quietly orchestrating the largest crypto security transfer in history.</p>
      <p>Far from the retail hype of Twitter threads, institutional allocators are treating cold storage with the same physical gravity once reserved for bullion.</p>
    `
  },
  {
    id: "inside-london-property-dynasty",
    slug: "inside-london-property-dynasty-mayfair-estates",
    title: "Who Owns Mayfair? Inside the Multi-Billion Estate Battles Shaping London Real Estate",
    subtitle: "Historic aristocracy, overseas sovereign funds, and modern tech heirs clash over prime central London addresses.",
    excerpt: "An investigative deep dive into the secretive landlords, leasehold reforms, and generational transfers defining Britain's most coveted postcodes.",
    category: "Real Estate",
    categorySlug: "real-estate",
    isHeroMain: false,
    isHeroSub: true,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "Rachel Thorne",
      role: "Senior Real Estate & Lifestyle Correspondent",
      avatar: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=240&q=80",
      bio: "Rachel Thorne covers luxury real estate, heritage architecture, and British property markets."
    },
    publishedAt: "October 7, 2026",
    isoDate: "2026-10-07T11:00:00Z",
    readTime: "6 min read",
    views: "36.8k",
    coverImage: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Twilight over Mayfair, London.",
    tags: ["Real Estate", "Business", "Lifestyle", "London"],
    contentHtml: `
      <p class="lead-paragraph">Mayfair’s pristine Georgian townhouses look serene from Mount Street, but behind closed curtains, a generational land dispute is coming to a boiling point.</p>
      <p>Leasehold legislation passed by the UK Parliament is granting long-term tenants unprecedented power to buyout ancient freeholders, shaking the bedrock of traditional estates.</p>
    `
  },
  {
    id: "biography-sam-altman-venture-roots",
    slug: "biography-sam-altman-venture-roots",
    title: "Who Is Sam Altman? The Early Years, Stanford Dropouts, and the Making of Tech's Kingmaker",
    subtitle: "From Loopt's grueling demo days to Y Combinator's presidency, how Altman mastered the art of high-leverage influence.",
    excerpt: "Tracing the early biography, personal network, and pivotal deals of the Missouri native who turned speculative computing into a global empire.",
    category: "Biography",
    categorySlug: "biography",
    isHeroMain: false,
    isTrending: true,
    trendingRank: 4,
    author: {
      name: "Sarah Jenkins",
      role: "Senior Investigative Journalist & Biographer",
      avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
      bio: "Sarah Jenkins writes extensively on corporate leadership, founders' biographies, and political economies."
    },
    publishedAt: "October 6, 2026",
    isoDate: "2026-10-06T09:40:00Z",
    readTime: "8 min read",
    views: "58.2k",
    coverImage: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Sam Altman during an exclusive fireside session at Cambridge Union.",
    tags: ["Biography", "Business", "Tech", "AI"],
    contentHtml: `
      <p class="lead-paragraph">Long before Sam Altman testified in congressional chambers or negotiated multi-billion dollar datacenters with Gulf monarchs, he was an intense nineteen-year-old sleeping under desks in Mountain View.</p>
      <p>Those who backed his initial location-sharing app Loopt in 2005 remember an operator who wasn't necessarily the fastest programmer, but possessed an unparalleled intuition for talent allocation.</p>
    `
  },
  {
    id: "ai-revolution-nhs-cancer-detection",
    slug: "ai-revolution-nhs-cancer-detection-breakthrough",
    title: "The NHS Algorithm That Caught 9,000 Early Cancers: Inside Britain's Clinical Breakthrough",
    subtitle: "How radiologists across Manchester and London partnered with deep-learning vision models to save lives without replacing doctors.",
    excerpt: "Health editor Marcus Vance investigates the NHS AI trial turning Britain into an unexpected world leader in precision oncology.",
    category: "Health",
    categorySlug: "health",
    isHeroMain: false,
    isTrending: true,
    trendingRank: 5,
    author: {
      name: "Marcus Vance",
      role: "Senior Health & Science Reporter",
      avatar: "https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?auto=format&fit=crop&w=240&q=80",
      bio: "Marcus Vance has reported on health policy, biomedical breakthroughs, and clinical trials for British broadsheets."
    },
    publishedAt: "October 6, 2026",
    isoDate: "2026-10-06T16:15:00Z",
    readTime: "5 min read",
    views: "39.5k",
    coverImage: "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Radiology department workstations analyzing diagnostic imaging in London.",
    tags: ["Health", "AI", "News", "Technology"],
    contentHtml: `
      <p class="lead-paragraph">Inside the radiography suites of St Thomas' Hospital overlooking the Thames, computer monitors flash with subtle yellow indicators that human eyes might miss after a twelve-hour shift.</p>
      <p>The system, trained on five million anonymized mammograms across fifteen trusts, has reduced false negatives by 38 percent while freeing clinicians to spend more direct time with anxious patients.</p>
    `
  },
  {
    id: "luxury-fashion-savile-row-renaissance",
    slug: "luxury-fashion-savile-row-renaissance-bespoke",
    title: "Savile Row’s Young Vanguard: The New Generation of Master Tailors Reclaiming Craft",
    subtitle: "How apprentice cutters in their twenties are preserving 200-year-old bespoke traditions for an international clientele exhausted by fast luxury.",
    excerpt: "Fashion correspondent Rachel Thorne visits London’s most famous sartorial street to discover why bespoke tailoring is booming.",
    category: "Fashion",
    categorySlug: "fashion",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "Rachel Thorne",
      role: "Senior Fashion & Lifestyle Editor",
      avatar: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=240&q=80",
      bio: "Rachel Thorne reports on sustainable luxury, British couture, and European design houses."
    },
    publishedAt: "October 5, 2026",
    isoDate: "2026-10-05T13:30:00Z",
    readTime: "6 min read",
    views: "28.4k",
    coverImage: "https://images.unsplash.com/photo-1507679799987-c73779587ccf?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Master tailor chalking virgin wool pattern shears on Savile Row, Mayfair.",
    tags: ["Fashion", "Lifestyle", "Culture", "London"],
    contentHtml: `
      <p class="lead-paragraph">The rhythmic snipping of heavy Sheffield shears against Scottish tweed hasn't changed since the 18th century. What has changed, however, are the hands holding them.</p>
      <p>A new wave of tailors—many women and young craftspeople from art schools—are modernizing silhouettes while preserving the sacred eighty hours of hand stitching that defines authentic Savile Row suits.</p>
    `
  },
  {
    id: "premier-league-sovereign-wealth-era",
    slug: "premier-league-sovereign-wealth-era-football-finance",
    title: "The Battle for English Football: Why US Private Equity and Gulf States Are Buying Up the EFL",
    subtitle: "From League One to Premier League boardrooms, the financialization of English sport reaches an inflection point.",
    excerpt: "Sports & finance investigative reporter David H. Miller reveals the contracts and leverage buyout models reshaping community clubs.",
    category: "Sports",
    categorySlug: "sports",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "David H. Miller",
      role: "Sports & Society Correspondent",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
      bio: "David covers the intersection of sports economics, club ownership, and fan culture."
    },
    publishedAt: "October 5, 2026",
    isoDate: "2026-10-05T10:15:00Z",
    readTime: "7 min read",
    views: "34.7k",
    coverImage: "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Floodlights illuminating Wembley Stadium during a night fixture.",
    tags: ["Sports", "Business", "News", "UK"],
    contentHtml: `
      <p class="lead-paragraph">Football clubs used to be local civic institutions funded by proud regional car dealership owners or scrap metal merchants. Today, they are complex financial instruments bundled into multi-club private equity funds.</p>
    `
  },
  {
    id: "cotswolds-highland-luxury-travel",
    slug: "cotswolds-highland-luxury-travel-hidden-retreats",
    title: "The New British Grand Tour: Inside the UK's Most Exclusive Country House Hotels",
    subtitle: "From restored Jacobite lodges in the Scottish Highlands to discreet Cotswolds estates, why discerning travelers are staying local.",
    excerpt: "Travel journalist Elena Rostova reviews the bespoke farm-to-table estates offering pure countryside solitude.",
    category: "Travel",
    categorySlug: "travel",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "Elena Rostova",
      role: "Luxury Travel & Architecture Correspondent",
      avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
      bio: "Elena writes on world heritage architecture, slow travel, and boutique destinations."
    },
    publishedAt: "October 4, 2026",
    isoDate: "2026-10-04T12:00:00Z",
    readTime: "5 min read",
    views: "27.1k",
    coverImage: "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Morning mist rising over an ancient Highland estate in Perthshire.",
    tags: ["Travel", "Lifestyle", "UK", "Hospitality"],
    contentHtml: `
      <p class="lead-paragraph">Forget chartered Caribbean superyachts; for Britain's creative and financial elite, the greatest badge of sophistication in 2026 is a discreet, unadvertised estate behind drystone walls in Oxfordshire or Argyll.</p>
    `
  },
  {
    id: "biography-demis-hassabis-deepmind",
    slug: "biography-demis-hassabis-deepmind-nobel-journey",
    title: "Who Is Sir Demis Hassabis? Chess Prodigy, Video Game Pioneer, and Nobel Laureate",
    subtitle: "Inside the extraordinary biography of the London native who decoded the protein universe with AlphaFold.",
    excerpt: "From child prodigy in North London to the Royal Swedish Academy of Sciences, tracing the mind that united biochemistry with artificial intelligence.",
    category: "Biography",
    categorySlug: "biography",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "Sarah Jenkins",
      role: "Senior Investigative Journalist & Biographer",
      avatar: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=240&q=80",
      bio: "Sarah Jenkins writes extensively on corporate leadership, founders' biographies, and political economies."
    },
    publishedAt: "October 3, 2026",
    isoDate: "2026-10-03T09:00:00Z",
    readTime: "8 min read",
    views: "61.9k",
    coverImage: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Molecular structural rendering of AlphaFold protein simulations in London.",
    tags: ["Biography", "Science", "Tech", "AI"],
    contentHtml: `
      <p class="lead-paragraph">At four years old, Demis Hassabis watched his father play chess in their Finchley living room. Within two years, he was beating experienced adults; by thirteen, he was the second-highest ranked player in the world in his age group.</p>
      <p>Yet for Hassabis, chess was never the destination—it was merely the training ground for tackling humanity's grandest biological puzzles.</p>
    `
  },
  {
    id: "entertainment-streaming-wars-reversal",
    slug: "entertainment-streaming-wars-reversal-cinema-boom",
    title: "Why Christopher Nolan Was Right: The Great Cinema Revival Defying Streaming Fatigue",
    subtitle: "Box office figures reveal audiences are flocking back to 70mm film screenings while subscription apps suffer churn.",
    excerpt: "Entertainment critic David H. Miller investigates how physical film distribution outmaneuvered algorithmic streaming models.",
    category: "Entertainment",
    categorySlug: "entertainment",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "David H. Miller",
      role: "Chief Cultural & Society Biographer",
      avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=240&q=80",
      bio: "David Miller writes in-depth celebrity biographies, theatre histories, and profiles of leading artists."
    },
    publishedAt: "October 2, 2026",
    isoDate: "2026-10-02T15:40:00Z",
    readTime: "5 min read",
    views: "31.4k",
    coverImage: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "Traditional cinema projection room operating a 70mm celluloid reel in London's West End.",
    tags: ["Entertainment", "Culture", "Cinema", "Celebrity"],
    contentHtml: `
      <p class="lead-paragraph">After a decade of tech executives claiming that movie theatres were doomed relics of a bygone era, the numbers tell an astonishingly different story.</p>
    `
  },
  {
    id: "business-bank-of-england-rate-shifts",
    slug: "business-bank-of-england-rate-shifts-autumn-forecast",
    title: "Threadneedle Street in Twilight: What the Bank of England's Latest Decision Means for Mortgages",
    subtitle: "With inflation cooling across services, Governor Andrew Bailey signals measured easing for British households.",
    excerpt: "City correspondent Dr. Julian Croft breaks down the Monetary Policy Committee vote and commercial bank reactions.",
    category: "Business",
    categorySlug: "business",
    isHeroMain: false,
    isTrending: false,
    trendingRank: null,
    author: {
      name: "Dr. Julian Croft",
      role: "Financial Markets & Crypto Editor",
      avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=240&q=80",
      bio: "Dr. Croft covers central banks, interest rate derivatives, and British fiscal policy."
    },
    publishedAt: "October 1, 2026",
    isoDate: "2026-10-01T11:20:00Z",
    readTime: "5 min read",
    views: "38.6k",
    coverImage: "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=1000&q=80",
    coverCaption: "The historic Bank of England facade in the City of London.",
    tags: ["Business", "Finance", "UK", "Economy"],
    contentHtml: `
      <p class="lead-paragraph">Inside the Court Room at Threadneedle Street, the mood among central bankers was noticeably less combative this month as long-awaited service-sector wage moderation took hold.</p>
    `
  }
];

// Categories matching southmag.co.uk
const CATEGORIES_DATA = [
  {
    name: "Biography",
    slug: "biography",
    description: "In-depth profiles, untold stories, and career retrospectives of world-shaping figures.",
    count: 36,
    cover: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "News",
    slug: "news",
    description: "Breaking global developments, political investigations, and sovereign policy analysis.",
    count: 48,
    cover: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Business",
    slug: "business",
    description: "Corporate boardrooms, executive strategies, private equity, and British industry.",
    count: 42,
    cover: "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Tech",
    slug: "tech",
    description: "Hardware, microchips, sovereign infrastructure, and the innovators transforming industry.",
    count: 38,
    cover: "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "AI",
    slug: "ai",
    description: "Frontier machine intelligence, neural models, clinical health breakthroughs, and ethics.",
    count: 31,
    cover: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Crypto",
    slug: "crypto",
    description: "Digital assets, sovereign vaults, decentralized protocols, and institutional custody.",
    count: 24,
    cover: "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Celebrity",
    slug: "celebrity",
    description: "Exclusive interviews, intimate portraits, and behind-the-scenes insights into icons of our time.",
    count: 29,
    cover: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Lifestyle",
    slug: "lifestyle",
    description: "Contemplative living, architecture, bespoke craftsmanship, and sustainable luxury.",
    count: 26,
    cover: "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Entertainment",
    slug: "entertainment",
    description: "Cinema, theatre, literature, and the creative minds shaping contemporary culture.",
    count: 22,
    cover: "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?auto=format&fit=crop&w=800&q=80"
  },
  {
    name: "Real Estate",
    slug: "real-estate",
    description: "Prime central property, historic country estates, and the economics of global housing.",
    count: 19,
    cover: "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=800&q=80"
  }
];

if (typeof window !== "undefined") {
  window.ARTICLES_DATA = ARTICLES_DATA;
  window.CATEGORIES_DATA = CATEGORIES_DATA;
}
