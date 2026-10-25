---
name: sourcing-research-procedures
description: Procédures réutilisables de recherche, vérification et comparaison sourcing - templates requêtes, checklists, exports
---

# Sourcing Research Procedures — SOURCING LAB AI

Trois procédures standardisées et réutilisables pour tout sourcing.

---

## Procédure 1 — RECHERCHE (SEARCH)

### Objectif
Passer de 0 à 30 candidats sourcés en 20 minutes.

### Template requêtes multilingues
Génère systématiquement ces 10 requêtes (adapte au produit) :

```
1. "product name" manufacturer factory food grade material capacity
2. "product name" factory China/Mexico/Turkey ISO certified supplier
3. site:made-in-china.com "product name" factory audited
4. site:alibaba.com "product name" manufacturer gold supplier
5. 产品中文名 厂家 生产厂家 工厂  (ex: 塑料桶 厂家)
6. "product name" Hersteller Fabrik Deutschland/EU
7. "product name" fabricant usine France/EU
8. HS Code + country importer (ex: HS 392390 plastic bucket importer USA)
9. "product name" OEM ODM private label factory
10. "product name" wholesale distributor USA/EU
```

### Checklist exécution
- [ ] Lancer `uvx ddgs text -q "requête" -m 10` pour chaque requête → 100 URLs brutes
- [ ] Dédupliquer URLs (même domaine + même raison sociale = 1)
- [ ] Pour chaque candidat potentiel, extraire via :
  ```bash
  curl -sL -A "Mozilla/5.0" "https://candidate.com" | uvx html2text --ignore-links > /tmp/candidate-XXX.txt
  wc -c /tmp/candidate-XXX.txt && head -c 8000 /tmp/candidate-XXX.txt
  ```
- [ ] Remplir fiche collecte brute :
  ```
  | Candidat | URL source | Raison sociale trouvée | Adresse | Produit 8-16L ? | Usine ? | À retenir ? |
  ```
- [ ] Filtrer : garder uniquement usines candidates (≥2 preuves usine), éliminer traders purs
- [ ] Trier par pertinence (produit exact + export + certifs)

### Output
`recherche-brute-YYYY-MM-DD.md` + liste 10-15 candidats à approfondir.

---

## Procédure 2 — VÉRIFICATION (VERIFY)

### Objectif
Passer de 15 candidats à 10 fabricants vérifiés avec preuves.

### Checklist vérification (Vérifié / Déclaré / Non vérifié / Contradictoire)

#### A. Identité & usine
- [ ] Raison sociale légale = footer site + fiche MIC/Alibaba + page About cohérents ?
- [ ] Adresse usine physique : rue + zone industrielle → test Maps
- [ ] Photos usine : ≥3 photos machines/lignes (pas stock images) ?
- [ ] Surface + effectif chiffrés ?
- [ ] Vérifier WHOIS domaine vs année création déclarée
- [ ] Statut : `Vérifié` si 3/5 ok avec URLs / `Déclaré` si 1-2 / `Non vérifié` si 0

#### B. Produit conforme
- [ ] Fiche produit officielle avec capacité exacte (ex: 10L, 16L) ?
- [ ] URL fiche produit capturée + extraction datée ?
- [ ] Si non trouvé sur site officiel mais présent MIC → `Déclaré` + note `À confirmer`
- [ ] Hors spec → exclure ou marquer `Hors spec - conservé pour info`

#### C. Certifications
- [ ] FDA / EU / ISO mentionnés où ? (site officiel page Certificates ? fiche MIC ?)
- [ ] Document PDF/image trouvé ? → `Vérifié` (noter n°, organisme, validité)
- [ ] Sinon → `Déclaré`
- [ ] Expiré / adresse différente → `Contradictoire` + alerte

#### D. Doublon / Société liée
- [ ] Comparer : raison sociale normalisée, adresse, tel, email, dirigeant, domaine
- [ ] Détection automatique via `rg` :
  ```bash
  rg -i "same phone|same address|M. Fan|cnbucket" /tmp/*.txt
  ```
- [ ] Si doublon → fusionner, noter `Doublon de #X`
- [ ] Si groupe (ex: Zibo Yundu → Foshan Chengpin) → `Unique - groupe lié à #Y`

### Output
CSV vérifié avec colonnes Statut vérification + Note doublon + Liens sources vérifiés (≥2 par ligne).

---

## Procédure 3 — COMPARAISON (COMPARE)

### Objectif
Produire tableau décisionnel clair pour le Manager / client.

### Template tableau comparatif (ex: seaux PP 8-16L)

| Critère | Poids | Source |
|---------|-------|--------|
| Identification juridique | 15% | Pilier 1 qualification |
| Preuve industrielle | 20% | Pilier 2 |
| Conformité produit | 15% | Pilier 3 |
| Capacités fabrication | 15% | Pilier 4 |
| Certifications | 15% | Pilier 5 |
| Conditions commerciales | 10% | Pilier 6 |
| Qualité sources | 10% | Pilier 7 |

### Étapes
1. **Scorer** chaque fournisseur via skill `supplier-qualification` → score /100
2. **Classer** : 90-100 / 70-89 / 40-69 / 0-39
3. **Comparer** capacités côte à côte :
   ```
   | Fournisseur | Surface | Lignes | MOQ | Certifs Vérifiés | Score | Recommandation |
   ```
4. **Identifier** :
   - Doublons : même adresse/tel
   - Sociétés liées : même groupe
   - Infos non prouvées : colonne `Déclaré` sans doc
   - Hors spec : pas dans 8-16L
   - Données manquantes : MOQ, prix, certif
5. **Recommander** : Top 3 Go / 2 À compléter / Reste No-Go + justification

### Exports standardisés

#### CSV corrigé
```csv
"ID";"Nom";"Site";"Gamme 8-16L";"Score /100";"Niveau";"Statut Vérification";"Certifs";"Sources";"Recommandation"
```

#### XLSX (python openpyxl)
```python
import openpyxl
from openpyxl.styles import PatternFill
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Fournisseurs Qualifiés"
# Header gelé, filtres, couleurs conditionnelles
# Rouge #FF6B6B (0-39), Orange #FFD93D (40-69), Vert clair #6BCB77 (70-89), Vert foncé #2D6A4F (90-100)
```

#### Rapport markdown
```
# Rapport Comparatif - [Produit] - [Date]
## Résumé exécutif (tableau scores + Go/No-Go)
## Méthodologie
## Détail par fournisseur (7 piliers + URLs)
## Doublons & sociétés liées
## Données manquantes & actions
## Recommandations
```

### Checklist livraison
- [ ] CSV corrigé + XLSX avec couleurs
- [ ] Rapport markdown avec URLs cliquables
- [ ] Grille qualification détaillée (7 piliers)
- [ ] Registre incohérences
- [ ] Recommandation Go/No-Go justifiée

---

## Règles communes aux 3 procédures
- **Traçabilité** : chaque donnée = URL source + date extraction
- **Aucune invention** : manquant = `Non communiqué`
- **Multilingue** : requêtes EN/ZH/FR minimum
- **Anti-doublon** : vérification systématique avant ajout
- **Livrables nommés** : `YYYY-MM-DD` dans nom fichier

Utilise ces procédures comme checklists. Coche chaque case et livre les outputs nommés.
