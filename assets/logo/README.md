# Pherospora logo

Brand: **Pherospora** (pheromone + spore). Web screen on 2026-09-29 found no company,
product or mark using the word. IPOPHL and WIPO database searches are still to do
(classes 5 and 21) before anything is printed.

**Mark.** An onion bulb whose leaves are moth wings. The pheromone draws the moth
in, and each wing carries a trail of three spores toward its tip, the spores riding
out. Reads as crop and pest at once. Two-tone wings and a lit crescent on the bulb
give depth without gradients, so it prints in flat colour.

**Wordmark.** "pherospora" in Manrope Bold, converted to outlines, so the SVG files
need no font installed. Manrope is SIL Open Font Licence (`fonts/OFL-Manrope.txt`).

**Build.** `python3 assets/logo/build_logo.py` regenerates everything.
Requires `pip install cairosvg pillow fonttools`. `--mark` renders a quick mark-only
preview. Geometry constants are at the top of the script.

| File | Use |
|---|---|
| `pherospora-horizontal.svg` | Primary lockup. Documents, banners, slide footers |
| `pherospora-horizontal-reversed.svg` | Same on field green |
| `pherospora-horizontal-mono.svg` | One-colour print, forms, fax-quality copies |
| `pherospora-stacked.svg`, `-reversed` | Square placements, title slides, posters |
| `pherospora-mark.svg`, `-mono`, `-reversed` | Symbol alone. Stencil on the hood, stickers, app icon |
| `pherospora-badge.svg` | Round icon on green. Social avatar, favicon |
| `*-2048.png`, `*-1024.png`, `*-256.png` | Raster exports of every variant |
| `favicon.ico` | 16 to 64 px |
| `logo-preview.png` | All variants on one sheet with 16, 32 and 64 px checks |

| Colour | Hex | Role |
|---|---|---|
| Field green | `#1E5A3C` | Wing shadow, wordmark, reversed background |
| Leaf green | `#3E8C5C` | Wing lit half |
| Onion violet | `#6B2150` | Bulb shadow |
| Onion violet light | `#943468` | Bulb lit crescent |
| Cream | `#F6F3EC` | Background, spores |
| Ink | `#15201A` | One-colour print |

Rules of use: keep clear space around the lockup equal to the bulb's width; do not
place the colour mark on photographs without the cream or green panel; the mark
alone is fine down to 32 px, the badge down to 16 px, the horizontal lockup down to
about 120 px wide.
