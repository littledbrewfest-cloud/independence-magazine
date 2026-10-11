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

def render_article_html(article):
    canonical_url = f"https://www.independencemagazine.com{article['url']}"
    
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{article['title']} | Independence Magazine</title>
  <meta name="description" content="{article['excerpt']}">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph / Social Meta Tags -->
  <meta property="og:type" content="article">
  <meta property="og:title" content="{article['title']}">
  <meta property="og:description" content="{article['excerpt']}">
  <meta property="og:image" content="https://www.independencemagazine.com/{article['coverImage']}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:site_name" content="Independence Magazine">
  <meta property="article:published_time" content="{article['isoDate']}">
  <meta property="article:section" content="{article['category']}">

  <!-- Twitter Meta Tags -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{article['title']}">
  <meta name="twitter:description" content="{article['excerpt']}">
  <meta name="twitter:image" content="https://www.independencemagazine.com/{article['coverImage']}">

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
    /* Standalone Article Navbar: Clean Left Logo & Right Controls (No Clustering) */
    .article-navbar-inner {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 62px;
      width: 100%;
    }}
    .article-navbar-inner .brand-masthead {{
      display: inline-flex;
      flex-direction: column;
      align-items: flex-start;
      text-decoration: none;
    }}
    .article-navbar-inner .brand-title {{
      font-family: var(--font-serif);
      font-size: 1.85rem;
      font-weight: 900;
      letter-spacing: -0.025em;
      color: var(--text-primary);
      line-height: 1;
    }}
    .article-navbar-inner .brand-subtitle {{
      font-family: var(--font-sans);
      font-size: 0.62rem;
      font-weight: 800;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: var(--text-muted);
      margin-top: 3px;
    }}
    .article-navbar-inner .header-actions {{
      display: flex;
      align-items: center;
      gap: 14px;
      margin-left: auto;
    }}
    @media (max-width: 600px) {{
      .article-navbar-inner .brand-title {{
        font-size: 1.45rem;
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
  </style>

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "NewsArticle",
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{canonical_url}"
    }},
    "headline": "{article['title']}",
    "description": "{article['excerpt']}",
    "image": [
      "https://www.independencemagazine.com/{article['coverImage']}"
    ],
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
        <a href="/" style="font-weight: 700; color: var(--text-primary); display: flex; align-items: center; gap: 6px;">
          &larr; Independence Magazine Homepage
        </a>
      </div>
      <div class="top-bar-right">
        <span>Verified Independent Press</span>
      </div>
    </div>
  </aside>

  <!-- Sticky Header with Clean Left-Aligned Logo and Right-Aligned Actions -->
  <header class="site-header">
    <div class="container article-navbar-inner">
      <a href="/" class="brand-masthead">
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
  </header>

  <!-- Main Article Container -->
  <main class="standalone-article-container">
    <div class="article-breadcrumb">
      <a href="/">Home</a>
      <span>/</span>
      <a href="/#{article['categorySlug']}" style="color: var(--accent-crimson); font-weight: 600;">{article['category']}</a>
      <span>/</span>
      <span style="color: var(--text-primary);">{article['title']}</span>
    </div>

    <header class="reader-article-header">
      <span class="category-badge" style="margin-bottom: 14px;">{article['category']}</span>
      <h1 class="reader-title">{article['title']}</h1>
      <p class="reader-subtitle">{article['subtitle']}</p>

      <div class="reader-author-bar">
        <div class="author-pill">
          <img src="{article['author']['avatar']}" alt="{article['author']['name']}">
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

    <figure class="reader-cover-box">
      <img src="/{article['coverImage']}" alt="{article['title']}" style="width: 100%; border-radius: var(--radius-sm); display: block;">
      <figcaption class="reader-caption">{article['coverCaption']}</figcaption>
    </figure>

    <div class="reader-prose">
      {article['contentHtml']}
    </div>

    <!-- Author Bio Box -->
    <div style="background-color: var(--bg-secondary); border: 1px solid var(--border-light); border-left: 3px solid var(--accent-crimson); border-radius: var(--radius-xs); padding: 22px; margin-top: 50px; display: flex; gap: 18px; align-items: center;">
      <img src="{article['author']['avatar']}" alt="{article['author']['name']}" style="width: 64px; height: 64px; border-radius: 50%; object-fit: cover; border: 1px solid var(--border-light);">
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
  </script>
</body>
</html>"""

def main():
    categories_data = [
      {
        "name": "Biography",
        "slug": "biography",
        "description": "In-depth profiles, verified histories, and untold lives of influential global figures.",
        "count": 5,
        "cover": "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=800&q=80"
      },
      {
        "name": "Celebrity",
        "slug": "celebrity",
        "description": "Profiles of prominent personalities, public relationships, and cultural legacies.",
        "count": 4,
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

    print("3. Updating sitemap.xml with all clean URLs...")
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- Core Publication Pages -->
  <url>
    <loc>https://www.independencemagazine.com/</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/about.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/contact.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/editorial-policy.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/privacy-policy.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/terms-of-service.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.independencemagazine.com/disclaimer.html</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>
"""
    for art in ALL_ARTICLES:
        sitemap_xml += f"""  <url>
    <loc>https://www.independencemagazine.com{art['url']}</loc>
    <lastmod>2026-10-11</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
"""
    sitemap_xml += "</urlset>\n"

    with open(SITEMAP_FILE, "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print("sitemap.xml updated with all 9 clean URLs!")

if __name__ == "__main__":
    main()
