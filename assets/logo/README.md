# Logo symbol (draft)

Symbol only. The brand name is on hold, so there is no wordmark yet.

**Concept.** An onion bulb whose leaves are the wings of a harabas moth
(*Spodoptera exigua*), so the mark reads as both the crop and the pest. The spot on
each wing is the moth's real orbicular spot. It also stands for the *Metarhizium*
spores the moth carries away from the Station to its own kind.

**Depth without effects.** Each wing is split along its midrib into a dark and a
light half. The bulb has a shadow side, a lit side and cut-out skin lines. A thin
gap separates the wings from the bulb. This keeps the mark printable in flat
colour. A gradient version exists for screens only.

**Build.** `python3 assets/logo/build_logo.py` regenerates every file here.
Requires `pip install cairosvg pillow`. Edit the path constants near the top to
reshape the mark, or `PAL` to recolour it.

| File | Use |
|---|---|
| `symbol-color.svg` | Primary mark on light backgrounds, tonal flat colour |
| `symbol-gradient.svg` | Screen-only version with soft gradients |
| `symbol-mono.svg` | One-colour print, rubber stamp, spray stencil on the hood |
| `symbol-reversed.svg` | On green or dark backgrounds, slides, shirts |
| `symbol-badge.svg` | Round app-style icon, stickers, social avatar, favicon |
| `*-1024.png`, `*-512.png`, `*-128.png` | Raster exports of each variant |
| `favicon.ico` | 16 to 64 px icon from the badge |
| `logo-preview.png` | All variants side by side, with 64, 32 and 16 px checks |

| Colour | Hex | Role |
|---|---|---|
| Field green dark / light | `#1B5236` / `#3C8A5A` | Wings |
| Onion violet dark / light | `#5E1B40` / `#8A2D5C` | Bulb |
| Cream | `#F7F4EC` | Background |
| Ink | `#16241C` | One-colour print |

Status: concept for team review. Before final use, refine the curves by eye in
Inkscape or Illustrator and pair the symbol with a wordmark once the name is chosen.
