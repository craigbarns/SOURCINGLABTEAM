---
name: us-lead-scoring-v2
description: "Nouveau scoring pour prospects USA /100 avec 5 composantes - adequation, besoin, probabilite de sous-traitance, accessibilite, potentiel. Separe faits, hypotheses, inconnues."
---

# US Lead Scoring v2

Score avancé pour identifier les prospects ayant une **probabilité élevée de payer** une prestation de sourcing international.

## Composantes du score /100

### 1. Adéquation à nos services — 25 pts
**Faits concrets** : l’entreprise correspond-elle à notre marché cible ?

| Points | Critère                                    |
|--------|--------------------------------------------|
| 5      | PME ou entreprise de taille intermédiaire (50–500 employés, chiffre d'affaires < 200 M$) |
| 5      | Marque de produits physiques, distributeur, grossiste, packaging, textile, quincaillerie, produits ménagers |
| 5      | Développe / lance / fait évoluer des gammes (preuve : communiqué, blog, annonce produit) |
| 5      | Besoin de sourcing multi‑produits ou multi‑origines (Chine, Asie, Europe) |
| 5      | Produit « made in » extérieur aux USA ou capacité de production externalisée |

### 2. Indices concrets de besoin — 25 pts
**Preuves documentées** de besoins d’importation, de fabrication ou de développement.

| Points | Indice                                     | Prouvé par |
|---|---|
| 5      | Données douanières récentes (< 24 mois) avec volume significatif (≥ 10 shipments / an) | Panjiva, ImportYeti, Zepol, Descartes |
| 5      | Publications presse / blog mentionnant des projets de sourcing, de lancement produit, de diversification fournisseurs | Site officiel, communiqués, articles |
| 5      | Page carrière mentionnant des postes Achats, Sourcing, Supply Chain | Site carrière, LinkedIn entreprise |
| 5      | Présence dans des salons internationaux sourcing (Canton Fair, ASD, Pack Expo) comme visiteur ou exposant | Programme salon, billet blog, photo |
| 5      | Demande de devis (RFQ) publiée sur plateforme B2B (Thomasnet, Alibaba, Global Sources) | Capture d’écran, lien |

### 3. Probabilité de sous‑traiter le sourcing — 20 pts
**Hypothèses fondées** sur la structure interne et les signaux.

| Points | Signal                                    | Justification |
|---|---|---|
| 5      | Pas d’équipe sourcing dédiée mentionnée (pas de « Director of Sourcing », « VP Global Procurement » nommé) | Site « Our team », LinkedIn |
| 5      | Taille modérée : trop petit pour avoir un département sourcing à plein temps, mais assez grand pour importer régulièrement | Effectif 50–300, CA < 100 M$ |
| 5      | Projets ponctuels ou saisonniers (ex. collection Noël, lancement ligne) nécessitant une mise en œuvre rapide | Communiqué, historique produits |
| 5      | Concurrents connus pour utiliser des agents de sourcing (benchmark sectoriel) | Étude de cas, témoignage indirect |

### 4. Accessibilité du décideur — 15 pts
**Contacts publics** et facilité d’accès.

| Points | Contact disponible                          |
|---|---|
| 5      | Email professionnel public (sales@, info@, contact@) répondant < 24h en test |
| 5      | Décideur identifié publiquement (CEO, Owner, Head of Purchasing) avec profil LinkedIn ouvert ou mention dans presse |
| 5      | Numéro de téléphone direct (hors standard) ou formulaire contact rapide |

### 5. Potentiel commercial — 15 pts
**Volume et récurrence** estimés.

| Points | Estimation                                  |
|---|---|
| 5      | Besoin récurrent (importations mensuelles/trimestrielles) vs. opération unique |
| 5      | Budget sourcing estimé > 50 k$/an (d’après volumes douaniers, prix produit, marge sectorielle) |
| 5      | Possibilité de vente additionnelle (contrôle qualité, logistique, landed cost) |

## Pénalités (retrait de points)

- **-20** : Grand groupe avec sourcing intégré (équipe > 10 personnes, « Global Sourcing Director »)
- **-15** : Réseau international d’usines déjà établi (filiales production en Asie)
- **-10** : Contacts uniquement destinés au service client (pas d’accès aux achats)
- **-10** : Importations historiques sans signe d’activité récente (> 3 ans)
- **-5**  : Absence totale d’opportunité commerciale identifiable

## Méthode de recherche

### Phase 1 – Identification large
- Recherche DuckDuckGo / Google ciblée : `"importer of" "USA" "textile" "private label"`, `"distributor" "home goods" "sourcing"`, `"manufacturer" "custom packaging" "USA"`.
- Sources : Thomasnet, Manta, Bloomberg, LinkedIn, Crunchbase, ImportYeti (si accès).
- **Ne pas collecter plus de 30 prospects bruts**.

### Phase 2 – Vérification approfondie
Pour chaque prospect :
1. **Site officiel** : extraire produits, mentions « global sourcing », « supply chain », « manufacturing partners », pages carrière.
2. **Données douanières** : via ImportYeti (si disponible) noter les **dates** des shipments, volumes, pays d’origine.
3. **Presse / blog** : rechercher sur site et Google `site:nomdusite.com sourcing` ou `site:nomdusite.com factory`.
4. **LinkedIn entreprise** : vérifier taille, postes clés, activité des employés.
5. **Salons** : rechercher `"nom entreprise" "exhibitor" "trade show"`.

### Phase 3 – Qualification v2
Remplir pour chaque prospect :

**FICHE PROSPECT v2**
```
Entreprise :
Site officiel :
Produits (max 3 lignes) :
Problème que nous pourrions résoudre (concret) :
Preuves documentées (URLs + extraits) :
Décideur approprié (nom, titre) :
Contact professionnel vérifié (email, téléphone) :
Angle d’approche personnalisé (1 phrase) :

SCORE DÉTAILLÉ :
- Adéquation /25 : [score] – [justification]
- Indices besoin /25 : [score] – [preuves]
- Probabilité sous‑traitance /20 : [score] – [hypothèse]
- Accessibilité /15 : [score] – [contacts]
- Potentiel commercial /15 : [score] – [estimation]
- Pénalités : [liste]
- TOTAL /100 : [score]
```

### Phase 4 – Audit
- Faire auditer les 20 fiches par **supplier‑auditor** (vérification des sources, cohérence des scores, séparation faits/hypothèses).
- Corriger les anomalies signalées (1 itération max).

### Phase 5 – Export Excel
Fichier `us‑leads‑v2‑YYYY‑MM‑DD.xlsx` avec feuilles :
- `Synthèse` : top 5, moyennes scores, recommandations.
- `Prospects` : 20 lignes avec toutes les colonnes de la fiche.
- `Scores` : détail des 5 composantes par prospect.
- `Sources` : URLs utilisées, dates d’extraction.
- `Journaux` : étapes, temps, coût estimé.

## Règles strictes

1. **Ne jamais inventer** de prospect, de contact, de donnée douanière.
2. **Séparer clairement** dans la justification :
   - **Faits** : extrait de source datée avec URL.
   - **Hypothèses** : déduction logique à partir des faits.
   - **Inconnues** : éléments non trouvés (ex. « Pas de données douanières récentes »).
3. **Vérifier les dates** : si données douanières > 3 ans, ne pas les considérer comme preuve de besoin actuel.
4. **Ne pas assimiler importation à intention d’achat** : une entreprise qui importe peut avoir un sourcing internalisé ; chercher les signes de fragilité (turnover fournisseurs, recherche de nouveaux partenaires).
5. **Pas de score élevé sans justification** : chaque point doit être argumenté.
6. **Ne pas contacter** les prospects pendant la recherche.

## Métriques de qualité

- **Taux de sourcing** : % de champs avec URL de preuve (objectif > 90 %).
- **Actualité des données** : % de données douanières < 2 ans (si disponibles).
- **Séparation claire** : chaque fiche doit contenir les sections « Faits », « Hypothèses », « Inconnues ».
- **Audit réussi** : supplier‑auditor valide ≥ 95 % des sources.

---

**Usage** : cette skill remplace l’ancien scoring US pour les missions de prospection ultérieures. L’agent `us‑lead‑hunter` doit être mis à jour pour utiliser cette grille.