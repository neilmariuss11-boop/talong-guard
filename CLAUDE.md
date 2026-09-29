# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A **technopreneurship project** (NOT a thesis) by 4th-year ABE students at **Mindoro State University (MinSU) Main Campus, Victoria, Oriental Mindoro**. The **field site and first market are San Jose, Occidental Mindoro**. San Jose is in *Occidental*, not Oriental, Mindoro. Don't mix them up.

The product is an **autodissemination station for onion armyworm (harabas, *Spodoptera exigua*)**. A pheromone lure draws male moths through a shaded velvet tube dusted with *Metarhizium anisopliae* spores, and they leave alive to infect mates, eggs and larvae. The old name "TalongGuard" (eggplant) is retired. The brand is **Pherospora** (decided 2026-09-29, `proposal.md` §12; logo in `assets/logo/`). Older docs still say "the Station" or "[BRAND]"; the trademark search at IPOPHL is still open.

**Key constraint:** product/device project, not scientific research. The biology is cited from published literature. The deliverables are a physical device, BOM and business model. Field work is framed as **product validation / demonstration**, never hypothesis research.

## Repository Structure

Documentation-only (Markdown). No code, build system or tests.

**Current (autodissemination direction, rewritten 2026-09-27):**
- `proposal.md`: **master technopreneurship proposal** (exec summary, product, market, business model, FPA pathway, financial summary, naming, risks, timeline, 18-question panel Q&A)
- `research-synthesis.md`: **evidence base**. 48 numbered references [R1–R48], confidence grades, and a list of corrections to earlier assumptions. Every other doc cites [R#] from here.
- `phase3-harabas-deepdive.md`: pest, personas, competition, MVP, lean canvas, riskiest assumptions
- `phase4-pitch-deck.md`: 15 slides + references slide, with speaker notes
- `phase5-device-design.md`: engineering (requirements, concept matrix, dimensions, sun-angle calculation, BOM, fabrication SOP, spore/cartridge SOP, QC tests, Tagalog farmer card)
- `phase6-validation-plan.md`: Tagalog interview scripts, LGU guide, bench tests, field demo design, forms A–D, pass/kill criteria
- `phase7-financial-model.md`: unit economics, Year-1 monthly cash plan, 3-year P&L, break-even, sensitivity, assumptions
- `phase8-onion-pivot.md`: decision history (eggplant → onion monitoring → autodissemination)
- `Business-Plan.md`: formal long-form business plan
- `loop-roadmap.md`: phase tracker and next actions
- `venture-board-description.md`: two-page project description for the venture board, drawn from `proposal.md`

**Historical (eggplant era, kept for reference):** `proposal-v2-problem.md`, `idea-pool.md`, `idea-pool-v2.md`, `phase2-scoring.md`. The old eggplant versions of phases 3–7 and the business plan are in git history.

## Current Product Direction

### Concept
- 40 cm white hood with lure cage.
- 80 mm open entry window with cross baffle vanes.
- 4-inch PVC tube (200 mm): 50 mm plain "sun collar", then a 150 mm removable velvet spore sleeve (2 g dry *M. anisopliae* conidia).
- Open bottom; moths exit alive.
- Pole-mounted; tube bottom about 600 mm above soil.
- No power.
- Sleeve swapped every 14 days, lure every 4 weeks.
- 4 Stations/ha (starting assumption).

### Key technical parameters (evidence-checked 2026-09-27)
- **Target:** *Spodoptera exigua* males. Pheromone: Z9,E12-14:OAc + Z9-14:OH (± Z11-16:OAc); 7:3:1 best in East Asia. Buy commercial rubber-septum lures; don't formulate our own.
- **Biocontrol agent: *M. anisopliae* for v1** (adult-moth kill and moth-to-moth transmission in *Spodoptera* [Akutse 2020]; PhilRice rice protocol; OMSC San Jose harabas data). *M. rileyi* is **v2** with NCPC-UPLB: great on larvae, but no adult-moth evidence, hard to mass-produce, not ovicidal.
- **Lure–spore separation:** ≥21 cm by design. The "5 cm" figure came from a whitefly plant volatile and the 10 cm figure from a thrips lure. **Moth sex pheromones showed no inhibition** (FAW, FCM). It's a precaution, not a proven requirement.
- **UV:** UV-B LT50 ≈ 4.4 h, so the interior must be opaque. The hood geometry allows direct sun on the velvet only at sun elevation <29°.
- **Shelf life:** ~72% viable at 135 d and ~28% at 176 d at 25 °C, so **produce per season**, seal with silica, refrigerate. The old "6–10 months ambient" claim was wrong.
- **Humidity risk:** FT83 larval kill was 86.7% at 85% RH vs 13.4% at 45% RH. Measure night canopy RH.
- **Moth behavior:** nocturnal; mates in the second half of the night; males mate ~5×; trap peaks 25–59 days after planting in PH onion.

### Supply chain
- **Spores:** self-produced with PhilRice Rice Technology Bulletin No. 44 (200 g palay/bag, 1 h sterilization, 1–2 weeks incubation) + dry-conidia harvest. Starter culture from PhilRice, NCPC-UPLB or BPI. The "₱17.59/bag" figure is **unverified**; estimate ₱15–25.
- **Lures:** India (₹25 list), PH distributor (Verca Agro Chem supplied DA-RFO III), US/EU backup (Evergreen US$3.70). **Landed lure cost ≤₱60 is the #1 financial driver.**
- **Body:** PP basin, 4-inch PVC, coroplast, GI rod, velvet, hose clamps, bamboo pole.

### Business model
- Station ₱690 (COGS ₱285) + Season Kit ₱520 per Station (3 lures + 6 cartridges; COGS ₱330).
- Farmer cost: ₱4,840/ha in the first season, then ₱2,080/ha (~0.8% of onion gross).
- First customers: LGU/DA programs (B2G; precedent ₱301k DA-RFO III pheromone trap order), irrigators' associations, commercial growers.
- **Regulatory:** the spore cartridge is a microbial pesticide under PD 1144 (FPA). Stage A demo with no cartridge sales (EUP/partner) → Stage B registered source or government program → Stage C own biorational registration. The hardware is not a pesticide.
- Financials (base): Y1 −₱170,100 (hardware-only sales); Y2 −₱47,800; Y3 +₱393,360; ask ₱180,000.

### Market figures (verified)
- Occidental Mindoro onion: **8,637 ha (2026)**, up from 6,000 ha (2025). San Jose ~3,285 ha (2023, verify with MAO).
- Nueva Ecija ~10,000–13,000 ha (not "2,300+", which is Bongabon red shallot only).
- 2016 NE outbreak ₱1.61 B; 2024 national 12,138 ha infested; 2024 Occidental Mindoro ₱30 M armyworm damage.

## Important Context
- The panel approved the pheromone concept and directed the pivot from eggplant to onion.
- The user is an ABE student. Device fabrication is within their skillset.
- The user explicitly rejected pure automation/monitoring traps, bundled two-product approaches, and anything requiring scientific research.
- Team size and budget are undecided (Sept 2026). Docs assume 3 members as a placeholder.
- When adding facts, add the source to `research-synthesis.md` §12 and cite it as [R#]. Keep the confidence grades honest, and never claim "100% field control".
