#!/usr/bin/env python3
# Génère le fichier Excel de prospection SOURCING LAB USA - mission USA-LEADS-20261024-001
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()

# ---------- Feuille Synthèse ----------
ws0 = wb.active
ws0.title = "Synthèse"
synth = [
    ["MISSION", "USA-LEADS-20261024-001 — Prospects clients pour Sourcing Lab USA"],
    ["Date", "2026-10-24"],
    ["Offre analysée", "https://sourcinglabusa.com — packaging & textiles custom, factory search, samples, QC, landed cost (contrat/facture France ou Chine)"],
    ["Cible", "10 PME/marques US importatrices de produits physiques avec besoins sourcing récurrents"],
    ["Prospects identifiés", "10 / 10 (sites officiels vérifiés)"],
    ["Besoins démontrés (preuves douanières ou presse)", "9 / 10 — Express Tile NY = besoin supposé"],
    ["Décideurs nommés publiquement", "5 / 10 (FAM, PPI, Faherty, REP, General Wax)"],
    ["Emails publics", "6 / 10"],
    ["TOP 1", "FAM Brands (87/100) — Bell, CA — 158 shipments CN prouvés, multi-marques textiles, CEO Frank Zarabi public"],
    ["TOP 2", "Gifts International (84/100) — Bloomington, CA — importateur direct packaging, 161 shipments CN, sales@giftsintl.com"],
    ["TOP 3", "PPI Apparel Group (82/100) — NYC — 795 shipments CN prouvés, intimes/textiles, CEO Abe Hanan"],
    ["Décision prospection", "GO — cibler d'abord TOP 3 + REP Fitness et General Wax (accessibilité maximale)"],
    ["Aucun contact effectué", "Conforme à la règle : aucun envoi, aucune sollicitation pendant la mission"],
    ["Coût API estimé", "≈ 0,15–0,25 USD (estimation tokens ; non mesuré par l'environnement)"],
    ["Durée", "≈ 10 minutes (22:41–22:51 UTC+2)"],
]
ws0.append(["Champ", "Valeur"])
for r in synth:
    ws0.append(r)
header_fill = PatternFill("solid", fgColor="1F4E79")
header_font = Font(color="FFFFFF", bold=True)
thin = Border(*[Side(style="thin", color="B0B0B0")] * 4)
for cell in ws0[1]:
    cell.fill = header_fill
    cell.font = header_font
ws0.column_dimensions["A"].width = 42
ws0.column_dimensions["B"].width = 120
for row in ws0.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = thin

# ---------- Feuille Prospects ----------
ws = wb.create_sheet("Prospects")
cols = ["Rang", "Score /100", "Nom", "Site officiel", "Secteur", "Produits",
        "Localisation USA", "Taille (si documentée)", "Preuves d'importation / approvisionnement international",
        "Type de besoin", "Besoins de sourcing potentiels", "Pourquoi acheter nos services",
        "Décideur", "Titre", "Email public", "Téléphone", "Page LinkedIn", "Sources"]
ws.append(cols)

rows = [
    [1, 87, "FAM Brands", "https://www.fambrands.com",
     "Textile / activewear — marques propriétaires & licences",
     "Activewear, bas et vêtements de sport (Marika, Three Dots, Ellie, Bally Total Fitness ; licences Bonobos, Eddie Bauer, Express, Orvis, Woolrich)",
     "Bell, CA (HQ) ; showroom New York, NY ; bureau Hong Kong",
     "PME multi-marques ; effectif non publié (4+ dirigeants dénommés sur le site)",
     "DÉMONTRÉ : ImportYeti — 158 shipments depuis la Chine, fournisseur principal Huaian Shengyuan Garments (https://www.importyeti.com/company/fam-brands) ; bureau FAM (HK) LIMITED (site officiel)",
     "Démontré",
     "Sourcing usines récurrent pour 8+ marques ; diversification supply chain (déclaration publique du CEO) ; contrôle qualité externe ; modèle de coût rendu par collection",
     "Volume multi-marques = besoins répétés de recherche d'usines et de QC ; Sourcing Lab offre contrat + échantillons + suivi production sans RH internes ; le CEO affiche publiquement une croyance en « diversified supply chain » = ouverture à de nouveaux partenaires sourcing",
     "Frank Zarabi", "President & CEO (fondateur, 2000)",
     "info@fambrands.com (contact) ; jspotts@fambrands.com ; rstone@fambrands.com (licences)", "",
     "https://www.linkedin.com/company/fambrandslife",
     "fambrands.com/pages/contact ; fambrands.com/pages/leadership ; importyeti.com/company/fam-brands ; linkedin.com/in/frank-zarabi-7a277926"],

    [2, 84, "Gifts International Inc", "https://www.giftsintl.com",
     "Packaging cadeau — fabrication, import direct, distribution",
     "Sacs organza/satin/velours, boîtes cadeaux papier, gift wrap, rubans, articles party",
     "Bloomington, CA (entrepôt Los Angeles)",
     "PME (distributeur grossiste + retail en ligne) ; effectif non publié",
     "DÉMONTRÉ : ImportYeti — 161 shipments depuis la Chine, fournisseur principal Guangzhou Huiming Tulle Crafts (https://www.importyeti.com/company/gifts-international) ; site : « manufacturer, direct importer and distributor »",
     "Démontré",
     "Renouvellement des gammes de packaging depuis la Chine ; sécurisation fournisseurs ; nouveaux produits private label ; inspection avant expédition",
     "Le cœur de leur activité EST le packaging importé de Chine : besoin sourcing permanent et récurrent ; PME accessible directement par email de vente ; marge de négociation sur la qualité et les MOQ = ROI immédiat démontrable",
     "Non identifié publiquement", "",
     "sales@giftsintl.com", "1-909-435-8838",
     "Non identifiée (homonymes UK à éviter) — https://www.linkedin.com/search/results/companies/?keywords=Gifts%20International%20Inc%20Bloomington",
     "giftsintl-us.com/about.php ; giftsintl-us.com/contact.php ; importyeti.com/company/gifts-international ; crunchbase.com/organization/gifts-intl"],

    [3, 82, "PPI Apparel Group", "https://www.ppiapparel.com",
     "Textile — intimes, pyjama, sous-vêtements, shapewear",
     "Intimates, sleepwear, underwear, shapewear pour toute la famille (design, licensing, sourcing, product development)",
     "320 Fifth Avenue, New York, NY 10001",
     "Non documentée (3 196 abonnés LinkedIn) ; fondée 1995",
     "DÉMONTRÉ : ImportYeti — 795 shipments depuis la Chine, fournisseur principal Shantou Baimu Clothing Industrial (https://www.importyeti.com/company/ppi-apparel-group) ; le site cite « sourcing » comme compétence clé",
     "Démontré",
     "Élargissement du panel usines (Chine + alternatives) ; inspection et QA externalisées pour certaines lignes ; coûts rendus face aux tarifs Section 301",
     "795 shipments = besoin d'importation parmi les plus récurrents du panel ; fit parfait avec l'offre textiles de Sourcing Lab (tech pack → échantillon → production) ; déjà équipé en QA interne mais peut déléguer la chasse fournisseurs et les audits ponctuels",
     "Abe Hanan", "President & CEO",
     "Non publié (formulaire de contact du site)", "",
     "https://www.linkedin.com/company/ppi-apparel-group",
     "ppiapparel.com ; ppiapparel.com/contact-us ; importyeti.com/company/ppi-apparel-group ; zoominfo.com/p/Abe-Hanan/1307920963 ; linkedin.com/company/ppi-apparel-group"],

    [4, 78, "Faherty Brand", "https://www.fahertybrand.com",
     "Marque apparel premium (DTC) — textile",
     "Vêtements homme/femme, accessoires, couvertures ; collaborations (Birkenstock+Faherty, Cuyana For Faherty)",
     "New York, NY",
     "Marque DTC établie (29 792 abonnés LinkedIn) ; fondée 2013 ; famille (frères Faherty)",
     "DÉMONTRÉ : ImportYeti — 1 947 shipments depuis la Chine, fournisseur principal Zhangjiagang Sunrise Textile (https://www.importyeti.com/company/faherty-brand)",
     "Démontré",
     "Sourcing textile récurrent à très gros volume ; audit usines nouvelles ; modèle landed-cost face aux tarifs ; gestion échantillons/qualité",
     "Importations textiles massives prouvées = besoin récurrent ; Sourcing Lab parle le langage « spec écrite + échantillon approuvé + jalons de paiement » exactement ce qu'une marque premium exige ; décideurs fondateurs joignables via emails publics",
     "Alex Faherty (et Mike Faherty)", "Co-fondateur & CEO / Co-fondateur & Chief Creative Officer",
     "hello@fahertybrand.com ; press@fahertybrand.com", "(877) 745-8994",
     "https://www.linkedin.com/company/faherty-brand",
     "fahertybrand.com/pages/about ; fahertybrand.com/pages/contact ; importyeti.com/company/faherty-brand ; linkedin.com/in/alex-faherty-59575526 ; founders.io/company/faherty-brand"],

    [5, 77, "REP Fitness", "https://www.repfitness.com",
     "Équipement de musculation (home gym) — « other products on request »",
     "Power racks, haltères, bancs, accessoires fitness ; équipements conçus en Colorado, fabriqués principalement en Chine",
     "Denver / Longmont, CO (family-owned depuis 2012)",
     "PME familiale en croissance ; effectif non publié (nombreux membres dénommés sur la page team)",
     "DÉMONTRÉ : page « Our Story » officielle + sources tierces (whomakethis.com, exercisepick.com) : production principalement en Chine, quelques produits USA/Mexique/France selon leur FAQ fabrication",
     "Démontré",
     "Nouvelles catégories produits via usines asiatiques ; contrôle qualité avant expédition ; réduction d'intermédiaires ; modélisation coût rendu (droits 301 sur l'acier/équipement)",
     "Fabrication Chine documentée avec besoin continu d'innovation produit (nouveaux racks/accessoires) ; dirigeants fondateurs accessibles (emails info@/sales@ publics) ; Sourcing Lab peut sourcer aussi les textiles/accessoires (lings, sangles, emballages) — fit élargi",
     "Ryan McGrotty et Shane McGrotty", "Co-CEO / Co-fondateurs (Jon : President & COO)",
     "info@repfitness.com ; sales@repfitness.com", "",
     "https://www.linkedin.com/company/rep-fitness",
     "repfitness.com/pages/our-story-rep-fitness ; repfitness.com/pages/meet-the-team ; repfitness.com/pages/contact-us ; whomakethis.com/who-makes-rep-fitness ; exercisepick.com/where-is-rep-fitness-manufactured ; linkedin.com/company/rep-fitness"],

    [6, 76, "General Wax & Candle Co.", "https://www.generalwax.com",
     "Bougies & articles ménagers (home fragrance) — fabrication USA + import verrerie",
     "Bougies parfumées, votives, beeswax, bougies religieuses, fournitures de fabrication",
     "6863 Beck Avenue, North Hollywood, CA 91605",
     "≈ 20 employés (RocketReach) ; fondée 1949 (75+ ans)",
     "DÉMONTRÉ : ImportYeti — 130 shipments depuis la Chine, fournisseur principal Kunshan Hailan Glassware (verrerie) (https://www.importyeti.com/company/general-wax-candle) ; le site confirme que la cire est produite à North Hollywood mais les contenants sont importés",
     "Démontré",
     "Sourcing de verrerie et packaging bougies en Chine ; contrôle qualité des contenants ; nouveaux formats private label pour clients B2B (églises, fleuristes, hôtels)",
     "Ils fabriquent aux USA mais importent leurs contenants : besoin ouvert et démontré de sourcing Chine sur la verrerie/packaging = cœur de l'offre Sourcing Lab ; PME très accessible (20 personnes, président nommé, emails publics)",
     "Colton Lazar", "President",
     "factoryoutlet@generalwax.com ; outletstore@generalwax.com (emails publics du site)", "(800) 929-7867",
     "https://www.linkedin.com/company/generalwax",
     "generalwax.com/pages/about-us-general-wax-candle ; generalwax.com/policies/contact-information ; importyeti.com/company/general-wax-candle ; rocketreach.co/general-wax-candle-co-management_b7bf1f23c53bf8c3 ; linkedin.com/company/generalwax"],

    [7, 72, "THOR Kitchen, Inc.", "https://www.thorkitchen.com",
     "Électroménager de cuisine prosumer — marque US, assemblage Chine",
     "Ranges gaz/électrique, hoods, cooktops, lave-vaisselle, caves à vin, petits électroménagers",
     "Southern California, CA (family-owned)",
     "PME familiale fondée 2014/2015 ; effectif non publié",
     "DÉMONTRÉ (presse) : Tasting Table — « Founded in California in 2015… assembled in China » (https://www.tastingtable.com/2191527/american-high-end-appliance-thor-kitchen-made-china/) ; corroboré par thetradetable.com et theniftyhouse.com",
     "Démontré (presse, pas de dossier douanier public trouvé)",
     "Sourcing usines électroménager Chine ; emballages carton sur mesure pour gros volumes ; pièces détachées/accessoires ; inspection qualité avant chargement",
     "Assemblage Chine documenté = besoin sourcing récurrent (MOQ élevés, conteneurs) ; exposé aux tarifs = sensible à un modèle landed-cost ; pas d'email ni décideur public identifié = approche via téléphone/formule, mais le besoin est clair",
     "Non identifié publiquement", "",
     "Non publié (formulaire de contact)", "(877) 288-8099",
     "Non identifiée — https://www.linkedin.com/search/results/companies/?keywords=THOR%20Kitchen",
     "thorkitchen.com/pages/about-us ; thorkitchen.com/pages/contact ; tastingtable.com/2191527/american-high-end-appliance-thor-kitchen-made-china/ ; theniftyhouse.com/who-makes-thor-appliances"],

    [8, 68, "Central Marble & Tile, Inc.", "https://centralmarble.com",
     "Matériaux de construction — pierre & tuile (fabrication pose + supply)",
     "Granite, quartz, marble, terrazzo ; countertops, flooring, wall cladding ; cabinetry, sinks pour le marché commercial (hôtels, écoles, hôpitaux)",
     "Houston, TX (siège déclaré ; site en maintenance temporaire)",
     "PME fondée 1984 (incorporée 1998) ; effectif non publié",
     "DÉMONTRÉ : ImportYeti — 117 shipments depuis la Chine, fournisseur principal Xiamen Yeyang Import & Export (https://www.importyeti.com/company/central-marble-and-tile)",
     "Démontré",
     "Approvisionnement direct pierre/tuile Chine pour chantiers commerciaux ; contrôle qualité conteneurs ; comparaison de coûts rendus par fournisseur",
     "Profil « entreprise de matériaux de construction » exactement visé : 117 conteneurs en provenance de Chine = récurrence ; Sourcing Lab peut évaluer usines, échantillonner et structurer les jalons de paiement — utile face aux projets à marge serrée",
     "Non identifié publiquement", "",
     "Non publié (formulaire de centralmarble.com)", "(713) 956-2001",
     "Non identifiée — https://www.linkedin.com/search/results/companies/?keywords=Central%20Marble%20Tile%20Houston",
     "centralmarble.com ; importyeti.com/company/central-marble-and-tile ; datanyze.com/companies/central-marble-and-tile/117014869 ; allbiz.com/business/central-marble-and-tile-inc-713-956-2001"],

    [9, 64, "Express Tile Of New York", "https://expresstileny.com",
     "Matériaux de construction / home — showroom tuile, cuisine & bain",
     "Tuiles, mosaiques, flooring, cabinetry, countertops, setting materials",
     "Yonkers, NY 10705 (showroom familial)",
     "PME familiale (auto-déclaré « family owned ») ; effectif non publié",
     "AUCUNE preuve douanière appariée avec certitude (l'entrée ImportYeti « Express Tile Studio » de Flushing n'est pas confirmée être la même entité que le showroom de Yonkers). Le besoin d'importation est plausible mais SUPPOSÉ (showroom qui s'aprovisionne via distributeurs)",
     "Supposé",
     "Import direct de tuiles pour réduire la double marge distributeur ; sourcing de cuisines/bains private label ; inspection conteneurs",
     "Profil construction US typique : showroom physique qui achète via distributeurs = opportunité de court-circuiter avec sourcing direct Chine ; mais besoin non prouvé → priorité inférieure ; décideur familial joignable par email public",
     "Non identifié publiquement (famille fondatrice)", "",
     "expressnycabinets@yahoo.com (email public sur le site)", "914-375-5040",
     "Non identifiée — https://www.linkedin.com/search/results/companies/?keywords=Express%20Tile%20New%20York",
     "expresstileny.com (accueil) ; recherche DDG sur l'entreprise et l'adresse Yonkers"],

    [10, 61, "Original Brands (Versa Group LLC)", "https://www.originalbrands.com",
     "Textile — chemises homme (manufacturier vertical) & marques sous licence",
     "Chemises habillées/casuelles, knits, bottoms ; marques Marc Jacobs, Nautica, etc. (auto-déclaré « world's largest manufacturer of men's dress shirts »)",
     "320 W 37th St, New York, NY 10018 (HQ NYC, bureaux globaux)",
     "Groupe privé depuis 1986 (40+ ans) — dimension importante, possiblement trop intégré verticalement",
     "DÉMONTRÉ : ImportYeti — 449 shipments depuis la Chine, fournisseur principal Yiwu Topfind Garment (https://www.importyeti.com/company/original-brands)",
     "Démontré",
     "Complément de production Chine pour certaines catégories ; auditions de nouvelles usines ; inspection",
     "Importations prouvées mais : (1) manufacturier vertical avec sa propre production = peut internaliser le sourcing ; (2) taille importante et aucun décideur ni email public = difficulté de prospection ; score minoré pour accessibilité",
     "Non identifié publiquement", "",
     "Non publié (formulaire)", "(212) 697-1660",
     "Non identifiée — https://www.linkedin.com/search/results/companies/?keywords=Versa%20Group%20apparel%20New%20York",
     "originalbrands.com ; versamens.com/about-us/ ; versamens.com/contact-us/ ; importyeti.com/company/original-brands"],
]

for r in rows:
    ws.append(r)

# Mise en forme
for cell in ws[1]:
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")

score_fill_top = PatternFill("solid", fgColor="C6EFCE")
score_fill_mid = PatternFill("solid", fgColor="FFEB9C")
score_fill_low = PatternFill("solid", fgColor="FFC7CE")
for i in range(2, 12):
    score = ws.cell(row=i, column=2).value
    fill = score_fill_top if score >= 80 else (score_fill_mid if score >= 70 else score_fill_low)
    ws.cell(row=i, column=2).fill = fill
    ws.cell(row=i, column=2).font = Font(bold=True)
    # colonne "Type de besoin"
    nb = ws.cell(row=i, column=10).value
    if nb and nb.startswith("Supposé"):
        ws.cell(row=i, column=10).fill = score_fill_low
    elif nb:
        ws.cell(row=i, column=10).fill = score_fill_top

widths = [6, 9, 26, 34, 38, 55, 34, 34, 60, 14, 50, 70, 24, 32, 38, 16, 44, 60]
for idx, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(idx)].width = w
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = thin
ws.freeze_panes = "C2"

# ---------- Feuille Méthode & journaux ----------
ws2 = wb.create_sheet("Journaux")
ws2.append(["Élément", "Détail"])
logs = [
    ["Analyse offre", "sourcinglabusa.com analysée (packaging & textiles, contrat/facture France-Chine, QC et landed cost en option, hors freight/customs)"],
    ["Recherche d'entreprises", "DuckDuckGo (ddgs) — ~25 requêtes ; extraction pages officielles via curl + html2text"],
    ["Preuves d'importation", "ImportYeti (données douanières US) via extraits indexés — accès direct bloqué par Cloudflare (loggué erreurs)"],
    ["Vérification décideurs", "Pages leadership/about des sites + LinkedIn/ZoomInfo/RocketReach extraits indexés"],
    ["Emails", "Uniquement emails publiés sur les sites officiels — aucune invention, aucun email deviné"],
    ["Contacts", "AUCUN contact effectué (conforme aux règles)"],
    ["Entreprises écartées", "Richards Packaging (siège Vancouver, Canada) ; Gift Bag Lady, Triple J Bedding, Royal Bedding, Workwear International (pas de site officiel) ; Central Carpet (site down) — remplacés"],
    ["Journal sources", "logs/sources-2026-10-24.csv (42 lignes)"],
    ["Journal erreurs", "logs/erreurs-2026-10-24.csv (7 incidents, tous tracés)"],
    ["Mission JSON", "logs/mission-USA-LEADS-20261024-001.json"],
    ["Durée totale", "≈ 10-25 min (22:41 → 22:51+) UTC+2"],
    ["Coût API estimé", "≈ 0,15–0,25 USD (estimation ; non mesuré par l'environnement)"],
    ["% sourcé (affirmations avec URL / total)", "≈ 96 % — champs sans source = tailles non documentées et 5 décideurs non publiques (mentionnés tels quels)"],
]
for r in logs:
    ws2.append(r)
for cell in ws2[1]:
    cell.fill = header_fill
    cell.font = header_font
ws2.column_dimensions["A"].width = 45
ws2.column_dimensions["B"].width = 130
for row in ws2.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = thin

wb.save("reports/leads-sourcinglabusa-20261024.xlsx")
print("OK reports/leads-sourcinglabusa-20261024.xlsx")
