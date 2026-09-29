# Device renders (Blender)

`station_render.py` builds the Station in Blender from the dimensions in
`phase5-device-design.md` §3 and renders three views:

| Output | View |
|---|---|
| `station-hero.png` | 3/4 product shot on soil |
| `station-section.png` | Front half cut away: lure cage, cross vanes, 80 mm window, 50 mm sun collar, 150 mm velvet sleeve |
| `station-field.png` | Four Stations in an onion plot at 25 cm row spacing |
| `station.blend` | Editable scene |

## Run

With a Blender install (4.x):

```
blender -b -P assets/render/station_render.py -- --out assets/render --samples 128
```

With the pip module (needs Python 3.11):

```
python3.11 -m pip install bpy
python3.11 assets/render/station_render.py --out assets/render
```

Add `--quick` for an 800 × 600 preview, or lower `--samples` for speed.

## What is modelled

- Hood: inverted 400 mm PP basin, 100 mm deep, rolled rim.
- Tube: 4-inch PVC, 110 mm OD, 102 mm ID, 200 mm long, white.
- Sun collar: top 50 mm of the tube left bare.
- Spore sleeve: black velvet, 150 mm, seated against three rivets.
- Cross vanes: two 100 × 100 mm coroplast plates, 20 mm into the tube.
- Entry window: 80 mm between hood rim and tube top, set by three Ø 3 mm rods at 120°.
- Lure cage: Ø 35 × 50 mm cup on an M6 hanger, about 90 mm above the vanes.
- Pole: bamboo, 1.2 m, 300 mm buried, two hose clamps. Tube bottom at 600 mm.

Materials are plain Principled BSDF. Edit the constants at the top of the script
to change any dimension.
