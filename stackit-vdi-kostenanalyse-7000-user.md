# STACKIT VDI-Kostenanalyse: 7.000 Benutzer (Linux Mint + openDesk)

> Basierend auf STACKIT Preisliste v1.0.36 (Stand 03.03.2026)
> Alle Preise netto zzgl. MwSt.

---

## 1. Annahmen

| Parameter | Wert | Begründung |
|---|---|---|
| Gesamtnutzer | 7.000 | Vorgabe |
| Concurrent-User-Rate | 70% | Typisch für Büroarbeitsplätze (Urlaub, Teilzeit, Meetings) |
| **Gleichzeitige Sessions** | **4.900** | 7.000 x 0,70 |
| Betriebssystem | Linux Mint | Keine Windows-Lizenz nötig |
| Arbeitszeit/Tag | 10 Stunden | 07:00-17:00 (mit Puffer) |
| Arbeitstage/Monat | 22 | Standard |
| Nutzungsstunden/Monat | 220 h | 10h x 22 Tage |
| 24/7-Monat (Referenz) | 720 h | STACKIT Kalkulationsbasis |

---

## 2. VM-Sizing: Drei Szenarien

### Szenario A: Basis-Office-Worker (2 vCPU / 8 GB RAM)
Typisch: E-Mail, Browser, openDesk/Collabora, SAP GUI for Java

### Szenario B: Standard-Worker (4 vCPU / 16 GB RAM)
Typisch: Wie A + parallel mehrere Anwendungen, leichte Datenauswertung

### Szenario C: Power-User (8 vCPU / 32 GB RAM)
Typisch: Wie B + aufwändige Datenverarbeitung, BI-Tools, Entwicklungsumgebungen

---

## 3. Compute-Kosten (Kernkomponente)

### Empfohlene SKU-Auswahl (Region: Germany South, ohne Windows-Lizenz)

| Szenario | SKU | HW | vCPU | RAM | Preis/Stunde | Preis/Monat (720h) |
|---|---|---|---|---|---|---|
| **A** Basis | General Purpose g1.2-EU01 | Intel | 2 | 8 GB | 0,0758 € | 54,59 € |
| **A** Basis (AMD) | General Purpose g2a.2d-EU01 | AMD | 2 | 8 GB | 0,1185 € | 85,34 € |
| **B** Standard | General Purpose g1.3-EU01 | Intel | 4 | 16 GB | 0,1516 € | 109,18 € |
| **B** Standard (AMD) | General Purpose g2a.4d-EU01 | AMD | 4 | 16 GB | 0,2371 € | 170,69 € |
| **C** Power | General Purpose g1.4-EU01 | Intel | 8 | 32 GB | 0,3033 € | 218,37 € |
| **C** Power (AMD) | General Purpose g2a.8d-EU01 | AMD | 8 | 32 GB | 0,4741 € | 341,37 € |

> **Hinweis:** Die g1-Generation (Intel) ist deutlich günstiger als g2a (AMD).
> Für VDI-Workloads ohne spezielle AMD-Anforderungen ist g1 empfohlen.

### Compute-Kosten pro Monat (4.900 concurrent VMs)

#### Variante 1: 24/7 Betrieb (VMs laufen durchgängig)

| Szenario | SKU | Kosten/VM/Monat | x 4.900 VMs | **Gesamt/Monat** |
|---|---|---|---|---|
| **A** Basis (Intel) | g1.2 | 54,59 € | | **267.491 €** |
| **B** Standard (Intel) | g1.3 | 109,18 € | | **534.982 €** |
| **C** Power (Intel) | g1.4 | 218,37 € | | **1.070.013 €** |

#### Variante 2: Nur Arbeitszeit (220h/Monat statt 720h)

| Szenario | SKU | Preis/h | x 220h | x 4.900 VMs | **Gesamt/Monat** |
|---|---|---|---|---|---|
| **A** Basis (Intel) | g1.2 | 0,0758 € | 16,68 € | | **81.718 €** |
| **B** Standard (Intel) | g1.3 | 0,1516 € | 33,36 € | | **163.464 €** |
| **C** Power (Intel) | g1.4 | 0,3033 € | 66,73 € | | **326.957 €** |

> **Einsparung durch On-Demand:** ca. **69%** gegenüber 24/7 Betrieb

---

## 4. Storage-Kosten

### Block Storage pro VDI-Desktop

| Komponente | Größe/User | SKU | Preis/GB/h | Preis/GB/Monat |
|---|---|---|---|---|
| OS + Apps Disk | 50 GB | Premium-Capacity-EU01 | 0,0000908 € | 0,07 € |
| Performance Tier | 1 Disk | Premium-Performance 2 (1000 IOPS) | 0,0201 €/Disk/h | 14,50 €/Disk |

### Storage-Kalkulation

| Posten | Berechnung | Monat/User | x 7.000 User | **Gesamt/Monat** |
|---|---|---|---|---|
| Capacity (50 GB) | 50 GB x 0,07 €/GB | 3,50 € | | 24.500 € |
| Performance (1 Disk) | | 14,50 € | | 101.500 € |
| **Storage Gesamt** | | **18,00 €** | | **126.000 €** |

> **Hinweis:** Storage wird für alle 7.000 User berechnet (persistent), nicht nur concurrent.

### Shared Storage (User-Daten, Profile)

| Komponente | Größe | SKU | Preis/GB/Monat | **Gesamt/Monat** |
|---|---|---|---|---|
| Object Storage (Dokumente) | 10 GB/User = 70 TB | Object Storage Premium | 0,03 € | **2.100 €** |
| File Storage (Profile/Home) | 5 GB/User = 35 TB | File Storage Standard | 0,22 € | **7.700 €** |

---

## 5. Netzwerk & Infrastruktur

| Komponente | Anzahl | SKU | Preis/Monat | **Gesamt/Monat** |
|---|---|---|---|---|
| Public IPs | 10 | Public IP (IPv4) | 2,92 € | 29 € |
| Load Balancer | 4 | App-LB-Dedicated-10 | 18,92 € | 76 € |
| DNS Zone | 2 | DNS-1000 | 3,09 € | 6 € |
| **Netzwerk Gesamt** | | | | **~111 €** |

---

## 6. Infrastruktur-Server (Management, openDesk, etc.)

| Rolle | Anzahl | SKU | vCPU | RAM | Monat/VM | **Gesamt/Monat** |
|---|---|---|---|---|---|---|
| VDI Connection Broker | 3 | g1.3 (4/16) | 4 | 16 GB | 109,18 € | 328 € |
| openDesk (Collabora, Nextcloud, etc.) | 5 | g1.4 (8/32) | 8 | 32 GB | 218,37 € | 1.092 € |
| Identity Management (Keycloak/AD) | 2 | g1.3 (4/16) | 4 | 16 GB | 109,18 € | 218 € |
| Monitoring / Logging | 2 | g1.3 (4/16) | 4 | 16 GB | 109,18 € | 218 € |
| Reverse Proxy / Gateway | 2 | g1.2 (2/8) | 2 | 8 GB | 54,59 € | 109 € |
| **Infrastruktur Gesamt** | **14 VMs** | | | | | **~1.965 €** |

---

## 7. Gesamtkosten-Übersicht

### Szenario A: Basis-Worker (2 vCPU / 8 GB), Intel g1, On-Demand

| Kostenblock | Monat (netto) | Anteil |
|---|---|---|
| Compute (4.900 VMs, 220h) | 81.718 € | 57% |
| Block Storage (7.000 User) | 126.000 € | 31% |
| Shared Storage | 9.800 € | 7% |
| Infrastruktur-Server | 1.965 € | 1% |
| Netzwerk | 111 € | <1% |
| **Monatlich Gesamt** | **~143.594 €** | |
| **Jährlich** | **~1.723.128 €** | |
| **Pro User/Monat** | **~20,51 €** | |

### Szenario B: Standard-Worker (4 vCPU / 16 GB), Intel g1, On-Demand

| Kostenblock | Monat (netto) | Anteil |
|---|---|---|
| Compute (4.900 VMs, 220h) | 163.464 € | 54% |
| Block Storage (7.000 User) | 126.000 € | 42% |
| Shared Storage | 9.800 € | 3% |
| Infrastruktur-Server | 1.965 € | <1% |
| Netzwerk | 111 € | <1% |
| **Monatlich Gesamt** | **~301.340 €** | |
| **Jährlich** | **~3.616.080 €** | |
| **Pro User/Monat** | **~43,05 €** | |

### Szenario C: Power-User (8 vCPU / 32 GB), Intel g1, On-Demand

| Kostenblock | Monat (netto) | Anteil |
|---|---|---|
| Compute (4.900 VMs, 220h) | 326.957 € | 70% |
| Block Storage (7.000 User) | 126.000 € | 27% |
| Shared Storage | 9.800 € | 2% |
| Infrastruktur-Server | 1.965 € | <1% |
| Netzwerk | 111 € | <1% |
| **Monatlich Gesamt** | **~464.833 €** | |
| **Jährlich** | **~5.577.996 €** | |
| **Pro User/Monat** | **~66,40 €** | |

---

## 8. Zusammenfassung: Kosten pro User/Monat

| Szenario | 24/7 | On-Demand (220h) |
|---|---|---|
| **A** Basis (2 vCPU / 8 GB) | ~58 € | **~21 €** |
| **B** Standard (4 vCPU / 16 GB) | ~97 € | **~43 €** |
| **C** Power (8 vCPU / 32 GB) | ~185 € | **~66 €** |

---

## 9. Kostenvergleich: Citrix on-premise vs. STACKIT VDI

| Posten | Citrix (typisch) | STACKIT Linux VDI |
|---|---|---|
| Citrix-Lizenzen | ~15-25 €/User/Monat | 0 € (Open Source VDI) |
| Windows-Lizenzen (VDA) | ~7-12 €/User/Monat | 0 € (Linux Mint) |
| MS Office-Lizenzen | ~10-15 €/User/Monat | 0 € (openDesk/Collabora) |
| Hardware/Datacenter | ~15-30 €/User/Monat | In Compute enthalten |
| Compute (Cloud) | n/a | 12-47 €/User/Monat |
| Storage (Cloud) | n/a | 19 €/User/Monat |
| **Geschätzt Gesamt** | **~50-80 €/User/Monat** | **~21-66 €/User/Monat** |

> **Fazit:** Der STACKIT-Linux-VDI-Ansatz ist im Basis-Szenario (A) ca. 50-70% günstiger als eine typische Citrix-Lösung, primär durch den Wegfall von Citrix-, Windows- und Office-Lizenzen.

---

## 10. Nicht in dieser Kalkulation enthalten

- VDI-Broker-Software (z.B. Apache Guacamole = kostenlos, oder kommerzielle Lösung)
- openDesk-Betriebskosten (Personal, Wartung)
- Bandbreite / Egress-Traffic (nicht in STACKIT-Preisliste aufgeführt)
- Backup-Kosten (ca. 0,03 €/GB/Monat für Block Storage Backups)
- Projektkosten (Migration, Setup, Schulung)
- Support-Vertrag STACKIT
- Mengenrabatte (bei 7.000 Usern verhandelbar!)

---

*Erstellt am: 10.03.2026 | Quelle: STACKIT Preisliste v1.0.36 (03.03.2026)*
