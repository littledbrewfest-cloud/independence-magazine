/**
 * Independence Magazine - Reader View & Editorial Typography Controller
 * Designed by DigitalRank.io
 */

const ReaderModal = {
  activeArticle: null,
  fontSizeLevel: 1, // 0: Small, 1: Normal, 2: Large, 3: Extra Large
  fontFamily: "serif", // 'serif' | 'sans'

  init() {
    this.modalEl = document.getElementById("readerModal");
    this.progressBar = document.getElementById("readingProgressBar");
    this.proseContainer = document.getElementById("readerProseContent");
    this.titleEl = document.getElementById("readerTitle");
    this.subtitleEl = document.getElementById("readerSubtitle");
    this.categoryEl = document.getElementById("readerCategory");
    this.authorAvatarEl = document.getElementById("readerAuthorAvatar");
    this.authorNameEl = document.getElementById("readerAuthorName");
    this.authorRoleEl = document.getElementById("readerAuthorRole");
    this.dateEl = document.getElementById("readerDate");
    this.readTimeEl = document.getElementById("readerReadTime");
    this.coverImgEl = document.getElementById("readerCoverImg");
    this.coverCaptionEl = document.getElementById("readerCoverCaption");
    this.authorBioEl = document.getElementById("readerAuthorBio");
    this.authorBioNameEl = document.getElementById("readerBioName");
    this.authorBioRoleEl = document.getElementById("readerBioRole");
    this.authorBioImgEl = document.getElementById("readerBioImg");

    // Close button
    document.querySelectorAll(".close-reader-trigger").forEach(btn => {
      btn.addEventListener("click", () => this.close());
    });

    // Font size controls
    document.getElementById("btnFontDecrease")?.addEventListener("click", () => this.adjustFontSize(-1));
    document.getElementById("btnFontIncrease")?.addEventListener("click", () => this.adjustFontSize(1));

    // Font type toggle
    document.getElementById("btnFontToggle")?.addEventListener("click", () => this.toggleFontFamily());

    // Share button
    document.getElementById("btnReaderShare")?.addEventListener("click", () => this.shareCurrentArticle());

    // Bookmark button
    document.getElementById("btnReaderBookmark")?.addEventListener("click", () => this.toggleBookmarkCurrent());

    // Scroll progress listener inside reader modal
    if (this.modalEl) {
      this.modalEl.addEventListener("scroll", () => this.handleScrollProgress());
    }

    // Keyboard ESC to close
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && this.isOpen()) {
        this.close();
      }
    });

    // Check URL hash on page load (e.g. #article/sovereign-compute-frontiers)
    window.addEventListener("hashchange", () => this.handleHashRoute());
    this.handleHashRoute();
  },

  handleHashRoute() {
    const hash = window.location.hash;
    if (hash.startsWith("#article/")) {
      const articleId = hash.replace("#article/", "");
      this.open(articleId, false);
    }
  },

  isOpen() {
    return this.modalEl && this.modalEl.classList.contains("active");
  },

  open(articleId, updateHistory = true) {
    const article = window.ARTICLES_DATA?.find(a => a.id === articleId || a.slug === articleId);
    if (!article) return;

    this.activeArticle = article;

    // Populate metadata
    this.categoryEl.textContent = article.category;
    this.titleEl.textContent = article.title;
    this.subtitleEl.textContent = article.subtitle || article.excerpt;
    this.authorAvatarEl.src = article.author.avatar;
    this.authorAvatarEl.alt = article.author.name;
    this.authorNameEl.textContent = article.author.name;
    this.authorRoleEl.textContent = article.author.role;
    this.dateEl.textContent = article.publishedAt;
    this.readTimeEl.textContent = article.readTime;

    // Cover
    this.coverImgEl.src = article.coverImage;
    this.coverImgEl.alt = article.title;
    this.coverCaptionEl.textContent = article.coverCaption || `Cover photograph: ${article.title}`;

    // Prose Body
    this.proseContainer.innerHTML = article.contentHtml;

    // Bio
    if (this.authorBioEl) {
      this.authorBioNameEl.textContent = article.author.name;
      this.authorBioRoleEl.textContent = article.author.role;
      this.authorBioEl.textContent = article.author.bio || `Special contributor to Independence Magazine.`;
      this.authorBioImgEl.src = article.author.avatar;
    }

    // Related articles preview
    this.renderRelatedArticles(article);

    // Apply font settings
    this.applyTypographySettings();

    // Show modal
    this.modalEl.classList.add("active");
    this.modalEl.scrollTop = 0;
    document.body.style.overflow = "hidden";

    if (updateHistory) {
      history.pushState(null, "", `#article/${article.id}`);
    }

    // Update bookmark icon state
    this.updateBookmarkButtonState();
  },

  close() {
    if (!this.isOpen()) return;
    this.modalEl.classList.remove("active");
    document.body.style.overflow = "";
    if (window.location.hash.startsWith("#article/")) {
      history.pushState(null, "", window.location.pathname);
    }
  },

  handleScrollProgress() {
    if (!this.modalEl) return;
    const scrollTop = this.modalEl.scrollTop;
    const scrollHeight = this.modalEl.scrollHeight - this.modalEl.clientHeight;
    if (scrollHeight > 0) {
      const percent = Math.min(100, Math.max(0, (scrollTop / scrollHeight) * 100));
      this.progressBar.style.width = `${percent}%`;
    }
  },

  adjustFontSize(delta) {
    this.fontSizeLevel = Math.max(0, Math.min(3, this.fontSizeLevel + delta));
    this.applyTypographySettings();
  },

  toggleFontFamily() {
    this.fontFamily = this.fontFamily === "serif" ? "sans" : "serif";
    this.applyTypographySettings();
    const btn = document.getElementById("btnFontToggle");
    if (btn) {
      btn.textContent = this.fontFamily === "serif" ? "Serif" : "Sans";
    }
  },

  applyTypographySettings() {
    if (!this.proseContainer) return;
    const sizes = ["1.05rem", "1.18rem", "1.32rem", "1.48rem"];
    this.proseContainer.style.fontSize = sizes[this.fontSizeLevel];
    this.proseContainer.style.fontFamily = this.fontFamily === "serif" ? "var(--font-serif)" : "var(--font-sans)";
  },

  shareCurrentArticle() {
    if (!this.activeArticle) return;
    const shareData = {
      title: this.activeArticle.title,
      text: this.activeArticle.excerpt,
      url: window.location.href
    };

    if (navigator.share) {
      navigator.share(shareData).catch(() => {});
    } else {
      navigator.clipboard.writeText(window.location.href);
      if (window.App) {
        window.App.showToast("Article link copied to clipboard");
      }
    }
  },

  toggleBookmarkCurrent() {
    if (!this.activeArticle) return;
    let bookmarks = JSON.parse(localStorage.getItem("independence_bookmarks") || "[]");
    const exists = bookmarks.some(b => b.id === this.activeArticle.id);

    if (exists) {
      bookmarks = bookmarks.filter(b => b.id !== this.activeArticle.id);
      if (window.App) window.App.showToast("Story removed from your Reading List");
    } else {
      bookmarks.push({
        id: this.activeArticle.id,
        title: this.activeArticle.title,
        category: this.activeArticle.category,
        readTime: this.activeArticle.readTime
      });
      if (window.App) window.App.showToast("Saved to your Reading List");
    }

    localStorage.setItem("independence_bookmarks", JSON.stringify(bookmarks));
    this.updateBookmarkButtonState();
  },

  updateBookmarkButtonState() {
    const btn = document.getElementById("btnReaderBookmark");
    if (!btn || !this.activeArticle) return;
    const bookmarks = JSON.parse(localStorage.getItem("independence_bookmarks") || "[]");
    const exists = bookmarks.some(b => b.id === this.activeArticle.id);
    btn.style.color = exists ? "var(--accent-gold)" : "";
  },

  renderRelatedArticles(currentArticle) {
    const container = document.getElementById("readerRelatedStories");
    if (!container) return;

    const related = window.ARTICLES_DATA
      .filter(a => a.id !== currentArticle.id)
      .slice(0, 3);

    container.innerHTML = related.map(item => `
      <div class="hero-sub-card" onclick="ReaderModal.open('${item.id}')">
        <div class="hero-sub-thumb">
          <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
        </div>
        <div class="hero-sub-details">
          <span class="category-badge gold" style="align-self: flex-start;">${item.category}</span>
          <h4 class="hero-sub-title">${item.title}</h4>
          <span class="article-meta-item" style="font-size: 0.76rem; color: var(--text-muted);">${item.readTime}</span>
        </div>
      </div>
    `).join("");
  }
};

window.ReaderModal = ReaderModal;
