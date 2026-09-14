# Phase 5: Technical Architecture — TalongGuard v1.0
**2026-09-12 | Loop Turn 4**

---

## 1. SYSTEM BLOCK DIAGRAM

```
                        ┌─────────────────────┐
                        │    SOLAR PANEL 5V    │
                        │    (1W, 5V/200mA)    │
                        └──────────┬──────────┘
                                   │ 5V
                        ┌──────────▼──────────┐
                        │   TP4056 CHARGE      │
                        │   CONTROLLER         │
                        │   + DW01 PROTECTION  │
                        └──────────┬──────────┘
                                   │ 3.7V
                        ┌──────────▼──────────┐
                        │   18650 Li-Ion       │
                        │   BATTERY (3400mAh)  │
                        └──────────┬──────────┘
                                   │ 3.7V
              ┌────────────────────▼────────────────────┐
              │                                         │
              │            ESP32 DevKit V1              │
              │          (Main Controller)              │
              │                                         │
              │  GPIO 14 ◄── IR Break-Beam RX           │
              │  GPIO 27 ──► IR Break-Beam TX (emitter) │
              │  GPIO 16 ──► SIM800L TX (RX on module)  │
              │  GPIO 17 ◄── SIM800L RX (TX on module)  │
              │  GPIO 2  ──► Status LED                 │
              │  GPIO 4  ──► Buzzer (optional)          │
              │  ADC (VP) ◄── Battery voltage divider   │
              │                                         │
              └──────┬──────────────────┬───────────────┘
                     │                  │
          ┌──────────▼──────┐   ┌───────▼──────────┐
          │  IR BREAK-BEAM  │   │    SIM800L GSM    │
          │  SENSOR PAIR    │   │    MODULE         │
          │                 │   │                   │
          │  TX ─── ))) ────│   │  ┌─────────────┐ │
          │  RX ◄── moth ───│   │  │ SIM CARD    │ │
          │  (3mm gap in    │   │  │ (prepaid)   │ │
          │   trap funnel)  │   │  └─────────────┘ │
          └─────────────────┘   └──────────────────┘
                                        │
                                   SMS alerts
                                        │
                                ┌───────▼───────┐
                                │  FARMER'S     │
                                │  PHONE        │
                                │  (any phone   │
                                │   with SMS)   │
                                └───────────────┘
```

---

## 2. CIRCUIT CONNECTION MAP

### ESP32 Pin Assignments

| ESP32 Pin | Direction | Connected To | Purpose |
|-----------|-----------|-------------|---------|
| GPIO 14 | INPUT (PULLUP) | IR Receiver OUT | Moth detection (interrupt-driven) |
| GPIO 27 | OUTPUT | IR Emitter Anode (via 100R) | IR beam source |
| GPIO 16 (TX2) | OUTPUT | SIM800L RXD | Serial data to GSM module |
| GPIO 17 (RX2) | INPUT | SIM800L TXD | Serial data from GSM module |
| GPIO 2 | OUTPUT | LED (via 220R) | Status indicator |
| GPIO 4 | OUTPUT | Buzzer + (via NPN transistor) | Audible alert (optional) |
| GPIO 36 (VP) | ADC INPUT | Voltage divider (100k/100k) from battery | Battery level monitoring |
| 3V3 | POWER | IR Receiver VCC | 3.3V supply |
| GND | GROUND | All grounds | Common ground |

### SIM800L Power Note
SIM800L draws **2A peak** during transmission. Cannot power from ESP32 3.3V pin directly.
- **Recommended:** Power SIM800L from battery (3.7-4.2V) through dedicated connection (SIM800L accepts 3.4-4.4V)
- Add **1000uF electrolytic capacitor** on SIM800L VCC to absorb current spikes

### Wiring Diagram (Text)

```
BATTERY 3.7V ──┬── TP4056 BAT+ ◄── SOLAR 5V+
               │
               ├── SIM800L VCC (direct, 3.7V within spec)
               │
               ├── ESP32 VIN (regulated internally to 3.3V)
               │
               └── Voltage divider ──► GPIO 36
                   100k ┬ 100k ┬ GND
                        └─────► ADC reads half battery voltage

ESP32 GPIO 27 ── 100R ── IR LED Anode ── IR LED Cathode ── GND
ESP32 GPIO 14 ◄── IR Phototransistor Collector
                  IR Phototransistor Emitter ── GND
                  10k pullup from GPIO 14 to 3.3V

ESP32 GPIO 16 ──── SIM800L RXD
ESP32 GPIO 17 ◄─── SIM800L TXD
GND ──────────────── SIM800L GND
```

---

## 3. FIRMWARE LOGIC FLOWCHART

```
                    ┌──────────────┐
                    │   POWER ON   │
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  INIT:       │
                    │  - GPIO setup│
                    │  - RTC init  │
                    │  - Load count│
                    │    from SPIFFS│
                    │  - Check batt│
                    └──────┬───────┘
                           │
                    ┌──────▼───────┐
                    │  CHECK TIME  │◄─────────────────────┐
                    │  (RTC)       │                      │
                    └──────┬───────┘                      │
                           │                              │
                ┌──────────▼──────────┐                   │
                │  Is it NIGHT?       │                   │
                │  (6:00 PM - 5:59 AM)│                   │
                └──┬──────────────┬───┘                   │
                   │ YES          │ NO                    │
                   │              │                       │
          ┌────────▼────────┐  ┌──▼───────────────┐      │
          │  ACTIVE MODE    │  │  DAYTIME:         │      │
          │                 │  │                   │      │
          │  Enable IR beam │  │  Is it 6:00 AM?   │      │
          │  Attach HW      │  │  (report time)    │      │
          │   interrupt on  │  └──┬────────────┬───┘      │
          │   GPIO 14       │     │ YES        │ NO       │
          │                 │     │            │          │
          │  On interrupt:  │  ┌──▼──────────┐ │          │
          │  - debounce     │  │ SEND REPORT │ │          │
          │    (50ms)       │  │             │ │          │
          │  - increment    │  │ moth_count  │ │          │
          │    moth_count   │  │ >= THRESHOLD│ │          │
          │  - save to      │  │ (6-8)?     │ │          │
          │    SPIFFS every │  └──┬───────┬──┘ │          │
          │    10 counts    │     │YES    │NO  │          │
          │                 │     │       │    │          │
          │  Light-sleep    │  ┌──▼────┐┌─▼──┐ │          │
          │  between moths  │  │ SMS:  ││SMS:│ │          │
          │  (wake on GPIO  │  │"SPRAY ││"OK │ │          │
          │   interrupt)    │  │ TODAY"││safe"│ │          │
          │                 │  │+count ││+cnt│ │          │
          └────────┬────────┘  └──┬────┘└─┬──┘ │          │
                   │              │       │    │          │
                   │              ├───────┘    │          │
                   │              │            │          │
                   │           ┌──▼──────────┐ │          │
                   │           │ RESET COUNT  │ │          │
                   │           │ moth_count=0 │ │          │
                   │           │ Save to SPIFFS│ │          │
                   │           └──┬───────────┘ │          │
                   │              │             │          │
                   │           ┌──▼─────────────▼──┐      │
                   │           │  DEEP SLEEP        │      │
                   │           │  Wake at 6:00 PM   │      │
                   └───────────┤  (timer wakeup)    │──────┘
                               └────────────────────┘
```

### Firmware Key Design Decisions

1. **Interrupt-driven counting:** GPIO 14 hardware interrupt fires when IR beam breaks. Software debounce (50ms) prevents double-counts from wing flutters. Count stored in RTC memory (survives light sleep).

2. **Night-only operation:** EFSB moths are nocturnal. No counting needed 6 AM - 6 PM. Deep sleep during day saves massive power.

3. **Daily SMS report at dawn:** One SMS per day keeps cost low (~P0.50/SMS on Globe/Smart prepaid). Alert content:
   - `"TalongGuard: 12 moths last night. THRESHOLD EXCEEDED. Spray today. Batt: 78%"`
   - `"TalongGuard: 3 moths last night. Safe, no spray needed. Batt: 92%"`

4. **SPIFFS storage:** Count and log data saved to ESP32 flash. Survives power loss. Stores last 30 days of nightly counts.

5. **Battery monitoring:** ADC reads battery voltage via divider. Below 3.3V = low battery SMS warning.

---

## 4. POWER BUDGET

### Current Consumption

| State | Current Draw | Duration/Day | Energy (mAh/day) |
|-------|-------------|-------------|-------------------|
| Deep sleep (daytime) | 10 uA | 12 hours | 0.12 mAh |
| Light sleep (nighttime idle) | 0.8 mA | ~11.5 hours | 9.2 mAh |
| Active counting (IR beam on) | 25 mA | ~30 min total (bursts) | 12.5 mAh |
| SIM800L standby | 7 mA | 12 hours (night) | 84 mAh |
| SIM800L transmitting SMS | 2000 mA (peak) | ~5 seconds/day | 2.8 mAh |
| Status LED (blink) | 5 mA | ~10 min total | 0.8 mAh |
| **TOTAL per day** | | | **~110 mAh/day** |

### Battery Sizing

- **18650 battery capacity:** 3,400 mAh (quality cell)
- **Days on full charge (no solar):** 3,400 / 110 = **~31 days**
- **With 1W solar panel (5V/200mA):**
  - Average 4-5 sun-hours/day in Mindoro
  - Daily charge: 200mA x 4h x 0.7 (efficiency) = **560 mAh/day**
  - Daily drain: 110 mAh/day
  - **Net positive: +450 mAh/day — battery stays topped up**
  - Even rainy days (1-2 sun-hours): 140-280 mAh charge, still net positive

### Conclusion
**1W solar panel + 3400mAh 18650 = indefinite field operation.** Battery provides ~1 month buffer for extended cloudy periods.

---

## 5. 3D ENCLOSURE DESIGN REQUIREMENTS

### Overall Design: Modified Funnel Trap

```
        ┌───────────────┐
        │  SOLAR PANEL  │  ◄── Angled 30 degrees south-facing
        │  (mounted top)│      Hinged for cleaning access
        └───────┬───────┘
                │
        ┌───────▼───────┐
        │  ELECTRONICS  │  ◄── Sealed compartment (IP54 minimum)
        │  HOUSING      │      ESP32 + SIM800L + battery
        │  (top box)    │      Silicone gasket seal
        │               │      SMA antenna port for GSM
        └───────┬───────┘
                │
        ┌───────▼───────┐
        │  FUNNEL ENTRY │  ◄── Standard funnel trap design
        │               │      Wide mouth (15-20cm diameter)
        │   \         / │      Narrows to 2cm opening
        │    \       /  │
        │     \     /   │
        │      \   /    │
        │       | |     │  ◄── IR BEAM crosses here
        │       | |     │      TX one side, RX opposite
        │  ┌────v─v────┐│      3mm gap = moth body width
        │  │COLLECTION ││
        │  │ CHAMBER   ││  ◄── Moths fall in, can't escape
        │  │           ││      Removable for cleaning/counting
        │  │  [LURE]   ││  ◄── Pheromone lure holder (clip)
        │  └───────────┘│      Easy swap every 30-45 days
        └───────────────┘
                │
           ┌────v────┐
           │  STAKE  │  ◄── Ground stake or hanging hook
           │  MOUNT  │      Height: 1-1.5m above ground
           └─────────┘      (canopy level of eggplant)
```

### Design Specifications

| Feature | Requirement | Reason |
|---------|------------|--------|
| Material | PETG or ASA filament | UV resistant, waterproof. PLA degrades outdoors. |
| Electronics seal | IP54 (splash-proof) | Rain, dew, irrigation splash |
| Gasket | 2mm silicone O-ring groove | Seal electronics compartment |
| Color | White or light gray | Minimize heat absorption |
| Funnel diameter | 15-20 cm opening | Standard for EFSB traps |
| IR sensor mounting | Opposing slots at funnel neck | Precise alignment, 3mm gap |
| Lure holder | Spring clip inside collection chamber | Easy lure swap without tools |
| Collection chamber | Removable twist-lock base | Empty dead moths, manual verification |
| Solar mount | Top surface, 30 degree tilt bracket | Optimal angle for Mindoro latitude (~13 degrees N) |
| Antenna | External SMA mount through housing | Better GSM reception than internal |
| Stake/mount | 25mm diameter pole socket | Fits standard bamboo or PVC pole |
| Drain holes | 2mm holes in collection chamber | Rainwater drainage, prevent drowning lure |
| Total height | ~35-40 cm (housing + funnel + chamber) | |
| Print time (est.) | 8-12 hours total (3-4 parts) | |
| Filament cost | ~200g PETG = P150-200 | |

### Assembly: 4 Printed Parts
1. **Electronics housing** (top box with lid)
2. **Funnel body** (with IR sensor slots)
3. **Collection chamber** (with lure clip)
4. **Solar panel tilt bracket**

Plus: silicone gasket, 4x M3 screws for lid, twist-lock tabs molded in.

---

## 6. COMPONENT SOURCING LIST

### Search terms for Shopee/Lazada Philippines

| Component | Search Term | Est. Price (P) | Notes |
|-----------|------------|----------------|-------|
| ESP32 DevKit V1 | "ESP32 DevKit V1 CP2102" | 300-400 | Get CP2102 USB chip version (more stable) |
| IR break-beam sensor | "IR break beam sensor 3mm" or "infrared beam sensor pair" | 80-150 | Get 3mm or 5mm pair. 5V compatible. |
| SIM800L module | "SIM800L GSM module" | 250-350 | Get version with antenna. Micro-SIM. |
| GSM antenna | "SIM800L antenna SMA" | 30-50 | If module doesn't include one |
| Solar panel 5V 1W | "5V 1W solar panel 110x80mm" | 200-300 | Mini panel, 5V output for TP4056 |
| TP4056 charge module | "TP4056 type-c charging module with protection" | 25-40 | Get version WITH battery protection (DW01) |
| 18650 battery | "18650 battery 3400mAh" | 100-180 | Buy branded (Samsung, LG, Panasonic). Avoid fakes. |
| 18650 holder | "18650 battery holder with wire" | 15-25 | Single cell holder |
| Resistors | "resistor assortment kit" | 50-80 | Need 100R, 220R, 10k, 100k |
| NPN transistor | "2N2222 transistor" | 5-10 | For buzzer drive (optional) |
| Buzzer | "5V active buzzer" | 15-25 | Optional — audible feedback |
| LED green | "3mm green LED" | 5-10 | Status indicator |
| Capacitor 1000uF | "1000uF 10V electrolytic capacitor" | 10-15 | For SIM800L power stabilization |
| Prepaid SIM | Globe/Smart prepaid SIM | 40 | Text promos ~P15/week |
| Jumper wires | "dupont jumper wire male female" | 40-60 | For prototyping |
| Breadboard | "breadboard 830 point" | 50-80 | For initial prototype testing |
| PETG filament | "PETG filament 1.75mm 1kg" | 800-1200 | Need ~200g per unit. White/light gray. |
| Silicone sealant | "silicone sealant clear waterproof" | 80-120 | For housing gasket/sealing |
| M3 hardware | "M3 screw nut assortment stainless" | 40-60 | Housing assembly |

### Pheromone Lure Sourcing

| Source | Product | Price | Lead Time |
|--------|---------|-------|-----------|
| IndiaMART suppliers | L. orbonalis pheromone lure | P10-100/piece | 2-4 weeks |
| Katyayani Organics (India) | EFSB lure + water trap | ~P80/set | 2-4 weeks |
| BigHaat (India) | Leucin brinjal lure | ~P55/piece | 2-4 weeks |
| Local: DA-BAR, UPLB Entomology | May have PH suppliers or synthesis contacts | TBD | Ask advisor |

**Import note:** Small quantities of pheromone lures ship via standard post. For bulk: check BPI import requirements.

---

## 7. PROTOTYPE BUILD ORDER

### Week 1: Breadboard Prototype
1. Wire ESP32 + IR sensor on breadboard
2. Write interrupt-based counter firmware
3. Test counting with finger/pencil breaking beam
4. Verify count accuracy (100 breaks = 100 counts?)

### Week 2: Add GSM + Power
5. Wire SIM800L, test SMS sending (AT commands)
6. Integrate counter + SMS: threshold trigger sends text
7. Wire TP4056 + battery + solar panel
8. Test charge/discharge cycle

### Week 3: Enclosure + Integration
9. Design enclosure in Fusion 360 / FreeCAD
10. 3D print funnel trap + electronics housing
11. Mount all components in enclosure
12. Seal electronics compartment, test splash resistance

### Week 4: Lab Validation
13. Simulate moth entry (small objects through funnel)
14. Run 24-hour power cycle test
15. Verify SMS delivery reliability
16. Document everything for pilot preparation

---

## 8. KEY TECHNICAL RISKS AND MITIGATIONS

| Risk | Impact | Mitigation |
|------|--------|-----------|
| IR counts non-moth objects (rain, debris) | False high counts | Software filter: ignore triggers < 5ms (too fast) and > 500ms (too slow). Funnel blocks large insects. |
| SIM800L 2A peak crashes ESP32 | Random resets, missed counts | Power SIM800L from battery directly. 1000uF cap on VCC. |
| Pheromone degrades in tropical heat | Reduced moth attraction | Store lures in fridge. Replace every 30 days in hot season. |
| ESP32 overheats in sealed box | Erratic behavior | White enclosure, mesh ventilation slots, shade mounting. |
| Moisture inside housing | Short circuits, corrosion | Silicone gasket, conformal coating on PCB, desiccant packet. |
| Farmer runs out of SIM load | No alerts sent | Use unlimited text promos (P15/week). Firmware queues and retries. |
