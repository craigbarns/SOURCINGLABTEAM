# 📈 PLAYBOOK — Analyse de tendances (trend-hunter)

*Conventions obligatoires pour toute mission de veille tendances. Distinguer systématiquement : intérêt de recherche, visibilité et ventes (cf. Google Trends support, Amazon Best Sellers Rank docs).*

## 1. Principe cardinal : recherche actuelle obligatoire
- Relever la **date/heure de démarrage** de la mission
- Effectuer de **nouvelles recherches web** à chaque demande
- Les connaissances du modèle et les anciens rapports = **contexte, jamais preuve**
- Distinguer **date de consultation** (quand on a regardé) et **période couverte** (ce que les données mesurent)

## 2. Les 3 types de signaux — ne jamais les mélanger

| Signal | Exemples de mesures | Pièges |
|---|---|---|
| **Attention sociale** | vues TikTok, posts, engagement | des vues ≠ des ventes ; une viralité ≠ une demande d'achat |
| **Intérêt de recherche** | indice Google Trends (relatif, 0-100), requêtes associées | un indice Trends ≠ volume absolu ; comparer seulement même zone + même période |
| **Signal commercial** | classement Amazon (BSR, Movers & Shakers), lancements produits | un classement ≠ unités vendues ; une pub visible ≠ rentabilité ; un best-seller établi ≠ tendance émergente |

### Règles de comparaison
- Même marché, même indicateur, même périmètre, même méthode de normalisation
- Croissance calculée **seulement** si valeurs + périodes disponibles et comparables
- Référence nulle ou inconnue → **pas de pourcentage** (« non calculable »)

## 3. Corroboration et classification
- **≥ 2 sources indépendantes** pour « corroborée » ; articles reprenant la même étude = 1 preuve
- Source consultée aujourd'hui ≠ données d'aujourd'hui : toujours contrôler la date des données
- Phases : `émergente / en croissance / établie / en essoufflement / phase indéterminée`
- Données insuffisantes → `signal à confirmer` (livrer quand même, sans surévaluer)
- Qualité avant quantité : 4 tendances bien documentées > 10 fragiles

## 4. Distinguer conclusion et preuve
Pour chaque conclusion :
- **Fait observé** : mesure relevée, URL, date
- **Interprétation** : ce qu'on en déduit (assumé)
- **Hypothèse** : supposition à tester
- **Inconnu** : ce qu'on ne peut pas établir

## 5. Modèle de preuve (chaque source consignée dans logs/sources-*.csv)
`URL exacte | plateforme | extrait ou mesure | unité | période | pays | date de consultation | limite éventuelle`

**Limites à consigner explicitement** : page nécessitant connexion/export/navigateur → « inaccessible + raison ». Extrait de moteur de recherche ≠ consultation complète de la source.

## 6. Grille d'opportunité Sourcing Lab USA (par tendance)
1. Produit / caractéristiques concernés
2. Public et marché observés
3. Marques ou acteurs qui l'illustrent
4. Preuves de progression
5. Indices de saisonnalité / saturation
6. Adéquation avec notre offre
7. Informations nécessaires pour vérifier la faisabilité
8. Prochaine action commerciale ou sourcing
9. **Compatibilité délais** : échantillons + production vs durée de l'opportunité (si inconnu → le signaler)

**Interdits** : inventer coût usine, MOQ, marge, chiffre d'affaires, garantie de succès. Une marque qui suit une tendance ≠ prospect automatique.

## 7. Format du tableau principal (rapport MD)
`Tendance | Marché | Phase | Signaux sociaux | Recherches | Signaux commerciaux | Évolution mesurée et période | Confiance justifiée | Opportunité Sourcing Lab USA | Limites | Prochaine action | Sources`

## 8. Livrables de mission (dossier unique `missions/YYYY-MM-DD-trends-<secteur>-<marché>/`)
- `rapport-tendances-YYYY-MM-DD.md`
- `tendances-YYYY-MM-DD.csv` (`;`, UTF-8-SIG)
- `observations-YYYY-MM-DD.json`
- `logs/sources-YYYY-MM-DD.csv`

**Conclusion obligatoire du rapport** :
- Les 3 opportunités les mieux étayées
- Les signaux à surveiller
- Les conclusions encore impossibles à établir

## 9. Passage aux autres agents (uniquement sur demande explicite)
- brief-engineer (CDC) / supplier-hunter (capacité fabrication) / us-lead-hunter-v2 (acheteurs) / lead-auditor (vérification commerciale)
- **Jamais** de contact commercial ni d'envoi d'email depuis trend-hunter

## 10. Checklist de sortie de mission
- [ ] Date/heure de démarrage relevées et consignées
- [ ] Nouvelles recherches effectuées (pas de recyclage d'anciens rapports)
- [ ] Filtres (pays, catégorie, période) enregistrés
- [ ] 3 types de signaux séparés par tendance
- [ ] Croissances calculées uniquement sur données comparables
- [ ] ≥ 2 sources indépendantes pour les tendances « corroborées »
- [ ] Phases attribuées (ou « signal à confirmer »)
- [ ] Faits/interprétations/hypothèses/inconnus distingués
- [ ] Sources inaccessibles signalées
- [ ] Aucun volume de ventes déduit d'un classement
- [ ] Fichiers MD/CSV/JSON/sources lisibles
- [ ] Aucun contact commercial effectué
