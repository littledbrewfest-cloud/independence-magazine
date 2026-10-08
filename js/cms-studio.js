/**
 * Independence Magazine - DigitalRank.io Agency Editorial Suite & CMS Publisher
 * Designed and Engineered by DigitalRank.io
 */

const CMSStudio = {
  init() {
    this.drawerBackdrop = document.getElementById("cmsDrawerBackdrop");
    this.form = document.getElementById("cmsPublishForm");
    this.titleInput = document.getElementById("cmsTitle");
    this.categorySelect = document.getElementById("cmsCategory");
    this.excerptInput = document.getElementById("cmsExcerpt");
    this.authorInput = document.getElementById("cmsAuthor");
    this.imageInput = document.getElementById("cmsImageUrl");
    this.contentInput = document.getElementById("cmsContent");

    // SERP Preview elements
    this.serpTitle = document.getElementById("serpPreviewTitle");
    this.serpSnippet = document.getElementById("serpPreviewSnippet");
    this.serpUrl = document.getElementById("serpPreviewUrl");

    // SEO Score elements
    this.scoreValue = document.getElementById("seoScoreValue");
    this.scoreBar = document.getElementById("seoScoreProgressBar");
    this.schemaPreview = document.getElementById("cmsJsonLdPreview");

    // Open/Close triggers
    document.querySelectorAll(".open-cms-trigger").forEach(btn => {
      btn.addEventListener("click", () => this.open());
    });

    document.querySelectorAll(".close-cms-trigger").forEach(btn => {
      btn.addEventListener("click", () => this.close());
    });

    if (this.drawerBackdrop) {
      this.drawerBackdrop.addEventListener("click", (e) => {
        if (e.target === this.drawerBackdrop) this.close();
      });
    }

    // Input listeners for live SEO calculation
    [this.titleInput, this.excerptInput, this.categorySelect, this.authorInput].forEach(el => {
      if (el) el.addEventListener("input", () => this.updateLiveSeoAnalysis());
    });

    // Form submit
    if (this.form) {
      this.form.addEventListener("submit", (e) => {
        e.preventDefault();
        this.publishArticle();
      });
    }

    // Copy Schema Button
    document.getElementById("btnCopySchema")?.addEventListener("click", () => {
      if (this.schemaPreview) {
        navigator.clipboard.writeText(this.schemaPreview.textContent);
        if (window.App) window.App.showToast("Schema.org NewsArticle JSON-LD copied to clipboard");
      }
    });

    // Initial calculation
    this.updateLiveSeoAnalysis();
  },

  open() {
    if (!this.drawerBackdrop) return;
    this.drawerBackdrop.classList.add("active");
    document.body.style.overflow = "hidden";
    this.updateLiveSeoAnalysis();
  },

  close() {
    if (!this.drawerBackdrop) return;
    this.drawerBackdrop.classList.remove("active");
    document.body.style.overflow = "";
  },

  updateLiveSeoAnalysis() {
    const title = this.titleInput?.value.trim() || "The Sovereign Compute Frontier";
    const excerpt = this.excerptInput?.value.trim() || "From subsea fiber networks to nationalized AI clusters, the geopolitical race for technological autonomy is reshaping global governance.";
    const category = this.categorySelect?.value || "Technology";
    const author = this.authorInput?.value || "Marcus Vance";

    // Update SERP preview
    if (this.serpTitle) {
      this.serpTitle.textContent = `${title} | Independence Magazine`;
    }
    if (this.serpSnippet) {
      this.serpSnippet.textContent = excerpt;
    }
    if (this.serpUrl) {
      const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");
      this.serpUrl.textContent = `https://independencemagazine.com/${category.toLowerCase()}/${slug}`;
    }

    // Calculate SEO score
    let score = 40;
    if (title.length >= 40 && title.length <= 70) score += 25;
    else if (title.length > 20) score += 15;

    if (excerpt.length >= 100 && excerpt.length <= 165) score += 25;
    else if (excerpt.length > 50) score += 15;

    if (author.length > 3) score += 10;

    if (this.scoreValue) this.scoreValue.textContent = `${score}/100`;
    if (this.scoreBar) {
      this.scoreBar.style.width = `${score}%`;
      this.scoreBar.style.background = score > 80 ? "#10b981" : (score > 60 ? "#f59e0b" : "#ef4444");
    }

    // Generate Schema.org JSON-LD
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-");
    const jsonLd = {
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": `https://independencemagazine.com/article/${slug}`
      },
      "headline": title,
      "description": excerpt,
      "articleSection": category,
      "image": [
        this.imageInput?.value || "https://images.unsplash.com/photo-1518770660439-4636190af475"
      ],
      "datePublished": new Date().toISOString(),
      "dateModified": new Date().toISOString(),
      "author": {
        "@type": "Person",
        "name": author,
        "jobTitle": "Investigative Journalist"
      },
      "publisher": {
        "@type": "NewsMediaOrganization",
        "name": "Independence Magazine",
        "url": "https://independencemagazine.com",
        "logo": {
          "@type": "ImageObject",
          "url": "https://independencemagazine.com/assets/logo.png"
        },
        "founder": {
          "@type": "Organization",
          "name": "DigitalRank.io"
        }
      }
    };

    if (this.schemaPreview) {
      this.schemaPreview.textContent = JSON.stringify(jsonLd, null, 2);
    }
  },

  publishArticle() {
    const title = this.titleInput.value.trim();
    const category = this.categorySelect.value;
    const excerpt = this.excerptInput.value.trim();
    const authorName = this.authorInput.value.trim() || "Independence Editorial Board";
    const coverImage = this.imageInput.value.trim() || "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1000&q=80";
    const rawContent = this.contentInput.value.trim();

    if (!title || !excerpt) {
      if (window.App) window.App.showToast("Please provide both a headline and excerpt.");
      return;
    }

    const id = "custom-" + Date.now();
    const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, "-");

    const formattedContent = rawContent
      ? rawContent.split("\n\n").map(p => `<p>${p}</p>`).join("")
      : `<p class="lead-paragraph">${excerpt}</p><p>In this newly filed investigative brief, Independence Magazine examines the rapidly evolving dynamics shaping this domain.</p><h2>Editorial Analysis</h2><p>Our research indicates structural shifts across institutional policies and market indicators.</p>`;

    const newArticle = {
      id: id,
      slug: slug,
      title: title,
      subtitle: excerpt,
      excerpt: excerpt,
      category: category,
      categorySlug: category.toLowerCase().replace(/[^a-z0-9]+/g, "-"),
      isHeroMain: false,
      isHeroSub: false,
      isTrending: false,
      author: {
        name: authorName,
        role: "Editorial Contributor",
        avatar: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=240&q=80",
        bio: `${authorName} writes for Independence Magazine on ${category.toLowerCase()} and strategic trends.`
      },
      publishedAt: "Just now",
      isoDate: new Date().toISOString(),
      readTime: "5 min read",
      views: "1.2k",
      coverImage: coverImage,
      coverCaption: `Staff photograph documenting: ${title}`,
      tags: [category, "Independence Editorial", "Exclusive"],
      contentHtml: formattedContent
    };

    // Prepend to articles array
    window.ARTICLES_DATA.unshift(newArticle);

    // Re-render
    if (window.App) {
      window.App.renderLatestArticles("all");
      window.App.showToast("Article published with valid NewsArticle Schema!");
    }

    this.close();

    // Reset form
    this.form.reset();

    // Open newly published article in reader view
    setTimeout(() => {
      if (window.ReaderModal) {
        window.ReaderModal.open(id);
      }
    }, 400);
  }
};

window.CMSStudio = CMSStudio;
