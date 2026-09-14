# Phase 7: Financial Model — TalongGuard
**2026-09-12 | Loop Turn 6**

---

## 1. UNIT ECONOMICS

### A. Device Unit Economics

| Component | Prototype (P) | Scale 50+ (P) | Scale 500+ (P) |
|-----------|--------------|---------------|-----------------|
| ESP32 DevKit V1 | 350 | 280 | 220 |
| IR break-beam sensor pair | 120 | 90 | 70 |
| SIM800L GSM module | 280 | 220 | 180 |
| GSM antenna | 40 | 30 | 25 |
| Solar panel 5V 1W | 250 | 200 | 160 |
| TP4056 + protection | 35 | 25 | 20 |
| 18650 battery 3400mAh | 150 | 120 | 100 |
| Battery holder | 20 | 15 | 10 |
| Resistors + cap + LED | 30 | 15 | 10 |
| PETG filament (~200g) | 200 | 160 | 120 |
| Silicone sealant + gasket | 30 | 20 | 15 |
| M3 hardware | 20 | 10 | 8 |
| PCB (JLCPCB) | 200 | 60 | 35 |
| Wires, connectors | 50 | 30 | 20 |
| Packaging + label | 0 | 50 | 40 |
| Assembly labor | 0 | 150 | 100 |
| **TOTAL** | **P1,775** | **P1,475** | **P1,133** |

| Metric | Scale 50+ | Scale 500+ |
|--------|-----------|------------|
| BOM + Labor | P1,475 | P1,133 |
| Selling Price | P3,000 | P2,800 |
| **Gross Margin** | **P1,525 (51%)** | **P1,667 (60%)** |

### B. Pheromone Lure Economics

| Item | Cost (P) |
|------|----------|
| Lure purchase (India, bulk 100+) | 30 |
| Shipping per lure (amortized) | 10 |
| Packaging (resealable foil) | 5 |
| **Total cost per lure** | **P45** |
| **Selling price** | **P100** |
| **Gross margin** | **P55 (55%)** |

### C. Customer Lifetime Value (3-Year)

| Item | Amount (P) |
|------|-----------|
| Device (one-time) | 3,000 |
| Lure refills x3 years (4/year) | 1,200 |
| **3-Year LTV** | **4,200** |
| 3-Year cost to serve | 1,880 |
| **3-Year Gross Profit/Customer** | **2,320 (55%)** |

---

## 2. THREE-YEAR P&L

### Year 1 — Monthly (Pilot + First Sales)

| Mo | Activity | Units | HW Rev | Lure Rev | Total Rev | COGS | OpEx | Net |
|----|----------|-------|--------|----------|-----------|------|------|-----|
| 1 | Interviews | 0 | 0 | 0 | 0 | 0 | 2,000 | -2,000 |
| 2 | Sourcing | 0 | 0 | 0 | 0 | 0 | 2,000 | -2,000 |
| 3 | Build prototypes | 0 | 0 | 0 | 0 | 3,960 | 2,000 | -5,960 |
| 4 | Lab testing | 0 | 0 | 0 | 0 | 0 | 2,000 | -2,000 |
| 5 | Pilot starts | 0 | 0 | 0 | 0 | 600 | 3,000 | -3,600 |
| 6 | Pilot running | 0 | 0 | 0 | 0 | 300 | 3,000 | -3,300 |
| 7 | Pilot running | 0 | 0 | 0 | 0 | 300 | 3,000 | -3,300 |
| 8 | Pilot report | 0 | 0 | 0 | 0 | 0 | 2,000 | -2,000 |
| 9 | Batch production | 0 | 0 | 0 | 0 | 73,750 | 5,000 | -78,750 |
| 10 | Sales begin | 30 | 90,000 | 3,000 | 93,000 | 0 | 8,000 | 85,000 |
| 11 | Sales ramp | 35 | 105,000 | 6,500 | 111,500 | 0 | 8,000 | 103,500 |
| 12 | Sales continue | 35 | 105,000 | 10,000 | 115,000 | 0 | 8,000 | 107,000 |
| **Y1** | | **100** | **300,000** | **19,500** | **319,500** | **78,910** | **48,000** | **192,590** |

*Y1 net margin inflated by unpaid founder labor. Imputed salary (P12k/mo x 3 x 4 active mo = P144k) would yield adjusted net of P48,590.*

### Year 2 — Quarterly (Regional Expansion)

| Qtr | Units | Cumul Active | HW Rev | Lure Rev | Total Rev | COGS | OpEx | Net |
|-----|-------|-------------|--------|----------|-----------|------|------|-----|
| Q1 | 80 | 180 | 240,000 | 18,000 | 258,000 | 118,000 | 60,000 | 80,000 |
| Q2 | 120 | 300 | 360,000 | 30,000 | 390,000 | 177,000 | 75,000 | 138,000 |
| Q3 | 150 | 450 | 450,000 | 45,000 | 495,000 | 221,250 | 85,000 | 188,750 |
| Q4 | 150 | 600 | 450,000 | 60,000 | 510,000 | 221,250 | 85,000 | 203,750 |
| **Y2** | **500** | **600** | **1,500,000** | **153,000** | **1,653,000** | **737,500** | **305,000** | **610,500** |

OpEx: 1 part-time assembler (P8k/mo), marketing P5k/mo, logistics P5k/mo, SMS, lure imports.

### Year 3 — Quarterly (National Rollout Begins)

| Qtr | Units | Cumul Active | HW Rev | Lure Rev | Total Rev | COGS | OpEx | Net |
|-----|-------|-------------|--------|----------|-----------|------|------|-----|
| Q1 | 300 | 900 | 840,000 | 90,000 | 930,000 | 339,900 | 150,000 | 440,100 |
| Q2 | 400 | 1,300 | 1,120,000 | 130,000 | 1,250,000 | 453,200 | 175,000 | 621,800 |
| Q3 | 400 | 1,700 | 1,120,000 | 170,000 | 1,290,000 | 453,200 | 175,000 | 661,800 |
| Q4 | 400 | 2,100 | 1,120,000 | 210,000 | 1,330,000 | 453,200 | 200,000 | 676,800 |
| **Y3** | **1,500** | **2,100** | **4,200,000** | **600,000** | **4,800,000** | **1,699,500** | **700,000** | **2,400,500** |

Unit cost at P1,133 (500+ scale). Price adjusted to P2,800 (coop volume discount).

### 3-Year Summary

| | Year 1 | Year 2 | Year 3 | Total |
|---|--------|--------|--------|-------|
| Units Sold | 100 | 500 | 1,500 | 2,100 |
| Hardware Revenue | 300,000 | 1,500,000 | 4,200,000 | 6,000,000 |
| Lure Revenue | 19,500 | 153,000 | 600,000 | 772,500 |
| **Total Revenue** | **319,500** | **1,653,000** | **4,800,000** | **6,772,500** |
| COGS | 78,910 | 737,500 | 1,699,500 | 2,515,910 |
| OpEx | 48,000 | 305,000 | 700,000 | 1,053,000 |
| **Net Income** | **192,590** | **610,500** | **2,400,500** | **3,203,590** |

---

## 3. BREAK-EVEN ANALYSIS

### Monthly Fixed Costs (Post-Launch)

| Item | Monthly (P) |
|------|------------|
| Lure inventory holding | 2,000 |
| Transport/logistics | 3,000 |
| Marketing materials | 2,000 |
| Miscellaneous | 1,000 |
| **Total Fixed** | **P8,000/month** |

### Contribution per Unit

| | Revenue | Variable Cost | Contribution |
|---|---------|--------------|-------------|
| Device | P3,000 | P1,475 | P1,525 |
| Lure (x4/year) | P400 | P180 | P220 |

### Break-Even Point

Startup investment: P78,910 (COGS) + P48,000 (OpEx months 1-9) = **P126,910**

Break-even units: P126,910 / P1,525 = **84 devices**

At projected sales (30-35/month from month 10): **break-even in Month 12.**

---

## 4. STARTUP COSTS AND FUNDING

### Phase 1: Prototype + Pilot (Months 1-8)

| Item | Cost (P) |
|------|----------|
| 2 prototypes | 3,960 |
| Lures for pilot (20) | 2,000 |
| SIM cards + load (4 months) | 1,200 |
| Transport to farms | 6,000 |
| Printing | 1,500 |
| Misc | 1,340 |
| **Subtotal** | **P16,000** |

### Phase 2: First Production (Month 9)

| Item | Cost (P) |
|------|----------|
| 100 units (P1,475 x 100) | 147,500 |
| Lure inventory (500 lures) | 22,500 |
| Packaging + labels | 5,000 |
| Marketing | 10,000 |
| Working capital buffer | 15,000 |
| **Subtotal** | **P200,000** |

### **Total Funding Need: P216,000**

---

## 5. FUNDING SOURCES

### A. DOST-SETUP
- Up to P500,000 for tech-based startups
- Apply through DOST Region IV-B (MIMAROPA)
- 2-4 month process
- Strong fit: IoT agricultural device

### B. DOST-PCIEERD
- P200,000-2,000,000 for R&D
- Apply through MinSU research office
- Annual calls, 3-6 month review
- Excellent fit: IoT + agriculture + pest management

### C. DA-BAR (Bureau of Agricultural Research)
- P100,000-1,000,000+ for agri-tech R&D
- Submit through university or regional DA
- Quarterly calls
- Direct fit: pest management for priority crop

### D. Competitions

| Program | Prize Range (P) | Notes |
|---------|----------------|-------|
| MinSU Technopreneurship Fair | 5,000-20,000 | Your class may have this |
| DOST-TAPI Invention Contest | 50,000-200,000 | Agriculture category |
| Go Negosyo ASEAN Youth | 100,000+ | Young entrepreneur program |
| IdeaSpace | 500,000-1,000,000 | Major PH accelerator (equity) |
| Villgro Philippines | Incubation + funding | Social enterprise, agri focus |
| QBO Innovation Hub | Mentoring + network | Accepts provincial startups |

### E. Pre-Sales
- P2,500 early-bird price, P500 deposit
- 20 pre-orders from pilot farmers/network = P50,000 working capital

---

## 6. SENSITIVITY ANALYSIS

### A: Price Sensitivity

| Price | Margin/Unit | Break-Even | Y1 Net | Y3 Net |
|-------|-------------|-----------|--------|--------|
| P3,500 | P2,025 (58%) | 63 units | 242,590 | 2,950,500 |
| **P3,000** | **P1,525 (51%)** | **84** | **192,590** | **2,400,500** |
| P2,500 | P1,025 (41%) | 124 | 142,590 | 1,262,500 |
| P2,000 | P525 (26%) | 242 | 67,590 | 412,500 |

Below P2,000 = not sustainable.

### B: Sales Volume Sensitivity

| Pace | Y1 Units | Y1 Net | Break-Even Month |
|------|----------|--------|-----------------|
| 1.5x (fast) | 150 | 317,840 | 11 |
| **1x (base)** | **100** | **192,590** | **12** |
| 0.5x (slow) | 50 | 32,840 | 15 |
| 0.25x (very slow) | 25 | -47,035 | 20 |

Half-pace still profitable Y1. Quarter-pace needs bridge funding.

### C: Component Cost Increase

| BOM Change | Unit Cost | Margin at P3,000 | Break-Even |
|-----------|-----------|-------------------|-----------|
| Base | P1,475 | 51% | 84 |
| +20% | P1,770 | 41% | 104 |
| +50% | P2,213 | 26% | 162 |
| +100% | P2,950 | 2% | 2,538 |

Can absorb 20% increase. At 50%, raise price to P3,500.

### D: Lure Supply Disruption

| Situation | Mitigation |
|-----------|-----------|
| India delays 2-4 weeks | Keep 2-month buffer inventory |
| Import cost doubles | Raise lure price to P150 (still cheap vs pesticide) |
| Import blocked | Partner UPLB/DA for local synthesis |

### E: 3-Year Scenario Range

| | Worst | Base | Best |
|---|-------|------|------|
| Y1 units | 25 | 100 | 200 |
| Y3 cumulative | 500 | 2,100 | 5,000 |
| Y3 revenue | 800,000 | 4,800,000 | 12,000,000 |
| 3-year net | 250,000 | 3,203,590 | 9,500,000 |

**Even worst case: viable small business. Best case: real company.**

---

## 7. KEY ASSUMPTIONS

| # | Assumption | Value | Basis |
|---|-----------|-------|-------|
| 1 | Price | P3,000 (Y1-2), P2,800 (Y3) | Interview WTP target |
| 2 | BOM at scale | P1,475 (50+), P1,133 (500+) | Component pricing research |
| 3 | Lures/unit/year | 4 | 30-45 day lifespan, 2 seasons |
| 4 | Lure cost | P45 each | IndiaMART bulk |
| 5 | Monthly OpEx post-launch | P8,000 | Transport, marketing, SIM |
| 6 | Failure/return rate | 5% | Industry average |
| 7 | Lure repurchase rate | 80% Y2, 70% Y3 | Conservative |
| 8 | Founder salary Y1 | P0 | Student sweat equity |
| 9 | Assembly labor | P100-150/unit | Local, manual |
| 10 | SMS cost | P0.50/alert | Globe/Smart standard |
