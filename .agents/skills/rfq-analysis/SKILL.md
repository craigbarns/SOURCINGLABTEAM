---
name: rfq-analysis
description: Procédure d'analyse de cotations fournisseurs - extraction PDF/Excel, comparaison prix/MOQ/Incoterms, marges, tableaux comparatifs
---

# RFQ Analysis Skill — Analyse de cotations SOURCING LAB AI

## Quand utiliser
À chaque réception de devis fournisseurs (PDF, Excel, email) pour produire un comparatif exploitable.

## Procédure en 6 étapes

### 1. Collecte & extraction
- Place tous devis dans `data/rfq/` (nommage : `RFQ-2026-10-24-Fournisseur-Produit.pdf`)
- Extraction :
  ```bash
  # PDF natif
  python3 -c "import pdfplumber; ..."
  # ou CLI
  pdftotext -layout RFQ.pdf -
  # Excel
  python3 -c "import openpyxl; wb=openpyxl.load_workbook('rfq.xlsx'); ..."
  ```
- Si scan illisible → `Lecture impossible - OCR requis`
- Output : `rfq-extracted-YYYY-MM-DD.json` avec pour chaque devis :
  ```json
  { "fournisseur": "...", "ref": "10L Bucket", "qty": 1000, "prix_unit": 1.2, "devise": "USD", "moq": 1000, "incoterm": "FOB", "port": "Qingdao", "delai": "25 days", "validite": "30 days" }
  ```

### 2. Normalisation
- Convertis tous prix en **même devise** (EUR par défaut) au taux BCE jour J
  - Source : `https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/`
  - Note : `Taux EUR/USD 1.08 BCE 2026-10-24`
- Aligne Incoterms : EXW → ajoute fret intérieur usine→port (estimation si besoin)
- Détecte frais cachés : moule, cliché IML, échantillon, packaging

### 3. Calcul coûts complets
```
Coût rendu HT = FOB + Fret maritime + Assurance (0.3%) + Droits douane (TARIC) + TVA (récupérable) + Fret intérieur
```
- Fret estimé si non fourni : fourchette 40HQ Cina→Le Havre (source Freightos)
- Droit douane : HS Code 3923.90.00 → taux TARIC UE (à vérifier le jour J)
- Note systématique : `Estimation - à confirmer transitaire` vs `Chiffré devis`

### 4. Analyse MOQ & paliers
- Tableau MOQ par réf/variante
- Calcule stock initial = Σ(MOQ par réf)
- Signale incohérence : "MOQ 10L=500 vs 16L=3000 même moule → à clarifier"

### 5. Comparatif & scoring
Critères pondérés :
- Prix rendu 40% | MOQ 20% | Délai 15% | Qualité perçue (certifs + audit) 15% | Paiement 10%
Tableau :
```
| Fournisseur | Prix EXW | Prix FOB | Prix CIF | Coût rendu | Écart | MOQ | Délai | Score /100 |
```

### 6. Livraison
- `comparatif-rfq-YYYY-MM-DD.xlsx` (synthèse + détail par fournisseur + graph écart)
- `comparatif-rfq-YYYY-MM-DD.csv` (séparateur `;`)
- `analyse-rfq-YYYY-MM-DD.md` (top 3 + négo + risques)

## Règles d'or
- **NE JAMAIS inventer** : manquant = `Non communiqué - à demander`
- Estimation = toujours marquée `Estimation` + source + fourchette
- Devise + date taux citées
- Contradiction devis = `Incohérence - clarification requise`
- Confidentialité : ne partage pas un devis avec un autre fournisseur

## Template message clarification fournisseur
```
Bonjour [Fournisseur],
Merci pour votre offre du [date] réf [ref].
Pour finaliser, merci de préciser :
- MOQ exact pour 10L et 16L IML
- Prix FOB Qingdao (ou CIF Le Havre) détaillé
- Délai production + validité offre
- Certificat FDA/EU à jour
```
