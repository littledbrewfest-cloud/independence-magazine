for slug in ['andi-rock', 'jason-clarkson', 'elly-castle']:
    with open(f'{slug}/index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    marker = '<div class="reader-prose">'
    pos = html.find(marker)
    print(f"=== {slug} ===")
    print(html[pos+len(marker):pos+len(marker)+350].strip())
    print()
