# Phase 3: Deep Dive — Smart Eggplant Borer Trap ("TalongGuard")
**2026-09-12 | Loop Turn 2**

---

## 1. THE PROBLEM (Research-Backed)

### The Pest
**Eggplant Fruit and Shoot Borer (EFSB)** — *Leucinodes orbonalis* Guenée
- Female moths lay eggs on eggplant leaves/fruits at night
- Larvae bore INTO fruit within hours of hatching — invisible from outside
- By the time farmer sees damage, fruit is reject-grade
- **The core problem: detection happens too late**

### The Damage (Philippines-specific)
- Eggplant = **#1 vegetable crop in PH**: 21,225 hectares, 248,000 MT/year
- Production value: **₱1.027 billion** (2024)
- EFSB causes **51-80% yield loss** at high pest pressure
- Farmers spray **up to 80 times per cropping season**
- Pesticide cost = **20-40% of total production cost**
- National annual loss from EFSB: **₱33.85 billion**

### What Farmers Do Now (All Bad)
1. **Calendar spraying** — spray every 2-3 days regardless of pest presence. Wasteful, expensive, health hazard.
2. **Wait and see** — spot damage when fruit is already bored. Too late.
3. **Nothing** — accept losses, sell at reject prices.
4. **Manual pheromone traps** — exist but nobody counts moths systematically. No threshold-based decision-making.

### The Insight
Adult EFSB moths are **attracted to sex pheromone lures** (E-11-hexadecenyl acetate & E-11-hexadecenol). The **Economic Threshold Level is 6-8 moths/trap/night**. Above that = spray NOW. Below = don't waste money.

**Nobody is giving farmers this data in real-time.**

---

## 2. THE SOLUTION: TalongGuard

**Smart pheromone trap with automated moth counting + threshold alerts.**

### How It Works
1. Pheromone lure attracts male EFSB moths into funnel trap
2. IR break-beam sensor counts each moth entering
3. ESP32 logs count per night, compares to threshold (6-8)
4. If threshold exceeded → SMS alert to farmer: "SPRAY TODAY"
5. If below threshold → "NO SPRAY NEEDED, SAVE YOUR MONEY"
6. Data logged over time → seasonal pest pressure trends

### Key Value Proposition
**"Stop guessing, start knowing. Spray only when you need to."**
- Reduces pesticide spraying by 50-70% (only spray when threshold hit)
- Saves ₱10,000-25,000 per hectare per season in pesticide costs
- Protects farmer health (less chemical exposure)
- Produces data for better farming decisions

---

## 3. CUSTOMER PERSONA

### Primary: "Mang Tonyo"
- **Who:** Male, 45-55, smallholder eggplant farmer in Mindoro
- **Farm:** 0.5-2 hectares of eggplant
- **Income:** ₱80,000-200,000/year from eggplant (gross)
- **Pain:** Spends ₱20,000-50,000/season on pesticides. Still loses 30-50% of crop.
- **Tech comfort:** Has Android phone (budget model). Uses Facebook, Messenger. Can read SMS.
- **Decision trigger:** "If I can save more on pesticide than the device costs, I'll try it."

### Secondary: Agricultural Extension Workers (AEWs)
- **Who:** DA/LGU agricultural technicians assigned to barangays
- **Need:** Data to justify IPM recommendations to farmers
- **Value:** TalongGuard gives them actual pest population data to show farmers

### Tertiary: Cooperatives / Farmer Organizations
- **Who:** Eggplant farmer coops buying inputs collectively
- **Need:** Reduce collective pesticide spend
- **Value:** Bulk purchase of TalongGuard units, shared dashboard

---

## 4. COMPETITIVE LANDSCAPE

| Competitor | What They Offer | Price | Gap |
|-----------|----------------|-------|-----|
| Manual pheromone traps | Trap + lure, farmer counts manually | ₱200-500/trap | No automation, nobody counts consistently |
| Bt Eggplant (UPLB) | Genetically modified resistant variety | Free (trial) | Regulatory delays, farmer distrust of GMO |
| Plantix / AI pest apps | Phone camera pest ID | Free | Detects DAMAGE, not incoming moths. Too late. |
| Commercial smart traps (Trapview, iScout) | Camera + AI + cloud | $850-1,000+ (~₱48-56k) | Way too expensive for Filipino smallholders |
| Calendar spraying | Spray every 2-3 days | ₱20-50k/season | Wasteful, unhealthy, expensive |

### TalongGuard's Position
- **Cheaper than commercial smart traps** by 10-20x
- **Smarter than manual traps** — automated counting + alerts
- **Earlier than pest ID apps** — catches moths BEFORE they lay eggs
- **Cheaper than calendar spraying** — device pays for itself in one season

**No direct competitor exists at this price point with this functionality in the Philippines.**

---

## 5. MVP FEATURE SET

### Must-Have (v1.0)
- [ ] ESP32 + IR break-beam moth counter
- [ ] Pheromone lure holder (standard funnel trap design)
- [ ] Nightly count logged to onboard memory
- [ ] SMS alert when threshold exceeded (via SIM800L GSM module)
- [ ] Solar panel + 18650 battery for field power
- [ ] 3D-printed weatherproof enclosure
- [ ] Simple setup: farmer places in field, turns on, done

### Nice-to-Have (v1.5)
- [ ] Companion mobile app (view count history, trends)
- [ ] Multiple trap data aggregation per farm
- [ ] Weather correlation (temp/humidity sensor add-on)
- [ ] Adjustable threshold via app

### Future (v2.0)
- [ ] Camera module for moth species verification (avoid false counts)
- [ ] LoRa mesh for multi-field coverage without cell signal
- [ ] Dashboard for agricultural extension workers
- [ ] Swappable lure system for other pests (different crops)

---

## 6. BILL OF MATERIALS (BOM) — Prototype

| Component | Unit Cost (₱) | Source |
|-----------|---------------|--------|
| ESP32 DevKit V1 | 350 | Shopee/Lazada |
| IR break-beam sensor pair (3mm) | 120 | Shopee |
| SIM800L GSM module | 280 | Shopee |
| 5V solar panel (1W) | 250 | Shopee |
| 18650 battery + TP4056 charger | 180 | Shopee |
| Funnel trap body (3D printed) | 200 | JLC3DP / university lab |
| Pheromone lure (L. orbonalis) | 100 | Import from India (IndiaMART) |
| Weatherproof housing | 150 | 3D printed |
| PCB (custom, optional) | 200 | JLCPCB |
| Wires, connectors, misc | 150 | Local electronics shop |
| **TOTAL per prototype** | **~₱1,980** | |
| **TOTAL for 2 prototypes** | **~₱3,960** | **Under ₱5k budget ✓** |

### Production Cost (at scale, 50+ units)
Estimated ₱1,200-1,500 per unit with bulk component purchase and JLC PCB assembly.

### Selling Price Target
**₱2,500-3,500 per unit** (50-100% margin)

### Customer ROI
- Device cost: ₱3,000 (one-time)
- Pheromone refills: ₱100/lure × 3-4 lures/season = ₱300-400/season
- Pesticide savings: ₱10,000-25,000/season
- **Payback period: LESS THAN ONE SEASON**
- Lure refills = recurring revenue stream

---

## 7. LEAN CANVAS

```
┌─────────────────────────────────────────────────────────────────────┐
│                        TALONGGUARD LEAN CANVAS                      │
├──────────────────┬──────────────────┬───────────────────────────────┤
│ PROBLEM          │ SOLUTION         │ UNIQUE VALUE PROPOSITION      │
│                  │                  │                               │
│ 1. EFSB causes   │ 1. Smart phero-  │ "Spray only when you need to."│
│    51-80% crop   │    mone trap w/  │                               │
│    loss          │    auto moth     │ First affordable IoT pest     │
│                  │    counter       │ monitoring for Filipino        │
│ 2. Farmers spray │                  │ smallholder eggplant farmers. │
│    up to 80x/    │ 2. SMS alert     │                               │
│    season blind  │    when pest     │ Saves ₱10-25k/season in       │
│                  │    threshold hit │ pesticide costs.              │
│ 3. No affordable│                  │                               │
│    monitoring    │ 3. Solar powered │                               │
│    tool exists   │    field device  │                               │
├──────────────────┤                  ├───────────────────────────────┤
│ KEY METRICS      │                  │ UNFAIR ADVANTAGE              │
│                  │                  │                               │
│ • Units deployed │                  │ • ABE domain knowledge        │
│ • Pest alerts    │                  │ • First mover in PH at this   │
│   sent/month     │                  │   price point                 │
│ • Pesticide cost │                  │ • Hardware + consumables moat │
│   reduction (%)  │                  │ • Field data from Mindoro     │
│ • Farmer         │                  │   pilot = hard to replicate   │
│   retention rate │                  │                               │
├──────────────────┼──────────────────┼───────────────────────────────┤
│ CHANNELS         │ CUSTOMER         │ EARLY ADOPTERS                │
│                  │ SEGMENTS         │                               │
│ 1. DA extension  │                  │ • Eggplant farmers you        │
│    workers       │ 1. Smallholder   │   already interviewed         │
│ 2. Farmer coops  │    eggplant      │ • Mindoro eggplant coops      │
│ 3. Agri-supply   │    farmers       │ • DA-MinSU extension program  │
│    stores        │    (0.5-2 ha)    │   farmers                     │
│ 4. Demo at       │                  │                               │
│    municipal     │ 2. Agri          │                               │
│    agri fairs    │    extension     │                               │
│                  │    offices       │                               │
├──────────────────┼──────────────────┼───────────────────────────────┤
│ COST STRUCTURE                      │ REVENUE STREAMS               │
│                                     │                               │
│ • BOM per unit: ₱1,200-1,500       │ • Hardware sales: ₱2,500-3,500│
│ • Pheromone lure sourcing           │   per unit                    │
│ • SMS costs (₱0.50/alert)          │ • Pheromone lure refills:      │
│ • Assembly labor                    │   ₱100/lure, 3-4x/season     │
│ • Packaging & distribution          │ • Bulk/coop packages          │
│ • Marketing (mostly free: demos)    │ • Future: data analytics sub  │
└─────────────────────────────────────┴───────────────────────────────┘
```

---

## 8. RISKIEST ASSUMPTIONS (Must Validate)

| # | Assumption | Risk Level | How to Validate |
|---|-----------|-----------|-----------------|
| 1 | IR break-beam accurately counts moths (not other insects, not double-counts) | **HIGH** | Build prototype, test in field with manual verification |
| 2 | Farmers will act on SMS alerts (change spraying behavior) | **HIGH** | Pilot with 3-5 interviewed farmers, track behavior |
| 3 | Pheromone lures can be sourced affordably in PH | **MEDIUM** | Contact Indian suppliers, check import logistics + cost |
| 4 | Solar + battery lasts through cloudy/rainy season | **MEDIUM** | Power consumption test in lab, size panel appropriately |
| 5 | ₱2,500-3,500 price point is acceptable to farmers | **MEDIUM** | Ask interviewed farmers directly: "Would you pay ₱3k to save ₱15k?" |
| 6 | Device survives outdoor conditions (rain, heat, dust) | **MEDIUM** | Weatherproofing test over 2-4 weeks in field |
| 7 | Cell signal available in eggplant fields for SMS | **LOW** | You already said signal is "tolerable" in Mindoro |

---

## 9. SOURCES

- [PSA Eggplant Statistics](https://psa.gov.ph/vegetable-root-crops/eggplant)
- [Bt Eggplant Field Performance — PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0157498)
- [₱33.85B Annual Loss from EFSB — ISAAA](https://www.isaaa.org/blog/entry/default.asp?BlogDate=2/3/2021)
- [UPLB CAFS Bt Eggplant](https://cafs.uplb.edu.ph/bt-eggplant/)
- [IoT Pest Monitoring — Nature Scientific Reports](https://www.nature.com/articles/s41598-024-83012-3)
- [Pheromone Lure Pricing — IndiaMART](https://www.indiamart.com/proddetail/leucinodes-orbonalis-brinjal-fruit-shoot-borer-pheromone-lure-bsfb-22240728173.html)
- [EFSB Pheromone Trap Studies — BanglaJOL](https://www.banglajol.info/index.php/JBS/article/view/8768)
- [YOLO-Pest Smart Trap — Nature](https://www.nature.com/articles/s41598-025-97825-3)
- [ESP32 Object Counter — ElectronicClinic](https://www.electroniclinic.com/object-counter-with-ir-sensor-oled-display-using-esp32/)
