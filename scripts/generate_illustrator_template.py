# -*- coding: utf-8 -*-
"""
Generate an Adobe Illustrator 2019 compatible vector template (1200x675)
for Independence Magazine featured images.
"""
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "templates")
os.makedirs(TEMPLATE_DIR, exist_ok=True)

svg_path = os.path.join(TEMPLATE_DIR, "featured-image-template-1200x675.svg")

svg_content = """<?xml version="1.0" encoding="utf-8"?>
<!-- Adobe Illustrator 2019 Compatible Vector Template (1200x675) - Independence Magazine -->
<svg version="1.1" id="Independence_Magazine_Cover_Template" 
     xmlns="http://www.w3.org/2000/svg" 
     xmlns:xlink="http://www.w3.org/1999/xlink" 
     x="0px" y="0px" 
     viewBox="0 0 1200 675" 
     width="1200px" height="675px" 
     xml:space="preserve">

<defs>
  <!-- Linear Gradients for Overlays & Badges -->
  <linearGradient id="bottomShadowGradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000000" stop-opacity="0"/>
    <stop offset="60%" stop-color="#000000" stop-opacity="0.3"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0.75"/>
  </linearGradient>

  <linearGradient id="topShadowGradient" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="#000000" stop-opacity="0.6"/>
    <stop offset="100%" stop-color="#000000" stop-opacity="0"/>
  </linearGradient>

  <linearGradient id="crimsonBadgeGradient" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" stop-color="#d90429"/>
    <stop offset="100%" stop-color="#ef233c"/>
  </linearGradient>

  <!-- Photo Clipping Mask (1200x675 exact 16:9 boundary) -->
  <clipPath id="photoClipBoundary">
    <rect x="0" y="0" width="1200" height="675" rx="0" ry="0"/>
  </clipPath>
</defs>

<!-- LAYER 1: BASE BACKGROUND & PHOTO PLACEHOLDER -->
<g id="Layer_1_Photo_Placeholder" clip-path="url(#photoClipBoundary)">
  <!-- Solid Neutral Base -->
  <rect x="0" y="0" width="1200" height="675" fill="#1e293b"/>
  
  <!-- Grid Texture / Placeholder Box for placing your photo in Illustrator -->
  <g opacity="0.35">
    <line x1="0" y1="0" x2="1200" y2="675" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8,8"/>
    <line x1="1200" y1="0" x2="0" y2="675" stroke="#94a3b8" stroke-width="2" stroke-dasharray="8,8"/>
    <rect x="100" y="60" width="1000" height="555" fill="none" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="6,6"/>
  </g>
  
  <!-- Instruction Note in Center (can be deleted or covered by your photo) -->
  <text x="600" y="325" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="28" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="1">
    PLACE YOUR PHOTO HERE IN ILLUSTRATOR
  </text>
  <text x="600" y="365" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="16" fill="#94a3b8" text-anchor="middle">
    File &gt; Place (Shift+Ctrl+P) &bull; Crop to Artboard (1200 x 675 px)
  </text>
</g>

<!-- LAYER 2: CINEMATIC GRADIENT OVERLAYS (Improves Text Contrast) -->
<g id="Layer_2_Gradient_Overlays">
  <!-- Top subtle shadow for masthead branding -->
  <rect x="0" y="0" width="1200" height="140" fill="url(#topShadowGradient)"/>
  <!-- Bottom gradient for clean headline / caption legibility -->
  <rect x="0" y="380" width="1200" height="295" fill="url(#bottomShadowGradient)"/>
</g>

<!-- LAYER 3: BRANDING & EDITORIAL ACCENTS -->
<g id="Layer_3_Branding">
  <!-- Top Left: Magazine Masthead Watermark -->
  <g transform="translate(48, 48)">
    <!-- Small background pill for contrast -->
    <rect x="-12" y="-14" width="220" height="38" rx="4" fill="#000000" opacity="0.45"/>
    <text x="0" y="11" font-family="'Georgia', 'Times New Roman', serif" font-size="21" font-weight="bold" fill="#ffffff" letter-spacing="0.5">
      Independence<tspan fill="#d90429">.</tspan>
    </text>
    <text x="146" y="11" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#cbd5e1" letter-spacing="2">
      MAGAZINE
    </text>
  </g>

  <!-- Top Right: Verified Editorial Stamp -->
  <g transform="translate(1010, 48)">
    <rect x="0" y="-12" width="142" height="28" rx="14" fill="#ffffff" opacity="0.15"/>
    <circle cx="16" cy="2" r="5" fill="#22c55e"/>
    <text x="28" y="6" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#ffffff" letter-spacing="0.5">
      VERIFIED PRESS
    </text>
  </g>
</g>

<!-- LAYER 4: CATEGORY PILL BADGES (Select or Edit as Needed) -->
<g id="Layer_4_Category_Badges" transform="translate(48, 545)">
  <!-- Option A: Biography Badge (Default Visible) -->
  <g id="Badge_Biography">
    <rect x="0" y="0" width="118" height="32" rx="4" fill="url(#crimsonBadgeGradient)"/>
    <text x="59" y="20.5" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1.2">
      BIOGRAPHY
    </text>
  </g>

  <!-- Option B: Technology Badge (Move/Show as needed) -->
  <g id="Badge_Technology" transform="translate(130, 0)">
    <rect x="0" y="0" width="134" height="32" rx="4" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="67" y="20.5" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="12" font-weight="800" fill="#38bdf8" text-anchor="middle" letter-spacing="1.2">
      TECHNOLOGY
    </text>
  </g>

  <!-- Option C: Celebrity Badge (Move/Show as needed) -->
  <g id="Badge_Celebrity" transform="translate(276, 0)">
    <rect x="0" y="0" width="118" height="32" rx="4" fill="#c59b27"/>
    <text x="59" y="20.5" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1.2">
      CELEBRITY
    </text>
  </g>

  <!-- Option D: Lifestyle Badge (Move/Show as needed) -->
  <g id="Badge_Lifestyle" transform="translate(406, 0)">
    <rect x="0" y="0" width="114" height="32" rx="4" fill="#16a34a"/>
    <text x="57" y="20.5" font-family="'Helvetica Neue', Helvetica, Arial, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle" letter-spacing="1.2">
      LIFESTYLE
    </text>
  </g>
</g>

<!-- LAYER 5: EDITORIAL HEADLINE PLACEHOLDER (Optional) -->
<g id="Layer_5_Headline_Text" transform="translate(48, 620)">
  <text x="0" y="0" font-family="'Georgia', 'Times New Roman', serif" font-size="24" font-weight="bold" fill="#ffffff">
    Article Headline or Subject Name Goes Here
  </text>
</g>

<!-- LAYER 6: SAFE AREA GUIDES (Turn Visibility Off Before Export) -->
<g id="Layer_6_Guides_and_Safe_Zone" opacity="0.75" display="none">
  <!-- Outer Safe Margins (48px) -->
  <rect x="48" y="48" width="1104" height="579" fill="none" stroke="#00ffff" stroke-width="1" stroke-dasharray="4,4"/>
  <!-- Rule of Thirds Vertical Lines -->
  <line x1="400" y1="0" x2="400" y2="675" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="800" y1="0" x2="800" y2="675" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3"/>
  <!-- Rule of Thirds Horizontal Lines -->
  <line x1="0" y1="225" x2="1200" y2="225" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3"/>
  <line x1="0" y1="450" x2="1200" y2="450" stroke="#f43f5e" stroke-width="1" stroke-dasharray="3,3"/>
</g>

</svg>
"""

with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

print(f"[SUCCESS] Generated Illustrator 2019 SVG template at:\n{svg_path}")
