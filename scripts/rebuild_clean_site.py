import os
import json
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))
ARTICLES_DATA_FILE = os.path.join(BASE_DIR, "js", "articles-data.js")
SITEMAP_FILE = os.path.join(BASE_DIR, "sitemap.xml")

# Import all 9 high-depth fact-checked articles
sys.path.append(SCRIPT_DIR)
from articles_database import ALL_ARTICLES

def xml_escape(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&apos;"))

def render_article_html(article):
    canonical_url = f"https://www.independencemagazine.com{article['url']}"
    
    clean_caption = article['coverCaption'].replace('"', '&quot;')
    clean_title = article['title'].replace('"', '&quot;')

    # Compute 3 related articles (prefer same category, fallback to others)
    related_candidates = [a for a in ALL_ARTICLES if a['id'] != article['id']]
    same_cat = [a for a in related_candidates if a['categorySlug'] == article['categorySlug']]
    diff_cat = [a for a in related_candidates if a['categorySlug'] != article['categorySlug']]
    curated_related = (same_cat + diff_cat)[:3]

    related_cards_html = ""
    for rel in curated_related:
        rel_caption = rel['coverCaption'].replace('"', '&quot;')
        related_cards_html += f"""
        <a href="{rel['url']}" class="related-profile-card" style="display: flex; flex-direction: column; text-decoration: none; background: var(--bg-secondary); border: 1px solid var(--border-light); border-radius: var(--radius-xs); overflow: hidden; transition: transform 0.2s ease, box-shadow 0.2s ease;">
          <div style="width: 100%; aspect-ratio: 16/9; overflow: hidden;">
            <img src="/{rel['coverImage']}" alt="{rel_caption}" width="600" height="338" style="width: 100%; height: 100%; object-fit: cover; display: block;" loading="lazy">
          </div>
          <div style="padding: 14px; display: flex; flex-direction: column; flex-grow: 1;">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--accent-crimson); text-transform: uppercase; margin-bottom: 6px;">{rel['category']}</span>
            <h4 style="font-family: var(--font-serif); font-size: 0.98rem; font-weight: 700; color: var(--text-primary); line-height: 1.35; margin-bottom: 8px;">{rel['title']}</h4>
            <span style="font-size: 0.74rem; color: var(--text-muted); margin-top: auto;">{rel['readTime']} &bull; By {rel['author']['name']}</span>
          </div>
        </a>"""

    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{article['title']} | Independence Magazine</title>
  <meta name="description" content="{article['excerpt']}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Social Meta Tags (Google Images & Discover Enhanced) -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{clean_title}">
  <meta property="og:description" content="{article['excerpt']}">
  <meta property="og:image" content="https://www.independencemagazine.com/{article['coverImage']}">
  <meta property="og:image:secure_url" content="https://www.independencemagazine.com/{article['coverImage']}">
  <meta property="og:image:type" content="image/jpeg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="675">
  <meta property="og:image:alt" content="{clean_caption}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="Independence Magazine">
  <meta property="article:published_time" content="{article['isoDate']}">
  <meta property="article:section" content="{article['category']}">

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{clean_title}">
  <meta name="twitter:description" content="{article['excerpt']}">
  <meta name="twitter:image" content="https://www.independencemagazine.com/{article['coverImage']}">
  <meta name="twitter:image:alt" content="{clean_caption}">

  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="shortcut icon" href="/favicon.ico">

  <!-- Google Fonts Preconnect -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,400;1,600&display=swap" rel="stylesheet">

  <!-- CSS Stylesheets -->
  <link rel="stylesheet" href="/styles/main.css">
  <link rel="stylesheet" href="/styles/components.css">
  <link rel="stylesheet" href="/styles/responsive.css">

  <style>
    /* Standalone Article Navbar: Perfectly Centered Masthead Logo */
    .article-navbar-inner {{
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      height: 64px;
      width: 100%;
    }}
    .article-navbar-inner .header-nav-left {{
      display: flex;
      align-items: center;
      justify-self: start;
    }}
    .article-navbar-inner .header-home-btn {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 7px 14px;
      border-radius: var(--radius-xs);
      background: var(--bg-secondary);
      border: 1px solid var(--border-light);
      transition: all 0.15s ease;
    }}
    .article-navbar-inner .header-home-btn:hover {{
      color: var(--accent-crimson);
      border-color: var(--accent-crimson);
      transform: translateX(-2px);
    }}
    .article-navbar-inner .brand-masthead {{
      display: inline-flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      text-decoration: none;
      justify-self: center;
    }}
    .article-navbar-inner .brand-title {{
      font-family: var(--font-serif);
      font-size: 2rem;
      font-weight: 900;
      letter-spacing: -0.025em;
      color: var(--text-primary);
      line-height: 1;
      text-align: center;
    }}
    .article-navbar-inner .brand-subtitle {{
      font-family: var(--font-sans);
      font-size: 0.62rem;
      font-weight: 800;
      letter-spacing: 0.24em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: 4px;
      text-align: center;
    }}
    .article-navbar-inner .header-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
      justify-self: end;
    }}
    .reading-progress-bar {{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: var(--accent-crimson);
      transition: width 0.08s ease;
      z-index: 101;
    }}
    @media (max-width: 680px) {{
      .article-navbar-inner .brand-title {{
        font-size: 1.45rem;
      }}
      .article-navbar-inner .header-home-btn span {{
        display: none;
      }}
      .article-navbar-inner .header-home-btn {{
        padding: 8px 10px;
      }}
    }}

    /* Desktop Easy-Reading Container & Balanced Gutters */
    .standalone-article-container {{
      width: 100%;
      max-width: 800px;
      margin: 36px auto 80px auto;
      padding-left: 24px;
      padding-right: 24px;
      box-sizing: border-box;
    }}
    @media (max-width: 768px) {{
      .standalone-article-container {{
        margin: 20px auto 50px auto;
        padding-left: 16px;
        padding-right: 16px;
      }}
      .reader-title {{
        font-size: 1.85rem !important;
      }}
    }}
    .article-breadcrumb {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-bottom: 24px;
    }}
    .article-breadcrumb a {{
      color: var(--text-secondary);
      text-decoration: none;
      transition: color 0.15s ease;
    }}
    .article-breadcrumb a:hover {{
      color: var(--accent-crimson);
    }}
    .reader-title {{
      font-family: var(--font-serif);
      font-size: 2.35rem;
      font-weight: 800;
      line-height: 1.25;
      letter-spacing: -0.015em;
      color: var(--text-primary);
      margin-bottom: 14px;
    }}
    .reader-subtitle {{
      font-size: 1.15rem;
      color: var(--text-secondary);
      line-height: 1.55;
      margin-bottom: 22px;
    }}
    .reader-cover-box {{
      margin: 28px 0 36px 0;
      border-radius: var(--radius-sm);
      overflow: hidden;
    }}
    .reader-cover-box img {{
      width: 100%;
      height: auto;
      aspect-ratio: 16 / 9;
      object-fit: cover;
      border-radius: var(--radius-sm);
    }}
    .reader-prose {{
      font-family: var(--font-sans);
      font-size: 1.1rem;
      line-height: 1.85;
      color: var(--text-primary);
    }}
    .reader-prose p {{
      margin-bottom: 1.5em;
    }}
    .reader-prose h2 {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 700;
      margin-top: 2em;
      margin-bottom: 0.7em;
      line-height: 1.3;
      color: var(--text-primary);
    }}
    .bio-quick-facts-box {{
      margin: 28px 0;
    }}
    .related-profile-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-sm);
    }}
    .inline-related-box a:hover {{
      text-decoration: underline !important;
    }}
  </style>

  <!-- Google Structured Data (Schema.org NewsArticle & Rich ImageObject) -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{canonical_url}"
    }},
    "headline": "{clean_title}",
    "description": "{article['excerpt']}",
    "image": {{
      "@type": "ImageObject",
      "url": "https://www.independencemagazine.com/{article['coverImage']}",
      "contentUrl": "https://www.independencemagazine.com/{article['coverImage']}",
      "caption": "{clean_caption}",
      "description": "{clean_title}",
      "width": 1200,
      "height": 675
    }},
    "primaryImageOfPage": {{
      "@type": "ImageObject",
      "url": "https://www.independencemagazine.com/{article['coverImage']}",
      "caption": "{clean_caption}",
      "width": 1200,
      "height": 675
    }},
    "datePublished": "{article['isoDate']}",
    "dateModified": "{article['isoDate']}",
    "author": {{
      "@type": "Person",
      "name": "{article['author']['name']}",
      "jobTitle": "{article['author']['role']}"
    }},
    "publisher": {{
      "@type": "NewsMediaOrganization",
      "name": "Independence Magazine",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://www.independencemagazine.com/assets/favicon.svg"
      }}
    }}
  }}
  </script>
</head>
<body>
  <!-- Top Utility Bar -->
  <aside class="top-utility-bar" aria-label="Edition Bar">
    <div class="container top-bar-inner">
      <div class="top-bar-left">
        <span>Verified Independent Press &bull; Editorial Edition</span>
      </div>
      <div class="top-bar-right">
        <span>{article['publishedAt']}</span>
      </div>
    </div>
  </aside>

  <!-- Sticky Header with Centered Masthead and Balanced Actions -->
  <header class="site-header" style="position: sticky; top: 0; z-index: 100; background: var(--bg-primary); border-bottom: 1px solid var(--border-light);">
    <div class="container article-navbar-inner">
      <div class="header-nav-left">
        <a href="/" class="header-home-btn" title="Back to Homepage">
          <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 19.5 3 12m0 0 7.5-7.5M3 12h18"/></svg>
          <span>Home</span>
        </a>
      </div>

      <a href="/" class="brand-masthead" aria-label="Independence Magazine Home">
        <span class="brand-title">Independence<span class="dot-accent">.</span></span>
        <span class="brand-subtitle">MAGAZINE</span>
      </a>

      <div class="header-actions">
        <button class="theme-switch-btn" id="articleThemeBtn" title="Toggle Appearance">
          <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" /></svg>
        </button>
        <a href="/#newsletterSection" class="btn btn-primary btn-sm">Subscribe</a>
      </div>
    </div>
    <div class="reading-progress-bar" id="readingProgressBar"></div>
  </header>

  <!-- Main Article Container -->
  <main class="standalone-article-container">
    <div class="article-breadcrumb">
      <a href="/">Home</a>
      <span>/</span>
      <a href="/#{article['categorySlug']}" style="color: var(--accent-crimson); font-weight: 600;">{article['category']}</a>
      <span>/</span>
      <span style="color: var(--text-primary); max-width: 420px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; display: inline-block; vertical-align: bottom;">{article['title']}</span>
    </div>

    <header class="reader-article-header">
      <span class="category-badge" style="margin-bottom: 14px;">{article['category']}</span>
      <h1 class="reader-title">{article['title']}</h1>
      <p class="reader-subtitle">{article['subtitle']}</p>

      <div class="reader-author-bar">
        <div class="author-pill">
          <img src="{article['author']['avatar']}" alt="{article['author']['name']}" width="40" height="40">
          <div>
            <div class="author-name">By {article['author']['name']}</div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">{article['author']['role']}</div>
          </div>
        </div>
        <div class="article-meta">
          <span>{article['readTime']}</span>
          <span class="article-meta-divider"></span>
          <span>{article['publishedAt']}</span>
        </div>
      </div>
    </header>

    <!-- Semantic Cover Image with Schema Microdata & SEO Attributes -->
    <figure class="reader-cover-box" itemscope itemtype="https://schema.org/ImageObject">
      <img itemprop="contentUrl"
           src="/{article['coverImage']}" 
           alt="{clean_caption}" 
           title="{clean_title}" 
           width="1200" 
           height="675" 
           fetchpriority="high" 
           loading="eager" 
           style="width: 100%; height: auto; aspect-ratio: 16/9; object-fit: cover; border-radius: var(--radius-sm); display: block;">
      <figcaption class="reader-caption" itemprop="caption">{article['coverCaption']}</figcaption>
    </figure>

    <div class="reader-prose">
      {article['contentHtml']}
    </div>

    <!-- Internal Linking: Related Biographies Grid -->
    <section class="related-profiles-section" style="margin-top: 50px; padding-top: 32px; border-top: 1px solid var(--border-light);">
      <h3 style="font-family: var(--font-serif); font-size: 1.45rem; font-weight: 800; margin-bottom: 20px; color: var(--text-primary);">
        Related Biographies & Recommended Reads
      </h3>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 18px;">
        {related_cards_html}
      </div>
    </section>

    <!-- Author Bio Box -->
    <div style="background-color: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 3px solid var(--accent-crimson); border-radius: var(--radius-xs); padding: 22px; margin-top: 50px; display: flex; gap: 18px; align-items: center;">
      <img src="{article['author']['avatar']}" alt="{article['author']['name']}" width="64" height="64" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; border: 1px solid var(--border-light);">
      <div>
        <h4 style="font-family: var(--font-serif); font-size: 1.15rem; font-weight: 700; margin-bottom: 2px;">{article['author']['name']}</h4>
        <div style="font-size: 0.74rem; color: var(--accent-crimson); text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">{article['author']['role']}</div>
        <p style="font-size: 0.9rem; color: var(--text-secondary); line-height: 1.5;">{article['author']['bio']}</p>
      </div>
    </div>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container" style="text-align: center;">
      <div class="brand-masthead" style="align-items: center; margin-bottom: 12px;">
        <span class="brand-title" style="color: #ffffff; font-size: 2.2rem;">Independence<span class="dot-accent">.</span></span>
        <span class="brand-subtitle" style="color: #64748b; font-size: 0.68rem; margin-top: 4px;">MAGAZINE</span>
      </div>
      <p style="font-size: 0.84rem; color: var(--text-muted); margin-bottom: 18px;">
        Authoritative biographical profiles and investigative journalism.
      </p>
      <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; margin-bottom: 18px; font-size: 0.82rem;">
        <a href="/about.html" style="color: #cbd5e1;">About</a>
        <a href="/editorial-policy.html" style="color: #cbd5e1;">Editorial Charter</a>
        <a href="/contact.html" style="color: #cbd5e1;">Contact</a>
        <a href="/privacy-policy.html" style="color: #cbd5e1;">Privacy Policy</a>
        <a href="/terms-of-service.html" style="color: #cbd5e1;">Terms of Service</a>
        <a href="/disclaimer.html" style="color: #cbd5e1;">Disclaimer</a>
      </div>
      <div style="font-size: 0.78rem; color: #64748b;">
        &copy; 2026 Independence Magazine. All Rights Reserved. &bull; Contact: <a href="mailto:info.washingtontimes@gmail.com" style="color: inherit;">info.washingtontimes@gmail.com</a> &bull; Digital Partner: <a href="https://digitalrank.io" target="_blank" rel="noopener" style="color: #38bdf8;">DigitalRank.io</a>
      </div>
    </div>
  </footer>

  <script>
    const savedTheme = localStorage.getItem("independence_theme") || "light";
    document.documentElement.setAttribute("data-theme", savedTheme);

    document.getElementById('articleThemeBtn')?.addEventListener('click', () => {{
      const curr = document.documentElement.getAttribute("data-theme") || "light";
      const next = curr === "light" ? "dark" : "light";
      document.documentElement.setAttribute("data-theme", next);
      localStorage.setItem("independence_theme", next);
    }});

    // Reading progress bar
    window.addEventListener('scroll', () => {{
      const bar = document.getElementById('readingProgressBar');
      if (!bar) return;
      const totalH = document.documentElement.scrollHeight - window.innerHeight;
      const progress = totalH > 0 ? (window.scrollY / totalH) * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, progress)) + '%';
    }});
  </script>
</body>
</html>"""

def main():
    bio_count = len([a for a in ALL_ARTICLES if a['categorySlug'] == 'biography'])
    celeb_count = len([a for a in ALL_ARTICLES if a['categorySlug'] == 'celebrity'])
    categories_data = [
      {
        "name": "Biography",
        "slug": "biography",
        "description": "In-depth profiles, verified histories, and untold lives of influential global figures.",
        "count": bio_count,
        "cover": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Celebrity",
        "slug": "celebrity",
        "description": "Profiles of prominent personalities, public relationships, and cultural legacies.",
        "count": celeb_count,
        "cover": "https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Culture",
        "slug": "culture",
        "description": "Critical analysis of arts, heritage, societal movements, and modern discourse.",
        "count": 3,
        "cover": "https://images.unsplash.com/photo-1499781350541-7783f6c6a0c8?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Business",
        "slug": "business",
        "description": "Strategic enterprise, executive leadership, capital allocation, and market dynamics.",
        "count": 2,
        "cover": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=800&q=80"
      }
    ]

    js_content = f"""/**
 * Independence Magazine - Celebrity & Biographical Journalism Repository
 * Authentic Editorial Standards & Fact-Checked Biographies
 */

const ARTICLES_DATA = {json.dumps(ALL_ARTICLES, indent=2)};

const CATEGORIES_DATA = {json.dumps(categories_data, indent=2)};

if (typeof window !== 'undefined') {{
  window.ARTICLES_DATA = ARTICLES_DATA;
  window.CATEGORIES_DATA = CATEGORIES_DATA;
}}
"""
    with open(ARTICLES_DATA_FILE, "w", encoding="utf-8") as f:
        f.write(js_content)
    print("articles-data.js updated successfully!")

    print("2. Generating clean static URL directories and index.html files...")
    for art in ALL_ARTICLES:
        slug_dir = os.path.join(BASE_DIR, art["slug"])
        os.makedirs(slug_dir, exist_ok=True)
        html_file = os.path.join(slug_dir, "index.html")
        html_content = render_article_html(art)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"Generated clean URL page: /{art['slug']}/index.html")

    print("3. Updating sitemap.xml with Google Image Extension and clean URLs...")
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">
  <!-- Core Publication Pages -->
  <url>
    <loc>https://www.independencemagazine.com/</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/about.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/contact.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/editorial-policy.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/privacy-policy.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/terms-of-service.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/disclaimer.html</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
"""
    for art in ALL_ARTICLES:
        cover_title = xml_escape(f"{art['title']} - Biography Photo")
        cover_caption = xml_escape(art['coverCaption'])
        sitemap_xml += f"""  <url>
    <loc>https://www.independencemagazine.com{art['url']}</loc>
    <lastmod>2026-10-12</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
    <image:image>
      <image:loc>https://www.independencemagazine.com/{art['coverImage']}</image:loc>
      <image:title>{cover_title}</image:title>
      <image:caption>{cover_caption}</image:caption>
    </image:image>"""
        if art['slug'] == 'marlene-knaus':
            sitemap_xml += """
    <image:image>
      <image:loc>https://www.independencemagazine.com/assets/covers/marlene-knaus-middle.jpg</image:loc>
      <image:title>Marlene Knaus alongside Niki Lauda in Formula One Paddock</image:title>
      <image:caption>Marlene Knaus with Niki Lauda during a Grand Prix race weekend in the mid-1970s.</image:caption>
    </image:image>"""
        sitemap_xml += "\n  </url>\n"
    sitemap_xml += "</urlset>\n"

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("sitemap.xml updated with Google Image Extension and all clean URLs!")

if __name__ == "__main__":
    main()
