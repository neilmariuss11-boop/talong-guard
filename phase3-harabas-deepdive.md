# Phase 3: Deep Dive — Harabas (Onion Armyworm) and the Autodissemination Station
**Rewritten 2026-09-27** (was: "Smart Eggplant Borer Trap / TalongGuard". The eggplant version is in git history.)

> Evidence tags [R#] refer to `research-synthesis.md` §12.

---

## 1. THE PROBLEM (research-backed)

### 1.1 The pest: *Spodoptera exigua* (harabas / onion armyworm / beet armyworm)
- **Order and family:** Lepidoptera, Noctuidae. A polyphagous pest; onion and shallot are key hosts in the Philippines.
- **Life cycle:**
  - Egg masses laid at night on leaves (tens to hundreds of eggs per mass).
  - Larvae feed gregariously, then disperse and defoliate.
  - Pupation in soil.
  - About 30-day generation; 5–8 generations a year in warm areas [R23].
- **Adults:** nocturnal. Males home in on the female sex pheromone, most actively late at night when mating happens. Each male mates ~5 times on average (range 1–11) [R33].
- **Migration:** the 2016 Nueva Ecija outbreak was traced to mass long-distance migration from the northeast, possibly El Niño-linked [R12].
- **Timing in PH onion:** pheromone trap catches peak **25–59 days after planting** [R13].
- **Pheromone:** Z9,E12-14:OAc (major) + Z9-14:OH (+ Z11-16:OAc). The East Asian optimum is 7:3:1 [R24].

### 1.2 The damage (Philippines)
- **2016 Nueva Ecija:** 5,330 ha, 4,089 farmers, **₱1.61 B** [R12].
- **2024 national:** 12,138 ha infested; 674 ha totally damaged; MIMAROPA 871.6 ha partially damaged [R16].
- **2024 Occidental Mindoro:** ₱30 M armyworm damage; San Jose, Magsaysay and Looc under a state of calamity [R17].
- **Farmer testimony (Bongabon):** outbreak about every 3 years; deep debt [R21a].
- **Pangasinan:** outbreak inputs about double to ₱400k/ha, and still only about half the crop is saved [R21].

### 1.3 What farmers do now (and why it isn't enough)

| Practice | Problem |
|---|---|
| Spray insecticides (near-universal [R21b]) | Resistance: diamides up to 2,477-fold, emamectin [R43]; cost; health |
| DA pheromone traps | **Monitoring only.** Useful for timing [R13, R14], but no population reduction |
| Spray *Metarhizium* | Sunlight kills spores in hours [R25]; labor-intensive |
| Abandon onion | Bongabon area fell from 2,800 to 1,800 ha [R21b] |

### 1.4 The insight
The male moth is the perfect delivery vehicle. It is **attracted to one point** (the lure), then **flies to exactly where the females are**, and it mates several times. Put a slow-acting, safe, natural pathogen on him, and **the pest spreads its own disease**. The science pieces are already published [R4, R5, R6, R7, R8]. Nobody has turned them into a product for harabas.

---

## 2. THE SOLUTION: THE STATION (summary)
- A pole-mounted device: 40 cm hood → lure cage → baffle vanes → 20 cm PVC tube with a removable velvet spore sleeve → open bottom.
- The moth is lured in, hits the baffles, drops through the dusted tube, and **exits alive carrying *M. anisopliae* conidia**.
- Contaminated moths die in about 4 days (LT50 3.9 d in FAW [R4]), pass spores to mates [R4], and reduce egg-laying and hatch [R4, R39]. Spores reaching larvae kill them [R1, R10].
- No power. Service every 2 weeks (sleeve) and every 4 weeks (lure).
- Full engineering: `phase5-device-design.md`.

### Key value proposition
> **"Ang gamu-gamo mismo ang magdadala ng lunas."** *(The moth itself carries the cure.)*
> A familiar pheromone trap that, instead of catching a few moths, **turns every visiting moth into a sprayer**. It works at night while the farmer sleeps, with spores kept out of the sun.

---

## 3. CUSTOMER PERSONAS

### Primary: "Mang Ramon," San Jose onion farmer
- 52; 1.5 ha; onion in the dry season, rice in the wet season.
- Invests ₱200–300k/ha [R20], often **financed by traders**.
- Sprays 3–6 times a season; was hit by harabas in 2024.
- Has seen DA pheromone traps; doesn't use the counts.
- Basic phone; trusts neighbors and the municipal technician.
- **Buys when:** he sees fuzzy (mycosed) larvae in a neighbor's field and fewer sprays.
- **Objections:** "Paano kung hindi gumana?" *(What if it doesn't work?)*; "Wala namang nahuhuli?" *(But nothing gets caught?)*; cash is tight at planting.
- **What helps:** a field-day demo; payment at harvest via a cooperative or trader; an LGU subsidy.

### Secondary: "Ma'am Liza," Municipal Agriculturist's office (San Jose MAO)
- Manages the crop protection program; distributes traps and inputs; faces criticism after outbreaks.
- Needs visible, non-chemical, modern programs, and has a procurement budget.
- **Buys when:** the demo results are credible, the paperwork is simple, and the unit cost fits small-value procurement (precedent: DA-RFO III bought *S. exigua* traps for ₱301k [R22]).

### Tertiary: irrigators' associations and cooperatives (e.g., Caguray RIS, Magsaysay, ~1,990 ha [R19])
- Can buy for **contiguous blocks**, which is best for an area-wide effect.
- Group credit; bulk orders; peer influence.

### Influencers
- Onion **traders and financiers** (they carry the crop risk).
- **Agri-supply store** owners.
- DA-MIMAROPA "Task Force Sibuyas" [R44].
- Local radio.

---

## 4. COMPETITIVE LANDSCAPE

| Alternative | Type | Strength | Weakness |
|---|---|---|---|
| Chlorantraniliprole (e.g., Prevathon), emamectin (e.g., Proclaim) | Chemical | Fast knockdown | Resistance [R43]; cost; residues |
| DA pheromone traps (Verca Agro Chem etc.) | Monitoring | Familiar, cheap or free | No population reduction |
| *Metarhizium* / *Beauveria* sprays (PhilRice, BPI, OMSC trial) | Biocontrol spray | Safe, cheap [R11] | UV kills spores [R25]; labor |
| Bt / NPV products | Biocontrol spray | Selective | Spraying, UV, availability |
| Mass trapping | Physical | Removes males | 40–50 traps/ha [R23b]; males mate multiple times |
| Exosex autoconfusion (UK) | Pheromone-powder station | Commercial proof of powder pickup [R32] | Not for harabas; not in PH; pheromone, not pathogen |
| **The Station** | **Autodissemination** | Moth does the spraying; spores shaded; area-wide | Must prove itself in local fields; FPA pathway for cartridges |

**Position:** between "monitoring trap" and "spray". It's the only option that *uses the pest's own behavior* to deliver a biocontrol agent.

---

## 5. MVP FEATURE SET

### Must-have (v1.0, demo season)
- Hood, lure cage and baffle vanes; 4-inch PVC tube with sun collar; open bottom.
- Removable velvet spore sleeve (2 g *M. anisopliae*), sealed foil + silica.
- Tool-free lure and sleeve swap.
- Tagalog label and instructions.
- Adjustable lure height (bench-test variants).

### Nice-to-have (v1.5, first sales)
- Velvet vane covers (variant A2), if the bench test shows more pickup.
- Color-coded sleeves by swap date (e.g., blue = week 1–2, red = week 3–4).
- QR code linking to a Tagalog video on Facebook.

### Future (v2.0)
- Injection-molded body.
- Dual *M. anisopliae* + *M. rileyi* cartridge (NCPC-UPLB partnership) [R1, R2].
- Swappable lures for *S. litura* and fall armyworm (corn).
- Electrostatic carrier powder [R32].
- Returnable sleeve program.

---

## 6. BILL OF MATERIALS (summary)
- **Station:** ₱445 prototype (retail parts) → **₱285** at a 100-unit batch (materials ₱235 + labor ₱50).
- **Cartridge:** **₱20**.
- **Lure:** **₱60 landed** (assumption).
- **Season Kit** (3 lures + 6 cartridges + packaging): **₱330**.
- **Selling prices:** Station ₱690; Season Kit ₱520.
- Details: `phase5-device-design.md` §4; economics: `phase7-financial-model.md`.

### Customer ROI (per hectare, 4 Stations)
- First season ₱4,840; following seasons ₱2,080.
- Onion gross ≈ ₱271,800/ha (9.06 t × ₱30/kg) [R20, R36].
- **Break-even: prevent 0.77% yield loss** (kit only), or skip about 1 spray (to confirm in interviews).

---

## 7. LEAN CANVAS

| Block | Content |
|---|---|
| **Problem** | (1) Harabas outbreaks destroy onion suddenly [R12, R16, R17]. (2) Insecticides failing (resistance) and costly [R21, R43]. (3) Existing pheromone traps only monitor; biocontrol sprays die in sunlight [R25] |
| **Customer segments** | LGU/DA crop protection programs; irrigators' associations and cooperatives; commercial onion growers in San Jose and Magsaysay, Occidental Mindoro (8,637 ha province [R18]) |
| **Unique value proposition** | "The moth itself carries the cure": a pheromone station that turns visiting harabas moths into carriers of a natural fungus, protected from sunlight, no spraying |
| **Solution** | Hood + baffle + velvet spore tube Station; season refill kit (lures + spore sleeves); field-day demonstrations |
| **Channels** | LGU/MAO programs; association meetings; field days; agri-supply stores; Facebook and local radio in Tagalog |
| **Revenue streams** | Station ₱690 (one-time); Season Kit ₱520 per Station per season (recurring); v2 service fee |
| **Cost structure** | Materials, lures (import), spore production (palay, lab), labor, logistics (Victoria ↔ San Jose), FPA registration |
| **Key metrics** | Hectares covered; kit re-order rate; mycosed larvae observed; farmer spray counts; NPS; lure landed cost |
| **Unfair advantage** | First autodissemination product for harabas; MinSU + LGU + PhilRice/NCPC relationships; local spore supply chain; Utility Model; first local demo data |

---

## 8. RISKIEST ASSUMPTIONS (must validate; see `phase6-validation-plan.md`)

| Rank | Assumption | Why risky | Test |
|---|---|---|---|
| 1 | Moths entering the Station pick up enough spores | No published harabas device; geometry is new | Bench test V2 (`phase5` §7.1) |
| 2 | Farmers and LGUs will pay ₱690 + ₱520/season | Low farmgate prices in 2026 [R20] | Interviews, price ladder (V1), pre-orders (V5) |
| 3 | There is a legal pathway for spore cartridges | FPA registration needed for sale [R29] | Letters to FPA, partner with a registrant or government lab |
| 4 | Lures can be landed at ≤ ₱60 | Import small orders; customs | 2 supplier quotes |
| 5 | Farmers can *see* the effect in one season | Autodissemination acts over generations | Mycosed-larvae walks; spray logs; field day |
| 6 | Night humidity is high enough for infection | FT83 mortality drops at low RH [R10] | Canopy loggers (V6) |
| 7 | Spores survive 14 days in the Station | Heat and humidity in Mindoro | Swab germination (V3) |

---

## 9. SOURCES
See `research-synthesis.md` §12 (R1–R48).
