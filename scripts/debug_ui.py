# -*- coding: utf-8 -*-
with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

print("searchModal:", 'id="searchModal"' in text)
print("searchInputField:", 'id="searchInputField"' in text)
print("searchResultsContainer:", 'id="searchResultsContainer"' in text)
print("open-search-trigger count:", text.count("open-search-trigger"))
print("close-search-trigger count:", text.count("close-search-trigger"))
print("themeToggleBtn:", 'id="themeToggleBtn"' in text)
print("themeIconSvg:", 'id="themeIconSvg"' in text)
