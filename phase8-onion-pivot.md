# Phase 8: Onion Pivot and the Autodissemination Decision
**Original: 2026-09-15 (panel feedback response) | Rewritten: 2026-09-27**

> This file records **how and why the direction changed**:
> eggplant monitoring trap → onion monitoring trap → **onion autodissemination station**.
> The current plan is in `proposal.md`, and the evidence is in `research-synthesis.md`.

---

## 1. DECISION HISTORY

| Date | Decision | Why |
|---|---|---|
| Early Sept 2026 | **TalongGuard**: ESP32 smart pheromone trap for eggplant fruit and shoot borer, with SMS threshold alerts | Ideation phases 1–2 (`idea-pool*.md`, `phase2-scoring.md`) |
| 2026-09-15 | **Panel:** approve the pheromone concept; **pivot crop from eggplant to onion** (higher national urgency) | Onion crisis 2022–23; harabas outbreaks [R12, R16] |
| Mid-Sept 2026 | Team **rejects pure monitoring/automation**, bundled two-product ideas, and anything requiring scientific research | Monitoring doesn't reduce pests; research is out of scope for technopreneurship |
| 2026-09-16 | **Direction: autodissemination.** A pheromone lure draws male moths, which get dusted with *Metarhizium* spores and leave alive to infect mates | Turns the proven lure into an intervention (`CLAUDE.md`) |
| 2026-09-27 | Full research synthesis. **Fungus: *M. anisopliae* for v1** (*M. rileyi* moved to v2). Field site: **San Jose, Occidental Mindoro** | Adult-moth evidence and producibility (`research-synthesis.md` §3); location correction |

---

## 2. WHY ONION (still valid from the original Phase 8)

- **National urgency:** the 2022–23 onion price crisis (retail up to ~₱700/kg), imports, congressional hearings, and a government push for self-sufficiency.
- **Harabas is the top onion pest:**
  - 2016 Nueva Ecija: ₱1.61 B lost [R12].
  - 2024: 12,138 ha infested nationally [R16].
  - 2024 Occidental Mindoro: ₱30 M, state of calamity in San Jose, Magsaysay and Looc [R17].
- **Our area is growing:** Occidental Mindoro onion went from 6,000 ha (2025) to **8,637 ha (2026)** [R18]; San Jose alone ~3,285 ha [R19].
- **Higher crop value** than eggplant per hectare, and farmers remember outbreak losses, so they're more willing to invest in prevention.

⚠️ **Correction to the original Phase 8.** It said "Oriental Mindoro, including San Jose". **San Jose is in Occidental Mindoro.** The team is based at MinSU Main Campus, Victoria, Oriental Mindoro. The field site and first market are in San Jose, Occidental Mindoro.

---

## 3. WHY WE DROPPED THE MONITORING TRAP (ESP32 + SMS)

| Monitoring trap (old) | Autodissemination Station (new) |
|---|---|
| Counts moths; the farmer still has to spray | **Reduces** the pest: moths carry the fungus to mates, eggs and larvae [R4] |
| Electronics: ESP32, GSM, solar, battery; failure-prone in the field | **Passive**: no power, no connectivity |
| Needs a local economic threshold (ETL). No PH value for harabas on onion, so establishing one would be *research* | No threshold needed; runs all season |
| Competes with free DA traps | **Upgrades** the DA trap concept into an intervention |
| Value depends on the farmer acting on alerts | Value delivered automatically |
| ~₱3,000 device | ~₱690 device + ₱520/season kit |

The original Phase 8 "why no camera" argument (the pheromone is the species filter) still holds. In the new design, **the pheromone specificity also protects non-target insects**, because few non-target species enter the Station [R28, R40].

---

## 4. WHAT CARRIED OVER
- **Target pest and pheromone:** *S. exigua*; Z9,E12-14:OAc + Z9-14:OH (± Z11-16:OAc), 7:3:1 optimal in East Asia [R24].
- **Pheromone supply chain:** commercial rubber-septum lures (India, a PH distributor such as Verca Agro Chem, US/EU backup) [R22, R23]. We **don't** formulate our own lures.
- **Razor-and-blade model:** device plus recurring refills.
- **Customer insight:** farmers and LGUs already know pheromone traps [R13, R14, R16, R22].

---

## 5. WHAT CHANGED

| Element | Onion monitoring (15 Sept) | **Onion autodissemination (now)** |
|---|---|---|
| Product | ESP32 IR-count trap + SMS | Passive hood + baffle + velvet spore tube |
| Active agent | None | *Metarhizium anisopliae* dry conidia (2 g/cartridge) |
| Refill | Lure | Lure (4-weekly) + spore sleeve (2-weekly) |
| Regulatory | None | **FPA**: the spore cartridge is a microbial pesticide [R29]; staged pathway |
| Novelty | Cheap automated counting | First autodissemination product for harabas; noctuid-scale device; local spore supply chain |
| Key partners | Lure suppliers | + PhilRice / NCPC-UPLB (spores), LGU/DA (demo, buyer) |
| Main risk | Farmers ignoring alerts | Spore pickup in the device; FPA pathway; lure cost |

---

## 6. SPECIES-SPECIFICITY ANSWER (updated panel Q&A)

> **Panel:** "How can you be sure only harabas is affected?"

1. **The pheromone is the filter.** Sex pheromones are species-specific by design; synthetic blends mostly catch the target species (Witzgall et al., 2010; Cork et al., 2003, cited in the original Phase 8).
2. **The fungus is delivered at one point, not broadcast.** Grams of spores per hectare inside a device, compared with a sprayed field.
3. ***M. anisopliae* safety:** US-EPA "reasonable certainty of no harm"; not harmful to honey bees; low toxicity to lady beetles and lacewings [R28].
4. **Honest caveat:** parasitoid wasps can be infected on direct contact [R40]. That's why the spores stay inside the tube, which parasitoids have no reason to enter.

---

## 7. NAMING
"TalongGuard" no longer fits. Options and a recommendation are in `proposal.md` §12. Recommended: **"Padala"** (the moth delivers the cure), with "SporaLure" as the technology or product-line name.

---

## 8. NEXT STEPS
The full timeline is in `proposal.md` §16. Highlights:
1. **Oct 2026:** letters to PhilRice / NCPC-UPLB (starter culture), FPA (EUP question), San Jose MAO; 2 lure quotes; 5 prototypes; bench test.
2. **Oct–Nov:** 20+ farmer interviews (`phase6-validation-plan.md`).
3. **Dec 2026 – Mar 2027:** field demonstration on 3–5 San Jose farms; field day.
4. **Apr 2027:** LGU proposal; pre-orders; TECHNiCOM application.
