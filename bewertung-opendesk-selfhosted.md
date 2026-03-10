# Bewertung: openDesk (Self-Hosted) als Alternative

## Wichtige Klarstellung: openDesk vs. VDI

**openDesk ist keine VDI-Lösung**, sondern eine **webbasierte Office- und Kollaborations-Suite** — vergleichbar mit Microsoft 365 / Google Workspace. Es ersetzt nicht die virtuelle Desktop-Infrastruktur (Citrix), sondern die darauf laufenden Produktivitätsanwendungen.

openDesk könnte jedoch eine **komplementäre Rolle** in der Citrix-Exit-Strategie spielen, indem es den Bedarf an VDI insgesamt reduziert.

---

## Was ist openDesk?

- **Herausgeber:** ZenDiS (Zentrum für Digitale Souveränität der öffentlichen Verwaltung)
- **Enterprise Support:** B1 Systems GmbH (Generalunternehmer)
- **Hosting:** Self-Hosted oder SaaS (via StackIT / Schwarz-Gruppe)
- **Lizenz:** Open Source (Community Edition frei verfügbar, Enterprise Edition mit Support)
- **Status:** Version 1.0 seit Oktober 2024, aktiv im Einsatz bei Bundesbehörden

### Komponenten

| Funktion | Komponente |
|---|---|
| Textverarbeitung / Tabellen / Präsentationen | Collabora Online |
| Cloud-Speicher / Dateiverwaltung | Nextcloud |
| E-Mail / Kalender / Kontakte | Open-Xchange |
| Chat / Messaging | Element (Matrix) |
| Videokonferenzen | Jitsi |
| Projektmanagement | OpenProject |
| Wiki / Wissensmanagement | XWiki |
| Identity & Access Management | Nubus (Univention) |

---

## Relevanz für AOK / ARGE

### Hohe strategische Relevanz

- **Deutsche Rentenversicherung Bund** und **Bundesagentur für Arbeit** haben im Januar 2026 eine Pilotimplementierung von openDesk begonnen — direkte ARGE-Relevanz
- **BWI/Bundeswehr** hat einen 7-Jahres-Vertrag mit ZenDiS für openDesk abgeschlossen (April 2025)
- **Robert Koch Institut / BMG** nutzt openDesk für 7.000 Nutzer
- Bundesinvestition von ca. **45 Mio. Euro** in die Entwicklung
- DSGVO-konform, digitale Souveränität als Kernprinzip

### Potenzielle Auswirkung auf Citrix-Exit

openDesk könnte den Bedarf an VDI **erheblich reduzieren**, wenn ein Großteil der täglichen Arbeit über den Webbrowser stattfinden kann:

| Szenario | Citrix heute | Mit openDesk |
|---|---|---|
| Office-Anwendungen | Citrix-Session erforderlich | Webbrowser (lokal) |
| E-Mail / Kalender | Citrix-Session erforderlich | Webbrowser (lokal) |
| Chat / Video | Citrix-Session erforderlich | Webbrowser (lokal) |
| Dateiverwaltung | Citrix-Session erforderlich | Webbrowser (lokal) |
| Sonderanwendungen | Citrix-Session erforderlich | Weiterhin VDI oder lokal |
| Fachanwendungen (Workbench) | Citrix-Session erforderlich | Weiterhin VDI oder lokal |

**Fazit:** Für Standard-Büroarbeit könnte openDesk die Citrix-Abhängigkeit eliminieren. Für Sonder- und Fachanwendungen bleibt eine VDI- oder lokale Lösung erforderlich.

---

## Bewertung nach ARGE-Kriterien

### Erfüllt Usecase?

**Teilweise.** openDesk adressiert den Office/Collaboration-Usecase vollständig, nicht aber den VDI-Usecase für Sonder-/Fachanwendungen. Es ist eine **ergänzende Lösung**, keine 1:1-Citrix-Alternative.

### Vor- und Nachteile

| Vorteile | Nachteile |
|---|---|
| Open Source, digitale Souveränität | Kein vollständiger Citrix-Ersatz (kein VDI) |
| Enterprise Support durch B1 Systems mit SLAs | Kubernetes-Infrastruktur erforderlich (min. 5-6 Server) |
| Self-Hosted möglich (eigenes Rechenzentrum) | Umstellung von Microsoft Office auf Collabora = Schulungsbedarf |
| DSGVO-konform, Ende-zu-Ende-Verschlüsselung | Enterprise Edition enthält teils proprietäre Komponenten |
| Bereits bei DRV Bund und BA im Pilotbetrieb | Noch relativ jung (v1.0 seit Oktober 2024) |
| Bundesfinanzierung sichert Weiterentwicklung | Kompatibilität mit MS-Office-Formaten nicht 100% |
| Desktop- und Mobile-Apps verfügbar | Abhängigkeit von vielen Einzelkomponenten |
| Active Directory-Integration möglich (Nubus/Keycloak) | |

### Kostenüberblick

- **Community Edition:** Kostenlos (ohne Support)
- **Enterprise Edition:** Lizenzkosten über B1 Systems (ab 500+ Nutzer konzipiert)
  - Inkl. Produkt-Subskriptionen aller Komponenten
  - SLAs bis 24/7 möglich
  - 99,9% garantierte Verfügbarkeit
- **Infrastruktur:** Kubernetes-Cluster (min. 5-6 Server)
- **SaaS-Variante:** Über StackIT verfügbar (alternative zum Self-Hosting)

### Support

- **B1 Systems GmbH** als Generalunternehmer mit festen SLAs
- Enterprise Support mit optionaler 24/7-Abdeckung
- B1 Systems: >140 Linux-Experten, spezialisiert auf Open-Source-Beratung
- Standort: Deutschland (Vohburg)

### Know-How in der ARGE?

- DRV Bund und BA bereits im Pilotbetrieb — **Know-How-Aufbau läuft in der ARGE**
- Erfahrungsaustausch mit anderen Trägern möglich
- Kubernetes-Know-How erforderlich für Self-Hosting

### Datenschutz / IT-Sicherheit

- DSGVO-konform (Kernziel des Projekts)
- Ende-zu-Ende-Verschlüsselung für Chat (Element/Matrix)
- OpenPGP-Verschlüsselung für E-Mail
- Automatischer Malware-Scan für Uploads
- Multi-Faktor-Authentifizierung
- BSI-Beteiligung an der Entwicklung

---

## Einordnung in die VDI-Strategie

openDesk ist **keine direkte Alternative** zu den in der Marktanalyse evaluierten VDI-Lösungen (Windows Terminal Server, Azure Virtual Desktop, VMware Horizon, Proxmox+UDS), sondern eine **vorgelagerte Strategie** zur Reduktion des VDI-Bedarfs:

```
Strategie-Ebene 1: Reduktion des VDI-Bedarfs
├── openDesk (Office/Collaboration → Webbrowser statt VDI)
├── Lokale Softwareverteilung (POC bereits geplant)
└── Sonderanwendungs-Audit (Hypothese: 1/3 eliminierbar)

Strategie-Ebene 2: VDI für verbleibende Anwendungen
├── Windows Terminal Server (RDS)
├── Azure Virtual Desktop
├── VMware Horizon
├── Proxmox + UDS Enterprise
└── Weitere Open-Source-VDI
```

### Empfehlung

openDesk sollte **als ergänzende Maßnahme** in die Citrix-Exit-Strategie aufgenommen werden:

1. **Synergieeffekt mit POC "Lokale Softwareverteilung":** Wenn Standard-Office-Arbeit über openDesk im Browser läuft, werden weniger Anwendungen lokal oder per VDI bereitgestellt
2. **ARGE-Alignment:** DRV Bund und BA pilotieren bereits — Erfahrungswerte und gemeinsame Infrastruktur möglich
3. **Kosten-Hebel:** Jeder Arbeitsplatz, der von Citrix auf openDesk migriert, reduziert Citrix-Lizenzkosten und VDI-Infrastrukturbedarf
4. **Zeitplan-kompatibel:** Enterprise Edition bereits verfügbar, passt in den Zeitrahmen bis Ende 2028

---

## Quellen

- [openDesk Produkt-Website](https://www.opendesk.eu/en/product)
- [openDesk Betriebsmodelle](https://www.opendesk.eu/en/operating-models)
- [openDesk Enterprise Edition Dokumentation](https://docs.opendesk.eu/operations/enterprise/)
- [ZenDiS Rahmenvertrag für Enterprise Edition](https://www.zendis.de/en/newsroom/press/zendis-awarded-framework-contract-for-opendesk-enterprise-edition-and-saas-offering)
- [heise: B1 und StackIT bieten Enterprise-Version](https://www.heise.de/en/news/openDesk-B1-and-StackIT-offer-enterprise-version-of-the-Microsoft-alternative-9848984.html)
- [Wikipedia: OpenDesk](https://en.wikipedia.org/wiki/OpenDesk)
- [openDesk FAQ](https://www.opendesk.eu/en/faq)
