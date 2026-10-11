/**
 * Independence Magazine - Core Application Controller
 * Independent Journalism, News & Biographies
 */

const App = {
  theme: "light", // 'light' | 'sepia' | 'dark'

  init() {
    this.initTheme();
    this.initDateTime();
    this.initMobileNav();
    this.renderHeroSection();
    this.renderTrendingSection();
    this.renderLatestArticles("all");
    this.renderCategoryBlocks();
    this.initNewsletter();

    // Init modules
    if (window.ReaderModal) window.ReaderModal.init();
    if (window.SearchFilter) window.SearchFilter.init();

    // Scroll listeners for sticky header compact logo & shadow
    window.addEventListener("scroll", () => {
      const header = document.querySelector(".site-header");
      if (header) {
        if (window.scrollY > 90) {
          header.classList.add("is-sticky");
          header.style.boxShadow = "var(--shadow-md)";
        } else {
          header.classList.remove("is-sticky");
          header.style.boxShadow = "none";
        }
      }
    });

    console.log("Independence Magazine initialized.");
  },

  /* ------------------------------------------------------------------------
     THEME MANAGEMENT (Light / Sepia / Dark)
  ------------------------------------------------------------------------ */
  initTheme() {
    const savedTheme = localStorage.getItem("independence_theme") || "light";
    this.setTheme(savedTheme);

    const themeToggleBtn = document.getElementById("themeToggleBtn");
    if (themeToggleBtn) {
      themeToggleBtn.addEventListener("click", () => {
        const next = this.theme === "light" ? "sepia" : (this.theme === "sepia" ? "dark" : "light");
        this.setTheme(next);
      });
    }
  },

  setTheme(themeName) {
    this.theme = themeName;
    document.documentElement.setAttribute("data-theme", themeName);
    localStorage.setItem("independence_theme", themeName);

    const iconEl = document.getElementById("themeIconSvg");
    if (iconEl) {
      if (themeName === "dark") {
        iconEl.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />`;
      } else if (themeName === "sepia") {
        iconEl.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 0 0 6 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 0 1 6 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 0 1 6-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0 0 18 18a8.967 8.967 0 0 0-6 2.292m0-14.25v14.25" />`;
      } else {
        iconEl.innerHTML = `<path stroke-linecap="round" stroke-linejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />`;
      }
    }
  },

  /* ------------------------------------------------------------------------
     LIVE DATE & EDITION TICKER
  ------------------------------------------------------------------------ */
  initDateTime() {
    const dateEl = document.getElementById("topBarDate");
    if (dateEl) {
      const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
      dateEl.textContent = new Date().toLocaleDateString('en-GB', options);
    }
  },

  /* ------------------------------------------------------------------------
     MOBILE NAVIGATION
  ------------------------------------------------------------------------ */
  initMobileNav() {
    const toggleBtn = document.getElementById("mobileNavToggle");
    const mainNav = document.getElementById("mainNavList");

    if (toggleBtn && mainNav) {
      toggleBtn.addEventListener("click", () => {
        mainNav.classList.toggle("mobile-active");
        const isOpen = mainNav.classList.contains("mobile-active");
        toggleBtn.setAttribute("aria-expanded", isOpen);
      });

      mainNav.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", () => {
          mainNav.classList.remove("mobile-active");
        });
      });
    }
  },

  /* ------------------------------------------------------------------------
     HERO SECTION
  ------------------------------------------------------------------------ */
  renderHeroSection() {
    const mainStory = window.ARTICLES_DATA.find(a => a.isHeroMain) || window.ARTICLES_DATA[0];
    const subStories = window.ARTICLES_DATA.filter(a => a.isHeroSub).slice(0, 3);

    // Main Card
    const mainCardContainer = document.getElementById("heroMainArticleWrap");
    if (mainCardContainer && mainStory) {
      mainCardContainer.innerHTML = `
        <article class="hero-main-card" onclick="window.location.href='/${mainStory.slug}/'" style="cursor: pointer;" aria-label="Lead Story: ${mainStory.title}">
          <div class="hero-main-image-wrap">
            <span class="hero-category-overlay category-badge">${mainStory.category}</span>
            <img src="${mainStory.coverImage}" alt="${mainStory.title}" loading="eager" fetchpriority="high">
          </div>
          <div class="hero-main-content">
            <h2 class="hero-main-headline"><a href="/${mainStory.slug}/" style="color: inherit; text-decoration: none;">${mainStory.title}</a></h2>
            <p class="hero-main-excerpt">${mainStory.excerpt}</p>
            <div class="hero-main-footer">
              <div class="author-pill">
                <img src="${mainStory.author.avatar}" alt="${mainStory.author.name}">
                <div>
                  <div class="author-name">By ${mainStory.author.name}</div>
                  <div style="font-size: 0.72rem; color: var(--text-muted);">${mainStory.author.role}</div>
                </div>
              </div>
              <div class="article-meta">
                <span class="article-meta-item">
                  <svg width="13" height="13" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"></path></svg>
                  ${mainStory.readTime}
                </span>
                <span class="article-meta-divider"></span>
                <span>${mainStory.publishedAt}</span>
              </div>
            </div>
          </div>
        </article>
      `;
    }

    // Sub Stories
    const subStoriesContainer = document.getElementById("heroSubArticlesWrap");
    if (subStoriesContainer) {
      subStoriesContainer.innerHTML = subStories.map(item => `
        <article class="hero-sub-card" onclick="window.location.href='/${item.slug}/'" style="cursor: pointer;" aria-label="Story: ${item.title}">
          <div class="hero-sub-thumb">
            <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
          </div>
          <div class="hero-sub-details">
            <span class="category-badge dark" style="align-self: flex-start;">${item.category}</span>
            <h3 class="hero-sub-title"><a href="/${item.slug}/" style="color: inherit; text-decoration: none;">${item.title}</a></h3>
            <div class="article-meta" style="font-size: 0.74rem;">
              <span>By ${item.author.name}</span>
              <span class="article-meta-divider"></span>
              <span>${item.readTime}</span>
            </div>
          </div>
        </article>
      `).join("");
    }
  },

  /* ------------------------------------------------------------------------
     TRENDING SLIDER ("Trending Now")
  ------------------------------------------------------------------------ */
  renderTrendingSection() {
    const track = document.getElementById("trendingStoriesTrack");
    if (!track) return;

    const trending = window.ARTICLES_DATA.filter(a => a.isTrending);

    track.innerHTML = trending.map((item, idx) => `
      <div class="trending-card" onclick="window.location.href='/${item.slug}/'" style="cursor: pointer;" role="button" tabindex="0">
        <div class="trending-rank">0${item.trendingRank || idx + 1}</div>
        <div class="trending-thumb">
          <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
        </div>
        <div class="trending-content">
          <span class="trending-category">${item.category}</span>
          <h4 class="trending-title"><a href="/${item.slug}/" style="color: inherit; text-decoration: none;">${item.title}</a></h4>
          <span style="font-size: 0.72rem; color: var(--text-muted);">${item.readTime} • ${item.views}</span>
        </div>
      </div>
    `).join("");
  },

  /* ------------------------------------------------------------------------
     LATEST ARTICLES SECTION (3-Col Grid)
  ------------------------------------------------------------------------ */
  renderLatestArticles(categorySlug = "all") {
    const grid = document.getElementById("latestArticlesGrid");
    if (!grid) return;

    let filtered = window.ARTICLES_DATA;
    if (categorySlug !== "all") {
      filtered = window.ARTICLES_DATA.filter(a => a.categorySlug === categorySlug);
    }

    if (filtered.length === 0) {
      grid.innerHTML = `
        <div style="grid-column: 1 / -1; text-align: center; padding: 48px 0; color: var(--text-muted);">
          No stories filed under this category yet. Check back soon.
        </div>
      `;
      return;
    }

    grid.innerHTML = filtered.map(item => `
      <article class="magazine-card" onclick="window.location.href='/${item.slug}/'" style="cursor: pointer;" aria-label="${item.title}">
        <div class="magazine-card-media">
          <span class="magazine-badge-pos category-badge">${item.category}</span>
          <img src="${item.coverImage}" alt="${item.title}" loading="lazy">
        </div>
        <div class="magazine-card-body">
          <h3 class="magazine-card-title"><a href="/${item.slug}/" style="color: inherit; text-decoration: none;">${item.title}</a></h3>
          <p class="magazine-card-excerpt">${item.excerpt}</p>
          <div class="magazine-card-footer">
            <div class="author-pill">
              <img src="${item.author.avatar}" alt="${item.author.name}">
              <div>
                <span class="author-name" style="font-size: 0.78rem;">By ${item.author.name}</span>
              </div>
            </div>
            <div class="article-meta">
              <span>${item.readTime}</span>
              <span class="article-meta-divider"></span>
              <span>${item.publishedAt.split(',')[0]}</span>
            </div>
          </div>
        </div>
      </article>
    `).join("");
  },

  /* ------------------------------------------------------------------------
     CATEGORY SHOWCASE BLOCKS
  ------------------------------------------------------------------------ */
  renderCategoryBlocks() {
    const container = document.getElementById("categoryBlocksContainer");
    if (!container || !window.CATEGORIES_DATA) return;

    container.innerHTML = window.CATEGORIES_DATA.map(cat => `
      <div class="category-block-card" onclick="App.filterToCategory('${cat.slug}')" role="button" tabindex="0">
        <img class="bg-image" src="${cat.cover}" alt="${cat.name}" loading="lazy">
        <div class="category-block-gradient"></div>
        <div class="category-block-content">
          <h3 class="category-block-name">${cat.name}</h3>
          <p class="category-block-desc">${cat.description}</p>
          <div class="category-block-footer">
            <span>${cat.count} ARTICLES</span>
            <span style="display: flex; align-items: center; gap: 4px;">EXPLORE &rarr;</span>
          </div>
        </div>
      </div>
    `).join("");
  },

  filterToCategory(categorySlug) {
    const tab = document.querySelector(`.filter-tab[data-category="${categorySlug}"]`);
    if (tab) {
      document.querySelectorAll(".filter-tab").forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
    }
    this.renderLatestArticles(categorySlug);
    const targetSection = document.getElementById("latestSection");
    if (targetSection) {
      targetSection.scrollIntoView({ behavior: "smooth" });
    }
  },

  /* ------------------------------------------------------------------------
     NEWSLETTER SUBSCRIPTION
  ------------------------------------------------------------------------ */
  initNewsletter() {
    document.querySelectorAll(".topic-chip").forEach(chip => {
      chip.addEventListener("click", () => {
        chip.classList.toggle("selected");
      });
    });

    const form = document.getElementById("newsletterSignupForm");
    if (form) {
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const input = document.getElementById("newsletterEmailInput");
        const email = input?.value.trim();

        if (!email || !email.includes("@")) {
          this.showToast("Please enter a valid email address.");
          return;
        }

        const subscribers = JSON.parse(localStorage.getItem("independence_subscribers") || "[]");
        if (!subscribers.includes(email)) {
          subscribers.push(email);
          localStorage.setItem("independence_subscribers", JSON.stringify(subscribers));
        }

        input.value = "";
        this.showToast("Welcome to Independence Magazine. Confirmation sent.");
      });
    }
  },

  /* ------------------------------------------------------------------------
     GLOBAL TOAST NOTIFICATIONS
  ------------------------------------------------------------------------ */
  showToast(message) {
    let toast = document.getElementById("globalAppToast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "globalAppToast";
      toast.className = "magazine-toast";
      document.body.appendChild(toast);
    }

    toast.innerHTML = `
      <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5"></path>
      </svg>
      <span>${message}</span>
    `;

    toast.classList.add("active");

    if (this._toastTimer) clearTimeout(this._toastTimer);
    this._toastTimer = setTimeout(() => {
      toast.classList.remove("active");
    }, 3500);
  }
};

window.App = App;

// Bootstrap on DOM ready
document.addEventListener("DOMContentLoaded", () => {
  App.init();
});
