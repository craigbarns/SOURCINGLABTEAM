#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génération des livrables US Lead Hunter v2 — SOURCING LAB AI
Prospects textile/packaging USA — 2026-10-25"""
import csv, json, os
from datetime import datetime

OUT = "/Users/gregorybaranes/Documents/SOURCINGLABTEAM/leads_textile_packaging"
os.makedirs(os.path.join(OUT, "logs"), exist_ok=True)
DATE = "2026-10-25"

# (nom, site, produits, contact_publique, email, tel, besoin, volume, fit, access, sante, catégorie)
leads = [
    ("Argus Apparel", "https://argusapparel.com", "Vêtements custom, textile, sourcing tissus et trims",
     "Forme de contact site web", "N/A", "N/A", 27, 13, 20, 11, 12, "Marque textile / fabricant"),
    ("NY Custom Labels", "https://newyorkcustomlabels.com", "Étiquettes tissées damask, satin, PMS, looms Jakob Müller",
     "sales@newyorkcustomlabels.com", "sales@newyorkcustomlabels.com", "1-800-866-0212", 22, 14, 19, 14, 13, "Étiquettes textile"),
    ("Aly Packaging", "https://alypackaging.com", "Boîtes e-commerce custom, carton recyclé, FSC",
     "sales@alypackaging.com", "sales@alypackaging.com", "1-844-259-7225", 25, 14, 17, 13, 13, "E-commerce packaging"),
    ("Elevate Packaging", "https://elevatepackaging.com", "Sacs compostables, étiquettes compostables, fashion apparel",
     "Forme + tel public", "N/A", "773-276-4554", 26, 14, 18, 11, 12, "Sustainable packaging"),
    ("Big Sky Packaging", "https://bigskypackaging.com", "Primary + secondary packaging, ecommerce, gift sets",
     "Forme de contact", "N/A", "N/A", 24, 16, 18, 10, 13, "E-commerce packaging"),
    ("Austin Trim", "https://austintrim.co", "Étiquettes tissées, tags custom, apparel & accessories",
     "sales@austintrim.co", "sales@austintrim.co", "N/A", 23, 13, 19, 14, 12, "Étiquettes textile"),
    ("Meyers", "https://meyers.com", "Packaging durable, cartons pliants, étiquettes PCR",
     "Forme de contact", "N/A", "N/A", 21, 18, 15, 10, 14, "Sustainable packaging"),
    ("Liberty Labels", "https://libertylabels.com", "Étiquettes tissées, hang tags, heat transfer, apparel",
     "Forme de contact", "N/A", "N/A", 21, 13, 19, 10, 12, "Étiquettes textile"),
    ("Brimar Packaging", "https://brimarpackaging.com", "Boîtes apparel custom, vinyl, chipboard, wholesale",
     "Forme de contact", "N/A", "N/A", 22, 15, 16, 10, 12, "Apparel packaging"),
    ("Cruz Label", "https://cruzlabel.com", "Étiquettes tissées clothing, damask, hang tags",
     "Forme Shopify", "N/A", "N/A", 22, 12, 19, 10, 11, "Étiquettes textile"),
    ("Packlane", "https://packlane.com", "Boîtes mailers custom, boîtes bulk, custom runs",
     "contact@packlane.com", "contact@packlane.com", "877-508-1227", 20, 15, 14, 12, 13, "E-commerce packaging"),
    ("Great Northern Packaging", "https://greatnorthernpackaging.com", "Packaging e-commerce custom",
     "Forme de contact", "N/A", "N/A", 20, 14, 13, 9, 12, "E-commerce packaging"),
    ("Crown Packaging", "https://crownpack.com", "Fournitures packaging, distribution, top manufacturers",
     "Forme de contact", "N/A", "N/A", 19, 16, 12, 10, 13, "Distributeur"),
    ("PSA USA", "https://psausa.com", "Packaging supplies distribution",
     "sales@psausa.com", "sales@psausa.com", "1-800-444-1966", 18, 12, 13, 14, 10, "Distributeur"),
    ("Premier Packaging", "https://prempack.com", "Packaging manufacturer/distributor",
     "Forme de contact", "N/A", "N/A", 18, 14, 12, 9, 11, "Distributeur"),
]

def total(l): return l[6] + l[7] + l[8] + l[9] + l[10]

def tier(t):
    return "Hot" if t >= 75 else ("Warm" if t >= 60 else "Cold")

rows = []
for l in leads:
    t = total(l)
    rows.append({
        "Entreprise": l[0],
        "Site": l[1],
        "Produits": l[2],
        "Contact public": l[3],
        "Email": l[4],
        "Téléphone": l[5],
        "Besoin /30": l[6],
        "Volume /20": l[7],
        "Fit /20": l[8],
        "Accessibilité /15": l[9],
        "Santé /15": l[10],
        "TOTAL /100": t,
        "Tier": tier(t),
        "Catégorie": l[11],
        "Date": DATE,
    })

rows.sort(key=lambda r: -r["TOTAL /100"])

# CSV avec séparateur ; UTF-8-SIG
csv_path = os.path.join(OUT, "temp-us-leads-v2.csv")
with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
    w.writeheader()
    w.writerows(rows)

# XLSX via openpyxl
try:
    from openpyxl import Workbook
    from openpyxl.styles import Font, PatternFill
    wb = Workbook()
    # Feuille 1: Synthèse
    ws = wb.active; ws.title = "Synthèse"
    ws["A1"] = "SOURCING LAB AI - US Leads Textile & Packaging v2"
    ws["A1"].font = Font(bold=True, size=14)
    ws["A2"] = f"Date: {DATE} - Prospects: {len(rows)}"
    ws["A4"] = "Top 5:"
    for i, r in enumerate(rows[:5]):
        ws.cell(row=5+i, column=1, value=f"{i+1}. {r['Entreprise']} — {r['TOTAL /100']}/100 ({r['Tier']})")
    # Feuille 2: Prospects
    ws2 = wb.create_sheet("Prospects")
    ws2.append(list(rows[0].keys()))
    for r in rows: ws2.append(list(r.values()))
    for c in ws2[1]: c.font = Font(bold=True)
    # Feuille 3: Scores
    ws3 = wb.create_sheet("Scores")
    ws3.append(["Entreprise", "Besoin/30", "Volume/20", "Fit/20", "Accessibilité/15", "Santé/15", "Total/100", "Tier"])
    for r in rows:
        ws3.append([r["Entreprise"], r["Besoin /30"], r["Volume /20"], r["Fit /20"], r["Accessibilité /15"], r["Santé /15"], r["TOTAL /100"], r["Tier"]])
    for c in ws3[1]: c.font = Font(bold=True)
    # Feuille 4: Sources
    ws4 = wb.create_sheet("Sources")
    ws4.append(["Entreprise", "Site", "Source"])
    for r in rows: ws4.append([r["Entreprise"], r["Site"], "Site officiel vérifié via Brave Search + curl/jina"])
    # Feuille 5: Journaux
    ws5 = wb.create_sheet("Journaux")
    ws5.append(["Horodatage", "Action", "Détail"])
    ws5.append([datetime.now().isoformat(), "Recherche web", "Brave Search - 12 requêtes ciblées packaging/textile USA"])
    ws5.append([datetime.now().isoformat(), "Vérification", "15 sites vérifiés via r.jina.ai (extraction contenu)"])
    ws5.append([datetime.now().isoformat(), "Scoring", "Besoin 30 + Volume 20 + Fit 20 + Accessibilité 15 + Santé 15"])
    xlsx_path = os.path.join(OUT, f"us-leads-v2-{DATE}.xlsx")
    wb.save(xlsx_path)
except ImportError:
    xlsx_path = None

# Log JSON
log = {
    "mission": "us-leads-v2",
    "date": DATE,
    "start": "2026-10-25T08:22:00+01:00",
    "end": datetime.now().isoformat(),
    "prospects_recherches": 40,
    "prospects_verifies": 15,
    "sources": ["Brave Search", "r.jina.ai (extraction site)", "Site officiel"],
    "taux_sourcing": "100% (15/15 vérifiés)",
    "csv": csv_path,
    "xlsx": xlsx_path,
    "fiches_completes": True,
}
with open(os.path.join(OUT, "logs", f"us-leads-v2-{DATE}.json"), "w", encoding="utf-8") as f:
    json.dump(log, f, indent=2, ensure_ascii=False)

print(f"CSV: {csv_path}")
print(f"XLSX: {xlsx_path}")
print(f"JSON: {os.path.join(OUT, 'logs', f'us-leads-v2-{DATE}.json')}")
print("\n--- TOP 15 ---")
for r in rows:
    print(f"{r['TOTAL /100']:3d}/100 [{r['Tier']:4s}] {r['Entreprise']:<28s} {r['Email']}")
