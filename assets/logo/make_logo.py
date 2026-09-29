#!/usr/bin/env python3
"""Pixel-art logo generator for the Padala / SporaLure Station venture.

Draws a harabas moth carrying spore dots on a small pixel grid, adds a
bitmap wordmark, and exports PNG (nearest-neighbour upscale) and SVG.

Run:  python3 assets/logo/make_logo.py
Deps: pillow
"""
from pathlib import Path
from PIL import Image, ImageDraw

OUT = Path(__file__).parent

# ---------------------------------------------------------------- palette
PAL = {
    "bg_light": "#FAF3E0",   # cream (paper / basin white)
    "bg_dark":  "#1E1424",   # night sky (moth is nocturnal)
    "wing":     "#7B2D8E",   # onion purple
    "wing_lt":  "#B06AC2",   # lighter purple (hindwing)
    "body":     "#3A2544",   # dark aubergine body
    "outline":  "#2B1B33",   # pixel outline
    "spore":    "#7BC043",   # Metarhizium green
    "spore_lt": "#C6E86B",   # spore highlight
    "eye":      "#F5D547",   # warm yellow
    "text":     "#2B1B33",
    "text_dark":"#FAF3E0",
    "accent":   "#7BC043",
}

# ------------------------------------------------------------ moth sprite
# Left half of a symmetric 32x30 sprite; column 15 touches the mirror axis.
# . transparent  A antenna  H head  E eye  B body  W forewing  L hindwing  S spore
HALF = [
    "................",
    "........A.......",
    ".........A......",
    "..........A.....",
    "...........A....",
    "............A...",
    ".............AHH",
    "..............EH",
    "....WW........HH",
    "..WWWWWWWWWWWWWB",
    ".WWWWWWWWWWWWWWB",
    ".WWWSWWWWWWSWWWB",
    ".WWWWWWWSWWWWWWB",
    ".WWWWWWWWWWWSWWB",
    "..WWSWWWSWWWWWWB",
    "..WWWWWWWWWWSWWB",
    "...WWWWSWWWWWWWB",
    "....WWWWWWWWWWWB",
    "......WWWWLLLLLB",
    ".....LLLLLLLLLLB",
    "....LLLLLSLLLLLB",
    "....LLLLLLLLLLLB",
    ".....LLLSLLLLLLB",
    "......LLLLLLLLLB",
    ".......LLLLLLLBB",
    ".........LLLLLBB",
    "...........LLLBB",
    "...............B",
    "...............B",
    "................",
]
CHAR_COLOR = {
    "A": "body", "H": "body", "E": "eye", "B": "body",
    "W": "wing", "L": "wing_lt", "S": "spore",
}

def moth_grid():
    rows = [r + r[::-1] for r in HALF]
    grid = [[CHAR_COLOR.get(c) for c in row] for row in rows]
    h, w = len(grid), len(grid[0])
    # 1-px outline: wing pixels that touch transparency become outline colour
    out = [row[:] for row in grid]
    for y in range(h):
        for x in range(w):
            if grid[y][x] in ("wing", "wing_lt"):
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = y+dy, x+dx
                    if not (0 <= ny < h and 0 <= nx < w) or grid[ny][nx] is None:
                        out[y][x] = "outline"; break
    # spore highlight: one lighter pixel top-left of each spore cluster
    return out

# ------------------------------------------------------------- bitmap font (5x7)
FONT = {
"A":["01110","10001","10001","11111","10001","10001","10001"],
"D":["11110","10001","10001","10001","10001","10001","11110"],
"E":["11111","10000","10000","11110","10000","10000","11111"],
"I":["11111","00100","00100","00100","00100","00100","11111"],
"L":["10000","10000","10000","10000","10000","10000","11111"],
"N":["10001","11001","10101","10011","10001","10001","10001"],
"O":["01110","10001","10001","10001","10001","10001","01110"],
"P":["11110","10001","10001","11110","10000","10000","10000"],
"R":["11110","10001","10001","11110","10100","10010","10001"],
"S":["01111","10000","10000","01110","00001","00001","11110"],
"T":["11111","00100","00100","00100","00100","00100","00100"],
"U":["10001","10001","10001","10001","10001","10001","01110"],
" ":["00000"]*7,
}

def text_grid(s, color):
    cols = []
    for i, ch in enumerate(s.upper()):
        g = FONT[ch]
        for x in range(5):
            cols.append([color if g[y][x]=="1" else None for y in range(7)])
        if i < len(s)-1:
            cols.append([None]*7)
    return [[cols[x][y] for x in range(len(cols))] for y in range(7)]

# ------------------------------------------------------------- compositing
def blank(w, h):
    return [[None]*w for _ in range(h)]

def paste(dst, src, ox, oy):
    for y, row in enumerate(src):
        for x, c in enumerate(row):
            if c is not None:
                dst[oy+y][ox+x] = c

def render_png(grid, path, px, bg=None):
    h, w = len(grid), len(grid[0])
    img = Image.new("RGBA", (w, h), PAL[bg] if bg else (0,0,0,0))
    d = ImageDraw.Draw(img)
    for y in range(h):
        for x in range(w):
            if grid[y][x]:
                d.point((x, y), PAL[grid[y][x]])
    img = img.resize((w*px, h*px), Image.NEAREST)
    img.save(path)

def render_svg(grid, path, bg=None):
    h, w = len(grid), len(grid[0])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
             f'shape-rendering="crispEdges" width="{w*16}" height="{h*16}">']
    if bg:
        parts.append(f'<rect width="{w}" height="{h}" fill="{PAL[bg]}"/>')
    # merge horizontal runs of same colour to keep the file small
    for y in range(h):
        x = 0
        while x < w:
            c = grid[y][x]
            if c is None: x += 1; continue
            x0 = x
            while x < w and grid[y][x] == c: x += 1
            parts.append(f'<rect x="{x0}" y="{y}" width="{x-x0}" height="1" fill="{PAL[c]}"/>')
    parts.append("</svg>")
    path.write_text("\n".join(parts))

# ------------------------------------------------------------- layouts
def icon(pad=2):
    m = moth_grid()
    g = blank(len(m[0])+2*pad, len(m)+2*pad)
    paste(g, m, pad, pad)
    return g

def stacked(dark=False):
    tcol = "text_dark" if dark else "text"
    m = moth_grid()
    word = text_grid("PADALA", tcol)
    tag  = text_grid("SPORALURE STATION", "accent")
    W = max(len(m[0]), len(word[0]), len(tag[0])) + 8
    H = len(m) + 2 + 7*2 + 4 + 7 + 6
    g = blank(W, H)
    y = 3
    paste(g, m, (W-len(m[0]))//2, y); y += len(m) + 1
    # wordmark at 2x scale
    big = [[c for c in row for _ in (0,1)] for row in word for _ in (0,1)]
    paste(g, big, (W-len(big[0]))//2, y); y += 14 + 3
    paste(g, tag, (W-len(tag[0]))//2, y)
    return g

def horizontal(dark=False):
    tcol = "text_dark" if dark else "text"
    m = moth_grid()
    word = text_grid("PADALA", tcol)
    big = [[c for c in row for _ in (0,1)] for row in word for _ in (0,1)]
    tag  = text_grid("SPORALURE STATION", "accent")
    textw = max(len(big[0]), len(tag[0]))
    W = 3 + len(m[0]) + 3 + textw + 4
    H = len(m) + 4
    g = blank(W, H)
    paste(g, m, 3, 2)
    tx = 3 + len(m[0]) + 3
    ty = (H - (14 + 3 + 7)) // 2
    paste(g, big, tx, ty)
    paste(g, tag, tx, ty + 14 + 3)
    return g

def sheet():
    """Preview sheet: all variants on one image."""
    tiles = [
        (icon(), "bg_light", 10), (icon(), "bg_dark", 10),
        (stacked(), "bg_light", 6), (stacked(True), "bg_dark", 6),
        (horizontal(), "bg_light", 6), (horizontal(True), "bg_dark", 6),
    ]
    imgs = []
    for g, bg, px in tiles:
        p = OUT / "_tmp.png"; render_png(g, p, px, bg); imgs.append(Image.open(p).convert("RGBA"))
    (OUT / "_tmp.png").unlink()
    gap = 24
    W = max(i.width for i in imgs[0:2]) * 2 + gap*3
    W = max(W, imgs[2].width*2 + gap*3, imgs[4].width*2 + gap*3)
    rows = [imgs[0:2], imgs[2:4], imgs[4:6]]
    H = sum(max(i.height for i in r) for r in rows) + gap*4
    sheet = Image.new("RGBA", (W, H), "#D9D2C5")
    y = gap
    for r in rows:
        x = gap
        for im in r:
            sheet.paste(im, (x, y)); x += im.width + gap
        y += max(i.height for i in r) + gap
    sheet.save(OUT / "padala-logo-sheet.png")

if __name__ == "__main__":
    render_png(icon(), OUT/"padala-icon.png", 16)                    # 576 px, transparent
    render_png(icon(), OUT/"padala-icon-dark.png", 16, "bg_dark")
    render_svg(icon(), OUT/"padala-icon.svg")
    render_png(stacked(), OUT/"padala-logo-stacked.png", 8, "bg_light")
    render_png(stacked(True), OUT/"padala-logo-stacked-dark.png", 8, "bg_dark")
    render_svg(stacked(), OUT/"padala-logo-stacked.svg")
    render_png(horizontal(), OUT/"padala-logo-horizontal.png", 8, "bg_light")
    render_png(horizontal(True), OUT/"padala-logo-horizontal-dark.png", 8, "bg_dark")
    render_svg(horizontal(), OUT/"padala-logo-horizontal.svg")
    sheet()
    print("done:", sorted(p.name for p in OUT.glob("padala-*")))
