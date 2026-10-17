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
            <img src="{img_url}" alt="{clean_caption}" width="600" height="338" loading="lazy">
          </div>
          <div class="hero-sub-details">
            <span class="category-badge dark" style="align-self: flex-start;">{art['category']}</span>
            <h3 class="hero-sub-title"><a href="{art['url']}" style="color: inherit; text-decoration: none;">{art['title']}</a></h3>
            <div class="article-meta" style="font-size: 0.74rem;">
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
    sub_arts = [a for a in ALL_ARTICLES if a.get("isHeroSub")][:3]
    trending_arts = sorted([a for a in ALL_ARTICLES if a.get("isTrending")], key=lambda x: x.get("trendingRank", 99))[:6]

    hero_main_html = "\n" + generate_hero_main(main_art) + "\n        "
    hero_subs_html = "\n" + "\n".join(generate_hero_sub(a) for a in sub_arts) + "\n          "
    trending_html = "\n" + "\n".join(generate_trending(a, idx + 1) for idx, a in enumerate(trending_arts)) + "\n          "
    latest_html = "\n" + "\n".join(generate_magazine_card(a) for a in ALL_ARTICLES) + "\n      "

    # Replace heroMainArticleWrap content
    html = re.sub(
        r'(<div id="heroMainArticleWrap">)(.*?)(</div>\s*<!-- 3 Secondary)',
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

    # Replace latestArticlesGrid content
    html = re.sub(
        r'(<div class="magazine-grid" id="latestArticlesGrid">)(.*?)(</div>\s*</section>)',
        rf'\1{latest_html}\3',
        html,
        flags=re.DOTALL
    )

    # Cache buster on script tags
    html = re.sub(
        r'<script src="/?js/articles-data.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/articles-data.js?v=20261017a"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/reader-modal.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/reader-modal.js?v=20261017a"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/search-filter.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/search-filter.js?v=20261017a"></script>',
        html
    )
    html = re.sub(
        r'<script src="/?js/app.js(\?v=[^"]*)?"></script>',
        r'<script src="/js/app.js?v=20261017a"></script>',
        html
    )

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html pre-rendered with all {len(ALL_ARTICLES)} articles, Lead Hero, and cache-busting scripts!")

if __name__ == "__main__":
    prerender()
