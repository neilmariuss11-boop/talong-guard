#!/usr/bin/env python3
"""Pherospora logo builder.

Mark: an onion bulb whose leaves are moth wings, each wing carrying a trail
of three spores toward its tip (pheromone draws the moth in, spores ride out).
Wordmark: "pherospora" set in Manrope and converted to outlines, so the SVG
files need no fonts installed.

Run:  python3 assets/logo/build_logo.py            # full export
      python3 assets/logo/build_logo.py --mark     # mark-only preview
Deps: pip install cairosvg pillow fonttools
Fonts: assets/logo/fonts/Manrope[wght].ttf (SIL OFL, see OFL-Manrope.txt)
"""
from pathlib import Path
import io
import sys

OUT = Path(__file__).parent
FONT = OUT / "fonts" / "Manrope[wght].ttf"

# ------------------------------------------------------------------ palette
PAL = {
    "green": "#1E5A3C",     # wing dark half, wordmark
    "green_lt": "#3E8C5C",  # wing lit half
    "violet": "#6B2150",    # bulb shadow side
    "violet_lt": "#943468", # bulb lit side
    "cream": "#F6F3EC",
    "ink": "#15201A",
}

# ------------------------------------------------------------------ mark geometry (512 grid, mirror at x = 256)
BULB = ("M 256 240 C 264 272, 344 278, 344 346 "
        "C 344 398, 304 430, 256 430 "
        "C 208 430, 168 398, 168 346 "
        "C 168 278, 248 272, 256 240 Z")
# lit side: a crescent on the right
BULB_LIT = ("M 256 240 C 264 272, 344 278, 344 346 "
            "C 344 398, 304 430, 256 430 "
            "C 318 406, 330 294, 256 240 Z")
ROOTS = "M 240 430 Q 236 444, 228 454 M 256 431 L 256 460 M 272 430 Q 276 444, 284 454"

# left wing: base at the thorax, apex up-left, broad rounded trailing edge
WING = ("M 247 214 C 226 166, 156 98, 86 96 "
        "C 86 160, 140 250, 247 242 Z")
WING_UP = ("M 247 214 C 226 166, 156 98, 86 96 "
           "C 128 132, 192 188, 247 230 Z")
WING_LOW = ("M 86 96 C 86 160, 140 250, 247 242 "
            "L 247 230 C 192 188, 128 132, 86 96 Z")
SPORES = ((186, 218, 10), (148, 192, 7.5), (116, 160, 5))   # along the dark lower half

THORAX = '<rect x="245" y="204" width="22" height="46" rx="9"/>'
HEAD = (256, 195, 11)
ANTENNA = "M 252 186 C 246 166, 236 150, 222 138"

MIRROR = 'transform="translate(512 0) scale(-1 1)"'


def both(inner):
    return f"{inner}<g {MIRROR}>{inner}</g>"


# ------------------------------------------------------------------ colour helpers
def _rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(v))) for v in rgb)


def mix(a, b, t):
    """Blend colour a toward colour b by t (0..1)."""
    ra, rb = _rgb(a), _rgb(b)
    return _hex(tuple(x + (y - x) * t for x, y in zip(ra, rb)))


def lighten(h, t):
    return mix(h, "#FFFFFF", t)


def darken(h, t):
    return mix(h, "#000000", t)


def mark(c, bg, depth=True):
    """c: colours for wing_dark, wing_lt, bulb_dark, bulb_lt, spore, head.

    depth=True adds restrained tonal gradients, a faint cast shadow where the
    wings meet the bulb, and a soft highlight on the bulb. depth=False is the
    flat version for one-colour print and stencils.
    """
    if depth:
        # wings: a touch lighter at the base, darker toward the apex
        defs = (
            "<defs>"
            '<linearGradient id="gWd" x1="1" y1="1" x2="0" y2="0">'
            f'<stop offset="0" stop-color="{lighten(c["wing_dark"], 0.06)}"/>'
            f'<stop offset="1" stop-color="{darken(c["wing_dark"], 0.14)}"/></linearGradient>'
            '<linearGradient id="gWl" x1="1" y1="1" x2="0" y2="0">'
            f'<stop offset="0" stop-color="{lighten(c["wing_lt"], 0.08)}"/>'
            f'<stop offset="1" stop-color="{darken(c["wing_lt"], 0.10)}"/></linearGradient>'
            # bulb: lit from the upper right, darker at the lower left
            '<radialGradient id="gB" cx="0.62" cy="0.30" r="0.85">'
            f'<stop offset="0" stop-color="{lighten(c["bulb_dark"], 0.10)}"/>'
            f'<stop offset="0.55" stop-color="{c["bulb_dark"]}"/>'
            f'<stop offset="1" stop-color="{darken(c["bulb_dark"], 0.18)}"/></radialGradient>'
            '<linearGradient id="gBl" x1="0" y1="0" x2="0.4" y2="1">'
            f'<stop offset="0" stop-color="{lighten(c["bulb_lt"], 0.14)}"/>'
            f'<stop offset="1" stop-color="{c["bulb_lt"]}"/></linearGradient>'
            # cast shadow of the wings onto the top of the bulb
            '<radialGradient id="gS" cx="0.5" cy="0" r="0.6">'
            '<stop offset="0" stop-color="#000" stop-opacity="0.22"/>'
            '<stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'
            # soft highlight on the bulb shoulder
            '<radialGradient id="gH" cx="0.68" cy="0.28" r="0.35">'
            '<stop offset="0" stop-color="#FFF" stop-opacity="0.16"/>'
            '<stop offset="1" stop-color="#FFF" stop-opacity="0"/></radialGradient>'
            '<clipPath id="cB"><path d="' + BULB + '"/></clipPath>'
            "</defs>"
        )
        wing_dark, wing_lt = "url(#gWd)", "url(#gWl)"
        bulb_dark, bulb_lt = "url(#gB)", "url(#gBl)"
        extras = (f'<g clip-path="url(#cB)">'
                  f'<rect x="150" y="236" width="212" height="120" fill="url(#gS)"/>'
                  f'<path d="{BULB}" fill="url(#gH)"/></g>')
        head_fill = f'{darken(c["head"], 0.04)}'
    else:
        defs, extras = "", ""
        wing_dark, wing_lt = c["wing_dark"], c["wing_lt"]
        bulb_dark, bulb_lt = c["bulb_dark"], c["bulb_lt"]
        head_fill = c["head"]

    # wings first, with a soft self-stroke so the apex is rounded
    wing = (f'<path d="{WING}" fill="{wing_dark}" stroke="{c["wing_dark"]}" '
            'stroke-width="5" stroke-linejoin="round"/>'
            f'<path d="{WING_UP}" fill="{wing_lt}"/>'
            f'<path d="{WING_LOW}" fill="{wing_dark}"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c["spore"]}"/>'
                      for x, y, r in SPORES)
            + f'<path d="{ANTENNA}" stroke="{c["head"]}" stroke-width="4.5" '
              'stroke-linecap="round" fill="none"/>')
    thorax = THORAX.replace("<rect", f'<rect fill="{head_fill}"')
    # bulb in front, separated from the wings by a background-coloured stroke
    bulb = (f'<path d="{ROOTS}" stroke="{c["bulb_dark"]}" stroke-width="6" '
            'stroke-linecap="round" fill="none"/>'
            f'<path d="{BULB}" fill="none" stroke="{bg}" stroke-width="10" '
            'stroke-linejoin="round"/>'
            f'<path d="{BULB}" fill="{bulb_dark}"/>'
            f'<path d="{BULB_LIT}" fill="{bulb_lt}"/>')
    hx, hy, hr = HEAD
    head = f'<circle cx="{hx}" cy="{hy}" r="{hr}" fill="{head_fill}"/>'
    return defs + both(wing) + thorax + bulb + extras + head


COLOR = dict(wing_dark=PAL["green"], wing_lt=PAL["green_lt"], bulb_dark=PAL["violet"],
             bulb_lt=PAL["violet_lt"], spore=PAL["cream"], head=PAL["green"])
MONO = dict(wing_dark=PAL["ink"], wing_lt=PAL["ink"], bulb_dark=PAL["ink"],
            bulb_lt=PAL["ink"], spore=PAL["cream"], head=PAL["ink"])
REVERSED = dict(wing_dark=PAL["cream"], wing_lt="#CFE0D3", bulb_dark="#E4CBD8",
                bulb_lt=PAL["cream"], spore=PAL["green"], head=PAL["cream"])

# mark bounding box on the 512 grid (for lockups)
MARK_BOX = (78, 88, 434, 462)   # x0, y0, x1, y1


# ------------------------------------------------------------------ wordmark outlines
def wordmark_paths(text, weight=700, tracking=-0.01):
    """Return (list of (path_d, x_offset), total_width, ascent, descent) in font units
    scaled so cap height == 100."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib.instancer import instantiateVariableFont
    from fontTools.pens.svgPathPen import SVGPathPen

    f = instantiateVariableFont(TTFont(FONT), {"wght": weight})
    upem = f["head"].unitsPerEm
    cap = f["OS/2"].sCapHeight or upem * 0.7
    xh = f["OS/2"].sxHeight
    scale = 100 / cap
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    hmtx = f["hmtx"]
    # kerning from GPOS pair adjustment if simple
    kern = {}
    try:
        from fontTools.ttLib.tables import otTables  # noqa
        gpos = f["GPOS"].table
        for lookup in gpos.LookupList.Lookup:
            for st in lookup.SubTable:
                if st.LookupType != 2:
                    continue
                if st.Format == 1:
                    for i, ps in enumerate(st.PairSet):
                        first = st.Coverage.glyphs[i]
                        for pvr in ps.PairValueRecord:
                            v = pvr.Value1.XAdvance if pvr.Value1 else 0
                            if v:
                                kern[(first, pvr.SecondGlyph)] = v
                elif st.Format == 2:
                    cd1, cd2 = st.ClassDef1.classDefs, st.ClassDef2.classDefs
                    for g1 in st.Coverage.glyphs:
                        c1 = cd1.get(g1, 0)
                        for g2, c2 in cd2.items():
                            rec = st.Class1Record[c1].Class2Record[c2]
                            v = rec.Value1.XAdvance if rec.Value1 else 0
                            if v:
                                kern.setdefault((g1, g2), v)
    except Exception:
        pass

    glyphs = [cmap[ord(ch)] for ch in text]
    paths, x = [], 0.0
    for i, g in enumerate(glyphs):
        pen = SVGPathPen(gs)
        gs[g].draw(pen)
        paths.append((pen.getCommands(), x))
        adv = hmtx[g][0]
        if i + 1 < len(glyphs):
            adv += kern.get((g, glyphs[i + 1]), 0)
        x += adv + tracking * upem
    return paths, x * scale, scale, xh * scale


def wordmark_svg(text, colour, weight=700, tracking=-0.01):
    paths, width, scale, xh = wordmark_paths(text, weight, tracking)
    # font y is up; flip. cap height = 100 units, baseline at y = 0
    inner = "".join(
        f'<path transform="translate({x * scale:.2f} 0) scale({scale:.5f} {-scale:.5f})" '
        f'd="{d}" fill="{colour}"/>' for d, x in paths)
    return inner, width, xh


# ------------------------------------------------------------------ lockups
def svg_doc(w, h, body, bg=None, title="Pherospora"):
    rect = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}">'
            f'<title>{title}</title>{rect}{body}</svg>\n')


def mark_doc(c, bg, size=512, pad=0, depth=True):
    x0, y0, x1, y1 = MARK_BOX
    mw, mh = x1 - x0, y1 - y0
    s = (size - 2 * pad) / max(mw, mh)
    tx = pad + (size - 2 * pad - mw * s) / 2 - x0 * s
    ty = pad + (size - 2 * pad - mh * s) / 2 - y0 * s
    body = f'<g transform="translate({tx:.2f} {ty:.2f}) scale({s:.5f})">{mark(c, bg, depth)}</g>'
    return svg_doc(size, size, body, bg)


def horizontal_doc(c, text_col, bg, depth=True):
    """Mark at left, wordmark at right, x-height aligned to the bulb centre."""
    inner, ww, xh = wordmark_svg("pherospora", text_col)
    cap = 100
    mark_h = 300                          # mark height in output units
    x0, y0, x1, y1 = MARK_BOX
    s = mark_h / (y1 - y0)
    mw = (x1 - x0) * s
    gap = 54
    pad = 48
    W = pad + mw + gap + ww + pad
    H = mark_h + 2 * pad
    # wordmark baseline: centre the x-height band on the mark's vertical centre
    baseline = pad + mark_h / 2 + xh / 2 + 6
    body = (f'<g transform="translate({pad - x0 * s:.2f} {pad - y0 * s:.2f}) scale({s:.5f})">{mark(c, bg, depth)}</g>'
            f'<g transform="translate({pad + mw + gap:.2f} {baseline:.2f})">{inner}</g>')
    return svg_doc(round(W), round(H), body, bg)


def stacked_doc(c, text_col, bg, depth=True):
    inner, ww, xh = wordmark_svg("pherospora", text_col)
    x0, y0, x1, y1 = MARK_BOX
    mark_h = 330
    s = mark_h / (y1 - y0)
    mw = (x1 - x0) * s
    pad = 56
    gap = 44
    W = max(mw, ww) + 2 * pad
    H = pad + mark_h + gap + 100 + 28 + pad   # 28 for descender of p
    body = (f'<g transform="translate({(W - mw) / 2 - x0 * s:.2f} {pad - y0 * s:.2f}) scale({s:.5f})">{mark(c, bg, depth)}</g>'
            f'<g transform="translate({(W - ww) / 2:.2f} {pad + mark_h + gap + 100:.2f})">{inner}</g>')
    return svg_doc(round(W), round(H), body, bg)


def badge_doc(size=512):
    g, cream = PAL["green"], PAL["cream"]
    body = (f'<circle cx="{size/2}" cy="{size/2}" r="{size/2}" fill="{g}"/>'
            f'<g transform="translate({size*0.14:.1f} {size*0.14:.1f}) scale({size*0.72/512:.5f})">'
            f'{mark_doc(REVERSED, g, 512)[mark_doc(REVERSED, g, 512).find("<g"):-7]}</g>')
    return svg_doc(size, size, body)


def variants():
    g, cream, ink = PAL["green"], PAL["cream"], PAL["ink"]
    return {
        "pherospora-mark": (mark_doc(COLOR, cream, pad=24), cream),
        "pherospora-mark-flat": (mark_doc(COLOR, cream, pad=24, depth=False), cream),
        "pherospora-mark-mono": (mark_doc(MONO, cream, pad=24, depth=False), cream),
        "pherospora-mark-reversed": (mark_doc(REVERSED, g, pad=24), g),
        "pherospora-badge": (badge_doc(), cream),
        "pherospora-horizontal": (horizontal_doc(COLOR, g, cream), cream),
        "pherospora-horizontal-flat": (horizontal_doc(COLOR, g, cream, depth=False), cream),
        "pherospora-horizontal-mono": (horizontal_doc(MONO, ink, cream, depth=False), cream),
        "pherospora-horizontal-reversed": (horizontal_doc(REVERSED, cream, g), g),
        "pherospora-stacked": (stacked_doc(COLOR, g, cream), cream),
        "pherospora-stacked-reversed": (stacked_doc(REVERSED, cream, g), g),
    }


# ------------------------------------------------------------------ export
class _Chrome:
    """Rasterise SVG through headless Chromium (exact gradient/clip support).
    Falls back to cairosvg if Playwright or the browser is unavailable."""
    _pw = _browser = _page = None

    @classmethod
    def render(cls, svg_text, width):
        from PIL import Image
        import re
        if cls._page is None and cls._browser is not False:
            try:
                import os
                from playwright.sync_api import sync_playwright
                os.environ.setdefault("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
                cls._pw = sync_playwright().start()
                exe = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
                kw = {"args": ["--no-sandbox"]}
                if Path(exe).exists():
                    kw["executable_path"] = exe
                cls._browser = cls._pw.chromium.launch(**kw)
                cls._page = cls._browser.new_page(device_scale_factor=1)
            except Exception as e:  # pragma: no cover
                print("Chromium unavailable, using cairosvg:", e)
                cls._browser = False
        if cls._page is None:
            import cairosvg
            return Image.open(io.BytesIO(cairosvg.svg2png(
                bytestring=svg_text.encode(), output_width=width))).convert("RGBA")
        m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg_text)
        vw, vh = int(m.group(1)), int(m.group(2))
        height = round(width * vh / vw)
        s = re.sub(r'width="\d+" height="\d+"', f'width="{width}" height="{height}"', svg_text, count=1)
        cls._page.set_viewport_size({"width": width, "height": height})
        cls._page.set_content("<body style='margin:0;background:transparent'>" + s + "</body>")
        data = cls._page.screenshot(omit_background=True, clip={"x": 0, "y": 0, "width": width, "height": height})
        return Image.open(io.BytesIO(data)).convert("RGBA")

    @classmethod
    def close(cls):
        try:
            if cls._browser:
                cls._browser.close()
            if cls._pw:
                cls._pw.stop()
        except Exception:
            pass


def png(svg_text, width):
    return _Chrome.render(svg_text, width)


def export(mark_only=False):
    from PIL import Image
    import cairosvg

    if mark_only:
        s = mark_doc(COLOR, PAL["cream"], pad=24)
        png(s, 640).save(OUT / "_mark-preview.png")
        _Chrome.close()
        print("wrote _mark-preview.png")
        return

    for old in OUT.glob("symbol-*"):
        old.unlink()
    for old in OUT.glob("_mark-preview.png"):
        old.unlink()

    v = variants()
    for name, (s, bg) in v.items():
        (OUT / f"{name}.svg").write_text(s)
        for w in (2048, 1024, 256):
            png(s, w).save(OUT / f"{name}-{w}.png")

    fav = png(v["pherospora-badge"][0], 256)
    fav.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

    # preview sheet
    order = ["pherospora-horizontal", "pherospora-horizontal-reversed", "pherospora-stacked",
             "pherospora-mark", "pherospora-mark-mono", "pherospora-badge"]
    tiles = []
    for n in order:
        s, bg = v[n]
        im = png(s, 900 if "horizontal" in n else 420)
        tile = Image.new("RGB", (im.width + 40, im.height + 40), bg)
        tile.paste(im, (20, 20), im)
        tiles.append(tile)
    gap = 28
    row1 = tiles[:2]
    row2 = tiles[2:]
    W = max(sum(t.width for t in row1) + gap * 3, sum(t.width for t in row2) + gap * 5)
    H = gap + max(t.height for t in row1) + gap + max(t.height for t in row2) + gap + 120
    sheet = Image.new("RGB", (W, H), "#DAD5CA")
    x = gap
    for t in row1:
        sheet.paste(t, (x, gap)); x += t.width + gap
    y2 = gap + max(t.height for t in row1) + gap
    x = gap
    for t in row2:
        sheet.paste(t, (x, y2)); x += t.width + gap
    # small-size checks
    y3 = y2 + max(t.height for t in row2) + gap
    x = gap
    for n, size in (("pherospora-mark", 64), ("pherospora-mark", 32), ("pherospora-mark", 16),
                    ("pherospora-badge", 64), ("pherospora-badge", 32), ("pherospora-badge", 16),
                    ("pherospora-horizontal", 240), ("pherospora-horizontal", 120)):
        im = png(v[n][0], size)
        bgc = v[n][1]
        t = Image.new("RGB", (im.width, im.height), bgc)
        t.paste(im, (0, 0), im)
        sheet.paste(t, (x, y3 + (80 - im.height) // 2)); x += im.width + 24
    sheet.save(OUT / "logo-preview.png")
    _Chrome.close()
    print("exported:", ", ".join(v))


if __name__ == "__main__":
    export(mark_only="--mark" in sys.argv)
