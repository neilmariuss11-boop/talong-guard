# Phase 5: Device Design — Autodissemination Station v1
**Rewritten 2026-09-27** (replaces the ESP32/SMS monitoring-trap architecture of the eggplant concept)

> **Why the old design was retired.** The ESP32 + IR counter + SIM800L design automated *monitoring*. The team and panel rejected pure monitoring and automation. The new product *acts* on the pest population. It has no electronics, which also removes the battery, solar and GSM cost and failure points.
>
> Evidence for every design decision: `research-synthesis.md` [R#]. Business context: `proposal.md`.

---

## 1. DESIGN REQUIREMENTS

### 1.1 Functional requirements

| ID | Requirement | Target | Basis |
|---|---|---|---|
| F1 | Attract *S. exigua* males at night | Commercial pheromone lure, 4-week life | [R13, R23] |
| F2 | Make visiting moths contact the spore surface | ≥80% of moths entering the tube carry visible spores (bench test) | [R5, R6] |
| F3 | Let moths leave alive | No funnel, glue or poison; open exit ≥10 cm | Autodissemination principle [R4] |
| F4 | Keep spores viable in the field | ≥70% germination at day 14 | [R5, R6] |
| F5 | Keep lure and spores apart | ≥10 cm (precaution; adjustable) | [R5, R6]; not needed per [R4, R7] |
| F6 | Block direct sunlight from the spore surface | No direct beam on velvet at sun elevation ≥ 30° | UV-B LT50 ≈ 4.4 h [R25] |
| F7 | Limit heat build-up | Interior ≤ ambient + 3 °C at midday (white, ventilated) | Growth slows >30 °C, stops ~35 °C [R27] |
| F8 | Survive a dry-season onion crop | 1 season without repair; 3+ seasons life | Nov–Apr [R20b] |
| F9 | Farmer-serviceable in <2 minutes | Tool-free cartridge and lure swap | Adoption |
| F10 | No power | Passive | Cost, reliability |

### 1.2 Constraints
- **Cost:** Station COGS ≤ ₱300 at a 100-unit batch; cartridge ≤ ₱25.
- **Materials:** locally available in Mindoro hardware and textile stores; fabricated in the MinSU ABE shop with hand tools and simple jigs.
- **Safety:** farmers never handle loose spore powder.
- **Regulatory:** the Station contains no active ingredient; the cartridge is handled as a pesticide product (`proposal.md` §9.2).

### 1.3 Target insect dimensions (for openings)
- *S. exigua* adult: wingspan ≈ 25–30 mm; body length ≈ 10–14 mm (standard entomology references; measure 20 field-caught males in October).
- **Design rule:** every opening a moth must pass is ≥ 4 × wingspan in its smallest dimension, so ≥ 100 mm bore and ≥ 80 mm entry window.

---

## 2. CONCEPT SELECTION

Four concepts, each adapted from a published or commercial device:

| Concept | Source | Description |
|---|---|---|
| **A. Hood + baffle + open velvet tube** | Unitrap geometry + Toledo/icipe open-bottom velvet cylinder [R6] | Lure under a hood; moths hit smooth cross-vanes, drop into a velvet-lined tube, exit through the open bottom |
| B. Perforated bottle | icipe thrips device (Lynfield trap, 2 × 3 cm holes) [R5] | Closed bottle, side holes, velvet inner cylinder |
| C. Velvet-floored delta | Standard delta monitoring trap | Delta tent with velvet floor instead of sticky card |
| D. Bottomless bucket | Unitrap with velvet funnel, no bucket | Moth slides down a velvet funnel and falls out |

### Decision matrix (1 = poor, 5 = best; weights sum to 100)

| Criterion | Weight | A | B | C | D |
|---|---|---|---|---|---|
| Moth exits alive (F3) | 20 | 5 | 2 (moths trapped by small holes) | 4 | 5 |
| Spore contact (F2) | 20 | 4 | 4 | 3 (moths may land on the roof only) | 3 (fast slide, brief contact) |
| Sun protection (F6) | 15 | 5 | 4 | 2 (open ends) | 3 |
| Lure–spore separation (F5) | 10 | 5 | 3 | 2 | 4 |
| Cartridge swap (F9) | 10 | 5 | 3 | 4 | 3 |
| Cost / local materials | 15 | 4 | 4 | 5 | 3 (funnel fabrication) |
| Rain protection | 10 | 5 | 4 | 3 | 4 |
| **Weighted score** | 100 | **4.6** | 3.4 | 3.4 | 3.7 |

**Selected: Concept A.** Concepts C and D stay as fallback variants if the bench test (§7) shows poor contact.

---

## 3. DETAILED DESIGN (Concept A)

### 3.1 Assembly drawing (side section, not to scale)

```
                  ◄──────────────── 400 mm hood (inverted white PP basin) ───────────────►
                 ╔══════════════════════════════════╤══════════════════════════════════╗
                 ║                              ┌───┴───┐  M6 hanger rod + wing nuts   ║ ▲
                 ║                              │ LURE  │  (lure height adjustable     ║ │ ~100 mm
                 ║                              │ CAGE  │   0–60 mm)                   ║ │ basin depth
                 ╚═════════════╤════════════════└───┬───┘════════════════╤═════════════╝ ▼
                               │            ┌───────┴───────┐            │   ▲
     moths enter from all  ──► │  support   │  cross baffle │  support   │   │ 80 mm ENTRY WINDOW
     sides (360°)              │  rod ×3    │  vanes (plain │  rod       │   │ (open sides)
                               │            │  white)       │            │   ▼
                               │     ┌──────┴───────────────┴──────┐     │
                               └─────┤  ▒▒▒ 50 mm SUN COLLAR ▒▒▒   ├─────┘   ← plain PVC, no velvet
                                     │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
                                     │ ░  VELVET SPORE SLEEVE    ░ │  ← cartridge, 150 mm tall
                                     │ ░  (2 g M. anisopliae)    ░ │     4-inch PVC tube,
                                     │ ░                         ░ │     200 mm total length
                                     │ ░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
                                     └─────────────┬───────────────┘
                                       OPEN BOTTOM │ (~102 mm bore) → moth exits
                                     ══════ hose clamps ══════ bamboo / PVC pole
                                                   │
                                   tube bottom ≈ 600 mm above soil (adjustable)
```

### 3.2 Parts list and specifications

| # | Part | Material / spec | Dimensions | Function |
|---|---|---|---|---|
| P1 | Hood | White polypropylene basin (*palanggana*), inverted; UV-stabilized preferred | Ø 400 mm, depth ~100 mm | Rain and sun shield; lure chamber; holds plume near the entry window |
| P2 | Lure hanger | M6 threaded rod, 2 wing nuts, 2 washers (galvanized) | 200 mm | Adjusts lure height; lure to top of vanes 60–120 mm |
| P3 | Lure cage | PP cup (film-canister size) with snap lid, 6 × Ø 8 mm holes | Ø 35 × 50 mm | Holds the rubber-septum lure; prevents farmer contact; tool-free swap |
| P4 | Baffle vanes | 2 white corrugated plastic (coroplast) plates, 3–4 mm, slotted to interlock as a cross | 100 mm W × 100 mm H each (80 mm in window + 20 mm into tube) | Moths flying at the lure hit the vanes and drop into the tube (unitrap principle) |
| P5 | Tube | 4-inch PVC pipe (PH "4-inch", ~110 mm OD, ~102 mm ID), exterior painted white | 200 mm long | Opaque inoculation chamber |
| P6 | Sun collar | Top 50 mm of P5 left bare (no velvet) | 50 mm | Keeps low-angle sun off the velvet (§3.4) |
| P7 | Spore sleeve (cartridge) | Black cotton or polyester velvet bonded to 0.3 mm PET backing; 2 g dry *M. anisopliae* conidia | 330 × 150 mm (curls to fit 102 mm ID with 10 mm overlap) | Spore surface; PET spring holds it against the wall; slides in and out from the bottom |
| P8 | Sleeve stop | 3 stainless blind rivets or a PVC ring inside the tube at 50 mm below the top | — | Sleeve sits against the stop, which defines the collar |
| P9 | Support rods | 3 × galvanized iron rod, Ø 3 mm, hooked ends | 220 mm | Connect hood to tube at 120°; set the 80 mm entry window |
| P10 | Pole mount | 2 stainless hose clamps (#40); pole = bamboo or 1" PVC, 1.2 m | — | Mount; tube bottom ~600 mm above soil |
| P11 | Label | Waterproof sticker, Tagalog instructions + batch/date | 80 × 50 mm | Instructions, traceability |

### 3.3 Key dimensions and why

| Dimension | Value | Reason |
|---|---|---|
| Lure → top of vanes | 60–120 mm (adjustable) | Plume source inside the hood, directly above the baffle |
| Lure → nearest velvet | **≥ 210 mm** (≥100 lure-to-vane + 80 window + 50 collar, minus hood overlap) | Far exceeds the 5–10 cm precaution [R5, R6] |
| Entry window height | 80 mm | ~3× wingspan; small enough for the hood to shade the tube (§3.4) |
| Tube bore | ~102 mm | ~3.5–4× wingspan; moths can flutter down and exit |
| Velvet sleeve height | 150 mm | Enough wall contact during descent; same order as the icipe 120 mm cylinder [R6] |
| Hood diameter | 400 mm | Shades the tube top; see the sun-angle calculation |
| Mount height | Tube bottom ~600 mm | Onion canopy ~300–450 mm; trap at or just above canopy is standard [R6, R23] |

### 3.4 Sun-shading calculation (F6)
- Hood overhang beyond the tube edge: (400 − 110) / 2 = **145 mm**.
- Vertical gap between hood rim and tube top: **80 mm**.
- Direct sun can enter the tube top only when sun elevation θ < atan(80 / 145) = **28.9°**.
- At θ = 28.9°, the beam's penetration depth into a 102 mm bore is ≈ 102 × tan(28.9°) = **56 mm**. That lands just at the 50 mm sun collar edge.
- **Result:** the velvet gets direct sun only in the first and last ~1.5 hours of daylight (sun below ~29° in the Mindoro dry season). UV-B is weakest then, and the exposure is a thin strip at the sleeve's top edge.
- **Rejected:** the first sketch used a 300 mm hood and a 120 mm window. That let direct sun onto the velvet at elevations up to ~52° (mid-morning and mid-afternoon).

### 3.5 Heat management (F7)
- White hood and white-painted tube reflect sunlight.
- Open sides and open bottom allow chimney ventilation (warm air rises out the entry window).
- **Test:** place a ₱150 digital thermometer probe inside the tube versus ambient in shade at 12:00–14:00 for 3 days. Pass: ≤ ambient + 3 °C.
- If it fails: drill 6 × Ø 10 mm vent holes in the hood crown (shielded by the lure cage), or add a second reflective foil skin on the tube.

### 3.6 Configuration variants for the bench test
- **A1 (baseline):** plain vanes, velvet sleeve only.
- **A2 (more contact):** vanes also covered with velvet covers dusted with 0.5 g conidia. More contact, but the vane velvet is less shaded, so swap it every 7 days.
- **A3 (lure lower):** lure dropped to 60 mm above the vanes. Stronger plume at the window.

The bench test (§7.1) picks the variant with the best spore pickup.

---

## 4. BILL OF MATERIALS

### 4.1 Station

| Part | Prototype (retail, 1 unit) | Batch of 100 (per unit) |
|---|---|---|
| P1 Hood, PP basin 40 cm | ₱110 | ₱65 |
| P2 M6 rod 200 mm + 2 wing nuts + washers | ₱45 | ₱20 |
| P3 Lure cage (PP cup) | ₱10 | ₱6 |
| P4 Baffle vanes (coroplast) | ₱30 | ₱12 |
| P5 4-inch PVC tube, 200 mm | ₱45 | ₱30 |
| Paint (white, exterior) | ₱40 | ₱8 |
| P8 Sleeve stop (rivets) | ₱10 | ₱4 |
| P9 3 × GI rods, Ø 3 mm | ₱30 | ₱18 |
| P10 2 hose clamps | ₱40 | ₱24 |
| Pole (bamboo, 1.2 m) | ₱30 | ₱20 |
| P11 Label | ₱10 | ₱5 |
| Fasteners / misc | ₱25 | ₱8 |
| Packaging (bag + instruction card) | ₱20 | ₱15 |
| **Materials** | **₱445** | **₱235** |
| Labor (25 min at ₱120/h) | (team) | ₱50 |
| **Station COGS** | **~₱445** | **₱285** |

### 4.2 Spore cartridge (per sleeve)

| Item | Cost |
|---|---|
| Dry conidia 2 g (≈ 70 g palay substrate + bag/energy/labor share) | ₱4 |
| Velvet 330 × 150 mm (~0.05 m² at ~₱150/linear m, 1.1 m wide) | ₱7 |
| PET backing 0.3 mm | ₱2 |
| Foil pouch (heat-sealed) | ₱3 |
| Silica gel sachet 5 g | ₱2 |
| Label + loading labor | ₱2 |
| **Cartridge COGS** | **₱20** |

### 4.3 Season Kit (per Station)
3 lures (₱60 landed each) + 6 cartridges (₱20 each) + gloves/instructions/packaging (₱30) = **₱330 COGS**; sells for ₱520 (`phase7-financial-model.md`).

---

## 5. FABRICATION SOP (MinSU ABE shop)

**Jigs to build first (₱3,500 total):**
- **J1** tube cut-off box: miter-box style, 200 mm stop.
- **J2** drill template: paper wrap-around with 3 rod holes at 120°, 15 mm below the top, and 3 rivet holes at 50 mm.
- **J3** hood drill template: center hole + 3 rod holes on a 130 mm radius.
- **J4** vane slot guide.
- **J5** sleeve cutting board: 330 × 150 mm stencil.

**Steps (per Station, about 25 minutes):**
1. Cut the PVC to 200 mm (J1). Deburr.
2. Drill 3 × Ø 4 mm rod holes (J2) and 3 × Ø 3.2 mm rivet holes; set the rivets as the sleeve stop.
3. Paint the tube exterior white; dry for 24 h (batch step).
4. Drill the hood: center Ø 7 mm and 3 × Ø 4 mm (J3).
5. Cut the vanes (100 × 100 mm) and slot them (J4); interlock to form a cross; notch the lower 20 mm so they sit inside the tube top.
6. Bend the rod hooks and fit the rods hood-to-tube so the entry window is 80 mm (gauge block).
7. Fit the M6 hanger through the hood center with wing nuts; attach the lure cage.
8. Attach the hose clamps (loose) for the pole; apply the label; bag with the instruction card.

**QC per unit:**
- Window 80 ± 5 mm.
- Tube square to hood (visual).
- Lure cage opens by hand.
- Clamps included.

---

## 6. SPORE CARTRIDGE PRODUCTION SOP

Based on PhilRice Rice Technology Bulletin No. 44 [R11], plus dry-conidia harvesting practice from icipe [R6]. Run under adviser supervision in the MinSU lab or at a partner lab. See the regulatory stage in `proposal.md` §9.2.

### 6.1 Starter
1. Get an *M. anisopliae* culture from PhilRice or NCPC-UPLB (or BPI). Record the isolate code and source.
2. Maintain it on PDA (39 g/L) or potato sucrose agar slants. Sterilize 121 °C / 15 psi / 15 min. Streak, incubate 1–2 weeks until green [R11].
3. Keep mother slants refrigerated. Subculture no more than 3 generations from the original (the usual practice to avoid losing virulence). Get fresh stock from the source each season.

### 6.2 Mass production (per bag)
1. 200 g palay + 200 mL water in a 9 × 16 PP bag; PVC ring + cotton plug [R11].
2. Sterilize 15 psi for **1 h**; cool [R11].
3. Add 5 mL sterile 0.05% soap solution to a 1–2-week slant; scrape the conidia; inoculate the bag with 5 mL suspension; mix [R11].
4. Incubate 14–21 days at room temperature (~26 °C ideal [R6]) in the dark until the grains are fully olive-green.

### 6.3 Dry-conidia harvest (for cartridges, not spraying)
1. Open the bags in a hood or a still-air box. Spread the grains in trays covered with paper, and air-dry in the shade for 3–5 days until the grains are brittle [R6].
2. Shake or sieve the grains over a fine mesh (e.g., 100–150 µm screen or fine nylon stocking) into a clean container. The powder that comes through is dry conidia.
3. Final drying: store the powder with silica gel in a sealed jar for 48 h [R26].
4. **Record yield (g powder per kg rice).** The business model assumes ~30 g/kg. Update it with real data.

### 6.4 Batch QC (every batch)

| Test | Method | Pass |
|---|---|---|
| Germination | Suspend in 0.05% soap; spread on PDA; incubate 18–24 h at ~25 °C; count 100 conidia × 3 fields (germ tube ≥ spore width) [R6] | ≥ 80% |
| Purity | Visual: uniform olive-green, no black/pink/yellow molds, no bacterial slime | Clean |
| Concentration (if hemocytometer available) | Count conidia per gram | Record (target ≥ 10⁹ conidia/g) |

Discard failed batches. Autoclave or bury them. Never sell them.

### 6.5 Cartridge loading
1. Cut the velvet and PET to 330 × 150 mm; bond them with contact adhesive; cure 24 h.
2. Weigh **2.0 g** of conidia. Spread it evenly on the velvet with a soft brush in a closed box (loading station), then tap off the excess.
3. Roll the sleeve velvet-side in; insert it into a foil pouch with a 5 g silica sachet; heat-seal.
4. Label: isolate, batch, loading date, **use-by date = loading + 90 days (refrigerated) or + 30 days (room temperature)**. This is conservative against the storage data [R26]; revise after in-house tests.
5. Store refrigerated (4–8 °C) until dispatch.

**PPE for loaders:** N95 mask, nitrile gloves, lab coat. *M. anisopliae* has low toxicity [R28], but fine powders can irritate airways and conidia are potential allergens.

---

## 7. PERFORMANCE TESTS (product QC, not research)

### 7.1 Bench test: spore pickup (validation step V2)
- **Moths:** field-caught *S. exigua* males from a plain DA-style pheromone trap (no glue) in San Jose, or from a partner's lab colony.
- **Setup:** a mesh cage 1 × 1 × 1 m at night with one Station (variant A1, A2 or A3) and one fresh lure; release 20 males; after 2 h, catch all moths with an aspirator.
- **Measures:**
  - % of moths with visible green dust (hand lens).
  - Tap-test: touch each moth's legs and abdomen to PDA, incubate 3–5 days, record growth.
- **Pass:** ≥ 80% of the moths that entered the tube show conidia.
- **Also record:** % of moths released that reached the Station, and any moths that failed to exit (should be 0).

### 7.2 Cartridge persistence in the field (validation step V3)
- 3 Stations in a San Jose onion field.
- Swab 1 cm² of velvet at days 0, 7, 14 and 21; run the germination test (§6.4).
- **Pass:** ≥ 70% germination at day 14. If it fails, move to a 10-day swap interval.

### 7.3 Environment inside the Station
- USB temperature/RH logger inside one tube and one in the crop canopy, logging every 15 min for 2 weeks.
- **Pass:** interior max ≤ ambient + 3 °C; canopy night RH ≥ 80% on most nights (the humidity risk [R10]).

### 7.4 Durability
- 2 Stations left in the field for a full season.
- Record damage, fading, rod corrosion, clamp slippage and animal interference.

---

## 8. INSTALLATION AND MAINTENANCE (farmer card)

**Layout:**
- 4 Stations per hectare in a grid about 50 m apart. For a 0.5 ha farm: 2 Stations, 35 m apart, along the long axis.
- Place them near the dikes (*pilapil*) for easy access.

**When to install:** at transplanting, **before** the moth peak (25–59 days after planting [R13]).

**Tagalog instruction card (printed on the label):**
> **PAANO GAMITIN (How to use)**
> 1. **Ibaon ang poste** (30 cm sa lupa). Ang ilalim ng tubo ay mga 60 cm mula sa lupa, bahagyang mas mataas sa sibuyas. *(Bury the pole 30 cm deep. The tube bottom should be about 60 cm off the ground, slightly above the onions.)*
> 2. **Ilagay ang pain (lure)** sa maliit na lalagyan sa ilalim ng takip. Palitan tuwing **4 na linggo.** *(Put the lure in the small holder under the hood. Replace every 4 weeks.)*
> 3. **Ipasok ang spore sleeve** mula sa ilalim ng tubo hanggang sa huminto. Palitan tuwing **2 linggo.** Gumamit ng guwantes. Huwag buksan ang supot hanggang ikakabit na. *(Slide the spore sleeve in from the bottom of the tube until it stops. Replace every 2 weeks. Wear gloves. Don't open the pouch until you're installing it.)*
> 4. **Walang mahuhuli — iyan ang punto.** Lalabas ang gamu-gamo na may dalang amag at ikakalat ito sa ibang harabas. *(Nothing gets caught — that's the point. The moth leaves carrying the fungus and spreads it to other harabas.)*
> 5. **Hanapin ang patay na uod na may puti o berdeng amag** — tanda na gumagana. *(Look for dead caterpillars with white or green mold — a sign it's working.)*
> 6. Itago ang Station pagkatapos ng anihan. *(Store the Station after harvest.)* Ang lumang sleeve ay ibaon sa lupa o ibalik sa amin. *(Bury old sleeves in the soil or return them to us.)*

**Maintenance calendar (100-day crop, transplant at day 0):**

| Day | Action |
|---|---|
| 0 | Install Station, lure #1, cartridge #1 |
| 14 | Cartridge #2 |
| 28 | Lure #2, cartridge #3 |
| 42 | Cartridge #4 |
| 56 | Lure #3, cartridge #5 |
| 70 | Cartridge #6 |
| 84–100 | Leave in place until harvest; remove and store |

*This schedule is why the Season Kit is 3 lures + 6 cartridges.*

---

## 9. SAFETY, ENVIRONMENT, DISPOSAL
- **Farmers:** sealed sleeves; gloves included; no powder handling.
- **Non-targets:** the pheromone is species-specific, so few non-target insects enter the tube. The point source uses grams per hectare versus broadcast sprays. *M. anisopliae* is not harmful to honey bees [R28]. Parasitoids can be infected on direct contact [R40], which is another reason for a point source over spraying.
- **Used sleeves:** the fungus is a natural soil organism. Bury used sleeves in the field, or return them for autoclaving and reuse of the PET backing (circular option, v2).
- **Livestock and pets:** mount height and the hood keep animals away from the sleeve.

---

## 10. DESIGN RISKS AND FALLBACKS

| Risk | Early sign | Fallback |
|---|---|---|
| Moths circle the lure but don't drop into the tube | Bench test: <50% enter the tube | Variant A2 (velvet vanes); increase vane height; Concept D (velvet funnel) |
| Moths get stuck in the tube | Dead or trapped moths in the tube | Shorten the tube to 150 mm; widen to 5-inch PVC |
| Spores wash out in dew or light rain | Wet, clumped velvet | Hydrophobic velvet (polyester); a small drip ring on the tube top |
| Interior too hot | Logger > ambient + 3 °C | Vent holes, reflective skin, relocate to a slightly shaded dike |
| Ants or spiders colonize the Station | Webs, ant trails | Grease band on the pole; weekly brush-off |
| Lure plume too weak at the window | Few moths reach the Station vs a plain trap | Lower the lure (A3); compare 2 lure brands |

---

## 11. v2 ROADMAP
1. **Injection-molded one-piece body** (hood + window + tube) at 1,000+ units/year. Lower labor, consistent geometry.
2. **Dual cartridge:** *M. anisopliae* + *M. rileyi* (with NCPC-UPLB) to add larval virulence [R1, R2].
3. **Swappable lures:** *S. litura* (onion, vegetables) and *S. frugiperda* (corn), using the same body.
4. **Electrostatic carrier powder** (Entostat-type) to increase conidia pickup per visit [R32]. Needs a partner.
5. **Returnable sleeve program:** collect, autoclave, re-load. Lower cartridge cost and waste.
