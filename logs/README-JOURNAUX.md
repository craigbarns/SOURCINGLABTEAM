# Journaux SOURCING LAB AI — Spécification

Toutes les missions produisent 3 journaux tracables et auditables commercialement.

## 1. mission-*.json — Journal maître
- `mission_id` format `SRC-YYYYMMDD-NNN` (ex: SRC-20261024-001)
- Timestamps ISO8601 début/fin par phase (T1 hunter, T2 auditor, T2B correction, T3 rfq, T4 synthèse)
- `duree_sec`, `cout_api_estime_usd`, `taux_reussite`, `pourcentage_source`, `boucles_correction`
- `erreurs[]` agrégées

## 2. sources-*.csv — Traçabilité URLs
`séparateur ; UTF-8-SIG`
`timestamp;agent;url;http_status;taille_octets;usage;fichier_archive`
Chaque `curl -L + html2text` loggé. Objectif: un auditeur externe peut rejouer chaque extraction.

## 3. erreurs-*.csv — Suivi qualité
`séparateur ; UTF-8-SIG`
`timestamp;agent;gravité;description;action;statut`
Gravités: `Bloquant` (arrête validation), `Majeur` (corriger avant GO), `Mineur` (noté, non bloquant)
Statuts: `ouvert → corrigé → escaladé`

## Règles
- Original jamais modifié — corrections = v2, v3 avec diff
- 1 boucle correction max (Hunter → Auditor) avant escalade
- Tous les fichiers survivent reboot (pas de /tmp seul)
