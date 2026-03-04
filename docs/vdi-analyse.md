# VDI-Lösungen — Umfassende Vergleichsanalyse

> **Zielgruppe:** Öffentlich-rechtliche Einrichtung
> **Erstellt:** März 2026
> **Status:** Entwurf zur Bewertung

---

## Inhaltsverzeichnis

1. [Zusammenfassung (Executive Summary)](#1-zusammenfassung)
2. [Bewertete Lösungen im Überblick](#2-bewertete-lösungen-im-überblick)
3. [Einzelanalysen](#3-einzelanalysen)
   - 3.1 [Windows Terminal Server (RDS / RemoteApps)](#31-windows-terminal-server-rds--remoteapps)
   - 3.2 [Azure Local (ehem. Azure Stack HCI)](#32-azure-local)
   - 3.3 [Azure Virtual Desktop (Cloud)](#33-azure-virtual-desktop-cloud)
   - 3.4 [VMware Horizon](#34-vmware-horizon)
   - 3.5 [Open Source — OpenDesktop](#35-open-source--opendesktop)
   - 3.6 [Proxmox VE mit UDS Enterprise](#36-proxmox-ve-mit-uds-enterprise)
4. [Vergleichsmatrix](#4-vergleichsmatrix)
5. [Kostenvergleich (TCO-Schätzung)](#5-kostenvergleich)
6. [Datenschutz und IT-Sicherheit](#6-datenschutz-und-it-sicherheit)
7. [Vergaberechtliche Aspekte](#7-vergaberechtliche-aspekte)
8. [Empfehlung und Fazit](#8-empfehlung-und-fazit)

---

## 1. Zusammenfassung

Diese Analyse vergleicht sechs VDI-Lösungen hinsichtlich Funktionalität, Kosten, Support, Datenschutz/IT-Sicherheit und vergaberechtlicher Eignung für eine öffentlich-rechtliche Einrichtung. Die Lösungen reichen von klassischen On-Premises-Ansätzen (RDS, VMware Horizon, Proxmox) über Hybrid-Modelle (Azure Local) bis hin zu reinen Cloud-Lösungen (Azure Virtual Desktop) und Open-Source-Alternativen (OpenDesktop, UDS Enterprise).

**Kernaussagen:**

- **Datensouveränität** ist der kritische Faktor: Reine Cloud-Lösungen (AVD) erfordern besondere Prüfung hinsichtlich DSGVO und Schrems-II.
- **Kosten** variieren erheblich: Open-Source-Lösungen haben niedrigere Lizenzkosten, erfordern aber mehr internes Know-how.
- **VMware Horizon** wurde als EUC-Sparte an KKR verkauft und firmiert seit Juli 2024 als **Omnissa** — die Zukunft der Plattform ist im Umbruch.
- **Vergaberecht** erfordert bei allen Lösungen ab dem EU-Schwellenwert (216.000 € netto seit 01.01.2026) eine europaweite Ausschreibung.
- **Deutsche Verwaltungscloud (DVC)** ist seit April 2025 produktiv — DVC-kompatible Lösungen bieten vereinfachte Beschaffungswege.

---

## 2. Bewertete Lösungen im Überblick

| Lösung | Typ | Hersteller | Lizenzmodell |
|--------|-----|------------|--------------|
| Windows RDS / RemoteApps | On-Premises | Microsoft | Proprietär (CAL-basiert) |
| Azure Local | Hybrid (On-Prem + Cloud) | Microsoft | Proprietär (Subscription) |
| Azure Virtual Desktop | Cloud | Microsoft | Proprietär (Pay-as-you-go) |
| VMware Horizon (Omnissa) | On-Premises / Hybrid | Omnissa (ehem. VMware/Broadcom, seit 07/2024 KKR) | Proprietär (Subscription) |
| OpenDesktop | On-Premises | Community / diverse | Open Source |
| Proxmox + UDS Enterprise | On-Premises | Proxmox Server Solutions / VirtualCable | Open Source + kommerziell |

---

## 3. Einzelanalysen

### 3.1 Windows Terminal Server (RDS / RemoteApps)

#### Beschreibung
Microsoft Remote Desktop Services (RDS) ist die klassische Terminal-Server-Lösung, die sitzungsbasierte Desktops und Einzelanwendungen (RemoteApps) über das RDP-Protokoll bereitstellt. Sie ist Bestandteil von Windows Server und wird seit Jahrzehnten in Unternehmen und Behörden eingesetzt.

#### Vorteile
- **Bewährte Technologie:** Seit Jahrzehnten im Einsatz, breit dokumentiert, großes Ökosystem
- **Einfache Integration:** Nahtlose Einbindung in bestehende Active-Directory- und Microsoft-365-Infrastrukturen
- **Geringer Client-Aufwand:** RDP-Clients auf nahezu allen Plattformen verfügbar (Windows, macOS, Linux, mobile Geräte)
- **RemoteApps:** Einzelne Anwendungen können ohne vollständigen Desktop bereitgestellt werden — reduziert Ressourcenverbrauch
- **Bestehendes Know-how:** Die meisten IT-Abteilungen verfügen bereits über RDS-Erfahrung
- **Vollständige On-Premises-Kontrolle:** Keine Cloud-Abhängigkeit, Daten verbleiben im eigenen Rechenzentrum

#### Nachteile
- **Keine echte VDI:** Sitzungsbasiert — alle Benutzer teilen sich ein Betriebssystem (kein dedizierter Desktop pro Nutzer)
- **Skalierungsgrenzen:** Vertikale Skalierung begrenzt; ab ca. 50–80 Nutzern pro Server werden zusätzliche Hosts nötig
- **Eingeschränkte Multimedia-Performance:** Für grafikintensive Anwendungen nur bedingt geeignet (GPU-Passthrough komplex)
- **Applikationskompatibilität:** Nicht alle Anwendungen sind Multi-User-fähig auf einem geteilten OS
- **Lizenzkosten steigen:** CAL-Modell wird bei wachsender Nutzerzahl teuer
- **End of Mainstream Support:** Windows Server 2019 RDS: 2024, Windows Server 2022 RDS: 2026 — regelmäßige Migration nötig
- **Kein modernes Management:** Fehlende zentrale Management-Konsole im Vergleich zu dedizierten VDI-Lösungen

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Einmalig | Jährlich |
|----------------|----------|----------|
| Windows Server 2025 Standard (2 Hosts) | ca. 2.000–4.000 € | — |
| RDS CALs (100 User) | ca. 15.000–20.000 € | — |
| Server-Hardware (2 Hosts) | ca. 20.000–40.000 € | — |
| Microsoft Software Assurance (optional) | — | ca. 5.000–8.000 € |
| **Gesamt (ohne Personal)** | **ca. 37.000–64.000 €** | **ca. 5.000–8.000 €** |

#### Support
- **Microsoft Unified Support:** Ab ca. 50.000 €/Jahr (pauschal, gesamtes Microsoft-Portfolio)
- **Microsoft Premier Support:** Individuell verhandelbar, typisch 25.000–100.000 €/Jahr
- **Pay-per-Incident:** Ab ca. 500 € pro Supportfall
- **Partner/Systemhäuser:** Managed Services über Microsoft-Partner, typisch 50–150 €/Nutzer/Jahr

---

### 3.2 Azure Local (ehem. Azure Stack HCI)

#### Beschreibung
Azure Local (vormals Azure Stack HCI) ist eine Hybrid-Lösung von Microsoft, die Azure-Dienste auf eigener Hardware im lokalen Rechenzentrum betreibt. Sie kombiniert die Vorteile von On-Premises-Kontrolle mit Azure-Management und ermöglicht es, Azure Virtual Desktop lokal zu betreiben.

#### Vorteile
- **Hybrid-Ansatz:** Daten bleiben im eigenen Rechenzentrum, Management über Azure Arc
- **Azure-Integration:** Nutzung von Azure-Diensten (AVD, AKS, Azure Arc VMs) ohne Daten in die Cloud zu senden
- **Datensouveränität:** Workloads und Daten bleiben on-premises — wichtig für DSGVO-Compliance
- **Skalierbarkeit:** Einfaches Hinzufügen von Knoten (2–16 Knoten pro Cluster)
- **Windows-Ökosystem:** Volle Kompatibilität mit bestehender Microsoft-Infrastruktur
- **AVD on-premises:** Azure Virtual Desktop kann lokal betrieben werden — Kombination aus modernem VDI und lokaler Datenhaltung

#### Nachteile
- **Cloud-Abhängigkeit für Management:** Azure-Verbindung für Management und Abrechnung erforderlich (regelmäßiger „Heartbeat")
- **Komplexe Lizenzierung:** Kombination aus Hardware-, Software- und Verbrauchslizenzen
- **Hohe Einstiegskosten:** Zertifizierte Hardware (HCI-Appliances) teurer als Standardserver
- **Microsoft-Lock-in:** Starke Bindung an Microsoft-Ökosystem
- **Steile Lernkurve:** Erfordert Know-how in Azure, Hyper-V und Windows Admin Center
- **Azure-Subscription notwendig:** Auch für rein lokale Nutzung fallen monatliche Azure-Gebühren an

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Einmalig | Jährlich/Monatlich |
|----------------|----------|-------------------|
| Zertifizierte HCI-Hardware (2-4 Knoten) | ca. 40.000–100.000 € | — |
| Azure Local Subscription (pro physischem Kern) | — | ca. 10–15 €/Kern/Monat |
| Windows Server Datacenter Subscription | — | inkludiert oder ca. 5–10 €/Kern/Monat |
| AVD-Zugriffslizenzen (Microsoft 365 E3/E5) | — | ca. 30–55 €/Nutzer/Monat |
| **Gesamt (ohne Personal, 100 User)** | **ca. 40.000–100.000 €** | **ca. 50.000–90.000 €/Jahr** |

> **Hinweis:** Die Kosten variieren stark je nach Konfiguration, Knotenzahl und gewählten Lizenzen. Microsoft bietet für den öffentlichen Sektor vergünstigte Konditionen über Rahmenverträge (z.B. Microsoft CASA/SELECT).

#### Support
- **Microsoft Unified Support:** Ab ca. 50.000 €/Jahr
- **Hardware-Support:** Über OEM-Partner (Dell, HPE, Lenovo), typisch 5–15 % der Hardware-Kosten/Jahr
- **Azure Support Plans:** Developer (29 $/Monat), Standard (100 $/Monat), Professional Direct (1.000 $/Monat)
- **Partner Managed Services:** 100–200 €/Nutzer/Jahr typisch

---

### 3.3 Azure Virtual Desktop (Cloud)

#### Beschreibung
Azure Virtual Desktop (AVD) ist Microsofts cloudbasierte VDI-Lösung, die vollständig in Azure betrieben wird. Sie bietet Multi-Session Windows 11/10, vollständige Desktop-Virtualisierung und RemoteApp-Funktionalität.

#### Vorteile
- **Kein eigenes Rechenzentrum nötig:** Vollständig cloudbasiert — keine Hardware-Investition
- **Elastische Skalierung:** Automatisches Hoch-/Herunterskalieren je nach Bedarf
- **Multi-Session Windows 11:** Einzigartige Funktion — mehrere Nutzer auf einem Windows-11-Desktop (kosteneffizienter als VDI)
- **Schnelle Bereitstellung:** Neue Desktops in Minuten statt Wochen verfügbar
- **Integrierte Sicherheit:** Microsoft Defender, Conditional Access, MFA nativ integriert
- **FSLogix-Profile:** Optimierte Profilverwaltung für nahtlose Benutzererfahrung
- **Microsoft-365-Optimierung:** Nativ optimiert für Teams, Outlook, OneDrive
- **Automatisierung:** Infrastructure-as-Code mit ARM/Bicep/Terraform

#### Nachteile
- **Datensouveränität kritisch:** Daten werden in Azure-Rechenzentren verarbeitet — DSGVO-Konformität umstritten (Schrems-II-Problematik, CLOUD Act)
- **Laufende Kosten:** Verbrauchsbasiertes Modell kann bei dauerhafter Nutzung teurer werden als On-Premises
- **Internetabhängigkeit:** Vollständige Abhängigkeit von stabiler Internetverbindung
- **Vendor-Lock-in:** Starke Abhängigkeit von Microsoft Azure — Migration zu anderen Plattformen aufwendig
- **Komplexe Kostenprognose:** Verbrauchsbasierte Abrechnung erschwert Budgetplanung
- **Latenz:** Netzwerklatenz kann Benutzererfahrung beeinflussen, insbesondere bei grafikintensiven Anwendungen
- **BSI C5-Testat:** Azure verfügt über C5-Testat, aber die Verantwortung für die korrekte Konfiguration liegt beim Kunden
- **Rechtliche Unsicherheit:** US-amerikanischer Anbieter — Zugriffsmöglichkeiten durch US-Behörden (CLOUD Act, FISA)

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Monatlich (100 User) |
|----------------|---------------------|
| Azure VMs (D2s_v5, ~100 VMs oder Multi-Session) | ca. 3.000–8.000 €/Monat |
| Managed Disks (128 GB SSD pro User) | ca. 500–1.500 €/Monat |
| Netzwerk (Egress-Traffic) | ca. 200–500 €/Monat |
| Microsoft 365 E3 (inkl. AVD-Berechtigung) | ca. 3.200 €/Monat (32 €/User) |
| Azure Storage (Profile, Daten) | ca. 200–500 €/Monat |
| **Gesamt (100 User)** | **ca. 7.100–13.500 €/Monat** |
| **Gesamt jährlich** | **ca. 85.000–162.000 €/Jahr** |

> **Hinweis:** Kosten können durch Reserved Instances (1-3 Jahre Vorauszahlung), Autoscaling und Multi-Session-Konfiguration signifikant reduziert werden (bis zu 40-60 %).

#### Support
- **Azure Support Plans:**
  - Basic: kostenlos (kein technischer Support, nur Abrechnung)
  - Developer: 29 $/Monat (Antwort <8h, nur Nicht-Produktionsumgebungen)
  - Standard: 100 $/Monat (24x7, Antwort <1h für kritische Fälle)
  - Professional Direct: 1.000 $/Monat (24x7, Antwort <1h, dedizierter Delivery Manager)
  - **Wichtig:** Seit 01.07.2024 ist der kostenlose Azure Standard Support für EA/MCA-E-Kunden beendet
- **Microsoft Unified Support:** Ab ca. 50.000 €/Jahr
- **Partner Managed Services:** 80–200 €/Nutzer/Jahr

---

### 3.4 VMware Horizon (jetzt: Omnissa Horizon)

#### Beschreibung
VMware Horizon war die VDI-Flaggschiff-Lösung von VMware. Nach der Broadcom-Übernahme (November 2023) wurde die gesamte End-User-Computing-Sparte (EUC) als „nicht-kerngeschäft" eingestuft und im Juli 2024 für ca. 4 Mrd. USD an die Private-Equity-Firma **KKR** verkauft. Das Produkt firmiert seither als **Omnissa Horizon** und wird von der eigenständigen Firma Omnissa (~4.000 Mitarbeiter, ~1,5 Mrd. USD ARR) weiterentwickelt.

#### Vorteile
- **Vollwertige VDI:** Dedizierte virtuelle Desktops pro Benutzer — volle Isolation
- **Blast Extreme Protokoll:** Proprietäres Display-Protokoll mit hervorragender Performance, auch über WAN
- **Plattformunabhängig:** Unterstützt Windows und Linux als Gast-OS
- **Unified Workspace:** Integration mit Workspace ONE für Endpoint-Management
- **Instant Clones:** Schnelle Bereitstellung von Desktops in Sekunden
- **App Volumes:** Anwendungsschichtung (Application Layering) für vereinfachte Softwareverteilung
- **Bewährt im Enterprise:** Langjähriger Marktführer im VDI-Bereich mit großem Partner-Ökosystem
- **On-Premises-Kontrolle:** Volle Kontrolle über Daten und Infrastruktur
- **Eigenständigkeit:** Unter Omnissa wieder unabhängig von Broadcom — eigene Produkt-Roadmap
- **Flexible Deployment:** On-Premises (Term), SaaS-managed, Horizon Cloud (DaaS auf Azure/AWS)

#### Nachteile
- **Übergangsphase:** Umfirmierung VMware → Omnissa noch nicht abgeschlossen; Lizenzmigration zu neuen Omnissa-Keys erforderlich (Horizon 8 2412+)
- **Perpetual-Lizenzen abgekündigt:** Nur noch Subscription-Modell für Neukunden
- **Komplexe Infrastruktur:** Erfordert vSphere, vCenter, Connection Server, UAG — viele Komponenten
- **vSphere-Kosten explodiert:** Die unterliegende VMware-vSphere-Lizenzierung unter Broadcom wurde drastisch teurer (per-Core, 72-Core-Minimum, Subscription-only) — betrifft die Gesamtkosten der VDI-Infrastruktur erheblich
- **Steile Lernkurve:** Spezialisiertes VMware/Omnissa-Know-how erforderlich
- **Unsichere Langfrist-Strategie:** KKR als Private-Equity-Eigentümer — Weiterverkauf oder Börsengang möglich
- **Basic Support abgekündigt:** Seit Ende 2025 nur noch Production Support verfügbar
- **Vendor-Lock-in:** Starke Abhängigkeit vom VMware/Omnissa-Ökosystem

#### Aktuelle Editionen (Stand 2026)

| Edition | Beschreibung | Listenpreis (ca.) |
|---------|-------------|-------------------|
| **Horizon Apps Standard** | Nur veröffentlichte Apps, kein Full-VDI | ~5 $/User/Monat |
| **Horizon Standard Plus** | + Windows-VDI | ~6 $/User/Monat |
| **Horizon Apps Universal** | Multi-Cloud, Apps + Multi-Session | ~6 $/User/Monat |
| **Horizon Enterprise Plus** | Full Desktop + App Delivery (On-Prem/Single-Cloud) | ~11 $/User/Monat |
| **Horizon Universal** | Umfassendstes Paket, Multi-Cloud | ~13 $/User/Monat |

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Jährlich |
|----------------|----------|
| Omnissa Horizon Universal (100 Named User) | ca. 15.000–20.000 €/Jahr |
| VMware vSphere Foundation for VDI (Broadcom, per Core) | ca. 25.000–60.000 €/Jahr (je nach Core-Anzahl) |
| Alternativ: Horizon Enterprise Term (inkl. VVF for VDI) | ca. 20.000–30.000 €/Jahr |
| Server-Hardware (3-4 Hosts) | ca. 40.000–80.000 € (einmalig) |
| Windows-Lizenzen (VDA oder Microsoft 365) | ca. 10.000–20.000 €/Jahr |
| **Gesamt (ohne Personal)** | **Einmalig: 40.000–80.000 € + Jährlich: 50.000–110.000 €** |

> **Achtung:** Die Horizon-Lizenzen selbst (Omnissa) sind preislich relativ stabil geblieben. Die größte Kostensteigerung betrifft die unterliegende **vSphere-Infrastruktur** (Broadcom), die laut Berichten um den Faktor 3–12x teurer geworden ist. Omnissa bietet kombinierte Horizon + VVF-for-VDI-Pakete an, die diesen Effekt abmildern können. Individuelle Angebote über Omnissa-Partner einholen (PricingOps.Support@omnissa.com).

#### Support
- **Omnissa Production Support:** 24x7, im Subscription-Preis enthalten (einziger verfügbarer Tier seit Ende 2025)
- **Basic Support:** Abgekündigt — alle Kunden müssen auf Production Support migrieren
- **Drittanbieter-Support:** Sphenbridge, SVA, Computacenter — typisch 100–250 €/Nutzer/Jahr
- **Verbesserung:** Unter Omnissa wird der Support als dediziertes Unternehmen wieder fokussierter — erste Kundenberichte positiver als unter Broadcom

---

### 3.5 Open Source — OpenDesktop

#### Beschreibung
OpenDesktop (auch bekannt als „The Open Desktop Project" / diverse Projekte) umfasst verschiedene Open-Source-Ansätze für Desktop-Virtualisierung. Hierunter fallen Kombinationen aus KVM/QEMU, Apache Guacamole, XRDP, noVNC und weitere Komponenten. Es gibt kein einzelnes „OpenDesktop"-Produkt, sondern ein Ökosystem aus Bausteinen.

**Typische Komponenten:**
- **KVM/QEMU:** Hypervisor für virtuelle Maschinen
- **Apache Guacamole:** Clientloser Remote-Desktop-Gateway (HTML5-basiert)
- **XRDP:** Open-Source RDP-Server für Linux-Desktops
- **noVNC:** VNC-Client im Browser
- **FreeRDP:** Open-Source RDP-Client
- **oVirt:** Virtualisierungsmanagement (Red Hat-basiert)

#### Vorteile
- **Keine Lizenzkosten:** Kernkomponenten vollständig frei verfügbar
- **Volle Kontrolle:** Quellcode einsehbar und anpassbar — maximale Transparenz
- **Datensouveränität:** Vollständige On-Premises-Kontrolle, keine Telemetrie
- **Vendor-unabhängig:** Keine Abhängigkeit von einzelnem Hersteller
- **Linux-native:** Ideal für Linux-Desktop-Arbeitsplätze
- **Audit-fähig:** Quellcode kann durch BSI oder eigene Sicherheitsteams geprüft werden
- **Vergaberechtlich vorteilhaft:** Keine proprietäre Bindung, fördert Wettbewerb

#### Nachteile
- **Kein einheitliches Produkt:** Zusammenstellung und Integration verschiedener Komponenten erforderlich
- **Windows-Desktop-Support eingeschränkt:** Windows als VDI-Gast erfordert weiterhin Microsoft-Lizenzen
- **Kein kommerzieller Support aus einer Hand:** Community-Support oder spezialisierte Dienstleister nötig
- **Hoher Integrationsaufwand:** Setup, Härtung und Wartung deutlich aufwendiger als bei kommerziellen Lösungen
- **Eingeschränkte Enterprise-Features:** Kein Equivalent zu Instant Clones, App Volumes, FSLogix
- **Weniger Automatisierung:** Provisioning und Lifecycle-Management manueller
- **Benutzererfahrung:** Display-Performance (VNC/SPICE) kann hinter proprietären Protokollen (Blast, HDX) zurückbleiben
- **Geringe Verbreitung in Behörden:** Wenig Referenzinstallationen in deutschen Behörden

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Einmalig | Jährlich |
|----------------|----------|----------|
| Software-Lizenzen | 0 € | 0 € |
| Server-Hardware (3-4 Hosts) | ca. 30.000–60.000 € | — |
| Externer Integrationsdienstleister | ca. 20.000–50.000 € | — |
| Wartung/Admin (intern, Personalkostenanteil) | — | ca. 20.000–40.000 € |
| Optionaler kommerzieller Support (z.B. Red Hat) | — | ca. 5.000–15.000 € |
| Windows-VDA-Lizenzen (falls Windows-Desktops) | — | ca. 10.000–15.000 € |
| **Gesamt (ohne Personal)** | **ca. 50.000–110.000 €** | **ca. 35.000–70.000 €** |

> **Hinweis:** Die höheren Personalkosten für Wartung und Know-how-Aufbau kompensieren oft die eingesparten Lizenzkosten. Eine realistische TCO-Berechnung muss interne Personalkosten berücksichtigen.

#### Support
- **Community:** Foren, Mailing-Listen, IRC/Matrix — kostenlos, aber ohne SLA
- **Red Hat (für oVirt/KVM):** Enterprise-Support ab ca. 5.000 €/Jahr
- **Spezialisierte Dienstleister:** z.B. Heinlein Support, credativ, ATIX — ab ca. 10.000–30.000 €/Jahr
- **BSI-Empfehlung:** Das BSI unterstützt grundsätzlich den Einsatz von Open-Source-Software in der Verwaltung

---

### 3.6 Proxmox VE mit UDS Enterprise

#### Beschreibung
Proxmox Virtual Environment (VE) ist eine Open-Source-Virtualisierungsplattform auf Basis von KVM und LXC. In Kombination mit **UDS Enterprise** (von VirtualCable) wird ein vollständiges VDI-Brokering und -Management auf Enterprise-Niveau ermöglicht.

**UDS Enterprise** ist ein VDI-Connection-Broker, der verschiedene Hypervisoren unterstützt (Proxmox, oVirt, VMware, Hyper-V, Citrix, OpenStack) und sowohl Windows- als auch Linux-Desktops bereitstellen kann.

#### Vorteile
- **Proxmox kostenlos nutzbar:** Community Edition ohne Lizenzkosten
- **UDS Enterprise als professioneller Broker:** Bietet Enterprise-Features (Pooled/Persistent Desktops, Load Balancing, Multi-Hypervisor)
- **Europäischer Hersteller:** VirtualCable ist ein spanisches Unternehmen — EU-Datenschutzrecht anwendbar
- **Multi-Protokoll:** Unterstützt RDP, SPICE, HTML5 (Guacamole), X2Go, PCoIP, Blast
- **Flexibel:** Unterstützt gemischte Umgebungen (verschiedene Hypervisoren gleichzeitig)
- **Gute Linux-Unterstützung:** Nativ für Linux-Desktops geeignet
- **Active-Directory-Integration:** Vollständige AD/LDAP-Integration vorhanden
- **Kosteneffizient:** Deutlich günstiger als VMware Horizon bei vergleichbarer Funktionalität
- **Referenzen im öffentlichen Sektor:** In Spanien in Universitäten und Behörden im Einsatz
- **Web-basiertes Management:** Proxmox und UDS Enterprise über Weboberfläche administrierbar

#### Nachteile
- **Geringere Marktpräsenz in Deutschland:** Weniger bekannt als VMware oder Microsoft, weniger lokale Partner
- **UDS Enterprise ist kommerziell:** Der VDI-Broker ist nicht Open Source (zwar gibt es UDS Open, aber mit eingeschränktem Funktionsumfang)
- **Proxmox kein zertifizierter Enterprise-Hypervisor:** Fehlendes BSI-Zertifikat / Common-Criteria-Zertifizierung
- **Kleineres Ökosystem:** Weniger Integrationspartner, weniger Drittanbieter-Tools
- **Display-Performance:** SPICE/RDP hinter Blast Extreme oder HDX bei WAN-Verbindungen
- **Eingeschränkter Windows-Optimierung:** Kein Äquivalent zu FSLogix oder App Volumes
- **Know-how-Aufbau nötig:** Proxmox- und UDS-Expertise in Deutschland weniger verbreitet

#### Kosten (Schätzung für 100 Benutzer)

| Kostenposition | Einmalig | Jährlich |
|----------------|----------|----------|
| Proxmox VE (Community Edition) | 0 € | 0 € |
| Proxmox Subscription (Standard, 3 Hosts) | — | ca. 3.000–5.000 €/Jahr |
| UDS Enterprise Lizenzen (100 User) | — | ca. 3.000–8.000 €/Jahr (je nach Edition) |
| Server-Hardware (3 Hosts) | ca. 30.000–60.000 € | — |
| Windows-VDA-Lizenzen (falls Windows-Desktops) | — | ca. 10.000–15.000 € |
| Implementierung/Consulting | ca. 10.000–25.000 € | — |
| **Gesamt (ohne Personal)** | **ca. 40.000–85.000 €** | **ca. 16.000–28.000 €** |

#### Support
- **Proxmox** (Preise pro CPU-Socket/Jahr, exkl. MwSt.):
  - Community: 115 €/Socket/Jahr (nur Enterprise-Repo, kein Support-Ticket)
  - Basic: 355 €/Socket/Jahr (3 Tickets/Jahr, NBD)
  - Standard: 530 €/Socket/Jahr (10 Tickets/Jahr, Antwort <4h)
  - Premium: 1.060 €/Socket/Jahr (unbegrenzte Tickets, Antwort <2h, SSH-Remote-Support)
  - Alle Knoten eines Clusters müssen den gleichen Subscription-Tier haben
- **UDS Enterprise (VirtualCable):**
  - Standard-Support: E-Mail 8x5, NBD — im Lizenzpreis enthalten
  - Premium-Support: 24x7 — in Premium-Editionen enthalten
  - Für 1–49 User: Support ausschließlich über Reseller-Kanal
  - Unlimited-Users-Lizenz: bis max. ca. 21.000 €/Jahr (Flatrate)
  - Bildungsrabatt: 33,33 %; Mehrjahresrabatt: 4 % pro zusätzlichem Jahr
- **Enterprise-Support über Fujitsu:** Es besteht ein Rahmenvertrag mit Fujitsu, über den Proxmox Enterprise Support bezogen werden könnte. **Zu klären:** Ob der bestehende Rahmenvertrag diese Dienstleistung abdeckt oder ob eine separate Ausschreibung erforderlich ist (abhängig vom Leistungsgegenstand des Rahmenvertrags und den vergaberechtlichen Abrufbedingungen).
- **Drittanbieter in DACH:** Wachsend (z.B. Thomas-Krenn, netways, Heinlein Support)

---

## 4. Vergleichsmatrix

| Kriterium | RDS | Azure Local | AVD (Cloud) | Omnissa Horizon | OpenDesktop | Proxmox + UDS |
|-----------|-----|-------------|-------------|----------------|-------------|---------------|
| **Deployment** | On-Prem | Hybrid | Cloud | On-Prem/Hybrid | On-Prem | On-Prem |
| **Echte VDI (dedizierte VMs)** | Nein (sitzungsbasiert) | Ja | Ja | Ja | Ja | Ja |
| **Multi-Session** | Ja | Ja | Ja | Ja | Eingeschränkt | Eingeschränkt |
| **Windows-Desktop** | Ja | Ja | Ja | Ja | Möglich (Lizenz) | Möglich (Lizenz) |
| **Linux-Desktop** | Eingeschränkt | Ja | Eingeschränkt | Ja | Ja (nativ) | Ja (nativ) |
| **Display-Protokoll** | RDP | RDP | RDP (optimiert) | Blast Extreme | VNC/SPICE/RDP | SPICE/RDP/HTML5 |
| **Performance (WAN)** | Mittel | Mittel-Gut | Gut | Sehr gut | Gering-Mittel | Mittel |
| **GPU-Unterstützung** | Eingeschränkt | Ja | Ja (NV-Serie) | Ja (vGPU) | Möglich | Möglich |
| **Automatisierung** | Gering | Hoch (Azure) | Sehr hoch | Hoch | Gering | Mittel |
| **Profil-Management** | Roaming Profiles | FSLogix | FSLogix | DEM/App Volumes | Manuell | Eingeschränkt |
| **HA/DR** | Manuell | Azure-integriert | Azure-integriert | vSphere HA | Manuell | Proxmox HA |
| **Vendor-Lock-in** | Mittel | Hoch | Sehr hoch | Hoch | Keiner | Gering |
| **Datensouveränität** | Hoch | Mittel-Hoch | Gering | Hoch | Sehr hoch | Sehr hoch |
| **BSI C5 / IT-Grundschutz** | Anwendbar | Azure C5-testiert | Azure C5-testiert | Nicht spezifisch | Anwendbar | Anwendbar |
| **Reifegrad** | Sehr hoch | Hoch | Hoch | Sehr hoch | Mittel | Mittel-Hoch |
| **Skalierbarkeit** | Mittel | Hoch | Sehr hoch | Hoch | Mittel | Mittel-Hoch |

---

## 5. Kostenvergleich

### TCO-Schätzung über 5 Jahre (100 Benutzer)

| Kostenposition | RDS | Azure Local | AVD (Cloud) | Omnissa Horizon | OpenDesktop | Proxmox + UDS |
|----------------|-----|-------------|-------------|----------------|-------------|---------------|
| **Hardware (einmalig)** | 30.000 € | 70.000 € | 0 € | 60.000 € | 45.000 € | 45.000 € |
| **Lizenzen/Subscriptions (5 J.)** | 60.000 € | 350.000 € | 500.000 € | 350.000 € | 0 € | 50.000 € |
| **Windows-Lizenzen (5 J.)** | 20.000 € | inkl. | inkl. | 60.000 € | 60.000 € | 60.000 € |
| **Support (5 J.)** | 30.000 € | 50.000 € | 25.000 € | 50.000 € | 50.000 € | 25.000 € |
| **Implementierung** | 15.000 € | 30.000 € | 20.000 € | 30.000 € | 40.000 € | 20.000 € |
| **Internes Personal (5 J.)** | 100.000 € | 125.000 € | 75.000 € | 125.000 € | 175.000 € | 125.000 € |
| **TCO 5 Jahre** | **~255.000 €** | **~625.000 €** | **~620.000 €** | **~675.000 €** | **~370.000 €** | **~325.000 €** |
| **TCO pro User/Jahr** | **~510 €** | **~1.250 €** | **~1.240 €** | **~1.350 €** | **~740 €** | **~650 €** |

> **Wichtige Anmerkungen:**
> - Diese Schätzungen sind Richtwerte und müssen für die spezifische Situation angepasst werden.
> - RDS ist am günstigsten, bietet aber keine echte VDI (sitzungsbasiert).
> - AVD-Kosten können durch Reserved Instances und Multi-Session um 30–50 % gesenkt werden.
> - VMware-Kosten sind nach Broadcom-Übernahme besonders schwer vorherzusagen.
> - Personalkosten für Open Source sind tendenziell höher (Know-how-Aufbau).
> - Windows-Lizenzen fallen bei allen Lösungen an, wenn Windows-Desktops benötigt werden.
> - **Die nachfolgenden zusätzlichen Hardware-Kostenblöcke (PoC, Migration, GPU) sind in der obigen TCO-Tabelle noch NICHT enthalten und müssen separat kalkuliert werden.**

### 5.1 Zusätzliche Hardware-Kostenblöcke (separat zu kalkulieren)

Die oben dargestellte TCO-Schätzung bildet den laufenden Betrieb ab. Drei wesentliche Hardware-Investitionen fallen **zusätzlich** an und müssen in der Gesamtplanung separat berücksichtigt werden:

#### 5.1.1 Test- und PoC-Hardware

Für eine fundierte Evaluierung (Proof of Concept) mit 2–3 favorisierten Lösungen muss **dedizierte Test-Hardware** beschafft werden. Produktivsysteme dürfen für Tests nicht zweckentfremdet werden.

| Kostenposition | Schätzung |
|----------------|-----------|
| Server-Hosts (2–4 Hosts pro PoC-Lösung) | ca. 40.000–120.000 € |
| Storage (Shared Storage / SSD) | ca. 10.000–30.000 € |
| Netzwerk (Switches, ggf. 10/25 GbE) | ca. 5.000–15.000 € |
| Thin Clients / Test-Endgeräte (20–50 Stück) | ca. 10.000–25.000 € |
| **Gesamt PoC-Hardware** | **ca. 65.000–190.000 €** |

> **Hinweis:** Die PoC-Hardware kann bei positivem Ergebnis in die Produktivumgebung überführt werden. Bei der Beschaffung sollte daher auf Produktionseignung geachtet werden (gleiche Modelle/Spezifikationen wie geplante Produktion).

#### 5.1.2 Migrations-Hardware (Parallelbetrieb)

Während der Migration von der bestehenden Infrastruktur auf die neue VDI-Lösung müssen **beide Systeme parallel betrieben** werden. Je nach Migrationsstrategie ist zusätzliche Hardware in erheblichem Umfang erforderlich.

| Migrationsstrategie | Zusätzliche Hardware | Dauer | Risikoeinschätzung |
|---------------------|---------------------|-------|-------------------|
| **Big Bang** (alle 7.000 gleichzeitig) | 100 % Zusatzkapazität | 1 Wochenende | Sehr hohes Risiko |
| **Phasenweise** (1.000–2.000 pro Welle) | 15–30 % Zusatzkapazität | 3–6 Monate | Mittleres Risiko |
| **Rollierend** (Abteilung für Abteilung) | 10–20 % Zusatzkapazität | 6–12 Monate | Geringes Risiko |

**Geschätzte Migrations-Hardwarekosten bei 7.000 Desktops:**

| Strategie | Zusätzliche Server | Geschätzte Kosten |
|-----------|-------------------|-------------------|
| Big Bang | ~80–120 Hosts (voller Parallelbetrieb) | ca. 1,5–3,0 Mio. € |
| Phasenweise | ~15–30 Hosts | ca. 300.000–600.000 € |
| Rollierend | ~10–20 Hosts | ca. 200.000–400.000 € |

> **Empfehlung:** Für eine Einrichtung mit 7.000 Desktops wird die **phasenweise Migration** empfohlen. Big Bang ist bei dieser Größenordnung zu riskant, rollierend dauert zu lange. Die exakte Menge der benötigten Migrations-Hardware muss im Rahmen der Anforderungsanalyse bestimmt werden.

> **Offener Punkt:** Die genaue Anzahl der benötigten Migrations-Hosts hängt ab von:
> - Anzahl und Größe der Migrationswellen
> - Akzeptierter Parallelbetriebsdauer
> - Rückfallstrategie (Rollback-Kapazität)
> - Bestehende Hardware, die weiterverwendet werden kann

#### 5.1.3 GPU-Anforderungen

Eine zentrale offene Frage ist, ob und in welchem Umfang **GPU-Rechenleistung** benötigt wird. Dies beeinflusst sowohl die Hardware-Spezifikation als auch die Kosten erheblich.

**Typische GPU-Anwendungsfälle in VDI-Umgebungen:**

| Anwendungsfall | GPU-Bedarf | Typische GPU-Klasse |
|----------------|-----------|---------------------|
| Standard-Office (Word, Excel, Browser) | Kein oder minimal | Keine (CPU-Rendering genügt) |
| Erweiterte Grafik (PowerBI-Dashboards, Präsentationen) | Niedrig | vGPU (shared, 1–2 GB VRAM) |
| CAD/CAM (AutoCAD, SolidWorks, GIS) | Mittel-Hoch | vGPU (4–8 GB VRAM, z.B. NVIDIA A16/L4) |
| Medizinische Bildgebung / PACS | Hoch | vGPU (8–16 GB VRAM, z.B. NVIDIA A40/L40) |
| KI/ML-Workloads, Video-Rendering | Sehr hoch | Dedizierte GPU (NVIDIA A100/H100) |
| Multimedia/Videokonferenzen (Teams, Zoom) | Niedrig-Mittel | Hardware-Encoding (GPU-assisted, z.B. NVIDIA NVENC) |

**Kostenabschätzung GPU-Hardware:**

| GPU-Modell | Einsatz | Ca. Preis/Karte | Max. vGPU-User/Karte |
|------------|---------|-----------------|----------------------|
| NVIDIA A2 (16 GB) | Einstieg/Office+ | ca. 1.500–2.500 € | 8–16 User |
| NVIDIA A16 (4×16 GB) | VDI-Standard | ca. 4.000–6.000 € | 32–64 User |
| NVIDIA L4 (24 GB) | VDI/leichtes CAD | ca. 3.000–5.000 € | 16–32 User |
| NVIDIA A40 (48 GB) | CAD/Imaging | ca. 5.000–8.000 € | 8–16 User |
| NVIDIA L40 (48 GB) | CAD/AI | ca. 7.000–10.000 € | 8–16 User |

> **Achtung:** Neben der GPU-Hardware fallen **zusätzliche vGPU-Lizenzkosten** (NVIDIA) an:
> - **NVIDIA vPC** (Virtual PC): ca. 2,50–4,00 €/User/Monat — für Standard-Desktop-Beschleunigung
> - **NVIDIA vWS** (Virtual Workstation): ca. 5,00–8,00 €/User/Monat — für professionelle Grafik (CAD, etc.)
> - **Bei 7.000 Usern (nur vPC):** ca. 210.000–336.000 €/Jahr zusätzliche Lizenzkosten

**Rechenbeispiel: GPU-Kosten bei 10 % GPU-Nutzern (700 von 7.000):**

| Position | Kosten |
|----------|--------|
| GPU-Hardware (z.B. 25× NVIDIA A16) | ca. 100.000–150.000 € |
| GPU-Server (zusätzliche Hosts mit GPU-Slots) | ca. 75.000–150.000 € |
| NVIDIA vPC-Lizenzen (700 User × 5 Jahre) | ca. 105.000–168.000 € |
| **Gesamt GPU-Zusatzkosten (5 Jahre)** | **ca. 280.000–468.000 €** |

> **Empfehlung:** Vor der Hardware-Planung muss eine **Benutzerprofilanalyse** durchgeführt werden, die klärt:
> 1. Wie viele Nutzer benötigen GPU-Beschleunigung?
> 2. Welche Anwendungen erfordern GPU? (CAD, GIS, PACS, Multimedia?)
> 3. Genügt geteilte vGPU oder werden dedizierte GPUs benötigt?
> 4. Werden GPUs auch für Hardware-Encoding bei Videokonferenzen genutzt?

**GPU-Support nach VDI-Lösung:**

| Lösung | vGPU-Support | Einschränkungen |
|--------|-------------|-----------------|
| **RDS** | Eingeschränkt (DDA ab Server 2025) | Kein echtes vGPU-Sharing nativ |
| **Azure Local** | Ja (GPU-VMs über Azure Arc) | Erfordert GPU-fähige HCI-Knoten |
| **AVD (Cloud)** | Ja (NVv4/NCasT4-VMs in Azure) | Verbrauchsbasiert, hohe laufende Kosten |
| **Omnissa Horizon** | Ja (Blast + NVIDIA vGPU) | Bester vGPU-Support im Markt |
| **OpenDesktop** | Möglich (KVM GPU-Passthrough/Mediated) | Manuell, kein Enterprise-Management |
| **Proxmox + UDS** | Möglich (PCIe-Passthrough, Mediated) | vGPU-Support in Entwicklung, kein offizieller NVIDIA-Support |

---

## 6. Datenschutz und IT-Sicherheit

### 6.1 Rechtlicher Rahmen

Für öffentlich-rechtliche Einrichtungen gelten besonders strenge Anforderungen:

| Regelwerk | Relevanz | Beschreibung |
|-----------|----------|--------------|
| **DSGVO (EU)** | Pflicht | Schutz personenbezogener Daten, Rechtsgrundlage für Verarbeitung |
| **BDSG (DE)** | Pflicht | Nationale Ergänzung zur DSGVO |
| **Landesdatenschutzgesetze** | Pflicht | Länderspezifische Regelungen für öffentliche Stellen |
| **BSI IT-Grundschutz** | Empfohlen/Pflicht | Standard für IT-Sicherheit in Bundesbehörden |
| **BSI C5** | Empfohlen | Cloud-spezifischer Kriterienkatalog |
| **KRITIS-Verordnung** | Ggf. Pflicht | Falls kritische Infrastruktur betroffen |
| **Schrems-II (EuGH)** | Pflicht | Einschränkungen bei Datenübermittlung in Drittstaaten (USA) |
| **OZG** | Relevant | Onlinezugangsgesetz — Anforderungen an digitale Verwaltung |

### 6.2 Bewertung der Lösungen

#### Datensouveränität

| Lösung | Datenstandort | US-Zugriff möglich? | Bewertung |
|--------|---------------|----------------------|-----------|
| **RDS** | Eigenes RZ | Nein | ✅ Sehr gut |
| **Azure Local** | Eigenes RZ (Management: Azure) | Metadaten: Ja | ⚠️ Gut (Einschränkung Management) |
| **AVD (Cloud)** | Azure-RZ (EU möglich) | Ja (CLOUD Act) | ❌ Kritisch |
| **Omnissa Horizon** | Eigenes RZ | Nein (On-Prem) | ✅ Sehr gut |
| **OpenDesktop** | Eigenes RZ | Nein | ✅ Sehr gut |
| **Proxmox + UDS** | Eigenes RZ | Nein | ✅ Sehr gut |

#### BSI-Konformität

| Lösung | BSI IT-Grundschutz | BSI C5 | Härtung |
|--------|--------------------|---------|---------|
| **RDS** | Bausteine verfügbar | n/a (On-Prem) | Microsoft Security Baselines |
| **Azure Local** | Bausteine teilweise verfügbar | Azure C5-testiert | Azure Security Center |
| **AVD (Cloud)** | Bausteine verfügbar | Azure C5-testiert | Azure Policy, Defender |
| **Omnissa Horizon** | Hardening Guides verfügbar | Nicht spezifisch | Omnissa/VMware Security Hardening Guides |
| **OpenDesktop** | Manuell umsetzbar | n/a (On-Prem) | CIS Benchmarks, eigene Härtung |
| **Proxmox + UDS** | Manuell umsetzbar | n/a (On-Prem) | Proxmox Hardening Docs |

#### Schrems-II / CLOUD Act — Risikobewertung

| Lösung | Risiko | Begründung |
|--------|--------|------------|
| **RDS** | Gering | Vollständig on-premises, keine Cloud-Anbindung nötig |
| **Azure Local** | Mittel | Daten on-premises, aber Management über Azure (Microsoft = US-Unternehmen) |
| **AVD (Cloud)** | Hoch | Daten in Azure-Cloud, Microsoft unterliegt CLOUD Act und FISA §702; EU Data Boundary seit 02/2025 abgeschlossen, ändert aber nicht die US-Jurisdiktion; Alternative: **Delos Cloud** (deutsche Betriebsführung) |
| **Omnissa Horizon** | Gering | On-premises möglich; Omnissa = US-Unternehmen (KKR), aber nur bei Cloud-Anbindung relevant |
| **OpenDesktop** | Sehr gering | Vollständig on-premises, kein US-Unternehmen involviert |
| **Proxmox + UDS** | Sehr gering | On-premises, EU-Hersteller (Österreich/Spanien) |

### 6.3 Empfehlung Datenschutz

Für öffentlich-rechtliche Einrichtungen mit hohen Datenschutzanforderungen:

1. **Bevorzugt:** On-Premises-Lösungen (RDS, VMware Horizon, Proxmox + UDS, OpenDesktop)
2. **Bedingt geeignet:** Azure Local (Hybrid) — nach DSFA und mit organisatorischen Maßnahmen
3. **Kritisch:** Azure Virtual Desktop (Cloud) — nur nach umfassender Datenschutz-Folgenabschätzung (DSFA), Risikoanalyse und ggf. Genehmigung durch den Datenschutzbeauftragten

> **Praxishinweis:** Mehrere Landesdatenschutzbeauftragte haben den Einsatz von Microsoft 365 und Azure-Cloud-Diensten in der öffentlichen Verwaltung als problematisch eingestuft. Eine rechtssichere Nutzung von AVD in der Cloud ist derzeit schwierig, aber nicht unmöglich — erfordert jedoch umfangreiche technische und organisatorische Maßnahmen (TOMs).

### 6.4 BSI C5:2025 — Aktualisierter Cloud-Kriterienkatalog

Die **BSI C5:2025** (Nachfolger von C5:2020) befindet sich in der Finalisierung und wird voraussichtlich 2026 veröffentlicht:

- **121 → erweiterte Kontrollen** in 17 Domänen
- **Neue Schwerpunkte:** Containermanagement, Supply-Chain-Security, Post-Quantum-Kryptografie, Confidential Computing, KI-Anforderungen, verstärkte Mandantentrennung, Souveränitätskriterien
- **Verpflichtend** für Prüfungen ab dem **1. Januar 2027** (frühere Anwendung möglich)
- **Ausrichtung an EUCS** (EU Cybersecurity Certification Scheme for Cloud Services, Level Substantial)
- **Gesundheitswesen-Präzedenz:** Seit 01.07.2025 ist ein C5-Typ-2-Testat für Cloud-Dienste im Gesundheitswesen Pflicht (§ 393 SGB V) — dieses Muster wird sich voraussichtlich auf andere öffentliche Bereiche ausweiten

### 6.5 Deutsche Verwaltungscloud (DVC) und Delos Cloud

**Deutsche Verwaltungscloud (DVC):**
- Seit **1. April 2025** im Produktivbetrieb als permanentes Produkt des IT-Planungsrats
- Über 40 Cloud-Dienste von 10+ Anbietern (SaaS, IaaS, PaaS)
- Abdeckung: Bund, Länder, Kommunen
- **Open Standards und Open-Source-Software** werden priorisiert
- Kommerzielle/Hyperscaler-Angebote können über **öffentliche IT-Dienstleister als Integratoren** eingebunden werden
- **Empfehlung:** Bei VDI-Beschaffung sollte die DVC-Kompatibilität evaluiert werden — DVC-verfügbare Lösungen bieten vereinfachte, rechtskonforme Beschaffungswege

**Delos Cloud (Souveräne Cloud für die Bundesverwaltung):**
- Betrieben von **Delos Cloud GmbH** (SAP-Tochter), nicht von Microsoft direkt
- Basiert auf Microsoft-Azure-Technologie, aber unter **deutscher rechtlicher und operativer Kontrolle**
- Erfüllt die **BSI-Cloud-Plattform-Anforderungen** für die Bundesverwaltung
- Umfasst Azure-Dienste und Microsoft-365-Produktivitätstools
- Technisch, operativ und rechtlich souverän nach deutschen regulatorischen Anforderungen
- **Relevant für AVD:** Falls AVD über Delos Cloud bereitgestellt wird, entfällt die Schrems-II-Problematik weitgehend — allerdings höhere Kosten und eingeschränkteres Dienstportfolio gegenüber Azure Public

---

## 7. Vergaberechtliche Aspekte

### 7.1 Rechtsgrundlagen

| Regelwerk | Anwendung |
|-----------|-----------|
| **GWB Teil 4 (§§ 97 ff.)** | Grundnorm für öffentliche Vergaben |
| **VgV** | Vergabeverordnung für Liefer- und Dienstleistungsaufträge oberhalb EU-Schwellenwert |
| **UVgO** | Unterschwellenvergabeordnung (nationale Vergaben) |
| **VOB/A** | Nur relevant für Bauleistungen (hier nicht einschlägig) |
| **EVB-IT** | Ergänzende Vertragsbedingungen für IT (System-, Pflege-, Cloud-Verträge) |

### 7.2 Schwellenwerte (seit 01.01.2026)

Die aktualisierten EU-Schwellenwerte gelten seit dem 1. Januar 2026 (veröffentlicht im Amtsblatt der EU am 23. Oktober 2025) und treten ohne nationale Umsetzung direkt in Kraft:

| Art | EU-Schwellenwert (netto) |
|-----|--------------------------|
| Liefer- und Dienstleistungsaufträge (oberste/obere Bundesbehörden) | **140.000 €** |
| Liefer- und Dienstleistungsaufträge (sonstige öffentliche Auftraggeber) | **216.000 €** |
| Sektorenauftraggeber (Versorgungsunternehmen) | 432.000 € |
| Bauaufträge | ca. 5.382.000 € |

**Unterschwellenbereich (UVgO):**
- **Direktvergabe** ist seit der UVgO-Reform bis **100.000 €** zulässig — ermöglicht schnelle IT-Beschaffungen ohne formales Verfahren
- Beschränkte Ausschreibung und Verhandlungsvergabe ohne Teilnahmewettbewerb bis zum EU-Schwellenwert möglich

> **Praxisrelevanz:** Bei einer VDI-Einführung mit geschätzten Kosten ab 100.000 € aufwärts ist **in den meisten Fällen eine europaweite Ausschreibung erforderlich** (der Schwellenwert wird über die gesamte Vertragslaufzeit berechnet — bei 5 Jahren Laufzeit wird die Schwelle schnell überschritten!).

> **Geplante Reform:** Das Vergabebeschleunigungsgesetz (erste Lesung Bundestag Oktober 2025) soll GWB und VgV vereinfachen und digitalisieren. Unterhalb des EU-Schwellenwerts wird eine neue, einheitliche UVgO mit den Ländern erarbeitet.

### 7.3 Relevanz für die einzelnen Lösungen

| Lösung | Vergaberechtliche Besonderheiten |
|--------|----------------------------------|
| **RDS** | Standardausschreibung IT-Dienstleistung/-Lieferung; Microsoft-Lizenzen ggf. über Rahmenverträge (z.B. MOCA, SELECT) beziehbar |
| **Azure Local** | Cloud-Dienst + Hardware — ggf. Aufteilung in Lose; EVB-IT Cloud-Vertrag anwendbar |
| **AVD (Cloud)** | EVB-IT Cloud-Vertrag; besondere Prüfung der AGB von Microsoft erforderlich (Standardvertragsklauseln); DSFA als Teil der Vergabeunterlage |
| **Omnissa Horizon** | Seit Juli 2024 eigenständiges Unternehmen (Omnissa/KKR); Beschaffungskanäle über Omnissa-Partner; unterliegende vSphere-Lizenzierung weiterhin über Broadcom — ggf. Losaufteilung (Horizon + vSphere getrennt); Perpetual-Lizenzen nicht mehr verfügbar |
| **OpenDesktop** | Ausschreibung der Integrationsdienstleistung; Software selbst frei verfügbar; fördert Wettbewerb und Anbietervielfalt — vergaberechtlich vorteilhaft |
| **Proxmox + UDS** | Ausschreibung der Implementierung + UDS-Lizenzen; europäischer Anbieter — positiv im Vergabeverfahren; Proxmox-Subscription über Partner beziehbar; **Prüfung:** Bestehender Rahmenvertrag mit Fujitsu — deckt dieser Proxmox-Enterprise-Support ab oder ist eine separate Ausschreibung nötig? |

### 7.4 Ausschreibungshinweise

1. **Produktneutrale Ausschreibung:** Grundsätzlich darf nicht ein bestimmtes Produkt vorgeschrieben werden (§ 31 Abs. 6 VgV). Stattdessen müssen funktionale Anforderungen definiert werden (z.B. „VDI-Lösung mit Unterstützung für mindestens 100 gleichzeitige Benutzer").

2. **Ausnahme Produktvorgabe:** Nur zulässig, wenn der Auftragsgegenstand dies rechtfertigt und technische Gründe vorliegen (z.B. Integration in bestehende Infrastruktur). Muss gut dokumentiert werden.

3. **Losaufteilung prüfen:** Hardware, Software-Lizenzen und Dienstleistungen sollten ggf. in separate Lose aufgeteilt werden (Mittelstandsförderung, § 97 Abs. 4 GWB).

4. **Zuschlagskriterien:** Neben dem Preis sollten qualitative Kriterien gewichtet werden:
   - Datenschutz/IT-Sicherheit (15–25 %)
   - Technische Leistungsfähigkeit (20–30 %)
   - Support und SLA (10–15 %)
   - Migrationsfähigkeit / Exit-Strategie (5–10 %)
   - Preis (30–40 %)

5. **EVB-IT Vertragstypen:**
   - **EVB-IT System** — für On-Premises-VDI-Systeme mit Hardware + Software (Generalunternehmer)
   - **EVB-IT Cloud** (seit März 2022) — für Cloud-basierte VDI (AVD, Azure Local); basiert auf Mietrecht (§§ 535 ff. BGB); **explizit an C5-Testat geknüpft** — Cloud-Anbieter müssen C5-testiert sein
   - **EVB-IT Überlassung Typ B** — für zeitlich begrenzte Softwarelizenzen (z.B. UDS Enterprise Subscription)
   - **EVB-IT Pflege S** — für laufende Wartung/Patching von Standard-VDI-Software
   - **EVB-IT Dienstvertrag** — für Implementierung, Beratung, Migration
   - **EVB-IT Rahmenvereinbarung** (seit Sommer 2024) — für Rahmenverträge mit mehreren VDI-Leistungsmodulen

   > **Pflicht:** Die Verwendung der EVB-IT ist für Bundesbehörden verpflichtend (§ 55 BHO). Die meisten Bundesländer haben vergleichbare Verpflichtungen.

---

## 8. Empfehlung und Fazit

### Bewertungsmatrix (gewichtet)

| Kriterium (Gewicht) | RDS | Azure Local | AVD (Cloud) | Omnissa Horizon | OpenDesktop | Proxmox + UDS |
|----------------------|-----|-------------|-------------|----------------|-------------|---------------|
| **Kosten (25 %)** | 9 | 5 | 4 | 3 | 7 | 8 |
| **Datenschutz (25 %)** | 8 | 6 | 3 | 7 | 10 | 9 |
| **Funktionsumfang (15 %)** | 5 | 8 | 9 | 9 | 4 | 7 |
| **Support (10 %)** | 8 | 7 | 8 | 5 | 3 | 6 |
| **Vergaberecht (10 %)** | 7 | 6 | 5 | 4 | 9 | 8 |
| **Zukunftssicherheit (10 %)** | 6 | 8 | 8 | 4 | 6 | 7 |
| **Betriebsaufwand (5 %)** | 8 | 5 | 9 | 5 | 3 | 6 |
| **Gewichtete Summe** | **7,45** | **6,25** | **5,60** | **5,35** | **6,55** | **7,70** |

> Skala: 1 (schlecht) bis 10 (sehr gut)

### Rangfolge

| Rang | Lösung | Score | Eignung |
|------|--------|-------|---------|
| 1 | **Proxmox + UDS Enterprise** | 7,70 | Bestes Gesamtpaket aus Kosten, Datenschutz und Funktionalität |
| 2 | **Windows RDS** | 7,45 | Günstigste Lösung, aber keine echte VDI — geeignet bei einfachen Anforderungen |
| 3 | **OpenDesktop** | 6,55 | Maximale Datensouveränität, aber hoher Personalaufwand |
| 4 | **Azure Local** | 6,25 | Guter Kompromiss, aber teuer und Microsoft-abhängig |
| 5 | **Azure Virtual Desktop** | 5,60 | Technisch stark, aber Datenschutz-Problematik für öffentliche Einrichtungen |
| 6 | **Omnissa Horizon** | 5,35 | Technisch ausgereift, aber Eigentümerwechsel (KKR) und vSphere-Kostensteigerung schaffen Unsicherheit |

### Handlungsempfehlung

1. **Kurzfristig / einfache Anforderungen:** Windows RDS als bewährte, kostengünstige Lösung für sitzungsbasierte Desktops
2. **Mittelfristig / VDI-Einstieg:** Proxmox VE + UDS Enterprise als kosteneffiziente, datenschutzkonforme Lösung mit europäischen Herstellern
3. **Strategisch / Digitale Souveränität:** Evaluierung einer Open-Source-Strategie (Proxmox/OpenDesktop) im Einklang mit der Digitalstrategie der öffentlichen Verwaltung
4. **Mit Vorsicht:** Omnissa Horizon (KKR-/vSphere-Kostenrisiko) und reine AVD-Cloud (Datenschutzrisiko) nur nach umfassender Risiko- und Kosten-Analyse; AVD ggf. über Delos Cloud evaluieren

### Nächste Schritte

- [ ] Anforderungsanalyse: Exakte Nutzerzahl, Anwendungslandschaft, Performance-Anforderungen definieren
- [ ] **Benutzerprofilanalyse GPU:** Klären, wie viele Nutzer GPU-Beschleunigung benötigen (CAD, GIS, PACS, Multimedia, KI)
- [ ] **Test-/PoC-Hardware beschaffen:** Dedizierte Infrastruktur für Proof of Concept (ca. 65.000–190.000 €, ggf. in Produktion überführbar)
- [ ] Proof of Concept (PoC) mit 2–3 favorisierten Lösungen
- [ ] **Migrationsstrategie festlegen:** Phasenweise vs. Big Bang — bestimmt Menge der benötigten Migrations-Hardware
- [ ] Datenschutz-Folgenabschätzung (DSFA) durchführen
- [ ] Abstimmung mit dem Datenschutzbeauftragten
- [ ] Marktrecherche und -erkundung (§ 28 VgV)
- [ ] Vergabeunterlage erstellen (funktionale Leistungsbeschreibung)
- [ ] Europaweite Ausschreibung (sofern Schwellenwert überschritten)

---

> **Haftungsausschluss:** Diese Analyse dient als Orientierungshilfe und ersetzt keine individuelle Beratung. Preise sind Schätzwerte (Stand: März 2026) und können je nach Verhandlung, Rahmenverträgen und konkreter Konfiguration erheblich abweichen. Für die vergaberechtliche Umsetzung wird die Einbindung einer spezialisierten Vergabeberatung empfohlen.
