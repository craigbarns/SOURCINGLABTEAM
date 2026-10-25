---
name: supplier-qualification
description: Qualification de fournisseurs sur 7 piliers avec score /100 explicite et reproductible - statuts Vérifié/Déclaré/Non vérifié/Contradictoire
---

# Supplier Qualification Skill — Méthode SOURCING LAB AI

Utilise cette skill chaque fois que tu dois qualifier un fournisseur industriel, attribuer un score /100 et justifier chaque point.

## Objectif
Fournir une **méthode explicite, reproductible et auditable** pour scorer tout fournisseur sur 7 piliers. Deux auditeurs appliquant la méthode doivent arriver au même score ±5 points.

## Les 7 piliers (total 100 points)

### Pilier 1 — Identification juridique (15 pts)
| Critère | Vérifié (15) | Déclaré (8) | Non vérifié (0) | Contradictoire (0) |
|---------|--------------|-------------|-----------------|---------------------|
| Raison sociale légale exacte | Nom complet + forme juridique (Co., Ltd.) sourcé sur site officiel + fiche MIC/Alibaba avec URL | Mention partielle sans preuve | Absent | Deux noms incompatibles |
| Adresse usine physique | Adresse rue + zone industrielle + ville + province vérifiable sur Maps | Adresse générique "Qingdao, China" | Aucune adresse | Adresse bureau ≠ usine affichée comme usine |
| Année création & capital | Année + capital-investissement cités avec source (MIC, qcc.com, site About) | Année seule sans source | Non communiqué | MIC dit 2017, site dit 2008 (cas Hivic) |

**Règle** : Si adresse usine = `Non communiqué` → max 5/15 même si raison sociale ok.

### Pilier 2 — Preuve d'activité industrielle (20 pts)
| Sous-critère | Points |
|--------------|--------|
| Photos usine / atelier / machines (≥3 photos distinctes sourcées) | 6 |
| Vidéo usine / visite virtuelle | +3 bonus (plafond 20) |
| Surface usine m² chiffrée + nb lignes + tonnage presse | 6 |
| Effectif production / QA | 4 |
| Certificat usine BV / SGS / Audited Supplier avec adresse usine | 4 |

**Statut par preuve** : `Vérifié` = photo/vidéo sur site officiel ou audit BV ; `Déclaré` = chiffre sans photo ; `Non vérifié` = rien ; `Contradictoire` = photos stock Shutterstock ou autre usine

### Pilier 3 — Conformité produit demandé (15 pts)
| Cas | Score |
|-----|-------|
| Gamme 8-16L prouvée sur **site officiel** (fiche produit avec litres) | 15 Vérifié |
| Gamme prouvée uniquement sur marketplace (MIC/Alibaba) | 10 Déclaré |
| Gamme partielle (ex: que 5L, pas 10-16L) | 5 Non vérifié |
| Hors spec (pas de seaux alimentaires PP, que bassines) | 0 Hors spec |
| Contradiction (site dit PP food-grade, fiche MIC dit PE non-food) | 0 Contradictoire |

**Obligation** : Citer URL fiche produit exacte. Pas d'extrapolation "fait aussi 10L car fait 20L".

### Pilier 4 — Capacités de fabrication (15 pts)
| Sous-critère | Points |
|--------------|--------|
| Procédés maîtrisés (injection, soufflage, IML, fluorination...) sourcés | 5 |
| Capacité volume (pcs/jour, tonnes/an) chiffrée | 4 |
| OEM/ODM + personnalisation (couleur, IML, logo, poignée) prouvés | 3 |
| Export avéré (≥10 pays ou volume Panjiva shipments) | 3 |

`Vérifié` = page Capabilities / Factory Tour ; `Déclaré` = phrase marketing "we can produce"

### Pilier 5 — Certifications documentées (15 pts)
Grille par certif (FDA, EU 10/2011, ISO 9001, HACCP, BSCI, UN, SGS) :
- **Vérifié** = document PDF/image avec numéro + organisme émetteur + adresse usine + date validité + URL source → 3 pts par certif (max 15)
- **Déclaré** = mention texte "FDA approved" sans document → 1 pt par certif
- **Non vérifié** = non mentionné → 0 pt
- **Contradictoire** = certificat expiré / adresse autre société / photoshop détecté → 0 pt + note `Contradictoire`

**Exigence** : Pour ISO 9001, vérifier organisme accrédité (ex: TÜV, SGS, BV). Pour FDA, exiger 21 CFR 177.1520 explicitement.

### Pilier 6 — Conditions commerciales (10 pts)
| Sous-critère | Vérifié | Déclaré | Non vérifié |
|--------------|---------|---------|-------------|
| MOQ chiffré par ref | 3 pts (avec source devis/catalogue) | 1 pt (mention vague) | 0 |
| Incoterms (FOB, CIF...) + port | 2 pts | 1 pt | 0 |
| Délai production + validité prix | 3 pts | 1 pt | 0 |
| Paiement (T/T 30/70, L/C) | 2 pts | 1 pt | 0 |

### Pilier 7 — Qualité des sources (10 pts)
| Niveau | Points | Critère |
|--------|--------|---------|
| Excellent | 10 | ≥3 URLs distinctes dont site officiel + fiche audit BV + fiche produit |
| Bon | 7 | 2 URLs dont site officiel |
| Moyen | 4 | 2 URLs marketplace seules (MIC + Alibaba) |
| Faible | 0 | 1 URL ou source non sourcée |
| Contradictoire | 0 | Sources se contredisent |

**Bonus/Malus** : Extraction datée `Vérifié YYYY-MM-DD via html2text` = +1

## Calcul du score
```
Score = P1 + P2 + P3 + P4 + P5 + P6 + P7  (max 100)
```
Arrondi à l'entier. Pas de demi-point.

## Niveaux de qualification
| Score | Niveau | Couleur | Action |
|-------|--------|---------|--------|
| 90-100 | Hautement qualifié | 🟢 Vert foncé | Go direct RFQ + échantillon |
| 70-89 | Qualifié | 🟢 Vert clair | Go RFQ |
| 40-69 | À compléter | 🟠 Orange | Demander docs manquants, puis re-scorer |
| 0-39 | Non qualifié | 🔴 Rouge | No-Go, remplacer |

## Application pratique

### Étape 1 — Collecte
Pour chaque fournisseur, ouvre 3 URLs minimum :
1. Site officiel page About + Contact
2. Fiche Made-in-China `company-*.html` ou Alibaba `company_profile.html`
3. Fiche produit phare (ex: 10L bucket)

Extrais via `curl + html2text`, sauvegarde dans `/tmp/`.

### Étape 2 — Remplis la grille
Crée tableau :
```
| Pilier | Score | Statut | Justification | URL |
```
Exemple pour Rulyda :
```
| P1 Identification | 11/15 | Déclaré | Adresse Huangdao sourcée mais année non citée | https://rulydaplastic.en.made-in-china.com/... |
```

### Étape 3 — Attribue statut global par fournisseur
Pour chaque pilier, note : `Vérifié` / `Déclaré` / `Non vérifié` / `Contradictoire`
Statut global = le plus fréquent ; en cas d'égalité, le plus sévère l'emporte.

### Étape 4 — Livraison
Produis :
- `scores-YYYY-MM-DD.csv` : `ID;Fournisseur;Score;P1;P2;P3;P4;P5;P6;P7;Niveau;Commentaire`
- `grille-qualification-YYYY-MM-DD.md` : détail 7 piliers par fournisseur + URLs
- Mise en forme XLSX : règle conditionnelle rouge/orange/vert + filtre

## Exemple noté (cas réel Mission Seaux PP)
**Enlightening Plast (Qingdao)**
- P1 13/15 Vérifié (3 adresses usine + année 2005 via site, léger doute Shanghai vs Qingdao → -2)
- P2 18/20 Vérifié (2 usines 20000m² + 85 machines + photos + BV Audit)
- P3 15/15 Vérifié (10L,12L,16L fiches officielles cnbucket.com/plastic-bucket-supplier)
- P4 12/15 Vérifié (1-30L + OEM + export 80 pays → manque tonnage chiffré)
- P5 9/15 Déclaré (FDA 177.1520 + EU 10/2011 + ISO 9001 cités mais pas de PDF certif complet → 3×1 + 3 bonus UN)
- P6 6/10 Déclaré (MOQ non chiffré publiquement, FOB Qingdao implicite)
- P7 10/10 Vérifié (3 sites + extraction datée)
- **Total 83/100 → Qualifié 🟢**

## Règles d'or
- **Reproductibilité** : un autre auditeur avec mêmes URLs doit retrouver ton score
- **Pas d'invention** : si MOQ non publié → 0 sur ce sous-critère, pas estimation
- **Traçabilité** : chaque point s'appuie sur URL exacte, pas "site officiel"
- **Contradictoire prime** : une info contradictoire annule le pilier (0) même si autres ok

Charge cette skill systématiquement quand tu scores un fournisseur.
