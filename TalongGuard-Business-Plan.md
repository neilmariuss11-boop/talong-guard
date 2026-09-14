# TalongGuard Business Plan
### Smart Pest Monitoring for Filipino Eggplant Farmers
**Prepared by:** [Team Names] | Mindoro State University  
**Program:** BS Agricultural and Biosystems Engineering  
**Course:** Technopreneurship  
**Date:** September 2026

---

# TABLE OF CONTENTS

1. Executive Summary
2. Company Description
3. Problem Statement
4. Solution: TalongGuard
5. Market Analysis
6. Competitive Analysis
7. Business Model
8. Marketing and Sales Strategy
9. Technical Overview
10. Validation Plan
11. Financial Projections
12. Funding Requirements
13. Growth Roadmap
14. Risk Analysis
15. Appendix

---

# 1. EXECUTIVE SUMMARY

**TalongGuard** is a solar-powered smart pest monitoring device that tells Filipino eggplant farmers exactly when to spray pesticide — and when not to.

The Eggplant Fruit and Shoot Borer (*Leucinodes orbonalis*) causes P33.85 billion in annual losses to Philippine agriculture. Eggplant is the country's #1 vegetable crop (21,225 hectares), and borer damage destroys 51-80% of harvests at high pest pressure. Farmers currently spray pesticides up to 80 times per season — blindly — spending 20-40% of their total production cost on chemicals that often fail because timing is wrong.

**The science to solve this already exists.** Male EFSB moths are attracted to sex pheromone lures, and entomologists have established that 6-8 moths per trap per night is the threshold requiring intervention. The problem: no affordable tool delivers this data to Filipino smallholder farmers.

**TalongGuard bridges this gap.** An ESP32-based device with an infrared moth counter, pheromone lure, and GSM module automatically counts moths nightly and sends an SMS alert to the farmer's phone: "Spray today" or "Safe — save your money." Solar-powered, no internet required.

**Key numbers:**
- Device cost: P3,000 (one-time)
- Farmer saves: P10,000-25,000 per season in pesticide costs
- Payback period: Less than one harvest
- No competitor exists at this price point in the Philippines
- Total addressable market: P127.4M in hardware + P17M/year in consumable lure refills
- 3-year revenue projection: P6.77 million
- 3-year net income: P3.2 million

**Tagline:** *"Huwag hulaan. Alamin."* (Don't guess. Know.)

---

# 2. COMPANY DESCRIPTION

### Who We Are
TalongGuard is founded by a team of Agricultural and Biosystems Engineering students at Mindoro State University (MinSU). We combine engineering skills in IoT, sensor systems, and 3D fabrication with deep understanding of Philippine agriculture — because we come from the farming communities we serve.

### Team

**[Your Name]** — Lead Engineer and CEO
- 4th year ABE, MinSU
- Skills: ESP32/Arduino programming, 3D printing, PCB design
- Role: Hardware development, firmware, farmer interviews

**[Teammate 2]** — [Role]
- [Year and program]
- [Skills]
- Role: [Specific responsibilities]

**[Teammate 3]** — [Role]
- [Year and program]
- [Skills]
- Role: [Specific responsibilities]

**Academic Advisor:** [Professor Name], ABE Department, MinSU

### Company Details
- **Location:** Mindoro, Philippines
- **Legal Form:** To be registered as sole proprietorship or partnership (DTI registration pending)
- **Stage:** Pre-revenue, prototype development

---

# 3. PROBLEM STATEMENT

## The Pest
The Eggplant Fruit and Shoot Borer (EFSB), *Leucinodes orbonalis* Guenee, is the most destructive pest of eggplant in South and Southeast Asia. Female moths lay eggs on leaves and fruit at night. Larvae bore into the fruit within hours of hatching — invisible from outside until the damage is irreversible.

## The Scale of Damage

| Metric | Value | Source |
|--------|-------|--------|
| PH eggplant area | 21,225 hectares | PSA |
| Annual production | 248,000 metric tons | PSA |
| Production value | P1.027 billion (2024) | CEIC |
| Yield loss from EFSB | 51-80% at high pressure | PLOS ONE |
| National annual loss | P33.85 billion | ISAAA |
| Spray frequency | Up to 80 times/season | UPLB CAFS |
| Pesticide share of cost | 20-40% of production | ISAAA |

## What Farmers Do Today

1. **Calendar spraying** — Spray every 2-3 days regardless of pest presence. Expensive (P20,000-50,000/season), harmful to health, often ineffective because timing doesn't match pest activity.
2. **Wait and see** — Spot borer damage after it's too late. Fruit is already reject-grade.
3. **Manual pheromone traps** — Exist in research settings but no farmer counts moths systematically. No threshold-based decision-making in practice.
4. **Nothing** — Accept losses and sell at reduced prices.

## The Core Problem
**Farmers have no affordable, automated way to know when pests are present and when intervention is actually needed.** They spray blind or accept losses.

---

# 4. SOLUTION: TALONGGUARD

## What It Is
A solar-powered smart pheromone trap that automatically counts EFSB moths at night and sends SMS alerts to farmers when pest populations exceed the scientifically established spray threshold.

## How It Works

1. **Attract** — Pheromone lure (E-11-hexadecenyl acetate and E-11-hexadecenol) attracts male EFSB moths into a funnel trap.
2. **Count** — Infrared break-beam sensor at the funnel neck counts each moth entering. ESP32 microcontroller logs the nightly count.
3. **Decide** — Onboard firmware compares nightly count to the Economic Threshold Level (6-8 moths/trap/night).
4. **Alert** — At dawn, SIM800L GSM module sends SMS to farmer:
   - Threshold exceeded: *"TalongGuard: 12 moths last night. THRESHOLD EXCEEDED. Spray today. Batt: 78%"*
   - Below threshold: *"TalongGuard: 3 moths last night. Safe, no spray needed. Batt: 92%"*

## Key Features
- **Solar-powered** — indefinite field operation, no charging needed
- **SMS-based** — works on any phone, no internet or smartphone app required
- **Autonomous** — farmer places it in the field and receives texts
- **Weatherproof** — 3D-printed PETG enclosure rated IP54
- **Data logging** — 30 days of nightly moth counts stored on device

## Value Proposition
**"Spray only when you need to."**
- Reduces pesticide applications by 50-70%
- Saves P10,000-25,000 per hectare per season
- Protects farmer health from excessive chemical exposure
- Improves crop quality by timing intervention to actual pest presence

---

# 5. MARKET ANALYSIS

## Market Sizing

**TAM — Total Addressable Market (All PH eggplant farms)**
- 21,225 hectares x 2 traps/ha = 42,450 units
- Hardware: **P127.4 million**
- Annual lure refills: **P17.0 million/year**

**SAM — Serviceable Addressable Market (MIMAROPA + Calabarzon)**
- ~4,200 hectares = 8,400 units
- Hardware: **P25.2 million** | Refills: **P3.4 million/year**

**SOM — Year 1 (Mindoro)**
- 100 units | **P319,500 revenue**

## Customer Segments

**Primary: Smallholder Eggplant Farmers**
- 0.5-2 hectare farms, P80,000-200,000 annual eggplant income
- Spend P20,000-50,000/season on pesticide
- Own budget Android phone, can receive SMS

**Secondary: Agricultural Extension Workers**
- Need pest data to support IPM recommendations

**Tertiary: Farmer Cooperatives**
- Bulk purchase for members, shared data

## Market Trends
- Government push for Integrated Pest Management
- Growing concern over pesticide residues in food
- DA extension programs promoting tech adoption
- Rising input costs make precision agriculture attractive

---

# 6. COMPETITIVE ANALYSIS

| Solution | Price | Auto-Count | Alerts | Offline | Pre-Damage | Affordable |
|----------|-------|:----------:|:------:|:-------:|:----------:|:----------:|
| Manual pheromone trap | P200-500 | No | No | Yes | Yes | Yes |
| Pest ID apps (Plantix) | Free | No | No | No | No | Yes |
| Commercial smart traps | P48-56k | Yes | Yes | No | Yes | No |
| Calendar spraying | P20-50k/season | No | No | Yes | No | No |
| **TalongGuard** | **P3,000** | **Yes** | **Yes** | **Yes** | **Yes** | **Yes** |

**TalongGuard is 15-20x cheaper than commercial smart traps.** No product in the Philippine market provides automated moth counting with SMS alerts at a smallholder-accessible price.

---

# 7. BUSINESS MODEL

## Razor and Blade

| Stream | Price | Margin | Frequency |
|--------|-------|--------|-----------|
| Device | P2,500-3,500 | 51% | One-time |
| Lure refill | P100 | 55% | Every 30-45 days |
| Coop bulk (10+) | P2,200/unit | 45% | Per order |
| *Future: data dashboard* | *P500/season* | *90%* | *Annual* |

## Customer ROI

| | With TalongGuard | Without |
|---|---|---|
| Sprays per season | 20-35 | 50-80 |
| Pesticide cost | P8,000-15,000 | P20,000-50,000 |
| TalongGuard annual cost | P3,400 (Y1), P400 (Y2+) | P0 |
| **Net savings Year 1** | **P6,600-31,600** | — |

---

# 8. MARKETING AND SALES STRATEGY

## Phase 1: Seed (Months 1-8)
- Direct farmer relationships from pilot
- Free trial devices generate testimonials and proof
- Cost: near zero

## Phase 2: Launch (Months 9-18)
- **DA Extension Workers** — partner with Municipal Agriculture Office, demo units for AEWs
- **Farmer Cooperatives** — bulk discount presentations at coop meetings
- **Agri-Fairs** — live demo at municipal/provincial fairs
- **Facebook Groups** — video testimonials, before/after pesticide cost comparisons

## Phase 3: Regional (Months 19-36)
- Agri-supply store consignment/wholesale (MIMAROPA, Calabarzon)
- DA Regional IPM program integration
- Agricultural university extension partnerships

## Messaging
- **Lead:** "Save P10,000-25,000 per season on pesticide."
- **Proof:** Pilot data showing reduced spraying + maintained yield
- **Trust:** "Backed by science — same threshold used by entomologists."
- **Tagline:** *"Huwag hulaan. Alamin."*

---

# 9. TECHNICAL OVERVIEW

## Architecture

```
Solar Panel (5V 1W) --> TP4056 Charger --> 18650 Battery (3400mAh)
                                                |
                                           ESP32 MCU
                                           /        \
                               IR Break-Beam     SIM800L GSM
                               Sensor (counter)  (SMS alerts)
```

## Specifications

| Spec | Value |
|------|-------|
| Controller | ESP32 DevKit V1 |
| Detection | IR break-beam, interrupt-driven, 50ms debounce |
| Communication | SIM800L GSM, 1 SMS/day at dawn |
| Power | 1W solar + 3400mAh 18650 |
| Daily consumption | ~110 mAh |
| Battery-only life | ~31 days |
| With solar | Indefinite |
| Enclosure | 3D-printed PETG, IP54 |
| Operation | Night only (6 PM - 6 AM) |
| Storage | 30 days on SPIFFS |
| BOM (50+ units) | P1,475 |

---

# 10. VALIDATION PLAN

## Customer Interviews
- 10-15 eggplant farmers, structured 10-question script in Filipino
- Targets: problem severity, willingness to use/pay, signal availability

## Pilot Program
- 6 farmers: 3 treatment (TalongGuard) vs 3 control (normal practice)
- 1 full cropping season (3-4 months)
- Weekly data collection: spray count, cost, damage, device accuracy

## Must-Pass KPIs

| KPI | Target | Minimum |
|-----|--------|---------|
| Moth count accuracy | 90% | 80% |
| SMS delivery | 95% | 90% |
| Pesticide cost savings vs control | 50% | 30% |
| Yield vs control | Equal or better | Within 10% |
| Post-trial buy intent | 2 of 3 | 1 of 3 |

---

# 11. FINANCIAL PROJECTIONS

## 3-Year Overview

| | Year 1 | Year 2 | Year 3 |
|---|--------|--------|--------|
| Units sold | 100 | 500 | 1,500 |
| Total revenue | P319,500 | P1,653,000 | P4,800,000 |
| COGS | P78,910 | P737,500 | P1,699,500 |
| Operating expenses | P48,000 | P305,000 | P700,000 |
| **Net income** | **P192,590** | **P610,500** | **P2,400,500** |

**3-Year cumulative: P6.77M revenue, P3.2M net income**

## Break-Even
- 84 units sold (Month 12 at projected pace)
- Profitable even at half projected sales volume

## Sensitivity
- Viable down to P2,500 selling price
- Worst-case 3-year scenario (25 Y1 units): still P250,000 net — viable small business
- Best-case (200 Y1 units): P9.5M 3-year net

---

# 12. FUNDING REQUIREMENTS

## Total: P216,000

| Phase | Amount | Purpose |
|-------|--------|---------|
| Phase 1 (Prototype + Pilot) | P16,000 | 2 prototypes, lures, transport, materials |
| Phase 2 (First 100 units) | P200,000 | Production, inventory, marketing, working capital |

## Sources
1. Team funds: P5,000 (prototype)
2. DOST-SETUP: up to P500,000
3. DOST-PCIEERD: P200,000-2,000,000
4. DA-BAR: P100,000+
5. Competitions: DOST-TAPI, IdeaSpace, Go Negosyo
6. Pre-sales: P50,000 from 20 early-bird deposits

---

# 13. GROWTH ROADMAP

| Phase | Period | Goal |
|-------|--------|------|
| Prove | Months 1-8 | Prototype, pilot 6 farmers, validate KPIs |
| Sell | Months 9-18 | 100 units in Mindoro via DA/coops |
| Expand | Months 19-30 | 500 units across MIMAROPA + Calabarzon |
| Scale | Months 31-36 | 1,500 units, national rollout begins |
| Platform | Year 3+ | Multi-pest lures, data analytics, ASEAN expansion |

---

# 14. RISK ANALYSIS

| Risk | Mitigation |
|------|-----------|
| IR sensor counts non-moths | Software filter (5-500ms window) + funnel design blocks large insects |
| Farmers don't change spray behavior | Build trust via pilot testimonials + AEW endorsement |
| Lure supply disruption from India | 2-month buffer stock; explore UPLB local synthesis |
| Component costs rise | Can absorb 20%; raise price at 50%+ |
| Device fails outdoors | IP54 enclosure, conformal coating, desiccant, pilot stress-test |
| Competitor enters | First-mover data advantage, consumable lock-in, farmer trust |

---

# 15. APPENDIX

## Supporting Documents

| Document | Contents |
|----------|----------|
| phase3-eggplant-deepdive.md | Full analysis, lean canvas, BOM, personas |
| phase4-pitch-deck.md | 13-slide pitch deck with speaker notes |
| phase5-technical-architecture.md | Circuits, firmware, power budget, enclosure, sourcing |
| phase6-validation-plan.md | Interview script, pilot protocol, 4 data forms |
| phase7-financial-model.md | Monthly P&L, sensitivity, funding detail |

## Key Sources
1. PSA — Eggplant production statistics (psa.gov.ph)
2. ISAAA — P33.85B annual EFSB loss estimate (2021)
3. Hautea et al. — Bt Eggplant field trials (PLOS ONE, 2016)
4. UPLB CAFS — Bt Eggplant program
5. Nature Scientific Reports — IoT pest management systems (2024)
6. BanglaJOL — EFSB pheromone ETL studies
7. IndiaMART — Pheromone lure pricing

---

*Prepared for Technopreneurship, Mindoro State University, September 2026*

*TalongGuard — "Huwag hulaan. Alamin."*
