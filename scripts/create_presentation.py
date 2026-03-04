#!/usr/bin/env python3
"""
Erstellt eine VDI-Vergleichspräsentation auf Basis des AOK PowerPoint Masters.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu, Cm
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
import copy
import os

TEMPLATE = os.path.join(os.path.dirname(__file__), "..", "Präsentation Master.pptx")
OUTPUT = os.path.join(os.path.dirname(__file__), "..", "docs", "VDI-Vergleichsanalyse.pptx")

# AOK brand colors (extracted from template)
AOK_GREEN = RGBColor(0x00, 0x7B, 0x3E)      # AOK Grün
AOK_DARK_GREEN = RGBColor(0x00, 0x5C, 0x2E)  # Dunkelgrün
AOK_LIGHT_GREEN = RGBColor(0xB2, 0xD2, 0x35) # Hellgrün/Pastell
AOK_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
AOK_BLACK = RGBColor(0x00, 0x00, 0x00)
AOK_DARK_GRAY = RGBColor(0x33, 0x33, 0x33)
AOK_GRAY = RGBColor(0x66, 0x66, 0x66)
AOK_LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
AOK_RED = RGBColor(0xC0, 0x00, 0x00)
AOK_ORANGE = RGBColor(0xE0, 0x7C, 0x00)

# Layout indices from the template
LY_TITLE_GREEN = 2       # 'Titelfolie, grüner Hintergrund'
LY_TITLE_WHITE = 3       # 'Titelfolie, weißer Hintergrund'
LY_SECTION_GREEN = 9     # 'Trennfolie, grüner Hintergrund'
LY_SECTION_WHITE = 10    # 'Trennfolie, weißer Hintergrund'
LY_AGENDA = 6            # 'Agenda'
LY_CONTENT = 12          # 'Titel, Untertitel, Inhalt groß'
LY_TWO_COL = 16          # 'Titel, Untertitel, zwei Inhalte'
LY_THREE_COL = 17        # 'Titel, Untertitel, drei Inhalte'
LY_ONLY_TITLE = 27       # 'Nur Titel'
LY_BLANK = 36            # 'Leeres'


def set_font(run, size=14, bold=False, color=AOK_DARK_GRAY, name="AOK Bundesweit"):
    """Set font properties on a run."""
    run.font.size = Pt(size)
    run.font.bold = bold
    if color:
        run.font.color.rgb = color
    run.font.name = name


def add_paragraph(tf, text, size=14, bold=False, color=AOK_DARK_GRAY, space_after=Pt(6),
                  space_before=Pt(0), alignment=PP_ALIGN.LEFT, level=0, bullet=False):
    """Add a paragraph to a text frame."""
    p = tf.add_paragraph()
    p.alignment = alignment
    p.space_after = space_after
    p.space_before = space_before
    p.level = level
    run = p.add_run()
    run.text = text
    set_font(run, size=size, bold=bold, color=color)
    return p


def add_table(slide, rows, cols, left, top, width, height):
    """Add a table shape to a slide."""
    table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
    return table_shape.table


def style_table_cell(cell, text, size=10, bold=False, color=AOK_DARK_GRAY,
                     fill_color=None, alignment=PP_ALIGN.LEFT):
    """Style a table cell."""
    cell.text = ""
    p = cell.text_frame.paragraphs[0]
    p.alignment = alignment
    run = p.add_run()
    run.text = text
    set_font(run, size=size, bold=bold, color=color)
    cell.text_frame.word_wrap = True
    cell.vertical_anchor = MSO_ANCHOR.MIDDLE

    if fill_color:
        cell.fill.solid()
        cell.fill.fore_color.rgb = fill_color


def style_header_row(table, col_texts, fill_color=AOK_GREEN, text_color=AOK_WHITE):
    """Style the header row of a table."""
    for i, text in enumerate(col_texts):
        style_table_cell(table.cell(0, i), text, size=10, bold=True,
                         color=text_color, fill_color=fill_color,
                         alignment=PP_ALIGN.CENTER)


def set_column_widths(table, widths_cm):
    """Set column widths in cm."""
    for i, w in enumerate(widths_cm):
        table.columns[i].width = Cm(w)


def create_presentation():
    prs = Presentation(TEMPLATE)

    # Remove existing slides (the template has 1 example slide)
    while len(prs.slides) > 0:
        rId = prs.slides._sldIdLst[0].rId
        prs.part.drop_rel(rId)
        prs.slides._sldIdLst.remove(prs.slides._sldIdLst[0])

    # ============================================================
    # SLIDE 1: Title Slide
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_TITLE_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:  # Title
            ph.text = ""
            run = ph.text_frame.paragraphs[0].add_run()
            run.text = "VDI-Lösungen"
            set_font(run, size=40, bold=True, color=AOK_WHITE)
            p2 = ph.text_frame.add_paragraph()
            run2 = p2.add_run()
            run2.text = "Umfassende Vergleichsanalyse"
            set_font(run2, size=28, bold=False, color=AOK_WHITE)
        elif ph.placeholder_format.idx == 1:  # Subtitle
            ph.text = ""
            run = ph.text_frame.paragraphs[0].add_run()
            run.text = "Bewertung für öffentlich-rechtliche Einrichtungen"
            set_font(run, size=18, color=AOK_WHITE)
        elif ph.placeholder_format.idx == 17:  # Bottom left text
            ph.text = ""
            run = ph.text_frame.paragraphs[0].add_run()
            run.text = "März 2026"
            set_font(run, size=12, color=AOK_WHITE)

    # ============================================================
    # SLIDE 2: Agenda
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_AGENDA])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:  # Title
            ph.text = "Agenda"
        elif ph.placeholder_format.idx == 20:  # Content
            tf = ph.text_frame
            tf.clear()
            items = [
                "Ausgangslage und Zielsetzung",
                "Bewertete VDI-Lösungen im Überblick",
                "Einzelanalysen der sechs Lösungen",
                "Vergleichsmatrix und TCO-Kostenvergleich",
                "Datenschutz und IT-Sicherheit",
                "Vergaberechtliche Aspekte",
                "Bewertungsmatrix und Empfehlung",
                "Nächste Schritte",
            ]
            for i, item in enumerate(items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.level = 0
                p.space_after = Pt(10)
                run = p.add_run()
                run.text = f"{i+1}.  {item}"
                set_font(run, size=18, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 3: Ausgangslage
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Ausgangslage und Zielsetzung"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Warum eine VDI-Evaluierung?"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()
            items = [
                ("Ziel:", " Evaluierung geeigneter VDI-Lösungen für unsere öffentlich-rechtliche Einrichtung"),
                ("Anforderungen:", " Datenschutz (DSGVO), IT-Sicherheit (BSI), Vergaberecht (VgV/UVgO)"),
                ("Bewertungskriterien:", " Kosten, Datenschutz, Funktionalität, Support, Vergaberecht, Zukunftssicherheit"),
                ("Sechs Lösungen:", " Von klassisch On-Premises bis Cloud, von proprietär bis Open Source"),
                ("Zielgruppe:", " Entscheidungsträger IT und Geschäftsführung"),
            ]
            for i, (label, desc) in enumerate(items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.space_after = Pt(12)
                run_b = p.add_run()
                run_b.text = label
                set_font(run_b, size=15, bold=True, color=AOK_GREEN)
                run_t = p.add_run()
                run_t.text = desc
                set_font(run_t, size=15, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 4: Overview of Solutions
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_ONLY_TITLE])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Bewertete VDI-Lösungen im Überblick"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Sechs Lösungen — von On-Premises bis Cloud"

    # Add overview table
    rows_data = [
        ["Lösung", "Typ", "Hersteller", "Lizenzmodell"],
        ["Windows RDS", "On-Premises", "Microsoft", "CAL-basiert"],
        ["Azure Local", "Hybrid", "Microsoft", "Subscription"],
        ["Azure Virtual Desktop", "Cloud", "Microsoft", "Pay-as-you-go"],
        ["Omnissa Horizon", "On-Prem/Hybrid", "Omnissa (KKR)", "Subscription"],
        ["OpenDesktop", "On-Premises", "Community", "Open Source"],
        ["Proxmox + UDS", "On-Premises", "Proxmox/VirtualCable", "OS + kommerziell"],
    ]

    left, top = Cm(1.5), Cm(4.2)
    width, height = Cm(30), Cm(0.8 * len(rows_data))
    table = add_table(slide, len(rows_data), 4, left, top, width, height)
    set_column_widths(table, [7, 4.5, 8, 5.5])
    style_header_row(table, rows_data[0])
    for r in range(1, len(rows_data)):
        bg = RGBColor(0xF0, 0xF7, 0xF0) if r % 2 == 1 else None
        for c in range(4):
            style_table_cell(table.cell(r, c), rows_data[r][c], size=11, fill_color=bg)

    # ============================================================
    # SLIDE 5: Section Divider — Einzelanalysen
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_SECTION_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Einzelanalysen"
        elif ph.placeholder_format.idx == 11:
            ph.text = "Detailbewertung der sechs VDI-Lösungen"

    # ============================================================
    # SLIDES 6-11: Individual Solution Analysis (one per solution)
    # ============================================================
    solutions = [
        {
            "name": "Windows Terminal Server (RDS)",
            "subtitle": "Klassische sitzungsbasierte Desktop-Bereitstellung",
            "pros": [
                "Bewährt, breit dokumentiert, großes Ökosystem",
                "Nahtlose AD- und M365-Integration",
                "RDP-Clients auf allen Plattformen",
                "RemoteApps: Einzelanwendungen ohne Full-Desktop",
                "Vorhandenes Know-how in den meisten IT-Abteilungen",
                "Volle On-Premises-Kontrolle",
            ],
            "cons": [
                "Keine echte VDI (sitzungsbasiert, geteiltes OS)",
                "Skalierungsgrenzen (~50-80 User/Server)",
                "Eingeschränkte Multimedia/GPU-Performance",
                "Steigende CAL-Kosten bei Wachstum",
                "Kein modernes zentrales Management",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~255.000 €",
            "cost_per_user": "~510 €/User/Jahr",
        },
        {
            "name": "Azure Local (ehem. Azure Stack HCI)",
            "subtitle": "Hybrid: Azure-Dienste auf eigener Hardware",
            "pros": [
                "Daten bleiben im eigenen RZ",
                "AVD on-premises möglich",
                "Azure-Management (Arc) und -Dienste lokal nutzbar",
                "Skalierbar (2-16 Knoten pro Cluster)",
                "Volle Microsoft-Ökosystem-Kompatibilität",
            ],
            "cons": [
                "Azure-Verbindung für Management zwingend erforderlich",
                "Hohe Einstiegskosten (zertifizierte HCI-Hardware)",
                "Komplexe Lizenzierung (Hardware + Cloud + User)",
                "Starker Microsoft-Lock-in",
                "Azure-Subscription auch bei reinem On-Prem nötig",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~625.000 €",
            "cost_per_user": "~1.250 €/User/Jahr",
        },
        {
            "name": "Azure Virtual Desktop (Cloud)",
            "subtitle": "Vollständig cloudbasierte VDI in Microsoft Azure",
            "pros": [
                "Keine eigene Hardware nötig",
                "Elastische Skalierung (Autoscaling)",
                "Multi-Session Windows 11 (einzigartig)",
                "Integrierte Sicherheit (Defender, MFA)",
                "FSLogix-Profile, M365-Optimierung",
                "Schnelle Bereitstellung in Minuten",
            ],
            "cons": [
                "Datensouveränität kritisch (CLOUD Act, Schrems-II)",
                "Laufende Kosten bei Dauerbetrieb hoch",
                "Vollständige Internetabhängigkeit",
                "Starker Vendor-Lock-in (Azure)",
                "Komplexe Kostenprognose (verbrauchsbasiert)",
                "Rechtliche Unsicherheit für öffentl. Einrichtungen",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~620.000 €",
            "cost_per_user": "~1.240 €/User/Jahr",
        },
        {
            "name": "Omnissa Horizon (ehem. VMware)",
            "subtitle": "Enterprise-VDI — seit 07/2024 unter KKR (ex-Broadcom/VMware)",
            "pros": [
                "Vollwertige VDI mit dedizierter VM pro Nutzer",
                "Blast Extreme: Bestes Display-Protokoll (WAN)",
                "Instant Clones, App Volumes, DEM",
                "Windows + Linux als Gast-OS",
                "Unter Omnissa: eigene Roadmap, besserer Support",
                "Flexible Deployment (On-Prem, SaaS, DaaS)",
            ],
            "cons": [
                "vSphere-Kosten (Broadcom): 3-12x teurer geworden",
                "Nur noch Subscription (keine Perpetual-Lizenzen)",
                "Komplexe Infrastruktur (vSphere, vCenter, UAG)",
                "Unsichere Langfrist-Strategie (KKR = Private Equity)",
                "Basic Support abgekündigt (nur noch Production)",
                "Starker Vendor-Lock-in",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~675.000 €",
            "cost_per_user": "~1.350 €/User/Jahr",
        },
        {
            "name": "Open Source — OpenDesktop",
            "subtitle": "KVM/QEMU + Guacamole + XRDP + oVirt",
            "pros": [
                "Keine Lizenzkosten (Kernkomponenten frei)",
                "Maximale Transparenz (Quellcode einsehbar)",
                "Volle Datensouveränität, keine Telemetrie",
                "Vendor-unabhängig, fördert Wettbewerb",
                "Linux-native, BSI-Audit möglich",
                "Vergaberechtlich vorteilhaft",
            ],
            "cons": [
                "Kein einheitliches Produkt — Integration nötig",
                "Windows als Gast erfordert weiterhin MS-Lizenzen",
                "Kein kommerzieller Support aus einer Hand",
                "Hoher Integrationsaufwand und Personalkosten",
                "Display-Performance hinter proprietären Protokollen",
                "Wenig Referenzen in deutschen Behörden",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~370.000 €",
            "cost_per_user": "~740 €/User/Jahr",
        },
        {
            "name": "Proxmox VE + UDS Enterprise",
            "subtitle": "Open-Source-Hypervisor + professioneller VDI-Broker (EU-Hersteller)",
            "pros": [
                "Proxmox kostenlos nutzbar (Community Edition)",
                "UDS Enterprise: Enterprise-VDI-Features",
                "EU-Hersteller (Österreich/Spanien) — DSGVO-konform",
                "Multi-Protokoll (RDP, SPICE, HTML5, X2Go)",
                "Kosteneffizient vs. VMware/Citrix",
                "Referenzen im öffentlichen Sektor (Spanien)",
            ],
            "cons": [
                "Geringere Marktpräsenz in Deutschland",
                "UDS Enterprise ist kommerziell (nicht Open Source)",
                "Kein BSI-/CC-Zertifikat für Proxmox",
                "Kleineres Ökosystem und weniger Partner",
                "Kein FSLogix/App Volumes-Äquivalent",
                "Know-how-Aufbau in DACH noch begrenzt",
            ],
            "cost_label": "TCO 5J / 100 User",
            "cost_value": "~325.000 €",
            "cost_per_user": "~650 €/User/Jahr",
        },
    ]

    for sol in solutions:
        slide = prs.slides.add_slide(prs.slide_layouts[LY_TWO_COL])
        for ph in slide.placeholders:
            if ph.placeholder_format.idx == 0:  # Title
                ph.text = sol["name"]
            elif ph.placeholder_format.idx == 15:  # Subtitle
                ph.text = sol["subtitle"]
            elif ph.placeholder_format.idx == 16:  # Left content - Vorteile
                tf = ph.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                run = p.add_run()
                run.text = "Vorteile"
                set_font(run, size=14, bold=True, color=AOK_GREEN)
                p.space_after = Pt(6)
                for item in sol["pros"]:
                    p = tf.add_paragraph()
                    p.level = 0
                    p.space_after = Pt(3)
                    run = p.add_run()
                    run.text = f"+ {item}"
                    set_font(run, size=10, color=AOK_DARK_GRAY)
                # Cost info at bottom
                p = tf.add_paragraph()
                p.space_before = Pt(12)
                run = p.add_run()
                run.text = f"{sol['cost_label']}: {sol['cost_value']} ({sol['cost_per_user']})"
                set_font(run, size=11, bold=True, color=AOK_GREEN)

            elif ph.placeholder_format.idx == 17:  # Right content - Nachteile
                tf = ph.text_frame
                tf.clear()
                p = tf.paragraphs[0]
                run = p.add_run()
                run.text = "Nachteile"
                set_font(run, size=14, bold=True, color=AOK_RED)
                p.space_after = Pt(6)
                for item in sol["cons"]:
                    p = tf.add_paragraph()
                    p.level = 0
                    p.space_after = Pt(3)
                    run = p.add_run()
                    run.text = f"– {item}"
                    set_font(run, size=10, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 12: Section Divider — Vergleich
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_SECTION_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Vergleich und\nKostenanalyse"
        elif ph.placeholder_format.idx == 11:
            ph.text = "Gegenüberstellung aller sechs Lösungen"

    # ============================================================
    # SLIDE 13: Comparison Matrix
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_ONLY_TITLE])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Vergleichsmatrix — Kerneigenschaften"
        elif ph.placeholder_format.idx == 15:
            ph.text = ""

    headers = ["Kriterium", "RDS", "Azure\nLocal", "AVD\n(Cloud)", "Omnissa\nHorizon", "Open\nDesktop", "Proxmox\n+ UDS"]
    data = [
        ["Deployment", "On-Prem", "Hybrid", "Cloud", "On-Prem/\nHybrid", "On-Prem", "On-Prem"],
        ["Echte VDI", "Nein", "Ja", "Ja", "Ja", "Ja", "Ja"],
        ["Multi-Session", "Ja", "Ja", "Ja", "Ja", "Eingeschr.", "Eingeschr."],
        ["Linux-Desktop", "Eingeschr.", "Ja", "Eingeschr.", "Ja", "Ja (nativ)", "Ja (nativ)"],
        ["Display-Protokoll", "RDP", "RDP", "RDP opt.", "Blast\nExtreme", "VNC/SPICE", "SPICE/RDP\n/HTML5"],
        ["WAN-Perform.", "Mittel", "Mittel-Gut", "Gut", "Sehr gut", "Gering-\nMittel", "Mittel"],
        ["Automatisierung", "Gering", "Hoch", "Sehr hoch", "Hoch", "Gering", "Mittel"],
        ["Vendor-Lock-in", "Mittel", "Hoch", "Sehr hoch", "Hoch", "Keiner", "Gering"],
        ["Datensouveränität", "Hoch", "Mittel-\nHoch", "Gering", "Hoch", "Sehr hoch", "Sehr hoch"],
        ["Reifegrad", "Sehr hoch", "Hoch", "Hoch", "Sehr hoch", "Mittel", "Mittel-\nHoch"],
    ]

    n_rows = len(data) + 1
    n_cols = 7
    left, top = Cm(1.5), Cm(3.5)
    width, height = Cm(30.5), Cm(0.75 * n_rows)
    table = add_table(slide, n_rows, n_cols, left, top, width, height)
    set_column_widths(table, [4.5, 3.5, 3.5, 3.5, 4, 3.5, 4])
    style_header_row(table, headers)

    # Color-code cells based on content
    color_map = {
        "Ja": RGBColor(0xE8, 0xF5, 0xE9),
        "Ja (nativ)": RGBColor(0xE8, 0xF5, 0xE9),
        "Sehr hoch": RGBColor(0xE8, 0xF5, 0xE9),
        "Hoch": RGBColor(0xF1, 0xF8, 0xE9),
        "Sehr gut": RGBColor(0xE8, 0xF5, 0xE9),
        "Gut": RGBColor(0xF1, 0xF8, 0xE9),
        "Nein": RGBColor(0xFF, 0xEB, 0xEE),
        "Gering": RGBColor(0xFF, 0xEB, 0xEE),
        "Eingeschr.": RGBColor(0xFF, 0xF3, 0xE0),
        "Keiner": RGBColor(0xE8, 0xF5, 0xE9),
        "Sehr hoch": RGBColor(0xE8, 0xF5, 0xE9),
    }

    for r, row_data in enumerate(data):
        for c, cell_text in enumerate(row_data):
            clean = cell_text.replace("\n", "")
            bg = color_map.get(clean, None) if c > 0 else RGBColor(0xF5, 0xF5, 0xF5)
            bold = c == 0
            align = PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT
            style_table_cell(table.cell(r + 1, c), cell_text, size=9, bold=bold,
                             fill_color=bg, alignment=align)

    # ============================================================
    # SLIDE 14: TCO Cost Comparison
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_ONLY_TITLE])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "TCO-Kostenvergleich — 5 Jahre, 100 Benutzer"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Total Cost of Ownership inkl. Hardware, Lizenzen, Support, Personal"

    tco_headers = ["Kostenposition", "RDS", "Azure\nLocal", "AVD\n(Cloud)", "Omnissa\nHorizon", "Open\nDesktop", "Proxmox\n+ UDS"]
    tco_data = [
        ["Hardware (einmalig)", "30.000 €", "70.000 €", "0 €", "60.000 €", "45.000 €", "45.000 €"],
        ["Lizenzen (5 J.)", "60.000 €", "350.000 €", "500.000 €", "350.000 €", "0 €", "50.000 €"],
        ["Windows-Lizenzen (5 J.)", "20.000 €", "inkl.", "inkl.", "60.000 €", "60.000 €", "60.000 €"],
        ["Support (5 J.)", "30.000 €", "50.000 €", "25.000 €", "50.000 €", "50.000 €", "25.000 €"],
        ["Implementierung", "15.000 €", "30.000 €", "20.000 €", "30.000 €", "40.000 €", "20.000 €"],
        ["Internes Personal (5 J.)", "100.000 €", "125.000 €", "75.000 €", "125.000 €", "175.000 €", "125.000 €"],
        ["TCO 5 Jahre", "~255.000 €", "~625.000 €", "~620.000 €", "~675.000 €", "~370.000 €", "~325.000 €"],
        ["TCO pro User/Jahr", "~510 €", "~1.250 €", "~1.240 €", "~1.350 €", "~740 €", "~650 €"],
    ]

    n_rows = len(tco_data) + 1
    left, top = Cm(1.5), Cm(3.5)
    width, height = Cm(30.5), Cm(0.7 * n_rows)
    table = add_table(slide, n_rows, 7, left, top, width, height)
    set_column_widths(table, [5.5, 3.5, 3.5, 3.5, 3.5, 3.5, 4])
    style_header_row(table, tco_headers)

    for r, row_data in enumerate(tco_data):
        is_total = r >= len(tco_data) - 2
        for c, cell_text in enumerate(row_data):
            bg = AOK_GREEN if is_total else (RGBColor(0xF0, 0xF7, 0xF0) if r % 2 == 0 else None)
            txt_color = AOK_WHITE if is_total else AOK_DARK_GRAY
            bold = c == 0 or is_total
            align = PP_ALIGN.RIGHT if c > 0 else PP_ALIGN.LEFT
            style_table_cell(table.cell(r + 1, c), cell_text, size=9, bold=bold,
                             color=txt_color, fill_color=bg, alignment=align)

    # ============================================================
    # SLIDE 15: Section Divider — Datenschutz
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_SECTION_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Datenschutz und\nIT-Sicherheit"
        elif ph.placeholder_format.idx == 11:
            ph.text = "DSGVO, BSI, Schrems-II, CLOUD Act"

    # ============================================================
    # SLIDE 16: Data Sovereignty Assessment
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_ONLY_TITLE])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Datensouveränität — Risikobewertung"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Schrems-II / CLOUD Act Analyse für öffentlich-rechtliche Einrichtungen"

    ds_headers = ["Lösung", "Datenstandort", "US-Zugriff\nmöglich?", "Schrems-II\nRisiko", "Bewertung"]
    ds_data = [
        ["RDS", "Eigenes RZ", "Nein", "Gering", "Sehr gut"],
        ["Azure Local", "Eigenes RZ\n(Mgmt: Azure)", "Metadaten:\nJa", "Mittel", "Gut"],
        ["AVD (Cloud)", "Azure-RZ\n(EU möglich)", "Ja\n(CLOUD Act)", "Hoch", "Kritisch"],
        ["Omnissa Horizon", "Eigenes RZ", "Nein\n(On-Prem)", "Gering", "Sehr gut"],
        ["OpenDesktop", "Eigenes RZ", "Nein", "Sehr gering", "Sehr gut"],
        ["Proxmox + UDS", "Eigenes RZ", "Nein", "Sehr gering", "Sehr gut"],
    ]

    n_rows = len(ds_data) + 1
    left, top = Cm(1.5), Cm(3.5)
    width, height = Cm(30.5), Cm(0.9 * n_rows)
    table = add_table(slide, n_rows, 5, left, top, width, height)
    set_column_widths(table, [5.5, 5, 5, 5, 5])
    style_header_row(table, ds_headers)

    risk_colors = {
        "Sehr gut": RGBColor(0xE8, 0xF5, 0xE9),
        "Gut": RGBColor(0xF1, 0xF8, 0xE9),
        "Kritisch": RGBColor(0xFF, 0xEB, 0xEE),
        "Gering": RGBColor(0xE8, 0xF5, 0xE9),
        "Sehr gering": RGBColor(0xE8, 0xF5, 0xE9),
        "Mittel": RGBColor(0xFF, 0xF3, 0xE0),
        "Hoch": RGBColor(0xFF, 0xEB, 0xEE),
    }

    for r, row_data in enumerate(ds_data):
        for c, cell_text in enumerate(row_data):
            bg = None
            if c == 3:  # Risiko column
                bg = risk_colors.get(cell_text.strip(), None)
            elif c == 4:  # Bewertung column
                bg = risk_colors.get(cell_text.strip(), None)
            bold = c == 0
            align = PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT
            style_table_cell(table.cell(r + 1, c), cell_text, size=11, bold=bold,
                             fill_color=bg, alignment=align)

    # ============================================================
    # SLIDE 17: Datenschutz Empfehlungen
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Datenschutz — Empfehlungen und Rahmenbedingungen"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Regulatorischer Rahmen für öffentlich-rechtliche Einrichtungen"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()
            sections = [
                ("Bevorzugt:", " On-Premises-Lösungen (RDS, Omnissa Horizon, Proxmox + UDS, OpenDesktop)"),
                ("Bedingt geeignet:", " Azure Local (Hybrid) — nach DSFA und mit organisatorischen Maßnahmen"),
                ("Kritisch:", " AVD Cloud — nur nach umfassender DSFA und Genehmigung durch DSB"),
                ("", ""),
                ("BSI C5:2025:", " Erweiterte Kontrollen, Souveränitätskriterien — verpflichtend ab 01/2027"),
                ("Delos Cloud:", " Souveräne Azure-Alternative unter deutscher Betriebsführung (SAP/Delos GmbH)"),
                ("DVC:", " Deutsche Verwaltungscloud seit 04/2025 produktiv — vereinfachte Beschaffung"),
                ("", ""),
                ("Landesdatenschutzbeauftragte:", " Einsatz von MS 365/Azure in öffentl. Verwaltung als problematisch eingestuft"),
            ]
            for i, (label, desc) in enumerate(sections):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                if not label and not desc:
                    p.space_after = Pt(4)
                    continue
                p.space_after = Pt(6)
                if label:
                    run_b = p.add_run()
                    run_b.text = label
                    color = AOK_GREEN if "Bevorzugt" in label or "BSI" in label or "Delos" in label or "DVC" in label else (AOK_ORANGE if "Bedingt" in label else AOK_RED)
                    set_font(run_b, size=12, bold=True, color=color)
                run_t = p.add_run()
                run_t.text = desc
                set_font(run_t, size=12, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 18: Section Divider — Vergaberecht
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_SECTION_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Vergaberechtliche\nAspekte"
        elif ph.placeholder_format.idx == 11:
            ph.text = "EU-Schwellenwerte, VgV, UVgO, EVB-IT"

    # ============================================================
    # SLIDE 19: Vergaberecht
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_TWO_COL])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Vergaberecht — Schwellenwerte und Verfahren"
        elif ph.placeholder_format.idx == 15:
            ph.text = "EU-Schwellenwerte seit 01.01.2026"
        elif ph.placeholder_format.idx == 16:  # Left
            tf = ph.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = "EU-Schwellenwerte (netto)"
            set_font(run, size=13, bold=True, color=AOK_GREEN)

            items = [
                ("Bundesbehörden:", " 140.000 €"),
                ("Sonstige öffentl. AG:", " 216.000 €"),
                ("Sektorenauftraggeber:", " 432.000 €"),
                ("", ""),
                ("Unterschwellenbereich (UVgO):", ""),
                ("Direktvergabe:", " bis 100.000 € möglich"),
                ("", ""),
                ("Praxis:", " Bei VDI-Projekten wird der Schwellenwert über die Vertragslaufzeit (5 J.) fast immer überschritten → EU-weite Ausschreibung erforderlich"),
            ]
            for label, val in items:
                p = tf.add_paragraph()
                p.space_after = Pt(4)
                if not label and not val:
                    continue
                if label:
                    run = p.add_run()
                    run.text = label
                    set_font(run, size=11, bold=True, color=AOK_DARK_GRAY)
                if val:
                    run = p.add_run()
                    run.text = val
                    set_font(run, size=11, color=AOK_DARK_GRAY)

        elif ph.placeholder_format.idx == 17:  # Right
            tf = ph.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            run = p.add_run()
            run.text = "EVB-IT Vertragstypen"
            set_font(run, size=13, bold=True, color=AOK_GREEN)

            evb_items = [
                "EVB-IT System — On-Premises VDI + Hardware",
                "EVB-IT Cloud — Cloud-VDI (AVD, Azure Local); C5-Testat erforderlich",
                "EVB-IT Überlassung Typ B — Softwarelizenzen (z.B. UDS Enterprise)",
                "EVB-IT Pflege S — Wartung und Patching",
                "EVB-IT Dienstvertrag — Implementierung/Beratung",
                "EVB-IT Rahmenvereinbarung — Modulare VDI-Leistungen",
                "",
                "Pflicht: EVB-IT für Bundesbehörden (§ 55 BHO)",
            ]
            for item in evb_items:
                p = tf.add_paragraph()
                p.space_after = Pt(4)
                if not item:
                    continue
                run = p.add_run()
                run.text = item
                bold = "Pflicht" in item
                set_font(run, size=10, bold=bold, color=AOK_RED if bold else AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 20: Ausschreibungshinweise
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Ausschreibungshinweise"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Empfohlene Zuschlagskriterien und produktneutrale Vergabe"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()
            items = [
                ("Produktneutrale Ausschreibung:", " Funktionale Anforderungen definieren, kein Produkt vorschreiben (§ 31 Abs. 6 VgV)"),
                ("Losaufteilung:", " Hardware, Software, Dienstleistungen ggf. in separate Lose (§ 97 Abs. 4 GWB)"),
                ("", ""),
                ("Empfohlene Zuschlagskriterien:", ""),
                ("  Preis:", " 30–40 %"),
                ("  Technische Leistungsfähigkeit:", " 20–30 %"),
                ("  Datenschutz / IT-Sicherheit:", " 15–25 %"),
                ("  Support und SLA:", " 10–15 %"),
                ("  Migrationsfähigkeit / Exit-Strategie:", " 5–10 %"),
            ]
            for i, (label, val) in enumerate(items):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.space_after = Pt(6)
                if not label and not val:
                    continue
                if label:
                    run = p.add_run()
                    run.text = label
                    set_font(run, size=13, bold=True, color=AOK_GREEN if "Empfohlene" not in label else AOK_GREEN)
                if val:
                    run = p.add_run()
                    run.text = val
                    set_font(run, size=13, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 21: Section Divider — Empfehlung
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_SECTION_GREEN])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Bewertung und\nEmpfehlung"
        elif ph.placeholder_format.idx == 11:
            ph.text = "Gewichtete Bewertungsmatrix"

    # ============================================================
    # SLIDE 22: Scoring Matrix
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_ONLY_TITLE])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Gewichtete Bewertungsmatrix"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Skala: 1 (schlecht) bis 10 (sehr gut)"

    score_headers = ["Kriterium (Gewicht)", "RDS", "Azure\nLocal", "AVD\n(Cloud)", "Omnissa\nHorizon", "Open\nDesktop", "Proxmox\n+ UDS"]
    score_data = [
        ["Kosten (25 %)", "9", "5", "4", "3", "7", "8"],
        ["Datenschutz (25 %)", "8", "6", "3", "7", "10", "9"],
        ["Funktionsumfang (15 %)", "5", "8", "9", "9", "4", "7"],
        ["Support (10 %)", "8", "7", "8", "5", "3", "6"],
        ["Vergaberecht (10 %)", "7", "6", "5", "4", "9", "8"],
        ["Zukunftssicherheit (10 %)", "6", "8", "8", "4", "6", "7"],
        ["Betriebsaufwand (5 %)", "8", "5", "9", "5", "3", "6"],
        ["Gewichtete Summe", "7,45", "6,25", "5,60", "5,35", "6,55", "7,70"],
    ]

    n_rows = len(score_data) + 1
    left, top = Cm(1.5), Cm(3.5)
    width, height = Cm(30.5), Cm(0.85 * n_rows)
    table = add_table(slide, n_rows, 7, left, top, width, height)
    set_column_widths(table, [6, 3.5, 3.5, 3.5, 3.5, 3.5, 4])
    style_header_row(table, score_headers)

    def score_color(val_str):
        try:
            v = float(val_str.replace(",", "."))
            if v >= 8:
                return RGBColor(0xC8, 0xE6, 0xC9)
            elif v >= 6:
                return RGBColor(0xE8, 0xF5, 0xE9)
            elif v >= 4:
                return RGBColor(0xFF, 0xF3, 0xE0)
            else:
                return RGBColor(0xFF, 0xEB, 0xEE)
        except ValueError:
            return None

    for r, row_data in enumerate(score_data):
        is_total = r == len(score_data) - 1
        for c, cell_text in enumerate(row_data):
            if is_total:
                bg = AOK_GREEN
                txt_color = AOK_WHITE
            elif c == 0:
                bg = RGBColor(0xF5, 0xF5, 0xF5)
                txt_color = AOK_DARK_GRAY
            else:
                bg = score_color(cell_text)
                txt_color = AOK_DARK_GRAY
            bold = c == 0 or is_total
            align = PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT
            style_table_cell(table.cell(r + 1, c), cell_text, size=11, bold=bold,
                             color=txt_color, fill_color=bg, alignment=align)

    # ============================================================
    # SLIDE 23: Ranking & Recommendation
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Rangfolge und Handlungsempfehlung"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Ergebnis der gewichteten Bewertung"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()

            rankings = [
                ("1.", "Proxmox + UDS Enterprise", "7,70", "Bestes Gesamtpaket: Kosten, Datenschutz, Funktionalität"),
                ("2.", "Windows RDS", "7,45", "Günstigste Lösung, aber keine echte VDI"),
                ("3.", "OpenDesktop", "6,55", "Maximale Datensouveränität, hoher Personalaufwand"),
                ("4.", "Azure Local", "6,25", "Guter Kompromiss, aber teuer und MS-abhängig"),
                ("5.", "Azure Virtual Desktop", "5,60", "Technisch stark, Datenschutz kritisch"),
                ("6.", "Omnissa Horizon", "5,35", "Technisch ausgereift, Kosten-/KKR-Risiko"),
            ]

            for i, (rank, name, score, note) in enumerate(rankings):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.space_after = Pt(8)
                # Rank
                run = p.add_run()
                run.text = f"{rank} "
                color = AOK_GREEN if i < 2 else (AOK_ORANGE if i < 4 else AOK_RED)
                set_font(run, size=14, bold=True, color=color)
                # Name + Score
                run = p.add_run()
                run.text = f"{name} ({score})  "
                set_font(run, size=14, bold=True, color=AOK_DARK_GRAY)
                # Note
                run = p.add_run()
                run.text = f"— {note}"
                set_font(run, size=12, color=AOK_GRAY)

    # ============================================================
    # SLIDE 24: Handlungsempfehlung
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Handlungsempfehlung"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Strategische Empfehlung für die VDI-Einführung"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()

            recommendations = [
                ("Kurzfristig / einfache Anforderungen:",
                 "Windows RDS als bewährte, kostengünstige Lösung für sitzungsbasierte Desktops"),
                ("Mittelfristig / VDI-Einstieg:",
                 "Proxmox VE + UDS Enterprise als kosteneffiziente, datenschutzkonforme Lösung mit europäischen Herstellern"),
                ("Strategisch / Digitale Souveränität:",
                 "Evaluierung einer Open-Source-Strategie (Proxmox/OpenDesktop) im Einklang mit der Digitalstrategie der öffentlichen Verwaltung"),
                ("Mit Vorsicht:",
                 "Omnissa Horizon (KKR-/vSphere-Kostenrisiko) und reine AVD-Cloud (Datenschutzrisiko) nur nach umfassender Risiko- und Kosten-Analyse; AVD ggf. über Delos Cloud evaluieren"),
            ]

            for i, (title, desc) in enumerate(recommendations):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.space_after = Pt(4)
                p.space_before = Pt(8)
                run = p.add_run()
                run.text = title
                color = AOK_GREEN if i < 3 else AOK_ORANGE
                set_font(run, size=14, bold=True, color=color)

                p2 = tf.add_paragraph()
                p2.space_after = Pt(8)
                run2 = p2.add_run()
                run2.text = desc
                set_font(run2, size=13, color=AOK_DARK_GRAY)

    # ============================================================
    # SLIDE 25: Next Steps
    # ============================================================
    slide = prs.slides.add_slide(prs.slide_layouts[LY_CONTENT])
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 0:
            ph.text = "Nächste Schritte"
        elif ph.placeholder_format.idx == 15:
            ph.text = "Fahrplan zur VDI-Einführung"
        elif ph.placeholder_format.idx == 14:
            tf = ph.text_frame
            tf.clear()

            steps = [
                ("1.", "Anforderungsanalyse", "Exakte Nutzerzahl, Anwendungslandschaft, Performance definieren"),
                ("2.", "Datenschutz-Folgenabschätzung (DSFA)", "Durchführung für favorisierte Lösungen"),
                ("3.", "Proof of Concept (PoC)", "Pilotierung mit 2-3 favorisierten Lösungen"),
                ("4.", "Abstimmung mit dem DSB", "Datenschutzbeauftragten einbeziehen"),
                ("5.", "Marktrecherche (§ 28 VgV)", "Markterkundung und Lieferantengespräche"),
                ("6.", "Vergabeunterlage erstellen", "Funktionale Leistungsbeschreibung"),
                ("7.", "EU-weite Ausschreibung", "Sofern Schwellenwert überschritten (sehr wahrscheinlich)"),
            ]

            for i, (num, title, desc) in enumerate(steps):
                if i == 0:
                    p = tf.paragraphs[0]
                else:
                    p = tf.add_paragraph()
                p.space_after = Pt(2)
                run = p.add_run()
                run.text = f"{num}  {title}"
                set_font(run, size=14, bold=True, color=AOK_GREEN)

                p2 = tf.add_paragraph()
                p2.space_after = Pt(8)
                run2 = p2.add_run()
                run2.text = f"     {desc}"
                set_font(run2, size=12, color=AOK_GRAY)

    # ============================================================
    # Save
    # ============================================================
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    prs.save(OUTPUT)
    print(f"Presentation saved to: {OUTPUT}")
    print(f"Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    create_presentation()
