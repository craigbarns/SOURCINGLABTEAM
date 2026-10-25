# 🔍 Fiche audit lead — SKIMS
**Mission** : LEAD-AUDIT-20261025-SKIMS | **Agent** : lead-auditor | **Demande** : "contacter Skims pour présenter Sourcing Lab"
**Date d'audit** : 2026-10-25 ~10:45 CET

| Prospect | Décision | Motif | Score v2 ajusté | Preuves (URL + date) | Contact vérifié | Prochaine action |
|---|---|---|---|---|---|---|
| SKIMS (marque, Kim Kardashian, skims.com) | **RETENU** — avec réserves explicites (voir §Réserves) | Adéquation réelle (textile/womenswear + lancement Skims Alpine oct. 2026 = angle TA1 de la mission trends), mais entreprise **très grande avec supply chain dédiée** → score réduit selon la grille | **52/100 — Tier Cold-Warm** | Voir §Preuves | ⚠️ Génériques uniquement : help@skims.com (site officiel), hello@skims.com (source secondaire) | Brouillons outreach-writer → validation humaine → envoi via send_emails.py |

## 1. Correspondance offre ↔ besoin (bloquant) — ✅ Passé
- SKIMS = marque de shapewear/loungewear/underwear en forte croissance → achète du textile (knits, fleece, sherpa, cos, lycra...) en gros volumes. Adéquation réelle avec l'offre sourcing textile.
- Preuve : catalogue officiel https://skims.com (consulté 2026-10-25, HTTP 200, 1,3 Mo).

## 2. Besoin commercial documenté — ✅ Partiellement
- **Documenté** : fabrication offshore avérée — principalement **Chine, Turquie, Thaïlande** (whomakethis.com mai 2026 ; thygesenapparel.com sept. 2026 ; articles avril 2025). Un sourcing multi-origines actif est un fait, pas une supposition.
- **Déclaré** : lancement **Skims Alpine** (collection cosy premium : cashmere, cotton fleece, sherpa) — rapporté par thezoereport.com le jour de la mission trends (2026-10-25) → signe d'expansion de gammes hiver.
- **Non prouvé** : qu'un besoin d'aide sourcing externe existe. Une société de cette taille a presque certainement une équipe supply chain interne → le besoin reste **supposé**.

## 3. Solvabilité et taille — ⚠️ Réducteur de score
- Marque de notoriété mondiale (cofondatrice Kim Kardashian), effectif et CA élevés, équipe sourcing dédiée quasi certaine → selon la grille lead-auditor : **score réduit** (trop grand).
- Aucun signal négatif détecté (litiges/faillite) dans les sources consultées — recherche non exhaustive.

## 4. Contact vérifiable — ⚠️ Générique uniquement
| Canal | Valeur | Statut |
|---|---|---|
| Email support | help@skims.com | **Vérifié sur le site officiel** (2026-10-25) — canal client, pas B2B |
| Email générique | hello@skims.com | Source secondaire (complaintsboard.com) — non confirmé sur skims.com |
| Wholesale / Partnerships | /pages/wholesale et /pages/partnerships → **HTTP 404** | Page B2B absente du site |
| Décideur nommé | Non identifié publiquement dans les sources consultées | — |

## ⚠️ Réserves de l'auditeur (à lire avant envoi)
1. **Probabilité de réponse faible** : le seul email public est un canal support client. Une approche B2B via help@ risque d'être ignorée ou redirigée. Alternative : LinkedIn (entreprise SKIMS, postes supply chain) ou formulaire officiel.
2. **Ne jamais** démarcher via les canaux presse (Cision) — réservés médias.
3. **Confusion évitée** : skimsglobal.com ("Skims Global FZCO", skimspharmaceuticals.com) est une **autre entreprise pharmaceutique** sans lien avec la marque SKIMS. Ne pas confondre les domaines.
4. La fiche ne garantit aucun besoin : nous vendons une capacité, pas un produit qu'ils cherchent.

## Tableau de couverture
| Établi | Partiel | Inconnu |
|---|---|---|
| Site officiel + help@skims.com vérifiés ; fabrication Chine/Turquie/Thaïlande documentée ; lancement Skims Alpine rapporté | hello@skims.com (source secondaire) ; structure de l'équipe supply chain | Contacts sourcing/procurement nominatifs ; volumes d'achat ; ouverture à un prestataire externe |

## Prochaine action
Brouillons outreach (1 email + 2 relances) → **validation humaine** → envoi via `send_emails.py --send` (canal : help@skims.com).

## Journal des sources
| # | Source | URL | Type | Date | Note |
|---|---|---|---|---|---|
| 1 | skims.com | https://skims.com | Site officiel | 2026-10-25 | HTTP 200, 1 295 652 o ; help@skims.com extrait du HTML |
| 2 | skims.com contact | https://skims.com/pages/contact-us | Site officiel | 2026-10-25 | Page contact = support client uniquement |
| 3 | skims.com wholesale | https://skims.com/pages/wholesale | Site officiel | 2026-10-25 | HTTP 404 |
| 4 | skims.com partnerships | https://skims.com/pages/partnerships | Site officiel | 2026-10-25 | HTTP 404 |
| 5 | whomakethis.com | https://whomakethis.com/who-makes-skims/ | Presse/analyse | 2026-10-25 | Fabr. Chine/Turquie (mai 2026) |
| 6 | thygesenapparel.com | https://thygesenapparel.com/blog/where-is-skims-clothing-made | Blog industriel | 2026-10-25 | Fabr. Thaïlande (sept. 2026) |
| 7 | complaintsboard.com | https://www.complaintsboard.com/skims-b135186/contacts | Annuaire | 2026-10-25 | hello@skims.com + tél — source secondaire, non confirmée |
| 8 | thezoereport.com | https://www.thezoereport.com/fashion/october-2026-fashion-news | Presse mode | 2026-10-25 | Lancement Skims Alpine (oct. 2026) |
| 9 | skimsglobal.com | https://skimsglobal.com/global-manufacturing-network.html | Site tiers | 2026-10-25 | **Autre entreprise (pharma)** — signalée pour éviter confusion |
| 10 | ddgs | recherche "SKIMS supply chain sourcing Asia" | Moteur | 2026-10-25 | 5 résultats utilisés |
