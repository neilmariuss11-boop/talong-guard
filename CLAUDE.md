# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

TalongGuard is a **technopreneurship project** (NOT a thesis) by MinSU ABE students in San Jose, Oriental Mindoro, Philippines. The project has pivoted from eggplant borer monitoring to an **autodissemination device for onion armyworm (harabas / Spodoptera exigua)** — a pheromone-baited station that inoculates moths with Metarhizium fungal spores and releases them alive to spread the pathogen through the pest population.

**Key constraint:** This is a product/device project, not scientific research. The science is cited from published literature; the deliverable is a physical device, bill of materials, and business model.

## Repository Structure

This is a documentation-only repository — all files are Markdown. There is no code, build system, or test suite.

- `phase8-onion-pivot.md` — Current direction: onion pivot rationale, target pest, pheromone compound (needs update to reflect autodissemination concept)
- `TalongGuard-Business-Plan.md` — Master business plan (currently for old eggplant concept, needs full rewrite)
- `phase3-eggplant-deepdive.md` — Original eggplant borer research (historical reference)
- `phase4-pitch-deck.md` — Pitch deck skeleton (needs rewrite for onion/autodissemination)
- `phase5-technical-architecture.md` — ESP32 circuit design for old concept (needs replacement with autodissemination device design)
- `phase6-validation-plan.md` — Validation plan (needs rewrite)
- `phase7-financial-model.md` — Financial model (needs rewrite)
- `proposal-v2-problem.md` — Research-grounded problem statement (eggplant, historical)
- `loop-roadmap.md` — Phase tracker
- `idea-pool.md`, `idea-pool-v2.md`, `phase2-scoring.md` — Early ideation (historical)

## Current Product Direction (Autodissemination Device)

### Concept
A passive device using pheromone lure to attract S. exigua male moths, inoculate them with Metarhizium spores on a velvet-lined interior surface, and release them alive. Moths spread the fungus through mating contact, contaminating females, eggs, and larvae. The fungus kills larvae within 5-7 days (100% mortality at proper concentration, per NCPC-UPLB studies).

### Key Technical Parameters
- **Target pest:** Spodoptera exigua (harabas/onion armyworm)
- **Pheromone compound:** (Z,E)-9,12-tetradecadienyl acetate
- **Biocontrol agent:** Metarhizium rileyi (preferred for S. exigua) or M. anisopliae
- **5cm spatial separation** required between pheromone lure and fungal spore surface (prevents germination inhibition)
- **UV protection** — device interior must be opaque; spores degrade in 4 hours of direct sunlight
- **Spore shelf life:** 6-10 months dry powder at ambient temperature
- **Moth activity:** Nocturnal, mates in second half of scotophase

### Supply Chain
- **Spores:** Self-produced using published rice substrate protocol (PhilRice Bulletin No. 44, cost ~₱17.59/bag), starter culture from NCPC-UPLB or DA-RCPC
- **Pheromone lures:** Rubber septa from international suppliers (Pherobio, Evergreen Growers); DA Region 3 has existing Philippine procurement channel
- **Device body:** Local materials — PVC pipe/plastic, velvet fabric, mounting hardware

### Business Model
- Device (one-time purchase) + refill kits (pheromone lure + spore cartridge, recurring revenue)
- Target market: Mindoro onion farmers (8,637 ha), Nueva Ecija (2,300+ ha)

## Key Research Citations (for reference when writing documents)
- Montecalvo & Navasero (NCPC-UPLB): M. rileyi vs S. exigua, 100% mortality at 10^7 conidia/mL
- Arida, Punzal et al. (UPLB, 2004): Pheromone traps in Bongabon, Nueva Ecija onion fields
- OMSC (2024): M. anisopliae vs harabas on onion "Red Pinoy" in San Jose, Occ. Mindoro
- Korean study (Mycobiology): M. anisopliae FT83 isolate, 100% S. exigua mortality day 3
- Horizontal transmission studies: Spodoptera moths retain/transmit spores for 72 hours

## Important Context
- Panel approved pheromone trap concept and directed pivot from eggplant to onion
- The user is an ABE (Agricultural and Biosystems Engineering) student — device fabrication is within their skillset
- Documents labeled "phase3" through "phase7" and the business plan are based on the OLD eggplant concept and need rewriting
- Only `phase8-onion-pivot.md` reflects the onion direction, but it also needs updating for the autodissemination concept
- The user explicitly rejected: pure automation/monitoring traps, bundled two-product approaches, anything requiring scientific research
