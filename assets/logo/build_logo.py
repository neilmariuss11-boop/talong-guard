#!/usr/bin/env python3
"""Vector logo symbol for the autodissemination Station (name TBD).

Concept: an onion bulb whose leaves are the wings of a harabas moth
(Spodoptera exigua). Reads as both the crop and the pest. The single spot on
each wing is the moth's orbicular spot and stands for the Metarhizium spores
it carries. No wordmark yet: the brand name is on hold.

Depth comes from tonal layering, not effects:
  * each wing is split along its midrib into a dark and a light half,
  * the bulb is split into a shadow and a lit side with skin lines cut out,
  * a thin knockout gap separates wings from bulb.
A gradient variant exists for screens only; print uses the tonal variant.

Run:  python3 assets/logo/build_logo.py
Deps: pip install cairosvg pillow
"""
from pathlib import Path
import io

OUT = Path(__file__).parent

# ------------------------------------------------------------------ palette
PAL = {
    "g_dark": "#1B5236",   # wing shadow half
    "g_light": "#3C8A5A",  # wing lit half
    "v_dark": "#5E1B40",   # bulb shadow side
    "v_light": "#8A2D5C",  # bulb lit side
    "cream": "#F7F4EC",
    "ink": "#16241C",
}

# ------------------------------------------------------------------ geometry
# 512 x 512 artboard, mirror axis x = 256. Wing paths are the LEFT wing.
BULB = ("M 256 206 C 262 238, 290 256, 318 276 C 346 296, 352 326, 348 350 "
        "C 342 392, 302 420, 256 422 C 210 420, 170 392, 164 350 "
        "C 160 326, 166 296, 194 276 C 222 256, 250 238, 256 206 Z")
BULB_LEFT = ("M 256 206 C 250 238, 222 256, 194 276 C 166 296, 160 326, 164 350 "
             "C 170 392, 210 420, 256 422 Z")
SKIN_L = "M 254 244 C 222 280, 212 360, 242 412"
SKIN_R = "M 258 244 C 290 280, 300 360, 270 412"
ROOTS = "M 244 421 Q 238 436 230 446 M 256 423 L 256 452 M 268 421 Q 274 436 282 446"

WING = ("M 248 232 C 236 190, 170 120, 82 92 C 110 190, 190 250, 250 244 Z")
WING_UPPER = "M 248 232 C 236 190, 170 120, 82 92 C 140 140, 200 196, 248 232 Z"
WING_LOWER = "M 82 92 C 110 190, 190 250, 250 244 L 248 232 C 200 196, 140 140, 82 92 Z"
SPOT = (168, 198, 9)

HEAD = (256, 194, 11)
ANTENNA = "M 250 186 C 244 160, 232 138, 212 118 C 226 128, 244 150, 256 184 Z"

MIRROR = 'transform="translate(512,0) scale(-1,1)"'


def both(inner):
    """Draw inner (left side) and its mirror image."""
    return f"{inner}<g {MIRROR}>{inner}</g>"


def mark(c, bg, gradient=False):
    """c: dict of colours for g_dark, g_light, v_dark, v_light, spot, line."""
    defs = ""
    if gradient:
        defs = (
            "<defs>"
            f'<linearGradient id="gw" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c["g_light"]}"/>'
            f'<stop offset="1" stop-color="{c["g_dark"]}"/></linearGradient>'
            f'<radialGradient id="gb" cx="0.62" cy="0.42" r="0.75">'
            f'<stop offset="0" stop-color="{c["v_light"]}"/>'
            f'<stop offset="1" stop-color="{c["v_dark"]}"/></radialGradient>'
            "</defs>"
        )
        bulb = f'<path d="{BULB}" fill="url(#gb)"/>'
        wing_fill = f'<path d="{WING}" fill="url(#gw)"/>'
    else:
        bulb = (f'<path d="{BULB}" fill="{c["v_light"]}"/>'
                f'<path d="{BULB_LEFT}" fill="{c["v_dark"]}"/>')
        wing_fill = (f'<path d="{WING_LOWER}" fill="{c["g_light"]}"/>'
                     f'<path d="{WING_UPPER}" fill="{c["g_dark"]}"/>')

    skin = (f'<path d="{SKIN_L} M 256 236 L 256 414 {SKIN_R}" stroke="{c["line"]}" '
            'stroke-width="5" stroke-linecap="round" fill="none" opacity="0.9"/>')
    roots = (f'<path d="{ROOTS}" stroke="{c["v_dark"]}" stroke-width="6" '
             'stroke-linecap="round" fill="none"/>')
    gap = f'<path d="{WING}" fill="{bg}" stroke="{bg}" stroke-width="12" stroke-linejoin="round"/>'
    sx, sy, sr = SPOT
    wing = gap + wing_fill + f'<circle cx="{sx}" cy="{sy}" r="{sr}" fill="{c["spot"]}"/>'
    hx, hy, hr = HEAD
    head = (f'<circle cx="{hx}" cy="{hy}" r="{hr}" fill="{c["g_dark"]}"/>'
            + both(f'<path d="{ANTENNA}" fill="{c["g_dark"]}"/>'))
    return defs + roots + bulb + skin + both(wing) + head


COLOR = {"g_dark": PAL["g_dark"], "g_light": PAL["g_light"], "v_dark": PAL["v_dark"],
         "v_light": PAL["v_light"], "spot": PAL["cream"], "line": PAL["cream"]}
MONO = {k: PAL["ink"] for k in ("g_dark", "g_light", "v_dark", "v_light")}
MONO.update(spot=PAL["cream"], line=PAL["cream"])
REV = {"g_dark": PAL["cream"], "g_light": "#DCE9DF", "v_dark": "#E9D3DE",
       "v_light": PAL["cream"], "spot": PAL["g_dark"], "line": PAL["g_dark"]}


def svg(content, bg=None, title="Station logo symbol"):
    rect = f'<rect width="512" height="512" fill="{bg}"/>' if bg else ""
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
            f'width="512" height="512"><title>{title}</title>{rect}'
            f'<g transform="translate(0 -14)">{content}</g></svg>\n')


def variants():
    cream, green = PAL["cream"], PAL["g_dark"]
    badge_inner = mark(REV, green)
    return {
        "symbol-color": (svg(mark(COLOR, cream), cream), cream),
        "symbol-gradient": (svg(mark(COLOR, cream, gradient=True), cream), cream),
        "symbol-mono": (svg(mark(MONO, cream), cream), cream),
        "symbol-reversed": (svg(mark(REV, green), green), green),
        "symbol-badge": (svg(
            f'<circle cx="256" cy="270" r="246" fill="{green}"/>'
            f'<g transform="translate(256 280) scale(.8) translate(-256 -280)">{badge_inner}</g>'),
            cream),
    }


def export():
    import cairosvg
    from PIL import Image

    v = variants()
    for name, (s, _) in v.items():
        (OUT / f"{name}.svg").write_text(s)
        for px in (1024, 512, 128):
            cairosvg.svg2png(bytestring=s.encode(), output_width=px,
                             write_to=str(OUT / f"{name}-{px}.png"))

    fav = Image.open(io.BytesIO(cairosvg.svg2png(
        bytestring=v["symbol-badge"][0].encode(), output_width=256)))
    fav.save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48), (64, 64)])

    t, pad = 320, 24
    names = list(v)
    sheet = Image.new("RGB", (pad + (t + pad) * len(names), t + 2 * pad + 72), "#E4DFD3")
    for i, name in enumerate(names):
        s, bg = v[name]
        x = pad + i * (t + pad)
        for j, size in enumerate((t, 64, 32, 16)):
            tile = Image.new("RGB", (size, size), bg)
            im = Image.open(io.BytesIO(cairosvg.svg2png(
                bytestring=s.encode(), output_width=size))).convert("RGBA")
            tile.paste(im, (0, 0), im)
            if j == 0:
                sheet.paste(tile, (x, pad))
            else:
                sheet.paste(tile, (x + (j - 1) * 80, pad + t + 8))
    sheet.save(OUT / "logo-preview.png")
    print("exported:", ", ".join(names))


if __name__ == "__main__":
    export()
