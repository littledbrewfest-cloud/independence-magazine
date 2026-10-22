import os
import sys
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

sys.path.append(SCRIPT_DIR)
from articles_database import ALL_ARTICLES

def generate_hero_main(art):
    img_url = f"/{art['coverImage'].lstrip('/')}"
    clean_caption = art['coverCaption'].replace('"', '&quot;')
    clean_title = art['title'].replace('"', '&quot;')
    return f"""<article class="hero-main-card" onclick="window.location.href='{art['url']}'" style="cursor: pointer;" aria-label="Lead Story: {clean_title}">
          <div class="hero-main-image-wrap">
            <span class="hero-category-overlay category-badge">{art['category']}</span>
            <img src="{img_url}" alt="{clean_caption}" width="1200" height="675" loading="eager" fetchpriority="high">
          </div>
          <div class="hero-main-content">
            <h2 class="hero-main-headline"><a href="{art['url']}" style="color: inherit; text-decoration: none;">{art['title']}</a></h2>
            <p class="hero-main-excerpt">{art['excerpt']}</p>
            <div class="hero-main-footer">
              <div class="author-pill">
                <img src="{art['author']['avatar']}" alt="{art['author']['name']}">
                <div>
                  <div class="author-name">By {art['author']['name']}</div>
                  <div style="font-size: 0.72rem; color: var(--text-muted);">{art['author']['role']}</div>
                </div>
              </div>
              <div class="article-meta">
                <span class="article-meta-item">
                  <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>
                  {art['readTime']}
                </span>
                <span class="article-meta-divider"></span>
                <span>{art['publishedAt']}</span>
              </div>
            </div>
          </div>
        </article>"""

def generate_hero_sub(art):
    img_url = f"/{art['coverImage'].lstrip('/')}"
    clean_caption = art['coverCaption'].replace('"', '&quot;')
    clean_title = art['title'].replace('"', '&quot;')
    return f"""<article class="hero-sub-card" onclick="window.location.href='{art['url']}'" style="cursor: pointer;" aria-label="Story: {clean_title}">
          <div class="hero-sub-thumb">
            <img src="{img_url}" alt="{clean_caption}" width="300" height="169" loading="lazy">
          </div>
          <div class="hero-sub-details">
            <span class="category-badge dark" style="align-self: flex-start; font-size: 0.65rem; padding: 2px 7px;">{art['category']}</span>
            <h3 class="hero-sub-title"><a href="{art['url']}" style="color: inherit; text-decoration: none;">{art['title']}</a></h3>
            <div class="article-meta" style="font-size: 0.72rem;">
              <span>By {art['author']['name']}</span>
              <span class="article-meta-divider"></span>
              <span>{art['readTime']}</span>
            </div>
          </div>
        </article>"""

def generate_trending(art, rank):
    img_url = f"/{art['coverImage'].lstrip('/')}"
    clean_caption = art['coverCaption'].replace('"', '&quot;')
    clean_title = art['title'].replace('"', '&quot;')
    return f"""<div class="trending-card" onclick="window.location.href='{art['url']}'" style="cursor: pointer;" role="button" tabindex="0">
        <div class="trending-rank">0{rank}</div>
        <div class="trending-thumb">
          <img src="{img_url}" alt="{clean_caption}" width="300" height="169" loading="lazy">
        </div>
        <div class="trending-content">
          <span class="trending-category">{art['category']}</span>
          <h4 class="trending-title"><a href="{art['url']}" style="color: inherit; text-decoration: none;">{art['title']}</a></h4>
          <span style="font-size: 0.72rem; color: var(--text-muted);">{art['readTime']} &bull; {art['views']}</span>
        </div>
      </div>"""

def generate_magazine_card(art):
    img_url = f"/{art['coverImage'].lstrip('/')}"
    clean_caption = art['coverCaption'].replace('"', '&quot;')
    clean_title = art['title'].replace('"', '&quot;')
    date_display = art['publishedAt'].split(',')[0]
    return f"""<article class="magazine-card" onclick="window.location.href='{art['url']}'" style="cursor: pointer;" aria-label="{clean_title}">
        <div class="magazine-card-media">
          <span class="magazine-badge-pos category-badge">{art['category']}</span>
          <img src="{img_url}" alt="{clean_caption}" width="600" height="338" loading="lazy">
        </div>
        <div class="magazine-card-body">
          <h3 class="magazine-card-title"><a href="{art['url']}" style="color: inherit; text-decoration: none;">{art['title']}</a></h3>
          <p class="magazine-card-excerpt">{art['excerpt']}</p>
          <div class="magazine-card-footer">
            <div class="author-pill">
              <img src="{art['author']['avatar']}" alt="{art['author']['name']}">
              <div>
                <span class="author-name" style="font-size: 0.78rem;">By {art['author']['name']}</span>
              </div>
            </div>
            <div class="article-meta">
              <span>{art['readTime']}</span>
              <span class="article-meta-divider"></span>
              <span>{date_display}</span>
            </div>
          </div>
        </div>
      </article>"""

def prerender():
    with open(INDEX_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    main_art = next((a for a in ALL_ARTICLES if a.get("isHeroMain")), ALL_ARTICLES[0])
    sub_arts = [a for a in ALL_ARTICLES if a['slug'] != main_art['slug']][:5]
    trending_arts = sorted([a for a in ALL_ARTICLES if a.get("isTrending")], key=lambda x: x.get("trendingRank", 99))[:6]

    hero_main_html = "\n" + generate_hero_main(main_art) + "\n        "
    hero_subs_html = "\n" + "\n".join(generate_hero_sub(a) for a in sub_arts) + "\n          "
    trending_html = "\n" + "\n".join(generate_trending(a, idx + 1) for idx, a in enumerate(trending_arts)) + "\n          "
    latest_html = "\n" + "\n".join(generate_magazine_card(a) for a in ALL_ARTICLES[:12]) + "\n      "

    # Pre-render pagination for Page 1
    total_pages = (len(ALL_ARTICLES) + 11) // 12
    pages_btns = []
    for p in range(1, total_pages + 1):
        active_cls = "active" if p == 1 else ""
        aria_curr = 'aria-current="page"' if p == 1 else ""
        pages_btns.append(f'<button class="pagination-number {active_cls}" onclick="App.goToPage({p})" aria-label="Page {p}" {aria_curr}>{p}</button>')
    pages_btn_html = "".join(pages_btns)
    pagination_html = f"""
        <button class="pagination-btn pagination-prev" onclick="App.goToPage(1)" disabled aria-label="Previous Page">&larr; Prev</button>
        <div class="pagination-numbers">
          {pages_btn_html}
        </div>
        <button class="pagination-btn pagination-next" onclick="App.goToPage(2)" aria-label="Next Page">Next &rarr;</button>
      """

    # Category Blocks
    bio_count = len([a for a in ALL_ARTICLES if a.get('categorySlug') == 'biography'])
    celeb_count = len([a for a in ALL_ARTICLES if a.get('categorySlug') == 'celebrity'])
    ent_count = len([a for a in ALL_ARTICLES if a.get('categorySlug') == 'entertainment'])
    cats = [
      {
        "name": "Celebrity",
        "slug": "celebrity",
        "description": "High-profile personalities, public marriages, net worth, and life stories.",
        "count": celeb_count,
        "cover": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Biography",
        "slug": "biography",
        "description": "Comprehensive life retrospectives, verified background, and archival career histories.",
        "count": bio_count,
        "cover": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Entertainment",
        "slug": "entertainment",
        "description": "Television, cinema, music lineages, and performing arts features.",
        "count": ent_count or 1,
        "cover": "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "All Stories",
        "slug": "all",
        "description": "Browse our complete archive of fact-checked biographical features and investigative reports.",
        "count": len(ALL_ARTICLES),
        "cover": "https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=800&q=80"
      }
    ]
    def gen_cat(cat):
        return f"""<div class="category-block-card" onclick="App.filterToCategory('{cat['slug']}')" role="button" tabindex="0">
        <div class="category-block-media">
          <img src="{cat['cover']}" alt="{cat['name']}" loading="lazy">
        </div>
        <div class="category-block-body">
          <h3 class="category-block-name">{cat['name']}</h3>
          <p class="category-block-desc">{cat['description']}</p>
          <div class="category-block-footer">
            <span>{cat['count']} STORIES</span>
            <span class="category-block-action">EXPLORE &rarr;</span>
          </div>
        </div>
      </div>"""

    cats_html = "\n" + "\n".join(gen_cat(c) for c in cats) + "\n      "

    # Replace heroMainArticleWrap content
    html = re.sub(
        r'(<div id="heroMainArticleWrap">)(.*?)(</div>\s*<!-- \d+ Secondary|</div>\s*<!-- 3 Secondary)',
        rf'\1{hero_main_html}\3',
        html,
        flags=re.DOTALL
    )

    # Replace heroSubArticlesWrap content
    html = re.sub(
        r'(<div id="heroSubArticlesWrap"[^>]*>)(.*?)(</div>\s*</div>\s*</div>\s*</section>)',
        rf'\1{hero_subs_html}\3',
        html,
        flags=re.DOTALL
    )

    # Replace trendingStoriesTrack content
    html = re.sub(
        r'(<div class="trending-track" id="trendingStoriesTrack"[^>]*>)(.*?)(</div>\s*</div>\s*</div>\s*</section>)',
        rf'\1{trending_html}\3',
        html,
        flags=re.DOTALL
    )

    # Replace latestArticlesGrid and latestPagination content
    html = re.sub(
        r'(<div class="magazine-grid" id="latestArticlesGrid">).*?(<!-- Pagination Controls.*?</div>\s*</section>|</div>\s*<!-- Pagination Controls.*?</div>\s*</section>)',
        rf'\1{latest_html}</div>\n\n      <!-- Pagination Controls (12 articles per page) -->\n      <div class="pagination-container" id="latestPagination">{pagination_html}</div>\n    </section>',
        html,
        flags=re.DOTALL
    )

    # Replace categoryBlocksContainer content if present
    if '<div class="category-blocks-grid" id="categoryBlocksContainer">' in html:
        html = re.sub(
            r'(<div class="category-blocks-grid" id="categoryBlocksContainer">)(.*?)(</div>)',
            rf'\1{cats_html}\3',
            html,
            flags=re.DOTALL
        )

    # Cache buster on script tags
    html = re.sub(
        r'<script src="/?js/articles-data.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/articles-data.js?v=20261022b"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/reader-modal.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/reader-modal.js?v=20261022b"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/search-filter.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/search-filter.js?v=20261022b"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/app.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/app.js?v=20261022b"></script>',
        html
    )

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html pre-rendered with 5 hero stories, 12-item page 1, pagination, and clean categories!")

if __name__ == "__main__":
    prerender()
