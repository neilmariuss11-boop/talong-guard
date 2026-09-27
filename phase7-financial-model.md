# Phase 7: Financial Model — Autodissemination Station
**Rewritten 2026-09-27** (replaces the eggplant ESP32 monitoring-trap model)

> All figures in Philippine pesos (₱). US$1 ≈ ₱58; ₹1 ≈ ₱0.68 (Sept 2026 assumption).
> Sources for market and cost inputs: `research-synthesis.md` [R#]. The numbers were computed with a script so the totals are consistent. Change an assumption in §8 and recompute every table that depends on it.

---

## 1. UNIT ECONOMICS

### 1.1 Products

| Product | Price | COGS | Gross margin | Margin % |
|---|---|---|---|---|
| Station (one-time) | ₱690 | ₱285 | ₱405 | 58.7% |
| Season Kit (per Station per season: 3 lures + 6 cartridges) | ₱520 | ₱330 | ₱190 | 36.5% |
| **Station + first Kit** | ₱1,210 | ₱615 | **₱595** | 49.2% |

### 1.2 COGS build-up
- **Station ₱285:** materials ₱235 + labor ₱50 (BOM in `phase5-device-design.md` §4.1; batch of 100).
- **Season Kit ₱330:** 3 lures × ₱60 (landed) + 6 cartridges × ₱20 + ₱30 packaging, gloves and instructions.
- **Cartridge ₱20:** conidia 2 g ₱4, velvet ₱7, PET ₱2, foil ₱3, silica ₱2, label and labor ₱2.
- **Lure ₱60 landed:** Indian list price ₹25 ≈ ₱17 [R23] + international shipping, customs and broker fees for a small order, spread over ~300 lures. **This is the most uncertain cost. Get 2 real quotes in October.**

### 1.3 Farmer economics (per hectare, 4 Stations/ha)

| Item | Value |
|---|---|
| First-season cost | 4 × ₱1,210 = **₱4,840/ha** |
| Following seasons | 4 × ₱520 = **₱2,080/ha** |
| Onion gross value/ha | 9.06 t/ha [R36] × ₱30/kg (Feb 2026 glut price [R20]) = **₱271,800** |
| Kit cost as % of gross | **0.77%** |
| First season as % of gross | **1.78%** |
| Production cost/ha (reference) | ₱200,000–300,000 [R20] → the kit is 0.7–1.0% of production cost |
| Break-even | Prevent **≥0.77%** yield loss, OR save the cost of about 1 insecticide application (to confirm in interviews) |
| Downside reference | Outbreak-year inputs ≈ ₱400,000/ha, still losing about half the crop [R21] |

At a normal farmgate price of ₱60–80/kg, gross value doubles or more and the kit becomes about 0.4% of it.

### 1.4 Customer lifetime value (1 hectare = 4 Stations, 3 seasons, 80% season-to-season retention)
- Seasons of kit purchases = 1 + 0.8 + 0.64 = 2.44
- **Lifetime revenue** = 4 × ₱690 + 4 × ₱520 × 2.44 = **₱7,835**
- **Lifetime gross margin** = 4 × ₱405 + 4 × ₱190 × 2.44 = **₱3,474**
- **Target customer acquisition cost** (field days, visits, demo units): ≤ ₱1,000/ha, giving LTV/CAC ≥ 3.5.

---

## 2. YEAR 1 (Oct 2026 – Sep 2027): PILOT, MONTHLY CASH PLAN

**Assumptions:**
- 100 Stations + 100 Kits built (Nov–Dec).
- **40 Stations go to core demo farms free** (10 ha).
- **60 Stations are sold as hardware only** to "cooperator" farmers (15 ha): 20 in Jan and 40 in Feb.
- **No cartridges are sold in the demonstration season** (FPA; `proposal.md` §9.2). Cooperators receive lures and cartridges free as demonstration materials, so all 100 Kits are a cost with no revenue in Year 1.
- ₱180,000 external funding received in October.

| Month | Revenue | COGS | Fixed | Net | Cash balance |
|---|---|---|---|---|---|
| Oct 2026 | 0 | 0 | 26,000 | −26,000 | 154,000 |
| Nov | 0 | 30,750 | 27,500 | −58,250 | 95,750 |
| Dec | 0 | 30,750 | 17,000 | −47,750 | 48,000 |
| Jan 2027 | 13,800 | 0 | 17,500 | −3,700 | 44,300 |
| Feb | 27,600 | 0 | 25,500 | 2,100 | 46,400 |
| Mar | 0 | 0 | 14,500 | −14,500 | 31,900 |
| Apr | 0 | 0 | 11,000 | −11,000 | 20,900 |
| May | 0 | 0 | 7,000 | −7,000 | 13,900 |
| Jun | 0 | 0 | 1,000 | −1,000 | 12,900 |
| Jul | 0 | 0 | 1,000 | −1,000 | 11,900 |
| Aug | 0 | 0 | 1,000 | −1,000 | 10,900 |
| Sep | 0 | 0 | 1,000 | −1,000 | **9,900** |
| **Total** | **41,400** | **61,500** | **150,000** | **−170,100** | **9,900** |

**Year-1 fixed costs (₱150,000):**

| Category | Amount | Timing |
|---|---|---|
| Prototyping and jigs | 11,500 | Oct–Nov |
| Lab and partner QC | 18,500 | Oct–Apr |
| Field logistics (Victoria ↔ San Jose) | 35,000 | Oct–Apr |
| Temp/RH loggers, field tools | 6,000 | Nov |
| Field day and marketing | 18,000 | Jan–May (Feb field day ₱10,000) |
| Regulatory, IP, DTI registration | 11,000 | Oct–Nov, Apr–May |
| Communications and team field allowance | 20,000 | Monthly |
| Lure samples and import/customs fees | 10,000 | Oct–Nov |
| Contingency | 20,000 | Dec–Mar |

**If there are no Year-1 hardware sales:** cash would go to −₱31,500. Mitigations:
- (a) Build only the 40 demo units (saves ~₱36,900 in COGS).
- (b) Secure LGU in-kind transport.
- (c) Raise a ₱30k top-up (competition prize or MinSU fund).

---

## 3. THREE-YEAR PROJECTION (base case)

**Volume drivers:**

| | Year 1 (2026–27) | Year 2 (2027–28) | Year 3 (2028–29) |
|---|---|---|---|
| New hectares | 25 (10 demo free) | 150 | 500 |
| Stations built | 100 | 600 | 2,000 |
| Stations sold | 60 (hardware only) | 600 | 2,000 |
| Kits built/sold | 100 / **0** (demo materials, not sold) | 680 / 680 (600 new + 80 returning) | 2,544 / 2,544 (2,000 new + 544 returning) |
| Cartridges produced | 600 | 4,080 | 15,264 |
| Dry conidia needed (2 g each) | 1.2 kg | 8.2 kg | 30.5 kg |
| Rice substrate (at ~30 g conidia/kg; assumption) | ~40 kg | ~270 kg | ~1,020 kg |
| Lures | 300 | 2,040 | 7,632 |

**Profit and loss:**

| | Year 1 | Year 2 | Year 3 |
|---|---|---|---|
| Station revenue | 41,400 | 414,000 | 1,380,000 |
| Kit revenue | 0 | 353,600 | 1,322,880 |
| **Total revenue** | **41,400** | **767,600** | **2,702,880** |
| Station COGS | 28,500 | 171,000 | 570,000 |
| Kit COGS | 33,000 | 224,400 | 839,520 |
| **Gross profit** | **−20,100** | **372,200** (48.5%) | **1,293,360** (47.9%) |
| Fixed costs | 150,000 | 420,000 | 900,000 |
| **Net income** | **−170,100** | **−47,800** | **+393,360** |
| Cumulative | −170,100 | −217,900 | **+175,460** |

**Year-2 fixed costs (₱420,000):**
- 2 part-time staff (production technician, field/sales) at ₱10,000/month each: ₱240,000
- Lab space and utilities: ₱48,000
- Transport and logistics: ₱60,000
- Marketing and field days: ₱30,000
- FPA biorational dossier preparation: ₱30,000
- Admin, permits, accounting: ₱12,000

**Year-3 fixed costs (₱900,000):**
- 2 full-time staff at ₱18,000/month: ₱432,000
- 1 part-time staff: ₱120,000
- Lab, storage and cold storage: ₱96,000
- Transport: ₱96,000
- Marketing: ₱60,000
- FPA registration fees and testing: ₱60,000
- Admin and accounting: ₱36,000

*Taxes are not modeled. A BMBE-registered micro-enterprise (Barangay Micro Business Enterprise, under RA 9178) is exempt from income tax. Confirm eligibility.*

---

## 4. BREAK-EVEN

- **Contribution per new hectare** (4 Stations + 4 Kits): 4 × ₱595 = **₱2,380**
- **Contribution per returning hectare** (4 Kits): 4 × ₱190 = **₱760**
- **Year-3 fixed costs ₱900,000:** break-even ≈ **378 new hectares** a year (with no returning customers), or fewer with returning ones.
- **Year-2 fixed costs ₱420,000:** break-even ≈ 176 new ha; the plan has 150 new + 20 returning, which is why Year 2 is slightly negative.
- **Cumulative payback:** during Year 3.

---

## 5. SENSITIVITY (Year-3 net income)

| Scenario | Revenue | Net income | Reading |
|---|---|---|---|
| Base | ₱2,702,880 | **₱393,360** | — |
| Prices −20% (Station ₱552, Kit ₱416) | ₱2,162,304 | −₱147,216 | Don't discount; sell value |
| Volume −30% | ₱1,892,120 | ₱5,390 | Survives, barely |
| Volume +50% (one LGU bulk order) | ₱4,054,320 | ₱1,040,040 | B2G is the upside lever |
| Lure landed cost ×2 (₱120) | ₱2,702,880 | −₱64,560 | Lure cost is critical |
| **US-retail lure (₱215)** | ₱2,702,880 | **−₱789,600** | **Never buy retail US lures at scale** |
| Cartridge cost ×2 (₱40) | ₱2,702,880 | ₱88,080 | Tolerable |
| Volume −30% AND lure ×2 | ₱1,892,120 | −₱315,190 | Worst plausible case |

**Kit price needed if lures can only be bought at ₱215:** even at ₱760/Kit, Year 3 is −₱179,040. The model **needs Asian-sourced lures or a local distributor price ≤ ₱100**.

**Levers, in order of power:**
1. Lure cost.
2. Institutional volume.
3. Price discipline.
4. Cartridge cost.

---

## 6. FUNDING AND SOURCES

| Stage | Need | Source |
|---|---|---|
| Year 1 pilot | ₱180,000 | Class or MinSU funds; business plan competitions; LGU in-kind (transport, farmer mobilization) |
| Year 2 working capital | ~₱100,000 buffer (cumulative low −₱217,900 before pre-order deposits) | Pre-order deposits (₱200/Station), LGU purchase orders, DOST-TAPI TECHNiCOM [R31] |
| Year 2–3 scale-up (lab, cold storage, registration) | ₱1–5 M | **DOST-TAPI TECHNiCOM (≤₱5 M; academic institutions eligible)**; CHED-DOST ATBI (₱5 M, if MinSU has an incubator); DOST-PCAARRD Startup Grant Fund (≤₱5 M; needs a startup operating 1–5 years) [R31] |

---

## 7. MARKET VALUE CHECK (top-down)

| Area | Hectares | Stations (4/ha) | One-time device value | Kit value per season |
|---|---|---|---|---|
| San Jose, Occ. Mindoro | 3,285 [R19] | 13,140 | ₱9.07 M | ₱6.83 M |
| Occidental Mindoro | 8,637 [R18] | 34,548 | ₱23.84 M | ₱17.96 M |
| Bongabon, Nueva Ecija | ~4,589 | 18,356 | ₱12.67 M | ₱9.55 M |
| Nueva Ecija | ~11,500 [R36] | 46,000 | ₱31.74 M | ₱23.92 M |

Year-3 plan = ~636 ha in service = **7.4% of Occidental Mindoro**.

---

## 8. KEY ASSUMPTIONS (change these first when real data arrives)

| # | Assumption | Value | Confidence | How to firm it up |
|---|---|---|---|---|
| 1 | Stations per hectare | 4 | LOW | Demo: 2 vs 4/ha |
| 2 | Station price | ₱690 | MEDIUM | Interview price ladder (`phase6`) |
| 3 | Season Kit price | ₱520 | MEDIUM | Same |
| 4 | Lure landed cost | ₱60 | **LOW** | 2 supplier quotes (India + Verca) |
| 5 | Lures per season | 3 (4-week life) | MEDIUM | Vendor data [R23]; heat may shorten it |
| 6 | Cartridges per season | 6 (14-day swap) | MEDIUM | Field germination test (`phase5` §7.2) |
| 7 | Conidia per cartridge | 2 g | LOW | Bench pickup test |
| 8 | Conidia yield | 30 g/kg rice | LOW | First production batches |
| 9 | Retention season to season | 80% | LOW | Pre-order sheet after the demo |
| 10 | Onion yield / price | 9.06 t/ha; ₱30/kg | MEDIUM | MAO data for San Jose |
| 11 | Year-3 new hectares | 500 | LOW | Depends on the demo and an LGU order |
| 12 | Labor cost | ₱120/h | MEDIUM | — |
