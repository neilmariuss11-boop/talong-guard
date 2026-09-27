# Research Synthesis — Pheromone-Baited Metarhizium Autodissemination Station for Onion Armyworm (Harabas)

**Prepared:** 2026-09-27
**Project type:** Technopreneurship (product + business), NOT a thesis
**Team base:** Mindoro State University (MinSU) Main Campus, Victoria, Oriental Mindoro
**Field / market site:** San Jose, Occidental Mindoro
**Working product name:** *TBD* (see `proposal.md` §12 for naming options). This document calls it **"the Station."**

> **How to use this document.** This is the evidence base for every other document in the repo. Each claim carries a source tag like **[R4]**, and the full reference list is in §12. Each finding also has a confidence grade:
> - **HIGH:** peer-reviewed, directly on our pest or setting.
> - **MEDIUM:** peer-reviewed but on a related pest or setting, or an official or news source on our setting.
> - **LOW:** a single source, a student paper, a news summary, or our own estimate.
>
> Where the evidence *corrects* something in our earlier notes, it is flagged with ⚠️ **CORRECTION**.

---

## 0. ONE-PAGE SUMMARY (read this if nothing else)

1. **The problem is real, recurring and local.** Harabas (*Spodoptera exigua*) outbreaks have hit Philippine onion repeatedly:
   - **2016:** 5,330 ha damaged and ₱1.61 billion lost in Nueva Ecija alone [R12].
   - **2024:** 12,138 ha of onion infested nationwide [R16], plus ₱30 M in damage in Occidental Mindoro, with San Jose, Magsaysay and Looc under a state of calamity (drought plus armyworm) [R17].

   Occidental Mindoro now plants **8,637 ha** of onion (2026 season), up from 6,000 ha in 2025 [R18].
2. **Farmers' current answer is spraying, and it is failing.**
   - Spraying is the near-universal response: 305 of 310 surveyed farmers [R21b].
   - *S. exigua* develops strong resistance to the newest insecticides. Chlorantraniliprole resistance ratios reach up to 2,477-fold in monitored populations, and emamectin resistance is documented [R43].
   - During outbreaks, input spending per hectare roughly doubles, reportedly to about ₱400,000/ha in Pangasinan [R21].
3. **Our approach, autodissemination, is published science with a working precedent in other pests:**
   - Pheromone-lured male moths pick up fungal spores and carry them to females through mating contact [R4, R5, R6, R7, R8, R9].
   - The key study for us is fall armyworm (*S. frugiperda*, same genus as harabas) [R4]:
     - *M. anisopliae* ICIPE 7 killed **100% of moths** (LT50 3.9 days).
     - The moth pheromone lure did **not** inhibit spore germination.
     - Contaminated moths transmitted spores to uncontaminated moths, and the infected females laid fewer, less viable eggs.
     - Moths still carried high spore loads after 72 hours.
4. **The fungus works on harabas.**
   - Philippine isolates kill harabas larvae: *M. rileyi* gave 100% mortality at 10⁷–10⁸ conidia/mL within 7 days [R1].
   - *M. anisopliae* has already been field-sprayed against harabas on onion **in San Jose, Occidental Mindoro** [R15].
5. ⚠️ **Species choice should change.** The v1 fungus should be ***Metarhizium anisopliae*, not *M. rileyi***:
   - *M. rileyi* is excellent against *larvae*.
   - But we found **no evidence that it infects or is carried by adult moths**, the stage our device contaminates.
   - It is also notoriously hard to mass-produce, has a short shelf life [R34], and showed no egg-killing activity [R3].
   - *M. anisopliae* has adult-moth efficacy [R4], egg-killing isolates [R39], a PhilRice rice-substrate production protocol [R11], and local harabas data [R15].
   - Keep *M. rileyi* as a v2 upgrade with NCPC-UPLB.
6. ⚠️ **The "5 cm separation" rule needs a caveat:**
   - The 5 cm figure comes from a **whitefly plant volatile** [R6], and the 10 cm figure from a **thrips lure** [R5]. Both are inhibitory chemicals.
   - **Moth sex pheromones showed no inhibition** in two studies: fall armyworm [R4] and false codling moth [R7].
   - The Station will still separate lure and spores by ≥10 cm, because it costs nothing, but we should not claim this is proven necessary for harabas.
7. ⚠️ **Spore shelf life is shorter than we assumed.** Dry *M. anisopliae* conidia at ~25 °C dropped to **72.5% viability at 135 days and 28.5% at 176 days** [R26].
   - The "6–10 months at ambient" figure is only achievable with very dry spores, a desiccant and sealed packaging, or refrigeration.
   - Business implication: **produce refills per season (Nov–Apr), not a year ahead.**
8. **Humidity is a hidden risk.** *M. anisopliae* FT83 killed 86.7% of harabas larvae at 85% relative humidity (RH) but only 13.4% at 45% RH [R10]. Onion is a **dry-season** crop.
   - Night-time humidity (when moths fly and mate) is usually high.
   - But this must be measured in San Jose fields, not assumed.
9. **The biggest business risk is regulatory, not technical.**
   - Any product containing a microbial pesticide sold commercially in the Philippines must be registered with the Fertilizer and Pesticide Authority (FPA) or covered by a permit [R29].
   - Biorational products have reduced data requirements, and field trials run under an Experimental Use Permit (EUP).
   - The spore refill therefore needs a registration pathway, which drives the go-to-market design in `proposal.md` §9.
10. **The strongest market signal: the government already buys this category.**
    - DA Regional Field Office III bought *S. exigua* sex pheromone traps for ₱301,000 in 2020 from Verca Agro Chem Inc. [R22].
    - DA-BPI installs pheromone traps in onion areas as standard response [R16].
    - Extension workers in Occidental Mindoro install pheromone lures in onion fields [R44].

    Local government and DA buyers (B2G) are a realistic first channel, alongside farmer associations.

---

## 1. THE PEST — *Spodoptera exigua* (harabas, onion armyworm, beet armyworm)

### 1.1 Biology relevant to the device

| Trait | Finding | Why it matters for the Station | Source / confidence |
|---|---|---|---|
| Activity | Nocturnal; males increase activity toward end of scotophase (night), when copulation happens | Station works at night; lure must be active at night; spores must survive the day in darkness inside the device | [R33] MEDIUM |
| Male mating | Average male mates with ~5 females (range 1–11) | **Each contaminated male can reach several females.** This multiplier is the core logic of autodissemination | [R33] MEDIUM (ADW summary, not primary) |
| Female fecundity | Lays up to ~500 eggs in masses (local report); 50–150 per mass | Contaminating one female protects against hundreds of larvae | [R15] LOW; phase8 notes |
| Generation time | ~30 days; 5–8 generations/year in warm areas | Several generations inside one onion season, which gives the fungus multiple chances to cycle | [R23] MEDIUM |
| Migration | 2016 Nueva Ecija outbreak attributed to mass long-distance migration from countries northeast of PH, possibly El Niño-triggered | Outbreaks can **arrive**, not just build locally. The Station must be up before moths arrive, so deploy at transplanting | [R12] HIGH |
| Peak moth activity in onion | Pheromone trap catches peaked **25–59 days after planting** | This defines the key protection window: the Station must hold fresh spores from about day 20 to day 65 | [R13] HIGH (PH, onion) |
| Larval damage | Defoliation; outbreaks escalate within days; late instars hard to kill | Autodissemination is a **preventive** tool, not a rescue tool | [R12, R21] HIGH |

### 1.2 The pheromone

| Item | Finding | Source / confidence |
|---|---|---|
| Major component | (Z,E)-9,12-tetradecadienyl acetate (Z9,E12-14:OAc) | [R23, R24] HIGH |
| Minor components | (Z)-9-tetradecen-1-ol (Z9-14:OH); (Z)-11-hexadecenyl acetate (Z11-16:OAc) | [R24] HIGH |
| **Best blend in East Asia** | Z9,E12-14:OAc : Z9-14:OH : Z11-16:OAc = **7:3:1** (China); **7:3** two-component best in Korea | [R24] HIGH |
| Philippine blend | **No published PH-specific optimum found** | GAP → compare 2 commercial lures in pilot (§10) |
| Commercial lure | Evergreen Growers lure contains Z9-14:OH + Z9,E12-14:OAc; ~4 weeks field life, shorter in hot or dusty conditions; stores 2 years frozen; from US$3.70/lure | [R23] HIGH (vendor data) |
| Koppert Pherodis *S. exigua* | Capsule effective 6 weeks | [R23] MEDIUM |
| India supplier | Innovac Bioscience (Vadodara) *S. exigua* rubber septum lure listed at ₹25 (~₱17) | [R23] MEDIUM (listing price; excludes shipping/import) |
| Local distributor precedent | Verca Agro Chem Inc. supplied DA-RFO III's *S. exigua* sex pheromone trap order (₱301,000 contract, Dec 2020) | [R22] HIGH |
| Carrier | Rubber septa caught far more *Spodoptera* males than strip carriers (41,165 vs 6,880 in one study) | [R23] MEDIUM |

**Design implication:** buy a pre-loaded commercial rubber-septum lure. Don't formulate our own, because that would be research. Replace it every 4 weeks, or sooner in the Mindoro dry-season heat.

### 1.3 Pheromone trapping already works for harabas in PH onion (monitoring and timing)

- **Arida et al. 2003 [R13]:** trap-timed sprays cut applications from **weekly to 1–3 per season**, with yield and leaf damage similar to weekly-sprayed plots. (HIGH, PH onion.)
- **Arida et al. 2004 [R14]:** in farmers' fields, pheromone-guided plots needed 2–3 sprays (mean 2.6), versus 2–6 (mean 4.4) under farmer practice. That is **about 40% fewer sprays** with no significant yield difference.
- **DA-BPI:** installs pheromone lure traps in onion areas as part of standard outbreak response (Oct 2025, Central Luzon) [R16].

**So what:** farmers and agricultural extension workers (AEWs) already recognize a pheromone trap. The Station **upgrades a familiar object**: the lure that already attracts moths now also infects them. This lowers the adoption barrier.

---

## 2. THE PROBLEM — Size, Location, Cost

### 2.1 Outbreak history

| Year | Location | Scale | Loss | Source / confidence |
|---|---|---|---|---|
| 2016 | Nueva Ecija (14 municipalities) | 5,330 ha; 4,089 farmers | **₱1,609,997,316** (Feb–Apr 2016) | [R12] HIGH |
| 2016 | Bongabon (onion capital) | 2,938 ha most damaged | — | [R12b] MEDIUM |
| ~3-year cycle | Bongabon | "Infestation cycle approximately every three years since 2016" (farmer testimony) | Farmer debts ₱600,000; one farmer suicide reported | [R21a] MEDIUM (journalism) |
| 2018 | San Jose City, Nueva Ecija (onion-growing city) | — | ₱261 M | [R21c] MEDIUM (headline only) |
| 2024 (Mar) | Nueva Ecija | 366 of 10,217 ha infested | 6.9 ha total loss | [R16b] MEDIUM |
| **2024 (May, national)** | Central Luzon 6,980 ha; Cagayan Valley 612 ha totally damaged; Ilocos; **MIMAROPA 871.6 ha partially damaged** | **12,137.92 ha infested; 674 ha totally damaged; 4,045 ha partially damaged** | — | [R16] HIGH (DA via PNA) |
| **2024 (Mar)** | **Occidental Mindoro** | San Jose, Magsaysay, Looc under state of calamity (drought + armyworm) | **₱30 M armyworm damage** (+₱300 M drought) | [R17] HIGH (PNA) |
| 2026 | Occidental Mindoro | Harabas described as reducing yields and increasing pesticide costs; AEWs install pheromone lures under crop protection program | — | [R44] MEDIUM |

### 2.2 The Occidental Mindoro market (our site)

| Indicator | Value | Source / confidence |
|---|---|---|
| Onion area, 2026 season | **8,637 ha** (from 6,000 ha in 2025) | [R18] HIGH (BusinessWorld, FTI) |
| Onion area, San Jose alone | 3,285 ha, 83,000 MT (2023) | [R19] LOW (search-summary of NIA IV-B page; verify with MAO) |
| Magsaysay | Caguray River Irrigation System, 1,990 ha service area, mostly onion | [R19] MEDIUM |
| Sablayan | 521 ha onion (2024), +64% | [R37] MEDIUM |
| Season | Plant **Nov–Jan**, harvest **Jan/Feb–Apr** (dry season) | [R20b] MEDIUM |
| Production cost | ₱200,000–300,000/ha | [R20] MEDIUM |
| Farmgate price (Feb 2026) | ₱30–45/kg (glut) | [R20] HIGH |
| Cold storage | 8 facilities, ~16% of projected harvest | [R18] HIGH |
| Govt attention | DA-MIMAROPA "Task Force Sibuyas"; 5 municipalities monitored | [R44] MEDIUM |

⚠️ **CORRECTION.** Earlier notes said "Nueva Ecija 2,300+ ha", which is only Bongabon's *red shallot* area. Bongabon alone is about 4,589 ha across varieties, and Nueva Ecija as a province plants about 10,000–13,000 ha with about 21,000 farmers, an average of **~0.55 ha per farmer** [R36].

⚠️ **CORRECTION.** Earlier notes placed San Jose in *Oriental* Mindoro. **San Jose is in Occidental Mindoro.** The team is at MinSU Main Campus, Victoria, Oriental Mindoro, and the field site is San Jose, Occidental Mindoro.

### 2.3 What farmers do now and why it fails

| Practice | Evidence | Weakness |
|---|---|---|
| Calendar or panic spraying | 305/310 farmers spray during infestations [R21b] | Resistance: chlorantraniliprole ratios 6.3–2,477-fold, emamectin resistance documented [R43]; cost spikes |
| Emergency spending | ~₱400,000/ha during outbreak vs ~₱200,000 normal, still saving only ~half the crop (Pangasinan) [R21] | Debt; pawned land [R21a] |
| Pheromone traps (from DA) | Monitoring and timing tool [R13, R14, R22] | Only *tells* farmers when to spray; doesn't reduce the population by itself |
| Metarhizium spraying | OMSC San Jose trial, 525 mL/L best [R15]; PhilRice ₱250/ha vs ₱800–1,200 chemical (rice, 2002 prices) [R11] | Sunlight kills spores in hours [R25]; must be sprayed repeatedly, late afternoon; farmers must handle and mix |
| Crop abandonment | Bongabon onion area shrank from 2,800 to 1,800 ha due to high investment risk [R21b] | Lost production; import dependence |

---

## 3. THE BIOCONTROL AGENT — Which *Metarhizium*?

### 3.1 Evidence table

| Question | *M. rileyi* (= *Nomuraea rileyi*) | *M. anisopliae* | Source / confidence |
|---|---|---|---|
| Kills harabas **larvae**? | **Yes.** PH isolate from Nueva Ecija onion: infection from day 2; >50% mortality by day 6; **100% at 10⁷–10⁸ conidia/mL by day 7**; 73–100% by day 10; LT 4.17–7.83 d; pupation <20%, adult emergence 3% | **Yes.** FT83 (Korea): **100% of L2 larvae by day 3** at 10⁷ conidia/mL; effective 20–30 °C. OMSC San Jose onion field trial: best mortality at 525 mL/L | [R1] HIGH; [R10] HIGH; [R15] LOW-MED (student journal) |
| Kills **adult moths**? | **No evidence found** (all studies are on larvae) | **Yes.** Akutse 2020: ICIPE 7 **100% moth mortality**, LT50 3.9 d (FAW) | [R4] HIGH |
| Horizontal transmission moth-to-moth? | **No evidence found** | **Yes.** Male and female FAW moths transmitted conidia to untreated moths; high mortality in donor and recipient groups | [R4] HIGH |
| Effect on eggs | **No ovicidal activity** (FAW) | ICIPE 78, 40, 20 caused **87.0, 83.0, 79.5% egg mortality** (FAW); infected females had lower oviposition and hatchability | [R3] HIGH; [R39, R4] HIGH |
| Spore retention on moths | — | "Single moths still retained high conidial numbers 72 h post-inoculation" | [R4] HIGH |
| Pheromone compatibility | — | FAW lure (FALLTRACT) did **not** affect germination; FCM pheromone (Cryptrack) did **not** affect viability | [R4, R7] HIGH |
| Mass production | **Difficult:** "highly variable growth and low productivity" in solid-state fermentation; needs supplements (yeast extract, V8 juice); short-lived propagules, poor stress tolerance | **Easy:** PhilRice Rice Technology Bulletin No. 44 protocol on palay; 2.5 × 10¹² spores per preparation; rice substrate standard worldwide | [R34] HIGH; [R11] HIGH |
| Local sources | NCPC-UPLB holds PH isolates from *S. exigua* (Nueva Ecija) and *S. frugiperda* (Quezon) | PhilRice, NCPC-UPLB (Dr. Dante Santiago group, corn-based method), BPI biocontrol labs mass-produce | [R1, R3]; [R11, R45] |
| Safety | Narrow host range (Lepidoptera) — very safe | US-EPA: "reasonable certainty of no harm" (strain F52); not harmful to honey bees; low toxicity to lady beetles, lacewings; "Caution" signal word | [R28] HIGH |
| Non-target natural enemies | — | Can infect parasitoids (*Telenomus remus* 81% mortality on direct contact with ICIPE 7) | [R40] HIGH. Point-source device exposes far fewer non-targets than spraying |

### 3.2 Verdict

⚠️ **CORRECTION: Recommend *M. anisopliae* for v1**, with the isolate sourced from PhilRice, NCPC-UPLB or BPI, and ideally a strain already used in Mindoro or against Lepidoptera.

Reasons:
1. Our device contaminates **adults**. The only adult-moth efficacy and horizontal-transmission data in our genus are for *M. anisopliae* [R4].
2. It can be **self-produced** with the PhilRice protocol an ABE team can run [R11]. *M. rileyi* cannot be produced reliably without research-level optimization [R34], and research is out of scope.
3. It has **local precedent** on harabas in San Jose [R15].
4. It hits three life stages: adults (die in ~4 days), eggs (isolate-dependent) and larvae.

**v2 option:** a mixed cartridge (*M. anisopliae* + *M. rileyi*) developed with NCPC-UPLB, who already hold a harabas-derived *M. rileyi* isolate. This is a partnership path, not our own research.

### 3.3 Environmental limits of *M. anisopliae*

| Factor | Finding | Implication | Source |
|---|---|---|---|
| Temperature | Optimum germination 26.4–28.1 °C; growth slows >30 °C, generally ceases ~35 °C; germination impaired at 38–40 °C; tropical isolates more heat-tolerant | Mindoro dry-season nights (~22–26 °C) are near ideal. **Daytime heat inside the device** is the risk: use a white, ventilated, shaded housing | [R27] HIGH |
| UV / sunlight | UV-B LT50 = 4 h 26 min at 1,200 mW/m²; 4 h full sunlight killed 100% of conidia of 2 of 3 strains | Interior must be **fully opaque**; the spore surface must never see direct sun | [R25] HIGH |
| Humidity | FT83 on harabas larvae: **86.7% mortality at 85% RH vs 13.4% at 45% RH** | Infection needs humidity. Moths contaminated at night and resting in the crop canopy are likely in high RH, but **verify with a cheap humidity logger in San Jose fields** | [R10] HIGH |
| Storage | ~25 °C: **72.5% viable at 135 d; 28.5% at 176 d**; very dry conidia (water activity <0.1) + desiccant can last months to >2 years; NCPC corn-based powder "viable >1 year" in freezer | Produce **per season**; pack cartridges in sealed foil + silica gel; store cool | [R26, R45] HIGH/MED |
| Viability inside device | Semi-field: ≥86% viability after **12 days** (thrips device); linear decline over 8 days in whitefly device | **Swap spore cartridge every ~14 days** (verify with a germination test) | [R5, R6] HIGH |

---

## 4. AUTODISSEMINATION — Does It Work, and How Are Devices Built?

### 4.1 Evidence ladder (honest assessment)

| Level | Pest | Result | Source |
|---|---|---|---|
| Lab | FAW (*S. frugiperda*) | 100% moth mortality; transmission to untreated moths; lower oviposition and hatch; lure compatible | [R4] |
| Lab | *Spoladea recurvalis* (moth) | Donor to recipient transmission, 76.9% mortality (LT50 6.9 d); inoculated females infected 48% of untreated males | [R46] |
| Lab | Diamondback moth | Horizontal transmission of entomopathogenic fungi demonstrated | [R9] |
| Large field cage | Diamondback moth | Released inoculated adults started fungal epizootics in larvae; "proof of concept for auto-dissemination" | [R8] |
| Semi-field | Whitefly | 62.8% mortality (ICIPE 18) vs 18.9% control; 3 g dry conidia on velvet | [R6] |
| Field | Bean flower thrips | Device + lure; conidia acquisition correlated with attraction; ≥86% viability at 12 d | [R5] |
| **Multi-location field** | **False codling moth (citrus, Kenya)** | Pheromone compatible; field efficacy trial of *M. anisopliae* ICIPE 69 in orchards | [R7] |
| Commercial analog | Codling moth (Exosex, Exosect UK) | Pheromone-powder "autoconfusion" device, about 5% market share in codling moth control in apples and pears. Proves **moths reliably pick up powder from a lure station at commercial scale** (powder carries pheromone, not fungus) | [R32] |
| Review (2026) | All EPF delivery strategies | Lure-based systems "exploit predictable pest behavior to improve inoculum targeting" but are "limited by labor, need for tailored system design" | [R38] |
| **Field, *S. exigua*** | — | **NOT FOUND. No published field trial of fungal autodissemination against *S. exigua*** | GAP |

**Honest bottom line for the panel:** the *components* are proven (lure attraction, fungal kill of harabas, moth-to-moth transmission in the same genus, device designs, commercial precedent for powder pickup at a lure). The *combination on harabas in a PH onion field* has not been published. That gap is our **business opportunity**, not a research question: we build the product from published components and run a field **demonstration** (§10). We don't run a hypothesis experiment.

### 4.2 Published device designs (what we copy)

| Design | Dimensions / materials | Spore load | Notes | Source |
|---|---|---|---|---|
| icipe thrips autoinoculation device | Lynfield trap 11 cm Ø × 10 cm; **six entry/exit holes 2 × 3 cm**; velvet 8 × 8.5 cm + netting around inner bottle 5.2 cm Ø × 6 cm | Dry conidia on velvet | Lure placed **outside** device, best at 10 cm below | [R5] |
| icipe whitefly device (after Toledo et al.) | Cylinder **12 cm long × 6 cm Ø**, velvet lined inside and outside with contact adhesive; lid 12.5 cm Ø on wire; **bottom open** | **3 g dry conidia**; netting lightly dusted; lid dusted | Hung 30 cm above canopy; "velvet offers good retention capacity of the spores" | [R6] |
| US Patent 5,359,807 | "Method and apparatus for autodissemination of insect pathogens" | — | 1990s patent, **expired**, so the basic concept is free to use (confirm with IPOPHL search) | [R42] |

**Design lessons for a noctuid moth** (harabas wingspan ~25–30 mm, far bigger than thrips or whitefly):
- Openings must be **≥4 cm**. Thrips-size 2 × 3 cm holes are too small.
- **No funnel and no kill agent.** Moths must leave freely.
- **Velvet-lined contact surfaces** (vanes or walls) that moths must touch while walking or fluttering toward the lure.
- The lure sits **above and away** from the velvet (≥10 cm), so the moth follows the plume *through* the dusted zone.
- The design follows the proven "bucket/unitrap" layout for noctuids, minus the collection bucket.

---

## 5. SPORE PRODUCTION (supply chain for the refill)

PhilRice Rice Technology Bulletin No. 44 (2002) [R11], a protocol written for technicians and farmers:
1. **Starter culture:** potato dextrose agar (PDA; 39 g/L), potato sucrose agar (PSA) or oatmeal agar slants; sterilize 121 °C / 15 psi / 15 min; streak with 1–2-week-old *Metarhizium*; incubate 1–2 weeks until green.
2. **Substrate:** 200 g palay + 200 mL water in a 9 × 16 polypropylene bag; PVC ring + cotton plug; sterilize 15 psi for **1 h**; cool.
3. **Inoculate:** add 5 mL sterile 0.05% soap solution to a slant, scrape the conidia, add 5 mL suspension per bag, mix, **incubate 1–2 weeks**.
4. **Yield and use:** "one preparation contains 2.5 trillion spores". PhilRice recommends 50 bags/ha for spraying (~1 × 10¹³ spores/ha).
5. **Equipment:** pressure cooker or autoclave, inoculating chamber or laminar flow hood, alcohol lamp, glassware. **All standard in an ABE or biology lab.**
6. **PhilRice offers technical assistance** for isolation and mass production.

icipe's industrial version of the same method [R6]: 2 kg rice per Milner bag, autoclaved 1 h at 121 °C, inoculated with a 3-day liquid (blastospore) culture, incubated **21 days at 26 °C, 40–70% RH**, dried 5 days, conidia harvested mechanically.

⚠️ **UNVERIFIED FIGURE.** "₱17.59/bag" in earlier notes: we could not find this number in Bulletin No. 44 or on PhilRice's site. Treat the cost per bag as **our estimate** until a PhilRice or NCPC quote is obtained. Our estimate is ₱15–25/bag in materials (200 g palay at ~₱30–40/kg is ₱6–8, plus bag, cotton, ring and fuel for sterilization).

**Harvesting dry conidia for cartridges.** The device needs **dry powder**, not the liquid suspension PhilRice uses for spraying:
- Sieve or shake the dried, sporulated rice through fine mesh, the method icipe uses.
- Then dry to low moisture with silica gel before packing [R26].

This is a **production step, not research**. It's standard practice in every autodissemination study cited.

---

## 6. REGULATORY LANDSCAPE

| Item | Finding | Implication | Source |
|---|---|---|---|
| Law | PD 1144 created the FPA. No pesticide may be "imported, manufactured, formulated, repacked, distributed, delivered, sold or offered for sale … unless duly registered … or covered by a numbered provisional permit" | **The spore cartridge counts as a pesticide product** once sold | [R29] HIGH |
| Biorationals | Microbial agents (bacteria, fungi, viruses, protozoa) are "biorational pesticides" with **reduced data requirements** | Registration is lighter than for chemicals, but still needed | [R29] HIGH |
| Experimental Use Permit | FPA Pesticide Regulatory Policies & Implementing Guidelines (3rd ed., 2020) include EUP provisions | Pilot field demos should run under an EUP, or under a DA-RCPC / LGU / university partnership | [R29] MEDIUM |
| Pheromone lures | Sold commercially in PH (Verca → DA-RFO III) | Lure supply is already legal through distributors; confirm registration status of the chosen lure | [R22] MEDIUM |
| Device (hardware) | A trap body with no active ingredient is not a pesticide | We can sell the **Station hardware** freely | Our reading of PD 1144. Confirm with FPA |
| Intellectual property | Utility Model filing ₱1,737.20 for a small entity (+1% LRF) | Protect our specific design (vanes, cartridge sleeve, hood); the concept itself is prior art | [R30] HIGH |

**Three regulatory pathways** (detail in `proposal.md` §9):
- **Path A, pilot:** run the demo under an EUP or DA-RCPC/LGU partnership. The government lab supplies or approves the spores, and we supply the Station.
- **Path B, first sales:** sell the Station and lure; the cartridge is filled with an **FPA-registered *M. anisopliae* product**, bought or licensed.
- **Path C, scale:** register our own *M. anisopliae* dry-conidia cartridge as a biorational.

---

## 7. COMPETITION AND SUBSTITUTES

| Alternative | Cost signal | Strength | Weakness vs the Station |
|---|---|---|---|
| Chemical insecticides (chlorantraniliprole, emamectin, etc.) | Prevathon 400–500 mL/ha per application [R47]; outbreak input costs ≈ ₱400k/ha [R21] | Fast knockdown | Resistance [R43]; repeated cost; residues; health |
| Plain pheromone trap (monitoring) | DA-procured; lure ~₱17–215 each | Familiar, cheap | Tells you when; **doesn't reduce the population** |
| Mass trapping (kill traps) | FAW: 40–50 traps/ha [R23b] | Removes males | Needs many traps; males mate with ~5 females each, so every missed male still mates |
| Metarhizium / Beauveria spray | PhilRice ₱250/ha (rice, 2002) [R11] | Cheap, safe | UV kills spores in hours; repeated labor; timing |
| Bt and NPV products | — | Selective | Must be sprayed; UV; availability |
| **Commercial autodissemination for moths** | **None found for fungal pathogens.** Exosex is autoconfusion (pheromone powder), UK/EU only | — | **Gap = our position** |

**Our differentiator in one line:** the Station turns the pheromone trap that farmers already know from a *warning light* into a *treatment* that works while they sleep. It uses spores only a few grams at a time, protected from sunlight, and moths carry them to the next generation.

---

## 8. FUNDING AND SUPPORT ECOSYSTEM

| Program | Amount | Fit | Source |
|---|---|---|---|
| DOST-PCAARRD Startup Grant Fund (2026 call) | Up to ₱5 M over 1 year | Needs a startup operating 1–5 years. **Later-stage fit** | [R31] HIGH |
| DOST-TAPI TECHNiCOM | Up to ₱5 M (raised 2025); open to academic institutions | **Strong fit** through MinSU as proponent | [R31] HIGH |
| CHED-DOST Agri-Aqua Technology Business Incubator (ATBI) | ₱5 M per project; SUCs with ATBIs | Check whether MinSU has an ATBI | [R31] HIGH |
| DA procurement (B2G) | Precedent: ₱301k pheromone trap order (RFO III) | **First customer** channel | [R22] HIGH |
| IPOPHL Utility Model | ₱1,737.20 filing (small entity) | Low-cost IP | [R30] HIGH |

---

## 9. ASSUMPTIONS WE MUST TEST (not research — product validation)

| # | Assumption | Risk if wrong | Cheapest test |
|---|---|---|---|
| A1 | Harabas males enter the Station and touch the velvet (not just circle the lure) | Fatal | Night observation with a red-light headlamp; count dusted moths caught 5–10 m away with a sweep net or a second plain trap |
| A2 | Contaminated males carry enough spores to infect | High | Tap-test captured moths on PDA, or a spore wash + hemocytometer count at a partner lab |
| A3 | Spores stay viable ≥14 days in the Station in San Jose heat | Medium | Germination test of cartridge swabs at day 0/7/14/21 |
| A4 | Night humidity in onion canopy ≥80% | Medium | ₱500 USB temperature/RH logger in the field for 2 weeks |
| A5 | Farmers will pay ₱690/Station + ₱520/season kit | High | 20+ interviews with the price ladder (`phase6-validation-plan.md`) |
| A6 | LGU/DA would procure | Medium | 2 meetings: San Jose MAO, DA-MIMAROPA RCPC |
| A7 | We can obtain a starter culture and legal cover (EUP / partnership) | High | Letters to PhilRice, NCPC-UPLB, FPA Region IV-B |
| A8 | Lure from supplier X attracts Mindoro harabas | Medium | 2 lures side by side, 2 weeks, simple trap counts |

---

## 10. GAPS AND OPEN QUESTIONS

1. **No published field trial of fungal autodissemination against *S. exigua*** (§4.1). Frame it as the market gap, and demonstrate rather than research.
2. **No PH-specific pheromone blend** (§1.2). Buy two brands and compare.
3. **Station density per hectare** for autodissemination is unknown. Mass trapping uses 40–50/ha and monitoring 8–10/ha for FAW [R23b]. Mosquito autodissemination (In2Care) shows **density matters**: only the highest density (~555 stations/km²) had an effect [R48]. v1 recommendation: **4 Stations/ha** (one per 0.25 ha, ~50 m apart). The demo compares 2 vs 4/ha if resources allow.
4. **Spore load per cartridge.** Whitefly device used 3 g [R6]. We assume **2 g per cartridge**, to validate against the germination and tap tests.
5. **Registration status** of any *M. anisopliae* product in the PH market. FPA's registered-product list must be checked directly.
6. **OMSC 2024 full paper** (site down during research). Obtain a PDF and extract mortality numbers, source of the liquid *M. anisopliae*, and cost.
7. **"₱17.59/bag"** production cost. Unverified; get a quote.

---

## 11. WHAT CHANGED VS OUR EARLIER NOTES (for CLAUDE.md / memory)

| Earlier note | Updated position | Why |
|---|---|---|
| *M. rileyi* preferred | ***M. anisopliae* for v1**; *M. rileyi* v2 via NCPC | Adult-moth evidence, production, local data (§3) |
| 5 cm separation "required" | Design uses ≥10 cm as **precaution**; moth pheromones showed no inhibition | [R4, R5, R6, R7] |
| Shelf life 6–10 months ambient | **~4 months at 25 °C** unless dried + desiccant + sealed or cold; produce per season | [R26] |
| "Spores degrade in 4 h of sun" | Correct in magnitude (UV-B LT50 ≈ 4.4 h; 4 h sun killed 100% of some strains) | [R25] |
| ₱17.59/bag spore cost | Unverified; use ₱15–25 estimate | §5 |
| San Jose, *Oriental* Mindoro | San Jose, **Occidental** Mindoro (team at MinSU Victoria, Oriental) | Geography |
| Nueva Ecija 2,300+ ha | ~10,000–13,000 ha (2,319 ha is Bongabon red shallot only) | [R36, R16b] |
| "100% mortality" | True for **larvae** in the lab (*M. rileyi* 10⁷–10⁸ [R1]; FT83 [R10]); field and adult effects are smaller and slower. **Never claim 100% field control** | Honesty with the panel |

---

## 12. REFERENCES

**Biocontrol agent, harabas**
- **[R1]** Montecalvo, M.P. & Navasero, M.M. (2020). Effect of entomopathogenic fungus *Metarhizium (Nomuraea) rileyi* (Farl.) Samson on the third instar larvae of the onion armyworm, *Spodoptera exigua* Hübner, under laboratory conditions. *Philippine Agricultural Scientist*, 103(2), 140–145. https://www.ukdr.uplb.edu.ph/journal-articles/291/
- **[R2]** Montecalvo, M.P. & Navasero, M.M. (2021). *Metarhizium (=Nomuraea) rileyi* from *Spodoptera exigua* cross infects fall armyworm, *Spodoptera frugiperda* larvae. *Philippine Journal of Science*, 150, 193–199. https://philjournalsci.dost.gov.ph/
- **[R3]** Montecalvo, M.P., Navasero, M.M. & Navasero, M.V. (2022). Lethal effect of native *Metarhizium rileyi* isolate to invasive fall armyworm, *Spodoptera frugiperda*, infesting corn in the Philippines. *International Journal of Agricultural Technology*, 18(1), 257–270. http://www.ijat-aatsea.com/
- **[R10]** Han, J.H., Jin, B.R., Kim, J.J. & Lee, S.Y. (2014). Virulence of entomopathogenic fungi *Metarhizium anisopliae* and *Paecilomyces fumosoroseus* for the microbial control of *Spodoptera exigua*. *Mycobiology*, 42(4), 385–390. https://doi.org/10.5941/MYCO.2014.42.4.385
- **[R15]** Occidental Mindoro State College (2024). Effectiveness of various concentrations of liquid *Metarhizium anisopliae* against armyworm (*Spodoptera exigua*) 'harabas' in onion 'Red Pinoy' variety. *Aka Student Research Journal*. Brgy. Bayotbot, San Jose, Occ. Mindoro, Dec 2022–Mar 2023. https://journal.omsc.edu.ph/index.php/aka-journal/article/view/53
- **[R34]** Performance of *Metarhizium rileyi* Nm017: nutritional supplementation to improve production and quality conidia (2024). *3 Biotech*. https://doi.org/10.1007/s13205-023-03911-6
- **[R39]** Akutse, K.S., Kimemia, J.W., Ekesi, S., Khamis, F.M., Ombura, O.L. & Subramanian, S. (2019). Ovicidal effects of entomopathogenic fungal isolates on the invasive fall armyworm *Spodoptera frugiperda*. *Journal of Applied Entomology*, 143, 626–634.
- **[R40]** Chepkemoi, J., Fening, K.O., Ambele, F.C., Munywoki, J. & Akutse, K.S. (2024). Effects of four potent entomopathogenic fungal isolates on the survival and performance of *Telenomus remus*. *Frontiers in Cellular and Infection Microbiology*, 14, 1445156. https://doi.org/10.3389/fcimb.2024.1445156

**Autodissemination**
- **[R4]** Akutse, K.S., Khamis, F.M., Ambele, F.C., Kimemia, J.W., Ekesi, S. & Subramanian, S. (2020). Combining insect pathogenic fungi and a pheromone trap for sustainable management of the fall armyworm, *Spodoptera frugiperda*. *Journal of Invertebrate Pathology*, 177, 107477. https://doi.org/10.1016/j.jip.2020.107477
- **[R5]** Mfuti, D.K., Subramanian, S., van Tol, R.W.H.M., Wiegers, G.L., de Kogel, W.J., Niassy, S., du Plessis, H., Ekesi, S. & Maniania, N.K. (2016). Spatial separation of semiochemical Lurem-TR and entomopathogenic fungi to enhance their compatibility and infectivity in an autoinoculation system for thrips management. *Pest Management Science*, 72, 131–139. https://doi.org/10.1002/ps.3979
- **[R6]** Paradza, V.M., Khamis, F.M., Yusuf, A.A., Subramanian, S. & Akutse, K.S. (2022). Efficacy of *Metarhizium anisopliae* and (E)-2-hexenal combination using autodissemination technology for the management of the adult greenhouse whitefly. *Frontiers in Insect Science*, 2, 991336. https://doi.org/10.3389/finsc.2022.991336
- **[R7]** Mkiga, A.M. et al. (2020). Compatibility and efficacy of *Metarhizium anisopliae* and sex pheromone for controlling *Thaumatotibia leucotreta*. *Journal of Pest Science*. https://doi.org/10.1007/s10340-020-01281-z
- **[R8]** Vickers, R.A. et al. (2004). Initiation of fungal epizootics in diamondback moth populations within a large field cage: proof of concept for auto-dissemination. *Entomologia Experimentalis et Applicata*. https://onlinelibrary.wiley.com/doi/abs/10.1111/j.0013-8703.2004.00140.x
- **[R9]** Furlong, M.J. & Pell, J.K. (2001). Horizontal transmission of entomopathogenic fungi by the diamondback moth. *Biological Control*.
- **[R32]** Exosect Ltd — Exosex autoconfusion / Entostat electrostatic powder (UK REF Impact Case Study). https://impact.ref.ac.uk/casestudies/CaseStudy.aspx?Id=42990
- **[R38]** Beltrán-Martí, R., Garcerá, C., Garrido-Jurado, I. & Chueca, P. (2026). Delivery strategies for entomopathogenic fungi in crop pest management: a review. *Pest Management Science*, 82, 9401–9413. https://doi.org/10.1002/ps.71080
- **[R42]** US Patent 5,359,807. Method and apparatus for autodissemination of insect pathogens. (Expired.)
- **[R46]** Horizontal transmission of *Metarhizium anisopliae* between *Spoladea recurvalis* adults and compatibility with phenylacetaldehyde. *Microbial Pathogenesis*. https://www.sciencedirect.com/science/article/abs/pii/S0882401018319405
- **[R48]** Tristão, W. et al. (2025). What is the optimal In2Care stations density to achieve *Aedes aegypti* population reduction? *PLoS NTD*, 19, e0013264.

**Pheromone and trapping**
- **[R13]** Arida, G.S., Punzal, B.S., Ravina, C.C., Gapud, V.P., Rajotte, E.G. & Talekar, N.S. (2003). Monitoring adult *Spodoptera* populations with sex pheromone traps for effective timing of interventions against insect defoliators affecting onion. *Philippine Entomologist*, 17(2), 192. https://www.ukdr.uplb.edu.ph/journal-articles/5749/
- **[R14]** Arida, G.S., Punzal, B.S., Duca, A.A. & Rajotte, E.G. (2004). Management of *Spodoptera litura* and *S. exigua* on onion by mass trapping of the moths and timing of interventions in farmers' fields. *Philippine Entomologist*, 18(2), 173–174. https://www.ukdr.uplb.edu.ph/journal-articles/5623/
- **[R23]** Lure suppliers: Evergreen Growers Supply (US$3.70/lure; 4-week field life; freezer 2 yrs) https://www.evergreengrowers.com/beet-armyworm-lure.html · Koppert Pherodis *S. exigua* (6 weeks) · Innovac Bioscience via IndiaMART (₹25/lure) https://m.indiamart.com/proddetail/pheromone-lure-for-beet-armyworm-spodoptera-exigua-21728288262.html · Russell IPM PH-869-1PR
- **[R23b]** Harmony Ecotech — *S. frugiperda* lure guidance (40–50 traps/ha mass trapping; 8–10/ha monitoring). https://harmonyecotech.com/pheromone-lures/spodoptera-frugiperda/
- **[R24]** Two sympatric *Spodoptera* species could mutually recognize sex pheromone components for behavioral isolation (2019). *Frontiers in Physiology*, 10, 1256 (7:3:1 blend in East Asia) https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2019.01256/full; Optimal sex pheromone composition for monitoring *S. exigua* in Korea, *Journal of Asia-Pacific Entomology* (2008).
- **[R33]** Animal Diversity Web — *Spodoptera exigua* (mating frequency, scotophase activity). https://animaldiversity.org/accounts/Spodoptera_exigua/

**Outbreaks, market, farmers**
- **[R12]** Navasero, M.V., Navasero, M.M., Cayabyab, B. et al. (2017). Investigation on the 2016 outbreak of the onion armyworm, *Spodoptera exigua*, in onion growing areas in Nueva Ecija. *Philippine Entomologist*, 31(2), 151–152. https://www.ukdr.uplb.edu.ph/journal-articles/4066/
- **[R12b]** Public-private partnership in managing onion armyworm outbreak in Nueva Ecija (ResearchGate). https://www.researchgate.net/publication/318054164
- **[R16]** PNA (2024-05-09). DA: Interventions in place vs. armyworm infestation in onion farms. https://www.pna.gov.ph/articles/1224372 · BPI Oct 2025 Central Luzon pheromone trap installation (Pwersa Balita). **[R16b]** Manila Bulletin (2024-03-15). https://mb.com.ph/2024/3/15/onion-price-down-by-p20-kilo-despite-armyworm-infestation-da
- **[R17]** PNA (2024-03-18). Prov'l council wants Occidental Mindoro placed under state of calamity. https://www.pna.gov.ph/articles/1221060
- **[R18]** BusinessWorld (2026-03-30). FTI seeking buyer support for Mindoro onion growers. https://www.bworldonline.com/economy/2026/03/30/739905/fti-seeking-buyer-support-for-mindoro-onion-growers/
- **[R19]** NIA Region IV-B. Onion production in Occidental Mindoro. https://region4b.nia.gov.ph/content/onion-production-occidental-mindoro
- **[R20]** Daily Tribune (2026-02-23) https://tribune.net.ph/2026/02/23/da-boosts-assistance-for-onion-farmers-in-occidental-mindoro · Manila Times (2026-02-24). **[R20b]** PIA (2024-01-25). Mindoro agri office expects increase in onion yield. https://pia.gov.ph/news/2024/01/25/mindoro-agri-office-expects-increase-in-onion-yield-this-harvest-season
- **[R21]** Rappler. High stakes: Why Pangasinan town's onion farmers carry on despite pests, low prices. https://www.rappler.com/business/why-onion-farmers-bayambang-pangasinan-carry-on-despite-challenges/ · **[R21a]** Eco-Business. Lives destroyed as armyworms invade Philippine 'onion capital'. https://www.eco-business.com/news/lives-destroyed-as-armyworms-invade-philippine-onion-capital/ · **[R21b]** IJELS. Strategies of onion farmers in dealing with the effects of army worms. https://ijels.com/detail/strategies-of-onion-farmers-in-dealing-with-the-effects-of-army-worms-in-their-crops/ · **[R21c]** PDI (2018-03-23). Onion-growing city loses P261M to armyworms.
- **[R22]** DA-RFO III (2020-12-24). Award of contract: Supply and delivery of sex pheromone trap (*Spodoptera exigua*), ₱301,000, Verca Agro Chem Inc. https://rfo3.da.gov.ph/
- **[R36]** PNA. Nueva Ecija onion farmers seek gov't help amid low prices (21,086 farmers; 11,502.84 ha). https://www.pna.gov.ph/articles/1065234
- **[R37]** PCAARRD ISP (2024). Onion production surge. https://ispweb.pcaarrd.dost.gov.ph/
- **[R43]** Monitoring and mechanisms of insecticide resistance in *Spodoptera exigua*, with special reference to diamides (2021). *Pesticide Biochemistry and Physiology*. https://www.sciencedirect.com/science/article/abs/pii/S0048357521000626
- **[R44]** Manila Times (2026-02-24). DA strictly monitoring onion prices in Occidental Mindoro. https://www.manilatimes.net/2026/02/24/business/top-business/da-strictly-monitoring-onion-prices-in-occidental-mindoro/2283110
- **[R47]** FMC Philippines — Prevathon 5SC product page. https://ag.fmc.com/ph/en/products/insecticides/prevathon-5sc-insect-control

**Spore production, stability, safety**
- **[R11]** PhilRice (2002). *Metarhizium: Microbial control agent for rice black bug*. Rice Technology Bulletin No. 44. ISSN 0117-9799. https://www.pinoyrice.com/wp-content/uploads/metarhizium.pdf
- **[R25]** Braga, G.U.L. et al. (2001). Effects of UVB irradiance on conidia and germinants of *Metarhizium anisopliae*. *Photochemistry and Photobiology*, 73, 140; Both solar UVA and UVB radiation impair conidial culturability… (PubMed 11723803).
- **[R26]** Viability of *Metarhizium anisopliae* conidia preserved in packages containing silica gel (2014). *BMC Proceedings*, 8(Suppl 4), P128. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4210827/
- **[R27]** UV-B radiation tolerance and temperature-dependent activity within the genus *Metarhizium* in Brazil (2021). *Frontiers in Fungal Biology*; Suitable models to describe the effect of temperature on conidial germination… *Biocontrol Science and Technology* (2021).
- **[R28]** US-EPA. *Metarhizium anisopliae* strain F52 Biopesticide Fact Sheet; Zimmermann, G. (2007). Review on safety of the entomopathogenic fungus *Metarhizium anisopliae*. *Biocontrol Science and Technology*, 17(9).
- **[R45]** Business Diary PH. Metarhizium: The mighty fungus (NCPC-UPLB, Dr. Dante Santiago; corn-based production; >1 year viability). https://businessdiary.com.ph/11746/metarhizium-mighty-fungus/

**Regulation, IP, funding**
- **[R29]** Presidential Decree No. 1144 (FPA); FPA Guidelines on Biorational Pesticides; FPA Pesticide Regulatory Policies and Implementing Guidelines, 3rd ed. (2020); CIRS Group summary. https://fpa.da.gov.ph/ · https://www.cirs-group.com/en/agrochemicals/pesticide-regulation-pesticide-registration-in-the-philippines
- **[R30]** IPOPHL. Utility Model & Industrial Design schedule of fees. https://www.ipophil.gov.ph/services/schedule-of-fees/utility-model-industrial-design/
- **[R31]** DOST-PCAARRD 2026 Startup Grant Fund call; DOST-TAPI 2025 TECHNiCOM (₱5 M ceiling); CHED-DOST ATBI. https://www.pcaarrd.dost.gov.ph/ · http://www.tapi.dost.gov.ph/

*Currency conversions used across the repo: US$1 ≈ ₱58; ₹1 ≈ ₱0.68 (assumption, Sept 2026 — update before presenting).*
