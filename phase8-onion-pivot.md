# Phase 8: Onion Pivot — Deep Dive
**2026-09-15 | Panel Feedback Response**

*Panel approved pheromone trap concept. Directed pivot from eggplant to onion — higher national urgency. Core technology unchanged; target pest, pheromone compound, and market profile updated.*

---

## 1. WHY ONION

### 1.1 The National Context

The Philippines experienced a severe onion supply crisis in late 2022–2023. Retail prices spiked to ₱700/kg (normal: ₱80–150/kg), triggering Congressional hearings, DA emergency imports, and national media coverage. The crisis exposed a structural vulnerability: the Philippines cannot grow enough onion to feed itself.

| Indicator | Value | Source |
|-----------|-------|--------|
| Area harvested (onion) | ~22,000 hectares | PSA, 2023 |
| Annual production | ~190,000–220,000 MT | PSA, 2022–2023 |
| Domestic demand | ~300,000+ MT/year | DA estimates |
| Supply gap | ~80,000–100,000 MT imported annually | PSA trade data |
| Peak crisis price | ₱700/kg (Jan 2023) | news reports |
| Normal farmgate price | ₱40–80/kg | PSA |

**The government is actively investing in onion self-sufficiency** — DA programs, DOST technology support, and LGU extension efforts are all channeling resources toward increasing domestic onion production. This is where funding flows right now.

### 1.2 Onion Production in Oriental Mindoro

Oriental Mindoro, including San Jose and surrounding municipalities, grows multiplier onion (shallot / *sibuyas Tagalog*) and bulb onion as rotational crops, typically after rice. Local advantages:

- Existing onion farmer community within reach of MinSU
- Municipal Agriculture Office support
- Dry-season cropping window aligns with pest monitoring needs
- Team is FROM the community — established trust and access

---

## 2. THE PEST

### 2.1 Primary Target: *Spodoptera exigua* (Beet Armyworm / Onion Armyworm)

**Classification:** Lepidoptera: Noctuidae

*Spodoptera exigua* is the most economically important lepidopteran pest of allium crops (onion, shallot, garlic) across Southeast Asia, including the Philippines.

**Biology:**
- Female moths oviposit egg masses (50–150 eggs) on leaves at night
- Larvae feed gregariously on foliage, skeletonizing leaves
- Severe infestations can defoliate entire fields within days — "armyworm" behavior
- Pupation in soil; adults emerge and repeat the cycle (~30-day generation time)
- Polyphagous — also attacks rice, corn, cabbage, tomato, but onion/shallot are primary hosts
- **Nocturnal adults** — highly amenable to pheromone trapping

**Damage pattern:**
- Unlike EFSB (which bores inside fruit invisibly), armyworm damage is visible but **sudden** — outbreaks escalate from manageable to catastrophic in 2–3 days
- By the time a farmer sees mass defoliation, the larvae are already large (L3–L5) and harder to control
- **The same core problem: detection happens too late for efficient intervention**

### 2.2 Pheromone

The sex pheromone of *Spodoptera exigua* is well-characterized:

| Component | Role | Chemical name |
|-----------|------|---------------|
| **Major component** | Primary attractant | (Z,E)-9,12-tetradecadienyl acetate (Z9,E12-14:Ac) |
| Minor component 1 | Synergist | (Z)-9-tetradecen-1-ol (Z9-14:OH) |
| Minor component 2 | Synergist | (Z)-9-tetradecenyl acetate (Z9-14:Ac) |

**Key references:**
- Tumlinson et al. (1990) — original pheromone identification
- Mitchell (1979) — field trapping optimization
- Multiple suppliers on IndiaMART sell *S. exigua* pheromone lures commercially

**Availability:** Pre-formulated rubber septum lures AND raw compound are both available from Indian suppliers. Same sourcing pathway as the eggplant pheromone — no new supply chain needed.

### 2.3 Economic Threshold Level (ETL)

ETL for *S. exigua* on allium crops varies by region and study. Values from published literature:

| Source/Region | ETL (moths/trap/night) | Notes |
|---------------|----------------------|-------|
| General recommendation | 5–10 moths/trap/night | Widely cited in IPM literature |
| Southeast Asian field trials | 8–12 moths/trap/night | Varies by crop stage and local conditions |

**Action needed:** Literature review for Philippines-specific or tropical-Asia-specific ETL values for *S. exigua* on onion. If no published Philippine ETL exists, this becomes part of the thesis contribution — **establishing a local ETL through the pilot data.**

### 2.4 Secondary Pests (Awareness, Not Targets for v1.0)

| Pest | Type | Pheromone-trappable? |
|------|------|---------------------|
| *Thrips tabaci* (onion thrips) | Thysanoptera | No — not a moth, no sex pheromone trapping |
| *Spodoptera litura* (common cutworm) | Lepidoptera | Yes — different pheromone; future lure swap target |
| *Helicoverpa armigera* (tomato fruitworm) | Lepidoptera | Yes — future expansion |

v1.0 focuses on *S. exigua* only. Multi-pest capability (swappable lures) is a v2.0 feature.

---

## 3. WHAT CHANGES VS. WHAT STAYS

### Stays the Same (Core Platform)

| Component | Status |
|-----------|--------|
| ESP32 + IR break-beam counter | Unchanged |
| SIM800L GSM + SMS alerts | Unchanged |
| Solar panel + 18650 battery | Unchanged |
| 3D-printed enclosure (funnel trap) | Minor dimensional tweaks possible |
| Variable clearance collar | Unchanged — same lure conservation benefit |
| Firmware logic (count → threshold → SMS) | Threshold value updated |
| Self-formulated lure process (rubber septum + solvent loading) | Same process, different compound |
| Razor-and-blade business model | Unchanged |
| Break-even economics structure | Unchanged |

### Changes

| Element | Eggplant (old) | Onion (new) |
|---------|---------------|-------------|
| Target pest | *Leucinodes orbonalis* (EFSB) | *Spodoptera exigua* (armyworm) |
| Pheromone compound | (E)-11-hexadecenyl acetate | (Z,E)-9,12-tetradecadienyl acetate |
| ETL | 6–8 moths/trap/night | ~5–10 (needs Philippine validation) |
| Crop | Eggplant (*Solanum melongena*) | Onion / shallot (*Allium cepa* / *A. cepa* var. *aggregatum*) |
| Primary market | Mindoro eggplant farmers | Mindoro onion farmers (expandable to Nueva Ecija, Pangasinan) |
| Branding | "TalongGuard" (talong = eggplant) | **Needs new name** |
| National urgency | High (₱33.85B loss) | **Higher** (supply crisis, active government programs) |
| Funding alignment | Good (agri-tech) | **Better** (onion self-sufficiency is a national priority) |

---

## 4. SPECIES SPECIFICITY — WHY NO CAMERA

### The Panel's Question

> "How can you be sure only the target pest gets trapped?"

### The Answer: The Pheromone IS the Species Filter

Sex pheromones are **species-specific by evolutionary design.** Their entire biological function is to ensure that only males of the correct species respond. Cross-species attraction would be reproductively wasteful and is selected against.

The synthetic pheromone blend for *S. exigua* attracts *S. exigua* males. Other moths, beetles, flies, and beneficial insects **do not respond** to it. This is not an engineering assumption — it is the foundational principle of pheromone-based IPM, validated across thousands of published field trials (Witzgall et al., 2010, *Annual Review of Entomology*).

**Published specificity data:** Pheromone traps typically capture **90–95%+ target species** when using the correct synthetic blend (Cork et al., 2003; Witzgall et al., 2010).

### Multi-Layer Filtering (Engineering Redundancy)

Even beyond pheromone specificity, the trap design adds engineering layers:

| Layer | What it filters | How |
|-------|----------------|-----|
| **1. Pheromone** | Non-target species | Only *S. exigua* males are attracted — biological filter |
| **2. Funnel geometry** | Wrong-sized insects | Funnel neck (2cm) and IR gap (3mm) exclude very large and very small arthropods |
| **3. IR beam-break timing** | Non-moth objects | Software rejects triggers <5ms (debris, rain) and >500ms (leaves, large insects) |
| **4. Nocturnal-only counting** | Daytime visitors | System only counts during 6PM–6AM when *S. exigua* adults are active |

### Why a Camera Would Be Overkill

| Concern | Camera approach | Our approach |
|---------|----------------|-------------|
| Species ID accuracy | 90–98% (AI/ML dependent) | 90–95% (pheromone does it) |
| Cost added | +₱1,500–3,000 (camera module + processing) | ₱0 |
| Power consumption | 10–50x higher (image processing) | Negligible (IR beam) |
| Cloud dependency | Usually required for ML inference | None — fully offline |
| Light attraction | Camera light or flash attracts non-target insects, **contaminating the sample** | IR beam is invisible to insects |
| Complexity | ML model training, edge/cloud compute, connectivity | Simple threshold counter |

**A camera adds cost and complexity to solve a problem the pheromone already solved.**

---

## 5. IS THERE A NEED? — EVIDENCE FRAMEWORK

### What Published Research Already Shows

- Onion supply deficit is structural — Philippines imports ~80,000–100,000 MT/year
- *S. exigua* outbreaks cause sudden, severe losses across allium crops in Southeast Asia
- Filipino onion farmers rely on calendar-based pesticide spraying (same pattern as eggplant)
- No affordable automated pest monitoring tool exists for onion in the Philippine market
- Government actively investing in onion self-sufficiency programs

### What Must Be Validated Locally (Farmer Conversations)

These conversations should be conducted with onion/shallot farmers in San Jose, Oriental Mindoro area:

**Questions to ask (non-leading):**

1. "What are the biggest problems you face growing onion?"
2. "How do you decide when to spray pesticides?"
3. "How much do you spend on pesticide per season?"
4. "Have you ever had a sudden pest outbreak that you didn't see coming?"
5. "If a device could tell you exactly when pests are arriving, would that change how you farm?"
6. "What price would make you say 'that's worth trying'?"

**What you need to hear (validation signals):**
- Pest damage / armyworm mentioned unprompted as a major concern
- Spraying decisions are guesswork-based, not data-based
- Pesticide cost is a significant burden
- Interest in "knowing before it's too late"
- Price tolerance in the ₱2,000–5,000 range

**Target: 5–8 conversations before prototype build.**

---

## 6. WOULD THEY BUY? — ECONOMIC LOGIC

### Farmer ROI (Onion)

| Item | Value |
|------|-------|
| Device cost (one-time) | ₱3,000 |
| Lure refills per season | 2–3 lures × ₱100 = ₱200–300 |
| Pesticide cost per hectare per season (typical) | ₱15,000–40,000 |
| Estimated reduction with threshold-based spraying | 40–60% |
| Estimated savings per season | ₱6,000–24,000 |
| **Payback period** | **Less than one season** |

### Onion vs. Eggplant — Farmer Economics

| | Eggplant farmer | Onion farmer |
|---|---|---|
| Crop value per hectare | Moderate | **Higher** (₱150–300k gross at normal prices) |
| Pesticide spend | ₱20–50k/season | ₱15–40k/season |
| Risk of total loss event | Gradual (borer accumulates) | **Sudden** (armyworm outbreak in 2–3 days) |
| Value of early warning | High | **Very high** — days matter |
| Willingness to invest in prevention | Moderate | **Higher** — recent crisis memory |

**The "would they buy" answer is stronger for onion than for eggplant** — higher crop value, more acute risk, and fresh memory of what happens when supply collapses.

---

## 7. WHAT IS THE NOVELTY?

### What Is NOT Novel (Established Science)

- Pheromone trapping of moths — known since 1960s
- *S. exigua* pheromone composition — published since 1990
- IoT-based pest monitoring — commercial products exist (Trapview, iScout)
- SMS alerts — basic telecommunications

### What IS Novel

| Novel Contribution | Why It's New |
|---|---|
| **Automated moth counting at <₱5,000** | No product exists at this price point globally. Commercial alternatives: ₱48,000–56,000 (Trapview, iScout). This is a 10–15x cost reduction. |
| **Multi-layer species filtering without camera/AI** | Novel engineering approach — pheromone specificity + physical geometry + IR timing replaces camera + ML inference. Avoids light-attraction contamination inherent in camera-based systems. Lower power, lower cost, fully offline. |
| **Variable airflow collar for lure conservation** | No existing trap design modulates airflow to extend pheromone lure lifespan. This is a novel mechanical feature. |
| **Self-formulated lure supply chain for PH market** | No Philippine retail source exists for *S. exigua* pheromone lures. Building this supply pathway (raw compound from India + local formulation at MinSU) is itself a contribution. |
| **SMS-based IPM coaching, infrastructure-independent** | No system delivers threshold-based pest alerts + IPM practice reminders to Filipino farmers' basic phones via SMS, without requiring internet, smartphone, or cloud. |
| **Philippine ETL validation for *S. exigua* on onion** (if no published local value exists) | Establishing a local economic threshold level through pilot trap data would be a direct scientific contribution. |

### The One-Liner for the Panel

> "Pheromone trapping is proven science. What doesn't exist is a system that automates it for ₱3,000, runs on solar, works offline, and texts a Filipino onion farmer when to spray. That's the gap, and that's the novelty."

---

## 8. NAMING

"TalongGuard" = talong (eggplant) + guard. No longer fits.

Options to consider:

| Name | Meaning | Notes |
|------|---------|-------|
| **SibuyasGuard** | sibuyas (onion) + guard | Direct parallel, Filipino |
| **CropGuard** | Generic crop protection | Multi-crop expandable, but generic |
| **PestGuard** | Generic pest monitoring | Same issue — generic |
| **TrapSense** | Trap + sensing | Tech-forward, crop-neutral |
| **AgriSense** | Agriculture + sensing | Broader platform feel |
| **HarvestGuard** | Harvest protection | Aspirational, crop-neutral |

Recommendation: Choose a **crop-neutral name** if the panel sees multi-crop potential as a strength. Keep it Filipino-accessible.

---

## 9. NEXT STEPS

1. **Farmer conversations** (5–8) with onion growers in San Jose, Oriental Mindoro — validate problem severity, spraying behavior, willingness to pay
2. **Literature review** — *S. exigua* ETL values for onion in tropical Asia; if none exist for Philippines, frame ETL establishment as thesis contribution
3. **Source pheromone** — contact IndiaMART suppliers for (Z,E)-9,12-tetradecadienyl acetate pricing and availability (raw compound AND pre-made lures for comparison)
4. **Update proposal documents** — pivot all technical, financial, and validation docs from eggplant to onion
5. **Prototype build** — hardware identical; update firmware threshold value once ETL is established
6. **Pilot design** — deploy 2–3 traps across onion fields in San Jose during next cropping season

---

## REFERENCES (Onion Pivot)

*To be expanded with full citations after literature review:*

- PSA (2023). Onion production statistics. psa.gov.ph
- Tumlinson, J.H. et al. (1990). Identification of the sex pheromone of *Spodoptera exigua*
- Witzgall, P., Kirsch, P., & Cork, A. (2010). Sex pheromones and their impact on pest management. *Annual Review of Entomology*, 55, 453–472.
- Cork, A. et al. (2003). Pheromone trap optimization and IPM trials. *Bulletin of Entomological Research*.
- Mitchell, E.R. (1979). Field evaluation of *S. exigua* pheromone traps.
- DA Philippines — Onion self-sufficiency program documents
- News sources on 2022–2023 onion crisis

*Previous eggplant references (Phase 3, proposal-v2) remain in the repository for comparison and as evidence of platform adaptability.*
