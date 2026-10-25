# 🎯 STANDARDS AGENTS — Sourcing Lab Team
*Inspiré du protocole REA 6.7.0 (rapport grok-bot-rea-2026-10-25) — niveau de rigueur cible pour tous les agents.*

## Les 7 principes non négociables

### 1. Traçabilité totale (pattern: "extraction manifest")
Chaque mission génère un journal horodaté (`logs/mission-YYYYMMDD-HHMM.json`) contenant :
- L'objectif initial, tel que reçu (verbatim)
- Chaque étape exécutée avec horodatage et résultat
- Le statut final et le coût API estimé

### 2. Preuves sourcées (pattern: "evidence bundle")
Toute donnée affichée dans un livrable doit référencer sa source :
- URL exacte de la page consultée
- Date de consultation
- Type de preuve : `documenté` (page officielle, données douanières) vs `déclaré` (site de l'entreprise, presse) vs `supposé` (inférence)
- Journal des sources : `logs/sources-YYYYMMDD.csv`

### 3. Distinction fait/supposition (pattern: "reconstruit vs inconnu")
Interdiction absolue de présenter une inférence comme un fait. Chaque livrable inclut une section :
| Question | État | Preuve |
|---|---|---|
| Besoin sourcing démontré ? | Oui/Non/Supposé | source |
Cette distinction est codée dans les scores : les besoins "démontrés" valent +20 pts vs "supposés" +5 pts.

### 4. Politique d'intégrité "record-and-continue" (pattern: "observed-untrusted")
Quand une donnée est incohérente (ex: domaine suspect `wildone.club` vs officiel `wildone.com`) :
- NE PAS bloquer la mission
- ENREGISTRER l'anomalie dans le journal avec un statut explicite
- CONTINUER avec la donnée la plus fiable, en le documentant
- Créer un avertissement de sécurité visible dans le livrable final

### 5. Auto-validation systématique (pattern: "offsets vérifiés contre les octets")
Avant toute livraison, l'agent vérifie son propre travail :
- Les fichiers générés existent-ils ? (taille > 0, lisible)
- Les données correspondent-elles aux sources déclarées ? (spot-check 20%)
- Les formats sont-ils conformes à la demande ? (Excel, CSV, etc.)
- Le nombre d'items correspond-il à la demande ? (10 prospects = 10 lignes)

### 6. Scope honnête (pattern: "ce qui reste inconnu")
Chaque livrable final se termine par un tableau "Couverture" :
| Ce qui est établi | Ce qui est partiel | Ce qui reste inconnu |
Les agents ne prétendent JAMAIS avoir couvert 100% sans preuve.

### 7. Sécurité des identifiants et des contacts
- Aucun mot de passe en clair dans les journaux ou livrables
- Aucun contact avec les prospects sans validation humaine explicite
- Les coordonnées ne proviennent que de sources publiques

## Checklist de sortie de mission (à exécuter avant de rendre le rapport)
- [ ] Journal de traçabilité créé et horodaté
- [ ] Chaque donnée a une source dans le journal des sources
- [ ] Les besoins sont marqués démontrés/déclarés/supposés
- [ ] Les anomalies enregistrées avec statut (record-and-continue)
- [ ] Auto-validation des livrables effectuée
- [ ] Tableau de couverture (établi/partiel/inconnu) inclus
- [ ] Coût API estimé communiqué
- [ ] Aucun contact non autorisé effectué
- [ ] Sécurité : aucun identifiant exposé dans les livrables

## Application aux agents existants
| Agent | Amélioration appliquée |
|---|---|
| supplier-hunter | Chaque fabricant : source + date + type de preuve. Les "capacités déclarées" vs "vérifiées" sont distinguées |
| supplier-auditor | Score composite : fiabilité douanière (40) + certifications (30) + preuve d'activité récente (20) + conformité export (10) |
| us-lead-hunter | Mêmes standards que supplier-hunter. Score de qualification distinguant besoin démontré vs supposé |
| rfq-analyst | Chaque ligne de devis sourcée du PDF original (page + cellule). Rien ne doit être tapé manuellement sans source |
| sourcing-manager | Orchestre les standards ci-dessus ; journalise les anomalie et l'auto-validation de chaque subagent |
