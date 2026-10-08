/**
 * Independence Magazine - Real-time Search & Category Filtering
 * Designed by DigitalRank.io
 */

const SearchFilter = {
  activeCategory: "all",

  init() {
    this.searchModal = document.getElementById("searchModal");
    this.searchInput = document.getElementById("searchInputField");
    this.searchResults = document.getElementById("searchResultsContainer");

    // Open/Close triggers
    document.querySelectorAll(".open-search-trigger").forEach(btn => {
      btn.addEventListener("click", () => this.openSearch());
    });

    document.querySelectorAll(".close-search-trigger").forEach(btn => {
      btn.addEventListener("click", () => this.closeSearch());
    });

    // Close on backdrop click
    if (this.searchModal) {
      this.searchModal.addEventListener("click", (e) => {
        if (e.target === this.searchModal) this.closeSearch();
      });
    }

    // Input search typing
    if (this.searchInput) {
      this.searchInput.addEventListener("input", (e) => this.handleSearchInput(e.target.value));
    }

    // Keyboard shortcuts (Cmd+K, Ctrl+K, or slash key)
    document.addEventListener("keydown", (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === "k") {
        e.preventDefault();
        this.openSearch();
      }
      if (e.key === "/" && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
        e.preventDefault();
        this.openSearch();
      }
      if (e.key === "Escape" && this.isSearchOpen()) {
        this.closeSearch();
      }
    });

    // Init Category Tabs
    this.setupCategoryTabs();
  },

  isSearchOpen() {
    return this.searchModal && this.searchModal.classList.contains("active");
  },

  openSearch() {
    if (!this.searchModal) return;
    this.searchModal.classList.add("active");
    if (this.searchInput) {
      this.searchInput.value = "";
      setTimeout(() => this.searchInput.focus(), 50);
      this.renderRecentSearches();
    }
    document.body.style.overflow = "hidden";
  },

  closeSearch() {
    if (!this.searchModal) return;
    this.searchModal.classList.remove("active");
    document.body.style.overflow = "";
  },

  handleSearchInput(query) {
    const trimmed = query.trim().toLowerCase();
    if (!trimmed) {
      this.renderRecentSearches();
      return;
    }

    const matches = window.ARTICLES_DATA.filter(item => {
      return (
        item.title.toLowerCase().includes(trimmed) ||
        item.excerpt.toLowerCase().includes(trimmed) ||
        item.category.toLowerCase().includes(trimmed) ||
        item.author.name.toLowerCase().includes(trimmed) ||
        item.tags.some(t => t.toLowerCase().includes(trimmed))
      );
    });

    this.renderSearchResults(matches, trimmed);
  },

  renderRecentSearches() {
    if (!this.searchResults) return;
    const popular = window.ARTICLES_DATA.slice(0, 4);

    this.searchResults.innerHTML = `
      <div style="padding: 10px 14px 6px 14px; font-size: 0.74rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em;">
        Trending Editorial Inquiries
      </div>
      ${popular.map(item => `
        <div class="search-result-item" onclick="SearchFilter.selectArticle('${item.id}')">
          <div style="width: 54px; height: 42px; border-radius: 4px; overflow: hidden; flex-shrink: 0;">
            <img src="${item.coverImage}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="flex-grow: 1; overflow: hidden;">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase;">${item.category}</span>
            <div style="font-family: var(--font-serif); font-size: 0.95rem; font-weight: 700; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              ${item.title}
            </div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">${item.readTime} • by ${item.author.name}</div>
          </div>
        </div>
      `).join("")}
    `;
  },

  renderSearchResults(results, query) {
    if (!this.searchResults) return;

    if (results.length === 0) {
      this.searchResults.innerHTML = `
        <div style="text-align: center; padding: 48px 16px; color: var(--text-muted);">
          <svg width="40" height="40" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" style="margin: 0 auto 12px auto; opacity: 0.5;">
            <path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"></path>
          </svg>
          <div style="font-weight: 600; font-size: 1rem; color: var(--text-primary);">No investigative pieces found</div>
          <div style="font-size: 0.84rem; margin-top: 4px;">No match for "${query}". Try searching "compute", "epigenetics", or "markets".</div>
        </div>
      `;
      return;
    }

    this.searchResults.innerHTML = `
      <div style="padding: 10px 14px 6px 14px; font-size: 0.74rem; font-weight: 700; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em;">
        ${results.length} Stories Matching "${query}"
      </div>
      ${results.map(item => `
        <div class="search-result-item" onclick="SearchFilter.selectArticle('${item.id}')">
          <div style="width: 58px; height: 46px; border-radius: 4px; overflow: hidden; flex-shrink: 0;">
            <img src="${item.coverImage}" alt="${item.title}" style="width: 100%; height: 100%; object-fit: cover;">
          </div>
          <div style="flex-grow: 1; overflow: hidden;">
            <span style="font-size: 0.68rem; font-weight: 700; color: var(--accent-gold); text-transform: uppercase;">${item.category}</span>
            <div style="font-family: var(--font-serif); font-size: 0.95rem; font-weight: 700; color: var(--text-primary); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">
              ${item.title}
            </div>
            <div style="font-size: 0.74rem; color: var(--text-muted);">${item.readTime} • ${item.publishedAt}</div>
          </div>
        </div>
      `).join("")}
    `;
  },

  selectArticle(id) {
    this.closeSearch();
    if (window.ReaderModal) {
      window.ReaderModal.open(id);
    }
  },

  setupCategoryTabs() {
    const tabsContainer = document.getElementById("categoryFilterTabs");
    if (!tabsContainer) return;

    tabsContainer.querySelectorAll(".filter-tab").forEach(tab => {
      tab.addEventListener("click", () => {
        tabsContainer.querySelectorAll(".filter-tab").forEach(t => t.classList.remove("active"));
        tab.classList.add("active");
        const categorySlug = tab.getAttribute("data-category");
        this.filterGridByCategory(categorySlug);
      });
    });
  },

  filterGridByCategory(categorySlug) {
    this.activeCategory = categorySlug;
    if (window.App) {
      window.App.renderLatestArticles(categorySlug);
    }
  }
};

window.SearchFilter = SearchFilter;
